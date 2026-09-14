# Central boxes and three monotone horns

## Status and purpose

This note completes task G5. It proves that every finite three-dimensional
lower ideal with no full-support minimal exclusion is a central anchored box
together with at most three disjoint coordinate horns whose transverse
rectangles are nested. It then proves the clipped form used when one
full-support corner is present and isolates the exact recurrence interface
used later in B2 and B6. There is no computer-assisted assertion here.

The only general graph-theoretic ingredient is the standard clique-tree
characterization of chordal graphs, associated in particular with Gavril's
subtree characterization. A short proof of the needed finite form is included
below, so the geometric theorem does not depend on accepting that citation as
a black box.

## 1. Statement

For \(r\in\mathbb N\), write \([r]=\{0,1,\ldots,r\}\). For
\(z\in\mathbb N^3\), let

\[
\mathcal B(z)=[z_1]\times[z_2]\times[z_3].
\]

### Theorem 1.1 (central-box/three-horn decomposition)

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

## 2. Plane determination and the compatibility graph

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

### Lemma 2.1

The graph \(G\) is chordal.

#### Proof

Suppose an induced cycle has length at least four. Because there are only
three coordinate classes, it repeats a class. An induced cycle can contain at
most two vertices from a clique, and those two must be consecutive. Write
their levels as \(t'<t\). The other cycle neighbor of
\((i,t)\) lies outside \(V_i\); by (5), it is also adjacent to \((i,t')\).
This is a chord, a contradiction. \(\square\)

## 3. The required clique-tree lemma

### Lemma 3.1 (clique tree)

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

## 4. From maximal cliques to maximal boxes

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

## 5. The median and the three arms

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

## 6. Disjoint rectangular sections

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
nonincreasing. Thus the thickened sets in
[`phase-and-thickening.md`](phase-and-thickening.md) belong to the same
central-box/three-horn geometric class, up to null boundary conventions.

## 7. One full-support corner

Let \(T\subseteq\mathbb N^3\) be a finite lower ideal with exactly one
full-support minimal excluded point \(p\). Let \(P\) be the set of all
minimal excluded points of \(T\), and define

\[
U=\mathbb N^3\setminus
\bigcup_{q\in P\setminus\{p\}}(q+\mathbb N^3).
\tag{10}
\]

### Corollary 7.1 (one-corner clipping)

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

## 8. Exact recurrence interface

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
height allowances, and interval bounds belong to the later B2 and B6
specifications rather than to G5.

## 9. Retained interface

Later notes may use G5 through the following statements only:

1. plane determination (4);
2. the disjoint central-box/three-horn representation (1)--(3);
3. exact one-corner removal and slice clipping (11)--(13);
4. exhaustive nested-cap recurrence (14).

The clique tree is a proof device. Its nonuniqueness, the unused tree
inclusion--exclusion formulas in the historical archive, and earlier
continuous horn-optimization variants are not part of the retained proof
interface.
