#!/usr/bin/env python3
"""Exact arithmetic audit of a residual-corner geometric counterexample.

This is NOT a numerical semigroup and NOT a counterexample to Wilf.
The construction and all checks are independent of the optimizing DP.
"""
import json
from itertools import product
from pathlib import Path


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def main():
    heights = [[6, 5, 4, 3, 2, 1], [4, 4, 2, 2], [3, 3, 2], [2, 2], [2], [1]]
    T = {(x, y, z) for x, row in enumerate(heights)
         for y, height in enumerate(row) for z in range(height)}
    units = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    for x in T:
        for i in range(3):
            if x[i]:
                assert sub(x, units[i]) in T
    boundary = {add(x, e) for x in T for e in units} - T
    corners = sorted(x for x in boundary
                     if all(sub(x, units[i]) in T for i in range(3) if x[i]))
    p = (1, 2, 2)
    assert [x for x in corners if all(x)] == [p]
    m = len(T)
    M = max(map(sum, T))
    sigma = sum(map(sum, T))
    D = 3 * m * M - 4 * sigma
    assert (m, M, sigma, D, m - D) == (48, 5, 170, 40, 8)
    assert D < m - 1 and 10 * (m - D) > 29

    planes = []
    for i in range(3):
        mixed = [x for x in corners if not x[i] and sum(t > 0 for t in x) == 2]
        dominating = [x for x in mixed if all(x[j] >= p[j] for j in range(3) if j != i)]
        planes.append(dict(omitted_axis=i, mixed_count=len(mixed),
                           mixed_allowed=sum(p) - 2,
                           dominating_count=len(dominating),
                           dominating_allowed=p[i]))
    assert [r['mixed_count'] for r in planes] == [5, 4, 4]
    assert [r['dominating_count'] for r in planes] == [3, 3, 3]

    B = {(0, 0, 0), *units}
    A = {x for x in T if all(add(x, b) in T for b in B)}
    difference = {sub(x, b) for x in A for b in B}
    assert (len(A), len(difference)) == (23, 55)
    assert len(difference) > m

    intersecting = [(i, j) for i in range(len(corners)) for j in range(i)
                    if any(corners[i][k] and corners[j][k] for k in range(3))]
    corner_labelings = []
    bijective_labelings = []
    for b, c in product(range(m), repeat=2):
        # The necessary full-corner equation is a + 2b + 2c == 0 (mod m).
        a = (-2 * b - 2 * c) % m
        w = (a, b, c)
        labels = [sum(t * v for t, v in zip(q, w)) % m for q in corners]
        if all(labels[i] != labels[j] for i, j in intersecting):
            corner_labelings.append(w)
        if len({sum(t * v for t, v in zip(q, w)) % m for q in T}) == m:
            bijective_labelings.append(w)
    assert (len(corners), len(intersecting), len(corner_labelings), len(bijective_labelings)) == (17, 120, 192, 0)

    result = dict(status='PASS', scope='Auxiliary geometric counterexample, excluded from Apéry ideals',
                  heights=heights, weights=[1, 1, 1], full_corner=p,
                  size=m, maximum=M, moment=sigma, D=D, size_minus_D=m-D,
                  corners=corners, planes=planes,
                  erosion=dict(A=len(A), A_minus_B=len(difference), T=m),
                  residue_checks=dict(modulus=m, tested_full_corner_labelings=m*m,
                                      intersecting_corner_pairs=len(intersecting),
                                      passing_corner_distinctness=len(corner_labelings),
                                      passing_full_bijection=len(bijective_labelings),
                                      example_corner_labeling=corner_labelings[0]))
    Path(__file__).with_name('erosion_fixture_checks.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
