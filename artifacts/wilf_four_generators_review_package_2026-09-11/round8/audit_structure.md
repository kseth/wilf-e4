# Fresh adversarial audit of the central-box and rectangular-horn theorem

11 September 2026.

**Finding:** the structural theorem is valid. In particular, the tree-median
monotonicity step does follow from the running-intersection property, but
it needs the path argument given below. No counterexample was found.
This note gives a self-contained existence proof of the tree and the
decomposition; it does not use a previous audit verdict. It separately
checks why the shape recurrence covers the entire claimed class.

The audit read the structural argument in
`round3/no_interior/clique_tree_and_bipartite_bound.md`, the finite-strip
argument and evaluator in `round7/uniform_gap_theorem.md` and
`round7/verify_uniform_gap.js`, and the high-height recurrence description
in `round7/geometric_residual.md`. It does not claim to replay the large
interval certificate or to audit unrelated Wilf dependencies.

## 1. Precise statement

Let $U\subset\mathbb N^3$ be a nonempty finite lower ideal. Suppose
no coordinatewise minimal point of $\mathbb N^3\setminus U$ has three
positive coordinates. Then some $c\in U$ gives a disjoint partition

\[
U=B(c)\mathbin{\dot\cup} A_1\mathbin{\dot\cup} A_2
\mathbin{\dot\cup} A_3,
\qquad B(c)=\prod_{i=1}^3[0,c_i]\cap\mathbb N^3.
\]

For each $i$, the possibly empty set $A_i$ lies at levels $x_i>c_i$.
At each such level its section is an integer rectangle

\[
\{t\}\times[0,r_t]\times[0,s_t]
\]

after permuting the axes. Its transverse caps are at most the corresponding
caps of $c$, and both caps are nonincreasing with $t$. Nonempty levels
form an initial interval starting at $c_i+1$. Missing coordinate units,
zero central caps, a single box, and empty arms are all allowed.

## 2. A self-contained clique-tree construction

First, membership in $U$ is determined by the three coordinate planes:

\[
(x,y,z)\in U\iff (x,y,0),(x,0,z),(0,y,z)\in U. \tag{2.1}
\]

The forward implication is downward closure. For the converse, an excluded
point dominates a minimal excluded point. Under the hypothesis the latter
lies in a coordinate plane, contradicting the three plane memberships.

