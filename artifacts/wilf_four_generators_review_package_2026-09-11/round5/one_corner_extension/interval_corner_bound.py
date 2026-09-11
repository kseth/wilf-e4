"""Exact box upper bounds for all one-interior-corner ideals.

This extension is separate from the audited no-interior certificate.
"""
from itertools import product


def stats(weights,p,axis,t,u,v):
    other=[i for i in (0,1,2) if i!=axis]
    al=weights[axis]; be,ga=[weights[i] for i in other]
    pj,pk=[p[i] for i in other]
    n=(u+1)*(v+1); twice_sum=n*(2*al*t+be*u+ga*v)
    height=al*t+be*u+ga*v
    if t>=p[axis] and u>=pj and v>=pk:
        removed=(u-pj+1)*(v-pk+1)
        n-=removed; twice_sum-=removed*(2*al*t+be*(pj+u)+ga*(pk+v))
        height=al*t+max(be*(pj-1)+ga*v,be*u+ga*(pk-1))
    return n,twice_sum,height


def central_stats(weights,p,c):
    n=(c[0]+1)*(c[1]+1)*(c[2]+1)
    height=sum(a*x for a,x in zip(weights,c)); twice_sum=n*height
    if all(x>=pi for x,pi in zip(c,p)):
        removed=(c[0]-p[0]+1)*(c[1]-p[1]+1)*(c[2]-p[2]+1)
        n-=removed; twice_sum-=removed*sum(a*(x+pi) for a,x,pi in zip(weights,c,p))
        height=max(sum(a*((pi-1) if j==i else x) for j,(a,x,pi) in enumerate(zip(weights,c,p))) for i in (0,1,2))
    return n,twice_sum,height


def corner_bound(lower,upper,q,p):
    lw=(q,lower[0],lower[1]); uw=(q,upper[0],upper[1])
    caps=[upper[2]//a for a in lw]; horns=[]
    for axis in (0,1,2):
        other=[i for i in (0,1,2) if i!=axis]
        n=caps[axis]+1; nb,nc=[caps[i]+1 for i in other]
        H=[[[0]*nc for _ in range(nb)] for _ in range(n+1)]
        for t in range(n-1,-1,-1):
            for u in range(nb):
                for v in range(nc):
                    val=0
                    count,_,height=stats(lw,p,axis,t,u,v)
                    if height<=upper[2]:
                        count2,twice_sum,_=stats(uw,p,axis,t,u,v)
                        assert count==count2
                        val=max(val,2*twice_sum+count*(q-3*lower[2])+H[t+1][u][v])
                    if u:val=max(val,H[t][u-1][v])
                    if v:val=max(val,H[t][u][v-1])
                    H[t][u][v]=val
        horns.append(H)
    best=None
    for c in product(*(range(n+1) for n in caps)):
        count,_,height=central_stats(lw,p,c)
        if height>upper[2]:continue
        _,twice_sum,_=central_stats(uw,p,c)
        val=2*twice_sum+count*(q-3*lower[2])
        val+=horns[0][c[0]+1][c[1]][c[2]]+horns[1][c[1]+1][c[0]][c[2]]+horns[2][c[2]+1][c[0]][c[1]]
        best=val if best is None else max(best,val)
    return best


def all_corners_bound(lower,upper,q):
    # Actual minimal p has a.p-a_min<=M, since all predecessors are in T.
    weights=(q,lower[0],lower[1]); cap=upper[2]+q
    rows=[]
    for p in product(*(range(1,cap//a+1) for a in weights)):
        if sum(a*x for a,x in zip(weights,p))<=cap:
            rows.append((corner_bound(lower,upper,q,p),p))
    return max(rows),len(rows)


if __name__=='__main__':
    import json,time
    from pathlib import Path
    cases=[((100,100,700),(101,101,710),100),((100,100,700),(105,105,710),100),((100,100,700),(101,101,750),100)]
    out=[]
    for lower,upper,q in cases:
        start=time.time(); maximum,n=all_corners_bound(lower,upper,q)
        row={'lower':lower,'upper':upper,'scale':q,'maximum':maximum,'corners_checked':n,'seconds':time.time()-start}
        out.append(row);print(row,flush=True)
    Path(__file__).with_name('initial_closed_box_checks.json').write_text(json.dumps(out,indent=2)+'\n')
