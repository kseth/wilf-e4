#!/usr/bin/env python3
"""Replay every supplementary low-height certificate; never regenerate proofs."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile


def main():
    root = Path(__file__).resolve().parent
    manifest = json.loads((root / 'certificate_manifest.json').read_text())
    for name, metadata in manifest.items():
        data = (root / name).read_bytes()
        assert len(data) == metadata['bytes'], f'length mismatch: {name}'
        assert hashlib.sha256(data).hexdigest() == metadata['sha256'], f'hash mismatch: {name}'
    compiler = os.environ.get('CXX') or shutil.which('c++') or shutil.which('g++')
    if not compiler:
        raise RuntimeError('A C++17 compiler is required.')
    # An isolated temporary directory keeps certificate inputs and old records unchanged.
    with tempfile.TemporaryDirectory(prefix='wilf-sixmax-verify-') as directory:
        working = Path(directory)
        for name in ('dual_bases.jsonl', 'dual_assignments.bin'):
            shutil.copy2(root / name, working / name)
        binary = working / 'verifier'
        subprocess.run([compiler, '-O3', '-std=c++17', str(root / 'independent_verify_sixmax.cpp'), '-o', str(binary)], check=True)
        process = subprocess.run([str(binary), str(working)], check=True, text=True, stdout=subprocess.PIPE)
        result = json.loads(process.stdout)
        assert result == {'status': 'passed', 'profiles': 1429, 'bases': 4513, 'exact_weighted_duals': 380607, 'floating_point_used': False}, result
        actual = [json.loads(line) for line in (working / 'independent_verification.jsonl').read_text().splitlines()]
        expected = [json.loads(line) for line in (root / 'independent_verification.jsonl').read_text().splitlines()]
        producer = [json.loads(line) for line in (root / 'certification.jsonl').read_text().splitlines()]
        assert actual == expected, 'independent replay records differ from preserved records'
        assert len(actual) == len(producer) == 9
        for independent, generated in zip(actual, producer):
            for key, value in independent.items():
                assert generated[key] == value, (independent['pid'], key)
        assert sum(row['remaining'] for row in actual) == 380607
        result['manifest_files_verified'] = len(manifest)
        result['all_counts_and_histograms_match'] = True
        result['regenerated_certificates'] = False
        print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
