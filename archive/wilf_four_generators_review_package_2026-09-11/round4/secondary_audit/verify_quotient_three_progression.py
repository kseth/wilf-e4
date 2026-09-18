"""Independent cubic-interpolation audit of the R_g family certificate.

No proposal code is imported. All operations are exact standard-library rationals.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

BITS=list(product((0,1),repeat=4))


def psi(parity, t, values):
    x,y,z,w=map(F,values)
    t=F(t)
    g=2*t+2+parity
    k=t+1
    Q=2*g-1+x+y
    P=2*g-1+z+w
    A=3*g-2+3*y
    B=3*g-1+3*x
    C=3*g-2+3*w
    D=3*g-1+3*z
    GA=(g-1)*(3*g-2)+(3*g-3)*x+(3*g-2)*y+3*x*y
    GB=(g-1)*(3*g-2)+(3*g-3)*z+(3*g-2)*w+3*z*w
    if parity:
        LA=((k+2*x)*A+(k+y)*B)/2
        LB=((k+2*z)*C+(k+w)*D)/2
    else:
        LA=((k+x)*A+(k-1+2*y)*B)/2
        LB=((k+z)*C+(k-1+2*w)*D)/2
    E=2*((g-1)*P*Q-g*(g-1)*(P+Q)/2+g*(g-1)*(2*g-1)/6)
    E+=y*w*(g+x)*(g+z)+x*z*(g-1+2*y)*(g-1+2*w)
    fx,fy,fz,fw=[min(u,1-u) for u in (x,y,z,w)]
    return (P*A*B+Q*C*D-2*P*Q-3*(P*Q*(3*g-3)+P*LA+Q*LB)
            +4*P*GA+4*Q*GB-4*E
            -P*(fx*A+fy*B)-Q*(fz*C+fw*D))


def interpolate(values):
    a,b,c,d=values
    d1=b-a
    d2=c-2*b+a
    d3=d-3*c+3*b-a
    return (a,d1-d2/2+d3/3,d2/2-d3/2,d3/6)


def main():
    proposal=json.loads(Path('round4/secondary/quotient_three_progression_certificate.json').read_text())
    proposal={(r['parity'],tuple(r['flags'])):r for r in proposal}
    rows=[]
    checks=0
    for parity in (0,1):
        for flags in BITS:
            coeffs={}
            for corner in BITS:
                values=[F(f+b,2) for f,b in zip(flags,corner)]
                powers=interpolate([psi(parity,t,values) for t in range(4)])
                for k,c in enumerate(powers):
                    coeffs[(k,*corner)]=c
                    assert F(proposal[parity,flags]['coefficients'][' '.join(map(str,(k,*corner)))])==c
            assert min(coeffs.values())>=0
            # On each half-box the expression has degree <=3 in t and
            # degree <=1 separately in its four bounded coordinates.
            # The 4*16 interpolation nodes therefore prove reconstruction.
            # Independently test further rational off-grid positions too.
            for t in (F(0),F(1,2),F(2)):
                for u in product((F(0),F(1,3),F(1)),repeat=4):
                    reconstructed=F(0)
                    for e,c in coeffs.items():
                        term=c*t**e[0]
                        for bit,v in zip(e[1:],u):
                            term*=v if bit else 1-v
                        reconstructed+=term
                    assert reconstructed==psi(parity,t,[F(f,2)+v/2 for f,v in zip(flags,u)])
                    checks+=1
            rows.append({'parity':parity,'flags':flags,'minimum':str(min(coeffs.values())),
                         'coefficients':{' '.join(map(str,e)):str(c) for e,c in coeffs.items()}})
    result={'regions':32,'coefficient_count':2048,'negative_coefficients':0,
            'reconstruction_evaluations':checks,'regions_data':rows}
    Path('round4/secondary_audit/independent_progression_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='regions_data'},indent=2))


if __name__=='__main__': main()
