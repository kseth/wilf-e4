# Adversarial audit: the six-final-window and conductor dependencies

11 September 2026.

**Finding:** I found no mathematical gap in the six-final-window reduction, its all-residue/all-lift certification route, the analytic conductor reduction, or the separate implication from the interior corner `(1,1,1)` to at most six maxima. This finding is confined to those dependencies. It does not audit the later continuous gap, no-interior interval theorem, short-corner theorem, or final high-height certificate.

The review below reconstructs the argument from the definitions and inspected source logic. It does not treat earlier PASS reports or matching enumeration counts as proofs of mathematical completeness. I did not rerun the existing large certificate computations in this audit.

## 1. Materials examined

- `prior/wilf_edim4_six_point_and_column_theorems_2026-09-05.md`.
- Section 4 of `deliverables/wilf_edim4_global_finite_reduction_2026-09-05.md`.
- `round2/arithmetic/interior_corner_111.md`.
- Source implementations in `round7/six_point_dependency_replay/`: `enumerate_compressed.cpp`, `wilf_six_point.py`, `extend_six_point.py`, `verify_final_window.py`, `check_residue_labels.cpp`, `verify_six_certificates.py`, `run_six_point_verification.py`, and the relevant helpers in `wilf_work.py` and `wilf_reassessment.py`.

The older `round6/audit_foundations.md` and `round7/six_point_fresh_math_audit.md` were read as comparison documents, not used to replace the derivations below.

## 2. The exact inequality that makes the enumeration sufficient

Let `T` be a preferred Apéry lower ideal, `|T|=m`, with positive integer weights `a_j>m`. Put

\[
M=\max_{x\in T}a\cdot x,
\quad D=3mM-4\sum_{x\in T}a\cdot x,
\quad Z=\{x\in T:M-a\cdot x<m\}.
\]

The genus identity gives `mW_4=D-m(m-1)`. For a coordinate line of length `L` and top `t`, direct summation gives

\[
D=\sum_{j,\ell\parallel e_j}L_\ell(M-a\cdot t_\ell).
\]

The sum is over directions as well as geometric lines. Common points of differently directed lines do not make their contributions duplicates.

Every point of `Z` is maximal because adding a generator would increase its weight by more than `m`. Write the top deficit on a line as `mq+β`, with `0≤β<m`, and set `A=[a_j]_m`. If

\[
R=\sum_{r=0}^{L-1}[rA]_m,
\qquad C=|\{r:[rA]_m+\beta\ge m\}|,
\]

then the sum of the point-deficit residues on this line is `Lβ+R-mC`. Each direction partitions a full residue system, so summing in all three directions and subtracting `m(m-1)` yields exactly

\[
mW_4=\binom m2+\sum_\ell(mL_\ell q_\ell+mC_\ell-R_\ell).
\]

When the top is outside `Z`, `q≥1`. The `L` relevant axis residues are distinct, include zero, and have sum at most

\[
R\le m(L-1)-\binom L2.
\]

This line contributes at least `m`. For the lines topped by `Z`, the initial budget `binom(m,2)` pays for each used positive axis residue once. Axis points from different axes are distinct points of `T`; their residues therefore cannot coincide. The unpaid repeat count is precisely

\[
E(Z)=\sum_{z\in Z}|z|_1-\sum_{j=1}^3\max_{z\in Z}z_j.
\]

Each repeat costs at most `m-1`. Thus, with `B(T)` the sum of the three projection sizes,

\[
\boxed{mW_4\ge m\bigl(B(T)-3|Z|-E(Z)\bigr)+E(Z).}
\]

All equality cases are included. In particular, a nonnegative projection score suffices; the finite search need only cover negative scores.

## 3. Why rank compression does not discard a realizable six-point set

The arithmetic fact used here is elementary. If `p` is minimal excluded and `q∈T` has its residue, a shared positive coordinate would allow subtracting the same unit vector from both, producing two distinct equal-residue points of `T`. Their supports must therefore be disjoint. Two distinct minimal excluded points sharing a positive coordinate similarly have different residues. Hence a full-support excluded point represents zero and there is at most one.

For an antichain `Z`, let `U` be its lower hull, and let `V` be the intersection of the cylinders over the three plane projections of `U`. Any ideal with no full-support excluded point is its own pairwise closure. An ideal with one such point is its pairwise closure minus that point's upper orthant. These statements follow directly by classifying each minimal excluded point according to its support.

A successor `z+e_k` belongs to `V` precisely when, for each `j≠k`, some `w∈Z` satisfies `w_j≥z_j` and `w_k>z_k`. If this successor is forced, any completion retaining `z` as maximal must remove it using the unique full-support point `p`. This is equivalent to

\[
p_k=z_k+1,\qquad p_j\le z_j\quad(j\ne k).
\]

The coordinatewise greatest solution to all these requirements is the candidate used in `one_corner_completion`. Inconsistency cannot be repaired by any completion. If this candidate is positive and outside `U`, deleting its orthant from `V` retains `U` and removes all forced successors, proving sufficiency too.

