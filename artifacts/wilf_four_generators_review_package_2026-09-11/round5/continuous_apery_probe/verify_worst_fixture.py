#!/usr/bin/env python3
"""Exact independent check of the bounded diagnostic's best fixture."""
import heapq
import json
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
record_path = ROOT / (sys.argv[1] if len(sys.argv) > 1 else "targeted_probe_results.json")
record = json.loads(record_path.read_text())
m, *weights = record["best_generators"]
best = [None] * m
best[0] = (0, (0, 0, 0))
heap = [(0, (0, 0, 0), 0)]
while heap:
    value, exponent, residue = heapq.heappop(heap)
    if best[residue] != (value, exponent):
        continue
    for j, weight in enumerate(weights):
        nxt = list(exponent)
        nxt[j] += 1
        nxt = tuple(nxt)
        target = (residue + weight) % m
        candidate = (value + weight, nxt)
        if best[target] is None or candidate < best[target]:
            best[target] = candidate
            heapq.heappush(heap, (candidate[0], nxt, target))

assert all(item is not None for item in best)
T = {p for value, p in best}
M = max(value for value, p in best)
total = sum(value for value, p in best)
s = sum(weights)
assert M == record["maximum_apery"] and total == record["sum_apery"]
excluded = set()
for p in T:
    for j in range(3):
        q = list(p)
        q[j] += 1
        q = tuple(q)
        if q in T:
            continue
        predecessors = []
        for k in range(3):
            if q[k]:
                z = list(q)
                z[k] -= 1
                predecessors.append(tuple(z))
        if all(z in T for z in predecessors):
            excluded.add(q)
interior = sorted(q for q in excluded if all(q))
criterion = 6 * total - 4 * m * M - m * s
assert criterion == record["exact_failure_numerator"]
mu = Fraction(2 * total + m * s, 2 * m * (M + s))
conductor = M - m + 1
wilf_numerator = 3 * m * M - 4 * total - m * (m - 1)
assert wilf_numerator % m == 0

result = {
    "status": "PASS",
    "generators": [m] + weights,
    "conductor": conductor,
    "wilf_number": wilf_numerator // m,
    "apery_maximum": M,
    "apery_sum": total,
    "cell_normalized_mean": str(mu),
    "cell_normalized_mean_decimal": float(mu),
    "exact_failure_numerator": criterion,
    "refutes_continuous_bound": criterion > 0,
    "preferred_lex_interior_corners": interior,
    "all_minimal_excluded_exponents": sorted(excluded),
    "apery_by_residue": [{"value": v, "exponent": p} for v, p in best],
    "scope": "One exact fixture and a bounded diagnostic; no universal proof.",
}
(ROOT / (record_path.stem + "_fixture_exact.json")).write_text(json.dumps(result, indent=2) + "\n")
for key in ("generators", "wilf_number", "cell_normalized_mean", "exact_failure_numerator",
            "preferred_lex_interior_corners", "refutes_continuous_bound"):
    print(key, result[key])
