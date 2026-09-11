# Extensions beyond four generators, and their limits

This section separates identities valid in every embedding dimension from structural theorems for specified families and from proposed extensions. None of the arguments below establishes Wilf's conjecture for all semigroups with five or more minimal generators. No novelty claim is made for the identities or sufficient families.

## 1. The arithmetic and centroid formulations in arbitrary dimension

Let
\[
S=\langle m,a_1,\ldots,a_d\rangle,\qquad e=d+1,
\]
be a minimally generated numerical semigroup, with multiplicity \(m\). The embedding dimension is \(e\); the associated Apéry exponent ideal has dimension \(d=e-1\). Choose, for each Apéry element, its lexicographically least factorization in the \(a_i\). The chosen exponents form a finite lower ideal \(T\subset\mathbb N^d\) of cardinality \(m\), whose labels \(a\cdot x\) represent every residue modulo \(m\) exactly once. Here and below \(\mathbb N\) includes zero.

Write
\[
s=\sum_{x\in T}x,\qquad
M=\max_{x\in T}a\cdot x=c+m-1,\qquad
\alpha=\frac{d-1}{2},
\]
and define
\[
D_d=dmM-(d+1)a\cdot s.
\]
If \(n=|S\cap[0,c)|\) and \(W_e=en-c\), the Apéry genus formula gives the exact identity
\[
\boxed{mW_{d+1}=D_d-\alpha m(m-1).}
\tag{HD1}
\]
Indeed, \(g=(a\cdot s)/m-(m-1)/2\), \(n=c-g\), and substitution into \((d+1)n-c\) yields (HD1).

Every coordinate line meeting \(T\) is an initial integer interval. Let \(L_\ell\) denote its length and \(t_\ell\) its top endpoint; take the sum over lines in all \(d\) directions. Counting points and summing the arithmetic progression on each line yields the vector identities
\[
\sum_\ell L_\ell=dm,
\qquad
\sum_\ell L_\ell t_\ell=(d+1)s.
\tag{HD2}
\]
For the second identity, lines in direction \(j\) contribute \(s+s_j e_j\). Consequently
\[
D_d=\sum_\ell L_\ell(M-a\cdot t_\ell)\ge0.
\tag{HD3}
\]
Thus the line-endpoint construction is available in every dimension; the required positive surplus is the substantive issue.

Set \(A=\min_i a_i\ge m+1\), \(b=a/A\), \(H=\max_T b\cdot x\), and \(D_{d,0}=D_d/A\). A weight-independent sufficient condition is a point \(z\in\operatorname{conv}(T)\) such that
\[
r=dmz-(d+1)s\ge0\quad\text{coordinatewise},
\qquad
|r|_1\ge\alpha m.
\tag{HD4}
\]
For every \(b_i\ge1\), such a point gives
\[
D_{d,0}=dmH-(d+1)b\cdot s
\ge b\cdot r\ge|r|_1\ge\alpha m.
\]
For a genuine Apéry ideal, (HD1) then implies the stronger conclusion
\[
W_{d+1}\ge\alpha(A-m+1)\ge d-1>0
\quad(d\ge2).
\tag{HD5}
\]
The coefficient and target change with dimension. In particular, the four-generator residual target \(m\) becomes \(3m/2\) for five generators.

The weaker contradiction strategy also generalizes exactly. Since \(W_{d+1}\) is an integer, a counterexample has \(W_{d+1}\le-1\). By (HD1),
\[
0\le D_d\le\alpha m(m-1)-m.
\]
Dividing by \(A\ge m+1\) gives
\[
\boxed{W_{d+1}<0\ \Longrightarrow\
\alpha m-D_{d,0}\ge\frac{dm}{m+1}.}
\tag{HD6}
\]
Thus, for five generators, a proof that \(3m/2-D_{4,0}\le39/10\) for \(m\ge40\) would suffice for that range, because \(160/41-39/10=1/410>0\). This is a sufficient target, not an established higher-dimensional bound.

