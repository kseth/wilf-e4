# R5: independent complete degree-six profile audit

## Result and scope

B5-FV is established internally under V0. This is not external mathematical
review or a proof-assistant certificate. The analytic coverage and witness
proofs are in [the degree-six note](../../paper/residual-degree-six.md).
The [fresh execution record](r5-replay.json) freezes every input by hash
at commit `e65a00c28119eb545b3ac6e4a7eb1743ccfda6c8`.

Both independently generated all 1,429 nonempty plane profiles and checked
5,574,644 eligible triples. Every ideal satisfied the local or axis predicate.
There were exactly 431 local failures; all passed the axis predicate.
Neither implementation reads that list or any saved shape, residue,
dual-witness, optimization, or historical output file.

| Corner | Eligible ideals | Local failures, all handled by the axis formula |
|---|---:|---:|
| (1,1,3) | 1,581,961 | 215 |
| (1,2,2) | 1,433,543 | 212 |
| (1,1,4) | 874,540 | 3 |
| (1,2,3) | 638,574 | 1 |
| (2,2,2) | 592,453 | 0 |
| (1,1,5) | 159,580 | 0 |
| (1,2,4) | 105,119 | 0 |
| (1,3,3) | 94,500 | 0 |
| (2,2,3) | 94,374 | 0 |

Some margins are zero. The required inequalities are weak; accepting
equality is mathematically necessary and is not a numerical tolerance.

## Independent mathematical paths

Path A, [the bitset checker](check_profiles_bits.cpp), recursively generates
all nonincreasing seven-entry height profiles with entry bound `7-i`.
It enumerates the nine explicit sorted corners, counts planar mixed
corners by positive height drops, and indexes compatible third profiles
by their two axis lengths. Each triple constructs the literal retained
point set, after clipping by the positive corner, inside a 343-bit cube.
The degree cap is checked at every retained column top before acceptance.

Absent one-step successors give the three coordinate top surfaces.
Right shifts with explicit interior masks avoid wraparound between rows
and planes. The union of one-step predecessor masks, followed by another
masked predecessor step, computes the existence of one- and two-step
successors independently of the surface intersections. Intersecting those
sets with line tops gives the integer local gain. Line mass and all three
weighted-top moment identities are checked on every eligible ideal.

Path B, [the column checker](check_profiles_columns.cpp), generates profiles
by enumerating every seven-element subset of a fourteen-element set and
applying the proved partition bijection. It generates sorted corners by
integer loops, identifies planar mixed corners from both immediate
predecessors, and builds literal integer column heights. Cardinality and
moments use sums over columns rather than Path A's point accumulation.
Top surfaces are tested by neighboring heights. Existence of a successor
of degree two is checked by the six explicit moves
`2e_i` and `e_i+e_j`; lower closure implies a degree-one successor.
This gives the same gain by a separate formula.

Both apply precisely the specification's degree, cardinality, and three
two-direction surface filters. There is no maxima-count, erosion, modular,
realizability, or saved-local-failure skip. Both check the axis rational
inequality by clearing its positive integer denominator; they use
different expressions for its moment terms. Every eligible triple must
pass an unconditional check of at least one of the two predicates.

The [runner](replay.py) compiles fresh temporary binaries, executes each
complete path, and only then compares all nine per-corner records,
including filter counts, cardinality histograms, margins, and diagnostic
checksums. Checksums are not acceptance predicates. Their defined unsigned
wraparound cannot affect signed mathematical calculations. An empty
eligible corner class would be represented without a claimed minimum;
none of the nine classes in this execution was empty.

## Arithmetic, failure semantics, and evidence

Mathematical values are signed integers with at least 63 value bits.
Indices are at most 343; profile codes fit in 21 bits; counters have at
least 64 value bits. The degree-six specification bounds cardinality,
moments, axis denominator, local gains, and rational-margin cross-products
below `2^30`; candidate counts are below `2^35`. A minimum's initial
sentinel is tested before any multiplication. No floating-point decision
or disabled C++ assertion is used.

The four negative executions reject partial modes and unexpected
arguments in both workers. Python optimized runner execution is also
rejected. Compilation diagnostics, malformed/incomplete outputs,
missing corners, inconsistent counts, failed witnesses, disagreement,
or input changes cause a nonzero exit and an incomplete failure record.
The runner checks that its hashed inputs are tracked and unchanged.
It writes only the bounded execution record; temporary binaries are removed.

The fresh complete run took 25.520 seconds: 17.701 seconds for the bitset
enumeration and 5.359 seconds for the column enumeration, plus compilation
and administration. Commands, compiler/Python/platform versions, all input
hashes, negative tests, results, and output hashes are in the record.

## Reproduction

From a clean tracked worktree at the frozen input version:

```sh
python3 -I -B verification/b5/replay.py
```

The output record is evidence for that complete execution, not a
substitute for rerunning the checkers or reviewing the analytic coverage.
The proof transfer is: a genuine B5 ideal, after simultaneous coordinate
and weight permutation, belongs to the exhaustive family; B5-FV gives
`max(U2,G)>=m`; both witness soundness proofs then give `D0>=m`.
The final-arithmetic lemma establishes the B5 Wilf conclusion.
