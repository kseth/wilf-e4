"""Independent exhaustive structural audit. No graph/tree or prior DP imported."""
from itertools import combinations_with_replacement, product
from pathlib import Path
import hashlib
import json
import time


def main():
    started = time.time()
    n = 4
    points = tuple(product(range(n), repeat=3))
    profiles = [tuple(reversed(p)) for p in combinations_with_replacement(range(n+1), n)]
    ideals = set()
    for xy, xz, yz in product(profiles, repeat=3):
        mask = 0
        for j, (x, y, z) in enumerate(points):
            if y < xy[x] and z < xz[x] and z < yz[y]:
                mask |= 1 << j
        ideals.add(mask)

    corner_scores = {(1,1,1): None, (1,1,2): None}
    corner_counts = {p: 0 for p in corner_scores}
    tested = 0
    max_size = max_maxima = 0
    fewest_centers = n**3
    for mask in sorted(ideals):
        T = tuple(x for j, x in enumerate(points) if (mask >> j) & 1)
        if not T:
            continue
        Ts = set(T)
        # Verify the generating characterization independently: no omitted
        # full-support point has all three immediate predecessors in T.
        for p in product(range(1,n+1), repeat=3):
            assert p in Ts or not all(tuple(p[k]-(k==i) for k in range(3)) in Ts for i in range(3))
        sections = []
        for i in range(3):
            jk = [j for j in range(3) if j != i]
            axis_sections = []
            for t in range(n):
                pairs = [(x[jk[0]],x[jk[1]]) for x in T if x[i] == t]
                if not pairs:
                    axis_sections.append(None)
                else:
                    caps = (max(x[0] for x in pairs),max(x[1] for x in pairs))
                    rectangular = len(pairs) == (caps[0]+1)*(caps[1]+1)
                    axis_sections.append((caps,rectangular))
            sections.append(axis_sections)
        centers = []
        for c in T:
            valid = True
            for i in range(3):
                jk = [j for j in range(3) if j != i]
                previous = (c[jk[0]],c[jk[1]])
                for t in range(c[i]+1,n):
                    section = sections[i][t]
                    if section is None:
                        continue
                    caps, rectangular = section
                    if not rectangular or any(caps[k]>previous[k] for k in range(2)):
                        valid = False
                        break
                    previous = caps
                if not valid:
                    break
            if valid:
                # Literal disjoint reassembly verifies every point, rather
                # than trusting just the caps/rectangle characterization.
                pieces = [{x for x in points if all(x[i]<=c[i] for i in range(3))}]
                for i in range(3):
                    pieces.append({x for x in T if x[i]>c[i]})
                assert set.union(*pieces) == Ts
                assert sum(len(piece) for piece in pieces) == len(T)
                centers.append(c)
        assert centers, {"no_central_horn_representation":T}
        tested += 1
        fewest_centers = min(fewest_centers,len(centers))
        max_size = max(max_size,len(T))
        maxima = [x for x in T if all(tuple(x[k]+(k==i) for k in range(3)) not in Ts for i in range(3))]
        max_maxima = max(max_maxima,len(maxima))

        # A tiny independent exhaustive benchmark of the clipped-horn DP.
        # Both sorted possible positive corners for height allowance R=3.
        for p in corner_scores:
            clipped = [x for x in T if any(x[i]<p[i] for i in range(3))]
            if any(sum(x)>3 for x in clipped):
                continue
            score = sum(4*sum(x)-5 for x in clipped)
            old = corner_scores[p]
            corner_scores[p] = score if old is None else max(old,score)
            corner_counts[p] += 1

    # Direct finite recursion with literal point scores; no prefix recurrence.
    from functools import lru_cache
    dp_scores = {}
    for p in corner_scores:
        def kept(x):
            return any(x[i]<p[i] for i in range(3))
        @lru_cache(None)
        def horn(axis,t,b,c):
            if t>=n:
                return 0
            best = 0
            jk = [i for i in range(3) if i!=axis]
            for r in range(b+1):
                for s in range(c+1):
                    section = []
                    for u,v in product(range(r+1),range(s+1)):
                        x=[0,0,0]; x[axis]=t; x[jk[0]]=u; x[jk[1]]=v
                        if kept(x): section.append(tuple(x))
                    if any(sum(x)>3 for x in section): continue
                    best=max(best,sum(4*sum(x)-5 for x in section)+horn(axis,t+1,r,s))
            return best
        best = -10**9
        for c in points:
            center = [x for x in points if all(x[i]<=c[i] for i in range(3)) and kept(x)]
            if any(sum(x)>3 for x in center): continue
            score = sum(4*sum(x)-5 for x in center)
            for i in range(3):
                jk=[j for j in range(3) if j!=i]
                score += horn(i,c[i]+1,c[jk[0]],c[jk[1]])
            best=max(best,score)
        dp_scores[p]=best
        assert best==corner_scores[p], (p,best,corner_scores[p])
    result={
        "status":"PASS", "scope":"all no-interior ideals contained in {0,1,2,3}^3",
        "plane_profiles":len(profiles), "plane_triples":len(profiles)**3,
        "distinct_nonempty_ideals":tested, "largest_ideal":max_size,
        "largest_maximal_antichain":max_maxima,
        "minimum_number_of_valid_centers":fewest_centers,
        "clipped_dp_checks":[{"corner":p,"height":3,"score":dp_scores[p],"exhaustive_feasible_closures":corner_counts[p]} for p in corner_scores],
        "proof_limitation":"Finite enumeration supports but does not replace the universal structural proof.",
        "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "seconds":round(time.time()-started,3)
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
