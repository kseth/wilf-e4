from one_corner_dp import maximize
from pathlib import Path
import json
out=[]
for R in range(3,8):
    rows=[]
    for a in range(1,R+2):
        for b in range(a,R+2):
            for c in range(b,R+2):
                if a+b+c<=R+1:rows.append(maximize((1,1,1),R,(a,b,c),penalty=1,moment_multiplier=0,height_multiplier=0))
    best=max(rows,key=lambda r:r['maximum'])
    assert best['maximum']==best['maximizer_size']
    out.append({'R':R,'maximum_cardinality':best['maximum'],'witness_corner':best['corner'],'all_corners':rows})
assert [r['maximum_cardinality'] for r in out]==[19,31,48,71,101]
Path(__file__).with_name('one_corner_cardinality_results.json').write_text(json.dumps(out,indent=2)+'\n')
print([(r['R'],r['maximum_cardinality']) for r in out])
