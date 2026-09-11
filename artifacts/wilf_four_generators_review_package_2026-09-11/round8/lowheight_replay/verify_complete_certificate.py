#!/usr/bin/env python3
"""Full independent low-degree replay by default; no LP solver required."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument("--records-only", action="store_true",
                    help="Compare existing records without executing the independent verifier.")
args = parser.parse_args()
run_summary = None
if not args.records_only:
    with tempfile.TemporaryDirectory(prefix="wilf_degree6_audit_") as temp:
        exe = Path(temp) / "independent_verify"
        subprocess.run(["g++", "-O3", "-std=c++17",
                        str(HERE / "independent_verify.cpp"), "-o", str(exe)], check=True)
        result = subprocess.run([str(exe), str(HERE)], check=True, text=True,
                                stdout=subprocess.PIPE)
        run_summary = json.loads(result.stdout.strip())
        assert run_summary == {
            "status": "passed", "profiles": 1429, "bases": 5733,
            "exact_weighted_duals": 3361434, "floating_point_used": False
        }, run_summary

def records(name):
    return [json.loads(line) for line in (HERE / name).read_text().splitlines()]

original = records("certification.jsonl")
independent = records("independent_verification.jsonl")
assert len(original) == len(independent) == 9
expected_corners = [(a,b,P-a-b)
                    for P in range(5,8)
                    for a in range(1,P+1)
                    for b in range(a,P+1)
                    if P-a-b >= b]
for pid, (source, replay, corner) in enumerate(zip(original, independent, expected_corners)):
    assert source["pid"] == replay["pid"] == pid
    assert source["corner"] == replay["corner"] == list(corner)
    for key, value in replay.items():
        assert source[key] == value, (pid, key, source[key], value)
    assert sum(replay["histogram"].values()) == replay["remaining"]
    assert replay["q_ok"] == replay["six_maxima"] + replay["remaining"]
    assert replay["certificate_min_numerator"] >= 0
    assert replay["certificate_min_denominator"] > 0

keys = ["compatible", "degree_ok", "m30", "erosion_ok", "q_ok",
        "six_maxima", "remaining"]
totals = {key: sum(row[key] for row in independent) for key in keys}
assert totals == {
    "compatible": 55199298, "degree_ok": 17808013, "m30": 17727110,
    "erosion_ok": 12575521, "q_ok": 3742041, "six_maxima": 380607,
    "remaining": 3361434
}, totals
assert (HERE / "dual_assignments.bin").stat().st_size == 4 * totals["remaining"]
assert len(records("dual_bases.jsonl")) == 5733
# Exact strict comparison underlying the m>=30 integer-slack implication.
assert 90 * 10 > 29 * 31
names = ["independent_verify.cpp", "verify_complete_certificate.py",
         "dual_bases.jsonl", "dual_assignments.bin", "certification.jsonl",
         "independent_verification.jsonl"]
report = {
    "status": "passed",
    "full_independent_recomputation_this_run": not args.records_only,
    "run_summary": run_summary,
    "all_coverage_fields_and_histograms_match": True,
    "totals": totals,
    "exact_weighted_target": "D >= m - 29/10 for every weight vector >= (1,1,1), with M<=7",
    "binary_assignment_encoding": "explicit little-endian unsigned 32-bit",
    "file_sha256": {name: hashlib.sha256((HERE / name).read_bytes()).hexdigest()
                    for name in names},
    "scope": "Degree<=6 residual ideal class only. Excluded shapes use the named prior theorems and necessary arithmetic filters."
}
(HERE / "complete_independent_verification.json").write_text(
    json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
