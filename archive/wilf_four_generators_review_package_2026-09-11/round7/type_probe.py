from heapq import heappush,heappop
from math import gcd
import json,random

def inspect(gens,shape=False):
 m,*a=gens
 if gcd(*gens)!=1:return
 inf=10**100
 ap=[inf]*m;rep=[None]*m;ap[0]=0;rep[0]=(0,0,0);heap=[(0,(0,0,0),0)]
 while heap:
  d,x,r=heappop(heap)
  if (d,x)!=(ap[r],rep[r]):continue
  for i,v in enumerate(a):
   q=(r+v)%m;y=tuple(x[j]+(j==i) for j in range(3));nd=d+v
   if nd<ap[q] or nd==ap[q] and y<rep[q]:
    ap[q]=nd;rep[q]=y;heappush(heap,(nd,y,q))
 def sin(x):return x>=0 and x>=ap[x%m]
 if any(any(sin(v-u) for u in gens[:j]) for j,v in enumerate(gens[1:],1)):return
 F=max(ap)-m;c=F+1;g=sum(w//m for w in ap);n=c-g;W=3*n-g
 pf=sorted(w-m for w in ap if w>0 and all(sin(w-m+v) for v in gens))
 t=len(pf)
 if t<4:return
 def lam(f):return sum(max(0,(f-w)//m+1) for w in ap)
 lams=[lam(f) for f in pf]
 theta=sum(lams)-g
 xi=sum((w//m)*(sum(sin(f-w+m) for f in pf)-1) for w in ap[1:])
 # A stronger lower bound than the paper's bare t-3 uses generator incidence.
 primitive=sum(sum(sin(f-v+m) for f in pf)-1 for v in a)
 d=t-3;target=sum(lams[:d]);margin=theta-target
 assert margin==sum(lams[-3:])-g
 assert margin==W-sum(n-q for q in lams[-3:])
 out=dict(gens=gens,m=m,c=c,g=g,n=n,W=W,pf=pf,t=t,k=sum(w>=c for w in ap),lambdas=lams,theta=theta,xi=xi,primitive=primitive,target=target,margin=margin,xi_margin=xi-target,t_minus3=t-3,tail_penalty=W-margin)
 if shape:
  T=set(rep);cand=set()
  for x in T:
   for i in range(3):
    p=tuple(x[j]+(j==i) for j in range(3))
    if p not in T and all(tuple(p[j]-(j==k) for j in range(3)) in T for k in range(3) if p[k]):cand.add(p)
  out['corners']=sorted(cand);out['interior']=[p for p in sorted(cand) if min(p)>0];out['apery']=ap;out['representatives']=rep
 return out

if __name__=='__main__':
 fixtures=[[175,185,201,202],[155,1552,1647,1651],[1213,1214,2478,4952]]
 out={'fixtures':[inspect(g,True) for g in fixtures]}
 rng=random.Random(20260910);lowxi=None;lowmargin=None;besttail=None;counts={'proposals':0,'minimal_e4_tge4':0,'tge7':0,'xi_fails':0,'marashdeh_fails':0}
 for _ in range(12000):
  m=rng.randrange(30,500);gens=[m,*sorted(rng.sample(range(m+1,4*m+1),3))];counts['proposals']+=1
  r=inspect(gens)
  if r is None:continue
  counts['minimal_e4_tge4']+=1
  if r['t']>=7:counts['tge7']+=1
  if r['xi_margin']<0:counts['xi_fails']+=1
  if r['margin']<0:counts['marashdeh_fails']+=1
  if lowxi is None or r['xi_margin']<lowxi['xi_margin']:lowxi=r
  if lowmargin is None or r['margin']<lowmargin['margin']:lowmargin=r
  if besttail is None or r['tail_penalty']>besttail['tail_penalty']:besttail=r
 out.update(counts=counts,lowest_xi=inspect(lowxi['gens'],True),lowest_margin=inspect(lowmargin['gens'],True),largest_tail=inspect(besttail['gens'],True))
 with open('round7/type_probe_results.json','w') as f:json.dump(out,f,indent=2)
 print(json.dumps({k:v for k,v in out.items() if k!='fixtures'},default=str)[:5000])
