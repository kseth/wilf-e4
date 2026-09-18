# Wilf in embedding dimension four: an explicit global finite reduction

**Date:** 5 September 2026.  
**Status:** The unrestricted conjecture is not proved or disproved here. This note gives an explicit large-multiplicity theorem, its complete analytic proof, and a finite region containing every possible four-generator counterexample. The arguments were independently checked during this research session; they have not undergone external peer review or formal proof-assistant verification. Publication priority has not been established.

## 1. Results and the exact unresolved task

Let
\[
S=\langle m,a_1,a_2,a_3\rangle,\qquad m<a_1<a_2<a_3,
\]
be a numerical semigroup with this minimal generating set. Write
\[
c=\text{conductor}(S),\quad n=|S\cap[0,c)|,\quad W=4n-c.
\]

**Theorem 1 (explicit large-multiplicity result).**
\[
\boxed{m\ge10^{27}\quad\Longrightarrow\quad W>0.}
\]

The proof establishes a quantitative moment inequality for every three-dimensional lower ideal containing the three unit vectors and having at most one minimal excluded point with all coordinates positive. Every preferred Apéry staircase satisfies that structural condition.

**Theorem 2 (analytic conductor reduction).**
\[
\boxed{W<0\quad\Longrightarrow\quad c\le m^2-3m+1,
\qquad a_3\le m(m-2).}
\]

The conductor bound was present in the preceding checkpoint with a computer-assisted dependency. The proof below removes that dependency by excluding a six-column configuration arithmetically and proving the remaining full weighted cases directly.

Together, these theorems give the unconditional finite reduction
\[
\boxed{W<0\ \Longrightarrow\ 4\le m<10^{27},
\quad m<a_1<a_2<a_3\le m(m-2).}
\tag{R}
\]
Using the published verification at multiplicity at most 19, the lower endpoint can be raised to 20. The core finite reduction (R) does not depend on that verification. Further published exclusions include conductor at most three times the multiplicity and genus at most 100 [3].

This is one finite region, rather than a finite box for each of infinitely many multiplicities. Its enormous size makes direct enumeration impractical. **No argument or exhaustive verification in this note eliminates the remaining region.** Thus (R) is a reduction, not a solution of Wilf in dimension four.

The supplementary slab theorem proves
\[
m\ge4K-2\Longrightarrow W\ge0,
\]
where \(K\) is the number of occupied rectangular cells obtained by compressing the coordinate intervals of the maximal Apéry exponents. It supplies another rigorous filter for (R), but does not bound all remaining compressed patterns.

An immediate asymptotic consequence is
\[
\liminf_{\substack{e(S)=4\\m(S)\to\infty}}\frac{n(S)}{c(S)}
\ge\frac14+1.5\times10^{-10}.
\]
Indeed the proof gives \(D/(mM)\ge6\times10^{-10}\), while its elementary lattice-point count gives \(M/m\to\infty\), hence \(m/c\to0\). Apply \(4n-c=D/m-(m-1)\). This is a derived consequence of the argument below, not an attribution to the existing literature.

## 2. Apéry preliminaries and the arithmetic restriction

Let \(\mathbb N=\{0,1,2,\ldots\}\). The Apéry set
\[
\operatorname{Ap}(S,m)=\{s\in S:s-m\notin S\}
\]
contains exactly one representative of every residue modulo \(m\). Select the lexicographically least factorization of each Apéry element using \(a_1,a_2,a_3\). The selected exponent set \(T\subset\mathbb N^3\) is a finite lower ideal of size \(m\), and contains \(0,e_1,e_2,e_3\).

To check downward closure, a divisor of an Apéry factorization is Apéry: otherwise adding its remaining factors would put the original element minus \(m\) in \(S\). Replacing a nonpreferred divisor factorization would also replace the original by a lexicographically smaller factorization. Both possibilities contradict its selection. Minimal generation places the three unit vectors in \(T\).

Set
\[
w(x)=a_1x_1+a_2x_2+a_3x_3,\quad
M=\max_Tw=c+m-1,\quad \Sigma=\sum_Tw,\quad D=3mM-4\Sigma.
\]
The classical Apéry genus formula gives
\[
g=\frac{\Sigma}{m}-\frac{m-1}{2},\qquad
\boxed{mW=D-m(m-1).}
\tag{1}
\]

If \(p\) is a coordinatewise minimal element of \(\mathbb N^3\setminus T\), let \(q\in T\) represent its residue. Their supports are disjoint. Indeed, a common positive coordinate \(j\) would put the distinct points \(p-e_j,q-e_j\) in \(T\) with equal residues. Likewise, two distinct minimal excluded points with a common positive coordinate cannot have the same residue. Consequently a minimal excluded point with all three coordinates positive has representative zero, and there is at most one such point.

This restriction is established prior work: see Hellus–Rechenauer–Waldi, Proposition 2.6 [2]. The proof is included to make the exact hypothesis of the stability theorem explicit.

