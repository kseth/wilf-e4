# The three-plane projection theorem

## Status and purpose

This note supplies the analytic replacement adopted by roadmap task D3.
Together with the [B3.1 entry lemma](six-maxima-entry.md) and the
[G3 projection inequality](final-window-projection.md), it completes the
large-multiplicity branch with corner \(p=(1,1,1)\), without a shape search,
residue enumeration, modular-cut computation, or linear program.

The new order-theoretic statement is:

> **Theorem 1.1.** Let \(T\subseteq\mathbb N^3\) be a finite lower ideal in
> which \((1,1,1)\) is minimal excluded. Suppose each coordinate plane has at
> most one mixed minimal exclusion. Put \(K=\operatorname{Max}(T)\). Then
> \[
> \boxed{\Phi(T,K)<0\quad\Longrightarrow\quad |T|\le29.}
> \tag{1}
> \]
> Consequently \(|T|\ge30\) implies \(\Phi(T,K)\ge0\).

Here, as in G3,

\[
P(T)=\sum_{j=1}^3|\pi_jT|,
\qquad
E(X)=\sum_{x\in X}|x|_1-\sum_j\max_{x\in X}x_j,
\]
\[
\Phi(T,X)=P(T)-3|X|-E(X).
\tag{2}
\]

The theorem is geometric: it requires neither residue labels nor generator
weights. B3.1 proves its plane-corner hypothesis for a genuine preferred
Apéry ideal. The role of the threshold 30 is essential to the retained route:
this note does not prove the broader historical six-final-window theorem.

## 1. The three possible plane frontiers

Put

\[
h_i=\max_{x\in T}x_i,
\qquad h=h_1+h_2+h_3.
\tag{3}
\]

Minimal exclusion of \((1,1,1)\) gives \(e_i+e_j\in T\) for every distinct
\(i,j\). Thus \(h_i\ge1\), \(h\ge3\), and every coordinate plane has points
with both coordinates positive. No point of \(T\) has three positive
coordinates.

Fix a plane with coordinates \(i,j\). Its pure-axis minimal exclusions are
\((h_i+1,0)\) and \((0,h_j+1)\). Since it has at most one mixed exclusion,
its footprint is either the full rectangle
\([0,h_i]\times[0,h_j]\), or that rectangle with one upper-right quadrant
deleted: every excluded point dominates one of these minimal exclusions.
In the latter case write the mixed corner as \((b+1,d+1)\), where

\[
0\le b<h_i,\qquad 0\le d<h_j.
\]

The included point \((1,1)\) rules out \(b=d=0\). There are therefore exactly
three types, with the side-capped type also allowed in the transposed
orientation:

| Plane type | Parameters | Mixed maximal points | Pure-axis planar maximum |
|---|---|---|---|
| Rectangle | none | \((h_i,h_j)\) | none |
| Split frontier | \(b,d\ge1\) | \((b,h_j),(h_i,d)\) | none |
| Side cap at axis \(i\) | \(b\ge1,\ d=0\) | \((b,h_j)\) | \((h_i,0)\) |

Every mixed planar maximum is a global maximum of \(T\): a point dominating
it must lie in the same plane, since three-positive-coordinate points are
excluded. A pure-axis point can be globally maximal only at its axis top.
That top is globally maximal precisely when both incident plane frontiers
have a side cap at that axis.

Let \(s\) be the number of split frontiers. Each plane contributes one mixed
global maximum, and a split frontier contributes one more. If \(I\) is the
set of globally maximal axis directions, then

\[
k:=|K|=3+s+|I|\le6.
\tag{4}
\]

The upper bound follows either from B3.1 or directly because each plane has
at most two planar maxima and every global maximum is one of them.

## 2. Counting mixed points and frontier corrections

For each plane \(i,j\), let \(c_{ij}\) be the number of its points with both
coordinates positive. Define a local frontier correction \(\beta_{ij}\) and
a local axis charge \(\nu_{ij}\) by the following table.

| Plane type | \(c_{ij}\) | \(\beta_{ij}\) | \(\nu_{ij}\) |
|---|---|---|---|
| Rectangle | \(h_i h_j\) | \(0\) | \(0\) |
| Split frontier | \(b h_j+d h_i-bd\) | \(b+d\) | \(0\) |
| Side cap at axis \(i\) | \(b h_j\) | \(b\) | \(h_i\) |

Use the transposed formulas for a side cap at axis \(j\). Put

\[
B=\sum_{i<j}\beta_{ij},
\qquad
C=\sum_{i<j}(c_{ij}-\beta_{ij}),
\qquad
N=\sum_{i<j}\nu_{ij},
\qquad
J=\sum_{i\in I}h_i.
\tag{5}
\]

Two elementary inequalities will be enough:

\[
\boxed{B\le C+s+N,\qquad N\ge2J.}
\tag{6}
\]

