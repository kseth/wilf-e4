"""Bounded heuristic probe only; not a universal theorem or coverage proof."""
from fractions import Fraction
import json
from pathlib import Path
import random
import numpy as np

rng = random.Random(2026091110)
attempts = 30000
accepted = 0
best = None
grids = {}
for trial in range(attempts):
    N = rng.choice((7, 8, 10, 12, 16))
    if N not in grids:
        grids[N] = np.indices((N, N, N))
    X, Y, Z = grids[N]
    p = [rng.randint(1, min(5, N-2)) for _ in range(3)]
    if sum(p) < 5:
        continue
    ns = [rng.randint(v+1, N) for v in p]
    profiles = []
    for i, j in ((0, 1), (0, 2), (1, 2)):
        rows = [ns[j]] + sorted(
            [rng.randint(1, ns[j]) for _ in range(ns[i]-1)], reverse=True
        )
        for k in range(p[i]+1):
            rows[k] = max(rows[k], p[j]+1)
        rows += [0]*(N-len(rows))
        corners = [(k, rows[k]) for k in range(1, ns[i])
                   if rows[k] < rows[k-1]]
        opp = 3-i-j
        if len(corners) > sum(p)-2 or sum(
            a >= p[i] and b >= p[j] for a, b in corners
        ) > p[opp]:
            break
        profiles.append(np.array(rows))
    if len(profiles) != 3:
        continue
    T = ((Y < profiles[0][X]) & (Z < profiles[1][X])
         & (Z < profiles[2][Y])
         & ~((X >= p[0]) & (Y >= p[1]) & (Z >= p[2])))
    m = int(T.sum())
    if m < 30:
        continue
    F = []
    E = T.copy()
    for i in range(3):
        successor = np.zeros_like(T)
        dst = [slice(None)]*3
        src = [slice(None)]*3
        dst[i] = slice(0, -1)
        src[i] = slice(1, None)
        successor[tuple(dst)] = T[tuple(src)]
        E &= successor
        F.append(T & ~successor)
    erosion = int(E.sum()) + sum(int(np.take(E, 0, axis=i).sum()) for i in range(3))
    if erosion > m:
        continue
    surfaces = [int((F[i] & F[j]).sum()) for i, j in ((0, 1), (0, 2), (1, 2))]
    if any(q > 2*ns[k] for q, k in zip(surfaces, (2, 1, 0))):
        continue
    accepted += 1
    degree = X+Y+Z
    rho = np.where(T, degree, -1)
    for i in range(3):
        rho = np.flip(np.maximum.accumulate(np.flip(rho, axis=i), axis=i), axis=i)
    gain = sum(int(np.sum(np.where(F[i], (grids[N][i]+1)*(rho-degree), 0)))
               for i in range(3))
    s = [int((v*T).sum()) for v in (X, Y, Z)]
    q = [v-1 for v in ns]
    axis = max(q)*(3*m-4*sum(Fraction(v, r) for v, r in zip(s, q)))
    margin = max(Fraction(gain), axis)-m
    if best is None or margin < Fraction(best["margin"]):
        best = {"trial": trial, "N": N, "corner": p, "axis_lengths": ns,
                "profiles": [v.tolist() for v in profiles], "m": m, "s": s,
                "degree": int(degree[T].max()), "erosion": erosion,
                "surfaces": surfaces, "upgrade": gain, "axis": str(axis),
                "margin": str(margin)}
    if margin < -2:
        break
result = {"scope": "bounded heuristic probe, possible repetitions; not exhaustive",
          "seed": 2026091110, "attempts_completed": trial+1,
          "accepted": accepted, "best": best}
out = Path(__file__).with_name("unbounded_two_witness_probe.json")
out.write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
