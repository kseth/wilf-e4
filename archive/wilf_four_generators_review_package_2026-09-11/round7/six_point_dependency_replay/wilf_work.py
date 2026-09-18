"""Exact arithmetic research utilities for Wilf's conjecture, 2026-09-05.

Finite searches are diagnostics, not a proof of Wilf's conjecture.
"""
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from math import gcd
from functools import reduce


def apery(gens):
    m, *a = sorted(gens)
    if len(a) != 3 or reduce(gcd, gens) != 1:
        return None
    best = [None] * m
    best[0] = (0, (0, 0, 0))
    heap = [(0, (0, 0, 0), 0)]
    while heap:
        w, x, r = heappop(heap)
        if best[r] != (w, x):
            continue
        for j, aj in enumerate(a):
            y = tuple(v + (i == j) for i, v in enumerate(x))
            s = (r + aj) % m
            cand = (w + aj, y)
            if best[s] is None or cand < best[s]:
                best[s] = cand
                heappush(heap, (*cand, s))
    weights = [v[0] for v in best]
    def contains(v):
        return v >= 0 and weights[v % m] <= v
    if any(contains(g - h) for g in a for h in [m, *a] if h < g):
        return None
    return m, a, best


def lower_hull(z):
    return {x for t in z for x in product(*(range(v + 1) for v in t))}


def projections(t):
    return [{tuple(x[j] for j in range(3) if j != i) for x in t}
            for i in range(3)]


def repeated(z):
    return sum(map(sum, z)) - sum(max(x[j] for x in z) for j in range(3))


def projection_score(z, t=None):
    if t is None:
        t = lower_hull(z)
    return sum(map(len, projections(t))) - 3 * len(z) - repeated(z)


def canonical(z):
    return min(tuple(sorted(tuple(x[j] for j in p) for x in z))
               for p in permutations(range(3)))


def is_antichain(z):
    return all(any(a < b for a, b in zip(p, q)) and
               any(a > b for a, b in zip(p, q)) for p, q in combinations(z, 2))


def is_compressed(z):
    return all(set(x[j] for x in z) == set(range(1 + max(x[j] for x in z)))
               for j in range(3))


def inspect(gens, verify=True):
    result = apery(gens)
    if result is None:
        return None
    m, a, best = result
    t = {x for _, x in best}
    w = {x: v for v, x in best}
    M = max(w.values())
    g = sum(v // m for v in w.values())
    c = M - m + 1
    n = c - g
    W = 4 * n - c
    z = {x for x in t if M - w[x] < m}
    E = repeated(z)
    D = sum(map(len, projections(t))) - 3 * len(z)
    data = dict(gens=[m, *a], m=m, c=c, g=g, n=n, W=W,
                Z=sorted(z), k=len(z), E=E, D=D, F=D-E)
    if not verify:
        return data
    assert len(t) == m
    assert all(tuple(v - (i == j) for i, v in enumerate(x)) in t
               for x in t for j in range(3) if x[j])
    assert all(tuple(v + (i == j) for i, v in enumerate(x)) not in t
               for x in z for j in range(3))
    line_total = deep_total = Gamma = boundary = 0
    for j in range(3):
        lines = {}
        for x in t:
            key = tuple(x[i] for i in range(3) if i != j)
            lines.setdefault(key, []).append(x)
        for line in lines.values():
            L = len(line)
            top = max(line, key=lambda x: x[j])
            h, beta = divmod(M - w[top], m)
            residues = [(k * a[j]) % m for k in range(L)]
            C = sum(r + beta >= m for r in residues)
            score = m * L * h + m * C - sum(residues)
            boundary += L * (M - w[top])
            line_total += score
            Gamma += L * h + C
            if h:
                assert score >= m + L * (L - 1) // 2
                deep_total += score
    Lambda = sum(sum((a[j] * x[j]) % m for j in range(3)) // m for x in t)
    used = set()
    delta = 0
    for j in range(3):
        for k in range(1, 1 + max(x[j] for x in z)):
            r = (k * a[j]) % m
            assert r and r not in used
            used.add(r)
            copies = sum(x[j] >= k for x in z)
            crossings = sum(x[j] >= k and M - w[x] + r >= m for x in z)
            delta += (copies - 1) * r - m * crossings
    Boff = sum(set(range(1, m)) - used)
    assert boundary == 3*m*M - 4*sum(w.values()) == m*W + m*(m-1)
    assert m*W == m*(m-1)//2 + line_total == Boff + deep_total - delta
    assert W == Gamma - Lambda
    assert n == sum((M - v)//m for v in w.values())
    data.update(Boff=Boff, deep_total=deep_total, delta=delta,
                Gamma=Gamma, Lambda=Lambda, T=sorted(t), apery=sorted(w.values()))
    return data


if __name__ == '__main__':
    import argparse, json, random
    parser = argparse.ArgumentParser()
    parser.add_argument('--random', type=int, default=0)
    args = parser.parse_args()
    fixed = [(7,8,9,11),(10,11,13,16),(10,14,17,19),(30,63,85,86),
             (8,9,10,13),(100,101,103,107)]
    for gens in fixed:
        r=inspect(gens)
        print(json.dumps({k:v for k,v in r.items() if k not in ('T','apery')}))
    rng = random.Random(20260905)
    tested = 0
    worst = None
    hist = {}
    for _ in range(args.random):
        m = rng.randint(20, 600)
        a = sorted(rng.sample(range(m+1, 10*m), 3))
        r = inspect([m,*a])
        if r is None:
            continue
        tested += 1
        assert r['W'] >= 0
        hist[r['k']] = hist.get(r['k'],0)+1
        if worst is None or r['F'] < worst['F']:
            worst = r
    if args.random:
        print(json.dumps(dict(attempts=args.random,tested=tested,hist=hist,
             worst={k:v for k,v in worst.items() if k not in ('T','apery')})))
