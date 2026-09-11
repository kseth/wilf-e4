# The high-height one-corner theorem and a low-height geometric obstruction

10 September 2026. **The exact interval certificate and its independent
full-tree replay are complete.** Every one of the 47,088 accepted DP leaves
has been independently verified. There are no pending or unresolved leaves.
The computation proves the following high-height theorem, with the uniform
continuous gap and structural results specified below as explicit dependencies.

**Theorem.** Let T be a finite lower ideal in N^3, with exactly one
full-support minimal excluded point p satisfying |p|_1>=5, and let
positive weights have minimum 1. Define

\[
m=|T|,\qquad H=\max_{x\in T}a\mathbin{\cdot}x,\qquad
D=3mH-4\sum_{x\in T}a\mathbin{\cdot}x.
\]

Then

\[
\boxed{H\ge7\quad\Longrightarrow\quad m-D\le\frac{29}{10}.}
\]

This bound is sufficient for Wilf for genuine four-generator Apéry ideals
in this class with multiplicity at least 30, by the integer-slack lemma
`round5/integer_slack_bridge.md`. Indeed, W_4<0 would give
m-D>=3m/(m+1)>=90/31>29/10. No arithmetic restrictions on the abstract
ideal are required for the geometric theorem itself. Lower heights and
the other corner classes belong to the separate arguments in the combined
manuscript. External mathematical review remains outstanding.

## An exact counterexample to the unrestricted geometric target

The ideal reconstructed in `round7/erosion_fixture.md` has

p=(1,2,2), a=(1,1,1), m=48, H=5, sum_T|x|=170, D=40.

Thus m-D=8: both the stronger m-D<=1 and the weaker m-D<=29/10 fail.
This is not a Wilf counterexample. Its coordinate-plane mixed corner
counts (5,4,4) violate the arithmetic upper bound |p|-2=3. Independently,
for B={0,e1,e2,e3}, the erosion A={x:x+B is contained in T} has cardinality 23 while
A-B has cardinality 55 > 48. This excludes every additive residue-bijective group
labeling of T. The exact constructive checker is
`round7/verify_erosion_fixture.py`.

## Bounded fixed-parameter diagnostics

The C++ clipped-box and nested-rectangle DP was evaluated at 2,193 parameter
triples: a=(1,B/4,C/4), B,C drawn in order from
{4,5,6,7,8,10,12,16,20,24}, with height from max(5,(B+C)/4) through 16 in
steps of 1/4. Every possible p of coordinate sum at least 5 and satisfying
4p1+Bp2+Cp3<=4H+4 was considered, with exact symmetry reduction where
available. There were 70,171 corner computations.

The only failure of m-D<=29/10 in this diagnostic was the preceding
unit-weight height 5 example; no failure occurred at H>5. This is a
finite grid diagnostic, not a proof for any open real region.

Source and complete rows are under `round7/geometric_residual/`:
`residual_all_corners.cpp`, `residual_parameter_scan.txt`.

## The full real parameter region

The script `certify_residual_parallel.py` covers the full real
region 1<=b<=c<=H, 7<=H<=78 for all remaining corners |p|>=5.
It uses integer endpoints with common scale q=4096; its boxes cover real
parameters, including their boundaries, rather than sampling them.

A putative failure has D<m-1. The previously audited phase bound gives
S=1+b+c <9+28/(H-3).
The separately restored continuous gap 5/42 gives
D/m >=(5H-37S)/42, hence 5H<42+37S.
Combining the two strict inequalities gives

\[
5H^2-390H+89<0.
\]

This polynomial has value 89 at H=78 and is increasing for H>=78.
Consequently every putative failure with H>=7 has H<78. Minimality of
the positive corner p implies that all three coordinate unit vectors
belong to T, so c<=H. The initial closed box therefore contains every
possible failure after sorting the normalized weights. The continuous
gap and phase arguments, including the thickening transfer and their
computational dependencies, are in `round7/uniform_gap_theorem.md`;
`round7/final_composition_audit.md` independently checks this reduction.

These necessary conditions and b<=c<=H are used only to remove impossible
failure parameters. Every division used for an integer upper endpoint is
rounded upward. An initial floor-rounding bug in the bound on b was
caught by an independent review before completion; those initial runs
were terminated and the corrected search restarted.

For each surviving box, lower weight endpoints and the upper height
endpoint enlarge the feasible ideal class. Upper weight endpoints and
the lower height endpoint enlarge the objective 4 sum a.x+(1-3H)m.
`interval_all_corners_parallel.cpp` computes an exact upper bound for each p and
accepts only after all p satisfy 10 bound<=29q. Earlier positive bounds
only trigger further subdivision; they never establish failure.

