# What the four-generator approach generalizes to other dimensions

11 September 2026. Internal research note. The identities and elementary propositions below are proved here. The archived fixed-dimension theorem is a proposed research theorem from the preceding manuscript; it is not presented as externally validated or as a solution in five or more generators.

## 1. A dimension-free arithmetic formulation

Let

\[
S=\langle m,a_1,\ldots,a_d\rangle,\qquad e=d+1,
\]

be minimally generated, with multiplicity `m`. Select the lexicographically least factorization of each Apéry element using the `a_i`. The selected set `T⊂N^d` is a finite lower ideal of size `m`, and its linear labels `w(x)=a·x` are bijective modulo `m`. Lower closure follows because a divisor of an Apéry factorization is again Apéry, and a lexicographically smaller divisor factorization would give a smaller factorization of the original element.

Put

\[
M=\max_{x\in T}w(x)=c+m-1,\quad \Sigma=\sum_{x\in T}w(x),\quad
D=dmM-(d+1)\Sigma.
\]

The genus formula gives the exact identity

\[
\boxed{mW_{d+1}=D-\frac{d-1}{2}m(m-1).}
\tag{1}
\]

Indeed, `g=Σ/m−(m−1)/2`, `n=c−g`, and `W_(d+1)=(d+1)n−c`; substitute `c=M−m+1`.

Every coordinate line in `T` is an initial integer interval. If its length is `L_ℓ` and its top is `t_ℓ`, summing its arithmetic progression gives

\[
\boxed{D=\sum_{\ell}L_\ell\bigl(M-w(t_\ell)\bigr)\ge0,}
\tag{2}
\]

where the sum includes lines in all `d` directions. In direction `j`, the sum of the weighted line tops is `Σ+Σ_x a_jx_j`; adding directions proves (2). This is a useful source of nonnegative terms in every dimension, although `D≥0` alone is weaker than Wilf.

### The exact negative-integer bridge also generalizes

Let `A=min a_i≥m+1`, and `D_0=D/A`. Since `W_(d+1)` is an integer, a counterexample has `W_(d+1)≤−1`. Equation (1) and `D≥0` then give

\[
D_0\le
\frac{\frac{d-1}{2}m(m-1)-m}{m+1},
\]

hence

\[
\boxed{W_{d+1}<0\quad\Longrightarrow\quad
\frac{d-1}{2}m-D_0\ge\frac{dm}{m+1}.}
\tag{3}
\]

For `d=3,m≥30`, the right side is at least `90/31`; the completed four-generator certificates instead bounded the left side by `29/10`. Thus the final contradiction is an instance of a dimension-free scheme. For `d=4`, the corresponding target is a bound on `3m/2−D_0` below `4m/(m+1)`. The old numerical constant `29/10` should not simply be copied into the next dimension.

## 2. Support restrictions and surface budgets in every dimension

The following statements apply to any finite lower ideal `T⊂N^d` that is a complete representative set for a finite quotient `Z^d/Λ`, including every preferred Apéry ideal.

If `p` is a minimal excluded exponent and `r∈T` represents its residue, then

\[
\operatorname{supp}(p)\cap\operatorname{supp}(r)=\varnothing.
\tag{4}
\]

If a common coordinate `i` existed, the distinct points `p−e_i,r−e_i∈T` would have the same residue. The same predecessor argument shows that two distinct minimal excluded exponents sharing a positive coordinate have different residues. A full-support excluded exponent therefore represents zero, and there can be at most one such exponent, in every dimension.

There is a useful extension beyond minimal excluded exponents. For nonempty `I⊂{1,…,d}`, let

\[
C_I=\{q\notin T:q_i>0\text{ and }q-e_i\in T\text{ for every }i\in I\}.
\]

Let `π_I` delete the coordinates in `I`. For a lower ideal, the number of points in the coordinate face where these coordinates are zero is `|π_I T|`. The representative of every `q∈C_I` lies in that face by the same argument as (4). Distinct `q` give different residues, by subtracting any fixed `e_i`, `i∈I`. Consequently

\[
\boxed{|C_I|\le |\pi_I T|.}
\tag{5}
\]

For `I` equal to all coordinates, (5) recovers the single-full-corner restriction.

Define direction-top sets

\[
F_i=\{x\in T:x+e_i\notin T\}.
\]

For any two distinct coordinates,

\[
\boxed{|F_i\cap F_j|\le2|\pi_{\{i,j\}}T|.}
\tag{6}
\]

To prove this, slice `T` at fixed values of its other `d−2` coordinates. A nonempty planar lower ideal with `h` maxima has `h−1` mixed excluded corners. Summing over slices gives

\[
|C_{\{i,j\}}|=|F_i\cap F_j|-|\pi_{\{i,j\}}T|.
\]

Apply (5). Thus the average number of maxima of these planar slices is at most two, regardless of the ambient dimension. In exponent dimension three the projection on the right is an axis interval, which recovers the earlier bound `|F_i∩F_j|≤2n_k`.

These inequalities retain genuine residue arithmetic at arbitrary scale. They are necessary conditions, not sufficient criteria for a lower ideal to be an Apéry ideal and not, by themselves, proved centroid inequalities.

### A general erosion inequality

If finite integer sets `B,E` satisfy `E+B⊂T`, then

\[
\boxed{|E-B|\le|T|.}
\tag{7}
\]

Equality of the residues of `x-y,x'-y'` implies equality of residues of `x+y',x'+y∈T`, hence equality of those integer vectors and of the original differences. The labeling is therefore injective on `E−B`.

