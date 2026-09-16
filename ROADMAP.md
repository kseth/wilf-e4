# Pre-manuscript reconstruction roadmap

**Status date:** 2026-09-16

## Purpose and cutoff

This is the execution order for work that must precede the definitive TeX
manuscript and final minimal verification package. Its endpoint is a frozen
proof architecture: every analytic lemma has a reviewable proof, every
retained finite assertion has a mathematical specification and audited replay,
and every external input has been checked at theorem level.

Historical programs may be run during reconstruction. Curating and packaging
the final proof code happens only after this roadmap is complete. Each task
below should normally produce one reviewable note, decision, or replay record
and one commit.

## Labels

- **[A]** conventional analytic proof;
- **[C]** finite-verification specification or audit;
- **[L]** literature and attribution;
- **[D]** route-selection decision;
- **[H]** independent human or external review.

## Dependency overview

```text
completed: literature baseline + foundations + case partition
                         |
             +-----------+-----------+
             |                       |
      common analytic tools     source/verification policy
             |                       |
     +-------+-------+---------------+
     |       |       |       |       |
    B1      B2      B3      B4    B5 and B6
     |       |       |       |       |
     +-------+--- simplification gates --+
                         |
             retained finite replays
                         |
       branch dossiers + literature refresh
                         |
        end-to-end composition + artifact inventory
                         |
             preliminary package checkpoint
                         |
        verification decision + external review
                         |
               pre-manuscript freeze
```

The layer numbers give a convenient topological order, but they are not
barriers: any task may begin as soon as its stated dependencies are complete.

## Completed base

| ID | Result | Location |
|---|---|---|
| LIT0 | Broad literature and attribution survey | [`literature/survey.md`](literature/survey.md) |
| CHO | Focused Chomicz comparison | [`research/chomicz-assessment.md`](research/chomicz-assessment.md) |
| FND | Apéry lower ideal, moment identity, and exclusion rules | [`paper/foundations.md`](paper/foundations.md) |
| PART | Exhaustive and disjoint branch routing | [`paper/case-partition.md`](paper/case-partition.md) |
| G1 | Final-arithmetic lemma and conditional branch assembly | [`paper/final-arithmetic.md`](paper/final-arithmetic.md) |
| G2 | Coordinate-line calculus and weighted-deficit identities | [`paper/coordinate-lines.md`](paper/coordinate-lines.md) |
| G3 | Final-window projection inequality and equality audit | [`paper/final-window-projection.md`](paper/final-window-projection.md) |
| G4 | Phase inequality, rectangular thickening, and endpoint audit | [`paper/phase-and-thickening.md`](paper/phase-and-thickening.md) |
| G5 | Central-box/three-horn decomposition and clipping corollary | [`paper/central-box-horns.md`](paper/central-box-horns.md) |
| B2.1 | Continuous no-corner inequality and compactness reduction | [`paper/no-corner-compactness.md`](paper/no-corner-compactness.md) |
| B2.2 | No-corner horn-DP and interval-tree specification | [`paper/no-corner-interval-specification.md`](paper/no-corner-interval-specification.md) |
| B1.1 | Full-weighted-ideal theorem and six-column exclusion | [`paper/full-weighted-ideal.md`](paper/full-weighted-ideal.md) |
| B1.2 | Negative-case conductor and generator bounds | [`paper/conductor-reduction.md`](paper/conductor-reduction.md) |
| V0 | Verification vocabulary, trust boundary, and replay policy | [`verification/trust-policy.md`](verification/trust-policy.md) |
| L1 | Multiplicity-through-19 statement, scope, and source audit | [`literature/multiplicity-through-19-audit.md`](literature/multiplicity-through-19-audit.md) |
| B1.3 | Finite generator-box specification and coverage proof | [`paper/small-multiplicity-specification.md`](paper/small-multiplicity-specification.md) |
| DOC0 | Reader-facing notation, status, and milestone normalization | [`README.md`](README.md), [`paper/proof-outline.md`](paper/proof-outline.md), and this roadmap |
| L2 | Published conductor, left-element, type, and Marashdeh comparison | [`literature/published-reduction-comparison.md`](literature/published-reduction-comparison.md) |
| D1 | Retain the exact B1 finite obligation and two independent checking paths | [`research/b1-simplification-decision.md`](research/b1-simplification-decision.md) |
| D2 | Retain the exact B2 interval tree and two independent checking paths | [`research/b2-simplification-decision.md`](research/b2-simplification-decision.md) |
| R1a | B1 cyclic-residue algorithm audit and fresh complete replay | [`verification/b1/r1a-residue-distance-audit.md`](verification/b1/r1a-residue-distance-audit.md) |
| R1b | B1 ordinary-membership audit, fresh replay, and R1a agreement | [`verification/b1/r1b-membership-audit.md`](verification/b1/r1b-membership-audit.md) |
| R2 | B2 interval-tree audit and two fresh complete checking paths | [`verification/b2/r2-interval-audit.md`](verification/b2/r2-interval-audit.md) |
| B3.1 | One mixed corner per plane, six global maxima, and \(\lvert Z\rvert\le6\) | [`paper/six-maxima-entry.md`](paper/six-maxima-entry.md) |
| B3.2 | Finite shape-generation specification (superseded alternative) | [`paper/six-window-shape-specification.md`](paper/six-window-shape-specification.md) |
| B3.3 | Modular-cut and integer-lift specification (superseded alternative) | [`paper/six-window-modular-specification.md`](paper/six-window-modular-specification.md) |
| D3 | Analytic three-plane projection bound; all B3 finite verification removed | [`paper/three-plane-projection.md`](paper/three-plane-projection.md), [`research/b3-simplification-decision.md`](research/b3-simplification-decision.md) |
| B4.1 | Sharp short-corner degree bound and exact remaining height/cardinality ranges | [`paper/short-corner-height-split.md`](paper/short-corner-height-split.md) |
| B4.2 | Planar mean bounds, improved high-height failure region \(H<36\), and analytic leaf rules | [`paper/short-corner-compactness.md`](paper/short-corner-compactness.md) |
| B4.3 | Necessary per-plane residue filters, exhaustive low-height profiles, and B4-low-FV contract | [`paper/short-corner-profile-specification.md`](paper/short-corner-profile-specification.md) |
| B4.4 | Exact centroid-dual soundness, integer predicate, three-maximal-point reduction, and complete-family checking semantics | [`paper/short-corner-centroid-certificates.md`](paper/short-corner-centroid-certificates.md) |

