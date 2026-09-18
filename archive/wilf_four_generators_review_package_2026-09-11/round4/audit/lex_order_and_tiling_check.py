"""Exact counterexamples to a lex-order shortcut, plus a tiling obstruction."""
from heapq import heappush,heappop
from itertools import permutations,product
import json

def certify(gens,expected_corner):
    m,*a=gens
    w=[None]*m;w[0]=0;heap=[(0,0)]
    while heap:
        val,r=heappop(heap)
        if w[r]!=val:continue
        for b in a:
            s=(r+b)%m;c=val+b
            if w[s] is None or c<w[s]:
                w[s]=c;heappush(heap,(c,s))
    assert all(v is not None for v in w)
    contains=lambda v:v>=0 and v>=w[v%m]
    assert not any(contains(b-c) for b in gens for c in gens if c<b)
    fact={}
    for val in w:
        fact[val]=[x for x in product(*(range(val//b+1) for b in a))
                   if sum(b*v for b,v in zip(a,x))==val]
        assert len(fact[val])==1
    T={xs[0] for xs in fact.values()}
    for order in permutations(range(3)):
        selected={min(xs,key=lambda x:tuple(x[i] for i in order))
                  for xs in fact.values()}
        assert selected==T
    p=expected_corner
    assert p not in T
    for j in range(3):
        z=list(p);z[j]-=1;assert tuple(z) in T
    maxs=tuple(max(x[i] for x in T)+1 for i in range(3))
    full=[]
    for p in product(*(range(1,z+1) for z in maxs)):
        if p in T:continue
        if all(tuple(v-(i==j) for i,v in enumerate(p)) in T for j in range(3)):
            full.append(p)
    assert full==[expected_corner]
    c=max(w)-m+1;g=sum(v//m for v in w);n=c-g
    Z=sorted(x for val,xs in fact.items() for x in xs if max(w)-val<m)
    return dict(gens=gens,apery=sorted(w),T=sorted(T),full_corner=expected_corner,
                all_apery_factorizations_unique=True,lex_orders_checked=6,c=c,n=n,W4=4*n-c,
                final_window_points=Z,final_window_count=len(Z))

examples=[certify((7,8,9,11),(1,1,1)),certify((11,12,14,17),(2,1,1)),
          certify((155,1552,1647,1651),(1,7,4))]
assert (examples[2]['c'],examples[2]['n'],examples[2]['W4'],examples[2]['final_window_count'])==(17979,6865,9481,7)
T={p for p in product(range(30),repeat=3)
   if max(p[0]+p[1],p[0]+p[2],p[1]+p[2])<=29 and min(p)<=3}
B={(0,0,0),(1,0,0),(0,1,0),(0,0,1)}
A={p for p in T if all(tuple(x+y for x,y in zip(p,q)) in T for q in B)}
E={tuple(x-y for x,y in zip(p,q)) for p in A for q in B}
assert (len(T),len(A),len(E))==(4246,3241,4546)
assert len(E)>len(T)
print(json.dumps(dict(status='exact checks passed',examples=examples,
    tiling_obstruction=dict(T=len(T),erosion=len(A),difference=len(E),excess=len(E)-len(T))),indent=2))
