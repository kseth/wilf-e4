"""Reproduce the finite certificate for the unbounded unit one-corner theorem."""
from pathlib import Path
import json
import subprocess
import tempfile
from one_corner_dp import maximize

base=Path(__file__).resolve().parent
with tempfile.TemporaryDirectory(prefix='wilf_unit_corner_') as folder:
    binary=Path(folder)/'unit_dp'
    subprocess.run(['c++','-O3','-std=c++17',str(base/'one_corner_unit_dp.cpp'),'-o',str(binary)],check=True)
    records={}
    for first,last,penalty,filename in [(3,16,1,'unit_target_strip.jsonl'),(14,34,3,'unit_decimation_strip.jsonl')]:
        raw=subprocess.check_output([str(binary),str(first),str(last),str(penalty)],text=True)
        rows=[json.loads(line) for line in raw.splitlines()]
        expected=[json.loads(line) for line in (base/filename).read_text().splitlines()]
        assert [r['R'] for r in rows]==list(range(first,last+1))
        assert len(rows)==len(expected)
        for row,old in zip(rows,expected):
            assert {k:v for k,v in row.items() if k!='seconds'}=={k:v for k,v in old.items() if k!='seconds'}
        records[penalty]=rows
    assert all(r['maximum']<=0 for r in records[3])
    assert all(r['maximum']<=0 for r in records[1] if r['R']>=7)
    for R in range(3,9):
        results=[]
        for a in range(1,R+2):
            for b in range(a,R+2):
                for c in range(b,R+2):
                    if a+b+c<=R+1:results.append(maximize((1,1,1),R,(a,b,c)))
        cpp=next(r for r in records[1] if r['R']==R)
        assert cpp['maximum']==max(r['maximum'] for r in results)
        assert cpp['corner_cases']==len(results)
        if R==6:assert max(r['maximum'] for r in results if r['corner']!=(1,1,1))==-1

R=6
T={(x,y,z) for x in range(R+1) for y in range(R+1-x) for z in range(R+1-x-y) if min(x,y,z)==0}
m=len(T);sigma=sum(map(sum,T));D=3*m*R-4*sigma
assert (m,sigma,D)==(64,273,60)
result={'status':'all exact finite certificate checks passed','unit_target_heights':[7,16],'decimation_strip_heights':[14,34],'decimation_base':17,'unbounded_theorem':'at most one interior corner and unit weights: m>=65 implies D>=m','sharp_obstruction':{'m':m,'R':R,'sigma':sigma,'D':D},'python_cpp_overlap_heights':[3,8]}
(base/'unit_one_corner_theorem_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
