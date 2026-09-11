"""Exact dynamic programming over all no-interior lower ideals of degree <=R.
Maximize sum_T(4*degree-3*R+1) without enumerating their shapes.
Uses the audited central-box / rectangular-horn decomposition.
"""
import json
from pathlib import Path

def solve(R):
 n=R+1
 # H[t][B][C] is best possible horn from outward integer t through R.
 H=[[[0]*n for _ in range(n)] for _ in range(R+2)]
 # Store actual optimal states for reconstructing one maximizer.
 choice=[[[None]*n for _ in range(n)] for _ in range(R+1)]
 for t in range(R,-1,-1):
  for b in range(n):
   for c in range(n):
    value=0;pick=None
    if t+b+c<=R:
     value=(b+1)*(c+1)*(4*t+2*b+2*c-3*R+1)+H[t+1][b][c]
     if value>=0:pick=(b,c)
     else:value=0
    if b and H[t][b-1][c]>value:value=H[t][b-1][c];pick=choice[t][b-1][c]
    if c and H[t][b][c-1]>value:value=H[t][b][c-1];pick=choice[t][b][c-1]
    H[t][b][c]=value;choice[t][b][c]=pick
 best=-10**100;center=None
 for a in range(n):
  for b in range(a,n):
   for c in range(b,n):
    if a+b+c>R:break
    box=(a+1)*(b+1)*(c+1)*(2*(a+b+c)-3*R+1)
    value=box+H[a+1][b][c]+H[b+1][a][c]+H[c+1][a][b]
    if value>best:best=value;center=(a,b,c)
 T=set()
 a,b,c=center
 for x in range(a+1):
  for y in range(b+1):
   for z in range(c+1):T.add((x,y,z))
 for axis in range(3):
  start=center[axis]+1;others=[j for j in range(3) if j!=axis]
  B,C=[center[j] for j in others]
  for t in range(start,R+1):
   pick=choice[t][B][C]
   if pick is None:break
   B,C=pick
   for u in range(B+1):
    for v in range(C+1):
     p=[0,0,0];p[axis]=t;p[others[0]]=u;p[others[1]]=v;T.add(tuple(p))
 assert all(sum(x)<=R for x in T)
 score=sum(4*sum(x)-3*R+1 for x in T)
 assert score==best,(R,score,best)
 # Directly check lower-ideal property and excluded-corner support.
 for x in T:
  for j in range(3):
   if x[j]:
    y=list(x);y[j]-=1;assert tuple(y) in T
 for i in range(1,R+2):
  for j in range(1,R+2-i):
   for k in range(1,R+2-i-j):
    x=(i,j,k)
    if x not in T:
     assert not all(tuple(x[d]-(d==h) for d in range(3)) in T for h in range(3)),x
 return {'R':R,'maximum_score':best,'central_box':center,'cardinality':len(T),'actual_max_degree':max(map(sum,T)),'D':3*len(T)*R-4*sum(map(sum,T)),'example':sorted(T) if R<=5 else None}

if __name__=='__main__':
 results=[solve(R) for R in range(1,24)]
 out={'method':'exact integer dynamic programming, no floating-point arithmetic','objective':'max_T sum(4 degree - 3R + 1)','R_range':[1,23],'results':results}
 Path(__file__).with_name('unit_weight_dp_results.json').write_text(json.dumps(out,indent=2)+'\n')
 for row in results:print({k:v for k,v in row.items() if k!='example'})