These items are internally reconstructed but still belong in the later
external-review packet when they are retained proof dependencies. The
superseded B3 alternatives are preserved research specifications, not required
components of that packet.

## Layer 1: route-wide prerequisites

All route-wide prerequisites are complete. L2 retains the moment-deficit
architecture, adds the analytic disposal
\(|\operatorname{Max}(T)|\le3\), and finds no published reduction that removes
the B1 finite obligation or any of B2--B6.

## Layer 2: common analytic tools

All common analytic tools are complete. G3 feeds B1 and B3; G4 feeds B2, B4,
and B6; and G5 supplies the structural recurrence interface used by B2 and
B6.

## Layer 3: branch-entry lemmas and route specifications

These tasks justify the infinite-to-finite interfaces. They do not yet endorse
the historical computations.

### B1: multiplicity at most 29

The branch-entry specification, L2 comparison, D1 gate, and both independent
replays are complete. B1.3-FV is established under V0.

### B2: no full-support corner

The analytic entry and finite specification are complete. B2.1 proves the
continuous no-corner moment inequality, degree-four cardinality bound,
compact failure region, and analytic leaf rule. B2.2 states the stronger
allowance-height finite obligation and proves the exact horn recurrence,
whole-box integer domination, and closed interval-tree coverage theorem.

B2.2 supplies the specification and coverage theorem, D2 retains its finite
obligation and exact interval tree, and R2 supplies two fresh complete and
independent checking paths. B2.2-FV and the B2 computed lemma are complete
under V0.

### B3: the corner \((1,1,1)\)

B3 is complete analytically. B3.1 proves that the ideal lies in three
coordinate planes, each with at most one mixed corner. D3's three-plane
counting theorem proves
\(\Phi(T,\operatorname{Max}(T))<0\Rightarrow |T|\le29\).
The routing hypothesis \(m\ge30\), final-window subset monotonicity, and G3
therefore prove \(W_4\ge0\), without any finite verification.

