"""Diagnostic: test continuous mean<=2/3 with one full-support corner.

Finite searches do not prove a universal inequality. Any reported violation
requires exact rechecking and is not automatically a Wilf counterexample.
"""
import numpy as np
from scipy.optimize import linprog
from pathlib import Path
import random,json,time

N=16
rng=random.Random(202609071)
grid=np.indices((N,N,N)).reshape(3,-1).T

def score(profiles,corner):
    f,g,h=profiles
    ok=(grid[:,1]<f[grid[:,0]])&(grid[:,2]<g[grid[:,0]])&(grid[:,2]<h[grid[:,1]])
    ok &= np.any(grid<corner,axis=1)
    t=grid[ok]
    if not len(t):return None
    mu=t.mean(axis=0)+.5
    # Componentwise maximal cell tops suffice for the weighted height cap.
    heights=np.zeros((N,N),dtype=int)
    for x,y,z in t:heights[x,y]=max(heights[x,y],z+1)
    maxima=[]
    for x,y in zip(*np.nonzero(heights)):
        z=heights[x,y]
        if (x==N-1 or heights[x+1,y]<z) and (y==N-1 or heights[x,y+1]<z):
            maxima.append(tuple(map(int,(x+1,y+1,z))))
    r=linprog(-mu,A_ub=maxima,b_ub=np.ones(len(maxima)),bounds=[(0,None)]*3,method='highs')
    assert r.success
    return -r.fun,len(t),r.x.tolist(),maxima,tuple(map(int,t.sum(axis=0)))

best=(0,None);start=time.monotonic();iterations=0
for trial in range(6):
    p=np.array([[max(1,N-i) for i in range(N)] for _ in range(3)])
    corner=np.array([rng.randint(1,N) for _ in range(3)])
    cur=score(p,corner)
    for step in range(600):
        z=p.copy();q=corner.copy()
        if rng.random()<.25:
            q[rng.randrange(3)]=rng.randint(1,N)
        else:
            j=rng.randrange(3);i=rng.randrange(N)
            lo=int(z[j,i+1]) if i+1<N else 0
            hi=int(z[j,i-1]) if i else N
            z[j,i]=rng.randint(lo,hi)
        s=score(z,q);iterations+=1
        temperature=.004*(1-step/600)
        if s and (s[0]>=cur[0] or rng.random()<np.exp((s[0]-cur[0])/max(temperature,1e-8))):
            p=z;corner=q;cur=s
        if cur[0]>best[0]:
            best=(cur[0],dict(mean=cur[0],m=cur[1],weights=cur[2],
                 maxima=cur[3],coordinate_sums=cur[4],profiles=p.tolist(),corner=corner.tolist(),
                 trial=trial,step=step))
            if cur[0]>.65:print(json.dumps(best[1]),flush=True)
        if cur[0]>2/3+1e-8 or time.monotonic()-start>110:break
    if best[0]>2/3+1e-8 or time.monotonic()-start>110:break
out=dict(status='Numerical diagnostic only',iterations=iterations,
         seconds=time.monotonic()-start,best=best[1],violation=best[0]>2/3+1e-8)
Path(__file__).with_name('interior_probe_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='best'}),flush=True)
print('Best mean:',best[0],flush=True)
