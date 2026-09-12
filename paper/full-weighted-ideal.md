# Full weighted Apéry ideals

## Status and purpose

This note completes task B1.1. It proves that a preferred Apéry ideal which
contains every lattice point below its largest weight satisfies Wilf's
inequality. The proof is entirely analytic. In particular, the apparent
six-column case is excluded by residue injectivity, not by a finite search.

The inputs are the Apéry lower-ideal and corner rules from
[`foundations.md`](foundations.md) and the final-window estimate from
[`final-window-projection.md`](final-window-projection.md). The argument uses
the same lower-ideal/L-shape interface discussed by Chomicz, but no choice of
relation-deletion L-shape simplifies the residue argument below; see the
[focused comparison](../research/chomicz-assessment.md).

## 1. Setup and statement

Let

\[
S=\langle m,a_1,a_2,a_3\rangle
\]

be a minimally four-generated numerical semigroup. Let
\(T\subseteq\mathbb N^3\) be its preferred Apéry lower ideal, and put

\[
w(x)=a_1x_1+a_2x_2+a_3x_3,
\qquad
M=\max_{x\in T}w(x).
\]

Thus \(|T|=m\), the labels of its points are pairwise distinct modulo
\(m\), and \(0,e_1,e_2,e_3\in T\). We say that \(T\) is *full weighted* if

\[
T=\{x\in\mathbb N^3:w(x)\le M\}.
\tag{1}
\]

Permuting the three coordinates preserves (1), lower closure, residue
injectivity, and all projection quantities used below. We may therefore
write the three nonmultiplicity generators as

\[
a<b<d
\]

and use coordinates \((x,y,z)\), so that

\[
w(x,y,z)=ax+by+dz.
\]

The inequalities are strict because the minimal generators are distinct.

### Theorem 1.1 (full-weighted-ideal theorem)

If the preferred Apéry ideal \(T\) is full weighted, then

\[
W_4(S)\ge0.
\]

We prove the theorem in three steps.

## 2. Classification of the column projection

Project away the \(x\)-coordinate. By (1), its image is

\[
Q=\pi_x(T)
=\{(y,z)\in\mathbb N^2:by+dz\le M\}.
\tag{2}
\]

Put

\[
h_y=\left\lfloor\frac Mb\right\rfloor,
\qquad
h_z=\left\lfloor\frac Md\right\rfloor.
\]

Both are positive because \(e_2,e_3\in T\).

### Lemma 2.1 (three possible projections)

The set \(Q\) is one of

\[
\begin{aligned}
Q_3&=\{(0,0),(1,0),(0,1)\},\\
Q_4&=\{(0,0),(1,0),(2,0),(0,1)\},\\
Q_6&=\{(y,z)\in\mathbb N^2:y+z\le2\}.
\end{aligned}
\tag{3}
\]

#### Proof

For \(1\le j\le h_y\), define

\[
p_j=
\left(
\left\lfloor\frac{M-bj}{a}\right\rfloor+1,
j,0
\right).
\tag{4}
\]

This is a minimal excluded point. Its \(x\)-predecessor is included by the
floor definition. Moreover,

\[
w(p_j)\le M+a,
\]

so its \(y\)-predecessor has weight at most \(M+a-b\le M\). Both displayed
coordinates of \(p_j\) are positive because \(bj\le M\).

The representative in \(T\) of the residue of \(p_j\) must have support
disjoint from \(\{x,y\}\), so it lies on the \(z\)-axis. The corners
\(p_1,\ldots,p_{h_y}\) have intersecting supports and hence distinct
residues. The \(z\)-axis contains exactly

\[
0,e_3,\ldots,h_ze_3,
\]

and therefore

\[
h_y\le h_z+1.
\tag{5}
\]

First suppose \(M<b+d\). Then (2) contains no point with both coordinates
positive. Since

\[
d\le M<b+d<2d,
\]

we have \(h_z=1\). Equation (5) gives \(h_y\le2\), while \(h_y\ge1\).
This gives \(Q_3\) or \(Q_4\).

Now suppose \(M\ge b+d\). The point

\[
p=
\left(
\left\lfloor\frac{M-b-d}{a}\right\rfloor+1,
1,1
\right)
\tag{6}
\]

is a full-support minimal exclusion: its \(x\)-predecessor is included by
the floor definition, while removing \(e_2\) or \(e_3\) reduces its weight
from at most \(M+a\) by at least \(a\). By the corner rules, \(p\) has
residue zero. Each \(p_j\) has support intersecting that of \(p\), so none
of their distinct representatives on the \(z\)-axis can be zero. Hence

\[
h_y\le h_z.
\tag{7}
\]

If \(M\ge2b+d\), then

\[
p'=
\left(
\left\lfloor\frac{M-2b-d}{a}\right\rfloor+1,
2,1
\right)
\]

is a second full-support minimal exclusion. Indeed, its \(x\)-predecessor is
included by the floor definition, and removing \(e_2\) or \(e_3\) reduces
its weight from at most \(M+a\) by at least \(a\). It is distinct from
\(p\) because its \(y\)-coordinate is two. This contradicts the uniqueness
of a full-support corner, so

