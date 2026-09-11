#!/usr/bin/env python3
"""Exact local two-step verification of the 388 strong cheap-bound exceptions."""
from fractions import Fraction
from itertools import combinations_with_replacement
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
rows=[json.loads(l)for l in (HERE/'cheap_bound_exceptions_strong.jsonl').read_text().splitlines()]
assert len(rows)==388
margins=[]
for row in rows:
 T=set(map(tuple,row['points']));m=len(T);assert m==row['m']
 assert all(tuple(v-(i==j)for j,v in enumerate(x))in T for x in T for i in range(3)if x[i])
 F=[{x for x in T if tuple(v+(i==j)for j,v in enumerate(x))not in T}for i in range(3)]
 K=set.intersection(*F)
 cheap=3*m-sum(sum(u)+3 for u in K)
 assert cheap<m
 G=Fraction(row['axis_numerator'],row['axis_denominator'])
 assert G<m
 gain=0;moment=[0]*3;up=[0]*3;mass=0
 for i in range(3):
  for t in F[i]:
   options=[tuple(v+(j==k)+(l==k)for k,v in enumerate(t))for j,l in combinations_with_replacement(range(3),2)]
   options+=[tuple(v+(j==k)for k,v in enumerate(t))for j in range(3)]+[t]
   u=next(u for u in options if u in T)
   L=t[i]+1;mass+=L;gain+=L*(sum(u)-sum(t))
   for j in range(3):moment[j]+=L*t[j];up[j]+=L*u[j]
 assert mass==3*m
 assert moment==[4*sum(x[j]for x in T)for j in range(3)]
 assert min(up[j]-moment[j]for j in range(3))>=0
 assert gain>=m
 margins.append(gain-m)
out={'status':'passed','exact_fixtures':388,'minimum_two_step_gain_minus_m':min(margins),
     'maximum_two_step_gain_minus_m':max(margins),
     'scope':'Local constructive verification of all recorded failures of cheap bound plus axis witness; combined with complete enumeration implies local two-step or axis suffices on the original residual class.'}
(HERE/'two_step_exception_verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
