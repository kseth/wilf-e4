#!/usr/bin/env python3
"""Exact stdlib replay of every obstruction to monotone coordinate-line upgrade."""
from collections import Counter
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent

def add(x,i): return tuple(v+(j==i) for j,v in enumerate(x))
def le(x,y): return all(a<=b for a,b in zip(x,y))
def check(row):
    T=set(map(tuple,row['points']));m=len(T)
    assert m==row['m'] and (0,0,0) in T and m>=30
    assert max(map(sum,T))<=6
    assert all(tuple(v-(j==i) for j,v in enumerate(x)) in T for x in T for i in range(3) if x[i])
    corners=[x for x in product(range(8),repeat=3) if x not in T and all(tuple(v-(j==i) for j,v in enumerate(x)) in T for i in range(3) if x[i])]
    p=tuple(row['corner'])
    assert [x for x in corners if all(x)]==[p]
    P=sum(p)
    for i,j,k in [(0,1,2),(0,2,1),(1,2,0)]:
        mixed=[x for x in corners if x[i]>0 and x[j]>0 and x[k]==0]
        assert len(mixed)<=P-2
        assert sum(x[i]>=p[i] and x[j]>=p[j] for x in mixed)<=p[k]
    surfaces=[{x for x in T if add(x,i)not in T}for i in range(3)]
    q=[max(x[i]for x in T)for i in range(3)]
    for i,j,k in [(0,1,2),(0,2,1),(1,2,0)]:assert len(surfaces[i]&surfaces[j])<=2*(q[k]+1)
    E={x for x in T if all(add(x,i)in T for i in range(3))}
    assert len(E)+sum(sum(x[i]==0 for x in E)for i in range(3))<=m
    maxima=sorted(set.intersection(*surfaces))
    s=[sum(x[i]for x in T)for i in range(3)]
    mass=0;moment=[0]*3;up=[0]*3
    for i in range(3):
        for t in surfaces[i]:
            L=t[i]+1;mass+=L
            u=max((u for u in maxima if le(t,u)),key=lambda u:(sum(u),u))
            for j in range(3):moment[j]+=L*t[j];up[j]+=L*u[j]
    assert mass==3*m and moment==[4*v for v in s]
    r=[up[i]-4*s[i]for i in range(3)]
    assert min(r)>=0 and sum(r)==row['gain'] and sum(r)<m-2
    coeff=[F(4*s[i],3*m*q[i])for i in range(3)]
    assert sum(coeff)<=1
    longest=max(range(3),key=lambda i:q[i]);coeff[longest]+=1-sum(coeff)
    z=[coeff[i]*q[i]for i in range(3)]
    axisr=[3*m*z[i]-4*s[i]for i in range(3)]
    assert min(axisr)>=0 and sum(coeff)==1
    G=max(q)*(3*m-4*sum(F(s[i],q[i])for i in range(3)))
    assert sum(axisr)==G and G>=m+8
    canonical=min(tuple(sorted(tuple(x[i]for i in perm)for x in T))for perm in permutations(range(3)))
    return {'m':m,'G_minus_m':G-m,'canonical':canonical,'r':r,'axisr':axisr}

rows=[json.loads(l)for l in (HERE/'upgrade_failures.jsonl').read_text().splitlines()]
assert len(rows)==121
results=[check(row)for row in rows]
assert len({r['canonical']for r in results})==62
assert min(r['G_minus_m']for r in results)==8
out={'status':'passed','exact_fixtures':len(rows),'coordinate_permutation_orbits':62,
     'minimum_axis_gain_minus_m':'8','multiplicity_range':[min(r['m']for r in results),max(r['m']for r in results)],
     'scope':'All recorded line-upgrade failures; this fixture replay is not full enumeration.'}
(HERE/'fixture_verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
