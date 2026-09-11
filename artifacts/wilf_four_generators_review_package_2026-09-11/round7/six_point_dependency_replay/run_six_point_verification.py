"""Regenerate and verify the complete finite part of the |Z| <= 6 theorem.

Requirements: Python 3, SciPy (certificate discovery only), and a C++17 compiler.
Run without Python's -O flag: exact verification uses assertions throughout.
The analytic reductions and the separate column theorem are in the research note.
"""
from pathlib import Path
from time import perf_counter
import json,os,platform,subprocess,sys


def main():
    if not __debug__:
        raise RuntimeError('Do not disable assertions with Python -O.')
    root=Path(__file__).resolve().parent
    os.chdir(root)
    started=perf_counter()
    stages=[]

    def run(args,log,stdin=None):
        start=perf_counter()
        with Path(log).open('w') as out:
            subprocess.run(args,stdin=stdin,stdout=out,stderr=subprocess.STDOUT,check=True)
        record=dict(command=args,log=log,seconds=perf_counter()-start)
        stages.append(record)
        print(json.dumps(record),flush=True)

    # This repeats the earlier <=5 proof so the package covers the whole claim.
    run([sys.executable,'verify_final_window.py'],'verification-run.log')
    for source,binary in [('enumerate_compressed.cpp','enumerate_compressed_recheck'),
                          ('check_residue_labels.cpp','check_six_residue_labels')]:
        subprocess.run(['c++','-O3','-std=c++17',source,'-o',binary],check=True)
    start=perf_counter()
    with Path('six_compressed_recheck.json').open('w') as out, \
         Path('six_compressed_recheck.log').open('w') as err:
        subprocess.run(['./enumerate_compressed_recheck','6'],stdout=out,stderr=err,check=True)
    assert 'canonical=345988 negative=2264 ' in Path('six_compressed_recheck.log').read_text()
    assert len(json.loads(Path('six_compressed_recheck.json').read_text()))==2264
    stages.append(dict(stage='compressed-six',seconds=perf_counter()-start))
    print(json.dumps(stages[-1]),flush=True)
    run([sys.executable,'wilf_six_point.py'],'six_expansion_run.log')
    result=json.loads(Path('six_expansion_results.json').read_text())
    assert (result['feasible_compressed'],result['negative_expanded'])==(891,4406)
    run([sys.executable,'extend_six_point.py'],'six_extension_run.log')
    result=json.loads(Path('six_extension_results.json').read_text())
    assert (result['all_pairs'],result['unique_shapes'],result['unique_pairs'])==(11790,5331,5962)
    shapes=json.loads(Path('six_candidate_shapes.json').read_text())
    assert max(r['m'] for r in shapes)==56
    with Path('six_residue_input.txt').open('w') as out:
        out.write(str(len(shapes))+'\n')
        for rec in shapes:
            out.write(str(rec['m'])+'\n')
            for x in rec['T']:out.write(' '.join(map(str,x))+'\n')
    with Path('six_residue_input.txt').open() as src:
        run(['./check_six_residue_labels'],'six_residue_labels.json',stdin=src)
    labels=json.loads(Path('six_residue_labels.json').read_text())
    assert len(labels)==930 and len({r[0] for r in labels})==71
    run([sys.executable,'certify_six_point.py'],'six_arithmetic_run.log')
    run([sys.executable,'verify_six_certificates.py'],'six_certificate_verification.log')
    run([sys.executable,'verify_corner_completion.py'],'corner_completion_verification.log')
    run([sys.executable,'wilf_column_bound.py'],'column_bound_run.log')
    import scipy
    result=dict(status='PASS',scope='Computer-assisted Wilf theorem for e=4 and |Z|<=6; '
                'analytic sufficient column theorem for e>=4',
                python=platform.python_version(),scipy=scipy.__version__,
                platform=platform.platform(),stages=stages,seconds=perf_counter()-started)
    Path('six_full_run_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)


if __name__=='__main__':main()
