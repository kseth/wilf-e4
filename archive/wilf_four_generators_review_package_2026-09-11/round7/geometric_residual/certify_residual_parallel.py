"""Conditional exact closed-box certificate attempt; inspect complete flag."""
from pathlib import Path
from fractions import Fraction
import subprocess,json,time,argparse
ROOT=Path(__file__).resolve().parent

def ceildiv(a,b):return -(-a//b)
def clip(lo,hi,q):
 lo=list(lo);hi=list(hi)
 for _ in range(20):
  old=(tuple(lo),tuple(hi));b0,c0,h0=lo;b1,c1,h1=hi
  lo=[b0,max(b0,c0),max(b0,c0,h0)];hi=[min(b1,c1,h1),min(c1,h1),h1]
  if any(a>b for a,b in zip(lo,hi)):break
  Sbound=9*q+ceildiv(28*q*q,lo[2]-3*q)
  hi[0]=min(hi[0],ceildiv(Sbound-q,2))
  hi[1]=min(hi[1],Sbound-q-lo[0])
  Supper=min(q+hi[0]+hi[1],Sbound)
  hi[2]=min(hi[2],ceildiv(42*q+37*Supper,5))
  if old==(tuple(lo),tuple(hi)):break
 return tuple(lo),tuple(hi)

def run(limit=200000,q=4096,hmin=7,resume=None):
 initial=((q,q,hmin*q),(78*q,78*q,78*q));tree=[None];stack=[(initial,0)];unresolved=[];count=0;start=time.time();dps=0;cases=0
 if resume:
  saved=json.loads(Path(resume).read_text());assert saved['scale']==q
  initial=saved['initial'];tree=saved['tree'];stack=saved['stack'];unresolved=saved['unresolved'];count=saved['count']
 worker=subprocess.Popen([str(ROOT/'interval_all_corners_parallel')],stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True,bufsize=1)
 while stack and count<limit:
  if count and count%1000==0:
   (ROOT/'residual_parallel_checkpoint.json').write_text(json.dumps({'tree':tree,'stack':stack,'unresolved':unresolved,'count':count,'scale':q,'initial':initial}))
   print({'nodes':count,'stack':len(stack),'unresolved':len(unresolved),'seconds':time.time()-start,'dp_calls':dps,'corner_cases':cases},flush=True)
  box,idx=stack.pop();count+=1;lo,hi=clip(*box,q)
  if any(x>y for x,y in zip(lo,hi)):
   tree[idx]={'box':box,'kind':'empty'};continue
  widths=[hi[i]-lo[i] for i in range(3)]
  # Refinement heuristic only; no boxes accepted on its basis.
  broad=(hi[2]-lo[2]>4*q or hi[0]>2*lo[0] or hi[1]>2*lo[1])
  bounds=None
  if not broad:
   worker.stdin.write(' '.join(map(str,(q,*lo,*hi)))+'\n');worker.stdin.flush()
   bounds=list(map(int,worker.stdout.readline().split()));dps+=1;cases+=bounds[4]
   if bounds[5] and 10*bounds[0]<=29*q:
    tree[idx]={'box':box,'kind':'dp','bounds':bounds};continue
  axes=[i for i in (0,1,2) if widths[i]>1]
  if not axes:
   unresolved.append({'box':box,'clipped':(lo,hi),'bounds':bounds});tree[idx]={'box':box,'kind':'unresolved','bounds':bounds};continue
  axis=max(axes,key=lambda i:Fraction(widths[i]*(3 if i==2 else 4)*hi[2],lo[i] if i<2 else hi[2]))
  mid=(lo[axis]+hi[axis])//2;hi1=list(hi);hi1[axis]=mid;lo2=list(lo);lo2[axis]=mid
  children=(len(tree),len(tree)+1);tree.extend((None,None));tree[idx]={'box':box,'kind':'split','axis':axis,'mid':mid,'children':children}
  stack.append(((tuple(lo2),hi),children[1]));stack.append(((lo,tuple(hi1)),children[0]))
  if count%100==0:
   print({'nodes':count,'stack':len(stack),'unresolved':len(unresolved),'seconds':time.time()-start,'dp_calls':dps,'corner_cases':cases,'box':(lo,hi)},flush=True)
  if count%10000==0:
   (ROOT/'residual_parallel_checkpoint.json').write_text(json.dumps({'tree':tree,'stack':stack,'unresolved':unresolved,'count':count,'scale':q,'initial':initial}))
 worker.stdin.close();worker.wait()
 result={'scope':'conditional attempted certificate generic p coordinate sum>=5, 7<=M<=78, positive weights normalized min1, score m-D<=29/10; relies on general phase and continuous gap5/42 for clipping','scale':q,'initial':initial,'complete':not unresolved and not stack,'tree':tree,'nodes':count,'unresolved':unresolved,'stack':stack,'seconds':time.time()-start,'dp_calls':dps,'corner_cases':cases}
 (ROOT/'residual_parallel_interval_certificate.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
 print({k:v for k,v in result.items() if k not in ('tree','unresolved','stack')}|{'unresolved_count':len(unresolved),'pending_count':len(stack)},flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--limit',type=int,default=200000);p.add_argument('--hmin',type=int,default=7);p.add_argument('--resume');a=p.parse_args();run(a.limit,hmin=a.hmin,resume=a.resume)
