# Wilf's conjecture in embedding dimension four

This repository is being reorganized into a reviewable proof artifact for the
claim that every numerical semigroup of embedding dimension four satisfies
Wilf's inequality.

The existing proof and its audit history were produced with AI assistance.
They are evidence and source material, not a substitute for external
mathematical review. The theorem should be regarded as **proposed** until the
analytic arguments and finite verifications have been independently checked.

## Proof maturity

| Component | Current state |
|---|---|
| Main theorem | Proposed; B1 and B2 are complete under the internal trust policy and B3 is complete analytically; B4--B6 remain to be simplified and audited |
| Shared foundations, routing, G1--G5, B2.1, B2.2, D2, B3.1, D3, and B4.1--B4.4 | Written in Markdown and internally checked; not independently reviewed |
| Multiplicity \(m\le19\) | Published external inputs audited at theorem level |
| Multiplicity \(20\le m\le29\) | Analytic reduction and two independent fresh replays complete under the repository trust policy |
| Computational verification | B1 and B2 are complete under the trust policy; D3 eliminates B3 computation; B4--B6 remain open |
| Release artifact | Definitive TeX, proof code, and PDF intentionally deferred until the roadmap freeze |

Here “reconstructed” means that a clean argument has been extracted from the
historical archive; it does not mean independently verified. `ROADMAP.md` is the
canonical source for task status and dependencies.

## Repository layout

- [`ROADMAP.md`](ROADMAP.md) is the topologically ordered plan through the
  pre-manuscript proof-architecture freeze.
- [`paper/proof-outline.md`](paper/proof-outline.md) is the current clean proof
  spine and dependency ledger. Start here.
- [`paper/foundations.md`](paper/foundations.md) proves the common Apéry,
  residue, exclusion, and moment lemmas used by every proof branch.
- [`paper/case-partition.md`](paper/case-partition.md) proves that the
  retained branches are exhaustive and mutually exclusive.
- [`paper/final-arithmetic.md`](paper/final-arithmetic.md) converts the three
  branch bounds into Wilf's inequality and checks their endpoints.
- [`paper/coordinate-lines.md`](paper/coordinate-lines.md) proves the
  line-count, line-top, weighted-deficit, and endpoint-upgrade identities.
- [`paper/phase-and-thickening.md`](paper/phase-and-thickening.md) proves the
  summed sawtooth phase inequality, exact rectangular-thickening identity,
  support preservation, and the compactness endpoints used by B2, B4, and B6.
- [`paper/central-box-horns.md`](paper/central-box-horns.md) proves the
  clique-tree decomposition into a central box and three monotone horns, its
  one-corner clipping corollary, and the exact nested-cap recurrence interface.
- [`paper/no-corner-compactness.md`](paper/no-corner-compactness.md) proves the
  continuous no-corner moment inequality, the degree-four cardinality
  bound, and the compact real parameter domain for B2.
- [`paper/no-corner-interval-specification.md`](paper/no-corner-interval-specification.md)
  states B2's finite theorem contract and proves the horn recurrence,
  whole-box bounds, and closed interval-tree coverage semantics.
- [`paper/final-window-projection.md`](paper/final-window-projection.md)
  proves the exact residue/projection bound and audits its equality boundary.
- [`paper/six-maxima-entry.md`](paper/six-maxima-entry.md) proves that the
  corner \((1,1,1)\) forces at most one mixed corner per coordinate plane,
  at most six maximal points, and at most six final-window points.
- [`paper/three-plane-projection.md`](paper/three-plane-projection.md)
  proves that a negative B3 projection score forces at most 29 points and
  closes the \(m\ge30\) branch analytically.
- The superseded [shape specification](paper/six-window-shape-specification.md)
  and [modular specification](paper/six-window-modular-specification.md)
  describe the broader six-window alternative; neither is a retained
  main-proof dependency or an established finite lemma.
- [`paper/short-corner-height-split.md`](paper/short-corner-height-split.md)
  proves the sharp short-corner degree bound and confines the \(H<6\) side
  of B4 to \(30\le m\le48\), analytically.
- [`paper/short-corner-compactness.md`](paper/short-corner-compactness.md)
  proves the planar mean bounds and improved \(H<36\) high-height failure
  cutoff, with compatibility to the historical \(42\)-box.
