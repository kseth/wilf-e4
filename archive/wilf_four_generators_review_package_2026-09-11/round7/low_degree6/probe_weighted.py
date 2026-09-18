import csv,json,random
from fractions import Fraction as F
from scipy.optimize import linprog
from pathlib import Path
out=Path(__file__).parent
ps=[(1,1,3),(1,2,2),(1,1,4),(1,2,3),(2,2,2),(1,1,5),(1,2,4),(1,3,3),(2,2,3)]
rows=list(csv.DictReader((out/'weighted_candidates_sample.tsv').open(),delimiter='\t'));random.Random(728).shuffle(rows)
best=None
for i,r in enumerate(rows):
 p=ps[int(r['pid'])];planes=[[(int(r[k])>>(3*x))&7 for x in range(7)] for k in ['xy','xz','yz']]
 T={(x,y,z) for x in range(7) for y in range(planes[0][x]) for z in range(min(planes[1][x],planes[2][y])) if not all(q>=v for q,v in zip((x,y,z),p))}
 assert len(T)==int(r['m']);m=len(T);sums=[sum(x[j] for x in T) for j in range(3)]
 fs=[{x for x in T if tuple(x[j]+(j==k) for j in range(3)) not in T} for k in range(3)];Z=sorted(set.intersection(*fs))
 Q=[len(fs[(k+1)%3]&fs[(k+2)%3]) for k in range(3)];n=[max(x[k] for x in T)+1 for k in range(3)]
 assert all(Q[k]<=2*n[k] for k in range(3)) and len(Z)>6
 opt=linprog([-4*s for s in sums]+[3*m],A_ub=[list(x)+[-1] for x in Z],b_ub=[0]*len(Z),bounds=[(1,None)]*3+[(0,7)],method='highs')
 assert opt.success
 if best is None or opt.fun-m+2.9<best[0]:best=(opt.fun-m+2.9,r,opt.x.tolist())
 if opt.fun < m-2.9-1e-8:
  a=[F(float(v)).limit_denominator(10000) for v in opt.x[:3]]
  M=max(sum(q*v for q,v in zip(a,x)) for x in T)
  if M==7:
   a=[(99*q+1)/100 for q in a];M=max(sum(q*v for q,v in zip(a,x)) for x in T)
  D=3*m*M-4*sum(q*v for q,v in zip(a,sums))
  assert M<7 and D<F(10*m-29,10)
  data=dict(status='exact geometric obstruction after all requested filters',checked=i+1,corner=p,plane_rows=planes,T=sorted(T),maxima=Z,m=m,sums=sums,Q=Q,axis_lengths=n,erosion=int(r['erosion']),weights=[str(q) for q in a],M=str(M),D=str(D),weak_target=str(F(10*m-29,10)),unit_D=int(r['unit_D']))
  (out/'weighted_obstruction.json').write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data,indent=2));break
 if (i+1)%1000==0:print(json.dumps(dict(checked=i+1,best=best)),flush=True)
else:
 (out/'weighted_sample_result.json').write_text(json.dumps(dict(status='bounded sample passed',checked=len(rows),best=best),indent=2)+'\n')
 print(json.dumps(dict(checked=len(rows),best=best)))
