# Two explicit centroid constructions and analytic families

11 September 2026. Supplement to the proposed four-generator Wilf proof.

## 1. Outcome and scope

The residual centroid argument can be substantially simplified:

- No stored linear-programming bases, determinants, or per-shape rational certificates are needed.
- Two explicit constructions suffice: local moves of at most two coordinate steps, and a convex combination of axis endpoints.
- The bound improves from \(D_0\ge m-29/10\) to **\(D_0\ge m\)**.
- The erosion restriction and the refined dominating-plane-corner restriction can both be removed from this lemma.
- The resulting larger class contains **5,574,644** enumerated shapes. Separate implementations completed exact checks on every shape and agreed on all nine coverage totals.

The convex-geometric constructions below are proved analytically for arbitrary finite lower ideals. The assertion that one of them always supplies enough surplus in the stated residual class is still established by finite enumeration. This is not yet a proof without computation.

There are also direct analytic proofs for unbounded families of corner-clipped boxes and prisms with arbitrary planar staircase bases. Those family proofs use no enumeration or Apéry arithmetic.

These are research results within the proposed manuscript. External mathematical review and proof-assistant formalization remain outstanding. No novelty claim relative to known special families of numerical semigroups is made.

A second completed route, described in Section 9, eliminates enumeration of
individual ideals in the centroid component. It verifies 44,281 universal
parameter certificates instead and uses the existing high-height theorem.
The two routes are alternatives with different strengths and dependencies.

## 2. The centroid target

For a finite lower ideal \(T\subset\mathbb N^3\), write
\[
m=|T|,\qquad s=\sum_{x\in T}x.
\]
A point \(z\in\operatorname{conv}(T)\) with
\[
r=3mz-4s\ge0\quad\text{coordinatewise},\qquad
\sum_i r_i\ge m
\tag{1}
\]
proves the desired inequality for every real vector \(b_i\ge1\). Indeed, with
\(H=\max_{x\in T}b\cdot x\),
\[
3mH-4b\cdot s
\ge b\cdot(3mz-4s)
\ge\sum_i r_i
\ge m.
\tag{2}
\]
The first step is convexity and the second is coordinatewise nonnegativity.
No height cutoff or relation between the weights is used.

## 3. First construction: local moves from coordinate-line tops

For each nonempty coordinate line \(\ell\) of \(T\), let \(L_\ell\) be its
number of points and \(t_\ell\) its top endpoint. Include lines in all three
directions. Since every such line is an initial interval,
\[
\sum_\ell L_\ell=3m,\qquad
\sum_\ell L_\ell t_\ell=4s.
\tag{3}
\]
For the second identity, fix a coordinate \(i\). Lines parallel to \(i\)
contribute \(2s_i\); lines in each of the other two directions contribute
\(s_i\). This proves (3) coordinate by coordinate.

For any \(t\in T\), define
\[
h_2(t)=
\max\{\,|u-t|_1:\ u\in T,\ u\ge t,\ |u-t|_1\le2\,\}.
\]
The value is \(0\), \(1\), or \(2\). It requires only local membership tests.
For every line top choose an admissible \(u_\ell\) attaining this value, and put
\[
z_{\rm local}=\frac1{3m}\sum_\ell L_\ell u_\ell,\qquad
U_2(T)=\sum_\ell L_\ell h_2(t_\ell).
\]
Equation (3) gives
\[
3mz_{\rm local}-4s
=\sum_\ell L_\ell(u_\ell-t_\ell)\ge0,\qquad
\sum_i(3mz_{\rm local}-4s)_i=U_2(T).
\tag{4}
\]
Thus \(U_2(T)\ge m\) supplies the required witness.

This construction needs neither a search for a farthest maximal point nor a
linear program. A fixed rule can break ties between equally good local moves.

For comparison, allowing arbitrary-length monotone moves gives
\[
U(T)=\sum_\ell L_\ell
\left(\max_{u\in T,\ u\ge t_\ell}|u|_1-|t_\ell|_1\right)\ge U_2(T).
\]
The earlier experiments used \(U\); the final simplified theorem uses \(U_2\).
The even cheaper one-step gain is
\[
U_1(T)=3m-\sum_{u\in\operatorname{Max}(T)}(|u|_1+3),
\]
obtained by moving every nonmaximal line top once. One step does not suffice
for the final alternative, so the two-step allowance is material.

## 4. Second construction: the axis simplex

