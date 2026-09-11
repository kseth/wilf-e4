"""Third implementation audit: exact retained-point sums and explicit transitions.

The separate structural auditor checks every leaf and full tree coverage.
This script provides a stratified sample with a different moment/DP algorithm.
"""
from pathlib import Path
import json
import subprocess
import tempfile

base=Path(__file__).resolve().parent
source=base.parents[1]/'one_corner_extension'/'short_corner_complete_certificate.json'
cert=json.loads(source.read_text());q=cert['scale']
leaves=[(i,n) for i,n in enumerate(cert['tree']) if n['kind']=='dp']
indices=sorted({round(j*(len(leaves)-1)/99) for j in range(100)})
rows=[]
with tempfile.TemporaryDirectory(prefix='wilf_independent_corner_') as tmp:
    worker=Path(tmp)/'worker'
    subprocess.run(['c++','-O3','-std=c++17',str(base/'independent_interval_worker.cpp'),'-o',str(worker)],check=True)
    proc=subprocess.Popen([str(worker)],stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True)
    for k in indices:
        node_id,node=leaves[k]
        lo,hi=node['box'];b0,c0,h0=lo;b1,c1,h1=hi
        low=(b0,max(b0,c0),max(b0,c0,h0));high=(min(b1,c1,h1),min(c1,h1),h1)
        proc.stdin.write(' '.join(map(str,(q,*low,*high)))+'\n');proc.stdin.flush()
        got=list(map(int,proc.stdout.readline().split()))
        assert got==node['bounds'],(node_id,got,node['bounds'])
        assert max(got)<=q
        rows.append({'node_id':node_id,'lower':low,'upper':high,'bounds':got})
    proc.stdin.close();assert proc.wait()==0
out={'status':'all 100 independent exact sample checks passed','scope':'stratified sample of DP leaves; separate auditor verifies all leaves and coverage','method':'retained-point prefix sums/maxima and explicit rectangle transitions','scale':q,'total_dp_leaves':len(leaves),'sampled_leaves':len(rows),'results':rows}
(base/'independent_interval_sample_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items() if k!='results'})
