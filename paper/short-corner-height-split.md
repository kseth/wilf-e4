# The short-corner height and cardinality split

## Status and purpose

This note completes roadmap task B4.1. For a finite lower ideal whose only
full-support minimal exclusion is \(p=(2,1,1)\), it proves the sharp bound

\[
|T|\le2R^2-R+3,\qquad R=\max_{x\in T}|x|_1.
\tag{1}
\]

Consequently the B4 branch splits into \(H\ge6\) and a low-height range
\(H<6,\ 30\le m\le48\). The latter requires degree four or five, and degree
five whenever \(m\ge32\). All these statements are analytic; no shape
enumeration, residue filter, or weighted certificate is used.

This is a routing reduction, not a proof of the B4 target \(D_0\ge m-1\).
The separate [B4.2 compactness note](short-corner-compactness.md) proves the
high-height analytic reduction. The
[B4.3 profile specification](short-corner-profile-specification.md) proves
the low-height arithmetic restrictions and coverage. The weighted target
on the remaining high- and low-height domains is still open.

## 1. Hypotheses and normalization

Let \(T\subseteq\mathbb N^3\) be a finite lower ideal whose sole full-support
minimal excluded point is \(p=(2,1,1)\). A coordinate permutation puts every
B4 ideal in this form; it does not prescribe which weight is smallest.
Write

\[
m=|T|,\qquad
R=\max_{x\in T}|x|_1,\qquad
A=\min_i a_i,\qquad b_i=\frac{a_i}{A},\qquad
H=\max_{x\in T}b\mathbin\cdot x
\tag{2}
\]

for arbitrary positive weights \(a_i\). Thus \(b_i\ge1\), and

\[
R\le H.
\tag{3}
\]

The three immediate predecessors of \(p\) belong to \(T\) and have degree
three, so \(R\ge3\). For a preferred Apéry ideal, the
[foundations](foundations.md) give \(|T|=m\), with \(m\) the multiplicity,
and uniqueness of the full-support corner. The
[case partition](case-partition.md) supplies \(m\ge30\) in B4.

## 2. The sharp degree bound

### Theorem 2.1

Under the hypotheses above, (1) holds. More generally, if \(T\) has degree
at most an integer \(r\ge3\), then

\[
|T|\le2r^2-r+3.
\tag{4}
\]

For each \(r\ge3\), some such lower ideal attains (4) with degree exactly \(r\).

#### Proof of the upper bound

Put \(\Delta_r=\{x\in\mathbb N^3:|x|_1\le r\}\). Every point above the
excluded point \(p\) is excluded. Removing this orthant from \(\Delta_r\)
leaves

\[
|\Delta_r\setminus(p+\mathbb N^3)|
=\binom{r+3}{3}-\binom{r-1}{3}
=2r^2+2.
\tag{5}
\]

The second binomial coefficient is zero at \(r=3\).

For each \(j=1,\ldots,r-1\), consider the excluded point

\[
q_j=(1,j,r-j).
\]

It has degree \(r+1\) and does not dominate \(p\). Every excluded point
dominates a minimal excluded point: choose a minimal element of the
nonempty finite set of excluded points below it. Let \(c\le q_j\) be one.
Since \(c\ne p\), uniqueness of the full-support exclusion implies that
some coordinate of \(c\) is zero. Therefore \(c\) lies below at least one of

\[
(0,j,r-j),\qquad (1,0,r-j),\qquad (1,j,0),
\tag{6}
\]

and that projection is excluded too.

All points in (6) lie in \(\Delta_r\setminus(p+\mathbb N^3)\): their degrees
are at most \(r\) and each has a zero coordinate. Their three support patterns
are distinct because \(j,r-j\ge1\). Within any one support pattern, distinct
values of \(j\) give distinct points. Thus the \(r-1\) triples are pairwise
disjoint, forcing at least \(r-1\) additional omissions from (5).
It follows that

\[
|T|\le2r^2+2-(r-1)=2r^2-r+3.
\tag{7}
\]

Taking \(r=R\) proves (1). ∎