Taking `B={0,e_1,…,e_d}` and `E=T⊖B`, lower closure gives

\[
|E-B|=|E|+\sum_{i=1}^d|\pi_iE|\le m.
\tag{8}
\]

The sets outside `E` in this difference set have exactly one negative coordinate, equal to `−1`, so their contributions are disjoint. Other choices of `B`, including after rectangular dilation of `T`, generate further necessary inequalities. There is no demonstrated finite list of such inequalities that implies Wilf in every dimension.

## 3. A general exact discrete-to-continuous transfer

Let `K` be a bounded measurable downset in the unit simplex in `R^d`, of positive volume. Suppose a structural class containing `K` is preserved by translated-grid sampling. Fix an integer `N≥d`, put `h=1/N`, and assume that every finite sampled ideal in that class, with degree allowance `R∈{N−d,…,N}`, satisfies

\[
dR|T|-(d+1)\sum_{x\in T}|x|_1\ge\lambda|T|.
\tag{9}
\]

Then

\[
\boxed{d-(d+1)\mathbb E_K|X|_1\ge\frac{\lambda-d/2}{N}.}
\tag{10}
\]

**Proof.** For each `r∈[0,h)^d` take `T_r={z∈N^d:r+hz∈K}` and
`R_r=floor((1−|r|_1)/h)`. The radius is in the stated degree window. By (9),

\[
\sum_{z\in T_r}\big[d-(d+1)|r+hz|_1\big]
\ge |T_r|(h\lambda-|r|_1),
\]

because `hR_r≤1−|r|_1`. Integrate over `r`. Each point of `K` is counted once, and its `r_i` is `X_i mod h`, up to null boundary choices. On an initial interval `[0,L]`, writing `L=kh+s`, `0≤s<h`, gives

\[
\int_0^L(t\bmod h)\,dt=kh^2/2+s^2/2\le hL/2.
\]

Apply this fiberwise to the downset: `E(X_i mod h)≤h/2`. The result is (10). ∎

The class with at most one full-support excluded orthant is preserved: sampling takes each excluded vertex to its coordinatewise ceiling after translating and rescaling; coordinates originally zero remain zero. Taking minimal vertices cannot create additional full-support vertices. In dimension three the earlier values `N=21,λ=4` give `(4−3/2)/21=5/42` exactly.

This transfers a finite combinatorial margin to a continuous margin without interpolation. It does not supply (9) automatically in the next dimension, and a positive continuous margin alone needs a discrete phase estimate to handle unequal weights.

## 4. What the archived fixed-dimension theorem already asserts

Part I of `deliverables/wilf_fixed_dimension_finite_reduction_2026-09-05.md` contains an analytic argument for the following proposed theorem, rather than merely suggesting it.

For each `d≥2`, set

\[
h_d=\frac1{8d},\quad r_d=\frac1{16d^2(d+1)},\quad
\delta_d=d!h_dr_d^d,
\]

\[
P_d=1+32d(d-1)(d+1)^2,\qquad
H_d=\frac{(d-1)P_d}{\delta_d},\qquad
B_d=\left\lceil\frac{(d+H_d)^d}{d!}\right\rceil.
\]

The argument asserts that `m≥B_d` implies `W_(d+1)>0`. Every remaining counterexample has

\[
d+2\le m<B_d,
\qquad
 a_i\le M\le
\frac{m(m-d)}2\big((d-1)(m-1)-2\big).
\tag{11}
\]

Its proof uses a quantitative continuous gap for the single-full-corner class, a phase estimate preventing very unequal weights when discrete slack is small, a count of lattice points, and a difference-set exclusion of standard discrete simplices to bound `M`. These are analytic dependencies; the old theorem does not depend on the new exhaustive four-generator certificate.

A check of its displayed rational formulas gives, for five generators (`d=4`),

\[
\delta_4=\frac3{10\,737\,418\,240\,000},\qquad
H_4=103\,089\,952\,522\,240\,000,
\]

and `B_4≈4.706×10^66`. Thus `m≥5×10^66` is a convenient weaker sufficient cutoff according to that argument. This is finite reduction, not a practical search and not a five-generator proof. No claim of novelty or external acceptance is made here. The dimension-free elementary identities in Sections 1–3 can be assessed independently of this archived theorem.

## 5. Why the existing geometric decomposition does not automatically extend

Four generators mean three exponent coordinates. In that setting, deleting the unique full-support excluded orthant leaves an ideal determined by its coordinate-plane profiles. The graph of nested coordinate levels is chordal because an induced cycle of length at least four must repeat one of only three coordinate classes. This yields a central box with at most three rectangular arms.

The mechanism already fails in four exponent coordinates. Consider

\[
U=\{0,e_1,e_2,e_3,e_4,
e_1+e_2,e_2+e_3,e_3+e_4,e_4+e_1\}.
\]

This is a lower ideal. Its minimal exclusions are the pure points `2e_i` and the pairs `e_1+e_3,e_2+e_4`; in particular it has no full-support corner. Its positive coordinate-level graph contains the induced four-cycle `1−2−3−4−1`. Hence the chordal-tree proof cannot be reused for the full four-coordinate geometric class. This example is a structural obstruction to that proof mechanism, not a numerical-semigroup counterexample.

There is an additional difficulty: in four coordinates, removing the full-support exclusion still allows genuine three-coordinate exclusions. Membership then requires three-coordinate projections, not just plane profiles. Higher-dimensional applications should preserve the arithmetic inequalities above and develop a new structural or analytic bound; directly enlarging the old box-and-arm enumeration is not justified.
