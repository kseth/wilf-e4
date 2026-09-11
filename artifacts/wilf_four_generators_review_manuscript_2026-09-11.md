# Wilf's inequality for four generators

## A proposed computer-assisted proof, explicit centroid witnesses, and dimensional limits

**Review manuscript · 11 September 2026**

### Abstract

We organize a proposed computer-assisted proof of Wilf's inequality for numerical semigroups of embedding dimension four. The main simplification is a pair of explicit, weight-independent centroid constructions: move coordinate-line endpoints upward by at most two steps, or combine the axis endpoints. For the specified residual class, exact finite verification shows that one construction always succeeds. This strengthens the normalized moment bound to \(D_0\ge m\), removes two auxiliary hypotheses, and replaces per-ideal linear-programming certificates with direct formulas.

The manuscript gives the complete case partition and identifies each retained analytic or computational dependency. It also proves the centroid criterion directly for infinite clipped-box and clipped-prism families. The moment identity and witness formulas extend to all embedding dimensions, but their coverage does not. Equality examples rule out the strongest unrestricted centroid statement, and two actual five-generator Apéry ideals exhibit geometric obstructions to a direct extension.

**Status.** This is a proposed research proof with completed exact checks and in-session audits. External mathematical review and proof-assistant formalization remain outstanding. The main manuscript is a readable synthesis; the accompanying technical archive contains the detailed retained proofs, source code, certificates, and replay records. No unrestricted theorem for five or more generators is claimed.

## 1. Main claim and notation

A numerical semigroup is a cofinite additive submonoid \(S\subseteq\mathbb N\), where \(\mathbb N\) includes zero. Its multiplicity \(m\) is its smallest positive element, its conductor \(c\) is the least integer with \(c+\mathbb N\subseteq S\), and its embedding dimension \(e\) is the number of minimal generators. Put \(n=|S\cap[0,c)|\). Wilf's inequality is \(en\ge c\).

**Proposed theorem.** Every minimally four-generated numerical semigroup satisfies
\[
W_4(S)=4n-c\ge0.
\]
The logical coverage is given in Section 3. The stronger strict inequalities below apply only to the indicated subclasses.

Write \(S=\langle m,a_1,a_2,a_3\rangle\). The Apéry set is
\[
\operatorname{Ap}(S,m)=\{w\in S:w-m\notin S\}.
\]
Choose the lexicographically least factorization in \(a_1,a_2,a_3\) of each Apéry element, and let \(T\subseteq\mathbb N^3\) be the resulting exponent set. These representatives form a lower ideal: if \(y\le x\in T\), its label is Apéry, and any lexicographically earlier factorization of \(y\)'s label would also give an earlier factorization of \(x\)'s label. The labels \(a\cdot x\) represent all residues modulo \(m\) exactly once; hence \(|T|=m\).

Set
\[
A=\min_i a_i\ge m+1,\quad b=a/A,\quad s=\sum_{x\in T}x,
\]
\[
M=\max\operatorname{Ap}(S,m)=c+m-1,\quad H=M/A,\quad
R=\max_{x\in T}|x|_1,
\]
\[
D_0=3mH-4b\cdot s,\qquad D=AD_0.
\]
The Apéry genus formula gives
\[
\boxed{mW_4=AD_0-m(m-1).} \tag{G1}
\]
Indeed, the genus \(g=|\mathbb N\setminus S|\) satisfies \(g=(a\cdot s)/m-(m-1)/2\), and \(n=c-g\). The inequality \(H\ge R\) follows from \(b_i\ge1\).

### Arithmetic structure of the ideal

A minimal excluded point is an exponent outside \(T\) whose immediate predecessors in every positive coordinate belong to \(T\). Such a point and its included residue representative have disjoint supports: subtracting a common positive coordinate would otherwise give two distinct included points of the same residue. Distinct minimal exclusions sharing a positive coordinate likewise have different residues.

Consequently there is at most one full-support minimal exclusion \(p\). If it exists, its residue representative is zero. Every other minimal exclusion has support at most two. Intersecting the three coordinate-plane cylinders and deleting \(p+\mathbb N^3\) therefore reconstructs \(T\) exactly.

Two necessary restrictions will be used in the finite centroid theorem. Write \(p=(r,s,t)\) temporarily and \(n_i=1+\max_Tx_i\).

