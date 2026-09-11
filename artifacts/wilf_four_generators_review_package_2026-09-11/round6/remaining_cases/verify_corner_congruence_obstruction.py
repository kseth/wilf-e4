#!/usr/bin/env python3
"""Exact reproduction of the scaled geometric obstruction and necessary residue checks."""
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

L=6
T={(x,y,z) for x in range(30) for y in range(30-x)
   for z in range(min(29-x,29-y)+1) if min(x,y,z)<=3}
cs=set()
for x in T:
 for j in range(3):
  q=tuple(x[i]+(i==j) for i in range(3))
  if q in T:continue
  if all(tuple(q[i]-(i==k) for i in range(3)) in T for k in range(3) if q[k]):cs.add(q)
expected={(30,0,0),(0,30,0),(0,0,30),(4,4,4)}
for j,k in [(0,1),(0,2),(1,2)]:
 for a in range(1,30):
  q=[0,0,0];q[j]=a;q[k]=30-a;expected.add(tuple(q))
assert cs==expected
m=len(T);H=max(map(sum,T));sigma=sum(map(sum,T))
mu=Fraction(2*sigma+3*m,2*m*(H+3))
assert (m,H,sigma)==(4246,32,92724)
assert mu==Fraction(99093,148610)>Fraction(2,3)
scaled_cs={tuple(L*v for v in q) for q in cs}
p=(24,24,24);m2=m*L**3;H2=L*H+3*(L-1)
sigma2=L**4*sigma+3*m*L**3*(L-1)//2
assert Fraction(2*sigma2+3*m2,2*m2*(H2+3))==mu
planes=[]
for k in range(3):
 ij=[i for i in range(3) if i!=k]
 mixed=[q for q in scaled_cs if q[k]==0 and all(q[i]>0 for i in ij)]
 upper=[q for q in mixed if all(q[i]>=p[i] for i in ij)]
 assert len(mixed)==29<=sum(p)-2
 assert len(upper)==23<=p[k]
 classes=Counter(tuple(q[i]%2 for i in ij) for q in upper)
 assert max(classes.values())==23>p[k]//2
 planes.append(dict(omitted_axis=k,mixed_count=len(mixed),dominating_count=len(upper),
                    maximum_mod2_class=max(classes.values()),capacity_if_axis_weight_odd=p[k]//2))
B={(0,0,0),(1,0,0),(0,1,0),(0,0,1)}
A={x for x in T if all(tuple(x[i]+b[i] for i in range(3)) in T for b in B)}
AmB={tuple(x[i]-b[i] for i in range(3)) for x in A for b in B}
assert (len(A),len(AmB))==(3241,4546)
assert len(AmB)>len(T)
result=dict(status='PASS',scope='An auxiliary geometric counterexample, not a Wilf counterexample',
 base=dict(m=m,maximum=H,moment=sigma),scale=L,
 scaled=dict(m=m2,maximum=H2,moment=sigma2,full_corner=p,
             normalized_continuous_mean=str(mu),centroid_failure_numerator=6*sigma2-4*m2*H2-3*m2),
 planes=planes,excluded_by_prime2_capacity=True,
 independent_erosion=dict(A=len(A)*L**3,A_minus_B=len(AmB)*L**3,T=m2))
Path(__file__).with_name('corner_congruence_obstruction_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
