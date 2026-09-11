"""Generate exact global moment certificates and a separate modular check."""
from pathlib import Path
from itertools import permutations
import json
from verify_final_window import boundary_slacks
from wilf_reassessment import geometric_optimum,ordered_geometric_optimum


def main():
    rows=json.loads(Path('six_residue_labels.json').read_text())
    shapes=json.loads(Path('six_candidate_shapes.json').read_text())
    records=[];cut_count=0;min_slack=None;bad=[]
    for idx,a,b,c in rows:
        t={tuple(x) for x in shapes[idx]['T']}
        slacks=boundary_slacks(t,(a,b,c));cut_count+=len(slacks)
        min_slack=min(slacks) if min_slack is None else min(min_slack,min(slacks))
        if min(slacks)<0:bad.append((idx,a,b,c,min(slacks)))
        records.append(dict(shape=idx,A=(a,b,c),slacks=slacks))
    geo=[]
    for idx in sorted({r[0] for r in rows}):
        t={tuple(x) for x in shapes[idx]['T']}
        eta=geometric_optimum(t);perms=[]
        if not eta['sufficient']:
            for p in permutations(range(3)):
                r=ordered_geometric_optimum({tuple(x[j] for j in p) for x in t})
                perms.append(dict(permutation=p,certificate=r))
        geo.append(dict(shape=idx,geometric=eta,ordered=perms))
    result=dict(residue_shapes=len(geo),labelings=len(rows),cut_count=cut_count,
        minimum_boundary_slack=min_slack,boundary_failures=bad,
        normalized_geometry_passes=sum(r['geometric']['sufficient'] for r in geo),
        ordered_geometry_failures=[r['shape'] for r in geo if any(not p['certificate']['sufficient'] for p in r['ordered'])],
        boundary_records=records,geometric_records=geo)
    assert not result['boundary_failures'] and not result['ordered_geometry_failures']
    Path('six_arithmetic_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('boundary_records','geometric_records')}),flush=True)


if __name__=='__main__':main()
