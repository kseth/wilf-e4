# R6a: complete finite-strip audit

## Result

B6-strip-FV is established internally under V0. Its conditional
finite-to-continuous proof therefore gives the \(5/42\) continuous gap.
This does not establish B6-high-FV, external review, or the global theorem.
The [mathematical contract](../../paper/residual-high-height.md#1-b61-finite-strip-specification)
and [fresh record](r6a-replay.json) specify the precise scope.

Inputs were frozen at `d1db65f122b864d2c8a31503911e32ab0231170c`.
Each independent implementation computed every one of the 1,029
configurations and unconditionally checked its bound against zero.
All individual bounds agreed, not merely their four aggregate maxima.

| Degree allowance | Configurations | Largest score \(4m-D_R\) upper bound |
|---|---:|---:|
| 18 | 204 | -50 |
| 19 | 237 | -53 |
| 20 | 274 | -56 |
| 21 | 314 | -59 |

The corner loops cover every sorted positive corner of degree at most
\(R+1\), including inactive corners representing no-full-corner ideals.
Missing units, zero axis caps, and singleton ideals are not skipped.
The displayed maxima are singleton scores; only nonpositive bounds
are required by the theorem predicate.

## Independent implementations

[Path A](check_strip_prefix.cpp) computes clipped counts and twice moments
by subtracting the removed upper box. Its feasibility test maximizes
over surviving faces. Horn optima use three separate prefix comparisons
and a backward level recurrence. Every feasible retained center is
enumerated, adding its three disjoint horn upper bounds.

[Path B](check_strip_points.cpp) starts from literal retained-point scores
in the full integer cube. Three-dimensional inclusion-exclusion prefixes
give central scores; retained maximum degrees use maximum prefixes.
For each horn level, a separately constructed two-dimensional point prefix
gives every section score and degree maximum. At every cap state it explicitly
enumerates every subrectangle, independently of Path A's prefix recurrence.
Corner generation uses a Cartesian cube with ordering and degree filters,
rather than Path A's nested constrained loops.

Both implement the structural coverage and exact recurrence already proved
in the specification. Neither reads saved bounds, historical code, shape
lists, residue labels, or producer outputs. The [runner](replay_strip.py)
compiles new binaries in a fresh temporary directory, validates complete
streams and exact configuration coverage, and compares individual results
only after both executions pass.

## Arithmetic, failure checks, and reproduction

All mathematical values have at least 63 signed value bits, indices at least
31; the specification's conservative envelope is below \(2^{31}\).
Point-score decisions, feasibility, recurrence, and comparisons are integral.
No floating-point decision or disabled C++ assertion is used.
The minimum-score sentinel is only compared, never used in arithmetic.

Four negative executions reject partial and unexpected-argument modes,
one of each on both workers. The runner rejects optimized Python execution,
dirty tracked inputs, compile warnings/failure, incomplete or reordered streams,
positive bounds, disagreement, or input changes.
Hashes, command lines, compiler/Python/platform versions, negative results,
and stdout hashes are in the record. The complete run took 3.485 seconds;
the two enumerations took 0.100 and 1.571 seconds.

From a clean tracked input version:

```sh
python3 -I -B verification/b6/replay_strip.py
```

The continuous conclusion uses the full translation/support/remainder proof
in the mathematical note; output agreement alone is not that transfer proof.