\[
M<2b+d<3d
\]

and \(h_z\le2\). On the other hand,

\[
M\ge b+d>2b,
\]

so \(h_y\ge2\). Since \(b<d\) also gives \(h_y\ge h_z\), equation (7)
forces

\[
h_y=h_z=2.
\tag{8}
\]

It follows from (8) that \(2d\le M<3b\). Every \((y,z)\) of total degree at
most two has weight at most \(2d\), while every point of total degree at
least three has weight at least \(3b\). Thus (2) is exactly \(Q_6\).
\(\square\)

## 3. The six-column triangle is impossible

For \((y,z)\in Q\), let

\[
L_{yz}=\left\lfloor\frac{M-by-dz}{a}\right\rfloor+1
\tag{9}
\]

be the length of its \(x\)-column. Subtracting \(b\) or \(d\) from the
available weight decreases a positive column length by at least one, because
\(b,d>a\).

### Lemma 3.1 (six-column exclusion)

The projection \(Q_6\) in (3) cannot occur.

#### Proof

Suppose it does, and abbreviate its positive column lengths by

\[
\begin{array}{c|cccccc}
(y,z)&(0,0)&(1,0)&(2,0)&(0,1)&(1,1)&(0,2)\\ \hline
L_{yz}&\alpha&\beta&\gamma&\varphi&\varepsilon&\eta.
\end{array}
\tag{10}
\]

The strict column descents give

\[
\alpha>\beta>\gamma>0,
\qquad
\alpha>\varphi>\eta>0,
\qquad
\varepsilon<\min(\beta,\varphi).
\tag{11}
\]

Work in \(\mathbb Z/m\mathbb Z\), and let \(r\) be the least positive
integer for which \(ra\equiv0\pmod m\). The point
\((\varepsilon,1,1)\) is the full-support minimal exclusion above the mixed
column: its \(x\)-predecessor lies in that column, and its other two
predecessors are included by \(\varepsilon<\varphi,\beta\). It therefore has
residue zero:

\[
\varepsilon a+b+d\equiv0\pmod m.
\tag{12}
\]

The residues in the origin column are

\[
0,a,\ldots,(\alpha-1)a,
\]

whereas (12) makes those in the mixed column

\[
-\varepsilon a,-(\varepsilon-1)a,\ldots,-a.
\]

All \(\alpha+\varepsilon\) points belong to \(T\), so residue injectivity
shows that these consecutive multiples of \(a\) are distinct. Consequently

\[
r\ge\alpha+\varepsilon.
\tag{13}
\]

The two points \((\beta,1,0)\) and \((\gamma,2,0)\) are minimal
exclusions: their \(x\)-predecessors lie at the tops of their columns, and
their \(y\)-predecessors are included by \(\beta<\alpha\) and
\(\gamma<\beta\). Their representatives have support on the \(z\)-axis.
Their residues are nonzero because their supports meet that of
\((\varepsilon,1,1)\), and they are distinct from each other. Since the
\(z\)-axis consists of \(0,e_3,2e_3\), their residues therefore permute
\(d,2d\).

The swapped assignment would be

\[
\beta a+b\equiv2d,
\qquad
\gamma a+2b\equiv d.
\tag{14}
\]

Subtracting twice the second congruence in (14) from the first gives

\[
(\beta-2\gamma)a-3b\equiv0\pmod m,
\]

while the second congruence in (14), substituted into (12), gives

\[
(\varepsilon+\gamma)a+3b\equiv0\pmod m.
\]

Adding these relations eliminates \(b\) and gives

\[
(\beta-\gamma+\varepsilon)a\equiv0\pmod m.
\]

But

\[
0<\beta-\gamma+\varepsilon
<\alpha+\varepsilon\le r,
\]

contradicting the definition of \(r\). We must therefore have

\[
\beta a+b\equiv d,
\qquad
\gamma a+2b\equiv2d.
\tag{15}
\]

The same argument for the minimal exclusions
\((\varphi,0,1)\) and \((\eta,0,2)\), whose representatives lie on the
\(y\)-axis, rules out the swapped assignment there: it would give
\((\varphi-\eta+\varepsilon)a\equiv0\pmod m\), although

\[
0<\varphi-\eta+\varepsilon<\alpha+\varepsilon\le r.
\]

Consequently

\[
\varphi a+d\equiv b,
\qquad
\eta a+2d\equiv2b.
\tag{16}
\]

Adding the first congruences in (15)--(16), and subtracting the second
congruences from twice their respective first congruences, shows that

\[
\beta+\varphi,
\qquad
2\beta-\gamma,
\qquad
2\varphi-\eta
\tag{17}
\]

are positive multiples of \(r\). Each is strictly less than \(2\alpha\),
and (13) gives \(\alpha<r\). Thus all three integers in (17) lie strictly
between zero and \(2r\), so

\[
\beta+\varphi=r,
\qquad
2\beta-\gamma=r,
\qquad
2\varphi-\eta=r.
\]

Adding the last two equalities and subtracting twice the first gives

\[
\gamma+\eta=0,
\]