For each coordinate $i$, introduce vertices $(i,t)$, where $0\le t\le h_i$
and $h_i$ is the largest coordinate-$i$ axis level in $U$. Each
coordinate class is a clique. Between different classes, join $(i,t)$
and $(j,s)$ exactly when $t e_i+s e_j\in U$. The three zero-level
vertices are universal, so this graph is connected. For $t'<t$, the
external neighborhood of $(i,t)$ is contained in that of $(i,t')$.

The graph has no induced cycle of length at least four. Indeed, any such
cycle repeats a coordinate class, because there are only three classes.
As the class is a clique, it can occur at most twice and its two occurrences
must be consecutive on the cycle. If their levels are $t'<t$, the other
cycle neighbor of $(i,t)$ belongs to a different class and is adjacent
also to $(i,t')$. This is a chord. Thus the graph is chordal.

For completeness, here is the finite chordal-graph result needed next,
with a proof instead of an external dependency.

**Clique-tree lemma.** The distinct maximal cliques of a nonempty connected
chordal graph admit a tree in which the nodes containing any fixed graph
vertex form a connected set.

**Proof.** Induct on the number of graph vertices. A complete graph has a
one-node tree. Otherwise choose nonadjacent vertices $a,b$ and an
inclusion-minimal set $Q$ separating them. For every $q\in Q$, minimality
gives neighbors of $q$ in both the component $C_a$ containing $a$ and
the component $C_b$ containing $b$ in the graph minus $Q$.
If $q,r\in Q$ were nonadjacent, a shortest $q$-to-$r$ path with internal
vertices in $C_a$, together with one with internal vertices in $C_b$,
would be an induced cycle of length at least four. Each path is induced
by shortestness, and there are no edges between the two components.
This contradicts chordality. Therefore $Q$ is a clique.

Let $C_1,\ldots,C_k$, $k\ge2$, be all components of the graph minus $Q$.
Each induced graph on $C_j\cup Q$ is connected, chordal, and smaller.
Apply induction, and in each resulting clique tree choose a bag $K_j$
containing $Q$. Join the $K_j$ in a star. The result is a tree of clique
bags with the required connectedness for every graph vertex: outside $Q$
the vertex occurs in only one component tree, and inside $Q$ the star
joins its connected component subtrees. Every global maximal clique occurs
as one of these bags, because a clique cannot meet two different $C_j$.

Remove any bag $B$ contained in another bag $C$. Along the tree path
from $B$ to $C$, the neighbor of $B$ contains every vertex of $B$,
by the connectedness property. Contract that edge, retaining the neighbor's
bag. This preserves the property. Repeating removes nonmaximal bags and
duplicate maximal bags and leaves exactly one node for each distinct
global maximal clique. This proves the lemma. \(\square\)

In our graph, every maximal clique contains a prefix of each coordinate
class: any lower level can be adjoined whenever a higher one occurs.
Equation (2.1) says that the three largest levels in the clique form a
point of $U$. Conversely, every point of $U$ gives a clique of three
prefixes. Inclusion of these prefix cliques is precisely coordinatewise
comparison of their upper corners. Consequently maximal cliques correspond
bijectively to maximal points $z\in U$, and hence to maximal boxes $B(z)$.

The clique-tree lemma therefore supplies a tree \(\mathcal T\) on the
maximal points such that

\[
\{z:z_i\ge t\}\text{ is connected whenever nonempty}. \tag{2.2}
\]

The familiar original subtree-intersection reference is F. Gavril,
*The intersection graphs of subtrees in trees are exactly the chordal
graphs*, Journal of Combinatorial Theory, Series B **16** (1974), 47–56,
DOI [10.1016/0095-8956(74)90094-X](https://doi.org/10.1016/0095-8956(74)90094-X).
The proof above makes this audit independent of that reference; the
publisher's full text was not available through the search interface.

## 3. Why the median gives precisely three monotone paths

Write $z(v)$ for the maximal point labeling tree node $v$. Distinct
node labels are incomparable. If a leaf $v$ has neighbor $w$, choose a
coordinate $i$ with $z_i(v)>z_i(w)$. If any other node $u$ had

\[
z_i(u)\ge z_i(v),
\]

then the superlevel set in (2.2) at threshold $z_i(v)$ would contain $u,v$
but not $w$, although the $u$-to-$v$ path passes through $w$.
Therefore $v$ is the unique global maximizer of coordinate $i$.
In particular there are at most three leaves.

For each coordinate $i$, choose any node $s_i$ maximizing $z_i$.
Every leaf is among the selected nodes $s_1,s_2,s_3$, by the uniqueness
just proved. Thus the whole tree is the minimal subtree spanning these
three selected nodes. To see this explicitly, a component outside that
spanning subtree would terminate in a leaf of the original tree that
was not selected.

Let $r$ be the median of $s_1,s_2,s_3$, namely the unique common node of
their three pairwise paths. Repeated selected nodes are permitted. The
paths $P(r,s_i)$ cover the tree, and distinct nontrivial paths meet only
at $r$. They are the at most three arms. Set $c=z(r)$.

Consider an edge $u v$ on a nontrivial path $P(r,s_i)$, oriented away
from $r$. The node $v$ lies on $P(u,s_i)$. If $z_i(u)>z_i(v)$,
the coordinate-$i$ superlevel set at $z_i(u)$ contains $u,s_i$ but not
$v$, contradicting (2.2). Hence

\[
z_i(u)\le z_i(v). \tag{3.1}
\]

Now fix $j\ne i$. The median property puts $s_j$ at $r$ or on another
arm. Therefore $u$ lies on the path $P(v,s_j)$. If
$z_j(v)>z_j(u)$, the coordinate-$j$ superlevel set at $z_j(v)$
contains $v,s_j$ but not $u$, again contradicting (2.2). Hence

\[
z_j(u)\ge z_j(v),\qquad j\ne i. \tag{3.2}
\]

This is the precise reason why an arm toward one coordinate maximum
cannot increase either other coordinate. It uses the location of the
other coordinate's selected global maximizer on the opposite side of
the edge; connected superlevels without that location would not suffice.

Finally, equality in (3.1), together with (3.2), would give
$z(v)\le z(u)$, contrary to the incomparability of distinct maximal
points. Thus coordinate $i$ increases strictly along its nontrivial arm.
The argument also handles a path with the median at an interior node
or endpoint, and a one-node tree has no arms.

## 4. Disjoint sections and a constructive formula

All boxes on arm $i$ stay below $c_j$ for $j\ne i$. Their outward
caps $z_i$ strictly increase and their transverse caps weakly decrease.
At an integer level $t>c_i$, boxes from the center or any other arm
contribute nothing. Among boxes on arm $i$, let $v(t)$ be the first
node whose outward cap is at least $t$, if such a node exists. The
transverse rectangles of all later contributing boxes are contained in
the rectangle of $v(t)$. Therefore the entire section equals

\[
\prod_{j\ne i}[0,z_j(v(t))]\cap\mathbb N^2. \tag{4.1}
\]

The index $v(t)$ moves weakly outward with $t$, so both side lengths
in (4.1) are nonincreasing. There is no skipped nonempty level because
each contributing box reaches all smaller coordinate-$i$ levels.
Every point outside $B(c)$ exceeds a central cap in exactly one
coordinate, since the union of maximal boxes is $U$. Therefore the
central box and the three collections (4.1) are disjoint and exhaust $U$.
This proves the theorem constructively once any clique tree is supplied.

## 5. Coverage of the clipped-rectangle recurrence

If $T$ has exactly one full-support minimal excluded point $p>0$, delete
that generator of the excluded monomial ideal. The remaining generators
have support at most two, and define a lower ideal $U$ of the preceding
class. All original pure-axis exclusions remain, so $U$ is finite.
Moreover

\[
T=U\setminus(p+\mathbb N^3).
\]

Clipping the disjoint decomposition of $U$ preserves disjointness.
For a fixed outward level $t$, the uncut transverse section has caps
$(r,s)$, and later caps are bounded by $(r,s)$. An exact upper bound
on an additive score is consequently obtained by taking the maximum of
termination and every choice of a feasible current rectangle, followed
by the optimum continuation with those caps. Feasibility must be tested
on retained points after clipping. This is precisely the recurrence
stated in Section 3.2 of `round7/uniform_gap_theorem.md`.

The implementation by prefix maxima is equivalent: every proper
subrectangle either reduces the first cap or reduces the second cap,
so comparisons with those two predecessor cap states enumerate every
choice. Clipping may make some nonminimal or inactive $p$ choices
admissible, but these only enlarge the optimization class. Independent
optimization of the three arms similarly cannot lose an actual ideal.
Axis points survive $p>0$, so a height bound supplies the axis cutoff
for $U$ itself and not merely for its clipped part.

No failure of geometric coverage or of this recurrence was identified.
This conclusion concerns the mathematical scope of the recurrence;
large certificate arithmetic and file provenance require their separate
audits.

## 6. Fresh exact finite challenge

`round8/check_structure_fresh.py` imports no earlier project code and uses
no graph or tree algorithm. Every two-dimensional lower ideal in a
four-by-four square is represented by a nonincreasing sequence of four
row lengths in \(\{0,1,2,3,4\}\). There are 70 such profiles. Their
343,000 ordered triples give every no-interior ideal contained in
\(\{0,1,2,3\}^3\) by intersecting the three plane-cylinder conditions.
Duplicate resulting point sets are removed.

For every distinct nonempty ideal, the program checks minimal excluded
points directly, tries each possible central point, tests literal
sections for rectangularity and nested caps, and reconstructs the
disjoint pieces point by point. The actual completed output is:

| Check | Result |
|---|---:|
| Profile triples tested | 343,000 |
| Distinct nonempty ideals | 18,212 |
| Ideals without a valid decomposition | 0 |
| Largest ideal cardinality | 64 |
| Largest number of maximal points | 7 |
| Minimum number of valid centers | 1 |

As a second finite challenge, all these closures were clipped by each
sorted positive corner possible for total-degree allowance 3. Direct
enumeration of every feasible clipped closure was compared with a newly
written literal-point rectangle recursion. The score here is
\(\sum_T(4|x|_1-5)\); no claim that it is nonpositive is made at this small
height.

| Corner | Exhaustively feasible closures | Brute-force maximum | Recurrence maximum |
|---|---:|---:|---:|
| \((1,1,1)\) | 1,768 | 73 | 73 |
| \((1,1,2)\) | 1,480 | 66 | 66 |

The finite checks took approximately six seconds in this session and
passed. They are a challenge to the proof and implementation model, not
a substitute for the universal argument in Sections 1–5.

Run `python3 round8/check_structure_fresh.py` to reproduce them. Its
machine-readable report is `round8/check_structure_fresh.json`, which
also records the exact source SHA-256.
