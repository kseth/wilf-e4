#!/usr/bin/env python3
"""R4a Path B: independent breadth-first coverage and direct-transition backend."""

from __future__ import annotations

import argparse
from collections import Counter, deque
import hashlib
import json
import math
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

REPOSITORY = Path(__file__).resolve().parents[2]
DEFAULT_MANIFEST = REPOSITORY / "verification/b4/certificate-manifest.json"
WORKER_SOURCE = REPOSITORY / "verification/b4/direct_clipped_worker.cpp"


class VerificationError(RuntimeError):
    pass


def ensure(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def reject_duplicates(pairs: list) -> dict:
    obj = {}
    for name, value in pairs:
        if name in obj:
            raise VerificationError(f"repeated JSON key {name!r}")
        obj[name] = value
    return obj


def bad_number(token: str) -> None:
    raise VerificationError(f"unsupported numeric constant {token!r}")


def parse(payload: bytes) -> object:
    return json.loads(
        payload.decode("utf-8"), object_pairs_hook=reject_duplicates,
        parse_constant=bad_number,
    )


def endpoints(value: object) -> tuple[tuple, tuple]:
    ensure(type(value) is list and len(value) == 2, "invalid endpoint pair")
    for side in value:
        ensure(type(side) is list and len(side) == 3, "invalid endpoint dimensions")
        ensure(all(type(v) is int for v in side), "nonintegral endpoint")
    low, high = tuple(value[0]), tuple(value[1])
    ensure(all(low[i] <= high[i] for i in range(3)), "reversed raw interval")
    return low, high


def ordered_part(low: tuple, high: tuple) -> tuple[tuple, tuple] | None:
    lower, upper = list(low), list(high)
    while True:
        before = tuple(lower), tuple(upper)
        for i in (0, 1):
            lower[i + 1] = max(lower[i + 1], lower[i])
            upper[i] = min(upper[i], upper[i + 1])
        if any(lower[i] > upper[i] for i in range(3)):
            return None
        after = tuple(lower), tuple(upper)
        if after == before:
            return after


def read_certificate(manifest_path: Path) -> tuple[dict, bytes, tuple]:
    manifest = parse(manifest_path.read_bytes())
    ensure(type(manifest) is dict, "manifest is not a dictionary")
    ensure(
        set(manifest) == {"schema_version", "component", "certificate_format", "certificate", "constants"},
        "unsupported manifest schema",
    )
    ensure(type(manifest["schema_version"]) is int and manifest["schema_version"] == 1, "manifest version")
    ensure(manifest["component"] == "B4-high-FV", "manifest component")
    ensure(manifest["certificate_format"] == "wilf-b4-high-interval-tree-historical-v1", "manifest format")
    constants = manifest["constants"]
    ensure(type(constants) is dict and set(constants) == {"root", "scale"}, "constant fields")
    ensure(type(constants["scale"]) is int and constants["scale"] == 4096, "constant scale")
    root = endpoints(constants["root"])
    ensure(root == ((4096, 4096, 24576), (172032, 172032, 172032)), "constant root")
    info = manifest["certificate"]
    ensure(type(info) is dict and set(info) == {"path", "bytes", "sha256"}, "certificate fields")
    filename, size, expected_hash = info["path"], info["bytes"], info["sha256"]
    ensure(type(filename) is str and filename != "", "certificate filename")
    ensure(not Path(filename).is_absolute(), "absolute certificate filename")
    source = (REPOSITORY / filename).resolve()
    ensure(source.is_relative_to(REPOSITORY), "certificate filename leaves repository")
    ensure(type(size) is int and size > 0, "certificate size")
    ensure(
        type(expected_hash) is str and len(expected_hash) == 64
        and set(expected_hash) <= set("0123456789abcdef"),
        "certificate checksum",
    )
    raw = source.read_bytes()
    ensure(len(raw) == size, "certificate size does not match")
    ensure(hashlib.sha256(raw).hexdigest() == expected_hash, "certificate checksum does not match")
    data = parse(raw)
    ensure(type(data) is dict, "certificate top-level type")
    ensure(
        set(data) == {"scope", "scale", "initial", "complete", "tree", "nodes", "unresolved", "seconds"},
        "unsupported certificate fields",
    )
    ensure(
        data["scope"] == "all real 1<=b<=c<=M with 6<=M<=42, full corner a permutation of 211, score m-D<=1",
        "historical scope",
    )
    ensure(type(data["scale"]) is int and data["scale"] == 4096, "document scale")
    ensure(endpoints(data["initial"]) == root, "document root")
    ensure(data["complete"] is True and data["unresolved"] == [], "unfinished certificate")
    ensure(type(data["seconds"]) in (int, float) and math.isfinite(data["seconds"]) and data["seconds"] >= 0, "invalid timing metadata")
    ensure(type(data["tree"]) is list and data["tree"], "document tree")
    ensure(type(data["nodes"]) is int and data["nodes"] == len(data["tree"]), "document node count")
    return data, raw, root


def evaluate_dp(leaves: list) -> tuple[list[tuple], dict, str]:
    checksum = hashlib.sha256(WORKER_SOURCE.read_bytes()).hexdigest()
    compiler = shutil.which("c++")
    ensure(compiler is not None, "C++17 toolchain unavailable")
    version_process = subprocess.run([compiler, "--version"], capture_output=True, text=True)
    ensure(version_process.returncode == 0, "compiler version query failed")
    with tempfile.TemporaryDirectory(prefix="wilf_r4a_direct_") as directory:
        binary = Path(directory) / "worker"
        build_command = [
            compiler, "-O3", "-std=c++17", "-Wall", "-Wextra", "-pedantic",
            str(WORKER_SOURCE), "-o", str(binary),
        ]
        build = subprocess.run(build_command, capture_output=True, text=True)
        ensure(build.returncode == 0, f"direct worker did not compile: {build.stderr}")
        requests = [
            " ".join(str(v) for v in [4096, *low, *high])
            for _, _, low, high in leaves
        ]
        worker = subprocess.run(
            [str(binary)], input="".join(line + "\n" for line in requests),
            capture_output=True, text=True,
        )
        ensure(worker.returncode == 0 and worker.stderr.strip() == "", "direct worker failure")
        replies = worker.stdout.splitlines()
        ensure(len(replies) == len(requests), "incomplete/extra direct worker reply")
        results = []
        for reply in replies:
            fields = reply.split()
            ensure(
                len(fields) == 3 and all(re.fullmatch(r"-?[0-9]+", f) is not None for f in fields),
                "direct bound encoding/dimensions",
            )
            results.append(tuple(int(f) for f in fields))
    ensure(hashlib.sha256(WORKER_SOURCE.read_bytes()).hexdigest() == checksum, "direct source changed")
    return results, {
        "path": compiler, "version": version_process.stdout.strip(),
        "command": build_command, "warnings": build.stderr,
    }, checksum


def verify(manifest_path: Path) -> dict:
    ensure(sys.flags.optimize == 0, "optimized interpreter mode is forbidden")
    data, raw, root = read_certificate(manifest_path)
    tree = data["tree"]
    queue, reached, counts = deque([(0, root)]), set(), Counter()
    accepted, leaves = [], []
    while queue:
        index, expected = queue.popleft()
        ensure(type(index) is int and 0 <= index < len(tree), "out-of-range child")
        ensure(index not in reached, "shared child or cyclic tree")
        reached.add(index)
        node = tree[index]
        ensure(type(node) is dict and type(node.get("kind")) is str, "invalid node type")
        kind = node["kind"]
        schemas = {
            "planar": {"kind", "box"}, "empty": {"kind", "box"},
            "dp": {"kind", "box", "bounds"},
            "split": {"kind", "box", "axis", "mid", "children"},
        }
        ensure(kind in schemas and set(node) == schemas[kind], "unrecognized node schema")
        raw_box = endpoints(node["box"])
        ensure(raw_box == expected, f"box propagation failed at node {index}")
        counts[kind] += 1
        clipped = ordered_part(*raw_box)
        if clipped is None:
            ensure(kind == "empty", "empty part has wrong node type")
            accepted.append((index, kind, None))
            continue
        ensure(kind != "empty", "false empty node")
        low, high = clipped
        if kind == "split":
            axis, division, children = node["axis"], node["mid"], node["children"]
            ensure(type(axis) is int and axis in (0, 1, 2) and type(division) is int, "invalid division")
            ensure(low[axis] < division < high[axis], "division outside tightened interval")
            ensure(type(children) is list and len(children) == 2, "division child dimensions")
            ensure(all(type(v) is int for v in children) and children[0] != children[1], "division child values")
            first_high, second_low = list(high), list(low)
            first_high[axis] = second_low[axis] = division
            queue.append((children[0], (low, tuple(first_high))))
            queue.append((children[1], (tuple(second_low), high)))
        elif kind == "planar":
            ensure(low[2] >= 3 * 4096 + 4 * (4096 + high[0] + high[1]), "planar rule not valid")
            accepted.append((index, kind, None))
        else:
            bounds = node["bounds"]
            ensure(
                type(bounds) is list and len(bounds) == 3 and all(type(v) is int for v in bounds),
                "direct DP record must have three integer bounds",
            )
            leaves.append((index, tuple(bounds), low, high))
    ensure(len(reached) == len(tree), "unreachable tree entries")
    ensure(counts["split"] + len(accepted) + len(leaves) == len(tree), "nonterminal branch")
    # Coverage is finished before any numerical leaf evaluation.
    leaves.sort()
    computed, compiler, checksum = evaluate_dp(leaves)
    numbers = []
    for position in range(len(leaves)):
        index, stated, _, _ = leaves[position]
        result = computed[position]
        ensure(result == stated, f"direct recurrence differs at node {index}")
        ensure(all(v <= 4096 for v in result), f"direct target fails at node {index}")
        accepted.append((index, "dp", result))
        numbers.extend(result)
    digest = hashlib.sha256()
    for index, kind, result in sorted(accepted):
        suffix = "" if result is None else ",".join(str(v) for v in result)
        digest.update(f"{index}:{kind}:{suffix}\n".encode("ascii"))
    return {
        "schema_version": 1, "component": "R4a-path-b-direct", "status": "PASS",
        "complete": True, "coverage_checked": True, "fresh_leaf_recomputation": True,
        "certificate_sha256": hashlib.sha256(raw).hexdigest(), "certificate_bytes": len(raw),
        "scale": 4096, "root": [list(v) for v in root],
        "tree_nodes": len(tree), "node_kinds": dict(sorted(counts.items())),
        "leaves": len(accepted), "dp_leaves": counts["dp"], "analytic_leaves": counts["planar"],
        "empty_leaves": counts["empty"], "corner_bounds_checked": len(numbers),
        "largest_dp_bound_numerator": max(numbers) if numbers else None,
        "smallest_dp_bound_numerator": min(numbers) if numbers else None,
        "leaf_result_sha256": digest.hexdigest(), "unresolved": 0, "unsupported": 0,
        "arithmetic": "C++ signed integers >=64 bits; indices >=32 bits; root bounds proved",
        "backend_path": str(WORKER_SOURCE.relative_to(REPOSITORY)), "backend_sha256": checksum,
        "compiler": compiler, "recurrence": "disjoint statistics and explicit rectangle transitions",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    arguments = parser.parse_args()
    try:
        print(json.dumps(verify(arguments.manifest.resolve()), sort_keys=True))
        return 0
    except Exception as error:
        print(f"R4a Path B failed: {type(error).__name__}: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
