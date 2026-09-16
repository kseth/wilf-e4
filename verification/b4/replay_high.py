#!/usr/bin/env python3
"""Fresh complete R4a replay, with separate checkers and temporary C++ builds."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[2]
COMPONENT = ROOT / "verification/b4"
SOURCES = {
    "runner": Path("verification/b4/replay_high.py"),
    "path_a": Path("verification/b4/check_high_prefix.py"),
    "path_b": Path("verification/b4/check_high_direct.py"),
    "backend_a": Path(
        "artifacts/wilf_four_generators_review_package_2026-09-11/"
        "round5/one_corner_extension/corner_interval_worker.cpp"
    ),
    "backend_b": Path("verification/b4/direct_clipped_worker.cpp"),
    "manifest": Path("verification/b4/certificate-manifest.json"),
    "certificate": Path(
        "artifacts/wilf_four_generators_review_package_2026-09-11/"
        "round5/one_corner_extension/short_corner_complete_certificate.json"
    ),
    "contract": Path("paper/short-corner-interval-specification.md"),
    "decision": Path("research/b4-simplification-decision.md"),
    "compactness": Path("paper/short-corner-compactness.md"),
    "clipping": Path("paper/central-box-horns.md"),
}
INDEPENDENT_FIELDS = {
    "component", "backend_path", "backend_sha256", "compiler", "recurrence",
}
RESULT_FIELDS = {
    "schema_version", "component", "status", "complete", "coverage_checked",
    "fresh_leaf_recomputation", "certificate_sha256", "certificate_bytes",
    "scale", "root", "tree_nodes", "node_kinds", "leaves", "dp_leaves",
    "analytic_leaves", "empty_leaves", "corner_bounds_checked",
    "largest_dp_bound_numerator", "smallest_dp_bound_numerator",
    "leaf_result_sha256", "unresolved", "unsupported", "arithmetic",
    "backend_path", "backend_sha256", "compiler", "recurrence",
}


class ReplayFailure(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ReplayFailure(message)


def utc() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(*args: str) -> str:
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    require(result.returncode == 0, f"git failed: {result.stderr}")
    return result.stdout.strip()


def execute(source: Path, manifest: Path, optimized: bool = False) -> tuple:
    command = [sys.executable, *(["-O"] if optimized else []), "-I", "-B",
               str(source), "--manifest", str(manifest)]
    environment = os.environ.copy()
    for name in ("PYTHONOPTIMIZE", "PYTHONPATH", "PYTHONHOME"):
        environment.pop(name, None)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    started, clock = utc(), time.monotonic()
    process = subprocess.run(
        command, cwd=ROOT, env=environment, capture_output=True, text=True,
    )
    return process, {
        "command": command, "started_utc": started, "finished_utc": utc(),
        "elapsed_seconds": time.monotonic() - clock, "exit_status": process.returncode,
        "stdout_sha256": hashlib.sha256(process.stdout.encode()).hexdigest(),
        "stderr": process.stderr,
    }


def negative_tests() -> list[dict]:
    original = json.loads((ROOT / SOURCES["manifest"]).read_text())
    results = []
    def rejected(label: str, manifest: Path, optimized: bool = False) -> None:
        for name in ("path_a", "path_b"):
            process, info = execute(ROOT / SOURCES[name], manifest, optimized)
            require(process.returncode != 0, f"{name} accepted mutation {label}")
            require("failed:" in process.stderr, f"{name} did not report a controlled rejection")
            results.append({
                "checker": name, "mutation": label, "rejected": True, **info,
            })

    rejected("optimized_execution", ROOT / SOURCES["manifest"], optimized=True)
    # Synthetic proof data stays in a unique component-local directory.
    with tempfile.TemporaryDirectory(prefix=".r4a-negative-", dir=COMPONENT) as temporary:
        directory = Path(temporary)
        bad_manifest = directory / "manifest.json"
        changed = json.loads(json.dumps(original))
        changed["certificate"]["sha256"] = "0" * 64
        bad_manifest.write_text(json.dumps(changed))
        rejected("certificate_hash_mismatch", bad_manifest)
        bad_manifest.write_text('{"schema_version":1,' + json.dumps(original)[1:])
        rejected("duplicate_manifest_field", bad_manifest)
        root = original["constants"]["root"]
        base = {
            "scope": "all real 1<=b<=c<=M with 6<=M<=42, full corner a permutation of 211, score m-D<=1",
            "scale": 4096, "initial": root, "complete": True, "tree": [],
            "nodes": 1, "unresolved": [], "seconds": 0,
        }
        mutants = [
            ("unsupported_node_kind", [{"box": root, "kind": "unsupported"}]),
            ("four_cached_corner_bounds", [{"box": root, "kind": "dp", "bounds": [0, 0, 0, 0]}]),
        ]
        left = [[4097, 4096, 24576], [88064, 172032, 172032]]
        right = [[88064, 4096, 24576], [172032, 172032, 172032]]
        mutants.append(("child_boundary_gap", [
            {"box": root, "kind": "split", "axis": 0, "mid": 88064, "children": [1, 2]},
            {"box": left, "kind": "planar"}, {"box": right, "kind": "planar"},
        ]))
        for label, nodes in mutants:
            value = {**base, "nodes": len(nodes), "tree": nodes}
            certificate = directory / "certificate.json"
            certificate.write_text(json.dumps(value))
            changed = json.loads(json.dumps(original))
            changed["certificate"] = {
                "path": str(certificate.relative_to(ROOT)),
                "sha256": digest(certificate), "bytes": certificate.stat().st_size,
            }
            bad_manifest.write_text(json.dumps(changed))
            rejected(label, bad_manifest)
    return results


def result_value(process: subprocess.CompletedProcess, name: str) -> dict:
    require(process.returncode == 0 and not process.stderr.strip(), f"{name} failed: {process.stderr}")
    lines = process.stdout.splitlines()
    require(len(lines) == 1, f"{name} has incomplete or extra output")
    value = json.loads(lines[0])
    require(type(value) is dict and set(value) == RESULT_FIELDS, f"{name} result schema")
    expected_component = "R4a-path-a-prefix" if name == "path_a" else "R4a-path-b-direct"
    require(value["component"] == expected_component and value["status"] == "PASS", f"{name} result identity")
    require(type(value["schema_version"]) is int and value["schema_version"] == 1, "result version")
    for field in ("complete", "coverage_checked", "fresh_leaf_recomputation"):
        require(value[field] is True, f"{name} omitted {field}")
    for field in (
        "certificate_bytes", "scale", "tree_nodes", "leaves", "dp_leaves", "analytic_leaves",
        "empty_leaves", "corner_bounds_checked", "unresolved", "unsupported",
        "largest_dp_bound_numerator", "smallest_dp_bound_numerator",
    ):
        require(type(value[field]) is int, f"{name} noninteger {field}")
    require(value["unresolved"] == value["unsupported"] == 0, f"{name} incomplete")
    require(value["scale"] == 4096 and value["largest_dp_bound_numerator"] <= 4096, f"{name} threshold")
    require(value["smallest_dp_bound_numerator"] <= value["largest_dp_bound_numerator"], f"{name} extrema")
    require(value["root"] == [[4096, 4096, 24576], [172032, 172032, 172032]], f"{name} root")
    require(value["tree_nodes"] > 0 and value["dp_leaves"] > 0, f"{name} empty result")
    require(value["corner_bounds_checked"] == 3 * value["dp_leaves"], f"{name} missing corner")
    require(value["leaves"] == value["dp_leaves"] + value["analytic_leaves"] + value["empty_leaves"], f"{name} leaf partition")
    kinds = value["node_kinds"]
    require(type(kinds) is dict and set(kinds) <= {"split", "dp", "planar", "empty"}, f"{name} node kinds")
    require(all(type(n) is int and n >= 0 for n in kinds.values()), f"{name} kind count")
    require(sum(kinds.values()) == value["tree_nodes"], f"{name} missing nodes")
    require(kinds.get("split", 0) + value["leaves"] == value["tree_nodes"], f"{name} tree termination")
    require(
        kinds.get("dp", 0) == value["dp_leaves"]
        and kinds.get("planar", 0) == value["analytic_leaves"]
        and kinds.get("empty", 0) == value["empty_leaves"],
        f"{name} inconsistent kinds",
    )
    for field in ("certificate_sha256", "leaf_result_sha256", "backend_sha256"):
        require(type(value[field]) is str and re.fullmatch("[0-9a-f]{64}", value[field]), f"{name} {field}")
    require(value["backend_path"] == str(SOURCES["backend_a" if name == "path_a" else "backend_b"]), f"{name} backend")
    require(value["arithmetic"] == "C++ signed integers >=64 bits; indices >=32 bits; root bounds proved", f"{name} arithmetic")
    expected_recurrence = (
        "subtraction statistics and prefix maxima" if name == "path_a"
        else "disjoint statistics and explicit rectangle transitions"
    )
    require(value["recurrence"] == expected_recurrence, f"{name} recurrence")
    compiler = value["compiler"]
    require(type(compiler) is dict and set(compiler) == {"path", "version", "command", "warnings"}, f"{name} compiler metadata")
    require(type(compiler["version"]) is str and compiler["version"], f"{name} compiler version")
    require(type(compiler["command"]) is list and all(type(s) is str for s in compiler["command"]), f"{name} build command")
    return value


def write_record(path: Path, record: dict) -> None:
    path.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def replay(record_path: Path) -> int:
    clock = time.monotonic()
    record = {
        "schema_version": 1, "component": "R4a", "status": "FAIL",
        "exit_status": 1,
        "started_utc": utc(), "complete": False, "fresh": True, "cache_free": True,
        "record_path": str(record_path.relative_to(ROOT)), "working_directory": str(ROOT),
        "repository_input_commit": None,
    }
    try:
        require(sys.flags.optimize == 0, "optimized runner mode is unsupported")
        require(not git("status", "--porcelain", "--untracked-files=no"), "tracked worktree is dirty")
        for relative in SOURCES.values():
            require((ROOT / relative).is_file(), f"missing input {relative}")
            git("ls-files", "--error-unmatch", str(relative))
        record["repository_input_commit"] = git("rev-parse", "HEAD")
        record["tracked_worktree_clean_before_replay"] = True
        snapshot = {name: digest(ROOT / path) for name, path in SOURCES.items()}
        record["sources"] = {
            name: {"path": str(path), "sha256": snapshot[name]}
            for name, path in SOURCES.items()
        }
        record["theorem_contract"] = {
            **record["sources"]["contract"], "statement": "B4-high-FV",
            "parameter_region": "1 <= b <= c <= Q, 6 <= Q <= 42; all three short-corner positions",
        }
        record["environment"] = {
            "platform": platform.platform(), "machine": platform.machine(),
            "python_executable": sys.executable, "python_version": sys.version,
            "dependencies": "Python standard library and a C++17 compiler",
            "integer_semantics": "Python arbitrary precision; C++ signed values >=64 bits, indices >=32 bits",
        }
        record["negative_tests"] = negative_tests()
        values, processes = {}, {}
        for name in ("path_a", "path_b"):
            process, info = execute(ROOT / SOURCES[name], ROOT / SOURCES["manifest"])
            processes[name] = info
            record["processes"] = processes
            values[name] = result_value(process, name)
            record[f"{name}_result"] = values[name]
            require(values[name]["certificate_sha256"] == snapshot["certificate"], f"{name} certificate identity")
            require(values[name]["backend_sha256"] == snapshot["backend_a" if name == "path_a" else "backend_b"], f"{name} source identity")
        fields = sorted(RESULT_FIELDS - INDEPENDENT_FIELDS)
        require(all(values["path_a"][f] == values["path_b"][f] for f in fields), "independent paths disagree")
        require(
            all(digest(ROOT / path) == snapshot[name] for name, path in SOURCES.items()),
            "proof input changed during replay",
        )
        record.update({
            "status": "PASS", "exit_status": 0, "complete": True,
            "unresolved": 0, "unsupported": 0,
            "independent_agreement": {
                "status": "PASS", "fields_compared": fields,
                "note": "Both paths independently proved coverage and recomputed all bounds before comparison.",
            },
            "replay_command": [sys.executable, str(SOURCES["runner"])],
            "historical_archive_modified": False,
            "claim_established_by_this_replay": "B4-high-FV, conditional on the mathematical specification and its coverage proof.",
            "does_not_establish": [
                "the B4 low-height finite lemma or R4b",
                "external mathematical review or proof-assistant formalization",
                "the global four-generator theorem",
            ],
        })
        record["finished_utc"], record["elapsed_seconds"] = utc(), time.monotonic() - clock
        write_record(record_path, record)
        print(json.dumps({
            "status": "PASS", "component": "R4a",
            "tree_nodes": values["path_a"]["tree_nodes"],
            "dp_leaves": values["path_a"]["dp_leaves"],
            "corner_bounds_checked_per_path": values["path_a"]["corner_bounds_checked"],
            "largest_bound": values["path_a"]["largest_dp_bound_numerator"],
            "scale": 4096, "negative_tests_rejected": len(record["negative_tests"]),
        }, indent=2))
        return 0
    except Exception as error:
        record.update({
            "status": "FAIL", "exit_status": 1, "complete": False,
            "error_type": type(error).__name__, "error": str(error),
            "finished_utc": utc(), "elapsed_seconds": time.monotonic() - clock,
        })
        write_record(record_path, record)
        print(f"R4a replay failed: {type(error).__name__}: {error}", file=sys.stderr)
        return 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", type=Path, default=COMPONENT / "r4a-replay.json")
    args = parser.parse_args()
    output = args.record.resolve()
    if output.parent != COMPONENT or re.fullmatch(r"r4a-replay(?:-[a-zA-Z0-9_-]+)?\.json", output.name) is None:
        parser.error("--record must be an r4a-replay[-suffix].json file in verification/b4")
    return replay(output)


if __name__ == "__main__":
    raise SystemExit(main())
