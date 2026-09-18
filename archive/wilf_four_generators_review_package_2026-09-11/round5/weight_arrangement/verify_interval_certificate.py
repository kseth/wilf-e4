"""Independent exact checker of the complete parameter-box certificate.

Imports no generating program. Checks the rooted binary partition tree,
including all closed boundaries and all order-cone clipping, then checks
every accepted leaf by an independently written flat-array horn DP.
"""
import json
from pathlib import Path
from collections import Counter
import time


def clip(lower,upper):
    b0,c0,h0=lower; b1,c1,h1=upper
    return [b0,max(b0,c0),max(b0,c0,h0)],[min(b1,c1,h1),min(c1,h1),h1]


def bound_score(lower,upper,q):
    feasible=(q,lower[0],lower[1]); objective=(q,upper[0],upper[1])
    height=upper[2]; offset=q-3*lower[2]
    lim=tuple(height//a for a in feasible)
    all_horns=[]
    for axis in (0,1,2):
        other=tuple(j for j in (0,1,2) if j!=axis)
        nb,nc=lim[other[0]]+1,lim[other[1]]+1
        layers=[[0]*(nb*nc) for _ in range(lim[axis]+2)]
        for t in reversed(range(lim[axis]+1)):
            data=layers[t]; tail=layers[t+1]
            for u in range(nb):
                row_best=0
                for v in range(nc):
                    index=u*nc+v
                    if feasible[axis]*t+feasible[other[0]]*u+feasible[other[1]]*v<=height:
                        n=(u+1)*(v+1)
                        # Rectangle sum: n times the midpoint of its coordinates.
                        slice_score=n*(offset+4*objective[axis]*t+2*objective[other[0]]*u+2*objective[other[1]]*v)
                        row_best=max(row_best,slice_score+tail[index])
                    data[index]=max(row_best,data[index-nc] if u else 0)
        all_horns.append((layers,nc))
    result=None
    for x in range(lim[0]+1):
        for y in range(lim[1]+1):
            for z in range(lim[2]+1):
                coords=(x,y,z)
                if sum(a*t for a,t in zip(feasible,coords))>height: continue
                n=(x+1)*(y+1)*(z+1)
                score=n*(offset+2*sum(a*t for a,t in zip(objective,coords)))
                for axis in (0,1,2):
                    other=tuple(j for j in (0,1,2) if j!=axis)
                    layers,nc=all_horns[axis]
                    score+=layers[coords[axis]+1][coords[other[0]]*nc+coords[other[1]]]
                result=score if result is None else max(result,score)
    return result


def verify_small_degree_cardinality():
    # Independent central-box cardinality bound at total degree 4.
    R=4; best=0
    for x in range(R+1):
        for y in range(R+1-x):
            for z in range(R+1-x-y):
                c=(x,y,z); size=(x+1)*(y+1)*(z+1)
                for axis in (0,1,2):
                    other=tuple(j for j in (0,1,2) if j!=axis)
                    for t in range(c[axis]+1,R+1):
                        choices=[(u+1)*(v+1) for u in range(c[other[0]]+1) for v in range(c[other[1]]+1) if t+u+v<=R]
                        size+=max(choices,default=0)
                best=max(best,size)
    assert best==29
    return best


def verify(path):
    start=time.time(); cert=json.loads(Path(path).read_text())
    q=cert['scale']; tree=cert['tree']; seen=set(); kinds=Counter()
    assert cert['complete'] and not cert['unresolved']
    assert cert['initial']==[[q,q,5*q],[24*q,24*q,24*q]]
    pending=[(0,cert['initial'])]; largest_bound=None
    while pending:
        node_id,expected=pending.pop()
        assert node_id not in seen; seen.add(node_id)
        node=tree[node_id]; assert node is not None and node['box']==expected
        raw_lo,raw_hi=node['box']; lower,upper=clip(raw_lo,raw_hi)
        kind=node['kind']; kinds[kind]+=1
        if kind=='empty':
            assert any(x>y for x,y in zip(lower,upper)); continue
        assert all(x<=y for x,y in zip(lower,upper))
        if kind=='split':
            axis=node['axis']; mid=node['mid']; children=node['children']
            assert axis in (0,1,2) and lower[axis]<mid<upper[axis]
            assert len(children)==2 and children[0]!=children[1]
            first_hi=upper.copy(); first_hi[axis]=mid
            second_lo=lower.copy(); second_lo[axis]=mid
            pending.append((children[0],[lower,first_hi]))
            pending.append((children[1],[second_lo,upper]))
        elif kind=='continuous':
            assert lower[2]>=2*(q+upper[0]+upper[1])+3*q
        elif kind=='dp':
            value=bound_score(lower,upper,q)
            assert value==node['bound'] and value<=q
            largest_bound=value if largest_bound is None else max(value,largest_bound)
        else:
            raise AssertionError(kind)
    assert len(seen)==len(tree)==cert['nodes']
    assert sum(v for k,v in kinds.items() if k!='split')==cert['leaf_count']
    result={'passed':True,'scope':'all real 1<=b<=c<=M with 5<=M<=24','tree_nodes':len(tree),'kinds':dict(kinds),'largest_dp_bound_numerator':largest_bound,'scale':q,'degree_four_max_cardinality':verify_small_degree_cardinality(),'seconds':time.time()-start}
    return result


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(); parser.add_argument('certificate',nargs='?',default=str(Path(__file__).with_name('full_interval_certificate.json')))
    args=parser.parse_args(); result=verify(args.certificate)
    Path(__file__).with_name('independent_interval_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
