from itertools import product
import json
out=[]
for R in range(3,21):
 T={(x,y,z) for x,y,z in product(range(R+1),repeat=3) if x+y<=R and x+z<=R and (y*z==0 or y+z<=R-1) and not(x>=2 and y>=1 and z>=1)}
 assert len(T)==2*R*R-R+3 and max(map(sum,T))==R
 triples=[{(0,j,R-j),(1,0,R-j),(1,j,0)} for j in range(1,R)]
 assert len(set.union(*triples))==3*(R-1)
 assert all(any(p not in T for p in tri) for tri in triples)
 assert all(sum(p)<=R for tri in triples for p in tri)
 assert all(tuple(v-(i==j) for j,v in enumerate((2,1,1))) in T for i in range(3))
 out.append(dict(R=R,cardinality=len(T),formula=2*R*R-R+3))
print(json.dumps(dict(status='exact sharpness and disjoint-witness checks passed',checks=out),indent=2))
