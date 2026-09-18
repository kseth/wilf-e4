# Proof and manuscript roadmap

**Status date:** 2026-09-17.

The goal is a self-contained, reviewable proof and manuscript before a
definitive release. The selected frozen packet is [prelim/](prelim/README.md);
the preliminary TeX/PDF draft is [manuscript/](manuscript/README.md).
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
| B6.1--B6.4, D6, R6a, R6b | Strip replay, \(5/42\) transfer, compact failure region, and complete fresh high-height verification | [Proof/contract](paper/residual-high-height.md), [R6a](verification/b6/r6a-strip-audit.md), [R6b](verification/b6/r6b-high-height-audit.md) |
| DOC0 and consolidation | Historical alternatives separated from selected dependencies; notation and navigation normalized | [Composition/inventory audit](research/prelim-synthesis-audit.md) |

All completion language here means internal reconstruction and verification,
not independent human review. A route-selection decision does not establish
its computational premise. R3 is discharged by eliminating the computation,
not by replaying the superseded shape/modular route.

## Current execution and synthesis

| ID | Current state | Completion test |
|---|---|---|
| R6b | PASS; B6 internally closed | Both fresh paths cover all 94,459 nodes and agree on all 47,088 DP leaves and 35,852,138 Cartesian corner evaluations |
| S1 | Internally complete; all B1--B6 premises closed | Selected branch dossiers synthesized into one proof spine plus three necessary analytic appendices |
| S2 | Internally complete; no pending branch premise | End-to-end hypothesis, endpoint, normalization, and negative-integrality composition audit |
| S3 | PASS; complete replay from a literal copy outside the checkout | All seven finite-premise pairs pass with exact-source matching; all 35 rejection tests pass |
| PRELIM | Internally complete; ready for private specialist review | Standalone proof, analytic appendices, comprehensive finite contracts, minimal inventory, and [complete evidence](prelim/replay.json) |
| T1 | Initial TeX/PDF draft complete | Requested section order; all selected analytic proofs; seven finite assertions; primary-source bibliography; construction history |
| T2 | PASS; editorial regression and isolated source-only build after T4 | Unchanged expressions compared against PRELIM; approved consolidations and editorial cuts recorded explicitly; implementation arithmetic envelopes remain in PRELIM; 149 labels resolve; 15 cited sources; warning-free 36-page PDF; ten-input cold build gives identical rendered text without PRELIM/Git/history |
| T3 | All six authorized edits complete; final checks PASS | Attribution and checking prose consolidated; one recurrence; shared projection/cutoff calculations; one-slab proof in named stages with a schematic; all seven finite statements and the six-column obstruction byte-for-byte unchanged |
| T4 | Complete; final checks PASS | All approved aside/disclaimer removals and direct rewrites applied, including parity explanation and degree-six encoding cuts; mathematical hypotheses, coverage, both model credits, seven finite statements, and six-column obstruction preserved |

The author has authorized a preliminary TeX/PDF draft before FREEZE, in a
separate directory. This supersedes the earlier drafting order but does not
discharge specialist review or the formalization decision. PRELIM inputs
and their source-specific complete replay remain frozen. External coordination
and a definitive release remain later work.

## Manuscript-tightening order

T3.1 is complete:
execution details, diagnostic counts, and overflow envelopes remain in the
existing packet documentation, while the paper retains exact arithmetic,
independent checking, and closed interval coverage. Attribution context lives
in the introduction and related work, with citations at actual points of use.
T3.2--T3.5 are also complete. The audit explicitly records the approved
consolidations while comparing the unchanged mathematics against PRELIM.
PRELIM and all computational contracts remain unchanged.
Literal projection-count regressions and exact rational cutoff checks also
pass. These are authoring regressions, not additional computational premises;
the frozen packet's complete source-matching replay remains unchanged.
T4 removes the approved repeated review-status disclaimers and self-evident
asides, and replaces negative comparisons with direct statements. Both
optional cuts are applied: the correction-term parity explanation and the
degree-six evaluator-specific subset encoding. The latter remains in the
packet documentation. All seven finite statements and the six-column
obstruction still match the initial TeX audit checkpoint byte for byte.
The updated expression comparison, frozen-packet audit, and ten-input
source-only cold build pass; the latter gives identical rendered text.

| Item | Proposed edit | Boundary to preserve |
|---|---|---|
| T3.1 | Complete: attribution consolidated; implementation details and repeated checking prose cleaned up | Keep introductory orientation, citations at point of use, and exact finite-family coverage |
| T3.2 | Complete: one generic nested-horn recurrence, instantiated for intervals and the strip | Preserve retained-point feasibility, termination, central-box enumeration, and every threshold |
| T3.3 | Complete: projection inequality reused; three-/four-column calculations merged | Restrict the shared calculation to the two classified projections; retain the six-column residue obstruction |
| T3.4 | Complete: one height-cutoff lemma and three-row parameter table | State \(H>3\), \(D_0<m\), \(\alpha>0\), \(0\le\beta\le3\); retain closed roots 24, 42, and 78 |
| T3.5 | Complete: named stages and one L-shaped boundary-path schematic | Retain all boundary, jump-merging, and polynomial nonnegativity arguments; clarity takes precedence over page count |
| T4 | Complete: remove repetitive status disclaimers and self-evident asides; make direct positive statements; omit parity explanation and evaluator-specific subset encoding | Preserve all seven finite statements, scope of the higher-dimensional example, conditional transfer hypothesis, rounding/coverage proofs, and construction attribution |

## Remaining topological order

1. Author read-through of the tightened draft; agree any further editorial
   changes. The approved aside/disclaimer audit is complete. The extension
   section retains its conditional hypothesis and general lower-ideal scope.
2. V1: choose the additional proof-verification scope and trusted boundary.
   Targeted formalization is an option, not already completed or mandatory.
3. H1: obtain independent specialist review of the mathematics, finite
   reductions, implementations, and attribution; triage the responses.
   Private circulation is appropriate after PRELIM; no external messages
   are sent without author direction.
4. FREEZE: resolve review issues and choices, then freeze the architecture.
5. Finalize the TeX manuscript, chosen final code/certificates,
   any agreed formalization, PDF, and release packaging.

PRELIM and the initial TeX draft are coherent artifacts suitable for private
review and exposition work, not public correctness or priority certifications.
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