First, each plane has at most \(|p|_1-2\) mixed minimal exclusions. In the first two coordinates, let \(q=(u,v,0)\) be such an exclusion. Its representative is \(\gamma e_3\). Exclusions with \(u<r\) or \(v<s\) contribute at most \(r-1+s-1\), since mixed corners have distinct first coordinates and distinct second coordinates. Otherwise \(q-(r,s,0)\) is a nonzero point of \(T\), with the same residue as \((\gamma+t)e_3\). If \(\gamma+t<n_3\), residue injectivity is violated. Thus \(\gamma\ge n_3-t\), leaving at most \(t\) distinct representatives. The total is at most \(r+s+t-2\). This bound applies separately in each plane.

Second, define the exposed surfaces
\[
F_i=\{x\in T:x+e_i\notin T\}.
\]
Mixed excluded corners in planar slices inject by their residues into the complementary axis. A nonempty planar lower ideal has one more maximal point than mixed excluded corners. Summing over the \(n_k\) nonempty slices gives
\[
|F_i\cap F_j|\le2n_k,\qquad\{i,j,k\}=\{1,2,3\}. \tag{G2}
\]
Detailed versions of these predecessor arguments are retained in the archive. No erosion assumption is needed for the primary centroid theorem.

## 2. Explicit centroid witnesses

### The centroid target

For a finite lower ideal \(T\subset\mathbb N^3\), write
\[
m=|T|,\qquad s=\sum_{x\in T}x.
\]
A point \(z\in\operatorname{conv}(T)\) with
\[
r=3mz-4s\ge0\quad\text{coordinatewise},\qquad
\sum_i r_i\ge m
\tag{C1}
\]
proves the desired inequality for every real vector \(b_i\ge1\). Indeed, with
\(H=\max_{x\in T}b\cdot x\),
\[
3mH-4b\cdot s
\ge b\cdot(3mz-4s)
\ge\sum_i r_i
\ge m.
\tag{C2}
\]
The first step is convexity and the second is coordinatewise nonnegativity.
No height cutoff or relation between the weights is used.

### First construction: local moves from coordinate-line tops

For each nonempty coordinate line \(\ell\) of \(T\), let \(L_\ell\) be its
number of points and \(t_\ell\) its top endpoint. Include lines in all three
directions. Since every such line is an initial interval,
\[
\sum_\ell L_\ell=3m,\qquad
\sum_\ell L_\ell t_\ell=4s.
\tag{C3}
\]
For the second identity, fix a coordinate \(i\). Lines parallel to \(i\)
contribute \(2s_i\); lines in each of the other two directions contribute
\(s_i\). This proves (C3) coordinate by coordinate.

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
Equation (C3) gives
\[
3mz_{\rm local}-4s
=\sum_\ell L_\ell(u_\ell-t_\ell)\ge0,\qquad
\sum_i(3mz_{\rm local}-4s)_i=U_2(T).
\tag{C4}
\]
Thus \(U_2(T)\ge m\) supplies the required witness.

This construction needs neither a search for a farthest maximal point nor a
linear program. A fixed rule can break ties between equally good local moves.

For comparison, allowing arbitrary-length monotone moves gives
\[
U(T)=\sum_\ell L_\ell
\left(\max_{u\in T,\ u\ge t_\ell}|u|_1-|t_\ell|_1\right)\ge U_2(T).
\]
The finite theorem below uses \(U_2\).
The even cheaper one-step gain is
\[
U_1(T)=3m-\sum_{u\in\operatorname{Max}(T)}(|u|_1+3),
\]
obtained by moving every nonmaximal line top once. One step does not suffice
for the final alternative, so the two-step allowance is material.

### Second construction: the axis simplex

Let
\[
q_i=\max_{x\in T}x_i>0,\qquad q_*=\max_i q_i,\qquad
G(T)=q_*\left(3m-4\sum_i\frac{s_i}{q_i}\right).
\tag{C5}
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
\tag{C6}
\]
Hence it also proves (C1).

Both constructions are valid for any finite lower ideal with positive axis
lengths. Only the assertion that at least one reaches the target needs the
additional structural hypotheses below.

### The simplified finite theorem

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
\tag{C7}
\]
Equations (C4) and (C6) then give the centroid witness (C1).

The previous erosion test and the bound on plane corners dominating the
projection of \(p\) are absent from this theorem's hypotheses. The total
mixed-corner bound remains. Although its earlier proof used a refined
counting argument, that refined condition is no longer part of the finite
enumeration or centroid lemma.

