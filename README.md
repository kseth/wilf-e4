# Wilf's conjecture in embedding dimension four

This repository is being reorganized into a reviewable proof artifact for the
claim that every numerical semigroup of embedding dimension four satisfies
Wilf's inequality.

The existing proof and its audit history were produced with AI assistance.
They are evidence and source material, not a substitute for external
mathematical review. The theorem should be regarded as **proposed** until the
analytic arguments and finite verifications have been independently checked.

## Repository layout

- [`paper/proof-outline.md`](paper/proof-outline.md) is the current clean proof
  spine and dependency ledger. Start here.
- [`paper/foundations.md`](paper/foundations.md) proves the common Apéry,
  residue, exclusion, and moment lemmas used by every proof branch.
- [`paper/case-partition.md`](paper/case-partition.md) proves that the
  retained branches are exhaustive and mutually exclusive.
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

The current canonical historical synthesis is
`artifacts/wilf_four_generators_review_manuscript_2026-09-11.md`. It is not the
source from which the eventual publication PDF will be built.
