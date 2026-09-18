"""Exact finite sanity checks for the analytic proofs, not a coverage theorem."""
from fractions import Fraction as F
from itertools import product, permutations
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]

def moments(T):
    return tuple(sum(x[i] for x in T) for i in range(3))

def clipped_box_checks():
    checked = 0
    for n in product(range(2, 7), repeat=3):
        for p in product(*(range(1, ni) for ni in n)):
            T = {x for x in product(*(range(ni) for ni in n))
                 if not all(xi >= pi for xi, pi in zip(x, p))}
            m, s = len(T), moments(T)
            q = tuple(ni-pi for ni, pi in zip(n, p))
            Q = q[0]*q[1]*q[2]
            vertices = [tuple(pj-1 if j == i else nj-1
                        for j, (pj, nj) in enumerate(zip(p, n))) for i in range(3)]
            assert all(v in T for v in vertices)
            z = tuple(sum(v[i] for v in vertices)/F(3) for i in range(3))
            residual = tuple(3*m*z[i]-4*s[i] for i in range(3))
            expected = tuple(m*(p[i]-1)+2*Q*p[i] for i in range(3))
            assert residual == expected
            assert min(residual) >= 0 and sum(residual) >= m-1
            if sum(p) >= 4:
                assert sum(residual) >= m
            checked += 1
    return checked

def profiles(max_axis=5):
    def rec(rows):
        if len(rows) == max_axis:
            if rows[0]:
                yield tuple(rows)
            return
        cap = rows[-1] if rows else max_axis
        for length in range(cap+1):
            yield from rec(rows+[length])
    yield from rec([])

def prism_checks():
    checked = admitted = 0
    for profile in profiles():
        P = {(i,j) for i, length in enumerate(profile) for j in range(length)}
        u = len(P)
        for a,b in P:
            if not a or not b:
                continue
            L = {(i,j) for i,j in P if i < a or j < b}
            v = len(L)
            sP = [sum(x[i] for x in P) for i in range(2)]
            sL = [sum(x[i] for x in L) for i in range(2)]
            zP = tuple(F(3*sP[i],2*u) for i in range(2))
            zL = tuple(F(3*sL[i],2*v) for i in range(2))
            for h in range(1,5):
                for n in range(h+1,7):
                    q=n-h
                    T={(i,j,k) for i,j in P for k in range(n)
                       if not (i>=a and j>=b and k>=h)}
                    m,s=len(T),moments(T)
                    alpha,beta=F(8*h*u,9*m),F(8*q*v,9*m)
                    z=(alpha*zP[0]+beta*zL[0]+F(a,9),
                       alpha*zP[1]+beta*zL[1]+F(b-1,9),
                       alpha*(h-1)+beta*(n-1)+F(n-1,9))
                    A=h*u*(n+2*h-3)+3*q*v*(n-2*h-1)
                    residual=tuple(3*m*z[i]-4*s[i] for i in range(3))
                    assert residual==(F(m*a,3),F(m*(b-1),3),F(A,3))
                    case=(h>=3 or
                          h==2 and n>=4 and a+b>=3 or
                          h==2 and n==3 and (a+b>=4 or a+b==3 and 7*v<=6*u) or
                          h==1 and n>=3 and a+b>=4)
                    if case:
                        assert min(residual)>=0 and sum(residual)>=m
                        admitted+=1
                    checked+=1
    return checked,admitted

def check_recorded_failures():
    path=ROOT/'round10/line_upgrade/upgrade_failures.jsonl'
    if not path.exists():
        return {'status':'failure file absent; optional probe skipped'}
    counts={'rows':0,'clipped_boxes':0,'clipped_prisms':0,'proved_prism_cases':0}
    for line in path.read_text().splitlines():
        row=json.loads(line)
        T={tuple(x) for x in row['points']}
        p=tuple(row['corner'])
        counts['rows']+=1
        n=tuple(max(x[i] for x in T)+1 for i in range(3))
        B={x for x in product(*(range(ni) for ni in n))
           if not all(xi>=pi for xi,pi in zip(x,p))}
        counts['clipped_boxes']+=T==B
        matched=proved=False
        for perm in permutations(range(3)):
            U={tuple(x[i] for i in perm) for x in T}
            a,b,h=(p[i] for i in perm)
            N=n[perm[2]]
            P={(x,y) for x,y,z in U if z==0}
            test={(x,y,z) for x,y in P for z in range(N)
                  if not(x>=a and y>=b and z>=h)}
            if test!=U:
                continue
            matched=True
            u=len(P);v=sum(x<a or y<b for x,y in P)
            proved|=(h>=3 or
                     h==2 and N>=4 and a+b>=3 or
                     h==2 and N==3 and (a+b>=4 or a+b==3 and 7*v<=6*u) or
                     h==1 and N>=3 and a+b>=4)
        counts['clipped_prisms']+=matched
        counts['proved_prism_cases']+=proved
    return counts

if __name__=='__main__':
    boxes=clipped_box_checks()
    prisms,admitted=prism_checks()
    result={'status':'passed','arithmetic':'exact fractions',
            'box_identity_checks':boxes,'prism_identity_checks':prisms,
            'prism_theorem_examples':admitted,
            'recorded_line_upgrade_failure_probe':check_recorded_failures(),
            'scope':'Finite sanity checks; the accompanying symbolic proofs establish the infinite families.'}
    output=Path(__file__).with_name('analytic_family_checks.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
