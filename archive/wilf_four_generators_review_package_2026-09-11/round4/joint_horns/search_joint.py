import numpy as np
from scipy.optimize import differential_evolution,minimize
import json
from pathlib import Path

def P(x,y):
 return x**3/6-x**4/4+x*y*y/2-3*x*x*y*y/4-x*y**3/2

def H(a,x,y):
 if x>y:x,y=y,x
 w=max(0,y+2*x-1);z=y-x
 return P(x,y)+w*w*z*z/8+w**3*z/24+w**4/192+(3*a-1)*x*y*(1-a-x-y)/2

def U(a,B,C):
 if B<C:B,C=C,B
 q=min(C,(1-B)/2)
 coeff=[-1,.5,B*(1-1.5*B-3*a),B*(-.5+B-.5*B*B+2*a-1.5*a*B-1.5*a*a)]
 roots=[r.real for r in np.roots(coeff) if abs(r.imag)<1e-7 and 0<r.real<q]
 caps=[(0,0),(C,C),(C,B),(q,B)]+[(x,B) for x in roots]
 return max([(H(a,x,y),x,y) for x,y in caps])

def obj(v):
 a=v[0]/3;b=a+(1-3*a)*v[1]/2;c=b+(1-a-2*b)*v[2]
 S=a+b+c
 js=[U(a,b,c),U(b,a,c),U(c,a,b)]
 credit=a*b*c*(2-1.5*S)
 margin=credit-sum(j[0] for j in js)
 return margin/(a*b*c+1e-15)

r=differential_evolution(obj,[(.0001,.9999),(0,1),(0,1)],tol=1e-10,popsize=20,maxiter=600,seed=4301)
v=r.x;a=v[0]/3;b=a+(1-3*a)*v[1]/2;c=b+(1-a-2*b)*v[2]
out={'minimum_normalized_margin':r.fun,'central':[a,b,c],'horns':[U(a,b,c),U(b,a,c),U(c,a,b)],'status':str(r.message)}
print(json.dumps(out,indent=2))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
