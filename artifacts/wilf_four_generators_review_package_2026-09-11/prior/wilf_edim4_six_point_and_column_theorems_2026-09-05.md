# Wilf research checkpoint: the complete six-point case and a column theorem

**Date:** 5 September 2026.  
**Continuation of:** `wilf_edim4_progress_2026-09-05.md` and `wilf_edim4_reassessment_2026-09-05.md`.

This checkpoint establishes two sufficient theorems for Wilf's inequality and an exact structural completion criterion. It does not prove or disprove the unrestricted conjecture, in embedding dimension four or in general. The six-point theorem has a finite computer-assisted part. The column theorem and the completion criterion have analytic proofs. No claim of priority or independent peer review is made.

## 1. Results and scope

Let a numerical semigroup have multiplicity \(m\), conductor \(c\), embedding dimension \(e\), and
\[
n=|S\cap[0,c)|,\qquad W_e=en-c.
\]

**Theorem A, with a computer-assisted finite part.** For a minimally four-generated numerical semigroup,
\[
\boxed{|\operatorname{Ap}(S,m)\cap[c,c+m)|\le6\quad\Longrightarrow\quad W_4\ge0.}
\]
There is no restriction on multiplicity, conductor, or generator size. This completes the six-point case left unresolved in the preceding checkpoint; the earlier condition \(m>512\) is no longer needed. Cases with at most five points were proved in the first checkpoint and have been rerun as part of the present verification.

**Theorem B, analytic.** Let \(e\ge4\), and choose a preferred Apéry factorization staircase \(T\subset\mathbb N^{e-1}\). In some coordinate direction, let \(A\) be the number of nonempty columns and let \(h\) be their minimum length. Then
\[
\boxed{2A(h-1)\ge m\quad\Longrightarrow\quad W_e\ge e-2.}
\]
In particular, for any fixed lower ideal used as a base, sufficiently many common column extensions satisfy Wilf whenever the resulting staircase has genuine Apéry labels. Neither the base nor the intermediate extensions need themselves be Apéry staircases.

**Structural criterion.** For any finite nonempty antichain \(Z\subset\mathbb N^3\), Section 3 decides exactly whether there is a finite lower ideal with at most one interior minimal excluded point in which every element of \(Z\) is maximal. This criterion depends only on the coordinate orders and equalities, so it is safe to apply before coordinate stretching. It is a necessary structural condition for Apéry realizability, not a sufficient arithmetic condition.

Together, A and B imply that a four-generated counterexample would have to satisfy
\[
|\operatorname{Ap}(S,m)\cap[c,c+m)|\ge7,
\qquad 2A_j(h_j-1)<m\quad(j=1,2,3)
\]
for every preferred staircase, where \(A_j,h_j\) refer to direction \(j\). These are restrictions on a possible counterexample, not a classification of all remaining semigroups.

## 2. Common setup and the sufficient projection estimate

### 2.1 Preferred factorizations and moments

Write
\[
S=\langle m,a_1,\ldots,a_d\rangle,\qquad d=e-1,
\]
with a minimal generating set. Choose the lexicographically least factorization of each Apéry element in the generators other than \(m\). Their exponent vectors form a finite lower ideal \(T\subset\mathbb N^d\), with \(|T|=m\). Its labels
\[
w(x)=a\cdot x
\]
represent every residue modulo \(m\) exactly once. Downward closure follows by replacing a nonpreferred divisor factorization, or by observing that a divisor whose weight minus \(m\) belongs to \(S\) would make the original weight non-Apéry. Minimal generation gives \(0,e_1,\ldots,e_d\in T\) and \(a_j\ge m+1\).

For any finite lower ideal and positive weights, put
\[
M=\max_T w(x),\qquad \Sigma=\sum_T w(x),\qquad
D_d=d|T|M-(d+1)\Sigma.
\]
Partition \(T\) into coordinate lines, with length \(L_\ell\) and top \(t_\ell\). Direct summation along each line gives
\[
\boxed{D_d=\sum_{j=1}^d\sum_{\ell\parallel e_j}
 L_\ell\bigl(M-w(t_\ell)\bigr)\ge0.} \tag{1}
\]
Indeed, the sum of \(L_\ell w(t_\ell)\) over all directions is \((d+1)\Sigma\). This is a line-sum form of the weighted lower-ideal inequality in Zhai's Lemma 3; the elementary derivation here also applies when the lower ideal is not Apéry.