Throughout, \(\pi_j\) denotes the projection deleting coordinate \(j\). For a coordinate line \(\ell\), let \(L_\ell\) be its length and \(t_\ell\) its top exponent. A separate partition into lines in each of the three directions gives
\[
\boxed{D=\sum_\ell L_\ell\bigl(M-w(t_\ell)\bigr)\ge0.}
\tag{2}
\]
For direction \(j\), the top weight averaged on a line is the mean total weight plus the mean contribution of coordinate \(j\). Summing over directions therefore gives \(4\Sigma\). This proves (2), the slack form of Zhai's lower-ideal inequality [1]. Wilf requires the additional correction \(m(m-1)\), which is why mere nonnegativity of (2) does not suffice.

## 3. Proof of the large-multiplicity theorem

The continuous lemma below is stated only for the exact sets needed: bounded downsets whose complements in the nonnegative orthant are finite unions of closed upper orthants. In the application these are unions of half-open rectangular cells. This fixes membership at boundary points while leaving all volume identities unchanged.

### 3.1 A continuous gap from the corner restriction

**Claim A.** Let K⊂Δ={x∈R³_≥0:x₁+x₂+x₃≤1} be a positive-volume downset whose complement in the nonnegative orthant is a finite union of closed upper orthants whose vertices have at most two positive coordinates, together with at most one orthant whose vertex has all coordinates positive. Write μ for its uniform mean x₁+x₂+x₃ and κ_c=3−4μ. Then κ_c≥10⁻⁶.

Boundary conventions are irrelevant for integrals. For the corner argument one may take the half-open pixel convention, as in the discrete application.

**Continuous identities.** If V=vol(K) and H_j(y) is the endpoint of its coordinate-j fiber, then

κ_c V = Σ_j J_j,
J_j = ∫_{π_jK} H_j(y)[1−Σy−H_j(y)]dy ≥ 0.

Indeed ∫H_j²=2∫_K x_j, so summing the three top-of-fiber integrals gives 4∫_K(x₁+x₂+x₃).

Further, with R=min(X₁,X₂,X₃) for uniform X∈K,

μ ≤ 2/3+E R.

To verify this, slice by the uniquely minimal coordinate j and its value r. Subtract r from each of the other two coordinates. Each resulting slice is a planar downset in u+v≤1−3r, whose mean u+v is ≤(2/3)(1−3r), by the continuous two-dimensional coordinate-line identity. The conditional total mean is therefore ≤2/3+r. Integrate the slices; ties have volume zero.

**Cube.** Suppose κ_c<10⁻⁶. Then E R≥1/12−κ_c/4>0.08. Thus there is a point of K with all coordinates greater than t=0.08, and K contains [0,t]³.

**Propagation lemma for seven specified targets.** For every target q satisfying

0≤q_i≤0.5, q₁+q₂≤0.8, q₁+q₂+q₃≤0.9,

κ_c<10⁻⁶ forces q∈K. Set r=0.015 and consider

v¹=(q₁+3r,3r,3r),
v²=(q₁+2r,q₂+2r,2r),
v³=(q₁+r,q₂+r,q₃+r).

1. If v¹∉K, then on y,z∈[3r,4r] the x-fiber has H_x≥t (by the cube) and H_x≤q₁+3r (by the omitted point). Hence its gap is at least 1−q₁−11r≥0.335. Thus
   J_x≥t r²(0.335)=0.00000603.
   Since V≤1/6, this gives κ_c≥0.00003618>10⁻⁶. Therefore v¹∈K.

2. If v²∉K, integrate y-fibers over x∈[q₁+2r,q₁+3r], z∈[2r,3r]. Membership of v¹ gives H_y≥3r; omission of v² gives H_y≤q₂+2r. The gap is at least 1−q₁−q₂−8r≥0.08. Thus
   J_y≥3r³(0.08)=0.00000081,
   whence κ_c≥0.00000486>10⁻⁶. Therefore v²∈K.

3. If v³∉K, integrate z-fibers over x∈[q₁+r,q₁+2r], y∈[q₂+r,q₂+2r]. Membership of v² gives H_z≥2r; omission of v³ gives H_z≤q₃+r. The gap is at least 1−Σq−5r≥0.025. Thus
   J_z≥2r³(0.025)=0.00000016875,
   whence κ_c≥0.0000010125>10⁻⁶. Therefore v³∈K, and q≤v³ implies q∈K.

**Contradiction from the corner condition.** Let

p=(0.5,0.3,0.3), q=(0.3,0.5,0.3), b=(0.3,0.3,0.3).

Points p and q are outside Δ and hence outside K. For each of p and q take the three points obtained by replacing one coordinate by 0.01. These six points, and b, satisfy the propagation-lemma bounds, so belong to K. Every excluded-orthant vertex below p must consequently have all three coordinates positive: a vertex with smaller support would also exclude the corresponding witness. Similarly q dominates an interior excluded vertex. Uniqueness makes these vertices identical and below min(p,q)=b, contradicting b∈K. This proves Claim A.

### 3.2 Transfer to a weighted integer lower ideal

