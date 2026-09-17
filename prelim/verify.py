#!/usr/bin/env python3
"""Complete standalone replay. Only Python's standard library and C++17 are needed."""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import time

ROOT=Path(__file__).resolve().parent
CODE=ROOT/"code"
CORNERS=((1,1,3),(1,2,2),(1,1,4),(1,2,3),(2,2,2),(1,1,5),(1,2,4),(1,3,3),(2,2,3))

def require(condition,reason):
    if not condition: raise RuntimeError(reason)

def unique(pairs):
    result={}
    for key,value in pairs:
        require(key not in result,"duplicate JSON key")
        result[key]=value
    return result

def nonfinite(value): raise RuntimeError("nonfinite JSON constant")

def decode(raw): return json.loads(raw,object_pairs_hook=unique,parse_constant=nonfinite)

def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def inputs(packet=ROOT):
    packet=packet.resolve()
    raw=(packet/"manifest.json").read_bytes();manifest=decode(raw)
    require(type(manifest) is dict and set(manifest)=={"schema_version","format","inputs"},"manifest schema")
    require(type(manifest["schema_version"]) is int and manifest["schema_version"]==1
            and manifest["format"]=="wilf-four-prelim-v1","manifest identity")
    entries=manifest["inputs"];require(type(entries) is list and entries,"missing inputs")
    seen=set()
    for entry in entries:
        require(type(entry) is dict and set(entry)=={"path","bytes","sha256"},"input descriptor")
        path=entry["path"]
        require(type(path) is str and path not in seen and not Path(path).is_absolute(),"input path")
        target=(packet/path).resolve();require(target.is_relative_to(packet),"input path escape")
        require(type(entry["bytes"]) is int and entry["bytes"]>0 and type(entry["sha256"]) is str
                and re.fullmatch("[0-9a-f]{64}",entry["sha256"]),"input hash descriptor")
        require(target.stat().st_size==entry["bytes"] and digest(target)==entry["sha256"],"input changed: "+path)
        seen.add(path)
    expected={"README.md","proof.md","analytic-details.md","verification.md","verify.py"}
    expected.update(str(p.relative_to(packet)) for folder in ("code","data") for p in (packet/folder).iterdir() if p.is_file())
    require(seen==expected,"missing/extra packet inputs")
    return raw,entries

def call(command,label):
    clock=time.monotonic()
    run=subprocess.run(command,cwd=ROOT,capture_output=True,text=True)
    info=dict(label=label,elapsed_seconds=time.monotonic()-clock,exit_status=run.returncode,
              stdout_sha256=hashlib.sha256(run.stdout.encode()).hexdigest(),stderr=run.stderr)
    return run,info

def success(run):
    require(run.returncode==0 and run.stderr=="","process failed/warned: "+run.stderr)

def load_module(name):
    spec=importlib.util.spec_from_file_location(name,CODE/(name+".py"))
    require(spec is not None and spec.loader is not None,"checker import")
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module

def negative_coverage():
    results=[]
    for name in ("trees_integer","trees_rational"):
        module=load_module(name)
        def document(component,nodes):
            q=4096;r,h={"b2":(5,24),"b4":(6,42),"b6":(7,78)}[component]
            return dict(schema_version=1,component=component,scale=q,
                        root=[[q,q,r*q],[h*q]*3],nodes=nodes)
        tests=[
            ("unsupported_leaf",document("b2",[[-4]]),"b2"),
            ("extra_cached_answer",document("b2",[[-2,0]]),"b2"),
            ("unsound_empty",document("b2",[[-1]]),"b2"),
            ("unjustified_analytic",document("b2",[[-3]]),"b2"),
            ("unreachable_node",document("b2",[[-2],[-2]]),"b2"),
            ("repeated_child",document("b2",[[0,5000,1,1],[-2]]),"b2"),
            ("boundary_split",document("b2",[[0,4096,1,2],[-2],[-2]]),"b2"),
            ("boolean_tag",document("b2",[[True]]),"b2"),
            ("high_analytic",document("b6",[[-3]]),"b6"),
            ("wrong_root",document("b4",[[-2]]),"b2"),
        ]
        for label,value,component in tests:
            rejected=False
            try: module.coverage(value,component)
            except (RuntimeError,ValueError): rejected=True
            require(rejected,"mutation accepted: "+name+"/"+label)
            results.append(dict(checker=name,mutation=label,rejected=True))
        try: module.decode('{"a":1,"a":2}') if hasattr(module,"decode") else module.read('{"a":1,"a":2}')
        except (RuntimeError,ValueError): pass
        else: raise RuntimeError("duplicate JSON accepted")
        results.append(dict(checker=name,mutation="duplicate_json_key",rejected=True))
    return results

