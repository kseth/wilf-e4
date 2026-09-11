from math import gcd
from heapq import heappop, heappush
from itertools import product
import json, random

def apery(gens):
 m=min(gens);dist=[10**30]*m;dist[0]=0;heap=[(0,0)]
 while heap:
  d,r=heappop(heap)
  if d!=dist[r]:continue
  for a in gens:
   rr=(r+a)%m;dd=d+a
   if dd<dist[rr]:dist[rr]=dd;heappush(heap,(dd,rr))
 F=max(dist)-m;g=(sum(dist)-m*(m-1)//2)//m
 return {'F':F,'g':g,'W':3*(F+1)-4*g,'m':m}

def member(n,a,b):return n>=0 and (n*pow(a,-1,b)%b)*a<=n

def side(r,h,v,z):
 a=4*v+z;b=2*r+3*h;q=(2*r+h)*v+(r+h)*z
 if gcd(a,b)!=1:return None
 if any(member(k*q,a,b)!=(k>=3) for k in range(1,8)):return None
 if not all(member(k*q-a-b,a,b) for k in (3,4,5)):return None
 return dict(r=r,h=h,v=v,z=z,a=a,b=b,q=q)

profiles=[{0,*range(3,10)}, {0,*range(2,10)}, {0,1,*range(3,10)},set(range(10))]
f=[2,1,2,-1];dual=[2,1,0,3]
def fsum(a,b):
 sums={x+y for x in profiles[a] for y in profiles[b]}
 return max([-1]+[i for i in range(8) if i not in sums])
Kcoef=[[f[i]+f[j]-fsum(dual[i],dual[j]) for j in range(4)] for i in range(4)]

def formulas(A,B):
 a,b,q=A['a'],A['b'],A['q'];c,d,p=B['a'],B['b'],B['q']
 r,h,v=A['r'],A['h'],A['v'];R,H,V=B['r'],B['h'],B['v']
 X=p*(a*b-a-b)+q*(c*d-c-d);P=p*q
 E=v*V*(r*R+r*H+h*R+4*h*H)
 g=(X+P+1)//2-p*v*(r+3*h)-q*V*(R+3*H)+E
 alpha=[0,h*a,v*b,min(2*v*b,h*a+v*b)]
 beta=[0,H*c,V*d,min(2*V*d,H*c+V*d)]
 K=min(p*alpha[i]+q*beta[j]+P*Kcoef[i][j] for i in range(4) for j in range(4))
 F=X-K;W=3*(F+1)-4*g
 bound=X-2*P+1+4*p*v*(r+3*h)+4*q*V*(R+3*H)-4*E-(3*(p*(h*a+2*v*b)+q*(H*c+2*V*d))+1)//2
 return {'F':F,'g':g,'W':W,'bound':bound,'m':min(p*a,p*b,q*c,q*d)}

def minimal(gens):
 for k,z in enumerate(gens):
  other=gens[:k]+gens[k+1:]
  m=min(other);dist=[10**30]*m;dist[0]=0;heap=[(0,0)]
  while heap:
   d,r=heappop(heap)
   if d!=dist[r] or d>z:continue
   for a in other:
    rr=(r+a)%m;dd=d+a
    if dd<dist[rr] and dd<=z:dist[rr]=dd;heappush(heap,(dd,rr))
  if dist[z%m]<=z:return False
 return True

if __name__=='__main__':
 sides=[A for t in product(range(1,5),repeat=4) if (A:=side(*t))]
 random.Random(47).shuffle(sides)
 out=[]
 for A,B in product(sides,sides):
  p,q=B['q'],A['q']
  if gcd(p,q)!=1:continue
  gens=sorted([p*A['a'],p*A['b'],q*B['a'],q*B['b']])
  if len(set(gens))<4 or not minimal(gens):continue
  exact=apery(gens);form=formulas(A,B)
  assert all(exact[k]==form[k] for k in exact),(A,B,exact,form)
  assert form['bound']>=1,(A,B,form)
  out.append({'A':A,'B':B,'gens':gens,'exact':exact,'formula':form})
  if len(out)==100:break
 print('sides',len(sides),'cases',len(out),'smallest_W',min(t['exact']['W'] for t in out),'smallest_bound',min(t['formula']['bound'] for t in out))
 open('round4/secondary/ordinary_three_checks.json','w').write(json.dumps({'sides_count':len(sides),'K_coefficients':Kcoef,'cases':out},indent=2))
