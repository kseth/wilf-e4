# R6b: complete high-height audit

## Result

B6-high-FV is established internally under V0. Together with
[R6a](r6a-strip-audit.md) and the analytic transfers in the
[mathematical contract](../../paper/residual-high-height.md), this closes B6
internally. This is not external review or a global composition audit.
The [fresh record](r6b-replay.json) identifies the exact inputs and executions.

Inputs were frozen at `a6e3be655ae37b603aa0d7f268bd081775ac2934`.
Both paths independently validated the entire closed parameter covering and
freshly computed every DP leaf. They agreed on every normalized leaf result,
not merely on the largest bound.

| Quantity | Result on each path |
|---|---:|
| Tree nodes | 94,459 |
| Splits | 47,229 |
| DP leaves | 47,088 |
| Empty leaves | 142 |
| Vacuous DP leaves (no eligible corner) | 564 |
| Cartesian corner evaluations | 35,852,138 |
| Largest nonvacuous bound numerator | 11,824 |
| Unresolved or unsupported nodes | 0 |

The scale is 4,096. The exact threshold is `10 V <= 29 * 4096`;
11,824 is below 11,878.4. No floating-point comparison enters acceptance.
The shared normalized leaf-result SHA-256 is
`14171f5ed92635d0ba1ad3b1246587b8bc77d40d60afe88cb86d13dc102b8a21`.

## Independent coverage and evaluation

[Path A](check_high_integer.py) derives every enclosure from its parent and
performs depth-first coverage with integer ceiling division.
Its [backend](high_subtract.cpp) obtains retained central scores by subtracting
the removed upper box, then evaluates horns with three prefix comparisons.

[Path B](check_high_rational.py) independently implements the clipping rules
using exact rational ceilings and breadth-first traversal.
Its [backend](high_disjoint.cpp) partitions each retained center into disjoint
coordinate pieces; horn transitions use row maxima followed by column prefixes.

Both require the exact root, supported node schemas, strict integer types,
closed shared split walls, and exactly one visit to every node. Clipping is
outward for at most twenty rounds; termination does not assume convergence.
Every nonempty DP enclosure is freshly evaluated. A corner-free leaf is
handled separately as vacuous, without arithmetic on a minimum sentinel.

Each worker enumerates the complete Cartesian positive-corner set proved
in B6.4. Endpoint symmetry does not prune the set. Consequently these fresh
corner counts can exceed the producer's safely pruned counts. The historical
accepted topology is retained for this reconstruction checkpoint, and its
cached metadata is schema-checked and compared afterward; cached scores
never substitute for a fresh bound or establish the acceptance predicate.
The standalone PRELIM input removes those cached fields altogether.

No residue, cardinality, unit, surface, realizability, or modular filter is
added to the abstract high-height theorem. Retained-height feasibility,
central-box/horn coverage, and the exact DP recurrence have their analytic
proofs in the contract.

## Arithmetic, failure checks, and reproduction

The fixed conservative score envelope is below `2^51`. C++ workers require
at least 63 signed value bits and 31 signed index bits. Thresholds, scores,
recurrences, feasibility, and counts are exact integers; sentinel values
are compared before any multiplication or addition.

Sixteen negative executions reject optimized Python, incorrect input identity,
duplicate fields, unsupported node kinds, malformed cached fields, unsound
empty leaves, Boolean endpoints, and gaps at child boundaries, on both paths.
The runner also rejects incomplete output, nonzero exit, compile warnings,
threshold failure, disagreement, dirty tracked inputs, or an input change.

The complete run took 3,555.792 seconds by the runner's elapsed clock;
paths A and B took 3,554.127 and 2,777.274 seconds respectively, running
concurrently. Commands, compiler versions, source hashes, output hashes,
negative-test details, and completion states are recorded.

From a clean tracked input version:

```sh
python3 -I -B verification/b6/replay_high.py
```

Whole-proof composition and the portable curated packet are assessed
separately in the [synthesis audit](../../research/prelim-synthesis-audit.md).

