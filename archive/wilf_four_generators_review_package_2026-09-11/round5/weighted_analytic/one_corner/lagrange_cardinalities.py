"""Exact possible cardinalities among all optimal Lagrange-score ideals."""
from one_corner_dp import slice_stats, box_stats
from itertools import product
from pathlib import Path
import json

def convolve(A,B):
    out=0
    while A:
        low=A&-A;k=low.bit_length()-1;out|=B<<k;A-=low
    return out

def maximize_cards(weights,M,p,penalty=2):
    caps=[M//w for w in weights];horns=[];counts=[]
    for axis in range(3):
        js=[j for j in range(3) if j!=axis]
        n=caps[axis]+1;nb,nc=(caps[j]+1 for j in js)
        H=[[[0]*nc for _ in range(nb)] for _ in range(n+1)]
        K=[[[1]*nc for _ in range(nb)] for _ in range(n+1)]
        for t in range(n-1,-1,-1):
            for b in range(nb):
                for c in range(nc):
                    options=[(0,1)]
                    vol,moment,height=slice_stats(weights,p,axis,t,b,c)
                    if height<=M:options.append((4*moment+vol*(penalty-3*M)+H[t+1][b][c],K[t+1][b][c]<<vol))
                    if b:options.append((H[t][b-1][c],K[t][b-1][c]))
                    if c:options.append((H[t][b][c-1],K[t][b][c-1]))
                    best=max(x[0] for x in options);bits=0
                    for value,cardbits in options:
                        if value==best:bits|=cardbits
                    H[t][b][c]=best;K[t][b][c]=bits
        horns.append(H);counts.append(K)
    best=None;bits=0
    for c in product(*(range(cap+1) for cap in caps)):
        vol,moment,height=box_stats(weights,p,c)
        if height>M:continue
        score=4*moment+vol*(penalty-3*M);cardbits=1<<vol
        for axis in range(3):
            js=[j for j in range(3) if j!=axis]
            score+=horns[axis][c[axis]+1][c[js[0]]][c[js[1]]]
            cardbits=convolve(cardbits,counts[axis][c[axis]+1][c[js[0]]][c[js[1]]])
        if best is None or score>best:best,bits=score,cardbits
        elif score==best:bits|=cardbits
    return {'weights':weights,'M':M,'p':p,'penalty':penalty,'maximum':best,'optimal_cardinalities':[i for i in range(bits.bit_length()) if bits>>i&1]}

if __name__=='__main__':
    R=6;out=[]
    for a in range(1,R+2):
        for b in range(a,R+2):
            for c in range(b,R+2):
                if a+b+c<=R+1:out.append(maximize_cards((1,1,1),R,(a,b,c)))
    result={'scope':'all full-support corners at unit height6; exact Lagrange2m-D maxima and their cardinalities','results':out}
    Path(__file__).with_name('lagrange_cardinality_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
