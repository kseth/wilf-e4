# The six-window shape-generation specification

## Status and purpose

This note completes roadmap task B3.2. It gives a code-independent finite
shape specification for the case

\[
1\le |Z|\le6,
\]

and proves that every negative projection-score pair \((T,Z)\) arising from
a preferred four-generator Apéry ideal occurs in that finite family, up to a
simultaneous coordinate permutation.

The proof covers rank compression, the exact one-corner completion test,
strict growth under coordinate-level insertion, exhaustive lower-ideal
extension, canonicalization, and termination. It uses the
[final-window projection inequality](final-window-projection.md), the
[six-maxima entry lemma](six-maxima-entry.md), and the
[verification trust policy](../verification/trust-policy.md).

The upper-orthant language is compatible with Chomicz's relation-deletion
description of three-dimensional L-shapes, but the completion and coverage
theorems below are proved directly; see the
[focused assessment](../research/chomicz-assessment.md).

This is a **specification and coverage proof**, not a replay result. It does
not establish the modular arithmetic predicate deferred to B3.3, endorse the
historical output counts, or promote the archived generator under V0.

## 1. The geometric target

Use the coordinatewise order on \(\mathbb N^3\). For a finite nonempty
antichain \(Z\subseteq\mathbb N^3\), let

\[
U(Z)=\bigcup_{z\in Z}[0,z]
\tag{1}
\]

be its lower hull. Let \(\pi_i\) delete coordinate \(i\), and for a finite
lower ideal \(Q\) put

\[
P(Q)=\sum_{i=1}^3|\pi_iQ|.
\tag{2}
\]

For \(k=|Z|\), define

\[
E(Z)=\sum_{z\in Z}|z|_1-\sum_{i=1}^3\max_{z\in Z}z_i
\tag{3}
\]

and

\[
\Phi(Q,Z)=P(Q)-3k-E(Z),
\qquad
\Phi_0(Z)=\Phi(U(Z),Z).
\tag{4}
\]

Suppose now that \(T\) is a preferred Apéry ideal and \(Z\) is its final
window. The G3 estimate is

\[
mW_4(S)\ge m\Phi(T,Z)+E(Z).
\tag{5}
\]

Since \(E(Z)\ge0\), only the strict case

\[
\Phi(T,Z)<0
\tag{6}
\]

requires a finite argument. Equality in (6) is deliberately excluded from
the finite domain because \(\Phi=0\) is already accepted by (5). By B3.1,
the branch with corner \((1,1,1)\) has \(1\le k\le6\).

Every preferred Apéry ideal contains \(e_1,e_2,e_3\), has at most one
full-support corner, and has \(Z\subseteq\operatorname{Max}(T)\). The shape
generator may therefore impose all three conditions. They are necessary
filters, not claims that every surviving shape is arithmetically realizable.

## 2. Pairwise closure and the exact completion test

The subtle point in compressing \(Z\) is that a compressed antichain need not
itself be the maximal set of its lower hull. We first decide, using only
coordinate comparisons, whether it can be maximal in *some* lower ideal with
at most one full-support corner.

### 2.1 Pairwise reconstruction

For a finite lower ideal \(Q\subseteq\mathbb N^3\), define its pairwise
closure by

\[
\widehat Q
=\{x\in\mathbb N^3:\pi_i x\in\pi_iQ\text{ for }i=1,2,3\}.
\tag{7}
\]

The set \(\widehat Q\) is a lower ideal containing \(Q\), and it is finite
because each coordinate is bounded in either projection in which it appears.

### Lemma 2.1 (pairwise reconstruction)

If \(Q\) has no full-support corner, then \(Q=\widehat Q\). If \(Q\) has
exactly one full-support corner \(p\), then

\[
Q=\widehat Q\setminus(p+\mathbb N^3).
\tag{8}
\]

#### Proof