def negative_manifest():
    with tempfile.TemporaryDirectory(prefix="wilf-hash-test-") as temporary:
        folder=Path(temporary)
        source=folder/"proof.md";source.write_text("changed")
        entry=dict(path="proof.md",bytes=7,sha256="0"*64)
        (folder/"manifest.json").write_text(json.dumps(
            dict(schema_version=1,format="wilf-four-prelim-v1",inputs=[entry])))
        try: inputs(folder)
        except RuntimeError as error:
            require("input changed" in str(error),"wrong hash-test failure")
        else: raise RuntimeError("wrong manifest hash accepted")
    return [dict(checker="verify.py",mutation="input_hash_mismatch",rejected=True)]

def b1(output):
    rows=[decode(line) for line in output.splitlines()]
    require(len(rows)==10,"small-multiplicity incomplete output")
    common=[]
    fields=("m","generator_bound_inclusive","raw_triples","smallest_redundant","middle_redundant",
            "largest_redundant","nontrivial_gcd","minimal_four_generator_semigroups",
            "maximum_apery_within_bound","negative_wilf_count","minimum_wilf_with_bounded_apery",
            "bounded_minimum_example","bounded_checksum_fnv1a64")
    for m,row in zip(range(20,30),rows,strict=True):
        require(type(row) is dict and set(fields)<=set(row),"generator-box schema")
        for field in fields[:-2]: require(type(row[field]) is int,"generator-box integer")
        bound=m*(m-2)
        require(row["m"]==m and row["generator_bound_inclusive"]==bound
                and row["raw_triples"]==math.comb(bound-m,3),"generator-box coverage")
        require(row["raw_triples"]==sum(row[k] for k in
                ("smallest_redundant","middle_redundant","largest_redundant",
                 "nontrivial_gcd","minimal_four_generator_semigroups")),"generator-box partition")
        require(row["negative_wilf_count"]==0 and row["minimum_wilf_with_bounded_apery"]>=0
                and row["maximum_apery_within_bound"]>0,"generator-box predicate")
        require(type(row["bounded_checksum_fnv1a64"]) is str and row["bounded_checksum_fnv1a64"].isdigit(),
                "generator-box checksum")
        common.append({k:row[k] for k in fields})
    return dict(status="PASS",complete=True,multiplicities=common)

def b4_low(output):
    lines=output.splitlines();require(len(lines)==1,"local-profile partial output")
    result=decode(lines[0])
    require(result["status"]=="PASS" and result["complete"] is True
            and result["unresolved"]==result["unsupported"]==0,"local-profile incomplete")
    counts=result["counts"]
    require(counts["eligible"]==counts["local_pass"]+len(result["exceptions"])
            and len(result["exceptions"])==2 and result["minimum_local_margin"]>=0,"local-profile predicate")
    require(result["largest_cardinality"]<=48 and len(result["profile_counts"])==2,"local-profile bounds")
    return {k:v for k,v in result.items() if k not in ("component","arithmetic","archive_inputs")}

