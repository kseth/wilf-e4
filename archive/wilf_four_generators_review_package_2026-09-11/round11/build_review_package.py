#!/usr/bin/env python3
"""Assemble and validate the consolidated Wilf review package.

Packaging/hash validation only: this program never runs a mathematical verifier.
The build expects the original workspace and its legacy ZIP. An extracted
package can validate its payload using --verify-extracted.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
LEGACY_DEFAULT = ROOT / 'deliverables/wilf_four_generator_proofs_and_certificates_2026-09-10.zip'
OUTPUT_DEFAULT = ROOT / 'deliverables/wilf_four_generators_review_package_2026-09-11.zip'
REPORT_DEFAULT = ROOT / 'round11/review_package_validation.json'
README_SOURCE = 'round11/REVIEW_PACKAGE_README.md'
PROOF_MAP = 'round11/proof_map.md'
MAIN_DOCUMENTS = (
    'deliverables/wilf_four_generators_review_manuscript_2026-09-11.md',
    'deliverables/wilf_four_generators_review_manuscript_2026-09-11.pdf',
    'deliverables/wilf_simplification_and_higher_dimensions_2026-09-11.md',
    'deliverables/wilf_centroid_local_constructions_2026-09-11.md',
)
LEGACY_RENAMES = {
    'MANIFEST.json': 'archive_notes/legacy_2026-09-10_MANIFEST.json',
    'README.md': 'archive_notes/legacy_2026-09-10_README.md',
}
EXCLUDED_PARTS = {'__pycache__', 'pdf_build', '.git', '.pytest_cache', 'node_modules'}
EXCLUDED_SUFFIXES = {
    '.pyc', '.pyo', '.o', '.a', '.so', '.dll', '.dylib', '.exe',
    '.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg', '.tiff', '.bmp',
    '.aux', '.log', '.toc', '.out', '.fdb_latexmk', '.fls', '.synctex',
    '.tmp', '.temp', '.bak',
}
EXCLUDED_ROUND11_NAMES = {
    'review_package_validation.json',
    'review_package_build_stdout.txt',
}
PROOF_REF = re.compile(r'`((?:round[0-9]+|prior|deliverables)/[^`]+)`')


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_name(name: str) -> str:
    p = PurePosixPath(name)
    require(not p.is_absolute() and '..' not in p.parts and '\\' not in name,
            f'Unsafe archive path: {name!r}')
    require(name and not name.endswith('/'), f'Not a payload path: {name!r}')
    return str(p)


def check_expected(data: bytes, expected: object, label: str) -> None:
    if isinstance(expected, str):
        digest, size = expected, None
    else:
        require(isinstance(expected, dict), f'Unsupported manifest record: {label}')
        digest = expected.get('sha256')
        size = expected.get('bytes', expected.get('size'))
    require(isinstance(digest, str) and len(digest) == 64, f'Invalid SHA-256: {label}')
    require(sha256(data) == digest, f'SHA-256 mismatch: {label}')
    if size is not None:
        require(len(data) == size, f'Byte-count mismatch: {label}')


def read_legacy(path: Path) -> tuple[dict[str, bytes], dict[str, object]]:
    require(path.is_file(), f'Missing legacy archive: {path}')
    payload: dict[str, bytes] = {}
    with zipfile.ZipFile(path) as archive:
        for entry in archive.infolist():
            if entry.is_dir():
                continue
            name = safe_name(entry.filename)
            require(name not in payload, f'Duplicate legacy ZIP member: {name}')
            payload[name] = archive.read(entry)
    require('MANIFEST.json' in payload and 'README.md' in payload,
            'Legacy archive must contain its root MANIFEST.json and README.md')
    manifest = json.loads(payload['MANIFEST.json'])
    records = manifest.get('files')
    require(isinstance(records, dict), 'Unsupported legacy manifest')
    require(set(records) == set(payload) - {'MANIFEST.json'},
            'Legacy manifest membership does not match the legacy archive')
    for name, expected in records.items():
        check_expected(payload[name], expected, f'legacy:{name}')
    relocated = {LEGACY_RENAMES.get(name, name): data for name, data in payload.items()}
    require(len(relocated) == len(payload), 'Legacy relocation caused a path collision')
    return relocated, {
        'archive': str(path),
        'archive_sha256': sha256(path.read_bytes()),
        'original_payload_members': len(payload),
        'original_manifest_payloads_checked': len(records),
        'root_files_relocated': LEGACY_RENAMES,
    }


def include_file(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    if any(part in EXCLUDED_PARTS for part in rel.parts):
        return False
    if path.suffix.lower() in EXCLUDED_SUFFIXES or path.name.endswith('~'):
        return False
    if rel.parts[0] == 'round11':
        if path.name in EXCLUDED_ROUND11_NAMES or path.suffix.lower() == '.pdf':
            return False
        if path.name.startswith(('tmp_', 'temp_', '.')):
            return False
    with path.open('rb') as handle:
        magic = handle.read(4)
    # Extensionless executables are common in the historical work directories.
    if magic in (b'\x7fELF', b'\xcf\xfa\xed\xfe', b'\xfe\xed\xfa\xcf',
                 b'\xca\xfe\xba\xbe') or magic[:2] == b'MZ':
        return False
    return True


def add(payload: dict[str, bytes], name: str, data: bytes, *, replace: bool = False) -> None:
    name = safe_name(name)
    if name in payload and payload[name] != data and not replace:
        raise RuntimeError(f'Conflicting payload at {name}; refusing silent replacement')
    payload[name] = data


def proof_map_references(payload: dict[str, bytes]) -> set[str]:
    require(PROOF_MAP in payload, f'Missing {PROOF_MAP}')
    return {safe_name(name) for name in PROOF_REF.findall(payload[PROOF_MAP].decode('utf-8'))}


def validate_inner_manifests(payload: dict[str, bytes]) -> dict[str, int]:
    results: dict[str, int] = {}
    for name in sorted(payload):
        p = PurePosixPath(name)
        if not name.startswith('round10/') or p.suffix != '.json' or 'manifest' not in p.name.lower():
            continue
        document = json.loads(payload[name])
        if not isinstance(document, dict):
            continue
        records = document.get('files', document.get('sha256'))
        if not isinstance(records, dict):
            continue
        checked = 0
        for relative, expected in records.items():
            target = safe_name(str(p.parent / relative))
            require(target in payload, f'Inner manifest dependency missing: {name} -> {target}')
            check_expected(payload[target], expected, f'{name}:{relative}')
            checked += 1
        results[name] = checked
    require(results, 'No round10 proof manifests were validated')
    return results


def validate_payload(payload: dict[str, bytes]) -> dict[str, object]:
    require('MANIFEST.json' in payload, 'Missing root MANIFEST.json')
    manifest = json.loads(payload['MANIFEST.json'])
    records = manifest.get('files')
    require(isinstance(records, dict), 'Invalid consolidated manifest')
    require(set(records) == set(payload) - {'MANIFEST.json'},
            'Consolidated manifest membership differs from ZIP payload membership')
    for name, expected in records.items():
        check_expected(payload[name], expected, name)
    for name in MAIN_DOCUMENTS:
        require(name in payload, f'Missing principal deliverable: {name}')
    require(payload[MAIN_DOCUMENTS[1]].startswith(b'%PDF-'), 'Reading PDF is not a PDF file')
    refs = proof_map_references(payload)
    missing = sorted(refs - set(payload))
    require(not missing, f'Missing proof-map dependencies: {missing}')
    inner = validate_inner_manifests(payload)
    return {
        'status': 'passed',
        'scope': 'Payload completeness and exact SHA-256 validation only; no mathematical replay',
        'payload_files_checked': len(records),
        'payload_bytes': sum(len(payload[name]) for name in records),
        'retained_proof_map_paths_checked': len(refs),
        'round10_manifests_checked': inner,
        'mathematical_verifiers_run': False,
    }


def load_zip(path: Path) -> dict[str, bytes]:
    payload = {}
    with zipfile.ZipFile(path) as archive:
        for entry in archive.infolist():
            if entry.is_dir():
                continue
            name = safe_name(entry.filename)
            require(name not in payload, f'Duplicate ZIP member: {name}')
            payload[name] = archive.read(entry)
    return payload


def verify_extracted() -> dict[str, object]:
    manifest_path = ROOT / 'MANIFEST.json'
    require(manifest_path.is_file(), 'Run --verify-extracted from a fully extracted review package')
    document = json.loads(manifest_path.read_text())
    names = document.get('files')
    require(isinstance(names, dict), 'Invalid consolidated manifest')
    payload = {'MANIFEST.json': manifest_path.read_bytes()}
    for name in names:
        path = ROOT / safe_name(name)
        require(path.is_file(), f'Missing extracted payload: {name}')
        payload[name] = path.read_bytes()
    result = validate_payload(payload)
    result['scope'] = ('All manifest-listed extracted payloads checked; newly generated replay '
                       'outputs outside the manifest are ignored; no mathematical replay')
    return result


def build(legacy_path: Path, output: Path, report_path: Path) -> dict[str, object]:
    payload, legacy_record = read_legacy(legacy_path)
    excluded: list[str] = []
    for dirname in ('round9', 'round10', 'round11'):
        directory = ROOT / dirname
        require(directory.is_dir(), f'Missing source directory: {directory}')
        for path in sorted(directory.rglob('*')):
            if not path.is_file():
                continue
            name = path.relative_to(ROOT).as_posix()
            if include_file(path):
                add(payload, name, path.read_bytes())
            else:
                excluded.append(name)
    for name in MAIN_DOCUMENTS:
        path = ROOT / name
        require(path.is_file(), f'Principal deliverable is not ready: {path}')
        add(payload, name, path.read_bytes())
    require(README_SOURCE in payload, f'Missing current README source: {README_SOURCE}')
    add(payload, 'README.md', payload[README_SOURCE])

    # A few retained source notes were absent from the older ZIP. Preserve their
    # original paths instead of leaving a reader dependent on the workspace.
    rescued: list[str] = []
    for name in sorted(proof_map_references(payload)):
        if name not in payload:
            path = ROOT / name
            require(path.is_file(), f'Proof-map source unavailable: {name}')
            require(include_file(path), f'Proof-map dependency is excluded by policy: {name}')
            add(payload, name, path.read_bytes())
            rescued.append(name)
    validate_inner_manifests(payload)
    manifest = {
        'schema': 1,
        'date': '2026-09-11',
        'canonical_reading_manuscript': MAIN_DOCUMENTS[0],
        'status': 'Proposed computer-assisted research proof; external review outstanding',
        'scope': 'SHA-256 and payload completeness, not a fresh mathematical replay',
        'legacy_source': legacy_record,
        'additional_retained_proof_map_sources': rescued,
        'files': {name: {'sha256': sha256(data), 'bytes': len(data)}
                  for name, data in sorted(payload.items())},
    }
    payload['MANIFEST.json'] = (json.dumps(manifest, indent=2, sort_keys=True) + '\n').encode()
    validate_payload(payload)
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_name(output.name + '.tmp')
    try:
        with zipfile.ZipFile(temporary, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for name, data in sorted(payload.items()):
                info = zipfile.ZipInfo(name, date_time=(2026, 9, 11, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
        # Read the actual ZIP back: an in-memory prewrite validation is insufficient.
        result = validate_payload(load_zip(temporary))
        temporary.replace(output)
    finally:
        if temporary.exists():
            temporary.unlink()
    result.update({
        'archive': str(output),
        'archive_sha256': sha256(output.read_bytes()),
        'archive_bytes': output.stat().st_size,
        'legacy_archive_validation': legacy_record,
        'additional_retained_proof_map_sources': rescued,
        'excluded_live_tree_files': excluded,
    })
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--verify-existing', type=Path, metavar='ZIP',
                      help='Verify a consolidated ZIP without rebuilding or mathematical replay')
    mode.add_argument('--verify-extracted', action='store_true',
                      help='Validate manifest-listed files in this extracted package')
    parser.add_argument('--legacy-archive', type=Path, default=LEGACY_DEFAULT)
    parser.add_argument('--output', type=Path, default=OUTPUT_DEFAULT)
    parser.add_argument('--report', type=Path, default=REPORT_DEFAULT)
    args = parser.parse_args()
    if args.verify_existing:
        result = validate_payload(load_zip(args.verify_existing))
        result['archive_sha256'] = sha256(args.verify_existing.read_bytes())
    elif args.verify_extracted:
        result = verify_extracted()
    else:
        result = build(args.legacy_archive, args.output, args.report)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    try:
        main()
    except (RuntimeError, OSError, ValueError, zipfile.BadZipFile) as error:
        print(f'Package validation failed: {error}', file=sys.stderr)
        raise SystemExit(1)