Take \(x\in\widehat Q\setminus Q\), and choose a corner \(q\le x\) of
\(Q\). If, say, \(q_i=0\), then \(\pi_iq\le\pi_ix\in\pi_iQ\). Since
\(\pi_iQ\) is a lower ideal, \(\pi_iq\in\pi_iQ\). Some point of \(Q\)
therefore has the same other two coordinates as \(q\); it dominates \(q\),
contradicting \(q\notin Q\). Thus every corner below a point of
\(\widehat Q\setminus Q\) has full support.

If there is no full-support corner, the difference is empty. If \(p\) is the
unique one, then \(p\in\widehat Q\), because
\(\pi_i p=\pi_i(p-e_i)\in\pi_iQ\) for every \(i\). Every point in the
difference dominates \(p\). Conversely, no point of \(Q\) can dominate the
excluded point \(p\). Restricting this equivalence to \(\widehat Q\) proves
(8).
\(\square\)

For the remainder of this section, fix an antichain \(Z\), put \(U=U(Z)\),
and define

\[
V=\widehat U.
\tag{9}
\]

The lower ideal \(V\) has no full-support corner. Indeed, if a full-support
point fails one of the projected conditions in (9), subtracting the unit
vector in the omitted coordinate leaves that condition unchanged, so the
point cannot be a minimal exclusion.

### 2.2 Forced successors

Call a pair \((r,z)\), with \(z\in Z\) and \(r\in\{1,2,3\}\), *forced* if

\[
z+e_r\in V.
\tag{10}
\]

Writing \(i\ne r\), condition (10) is equivalent to

\[
\text{for every }i\ne r\text{ there is }y\in Z
\text{ such that }y_i\ge z_i\text{ and }y_r>z_r.
\tag{11}
\]

Indeed, the projection omitting \(r\) is already supplied by \(z\), while
each of the other two projected pairs belongs to the lower hull exactly when
the corresponding witness in (11) exists.

Suppose a lower ideal \(Q\supseteq U\) retains every point of \(Z\) as
maximal and has at most one full-support corner. If \((r,z)\) is forced, then
\(z+e_r\in V\subseteq\widehat Q\), but \(z+e_r\notin Q\). Lemma 2.1 shows
that \(Q\) must have a full-support corner \(p\), and comparison with the
included predecessor \(z\) gives the exact constraints

\[
p_r=z_r+1,
\qquad
p_i\le z_i\quad(i\ne r).
\tag{12}
\]

Here \(p\le z+e_r\) gives all the weak inequalities, while \(z\in Q\)
means that \(p\le z\) is impossible. The only coordinate in which that
inequality can fail is \(r\), so integrality gives \(p_r=z_r+1\).

Let \(\mathcal F(Z)\) be the set of forced pairs. When it is nonempty, define
for each coordinate \(j\)

\[
R_j=\{z_j+1:(j,z)\in\mathcal F(Z)\},
\tag{13}
\]

\[
B_j=\{z_j:(r,z)\in\mathcal F(Z),\ r\ne j\}.
\tag{14}
\]

If \(R_j\) is empty, then \(B_j\) is nonempty because
\(\mathcal F(Z)\ne\varnothing\). Subject to the consistency requirements
below, define

\[
p_j^*=\begin{cases}
\text{the unique element of }R_j,&R_j\ne\varnothing,\\
\min B_j,&R_j=\varnothing.
\end{cases}
\tag{15}
\]

### Theorem 2.2 (one-corner completion criterion)

There is a finite lower ideal \(Q\supseteq U(Z)\) in which every point of
\(Z\) is maximal and which has at most one full-support corner if and only if
one of the following alternatives holds.

1. There are no forced pairs.
2. The forced set is nonempty and:
   - every \(R_j\) has at most one element;
   - if \(R_j=\{r_j\}\) and \(B_j\ne\varnothing\), then
     \(r_j\le\min B_j\);
   - every coordinate of \(p^*\) in (15) is positive; and
   - \(p^*\notin U(Z)\).

