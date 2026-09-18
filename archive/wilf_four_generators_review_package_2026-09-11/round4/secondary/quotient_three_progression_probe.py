from fractions import Fraction as F
from itertools import product

def distribution(g,x,y):
 c={}
 def put(h,k,v):c[h,k]=c.get((h,k),0)+v
 put(g,g,x*y)
 for k in range(g):put(g,k,y)
 put(g-1,g,x)
 put(g-1,g-1,1-x*y)
 for k in range(g-1):put(g-1,k,1-y)
 for h in range(1,g-1):put(h,g,x);put(h,g-1,1-x)
 put(0,g,x*y);put(0,g-1,1-x*y)
 return {k:v for k,v in c.items() if v}

def evaluate(g,x,y,z,w,coarse=False):
 assert g>=2
 ca=distribution(g,x,y);cb=distribution(g,z,w)
 Q=2*g-1+x+y;P=2*g-1+z+w
 assert sum(ca.values())==Q and sum(cb.values())==P
 ga=sum((h+k)*v for (h,k),v in ca.items());gb=sum((h+k)*v for (h,k),v in cb.items())
 E=sum(c*d*(min(h,H,k+K+1)+min(k,K,h+H)) for (h,k),c in ca.items() for (H,K),d in cb.items())
 if coarse:E=2*((g-1)*P*Q-F(g*(g-1),2)*(P+Q)+F(g*(g-1)*(2*g-1),6))+y*w*(g+x)*(g+z)+x*z*(g-1+2*y)*(g-1+2*w)
 A=3*g-2+3*y;B=3*g-1+3*x;C=3*g-2+3*w;D=3*g-1+3*z
 t=g//2
 la=F(1,2)*((t+x)*A+(t-1+2*y)*B) if g%2==0 else F(1,2)*((t+2*x)*A+(t+y)*B)
 lb=F(1,2)*((t+z)*C+(t-1+2*w)*D) if g%2==0 else F(1,2)*((t+2*z)*C+(t+w)*D)
 penalty=P*(min(x,1-x)*A+min(y,1-y)*B)+Q*(min(z,1-z)*C+min(w,1-w)*D)
 return P*A*B+Q*C*D-2*P*Q-3*(P*Q*(3*g-3)+P*la+Q*lb)+4*P*ga+4*Q*gb-4*E-penalty
if __name__=='__main__':
 vals=[F(i,4) for i in range(5)]
 for g in [2,3,4,5,8,20]:
  print(g,min((evaluate(g,*t,coarse=True),t) for t in product(vals,repeat=4)),flush=True)
