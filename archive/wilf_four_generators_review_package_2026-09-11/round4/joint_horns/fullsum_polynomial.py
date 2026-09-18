from fractions import Fraction as F
from math import comb
from itertools import product
D=4
class P(dict):
 def __add__(self,o):
  if not isinstance(o,P):o=P({(0,)*D:F(o)})
  z=P(self)
  for k,v in o.items():z[k]=z.get(k,0)+v
  return P({k:v for k,v in z.items() if v})
 __radd__=__add__
 def __neg__(self):return P({k:-v for k,v in self.items()})
 def __sub__(self,o):return self+-co(o)
 def __rsub__(self,o):return co(o)+-self
 def __mul__(self,o):
  o=co(o);z=P()
  for k,v in self.items():
   for j,w in o.items():
    e=tuple(a+b for a,b in zip(k,j));z[e]=z.get(e,0)+v*w
  return P({k:v for k,v in z.items() if v})
 __rmul__=__mul__
 def __pow__(self,n):
  z=co(1)
  for _ in range(n):z=z*self
  return z
 def __truediv__(self,n):return self*F(1,n)
def co(x):return x if isinstance(x,P) else P({(0,)*D:F(x)})
def var(i):return P({tuple(int(j==i) for j in range(D)):F(1)})
a,d,e,t=[var(i) for i in range(D)]
b=a+d;c=b+e;M=a+b+c;x=t*b

def h(a,x,y):
 return M*x**3/6-x**4/4+M*x*y*y/2-3*x*x*y*y/4-x*y**3/2+(3*a-M)*x*y*(M-a-x-y)/2

def gain(x,y):
 w=y+2*x-M;z=y-x
 return w*w*z*z/8+w**3*z/24+w**4/192
credit=a*b*c*M/2
# strongest canonical single-horn effective bound
G=credit-h(a,x,c)-h(b,a,c)-h(c,a,b)
# Bernstein t for each power monomial a,d,e.
def bernstein(p):
 terms={}
 for k,v in p.items():
  h=k[:3];terms.setdefault(h,{})[k[3]]=v
 out={}
 for h,q in terms.items():
  n=max(q)
  coeff=[sum(v*F(comb(i,k),comb(n,k)) for k,v in q.items() if k<=i) for i in range(n+1)]
  out[h]=coeff
 return out
for nm,p in [('canonical',G),('gain',G-gain(x,c))]:
 bb=bernstein(p)
 print(nm)
 for k,v in sorted(bb.items()):
  print(k,[str(z) for z in v])

def build(aa,bb,cc,xx,withgain=False):
 global M
 M=aa+bb+cc
 return aa*bb*cc*M/2-h(aa,xx,cc)-h(bb,aa,cc)-h(cc,aa,bb)-(gain(xx,cc) if withgain else 0)
# x <= a <= b <= c
z,u,v,w=[var(i) for i in range(D)]
for nm,pp in [('x_le_a',build(z+u,z+u+v,z+u+v+w,z)),('x_ge_a',build(z,z+u+v,z+u+v+w,z+u))]:
 print(nm,'negative',[ (k,str(v)) for k,v in pp.items() if v<0], 'all',len(pp))
# active gain requires x >= (a+b)/2; substitute b=a+d, x=(a+b)/2+t*d/2, or a=x-u-v,b=x+u-v where u>=v
# Set x=a+u+v, b=a+2u, 0<=v<=u. use u=v+w, x=a+2v+w,b=a+2v+2w.
pp=build(z,z+2*u+2*v,z+2*u+2*v+w,z+2*u+v,True)
print('gain_active','negative',[(k,str(v)) for k,v in pp.items() if v<0], 'all',len(pp))
# Verify derivative factorization without relying on sampled signs.
def derivative(p,i):
 out=P()
 for k,v in p.items():
  if k[i]:
   j=list(k);j[i]-=1;out[tuple(j)]=v*k[i]
 return out
# base z, small u, large v, slack w, M=z+u+v+w.
M=z+u+v+w
# derivative with M held fixed must account for substituted M: d/du h minus d/dw h.
HH=h(z,u,v)
actual=2*(derivative(HH,1)-derivative(HH,3))
expected=(z-u)*(u-v)**2+w*(u*u+2*z*v-v*w)
print('derivative_factor',actual==expected)
