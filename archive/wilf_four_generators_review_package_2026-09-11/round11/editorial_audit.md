# Editorial and mathematical scope audit for the final presentation

11 September 2026. This audit concerns the final presentation of the current
centroid simplifications and their place in the proposed four-generator proof.
It is an in-session audit, not external mathematical review. No new global
theorem or full certificate replay is claimed by this audit.

## 1. Recommended primary route

Use the **local two-step or axis-endpoint construction** as the primary
low-degree lemma. Its proof has three inspectable components:

1. An elementary coordinate-line identity.
2. Two explicit convex combinations and their exact residuals.
3. A finite statement that at least one residual is large enough.

The resulting inequality is stronger than the original one, removes two
finite-enumeration hypotheses, requires no stored pointwise LP certificates,
and gives the short deduction

\[
W_4\ge A-m+1\ge2
\]

for the genuine semigroups in this residual class. **This strict inequality is
not a statement about all four-generated semigroups.** Other branches of the
proposed global proof establish nonnegativity and include equality cases.

The residual split should be stated by **integer total degree**: degree at
most six uses the new centroid theorem, while degree at least seven forces
normalized height at least seven and invokes the existing high-height theorem.
The nonresidual multiplicity and corner classes remain separate dependencies.

Put the universal indicator envelope in an alternative-route appendix. It
reduces the number of finite cases and avoids enumerating individual ideals,
but its model and proof dependencies are more substantial than those of the
explicit local witness. It is an alternative to the centroid branch, not an
additional hypothesis or compulsory verification gate for the local route.

## 2. Mathematical checks of the two explicit constructions

For a finite lower ideal \(T\subset\mathbb N^3\), write \(m=|T|\) and
\(s=\sum_Tx\). Counting all coordinate lines gives

\[
\sum_\ell L_\ell=3m,
\qquad \sum_\ell L_\ell t_\ell=4s.
\]

In coordinate \(j\), lines parallel to \(j\) contribute \(2s_j\), and
the other two directions contribute \(s_j\) each. These identities are valid
without any Apéry or degree assumption.

For each line top choose an included point at maximal monotone distance at
most two, and denote that distance by \(h_2(t_\ell)\). Then

\[
z_L=\frac1{3m}\sum_\ell L_\ell u_\ell,
\qquad
3mz_L-4s=\sum_\ell L_\ell(u_\ell-t_\ell)\ge0.
\]

The total residual is exactly \(U_2=\sum_\ell L_\ell h_2(t_\ell)\).
There is no LP or hidden optimization over weights in this construction.

For positive axis endpoints \(q_i=\max_Tx_i\), put

\[
G=q_*\left(3m-4\sum_i\frac{s_i}{q_i}\right),\quad q_*=\max_iq_i.
\]

When \(G\ge m>0\), the axis masses \(4s_i/(3mq_i)\) are nonnegative
and sum to less than one. Allocating the remaining mass to a longest-axis
endpoint gives residual \(Ge_j\). Thus the asserted axis construction is
valid. Division by an axis endpoint is safe in the residual class: the full
corner and its mandatory predecessors give positive extent in every axis.

For either construction, a nonnegative residual of total at least \(m\)
proves

\[
3m\max_T b\cdot x-4b\cdot s\ge m\quad(b_i\ge1).
\]

This establishes a statement for arbitrary normalized real weights, with no
height restriction. The remaining computational theorem is precisely
\(\max\{U_2,G\}\ge m\) for the specified finite class.

## 3. Exact finite scope and count distinctions

The theorem's full hypotheses must remain visible:

- \(T\) is a finite coordinatewise lower ideal in three coordinates.
- \(T\subset\Delta_6\), \(m\ge30\).
- There is exactly one full-support minimal excluded point \(p\), with
  \(5\le|p|_1\le7\).
- Each coordinate-plane projection has at most \(|p|_1-2\) mixed minimal
  exclusions.
- The pairwise exposed-surface inequalities
  \(|F_i\cap F_j|\le2(1+\max_Tx_k)\) hold.

