#!/usr/bin/env python3
"""Read-only packet identity, closure, links, syntax, and independent coverage audit."""
from __future__ import annotations
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
PACKET=ROOT/"prelim"

def require(condition,reason):
    if not condition: raise RuntimeError(reason)

def module(name):
    path=PACKET/"code"/(name+".py")
    spec=importlib.util.spec_from_file_location(name,path)
    require(spec is not None and spec.loader is not None,"missing module")
    loaded=importlib.util.module_from_spec(spec);spec.loader.exec_module(loaded)
    return loaded

def main():
    require(len(sys.argv)==1 and not sys.flags.optimize,"unoptimized audit only")
    manifest=json.loads((PACKET/"manifest.json").read_bytes())
    paths={entry["path"] for entry in manifest["inputs"]}
    for entry in manifest["inputs"]:
        path=PACKET/entry["path"];raw=path.read_bytes()
        require(len(raw)==entry["bytes"] and hashlib.sha256(raw).hexdigest()==entry["sha256"],"changed input")
        if path.suffix==".py": ast.parse(raw)
        if path.suffix in (".py",".cpp",".md"):
            value=raw.decode()
            require(not re.search(r"Astra|artifacts/|round[1-9]/|\.{2}/",value),"nonstandalone reference")
            if path.suffix==".md":
                require(value.count(r"\[")==value.count(r"\]"),"display delimiters")
                require(value.count(r"\(")==value.count(r"\)"),"inline delimiters")
                for target in re.findall(r"\]\(([^)]+)\)",value):
                    if "://" in target: continue
                    base=target.split("#")[0]
                    resolved=(path.parent/base).resolve()
                    require(resolved.is_relative_to(PACKET),"local link escape")
                    require(resolved.exists() or base=="replay.json","broken local link")
    require(paths=={"README.md","proof.md","analytic-details.md","verification.md","verify.py"}
            |{str(p.relative_to(PACKET)) for directory in ("code","data")
              for p in (PACKET/directory).iterdir() if p.is_file()},"inventory mismatch")
    a,b=module("trees_integer"),module("trees_rational")
    counts={}
    for component in ("b2","b4","b6"):
        value=json.loads((PACKET/"data"/(component+".json")).read_bytes())
        left=a.coverage(value,component);right=b.coverage(value,component)
        require(left[0]==right[0] and sorted(left[1])==sorted(right[1]) and left[2]==right[2],
                "independent coverage disagreement")
        counts[component]=left[2]
    replay=PACKET/"replay.json";evidence="not yet present"
    if replay.exists():
        record=json.loads(replay.read_bytes())
        require(record["status"]=="PASS" and record["complete"] is True,"incomplete replay")
        require(record["inputs"]==manifest["inputs"]
                and record["manifest_sha256"]==hashlib.sha256((PACKET/"manifest.json").read_bytes()).hexdigest(),
                "evidence source drift")
        require(len(record["components"])==7 and all(c["complete"] is True and c["independent_agreement"] is True
                                                   for c in record["components"]),"incomplete component closure")
        evidence="complete source-matching PASS"
    print(json.dumps(dict(status="PASS",packet_inputs=len(paths),coverage=counts,replay=evidence),sort_keys=True))
    return 0

if __name__=="__main__": raise SystemExit(main())
