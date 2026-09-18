# Independent audit of the residual interval construction

10 September 2026. This note audits the mathematical reductions and the corrected
generator source. Completion and full replay are separate obligations, recorded
in the machine-readable results of `verify_residual_certificate.py`.

## One bug found and corrected

The initial generator rounded the upper bound for the real parameter \(qb\)
down with integer division by two. This was unsound when the numerator was odd:
a strict real upper bound does not permit downward rounding to an integer.
The author corrected this to `ceildiv(Sbound-q,2)` and restarted the run.
The earlier interrupted runs cannot be used as certificates.

The following audit applies to that corrected expression.

## Conditional clipping is sound

Write the actual normalized weights as \((1,b,c)\), with
\(1\le b\le c\le H\), and \(S=1+b+c\). Suppose the proposed target fails:
\(m-D>29/10\). Then \(D<m-1\), so the existing phase estimate, for \(H>3\), gives

\[
S<9+\frac{28}{H-3}.
\]

The continuous gap \(5/42\), using
\(\kappa_c=(\kappa+S/H)/(1+S/H)\) and \(\kappa<1/H\), also gives

\[
5H<42+37S.
\]

For a closed grid box with denominator \(q\), replacing \(H\) by its lower
endpoint in the first bound gives a valid upper bound on \(S\). Rounding that
bound upward remains valid. The consequences

\[
b\le(S-1)/2,\qquad c\le S-1-b_{\rm lower},\qquad
H\le(42+37S_{\rm upper})/5
\]

are likewise rounded upward in the corrected implementation. Ordering propagation
uses only \(b\le c\le H\). Repeating these implications can only discard points
which fail a necessary condition for a counterexample. Stopping after twenty
iterations merely retains a possibly larger box.

The independent verifier implements these calculations using `Fraction`, with
explicit outward rounding. It does not import the generator's clipping function.
Five thousand deterministic box comparisons agreed with the corrected generator.

## Corner-loop completeness

Let \(p\) be an actual full-support minimal excluded exponent. In particular
\(p-e_1\in T\); the first normalized weight is exactly one. Therefore

\[
w\cdot p\le H+1.
\]

Since all weights are at least one, this implies
\(|p|_1\le\lfloor H_{\rm upper}\rfloor+1\). The generating worker enumerates
every positive composition of each total degree from five through this bound,
and retains every one satisfying the weaker necessary condition

\[
w_{\rm lower}\cdot p\le H_{\rm upper}+1.
\]

The first symmetry reduction applies only when the first two feasible and
objective weights are both equal. The second applies only when the second and
third feasible weights are equal **and** the corresponding objective weights
are equal. These conditions make the enlarged objective and feasible ideal class
invariant under the respective coordinate exchanges. The second reduction is
therefore sound even when the actual weights range through a nonconstant equal
interval: it is symmetry of the bounding problem, not a claim that the actual
weights coincide.

If no corner is eligible, the represented residual class in the box is empty;
the minimum signed integer sentinel records this case without being multiplied
inside the C++ worker.

## Interval objective and rectangle clipping

For each retained point, replacing weights by upper endpoints and height by its
lower endpoint bounds the scaled objective from above:

\[
q(m-D)\le \sum_{x\in T}
\bigl(4w_{\rm upper}\cdot x+q-3H_{\rm lower,scaled}\bigr).
\]

Replacing weights by lower endpoints and height by its upper endpoint enlarges
the permitted ideal class. The C++ variable `twice` is twice the upper-weight
moment, so `2*twice + count*(q-3*lo[2])` is exactly this enlarged objective.

For a clipped transverse rectangle, the retained maximum is achieved on one of
the two faces immediately below the excluded transverse corner. For a clipped
central box it is achieved on one of its three such faces. The generating formulas
for both maxima, both cardinalities, and both moments are correct.

The nested-section recurrence allows stopping and all smaller rectangles. Its
one-dimensional row and column prefix maxima implement the maximum over every
rectangle below the current bounds. The center and three outward arms are
disjoint. Their completeness depends on the previously audited no-interior
central-box/three-arm representation applied before removing the corner orthant.

The worker may terminate a box evaluation after one corner exceeds the target.
Its returned value is then only a witness. The Python generator requires the
separate completion flag before accepting any box; this is correct.

## Integer safety

At scale 4096 and height at most 78, each axis has at most 79 retained integer
positions. Flattened indices and allocation lengths are below \(80\cdot79^2\),
and thus fit signed 32-bit integers. All count-weight products and objective
values use signed 64-bit integers. A deliberately loose bound is

\[
79^3\bigl(12\cdot78^2\cdot4096+3\cdot78\cdot4096+4096\bigr)<2\times10^{14}.
\]

Even multiplying a finite score by ten stays far below \(2^{63}-1\).

## Independent replay

`independent_residual_worker.cpp` derives counts and moments from a disjoint
partition according to the **first** coordinate below \(p\). It does not use
upper-box subtraction or the generator's clipped-maximum formula. It enumerates
corner coordinates in a Cartesian loop and performs no symmetry pruning.

