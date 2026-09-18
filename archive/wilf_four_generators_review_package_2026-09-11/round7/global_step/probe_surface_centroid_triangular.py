#!/usr/bin/env python3
"""Heuristic abstract-ideal probe. Does not construct semigroups or prove a bound."""
import json,math,random,sys
from pathlib import Path
import numpy as np
from scipy.optimize import linprog

rng=random.Random(425519);N=16
G=np.indices((N,N,N));x,y,z=G
sumg=x+y+z
best=None;valid=0

def evaluate(prof,p):
 T=(y<prof[0][x])&(z<prof[1][x])&(z<prof[2][y])&((x<p[0])|(y<p[1])|(z<p[2]))
 m=int(T.sum());M=int(sumg[T].max());S=int(sumg[T].sum())
 F=[]
 for i in range(3):
  nxt=np.roll(T,-1,axis=i); sl=[slice(None)]*3;sl[i]=-1;nxt[tuple(sl)]=False
  F.append(T&~nxt)
 Q=[int((F[j]&F[k]).sum()) for j,k in [(1,2),(0,2),(0,1)]]
 ratio=(S/m+1.5)/(M+3)
 penalty=sum(max(q-2*N,0) for q in Q)/(20*N)
 return ratio-penalty,ratio,Q,m,M,S,T,F

def lp_check(prof,p,out):
 _,ratio,Q,m,M,S,T,F=out
 Z=np.argwhere(F[0]&F[1]&F[2]); sums=[int(G[i][T].sum()) for i in range(3)]
 opt=linprog([m-6*t for t in sums]+[4*m],A_ub=[[*map(int,v),-1] for v in Z],b_ub=[0]*len(Z),A_eq=[[1,1,1,0]],b_eq=[1],bounds=[(0,None)]*4,method='highs')
 assert opt.success
 return dict(N=N,p=p,profiles=[v.tolist() for v in prof],m=m,M=M,S=S,Q=Q,unit_centroid=ratio,LP_objective=opt.fun,LP_weights=opt.x.tolist(),sums=sums,maxima=Z.tolist())

steps=int(sys.argv[1]) if len(sys.argv)>1 else 50000
for restart in range(10):
 prof=[np.array([N-i for i in range(N)]) for _ in range(3)];p=[rng.randrange(1,5) for _ in range(3)]
 cur=evaluate(prof,p)
 for it in range(steps//10):
  new=[a.copy() for a in prof];pnew=p.copy()
  if rng.random()<.06:
   i=rng.randrange(3);pnew[i]+=rng.choice([-1,1])
   if not 1<=pnew[i]<N:continue
  else:
   h=rng.randrange(3);i=rng.randrange(1,N);new[h][i]+=rng.choice([-1,1])
   if not 1<=new[h][i]<=N or new[h][i]>new[h][i-1] or (i+1<N and new[h][i]<new[h][i+1]):continue
  if new[0][pnew[0]]<=pnew[1] or new[1][pnew[0]]<=pnew[2] or new[2][pnew[1]]<=pnew[2]:continue
  out=evaluate(new,pnew)
  temp=.004*(1-(it/(steps//10)))+.00003
  if out[0]>=cur[0] or rng.random()<math.exp((out[0]-cur[0])/temp):prof,p,cur=new,pnew,out
  if max(out[2])<=2*N:
   valid+=1
   if best is None or out[1]>best['unit_centroid']:
    cand=lp_check(new,pnew,out);best=cand
    print(json.dumps(dict(restart=restart,it=it,valid=valid,best=best)),flush=True)
    if cand['LP_objective']< -1e-7:break
 else:continue
 break
out=dict(scope='Heuristic abstract-ideal search only',attempts=steps,valid=valid,best=best)
Path(__file__).with_name('surface_centroid_triangular_probe.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out),flush=True)
