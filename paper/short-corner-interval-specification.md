# Short-corner high-height interval specification

## Purpose and trust boundary

This note makes the retained D4 high-height contract, clipped-box statistics,
horn recurrence, and real-parameter coverage explicit. It is a mathematical
specification and soundness proof; replay evidence belongs in the separate
R4a audit. The [D4 decision](../research/b4-simplification-decision.md)
retains the historical tree without endorsing its cached success flags.

The [B4.2 compactness theorem](short-corner-compactness.md) and
[G5 clipping theorem](central-box-horns.md) are the analytic inputs.
The construction is the clipped version of the
[B2 interval specification](no-corner-interval-specification.md).

## 1. The finite contract

Put

\[
\mathcal P_4=\{(b,c,Q):1\le b\le c\le Q,\ 6\le Q\le42\},\qquad
w=(1,b,c),
\]
\[
\mathcal C=\{(2,1,1),(1,2,1),(1,1,2)\}.
\tag{1}
\]

> **B4-high-FV.** For every parameter in \(\mathcal P_4\), every
> \(p\in\mathcal C\), and every finite nonempty lower ideal \(U\) with
> no full-support minimal exclusion, set
> \(T=U\setminus(p+\mathbb N^3)\).
> If \(T\ne\varnothing\) and \(Q\ge\max_Tw\cdot x\), then, with
> \(m=|T|\), \(s=\sum_{x\in T}x\),
> \[
> \boxed{m-(3mQ-4w\cdot s)\le1.}
> \tag{FV}
> \]

The height allowance is imposed on \(T\), not \(U\); the uncut central
corner can be outside \(T\). No minimality of \(p\), residue labels,
plane-corner filters, coordinate units, or \(m\ge30\) are assumed.
Positive \(p\) leaves every axis section unchanged, so
every coordinate of \(U\) is bounded by \(\lfloor Q/w_i\rfloor\).

For a genuine B4 ideal, G5 supplies this representation. If its normalized
attained height \(H\ge6\) and \(D_0<m-1\), B4.2 gives \(H<36\) and,
after simultaneously sorting weights and coordinates, one of the three
corners (1). Coordinate units give \(c\le H\). Applying (FV) at \(Q=H\)
contradicts the failure. Thus B4.2 and an established (FV) prove the
high-height target \(D_0\ge m-1\), then G1 gives \(W_4\ge1\).
The low-height branch remains separate.

## 2. Whole-box integer domination

At scale \(q=4096\), integer endpoints
\(L=(B_0,C_0,H_0)\), \(R=(B_1,C_1,H_1)\) describe a closed real box
for \((b,c,Q)\). Define

\[
\ell=(q,B_0,C_0),\qquad u=(q,B_1,C_1),\qquad
h_-=H_0,\quad h_+=H_1,
\]
\[
N_i=\lfloor h_+/\ell_i\rfloor,\qquad
\psi(x)=4u\cdot x-3h_-+q.
\tag{2}
\]

For every parameter in that box, feasibility of \(T\) implies
\(\ell\cdot x\le h_+\) on \(T\). Unchanged axes therefore bound the
coordinates of \(U\) by \(N_i\), although \(U\) itself need not satisfy
the weighted-height constraint. Pointwise monotonicity gives

\[
q(4w\cdot x-3Q+1)\le\psi(x),\qquad
q\bigl(m-(3mQ-4w\cdot s)\bigr)\le\sum_{x\in T}\psi(x).
\tag{3}
\]

These comparisons cover all real parameters, including irrational
weights and equality walls. No weight grid or interpolation is used.

## 3. Exact statistics after clipping

For an integer rectangular box \(B=[a,b]\), use coordinatewise inclusive
endpoints and omit an inverted box. Its full count, twice objective
moment, and feasibility maximum are

\[
n(B)=\prod_i(b_i-a_i+1),\quad
J(B)=n(B)\sum_i u_i(a_i+b_i),\quad
M(B)=\ell\cdot b.
\tag{4}
\]

Here \(J(B)=2\sum_{x\in B}u\cdot x\).
Let \(A=B\setminus(p+\mathbb N^3)\).
The removed box is \([\max(a,p),b]\), when nonempty. Subtracting its
count and twice moment from (4) gives \(n(A),J(A)\).
The retained feasibility maximum is

\[
M(A)=
\max_{\substack{i\\a_i\le\min(b_i,p_i-1)}}
\left(\ell_i\min(b_i,p_i-1)+\sum_{j\ne i}\ell_jb_j\right).
\tag{5}
\]

Indeed \(A\) is the union of the surviving faces' anchored subboxes:
a retained point has some coordinate below \(p\), and positive weights
maximize each such part at its upper corner. Relevant central boxes
and horn sections always retain their origin or axis point, so the
maximum is nonempty.

The independent statistics formula uses the disjoint partition

\[
A=\mathbin{\dot\bigcup}_{i=1}^3
\bigl(B\cap\{x_j\ge p_j\ (j<i),\ x_i<p_i\}\bigr).
\tag{6}
\]

It classifies a point by its first coordinate below \(p\).
Each part is a box; sum its count and twice moment and take the maximum
of its heights. This derives the same statistics without subtraction
or the surviving-face formula.

For a horn in direction \(i\), at level \(t\) with transverse caps
\(r,s\), apply these formulas to
\(B=\{t\}\times[0,r]\times[0,s]\) in the appropriate coordinate order.
The exact upper score is

\[
C_i(t,r,s)=2J(A)+(q-3h_-)n(A),
\tag{7}
\]

