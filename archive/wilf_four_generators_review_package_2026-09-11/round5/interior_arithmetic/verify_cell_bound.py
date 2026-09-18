"""Independent integer-bitset verification of the p=(2,1,1) cell bound.
No imports from the discovery program. Enumerates all allowable plane profiles,
then counts included cells only at occurring coordinate cuts.
"""
from itertools import combinations, product
from functools import lru_cache
import json

points=list(product(range(5),range(6),range(6)))
full=(1<<len(points))-1

def upper_mask(corners):
 return sum(1<<i for i,p in enumerate(points) if any(all(a>=b for a,b in zip(p,q)) for q in corners))

def profiles(first_limit,second_limit,kind):
 # Increasing first coordinates and decreasing second coordinates specify all
 # planar antichains uniquely; zero, one, and two corners are the only cases.
 out=[]
 for size in range(3):
  for xs in combinations(range(1,first_limit),size):
   if kind=='xy' and sum(x>=2 for x in xs)>1:continue
   for ys in combinations(range(1,second_limit),size):
    pairs=tuple(zip(xs,reversed(ys)))
    if kind=='xy' and any(x<=2 and y<=1 for x,y in pairs):continue
    if kind=='yz' and (1,1) in pairs:continue
    out.append(pairs)
 return out

xy=profiles(5,6,'xy');yz=profiles(6,6,'yz')
assert (len(xy),len(yz))==(45,125)

@lru_cache(None)
def sample_mask(xs,ys,zs):
 return sum(1<<((x*6+y)*6+z) for x,y,z in product(xs,ys,zs))

def prep(options,plane):
 out=[]
 for pairs in options:
  if plane==0:corners=tuple((x,y,0) for x,y in pairs)
  elif plane==1:corners=tuple((x,0,y) for x,y in pairs)
  else:corners=tuple((0,x,y) for x,y in pairs)
  coords=tuple(frozenset(q[i] for q in corners) for i in range(3))
  out.append((corners,coords,upper_mask(corners)))
 return out

base=upper_mask(((2,1,1),));best=0;count=0;witness=None;hist={}
for X,Y,Z in product(prep(xy,0),prep(xy,1),prep(yz,2)):
 cuts=tuple(tuple(sorted({0,2 if i==0 else 1}|X[1][i]|Y[1][i]|Z[1][i])) for i in range(3))
 occupied=full & ~(base|X[2]|Y[2]|Z[2])
 n=(occupied & sample_mask(*cuts)).bit_count()
 hist[n]=hist.get(n,0)+1;count+=1
 if n>best:
  best=n;witness=dict(corners=X[0]+Y[0]+Z[0]+((2,1,1),(5,0,0),(0,6,0),(0,0,6)),cuts=cuts)
assert count==253125 and best==68
result=dict(status='independent exact certificate passed',templates=count,max_cells=best,wilf_cutoff=4*best-2,histogram=hist,witness=witness)
print(json.dumps(result,indent=2,sort_keys=True))
