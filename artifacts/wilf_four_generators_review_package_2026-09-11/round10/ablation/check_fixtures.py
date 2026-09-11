"""Direct set-membership check of the two exact ablation failures."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent

def plus(x,i,n=1):
    y=list(x);y[i]+=n;return tuple(y)

def verify(name):
    record=json.loads((ROOT/name).read_text())
    T={tuple(x) for x in record['points']};m=len(T)
    assert len(record['points'])==m==record['m']
    for x in T:
        for i in range(3):
            if x[i]:
                assert plus(x,i,-1) in T
    n=[max(x[i] for x in T)+1 for i in range(3)]
    excluded=[]
    for x in product(*(range(ni+1) for ni in n)):
        if x not in T and all(plus(x,i,-1) in T for i in range(3) if x[i]):
            excluded.append(x)
    full=[x for x in excluded if all(x)]
    assert full==[tuple(record['corner'])]
    p=full[0];R=max(map(sum,T));assert R<=6
    E={x for x in T if all(plus(x,i) in T for i in range(3))}
    erosion=len(E)+sum(sum(x[i]==0 for x in E) for i in range(3))
    assert erosion==record['erosion']
    surface=[{x for x in T if plus(x,i) not in T} for i in range(3)]
    Q=[len(surface[1]&surface[2]),len(surface[0]&surface[2]),len(surface[0]&surface[1])]
    assert all(Q[i]<=2*n[i] for i in range(3))
    U=U2=0
    for i in range(3):
        for t in surface[i]:
            top=max(sum(x) for x in T if all(x[j]>=t[j] for j in range(3)))
            delta=top-sum(t)
            U+=(t[i]+1)*delta
            U2+=(t[i]+1)*min(delta,2)
    assert U==record['gain']
    s=[sum(x[i] for x in T) for i in range(3)]
    q=[ni-1 for ni in n]
    G=max(q)*(3*m-4*sum(Fraction(s[i],q[i]) for i in range(3)))
    assert G==Fraction(record['axis_gain_numerator'],record['axis_gain_denominator'])
    plane=[]
    for i,j,k in ((0,1,2),(0,2,1),(1,2,0)):
        corners=[x for x in excluded if x[i]>0 and x[j]>0 and x[k]==0]
        plane.append({'coordinates':[i,j], 'mixed_corners':corners,
                      'count':len(corners),'total_count_bound':sum(p)-2,
                      'dominating_count':sum(x[i]>=p[i] and x[j]>=p[j] for x in corners),
                      'dominating_bound':p[k]})
    assert any(row['count']>row['total_count_bound'] for row in plane)
    return {'fixture':name,'m':m,'degree':R,'unique_full_corner':p,
            'erosion':erosion,'pair_surface_counts':Q,'axis_lengths':n,
            'U':U,'U2':U2,'G':str(G),'plane_corner_counts':plane,
            'interpretation':'Failure of the two selected witness formulas only; not a counterexample to the centroid inequality or Wilf.'}

result={'status':'passed','arithmetic':'integer sets and exact fractions',
        'fixtures':[verify('only_surface_first_failure.json'),
                    verify('only_surface_weak_first_failure.json')]}
(ROOT/'fixture_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
