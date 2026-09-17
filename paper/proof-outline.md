# Reconstruction proof outline and dependency ledger

## Purpose and status

The selected self-contained reader proof is now
[prelim/proof.md](../prelim/proof.md). This document is the detailed
reconstruction ledger; its historical references are not PRELIM dependencies.
Use [the roadmap](../ROADMAP.md) for live status.

This ledger records the selected reconstruction argument and source-specific
dependencies. The standalone proof, including all analytic details and fresh
finite verification, is in PRELIM; this ledger is not a reader dependency.

Every dependency is classified as follows:

- **[A] Analytic:** intended to have a conventional mathematical proof.
- **[C] Computed:** contains an essential finite verification.
- **[E] External:** taken from the published literature.

These labels describe the form of the argument, not its review status. Except
for the external inputs, the present proofs and programs were AI-generated and
must be audited independently.

Every `[C]` item is governed by the
[`verification trust policy`](../verification/trust-policy.md). In particular,
a computed lemma requires a code-independent theorem contract, a mathematical
coverage proof, exact fail-closed checking, a fresh complete replay, and an
independent checking path before release. Counts, timings, random probes,
stored `PASS` records, and manifest checks are diagnostic or provenance
evidence, not substitutes for those obligations. The later V1 task will decide
whether any retained components should additionally be formalized in a proof
assistant.

## 1. Statement and normalization

Let \(S\subseteq\mathbb N\) be a numerical semigroup with multiplicity \(m\),
conductor \(c\), and embedding dimension four. Put

\[
n=|S\cap[0,c)|,\qquad W_4(S)=4n-c.
\]

The proposed theorem is

> **Theorem.** If \(S\) has embedding dimension four, then \(W_4(S)\ge0\).

Write the minimal generators as

\[
S=\langle m,a_1,a_2,a_3\rangle,
\qquad A=\min_i a_i\ge m+1,
\qquad b_i=a_i/A.
\]

For every element of the Apéry set \(\operatorname{Ap}(S,m)\), choose the
lexicographically first factorization using \(a_1,a_2,a_3\). Let
\(T\subseteq\mathbb N^3\) be the resulting exponent set, and set

\[
s=\sum_{x\in T}x,\qquad
M=\max\operatorname{Ap}(S,m)=c+m-1,
\]
\[
H=M/A,\qquad R=\max_{x\in T}|x|_1,
\qquad D_0=3mH-4b\mathbin\cdot s.
\]

In the terminology used in the geometric literature, \(T\) is a
three-dimensional L-shape for the Apéry set. Chomicz gives relation-based
procedures that can produce other L-shapes. The present route retains the
lexicographic choice because it is canonical and interfaces directly with the
initial-ideal results used below.

The proof uses three foundational facts.

### F1. Preferred Apéry ideal [E]+[A]

The set \(T\) is a finite lower ideal of cardinality \(m\), contains
\(0,e_1,e_2,e_3\), and its labels \(a\cdot x\) form a complete set of residues
modulo \(m\).

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
deficit \(D_0\).

This reduction is independent of which L-shape is chosen. Indeed, for every
system of one factorization \(x(w)\) of each Apéry element,

\[
b\mathbin\cdot\sum_w x(w)
=\frac1A\sum_w a\mathbin\cdot x(w)
=\frac1A\sum_{w\in\operatorname{Ap}(S,m)}w.
\]

Thus changing L-shape cannot improve \(D_0\) itself. It can only change the
auxiliary geometry---for example \(R\), the minimal corners, \(U_2\), and \(G\)---
used to certify the same invariant inequality.