## 2. Both explicit centroid constructions extend formally

The two constructions used in the residual four-generator computation have direct counterparts in dimension \(d\).

**Upward movement of line endpoints.** For every coordinate line, choose \(u_\ell\in T\) with \(u_\ell\ge t_\ell\) coordinatewise. Then
\[
z=\frac1{dm}\sum_\ell L_\ell u_\ell\in\operatorname{conv}(T),
\qquad
r=\sum_\ell L_\ell(u_\ell-t_\ell)\ge0.
\tag{HD7}
\]
The total surplus is exactly the sum of the upward step counts, weighted by the line lengths. Restricting to at most two steps remains a valid construction in any dimension. What has not been established is that the available movements, alone or with the axis construction, attain \(\alpha m\) for an appropriate exhaustive higher-dimensional residual class.

**Axis endpoints.** Suppose \(q_i=\max_Tx_i>0\), and write \(q_{\max}=\max_iq_i\). Define
\[
G_d(T)=q_{\max}\left(dm-(d+1)\sum_{i=1}^d\frac{s_i}{q_i}\right).
\tag{HD8}
\]
If \(G_d(T)\ge\alpha m\), an explicit combination of the axis endpoints satisfies (HD4). To see this, give \(q_i e_i\) the initial coefficient
\[
\beta_i=\frac{(d+1)s_i}{dmq_i}.
\]
Their sum is at most one under the stated hypothesis. Assign the remaining coefficient to any longest axis endpoint. The resulting residual is nonnegative, supported on that axis, and has total \(G_d(T)\).

These formulas are dimension-independent witness constructions. The coverage theorem for the finite four-generator class does not itself imply a coverage theorem in the next dimension.

There is also a necessary limitation on any proposed universal centroid statement. The ordinary semigroup
\[
S=\{0\}\cup\{d+1,d+2,\ldots\}
\]
has \(e=m=d+1\), \(T=\{0,e_1,\ldots,e_d\}\), and \(W_e=0\). For any \(z\in\operatorname{conv}(T)\),
\[
\sum_i\bigl(dmz_i-(d+1)s_i\bigr)
=d(d+1)\left(\sum_i z_i-1\right)\le0.
\]
It therefore admits no witness with positive total surplus. This shows that (HD4) cannot hold for every genuine Apéry ideal. A uniform positive centroid theorem must specify a residual class and handle equality families separately, as the four-generator argument does. The example does not contradict Wilf: allowing all normalized weights discards the arithmetic distinctions among the actual generator labels.

## 3. An analytic higher-dimensional family: corner-clipped boxes

The direct clipped-box witness extends without enumeration. Let \(d\ge4\), choose integers \(1\le p_i<n_i\), and put
\[
T=\prod_{i=1}^d\{0,\ldots,n_i-1\}\setminus(p+\mathbb N^d),
\]
\[
N=\prod_i n_i,\qquad Q=\prod_i(n_i-p_i),\qquad m=N-Q.
\]
For each \(i\), let \(v^{(i)}\) be the full upper corner, with its \(i\)-th coordinate replaced by \(p_i-1\). All \(v^{(i)}\) belong to \(T\). Take their average as \(z\).

Subtracting the removed box's first moment from the full box's moment gives
\[
2s_i=m(n_i-1)-Qp_i.
\]
Also \(dz_i=d(n_i-1)-(n_i-p_i)\). Hence the residual is exactly
\[
\boxed{
r_i=\frac{d-3}{2}m(n_i-1)+m(p_i-1)
       +\frac{d+1}{2}Qp_i.}
\tag{HD9}
\]
Every coordinate is nonnegative. Since \(n_i-1\ge p_i\ge1\),
\[
|r|_1\ge\frac{d(d-3)}2m\ge\frac{d-1}{2}m,
\]
the last inequality following from \(d^2-4d+1\ge0\) for integer \(d\ge4\). Thus (HD4) holds for every such clipped box, with no condition on unequal normalized weights. Whenever it is the preferred Apéry ideal of a minimally \((d+1)\)-generated numerical semigroup, (HD5) proves strict Wilf.

