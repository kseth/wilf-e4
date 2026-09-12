# The final-window projection inequality

## Status and purpose

This note completes task G3. It proves the projection estimate that precedes
the small-multiplicity and six-final-window arguments. The proof is analytic:
it combines the coordinate-line slack identity with exact residue accounting
and contains no finite search.

The note also records the equality boundary. In particular, every inequality
is weak where required; no genericity, strict weight ordering, or omitted
equality wall is hidden in the argument.

## 1. Setup and the final window

Let

\[
S=\langle m,a_1,a_2,a_3\rangle
\]

be a minimally four-generated numerical semigroup, and let
\(c\) be its conductor. Put

\[
W_4(S)=4|S\cap[0,c)|-c,
\]

and let \(T\subseteq\mathbb N^3\) be its preferred Apéry lower ideal. Write

\[
w(x)=a\mathbin\cdot x,\qquad
M=\max_{x\in T}w(x)=c+m-1.
\]

Thus \(|T|=m\), the residues \([w(x)]_m\) for \(x\in T\) are exactly
\(0,1,\ldots,m-1\), and each \(a_j>m\). For an integer \(u\), let
\([u]_m\) denote its representative in \(\{0,\ldots,m-1\}\).

Use the indexed coordinate-line family \(\mathcal L\), line lengths
\(L_\ell\), line tops \(t_\ell\), and projection count

\[
P(T)=\sum_{j=1}^3|\pi_j(T)|=|\mathcal L|
\]

from [`coordinate-lines.md`](coordinate-lines.md). The line-slack and moment
identities are

\[
D=\sum_{\ell\in\mathcal L}
L_\ell\bigl(M-w(t_\ell)\bigr),
\qquad
mW_4(S)=D-m(m-1).
\tag{1}
\]

Define the final Apéry window

\[
Z=\{x\in T:M-w(x)<m\},\qquad k=|Z|,
\tag{2}
\]

and let \(K=\operatorname{Max}(T)\) be the set of coordinatewise maximal
points of \(T\). For every nonempty finite
\(X\subseteq\mathbb N^3\), put

\[
E(X)=\sum_{x\in X}|x|_1-\sum_{j=1}^3\max_{x\in X}x_j.
\tag{3}
\]

Finally, set

\[
\Phi(T,Z)=P(T)-3k-E(Z).
\tag{4}
\]

### Lemma 1.1 (final-window geometry)

The following statements hold.

1. The labels of \(Z\) are precisely
   \[
   \operatorname{Ap}(S,m)\cap[c,c+m).
   \]
   In particular, \(Z\ne\varnothing\).
2. Every point of \(Z\) is globally maximal in \(T\), so \(Z\subseteq K\)
   and \(Z\) is an antichain.
3. Exactly \(3k\) indexed coordinate lines have their top in \(Z\).
   Consequently \(P(T)-3k\) lines have their top outside \(Z\).
4. The integer \(E(Z)\) is nonnegative. It vanishes exactly when, for each
   coordinate \(j\), at most one point of \(Z\) has positive \(j\)-th
   coordinate.

#### Proof

Since \(M=c+m-1\), condition (2) is equivalent to
\(c\le w(x)<c+m\). A point attaining \(M\) belongs to \(Z\), proving the
first assertion.

If \(z\in Z\) and \(z+e_j\in T\), then

\[
w(z+e_j)=w(z)+a_j>M-m+m=M,
\]

contradicting the definition of \(M\). Thus \(z\) is maximal.

A maximal point is the top of exactly one line in each of the three indexed
direction families. This gives \(3k\) lines. Finally, for each coordinate
\(j\),

\[
\sum_{z\in Z}z_j\ge\max_{z\in Z}z_j,
\]

and summing over \(j\) proves \(E(Z)\ge0\). Equality in the displayed
inequality holds exactly when at most one of the nonnegative integers
\(\{z_j:z\in Z\}\) is positive. Since the three coordinatewise differences
are nonnegative, their sum vanishes exactly under the stated condition.
\(\square\)

