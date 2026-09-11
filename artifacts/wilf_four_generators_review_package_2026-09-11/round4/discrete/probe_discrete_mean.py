from itertools import product,combinations_with_replacement
from pathlib import Path
import random, json
import numpy as np
from scipy.optimize import linprog
rng=random.Random(7192026)
rows=[]; best={}
for case in range(6000):
 N=rng.randint(2,15)
 if case%2:
  p=[sorted([rng.randint(0,N) for _ in range(N)],reverse=True) for _ in range(3)]
 else:
  p=[[max(0,min(N,int(rng.uniform(.3,2)*N-rng.uniform(.3,3)*i))) for i in range(N)] for _ in range(3)]
  p=[sorted(x,reverse=True) for x in p]
 f,g,h=p
 T=np.array([(x,y,z) for x in range(N) for y in range(f[x]) for z in range(min(g[x],h[y]))])
 if len(T)<4 or not all(any(np.array_equal(x,e) for x in T) for e in ((1,0,0),(0,1,0),(0,0,1))):continue
 sm=T.sum(axis=0);m=len(T)
 res=linprog(-sm,A_ub=T,b_ub=np.ones(m),bounds=[(0,None)]*3,method='highs')
 assert res.success
 val=-res.fun;ratio=val/m;score=3*val-2*m
 row=dict(m=m,ratio=ratio,score=score,weights=res.x.tolist(),profiles=p)
 for key,v in [('ratio',ratio),('score',score),('ratio_m_ge6',ratio if m>=6 else 0)]:
  if key not in best or v>best[key][key if key in row else 'ratio']+1e-8:
   best[key]=row;print(key,json.dumps(row),flush=True)
 rows.append((m,ratio,score))
Path(__file__).with_name('probe_discrete_mean_results.json').write_text(json.dumps(dict(count=len(rows),best=best),indent=2))
