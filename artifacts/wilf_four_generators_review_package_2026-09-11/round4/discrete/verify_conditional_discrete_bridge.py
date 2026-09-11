"""Independent exact checks of a conditional bound, not verification of its hypothesis."""
from itertools import product
from pathlib import Path
import json
R=23
# Independent brute-force rectangle endpoint pairs, rather than eliminating v.
Q={}
for a in range(R+1):
 for b in range(R+1):
  vals=[0]*(R+1)
  for u in range(a+1):
   for v in range(b+1):
    if u+v<=R:vals[u+v]=max(vals[u+v],(u+1)*(v+1))
  for h in range(1,R+1):vals[h]=max(vals[h],vals[h-1])
  Q[a,b]=vals
best=0;best_cs=[];count=0
for a,b,c in product(range(R+1),repeat=3):
 if a+b+c>R:continue
 count+=1;sz=(a+1)*(b+1)*(c+1)
 for base,cap1,cap2 in ((a,b,c),(b,a,c),(c,a,b)):
  sz+=sum(Q[cap1,cap2][R-t] for t in range(base+1,R+1))
 if sz>best:best=sz;best_cs=[(a,b,c)]
 elif sz==best:best_cs.append((a,b,c))
assert best==1836
assert count==2600
rows=[]
for r in range(1,31):
 T={(x,y,z) for x,y,z in product(range(r+1),repeat=3) if x+y<=r and x+z<=r and y*z==0}
 m=len(T);M=max(map(sum,T));sigma=sum(map(sum,T))
 assert m==(r+1)**2 and M==r
 assert 6*sigma==r*(r+1)*(4*r+5)
 assert 2*(3*sigma-2*m*M)==r*(r+1)
 if r>=2:assert 3*sigma>(2*m+1)*M
 rows.append(dict(R=r,m=m,M=M,sigma=sigma))
# Exact bound sqrt(137)<12 suffices for the strict degree limit 24.
assert 137<12**2
out=dict(status='All exact checks passed; continuous hypothesis remains unproved.',ordered_central_triples=count,degree_limit=R,max_cardinality=best,maximizers=best_cs,two_plane_family_checks=rows)
Path(__file__).with_name('conditional_discrete_bridge_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='two_plane_family_checks'}))
