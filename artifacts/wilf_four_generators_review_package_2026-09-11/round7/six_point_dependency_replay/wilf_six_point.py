"""Six-point research and verification utilities.

Proofs of completeness and the one-corner completion criterion are recorded in
the accompanying research note. No unrestricted Wilf claim is made here.
"""
from itertools import combinations,permutations,product
from collections import Counter
from pathlib import Path
from time import perf_counter
import json

from wilf_work import canonical,lower_hull,projection_score
from wilf_reassessment import corners,maximal,projected_grid_witness


def score(z):
    k=len(z)
    E=sum(map(sum,z))-sum(max(p[j] for p in z) for j in range(3))
    B=0
    for i,j in ((0,1),(0,2),(1,2)):
        levels=sorted({p[i] for p in z})
        prev=-1
        for x in levels:
            ymax=max(p[j] for p in z if p[i]>=x)
            B+=(x-prev)*(ymax+1)
            prev=x
    return B-3*k-E


def one_corner_completion(z):
    """Necessary and sufficient for Z to be maximal in some <=1-corner ideal.

    Returns the largest feasible corner parameter, or None if there is no
    required interior cut. An explicit failure reason means no completion.
    """
    forced=[]
    for k in range(3):
        others=[j for j in range(3) if j!=k]
        for v in z:
            if all(any(w[j]>=v[j] and w[k]>v[k] for w in z) for j in others):
                forced.append((k,v))
    if not forced:return dict(feasible=True,corner=None,forced=[])
    p=[]
    for j in range(3):
        required={v[j]+1 for k,v in forced if k==j}
        upper=min((v[j] for k,v in forced if k!=j),default=None)
        if len(required)>1:
            return dict(feasible=False,reason='distinct_required_heights',direction=j)
        if required:
            val=next(iter(required))
            if upper is not None and val>upper:
                return dict(feasible=False,reason='incompatible_corner_coordinates',direction=j)
        else:
            assert upper is not None
            val=upper
        if val<1:return dict(feasible=False,reason='nonpositive_corner')
        p.append(val)
    if any(all(u<=v for u,v in zip(p,zv)) for zv in z):
        return dict(feasible=False,reason='corner_would_remove_Z')
    return dict(feasible=True,corner=tuple(p),forced=forced)


def build_completion(z,parameter):
    U=lower_hull(z)
    proj={ij:{tuple(x[j] for j in ij) for x in U} for ij in ((0,1),(0,2),(1,2))}
    V={x for x in product(*(range(1+max(v[j] for v in z)) for j in range(3)))
       if all(tuple(x[j] for j in ij) in pp for ij,pp in proj.items())}
    p=parameter['corner']
    return {x for x in V if p is None or not all(a>=b for a,b in zip(x,p))}


def expand(seeds):
    seen=set(seeds);queue=sorted(seen)
    start=perf_counter()
    for idx,z in enumerate(queue):
        before=score(z)
        assert before<0 and one_corner_completion(z)['feasible']
        for j in range(3):
            for h in sorted({x[j] for x in z}):
                q=canonical(tuple(tuple(v+(i==j and v>=h) for i,v in enumerate(x)) for x in z))
                after=score(q)
                assert after>before
                if after<0 and q not in seen:
                    assert one_corner_completion(q)['feasible']
                    seen.add(q);queue.append(q)
        if idx and idx%2000==0:
            print(json.dumps(dict(processed=idx,discovered=len(queue),seconds=perf_counter()-start)),flush=True)
    return sorted(seen)


def main(seed_file='six_compressed_recheck.json'):
    raw=[tuple(map(tuple,z)) for z in json.loads(Path(seed_file).read_text())]
    assert all(score(z)==projection_score(z) for z in raw)
    counts=Counter()
    seeds=[]
    for z in raw:
        r=one_corner_completion(z)
        counts['feasible' if r['feasible'] else r['reason']]+=1
        if r['feasible']:
            assert projected_grid_witness(z) is None
            T=build_completion(z,r)
            assert set(z)<=set(maximal(T))
            assert len([x for x in corners(T) if all(x)])<=1
            seeds.append(z)
    print(json.dumps(dict(raw=len(raw),completion_counts=counts,
                         minimum_score=min(map(score,seeds)))),flush=True)
    expanded=expand(seeds)
    Path('six_negative_expanded.json').write_text(json.dumps(expanded)+'\n')
    result=dict(raw_negative_compressed=len(raw),completion_counts=counts,
                feasible_compressed=len(seeds),negative_expanded=len(expanded),
                score_histogram=Counter(map(score,expanded)),
                maximum_U_size=max(len(lower_hull(z)) for z in expanded))
    Path('six_expansion_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)


if __name__=='__main__':main()