Let
\[
q_i=\max_{x\in T}x_i>0,\qquad q_*=\max_i q_i,\qquad
G(T)=q_*\left(3m-4\sum_i\frac{s_i}{q_i}\right).
\tag{5}
\]
If \(G(T)\ge m\), choose an index \(j\) with \(q_j=q_*\) and define
\[
\lambda_i=\frac{4s_i}{3mq_i},\qquad
\delta=1-\sum_i\lambda_i.
\]
The positive lower bound on \(G\) implies \(\delta>0\). Each axis endpoint
\(q_i e_i\) belongs to \(T\), and
\[
z_{\rm axis}=\sum_i\lambda_iq_i e_i+\delta q_j e_j
\]
is a convex combination of those endpoints. Its residual is exactly
\[
3mz_{\rm axis}-4s=G(T)e_j.
\tag{6}
\]
Hence it also proves (1).

Both constructions are valid for any finite lower ideal with positive axis
lengths. Only the assertion that at least one reaches the target needs the
additional structural hypotheses below.

## 5. The simplified finite theorem

Let \(T\subset\Delta_6=\{x\in\mathbb N^3:|x|_1\le6\}\) be a lower ideal,
with \(m\ge30\), exactly one full-support minimal excluded point \(p\), and
\(5\le|p|_1\le7\). Assume only these two additional restrictions:

1. Each coordinate-plane projection has at most \(|p|_1-2\) mixed minimal
   excluded points.
2. For \(F_i=\{x\in T:x+e_i\notin T\}\) and \(n_k=1+\max_Tx_k\),
   \[
   |F_i\cap F_j|\le2n_k
   \quad(\{i,j,k\}=\{1,2,3\}).
   \]

The completed exact verification establishes
\[
\boxed{\max\{U_2(T),G(T)\}\ge m.}
\tag{7}
\]
Equations (4) and (6) then give the centroid witness (1).

The previous erosion test and the bound on plane corners dominating the
projection of \(p\) are absent from this theorem's hypotheses. The total
mixed-corner bound remains. Although its earlier proof used a refined
counting argument, that refined condition is no longer part of the finite
enumeration or centroid lemma.

The local construction alone reaches \(m\) on **5,574,213** shapes; the axis
construction handles the remaining **431**. The two constructions can both
succeed on the same shape, so their separate success counts should not be
added. All 431 fallback witnesses have been reconstructed explicitly.

### Finite coverage

After sorting the coordinates of \(p\), the larger class has these counts:

| Corner | Shapes checked |
|---|---:|
| \((1,1,3)\) | 1,581,961 |
| \((1,2,2)\) | 1,433,543 |
| \((1,1,4)\) | 874,540 |
| \((1,2,3)\) | 638,574 |
| \((2,2,2)\) | 592,453 |
| \((1,1,5)\) | 159,580 |
| \((1,2,4)\) | 105,119 |
| \((1,3,3)\) | 94,500 |
| \((2,2,3)\) | 94,374 |
| **Total** | **5,574,644** |

The class is larger than the previous 3,742,041-shape class because two
filters have been removed. The improvement is in the hypotheses, proof
construction, and verification burden, not a reduction in this shape count.

The verifier enumerates compatible planar lower profiles, removes the upper
orthant of \(p\), checks the stated restrictions, and evaluates (7) with integer
arithmetic. Rational axis expressions are cleared by a positive common
denominator. It reads no per-shape certificate stream.

The separate implementations construct the shapes using bitsets and literal
column heights, respectively. Their complete counts agree. The independent
local verifier computes \(h_2\) by membership tests rather than importing a
producer's dynamic program or geometric data.

### A shorter Wilf deduction

For a genuine minimally four-generated semigroup,
\[
A=\min(a_1,a_2,a_3)\ge m+1,\quad b=a/A,\quad
D_0=3mH-4b\cdot s.
\]
The exact Apéry identity is
\[
mW_4=AD_0-m(m-1).
\]
Using \(D_0\ge m\) gives
\[
mW_4\ge m(A-m+1)\ge2m,
\qquad\boxed{W_4\ge2.}
\tag{8}
\]
Thus the earlier comparison of \(90/31\) with \(29/10\) is unnecessary for
this residual low-degree class.

The earlier small-multiplicity, no-full-corner, exceptional-corner, and
high-height arguments remain dependencies of the global four-generator proof.
This supplement simplifies its centroid part.

## 6. Direct proofs for unbounded families

### Corner-clipped boxes

