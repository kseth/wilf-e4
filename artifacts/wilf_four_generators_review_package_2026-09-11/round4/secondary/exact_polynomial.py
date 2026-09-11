"""Exact rational polynomial operations and mixed Bernstein/power conversion."""
from fractions import Fraction as Q
from math import comb
from itertools import product


class Poly:
    def __init__(self,p=0):
        self.p=p.p.copy() if isinstance(p,Poly) else ({(0,)*5:Q(p)} if p else {})
    @staticmethod
    def var(i):
        p=Poly();exp=[0]*5;exp[i]=1;p.p={tuple(exp):Q(1)};return p
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
    def eval(self,x):return sum(v*__import__('functools').reduce(lambda a,b:a*b,(t**k for t,k in zip(x,e)),Q(1)) for e,v in self.p.items())

def bernstein(poly,bounded):
    deg=[max((e[i] for e in poly.p),default=0) for i in range(5)]
    out={}
    for ex in product(*(range(d+1) for d in deg)):
        b=Q(0)
        for e,v in poly.p.items():
            scale=Q(1)
            for i in range(5):
                if i in bounded:
                    if e[i]>ex[i]:scale=0;break
                    scale*=Q(comb(ex[i],e[i]),comb(deg[i],e[i]))
                elif e[i]!=ex[i]:scale=0;break
            b+=v*scale
        out[ex]=b
    return out

def reconstruct(coefficients, degrees, bounded):
    """Expand the mixed basis explicitly, independently of conversion."""
    variables=[Poly.var(i) for i in range(5)]
    basis={}
    for i,(variable,degree) in enumerate(zip(variables,degrees)):
        for j in range(degree+1):
            basis[i,j]=(comb(degree,j)*variable**j*(1-variable)**(degree-j)
                        if i in bounded else variable**j)
    result=Poly()
    for exponent,coefficient in coefficients.items():
        if not coefficient:
            continue
        term=Poly(coefficient)
        for i,j in enumerate(exponent):
            term=term*basis[i,j]
        result=result+term
    return result
