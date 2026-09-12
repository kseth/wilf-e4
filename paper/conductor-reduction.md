# The negative-case conductor reduction

## Status and purpose

This note completes task B1.2. It proves the analytic implication

\[
W_4(S)<0
\quad\Longrightarrow\quad
M\le m(m-2),
\]

where \(M\) is the largest Apéry element. It also records the resulting
conductor and generator bounds used to make the small-multiplicity search
finite.

The proof has no multiplicity threshold and no computer-assisted input. Its
only substantive ingredients are the full-weighted theorem in
[`full-weighted-ideal.md`](full-weighted-ideal.md), the strengthened
predecessor-line bound in [`coordinate-lines.md`](coordinate-lines.md), and
the exact moment identity in [`foundations.md`](foundations.md).

## 1. Setup

Let

\[
S=\langle m,a_1,a_2,a_3\rangle
\]

be a minimally four-generated numerical semigroup. Let \(c\) be its
conductor, let

\[
W_4(S)=4|S\cap[0,c)|-c,
\]

and let \(T\subseteq\mathbb N^3\) be its preferred Apéry lower ideal. Write

\[
w(x)=a_1x_1+a_2x_2+a_3x_3,
\qquad
M=\max_{x\in T}w(x)=c+m-1,
\]

\[
s=\sum_{x\in T}x,
\qquad
D=3mM-4(a_1,a_2,a_3)\mathbin\cdot s.
\]

The coordinate-line and moment identities give

\[
D=\sum_{\ell}L_\ell\bigl(M-w(t_\ell)\bigr)
\tag{1}
\]

and

\[
mW_4(S)=D-m(m-1).
\tag{2}
\]

Every summand in (1) is nonnegative because every line top \(t_\ell\)
belongs to \(T\).

## 2. A non-full ideal has a low-weight corner

Recall that \(T\) is *full weighted* when

\[
T=\{x\in\mathbb N^3:w(x)\le M\}.
\tag{3}
\]

### Lemma 2.1 (low-weight corner)

If \(T\) is not full weighted, then there is a minimal excluded point
\(p\in\mathbb N^3\setminus T\) satisfying

\[
w(p)\le M.
\tag{4}
\]

#### Proof

The inclusion

\[
T\subseteq\{x\in\mathbb N^3:w(x)\le M\}
\]

holds by the definition of \(M\). If equality fails, the following set is
finite because all three weights are positive, and it is nonempty:

\[
U=\{x\notin T:w(x)\le M\}.
\]

Choose \(p\in U\) of least total degree. If \(p_i>0\), then
\(w(p-e_i)<w(p)\le M\). The point \(p-e_i\) cannot belong to \(U\), by
minimality of \(|p|_1\), so it belongs to \(T\). Thus every positive-coordinate
predecessor of \(p\) lies in \(T\), which is exactly minimal exclusion.
Condition (4) holds because \(p\in U\). \(\square\)

## 3. The predecessor lines contribute at least the maximum

### Lemma 3.1 (maximum-sized contribution)

If \(p\) is a minimal excluded point satisfying \(w(p)\le M\), then

\[
D\ge M.
\tag{5}
\]

#### Proof

For each \(i\) with \(p_i>0\), the point \(p-e_i\) is the top of its
coordinate-\(i\) line. That line has length exactly \(p_i\): lower closure
supplies the points whose \(i\)-th coordinates are
\(0,1,\ldots,p_i-1\), and no later point can be included because it would
dominate the excluded point \(p\).

These lines belong to different indexed coordinate families, so they are
distinct summands in (1), even when the underlying geometric lines intersect.
Their total contribution is

\[
\begin{aligned}
\sum_{i:p_i>0}p_i\bigl(M-w(p-e_i)\bigr)
&=\sum_{i:p_i>0}p_i\bigl(M-w(p)+a_i\bigr)\\
&=|p|_1\bigl(M-w(p)\bigr)+w(p)\\
&=M+(|p|_1-1)\bigl(M-w(p)\bigr)\\
&\ge M.
\end{aligned}
\tag{6}
\]

