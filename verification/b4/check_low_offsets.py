#!/usr/bin/env python3
"""Complete B4-low-local-FV check: recursive profiles and explicit offsets."""
from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import itertools
import json
import sys

E0 = ((4, 3, 3, 2, 0, 0), (6, 3, 3, 2, 0, 0), (6, 4, 2, 2, 0, 0))
E1 = ((6, 3, 3, 2, 0, 0), (4, 3, 3, 2, 0, 0), (4, 4, 2, 2, 1, 1))
WITNESS = (((0, 0, 5), 38), ((2, 2, 0), 48), ((3, 1, 0), 4))
OFFSETS = tuple(v for v in itertools.product(range(3), repeat=3) if sum(v) <= 2)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def profiles(prefix=()):
    if len(prefix) == 6:
        yield prefix
        return
    cap = min(6 - len(prefix), prefix[-1] if prefix else 6)
    for value in range(cap + 1):
        yield from profiles(prefix + (value,))


def extent(row):
    return sum(v > 0 for v in row)


def drops(row):
    return [i for i in range(1, extent(row)) if row[i] < row[i - 1]]


def points_of(key):
    f, g, h = key
    return {(x, y, z) for x in range(extent(f)) for y in range(f[x])
            for z in range(min(g[x], h[y])) if x < 2 or y == 0 or z == 0}


def check_integer_witness(points, weighted_points):
    require(all(type(n) is int and n >= 0 and p in points
                for p, n in weighted_points), "witness membership/nonnegativity")
    require(sum(n for _, n in weighted_points) == 3 * len(points), "witness mass")
    residual = tuple(sum(n * p[i] for p, n in weighted_points)
                     - 4 * sum(p[i] for p in points) for i in range(3))
    require(min(residual) >= 0 and sum(residual) >= len(points) - 1,
            "witness residual/target")
    return residual


def gain(points):
    fibers = [defaultdict(list) for _ in range(3)]
    for p in points:
        for i in range(3):
            fibers[i][tuple(p[j] for j in range(3) if j != i)].append(p)
            if p[i]:
                require(tuple(p[j] - (i == j) for j in range(3)) in points,
                        "lower closure")
    lines = [(len(f), max(f, key=lambda p: p[i]))
             for i in range(3) for f in fibers[i].values()]
    require(all(n == p[i] + 1 for i in range(3)
                for f in fibers[i].values()
                for n, p in [(len(f), max(f, key=lambda p: p[i]))]), "initial fibers")
    require(sum(n for n, _ in lines) == 3 * len(points), "line mass")
    for i in range(3):
        require(sum(n * p[i] for n, p in lines) == 4 * sum(p[i] for p in points),
                "line moment")
    return sum(n * max(sum(v) for v in OFFSETS
                       if tuple(p[i] + v[i] for i in range(3)) in points)
               for n, p in lines)


def check():
    require(sys.flags.optimize == 0, "optimized Python is unsupported")
    rows = sorted(profiles())
    require(len(rows) == len(set(rows)), "profile uniqueness")
    px = [r for r in rows if r[2] >= 2 and len(drops(r)) <= 2
          and sum(i >= 2 for i in drops(r)) <= 1]
    pyz = [r for r in rows if r[1] >= 2 and len(drops(r)) <= 2]
    index = defaultdict(list)
    for h in pyz:
        index[extent(h), h[0]].append(h)
    counts = dict(compatible=0, degree_filtered=0, eligible=0, local_pass=0)
    largest = 0
    smallest_margin = None
    exceptions = []
    digest = hashlib.sha256()
    for f in px:
        for g in px:
            if extent(f) != extent(g):
                continue
            for h in index[f[0], g[0]]:
                counts["compatible"] += 1
                short_degree = all(y + min(g[1], h[y]) <= 5
                                   for y in range(1, f[1]))
                key = f, g, h
                points = points_of(key)
                require(short_degree == (max(map(sum, points)) <= 5),
                        "short versus literal degree")
                if not short_degree:
                    continue
                counts["degree_filtered"] += 1
                m = (sum(h) + sum(min(g[1], h[y]) for y in range(f[1]))
                     + sum(f[x] + g[x] - 1 for x in range(2, extent(f))))
                require(m == len(points) and m <= 48, "cardinality identity/bound")
                largest = max(largest, m)
                if m < 30:
                    continue
                counts["eligible"] += 1
                value = gain(points)
                moment = tuple(sum(p[i] for p in points) for i in range(3))
                if value >= m - 1:
                    counts["local_pass"] += 1
                    margin = value - m + 1
                    smallest_margin = (margin if smallest_margin is None
                                       else min(smallest_margin, margin))
                else:
                    require(key in (E0, E1), "unexpected local failure")
                    witness = (WITNESS if key == E0 else
                               tuple(((p[0], p[2], p[1]), n) for p, n in WITNESS))
                    residual = check_integer_witness(points, witness)
                    exceptions.append(dict(key=key, m=m, moment=moment,
                                           U2=value, residual=residual))
                digest.update((json.dumps([key, m, moment, value],
                                          separators=(",", ":")) + "\n").encode())
    require({tuple(map(tuple, e["key"])) for e in exceptions} == {E0, E1},
            "exceptional key coverage")
    require(counts["eligible"] == counts["local_pass"] + len(exceptions),
            "complete predicate classification")
    return dict(schema_version=1, component="R4b-offsets", status="PASS",
                complete=True, contract="B4-low-local-FV", counts=counts,
                profile_counts=[len(px), len(pyz)], largest_cardinality=largest,
                minimum_local_margin=smallest_margin, exceptions=exceptions,
                result_sha256=digest.hexdigest(), unresolved=0, unsupported=0,
                arithmetic="Python arbitrary-precision integers", archive_inputs=False)


def main():
    argparse.ArgumentParser(description=__doc__).parse_args()
    try:
        print(json.dumps(check(), sort_keys=True))
    except Exception as error:
        print(f"R4b offsets failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
