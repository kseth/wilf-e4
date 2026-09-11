#!/usr/bin/env python3
"""Independent finite checks of the symbolic two- and three-direction identities.
This exhaustive box check validates the formulas, not the universal theorem.
"""
from itertools import product
from pathlib import Path
import json

def stats(T):
 F=[{x for x in T if tuple(x[j]+int(i==j) for j in range(3)) not in T} for i in range(3)]
 Q={(i,j):len(F[i]&F[j]) for i in range(3) for j in range(i+1,3)}
 n=[1+max(x[i] for x in T) for i in range(3)]
 K=len(set.intersection(*F));Kp=[]
 for i in range(3):
  P={tuple(x[j] for j in range(3) if i!=j) for x in T}
  Kp.append(sum(all(tuple(x[j]+int(i2==j) for j in range(2)) not in P for i2 in range(2)) for x in P))
 return Q,n,K,Kp

def dilation(T,L):
 return {tuple(L[i]*x[i]+r[i] for i in range(3)) for x in T for r in product(*(range(l) for l in L))}
def excess(U,dirs):
 B={(0,0,0)}|{tuple(int(i==j) for j in range(3)) for i in dirs}
 A={x for x in U if all(tuple(x[i]+b[i] for i in range(3)) in U for b in B)}
 # Directly enumerate all integer differences, independently of projection formula.
 AB={tuple(x[i]-b[i] for i in range(3)) for x in A for b in B}
 return len(AB)-len(U)

def height_arrays():
 a=[0]*9
 def rec(pos):
  if pos==9:
   yield tuple(a);return
  x,y=divmod(pos,3)
  cap=3
  if x:cap=min(cap,a[pos-3])
  if y:cap=min(cap,a[pos-1])
  for z in range(cap+1):
   a[pos]=z;yield from rec(pos+1)
 yield from rec(0)

def main():
 count=0;checks2=0;checks3=0
 for a in height_arrays():
  T={(x,y,z) for x in range(3) for y in range(3) for z in range(a[3*x+y])}
  if not T:continue
  count+=1;Q,n,K,Kp=stats(T)
  for i,j in [(0,1),(0,2),(1,2)]:
   k=3-i-j;L=[2,2,2];L[k]=1
   assert excess(dilation(T,L),(i,j))==Q[i,j]-2*n[k],(a,i,j)
   checks2+=1
  L=[2,3,2]
  lhs=excess(dilation(T,L),(0,1,2))
  rhs=sum(L[3-i-j]*(q-2*n[3-i-j]) for (i,j),q in Q.items())+sum(Kp)-K
  assert lhs==rhs,(a,lhs,rhs)
  checks3+=1
 out=dict(status='PASS',scope='Exhaustive validation of exact dilation identities on all nonempty lower ideals in {0,1,2}^3; universal theorem has a separate symbolic proof',ideals=count,two_direction_identities=checks2,three_direction_identities=checks3)
 assert count==979
 Path(__file__).with_name('surface_identity_checks.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
