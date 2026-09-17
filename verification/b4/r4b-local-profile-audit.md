# R4b: complete local-profile audit and replay

**Status date:** 2026-09-17

## Verdict

Two fresh complete independent paths establish B4-low-local-FV under V0.
The [profile coverage theorem](../../paper/short-corner-profile-specification.md)
and [local and exceptional witness soundness](../../paper/short-corner-local-certificates.md)
therefore prove \(D_0\ge m-1\) for the \(H<6\) B4 routing subcase.
Together with R4a, this closes B4 internally; G1 gives \(W_4\ge1\).
No global theorem, external review, or formalization is claimed by this replay.

## Mathematical checking contract

Generate every ordered six-entry profile triple defined by B4.3:
nonincreasing degree-five planar profiles, the proved per-plane corner
filters and required predecessor projections, and matching shared axes.
Reject exactly reconstructed ideals with degree greater than five.
On every resulting ideal of cardinality at least 30, check
\[
U_2(T)\ge |T|-1
\quad\text{or}\quad (f,g,h)\in\{E_0,E_1\}.
\]
Both exceptional keys and their three-point witnesses are reconstructed
and checked. The analytic cardinality bound 48 is an invariant,
not a learned rejection threshold. The smaller observed maximum is not
used for pruning. There is no symmetry quotient, residue-label search,
maxima-count skip, stored dual, or floating-point decision.

## Independent implementations and coverage

[Path A](check_low_offsets.py) recursively chooses each profile entry
from zero through its previous entry and the degree cap. Each allowed
integer vector occurs exactly once. It applies positive-column drops,
then indexes the third profiles by the two shared axis counts.
It reconstructs literal points columnwise, compares the short degree
test with literal degree, and compares the cardinality formula with
the literal count. For each eligible ideal it groups points into
coordinate fibers, checks their initial intervals and both line identities,
and enumerates all ten offsets of coordinate sum at most two.

[Path B](check_low_successors.py) enumerates the Cartesian product of
the six bounded coordinate ranges and tests monotonicity. It finds mixed
corners from literal planar predecessor membership, not from a drop list.
It enumerates compatible triples directly, reconstructs their points in
the full six-cube, and tests literal degree and cardinality. Line tops are
recognized by missing successors, with length \(t_i+1\).
The gain is two if any successor has a successor, one if only an immediate
successor exists, and zero otherwise.

The successor test is equivalent to the offset definition: lower closure
supplies the intermediate point of every included two-step destination;
conversely every included successor path is an allowed destination.
The two complete generators cover the same mathematical family but share
no profile-generation, reconstruction, fiber, or gain code. They share
only Python's standard runtime and the stated integer theorem contract.
Canonical serialization of keys and results is used for diagnostic agreement,
not acceptance.

Both paths derive the exceptional residual from point membership,
integer nonnegative multipliers, mass \(3m\), and literal moments.
They obtain \(m=30,\ U_2=27\) and residuals \((0,0,54)\) and
\((0,54,0)\). Their sums exceed \(m-1=29\).

## Arithmetic, scope, and defensive tests

Every mathematical value is a Python arbitrary-precision integer.
Both checkers reject optimized execution; required checks use exceptions,
not removable assertions. No partial or sampled mode is supported.

The [runner](replay_low.py) exercises six negative cases against each
path: optimized execution, a requested sample mode, and witnesses with
bad membership, wrong mass, negative residual, or a boolean multiplier.
All twelve are rejected. These are defensive tests, not proof of the
positive universal claim.

The positive check always regenerates the full profile family from constants.
It has no certificate or historical input. No prior result is consulted.
Each path checks its theorem predicates before their results are compared.

## Frozen execution and results

The [record](r4b-replay.json) identifies clean tracked inputs at commit
`e1b0a50e21af92d89cc3f857f9f52f47623d25af`.
It hashes the two checkers, runner, and six declared mathematical notes
before checking and requires them unchanged afterward.
All source identities were rechecked against this input commit.

| Quantity | Each path |
|---|---:|
| Incident / complementary plane profile classes | 145 / 265 |
| Axis-compatible triples | 81,373 |
| Degree-filtered triples | 70,175 |
| Eligible keys | 28,499 |
| Direct local passes | 28,497 |
| Explicit exceptional witnesses | 2 |
| Largest observed degree-filtered cardinality | 43 |
| Minimum nonexceptional local margin | 1 |
| Unresolved or unsupported cases | 0 |

The common result digest is

```text
b1a06a8c5df228fef24531c5266f1ca68d49c0acb59a68290153bfbf1843c2b6
```

These counts and digest are regression diagnostics. The complete generation,
predicate checks, and analytic coverage establish the finite claim.
The combined frozen run took approximately 11.23 seconds.

## Reproduction and trust boundary

From a clean tracked repository root, with Python 3.10 or later:

```sh
python3 -I -B verification/b4/replay_low.py
```

Only the standard library is required. The command regenerates its JSON
execution record; there are no persistent binaries, bytecode, or caches.
The trusted boundary is the mathematical coverage/soundness arguments,
these two checker sources and runner, Python integer/runtime semantics,
operating system, and hardware. Independence is of code and derivation,
not of human authorship. Historical artifacts are neither imported nor
read, and the archive remains unchanged.
