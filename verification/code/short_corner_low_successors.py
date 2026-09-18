#!/usr/bin/env python3
"""Finite Lemma 2.5: Cartesian profiles, literal cube, successor paths."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys

EXCEPTIONS = (
    ((4, 3, 3, 2, 0, 0), (6, 3, 3, 2, 0, 0), (6, 4, 2, 2, 0, 0)),
    ((6, 3, 3, 2, 0, 0), (4, 3, 3, 2, 0, 0), (4, 4, 2, 2, 1, 1)),
)


def ensure(condition, reason):
    if not condition:
        raise RuntimeError(reason)


def planar_data(row):
    footprint = {(x, y) for x in range(6) for y in range(row[x])}
    corners = [(x, y) for x in range(1, 6) for y in range(1, 6)
               if (x, y) not in footprint and (x - 1, y) in footprint
               and (x, y - 1) in footprint]
    return footprint, corners, sum((x, 0) in footprint for x in range(6))


def check_integer_witness(points, weighted_points):
    total, weighted_sum = 0, [0, 0, 0]
    for p, amount in weighted_points:
        ensure(type(amount) is int and amount >= 0 and p in points, "invalid witness")
        total += amount
        for i, coordinate in enumerate(p):
            weighted_sum[i] += amount * coordinate
    ensure(total == 3 * len(points), "wrong witness mass")
    residual = []
    for i in range(3):
        value = weighted_sum[i] - 4 * sum(p[i] for p in points)
        ensure(value >= 0, "negative witness coordinate")
        residual.append(value)
    ensure(sum(residual) >= len(points) - 1, "witness below target")
    return tuple(residual)


def next_points(p, points):
    return [q for i in range(3)
            for q in [tuple(v + (j == i) for j, v in enumerate(p))] if q in points]


def successor_gain(points):
    total = 0
    mass = 0
    weighted_tops = [0, 0, 0]
    for p in points:
        for i in range(3):
            if p[i]:
                ensure(tuple(v - (j == i) for j, v in enumerate(p)) in points,
                       "not downward closed")
            if tuple(v + (j == i) for j, v in enumerate(p)) in points:
                continue
            length = p[i] + 1
            mass += length
            for j in range(3):
                weighted_tops[j] += length * p[j]
            successors = next_points(p, points)
            depth = (2 if any(next_points(q, points) for q in successors)
                     else 1 if successors else 0)
            total += length * depth
    ensure(mass == 3 * len(points), "top mass identity")
    ensure(weighted_tops == [4 * sum(p[i] for p in points) for i in range(3)],
           "top vector identity")
    return total


def verify():
    ensure(not sys.flags.optimize, "optimized interpreter is forbidden")
    px, yz = [], []
    for row in itertools.product(*(range(7 - i) for i in range(6))):
        if any(row[i] < row[i + 1] for i in range(5)):
            continue
        footprint, corners, xaxis = planar_data(row)
        if (2, 1) in footprint and len(corners) <= 2 \
                and sum(x >= 2 for x, _ in corners) <= 1:
            px.append((row, xaxis))
        if (1, 1) in footprint and len(corners) <= 2:
            yz.append((row, xaxis))
    cube = list(itertools.product(range(6), repeat=3))
    counts = dict(compatible=0, degree_filtered=0, eligible=0, local_pass=0)
    maximum = 0
    margin_min = None
    exceptions = []
    digest = hashlib.sha256()
    for f, fx in px:
        for g, gx in px:
            if fx != gx:
                continue
            for h, hx in yz:
                if f[0] != hx or g[0] != h[0]:
                    continue
                counts["compatible"] += 1
                points = {p for p in cube
                          if p[1] < f[p[0]] and p[2] < g[p[0]]
                          and p[2] < h[p[1]]
                          and not (p[0] >= 2 and p[1] >= 1 and p[2] >= 1)}
                if any(sum(p) > 5 for p in points):
                    continue
                counts["degree_filtered"] += 1
                cardinality = len(points)
                ensure(cardinality <= 48, "analytic cardinality bound")
                maximum = max(maximum, cardinality)
                if cardinality < 30:
                    continue
                counts["eligible"] += 1
                key = f, g, h
                value = successor_gain(points)
                moments = tuple(sum(p[i] for p in points) for i in range(3))
                if value < cardinality - 1:
                    ensure(key in EXCEPTIONS, "unadvertised failure")
                    p1, p2, p3 = ((0, 0, 5), (2, 2, 0), (3, 1, 0))
                    if key == EXCEPTIONS[1]:
                        p1, p2, p3 = [(x, z, y) for x, y, z in (p1, p2, p3)]
                    residual = check_integer_witness(points, [(p1, 38), (p2, 48), (p3, 4)])
                    exceptions.append(dict(key=key, m=cardinality, moment=moments,
                                           U2=value, residual=residual))
                else:
                    counts["local_pass"] += 1
                    margin = value - cardinality + 1
                    margin_min = margin if margin_min is None else min(margin_min, margin)
                digest.update((json.dumps([key, cardinality, moments, value],
                                          separators=(",", ":")) + "\n").encode())
    ensure({tuple(map(tuple, e["key"])) for e in exceptions} == set(EXCEPTIONS),
           "both exceptional ideals checked")
    ensure(counts["eligible"] == counts["local_pass"] + len(exceptions),
           "missing predicate result")
    return dict(schema_version=1, component="short-corner-successors", status="PASS",
                complete=True, contract="finite:short-corner-low", counts=counts,
                profile_counts=[len(px), len(yz)], largest_cardinality=maximum,
                minimum_local_margin=margin_min, exceptions=exceptions,
                result_sha256=digest.hexdigest(), unresolved=0, unsupported=0,
                arithmetic="Python arbitrary-precision integers")


def main():
    argparse.ArgumentParser(description=__doc__).parse_args()
    try:
        print(json.dumps(verify(), sort_keys=True))
    except Exception as error:
        print(f"short-corner successors failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
