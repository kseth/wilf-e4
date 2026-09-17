# Residual high-height proof and finite contracts

## Scope and status

This note selects one route for B6: an exact four-allowance strip,
a finite-to-continuous transfer, a compactness implication, and an exact
closed-box interval certificate. Each computational premise is stated
independently of a saved run. Evidence is recorded separately.
The target for a genuine residual Apéry ideal is
\[
D_0\ge m-\frac{29}{10}\qquad(R\ge7,\ |p|_1\ge5).
\]
The inputs are the [phase/thickening theorem](phase-and-thickening.md)
and [central-box/three-horn theorem](central-box-horns.md).

## 1. B6.1: finite-strip specification

For \(R\in\{18,19,20,21\}\), let \(T\) be any nonempty finite lower ideal
in \(\mathbb N^3\), of degree at most \(R\), with at most one full-support
minimal excluded point. Write
\[
m_T=|T|,\qquad D_R(T)=3Rm_T-4\sum_{x\in T}|x|_1.
\]

> **B6-strip-FV.** For every such \(R,T\),
> \[
> D_R(T)\ge4m_T.
> \tag{S}
> \]
> Missing coordinate units and maximum degree strictly below \(R\)
> are allowed. The empty ideal satisfies (S) by equality.

### Complete corner and support coverage

An actual positive minimal excluded point \(p\) has
\(p-e_i\in T\); therefore \(|p|_1\le R+1\).
Delete its orthant generator from the complement to obtain a finite
no-full-corner ideal \(U\). Pure-axis exclusions remain, and clipping
by a positive \(p\) leaves all axis points unchanged. Thus
\[
T=U\setminus(p+\mathbb N^3),\qquad
0\le\max_Ux_i=\max_Tx_i\le R.
\tag{1}
\]
If no such corner exists, set \(U=T\) and \(p=(1,1,R-1)\).
This corner is inactive on the degree-\(R\) simplex.
Unit weights and the score are symmetric, so enumerate exactly
\[
1\le p_1\le p_2\le p_3,\qquad |p|_1\le R+1.
\tag{2}
\]
Minimality of the enumerated corner is not required by the evaluator;
allowing inactive/nonminimal corners only enlarges its covered class.
Zero axis caps and singleton ideals must not be skipped.

### Exact section and center scores

Put \(f_R(x)=4|x|_1+4-3R\).
For direction \(i\), level \(t\), and transverse caps \(u,v\), let
\[
A_i(t,u,v)=
\{x:x_i=t,\ 0\le x_j\le u,\ 0\le x_k\le v,\ x\not\ge p\},
\qquad C_i(t,u,v)=\sum_{A_i(t,u,v)}f_R(x).
\]
Call a section feasible if its *retained* maximum degree is at most \(R\).
The uncut upper corner need not be retained. Its axis point survives;
therefore no nonempty section can occur beyond level \(R\).
The exact nested-rectangle upper bound is
\[
F_i(R+1;b,c)=0,\qquad
F_i(t;b,c)=
\max\left(0,\ 
\max_{\substack{0\le u\le b,\ 0\le v\le c\\A_i(t,u,v)\ {\rm feasible}}}
\{C_i(t,u,v)+F_i(t+1;u,v)\}\right).
\tag{3}
\]
The zero option terminates a horn; lower closure prevents restarting it.
Backward induction proves (3) for every nested horn in the structural
decomposition. Prefix maxima are an equivalent implementation of the
inner maximum, since a proper subrectangle reduces at least one cap.

For a central cap \(c\in\{0,\ldots,R\}^3\), put
\(A(c)=[0,c]\setminus(p+\mathbb N^3)\), and require its retained
maximum degree to be at most \(R\). Define
\[
V_{R,p}=\max_{c\ {\rm feasible}}
\left(\sum_{x\in A(c)}f_R(x)
+\sum_iF_i(c_i+1;c_j,c_k)\right).
\tag{4}
\]
The center and horns are disjoint before and after clipping. The
structural theorem and (3) give
\[
4|T|-D_R(T)=\sum_T f_R(x)\le V_{R,p}.
\tag{5}
\]
Every central anchored box retains the origin, so the maximum is nonempty.
Consequently the finite per-configuration predicate
\[
V_{R,p}\le0\quad\text{for all (2) and all four }R
\tag{6}
\]
implies (S). This computes upper bounds, not a list of all ideals.

Statistics may be computed either by full-box count/moment subtraction
and surviving-face maxima, or by independent retained-point sums.
The moment for an inclusive box \([a,b]\) is
\(\sum_B|x|_1=|B|\sum_i(a_i+b_i)/2\); use twice moments to keep
intermediate arithmetic integral. Inactive corners are covered by
the same formulas. Singleton score \(4-3R\) is a regression diagnostic,
not the acceptance predicate.

### Arithmetic and completeness

Here \(n=R+1\le22\). All supports lie in \([0,R]^3\).
A conservative bound for signed score, twice-moment, and disjoint-piece
intermediates is
\[
8n^3(9R+4)<2^{31}.
\tag{7}
\]
The implementations must use signed values with at least 63 value bits
and indices with at least 31 value bits, reject unsupported/partial modes,
enumerate all four allowances and every corner (2), and fail on any
positive bound. Stored outputs, counts, or checksums do not establish (6).
The selected audit requires two fresh independent complete implementations.

The four allowances are precisely those arising from translations of a
mesh of size \(1/21\) in the unit simplex; their necessity and the
continuous consequence are proved next, conditionally on (S).
