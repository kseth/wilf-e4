# R4a: short-corner high-height audit and replay

**Status date:** 2026-09-16

## Verdict and scope

The retained high-height interval tree passed two fresh, complete, exact
checking paths. Each path independently verifies closed parameter coverage
and recomputes every required corner bound. Together with the coverage proof
in the [interval specification](../../paper/short-corner-interval-specification.md),
this establishes **B4-high-FV under V0**.

The checked statement is

\[
m-(3mQ-4w\cdot s)\le1,
\qquad m=|T|,\quad s=\sum_{x\in T}x,
\]

for every real \(w=(1,b,c)\) with
\(1\le b\le c\le Q,\ 6\le Q\le42\), every
\(p\in\{(2,1,1),(1,2,1),(1,1,2)\}\), and every finite nonempty
no-full-support-corner lower ideal \(U\) for which
\(T=U\setminus(p+\mathbb N^3)\) is nonempty and
\(\max_{x\in T}w\cdot x\le Q\).

The allowance \(Q\) need not be attained. The statement does not require
that \(p\) be an active corner, that the unit vectors belong to \(T\), or
that \(m\ge30\). The height condition applies to the retained set \(T\),
not to the uncut completion \(U\).

The [B4.2 compactness reduction](../../paper/short-corner-compactness.md)
confines any genuine high-height target failure to \(6\le H<36\).
Consequently, B4-high-FV proves \(D_0\ge m-1\) throughout the
\(H\ge6\) routing subcase; G1 then gives \(W_4\ge1\) there.
The \(H<6\) finite obligation remains open pending R4b.
This audit does not establish the whole B4 branch, the global theorem,
external mathematical review, or proof-assistant formalization.

## 1. Immutable certificate and schema

The sole proof-data file is the existing historical certificate:

```text
artifacts/wilf_four_generators_review_package_2026-09-11/
round5/one_corner_extension/short_corner_complete_certificate.json
```

Its byte length is \(31{,}363{,}264\), and its SHA-256 is

```text
c840c66eae5ade228ef500567e2bd1daa7533be89276cd6a73906abf3dfea1ac
```

It is not copied or modified. The [manifest](certificate-manifest.json)
names the historical format, exact file identity, scale \(q=4096\),
and raw root box

\[
[(4096,4096,24576),(172032,172032,172032)].
\]

Both loaders hash the same byte buffer they subsequently parse. They reject
duplicate JSON fields, unsupported versions, wrong field sets, nonfinite
JSON constants, boolean values in integer positions, and vectors of
incorrect dimension. The historical timing and success summaries are metadata,
not proof. Stored DP numerators must agree with fresh computations and
independently satisfy the target. The low-height dual list is not an input.

## 2. Mathematical interfaces audited

The code audit checks the following against the specification and G5:

1. Clipping by a strictly positive \(p\) leaves all axes unchanged. Thus a
   height bound on \(T\) bounds the coordinates of the completion \(U\).
2. A whole parameter box uses its lower weight endpoints and upper height
   endpoint for feasibility, but upper weights and lower height for the
   score. This bounds every real point in the box, not just a weight grid.
3. Inclusive rectangle counts and twice-weighted moments are exact.
   Subtracting the removed rectangle and summing disjoint retained
   rectangles give the same statistics.
4. Feasibility uses the maximum over the **retained** rectangle. Testing
   the uncut central corner would wrongly discard valid clipped centers.
5. G5 supplies a disjoint clipped center and three horns with nested
   transverse caps. The recurrence's independent horn choices therefore
   bound every allowed ideal; the zero option permits a horn to stop.
6. Direct enumeration of every smaller transverse rectangle and the
   optimized prefix recurrence evaluate the same finite maximum.
7. Order-cone tightening preserves each raw box's ordered part. Children
   meet on a closed shared wall, so exact parent-child reconstruction
   and terminal acceptance give coverage including all boundaries.

The planar leaf rule uses the proved weak inequality
\(H_0\ge3q+4(q+B_1+C_1)\); equality is accepted. No residue filter,
unit-vector assumption, maxima-count skip, sampled-weight test, or
unresolved-leaf acceptance is used.

As bounded diagnostics, 3,000 literal clipped rectangles were compared
with the historical statistics: all three corner positions, two weight
vectors, central caps through four, and all three horn axes with levels
and caps through four. Counts, twice-weighted moments, and retained
maxima agreed. Another 1,000 small raw boxes checked the two
order-tightening implementations against literal ordered intersections.
These diagnostics helped audit the interfaces; they are not substitutes
for the coverage proof or dependencies of the complete replay.

## 3. Two materially separate checking paths

[Path A](check_high_prefix.py) performs a depth-first coverage walk with
the explicit order-tightening formulas. Its fresh leaf computation uses
the frozen historical
[C++ worker](../../artifacts/wilf_four_generators_review_package_2026-09-11/round5/one_corner_extension/corner_interval_worker.cpp),
whose SHA-256 is

```text
469eca1828ab05bf2f671026dfbcbeccab80110f1bad5a330e71cd60af625bbf
```

