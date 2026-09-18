#!/usr/bin/env python3
"""Fresh exact checks for the analytic reduction, not a substitute for proof.

No previous verifier is imported. All bounded instances use Fraction.
The finite strip theorem itself is an explicitly separate dependency.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import hashlib


def ideals_cube(side):
    """All plane partitions in a side x side x side cube."""
    rows = list(product(range(side + 1), repeat=side))
    rows = [r for r in rows if all(r[i] >= r[i + 1] for i in range(side - 1))]
    def visit(prefix):
        if len(prefix) == side:
            yield {(i, j, k) for i in range(side) for j in range(side)
                   for k in range(prefix[i][j])}
        else:
            for r in rows:
                if not prefix or all(x <= y for x, y in zip(r, prefix[-1])):
                    yield from visit(prefix + [r])
    yield from visit([])


def saw_primitive(x, period):
    q = x // period
    r = x - q * period
    return q * period * period / 2 + r * r / 2


def main():
    counts = dict(ideals=0, ideals_with_units=0, weighted_ideals=0,
                  individual_phase_inequalities=0, summed_phase_inequalities=0,
                  thickening_identities=0, sawtooth_intervals=0,
                  remainder_fibers=0)
    units = {(1, 0, 0), (0, 1, 0), (0, 0, 1)}
    for points in ideals_cube(3):
        counts['ideals'] += 1
        if not units <= points:
            continue
        counts['ideals_with_units'] += 1
        m = len(points)
        sums = tuple(sum(x[i] for x in points) for i in range(3))
        tops = [{tuple(x[j] for j in range(3) if j != i):
                 max(y[i] for y in points
                     if all(y[j] == x[j] for j in range(3) if j != i))
                 for x in points} for i in range(3)]
        for weights in product(range(1, 5), repeat=3):
            M = max(sum(a * b for a, b in zip(weights, x)) for x in points)
            u = tuple(F(a, M) for a in weights)
            mu = tuple(u[i] * F(sums[i], m) for i in range(3))
            kappa = 3 - 4 * sum(mu)
            s, v = sum(u), min(u)
            delta = []
            for i in range(3):
                total = F(0)
                for x in points:
                    top = tops[i][tuple(x[j] for j in range(3) if j != i)]
                    total += 1 - u[i] * top - sum(u[j] * x[j]
                                                               for j in range(3) if j != i)
                delta.append(total / m)
                assert delta[i] == 1 - sum(mu) - mu[i]
                assert delta[i] >= 0
            assert sum(delta) == kappa >= 0
            for k in range(3):
                if u[k] != v:
                    continue
                for j in range(3):
                    if j != k:
                        assert 2 * delta[j] * (1 + v + u[j]) >= 2 * u[j] * mu[k] - v * (1 + v)
                        counts['individual_phase_inequalities'] += 1
            assert s * (1 - 3 * kappa) <= 4 * kappa + 5 * v - 3 * kappa * v + 4 * v * v
            counts['summed_phase_inequalities'] += 1
            continuous_mean = sum(mu[i] + u[i] / 2 for i in range(3)) / (1 + s)
            assert 3 - 4 * continuous_mean == (kappa + s) / (1 + s)
            counts['thickening_identities'] += 1
            counts['weighted_ideals'] += 1
    for period_num in range(1, 8):
        period = F(period_num, 7)
        for length_num in range(1, 50):
            length = F(length_num, 13)
            q = length // period
            r = length - q * period
            exact_minimum = (q * period * period + r * r) / 2
            assert exact_minimum >= length * length / (2 * (q + 1))
            assert length * length / (2 * (q + 1)) >= period * length * length / (2 * (length + period))
            assert saw_primitive(length, period) == exact_minimum
            assert exact_minimum <= period * length / 2
            counts['remainder_fibers'] += 1
            for start_num in range(-23, 24):
                start = F(start_num, 17)
                integral = saw_primitive(start + length, period) - saw_primitive(start, period)
                assert integral >= exact_minimum
                counts['sawtooth_intervals'] += 1
    assert F(90, 31) - F(29, 10) == F(1, 310)
    assert 5 * 78 * 78 - 390 * 78 + 89 == 89
    assert 80 * 79 * 78 // 6 == 82160
    # Recheck the rational formula transformations without symbolic software.
    for n in range(4, 201):
        v = F(1, n)
        sbound = (9 * v + v * v) / (1 - 3 * v)
        assert (v + sbound) / (1 + sbound) == 2 * v * (5 - v) / (1 + 6 * v + v * v)
        assert sbound / v == 9 + F(28, n - 3)
        assert ((5 * (1 + 6 * v + v * v) - 84 * v * (5 - v))
                == 89 * v * v - 390 * v + 5)
    result = dict(status='PASS', scope='bounded exact analytic sanity checks; not the finite strip or final DP replay',
                  counts=counts, script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
