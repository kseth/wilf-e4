"""Exact checks for the unequal exposed-vertex example; standard library only."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
Z=((6,1,1),(1,5,1),(1,1,4))
T=set().union(*(set(product(*(range(t+1) for t in z))) for z in Z))
m=len(T);sums=tuple(sum(x[i] for x in T) for i in range(3))
assert m==56 and sums==(98,76,58)
for x in T:
 for i in range(3):
  if x[i]:
   y=list(x);y[i]-=1;assert tuple(y) in T
maximal={x for x in T if all(tuple(x[j]+(j==i) for j in range(3)) not in T for i in range(3))}
assert maximal==set(Z)
corners=set()
for x in product(range(8),range(7),range(6)):
 if x in T:continue
 if all(not x[i] or tuple(x[j]-(j==i) for j in range(3)) in T for i in range(3)):corners.add(x)
expected={(7,0,0),(0,6,0),(0,0,5),(2,2,0),(2,0,2),(0,2,2)}
assert corners==expected
assert all(any(t==0 for t in x) for x in corners)
weights=(F(1),F(5,4),F(5,3))
values=[sum(w*t for w,t in zip(weights,z)) for z in Z]
assert len(set(values))==1
M=max(sum(w*t for w,t in zip(weights,x)) for x in T)
D=3*m*M-4*sum(w*t for w,t in zip(weights,sums))
assert D==F(1018,3)
D_unit=3*m*max(map(sum,T))-4*sum(sums)
assert D_unit==416 and D_unit>D
# Coefficient identities proving the minimization, not a parameter grid.
coef_H=3*m
coef_b=3*m-4*sums[1]
coef_c=3*m-4*sums[2]
constant=3*m-4*sums[0]
assert (coef_H,coef_b,coef_c,constant)==(168,-136,-64,-224)
slope=F(coef_H)+F(coef_b,4)+F(coef_c,3)
assert slope==F(338,3)>0
assert 5*slope+constant==D
out={'status':'PASS','cardinality':m,'coordinate_sums':sums,'minimal_excluded':sorted(corners),'unique_ordered_minimizer':[str(w) for w in weights],'minimum_D':str(D),'unit_D':D_unit,'fixed_H_slope':str(slope),'scope':'Obstruction to naive equal-weight minimization, not a counterexample to the weighted target; no Apéry realization asserted.'}
Path(__file__).with_name('unequal_exposed_vertex_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
