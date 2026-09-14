# Verification trust policy

## Status and decision

This document completes roadmap task V0. It fixes the evidentiary standard for
every computer-assisted statement retained in the proposed proof of Wilf's
conjecture for four generators.

The central decision is:

> A successful program run is never cited as a proof by itself. A retained
> finite lemma consists of a mathematical specification, a proof that its
> finite domain covers the intended cases, an exact fail-closed checker, and
> a fresh complete replay. Before release, it must also have an independent
> checking path proportionate to the risk of the computation.

Counts, timings, random tests, hashes, solver success messages, and prior
`PASS` records are supporting evidence only. None can replace one of the
four logical components above.

This is a policy for the final proof artifact and for the reconstruction work
leading to it. It does not retroactively certify any program in `artifacts/`.
The historical archive remains immutable source material until the relevant
roadmap specification, simplification gate, and replay have been completed.

## 1. Vocabulary and evidence levels

The following terms are reserved throughout the repository.

| Term | Meaning | What it establishes |
|---|---|---|
| **Diagnostic** | A sample, random probe, timing, count, checksum, or exploratory optimization | Evidence useful for finding mistakes; no universal theorem |
| **Specification** | A code-independent statement of the finite domain, predicate, coverage argument, arithmetic semantics, and expected output | What must be checked and why it is sufficient |
| **Complete run** | An execution that generates or covers the entire specified domain and checks every required predicate | The finite claim for that implementation and those inputs |
| **Fresh replay** | A complete run rebuilt from declared immutable inputs, without trusted cached successes or precomputed acceptance flags | Reproducibility of the complete run |
| **Independent check** | A materially separate checker or implementation derived from the mathematical specification rather than the producer's internal state | Reduced risk of a shared implementation error |
| **Provenance check** | A hash, size, manifest, or package-integrity comparison | Identity and completeness of files, not mathematical truth |
| **Audit** | Human inspection of mathematics, code, coverage, or records | Review evidence; not a replay unless the computation was actually rerun |
| **Formalization** | A proof checked by a proof assistant against an explicitly named trusted kernel and libraries | Only the statements actually formalized |

A document must use the narrowest accurate term. In particular:

- comparing stored result files is not a fresh replay;
- verifying a certificate is not a coverage replay unless certificate
  coverage is also checked;
- rebuilding a package manifest is not a mathematical verification;
- two programs written from the same pseudocode are two implementations, but
  not necessarily independent mathematical derivations;
- an exact verifier is not a proof-assistant formalization.

## 2. The five obligations for a computed lemma

Every retained `[C]` result must discharge the following obligations in
separate, reviewable form.

### 2.1 Theorem contract

The specification must state, without referring to source-code behavior:

1. the hypotheses and exact conclusion of the lemma;
2. the finite objects being quantified over;
3. their canonical representation, including coordinate order and symmetry
   conventions;
4. the exact predicate checked on each object or parameter cell;
5. all endpoints, equality cases, exceptional cases, and unsupported ranges;
6. the analytic lemmas that make the finite statement sufficient for the
   proof branch.

The manuscript will cite this mathematical contract, not an output count or a
filename.

### 2.2 Exhaustive coverage

There must be a mathematical proof that the generated or certified domain
covers every object in the theorem contract. As applicable, it must justify:

- finite bounds and termination;
- sorting, symmetry reduction, rank compression, or canonicalization;
- every pruning rule and rejection filter;
- recurrence transitions and base cases;
- subdivision of closed parameter regions, including shared boundaries;
- lifting from compressed or normalized objects back to all original cases;
- the absence of skipped, unresolved, overflowed, or unsupported cases.

Reported totals can test this reasoning, but totals alone do not prove
coverage.

### 2.3 Exact checking semantics

The acceptance predicate must be evaluated with proof-preserving arithmetic.
The default rules are:

- use integers or exact rationals whenever possible;
- prove explicit numerical bounds before using fixed-width integers;
- use interval arithmetic with documented outward rounding when enclosing a
  real parameter region;
- treat floating-point optimization only as certificate discovery, unless a
  separate rigorous error analysis proves the accepted inequality;
- convert solver output into exact rational or integer certificates and check
  those certificates without trusting the solver;
- include equality walls and use strict versus weak comparisons exactly as in
  the theorem contract.

The verifier must fail closed. Malformed inputs, hash mismatches, failed
assertions, unsupported values, unresolved leaves, arithmetic overflow, and
missing records must produce a nonzero exit rather than a warning followed by
success. Assertions required for correctness must remain enabled.

### 2.4 Fresh complete replay

A replay counts as complete only if it rebuilds the executable components and
checks the entire specified domain from the declared proof inputs. It must not
trust:

- cached success flags;
- stored accepted-leaf lists whose coverage is not rechecked;
- producer summaries in place of certificate contents;
- an earlier result file merely compared byte-for-byte;
- a sample or prefix of the finite domain.

Long computations may use deterministic checkpointing, but the replay entry
point must validate checkpoint provenance and make clear which portions were
actually recomputed. A no-cache run is preferred for the release record.

### 2.5 Independent checking path

Every computed lemma retained at release must have at least one checking path
which does not import or trust the discovery producer. The appropriate form
depends on the computation:

- **Direct exhaustion:** prefer a second implementation using a materially
  different representation or algorithm.
- **Certificate proof:** use a small exact verifier which reconstructs the
  claimed inequalities and separately checks coverage of the certificate
  family.
- **Interval tree:** independently check both local leaf bounds and complete
  coverage of the closed root region.
- **Compressed shape search:** independently check generation, lifting or
  completion, and the final arithmetic predicate; checking only the surviving
  shapes is insufficient.

