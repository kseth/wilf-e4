"""Additional independent checks of the unit-weight one-corner theorem.

Does not rerun the full already independently reproduced C++ finite strips.
Checks interval coverage, every low-height recorded corner, direct clipped
box/slice moments, and exact residue-decimation identities on explicit ideals.
"""
from itertools import product
from pathlib import Path
from collections import defaultdict
import json

base = Path('round5/weighted_analytic/one_corner')
strips = {}
for penalty, filename, first, last in [(1, 'unit_target_strip.jsonl', 3, 16),
                                     (3, 'unit_decimation_strip.jsonl', 14, 34)]:
    rows = [json.loads(line) for line in (base / filename).read_text().splitlines()]
    assert [row['R'] for row in rows] == list(range(first, last + 1))
    for row in rows:
        R = row['R']
        expected_corners = [(a,b,c) for a in range(1,R)
                            for b in range(a,R) for c in range(b,R)
                            if a+b+c <= R+1]
        assert row['corner_cases'] == len(expected_corners)
        assert row['penalty'] == penalty
        if penalty == 3 or R >= 7:
            assert row['maximum'] <= 0
    strips[penalty] = rows

low = json.loads((base/'unit_one_corner_results.json').read_text())
row = next(row for row in low if row['R'] == 6)
corners = row['all_corner_results']
assert {tuple(r['corner']) for r in corners} == {
    (a,b,c) for a in range(1,7) for b in range(a,7) for c in range(b,7)
    if a+b+c <= 7}
assert max(r['maximum'] for r in corners if r['corner'] != [1,1,1]) == -1

# Directly verify the closed clipped-box formulas used by the C++ program.
moment_checks = 0
for p in product(range(1,4), repeat=3):
    for top in product(range(4), repeat=3):
        points = [x for x in product(*(range(t+1) for t in top))
                  if not all(xi>=pi for xi,pi in zip(x,p))]
        size = (top[0]+1)*(top[1]+1)*(top[2]+1)
        twice_sum = size*sum(top)
        height = sum(top)
        if all(t>=q for t,q in zip(top,p)):
            removed = (top[0]-p[0]+1)*(top[1]-p[1]+1)*(top[2]-p[2]+1)
            size -= removed
            twice_sum -= removed*(sum(top)+sum(p))
            height = max(sum(top)-top[i]+p[i]-1 for i in range(3))
        assert (size, twice_sum, height) == (len(points), 2*sum(map(sum,points)), max(map(sum,points)))
        moment_checks += 1

def full_corners(T):
    candidates = {tuple(xj+(i==j) for j,xj in enumerate(x))
                  for x in T for i in range(3)} - T
    return [p for p in candidates if all(p) and all(
        tuple(pj-(i==j) for j,pj in enumerate(p)) in T for i in range(3))]

fixtures = []
for R in (17, 18, 33, 34, 50, 79):
    # Three triangular faces: one full corner, arbitrary degree radius.
    T = {(x,y,z) for x in range(R+1) for y in range(R+1-x)
         for z in range(R+1-x-y) if min(x,y,z)==0}
    L = R//17
    classes = defaultdict(set)
    for x in T:
        classes[tuple(v%L for v in x)].add(tuple(v//L for v in x))
    original = 3*len(T)*R-4*sum(map(sum,T))
    reconstructed = 0
    for r, Tr in classes.items():
        allowance, remainder = divmod(R-sum(r),L)
        assert 14 <= allowance <= 33
        assert len(full_corners(Tr)) <= 1
        D = 3*len(Tr)*allowance-4*sum(map(sum,Tr))
        assert D >= 3*len(Tr)
        reconstructed += L*D+(3*remainder-sum(r))*len(Tr)
    assert reconstructed == original
    fixtures.append({'R':R,'L':L,'m':len(T),'classes':len(classes),'D':original})

F6 = {(x,y,z) for x in range(7) for y in range(7-x)
      for z in range(7-x-y) if min(x,y,z)==0}
assert (len(F6),sum(map(sum,F6)),3*len(F6)*6-4*sum(map(sum,F6))) == (64,273,60)
result = {'status':'PASS','scope':'independent formulas, low-height and decimation checks; full strips audited separately',
          'clipped_box_moment_checks':moment_checks,'decimation_fixtures':fixtures,
          'low_height_non111_maximum':-1,'sharp_threshold':65}
Path('round5/structural_audit/unit_one_corner_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