The only delicate compression issue is whether replacing the smallest occurring level by zero invalidates positivity. If an upper bound `p_j≤z_j` arises from a forced successor in a different direction `k`, take the witness for the third coordinate. That witness is strictly larger in direction `k` and no smaller in the third direction; incomparability therefore forces it to be strictly smaller in direction `j`. Consequently `z_j` is not the least occurring `j`-level and remains positive after compression. Prescribed coordinates are successors and automatically positive.

All other conditions reduce to comparisons between occurring coordinate levels: for integer levels, `u+1≤v` means exactly `u<v`. Thus compression preserves completion feasibility even in the presence of repeated levels, translations, and unequal spacings. The code uses only this structural criterion; it does not prune a compressed shape merely because that compressed shape lacks a modular labeling.

## 4. Strict growth under every permitted insertion

Raise by one the subset `H={z∈Z:z_i≥r}`, where `r` is an occurring level. Put `b=|H|` and let `p,q` be its maxima in the other two coordinates. The two affected plane projections gain `p+1` and `q+1` points. The repeat count gains `b-1`. Hence

\[
\Delta\Phi_0=p+q+3-b.
\]

An antichain projects injectively on every pair of coordinates, giving `b≤(p+1)(q+1)`. For `b≤5` this implies a strictly positive increment. For `b=6`, a nonpositive increment can only occur at `(p,q)=(1,2)` or `(2,1)`, and injectivity then forces a full `2×3` projected grid.

Here is a direct check of the grid obstruction. Write the height over `(x,y)` as the minimum of its x-axis plane height and y-axis plane height, with possibly one additional constant cap in an upper-right quadrant. For grid rows `x_0<x_1` and columns `y_0<y_1<y_2`, maximality forces the six top heights to decrease strictly along rows and columns. At both `(x_1,y_1)` and `(x_1,y_2)`, each one-coordinate height bound is strictly above the actual height: compare respectively with the point above the same column in row zero and the point to its left in row one. Both heights must therefore equal the unique cap, contradicting their strict decrease. This argument is independent of coordinate gaps and weight values.

Every realizable compressed six-point set therefore has strictly positive score growth at every insertion. An arbitrary original set can be restored by precisely the implemented operations, including translation below its smallest level. If the final score is negative, all earlier scores along this restoration are negative. Since the score rises by an integer at each step, the negative expansion terminates without any numerical cutoff.

## 5. Completeness of the finite shape generation

The compressed generator exhausts all onto coordinate sequences with image `{0,...,r}`, `r<k`. Sorting the point rows lexicographically makes the first coordinate sequence nondecreasing. The remaining two sequences are unrestricted onto sequences; pairwise incomparability is checked. Identifying coordinate permutations does not impose an ordering on the future weights. This exhausts compressed antichains, including all repeated-coordinate patterns.

For a fixed expanded `Z`, every completion contains `U(Z)`. A minimal point of a nonempty difference between a target ideal and a current subideal lies on the successor frontier and has all positive-coordinate predecessors present. Thus the frontier rule in `all_negative_extensions` can produce every target ideal. The maximality test excludes exactly an added point dominating an element of `Z`. Along a path to a negative target, every intermediate score remains negative because plane projections can only increase.

The extension search is finite: `B(T)<3k+E(Z)` bounds every axis length, since each axis segment occurs in two plane projections, and therefore bounds all three coordinate extents. Importantly, the code does not discard intermediate ideals with several interior corners. That filter is applied only after extension, because adding points can remove interior corners.

The cardinality bound `m≤56` is an output of the retained enumeration, not an assumed bound on semigroups. The bitset residue checker explicitly fails outside its supported range `1≤m≤64`; it does not silently skip larger inputs. The complete runner checks the maximum output cardinality before the residue step.

For `k≤5`, the separate generator implements the same compression/insertion/extension argument without needing the one-corner filter. It is included in the complete runner. Thus the stated theorem is for `|Z|≤6`, not only `|Z|=6`.

## 6. All residues, equality walls, and all integer lifts

All retained genuine ideals contain `0,e_1,e_2,e_3`. Therefore the three generator residues are nonzero and pairwise distinct. Exhausting every ordered triple of distinct nonzero residues covers all genuine cases, even though many retained labelings need not come from numerical semigroups. The implementation checks every point for residue injectivity, which is bijectivity because there are exactly `m` points.

For each surviving ordered labeling `A` it checks every `f∈{0,...,m-1}` in

\[
\mathcal R_f(T,A)=\sum_{j,\ell\parallel e_j}
L_\ell[f-A\cdot t_\ell]_m\ge m(m-1).
\]

For any actual integer lift `a` and actual maximum `M`, set `f=[M]_m`. Every line deficit is a nonnegative integer with the displayed residue, so

\[
D=\sum L_\ell(M-a\cdot t_\ell)
\ge\mathcal R_f(T,A)\ge m(m-1).
\]

