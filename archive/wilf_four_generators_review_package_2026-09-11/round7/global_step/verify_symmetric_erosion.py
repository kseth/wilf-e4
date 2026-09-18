#!/usr/bin/env python3
"""Exact diagnostic replay for the separately proved symbolic erosion theorem."""
from itertools import product
from pathlib import Path
import json

def ideal(R,k):
 return {(x,y,z) for x in range(R+1) for y in range(R-x+1) for z in range(min(R-x,R-y)+1) if min(x,y,z)<=k}
def counts(T):
 F=[{x for x in T if tuple(x[j]+int(i==j) for j in range(3)) not in T} for i in range(3)]
 A=T-set.union(*F)
 P=sum(len({tuple(x[j] for j in range(3) if j!=i) for x in A}) for i in range(3))
 return dict(m=len(T),A=len(A),P=P,excess=len(A)+P-len(T),Q=len(F[0]&F[1]),K=len(set.intersection(*F)))
def main():
 checks=[]
 for R in range(3,31):
  for k in range(1,(R-1)//2+1):
   out=counts(ideal(R,k))
   assert out['Q']==(k+3)*(R-k)
   assert out['K']==3*(R-k)
   assert out['excess']==3*(k+1)*(R-k-1)>0
   checks.append(dict(R=R,k=k,**out))
 dilations=[]
 for R,k in [(3,1),(5,1),(5,2),(7,2),(9,3)]:
  T=ideal(R,k)
  for L in [(2,2,2),(2,3,4),(3,3,3)]:
   U={tuple(L[i]*x[i]+r[i] for i in range(3)) for x in T for r in product(*(range(l) for l in L))}
   out=counts(U)
   assert out['excess']==(k+1)*((R-k-2)*sum(L)+3)>0
   dilations.append(dict(R=R,k=k,L=L,**out))
 fixture=counts(ideal(29,3))
 assert fixture['excess']==300
 result=dict(status='PASS',scope='Exact checks of symbolic formulas; not a proof of unrestricted Wilf',undilated_cases=len(checks),dilated_cases=len(dilations),fixture=fixture,dilations=dilations)
 Path(__file__).with_name('symmetric_erosion_checks.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