B3.2 and B3.3 remain completed specifications of the broader six-window
alternative, but are no longer retained main-proof dependencies. B3.3-FV
has not been established under V0 and is not needed. D3 discharges R3 by
removing the computation, not by supplying a replay.

### B4: the corner \((2,1,1)\)

B4.1 is complete analytically. The sharp bound
\(m\le2R^2-R+3\) gives \(m\ge49\Rightarrow H\ge6\) and confines
the \(H<6\) side to \(30\le m\le48\), with \(R=4\) or \(5\).
For \(32\le m\le48\), necessarily \(R=5\) and \(5\le H<6\).
The endpoint \(H=6\) belongs to the high-height side; degree at most five
alone does not imply low height. No residue filter or weighted deficit
estimate is established by this split.

B4.2 is complete analytically. Two planar partitions and the G4 phase cutoff
confine any high-height target failure to
\(1\le b\le c\le H,\ 6\le H<36\), retaining all three positions of the
doubled corner coordinate. Optional weight bounds give \(b<9,\ c<17\).
The historical certificate's larger closed \(42\)-box remains a compatible
superset; no certificate has been changed or replayed. Both simple and
refined planar acceptance rules include their equality boundaries.

B4.3 is complete as a specification and analytic coverage proof. It proves
the two-corner per-plane bound, with at most one corner at \(x\ge2\) in
each plane incident to the doubled coordinate, and defines all compatible
degree-five profiles without a maxima-count skip. The final degree check
reduces to at most four row inequalities. A standalone construction
diagnostic agrees with the historical 70,175 shapes and 28,499 eligible
keys; no weighted dual is replayed and B4-low-FV remains open.

B4.4 is complete as exact certificate semantics and an analytic soundness
proof. It derives the three-coordinate residual from the point multipliers,
proves the all-real-weight/height-allowance slack identity, and gives an
equivalent integer predicate. Any valid witness can be reduced to at most
three maximal points without weakening its bound.
R4b must explicitly validate schema dimensions: the historical verifier
does not enforce a three-entry cached residual before summing it, although
all saved records have that dimension. No full weighted replay has been
performed and B4-low-FV remains open.

All B4 entry/specification tasks are now complete. D4 is the next dependency:
decide whether either certificate family can be replaced analytically before
running any retained R4a or R4b computation.

### B5: residual degree at most six

| ID | Type | Atomic deliverable | Depends on | Completion test |
|---|---|---|---|---|
| B5.1 | [A] | Plane-corner restriction | FND, PART | Prove the per-plane bound \(\lvert p\rvert_1-2\), without summing across planes |
| B5.2 | [A] | Surface-injection restriction | FND, PART | Prove \(\lvert F_i\cap F_j\rvert\le2n_k\), including slice boundaries |
| B5.3 | [A] | Local and axis centroid witnesses | G2 | Prove \(D_0\ge U_2\) and, when applicable, \(D_0\ge G\) |
| B5.4 | [C] | Degree-six profile specification | B5.1, B5.2, V0 | Prove exhaustive profiles, shared-axis conditions, corner cuts, and filters |

### B6: residual degree at least seven

| ID | Type | Atomic deliverable | Depends on | Completion test |
|---|---|---|---|---|
| B6.1 | [C] | Finite-strip theorem specification | G5, V0 | Justify allowances \(18,19,20,21\), the corner range, and horn recurrence |
| B6.2 | [A] | Finite-to-continuous transfer | B6.1 | Derive the \(5/42\) gap, including boundary, support, Jacobian, and remainder checks |
| B6.3 | [A] | High-height compactness | G4, B6.2 | Derive \(7\le H<78\) and all closed-box clipping inequalities |
| B6.4 | [C] | High-height interval-tree specification | B6.3, V0 | Prove recurrence, whole-box bounds, outward rounding, and coverage |

## Layer 4: bounded simplification gates

Each research gate ends with a written decision: adopt a proved replacement,
or retain the existing route. These gates come before expensive replay and
final code design.