This is an explicit infinite sufficient family in every embedding dimension at least five. It does not provide a decomposition theorem for general Apéry ideals. In particular, decomposing an ideal into overlapping pieces does not permit subtraction of their centroid witnesses: the overlap moments must be controlled separately. The analogous three-dimensional clipped-prism formulas likewise establish the families stated in the analytic supplement, rather than a classification of arbitrary ideals.

## 4. Arithmetic restrictions that survive in every dimension

Residue injectivity supplies additional structure beyond being a lower ideal. The following restrictions hold in every dimension and can be combined with the preceding witness constructions.

* If \(p\) is a minimal excluded exponent and \(x\in T\) is its residue representative, their supports are disjoint. Otherwise subtracting a common unit coordinate gives distinct points of \(T\) with the same residue. Distinct minimal exclusions sharing a positive coordinate also have different residues. In particular, there is at most one full-support minimal exclusion.
* For nonempty \(I\subseteq\{1,\ldots,d\}\), let \(C_I\) consist of excluded exponents \(q\) for which \(q_i>0\) and \(q-e_i\in T\) for every \(i\in I\). If \(\pi_I\) deletes those coordinates, the predecessor argument injects \(C_I\) into the complementary coordinate face, giving
  \[
  |C_I|\le|\pi_I T|.
  \tag{HD10}
  \]
* If \(F_i=\{x\in T:x+e_i\notin T\}\), then
  \[
  |F_i\cap F_j|\le2|\pi_{\{i,j\}}T|\quad(i\ne j).
  \tag{HD11}
  \]
  Indeed, a nonempty planar lower ideal with \(h\) maximal points has \(h-1\) mixed excluded corners. Slicing at fixed values of the other coordinates and applying (HD10) proves (HD11). It bounds the average number of maxima over nonempty planar slices by two; it does not bound each individual slice by two.
* If finite integer sets \(E,B\) satisfy \(E+B\subseteq T\), then
  \[
  |E-B|\le m.
  \tag{HD12}
  \]
  Equal residues of \(x-y\) and \(x'-y'\) give equal residues of \(x+y'\) and \(x'+y\), both in \(T\), and therefore equal difference vectors. Taking \(B=\{0,e_1,\ldots,e_d\}\) and \(E=T\ominus B\) yields \(|E|+\sum_i|\pi_iE|\le m\).

These are necessary restrictions. They have not been shown to characterize preferred Apéry ideals or to imply the required centroid inequality in arbitrary dimension.

## 5. Two genuine obstructions to extending the three-coordinate geometry

The geometric reduction for four generators uses three exponent coordinates. Both the compatibility-graph argument and the sufficiency of pair profiles fail for actual five-generator semigroups.

**A cycle in an actual Apéry ideal.** For
\[
S=\langle9,12,15,19,20\rangle,
\]
use coordinate weights \((19,20,12,15)\). Its Apéry exponent ideal is
\[
T=\{0,e_1,e_2\}+\{0,e_3,e_4\}.
\]
The nine labels are \(0,12,15,19,20,31,32,34,35\), with distinct residues modulo nine. The six minimal exclusions have the strict reductions
\[
\begin{aligned}
38&=20+2\cdot9,&39&=12+3\cdot9,&40&=19+12+9,\\
24&=15+9,&27&=3\cdot9,&30&=12+2\cdot9.
\end{aligned}
\]
Thus every outside exponent has a label whose value minus nine lies in \(S\); the displayed ideal is exactly the Apéry ideal, with unique factorizations. Its positive-coordinate compatibility edges are \(13,14,23,24\), an induced four-cycle. There is no full-support excluded corner. Nor can a central box with coordinate horns describe this ideal: an admissible central corner uses at most two coordinates, and some included point exceeds it in at least two coordinates. A single coordinate horn can exceed it in only one.

