import numpy as np
from scipy.optimize import minimize
import json
from pathlib import Path

def constraints(x):
 v,b,c,k,d1,d2=x;u=[v,b,c];d=[d1,d2,k-d1-d2];mu=[(1+k)/4-h for h in d]
 out=[b-v,c-b,v-k,k-d1-d2,2*(v+b+c)+3*k-1]
 for j in range(3):
  for i in range(3):
   if i!=j:out.append(2*d[j]*(1+u[i]+u[j])-2*u[j]*mu[i]+u[i]*(1+u[i]))
 return np.array(out)
resbest=None
for i in range(20):
 rng=np.random.default_rng(i)
 x0=[.1,.15,.3,.095,.02,.025]+rng.uniform(-.005,.005,6)
 r=minimize(lambda x:x[0],x0,bounds=[(.001,1),(0,1),(0,1),(0,1),(0,1),(0,1)],constraints=[dict(type='ineq',fun=constraints)],method='SLSQP',options=dict(ftol=1e-13,maxiter=1000))
 if r.success and (resbest is None or r.fun<resbest.fun):resbest=r;print(r.fun,r.x,constraints(r.x),flush=True)
Path(__file__).with_name('optimize_phase_cutoff_results.json').write_text(json.dumps(dict(value=resbest.fun,x=resbest.x.tolist(),constraints=constraints(resbest.x).tolist()),indent=2))
