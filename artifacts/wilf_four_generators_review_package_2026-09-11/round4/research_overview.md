# Wilf research: the continuous no-interior theorem and its arithmetic consequences

7 September 2026

**Status.** This continuation completes the continuous no-interior mean theorem, its multiplicity consequence, an integer theorem for equal weights, and another unbounded secondary family. These are arguments developed and independently checked within this research session; they have not received external mathematical review. **The unrestricted four-generator Wilf conjecture is not proved or disproved here.**

The main new geometric result closes the arbitrary-horn gap explicitly left open on 5 September. The remaining arithmetic and interior-corner questions below are not established by finite numerical evidence.

## 1. The exact target

Let
\[
S=\langle m,a_1,a_2,a_3\rangle,
\qquad m<a_1<a_2<a_3,
\]
be minimally generated, with conductor \(c\) and \(n=|S\cap[0,c)|\). Put
\[
W_4(S)=4n-c.
\]
Wilf asks for \(W_4(S)\ge0\).

Choose one preferred factorization of each element of the Apéry set with respect to \(m\), using an additive order to break ties. Its exponent vectors form a finite lower ideal \(T\subset\mathbb N^3\), with exactly \(m\) elements and distinct labels modulo \(m\). Define
\[
M=\max_{x\in T}a\cdot x=c+m-1,
\qquad \Sigma=\sum_{x\in T}a\cdot x,
\qquad D=3mM-4\Sigma.
\]
The exact identity is
\[
\boxed{mW_4=D-m(m-1).}
\tag{1}
\]
Thus the required arithmetic inequality is \(D\ge m(m-1)\).

A minimal excluded point is an exponent outside \(T\) whose proper divisors lie in \(T\). An **interior corner** means such a point has all three coordinates positive. The preferred Apéry ideal has at most one interior corner. The first theorem concerns the case with none.

## 2. The completed continuous theorem

**Theorem A.** Let \(K\subset\mathbb R_{\ge0}^3\) be a bounded lower set of positive volume that is a finite union of anchored rectangular boxes. Suppose its excluded upper orthants can all be generated at points supported on at most two coordinates. For every positive linear weight \(w\),
\[
\boxed{\frac{1}{\operatorname{vol}K}\int_K w(x)\,dx
\le \frac23\sup_Kw.}
\tag{2}
\]
Boundary conventions do not affect these integrals. The constant is sharp in limits of finite box unions.

Here is the complete chain of implications; the analytic reductions and exact identities appear in the appendices.

1. Scale the coordinates by their weights and normalize the largest coordinate sum to one. The pairwise membership condition gives a chordal graph on coordinate levels. Its clique tree has at most three leaves. Consequently \(K\) is a central box \([0,a]\times[0,b]\times[0,c]\), together with at most three disjoint outward arms. Each arm has nested rectangular cross sections, and \(a+b+c\le1\).
2. For an arm based at \(a\), with transverse caps \(B,C\), its contribution to \(\int_K[3(x+y+z)-2]\) is bounded by
   \[
   U(a;B,C)=\max_{0\le x\le B,\,0\le y\le C}
   \left[\frac{3a-1}{2}(1-a-x-y)xy+Q(x,y)\right],
   \tag{3}
   \]
   where \(Q\) is the exact optimal boundary-tail integral. This is the new arbitrary-horn bridge. Endpoint convexity first gives tight slabs. A sign argument moves the early part onto an L-shaped path; exact jump-gain identities then eliminate or merge every jump except the initial one. This handles underfilled caps, arbitrary central slack, and multiple off-boundary plateaus.
3. The second new theorem proves
   \[
   U(a;b,c)+U(b;a,c)+U(c;a,b)
   \le abc\left[2-\frac32(a+b+c)\right].
   \tag{4}
   \]
   The larger effective cap can be retained at its full value. For saturated central boxes, only the smallest-base arm needs optimization; three explicit positive polynomial identities settle it. Increasing the height allowance cannot decrease the joint deficit, which proves the result for all central slack.
4. The central box contributes exactly
   \[
   abc\left[\frac32(a+b+c)-2\right].
   \]
   Adding (3) and (4) makes the total integral nonpositive, proving (2).

