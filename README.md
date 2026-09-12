# Wilf's conjecture in embedding dimension four

This repository is being reorganized into a reviewable proof artifact for the
claim that every numerical semigroup of embedding dimension four satisfies
Wilf's inequality.

The existing proof and its audit history were produced with AI assistance.
They are evidence and source material, not a substitute for external
mathematical review. The theorem should be regarded as **proposed** until the
analytic arguments and finite verifications have been independently checked.

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
- [`paper/final-window-projection.md`](paper/final-window-projection.md)
  proves the exact residue/projection bound and audits its equality boundary.
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
- [`literature/multiplicity-through-19-audit.md`](literature/multiplicity-through-19-audit.md)
  verifies the exact published statements that remove (m\le19), their
  scope, computational dependencies, and version-of-record citations.
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

The current canonical historical synthesis is
`artifacts/wilf_four_generators_review_manuscript_2026-09-11.md`. It is not the
source from which the eventual publication PDF will be built.
