# Independent audit of the finite exhaustive checks

Audit date: 9 September 2026. Auditor: `audit_enumerations` agent, Round 6.

## Verdict and exact scope

**PASS: the source-code audit found no gap in either finite enumeration,
and both new full canonical reruns passed.** All four C++ programs were
freshly compiled and run on their complete stated ranges. Every recorded
integer field and checksum matched the historical results.

The finite computations themselves are unconditional statements about
the following inclusive generator boxes, with `B=m(m-2)`:

1. For every `20 <= m <= 29`, every minimally four-generated numerical
   semigroup `<m,a,b,c>` with `m<a<b<c<=B` has positive Wilf number.
2. For every `30 <= m <= 48`, the same conclusion holds for every such
   tuple satisfying at least one of
   `2a+b+c=0`, `a+2b+c=0`, `a+b+2c=0` modulo `m`.

Extending either conclusion to all generator sizes at those multiplicities
**depends on the separately audited implication**

\[
W_4(S)<0\Longrightarrow M=\max\operatorname{Ap}(S,m)\le m(m-2).
\tag{CR}
\]

This audit does not independently establish (CR). Under (CR), the resulting
global conclusion is nonnegativity, `W_4>=0`, not strict positivity. An
equality case outside the enumerated boxes would not contradict (CR).
The positive minima in the records are box minima only.

## Materials inspected

All four C++ source files were read in full:

- `round5/small_multiplicity/exhaust_small_multiplicity.cpp`
- `round5/small_multiplicity/independent_membership_check.cpp`
- `round5/short_corner_small_m/exhaust_p211_relations.cpp`
- `round5/short_corner_small_m/independent_p211_membership.cpp`

Both canonical Python verifiers and both explanatory theorem notes were
also read in full. Historical files have not been changed by this audit.

## Exhaustive domain and minimality

In the first domain the loops are exactly
`m+1<=a<=B-2`, `a+1<=b<=B-1`, `b+1<=c<=B`. Thus every increasing triple
from the `B-m` allowed integers appears once, including the right endpoint.
Its size is `choose(B-m,3)`.

A generator `a` is redundant precisely when `a` is a multiple of `m`.
After excluding that case, `b` is redundant precisely when it belongs to
`<m,a>`, and `c` is redundant precisely when it belongs to `<m,a,b>`.
Larger later generators cannot represent any smaller positive earlier
generator. These ascending-prefix tests therefore characterize minimality
of the full ordered generating set; they do not discard a genuinely
minimal four-generator tuple.

The condition `gcd(m,a,b,c)=1` is exactly what makes this finitely generated
positive submonoid a numerical semigroup. Every skipped tuple is counted
in precisely one of the three redundancy categories or the nontrivial-gcd
category; every other tuple is counted as valid. Both programs verify that
these categories partition the full count.

For the short-corner domain, fix `a,b` and reduce `c` modulo `m`. The first
program solves the first two linear congruences directly. For `2c=-a-b`,
it uses the inverse `(m+1)/2` when `m` is odd; when `m` is even it returns
no solution for odd right-hand side and the two solutions separated by
`m/2` for even right-hand side. The resulting residue list is sorted and
deduplicated. The second program independently tests every residue
`0,...,m-1` against all three congruences.

For each allowed residue `r`, the number of integers `b<c<=B` is

\[
\lfloor(B-r)/m\rfloor-\lfloor(b-r)/m\rfloor.
\]

Both numerators are positive in the actual loops, so C++ integer division
has the required floor meaning. The loops over `q=floor(b/m),...,floor(B/m)`
and sorted `r`, followed by the exact endpoint tests on `c=qm+r`, enumerate
every allowed `c` once in increasing order. There is no congruence heuristic
or sampling step. The canonical verifier also compares the explicit solver
against every possible residue triple for each `m=30,...,48`.

## Exactness of the residue-distance algorithm

For a generator prefix, let `d(r)` be its least nonnegative attainable
integer in residue `r`, or infinity. Adding a positive generator `w` gives

\[
d'(r)=\min_{0\le k<L}\bigl(d(r-kw)+kw\bigr),
\qquad L=m/\gcd(m,w).
\]

Taking `k>=L` adds a positive full cycle and cannot improve the minimum.
Translation by `w mod m` partitions the residues into cycles of length `L`.
The starts `0,...,gcd(m,w)-1` enumerate exactly those cycles. Two forward
passes contain a run of at least `L-1` following edges after every possible
initial source vertex, and hence propagate every candidate in the displayed
minimum. Every relaxation is a feasible path; therefore it cannot produce
a value below the true minimum. The update is exact in both directions.

The redundancy test `d(v mod m)<=v` is equivalent to membership: the
difference is a nonnegative multiple of `m`. Total gcd one ensures that
every final distance is finite, which the program also checks explicitly.

Writing `A=sum_r d(r)` and `M=max_r d(r)`, the usual residue count gives
`g=A/m-(m-1)/2` and `C=M-m+1`. Consequently

\[
W_4=4(C-g)-C
=\frac{3mM-4A-m(m-1)}m.
\]

The program uses exactly this expression and checks numerator divisibility
by `m`. It checks the Wilf number for every valid tuple in the box, including
those with `M>B`.

## Independent integer-membership algorithm

