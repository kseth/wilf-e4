# An integer-slack target sufficient for four-generator Wilf

Let a minimally four-generated numerical semigroup have multiplicity m,
other generator weights a_i, and preferred Apéry exponent ideal T. Put

\[
A=\min_i a_i\ge m+1,\quad b_i=a_i/A,\quad
H=\max_T b\cdot x,\quad D_0=3mH-4\sum_T b\cdot x.
\]

The exact arithmetic identity is

\[
mW_4=A D_0-m(m-1).
\]

For m>=30, the geometric estimate

\[
\boxed{m-D_0\le29/10}
\]

already implies Wilf. It is weaker than the previously pursued estimate
`m-D_0<=1`, and does not assert strict positivity of W.

**Proof.** If W_4<0, integrality gives W_4<=-1, so

\[
D_0\le\frac{m(m-2)}{A}
\le\frac{m(m-2)}{m+1}
=m-3+\frac3{m+1}.
\]

Consequently

\[
m-D_0\ge3-\frac3{m+1}
\ge\frac{90}{31}>\frac{29}{10},
\]

a contradiction. The last strict comparison is the integer inequality
`900>899`. No structural restriction on T is needed for this implication.

More generally, a uniform bound `m-D_0<=C` suffices on m>=m_0 whenever
`C<3m_0/(m_0+1)`. This observation changes the amount of geometric slack
needed to prove Wilf; it is not itself an inequality for the remaining ideals.
