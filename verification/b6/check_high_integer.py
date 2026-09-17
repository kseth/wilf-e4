#!/usr/bin/env python3
"""R6b A: strict depth-first coverage, integer outward clipping, subtractive DP."""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
ROOT=Path(__file__).resolve().parents[2]
HERE=ROOT/"verification/b6"
def require(b,why):
    if not b: raise RuntimeError(why)
def unique(pairs):
    out={}
    for k,v in pairs:
        require(k not in out,"duplicate JSON field");out[k]=v
    return out
def reject(value): raise RuntimeError("nonfinite JSON constant")
def decode(raw): return json.loads(raw,object_pairs_hook=unique,parse_constant=reject)
def box(v):
    require(type(v) is list and len(v)==2,"box dimensions")
    require(all(type(e) is list and len(e)==3 and all(type(t) is int for t in e) for e in v),
            "endpoint types")
    a,b=map(tuple,v);require(all(x<=y for x,y in zip(a,b)),"inverted raw box")
    return a,b
def clip(a,b):
    a,b=list(a),list(b);q=4096
    for _ in range(20):
        old=tuple(a),tuple(b)
        a=[a[0],max(a[0],a[1]),max(a)]
        b=[min(b),min(b[1],b[2]),b[2]]
        if any(x>y for x,y in zip(a,b)): return None
        require(a[2]>3*q,"clipping denominator")
        S=9*q-(-(28*q*q)//(a[2]-3*q))
        b[0]=min(b[0],-(-(S-q)//2))
        b[1]=min(b[1],S-q-a[0])
        upper=min(q+b[0]+b[1],S)
        b[2]=min(b[2],-(-(42*q+37*upper)//5))
        if (tuple(a),tuple(b))==old: break
    return None if any(x>y for x,y in zip(a,b)) else (tuple(a),tuple(b))
def load(path):
    manifest=decode(path.read_bytes())
    require(type(manifest) is dict and set(manifest)==
            {"schema_version","component","certificate_format","certificate","constants"},"manifest schema")
    require(type(manifest["schema_version"]) is int and manifest["schema_version"]==1
            and manifest["component"]=="B6-high-FV"
            and manifest["certificate_format"]=="wilf-b6-high-interval-tree-v1","manifest identity")
    d=manifest["certificate"];require(type(d) is dict and set(d)=={"path","sha256","bytes"},"descriptor")
    require(type(d["path"]) is str and not Path(d["path"]).is_absolute(),"path")
    source=(ROOT/d["path"]).resolve();require(source.is_relative_to(ROOT),"path escape")
    require(type(d["sha256"]) is str and re.fullmatch("[0-9a-f]{64}",d["sha256"]),"digest")
    require(type(d["bytes"]) is int and d["bytes"]>0,"byte count")
    raw=source.read_bytes()
    require(len(raw)==d["bytes"] and hashlib.sha256(raw).hexdigest()==d["sha256"],"certificate identity")
    constants=manifest["constants"]
    require(type(constants) is dict and set(constants)=={"scale","root"}
            and type(constants["scale"]) is int and constants["scale"]==4096,"constants")
    root=box(constants["root"])
    require(root==((4096,4096,28672),(319488,319488,319488)),"root")
    data=decode(raw)
    require(type(data) is dict and set(data)==
            {"scope","scale","initial","complete","tree","nodes","unresolved","stack","seconds","dp_calls","corner_cases"},
            "certificate schema")
    require(type(data["scope"]) is str and data["scope"].startswith("conditional attempted certificate generic p"),
            "scope label")
    require(type(data["scale"]) is int and data["scale"]==4096 and box(data["initial"])==root,"data constants")
    require(data["complete"] is True and data["unresolved"]==[] and data["stack"]==[],"partial certificate")
    require(type(data["seconds"]) in (int,float) and math.isfinite(data["seconds"]) and data["seconds"]>=0,
            "timing metadata")
    for k in ("nodes","dp_calls","corner_cases"):
        require(type(data[k]) is int and data[k]>=0,"counter metadata")
    require(type(data["tree"]) is list and data["nodes"]==len(data["tree"])>0,"tree dimensions")
    return data,root,raw
def backend(leaves):
    compiler=shutil.which("c++");require(compiler is not None,"compiler")
    source=HERE/"high_subtract.cpp"
    version=subprocess.run([compiler,"--version"],capture_output=True,text=True,check=True).stdout
    with tempfile.TemporaryDirectory(prefix="wilf-r6b-a-") as temporary:
        exe=str(Path(temporary)/"check")
        command=[compiler,"-std=c++17","-O3","-Wall","-Wextra","-pedantic",str(source),"-o",exe]
        build=subprocess.run(command,capture_output=True,text=True)
        require(build.returncode==0 and not build.stderr,"compile failure/warning")
        request="".join(" ".join(map(str,(4096,*a,*b)))+"\n" for _,a,b,_ in leaves)
        run=subprocess.run([exe],input=request,capture_output=True,text=True)
        require(run.returncode==0 and not run.stderr,"complete backend failed: "+run.stderr)
        rows=run.stdout.splitlines();require(len(rows)==len(leaves),"partial response")
        values=[]
        for line in rows:
            t=line.split();require(len(t)==2 and all(re.fullmatch(r"-?\d+",x) for x in t),"response schema")
            v,n=map(int,t);require(n>=0 and (n>0 or v==0),"vacuous response")
            require(not n or 10*v<=29*4096,"threshold")
            values.append((v,n))
    return values,dict(version=version,command=command)
def check(path):
    require(not sys.flags.optimize,"optimized execution unsupported")
    data,root,raw=load(path);tree=data["tree"];todo=[(0,root)];seen=set();counts=Counter()
    schemas={"empty":{"kind","box"},"dp":{"kind","box","bounds"},
             "split":{"kind","box","axis","mid","children"}}
    leaves=[];terminal=[]
    while todo:
        index,expected=todo.pop()
        require(type(index) is int and 0<=index<len(tree) and index not in seen,"child/cycle")
        seen.add(index);node=tree[index]
        require(type(node) is dict and type(node.get("kind")) is str,"node type")
        kind=node["kind"];require(kind in schemas and set(node)==schemas[kind],"node schema")
        require(box(node["box"])==expected,"child boundary gap");counts[kind]+=1
        tightened=clip(*expected)
        if tightened is None:
            require(kind=="empty","inverted enclosure not empty");terminal.append((index,"empty",None,0));continue
        require(kind!="empty","nonempty leaf marked empty");a,b=tightened
        if kind=="split":
            axis,mid,children=node["axis"],node["mid"],node["children"]
            require(type(axis) is int and 0<=axis<3 and type(mid) is int and a[axis]<mid<b[axis],"split")
            require(type(children) is list and len(children)==2 and all(type(c) is int for c in children)
                    and children[0]!=children[1],"children")
            left,right=list(b),list(a);left[axis]=right[axis]=mid
            todo.extend([(children[1],(tuple(right),b)),(children[0],(a,tuple(left)))])
        else:
            bounds=node["bounds"]
            require(type(bounds) is list and len(bounds)==6 and all(type(v) is int for v in bounds)
                    and bounds[4]>=0 and bounds[5]==1,"cached bound dimensions/types/completion")
            leaves.append((index,a,b,bounds))
    require(len(seen)==len(tree),"unreachable nodes")
    leaves.sort();values,compiler=backend(leaves);extrema=[];cases=0;vacuous=0
    for (index,_,_,stored),(value,n) in zip(leaves,values,strict=True):
        if n:
            require(value==stored[0] and n>=stored[4],"fresh/stored bound disagreement")
            extrema.append(value);cases+=n;terminal.append((index,"dp",value,n))
        else:
            require(stored[4]==0 and stored[0]==-(1<<63),"invalid vacuity metadata")
            vacuous+=1;terminal.append((index,"dp",None,0))
    digest=hashlib.sha256()
    for index,kind,value,n in sorted(terminal):
        digest.update(f"{index}:{kind}:{value}:{n}\n".encode())
    return dict(component="R6b-A",status="PASS",complete=True,coverage_checked=True,
                fresh_leaf_recomputation=True,cache_free=True,certificate_sha256=hashlib.sha256(raw).hexdigest(),
                tree_nodes=len(tree),node_kinds=dict(sorted(counts.items())),dp_leaves=len(leaves),
                vacuous_dp_leaves=vacuous,corner_bounds_checked=cases,largest_bound_numerator=max(extrema),
                leaf_result_sha256=digest.hexdigest(),unresolved=0,unsupported=0,
                compiler=compiler,backend_sha256=hashlib.sha256((HERE/"high_subtract.cpp").read_bytes()).hexdigest())
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--manifest",type=Path,default=HERE/"certificate-manifest.json")
    args=p.parse_args()
    try: print(json.dumps(check(args.manifest.resolve()),sort_keys=True));return 0
    except Exception as e: print(f"R6b A failed: {type(e).__name__}: {e}",file=sys.stderr);return 1
if __name__=="__main__": raise SystemExit(main())