## 2. Exact residue decomposition

Fix a line \(\ell\in\mathcal L_j\), where \(\mathcal L_j\) is the family
parallel to \(e_j\). Write its top deficit uniquely as

\[
M-w(t_\ell)=mq_\ell+\beta_\ell,
\qquad q_\ell\in\mathbb N,\quad 0\le\beta_\ell<m.
\tag{5}
\]

Define

\[
R_j(L)=\sum_{r=0}^{L-1}[ra_j]_m
\tag{6}
\]

and

\[
C_\ell=
\bigl|\{0\le r<L_\ell:
\beta_\ell+[ra_j]_m\ge m\}\bigr|.
\tag{7}
\]

### Lemma 2.1 (exact modular line formula)

With

\[
\sigma_\ell
=mL_\ell q_\ell+mC_\ell-R_j(L_\ell),
\tag{8}
\]

one has

\[
\boxed{
mW_4(S)=\binom m2+\sum_{\ell\in\mathcal L}\sigma_\ell.
}
\tag{9}
\]

#### Proof

Read the points of \(\ell\) backward from its top:

\[
x_r=t_\ell-re_j,\qquad 0\le r<L_\ell.
\]

Their deficit residues are

\[
[M-w(x_r)]_m
=[\beta_\ell+ra_j]_m.
\]

By the definition of \(C_\ell\),

\[
\sum_{r=0}^{L_\ell-1}[M-w(x_r)]_m
=L_\ell\beta_\ell+R_j(L_\ell)-mC_\ell.
\tag{10}
\]

On the other hand,

\[
L_\ell\bigl(M-w(t_\ell)\bigr)
=mL_\ell q_\ell+L_\ell\beta_\ell.
\]

Eliminating \(L_\ell\beta_\ell\) with (10) expresses this line's contribution
to \(D\) as

\[
\sum_{x\in\ell}[M-w(x)]_m+\sigma_\ell.
\tag{11}
\]

In each coordinate direction the lines partition \(T\). Since
\([w(x)]_m\) runs through all residues modulo \(m\), so does
\([M-w(x)]_m\). Therefore the first term in (11), summed over one direction,
is \(\binom m2\), and summed over all three directions it is
\(3\binom m2\). Equation (1) now gives

\[
mW_4(S)
=3\binom m2+\sum_\ell\sigma_\ell-m(m-1)
=\binom m2+\sum_\ell\sigma_\ell.
\]

No estimate has yet been made. \(\square\)

## 3. The projection estimate

Call a line *deep* if its top is not in \(Z\), and *final* if its top is in
\(Z\).

### Lemma 3.1 (deep-line contribution)

For every deep line \(\ell\),

\[
\sigma_\ell\ge m+\binom{L_\ell}{2}\ge m.
\tag{12}
\]

Moreover, \(\sigma_\ell=m\) holds exactly when
\(L_\ell=1\) and \(q_\ell=1\).

#### Proof

For a deep line, (2) and (5) give \(q_\ell\ge1\). If
\(\ell\in\mathcal L_j\), then the axis points

\[
0,e_j,\ldots,(L_\ell-1)e_j
\]

belong to \(T\): each is coordinatewise below \(t_\ell\). Their residues are
distinct, and only the first has residue zero. Hence \(R_j(L_\ell)\) is at
most the sum of the \(L_\ell-1\) largest nonzero residues:

\[
R_j(L_\ell)
\le m(L_\ell-1)-\binom{L_\ell}{2}.
\tag{13}
\]

Using \(q_\ell\ge1\) and \(C_\ell\ge0\) in (8) proves (12).
More precisely,

\[
\sigma_\ell-m
\ge mL_\ell(q_\ell-1)+mC_\ell+\binom{L_\ell}{2}.
\tag{14}
\]