Let T⊂N³ be a finite lower ideal containing 0,e₁,e₂,e₃, with at most one full-support minimal excluded point. Put m=|T|, normalize positive weights u_j so max_T u·x=1, and write κ=3−4E[u·X]. Set U=max u_j≤1 and v=min u_j.

For uniform \(X\in T\), define \(\mu_j=\mathbb E[u_jX_j]\) and \(\mu=\sum_j\mu_j\). Let \(H_j(x_{-j})\) be the largest integer coordinate on the corresponding discrete fiber, and put
\[
\delta_j(x)=1-u_jH_j(x_{-j})-\sum_{i\ne j}u_ix_i\ge0.
\]
Uniformity on each fiber gives
\[
\mathbb E\delta_j=1-\mu-\mu_j,\qquad
\sum_j\mathbb E\delta_j=\kappa,\qquad
\mu_j\ge\frac14-\frac{3\kappa}{4}.
\]
In particular, the normalized slack is nonnegative. For a downward coordinate shift, the map from the eligible points to their shifted points is injective, so summing the two gap terms counts each point at most twice. Also, for \(0\le Y\le1\), \(\Pr(Y\ge s)\ge\mathbb EY-s\). These are the two elementary counting steps used next.

**Phase estimate.** If κ≤1/15, then

U≤400κ+20v.

Indeed, if v>U/20 the conclusion is immediate. Otherwise choose distinct directions j,k of maximum and minimum weight. Let s₀=min(U/4,1/10), h=floor(s₀/v), s=hv. We have v≤s₀/2 and s∈[s₀/2,s₀]⊂(0,U/2]. Coordinate means satisfy μ_k≥1/4−3κ/4≥1/5. For x_k≥h, the nonnegative j-fiber gaps at x and x−h e_k differ by −s modulo U, so their sum is at least s. Summing pairs,

2κ≥2Eδ_j≥s P(vX_k≥s)≥s(μ_k−s)≥s₀/20≥U/200.

Thus U≤400κ, proving the estimate in either case.

With s=u₁+u₂+u₃, form the downset

\[
K=\bigcup_{x\in T}\prod_{j=1}^3
\left[\frac{u_jx_j}{1+s},\frac{u_j(x_j+1)}{1+s}\right).
\]

It lies in Δ, has positive volume, and its complement is the union of upper orthants based at the scaled minimal excluded exponents of T. Positive diagonal scaling preserves their supports, so the continuous theorem applies. Uniform measure in each equal-volume cell gives mean total coordinate (E[u·X]+s/2)/(1+s). Its continuous deficit is

Under the phase-estimate hypothesis κ≤1/15,
\[
\kappa_c=\frac{\kappa+s}{1+s}\le\kappa+s\le1201\kappa+60v.
\]

Its excluded orthants meet Claim A's hypotheses, so κ_c≥10⁻⁶.

Counting lattice points also gives

m≤binom(floor(1/v)+3,3)≤(1/v+3)³/6,

hence v≤1/((6m)^(1/3)−3) when the denominator is positive.

**Claim B.** If m≥10²⁷, then κ≥6×10⁻¹⁰.

For such m, (6m)^(1/3)>1.8×10⁹, whence v<6×10⁻¹⁰. Were κ<6×10⁻¹⁰, the phase estimate would apply and give

κ_c≤1201κ+60v <1261(6×10⁻¹⁰)=7.566×10⁻⁷<10⁻⁶,

contradicting Claim A.

### 3.3 Completion of Theorem 1

For a minimally four-generated numerical semigroup S=⟨m,a₁,a₂,a₃⟩, the preferred Apéry staircase has the hypotheses of Claim B (the one-interior-corner property is established by disjoint supports of equal-residue boundary reductions). Let M=max Ap(S,m)=c+m−1, and D=3mM−4Σ Ap(S,m). Then

κ=D/(mM),   mW=D−m(m−1),   W=4|S∩[0,c)|−c.

Also a_min>m and lattice-point counting gives

M/m > M/a_min ≥(6m)^(1/3)−3.

For m≥10²⁷, Claim B yields

D/m²=κ(M/m) >(6×10⁻¹⁰)(1.8×10⁹−3)>1.

Hence W>0. This proves Theorem 1. Every four-generator counterexample therefore has multiplicity below 10²⁷. The remaining finite range has not been verified.


## 4. Entirely analytic conductor bound

Let \(S=\langle m,a,b,d\rangle\) be minimally generated, with \(m<a<b<d\), conductor \(c\), \(n=|S\cap[0,c)|\), and \(W=4n-c\). Let \(T\subset\mathbb N^3\) be the preferred Apéry factorization lower ideal, \(|T|=m\), with weight \(w(x,y,z)=ax+by+dz\). Its labels are bijective modulo \(m\). Write

\[
M=\max_Tw=c+m-1,\qquad \Sigma=\sum_Tw,\qquad D=3mM-4\Sigma.
\]

The coordinate-line identity and genus identity are

\[
D=\sum_{\ell}L_\ell(M-w(t_\ell)),\qquad mW=D-m(m-1).
\tag{1}
\]

