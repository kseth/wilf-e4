# Exact finite verification

This specification belongs to [the proof](proof.md).
Its finite assertions are mathematical predicates, not claims that a saved
program happened to print “PASS.” The complete replay independently
regenerates profile families, reconstructs interval coverage, and recomputes
every dynamic-programming leaf. Its seven premises are:

| Premise | Proof location | Independent checking paths |
|---|---|---|
| Inclusive generator box, \(20\le m\le29\) | Section 6 | [Cyclic residues](code/b1_residues.cpp); [ordinary membership](code/b1_membership.cpp) |
| No-corner real interval bound | Section 8 | [Prefix DP](code/b2_prefix.py); [direct recursive DP](code/b2_direct.py) |
| Short corner, high height | Section 9 | [Subtractive/prefix DP](code/b4_high_prefix.cpp); [disjoint/direct DP](code/b4_high_direct.cpp) |
| Short corner, low height | Section 9 | [Recursive profiles/offsets](code/b4_low_offsets.py); [Cartesian profiles/successors](code/b4_low_successors.py) |
| Degree-six residual profiles | Section 10 | [Recursive profiles/bitsets](code/b5_bits.cpp); [subset profiles/columns](code/b5_columns.cpp) |
| Three-allowance strip | Section 11.1 | [Subtractive/prefix DP](code/b6_strip_prefix.cpp); [retained points/direct DP](code/b6_strip_points.cpp) |
| Residual high-height real interval bound | Section 11.3 | [Subtractive DP](code/b6_high_subtract.cpp); [disjoint DP](code/b6_high_disjoint.cpp) |

The two interval coverage implementations are
[depth-first integer](code/trees_integer.py) and
[breadth-first rational](code/trees_rational.py), respectively.
Their evaluations stay separate. [verify.py](verify.py) supplies only
administrative compilation, hashing, process execution, result validation,
and agreement checks; it is not a shared mathematical evaluator.
The analytic three-plane branch has no computational premise.

## 1. Exhaustiveness and exact predicates

The proof establishes why every genuine Apéry ideal reaches a retained
geometric family. An evaluator may enlarge a family by dropping
realizability, residue, minimality, unit, or cardinality restrictions only
where its contract explicitly allows it. An upper bound on the enlarged
family remains sound.

The generator box uses the inclusive bound \(m(m-2)\). Both programs
partition every strictly increasing generator triple by the same five
mutually exclusive categories. The residue program calculates all Apéry
labels; the membership program recognizes the conductor/Apéry bound by a full
length-\(m\) membership window and counts the gaps directly. Bounded-family
counts, minima, examples, and enumeration fingerprints must agree.
Both independently check the nonnegative Wilf predicate.
The published \(m\le19\) computation is outside this replay.

The short-corner low and degree-six programs independently generate all
compatible plane profiles. Literal degree, cardinality, and stated
surface/drop filters are checked before local line-top gains.
The two exceptional short-corner witnesses are displayed in the proof;
their membership, nonnegative mass, total mass, and coordinatewise residual
are checked afresh. Degree-six local failures must pass the
denominator-cleared axis formula; zero margins are accepted.
No saved exceptional family, LP solver, modular lift, or tolerance is used.

The strip programs enumerate every sorted positive corner of degree at most
allowance plus one, for allowances 18, 19, and 20: 715 configurations.
Allowance 21 occurs only at the omitted null translation.
The replay independently
constructs the complete expected sequence and checks each score.
The second evaluator uses every subrectangle transition explicitly.
The predicate is score at most zero.

For interval trees the proof gives whole-box point domination, clipped
moments, retained-height feasibility, and the exhaustive nested-horn
recurrence. The short-corner worker checks all three orientations.
The residual worker enumerates every positive Cartesian corner in the
proved range and tests \(10V_p\le29q\), \(q=4096\).
An empty residual corner list is reported separately as vacuity.
All comparisons include the stated equality boundaries.

## 2. Compact closed-tree format

Each data file has exactly these fields:

```text
schema_version: 1
component: "b2", "b4", or "b6"
scale: 4096
root: [[lower_b, lower_d, lower_Q], [upper_b, upper_d, upper_Q]]
nodes: a nonempty indexed list
```

The fixed roots have heights \(5\ldots24\), \(6\ldots42\), and \(7\ldots78\),
respectively, with both weight coordinates ranging from one to the maximum
height. All endpoints are multiplied by the scale.

