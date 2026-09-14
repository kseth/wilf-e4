# The six-maxima entry lemma

## Status and purpose

This note completes task B3.1. It proves the analytic entry lemma for the
branch in which the full-support minimal excluded point is

\[
p=(1,1,1).
\]

There are three conclusions: each coordinate plane has at most one mixed
corner, the preferred Apéry ideal has at most six coordinatewise maximal
points, and its final Apéry window has at most six points. No finite search is
used.

The only arithmetic input is the support-and-collision rule from
[`foundations.md`](foundations.md). The proof in fact applies to any finite
residue-bijective lower ideal with the stated corner. Thus Chomicz's
relation-deletion L-shapes provide relevant geometric context, but changing
from the canonical preferred ideal supplies no shorter input to this lemma.

## 1. Setup and statement

Let

\[
S=\langle m,a_1,a_2,a_3\rangle
\]

be a minimally four-generated numerical semigroup, and let
\(T\subseteq\mathbb N^3\) be its preferred Apéry lower ideal. Write

\[
\lambda(x)=a\mathbin\cdot x.
\]

Thus \(|T|=m\), the labels \(\lambda(x)\) for \(x\in T\) are pairwise
distinct modulo \(m\), and \(a_i>m\) for each \(i\). For every
\(q\in\mathbb N^3\), let \(\rho(q)\in T\) be the unique representative of
its label residue:

\[
\lambda(\rho(q))\equiv\lambda(q)\pmod m.
\]

A *corner* is a minimal point of \(\mathbb N^3\setminus T\). A corner in the
plane \(x_k=0\) is *mixed* if its other two coordinates are positive. Put

\[
K=\operatorname{Max}(T),
\qquad
M=\max_{x\in T}\lambda(x),
\qquad
Z=\{x\in T:M-\lambda(x)<m\}.
\tag{1}
\]

For the preferred Apéry ideal, \(M=c+m-1\), so the labels of \(Z\) are
exactly the Apéry elements in \([c,c+m)\).

### Theorem 1.1 (B3.1)

Suppose that \((1,1,1)\) is a corner of \(T\). Then:

1. each coordinate plane contains at most one mixed corner;
2. \(|K|\le6\); and
3. \(Z\subseteq K\), so \(|Z|\le6\).

## 2. The opposite-axis forcing argument

We use the following consequences of Proposition 5.1 in the foundational
note.

- A corner and its residue representative have disjoint supports.
- Distinct corners with intersecting supports have different residues.

Since \(p=(1,1,1)\) has full support, its representative is zero. Hence

\[
a_1+a_2+a_3\equiv0\pmod m.
\tag{2}
\]

For \(k\in\{1,2,3\}\), let

\[
h_k=\max\{t\in\mathbb N:te_k\in T\}.
\tag{3}
\]

This is well-defined because \(T\) is finite and contains \(e_k\).

### Lemma 2.1 (opposite-axis forcing)

Let \(\{i,j,k\}=\{1,2,3\}\), and let \(q\) be a mixed corner in the plane
\(x_k=0\). Then

\[
\rho(q)=h_ke_k.
\tag{4}
\]

#### Proof

The support rule forces \(\rho(q)=\gamma e_k\) for some
\(0\le\gamma\le h_k\). The corners \(q\) and \(p\) are distinct and have
intersecting supports, so they cannot have the same residue. Since \(p\) has
residue zero, \(\gamma\ne0\).

Both positive-coordinate predecessors of \(q\) belong to \(T\). Lower
closure therefore gives

\[
r=q-e_i-e_j\in T.
\]

Using (2),

\[
\lambda(r)
\equiv\lambda(q)-a_i-a_j
\equiv\gamma a_k+a_k
\equiv(\gamma+1)a_k
\pmod m.
\tag{5}
\]

If \(\gamma<h_k\), then \((\gamma+1)e_k\in T\). Equation (5) would give two
distinct points of \(T\) with the same residue: \(r\) has zero \(k\)-th
coordinate, while \((\gamma+1)e_k\) has positive \(k\)-th coordinate. This
contradicts residue injectivity. Hence \(\gamma=h_k\), proving (4).
\(\square\)

### Corollary 2.2 (one mixed corner per plane)

