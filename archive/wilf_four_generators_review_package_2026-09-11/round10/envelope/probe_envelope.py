"""Fractional order-ideal envelope. Exploratory only, never a proof certificate."""
import itertools, json
import numpy as np
from scipy.optimize import linprog

POINTS=[q for q in itertools.product(range(7),repeat=3) if sum(q)<=6]
PSET=set(POINTS)
PS=[(1,1,3),(1,2,2),(1,1,4),(1,2,3),(2,2,2),(1,1,5),(1,2,4),(1,3,3),(2,2,3)]

class LP:
 def __init__(self): self.names=[];self.bounds=[];self.obj=[];self.rows=[];self.rhs=[];self.row_names=[]
 def var(self,name,bounds=(0,1),obj=0):
  i=len(self.names);self.names.append(name);self.bounds.append(bounds);self.obj.append(obj);return i
 def row(self,d,rhs,name=None): self.rows.append({i:v for i,v in d.items() if v});self.rhs.append(rhs);self.row_names.append(name)
 def solve(self):
  from scipy.sparse import lil_matrix
  a=lil_matrix((len(self.rows),len(self.names)))
  for r,d in enumerate(self.rows):
   for i,v in d.items(): a[r,i]=v
  return linprog(self.obj,A_ub=a.tocsr(),b_ub=self.rhs,bounds=self.bounds,method='highs')

def solve(p,b,H,mmin=30,return_model=False,integer_scale=None):
 lp=LP(); y={}
 for q in POINTS:
  allowed=sum(bi*qi for bi,qi in zip(b,q))<=H+(0 if integer_scale else 1e-8) and not all(qi>=pi for qi,pi in zip(q,p))
  y[q]=lp.var(('y',q), (0,1 if allowed else 0), -((integer_scale or 1)+4*sum(bi*qi for bi,qi in zip(b,q))-3*H))
 def add(row,q,c):
  if q in y: row[y[q]]=row.get(y[q],0)+c
 def step(q,i,s=1):
  r=list(q);r[i]+=s;return tuple(r)
 # Lower ideal and exactly one full support minimal excluded point.
 for q in POINTS:
  for i in range(3):
   if q[i]: lp.row({y[q]:1,y[step(q,i,-1)]:-1},0,('lower',q,i))
  if all(q) and q!=p:
   d={y[q]:-1}
   for i in range(3):add(d,step(q,i,-1),1)
   lp.row(d,2,('no_full_corner',q))
 # Also forbid minimal exclusions outside degree simplex.
 for q in itertools.product(range(1,8),repeat=3):
  if sum(q)==7 and q!=p:
   d={}
   for i in range(3):add(d,step(q,i,-1),1)
   lp.row(d,2,('no_full_corner',q))
 for i in range(3):
  q=step(p,i,-1)
  if q not in y: return None
  if lp.bounds[y[q]][1]==0: return None
  lp.bounds[y[q]]=(1,1)
 if mmin:lp.row({i:-1 for i in y.values()},-mmin,('cardinality',))
 # Erosion lower bound, sufficient for the exact arithmetic inequality at 0/1 vertices.
 d={i:-1 for i in y.values()}
 for q in POINTS:
  if sum(q)>5:continue
  z=lp.var(('erosion',q));r={z:-1,y[q]:-2}
  for i in range(3): add(r,step(q,i),1)
  lp.row(r,0,('erosion_local',q)); d[z]=1+sum(qi==0 for qi in q)
 lp.row(d,0,('erosion_global',))
 # Pairwise exposed-surface size.
 for i,j in itertools.combinations(range(3),2):
  k=3-i-j; d={}
  for q in POINTS:
   w=lp.var(('surface',i,j,q));r={y[q]:1,w:-1}
   add(r,step(q,i),-1);add(r,step(q,j),-1);lp.row(r,0,('surface_local',i,j,q));d[w]=1
  for q in POINTS:
   if all(q[t]==0 for t in (i,j)):add(d,q,-2)
  lp.row(d,0,('surface_global',i,j))
 # Two plane minimal-exclusion budgets.
 for i,j in itertools.combinations(range(3),2):
  k=3-i-j;d={};du={}
  for u in range(1,7):
   for v in range(1,8-u):
    q=[0,0,0];q[i]=u;q[j]=v;q=tuple(q)
    w=lp.var(('corner',q));r={w:-1};add(r,q,-1)
    add(r,step(q,i,-1),1);add(r,step(q,j,-1),1);lp.row(r,1,('corner_local',q));d[w]=1
    if u>=p[i] and v>=p[j]:du[w]=1
  lp.row(d,sum(p)-2,('corner_global',i,j));lp.row(du,p[k],('corner_upper_global',i,j))
 res=lp.solve()
 if return_model:return lp,res,y
 return {'corner':p,'weights':b,'height':H,'status':res.message,'objective':-res.fun if res.success else None,
 'm':sum(res.x[i] for i in y.values()) if res.success else None,
 'fractional':int(sum(abs(res.x[i]-round(res.x[i]))>1e-7 for i in y.values())) if res.success else None,
 'y':[(q,float(res.x[i])) for q,i in y.items() if res.success and res.x[i]>1e-7]}

if __name__=='__main__':
 out=[]
 for p in PS:
  for H in (4,5,6):
   r=solve(p,(1,1,1),H)
   if r: out.append(r);print({k:v for k,v in r.items() if k!='y'},flush=True)
 open('round10/envelope/fractional_probe.json','w').write(json.dumps(out,indent=2))