| Node | Meaning |
|---|---|
| `[axis, split, left_index, right_index]` | Split the tightened parent along axis 0, 1, or 2 |
| `[-1]` | Empty leaf, justified by an inverted tightened enclosure |
| `[-2]` | Dynamic-programming leaf, requiring fresh complete evaluation |
| `[-3]` | Analytic leaf, allowed only for the no-corner and short-corner trees |

Node zero is the root. Every node must be reached exactly once.
Child boxes are derived: the left upper and right lower endpoint equal
the split. The wall is strictly interior and shared by both closed children.
Apply order tightening before every node; for the residual tree also apply
precisely the twenty-step outward clipping schedule in proof (27).
Every finite step preserves all relevant real parameters.
Tree induction proves complete coverage, including the walls.

Analytic leaves require \(Q_0\ge2(q+B_1+C_1)+3q\) for the no-corner tree
or \(Q_0\ge4(q+B_1+C_1)+3q\) for the short-corner tree.
Every other nonempty leaf recomputes its exact bound.
No cached scores, maximizing corners, completion flags, raw child boxes,
checkpoints, timings, or producer provenance occur inside the trees.
Their shape is untrusted input, useful only after complete coverage and
all leaf predicates are checked.

## 3. Replay and rejection tests

Run `python3 -I -B verify.py`. It uses no Git or network service, resolves
all paths inside this packet, verifies every manifest input, and checks those
identities again after the run. Programs are freshly compiled with
`-std=c++17 -O3 -Wall -Wextra -pedantic`; compiler diagnostics reject a run.
At most two checking paths run concurrently. Each native interval path
uses at most four evaluator processes, capped at half the reported CPU count
(at least one). Its independent partition and response-coverage checks
assign every leaf exactly once; all leaf results are restored to index order.
This is scheduling only: each evaluator has separate state and recomputes
every supplied corner and DP state. No cached result is shared.

The replay rejects partial/unsupported arguments and optimized Python mode.
Checks are unconditional, not removable Python assertions.
Coverage mutation tests reject unknown/extended leaf records, unsound
empty/analytic leaves, wrong roots, repeated children, boundary splits,
unreachable nodes, boolean node values, and duplicate JSON keys.
Stream checks reject missing configurations, partial/extra worker responses,
malformed integers, negative counts, and threshold violations.
Changing any manifest input or its hash rejects the packet.

Agreement covers every per-leaf bound through an ordered SHA-256 fingerprint,
complete node-kind counts, extrema, and residual corner/vacuity counts.
Profile agreement includes family fingerprints and predicate partitions.
The strip compares all score fingerprints.
Generator-box agreement includes counts, minima, witnesses, and a 64-bit
modular diagnostic fingerprint, which is neither an acceptance predicate
nor a cryptographic security claim.

The generated [replay.json](replay.json) records input identities, platform,
process exit statuses/timings, result fingerprints, negative tests, and
agreement. PASS requires all seven pairs to complete without unresolved
cases or changed inputs. The record is never an acceptance input.
The manifest identifies documents, code, and trees; the replay separately
records its hash. Neither the manifest nor replay hashes itself.

## 4. Trusted boundary and review checklist

The argument depends on the published small-multiplicity theorem, the
written analytic proofs and coverage reductions, and faithful integer
evaluation by the source, compiler, and runtime. Required widths and
conservative overflow envelopes are proved in Section 12.
Independent agreement reduces error risk; it does not prove that the common
mathematical specification is correct.

External review should, in order:

1. Check Apéry lower closure, moment identity, collision rules, and
   final-window projection inequality.
2. Check the full-weighted reduction and exhaustive branch routing.
3. Check the central-box/horn theorem, continuous no-corner proof, phase
   estimate, strip transfer, and compact failure domains.
4. Check profile coverage, filters, local/axis witness soundness, and the
   two inline exceptions.
5. Read both evaluators against their contracts, check integer envelopes,
   and rerun the packet on another toolchain.
6. Review citations and contribution claims, particularly the inherited
   Apéry/initial-ideal framework and published computational theorem.

No proof-assistant certification is claimed. Suitable first targets would
be the moment identities, horn recurrence, and closed-tree coverage theorem,
followed by a kernel-checked finite certificate route. Undertaking that work
is a separate decision and would not replace review of the reductions.
