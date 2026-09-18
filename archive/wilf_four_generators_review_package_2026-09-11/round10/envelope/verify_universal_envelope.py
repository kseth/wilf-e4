"""Independent standard-library reconstruction and exact replay.

This imports neither the LP producer nor SciPy. Constraint rows are reconstructed
from indicator inequalities; optimization outputs enter only as nonnegative
integer coefficients, checked by direct addition and box maximization.
"""
import gzip,json,itertools,math,time
from pathlib import Path

P=list(q for q in itertools.product(range(7),repeat=3) if sum(q)<=6)
PS=sorted((q for q in itertools.combinations_with_replacement(range(1,6),3) if 5<=sum(q)<=7),key=lambda q:(sum(q),q))

def all_normals():
 out=set()
 # A projected triangle in the side-six coordinate simplex has doubled area
 # at most36, so every primitive positive triangle normal has entries<=36.
 for n in itertools.product(range(1,37),repeat=3):
  if math.gcd(math.gcd(n[0],n[1]),n[2])!=1:continue
  groups={}
  for q in P:groups.setdefault(sum(a*b for a,b in zip(q,n)),[]).append(q)
  yes=False
  for qs in groups.values():
   if len(qs)<3:continue
   p,r=qs[:2];u=tuple(a-b for a,b in zip(r,p))
   for q in qs[2:]:
    v=tuple(a-b for a,b in zip(q,p))
    if any(u[i]*v[j]!=u[j]*v[i] for i,j in ((0,1),(0,2),(1,2))):yes=True;break
   if yes:break
  if yes:out.add(n)
 # Epigraph vertices with two weight lower bounds active.
 for n in itertools.product(range(1,13),repeat=3):
  if math.gcd(math.gcd(n[0],n[1]),n[2])!=1 or n.count(min(n))<2:continue
  k=n.index(max(n))
  if any(q[k]!=r[k] and sum(n[i]*(q[i]-r[i]) for i in range(3))==0 for q,r in itertools.combinations(P,2)):out.add(n)
 out.add((1,1,1));return sorted(out)

def cases(ns):
 for p in PS:
  for n in ns:
   u=min(n);least=sum(a*b for a,b in zip(n,p))-u
   if least>=7*u:continue
   levels=sorted(sum(a*b for a,b in zip(n,q)) for q in P if not all(q[i]>=p[i] for i in range(3)))
   for h in sorted(set(levels)):
    if least<=h<7*u and sum(t<=h for t in levels)>=30:yield p,n,h

def model(p,n,h,kind):
 names=[('t',q) for q in P]
 names += [('e',q) for q in P if sum(q)<=5]
 names += [('s',i,j,q) for i,j in itertools.combinations(range(3),2) for q in P]
 names += [('c',i,j,a,b) for i,j in itertools.combinations(range(3),2) for a in range(1,7) for b in range(1,8-a)]
 index={name:i for i,name in enumerate(names)};rows=[];rhs=[];bounds=[(0,1)]*len(names)
 def row(items,b):
  d={}
  for name,c in items:
   if name in index:d[index[name]]=d.get(index[name],0)+c
  rows.append(d);rhs.append(b)
 def move(q,i,d):r=list(q);r[i]+=d;return tuple(r)
 for q in P:
  bounds[index['t',q]]=(0,int(sum(a*b for a,b in zip(q,n))<=h and not all(q[i]>=p[i] for i in range(3))))
  for i in range(3):
   if q[i]:row([(('t',q),1),(('t',move(q,i,-1)),-1)],0)
  if min(q)>0 and q!=p:row([(('t',q),-1)]+[(('t',move(q,i,-1)),1) for i in range(3)],2)
 for q in itertools.product(range(1,8),repeat=3):
  if sum(q)==7 and q!=p:row([(('t',move(q,i,-1)),1) for i in range(3)],2)
 for i in range(3):
  q=move(p,i,-1);assert bounds[index['t',q]][1]==1
  bounds[index['t',q]]=(1,1)
 if kind=='moment':row([(('t',q),-1) for q in P],-30)
 for q in P:
  if sum(q)<=5:row([(('e',q),-1),(('t',q),-2)]+[(('t',move(q,i,1)),1) for i in range(3)],0)
 row([(('t',q),-1) for q in P]+[(('e',q),1+q.count(0)) for q in P if sum(q)<=5],0)
 for i,j in itertools.combinations(range(3),2):
  for q in P:row([(('t',q),1),(('s',i,j,q),-1),(('t',move(q,i,1)),-1),(('t',move(q,j,1)),-1)],0)
  row([(('s',i,j,q),1) for q in P]+[(('t',q),-2) for q in P if q[i]==q[j]==0],0)
 for i,j in itertools.combinations(range(3),2):
  allc=[];upperc=[]
  for a in range(1,7):
   for b in range(1,8-a):
    q=[0,0,0];q[i]=a;q[j]=b;q=tuple(q);name=('c',i,j,a,b)
    row([(name,-1),(('t',q),-1),(('t',move(q,i,-1)),1),(('t',move(q,j,-1)),1)],1)
    allc.append((name,1))
    if a>=p[i] and b>=p[j]:upperc.append((name,1))
  row(allc,sum(p)-2);row(upperc,p[3-i-j])
 objective=[0]*len(names)
 for q in P:objective[index['t',q]]=min(n)+4*sum(a*b for a,b in zip(q,n))-3*h if kind=='moment' else 1
 return rows,rhs,bounds,objective

def main():
 started=time.time();here=Path(__file__).parent;ns=all_normals();assert len(ns)==2425
 assert max(max(n) for n in ns)==30
 assert len({tuple(sorted(n)) for n in ns})==416
 expected=iter(cases(ns));count=0;moment=0;cardinality=0;greatest=(-10**99,1)
 with gzip.open(here/'universal_envelope_certificates.jsonl.gz','rt') as stream:
  for line in stream:
   rec=json.loads(line);p,n,h=next(expected)
   assert rec['p']==list(p) and rec['n']==list(n) and rec['h']==h
   kind=rec['kind'];assert kind in ('moment','cardinality')
   rows,rhs,bounds,obj=model(p,n,h,kind);den=rec['denominator'];assert den==1000000
   residual=[v*den for v in obj];upper=0;previous=-1
   for i,z in rec['multipliers']:
    assert isinstance(i,int) and isinstance(z,int) and previous<i<len(rows) and z>0;previous=i
    upper+=z*rhs[i]
    for j,a in rows[i].items():residual[j]-=z*a
   for value,(lo,hi) in zip(residual,bounds):upper+=max(value*lo,value*hi)
   assert upper==rec['upper_numerator']
   if kind=='moment':
    assert 10*upper<=29*min(n)*den;moment+=1
    if upper*greatest[1]>greatest[0]*den*min(n):greatest=(upper,den*min(n))
   else:assert upper<30*den;cardinality+=1
   count+=1
 try:next(expected);raise AssertionError('missing certificate')
 except StopIteration:pass
 assert count==44281
 result={'status':'passed','normals':len(ns),'normal_coordinate_orbits':416,'parameter_cases':count,'moment_certificates':moment,'cardinality_certificates':cardinality,'greatest_normalized_upper_numerator':greatest[0],'greatest_normalized_upper_denominator':greatest[1],'seconds':time.time()-started,'scipy_used':False,'producer_imported':False,'arithmetic':'exact Python integers'}
 (here/'universal_envelope_independent_result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)

if __name__=='__main__':main()
