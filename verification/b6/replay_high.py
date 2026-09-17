#!/usr/bin/env python3
"""Fresh complete R6b replay; independently checked trees and no leaf caches."""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import re
import subprocess
import sys
import tempfile
import time
ROOT=Path(__file__).resolve().parents[2]
HERE=ROOT/"verification/b6"
CERT="artifacts/wilf_four_generators_review_package_2026-09-11/round7/geometric_residual/residual_parallel_interval_certificate.json"
INPUTS=("verification/b6/replay_high.py","verification/b6/check_high_integer.py",
        "verification/b6/check_high_rational.py","verification/b6/high_subtract.cpp",
        "verification/b6/high_disjoint.cpp","verification/b6/certificate-manifest.json",CERT,
        "paper/residual-high-height.md","paper/phase-and-thickening.md","paper/central-box-horns.md",
        "research/b6-simplification-decision.md","verification/b6/r6a-replay.json")
def require(condition,why):
    if not condition: raise RuntimeError(why)
def now(): return datetime.now(timezone.utc).isoformat()
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def git(*args):
    p=subprocess.run(["git",*args],cwd=ROOT,capture_output=True,text=True)
    require(p.returncode==0,p.stderr);return p.stdout.strip()
def call(command):
    start,clock=now(),time.monotonic()
    p=subprocess.run(command,cwd=ROOT,capture_output=True,text=True)
    return p,dict(command=command,started_utc=start,finished_utc=now(),
                  elapsed_seconds=time.monotonic()-clock,exit_status=p.returncode,stderr=p.stderr,
                  stdout_sha256=hashlib.sha256(p.stdout.encode()).hexdigest())
def check_command(name,manifest,optimized=False):
    return [sys.executable,*(["-O"] if optimized else []),"-I","-B",str(HERE/name),
            "--manifest",str(manifest)]
def negative_tests():
    original=json.loads((HERE/"certificate-manifest.json").read_bytes());results=[]
    names=("check_high_integer.py","check_high_rational.py")
    def reject(label,path,optimized=False):
        for name in names:
            p,info=call(check_command(name,path,optimized))
            require(p.returncode!=0 and "failed:" in p.stderr,"mutation not rejected")
            results.append(dict(checker=name,mutation=label,rejected=True,**info))
    reject("optimized_execution",HERE/"certificate-manifest.json",True)
    with tempfile.TemporaryDirectory(prefix=".r6b-negative-",dir=HERE) as tmp:
        folder=Path(tmp);manifest=folder/"manifest.json";cert=folder/"certificate.json"
        value=json.loads(json.dumps(original));value["certificate"]["sha256"]="0"*64
        manifest.write_text(json.dumps(value));reject("certificate_hash_mismatch",manifest)
        manifest.write_text('{"schema_version":1,'+json.dumps(original)[1:])
        reject("duplicate_manifest_field",manifest)
        root=original["constants"]["root"]
        header=dict(scope="conditional attempted certificate generic p",scale=4096,initial=root,
                    complete=True,tree=[],nodes=1,unresolved=[],stack=[],seconds=0,dp_calls=0,corner_cases=0)
        mutations=[
            ("unsupported_kind",[dict(box=root,kind="unsupported")]),
            ("five_cached_fields",[dict(box=root,kind="dp",bounds=[0,1,1,3,1])]),
            ("unsound_empty_leaf",[dict(box=root,kind="empty")]),
            ("boolean_endpoint",[dict(box=[[True,4096,28672],root[1]],kind="empty")]),
        ]
        # The first child's lower b endpoint is one unit too high.
        mutations.append(("child_boundary_gap",[
            dict(box=root,kind="split",axis=1,mid=30720,children=[1,2]),
            dict(box=[[4097,4096,28672],[14336,30720,163840]],kind="empty"),
            dict(box=[[4096,30720,28672],[14336,55296,163840]],kind="empty")]))
        for label,nodes in mutations:
            cert.write_text(json.dumps({**header,"tree":nodes,"nodes":len(nodes)}))
            value=json.loads(json.dumps(original))
            value["certificate"]=dict(path=str(cert.relative_to(ROOT)),sha256=digest(cert),bytes=cert.stat().st_size)
            manifest.write_text(json.dumps(value));reject(label,manifest)
    return results
