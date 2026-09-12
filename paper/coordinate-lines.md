# Coordinate-line calculus for finite lower ideals

## Status and purpose

This note completes task G2. It proves the coordinate-line identities used
throughout the proposed four-generator proof, including their weighted and
centroid forms. The arguments are elementary and contain no
computer-assisted assertion.

Except for the Apéry specialization in Section 3, the results apply to every
nonempty finite lower ideal \(T\subseteq\mathbb N^3\).

The nonnegative specialization of the line-slack identity is the line-sum
form of Zhai's weighted inequality for finite downsets; see the
[literature survey](../literature/survey.md#41-apéry-sets-and-preferred-factorizations).
The vector bookkeeping and endpoint-upgrade forms needed later are proved
explicitly below.

## 1. Lines and conventions

Put

\[
m=|T|,\qquad s=\sum_{x\in T}x,
\]

and write \(s_i\) for the \(i\)-th coordinate of \(s\). For
\(i\in\{1,2,3\}\), let

\[
\pi_i:\mathbb N^3\longrightarrow\mathbb N^2
\]

delete coordinate \(i\), and let
\(\iota_i:\mathbb N^2\longrightarrow\mathbb N^3\) insert a zero in that
coordinate.

For \(y\in\pi_i(T)\), define

\[
h_i(y)=\max\{k\in\mathbb N:\iota_i(y)+ke_i\in T\}.
\]

The corresponding nonempty coordinate line is

\[
\ell_{i,y}
=\{\iota_i(y)+ke_i:0\le k\le h_i(y)\}.
\]

Its length and top are

\[
L_{i,y}=h_i(y)+1,\qquad
t_{i,y}=\iota_i(y)+h_i(y)e_i.
\]

Lower closure is exactly what makes every fiber the displayed initial
interval. Let

\[
\mathcal L_i=\{\ell_{i,y}:y\in\pi_i(T)\},\qquad
\mathcal L=\mathcal L_1\sqcup\mathcal L_2\sqcup\mathcal L_3.
\]

The last union is an indexed disjoint union. Lines from different directions
are different summands even when they intersect as subsets of \(T\).
Length-one fibers are included, and a line top need not be globally maximal
in \(T\).

Finally, define the total projection count

\[
P(T)=\sum_{i=1}^3|\pi_i(T)|=|\mathcal L|.
\]

## 2. Counting and line-top identities

### Proposition 2.1

For each coordinate direction \(i\),

\[
|\mathcal L_i|=|\pi_i(T)|,\qquad
\sum_{\ell\in\mathcal L_i}L_\ell=m,
\tag{1}
\]

\[
\sum_{\ell\in\mathcal L_i}\binom{L_\ell}{2}=s_i,
\tag{2}
\]

and

\[
\sum_{\ell\in\mathcal L_i}L_\ell t_\ell=s+s_i e_i.
\tag{3}
\]

Consequently, across all three indexed line families,

\[
|\mathcal L|=P(T),\qquad
\boxed{\sum_{\ell\in\mathcal L}L_\ell=3m},
\tag{4}
\]

\[
\boxed{\sum_{\ell\in\mathcal L}L_\ell t_\ell=4s}.
\tag{5}
\]

#### Proof

The lines in \(\mathcal L_i\) are indexed by \(\pi_i(T)\) and partition
\(T\), proving (1).

On a line of length \(L\), coordinate \(i\) takes the values
\(0,1,\ldots,L-1\). Its sum on that line is therefore
\(\binom L2\). Summing the \(i\)-th coordinate over the partition proves
(2).

For \(j\ne i\), coordinate \(j\) is constant on each \(i\)-line, so

\[
\sum_{\ell\in\mathcal L_i}L_\ell(t_\ell)_j=s_j.
\]

In coordinate \(i\), the contribution of a line of length \(L\) is

\[
L(L-1)=2\binom L2.
\]

Equation (2) now shows that the \(i\)-th coordinate of the left side of (3)
is \(2s_i\), proving (3).

Summing (1) over the three directions proves (4). Summing (3) gives

\[
3s+\sum_{i=1}^3s_i e_i=4s,
\]

which is (5). \(\square\)

### Corollary 2.2 (axis endpoints)

Let \(q_i=\max_{x\in T}x_i\). Then \(q_i e_i\in T\), and it is the top of
the coordinate-\(i\) axis line. If \(e_i\in T\), then \(q_i\ge1\).

#### Proof

Choose \(x\in T\) with \(x_i=q_i\). Since \(q_i e_i\le x\), lower closure
gives \(q_i e_i\in T\). Maximality of \(q_i\) makes it the axis-line top.
\(\square\)

## 3. Weighted deficits

Let \(\omega\in\mathbb R^3\) and \(Q\in\mathbb R\), and define

\[
D_T(\omega,Q)=3mQ-4\omega\mathbin\cdot s.
\]

### Proposition 3.1 (line-slack identity)

\[
\boxed{
D_T(\omega,Q)
=\sum_{\ell\in\mathcal L}
L_\ell\bigl(Q-\omega\mathbin\cdot t_\ell\bigr).
}
\tag{6}
\]

In particular, if

\[
Q\ge\max_{x\in T}\omega\mathbin\cdot x,
\]

then every summand in (6) is nonnegative and \(D_T(\omega,Q)\ge0\).

#### Proof

Expand the right side and apply (4) and (5):

\[
Q\sum_\ell L_\ell
-\omega\mathbin\cdot\sum_\ell L_\ell t_\ell
=3mQ-4\omega\mathbin\cdot s.
\]

Every line top belongs to \(T\), which proves the last assertion.
\(\square\)

For the preferred Apéry ideal in
[`foundations.md`](foundations.md), write

\[
a=(a_1,a_2,a_3),\quad
M=\max_{x\in T}a\mathbin\cdot x,\quad
A=\min_i a_i,\quad b=\frac aA,\quad H=\frac MA.
\]

The two relevant specializations are

\[
D=D_T(a,M)
=\sum_\ell L_\ell(M-a\mathbin\cdot t_\ell),
\tag{7}
\]

\[
D_0=D_T(b,H)
=\sum_\ell L_\ell(H-b\mathbin\cdot t_\ell).
\tag{8}
\]

In particular, \(D=AD_0\).

Combining (7) with the exact moment identity gives the line form

\[
\boxed{
mW_4(S)
=\sum_\ell L_\ell(M-a\mathbin\cdot t_\ell)-m(m-1).
}
\tag{9}
\]

### Corollary 3.2 (predecessor lines)

Let \(p\) be a minimal point of
\(\mathbb N^3\setminus T\), let
\(\omega\in\mathbb R_{>0}^3\), and suppose

\[
Q\ge\max_{x\in T}\omega\mathbin\cdot x,
\qquad
\omega\mathbin\cdot p\le Q.
\]

Then

\[
D_T(\omega,Q)\ge\omega\mathbin\cdot p.
\tag{10}
\]

#### Proof

If \(p_i>0\), minimal exclusion gives \(p-e_i\in T\). It is the top of its
coordinate-\(i\) line: its successor \(p\) is excluded, and lower closure
rules out any point farther along that line. The line has length \(p_i\).

These predecessor lines belong to different indexed direction families.
Their contribution to (6) is

\[
\begin{aligned}
\sum_{i:p_i>0}
p_i\bigl(Q-\omega\mathbin\cdot(p-e_i)\bigr)
&=|p|_1\bigl(Q-\omega\mathbin\cdot p\bigr)
  +\omega\mathbin\cdot p\\
&\ge\omega\mathbin\cdot p.
\end{aligned}
\]

All remaining summands in (6) are nonnegative. \(\square\)

## 4. Replacing line tops by dominating points

The vector identity (5) also gives the common analytic core of the local
centroid construction.

### Proposition 4.1 (endpoint upgrade)

For every \(\ell\in\mathcal L\), choose any \(u_\ell\in T\) satisfying
\(u_\ell\ge t_\ell\) coordinatewise, and put

\[
z=\frac1{3m}\sum_{\ell\in\mathcal L}L_\ell u_\ell.
\]

Then \(z\in\operatorname{conv}(T)\), and

\[
r:=3mz-4s
=\sum_{\ell\in\mathcal L}L_\ell(u_\ell-t_\ell)
\ge0
\tag{11}
\]

coordinatewise. Moreover, if \(b_i\ge1\) for every \(i\) and

\[
H\ge\max_{x\in T}b\mathbin\cdot x,
\]

then

\[
\boxed{
D_T(b,H)\ge b\mathbin\cdot r\ge|r|_1
=\sum_\ell L_\ell\bigl(|u_\ell|_1-|t_\ell|_1\bigr).
}
\tag{12}
\]

#### Proof

Equation (4) shows that the nonnegative coefficients
\(L_\ell/(3m)\) sum to one, so \(z\) is a convex combination of points of
\(T\). Equation (11) follows from (5), and every vector
\(u_\ell-t_\ell\) is coordinatewise nonnegative.

Because \(z\in\operatorname{conv}(T)\), one has
\(b\cdot z\le H\). Hence

\[
D_T(b,H)
=3m(H-b\mathbin\cdot z)+b\mathbin\cdot r
\ge b\mathbin\cdot r
\ge|r|_1,
\]

where the last inequality uses \(b_i\ge1\) and \(r_i\ge0\).
Taking coordinate sums in (11) proves the final equality in (12).
\(\square\)

Taking \(u_\ell=t_\ell\) shows directly that

\[
\frac{4s}{3m}
=\frac1{3m}\sum_\ell L_\ell t_\ell
\in\operatorname{conv}(T),
\]

and recovers the nonnegative weighted-deficit baseline. Later applications
obtain positive surplus by moving selected line tops upward inside \(T\).

## 5. Scope

Propositions 2.1, 3.1, and 4.1 use only that \(T\) is a nonempty finite lower
ideal. Corollary 3.2 additionally uses minimal exclusion. No residue,
full-corner, degree, or semigroup hypothesis enters these statements.
