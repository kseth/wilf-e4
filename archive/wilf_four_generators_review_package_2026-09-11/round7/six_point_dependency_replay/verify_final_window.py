"""Reproducible finite part of the |Z| <= 5 theorem.

Only the Python standard library is required. See the accompanying note for
the analytic reductions that make this finite enumeration an infinite-class
proof. This script does NOT prove Wilf's conjecture for all e=4 semigroups.

Usage: python verify_final_window.py
"""
from collections import Counter
from itertools import combinations, permutations, product
import json
from pathlib import Path
from time import perf_counter

from wilf_work import (canonical, is_antichain, lower_hull, projection_score,
                       projections, inspect)


def compressed_shapes(k):
    # Every coordinate column is a surjection onto {0,...,r}, r<k.
    columns = [a for a in product(range(k), repeat=k)
               if set(a) == set(range(max(a) + 1))]
    first_columns = [a for a in columns if tuple(sorted(a)) == a]
    row_pairs = [(i,j) for i in range(k) for j in range(i)]
    shapes = set()
    for x in first_columns:
        for y in columns:
            # Sort rows by (x,y). An antichain has an injective xy projection.
            if any(x[i] == x[j] and y[i] <= y[j] for i,j in row_pairs):
                continue
            for z in columns:
                # x[i]>=x[j]. Reverse comparability is impossible after the
                # row-order check, so this is the remaining comparable case.
                if any(y[i] >= y[j] and z[i] >= z[j] for i,j in row_pairs):
                    continue
                points = tuple(zip(x,y,z))
                assert is_antichain(points)
                shapes.add(canonical(points))
    return sorted(shapes)


def all_negative_expansions(seeds):
    seen = set(seeds)
    queue = list(sorted(seen))
    for z in queue:
        before = projection_score(z)
        for j in range(3):
            for h in sorted({x[j] for x in z}):
                q = canonical(tuple(tuple(v + (i == j and v >= h)
                                           for i,v in enumerate(x)) for x in z))
                after = projection_score(q)
                assert after > before  # Analytically true for |Z|<=5.
                if after < 0 and q not in seen:
                    seen.add(q)
                    queue.append(q)
    return sorted(seen)


def all_negative_extensions(z):
    start = frozenset(lower_hull(z))
    seen = {start}
    queue = [start]
    for t in queue:
        candidates = {tuple(v+(i==j) for i,v in enumerate(x))
                      for x in t for j in range(3)} - t
        for x in sorted(candidates):
            # Every point of Z must remain maximal in the enlarged lower ideal.
            if any(all(v >= u for v,u in zip(x,p)) for p in z):
                continue
            if any(tuple(v-(i==j) for i,v in enumerate(x)) not in t
                   for j in range(3) if x[j]):
                continue
            q = t | {x}
            if q not in seen and projection_score(z,q) < 0:
                seen.add(q)
                queue.append(q)
    return sorted(seen, key=lambda t: (len(t), sorted(t)))


def residue_labels(t):
    m = len(t)
    points = sorted(t)
    for a in permutations(range(1,m), 3):
        seen = set()
        for x in points:
            r = sum(v*b for v,b in zip(x,a)) % m
            if r in seen:
                break
            seen.add(r)
        else:
            yield a


def boundary_slacks(t, a):
    m = len(t)
    weighted_tops = []
    for j in range(3):
        lines = {}
        for x in t:
            key = tuple(x[i] for i in range(3) if i != j)
            lines.setdefault(key,[]).append(x)
        for line in lines.values():
            top = max(line, key=lambda x:x[j])
            weighted_tops.append((len(line), sum(v*b for v,b in zip(top,a)) % m))
    return [sum(L*((f-r)%m) for L,r in weighted_tops)-m*(m-1)
            for f in range(m)]


def verify():
    start = perf_counter()
    records = []
    expected = {1:(1,0), 2:(2,0), 3:(18,0), 4:(287,1), 5:(8340,58)}
    for k in range(1,6):
        shapes = compressed_shapes(k)
        hist = Counter(projection_score(z) for z in shapes)
        seeds = [z for z in shapes if projection_score(z) < 0]
        assert (len(shapes),len(seeds)) == expected[k]
        expanded = all_negative_expansions(seeds)
        pairs = [(z,t) for z in expanded for t in all_negative_extensions(z)]
        survivors = []
        for z,t in pairs:
            # A genuine four-generated Apéry staircase contains all three axes.
            if not all(tuple(int(i==j) for i in range(3)) in t for j in range(3)):
                continue
            labels = list(residue_labels(t))
            if labels:
                checks = [(a,boundary_slacks(t,a)) for a in labels]
                assert all(min(slacks) >= 0 for _,slacks in checks)
                survivors.append(dict(Z=z,T=sorted(t),m=len(t),
                    F=projection_score(z,t), labels=labels,
                    min_boundary_slack=min(min(s) for _,s in checks),
                    boundary_slacks=[dict(A=a,slacks=s) for a,s in checks]))
        record=dict(k=k, compressed_count=len(shapes),
            compressed_score_histogram=dict(sorted(hist.items())),
            negative_compressed=len(seeds),negative_expanded=len(expanded),
            negative_pairs=len(pairs),
            largest_negative_ideal=max((len(t) for _,t in pairs),default=0),
            residue_bijective_pairs=len(survivors),
            residue_label_count=sum(len(s['labels']) for s in survivors),
            cut_count=sum(s['m']*len(s['labels']) for s in survivors),
            survivors=survivors)
        records.append(record)
        print(json.dumps({a:b for a,b in record.items()
                          if a not in ('survivors','compressed_score_histogram')}),flush=True)
    assert records[3]['negative_expanded']==2
    assert records[3]['negative_pairs']==2
    assert records[4]['negative_expanded']==131
    assert records[4]['negative_pairs']==198
    assert records[4]['residue_bijective_pairs']==3
    assert records[4]['residue_label_count']==40
    # Directly cross-check the geometric identities against exact Apéry data.
    fixed=[(7,8,9,11),(10,11,13,16),(10,14,17,19),(30,63,85,86),
           (8,9,10,13),(100,101,103,107),(25,26,30,31)]
    examples=[inspect(gens) for gens in fixed]
    result=dict(status='PASS: Wilf verified for every e=4 semigroup with |Z|<=5',
                scope='Computer-assisted partial theorem, not full Wilf conjecture',
                enumeration=records,examples=examples,
                elapsed_seconds=perf_counter()-start)
    Path('verification-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(result['status'],flush=True)
    return result


if __name__ == '__main__':
    verify()
