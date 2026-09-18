"""Exact no-interior ideal DP for fixed integer weights and height allowance.

The objective is sum_T(4*w(x)-3*M+penalty), additive over disjoint horns.
An exhaustive test over weight triples is not a proof for arbitrary weights.
"""
from itertools import product

def maximize(weights,M,penalty=1):
 caps=[M//w for w in weights]
 horns=[];counts=[]
 for axis in range(3):
  js=[j for j in range(3) if j!=axis];al=weights[axis];be,ga=[weights[j] for j in js]
  n=caps[axis]+1;nb,nc=[caps[j]+1 for j in js]
  H=[[[0]*nc for _ in range(nb)] for _ in range(n+1)]
  K=[[[0]*nc for _ in range(nb)] for _ in range(n+1)]
  for t in range(n-1,-1,-1):
   for b in range(nb):
    for c in range(nc):
     val=0;num=0
     if al*t+be*b+ga*c<=M:
      vol=(b+1)*(c+1)
      v=vol*(4*al*t+2*be*b+2*ga*c-3*M+penalty)+H[t+1][b][c]
      k=vol+K[t+1][b][c]
      if (v,k)>(val,num):val,num=v,k
     if b and (H[t][b-1][c],K[t][b-1][c])>(val,num):val,num=H[t][b-1][c],K[t][b-1][c]
     if c and (H[t][b][c-1],K[t][b][c-1])>(val,num):val,num=H[t][b][c-1],K[t][b][c-1]
     H[t][b][c]=val;K[t][b][c]=num
  horns.append(H);counts.append(K)
 best=-10**100;size=0;center=None
 for a,b,c in product(*(range(cap+1) for cap in caps)):
  height=sum(x*w for x,w in zip((a,b,c),weights))
  if height>M:continue
  vol=(a+1)*(b+1)*(c+1)
  score=vol*(2*height-3*M+penalty)+horns[0][a+1][b][c]+horns[1][b+1][a][c]+horns[2][c+1][a][b]
  count=vol+counts[0][a+1][b][c]+counts[1][b+1][a][c]+counts[2][c+1][a][b]
  if (score,count)>(best,size):best,size,center=score,count,(a,b,c)
 return {'weights':weights,'M':M,'penalty':penalty,'maximum':best,'maximizer_size':size,'center':center}

if __name__=='__main__':
 import json
 from pathlib import Path
 out=[];large=[];maxsize=0;bestrow=None
 # Exact bounded diagnostic for integer normalized weights. Not used as a universal theorem.
 for M in range(1,24):
  for b in range(1,M+1):
   for c in range(b,M+1):
    row=maximize((1,b,c),M)
    if row['maximum']>1:
     out.append(row)
     if row['maximizer_size']>maxsize:maxsize=row['maximizer_size'];bestrow=row
     if row['maximizer_size']>=30:large.append(row)
 result={'scope':'fixed finite integer-weight diagnostic, not all rational weights','tested':sum(M*(M+1)//2 for M in range(1,24)),'failures':out,'max_failure_size':maxsize,'largest_failure':bestrow,'large_failures':large}
 Path(__file__).with_name('weighted_dp_integer_diagnostic.json').write_text(json.dumps(result,indent=2)+'\n')
 print({k:v for k,v in result.items() if k!='failures'})