The local construction alone reaches \(m\) on **5,574,213** shapes; the axis
construction handles the remaining **431**. The two constructions can both
succeed on the same shape, so their separate success counts should not be
added. All 431 fallback witnesses have been reconstructed explicitly.

#### Finite coverage

After sorting the coordinates of \(p\), the larger class has these counts:

| Corner | Ideal/profile cases | Axis fallbacks |
|---|---:|---:|
| \((1,1,3)\) | 1,581,961 | 215 |
| \((1,2,2)\) | 1,433,543 | 212 |
| \((1,1,4)\) | 874,540 | 3 |
| \((1,2,3)\) | 638,574 | 1 |
| \((2,2,2)\) | 592,453 | 0 |
| \((1,1,5)\) | 159,580 | 0 |
| \((1,2,4)\) | 105,119 | 0 |
| \((1,3,3)\) | 94,500 | 0 |
| \((2,2,3)\) | 94,374 | 0 |
| **Total** | **5,574,644** | **431** |

These are ideal/profile cases after sorting the full corner, not numerical semigroups or all coordinate-permutation orbits. The weaker hypotheses enlarge the class; the simplification is in the witnesses and checking machinery.

The verifier enumerates compatible planar lower profiles, removes the upper
orthant of \(p\), checks the stated restrictions, and evaluates (C7) with integer
arithmetic. Rational axis expressions are cleared by a positive common
denominator. It reads no per-shape certificate stream.

The separate implementations construct the shapes using bitsets and literal
column heights, respectively. Their complete counts agree. The independent
local verifier computes \(h_2\) by membership tests rather than importing a
producer's dynamic program or geometric data.

#### A shorter Wilf deduction

For a genuine minimally four-generated semigroup,
\[
A=\min(a_1,a_2,a_3)\ge m+1,\quad b=a/A,\quad
D_0=3mH-4b\cdot s,\qquad D=AD_0.
\]
The exact Apéry identity is
\[
mW_4=AD_0-m(m-1).
\]
Using \(D_0\ge m\) gives
\[
mW_4\ge m(A-m+1)\ge2m,
\qquad\boxed{W_4\ge2.}
\tag{C8}
\]
The high-height comparison in Section 3 is unnecessary for this residual low-degree class.

The earlier small-multiplicity, no-full-corner, exceptional-corner, and
high-height arguments remain dependencies of the global four-generator proof.
The present constructions simplify the residual centroid branch.

## 3. Composition of the four-generator argument

First handle \(m\le29\). For \(m\ge30\), divide by the unique full-support corner, and only then divide the residual case by integer degree.

| Case | Exact input | Result used |
|---|---|---|
| \(m\le19\) | Published small-multiplicity theorem | \(W_4\ge0\) |
| \(20\le m\le29\) | Analytic negative-case conductor reduction, then complete generator-box verification | \(W_4\ge0\) |
| \(m\ge30\), no full-support corner | Weighted no-interior theorem | \(D_0\ge m-1\), hence \(W_4\ge1\) |
| \(m\ge30\), \(p=(1,1,1)\) | At most six maxima; six-final-window theorem | \(W_4\ge0\) |
| \(m\ge30\), \(p\) a permutation of \((2,1,1)\) | Short-corner weighted theorem | \(D_0\ge m-1\), hence \(W_4\ge1\) |
| \(m\ge30\), \(\vert p\vert _1\ge5\), \(R\le6\) | Local-or-axis centroid lemma and necessary surface/plane-corner restrictions | \(D_0\ge m\), hence \(W_4\ge2\) |
| \(m\ge30\), \(\vert p\vert _1\ge5\), \(R\ge7\) | \(H\ge R\ge7\), then high-height one-corner theorem | \(D_0\ge m-29/10\), hence \(W_4\ge0\) |

The rows are exhaustive because a positive integer triple has coordinate sum at least three; the only sum-three triple is \((1,1,1)\), and the only sum-four type is \((2,1,1)\). Integer degree is either at most six or at least seven. There is no omitted height boundary: the last row includes \(H=7\), while the penultimate row works at *every* normalized height.

The four-generator theorem is a composition of these named results. Its conclusion is nonnegativity; strict positivity has only been derived in the displayed subclasses.

### Small multiplicities and analytic conductor reduction

