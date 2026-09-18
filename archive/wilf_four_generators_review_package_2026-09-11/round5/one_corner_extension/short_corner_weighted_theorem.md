# The weighted theorem for the short interior corner (2,1,1)

7 September 2026. This is a complete parameter-space certificate for a
specific interior-corner class. It is separate from the no-interior
certificate and does not establish arbitrary interior corners.

## The theorem established here

Let T be a finite lower ideal in N^3 whose only full-support minimal
excluded point is a permutation of (2,1,1). For positive weights a, put

\[
m=|T|,\qquad M=\max_{x\in T}a\cdot x,
\qquad D=3mM-4\sum_{x\in T}a\cdot x.
\]

Then

\[
\boxed{M\ge6a_{\min}\quad\Longrightarrow\quad
D\ge a_{\min}(m-1).}
\]

In particular, the same conclusion holds whenever m>=49. The proof
has three ingredients: an elementary planar decomposition, the prior
general lower-ideal phase estimate, and an exact certificate covering
all real parameters in a compact region.

## 1. A planar bound and compactness

Normalize a_min=1, and first orient the corner as (2,1,1), with weights
(A,B,C). Write S=A+B+C. Partition T into four disjoint sets:

1. y=0, translated by zero;
2. y>=1 and z=0, translated by (0,1,0);
3. x=0 and y,z>=1, translated by (0,1,1);
4. x=1 and y,z>=1, translated by (1,1,1).

Every remaining point would dominate (2,1,1), so these four sets cover
T. After the stated translations, each nonempty set is a finite planar
lower ideal. Their weight offsets are 0,B,B+C,S.

The weighted planar lower-ideal mean inequality is

\[
\operatorname{mean}(w)\le\frac23\max(w).
\]

Consequently a piece of offset h has mean at most
2(M-h)/3+h=2M/3+h/3. Averaging the four pieces gives

\[
\frac1m\sum_Ta\cdot x\le\frac{2M}{3}+\frac S3,
\qquad \frac Dm\ge\frac{M-4S}{3}.                 \tag{1}
\]

The same bound applies to each permutation of the short corner. Thus
M>=3+4S immediately proves D>=m.

Suppose D<m-1 and M>=6. Set v=1/M, s=S/M and kappa=D/(mM), so kappa<v.
The previously proved general phase estimate yields

\[
S<\frac{9M+1}{M-3}=9+\frac{28}{M-3}.
\]

Meanwhile (1) implies M<3+4S. Therefore

\[
M<39+\frac{112}{M-3},\qquad
M^2-42M+5<0,\qquad M<42.                          \tag{2}
\]

This compactness argument does not use the much weaker general
continuous one-corner gap. The coordinate unit vectors are present
because the short corner is minimal excluded.

Permute the normalized weights into (1,b,c), 1<=b<=c. The corner may
then be any of (2,1,1),(1,2,1),(1,1,2). Since the unit vectors belong
to T, c<=M. Thus any failure of the theorem must lie in

\[
1\le b\le c\le M,\qquad 6\le M\le42.             \tag{3}
\]

## 2. All-real-parameter certificate

The stored certificate proves the stronger assertion that for every
parameter in (3), for every corner permutation p above, and for every
nonempty ideal of the form

\[
T=U\setminus(p+\mathbb N^3),
\]

with U a no-interior lower ideal of clipped weighted height at most M,
one has m-D_M<=1. Here D_M uses M as a height allowance; the allowance
need not be attained.

Every ideal with exactly the full corner p has this form: remove p
from its minimal-excluded generator list to obtain U. The remaining
generators have support at most two. The converse can also yield an
ideal with no actual interior corner, which only enlarges the class
checked.

The no-interior structure theorem writes U as a central box and three
nested rectangular horns. Delete p+N^3 from each box or slice before
computing its cardinality, first moment, and maximum. The disjointness
and nested-rectangle recurrence remain valid after this deletion.

All box endpoints are integers in the common scale q=4096. For a
parameter box

\[
(B_0,C_0,H_0)\le q(b,c,M)\le(B_1,C_1,H_1),
\]

use weights l=(q,B_0,C_0) and height H_1 to enlarge feasibility, and
weights u=(q,B_1,C_1) with height H_0 to bound the additive score above.
For every retained point x,

