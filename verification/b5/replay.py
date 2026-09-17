#!/usr/bin/env python3
"""Fresh B5 profile verification: two independent C++17 implementations."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import shlex
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / "verification/b5"
INPUTS = (
    "verification/b5/replay.py",
    "verification/b5/check_profiles_bits.cpp",
    "verification/b5/check_profiles_columns.cpp",
    "paper/residual-degree-six.md",
    "paper/coordinate-lines.md",
    "paper/short-corner-local-certificates.md",
    "paper/foundations.md",
    "research/b5-simplification-decision.md",
)
CORNERS = [(1,1,3),(1,2,2),(1,1,4),(1,2,3),(2,2,2),
           (1,1,5),(1,2,4),(1,3,3),(2,2,3)]

def require(condition, message):
    if not condition:
        raise RuntimeError(message)

def now():
    return datetime.now(timezone.utc).isoformat()

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def git(*args):
    p = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    require(p.returncode == 0, p.stderr)
    return p.stdout.strip()

def call(command):
    start, clock = now(), time.monotonic()
    p = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    return p, dict(command=command, started_utc=start, finished_utc=now(),
                   elapsed_seconds=time.monotonic()-clock, exit_status=p.returncode,
                   stderr=p.stderr, stdout_sha256=hashlib.sha256(p.stdout.encode()).hexdigest())

def validate(output, component):
    lines = output.splitlines()
    require(len(lines) == 10, "incomplete result stream")
    records = [json.loads(line) for line in lines]
    summary = records.pop()
    require(summary == dict(component=component, status="PASS", complete=True,
                            profiles=summary.get("profiles"), eligible=summary.get("eligible")),
            "bad completion summary")
    require(type(summary["profiles"]) is int and summary["profiles"] > 0,
            "empty profile generator")
    for pid, record in enumerate(records):
        require(set(record) == {
            "pid","corner","compatible","degree_filtered","m30","eligible",
            "local_pass","axis_pass","axis_fallback","minimum_margin_numerator",
            "minimum_margin_denominator","checksum","histogram"}, "record schema")
        require(record["pid"] == pid and record["corner"] == list(CORNERS[pid]),
                "missing or reordered corner")
        for key in set(record)-{"corner","histogram"}:
            require(type(record[key]) is int and record[key] >= 0, "bad integer field")
        require(record["compatible"] >= record["degree_filtered"] >= record["m30"]
                >= record["eligible"], "filter counts")
        n = record["eligible"]
        require(record["local_pass"]+record["axis_fallback"] == n
                and record["axis_fallback"] <= record["axis_pass"] <= n,
                "predicate coverage")
        require(record["minimum_margin_denominator"] > 0, "margin denominator")
        if not n:
            require(record["minimum_margin_numerator"] == (1<<63)-1
                    and record["minimum_margin_denominator"] == 1, "empty margin sentinel")
            record["minimum_margin_numerator"] = None
            record["minimum_margin_denominator"] = None
        hist = record["histogram"]
        require(len(hist) == 85 and all(type(v) is int and v >= 0 for v in hist)
                and sum(hist) == n and not any(hist[:30]), "cardinality histogram")
    require(type(summary["eligible"]) is int
            and summary["eligible"] == sum(r["eligible"] for r in records), "total")
    return dict(component=component, summary=summary, corners=records)

def replay(output):
    clock = time.monotonic()
    record = dict(schema_version=1, component="R5", status="FAIL", complete=False,
                  exit_status=1, started_utc=now(), fresh=True, cache_free=True,
                  archive_inputs=False)
    try:
        require(not sys.flags.optimize, "optimized runner is unsupported")
        require(not git("status","--porcelain","--untracked-files=no"), "tracked inputs dirty")
        record["repository_input_commit"] = git("rev-parse","HEAD")
        for path in INPUTS:
            git("ls-files","--error-unmatch",path)
        hashes = {p:digest(ROOT/p) for p in INPUTS}
        record["sources"] = [dict(path=p,sha256=h) for p,h in hashes.items()]
        compiler = shlex.split(os.environ.get("CXX","c++"))
        require(bool(compiler), "missing compiler")
        version, _ = call([*compiler,"--version"])
        require(version.returncode == 0, "compiler version check")
        record["environment"] = dict(python=sys.version, platform=platform.platform(),
                                     compiler=version.stdout, dependencies="C++17 and Python standard libraries")
        record["replay_command"] = [sys.executable,*sys.orig_argv[1:]]
        results, processes, negatives = [], [], []
        with tempfile.TemporaryDirectory(prefix="wilf-r5-") as tmp:
            for name, component in (("check_profiles_bits.cpp","B5-bitsets"),
                                    ("check_profiles_columns.cpp","B5-columns")):
                binary = str(Path(tmp)/Path(name).stem)
                p, info = call([*compiler,"-std=c++17","-O3","-Wall","-Wextra","-pedantic",
                                str(HERE/name),"-o",binary])
                processes.append(info)
                require(p.returncode == 0 and not p.stderr, f"{name}: compile failure or diagnostic")
                for label, args in (("partial_mode",["--sample","1"]),("unexpected_argument",["1"])):
                    p, info = call([binary,*args])
                    require(p.returncode != 0 and "failed:" in p.stderr, "partial mode accepted")
                    negatives.append(dict(checker=name,mutation=label,rejected=True,**info))
                p, info = call([binary])
                processes.append(info)
                require(p.returncode == 0 and not p.stderr, f"{name}: complete execution failed")
                results.append(validate(p.stdout,component))
        left, right = results
        require(left["corners"] == right["corners"]
                and left["summary"]["profiles"] == right["summary"]["profiles"]
                and left["summary"]["eligible"] == right["summary"]["eligible"],
                "independent enumeration or predicate disagreement")
        require(all(digest(ROOT/p) == h for p,h in hashes.items()), "input changed during replay")
        record.update(status="PASS",complete=True,exit_status=0,results=results,
                      processes=processes,negative_tests=negatives,independent_agreement=True,
                      unresolved=0,unsupported=0,establishes="B5-FV under its analytic coverage proof",
                      does_not_establish=["external review","global theorem"])
    except Exception as error:
        record["error"] = f"{type(error).__name__}: {error}"
    record.update(finished_utc=now(),elapsed_seconds=time.monotonic()-clock)
    output.write_text(json.dumps(record,indent=2,sort_keys=True)+"\n")
    print(json.dumps(dict(status=record["status"],component="R5",
                         elapsed_seconds=record["elapsed_seconds"],error=record.get("error"))))
    return record["exit_status"]

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record",type=Path,default=HERE/"r5-replay.json")
    output=parser.parse_args().record.resolve()
    if output.parent != HERE or not re.fullmatch(r"r5-replay(?:-[\w-]+)?\.json",output.name):
        parser.error("record must be r5-replay[-suffix].json in verification/b5")
    return replay(output)

if __name__ == "__main__":
    raise SystemExit(main())
