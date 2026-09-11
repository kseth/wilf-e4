"""Exact dual certificates for all arithmetically allowed p211 shapes in Δ5.
SciPy proposes only; every accepted certificate is checked as rational arithmetic.
"""
from itertools import product
from fractions import Fraction as F
from scipy.optimize import linprog
from pathlib import Path
import json

OUT=Path(__file__).resolve().parent

def profiles(R,first,second,upper_restrict=False):
 out=[]
 def rec(row):
  if len(row)==R+1:
   if row[first]<=second:return
   hx=sum(v>0 for v in row);hy=row[0]
   corners=[(i,row[i]) for i in range(1,hx) if row[i]<row[i-1]]
   if len(corners)>2:return
   if upper_restrict and sum(i>=2 for i,v in corners)>1:return
   out.append((tuple(row),hx,hy));return
  i=len(row);cap=min(R-i+1,row[-1] if row else R+1)
  for h in range(cap+1):rec(row+[h])
 rec([]);return out

def enumerate_shapes(R):
 xy=profiles(R,2,1,True);yz=profiles(R,1,1)
 for a,b,c in product(xy,xy,yz):
  if (a[1],a[2],b[2])!=(b[1],c[1],c[2]):continue
  T=tuple((x,y,z) for x in range(a[1]) for y in range(a[0][x]) for z in range(min(b[0][x],c[0][y])) if not (x>=2 and y>=1 and z>=1))
  if max(sum(p) for p in T)>R:continue
  yield (a[0],b[0],c[0]),T

def main():
 certificates=[];counts={};total=0;best=None
 for rows,T in enumerate_shapes(5):
  total+=1;m=len(T);counts[m]=counts.get(m,0)+1
  if m<30:continue
  ts=set(T);Z=tuple(p for p in T if all(tuple(v+(i==j) for j,v in enumerate(p)) not in ts for i in range(3)))
  sums=tuple(sum(p[i] for p in T) for i in range(3))
  opt=linprog([-4*s for s in sums]+[3*m],A_ub=[list(p)+[-1] for p in Z],b_ub=[0]*len(Z),bounds=[(1,None)]*3+[(None,None)],method='highs')
  assert opt.success,(rows,opt.message)
  y=[F(float(-v)).limit_denominator(1000000) for v in opt.ineqlin.marginals]
  beta=[F(float(v)).limit_denominator(1000000) for v in opt.lower.marginals[:3]]
  assert all(v>=0 for v in y+beta)
  assert sum(y)==3*m,(rows,y)
  assert all(beta[i]-sum(t*p[i] for t,p in zip(y,Z))==-4*sums[i] for i in range(3)),(rows,y,beta)
  bound=sum(beta)
  if best is None or bound-(m-1)<best[0]:best=(bound-(m-1),m,rows,bound)
  if bound<m-1:
   fail=dict(status='weighted obstruction',m=m,rows=rows,T=T,Z=Z,sums=sums,bound=str(bound),weights=opt.x.tolist())
   (OUT/'low_height_weighted_failure.json').write_text(json.dumps(fail,indent=2));print(json.dumps(fail),flush=True);return
  certificates.append(dict(rows=rows,m=m,sums=sums,dual=[dict(point=p,coefficient=str(v)) for p,v in zip(Z,y) if v],beta=[str(v) for v in beta],lower_bound=str(bound)))
  if len(certificates)%1000==0:print(json.dumps(dict(proved=len(certificates),enumerated=total)),flush=True)
 assert total==70175 and max(counts)==43
 (OUT/'low_height_weighted_certificates.json').write_text(json.dumps(certificates,separators=(',',':')))
 summary=dict(status='all exact dual certificates passed',degree_cap=5,total_shapes=total,certified_shapes=len(certificates),cardinality_histogram=counts,minimum_margin=str(best[0]),minimum_multiplicity=best[1],minimum_rows=best[2],minimum_bound=str(best[3]))
 (OUT/'low_height_weighted_certificate_summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2),flush=True)
if __name__=='__main__':main()
