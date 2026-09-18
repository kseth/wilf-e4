#!/usr/bin/env python3
"""Finite Lemmas 2.3, 2.4, and 2.8: depth-first coverage and integer evaluators."""
from __future__ import annotations
import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
PACKET = HERE.parent
Q = 4096

def require(condition, message):
    if not condition: raise RuntimeError(message)

def unique(pairs):
    result = {}
    for key,value in pairs:
        require(key not in result, "duplicate JSON key")
        result[key] = value
    return result

def reject(value): raise RuntimeError("nonfinite JSON number")

def decode(raw):
    return json.loads(raw, object_pairs_hook=unique, parse_constant=reject)

def root(component):
    return ((Q,Q,{"no-corner-interval":5,"short-corner-high":6,"high-height":7}[component]*Q),
            ({"no-corner-interval":24,"short-corner-high":42,"high-height":78}[component]*Q,)*3)

def tighten(low, high, component):
    low,high = list(low),list(high)
    for _ in range(20 if component == "high-height" else 1):
        old = tuple(low),tuple(high)
        low = [low[0],max(low[:2]),max(low)]
        high = [min(high),min(high[1:]),high[2]]
        if any(x>y for x,y in zip(low,high)): return None
        if component == "high-height":
            require(low[2]>3*Q,"nonpositive clipping denominator")
            ceiling = lambda a,b: -(-a//b)
            cap = 9*Q+ceiling(28*Q*Q,low[2]-3*Q)
            high[0] = min(high[0],ceiling(cap-Q,2))
            high[1] = min(high[1],cap-Q-low[0])
            upper_sum = min(Q+high[0]+high[1],cap)
            high[2] = min(high[2],ceiling(42*Q+37*upper_sum,5))
        if (tuple(low),tuple(high)) == old: break
    return None if any(x>y for x,y in zip(low,high)) else (tuple(low),tuple(high))

def coverage(data, component):
    require(type(data) is dict and set(data)=={"schema_version","component","scale","root","nodes"},"tree schema")
    require(type(data["schema_version"]) is int and data["schema_version"]==1
            and data["component"]==component and type(data["scale"]) is int and data["scale"]==Q,"tree identity")
    endpoints = data["root"]
    require(type(endpoints) is list and len(endpoints)==2
            and all(type(a) is list and len(a)==3 and all(type(x) is int for x in a) for a in endpoints),
            "root endpoint types")
    initial = tuple(map(tuple,endpoints));require(initial==root(component),"wrong root")
    nodes = data["nodes"];require(type(nodes) is list and len(nodes)>0,"no tree")
    stack = [(0,initial)];seen=set();counts=Counter();leaves=[];terminal=[]
    while stack:
        index,(low,high) = stack.pop()
        require(type(index) is int and 0<=index<len(nodes) and index not in seen,"invalid/repeated child")
        seen.add(index);node=nodes[index]
        require(type(node) is list and all(type(x) is int for x in node),"node integer schema")
        box=tighten(low,high,component)
        if len(node)==4:
            require(box is not None,"split in empty region")
            low,high=box;axis,mid,left,right=node
            require(0<=axis<3 and low[axis]<mid<high[axis] and left!=right,"split geometry")
            lower_right,upper_left=list(low),list(high)
            lower_right[axis]=upper_left[axis]=mid
            stack.extend([(right,(tuple(lower_right),high)),(left,(low,tuple(upper_left)))])
            counts["split"]+=1;continue
        require(len(node)==1 and node[0] in (-1,-2,-3),"unknown/extra leaf fields")
        tag=node[0]
        if box is None:
            require(tag==-1,"empty region not empty leaf")
            counts["empty"]+=1;terminal.append((index,"empty",None,0));continue
        require(tag!=-1,"unsound empty leaf");low,high=box
        if tag==-3:
            require(component!="high-height","unsupported analytic leaf")
            weight_sum=Q+high[0]+high[1]
            if component=="no-corner-interval":
                require(low[2]>=2*weight_sum+3*Q,"continuous leaf inequality")
            else:
                require(low[2]>=4*weight_sum+3*Q,"planar leaf inequality")
            counts["analytic"]+=1;terminal.append((index,"analytic",None,0))
        else:
            counts["dp"]+=1;leaves.append((index,low,high))
    require(len(seen)==len(nodes),"unreachable nodes")
    require(counts["dp"]>0,"no computational leaves")
    leaves.sort()
    return leaves,terminal,dict(sorted(counts.items()))

def cpp(component, leaves):
    source=HERE/{"short-corner-high":"short_corner_high_prefix.cpp","high-height":"high_height_subtract.cpp"}[component]
    compiler=shutil.which("c++");require(compiler is not None,"C++17 compiler missing")
    version=subprocess.run([compiler,"--version"],capture_output=True,text=True,check=True).stdout.splitlines()[0]
    with tempfile.TemporaryDirectory(prefix="wilf-integer-") as directory:
        executable=str(Path(directory)/"evaluate")
        flags=["-std=c++17","-O3","-Wall","-Wextra","-pedantic"]
        build=subprocess.run([compiler,*flags,str(source),"-o",executable],capture_output=True,text=True)
        require(build.returncode==0 and not build.stderr,"compile failure/warning: "+build.stderr)
        workers=min(len(leaves),4,max(1,(os.cpu_count() or 2)//2))
        def batch(start):
            positions=range(start,len(leaves),workers)
            request="".join(" ".join(map(str,(Q,*leaves[i][1],*leaves[i][2])))+"\n"
                            for i in positions)
            run=subprocess.run([executable],input=request,capture_output=True,text=True)
            require(run.returncode==0 and not run.stderr,"worker failure: "+run.stderr)
            responses=run.stdout.splitlines()
            require(len(responses)==len(positions),"partial worker response")
            return list(zip(positions,responses,strict=True))
        rows=[None]*len(leaves)
        with ThreadPoolExecutor(max_workers=workers) as pool:
            for answers in pool.map(batch,range(workers)):
                for position,row in answers:
                    require(rows[position] is None,"duplicate worker response")
                    rows[position]=row
        require(all(type(row) is str for row in rows),"missing worker response")
        values=[]
        for row in rows:
            cells=row.split()
            require(len(cells)==(3 if component=="short-corner-high" else 2)
                    and all(re.fullmatch(r"-?\d+",x) for x in cells),"worker response schema")
            integers=tuple(map(int,cells))
            if component=="short-corner-high":
                require(max(integers)<=Q,"short-corner predicate");values.append((integers,3))
            else:
                bound,cases=integers
                require(cases>=0 and (cases>0 or bound==0),"invalid vacuity")
                require(not cases or 10*bound<=29*Q,"high-height predicate")
                values.append((bound if cases else None,cases))
    return values,dict(version=version,flags=flags,source=source.name,workers=workers)

def check(component):
    require(not sys.flags.optimize,"optimized Python unsupported")
    path=PACKET/"data"/(component+".json");raw=path.read_bytes()
    manifest=decode((PACKET/"manifest.json").read_bytes())
    descriptors=[d for d in manifest["inputs"] if d["path"]==f"data/{component}.json"]
    require(len(descriptors)==1,"tree absent/duplicated in manifest")
    d=descriptors[0]
    require(len(raw)==d["bytes"] and hashlib.sha256(raw).hexdigest()==d["sha256"],"tree hash mismatch")
    leaves,terminal,counts=coverage(decode(raw),component)
    if component=="no-corner-interval":
        spec=importlib.util.spec_from_file_location("no_corner_interval_prefix",HERE/"no_corner_interval_prefix.py")
        require(spec is not None and spec.loader is not None,"evaluator module")
        evaluator=importlib.util.module_from_spec(spec);spec.loader.exec_module(evaluator)
        values=[(evaluator.prefix_bound(low,high,Q),1) for _,low,high in leaves]
        require(all(value<=Q for value,_ in values),"no-corner predicate")
        environment=dict(arithmetic="Python integers",source="no_corner_interval_prefix.py")
    else: values,environment=cpp(component,leaves)
    extrema=[];total=0;vacuous=0
    for (index,_,_),(value,cases) in zip(leaves,values,strict=True):
        terminal.append((index,"dp",value,cases));total+=cases
        if cases:
            extrema.extend(value if isinstance(value,tuple) else (value,))
        else: vacuous+=1
    digest=hashlib.sha256()
    for entry in sorted(terminal):
        digest.update((json.dumps(entry,separators=(",",":"))+"\n").encode())
    return dict(component=component,status="PASS",complete=True,tree_nodes=sum(counts.values()),
                node_kinds=counts,dp_leaves=len(leaves),vacuous_dp_leaves=vacuous,
                bounds_checked=total,largest_bound=max(extrema),leaf_sha256=digest.hexdigest(),
                tree_sha256=hashlib.sha256(raw).hexdigest(),unresolved=0,unsupported=0,
                environment=environment)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("component",choices=("no-corner-interval","short-corner-high","high-height"))
    args=parser.parse_args()
    try: print(json.dumps(check(args.component),sort_keys=True));return 0
    except Exception as error: print(f"integer tree failed: {error}",file=sys.stderr);return 1

if __name__=="__main__": raise SystemExit(main())