In the first alternative, \(V\) is such a completion. In the second,

\[
Q^*=V\setminus(p^*+\mathbb N^3)
\tag{16}
\]

is such a completion.

#### Proof

First suppose a completion \(Q\) exists. If there is a forced pair, the
argument preceding (12) supplies its unique possible full-support corner
\(p\), which satisfies every constraint (12). Thus all equalities prescribed
in a fixed coordinate agree, and a prescribed equality cannot exceed any
upper bound in that coordinate. The point \(p^*\) is the coordinatewise
greatest solution of these constraints, so \(p\le p^*\). If
\(p^*\in U(Z)\), lower closure would give \(p\in U(Z)\subseteq Q\), a
contradiction. Positivity follows from the full support of \(p\). This proves
necessity.

If there are no forced pairs, every successor of every \(z\in Z\) lies
outside \(V\), so \(Z\subseteq\operatorname{Max}(V)\). The set \(V\) has no
full-support corner, giving the first construction.

Now suppose the conditions in the second alternative hold. For every forced
\((r,z)\), equations (13)--(15) give

\[
p^*\le z+e_r.
\tag{17}
\]

Since \(z+e_r\in V\) and \(V\) is lower, \(p^*\in V\). Because
\(p^*\notin U(Z)\), removing its upper orthant retains \(U(Z)\). A successor
of \(z\) which is outside \(V\) is absent from \(Q^*\); a successor inside
\(V\) is forced and is removed by (17). Hence every point of \(Z\) is
maximal in \(Q^*\). Finally, \(V\) has no full-support corner, and deleting
one upper orthant introduces only the corner \(p^*\). Thus (16) is the
required completion.
\(\square\)

Passing this criterion is not sufficient for an Apéry labeling. It is only
the exact order-theoretic condition needed before shape generation.

### 2.3 Invariance under rank compression

For each coordinate \(i\), list the levels occurring in \(Z\) as

\[
\ell_{i,0}<\ell_{i,1}<\cdots<\ell_{i,d_i}.
\]

The *rank compression* \(\operatorname{comp}(Z)\) replaces
\(\ell_{i,s}\) by \(s\). It preserves every equality and strict or weak
comparison between occurring levels, and it preserves the antichain
property.

### Lemma 2.3 (compression preserves completion feasibility)

The antichain \(Z\) passes Theorem 2.2 if and only if
\(\operatorname{comp}(Z)\) does.

#### Proof

Condition (11), agreement among the values in each \(R_j\), and all
comparisons between a prescribed value and an upper bound depend only on
equalities and order among occurring levels. For integers,

\[
z_j+1\le y_j\quad\Longleftrightarrow\quad z_j<y_j,
\tag{18}
\]

so these tests survive compression.

The test \(p^*\in U(Z)\) is also order-theoretic. In a coordinate prescribed
as \(z_j+1\), the comparison \(p_j^*\le y_j\) means \(z_j<y_j\); in an
unprescribed coordinate, \(p_j^*\) is itself an occurring level and ordinary
weak comparison applies.

Only positivity needs comment. A prescribed coordinate is a successor and
is automatically positive. Suppose an unprescribed coordinate \(j\) obtains
an upper bound from a forced pair \((r,z)\), where \(r\ne j\), and let
\(s\) be the third coordinate. The witness in (11) for coordinate \(s\) has

\[
y_s\ge z_s,
\qquad
y_r>z_r.
\]

Since \(Z\) is an antichain, this forces \(y_j<z_j\). Thus every level
contributing to \(B_j\) lies strictly above another occurring \(j\)-level,
and its compressed rank is positive. All tests in Theorem 2.2 are therefore
preserved in both directions.
\(\square\)

## 3. Coordinate insertions and strict score growth

Rank compression is useful only if every original level spacing can be
restored without losing a negative candidate.