Thus equality forces \(L_\ell=1\) and \(q_\ell=1\). Conversely, when
\(L_\ell=1\), equations (6) and (7) give
\(R_j(1)=C_\ell=0\), so \(q_\ell=1\) gives
\(\sigma_\ell=m\). \(\square\)

For the final lines, define the used positive axis-prefix points

\[
\mathcal A(Z)=
\{re_j:1\le j\le3,\ 1\le r\le\max_{z\in Z}z_j\}.
\tag{15}
\]

For \(re_j\in\mathcal A(Z)\), let

\[
\nu_{j,r}=|\{z\in Z:z_j\ge r\}|.
\tag{16}
\]

Every point in \(\mathcal A(Z)\) belongs to \(T\). These points are distinct,
so residue injectivity shows that their residues
\([ra_j]_m\) are distinct and nonzero. The number of repeated occurrences in
the final-line prefixes is

\[
\begin{aligned}
\sum_{re_j\in\mathcal A(Z)}(\nu_{j,r}-1)
&=\sum_{z\in Z}|z|_1
  -\sum_{j=1}^3\max_{z\in Z}z_j\\
&=E(Z).
\end{aligned}
\tag{17}
\]

### Theorem 3.2 (final-window projection inequality)

\[
\boxed{
mW_4(S)
\ge m\bigl(P(T)-3|Z|-E(Z)\bigr)+E(Z)
=m\Phi(T,Z)+E(Z).
}
\tag{18}
\]

#### Proof

There are \(P(T)-3k\) deep lines by Lemma 1.1. A final line has
\(q_\ell=0\), because its top deficit is less than \(m\). Lemmas 2.1 and 3.1
therefore give

\[
\begin{aligned}
mW_4(S)
&=\binom m2+\sum_{\ell\ {\rm deep}}\sigma_\ell
  +\sum_{\ell\ {\rm final}}
   \bigl(mC_\ell-R_j(L_\ell)\bigr)\\
&\ge m(P(T)-3k)+\binom m2
  -\sum_{\ell\ {\rm final}}R_j(L_\ell).
\end{aligned}
\tag{19}
\]

By (15) and (16),

\[
\sum_{\ell\ {\rm final}}R_j(L_\ell)
=\sum_{re_j\in\mathcal A(Z)}
\nu_{j,r}[ra_j]_m.
\tag{20}
\]

The sum \(\binom m2\) contains every positive residue exactly once. Use one
copy to pay for each of the distinct residues in \(\mathcal A(Z)\). Any
unused positive residues make a nonnegative contribution. Each of the
\(E(Z)\) repeated copies in (17) costs at most \(m-1\). Hence

\[
\binom m2-\sum_{\ell\ {\rm final}}R_j(L_\ell)
\ge-(m-1)E(Z).
\tag{21}
\]

Substitution in (19) gives

\[
mW_4(S)
\ge m(P(T)-3k)-(m-1)E(Z)
=m\Phi(T,Z)+E(Z).
\]

\(\square\)

## 4. Boundary and equality

### Corollary 4.1

If \(\Phi(T,Z)\ge0\), then \(W_4(S)\ge0\). If, in addition,
\(\Phi(T,Z)>0\) or \(E(Z)>0\), then \(W_4(S)\ge1\).

Consequently, equality \(W_4(S)=0\) under the projection criterion is possible
only when

\[
\Phi(T,Z)=E(Z)=0.
\tag{22}
\]

#### Proof

The right side of (18) is nonnegative under the first hypothesis and strictly
positive under the second. Since \(m>0\) and \(W_4(S)\) is an integer, the
claims follow. \(\square\)

This is only a sufficient criterion. A negative value of \(\Phi(T,Z)\) is
not evidence that \(W_4(S)<0\); it merely identifies the cases for which
later arguments must retain more information than the projection counts.

The next statement identifies when (18) itself is sharp.

### Proposition 4.2 (equality in the projection estimate)

Equality holds in (18) if and only if all three conditions below hold.