| ID | Type | Question | Depends on | Fallback |
|---|---|---|---|---|
| D4 | [D] | Can symbolic classification replace either B4 certificate family? | B4.2--B4.4 | Retain the high-height tree and 28,499 low-height duals |
| D5 | [D] | Can residue compatibility prove \(U_2(T)\ge m\) for genuine B5 shapes? | CHO, B5.1--B5.4 | Retain local-or-axis enumeration and \(G\) |
| D6 | [D] | Can a direct weighted argument remove the B6 strip or interval tree? | B6.1--B6.4 | Retain both exact B6 computations |

D1 is complete and retains B1.3-FV with both independent checking paths. D2
is complete and retains the B2.2-FV contract with the exact interval tree and
both R2 checking paths. D3 is complete with an analytic replacement for the
actual B3 routing cell and removes every B3 computed component. No other
computed component is promoted into the final architecture until its gate
has closed.

## Layer 5: audit and replay retained computations

These tasks use historical implementations. They establish what must later be
replaced or curated in the final verification package.

| ID | Type | Atomic replay/audit | Depends on |
|---|---|---|---|
| R4a | [C] | B4 high-height interval certificate | D4 retaining it |
| R4b | [C] | B4 28,499 low-height rational duals | D4 retaining them |
| R5 | [C] | B5 5,574,644 shapes and 431 fallbacks | D5 retaining computation |
| R6a | [C] | B6 1,029 finite-strip configurations | D6 retaining that component |
| R6b | [C] | B6 47,088 high-height interval leaves | D6 retaining that component |

Each replay must record source hashes, commands, exact counts, arithmetic
bounds, environment information, and a result independent of cached success
flags.

A conditional replay edge is satisfied automatically if its decision gate
proves a replacement and removes that computation.

R3 is discharged by D3's analytic replacement and is no longer scheduled.
No B3 shape, residue-label, modular-cut, or linear-program data belongs in the
required minimal verification inventory.

R1a and R1b are complete. Each path independently establishes B1.3-FV, and
their common classification and bounded-domain diagnostics agree. R2 is also
complete: both paths independently establish B2 tree coverage and every leaf
bound. The B1 and B2 finite lemmas are complete under V0.

## Layer 6: synthesis and pre-manuscript freeze

| ID | Type | Atomic deliverable | Depends on | Completion test |
|---|---|---|---|---|
| L3 | [L] | Branch-level novelty and attribution refresh | D1--D6 | Search the final surplus statements and update citations without broad priority claims |
| S1 | [A]+[C] | Clean branch dossiers | B1--B6 specifications, D1--D6, and all retained replays | Each B1--B6 dossier has one theorem, proof, finite contract if any, and no historical alternatives |
| S2 | [A] | End-to-end composition audit | G1, L1, S1 | Check every hypothesis transfer and prove the main theorem once in Markdown |
| S3 | [C] | Minimal computation inventory | V0, all decisions and replays | List exactly what the final proof package must contain and why |
| PRELIM | [D] | Preliminary-package readiness checkpoint | L3, S1, S2, S3 | The end-to-end Markdown proof, retained replay evidence, and minimal artifact inventory are stable enough for private circulation and TeX planning |
| V1 | [D] | Proof-verification scope decision | PRELIM | Choose independent replay, targeted formalization, or broader formalization; name the trusted boundary |
| H1 | [H] | Architecture-review cycle | PRELIM | Send the proof notes, finite contracts, and checklist to appropriate specialists; triage every response received by the agreed cutoff |
| FREEZE | [D] | Pre-manuscript architecture freeze | H1, V1 | No unresolved dependency, review issue, route, attribution, or finite specification remains |

`PRELIM` marks a coherent preliminary research package, not a public theorem
claim. It permits private circulation and concrete TeX/artifact planning.
After `FREEZE`, and not before, begin the definitive TeX manuscript, curated
proof-code package, any chosen formalization, and PDF/release packaging.

## Current ready queue

The topologically available tasks are D4, B5.1, B5.2, B5.3, and B6.1.
The recommended next task is **D4, the short-corner symbolic simplification
gate**: use the proved planar and three-point centroid interfaces to seek an
analytic replacement, or document why either certificate family is retained.