The local constructions themselves are universally valid. The assertion that
one reaches the target has been checked only under these hypotheses.

| Quantity | Correct interpretation |
|---|---|
| 5,574,644 | Accepted ideal/profile cases after sorting the full corner; not numerical semigroups and not the number of all permutation orbits |
| 5,574,213 | Cases where the local two-step construction succeeds |
| 431 | Cases where the local construction fails and the axis construction supplies the required fallback |
| 3,011,728 | Cases where the axis construction succeeds, including overlap with the local construction |
| 3,742,041 | Earlier, smaller residual class with two additional filters; historical, not the final local theorem's class |
| 44,281 | Parameter cells for the separate universal indicator route, not ideal shapes |
| 40,115 and 4,166 | Moment certificates and exact cardinality exclusions within those parameter cells |

The 431 fallback count is not the count of all successful axis witnesses.
The shape count increased because the hypotheses weakened. Do not advertise
the change as reducing the number of shapes or as replacing the entire global
proof with 431 cases.

The final local record has 85,392,579 compatible planar-profile triples,
26,252,336 passing the degree cutoff, 26,153,719 passing \(m\ge30\), and
5,574,644 passing the surface restrictions. These are stages of one coverage
calculation, not additional independent theorem classes.

## 4. Coverage and implementation review

The independent source `round10/local_centroid/independent_two_step.cpp`
generates all partitions in the planar degree-six simplex by a distinct
seven-subset construction, obtaining 1,429 nonempty profiles. It retains the
stated total mixed-corner bound, matches the three axis extents, intersects the
three plane cylinders, and removes the upper orthant of \(p\).

The geometric coverage justification should be stated in prose: every minimal
exclusion other than \(p\) has support at most two and is therefore detected
by a coordinate-plane projection. Conversely, any point outside a finite lower
ideal dominates a minimal exclusion. This proves that the plane intersections
minus the orthant reconstruct every ideal in the theorem's class. The mandatory
plane projections of \(p\) ensure that \(p\) is actually a minimal exclusion.

The implementation directly computes all three exposed-surface counts. It
tests all six two-step moves; lower closure guarantees a one-step predecessor
whenever a two-step move is possible. It checks both line identities on every
accepted shape. The axis expression is cleared by the positive denominator
\(q_1q_2q_3\). The degree bound keeps all array accesses and integer
arithmetic within their stated ranges.

For this editorial audit I checked the four manifest hashes, the nine saved
coverage records, each multiplicity histogram total, the aggregate counts,
and the nonnegative recorded minimum residuals. These checks passed. **They
were record and source checks, not a fresh full enumeration.** The archived
portable replay record reports the earlier fresh complete enumeration, all
431 Python-Fraction fallback reconstructions, and elapsed time 25.379318
seconds in the session environment. This timing is not a general performance
guarantee.

## 5. Universal envelope: valid alternative with distinct dependencies

I reviewed the epigraph vertex argument, the finite normal-direction bound,
the indicator-row interpretations, the exact dual box bound, and the return
to a centroid witness by LP duality. No gap was identified in that argument.

The following qualifications matter:

1. This route retains erosion and the refined dominating-plane-corner
   restriction. Their removal from the local theorem does not remove them
   from this relaxation.
2. The 44,281-cell verification treats vertices below height seven. The
   separately established high-height theorem handles other vertices.
3. The resulting all-weight conclusion is \(D_0\ge m-29/10\), not the
   local theorem's stronger \(D_0\ge m\).
4. The observed negative maximum normalized score for the checked cells must
   not be extended to every weight or height; that would ignore the other
   vertices and the high-height dependency.
5. The relaxed score is a fixed-height expression. It agrees with the true
   support-height deficit at the selected epigraph vertex; that equality
   should not be asserted for every arbitrary fractional indicator vector.
6. Fractional solutions need not represent Apéry ideals. Only the inclusion
   of each genuine ideal's zero-one indicators is needed for the upper bound.
7. SciPy proposes rational multipliers; exact integer arithmetic verifies
   them. The independent verifier imports neither SciPy nor the producer.

