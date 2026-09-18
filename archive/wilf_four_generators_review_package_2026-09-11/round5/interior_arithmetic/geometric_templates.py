from itertools import product,combinations
import json
from scipy.optimize import linprog

def plane(h1,h2,p1,p2):
 cand=[(u,v) for u in range(1,h1+1) for v in range(1,h2+1) if not (u<=p1 and v<=p2)]
 out=[()]
 out +=[(q,) for q in cand]
 out +=[(q,r) for q,r in combinations(cand,2) if (q[0]-r[0])*(q[1]-r[1])<0]
 return out

def test(h,cs):
 corners=[(h[0]+1,0,0),(0,h[1]+1,0),(0,0,h[2]+1),(2,1,1)]+cs
 T={p for p in product(*(range(v+1) for v in h)) if not any(all(p[i]>=q[i] for i in range(3)) for q in corners)}
 true=[]
 for q in corners:
  if all(tuple(q[j]-(i==j) for j in range(3)) in T for i in range(3) if q[i]):true.append(q)
 if len(true)!=len(corners):return
 Z=[p for p in T if not any(tuple(p[j]+(i==j) for j in range(3)) in T for i in range(3))]
 if len(Z)<7:return
 for zz in combinations(Z,7):
  # all seven lie in width <1 while each weight >=1; maximize minimum gap improvement
  A=[list(z)+[-1,0] for z in Z]+[[-v for v in z]+[1,1] for z in zz]
  b=[0]*len(Z)+[1]*7
  opt=linprog([0,0,0,0,-1],A_ub=A,b_ub=b,bounds=[(1,None)]*3+[(None,None),(None,None)],method='highs')
  if opt.success and opt.x[-1]>1e-7:return dict(h=h,corners=corners,Z=Z,chosen=zz,weights=opt.x.tolist(),m=len(T))

if __name__=='__main__':
 count=0;nc=0
 for h in [(4,4,4),(5,4,4),(4,5,5)]:
  planes=[plane(h[0],h[1],2,1),plane(h[0],h[2],2,1),plane(h[1],h[2],1,1)]
  for xy,xz,yz in product(*planes):
   # refined arithmetic bound: xy/xz at most one corner with first>=2
   if sum(u>=2 for u,v in xy)>1 or sum(u>=2 for u,v in xz)>1:continue
   cs=[(u,v,0) for u,v in xy]+[(u,0,v) for u,v in xz]+[(0,u,v) for u,v in yz]
   count+=1;r=test(h,cs)
   if r:
    print(json.dumps(dict(count=count,result=r),indent=2));raise SystemExit
 print(json.dumps(dict(count=count,result=None)))
