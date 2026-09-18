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


---

# Appendix A. The clique-tree and three-arm decomposition

This structural argument is retained from the preceding checkpoint. Its former references to an unproved mean bound are superseded by Appendices D–E; no change to the structural hypotheses is needed.

## 1. A chordal graph encodes the maximal boxes

For coordinate i let h_i be its largest axis exponent. Introduce graph vertices (i,r), 0<=r<=h_i. Vertices from the same coordinate class are all adjacent. Vertices (i,r),(j,s), i!=j, are adjacent exactly when r e_i+s e_j belongs to T. The zero vertices are universal.

Within one coordinate class, the external neighborhood of a lower level contains that of any higher level. This is downward closure.

Every induced cycle of length at least four would repeat a coordinate class. Since that class is a clique, its repeated vertices must be exactly two adjacent cycle vertices. Name their levels r<s. The other cycle neighbor of (i,s) lies outside this class and is also adjacent to (i,r), by nested external neighborhoods. That edge is a chord, a contradiction. Thus the graph is chordal.

A maximal clique contains every level below each of its coordinate maxima. Its three maxima form a point of T, by pairwise determination. Conversely, every point of T gives the clique consisting of the three coordinate prefixes. Hence maximal graph cliques correspond bijectively to maximal points z of T, or equivalently to their boxes B_z=[0,z] intersected with N^3.

The clique-tree theorem for chordal graphs therefore supplies a tree on these maximal boxes such that the boxes containing any graph vertex form a connected subtree. In particular, for every coordinate i and level r,

  {z maximal in T:z_i>=r}

is a connected subtree. Intersections of connected subtrees of a tree are connected, so the boxes containing any point x also form a connected subtree.

## 2. Exact tree inclusion-exclusion

Let E be the edges of such a tree, and let z meet z' denote the coordinatewise minimum. Since a nonempty finite tree has one more vertex than edge, pointwise counting gives

  1_T = sum_z 1_{B_z} - sum_{zz' in E} 1_{B_(z meet z')}.

Consequently

  |T| = sum_z prod_i(z_i+1) - sum_{zz' in E} prod_i(min(z_i,z'_i)+1),