#### Sharpness

For an integer \(r\ge3\), define

\[
T_r=
\left\{(x,y,z)\in\mathbb N^3:
 x+y\le r,\ x+z\le r,\
 yz=0\ \text{or}\ y+z\le r-1
\right\}\setminus\bigl((2,1,1)+\mathbb N^3\bigr).
\tag{8}
\]

This is a finite lower ideal. An excluded point that violates one of the
three pair conditions remains excluded after deleting its unused coordinate.
It therefore cannot be a full-support minimal exclusion. The remaining
excluded points dominate \(p\), and all three immediate predecessors of
\(p\) satisfy (8). Hence \(p\) is the sole full-support minimal exclusion.

Every point of \(T_r\) has degree at most \(r\). If \(y,z>0\), exclusion of the
\(p\)-orthant gives \(x\le1\), and the third pair condition gives
\(y+z\le r-1\). If \(y=0\) or \(z=0\), one of the first two conditions
bounds the total degree. The point \((r,0,0)\) belongs, so the degree is
exactly \(r\).

Inside \(\Delta_r\), the first two pair conditions remove nothing. The third
removes exactly

\[
(0,j,r-j),\qquad j=1,\ldots,r-1.
\]

These points are disjoint from the removed \(p\)-orthant. The count in (7)
is therefore attained.

## 3. The B4 height split and its endpoints

### Corollary 3.1 (B4.1)

For a B4 preferred Apéry ideal, precisely one of the following height
alternatives holds:

- \(H\ge6\), which includes every \(m\ge49\);
- \(H<6\), in which case \(30\le m\le48\) and \(4\le R\le5\).

The necessary low-height ranges can be refined as follows:

| Multiplicity | Possible degree | Necessary height range |
|---|---|---|
| \(30\le m\le31\) | \(R=4\) or \(R=5\) | \(4\le H<6\), with \(H\ge R\) |
| \(32\le m\le48\) | \(R=5\) | \(5\le H<6\) |

#### Proof

If \(H<6\), (3) and integrality of \(R\) give \(R\le5\). Theorem 2.1 at
\(r=5\) gives \(m\le48\). Conversely \(m\ge49\) forces \(R\ge6\), hence
\(H\ge6\). At \(r=3\) and \(r=4\), the same theorem gives bounds \(18\) and
\(31\), respectively. Thus \(m\ge30\) forces \(R\ge4\), and \(m\ge32\)
forces \(R\ge5\). This proves all the stated ranges. ∎

The boundary \(H=6\) belongs to the high-height side. Degree at most five
does **not** imply \(H<6\): weights can raise the height without changing
the ideal. Some multiplicities \(30\le m\le48\) may therefore use the
high-height argument as well.

The threshold 49 cannot be lowered using these geometric hypotheses alone:
\(T_5\) from (8), with unit weights, has \(m=48\), \(R=H=5\).
This is an abstract lower ideal, not an assertion of semigroup realization.
Residue restrictions may further reduce the low-height range, but no
historical enumeration count is promoted into an analytic bound here.

## 4. Retained interface and provenance

The B4.2 reduction uses \(H\ge6\). B4.3 restricts its low-height profiles to
degree at most five and cardinality \(30\le m\le48\), using the refinements
in Corollary 3.1 if useful. This split alone asserts neither the weighted
deficit bound nor the validity of any residue filter or centroid dual;
B4.3 proves the filters separately.

The source argument and extremal family are in the historical
[short-corner cardinality theorem](../artifacts/wilf_four_generators_review_package_2026-09-11/round5/interior_arithmetic/short_corner_cardinality_theorem.md).
The projection step above is proved directly by minimal exclusions, avoiding
a dependency on pairwise projection closure. Novelty and upstream attribution
of the final retained estimates remain subject to the L3 literature refresh.

As bounded diagnostics only, the archived sharpness script and a separate
immediate-predecessor/corner check passed for \(r=3,\ldots,20\) on
2026-09-16. These checks are not proof dependencies; the arguments above
cover every integer \(r\ge3\).
