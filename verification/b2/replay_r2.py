#!/usr/bin/env python3
"""Fresh complete R2 replay of both independent B2 interval-tree paths."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import tempfile
import time


ROOT = Path(__file__).resolve().parents[2]
RUNNER = Path(__file__).resolve()
PATH_A_REL = Path("verification/b2/check_interval_prefix.py")
PATH_B_REL = Path("verification/b2/check_interval_direct.py")
MANIFEST_REL = Path("verification/b2/certificate-manifest.json")
CERTIFICATE_REL = Path(
    "artifacts/wilf_four_generators_review_package_2026-09-11/"
    "round5/weight_arrangement/full_interval_certificate.json"
)
SPEC_REL = Path("paper/no-corner-interval-specification.md")
DECISION_REL = Path("research/b2-simplification-decision.md")
DEFAULT_RECORD_REL = Path("verification/b2/r2-replay.json")

COMMON_RESULT_FIELDS = {
    "schema_version",
    "component",
    "status",
    "complete",
    "fresh_leaf_recomputation",
    "coverage_checked",
    "certificate_sha256",
    "certificate_bytes",
    "scale",
    "root",
    "tree_nodes",
    "node_kinds",
    "leaves",
    "dp_leaves",
    "analytic_leaves",
    "empty_leaves",
    "largest_dp_bound_numerator",
    "smallest_dp_bound_numerator",
    "leaf_result_sha256",
    "unresolved",
    "unsupported",
    "arithmetic",
}
AGREEMENT_FIELDS = tuple(
    sorted(
        COMMON_RESULT_FIELDS
        - {
            "component",
        }
    )
)


class ReplayFailure(RuntimeError):
    """Raised whenever the combined replay cannot establish B2.2-FV."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ReplayFailure(message)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def checked_output(command: list[str]) -> str:
    result = subprocess.run(
        command,
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise ReplayFailure(
            f"command failed with exit {result.returncode}: {command!r}; "
            f"stderr={result.stderr.strip()!r}"
        )
    return result.stdout.strip()


def git_head() -> str:
    value = checked_output(["git", "rev-parse", "HEAD"])
    require(len(value) == 40, f"unexpected git commit: {value!r}")
    return value


def require_clean_tracked_worktree() -> None:
    status = checked_output(["git", "status", "--porcelain", "--untracked-files=no"])
    require(not status, f"tracked worktree is not clean before replay: {status!r}")


def checker_environment() -> dict[str, str]:
    environment = os.environ.copy()
    environment.pop("PYTHONOPTIMIZE", None)
    environment.pop("PYTHONPATH", None)
    environment.pop("PYTHONHOME", None)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    return environment


def checker_command(source: Path, manifest: Path, optimized: bool = False) -> list[str]:
    command = [sys.executable]
    if optimized:
        command.append("-O")
    command.extend(["-I", "-B", str(source), "--manifest", str(manifest)])
    return command


def run_process(command: list[str]) -> tuple[subprocess.CompletedProcess[str], float]:
    start = time.monotonic()
    result = subprocess.run(
        command,
        cwd=ROOT,
        env=checker_environment(),
        check=False,
        capture_output=True,
        text=True,
    )
    return result, time.monotonic() - start


def parse_checker_result(stdout: str, expected_component: str, path_label: str) -> dict[str, object]:
    lines = [line for line in stdout.splitlines() if line.strip()]
    require(len(lines) == 1, f"{path_label} emitted {len(lines)} nonempty output lines")
    try:
        value = json.loads(lines[0])
    except json.JSONDecodeError as error:
        raise ReplayFailure(f"{path_label} emitted malformed JSON: {error}") from error
    require(isinstance(value, dict), f"{path_label} output is not an object")
    expected_fields = COMMON_RESULT_FIELDS | ({"recurrence"} if path_label == "Path B" else set())
    require(set(value) == expected_fields, f"{path_label} output schema differs")
    require(value["schema_version"] == 1, f"{path_label} schema version differs")
    require(value["component"] == expected_component, f"{path_label} component differs")
    require(value["status"] == "PASS", f"{path_label} did not pass")
    require(value["complete"] is True, f"{path_label} was not complete")
    require(value["fresh_leaf_recomputation"] is True, f"{path_label} used stored leaf decisions")
    require(value["coverage_checked"] is True, f"{path_label} did not check coverage")
    require(value["unresolved"] == 0, f"{path_label} has unresolved cases")
    require(value["unsupported"] == 0, f"{path_label} has unsupported cases")
    require(value["arithmetic"] == "Python arbitrary-precision integers", f"{path_label} arithmetic differs")

    integer_fields = (
        "certificate_bytes",
        "scale",
        "tree_nodes",
        "leaves",
        "dp_leaves",
        "analytic_leaves",
        "empty_leaves",
        "largest_dp_bound_numerator",
        "smallest_dp_bound_numerator",
    )
    require(
        all(type(value[field]) is int for field in integer_fields),
        f"{path_label} has a noninteger count or bound",
    )
    require(value["scale"] == 4096, f"{path_label} scale differs")
    require(value["tree_nodes"] > 0 and value["leaves"] > 0, f"{path_label} counts are empty")
    require(
        value["dp_leaves"] + value["analytic_leaves"] + value["empty_leaves"]
        == value["leaves"],
        f"{path_label} leaf counts do not partition the leaves",
    )
    require(value["largest_dp_bound_numerator"] <= value["scale"], f"{path_label} threshold fails")
    require(
        value["smallest_dp_bound_numerator"] <= value["largest_dp_bound_numerator"],
        f"{path_label} bound interval is reversed",
    )
    kinds = value["node_kinds"]
    require(isinstance(kinds, dict), f"{path_label} node kinds are missing")
    require(set(kinds) <= {"split", "dp", "continuous", "empty"}, f"{path_label} kind is unsupported")
    require(all(type(count) is int and count >= 0 for count in kinds.values()), f"{path_label} kind count invalid")
    require(sum(kinds.values()) == value["tree_nodes"], f"{path_label} kind counts are incomplete")
    require(kinds.get("split", 0) + value["leaves"] == value["tree_nodes"], f"{path_label} tree count fails")
    require(kinds.get("dp", 0) == value["dp_leaves"], f"{path_label} DP count differs")
    require(kinds.get("continuous", 0) == value["analytic_leaves"], f"{path_label} analytic count differs")
    require(kinds.get("empty", 0) == value["empty_leaves"], f"{path_label} empty count differs")

    for field in ("certificate_sha256", "leaf_result_sha256"):
        digest = value[field]
        require(
            isinstance(digest, str)
            and len(digest) == 64
            and all(char in "0123456789abcdef" for char in digest),
            f"{path_label} {field} is malformed",
        )
    root = value["root"]
    require(
        root == [[4096, 4096, 20480], [98304, 98304, 98304]],
        f"{path_label} root differs",
    )
    if path_label == "Path B":
        require(
            value["recurrence"] == "explicit enumeration of every transverse rectangle transition",
            "Path B recurrence label differs",
        )
    return value


def negative_tests(path_a: Path, path_b: Path, manifest: Path) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for label, source in (("Path A", path_a), ("Path B", path_b)):
        command = checker_command(source, manifest, optimized=True)
        process, elapsed = run_process(command)
        require(process.returncode != 0, f"{label} accepted optimized execution")
        results.append(
            {
                "checker": label,
                "mutation": "optimized_execution",
                "rejected": True,
                "exit_status": process.returncode,
                "elapsed_seconds": elapsed,
                "stderr_sha256": hashlib.sha256(process.stderr.encode()).hexdigest(),
            }
        )

    manifest_value = json.loads(manifest.read_text(encoding="utf-8"))
    manifest_value["certificate"]["sha256"] = "0" * 64
    with tempfile.TemporaryDirectory(prefix="wilf_r2_negative_") as temporary:
        bad_manifest = Path(temporary) / "bad-manifest.json"
        bad_manifest.write_text(json.dumps(manifest_value), encoding="utf-8")
        for label, source in (("Path A", path_a), ("Path B", path_b)):
            command = checker_command(source, bad_manifest)
            process, elapsed = run_process(command)
            require(process.returncode != 0, f"{label} accepted a certificate hash mismatch")
            results.append(
                {
                    "checker": label,
                    "mutation": "certificate_hash_mismatch",
                    "rejected": True,
                    "exit_status": process.returncode,
                    "elapsed_seconds": elapsed,
                    "stderr_sha256": hashlib.sha256(process.stderr.encode()).hexdigest(),
                }
            )

    root = [[4096, 4096, 20480], [98304, 98304, 98304]]
    malformed_tree = {
        "claim": "m-D<=1 for every nonempty no-interior ideal in each certified parameter box",
        "scale": 4096,
        "initial": root,
        "nodes": 1,
        "seconds": 0,
        "complete": True,
        "leaf_count": 1,
        "tree": [{"box": root, "kind": "unsupported"}],
        "unresolved": [],
    }
    with tempfile.TemporaryDirectory(prefix=".r2_structural_", dir=manifest.parent) as temporary:
        bad_certificate = Path(temporary) / "bad-certificate.json"
        bad_certificate.write_text(json.dumps(malformed_tree), encoding="utf-8")
        bad_manifest_value = json.loads(manifest.read_text(encoding="utf-8"))
        bad_manifest_value["certificate"] = {
            "path": str(bad_certificate.relative_to(ROOT)),
            "sha256": sha256(bad_certificate),
            "bytes": bad_certificate.stat().st_size,
        }
        bad_manifest = Path(temporary) / "bad-tree-manifest.json"
        bad_manifest.write_text(json.dumps(bad_manifest_value), encoding="utf-8")
        for label, source in (("Path A", path_a), ("Path B", path_b)):
            command = checker_command(source, bad_manifest)
            process, elapsed = run_process(command)
            require(process.returncode != 0, f"{label} accepted an unsupported node kind")
            results.append(
                {
                    "checker": label,
                    "mutation": "unsupported_root_node_kind_with_matching_hash",
                    "rejected": True,
                    "exit_status": process.returncode,
                    "elapsed_seconds": elapsed,
                    "stderr_sha256": hashlib.sha256(process.stderr.encode()).hexdigest(),
                }
            )
    return results


def write_record(path: Path, value: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def replay(record_path: Path) -> int:
    started_utc = utc_now()
    start = time.monotonic()
    path_a = ROOT / PATH_A_REL
    path_b = ROOT / PATH_B_REL
    manifest = ROOT / MANIFEST_REL
    certificate = ROOT / CERTIFICATE_REL
    specification = ROOT / SPEC_REL
    decision = ROOT / DECISION_REL
    base: dict[str, object] = {
        "schema_version": 1,
        "component": "R2",
        "started_utc": started_utc,
        "repository_input_commit": None,
        "working_directory_repository_relative": ".",
        "fresh": True,
        "cache_free": True,
        "complete": False,
        "status": "FAIL",
        "record_path": str(record_path.relative_to(ROOT)),
    }

    try:
        require(sys.flags.optimize == 0, "the R2 runner does not support optimized execution")
        for source in (path_a, path_b, manifest, certificate, specification, decision):
            require(source.is_file(), f"required input is missing: {source.relative_to(ROOT)}")
        require_clean_tracked_worktree()
        base["tracked_worktree_clean_before_replay"] = True
        base["repository_input_commit"] = git_head()

        rejected_mutations = negative_tests(path_a, path_b, manifest)

        command_a = checker_command(path_a, manifest)
        process_a, elapsed_a = run_process(command_a)
        require(process_a.returncode == 0, f"Path A exited {process_a.returncode}: {process_a.stderr.strip()}")
        require(not process_a.stderr.strip(), f"Path A emitted stderr: {process_a.stderr.strip()}")
        result_a = parse_checker_result(process_a.stdout, "R2-path-a-prefix", "Path A")

        command_b = checker_command(path_b, manifest)
        process_b, elapsed_b = run_process(command_b)
        require(process_b.returncode == 0, f"Path B exited {process_b.returncode}: {process_b.stderr.strip()}")
        require(not process_b.stderr.strip(), f"Path B emitted stderr: {process_b.stderr.strip()}")
        result_b = parse_checker_result(process_b.stdout, "R2-path-b-direct", "Path B")

        disagreements = [
            field for field in AGREEMENT_FIELDS if result_a[field] != result_b[field]
        ]
        require(not disagreements, f"independent paths disagree on: {disagreements}")

        finished_utc = utc_now()
        result: dict[str, object] = {
            **base,
            "finished_utc": finished_utc,
            "elapsed_seconds": time.monotonic() - start,
            "complete": True,
            "status": "PASS",
            "theorem_contract": {
                "path": str(SPEC_REL),
                "sha256": sha256(specification),
                "statement": "B2.2-FV",
                "parameter_region": "1 <= b <= c <= H, 5 <= H <= 24",
            },
            "decision": {"path": str(DECISION_REL), "sha256": sha256(decision)},
            "certificate_manifest": {
                "path": str(MANIFEST_REL),
                "sha256": sha256(manifest),
            },
            "certificate": {
                "path": str(CERTIFICATE_REL),
                "sha256": result_a["certificate_sha256"],
                "bytes": result_a["certificate_bytes"],
                "historical_archive_modified": False,
            },
            "sources": {
                "runner": {"path": str(RUNNER.relative_to(ROOT)), "sha256": sha256(RUNNER)},
                "path_a": {"path": str(PATH_A_REL), "sha256": sha256(path_a)},
                "path_b": {"path": str(PATH_B_REL), "sha256": sha256(path_b)},
            },
            "environment": {
                "platform": platform.platform(),
                "machine": platform.machine(),
                "python_executable": sys.executable,
                "python_version": sys.version,
                "dependencies": "Python standard library only",
                "integer_semantics": "arbitrary precision",
            },
            "commands": {
                "replay": [sys.executable, str(RUNNER.relative_to(ROOT))],
                "path_a": command_a,
                "path_b": command_b,
            },
            "processes": {
                "path_a": {
                    "exit_status": process_a.returncode,
                    "elapsed_seconds": elapsed_a,
                    "stderr": process_a.stderr,
                    "stdout_sha256": hashlib.sha256(process_a.stdout.encode()).hexdigest(),
                },
                "path_b": {
                    "exit_status": process_b.returncode,
                    "elapsed_seconds": elapsed_b,
                    "stderr": process_b.stderr,
                    "stdout_sha256": hashlib.sha256(process_b.stdout.encode()).hexdigest(),
                },
            },
            "negative_tests": rejected_mutations,
            "path_a_result": result_a,
            "path_b_result": result_b,
            "independent_agreement": {
                "status": "PASS",
                "fields_compared": list(AGREEMENT_FIELDS),
                "note": (
                    "Each path checked coverage and leaf inequalities before comparison; "
                    "agreement is a regression diagnostic, not an acceptance shortcut."
                ),
            },
            "unresolved": 0,
            "unsupported": 0,
            "claim_established_by_this_replay": (
                "Both exact checkers independently established complete closed-box coverage "
                "and recomputed every retained B2 leaf; with the B2.2 coverage theorem this "
                "establishes B2.2-FV for the immutable certificate."
            ),
            "does_not_establish": [
                "the analytic B2.1 compactness and continuous inequalities",
                "external peer review",
                "proof-assistant formalization",
                "the full four-generator theorem without the other branch obligations",
            ],
        }
        write_record(record_path, result)
        print(
            json.dumps(
                {
                    "status": "PASS",
                    "component": "R2",
                    "tree_nodes": result_a["tree_nodes"],
                    "dp_leaves": result_a["dp_leaves"],
                    "analytic_leaves": result_a["analytic_leaves"],
                    "largest_dp_bound_numerator": result_a["largest_dp_bound_numerator"],
                    "scale": result_a["scale"],
                    "independent_agreement": "PASS",
                },
                indent=2,
            )
        )
        return 0
    except Exception as error:
        failure = {
            **base,
            "finished_utc": utc_now(),
            "elapsed_seconds": time.monotonic() - start,
            "error_type": type(error).__name__,
            "error": str(error),
        }
        write_record(record_path, failure)
        print(f"R2 replay failed: {type(error).__name__}: {error}", file=sys.stderr)
        return 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", type=Path, default=ROOT / DEFAULT_RECORD_REL)
    arguments = parser.parse_args()
    record_path = arguments.record.resolve()
    try:
        record_path.relative_to(ROOT)
    except ValueError as error:
        raise SystemExit("--record must be inside the repository") from error
    return replay(record_path)


if __name__ == "__main__":
    raise SystemExit(main())