Let \(1\le p_i<n_i\) and
\[
T=\prod_i\{0,\ldots,n_i-1\}\setminus(p+\mathbb N^3),\qquad
Q=\prod_i(n_i-p_i),\qquad m=\prod_i n_i-Q.
\]
Let \(v^{(i)}\) be the box's top vertex with coordinate \(i\) replaced by
\(p_i-1\), and set \(z=(v^{(1)}+v^{(2)}+v^{(3)})/3\).
All three vertices belong to \(T\). Direct summation gives
\[
2s_i=m(n_i-1)-Qp_i,\qquad
(3mz-4s)_i=m(p_i-1)+2Qp_i.
\]
Therefore
\[
\sum_i(3mz-4s)_i=m(|p|_1-3)+2Q|p|_1\ge m
\]
whenever \(|p|_1\ge4\). This includes every residual corner considered here,
with no degree, size, or arithmetic restriction.

For \(p=(1,1,1)\), the same construction gives surplus \(6Q\ge m-1\).
Writing \(q_i=n_i-1\ge1\), the latter inequality follows from
\[
m=q_1q_2+q_1q_3+q_2q_3+q_1+q_2+q_3+1\le6Q+1.
\]

### Clipped prisms with arbitrary planar staircases

Let \(P\subset\mathbb N^2\) be any finite lower ideal containing \((a,b)\),
with \(a,b\ge1\). For integers \(n>h\ge3\), put
\[
L=P\setminus((a,b)+\mathbb N^2),\quad
u=|P|,\ v=|L|,\ q=n-h,\ m=hu+qv,
\]
\[
T=(P\times\{0,\ldots,n-1\})\setminus((a,b,h)+\mathbb N^3).
\]
In two dimensions the line-top identity supplies
\[
z_P=\frac{3s(P)}{2u}\in\operatorname{conv}(P),\qquad
z_L=\frac{3s(L)}{2v}\in\operatorname{conv}(L).
\]
Combine \((z_P,h-1)\), \((z_L,n-1)\), and \((a,b-1,n-1)\) with weights
\[
\frac{8hu}{9m},\quad\frac{8qv}{9m},\quad\frac19.
\]
The residual of this explicit witness is
\[
r=\frac13\big(ma,\ m(b-1),\ B\big),\quad
B=hu(n+2h-3)+3qv(n-2h-1).
\]
As a function of \(v/u\in[0,1]\), the ratio \(B/m\) lies between
\[
n+2h-3,\qquad 3n-8h-3+\frac{8h^2}{n}.
\]
Both are at least \(2\) for \(h\ge3\). For the second, multiply its
difference from \(2\) by \(n\): the resulting quadratic
\[
3n^2-(8h+5)n+8h^2
\]
has positive leading coefficient and discriminant
\(-32h^2+80h+25<0\). Hence \(r\ge0\) and
\[
\sum_i r_i\ge\frac{m(a+b-1)+2m}{3}\ge m.
\]
This is a direct proof for arbitrary planar staircase complexity. Coordinate
permutations are allowed. Additional cases with \(h=1,2\), and a
higher-dimensional clipped-box formula, are proved in the accompanying
analytic-family note.

## 7. What is still missing from an analytic replacement

The remaining finite obligation is now exactly (7), rather than the
existence of thousands of unrelated rational bases:

> Prove that the stated corner and surface restrictions force
> \(\max\{U_2(T),G(T)\}\ge|T|\), without listing every eligible ideal.

The two constructions themselves are already proved. The box and prism
arguments establish that implication on unbounded structural subclasses.
They do not exhaust general ideals with varying restrictions in all three
coordinate planes.

Some tempting shortcuts fail:

- The first construction alone fails on eligible shapes. A second witness
  really is needed by this method.
- One-step moves plus the axis construction do not cover every shape.
- Removing all mixed-plane-corner restrictions permits shapes for which
  even arbitrary-length monotone moves and the axis construction fall below
  \(m-29/10\).

The last failure is a counterexample to the proposed two-construction
criterion, not a counterexample to the centroid inequality or to Wilf.
Exact fixtures are included so those distinctions can be checked.

## 8. Reproduction and dependencies

The primary local construction and its portable verifier are in
round10/local_centroid. The independent audit is in round10/independent;
filter-removal results and failed extensions are in round10/ablation.
The full symbolic family proofs and exact bounded identity checks are in
round10/symbolic.

The bounded identity checks are ancillary: the displayed algebra proves the
infinite-family statements. The finite theorem (7), by contrast, still
depends on the complete enumeration. The archive distinguishes these two
kinds of evidence.

