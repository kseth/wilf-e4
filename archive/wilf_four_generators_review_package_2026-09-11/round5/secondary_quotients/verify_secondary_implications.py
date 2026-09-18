"""Exact finite checks accompanying the analytic implication audit.

This checks the degree-four cardinality bound and a sharp m=35 example.
It does not replace the interval certificate, phase proof, or structural proof.
"""
import heapq
import json
from math import prod
from pathlib import Path


def cardinality_bound(R, center):
    result=prod(x+1 for x in center)
    for axis in range(3):
        j,k=[i for i in range(3) if i!=axis]
        for t in range(center[axis]+1,R+1):
            result+=max((u+1)*(v+1)
                        for u in range(center[j]+1)
                        for v in range(center[k]+1)
                        if u+v<=R-t)
    return result


def apery(gens):
    m=min(gens);dist=[None]*m;dist[0]=0;heap=[(0,0)]
    while heap:
        value,residue=heapq.heappop(heap)
        if value!=dist[residue]:continue
        for g in gens:
            nr=(residue+g)%m;nv=value+g
            if dist[nr] is None or nv<dist[nr]:
                dist[nr]=nv;heapq.heappush(heap,(nv,nr))
    assert all(v is not None for v in dist)
    return dist


def member(n, ap):
    return n>=0 and n>=ap[n%len(ap)]


def side(a,b,q):
    ap=apery((a,b));F=a*b-a-b
    gaps=[z for z in range(1,F//q+1) if not member(q*z,ap)]
    violations=[z for z in range(1,a*b//q+2)
                if member(q*z,ap) and not member(q*z-a-b,ap)]
    return {'a':a,'b':b,'quotient_divisor':q,'quotient_gaps':gaps,
            'interior_violations':violations}


def main():
    centers=[(a,b,c) for a in range(5) for b in range(5-a)
             for c in range(5-a-b)]
    values=[cardinality_bound(4,c) for c in centers]
    assert max(values)==29
    A=side(5,6,7);B=side(5,7,8)
    assert A['quotient_gaps']==B['quotient_gaps']==[1,2]
    assert not A['interior_violations'] and not B['interior_violations']
    gens=(35,40,48,49)
    assert all(not member(g,apery(gens[:i]+gens[i+1:]))
               for i,g in enumerate(gens))
    ap=apery(gens);m=min(gens);F=max(ap)-m
    numer=2*sum(ap)-m*(m-1);assert numer%(2*m)==0
    genus=numer//(2*m);W=3*(F+1)-4*genus
    assert W>0
    out={'degree4_central_triples':len(centers),'degree4_max_cardinality':max(values),
         'maximizers':[c for c,v in zip(centers,values) if v==29],
         'sharp_secondary_m35_example':{'generators':gens,'side_A':A,'side_B':B,
           'multiplicity':m,'Frobenius':F,'genus':genus,'W4':W}}
    path=Path(__file__).with_name('secondary_implication_checks.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))

if __name__=='__main__':main()
