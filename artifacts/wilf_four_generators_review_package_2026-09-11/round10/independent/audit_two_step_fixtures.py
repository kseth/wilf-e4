#!/usr/bin/env python3
"""Independent direct-membership two-step check of the complete cheap-exception set."""
import json
from pathlib import Path
from fractions import Fraction
import hashlib

root=Path(__file__).resolve().parents[2]
paths=[root/'round10/line_upgrade/cheap_bound_exceptions_strong.jsonl',root/'round10/ablation/cheap_bound_exceptions_strong.jsonl']
sets=[]
for path in paths:
    rows=[json.loads(line) for line in path.read_text().splitlines()]
    assert len(rows)==388
    shapes={tuple(sorted(tuple(t) for t in row['points'])) for row in rows}
    assert len(shapes)==388
    sets.append(shapes)
assert sets[0]==sets[1]
minimum=10**9
mins=[]
for shape in sorted(sets[0]):
    T=set(shape);m=len(T);s=[sum(t[i] for t in T) for i in range(3)]
    q=[max(t[i] for t in T) for i in range(3)]
    G=max(q)*(3*m-4*sum((Fraction(s[i],q[i]) for i in range(3)),Fraction(0)))
    maxima=set();r=[0,0,0];U2=0
    for t in T:
        tops=[]
        for i in range(3):
            u=list(t);u[i]+=1
            if tuple(u) not in T:tops.append(i)
        if len(tops)==3:maxima.add(t)
        candidates={t}
        for j in range(3):
            u=list(t);u[j]+=1
            if tuple(u) in T:candidates.add(tuple(u))
            for k in range(j,3):
                v=u.copy();v[k]+=1
                if tuple(v) in T:candidates.add(tuple(v))
        v=max(candidates,key=lambda v:(sum(v),v))
        for i in tops:
            L=t[i]+1
            U2+=L*(sum(v)-sum(t))
            for j in range(3):r[j]+=L*(v[j]-t[j])
    C=3*m-sum(sum(t)+3 for t in maxima)
    assert C<m and G<m
    assert U2>=m and U2==sum(r) and min(r)>=0
    minimum=min(minimum,U2-m)
result={'status':'passed','fixtures':388,'no_erosion_fixture_set_equal_to_original':True,'maximal_dominator_search_used':False,'direct_neighbor_distances_checked':[0,1,2],'minimum_U2_minus_m':minimum,'input_sha256':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
print(json.dumps(result,indent=2))