The weighted-lower-ideal approach has established antecedents; see
[Hellus, Rechenauer and Waldi, “Variants on a question of Wilf”](https://arxiv.org/abs/1804.06141)
and [Zhai, “An asymptotic result concerning a question of Wilf”](https://arxiv.org/abs/1111.2779).
The particular constructions, bounds, and verification results reported here
are assessed through the accompanying proofs and files.

## 9. A second completed route: no enumeration of individual ideals

A separate argument developed during this investigation removes the
individual-ideal enumeration from the centroid proof. It uses universal
indicator inequalities and retains finite verification over weight and height
parameters. This route retains the original erosion and refined plane-corner
restrictions, and concludes \(D_0\ge m-29/10\); it should not be confused with
the stronger, more explicit local-construction theorem above.

For a fixed ideal, minimize
\[
3mH-4b\cdot s
\quad\text{subject to }b_i\ge1,\ H\ge b\cdot x\ (x\in T).
\]
The coordinate-line identity bounds the objective below by zero. A finite
minimum is attained at a vertex. Each vertex is determined by three point
equalities and one lower-weight equality, two of each, or one point equality
and three lower-weight equalities. Consequently a universal finite set of
directions can be constructed from lattice points of \(\Delta_6\), independently
of the ideal.

Exact independent constructions find **2,425** positive primitive directions.
Write \(b=n/u\), \(u=\min_i n_i\), and \(H=h/u\). The mandatory predecessors of
\(p\), the condition \(H<7\), and the requirement that at least 30 eligible
lattice points exist leave **44,281** universal parameter cells \((p,n,h)\).
Vertices with \(H\ge7\) are handled by the existing high-height theorem.

For each cell, use occupancy variables \(t_x\in[0,1]\) and auxiliary variables
for erosion, exposed surfaces, and mixed corners. There are 455 variables.
Lower closure, the unique full-support corner, and the arithmetic budgets
give a fixed collection of linear inequalities. Every genuine ideal embeds
by its zero-one indicators; fractional feasible points are allowed as a
relaxation.

If the rows are \(Ax\le r\), with bounds \(l\le x\le v\), any nonnegative
rational vector \(\lambda\) proves the exact upper bound
\[
c\cdot x\le
\lambda\cdot r+
\sum_i\max\{(c-A^\mathsf T\lambda)_i l_i,\,
             (c-A^\mathsf T\lambda)_i v_i\}.
\tag{9}
\]
Here \(c\) encodes the fixed-height score \(u(m-D_h)\). Equation (9) follows
just by multiplying valid inequalities by nonnegative numbers and bounding
each remaining variable by its interval. It does not require an exact LP
solver or zero coefficient residuals.

All **44,281** cells have now passed a complete independent integer replay:

- **40,115** cells have exact moment upper-bound certificates.
- **4,166** cells are excluded by an exact cardinality bound strictly below 30.
- The largest certified normalized moment upper bound is
  \(-999992/1000000\), below the required \(29/10\).

The independent verifier reconstructs the weight directions by a different
algorithm, rebuilds the indicator inequalities, and checks the rational
combinations using Python standard-library integers. It imports neither the
producer nor SciPy and enumerates no individual ideals.

Together with the high-height theorem, the vertex argument gives
\(D_T(b)\ge m-29/10\) for every \(b_i\ge1\). Linear-programming duality then
provides the corresponding centroid witness in \(\operatorname{conv}(T)\).
The better observed margin in the checked cells is not asserted for all
weights or heights: the remaining vertices use the high-height theorem's
original bound.

The detailed proof, exact multipliers, independent reconstruction, and observed
replay records are in round10/envelope. This provides an alternative to the
shape-enumerating local proof, not an additional dependency of that proof.

| Route | Centroid conclusion | Remaining computation |
|---|---|---|
| Local two-step moves or axis endpoints | \(D_0\ge m\); explicit witness; fewer hypotheses | Check two formulas on 5,574,644 shapes |
| Universal indicator inequalities | \(D_0\ge m-29/10\); existence by duality; original arithmetic hypotheses | Check 44,281 parameter certificates; use the high-height theorem |
| Clipped boxes and prisms | Explicit analytic witnesses on the stated infinite families | None |

The first route has the simpler witness and smaller verification machinery.
The second eliminates individual-shape enumeration in the centroid component.
A short symbolic choice of the multipliers in (9), valid across parameter
ranges, would further simplify the second route; it has not been derived here.