For an actual Apéry staircase,
\[
M=c+m-1,\qquad g=\Sigma/m-(m-1)/2.
\]
Substituting \(n=c-g\) yields
\[
\boxed{mW_e=D_d-\frac{d-1}{2}m(m-1).} \tag{2}
\]
In particular, \(D_3\ge m(m-1)\) suffices for the four-generator case.

### 2.2 Final-window points

For the remainder of Sections 2–5 take \(d=3\). Define
\[
Z=\{x\in T:M-w(x)<m\},\qquad k=|Z|.
\]
Its labels are exactly \(\operatorname{Ap}(S,m)\cap[c,c+m)\). All its points are coordinatewise maximal in \(T\), since a successor would add a generator greater than \(m\).

Let \(\pi_j\) delete coordinate \(j\), and set
\[
B(T)=\sum_{j=1}^3|\pi_jT|,\qquad
E(Z)=\sum_{z\in Z}|z|_1-\sum_{j=1}^3\max_{z\in Z}z_j,
\]
\[
\Phi(T,Z)=B(T)-3k-E(Z).
\]
The audited estimate from the first checkpoint is
\[
\boxed{mW_4\ge m\Phi(T,Z)+E(Z).} \tag{3}
\]
Thus only \(\Phi<0\) needs further treatment. Here is a compact derivation to make the reduction explicit.

On a coordinate line, write \(M-w(t_\ell)=mq_\ell+\beta_\ell\), with \(0\le\beta_\ell<m\), and put
\[
R_A(L)=\sum_{r=0}^{L-1}[rA]_m,
\qquad C_A(L,\beta)=|\{0\le r<L:[rA]_m+\beta\ge m\}|.
\]
Line reflection and residue completeness give
\[
mW_4=\binom m2+\sum_\ell s_\ell,
\qquad s_\ell=mL_\ell q_\ell+mC_{[a_j]_m}(L_\ell,\beta_\ell)
             -R_{[a_j]_m}(L_\ell). \tag{4}
\]
For a line whose top is outside \(Z\), \(q_\ell\ge1\); its distinct axis residues include zero. Consequently
\[
R_A(L)\le(L-1)(2m-L)/2,
\qquad s_\ell\ge m+\binom L2\ge m.
\]
There are \(B(T)-3k\) such lines. For the lines topped by \(Z\), pay for one copy of every used positive axis residue out of \(\binom m2\), the sum of all nonzero residues. These axis points are distinct elements of \(T\), so their residues are distinct even across directions. The number of remaining copies is
\[
\sum_{j=1}^3\sum_{r=1}^{\max_Z z_j}
\bigl(|\{z\in Z:z_j\ge r\}|-1\bigr)=E(Z).
\]
Each costs at most \(m-1\); all omitted carry and unused-residue contributions are nonnegative. Hence
\[
mW_4\ge m(B(T)-3k)-(m-1)E(Z)=m\Phi(T,Z)+E(Z),
\]
as asserted. The first checkpoint contains the complete reflection bookkeeping behind (4).

## 3. An exact completion criterion

### 3.1 The arithmetic restriction behind the criterion

Call a minimal element of \(\mathbb N^3\setminus T\) a minimal excluded point, and call it interior if all three coordinates are positive.

Suppose that a finite lower ideal has residue-bijective labels modulo its size. If \(p\) is minimal excluded and \(q\in T\) represents its residue, then
\[
\operatorname{supp}(p)\cap\operatorname{supp}(q)=\varnothing. \tag{5}
\]
Otherwise, subtracting a shared coordinate vector gives two distinct points \(p-e_j,q-e_j\in T\) with the same residue. Similarly, two distinct minimal excluded points whose supports intersect cannot have the same residue.

An interior minimal excluded point must therefore have representative zero, and there can be at most one. This is the relevant specialization of Hellus–Rechenauer–Waldi, Proposition 2.6. The proof above shows that it uses residue bijectivity, without assuming any extra genericity of the generator weights.

