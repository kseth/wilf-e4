#!/usr/bin/env python3
"""R6b B: breadth-first coverage, rational outward clipping, disjoint-piece DP."""
from __future__ import annotations
import argparse
from collections import Counter, deque
from fractions import Fraction
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
def verify(b,message):
    if not b: raise ValueError(message)
def pairs(values):
    result={}
    for key,value in values:
        verify(key not in result,"duplicate object member");result[key]=value
    return result
def invalid_constant(s): raise ValueError("nonfinite constant")
def read_json(path):
    return json.loads(path.read_bytes(),object_pairs_hook=pairs,parse_constant=invalid_constant)
def endpoints(value):
    verify(type(value) is list and len(value)==2,"endpoint pair")
    converted=[]
    for endpoint in value:
        verify(type(endpoint) is list and len(endpoint)==3,"endpoint triple")
        verify(all(type(t) is int for t in endpoint),"endpoint integers")
        converted.append(tuple(endpoint))
    verify(all(converted[0][i]<=converted[1][i] for i in range(3)),"raw inversion")
    return tuple(converted)
def ceiling(r): return r.numerator//r.denominator+bool(r.numerator%r.denominator)
def enclose(region):
    left,right=map(list,region);scale=4096
    for unused in range(20):
        previous=tuple(left),tuple(right)
        left=[left[0],max(left[:2]),max(left)]
        right=[min(right),min(right[1:]),right[2]]
        if any(left[i]>right[i] for i in range(3)): return None
        verify(left[2]>3*scale,"nonpositive phase denominator")
        sum_bound=Fraction(9)+Fraction(28)/(Fraction(left[2],scale)-3)
        sum_bound=Fraction(ceiling(scale*sum_bound),scale)
        right[0]=min(right[0],ceiling(scale*(sum_bound-1)/2))
        right[1]=min(right[1],ceiling(scale*(sum_bound-1-Fraction(left[0],scale))))
        upper_sum=min(sum_bound,1+Fraction(right[0]+right[1],scale))
        right[2]=min(right[2],ceiling(scale*(42+37*upper_sum)/5))
        if previous==(tuple(left),tuple(right)): break
    if any(left[i]>right[i] for i in range(3)): return None
    return tuple(left),tuple(right)
def certificate(path):
    descriptor=read_json(path)
    verify(type(descriptor) is dict and set(descriptor)==
           {"schema_version","component","certificate_format","certificate","constants"},"manifest fields")
    verify(type(descriptor["schema_version"]) is int and descriptor["schema_version"]==1
           and descriptor["component"]=="B6-high-FV"
           and descriptor["certificate_format"]=="wilf-b6-high-interval-tree-v1","manifest format")
    identity=descriptor["certificate"]
    verify(type(identity) is dict and set(identity)=={"path","sha256","bytes"},"identity fields")
    verify(type(identity["path"]) is str and not Path(identity["path"]).is_absolute(),"relative data path")
    source=(ROOT/identity["path"]).resolve();verify(source.is_relative_to(ROOT),"path outside repository")
    verify(type(identity["bytes"]) is int and identity["bytes"]>0,"size type")
    verify(type(identity["sha256"]) is str and re.fullmatch("[0-9a-f]{64}",identity["sha256"]),"hash type")
    raw=source.read_bytes();verify(len(raw)==identity["bytes"],"wrong byte count")
    verify(hashlib.sha256(raw).hexdigest()==identity["sha256"],"wrong certificate hash")
    constants=descriptor["constants"]
    verify(type(constants) is dict and set(constants)=={"scale","root"}
           and type(constants["scale"]) is int and constants["scale"]==4096,"scale metadata")
    expected=((4096,4096,28672),(319488,319488,319488))
    verify(endpoints(constants["root"])==expected,"manifest root")
    data=read_json(source)
    verify(type(data) is dict and set(data)==
           {"scope","scale","initial","complete","tree","nodes","unresolved","stack","seconds","dp_calls","corner_cases"},
           "tree header fields")
    verify(type(data["scope"]) is str and data["scope"].startswith("conditional attempted certificate generic p"),
           "scope metadata")
    verify(type(data["scale"]) is int and data["scale"]==4096 and endpoints(data["initial"])==expected,
           "tree root metadata")
    verify(data["complete"] is True and data["stack"]==[] and data["unresolved"]==[],"unfinished tree")
    verify(type(data["seconds"]) in (int,float) and math.isfinite(data["seconds"]) and data["seconds"]>=0,
           "timing metadata")
    verify(all(type(data[k]) is int and data[k]>=0 for k in ("nodes","dp_calls","corner_cases")),"header counters")
    verify(type(data["tree"]) is list and len(data["tree"])==data["nodes"]>0,"node array")
    return data,expected,raw
