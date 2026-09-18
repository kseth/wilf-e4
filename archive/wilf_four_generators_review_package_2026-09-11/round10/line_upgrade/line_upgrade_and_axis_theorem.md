# Two explicit centroid constructions replace the residual dual registry

11 September 2026. Research result within the proposed four-generator Wilf proof. The analytic constructions below are elementary and general. Their sufficient union over the finite residual class is established by complete exact enumeration, not yet by a structural proof eliminating enumeration.

## 1. General line-upgrade construction

Let `T` be a nonempty finite lower ideal in `N^d`, let `m=|T|`, and write `s=sum_{x in T}x`. For every coordinate direction `i`, partition `T` into its nonempty coordinate lines. A line has top `t` and length `L=t_i+1`. Across all directions,

\[
\sum_{\ell}L_\ell=dm,\qquad
\sum_{\ell}L_\ell t_\ell=(d+1)s. \tag{1}
\]

For the second identity, fix coordinate `j`. Lines in direction `j` contribute twice `sum_T x_j`, because `(t_j+1)t_j=2 sum_{k=0}^{t_j} k`. Each of the other `d-1` directions contributes `sum_T x_j`, because coordinate `j` is constant on its lines.

For every top `t`, choose a point `u(t)` of maximal total degree among the points of `T` that dominate `t` coordinatewise. Such a point exists and is coordinatewise maximal. Define

\[
U(T)=\sum_\ell L_\ell\bigl(|u(t_\ell)|_1-|t_\ell|_1\bigr),
\qquad
z_U=\frac1{dm}\sum_\ell L_\ell u(t_\ell).
\]

Then `z_U in conv(T)` and

\[
r_U=dmz_U-(d+1)s
 =\sum_\ell L_\ell(u(t_\ell)-t_\ell)\ge0,
\qquad |r_U|_1=U(T). \tag{2}
\]

Thus any lower bound on the integer `U(T)` supplies a weight-independent centroid witness. In dimension three, for arbitrary real `b_i>=1` and `H>=max_T b.x`,

\[
3mH-4b\cdot s\ge U(T). \tag{3}
\]

No optimization algorithm or certificate registry is required to construct this witness.

### A simpler sufficient lower bound

Every nonmaximal line top can increase total degree by at least one. Every maximal point occurs as a top in all `d` directions, with total line weight `|u|_1+d`. Therefore

\[
U(T)\ge dm-\sum_{u\in\operatorname{Max}(T)}(|u|_1+d). \tag{4}
\]

For `d=3`, the condition `sum_MaxT (|u|+3)<=2m` is therefore sufficient for the stronger target `U(T)>=m`. The corresponding `<=2m+2` condition proves `U(T)>=m-2`. These are general analytic lemmas, not merely finite observations.

## 2. General axis construction

Suppose `q_i=max_T x_i>0` for every coordinate, and put `q_*=max_i q_i`. Each axis endpoint `q_i e_i` belongs to `T`. Define

\[
G(T)=q_*\left(dm-(d+1)\sum_i\frac{s_i}{q_i}\right). \tag{5}
\]

If `G(T)>=0`, set `lambda_i=(d+1)s_i/(dm q_i)`, so `sum_i lambda_i<=1`. Assign these masses to the axis endpoints, then assign the remaining mass to any longest axis endpoint. The resulting convex combination `z_A` satisfies

\[
r_A=dmz_A-(d+1)s\ge0,
\qquad |r_A|_1=G(T). \tag{6}
\]

In fact all surplus is in the selected longest-axis coordinate. Thus in dimension three, whenever `G(T)>=0`,

\[
3mH-4b\cdot s\ge G(T) \quad(b_i\ge1). \tag{7}
\]

The line construction and the axis construction need not use the same points or the same coupling. Their union is valid because either witness suffices.

## 3. Strong residual theorem

Let `T subset N^3` be a lower ideal with:

- total degree at most six;
- `m=|T|>=30`;
- exactly one full-support minimal excluded point `p`, with `5<=|p|<=7`;
- the plane-corner, erosion, and pairwise-surface restrictions specified in `round7/low_degree6/low_height_theorem.md`.

The complete enumeration establishes the stronger inequality

\[
\boxed{\max\{U(T),G(T)\}\ge m.} \tag{8}
\]

Consequently there is an explicitly constructed `z in conv(T)` such that

