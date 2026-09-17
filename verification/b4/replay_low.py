#!/usr/bin/env python3
"""Fresh complete R4b replay; no historical inputs or saved acceptance data."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import re
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / "verification/b4"
INPUTS = (
    "verification/b4/replay_low.py",
    "verification/b4/check_low_offsets.py",
    "verification/b4/check_low_successors.py",
    "paper/short-corner-profile-specification.md",
    "paper/short-corner-local-certificates.md",
    "paper/coordinate-lines.md",
    "paper/short-corner-centroid-certificates.md",
    "paper/short-corner-height-split.md",
    "paper/foundations.md",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def hash_file(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat()


def call(command):
    start, clock = now(), time.monotonic()
    p = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    return p, dict(command=command, started_utc=start, finished_utc=now(),
                   elapsed_seconds=time.monotonic() - clock,
                   exit_status=p.returncode, stderr=p.stderr,
                   stdout_sha256=hashlib.sha256(p.stdout.encode()).hexdigest())


def git(*args):
    p = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    require(p.returncode == 0, p.stderr)
    return p.stdout.strip()


def replay(output):
    record = dict(schema_version=1, component="R4b", status="FAIL",
                  complete=False, exit_status=1, started_utc=now(),
                  fresh=True, cache_free=True, archive_inputs=False)
    clock = time.monotonic()
    try:
        require(not sys.flags.optimize, "optimized runner is unsupported")
        require(not git("status", "--porcelain", "--untracked-files=no"),
                "tracked worktree must be clean")
        record["repository_input_commit"] = git("rev-parse", "HEAD")
        for path in INPUTS:
            git("ls-files", "--error-unmatch", path)
        sources = {p: hash_file(ROOT / p) for p in INPUTS}
        record["sources"] = [dict(path=p, sha256=h) for p, h in sources.items()]
        record["environment"] = dict(python=sys.version, platform=platform.platform(),
                                     dependencies="Python standard library only")
        record["replay_command"] = [sys.executable, *sys.orig_argv[1:]]
        records, tests, processes = [], [], []
        for name in ("check_low_offsets.py", "check_low_successors.py"):
            script = HERE / name
            for label, options in (("optimized", ["-O"]), ("partial_mode", [])):
                command = [sys.executable, *options, "-I", "-B", str(script)]
                if label == "partial_mode":
                    command += ["--sample", "1"]
                p, info = call(command)
                require(p.returncode != 0, f"{name} accepted {label}")
                tests.append(dict(checker=name, mutation=label, rejected=True, **info))
            # Direct negative witness tests exercise membership, mass, residual
            # and boolean handling without changing the frozen checker sources.
            fixture = (
                "import importlib.util,itertools; "
                f"s=importlib.util.spec_from_file_location('check',{str(script)!r}); "
                "m=importlib.util.module_from_spec(s);s.loader.exec_module(m); "
                "f=(4,3,3,2,0,0);g=(6,3,3,2,0,0);h=(6,4,2,2,0,0); "
                "t={p for p in itertools.product(range(6),repeat=3) "
                "if p[1]<f[p[0]] and p[2]<g[p[0]] and p[2]<h[p[1]] "
                "and not(p[0]>=2 and p[1]>=1 and p[2]>=1)}; "
            )
            for label, witness in (
                ("bad_membership", [((9, 9, 9), 90)]),
                ("bad_mass", [((0, 0, 5), 38), ((2, 2, 0), 48), ((3, 1, 0), 5)]),
                ("bad_residual", [((0, 0, 0), 90)]),
                ("boolean_multiplier", [((0, 0, 0), True)]),
            ):
                command = [sys.executable, "-I", "-B", "-c",
                           fixture + f"m.check_integer_witness(t,{witness!r})"]
                p, info = call(command)
                require(p.returncode != 0 and "Error" in p.stderr,
                        f"{name} accepted or failed to exercise {label}")
                tests.append(dict(checker=name, mutation=label, rejected=True, **info))
            p, info = call([sys.executable, "-I", "-B", str(script)])
            processes.append(info)
            require(p.returncode == 0 and not p.stderr and len(p.stdout.splitlines()) == 1,
                    f"{name} failed or produced incomplete output")
            result = json.loads(p.stdout)
            require(result["status"] == "PASS" and result["complete"] is True
                    and result["contract"] == "B4-low-local-FV"
                    and result["unresolved"] == result["unsupported"] == 0
                    and result["archive_inputs"] is False, f"{name} incomplete result")
            records.append(result)
        left, right = [dict(r) for r in records]
        left.pop("component"); right.pop("component")
        require(left == right, "independent enumeration or predicate disagreement")
        require(all(hash_file(ROOT / p) == h for p, h in sources.items()),
                "proof input changed during replay")
        record.update(status="PASS", complete=True, exit_status=0,
                      processes=processes, negative_tests=tests, results=records,
                      independent_agreement=True, unresolved=0, unsupported=0,
                      establishes="B4-low-local-FV under its mathematical coverage proof",
                      does_not_establish=["external review", "global theorem"])
    except Exception as error:
        record["error"] = f"{type(error).__name__}: {error}"
    record["finished_utc"] = now()
    record["elapsed_seconds"] = time.monotonic() - clock
    output.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
    print(json.dumps(dict(status=record["status"], component="R4b",
                          elapsed_seconds=record["elapsed_seconds"])))
    return record["exit_status"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", type=Path, default=HERE / "r4b-replay.json")
    output = parser.parse_args().record.resolve()
    if output.parent != HERE or not re.fullmatch(r"r4b-replay(?:-[\w-]+)?\.json", output.name):
        parser.error("record must be an r4b-replay[-suffix].json file in verification/b4")
    return replay(output)


if __name__ == "__main__":
    raise SystemExit(main())
