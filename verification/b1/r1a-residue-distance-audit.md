# R1a: residue-distance audit and replay

**Status date:** 2026-09-14

## Verdict and scope

The historical cyclic-residue implementation has been read in full, its
mathematical update has been reconstructed below, and a fresh complete replay
passes the B1.3-FV contract for all multiplicities \(20\le m\le29\).

The replay establishes the retained result through the residue-distance path.
It does **not** by itself supply an independent derivation of the semigroup
invariants. That derivation is now supplied by the separate
[R1b ordinary-membership audit](r1b-membership-audit.md), so the combined B1
computed lemma is complete under the repository trust policy.

The audited immutable source is

```text
artifacts/wilf_four_generators_review_package_2026-09-11/
round5/small_multiplicity/exhaust_small_multiplicity.cpp
```

with SHA-256

```text
bb86d9e78f2f3af7c9f0a916a5122b2af3a5f0d4cc290e403c0f23d393d098f3
```

The fail-closed runner is
[`replay_r1a.py`](replay_r1a.py), and the machine-readable result is
[`r1a-replay.json`](r1a-replay.json). The runner reads no stored result,
accepted-tuple list, checksum, or success flag.

## 1. Exact residue update

Fix a multiplicity \(m\). For a generator prefix, let \(d(r)\) be the least
attainable nonnegative integer congruent to \(r\pmod m\), or infinity if the
prefix does not generate that residue. Suppose a positive generator \(w\) is
adjoined. Put

\[
g=\gcd(m,w),\qquad L=\frac m g.
\]

Translation by \(w\) partitions \(\mathbb Z/m\mathbb Z\) into the \(g\)
cycles given by residues modulo \(g\), each of length \(L\). Every expression
using the new generator can be reordered with all copies of \(w\) last, so
the new exact distance is

\[
d'(r)=\min_{0\le k<L}\bigl(d(r-kw)+kw\bigr).
\tag{1}
\]

It is enough to take \(k<L\): replacing \(k\) by \(k+L\) returns to the same
residue and adds the positive amount \(Lw\).

The source initializes the output vector with \(d\), then performs relaxations

\[
d_{\mathrm{new}}(r+w)
\leftarrow
\min\bigl(d_{\mathrm{new}}(r+w),d_{\mathrm{new}}(r)+w\bigr)
\tag{2}
\]

in cyclic order, twice around each cycle. For a source vertex preceding its
target in the chosen cyclic listing, the required path of at most \(L-1\)
edges occurs in the first traversal. If it crosses the listing boundary, it
finishes in the second. Thus every candidate in (1) reaches its target. Every
relaxation in (2) appends a feasible copy of \(w\), so it can never
underestimate the true distance. The two inequalities prove that the update
equals (1).

The cycle representatives `0,...,g-1` are exact because addition by \(w\)
preserves the residue modulo \(g\) and acts transitively on each such class.
Starting with distance zero in residue zero and infinity elsewhere, induction
over \(a,b,c\) therefore gives the Apéry distances of
\(\langle m,a,b,c\rangle\).

As a deterministic schedule diagnostic, the runner separately simulates the
two traversals and compares them with (1) on every one-source basis vector for
every \(20\le m\le29\), every \(m<w\le m(m-2)\), and every source residue.
All 134,870 basis cases, comprising 6,883,916 edge relaxations, passed. This
diagnostic supports the preceding proof; it is not substituted for it.

## 2. Exhaustive tuple classification

For each \(m\), the source uses the inclusive bounds

\[
m+1\le a\le B_m-2,
\quad a+1\le b\le B_m-1,
\quad b+1\le c\le B_m,
\quad B_m=m(m-2).
\]

Hence it visits every element of \(\mathcal R_m\) exactly once. The total is

\[
\sum_{m=20}^{29}\binom{B_m-m}{3}=301{,}098{,}092.
\]

The rejection predicates are exact and disjoint in their execution order:

1. \(a\equiv0\pmod m\) is precisely \(a\in\langle m\rangle\);
2. a prefix distance no larger than \(b\) is precisely
   \(b\in\langle m,a\rangle\);
3. the analogous test is precisely \(c\in\langle m,a,b\rangle\); and
4. after these tests, total gcd greater than one is precisely failure to be a
   numerical semigroup.

For the distance tests, equality of residues makes the difference between the
candidate integer and the minimum representative a nonnegative multiple of
\(m\). Larger later generators cannot make an earlier smaller generator
redundant. Thus every remaining tuple is the unique increasing minimal
generator list of a four-generated numerical semigroup, and every such tuple
in the box remains.

