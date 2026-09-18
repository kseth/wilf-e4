# Adversarial audit of the proposed complete four-generator composition

10 September 2026.

## Verdict

**Final verdict: the computer-assisted composition is complete.** The corrected high-height certificate and its complete independent replay have now passed, discharging the one obligation left conditional in the first version of this audit. I found no missing multiplicity, corner, weight-order, or height-endpoint case, and no remaining logical gap in the composition described below.

This conclusion follows from reviewing the mathematical hypotheses and the finite proof structure, not merely from a `PASS` label. In the final review I reread `geometric_residual.md`, checked the preferred-ideal and full-corner arguments, reconstructed the normalized moment and strict arithmetic margin, and checked the continuous-gap/phase reduction and the low/high boundary once more. The saved high certificate's bytes, SHA-256, completion flag, node counts, and largest accepted scaled bound were separately inspected.

The low-height certificate and its full independent replay have also completed. Older subclass and small-multiplicity conclusions retain their explicitly stated computer-assisted dependencies. This is an independent in-session mathematical audit, not a machine-formal proof or external referee report. External mathematical review remains outstanding.

## 1. Precise sufficient chain

The following statements, taken together, imply Wilf for every minimally four-generated numerical semigroup:

1. Every multiplicity `m≤29` satisfies `W_4≥0`.
2. For `m≥30`, every preferred Apéry ideal with no full-support corner satisfies `W_4≥0`.
3. For `m≥30`, the full-support corner `(1,1,1)` and all permutations of `(2,1,1)` satisfy `W_4≥0`.
4. For `m≥30`, one full-support corner of coordinate sum at least five, and actual normalized height `H<7`, the completed low-height argument gives `W_4≥0`.
5. The completed corrected high-height certificate and its full independent replay exclude every **failure** of `m−D_0≤29/10` in the residual corner class with `7≤H≤78`, under the necessary phase and continuous-gap conditions used by its clipping.

All five inputs have now completed. Item 5 was the remaining certificate obligation when this audit was first written; its final verification is recorded in Section 8 below.

The global conductor bound and the displayed multiplicity cutoff `82,160` are not separately needed in the high-height composition. They remain useful corollaries and search bounds. The argument below reduces a hypothetical negative Wilf case directly to `7≤H<78`.

## 2. The preferred ideal and arithmetic identity

Let `S=<m,a_1,a_2,a_3>` be minimally four-generated, with `m` the smallest generator. For each element of `Ap(S,m)`, choose its lexicographically least factorization in the other three generators. Positive weights ensure that a fixed integer has finitely many factorizations.

The chosen set `T` is a lower ideal. If `x` is chosen and `y≤x`, a violation of the Apéry property for `y` would extend to one for `x`; a lexicographically earlier factorization of `y` would likewise extend to one for `x`. It has exactly `m` points, with residues bijective modulo `m`. Minimal generation places the three unit vectors in `T`.

If `p` is minimal excluded and `r∈T` is its residue representative, their supports are disjoint. Otherwise subtraction of a common coordinate gives distinct equal-residue points in `T`. A full-support `p` therefore represents zero. Two distinct full-support excluded points would then give a collision after subtracting any coordinate. Consequently there is at most one full-support excluded point.

Put

\[
A=\min_i a_i\ge m+1,\quad b_i=a_i/A,\quad
M=\max\operatorname{Ap}(S,m),\quad H=M/A,
\]

\[
D_0=3mH-4\sum_{x\in T}b\cdot x.
\]

The exact genus identity is

\[
\boxed{mW_4=A D_0-m(m-1).} \tag{1}
\]

All notation in the low- and high-height certificates is compatible with this normalization; in particular the high worker's height is `H`, not the unnormalized integer `M`.

Coordinate permutations preserve lower closure, residue injectivity, and the full-corner condition. Thus one may sort the real normalized weights as `(1,b,c)` even though a permuted ideal need not be lexicographically least for the new coordinate order. None of the subsequent arguments requires that additional property.

## 3. Strict arithmetic margin at the first remaining multiplicity

Suppose `m≥30` and `W_4<0`. Since `W_4` is integral, (1) gives