The published input is [Bruns, García-Sánchez, O’Neill and Wilburne](https://arxiv.org/abs/1903.04342) through multiplicity 18 and [Kliem and Stump](https://arxiv.org/abs/1905.01945) for multiplicity 19.

For a genuine four-generator numerical semigroup,

\[
\boxed{W_4<0\ \Longrightarrow\ M\le m(m-2).} \tag{G3}
\]

Consequently every generator other than \(m\) is at most \(m(m-2)\), since each is an Apéry element. For each \(m=20,\ldots,29\), one may therefore enumerate exactly

\[
m<a_1<a_2<a_3\le m(m-2).
\]

The conductor is correspondingly at most \(m^2-3m+1\). The proof of (G3) is analytic: a full weighted ideal \(T=\{x\in\mathbb N^3:a\cdot x\le M\}\) is first proved to satisfy Wilf; otherwise a minimal excluded point of weight at most \(M\) forces \(D\ge M\), while negative integer \(W_4\) gives \(D\le m(m-2)\). It does not rely on the six-point enumeration or on a large-multiplicity theorem.

Detailed proofs, implementation sources, and completed records are indexed in the accompanying proof map.

The two full arithmetic programs cover **301,098,092** sorted generator triples and **180,719,029** minimal four-generator numerical semigroups in the proved boxes. Positive minima in those boxes do not prove strict positivity for generators outside the boxes: (G3) excludes only a negative case.

### No full-support corner

**Abstract weighted theorem.** If \(T\subset\mathbb N^3\) is a finite lower ideal containing the coordinate units, with no full-support minimal exclusion and \(|T|=m\ge30\), then

\[
3m\max_T a\cdot x-4a\cdot s\ge a_{\min}(m-1).
\]

This theorem does not require residue labels. It uses the central-box/three-horn structural theorem, the continuous no-interior bound, the general phase inequality, the degree-four cardinality bound 29, and a closed real-parameter interval certificate on \(1\le b\le c\le H\), \(5\le H\le24\).

Detailed proofs, implementation sources, and completed records are indexed in the accompanying proof map.

Recorded complete coverage: **50,885 nodes**, **24,912 DP leaves**, **531 analytic leaves**, zero unresolved leaves. The second independent DP implementation uses explicit rectangle transitions; distinguish its leaf replay from the separate tree-coverage proof.

### The corner \((1,1,1)\)

When \(p=(1,1,1)\), every mixed corner of a coordinate plane must represent the terminal point on the complementary axis. Residue injectivity therefore allows at most one mixed corner in each plane. Since every included point has a zero coordinate, the whole ideal has at most six maximal points.

Let \(Z=\{x\in T:M-a\cdot x<m\}\). Every point of \(Z\) is maximal, so \(|Z|\le6\). The six-final-window theorem gives \(W_4\ge0\).

Detailed proofs, implementation sources, and completed records are indexed in the accompanying proof map.

The sufficient verification route is compression, all admissible insertions and extensions, all ordered residue-bijective labelings, then **all modular cuts**. It covers arbitrary integer lifts and equality walls. It need not retain auxiliary LP certificates. The six-point arithmetic record has **930** ordered residue labelings and **23,002** modular-cut checks; the complete runner additionally covers \(|Z|\le5\).

This remains a dependency of the exceptional-corner branch. The residual low-degree branch uses the explicit centroid theorem instead.

### The corner \((2,1,1)\) and permutations

**Genuine short-corner theorem.** For the preferred Apéry ideal of a minimally four-generated semigroup, if \(m\ge30\) and \(p\) is a permutation of \((2,1,1)\), then \(D_0\ge m-1\).

Its preferred proof has two parts:

1. A generic geometric inequality for normalized height \(H\ge6\), using planar slicing, phase compactness \(H<42\) for a failure, and an exact closed interval certificate.
2. If \(H<6\), degree is at most five; necessary residue restrictions yield **70,175** eligible shapes, of which **28,499** have cardinality at least 30. Their exact rational centroid duals establish the same bound for all real normalized weights.

Detailed proofs, implementation sources, and completed records are indexed in the accompanying proof map.

The interval replay covers **110,865 nodes**, **54,978 DP leaves**, **455 analytic leaves**, and **164,934** corner-placement bounds, with no unresolved region. The rational low-height record verifies all **28,499** shapes.

The archived short-corner generator enumeration is an alternative, not a dependency of this chosen route.

### Residual degree at most six

The theorem in Section 2 applies. The lower bound on the corner sum is the definition of the residual branch; its upper bound is automatic because each predecessor of the corner has degree at most six. The two arithmetic restrictions were proved in Section 1. Thus the conclusion is \(D_0\ge m\), for every normalized weight vector, regardless of height.

### Residual high degree

**Abstract high-height theorem.** If \(T\subset\mathbb N^3\) is a finite lower ideal with exactly one full-support minimal excluded point \(p\), \(|p|_1\ge5\), and positive weights of minimum one, then

\[
H\ge7\quad\Longrightarrow\quad D_0\ge m-29/10.
\]

No residue, cardinality, plane-corner, surface, or erosion restriction is needed for this geometric theorem. Its infinite-to-finite reduction uses the phase inequality and the continuous gap \(5/42\) to place any failure in \(1\le b\le c\le H\), \(7\le H<78\). The certificate covers the corresponding closed root box through 78.

Detailed proofs, implementation sources, and completed records are indexed in the accompanying proof map.

The continuous gap retains an exact finite-strip dependency: allowances **18, 19, 20, 21**, with **1,029** sorted corner configurations in total. The high-height tree has **94,459 nodes**: **47,229 splits**, **47,088 DP leaves**, **142 empty leaves**. The fresh no-cache replay recomputed **35,852,138** full Cartesian corner cases, with zero unresolved nodes and zero cached checks. Its certificate hash is preserved in the proof map and archive manifest.

### Final arithmetic

If \(D_0\ge m-1\), equation (G1) gives

\[
mW_4\ge(A-m)(m-1)>0,
\]

so integrality yields \(W_4\ge1\). If \(D_0\ge m\), it gives

\[
W_4\ge A-m+1\ge2.
\]

For the weaker high-height bound, suppose \(W_4<0\). As \(W_4\) is an integer,

\[
D_0\le\frac{m(m-2)}A\le\frac{m(m-2)}{m+1}
=m-3+\frac3{m+1}.
\]

Hence, when \(m\ge30\),

\[
m-D_0\ge\frac{3m}{m+1}\ge\frac{90}{31}>
\frac{29}{10},\qquad \frac{90}{31}-\frac{29}{10}=\frac1{310}.
\]

This contradicts the high-height theorem. The distinction between this integer-negativity argument and the stronger direct positive bound should be retained.

These implications complete the proposed case composition, conditional on the retained theorems and finite verifications whose proofs and records accompany this manuscript. The reading text does not replace those technical dependencies.

## 4. Analytic families without enumeration

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

## 5. Extensions to higher embedding dimensions

The formulas below distinguish general identities from sufficient structural families and unproved coverage claims. No novelty claim is made for the identities or special families.

### The arithmetic and centroid formulations in arbitrary dimension

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

### Both explicit centroid constructions extend formally

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

### An analytic higher-dimensional family: corner-clipped boxes

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

### Arithmetic restrictions that survive in every dimension

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

### Two genuine obstructions to extending the three-coordinate geometry

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

### The separate proposed fixed-dimension finite reduction

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

## 6. Simplifications, evidence, and remaining limitations

### What has become simpler

The primary residual lemma is now a statement about two explicit quantities, \(U_2(T)\) and \(G(T)\). Its proof uses elementary convex combinations; it needs no per-shape LP bases, determinants, or rational certificate stream. The stronger bound \(D_0\ge m\) gives \(W_4\ge2\) directly in that class. The erosion and refined dominating-corner filters have been removed from this lemma, though related restrictions remain in other arguments.

The global partition uses integer degree: \(R\le6\) invokes the explicit witnesses, while \(R\ge7\) implies \(H\ge7\). This avoids a weight-dependent boundary in the primary centroid computation. Earlier eventual-multiplicity thresholds, duplicate low-height certificate streams, and alternative short-corner generator searches are not needed simultaneously. Their records are retained as history and alternative evidence.

A complete proof without finite computation has not been obtained. The exact unresolved *simplification target* is to prove structurally that the stated residual corner and surface hypotheses force
\[
\max\{U_2(T),G(T)\}\ge|T|.
\]
This implication has been checked exhaustively on the finite class; it is not an uncovered case in the proposed computer-assisted argument.

### Reproducibility and scope of the evidence

The consolidated archive includes a proof map, original retained proofs, source code, certificates, and completed replay records. A manifest identifies the payload by SHA-256. Run the commands below from the extracted archive root.

For the primary residual theorem:

```text
python3 round10/local_centroid/verify_complete_local_centroid.py
```

This portable driver compiles the independent C++17 enumeration, checks all nine coverage totals and the coordinate-line identities, and reconstructs the 431 axis fallbacks using Python fractions. The archived full run passed. This component requires no external optimizer.

For the alternative parameter-envelope theorem:

```text
python3 round10/envelope/verify_universal_envelope.py
```

The independent verifier rebuilds the rows and checks exact rational multipliers with standard-library integer arithmetic. Its archived complete run passed. It is an alternative to the primary centroid component, not an extra mandatory gate.

The retained global branches have their own verifiers and analytic reductions. The proof map lists those sources and completed records. Source inspection, hash validation, bounded symbolic checks, full finite replay, and external mathematical review are distinct forms of evidence. The editorial pass producing this reading manuscript checked consistency and presentation; it did not rerun every global calculation.

### Limits and promising next improvements

The two explicit witnesses do not provide a universal coverage theorem for arbitrary lower ideals. Local moves alone fail on eligible shapes, and one-step moves plus the axis witness also fail. Removing every mixed-plane-corner restriction permits examples where even unrestricted monotone moves and the axis construction miss the target. These are failures of a proposed criterion, not counterexamples to Wilf or necessarily to the centroid inequality.

The most useful further simplification is a structural proof of the two-witness alternative for the stated residual class. A second possibility is a short symbolic rule for the parameter-envelope multipliers in Appendix A. Neither has been established here. The clipped-box and clipped-prism identities give infinite test families, but do not classify all admissible ideals.

Beyond four generators, the moment identity, integer contradiction threshold, and explicit witness formulas survive. What remains missing is a higher-dimensional coverage theorem that handles equality families, compatibility cycles, and intermediate-support exclusions. The separate fixed-dimension finite reduction has its own analytic review obligations and enormous bounds; it does not supply a practical five-generator verification.

The proposed four-generator proof should therefore be assessed through its complete analytic dependency chain and exact finite coverage, with external mathematical review still outstanding.

## Appendix A. Universal parameter certificates as an alternative

This appendix concerns the degree-six residual class: \(m\ge30\), exactly one full-support corner \(p\), and \(5\le|p|_1\le7\), with the original arithmetic restrictions, including erosion and the refined dominating-plane-corner bound. It is a separate route from the weaker-hypothesis theorem in Section 2.

A separate argument removes the
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
\tag{A1}
\]
Here \(c\) encodes the fixed-height score \(u(m-D_h)\). Equation (A1) follows
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
A short symbolic choice of the multipliers in (A1), valid across parameter
ranges, would further simplify the second route; it has not been derived here.

