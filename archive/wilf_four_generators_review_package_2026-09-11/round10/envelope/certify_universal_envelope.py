"""Generate exact universal envelope upper bounds. SciPy proposes multipliers only."""
import gzip,json,time,sys
from pathlib import Path
from probe_envelope import solve
from generate_normal_cases import cases

DEN=1000000

def bound(lp,res):
 # For max q.x with A.x<=r, box l<=x<=u, any lambda>=0 gives
 # q.x <= lambda.r + sum_i max((q-A^T lambda)_i*l_i,(q-A^T lambda)_i*u_i).
 mult=[max(0,round(-float(v)*DEN)) for v in res.ineqlin.marginals]
 coeff=[int(-v)*DEN for v in lp.obj]
 total=0
 for z,row,rhs in zip(mult,lp.rows,lp.rhs):
  total+=z*rhs
  if z:
   for i,a in row.items():coeff[i]-=z*a
 for v,(lo,hi) in zip(coeff,lp.bounds):total+=v*(hi if v>=0 else lo)
 return total,[[i,z] for i,z in enumerate(mult) if z]

def main():
 start=time.time();outdir=Path(__file__).parent;maxnum=-10**99;maxden=1;count=0;feasible=0;infeasible=0
 with gzip.open(outdir/'universal_envelope_certificates.jsonl.gz','wt') as out:
  for index,(p,n,h) in enumerate(cases()):
   u=min(n);lp,res,y=solve(p,n,h,return_model=True,integer_scale=u)
   kind='moment'
   if not res.success:
    assert res.status==2,res.message
    # Relax cardinality and certify that even its maximum is below30.
    at=lp.row_names.index(('cardinality',))
    for ar in (lp.rows,lp.rhs,lp.row_names):ar.pop(at)
    lp.obj=[-int(i in set(y.values())) for i in range(len(lp.names))]
    res=lp.solve();assert res.success,res.message;kind='cardinality'
   upper,mult=bound(lp,res)
   if kind=='moment':
    assert 10*upper<=29*u*DEN,(index,p,n,h,upper,u)
    if upper*maxden>maxnum*u*DEN:maxnum=upper;maxden=u*DEN
    feasible+=1
   else:assert upper<30*DEN,(index,p,n,h,upper);infeasible+=1
   out.write(json.dumps({'p':p,'n':n,'h':h,'kind':kind,'upper_numerator':upper,'denominator':DEN,'multipliers':mult},separators=(',',':'))+'\n')
   count+=1
   if count%2000==0:print(json.dumps({'completed':count,'moment':feasible,'cardinality':infeasible,'maximum_normalized_bound':maxnum/maxden,'seconds':time.time()-start}),flush=True)
 result={'status':'passed','cases':count,'moment_cases':feasible,'cardinality_cases':infeasible,'max_normalized_numerator':maxnum,'max_normalized_denominator':maxden,'seconds':time.time()-start,'scipy_used_for_proposals_only':True,'exact_integer_inequality_acceptance':True}
 assert count==44281
 (outdir/'universal_envelope_generation_result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)

if __name__=='__main__':main()