contrary to (11). Hence \(Q_6\) is impossible. \(\square\)

### Remark 3.2

The proof of Lemma 3.1 used only residue bijectivity, the corner rules, the
six-point projection, and the strict descents in (11). The exact floor
formula (9) is not otherwise needed. This isolates the arithmetic obstruction
from the full-weighted classification which produces the six-point shape.

## 4. The remaining projection scores

Let

\[
Z=\{x\in T:M-w(x)<m\},
\qquad
K=\operatorname{Max}(T),
\]

and use the notation

\[
P(T)=\sum_{j=1}^3|\pi_j(T)|,
\qquad
E(X)=\sum_{x\in X}|x|_1-\sum_{j=1}^3\max_{x\in X}x_j,
\]

\[
\Phi(T,X)=P(T)-3|X|-E(X)
\]

from the final-window note. That note proves \(E(Z)\ge0\), \(Z\subseteq K\),
and

\[
mW_4(S)\ge m\Phi(T,Z)+E(Z).
\tag{18}
\]

For nonempty \(X\subseteq K\), adding points to \(X\) cannot decrease
\(|X|\), and it cannot decrease \(E(X)\): in each coordinate the increase
in the coordinate sum is at least the increase in the coordinate maximum.
Hence

\[
\Phi(T,Z)\ge\Phi(T,K).
\tag{19}
\]

We now calculate the right side for the only two remaining projections.

### Lemma 4.1 (three columns)

If \(Q=Q_3\), then \(\Phi(T,K)\ge0\).

#### Proof

Write the column lengths over \((0,0),(1,0),(0,1)\) as
\(\alpha,\beta,\gamma\). Then

\[
\alpha>\beta,\gamma\ge1,
\qquad
m=\alpha+\beta+\gamma.
\tag{20}
\]

The three column tops are pairwise incomparable and every other point is
below one of them, so they are precisely \(K\). Direct projection counting
gives

\[
P(T)=3+(\alpha+\gamma)+(\alpha+\beta)
=3+\alpha+m.
\tag{21}
\]

The sum of the total degrees of the three tops is \(m-1\), while their
coordinatewise maxima sum to \((\alpha-1)+1+1=\alpha+1\). Therefore

\[
E(K)=m-\alpha-2
\]

and

\[
\Phi(T,K)
=(3+\alpha+m)-9-(m-\alpha-2)
=2\alpha-4\ge0,
\tag{22}
\]

because \(\alpha>\beta\ge1\) implies \(\alpha\ge2\). \(\square\)

### Lemma 4.2 (four columns)

If \(Q=Q_4\), then \(\Phi(T,K)\ge0\).

#### Proof

Write the column lengths over \((0,0),(1,0),(2,0),(0,1)\) as
\(\alpha,\beta,\gamma,\delta\). Then

\[
\alpha>\beta>\gamma\ge1,
\qquad
\alpha>\delta\ge1,
\qquad
m=\alpha+\beta+\gamma+\delta.
\tag{23}
\]

Again, the four column tops are precisely \(K\). The projections have sizes

\[
4,
\qquad
\alpha+\delta,
\qquad
\alpha+\beta+\gamma,
\]

so

\[
P(T)=4+\alpha+m.
\tag{24}
\]

The total degrees of the four tops sum to \(m\), and their coordinatewise
maxima sum to \((\alpha-1)+2+1=\alpha+2\). Thus

\[
E(K)=m-\alpha-2
\]

and

\[
\Phi(T,K)
=(4+\alpha+m)-12-(m-\alpha-2)
=2\alpha-6\ge0,
\tag{25}
\]

because \(\alpha>\beta>\gamma\ge1\) implies \(\alpha\ge3\). \(\square\)

## 5. Proof of Theorem 1.1

Lemma 2.1 lists the three possible \(x\)-column projections. Lemma 3.1
excludes the six-column triangle, and Lemmas 4.1--4.2 give
\(\Phi(T,K)\ge0\) in the remaining cases. Equation (19) therefore gives
\(\Phi(T,Z)\ge0\), and (18) proves \(W_4(S)\ge0\).

No finite verification is used. \(\square\)

## 6. Retained interface

Later arguments may use the following result without reopening the column
classification:

> **B1.1.** If the preferred Apéry ideal is full weighted, then
> \(W_4(S)\ge0\). Analytically, its projection along the least-weight
> coordinate has three or four columns; the only other formal possibility is
> a six-column triangle, which residue injectivity excludes.

The immediate contrapositive used in the
[`conductor reduction`](conductor-reduction.md) is

\[
W_4(S)<0
\quad\Longrightarrow\quad
T\ne\{x\in\mathbb N^3:w(x)\le M\}.
\tag{26}
\]

## 7. Historical source

The proof was reconstructed from Section 4.1 of the historical
[`global finite-reduction deliverable`](../artifacts/wilf_four_generators_review_package_2026-09-11/deliverables/wilf_edim4_global_finite_reduction_2026-09-05.md)
and checked against the independent six-point and foundation audits in the
same archive. Those documents remain research history; this note is the
clean analytic statement used by the proof roadmap.