For an occurring level \(h\) in coordinate \(i\), define the insertion

\[
I_{i,h}(z)_j=
\begin{cases}
z_j+1,&j=i\text{ and }z_i\ge h,\\
z_j,&\text{otherwise}.
\end{cases}
\tag{19}
\]

for \(z\in Z\). In words, insert one new lattice level immediately below
the points at levels at least \(h\). This operation is a strictly increasing
relabeling of the occurring \(i\)-levels, so it preserves the order type,
the antichain property, and completion feasibility.

### Lemma 3.1 (reconstruction by insertions)

Every finite antichain \(Z\) can be recovered from
\(\operatorname{comp}(Z)\) by finitely many operations (19), one coordinate
at a time.

#### Proof

In a fixed coordinate, repeated insertion at the current least level
translates all levels until the desired least level is reached. Then, from
bottom to top, repeated insertion at the next occurring level creates each
required gap between consecutive target levels. The operations do not alter
the other coordinates. Applying this construction in all three coordinates
recovers \(Z\).
\(\square\)

### Lemma 3.2 (exact insertion increment)

Let

\[
H=\{z\in Z:z_i\ge h\},
\qquad b=|H|,
\]

and let \(u,v\) be the maximum values on \(H\) in the other two
coordinates. Then

\[
\Phi_0(I_{i,h}(Z))-\Phi_0(Z)=u+v+3-b.
\tag{20}
\]

#### Proof

The projection deleting coordinate \(i\) does not change. In each projection
containing coordinate \(i\), the order-preserving map which shifts levels at
least \(h\) embeds the old projected lower hull and skips exactly the new row
at level \(h\). The two new row lengths are \(u+1\) and \(v+1\),
respectively. Hence \(P(U(Z))\) increases by \(u+v+2\).

The sum of all coordinates of points in \(Z\) increases by \(b\). The
coordinatewise maximum in direction \(i\) increases by one, while the other
two maxima do not change. Thus \(E(Z)\) increases by \(b-1\). Subtracting
these increments in (4) gives (20).
\(\square\)

For an antichain, projection onto any two coordinates is injective. Therefore

\[
b\le(u+1)(v+1).
\tag{21}
\]

When \(b\le5\), equations (20)--(21) give a positive increment. Indeed, if
\(u+v\ge3\), then \(b\le5\le u+v+2\); if \(u+v\le2\), then
\((u+1)(v+1)\le u+v+2\). In either case

\[
b\le u+v+2.
\tag{22}
\]

The only new issue for six points is a full projected grid.

### Lemma 3.3 (forbidden \(2\times3\) grid)

An antichain of at most six points which passes the completion criterion
cannot contain six points whose projection onto two coordinates is a complete
\(2\times3\) grid.

#### Proof

If such a grid occurs, the antichain has exactly six points. After naming the
two projected coordinates \(x,y\), write its points as

\[
z_{rs}=(x_r,y_s,t_{rs}),
\qquad
r\in\{0,1\},\quad s\in\{0,1,2\},
\]

where \(x_0<x_1\) and \(y_0<y_1<y_2\). Antichain incomparability forces the
third coordinates to decrease strictly along every increasing row and
column.

For \(z_{11}\), the points \(z_{10}\) and \(z_{01}\) are the two witnesses
in (11) showing that the successor in the third direction is forced. For
\(z_{12}\), the witnesses are \(z_{11}\) and \(z_{02}\). Constraint (12)
would therefore require the same full-support corner coordinate to equal
both

\[
t_{11}+1
\qquad\text{and}\qquad
t_{12}+1.
\]

These values are different because \(t_{11}>t_{12}\). The completion
criterion fails, a contradiction.
\(\square\)

### Proposition 3.4 (strict insertion growth)

If \(1\le|Z|\le6\) and \(Z\) passes the completion criterion, then every
insertion satisfies

