"""Exact polynomial certificate for the joint effective-cap horn inequality.
Python standard library only. Analytical domain reductions are in the companion
proof; this checker verifies identities and positive coefficient certificates.
"""
from fractions import Fraction as F
from pathlib import Path
import json

N = 7
class Poly(dict):
    def __add__(self, other):
        other = co(other)
        out = Poly(self)
        for key, value in other.items():
            out[key] = out.get(key, F(0)) + value
        return Poly({key: value for key, value in out.items() if value})
    __radd__ = __add__
    def __neg__(self):
        return Poly({key: -value for key, value in self.items()})
    def __sub__(self, other):
        return self + -co(other)
    def __rsub__(self, other):
        return co(other) + -self
    def __mul__(self, other):
        other = co(other)
        out = Poly()
        for key, value in self.items():
            for key2, value2 in other.items():
                term = tuple(a + b for a, b in zip(key, key2))
                out[term] = out.get(term, F(0)) + value * value2
        return Poly({key: value for key, value in out.items() if value})
    __rmul__ = __mul__
    def __pow__(self, power):
        out = co(1)
        for _ in range(power):
            out = out * self
        return out
    def __truediv__(self, denominator):
        return self * F(1, denominator)

def co(value):
    return value if isinstance(value, Poly) else Poly({(0,) * N: F(value)})

def var(index):
    return Poly({tuple(int(j == index) for j in range(N)): F(1)})

def derivative(polynomial, index):
    out = Poly()
    for key, value in polynomial.items():
        if key[index]:
            lowered = list(key)
            lowered[index] -= 1
            out[tuple(lowered)] = value * key[index]
    return out

def canonical(M, a, x, y):
    return (M*x**3/6-x**4/4+M*x*y*y/2-3*x*x*y*y/4-x*y**3/2
            +(3*a-M)*x*y*(M-a-x-y)/2)

def gain(M, x, y):
    w = y+2*x-M
    z = y-x
    return w*w*z*z/8+w**3*z/24+w**4/192

def single_deficit(a,b,c,x, active=False):
    M=a+b+c
    out=(a*b*c*M/2-canonical(M,a,x,c)
         -canonical(M,b,a,c)-canonical(M,c,a,b))
    return out-gain(M,x,c) if active else out

a,b,c,x,y,z,delta=[var(i) for i in range(N)]
S=a+b+c
M=S+delta

def joint_canonical(M):
    return (a*b*c*(2*M-3*S/2)-canonical(M,a,x,c)
            -canonical(M,b,y,c)-canonical(M,c,z,b))
fa=x**3/6+c*x*x/2+c*(a-b)*x
fb=y**3/6+c*y*y/2+c*(b-a)*y
fc=z**3/6+b*z*z/2+b*(c-a)*z
L=2*a*b*c-fa-fb-fc
assert joint_canonical(M)-joint_canonical(S) == delta*L+delta**2*(c*x+c*y+b*z)/2

def fsmall(t):return t**3/6+c*t*t/2+c*(a-b)*t
def fmiddle(t):return t**3/6+c*t*t/2+c*(b-a)*t
def flarge(t):return t**3/6+b*t*t/2+b*(c-a)*t
Lfull=2*a*b*c-fsmall(b)-fmiddle(a)-flarge(a)
Lzero=2*a*b*c-fmiddle(a)-flarge(a)
assert Lfull == (b-a)**2*(2*(b-a)+3*(c-b))/6
assert Lzero == a*a*((b+c)/2-a/3)

# Derivatives hold at fixed M.
# M=a+x+y+delta, so subtract the delta derivative when differentiating a side.
MM=a+x+y+delta
HH=canonical(MM,a,x,y)
Hx=derivative(HH,3)-derivative(HH,6)
Hy=derivative(HH,4)-derivative(HH,6)
assert 2*Hx == (a-x)*(x-y)**2+delta*(x*x+2*a*y-y*delta)
assert 2*Hy == x*delta*(3*(a+y)-MM)
# Along equal caps x=y=t, fixed M needs correction twice.
HD=canonical(a+2*x+delta,a,x,x)
actual=derivative(HD,3)-2*derivative(HD,6)
MM=a+2*x+delta
assert actual == -6*x*(x-(MM-a)/2)*(x-(MM/3-a))

# Three nonnegative orthant certificates for the saturated single-horn deficit.
p,q,r,s=[var(i) for i in range(4)]
certificates={
    'canonical_x_le_a':single_deficit(p+q,p+q+r,p+q+r+s,p),
    'canonical_x_ge_a':single_deficit(p,p+q+r,p+q+r+s,p+q),
    'active_gain':single_deficit(p,p+2*q+2*r,p+2*q+2*r+s,p+2*q+r,True),
}
# Verify the explicit grouped formulas printed in the proof as well.
claimed_A=(3*p*p*(q+r)**2/4+p*(q+r)**2*(s+r+2*q)/2
           +q*q*((s+2*r)**2/4+2*q*(s+2*r)/3+q*q/2))
claimed_B=(3*p*p*r*r/4+p*r*r*(s+r+2*q)/2+q*r*r*(s+r)/2
           +q*q*((s+2*r)**2/4+r*r/4)+q**3*(s+2*r)/3+q**4/6)
claimed_C=(3*p*p*r*r/4+p*r*r*(s+3*r+4*q)/2
           +s*s*(r*r/4+q*r+q*q/2)
           +s*(11*r**3/6+7*q*r*r+7*q*q*r+7*q**3/3)
           +31*r**4/12+34*q*r**3/3+33*q*q*r*r/2
           +31*q**3*r/3+31*q**4/12)
assert certificates['canonical_x_le_a']==claimed_A
assert certificates['canonical_x_ge_a']==claimed_B
assert certificates['active_gain']==claimed_C
serialized={}
for name, polynomial in certificates.items():
    assert all(value>0 for value in polynomial.values())
    assert all(sum(key)==4 for key in polynomial)
    assert all(not any(key[4:]) for key in polynomial)
    serialized[name]=[{'exponents':list(key[:4]),'coefficient':str(value)}
                      for key,value in sorted(polynomial.items())]
output={
    'slack_expansion_identity':True,
    'slack_linear_endpoint_identities':True,
    'small_cap_derivative_identity':True,
    'large_cap_derivative_identity':True,
    'diagonal_derivative_identity':True,
    'positive_certificate_counts':{name:len(p) for name,p in certificates.items()},
    'printed_grouped_formula_identities':True,
    'certificates':serialized,
}
Path(__file__).with_name('joint_effective_caps_certificate.json').write_text(json.dumps(output,indent=2))
print('PASS: 44 positive rational monomials in three certificates; six exact derivative/slack identities.')
