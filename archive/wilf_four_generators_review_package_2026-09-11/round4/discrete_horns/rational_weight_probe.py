from weighted_dp import maximize
from weighted_size_dp import maximize_min_size
from pathlib import Path
import json
q=10;tested=0;inconclusive=0;worst=None;counter=None
# Structured exact rational diagnostic around low normalized heights.
for M in range(4*q,9*q+1):
 for b in range(q,2*q+1):
  for c in range(b,3*q+1):
   tested+=1
   out=maximize((q,b,c),M,penalty=q)
   if out['maximum']<=q:continue
   lag=maximize((q,b,c),M,penalty=2*q)
   if lag['maximum']-30*q<=q:continue
   inconclusive+=1
   exact=maximize_min_size((q,b,c),M,penalty=q)
   if exact['feasible'] and (worst is None or exact['maximum']>worst['maximum']):worst=exact
   if exact['feasible'] and exact['maximum']>q:
    counter=exact;break
  if counter:break
 if counter:break
result={'scope':'structured finite rational grid, not a universal weighted theorem','normalization_denominator':q,'tested':tested,'size_dp_calls':inconclusive,'worst_constrained':worst,'counterexample_parameters':counter}
Path(__file__).with_name('rational_weight_probe_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