\[
\boxed{3mz-4s\ge0,\qquad \sum_i(3mz_i-4s_i)\ge m.} \tag{9}
\]

This improves the previous residual bound `m-29/10` to `m`. It eliminates every low-degree LP proposal, basis inverse, assignment record, and individual rational dual certificate from the necessary verification. Shape enumeration remains.

The exact minima of `max(U,G)-m` for the nine sorted corner types are:

| Corner | Shapes | Minimum |
|---|---:|---:|
| (1,1,3) | 708,617 | 0 |
| (1,2,2) | 976,430 | 0 |
| (1,1,4) | 571,100 | 1 |
| (1,2,3) | 519,716 | 2 |
| (2,2,2) | 533,570 | 4 |
| (1,1,5) | 150,481 | 14 |
| (1,2,4) | 100,341 | 22 |
| (1,3,3) | 90,696 | 27 |
| (2,2,3) | 91,090 | 33 |
| **Total** | **3,742,041** | **0** |

The exact all-case counts, including the number needing the axis witness at the stronger threshold `m`, are in `independent_verification.jsonl`. The separate file `coverage.jsonl` records an earlier diagnostic at the weaker threshold `m-29/10`; its counts must not be used as the counts for (8).

### Consequence for the proposed Wilf proof

For a genuine four-generated semigroup, write `A=min(a_1,a_2,a_3)>=m+1` and `D_0=3mH-4b.s` for `b=a/A`. The exact Apéry identity gives

\[
mW_4=AD_0-m(m-1).
\]

For a semigroup whose preferred ideal lies in this residual class, (9) gives

\[
mW_4\ge Am-m(m-1)=m(A-m+1)\ge2m,
\quad\boxed{W_4\ge2.}
\]

The other geometric/multiplicity classes and the high-degree argument remain separate dependencies. This new lemma does not alone establish unrestricted Wilf or the whole proposed proof.

## 4. What the canonical construction cannot prove alone

The pure line-upgrade assertion `U>=m-2` is false even under all the enumerated restrictions. There are 121 failures at this weaker threshold, all with `30<=m<=34` and corner type `(1,1,3)` or `(1,2,2)`. They comprise 62 coordinate-permutation orbits. The complete exact point sets are in `upgrade_failures.jsonl`, and `verify_fixtures.py` checks their lower-ideal property, minimal exclusions, plane-corner counts, erosion, all surface bounds, line identities, and axis witnesses using only integer and rational arithmetic. Every one has `G-m>=8`.

For one transparent example, the profiles in the `xy`, `xz`, and `yz` planes are respectively

```
[5,3,2,1,1,0,0], [7,4,2,2,1,0,0], [7,4,2,2,1,0,0].
```

Remove the orthant above `p=(1,1,3)`. The resulting ideal has `m=32`, `s=(27,27,42)`, all pairwise surface bounds saturated, and erosion exactly 32. Its optimal monotone line upgrades have total surplus `U=26<m-2`. But

\[
z=\frac9{32}(4,0,0)+\frac9{32}(0,4,0)+\frac7{16}(0,0,6)
\]

has surplus `3mz-4s=(0,0,84)`. This is an obstruction to insisting on individual coordinatewise transport of each line top. It is not an obstruction to the centroid inequality and is not asserted to be a genuine Apéry ideal.

## 5. Verification and remaining analytic task

The bitset producer builds coordinate-plane partitions recursively, constructs the ideals as bitset intersections, and computes `U` by explicit comparison of each line top with every dominating maximal point. The separate verifier `independent_closed_form.cpp` generates partitions from seven-element subsets, constructs literal column heights, recomputes all filters, and obtains maximal dominating degree by a reverse dynamic program. It directly checks both coordinate-line identities for every accepted ideal. The axis computation uses an integer product denominator. There are no floating-point operations or external proof-data inputs.

The source performs all 55,199,298 axis-compatible profile triples, all geometric filters, and all 3,742,041 final centroid checks. It requires `max(U,G)>=m` for every accepted ideal. The portable entry point compiles and runs this source in a temporary directory and compares all coverage fields and multiplicity histograms with the archived run.

The strongest analytic target is now the explicit, parameter-free inequality (8) for the residual geometric class. A structural proof of (8), possibly by charging the nonmaximal line-top mass using the surface and erosion restrictions, would remove the shape enumeration. The current result gives two formulas in place of millions of witness records; it does not yet prove (8) without finite verification.
