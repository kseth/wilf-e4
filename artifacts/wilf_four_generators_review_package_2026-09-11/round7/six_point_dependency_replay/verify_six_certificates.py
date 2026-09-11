"""Check the six-point certificates using the Python standard library only.

This verifies arithmetic soundness of the stored certificates. Completeness of
the enumeration also uses the analytic reductions and the generator programs.
"""
from fractions import Fraction as Q
from itertools import permutations
from pathlib import Path
import json


def tops(T):
    return {x for x in T if all(tuple(v+(i==j) for i,v in enumerate(x)) not in T
                               for j in range(3))}


def verify_lp(T,cert,ordered):
    m=len(T);sums=[sum(x[j] for x in T) for j in range(3)]
    cost=[-4*s for s in sums]+[3*m]
    if ordered:
        allowed={((1,0,0,0),m+1),((-1,1,0,0),1),((0,-1,1,0),1)}
        bound=Q(cert['D_min'])
    else:
        allowed={((1,0,0,0),1),((0,1,0,0),1),((0,0,1,0),1)}
        bound=Q(cert['eta'])
    allowed|={(tuple(-v for v in x)+(1,),0) for x in tops(T)}
    lhs=[Q(0)]*4;rhs=Q(0)
    for item in cert['active_dual']:
        row=tuple(item['row']);b=item['rhs'];y=Q(item['value'])
        assert (row,b) in allowed and y>=0
        lhs=[v+y*u for v,u in zip(lhs,row)];rhs+=y*b
    assert lhs==cost and rhs==bound
    primal=list(map(Q,cert['weights']))+[Q(cert['M'])]
    assert all(sum(v*w for v,w in zip(row,primal))>=b for row,b in allowed)
    assert sum(v*w for v,w in zip(cost,primal))==bound
    return bound-m*(m-1) if ordered else (m+1)*bound-m*(m-1)


def main():
    shapes=json.loads(Path('six_candidate_shapes.json').read_text())
    labels=json.loads(Path('six_residue_labels.json').read_text())
    data=json.loads(Path('six_arithmetic_results.json').read_text())
    for rec in shapes:
        T={tuple(x) for x in rec['T']};m=len(T)
        assert m==rec['m'] and m<=56
        assert all(tuple(int(i==j) for i in range(3)) in T for j in range(3))
        for x in T:
            for j in range(3):
                if x[j]:assert tuple(v-(i==j) for i,v in enumerate(x)) in T
        B=sum(len({tuple(x[i] for i in range(3) if i!=j) for x in T}) for j in range(3))
        for zz in rec['Zs']:
            Z={tuple(x) for x in zz}
            assert len(Z)==6 and Z<=tops(T)
            E=sum(map(sum,Z))-sum(max(x[j] for x in Z) for j in range(3))
            assert B-18-E<0
    expected={(i,a,b,c) for i,a,b,c in labels}
    assert len(expected)==len(labels)==930
    assert {g['shape'] for g in data['geometric_records']}=={r[0] for r in labels}
    normalized=ordered=0
    for g in data['geometric_records']:
        T={tuple(x) for x in shapes[g['shape']]['T']}
        margin=verify_lp(T,g['geometric'],False)
        if margin>=0:
            normalized+=1
        else:
            assert {tuple(p['permutation']) for p in g['ordered']}==set(permutations(range(3)))
            for p in g['ordered']:
                TT={tuple(x[j] for j in p['permutation']) for x in T}
                assert verify_lp(TT,p['certificate'],True)>=0
                ordered+=1
    got=set();cuts=0;min_slack=None
    for r in data['boundary_records']:
        idx=r['shape'];a=r['A'];T={tuple(x) for x in shapes[idx]['T']};m=len(T)
        assert len({sum(v*w for v,w in zip(a,x))%m for x in T})==m
        lines=[]
        for x in T:
            for j in range(3):
                if tuple(v+(i==j) for i,v in enumerate(x)) not in T:
                    lines.append((x[j]+1,sum(v*w for v,w in zip(a,x))%m))
        slacks=[sum(L*((f-res)%m) for L,res in lines)-m*(m-1) for f in range(m)]
        assert slacks==r['slacks'] and min(slacks)>=0
        min_slack=min(slacks) if min_slack is None else min(min_slack,min(slacks))
        cuts+=m;got.add((idx,*a))
    assert got==expected and cuts==23002 and normalized==67 and ordered==24
    result=dict(status='PASS',scope='Finite certificates for the |Z|=6 theorem',
        normalized_certificates=normalized,ordered_certificates=ordered,
        residue_labelings=len(labels),modular_cut_checks=cuts,minimum_modular_slack=min_slack)
    Path('six_certificate_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)


if __name__=='__main__':main()