\[
\Phi_0(I_{i,h}(Z))\ge\Phi_0(Z)+1.
\tag{23}
\]

#### Proof

If \(b\le5\), this is (20) and (22). If \(b=6\) and the increment in (20)
were nonpositive, then

\[
u+v\le3,
\qquad
6\le(u+1)(v+1).
\]

The only possibilities are \((u,v)=(1,2)\) and \((2,1)\). Equality in
(21) then forces the six projected points to fill the corresponding
\(2\times3\) grid, contradicting Lemma 3.3.
\(\square\)

It follows that the negative insertion search terminates. Starting from a
fixed compressed seed of score \(s<0\), every retained path has length at
most \(-s-1\). Each state has at most \(3|Z|\) distinct insertion choices,
and score growth prevents cycles even after symmetry identification.

## 4. Exhausting all lower-ideal extensions

For a fixed expanded antichain \(Z\), begin with \(Q_0=U(Z)\). From a current
finite lower ideal \(Q\), an *admissible addition* is a point
\(x\in\mathbb N^3\setminus Q\) such that:

1. every predecessor \(x-e_i\) with \(x_i>0\) belongs to \(Q\);
2. \(x\) does not dominate any point of \(Z\); and
3. \(\Phi(Q\cup\{x\},Z)<0\).

Adjoin every admissible point in turn, retain every reached state as a
candidate, and continue until no new state appears. Equivalently, it is enough
to test the finite successor frontier
\(\{q+e_i:q\in Q,\ 1\le i\le3\}\setminus Q\), because every admissible
point has a predecessor in \(Q\). No corner-count filter is permitted on
intermediate states: adding a point can remove a corner.

### Proposition 4.1 (extension completeness)

Let \(T\) be a finite lower ideal containing \(U(Z)\), retaining every point
of \(Z\) as maximal, and satisfying \(\Phi(T,Z)<0\). Then the admissible
addition process reaches \(T\).

#### Proof

If a current state \(Q\subsetneq T\), choose a minimal point \(x\) of
\(T\setminus Q\). Since \(U(Z)\subseteq Q\), one has \(x\ne0\). Every
positive-coordinate predecessor of \(x\) belongs to \(T\) by lower closure
and to \(Q\) by the minimal choice of \(x\). Thus \(x\) is on the enumerated
successor frontier.

No point of \(T\) strictly dominates an element of \(Z\), because the latter
are maximal in \(T\). Finally, projection cardinalities are monotone under
inclusion, so

\[
\Phi(Q\cup\{x\},Z)\le\Phi(T,Z)<0.
\]

Thus \(x\) is admissible. Repeating the argument constructs \(T\).
\(\square\)

### Proposition 4.2 (extension termination)

For fixed \(Z\), the admissible addition process reaches only finitely many
states.

#### Proof

Every reached state satisfies

\[
P(Q)<3|Z|+E(Z).
\tag{24}
\]

If \(x\in Q\) has \(x_j=d\), lower closure puts
\(0,e_j,\ldots,de_j\) in \(Q\). Either projection which retains coordinate
\(j\) therefore has at least \(d+1\) points. Equation (24) bounds every
coordinate of every reached point by a constant depending only on \(Z\).
All reached ideals lie in one finite lattice box, so only finitely many states
can occur.
\(\square\)

This proof supplies the finite bound; an implementation must not replace it
with an unexplained coordinate, cardinality, queue-length, or time cutoff.

## 5. The canonical finite family

For a finite point set, sort its points lexicographically. A *canonical
antichain* is the lexicographically least sorted image under the six
simultaneous coordinate permutations. A pair \((Q,Z)\) is canonicalized by
applying the same permutation to both sets and taking the least resulting
ordered pair. Coordinate permutation preserves every quantity and predicate
above.

Define the family \(\mathcal G_{\le6}\) by the following exact procedure.

