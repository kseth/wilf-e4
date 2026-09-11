"""Exact integer DP retaining cardinality, capped at a requested threshold."""
import numpy as np
from itertools import product
NEG=-(10**15)

def maximize_min_size(weights,M,penalty=1,min_size=30):
 if not (len(weights)==3 and all(isinstance(w,int) and w>0 for w in weights) and isinstance(M,int) and M>=0 and isinstance(penalty,int) and isinstance(min_size,int) and min_size>=1):
  raise ValueError("Expected three positive integer weights, nonnegative integer M, integer penalty, and positive integer cardinality threshold.")
 caps=[M//w for w in weights]
 box_count=(caps[0]+1)*(caps[1]+1)*(caps[2]+1)
 if box_count*(7*M+abs(penalty)+1)>=10**12:
  raise ValueError("Problem exceeds the validated int64/sentinel arithmetic range.")
 L=min_size;ix=np.arange(L+1)
 horns=[]
 for axis in range(3):
  js=[j for j in range(3) if j!=axis];al=weights[axis];be,ga=[weights[j] for j in js]
  n=caps[axis]+1;nb,nc=[caps[j]+1 for j in js]
  H=np.full((n+1,nb,nc,L+1),NEG,dtype=np.int64);H[:,:,:,0]=0
  for t in range(n-1,-1,-1):
   for b in range(nb):
    for c in range(nc):
     cur=H[t,b,c]
     if al*t+be*b+ga*c<=M:
      vol=(b+1)*(c+1)
      reward=vol*(4*al*t+2*be*b+2*ga*c-3*M+penalty)
      tail=H[t+1,b,c]
      if vol>=L:
       cur[L]=max(cur[L],int(np.max(tail))+reward)
      else:
       cur[vol:L]=np.maximum(cur[vol:L],tail[:L-vol]+reward)
       cur[L]=max(cur[L],int(np.max(tail[L-vol:]))+reward)
     if b:np.maximum(cur,H[t,b-1,c],out=cur)
     if c:np.maximum(cur,H[t,b,c-1],out=cur)
  horns.append(H)
 best=NEG;center=None
 for a,b,c in product(*(range(cap+1) for cap in caps)):
  height=sum(x*w for x,w in zip((a,b,c),weights))
  if height>M:continue
  vol=(a+1)*(b+1)*(c+1)
  reward=vol*(2*height-3*M+penalty)
  h0=horns[0][a+1,b,c];h1=horns[1][b+1,a,c];h2=horns[2][c+1,a,b]
  target=np.maximum(0,L-vol-ix[:,None]-ix[None,:])
  h2suffix=np.maximum.accumulate(h2[::-1])[::-1]
  value=reward+int(np.max(h0[:,None]+h1[None,:]+h2suffix[target]))
  if value>best:best=value;center=(a,b,c)
 return {'weights':weights,'M':M,'penalty':penalty,'min_size':min_size,'maximum':best,'center':center,'feasible':best>NEG//2}

if __name__=='__main__':
 from weighted_dp import maximize
 for w,M in [((1,1,1),4),((1,1,1),5),((10,11,12),60),((2,3,4),14)]:
  print(maximize_min_size(w,M,penalty=min(w)))
