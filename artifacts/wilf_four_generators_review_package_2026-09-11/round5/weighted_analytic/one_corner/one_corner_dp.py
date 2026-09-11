"""Exact fixed-parameter DP for at most one full-support excluded corner.

T = U \\ (p+N^3), U a no-interior lower ideal. Arithmetic is integral.
No finite parameter run is a theorem for all weights or heights.
"""
from itertools import product
from pathlib import Path
import json

def slice_stats(weights,p,axis,t,u,v):
    js=[j for j in range(3) if j!=axis]
    al=weights[axis]; be,ga=(weights[j] for j in js)
    pj,pk=(p[j] for j in js)
    n=(u+1)*(v+1)
    twice_sum=n*(2*al*t+be*u+ga*v)
    height=al*t+be*u+ga*v
    if t>=p[axis] and u>=pj and v>=pk:
        removed=(u-pj+1)*(v-pk+1)
        n-=removed
        twice_sum-=removed*(2*al*t+be*(pj+u)+ga*(pk+v))
        height=al*t+max(be*(pj-1)+ga*v,be*u+ga*(pk-1))
    assert twice_sum%2==0
    return n,twice_sum//2,height

def box_stats(weights,p,c):
    n=(c[0]+1)*(c[1]+1)*(c[2]+1)
    height=sum(w*x for w,x in zip(weights,c))
    twice_sum=n*height
    if all(x>=pi for x,pi in zip(c,p)):
        removed=(c[0]-p[0]+1)*(c[1]-p[1]+1)*(c[2]-p[2]+1)
        n-=removed
        twice_sum-=removed*sum(w*(x+pi) for w,x,pi in zip(weights,c,p))
        height=max(sum(w*(pi-1 if j==i else x) for j,(w,x,pi) in enumerate(zip(weights,c,p))) for i in range(3))
    assert twice_sum%2==0
    return n,twice_sum//2,height

def maximize(weights,M,p,penalty=1,reconstruct=False,moment_multiplier=4,height_multiplier=3):
    caps=[M//w for w in weights]; horns=[]; counts=[]; choices=[]
    for axis in range(3):
        js=[j for j in range(3) if j!=axis]
        n=caps[axis]+1; nb,nc=(caps[j]+1 for j in js)
        H=[[[0]*nc for _ in range(nb)] for _ in range(n+1)]
        K=[[[0]*nc for _ in range(nb)] for _ in range(n+1)]
        C=[[[None]*nc for _ in range(nb)] for _ in range(n+1)]
        for t in range(n-1,-1,-1):
            for b in range(nb):
                for c in range(nc):
                    val=0; num=0; choice=None
                    vol,moment,height=slice_stats(weights,p,axis,t,b,c)
                    if height<=M:
                        v=moment_multiplier*moment+vol*(penalty-height_multiplier*M)+H[t+1][b][c]
                        k=vol+K[t+1][b][c]
                        if (v,k)>(val,num):val,num,choice=v,k,('take',b,c)
                    if b and (H[t][b-1][c],K[t][b-1][c])>(val,num):val,num,choice=H[t][b-1][c],K[t][b-1][c],('left',b-1,c)
                    if c and (H[t][b][c-1],K[t][b][c-1])>(val,num):val,num,choice=H[t][b][c-1],K[t][b][c-1],('down',b,c-1)
                    H[t][b][c]=val; K[t][b][c]=num; C[t][b][c]=choice
        horns.append(H); counts.append(K); choices.append(C)
    best=None; size=0; center=None
    for c in product(*(range(cap+1) for cap in caps)):
        vol,moment,height=box_stats(weights,p,c)
        if height>M:continue
        score=moment_multiplier*moment+vol*(penalty-height_multiplier*M); count=vol
        for axis in range(3):
            js=[j for j in range(3) if j!=axis]
            score+=horns[axis][c[axis]+1][c[js[0]]][c[js[1]]]
            count+=counts[axis][c[axis]+1][c[js[0]]][c[js[1]]]
        if best is None or (score,count)>(best,size):best,size,center=score,count,c
    result={'weights':weights,'M':M,'corner':p,'penalty':penalty,'moment_multiplier':moment_multiplier,'height_multiplier':height_multiplier,'maximum':best,'maximizer_size':size,'center':center}
    if reconstruct:
        U=set(product(*(range(c+1) for c in center)))
        for axis in range(3):
            js=[j for j in range(3) if j!=axis]
            t=center[axis]+1; b,c=center[js[0]],center[js[1]]
            while t<len(choices[axis]):
                choice=choices[axis][t][b][c]
                if choice is None:break
                kind,b,c=choice
                if kind=='take':
                    for u,v in product(range(b+1),range(c+1)):
                        x=[0,0,0];x[axis]=t;x[js[0]]=u;x[js[1]]=v;U.add(tuple(x))
                    t+=1
        T={x for x in U if not all(y>=z for y,z in zip(x,p))}
        assert len(T)==size
        moment=sum(sum(w*y for w,y in zip(weights,x)) for x in T)
        assert moment_multiplier*moment+size*(penalty-height_multiplier*M)==best
        for x in T:
            for i in range(3):
                if x[i]:
                    y=list(x);y[i]-=1;assert tuple(y) in T
        corners=[]
        for x in product(*(range(cap+2) for cap in caps)):
            if x in T or not all(x):continue
            if all(tuple(x[j]-(j==i) for j in range(3)) in T for i in range(3)):corners.append(x)
        assert len(corners)<=1 and (not corners or corners[0]==p)
        result.update(points=sorted(T),sigma=moment,actual_M=max(sum(w*y for w,y in zip(weights,x)) for x in T),full_corners=corners)
    return result

if __name__=='__main__':
    out=[]
    for R in range(3,9):
        rows=[]
        for a in range(1,R+2):
            for b in range(a,R+2):
                for c in range(b,R+2):
                    if a+b+c<=R+1:rows.append(maximize((1,1,1),R,(a,b,c)))
        row=max(rows,key=lambda r:(r['maximum'],r['maximizer_size']))
        witness=maximize((1,1,1),R,row['corner'],reconstruct=True)
        print({k:v for k,v in witness.items() if k!='points'},flush=True)
        out.append({'R':R,'corner_cases':len(rows),'maximum':witness,'all_corner_results':rows})
    Path(__file__).with_name('unit_one_corner_results.json').write_text(json.dumps(out,indent=2)+'\n')
