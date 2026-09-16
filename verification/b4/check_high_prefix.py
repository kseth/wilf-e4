#!/usr/bin/env python3
"""R4a Path A: strict depth-first coverage and subtraction/prefix backend."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "verification/b4/certificate-manifest.json"
BACKEND = ROOT / (
    "artifacts/wilf_four_generators_review_package_2026-09-11/"
    "round5/one_corner_extension/corner_interval_worker.cpp"
)
BACKEND_HASH = "469eca1828ab05bf2f671026dfbcbeccab80110f1bad5a330e71cd60af625bbf"
SCOPE = "all real 1<=b<=c<=M with 6<=M<=42, full corner a permutation of 211, score m-D<=1"


class CheckFailure(RuntimeError):
    pass


def require(condition: bool, detail: str) -> None:
    if not condition:
        raise CheckFailure(detail)


def unique_object(pairs: list) -> dict:
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON field {key!r}")
        result[key] = value
    return result


def reject_constant(value: str) -> None:
    raise CheckFailure(f"nonfinite JSON constant {value!r}")


def decode(raw: bytes) -> object:
    return json.loads(
        raw.decode("utf-8"), object_pairs_hook=unique_object,
        parse_constant=reject_constant,
    )


def box(value: object) -> tuple[tuple[int, ...], tuple[int, ...]]:
    require(type(value) is list and len(value) == 2, "box is not an endpoint pair")
    for endpoint in value:
        require(type(endpoint) is list and len(endpoint) == 3, "endpoint is not a triple")
        require(all(type(x) is int for x in endpoint), "noninteger endpoint")
    low, high = map(tuple, value)
    require(all(a <= b for a, b in zip(low, high)), "inverted raw box")
    return low, high


def tighten(low: tuple, high: tuple) -> tuple[tuple, tuple] | None:
    b0, c0, h0 = low
    b1, c1, h1 = high
    lower = b0, max(b0, c0), max(b0, c0, h0)
    upper = min(b1, c1, h1), min(c1, h1), h1
    return None if any(a > b for a, b in zip(lower, upper)) else (lower, upper)


def inputs(path: Path) -> tuple[dict, dict, bytes, tuple]:
    manifest = decode(path.read_bytes())
    require(type(manifest) is dict, "manifest is not an object")
    require(
        set(manifest) == {"schema_version", "component", "certificate_format", "certificate", "constants"},
        "unexpected manifest fields",
    )
    require(type(manifest["schema_version"]) is int and manifest["schema_version"] == 1, "manifest version")
    require(manifest["component"] == "B4-high-FV", "wrong component")
    require(manifest["certificate_format"] == "wilf-b4-high-interval-tree-historical-v1", "wrong format")
    descriptor = manifest["certificate"]
    require(type(descriptor) is dict and set(descriptor) == {"path", "sha256", "bytes"}, "certificate descriptor")
    name, digest, length = (descriptor[k] for k in ("path", "sha256", "bytes"))
    require(type(name) is str and name and not Path(name).is_absolute(), "certificate path")
    require(type(digest) is str and re.fullmatch("[0-9a-f]{64}", digest) is not None, "certificate hash")
    require(type(length) is int and length > 0, "certificate length")
    source = (ROOT / name).resolve()
    require(source.is_relative_to(ROOT), "certificate path escapes repository")
    raw = source.read_bytes()
    require(len(raw) == length, "certificate byte count mismatch")
    require(hashlib.sha256(raw).hexdigest() == digest, "certificate SHA-256 mismatch")
    constants = manifest["constants"]
    require(type(constants) is dict and set(constants) == {"scale", "root"}, "manifest constants")
    require(type(constants["scale"]) is int and constants["scale"] == 4096, "scale")
    root = box(constants["root"])
    require(root == ((4096, 4096, 24576), (172032, 172032, 172032)), "manifest root")
    data = decode(raw)
    require(type(data) is dict, "certificate is not an object")
    require(set(data) == {"scope", "scale", "initial", "complete", "tree", "nodes", "unresolved", "seconds"}, "certificate fields")
    require(data["scope"] == SCOPE, "historical scope label")
    require(type(data["scale"]) is int and data["scale"] == 4096, "certificate scale")
    require(box(data["initial"]) == root, "certificate root")
    require(data["complete"] is True and data["unresolved"] == [], "partial certificate")
    seconds = data["seconds"]
    require(type(seconds) in (int, float) and math.isfinite(seconds) and seconds >= 0, "producer timing")
    tree = data["tree"]
    require(type(tree) is list and tree, "tree")
    require(type(data["nodes"]) is int and data["nodes"] == len(tree), "node count")
    return manifest, data, raw, root


def run_backend(leaves: list) -> tuple[list[tuple[int, int, int]], dict, str]:
    source_hash = hashlib.sha256(BACKEND.read_bytes()).hexdigest()
    require(source_hash == BACKEND_HASH, "historical backend hash mismatch")
    compiler = shutil.which("c++")
    require(compiler is not None, "C++17 compiler not found")
    version = subprocess.run([compiler, "--version"], capture_output=True, text=True, check=True).stdout.strip()
    with tempfile.TemporaryDirectory(prefix="wilf_r4a_prefix_") as temporary:
        directory = Path(temporary)
        guard = directory / "widths.hpp"
        guard.write_text(
            "#include <limits>\n"
            'static_assert(std::numeric_limits<int>::digits >= 31, "32-bit indices");\n'
            'static_assert(std::numeric_limits<long long>::digits >= 63, "64-bit values");\n',
            encoding="utf-8",
        )
        executable = directory / "checker"
        command = [
            compiler, "-std=c++17", "-O3", "-Wall", "-Wextra", "-pedantic",
            "-include", str(guard), str(BACKEND), "-o", str(executable),
        ]
        built = subprocess.run(command, capture_output=True, text=True)
        require(built.returncode == 0, f"backend compilation failed: {built.stderr}")
        request = "".join(
            " ".join(map(str, (4096, *low, *high))) + "\n"
            for _, _, _, low, high in leaves
        )
        process = subprocess.run([str(executable)], input=request, capture_output=True, text=True)
        require(process.returncode == 0 and not process.stderr.strip(), "backend failed")
        rows = process.stdout.splitlines()
        require(len(rows) == len(leaves), "partial or extra backend response")
        computed = []
        for line in rows:
            tokens = line.split()
            require(len(tokens) == 3 and all(re.fullmatch("-?[0-9]+", t) for t in tokens), "backend bound dimensions/encoding")
            computed.append(tuple(map(int, tokens)))
    require(hashlib.sha256(BACKEND.read_bytes()).hexdigest() == source_hash, "backend source changed")
    return computed, {"path": compiler, "version": version, "command": command, "warnings": built.stderr}, source_hash


def check(path: Path) -> dict:
    require(sys.flags.optimize == 0, "optimized Python execution is unsupported")
    manifest, data, raw, root = inputs(path)
    tree = data["tree"]
    pending, seen, kinds = [(0, root)], set(), Counter()
    terminals, dp = [], []
    schemas = {
        "split": {"box", "kind", "axis", "mid", "children"},
        "dp": {"box", "kind", "bounds"},
        "planar": {"box", "kind"},
        "empty": {"box", "kind"},
    }
    while pending:
        identifier, wanted = pending.pop()
        require(type(identifier) is int and 0 <= identifier < len(tree), "child index")
        require(identifier not in seen, "repeated node/cycle")
        seen.add(identifier)
        node = tree[identifier]
        require(type(node) is dict and type(node.get("kind")) is str, "node object/kind")
        kind = node["kind"]
        require(kind in schemas and set(node) == schemas[kind], "unsupported node kind/schema")
        actual = box(node["box"])
        require(actual == wanted, f"wrong child box at node {identifier}")
        kinds[kind] += 1
        clipped = tighten(*actual)
        if clipped is None:
            require(kind == "empty", "empty ordered part not marked empty")
            terminals.append((identifier, kind, None))
            continue
        require(kind != "empty", "nonempty part marked empty")
        low, high = clipped
        if kind == "split":
            axis, middle, children = (node[k] for k in ("axis", "mid", "children"))
            require(type(axis) is int and 0 <= axis < 3 and type(middle) is int, "split fields")
            require(low[axis] < middle < high[axis], "noninterior split")
            require(type(children) is list and len(children) == 2, "child dimensions")
            require(all(type(c) is int for c in children) and children[0] != children[1], "child types/duplication")
            left, right = list(high), list(low)
            left[axis] = right[axis] = middle
            pending.extend([(children[1], (tuple(right), high)), (children[0], (low, tuple(left)))])
        elif kind == "planar":
            require(low[2] >= 3 * 4096 + 4 * (4096 + high[0] + high[1]), "failed planar leaf")
            terminals.append((identifier, kind, None))
        else:
            bounds = node["bounds"]
            require(type(bounds) is list and len(bounds) == 3 and all(type(v) is int for v in bounds), "DP bounds must be exactly three integers")
            dp.append((identifier, kind, tuple(bounds), low, high))
    require(len(seen) == len(tree), "unreachable stored nodes")
    require(kinds["split"] + len(terminals) + len(dp) == len(tree), "unterminated tree")
    values, compiler, source_hash = run_backend(dp)
    extrema = []
    for leaf, computed in zip(dp, values, strict=True):
        identifier, kind, stored, _, _ = leaf
        require(computed == stored, f"recomputed bounds differ at node {identifier}")
        require(max(computed) <= 4096, f"target failed at node {identifier}")
        terminals.append((identifier, kind, computed))
        extrema.extend(computed)
    digest = hashlib.sha256()
    for identifier, kind, values in sorted(terminals):
        payload = "" if values is None else ",".join(map(str, values))
        digest.update(f"{identifier}:{kind}:{payload}\n".encode())
    return {
        "schema_version": 1, "component": "R4a-path-a-prefix", "status": "PASS",
        "complete": True, "coverage_checked": True, "fresh_leaf_recomputation": True,
        "certificate_sha256": hashlib.sha256(raw).hexdigest(), "certificate_bytes": len(raw),
        "scale": 4096, "root": [list(x) for x in root],
        "tree_nodes": len(tree), "node_kinds": dict(sorted(kinds.items())),
        "leaves": len(terminals), "dp_leaves": kinds["dp"], "analytic_leaves": kinds["planar"],
        "empty_leaves": kinds["empty"], "corner_bounds_checked": len(extrema),
        "largest_dp_bound_numerator": max(extrema) if extrema else None,
        "smallest_dp_bound_numerator": min(extrema) if extrema else None,
        "leaf_result_sha256": digest.hexdigest(), "unresolved": 0, "unsupported": 0,
        "arithmetic": "C++ signed integers >=64 bits; indices >=32 bits; root bounds proved",
        "backend_path": str(BACKEND.relative_to(ROOT)), "backend_sha256": source_hash,
        "compiler": compiler, "recurrence": "subtraction statistics and prefix maxima",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=MANIFEST)
    args = parser.parse_args()
    try:
        print(json.dumps(check(args.manifest.resolve()), sort_keys=True))
        return 0
    except Exception as error:
        print(f"R4a Path A failed: {type(error).__name__}: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
