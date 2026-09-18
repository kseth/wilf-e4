# Arithmetic surface constraints for genuine Apéry ideals

10 September 2026. This note proves a necessary structural inequality for all finite lower ideals that admit a residue-bijective lattice labeling. It does **not** prove the remaining Wilf inequality or the genuine-cell centroid bound.

## 1. A general two-direction surface bound

Let `T` be a finite nonempty lower ideal in `N^3`, and assume that `T` is a complete set of representatives of `Z^3/Λ` for a finite-index subgroup `Λ`. For `i=1,2,3`, define

\[
F_i=\{x\in T:x+e_i\notin T\},\qquad
n_i=1+\max_{x\in T}x_i.
\]

**Theorem.** For distinct `i,j,k`,

\[
\boxed{|F_i\cap F_j|\le 2n_k.}
\]

The left side is also the sum, over the `n_k` nonempty slices perpendicular to axis `k`, of the number of maximal points in the corresponding planar lower ideals. Thus their average number of maximal points is at most two.

### Direct residue proof

Let `C_{ij}` consist of all integer points `q∉T` with `q_i,q_j>0` and both `q−e_i,q−e_j∈T`. These are exactly the mixed minimal excluded points of the nonempty planar slices. A finite nonempty planar lower ideal with `h` maximal points has exactly `h−1` mixed minimal excluded points. Consequently

\[
|C_{ij}|=|F_i\cap F_j|-n_k.
\]

If `r∈T` represents the residue of `q∈C_{ij}`, then `r_i>0` would put the distinct equal-residue points `q−e_i,r−e_i` in `T`. Thus `r_i=0`, and similarly `r_j=0`. Every representative therefore lies on the `k`-axis.

Moreover, distinct `q,q'∈C_{ij}` cannot have equal residues: their distinct predecessors `q−e_i,q'−e_i` belong to `T`. Hence the representatives of `C_{ij}` are distinct points of the `k`-axis, which has `n_k` points. This proves `|C_{ij}|≤n_k` and the theorem. ∎

### Independent dilation proof

First recall the elementary difference-set consequence of a residue-bijective labeling. If finite sets `A,B` satisfy `A+B⊂U`, where `U` is a complete set of representatives of a finite quotient group, then the labeling is injective on `A−B`. Indeed, equality of labels on `a−b` and `a'−b'` gives equality of labels on `a+b'` and `a'+b`, both in `U`; injectivity on `U` implies equality of these integer vectors. Therefore

\[
|A-B|\le |U|. \tag{1}
\]

Choose integer dilation factors `L_i,L_j≥2` and `L_k≥1`, and set

\[
U=D T+\prod_{r=1}^3\{0,\ldots,L_r-1\},\qquad
D=\operatorname{diag}(L_1,L_2,L_3).
\]

The set `U` is a lower ideal and a complete representative set for `Z^3/DΛ`. Existence and uniqueness follow by coordinatewise Euclidean division by `L_r`, followed by reduction of the quotient vector to its representative in `T`.

Let `P_r=|π_rT|`, `Q=|F_i∩F_j|`, and

\[
B=\{0,e_i,e_j\},\qquad A=\{x\in U:x+B\subset U\}.
\]

The deleted part of `U` is the union of its direction-`i` and direction-`j` top layers. Their intersection has one fixed fine coordinate in directions `i,j`, with `L_k` choices in direction `k` for every point of `F_i∩F_j`. Exact inclusion–exclusion gives

\[
|A|=|T|L_iL_jL_k-P_iL_jL_k-P_jL_iL_k+QL_k. \tag{2}
\]

Since `A` is lower, the nonnegative points of `A−B` are exactly `A`; the other points form two disjoint negative coordinate faces. Thus

\[
|A-B|=|A|+|\pi_iA|+|\pi_jA|. \tag{3}
\]

To count `π_iA`, work in the slice with fine coordinate `i=0`. Because `L_i≥2`, the `+e_i` requirement is automatic there. The remaining `+e_j` requirement deletes precisely the top point of every line in the direction `j` in the dilated planar projection. The latter has `n_kL_k` such lines. Therefore

\[
|\pi_iA|=P_iL_jL_k-n_kL_k,
\qquad
|\pi_jA|=P_jL_iL_k-n_kL_k. \tag{4}
\]

Equations (2)–(4) yield the exact identity