All remaining summands in (1) are nonnegative, proving (5). This is the
Apéry specialization of the strengthened predecessor-line bound in the
coordinate-line note. \(\square\)

## 4. Conductor and generator bounds

### Theorem 4.1 (negative-case conductor reduction)

If \(W_4(S)<0\), then

\[
\boxed{
M\le m(m-2),
\qquad
c\le m^2-3m+1,
\qquad
\max_i a_i\le m(m-2).
}
\tag{7}
\]

#### Proof

The full-weighted theorem proves \(W_4(S)\ge0\) whenever (3) holds. Thus
the assumption \(W_4(S)<0\) forces \(T\) to be non-full. Lemmas 2.1 and
3.1 then give

\[
M\le D.
\tag{8}
\]

The Wilf number is an integer, so \(W_4(S)<0\) implies
\(W_4(S)\le-1\). Equation (2) therefore gives

\[
D=mW_4(S)+m(m-1)
\le-m+m(m-1)
=m(m-2).
\tag{9}
\]

Combining (8)--(9) proves the bound on \(M\). Since \(M=c+m-1\),

\[
c=M-m+1\le m(m-2)-m+1=m^2-3m+1.
\]

Finally, every nonmultiplicity minimal generator \(a_i\) is an Apéry
element, and \(M\) is the largest Apéry element. Hence \(a_i\le M\) for
each \(i\), proving the last assertion. \(\square\)

### Corollary 4.2 (finite generator box)

After sorting the nonmultiplicity generators, every hypothetical negative
example of multiplicity \(m\) lies in the inclusive box

\[
m<a_1<a_2<a_3\le m(m-2).
\tag{10}
\]

The theorem makes this a necessary search domain, not a sufficient criterion
for negativity. Any exhaustive computation over (10) must still enforce
minimal generation and \(\gcd(m,a_1,a_2,a_3)=1\).

## 5. Endpoint and scope audit

The retained bounds above are inclusive. In the absence of a separately
proved sharpening, a finite verification must not discard the endpoint
\(a_3=m(m-2)\). Equality \(M=m(m-2)\) would require

\[
W_4(S)=-1,
\qquad
D=M.
\]

Because \(e_1,e_2,e_3\in T\), the low-weight corner in Lemma 2.1 has
\(|p|_1\ge2\). Equality in (6) would therefore additionally force
\(w(p)=M\), while equality in (5) would force every unselected line slack in
(1) to vanish. These observations are not used to narrow the search; they
only confirm where equality was retained.

Neither the proof nor its conclusion assumes \(m\le29\). The range
\(20\le m\le29\) enters only in B1.3. The
[finite generator-box specification](small-multiplicity-specification.md)
proves exactly how the finite box (10), together with the bound on \(M\),
covers every possible counterexample. No claim about nonnegative cases
follows from the bound: a semigroup with \(W_4(S)\ge0\) may have arbitrarily
larger conductor.

## 6. Retained interface

Later work may use the following implication without reopening the
full-weighted classification or the predecessor-line calculation:

> **B1.2.** For every minimally four-generated numerical semigroup,
> \[
> W_4(S)<0\Longrightarrow
> M\le m(m-2),\quad
> c\le m^2-3m+1,\quad
> \max_i a_i\le m(m-2).
> \]

This is an analytic infinite-to-finite reduction. It does not itself verify
any semigroup in the resulting generator box.

## 7. Historical source

The argument was reconstructed from Section 4.2 of the historical
[`global finite-reduction deliverable`](../artifacts/wilf_four_generators_review_package_2026-09-11/deliverables/wilf_edim4_global_finite_reduction_2026-09-05.md)
and checked against the independent conductor and small-multiplicity audits in
the same archive. Those documents remain research history; the present note
is the clean analytic interface for B1.3.
