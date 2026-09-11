# Apéry foundations for the four-generator proof

## Status and purpose

This note supplies the common front end of the proposed proof. It constructs
the preferred Apéry exponent set, proves the residue and minimal-exclusion
properties used later, and derives the exact moment form of Wilf's inequality.
There is no computer-assisted assertion here.

The construction and its essential properties are not new. The preferred
factorizations and lower-ideal argument occur in Zhai's proof of Theorem 1;
the monomial-ideal, periodic-tiling, and minimal-exclusion formulations are
developed by Hellus, Rechenauer, and Waldi. Short proofs are included so that
the later argument can be read without translating conventions between
sources.

## 1. Setup

Let

\[
S=\langle m,a_1,a_2,a_3\rangle\subseteq\mathbb N
\]

be a minimally four-generated numerical semigroup, with \(m\) its
multiplicity. Thus \(m<a_i\) for every \(i\). Let \(c\) be its conductor,
\(g=|\mathbb N\setminus S|\) its genus, and

\[
n=|S\cap[0,c)|,\qquad W_4(S)=4n-c.
\]

Write

\[
\operatorname{Ap}(S,m)=\{w\in S:w-m\notin S\}
\]

for the Apéry set with respect to \(m\). Define the label map

\[
\begin{gathered}
a=(a_1,a_2,a_3),\\
\lambda:\mathbb N^3\longrightarrow S,\qquad
\lambda(x)=a_1x_1+a_2x_2+a_3x_3.
\end{gathered}
\]

We use the coordinatewise order on \(\mathbb N^3\). A set \(T\) is a
*lower ideal* if \(x\in T\) and \(0\le y\le x\) imply \(y\in T\).

## 2. Elementary Apéry facts

### Lemma 2.1

The Apéry set has the following properties.

1. It contains exactly one element in every residue class modulo \(m\), so
   \(|\operatorname{Ap}(S,m)|=m\).
2. Every Apéry element has a factorization using only
   \(a_1,a_2,a_3\).
3. The four elements \(0,a_1,a_2,a_3\) belong to the Apéry set, and the only
   factorization of \(a_i\) using the minimal generators is \(a_i\) itself.
4. If \(M=\max\operatorname{Ap}(S,m)\), then
   \[
   M=c+m-1.
   \]

#### Proof

Because \(S\) is cofinite, every residue class modulo \(m\) has a least
element in \(S\). An element \(w\in S\) is this least element precisely when
\(w-m\notin S\). This proves the first assertion.

No factorization of an Apéry element can use \(m\): removing one copy would
put \(w-m\) in \(S\). This proves the second assertion. If \(a_i-m\in S\),
then \(a_i=m+(a_i-m)\) expresses \(a_i\) using the other minimal generators,
contrary to minimality. Hence \(a_i\in\operatorname{Ap}(S,m)\). In any
factorization of \(a_i\) different from the single generator \(a_i\), the
coefficient of \(a_i\) must be zero because all generators are positive.
Such a factorization again contradicts minimality, proving the third
assertion.

Finally, \(w-m\notin S\) for every Apéry element \(w\), so \(w-m\le c-1\)
and \(w\le c+m-1\). Conversely, \(c-1+m\in S\), while
\((c-1+m)-m=c-1\notin S\). Thus \(c+m-1\) is itself an Apéry element. ∎

## 3. Preferred exponent representatives (F1)

Order \(\mathbb N^3\) lexicographically. For each
\(w\in\operatorname{Ap}(S,m)\), let \(x(w)\) be the lexicographically least
factorization satisfying \(\lambda(x(w))=w\), and put

\[
T=\{x(w):w\in\operatorname{Ap}(S,m)\}.
\]

The minimum exists because a fixed positive integer has only finitely many
factorizations using the positive integers \(a_1,a_2,a_3\).

### Proposition 3.1 (preferred Apéry ideal)

The set \(T\subseteq\mathbb N^3\) has the following properties.

1. \(T\) is a finite lower ideal.
2. The restriction \(\lambda|_T\) is a bijection from \(T\) to
   \(\operatorname{Ap}(S,m)\). In particular, \(|T|=m\), and the labels of
   the points of \(T\) are pairwise distinct modulo \(m\).
3. \(0,e_1,e_2,e_3\in T\).

#### Proof

Only lower closure needs proof. Let \(x=x(w)\in T\), take \(0\le y\le x\),
and set \(v=x-y\). First, \(\lambda(y)\in\operatorname{Ap}(S,m)\). Otherwise
\(\lambda(y)-m\in S\), and hence

\[
w-m=(\lambda(y)-m)+\lambda(v)\in S,
\]

contrary to \(w\in\operatorname{Ap}(S,m)\).

