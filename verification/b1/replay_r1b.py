#!/usr/bin/env python3
"""Fresh, fail-closed replay of the independent B1 membership exhaustion.

The theorem phase compiles and runs the immutable ordinary-membership source
without reading R1a output.  Only after that output independently passes the
B1.3-FV contract does the runner compare common diagnostics with R1a.
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
    "round5/small_multiplicity/independent_membership_check.cpp"
)
SPEC_REL = Path("paper/small-multiplicity-specification.md")
DECISION_REL = Path("research/b1-simplification-decision.md")
R1A_RECORD_REL = Path("verification/b1/r1a-replay.json")
DEFAULT_RECORD_REL = Path("verification/b1/r1b-replay.json")

PARTITION_KEYS = (
    "smallest_redundant",
    "middle_redundant",
    "largest_redundant",
    "nontrivial_gcd",
    "minimal_four_generator_semigroups",
)

COUNT_KEYS = (
    "raw_triples",
    *PARTITION_KEYS,
    "maximum_apery_within_bound",
    "negative_wilf_count",
    "zero_wilf_count",
)

INTEGER_KEYS = (
    "m",
    "generator_bound_inclusive",
    *COUNT_KEYS,
    "minimum_wilf_with_bounded_apery",
)

REQUIRED_KEYS = {
    *INTEGER_KEYS,
    "bounded_minimum_example",
    "bounded_checksum_fnv1a64",
    "elapsed_seconds",
}

AGREEMENT_FIELDS = (
    "m",
    "generator_bound_inclusive",
    "raw_triples",
    *PARTITION_KEYS,
    "maximum_apery_within_bound",
    "minimum_wilf_with_bounded_apery",
    "bounded_minimum_example",
    "bounded_checksum_fnv1a64",
)


class ReplayFailure(RuntimeError):
    """Raised whenever replay or downstream agreement is not established."""


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


def validate_example(value: object, m: int, bound: int) -> None:
    require(isinstance(value, list), f"bounded minimizer is not a list for m={m}")
    require(len(value) == 4, f"bounded minimizer does not have four entries for m={m}")
    require(
        all(isinstance(item, int) and not isinstance(item, bool) for item in value),
        f"bounded minimizer contains a noninteger for m={m}",
    )
    require(value[0] == m, f"bounded minimizer has wrong multiplicity for m={m}")
    require(m < value[1] < value[2] < value[3] <= bound, f"invalid minimizer for m={m}")


def validate_independent_records(records: list[dict[str, object]]) -> dict[str, int]:
    """Validate R1b before any R1a result is opened."""
    totals = {key: 0 for key in COUNT_KEYS}

    for expected_m, record in zip(range(20, 30), records, strict=True):
        require(set(record) == REQUIRED_KEYS, f"unexpected output schema for m={expected_m}")
        for key in INTEGER_KEYS:
            require(
                isinstance(record[key], int) and not isinstance(record[key], bool),
                f"{key} is not an integer for m={expected_m}",
            )
        require(record["m"] == expected_m, f"wrong or unordered multiplicity {record['m']!r}")

        bound = expected_m * (expected_m - 2)
        raw = math.comb(bound - expected_m, 3)
        require(record["generator_bound_inclusive"] == bound, f"wrong bound for m={expected_m}")
        require(record["raw_triples"] == raw, f"wrong raw count for m={expected_m}")
        require(
            all(record[key] >= 0 for key in COUNT_KEYS),
            f"negative count in output for m={expected_m}",
        )
        require(
            sum(record[key] for key in PARTITION_KEYS) == raw,
            f"classification does not partition the raw domain for m={expected_m}",
        )

        valid = record["minimal_four_generator_semigroups"]
        bounded = record["maximum_apery_within_bound"]
        negative = record["negative_wilf_count"]
        zero = record["zero_wilf_count"]
        require(0 < bounded <= valid, f"invalid bounded count for m={expected_m}")
        require(0 <= negative <= bounded, f"invalid negative count for m={expected_m}")
        require(0 <= zero <= bounded, f"invalid zero count for m={expected_m}")
        require(negative == 0, f"negative Wilf number found for m={expected_m}")
        require(
            record["minimum_wilf_with_bounded_apery"] >= 0,
            f"negative bounded-Apéry minimum for m={expected_m}",
        )
        validate_example(record["bounded_minimum_example"], expected_m, bound)

        checksum = record["bounded_checksum_fnv1a64"]
        require(
            isinstance(checksum, str)
            and checksum.isdecimal()
            and int(checksum) < 2**64,
            f"malformed diagnostic checksum for m={expected_m}",
        )
        elapsed = record["elapsed_seconds"]
        require(
            isinstance(elapsed, (int, float))
            and not isinstance(elapsed, bool)
            and math.isfinite(elapsed)
            and elapsed >= 0,
            f"invalid elapsed time for m={expected_m}",
        )

        for key in totals:
            totals[key] += record[key]

    require(totals["raw_triples"] == 301_098_092, "wrong total raw traversal count")
    require(totals["negative_wilf_count"] == 0, "negative Wilf number found")
    return totals


def packed_window(blocks: list[int], start: int, width: int) -> int:
    """Python transcription of the source's packed-window helper."""
    mask = (1 << width) - 1
    if start <= -width:
        return 0
    if start < 0:
        return (blocks[0] << (-start)) & mask
    block, offset = divmod(start, 64)
    result = blocks[block] >> offset
    if offset:
        result |= blocks[block + 1] << (64 - offset)
    return result & mask