The source checks internally, and the runner checks again from its output,
that the four rejection categories and the valid category sum to the exact
raw count for each multiplicity.

## 3. Wilf calculation

For a valid tuple, let

\[
M=\max_r d(r),qquad \Sigma=\sum_r d(r).
\]

The Apéry identities give

\[
C=M-m+1,qquad
g=\frac\Sigma m-\frac{m-1}{2},
\]

and therefore

\[
W_4=3C-4g
=\frac{3mM-4\Sigma-m(m-1)}m.
\tag{3}
\]

The source evaluates exactly the numerator in (3), rejects nondivisibility by
\(m\), and uses signed integer comparison for the result. It evaluates every
valid tuple in the generator box, which is stronger than required. The replay
runner rejects if the total negative count is nonzero; total count zero in
particular proves that no tuple in the required subdomain \(M\le B_m\) is
negative.

The `zero` counts, minima, witnesses, elapsed times, and FNV checksum are
diagnostics. Neither the theorem contract nor the runner requires strict
positivity or accepts on the basis of a checksum.

## 4. Arithmetic and failure audit

On the retained range,

\[
B_m\le783,qquad
d(r)\le(m-1)B_m\le21{,}924,qquad
\Sigma\le635{,}796.
\]

The infinity sentinel is \(10^9\), and adding any in-range generator to it
remains below the signed 32-bit maximum. Finite residue distances and maxima
therefore fit safely in the source's `int`; the sum and Wilf numerator use
signed 64-bit integers. Raw and category counts use unsigned 64-bit integers.
Overflow of the unsigned FNV accumulator is defined by C++ and affects only a
diagnostic checksum.

The historical executable reports counts rather than exiting on a negative
Wilf number. The new runner supplies the fail-closed boundary: it rejects a
compiler or program error, compiler warnings under `-Werror`, stderr output,
malformed or extra records, an unexpected schema or multiplicity, incorrect
inclusive bounds, a failed count partition, malformed diagnostics, or any
negative count or minimum. It writes a failure record and returns nonzero on
any such condition.

The replay compiles in a fresh temporary directory with

```sh
/usr/bin/g++ -O3 -std=c++17 -Wall -Wextra -Wpedantic -Werror \
  artifacts/wilf_four_generators_review_package_2026-09-11/round5/\
small_multiplicity/exhaust_small_multiplicity.cpp \
  -o <temporary-directory>/exhaust_small_multiplicity
```

and runs the resulting temporary executable on the explicit endpoints 20 and
29. No binary or compiler cache is retained in the repository.

## 5. Fresh replay result

The complete cache-free replay produced:

| \(m\) | Raw triples | Valid semigroups | \(M\le B_m\) | Bounded minimum \(W_4\) | Negative |
|---:|---:|---:|---:|---:|---:|
| 20 | 6,492,980 | 3,443,090 | 162,507 | 31 | 0 |
| 21 | 8,930,376 | 5,062,582 | 245,781 | 35 | 0 |
| 22 | 12,085,216 | 6,572,752 | 308,356 | 32 | 0 |
| 23 | 16,117,020 | 9,396,905 | 469,286 | 25 | 0 |
| 24 | 21,210,504 | 11,916,965 | 457,322 | 24 | 0 |
| 25 | 27,578,100 | 16,773,245 | 734,594 | 20 | 0 |
| 26 | 35,462,596 | 20,415,122 | 828,230 | 32 | 0 |
| 27 | 45,139,896 | 28,032,547 | 1,098,827 | 28 | 0 |
| 28 | 56,921,900 | 33,786,843 | 1,201,133 | 45 | 0 |
| 29 | 71,159,504 | 45,318,978 | 1,820,956 | 59 | 0 |
| **Total** | **301,098,092** | **180,719,029** | **7,326,992** | — | **0** |

There were zero unresolved and zero unsupported cases. The full environment,
commands, source and contract hashes, per-multiplicity records, process exit
statuses, and exact timestamps are in `r1a-replay.json`. A read-only comparison
after the run found every nontiming field identical to the archived record;
that agreement is a regression diagnostic, not a replay input.

## 6. Trust boundary and independent completion

R1a trusts the mathematical arguments in the B1.2 conductor reduction and
B1.3 specification, the inspected C++ source, the fail-closed Python runner,
the C++17 and Python language implementations, the compiler, operating system,
and hardware. It does not trust historical output.

R1a alone is not the independent check required by V0. The completed
[R1b path](r1b-membership-audit.md) independently generates the tuple domain
and calculates membership, conductor, genus, and \(W_4\) without importing
the residue distances, classifications, accepted tuple list, or success
result from this replay. The two paths together complete the B1 finite lemma
under the repository policy.
