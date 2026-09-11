# Fresh mathematical audit of the six-point dependency

10 September 2026.

**Verdict: no mathematical coverage gap found.** The six-final-window theorem, including arbitrary multiplicity, arbitrary genuine positive integer weights, and all integer lifts of the residue labelings, is supported by the written reductions and the examined implementation. Its use to exclude ideals with at most six coordinatewise maximal points in the new low-height proof is valid.

This is a fresh mathematical review of
`prior/wilf_edim4_six_point_and_column_theorems_2026-09-05.md`
and the combinatorial/modular source files in
`prior/wilf_edim4_six_point_verification_2026-09-05/`.
I did not rerun the computation. The root agent's complete fresh replay is recorded separately in `round7/six_point_dependency_replay/`; its reported matching counts are the computational input to this audit. This audit does not replace external mathematical review.

## 1. Preferred ideals and the precise six-point hypothesis

Let `T` be the preferred Apéry factorization ideal, with positive generator weights `a_j≥m+1`, size `m`, and maximum weight `M`. Define

\[
Z=\{x\in T:M-a\cdot x<m\}.
\]

This is the desired final Apéry window because `M=c+m−1`. Every `z∈Z` is coordinatewise maximal: a successor in direction `j` would have weight at least `a·z+m+1>M`. This proves the exact implication used in the low-height certificate:

\[
|\operatorname{Max}_{\rm coord}T|\le6
\quad\Longrightarrow\quad |Z|\le6.
\]

No converse identification of coordinatewise maxima with the final window is assumed. `Z` is permitted to be a proper subset of the maximal set throughout the finite extension enumeration.

The restriction to at most one full-support minimal excluded point also follows directly from residue bijectivity. A minimal excluded point and its included residue representative cannot share a positive coordinate, since subtracting that coordinate produces two distinct equal-residue included points. Thus a full-support corner represents zero. Two different full-support corners would give two distinct equal-residue predecessors in any direction, which is impossible.

## 2. Independent derivation of the projection estimate

Write `C=m(m−1)/2`. On a direction-`j` line of length `L` and top `t`, put

\[
M-a\cdot t=mq+\beta,
\quad A=[a_j]_m,
\quad R=\sum_{r=0}^{L-1}[rA]_m,
\quad N=|\{r:[rA]_m+\beta\ge m\}|.
\]

The residues of the deficits along that line sum to `Lβ+R−mN`. In each coordinate direction, the lines partition `T`, so those deficit residues total `C`; across the three directions they total `3C`. Combining this with the line-moment identity gives

\[
D=3C+\sum_\ell(mL_\ell q_\ell+mN_\ell-R_\ell),
\]

and subtracting `m(m−1)=2C` yields the manuscript's identity

\[
mW_4=C+\sum_\ell(mL_\ell q_\ell+mN_\ell-R_\ell).
\]

For a line whose top lies outside `Z`, `q≥1`. Its `L` axis residues are distinct, including zero, and

\[
R\le\frac{(L-1)(2m-L)}2.
\]

The line contributes at least `m+L(L−1)/2≥m`. There are `B(T)−3|Z|` such lines, where `B` is the sum of the three projection cardinalities.

For the remaining lines, the budget `C` pays for each used nonzero axis residue once. The relevant positive axis points are distinct points of `T`, even across coordinate directions, so the residue payments do not overlap. The unpaid repeat count is exactly

\[
E(Z)=\sum_{z\in Z}|z|_1-\sum_j\max_{z\in Z}z_j.
\]

Each repeat costs at most `m−1`. Consequently

\[
mW_4\ge m\bigl(B(T)-3|Z|-E(Z)\bigr)+E(Z).
\]

All signs and constants in this reduction are correct. Only the negative projection-score cases require enumeration.

## 3. Completion criterion and rank compression

For an antichain `Z`, let `U` be its lower hull and `V` the intersection of the cylinders over its three coordinate-plane projections. Any completion of `Z` has pairwise closure containing `V`. A successor `z+e_k` forced into `V` must therefore be removed by the unique full-support corner `p`. Because its predecessor `z` stays included, this is equivalent to

\[
p_k=z_k+1,\qquad p_j\le z_j\quad(j\ne k).
\]

The manuscript's coordinatewise greatest solution of these constraints is necessary: it is at least the corner of any actual completion and therefore cannot belong to the lower hull `U`. It is sufficient as well: removing its upper orthant from `V` retains `U` and removes every forced successor, leaving all points of `Z` maximal. Empty sets of forced successors are handled separately by using `V` itself.