1. **Compressed seeds.** For each \(1\le k\le6\), enumerate every canonical
   \(k\)-point antichain whose occurring values in each coordinate are exactly
   \(0,1,\ldots,d_i\), with \(d_i<k\). Retain those with \(\Phi_0<0\)
   which pass Theorem 2.2.
2. **Level expansion.** Close the seed family under every insertion (19),
   canonicalizing after each insertion. Retain exactly the states with
   \(\Phi_0<0\). Completion feasibility may be rechecked defensively; Lemma
   2.3 proves that it cannot change.
3. **Ideal extension.** From the lower hull of every expanded antichain,
   enumerate all states reached by the admissible additions of Section 4.
4. **Necessary structural filters.** Retain a pair \((Q,Z)\) only if
   \(e_1,e_2,e_3\in Q\) and \(Q\) has at most one full-support corner. Apply
   this filter only to completed candidate states, not during their extension
   paths.
5. **Pair symmetry.** Retain one canonical representative of every
   simultaneous coordinate-permutation orbit of \((Q,Z)\).

This uniform specification safely applies the completion filter for every
\(k\le6\). A conforming implementation may enumerate a declared superset—for
example, by omitting that filter when \(k\le5\)—provided B3.3 checks every
extra candidate as well.

### Theorem 5.1 (B3.2 shape coverage)

The family \(\mathcal G_{\le6}\) is finite. Let \(T\) be a preferred
four-generator Apéry ideal and let \(Z\) be its final window. If

\[
1\le|Z|\le6
\qquad\text{and}\qquad
\Phi(T,Z)<0,
\tag{25}
\]

then the simultaneous coordinate-permutation orbit of \((T,Z)\) occurs in
\(\mathcal G_{\le6}\).

#### Proof

The set \(Z\) is an antichain, and \(T\) is a completion witnessing that
\(Z\) passes Theorem 2.2. Lemma 2.3 shows that its rank compression passes as
well. Since \(U(Z)\subseteq T\),

\[
\Phi_0(Z)\le\Phi(T,Z)<0.
\tag{26}
\]

Reconstruct \(Z\) from \(\operatorname{comp}(Z)\) by Lemma 3.1. Every
intermediate antichain has the same order type and hence passes the completion
criterion. Proposition 3.4 says that its score strictly increases at each
step. The final score is negative by (26), so the compressed seed and every
intermediate score are negative. Thus the level-expansion stage reaches the
orbit of \(Z\).

Proposition 4.1 then reaches \(T\) from \(U(Z)\). The foundational properties
of a preferred Apéry ideal give all three coordinate units and at most one
full-support corner, so the structural filters retain the pair. Pair
canonicalization retains its orbit.

There are finitely many compressed seeds. Proposition 3.4 makes every
negative expansion tree finite, and Proposition 4.2 makes every extension
tree finite. Therefore \(\mathcal G_{\le6}\) is finite.
\(\square\)

The theorem has no hidden multiplicity, generator, conductor, coordinate, or
cardinality cutoff. Any maximum cardinality observed in a generated family is
an output diagnostic, not a hypothesis.

## 6. Exact generator semantics

If the computation is retained after D3, a generator conforming to this
specification must:

1. represent coordinates, scores, projection sizes, and cardinalities by
   exact integers;
2. cover all six values \(k=1,\ldots,6\), including repeated coordinate
   levels and antichains touching coordinate planes or axes;
3. implement strict \(\Phi<0\), since the equality wall is analytically
   accepted by (5);
4. enumerate all restricted-rank coordinate columns, not merely permutations
   with distinct entries;
5. apply only simultaneous coordinate permutations to a pair \((Q,Z)\);
6. exhaust both the insertion and extension queues without numerical or time
   cutoffs;
7. validate every emitted pair directly: lower closure, antichain and
   maximality conditions, score, coordinate units, corner count, and
   canonical form; and