1. Every deep line has \(L_\ell=1\) and \(q_\ell=1\).
2. Every final line has \(C_\ell=0\).
3. The used axis-prefix points exhaust the nonzero ideal:
   \[
   \mathcal A(Z)=T\setminus\{0\}.
   \]

Under these conditions \(E(Z)=0\).

#### Proof

Lemma 3.1 gives the first equality condition, while discarding the
nonnegative final-line terms \(mC_\ell\) in (19) gives the second.

It remains to inspect (21). Let \(\mathcal U\) be the set of positive residues
used by \(\mathcal A(Z)\). Subtracting the right side of (21) from its left
side gives

\[
\sum_{v\in\{1,\ldots,m-1\}\setminus\mathcal U}v
+
\sum_{re_j\in\mathcal A(Z)}
(\nu_{j,r}-1)\bigl(m-1-[ra_j]_m\bigr).
\tag{23}
\]

Both sums are nonnegative. Equality first forces
\(\mathcal U=\{1,\ldots,m-1\}\). Residue injectivity then says that
\(\mathcal A(Z)\) consists of all \(m-1\) nonzero points of \(T\), giving
condition 3.

Conversely, condition 3 makes \(T\) a union of its three coordinate axes.
Since \(Z\subseteq\operatorname{Max}(T)\), at most one point of \(Z\) has a
positive coordinate in any fixed direction. Thus every
\(\nu_{j,r}=1\), so \(E(Z)=0\), and (23) vanishes. Together with conditions
1 and 2, every estimate in (19)--(21) is an equality. \(\square\)

### Example 4.3 (the boundary is attained)

For

\[
S=\langle4,5,6,7\rangle,
\]

the preferred ideal is

\[
T=\{0,e_1,e_2,e_3\}.
\]

Here \(P(T)=9\), \(Z=\{e_1,e_2,e_3\}\), \(E(Z)=0\), and
\(\Phi(T,Z)=0\). The conductor is \(4\), so \(W_4(S)=0\). Thus neither the
weak inequality in Corollary 4.1 nor the endpoint in (22) can be made strict
without an additional hypothesis.

## 5. Monotonicity in the maximal set

### Lemma 5.1

If \(\varnothing\ne X\subseteq Y\subseteq\mathbb N^3\) are finite, then

\[
E(X)\le E(Y).
\tag{24}
\]

#### Proof

For each coordinate \(j\),

\[
\sum_{y\in Y\setminus X}y_j
\ge \max_{y\in Y}y_j-\max_{x\in X}x_j.
\]

Sum this inequality over the three coordinates and use (3). \(\square\)

### Corollary 5.2

Since \(Z\subseteq K=\operatorname{Max}(T)\),

\[
\boxed{\Phi(T,Z)\ge\Phi(T,K).}
\tag{25}
\]

Equality holds in (25) exactly when \(Z=K\).

#### Proof

By Lemma 5.1,

\[
\Phi(T,Z)-\Phi(T,K)
=3(|K|-|Z|)+E(K)-E(Z)\ge0.
\]

If equality holds, the first nonnegative term forces
\(|Z|=|K|\), and hence \(Z=K\). The converse is immediate. \(\square\)

In particular, proving \(\Phi(T,K)\ge0\) from the geometry of all maximal
points is enough to prove Wilf's inequality, even if the actual final window
is a proper subset of \(K\).

## 6. Retained interface

Later notes may cite the following facts without repeating the residue
bookkeeping:

1. \(Z=\operatorname{Ap}(S,m)\cap[c,c+m)\) in exponent coordinates and is
   an antichain contained in \(\operatorname{Max}(T)\);
2. exactly \(3|Z|\) indexed lines are final;
3. the estimate (18), including its equality boundary;
4. \(\Phi(T,Z)\ge0\) is sufficient for Wilf, with strict positivity except
   possibly when \(\Phi(T,Z)=E(Z)=0\); and
5. replacing \(Z\) by all maximal points can only decrease \(\Phi\).

No full-support-corner, multiplicity bound, or computational hypothesis is
used.
