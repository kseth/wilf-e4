#!/usr/bin/env python3
"""Exact residue and interval checks on two previously certified genuine ideals."""
from itertools import combinations
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]

def main():
 records=[]
 for source in sorted((ROOT/'round5/continuous_apery_probe').glob('*fixture_exact.json')):
  d=json.loads(source.read_text());m,*a=d['generators']
  T={tuple(x['exponent']) for x in d['apery_by_residue']}
  assert len(T)==m
  reps={sum(ai*xi for ai,xi in zip(a,x))%m:x for x in T}
  assert len(reps)==m
  surfaces=[]
  for i,j in combinations(range(3),2):
   k=3-i-j;n=1+max(x[k] for x in T)
   Fi={x for x in T if tuple(x[t]+int(t==i) for t in range(3)) not in T}
   Fj={x for x in T if tuple(x[t]+int(t==j) for t in range(3)) not in T}
   C=set()
   for x in Fi:
    q=tuple(x[t]+int(t==i) for t in range(3))
    if q[j]>0 and tuple(q[t]-int(t==j) for t in range(3)) in T:C.add(q)
   assert len(C)==len(Fi&Fj)-n
   images={};runs={}
   for q in sorted(C):
    rep=reps[sum(ai*xi for ai,xi in zip(a,q))%m]
    assert rep[i]==rep[j]==0
    assert rep[k] not in images;images[rep[k]]=q
    runs.setdefault((q[i],q[j]),[]).append((q[k],rep[k]))
   assert len(C)<=n
   interior=d['preferred_lex_interior_corners']
   if interior:
    for r in runs.values():
     r.sort()
     for (t,b),(tp,bp) in zip(r,r[1:]):
      assert tp==t+1 and bp==b+1
    p=tuple(interior[0]);r=runs[p[i],p[j]]
    assert min(r)==(p[k],0)
   surfaces.append(dict(pair=[i,j],axis=k,axis_length=n,number_of_slice_maxima=len(Fi&Fj),mixed_excluded_count=len(C),runs=[dict(planar_corner=list(q),slice_to_axis=r) for q,r in sorted(runs.items())]))
  records.append(dict(generators=d['generators'],surfaces=surfaces))
 out=dict(status='PASS',scope='Exact finite fixture validation of direct residue proof and nonwrapping run packing; no unrestricted search',records=records)
 Path(__file__).with_name('corner_run_packing_checks.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(dict(status='PASS',fixtures=len(records),surfaces=sum(len(r['surfaces']) for r in records))))
if __name__=='__main__':main()
