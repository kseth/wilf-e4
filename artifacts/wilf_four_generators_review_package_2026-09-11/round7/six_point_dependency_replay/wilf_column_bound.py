"""Exact diagnostics for the column-thickness theorem in every e>=4.

The theorem is proved in the accompanying note, not by the bounded checks here.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
from heapq import heappop,heappush
from pathlib import Path
import json,random


def column_heights(T,j):
    out=defaultdict(int)
    for x in T:
        key=tuple(v for k,v in enumerate(x) if k!=j)
        out[key]=max(out[key],x[j]+1)
    return dict(out)


def elongate(T,j,t):
    h=column_heights(T,j)
    out=set()
    for u,height in h.items():
        for v in range(height+t):out.add(u[:j]+(v,)+u[j:])
    return out


def deficit(T,a):
    m=len(T);d=len(a)
    w=[sum(u*v for u,v in zip(x,a)) for x in T]
    return d*m*max(w)-(d+1)*sum(w),max(w),sum(w)


def apery_nd(m,a):
    d=len(a)
    best=[None]*m;best[0]=(0,(0,)*d)
    heap=[(0,(0,)*d,0)]
    while heap:
        w,x,r=heappop(heap)
        if best[r]!=(w,x):continue
        for j,aj in enumerate(a):
            y=tuple(v+(i==j) for i,v in enumerate(x));rr=(r+aj)%m
            cand=(w+aj,y)
            if best[rr] is None or cand<best[rr]:
                best[rr]=cand;heappush(heap,(*cand,rr))
    assert all(v is not None for v in best)
    return best


def main():
    rng=random.Random(20260907)
    checks=0
    for d in range(3,6):
        for _ in range(30):
            tops=[tuple(rng.randrange(3) for j in range(d)) for i in range(rng.randint(2,7))]
            T0={x for v in tops for x in product(*(range(c+1) for c in v))}
            j=rng.randrange(d);h=column_heights(T0,j);A=len(h);m0=len(T0)
            s=Q(m0,A);t=(m0+A-1)//A+rng.randrange(4)
            T=elongate(T0,j,t);m=len(T)
            a=tuple(m+1+rng.randrange(m) for k in range(d));b=a[j]
            D0,M0,S0=deficit(T0,a)
            D,M,S=deficit(T,a)
            sf=sum(sum(x*aa for x,aa in zip(u,a[:j]+a[j+1:])) for u in h)
            F=(d-1)*t*t-2*s*t+2*t-(d-1)*s
            factored=(t-s)*((d-1)*t+(d-3)*s+2)+(d-3)*s*(s-1)
            assert F==factored>=0
            assert M==M0+b*t and S==S0+b*t*m0+t*sf+b*A*t*(t-1)//2
            assert D==D0+t*(d*A*M0-b*m0-(d+1)*sf+Q(d+1,2)*A*b)+Q(d-1,2)*A*b*t*t
            assert D>=Q(d-1,2)*m*(m+1)
            assert 2*len(column_heights(T,j))*(min(column_heights(T,j).values())-1)>=m
            checks+=1
    examples=[]
    for d in range(3,8):
        m=2**d;a=tuple(3**j*2**(d-j) for j in range(1,d+1))
        best=apery_nd(m,a);T={x for _,x in best}
        assert T==set(product(range(2),repeat=d))
        assert all(not any(g>v and g-v>=best[(g-v)%m][0] for v in (m,*a) if v<g)
                   for g in a)
        c=max(w for w,x in best)-m+1;g=sum(w//m for w,x in best)
        W=(d+1)*(c-g)-c
        assert W>=d-1
        examples.append(dict(e=d+1,generators=[m,*a],m=m,c=c,W=W,
                             A=m//2,min_column_length=2))
    a=(31,42,49);m=28;best=apery_nd(m,a);T={x for _,x in best}
    c=max(w for w,x in best)-m+1;g=sum(w//m for w,x in best)
    H=column_heights(T,0)
    assert len(H)==4 and set(H.values())=={7}
    assert 4*(c-g)-c>=2
    examples.append(dict(e=4,generators=[m,*a],m=m,c=c,W=4*(c-g)-c,
                         A=len(H),min_column_length=min(H.values())))
    # A genuine nonuniform staircase: the theorem does not require a prism.
    m=126;a=(127,2569,3615);best=apery_nd(m,a);T={x for _,x in best}
    assert all(not any(g>v and g-v>=best[(g-v)%m][0] for v in (m,*a) if v<g)
               for g in a)
    H=column_heights(T,0)
    assert sorted(H.values())==[38,39,49]
    c=max(w for w,x in best)-m+1;g=sum(w//m for w,x in best)
    W=4*(c-g)-c
    assert c==8316 and W==7060 and 2*len(H)*(min(H.values())-1)>=m
    examples.append(dict(e=4,generators=[m,*a],m=m,c=c,W=W,A=len(H),
                         column_lengths=sorted(H.values()),
                         min_column_length=min(H.values())))
    result=dict(status='PASS',random_identity_checks=checks,examples=examples,
                scope='Analytic sufficient theorem for e>=4; not unrestricted Wilf')
    Path('column_bound_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)


if __name__=='__main__':main()
