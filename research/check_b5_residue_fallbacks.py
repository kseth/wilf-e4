#!/usr/bin/env python3
"""Probe residue compatibility of the 431 B5 local-witness fallbacks.

This is an exploratory exact check, not part of the retained proof.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter
from pathlib import Path


DEFAULT_INPUT = Path(
    "artifacts/wilf_four_generators_review_package_2026-09-11/"
    "round10/local_centroid/axis_fallbacks_strong.jsonl"
)


def dot_mod(point: tuple[int, int, int], weights: tuple[int, int, int], m: int) -> int:
    return sum(x * a for x, a in zip(point, weights)) % m


def minimal_mixed_corners(points: set[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    maxima = [max(point[i] for point in points) for i in range(3)]
    corners: list[tuple[int, int, int]] = []
    for point in itertools.product(*(range(bound + 2) for bound in maxima)):
        if point in points or sum(coordinate > 0 for coordinate in point) != 2:
            continue
        predecessors = [
            tuple(coordinate - (i == j) for j, coordinate in enumerate(point))
            for i in range(3)
            if point[i] > 0
        ]
        if all(predecessor in points for predecessor in predecessors):
            corners.append(point)
    return corners


def analyze(row: dict[str, object]) -> tuple[str, int | None]:
    m = int(row["m"])
    full_corner = tuple(row["corner"])
    points = {tuple(point) for point in row["points"]}
    assert len(points) == m

    axes = [
        sorted(point for point in points if all(point[j] == 0 for j in range(3) if j != i))
        for i in range(3)
    ]
    axis_union = set().union(*map(set, axes))

    candidates: list[tuple[int, int, int]] = []
    for weights in itertools.permutations(range(1, m), 3):
        if dot_mod(full_corner, weights, m) != 0:
            continue
        residues = {dot_mod(point, weights, m) for point in axis_union}
        if len(residues) == len(axis_union):
            candidates.append(weights)

    if not candidates:
        return "corner_and_axes", None

    # A genuine residue labeling would in particular survive the conditions
    # above. None does; retain this assertion as a cross-check.
    assert not any(
        len({dot_mod(point, weights, m) for point in points}) == m
        for weights in candidates
    )

    for corner in minimal_mixed_corners(points):
        zero_coordinate = corner.index(0)
        if not any(
            dot_mod(corner, weights, m)
            in {dot_mod(point, weights, m) for point in axes[zero_coordinate]}
            for weights in candidates
        ):
            return "one_mixed_corner", zero_coordinate

    return "unresolved", None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", type=Path, default=DEFAULT_INPUT)
    args = parser.parse_args()

    outcomes: Counter[str] = Counter()
    zero_coordinates: Counter[int] = Counter()
    with args.input.open(encoding="utf-8") as rows:
        for line in rows:
            outcome, zero_coordinate = analyze(json.loads(line))
            outcomes[outcome] += 1
            if zero_coordinate is not None:
                zero_coordinates[zero_coordinate] += 1

    summary = {
        "input": str(args.input),
        "shapes": sum(outcomes.values()),
        "excluded_by_corner_and_axes": outcomes["corner_and_axes"],
        "excluded_by_one_mixed_corner": outcomes["one_mixed_corner"],
        "unresolved": outcomes["unresolved"],
        "mixed_corner_zero_coordinate": dict(sorted(zero_coordinates.items())),
    }
    print(json.dumps(summary, indent=2))

    assert summary["shapes"] == 431
    assert summary["excluded_by_corner_and_axes"] == 199
    assert summary["excluded_by_one_mixed_corner"] == 232
    assert summary["unresolved"] == 0


if __name__ == "__main__":
    main()
