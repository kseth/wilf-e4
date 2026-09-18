"""Independent finite-difference audit of the ordinary-three family certificate.

Uses only the standard library.  No code is imported from the proposal.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

BITS = list(product((0, 1), repeat=4))


def expression(values, fvalues):
    x, y, X, Y = map(F, values)
    fx, fy, fX, fY = map(F, fvalues)
    Q = 2*x + 1 + (x+1)*y
    P = 2*X + 1 + (X+1)*Y
    A = 4*x+x*y+y/2+8-fx*(4+y)-fy*(2*x+3)
    B = 4*X+X*Y+Y/2+8-fX*(4+Y)-fY*(2*X+3)
    return P*A+Q*B-4*(x*X+x+X+4)


def uncollected(values, eps):
    x, y, X, Y = map(F, values)
    eh, ev, eH, eV = map(F, eps)
    Q = 2*x+1+(x+1)*y
    P = 2*X+1+(X+1)*Y
    FA = (4+y)*(2*x+3)-eh*(4+y)-ev*(2*x+3)
    FB = (4+Y)*(2*X+3)-eH*(4+Y)-eV*(2*X+3)
    return (P*FA+Q*FB-2*P*Q+4*P*(x+3)+4*Q*(X+3)
            -4*(x*X+x+X+4)
            -F(3,2)*(P*(4*x+y+10)+Q*(4*X+Y+10)))


def region(flags, t):
    values = [F(u)+flag for flag, u in zip(flags,t)]
    fs = [F(1) if flag else F(u) for flag,u in zip(flags,t)]
    return expression(values,fs)


def coefficient(flags, exponents):
    """Bounded coordinates evaluate at endpoints; upper coordinates difference."""
    differentiated = [i for i in range(4) if flags[i] and exponents[i]]
    answer = F(0)
    for subset in product((0,1),repeat=len(differentiated)):
        t = [0 if flags[i] else exponents[i] for i in range(4)]
        for i, bit in zip(differentiated, subset):
            t[i] = bit
        answer += (-1)**(len(subset)-sum(subset))*region(flags,t)
    return answer


def reconstructed(flags, coefficients, t):
    total = F(0)
    for exponent, coeff in coefficients.items():
        term = coeff
        for flag, e, u in zip(flags,exponent,t):
            term *= u if e else (1 if flag else 1-u)
        total += term
    return total


def main():
    # Both sides are separately affine in all eight formal variables.
    # Therefore equality at the 256 Boolean vertices is an identity proof.
    for values in BITS:
        for eps in BITS:
            assert uncollected(values,eps) == expression(values,eps)

    existing = json.loads(Path('round4/secondary/ordinary_three_certificate.json').read_text())
    existing = {tuple(row['flags']):row for row in existing}
    rows=[]
    reconstruction_tests=0
    for flags in BITS:
        coefficients = {e:coefficient(flags,e) for e in BITS}
        assert min(coefficients.values()) >= 0
        for e, coefficient_value in coefficients.items():
            assert F(existing[flags]['coefficients'][' '.join(map(str,e))]) == coefficient_value
        # The independently collected polynomial is separately affine.
        # Boolean reconstruction is thus sufficient; include off-grid values too.
        for t in product((F(0),F(1),F(1,3),F(2)),repeat=4):
            assert region(flags,t) == reconstructed(flags,coefficients,t)
            reconstruction_tests += 1
        rows.append({'flags':flags,'minimum':str(min(coefficients.values())),
                     'coefficients':{' '.join(map(str,e)):str(c) for e,c in coefficients.items()}})

    # Since every type contains all integers >=3, checking below 3 suffices
    # for sumset genus and dual identities.  Negative labels are never members.
    holes=({1,2},{1},{2},set())
    frobenius=(2,1,2,-1)
    dual=(2,1,0,3)
    def member(i,n): return n>=0 and n not in holes[i]
    genus=[]
    for i in range(4):
        assert {n for n in range(3) if member(i,frobenius[i]-n)} == holes[dual[i]]
        row=[]
        for j in range(4):
            row.append(sum(not any(member(i,u) and member(j,n-u)
                                   for u in range(n+1)) for n in range(3)))
        genus.append(row)
    assert genus==[[2,1,1,0],[1,1,0,0],[1,0,0,0],[0,0,0,0]]

    result={'normalization_identity_boolean_vertices':256,
            'regions':16,'coefficient_count':256,'negative_coefficients':0,
            'reconstruction_evaluations':reconstruction_tests,
            'sumset_genus_matrix':genus,'regions_data':rows}
    output=Path('round4/secondary_audit/independent_certificate.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='regions_data'},indent=2))


if __name__=='__main__': main()