### 4.1 Full weighted staircases satisfy Wilf

**Theorem.** If \(T=\{x\in\mathbb N^3:w(x)\le M\}\), then \(W\ge0\).

The projection of a full weighted staircase onto its last two coordinates must be one of the following; the elementary classification proof is included immediately below:

\[
\{(0,0),(1,0),(0,1)\},\qquad
\{(0,0),(1,0),(2,0),(0,1)\},\qquad
\{(y,z):y+z\le2\}.
\tag{2}
\]

That classification uses only residue bijectivity and the following elementary support fact. For any minimal excluded point \(p\), its residue representative \(q\in T\) has support disjoint from \(p\). Otherwise subtracting a coordinate present in both gives two distinct points of \(T\) with equal residues. Likewise, minimal excluded points with intersecting supports have different residues. An interior minimal excluded point consequently represents zero and is unique.

### Projection classification proof

**Lemma 2.** Let the full weighted condition hold, let \(a\le b\le d\), and suppose the labels on \(T\) are bijective modulo \(|T|\). If \(T\) contains all three unit vectors, its projection onto coordinates 2 and 3 is one of the following:

1. the union of the two axes, with coordinate heights \((h_2,h_3)=(1,1)\) or \((2,1)\); or
2. \(\{(y,z)\in\mathbb N^2:y+z\le2\}\).

In particular, \(T\) has at most six maximal points.

**Proof.** Put
\[
h_2=\lfloor M/b\rfloor,\qquad h_3=\lfloor M/d\rfloor.
\]
Both are positive. For each \(1\le y\le h_2\), the point
\[
p_y=\left(\left\lfloor\frac{M-by}{a}\right\rfloor+1,\ y,\ 0\right)
\]
is minimal excluded. Its first-coordinate predecessor has weight at most \(M\). Its second-coordinate predecessor also has weight at most \(M\), because \(b\ge a\). Both its positive coordinates are indeed positive, since \(by\le M\).

By the disjoint-support property, the representatives of these \(h_2\) points lie on the third axis. They are distinct, so
\[
h_2\le h_3+1. \tag{7}
\]

If \(M<b+d\), the projection contains no point with both coordinates positive. Also \(M<b+d\le2d\), so \(h_3=1\), and (7) gives \(h_2\le2\). This is alternative 1 and gives at most four columns.

Now suppose \(M\ge b+d\). Then
\[
p=\left(\left\lfloor\frac{M-b-d}{a}\right\rfloor+1,1,1\right)
\]
is an interior minimal excluded point. Its representative is zero, and its support intersects that of every \(p_y\). Consequently none of the \(p_y\) can use the zero residue, which strengthens (7) to
\[
h_2\le h_3. \tag{8}
\]
If \(M\ge2b+d\), the analogous point with last two coordinates \((2,1)\) would be a second interior minimal excluded point. Therefore
\[
M<2b+d\le3d,
\]
and \(h_3\le2\). On the other hand, \(M\ge b+d\ge2b\) gives \(h_2\ge2\). Combining with (8),
\[
h_2=h_3=2.
\]
Thus \(2d\le M<3b\). Every two-coordinate point of total degree at most two has weight at most \(2d\), and every point of total degree at least three has weight at least \(3b\). The projection is exactly the six-point triangle in alternative 2.

Finally, each maximal point of \(T\) must be the top of its first-coordinate column. There are at most six such columns. \(\square\)

The classification alone leaves the six-column alternative possible. The next argument excludes it without a finite search.


### Excluding the six-column triangle

Here is an independently derived short exclusion. Let the column lengths at \((y,z)=(0,0),(1,0),(2,0),(0,1),(1,1),(0,2)\) be \(A,B,C,F,E,G\), respectively. They are positive. The full weighted condition gives

\[
A>B>C,\qquad A>F>G,\qquad E<\min(B,F).
\]

Work in \(\mathbb Z/m\mathbb Z\), writing the weights with the same letters \(a,b,d\), and let \(r\) be the order of \(a\). The interior minimal excluded point \((E,1,1)\) gives

\[
Ea+b+d=0.
\tag{3}
\]

Thus the origin and mixed columns are disjoint sets of residues in the subgroup \(\langle a\rangle\), and \(r\ge A+E\).

The two minimal excluded points \((B,1,0),(C,2,0)\) have representatives permuting \(d,2d\). Neither can represent zero because its support meets the interior point's support. There are two cases.

* If \(Ba+b=2d\) and \(Ca+2b=d\), then eliminating \(b,d\) with (3) yields
  \[
  (B-C+E)a=0.
  \]
  But \(0<B-C+E<A+E\le r\), impossible.
* Therefore \(Ba+b=d\) and \(Ca+2b=2d\). The same argument with \(b,d\) interchanged forces \(Fa+d=b\) and \(Ga+2d=2b\). Consequently all three positive integers
  \[
  B+F,\qquad 2B-C,\qquad 2F-G
  \]
  are multiples of \(r\). Each is less than \(2A\le2r\), so each equals \(r\). Adding the last two and comparing with twice the first gives \(C+G=0\), contradicting positivity.

