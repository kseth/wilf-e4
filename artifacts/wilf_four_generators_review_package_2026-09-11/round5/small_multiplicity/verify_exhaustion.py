#!/usr/bin/env python3
"""Compare both exhaustive certificates, optionally rebuilding/rerunning them.

python3 verify_exhaustion.py            # check recorded certificates
python3 verify_exhaustion.py --rerun    # compile both C++17 programs and rerun
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
EXPECTED = {
    "raw_triples": 301098092,
    "minimal_four_generator_semigroups": 180719029,
    "maximum_apery_within_bound": 7326992,
    "negative_wilf_count": 0,
}


def read_records(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line]


def compare(first, second):
    assert [x["m"] for x in first] == list(range(20, 30))
    assert [x["m"] for x in second] == list(range(20, 30))
    for a, b in zip(first, second):
        for key, value in b.items():
            if key != "elapsed_seconds":
                assert a[key] == value, (a["m"], key, a[key], value)
        m = a["m"]
        B = m * (m - 2)
        n = B - m
        assert a["generator_bound_inclusive"] == B
        assert a["raw_triples"] == n * (n - 1) * (n - 2) // 6
        assert a["raw_triples"] == sum(a[key] for key in (
            "smallest_redundant", "middle_redundant", "largest_redundant",
            "nontrivial_gcd", "minimal_four_generator_semigroups"))
        assert a["negative_wilf_count"] == a["zero_wilf_count"] == 0
        # Direct unbounded-by-generator witness validation by integer DP.
        gens = a["bounded_minimum_example"]
        membership = [True] + [False] * B
        for i in range(1, B + 1):
            membership[i] = any(i >= g and membership[i - g] for g in gens)
        assert all(membership[B - m + 1:])
        conductor = max(i for i, present in enumerate(membership) if not present) + 1
        genus = membership.count(False)
        wilf = 3 * conductor - 4 * genus
        assert wilf == a["minimum_wilf_with_bounded_apery"]
    for key, expected in EXPECTED.items():
        assert sum(x[key] for x in first) == expected


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rerun", action="store_true")
    args = parser.parse_args()
    first = read_records(ROOT / "exhaustive_m20_m29.jsonl")
    second = read_records(ROOT / "independent_m20_m29.jsonl")
    compare(first, second)
    if args.rerun:
        with tempfile.TemporaryDirectory(prefix="wilf_m20_m29_") as tmp:
            reruns = []
            for stem, expected in (
                ("exhaust_small_multiplicity", first),
                ("independent_membership_check", second),
            ):
                binary = Path(tmp) / stem
                subprocess.run(["g++", "-O3", "-std=c++17", "-Wall", "-Wextra",
                                "-pedantic", str(ROOT / (stem + ".cpp")),
                                "-o", str(binary)], check=True)
                result = subprocess.run([str(binary), "20", "29"], check=True,
                                        capture_output=True, text=True)
                actual = [json.loads(line) for line in result.stdout.splitlines()]
                compare(expected, actual)
                reruns.append(actual)
            compare(*reruns)
    summary = {
        "status": "PASS",
        "multiplicity_interval_inclusive": [20, 29],
        "all_embedding_dimension_four": True,
        "depends_on_proved_conductor_reduction": True,
        "algorithms": ["cyclic residue shortest paths", "integer semigroup membership"],
        "totals": EXPECTED,
        "sources_sha256": {
            p.name: hashlib.sha256(p.read_bytes()).hexdigest()
            for p in [ROOT / "exhaust_small_multiplicity.cpp",
                      ROOT / "independent_membership_check.cpp"]
        },
        "compiled_and_reran_this_invocation": args.rerun,
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
