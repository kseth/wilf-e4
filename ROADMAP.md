# Pre-manuscript reconstruction roadmap

**Status date:** 2026-09-11

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
        end-to-end composition and trust audit
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

These items are internally reconstructed but still belong in the later
external-review packet.

## Layer 1: route-wide prerequisites

Three tasks are ready now.

| ID | Type | Atomic deliverable | Depends on | Completion test |
|---|---|---|---|---|
| L1 | [L] | Multiplicity-through-19 source audit | LIT0 | Verify the exact Bruns et al. and Kliem--Stump statements, scope, and bibliography |
| L2 | [L]+[D] | Published-reduction comparison | LIT0, FND | Decide whether Marashdeh or the known \(c\), \(n\), and type reductions shorten any branch |
| V0 | [C] | Verification trust policy | none | Fix the separation between theorem specification, exhaustive generation, exact checking, independent replay, and diagnostic counts |

## Layer 2: common analytic tools

| ID | Type | Atomic deliverable | Depends on | Completion test |
|---|---|---|---|---|
| G3 | [A] | Final-window projection inequality | FND, G2 | Prove the projection/\(E(Z)\) bound, residue accounting, and equality cases |
| G4 | [A] | Phase and thickening lemma | FND, G2 | Reconstruct the discrete phase inequality, continuous thickening identity, normalization, and endpoints |
| G5 | [A] | Central-box/three-horn theorem | FND | Give the clique-tree proof, three monotone arms, and one-corner clipping corollary |

G3 feeds B1 and B3. G4 feeds B2, B4, and B6. G5 feeds the finite
recurrences in B2 and B6.

## Layer 3: branch-entry lemmas and route specifications

These tasks justify the infinite-to-finite interfaces. They do not yet endorse
the historical computations.

### B1: multiplicity at most 29

| ID | Type | Atomic deliverable | Depends on | Completion test |
|---|---|---|---|---|
| B1.1 | [A] | Full-weighted-ideal theorem | G3 | Reconstruct the three-, four-, and impossible six-column cases |
| B1.2 | [A] | Conductor reduction | G1, G2, B1.1 | Prove \(W_4<0\Rightarrow M\le m(m-2)\), including the non-full corner argument |
| B1.3 | [C] | Finite generator-box specification | L1, B1.2, V0 | Prove exhaustive coverage of sorted minimal triples for \(20\le m\le29\) |

### B2: no full-support corner

| ID | Type | Atomic deliverable | Depends on | Completion test |
|---|---|---|---|---|
| B2.1 | [A] | Compactness reduction | G4, G5 | Derive \(1\le b\le c\le H\), \(5\le H\le24\), including the degree-four cardinality bound \(29\) |
| B2.2 | [C] | Horn-DP and interval-tree specification | B2.1, V0 | Prove exhaustive recurrence and whole-box rational bounds |

### B3: the corner \((1,1,1)\)

| ID | Type | Atomic deliverable | Depends on | Completion test |
|---|---|---|---|---|
| B3.1 | [A] | Six-maxima entry lemma | FND | Prove one mixed corner per plane, at most six maxima, and \(|Z|\le6\) |
| B3.2 | [A]+[C] | Shape-generation specification | G3, B3.1, V0 | Prove rank compression, completion, insertion growth, extension completeness, and termination |
| B3.3 | [A]+[C] | Modular-cut specification | B3.2 | Prove coverage of all residue labelings, integer lifts, cuts, and equality walls |

### B4: the corner \((2,1,1)\)

| ID | Type | Atomic deliverable | Depends on | Completion test |
|---|---|---|---|---|
| B4.1 | [A] | Height and cardinality split | FND, PART | Prove \(H<6\Rightarrow R\le5\), \(m\ge49\Rightarrow H\ge6\), and the remaining range |
| B4.2 | [A] | High-height analytic reduction | G4, B4.1 | Prove the planar bound and compact parameter reduction |
| B4.3 | [A]+[C] | Low-height shape/filter specification | FND, B4.1, V0 | Prove exhaustive profiles and every necessary residue rejection |
| B4.4 | [C] | Centroid-dual semantics | B4.3, V0 | Prove that each rational dual covers all real normalized weights |

