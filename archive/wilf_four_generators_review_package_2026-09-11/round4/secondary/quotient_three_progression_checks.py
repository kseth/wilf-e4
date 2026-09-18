from fractions import Fraction as F
from itertools import product
from math import gcd
from collections import Counter
import json,sys,random
sys.path.insert(0,'round4/secondary')
from ordinary_three_checks import member,apery,minimal
from quotient_three_progression_probe import distribution,evaluate

def side(g,r,s,alpha,beta):
 assert 0<alpha<r and 0<beta<s
 h=(g-1)*r+alpha;v=(g-1)*s+beta
 a=3*v+s;b=2*r+3*h;q=r*v+(r+h)*s
 if gcd(a,b)!=1:return None
 assert [k for k in range(1,3*g+3) if not member(k*q,a,b)]==[k for k in range(1,3*g) if k%3]
 assert all(member(k*q-a-b,a,b) for k in (3,3*g+1,3*g+2))
 reps=[(i,j) for i in range(r+h) for j in range(s)]+[(i,j) for i in range(r) for j in range(s,v+s)]
 assert len(reps)==q
 assert len({(i*a+j*b)%q for i,j in reps})==q
 counts=Counter();mins={}
 for i,j in reps:
  n=i*a+j*b
  assert all(not member(n-k*q,a,b) for k in (1,2,3))
  H=next(k for k in range(g+1) if member(n+(3*k+1)*q,a,b));K=next(k for k in range(g+1) if member(n+(3*k+2)*q,a,b))
  counts[H,K]+=1;mins[H,K]=min(mins.get((H,K),n),n)
 predicted={k:int(v*r*s) for k,v in distribution(g,F(alpha,r),F(beta,s)).items()}
 assert dict(counts)==predicted,(g,r,s,alpha,beta,counts,predicted)
 t=g//2
 if g%2==0:
  types=[(t,g),(g-1,t-1)];labels=[((t-1)*s+beta)*b,(t*r+alpha)*a+beta*b]
 else:
  types=[(g,t),(t,g-1)];labels=[(t*r+alpha)*a,alpha*a+(t*s+beta)*b]
 assert all(typ in mins and mins[typ]<=label for typ,label in zip(types,labels))
 return dict(g=g,r=r,s=s,alpha=alpha,beta=beta,a=a,b=b,q=q,counts={str(k):v for k,v in counts.items()},mins={str(k):v for k,v in mins.items()},self_dual_types=types,self_dual_labels=labels)

if __name__=='__main__':
 out=[]
 for g in (2,3,4,5,8,12):
  sides=[A for r,s in product(range(2,6),repeat=2) for alpha in range(1,r) for beta in range(1,s) if (A:=side(g,r,s,alpha,beta))]
  random.Random(g).shuffle(sides);cases=[]
  for A,B in product(sides,sides):
   p,q=B['q'],A['q']
   if gcd(p,q)!=1:continue
   gens=sorted([p*A['a'],p*A['b'],q*B['a'],q*B['b']])
   if len(set(gens))<4 or not minimal(gens):continue
   inv=apery(gens)
   psi=evaluate(g,F(A['alpha'],A['r']),F(A['beta'],A['s']),F(B['alpha'],B['r']),F(B['beta'],B['s']),coarse=True)
   lower=1+A['r']*A['s']*B['r']*B['s']*psi
   assert inv['W']>=lower>=1,(A,B,inv,lower)
   cases.append({'A':A,'B':B,'gens':gens,'invariants':inv,'lower_bound':str(lower)})
   if len(cases)==10:break
  print('g',g,'sides',len(sides),'paired cases',len(cases),'least W',min([c['invariants']['W'] for c in cases],default=None),flush=True)
  out.append({'g':g,'sides_count':len(sides),'cases':cases})
 open('round4/secondary/quotient_three_progression_checks.json','w').write(json.dumps(out,indent=2))
