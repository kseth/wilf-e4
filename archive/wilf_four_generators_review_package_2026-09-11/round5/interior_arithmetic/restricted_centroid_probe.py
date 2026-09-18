from itertools import combinations,product
from random import Random
from scipy.optimize import linprog
import json

def profiles(l1,l2,kind):
 out=[]
 for size in range(3):
  for xs in combinations(range(1,l1),size):
   if kind=='xy' and sum(x>=2 for x in xs)>1:continue
   for ys in combinations(range(1,l2),size):
    pairs=tuple(zip(xs,reversed(ys)))
    if kind=='xy' and any(x<=2 and y<=1 for x,y in pairs):continue
    if kind=='yz' and (1,1) in pairs:continue
    out.append(pairs)
 return out
xy=profiles(5,6,'xy');yz=profiles(6,6,'yz')
rng=Random(42945);best=None;count=0
for it in range(1000):
 cs=[(5,0,0),(0,6,0),(0,0,6),(2,1,1)]
 cs +=[(x,y,0) for x,y in rng.choice(xy)]+[(x,0,z) for x,z in rng.choice(xy)]+[(0,y,z) for y,z in rng.choice(yz)]
 # Stretch coordinate intervals, preserving the actual p211 coordinates.
 lev=[sorted(set(q[i] for q in cs)) for i in range(3)];maps=[]
 for i,ls in enumerate(lev):
  mp={0:0}
  for l in ls[1:]:mp[l]=l if l<= (2 if i==0 else 1) else max(mp.values())+rng.randrange(1,4)
  maps.append(mp)
 cs=[tuple(maps[i][q[i]] for i in range(3)) for q in cs]
 h=tuple(max(q[i] for q in cs) for i in range(3))
 T=[p for p in product(*(range(v) for v in h)) if not any(all(p[i]>=q[i] for i in range(3)) for q in cs)]
 m=len(T)
 if m<30 or m>269:continue
 Ts=set(T);Z=[p for p in T if all(tuple(p[j]+(i==j) for j in range(3)) not in Ts for i in range(3))]
 sums=[sum(p[i] for p in T) for i in range(3)]
 opt=linprog([-3*s for s in sums]+[2*m],A_ub=[list(p)+[-1] for p in Z],b_ub=[0]*len(Z),bounds=[(1,None)]*3+[(None,None)],method='highs')
 count+=1
 if opt.success:
  delta=opt.fun
  if best is None or delta<best['delta']:best=dict(delta=delta,m=m,corners=cs,Z=Z,weights=opt.x.tolist(),D=opt.fun,sums=sums)
  if delta< -1e-7:break
print(json.dumps(dict(count=count,best=best),indent=2))
