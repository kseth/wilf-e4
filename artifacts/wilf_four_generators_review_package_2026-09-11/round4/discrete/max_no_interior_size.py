from itertools import product
from pathlib import Path
from math import comb
import json

def rectangle(cap1,cap2,budget):
 if budget<0:return 0
 return max((u+1)*(min(cap2,budget-u)+1) for u in range(min(cap1,budget)+1))
def horn(base,cap1,cap2,R):
 return sum(rectangle(cap1,cap2,R-t) for t in range(base+1,R+1))
def volume(c,R):
 out=(c[0]+1)*(c[1]+1)*(c[2]+1)
 for i in range(3):
  caps=[c[j] for j in range(3) if j!=i]
  out+=horn(c[i],*caps,R)
 return out

def main():
 rows=[]
 for R in range(1,24):
  best=0;examples=[]
  for a in range(R+1):
   for b in range(a,R-a+1):
    for c in range(b,R-a-b+1):
     v=volume((a,b,c),R)
     if v>best:best=v;examples=[(a,b,c)]
     elif v==best:examples.append((a,b,c))
  rows.append(dict(R=R,best=best,central=examples,simplex_bound=comb(R+3,3)))
  print(rows[-1],flush=True)
 Path(__file__).with_name('max_no_interior_size_results.json').write_text(json.dumps(rows,indent=2)+'\n')
if __name__=='__main__':main()
