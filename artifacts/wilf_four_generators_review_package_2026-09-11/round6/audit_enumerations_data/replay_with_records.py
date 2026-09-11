#!/usr/bin/env python3
"""Run an unchanged canonical verifier, retaining its fresh subprocess output.

The only wrapped behavior is recording completed enumeration stdout.  The
canonical verifier still compiles each C++ source, checks return codes, and
performs all comparisons against the historical records and the other run.
"""
from pathlib import Path
import runpy
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
mode = sys.argv[1]
if mode == "small":
    verifier = ROOT / "round5/small_multiplicity/verify_exhaustion.py"
    stems = {"exhaust_small_multiplicity", "independent_membership_check"}
elif mode == "p211":
    verifier = ROOT / "round5/short_corner_small_m/verify_p211_exhaustion.py"
    stems = {"exhaust_p211_relations", "independent_p211_membership"}
else:
    raise ValueError(mode)

original_run = subprocess.run

def record_run(args, *pos, **kwargs):
    result = original_run(args, *pos, **kwargs)
    stem = Path(args[0]).name
    if stem in stems:
        assert kwargs.get("capture_output") and kwargs.get("text")
        (HERE / f"{stem}_2026-09-09.jsonl").write_text(result.stdout)
    return result

subprocess.run = record_run
sys.argv = [str(verifier), "--rerun"]
runpy.run_path(str(verifier), run_name="__main__")