def packed_window_diagnostic() -> dict[str, int]:
    """Compare every in-scope one-bit window with its closed-form location."""
    basis_cases = 0
    for m in range(20, 30):
        bound = m * (m - 2)
        block_count = (bound + 1) // 64 + 2
        for position in range(bound + 1):
            blocks = [0] * block_count
            blocks[position // 64] = 1 << (position % 64)
            for start in range(-m, bound - m + 2):
                expected = 0
                if start <= position < start + m:
                    expected = 1 << (position - start)
                require(
                    packed_window(blocks, start, m) == expected,
                    f"packed-window mismatch for m={m}, position={position}, start={start}",
                )
                basis_cases += 1
    return {"one_bit_basis_cases": basis_cases}


def compare_with_r1a(
    r1b_records: list[dict[str, object]], specification_hash: str
) -> dict[str, object]:
    """Compare only after R1b has independently passed its theorem contract."""
    path = ROOT / R1A_RECORD_REL
    require(path.is_file(), f"missing R1a replay record: {R1A_RECORD_REL}")
    try:
        r1a = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ReplayFailure(f"cannot read R1a replay record: {error}") from error
    require(isinstance(r1a, dict), "R1a replay record is not an object")
    require(r1a.get("status") == "PASS" and r1a.get("complete") is True, "R1a did not pass")
    contract = r1a.get("theorem_contract")
    require(isinstance(contract, dict), "R1a theorem contract is missing")
    require(contract.get("sha256") == specification_hash, "R1a contract hash is stale")
    result = r1a.get("result")
    require(isinstance(result, dict), "R1a result is missing")
    totals = result.get("totals")
    require(isinstance(totals, dict), "R1a totals are missing")
    require(result.get("unresolved") == 0, "R1a has unresolved cases")
    require(result.get("unsupported") == 0, "R1a has unsupported cases")
    require(totals.get("negative_wilf_count") == 0, "R1a found a negative Wilf number")
    r1a_records = result.get("per_multiplicity")
    require(isinstance(r1a_records, list) and len(r1a_records) == 10, "invalid R1a records")

    for expected_m, (left, right) in enumerate(
        zip(r1a_records, r1b_records, strict=True), start=20
    ):
        require(isinstance(left, dict), f"invalid R1a record for m={expected_m}")
        for field in AGREEMENT_FIELDS:
            require(
                left.get(field) == right.get(field),
                f"R1a/R1b disagreement for m={expected_m}, field={field}",
            )

    return {
        "status": "PASS",
        "performed_after_independent_r1b_validation": True,
        "r1a_record": {
            "path": str(R1A_RECORD_REL),
            "sha256": sha256(path),
            "repository_input_commit": r1a.get("repository_input_commit"),
        },
        "multiplicities_compared": 10,
        "fields_compared": list(AGREEMENT_FIELDS),
        "note": (
            "negative and zero counts were not compared because R1a records them on all "
            "valid boxed tuples whereas R1b records them only when M <= B_m; each checker "
            "validated its own negative count independently"
        ),
    }


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
        "component": "R1b",
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
        window_diagnostic = packed_window_diagnostic()

        with tempfile.TemporaryDirectory(prefix="wilf_r1b_") as temporary:
            binary = Path(temporary) / "independent_membership_check"
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
                f"membership exhaustion exited with {run_result.returncode}: "
                f"{run_result.stderr.strip()}",
            )
            require(
                not run_result.stderr.strip(),
                f"unexpected stderr: {run_result.stderr.strip()}",
            )
            records = parse_records(run_result.stdout)
            totals = validate_independent_records(records)

        base["independent_result"] = {
            "status": "PASS",
            "validated_before_r1a_record_was_opened": True,
            "unresolved": 0,
            "unsupported": 0,
            "packed_window_diagnostic": window_diagnostic,
            "totals": totals,
            "per_multiplicity": records,
        }
        specification_hash = sha256(specification)
        agreement = compare_with_r1a(records, specification_hash)

        result: dict[str, object] = {
            **base,
            "finished_utc": utc_now(),
            "elapsed_seconds": time.monotonic() - started_monotonic,
            "complete": True,
            "status": "PASS",
            "source": {
                "path": str(SOURCE_REL),
                "sha256": sha256(source),
                "historical_archive_modified": False,
            },
            "theorem_contract": {
                "path": str(SPEC_REL),
                "sha256": specification_hash,
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
                    "<temporary-directory>/independent_membership_check",
                ],
                "run": ["<temporary-directory>/independent_membership_check", "20", "29"],
            },
            "process": {
                "compile_exit_status": compile_result.returncode,
                "run_exit_status": run_result.returncode,
                "compile_stderr": compile_result.stderr,
                "run_stderr": run_result.stderr,
                "stdout_sha256": hashlib.sha256(run_result.stdout.encode()).hexdigest(),
            },
            "agreement_with_r1a": agreement,
            "claim_established_by_independent_r1b_replay": (
                "The ordinary-membership implementation independently traversed every "
                "sorted generator tuple in the B1 box for 20 <= m <= 29 and found no "
                "negative Wilf number in the required M <= B_m domain."
            ),
            "does_not_establish": [
                "external peer review",
                "proof-assistant formalization",
                "a theorem about valid boxed tuples with M > B_m",
                "strict positivity outside the finite theorem contract",
            ],
        }
        write_record(record_path, result)
        print(
            json.dumps(
                {
                    "status": "PASS",
                    "component": "R1b",
                    "independent_totals": totals,
                    "agreement_with_r1a": "PASS",
                },
                indent=2,
            )
        )
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
        print(f"R1b replay failed: {error}", file=sys.stderr)
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
