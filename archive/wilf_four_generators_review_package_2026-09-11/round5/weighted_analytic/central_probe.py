from itertools import product

def maximize(weights,M,coefficient=6,height_coefficient=4,mincentral=1,penalty=0):
 caps=[M//w for w in weights]; horns=[]; counts=[]
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
      v=vol*(coefficient*al*t+coefficient//2*(be*b+ga*c)-height_coefficient*M+penalty)+H[t+1][b][c]
      k=vol+K[t+1][b][c]
      if (v,k)>(val,num):val,num=v,k
     if b and (H[t][b-1][c],K[t][b-1][c])>(val,num):val,num=H[t][b-1][c],K[t][b-1][c]
     if c and (H[t][b][c-1],K[t][b][c-1])>(val,num):val,num=H[t][b][c-1],K[t][b][c-1]
     H[t][b][c]=val;K[t][b][c]=num
  horns.append(H);counts.append(K)
 best=-10**100;size=0;center=None
 for a,b,c in product(*(range(mincentral,cap+1) for cap in caps)):
  height=sum(x*w for x,w in zip((a,b,c),weights))
  if height>M:continue
  vol=(a+1)*(b+1)*(c+1)
  score=vol*(coefficient//2*height-height_coefficient*M+penalty)+horns[0][a+1][b][c]+horns[1][b+1][a][c]+horns[2][c+1][a][b]
  count=vol+counts[0][a+1][b][c]+counts[1][b+1][a][c]+counts[2][c+1][a][b]
  if (score,count)>(best,size):best,size,center=score,count,(a,b,c)
 return {'weights':weights,'M':M,'score_6Sigma_minus_4mM':best,'size':size,'center':center}

if __name__=='__main__':
 import json
 out=[maximize((1,1,1),M) for M in range(3,24)]
 print(json.dumps(out,indent=2))