### 3.2 Pairwise closure

Let \(Z\subset\mathbb N^3\) be a finite nonempty antichain and write
\[
U=\bigcup_{z\in Z}[0,z].
\]
Let \(\pi_{ij}\) retain coordinates \(i,j\), and define
\[
V=\{x\in\mathbb N^3:\pi_{ij}x\in\pi_{ij}U\text{ for all }i<j\}. \tag{6}
\]
This is a finite lower ideal containing \(U\), with the same pairwise projections. It has no interior minimal excluded point: its exclusions are generated by conditions on at most two coordinates.

More generally, any lower ideal \(T\) with at most one interior minimal excluded point is its own pairwise closure, with possibly one upper orthant \(p+\mathbb N^3\) removed. To see this, every excluded point dominates a minimal excluded point; those supported on at most two coordinates are exactly the restrictions detected by the pairwise closure. Only the possible interior point \(p\) remains.

### 3.3 Forced successors and the decision rule

For \(z\in Z\) and direction \(k\), call \((k,z)\) forced if
\[
\text{for each }j\ne k\text{ there is a }w\in Z
\text{ with }w_j\ge z_j\text{ and }w_k>z_k. \tag{7}
\]
Equivalently, \(z+e_k\in V\). The pair not involving \(k\) already belongs to \(\pi_{ij}U\); the other two pairs give exactly (7).

If there are no forced successors, \(V\) itself is the required completion. Otherwise a single interior corner \(p\) must remove every forced successor without removing its predecessor \(z\). This requires
\[
\boxed{p_k=z_k+1,\qquad p_j\le z_j\quad(j\ne k)} \tag{8}
\]
for each forced \((k,z)\).

The following rule is necessary and sufficient:

1. In each coordinate \(j\), collect the prescribed values \(z_j+1\) from forced pairs with \(k=j\). If they disagree, reject.
2. Let \(b_j\) be the minimum of \(z_j\) over forced pairs with \(k\ne j\), when such pairs exist. A prescribed value must be at most \(b_j\).
3. If coordinate \(j\) has a prescription, use it for \(p_j\). Otherwise use \(p_j=b_j\); this minimum exists because the forced set is nonempty.
4. Require all \(p_j>0\) and \(p\notin U\). If these hold, accept and use
   \[
   T^*=V\setminus(p+\mathbb N^3).
   \]

**Necessity.** Suppose an actual completion \(T\) exists. Its pairwise closure contains \(V\). Since \(Z\) must stay maximal, every forced successor is removed by its interior corner. This proves (8). The candidate constructed above is the largest coordinatewise solution of (8). It is at least the actual corner, so it cannot belong to \(U\), because the actual corner does not. All consistency and positivity requirements follow.

**Sufficiency.** The proposed \(T^*\) retains \(U\), is a finite lower ideal, and has at most one interior minimal excluded point. For each \(z\), a successor outside \(V\) is already excluded, while a successor inside \(V\) is forced and removed by (8). Thus every \(z\in Z\) is maximal in \(T^*\). This proves the criterion.

### 3.4 Why compression is safe

Every condition above depends only on equalities and strict or weak comparisons among occurring coordinate levels. In particular, an inequality \(u+1\le v\) between integer levels is equivalent to \(u<v\). The test \(p\in U\) has the same property, coordinate by coordinate.

The positivity condition is also invariant under rank compression. A bound \(z_j\) coming from a forced pair \((k,z)\), \(k\ne j\), cannot be a smallest occurring \(j\)-level. Indeed, use the witness in (7) for the third coordinate: it is greater in coordinate \(k\), at least as large in that third coordinate, and hence strictly smaller in coordinate \(j\), by the antichain property. Thus such a bound is positive after compression. Prescribed levels are positive by construction.

Consequently arbitrary strictly increasing relabelings of coordinate levels preserve feasibility. This is the justification for discarding impossible compressed seeds before stretching; an exclusion based merely on a failed modular labeling of a compressed shape would not have this justification.