## References and technical source guide

The classical weighted-ideal and asymptotic literature provides context, not external validation of the new proposed proof.

1. W. Bruns, P. A. García-Sánchez, C. O’Neill and D. Wilburne, *Wilf’s conjecture in fixed multiplicity* (2019). [arXiv:1903.04342](https://arxiv.org/abs/1903.04342). Published multiplicities through 18.
2. J. Kliem and C. Stump, *A new face iterator for polyhedra and more general finite locally branched lattices* (2019; revised 2020). [arXiv:1905.01945](https://arxiv.org/abs/1905.01945). Published multiplicity 19.
3. A. Zhai, *An asymptotic result concerning a question of Wilf* (2011). [arXiv:1111.2779](https://arxiv.org/abs/1111.2779). Approximate fixed-embedding-dimension bounds must be distinguished from exact eventual Wilf.
4. M. Hellus, A. Rechenauer and R. Waldi, *Variants on a question of Wilf* (2018). [arXiv:1804.06141](https://arxiv.org/abs/1804.06141). Weighted lower ideals and sufficient cases.
5. M. Delgado, S. Eliahou and J. Fromentin, *A verification of Wilf’s conjecture up to genus 100* (2023). [arXiv:2310.07742](https://arxiv.org/abs/2310.07742). Genus-bounded verification is a different finite restriction.

The archive's current source map is round11/proof_map.md. The final local theorem and portable verifier are in round10/local_centroid; the alternative envelope is in round10/envelope; the analytic family proofs are in round10/symbolic. The higher-dimensional derivations and editorial audit are in round11. Earlier global reductions and completed records retain their original relative paths, as indexed by the proof map. The large historical research manuscript is preserved for provenance; its interleaved checkpoints are superseded by the case partition in the present reading manuscript.