Thus the third projection in (2) is impossible. This argument actually excludes every residue-bijective lower ideal with that projection and the stated strict column descents; exact floor formulas are unnecessary.

### An analytic boundary inequality

For completeness, the sufficient estimate used below has no finite enumeration input. Put

\[
Z=\{x\in T:M-w(x)<m\},\quad k=|Z|,\quad
P(T)=\sum_{j=1}^3|\pi_jT|,
\]

\[
E(Z)=\sum_{z\in Z}|z|_1-\sum_{j=1}^3\max_{z\in Z}z_j,
\quad \Phi(T,Z)=P(T)-3k-E(Z).
\]

Every point of \(Z\) is maximal, since all generator weights exceed \(m\). Then

\[
\boxed{mW\ge m\Phi(T,Z)+E(Z).}
\tag{4}
\]

To prove it, for a line in direction \(j\) write its top deficit as \(mq+\beta\), \(0\le\beta<m\). With \(A_j=[a_j]_m\), set

\[
R=\sum_{s=0}^{L-1}[sA_j]_m,\qquad
C=|\{0\le s<L:[sA_j]_m+\beta\ge m\}|.
\]

The sum of the residues of point deficits on that line is \(L\beta+R-mC\). Each direction partitions \(T\), whose deficit residues are complete modulo \(m\). Therefore (1) gives

\[
mW=\binom m2+\sum_\ell(mL_\ell q_\ell+mC_\ell-R_\ell).
\]

A line whose top is outside \(Z\) has \(q\ge1\). Its axis residues are distinct, so \(R\le m(L-1)-\binom L2\), and its summand is at least \(m\). There are \(P(T)-3k\) such lines. For lines with tops in \(Z\), discard their nonnegative carry terms. Across these lines, pay once for every distinct positive axis residue from \(\binom m2\). Axis points in different directions have distinct residues because they are distinct points of \(T\). The number of remaining copies is exactly \(E(Z)\), each costing at most \(m-1\). This proves (4).

### The two axis projections

Let \(K=\operatorname{Max}(T)\). For any nonempty subset \(Z\subseteq K\), both \(|Z|\le|K|\) and \(E(Z)\le E(K)\): in each coordinate, adding a point increases the sum at least as much as it increases the maximum. Thus

\[
\Phi(T,Z)\ge\Phi(T,K).
\tag{5}
\]

For the three-column projection, let the lengths be \(A,B,C\) at \((0,0),(1,0),(0,1)\). Full weightedness gives \(A>B,C\ge1\), so the three column tops are precisely \(K\), and \(A\ge2\). Direct counting gives

\[
m=A+B+C,\quad P(T)=3+2A+B+C=3+A+m,
\]
\[
E(K)=m-A-2,\qquad \Phi(T,K)=2A-4\ge0.
\]

For the four-column projection, let the lengths be \(A,B,C,F\) at \((0,0),(1,0),(2,0),(0,1)\). Full weightedness gives \(A>B>C\ge1\), \(A>F\ge1\). Again the column tops are precisely \(K\), and \(A\ge3\). Now

\[
m=A+B+C+F,\quad P(T)=4+2A+B+C+F=4+A+m,
\]
\[
E(K)=m-A-2,\qquad \Phi(T,K)=2A-6\ge0.
\]

Equations (4) and (5) prove \(W\ge0\) in both cases, completing the theorem.

### 4.2 Completion of the conductor reduction

If \(p\) is a minimal excluded exponent with \(w(p)\le M\), its predecessor coordinate lines contribute exactly

\[
\sum_{j:p_j>0}p_j\bigl(M-w(p-e_j)\bigr)
=M+(|p|_1-1)(M-w(p))\ge M.
\]

Their contributions are distinct for different minimal excluded points: selecting the same line in a fixed direction would make the two excluded points comparable, contradicting their minimality. Thus, if \(H\) such points exist,

\[
D\ge HM+\sum_{\substack{p\text{ minimal excluded}\\w(p)\le M}}
(|p|_1-1)(M-w(p)).
\tag{6}
\]

If \(W<0\), the theorem shows that the staircase is not full weighted, so \(H\ge1\). Integrality and (1) give \(D\le m(m-2)\), whence

\[
M\le m(m-2),\qquad
\boxed{c\le m^2-3m+1},\qquad
\boxed{d\le m(m-2)}.
\]

More generally, a putative counterexample with \(H\) low-weight minimal excluded points satisfies

\[
\boxed{c\le\left\lfloor\frac{m(m-2)}{H}\right\rfloor-m+1}.
\]

The extra nonnegative sum in (6) strengthens this further when omitted corners are substantially below \(M\). No universal lower bound \(H\ge2\) is established here, and these conductor estimates alone do not bound multiplicity. Theorem 1 supplies that separate bound.



## 5. Supplementary slab and compressed-cell bounds