Testing only the interior corners of \(U\) would also be unsafe. For example, take
\[
Z=\{(0,1,3),(0,2,2),(1,0,3),(1,2,1),(2,0,2),(3,1,0)\}.
\]
Its 25-point lower hull has two interior minimal excluded points, \((1,1,2)\) and \((2,1,1)\). Adding just \((2,1,1)\) retains every element of \(Z\) as maximal and leaves only the interior corner \((1,1,2)\). The criterion correctly accepts this 26-point completion. The supplied checker includes this example separately from the smaller reference box.

As a separate diagnostic, the criterion was checked against all 979 nonempty lower ideals in \(\{0,1,2\}^3\), of which 892 have at most one interior corner. The reference calculation exhausts possible completions in that box; no completion outside the box is needed, since the criterion constructs one within the coordinate ranges of \(Z\). All existence comparisons, explicit constructions, and 979 nonlinear coordinate-stretch checks passed. This finite check supplements, rather than replaces, the proof above.

## 4. Why six points give a finite exhaustive problem

### 4.1 The forbidden grid

For a lower ideal with at most one interior corner, put
\[
F=\{(x,y):(x,y,0)\in T\},\quad P_x=h(x,0),\quad Q_y=h(0,y).
\]
The height is \(h(x,y)=\min(P_x,Q_y)\), except that a possible interior corner \((\alpha,\beta,\gamma)\) adds the cap \(\gamma\) when \(x\ge\alpha,y\ge\beta\). This follows from the pairwise-closure description.

Six maximal points cannot have a full \(2\times3\) grid in two-coordinate projection. If they were \((x_i,y_j,z_{ij})\), with \(x_0<x_1\) and \(y_0<y_1<y_2\), the heights \(z_{ij}\) would strictly decrease along increasing rows and columns. At \((x_1,y_1)\), both \(P_{x_1}\) and \(Q_{y_1}\) are strictly greater than \(z_{11}+1\), so the unique cap would have to equal \(z_{11}+1\). The same argument at \((x_1,y_2)\) would make it equal \(z_{12}+1\), a contradiction.

This obstruction depends only on coordinate levels and survives stretching. The completion criterion is stronger, but this short grid lemma supplies the strict growth needed below.

### 4.2 Strict growth under insertion

Write \(\Phi_0(Z)=\Phi(U(Z),Z)\). Insert a coordinate level in direction \(i\): raise by one every point of \(H=\{z:z_i\ge r\}\), where \(r\) is an occurring level. Let \(b=|H|\), and let \(p,q\) be the other-coordinate maxima on \(H\). Counting the two growing projections gives
\[
\Delta B=p+q+2,\qquad \Delta E=b-1,
\qquad \boxed{\Delta\Phi_0=p+q+3-b.} \tag{9}
\]
An antichain has injective projection on any pair of coordinates, so \(b\le(p+1)(q+1)\). For \(b\le5\), (9) is positive. For \(b=6\), a nonpositive value is possible only when \((p,q)=(1,2)\) or \((2,1)\); the six projected points would then fill the forbidden grid. Thus all insertions relevant to a feasible six-point set increase \(\Phi_0\) by at least one.

Compress each coordinate to consecutive ranks beginning at zero. Every original antichain is recovered by level insertions, including translations below the smallest level. If its final score is negative, all intermediate scores are negative. Therefore it suffices to enumerate all compressed negative feasible seeds, then every insertion that keeps the score negative. Strict increase proves termination, independently of any computational cutoff.

### 4.3 Exhausting staircase extensions

For each resulting \(Z\), enumerate every lower ideal extending \(U(Z)\), retaining \(Z\) as maximal, and having \(\Phi(T,Z)<0\). Add one point at a time when its predecessors are already present and it does not dominate any \(z\in Z\). Along a path to a negative final ideal, all intermediate scores remain negative, since projections only increase.

There are finitely many extensions: \(B(T)<18+E(Z)\) bounds projection sizes and consequently all coordinate extents. The implementation does not prune intermediate shapes by their number of interior corners; later additions could remove corners. It applies that necessary condition only to the resulting candidates.

Finally retain the three axis unit vectors and at most one interior corner, and identify simultaneous coordinate permutations of \((T,Z)\). This is a finite classification of every possible failure of (3) with \(|Z|=6\), not a bounded-generator search.

## 5. The complete finite certification

### 5.1 Enumeration ledger