def b5(output):
    rows=[decode(line) for line in output.splitlines()]
    require(len(rows)==10,"degree-six partial output");summary=rows.pop()
    require(summary["status"]=="PASS" and summary["complete"] is True
            and type(summary["profiles"]) is int and summary["profiles"]>0,"degree-six summary")
    for pid,(corner,row) in enumerate(zip(CORNERS,rows,strict=True)):
        require(set(row)=={"pid","corner","compatible","degree_filtered","m30","eligible","local_pass",
                "axis_pass","axis_fallback","minimum_margin_numerator","minimum_margin_denominator",
                "checksum","histogram"},"degree-six schema")
        require(row["pid"]==pid and row["corner"]==list(corner),"degree-six corner coverage")
        for key in set(row)-{"corner","histogram"}:
            require(type(row[key]) is int and row[key]>=0,"degree-six integer")
        require(row["compatible"]>=row["degree_filtered"]>=row["m30"]>=row["eligible"],"profile filter partition")
        require(row["local_pass"]+row["axis_fallback"]==row["eligible"]
                and row["axis_fallback"]<=row["axis_pass"]<=row["eligible"],"degree-six witness coverage")
        require(row["minimum_margin_denominator"]>0,"degree-six denominator")
        histogram=row["histogram"]
        require(type(histogram) is list and len(histogram)==85
                and all(type(n) is int and n>=0 for n in histogram)
                and sum(histogram)==row["eligible"] and not any(histogram[:30]),"degree-six histogram")
    require(summary["eligible"]==sum(r["eligible"] for r in rows),"degree-six total")
    return dict(status="PASS",complete=True,profiles=summary["profiles"],eligible=summary["eligible"],corners=rows)

def strip(output):
    lines=output.splitlines()
    expected=[(r,a,b,d) for r in range(18,21) for a in range(1,r+1)
              for b in range(a,r+1) for d in range(b,r+1) if a+b+d<=r+1]
    require(len(lines)==len(expected)+1 and lines[-1].split()==["PASS",str(len(expected))],"strip incomplete")
    rows=[]
    for key,line in zip(expected,lines[:-1],strict=True):
        parts=line.split();require(len(parts)==5 and all(re.fullmatch("-?[0-9]+",p) for p in parts),"strip schema")
        row=tuple(map(int,parts));require(row[:4]==key and row[4]<=0,"strip configuration/predicate");rows.append(row)
    return dict(status="PASS",complete=True,configurations=len(rows),
                bound_sha256=hashlib.sha256(json.dumps(rows,separators=(",",":")).encode()).hexdigest(),
                by_allowance=[dict(R=r,configurations=sum(x[0]==r for x in rows),
                                  largest_bound=max(x[4] for x in rows if x[0]==r)) for r in range(18,21)])

def tree(output):
    rows=output.splitlines();require(len(rows)==1,"tree partial output");result=decode(rows[0])
    require(set(result)=={"component","status","complete","tree_nodes","node_kinds","dp_leaves",
            "vacuous_dp_leaves","bounds_checked","largest_bound","leaf_sha256","tree_sha256",
            "unresolved","unsupported","environment"},"tree result schema")
    require(result["status"]=="PASS" and result["complete"] is True
            and result["unresolved"]==result["unsupported"]==0,"tree incomplete")
    require(sum(result["node_kinds"].values())==result["tree_nodes"] and result["dp_leaves"]>0,"tree partition")
    return {k:v for k,v in result.items() if k!="environment"}

def run_pair(label,names,validator,native,processes,negatives):
    with tempfile.TemporaryDirectory(prefix="wilf-prelim-") as temporary:
        commands=[]
        if native:
            compiler=shutil.which("c++");require(compiler is not None,"C++17 compiler missing")
            for filename in names:
                binary=str(Path(temporary)/Path(filename).stem)
                build,info=call([compiler,"-std=c++17","-O3","-Wall","-Wextra","-pedantic",
                                 str(CODE/filename),"-o",binary],label+"/"+filename+"/compile")
                processes.append(info);success(build);commands.append([binary])
        else:
            commands=[[sys.executable,"-I","-B",str(CODE/filename)] for filename in names]
        for name,command in zip(names,commands,strict=True):
            rejected,info=call([*command,"--sample","1"],label+"/"+name+"/partial-mode")
            require(rejected.returncode!=0,"partial mode accepted")
            negatives.append(dict(checker=name,mutation="partial_mode",rejected=True))
            if not native:
                rejected,info=call([sys.executable,"-O","-I","-B",str(CODE/name)],label+"/"+name+"/optimized")
                require(rejected.returncode!=0,"optimized mode accepted")
                negatives.append(dict(checker=name,mutation="optimized_mode",rejected=True))
        with ThreadPoolExecutor(max_workers=2) as pool:
            futures=[pool.submit(call,command,label+"/"+name) for name,command in zip(names,commands,strict=True)]
            runs=[f.result() for f in futures]
        normalized=[]
        for process,info in runs:
            processes.append(info);success(process);normalized.append(validator(process.stdout))
        require(normalized[0]==normalized[1],"independent disagreement: "+label)
        return dict(component=label,independent_agreement=True,**normalized[0])