The following supplementary argument gives a separate restriction on any remaining counterexample. Its dimension parameter d=e−1 is local to this section.

### 5.1. Setup

In this section \(W_e=e|S\cap[0,c)|-c\) is the Wilf number for embedding dimension \(e\).

Let `d=e−1≥2`, and let `T⊂N^d` be any finite lower ideal, with positive weights `a_1,…,a_d`. Write

\[
m=|T|,\quad w(x)=a\cdot x,\quad M=\max_Tw,\quad
D=d mM-(d+1)\sum_Tw.
\]

For coordinate direction `j`, let
\[
D_j=\sum_{\ell\parallel e_j}|\ell|\,[M-w(t_\ell)].
\]
The coordinate-line identity gives `D=Σ_jD_j`, with every `D_j≥0`.

If `T` is a preferred Apéry staircase of a minimally e-generated numerical semigroup with multiplicity `m`, then `a_j≥m+1`, and
\[
mW_e=D-\frac{d-1}{2}m(m-1).
\]
All geometric inequalities below precede, and do not require, residue bijectivity.

### 5.2. Exact decomposition into slabs

Fix a coordinate `i` with weight `b=a_i`. Write the nonempty nested slices perpendicular to it as `F_z`. Partition them into maximal consecutive runs of identical slices. A run is described by

- initial level `r`;
- length `L≥1`;
- the common `(d−1)`-dimensional lower ideal `F`, of size `A`.

Let `v` denote the weight in the other coordinates, and put
\[
M_F=\max_Fv,\quad\Sigma_F=\sum_Fv,\quad
\delta_F=(d-1)AM_F-d\Sigma_F\ge0,
\]
\[
g_F=M-M_F-b(r+L-1)\ge0.
\]
The nonnegativity of `δ_F` is the coordinate-line identity in dimension `d−1`. The last slice of the run contains a point of weight `M_F+b(r+L−1)`, proving `g_F≥0`.

At slice `r+s`, the sum of all coordinate-line contributions in the directions other than `i` is
\[
(d-1)A[M-b(r+s)]-d\Sigma_F
=\delta_F+(d-1)A g_F+(d-1)Ab(L-1-s).
\]
Summing `s=0,…,L−1` and then the runs gives the exact identity
\[
\boxed{D-D_i=\sum_{\text{runs}}\left[
L\delta_F+(d-1)ALg_F+\frac{d-1}{2}AbL(L-1)\right].}
\]
Define
\[
P_i=\sum_{\text{runs}} A L(L-1).
\]
Every omitted term is nonnegative, so
\[
\boxed{D-D_i\ge\frac{d-1}{2}a_iP_i.}\tag{1}
\]
Summing over all `i`, each `D_j` occurs exactly `d−1` times on the left. Therefore
\[
\boxed{2D\ge\sum_{i=1}^d a_iP_i.}\tag{2}
\]

### 5.3. Wilf consequences

For an Apéry staircase, equation (1) implies
\[
mW_e\ge\frac{d-1}{2}\left[(m+1)P_i-m(m-1)\right].
\]
Thus `P_i≥m−2` implies Wilf: the displayed bound gives `mW_e≥−(d−1)`, and `m≥d+1` excludes a negative integer `W_e`. Also, `P_i≥m−1` implies `W_e≥1`, and `P_i≥m` implies `W_e≥d−1=e−2`.

A direction with projection size `A` and shortest column length `h` has an initial run of length `h`. Consequently
\[
\boxed{Ah(h-1)\ge m-2\quad\Longrightarrow\quad W_e\ge0.}\tag{3}
\]
This strengthens the checkpoint's sufficient criterion `2A(h−1)≥m`. For `h≥2`, `h(h−1)≥2(h−1)`, and improvement is strict for `h>2`. The new required bottom thickness grows like the square root of the mean column length. The full statistic `P_i` also uses runs above the bottom, and so handles long insertions on proper subsets of columns.

In dimension four, (2) additionally gives
\[
\boxed{\sum_{i=1}^3 a_iP_i\ge2m(m-1)\quad\Longrightarrow\quad W_4\ge0.}\tag{4}
\]

### 5.4. Every fixed compressed shape admits a finite reduction

For each coordinate `i`, take the distinct values `z_i+1` at the coordinatewise maximal points `z` of `T`, together with zero. These partition the coordinate range into consecutive intervals. Every Cartesian product of these intervals lies either entirely in `T` or entirely outside it, since `T` is the union of the boxes `[0,z]`.

These coordinate intervals are exactly the constant-slice runs used above. Indeed, a maximal point `z` forces a change after slice `z_i`, because its projection is present there and cannot be present at `z_i+1`. Conversely any slice change has a disappearing projected point; extend its top to a maximal point, whose `i`-coordinate must equal that top level.

Call each occupied Cartesian product a cell, and let `K` be the number of occupied cells. Replacing each interval by one coordinate level gives a compressed lower ideal with `K` points. Its pattern remains fixed under arbitrary positive integer changes to all interval lengths.

