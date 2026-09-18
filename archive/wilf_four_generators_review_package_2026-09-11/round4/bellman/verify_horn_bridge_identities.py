"""Exact coefficient checks for the analytic arbitrary-horn bridge.

Standard library only. These checks verify the polynomial identities used
in the proof, not the nonalgebraic reductions; those require the written
proof and its independent audit.
"""
from fractions import Fraction as F
import json
from pathlib import Path

N=6
class P:
    def __init__(self, value=0):
        if isinstance(value,P): self.t=dict(value.t)
        elif isinstance(value,dict):self.t={k:F(v) for k,v in value.items() if v}
        else:self.t={(0,)*N:F(value)} if value else {}
    def __add__(self,other):
        other=P(other);d=dict(self.t)
        for k,v in other.t.items():d[k]=d.get(k,F(0))+v
        return P(d)
    __radd__=__add__
    def __neg__(self):return P({k:-v for k,v in self.t.items()})
    def __sub__(self,other):return self+-P(other)
    def __rsub__(self,other):return P(other)+-self
    def __mul__(self,other):
        other=P(other);d={}
        for i,a in self.t.items():
            for j,b in other.t.items():
                k=tuple(x+y for x,y in zip(i,j));d[k]=d.get(k,F(0))+a*b
        return P(d)
    __rmul__=__mul__
    def __truediv__(self,n):return self*F(1,n)
    def __pow__(self,n):
        out=P(1)
        for _ in range(n):out=out*self
        return out
    def deriv(self,i):
        d={}
        for k,v in self.t.items():
            if k[i]:
                j=list(k);j[i]-=1;d[tuple(j)]=v*k[i]
        return P(d)

def var(i):return P({tuple(int(j==i) for j in range(N)):1})
c,d,e,u,p,q=[var(i) for i in range(N)]
A=lambda r:1-3*r/2
# Primitive of c*(r-c)*A(r) with respect to r.
B=lambda r,c:c*(-r**3/2+(F(1,2)+3*c/4)*r**2-c*r)
g=lambda c,d:c*d**2*(2*d+3*c-2)/4
checks={}
def check(name,left,right):
    delta=left-right
    assert not delta.t,(name,delta.t)
    checks[name]=True

# General exact tight-slab payoff; symbolic sum s=u+p.
r=c;s=u+p;area=u*p
integral=area*((1+3*s/2)*(r-s)-3*(r**2-s**2)/2)
check('tight_slab_transition',integral,A(r)*(r-s)*area)

# Constant-coordinate jump gain, independent of its starting location u.
r=c+u+d;s=c+u
jump=A(r)*d*c*u
boundary=B(r,c)-B(s,c)
check('constant_side_jump_gain',jump-boundary,g(c,d))
check('constant_side_gain_merge',g(c,d+e)-g(c,d)-g(c,e),3*c*d*e*(d+e+c-F(2,3))/2)

# Cross-turn gain: C=c, start=(u+p,c), end=(u,c-q).
r=u+p+c;s=u+c-q
jump=A(r)*(p+q)*u*(c-q)
boundary=(B(r,c)-B(u+c,c))+(B(u+c,u)-B(s,u))
G=(3*c**2*p**2+2*c*p**3-2*c*p**2+6*p**2*q*u+6*p*q**2*u+6*p*q*u**2-4*p*q*u+2*q**3*u+3*q**2*u**2-2*q**2*u)/4
check('cross_turn_gain',jump-boundary,G)
check('cross_turn_endpoint_derivative',G.deriv(5),u*(p+q)*(3*p+3*q+3*u-2)/2)

# Balanced-ending jump and tail; use c=r, u=z.
r=c;z=u
D=A(r)*(r-2*z)*z**2+2*z**3/3-3*z**4/2
check('balanced_ending_jump_derivative',D.deriv(3),-6*z*(z-r/2)*(z-r+F(2,3)))

out={'status':'PASS','arithmetic':'exact Fraction polynomial coefficient arithmetic','identities_checked':len(checks),'checks':checks,'scope':'Polynomial identities only; the written argument supplies the inequality and profile reductions.'}
Path(__file__).with_name('horn_bridge_identity_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