def compute(leaves):
    compiler=shutil.which("c++");verify(compiler is not None,"C++17 unavailable")
    version=subprocess.run([compiler,"--version"],capture_output=True,text=True,check=True).stdout
    with tempfile.TemporaryDirectory(prefix="wilf-r6b-b-") as temp:
        binary=str(Path(temp)/"evaluate")
        command=[compiler,"-std=c++17","-O3","-Wall","-Wextra","-pedantic",str(HERE/"high_disjoint.cpp"),"-o",binary]
        result=subprocess.run(command,capture_output=True,text=True)
        verify(result.returncode==0 and not result.stderr,"compiler diagnostic")
        requests=[]
        for _,(a,b),_ in leaves: requests.append(" ".join(str(t) for t in [4096,*a,*b]))
        process=subprocess.run([binary],input="\n".join(requests)+"\n",capture_output=True,text=True)
        verify(process.returncode==0 and not process.stderr,"disjoint worker failed: "+process.stderr)
        rows=process.stdout.splitlines();verify(len(rows)==len(leaves),"missing leaf responses")
        output=[]
        for row in rows:
            words=row.split()
            verify(len(words)==2 and all(re.fullmatch(r"-?\d+",w) for w in words),"bound response dimensions")
            value,count=map(int,words)
            verify(count>=0 and (count or value==0),"empty corner response")
            verify(count==0 or 10*value<=29*4096,"target predicate")
            output.append((value,count))
    return output,dict(version=version,command=command)
def check(path):
    verify(sys.flags.optimize==0,"optimized Python is unsupported")
    data,root,raw=certificate(path);nodes=data["tree"];queue=deque([(0,root)])
    visited=set();counts=Counter();leaves=[];results=[]
    allowed={"split":{"box","kind","axis","mid","children"},
             "dp":{"box","kind","bounds"},"empty":{"box","kind"}}
    while queue:
        identifier,region=queue.popleft()
        verify(type(identifier) is int and 0<=identifier<len(nodes),"node address")
        verify(identifier not in visited,"duplicate node visit");visited.add(identifier)
        node=nodes[identifier]
        verify(type(node) is dict and type(node.get("kind")) is str,"node object")
        kind=node["kind"];verify(kind in allowed and set(node)==allowed[kind],"node fields")
        verify(endpoints(node["box"])==region,"incorrect derived child")
        counts[kind]+=1;bounded=enclose(region)
        if bounded is None:
            verify(kind=="empty","unmarked empty enclosure");results.append((identifier,"empty",None,0));continue
        verify(kind!="empty","unsound empty leaf")
        if kind=="dp":
            cached=node["bounds"]
            verify(type(cached) is list and len(cached)==6 and all(type(t) is int for t in cached)
                   and cached[4]>=0 and cached[5]==1,"cached output dimensions or completeness")
            leaves.append((identifier,bounded,cached));continue
        dimension=node["axis"];cut=node["mid"];children=node["children"]
        low,high=bounded
        verify(type(dimension) is int and dimension in (0,1,2)
               and type(cut) is int and low[dimension]<cut<high[dimension],"split wall")
        verify(type(children) is list and len(children)==2 and all(type(t) is int for t in children)
               and children[0]!=children[1],"child addresses")
        upper_left=list(high);lower_right=list(low);upper_left[dimension]=lower_right[dimension]=cut
        queue.append((children[0],(low,tuple(upper_left))))
        queue.append((children[1],(tuple(lower_right),high)))
    verify(len(visited)==len(nodes),"orphan nodes")
    leaves.sort();calculated,compiler=compute(leaves);corner_total=0;empty_dp=0;maximum=None
    for (identifier,_,cached),(value,count) in zip(leaves,calculated,strict=True):
        if count==0:
            verify(cached[4]==0 and cached[0]==-(1<<63),"cached empty-case mismatch")
            empty_dp+=1;results.append((identifier,"dp",None,0))
        else:
            verify(value==cached[0] and count>=cached[4],"recomputed bound mismatch")
            corner_total+=count;maximum=value if maximum is None else max(value,maximum)
            results.append((identifier,"dp",value,count))
    digest=hashlib.sha256()
    for identifier,kind,value,count in sorted(results):
        digest.update(f"{identifier}:{kind}:{value}:{count}\n".encode())
    return dict(component="R6b-B",status="PASS",complete=True,coverage_checked=True,
                fresh_leaf_recomputation=True,cache_free=True,certificate_sha256=hashlib.sha256(raw).hexdigest(),
                tree_nodes=len(nodes),node_kinds=dict(sorted(counts.items())),dp_leaves=len(leaves),
                vacuous_dp_leaves=empty_dp,corner_bounds_checked=corner_total,largest_bound_numerator=maximum,
                leaf_result_sha256=digest.hexdigest(),unresolved=0,unsupported=0,compiler=compiler,
                backend_sha256=hashlib.sha256((HERE/"high_disjoint.cpp").read_bytes()).hexdigest())
def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest",type=Path,default=HERE/"certificate-manifest.json")
    args=parser.parse_args()
    try: print(json.dumps(check(args.manifest.resolve()),sort_keys=True));return 0
    except Exception as e: print(f"R6b B failed: {type(e).__name__}: {e}",file=sys.stderr);return 1
if __name__=="__main__": raise SystemExit(main())
