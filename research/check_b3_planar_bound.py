#!/usr/bin/env python3
"""Bounded exact diagnostic for the analytic D3 three-plane proof.

This does not establish the theorem by computation. It reconstructs literal
point sets for bounded axis lengths and cross-checks every counting identity.
No historical program, shape list, residue label, or certificate is imported.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter
from dataclasses import dataclass


Point = tuple[int, int, int]


@dataclass(frozen=True)
class Plane:
    mixed: frozenset[Point]
    cells: int
    beta: int
    charge: int
    split: bool


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def profiles(i: int, j: int, hi: int, hj: int) -> list[Plane]:
    result = []
    # The full rectangle has no mixed exclusion; all other profiles remove
    # the quadrant starting at (b+1,d+1). The included (1,1) forbids (0,0).
    parameters = [None] + [
        (b, d)
        for b in range(hi)
        for d in range(hj)
        if b or d
    ]
    for parameter in parameters:
        mixed = set()
        for x in range(1, hi + 1):
            for y in range(1, hj + 1):
                if parameter is not None:
                    b, d = parameter
                    if x > b and y > d:
                        continue
                point = [0, 0, 0]
                point[i], point[j] = x, y
                mixed.add(tuple(point))
        if parameter is None:
            cells, beta, charge, split = hi * hj, 0, 0, False
        else:
            b, d = parameter
            cells = b * hj + d * hi - b * d
            beta = b + d
            charge = hi if d == 0 else (hj if b == 0 else 0)
            split = b > 0 and d > 0
        require(len(mixed) == cells, "plane area formula")
        result.append(Plane(frozenset(mixed), cells, beta, charge, split))
    require(len(result) == hi * hj, "plane profile count")
    return result


def successor(point: Point, i: int) -> Point:
    return tuple(value + (j == i) for j, value in enumerate(point))


def analyze(axes: tuple[int, int, int], planes: tuple[Plane, ...]) -> tuple[int, int, int]:
    points = {(0, 0, 0)}
    for i, length in enumerate(axes):
        for value in range(1, length + 1):
            point = [0, 0, 0]
            point[i] = value
            points.add(tuple(point))
    for plane in planes:
        points.update(plane.mixed)
    for point in points:
        for i, value in enumerate(point):
            if value:
                predecessor = tuple(x - (j == i) for j, x in enumerate(point))
                require(predecessor in points, "literal lower closure")
    require((1, 1, 1) not in points, "full corner excluded")
    require(all(tuple(1 - (j == i) for j in range(3)) in points for i in range(3)),
            "full corner predecessors")

    maxima = {
        point for point in points
        if all(successor(point, i) not in points for i in range(3))
    }
    m, k = len(points), len(maxima)
    h = sum(axes)
    B = sum(plane.beta for plane in planes)
    C = sum(plane.cells - plane.beta for plane in planes)
    N = sum(plane.charge for plane in planes)
    s = sum(plane.split for plane in planes)
    axis_maxima = [point for point in maxima if sum(x > 0 for x in point) == 1]
    J = sum(sum(point) for point in axis_maxima)
    Q = h + C + N - J
    P = sum(
        len({tuple(x for j, x in enumerate(point) if j != i) for point in points})
        for i in range(3)
    )
    degree_sum = sum(map(sum, maxima))
    E = degree_sum - sum(max(point[i] for point in maxima) for i in range(3))
    phi = P - 3 * k - E

    require(m == 1 + h + B + C, "cardinality identity")
    require(P == m + h + 2, "projection identity")
    require(degree_sum == 2 * h + B - N + J, "maximal-degree identity")
    require(E == h + B - N + J, "E identity")
    require(k == 3 + s + len(axis_maxima) and k <= 6, "maxima count")
    require(C >= 0 and B <= C + s + N, "frontier correction bound")
    require(N >= 2 * J, "double axis charge")
    require(phi == Q + 3 - 3 * k, "projection-score identity")
    require(m <= 1 + 2 * Q - h + s, "cardinality domination")
    if phi < 0:
        require(Q <= 3 * k - 4 <= 14, "negative-score integer bound")
        require(m <= 29, "D3 cardinality bound")
        # Check the subset transfer independently on every nonempty subset
        # of K for the negative-score profiles.
        ordered = sorted(maxima)
        for mask in range(1, 1 << k):
            subset = [point for i, point in enumerate(ordered) if mask & (1 << i)]
            subset_E = sum(map(sum, subset)) - sum(
                max(point[i] for point in subset) for i in range(3)
            )
            require(subset_E <= E, "subset E monotonicity")
            require(P - 3 * len(subset) - subset_E >= phi, "subset score monotonicity")
    return m, k, phi


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--axis-limit", type=int, default=4)
    args = parser.parse_args()
    require(args.axis_limit >= 1, "axis limit must be positive")
    total = negative = 0
    largest_negative = minimum_phi = None
    negative_by_maxima: Counter[int] = Counter()
    cache = {
        (i, j, hi, hj): profiles(i, j, hi, hj)
        for i, j in ((0, 1), (0, 2), (1, 2))
        for hi in range(1, args.axis_limit + 1)
        for hj in range(1, args.axis_limit + 1)
    }
    for axes in itertools.product(range(1, args.axis_limit + 1), repeat=3):
        families = [cache[i, j, axes[i], axes[j]] for i, j in ((0, 1), (0, 2), (1, 2))]
        for planes in itertools.product(*families):
            m, k, phi = analyze(axes, planes)
            total += 1
            minimum_phi = phi if minimum_phi is None else min(minimum_phi, phi)
            if phi < 0:
                negative += 1
                negative_by_maxima[k] += 1
                largest_negative = m if largest_negative is None else max(largest_negative, m)
    expected = sum(i * i for i in range(1, args.axis_limit + 1)) ** 3
    require(total == expected, "bounded profile coverage")
    print(json.dumps({
        "scope": "bounded diagnostic only; not a retained finite proof obligation",
        "axis_limit": args.axis_limit,
        "ordered_profiles": total,
        "negative_profiles": negative,
        "negative_by_maxima": dict(sorted(negative_by_maxima.items())),
        "largest_negative_cardinality": largest_negative,
        "minimum_projection_score": minimum_phi,
        "result": "all counting identities and analytic inequalities agree",
    }, indent=2))


if __name__ == "__main__":
    main()
