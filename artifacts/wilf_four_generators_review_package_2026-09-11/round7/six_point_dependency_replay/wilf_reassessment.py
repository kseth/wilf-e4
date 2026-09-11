"""Structural and exact-certificate diagnostics for the Wilf reassessment.

This is research code, not a proof of unrestricted Wilf. SciPy proposes an LP
solution; every reported LP optimum is checked using rational arithmetic.
"""
from fractions import Fraction as Q
from itertools import product, permutations, combinations
from collections import Counter
import json
import random

from wilf_work import apery


def corners(t):
    candidates={tuple(v+(i==j) for i,v in enumerate(x)) for x in t for j in range(3)}-t
    return sorted(x for x in candidates if all(
        tuple(v-(i==j) for i,v in enumerate(x)) in t for j in range(3) if x[j]))


def maximal(t):
    return sorted(x for x in t if all(tuple(v+(i==j) for i,v in enumerate(x)) not in t
                                    for j in range(3)))


def projected_grid_witness(z):
    """Find a complete 2-by-3 grid in an ordered coordinate projection."""
    for i,j in permutations(range(3),2):
        rows={x[i]:{y[j] for y in z if y[i]==x[i]} for x in z}
        for u,v in combinations(sorted(rows),2):
            common=sorted(rows[u]&rows[v])
            if len(common)>=3:
                return dict(coordinates=[i,j],rows=[u,v],columns=common[:3])
    return None


def reconstruct(t):
    c=corners(t)
    interior=[x for x in c if all(x)]
    if len(interior)>1:
        return None
    f={(x,y) for x,y,z in t if z==0}
    p={x:1+max(z for xx,y,z in t if xx==x and y==0) for x,y in f if y==0}
    q={y:1+max(z for x,yy,z in t if x==0 and yy==y) for x,y in f if x==0}
    shape=set()
    for x,y in f:
        h=min(p[x],q[y])
        if interior:
            a,b,c=interior[0]
            if x>=a and y>=b:h=min(h,c)
        shape.update((x,y,z) for z in range(h))
    assert shape==t
    return dict(F=sorted(f),p=sorted(p.items()),q=sorted(q.items()),interior=interior)


def exact_lp(cost,G,b):
    from scipy.optimize import linprog
    result=linprog(cost,A_ub=[[-v for v in r] for r in G],b_ub=[-v for v in b],
                   bounds=[(None,None)]*4,method='highs')
    assert result.success,result.message
    x=[Q(float(v)).limit_denominator(10**6) for v in result.x]
    dual=[Q(float(-v)).limit_denominator(10**6) for v in result.ineqlin.marginals]
    assert all(v>=0 for v in dual)
    assert all(sum(dual[i]*G[i][j] for i in range(len(G)))==cost[j] for j in range(4))
    assert all(sum(gj*xj for gj,xj in zip(row,x))>=bb for row,bb in zip(G,b))
    lower=sum(bb*y for bb,y in zip(b,dual))
    assert sum(v*y for v,y in zip(cost,x))==lower
    return lower,x,[dict(row=G[i],rhs=b[i],value=str(y)) for i,y in enumerate(dual) if y]


def geometric_optimum(t):
    m=len(t)
    sums=[sum(x[j] for x in t) for j in range(3)]
    tops=maximal(t)
    cost=[-4*s for s in sums]+[3*m]
    G=[(1,0,0,0),(0,1,0,0),(0,0,1,0)]+[tuple(-v for v in x)+(1,) for x in tops]
    b=[1,1,1]+[0]*len(tops)
    lower,x,dual=exact_lp(cost,G,b)
    return dict(m=m,eta=str(lower),weights=[str(v) for v in x[:3]],M=str(x[3]),
                sufficient=(m+1)*lower>=m*(m-1),
                margin=str((m+1)*lower-m*(m-1)),
                active_dual=dual)


def ordered_geometric_optimum(t):
    """Sufficient bound assuming coordinates correspond to a1<a2<a3."""
    m=len(t)
    sums=[sum(x[j] for x in t) for j in range(3)]
    tops=maximal(t)
    cost=[-4*s for s in sums]+[3*m]
    G=[(1,0,0,0),(-1,1,0,0),(0,-1,1,0)]+[tuple(-v for v in x)+(1,) for x in tops]
    b=[m+1,1,1]+[0]*len(tops)
    lower,x,dual=exact_lp(cost,G,b)
    return dict(m=m,D_min=str(lower),weights=[str(v) for v in x[:3]],M=str(x[3]),
                sufficient=lower>=m*(m-1),margin=str(lower-m*(m-1)),active_dual=dual)


