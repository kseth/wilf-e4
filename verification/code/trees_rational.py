#!/usr/bin/env python3
"""Independent breadth-first coverage, rational clipping, independent evaluators."""
from __future__ import annotations
import argparse
from collections import Counter,deque
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

BASE=Path(__file__).resolve().parent
PACKAGE=BASE.parent
SCALE=4096

def ensure(condition, reason):
    if not condition: raise ValueError(reason)

def distinct(fields):
    document={}
    for name,value in fields:
        ensure(name not in document,"duplicate field")
        document[name]=value
    return document

def invalid(value): raise ValueError("invalid JSON number")

def read(raw): return json.loads(raw,object_pairs_hook=distinct,parse_constant=invalid)

def initial(component):
    height_min,height_max={"no-corner-interval":(5,24),"short-corner-high":(6,42),"high-height":(7,78)}[component]
    return ((SCALE,SCALE,height_min*SCALE),(height_max*SCALE,)*3)

def narrow(bottom,top,component):
    bottom=list(bottom);top=list(top)
    for iteration in range(20 if component=="high-height" else 1):
        previous=tuple(bottom+top)
        b0,d0,h0=bottom;b1,d1,h1=top
        bottom=[b0,max(b0,d0),max(b0,d0,h0)]
        top=[min(b1,d1,h1),min(d1,h1),h1]
        if any(a>b for a,b in zip(bottom,top)): return None
        if component=="high-height":
            ensure(bottom[2]>3*SCALE,"denominator outside domain")
            total_cap=9*SCALE+math.ceil(Fraction(28*SCALE*SCALE,bottom[2]-3*SCALE))
            top[0]=min(top[0],math.ceil(Fraction(total_cap-SCALE,2)))
            top[1]=min(top[1],total_cap-SCALE-bottom[0])
            total_upper=min(SCALE+top[0]+top[1],total_cap)
            top[2]=min(top[2],math.ceil(Fraction(42*SCALE+37*total_upper,5)))
        if tuple(bottom+top)==previous: break
    if any(a>b for a,b in zip(bottom,top)): return None
    return tuple(bottom),tuple(top)

def coverage(document,component):
    ensure(type(document) is dict and set(document)=={"schema_version","component","scale","root","nodes"},
           "unexpected top-level fields")
    ensure(type(document["schema_version"]) is int and document["schema_version"]==1
           and document["component"]==component and type(document["scale"]) is int
           and document["scale"]==SCALE,"identity")
    rawroot=document["root"]
    ensure(type(rawroot) is list and len(rawroot)==2,"root dimensions")
    for endpoint in rawroot:
        ensure(type(endpoint) is list and len(endpoint)==3 and all(type(n) is int for n in endpoint),
               "endpoint schema")
    ensure(tuple(map(tuple,rawroot))==initial(component),"wrong root")
    records=document["nodes"];ensure(type(records) is list and len(records)>0,"missing nodes")
    queue=deque([(0,initial(component))]);visited=set();tallies=Counter();work=[];results=[]
    while queue:
        identifier,rectangle=queue.popleft()
        ensure(type(identifier) is int and 0<=identifier<len(records) and identifier not in visited,
               "cycle/repeated/out-of-range child")
        visited.add(identifier);record=records[identifier]
        ensure(type(record) is list and all(type(n) is int for n in record),"node schema")
        enclosure=narrow(*rectangle,component)
        if len(record)==4:
            ensure(enclosure is not None,"empty split")
            bottom,top=enclosure;direction,wall,lchild,rchild=record
            ensure(0<=direction<3 and bottom[direction]<wall<top[direction] and lchild!=rchild,
                   "split does not cover enclosure")
            ltop=list(top);rbottom=list(bottom)
            ltop[direction]=wall;rbottom[direction]=wall
            queue.append((lchild,(bottom,tuple(ltop))))
            queue.append((rchild,(tuple(rbottom),top)))
            tallies["split"]+=1;continue
        ensure(len(record)==1 and record[0] in (-1,-2,-3),"unknown or extended leaf")
        if enclosure is None:
            ensure(record==[-1],"empty leaf type");tallies["empty"]+=1
            results.append((identifier,"empty",None,0));continue
        ensure(record!=[-1],"unjustified empty leaf")
        bottom,top=enclosure
        if record==[-3]:
            ensure(component in ("no-corner-interval","short-corner-high"),"unavailable analytic rule")
            total=Fraction(SCALE+top[0]+top[1],SCALE)
            multiplier=2 if component=="no-corner-interval" else 4
            ensure(Fraction(bottom[2],SCALE)>=multiplier*total+3,"analytic leaf fails")
            tallies["analytic"]+=1;results.append((identifier,"analytic",None,0))
        else:
            tallies["dp"]+=1;work.append((identifier,bottom,top))
    ensure(len(visited)==len(records),"unvisited record")
    ensure(len(work)>0,"no finite leaves")
    return sorted(work),results,dict(sorted(tallies.items()))