**An exclusion invisible in every pair projection.** For
\[
S=\langle14,21,29,30,32\rangle,
\]
use weights \((29,30,32,21)\). Its Apéry ideal is
\[
T=\{0,1\}^4\setminus\bigl((1,1,1,0)+\mathbb N^4\bigr).
\]
The fourteen residues are supplied by weights \((1,2,4,7)\) modulo fourteen: the first three bits give \(0,\ldots,6\), and the last bit adds zero or seven. The minimal exclusions have reductions
\[
58=30+2\cdot14,\quad60=32+2\cdot14,\quad
64=29+21+14,\quad42=3\cdot14,\quad91=21+5\cdot14.
\]
These again establish the exact Apéry description. Every pair projection is the full Boolean square, although the ideal has a support-three exclusion. Intersecting the pair cylinders would incorrectly restore two excluded points.

The semigroups are minimally five-generated and have Wilf values \(18\) and \(65\), respectively. They are not counterexamples to Wilf. They demonstrate that higher dimensions require a method that handles both cycles and exclusions of intermediate support; merely adding another horn or another pair profile is insufficient.

## 6. The separate proposed fixed-dimension finite reduction

The earlier analytic manuscript, `wilf_fixed_dimension_finite_reduction_2026-09-05.md`, proposes eventual strict Wilf at every fixed embedding dimension. This is a separate theorem with its own proof dependencies and outstanding external review. It is not a consequence of the four-generator centroid verification.

For \(d\ge2\), its displayed constants are
\[
h_d=\frac1{8d},\qquad r_d=\frac1{16d^2(d+1)},\qquad
\delta_d=d!h_dr_d^d,
\]
\[
P_d=1+32d(d-1)(d+1)^2,\qquad
H_d=\frac{(d-1)P_d}{\delta_d},\qquad
B_d=\left\lceil\frac{(d+H_d)^d}{d!}\right\rceil.
\]
That manuscript asserts \(m\ge B_d\Rightarrow W_{d+1}>0\), with every remaining counterexample contained in
\[
d+2\le m<B_d,\qquad
a_i\le M\le\frac{m(m-d)}2\bigl((d-1)(m-1)-2\bigr).
\tag{HD13}
\]
The analytic dependencies are a quantitative continuous gap for the single-full-corner class, an estimate controlling unequal weights when the discrete deficit is small, a lattice-point bound, and an arithmetic exclusion of discrete simplices for the conductor bound. Each needs review independently of the present finite centroid theorem.

For five generators, its formulas give
\[
\delta_4=\frac3{10\,737\,418\,240\,000},\qquad
H_4=103\,089\,952\,522\,240\,000,
\qquad B_4\approx4.706\times10^{66}.
\]
Even if the proposed analytic argument is accepted, the remaining region is far beyond practical exhaustive enumeration. Its value is a possible reduction from an infinite question to a bounded one, not a completed five-generator proof.

## 7. A focused continuation

For the four-generator manuscript, the immediate analytic target is to derive the local-movement or axis surplus directly from the specified residual corner and surface restrictions. That would replace the remaining shape enumeration with a structural proof. The existing clipped-box and clipped-prism identities provide exact infinite families against which proposed general lemmas can be tested.

For higher dimensions, the transferable part of the program is (HD1)–(HD12): the moment identity, the integer contradiction threshold, explicit convex witnesses, and arithmetic restrictions. An extension needs both an appropriate residual class, excluding equality obstructions, and a proof that its witnesses reach the dimension-dependent target. The two genuine five-generator examples identify structural requirements for such a proof. Neither the success of the four-generator verification nor the formal availability of the witness formulas supplies that missing coverage theorem.
