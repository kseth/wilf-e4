#!/usr/bin/env python3
"""Check completion and provenance of this review's observed full replays.

This checks saved results and exact byte identities. It does not rerun the
dynamic programs or rational dual assignments; their fresh run commands are
listed in the corresponding theorem and audit notes.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent.parent


def read(name):
    return json.loads((ROOT / name).read_text())


def digest(name):
    return hashlib.sha256((ROOT / name).read_bytes()).hexdigest()


def main():
    low = read('round8/lowheight_replay/complete_independent_verification.json')
    assert low['status'] == 'passed'
    assert low['full_independent_recomputation_this_run'] is True
    assert low['all_coverage_fields_and_histograms_match'] is True
    assert low['run_summary']['exact_weighted_duals'] == 3361434
    assert low['run_summary']['floating_point_used'] is False
    for name, expected in low['file_sha256'].items():
        assert digest('round8/lowheight_replay/' + name) == expected, name

    supplement = read('round8/simplification/complete_checks.json')
    assert supplement['status'] == 'passed'
    assert supplement['exact_weighted_duals'] == 380607
    assert supplement['floating_point_used'] is False
    assert supplement['coverage_counts_and_histograms_match'] is True
    assert supplement['combined_dual_covered_shapes'] == 3742041
    manifest = read('round8/simplification/certificate_manifest.json')
    for name, metadata in manifest.items():
        target = ROOT / 'round8/simplification' / name
        assert target.stat().st_size == metadata['bytes'], name
        assert digest(str(target.relative_to(ROOT))) == metadata['sha256'], name
    partition = read('round8/root_supplement_audit.json')
    assert partition['status'] == 'PASS'
    assert partition['complementary_maxima_partition'] is True

    high_name = 'round8/high_height_replay/independent_residual_complete_checks.json'
    high = read(high_name)
    assert high['status'] == 'PASS' and high['scope'] == 'complete tree'
    assert high['dp_leaves_replayed'] == high['total_verified_leaves'] == 47088
    assert high['cached_verified_leaves'] == 0 and high['cached_corner_cases'] == 0
    assert high['sampled'] is False and high['coverage_only'] is False
    assert high['independent_corner_cases'] == 35852138
    assert high['coverage'] == {
        'split': 47229, 'dp': 47088, 'empty': 142, 'pending': 0, 'unresolved': 0,
    }
    certificate = 'round8/high_height_replay/residual_parallel_interval_certificate.json'
    expected = '173fe6ec196b3d2adabad313749482542ad3492b5f6b4e398e76bbe6e52e405c'
    assert digest(certificate) == high['certificate_sha256'] == expected
    assert digest('round7/geometric_residual/residual_parallel_interval_certificate.json') == expected
    for name in ('verify_residual_certificate.py', 'independent_residual_worker.cpp',
                 'independent_residual_point_worker.cpp', 'independent_specialized_piece_worker.cpp'):
        assert digest('round8/high_height_replay/' + name) == digest('round7/geometric_residual/' + name), name

    audits = ['structure', 'phase', 'lowheight', 'sixpoint', 'computation']
    note_hashes = {}
    for name in audits:
        path = 'round8/audit_' + name + '.md'
        assert (ROOT / path).is_file()
        note_hashes[path] = digest(path)

    result = {
        'status': 'PASS',
        'date': '2026-09-11',
        'scope': 'Completion and provenance of the fresh in-session review; recorded full computations are not rerun by this script.',
        'fresh_original_low_height_duals': 3361434,
        'fresh_supplementary_low_height_duals': 380607,
        'combined_direct_low_height_duals': 3742041,
        'fresh_high_height_leaves': 47088,
        'high_height_cached_leaves': 0,
        'fresh_high_height_cartesian_cases': 35852138,
        'high_height_certificate_sha256': expected,
        'unresolved_high_height_nodes': 0,
        'six_point_dependency_removed_from_residual_low_height_branch': True,
        'six_point_dependency_retained_for_corner_111': True,
        'external_mathematical_review_performed': False,
        'proof_assistant_formalization_performed': False,
        'audit_note_sha256': note_hashes,
        'full_high_replay_report_sha256': digest(high_name),
    }
    (ROOT / 'round8/final_review_completion.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