\[
\boxed{|A-B|-|U|=L_k(Q-2n_k).} \tag{5}
\]

By (1), the left side is nonpositive. This proves the theorem. In particular, the fixed dilation `L_i=L_j=2,L_k=1` already proves the result; no limiting argument is required. ∎

The quotient `Z^3/DΛ` need not be cyclic. This is harmless: (1) applies to every finite quotient group. A genuine preferred Apéry ideal is a complete representative set for the cyclic residue quotient, so the theorem applies to it.

## 1a. Nonwrapping interval packing in the interior-corner case

Assume now that `T` has a full-support minimal excluded point `p`. Its residue representative is zero: any positive coordinate of its representative would give a predecessor collision.

Let `h_k` be the additive order of `e_k` in `Z^3/Λ`. Axis injectivity gives `n_k≤h_k`. In fact

\[
n_k<h_k.
\]

Otherwise `n_ke_k` and `p` would be distinct excluded points of residue zero with both predecessors in direction `k` belonging to `T`, again a collision.

Fix a consecutive run `q(t)=u e_i+v e_j+t e_k∈C_{ij}`, with `u,v>0` fixed. Write its axis representative as `r(t)e_k`. Then `r(t+1)−r(t)≡1 (mod h_k)`, and `0≤r(t)<n_k<h_k`. A wrap would require `r(t)=h_k−1`, which is unavailable. Therefore

\[
r(t+1)=r(t)+1.
\]

Thus every mixed-corner run maps to an ordinary interval of integer axis exponents, with no cyclic wrap. The intervals belonging to different runs are disjoint. In particular, the run beginning at `p` maps to an initial interval starting at axis exponent zero.

This refinement retains the lengths and assignments of the excluded-corner runs. The surface bound records only the total length of their disjoint images. It is a necessary structural condition, not yet a centroid or Wilf inequality.

## 2. The three-direction dilation identity

For a general finite lower ideal `T`, write `Q_{ij}=|F_i∩F_j|`, `K=|Max(T)|`, and `K_i=|Max(π_iT)|`. No lattice-labeling hypothesis is required for this identity.

Take all `L_i≥2`, construct `U` as above, and now use

\[
B=\{0,e_1,e_2,e_3\},\qquad A=U\ominus B.
\]

Then

\[
\boxed{|A-B|-|U|
=\sum_{\{i,j,k\}=\{1,2,3\},\ i<j}
L_k(Q_{ij}-2n_k)+\sum_iK_i-K.} \tag{6}
\]

For clarity, the sum has exactly the three terms associated to unordered pairs `(1,2),(1,3),(2,3)` and their complementary coordinate.

**Proof.** Three-set inclusion–exclusion gives

\[
|A|=|T|L_1L_2L_3-\sum_iP_iL_jL_k
+\sum_{i<j}Q_{ij}L_k-K.
\]

In the `i=0` plane, the direction-`i` condition is automatic. Eroding the remaining planar dilation in both coordinate directions gives

\[
|\pi_iA|=P_iL_jL_k-n_kL_k-n_jL_j+K_i.
\]

The only negative points in `A−B` lie on the three disjoint faces with one coordinate `−1`. Thus `|A−B|=|A|+Σ_i|π_iA|`. Cancellation proves (6). ∎

For a lattice fundamental domain, (6) is nonpositive for every such dilation. In addition to the coefficient bounds from Section 1, choosing all `L_i=2` gives the necessary inequality

\[
2\sum_{i<j}Q_{ij}-4\sum_i n_i+\sum_iK_i-K\le0.
\]

## 3. Entire symmetric obstruction family excluded

For integers `k≥1` and `R≥2k+1`, define

\[
T_{R,k}=\{(x,y,z)\in\mathbb N^3:
 x+y\le R,\ x+z\le R,\ y+z\le R,
 \min(x,y,z)\le k\}.
\]

Some members of this family disprove the unrestricted geometric `2/3` cell-centroid inequality. None admits a residue-bijective finite-group labeling.

The exact surface statistics are

\[
n_i=R+1,\quad K_i=R+1,\quad
Q_{ij}=(k+3)(R-k),\quad K=3(R-k).
\]

To count `Q_{12}`, split its points into four disjoint types:

