"""Exact auxiliary-inequality counterexamples. Not Wilf counterexamples."""
from fractions import Fraction as F
from itertools import product
import json

t=F(1,10)
lam=1-2*t
vu=F(1,4)
iu=F(7,32)
mu=F(3,2)
vr=lam**3*vu
ir=lam**3*(3*t*vu+lam*iu)
vk=vu-vr
ik=iu-ir
mk=1+t
rho=ik/(vk*mk)
assert (vk,ik,mk,rho)==(F(61,500),F(363,4000),F(11,10),F(165,244))
assert rho-F(2,3)==F(7,732)
terms=(3*iu-2*mu*vu,2*(mu-mk)*vu,-(3*ir-2*mk*vr))
assert terms==(F(-3,32),F(1,5),F(-64,625))
assert sum(terms)==3*ik-2*mk*vk==F(77,20000)

T={p for p in product(range(30),repeat=3)
   if max(p[0]+p[1],p[0]+p[2],p[1]+p[2])<=29 and min(p)<=3}
total=len(T)
sigma=sum(map(sum,T))
height=max(map(sum,T))
assert (total,sigma,height)==(4246,92724,32)
corners=[]
for p in product(range(31),repeat=3):
    if p in T:
        continue
    predecessors=[]
    for i in range(3):
        if p[i]:
            q=list(p);q[i]-=1
            predecessors.append(tuple(q))
    if predecessors and all(q in T for q in predecessors):
        corners.append(p)
full=[p for p in corners if min(p)>0]
mixed=[p for p in corners if sum(x>0 for x in p)==2]
pure=[p for p in corners if sum(x>0 for x in p)==1]
assert full==[(4,4,4)]
assert len(mixed)==87 and len(pure)==3 and len(corners)==91
cell_i=F(sigma)+F(3,2)*total
cell_m=height+3
cell_rho=cell_i/(total*cell_m)
assert cell_i==99093 and cell_rho==F(99093,148610)
assert cell_rho-F(2,3)==F(59,445830)>0
print(json.dumps({
    'status':'exact auxiliary geometric counterexamples verified',
    'polytope_normalized_mean':str(rho),
    'polytope_cut_identity_terms':list(map(str,terms)),
    'finite_point_count':total,
    'finite_coordinate_sum':sigma,
    'finite_cell_height':cell_m,
    'finite_cell_normalized_mean':str(cell_rho),
    'finite_full_support_corners':full,
    'finite_mixed_corners':len(mixed),
    'finite_pure_corners':len(pure)
},indent=2))
