# R2: no-corner interval-tree audit and replay

**Status date:** 2026-09-14

## Verdict and scope

The retained B2 interval tree has passed two fresh, complete, exact checking
paths. Each path independently verifies closed coverage of the whole parameter
region and recomputes every leaf inequality. Together with the mathematical
coverage theorem in the
[`B2.2 specification`](../../paper/no-corner-interval-specification.md), this
establishes B2.2-FV under the repository trust policy.

The checked statement is

\[
|T|-D_H(T;1,b,c)\le1
\]

for every real

\[
1\le b\le c\le H,
\qquad 5\le H\le24,
\]

and every nonempty finite no-full-support-corner lower ideal whose weighted
height is at most \(H\). This replay does not independently verify the B2.1
analytic reduction, externally review the proof, formalize it in a proof
assistant, or discharge any other branch.

The retained components are:

- [`certificate-manifest.json`](certificate-manifest.json), which promotes
  one frozen historical tree by exact size and SHA-256;
- [`check_interval_prefix.py`](check_interval_prefix.py), Path A;
- [`check_interval_direct.py`](check_interval_direct.py), Path B;
- [`replay_r2.py`](replay_r2.py), the fresh fail-closed runner; and
- [`r2-replay.json`](r2-replay.json), the machine-readable replay record.

## 1. Immutable certificate and schema boundary

The proof data is the single existing file

```text
artifacts/wilf_four_generators_review_package_2026-09-11/
round5/weight_arrangement/full_interval_certificate.json
```

with byte length

```text
13,000,407
```

and SHA-256

```text
f4c39ca1720da0bde6a9845cb2b096e5c3b0fba2a1fffc67ecd72bcea6cf8da4
```

The file is not duplicated. The small manifest supplies the schema version,
component name, certificate format, exact file identity, scale \(4096\), and
root box. Both checkers validate the manifest, byte length, and hash before
parsing any proof data.

The historical format has no internal schema version. The external manifest
therefore names it `wilf-b2-interval-tree-historical-v1`, and the checkers
require its exact nine top-level fields. They also require the exact field set
for each node kind. Duplicate JSON keys are rejected rather than silently
overwritten. The historical producer's timing, completion flag, stored node
count, leaf count, and leaf bounds are not accepted as proof: the checkers
validate their types and consistency, then independently reconstruct the
coverage and inequalities.

The discovery program is not imported, executed, or trusted. Its only
retained product is the hash-identified tree.

## 2. Path A: prefix recurrence and depth-first coverage

Path A implements the B2.2 formulas directly. At every node it computes

\[
L^\sharp=(B_0,\max(B_0,C_0),\max(B_0,C_0,H_0)),
\]

\[
U^\sharp=(\min(B_1,C_1,H_1),\min(C_1,H_1),H_1).
\]

Starting from the manifest root, a depth-first walk reconstructs the exact raw
box expected at every child. A split at integer \(d\) produces the two closed
children ending and beginning at \(d\); the shared wall is therefore covered.
The checker rejects a repeated node, unreachable node, invalid child, cycle,
noninterior split, wrong child box, or unterminated branch.

For every DP leaf, Path A uses the two-dimensional prefix identity

\[
F_i(t;R,S)=
\max\{0,A_i(t;R,S),F_i(t;R-1,S),F_i(t;R,S-1)\}.
\]

It builds every level from the terminal zero layer, enumerates every feasible
central corner, adds the three independent horn bounds, and compares the
fresh result with the stored leaf numerator. Analytic and empty leaves are
checked from their exact endpoint predicates. No sampled, partial, cached, or
producer-decision mode exists.

## 3. Path B: direct recurrence and breadth-first coverage

Path B imports no code from Path A or the historical producer. Its coverage
walk uses a separate breadth-first implementation. Rather than use the closed
formula for order-cone tightening, it repeatedly propagates

\[
B_{\min}\le C_{\min}\le H_{\min},
\qquad
B_{\max}\le C_{\max}\le H_{\max}
\]

to a fixed point. It independently reconstructs both children, proves that
every stored node is reached once, and collects only valid terminal leaves.

