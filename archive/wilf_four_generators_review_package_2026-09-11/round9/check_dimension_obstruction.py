"""Exact, small checks for genuine five-generator Apéry obstructions.

Run with the Python standard library. No Wilf counterexample is asserted.
"""
from heapq import heappop, heappush
from itertools import product
import json
from pathlib import Path


def check(m, weights, allowed):
    d = len(weights)
    zero = (0,) * d
    T = {x for x in product(range(2), repeat=d) if allowed(x)}
    assert len(T) == m
    label = lambda x: sum(a * t for a, t in zip(weights, x))
    assert {label(x) % m for x in T} == set(range(m))
    # Independent shortest paths give the actual Apéry values.
    dist = [10**12] * m
    dist[0] = 0
    queue = [(0, 0)]
    while queue:
        value, residue = heappop(queue)
        if value != dist[residue]:
            continue
        for a in weights:
            nr = (residue + a) % m
            nv = value + a
            if nv < dist[nr]:
                dist[nr] = nv
                heappush(queue, (nv, nr))
    assert {label(x) for x in T} == set(dist)
    # Literal bounded membership establishes the five listed generators
    # are minimal; every possible summand is positive.
    gens = [m] + list(weights)
    for excluded, target in enumerate(gens):
        attainable = [False] * (target + 1)
        attainable[0] = True
        for value in range(target + 1):
            if attainable[value]:
                for i, a in enumerate(gens):
                    if i != excluded and value + a <= target:
                        attainable[value + a] = True
        assert not attainable[target]
    corners = []
    for x in product(range(3), repeat=d):
        if x in T:
            continue
        if all(tuple(t - (j == i) for j, t in enumerate(x)) in T
               for i in range(d) if x[i]):
            corners.append(x)
    assert not any(all(x) for x in corners)
    # Every forbidden minimal monomial has a strictly cheaper residue
    # representative, hence every point outside T is outside the Apéry set.
    reductions = []
    for x in corners:
        value = label(x)
        representative = next(y for y in T if label(y) % m == value % m)
        delta = value - label(representative)
        assert delta > 0 and delta % m == 0
        reductions.append({"excluded": x, "representative": representative,
                           "multiplicity_copies": delta // m})
    conductor = max(dist) - m + 1
    n = sum(1 for value in range(conductor) if value >= dist[value % m])
    return {"multiplicity": m, "coordinate_weights": weights,
            "generators_sorted": sorted(gens), "apery_sorted": sorted(dist),
            "ideal_size": len(T), "minimal_excluded": corners,
            "strict_reductions": reductions, "conductor": conductor,
            "left_elements": n, "wilf_number": 5 * n - conductor,
            "minimal_embedding_dimension": len(gens)}


cycle = check(9, (19, 20, 12, 15),
              lambda x: x[0] + x[1] <= 1 and x[2] + x[3] <= 1)
triple = check(14, (29, 30, 32, 21),
               lambda x: not all(x[:3]))
assert len(cycle["minimal_excluded"]) == 6
assert len(triple["minimal_excluded"]) == 5

T_cycle = {x for x in product(range(2), repeat=4)
           if x[0] + x[1] <= 1 and x[2] + x[3] <= 1}
edges = []
for i in range(4):
    for j in range(i + 1, 4):
        if tuple(int(k in (i, j)) for k in range(4)) in T_cycle:
            edges.append([i + 1, j + 1])
assert edges == [[1, 3], [1, 4], [2, 3], [2, 4]]
cycle["unit_level_graph_edges"] = edges
# Any alleged central box has its upper corner in T. At least one point
# then exceeds that corner in two coordinates, excluding four-horn form.
assert all(any(sum(x[i] > center[i] for i in range(4)) >= 2
               for x in T_cycle) for center in T_cycle)
cycle["no_central_box_plus_coordinate_horns"] = True

T_triple = {x for x in product(range(2), repeat=4) if not all(x[:3])}
for i in range(4):
    for j in range(i + 1, 4):
        assert {(x[i], x[j]) for x in T_triple} == set(product(range(2), repeat=2))
triple["all_pair_projections_full_boolean_square"] = True

report = {"status": "PASS", "chordless_cycle": cycle,
          "support_three_exclusion": triple}
out = Path(__file__).with_name("dimension_obstruction_checks.json")
out.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
