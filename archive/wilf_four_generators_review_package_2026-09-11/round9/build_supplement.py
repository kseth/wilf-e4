#!/usr/bin/env python3
"""Package the new research supplement; no compiled executables or old streams."""
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "deliverables/wilf_simplification_and_higher_dimensions_checks_2026-09-11.zip"
ALLOWED = {".py", ".cpp", ".hpp", ".md", ".json", ".jsonl", ".bin", ".txt", ".tsv"}
payloads = {
    p.relative_to(ROOT).as_posix(): p
    for p in (ROOT / "round9").rglob("*")
    if p.is_file()
    and p.suffix in ALLOWED
    and "__pycache__" not in p.parts
    and p.name not in {"package_verification.json", "package_manifest.json"}
}
for name in (
    "deliverables/wilf_simplification_and_higher_dimensions_2026-09-11.md",
    "deliverables/wilf_fixed_dimension_finite_reduction_2026-09-05.md",
    "round7/low_degree6/low_height_theorem.md",
    "round7/low_degree6/certify_all.cpp",
    "round7/low_degree6/independent_verify.cpp",
    "round7/global_step_audit.md",
    "round7/erosion_fixture.md",
):
    payloads[name] = ROOT / name
manifest = {}
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for name, path in sorted(payloads.items()):
        data = path.read_bytes()
        manifest[name] = {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}
        archive.writestr(name, data)
    archive.writestr("MANIFEST_SHA256.json", json.dumps(manifest, indent=2) + "\n")
with zipfile.ZipFile(OUT) as archive:
    assert archive.testzip() is None
    archived = json.loads(archive.read("MANIFEST_SHA256.json"))
    assert set(archive.namelist()) == set(archived) | {"MANIFEST_SHA256.json"}
    for name, expected in archived.items():
        data = archive.read(name)
        assert len(data) == expected["bytes"], name
        assert hashlib.sha256(data).hexdigest() == expected["sha256"], name
result = {
    "status": "passed",
    "payloads": len(manifest),
    "archive_bytes": OUT.stat().st_size,
    "archive_sha256": hashlib.sha256(OUT.read_bytes()).hexdigest(),
    "all_payload_hashes_checked": True,
    "full_certificate_replayed_during_packaging": False,
    "full_replay_record": "round9/height_free_duals/portable_full_replay_result.json",
}
(ROOT / "round9/package_verification.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