def replay():
    started=datetime.now(timezone.utc).isoformat();clock=time.monotonic()
    record=dict(schema_version=1,packet="wilf-four-prelim",status="FAIL",complete=False,started_utc=started,
                fresh=True,cache_free=True,processes=[],negative_tests=[],components=[])
    output=ROOT/"replay.json"
    try:
        require(not sys.flags.optimize,"optimized Python runner unsupported")
        raw,entries=inputs()
        record["manifest_sha256"]=hashlib.sha256(raw).hexdigest();record["inputs"]=entries
        compiler=shutil.which("c++");require(compiler is not None,"C++17 compiler missing")
        version,info=call([compiler,"--version"],"compiler identity");success(version)
        record["processes"].append(info)
        record["environment"]=dict(python=sys.version,platform=platform.platform(),
                                  compiler=version.stdout,
                                  dependencies="Python standard library and C++17; no third-party packages")
        record["replay_command"]=["python3","-I","-B","verify.py"]
        record["negative_tests"].extend(negative_coverage())
        record["negative_tests"].extend(negative_manifest())
        for name in ("trees_integer.py","trees_rational.py"):
            failed,_=call([sys.executable,"-O","-I","-B",str(CODE/name),"b2"],name+"/optimized")
            require(failed.returncode!=0,"optimized tree checker accepted")
            record["negative_tests"].append(dict(checker=name,mutation="optimized_mode",rejected=True))
        for label,names,validate,native in (
            ("generator-box",("b1_residues.cpp","b1_membership.cpp"),b1,True),
            ("short-corner-low",("b4_low_offsets.py","b4_low_successors.py"),b4_low,False),
            ("degree-six",("b5_bits.cpp","b5_columns.cpp"),b5,True),
            ("strip",("b6_strip_prefix.cpp","b6_strip_points.cpp"),strip,True),
        ):
            print(json.dumps(dict(component=label,phase="two complete fresh paths")),flush=True)
            result=run_pair(label,names,validate,native,record["processes"],record["negative_tests"])
            record["components"].append(result)
            print(json.dumps(dict(component=label,status="PASS")),flush=True)
        for component in ("b2","b4","b6"):
            print(json.dumps(dict(component=component,phase="two complete fresh trees")),flush=True)
            with ThreadPoolExecutor(max_workers=2) as pool:
                futures=[pool.submit(call,[sys.executable,"-I","-B",str(CODE/name),component],component+"/"+name)
                         for name in ("trees_integer.py","trees_rational.py")]
                runs=[f.result() for f in futures]
            normalized=[]
            for process,info in runs:
                record["processes"].append(info);success(process);normalized.append(tree(process.stdout))
            require(normalized[0]==normalized[1],"independent tree disagreement: "+component)
            record["components"].append(dict(independent_agreement=True,**normalized[0]))
            print(json.dumps(dict(component=component,status="PASS")),flush=True)
        require(inputs()[0]==raw,"inputs/manifest changed during replay")
        record.update(status="PASS",complete=True,independent_agreement=True,unresolved=0,unsupported=0,
                      establishes="all seven retained finite premises of the preliminary proof",
                      does_not_establish=["published multiplicity-at-most-19 computation",
                                          "proof-assistant certification","external mathematical review"])
    except Exception as error: record["error"]=f"{type(error).__name__}: {error}"
    record.update(finished_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-clock)
    output.write_text(json.dumps(record,indent=2,sort_keys=True)+"\n")
    print(json.dumps(dict(status=record["status"],complete=record["complete"],error=record.get("error"),
                         elapsed_seconds=record["elapsed_seconds"])),flush=True)
    return 0 if record["complete"] else 1

def main():
    argparse.ArgumentParser(description=__doc__).parse_args()
    return replay()

if __name__=="__main__": raise SystemExit(main())