For a cell with side lengths `L_1,…,L_d`, let `v=∏_iL_i` be its volume. The slab definition gives exactly
\[
\sum_iP_i=\sum_{\text{cells}}v\left(\sum_iL_i-d\right).\tag{5}
\]

For positive integer lengths,
\[
\boxed{v\left(2d+1-\sum_iL_i\right)\le2^d.}\tag{6}
\]
To prove this, write `Σ_iL_i=d+r`. For `r≥d+1` the left side is nonpositive. For `0≤r≤d`, integer balancing gives `v≤2^r`: the maximum product consists of `r` lengths equal to 2 and the remaining lengths equal to 1. The left side is therefore at most `(d+1−r)2^r≤2^d`, the last inequality being `u+1≤2^u` for `u=d−r≥0`.

Summing (6) and using (5) proves
\[
\boxed{\sum_iP_i\ge(d+1)m-2^dK.}\tag{7}
\]
Combining with (2) and `a_i≥m+1`,
\[
\boxed{mW_e\ge m^2+d m-2^{d-1}K(m+1).}\tag{8}
\]
In particular:

1. If `m≥2^(d−1)K`, then `W_e≥d−1`.
2. If `m≥2^(d−1)K−d+1`, then the right side of (8) is at least `−(d−1)`. Since `m≥e=d+1` and `mW_e` is an integer multiple of `m`, a negative Wilf number is impossible.

Hence
\[
\boxed{e=4,\quad m\ge4K-2\quad\Longrightarrow\quad W_4\ge0.}\tag{9}
\]
For each fixed compressed pattern, a counterexample therefore requires `m≤4K−3`. There are only finitely many positive integer interval lengths producing that many points; consequently arbitrary simultaneous coordinate stretches reduce to finitely many actual lower ideals.

If there are `q` maximal points, each coordinate has at most `q` intervals, so `K≤q^d`. In dimension four this gives the coarse necessary condition `m≤4q^3−3` for a counterexample. This counts all maximal points of the selected factorization staircase. It neither bounds that number universally nor equates it with numerical-semigroup type or the final-window cardinality.

### 5.5. Exact examples separating the criteria

#### Stronger initial-run criterion

For `S=⟨23,98,258,272⟩`, exact preferred Apéry computation gives `c=838`, `W=670`.

| Direction weight | Projection size A | Shortest length h | Old 2A(h−1) | New Ah(h−1) |
| --- | ---: | ---: | ---: | ---: |
| 98 | 5 | 3 | 20 | 30 |
| 258 | 17 | 1 | 0 | 0 |
| 272 | 13 | 1 | 0 | 0 |

The old criterion fails in every direction. The new criterion succeeds in the 98 direction.

#### Runs above the bottom

For `S=⟨27,232,302,314⟩`, exact preferred Apéry computation gives `c=1764`, `W=1560`.

| Weight | A | h | Old 2A(h−1) | New bottom Ah(h−1) | Full P_i |
| --- | ---: | ---: | ---: | ---: | ---: |
| 232 | 14 | 1 | 0 | 0 | 0 |
| 302 | 10 | 2 | 20 | 20 | 32 |
| 314 | 11 | 1 | 0 | 0 | 48 |

Both bottom criteria fail in all directions. In the 314 direction, the slice runs `(r,L,A)` are `(0,1,11)` and `(1,4,4)`, giving `P_i=48≥27`. This illustrates the additional gain from a long run on a proper subset of columns.

These examples demonstrate a stronger criterion relative to the checkpoint; they are not claimed as semigroups previously unknown to satisfy Wilf.

### 5.6. Verification and remaining limitation

`slab_bound.py` verifies the exact decomposition, its inequalities, and the Apéry moment formula by integer arithmetic. The initial run checked 300 random lower ideals in dimensions 3, 4, and 5, together with 25 minimally four-generated semigroups, producing ten examples where the old theorem fails in all axes and the new theorem succeeds. These computations are checks of an analytic proof, not proof of a universal conclusion.

The finite reduction applies after fixing the compressed staircase pattern. The number and structure of compressed patterns remain unbounded. In particular, shapes whose slices change at every level can have `P_i=0`. The slab argument alone does not control all such patterns. Theorem 1 independently bounds total multiplicity; the finite region left by the combined results is still unresolved.

Independent audit: the full-weighted agent checked the slab decomposition, compressed-cell identity, discrete product bound, and integer endpoint. The weaker single-direction threshold `P_i≥m−2` was added following that audit.

### 5.7. A seven-point zero-insertion family is arithmetically impossible

This secondary lemma illustrates why the lattice condition remains useful beyond six points. For each integer `t≥0`, consider the height array

\[
\begin{pmatrix}
t+6&t+5&t+4\\
t+5&t+3&t+3\\
t+4&t+3&0
\end{pmatrix}.
\]

The resulting lower ideal has `m=8t+33` points, one interior minimal excluded point `(1,1,t+3)`, and seven maximal points. Their two-coordinate projection has maxima 2 and 2, so translating all seven maximal points by one in the height direction changes the projection-count score by `2+2+3−7=0`.