All combinatorial generation, score calculations, residue tests, and modular checks use exact integer arithmetic.

| Stage | Count |
| --- | ---: |
| Compressed six-point antichains, up to coordinate permutations | 345,988 |
| Negative compressed antichains | 2,264 |
| Negative compressed antichains passing the completion criterion | 891 |
| All negative antichains after permitted insertions | 4,406 |
| All negative staircase extensions, before structural filtering | 11,790 |
| Extensions retaining axes and at most one interior corner, before symmetry identification | 6,019 |
| Distinct retained \((T,Z)\) pairs | 5,962 |
| Distinct retained staircases \(T\) | 5,331 |
| Staircases admitting at least one residue-bijective labeling | 71 |
| Ordered residue labelings on those staircases | 930 |
| Labeling/cut checks | 23,002 |

The completion criterion rejects 1,182 seeds for inconsistent prescribed heights, 115 for incompatible corner coordinates, and 76 because the corner would remove a point of \(Z\). The minimum score among the 891 survivors is \(-6\), so at most five insertions can occur along a negative expansion path from these seeds.

The largest raw extension has 57 points. The largest retained staircase has **56** points. These are outputs of the exhaustive reduction, not imposed search cutoffs. The residue checker supports up to 64 points and asserts this precondition; all retained candidates are within its supported range.

For each \(T\), with \(m=|T|\), enumerate every ordered triple of distinct nonzero residues \(A_1,A_2,A_3\pmod m\). Retain a triple exactly when \(x\mapsto A\cdot x\pmod m\) is bijective on \(T\). Every genuine staircase is covered, because \(0,e_1,e_2,e_3\in T\). Residue bijectivity alone is not claimed to imply that a staircase has genuine Apéry weights; retaining this larger class is harmless for a sufficient proof.

### 5.2 First certificate: every modular cut

For each retained labeling and every \(f\in\{0,\ldots,m-1\}\), compute
\[
\mathcal R_f(T,A)=\sum_{j,\ell\parallel e_j}
 L_\ell[f-A\cdot t_\ell]_m.
\]
The exact check gives
\[
\mathcal R_f(T,A)\ge m(m-1)
\]
in all 23,002 cases; the minimum slack is zero.

For actual generator weights, choose \(f=[M]_m\). Each nonnegative integer \(M-w(t_\ell)\) is at least its least residue \([f-A\cdot t_\ell]_m\). Equations (1) and (2) therefore give
\[
D_3\ge\mathcal R_f(T,A)\ge m(m-1),\qquad W_4\ge0.
\]
This proves the required finite part for every possible integer lift of every surviving residue labeling. No upper bound on the weights is involved.

### 5.3 Second certificate: global moments with exact dual witnesses

A separate calculation verifies each of the 71 shapes directly with global moment inequalities. Put \(s_j=\sum_{x\in T}x_j\) and consider
\[
\eta(T)=\min\{3mM-4u\cdot s:u_j\ge1,\ M\ge u\cdot x\ (x\in T)\}.
\]
Since actual \(a_j\ge m+1\), positive homogeneity gives \(D_3\ge(m+1)\eta(T)\). On 67 shapes this already exceeds or equals \(m(m-1)\).

For the other four shapes, use the integer spacing of distinct generators. After sorting weights, impose
\[
a_1\ge m+1,\qquad a_2-a_1\ge1,\qquad a_3-a_2\ge1,
\qquad M\ge a\cdot x.
\]
Check all six coordinate permutations of each shape. All 24 exact bounds pass:

| Shape index in the stored list | \(m\) | Normalized \(\eta\) | Six ordered margins \(D_{\min}-m(m-1)\) |
| ---: | ---: | ---: | --- |
| 5244 | 15 | 11 | 84, 100, 96, 79, 128, 50 |
| 5245 | 16 | 8 | 32, 48, 32, 48, 64, 64 |
| 5258 | 13 | 9 | 188, 192, 212, 19, 220, 23 |
| 5300 | 15 | 11 | 112, 63, 116, 116, 63, 112 |

