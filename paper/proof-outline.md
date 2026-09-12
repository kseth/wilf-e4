# Proof outline and dependency ledger

## Purpose and status

This document extracts the shortest presently claimed proof of Wilf's
inequality for embedding dimension four from the historical archive. It is a
map for reconstruction, not yet a self-contained proof.

Every dependency is classified as follows:

- **[A] Analytic:** intended to have a conventional mathematical proof.
- **[C] Computed:** contains an essential finite verification.
- **[E] External:** taken from the published literature.

These labels describe the form of the argument, not its review status. Except
for the external inputs, the present proofs and programs were AI-generated and
must be audited independently.

## 1. Statement and normalization

Let (S\subseteq\mathbb N) be a numerical semigroup with multiplicity (m),
conductor (c), and embedding dimension four. Put

\[
n=|S\cap[0,c)|,\qquad W_4(S)=4n-c.
\]

The proposed theorem is

> **Theorem.** If (S) has embedding dimension four, then (W_4(S)\ge0).

Write the minimal generators as

\[
S=\langle m,a_1,a_2,a_3\rangle,
\qquad A=\min_i a_i\ge m+1,
\qquad b_i=a_i/A.
\]

For every element of the Apéry set \(\operatorname{Ap}(S,m)\), choose the
lexicographically first factorization using (a_1,a_2,a_3). Let
(T\subseteq\mathbb N^3) be the resulting exponent set, and set

\[
s=\sum_{x\in T}x,\qquad
M=\max\operatorname{Ap}(S,m)=c+m-1,
\]
\[
H=M/A,\qquad R=\max_{x\in T}|x|_1,
\qquad D_0=3mH-4b\mathbin\cdot s.
\]

In the terminology used in the geometric literature, (T) is a
three-dimensional L-shape for the Apéry set. Chomicz gives relation-based
procedures that can produce other L-shapes. The present route retains the
lexicographic choice because it is canonical and interfaces directly with the
initial-ideal results used below.

The proof uses three foundational facts.

### F1. Preferred Apéry ideal [E]+[A]

The set (T) is a finite lower ideal of cardinality (m), contains
(0,e_1,e_2,e_3), and its labels (a\cdot x) form a complete set of residues
modulo (m).