### B5: residual degree at most six

| ID | Type | Atomic deliverable | Depends on | Completion test |
|---|---|---|---|---|
| B5.1 | [A] | Plane-corner restriction | FND, PART | Prove the per-plane bound \(|p|_1-2\), without summing across planes |
| B5.2 | [A] | Surface-injection restriction | FND, PART | Prove \(|F_i\cap F_j|\le2n_k\), including slice boundaries |
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
| D1 | [D] | Can a published or analytic result remove or shrink the \(20\le m\le29\) search? | L2, B1.2, B1.3 | Retain both exact B1 algorithms |
| D2 | [D] | Can a direct horn inequality replace B2's interval tree? | B2.1, B2.2 | Retain the exact B2 tree |
| D3 | [D] | Can the six-window conclusion be proved without full shape and cut enumeration? | B3.1--B3.3 | Retain the compressed B3 search |
| D4 | [D] | Can symbolic classification replace either B4 certificate family? | B4.2--B4.4 | Retain the high-height tree and 28,499 low-height duals |
| D5 | [D] | Can residue compatibility prove \(U_2(T)\ge m\) for genuine B5 shapes? | CHO, B5.1--B5.4 | Retain local-or-axis enumeration and \(G\) |
| D6 | [D] | Can a direct weighted argument remove the B6 strip or interval tree? | B6.1--B6.4 | Retain both exact B6 computations |

No computed component is promoted into the final architecture until its gate
has closed.

## Layer 5: audit and replay retained computations

These tasks use historical implementations. They establish what must later be
replaced or curated in the final verification package.

| ID | Type | Atomic replay/audit | Depends on |
|---|---|---|---|
| R1a | [C] | B1 cyclic-residue shortest-path algorithm | D1 retaining computation |
| R1b | [C] | B1 ordinary-membership algorithm and agreement | R1a |
| R2 | [C] | B2 interval coverage and horn-DP leaves | D2 retaining computation |
| R3 | [C] | B3 compressed shapes, 930 labelings, and 23,002 cuts | D3 retaining computation |
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

## Layer 6: synthesis and pre-manuscript freeze

| ID | Type | Atomic deliverable | Depends on | Completion test |
|---|---|---|---|---|
| L3 | [L] | Branch-level novelty and attribution refresh | D1--D6 | Search the final surplus statements and update citations without broad priority claims |
| S1 | [A]+[C] | Clean branch dossiers | B1--B6 specifications, D1--D6, and all retained replays | Each B1--B6 dossier has one theorem, proof, finite contract if any, and no historical alternatives |
| S2 | [A] | End-to-end composition audit | G1, L1, S1 | Check every hypothesis transfer and prove the main theorem once in Markdown |
| S3 | [C] | Minimal computation inventory | V0, all decisions and replays | List exactly what the final proof package must contain and why |
| V1 | [D] | Proof-verification scope decision | S2, S3 | Choose independent replay, targeted formalization, or broader formalization; name the trusted boundary |
| H1 | [H] | Architecture-review cycle | L3, S2, S3 | Send the proof notes, finite contracts, and checklist to appropriate specialists; triage every response received by the agreed cutoff |
| FREEZE | [D] | Pre-manuscript architecture freeze | H1, V1 | No unresolved dependency, review issue, route, attribution, or finite specification remains |

After `FREEZE`, and not before, begin the definitive TeX manuscript,
curated proof-code package, any chosen formalization, and PDF/release
packaging.

## Current ready queue

The topologically available tasks are L1, L2, V0, G3, G4, G5, B3.1, B4.1,
B5.1, B5.2, and B5.3. The next analytic task is **G3, the final-window
projection inequality**. It advances both the small-multiplicity conductor
route and the six-window branch.