The second program computes ordinary membership on `0,...,B` in increasing
integer order. At each new generator `w`, the recurrence is prefix
membership or membership of `n-w` in the enlarged semigroup. All entries
are recomputed in increasing order, so no stale array entry can affect the
result. The bit array is reset for each generator prefix.

Its only extra pruning is the exact equivalence

\[
[B-m+1,B]\subseteq S\quad\Longleftrightarrow\quad M\le B.
\]

The interval contains the largest integer at most `B` in each residue class.
If a class has any semigroup representative at most `B`, closure under
`+m` puts its interval representative in `S`. Conversely, presence of the
interval representative supplies such a representative. These two facts
prove the equivalence.

To test the interval, membership in `<m,a,b,c>` is the union, over all
nonnegative multiples `kc<=B`, of membership in `<m,a,b>` translated by
`kc`. The bit-window code computes exactly this union. A negative window
start is handled by zero padding; no membership below zero is introduced.

Once the last `m` integers are present, closure under `+m` proves that every
larger integer is also present. Counting absent integers up to `B` therefore
gives the full genus, and the last absent integer gives the conductor. The
second program independently evaluates `W_4=3C-4g`. It checks every tuple
with `M<=B`; using it to discard `M>B` as a possible negative case requires
(CR). The first program has no such pruning.

## Integer and memory safety within the audited ranges

Throughout these computations `m<=48` and `B<=2208`. Every finite shortest
residue path can be taken simple, so its optimum is at most
`(m-1)B<=103776`. All finite transient relaxations are also far below the
infinity sentinel `10^9`. Adding a generator to that sentinel remains below
`10^9+2208`, well below the signed 32-bit maximum; infinity cannot spuriously
decrease. The moment sum and Wilf numerator use signed 64-bit arithmetic.

All count totals and checksums use unsigned 64-bit integers. The FNV checksum
wraparound is defined unsigned arithmetic and serves only as a replay
diagnostic. It is not used to justify inclusion, pruning, or the inequality.

The bit-window width is at most 48, so all shifts are below 64. A negative
start that reaches the left-shift branch has `-start<width`. For a positive
start, the offset branch excludes a shift by 64. The allocated bit array
includes two padding words; its two-word window accesses remain within the
allocation. All array indices in the membership recurrences have explicit
nonnegativity guards and are at most `B`.

## Why an actual `(2,1,1)` corner implies the congruence condition

This implication needs only a lower ideal `T` containing exactly one
representative of each residue modulo `m`. Let `p` be a full-support minimal
excluded exponent, and let `q in T` have the same residue. If `q_i>0` for
some coordinate, then `q-e_i` and `p-e_i` both lie in `T`, the first by
downward closure and the second by minimal exclusion. They have the same
residue, so uniqueness forces `q-e_i=p-e_i`, giving `q=p`, a contradiction.
Thus `q=0`, and `a dot p=0 mod m`.

For a coordinate permutation of `(2,1,1)`, this is one of the three tested
congruences. The enumeration deliberately checks the larger congruence
union; it never assumes that satisfying a congruence determines an actual
Apéry corner.

## Fresh replay records

The helper `round6/audit_enumerations_data/replay_with_records.py` invokes
the original, unchanged canonical verifier with `--rerun`. Its only wrapper
around `subprocess.run` saves completed enumeration stdout to a new file.
The canonical verifier still compiles the original C++17 sources, checks
their exit codes, compares every fresh record field except elapsed time to
the historical record, and compares the two algorithms with each other.
Compiler flags are `-O3 -std=c++17 -Wall -Wextra -pedantic`.

Fresh results and source hashes are retained in the same directory. The
recorded `compiled_and_reran_this_invocation` flag is true. No historical
certificate was overwritten.

The small-multiplicity replay covers 301,098,092 sorted triples,
180,719,029 minimally four-generated numerical semigroups, and 7,326,992
cases with `M<=B`. Both complete runs agree; there are zero negative Wilf
numbers. The first run also proves zero equality cases inside the entire
generator box; the second confirms this over `M<=B`.

The short-corner replay covers 803,005,632 congruence-union triples,
508,199,476 minimally four-generated numerical semigroups, and 14,416,025
cases with `M<=B`. Both complete runs agree, with zero negative Wilf numbers
and zero equality cases in their respective checked domains.

| Fresh program run | Multiplicity range | Sum of per-m elapsed seconds |
|---|---|---:|
| `exhaust_small_multiplicity` | 20 through 29 | 19.156 |
| `independent_membership_check` | 20 through 29 | 7.916 |
| `exhaust_p211_relations` | 30 through 48 | 89.654 |
| `independent_p211_membership` | 30 through 48 | 62.552 |

These times describe this rerun environment; the two range verifiers were
started concurrently and the timings are not proof inputs. Their two
canonical verifier processes both returned exit code zero.

## Limits of this audit

No new unbounded mathematical inequality is proved by these replays.
Neither source inspection, agreement of two implementations, nor a checksum
supplies (CR). Subject to its independent proof, these computations remove
all multiplicities 20 through 29, and remove the short-corner congruence union
at multiplicities 30 through 48. They do not remove unrestricted corners at
higher multiplicities and do not prove unrestricted four-generator Wilf.