For example, shape 5245 has maximal points
\[
(0,0,3),(0,1,2),(0,2,1),(0,3,0),(1,0,2),(2,0,1),(3,0,0).
\]
In the coordinate order \(a_1<a_2<a_3\), its certificate is the exact identity
\[
D_3=8a_1+48(a_2-a_1)+88(a_3-a_2)+48(M-3a_3).
\]
Every term has a known nonnegative lower bound, so \(D_3\ge8\cdot17+48+88=272>240\). The other coordinate orders are checked separately as recorded in the table.

SciPy is used only to propose primal and dual solutions. The stored certificates use rational numbers. A separate checker verifies that every dual row is one of the actual shape inequalities, every dual coefficient is nonnegative, their sum is exactly the objective, and the claimed lower bound is exact. It also checks a feasible primal point with matching objective. The checker uses only the Python standard library and does not invoke a numerical optimizer.

The modular and moment certificates each suffice for the surviving six-point shapes. The second mechanism confirms that the result is not an artifact of selecting a favorable modular cut.

### 5.4 Reproduction

`run_six_point_verification.py` regenerates the compressed seeds, all expansions and extensions, every residue labeling, and both certificate sets. It also reruns the complete earlier \(k\le5\) verifier, the independent bounded completion check, and the column diagnostics. The complete run passed in about 48 seconds in the recorded environment: Python 3.12.13, SciPy 1.17.0, and a C++17 compiler.

The finite generation and the proofs of completeness in Sections 3–4 together establish Theorem A. Neither a list of successful semigroup examples nor the LP discovery software alone would establish it.

## 6. The column theorem in every embedding dimension at least four

This section is an analytic proof and uses neither the six-point enumeration nor the one-interior-corner restriction.

### 6.1 Removing a common bottom thickness

Let \(d=e-1\ge3\), and select a coordinate direction of \(T\). Write its generator weight as \(b\). Let \(F\subset\mathbb N^{d-1}\) be the projection in that direction and \(A=|F|\). Let \(h\) be the shortest column length and put
\[
t=h-1.
\]
Shorten every column by \(t\) to form \(T_0\). Every column stays nonempty, and \(T_0\) is a lower ideal. Put
\[
m_0=|T_0|,\qquad s=m_0/A\ge1,\qquad m=m_0+At=A(s+t).
\]
The hypothesis \(2A(h-1)\ge m\) is exactly \(t\ge s\).

Use the original weights of \(T\) on \(T_0\); do not presume that \(T_0\) represents a numerical semigroup. Write \(M_0,\Sigma_0,D_0\) for its moments. For \(u\in F\), let \(v(u)\) be the weight using the other \(d-1\) coordinates, and set
\[
S_F=\sum_{u\in F}v(u),\qquad M_F=\max_F v(u).
\]
The exact elongation formulas are
\[
M=M_0+bt,
\]
\[
\Sigma=\Sigma_0+b t m_0+tS_F+\frac12 bA t(t-1). \tag{10}
\]
Each column's top increases by \(bt\), and summing the \(t\) added points gives the second equality.

Substitution into \(D_d=dmM-(d+1)\Sigma\) yields
\[
\begin{aligned}
D_d={}&D_0+t\left[dAM_0-bm_0-(d+1)S_F
                     +\frac{d+1}{2}Ab\right]\\
&+\frac{d-1}{2}Abt^2. \tag{11}
\end{aligned}
\]

### 6.2 A lower bound for the elongation surplus

Equation (1) gives \(D_0\ge0\). Applying its \((d-1)\)-dimensional version to \(F\) gives
\[
dS_F\le(d-1)AM_F\le(d-1)AM_0.
\]
Consequently
\[
dAM_0-(d+1)S_F\ge AM_0/d\ge0.
\]
Drop these nonnegative contributions in (11) to obtain
\[
\boxed{D_d\ge Ab\left[\frac{d-1}{2}t^2
                      +\frac{d+1}{2}t-st\right].} \tag{12}
\]
For \(d\ge3\) and \(t\ge s\ge1\), the bracket is at least \(\frac{d-1}{2}(s+t)\). The exact factorization proving this is
\[
\begin{aligned}
&(d-1)t^2-2st+2t-(d-1)s\\
&\quad=(t-s)\bigl((d-1)t+(d-3)s+2\bigr)
          +(d-3)s(s-1)\ge0. \tag{13}
\end{aligned}
\]
Since \(A(s+t)=m\) and \(b\ge m+1\), (12) now gives
\[
D_d\ge\frac{d-1}{2}bm
       \ge\frac{d-1}{2}m(m+1).
\]
Subtracting the Apéry correction in (2) proves
\[
\boxed{W_e\ge d-1=e-2.}
\]
This proves Theorem B.