\[
D_0\le\frac{m(m-2)}{A}
\le\frac{m(m-2)}{m+1}
=m-3+\frac3{m+1}.
\]

Hence

\[
\boxed{m-D_0\ge\frac{3m}{m+1}\ge\frac{90}{31}
>\frac{29}{10}.} \tag{2}
\]

The last strict margin is exactly `1/310`. This remains strict at `m=30`; there is no lost endpoint. Conversely, a proved weak inequality `m−D_0≤29/10` suffices to exclude negative Wilf numbers. It does **not** imply strict positivity of `W_4`.

No residue or corner hypothesis beyond those already used to obtain (1) is needed for this arithmetic bridge.

## 4. Coverage of the low-height branch

After items 1–3, a hypothetical counterexample has `m≥30` and one full-support minimal excluded point `p` with `|p|_1≥5`.

If `H<7`, then `b_i≥1` gives

\[
|x|_1\le b\cdot x\le H<7 \quad(x\in T),
\]

so `T⊂Δ_6`. Every predecessor `p−e_i` is in `T`, hence `|p|_1≤7`. Sorting corner coordinates leaves exactly

\[
(1,1,3),(1,2,2),(1,1,4),(1,2,3),(2,2,2),
(1,1,5),(1,2,4),(1,3,3),(2,2,3).
\]

The enumeration in `low_degree6/low_height_theorem.md` contains all three coordinate-plane projections as planar lower ideals in `Δ_6`, with matching coordinate axes and the required proper projections of `p`. Removing the one full-support excluded generator gives a no-interior ideal `U`, and exactly

\[
T=U\setminus(p+\mathbb N^3).
\]

The following filters used there are necessary, rather than heuristically plausible:

* Plane-corner representatives lie on the complementary axis and are distinct. For a plane corner dominating the projection of `p`, its representative lies in the terminal portion of that axis of length at most the opposite coordinate of `p`. This proves both stated plane-corner-count restrictions.
* The erosion inequality follows from injectivity on `E−B` whenever `E+B⊂T`; the projection formula uses that `E` is lower.
* The surface inequality `|F_i∩F_j|≤2n_k` follows from the direct mixed-excluded-point injection proved in `global_step_audit.md`.
* Every final-window point is coordinatewise maximal because each nonmultiplicity generator exceeds `m`. Thus at most six maxima permits the separately certified six-final-window theorem.

For every other surviving shape, the exact dual certifies

\[
3mH-4\sum_i b_i\sum_{x\in T}x_i\ge m-29/10
\]

for all `b_i≥1`, `H≥b·x`, and `H≤7`. Allowing `H=7` in the linear program is a safe enlargement; it does not claim that every ideal with actual height exactly seven has degree at most six. The `H=7` endpoint of the overall composition belongs to the high-height branch.

I checked the dual's signs directly. The displayed nonnegative combination expands to the target objective, including cancellation of the upper-bound term `γ(7−H)−7γ`. Point membership and nonnegativity of all coefficients are necessary; the completed independent verifier explicitly checks them. Thus the finite certificate yields a contradiction to (2) on this entire low-height branch.

## 5. The high-height compact reduction

For the remaining branch `H≥7`, sort normalized weights as `(1,b,c)`. Since all coordinate units are in `T`,

\[
1\le b\le c\le H.
\]

Set `v=1/H`, `S=1+b+c`, `s=S/H`, and `κ=D_0/(mH)`. The coordinate-line slack identity gives `κ≥0`. A putative failure in (2) gives `κ<v`; in fact only `D_0<m` is needed here.

The phase estimate is

\[
s(1-3\kappa)\le4\kappa+5v-3\kappa v+4v^2. \tag{3}
\]

Its hypotheses hold: `v<1/3` because `H≥7`; all normalized-by-height weights are at most one; the coordinate-line slacks are nonnegative. Replacing `κ` by the strictly larger `v` gives

\[
\boxed{S<9+\frac{28}{H-3}.} \tag{4}
\]

I independently checked the phase algebra. Summing the two sawtooth bounds along the minimum-weight axis leaves a coefficient proportional to the middle normalized weight minus `1+v`, which is nonpositive. Discarding it and using the maximum-weight bound gives (3), with the displayed signs and constants.

