# Short-corner low-height profiles and residue filters

## Status and purpose

This note completes roadmap task B4.3. It proves the necessary arithmetic
restrictions on the three plane frontiers, defines a finite profile family,
and proves that the family covers every B4 preferred Apéry ideal with
\(H<6\), up to a simultaneous permutation of coordinates and generators.

The [B4.1 split](short-corner-height-split.md) gives
\(T\subseteq\Delta_5\) and \(30\le m\le48\). The family below is a geometric
superset of those genuine ideals, not a classification of realizable
semigroups. It has no residue-label search, weight grid, or six-maxima skip.

This is a specification and coverage proof, not a replay of the historical
centroid duals. The finite weighted obligation is stated in Section 6; B4.4
must supply its exact certificate semantics, D4 must decide whether to retain
the computation, and R4b must replay it if retained.

## 1. The arithmetic frontier restrictions

Let \(T\) be a preferred Apéry ideal for
\(S=\langle m,a_1,a_2,a_3\rangle\), and orient its full-support corner as
\(p=(2,1,1)\). Write

\[
\lambda(x)=a\cdot x,\qquad
h_i=\max\{t:te_i\in T\}.
\tag{1}
\]

Let \(\rho(q)\in T\) be the unique representative of the residue of
\(\lambda(q)\) modulo \(m\). The
[foundational support/collision rules](foundations.md#5-minimal-excluded-points-f3)
give

\[
\rho(p)=0,\qquad 2a_1+a_2+a_3\equiv0\pmod m.
\tag{2}
\]

A corner in a coordinate plane is *mixed* when its two plane coordinates
are positive. Its predecessor conditions in that plane are exactly the
conditions for being a corner of \(T\).

### Proposition 1.1 (necessary plane filters)

1. Each of the \(xy\) and \(xz\) planes has at most two mixed corners.
   In each, at most one mixed corner has \(x\)-coordinate at least two.
2. The \(yz\) plane has at most two mixed corners.
3. The plane sections contain \((2,1)\) in \(xy\) and \(xz\), and
   \((1,1)\) in \(yz\).

#### Proof

Consider an \(xy\) mixed corner \(q=(u,v,0)\).
The support rule forces \(\rho(q)=\gamma e_3\) with
\(0\le\gamma\le h_3\). Since \(q\) and \(p\) share a positive coordinate,
the collision rule and (2) also give \(\gamma\ne0\).

If \(u\ge2\), lower closure and minimal exclusion give

\[
r=(u-2,v-1,0)\in T.
\]

Using (2),

\[
\lambda(r)\equiv\gamma a_3-2a_1-a_2
\equiv(\gamma+1)a_3\pmod m.
\tag{3}
\]

If \(\gamma<h_3\), the positive axis point \((\gamma+1)e_3\) also belongs
to \(T\). It differs from \(r\), whose third coordinate is zero, but has the
same residue. Injectivity is contradicted. Therefore \(\gamma=h_3\).
Any two such corners would have the same residue, contrary to the collision
rule, so at most one has \(u\ge2\).

Distinct mixed corners in a planar lower ideal cannot have the same first
coordinate: they are an antichain. Thus at most one further corner has
\(u=1\). This proves the \(xy\) assertions; exchanging \(y,z\) proves
the \(xz\) assertions.

Now take a \(yz\) mixed corner \(q=(0,v,t)\), with
\(\rho(q)=\gamma e_1\), \(1\le\gamma\le h_1\).
The included point \(r=(0,v-1,t-1)\) has residue

\[
\lambda(r)\equiv\gamma a_1-a_2-a_3
\equiv(\gamma+2)a_1\pmod m.
\tag{4}
\]

If \(\gamma+2\le h_1\), this again collides with a distinct positive axis
point of \(T\). Hence

\[
\gamma\in\{h_1-1,h_1\}.
\tag{5}
\]

The collision rule requires different representatives for distinct mixed
corners in this plane, so there are at most two.

Finally \(p-e_3=(2,1,0)\), \(p-e_2=(2,0,1)\), and the projection of
\(p-e_1=(1,1,1)\) into \(yz\) belong to \(T\). These give the three
required plane points. ∎

These are per-plane restrictions. No bound of two on the *total* number
of mixed corners across the three planes follows from this proposition.
No bound is imposed on the representative of an \(xy\) or \(xz\) corner
whose \(x\)-coordinate is one.

## 2. The planar profile dictionary

A profile is an integer vector \(f=(f_0,\ldots,f_5)\) with

\[
0\le f_i\le6-i,\qquad f_0\ge f_1\ge\cdots\ge f_5.
\tag{6}
\]

It represents the planar footprint

\[
F(f)=\{(u,v):0\le u\le5,\ 0\le v<f_u\}.
\tag{7}
\]

The entries are point counts, not last included coordinates: the top of
a nonempty column \(u\) is \(f_u-1\). Thus (6) is exactly the condition
that \(F(f)\) is a lower ideal in the degree-five planar triangle.
Conversely every such ideal has a unique profile (6), padded by zeros.

For a nonempty profile, put

\[
\ell(f)=|\{i:f_i>0\}|,\qquad
D(f)=\{i:1\le i<\ell(f),\ f_i<f_{i-1}\}.
\tag{8}
\]

Its axis point counts are \((\ell(f),f_0)\). Its mixed corners are exactly

\[
(i,f_i)\qquad(i\in D(f)).
\tag{9}
\]

Indeed a drop makes both predecessors of \((i,f_i)\) included.
Conversely the predecessor conditions for a mixed corner force its second
coordinate to be \(f_i>0\), and force \(f_{i-1}>f_i\).
The two pure-axis corners are \((\ell(f),0)\) and \((0,f_0)\).
In particular, a drop to a zero column is **not** a mixed corner and must not
be included in \(D(f)\).

Define two finite profile classes:

\[
\begin{aligned}
\mathcal P_x=\{f\text{ satisfying (6)}:\;&
 f_2\ge2,\ |D(f)|\le2,\\
&|\{i\in D(f):i\ge2\}|\le1\},\\
\mathcal P_{yz}=\{h\text{ satisfying (6)}:\;&
 h_1\ge2,\ |D(h)|\le2\}.
\end{aligned}
\tag{10}
\]

The conditions \(f_2\ge2\) and \(h_1\ge2\) include the plane points in
Proposition 1.1. They also rule out every mixed plane corner below those
points, so no additional predecessor-point rejection is needed.

Profiles in \(\mathcal P_x\) serve for both \(xy\) and \(xz\); profiles in
\(\mathcal P_{yz}\) serve for \(yz\).

## 3. Compatible reconstruction

Take \(f,g\in\mathcal P_x\) and \(h\in\mathcal P_{yz}\), for \(xy,xz,yz\),
respectively. Their shared-axis point counts must agree:

\[
\ell(f)=\ell(g),\qquad f_0=\ell(h),\qquad g_0=h_0.
\tag{11}
\]

For a compatible triple, define

\[
U(f,g,h)=
\{(x,y,z)\in\mathbb N^3:
 (x,y)\in F(f),\ (x,z)\in F(g),\ (y,z)\in F(h)\},
\]
\[
T(f,g,h)=U(f,g,h)\setminus\bigl((2,1,1)+\mathbb N^3\bigr).
\tag{12}
\]

All coordinates of \(U\) are at most five. On \(\{0,\ldots,5\}^3\), its
membership tests are simply \(y<f_x,\ z<g_x,\ z<h_y\).

### Lemma 3.1 (exact reconstruction)

A compatible triple gives a finite lower ideal \(T(f,g,h)\) whose plane
sections are exactly \(F(f),F(g),F(h)\), and whose sole full-support corner
is \((2,1,1)\). Conversely, every preferred B4 ideal of degree at most five
is given by (12) for a unique compatible triple in (10).

#### Proof

All three pair conditions in (12) are lower-closed, and removing an upper
orthant preserves lower closure.

For the \(xy\) section, a point \((x,y)\in F(f)\) has
\(x<\ell(f)=\ell(g)\) and \(y<f_x\le f_0=\ell(h)\).
Hence \(g_x,h_y>0\), so \((x,y,0)\) satisfies the other two pair tests.
The removed orthant cannot affect this plane. This proves that its section
is exactly \(F(f)\); the other two sections follow in the same way.

The conditions in (10) and monotonicity give \(f_1,g_1,h_1\ge2\).
It follows that all three predecessors \((1,1,1),(2,0,1),(2,1,0)\) of
\(p\) belong to (12), so \(p\) is minimal excluded. A point excluded by a
pair condition remains excluded after setting the omitted coordinate to
zero, and cannot be a full-support minimal exclusion. Any other excluded
point dominates \(p\), so \(p\) is the sole full-support corner.

For the converse, take the plane sections of a genuine ideal \(T\).
Lower closure identifies each section with its corresponding projection.
The degree bound gives (6), Proposition 1.1 gives (10), and the common
axes give (11). Certainly \(T\subseteq T(f,g,h)\).

If a point of \(T(f,g,h)\) were outside \(T\), it would dominate some
minimal exclusion \(q\) of \(T\). This cannot be \(p\), because the point
is not above \(p\). By the foundational uniqueness rule, \(q\) lies in a
coordinate plane. The corresponding pair test in (12) and lower closure
of that plane section then put \(q\) in \(T\), a contradiction.
This proves equality.

Finally the three recovered plane sections uniquely determine their padded
profiles, so two compatible triples cannot encode the same oriented ideal. ∎

The proof is direct and does not invoke the superseded B3 six-window
specification. It is pairwise footprint reconstruction followed by one
upper-orthant deletion, not an additional assumption on genuine ideals.

## 4. The final degree check and cardinality

The profile bounds in (6) control each plane section, not automatically
the degree of the reconstructed ideal.

For example, the compatible profiles

\[
f=g=(4,4,2,0,0,0),\qquad h=(4,4,4,3,0,0)
\tag{13}
\]

satisfy (10). Their reconstruction has 33 points and contains \((1,2,3)\),
of degree six. It must be rejected from the degree-five family.

There is a short exact test. Every retained point with three positive
coordinates has \(x=1\). At that level the allowed column lengths are

\[
c_y=\min(g_1,h_y)\qquad(0\le y<f_1).
\tag{14}
\]

Thus its top point has degree \(1+y+(c_y-1)=y+c_y\). The \(y=0\)
column already satisfies the planar \(xz\) bound, and all other coordinate
planes already have degree at most five. Therefore

\[
\boxed{T(f,g,h)\subseteq\Delta_5
\quad\Longleftrightarrow\quad
y+\min(g_1,h_y)\le5
\quad(1\le y<f_1).}
\tag{15}
\]

Compatibility ensures \(h_y>0\) in this range, so the top used in this
test always exists. Since \(f_1\le5\), (15) needs at most four integer
inequalities. It remains valid for \(c_y=1\), when that column lies in
the \(xy\) plane.

The same decomposition gives an exact cardinality formula. At \(x=0\)
the section is \(F(h)\); at \(x=1\) use (14). At \(x\ge2\), deleting the
corner orthant leaves the two axis lines of lengths \(f_x,g_x\), meeting
at one point. Consequently

\[
\boxed{
m(f,g,h)=
\sum_{y=0}^{5}h_y+
\sum_{y=0}^{f_1-1}\min(g_1,h_y)+
\sum_{x=2}^{\ell(f)-1}(f_x+g_x-1).
}
\tag{16}
\]

An empty sum is zero. All entries and calculations are integers.

## 5. Exhaustive generation and canonical keys

Let \(\mathcal F_5\) consist of every compatible ordered triple in (10)
satisfying (15), with associated ideal (12). Let

\[
\mathcal F_5^{\ge30}
=\{(f,g,h)\in\mathcal F_5:30\le m(f,g,h)\le48\}.
\tag{17}
\]

The upper cardinality bound is redundant by B4.1, but may be checked as a
consistency invariant.

A complete generator has the following code-independent specification.

1. List every integer vector satisfying (6). One method recursively chooses
   \(f_i\) from \(0\) through
   \(\min(6-i,f_{i-1})\), taking \(6\) as the initial cap. Another lists
   the Cartesian product of the six allowed coordinate ranges and tests
   monotonicity.
2. Apply exactly the profile tests (10), obtaining the two profile classes.
3. List every ordered triple
   \(\mathcal P_x\times\mathcal P_x\times\mathcal P_{yz}\).
   An index by axis point counts may accelerate (11), provided it omits
   only incompatible triples.
4. Retain precisely the triples satisfying (11) and (15).
5. Compute (16), requiring \(m\le48\) as a consistency invariant, and retain
   \(m\ge30\) for the weighted obligation. The first moment \(s\) is the
   literal sum of the points in (12).

### Theorem 5.1 (coverage and termination)

Every genuine B4 ideal with \(H<6\) occurs in \(\mathcal F_5^{\ge30}\) after
orienting its corner as \((2,1,1)\). This generation terminates, and each
oriented ideal has one profile key.

#### Proof

B4.1 gives degree at most five and cardinality \(30\le m\le48\).
Proposition 1.1 and the profile dictionary put its three sections in (10).
Lemma 3.1 supplies their compatibility, reconstruction, and uniqueness.
Its degree bound implies (15), so no specified rejection loses it.

Before filtering there are at most
\(7\cdot6\cdot5\cdot4\cdot3\cdot2=5{,}040\) profile vectors.
Each step operates on finite lists and at most \(6^3\) literal grid points
per reconstruction, so termination is immediate. ∎

The canonical oriented key is the ordered triple of six-entry integer
vectors \((f,g,h)\), including zero tails. The \(xy\) and \(xz\) profiles
are not sorted or identified: exchanging \(y,z\) may give another oriented
key. This harmless duplication of permutation classes avoids any need for
a symmetry-lifting argument.

Weights are not sorted during profile generation. A coordinate permutation
used to orient the corner must be applied to the generator labels or weights
as well. The weighted obligation quantifies over all three weights, so it
still covers every position of the least weight relative to the doubled
corner coordinate.

## 6. The finite weighted obligation

The contract for the low-height alternative is the following:

> **B4-low-FV.** For every key in \(\mathcal F_5^{\ge30}\), let
> \(T=T(f,g,h)\), \(m=|T|\), and \(s=\sum_{x\in T}x\). For every real
> \(w=(w_1,w_2,w_3)\) with \(w_i\ge1\), and every real height allowance
> \(Q\ge\max_{x\in T}w\cdot x\), prove
> \[
> 3mQ-4w\cdot s\ge m-1.
> \tag{18}
> \]

This is stronger than restricting \(Q<6\) and \(\min_i w_i=1\), but it is
the all-weight statement targeted by the historical centroid duals. The
weights are real, not a finite grid, and the allowance need not be attained.

B4.4 must specify and prove the exact rational certificate predicate
sufficient for (18). A complete retained checker must reconstruct every
key and its point set and moment, check its certificate exactly, and reject
missing, duplicate, malformed, or unused records. A success count or
floating-point optimization status is not an acceptance predicate.

No dual is replayed in this task, and B4-low-FV is not established by the
coverage proof. If it is later established, Theorem 5.1 applies it to the
normalized genuine weights \(w_i=a_i/A\) and attained height \(Q=H\),
giving the B4 low-height target \(D_0\ge m-1\).

## 7. Rejection boundaries and provenance

The allowed exclusions have the following precise justifications:

| Rejection | Justification |
|---|---|
| A profile violates (6) | It is not a lower ideal in the degree-five planar triangle. |
| A required profile entry is below two | A plane projection of a predecessor of \(p\) is missing. |
| Too many positive-height drops, or too many drops at \(x\ge2\) | Proposition 1.1, with the dictionary (9). |
| Shared axes disagree | A single ideal cannot have different footprints on the same axis. |
| A row fails (15) | The reconstruction contains a point of degree above five. |
| Cardinality below 30 | The B4 routing condition does not assign it to this branch. |

Cardinality above 48 should be impossible after the other tests, by B4.1;
it is not an additional empirical arithmetic filter. In particular, no
rejection based on maxima count, a six-window theorem, observed
nonrealizability, or an unproved numerical threshold is permitted.
The definition includes every surviving degree-four ideal as well as the
degree-five ideals.

The historical arithmetic forcing argument is in the
[short-interior cell note](../artifacts/wilf_four_generators_review_package_2026-09-11/round5/interior_arithmetic/short_interior_cell_theorem.md).
The historical [producer](../artifacts/wilf_four_generators_review_package_2026-09-11/round5/interior_arithmetic/low_height_weighted_certificate.py)
uses recursive profiles; the [independent verifier](../artifacts/wilf_four_generators_review_package_2026-09-11/round5/interior_arithmetic/verify_low_height_weighted.py)
uses Cartesian-product profiles and direct membership tests.
Their reported totals of 70,175 degree-five shapes, 28,499 eligible
certificates, and maximum cardinality 43 remain comparison targets, not
retained proof inputs at this stage. The analytic bound 48 remains the
cardinality interface.

The foundational exclusion rules retain their upstream attribution. The
one-orthant reconstruction is compatible with Chomicz's relation-deletion
L-shape viewpoint; no additional theorem from it is needed here. See the
[focused assessment](../research/chomicz-assessment.md). L3 will refresh
attribution for the final retained branch statements.

## 8. Construction diagnostic

The standalone [diagnostic](../research/check_b4_low_height_profiles.py)
imports neither archived generation code nor certificates. It compares
recursive and Cartesian-product profile generation, checks the corner
dictionary against literal plane sets, compares axis-indexed and direct
triple generation, and reconstructs every compatible ideal in two ways.
It also checks lower closure, recovery of its three sections, the short
degree test (15), and the cardinality formula (16).

Commands, run on 2026-09-16:

    python3 research/check_b4_low_height_profiles.py --degree-cap 4
    python3 research/check_b4_low_height_profiles.py --degree-cap 5

| Degree cap | Compatible triples | Degree-filtered shapes | Cardinality at least 30 | Largest cardinality |
|---|---|---|---|---|
| 4 | 4,824 | 3,928 | 0 | 29 |
| 5 | 81,373 | 70,175 | 28,499 | 43 |

At cap five the two profile classes have 145 and 265 members. All
construction checks passed, and the degree-filtered counts agree with the
historical reports. These are construction diagnostics only: no weighted
certificate is checked, no replay obligation is discharged, and no empirical
sharpening of the analytic range \(30\le m\le48\) is adopted.

A separate bounded diagnostic constructed preferred Apéry ideals for the
3,952 coprime generator tuples with \(30\le m\le48\) and
\(m<a_1<a_2<a_3\le m+12\). All are minimally generated since
\(a_i<2m\). It found 28 low-height short-corner ideals, with the doubled
coordinate in all three positions; their residue forcing and reconstructed
profiles passed. This sampled semigroup check is not a proof by generator
exhaustion and does not establish B4-low-FV.