The finite p loop is exhaustive because minimality gives
q p1+B_lower p2+C_lower p3<=H_upper+q, hence |p|<=floor(H_upper/q)+1.
Coordinate permutations are removed only where both lower and upper
weight endpoints agree, so the enlarged objective and feasible set are
symmetric. Every other orientation is included.

### Why the dynamic program is an upper bound

Remove p from the minimal excluded generators of T and call the resulting
lower ideal U. Its pure-axis excluded generators remain, so U is finite;
it has no full-support minimal excluded point and

\[
T=U\setminus(p+\mathbb N^3).
\]

The no-interior structure decomposes U into a central integer box and
three disjoint horns. Each horn has nested rectangular transverse
sections; the nesting follows from the lower-ideal property. The exact
structure and its use in the uniform-gap certificate are proved in
`round7/uniform_gap_theorem.md`. Clipping each disjoint piece by the
complement of p+N^3 preserves disjointness. Allowing arbitrary centers
and nested rectangles, even where p would not actually be minimal,
only enlarges the class.

For a scaled parameter box with lower weights l=(q,B0,C0), upper weights
u=(q,B1,C1), and height endpoints H0,H1, assign each retained point x
the integer score

\[
f(x)=4u\mathbin{\cdot}x+q-3H_0.
\]

For every actual parameter in the box, summing f over T is at least
q(m-D). Every actual retained point also satisfies l.x<=H1. Thus the
worker may maximize this additive score subject only to the latter
height test. For a horn with long coordinate t and transverse rectangle
[0,r]x[0,s], its clipped section has exact count, first moment, and
maximum l-weight. If F(t,r,s) is the best score from t onward, the
recurrence takes the maximum of stopping, shrinking either transverse
side, and (when the clipped section is feasible) retaining the section
and adding F(t+1,r,s). Its terminal value is zero. This enumerates all
nested rectangular sections, including underfilled horns. A central
box contributes its exact clipped score plus the three corresponding
horn values. Maximizing over centers therefore gives the required upper
bound, without an assumption that the height allowance is attained.

The finite p loop includes every genuine p: p-e_i belongs to T for
each i, and subtracting the unit-weight coordinate gives a.p<=H+1.
All lattice coordinates of retained points are at most floor(H1/q)<=78;
the pure-axis points of U survive clipping, so this also bounds every
center and horn coordinate needed to represent U. All intermediate
counts, doubled first moments and scores are below 10^15 in absolute
value, including the threshold multiplication by 10, and fit safely in
signed 64-bit arithmetic. No floating-point value decides an acceptance.

If the p loop is empty, its signed-64 minimum sentinel is a vacuous
exclusion of this corner class, not a maximum over a nonempty set.
The independent workers separately verify the zero corner count.

### Why interval subdivision covers real parameters

Each tree node starts with a closed integer-endpoint box divided by q.
Clipping removes only parameters violating a necessary failure condition;
all upper endpoints are rounded outward. An empty clipped box is excluded.
A split produces two closed children whose union is exactly the clipped
parent; both include the splitting face. A DP leaf is accepted only when
every possible p has exact score at most 29q/10. Induction from the root
then excludes every real failure once every leaf is empty or accepted.
The mesh is a representation of enclosing intervals, not an assumption
that the unknown weights or height lie on a rational grid.

The frozen file `residual_parallel_interval_certificate.json` has
`complete:true`, no pending stack and no unresolved leaf. It contains
94,459 nodes: 47,229 splits, 47,088 DP leaves and 142 empty leaves.
Its independent coverage and all-leaf DP replay have both passed. The producer's 47,088
accepted DP leaves contain 35,389,687 corner computations after symmetry
reduction. Of those leaves, 564 have no possible positive corner and are
vacuous exclusions. The maximum accepted scaled bound is 11,824, below
29q/10. The certificate SHA-256 is
`173fe6ec196b3d2adabad313749482542ad3492b5f6b4e398e76bbe6e52e405c`.

These facts complete the proof: a failure with H>=7 lies in the initial
real box by the compact reduction; the independently verified closed tree
covers every such parameter by empty or accepted leaves; each accepted
leaf gives m-D<=29/10. This contradicts the proposed failure.

## Independent source review

The corrected clipping code and the generic interval worker received a
separate source review. A fresh Fraction implementation agreed with 5,000
clipping comparisons; four independently computed generic interval bounds
agreed, including nonconstant equal-endpoint weight intervals and early
failure handling. The independent worker integrates retained cells by
disjoint first-below-corner pieces and enumerates corner triples in a
Cartesian loop without the generator's symmetry pruning. The bounded
comparisons were preparatory checks; the completed all-leaf gate is
recorded separately below.

## Reproducible execution and canonical artifacts

Compile `interval_all_corners_parallel.cpp` with a C++17 compiler, optimization
and OpenMP support (`-std=c++17 -O3 -fopenmp`), then run
`python3 round7/geometric_residual/certify_residual_parallel.py --limit 200000`.
The parallel wrapper changes only scheduling of independent corner
computations. Every acceptance requires all corners to finish and satisfy
the exact integer threshold; early rejection merely requests subdivision.
The original serial worker remains available for comparison.

