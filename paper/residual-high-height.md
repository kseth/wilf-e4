# Residual high-height proof and finite contracts

## Scope and status

This note selects one route for B6: an exact four-allowance strip,
a finite-to-continuous transfer, a compactness implication, and an exact
closed-box interval certificate. Each computational premise is stated
independently of a saved run. Evidence is recorded separately.
The target for a genuine residual Apéry ideal is
\[
D_0\ge m-\frac{29}{10}\qquad(R\ge7,\ |p|_1\ge5).
\]
The inputs are the [phase/thickening theorem](phase-and-thickening.md)
and [central-box/three-horn theorem](central-box-horns.md).

## 1. B6.1: finite-strip specification

For \(R\in\{18,19,20,21\}\), let \(T\) be any nonempty finite lower ideal
in \(\mathbb N^3\), of degree at most \(R\), with at most one full-support
minimal excluded point. Write
\[
m_T=|T|,\qquad D_R(T)=3Rm_T-4\sum_{x\in T}|x|_1.
\]

> **B6-strip-FV.** For every such \(R,T\),
> \[
> D_R(T)\ge4m_T.
> \tag{S}
> \]
> Missing coordinate units and maximum degree strictly below \(R\)
> are allowed. The empty ideal satisfies (S) by equality.

### Complete corner and support coverage

An actual positive minimal excluded point \(p\) has
\(p-e_i\in T\); therefore \(|p|_1\le R+1\).
Delete its orthant generator from the complement to obtain a finite
no-full-corner ideal \(U\). Pure-axis exclusions remain, and clipping
by a positive \(p\) leaves all axis points unchanged. Thus
\[
T=U\setminus(p+\mathbb N^3),\qquad
0\le\max_Ux_i=\max_Tx_i\le R.
\tag{1}
\]
If no such corner exists, set \(U=T\) and \(p=(1,1,R-1)\).
This corner is inactive on the degree-\(R\) simplex.
Unit weights and the score are symmetric, so enumerate exactly
\[
1\le p_1\le p_2\le p_3,\qquad |p|_1\le R+1.
\tag{2}
\]
Minimality of the enumerated corner is not required by the evaluator;
allowing inactive/nonminimal corners only enlarges its covered class.
Zero axis caps and singleton ideals must not be skipped.

### Exact section and center scores

Put \(f_R(x)=4|x|_1+4-3R\).
For direction \(i\), level \(t\), and transverse caps \(u,v\), let
\[
A_i(t,u,v)=
\{x:x_i=t,\ 0\le x_j\le u,\ 0\le x_k\le v,\ x\not\ge p\},
\qquad C_i(t,u,v)=\sum_{A_i(t,u,v)}f_R(x).
\]
Call a section feasible if its *retained* maximum degree is at most \(R\).
The uncut upper corner need not be retained. Its axis point survives;
therefore no nonempty section can occur beyond level \(R\).
The exact nested-rectangle upper bound is
\[
F_i(R+1;b,c)=0,\qquad
F_i(t;b,c)=
\max\left(0,\ 
\max_{\substack{0\le u\le b,\ 0\le v\le c\\A_i(t,u,v)\ {\rm feasible}}}
\{C_i(t,u,v)+F_i(t+1;u,v)\}\right).
\tag{3}
\]
The zero option terminates a horn; lower closure prevents restarting it.
Backward induction proves (3) for every nested horn in the structural
decomposition. Prefix maxima are an equivalent implementation of the
inner maximum, since a proper subrectangle reduces at least one cap.

For a central cap \(c\in\{0,\ldots,R\}^3\), put
\(A(c)=[0,c]\setminus(p+\mathbb N^3)\), and require its retained
maximum degree to be at most \(R\). Define
\[
V_{R,p}=\max_{c\ {\rm feasible}}
\left(\sum_{x\in A(c)}f_R(x)
+\sum_iF_i(c_i+1;c_j,c_k)\right).
\tag{4}
\]
The center and horns are disjoint before and after clipping. The
structural theorem and (3) give
\[
4|T|-D_R(T)=\sum_T f_R(x)\le V_{R,p}.
\tag{5}
\]
Every central anchored box retains the origin, so the maximum is nonempty.
Consequently the finite per-configuration predicate
\[
V_{R,p}\le0\quad\text{for all (2) and all four }R
\tag{6}
\]
implies (S). This computes upper bounds, not a list of all ideals.

