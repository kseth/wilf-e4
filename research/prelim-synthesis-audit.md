# Preliminary synthesis and composition audit

**Date:** 2026-09-17. Internal reconstruction/verification assessment,
not external review or a proof-assistant correctness verdict.

The selected reader-facing result is [prelim/](../prelim/README.md).
Its proof and checking sources are frozen separately from their complete-run
evidence. All B1--B6 reconstruction premises are now internally closed,
including [R6b](../verification/b6/r6b-high-height-audit.md).
All seven packet premises also passed on both fresh paths in a literal copy
outside the Git checkout. The [complete record](../prelim/replay.json)
matches every frozen input and the manifest; all 35 rejection tests passed.
There is no pending reconstruction or portable computational premise.

## S1 and S2: selected proof and hypothesis transfers

The proof spine and three necessary analytic appendices contain the selected
argument, with no research alternatives or historical manuscript dependency.
The dependency review checks the following:

| Transfer | Checked condition |
|---|---|
| Apéry representatives to all geometric branches | Finite lower closure, cardinality \(m\), units, distinct residues, and at most one positive corner |
| Full-weighted theorem to generator box | The theorem is analytic, uses the independently proved projection inequality, and gives a genuinely missing corner of weight at most \(M\) in a negative case |
| Missing corner to inclusive bound | Its predecessor-line contribution is at least \(M\); integer \(W_4\le-1\) yields \(M\le m(m-2)\) |
| Three-plane branch | Minimality of \((1,1,1)\) includes every planar \((1,1)\); the negative projection-score bound is at most 29 and therefore contradicts routing \(m\ge30\) |
| Phase estimate | Units justify every normalized weight at most one; line slacks give the nonnegative deficit used before any continuous gap |
| Completion and horn DP | Positive-orthant deletion preserves axis caps; retained-height feasibility, not the removed corner's height, is used |
| No-corner compactness | Degree at most four has at most 29 points; a genuine failure has \(H\ge5\), lies below 24, and is covered by an allowance-height theorem |
| Short-corner split | Degree at most five bounds cardinality by 48; the endpoint \(H=6\) is assigned to high height; every doubled-coordinate orientation is checked |
| Low profiles | Required predecessor entries and matching axes recover the three plane sections; the literal total-degree check is retained |
| Degree-six profiles | Sorted corners are accompanied by simultaneous weight permutations; plane and surface restrictions are necessary; no realizability filter is added |
| Axis witness | Remaining mass is nonnegative only when its coefficient is; otherwise the independent baseline handles the negative formula |
| Strip to continuous gap | The three almost-everywhere allowances and missing-unit cases are covered; zero supports stay zero; exceptional boundaries and the zero translation are null; the partition Jacobian is one; fiber-average remainders give \(5/42\) |
| High compactness and coverage | The gap is used only after the strip predicate; every clipping ceiling is outward, including all equality walls; every Cartesian corner in the proved range is evaluated |
| Final arithmetic | The analytic three-plane branch proves Wilf directly; the uniform deficit excludes \(W_4\le-1\) using \(D_0\le m(m-2)/(m+1)\); at \(m=30\) the normalized gap is \(1/310>0\) |

The conductor is \(c\), sorted normalized weights are \((1,b,d)\),
attained height is \(H\), allowance is \(Q\), and total degree is \(R\).
Appendix variables and local recurrence caps are explicitly scoped.
The analytic branch is not erroneously assigned a moment bound it did not prove.
No circular dependence on a finite predicate's unverified historical output
is used to justify its domain.

The composition pass caught and corrected a preliminary arithmetic
presentation error: the weakest uniform deficit does not directly imply
strict positivity. Negative integrality gives the correct nonnegative Wilf
conclusion, with the displayed \(1/310\) endpoint gap. No finite family,
predicate, evaluator, or earlier reconstruction lemma changed.
The isolated replay is restarted against the corrected document identities.

Final copyediting also corrects Christopher O'Neill's bibliographic initial
and points the appendix's projection reference explicitly to proof Section 3.
These textual corrections change no finite contract, evaluator, or data.

Native interval replay is scheduled in bounded parallel leaf batches:
forward stripes on the integer path, reverse stripes on the rational path,
with independent complete request/response coverage. Each path uses at most
four processes and half the reported CPU count. Mathematical evaluators,
predicates, and trees are unchanged; every leaf and corner is still fresh.

A further selected-proof refinement removes allowance 21: for every nonzero
translation in the mesh cube, the allowance is 18, 19, or 20.
The zero translation is null and cannot affect the integral. The standalone
strip therefore needs only 715 configurations, with unchanged continuous
gap and high-height predicate. The broader 1,029-configuration reconstruction
contract and its successful source-specific R6a record remain intact;
they are not required reader references.

## S3: exact minimal inventory and portability

The packet has one proof spine, three longer proofs in one appendix document,
one verification specification, a README, one administrative runner,
sixteen independent evaluator/coverage files, three compact trees, a manifest,
and one complete-run record: 26 files total.
The 24 manifest inputs exclude the manifest itself and the generated replay.

The compact trees preserve every split and leaf type after checked
parent-derived-box reconstruction:
50,885 no-corner nodes, 110,865 short-corner nodes, and 94,459 residual nodes.
Both independent coverage walks agree on all derived boxes and leaf types.
The new data occupy 3,424,924 bytes, rather than the 53,835,683 bytes of
the three reconstruction inputs. No cached bound survives the conversion.
Their correctness does not depend on trusting the conversion: both standalone
walks validate the entire new topology and freshly evaluate all leaves.

Excluded from the packet: the superseded three-plane shape/modular route,
LP solvers, saved short-corner duals, saved degree-six fallback lists,
producer scripts and logs, checkpoints, cached leaf results, old manifests,
and task-by-task replay records. The two exceptional witnesses are stated
inline and checked directly.

The successful literal-copy replay uses no Git checkout or external source paths.
Only Python standard libraries and a C++17 compiler are required.
The isolated replay and [read-only packet audit](audit_prelim.py) are
reconstruction QA conveniences, not dependencies of the standalone artifact.
Frozen reconstruction inputs and records are not rewritten for stylistic
consistency; the new manifest and fresh run identify the curated versions.
The existing archive is preserved outside the selected reading/runtime path.

The complete isolated run took 861.005 seconds (about 14 minutes) on the
recorded toolchain, with four native interval processes per checking path.
All seven pairs completed, with no unresolved or unsupported cases. The
post-run audit confirms source/document/data matching and both full coverage
walks again. This timing is reproduction evidence, not a theorem premise.

## Attribution and remaining decisions

[L3](../literature/survey.md#selected-proof-refresh-2026-09-17-l3) refreshed
the selected upstream versions and concrete surplus/horn searches.
Its absence-of-match finding is bounded, not a priority certification.
The preliminary proof credits Wilf, Zhai, Hellus--Rechenauer--Waldi,
Gavril, Bruns and collaborators, Kliem--Stump, the L-shape literature,
and Chomicz where relevant. Chomicz and Marashdeh are not unproved branch inputs.
The published multiplicity-through-19 computation is explicitly external.

PRELIM is promoted with exact-source matching of the complete isolated
packet record. Its selected sources were frozen at `1ecefb5`; its three-allowance
strip covers 715 configurations, and its high-height pair freshly evaluates
35,852,138 Cartesian corners on 47,088 DP leaves with exact agreement.
V1, H1, and FREEZE are not discharged
by AI-assisted internal agreement. External review, any formalization choice,
and definitive TeX/PDF production remain separate subsequent milestones.