Nevertheless no member of this infinite family admits residue-bijective linear labels modulo its size. Suppose the coordinate residues are `A,B,C`. The two mixed minimal corners in the `xz` plane are `(1,0,t+5)` and `(2,0,t+4)`. Their representatives lie on the y-axis, are distinct, and cannot be zero: both corner supports intersect that of the interior corner, whose representative must be zero. They therefore represent a permutation of the only two nonzero y-axis points. Summing gives

\[
3A+(2t+9)C\equiv3B\pmod m.
\]

The symmetric `yz` argument gives
\[
3B+(2t+9)C\equiv3A\pmod m.
\]

Adding and doubling implies `(8t+36)C≡0`. Since `m=8t+33`, this gives `3C≡0`. But `0` and `3e_z` both lie in the ideal, contradicting residue injectivity.

This generalizes a specific obstruction beyond the six-point argument, using the same saturated-axis-permutation mechanism as the checkpoint's three-face exclusion. It is not required for the slab theorem.


## 6. What was checked, what failed, and what remains

The global proof was audited separately by two additional mathematical reviewers in this session. They checked the line identities, the minimum-coordinate slicing argument, all three propagation rectangles, the support contradiction, the phase estimate, the cardinality inversion, and the final threshold. The root also independently checked these steps. This is proof review within this research session, not external peer review.

All numerical constants are terminating decimals used as exact rationals. The included standard-library checker verifies their strict inequalities. It also computes Apéry invariants using shortest paths and independently counts semigroup membership for selected diagnostic fixtures. These checks verify constants and expose implementation or example errors; they do not replace the analytic proofs or enumerate the remaining box.

Exploratory computation optimized 1,200 pair-constraint shapes and checked ordered geometric certificates for 2,162 randomly proposed minimally four-generated semigroups. All of those semigroups passed the geometric sufficient test. This observation is not used in either main theorem and establishes no universal assertion. The scripts and results are retained in the companion archive.

Three tempting stronger statements were rejected. The total length of lines with nonmaximal tops need not be at least m−1: the genuine semigroup ⟨23,181,189,192⟩ gives 20 rather than 22. The geometric bound D≥(m−10)M/3 is also false: for T_R={x∈N³:|x|₁≤R, x₁x₂x₃=0} with equal weights, m=1+3R(R+1)/2 and D/M=(R−1)(R−2)/2, so m−3D/M=6R−2 is unbounded. Such abstract shapes need not admit Apéry residue labels. Finally, the apparently useful strengthening D≥(m−1)a_min fails even for a genuine semigroup: ⟨16,49,52,53⟩ has D=624<735=(m−1)a_min, while W=24>0. This prevents replacing the remaining Wilf inequality by that stronger assertion.

The exact unresolved objective is to exclude every minimal four-generator tuple in (R), or to find one with W<0. Neither the stability proof nor the finite reduction supplies that last step. The threshold 10²⁷ is deliberately coarse, and the residual problem requires stronger mathematics; no feasible exhaustive computation of the entire stated region has been carried out. No extension to all higher embedding dimensions is asserted in this note.

## 7. References and provenance

1. A. Zhai, *An asymptotic result concerning a question of Wilf*, arXiv:1111.2779 (2011), especially Lemma 3 and the concluding questions. https://arxiv.org/pdf/1111.2779
2. M. Hellus, A. Rechenauer, R. Waldi, *Variants on a question of Wilf*, arXiv:1804.06141 (2018), especially Propositions 2.5–2.6. https://arxiv.org/pdf/1804.06141
3. M. F. Marashdeh, *An upper bound for the type of a numerical semigroup, and a reduction of Wilf’s conjecture*, arXiv:2608.12531v1 (12 August 2026). Its introduction records the known multiplicity and genus ranges and explicitly leaves Wilf unresolved. https://arxiv.org/html/2608.12531v1
4. J. Kliem and C. Stump, *A New Face Iterator for Polyhedra and for More General Finite Locally Branched Lattices*, Discrete & Computational Geometry (2022), for the multiplicity-at-most-19 result. https://doi.org/10.1007/s00454-021-00344-x
5. W. Bruns, P. A. García-Sánchez, C. O’Neill, D. Wilburne, *Wilf’s conjecture in fixed multiplicity*, International Journal of Algebra and Computation 30 (2020), 861–882. https://doi.org/10.1142/S021819672050023X

The Apéry representation, lower-ideal inequality, and excluded-corner restriction are prior work. The explicit stability argument, its global multiplicity cutoff, the analytic removal of the conductor bound’s computational dependency, and the slab estimates are derivations made in this research session. A targeted primary-source search did not locate the same global cutoff or a previously established positive asymptotic gap, but this is not a claim of publication priority.

Historical clarification: the standard unrestricted three-generator attribution is Fröberg–Gottlieb–Häggkvist (1987), rather than the mid-twentieth century. A counterexample in embedding dimension four would disprove the overall conjecture; it would not by itself establish a counterexample in every larger exact embedding dimension.
