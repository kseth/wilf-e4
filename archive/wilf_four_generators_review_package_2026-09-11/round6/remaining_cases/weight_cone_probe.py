#!/usr/bin/env python3
"""Bounded diagnostic; optimize the entire positive generator-weight cone of actual Apéry ideals."""
import heapq,json,math,random,sys
from pathlib import Path
from scipy.optimize import linprog

def apery(m,a):
 best=[None]*m;best[0]=(0,(0,0,0));heap=[(0,(0,0,0),0)]
 while heap:
  v,p,r=heapq.heappop(heap)
  if best[r]!=(v,p):continue
  for i,w in enumerate(a):
   q=list(p);q[i]+=1;q=tuple(q);n=(r+w)%m;can=(v+w,q)
   if best[n] is None or can<best[n]:best[n]=can;heapq.heappush(heap,(*can,n))
 if any(b is None for b in best):return None
 T={p for v,p in best}
 if any(tuple(int(i==j) for i in range(3)) not in T for j in range(3)):return None
 corners=set();maxima=[]
 for p in T:
  ismax=True
  for j in range(3):
   q=tuple(p[i]+int(i==j) for i in range(3))
   if q in T:ismax=False;continue
   if all(tuple(q[i]-int(i==k) for i in range(3)) in T for k in range(3) if q[k]):corners.add(q)
  if ismax:maxima.append(p)
 return best,T,sorted(corners),maxima

def cone(m,a):
 st=apery(m,a)
 if st is None:return None
 best,T,cs,Z=st;interior=[q for q in cs if all(q)]
 if len(interior)!=1 or sum(interior[0])<5:return None
 sums=[sum(p[i] for p in T) for i in range(3)]
 aub=[[*p,-1] for p in Z]
 for q in cs:
  r=sum(q[i]*a[i] for i in range(3))%m;t=best[r][1]
  aub.append([*(t[i]-q[i] for i in range(3)),0])
 obj=[m-6*s for s in sums]+[4*m]
 opt=linprog(obj,A_ub=aub,b_ub=[0]*len(aub),A_eq=[[1,1,1,0]],b_eq=[1],bounds=[(0,None)]*4,method='highs')
 if not opt.success:raise RuntimeError(opt.message)
 return dict(m=m,generators=[m]+a,interior=interior[0],objective=opt.fun,weights=opt.x.tolist(),mean_sums=sums,corners=cs,maxima=Z)

def main():
 rng=random.Random(847266);worst=None;count=0;attempts=int(sys.argv[1]) if len(sys.argv)>1 else 5000
 for it in range(attempts):
  m=rng.choice([31,43,61,97,151,233,379,613,997])
  # Force a candidate interior relation p.a == 0 mod m.
  p=rng.choice([(3,1,1),(2,2,1),(1,1,3),(1,2,2),(1,3,4),(2,3,3),(3,4,5)])
  a=[m+rng.randrange(1,8*m) for _ in range(2)]
  if math.gcd(p[2],m)>1:continue
  r=(-p[0]*a[0]-p[1]*a[1])*pow(p[2],-1,m)%m
  a.append(r+m*rng.randrange(1,8))
  out=cone(m,a)
  if out is None:continue
  count+=1
  if worst is None or out['objective']<worst['objective']:
   worst=out
   print(json.dumps(dict(attempt=it,count=count,worst=worst)),flush=True)
  if out['objective']< -1e-7:break
 result=dict(status='bounded diagnostic only',attempts=it+1,valid_interior_cones=count,worst=worst)
 Path(__file__).with_name('weight_cone_probe_results.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result),flush=True)
if __name__=='__main__':main()