The saved replay reports 49.75016260147095 seconds. It is appropriate to say
"about 50 seconds in the recorded environment," if runtime is useful at all.
Avoid claiming this smaller number of cases proves the full Wilf theorem by
itself or makes all high-height computations unnecessary.

## 6. Essential global dependencies and presentation status

The current supplement does not replace the proofs for small multiplicities,
no full-support corner, the exceptional corners \((1,1,1)\) and permutations
of \((2,1,1)\), or the high-height branch. In particular, the six-final-window
theorem remains relevant to its separate exceptional-corner branch even though
the residual centroid proof no longer requires its old six-maximal-point split.

Use one definition of a **preferred Apéry ideal** and give the residue
injectivity/lower-closure reason before invoking any arithmetic restriction.
An arbitrary set of factorizations must not be silently substituted for this
preferred lower ideal. Use embedding dimension \(e\) for the number of
minimal generators and exponent dimension \(d=e-1\) consistently.

Recommended status wording:

> We present a proposed computer-assisted proof of Wilf's inequality for
> embedding dimension four. The manuscript gives the analytic reductions,
> finite mathematical obligations, and reproducible exact verifiers. The
> recorded complete checks passed, and the in-session audits identified no
> gap. External mathematical review and proof-assistant formalization remain
> outstanding.

The theorem may then be stated cleanly as the claim proved by the manuscript.
Do not describe it as an accepted resolution, externally certified, formally
verified, or established in the published literature. Separate implementations
written in this session are useful independent checks, not outside review.

## 7. Simplifications to make visible; material to move out of the main text

Keep these improvements in the introduction:

- A weight-free centroid witness and an integer-degree proof split.
- Two explicit witness formulas replacing thousands of per-shape LP bases.
- The strengthened residual bound \(D_0\ge m\).
- Removal of two hypotheses from that finite centroid theorem.
- A self-contained verifier using standard-library Python and C++17.
- Direct symbolic proofs on unbounded clipped-box and clipped-prism families.

Move chronological worked-time summaries, copied progress messages, complete
execution logs, obsolete finite multiplicity thresholds, superseded certificate
registries, and duplicate audit prose into the evidence archive or historical
appendices. State the latest result once. The earlier thresholds and remaining
ranges are development history, not current open obligations of the proposed
four-generator proof.

Retain a brief dependency table and reproducibility commands. A clean primary
route should not force a reader to reconstruct the latest theorem by combining
different generations of supplements. Preserve unsuccessful extensions in one
short limitations subsection with exact fixtures in the archive; they are useful
for explaining why the next generalization is nontrivial.

## 8. Higher dimensions: correct extent of the claims

The general line identities, moment identity, centroid formulation, residue
support restrictions, and some surface/erosion bounds transfer to
\(\mathbb N^d\). The local two-step and axis constructions also have formulas
in every \(d\), but their successful union has only been verified in the stated
three-coordinate finite class. Do not infer a universal higher-dimensional
centroid inequality merely from the existence of those formulas.

The archived clipped-box formula is a genuine analytic sufficient condition in
every \(d\ge4\); identify it as a structural family, not arbitrary Apéry ideals.
General higher-dimensional ideals may have cyclic compatibility patterns and
minimal exclusions of intermediate support. Such patterns prevent simply
adding another arm to the four-generator decomposition. The explicit
five-generator examples are counterexamples to those proposed decompositions,
not counterexamples to Wilf.

Any fixed-embedding-dimension finite-reduction claim should be clearly attached
to its own archived analytic lemmas and review status. It is not a consequence
of the four-generator theorem alone, is not an algorithmically practical
solution for five generators, and should not be confused with the established
approximate asymptotic statement of Zhai.

## Outcome

No mathematical gap was identified in the local constructions, their specified
finite coverage model, or the envelope reduction examined here. The main risks
for the final presentation are **scope inflation**, mixing the two alternative
centroid routes, presenting old counts as current, and implying that component
replays or in-session audits independently certify the entire global theorem.