def evaluate_native(component,work):
    filename={"short-corner-high":"short_corner_high_direct.cpp","high-height":"high_height_disjoint.cpp"}[component]
    cc=shutil.which("c++");ensure(cc is not None,"compiler unavailable")
    version=subprocess.run([cc,"--version"],capture_output=True,text=True,check=True).stdout.splitlines()[0]
    flags=["-std=c++17","-O3","-Wall","-Wextra","-pedantic"]
    with tempfile.TemporaryDirectory(prefix="wilf-rational-") as folder:
        program=str(Path(folder)/"check")
        built=subprocess.run([cc,*flags,str(BASE/filename),"-o",program],capture_output=True,text=True)
        ensure(built.returncode==0 and built.stderr=="","compilation failed/warned: "+built.stderr)
        workers=min(4,len(work),max(1,(os.cpu_count() or 2)//2))
        # Reverse-order stripes differ from the integer path's forward stripes.
        identifiers=[list(range(len(work)-1-group,-1,-workers)) for group in range(workers)]
        ensure(sorted(i for stripe in identifiers for i in stripe)==list(range(len(work))),
               "batch coverage")
        def execute(stripe):
            requests=[" ".join(str(n) for n in (SCALE,*work[i][1],*work[i][2])) for i in stripe]
            process=subprocess.run([program],input="\n".join(requests)+"\n",capture_output=True,text=True)
            ensure(process.returncode==0 and process.stderr=="","evaluator failure: "+process.stderr)
            output=process.stdout.splitlines();ensure(len(output)==len(stripe),"truncated evaluator")
            return list(zip(stripe,output,strict=True))
        responses={}
        with ThreadPoolExecutor(max_workers=workers) as pool:
            for stripe in pool.map(execute,identifiers):
                for identifier,row in stripe:
                    ensure(identifier not in responses,"repeated response")
                    responses[identifier]=row
        ensure(set(responses)==set(range(len(work))),"missing response")
        output=[responses[i] for i in range(len(work))]
        bounds=[]
        for response in output:
            parts=response.split()
            ensure(len(parts)==(3 if component=="short-corner-high" else 2)
                   and all(re.fullmatch("-?[0-9]+",p) for p in parts),"invalid response")
            numbers=tuple(int(p) for p in parts)
            if component=="short-corner-high":
                ensure(all(n<=SCALE for n in numbers),"short-corner violation");bounds.append((numbers,3))
            else:
                maximum,cardinality=numbers
                ensure(cardinality>=0,"negative corner count")
                if cardinality:
                    ensure(10*maximum<=29*SCALE,"residual interval violation")
                    bounds.append((maximum,cardinality))
                else:
                    ensure(maximum==0,"invalid empty enumeration")
                    bounds.append((None,0))
    return bounds,dict(version=version,flags=flags,source=filename,workers=workers)

def check(component):
    ensure(sys.flags.optimize==0,"optimized execution forbidden")
    raw=(PACKAGE/"data"/f"{component}.json").read_bytes()
    catalog=read((PACKAGE/"manifest.json").read_bytes())["inputs"]
    matches=[entry for entry in catalog if entry["path"]==f"data/{component}.json"]
    ensure(len(matches)==1,"manifest descriptor not unique")
    ensure(matches[0]["bytes"]==len(raw) and matches[0]["sha256"]==hashlib.sha256(raw).hexdigest(),
           "tree identity mismatch")
    work,results,tallies=coverage(read(raw),component)
    if component=="no-corner-interval":
        specification=importlib.util.spec_from_file_location("no_corner_interval_direct",BASE/"no_corner_interval_direct.py")
        ensure(specification is not None and specification.loader is not None,"evaluator import")
        evaluator=importlib.util.module_from_spec(specification);specification.loader.exec_module(evaluator)
        evaluated=[(evaluator.explicit_bound(bottom,top,SCALE),1) for _,bottom,top in work]
        ensure(all(value<=SCALE for value,_ in evaluated),"no-corner interval violation")
        environment=dict(arithmetic="Python integers",source="no_corner_interval_direct.py")
    else: evaluated,environment=evaluate_native(component,work)
    extreme=[];number=0;empty=0
    for request,value in zip(work,evaluated,strict=True):
        identifier,_,_=request;bound,count=value
        results.append((identifier,"dp",bound,count));number+=count
        if count: extreme.extend(bound if type(bound) is tuple else (bound,))
        else: empty+=1
    fingerprint=hashlib.sha256()
    for result in sorted(results):
        fingerprint.update((json.dumps(result,separators=(",",":"))+"\n").encode())
    return dict(component=component,status="PASS",complete=True,tree_nodes=sum(tallies.values()),
                node_kinds=tallies,dp_leaves=len(work),vacuous_dp_leaves=empty,bounds_checked=number,
                largest_bound=max(extreme),leaf_sha256=fingerprint.hexdigest(),
                tree_sha256=hashlib.sha256(raw).hexdigest(),unresolved=0,unsupported=0,
                environment=environment)

def main():
    argument_parser=argparse.ArgumentParser(description=__doc__)
    argument_parser.add_argument("component",choices=("no-corner-interval","short-corner-high","high-height"))
    args=argument_parser.parse_args()
    try: print(json.dumps(check(args.component),sort_keys=True));return 0
    except Exception as failure: print(f"rational tree failed: {failure}",file=sys.stderr);return 1

if __name__=="__main__": raise SystemExit(main())
