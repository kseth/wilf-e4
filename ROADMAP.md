# Reconstruction and preliminary-package roadmap

**Status date:** 2026-09-17.

The goal is a self-contained, reviewable proof architecture before definitive
TeX/PDF production. The selected packet is [prelim/](prelim/README.md).
Its source-freeze and complete-run evidence are separate atomic commits.
Live state belongs here, not in frozen reconstruction inputs.

## Completed reconstruction

| Milestones | Selected result | Evidence or source |
|---|---|---|
| LIT0, CHO, L1, L2, L3 | Upstream framework attributed; published multiplicity through 19 audited; selected-source refresh | [Survey](literature/survey.md), [published-input audit](literature/multiplicity-through-19-audit.md), [L2](literature/published-reduction-comparison.md) |
| FND, PART, G1--G5 | Apéry framework, exhaustive routing, final arithmetic, line/projection/phase tools, and central-box/horns | [Selected proof](prelim/proof.md), [analytic details](prelim/analytic-details.md) |
| V0 | Explicit trust boundary and fresh independent replay policy | [Policy](verification/trust-policy.md), [standalone specification](prelim/verification.md) |
| B1.1--B1.3, D1, R1a, R1b | Inclusive generator-box reduction and two complete paths for \(20\le m\le29\) | [R1a](verification/b1/r1a-residue-distance-audit.md), [R1b](verification/b1/r1b-membership-audit.md) |
| B2.1--B2.2, D2, R2 | Continuous no-corner gap and complete real interval bound | [R2](verification/b2/r2-interval-audit.md) |
| B3.1--B3.3, D3 | Three-plane branch replaced by an analytic counting/projection proof; finite alternatives superseded | [Analytic theorem](paper/three-plane-projection.md), [decision](research/b3-simplification-decision.md) |
| B4.1--B4.4, D4, R4a, R4b | High-height interval bound; low-height complete local profiles and two inline exceptions | [R4a](verification/b4/r4a-high-height-audit.md), [R4b](verification/b4/r4b-local-profile-audit.md) |
| B5.1--B5.4, D5, R5 | Necessary plane/surface restrictions, exhaustive degree-six profiles, and local-or-axis predicates | [Proof/contract](paper/residual-degree-six.md), [R5](verification/b5/r5-degree-six-audit.md) |
| B6.1--B6.4, D6, R6a | Strip contract and replay; \(5/42\) transfer; compact failure region and exact high contract | [Proof/contract](paper/residual-high-height.md), [decision](research/b6-simplification-decision.md), [R6a](verification/b6/r6a-strip-audit.md) |
| DOC0 and consolidation | Historical alternatives separated from selected dependencies; notation and navigation normalized | [Composition/inventory audit](research/prelim-synthesis-audit.md) |

All completion language here means internal reconstruction and verification,
not independent human review. A route-selection decision does not establish
its computational premise. R3 is discharged by eliminating the computation,
not by replaying the superseded shape/modular route.

## Current execution and synthesis

| ID | Current state | Completion test |
|---|---|---|
| R6b | Two independent complete fresh high-height paths running | Validate all 94,459 nodes and freshly recompute all 47,088 DP leaves, complete Cartesian corners, exact threshold, and agreement |
| S1 | Selected branch dossiers synthesized into one proof spine plus three necessary analytic appendices | Promote after all B1--B6 finite premises close |
| S2 | End-to-end hypothesis, endpoint, normalization, and final-arithmetic audit written | Complete branch composition without an unestablished premise |
| S3 | Standalone minimal code/data/documents frozen; isolated replay running | All seven finite-premise pairs complete with exact-source matching and independent coverage/evaluation |
| PRELIM | Sources assembled; promotion pending both complete high-height replays | Stable self-contained proof, comprehensive finite contracts, minimal inventory, and complete source-matching evidence |

The active request authorizes self-contained PRELIM proof code and documents
before FREEZE. The old code-packaging cutoff is superseded for this preliminary
packet only. Definitive TeX/PDF, external coordination, and formalization
remain later work.

## Remaining topological order

1. Close R6b and the isolated whole-packet replay; promote S1--S3 and PRELIM.
2. V1: choose the additional proof-verification scope and trusted boundary.
   Targeted formalization is an option, not already completed or mandatory.
3. H1: obtain independent specialist review of the mathematics, finite
   reductions, implementations, and attribution; triage the responses.
   Private circulation is appropriate after PRELIM; no external messages
   are sent without author direction.
4. FREEZE: resolve review issues and choices, then freeze the architecture.
5. Prepare the definitive TeX manuscript, chosen final code/certificates,
   any agreed formalization, PDF, and release packaging.

PRELIM is a coherent proposed proof suitable for private review and concrete
TeX planning, not a public correctness or priority certification.
The literature search must be refreshed again before circulation/submission.

## Inventory discipline

The packet retains seven local finite premises and the one explicitly external
published multiplicity-through-19 theorem. It excludes superseded B3
computation, LP solvers, saved short-corner duals, saved degree-six fallback
lists, producer logs, checkpoints, and cached leaf answers.
Independent evaluators are not merged for tidiness.

The three interval inputs are topology-only: every child enclosure and every
leaf result is independently reconstructed. The packet uses no historical
source path, Git checkout, network service, or third-party Python dependency.
Frozen component inputs, accurate old replay records, and the research archive
remain intact outside this reader/runtime path.
Git history preserves the earlier checkpoints and atomic task decisions;
obsolete ready queues and empty milestone tables are removed from this live map.
