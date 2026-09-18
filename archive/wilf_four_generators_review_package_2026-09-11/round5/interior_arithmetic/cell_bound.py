"""Finite exact upper bound for compressed p=(2,1,1) ideals.
Extra unused levels are removed, so the objective is occupied compressed cells.
This is a geometric bound after the necessary arithmetic mixed-corner bound.
"""
from itertools import product,combinations
import json

def options_xy():
 cand=[(1,v) for v in range(2,6)]+[(u,v) for u in (2,3,4) for v in range(1,6) if (u,v)!=(2,1)]
 yield ()
 for q in cand:yield (q,)
 for q,r in combinations(cand,2):
  if (q[0]-r[0])*(q[1]-r[1])<0 and sum(t[0]>=2 for t in (q,r))<=1:yield(q,r)

def options_yz():
 cand=[(u,v) for u in range(1,6) for v in range(1,6) if (u,v)!=(1,1)]
 yield ()
 for q in cand:yield(q,)
 for q,r in combinations(cand,2):
  if (q[0]-r[0])*(q[1]-r[1])<0:yield(q,r)

def compressed(cs):
 # Corners include pure bounds; partition only at their occurring positive levels.
 levels=[sorted({0}|{q[i] for q in cs if q[i]}) for i in range(3)]
 # Minimal generators must form an antichain.
 for i,q in enumerate(cs):
  if any(i!=j and all(q[t]>=r[t] for t in range(3)) for j,r in enumerate(cs)):return
 z_index={z:i for i,z in enumerate(levels[2])}
 n=0
 for x,y in product(levels[0][:-1],levels[1][:-1]):
  zcap=min(q[2] for q in cs if q[0]<=x and q[1]<=y)
  n+=z_index[zcap]
 return n,levels,[]


best=(-1,None);n=0
for xy,xz,yz in product(tuple(options_xy()),tuple(options_xy()),tuple(options_yz())):
 cs=[(5,0,0),(0,6,0),(0,0,6),(2,1,1)]+[(u,v,0) for u,v in xy]+[(u,0,v) for u,v in xz]+[(0,u,v) for u,v in yz]
 out=compressed(cs)
 if out is None:continue
 n+=1
 if out[0]>best[0]:best=(out[0],dict(corners=cs,levels=out[1],points=out[2]))
print(json.dumps(dict(status='exact finite enumeration',candidates=n,max_cells=best[0],fixture=best[1]),indent=2))
