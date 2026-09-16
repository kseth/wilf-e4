#!/usr/bin/env python3
"""Exact construction diagnostic for the B4.3 profile specification.

This checks a bounded geometric family, not its weighted theorem. It reads
no historical shape list or dual certificate and writes only to stdout.
Neither this script nor its counts establish B4-low-FV.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter, defaultdict


Row = tuple[int, ...]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def extent(row: Row) -> int:
    return sum(value > 0 for value in row)


def drops(row: Row) -> set[int]:
    return {i for i in range(1, extent(row)) if row[i] < row[i - 1]}


def footprint(row: Row) -> set[tuple[int, int]]:
    return {(i, j) for i, length in enumerate(row) for j in range(length)}


def recursive_rows(cap: int, prefix: Row = ()) -> list[Row]:
    if len(prefix) == cap + 1:
        return [prefix]
    limit = min(cap + 1 - len(prefix), prefix[-1] if prefix else cap + 1)
    return [
        row
        for value in range(limit + 1)
        for row in recursive_rows(cap, prefix + (value,))
    ]


def dictionary_check(row: Row, cap: int) -> None:
    points = footprint(row)
    corners = {
        (i, j)
        for i, j in itertools.product(range(cap + 2), repeat=2)
        if (i, j) not in points
        and (i == 0 or (i - 1, j) in points)
        and (j == 0 or (i, j - 1) in points)
    }
    if points:
        expected = {(0, row[0]), (extent(row), 0)}
        expected.update((i, row[i]) for i in drops(row))
    else:
        expected = {(0, 0)}
    require(corners == expected, "literal planar corner dictionary")


def compatible(f: Row, g: Row, h: Row) -> bool:
    return extent(f) == extent(g) and f[0] == extent(h) and g[0] == h[0]


def construction_check(f: Row, g: Row, h: Row, cap: int) -> tuple[bool, int]:
    points = {
        (x, y, z)
        for x, y, z in itertools.product(range(cap + 1), repeat=3)
        if y < f[x] and z < g[x] and z < h[y]
        and not (x >= 2 and y >= 1 and z >= 1)
    }
    columns = {
        (x, y, z)
        for x in range(extent(f))
        for y in range(f[x])
        for z in range(min(g[x], h[y]))
        if x < 2 or y == 0 or z == 0
    }
    require(points == columns, "grid/column reconstruction agreement")
    for point in points:
        for i, value in enumerate(point):
            if value:
                predecessor = tuple(v - (j == i) for j, v in enumerate(point))
                require(predecessor in points, "literal lower closure")
    require((2, 1, 1) not in points, "full corner excluded")
    require(all(p in points for p in ((1, 1, 1), (2, 0, 1), (2, 1, 0))),
            "full corner predecessors")
    sections = (
        {(x, y) for x, y, z in points if z == 0},
        {(x, z) for x, y, z in points if y == 0},
        {(y, z) for x, y, z in points if x == 0},
    )
    require(sections == tuple(footprint(row) for row in (f, g, h)),
            "exact recovery of all three plane profiles")
    degree_pass = all(y + min(g[1], h[y]) <= cap for y in range(1, f[1]))
    require(degree_pass == (max(map(sum, points)) <= cap),
            "short row test equals literal total-degree test")
    cardinality = (
        sum(h)
        + sum(min(g[1], h[y]) for y in range(f[1]))
        + sum(f[x] + g[x] - 1 for x in range(2, extent(f)))
    )
    require(cardinality == len(points), "three-slice cardinality formula")
    if degree_pass:
        require(cardinality <= 2 * cap * cap - cap + 3,
                "analytic cardinality invariant")
    return degree_pass, cardinality


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--degree-cap", type=int, choices=(4, 5), default=5)
    cap = parser.parse_args().degree_cap
    all_rows = {
        row for row in itertools.product(*(range(cap + 2 - i) for i in range(cap + 1)))
        if all(row[i] >= row[i + 1] for i in range(cap))
    }
    recursive = recursive_rows(cap)
    require(len(recursive) == len(set(recursive)), "recursive profile uniqueness")
    require(set(recursive) == all_rows, "Cartesian/recursive profile agreement")
    for row in all_rows:
        dictionary_check(row, cap)
    x_rows = sorted(
        row for row in all_rows
        if row[2] >= 2 and len(drops(row)) <= 2
        and sum(i >= 2 for i in drops(row)) <= 1
    )
    yz_rows = sorted(row for row in all_rows if row[1] >= 2 and len(drops(row)) <= 2)
    indexed: dict[tuple[int, int], list[Row]] = defaultdict(list)
    for h in yz_rows:
        indexed[extent(h), h[0]].append(h)
    indexed_keys = {
        (f, g, h)
        for f, g in itertools.product(x_rows, repeat=2)
        if extent(f) == extent(g)
        for h in indexed[f[0], g[0]]
    }
    direct_keys = {
        (f, g, h) for f, g, h in itertools.product(x_rows, x_rows, yz_rows)
        if compatible(f, g, h)
    }
    require(indexed_keys == direct_keys, "axis index omits no compatible triple")
    histogram: Counter[int] = Counter()
    for f, g, h in sorted(indexed_keys):
        degree_pass, cardinality = construction_check(f, g, h, cap)
        if degree_pass:
            histogram[cardinality] += 1
    print(json.dumps({
        "scope": "construction diagnostic only; no weighted dual replay",
        "degree_cap": cap,
        "all_triangle_profiles": len(all_rows),
        "xy_or_xz_profiles": len(x_rows),
        "yz_profiles": len(yz_rows),
        "compatible_triples": len(indexed_keys),
        "degree_filtered_shapes": sum(histogram.values()),
        "eligible_at_least_30": sum(n for m, n in histogram.items() if m >= 30),
        "maximum_cardinality": max(histogram),
        "cardinality_histogram": dict(sorted(histogram.items())),
        "result": "all dictionary, reconstruction, degree, and cardinality checks passed",
    }, indent=2))


if __name__ == "__main__":
    main()