For \(e=4\), the decisive comparison is especially simple:
\[
D_3\ge Ab(t^2+2t-st),\qquad
t^2+2t-st-(s+t)=(t+1)(t-s)\ge0.
\]
Thus \(D_3\ge bm\ge m(m+1)\), leaving a Wilf margin of at least two.

### 6.3 The fixed-base consequence and examples

Start with any fixed finite lower ideal \(T_0\), of size \(m_0\), with \(A\) nonempty columns in a chosen direction. Add \(t\) points to every column. The argument above applies directly whenever
\[
t\ge\left\lceil\frac{m_0}{A}\right\rceil.
\]
If the resulting staircase is an Apéry staircase in embedding dimension \(e\ge4\), it satisfies \(W_e\ge e-2\), for every genuine choice of its weights. Common elongation of a fixed base is therefore not an unbounded source of counterexamples.

This statement does not cover all insertions on proper subsets of the columns, or sequences in which the base grows together with the common thickness.

Exact examples checked in the supplied code include:

| Generators | Direction weight | Column count \(A\) | Column lengths | \(c\) | \(W_e\) |
| --- | ---: | ---: | --- | ---: | ---: |
| \(8,12,18,27\) | 12 | 4 | all 2 | 50 | 50 |
| \(28,31,42,49\) | 31 | 4 | all 7 | 250 | 250 |
| \(126,127,2569,3615\) | 127 | 3 | 38, 39, 49 | 8,316 | 7,060 |

The third example illustrates that equal column lengths are not required. These examples are illustrations, not claims of previously unknown Wilf classes. The code also checks binary-cube Apéry examples in embedding dimensions 5–8, and 90 seeded exact elongation identities in dimensions 3–5. Those finite calculations are diagnostics; the proof is (10)–(13).

## 7. What the progress changes

The six-point obstruction has been removed completely. The useful change from the original relaxed-shape approach is that arithmetic realizability first restricts the allowable boundary. That restriction supplies an order-invariant completion test, which makes finite compression safe, and the remaining shapes then admit exact global certificates.

For larger final-window sets, a universal finite classification has not been established. In particular, the present work does not claim that every insertion still raises \(\Phi\) for seven or more points. The column theorem handles a specific unbounded operation analytically, without requiring a finite list of its integer lengths, but does not remove every possible neutral or negative insertion.

The next unresolved task is consequently precise: understand genuine residue-bijective staircases with at least seven final-window points that have a short column in every direction, while retaining the sparse reduction relations at their minimal excluded points. Enlarging the six-point enumeration by itself is not a proof of that remaining statement.

## 8. Primary references and relation to the checkpoints

- A. Zhai, *An asymptotic result concerning a question of Wilf*, especially Lemma 3: [arXiv:1111.2779](https://arxiv.org/pdf/1111.2779). This supplies the established weighted lower-ideal background; equation (1) re-derives the inequality in the form needed here.
- M. Hellus, A. Rechenauer, R. Waldi, *Variants on a question of Wilf*, especially Proposition 2.6: [arXiv:1804.06141](https://arxiv.org/pdf/1804.06141). This supplies the established restriction on full-support minimal excluded points; Section 3.1 includes the short residue proof.
- `wilf_edim4_progress_2026-09-05.md`: the complete reflection bookkeeping and the earlier \(|Z|\le5\) proof. Included unchanged in the verification package as a historical dependency.
- `wilf_edim4_reassessment_2026-09-05.md`: the prior boundary and height reduction, grid exclusion, coarse six-point multiplicity bound, and targeted literature assessment. Its statement that the six-point case remained unfinished is superseded by Theorem A above.

The analytic arguments and finite certificates in this checkpoint are fully stated for review. Establishing whether these particular formulations extend the published literature would require a separate priority analysis.
