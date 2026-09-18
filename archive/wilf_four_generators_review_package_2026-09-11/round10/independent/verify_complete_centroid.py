#!/usr/bin/env python3
"""Portable complete integer replay; Python standard library plus C++17 only."""
from pathlib import Path
from fractions import Fraction
import argparse
import hashlib
import json
import shutil
import subprocess
import tempfile

ROOT=Path(__file__).resolve().parent

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output-dir',type=Path,default=ROOT/'replay')
    ap.add_argument('--compiler',default='g++')
    args=ap.parse_args()
    output=args.output_dir.resolve()
    output.mkdir(parents=True,exist_ok=True)
    manifest=json.loads((ROOT/'source_manifest.json').read_text())
    for name,expected_hash in manifest['sha256'].items():
        assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==expected_hash,('source hash mismatch',name)
    expected=json.loads((ROOT/'expected_enumeration_counts.json').read_text())
    with tempfile.TemporaryDirectory(prefix='wilf_centroid_') as tmp:
        binary=Path(tmp)/'verify'
        subprocess.run([args.compiler,'-std=c++17','-O3',str(ROOT/'verify_two_centroids.cpp'),'-o',str(binary)],check=True)
        with (output/'progress.txt').open('w') as progress:
            process=subprocess.run([str(binary),str(output)],text=True,stdout=subprocess.PIPE,stderr=progress,check=True)
        result=json.loads(process.stdout)
        assert result['status']=='passed' and result['target']=='D>=m'
        assert result['shapes']==result['union_at_least_m']==3742041
        (output/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    actual=[json.loads(line) for line in (output/'coverage.jsonl').read_text().splitlines()]
    assert len(actual)==len(expected)==9
    for old,new in zip(expected,actual):
        for key,value in old.items():
            assert new[key]==value,('coverage mismatch',old['pid'],key)
        assert new['union_at_least_m']==new['remaining']
        assert new['min_combined_num']>=0
    worst={}
    for line in (output/'successive_extrema.jsonl').read_text().splitlines():
        point=json.loads(line)
        worst[point['pid']]=point
    assert len(worst)==9
    for pid,record in worst.items():
        T={tuple(x) for x in record['points']}
        m=len(T)
        s=[sum(t[i] for t in T) for i in range(3)]
        q=[max(t[i] for t in T) for i in range(3)]
        assert m==record['m'] and s==record['s'] and q==record['q']
        for t in T:
            for i in range(3):
                if t[i]:
                    predecessor=list(t);predecessor[i]-=1
                    assert tuple(predecessor) in T
        U=0;weighted=[0,0,0];base_tops=[0,0,0];length_sum=0
        for i in range(3):
            for t in T:
                successor=list(t);successor[i]+=1
                if tuple(successor) in T:
                    continue
                u=max((u for u in T if all(u[j]>=t[j] for j in range(3))),key=lambda u:(sum(u),u))
                L=t[i]+1
                length_sum+=L
                U+=L*(sum(u)-sum(t))
                for j in range(3):
                    weighted[j]+=L*u[j]
                    base_tops[j]+=L*t[j]
        assert length_sum==3*m and base_tops==[4*a for a in s]
        r=[weighted[j]-4*s[j] for j in range(3)]
        assert sum(r)==U and min(r)>=0
        G=max(q)*(3*m-4*sum((Fraction(s[i],q[i]) for i in range(3)),Fraction(0)))
        assert U==record['U'] and G==Fraction(record['G_numerator'],record['G_denominator'])
        assert max(U,G)>=m
        record['G_exact']=str(G)
        record['max_U_G_minus_m']=str(max(U,G)-m)
        record['line_z_numerators']=weighted
        record['line_z_denominator']=3*m
        record['line_r']=r
        j=max(range(3),key=lambda i:q[i])
        lam=[Fraction(4*s[i],3*m*q[i]) for i in range(3)]
        lam[j]+=1-sum(lam)
        assert sum(lam)==1
        if G>=m:
            assert min(lam)>=0
            axis_r=[3*m*lam[i]*q[i]-4*s[i] for i in range(3)]
            assert all(axis_r[i]==(G if i==j else 0) for i in range(3))
        record['axis_vertex_weights']=[str(t) for t in lam]
        record['axis_witness_feasible']=min(lam)>=0
        new=actual[pid]
        assert max(U,G)-m==Fraction(new['min_combined_num'],new['min_combined_den'])
    (output/'worst_witnesses.json').write_text(json.dumps(list(worst.values()),indent=2)+'\n')
    summary={
        'status':'passed','target':'D>=m','source_hashes_verified':len(manifest['sha256']),
        'old_filter_and_histogram_records_matched':9,
        'total_shapes':sum(r['remaining'] for r in actual),
        'line_at_least_m':sum(r['line_at_least_m'] for r in actual),
        'axis_at_least_m':sum(r['axis_at_least_m'] for r in actual),
        'union_at_least_m':sum(r['union_at_least_m'] for r in actual),
        'per_corner_min_max_U_G_minus_m':[str(Fraction(r['min_combined_num'],r['min_combined_den'])) for r in actual],
        'worst_witnesses_recomputed_with_python_fractions':len(worst),
        'lp_data_required':False,'old_archive_required':False,
    }
    (output/'comparison_result.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))

if __name__=='__main__':
    main()
