#!/usr/bin/env python3
"""Replay a literal packet copy outside the Git checkout, then preserve its evidence."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[1]
PACKET=ROOT/"prelim"

def require(condition,reason):
    if not condition: raise RuntimeError(reason)

def main():
    require(len(sys.argv)==1 and not sys.flags.optimize,"complete unoptimized mode only")
    expected=(PACKET/"manifest.json").read_bytes()
    with tempfile.TemporaryDirectory(prefix="wilf-standalone-") as directory:
        copied=Path(directory)/"packet"
        shutil.copytree(PACKET,copied,ignore=shutil.ignore_patterns("replay.json","__pycache__"))
        require(not (copied/".git").exists(),"copy must not be a checkout")
        result=subprocess.run([sys.executable,"-I","-B",str(copied/"verify.py")],cwd=copied)
        record=json.loads((copied/"replay.json").read_bytes())
        require((PACKET/"manifest.json").read_bytes()==expected,"packet manifest changed")
        for descriptor in record["inputs"]:
            path=PACKET/descriptor["path"]
            require(path.stat().st_size==descriptor["bytes"]
                    and hashlib.sha256(path.read_bytes()).hexdigest()==descriptor["sha256"],"packet input changed")
        record["standalone_copy_checked"]=True
        record["standalone_copy_contained_git"]=False
        (PACKET/"replay.json").write_text(json.dumps(record,indent=2,sort_keys=True)+"\n")
        require(result.returncode==0 and record["status"]=="PASS" and record["complete"] is True,
                "standalone replay failed")
    return 0

if __name__=="__main__": raise SystemExit(main())
