import sys,json
from itertools import product
from fractions import Fraction as F
from exact_polynomial import Poly,bernstein,reconstruct

def build(parity,flags):
 t,X,Y,Z,W=[Poly.var(i) for i in range(5)]
 x,y,z,w=[(f+u)*F(1,2) for f,u in zip(flags,[X,Y,Z,W])]
 fx,fy,fz,fw=[1-v if f else v for f,v in zip(flags,[x,y,z,w])]
 g=2*t+2+parity;k=t+1
 Q=2*g-1+x+y;P=2*g-1+z+w
 A=3*g-2+3*y;B=3*g-1+3*x;C=3*g-2+3*w;D=3*g-1+3*z
 ga=(g-1)*(3*g-2)+(3*g-3)*x+(3*g-2)*y+3*x*y
 gb=(g-1)*(3*g-2)+(3*g-3)*z+(3*g-2)*w+3*z*w
 E=2*((g-1)*P*Q-F(1,2)*g*(g-1)*(P+Q)+F(1,6)*g*(g-1)*(2*g-1))+y*w*(g+x)*(g+z)+x*z*(g-1+2*y)*(g-1+2*w)
 if parity:
  la=F(1,2)*((k+2*x)*A+(k+y)*B);lb=F(1,2)*((k+2*z)*C+(k+w)*D)
 else:
  la=F(1,2)*((k+x)*A+(k-1+2*y)*B);lb=F(1,2)*((k+z)*C+(k-1+2*w)*D)
 penalty=P*(fx*A+fy*B)+Q*(fz*C+fw*D)
 psi=P*A*B+Q*C*D-2*P*Q-3*(P*Q*(3*g-3)+P*la+Q*lb)+4*P*ga+4*Q*gb-4*E-penalty
 return psi
if __name__=='__main__':
 out=[]
 for parity in (0,1):
  for flags in product((0,1),repeat=4):
   p=build(parity,flags);b=bernstein(p,[1,2,3,4]);deg=[max(e[i] for e in p.p) for i in range(5)]
   rec=reconstruct(b,deg,[1,2,3,4]);assert rec.p==p.p
   out.append({'parity':parity,'flags':flags,'degrees':deg,'count':len(b),'minimum':str(min(b.values())),'negative':sum(c<0 for c in b.values()),'coefficients':{' '.join(map(str,e)):str(c) for e,c in b.items()}})
 print([(t['parity'],t['flags'],t['minimum'],t['negative']) for t in out]);print('total',sum(t['count'] for t in out))
 open('round4/secondary/quotient_three_progression_certificate.json','w').write(json.dumps(out,indent=2))
 assert all(t['negative']==0 for t in out)