Statistics may be computed either by full-box count/moment subtraction
and surviving-face maxima, or by independent retained-point sums.
The moment for an inclusive box \([a,b]\) is
\(\sum_B|x|_1=|B|\sum_i(a_i+b_i)/2\); use twice moments to keep
intermediate arithmetic integral. Inactive corners are covered by
the same formulas. Singleton score \(4-3R\) is a regression diagnostic,
not the acceptance predicate.

### Arithmetic and completeness

Here \(n=R+1\le22\). All supports lie in \([0,R]^3\).
A conservative bound for signed score, twice-moment, and disjoint-piece
intermediates is
\[
8n^3(9R+4)<2^{31}.
\tag{7}
\]
The implementations must use signed values with at least 63 value bits
and indices with at least 31 value bits, reject unsupported/partial modes,
enumerate all four allowances and every corner (2), and fail on any
positive bound. Stored outputs, counts, or checksums do not establish (6).
The selected audit requires two fresh independent complete implementations.

The four allowances are precisely those arising from translations of a
mesh of size \(1/21\) in the unit simplex; their necessity and the
continuous consequence are proved next, conditionally on (S).


## 2. B6.2: conditional finite-to-continuous transfer

Assume B6-strip-FV. Let \(K\subseteq\mathbb R_{\ge0}^3\) be a measurable
downset of positive volume, contained in the unit simplex, whose complement
is, up to boundary conventions, a finite union of upper orthants with
at most one coordinatewise minimal vertex of full support. Then
\[
\boxed{\kappa_c(K)=3-4\mathbb E_K|X|_1\ge\frac5{42}.}
\tag{8}
\]

### Translated sections preserve the required exclusion class

Fix \(h=1/21\). Almost every point of the orthant has a unique expression
\(x=r+hy\), with \(r\in[0,h)^3\), \(y\in\mathbb N^3\).
For each translation put \(T_r=\{y:r+hy\in K\}\).
It is finite and lower closed. An excluded orthant vertex \(g\) maps to
\[
g'_i=\max\!\left(0,\left\lceil\frac{g_i-r_i}{h}\right\rceil\right).
\tag{9}
\]
A zero coordinate remains zero. A generator supported on at most two
coordinates cannot produce a full-support generator. The one possible
positive generator produces at most one; deleting redundant generators
does not increase this number. Thus every nonempty \(T_r\) has the exact
support restriction needed for (S), without assuming coordinate units.
Boundary differences affect a null set: for each of the finitely many
orthant walls, the relevant translation coordinate belongs to a finite
set modulo \(h\). We may use the closed-orthant convention away from
those exceptional translations.

Put
\[
R_r=\left\lfloor\frac{1-|r|_1}{h}\right\rfloor,\qquad
\varepsilon_r=1-|r|_1-hR_r.
\]
Since \(0\le |r|_1<3h\),
\(R_r\in\{18,19,20,21\}\) and \(0\le\varepsilon_r<h\).
The simplex constraint gives \(|y|_1\le R_r\) for every \(y\in T_r\).
Direct expansion, including its sign, gives
\[
\begin{aligned}
\sum_{y\in T_r}(3-4|r+hy|_1)
&=hD_{R_r}(T_r)+(3\varepsilon_r-|r|_1)|T_r|\\
&\ge (4h-|r|_1)|T_r|.
\end{aligned}
\tag{10}
\]
Empty sections contribute zero. Integrate over the translation cube:
the maps \(r\mapsto r+hy\) have Jacobian one, so
\[
\kappa_c(K)\ge
4h-\sum_i\mathbb E_K(X_i\bmod h).
\tag{11}
\]
There is no additional \(h^3\) factor. All sets are bounded and the
integrands integrable, so the finite/countable partition and Fubini
steps are justified.