The preferred-factorization/downset construction is due to Zhai and was
developed as an initial-monomial-ideal construction by Hellus, Rechenauer, and
Waldi. The foundational note gives a self-contained translation with exact
attribution. See the
[foundational note](foundations.md#3-preferred-exponent-representatives-f1)
and the
[literature survey](../literature/survey.md#41-apéry-sets-and-preferred-factorizations).
Chomicz's L-shape constructions give the same lower-ideal and residue-
representative interface, but do not presently shorten these inputs.

### F2. Moment identity [A]

The Apéry genus formula gives

\[
\boxed{mW_4(S)=A D_0-m(m-1).}
\tag{1}
\]

Consequently the problem is reduced to a lower bound for the weighted moment
deficit (D_0).

This reduction is independent of which L-shape is chosen. Indeed, for every
system of one factorization (x(w)) of each Apéry element,

\[
b\mathbin\cdot\sum_w x(w)
=\frac1A\sum_w a\mathbin\cdot x(w)
=\frac1A\sum_{w\in\operatorname{Ap}(S,m)}w.
\]

Thus changing L-shape cannot improve (D_0) itself. It can only change the
auxiliary geometry---for example (R), the minimal corners, (U_2), and (G)---
used to certify the same invariant inequality.

The underlying Apéry genus formula is classical. Zhai's weighted inequality
for finite downsets supplies the nonnegative baseline for (D_0); the new burden
is the positive surplus needed to dominate (m(m-1)/A). The identity and
baseline are proved in the
[foundational note](foundations.md#4-the-moment-identity-and-baseline-f2).

### F3. Minimal-exclusion structure [E]+[A]

If (p\notin T) is minimal excluded and (x\in T) represents the same
residue, then (p) and (x) have disjoint supports. Distinct minimal excluded
points sharing a positive coordinate have different residues. Hence:

1. (T) has at most one full-support minimal excluded point;
2. if it exists, call it (p), and its residue is zero;
3. all other minimal excluded points are visible in coordinate planes.

The proof of these facts is the common arithmetic input to every large-(m)
branch. It is given in the
[foundational note](foundations.md#5-minimal-excluded-points-f3).

This support/exclusion structure is substantially present in Proposition 2.6
of Hellus, Rechenauer, and Waldi. The foundational note distinguishes that
cited result from the elementary representative-disjointness corollary.

## 2. The complete case partition

After treating (m\le29), suppose (m\ge30). First split according to whether
the full-support corner (p) exists. If it does, split according to its degree
(|p|_1), and finally split the residual class according to (R).

| Case | Required result | Type | Bound obtained |
|---|---|---:|---:|
| (m\le19) | Published bounded-multiplicity results | [E] | (W_4\ge0) |
| (20\le m\le29) | Negative-case conductor reduction and finite generator search | [A]+[C] | (W_4\ge0) |
| (m\ge30), no full-support corner | No-corner weighted theorem | [A]+[C] | (D_0\ge m-1) |
| (m\ge30), (p=(1,1,1)) | Six-final-window theorem | [A]+[C] | (W_4\ge0) |
| (m\ge30), (p\sim(2,1,1)) | Short-corner weighted theorem | [A]+[C] | (D_0\ge m-1) |
| (m\ge30), (|p|_1\ge5), (R\le6) | Local-or-axis centroid theorem | [A]+[C] | (D_0\ge m) |
| (m\ge30), (|p|_1\ge5), (R\ge7) | High-height one-corner theorem | [A]+[C] | (D_0\ge m-29/10) |

Here (p\sim(2,1,1)) means a coordinate permutation. The partition is
exhaustive: a positive integer triple has degree at least three; the only
degree-three type is ((1,1,1)), and the only degree-four type is
((2,1,1)). In the residual class, (R\le6) or (R\ge7). Moreover,
(p-e_i\in T) gives (|p|_1\le7) in the first alternative, while
(H\ge R\ge7) in the second.

The complete elementary proof, including mutual exclusivity and the boundary
between routing hypotheses and branch-entry lemmas, is in the
[case-partition note](case-partition.md).

## 3. Branch contracts

This section records exactly what each branch must establish. A publishable
proof must supply the analytic arguments and the completeness proof of each
finite task, not merely cite a successful run.

### B1. Multiplicity at most 29 [E], [A], [C]

Published work supplies (W_4\ge0) for (m\le19). For (20\le m\le29), the
analytic conductor reduction is

\[
W_4<0\quad\Longrightarrow\quad M\le m(m-2).
\tag{2}
\]

Because each nonmultiplicity generator is an Apéry element, any counterexample
must occur among

\[
m<a_1<a_2<a_3\le m(m-2).
\]

The retained computation exhausts this finite box using two distinct exact
algorithms. Thus the mathematical obligations are:

1. prove (2), including the full-weighted-ideal subcase;
2. prove that the enumeration covers precisely every possible counterexample;
3. verify the exact Wilf computation for every retained tuple.

Historical source:
`round5/small_multiplicity/exhaustive_m20_m29_theorem.md` in the review
package.

### B2. No full-support corner [A], [C]

The required abstract theorem is:

> If (T\subseteq\mathbb N^3) is a finite lower ideal containing the coordinate
> units, has no full-support minimal exclusion, and (|T|=m\ge30), then for all
> positive weights (a),
> \[
> 3m\max_{x\in T}a\cdot x-4a\cdot\sum_{x\in T}x
> \ge a_{\min}(m-1).
> \]

The current proof has an analytic reduction to
(1\le b\le c\le H), (5\le H\le24), followed by an exact interval tree.
The leaf bound uses a structural decomposition of a no-corner ideal into a
central box and at most three nested rectangular horns.

The retained finite task consists of 24,912 dynamic-programming leaves and 531
analytic leaves. The priority is to simplify the structural and compactness
arguments before preserving the interval certificate as essential.

Historical source:
`round5/weight_arrangement/weighted_no_interior_theorem.md`.

### B3. Corner (p=(1,1,1)) [A], [C]

Residue injectivity implies that each coordinate plane has at most one mixed
excluded corner. Since every point of (T) lies in a coordinate plane, (T)
has at most six maximal points.

Let

\[
Z=\{x\in T:M-a\cdot x<m\}.
\]

Every point of (Z) is maximal, so (|Z|\le6). The required finite theorem is:

> If a preferred four-generator Apéry ideal has at most six elements in its
> final Apéry window (Z), then (W_4\ge0).

The current proof compresses all possible antichains (Z), proves that every
negative completion can be reached by finitely many insertions and extensions,
checks every residue-bijective labeling, and checks all modular cuts. The
recorded arithmetic core has 930 ordered residue labelings and 23,002 cuts;
the complete generator also covers (|Z|\le5).

Historical source: `round8/audit_sixpoint.md` together with
`round7/six_point_dependency_replay/`.

### B4. Corner (p\sim(2,1,1)) [A], [C]

The required theorem is

\[
D_0\ge m-1\qquad(m\ge30).
\]

The current proof splits by normalized height.

- For (H\ge6), a planar mean bound and the phase inequality reduce every
  possible failure to a compact real parameter box; an interval certificate
  covers it.
- For (H<6), the degree is at most five. Necessary residue restrictions leave
  28,499 shapes of cardinality at least 30, each handled by an exact rational
  centroid dual.

The cardinality observation (m\ge49\Rightarrow H\ge6) is analytic, so the
low-height computation is relevant only for (30\le m\le48).

Historical source:
`round5/one_corner_extension/short_corner_weighted_theorem.md` and its cited
low-height theorem.

### B5. Residual degree at most six [A], [C]

For each coordinate line \(\ell\) of (T), let (L_\ell) be its length and
(t_\ell) its top. The elementary identities

\[
\sum_\ell L_\ell=3m,
\qquad
\sum_\ell L_\ell t_\ell=4s
\tag{3}
\]

lead to two explicit centroid witnesses.

For the local witness, define

\[
U_2(T)=\sum_\ell L_\ell
\max\{\,|v|_1: v\ge0,\ |v|_1\le2,\ t_\ell+v\in T\,\}.
\]

For the axis witness, with (q_i=\max_Tx_i) and (q_*=\max_iq_i), define

\[
G(T)=q_*\left(3m-4\sum_i\frac{s_i}{q_i}\right).
\]

Both formulas analytically give a point (z\in\operatorname{conv}(T)) whose
residual (3mz-4s) is coordinatewise nonnegative and has total surplus
(U_2(T)) or (G(T)). The only computed assertion is

\[
\boxed{\max\{U_2(T),G(T)\}\ge m.}
\tag{4}
\]

Its domain consists of lower ideals in the degree-six simplex with (m\ge30),
one full-support corner (5\le|p|_1\le7), and two necessary arithmetic
restrictions:

1. each coordinate plane has at most (|p|_1-2) mixed corners;
2. (|F_i\cap F_j|\le2n_k) for the exposed surfaces.

The exact enumeration checks 5,574,644 shapes. The local witness handles all
but 431, and the axis witness handles those 431. Finding a structural proof of
(4), perhaps by classifying the fallback shapes, is the highest-priority
opportunity to remove a large enumeration.

A focused residue audit found that none of the 431 fallback shapes satisfies
the necessary residue conditions for an Apéry L-shape. Of these, 199 are
already excluded by nonzero, pairwise-distinct generator residues, the
full-corner relation, and injectivity on the three axes; each of the remaining
232 is excluded by one mixed minimal corner together with the opposite-axis
support condition from F3. This suggests the sharper structural target

\[
\text{genuine Apéry L-shape in this branch}\quad\Longrightarrow\quad U_2(T)\ge m.
\tag{5}
\]

We do not replace (4) by a modular search: that would exchange a short
analytic witness for another computation rather than reduce verification.
The present strategy keeps (G) and treats (5) as a candidate analytic lemma.
See the [Chomicz assessment](../research/chomicz-assessment.md).

Historical source: `round10/local_centroid/local_centroid_theorem.md`.

### B6. Residual degree at least seven [A], [C]

Since (H\ge R\), this branch has (H\ge7). The required abstract theorem is:

> If (T\subseteq\mathbb N^3) is a finite lower ideal with exactly one
> full-support corner (p), (|p|_1\ge5), and normalized positive weights,
> then
> \[
> H\ge7\quad\Longrightarrow\quad D_0\ge m-\frac{29}{10}.
> \]

No residue or exposed-surface restriction is used by this abstract theorem.
Its current proof has two computational layers:

1. a 1,029-case finite strip used to prove the continuous gap (5/42);
2. a closed real-parameter interval certificate with 47,088 accepted leaves.

The phase inequality and continuous gap reduce any failure to
(1\le b\le c\le H), (7\le H<78); the interval certificate treats this
compact region.

Historical sources: `round7/uniform_gap_theorem.md` and
`round7/geometric_residual.md`.

## 4. Final arithmetic [A]

The [final-arithmetic note](final-arithmetic.md) proves, directly from (1),

\[
\begin{array}{rcl}
D_0\ge m-1 &\Longrightarrow& W_4\ge1,\\
D_0\ge m   &\Longrightarrow& W_4\ge A-m+1\ge2,\\
m\ge30,\quad D_0\ge m-\dfrac{29}{10}
&\Longrightarrow& W_4\ge0.
\end{array}
\]

The last implication uses negative integrality. Its worst endpoint is
\(m=30\), where

\[
\frac{90}{31}-\frac{29}{10}=\frac1{310}>0.
\]

The note also checks the seven rows of the case partition, conditionally on
their branch theorems.

## 5. Dependency ledger

The following is the minimal presently retained proof interface.

| ID | Dependency | Form | Main simplification target |
|---|---|---|---|
| F1–F3 | Apéry ideal, moment identity, exclusion structure | [E]+[A] | Reconstructed in `foundations.md`; obtain independent review |
| B1a | Published multiplicity (\le19) theorem | [E] | Verify statement and bibliography |
| B1b | Negative-case conductor reduction | [A] | Isolate from historical global reduction |
| B1c | Multiplicities (20\)–(29) | [C] | Retain two small exact kernels or find a literature replacement |
| B2 | No-corner weighted theorem | [A]+[C] | Seek an analytic horn inequality |
| B3 | Six-final-window theorem | [A]+[C] | Shrink the shape/completion argument and certificate interface |
| B4 | Short-corner theorem | [A]+[C] | Classify the low-height duals symbolically |
| B5 | Local-or-axis theorem | [A]+[C] | Prove (5) from Apéry relation compatibility, or prove (4) structurally |
| B6a | Uniform continuous gap | [A]+[C] | Replace the four-strip computation if possible |
| B6b | High-height interval theorem | [A]+[C] | Derive a direct weighted inequality or smaller certificate |
| PART | Case exhaustion | [A] | Reconstructed in `case-partition.md`; obtain independent review |
| G1 | Final arithmetic | [A] | Reconstructed in `final-arithmetic.md`; obtain independent review |

## 6. Material excluded from the main proof

The following material is useful but is not part of the shortest retained
four-generator proof:

- the universal parameter-envelope alternative;
- older per-shape LP registries and erosion filters;
- the alternative short-corner generator enumeration;
- higher-dimensional extensions and obstructions;
- proposed fixed-dimension finite reductions;
- exploratory scans, failed criteria, and historical weaker constants.

These belong in a companion note or preserved archive. At most one motivating
example from them should appear in the main paper.

## 7. Reconstruction order

The atomic tasks, dependencies, simplification gates, and pre-manuscript exit
criteria are maintained in [`ROADMAP.md`](../ROADMAP.md). This outline records
the mathematical spine; the roadmap is the execution plan.

## Source convention

All historical paths above are relative to
`artifacts/wilf_four_generators_review_package_2026-09-11/`. The historical
archive is intentionally not copied into the new paper tree.
