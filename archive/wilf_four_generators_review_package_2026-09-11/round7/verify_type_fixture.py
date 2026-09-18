"""Independent direct-membership verification of the type-reduction obstruction."""
import json
from pathlib import Path

gens=(155,1552,1647,1651)
m=gens[0]
# The precomputed M is used only as an explicit finite interval endpoint. A block
# of m consecutive members will independently establish the conductor.
limit=18133
member=[False]*(limit+1);member[0]=True
for z in range(1,limit+1):
 member[z]=any(z>=a and member[z-a] for a in gens)
assert all(member[z] for z in range(limit-m+1,limit+1))
F=max(z for z in range(limit+1) if not member[z]);c=F+1
# The terminal m-block makes every integer after limit a member, by induction.
assert all(member[z] for z in range(c,limit+1))
def sin(z):return z>=c or z>=0 and member[z]
ap=[]
for r in range(m):ap.append(next(z for z in range(r,limit+1,m) if member[z]))
assert max(ap)==limit
assert all(not any(sin(a-b) for b in gens[:j]) for j,a in enumerate(gens[1:],1))
pf=[z for z in range(1,c) if not member[z] and all(sin(z+a) for a in gens)]
gaps=[z for z in range(1,c) if not member[z]]
g=len(gaps);n=sum(member[:c]);t=len(pf)
lam=[sum(member[:f+1]) for f in pf]
nu={z:sum(sin(f-z) for f in pf) for z in gaps}
theta=sum(v-1 for v in nu.values())
xi=sum((w//m)*(nu[w-m]-1) for w in ap[1:])
W=4*n-c;target=sum(lam[:t-3])
assert (c,g,n,t,W,theta,xi,target)==(17979,11114,6865,13,9481,65609,22130,56287)
# Independently enumerate all non-multiplicity factorizations below M by loops.
reps={}
for x in range(limit//gens[1]+1):
 for y in range((limit-x*gens[1])//gens[2]+1):
  for z in range((limit-x*gens[1]-y*gens[2])//gens[3]+1):
   value=x*gens[1]+y*gens[2]+z*gens[3]
   if ap[value%m]==value:
    key=(x,y,z)
    if value not in reps or key<reps[value]:reps[value]=key
assert len(reps)==m
T=set(reps.values());corners=set()
for x in T:
 for i in range(3):
  p=tuple(x[j]+(j==i) for j in range(3))
  if p not in T and all(tuple(p[j]-(j==k) for j in range(3)) in T for k in range(3) if p[k]):corners.add(p)
interior=sorted(p for p in corners if min(p)>0)
assert interior==[(1,7,4)]
latest_gaps=gaps[-3:]
assert pf[-3:]==latest_gaps
penalty=sum(n-l for l in lam[-3:])
assert penalty==2*F-pf[-2]-pf[-3]-3==159
assert W-penalty==theta-target==9322
out={'status':'passed','generators':gens,'conductor':c,'genus':g,'n':n,'type':t,'wilf':W,'pseudo_frobenius':pf,'lambdas':lam,'Theta':theta,'Xi':xi,'required_redundancy':target,'Xi_shortfall':target-xi,'stronger_conjecture_margin':theta-target,'tail_penalty':penalty,'full_corners':interior,'independent_method':'Integer membership recurrence and direct incidence counting; separate factorization loops.'}
path=Path(__file__).with_name('type_fixture_independent_verification.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
