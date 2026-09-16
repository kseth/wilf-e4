#!/usr/bin/env python3
"""Enumeration-wide diagnostic for the D4 local short-corner route.

Reads no archived code or certificates and writes only to stdout.
This shares B4.3 research profile helpers; it is neither an independent
R4b implementation nor audited release proof code.
"""

from __future__ import annotations

import itertools
import json
from collections import Counter, defaultdict
from fractions import Fraction

from check_b4_low_height_profiles import drops, extent, recursive_rows


Point = tuple[int, int, int]
Row = tuple[int, ...]
Key = tuple[Row, Row, Row]
E0: Key = (
    (4, 3, 3, 2, 0, 0),
    (6, 3, 3, 2, 0, 0),
    (6, 4, 2, 2, 0, 0),
)
E1: Key = (
    E0[1],
    E0[0],
    tuple(sum(length > z for length in E0[2]) for z in range(6)),
)
OFFSETS = tuple(
    v for v in itertools.product(range(3), repeat=3) if sum(v) <= 2
)
WITNESS = (((0, 0, 5), 38), ((2, 2, 0), 48), ((3, 1, 0), 4))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def reconstruct(key: Key) -> set[Point]:
    f, g, h = key
    return {
        (x, y, z)
        for x in range(extent(f))
        for y in range(f[x])
        for z in range(min(g[x], h[y]))
        if x < 2 or y == 0 or z == 0
    }


def moment(points: set[Point]) -> Point:
    return tuple(sum(p[i] for p in points) for i in range(3))


def coordinate_lines(points: set[Point]) -> list[tuple[int, int, Point]]:
    lines = []
    for i in range(3):
        fibers: dict[tuple[int, ...], list[Point]] = defaultdict(list)
        for point in points:
            fibers[tuple(point[j] for j in range(3) if j != i)].append(point)
        for fiber in fibers.values():
            top = max(fiber, key=lambda p: p[i])
            require(len(fiber) == top[i] + 1, "initial coordinate interval")
            lines.append((i, len(fiber), top))
    return lines


def local_gain(points: set[Point]) -> tuple[int, list[tuple[int, int, Point]]]:
    lines = coordinate_lines(points)
    m, s = len(points), moment(points)
    require(sum(length for _, length, _ in lines) == 3 * m, "line mass")
    base = [sum(length * top[i] for _, length, top in lines) for i in range(3)]
    require(base == [4 * v for v in s], "line moment")
    upgraded = [0, 0, 0]
    gain = 0
    for _, length, top in lines:
        _, offset = max(
            (sum(v), v) for v in OFFSETS
            if tuple(top[i] + v[i] for i in range(3)) in points
        )
        gain += length * sum(offset)
        for i in range(3):
            upgraded[i] += length * (top[i] + offset[i])
    residual = [upgraded[i] - 4 * s[i] for i in range(3)]
    require(all(v >= 0 for v in residual), "local residual nonnegative")
    require(sum(residual) == gain, "local residual sum")
    return gain, lines


def exceptional_checks(
    key: Key, points: set[Point], gain: int, lines: list
) -> dict:
    require(key in (E0, E1), "recognized exceptional key")
    m, s = len(points), moment(points)
    witness = (
        WITNESS if key == E0
        else tuple(((p[0], p[2], p[1]), n) for p, n in WITNESS)
    )
    require(all(p in points for p, _ in witness), "exceptional point membership")
    require(sum(n for _, n in witness) == 3 * m, "exceptional mass")
    residual = [
        sum(n * p[i] for p, n in witness) - 4 * s[i] for i in range(3)
    ]
    require(all(v >= 0 for v in residual), "exceptional coordinate residual")
    require(sum(residual) >= m - 1, "exceptional bound")
    maxima = {
        p for p in points
        if all(
            tuple(v + (j == i) for j, v in enumerate(p)) not in points
            for i in range(3)
        )
    }
    unlimited = sum(
        length * max(
            sum(p) - sum(top)
            for p in maxima if all(p[i] >= top[i] for i in range(3))
        )
        for _, length, top in lines
    )
    axes = tuple(max(p[i] for p in points) for i in range(3))
    projections = sum(
        len({tuple(p[j] for j in range(3) if j != i) for p in points})
        for i in range(3)
    )
    phi = projections - 3 * len(maxima) - sum(map(sum, maxima)) + sum(axes)
    grouped = [Counter() for _ in range(3)]
    for i, length, top in lines:
        rho = max(
            sum(v) for v in OFFSETS
            if tuple(top[j] + v[j] for j in range(3)) in points
        )
        grouped[i][rho] += length
    require(
        unlimited == gain, "unlimited dominating upgrades still insufficient"
    )
    require(
        all(p in points for p in itertools.product(range(4), repeat=3) if sum(p) <= 3),
        "degree-three simplex contained in exception",
    )
    return {
        "key": key, "m": m, "s": s, "U2": gain,
        "unlimited_upgrade": unlimited, "projection_score": phi,
        "line_mass_by_gain": [dict(sorted(c.items())) for c in grouped],
        "explicit_witness_residual": residual,
    }