and the section is feasible exactly when \(M(A)\le h_+\).
For the central box \([0,c]\), use the same score formula, denoted
\(C_p(c)\), and the same retained-maximum feasibility test.
In particular, requiring \(\ell\cdot c\le h_+\) would incorrectly
reject some permissible uncut centers.

## 4. Horn recurrence and complete box bound

Let \(F_i(t;R,S)\) maximize the upper score of a possibly empty nested
clipped horn beginning at level \(t\), with first transverse caps at
most \(R,S\). Set \(F_i(N_i+1;R,S)=0\), and use

\[
F_i(t;R,S)=
\max\left\{0,\
\max_{\substack{0\le r\le R,\ 0\le s\le S\\
                M(A_i(t,r,s))\le h_+}}
\bigl(C_i(t,r,s)+F_i(t+1;r,s)\bigr)\right\}.
\tag{8}
\]

The zero option terminates the horn. A section's axis point survives
clipping, so lower closure forbids restarting after termination.
Every other transition selects the present rectangle and bounds the
next rectangle by its exact caps. Backward induction proves coverage
of every permitted nested sequence, as in G5.

With \(A_i^\sharp(t;R,S)\) equal to the candidate for precisely \(R,S\),
or absent when infeasible, (8) also has the prefix implementation

\[
F_i(t;R,S)=
\max\{0,A_i^\sharp(t;R,S),F_i(t;R-1,S),F_i(t;R,S-1)\},
\tag{9}
\]

omitting negative indices. Induction on \(R+S\) covers every subrectangle.
The second checking path evaluates (8) directly, not (9).

For each corner \(p\), define

\[
V_p(L,R)=
\max_{\substack{0\le c_i\le N_i\\M([0,c]\setminus(p+\mathbb N^3))\le h_+}}
\left(C_p(c)+\sum_i F_i(c_i+1;c_j,c_k)\right).
\tag{10}
\]

G5 partitions every relevant \(U\) into a central box and three disjoint
nested horns. Clipping preserves disjointness. Their statistics give
their exact upper scores, and (8) bounds each actual horn.
The independent horn choices may enlarge the geometric class but never
decrease its upper bound. Thus (3) proves

\[
q\bigl(m-(3mQ-4w\cdot s)\bigr)\le V_p(L,R).
\tag{11}
\]

A DP leaf is sound when all three corner bounds satisfy \(V_p\le q\).
The weak threshold includes equality.

## 5. Analytic leaves and closed-tree coverage

B4.2's simple planar partition uses only lower closure and exclusion
of the \(p\)-orthant; its allowance-height form applies also when
the corner is inactive or coordinate units are missing. It gives

\[
(3mQ-4w\cdot s)/m\ge(Q-4(1+b+c))/3.
\]

Therefore the whole-box planar rule

\[
H_0\ge3q+4(q+B_1+C_1)
\tag{12}
\]

proves deficit at least \(m\), hence the target. Equality is accepted.

Intersect each raw box with the order cone using the enclosing endpoints

\[
L^\sharp=(B_0,\max(B_0,C_0),\max(B_0,C_0,H_0)),\quad
R^\sharp=(\min(B_1,C_1,H_1),\min(C_1,H_1),H_1).
\tag{13}
\]

As proved in the B2 specification, the ordered intersections of the
raw and tightened boxes are equal. Inverted tightened endpoints mean
an empty ordered intersection. Otherwise all splits and leaf tests use
the tightened box.

The root is \(((q,q,6q),(42q,42q,42q))\).
A split along coordinate \(i\), at an integer strictly between its
tightened endpoints, gives two closed children ending and beginning
at that split. They cover the parent and share the entire boundary wall.
Require every stored node to be reached exactly once and every branch to
end at a checked empty, planar, or DP leaf. Induction down the finite
tree sends every ordered root parameter to a valid leaf. Equations
(11)--(12) then prove (FV).
This is a real-parameter coverage proof, not a test of rational grid points.

## 6. Fixed-width arithmetic and fail-closed semantics

Within the root, \(\ell_i\ge q\), \(u_i\le42q\), \(h_+\le42q\), so
\(N_i\le42\). Let \(K=43^3=79{,}507\), \(W=42q\).
All retained or uncut boxes and single-horn supports lie in \([0,42]^3\).
Counts are at most \(K\); twice moments and their subtraction operands
are bounded by \(84(3W)K\). Disjoint partition sums obey the same bound.
The magnitude of any point score is at most

\[
P=4\cdot42(3W)+127q.
\]

Horn candidates sum disjoint levels, and central-plus-horn candidates
sum disjoint pieces, so their score magnitudes are bounded by \(KP\).
A generous envelope for all arithmetic intermediates is

\[
16K\bigl(84(3W)+127q\bigr)<2^{47}<2^{63}-1.
\tag{14}
\]

There is no arithmetic on a negative-infinity sentinel. The origin is
always a feasible central box, so a finite final answer exists.
Flattened array sizes and indices are below \(44\cdot43^2<2^{17}\).
Consequently signed integers with at least 63 value bits and indices
with at least 31 value bits suffice; compilation must enforce those widths.

The certificate loader must reject repeated JSON fields, wrong schemas,
booleans in integer fields, malformed dimensions, unknown node kinds,
wrong roots or scale, invalid children, cycles, unreachable nodes,
and failed or incomplete runs. A DP bound has exactly three integer
entries in the order (1); no unvalidated fourth entry is allowed.
Every bound is freshly recomputed, and cached flags never substitute
for the recurrence or coverage check.

No fixed producer count or margin is a theorem predicate. Immutable
hashes identify proof data; only full local checking and full tree
coverage prove (FV). Independent-path and replay evidence must satisfy
[V0](../verification/trust-policy.md).
