#!/usr/bin/env python3
"""Path A: fail-closed B2 tree checker with prefix-max horn recurrence."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MANIFEST = ROOT / "verification/b2/certificate-manifest.json"

MANIFEST_KEYS = {
    "schema_version",
    "component",
    "certificate_format",
    "certificate",
    "constants",
}
CERTIFICATE_KEYS = {
    "claim",
    "scale",
    "initial",
    "nodes",
    "seconds",
    "complete",
    "leaf_count",
    "tree",
    "unresolved",
}


class CheckFailure(RuntimeError):
    """Raised when the certificate does not establish its exact contract."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CheckFailure(message)


def is_integer(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise CheckFailure(f"duplicate JSON key: {key!r}")
        result[key] = value
    return result


def load_json(path: Path, label: str) -> object:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as error:
        raise CheckFailure(f"cannot read {label} {path}: {error}") from error
    try:
        return json.loads(text, object_pairs_hook=unique_object)
    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        raise CheckFailure(f"malformed {label} {path}: {error}") from error


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_box(value: object, label: str) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
    require(isinstance(value, list) and len(value) == 2, f"{label} is not an endpoint pair")
    endpoints: list[tuple[int, int, int]] = []
    for side, endpoint in zip(("lower", "upper"), value, strict=True):
        require(
            isinstance(endpoint, list) and len(endpoint) == 3,
            f"{label} {side} endpoint is not a triple",
        )
        require(all(is_integer(item) for item in endpoint), f"{label} has a noninteger endpoint")
        endpoints.append((endpoint[0], endpoint[1], endpoint[2]))
    lower, upper = endpoints
    require(all(a <= b for a, b in zip(lower, upper, strict=True)), f"{label} is inverted")
    return lower, upper


def tighten(
    lower: tuple[int, int, int], upper: tuple[int, int, int]
) -> tuple[tuple[int, int, int], tuple[int, int, int]] | None:
    b0, c0, h0 = lower
    b1, c1, h1 = upper
    tightened_lower = (b0, max(b0, c0), max(b0, c0, h0))
    tightened_upper = (min(b1, c1, h1), min(c1, h1), h1)
    if any(a > b for a, b in zip(tightened_lower, tightened_upper, strict=True)):
        return None
    return tightened_lower, tightened_upper


def validate_manifest(path: Path) -> tuple[Path, str, int, int, tuple[tuple[int, int, int], tuple[int, int, int]]]:
    value = load_json(path, "manifest")
    require(isinstance(value, dict), "manifest is not an object")
    require(set(value) == MANIFEST_KEYS, "unexpected manifest schema")
    require(value["schema_version"] == 1, "unsupported manifest schema version")
    require(value["component"] == "B2.2-FV", "wrong manifest component")
    require(
        value["certificate_format"] == "wilf-b2-interval-tree-historical-v1",
        "unsupported certificate format",
    )

    certificate = value["certificate"]
    require(isinstance(certificate, dict), "manifest certificate entry is not an object")
    require(set(certificate) == {"path", "sha256", "bytes"}, "unexpected certificate entry")
    relative = certificate["path"]
    expected_hash = certificate["sha256"]
    expected_bytes = certificate["bytes"]
    require(isinstance(relative, str) and relative, "certificate path is invalid")
    require(
        isinstance(expected_hash, str)
        and len(expected_hash) == 64
        and all(char in "0123456789abcdef" for char in expected_hash),
        "certificate SHA-256 is invalid",
    )
    require(is_integer(expected_bytes) and expected_bytes > 0, "certificate byte count is invalid")
    relative_path = Path(relative)
    require(not relative_path.is_absolute(), "certificate path must be repository-relative")
    certificate_path = (ROOT / relative_path).resolve()
    try:
        certificate_path.relative_to(ROOT)
    except ValueError as error:
        raise CheckFailure("certificate path escapes the repository") from error
    require(certificate_path.is_file(), f"certificate is missing: {relative}")
    require(certificate_path.stat().st_size == expected_bytes, "certificate byte count mismatch")
    require(sha256(certificate_path) == expected_hash, "certificate SHA-256 mismatch")

    constants = value["constants"]
    require(isinstance(constants, dict), "manifest constants entry is not an object")
    require(set(constants) == {"scale", "root"}, "unexpected constants entry")
    scale = constants["scale"]
    require(is_integer(scale) and scale == 4096, "wrong interval scale")
    root = parse_box(constants["root"], "manifest root")
    require(root == ((scale, scale, 5 * scale), (24 * scale,) * 3), "wrong manifest root")
    return certificate_path, expected_hash, expected_bytes, scale, root


def prefix_bound(
    lower: tuple[int, int, int], upper: tuple[int, int, int], scale: int
) -> int:
    feasible = (scale, lower[0], lower[1])
    objective = (scale, upper[0], upper[1])
    height = upper[2]
    offset = scale - 3 * lower[2]
    caps = tuple(height // weight for weight in feasible)
    require(all(0 <= cap <= 24 for cap in caps), "coordinate cap is outside the proved range")

    horns: list[tuple[list[list[int]], int]] = []
    for axis in range(3):
        other = tuple(index for index in range(3) if index != axis)
        rows = caps[other[0]] + 1
        columns = caps[other[1]] + 1
        layers = [[0] * (rows * columns) for _ in range(caps[axis] + 2)]
        for level in range(caps[axis], -1, -1):
            current = layers[level]
            tail = layers[level + 1]
            for first in range(rows):
                row_maximum = 0
                for second in range(columns):
                    index = first * columns + second
                    if (
                        feasible[axis] * level
                        + feasible[other[0]] * first
                        + feasible[other[1]] * second
                        <= height
                    ):
                        count = (first + 1) * (second + 1)
                        section = count * (
                            offset
                            + 4 * objective[axis] * level
                            + 2 * objective[other[0]] * first
                            + 2 * objective[other[1]] * second
                        )
                        row_maximum = max(row_maximum, section + tail[index])
                    prior_row = current[index - columns] if first else 0
                    current[index] = max(row_maximum, prior_row)
        horns.append((layers, columns))

    result: int | None = None
    for x in range(caps[0] + 1):
        for y in range(caps[1] + 1):
            for z in range(caps[2] + 1):
                center = (x, y, z)
                if sum(a * b for a, b in zip(feasible, center, strict=True)) > height:
                    continue
                count = (x + 1) * (y + 1) * (z + 1)
                score = count * (
                    offset
                    + 2 * sum(a * b for a, b in zip(objective, center, strict=True))
                )
                for axis in range(3):
                    other = tuple(index for index in range(3) if index != axis)
                    layers, columns = horns[axis]
                    score += layers[center[axis] + 1][
                        center[other[0]] * columns + center[other[1]]
                    ]
                result = score if result is None else max(result, score)
    require(result is not None, "no feasible central box")
    return result


def check(manifest_path: Path) -> dict[str, object]:
    require(sys.flags.optimize == 0, "optimized Python execution is unsupported")
    certificate_path, expected_hash, expected_bytes, scale, root = validate_manifest(manifest_path)
    certificate = load_json(certificate_path, "certificate")
    require(isinstance(certificate, dict), "certificate is not an object")
    require(set(certificate) == CERTIFICATE_KEYS, "unexpected certificate top-level schema")
    require(
        certificate["claim"]
        == "m-D<=1 for every nonempty no-interior ideal in each certified parameter box",
        "unexpected historical claim label",
    )
    require(certificate["scale"] == scale, "certificate scale mismatch")
    require(parse_box(certificate["initial"], "certificate root") == root, "root mismatch")
    require(certificate["complete"] is True, "certificate is not marked complete")
    require(certificate["unresolved"] == [], "certificate contains unresolved boxes")
    require(is_integer(certificate["nodes"]) and certificate["nodes"] > 0, "invalid node count")
    require(
        is_integer(certificate["leaf_count"]) and certificate["leaf_count"] > 0,
        "invalid leaf count",
    )
    seconds = certificate["seconds"]
    require(
        isinstance(seconds, (int, float))
        and not isinstance(seconds, bool)
        and math.isfinite(seconds)
        and seconds >= 0,
        "invalid producer timing field",
    )
    tree = certificate["tree"]
    require(isinstance(tree, list) and tree, "tree is not a nonempty list")
    require(certificate["nodes"] == len(tree), "stored node count does not match tree length")

    seen: set[int] = set()
    kinds: Counter[str] = Counter()
    leaves: list[tuple[int, str, int | None]] = []
    pending = [(0, root)]
    largest_bound: int | None = None
    smallest_bound: int | None = None
    while pending:
        node_id, expected_box = pending.pop()
        require(is_integer(node_id) and 0 <= node_id < len(tree), "child identifier is invalid")
        require(node_id not in seen, f"node {node_id} is reached more than once")
        seen.add(node_id)
        node = tree[node_id]
        require(isinstance(node, dict), f"node {node_id} is not an object")
        require("kind" in node and isinstance(node["kind"], str), f"node {node_id} has no kind")
        kind = node["kind"]
        kinds[kind] += 1
        expected_keys = {
            "empty": {"box", "kind"},
            "continuous": {"box", "kind"},
            "dp": {"box", "kind", "bound"},
            "split": {"box", "kind", "axis", "mid", "children"},
        }.get(kind)
        require(expected_keys is not None, f"node {node_id} has unsupported kind {kind!r}")
        require(set(node) == expected_keys, f"node {node_id} has an unexpected schema")
        actual_box = parse_box(node["box"], f"node {node_id} box")
        require(actual_box == expected_box, f"node {node_id} does not match its parent box")
        tightened = tighten(*actual_box)

        if tightened is None:
            require(kind == "empty", f"node {node_id} has empty ordered part but wrong kind")
            leaves.append((node_id, kind, None))
            continue
        require(kind != "empty", f"node {node_id} is incorrectly marked empty")
        lower, upper = tightened

        if kind == "split":
            axis = node["axis"]
            middle = node["mid"]
            children = node["children"]
            require(is_integer(axis) and 0 <= axis < 3, f"node {node_id} has invalid split axis")
            require(is_integer(middle), f"node {node_id} has noninteger split point")
            require(lower[axis] < middle < upper[axis], f"node {node_id} split is not interior")
            require(isinstance(children, list) and len(children) == 2, f"node {node_id} children invalid")
            require(all(is_integer(child) for child in children), f"node {node_id} child is noninteger")
            require(children[0] != children[1], f"node {node_id} repeats a child")
            left_upper = list(upper)
            right_lower = list(lower)
            left_upper[axis] = middle
            right_lower[axis] = middle
            pending.append((children[1], (tuple(right_lower), upper)))
            pending.append((children[0], (lower, tuple(left_upper))))
            continue

        if kind == "continuous":
            require(
                lower[2] >= 2 * (scale + upper[0] + upper[1]) + 3 * scale,
                f"node {node_id} fails the analytic leaf inequality",
            )
            leaves.append((node_id, kind, None))
            continue

        require(kind == "dp", f"node {node_id} is unterminated")
        stored = node["bound"]
        require(is_integer(stored), f"node {node_id} has a noninteger DP bound")
        actual = prefix_bound(lower, upper, scale)
        require(actual == stored, f"node {node_id} DP mismatch: recomputed {actual}, stored {stored}")
        require(actual <= scale, f"node {node_id} DP bound exceeds the threshold")
        largest_bound = actual if largest_bound is None else max(largest_bound, actual)
        smallest_bound = actual if smallest_bound is None else min(smallest_bound, actual)
        leaves.append((node_id, kind, actual))

    require(len(seen) == len(tree), "certificate contains unreachable nodes")
    require(len(leaves) == certificate["leaf_count"], "stored leaf count is inconsistent")
    require(sum(kinds.values()) == len(tree), "node-kind counts do not cover the tree")
    require(kinds["split"] + len(leaves) == len(tree), "tree is not fully terminated")

    digest = hashlib.sha256()
    for node_id, kind, bound in sorted(leaves):
        digest.update(f"{node_id}:{kind}:{'' if bound is None else bound}\n".encode())

    return {
        "schema_version": 1,
        "component": "R2-path-a-prefix",
        "status": "PASS",
        "complete": True,
        "fresh_leaf_recomputation": True,
        "coverage_checked": True,
        "certificate_sha256": expected_hash,
        "certificate_bytes": expected_bytes,
        "scale": scale,
        "root": [list(root[0]), list(root[1])],
        "tree_nodes": len(tree),
        "node_kinds": dict(sorted(kinds.items())),
        "leaves": len(leaves),
        "dp_leaves": kinds["dp"],
        "analytic_leaves": kinds["continuous"],
        "empty_leaves": kinds["empty"],
        "largest_dp_bound_numerator": largest_bound,
        "smallest_dp_bound_numerator": smallest_bound,
        "leaf_result_sha256": digest.hexdigest(),
        "unresolved": 0,
        "unsupported": 0,
        "arithmetic": "Python arbitrary-precision integers",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    arguments = parser.parse_args()
    try:
        result = check(arguments.manifest.resolve())
    except Exception as error:
        print(f"R2 Path A failed: {type(error).__name__}: {error}", file=sys.stderr)
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