The rectangular thickening of `T` preserves the support of every minimal excluded vertex. The uniform-gap theorem therefore applies and gives

\[
\frac5{42}\le\kappa_c
=\frac{\kappa+S/H}{1+S/H}.
\]

Since `κ<1/H`, this implies

\[
\boxed{5H<42+37S.} \tag{5}
\]

Alternatively substitute the full phase bound into `κ_c` to obtain

\[
\frac5{42}<\frac{2v(5-v)}{1+6v+v^2},
\]

where the intended chain is `5/42≤κ_c<` the right side. Cross multiplication gives

\[
5H^2-390H+89<0.
\]

The polynomial is positive at `H=78` and increasing thereafter. Therefore every failure satisfies

\[
\boxed{7\le H<78.} \tag{6}
\]

The high certificate starts from the larger closed box with `7≤H≤78`, so it includes the lower boundary and safely overcovers the upper boundary.

I also checked the uniform-gap transfer: inverse images of excluded orthants cannot turn a zero coordinate into a positive one; the integer section allowances are exactly `18,19,20,21`; the translation integral has Jacobian one; and the average remainder on each lower coordinate fiber is at most half a mesh interval. Thus the finite strip's `D_R≥4|T|` premise yields the stated `5/42` continuous gap with no interpolation assumption. Its three independent exact strip implementations remain explicit computational dependencies.

## 6. Why failure-only clipping is sufficient

The residual tree does not need to prove a geometric inequality for points that violate (4) or (5). Instead, assume a genuine negative Wilf case and follow its parameter point through the tree. By (2), (4), (5), and the weight ordering, that point survives every valid clipping operation.

For a denominator-`q` closed box, the corrected code uses upward rounding for each strict real upper bound. In particular, the bound on `qb` is

\[
\operatorname{ceil}\bigl((S_{\rm bound}-q)/2\bigr),
\]

not downward integer division. This correction is essential. The earlier incorrectly rounded runs cannot be used.

Using the lower height endpoint in (4) enlarges the upper bound on `S`, because its right side decreases with `H`. The derived bounds on `b`, `c`, and `H` are likewise outward bounds. Repetition twenty times need not attain a fixed point: it merely retains a possibly larger box. Empty boxes exclude all parameter points satisfying the necessary failure conditions.

A split covers the whole clipped box with two closed children sharing the midpoint. Consequently a hypothetical failure follows at least one branch until it reaches either a proved empty leaf or an accepted DP leaf, provided the finite tree is complete.

For a DP leaf, lower weights and upper height enlarge feasibility, while upper weights and lower height enlarge the additive score:

\[
q(m-D_0)\le\sum_{x\in T}(4w_{\rm upper}\cdot x+q-3H_{\rm lower,scaled}).
\]

An independently verified upper bound at most `29q/10` contradicts (2). This is the exact reason that a **conditional failure-only certificate** is enough for the global proof; it is not circularly assuming the desired moment inequality.

## 7. Corner and shape coverage in the high worker

The true residual corner has positive coordinates and `|p|_1≥5`. Since the first normalized weight is one and `p−e_1∈T`,

\[
b\cdot p\le H+1.
\]

Thus it is included in the worker's loops over positive compositions through `floor(H_upper)+1`, with the weaker lower-weight test `w_lower·p≤H_upper+1`. Both symmetry reductions are applied only when the corresponding **lower and upper** weight coefficients agree. They are symmetries of the enlarged bounding problem and do not require the actual weights within equal intervals to be equal.

Removing `p` from the excluded generators gives a finite no-interior closure `U`; the positive corner removes no axis points. Therefore every axis cap of `U` is bounded by the corresponding `floor(H_upper/w_lower_i)`. The no-interior structure theorem expresses `U` as a central box and three disjoint arms with nested rectangular sections. Its chordal-graph argument and tree median cover a single box, a path, and the three-arm case.

