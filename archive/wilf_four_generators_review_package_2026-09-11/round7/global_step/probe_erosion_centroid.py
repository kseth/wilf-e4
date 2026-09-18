import itertools,json,random,sys
from fractions import Fraction
from scipy.optimize import linprog
from pathlib import Path

def build(c,p):
 A,B,C=c
 return {(x,y,z) for x in range(min(A,B)+1) for y in range(min(A-x,C)+1) for z in range(min(B-x,C-y)+1) if any(t<v for t,v in zip((x,y,z),p))}
def records(T):
 F=[{x for x in T if tuple(x[j]+(i==j) for j in range(3)) not in T} for i in range(3)]
 A=T-set.union(*F)
 E=len(A)+sum(len({tuple(x[j] for j in range(3) if j!=i) for x in A}) for i in range(3))-len(T)
 return E,F[0]&F[1]&F[2]

rng=random.Random(98756);count=0;best=None
for it in range(int(sys.argv[1]) if len(sys.argv)>1 else 10000):
 c=tuple(rng.randrange(5,35) for _ in range(3))
 p=tuple(rng.randrange(1,1+min(c)//2) for _ in range(3))
 if p[0]+p[1]>c[0]+1 or p[0]+p[2]>c[1]+1 or p[1]+p[2]>c[2]+1:continue
 T=build(c,p);m=len(T)
 if m<30:continue
 E,Z=records(T)
 if E>0:continue
 count+=1;s=[sum(x[i] for x in T) for i in range(3)]
 opt=linprog([m-6*v for v in s]+[4*m],A_ub=[list(x)+[-1] for x in Z],b_ub=[0]*len(Z),A_eq=[[1,1,1,0]],b_eq=[1],bounds=[(0,None)]*4,method='highs')
 if not opt.success:raise RuntimeError(opt.message)
 if best is None or opt.fun<best['objective']:
  best=dict(pair_caps=c,corner=p,m=m,E=E,objective=opt.fun,weights=opt.x.tolist(),sums=s)
  print(json.dumps(dict(iteration=it,valid=count,best=best)),flush=True)
 if opt.fun < -1e-7:break
out=dict(scope='bounded diagnostic',attempts=it+1,valid=count,best=best)
Path(__file__).with_name('erosion_centroid_probe.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
