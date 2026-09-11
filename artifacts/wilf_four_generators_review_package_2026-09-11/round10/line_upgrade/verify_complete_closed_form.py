#!/usr/bin/env python3
"""Fresh all-case replay, Python standard library plus a C++17 compiler only."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import time

HERE=Path(__file__).resolve().parent
manifest=json.loads((HERE/'closed_form_manifest.json').read_text())
for name,digest in manifest['files'].items():
    assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest, ('manifest mismatch',name)
expected=[json.loads(l)for l in (HERE/'independent_verification.jsonl').read_text().splitlines()]
compiler=shutil.which('g++')or shutil.which('clang++')
if compiler is None:raise RuntimeError('A C++17 compiler (g++ or clang++) is required.')
started=time.monotonic()
with tempfile.TemporaryDirectory(prefix='wilf_closed_form_')as tmp:
    binary=str(Path(tmp)/'verify')
    subprocess.run([compiler,'-std=c++17','-O3',str(HERE/'independent_closed_form.cpp'),'-o',binary],check=True)
    run=subprocess.run([binary,tmp],capture_output=True,text=True,check=True)
    status=json.loads(run.stdout)
    assert status=={'status':'passed','profiles':1429,'exact_closed_form_centroid_checks':3742041,'floating_point_used':False}
    observed=[json.loads(l)for l in (Path(tmp)/'independent_verification.jsonl').read_text().splitlines()]
    assert observed==expected, 'Fresh coverage or histograms differ from the recorded run.'
    assert len(observed)==9
    assert sum(row['union']for row in observed)==3742041
    assert sum(row['pure_upgrade']for row in observed)==3741763
    assert sum(row['axes']for row in observed)==2090810
    assert all(row['minimum_union_minus_m_numerator']>=0 for row in observed)
    assert sum(1 for _ in (Path(tmp)/'axis_fallbacks_strong.jsonl').open())==278
out={'status':'passed','scope':'Fresh independent full enumeration and exact closed-form centroid verification',
     'total_shapes':3742041,'line_upgrade_at_least_m':3741763,'axis_gain_at_least_m':2090810,
     'axis_fallbacks':278,'uniform_centroid_surplus':'at least m','all_nine_coverage_records_and_histograms_match':True,
     'floating_point_used':False,'external_certificate_data_used':False,
     'elapsed_seconds':round(time.monotonic()-started,6),
     'source_sha256':manifest['files']['independent_closed_form.cpp']}
(HERE/'portable_replay_result.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
