"""Independent complete coverage and ALL-leaf DP audit for the 211 theorem."""
from collections import Counter,deque
from pathlib import Path
import hashlib
import json
import subprocess
import tempfile
import time
from independent_interval_dp import tighten

base=Path(__file__).resolve().parent
source=base.parent/'one_corner_extension'/'short_corner_complete_certificate.json'
raw=source.read_bytes();cert=json.loads(raw);q=cert['scale'];tree=cert['tree']
root=[[q,q,6*q],[42*q,42*q,42*q]]
assert cert['initial']==root and cert['complete'] and cert['unresolved']==[]
pending=deque([(0,root)]);visited=set();kinds=Counter();dp=[]
start=time.time()
while pending:
    node_id,wanted=pending.popleft()
    assert isinstance(node_id,int) and 0<=node_id<len(tree)
    assert node_id not in visited;visited.add(node_id)
    node=tree[node_id];assert node['box']==wanted
    box=tighten(*wanted);kind=node['kind'];kinds[kind]+=1
    if box is None:
        assert kind=='empty';continue
    lo,hi=map(list,box)
    if kind=='split':
        axis,mid=node['axis'],node['mid'];children=node['children']
        assert axis in (0,1,2) and lo[axis]<mid<hi[axis]
        assert len(children)==2 and children[0]!=children[1]
        left_hi=hi.copy();right_lo=lo.copy();left_hi[axis]=right_lo[axis]=mid
        pending.append((children[0],[lo,left_hi]))
        pending.append((children[1],[right_lo,hi]))
    elif kind=='planar':
        assert lo[2]>=3*q+4*(q+hi[0]+hi[1])
    elif kind=='dp':
        assert len(node['bounds'])==3 and max(node['bounds'])<=q
        dp.append((lo,hi,node['bounds']))
    else:
        raise AssertionError(kind)
assert len(visited)==len(tree)==cert['nodes']
print(json.dumps({'coverage':'PASS','nodes':len(tree),'kinds':dict(kinds)}),flush=True)

with tempfile.TemporaryDirectory(prefix='independent_211_') as temp:
    binary=Path(temp)/'checker'
    subprocess.run(['c++','-O3','-std=c++17','-Wall','-Wextra','-pedantic',
                    str(base/'independent_clipped_worker.cpp'),'-o',str(binary)],check=True)
    request=''.join(' '.join(map(str,(q,*lo,*hi)))+'\n' for lo,hi,_ in dp)
    response=subprocess.run([str(binary)],input=request,text=True,capture_output=True,check=True)
    rows=response.stdout.splitlines()
    assert len(rows)==len(dp)
    largest=None
    for (lo,hi,wanted),row in zip(dp,rows):
        computed=list(map(int,row.split()))
        assert computed==wanted,(lo,hi,wanted,computed)
        assert max(computed)<=q
        largest=max(computed) if largest is None else max(largest,max(computed))
result={'status':'PASS','scope':'independent complete coverage and every DP leaf; three corner permutations',
        'nodes':len(tree),'node_kinds':dict(kinds),'corner_bounds_checked':3*len(dp),
        'scale':q,'largest_bound':largest,'certificate_sha256':hashlib.sha256(raw).hexdigest(),
        'seconds':time.time()-start}
(base/'complete_short_corner_audit_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