- [`paper/short-corner-profile-specification.md`](paper/short-corner-profile-specification.md)
  proves the low-height residue filters and exhaustive profile construction,
  and states the open B4-low-FV weighted obligation. Its
  [construction diagnostic](research/check_b4_low_height_profiles.py) is
  research tooling, not release proof code or a dual replay.
- [`paper/short-corner-centroid-certificates.md`](paper/short-corner-centroid-certificates.md)
  proves exact centroid-certificate soundness for all real weights, the
  integer checking predicate, and reduction to three maximal points; it
  specifies complete-family checking without declaring a full replay.
- [`paper/full-weighted-ideal.md`](paper/full-weighted-ideal.md) classifies
  full weighted ideals, excludes the six-column triangle analytically, and
  proves Wilf's inequality for this subcase.
- [`paper/conductor-reduction.md`](paper/conductor-reduction.md) proves that a
  negative Wilf number forces bounded Apéry maximum, conductor, and
  nonmultiplicity generators.
- [`paper/small-multiplicity-specification.md`](paper/small-multiplicity-specification.md)
  specifies the exact finite obligation for \(20\le m\le29\) and proves
  that its sorted minimal generator tuples cover every possible
  counterexample.
- [`verification/trust-policy.md`](verification/trust-policy.md) defines the
  evidentiary standard, exactness rules, independent-check requirement, and
  replay records for every retained computation.
- [`verification/b1/r1a-residue-distance-audit.md`](verification/b1/r1a-residue-distance-audit.md)
  proves the residue-cycle update, audits the first B1 implementation, and
  records its fresh complete replay.
- [`verification/b1/r1b-membership-audit.md`](verification/b1/r1b-membership-audit.md)
  proves the ordinary-membership path, records its independent replay, and
  audits agreement with R1a.
- [`verification/b2/r2-interval-audit.md`](verification/b2/r2-interval-audit.md)
  audits the retained B2 tree and records two fresh complete checking paths.
- [`literature/multiplicity-through-19-audit.md`](literature/multiplicity-through-19-audit.md)
  verifies the exact published statements that remove \(m\le19\), their
  scope, computational dependencies, and version-of-record citations.
- [`literature/published-reduction-comparison.md`](literature/published-reduction-comparison.md)
  decides how the known conductor, left-element, and type reductions and
  Marashdeh's defect decomposition affect the retained branches.
- [`research/b1-simplification-decision.md`](research/b1-simplification-decision.md)
  records why the exact \(20\le m\le29\) finite obligation and its two
  independent checking paths are retained.
- [`research/b2-simplification-decision.md`](research/b2-simplification-decision.md)
  records why D2 retains the B2 interval tree after the direct horn
  simplification gate.
- [`research/b3-simplification-decision.md`](research/b3-simplification-decision.md)
  records D3's analytic replacement, removal of R3, and downstream dependency
  audit. Its small diagnostic script is not release proof code.
- [`literature/survey.md`](literature/survey.md) records prior results, direct
  technical predecessors, the current-state search, and the attribution plan.
- [`research/chomicz-assessment.md`](research/chomicz-assessment.md) records the
  focused comparison with Chomicz's three-dimensional L-shape construction.
- `artifacts/` is the frozen research archive: manuscripts, historical routes,
  exact programs, certificates, and replay records.
- A definitive TeX paper and a minimal verification package will be added only
  after the retained proof route has stabilized.

## Working principles

1. Keep the mathematical proof, finite-verification specifications, and
   historical research record separate.
2. State the hypotheses and conclusion of every computer-assisted lemma
   independently of its implementation.
3. Explain why every finite search is exhaustive before reporting its output.
4. Prefer short analytic arguments or small checkable certificates to large
   enumerations.
5. Do not edit the historical archive while reconstructing the proof.
6. Attribute inherited constructions at the point of use and reserve novelty
   claims for the precise surplus estimates proved here.
7. Distinguish complete mathematical replays from provenance checks,
   record comparisons, and diagnostic experiments.
8. Use `\(...\)` for inline mathematics and `\[...\]` for display
   mathematics; use roadmap task identifiers consistently across notes.

The current canonical historical synthesis is
`artifacts/wilf_four_generators_review_manuscript_2026-09-11.md`. It is not the
source from which the eventual publication PDF will be built.