8. fail closed on malformed state, unsupported ranges, arithmetic overflow,
   incomplete queues, or inconsistent duplicate records.

Counts and stored candidate lists may be used for regression and provenance,
but cannot be acceptance predicates. B3.3 must state the residue-label and
all-cut predicate on the distinct lower ideals underlying the generated
pairs. If D3 retains this computation, R3 must freshly regenerate the whole
family and provide an independent path that checks generation and lifting,
not only the surviving arithmetic certificates.

## 7. Audit of the historical candidate

The frozen archive contains the following candidate implementation:

- [`enumerate_compressed.cpp`](../artifacts/wilf_four_generators_review_package_2026-09-11/round7/six_point_dependency_replay/enumerate_compressed.cpp)
  enumerates compressed six-point antichains and quotients simultaneous
  coordinate permutations;
- [`wilf_six_point.py`](../artifacts/wilf_four_generators_review_package_2026-09-11/round7/six_point_dependency_replay/wilf_six_point.py)
  implements the completion criterion and negative insertion closure;
- [`extend_six_point.py`](../artifacts/wilf_four_generators_review_package_2026-09-11/round7/six_point_dependency_replay/extend_six_point.py),
  using `all_negative_extensions` from
  [`verify_final_window.py`](../artifacts/wilf_four_generators_review_package_2026-09-11/round7/six_point_dependency_replay/verify_final_window.py),
  enumerates lower-ideal extensions and applies the final six-point filters;
  and
- [`run_six_point_verification.py`](../artifacts/wilf_four_generators_review_package_2026-09-11/round7/six_point_dependency_replay/run_six_point_verification.py)
  runs those stages and separately invokes the older \(k\le5\) path.

The source transitions match the mathematical operations above. In
particular, the extension source does not prune intermediate ideals by corner
count, and the six-point enumeration has no imposed multiplicity bound. The
older \(k\le5\) path omits the completion and final corner filters, thereby
enumerating a safe superset rather than risking false rejection.

The stored six-point records report the following diagnostics:

| Stage | Historical count |
|---|---:|
| Compressed antichains up to coordinate permutation | 345,988 |
| Negative compressed antichains | 2,264 |
| Negative seeds passing completion | 891 |
| Negative antichains after insertion | 4,406 |
| Extension pairs before final filters | 11,790 |
| Pairs passing axis and corner filters, before symmetry | 6,019 |
| Canonical \((T,Z)\) pairs | 5,962 |
| Distinct lower ideals \(T\) | 5,331 |
| Largest raw extension / largest retained ideal | 57 / 56 |

The older path reports:

| \(|Z|\) | Compressed | Negative compressed | Negative expanded | Extension pairs |
|---:|---:|---:|---:|---:|
| 1 | 1 | 0 | 0 | 0 |
| 2 | 2 | 0 | 0 | 0 |
| 3 | 18 | 0 | 0 | 0 |
| 4 | 287 | 1 | 2 | 2 |
| 5 | 8,340 | 58 | 131 | 198 |

These totals are useful regression targets only. The archived completion
diagnostic checks bounded examples but imports the producer's criterion, so
it is not an independent general proof or an independent checking path under
V0. The historical runner also uses assertion-driven stage checks and stored
intermediate files. Those issues are for R3 if D3 retains the computation;
they do not affect the analytic coverage theorem proved here.

## 8. Retained interface

B3.2 supplies B3.3 with the following exact statement:

> Every preferred four-generator Apéry ideal with at most six final-window
> points and negative projection score has, up to simultaneous coordinate
> permutation, a pair \((T,Z)\) in the finite family
> \(\mathcal G_{\le6}\).

B3.3 must now specify and prove the finite arithmetic implication for every
distinct ideal underlying that family, including all ordered residue-bijective
labels, every modular cut, every integer lift, and equality. Until B3.3 and
the later D3/R3 gates are complete, no computed six-window lemma is promoted
under V0.
