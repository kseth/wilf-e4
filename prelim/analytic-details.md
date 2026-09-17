# Analytic details of the preliminary proof

These three appendices are integral parts of [the proof](proof.md).
Their equation and lemma numbers are local to each appendix.
Each establishes an analytic reduction without a finite computation.
All hypotheses required by the proof spine are stated here.

## Appendix A: central boxes and three monotone horns

The needed clique-tree fact is classical and is proved below.

### A.1. Statement

For \(r\in\mathbb N\), write \([r]=\{0,1,\ldots,r\}\). For
\(z\in\mathbb N^3\), let

\[
\mathcal B(z)=[z_1]\times[z_2]\times[z_3].
\]

#### Theorem 1.1 (central-box/three-horn decomposition)

Let \(U\subseteq\mathbb N^3\) be a nonempty finite lower ideal. Suppose
that no minimal point of \(\mathbb N^3\setminus U\) has all three
coordinates positive. Then there is a point \(c\in U\) and a disjoint
partition

\[
U=\mathcal B(c)\mathbin{\dot\cup}A_1
 \mathbin{\dot\cup}A_2\mathbin{\dot\cup}A_3
\tag{1}
\]

with the following properties. For each \(i\), let \(j,k\) be the other
two coordinates, and put \(h_i=\max\{x_i:x\in U\}\), which is also the
largest coordinate-\(i\) axis level in \(U\). Then \(h_i\ge c_i\), and
there are nonincreasing functions

\[
r_i:\{c_i+1,\ldots,h_i\}\longrightarrow\{0,\ldots,c_j\},
\qquad
s_i:\{c_i+1,\ldots,h_i\}\longrightarrow\{0,\ldots,c_k\}
\tag{2}
\]

such that

\[
A_i=
\left\{x\in\mathbb N^3:
c_i<x_i\le h_i,\quad
0\le x_j\le r_i(x_i),\quad
0\le x_k\le s_i(x_i)
\right\}.
\tag{3}
\]

The domain in (2) is empty when \(h_i=c_i\), giving an empty horn. Thus
the theorem includes a single box, one or two nonempty horns, zero central
caps, and ideals that do not contain all coordinate units.

### A.2. Plane determination and the compatibility graph

The exclusion hypothesis has the following equivalent form:

\[
x\in U
\quad\Longleftrightarrow\quad
(x_1,x_2,0),(x_1,0,x_3),(0,x_2,x_3)\in U.
\tag{4}
\]

The forward implication is lower closure. Conversely, if \(x\notin U\),
then \(x\) dominates a minimal excluded point \(p\). At least one coordinate
of \(p\) is zero, so one of the three planar points in (4) also dominates
\(p\) and lies outside \(U\).

For coordinate \(i\), let

\[
h_i^{\mathrm{ax}}=\max\{t\in\mathbb N:te_i\in U\}.
\]

Construct a graph \(G\) with vertices

\[
V_i=\{(i,t):0\le t\le h_i^{\mathrm{ax}}\},
\qquad i=1,2,3.
\]

Each \(V_i\) is a clique. For \(i\ne j\), join \((i,t)\) to \((j,s)\)
exactly when \(te_i+se_j\in U\). The three zero-level vertices are
universal. Moreover, lower closure gives the nested-neighborhood property