### The remainder average, not a pointwise estimate

Fix the other two coordinates. A coordinate fiber of a downset is an
interval starting at zero, of some length \(L\ge0\), up to endpoints.
Write \(L=qh+t\) with integer \(q\ge0\) and \(0\le t<h\). Then
\[
\int_0^L(x\bmod h)\,dx
=\frac{qh^2+t^2}{2}\le\frac{h(qh+t)}2=\frac{hL}{2}.
\tag{12}
\]
Fubini and division by the positive volume give
\(\mathbb E_K(X_i\bmod h)\le h/2\).
Substitution into (11) proves
\(4h-3h/2=5h/2=5/42\), including equality.
The weaker pointwise bound \(|r|_1<3h\) would not prove this constant.

Positive diagonal rectangular thickenings in the phase/thickening theorem
satisfy this entire continuous class: finite orthant complements,
preserved supports, positive volume, and simplex containment.
Thus (8) applies to a genuine residual ideal as soon as (S) is established.
No success of an unverified saved program has been assumed.


## 3. B6.3: conditional compactness and outward clipping

Assume (S), hence the continuous gap (8). Let \(T\) be a genuine B6
Apéry ideal, put \(w=(1,b,c)\) after simultaneously sorting coordinates
and weights, \(H=\max_Tw\cdot x\), and \(B=1+b+c\).
The unique full-support corner is positive and minimal; its predecessors
contain the coordinate units. Thus \(1\le b\le c\le H\).
Since every weight is at least one, \(H\ge R\ge7\).

Suppose the target fails:
\[
D_0<m-\frac{29}{10}<m.
\tag{13}
\]
The phase theorem gives \(B<9+28/(H-3)\). Thickening and (8) give
\[
D_0/m\ge(5H-37B)/42,\qquad 5H<42+37B.
\tag{14}
\]
Combining the two strict bounds, with \(H-3>0\), yields
\[
5H^2-390H+89<0.
\tag{15}
\]
The polynomial is positive at 78 (value 89) and strictly increasing
thereafter. Hence \(7\le H<78\).
For any positive minimal corner \(p\), \(p-e_1\in T\) and \(w_1=1\), so
\[
|p|_1\ge5,\qquad w\cdot p\le H+1.
\tag{16}
\]
There is no weight-ordering restriction on \(p\); all positions of its
coordinates must remain covered.

### Closed necessary failure region

Use the closed superset
\[
\mathcal F_6=\{(b,c,Q):
1\le b\le c\le Q,\quad 7\le Q\le78,\quad
1+b+c\le9+28/(Q-3),\quad
5Q\le42+37(1+b+c)\}.
\tag{17}
\]
A genuine failure lies in this region at \(Q=H\), and satisfies (16).
The interval proof need only cover (17), not every ordered point of
the whole root. This restriction is conditional on the established
continuous gap, not a conjectural geometric skip.

At scale \(q=4096\), let integer endpoints
\(L=(B_0,C_0,H_0)\), \(U=(B_1,C_1,H_1)\) enclose a raw closed box.
Each of the following updates encloses its intersection with (17):

1. Order:
\[
L\leftarrow(B_0,\max(B_0,C_0),\max(B_0,C_0,H_0)),\qquad
U\leftarrow(\min(B_1,C_1,H_1),\min(C_1,H_1),H_1).
\]
2. If not inverted, set
\[
S_{\max}=9q+\left\lceil\frac{28q^2}{H_0-3q}\right\rceil,
\quad
B_1\leftarrow\min\!\left(B_1,\left\lceil\frac{S_{\max}-q}{2}\right\rceil\right),
\quad
C_1\leftarrow\min(C_1,S_{\max}-q-B_0).
\]
3. Set
\[
S_{\rm upper}=\min(q+B_1+C_1,S_{\max}),\qquad
H_1\leftarrow
\min\!\left(H_1,\left\lceil\frac{42q+37S_{\rm upper}}5\right\rceil\right).
\tag{18}
\]