The boundary-horn formula, all six identities in the arbitrary-horn bridge, and the 44 positive monomials in the joint bound have exact rational checkers. The analytic transformations were also checked separately; polynomial identities alone would not establish their validity.

## 3. The unconditional multiplicity consequence

**Theorem B.** If a four-generator preferred Apéry ideal has no interior corner, then
\[
\boxed{m\ge1837\quad\Longrightarrow\quad W_4(S)>0.}
\tag{5}
\]

The proof uses the endpoint correction rather than dropping it. Put
\[
u_i=a_i/M,\quad v=\min u_i,\quad s=u_1+u_2+u_3,
\quad\kappa=D/(mM).
\]
Unit thickening has normalized continuous deficit
\[
\kappa_c=\frac{\kappa+s}{1+s}\ge\frac13
\]
by Theorem A. If \(W_4\le0\), (1) implies \(\kappa<v\). The earlier phase estimate, proved for every finite lower ideal containing the coordinate unit vectors, is
\[
s(1-3\kappa)\le4\kappa+5v-3\kappa v+4v^2.
\]
When \(v<1/3\), substitution and monotonicity yield
\[
\frac13\le\kappa_c
<\frac{2v(5-v)}{1+6v+v^2},
\qquad
\frac1v<12+\sqrt{137}<24.
\]
When \(v\ge1/3\), the last weaker bound is immediate. Every exponent in \(T\) therefore has total degree at most 23.

The central-box and three-arm description bounds the number of such exponents by 1836. This last constant comes from a small exact integer maximization over central triples and feasible rectangular slices. Two separate computations reproduce the maximum. Hence \(W_4\le0\) forces \(m\le1836\), proving (5).

The published result through multiplicity 19 means any **negative** case in this subclass must have
\[
\boxed{20\le m\le1836.}
\tag{6}
\]
This interval is not asserted to have been exhausted. It also does not apply to the one-interior-corner class.

## 4. Further completed integer and arithmetic results

**Theorem C, equal weights.** For a finite no-interior lower ideal \(T\subset\mathbb N^3\), containing the coordinate unit vectors, let \(R=\max_T|x|_1\). Then
\[
|T|\ge30\quad\Longrightarrow\quad
3|T|R-4\sum_{x\in T}|x|_1\ge|T|.
\tag{7}
\]
Theorem A handles \(R\ge9\). Exact dynamic programming handles \(R=5,6,7,8\), and the cardinality bound for \(R\le4\) is 29. The recurrence enumerates every nested rectangular arm, not a sampled family of shapes. This theorem does not substitute equal weights for the unequal generators in (1).

**Theorem D, a secondary family.** Let \(A=\langle a,b\rangle\), \(B=\langle c,d\rangle\) be two-generated numerical semigroups, and \(p,q\) coprime positive integers. Suppose \(S=pA+qB\) is minimally four-generated and
\[
A/q=B/p=R_g=\langle3,3g+1,3g+2\rangle,\qquad g\ge1,
\]
with the paired interior conditions
\[
q(R_g\setminus\{0\})\subseteq a+b+A,
\qquad
p(R_g\setminus\{0\})\subseteq c+d+B.
\]
Then
\[
\boxed{W_4(S)\ge1.}
\tag{8}
\]
Here \(A/q=\{z\in\mathbb N:qz\in A\}\). The proof uses a complete positive integer parameterization, an exact residue transversal, fiber counts, a genus upper bound, and two self-dual fibers supplying a Frobenius lower bound. Exact positive coefficient certificates prove the final inequalities for every parameter, including unbounded \(g\). Independent programs reproduce 256 coefficients for \(g=1\) and 2,048 coefficients for \(g\ge2\).

For example, \(\langle176,253,288,299\rangle\) has multiplicity 176, eight final-window Apéry points, every triple gcd equal to one, and \(W_4=1942\). It lies inside (6) and beyond the previous six-point and gcd exclusions. The theorem covers its whole stated quotient family; it does not cover arbitrary multiplicity-three quotients.

