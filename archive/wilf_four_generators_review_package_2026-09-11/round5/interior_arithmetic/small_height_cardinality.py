from itertools import product
import json

def profiles(R,first,second,upper_restrict=False):
 out=[]
 def rec(row):
  if len(row)==R+1:
   if row[first]<=second:return
   hx=sum(v>0 for v in row);hy=row[0]
   corners=[(i,row[i]) for i in range(1,hx) if row[i]<row[i-1]]
   if len(corners)>2:return
   if upper_restrict and sum(i>=2 for i,v in corners)>1:return
   out.append((tuple(row),hx,hy,corners));return
  i=len(row);cap=min(R-i+1,row[-1] if row else R+1)
  for h in range(cap+1):rec(row+[h])
 rec([]);return out

ans={}
for R in range(3,7):
 xy=profiles(R,2,1,True);yz=profiles(R,1,1)
 best=(-1,None);count=0
 for a,b,c in product(xy,xy,yz):
  if (a[1],a[2],b[2])!=(b[1],c[1],c[2]):continue
  T=[(x,y,z) for x in range(a[1]) for y in range(a[0][x]) for z in range(min(b[0][x],c[0][y])) if not (x>=2 and y>=1 and z>=1)]
  if max(sum(p) for p in T)>R:continue
  count+=1
  if len(T)>best[0]:best=(len(T),dict(xy=a[0],xz=b[0],yz=c[0],T=T))
 ans[R]=dict(candidates=count,max_cardinality=best[0],witness=best[1])
print(json.dumps(ans,indent=2))