The denominator is positive throughout this root.
For update 2, \(q(1+b+c)\le S_{\max}\) follows from \(qQ\ge H_0\);
\(b\le c\) gives \(2qb\le S_{\max}-q\), and \(qb\ge B_0\)
gives the second cap. Update 3 follows from the last inequality of (17).
Every ceiling is outward. No floor may replace these upper ceilings.

Perform these updates in order at most twenty times, stopping on inversion
or unchanged endpoints. Each finite step preserves every relevant real
point. Convergence is not needed for soundness. Inversion proves that
the raw box contains no point of (17). Otherwise the resulting tightened
box remains a closed enclosure; splitting that enclosure covers every
relevant point of the raw parent, including boundary walls.


## 4. B6.4: high-height interval contract and coverage

> **B6-high-FV.** For every \((b,c,Q)\in\mathcal F_6\), every positive
> integer \(p\) with \(|p|_1\ge5\) and \((1,b,c)\cdot p\le Q+1\),
> and every nonempty finite no-full-corner lower ideal \(U\), let
> \(T=U\setminus(p+\mathbb N^3)\).
> If \(\max_T(1,b,c)\cdot x\le Q\), then
> \[
> |T|-\left(3Q|T|-4(1,b,c)\cdot\sum_Tx\right)\le29/10.
> \tag{I}
> \]
> Neither minimality of \(p\), residue labels, units, cardinality,
> nor exposed-surface restrictions are assumed in this finite contract.

A genuine failure satisfies every hypothesis at \(Q=H\), by (16)--(17)
and the structural clipping theorem. Thus established (S) and (I)
contradict (13), proving the B6 target.

### Whole-box domination and finite corner range

On a tightened integer box put
\[
\ell=(q,B_0,C_0),\quad u=(q,B_1,C_1),\quad
h_-=H_0,\ h_+=H_1,\quad N_i=\lfloor h_+/\ell_i\rfloor.
\]
Every relevant retained point satisfies \(\ell\cdot x\le h_+\);
unchanged axes bound all coordinates of \(U\) by \(N_i\).
The exact integer point majorant is
\[
\psi(x)=4u\cdot x+q-3h_-,\qquad
q\left(|T|-(3Q|T|-4w\cdot\sum_Tx)\right)\le\sum_T\psi(x).
\tag{19}
\]
It holds for every real parameter in the box; there is no weight grid.
Every relevant \(p\) is covered by the finite list
\[
p_i\ge1,\quad 5\le |p|_1\le\lfloor h_+/q\rfloor+1,\quad
\ell\cdot p\le h_++q.
\tag{20}
\]
Indeed all \(\ell_i\ge q\), and the real corner bound implies the last
inequality. No sorting of \(p\) is allowed unless the *lower and upper*
weights of the exchanged coordinates are both equal. The independent
route enumerates the full Cartesian list without symmetry pruning.
An empty list means no genuine candidate corner; acceptance is vacuous,
not a claimed numerical bound on an actual ideal.

### Clipped statistics and recurrence

For an inclusive box \(B=[a,b]\), let
\[
n(B)=\prod_i(b_i-a_i+1),\quad
J(B)=n(B)\sum_i u_i(a_i+b_i).
\]
Here \(J=2\sum_Bu\cdot x\). Subtract the removed box
\([\max(a,p),b]\), when nonempty, to obtain \(n(A),J(A)\) for
\(A=B\setminus(p+\mathbb N^3)\).
Its retained feasibility maximum is
\[
M(A)=\max_{\substack{i\\a_i\le\min(b_i,p_i-1)}}
\left(\ell_i\min(b_i,p_i-1)+\sum_{j\ne i}\ell_jb_j\right).
\tag{21}
\]
A retained point has some coordinate below \(p\); the upper corner
of each such surviving part proves (21).
Independently partition by the first coordinate below \(p\):
\[
A=\mathbin{\dot\bigcup}_{i=1}^3
\left(B\cap\{x_j\ge p_j\ (j<i),\ x_i<p_i\}\right).
\tag{22}
\]
Summing disjoint-box counts and moments and maximizing their heights
gives the same statistics without subtraction.