1. `x+y=R`: there are `Σ_{z=0}^k(R−2z+1)=(k+1)(R+1−k)`.
2. `x=y=t`, `z=R−t`, `0≤t≤k`: there are `k+1`.
3. `x=k`, `y,z>k`, `y+z=R`: there are `R−2k−1`.
4. The coordinate swap of type 3: the same number.

Their sum is `(k+3)(R−k)`. The maximal points consist of the three versions of type 2 and the three choices of which coordinate is fixed at `k` in type 3. Hence `K=3(R−k)`.

For every rectangular dilation with all `L_i≥2`, (6) becomes

\[
|A-B|-|U|
=(k+1)\big[(R-k-2)(L_1+L_2+L_3)+3\big]>0.
\]

This contradicts (1). The strict inequality holds even at the endpoint `k=1,R=3`, where the linear coefficient vanishes but the constant is `6`.

The undilated family also fails the unit-simplex erosion test directly:

\[
\boxed{|T_{R,k}\ominus B-B|-|T_{R,k}|
=3(k+1)(R-k-1)>0,}\tag{7}
\]

where the left expression means `|(T_{R,k}⊖B)−B|−|T_{R,k}|`.

For a direct verification of (7), put

\[
V_R=\{x+y,x+z,y+z\le R\},\qquad f(R)=|V_R|.
\]

Then `|T_{R,k}|=f(R)−f(R−2k−2)`. Its erosion consists of `T_{R−1,k−1}` together with the points having at least two coordinates equal to `k`, subject to pair caps `R−1`; this adds `3R−6k−2` points. Each planar projection of the erosion is the degree-`R−1` triangle and has `R(R+1)/2` points. Finally,

\[
f(t)-f(t-1)=\left\lfloor\frac{3(t+1)^2+1}{4}\right\rfloor.
\]

The two boundary arguments `R` and `R−2k−1` have opposite parity. Substitution and cancellation give (7), including `R=2k+1` with `f(-1)=0`.

For the earlier fixture `R=29,k=3`, (7) is `4546−4246=300`; for uniform dilation by `L≥2`, the excess is `288L+12`. Thus arbitrary uniform coarsening does not remove this erosion obstruction.

## 4. Scope and outstanding implication

The new inequalities use modular injectivity, not generator magnitudes or a bounded search. They are necessary conditions for genuine Apéry ideals of every multiplicity. They do not assert that every ideal satisfying them admits a cyclic labeling, nor that they imply

\[
6\sum_{x\in T}a\cdot x\le4m\max_{x\in T}a\cdot x+m\sum_i a_i.
\]

The latter would establish the proposed genuine-cell `2/3` centroid bound. Its implication from the surface constraints remains under investigation. No Wilf counterexample is claimed.

Exact replay code and diagnostic data are in `round7/global_step/`. The identities above are proved symbolically; bounded numerical checks are implementation validation only.

## 5. Verification and bounded bridge probes

The following checks were actually completed:

* `verify_surface_identities.py`: every one of the 979 nonempty lower ideals in `{0,1,2}^3`; 2,937 two-direction identities and 979 three-direction identities, using direct enumeration of `A−B`, all passed.
* `verify_symmetric_erosion.py`: 210 undilated family instances and 15 rectangular dilations, all passed the exact symbolic formulas.
* `verify_corner_run_packing.py`: both previously saved genuine Apéry fixtures, checking the axis images and all six directional surface bounds exactly. For the interior fixture `<1213,1214,2478,4952>`, the three pairs `(Q_{ij},2n_k)` are `(98,102),(48,48),(26,26)`.

The two centroid probes below are explicitly heuristic and are **not** certificates:

* The unequal pair-cap probe tried 10,000 parameter tuples and optimized the positive weight cone for 2,386 qualifying ideals that passed the unit erosion test. It found no negative cell-centroid objective.
* The general profile probe used a million proposal slots in a fixed `16×16×16` box, searching one-corner ideals while penalizing failure of `Q_{ij}≤2n_k`. There were 78,979 qualifying proposals, with possible repetitions. The best observed unit-weight cell mean was approximately `0.638099`, below `2/3`. Positive-weight linear programs were solved only when this unit-weight record improved; they did not establish the full weight cone for every qualifying ideal.

These probes show only that these bounded attempts did not refute the proposed bridge. The implication from surface budgets and interval packing to the genuine-cell `2/3` inequality remains unproved. This task has not closed unrestricted four-generator Wilf and has not produced a numerical-semigroup counterexample.
