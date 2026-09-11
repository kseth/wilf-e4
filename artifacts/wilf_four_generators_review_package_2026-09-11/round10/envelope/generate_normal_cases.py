"""Exact universal epigraph-vertex directions for degree-six ideals."""
from itertools import combinations,product
from math import gcd
from functools import reduce
import json

POINTS=[q for q in product(range(7),repeat=3) if sum(q)<=6]
PS=[(1,1,3),(1,2,2),(1,1,4),(1,2,3),(2,2,2),(1,1,5),(1,2,4),(1,3,3),(2,2,3)]

def normals():
 out={(1,1,1)}
 for p,q in combinations(POINTS,2):
  d=[p[i]-q[i] for i in range(3)]
  for k in range(3):
   if not d[k]:continue
   t=-(sum(d)-d[k]);den=d[k]
   if den<0:t=-t;den=-den
   if t<den:continue
   b=[den]*3;b[k]=t;g=reduce(gcd,b);out.add(tuple(x//g for x in b))
 for p,q,r in combinations(POINTS,3):
  u=[q[i]-p[i] for i in range(3)];v=[r[i]-p[i] for i in range(3)]
  b=[u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]]
  if max(b)<0:b=[-x for x in b]
  if min(b)<=0:continue
  g=reduce(gcd,b);out.add(tuple(x//g for x in b))
 return sorted(out)

def cases():
 out=[]
 for p in PS:
  for n in normals():
   u=min(n);hmin=sum(a*b for a,b in zip(p,n))-u
   if hmin>=7*u:continue
   allowed=[sum(a*b for a,b in zip(q,n)) for q in POINTS if not all(a>=b for a,b in zip(q,p))]
   for h in sorted(set(allowed)):
    if hmin<=h<7*u and sum(t<=h for t in allowed)>=30:out.append((p,n,h))
 return out

if __name__=='__main__':
 ns=normals();cs=cases()
 assert len(ns)==2425 and len(cs)==44281
 print(json.dumps({'normals':len(ns),'coordinate_orbits':len({tuple(sorted(n)) for n in ns}),'cases':len(cs),'max_coordinate':max(max(n) for n in ns)}))
 open('round10/envelope/universal_normals.json','w').write(json.dumps(ns))
 open('round10/envelope/universal_low_height_tests.json','w').write(json.dumps(cs))