and, for any positive weights a,

  sum_T a.x = (1/2) [sum_z |B_z| a.z
                    -sum_{zz' in E} |B_(z meet z')| a.(z meet z')].

The same identity holds for the union of the corresponding continuous boxes and its volume and first moments. Thus the general inclusion-exclusion over exponentially many subsets reduces to tree vertices and edges.

## 3. At most three leaves and a three-arm description

If z is a leaf with neighbor z', then z_i>z'_i for some coordinate i, since distinct maximal points are incomparable. The connected-superlevel-set property implies that z_i exceeds the value of coordinate i at every other node: otherwise the path to another such node would cross z'. Different leaves cannot use the same coordinate. Therefore the clique tree has at most three leaves; it is a path or a tripod, aside from the single-box case.

Choose one node where each coordinate reaches its global maximum, and let z0 be the median of those three nodes in the tree. Every component beyond z0 contains at most one of the three chosen maximum nodes. Along an arm toward the maximum of coordinate i, coordinate i is nondecreasing and the other two coordinates are nonincreasing, by connectedness of every coordinate superlevel set. The increasing coordinate is strictly increasing between consecutive nodes, since otherwise the later maximal point would be dominated by the earlier one.

After thickening to boxes, or after any positive diagonal coordinate scaling, this yields a central box [0,c_1]x[0,c_2]x[0,c_3] and at most three disjoint arms. Arm i lies beyond x_i=c_i and below the other two central coordinate bounds. Each cross section perpendicular to its outward coordinate is a rectangle, and its two side lengths are nonincreasing functions of the outward coordinate.

This reduces the unproved full continuous mean bound to an inequality for a central box plus at most three rectangular-fiber arms. The arms' intersections are exactly contained in the central box.


---

# Appendix B. Exact optimization of boundary horns

The formulas below use maximum height one. Positive scaling gives the height-M formula in Appendix E. The earlier full-cap theorem is also preserved in the source archive.

## 1. Exact optimization of a boundary horn

Let its two caps be `B>=C>=0`, with `R=B+C<=1`. Reverse time by setting `r=1-t`, so `0<=r<=R`. The boundary condition is `u+v=r` and both profiles are nondecreasing in `r`.

We may sort the two side lengths pointwise. Their product and sum stay unchanged; the larger sorted length is still at most `B`, the smaller is at most `C`, and both remain nondecreasing. Let `d` be their nonnegative difference. Then `d` is 1-Lipschitz and

`L(r)=max(0,r-2C) <= d(r) <= U(r)=min(r,2B-r)`.

The boundary contribution is

`Q=∫_0^R (2-3r)(r²-d(r)²)/8 dr`.

The coefficient of `d²` changes sign at `r0=2/3`.

If `R<=r0`, the maximizing profile minimizes `d` everywhere, so `d=L`.

If `R>=r0`, fix `v=d(r0)`. For `r<r0`, the smallest feasible difference is

`d_-(r)=max(L(r),v+r-r0)`.

For `r>r0`, the largest feasible difference is

`d_+(r)=min(U(r),v+r-r0)`.

These bounds follow directly from the 1-Lipschitz condition. They are attained simultaneously: both displayed functions are 1-Lipschitz, remain between `L` and `U`, and meet at `v`. The first maximizes the integrand where the coefficient is nonnegative, and the second where it is nonpositive. Thus they maximize the whole integral among profiles with the given value at `r0`.

Putting `q=(r0-v)/2`, the resulting profiles have the following one-tent form:

- for `0<=r<=2q`, the two side lengths are both `r/2`;
- for `2q<=r<=B+q`, they are `q` and `r-q`;
- for `B+q<=r<=B+C`, they are `B` and `r-B`.

Here `0<=q<=C`. The feasible envelope parameters when `R>=r0` form the smaller interval

`max(0,r0-B)<=q<=min(C,r0/2)`.

The integral of this one-tent profile, denoted `I(q;B,C)`, satisfies the exact derivative identity

`∂I/∂q = (B-q)²(1-B-2q)/2`.

Therefore its unrestricted maximum on `[0,C]` occurs at

`q*=min(C,(1-B)/2)`.

When `R>=r0`, this value lies in the feasible envelope interval: `B>=1/3` gives `(1-B)/2<=1/3` and `(1-B)/2>=2/3-B`; the condition `B+C>=2/3` handles the endpoint `q*=C`. When `R<=r0`, `B+2C<=3R/2<=1`, so the formula gives `q*=C`, agreeing with the earlier direct maximization.

This proves the boundary optimum for every pair of caps.

## 2. Gain over the balanced capped profile

The usual capped-balanced boundary profile is the endpoint `q=C`. Improvement is possible exactly when `B+2C>1`.

Put `w=B+2C-1` and `y=B-C`. Integrating the displayed derivative gives

`I((1-B)/2;B,C)-I(C;B,C)`

`= w²y²/8+w³y/24+w⁴/192`.

If `w<=0`, the gain is zero. Thus the exact gain is

`g(w_+,y)`, where `g(z,y)=z²y²/8+z³y/24+z⁴/192`.

For example, `B=C=2/5` gives gain `1/120000`. This is the explicit obstruction to assuming a capped-balanced taper is always optimal.


---

# Appendix C. Endpoint convexity and the late-horn theorem



Normalize the maximum height to `M=1`. Let a horn start at outward
coordinate `a>=1/3`, with transverse caps `B,C>=0` satisfying
`a+B+C<=1`. Its transverse fibers are rectangles with nonincreasing side
lengths `f(t)<=B`, `g(t)<=C`, and satisfy `t+f(t)+g(t)<=1`.
The moment defect of the horn is

\[
\mathcal J_H=\int f(t)g(t)
  \left(3t+\frac32(f(t)+g(t))-2\right)dt.
\]

Write `x=min(B,C)`, `y=max(B,C)`, and define

\[
J(x,y)=\frac{x^3}{6}-\frac{x^4}{4}
 +\frac{xy^2}{2}-\frac{3x^2y^2}{4}-\frac{xy^3}{2},
\]

\[
\boxed{H(a;x,y)=J(x,y)
 +\frac{xy}{2}(1-a-x-y)(3a-1).}
\]

Then the universal bound is

\[
\boxed{\mathcal J_H\le H(a;x,y).}
\]

Equality is attained by holding the full caps constant from `t=a` to
`t=1-x-y`, then holding the smaller cap fixed while decreasing the larger
cap until they agree, and finally decreasing both equally to zero along
the height boundary. Central slack is allowed in this theorem.

## 1. Endpoint normalization for finite staircase horns

Suppose the horn has constant fibers `(f_j,g_j)` on intervals
`(t_(j-1),t_j]`, where `t_0=a`. Put `p_j=f_j g_j` and `s_j=f_j+g_j`.
The endpoint constraints are

\[
a\le t_1\le\cdots\le t_N,
\qquad t_j\le1-s_j.
\]

For fixed side lengths, the objective is

\[
\sum_j p_j(t_j-t_{j-1})
 \left(\frac32(t_j+t_{j-1}+s_j)-2\right).
\]

After collecting endpoint terms, this is a separable convex quadratic:
the quadratic coefficient of `t_j` is `3(p_j-p_(j+1))/2>=0`, where
`p_(N+1)=0`. A maximum on the compact endpoint polytope occurs at a vertex.

At a vertex, after deleting zero-length intervals, each surviving interval
ends at its height bound `t_j=1-s_j`. Indeed a block of equal endpoints
that touches neither `a` nor an upper bound could be moved slightly in both
directions, contradicting extremality. The upper bounds `1-s_j` are
nondecreasing, so a nonzero interval's active bound is its own upper bound.

Thus it suffices to bound staircase horns with every surviving right
endpoint on the height boundary.

## 2. Filling the tail has the correct sign here

Keep the first constant rectangle, with caps `(b,c)`, from `a` to its tight
right endpoint `1-b-c`. Between every subsequent pair of tight endpoints,
interpolate the two side lengths monotonically so that `f+g=1-t`.
Linear interpolation suffices. It lies above the original constant
rectangle on that interval.

Set `u=1-t`. If the original rectangle has product `p_0` and side sum `s`,
the interpolated rectangle has product `p>=p_0`, and the pointwise gain in
moment-defect integrands is

\[
(p-p_0)\left(1-\frac32u\right)+\frac32p_0(u-s)\ge0.
\]

Both terms are nonnegative because `u<=1-a<=2/3` and `u>=s`. Extend the
last tight rectangle to zero along the boundary as well; its added defect
is nonnegative for the same reason.

On this boundary tail the defect integrand is
`fg(1-3u/2)`, with nonnegative coefficient. For fixed `u=f+g` and starting
caps `(b,c)`, the product is maximized by keeping the smaller cap fixed
until the two sides balance, then reducing them together. This pointwise
maximizer is a valid nested profile. Consequently the original horn is
bounded by `H(a;min(b,c),max(b,c))`.

## 3. The full caps maximize the potential

For `x<=y`, write `r=1-a-x-y>=0`. Direct differentiation gives

\[
H_y=\frac{x r}{2}\bigl(3(a+y)-1\bigr),
\]

\[
H_x=\frac12\left[(a-x)(x-y)^2
       +r\bigl(x^2+2ay-yr\bigr)\right].
\]

The first derivative is nonnegative because `a>=1/3`. Also
`x<=(1-a)/2<=a` and `r<=1-a<=2a`, so every term in the second derivative
is nonnegative. Symmetry handles an interchange of the ordered caps.
Thus the potential is nondecreasing in both transverse caps. Replacing
the first rectangle's caps with the full bounds `(B,C)` proves the theorem.

General bounded monotone profiles follow by approximation with finite
step profiles from below and convergence of their volumes and first
moments. The finite staircase case already includes the cell unions
arising from finite lower ideals.


---

# Appendix D. The arbitrary-horn bridge



**Status:** complete analytic proof; independently audited by two separate reviewers.
The companion exact coefficient checker passes all six identities used below.
This proves a geometric horn reduction, not Wilf's conjecture by itself.

Normalize maximum coordinate sum to one. Fix `a,B,C>=0` with
`a+B+C<=1`. A horn based at `a` has nested rectangular fibers
`f(t)<=B`, `g(t)<=C`, and `t+f(t)+g(t)<=1`. Write

\[
J_H=\int f(t)g(t)\left(3t+\frac32(f(t)+g(t))-2\right)dt.
\]

For caps `(x,y)`, let `Q(x,y)` denote the supremum of this objective over
continuous monotone profiles on the height boundary, starting at
`t=1-x-y` with caps `(x,y)` and ending at zero. This is the previously
proved exact boundary potential; its formula is not needed in the proof
below. The value zero is available by taking a zero cap.

## Theorem

\[
\boxed{J_H\le
\max_{0\le x\le B,\;0\le y\le C}
\left[\left(1-\frac32(1-a)\right)
(1-a-x-y)xy+Q(x,y)\right].}
\]

Thus every arbitrary horn is dominated by one initial constant slab with
effective caps, followed by a continuous boundary horn. The first slab
runs from `a` to `1-x-y`. The theorem allows strict central slack.

The already proved late-horn theorem handles `a>=1/3`. We prove the
remaining case `a<1/3`.

## 1. Exact transition and interpolation formulas

Set `A(r)=1-3r/2` and reverse time `r=1-t`. The endpoint-convexity lemma
reduces any finite step horn to an endpoint-tight staircase of at least
its objective. If consecutive tight cap sums are `r>s`, and the later
rectangle is `(x,y)` with `x+y=s`, its exact slab payoff is

\[
A(r)(r-s)xy.\tag{1}
\]

The initial reverse time is `r_0=1-a`; the initial rectangle need not fill
its caps, so there need not be a rectangle at `r_0`.

On a boundary branch with one transverse side fixed at `c`, replace a
continuous segment of length `d` in the other side by one tight slab.
The **jump gain over continuity** is

\[
g_c(d)=\frac c4d^2(2d+3c-2).\tag{2}
\]

It depends only on the jump length, not its location along the branch.
Also

\[
g_c(d+e)-g_c(d)-g_c(e)
 =\frac{3c}{2}de\left(d+e+c-\frac23\right).\tag{3}
\]

Both identities follow by integrating `c(r-c)A(r)` along the boundary.

## 2. The negative part can be moved to an L-shaped boundary path

Sort transverse coordinates at every state, and sort the original caps,
so `B<=C` and every actual state is `(x_i,y_i)` with `x_i<=y_i`.
Sorting preserves nesting, cap bounds, sums, products, and objective.

If every nonzero slab ends at reverse time greater than `2/3`, every slab
has nonpositive payoff by (1), so the empty horn dominates. Otherwise,
let `(u,v)`, `u<=v`, be the first staircase state with
`t:=u+v<=2/3`. From this state onward the late boundary bridge applies.
Replace that tail by the capped-balanced continuous boundary profile
with value `P(u,v)`. In particular `u<=1/3`.

All preceding slab coefficients `A(r_previous)` are nonpositive. For
any preceding state of sum `s>=u+v`, nestedness and caps imply

\[
x\ge u,\qquad y\le C,\qquad x\le y.
\]

Consequently the smallest possible product at that sum is attained at

\[
x_*(s)=\max(u,s-C),\qquad
 y_*(s)=\min(C,s-u).\tag{4}
\]

Indeed `x(s-x)` is nondecreasing for `x<=s/2`, and (4) is its smallest
feasible `x`. This state is feasible: `x_*<=B`, `y_*<=C`,
`x_*<=y_*`, and both coordinates are nondecreasing in `s`.
At `s=u+v`, it equals `(u,v)`. Replacing every earlier state using (4)
therefore preserves nesting and weakly increases every early slab payoff.

All actual states now lie on the L path

\[
(B,C)\longrightarrow(u,C)\longrightarrow(u,u),
\]

followed by the balanced diagonal to zero. Its first branch holds `C`
fixed, and its second holds `u` fixed. The initial reverse time can be
represented formally by the virtual state `(x_0,C)`, where

\[
x_0=r_0-C\ge B.
\]

The part with first coordinate above `B` is only a device for computing
jump gains: the first actual jump necessarily covers it. Every profile
constructed below retains a first jump of length at least `x_0-B`, unless
it is replaced by an explicitly admissible one-slab profile.

## 3. Jumps wholly on the smaller-side branch can be filled

A jump on the branch with fixed side `u` has length

\[
d\le C-u\le1-2u.
\]

The last inequality uses `C+u<=B+C<=1`. Hence

\[
2d+3u-2\le-u\le0,
\]

so (2) shows its gain is nonpositive. Replace all such jumps by
continuity. The balanced tail is already continuous. At most one jump
can cross the turn of the L path.

## 4. A cross-turn jump reduces to the turn or to balance

Suppose a cross-turn jump starts at `(u+p,C)`, ends at `(u,C-q)`, and is
followed by the continuous smaller-side branch and balanced tail. Here
`p,q>=0` and `q<=C-u`. Its gain over the L-shaped continuous path between
those endpoints is

\[
\begin{aligned}
G(p,q;u,C)=\frac14\bigl(&3C^2p^2+2Cp^3-2Cp^2
 +6p^2qu+6pq^2u+6pqu^2-4pqu\\
 &+2q^3u+3q^2u^2-2q^2u\bigr).
\end{aligned}\tag{5}
\]

Direct differentiation gives

\[
\frac{\partial G}{\partial q}
 =\frac u2(p+q)\bigl(3p+3q+3u-2\bigr).\tag{6}
\]

For fixed `p,u,C`, this derivative changes sign at most once, from
negative to positive. Thus the maximum on `0<=q<=C-u` is attained at
`q=0` or `q=C-u`. The continuous baseline from the jump's start all the
way to zero is independent of `q`, so the same endpoint statement holds
for the whole jump plus its continuation.

The endpoint `q=0` leaves a jump entirely on the first branch, followed
by a continuous tail. It remains to eliminate the balanced endpoint
`q=C-u`.

Let `r` be the reverse time at the start of this balanced-ending jump.
A jump to `(z,z)` followed by the balanced boundary tail has value

\[
F_r(z)=A(r)(r-2z)z^2+\frac23z^3-\frac32z^4.
\]

Its derivative factors as

\[
F_r'(z)=-6z\left(z-\frac r2\right)
                 \left(z-r+\frac23\right).\tag{7}
\]

On every interval `0<=z<=L<=r/2`, this derivative changes sign at most
once, from negative to positive. Therefore

\[
F_r(z)\le\max\{0,F_r(L)\}.\tag{8}
\]

There are two cases.

* **The cross-turn jump is not the initial jump.** Its starting state is
  an actual state `(x,C)`, with `x<=B<=C` and `r=x+C<=1`. Take `L=x` in
  (8). The value `F_r(x)` is a jump along the fixed-`x` branch from
  `(x,C)` to `(x,x)`, followed by the balanced tail. By Section 3 this is
  bounded by its continuous capped-balanced boundary value `P(x,C)`.
  Thus the cross-turn jump and all its continuation are bounded by
  `max(0,P(x,C))`. If the zero alternative is used, all earlier slabs
  were in the negative part, and their sum is nonpositive; the entire
  horn is dominated by zero. Otherwise replace this jump and tail by
  the continuous profile with value `P(x,C)`.

* **The cross-turn jump is the initial jump.** Its formal start may have
  `x_0>B`. Apply (8) with `r=r_0` and `L=B`; this is valid because
  `B<=C` and `B+C<=r_0` imply `B<=r_0/2`. The zero alternative again
  suffices, or `F_(r_0)(B)` is attained by one initial slab to `(B,B)`
  followed by its balanced boundary tail. This is an admissible
  one-slab profile and is already bounded by the theorem's envelope.

Consequently, unless a one-slab profile or zero has already dominated
the whole horn, all remaining jumps lie on the first, fixed-`C` branch.

## 5. All remaining jumps merge into one initial jump

The remaining profile consists of jumps and continuous intervals along
a fixed-`C` branch, followed by a continuous boundary tail. Relative to
its wholly continuous baseline, each jump contributes (2).

Retain the first jump, of length `d_0>=x_0-B`, even if its gain is
negative. If `x_0=B` and there is no initial jump, insert a zero-length
initial jump; this changes neither feasibility nor the objective. Replace every later jump of nonpositive gain by continuity.
For each remaining later jump of length `e`, its gain is positive. If
`C<2/3`, positivity implies

\[
e>\frac32\left(\frac23-C\right)>\frac23-C.
\]

If `C>=2/3`, the expression `d+e+C-2/3` is automatically nonnegative.
In either case (3) proves that merging this jump into the initial jump
weakly increases their total gain. Location independence in (2) permits
reordering the finite list of jump lengths and continuous lengths along
this fixed-`C` interval, preserving their total length, so this jump can
be placed directly after the initial jump before merging. This does not
slide a jump through another state while pretending those states remain
fixed; it constructs a new nested boundary/slab profile with the same
continuous baseline and the same individual jump gains. The merged length
never exceeds the total fixed-`C` branch length, and only increases the
initial jump length, so the cap constraint remains satisfied.

After finitely many merges, there is a single initial jump, followed by
an entirely continuous boundary profile. Its effective caps are within
`(B,C)`. Replacing its continuous continuation by the optimal one, with
value `Q`, proves the desired envelope inequality.

## 6. General monotone profiles

Approximate a bounded nested rectangular profile from below by finite
step profiles, preserving its cap and height constraints. Their volumes
and first moments converge by dominated convergence. Every finite step
profile is bounded by the same envelope, as just proved. Passing to the
limit establishes the theorem for arbitrary monotone profiles.

## Scope

The independently proved joint bound in
`../joint_horns/joint_effective_cap_theorem.md` bounds the three one-slab
envelopes against a central box. Together these results complete the
continuous no-interior-corner mean inequality. The present note does not
supply a discrete Wilf argument, and does not treat an interior corner.


---

# Appendix E. The joint effective-cap theorem



**Status: proved, using the already established formula for the optimal continuous boundary horn.** This closes the joint effective-cap inequality. The separate proof in `../bellman/arbitrary_horn_bridge.md` now establishes that arbitrary rectangular horns are dominated by an initial slab and an optimal continuous boundary tail. Together they complete the continuous no-interior mean theorem. They are not a proof of unrestricted Wilf's conjecture.

## Statement

Let `a,b,c>=0`, `S=a+b+c<=M`, where `M>0`. For sorted caps `0<=x<=y` define

\[
P_M(x,y)=\frac{Mx^3}{6}-\frac{x^4}{4}
 +\frac{Mxy^2}{2}-\frac{3x^2y^2}{4}-\frac{xy^3}{2},
\]

\[
g(w,z)=\frac{w^2z^2}{8}+\frac{w^3z}{24}+\frac{w^4}{192},\qquad
Q_M(x,y)=P_M(x,y)+g((y+2x-M)_+,y-x).
\]

The earlier boundary optimization theorem establishes that `Q_M` is the exact maximum boundary-tail contribution. Define the value of one initial slab followed by this tail as

\[
F_M(a;x,y)=Q_M(x,y)+\frac{3a-M}{2}xy(M-a-x-y).
\]

Extend this definition symmetrically in `x,y`. Put

\[
U_M(a;B,C)=\max_{0\le x\le B,\,0\le y\le C}F_M(a;x,y)
\]

whenever `a+B+C<=M`. Then

\[
\boxed{U_M(a;b,c)+U_M(b;a,c)+U_M(c;a,b)
\le abc\left(2M-\frac32S\right).}
\]

In particular `M=1` gives precisely the joint effective-cap inequality that was left open in the previous checkpoint.

## 1. The larger effective cap can be taken at its full value

Write

\[
H_M(a;x,y)=P_M(x,y)+\frac{3a-M}{2}xy(M-a-x-y),\quad x\le y,
\]

and `r=M-a-x-y>=0`. Exact differentiation gives

\[
(H_M)_y=\frac{xr}{2}[3(a+y)-M]. \tag{1}
\]

On the region where the gain is active, `y+2x>=M` and `y>=x` imply `y>=M/3`. The derivative with respect to `y` of the gain is nonnegative: both its arguments `y+2x-M` and `y-x` increase with `y`, and `g` has nonnegative coefficients. Therefore, for fixed `x`, the function `F_M(a;x,y)` first decreases and then increases as `y` runs from `x` to its allowed maximum `B`. Its maximum is at an endpoint.

The diagonal endpoint is also dispensable. If `a+x>=M/3`, (1) and the preceding gain argument show

`F_M(a;x,x)<=F_M(a;x,B)`.

If `a+x<=M/3`, the whole diagonal segment from zero to `x` lies in the region with no gain. Along that segment,

\[
\frac d{dt}H_M(a;t,t)
=-6t\left(t-\frac{M-a}{2}\right)
     \left(t-\left(\frac M3-a\right)\right)\le0.
\]

Hence `F_M(a;x,x)<=0`, and zero is attainable with an effective cap equal to zero. Sorting a pair of effective caps is feasible when the available caps are sorted. Consequently, for `B>=C`,

\[
U_M(a;B,C)=\max_{0\le x\le C}F_M(a;x,B). \tag{2}
\]

No unproved optimization ansatz is used in (2).

## 2. Saturated central boxes: only the smallest-base horn needs optimization

Relabel so that `a<=b<=c`, and first suppose `M=S=a+b+c`.

For the horn based at `b`, formula (2) leaves the small cap `y` in `[0,a]`, with the large cap equal to `c`. Its boundary gain vanishes because `c+2y<=c+2a<=S`. The following derivative identity is useful, with `r=M-base-small-large`:

\[
2(H_M)_x=(\mathrm{base}-x)(x-\mathrm{large})^2
 +r[x^2+2\,\mathrm{base}\,\mathrm{large}-\mathrm{large}\,r]. \tag{3}
\]

Here `base=b`, `large=c`, and `r=a-y`. Every term in (3) is nonnegative because `y<=a<=b` and `r<=a<=b`. Thus this horn attains its maximum at `y=a`. The same argument applies to the horn based at `c`, whose large cap is `b` and whose small cap lies in `[0,a]`. Both full-cap values are nonnegative, since their value at a zero small cap is zero and they are nondecreasing.

It remains to prove, for every `0<=x<=b`,

\[
D=\frac{abcS}{2}-F_S(a;x,c)-H_S(b;a,c)-H_S(c;a,b)\ge0. \tag{4}
\]

## 3. Three explicit positive polynomial certificates prove (4)

All variables `p,q,r,s` in this section are nonnegative. Each displayed expression is an exact homogeneous polynomial identity. The companion standard-library checker expands the defining formulas and verifies every coefficient exactly.

**Case A: no gain, `x<=a`.** Substitute

`x=p`, `a=p+q`, `b=p+q+r`, `c=p+q+r+s`.

Then

\[
\begin{aligned}
D={}&\frac34p^2(q+r)^2
 +\frac12p(q+r)^2(s+r+2q)\\
 &+q^2\left[\frac{(s+2r)^2}{4}
       +\frac23q(s+2r)+\frac12q^2\right]\ge0.
\end{aligned}
\]

**Case B: no gain, `a<=x<=b`.** Substitute

`a=p`, `x=p+q`, `b=p+q+r`, `c=p+q+r+s`.

Then

\[
\begin{aligned}
D={}&\frac34p^2r^2+\frac12pr^2(s+r+2q)
 +\frac12qr^2(s+r)\\
 &+q^2\left[\frac{(s+2r)^2}{4}+\frac{r^2}{4}\right]
 +\frac13q^3(s+2r)+\frac16q^4\ge0.
\end{aligned}
\]

**Case C: active gain.** Its condition is `c+2x>=S`, equivalently `x>=(a+b)/2`. Substitute

`a=p`, `x=p+2q+r`, `b=p+2q+2r`, `c=p+2q+2r+s`.

Then the deficit including the gain is

\[
\begin{aligned}
D={}&\frac34p^2r^2+\frac12pr^2(s+3r+4q)\\
&+s^2\left(\frac14r^2+qr+\frac12q^2\right)\\
&+s\left(\frac{11}{6}r^3+7qr^2+7q^2r+\frac73q^3\right)\\
&+\frac{31}{12}r^4+\frac{34}{3}qr^3+\frac{33}{2}q^2r^2
 +\frac{31}{3}q^3r+\frac{31}{12}q^4\ge0.
\end{aligned}
\]

These three cases exhaust (4). They prove the saturated theorem, including arbitrary effective small caps. In expanded form they have respectively 16, 12, and 16 positive rational monomials.

## 4. Increasing the height allowance cannot worsen the joint deficit

Keep `a<=b<=c` and fixed effective small caps

`0<=x<=b`, `0<=y<=a`, `0<=z<=a`.

By (2), the respective large caps are `c,c,b`. Let `M=S+delta`, with `delta>=0`. Define the canonical joint deficit

\[
G(M)=abc\left(2M-\frac32S\right)
-H_M(a;x,c)-H_M(b;y,c)-H_M(c;z,b).
\]

An exact expansion gives

\[
G(S+\delta)=G(S)+\delta L+
\frac{\delta^2}{2}(cx+cy+bz), \tag{5}
\]

where

\[
L=2abc-f_a(x)-f_b(y)-f_c(z),
\]

\[
\begin{aligned}
f_a(x)&=\frac{x^3}{6}+\frac{cx^2}{2}+c(a-b)x,\\
f_b(y)&=\frac{y^3}{6}+\frac{cy^2}{2}+c(b-a)y,\\
f_c(z)&=\frac{z^3}{6}+\frac{bz^2}{2}+b(c-a)z.
\end{aligned}
\]

All three functions are convex on their intervals. The last two are nondecreasing, so they attain their maxima at `a`. The first attains its maximum at `0` or `b`. At these two alternatives, the resulting lower bounds for `L` are respectively

\[
2abc-f_b(a)-f_c(a)
=a^2\left(\frac{b+c}{2}-\frac a3\right)\ge0
\]

and

\[
2abc-f_a(b)-f_b(a)-f_c(a)
=\frac{(b-a)^2[2(b-a)+3(c-b)]}{6}\ge0.
\]

Therefore `L>=0`, and (5) shows the canonical deficit is nondecreasing with the height allowance.

The only possible boundary gain is on the horn based at `a`: the other two have `c+2y<=S` and `b+2z<=S`. Its gain is

`g((c+2x-M)_+,c-x)`.

This is nonincreasing as `M` increases. Subtracting it therefore preserves the monotonicity of the total deficit. At `M=S`, the deficit is nonnegative by Sections 2–3. It remains nonnegative for every `M>=S`. Maximizing each horn independently proves the stated theorem.

## Verification and exact scope

Run:

`python3 round4/joint_horns/verify_joint_effective_caps.py`

The checker uses exact `Fraction` arithmetic. It verifies the slack expansion, both convex-endpoint identities, three derivative identities, and all 44 positive monomials in the three saturated-case certificates. Its full coefficient output is `joint_effective_caps_certificate.json`.

The resulting theorem permits underfilled initial caps, arbitrary central slack, and every monotone continuous boundary tail. It removes the joint effective-cap optimization gap. The separate arbitrary-horn bridge supplies the reduction of each individual horn to one initial constant slab followed by a boundary tail, including bases below the sign threshold.


---

# Appendix F. The exact discrete phase estimate

For a normalized finite lower ideal, let μ_i=E[u_i X_i] and let δ_i be one minus the weight of the top of the i-coordinate fiber through X. Conditional uniformity gives Eδ_i=1−E[u·X]−μ_i. Summing yields Σ_i Eδ_i=κ, and hence μ_i=(1+κ)/4−Eδ_i. These exact identities justify the uses below.

Let T be a finite lower ideal in N^3 with positive weights u_j, normalized so that max_T u.x=1, and suppose that T contains all three unit vectors. Write

  kappa = 3 - 4 E[u.X], U = max u_j, v = min u_j.

Then

  U(1-7 kappa) <= (1+v)(4 kappa+2v).                 (P)

Thus, whenever kappa<1/7,

  U <= (1+v)(4 kappa+2v)/(1-7 kappa).

This replaces the earlier coarse phase bound U<=400 kappa+20v.

## Proof

Choose distinct coordinate directions j,k of weights U,v. This is possible even if all weights are equal. Let delta_j(x) denote the nonnegative deficit of the j-fiber top containing x. The coordinate-line identity gives

  E delta_j <= kappa,
  mu_k := E[v X_k] >= (1-3 kappa)/4.

Fix a k-fiber of length L. For t=0,...,L-1, its j-top deficits satisfy

  delta_j(t) >= [A-tv]_U,

where [.]_U is the representative in [0,U). Indeed the deficits differ modulo U by exactly -v between successive k-coordinate positions.

For each t and 0<=r<=v,

  [A-tv+r]_U <= [A-tv]_U+r <= delta_j(t)+r.

Integrating and summing gives, for one interval I of length h=Lv,

  integral_I [s]_U ds <= v sum_t delta_j(t)+Lv^2/2.  (1)

For every interval of length h, write h=qU+r, q>=0 an integer and 0<=r<U. Periodicity and the minimum integral over a remainder interval give

  integral_I [s]_U ds >= (qU^2+r^2)/2
                          >= h^2/[2(q+1)]
                          >= Uh^2/[2(h+U)].         (2)

The middle inequality is Cauchy--Schwarz on q copies of U and one copy of r. The first inequality holds because the q complete periods integrate to qU^2/2, while any arc of length r in the residue circle has integral at least r^2/2.

Combining (1)--(2),

  mean_fiber delta_j >= Uh/[2(h+U)]-v/2.

Every fiber satisfies v(L-1)<=1, so h<=1+v. Therefore

  mean_fiber delta_j >= UvL/[2(1+v+U)]-v/2.

Average over k-fibers with weights proportional to their lengths. Since v E L=2mu_k+v,

  E delta_j >= U(2mu_k+v)/[2(1+v+U)]-v/2
            = [2U mu_k-v(1+v)]/[2(1+v+U)].

Now E delta_j<=kappa and mu_k>=(1-3kappa)/4 imply

  4kappa(1+v+U) >= U(1-3kappa)-2v(1+v),

which rearranges to (P). No excluded-corner restriction or residue labeling is needed.


## Summing the two phase inequalities

Use \(d=3\), \(u_i=a_i/M\), \(v=\min u_i\), \(U=\max u_i\),
\(s=u_1+u_2+u_3\), and \(\kappa=D/(mM)\). Choose an index \(k\)
of minimum weight. Write \(\bar\delta_j=\mathbb E\delta_j\).
The preceding sawtooth proof works for each \(j\ne k\), giving
\[
2\bar\delta_j(1+v+u_j)\ge2u_j\mu_k-v(1+v).
\]
Summing both inequalities, and using nonnegativity of every
\(\bar\delta_j\), gives
\[
(s-v)\mu_k\le(1+v+U)(\kappa-\bar\delta_k)+v(1+v).
\]
The exact identity \(\mu_k=(1+\kappa)/4-\bar\delta_k\) yields
\[
\frac{(s-v)(1+\kappa)}4
\le(1+v+U)\kappa+v(1+v)
 +\bar\delta_k[(s-v)-(1+v+U)].
\]
The bracket equals the middle weight minus \(1+v\), hence is
nonpositive: every normalized weight is at most one because the unit
vectors belong to the staircase. Discard that term and use \(U\le s-2v\).
Rearrangement gives the useful bound
\[
\boxed{s(1-3\kappa)\le4\kappa+5v-3\kappa v+4v^2.}
\tag{S1}
\]

Suppose, for contradiction, that \(W_4\le0\). The Apéry identity gives
\[
\kappa=\frac{W_4+m-1}{M}\le\frac{m-1}{M}<\frac{a_{\min}}M=v.
\]
For \(v<1/3\), the quotient on the right of (S1), after division by
\(1-3\kappa\), is strictly increasing in \(\kappa\): its derivative
has numerator \(4+12v+12v^2>0\). Therefore
\[
s<\frac{9v+v^2}{1-3v}.
\]
The continuous thickening has
\(\kappa_c=(\kappa+s)/(1+s)\). This expression is increasing in
both variables for \(\kappa<1\), so
\[
\boxed{\kappa_c<\frac{2v(5-v)}{1+6v+v^2}<10v.}
\tag{S2}
\]


---

# Appendix G. The multiplicity bound 1836



7 September 2026, final update. The formerly conditional input has now been proved by the arbitrary-horn bridge and the joint effective-cap theorem. Consequently the multiplicity bound below is **unconditional within the no-interior subclass**, subject to those proofs. It does not prove unrestricted Wilf. The historical filename is retained for reproducibility.

Let T be a preferred Apéry lower ideal for a minimally four-generated numerical semigroup S with multiplicity m. Its coordinate weights are a_i>m; put

- M=max_{x in T} a·x=c+m−1;
- Σ=sum_{x in T} a·x;
- D=3mM−4Σ;
- W=4n−c, so mW=D−m(m−1).

Assume T has no full-support minimal excluded point. The independent clique-tree theorem gives a central box and at most three rectangular-fiber arms.

## 1. The continuous input, now proved

Every bounded finite-box continuous lower set of this no-interior kind satisfies

    E[w(X)] <= (2/3) max w.

This follows from `../bellman/arbitrary_horn_bridge.md` and `../joint_horns/joint_effective_cap_theorem.md`, using the clique-tree description and the optimal boundary-horn formula. The deductions below use that completed theorem.

## 2. Direct thickening loses a real endpoint correction

Thicken each lattice point x to x+[0,1]^3. The new volume is m, its mean weight is Σ/m+(a_1+a_2+a_3)/2, and its maximum is M+a_1+a_2+a_3. Thus the assumed continuous theorem yields only

    Σ/m <= 2M/3+(a_1+a_2+a_3)/6,

and hence

    W >= M/3−2(a_1+a_2+a_3)/3−(m−1).

The correction cannot simply be omitted. In fact there is an infinite family of no-interior ideals violating the uncorrected discrete mean bound.

For R>=1 let

    T_R={(x,y,z):x+y<=R, x+z<=R, yz=0}.

This is the union of two degree-R planar triangles sharing one axis. All defining excluded constraints have support at most two. With unit weights,

    m=(R+1)^2,
    M=R,
    Σ=R(R+1)(4R+5)/6,
    Σ/m=2R/3+R/[6(R+1)] > 2R/3.

Also

    3Σ−2mM=R(R+1)/2.

Consequently even a proposed correction 3Σ<=(2m+1)M fails for every R>=2. The size of the correction cannot be bounded by one maximum weight. This is an obstruction to a proof shortcut, not a counterexample to Wilf. The family has genuine Apéry realizations treated in the preceding checkpoint; their unequal arithmetic weights restore Wilf.

## 3. A valid phase bridge gives total exponent at most 23

Normalize u_i=a_i/M, set v=min u_i, s=sum u_i, and κ=D/(mM). The unit thickening has normalized deficit

    κ_c=(κ+s)/(1+s).

The continuous mean theorem is exactly κ_c>=1/3.

The previously proved sawtooth estimate, valid for every finite lower ideal containing the coordinate unit vectors, is

    s(1−3κ)<=4κ+5v−3κv+4v².                  (1)

For a nonpositive Wilf number,

    κ=(W+m−1)/M <=(m−1)/M <a_min/M=v.

If v>=1/3, then M/a_min<=3 already. If v<1/3, the right-hand bound for s in (1) is strictly increasing in κ. Substituting κ<v gives

    s<(9v+v²)/(1−3v),
    κ_c<2v(5−v)/(1+6v+v²).

Combining with κ_c>=1/3 yields

    7v²−24v+1<0,
    v>(12−sqrt(137))/7=1/(12+sqrt(137)).

Hence, in both cases,

    M/a_min<12+sqrt(137)<24.

Since a·x>=a_min |x|_1, every x in T has total exponent at most 23. The crude consequence is m<=binom(26,3)=2600.

The input (1) is proved in the previous fixed-dimension checkpoint, in the section "Summing the two phase inequalities". Its proof is independent of no-interior geometry and of the new continuous input.

## 4. The tripod structure improves the cutoff to 1836

For an integer degree limit R, choose the central point c=(c_1,c_2,c_3) supplied by the clique tree. It belongs to T, so c_i>=0 and sum c_i<=R.

Its central box contains at most

    (c_1+1)(c_2+1)(c_3+1)

points. Beyond this box, each point belongs to exactly one arm. In arm i, at outward integer level t>c_i, the remaining coordinates form a rectangle [0,u]×[0,v]. Its caps obey

    u<=c_j, v<=c_k, u+v<=R−t.

Therefore its cardinality is at most

    Q(c_j,c_k,R−t)
      =max_{0<=u<=min(c_j,R−t)} (u+1)(min(c_k,R−t−u)+1).

Summing the disjoint central box and arm layers gives the rigorous bound

    |T| <= B_R(c)
      :=prod_i(c_i+1)+sum_i sum_{t=c_i+1}^R Q(c_j,c_k,R−t).

The bound is invariant under coordinate permutations, so it is enough to enumerate sorted c_1<=c_2<=c_3 with sum c_i<=R. Exact integer evaluation at R=23 gives

    max_c B_23(c)=1836.

A maximizing sorted central triple is (7,7,8); (7,7,9) and (7,8,8) also attain the same bound. The standard-library checker `max_no_interior_size.py` implements exactly the displayed finite formula and supplies the full R=1,...,23 table in `max_no_interior_size_results.json`. The separate checker enumerates all ordered central triples and all feasible rectangle endpoint pairs and obtains the identical maximum.

Thus the conclusion is:

> A four-generator Apéry ideal with no full-support excluded corner and W<=0 has m<=1836. In particular m>=1837 forces strict Wilf in that subclass.

The reduction also applies without residues to the ordered geometric relaxation: if a_1>=m+1, a_2>=a_1+1, a_3>=a_2+1 and D<m(m−1), then κ<v by exactly the same argument. Therefore any such no-interior geometric failure is contained in Δ_23 and has m<=1836. This does not classify those finite shapes.

For genuine semigroups, the previously published small-multiplicity result m<=19 means any negative case remaining in that subclass would have 20<=m<=1836. No enumeration or analytic exclusion of that remaining interval is asserted here. The statement does not apply to ideals with a full-support excluded corner.

## 5. Exact verification and scope

The cutoff is a mathematical consequence of the completed continuous theorem, with a small finite integer computation for its last constant. It does not use floating-point optimizers as proof. The separate exploratory `probe_discrete_mean.py` and `optimize_phase_cutoff.py` scripts are diagnostics only; their numerical results are not inputs to this deduction. The infinite T_R formula already supplies exact counterexamples to the two proposed discrete shortcuts.


---

# Appendix H. The unit-weight integer theorem and weighted scope



7 September 2026. The unit-weight theorem below is proved. The proposed
extension to arbitrary positive weights remains unproved. None of these
results is a proof of four-generator Wilf by itself.

## 1. The completed unit-weight theorem

Let `T` be a finite lower ideal in `N^3`, containing the three coordinate
unit vectors, with no full-support minimal excluded point. Put

\[
m=|T|,\qquad R=\max_{x\in T}|x|_1,\qquad
D_1=3mR-4\sum_{x\in T}|x|_1.
\]

Then

\[
\boxed{m\ge30\quad\Longrightarrow\quad D_1\ge m.}
\]

This is stronger than the unit-weight target `D_1>=m-1`. The theorem uses
the completed continuous no-interior moment theorem and a small exact
integer dynamic program. The recurrence was independently audited; its
correctness, not random or floating-point search, supplies the finite
part of the proof.

### Large degree follows directly from the continuous theorem

Thicken every lattice point to its unit cube. The resulting continuous
no-interior lower set has maximum coordinate sum `R+3`, mean sum
`(sum_T |x|)/m+3/2`, and volume `m`. Its mean is at most `2(R+3)/3`.
Therefore

\[
\frac{D_1}{m}\ge\frac R3-2.
\]

For `R>=9`, this already gives `D_1>=m`.

### Exact recurrence for the remaining degrees

Fix `R` and define the additive score

\[
\Phi_R(T)=\sum_{x\in T}(4|x|_1-3R+1)=m-D_1.
\]

A horn starting at outward integer coordinate `t`, with transverse caps
`B,C`, has a rectangular slice `(u+1)(v+1)` at that level, where
`0<=u<=B`, `0<=v<=C`, and `t+u+v<=R`. The slice's exact score is

\[
(u+1)(v+1)(4t+2u+2v-3R+1).
\]

Let `H_t(B,C)` be the maximum horn score, allowing an empty horn. Then

\[
H_t(B,C)=\max\left(0,
\max_{\substack{u\le B,\,v\le C\\t+u+v\le R}}
\left[(u+1)(v+1)(4t+2u+2v-3R+1)+H_{t+1}(u,v)\right]\right),
\]

with `H_(R+1)=0`. The inner maximum is computed exactly by two-dimensional
prefix maxima. This recurrence considers every nested sequence of
rectangular slices, including arbitrary omissions and slack.

The audited clique-tree theorem writes every no-interior ideal as a
central box `[0,a]×[0,b]×[0,c]` with three disjoint such horns. Conversely
such a construction is a feasible lower ideal with no full-support
excluded corner. Thus the exact maximum of `Phi_R` is obtained by
maximizing

\[
\begin{aligned}
&(a+1)(b+1)(c+1)[2(a+b+c)-3R+1]\\
&\qquad +H_{a+1}(b,c)+H_{b+1}(a,c)+H_{c+1}(a,b)
\end{aligned}
\]

over `a,b,c>=0`, `a+b+c<=R`. Symmetry allows sorting the central triple.

The required exact results are:

| Degree allowance R | Maximum of Phi_R over every nonempty no-interior ideal |
|---:|---:|
| 5 | -4 |
| 6 | -17 |
| 7 | -20 |
| 8 | -23 |

All are negative, so `D_1>=m` in these cases too. The program also records
R=1,...,23, but R>=9 is not needed computationally.

Finally, the independent exact central-box cardinality calculation gives
`|T|<=29` when `R<=4`. It maximizes each feasible horn slice's cardinality
and then sums with the central box. Hence `m>=30` forces `R>=5`, completing
the theorem.

The main exact checker is `unit_weight_dp.py`; its output is
`unit_weight_dp_results.json`. It reconstructs one maximizer and checks
its cardinality, score, downward closure, and absence of an interior
excluded corner. The preceding cardinality checker is
`round4/discrete/max_no_interior_size.py`.

## 2. A general weighted dynamic program is available

For positive integer weights `a=(a_1,a_2,a_3)`, height allowance `M`, and
integer penalty `p`, consider

\[
\Phi_{a,M,p}(T)=\sum_{x\in T}[4a\cdot x-3M+p]=pm-D.
\]

For a horn in coordinate i, at outward integer level t, with remaining
weights beta,gamma and slice `[0,u]×[0,v]`, the exact contribution is

\[
(u+1)(v+1)[4a_it+2\beta u+2\gamma v-3M+p].
\]

Replace the degree constraint in the preceding recurrence by
`a_i t+beta u+gamma v<=M`. The same prefix-maximum recurrence computes the
exact optimum over every no-interior ideal within the weighted height
allowance. Central triples must now be enumerated without sorting,
because unequal weights remove that symmetry.

`weighted_dp.py` implements this recurrence with exact integer arithmetic.
For a fixed cardinality requirement `m>=L`, `weighted_size_dp.py` retains
cardinalities 0,...,L-1 exactly and caps all larger cardinalities at L.
The recurrence adds each slice cardinality and uses the same prefix
maxima; the three horns are combined by capped max-plus convolution.
It uses an integer sentinel for impossible states and reports feasibility
separately. These routines provide fixed-parameter certificates. They do
not establish any universal statement over all real weight triples.

## 3. What was checked about arbitrary weights

The natural open extension is

\[
m\ge30\quad\Longrightarrow\quad
3mM-4\sum_Ta\cdot x\ge a_{\min}(m-1).
\]

For genuine four-generator Apéry ideals, `a_min>=m+1`, so this inequality
would prove Wilf for the no-interior subclass of size at least 30.
It is not proved here.

A potentially simpler open sufficient statement is that, after
normalizing `a_min=1`, every no-interior ideal with `M>=5` satisfies
`m-D<=1`. Together with the degree<=4 cardinality bound, this would imply
the preceding statement. It too is unproved.

Two finite diagnostics were completed:

* All 2,300 integer normalized cases `(a_1,a_2,a_3)=(1,b,c)`,
  `1<=b<=c<=M<=23`. No unconstrained optimum violated `m-D<=1` at `M>=5`.
  Some smaller-height optima violate it; their largest maximizing
  cardinality is 29. The latter observation alone does not exclude a
  smaller positive score at a larger cardinality.
* A structured rational grid with integer weights `(10,b,c)`,
  `10<=b<=20`, `b<=c<=30`, and `40<=M<=90`: 8,976 cases. The target
  `10m-D<=10` for cardinality at least 30 passed in every case. Most
  cases were certified by the unconstrained DP or the exact Lagrange
  bound `max_T(20m-D)-300<=10`; one remaining case was settled by the
  capped-cardinality DP, which found no admissible ideal.

These grids are bounded computations, not proofs for all rational or
real parameters. They produced no counterexample to the open weighted
extension. The diagnostic output files explicitly record their scope.

## 4. Discrete endpoint convexity survives, with a cardinality caveat

For fixed weights, height M, a fixed central box, and a fixed nested
sequence of transverse rectangles in each horn, vary the outward right
endpoints `e_j`. If the rectangle cardinalities are `N_j`, the quadratic
coefficient of `sum_T a·x` at `e_j` is

\[
\frac{a_i}{2}(N_j-N_{j+1})\ge0.
\]

There are no cross terms in that first-moment contribution. Cardinality
m is affine in the endpoints. Consequently the violation functional

\[
4\sum_Ta\cdot x-3mM+m(m-1)
\]

is convex in the endpoint vector: its additional quadratic term is m²,
a positive-semidefinite rank-one form.

Without a cardinality constraint, the integer ordered-endpoint polytope
has integer vertices, so a maximum occurs at an endpoint pattern where,
after coalescing zero-length intervals, each right endpoint is

`floor((M-beta u-gamma v)/a_i)`.

This is a valid discrete extremal reduction for the unconstrained
geometric functional. It does not give a semigroup deformation. Fixing
m or imposing `m<=a_min-1` adds a cardinality constraint and requires
additional analysis; changing endpoints also generally destroys residue
bijection. Those constraints cannot be silently dropped when proving
Wilf for genuine semigroups.


---

# Appendix I. The secondary quotient ⟨3,4,5⟩



7 September 2026. This is a new family argument within the current research session, not an unrestricted four-generator proof. External review remains outstanding.

**Theorem.** Let A=⟨a,b⟩ and B=⟨c,d⟩ be two-generated numerical semigroups, let p,q be coprime positive integers, and suppose S=pA+qB is minimally four-generated. Suppose

A/q=B/p=R=⟨3,4,5⟩,

qR₊⊆a+b+A and pR₊⊆c+d+B.

Then W₄(S)=4n(S)−c(S)≥1.

The common quotient here has precisely the gaps 1,2. The theorem does not cover arbitrary multiplicity-three quotients.

## 1. Positive integer parameters

Write the unique gap representation

q=ab−u a−v b, 0<u<b, 0<v<a.

Because 2q is also a gap, exactly one of 2u>b and 2v>a holds. Interchanging a,b if necessary gives 2u>b. The condition that 3q has a representation using positive coefficients of both generators then implies

b/2<u<2b/3, 0<v<a/3.

Indeed if u≥2b/3 or v≥a/3, the canonical gap representation of 3q either remains a gap or reaches a pure-axis boundary. Similarly the interior representation of 4q gives 4v<a. Put

r=2b−3u>0, h=2u−b>0, z=a−4v>0.

Then r,h,v,z are positive integers and

b=2r+3h, u=r+2h, a=4v+z,
q=(2r+h)v+(r+h)z.

The condition on 5q imposes an additional restriction, but our inequality will hold on the larger domain where all four parameters are merely positive. Apply the same construction to B, using positive integers R₀,H,V,Z:

d=2R₀+3H, c=4V+Z,
p=(2R₀+H)V+(R₀+H)Z.

For completeness, the assertions about the gap boundaries can be checked without an implicit choice of representation. For any positive integer k, a positive-coefficient representation of kq exists exactly when

ceil(ku/b)+ceil(kv/a)≤k,

with a ceiling increased by one when its argument is an integer. This is obtained by choosing the least positive coefficients congruent to −ku modulo b and −kv modulo a. At k=3 and k=4 it gives the strict inequalities above.

## 2. Four normalized residue-fiber types

For each residue modulo q let Aᵢ be its least element in A and put Iᵢ={k≥0:Aᵢ+qk∈A}. Since Iᵢ contains 0 and all integers ≥3, it is one of

T={0,3,4,5,…},
I={0,2,3,4,…},
J={0,1,3,4,…},
N={0,1,2,3,…}.

Two-generator symmetry pairs a fiber K with its normalized dual

K*={k≥0:f(K)−k∉K},

where f(K) is its largest missing integer, with f(N)=−1. Here T*=J, J*=T, I*=I and N*=N. In particular the numbers of T and J fibers are equal. If α_K is the least fiber minimum Aᵢ of type K, symmetry says that the largest minimum of type K* is

F_A−q f(K)−α_K,

where F_A=ab−a−b.

For a positive gap t=ab−u₀a−v₀b, the number of s∈A with s+t∉A is u₀v₀: in the canonical representation s=i a+j b, 0≤i<b, the excluded set is exactly the rectangle i<u₀,j<v₀.

Apply this to q and 2q=ab−h a−2v b. Translation by q has one defect in each T,I,J fiber; translation by 2q has one defect in each T,J fiber. Thus, writing the numbers of T,J fibers as t and of I fibers as s,

2t+s=uv=(r+2h)v,
2t=2hv.

Consequently

#T=#J=hv, #I=rv,
Σᵢ genus(Iᵢ)=v(r+3h).

The corresponding counts for B are HV, R₀V and V(R₀+3H).

## 3. Exact genus and two conductor lower bounds

Let P=pq and X=pF_A+qF_B. The pair of residues of A modulo q and B modulo p indexes the S-residue classes modulo P. Its normalized fiber is the sumset Iᵢ+Jⱼ. The only sumsets with positive genus are

T+T (genus 2), T+I and I+T (genus 1),
T+J and J+T (genus 1), I+I (genus 1).

The residue-offset count therefore gives the exact genus

G(S)=(X+P+1)/2−pv(r+3h)−qV(R₀+3H)+E,

where

E=vV(rR₀+rH+hR₀+4hH).

This uses the general residue formula

G(S)=(X+P+1)/2−pΣgenus(Iᵢ)−qΣgenus(Jⱼ)+Σgenus(Iᵢ+Jⱼ).

We need only two conductor branches, rather than the full maximum over sixteen type pairs.

**Two concrete fiber minima.** The label ha is the least element of a residue fiber of type I, and 2vb is the least element of a fiber of type N. To see minimality, it is enough to check subtraction by q,2q,3q: since 3q∈A, any earlier element at distance kq with k≥4 would imply one of these three predecessors exists. In the canonical representation with a-coefficient between 0 and b−1, each of the following predecessors has negative b-coefficient:

ha−q=−ra+vb,
ha−2q=(−2r−h)a+2vb,
ha−3q=(h−r)a−(v+z)b;

2vb−q=−(r+h)a+3vb,
2vb−2q=ha−zb,
2vb−3q=−ra+(v−z)b.

Reducing a negative a-coefficient modulo b only decreases the b-coefficient by a, preserving negativity. Also ha+q is a gap and ha+2q∈A, so the first fiber is I; both 2vb+q and 2vb+2q belong to A, so the second is N. Thus α_I≤ha and α_N≤2vb. The same bounds hold on the B side.

Symmetry and I+I=I now give

F(S)≥X−P−pha−qHc.

Symmetry and N+N=N give

F(S)≥X+P−2pvb−2qVd.

Taking their arithmetic mean cancels P:

F(S)≥X−½[p(ha+2vb)+q(Hc+2Vd)].

Combining this bound with the exact genus gives

W₄(S)≥1+X−2P+4pv(r+3h)+4qV(R₀+3H)−4E
             −(3/2)[p(ha+2vb)+q(Hc+2Vd)].       (★)

## 4. A four-variable nonnegative polynomial

Normalize

x=r/h, y=z/v, X₀=R₀/H, Y=Z/V,
Q=2x+1+(x+1)y=q/(hv),
P₀=2X₀+1+(X₀+1)Y=p/(HV).

Let f(t)=min(t,1). Positive integrality gives

1/h≤f(x), 1/v≤f(y), 1/H≤f(X₀), 1/V≤f(Y).

After dividing the right side of (★), apart from its constant 1, by hvHV, substitution gives

W₄(S)≥1+hvHV Φ(x,y,X₀,Y),

Φ=P₀ A(x,y)+Q A(X₀,Y)−4(xX₀+x+X₀+4),

A(x,y)=4x+xy+y/2+8−f(x)(4+y)−f(y)(2x+3).

We prove Φ≥0 on the relaxed domain x,y,X₀,Y≥0. Split each variable at 1, yielding sixteen regions. For a lower variable use t=T∈[0,1], and for an upper variable use t=1+T, T≥0. The resulting polynomial has degree at most one in each of the four variables. Expand bounded coordinates in the degree-one Bernstein basis {1−T,T}, and leave unbounded coordinates in the ordinary power basis {1,T}. Every basis function is nonnegative.

The sixteen coefficients on each region are all nonnegative. The exact smallest coefficients for the flags (x,y,X₀,Y), with 0=lower and 1=upper, are:

| Flags | Minimum |
|---|---:|
| 0000 | 0 |
| 0001 | 11/2 |
| 0010 | 7 |
| 0011 | 7 |
| 0100 | 11/2 |
| 0101 | 1 |
| 0110 | 9/2 |
| 0111 | 3/2 |
| 1000 | 7 |
| 1001 | 9/2 |
| 1010 | 7 |
| 1011 | 6 |
| 1100 | 7 |
| 1101 | 3/2 |
| 1110 | 6 |
| 1111 | 2 |

`ordinary_three_certificate.py` constructs Φ using exact rational arithmetic, performs all sixteen conversions, verifies all 256 coefficients, and expands each representation back to the original polynomial. The complete rational data are in `ordinary_three_certificate.json`. This is a finite exact identity certificate, not a parameter search. Consequently Φ≥0, and (★) proves W₄(S)≥1. ∎

## 5. Independent checks and scope

`ordinary_three_checks.py` computes the exact fiber formulas and separately computes semigroup invariants using shortest paths modulo the multiplicity. One hundred minimally four-generated examples with coprime p,q passed the exact genus and conductor comparisons and the lower bound. These checks support the derivation but are not the argument for the unbounded family.

The previously uncovered example A=⟨5,7⟩, q=9, B=⟨5,8⟩, p=11 gives S=⟨45,55,72,77⟩. Its exact invariants are F=395, genus 225 and W₄=288. The intermediate bound (★) already gives W₄≥67.

This theorem extends the completed common-quotient multiplicity-two family to the next ordinary quotient. General quotients of multiplicity three, ordinary quotients of multiplicity at least four, and unrestricted primary four-generator semigroups remain outside these two family arguments.


---

# Appendix J. The secondary family ⟨3,3g+1,3g+2⟩



7 September 2026. Family proof with exact rational certificates and a completed independent in-session audit. External review remains outstanding. This is not the unrestricted four-generator conjecture.

**Theorem.** Let A=⟨a,b⟩ and B=⟨c,d⟩ be two-generated numerical semigroups, p,q coprime, and S=pA+qB minimally four-generated. Assume

A/q=B/p=R_g=⟨3,3g+1,3g+2⟩,
q(R_g)₊⊆a+b+A, p(R_g)₊⊆c+d+B.

Then W₄(S)≥1 for every integer g≥1. The case g=1 is proved separately in `ordinary_three_theorem.md`. We prove g≥2 below. The quotient has genus 2g, so this family has unbounded quotient genus.

## 1. Complete positive parameterization for g≥2

As in the ordinary-three proof, orient the unique gap representation q=ab−ua−vb so that 2u>b. Since q and 2q are gaps but 3q has an interior representation, put

r=2b−3u>0, h=2u−b>0, s=a−3v>0.

Then

b=2r+3h, u=r+2h, a=3v+s,
q=rv+(r+h)s, 3q=ra+sb.

The two gap progressions have the exact representations

(3j+1)q=ab−(r+2h−jr)a−(v−js)b,
(3j+2)q=ab−(h−jr)a−(2v−js)b.

Until either displayed coefficient becomes nonpositive these are canonical gap representations; at the first nonpositive coefficient the value is represented in A and all later values in that progression are represented by adding 3q. Thus the numbers of gaps in the two progressions are respectively

min(ceil(1+2h/r),ceil(v/s)),
min(ceil(h/r),ceil(2v/s)).

Both equal g. For g≥2 this forces ceil(h/r)=ceil(v/s)=g. Indeed if the second minimum attained g through ceil(2v/s) while ceil(h/r)>g, then ceil(v/s)≤ceil(g/2)<g, contradicting the first minimum. Once ceil(h/r)=g, ceil(1+2h/r)≥2g−1>g, so the first minimum forces ceil(v/s)=g. The strict interior conditions at 3g+1 and 3g+2 exclude the upper endpoints. Therefore

h=(g−1)r+α, v=(g−1)s+β,
0<α<r, 0<β<s.

Consequently

a=(3g−2)s+3β,
b=(3g−1)r+3α,
q=(2g−1)rs+rβ+sα.

The same formulas describe B with positive integers R,T,α′,β′, with 0<α′<R and 0<β′<T. Its quotient divisor is p. Normalize

x=α/r, y=β/s, z=α′/R, w=β′/T,
Q=2g−1+x+y=q/(rs), P=2g−1+z+w=p/(RT),
A₀=3g−2+3y=a/s, B₀=3g−1+3x=b/r,
C₀=3g−2+3w=c/T, D₀=3g−1+3z=d/R.

## 2. Exact L-shape of residue minima

Use canonical coordinates ia+jb with 0≤i<b, j≥0. Such a label is the least in its q-residue exactly when none of its predecessors at distances q,2q,3q belongs to A. These three tests suffice because 3q∈A. The gap representations of q and 2q say that absence of the first two predecessors is exactly

i<r+h and j<v+s.

On this rectangle, absence of the third predecessor is i<r or j<s. Thus the residue minima form the disjoint L-shape

0≤i<r+h, 0≤j<s,

or

0≤i<r, s≤j<v+s.

Its size (r+h)s+rv=q also verifies the count.

A normalized fiber has the form

I(H,K)=3N ∪(3H+1+3N)∪(3K+2+3N),

with 0≤H,K≤g. At the minimum ia+jb the two thresholds are

H=max(0,min(ceil((r+2h−i)/r),ceil((v−j)/s))),
K=max(0,min(ceil((h−i)/r),ceil((2v−j)/s))).

Evaluating these on the two rectangles gives the following distribution, divided by rs. Every listed contribution is additive; the ranges do not overlap beyond the explicitly combined entries:

| Threshold pair | Normalized number of fibers |
|---|---:|
| (g,g) | xy |
| (g,k), 0≤k≤g−1 | y |
| (g−1,g) | x |
| (g−1,g−1) | 1−xy |
| (g−1,k), 0≤k≤g−2 | 1−y |
| (h₀,g), 1≤h₀≤g−2 | x |
| (h₀,g−1), 1≤h₀≤g−2 | 1−x |
| (0,g) | xy |
| (0,g−1) | 1−xy |

An empty range contributes nothing. The total is Q. For 1≤j<g, both marginal tail counts, divided by rs, are Q−j. At j=g they are

Pr-count(H≥g)/(rs)=y(g+x),
Pr-count(K≥g)/(rs)=x(g−1+2y).

In particular the normalized sum of fiber genera is

G_A=(g−1)(3g−2)+(3g−3)x+(3g−2)y+3xy.

Write G_B for the analogous expression in z,w.

## 3. A genus upper bound from the marginal tails

For two normalized fibers, direct residue addition gives

I(H,K)+I(H′,K′)=I(min(H,H′,K+K′+1), min(K,K′,H+H′)).

Its genus is at most min(H,H′)+min(K,K′). Therefore the normalized sum of genera of all paired sum fibers is at most

Ē=2[(g−1)PQ−g(g−1)(P+Q)/2+g(g−1)(2g−1)/6]
   +yw(g+x)(g+z)+xz(g−1+2y)(g−1+2w).

This follows by summing the products of the two marginal tail counts at each threshold j=1,…,g.

Set X=p(ab−a−b)+q(cd−c−d) and P_abs=pq. The exact residue genus identity from the ordinary-three proof consequently gives

G(S)≤(X+P_abs+1)/2−p(rs)G_A−q(RT)G_B+(rsRT)Ē.       (1)

## 4. Two self-dual fibers and a Frobenius lower bound

The symmetric numerical semigroup I(t,2t) has Frobenius number 6t−1 and is self-dual. Similarly I(2t+1,t) is symmetric and self-dual, with Frobenius number 6t+1. Each is closed under its own addition.

If g=2t is even, the distribution contains self-dual fibers

U=I(t,g), f(U)=6t−1,
V=I(g−1,t−1), f(V)=6t−5.

The L-shape supplies actual minima of these types with labels at most

ℓ_U=((t−1)s+β)b,
ℓ_V=(tr+α)a+βb.

For g=2 this remains valid, including the boundary index t−1=0.

If g=2t+1 is odd, the self-dual fibers are

U=I(g,t), f(U)=6t+1,
V=I(t,g−1), f(V)=6t−1,

with labels at most

ℓ_U=(tr+α)a,
ℓ_V=αa+(ts+β)b.

Define L_A=(ℓ_U+ℓ_V)/(2rs). Thus

L_A=[(t+x)A₀+(t−1+2y)B₀]/2 if g=2t,
L_A=[(t+2x)A₀+(t+y)B₀]/2 if g=2t+1.

Define L_B analogously.

Two-generator symmetry sends a minimum α_I of a self-dual fiber I to a maximum minimum F_A−q f(I)−α_I. Since I+I=I, pairing the largest such minima from A and B yields

F(S)≥X−P_abs f(I)−pα_I^A−qα_I^B.

Apply this for U and V and average. Their Frobenius numbers have mean 3g−3, so

F(S)≥X−P_abs(3g−3)−p(rs)L_A−q(RT)L_B.       (2)

## 5. Exact positive polynomial certificate

Let f(t)=min(t,1−t) on [0,1]. Positive integrality gives

1/r≤f(x), 1/s≤f(y), 1/R≤f(z), 1/T≤f(w).

Combining (1) and (2) in W₄=3(F+1)−4G and using these inverse-integer bounds yields

W₄(S)≥1+rsRT Ψ,

Ψ=P A₀B₀+Q C₀D₀−2PQ
 −3[PQ(3g−3)+P L_A+Q L_B]
 +4P G_A+4Q G_B−4Ē
 −P[f(x)A₀+f(y)B₀]−Q[f(z)C₀+f(w)D₀].

It remains to show Ψ≥0 for g≥2, 0≤x,y,z,w≤1. For even g write g=2t+2, and for odd g write g=2t+3, with t≥0. Split each of x,y,z,w into its lower and upper half, parametrized by (ε+T)/2, T∈[0,1]. This yields 32 rational polynomials.

Expand each in the ordinary power basis in the unbounded parameter t and the Bernstein basis in the four bounded variables. `quotient_three_progression_certificate.py` constructs every polynomial, converts every coefficient exactly, checks that all 2,048 coefficients are nonnegative, and reconstructs all 32 original polynomials exactly. No floating-point computation appears in this certificate. For the even regions the smallest coefficients are 44, 899/16, or 267/4; for every odd region the smallest coefficient is 272/3. All basis functions are nonnegative on their domains, so Ψ≥0. Therefore W₄(S)≥1. ∎

## Verification and remaining scope

`quotient_three_progression_checks.py` independently computes the q-residue minima of the two-generator sides and their exact fiber types, and compares the resulting distribution with Section 2. It also computes S invariants independently using shortest paths and checks the derived lower bound. The checked quotient parameters include g=2,3,4,5,8,12, with 60 minimally four-generated paired examples in total.

The theorem treats the entire common-quotient family R_g=⟨3,3g+1,3g+2⟩ under the paired interior conditions. It does not treat arbitrary multiplicity-three quotients, whose two nonzero Apéry thresholds can differ, or unrestricted four-generator semigroups.

For a concrete case beyond the earlier six-point and gcd-triple exclusions, g=2 gives S=⟨176,253,288,299⟩, with every triple gcd equal to one, final-window cardinality eight, and W₄=1942. Its multiplicity 176 is also inside the separate residual range m≤1836. For g=12, S=⟨10295,17111,26680,26751⟩ has every triple gcd one, final-window cardinality 36, and W₄=1314401. Exact final-window diagnostics are in `quotient_three_progression_final_windows.json`.

The independent audit is `../secondary_audit/audit_quotient_three_progression.md`. Its separate verifier independently reproduced all 2,048 coefficients, confirmed nonnegativity, and passed 7,776 rational reconstruction checks. The proof of parameter completeness, residue L-shape, full threshold distribution, and both parity-dependent self-dual fiber witnesses was also checked independently.


---

# Appendix K. Composition audit and the quotient-conductor bound 40



7 September 2026. This audit checks compatibility of the component theorems. It does not expand the numerical searches or claim unrestricted Wilf.

## Conclusion

The newly completed components compose correctly. They establish the continuous no-interior moment inequality and the unconditional implication

`no full-support Apéry corner and W_4<=0 => m<=1836`.

For every negative secondary semigroup in the paired-quotient class, they also force the **common quotient's conductor** to be at most 40. This is not a bound of 40 on the conductor of the original four-generated semigroup, and it does not require choosing a conductor-minimal counterexample.

## 1. Structure, horn reduction, and joint inequality have matching hypotheses

The finite clique-tree argument applies to a finite box lower set whose membership is determined by its pair projections. This is exactly the no-full-support-complement-generator condition for the half-open finite-cell model. An arbitrary finite coordinate grid can be compressed to integer levels: the graph and connected-superlevel argument use only coordinate order, so unequal interval widths do not affect the decomposition.

It yields a central anchored box with side lengths `a,b,c>=0` and at most three arms. Each arm lies beyond one central face, remains below the other two central caps, and has nested rectangular fibers. The central box belongs to the set, so `a+b+c<=M`, where `M` is the supremum of total coordinate. Each arm satisfies the same height restriction `t+f(t)+g(t)<=M`.

These are precisely the hypotheses of `round4/bellman/arbitrary_horn_bridge.md`. Positive scaling by `M` transfers its normalization `M=1` to general `M>0`. Its one-slab value is exactly

`Q_M(x,y)+(3a-M)xy(M-a-x-y)/2`,

which is the function `F_M` in `round4/joint_horns/joint_effective_cap_theorem.md`. The boundary potential `Q_M` in both statements is the same sorted-cap one-tent optimum from `round3/horns_optimization/fullcap_boundary_theorem.md`. The earlier false balanced-taper ansatz is not reinstated: the extra boundary gain is included in `Q_M`.

For the functional `J=3 integral(x+y+z)-2M volume`, the central box contributes

`abc[3(a+b+c)/2-2M]`.

The joint theorem bounds the sum of the three horn contributions by its negative. Regions are disjoint apart from boundaries, so their volumes and first moments add. Consequently `J<=0`, or

`mean(x+y+z)<=2M/3`.

Empty arms and zero-width cross sections are allowed. Zero caps give zero contribution, and the joint certificates use nonnegative variables without division by a central side. Thus degenerate sections do not invalidate the composition. For a wholly zero-volume set the integral inequality is trivial; the uniform mean is asserted only for positive-volume sets. Closing or opening the finitely many boundary faces changes neither integrals nor the relevant supremum.

Older component notes still describe the bridge as missing or the consequence as conditional. Those statements describe their earlier checkpoint status; the new bridge supplies the missing hypothesis rather than altering it.

## 2. The discrete consequence retains the endpoint correction

For an Apéry ideal `T` of size `m`, put `M=max a.x`, `Sigma=sum_T a.x`, `s=(a_1+a_2+a_3)/M`, `v=a_min/M`, and `kappa=(3mM-4Sigma)/(mM)`.

Anisotropic cell thickening preserves the support of every excluded generator and therefore the no-interior hypothesis. Its equal cell volumes give exactly

`kappa_c=(kappa+s)/(1+s)`.

The continuous theorem supplies `kappa_c>=1/3`; it does not supply an uncorrected discrete mean bound. For `W_4<=0`, the exact Apéry identity and `a_min>m` give `kappa<v`. The previously proved summed sawtooth inequality then gives, when `v<1/3`,

`kappa_c<2v(5-v)/(1+6v+v^2)`.

Hence `7v^2-24v+1<0`, so `1/v<12+sqrt(137)<24`. The case `v>=1/3` satisfies the same weaker conclusion directly. Every exponent in `T` thus has integer total degree at most 23.

At a central integer triple of total degree at most 23, the existing cardinality formula bounds each arm layer by the largest admissible rectangle. It is an upper bound even if independently optimal rectangles at different levels were not nested. Maximizing this finite formula over all sorted central triples gives 1836, as independently checked in the existing exact cardinality computation. Thus every such `T` with `W_4<=0` has `m<=1836`. In particular `m>=1837` forces strict positivity in this subclass.

## 3. The secondary quotient-conductor bound applies to all negative cases

Write a secondary semigroup in the established paired form

`S=p<a,b>+q<c,d>`, with `a<b`, `c<d`, `gcd(a,b)=gcd(c,d)=1`,

and common quotient `R=<a,b>/q=<c,d>/p`. Its interior conditions include

`q R_+ subseteq a+b+<a,b>` and `p R_+ subseteq c+d+<c,d>`.

These conditions themselves imply `q>b` and `p>d`; no triple-gcd exclusion is needed. To see the first, let `h=gcd(a,q)`. The positive integer `a/h` belongs to `R`, since its multiple by `q` is `(q/h)a`. If `q/h<=b`, this multiple cannot belong to `a+b+<a,b>`: an equality

`ta=(u+1)a+(v+1)b`, with `t<=b`,

would, by coprimality, imply `t-u-1>=b`, a contradiction. Therefore `q/h>b`, and in particular `q>b`. The other pair gives `p>d` identically.

Let `C=c(R)`. The two-generator Frobenius formula and `q>=b+1` show that every integer `n>=a-1` belongs to `R`, because

`nq >= (a-1)(b+1) > ab-a-b`.

Thus `C<=a-1`; similarly `C<=c-1`. Also `p>=d+1>=c+2` and `q>=b+1>=a+2`. Therefore

`m(S)=min(pa,qc)>=(C+1)(C+3)`.

Every secondary semigroup has no full-support preferred Apéry corner by the previously proved pure-critical-pair argument. If it has `W_4<0` (indeed if `W_4<=0`), the new multiplicity consequence gives `m<=1836`. But `C>=41` would force

`m >=42*44=1848>1836`.

Hence `c(R)<=40` for every negative secondary semigroup in this class. No minimal-conductor choice or inverse-inflation step occurs in this deduction.

## Remaining scope

None of these compositions covers a preferred Apéry ideal with a full-support corner. The exact geometric extension counterexample and the unavoidable-corner semigroup examples remain valid. The bound `c(R)<=40` also does not by itself prove Wilf for all secondary cases with quotient conductor at most 40.


---

# Appendix L. An exact obstruction to the one-corner extension



7 September 2026. Exact independent counterexample to an auxiliary geometric inequality, not a counterexample to Wilf's conjecture.

## Result

Even if every continuous lower ideal without a full-support excluded corner satisfies `mean(x+y+z)<=2M/3`, that assertion does **not** extend to lower ideals with one full-support excluded corner. Here `M` is the maximum total coordinate on the set, or its supremum for half-open sets.

The obstruction occurs both for an elementary polytope with one orthant removed and for a finite union of unit cells whose complement is a finite union of upper orthants. Thus it cannot be dismissed as a boundary or infinite-representation issue.

## 1. Elementary continuous family

Set

`U={x,y,z>=0: x+y<=1, x+z<=1, y+z<=1}`,

and, for `0<t<1/2`, remove the upper orthant:

`K_t=U \ [t,infinity)^3`.

Every excluded condition defining `U` has support at most two. The additional condition introduces one full-support excluded vertex, `(t,t,t)`.

Write `V(A)=vol(A)` and `I(A)=integral_A(x+y+z)`. The set `U` has

`V(U)=1/4`, `I(U)=7/32`, `M(U)=3/2`.

For a direct derivation, slice according to which coordinate is minimal and its value `r`. After translating the other two coordinates by `r`, the cross-section is the triangle of radius `1-2r`. There are three equal contributions, each with area `(1-2r)^2/2`. Its conditional mean total coordinate is

`3r+(2/3)(1-2r)=2/3+(5/3)r`.

Integration over `0<=r<=1/2` gives the displayed volume and first moment.

Let `lambda=1-2t`. The removed region is exactly

`R_t=t(1,1,1)+lambda U`,

so

`V(K_t)=(1-lambda^3)/4`,

`I(K_t)=[7-(7+10t)lambda^3]/32`,

`M(K_t)=1+t`.

The last equality is a supremum if the excluded orthant is closed: a retained point has a coordinate below `t`, while the other pair sums to at most one; points approaching `(t,1/2,1/2)` attain the bound in the limit. Closing the retained boundary changes no integral.

The normalized mean is therefore

`rho(t)=[7-(7+10t)(1-2t)^3]/[8(1+t)(1-(1-2t)^3)]`.

Subtracting `2/3` gives

`rho(t)-2/3 = t^2(3-16t+14t^2)/[3(1+t)(1-(1-2t)^3)]`.

It is positive whenever

`0<t<(8-sqrt(22))/14`.

In particular, at `t=1/10`,

`V(K)=61/500`, `I(K)=363/4000`, `M(K)=11/10`,

`mean(K)/M(K)=165/244 = 2/3+7/732`.

Equivalently its normalized four-dimensional slack is

`3-4 mean(K)/M(K)=18/61<1/3`.

The original set `U` itself satisfies the proposed no-interior-corner bound, since its mean is `7/8`, below `(2/3)M(U)=1`. Thus this is specifically a failure of the extension across a single removed orthant.

## 2. Finite-orthant counterexample

To remain within the exact finite cell class used for Apéry thickening, take

`T={(x,y,z) in N^3: x+y,x+z,y+z<=29; min(x,y,z)<=3}`,

and

`K=union_(v in T) [v_1,v_1+1) x [v_2,v_2+1) x [v_3,v_3+1)`.

The minimal excluded exponents consist of:

- the three pure bounds `30e_i`;
- the 29 mixed bounds on each coordinate plane, whose two positive coordinates sum to 30;
- the single full-support exponent `(4,4,4)`.

Every point excluded by a pair bound has a coordinate-plane excluded predecessor below it; every remaining excluded point dominates `(4,4,4)`. These are all the minimal exclusions.

Exact finite sums yield

`|T|=4246`, `sum_(v in T)|v|=92724`, `max_(v in T)|v|=32`.

Consequently

`V(K)=4246`, `I(K)=92724+(3/2)4246=99093`, `M(K)=35`,

and

`mean(K)/M(K)=99093/148610 = 2/3+59/445830>2/3`.

The complement of this `K` in the nonnegative orthant is exactly a finite union of closed upper orthants. It has exactly one full-support minimal vertex. The inequality therefore fails in the precise continuous cell setting as well.

These are geometric examples. They do not carry a verified residue-bijective Apéry labeling. In fact the finite example has 29 mixed corners on a coordinate plane, exceeding the earlier necessary arithmetic bound `P-2=10` for a full-support corner of coordinate sum `P=12`; it cannot be an Apéry staircase of the required kind.

## 3. The missing term in the deletion argument

Let `K=U\R`, set `M_U=sup_U(x+y+z)` and `M_K=sup_K(x+y+z)`, and use the target functional

`J(A;M)=3I(A)-2M V(A)`.

The exact identity is

`J(K;M_K)=J(U;M_U)+2(M_U-M_K)V(U)-[3I(R)-2M_K V(R)]`.

Knowing `J(U;M_U)<=0` leaves a positive height-loss contribution `2(M_U-M_K)V(U)`. Removing points decreases both the first moment and the admissible height, and the latter change cannot be discarded.

For the explicit `t=1/10` example the three terms are

`J(U;M_U)=-3/32`,

`2(M_U-M_K)V(U)=1/5`,

`3I(R)-2M_K V(R)=64/625`.

Their sum is

`J(K;M_K)=77/20000>0`.

Hence no proof based solely on the no-full-corner `2/3` bound and orthant deletion can establish the same constant for the one-corner class. Arithmetic restrictions could still rule out relevant geometric examples, but such restrictions would be additional input.

## Verification

`one_corner_extension_check.py` recomputes the rational family values, the exact finite cell counts, all minimal excluded corners of the finite example, and the cut-removal identity using the Python standard library. It is a certificate for these counterexamples only.


---

# Appendix M. Unavoidable corners and residue-tiling constraints



7 September 2026. Exact obstruction and additional necessary lattice conditions.

## 1. A smallest-cardinality obstruction

Let `S=<7,8,9,11>`. Its Apéry set modulo 7 is

`Ap(S,7)={0,8,9,11,17,19,20}`.

Each listed value has exactly one factorization in the three nonmultiplicity generators. Thus **every** coordinate lexicographic order, and indeed every possible selection of Apéry factorizations, gives the same set

`T={0,e1,e2,e3,e1+e2,e1+e3,e2+e3}`.

Its minimal excluded exponents are `2e1,2e2,2e3,(1,1,1)`. The last is a full-support corner, since all three of its immediate predecessors belong to `T`.

Therefore it is false that every four-generated numerical semigroup can be moved into the no-interior-corner class by changing its Apéry factorization order. The example has conductor 14, `n=5`, and `W_4=6`, so it is not a Wilf counterexample.

Seven is the smallest possible cardinality for an exponent lower ideal with a full-support minimal excluded point: all seven points of `{0,1}^3` except `(1,1,1)` must be included.

There are also order-independent nonunit interior corners. For

`S=<11,12,14,17>`,

the Apéry exponent set is exactly

`T={0,1,2} x {0,1} x {0,1} \ {(2,1,1)}`.

Every Apéry element again has a unique factorization. Its Apéry values are

`0,12,14,17,24,26,29,31,38,41,43`,

and its unique full-support corner is `(2,1,1)`. Here `c=33`, `n=13`, and `W_4=19`. Both examples are already settled Wilf families; their purpose is to refute a universal change-of-order shortcut.

The obstruction also occurs outside the six-final-window class. The semigroup

`S=<155,1552,1647,1651>`

has unique factorizations for all 155 Apéry elements, an unavoidable full-support corner `(1,7,4)`, and seven final-window points. Its exact invariants are

`M=18133`, `c=17979`, `n=6865`, `W_4=9481`.

The seven exponent vectors in the final window are

`(0,7,4),(1,2,8),(1,3,7),(1,4,6),(1,5,5),(1,6,4),(1,7,3)`.

This fixture rules out treating all order-independent full corners as automatically belonging to the six-point class. Its Wilf number is positive; no claim that it violates another established sufficient criterion is intended.

## 2. A sumset–difference-set obstruction stronger than merely counting corners

Let `T` have bijective linear labels in a group `G` of order `m`. Suppose finite integer sets `A,B` satisfy

`A+B subseteq T`.

Then

`|A-B|<=m`.

Indeed, equal labels on `a-b` and `a'-b'` give equal labels on `a+b'` and `a'+b`, both in `T`. Injectivity on `T` forces equality of these integer vectors, hence `a-b=a'-b'`. Thus labels are injective on `A-B` as well. This argument applies to any finite group labeling induced by a homomorphism; cyclicity is unnecessary.

An entire hierarchy follows. For any finite test set `B`, define the erosion

`A_B={x in Z^3: x+B subseteq T}`.

Every residue-bijective `T` must satisfy `|A_B-B|<=m`. The simplex difference-set exclusion in the earlier manuscript is one special case, but the condition applies to arbitrary shapes and arbitrary finite test sets.

## 3. Exact exclusion of the bad geometric one-corner example

For the auxiliary continuous counterexample's cell index set,

`T={x in N^3: x1+x2,x1+x3,x2+x3<=29; min(x)<=3}`,

take

`B={0,e1,e2,e3}`,

`A={x in T: x+B subseteq T}`.

The exact counts are

`|T|=4246`, `|A|=3241`, `|A-B|=4546`.

Since `4546>4246`, this `T` cannot admit any residue-bijective lattice labeling of the required index. This excludes it without using the separate bound on the number of mixed corners.

The result does not claim that the unit-simplex test suffices for all staircases. Coarsening profiles may defeat one test while preserving the bad centroid. The full hierarchy supplies additional necessary conditions; neither sufficiency nor a centroid theorem from it has been proved here.

## 4. Further exact constraints available from an actual interior corner

Write `Lambda=ker(Z^3 -> Z/mZ)` for the residue lattice. If `p` is a full-support minimal excluded exponent, then `p in Lambda`. For a mixed excluded corner `q` in a coordinate plane and its representative `h e_i` on the complementary axis, both

`q-h e_i in Lambda` and `q-h e_i-p in Lambda`.

None of these nonzero vectors can lie in `T-T`. More generally every nonzero vector of `Lambda` is excluded from `T-T`, since two points of `T` cannot have the same residue. The resulting translated-overlap exclusions retain the positions and sizes of mixed corners, not only their count.

If three such lattice vectors are linearly independent, the absolute value of their determinant is a positive integer multiple of `m`. This follows because they generate a sublattice of `Lambda`, whose index in `Z^3` is `m`. It is a further exact condition on candidate corner data, not a stand-alone sufficient labeling criterion.

No implication from these necessary conditions to the sharp continuous `2/3` centroid inequality for all genuine one-corner Apéry shapes has been completed.

## Verification

`lex_order_and_tiling_check.py` computes the three Apéry sets independently, enumerates all their factorizations, checks all six lexicographic orders, and verifies the displayed sumset–difference-set counts using exact integer arithmetic.


---

# Appendix N. Why equalizing weights does not finish the proof



This exact example shows why the proved unit-weight inequality cannot be
extended by simply asserting that equal weights minimize the defect.
It does **not** refute the weighted inequality being sought, and no Apéry
realization of this ideal at the minimizing weights is asserted.

Let T be the union of the three integer boxes with maximal points

\[
(6,1,1),\qquad(1,5,1),\qquad(1,1,4).
\]

Equivalently, coordinates are bounded by `(6,5,4)`, and at most one
coordinate exceeds 1. Its minimal excluded points are exactly

\[
(7,0,0),(0,6,0),(0,0,5),
(2,2,0),(2,0,2),(0,2,2).
\]

Thus T has no full-support excluded corner, contains the entire cube
`{0,1}^3`, and has three nonempty arms. Its cardinality and coordinate
sums are

\[
m=56,\qquad\sum_{x\in T}x=(98,76,58).
\]

Consider ordered normalized weights `(1,b,c)`, with `1<=b<=c`. Set

\[
H=\max(5,4b,3c).
\]

The largest weight in T is `M=1+b+c+H`, and therefore

\[
\begin{aligned}
D(1,b,c)
&=3mM-4\sum_{x\in T}(x_1+bx_2+cx_3)\\
&=168H-224-136b-64c.
\end{aligned}
\]

For a fixed `H>=5`, feasibility gives `b<=H/4` and `c<=H/3`. The last
expression strictly decreases in both b and c. Their upper bounds are
simultaneously feasible and ordered, so the unique fixed-H minimizer is

\[
b=H/4,\qquad c=H/3.
\]

Its value is

\[
D=\frac{338}{3}H-224,
\]

which strictly increases with H. Consequently the unique global minimum
on the entire ordered cone is

\[
\boxed{(1,b,c)=(1,5/4,5/3),\qquad D_{\min}=1018/3.}
\]

All three maximal points are exposed and tied at this vertex. By
comparison, unit weights give `M=8` and

\[
D(1,1,1)=416>1018/3.
\]

Thus this minimum is neither the unit-weight point nor a vertex forced
by equality of two coordinate weights. Its ratios are proportional to
`(12,15,20)`; no coordinate is an integer multiple of another.

The proposed bound `D>=a_min(m-1)` still holds comfortably in this
example: `1018/3>55`. The example obstructs a proof shortcut, not the
conjectured weighted bound.

At the minimizing weights the three maximal points have identical
weight. Thus this minimizing configuration itself is not a preferred
Apéry factorization set: different representatives there would have the
same numerical value. The example concerns the geometric relaxation.
This distinction is essential when trying to use arithmetic residue
constraints to exclude or control extremal boundary configurations.

For completeness, the generic LP has variables `(b,c,M)` and constraints
`b>=1`, `c>=b`, and `M>=x_1+bx_2+cx_3` for maximal x in T. A minimizing
vertex may consist of both order constraints and one exposed maximum,
one order constraint and two tied maxima, or three tied maxima with
independent tie equations. The example realizes the last type with one
maximum on each of the three arms. The tripod structure does not remove
that vertex type.

Run the standard-library checker:

`python3 round4/discrete_horns/verify_unequal_exposed_vertex.py`
