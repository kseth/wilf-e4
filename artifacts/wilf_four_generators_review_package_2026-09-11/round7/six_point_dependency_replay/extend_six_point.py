"""Complete deficient staircase extensions of the six-point maximal sets."""
from itertools import permutations
from collections import Counter
from pathlib import Path
from time import perf_counter
import json

from verify_final_window import all_negative_extensions
from wilf_reassessment import corners


def canonical_pair(t,z):
    pairs=[]
    for p in permutations(range(3)):
        tt=tuple(sorted(tuple(x[j] for j in p) for x in t))
        zz=tuple(sorted(tuple(x[j] for j in p) for x in z))
        pairs.append((tt,zz))
    return min(pairs)


def main():
    seeds=[tuple(map(tuple,z)) for z in json.loads(Path('six_negative_expanded.json').read_text())]
    shape_pairs={};hist=Counter();total=0;valid=0;start=perf_counter()
    for idx,z in enumerate(seeds):
        ts=all_negative_extensions(z)
        total+=len(ts)
        for t in ts:
            hist[len(t)]+=1
            if not all(tuple(int(i==j) for i in range(3)) in t for j in range(3)):continue
            if len([p for p in corners(t) if all(p)])>1:continue
            valid+=1
            tt,zz=canonical_pair(t,z)
            shape_pairs.setdefault(tt,set()).add(zz)
        if idx%200==0:
            print(json.dumps(dict(processed=idx,total_pairs=total,valid_pairs=valid,
                                  shapes=len(shape_pairs),seconds=perf_counter()-start)),flush=True)
    records=[dict(T=tt,Zs=sorted(zs),m=len(tt)) for tt,zs in sorted(shape_pairs.items())]
    Path('six_candidate_shapes.json').write_text(json.dumps(records)+'\n')
    result=dict(expanded_seeds=len(seeds),all_pairs=total,
                pair_size_histogram=hist,maximum_size=max(hist),
                valid_pairs_before_symmetry=valid,unique_shapes=len(records),
                unique_pairs=sum(len(r['Zs']) for r in records),
                elapsed_seconds=perf_counter()-start)
    Path('six_extension_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)


if __name__=='__main__':main()