For a rectangle, \(c_{ij}-\beta_{ij}=h_i h_j\ge0\). For a split frontier,

\[
\begin{aligned}
c_{ij}-\beta_{ij}
&=bd+b(h_j-d-1)+d(h_i-b-1)\\
&\ge bd\ge b+d-1.
\end{aligned}
\tag{7}
\]

The last inequality is \((b-1)(d-1)\ge0\). Thus its correction
\(\beta_{ij}=b+d\) costs at most its contribution to \(C\), plus one.
For a side cap,

\[
c_{ij}-\beta_{ij}=b(h_j-1)\ge0,
\qquad \beta_{ij}=b\le h_i=\nu_{ij}.
\tag{8}
\]

Summing these bounds proves the first part of (6). Each globally maximal
axis top requires a side cap at that axis in both incident planes, so its
length is charged twice in \(N\). This proves the second part.

## 3. The negative-score cardinality bound

The origin, three positive axes, and three positive plane interiors form a
disjoint decomposition of \(T\). Hence

\[
m:=|T|=1+h+B+C.
\tag{9}
\]

For a lower ideal contained in the coordinate planes, \(\pi_jT\) equals its
section in the opposite coordinate plane. Summing those section sizes gives

\[
P(T)=3+2h+B+C=m+h+2.
\tag{10}
\]

The sum of degrees of the mixed maxima in a plane is
\(h_i+h_j+\beta_{ij}-\nu_{ij}\), by the first table. Add the globally
maximal axis tops to obtain

\[
\sum_{x\in K}|x|_1=2h+B-N+J.
\tag{11}
\]

Every axis endpoint lies below a maximal point, so
\(\max_{x\in K}x_i=h_i\). Thus

\[
E(K)=h+B-N+J.
\tag{12}
\]

Set

\[
Q=h+C+N-J.
\tag{13}
\]

Equations (9)--(12) yield the exact identity

\[
\boxed{\Phi(T,K)=Q+3-3k.}
\tag{14}
\]

If \(\Phi(T,K)<0\), all quantities are integral. By (4),

\[
Q\le3k-4\le14.
\tag{15}
\]

Using (6), (9), and (13),

\[
\begin{aligned}
m
&=1+Q+B-N+J\\
&\le1+Q+C+s+J\\
&=1+2Q-h+s-N+2J\\
&\le1+2Q-h+s\\
&\le1+28-3+3=29.
\end{aligned}
\tag{16}
\]

Here \(h\ge3\) and \(s\le3\). This proves Theorem 1.1. No enumeration of
configurations or coordinate cutoff was used. \(\square\)

## 4. Passing from all maxima to the final window

If \(X\subseteq Y\subseteq\mathbb N^3\) are finite nonempty point sets, then

\[
E(X)\le E(Y).
\tag{17}
\]

Indeed, adding one point \(y\) increases the coordinate-\(i\) term of \(E\)
by

\[
y_i-\max\bigl(0,y_i-\max_{x\in X}x_i\bigr)\ge0.
\]

Consequently, for nonempty \(Z\subseteq K\),

\[
\Phi(T,Z)\ge\Phi(T,K).
\tag{18}
\]

### Theorem 4.1 (analytic B3 theorem)

Let \(S=\langle m,a_1,a_2,a_3\rangle\) be minimally four-generated with
\(m\ge30\). If its preferred Apéry ideal has corner \(p=(1,1,1)\), then

\[
\boxed{W_4(S)\ge0.}
\tag{19}
\]

#### Proof

B3.1 supplies the one-mixed-corner-per-plane hypothesis and
\(Z\subseteq K\) for the nonempty final Apéry window \(Z\).
Theorem 1.1 and \(m\ge30\) give \(\Phi(T,K)\ge0\), so (18) gives
\(\Phi(T,Z)\ge0\). G3 now proves

\[
mW_4(S)\ge m\Phi(T,Z)+E(Z)\ge0.
\]

\(\square\)

The boundary \(\Phi=0\) is accepted throughout; only the strictly negative
integer case was bounded in (15). No strict weight ordering is used,
final-window points may be a proper subset of \(K\), and no genericity or
residue-lift assumption has been added.

## 5. Scope and retained interface

The retained B3 dependency chain is now

\[
\text{foundations}
\ \Longrightarrow\ \text{B3.1 plane-frontier restriction}
\ \Longrightarrow\ \text{Theorem 1.1}
\ \Longrightarrow\ \text{G3 and }W_4\ge0.
\]

The proof uses the already established routing hypothesis \(m\ge30\).
Smaller multiplicities remain in B1; this is not an analytic proof of the
unrestricted six-window theorem.

The [B3.2 shape specification](six-window-shape-specification.md) and
[B3.3 modular specification](six-window-modular-specification.md) describe
that broader alternative, but are no longer dependencies of the proposed
main theorem. Their finite assertions are not promoted under V0. D3 removes
R3 from the required replay queue rather than claiming that R3 has been run.
