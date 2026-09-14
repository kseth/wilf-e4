#!/usr/bin/env python3
"""Fresh, fail-closed replay of the B1 residue-distance exhaustion.

This runner compiles the immutable historical C++ source in a temporary
directory, executes the complete multiplicity range 20 through 29, validates
the output without consulting stored success records, and writes a
machine-readable replay record.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import platform
import subprocess
import sys
import tempfile
import time


ROOT = Path(__file__).resolve().parents[2]
RUNNER = Path(__file__).resolve()
SOURCE_REL = Path(
    "artifacts/wilf_four_generators_review_package_2026-09-11/"
    "round5/small_multiplicity/exhaust_small_multiplicity.cpp"
)
SPEC_REL = Path("paper/small-multiplicity-specification.md")
DECISION_REL = Path("research/b1-simplification-decision.md")
DEFAULT_RECORD_REL = Path("verification/b1/r1a-replay.json")

PARTITION_KEYS = (
    "smallest_redundant",
    "middle_redundant",
    "largest_redundant",
    "nontrivial_gcd",
    "minimal_four_generator_semigroups",
)

INTEGER_KEYS = (
    "m",
    "generator_bound_inclusive",
    "raw_triples",
    *PARTITION_KEYS,
    "maximum_apery_within_bound",
    "negative_wilf_count",
    "zero_wilf_count",
    "minimum_wilf",
    "minimum_wilf_with_bounded_apery",
)

REQUIRED_KEYS = {
    *INTEGER_KEYS,
    "minimum_wilf_example",
    "bounded_minimum_example",
    "bounded_checksum_fnv1a64",
    "elapsed_seconds",
}


class ReplayFailure(RuntimeError):
    """Raised whenever the replay cannot establish its exact contract."""


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ReplayFailure(message)


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
    require(len(value) == 40, f"unexpected git commit identifier: {value!r}")
    return value


def require_clean_tracked_worktree() -> None:
    status = checked_output(["git", "status", "--porcelain", "--untracked-files=no"])
    require(not status, f"tracked worktree is not clean before replay: {status!r}")


def compiler_version(compiler: str) -> str:
    value = checked_output([compiler, "--version"])
    require(bool(value), "compiler returned an empty version string")
    return value


def parse_records(stdout: str) -> list[dict[str, object]]:
    lines = [line for line in stdout.splitlines() if line.strip()]
    require(len(lines) == 10, f"expected 10 JSON records, found {len(lines)}")
    records: list[dict[str, object]] = []
    for number, line in enumerate(lines, start=1):
        try:
            value = json.loads(line)
        except json.JSONDecodeError as error:
            raise ReplayFailure(f"malformed JSON on output line {number}: {error}") from error
        require(isinstance(value, dict), f"output line {number} is not an object")
        records.append(value)
    return records


def validate_example(value: object, m: int, bound: int, label: str) -> None:
    require(isinstance(value, list), f"{label} is not a list for m={m}")
    require(len(value) == 4, f"{label} does not contain four entries for m={m}")
    require(
        all(isinstance(item, int) and not isinstance(item, bool) for item in value),
        f"{label} contains a noninteger entry for m={m}",
    )
    require(value[0] == m, f"{label} has the wrong multiplicity for m={m}")
    require(m < value[1] < value[2] < value[3] <= bound, f"invalid {label} for m={m}")


def validate_records(records: list[dict[str, object]]) -> dict[str, object]:
    totals = {
        "raw_triples": 0,
        "smallest_redundant": 0,
        "middle_redundant": 0,
        "largest_redundant": 0,
        "nontrivial_gcd": 0,
        "minimal_four_generator_semigroups": 0,
        "maximum_apery_within_bound": 0,
        "negative_wilf_count": 0,
        "zero_wilf_count": 0,
    }

    for expected_m, record in zip(range(20, 30), records, strict=True):
        require(set(record) == REQUIRED_KEYS, f"unexpected output schema for m={expected_m}")
        for key in INTEGER_KEYS:
            require(
                isinstance(record[key], int) and not isinstance(record[key], bool),
                f"{key} is not an integer for m={expected_m}",
            )
        require(record["m"] == expected_m, f"wrong or unordered multiplicity {record['m']!r}")

        bound = expected_m * (expected_m - 2)
        number_of_choices = bound - expected_m
        raw = math.comb(number_of_choices, 3)
        require(record["generator_bound_inclusive"] == bound, f"wrong bound for m={expected_m}")
        require(record["raw_triples"] == raw, f"wrong raw count for m={expected_m}")
        require(
            sum(record[key] for key in PARTITION_KEYS) == raw,
            f"classification does not partition the raw domain for m={expected_m}",
        )

        valid = record["minimal_four_generator_semigroups"]
        bounded = record["maximum_apery_within_bound"]
        negative = record["negative_wilf_count"]
        zero = record["zero_wilf_count"]
        require(0 <= bounded <= valid, f"invalid bounded count for m={expected_m}")
        require(0 <= negative <= valid, f"invalid negative count for m={expected_m}")
        require(0 <= zero <= valid, f"invalid zero count for m={expected_m}")
        require(negative == 0, f"negative Wilf number found for m={expected_m}")
        require(record["minimum_wilf"] >= 0, f"negative recorded minimum for m={expected_m}")
        require(
            record["minimum_wilf_with_bounded_apery"] >= 0,
            f"negative bounded-Apéry minimum for m={expected_m}",
        )

        validate_example(record["minimum_wilf_example"], expected_m, bound, "minimum example")
        validate_example(
            record["bounded_minimum_example"], expected_m, bound, "bounded minimum example"
        )
        checksum = record["bounded_checksum_fnv1a64"]
        require(
            isinstance(checksum, str) and checksum.isdecimal(),
            f"malformed diagnostic checksum for m={expected_m}",
        )
        elapsed = record["elapsed_seconds"]
        require(
            isinstance(elapsed, (int, float)) and not isinstance(elapsed, bool) and elapsed >= 0,
            f"invalid elapsed time for m={expected_m}",
        )

        for key in totals:
            totals[key] += record[key]

    require(totals["raw_triples"] == 301_098_092, "wrong total raw traversal count")
    require(totals["negative_wilf_count"] == 0, "negative Wilf number found")
    return totals


def cycle_schedule_diagnostic() -> dict[str, int]:
    """Check the two-pass schedule on every one-source basis case in scope."""
    infinity = 1_000_000_000
    basis_cases = 0
    relaxations = 0
    for m in range(20, 30):
        bound = m * (m - 2)
        for weight in range(m + 1, bound + 1):
            step = weight % m
            divisor = math.gcd(m, step)
            length = m // divisor
            for source in range(m):
                before = [infinity] * m
                before[source] = source
                after = before.copy()
                for start in range(divisor):
                    residue = start
                    for _ in range(2 * length):
                        following = residue + step
                        if following >= m:
                            following -= m
                        after[following] = min(after[following], after[residue] + weight)
                        residue = following
                        relaxations += 1

                expected = [infinity] * m
                residue = source
                for multiple in range(length):
                    expected[residue] = source + multiple * weight
                    residue = (residue + step) % m
                require(
                    after == expected,
                    f"cycle schedule mismatch for m={m}, weight={weight}, source={source}",
                )
                basis_cases += 1
    return {"one_source_basis_cases": basis_cases, "edge_relaxations": relaxations}


def write_record(path: Path, record: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def replay(compiler: str, record_path: Path) -> int:
    started_utc = utc_now()
    started_monotonic = time.monotonic()
    source = ROOT / SOURCE_REL
    specification = ROOT / SPEC_REL
    decision = ROOT / DECISION_REL
    base: dict[str, object] = {
        "schema_version": 1,
        "component": "R1a",
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
        require(source.is_file(), f"missing source: {SOURCE_REL}")
        require(specification.is_file(), f"missing specification: {SPEC_REL}")
        require(decision.is_file(), f"missing D1 decision: {DECISION_REL}")
        require_clean_tracked_worktree()
        base["tracked_worktree_clean_before_replay"] = True
        base["repository_input_commit"] = git_head()
        version = compiler_version(compiler)
        schedule_diagnostic = cycle_schedule_diagnostic()

        with tempfile.TemporaryDirectory(prefix="wilf_r1a_") as temporary:
            binary = Path(temporary) / "exhaust_small_multiplicity"
            compile_command = [
                compiler,
                "-O3",
                "-std=c++17",
                "-Wall",
                "-Wextra",
                "-Wpedantic",
                "-Werror",
                str(source),
                "-o",
                str(binary),
            ]
            compile_result = subprocess.run(
                compile_command,
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            require(
                compile_result.returncode == 0,
                "compilation failed: " + compile_result.stderr.strip(),
            )

            run_command = [str(binary), "20", "29"]
            run_result = subprocess.run(
                run_command,
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            require(
                run_result.returncode == 0,
                f"exhaustion exited with {run_result.returncode}: {run_result.stderr.strip()}",
            )
            require(not run_result.stderr.strip(), f"unexpected stderr: {run_result.stderr.strip()}")
            records = parse_records(run_result.stdout)
            totals = validate_records(records)

        finished_utc = utc_now()
        elapsed = time.monotonic() - started_monotonic
        result: dict[str, object] = {
            **base,
            "finished_utc": finished_utc,
            "elapsed_seconds": elapsed,
            "complete": True,
            "status": "PASS",
            "source": {
                "path": str(SOURCE_REL),
                "sha256": sha256(source),
                "historical_archive_modified": False,
            },
            "theorem_contract": {
                "path": str(SPEC_REL),
                "sha256": sha256(specification),
                "statement": "B1.3-FV",
                "multiplicity_interval_inclusive": [20, 29],
            },
            "decision": {"path": str(DECISION_REL), "sha256": sha256(decision)},
            "runner": {
                "path": str(RUNNER.relative_to(ROOT)),
                "sha256": sha256(RUNNER),
                "python": sys.version,
            },
            "environment": {
                "platform": platform.platform(),
                "machine": platform.machine(),
                "compiler_path": compiler,
                "compiler_version": version,
            },
            "commands": {
                "replay": ["python3", str(RUNNER.relative_to(ROOT))],
                "compile": [
                    compiler,
                    "-O3",
                    "-std=c++17",
                    "-Wall",
                    "-Wextra",
                    "-Wpedantic",
                    "-Werror",
                    str(SOURCE_REL),
                    "-o",
                    "<temporary-directory>/exhaust_small_multiplicity",
                ],
                "run": ["<temporary-directory>/exhaust_small_multiplicity", "20", "29"],
            },
            "process": {
                "compile_exit_status": compile_result.returncode,
                "run_exit_status": run_result.returncode,
                "compile_stderr": compile_result.stderr,
                "run_stderr": run_result.stderr,
                "stdout_sha256": hashlib.sha256(run_result.stdout.encode()).hexdigest(),
            },
            "result": {
                "unresolved": 0,
                "unsupported": 0,
                "cycle_schedule_diagnostic": schedule_diagnostic,
                "totals": totals,
                "per_multiplicity": records,
            },
            "claim_established_by_this_replay": (
                "The audited residue-distance implementation freshly traversed every sorted "
                "generator tuple in the B1 box for 20 <= m <= 29 and found no negative "
                "Wilf number; in particular it establishes B1.3-FV for this implementation."
            ),
            "does_not_establish": [
                "independence from the residue-distance derivation (reserved for R1b)",
                "external peer review",
                "proof-assistant formalization",
                "strict positivity outside the necessary bounded-Apéry domain",
            ],
        }
        write_record(record_path, result)
        print(json.dumps({"status": "PASS", "component": "R1a", "totals": totals}, indent=2))
        return 0
    except Exception as error:
        failure = {
            **base,
            "finished_utc": utc_now(),
            "elapsed_seconds": time.monotonic() - started_monotonic,
            "error_type": type(error).__name__,
            "error": str(error),
        }
        write_record(record_path, failure)
        print(f"R1a replay failed: {error}", file=sys.stderr)
        return 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--compiler", default="/usr/bin/g++")
    parser.add_argument("--record", type=Path, default=ROOT / DEFAULT_RECORD_REL)
    arguments = parser.parse_args()
    record_path = arguments.record.resolve()
    try:
        record_path.relative_to(ROOT)
    except ValueError as error:
        raise SystemExit("--record must be inside the repository") from error
    return replay(arguments.compiler, record_path)


if __name__ == "__main__":
    raise SystemExit(main())