For the axis-\(i\) section \(A_i(t,r,s)\), its score is
\(C_i=2J+(q-3h_-)n\); feasibility is \(M\le h_+\).
For a central box use the identical score and retained feasibility,
not its uncut upper corner. With terminal \(F_i(N_i+1;R,S)=0\), use
\[
F_i(t;R,S)=
\max\left(0,\
\max_{\substack{r\le R,\ s\le S\\M(A_i(t,r,s))\le h_+}}
\{C_i(t,r,s)+F_i(t+1;r,s)\}\right).
\tag{23}
\]
All transverse caps are nonnegative. This is the same proved
nested-horn induction as (3), now with separate feasibility and objective
weights. Let
\[
V_p=\max_{c\ {\rm retained\ feasible}}
\left(2J(A(c))+(q-3h_-)n(A(c))
+\sum_iF_i(c_i+1;c_j,c_k)\right).
\tag{24}
\]
The origin survives every clipped center, so this maximum exists.
The disjoint decomposition proves the upper bound (19) by \(V_p\).
Independent horns may enlarge the geometric class; that is safe for
an upper bound. A leaf is accepted only if every corner (20) satisfies
\[
10V_p\le29q.
\tag{25}
\]
Integer comparison, not rounding or tolerance, handles equality.

Both paths may evaluate the equivalent nested-rectangle prefix maximum.
Their independent statistics and per-level implementations remain separate:
one uses subtractive moments and three prefix comparisons; the other uses
disjoint rectangles/boxes and a row-scan maximum followed by a column prefix.
A literal-point/explicit-transition implementation is additionally suitable
for bounded validation, but is not an omitted complete replay requirement.

### Closed-tree coverage

The root is \(((q,q,7q),(78q,78q,78q))\).
At every node apply the exact finite tightening schedule (18).
An inverted enclosure permits an empty leaf. Otherwise a split has
an axis and integer split strictly inside that tightened interval.
Its two children end and begin at the same split, in the other
coordinates retaining the tightened endpoints. They cover every
relevant parent point, including the shared wall.

Every stored node must be reached exactly once; its raw box must equal
the derived parent child, and every branch must end at a checked empty
or DP leaf. A DP leaf recomputes the entire corner list and all its
bounds. Cached completion flags, maximizing corners, case counts,
and producer bounds do not permit early acceptance.
Induction over this finite tree proves (I) throughout (17).

### Fixed-width envelope and fail-closed semantics

Within this root \(N_i\le78\), \(\ell_i,u_i\le78q\).
Let \(K=79^3\), \(W=78q\). Counts are at most \(K\);
twice moments are at most \(156(3W)K\).
Center and horn supports are disjoint; a score envelope for every signed
mathematical intermediate, including threshold multiplication, is
\[
16K\bigl(156(3W)+235q\bigr)<2^{51}<2^{63}-1.
\tag{26}
\]
Array indices and dimensions fit signed 32-bit integers; signed scores
require at least 63 value bits. No arithmetic may involve a negative
infinity sentinel. For an empty corner list the worker must signal
vacuity separately. Python tree/hash/clipping arithmetic is arbitrary precision.

Malformed schemas, duplicate JSON fields, boolean endpoints, wrong roots,
incomplete/unreachable/repeated nodes, inconsistent children, unsupported
leaves, inward rounding, partial worker responses, positive threshold
violations, and changed inputs cause rejection. The final evidence must
name the exact data and source versions and independently recheck coverage
and fresh leaf bounds on two paths.