The generator writes `residual_parallel_checkpoint.json` every 1,000
processed nodes; this is explicitly an incomplete tree with pending boxes.
The final file is `residual_parallel_interval_certificate.json`.
Independent replay is provided by `verify_residual_certificate.py` using
`independent_residual_point_worker.cpp` or the slower disjoint-piece
`independent_residual_worker.cpp`. Per-leaf cache records preserve the exact
original box, independently clipped box, verified maximum, full Cartesian
corner count and independently audited worker source hash. Reused records
must match the final tree unchanged. The completed final verification reports
`total_verified_leaves==coverage.dp`, `sampled:false`, and
`coverage_only:false`, with a complete tree and no pending or unresolved
leaf. Checkpoints and finite samples alone were not used to satisfy this gate.

The optimized independent replay worker,
`independent_specialized_piece_worker.cpp`, evaluates each clipped section
as at most two disjoint rectangles and the center as three disjoint boxes,
classified by the first coordinate below the corner. It does not use the
producer's subtraction-of-an-excluded-box formulas. Its complete Cartesian
corner loop includes every orientation without symmetry pruning. Its
source was separately audited, and all five saved comparison boxes agree
exactly with retained-point prefix integration. Cache provenance records
which of the three independently audited workers verified each leaf.

## Full verification record

The preserved first full-tree result is
`round7/geometric_residual/independent_full_tree_replay_47088_checks.json`.
It records the exact SHA-256 above and the following complete coverage:

| Verified quantity | Count |
|---|---:|
| Tree nodes | 94,459 |
| Split nodes | 47,229 |
| DP leaves | 47,088 |
| Empty leaves | 142 |
| Pending or unresolved nodes | 0 |
| Previously observed, matched independent leaf replays | 39,495 |
| Newly completed independent leaf replays | 7,593 |
| Total independently verified DP leaves | 47,088 |
| Full Cartesian corner computations in matched prior replays | 31,435,556 |
| Full Cartesian corner computations in new replays | 4,416,582 |
| Aggregate full Cartesian corner computations | 35,852,138 |

The flags are `status:PASS`, `scope:complete tree`, `sampled:false`, and
`coverage_only:false`. Cached checks count only when their original box,
independently clipped box, exact maximum, Cartesian corner count and
audited worker source hash match the unchanged final leaf. Records not
present in the visible cache were recomputed; inaccessible earlier
in-flight checks were not credited. Replayed leaf identities are unique.

The producer uses clipped-box subtraction formulas. Independent replays
use retained-point prefix counts and moments, or disjoint-piece integration,
including the optimized specialized two-rectangle section construction.
Every independent implementation enumerates the full Cartesian corner set
without the producer's symmetry pruning. The aggregate counts above count
each verified final leaf once; they do not claim that all three independent
workers were run on every leaf.

To repeat the complete independent gate from the certificate without
reusing any saved per-leaf checks, run from the repository root:

```sh
python3 round7/geometric_residual/verify_residual_certificate.py \
  --certificate round7/geometric_residual/residual_parallel_interval_certificate.json \
  --worker specialized --jobs 8
```

The verifier compiles its selected C++17 worker when needed. Omitting
`--cache` forces every accepted leaf to be recomputed. The separate
`independent_residual_complete_checks.json` is the most recent full
verification result and may also record a later cache-reconciliation pass;
the named 47,088-leaf record above preserves the first complete observed
replay and its new-versus-cached accounting.

The immutable per-leaf cache for this completed certificate is
`round7/geometric_residual/verified_residual_leaves_frozen.jsonl`, with
SHA-256
`1cf1a33b466fbd0a11406da0dc2b2c80ca46fe9f7f18c1dc7d35abb32ff696e7`.
It contains exactly the 47,088 unique final DP leaf identities and
35,852,138 Cartesian corner computations. The final reconciliation
recomputed 97 absent cache records comprising 4,488 corner computations,
then checked every frozen record against the final tree. Its stable
record is `independent_full_tree_reconciliation_checks.json`; the source
hashes, frozen-file hash and provenance are recorded in
`independent_residual_frozen_provenance.json`.

| Independently audited replay method | Final leaves | Cartesian corners |
|---|---:|---:|
| Generic disjoint-piece integration | 1,689 | 1,137,928 |
| Retained-point prefix counts and moments | 6,845 | 4,831,956 |
| Specialized disjoint-piece integration | 38,554 | 29,882,254 |
| Total | 47,088 | 35,852,138 |

The independent source and coverage audit is
`round7/geometric_residual/residual_interval_audit.md`. Its final section
names the completed certificate, frozen cache, both SHA-256 values and
the complete verification totals.