Shared language runtimes, compilers, and basic exact-arithmetic libraries are
acceptable, but must be named in the trust boundary. Shared high-level search
logic, cached intermediate states, or producer-generated acceptance decisions
must be disclosed. If a genuinely independent implementation is impractical,
the branch dossier must say so and record the residual risk for the later V1
verification-scope decision.

Here *independent* refers to code and derivation paths. It does not mean
independent authorship or external peer review; those are separate obligations
in H1.

## 3. Roles inside a verification component

A component may combine roles in one executable, but its documentation must
distinguish them logically.

1. The **generator** enumerates the finite domain or subdivides a parameter
   region.
2. The **producer** may discover witnesses, optimization multipliers, or a
   compressed certificate. It is not trusted when an exact checker can verify
   its output.
3. The **checker** validates the theorem predicate and any certificate using
   the declared exact semantics.
4. The **runner** rebuilds the required code, invokes complete generation and
   checking, rejects partial modes, and writes the replay record.
5. The **manifest checker** confirms file identity. Its result is provenance,
   even when it is invoked by the runner.

The smallest practical trusted code path is preferred. Discovery code,
optimization packages, plotting utilities, and diagnostic scripts should not
be dependencies of the checker unless logically unavoidable.

## 4. Required replay record

Every retained replay must emit or accompany a machine-readable record with
at least:

- a schema version and component or roadmap ID;
- the exact theorem-contract version or hash;
- the repository commit and hashes of proof inputs, source files, and
  certificates;
- the command, working directory, and whether the run was full, fresh, and
  cache-free;
- UTC start and finish times, plus elapsed time as diagnostic metadata;
- operating system and architecture;
- interpreter, compiler, and dependency versions;
- exit status and an explicit pass/fail field;
- generated, rejected, accepted, unresolved, and unsupported counts relevant
  to the specification;
- the exact extremal value or failure witness when the contract calls for
  one;
- enough partition totals or checksums to detect truncation and regression;
- a statement of which claims the run does and does not establish.

The runner must write a failure record when practical, but the absence or
malformation of a success record can never be interpreted as success. Timing
and hardware differences do not affect the mathematical result.

## 5. Packaging and reproducibility

The final verification package for each retained component must be
self-contained at the level needed to run the checker. It will include:

- the theorem specification and coverage proof;
- readable source for the generator, checker, and runner actually used;
- immutable proof data and certificates, if any;
- a manifest of all trusted inputs;
- one documented full-replay command;
- dependency and platform requirements;
- a completed replay record and the independent-check record;
- a short explanation of the trust boundary and known limitations.

Generated binaries, compiler caches, temporary trees, exploratory outputs,
and redundant producer artifacts are excluded. Dependencies must be pinned or
bounded tightly enough for reproducibility. The release replay should require
no network access after documented dependency installation. Parallel execution
must not change coverage or acceptance, and a deterministic single-process
mode should exist whenever feasible.

The eventual directory names and common record schema will be fixed by S3,
after the simplification gates determine which computations survive. V0 fixes
the semantic requirements, not a premature code layout.

## 6. Roadmap gates

The following states must not be conflated:

1. A branch specification task such as B1.3 or B3.2 is complete when its
   theorem contract and coverage proof are reviewable. It need not yet claim
   that the historical computation has been freshly reproduced.
2. A simplification gate D1--D6 decides whether the computation remains a
   proof dependency at all.
3. A retained computed lemma clears the replay stage only after it meets
   Sections 2.3--2.5 and has conforming replay records. An individual path
   task such as R1a may close after its own audit and fresh replay, but that
   does not complete the lemma until its required independent path also
   closes.
4. S1 may incorporate the computed lemma into a clean branch dossier only
   after its specification, decision gate, and required replay are complete.
5. S2 may use that dossier in the end-to-end proof only with the trust boundary
   stated explicitly.
6. V1 decides whether independent executable replay is sufficient for release
   or whether selected analytic or finite components should also be formalized
   in a proof assistant.

Until these gates close, repository prose must say *proposed
computer-assisted proof* rather than state that external verification or
formal certification has occurred.

## 7. Treatment of the historical archive

The existing archive contains valuable source, certificate, audit, and replay
records, but uses terms such as `verify`, `replay`, `audit`, and `PASS` with
different scopes. Under this policy:

- hash-only and payload-presence commands are provenance checks;
- `--records-only` modes are record-consistency checks;
- bounded and random probes are diagnostics;
- saved JSON success records are evidence of past runs;
- certificate-only checks establish local certificate validity, not global
  coverage unless they also reconstruct the coverage argument;
- a historical full runner is a candidate replay entry point, not an accepted
  final component until its branch specification and simplification gate are
  complete.

Later R-tasks will classify each retained historical command against these
definitions, rerun it from immutable inputs, and replace or remove redundant
code. Historical files themselves remain unchanged.

## 8. Review checklist

A reviewer should be able to answer *yes* to every applicable question before
a computed lemma is promoted into the final proof.

- Is the theorem stated independently of the program?
- Is the finite domain derived from proved analytic bounds?
- Are representation, symmetry, pruning, lifting, and termination justified?
- Are all endpoints and equality cases covered?
- Is the acceptance predicate exact and fail-closed?
- Does the full command regenerate or revalidate complete coverage?
- Are cached results, manifests, and diagnostics labeled accurately?
- Can a checker run without trusting the discovery producer?
- Is there a materially independent checking path or an explicit residual-risk
  statement?
- Does the replay record identify source, inputs, environment, counts, and
  scope?
- Is the trusted software and mathematical boundary explicit?
- Are the computation's limitations preserved in the manuscript claim?

Failure of any applicable item keeps the lemma open on the roadmap. A
successful replay establishes only its stated finite contract; the global
theorem still depends on the analytic reductions, branch routing, external
literature inputs, and final composition.
