#!/usr/bin/env python3
"""Path B: independent B2 coverage walk and explicit-transition horn replay."""

from __future__ import annotations

import argparse
from collections import Counter, deque
from functools import lru_cache
import hashlib
from itertools import product
import json
import math
from pathlib import Path
import sys
from typing import Any


REPOSITORY = Path(__file__).resolve().parents[2]
DEFAULT_MANIFEST = REPOSITORY / "verification/b2/certificate-manifest.json"


class VerificationError(RuntimeError):
    """The independent path cannot certify the supplied tree."""


def ensure(condition: bool, detail: str) -> None:
    if not condition:
        raise VerificationError(detail)


def exact_int(value: object) -> bool:
    return type(value) is int


def reject_repeated_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    obj: dict[str, Any] = {}
    for name, value in pairs:
        if name in obj:
            raise VerificationError(f"repeated JSON field {name!r}")
        obj[name] = value
    return obj


def decode(path: Path, description: str) -> object:
    try:
        payload = path.read_text(encoding="utf-8")
        return json.loads(payload, object_pairs_hook=reject_repeated_keys)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise VerificationError(f"cannot decode {description}: {error}") from error


def file_digest(path: Path) -> str:
    state = hashlib.sha256()
    with path.open("rb") as source:
        while True:
            block = source.read(1 << 20)
            if not block:
                break
            state.update(block)
    return state.hexdigest()


def endpoint_pair(
    value: object, description: str
) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
    ensure(type(value) is list and len(value) == 2, f"{description} is not a pair")
    converted: list[tuple[int, int, int]] = []
    for endpoint in value:
        ensure(type(endpoint) is list and len(endpoint) == 3, f"{description} endpoint is invalid")
        ensure(all(exact_int(entry) for entry in endpoint), f"{description} endpoint is nonintegral")
        converted.append((endpoint[0], endpoint[1], endpoint[2]))
    low, high = converted
    ensure(all(x <= y for x, y in zip(low, high, strict=True)), f"{description} is reversed")
    return low, high


def ordered_part(
    low: tuple[int, int, int], high: tuple[int, int, int]
) -> tuple[tuple[int, int, int], tuple[int, int, int]] | None:
    """Propagate b <= c <= H to a fixed point rather than use Path A's formula."""
    lower = list(low)
    upper = list(high)
    while True:
        previous = (tuple(lower), tuple(upper))
        for index in range(2):
            lower[index + 1] = max(lower[index + 1], lower[index])
            upper[index] = min(upper[index], upper[index + 1])
        if any(x > y for x, y in zip(lower, upper, strict=True)):
            return None
        current = (tuple(lower), tuple(upper))
        if current == previous:
            return current


def manifest_input(
    manifest_path: Path,
) -> tuple[Path, str, int, int, tuple[tuple[int, int, int], tuple[int, int, int]]]:
    manifest = decode(manifest_path, "manifest")
    ensure(type(manifest) is dict, "manifest is not an object")
    ensure(
        set(manifest)
        == {"schema_version", "component", "certificate_format", "certificate", "constants"},
        "manifest fields are unsupported",
    )
    ensure(manifest["schema_version"] == 1, "manifest version is unsupported")
    ensure(manifest["component"] == "B2.2-FV", "manifest names the wrong component")
    ensure(
        manifest["certificate_format"] == "wilf-b2-interval-tree-historical-v1",
        "certificate encoding is unsupported",
    )

    descriptor = manifest["certificate"]
    ensure(type(descriptor) is dict, "certificate descriptor is invalid")
    ensure(set(descriptor) == {"path", "sha256", "bytes"}, "certificate descriptor fields differ")
    name = descriptor["path"]
    digest = descriptor["sha256"]
    length = descriptor["bytes"]
    ensure(type(name) is str and name != "", "certificate filename is invalid")
    ensure(
        type(digest) is str
        and len(digest) == 64
        and set(digest) <= set("0123456789abcdef"),
        "certificate digest is invalid",
    )
    ensure(exact_int(length) and length > 0, "certificate length is invalid")
    relative = Path(name)
    ensure(not relative.is_absolute(), "certificate filename is not relative")
    source = (REPOSITORY / relative).resolve()
    try:
        source.relative_to(REPOSITORY)
    except ValueError as error:
        raise VerificationError("certificate filename leaves the repository") from error
    ensure(source.is_file(), "certificate file does not exist")
    ensure(source.stat().st_size == length, "certificate length differs from manifest")
    ensure(file_digest(source) == digest, "certificate digest differs from manifest")

    constants = manifest["constants"]
    ensure(type(constants) is dict and set(constants) == {"scale", "root"}, "constants are invalid")
    scale = constants["scale"]
    ensure(exact_int(scale) and scale == 4096, "scale is not 4096")
    root = endpoint_pair(constants["root"], "manifest root")
    ensure(root == ((scale, scale, 5 * scale), (24 * scale,) * 3), "root is not the B2 box")
    return source, digest, length, scale, root


