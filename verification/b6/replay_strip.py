#!/usr/bin/env python3
"""Fresh, complete, independent R6a finite-strip verification."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import time
ROOT=Path(__file__).resolve().parents[2]
HERE=ROOT/"verification/b6"
INPUTS=("verification/b6/replay_strip.py","verification/b6/check_strip_prefix.cpp",
        "verification/b6/check_strip_points.cpp","paper/residual-high-height.md",
        "paper/central-box-horns.md","paper/phase-and-thickening.md",
        "research/b6-simplification-decision.md")
def require(b,why):
    if not b: raise RuntimeError(why)
def now(): return datetime.now(timezone.utc).isoformat()
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def git(*args):
    p=subprocess.run(["git",*args],cwd=ROOT,capture_output=True,text=True)
    require(p.returncode==0,p.stderr)
    return p.stdout.strip()
def call(command):
    start,clock=now(),time.monotonic()
    p=subprocess.run(command,cwd=ROOT,capture_output=True,text=True)
    return p,dict(command=command,started_utc=start,finished_utc=now(),
                  elapsed_seconds=time.monotonic()-clock,exit_status=p.returncode,
                  stderr=p.stderr,stdout_sha256=hashlib.sha256(p.stdout.encode()).hexdigest())
def validate(output):
    lines=output.splitlines()
    require(lines and lines[-1].split()==["PASS",str(len(lines)-1)],"incomplete stream")
    expected=[(R,a,b,c) for R in range(18,22) for a in range(1,R+1)
              for b in range(a,R+1) for c in range(b,R+1) if a+b+c<=R+1]
    require(len(lines)-1==len(expected),"missing configurations")
    records=[]
    for line,key in zip(lines[:-1],expected,strict=True):
        tokens=line.split()
        require(len(tokens)==5 and all(re.fullmatch(r"-?\d+",t) for t in tokens),"bad bound row")
        row=list(map(int,tokens))
        require(tuple(row[:4])==key and row[4]<=0,"wrong configuration or strip predicate")
        records.append(row)
    return dict(status="PASS",complete=True,configurations=len(records),bounds=records,
                by_allowance=[dict(R=R,configurations=sum(r[0]==R for r in records),
                                  maximum_bound=max(r[4] for r in records if r[0]==R))
                              for R in range(18,22)])
def replay(output):
    clock=time.monotonic()
    record=dict(schema_version=1,component="R6a",status="FAIL",complete=False,
                exit_status=1,started_utc=now(),fresh=True,cache_free=True,archive_inputs=False)
    try:
        require(not sys.flags.optimize,"optimized runner unsupported")
        require(not git("status","--porcelain","--untracked-files=no"),"tracked inputs dirty")
        record["repository_input_commit"]=git("rev-parse","HEAD")
        for p in INPUTS: git("ls-files","--error-unmatch",p)
        hashes={p:digest(ROOT/p) for p in INPUTS}
        record["sources"]=[dict(path=p,sha256=h) for p,h in hashes.items()]
        compiler=shutil.which("c++");require(compiler is not None,"missing C++17 compiler")
        version,_=call([compiler,"--version"]);require(version.returncode==0,"compiler identity")
        record["environment"]=dict(python=sys.version,platform=platform.platform(),
                                   compiler=version.stdout,dependencies="C++17 and Python standard libraries")
        record["replay_command"]=[sys.executable,*sys.orig_argv[1:]]
        results,processes,negatives=[],[],[]
        with tempfile.TemporaryDirectory(prefix="wilf-r6a-") as tmp:
            for name in ("check_strip_prefix.cpp","check_strip_points.cpp"):
                exe=str(Path(tmp)/Path(name).stem)
                p,info=call([compiler,"-std=c++17","-O3","-Wall","-Wextra","-pedantic",
                             str(HERE/name),"-o",exe]);processes.append(info)
                require(p.returncode==0 and not p.stderr,"compilation failure or warning")
                for label,args in (("partial_mode",["--sample","1"]),("unexpected_argument",["1"])):
                    p,info=call([exe,*args])
                    require(p.returncode!=0 and "failed:" in p.stderr,"accepted partial mode")
                    negatives.append(dict(checker=name,mutation=label,rejected=True,**info))
                p,info=call([exe]);processes.append(info)
                require(p.returncode==0 and not p.stderr,"complete strip execution failed")
                results.append(dict(checker=name,**validate(p.stdout)))
        require(results[0]["bounds"]==results[1]["bounds"],"independent bound disagreement")
        require(all(digest(ROOT/p)==h for p,h in hashes.items()),"proof input changed")
        record.update(status="PASS",complete=True,exit_status=0,results=results,processes=processes,
                      negative_tests=negatives,independent_agreement=True,unresolved=0,unsupported=0,
                      establishes="B6-strip-FV and its conditional 5/42 continuous consequence",
                      does_not_establish=["external review","B6-high-FV","global theorem"])
    except Exception as e: record["error"]=f"{type(e).__name__}: {e}"
    record.update(finished_utc=now(),elapsed_seconds=time.monotonic()-clock)
    output.write_text(json.dumps(record,indent=2,sort_keys=True)+"\n")
    print(json.dumps(dict(component="R6a",status=record["status"],error=record.get("error"),
                         elapsed_seconds=record["elapsed_seconds"])))
    return record["exit_status"]
def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record",type=Path,default=HERE/"r6a-replay.json")
    p=parser.parse_args().record.resolve()
    if p.parent!=HERE or not re.fullmatch(r"r6a-replay(?:-[\w-]+)?\.json",p.name):
        parser.error("record must be r6a-replay[-suffix].json in verification/b6")
    return replay(p)
if __name__=="__main__": raise SystemExit(main())
