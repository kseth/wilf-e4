# D2: no-corner simplification decision

**Status date:** 2026-09-14

## Decision

Retain the exact B2 interval tree and horn dynamic program specified in
[`no-corner-interval-specification.md`](../paper/no-corner-interval-specification.md).
No direct discrete horn inequality has been proved that covers the remaining
compact parameter region.

The continuous no-corner theorem remains a substantial analytic reduction:
it proves every analytic leaf and is essential to compactness. It does not,
however, control the lattice correction strongly enough to prove the discrete
target throughout the complementary region. The natural ways to remove the
remaining computation encounter exact obstructions described below.

This is a bounded research decision, not a claim that an analytic proof is
impossible. It fixes the present proof architecture so that R2 can audit and
freshly replay one finite object instead of leaving B2 conditional on further
open-ended simplification.

## 1. The replacement that would be needed

For

\[
\mathcal P=\{(b,c,H):1\le b\le c\le H,\ 5\le H\le24\},
\]

put \(w=(1,b,c)\). For a nonempty finite lower ideal \(T\) with no
full-support minimal exclusion and \(w\cdot x\le H\), B2.2 asks for

\[
\sum_{x\in T}\bigl(4w\cdot x-3H+1\bigr)\le1.
\tag{1}
\]

A direct replacement must prove (1) uniformly for every real parameter in
\(\mathcal P\), or prove the original B2 branch statement using its extra
hypotheses \(m\ge30\), coordinate units, and attained height. A successful
horn-potential proof would need an explicit upper bound for every nested
rectangle sequence and a joint inequality absorbing three such bounds into
the central-box deficit. No such discrete joint potential is presently
proved.

## 2. What the analytic argument already removes

Write \(B=1+b+c\) and

\[
D_H=3|T|H-4w\cdot\sum_{x\in T}x.
\]

The B2.1 continuous theorem and exact rectangular thickening give

\[
\frac{D_H}{|T|}\ge\frac{H-2B}{3}.
\tag{2}
\]

Consequently

\[
H\ge2B+3
\quad\Longrightarrow\quad
|T|-D_H\le0,
\tag{3}
\]

which is stronger than (1). Together with the phase inequality, this reduces
every possible branch failure to the compact region used by B2.2. Thus the
interval computation is not standing in for the continuous proof; it covers
only the lattice-sensitive remainder left after that proof.

There is also a direct analytic subcase. If the graph of pair-supported
minimal exclusions is bipartite, simultaneous coordinate-top moves in its
two color classes give

\[
\frac1{|T|}\sum_{x\in T}w\cdot x\le\frac{2H}{3}.
\]

For the genuine B2 branch, \(|T|\ge30\) and \(H\ge5\), so this already gives
\(D_H\ge |T|H/3>|T|-1\). The unresolved interaction graph is the triangle.
Encoding that distinction in the finite optimization would require tracking
all three kinds of pair corner and would not eliminate the triangle case, so
the retained checker continues to certify the cleaner geometric superset. A
proof of the simultaneous-top bound is recorded in the frozen historical
[`clique-tree and bipartite note`](../artifacts/wilf_four_generators_review_package_2026-09-11/round3/no_interior/clique_tree_and_bipartite_bound.md).

## 3. Exact obstructions to the natural shortcuts

### 3.1 Rectangular thickening has an essential lattice correction

For \(R\ge1\), consider

\[
T_R=\{(x,y,z)\in\mathbb N^3:
x+y\le R,\ x+z\le R,\ yz=0\}.
\tag{4}
\]

This is a no-full-support-corner ideal: it is the union of two planar
degree-\(R\) triangles along their common axis. With unit weights,

\[
|T_R|=(R+1)^2,
\qquad
\sum_{x\in T_R}|x|_1
=\frac{R(R+1)(4R+5)}6.
\]

Hence

\[
3\sum_{x\in T_R}|x|_1-2|T_R|R
=\frac{R(R+1)}2.
\tag{5}
\]

The discrete mean therefore exceeds \(2R/3\), and the excess in (5) is not
bounded by one copy of the maximum height. The continuous \(2/3\)-centroid
theorem cannot be transferred by deleting, or by replacing with a fixed
endpoint constant, the correction introduced by unit-cell thickening. The
family does satisfy the B2 target; it is an obstruction to this proof
shortcut, not a counterexample.

### 3.2 Equal weights are not extremal

Let \(T\) be the union of the anchored boxes with maximal points

\[
(6,1,1),\qquad(1,5,1),\qquad(1,1,4).
\tag{6}
\]

Its six minimal exclusions all have support at most two,
\(|T|=56\), and its coordinate sums are \((98,76,58)\). Over ordered
normalized weights its defect is uniquely minimized at

