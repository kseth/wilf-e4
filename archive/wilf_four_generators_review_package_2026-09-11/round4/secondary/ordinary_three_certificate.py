from fractions import Fraction as F
from itertools import product
from math import comb
import json
N=4
class Poly:
 def __init__(self,p=0):self.p=p.p.copy() if isinstance(p,Poly) else ({(0,)*N:F(p)} if p else {})
 @staticmethod
 def var(i):
  p=Poly(); e=[0]*N;e[i]=1;p.p[tuple(e)]=F(1);return p
 def __add__(self,b):
  b=Poly(b);c=Poly(self)
  for e,v in b.p.items():c.p[e]=c.p.get(e,0)+v
  c.p={e:v for e,v in c.p.items() if v};return c
 __radd__=__add__
 def __neg__(self):
  p=Poly();p.p={e:-v for e,v in self.p.items()};return p
 def __sub__(self,b):return self+-Poly(b)
 def __rsub__(self,b):return Poly(b)+-self
 def __mul__(self,b):
  b=Poly(b);c=Poly()
  for e,v in self.p.items():
   for f,w in b.p.items():
    ef=tuple(x+y for x,y in zip(e,f));c.p[ef]=c.p.get(ef,0)+v*w
  c.p={e:v for e,v in c.p.items() if v};return c
 __rmul__=__mul__
 def __pow__(self,n):
  p=Poly(1)
  for _ in range(n):p=p*self
  return p

def cert(flags):
 vars=[Poly.var(i) for i in range(N)]
 x,y,X,Y=[1+t if f else t for t,f in zip(vars,flags)]
 fx,fy,fX,fY=[Poly(1) if f else t for t,f in zip(vars,flags)]
 Q=2*x+1+(x+1)*y;P=2*X+1+(X+1)*Y
 A=4*x+x*y+F(1,2)*y+8-fx*(4+y)-fy*(2*x+3)
 B=4*X+X*Y+F(1,2)*Y+8-fX*(4+Y)-fY*(2*X+3)
 p=P*A+Q*B-4*(x*X+x+X+4)
 deg=[max(e[i] for e in p.p) for i in range(N)]
 bounded=[i for i,f in enumerate(flags) if not f]
 co={}
 for ex in product(*(range(d+1) for d in deg)):
  b=F(0)
  for e,v in p.p.items():
   t=F(1)
   for i in range(N):
    if i in bounded:
     if e[i]>ex[i]:t=0;break
     t*=F(comb(ex[i],e[i]),comb(deg[i],e[i]))
    elif e[i]!=ex[i]:t=0;break
   b+=v*t
  co[ex]=b
 rec=Poly()
 for e,c in co.items():
  term=Poly(c)
  for i,d in enumerate(deg):
   term*=comb(d,e[i])*vars[i]**e[i]*(1-vars[i])**(d-e[i]) if i in bounded else vars[i]**e[i]
  rec+=term
 assert rec.p==p.p
 return {'flags':flags,'degrees':deg,'count':len(co),'minimum':str(min(co.values())),'negative':sum(c<0 for c in co.values()),'coefficients':{' '.join(map(str,e)):str(c) for e,c in co.items()}}
if __name__=='__main__':
 out=[cert(f) for f in product((0,1),repeat=N)]
 print([(t['flags'],t['count'],t['minimum'],t['negative']) for t in out])
 print('total',sum(t['count'] for t in out))
 open('round4/secondary/ordinary_three_certificate.json','w').write(json.dumps(out,indent=2))
 assert all(t['negative']==0 for t in out)