def shape_from_pair_bounds(bounds,corner):
    xy,xz,yz=bounds
    limits=(min(xy,xz),min(xy,yz),min(xz,yz))
    return {x for x in product(*(range(v+1) for v in limits))
            if x[0]+x[1]<=xy and x[0]+x[2]<=xz and x[1]+x[2]<=yz
            and (corner is None or not all(v>=c for v,c in zip(x,corner)))}


def audit_semigroup(gens,lp=True):
    data=apery(gens)
    if data is None:return None
    m,a,best=data
    t={x for _,x in best}
    shape=reconstruct(t)
    assert shape is not None
    assert projected_grid_witness(maximal(t)) is None
    representative={w%m:x for w,x in best}
    boundary=[]
    for p in corners(t):
        label=sum(aj*x for aj,x in zip(a,p))
        q=representative[label%m]
        assert all(not(pj and qj) for pj,qj in zip(p,q))
        difference=label-sum(aj*x for aj,x in zip(a,q))
        assert difference>=0 and difference%m==0
        required_carry=int(q>p)
        assert difference//m>=required_carry
        boundary.append(dict(head=p,tail=q,carry=difference//m,
                             required_carry=required_carry))
    M=max(w for w,x in best)
    sigma=sum(w for w,x in best)
    c=M-m+1;g=sum(w//m for w,x in best)
    out=dict(gens=[m,*a],m=m,c=c,W=4*(c-g)-c,k=sum(M-w<m for w,x in best),
             interior=shape['interior'],corner_count=len(boundary),boundary=boundary)
    if lp:
        out['geometric']=geometric_optimum(t)
        out['ordered_geometric']=ordered_geometric_optimum(t)
    return out


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--random',type=int,default=0)
    parser.add_argument('--pair-shapes',type=int,default=0)
    args=parser.parse_args()
    fixed=[(25,26,30,31),(36,37,42,43),(49,50,56,57),(30,63,85,86),
           (100,101,103,107),(8,9,10,13),(19,20,25,27)]
    records=[audit_semigroup(g) for g in fixed]
    for r in records:print(json.dumps({k:v for k,v in r.items() if k!='boundary'}),flush=True)
    rng=random.Random(20260906)
    random_records=[]
    for i in range(args.random):
        m=rng.randint(20,300)
        span=(max(5,int(m**0.5)*3) if i%2 else 5*m)
        a=sorted(rng.sample(range(m+1,m+span),3))
        r=audit_semigroup([m,*a])
        if r is not None:random_records.append(r)
    bad_shapes=[]
    largest_bad=None
    for _ in range(args.pair_shapes):
        d=rng.randint(2,22)
        bounds=tuple(d+rng.randint(-d//3,d//3) for j in range(3))
        corner=tuple(rng.randint(1,max(1,d//2)) for j in range(3)) if rng.random()<0.85 else None
        t=shape_from_pair_bounds(bounds,corner)
        if len(t)<4:continue
        assert reconstruct(t) is not None
        r=geometric_optimum(t)
        if not r['sufficient']:
            r.update(bounds=bounds,corner=corner)
            bad_shapes.append(r)
            if largest_bad is None or r['m']>largest_bad['m']:largest_bad=r
    result=dict(fixed=records,random=random_records,pair_shape_attempts=args.pair_shapes,
                geometric_failure_shapes=bad_shapes)
    with open('reassessment-results.json','w') as f:json.dump(result,f,indent=2)
    print(json.dumps(dict(random_proposals=args.random,random_semigroups=len(random_records),
        random_geometric_passes=sum(r['geometric']['sufficient'] for r in random_records),
        random_geometric_failures=[r['gens'] for r in random_records if not r['geometric']['sufficient']],
        pair_shape_attempts=args.pair_shapes,geometric_failure_shape_count=len(bad_shapes),
        largest_bad=largest_bad)),flush=True)
