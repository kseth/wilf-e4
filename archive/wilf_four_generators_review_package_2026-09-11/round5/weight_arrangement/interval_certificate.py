"""Rigorous interval certificate for weighted no-interior horn inequalities.

The bounds range over every real parameter in a box, not merely its corners.
No floating-point arithmetic is used in the certificate calculation.
"""
from itertools import product
from fractions import Fraction
import json
from pathlib import Path
import time


def upper_score(lo, hi, scale=1):
    """Upper bound on m-D for weights (1,b,c), height M in this box.

    lo/hi contain b,c,M, all in common integer scale. Admissibility uses
    the lower weights and upper height; objective uses the upper weights
    and lower height. Therefore one exact horn DP dominates every ideal
    at every parameter in the box.
    """
    lw=(scale,lo[0],lo[1]); uw=(scale,hi[0],hi[1])
    lm=lo[2]; hm=hi[2]
    caps=[hm//w for w in lw]
    horns=[]
    for axis in range(3):
        js=[j for j in range(3) if j!=axis]
        n=caps[axis]+1; nb,nc=[caps[j]+1 for j in js]
        H=[[[0]*nc for _ in range(nb)] for _ in range(n+1)]
        for t in range(n-1,-1,-1):
            for b in range(nb):
                for c in range(nc):
                    val=0
                    if lw[axis]*t+lw[js[0]]*b+lw[js[1]]*c<=hm:
                        vol=(b+1)*(c+1)
                        val=max(val,vol*(4*uw[axis]*t+2*uw[js[0]]*b+2*uw[js[1]]*c-3*lm+scale)+H[t+1][b][c])
                    if b: val=max(val,H[t][b-1][c])
                    if c: val=max(val,H[t][b][c-1])
                    H[t][b][c]=val
        horns.append(H)
    best=None
    for a,b,c in product(*(range(cap+1) for cap in caps)):
        if a*lw[0]+b*lw[1]+c*lw[2]>hm: continue
        vol=(a+1)*(b+1)*(c+1)
        val=vol*(2*(a*uw[0]+b*uw[1]+c*uw[2])-3*lm+scale)+horns[0][a+1][b][c]+horns[1][b+1][a][c]+horns[2][c+1][a][b]
        if best is None or val>best: best=val
    return best


def tightened(lo,hi):
    # Domain is b <= c <= M. Tightening does not remove feasible points.
    lo=list(lo); hi=list(hi)
    lo[1]=max(lo[1],lo[0]); lo[2]=max(lo[2],lo[1])
    hi[1]=min(hi[1],hi[2]); hi[0]=min(hi[0],hi[1])
    if any(l>h for l,h in zip(lo,hi)): return None
    return tuple(lo),tuple(hi)


def certify(scale=4096, max_nodes=None, max_weight=24, progress=10000):
    initial=((scale,scale,5*scale),(max_weight*scale,max_weight*scale,24*scale))
    stack=[(initial,0)]; leaves=[]; unresolved=[]; nodes=0; start=time.time()
    tree=[None]
    while stack:
        raw,node_id=stack.pop(); nodes+=1
        if max_nodes and nodes>max_nodes:
            unresolved.extend([raw]+[x[0] for x in stack]); break
        box=tightened(*raw)
        if box is None:
            rec={'box':raw,'kind':'empty'}
            leaves.append(rec); tree[node_id]=rec; continue
        lo,hi=box
        if lo[2]>=2*(scale+hi[0]+hi[1])+3*scale:
            rec={'box':raw,'kind':'continuous'}
            leaves.append(rec); tree[node_id]=rec; continue
        bound=upper_score(lo,hi,scale)
        if bound<=scale:
            rec={'box':raw,'kind':'dp','bound':bound}
            leaves.append(rec); tree[node_id]=rec; continue
        # Use proportional interval widths; M score has coefficient 3m.
        widths=[hi[i]-lo[i] for i in range(3)]
        available=[i for i in range(3) if widths[i]>1]
        if not available:
            unresolved.append(raw); continue
        axis=max(available,key=lambda i: Fraction(widths[i]*(3 if i==2 else 4)*hi[2],lo[i] if i<2 else hi[2]))
        mid=(lo[axis]+hi[axis])//2
        h1=list(hi); h1[axis]=mid
        l2=list(lo); l2[axis]=mid
        ids=(len(tree),len(tree)+1); tree.extend((None,None))
        tree[node_id]={'box':raw,'kind':'split','axis':axis,'mid':mid,'children':ids}
        stack.append(((tuple(l2),hi),ids[1])); stack.append(((lo,tuple(h1)),ids[0]))
        if progress and nodes%progress==0:
            print(json.dumps({'nodes':nodes,'leaves':len(leaves),'stack':len(stack),'unresolved':len(unresolved),'elapsed':time.time()-start}),flush=True)
    return {'claim':'m-D<=1 for every nonempty no-interior ideal in each certified parameter box','scale':scale,'initial':initial,'nodes':nodes,'seconds':time.time()-start,'complete':not unresolved,'leaf_count':len(leaves),'tree':tree,'unresolved':unresolved}


if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser(); p.add_argument('--max-nodes',type=int); p.add_argument('--scale',type=int,default=4096); p.add_argument('--max-weight',type=int,default=24); p.add_argument('--output',default='interval_certificate_results.json')
    args=p.parse_args()
    result=certify(scale=args.scale,max_nodes=args.max_nodes,max_weight=args.max_weight)
    Path(__file__).with_name(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('tree','unresolved')}|{'unresolved_count':len(result['unresolved'])}))