\[
t'<t\quad\Longrightarrow\quad
N(i,t)\setminus V_i\subseteq N(i,t')\setminus V_i.
\tag{5}
\]

#### Lemma 2.1

The graph \(G\) is chordal.

#### Proof

Suppose an induced cycle has length at least four. Because there are only
three coordinate classes, it repeats a class. An induced cycle can contain at
most two vertices from a clique, and those two must be consecutive. Write
their levels as \(t'<t\). The other cycle neighbor of
\((i,t)\) lies outside \(V_i\); by (5), it is also adjacent to \((i,t')\).
This is a chord, a contradiction. \(\square\)

### A.3. The required clique-tree lemma

#### Lemma 3.1 (clique tree)

The distinct maximal cliques of a finite nonempty connected chordal graph are
the nodes of a tree such that the nodes containing any fixed graph vertex
form a connected subtree.

#### Proof

We induct on the number of graph vertices. A complete graph has a one-node
tree. Otherwise choose nonadjacent vertices \(a,b\) and an inclusion-minimal
set \(Q\) separating them. Let \(C_a,C_b\) be their components in
\(G-Q\).

The separator \(Q\) is a clique. Indeed, minimality implies that every
\(q\in Q\) has a neighbor in both \(C_a\) and \(C_b\). If nonadjacent
\(q,r\in Q\) existed, take a shortest \(q\)-to-\(r\) path whose internal
vertices lie in \(C_a\), and another through \(C_b\). Their union would be
an induced cycle of length at least four: shortestness rules out chords
within either path, and distinct components of \(G-Q\) have no edges between
them. This contradicts chordality.

Let \(C_1,\ldots,C_d\), with \(d\ge2\), be all components of \(G-Q\).
Each induced graph on \(C_\ell\cup Q\) is connected, chordal, and smaller.
Apply induction to each, and choose in each resulting clique tree a bag
\(K_\ell\) containing the clique \(Q\). Join the nodes \(K_\ell\) in a
star. A vertex outside \(Q\) occurs in only one component tree. A vertex in
\(Q\) occurs in a connected subtree of every component tree containing
\(K_\ell\), and the added star joins those subtrees. Thus the resulting tree
of clique bags has the required connectedness property.

Every maximal clique of \(G\) occurs among these bags, because a clique cannot
meet two components of \(G-Q\). Some bags may be nonmaximal in \(G\), or the
same maximal clique may occur more than once. If a bag \(B\) is contained in
another bag \(C\), then every node on the tree path from \(B\) to \(C\)
contains every vertex of \(B\). Contract the first edge of that path and keep
the neighboring bag. This preserves the connectedness property. Repeating
removes all nonmaximal and duplicate bags, leaving exactly the distinct
maximal cliques. \(\square\)

This is the finite clique-tree property arising from the classical
subtree characterization of chordal graphs; see Fănică Gavril,
[*The intersection graphs of subtrees in trees are exactly the chordal
graphs*](https://doi.org/10.1016/0095-8956(74)90094-X), *Journal of
Combinatorial Theory, Series B* **16** (1974), 47--56.

### A.4. From maximal cliques to maximal boxes

Every maximal clique of the compatibility graph contains a prefix of each
coordinate class. Indeed, if it contains \((i,t)\), then every lower level in
\(V_i\) is adjacent to the whole clique by (5), and maximality adds it.
The universal zero levels ensure that no coordinate class is absent.

Let \(z_i\) be the largest level from \(V_i\) in the clique. All three pairs
of coordinate maxima are adjacent, so (4) gives \(z=(z_1,z_2,z_3)\in U\).
Conversely, every \(z\in U\) gives the clique consisting of the three
coordinate prefixes through \(z_i\). Inclusion of these prefix cliques is
exactly coordinatewise comparison of their upper corners. It follows that
the maximal cliques of \(G\) correspond bijectively to the maximal points
of \(U\), and hence to the anchored boxes \(\mathcal B(z)\) maximal in
\(U\): a nonmaximal corner extends its prefix clique, and any extension of a
prefix clique produces a larger corner through (4).

Apply Lemma 3.1, and write \(\mathcal T\) for the resulting tree on maximal
points. A graph vertex \((i,t)\) belongs to the clique for \(z\) precisely
when \(z_i\ge t\). Therefore

\[
\boxed{
\{z\in\operatorname{Max}(U):z_i\ge t\}
\text{ induces a connected subtree whenever it is nonempty.}
}
\tag{6}
\]

### A.5. The median and the three arms

Distinct maximal points of \(U\) are incomparable. Let \(z(v)\) denote the
point labeling a node \(v\) of \(\mathcal T\).

If \(v\) is a leaf with neighbor \(w\), choose a coordinate \(i\) for which
\(z_i(v)>z_i(w)\). If another node \(u\) had \(z_i(u)\ge z_i(v)\), the
superlevel subtree (6) at level \(z_i(v)\) would contain \(u,v\) but not
\(w\), even though the path from \(u\) to \(v\) passes through \(w\).
Hence \(v\) is the unique global maximizer of coordinate \(i\). Two leaves
cannot be unique maximizers of the same coordinate, so \(\mathcal T\) has at
most three leaves.

For each coordinate \(i\), choose a node \(v_i\) maximizing \(z_i\). Every
leaf is one of \(v_1,v_2,v_3\), by the preceding uniqueness. Consequently
the whole tree is the minimal subtree spanning those three nodes: otherwise
a component outside that spanning subtree would end in an unselected leaf.

Let \(v_0\) be the median of \(v_1,v_2,v_3\), the unique common node of
their three pairwise paths, and set \(c=z(v_0)\). Repeated selected nodes are
allowed. The nontrivial paths from \(v_0\) to the \(v_i\) cover the tree and
meet only at \(v_0\); these are the at most three arms.

Consider an edge \(uv\) on the path from \(v_0\) toward \(v_i\), oriented
away from \(v_0\). If \(z_i(u)>z_i(v)\), the coordinate-\(i\) superlevel
subtree at height \(z_i(u)\) would contain \(u,v_i\) but not the intervening
node \(v\). Thus

\[
z_i(u)\le z_i(v).
\tag{7}
\]

For \(j\ne i\), the selected maximizer \(v_j\) is either \(v_0\) or lies
on another arm. Hence \(u\) lies on the path from \(v\) to \(v_j\). If
\(z_j(v)>z_j(u)\), the corresponding superlevel subtree would contain
\(v,v_j\) but not \(u\). Therefore

\[
z_j(u)\ge z_j(v),\qquad j\ne i.
\tag{8}
\]

Equality in (7), together with (8), would give \(z(v)\le z(u)\), contrary
to incomparability. Thus the outward coordinate increases strictly along
its arm, while both transverse coordinates weakly decrease.

### A.6. Disjoint rectangular sections

All maximal boxes on arm \(i\) have transverse caps at most \(c_j,c_k\).
Fix an integer \(t>c_i\). The central node and the other arms have
coordinate-\(i\) cap at most \(c_i\), so they contribute nothing at this
level. Among nodes on arm \(i\) whose outward cap is at least \(t\), let
\(v(t)\) be the first. All later contributing boxes have transverse
rectangles contained in that of \(v(t)\), by (8). Hence the entire level
section is

\[
\{t\}\times\prod_{\ell\ne i}[z_\ell(v(t))],
\tag{9}
\]

after putting coordinate \(i\) first. As \(t\) increases, \(v(t)\) moves
weakly outward, so both transverse caps are nonincreasing. There is no gap
between \(c_i+1\) and the last nonempty level, because every anchored box
contains all lower levels.

Every point of \(U\) belongs to a maximal anchored box. If it is outside
\(\mathcal B(c)\), that maximal box lies on a unique arm, and the point
exceeds the corresponding central cap while staying below the other two.
It therefore lies in exactly one section (9). This proves the disjoint
partition (1) and Theorem 1.1. \(\square\)

Positive diagonal scaling preserves the decomposition. Rectangular
thickening replaces each integer level by a slab and each integer transverse
rectangle by a continuous rectangle; its two transverse side lengths remain
nonincreasing. Thus the thickened sets of proof Section 4 belong to the same
central-box/three-horn geometric class, up to null boundary conventions.

### A.7. One full-support corner

Let \(T\subseteq\mathbb N^3\) be a finite lower ideal with exactly one
full-support minimal excluded point \(p\). Let \(P\) be the set of all
minimal excluded points of \(T\), and define

\[
U=\mathbb N^3\setminus
\bigcup_{q\in P\setminus\{p\}}(q+\mathbb N^3).
\tag{10}
\]

#### Corollary 7.1 (one-corner clipping)

The set \(U\) is a finite lower ideal with no full-support minimal exclusion,
and

\[
\boxed{T=U\setminus(p+\mathbb N^3).}
\tag{11}
\]

The ideals \(T\) and \(U\) have the same points on every coordinate axis.
If (1) is a central-box/three-horn partition of \(U\), then

\[
T=
\bigl(\mathcal B(c)\setminus(p+\mathbb N^3)\bigr)
\mathbin{\dot\cup}
\bigl(A_1\setminus(p+\mathbb N^3)\bigr)
\mathbin{\dot\cup}
\bigl(A_2\setminus(p+\mathbb N^3)\bigr)
\mathbin{\dot\cup}
\bigl(A_3\setminus(p+\mathbb N^3)\bigr).
\tag{12}
\]

At an outward level \(t\) of horn \(i\), with transverse coordinates
\(j,k\) and uncut caps \(r,s\), the retained section is the exact set

\[
\begin{cases}
[r]\times[s], & t<p_i,\\
([r]\times[s])\setminus
   \bigl([p_j,r]\times[p_k,s]\bigr), & t\ge p_i,
\end{cases}
\tag{13}
\]

where an interval \([a,r]\) is empty when \(a>r\).

#### Proof

Every member of \(P\setminus\{p\}\) has support at most two, so the minimal
excluded points of \(U\), after redundant generators are removed, also have
support at most two. For each coordinate \(i\), the first missing axis point
of \(T\) is a pure-axis member of \(P\). It remains in (10), proving that
\(U\) is finite. The full-support orthant \(p+\mathbb N^3\) contains no axis
point, so \(T\) and \(U\) have the same axis sections. The upper-ideal
description of a lower ideal's complement gives (11).

Deleting the same upper orthant from each piece of a disjoint partition
preserves disjointness and proves (12). At level \(t<p_i\), no point lies
above \(p\); at level \(t\ge p_i\), precisely the transverse upper-right
rectangle lies above \(p\). This proves (13). \(\square\)

The same clipping formulas remain valid for any positive integer point
\(p\), even if it is inactive or not minimal excluded after clipping. Allowing
such choices enlarges a later optimization class and therefore remains safe
for an upper-bound certificate. In particular, if no point of \(U\) dominates
\(p\), the clipping is inactive and the representation includes the
no-full-corner case.

### A.8. Exact recurrence interface

Fix an outward coordinate \(i\), a first level \(t_0=c_i+1\), and central
transverse caps \(b_0=c_j\), \(d_0=c_k\). Suppose a problem assigns an
additive score \(C_i(t,r,s)\) to the retained section (13) and has a
pointwise feasibility predicate \(\mathcal F_i(t,r,s)\). Let
\(F_i(t,b,d)\) be the maximum score of a possibly empty nested sequence
starting at level \(t\), with first caps at most \(b,d\). Then

\[
\boxed{
F_i(t,b,d)=\max\left\{
0,
\max_{\substack{0\le r\le b,\ 0\le s\le d\\
                 \mathcal F_i(t,r,s)}}
\bigl(C_i(t,r,s)+F_i(t+1,r,s)\bigr)
\right\}.
}
\tag{14}
\]

A terminal level beyond the allowed axis range has value zero. The zero
option terminates the horn. Every nonempty uncut section contains its axis
point, which survives clipping because \(p\) is positive; lower closure then
forbids a later nonempty section after termination. Every other choice in
(14) selects the current rectangle and passes exactly its caps to the next
level. Induction on the remaining number of levels proves that (14) covers
every nested horn and only such sequences.

Equivalently, a prefix-maximum implementation may compare the state
\((b,d)\) with \((b-1,d)\) and \((b,d-1)\), because every proper
subrectangle decreases at least one cap. This is an implementation identity,
not an additional geometric assumption.

For a fixed center, the three arms in (1) or (12) are disjoint, so their
additive optima may be computed independently and added to the central-piece
score. Maximizing over all centers therefore covers every ideal in the
theorem or clipping corollary. Particular score formulas, degree or weighted
height allowances, and interval bounds are specified in the proof spine.

## Appendix B: full weighted Apéry ideals

Here \(w(x)\) denotes the unnormalized integer label, locally to this appendix.

### B.1. Setup and statement

Let

\[
S=\langle m,a_1,a_2,a_3\rangle
\]

be a minimally four-generated numerical semigroup. Let
\(T\subseteq\mathbb N^3\) be its preferred Apéry lower ideal, and put

\[
w(x)=a_1x_1+a_2x_2+a_3x_3,
\qquad
M=\max_{x\in T}w(x).
\]

Thus \(|T|=m\), the labels of its points are pairwise distinct modulo
\(m\), and \(0,e_1,e_2,e_3\in T\). We say that \(T\) is *full weighted* if

\[
T=\{x\in\mathbb N^3:w(x)\le M\}.
\tag{1}
\]

Permuting the three coordinates preserves (1), lower closure, residue
injectivity, and all projection quantities used below. We may therefore
write the three nonmultiplicity generators as

\[
a<b<d
\]

and use coordinates \((x,y,z)\), so that

\[
w(x,y,z)=ax+by+dz.
\]

The inequalities are strict because the minimal generators are distinct.

#### Theorem 1.1 (full-weighted-ideal theorem)

If the preferred Apéry ideal \(T\) is full weighted, then

\[
W_4(S)\ge0.
\]

We prove the theorem in three steps.

### B.2. Classification of the column projection

Project away the \(x\)-coordinate. By (1), its image is

\[
Q=\pi_x(T)
=\{(y,z)\in\mathbb N^2:by+dz\le M\}.
\tag{2}
\]

Put

\[
h_y=\left\lfloor\frac Mb\right\rfloor,
\qquad
h_z=\left\lfloor\frac Md\right\rfloor.
\]

Both are positive because \(e_2,e_3\in T\).

#### Lemma 2.1 (three possible projections)

The set \(Q\) is one of

\[
\begin{aligned}
Q_3&=\{(0,0),(1,0),(0,1)\},\\
Q_4&=\{(0,0),(1,0),(2,0),(0,1)\},\\
Q_6&=\{(y,z)\in\mathbb N^2:y+z\le2\}.
\end{aligned}
\tag{3}
\]

#### Proof

For \(1\le j\le h_y\), define

\[
p_j=
\left(
\left\lfloor\frac{M-bj}{a}\right\rfloor+1,
j,0
\right).
\tag{4}
\]

This is a minimal excluded point. Its \(x\)-predecessor is included by the
floor definition. Moreover,

\[
w(p_j)\le M+a,
\]

so its \(y\)-predecessor has weight at most \(M+a-b\le M\). Both displayed
coordinates of \(p_j\) are positive because \(bj\le M\).

The representative in \(T\) of the residue of \(p_j\) must have support
disjoint from \(\{x,y\}\), so it lies on the \(z\)-axis. The corners
\(p_1,\ldots,p_{h_y}\) have intersecting supports and hence distinct
residues. The \(z\)-axis contains exactly

\[
0,e_3,\ldots,h_ze_3,
\]

and therefore

\[
h_y\le h_z+1.
\tag{5}
\]

First suppose \(M<b+d\). Then (2) contains no point with both coordinates
positive. Since

\[
d\le M<b+d<2d,
\]

we have \(h_z=1\). Equation (5) gives \(h_y\le2\), while \(h_y\ge1\).
This gives \(Q_3\) or \(Q_4\).

Now suppose \(M\ge b+d\). The point

\[
p=
\left(
\left\lfloor\frac{M-b-d}{a}\right\rfloor+1,
1,1
\right)
\tag{6}
\]

is a full-support minimal exclusion: its \(x\)-predecessor is included by
the floor definition, while removing \(e_2\) or \(e_3\) reduces its weight
from at most \(M+a\) by at least \(a\). By the corner rules, \(p\) has
residue zero. Each \(p_j\) has support intersecting that of \(p\), so none
of their distinct representatives on the \(z\)-axis can be zero. Hence

\[
h_y\le h_z.
\tag{7}
\]

If \(M\ge2b+d\), then

\[
p'=
\left(
\left\lfloor\frac{M-2b-d}{a}\right\rfloor+1,
2,1
\right)
\]

is a second full-support minimal exclusion. Indeed, its \(x\)-predecessor is
included by the floor definition, and removing \(e_2\) or \(e_3\) reduces
its weight from at most \(M+a\) by at least \(a\). It is distinct from
\(p\) because its \(y\)-coordinate is two. This contradicts the uniqueness
of a full-support corner, so

\[
M<2b+d<3d
\]

and \(h_z\le2\). On the other hand,

\[
M\ge b+d>2b,
\]

so \(h_y\ge2\). Since \(b<d\) also gives \(h_y\ge h_z\), equation (7)
forces

\[
h_y=h_z=2.
\tag{8}
\]

It follows from (8) that \(2d\le M<3b\). Every \((y,z)\) of total degree at
most two has weight at most \(2d\), while every point of total degree at
least three has weight at least \(3b\). Thus (2) is exactly \(Q_6\).
\(\square\)

### B.3. The six-column triangle is impossible

For \((y,z)\in Q\), let

\[
L_{yz}=\left\lfloor\frac{M-by-dz}{a}\right\rfloor+1
\tag{9}
\]

be the length of its \(x\)-column. Subtracting \(b\) or \(d\) from the
available weight decreases a positive column length by at least one, because
\(b,d>a\).

#### Lemma 3.1 (six-column exclusion)

The projection \(Q_6\) in (3) cannot occur.

#### Proof

Suppose it does, and abbreviate its positive column lengths by

\[
\begin{array}{c|cccccc}
(y,z)&(0,0)&(1,0)&(2,0)&(0,1)&(1,1)&(0,2)\\ \hline
L_{yz}&\alpha&\beta&\gamma&\varphi&\varepsilon&\eta.
\end{array}
\tag{10}
\]

The strict column descents give

\[
\alpha>\beta>\gamma>0,
\qquad
\alpha>\varphi>\eta>0,
\qquad
\varepsilon<\min(\beta,\varphi).
\tag{11}
\]

Work in \(\mathbb Z/m\mathbb Z\), and let \(r\) be the least positive
integer for which \(ra\equiv0\pmod m\). The point
\((\varepsilon,1,1)\) is the full-support minimal exclusion above the mixed
column: its \(x\)-predecessor lies in that column, and its other two
predecessors are included by \(\varepsilon<\varphi,\beta\). It therefore has
residue zero:

\[
\varepsilon a+b+d\equiv0\pmod m.
\tag{12}
\]

The residues in the origin column are

\[
0,a,\ldots,(\alpha-1)a,
\]

whereas (12) makes those in the mixed column

\[
-\varepsilon a,-(\varepsilon-1)a,\ldots,-a.
\]

All \(\alpha+\varepsilon\) points belong to \(T\), so residue injectivity
shows that these consecutive multiples of \(a\) are distinct. Consequently

\[
r\ge\alpha+\varepsilon.
\tag{13}
\]

The two points \((\beta,1,0)\) and \((\gamma,2,0)\) are minimal
exclusions: their \(x\)-predecessors lie at the tops of their columns, and
their \(y\)-predecessors are included by \(\beta<\alpha\) and
\(\gamma<\beta\). Their representatives have support on the \(z\)-axis.
Their residues are nonzero because their supports meet that of
\((\varepsilon,1,1)\), and they are distinct from each other. Since the
\(z\)-axis consists of \(0,e_3,2e_3\), their residues therefore permute
\(d,2d\).

The swapped assignment would be

\[
\beta a+b\equiv2d,
\qquad
\gamma a+2b\equiv d.
\tag{14}
\]

Subtracting twice the second congruence in (14) from the first gives

\[
(\beta-2\gamma)a-3b\equiv0\pmod m,
\]

while the second congruence in (14), substituted into (12), gives

\[
(\varepsilon+\gamma)a+3b\equiv0\pmod m.
\]

Adding these relations eliminates \(b\) and gives

\[
(\beta-\gamma+\varepsilon)a\equiv0\pmod m.
\]

But

\[
0<\beta-\gamma+\varepsilon
<\alpha+\varepsilon\le r,
\]

contradicting the definition of \(r\). We must therefore have

\[
\beta a+b\equiv d,
\qquad
\gamma a+2b\equiv2d.
\tag{15}
\]

The same argument for the minimal exclusions
\((\varphi,0,1)\) and \((\eta,0,2)\), whose representatives lie on the
\(y\)-axis, rules out the swapped assignment there: it would give
\((\varphi-\eta+\varepsilon)a\equiv0\pmod m\), although

\[
0<\varphi-\eta+\varepsilon<\alpha+\varepsilon\le r.
\]

Consequently

\[
\varphi a+d\equiv b,
\qquad
\eta a+2d\equiv2b.
\tag{16}
\]

Adding the first congruences in (15)--(16), and subtracting the second
congruences from twice their respective first congruences, shows that

\[
\beta+\varphi,
\qquad
2\beta-\gamma,
\qquad
2\varphi-\eta
\tag{17}
\]

are positive multiples of \(r\). Each is strictly less than \(2\alpha\),
and (13) gives \(\alpha<r\). Thus all three integers in (17) lie strictly
between zero and \(2r\), so

\[
\beta+\varphi=r,
\qquad
2\beta-\gamma=r,
\qquad
2\varphi-\eta=r.
\]

Adding the last two equalities and subtracting twice the first gives

\[
\gamma+\eta=0,
\]

contrary to (11). Hence \(Q_6\) is impossible. \(\square\)

#### Remark 3.2

The proof of Lemma 3.1 used only residue bijectivity, the corner rules, the
six-point projection, and the strict descents in (11). The exact floor
formula (9) is not otherwise needed. This isolates the arithmetic obstruction
from the full-weighted classification which produces the six-point shape.

### B.4. The remaining projection scores

Let

\[
Z=\{x\in T:M-w(x)<m\},
\qquad
K=\operatorname{Max}(T),
\]

and use the notation

\[
P(T)=\sum_{j=1}^3|\pi_j(T)|,
\qquad
E(X)=\sum_{x\in X}|x|_1-\sum_{j=1}^3\max_{x\in X}x_j,
\]

\[
\Phi(T,X)=P(T)-3|X|-E(X)
\]

from the final-window note. That note proves \(E(Z)\ge0\), \(Z\subseteq K\),
and

\[
mW_4(S)\ge m\Phi(T,Z)+E(Z).
\tag{18}
\]

For nonempty \(X\subseteq K\), adding points to \(X\) cannot decrease
\(|X|\), and it cannot decrease \(E(X)\): in each coordinate the increase
in the coordinate sum is at least the increase in the coordinate maximum.
Hence

\[
\Phi(T,Z)\ge\Phi(T,K).
\tag{19}
\]

We now calculate the right side for the only two remaining projections.

#### Lemma 4.1 (three columns)

If \(Q=Q_3\), then \(\Phi(T,K)\ge0\).

#### Proof

Write the column lengths over \((0,0),(1,0),(0,1)\) as
\(\alpha,\beta,\gamma\). Then

\[
\alpha>\beta,\gamma\ge1,
\qquad
m=\alpha+\beta+\gamma.
\tag{20}
\]

The three column tops are pairwise incomparable and every other point is
below one of them, so they are precisely \(K\). Direct projection counting
gives

\[
P(T)=3+(\alpha+\gamma)+(\alpha+\beta)
=3+\alpha+m.
\tag{21}
\]

The sum of the total degrees of the three tops is \(m-1\), while their
coordinatewise maxima sum to \((\alpha-1)+1+1=\alpha+1\). Therefore

\[
E(K)=m-\alpha-2
\]

and

\[
\Phi(T,K)
=(3+\alpha+m)-9-(m-\alpha-2)
=2\alpha-4\ge0,
\tag{22}
\]

because \(\alpha>\beta\ge1\) implies \(\alpha\ge2\). \(\square\)

#### Lemma 4.2 (four columns)

If \(Q=Q_4\), then \(\Phi(T,K)\ge0\).

#### Proof

Write the column lengths over \((0,0),(1,0),(2,0),(0,1)\) as
\(\alpha,\beta,\gamma,\delta\). Then

\[
\alpha>\beta>\gamma\ge1,
\qquad
\alpha>\delta\ge1,
\qquad
m=\alpha+\beta+\gamma+\delta.
\tag{23}
\]

Again, the four column tops are precisely \(K\). The projections have sizes

\[
4,
\qquad
\alpha+\delta,
\qquad
\alpha+\beta+\gamma,
\]

so

\[
P(T)=4+\alpha+m.
\tag{24}
\]

The total degrees of the four tops sum to \(m\), and their coordinatewise
maxima sum to \((\alpha-1)+2+1=\alpha+2\). Thus

\[
E(K)=m-\alpha-2
\]

and

\[
\Phi(T,K)
=(4+\alpha+m)-12-(m-\alpha-2)
=2\alpha-6\ge0,
\tag{25}
\]

because \(\alpha>\beta>\gamma\ge1\) implies \(\alpha\ge3\). \(\square\)

### B.5. Proof of Theorem 1.1

Lemma 2.1 lists the three possible \(x\)-column projections. Lemma 3.1
excludes the six-column triangle, and Lemmas 4.1--4.2 give
\(\Phi(T,K)\ge0\) in the remaining cases. Equation (19) therefore gives
\(\Phi(T,Z)\ge0\), and (18) proves \(W_4(S)\ge0\).

No finite verification is used. \(\square\)

## Appendix C: the continuous no-corner moment inequality

### C.2. Box-horn sets and their moment functional

Boundary faces never affect the integrals below. A *box-horn set of height
one* is the disjoint union, up to null sets, of a central box

\[
C=[0,a]\times[0,b]\times[0,c],
\qquad a,b,c\ge0,\qquad a+b+c\le1,
\tag{5}
\]

and at most three outward horns. The horn beyond the \(a\)-face has the form

\[
\{(t,y,z):a<t<1,\ 0<y<f(t),\ 0<z<g(t)\},
\tag{6}
\]

where \(f,g\) are nonnegative, nonincreasing finite step functions satisfying

\[
f(t)\le b,\qquad g(t)\le c,
\qquad t+f(t)+g(t)\le1.
\tag{7}
\]

The other two horns are defined by coordinate permutation. Empty horns and
zero-width sections are allowed.

For a measurable \(E\subseteq\mathbb R_{\ge0}^3\), define

\[
\mathcal J(E)=\int_E\bigl(3(x_1+x_2+x_3)-2\bigr)\,dx.
\tag{8}
\]

Thus \(\mathcal J(E)\le0\) is equivalent to

\[
\frac1{\operatorname{vol}E}
\int_E(x_1+x_2+x_3)\,dx\le\frac23
\tag{9}
\]

when \(E\) has positive volume. The central box contributes

\[
\mathcal J(C)
=abc\left(\frac32(a+b+c)-2\right).
\tag{10}
\]

The contribution of the horn (6) is

\[
\mathcal J_a(f,g)
=\int_a^1 f(t)g(t)
 \left(3t+\frac32(f(t)+g(t))-2\right)dt.
\tag{11}
\]

We next obtain a sharp enough common envelope for (11), then show that the
three envelopes are absorbed by the negative contribution (10).

### C.3. The boundary-tail potential

It is convenient to give the formulas at an arbitrary height allowance
\(L>0\). For \(0\le x\le y\), define

\[
\begin{aligned}
P_L(x,y)={}&\frac{Lx^3}{6}-\frac{x^4}{4}
 +\frac{Lxy^2}{2}-\frac{3x^2y^2}{4}-\frac{xy^3}{2},\\
g(q,z)={}&\frac{q^2z^2}{8}+\frac{q^3z}{24}+\frac{q^4}{192},\\
Q_L(x,y)={}&P_L(x,y)
 +g\bigl((y+2x-L)_+,y-x\bigr).
\end{aligned}
\tag{12}
\]

Extend \(Q_L\) symmetrically in \(x,y\).

#### Lemma 3.1 (boundary-tail optimum)

Suppose a horn is already on the height boundary: in reverse time
\(r=L-t\), its transverse sides are nondecreasing functions with sum \(r\),
ending at caps \(x\le y\). Its contribution is at most \(Q_L(x,y)\).

#### Proof

By scaling, take \(L=1\). At each \(r\), sort the two sides and write their
difference as \(d(r)\ge0\). Sorting preserves the sum, product, caps, and
monotonicity. The boundary contribution becomes

\[
\int_0^{x+y}\frac{(2-3r)(r^2-d(r)^2)}8\,dr.
\tag{13}
\]

The two sides are nondecreasing precisely when \(d\) is \(1\)-Lipschitz.
The cap conditions give

\[
\max(0,r-2x)\le d(r)\le\min(r,2y-r).
\tag{14}
\]

The coefficient of \(-d^2\) changes sign only at \(r=2/3\). After fixing
\(d(2/3)\), the optimal admissible function is therefore the smallest one
allowed by (14) to the left of \(2/3\), and the largest one allowed to its
right. Writing \(q=(2/3-d(2/3))/2\), the associated transverse sides are

\[
\begin{cases}
(r/2,r/2),&0\le r\le2q,\\
(q,r-q),&2q\le r\le y+q,\\
(r-y,y),&y+q\le r\le x+y.
\end{cases}
\tag{15}
\]

The same profile follows directly from pointwise product maximization if
\(x+y\le2/3\). When \(x+y\ge2/3\), feasibility gives

\[
\max(0,2/3-y)\le q\le\min(x,1/3).
\]

Let \(I(q;x,y)\) denote the integral in (13) for (15). Direct integration
gives

\[
\frac{\partial I}{\partial q}
=\frac{(y-q)^2(1-y-2q)}2.
\tag{16}
\]

Hence the optimum is attained at

\[
q_*=\min\left(x,\frac{1-y}{2}\right).
\tag{17}
\]

In the second case above, \(y\ge1/3\), so \(q_*\) lies in the displayed
feasible interval. The endpoint \(q=x\) has value \(P_1(x,y)\). If
\(q_*<x\), integration of (16) from \(q_*\) to \(x\) shows that the
improvement is

\[
g(y+2x-1,y-x).
\tag{18}
\]

Equations (12) and (18) prove the claim for \(L=1\); homogeneity gives the
general statement. \(\square\)

### C.4. Reducing an arbitrary horn to one slab

For \(a+x+y\le L\), put

\[
F_L(a;x,y)=Q_L(x,y)
 +\frac{3a-L}{2}xy(L-a-x-y),
\tag{19}
\]

and, whenever \(a+B+C\le L\), define

\[
U_L(a;B,C)=
\max_{0\le x\le B,\ 0\le y\le C}F_L(a;x,y).
\tag{20}
\]

The term added to \(Q_L\) is the contribution of a constant initial slab
from \(t=a\) to \(t=L-x-y\).

#### Lemma 4.1 (one-slab envelope)

Every finite-step horn based at \(a\), with transverse caps \(B,C\) and
height allowance \(L\), has contribution at most \(U_L(a;B,C)\).

#### Proof

Scale to \(L=1\), and sort the two transverse coordinates so \(B\le C\).
First fix the finite list of nested rectangle states and vary only the
outward endpoints of their slabs. The objective is a separable convex
quadratic in those endpoints: the quadratic coefficient at an endpoint is
\(3(A_i-A_{i+1})/2\ge0\), where \(A_i\) is the area of the \(i\)-th rectangle
and \(A_{n+1}=0\). A maximum on the endpoint polytope is attained at a
vertex. A block of equal endpoints at such a vertex either begins at \(a\)
or meets one of its height bounds. Removing zero-length slabs leaves every
surviving slab tight at its right endpoint.

Reverse time by \(r=1-t\), and write

\[
A(r)=1-\frac32r.
\]

If a tight slab starts at reverse time \(r\), ends with rectangle \((x,y)\),
and \(x+y=s\le r\), its exact contribution is

\[
A(r)(r-s)xy.
\tag{21}
\]

For transitions wholly inside \(r\le2/3\), any monotone boundary
interpolation has area at least that of the smaller endpoint rectangle, while
\(A(r)\ge0\). Filling those transitions therefore weakly increases the
objective. Lemma 3.1 then bounds the filled tail.

It remains to control the earlier transitions, where \(A(r)\le0\). If none
of the states reaches reverse time at most \(2/3\), all terms in (21) are
nonpositive and the empty horn dominates. Otherwise let \((u,v)\), \(u\le v\),
be the first tight state with \(u+v\le2/3\). At every earlier state of sum
\(s\), nestedness and the cap conditions allow its product to be replaced by
the smaller product at

\[
x_*(s)=\max(u,s-C),\qquad
y_*(s)=\min(C,s-u).
\tag{22}
\]

Indeed \(x(s-x)\) is increasing for \(x\le s/2\); the pair in (22) is
nested as \(s\) varies, respects \(B,C\), and ends at \((u,v)\). Since the
coefficient in (21) is nonpositive, this replacement can only increase the
objective. All earlier states now lie on the L-shaped boundary path

\[
(B,C)\longrightarrow(u,C)\longrightarrow(u,u).
\tag{23}
\]

The possibly slack initial position is represented only for bookkeeping by
the virtual state \((x_0,C)\), where \(x_0=1-a-C\ge B\). The first actual
jump covers the virtual excess.

We now compare a jump on (23) with filling the same part of the boundary
path continuously. Along a branch with one fixed side \(c\), a jump of
length \(d\) has gain

\[
G_c(d)=\frac c4d^2(2d+3c-2),
\tag{24}
\]

and two jumps satisfy

\[
G_c(d+e)-G_c(d)-G_c(e)
=\frac{3c}{2}de\left(d+e+c-\frac23\right).
\tag{25}
\]

These follow by integrating \(c(r-c)A(r)\). On the second branch of (23),
the fixed side is \(u\), and every jump has
\(d\le C-u\le1-2u\). Thus \(2d+3u-2\le-u\), so (24) is nonpositive and all
such jumps may be filled.

At most one jump crosses the turn in (23). Suppose it starts at
\((u+p,C)\) and ends at \((u,C-q)\). If its gain over the continuous L-path
is denoted by \(G(p,q;u,C)\), direct integration gives

\[
\frac{\partial G}{\partial q}
=\frac u2(p+q)(3p+3q+3u-2).
\tag{26}
\]

This derivative changes sign at most once, from negative to positive, so the
maximum occurs at \(q=0\) or \(q=C-u\). The continuous baseline from the
jump's start through the remaining tail is independent of \(q\), so the same
endpoint conclusion applies to the whole continuation. The first choice
moves the jump entirely onto the fixed-\(C\) branch.

For the balanced endpoint, a jump from reverse time \(r\) to \((z,z)\),
followed by the balanced tail, has value

\[
E_r(z)=A(r)(r-2z)z^2+\frac23z^3-\frac32z^4,
\]

with

\[
E_r'(z)=-6z\left(z-\frac r2\right)
              \left(z-r+\frac23\right).
\tag{27}
\]

On \(0\le z\le R\le r/2\), the maximum of \(E_r\) is therefore at \(0\) or
\(R\). For a noninitial crossing jump, take \(R\) to be the smaller side of
its genuine starting state; the second endpoint is a fixed-smaller-side jump
and is dominated by filling. For the initial crossing jump, take \(R=B\),
which is valid because \(2B\le B+C\le1-a\). Its second endpoint is the
admissible initial slab ending at \((B,B)\). If the zero endpoint wins, every
earlier term still lies in the nonpositive part, so the empty horn dominates.
Thus the crossing jump either disappears or is replaced by an admissible
one-slab construction.

All remaining jumps lie on the fixed-\(C\) branch. Retain the first jump,
including any mandatory initial slack, and fill every later jump whose gain
in (24) is nonpositive. If a later jump of length \(e\) has positive gain,
then either \(C\ge2/3\), or

\[
e>\frac32\left(\frac23-C\right)>\frac23-C.
\]

Equation (25) shows that merging it into the first jump cannot decrease the
total gain. The individual gains depend only on jump lengths, so the jump and
continuous lengths may be reordered along the same branch before merging.
Their total length, the continuous baseline, nestedness, and the initial cap
constraint are unchanged. Repetition leaves a single initial jump followed
by a boundary profile.

If that jump ends at effective caps \((x,y)\), its contribution together with
the optimal continuation is \(F_1(a;x,y)\). The effective caps lie inside
\((B,C)\), so (20) proves the lemma. \(\square\)

### C.5. The joint three-horn inequality

#### Lemma 5.1 (joint envelope)

If \(a,b,c\ge0\), \(S=a+b+c\le L\), then

\[
\boxed{
U_L(a;b,c)+U_L(b;a,c)+U_L(c;a,b)
\le abc\left(2L-\frac32S\right).
}
\tag{28}
\]

#### Proof

For \(x\le y\), first omit the boundary-tail gain from (12) and write

\[
H_L(a;x,y)=P_L(x,y)
 +\frac{3a-L}{2}xy(L-a-x-y).
\tag{29}
\]

Let \(r=L-a-x-y\). Direct differentiation gives

\[
(H_L)_y=\frac{xr}{2}\,[3(a+y)-L].
\tag{30}
\]

Where the gain in (12) is active, it is nondecreasing in \(y\). Hence, for
fixed \(x\), \(F_L(a;x,y)\) first decreases and then increases as \(y\) runs
from \(x\) to its allowed cap; its maximum is at the diagonal or at the full
larger cap. If \(a+x\ge L/3\), (30) sends the diagonal endpoint to the full
cap. If \(a+x\le L/3\), the gain vanishes on the diagonal segment and

\[
\frac d{dt}H_L(a;t,t)
=-6t\left(t-\frac{L-a}{2}\right)
       \left(t-\left(\frac L3-a\right)\right)\le0
\tag{31}
\]

for \(0\le t\le x\). That diagonal endpoint is at most zero, which is
attained by the empty horn. Thus, for \(B\ge C\),

\[
U_L(a;B,C)=\max_{0\le x\le C}F_L(a;x,B).
\tag{32}
\]

Relabel the central sides so that \(a\le b\le c\), and first take the
saturated case \(L=S\). The gain in (12) vanishes for the horns based at
\(b\) and \(c\). For the gain-free expression, one also has

\[
2(H_L)_x=(a-x)(x-y)^2
 +r\,[x^2+2ay-yr],
\tag{33}
\]

where \(a\) in this formula denotes the horn's base and \(y\) its full larger
cap. Equation (33) is nonnegative in the two relevant ranges. Consequently
the \(b\)- and \(c\)-horns take their full smaller cap \(a\). Only the horn
based at the smallest side remains to be optimized.

Indeed, for the \(b\)-horn one has \(0\le x\le a\le b\), larger cap \(c\),
and \(r=a-x\); for the \(c\)-horn the larger cap is \(b\) and the same
relations hold. Both terms on the right of (33) are then nonnegative.

For \(0\le x\le b\), set

\[
\Delta=\frac{abcS}{2}-F_S(a;x,c)
       -H_S(b;a,c)-H_S(c;a,b).
\tag{34}
\]

Three nonnegative polynomial identities cover its entire domain. In the
gain-free range \(x\le a\), substitute

\[
x=p,\quad a=p+q,\quad b=p+q+r,\quad c=p+q+r+s.
\]

Then

\[
\begin{aligned}
\Delta={}&\frac34p^2(q+r)^2
 +\frac12p(q+r)^2(s+r+2q)\\
&+q^2\left[\frac{(s+2r)^2}{4}
 +\frac23q(s+2r)+\frac12q^2\right]\ge0.
\end{aligned}
\tag{35}
\]

In the remaining gain-free range \(a\le x\le(a+b)/2\), substitute

\[
a=p,\quad x=p+q,\quad b=p+q+r,\quad c=p+q+r+s.
\]

Then

\[
\begin{aligned}
\Delta={}&\frac34p^2r^2+\frac12pr^2(s+r+2q)
 +\frac12qr^2(s+r)\\
&+q^2\left[\frac{(s+2r)^2}{4}+\frac{r^2}{4}\right]
 +\frac13q^3(s+2r)+\frac16q^4\ge0.
\end{aligned}
\tag{36}
\]

Finally, the gain is active exactly when \(x\ge(a+b)/2\). Substitute

\[
a=p,\quad x=p+2q+r,\quad b=p+2q+2r,
\quad c=p+2q+2r+s.
\]

After including the gain in \(F_S\), identity (34) becomes

\[
\begin{aligned}
\Delta={}&\frac34p^2r^2+\frac12pr^2(s+3r+4q)\\
&+s^2\left(\frac14r^2+qr+\frac12q^2\right)\\
&+s\left(\frac{11}{6}r^3+7qr^2+7q^2r+\frac73q^3\right)\\
&+\frac{31}{12}r^4+\frac{34}{3}qr^3
 +\frac{33}{2}q^2r^2+\frac{31}{3}q^3r
 +\frac{31}{12}q^4\ge0.
\end{aligned}
\tag{37}
\]

All variables in (35)--(37) are nonnegative. These cases prove (28) when
\(L=S\).

It remains to allow central slack. Fix effective smaller caps

\[
0\le x\le b,\qquad0\le y,z\le a,
\]

for the horns based at \(a,b,c\), respectively; by (32), their larger caps
are \(c,c,b\). First omit the possible gain and define

\[
\begin{aligned}
G(L)={}&abc\left(2L-\frac32S\right)
 -H_L(a;x,c)-H_L(b;y,c)-H_L(c;z,b).
\end{aligned}
\tag{38}
\]

For \(L=S+\delta\), direct expansion gives

\[
G(S+\delta)=G(S)+\delta\Lambda
 +\frac{\delta^2}{2}(cx+cy+bz),
\tag{39}
\]

where

\[
\begin{aligned}
\Lambda={}&2abc-f_a(x)-f_b(y)-f_c(z),\\
f_a(t)={}&\frac{t^3}{6}+\frac{ct^2}{2}+c(a-b)t,\\
f_b(t)={}&\frac{t^3}{6}+\frac{ct^2}{2}+c(b-a)t,\\
f_c(t)={}&\frac{t^3}{6}+\frac{bt^2}{2}+b(c-a)t.
\end{aligned}
\tag{40}
\]

These three functions are convex on their intervals; \(f_b,f_c\) are
nondecreasing, while \(f_a\) is maximized at \(0\) or \(b\). At those two
endpoint choices, respectively,

\[
\Lambda\ge
a^2\left(\frac{b+c}{2}-\frac a3\right)\ge0,
\]

\[
\Lambda\ge
\frac{(b-a)^2[2(b-a)+3(c-b)]}{6}\ge0.
\tag{41}
\]

Thus the gain-free deficit is nondecreasing in \(L\). At \(L=S\), it is
nonnegative for every \(x,y,z\): equations (35)--(37) handle the largest
possible \(b\)- and \(c\)-horns, whose full smaller cap is \(a\).

Only the horn based at \(a\) can have the extra gain from (12), because
\(c+2y\le S\) and \(b+2z\le S\) for the other two. Its gain

\[
g((c+2x-L)_+,c-x)
\]

is nonincreasing in \(L\). Subtracting it preserves the monotonicity of the
full deficit. Since the saturated deficit is nonnegative by (35)--(37), it
remains nonnegative for \(L\ge S\). Maximizing the three horns independently
proves (28). \(\square\)

#### Theorem 5.2 (continuous no-corner inequality)

Every positive-volume box-horn set \(K\) of height one satisfies

\[
\boxed{
\frac1{\operatorname{vol}K}
\int_K(x_1+x_2+x_3)\,dx\le\frac23.
}
\tag{42}
\]

#### Proof

Apply Lemma 4.1 to the three horns and then Lemma 5.1 with \(L=1\).
Their total contribution to (8) is at most

\[
abc\left(2-\frac32(a+b+c)\right),
\]

which is the negative of the central contribution (10). Hence
\(\mathcal J(K)\le0\), which is (42). \(\square\)


### C.6. Application to the thickening

The rectangular thickening of proof Section 4, after positive diagonal
scaling, has the box-horn form proved in Appendix A. Its simplex containment
and the preceding theorem give its deficit at least one third.
The box side lengths named \(a,b,c\) in this appendix are local geometric
variables, not the semigroup conductor or normalized generator weights.

### C.7. The degree-four cardinality bound


#### Lemma 7.1

If \(T\) has no full-support minimal exclusion and every point of \(T\) has
total degree at most four, then

\[
|T|\le29.
\tag{44}
\]

#### Proof

Use the Appendix A decomposition with central point
\(q=(q_1,q_2,q_3)\). Necessarily \(|q|_1\le4\). At horn \(i\), level
\(t>q_i\), its rectangular section has caps \(r\le q_j\), \(s\le q_k\) and
\(t+r+s\le4\). Consequently

\[
\begin{aligned}
|T|\le{}&\prod_{i=1}^3(q_i+1)\\
&+\sum_{i=1}^3\sum_{t=q_i+1}^4
\max_{\substack{0\le r\le q_j,\ 0\le s\le q_k\\t+r+s\le4}}
(r+1)(s+1).
\end{aligned}
\tag{45}
\]

Dropping the nesting relation between successive sections only enlarges this
upper bound. The expression is symmetric in \(q\), so the possible sorted
central triples and their values in (45) are:

| \(q\) | Bound in (45) | \(q\) | Bound in (45) |
|---|---:|---|---:|
| \((0,0,0)\) | 13 | \((0,0,1)\) | 19 |
| \((0,0,2)\) | 23 | \((0,0,3)\) | 25 |
| \((0,0,4)\) | 25 | \((0,1,1)\) | 25 |
| \((0,1,2)\) | 28 | \((0,1,3)\) | 28 |
| \((0,2,2)\) | 28 | \((1,1,1)\) | 29 |
| \((1,1,2)\) | 29 |  |  |

These are all partitions into at most three parts of an integer at most four.
The largest entry is \(29\), proving (44). \(\square\)