Initial comparisons cover four boxes, including equal nonconstant weight
intervals and a box where the generating worker correctly stops early. The
independent maxima agree with a separate Python implementation on all four.

`verify_residual_certificate.py` checks the original root, every node's incoming
box, every complete closed split (including the common boundary), every empty
leaf, and every accepted leaf. It checks unique visitation and rejects unreachable
nodes. Full replay recomputes every accepted bound with the independent worker;
sampled and incomplete-checkpoint results are explicitly labeled as such.

A successful sample does not by itself certify the complete parameter domain.

## Parallel generator and resumed independent replay

The parallel generator changes only the evaluation order of corner candidates.
Each dynamic-programming call has private state. The maximum, maximizing corner,
and evaluated count are updated in an OpenMP critical region. The early-stop flag
is atomic and only changes from false to true within a box. Consequently, an
accepted completion flag still implies that every eligible corner was evaluated.
Different failing witnesses or tied maximizing corners do not affect the split
decisions or any accepted maximum.

The independent verifier can distribute different leaves among subprocesses with
`--jobs 4`; no dynamic-programming state is shared. Its optional `--cache` mode
records the original box, independently clipped box, exact maximum, corner count,
and evaluator source hash for each completed replay. A final resumed run checks
that every cached leaf is an identical leaf of the completed tree. Running without
`--cache` recomputes all leaves from scratch. Cache files should have only one
writer process at a time.

The first independently replayed checkpoint contained 3000 processed nodes,
1492 accepted leaves, and 17 pending nodes. All 100 sampled leaves matched, across
44,513 independently enumerated corner cases. This result alone is partial.
An immutable later checkpoint with 8000 processed nodes and 3993 accepted leaves
was then submitted for full independent prefix replay while generation continued.
Its results are recorded separately; the completed-domain claim requires the
final tree and all of its leaves to be covered.

A second independent evaluator, `independent_residual_point_worker.cpp`, computes
each rectangle's counts, moments, and maximum from individual retained lattice
points and two-dimensional prefix arrays. The central box uses three-dimensional
point-prefix sums. It uses the same audited rectangle optimization recurrence,
without the generator's clipped-box subtraction or maximum formulas. Five exact
comparisons against the disjoint-piece evaluator passed, including a box with
1606 candidate corners. On that representative larger box the point evaluator
was about 2.3 times faster. Resumed replay accepts records from either evaluator
only when their source hash matches the corresponding included source file.

The verifier explicitly asserts that a nonsampled replay covers exactly every
accepted DP leaf. For the final complete-domain audit the required fields are:
`scope="complete tree"`, `sampled=false`, `coverage_only=false`, and
`total_verified_leaves=coverage.dp`, in addition to zero pending or unresolved
nodes.

The final fast replay uses `independent_specialized_piece_worker.cpp`, audited
separately by the root reviewer. It partitions a clipped transverse rectangle
into at most two disjoint rectangles and a clipped center into three disjoint
boxes. This retains the independent disjoint-partition method while avoiding
general-purpose per-piece coordinate loops. Its comparisons against the point
evaluator are recorded in `independent_specialized_piece_comparisons.json`.
The cache accepts the matching source hashes of all three included evaluators.

During an interrupted point-evaluator run, output showed progress beyond the
externally visible cache. The inaccessible records were **not** counted. Replay
resumed from the 8534 visible complete records and recomputed all others using
the specialized evaluator. Cache appends now reopen the path for every record
under a lock, preventing a long-lived descriptor from continuing to refer to a
replaced file. Independent process reads confirmed that the new records become
visible. This operational incident does not excuse any final leaf from replay.


## Final complete replay and frozen cache

The final parallel certificate has SHA256 `173fe6ec196b3d2adabad313749482542ad3492b5f6b4e398e76bbe6e52e405c`. Independent rational clipping and full-tree coverage passed on all 94,459 nodes: 47,229 split, 47,088 DP, 142 empty, zero pending, and zero unresolved. Every DP leaf was independently replayed or matched against a previously independently replayed identical box, clipped box, exact bound, and worker source hash. The result has `sampled=false`, `coverage_only=false`, and `total_verified_leaves=47088`.

The first complete replay (`independent_full_tree_replay_47088_checks.json`) used 39,495 cached plus 7,593 freshly replayed leaves, totaling 35,852,138 Cartesian corner cases. A final visibility reconciliation independently recomputed 97 missing cache records (4,488 corner cases), then validated and froze all records in the same process. The immutable `verified_residual_leaves_frozen.jsonl` was re-read after the writer exited and has SHA256 `1cf1a33b466fbd0a11406da0dc2b2c80ca46fe9f7f18c1dc7d35abb32ff696e7`. It contains exactly the final tree's 47,088 distinct DP IDs and 35,852,138 corner cases. No inaccessible cache records were counted.

Provenance: generic disjoint pieces, 1,689 leaves / 1,137,928 corners; retained-point prefix sums, 6,845 leaves / 4,831,956 corners; specialized disjoint pieces, 38,554 leaves / 29,882,254 corners. The machine-readable hashes, counts, and gates are in `independent_residual_frozen_provenance.json`; the final reconciliation result is `independent_full_tree_reconciliation_checks.json`.