**Corollary E, all remaining secondary cases.** For any paired secondary case with common quotient \(R\), a negative Wilf number would force
\[
\boxed{c(R)\le40.}
\tag{9}
\]
The conductor here belongs to the common quotient, not to \(S\). The pure critical relation places these semigroups in the no-interior class. The interior conditions and the two-generator Frobenius formula imply, with \(C=c(R)\),
\[
m\ge(C+1)(C+3).
\]
Combine this with \(m\le1836\), since \(42\cdot44=1848>1836\). The argument applies to every remaining secondary counterexample; it does not require choosing one with minimum conductor.

## 5. Why this is not a four-generator proof

There are two distinct unresolved classes.

**No interior corner, unequal weights.** A sufficient unproved strengthening of (7) is
\[
|T|\ge30\quad\Longrightarrow\quad
3|T|M-4\sum_{x\in T}a\cdot x
\ge a_{\min}(|T|-1).
\tag{10}
\]
For genuine Apéry ideals \(a_{\min}>|T|\), so this would settle that range. It would still leave small cardinalities not covered by the published multiplicity bound. Bounded integer and rational weight diagnostics found no counterexample to (10), but they do not prove it. The applicable residual interval remains (6).

**One interior corner.** Theorem A cannot be extended unchanged to this class. Let
\[
U=\{(x,y,z)\ge0:x+y\le1,\ x+z\le1,\ y+z\le1\},
\qquad K=U\setminus[1/10,\infty)^3.
\]
Exact integration gives
\[
\frac{\mathbb E_K[x+y+z]}{\sup_K(x+y+z)}
=\frac{165}{244}>\frac23.
\]
There are finite box versions of this obstruction. They are counterexamples to a proposed geometric extension, not numerical semigroup counterexamples: residue-injectivity constraints can exclude them. No argument here proves that those arithmetic constraints exclude every harmful one-corner shape.

Changing the preferred factorization order does not avoid the issue. For example, \(\langle155,1552,1647,1651\rangle\) has unique factorizations for all 155 Apéry elements and an unavoidable excluded corner \((1,7,4)\); its final window has seven points. This semigroup satisfies Wilf, but no tie-breaking order moves it into the no-interior theorem.

The previous general finite reduction remains available, including the bound \(m<2\times10^{14}\) for a negative four-generator case. Neither that finite reduction nor the stronger subclass bound (6) proves that the remaining finite collection is empty.

## 6. Verification and reproducibility

The companion archive preserves the proof notes, separate audits, exact checkers, and diagnostic outputs. Run

```bash
python3 round4/verify_completed_results.py
```

from the extracted archive. Its proof-certificate checks need only Python's standard library. Exploratory optimization files are separately labeled and may require NumPy, SciPy, or SymPy; they are not dependencies of the completed proofs. Bundled third-party installations are excluded.

The runner checks finite algebra and integer recurrences. Reading the analytic reductions is also necessary. It does not enumerate all remaining four-generator numerical semigroups and it does not certify unrestricted Wilf.

## 7. Primary background references

- Michael Hellus, Anton Rechenauer, and Rolf Waldi, [*Variants on a question of Wilf*](https://arxiv.org/abs/1804.06141): preferred exponent ideals and excluded-corner structure.
- Jonathan Kliem and Christian Stump, [*A new face iterator for polyhedra and more general finite locally branched lattices*](https://arxiv.org/abs/1905.01945): verification at multiplicity 19, extending the earlier verified range.
- Shalom Eliahou, [*Wilf's conjecture and Macaulay's theorem*](https://arxiv.org/abs/1703.01761): the conductor range \(c\le3m\).
- Alex Zhai, [*An asymptotic result concerning a question of Wilf*](https://arxiv.org/abs/1111.2779): fixed-embedding-dimension asymptotic background.
- Kazimierz Chomicz, [*The type and cardinality of minimal presentations of numerical semigroups with embedding dimension four*](https://arxiv.org/abs/2609.04000): primary and secondary structure.
- Jean R. S. Blair and Barry Peyton, [*An Introduction to Chordal Graphs and Clique Trees*](https://people.math.binghamton.edu/zaslav/Oldcourses/580.S13/blair-peyton.chordal-graphs-clique-trees.ornl1992.pdf): the clique-tree theorem used in the geometric decomposition.

The sources provide background and stated prior results. The new arguments in this report are supported by their displayed proofs and certificates, not by attributing them to these papers.
