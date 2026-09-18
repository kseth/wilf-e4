"""Whole-real-parameter certificate attempt for corner permutations of 211."""
from interval_corner_bound import corner_bound
from fractions import Fraction
from pathlib import Path
import json,time


def clip(lower,upper):
    b0,c0,h0=lower; b1,c1,h1=upper
    return (b0,max(b0,c0),max(b0,c0,h0)),(min(b1,c1,h1),min(c1,h1),h1)


def certify(q=4096,limit=100000,worker=None):
    initial=((q,q,6*q),(42*q,42*q,42*q))
    tree=[None]; stack=[(initial,0)]; unresolved=[]; count=0; start=time.time()
    while stack:
        box,idx=stack.pop(); count+=1
        if count>limit:
            unresolved=[box]+[x[0] for x in stack];break
        lo,hi=clip(*box)
        if any(x>y for x,y in zip(lo,hi)):
            tree[idx]={'box':box,'kind':'empty'};continue
        if lo[2]>=3*q+4*(q+hi[0]+hi[1]):
            tree[idx]={'box':box,'kind':'planar'};continue
        bounds=[]
        if worker:
            worker.stdin.write(' '.join(map(str,(q,*lo,*hi)))+'\n');worker.stdin.flush()
            bounds=list(map(int,worker.stdout.readline().split()))
            assert bounds
        else:
            for p in ((2,1,1),(1,2,1),(1,1,2)):
                bounds.append(corner_bound(lo,hi,q,p))
                if bounds[-1]>q:break
        if len(bounds)==3 and max(bounds)<=q:
            tree[idx]={'box':box,'kind':'dp','bounds':bounds};continue
        widths=[hi[i]-lo[i] for i in range(3)]
        axes=[i for i in (0,1,2) if widths[i]>1]
        if not axes:
            unresolved.append(box);tree[idx]={'box':box,'kind':'unresolved','bounds':bounds};continue
        axis=max(axes,key=lambda i:Fraction(widths[i]*(3 if i==2 else 4)*hi[2],lo[i] if i<2 else hi[2]))
        mid=(lo[axis]+hi[axis])//2
        hi1=list(hi);hi1[axis]=mid
        lo2=list(lo);lo2[axis]=mid
        children=(len(tree),len(tree)+1);tree.extend((None,None))
        tree[idx]={'box':box,'kind':'split','axis':axis,'mid':mid,'children':children}
        stack.append(((tuple(lo2),hi),children[1]));stack.append(((lo,tuple(hi1)),children[0]))
        if count%5000==0:print({'nodes':count,'stack':len(stack),'unresolved':len(unresolved),'seconds':time.time()-start},flush=True)
    return {'scope':'all real 1<=b<=c<=M with 6<=M<=42, full corner a permutation of 211, score m-D<=1','scale':q,'initial':initial,'complete':not unresolved,'tree':tree,'nodes':count,'unresolved':unresolved,'seconds':time.time()-start}


if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--limit',type=int,default=100000);p.add_argument('--worker')
    args=p.parse_args();worker=None
    if args.worker:
        import subprocess
        worker=subprocess.Popen([args.worker],stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True,bufsize=1)
    result=certify(limit=args.limit,worker=worker)
    if worker:worker.stdin.close();worker.wait()
    Path(__file__).with_name('short_corner_complete_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print({k:v for k,v in result.items() if k not in ('tree','unresolved')}|{'unresolved_count':len(result['unresolved'])})