That worker computes clipped statistics by subtraction and horn maxima
by prefix recurrence. It was also used by the historical producer:
R4a explicitly promotes its inspected source to trusted **checker code**,
not its old decisions or results. The discovery wrapper is neither
executed nor imported.

[Path B](check_high_direct.py) imports no Path A or producer code. It
performs a breadth-first coverage walk, tightens endpoints by repeated
order propagation to a fixed point, and invokes the new
[direct worker](direct_clipped_worker.cpp). This worker partitions each
retained rectangle by the first coordinate below \(p\), then sums the
disjoint pieces. For every pair of transverse caps it explicitly
enumerates every smaller rectangle transition. It uses neither clipped
subtraction formulas nor prefix maxima.

Each path reconstructs every raw child box, reaches every stored node
exactly once, and rejects a wrong root, cycle, repeated or unreachable
node, invalid split, unsupported kind, or coverage gap. Each compiles its
worker into a fresh temporary directory and requires exactly three
integer results per DP leaf. Missing, extra, partial, nonzero-exit, or
malformed worker output fails the check. In particular, the historical
worker's early return after a failing corner cannot produce an accepted
partial result.

The paths share the certificate, standard JSON facilities, language
runtimes, compiler, and mathematical theorem contract. They do not
share traversal code, clipped-statistics code, recurrence code, or
cached leaf computations. Here independence concerns implementation and
derivation paths, not authorship or external review.

## 4. Arithmetic and rejection checks

Coverage and schema arithmetic uses Python arbitrary-precision integers.
Leaf computations use signed C++ integers with at least 63 value bits;
indices have at least 31 value bits. Path A enforces these widths by a
fresh forced-include header, and Path B by source-level static assertions.
The specification proves a generous bound for all relevant values and
intermediate arithmetic:

\[
55{,}810{,}423{,}324{,}672<2^{47}<2^{63}-1.
\]

The largest indexing envelope is \(81{,}356<2^{17}\).
Sentinels are not added to scores. Mathematical predicates use no
floating-point values; floating-point timings are metadata only.

The runner exercised six rejection cases separately against both paths:

- optimized Python execution;
- certificate hash mismatch;
- duplicate manifest fields;
- an unsupported node kind;
- a four-entry DP-bound vector; and
- a child box with a boundary coverage gap.

The last three use small synthetic certificates with matching manifest
hashes, so rejection exercises the schema or coverage logic rather than
merely the hash gate. All twelve runs failed with nonzero status and
explicit checker errors. These tests support fail-closed behavior;
they are not themselves the positive finite proof.

## 5. Frozen replay and results

The final replay used clean, tracked proof inputs at commit
`349ff58c2a180d97088a8ad5d24a1eb6099e9474`.
The [runner](replay_high.py) records all eleven declared source/input
hashes before checking and requires them to remain unchanged afterward.
The [machine-readable record](r4a-replay.json) includes the exact commands,
compiler information, timestamps, exit statuses, and both complete results.

| Quantity | Each path |
|---|---:|
| Tree nodes | 110,865 |
| Split nodes | 55,432 |
| DP leaves | 54,978 |
| Analytic planar leaves | 455 |
| Empty leaves | 0 |
| All terminal leaves | 55,433 |
| Corner bounds freshly recomputed | 164,934 |
| Largest DP numerator | 4,096 |
| Smallest DP numerator | -492,320 |
| Unresolved or unsupported cases | 0 |

Every recomputed numerator is at most \(q=4096\), including the weak
equality endpoint. Both paths independently passed coverage and every
inequality before the runner compared their summaries. Their common
terminal-result digest is

```text
25682c2bcc76cc2a3d3f20670f9919e26e5f81c4bc2dc9488453ccb2ad8c8922
```

Digest agreement is a diagnostic, not the justification of acceptance.
The replay ran from 22:07:15 to 22:07:37 UTC on 2026-09-16:
Path A took approximately 3.03 seconds, Path B 18.80 seconds, and the
runner 22.82 seconds including rejection tests and provenance checks.
The environment was Python 3.14.6 and Apple clang 21.0.0 on macOS arm64.
Both workers were freshly compiled, with no warnings, persistent
binaries, or result caches. No dependency installation was needed.

## 6. Reproduction and trust boundary

From a clean tracked worktree at the repository root:

```sh
python3 -I -B verification/b4/replay_high.py
```

Requirements are Python 3.10 or later with its standard library and a
C++17 compiler available as `c++`, satisfying the checked integer widths.
No network, solver, or third-party Python package is required. The command
regenerates `verification/b4/r4a-replay.json`; timestamps and temporary
paths are expected to differ. Build directories are temporary and cleaned.
An optional record name is restricted to the B4 verification directory
and cannot overwrite proof inputs.

The trusted boundary consists of the mathematical specification and its
analytic dependencies, manifest and certificate as validated data, both
checkers and their C++ backends, runner, standard integer/JSON facilities,
compiler, operating system, and hardware. It does not include historical
producer summaries, old success flags, cached accepted lists, low-height
duals, or diagnostic counts as mathematical premises.

**R4a is complete under V0.** This is reconstruction-stage evidence, not
the final S3 artifact inventory or external review. R4b, the independent
low-height local-profile audit and replay, is the next atomic task.
