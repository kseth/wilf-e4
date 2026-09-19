# Exact finite verification

This specification accompanies [the manuscript](../manuscript/wilf-four-generators.pdf).
The complete replay independently regenerates finite families and checks their
predicates. The three interval certificates encode subdivision topology rather
than cached bounds: each checking path reconstructs full coverage, justifies
empty and analytic leaves, and recomputes every dynamic-programming bound.
Input hashes identify the exact files used in a run; result fingerprints
compactly compare computed results. Coverage and predicate checks establish
the computational premises.

| Premise | Manuscript location | Independent checking paths |
|---|---|---|
| Inclusive generator box, \(20\le m\le29\) | Finite Lemma 2.2, Section 2.6 | [Cyclic residues](code/generator_box_residues.cpp); [ordinary membership](code/generator_box_membership.cpp) |
| No-full-corner real interval bound | Finite Lemma 2.3, Section 2.8 | [Prefix DP](code/no_corner_interval_prefix.py); [direct recursive DP](code/no_corner_interval_direct.py) |
| Short corner, high height | Finite Lemma 2.4, Section 2.9 | [Subtractive/prefix DP](code/short_corner_high_prefix.cpp); [disjoint/direct DP](code/short_corner_high_direct.cpp) |
| Short corner, low height | Finite Lemma 2.5, Section 2.9 | [Recursive profiles/offsets](code/short_corner_low_offsets.py); [Cartesian profiles/successors](code/short_corner_low_successors.py) |
| Degree-six residual profiles | Finite Lemma 2.6, Section 2.10 | [Recursive profiles/bitsets](code/degree_six_bits.cpp); [subset profiles/columns](code/degree_six_columns.cpp) |
| Three-allowance strip | Finite Lemma 2.7, Section 2.11.1 | [Subtractive/prefix DP](code/strip_prefix.cpp); [retained points/direct DP](code/strip_points.cpp) |
| Residual high-height real interval bound | Finite Lemma 2.8, Section 2.11.3 | [Subtractive DP](code/high_height_subtract.cpp); [disjoint DP](code/high_height_disjoint.cpp) |

The two interval coverage implementations are
[depth-first integer](code/trees_integer.py) and
[breadth-first rational](code/trees_rational.py), respectively.
The runner [verify.py](verify.py) compiles and executes the separate
evaluators, validates results, and checks agreement.

## 1. Exhaustiveness and exact predicates

The proof establishes that every Apéry ideal arising in the argument belongs
to one of the retained geometric families. An evaluator may enlarge a family
by dropping realizability, residue, minimality, unit, or cardinality
restrictions only where its contract explicitly allows it. An upper bound on
the enlarged family remains sound.

The generator box uses the inclusive bound \(m(m-2)\). Both programs
partition every strictly increasing generator triple by the same five
mutually exclusive categories. The residue program calculates all Apéry
labels; the membership program recognizes the conductor/Apéry bound by a full
length-\(m\) membership window and counts the gaps directly. Bounded-family
counts, minima, examples, and enumeration fingerprints must agree.
Both independently check the nonnegative Wilf predicate.

The short-corner low and degree-six programs independently generate all
compatible plane profiles. Literal degree, cardinality, and stated
surface/drop filters are checked before local line-top gains.
The two exceptional short-corner witnesses are displayed in the proof;
their membership, nonnegative mass, total mass, and coordinatewise residual
are checked afresh. Degree-six local failures must pass the
denominator-cleared axis formula; zero margins are accepted.

The strip programs enumerate every sorted positive corner of degree at most
allowance plus one, for allowances 18, 19, and 20: 715 configurations.
The replay independently constructs the complete expected sequence and
checks each score.
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
component: "no-corner-interval", "short-corner-high", or "high-height"
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
| `[-3]` | Analytic leaf, allowed only for the no-full-corner and short-corner trees |

Node zero is the root. Every node must be reached exactly once.
Child boxes are derived: the left upper and right lower endpoint equal
the split. The wall is strictly interior and shared by both closed children.
Apply order tightening before every node; for the residual tree also apply
precisely the twenty-step outward clipping schedule in manuscript (2.26)
(TeX label `eq:p:27`).
Every finite step preserves all relevant real parameters.
Tree induction proves complete coverage, including the walls.

Analytic leaves require \(Q_0\ge2(q+B_1+C_1)+3q\) for the no-full-corner tree
or \(Q_0\ge4(q+B_1+C_1)+3q\) for the short-corner tree.
Every other nonempty leaf recomputes its exact bound.
The certificates encode subdivision topology. Acceptance requires complete
coverage and verification of every terminal predicate.

## 3. Replay and rejection tests

Run `python3 -I -B verify.py`. The runner verifies every manifest input
before and after execution. Programs are freshly compiled with
`-std=c++17 -O3 -Wall -Wextra -pedantic`; compiler diagnostics reject a run.
At most two checking paths run concurrently. Each native interval path
uses at most four evaluator processes, capped at half the reported CPU count
(at least one). Its independent partition and response-coverage checks
assign every leaf exactly once; all leaf results are restored to index order.
Each checking path maintains separate evaluator state and recomputes its
bounds.

The replay rejects partial/unsupported arguments and optimized Python mode.
Validation uses explicit runtime checks.
Coverage mutation tests reject unknown/extended leaf records, unsound
empty/analytic leaves, wrong roots, repeated children, boundary splits,
unreachable nodes, boolean node values, and duplicate JSON keys.
Stream checks reject missing configurations, partial/extra worker responses,
malformed integers, negative counts, and threshold violations.
Tree summaries must identify the expected component and certificate hash,
give exact nonnegative counts with consistent node and leaf partitions,
and report valid fingerprints and threshold-respecting extrema.
Changing any manifest input or its hash rejects the packet.

Agreement covers every per-leaf bound through an ordered SHA-256 fingerprint,
complete node-kind counts, extrema, and residual corner/vacuity counts.
Profile agreement includes family fingerprints and predicate partitions.
The strip compares all score fingerprints.
Generator-box agreement includes counts, minima, witnesses, and a 64-bit
modular diagnostic traversal fingerprint.

The generated [replay.json](replay.json) records input identities, platform,
process exit statuses/timings, result fingerprints, negative tests, and
agreement. PASS requires all seven pairs to complete and agree, all rejection
tests to pass, and the inputs to remain unchanged. The manifest identifies
input documents, code, and trees; the generated replay record includes the
manifest's hash and execution results.

## 4. Integer widths and overflow bounds

Python integers are unbounded. C++ evaluators require signed scores with
at least 63 value bits, indices with at least 31 value bits, and 64-bit
bitsets where used. The implementations check their required widths.

For the largest interval root, \(N_i\le78\), \(q=4096\), a conservative
bound on score, moment, and threshold intermediates is
\[
16\cdot79^3\bigl(156(3\cdot78q)+235q\bigr)<2^{51}<2^{63}-1.
\]
The strip envelope \(8\cdot21^3(9\cdot20+4)<2^{31}\) is smaller.
Degree-six profiles have \(m\le84\), \(s_i\le504\), and axis caps at most
six; their denominator-cleared margins fit below \(2^{30}\) in magnitude.
Generator-box distances are at most \((m-1)m(m-2)\le21924\).
No mathematical operation is performed on a negative-infinity sentinel.
