from heapq import heappush,heappop
from random import Random
import json

def apery(gens):
 m,*a=gens
 d=[None]*m;d[0]=(0,(0,0,0));q=[(0,(0,0,0),0)]
 while q:
  v,x,r=heappop(q)
  if d[r]!=(v,x):continue
  for i,b in enumerate(a):
   s=(r+b)%m;y=tuple(u+(i==j) for j,u in enumerate(x));cand=(v+b,y)
   if d[s] is None or cand<d[s]:d[s]=cand;heappush(q,(*cand,s))
 if None in d:return
 T={x for v,x in d}
 p=(2,1,1)
 if p in T or any(tuple(u-(i==j) for j,u in enumerate(p)) not in T for i in range(3)):return
 maxima=[x for x in T if all(tuple(u+(i==j) for j,u in enumerate(x)) not in T for i in range(3))]
 M=max(v for v,x in d);Z=[x for v,x in d if M-v<m]
 corners=set()
 for x in T:
  for i in range(3):
   y=tuple(u+(i==j) for j,u in enumerate(x))
   if y not in T and all(tuple(u-(k==j) for j,u in enumerate(y)) in T for k in range(3) if y[k]):corners.add(y)
 c=M-m+1;g=sum(v//m for v,x in d)
 return dict(gens=gens,m=m,M=M,W=3*c-4*g,maxima=sorted(maxima),Z=sorted(Z),corners=sorted(corners),axis=[max(x[i] for x in T) for i in range(3)])

rng=Random(4931208);bestq={};bestz={};count=0;max_by_corners={}
for it in range(15000):
 m=rng.randrange(11,501);A=rng.randrange(m+1,20*m);B=rng.randrange(m+1,20*m)
 C=(-(2*A+B))%m+m*rng.randrange(2,20)
 if C<=m or len({A,B,C})<3:continue
 out=apery((m,A,B,C))
 if out is None:continue
 count+=1;q=len(out['maxima']);z=len(out['Z'])
 if q not in bestq:bestq[q]=out
 if z not in bestz:bestz[z]=out
pat=dict(count=count,maxima=bestq,final_window=bestz)
print(json.dumps(pat,indent=2))
