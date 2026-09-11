"""Independent height-array enumeration of fixed-parameter one-corner DP."""
from pathlib import Path
from one_corner_dp import maximize
import json

def brute(weights,M,p):
    nx=M//weights[0]+1;ny=M//weights[1]+1
    h=[[0]*ny for _ in range(nx)]
    best=None;size=0;count=0
    def rec(k,card,moment):
        nonlocal best,size,count
        if k==nx*ny:
            if card:
                count+=1;score=4*moment+card*(1-3*M)
                if best is None or (score,card)>(best,size):best,size=score,card
            return
        i,j=divmod(k,ny)
        cap=max(0,(M-weights[0]*i-weights[1]*j)//weights[2]+1)
        if i:cap=min(cap,h[i-1][j])
        if j:cap=min(cap,h[i][j-1])
        if i and j:
            bound=min(h[i-1][j],h[i][j-1]);options=[0]
            if 0<bound<=cap:options.append(bound)
            if (i,j)==p[:2] and 0<p[2]<bound and p[2]<=cap:options.append(p[2])
        else:options=range(cap+1)
        for z in options:
            h[i][j]=z
            rec(k+1,card+z,moment+z*(weights[0]*i+weights[1]*j)+weights[2]*z*(z-1)//2)
    rec(0,0,0)
    dp=maximize(weights,M,p)
    assert (best,size)==(dp['maximum'],dp['maximizer_size']),(weights,M,p,best,size,dp)
    return dict(weights=weights,M=M,p=p,enumerated_ideals=count,best=best,size=size,agreement=True)

cases=[((1,1,1),3,(1,1,1)),((1,1,1),4,(1,1,1)),((1,1,1),4,(1,1,2)),((2,3,5),9,(1,1,1)),((2,3,3),10,(1,1,2))]
rows=[brute(*case) for case in cases]
result={'scope':'independent finite implementation audit, not universal one-corner theorem','cases':rows}
Path(__file__).with_name('independent_one_corner_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