Let \(y'=x(\lambda(y))\). If \(y'\ne y\), then
\(y'<_{\mathrm{lex}}y\). Lexicographic order is invariant under translation,
so \(y'+v<_{\mathrm{lex}}y+v=x\). But \(y'+v\) and \(x\) have the same label
\(w\), contradicting the choice of \(x\). Therefore \(y'=y\in T\).

The second assertion follows directly from the construction and Lemma 2.1(1).
Lemma 2.1(3) shows that the selected representatives of
\(0,a_1,a_2,a_3\) are \(0,e_1,e_2,e_3\), proving the last assertion. ∎

### Corollary 3.2 (residue-lattice tiling)

Let

\[
\Lambda=\{z\in\mathbb Z^3:a_1z_1+a_2z_2+a_3z_3\equiv0\pmod m\}.
\]

Then \(T\) is a complete set of representatives for
\(\mathbb Z^3/\Lambda\), and

\[
\mathbb Z^3=\bigsqcup_{u\in\Lambda}(u+T).
\]

#### Proof

Two integer vectors lie in the same coset of \(\Lambda\) exactly when their
labels agree modulo \(m\). Proposition 3.1 says that the \(m\) points of \(T\)
give all \(m\) residues exactly once. ∎

Separately, lower closure says that the complement of \(T\) in
\(\mathbb N^3\) is an additive upper ideal, and its monomials form an
Artinian monomial ideal. This is the
initial-ideal viewpoint of Hellus--Rechenauer--Waldi. In the broader geometric
terminology, \(T\) is a three-dimensional L-shape for the Apéry set.

## 4. The moment identity and baseline (F2)

### Lemma 4.1 (Apéry sum formula)

\[
g=\frac1m\sum_{w\in\operatorname{Ap}(S,m)}w-\frac{m-1}{2}.
\]

#### Proof

Write the least element of \(S\) congruent to
\(r\in\{0,\ldots,m-1\}\) as \(w_r=r+k_rm\). The gaps in that residue class
are exactly \(r,r+m,\ldots,r+(k_r-1)m\), with the empty interpretation for
\(k_r=0\). Therefore

\[
g=\sum_{r=0}^{m-1}k_r
=\frac1m\left(\sum_{r=0}^{m-1}w_r-\sum_{r=0}^{m-1}r\right),
\]

which is the claimed formula. ∎

Set

\[
s=\sum_{x\in T}x,\qquad A=\min_i a_i\ge m+1,\qquad
b_i=\frac{a_i}{A},\qquad H=\frac MA,
\]

and define

\[
D=3mM-4a\mathbin\cdot s,\qquad
D_0=3mH-4b\mathbin\cdot s.
\]

Thus \(D=AD_0\).

### Proposition 4.2 (exact Wilf moment identity)

\[
\boxed{mW_4(S)=D-m(m-1)=AD_0-m(m-1).}
\]

#### Proof

There are \(c\) integers in \([0,c)\), of which \(g\) are gaps, so
\(n=c-g\) and \(W_4=3c-4g\). Proposition 3.1 and Lemma 4.1 give

\[
\sum_{w\in\operatorname{Ap}(S,m)}w
=\sum_{x\in T}\lambda(x)=a\mathbin\cdot s
\]

and hence

\[
\begin{aligned}
mW_4
 &=3mc-4mg\\
 &=3mc-4a\mathbin\cdot s+2m(m-1)\\
 &=3mM-4a\mathbin\cdot s-m(m-1),
\end{aligned}
\]

where the last line uses \(M=c+m-1\). ∎

### Corollary 4.3 (choice-invariance)

The quantities \(a\cdot s\), \(D\), and \(D_0\) do not depend on the choice of
one factorization for each Apéry element. Indeed,

\[
a\mathbin\cdot s
=\sum_{x\in T}\lambda(x)
=\sum_{w\in\operatorname{Ap}(S,m)}w.
\]

The lexicographic choice is needed for the lower-ideal geometry, not for the
moment identity.

### Proposition 4.4 (Zhai's lower-ideal baseline)

\[
D=3mM-4a\mathbin\cdot s\ge0,
\qquad\text{equivalently}\qquad D_0\ge0.
\]

#### Proof

Fix a coordinate \(i\) and partition \(T\) into lines parallel to \(e_i\).
On a line of length \(L\), lower closure makes the points
\(u,u+e_i,\ldots,u+(L-1)e_i\), where \(u_i=0\). If \(t\) is its top, then

\[
\sum_{k=0}^{L-1}
\bigl(\lambda(u+ke_i)+a_i(u_i+k)\bigr)
=L\lambda(t)\le LM.
\]

Summing over all such lines gives

\[
\sum_{x\in T}\lambda(x)+a_i\sum_{x\in T}x_i\le mM.
\]

Now sum over the three coordinates. Since
\(\sum_i a_i\sum_{x\in T}x_i
=\sum_{x\in T}\lambda(x)=a\cdot s\), we obtain
\(4a\cdot s\le3mM\). ∎

This is the \(d=3\) specialization of Zhai's Lemma 3. It is only the
nonnegative baseline: Proposition 4.2 shows that Wilf's inequality requires
the stronger bound \(D\ge m(m-1)\), or
\(D_0\ge m(m-1)/A\).

## 5. Minimal excluded points (F3)

A point \(p\in\mathbb N^3\setminus T\) is *minimal excluded*, or a *corner*,
if every strictly smaller nonnegative point lies in \(T\). Since \(T\) is a
lower ideal, it is enough to require

\[
p-e_i\in T\qquad\text{whenever }p_i>0.
\]

Let \(\rho(p)\in T\) denote the unique point satisfying

\[
\lambda(\rho(p))\equiv\lambda(p)\pmod m.
\]

For \(x\in\mathbb N^3\), write
\(\operatorname{supp}(x)=\{i:x_i>0\}\).

### Proposition 5.1 (support and collision rules)

Let \(p,p'\) be minimal excluded points.

1. \(\operatorname{supp}(p)\cap\operatorname{supp}(\rho(p))=\varnothing\).
2. If \(p\ne p'\) and their supports intersect, then
   \(\lambda(p)\not\equiv\lambda(p')\pmod m\).
3. There is at most one full-support minimal excluded point. If it exists,
   its residue is zero. Every other minimal excluded point lies in a
   coordinate plane.

#### Proof

Suppose \(p_i>0\) and \(\rho(p)_i>0\). Minimal exclusion and lower closure
give \(p-e_i,\rho(p)-e_i\in T\). They are distinct points with the same
residue modulo \(m\), contradicting Proposition 3.1. This proves the first
assertion.

If distinct \(p,p'\) share a positive coordinate \(i\) and have the same
residue, then \(p-e_i,p'-e_i\in T\) are distinct and have the same residue,
again a contradiction. This proves the second assertion.

If \(p\) has full support, the first assertion forces \(\rho(p)=0\), so
\(\lambda(p)\equiv0\pmod m\). Two full-support minimal exclusions would then
contradict the second assertion. In three dimensions, a point without full
support has a zero coordinate and hence lies in a coordinate plane. ∎

The second and third assertions are the present specialization of
Hellus--Rechenauer--Waldi, Proposition 2.6. The first is the same
predecessor-subtraction argument applied to a corner and its representative.

## 6. Retained interface

All later branches may use the following facts without reopening their
construction:

- **F1:** \(T\) is a lower ideal of size \(m\), contains
  \(0,e_1,e_2,e_3\), and its labels form a complete residue system modulo
  \(m\).
- **F2:** \(mW_4=AD_0-m(m-1)\), the moment is independent of the selected
  L-shape, and \(D_0\ge0\) by Zhai's lower-ideal inequality.
- **F3:** a corner and its residue representative have disjoint supports;
  overlapping corners have distinct residues; consequently there is at most
  one full-support corner, and it has residue zero.

## 7. A small example

For \(S=\langle4,5,6,7\rangle\),

\[
\operatorname{Ap}(S,4)=\{0,5,6,7\},\qquad
T=\{0,e_1,e_2,e_3\}.
\]

The corner \(e_1+e_2\) has label \(11\), whose residue representative is
\(e_3\), with label \(7\); their supports are disjoint. The corner
\(e_1+e_3\) has label \(12\) and residue representative \(0\). These two
corners overlap in the first coordinate and have different residues, as
Proposition 5.1 requires.

Here \(c=4\), \(M=7\), \(a\cdot s=18\), and

\[
D=3\cdot4\cdot7-4\cdot18=12=m(m-1).
\]

Proposition 4.2 therefore gives \(W_4(S)=0\), the equality case.

## 8. Attribution map

| Statement used here | Source status |
|---|---|
| Basic Apéry residue, maximum, and sum formulas | Classical; the counting formula also appears as Zhai, Lemma 1 |
| Lexicographically preferred Apéry factorizations and lower closure | Zhai, proof of Theorem 1 |
| Initial-monomial-ideal formulation | Hellus--Rechenauer--Waldi, Proposition 2.3; context only, not needed in the proofs above |
| Periodic residue-lattice tiling | Hellus--Rechenauer--Waldi, Proposition 2.5 |
| Minimal-exclusion collision and full-support rules | Hellus--Rechenauer--Waldi, Proposition 2.6 |
| Weighted lower-ideal baseline | Zhai, Lemma 3 |
| Three-dimensional relation-deletion/L-shape viewpoint | Chomicz, Section 2; context only |
| Exact \(D_0\) normalization and displayed Wilf identity | Algebraic repackaging for the present proof; derived above from the classical Apéry formula |

## References

- Alex Zhai, “An asymptotic result concerning a question of Wilf,”
  [arXiv:1111.2779](https://arxiv.org/abs/1111.2779), 2011.
- Michael Hellus, Anton Rechenauer, and Rolf Waldi, “Variants on a question of
  Wilf,” [arXiv:1804.06141](https://arxiv.org/abs/1804.06141), version 2,
  2018.
- J. C. Rosales and P. A. García-Sánchez, *Numerical Semigroups*, Developments
  in Mathematics 20, Springer, 2009.
  [doi:10.1007/978-1-4419-0160-6](https://doi.org/10.1007/978-1-4419-0160-6).
- Kazimierz Chomicz, “On numerical semigroups with embedding dimension four,”
  [arXiv:2604.25653](https://arxiv.org/abs/2604.25653), version 3, 2026.
