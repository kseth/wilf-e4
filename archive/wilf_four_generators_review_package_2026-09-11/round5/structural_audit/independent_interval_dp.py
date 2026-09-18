"""Independent exact DP audit: explicit rectangle transitions, no prefix maxima.

The source interval implementation is deliberately not imported.  This audits
the numerical leaf bounds; tree coverage has a separate checker.
"""
from itertools import product
from functools import lru_cache
from pathlib import Path
import argparse
import json
import time


def tighten(lo, hi):
    # Independent fixed-point propagation of coordinate ordering.
    lo, hi = list(lo), list(hi)
    while True:
        old = (tuple(lo), tuple(hi))
        for i in range(2):
            lo[i + 1] = max(lo[i + 1], lo[i])
            hi[i] = min(hi[i], hi[i + 1])
        if any(a > b for a, b in zip(lo, hi)):
            return None
        if old == (tuple(lo), tuple(hi)):
            return tuple(lo), tuple(hi)


def bound(lo, hi, scale):
    lower, upper = (scale, lo[0], lo[1]), (scale, hi[0], hi[1])
    caps = tuple(hi[2] // x for x in lower)

    @lru_cache(None)
    def arm(axis, t, ucap, vcap):
        if t > caps[axis]:
            return 0
        j, k = [x for x in range(3) if x != axis]
        best = 0  # Empty continuation.
        for u in range(ucap + 1):
            for v in range(vcap + 1):
                if lower[axis] * t + lower[j] * u + lower[k] * v > hi[2]:
                    continue
                count = (u + 1) * (v + 1)
                slice_score = count * (
                    4 * upper[axis] * t + 2 * upper[j] * u
                    + 2 * upper[k] * v - 3 * lo[2] + scale
                )
                best = max(best, slice_score + arm(axis, t + 1, u, v))
        return best

    best = None
    for core in product(*(range(x + 1) for x in caps)):
        if sum(x * w for x, w in zip(core, lower)) > hi[2]:
            continue
        count = (core[0] + 1) * (core[1] + 1) * (core[2] + 1)
        score = count * (2 * sum(x * w for x, w in zip(core, upper))
                         - 3 * lo[2] + scale)
        for axis in range(3):
            j, k = [x for x in range(3) if x != axis]
            score += arm(axis, core[axis] + 1, core[j], core[k])
        if best is None or score > best:
            best = score
    return best


def degree_four_cap():
    # Deliberately enumerate both rectangle side lengths at every arm level.
    best = 0
    for core in product(range(5), repeat=3):
        if sum(core) > 4:
            continue
        count = (core[0] + 1) * (core[1] + 1) * (core[2] + 1)
        for axis in range(3):
            j, k = [i for i in range(3) if i != axis]
            for t in range(core[axis] + 1, 5):
                count += max((u + 1) * (v + 1)
                             for u in range(core[j] + 1)
                             for v in range(core[k] + 1) if t + u + v <= 4)
        best = max(best, count)
    assert best == 29
    return best


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int)
    parser.add_argument('--input', default='round5/weight_arrangement/full_interval_certificate.json')
    parser.add_argument('--output', default='round5/structural_audit/independent_interval_dp_results.json')
    args = parser.parse_args()
    source = json.loads(Path(args.input).read_text())
    scale = source['scale']
    checks = {'dp': 0, 'continuous': 0, 'empty': 0}
    leaves = source.get('leaves')
    if leaves is None:
        leaves = [node for node in source['tree'] if node['kind'] != 'split']
    if args.limit:
        leaves = [leaves[i * len(leaves) // args.limit] for i in range(args.limit)]
    start = time.time()
    for leaf in leaves:
        tightened = tighten(*leaf['box'])
        if tightened is None:
            assert leaf['kind'] == 'empty'
        else:
            lo, hi = tightened
            if leaf['kind'] == 'continuous':
                assert lo[2] >= 2 * (scale + hi[0] + hi[1]) + 3 * scale
            else:
                actual = bound(lo, hi, scale)
                assert actual == leaf['bound'], (lo, hi, actual, leaf['bound'])
                assert actual <= scale
        checks[leaf['kind']] += 1
        if sum(checks.values()) % 1000 == 0:
            print(json.dumps({'checked': sum(checks.values()), 'seconds': time.time() - start}), flush=True)
    result = {'status': 'PASS', 'scope': 'independent leaf-bound replay; no tree coverage claim',
              'sampled': bool(args.limit), 'checks': checks,
              'degree_four_no_interior_cardinality_bound': degree_four_cap(),
              'seconds': time.time() - start}
    Path(args.output).write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