def main() -> None:
    rows = sorted(recursive_rows(5))
    require(len(rows) == len(set(rows)), "unique profile vectors")
    px = [
        r for r in rows if r[2] >= 2 and len(drops(r)) <= 2
        and sum(i >= 2 for i in drops(r)) <= 1
    ]
    pyz = [r for r in rows if r[1] >= 2 and len(drops(r)) <= 2]
    indexed = defaultdict(list)
    for h in pyz:
        indexed[extent(h), h[0]].append(h)
    counts = Counter()
    exceptions = []
    visited: set[Key] = set()
    minimum_local_margin = None
    for f, g in itertools.product(px, repeat=2):
        if extent(f) != extent(g):
            continue
        for h in indexed[f[0], g[0]]:
            counts["compatible"] += 1
            if any(y + min(g[1], h[y]) > 5 for y in range(1, f[1])):
                continue
            counts["degree_filtered"] += 1
            cardinality = (
                sum(h) + sum(min(g[1], h[y]) for y in range(f[1]))
                + sum(f[x] + g[x] - 1 for x in range(2, extent(f)))
            )
            if cardinality < 30:
                continue
            key = f, g, h
            require(key not in visited, "duplicate canonical key")
            visited.add(key)
            points = reconstruct(key)
            require(len(points) == cardinality <= 48, "reconstructed cardinality")
            require(max(map(sum, points)) <= 5, "literal degree check")
            gain, lines = local_gain(points)
            counts["eligible"] += 1
            if gain >= cardinality - 1:
                counts["local_pass"] += 1
                margin = gain - (cardinality - 1)
                minimum_local_margin = (
                    margin if minimum_local_margin is None
                    else min(minimum_local_margin, margin)
                )
            else:
                require(key in (E0, E1), "unexpected local failure")
                exceptions.append(exceptional_checks(key, points, gain, lines))
    require(
        {tuple(tuple(r) for r in e["key"]) for e in exceptions} == {E0, E1},
        "both advertised exceptions found",
    )
    require(visited >= {E0, E1}, "exceptional profile coverage")

    # Exact obstructions to removing necessary hypotheses or assuming
    # equal weights; these are abstract ideals, not semigroup examples.
    t5 = {
        p for p in itertools.product(range(6), repeat=3)
        if p[0] + p[1] <= 5 and p[0] + p[2] <= 5
        and (p[1] * p[2] == 0 or p[1] + p[2] <= 4)
        and not (p[0] >= 2 and p[1] >= 1 and p[2] >= 1)
    }
    d5 = 3 * len(t5) * 5 - 4 * sum(map(sum, t5))
    require(
        (len(t5), moment(t5), d5) == (48, (61, 55, 55), 36),
        "unfiltered low-height obstruction",
    )
    t0 = reconstruct(E0)
    w = (Fraction(5, 4), Fraction(5, 4), Fraction(1))
    H = max(sum(w[i] * p[i] for i in range(3)) for p in t0)
    D = (
        3 * len(t0) * H
        - 4 * sum(w[i] * moment(t0)[i] for i in range(3))
    )
    require((H, D) == (5, 54), "unequal-weight exposed vertex")

    print(json.dumps({
        "scope": "enumeration-wide research diagnostic; not an audited or independent R4b replay",
        "archive_inputs": False, "floating_point_used": False,
        "counts": dict(counts), "minimum_nonexceptional_local_margin": minimum_local_margin,
        "exceptions": exceptions,
        "unfiltered_obstruction": {"m": 48, "H": 5, "D": d5},
        "unequal_weight_obstruction": {"weights": [str(v) for v in w], "H": str(H), "D": str(D)},
        "result": "all local identities, selected finite predicates, and explicit witnesses passed",
    }, indent=2))


if __name__ == "__main__":
    main()
