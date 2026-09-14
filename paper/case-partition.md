# Exhaustive case partition

## Status and purpose

This note proves only that the branches in the proposed four-generator proof
cover every numerical semigroup. It contains no Wilf estimate and no
computer-assisted assertion. The analytic or computational theorem assigned
to each branch remains a separate obligation.

The only imported facts are the preferred Apéry construction and the
uniqueness of a full-support corner, proved in
[`foundations.md`](foundations.md).

## 1. Notation

Let

\[
S=\langle m,a_1,a_2,a_3\rangle
\]

be minimally four-generated, with \(m\) its multiplicity. Let
\(T\subseteq\mathbb N^3\) be its preferred Apéry lower ideal. Put

\[
a=(a_1,a_2,a_3),\qquad A=\min_i a_i,\qquad
M=\max_{x\in T}a\cdot x,\qquad
H=\frac{M}{A},\qquad
R=\max_{x\in T}|x|_1.
\]

A *full-support corner* is a minimal excluded point
\(p\in\mathbb N^3\setminus T\) with \(p_1,p_2,p_3>0\). By Proposition 5.1 of
the foundational note, \(T\) has at most one such corner.

## 2. Partition lemma

### Proposition 2.1

Exactly one of the following cases holds:

| Case | Routing condition |
|---|---|
| B1 via L1 | \(m\le19\) |
| B1 via B1.1--B1.3 | \(20\le m\le29\) |
| B2 | \(m\ge30\), with no full-support corner |
| B3 | \(m\ge30\), with full-support corner \(p=(1,1,1)\) |
| B4 | \(m\ge30\), with \(p\) a coordinate permutation of \((2,1,1)\) |
| B5 | \(m\ge30\), with \(\lvert p\rvert_1\ge5\) and \(R\le6\) |
| B6 | \(m\ge30\), with \(\lvert p\rvert_1\ge5\) and \(R\ge7\) |

In B5 one automatically has

\[
5\le |p|_1\le7.
\]

In B6 one automatically has

\[
H\ge R\ge7.
\]

#### Proof

First split into \(m\le29\) and \(m\ge30\). The former range divides into
\(m\le19\), handled by L1, and \(20\le m\le29\), handled by the B1.1--B1.2
reduction followed by the B1.3 verification. Now suppose \(m\ge30\).

If \(T\) has no full-support corner, we are in B2. Otherwise the foundational
corner lemma gives a unique full-support corner
\(p=(p_1,p_2,p_3)\). Its coordinates are positive integers, so
\(|p|_1\ge3\).

If \(|p|_1=3\), all three coordinates equal one, giving B3. If
\(|p|_1=4\), exactly one coordinate equals two and the other two equal one,
giving B4. The only remaining possibility is \(|p|_1\ge5\).

Because \(R\) is an integer, exactly one of \(R\le6\) and \(R\ge7\) holds.
These alternatives give B5 and B6.

It remains to verify the two additional bounds. In B5, minimal exclusion and
full support give \(p-e_i\in T\) for every \(i\). Hence

\[
|p|_1-1=|p-e_i|_1\le R\le6,
\]

so \(|p|_1\le7\).

In B6, choose \(x\in T\) with \(|x|_1=R\). Since every \(a_i\ge A\),

\[
M\ge a\cdot x\ge A|x|_1=AR.
\]

Dividing by \(A>0\) gives \(H\ge R\ge7\).

Every step above is a split into disjoint alternatives, so the seven rows are
both exhaustive and mutually exclusive. ∎

## 3. Branching diagram

```text
all minimally four-generated semigroups
├── m <= 19 ............................................. B1 via L1
├── 20 <= m <= 29 ............................ B1 via B1.1--B1.3
└── m >= 30
    ├── no full-support corner ................................. B2
    └── unique full-support corner p
        ├── |p|_1 = 3, hence p = (1,1,1) ....................... B3
        ├── |p|_1 = 4, hence p ~ (2,1,1) ....................... B4
        └── |p|_1 >= 5
            ├── R <= 6, hence 5 <= |p|_1 <= 7 .................. B5
            └── R >= 7, hence H >= R >= 7 ...................... B6
```

Here \(p\sim(2,1,1)\) means equality after a coordinate permutation.

## 4. Scope boundary

Proposition 2.1 establishes only the routing conditions. Some retained branch
theorems use further consequences of being a genuine preferred Apéry ideal:

- B3 uses the [six-maxima entry lemma](six-maxima-entry.md);
- B4 uses additional residue restrictions in its low-height subcase; and
- B5 uses plane-corner and exposed-surface restrictions.

Those statements are branch-entry lemmas, not extra partition assumptions.
They must be proved before the corresponding branch theorem is invoked.

The routing cells above are mutually exclusive, but the applicability domains
of the branch theorems need not be. In particular, \(R\le6\) does not imply
\(H<7\); a semigroup routed to B5 may also satisfy the high-height hypothesis
used by the B6 theorem. Assigning it to B5 preserves a disjoint proof
organization.

## 5. Retained interface

The remainder of the proof may cite Proposition 2.1 for the following:

1. it is enough to prove the result through L1, B1.1--B1.3, and B2--B6;
2. the B5 search may assume \(5\le|p|_1\le7\); and
3. the B6 argument may assume \(H\ge7\).

No finite verification is needed for any of these reductions.
