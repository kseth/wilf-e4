"""Exact polynomial certificates for the full-cap plateau/boundary horn theorem.
All coefficients use Fraction; no numeric optimization is involved.
"""
from fractions import Fraction as Q
import json
from pathlib import Path
ZERO={};ONE={(0,0,0):Q(1)}
def add(*ps):
 o={}
 for p in ps:
  for k,v in p.items():o[k]=o.get(k,Q(0))+v
 return {k:v for k,v in o.items() if v}
def scale(p,q):return {k:v*q for k,v in p.items() if v*q}
def sub(p,q):return add(p,scale(q,-1))
def mul(p,q):
 o={}
 for i,a in p.items():
  for j,b in q.items():
   k=tuple(x+y for x,y in zip(i,j));o[k]=o.get(k,Q(0))+a*b
 return {k:v for k,v in o.items() if v}
def pw(p,n):
 o=ONE
 for _ in range(n):o=mul(o,p)
 return o
def deriv(p,i):
 o={}
 for k,v in p.items():
  if k[i]:
   j=list(k);j[i]-=1;o[tuple(j)]=v*k[i]
 return o
def ev(p,x):return sum(v*pw_num(x,k) for k,v in p.items())
def pw_num(x,k):
 r=Q(1)
 for a,b in zip(x,k):r*=a**b
 return r

a={(1,0,0):Q(1)};b={(0,1,0):Q(1)};c={(0,0,1):Q(1)}
def canonical(a,U,V):
 R=sub(ONE,a)
 inside=add(R,scale(pw(R,2),Q(-3,2)),scale(mul(R,U),Q(3,2)),scale(U,Q(-1,2)),scale(mul(R,V),Q(3,2)),scale(V,-1),scale(pw(U,2),Q(-1,2)),scale(mul(U,V),Q(-3,4)))
 return add(mul(mul(U,V),inside),scale(pw(V,3),Q(1,6)),scale(pw(V,4),Q(-1,4)))
S=add(a,b,c);delta=sub(ONE,S);x=sub(b,a);y=sub(c,b);e2=add(mul(a,b),mul(a,c),mul(b,c))
credit=mul(mul(mul(a,b),c),sub(scale(ONE,2),scale(S,Q(3,2))))
gap=sub(credit,add(canonical(a,c,b),canonical(b,c,a),canonical(c,b,a)))
F=scale(mul(pw(x,2),add(scale(pw(x,2),2),scale(mul(x,y),4),scale(pw(y,2),3))),Q(1,12))
claimed=add(scale(mul(pw(delta,2),e2),Q(1,2)),scale(mul(mul(delta,pw(x,2)),add(scale(x,2),scale(y,3))),Q(1,6)),F)
assert sub(gap,claimed)=={}

def bal(r):return add(scale(pw(r,3),Q(1,12)),scale(pw(r,4),Q(-3,32)))
def primitive(P,r):
 return mul(P,add(scale(pw(r,3),Q(-1,2)),scale(pw(r,2),Q(1,2)),scale(mul(P,pw(r,2)),Q(3,4)),scale(mul(P,r),-1)))
def tent(B,C,q):
 r1=scale(q,2);r2=add(B,q);R=add(B,C)
 return add(bal(r1),primitive(q,r2),scale(primitive(q,r1),-1),primitive(B,R),scale(primitive(B,r2),-1))
# Use symbolic a=B,b=C,c=q in the next two identities.
I=tent(a,b,c)
expected_derivative=scale(mul(pw(sub(a,c),2),sub(sub(ONE,a),scale(c,2))),Q(1,2))
assert sub(deriv(I,2),expected_derivative)=={}
qstar=scale(sub(ONE,a),Q(1,2));w=sub(add(a,scale(b,2)),ONE);yy=sub(a,b)
gain=sub(tent(a,b,qstar),tent(a,b,b))
gain_claim=add(scale(mul(pw(w,2),pw(yy,2)),Q(1,8)),scale(mul(pw(w,3),yy),Q(1,24)),scale(pw(w,4),Q(1,192)))
assert sub(gain,gain_claim)=={}
# Subtracting the gain at x rather than (x-delta)+ gives the stated safe lower bound.
gx=add(scale(mul(pw(x,2),pw(y,2)),Q(1,8)),scale(mul(pw(x,3),y),Q(1,24)),scale(pw(x,4),Q(1,192)))
remaining=add(scale(mul(pw(x,2),pw(y,2)),Q(1,8)),scale(mul(pw(x,3),y),Q(7,24)),scale(pw(x,4),Q(31,192)))
assert sub(sub(F,gx),remaining)=={}
assert ev(gain,(Q(2,5),Q(2,5),0))==Q(1,120000)
out={'canonical_gap_identity':True,'boundary_tent_derivative_identity':True,'boundary_gain_identity':True,'remaining_positive_polynomial_identity':True,'equal_caps_gain':'1/120000'}
Path(__file__).with_name('fullcap_boundary_verification.json').write_text(json.dumps(out,indent=2))
print('PASS: exact canonical-gap, one-tent derivative, gain, and positive-remainder identities.')