The underlying Apéry genus formula is classical. Zhai's weighted inequality
for finite downsets supplies the nonnegative baseline for \(D_0\); the new burden
is the positive surplus needed to dominate \(m(m-1)/A\). The identity and
baseline are proved in the
[foundational note](foundations.md#4-the-moment-identity-and-baseline-f2).
The vector and line-slack refinements used by later branches are proved in the
[coordinate-line note](coordinate-lines.md).

### F3. Minimal-exclusion structure [E]+[A]

If \(p\notin T\) is minimal excluded and \(x\in T\) represents the same
residue, then \(p\) and \(x\) have disjoint supports. Distinct minimal excluded
points sharing a positive coordinate have different residues. Hence:

1. \(T\) has at most one full-support minimal excluded point;
2. if it exists, call it \(p\), and its residue is zero;
3. all other minimal excluded points are visible in coordinate planes.

The proof of these facts is the common arithmetic input to every large-\(m\)
branch. It is given in the
[foundational note](foundations.md#5-minimal-excluded-points-f3).

This support/exclusion structure is substantially present in Proposition 2.6
of Hellus, Rechenauer, and Waldi. The foundational note distinguishes that
cited result from the elementary representative-disjointness corollary.

### F4. Optional published reductions [E]+[A]

Let \(K=\operatorname{Max}(T)\) be the coordinatewise maximal points of the
preferred exponent ideal. A maximal element of the Apéry poset must be labeled
by a point of \(K\): if \(x+e_i\in T\), then its label exceeds the label of
\(x\) by the nonzero semigroup element \(a_i\). Since the maximal Apéry-poset
elements are the pseudo-Frobenius numbers translated by \(m\),

\[
\operatorname{type}(S)\le |K|.
\]

The Fröberg--Gottlieb--Häggkvist inequality settles Wilf's conjecture when the
type is at most \(e-1=3\). It permits a preliminary disposal of
\(|K|\le3\), but the selected branch arguments and checking domains do not
require that disposal or impose a maxima-count skip. The conductor and
left-element theorems likewise permit the assumptions \(c>3m\) and \(n\ge13\)
after disposing of their complements, but neither shortens the present
branch parameters or the B1 computation. These are contextual reductions,
not prerequisites of the retained seven-row proof. The exact source
comparison and the
decision not to use Marashdeh's defect decomposition as a replacement are in
the [published-reduction comparison](../literature/published-reduction-comparison.md).

### G4. Phase and rectangular thickening [A]

Let \(X\) be uniform on \(T\). For normalized positive weights
\(u_i=a_i/M\), put

\[
v=\min_i u_i,\qquad \sigma=\sum_i u_i,
\qquad \kappa=3-4\mathbb E_T(u\cdot X).
\]

Coordinate-line slacks and a one-dimensional sawtooth integral give

\[
\boxed{
\sigma(1-3\kappa)
\le4\kappa+5v-3\kappa v+4v^2.
}
\]

The rectangular thickening of \(T\), rescaled into the unit simplex, has
continuous deficit

\[
\boxed{\kappa_c=\frac{\kappa+\sigma}{1+\sigma}.}
\]

Its excluded upper-orthant vertices have exactly the supports of the discrete
minimal excluded points. The
[`phase-and-thickening note`](phase-and-thickening.md) proves both identities
without residue hypotheses and records every strict endpoint later used to
obtain \(H<24\), \(H<42\), and \(H<78\). The older coarse phase estimate in
the archive is not retained. The
[B4.2 planar refinement](short-corner-compactness.md) improves the B4
cutoff to \(H<36\), while preserving the \(42\)-box as a compatible
certificate superset.

### G5. Central box and three monotone horns [A]

If a finite lower ideal \(U\subseteq\mathbb N^3\) has no full-support
minimal exclusion, a chordal compatibility graph and its clique tree give a
disjoint decomposition

\[
U=\mathcal B(c)\mathbin{\dot\cup}A_1
 \mathbin{\dot\cup}A_2\mathbin{\dot\cup}A_3.
\]

Here \(\mathcal B(c)\) is an anchored central box. Horn \(A_i\) lies beyond
the \(i\)-th face of that box, and its sections perpendicular to coordinate
\(i\) are rectangles whose two transverse caps are nonincreasing. The tree
has at most three leaves; choosing the median of the three coordinate maxima
produces the center and proves the monotonicity.

If \(T\) has one full-support minimal exclusion \(p\), removing that generator
from the complement produces a finite no-full-corner ideal \(U\) with

\[
T=U\setminus(p+\mathbb N^3).
\]

Clipping the central box and each horn slice preserves the disjoint
decomposition. The
[`central-box/three-horn note`](central-box-horns.md) includes a self-contained
proof of the needed clique-tree lemma, attributes the classical chordal-graph
input, and proves the exact nested-cap recurrence used by B2, B4, and B6.

## 2. The complete case partition

After treating \(m\le29\), suppose \(m\ge30\). First split according to whether
the full-support corner \(p\) exists. If it does, split according to its degree
\(|p|_1\), and finally split the residual class according to \(R\).

| Case | Required result | Type | Bound obtained |
|---|---|---:|---:|
| \(m\le19\) | Published bounded-multiplicity results | [E] | \(W_4\ge0\) |
| \(20\le m\le29\) | Negative-case conductor reduction and finite generator search | [A]+[C] | \(W_4\ge0\) |
| \(m\ge30\), no full-support corner | No-corner weighted theorem | [A]+[C] | \(D_0\ge m-1\) |
| \(m\ge30\), \(p=(1,1,1)\) | Three-plane projection theorem | [A] | \(W_4\ge0\) |
| \(m\ge30\), \(p\sim(2,1,1)\) | Short-corner weighted theorem | [A]+[C] | \(D_0\ge m-1\) |
| \(m\ge30\), \(\lvert p\rvert_1\ge5\), \(R\le6\) | Local-or-axis centroid theorem | [A]+[C] | \(D_0\ge m\) |
| \(m\ge30\), \(\lvert p\rvert_1\ge5\), \(R\ge7\) | High-height one-corner theorem | [A]+[C] | \(D_0\ge m-29/10\) |

Here \(p\sim(2,1,1)\) means a coordinate permutation. The partition is
exhaustive: a positive integer triple has degree at least three; the only
degree-three type is \((1,1,1)\), and the only degree-four type is
\((2,1,1)\). In the residual class, \(R\le6\) or \(R\ge7\). Moreover,
\(p-e_i\in T\) gives \(|p|_1\le7\) in the first alternative, while
\(H\ge R\ge7\) in the second.

The complete elementary proof, including mutual exclusivity and the boundary
between routing hypotheses and branch-entry lemmas, is in the
[case-partition note](case-partition.md).

## 3. Branch contracts

This section records exactly what each branch must establish. A publishable
proof must supply the analytic arguments and the completeness proof of each
finite task, not merely cite a successful run.

### B1. Multiplicity at most 29 [E], [A], [C]

Bruns--García-Sánchez--O'Neill--Wilburne, Theorem 4.3, prove Wilf's
inequality for every numerical semigroup of multiplicity at most \(18\).
Kliem--Stump, Proposition 6.9 in the published version, prove it for every
numerical semigroup of multiplicity \(19\). Thus the external input has no
embedding-dimension or subclass restriction and supplies \(W_4\ge0\) for
\(m\le19\). Exact statements, computational dependencies, version numbering,
and bibliographic data are in the
[multiplicity-through-19 source audit](../literature/multiplicity-through-19-audit.md).

For \(20\le m\le29\), the analytic conductor reduction is

\[
W_4<0\quad\Longrightarrow\quad M\le m(m-2).
\tag{2}
\]

Because each nonmultiplicity generator is an Apéry element, any counterexample
must occur among

\[
m<a_1<a_2<a_3\le m(m-2).
\]

The minimal finite obligation is to check every sorted, minimally generated
tuple in this box whose Apéry maximum also satisfies \(M\le m(m-2)\).
The [finite generator-box specification](small-multiplicity-specification.md)
proves that these tuples contain every possible counterexample and gives
exact Apéry-distance and ordinary-membership predicates. Thus the
mathematical obligations are:

1. prove (2), including the full-weighted-ideal subcase;
2. prove that the enumeration covers precisely every possible counterexample;
3. verify the exact Wilf computation for every retained tuple.

Historical source:
`round5/small_multiplicity/exhaustive_m20_m29_theorem.md` in the review
package.

The first two obligations are now fully reconstructed. The
[`full-weighted-ideal note`](full-weighted-ideal.md) classifies the projection
along the least-weight coordinate, excludes the only six-column possibility
by an additive-order argument, and dispatches the remaining three- and
four-column cases with the final-window projection inequality. The
[`conductor-reduction note`](conductor-reduction.md) extracts a low-weight
corner in every non-full ideal and proves from its predecessor lines that
\(M\le D\le m(m-2)\) in a negative case. Neither step uses finite
verification or assumes a multiplicity range. The generator-box note proves
the canonical-tuple, minimality, gcd, endpoint, and negative-case coverage
claims without relying on a historical run. The
[D1 simplification gate](../research/b1-simplification-decision.md) found no
smaller analytic or published replacement and retains this exact finite
obligation. The
[R1a audit](../verification/b1/r1a-residue-distance-audit.md) proves the cyclic
update and records a fresh complete residue-distance replay. The
[R1b audit](../verification/b1/r1b-membership-audit.md) proves the ordinary
membership calculation, records its independent fresh replay, and checks the
common diagnostics only after R1b passes on its own. Both paths find no
negative case, so the finite lemma is complete under V0.

### B2. No full-support corner [A], [C]

The required abstract theorem is:

> If \(T\subseteq\mathbb N^3\) is a finite lower ideal containing the coordinate
> units, has no full-support minimal exclusion, and \(|T|=m\ge30\), then for all
> positive weights \(a\),
> \[
> 3m\max_{x\in T}a\cdot x-4a\cdot\sum_{x\in T}x
> \ge a_{\min}(m-1).
> \]

The analytic entry is now reconstructed in the
[B2.1 compactness note](no-corner-compactness.md). The G5 decomposition and
an explicit boundary-potential argument first prove the continuous
no-corner inequality

\[
\kappa_c\ge\frac13.
\]

Only the finite-step horn geometry arising from rectangular thickening is
needed. Combining this inequality with G4 gives

\[
\frac{D_0}{m}\ge\frac{H-2(1+b+c)}3
\]

and sends every possible failure to

\[
1\le b\le c\le H,\qquad
5\le H<12+\sqrt{137}<24.
\]

The lower endpoint uses the explicit degree-four cardinality bound
\(|T|\le29\). The later certificate may harmlessly cover the larger closed
box ending at \(H=24\). Thus B2.1 contains no computed assertion.

The [B2.2 finite specification](no-corner-interval-specification.md) defines
the allowance-height obligation

\[
m-D_H\le1
\]

for every nonempty no-corner ideal throughout the closed parameter box. It
derives the additive point score, proves the exact nested-rectangle
recurrence, proves simultaneous whole-box domination for every real
parameter, and specifies fail-closed coverage of a closed interval tree.

The [D2 simplification gate](../research/b2-simplification-decision.md) found
exact obstructions to the natural direct reductions and retained the tree.
The [R2 audit and fresh replay](../verification/b2/r2-interval-audit.md) then
checked all 50,885 nodes through two independent paths: both established
closed coverage and recomputed all 24,912 dynamic-programming leaves and 531
analytic leaves. The largest exact numerator is the permitted equality value
\(4096\). Thus B2.2-FV is established under V0; the counts remain regression
evidence rather than acceptance predicates.

Historical source chain:
`round3/horns_optimization/fullcap_boundary_theorem.md`,
`round4/bellman/arbitrary_horn_bridge.md`,
`round4/joint_horns/joint_effective_cap_theorem.md`, and
`round5/weight_arrangement/weighted_no_interior_theorem.md`.

### B3. Corner \(p=(1,1,1)\) [A]

The [B3.1 entry lemma](six-maxima-entry.md) proves that every mixed corner in
a coordinate plane must be represented by the top point of the opposite
coordinate axis. The collision rule therefore permits at most one such
corner per plane. A planar lower ideal with at most one mixed corner has at
most two maximal points; since every point of \(T\) lies in a coordinate
plane, \(T\) has at most six maximal points.

The [D3 three-plane theorem](three-plane-projection.md) uses this stronger
planar geometry, rather than only the six-window cardinality. Put
\(K=\operatorname{Max}(T)\), and use

\[
P(T)=\sum_j|\pi_jT|,
\qquad
E(X)=\sum_{x\in X}|x|_1-\sum_j\max_{x\in X}x_j,
\]
\[
\Phi(T,X)=P(T)-3|X|-E(X).
\]

A direct count of the three plane frontiers proves

\[
\boxed{\Phi(T,K)<0\quad\Longrightarrow\quad |T|\le29.}
\]

Since B3 is routed only when \(m=|T|\ge30\), this gives \(\Phi(T,K)\ge0\).
The actual final window \(Z=\{x\in T:M-a\cdot x<m\}\) is a nonempty subset
of \(K\). Adding points increases \(E\), so
\(\Phi(T,Z)\ge\Phi(T,K)\). The
[G3 projection inequality](final-window-projection.md) therefore gives

\[
mW_4(S)\ge m\Phi(T,Z)+E(Z)\ge0.
\]

This closes B3 analytically, including \(\Phi=0\), without a shape, residue,
cut, or LP computation. The
[D3 decision](../research/b3-simplification-decision.md) removes R3 from the
required replay queue. B3.2 and B3.3 remain specifications of the broader
six-window alternative, not dependencies of this proof. The replacement
does not prove that broader theorem at arbitrary multiplicity.

### B4. Corner \(p\sim(2,1,1)\) [A], [C]

The required theorem is

\[
D_0\ge m-1\qquad(m\ge30).
\]

B4.1 is complete in the [short-corner height-split note](short-corner-height-split.md).
The sharp analytic bound

\[
m\le2R^2-R+3
\]

gives \(m\ge49\Rightarrow H\ge6\). The \(H<6\) side is confined to
\(30\le m\le48\), with \(R=4\) or \(5\); for \(m\ge32\), necessarily
\(R=5\) and \(5\le H<6\). The endpoint \(H=6\) belongs to the high-height
side. Degree at most five alone does not imply low height.

B4.2 is complete in the
[short-corner compactness note](short-corner-compactness.md). Its simple
planar mean bound is

\[
\frac{D_0}{m}\ge\frac{H-4B}{3},\qquad B=\sum_i b_i.
\]

Two planar partitions improve this to
\(D_0/m\ge H/3-16B/15-2/5\). Together with G4, any target failure on the
\(H\ge6\) side must satisfy

\[
B<9+\frac{28}{H-3},\qquad
5H^2-180H+47<0,\qquad H<36.
\]

The closed domain \(1\le b\le c\le H,\ 6\le H\le36\), after sorting weights
into \((1,b,c)\), contains all possible high-height failures. All three
positions of the doubled corner coordinate remain necessary.
The larger historical \(42\)-box is still a compatible superset.

B4.3 is complete in the
[low-height profile specification](short-corner-profile-specification.md).
The residue forcing argument allows at most two mixed corners in each
plane, and at most one with \(x\ge2\) in each of \(xy,xz\) after orienting
\(p=(2,1,1)\). Three compatible six-entry profiles reconstruct the ideal
by removing the \(p\)-orthant. A final degree test needs at most four row
inequalities; plane degree bounds alone would not suffice.
The coverage proof keeps every eligible oriented key, without sorting
weights or skipping shapes with few maxima.

B4.4 is complete in the
[centroid-certificate note](short-corner-centroid-certificates.md).
A sparse nonnegative rational point combination is sufficient when

\[
\sum_xy_x=3m,\qquad
\beta_i:=\sum_xy_x\,x_i-4s_i\ge0,\qquad
\sum_i\beta_i\ge m-1.
\]

The identity

\[
3mQ-4w\cdot s=\sum_xy_x(Q-w\cdot x)+
\sum_i\beta_i(w_i-1)+\sum_i\beta_i
\]

proves the target for all real \(w_i\ge1\) and height allowances
\(Q\ge\max_{x\in T}w\cdot x\).
Denominator clearing gives an integer predicate, and any valid witness can
be replaced by one on at most three maximal points.

[D4](../research/b4-simplification-decision.md) is complete with a partial
computational simplification:

- For \(H\ge6\), the [interval specification](short-corner-interval-specification.md)
  and [R4a audit and replay](../verification/b4/r4a-high-height-audit.md)
  establish B4-high-FV under V0 through two fresh complete checking paths.
  Together with B4.2, this proves the target throughout this subcase.
  B4.2 also proves analytic acceptance rules
  \(H\ge3+4B\) and \(5H\ge21+16B\), both implying \(D_0\ge m\) and including
  equality.
- For \(H<6\), the B4-low-FV contract quantifies over every generated
  eligible key and all real weights \(w_i\ge1\), including arbitrary
  height allowances. D4 selects the
  [deterministic local route](short-corner-local-certificates.md):
  check \(U_2(T)\ge m-1\) on every B4.3 profile, with two inline exceptional
  three-point witnesses. G2 proves the local construction's soundness;
  B4.4 proves the exceptional witnesses' all-real-weight soundness.
  An enumeration-wide research diagnostic passes 28,497 keys locally
  and handles exactly two exceptions. [R4b](../verification/b4/r4b-local-profile-audit.md)
  now supplies two fresh independent complete paths and establishes
  B4-low-local-FV and hence B4-low-FV under V0.

The legacy 28,499-record dual list and its loader are no longer selected
proof inputs. R4a and R4b are complete; both height subcases establish
the target under V0. B4 is internally closed, without external review.

Historical source:
`round5/one_corner_extension/short_corner_weighted_theorem.md` and its cited
low-height theorem.

### B5. Residual degree at most six [A], [C]

B5 is internally complete under V0, without external review.
The [degree-six note](residual-degree-six.md) proves the necessary
per-plane mixed-corner bound and two-direction surface injection,
the axis-witness soundness (including its remaining-mass sign condition),
and exact profile coverage. G2 and the generic two-step construction give
the local witness without another proof.

For line lengths and tops, define
\[
U_2(T)=\sum_\ell L_\ell
\max\{\,|v|_1:v\ge0,\ |v|_1\le2,\ t_\ell+v\in T\,\}.
\]
With \(q_i=\max_Tx_i>0\), \(q_*=\max_iq_i\), define
\[
G(T)=q_*\left(3m-4\sum_i\frac{s_i}{q_i}\right).
\]
The two proved soundness bounds give \(D_0\ge\max(U_2,G)\).
When the remaining axis mass is negative, \(G<0\) and the
nonnegative deficit baseline supplies that bound; no negative-mass
centroid is claimed.

B5-FV states \(\max(U_2,G)\ge m\) on the exhaustively specified
degree-six family with \(m\ge30\), \(5\le|p|_1\le7\), the necessary
per-plane corner bounds, and the three surface intersections.
[R5](../verification/b5/r5-degree-six-audit.md) independently regenerates
all 5,574,644 eligible triples twice and checks this predicate.
The local formula handles all but 431, all of which pass the axis
formula. No saved fallback list, residue search, LP, or dual data is used.
[D5](../research/b5-simplification-decision.md) records the route choice;
the focused Chomicz/residue probe remains research context, not a premise.
Thus \(D_0\ge m\) for every genuine B5 ideal.

### B6. Residual degree at least seven [A], [C]

The [selected B6 proof and finite contracts](residual-high-height.md) and
[D6 decision](../research/b6-simplification-decision.md) are complete.
[R6a](../verification/b6/r6a-strip-audit.md) establishes the strip and its
continuous consequence internally. [R6b](../verification/b6/r6b-high-height-audit.md)
establishes the high-height predicate with two complete fresh paths;
B6 is internally closed.

Since \(H\ge R\), this branch has \(H\ge7\). The required abstract theorem is:

> If \(T\subseteq\mathbb N^3\) is a finite lower ideal with exactly one
> full-support corner \(p\), \(|p|_1\ge5\), and normalized positive weights,
> then
> \[
> H\ge7\quad\Longrightarrow\quad D_0\ge m-\frac{29}{10}.
> \]

No residue or exposed-surface restriction is used by this abstract theorem.
The G5 [structural note](central-box-horns.md) proves clipped-horn coverage.
B6.1 specifies its complete finite allowances and scores.
The selected route has two computational layers:

1. a finite strip used to prove the continuous gap \(5/42\):
   R6a checked 1,029 configurations, while the standalone packet needs only
   715 after omitting the allowance arising only at the null zero translation;
2. a closed real-parameter interval certificate with 47,088 accepted leaves.

B6.2 proves that the finite-strip predicate implies the continuous
gap, and B6.3 proves that this gap and G4 confine any target failure to
\(1\le b\le c\le H,\ 7\le H<78\). These are conditional analytic
implications whose strip premise is now established by R6a.
B6.4 specifies and justifies the interval predicate;
R6b checks its full compact region. Historical success records
and configuration counts do not establish either finite premise.

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
| L1 | Published multiplicity \(\le19\) theorem | [E] | Audited in `literature/multiplicity-through-19-audit.md` |
| B1.1--B1.2 | Negative-case conductor reduction | [A] | Reconstructed in `full-weighted-ideal.md` and `conductor-reduction.md`; obtain independent review |
| B1.3 | Multiplicities \(20\)–\(29\) | [C] | Specification, D1, R1a, and independent R1b complete |
| B2 | No-corner weighted theorem | [A]+[C] | B2.1, B2.2, D2, and both R2 paths complete under V0; obtain independent analytic review |
| B3 | Three-plane projection theorem | [A] | B3.1 and D3 complete analytically; no R3 needed; obtain independent review |
| B4 | Short-corner theorem | [A]+[C] | Both height subcases complete under V0 through R4a and R4b; no legacy dual list |
| B5 | Local-or-axis theorem | [A]+[C] | Analytic soundness and profile coverage, D5, and independent complete R5 replay established under V0 |
| B6a | Uniform continuous gap | [A]+[C] | B6.1--B6.2, D6, and R6a complete internally; gap \(5/42\) established |
| B6b | High-height interval theorem | [A]+[C] | B6.3--B6.4, D6, and independent full R6b replay complete internally |
| PART | Case exhaustion | [A] | Reconstructed in `case-partition.md`; obtain independent review |
| G1 | Final arithmetic | [A] | Reconstructed in `final-arithmetic.md`; obtain independent review |
| G2 | Coordinate-line calculus | [A] | Reconstructed in `coordinate-lines.md`; obtain independent review |
| G3 | Final-window projection inequality | [A] | Reconstructed in `final-window-projection.md`; obtain independent review |
| G4 | Phase and rectangular thickening | [A] | Reconstructed in `phase-and-thickening.md`; obtain independent review |
| G5 | Central box, three horns, and clipping | [A] | Reconstructed in `central-box-horns.md`; obtain independent review |

## 6. Material excluded from the main proof

The following material is useful but is not part of the shortest retained
four-generator proof:

- the universal parameter-envelope alternative;
- the broader six-window shape, residue-label, and modular-cut route,
  superseded for B3 by D3's analytic theorem;
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
