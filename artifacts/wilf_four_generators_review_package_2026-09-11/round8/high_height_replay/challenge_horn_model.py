"""Compare a horn bound with direct plane-cylinder ideal enumeration.

The brute implementation never invokes a center/horn representation. It lists
all coordinate-plane lower ideals, matches their common axes, intersects the
three cylinders, removes p+N^3, and sums individual retained points.
"""
from pathlib import Path
import itertools,json,subprocess,time,hashlib
root=Path(__file__).resolve().parent
cases=[]
for H in [4,5]:
 for p in itertools.product(range(1,H),repeat=3):
  if 5<=sum(p)<=H+1:
   cases.append((1,1,1,H,1,1,H,*p))
for box in [(2,2,3,9,2,3,10),(2,2,3,9,3,4,10),(2,3,4,11,4,5,12),(2,2,2,9,3,3,10),(1,1,2,5,1,2,5)]:
 q,B,C,H0,UB,UC,H1=box
 for p in itertools.product(range(1,6),repeat=3):
  if sum(p)>=5 and q*p[0]+B*p[1]+C*p[2]<=H1+q:
   cases.append((*box,*p))
start=time.time();rows=[]
with subprocess.Popen([str(root/'brute_plane_cylinders')],stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True) as brute,subprocess.Popen([str(root/'fixed_corner_wrapper')],stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True) as horn:
 for args in cases:
  line=' '.join(map(str,args))+'\n'
  brute.stdin.write(line);brute.stdin.flush();a=list(map(int,brute.stdout.readline().split()))
  horn.stdin.write(line);horn.stdin.flush();b=int(horn.stdout.readline())
  assert len(a)==7 and a[0]<=b,(args,a,b)
  rows.append({'input':args,'brute_best':a[0],'horn_bound':b,'compatible':a[1],'feasible':a[2],'point_scores':a[3],'profile_counts':a[4:]})
  print(json.dumps({'done':len(rows),'of':len(cases),'seconds':time.time()-start,'input':args,'brute_best':a[0],'horn_bound':b,'feasible':a[2]}),flush=True)
 brute.stdin.close();horn.stdin.close();assert brute.wait()==horn.wait()==0
result={'status':'PASS','scope':'small exact independent challenge of horn upper-bound coverage, not global proof','cases':len(rows),'feasible_ideals':sum(r['feasible'] for r in rows),'individual_point_scores':sum(r['point_scores'] for r in rows),'strict_overbounds':sum(r['brute_best']<r['horn_bound'] for r in rows),'rows':rows,'seconds':time.time()-start}
(root/'brute_plane_cylinder_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}),flush=True)