\[
(1,b,c)=\left(1,\frac54,\frac53\right),
\qquad D=\frac{1018}{3},
\tag{7}
\]

where the three displayed maxima are exposed and tied. Unit weights instead
give \(D=416\). Thus neither symmetry nor monotonic deformation to equal
weights controls the arbitrary-weight problem. A direct argument must allow
vertices determined by three unequal exposed maxima.

### 3.3 Full transverse caps do not maximize an early horn

Even before discretization, an early horn can improve by discarding part of a
transverse cap. At

\[
(a,B,C)=\left(\frac1{20},\frac3{20},\frac45\right),
\]

the best boundary profile using the original caps has contribution
\(-1/4800\), while using the effective cap
\((x,y)=(1/20,4/5)\) with an initial constant slab gives

\[
\frac{613}{1{,}920{,}000}>0.
\tag{8}
\]

B2.1 resolves this phenomenon continuously by optimizing the effective caps
and then proving a joint three-horn inequality. It rules out a shorter proof
that evaluates only the central caps. A discrete replacement would likewise
have to retain effective-cap optimization.

## 4. Why endpoint convexity does not close the discrete problem

There is a valid partial reduction. Fix the sequence of transverse rectangles
in one discrete horn and vary only the outward endpoints of its constant
plateaus. After collecting terms, the coefficient of each endpoint square is
a nonnegative multiple of the drop in rectangle area. The additive score is
therefore convex in those endpoints. A maximum occurs when adjacent
plateaus coalesce or a plateau reaches its last feasible lattice level.

For a state with transverse caps \((r,s)\) in outward direction \(i\), that
last level is

\[
\left\lfloor
\frac{H-w_jr-w_ks}{w_i}
\right\rfloor.
\tag{9}
\]

Unlike the continuous boundary relation, (9) changes across every relevant
lattice hyperplane. The effective caps remain free and nested, the three
weights are genuinely unequal, and the three horns must be controlled
jointly. In the compact region every feasible point has total degree at most
24, so this is a finite arrangement, but resolving its floor regimes is
precisely a finite case analysis. The B2.2 recurrence is the concise exact
form of that analysis.

Exploratory exact grids suggest that the true geometric inequality may have
more margin than (1). That observation does not provide a Bellman
supersolution, a joint discrete potential, or coverage between grid points,
and is not retained as a theorem or verification result.

## 5. Why the extra branch hypotheses are not added to the computation

The finite obligation deliberately drops \(m\ge30\), the three coordinate
units, attained height, residue labels, and the published consequence
\(|\operatorname{Max}(T)|\ge4\). Restoring them does not currently yield a
complete analytic proof. It would instead require a more complicated dynamic
program that tracks cardinality, unit occupancy, exact attainment, maximal
points, or arithmetic labels.

Those predicates are unnecessary for the existing upper-bound recurrence.
They would enlarge the theorem-to-code interface while leaving a finite
triangle-interaction case. The clean choice is to certify the stronger
geometric superset already stated in B2.2.

## 6. Retained R2 interface

D2 fixes the following handoff.

1. Promote the archived interval tree only after validating its schema and
   immutable hash; the discovery producer remains outside the proof boundary.
2. Build a compact exact checker that reconstructs every child box, verifies
   complete closed coverage, and recomputes every leaf with the prefix horn
   recurrence.
3. Build a materially separate path whose coverage walk is independent and
   whose horn values use the direct rectangle recurrence rather than prefix
   maxima.
4. Run both paths over every reachable node and every DP leaf, fail closed,
   and record the commands, source and certificate hashes, environment,
   arithmetic bounds, and exact counts required by V0.
5. Do not retain the producer, sampling modes, redundant degree-four checks,
   or historical success records in the final proof package.

The target remains exactly B2.2-FV. Historical node counts and stronger
diagnostic margins are not acceptance conditions.

## 7. Gate closure

D2 is closed with the fallback route:

- retain the analytic and compactness results of B2.1;
- retain the exact B2.2 interval-tree contract unchanged;
- proceed to the complete and independent R2 replays;
- keep bipartite, low-type, and other free filters as explanatory subcases,
  not executable certificate predicates; and
- revisit the decision only if a proved discrete joint horn potential removes
  the entire residual parameter region.

The exact examples in Section 3 are documented in the frozen historical
notes
[`conditional_discrete_bridge.md`](../artifacts/wilf_four_generators_review_package_2026-09-11/round4/discrete/conditional_discrete_bridge.md),
[`unequal_exposed_vertex.md`](../artifacts/wilf_four_generators_review_package_2026-09-11/round4/discrete_horns/unequal_exposed_vertex.md),
and
[`late_horn_potential.md`](../artifacts/wilf_four_generators_review_package_2026-09-11/round3/descent/late_horn_potential.md).