Only after coverage succeeds does Path B evaluate the DP leaves. Its cached
function implements the direct rectangle recurrence

\[
F_i(t;R,S)=
\max\left\{0,
\max_{0\le r\le R,\ 0\le s\le S}
\bigl(S_i(t,r,s)+F_i(t+1;r,s)\bigr)
\right\},
\]

with the exact feasibility test inside the inner maximum. It explicitly
enumerates every transverse rectangle transition and does not use prefix
maxima. Thus agreement with Path A tests both the optimized recurrence and
the independently written coverage logic.

Both paths use the same immutable certificate and Python's basic JSON and
integer facilities. They do not share traversal state, recurrence code,
accepted-leaf lists, or computed leaf values.

## 4. Exact arithmetic and fail-closed behavior

All endpoint, feasibility, slice, central-box, and recurrence calculations use
Python arbitrary-precision integers. This is stronger operationally than the
signed 64-bit bound proved in B2.2 and removes overflow and sentinel concerns
from the implementation.

Both checkers return nonzero on a malformed manifest or certificate, repeated
JSON field, unknown schema or node kind, wrong root or scale, hash or byte
count mismatch, noninteger endpoint or bound, invalid topology, incomplete
coverage, failed analytic predicate, recomputed DP mismatch, or accepted value
above \(4096\). They reject Python optimized execution explicitly; correctness
does not depend on assertions.

The runner performs six negative tests before the theorem replay:

1. each checker must reject optimized execution;
2. each checker must reject an incorrect certificate hash; and
3. each checker must reject a correctly hashed synthetic tree with an
   unsupported root-node kind.

All six tests returned nonzero. These are diagnostics of the fail-closed
boundary; the complete positive runs establish the finite result.

The runner invokes both paths with isolated mode and bytecode disabled, clears
Python path and optimization environment variables, and writes no persistent
cache. It first requires a clean tracked worktree and records the input commit,
source hashes, contract and decision hashes, commands, environment, exit
statuses, timestamps, and complete outputs.

## 5. Fresh complete replay result

The two paths returned:

| Quantity | Path A: prefix | Path B: direct |
|---|---:|---:|
| Tree nodes | 50,885 | 50,885 |
| Split nodes | 25,442 | 25,442 |
| DP leaves | 24,912 | 24,912 |
| Analytic leaves | 531 | 531 |
| Empty leaves | 0 | 0 |
| Largest DP numerator | 4,096 | 4,096 |
| Smallest DP numerator | -279,776 | -279,776 |
| Unresolved | 0 | 0 |
| Unsupported | 0 | 0 |

The common scale is \(4096\), so the largest leaf includes equality in the
weak target; it is accepted exactly, not by rounding. Both paths produced the
complete leaf-result digest

```text
7096b4be7da6ba8c2891dba0ab6b2fae7134d782cb9d21dc64d9fe9460ae9b4b
```

after independently validating every entry. Digest agreement is a regression
diagnostic, not an acceptance shortcut.

On the recorded machine, Path A took about 9.2 seconds, Path B about 20.6
seconds, and the combined runner about 30.7 seconds. Timings have no
mathematical role. Exact timestamps, commands, source hashes, negative-test
records, and environment details are in `r2-replay.json`.

## 6. Reproduction and trust boundary

From a clean tracked worktree at the repository root, run

```sh
python3 verification/b2/replay_r2.py
```

The component uses only the Python standard library and requires no network
access. The replay trusts:

- the B2.2 theorem contract and its mathematical coverage proof;
- the D2 decision to retain this certificate architecture;
- the manifest, two checker sources, and runner;
- the immutable certificate as proof data rather than as prevalidated output;
- Python's arbitrary-precision integer and JSON semantics; and
- the interpreter, operating system, and hardware.

It does not trust the discovery producer, historical checker assertions,
stored success records, stored completion or acceptance decisions, sample
runs, or cached leaf results.

Under V0, R2 is complete and B2.2-FV is established. Combining it with B2.1
proves the B2 weighted theorem within the proposed proof architecture. That
analytic combination still requires external mathematical review, and the
global theorem remains conditional on the unfinished B3--B6 branches.
