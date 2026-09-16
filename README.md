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
| Main theorem | Proposed; B1 and B2 are complete under the internal trust policy and B3 is complete analytically; B4 low-height, B5, and B6 obligations remain |
| Shared analytic interfaces | Written in Markdown and internally checked; not externally reviewed or formalized |
| Multiplicity \(m\le19\) | Published external inputs audited at theorem level |
| Multiplicity \(20\le m\le29\) | Analytic reduction and two independent fresh replays complete under the repository trust policy |
| B4 high-height subcase | Analytic reduction and two independent fresh complete checking paths establish B4-high-FV under the trust policy |
| Computational verification | B1, B2, and B4 high-height are complete under the trust policy; D3 eliminates B3 computation; B4 low-height, B5, and B6 remain open |
| Release artifact | Definitive TeX, proof code, and PDF intentionally deferred until the roadmap freeze |

Here “reconstructed” means that a clean argument has been extracted from the
historical archive; it does not mean independently verified. `ROADMAP.md` is the
canonical source for task status and dependencies.

## Reader's map

Start with the [proof spine](paper/proof-outline.md). It gives the
normalization, disjoint case partition, branch targets, and links to the
individual mathematical notes. Use the [roadmap](ROADMAP.md) for live
status, dependencies, and the post-R4a checkpoint.

| Location | Role |
|---|---|
| [paper/](paper) | Mathematical proofs and code-independent finite contracts; not yet a full manuscript |
| [verification/](verification) | Internal audits, exact checking paths, manifests, and records of actual replays |
| [literature/survey.md](literature/survey.md) | Dated survey and attribution map; [L1](literature/multiplicity-through-19-audit.md) and [L2](literature/published-reduction-comparison.md) audit the external inputs and reduction choices |
| [research/](research) | Simplification decisions and diagnostic scripts; not release proof code |
| [artifacts/](artifacts) | Frozen AI-assisted research archive, not the manuscript source or a blanket-certified proof package |

For a branch-level reading path:

| Branch | Mathematical entry | Checking evidence or remaining obligation |
|---|---|---|
| B1 | [Generator-box contract](paper/small-multiplicity-specification.md), with its linked analytic reductions | [R1a](verification/b1/r1a-residue-distance-audit.md) and [R1b](verification/b1/r1b-membership-audit.md) |
| B2 | [Compactness](paper/no-corner-compactness.md) and [interval contract](paper/no-corner-interval-specification.md) | [R2](verification/b2/r2-interval-audit.md) |
| B3 | [Plane-entry lemma](paper/six-maxima-entry.md) and [analytic projection theorem](paper/three-plane-projection.md) | No retained computation; [D3](research/b3-simplification-decision.md) records the replacement |
| B4 high-height | [Compactness](paper/short-corner-compactness.md) and [interval contract](paper/short-corner-interval-specification.md) | [R4a](verification/b4/r4a-high-height-audit.md) |
| B4 low-height | [Profile coverage](paper/short-corner-profile-specification.md) and [local certificates](paper/short-corner-local-certificates.md) | R4b remains; [D4](research/b4-simplification-decision.md) selects local checks and two inline witnesses, not the old dual list |
| B5 and B6 | [Candidate contracts in the proof spine](paper/proof-outline.md#b5-residual-degree-at-most-six-a-c) | Entry proofs, finite specifications, simplification gates, and any retained replays remain |

The [Chomicz comparison](research/chomicz-assessment.md) informs the
geometric language and D5 research target; it does not discharge a branch.

Some files preserve alternatives rather than selected dependencies.
The B3 [shape](paper/six-window-shape-specification.md) and
[modular](paper/six-window-modular-specification.md) specifications are
explicitly superseded. The B4 [centroid note](paper/short-corner-centroid-certificates.md)
provides retained witness soundness, but its legacy-list machinery is not
selected. These distinctions will be reflected in the S1 branch dossiers
and S3 minimal inventory; preserving a research argument does not require
including it in the manuscript.

A coherent full working proof in Markdown is the PRELIM target.
The definitive TeX manuscript, curated proof-code package, chosen
formalization, and PDF/release packaging follow FREEZE. External review
and any additional formalization are separate from the existing internal
replays.

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