I specifically checked the possible compression pitfall concerning zero. A bound `p_j≤z_j` arises from a forced successor in another direction `k`. The witness for the third coordinate is larger in coordinate `k` and no smaller in that third coordinate. Since `Z` is an antichain, that witness must be strictly smaller in coordinate `j`. Hence `z_j` is not the least occurring `j`-coordinate and remains positive after rank compression. Prescribed coordinates `z_k+1` are positive automatically.

All other tests reduce to equalities or strict/weak comparisons among occurring levels: `u+1≤v` is exactly `u<v` for integer levels. Thus infeasibility of a compressed seed cannot become feasibility under stretching. The pruning is structural, not a modular-labeling test on a compressed shape.

## 4. Strict insertion growth and termination

Inserting a level in coordinate `i` raises a subset `H⊂Z` of size `b`. If `p,q` are its maxima in the other coordinates, the exact projection-score increment is

\[
\Delta\Phi_0=p+q+3-b.
\]

Pairwise projections of an antichain are injective, so `b≤(p+1)(q+1)`. For `b≤5`, the increment is always positive. For `b=6`, the only possible nonpositive cases are `(p,q)=(1,2)` and `(2,1)`; injectivity then forces a full `2×3` grid in the projection.

Such a grid cannot occur among maximal points of an ideal with at most one full-support corner. In the column-height description, the strictly decreasing heights at both interior row/column intersections are below both one-coordinate bounds. They would therefore need to equal the same unique interior cap. Their strict decrease makes that impossible. This argument remains valid when the grid's coordinate levels have arbitrary positive gaps.

Every insertion along a feasible six-point stretching path therefore raises `Φ_0` by at least one. Every antichain can be reconstructed from its consecutive-rank compression using the permitted insertions, including translations below its lowest level. If the final score is negative, every intermediate score is negative. The finite expansion explores all such steps; there is no unexplained bound on the number or size of insertions.

## 5. Exhausting all negative extensions

For fixed `Z`, any actual ideal contains its lower hull. The projection score is nondecreasing when points are added. Hence a path from the lower hull to a negative final ideal, adding minimal missing points, remains negative throughout.

The implementation generates every such minimal missing point from the successor frontier, checks all predecessor conditions, and rejects a point precisely when it would destroy the maximality of some element of `Z` or would make the score nonnegative. It does **not** reject an intermediate ideal merely for having too many interior corners. This matters because later additions can remove those corners.

The condition `B(T)<18+E(Z)` bounds all coordinate extents: every included axis segment contributes to two projections. Thus the extension search is finite without an imposed coordinate or multiplicity cutoff. The reported maximum size 56 among retained candidates is an output. The C++ residue checker verifies its supported size bound explicitly, rather than silently omitting larger inputs.

The compressed-seed generator enumerates all onto coordinate columns with values `0,...,r`, sorts rows lexicographically, tests incomparability, and identifies only coordinate permutations. The extension stage likewise canonicalizes simultaneous coordinate permutations of `(T,Z)`. These operations remove duplicates and preserve coverage. Arithmetic checking later treats every ordered residue labeling, so canonicalizing coordinates does not impose a weight ordering.

## 6. All residues and all integer lifts

Every genuine retained staircase contains `0,e_1,e_2,e_3`. Their residues are distinct, so enumerating all ordered triples of distinct nonzero residues omits no genuine labeling. Full bijectivity is tested on every point of the ideal; no gcd or heuristic realizability filter is substituted for that test.

For each surviving labeling and each `f∈{0,...,m−1}`, the certificate checks

\[
\sum_{j,\ell\parallel e_j}L_\ell[f-A\cdot t_\ell]_m\ge m(m-1).
\]

For an actual integer lift of the residue labels, choose `f=[M]_m`. Each line deficit `M−a·t_ell` is a nonnegative integer with the indicated residue, so it is at least that least residue. The line-moment identity then proves `D≥m(m−1)` and hence Wilf. This establishes the conclusion for every lift, regardless of conductor or generator size. No numeric upper bound on those lifts is used.

This modular certificate alone suffices. The separately recorded global moment certificates are additional confirmation; their optimization software need not be trusted to justify the modular proof route.

## 7. Remaining concerns and limits

I found no unresolved mathematical gap in this dependency or in its use by the low-height proof. The dependence on finite computation is explicit: completeness uses the proved structural reductions plus the exhaustive enumeration and all-cut modular checks. A count match by itself would not prove the mathematics; the source logic and the reductions above provide that justification.

This finding does not establish the separate high-height theorem, does not turn a bounded random search into a proof, and does not certify external publication priority. It removes no qualifications about the overall project beyond confirming this particular oldest finite dependency.
