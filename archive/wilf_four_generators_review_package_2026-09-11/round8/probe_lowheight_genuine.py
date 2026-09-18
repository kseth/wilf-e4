"""Independent deterministic falsification probe on genuine Apery representatives.

This is not an exhaustive semigroup verification or a proof dependency.
It constructs Apéry representatives by value/lexicographic Dijkstra and checks
the arithmetic filters used to reject abstract low-height shapes.
"""
import hashlib
import heapq
import json
import math
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
UNIT = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
ZERO = (0, 0, 0)


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def apery(m, a):
    # Lexicographic tie breaking is invariant under translating exponent tuples.
    d = [None] * m
    d[0] = (0, ZERO)
    heap = [(0, ZERO, 0)]
    while heap:
        w, x, r = heapq.heappop(heap)
        if d[r] != (w, x):
            continue
        for weight, unit in zip(a, UNIT):
            target = (r + weight) % m
            candidate = (w + weight, add(x, unit))
            if d[target] is None or candidate < d[target]:
                d[target] = candidate
                heapq.heappush(heap, (*candidate, target))
    assert all(v is not None for v in d)
    return d


def is_minimal(m, a):
    # Unit membership of a lex-preferred ideal is not a converse test for
    # generator minimality: a reducible generator's unit can win a lex tie.
    reachable = [False] * (a[-1] + 1)
    reachable[0] = True
    for g in (m,) + a:
        if reachable[g]:
            return False
        for value in range(g, a[-1] + 1):
            reachable[value] |= reachable[value - g]
    return True


def check(m, a, d, report):
    T = {v[1] for v in d}
    assert len(T) == m and ZERO in T
    assert is_minimal(m, a)
    assert all(e in T for e in UNIT)
    report['minimal_four_generated'] += 1
    label = lambda x: sum(v * b for v, b in zip(x, a)) % m
    reps = {label(x): x for x in T}
    assert len(reps) == m
    for x in T:
        for j, e in enumerate(UNIT):
            if x[j] > 0:
                assert sub(x, e) in T
    outside = {add(x, e) for x in T for e in UNIT} - T
    corners = {q for q in outside if all(sub(q, e) in T
               for j, e in enumerate(UNIT) if q[j] > 0)}
    for q in corners:
        r = reps[label(q)]
        assert all(qi == 0 or ri == 0 for qi, ri in zip(q, r))
    full = [q for q in corners if min(q) > 0]
    assert len(full) <= 1
    report['full_corner'] += bool(full)
    n = [1 + max(x[j] for x in T) for j in range(3)]
    E = {x for x in T if all(add(x, e) in T for e in UNIT)}
    difference = {sub(x, e) for x in E for e in (ZERO,) + UNIT}
    assert len(difference) == len(E) + sum(sum(x[j] == 0 for x in E) for j in range(3))
    assert len({label(x) for x in difference}) == len(difference) <= m
    F = [{x for x in T if add(x, e) not in T} for e in UNIT]
    for i, j, k in ((0, 1, 2), (0, 2, 1), (1, 2, 0)):
        C = {q for q in outside if q[i] > 0 and q[j] > 0
             and sub(q, UNIT[i]) in T and sub(q, UNIT[j]) in T}
        Q = len(F[i] & F[j])
        assert len(C) == Q - n[k]
        assert len({label(q) for q in C}) == len(C)
        assert all(reps[label(q)][i] == reps[label(q)][j] == 0 for q in C)
        assert Q <= 2 * n[k]
        if full:
            p = full[0]
            planar = {q for q in corners if q[k] == 0 and q[i] > 0 and q[j] > 0}
            upper = {q for q in planar if q[i] >= p[i] and q[j] >= p[j]}
            assert len(planar) <= sum(p) - 2
            assert len(upper) <= p[k]
            for q in upper:
                reduced = list(q)
                reduced[i] -= p[i]
                reduced[j] -= p[j]
                reduced = tuple(reduced)
                assert reduced in T and reduced != ZERO
                gamma = reps[label(q)][k]
                assert gamma > 0 and gamma + p[k] >= n[k]
                assert label(reduced) == ((gamma + p[k]) * a[k]) % m
    if full:
        p = full[0]
        assert reps[label(p)] == ZERO
        maxima = len(F[0] & F[1] & F[2])
        mixed_counts = [sum(q[k] == 0 and q[(k + 1) % 3] > 0
                            and q[(k + 2) % 3] > 0 for q in corners)
                        for k in range(3)]
        assert maxima <= sum(p[k] * (mixed_counts[k] + 1) for k in range(3))
        assert maxima <= sum(p) * (sum(p) - 1)
    M = max(v[0] for v in d)
    D = 3 * m * M - 4 * sum(v[0] for v in d)
    numerator = D - m * (m - 1)
    assert numerator % m == 0
    W = numerator // m
    assert W >= 0
    report['smallest_W'] = min(report['smallest_W'], W)
    if M < 7 * min(a):
        report['height_below_seven'] += 1
        assert all(sum(x) <= 6 for x in T)
        if full:
            assert sum(full[0]) <= 7
        if m >= 30 and full and sum(full[0]) >= 5:
            report['residual_low_height'] += 1
            report['residual_low_height_corners'][str(tuple(sorted(full[0])))] = (
                report['residual_low_height_corners'].get(str(tuple(sorted(full[0]))), 0) + 1)
            assert 10 * D >= (10 * m - 29) * min(a)
            # Literal reconstruction from coordinate-plane shadows and p cut.
            shadows = [{tuple(x[t] for t in range(3) if t != k) for x in T}
                       for k in range(3)]
            reconstructed = set()
            for x in range(7):
                for y in range(7 - x):
                    for z in range(7 - x - y):
                        point = (x, y, z)
                        if all(tuple(point[t] for t in range(3) if t != k) in shadows[k]
                               for k in range(3)) and not all(point[t] >= full[0][t] for t in range(3)):
                            reconstructed.add(point)
            assert reconstructed == T


def main():
    rng = random.Random(11092026)
    report = dict(trials=30000, numerical=0, minimal_four_generated=0,
                  full_corner=0, height_below_seven=0, residual_low_height=0,
                  residual_low_height_corners={}, smallest_W=10**30)
    digest = hashlib.sha256()
    for index in range(report['trials']):
        # Blend small broad examples and higher-multiplicity close generators.
        m = rng.randrange(4, 101)
        cap = 2 * m if index % 2 else 6 * m
        a = tuple(sorted(rng.sample(range(m + 1, cap + 1), 3)))
        if math.gcd(m, *a) != 1:
            continue
        report['numerical'] += 1
        digest.update(f'{m},{a}\n'.encode())
        if is_minimal(m, a):
            check(m, a, apery(m, a), report)
    report.update(status='PASS', scope='Deterministic falsification probe; not an exhaustive proof',
                  sample_sha256=digest.hexdigest(), source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (HERE / 'probe_lowheight_genuine_checks.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
