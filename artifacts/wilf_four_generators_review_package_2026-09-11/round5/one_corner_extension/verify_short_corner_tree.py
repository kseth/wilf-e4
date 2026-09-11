"""Independent exact tree/coverage verification, plus complete worker replay.

The C++ worker is separately audited; this script itself imports no
generating code and checks every closed parameter-box boundary.
"""
from pathlib import Path
from collections import Counter
import json,subprocess,time


def verify(path,worker_path):
    start=time.time();data=json.loads(Path(path).read_text());q=data['scale'];tree=data['tree']
    assert data['complete'] and not data['unresolved']
    initial=[[q,q,6*q],[42*q,42*q,42*q]];assert data['initial']==initial
    worker=subprocess.Popen([worker_path],stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True,bufsize=1)
    queue=[(0,initial)];seen=set();kinds=Counter();max_bound=None
    while queue:
        idx,expected=queue.pop();assert idx not in seen;seen.add(idx)
        node=tree[idx];assert node and node['box']==expected
        (b0,c0,h0),(b1,c1,h1)=expected
        lo=[b0,max(b0,c0),max(b0,c0,h0)];hi=[min(b1,c1,h1),min(c1,h1),h1]
        kind=node['kind'];kinds[kind]+=1
        if kind=='empty':assert any(a>b for a,b in zip(lo,hi));continue
        assert all(a<=b for a,b in zip(lo,hi))
        if kind=='split':
            axis=node['axis'];mid=node['mid'];ids=node['children']
            assert axis in (0,1,2) and lo[axis]<mid<hi[axis] and len(ids)==2
            first_hi=hi.copy();first_hi[axis]=mid
            second_lo=lo.copy();second_lo[axis]=mid
            queue.append((ids[0],[lo,first_hi]));queue.append((ids[1],[second_lo,hi]))
        elif kind=='planar':
            assert lo[2]>=3*q+4*(q+hi[0]+hi[1])
        elif kind=='dp':
            worker.stdin.write(' '.join(map(str,(q,*lo,*hi)))+'\n');worker.stdin.flush()
            bounds=list(map(int,worker.stdout.readline().split()))
            assert len(bounds)==3 and bounds==node['bounds'] and max(bounds)<=q
            max_bound=max(bounds) if max_bound is None else max(max_bound,max(bounds))
        else:raise AssertionError(kind)
    worker.stdin.close();assert worker.wait()==0
    assert len(seen)==len(tree)==data['nodes']
    return {'passed':True,'scope':data['scope'],'nodes':len(tree),'kinds':dict(kinds),'largest_bound_numerator':max_bound,'scale':q,'seconds':time.time()-start}


if __name__=='__main__':
    here=Path(__file__).parent
    result=verify(here/'short_corner_complete_certificate.json',str(here/'corner_interval_worker'))
    (here/'short_corner_tree_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