No upper bound on any lift, conductor, or generator is involved. No hyperplane arrangement, generic weight assumption, or strict weight-order chamber is used in this route. Equal values of competing weighted expressions and their boundary cases are therefore automatically included. The separate LP certificates can be omitted from the logical route entirely; they are additional certificates, not a dependency for the all-cut proof.

The inspected source computes the line length as `top_j+1`, which is exact for a lower ideal, and finds every line top by testing its coordinate successor. It checks the full ordered-label list against the certificate records and checks every modular cut. Thus its local arithmetic tests implement the stated sufficient inequality.

## 7. Analytic conductor reduction, reconstructed

Order the three actual generators as `a≤b≤d`. First suppose the ideal is full weighted:

\[
T=\{(x,y,z)\in\mathbb N^3:ax+by+dz\le M\}.
\]

Put `h_2=floor(M/b)` and `h_3=floor(M/d)`. For every `1≤y≤h_2`,

\[
p_y=(\lfloor(M-by)/a\rfloor+1,y,0)
\]

is minimal excluded: its x predecessor is included by the floor definition, and its y predecessor is included because `b≥a`. These points have distinct representatives on the z axis, so `h_2≤h_3+1`.

If `M<b+d`, no mixed yz point is included and `h_3=1`, so only three or four x-direction columns occur. If `M≥b+d`, there is a full-support corner above `(1,1)`, which uses residue zero. The `p_y` must then use nonzero z-axis residues, so `h_2≤h_3`. A second full-support corner would occur if `M≥2b+d`; hence `M<2b+d≤3d`. Together with `M≥b+d≥2b`, this forces `h_2=h_3=2`, and the yz projection is exactly `y+z≤2`.

The six-column possibility is impossible arithmetically. Write its column lengths as `A,B,C,F,E,G` over `(0,0),(1,0),(2,0),(0,1),(1,1),(0,2)`. Full weightedness gives `A>B>C`, `A>F>G`, and `E<min(B,F)`. If `r` is the additive order of `a`, the interior relation `Ea+b+d=0` puts the origin and mixed columns disjointly in the subgroup generated by `a`, giving `r≥A+E`.

The two xy mixed corners must represent the two nonzero z-axis points. The swapped assignment yields `(B-C+E)a=0`, impossible because `0<B-C+E<A+E≤r`. The unswapped assignment and its yz-symmetric counterpart imply that `B+F`, `2B-C`, and `2F-G` are positive multiples of `r`, each smaller than `2A≤2r`; all three equal `r`. Their equations imply `C+G=0`, contradicting positivity.

For the remaining three- and four-column cases, strict column descent makes all column tops maximal. Direct projection counting gives `Φ(T,Max T)=2A-4` or `2A-6`, respectively, which is nonnegative. Removing maxima from `Z` cannot increase `|Z|` or `E(Z)`, so the projection inequality above proves Wilf. This entire full-weighted theorem is analytic and independent of the six-point finite enumeration.

If the preferred ideal is not full weighted, some minimal excluded `p` has `a·p≤M`. Its predecessor lines have lengths `p_j` and tops `p-e_j`, so their contributions sum to

\[
\sum_{j:p_j>0}p_j\bigl(M-a\cdot(p-e_j)\bigr)
=M+(|p|_1-1)(M-a\cdot p)\ge M.
\]

If `W_4<0`, the full-weighted case is already excluded and integer-valuedness gives `mW_4≤-m`. Therefore

\[
\boxed{M\le D=mW_4+m(m-1)\le m(m-2).}
\]

Since every nonmultiplicity generator is an Apéry element and `c=M-m+1`, this gives exactly the claimed bounds on conductor and generators. No large-multiplicity assumption or finite-computation dependency enters this conductor argument.

## 8. The `(1,1,1)` interface

When `(1,1,1)` is minimal excluded, its residue is zero: `A+B+C=0`. A mixed xy corner `(u,v,0)` must represent a nonzero z-axis point `γe_3`. Subtracting `e_1+e_2` gives an included point of residue `(γ+1)C`. If `γ` is not the terminal z-axis exponent, this collides with the included point `(γ+1)e_3`. Thus every such corner represents the terminal axis point. Distinct mixed xy corners must have distinct residues, so there is at most one of them. The same holds in the other planes.

Every included point has at least one zero coordinate. Each of its three plane sections is a rectangle with at most one upper-right quadrant deleted and hence has at most two planar maxima. Every global maximum belongs to the union of these three planar-maxima sets, so there are at most six. The final Apéry window is a subset of these maxima, supplying exactly the hypothesis of the audited six-final-window theorem.

## 9. Conclusion and precise limits

The requested dependency chain has no remaining gap identified by this review. Its finite part is explicit: one must trust or independently reproduce the exhaustive compressed-shape generation, all permitted insertions and extensions, full ordered residue labeling, and the modular cuts. The mathematical arguments above establish why those finite tasks cover the relevant infinite family and why equality cases and arbitrary integer lifts are included.

This is an in-session adversarial review, not formal verification or external peer review. It supports these specific dependencies; it does not independently certify the whole four-generator manuscript.