The worker clips each section and the center before testing its retained maximum. This is essential: using the uncut maximum would wrongly discard permitted shapes. I checked the retained-maximum and doubled-moment formulas in the current serial and parallel workers. The zero option terminates an arm; prefix maxima include every smaller rectangle; the central box and arms are disjoint. Nonminimal or inactive enumerated corners only enlarge the class.

The worker's early-stopping flag is safe only because a DP leaf is accepted when the separate completion flag is true. A witness above the threshold causes a split or unresolved status, not acceptance. Empty corner ranges are treated as an empty represented class.

## 8. Completed final acceptance gate

The final saved **corrected** high certificate and independent replay meet all of the following requirements:

* The exact initial box `((q,q,7q),(78q,78q,78q))`, with `q=4096`.
* No pending nodes, no unresolved leaves, and an explicit completion flag.
* An independent full traversal validating every incoming box, every outward clip, every closed split, every empty leaf, and unique visitation of every node.
* Independent recomputation of every accepted DP bound across every eligible corner, with no sample-only or coverage-only mode substituted.
* All accepted scaled bounds satisfying `10·bound≤29q` and all worker completion flags true.

The supplied `verify_residual_certificate.py` explicitly distinguishes complete from checkpoint, sampled, and coverage-only results. I reviewed its current cache-reconciliation logic: cached entries must be unique final-tree leaves, match the original and independently clipped boxes and exact bound, have a full Cartesian corner count at least the producer count, and match the source hash of an independently audited worker. Missing records are recomputed. The final non-sampled, non-coverage-only gate asserts that fresh plus matched independent replays equals the total number of DP leaves.

The frozen certificate is `geometric_residual/residual_parallel_interval_certificate.json`, with SHA-256

`173fe6ec196b3d2adabad313749482542ad3492b5f6b4e398e76bbe6e52e405c`.

Its actual bytes were inspected in this final review. They have `complete:true`, no pending stack, no unresolved leaves, and:

| Item | Count |
|---|---:|
| Total tree nodes | 94,459 |
| Closed split nodes | 47,229 |
| Accepted DP leaves | 47,088 |
| Empty leaves | 142 |
| Pending or unresolved leaves | 0 |
| Largest accepted scaled bound | 11,824 |

The threshold is `29·4096/10=11,878.4`, so the largest finite accepted bound satisfies it strictly. The generic theorem is nevertheless stated with the weak bound `m−D≤29/10`, exactly as needed.

The preserved first complete replay record, `geometric_residual/independent_full_tree_replay_47088_checks.json`, matches this certificate hash and records 39,495 previously observed, unchanged independent leaf replays plus 7,593 newly completed independent leaf replays: exactly 47,088 leaves. The corresponding full Cartesian corner counts are 31,435,556 and 4,416,582, totaling 35,852,138. Its scope is `complete tree`, with `sampled:false` and `coverage_only:false`. The latest reconciliation record separately reports 46,991 matched leaf replays plus 97 newly recomputed records, again covering exactly the same final tree.

These records use independently reviewed retained-point or disjoint-piece integration and full Cartesian corner enumeration. They do not credit an unobserved calculation or claim that each independent worker was run on every leaf. The producer uses different clipped-box subtraction formulas and symmetry pruning. A fresh no-cache full replay remains reproducible using the invocation in `geometric_residual.md`.

## 9. Final implication and limits of the claim

Assume a minimally four-generated numerical semigroup had `W_4<0`. The completed small-multiplicity and special-corner results reduce it to `m≥30` and a preferred ideal with one full-support corner of coordinate sum at least five. If `H<7`, the completed low-height certificate contradicts the strict arithmetic margin (2). If `H≥7`, the phase and uniform-gap arguments force `7≤H<78`; the now-complete high-height tree and independent leaf bounds give the same contradiction. These two branches are exhaustive, and `H=7` is explicitly included in the second.

Consequently the assembled computer-assisted argument proves

\[
\boxed{4|S\cap[0,c)|-c\ge0}
\]

for every minimally four-generated numerical semigroup `S`, with the explicitly identified analytic and exact computational dependencies. No numerical-semigroup counterexample was produced. The conclusion concerns embedding dimension four; higher embedding dimensions are not settled by this composition. External review and any future formalization are additional validation, not omitted cases in the stated argument.
