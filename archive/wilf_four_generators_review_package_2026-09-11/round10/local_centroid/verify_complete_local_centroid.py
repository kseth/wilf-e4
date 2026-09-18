#!/usr/bin/env python3
"""Fresh independent full replay. Requires Python stdlib and a C++17 compiler."""
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import time

HERE=Path(__file__).resolve().parent
manifest=json.loads((HERE/'local_centroid_manifest.json').read_text())
for name,digest in manifest['files'].items():
    assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest, ('manifest mismatch',name)
expected=[json.loads(l)for l in (HERE/'two_step_verification.jsonl').read_text().splitlines()]
compiler=shutil.which('g++')or shutil.which('clang++')
if compiler is None:raise RuntimeError('A C++17 compiler (g++ or clang++) is required.')
started=time.monotonic()
with tempfile.TemporaryDirectory(prefix='wilf_local_centroid_')as tmp:
    binary=str(Path(tmp)/'verify')
    subprocess.run([compiler,'-std=c++17','-O3',str(HERE/'independent_two_step.cpp'),'-o',binary],check=True)
    run=subprocess.run([binary,tmp],capture_output=True,text=True,check=True)
    status=json.loads(run.stdout)
    assert status=={'status':'passed','profiles':1429,'exact_two_step_centroid_checks':5574644,'floating_point_used':False}
    observed=[json.loads(l)for l in (Path(tmp)/'two_step_verification.jsonl').read_text().splitlines()]
    assert observed==expected, 'Fresh coverage or multiplicity histograms differ.'
    assert len(observed)==9
    assert sum(r['union']for r in observed)==5574644
    assert sum(r['two_step_upgrade']for r in observed)==5574213
    assert sum(r['axes']for r in observed)==3011728
    assert all(r['minimum_union_minus_m_numerator']>=0 for r in observed)
    fallbacks=[json.loads(l)for l in (Path(tmp)/'axis_fallbacks_strong.jsonl').read_text().splitlines()]
    assert len(fallbacks)==431
    for row in fallbacks:
        T=set(map(tuple,row['points']));m=len(T)
        assert m==row['m']
        q=[max(x[i]for x in T)for i in range(3)]
        s=[sum(x[i]for x in T)for i in range(3)]
        G=max(q)*(3*m-4*sum(Fraction(s[i],q[i])for i in range(3)))
        assert G==Fraction(row['axis_numerator'],row['axis_denominator']) and G>=m
        gain=0
        for t in T:
            one=[tuple(v+(i==j)for j,v in enumerate(t))for i in range(3)]
            two=[tuple(v+(i==j)+(k==j)for j,v in enumerate(t))for i in range(3)for k in range(i,3)]
            step=2 if any(x in T for x in two)else 1 if any(x in T for x in one)else 0
            gain+=sum(t[i]+1 for i in range(3)if one[i]not in T)*step
        assert gain==row['gain'] and gain<m
    for name in ['axis_fallbacks_strong.jsonl','cheap_bound_exceptions_strong.jsonl']:
        data=(Path(tmp)/name).read_bytes()
        for line in data.splitlines():json.loads(line)
        (HERE/name).write_bytes(data)
out={'status':'passed','scope':'Fresh independent complete enumeration of the larger class; direct local successor tests',
     'total_shapes':5574644,'local_two_step_gain_at_least_m':5574213,'axis_gain_at_least_m':3011728,
     'axis_fallbacks':431,'all_fallbacks_independently_reconstructed_with_python_fractions':True,
     'uniform_centroid_surplus':'at least m','all_nine_coverage_records_and_histograms_match':True,
     'erosion_filter_used':False,'refined_dominating_corner_filter_used':False,
     'floating_point_used':False,'external_certificate_data_used':False,
     'elapsed_seconds':round(time.monotonic()-started,6),
     'source_sha256':manifest['files']['independent_two_step.cpp']}
(HERE/'portable_replay_result.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
