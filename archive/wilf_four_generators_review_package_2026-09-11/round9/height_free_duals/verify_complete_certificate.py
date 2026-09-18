#!/usr/bin/env python3
"""Portable complete replay; standard-library Python and a C++17 compiler only."""
import argparse, hashlib, json, pathlib, shutil, subprocess, tempfile
HERE=pathlib.Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument('--records-only',action='store_true',help='Check archived output records without recomputing the independent verifier.')
args=parser.parse_args()
manifest=json.loads((HERE/'certificate_manifest.json').read_text())
for name,want in manifest.items():
    assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==want,('hash mismatch',name)
def records(path):return [json.loads(s) for s in path.read_text().splitlines()]
source=records(HERE/'certification.jsonl')
run_summary=None
if args.records_only:
    replay=records(HERE/'independent_verification.jsonl')
else:
    with tempfile.TemporaryDirectory(prefix='wilf_height_free_') as name:
        work=pathlib.Path(name)
        for filename in ('dual_bases.jsonl','dual_assignments.bin'):
            shutil.copyfile(HERE/filename,work/filename)
        exe=work/'independent_verify'
        subprocess.run(['c++','-O3','-std=c++17',str(HERE/'independent_verify_height_free.cpp'),'-o',str(exe)],check=True)
        result=subprocess.run([str(exe),str(work)],check=True,text=True,stdout=subprocess.PIPE)
        run_summary=json.loads(result.stdout)
        assert run_summary=={'status':'passed','profiles':1429,'bases':6816,'exact_weighted_duals':3742041,'floating_point_used':False},run_summary
        replay=records(work/'independent_verification.jsonl')
assert len(source)==len(replay)==9
corners=[(a,b,P-a-b) for P in range(5,8) for a in range(1,P+1) for b in range(a,P+1) if P-a-b>=b]
for pid,(x,y,corner) in enumerate(zip(source,replay,corners)):
    assert x['pid']==y['pid']==pid and x['corner']==y['corner']==list(corner)
    for k,v in y.items():assert x[k]==v,(pid,k,x[k],v)
    assert sum(y['histogram'].values())==y['remaining']==y['q_ok']
    assert y['certificate_min_numerator']>=0 and y['certificate_min_denominator']>0
keys=['compatible','degree_ok','m30','erosion_ok','q_ok','six_maxima','remaining']
totals={k:sum(x[k] for x in replay) for k in keys}
assert totals=={'compatible':55199298,'degree_ok':17808013,'m30':17727110,'erosion_ok':12575521,'q_ok':3742041,'six_maxima':380607,'remaining':3742041}
assert (HERE/'dual_assignments.bin').stat().st_size==4*3742041
bs=records(HERE/'dual_bases.jsonl');assert len(bs)==6816
assert all(346 not in x['columns'] and 347 not in x['columns'] and sum(c<343 for c in x['columns'])<=3 for x in bs)
print(json.dumps({'status':'passed','full_independent_recomputation_this_run':not args.records_only,'run_summary':run_summary,'all_coverage_fields_and_histograms_match':True,'totals':totals,'exact_weighted_target':'D >= m-29/10 for all b_i>=1, no upper bound on H','centroid_witness_uses_at_most_three_points':True,'manifest_files_checked':len(manifest)},indent=2))