Each coordinate plane contains at most one mixed corner.

#### Proof

By Lemma 2.1, every mixed corner in the plane \(x_k=0\) has the residue of
the same point \(h_ke_k\). Any two such corners have intersecting supports,
so the collision rule says that their residues must be different. Thus there
cannot be two. The argument is symmetric in the three coordinates.
\(\square\)

## 3. From planar corners to global maxima

The next elementary observation isolates the purely order-theoretic part of
the argument.

### Lemma 3.1 (planar frontier)

Let \(U\subseteq\mathbb N^2\) be a finite nonempty lower ideal. If \(U\) has
at most \(r\) mixed corners, then

\[
|\operatorname{Max}(U)|\le r+1.
\tag{6}
\]

#### Proof

List the maximal points as

\[
(u_1,v_1),\ldots,(u_s,v_s),
\qquad
u_1<\cdots<u_s.
\]

Incomparability forces \(v_1>\cdots>v_s\). For each \(t<s\), the point

\[
q_t=(u_t+1,v_{t+1}+1)
\tag{7}
\]

is excluded. Indeed, if it belonged to \(U\), it would lie below some
maximal point. A maximal point with first coordinate greater than \(u_t\)
has second coordinate at most \(v_{t+1}\), which is impossible for a point
above \(q_t\).

Both predecessors of \(q_t\) belong to \(U\), because

\[
(u_t,v_{t+1}+1)\le(u_t,v_t),
\qquad
(u_t+1,v_{t+1})\le(u_{t+1},v_{t+1}).
\]

Thus the \(s-1\) distinct points in (7) are mixed corners. Hence
\(s-1\le r\), which is (6).
\(\square\)

### Proposition 3.2 (six global maxima)

One has

\[
|K|\le6.
\tag{8}
\]

#### Proof

Because \((1,1,1)\notin T\) and \(T\) is a lower ideal, no point of \(T\)
can have all three coordinates positive. Therefore

\[
T=T_1\cup T_2\cup T_3,
\qquad
T_k=T\cap\{x_k=0\}.
\tag{9}
\]

Each \(T_k\), viewed as a lower ideal in \(\mathbb N^2\), has at most one
mixed corner by Corollary 2.2: a planar mixed corner has exactly the same
positive-coordinate predecessor conditions as a corner of \(T\). Lemma 3.1
gives

\[
|\operatorname{Max}(T_k)|\le2.
\tag{10}
\]

Every point of \(K\) lies in at least one \(T_k\), and global maximality
makes it maximal in every plane section containing it. Consequently

\[
K\subseteq
\operatorname{Max}(T_1)\cup
\operatorname{Max}(T_2)\cup
\operatorname{Max}(T_3).
\]

Summing the three bounds in (10) proves (8). Possible overlaps between plane
sections only make the bound smaller.
\(\square\)

## 4. The final Apéry window

### Proposition 4.1

The set \(Z\) in (1) satisfies \(Z\subseteq K\), and hence

\[
|Z|\le6.
\tag{11}
\]

#### Proof

Suppose \(z\in Z\) were not maximal. Lower closure would then give an
immediate successor \(z+e_i\in T\) in some coordinate direction. But

\[
M-\lambda(z)<m<a_i
\]

implies \(\lambda(z+e_i)=\lambda(z)+a_i>M\), contradicting the definition
of \(M\). Thus \(Z\subseteq K\), and Proposition 3.2 gives (11).
\(\square\)

## 5. Retained interface and scope

Later B3 tasks may cite Theorem 1.1 for exactly the following facts:

1. a plane section has at most one mixed corner and at most two planar
   maximal points;
2. \(4\le|K|\le6\) after the separate low-type disposal is applied; and
3. the final-window classification needs to cover only \(|Z|\le6\).

The lower bound \(|K|\ge4\) comes from the published type reduction recorded
in the proof outline; it is not part of B3.1. The
[B3.2 shape specification](six-window-shape-specification.md) now supplies the
finite geometric reduction, and the
[B3.3 modular specification](six-window-modular-specification.md) supplies
the all-label, all-cut, and integer-lift implication. The D3 simplification
gate must now decide whether the finite predicate itself remains necessary.
The branch assumption \(m\ge30\) is not used in the entry lemma.
