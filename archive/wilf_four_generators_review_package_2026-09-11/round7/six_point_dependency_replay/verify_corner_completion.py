"""Independent exhaustive bounded reference check of the completion criterion."""
from itertools import product,combinations
from pathlib import Path
import json
from wilf_reassessment import corners,maximal
from wilf_six_point import one_corner_completion,build_completion


def main():
    # A proper completion is essential here: U itself has two interior corners.
    z=((0,1,3),(0,2,2),(1,0,3),(1,2,1),(2,0,2),(3,1,0))
    from wilf_work import lower_hull
    U=lower_hull(z);r=one_corner_completion(z);completed=build_completion(z,r)
    assert r['feasible'] and r['corner']==(1,1,2)
    assert len(U)==25 and completed-U=={(2,1,1)}
    assert [p for p in corners(U) if all(p)]==[(1,1,2),(2,1,1)]
    assert [p for p in corners(completed) if all(p)]==[(1,1,2)]
    assert set(z)<=set(maximal(completed))
    rows=[r for r in product(range(4),repeat=3) if r[0]>=r[1]>=r[2]]
    ideals=[];possible=set();valid=0
    for h in product(rows,repeat=3):
        if not all(h[i][j]>=h[i+1][j] for i in range(2) for j in range(3)):continue
        T={(i,j,k) for i,j in product(range(3),repeat=2) for k in range(h[i][j])}
        if not T:continue
        z=tuple(maximal(T));ideals.append((T,z))
        if len([p for p in corners(T) if all(p)])<=1:
            valid+=1
            for n in range(1,len(z)+1):
                possible.update(frozenset(s) for s in combinations(z,n))
    assert len(ideals)==979
    accepted=0
    for T,z in ideals:
        r=one_corner_completion(z)
        assert r['feasible']==(frozenset(z) in possible)
        stretched=tuple((x*x+3*x+1,7*y+3,2*w*w+w+4) for x,y,w in z)
        assert one_corner_completion(stretched)['feasible']==r['feasible']
        if r['feasible']:
            completed=build_completion(z,r)
            assert T<=completed and set(z)<=set(maximal(completed))
            assert len([p for p in corners(completed) if all(p)])<=1
            accepted+=1
    result=dict(status='PASS',nonempty_ideals=979,ideals_with_at_most_one_interior_corner=valid,
                maximal_sets_admitting_completion=accepted,stretch_invariance_checks=979,
                proper_completion_example=dict(Z=z,U_size=25,completion_size=26,
                                               added_point=(2,1,1),interior_corner=(1,1,2)),
                scope='Bounded check; the general theorem has an analytic proof')
    Path('corner_completion_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)


if __name__=='__main__':main()
