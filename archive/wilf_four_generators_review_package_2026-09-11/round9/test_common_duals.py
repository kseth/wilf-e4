import pathlib,json,itertools,collections,csv
import numpy as np
from fractions import Fraction
ROOT=pathlib.Path(__file__).resolve().parents[1]
stat=json.loads((ROOT/'round9/dual_compression_statistics.json').read_text())
# Read the full registry again, because detailed JSON intentionally stores only top 20.
exec((ROOT/'round9/analyze_dual_compression.py').read_text().split("(ROOT/'round9/dual_compression_statistics.json').write_text")[0])
top=[b for b,n in canonjoined.most_common(100)]
def det(M):
 if len(M)==1:return int(M[0][0])
 return sum((-1)**j*int(M[0][j])*det([r[:j]+r[j+1:] for r in M[1:]]) for j in range(len(M)))
def column(id):
 if id<343:return [-(id//49),-(id//7%7),-(id%7),1]
 return [int(j==id-343) for j in range(4)] if id<347 else [0,0,0,-1]
rows=[]
for rank,b in enumerate(top):
 for bs in sorted({tuple(sorted(trans(k,p) for k in b)) for p in PERMS}):
  M=np.array([column(k) for k in bs],dtype=np.int64).T.tolist();d=det(M);adj=[]
  for i in range(4):
   adj.append([(-1)**(i+j)*det([[M[r][c] for c in range(4) if c!=i] for r in range(4) if r!=j]) for j in range(4)])
  if d<0:d=-d;adj=[[-v for v in r] for r in adj]
  rows.append((rank,bs,d,adj))
adj=np.array([r[3] for r in rows],dtype=np.int64);den=np.array([r[2] for r in rows]);ids=np.array([r[1] for r in rows]);rank=np.array([r[0] for r in rows]);rhsbound=((ids>=343)&(ids<=345)).astype(np.int64)-7*(ids==347)
ps=[(1,1,3),(1,2,2),(1,1,4),(1,2,3),(2,2,2),(1,1,5),(1,2,4),(1,3,3),(2,2,3)]
n=0;hits=collections.Counter();considered=0
for r in csv.DictReader(open(ROOT/'round7/low_degree6/weighted_candidates_sample.tsv'),delimiter='\t'):
 considered+=1
 if any(v is None for v in r.values()):continue
 p=ps[int(r['pid'])];a=[int(r['xy'])>>3*i&7 for i in range(7)];b=[int(r['xz'])>>3*i&7 for i in range(7)];c=[int(r['yz'])>>3*i&7 for i in range(7)]
 T={(x,y,z) for x in range(7) for y in range(a[x]) for z in range(min(b[x],c[y])) if not all(q>=q0 for q,q0 in zip((x,y,z),p))}
 m=len(T)
 F=[{v for v in T if tuple(q+int(i==j) for j,q in enumerate(v)) not in T} for i in range(3)]
 ns=[max(v[i] for v in T)+1 for i in range(3)]
 if any(len(F[i]&F[j])>2*ns[3-i-j] for i,j in ((0,1),(0,2),(1,2))):continue
 n+=1;s=np.array([sum(v[i] for v in T) for i in range(3)]);obj=np.r_[-4*s,3*m];v=adj@obj;bound=(v*rhsbound).sum(axis=1)
 mask=np.ones(348,dtype=bool);mask[:343]=False
 for x,y,z in T:mask[49*x+7*y+z]=True
 ok=(v>=0).all(axis=1)&mask[ids].all(axis=1)&(10*bound>=(10*m-29)*den)
 for k in (1,5,10,20,50,100):hits[k]+=int(np.any(ok&(rank<k)))
result={'scope':'Existing deterministic diagnostic sample, filtered by the same pairwise surface restrictions; not exhaustive and not randomized holdout.','input_rows':considered,'sampled_eligible_shapes':n,'basis_orbits_tested':100,'oriented_bases_tested':len(rows),'exact_integer_retest_coverage':dict(hits),'arithmetic':'All determinants, adjugates, objectives, multipliers, membership, and bounds tested in signed int64; entries are small degree-six integers.'}
(ROOT/'round9/common_dual_sample_results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