\[
q[4(x_1+bx_2+cx_3)-3M+1]
\le4u\cdot x-3H_0+q.
\]

Since every retained coordinate is nonnegative, these inequalities
hold throughout the entire real box.

For a slice at outward axis i coordinate t with rectangle
[0,r] x [0,s], start with its usual size and moment. If
t>=p_i,r>=p_j,s>=p_k, subtract the corner rectangle
[p_j,r] x [p_k,s]. Its retained maximum for lower weights is

\[
l_it+\max\{l_j(p_j-1)+l_ks,\ l_jr+l_k(p_k-1)\}.
\]

Otherwise it is l_it+l_jr+l_ks. The central box is treated by the
corresponding three-dimensional subtraction; its retained maximum is
the largest of the three surviving faces. Exact integer formulas are
implemented in `interval_corner_bound.py` and
`corner_interval_worker.cpp`.

Each of the three corner permutations is maximized separately over
every central box and every nested horn sequence. A parameter box is
accepted when all three resulting integer bounds are at most q.
Alternatively, (1) accepts the whole box when

\[
H_0\ge3q+4(q+B_1+C_1).
\]

The complete certificate has:

| Item | Count |
|---|---:|
| Partition-tree nodes | 110,865 |
| DP leaves | 54,978 |
| Planar-bound leaves | 455 |
| Unresolved leaves | 0 |

The root is the closed box [1,42] x [1,42] x [6,42]. Each node is
clipped using b<=c<=M, then either accepted or divided into two closed
children sharing the split boundary. The verifier checks every child
and every clipping operation, so all real parameters and all boundary
cases are covered. The denominators describe real intervals; the
certificate is not a grid test.

The canonical artifact is `short_corner_complete_certificate.json`.
`verify_short_corner_tree.py` independently verifies complete tree
coverage and replays all recorded leaf bounds. A separate adversarial
audit independently reconstructs slice statistics from retained points
and uses explicit rectangle transitions to check all DP leaves.

## 3. Why cardinality 49 suffices

Suppose every point of T has total degree at most 5. The full simplex
Delta_5 has 56 points. The orthant above p=(2,1,1) removes four of them.

For j=1,2,3,4, the point q_j=(1,j,5-j) has total degree 6, so is outside
T, and does not dominate p. At least one of its three coordinate-plane
projections must be outside T. Otherwise no support-at-most-two minimal
excluded generator could lie below q_j, and p does not lie below it
either, contradicting q_j being outside.

These four triples of projections are pairwise disjoint, lie inside
Delta_5, and are disjoint from the removed orthant. They therefore
force at least four additional missing points. Hence

\[
|T|\le56-4-4=48.
\]

Thus m>=49 forces a point of total degree at least 6 and therefore
M>=6a_min. This proves the stated cardinality corollary without an
additional computational input.

## 4. Combining with the arithmetic low-height proof

The interval theorem alone deliberately leaves M<6a_min open; that
extension is false for arbitrary short-corner geometry. For example,
unit weights permit m=48,M=5,D=36, violating D>=m-1.

For genuine preferred Apéry ideals, the established short-corner
restriction gives at most two mixed minimal excluded points in each
coordinate plane. The separate report
`round5/interior_arithmetic/short_interior_cell_theorem.md` and its
low-height extension account for all 70,175 such ideals in Delta_5.
Every one of the 28,499 with m>=30 has an exact rational LP-dual
certificate proving D>=a_min(m-1) for all positive weights.

Consequently those low-height certificates, the present M>=6a_min
theorem, and the completed small-multiplicity verification together
prove Wilf for every genuine four-generator preferred Apéry ideal
whose full-support excluded corner is a permutation of (2,1,1).

The separate component certificates and analytic assumptions should be
reviewed together before publication. The in-session audits do not
constitute external peer review.

## Reproduction

```
g++ -std=c++17 -O3 corner_interval_worker.cpp -o corner_interval_worker
python3 short_corner_certificate.py --limit 200000 --worker ./corner_interval_worker
python3 verify_short_corner_tree.py
```

The Python programs use the standard library; the accelerated generator
and replay require a C++17 compiler. All mathematical arithmetic is
integer or rational. The recorded problem bounds keep all C++ values
well within signed 64-bit range; the independent checker audits this
range and uses a separate implementation of the DP.
