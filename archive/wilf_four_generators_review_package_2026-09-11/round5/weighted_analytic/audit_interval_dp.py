"""Independent direct ideal enumeration against the interval horn DP.

This is a finite implementation audit. The analytic domination argument,
and separately checked subdivision coverage, establish parameter-box scope.
Standard library only. Enumerates height arrays rather than horns or boxes.
"""
from pathlib import Path
import importlib.util
import json

path=Path(__file__).resolve().parents[1]/'weight_arrangement'/'interval_certificate.py'
spec=importlib.util.spec_from_file_location('interval_certificate',path)
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)

def brute(lo,hi,scale):
    lw=(scale,lo[0],lo[1]); uw=(scale,hi[0],hi[1])
    hm=hi[2]; lm=lo[2]
    nx=hm//lw[0]+1; ny=hm//lw[1]+1
    h=[[0]*ny for _ in range(nx)]
    count=0; best=None; witness=None
    def rec(k,card,moment):
        nonlocal count,best,witness
        if k==nx*ny:
            if card:
                count+=1
                score=4*moment+(scale-3*lm)*card
                if best is None or score>best:
                    best=score; witness=[row[:] for row in h]
            return
        i,j=divmod(k,ny)
        cap=max(0,(hm-lw[0]*i-lw[1]*j)//lw[2]+1)
        if i: cap=min(cap,h[i-1][j])
        if j: cap=min(cap,h[i][j-1])
        if i and j:
            # A positive height k creates a full-support excluded corner
            # iff both preceding heights are strictly larger than k.
            bound=min(h[i-1][j],h[i][j-1])
            options=[0]+([bound] if 0<bound<=cap else [])
        else:
            options=range(cap+1)
        for z in options:
            h[i][j]=z
            rec(k+1,card+z,moment+z*(uw[0]*i+uw[1]*j)+uw[2]*z*(z-1)//2)
    rec(0,0,0)
    dp=mod.upper_score(lo,hi,scale)
    assert best==dp,(lo,hi,scale,best,dp)
    return {'scale':scale,'lo':lo,'hi':hi,'enumerated_nonempty_no_interior_ideals':count,'maximum_score':best,'agreement':True}

cases=[((1,1,3),(1,1,3),1),((1,1,4),(1,1,4),1),((10,11,30),(12,15,39),10),((2,4,6),(3,5,7),1),((5,7,12),(6,9,15),3),((4,4,9),(6,8,12),3)]
out={'scope':'independent exact finite implementation audit; height-array enumeration, not horn recurrence','cases':[brute(*case) for case in cases]}
Path(__file__).with_name('interval_dp_independent_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