def result(p,component):
    require(p.returncode==0 and not p.stderr,"complete checker failed: "+p.stderr)
    require(len(p.stdout.splitlines())==1,"partial or extra checker output")
    value=json.loads(p.stdout)
    require(type(value) is dict and set(value)=={
        "component","status","complete","coverage_checked","fresh_leaf_recomputation","cache_free",
        "certificate_sha256","tree_nodes","node_kinds","dp_leaves","vacuous_dp_leaves",
        "corner_bounds_checked","largest_bound_numerator","leaf_result_sha256","unresolved","unsupported",
        "compiler","backend_sha256"},"result schema")
    require(value["component"]==component and value["status"]=="PASS","result identity")
    for k in ("complete","coverage_checked","fresh_leaf_recomputation","cache_free"):
        require(value[k] is True,"incomplete replay")
    for k in ("tree_nodes","dp_leaves","vacuous_dp_leaves","corner_bounds_checked","unresolved","unsupported"):
        require(type(value[k]) is int and value[k]>=0,"result integer")
    require(value["unresolved"]==value["unsupported"]==0 and value["dp_leaves"]>0,"unsupported/empty replay")
    require(type(value["largest_bound_numerator"]) is int and 10*value["largest_bound_numerator"]<=29*4096,
            "result threshold")
    kinds=value["node_kinds"]
    require(type(kinds) is dict and set(kinds)<={"split","empty","dp"}
            and all(type(n) is int and n>=0 for n in kinds.values()),"kind partition")
    require(sum(kinds.values())==value["tree_nodes"] and kinds.get("dp",0)==value["dp_leaves"],"node count")
    for k in ("certificate_sha256","leaf_result_sha256","backend_sha256"):
        require(type(value[k]) is str and re.fullmatch("[0-9a-f]{64}",value[k]),"hash field")
    return value
def replay(output):
    clock=time.monotonic()
    record=dict(schema_version=1,component="R6b",status="FAIL",complete=False,exit_status=1,
                started_utc=now(),fresh=True,cache_free=True)
    try:
        require(not sys.flags.optimize,"optimized runner unsupported")
        require(not git("status","--porcelain","--untracked-files=no"),"tracked inputs dirty")
        record["repository_input_commit"]=git("rev-parse","HEAD")
        for path in INPUTS: git("ls-files","--error-unmatch",path)
        hashes={p:digest(ROOT/p) for p in INPUTS}
        record["sources"]=[dict(path=p,sha256=h) for p,h in hashes.items()]
        record["environment"]=dict(python=sys.version,platform=platform.platform(),
                                   dependencies="C++17 and Python standard libraries; no OpenMP")
        record["replay_command"]=[sys.executable,*sys.orig_argv[1:]]
        record["negative_tests"]=negative_tests()
        print(json.dumps(dict(component="R6b",phase="negative tests passed; two complete paths running")),flush=True)
        with ThreadPoolExecutor(max_workers=2) as pool:
            futures=[pool.submit(call,check_command(name,HERE/"certificate-manifest.json"))
                     for name in ("check_high_integer.py","check_high_rational.py")]
            runs=[future.result() for future in futures]
        results=[result(p,component) for (p,_),component in zip(runs,("R6b-A","R6b-B"),strict=True)]
        normalized=[{k:v for k,v in r.items() if k not in ("component","compiler","backend_sha256")} for r in results]
        require(normalized[0]==normalized[1],"independent coverage/leaf disagreement")
        require(all(digest(ROOT/p)==h for p,h in hashes.items()),"input changed during replay")
        record.update(status="PASS",complete=True,exit_status=0,results=results,
                      processes=[info for _,info in runs],independent_agreement=True,unresolved=0,unsupported=0,
                      establishes="B6-high-FV; with the strip and analytic transfer, B6 is internally closed",
                      does_not_establish=["external mathematical review","global composition audit"])
    except Exception as error: record["error"]=f"{type(error).__name__}: {error}"
    record.update(finished_utc=now(),elapsed_seconds=time.monotonic()-clock)
    output.write_text(json.dumps(record,indent=2,sort_keys=True)+"\n")
    print(json.dumps(dict(component="R6b",status=record["status"],elapsed_seconds=record["elapsed_seconds"],
                         error=record.get("error"))),flush=True)
    return record["exit_status"]
def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record",type=Path,default=HERE/"r6b-replay.json")
    output=parser.parse_args().record.resolve()
    if output.parent!=HERE or not re.fullmatch(r"r6b-replay(?:-[\w-]+)?\.json",output.name):
        parser.error("record must be r6b-replay[-suffix].json in verification/b6")
    return replay(output)
if __name__=="__main__": raise SystemExit(main())