def explicit_bound(
    low: tuple[int, int, int], high: tuple[int, int, int], scale: int
) -> int:
    lower_weights = (scale, low[0], low[1])
    upper_weights = (scale, high[0], high[1])
    maximum_height = high[2]
    caps = tuple(maximum_height // weight for weight in lower_weights)
    ensure(all(0 <= cap <= 24 for cap in caps), "a coordinate cap exceeds 24")

    @lru_cache(maxsize=None)
    def horn(axis: int, level: int, first_cap: int, second_cap: int) -> int:
        if level > caps[axis]:
            return 0
        transverse = [coordinate for coordinate in range(3) if coordinate != axis]
        first_axis, second_axis = transverse
        maximum = 0
        for first in range(first_cap + 1):
            for second in range(second_cap + 1):
                if (
                    lower_weights[axis] * level
                    + lower_weights[first_axis] * first
                    + lower_weights[second_axis] * second
                    > maximum_height
                ):
                    continue
                count = (first + 1) * (second + 1)
                section_score = count * (
                    4 * upper_weights[axis] * level
                    + 2 * upper_weights[first_axis] * first
                    + 2 * upper_weights[second_axis] * second
                    - 3 * low[2]
                    + scale
                )
                maximum = max(
                    maximum,
                    section_score + horn(axis, level + 1, first, second),
                )
        return maximum

    answer: int | None = None
    for center in product(*(range(cap + 1) for cap in caps)):
        if sum(x * y for x, y in zip(center, lower_weights, strict=True)) > maximum_height:
            continue
        count = math.prod(coordinate + 1 for coordinate in center)
        score = count * (
            2 * sum(x * y for x, y in zip(center, upper_weights, strict=True))
            - 3 * low[2]
            + scale
        )
        for axis in range(3):
            transverse = [coordinate for coordinate in range(3) if coordinate != axis]
            score += horn(
                axis,
                center[axis] + 1,
                center[transverse[0]],
                center[transverse[1]],
            )
        answer = score if answer is None else max(answer, score)
    ensure(answer is not None, "central-box search is empty")
    return answer
def verify(manifest_path: Path) -> dict[str, object]:
    ensure(sys.flags.optimize == 0, "optimized interpreter mode is forbidden")
    certificate_path, certificate_hash, certificate_bytes, scale, root = manifest_input(manifest_path)
    document = decode(certificate_path, "certificate")
    ensure(type(document) is dict, "certificate top level is not an object")
    ensure(
        set(document)
        == {
            "claim",
            "scale",
            "initial",
            "nodes",
            "seconds",
            "complete",
            "leaf_count",
            "tree",
            "unresolved",
        },
        "certificate top-level fields differ",
    )
    ensure(
        document["claim"]
        == "m-D<=1 for every nonempty no-interior ideal in each certified parameter box",
        "certificate claim label differs",
    )
    ensure(document["scale"] == scale, "certificate scale differs")
    ensure(endpoint_pair(document["initial"], "certificate root") == root, "certificate root differs")
    ensure(document["complete"] is True, "certificate completion flag is false")
    ensure(document["unresolved"] == [], "certificate unresolved list is nonempty")
    ensure(exact_int(document["nodes"]) and document["nodes"] > 0, "node count is invalid")
    ensure(exact_int(document["leaf_count"]) and document["leaf_count"] > 0, "leaf count is invalid")
    producer_seconds = document["seconds"]
    ensure(
        type(producer_seconds) in (int, float)
        and math.isfinite(producer_seconds)
        and producer_seconds >= 0,
        "producer duration is invalid",
    )
    tree = document["tree"]
    ensure(type(tree) is list and len(tree) > 0, "tree is invalid")
    ensure(document["nodes"] == len(tree), "node count is inconsistent")

    frontier = deque([(0, root)])
    reached: set[int] = set()
    counts: Counter[str] = Counter()
    leaves: list[
        tuple[int, str, int | None, tuple[int, int, int] | None, tuple[int, int, int] | None]
    ] = []
    while frontier:
        identifier, required_box = frontier.popleft()
        ensure(exact_int(identifier) and 0 <= identifier < len(tree), "child index is out of range")
        ensure(identifier not in reached, f"node {identifier} is reached twice")
        reached.add(identifier)
        node = tree[identifier]
        ensure(type(node) is dict, f"node {identifier} is not an object")
        ensure(type(node.get("kind")) is str, f"node {identifier} kind is invalid")
        kind = node["kind"]
        schemas = {
            "split": {"box", "kind", "axis", "mid", "children"},
            "dp": {"box", "kind", "bound"},
            "continuous": {"box", "kind"},
            "empty": {"box", "kind"},
        }
        ensure(kind in schemas, f"node {identifier} kind is unknown")
        ensure(set(node) == schemas[kind], f"node {identifier} fields differ")
        node_box = endpoint_pair(node["box"], f"node {identifier} box")
        ensure(node_box == required_box, f"node {identifier} has the wrong propagated box")
        clipped = ordered_part(*node_box)
        counts[kind] += 1

        if clipped is None:
            ensure(kind == "empty", f"node {identifier} should be empty")
            leaves.append((identifier, kind, None, None, None))
            continue
        ensure(kind != "empty", f"node {identifier} has a nonempty ordered part")
        low, high = clipped

        if kind == "split":
            axis = node["axis"]
            division = node["mid"]
            children = node["children"]
            ensure(exact_int(axis) and axis in (0, 1, 2), f"node {identifier} axis is invalid")
            ensure(exact_int(division), f"node {identifier} division is nonintegral")
            ensure(low[axis] < division < high[axis], f"node {identifier} division is not internal")
            ensure(type(children) is list and len(children) == 2, f"node {identifier} children invalid")
            ensure(all(exact_int(child) for child in children), f"node {identifier} child is nonintegral")
            ensure(children[0] != children[1], f"node {identifier} has duplicate children")
            first_high = list(high)
            second_low = list(low)
            first_high[axis] = division
            second_low[axis] = division
            frontier.append((children[0], (low, tuple(first_high))))
            frontier.append((children[1], (tuple(second_low), high)))
            continue

        if kind == "continuous":
            ensure(
                low[2] >= 2 * (scale + high[0] + high[1]) + 3 * scale,
                f"node {identifier} does not satisfy the continuous bound",
            )
            leaves.append((identifier, kind, None, low, high))
            continue

        ensure(kind == "dp", f"node {identifier} does not terminate")
        ensure(exact_int(node["bound"]), f"node {identifier} bound is nonintegral")
        leaves.append((identifier, kind, node["bound"], low, high))

    ensure(len(reached) == len(tree), "some stored nodes are unreachable")
    ensure(len(leaves) == document["leaf_count"], "leaf count is inconsistent")
    ensure(counts["split"] + len(leaves) == len(tree), "a branch is unterminated")

    largest: int | None = None
    smallest: int | None = None
    checked_leaves: list[tuple[int, str, int | None]] = []
    for identifier, kind, stored, low, high in sorted(leaves):
        if kind != "dp":
            checked_leaves.append((identifier, kind, None))
            continue
        ensure(low is not None and high is not None and stored is not None, "internal DP leaf error")
        recomputed = explicit_bound(low, high, scale)
        ensure(
            recomputed == stored,
            f"node {identifier} explicit recurrence gives {recomputed}, stored value is {stored}",
        )
        ensure(recomputed <= scale, f"node {identifier} exceeds the acceptance threshold")
        largest = recomputed if largest is None else max(largest, recomputed)
        smallest = recomputed if smallest is None else min(smallest, recomputed)
        checked_leaves.append((identifier, kind, recomputed))

    summary_hash = hashlib.sha256()
    for identifier, kind, bound in checked_leaves:
        summary_hash.update(f"{identifier}:{kind}:{'' if bound is None else bound}\n".encode())

    return {
        "schema_version": 1,
        "component": "R2-path-b-direct",
        "status": "PASS",
        "complete": True,
        "fresh_leaf_recomputation": True,
        "coverage_checked": True,
        "certificate_sha256": certificate_hash,
        "certificate_bytes": certificate_bytes,
        "scale": scale,
        "root": [list(root[0]), list(root[1])],
        "tree_nodes": len(tree),
        "node_kinds": dict(sorted(counts.items())),
        "leaves": len(leaves),
        "dp_leaves": counts["dp"],
        "analytic_leaves": counts["continuous"],
        "empty_leaves": counts["empty"],
        "largest_dp_bound_numerator": largest,
        "smallest_dp_bound_numerator": smallest,
        "leaf_result_sha256": summary_hash.hexdigest(),
        "unresolved": 0,
        "unsupported": 0,
        "arithmetic": "Python arbitrary-precision integers",
        "recurrence": "explicit enumeration of every transverse rectangle transition",
    }


def main() -> int:
    arguments_parser = argparse.ArgumentParser(description=__doc__)
    arguments_parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    arguments = arguments_parser.parse_args()
    try:
        outcome = verify(arguments.manifest.resolve())
    except Exception as error:
        print(f"R2 Path B failed: {type(error).__name__}: {error}", file=sys.stderr)
        return 1
    print(json.dumps(outcome, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
