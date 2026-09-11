# Wilf research continuation: finite reduction and new four-generator classes

**5 September 2026. Research manuscript.**

The unrestricted conjecture is not proved or disproved by this manuscript.
The work completes several subarguments and identifies a finite region that
has not been eliminated. Independent adversarial checks within this research
session found no gap in the analytic theorems below; that is not external
peer review or a claim of publication priority.

## Results established in this continuation

For a numerical semigroup let \(m\) be the multiplicity, \(c\) the conductor,
\(e\) the embedding dimension, \(n=|S\cap[0,c)|\), and \(W_e=en-c\).

1. **Four generators, large multiplicity:**
   \[
   \boxed{m\ge2\times10^{14}\quad\Longrightarrow\quad W_4>0.}
   \]
   The proof is analytic. It replaces the previous \(10^{27}\) cutoff.
2. **Every fixed embedding dimension:** there is an explicit \(B_{e-1}\)
   above which \(W_e>0\), and an explicit upper bound on every generator
   in any remaining counterexample. Consequently only finitely many possible
   counterexamples remain at each fixed \(e\). This does not give a finite
   bound uniform over all embedding dimensions.
3. **Interior corner \((1,1,1)\):** a residue-bijective Apéry staircase
   with this minimal excluded point has at most six coordinatewise maxima.
   Hence its semigroup satisfies Wilf, by the previously completed six-point
   theorem. The new structural proof is analytic; this Wilf corollary retains
   the earlier theorem's finite computational dependency.
4. **A generator criterion:** if a nonmultiplicity minimal generator \(A\)
   satisfies \(m\mid2A\), then Wilf holds. More generally, if its first
   critical multiple is \(aA=bm\), Wilf holds for
   \(m\ge16a^3-2\). The exponent-two corollary also uses the six-point
   theorem; the parameter cutoff uses the analytic slab theorem.

Part I gives the complete analytic fixed-dimension proof, including an
independent conductor bound. Part II proves the sharper four-generator
cutoff. Part III gives the new residue argument. Part IV records what is
still missing and distinguishes failed auxiliary claims from counterexamples
to Wilf.

The accompanying verification archive contains the source notes, independent
audits, exact checkers and outputs, and the prior computational dependencies.

---

# Part I. Explicit finite reduction at every fixed embedding dimension

**Research derivation, 5 September 2026.** This note supplies a self-contained
generalization of the stability argument to every fixed embedding dimension
`e=d+1>=3`. It proves an explicit sufficient multiplicity threshold, and,
using the difference-set exclusion of discrete simplexes, a
finite region containing all possible counterexamples at each fixed `e`.
It does not exclude that finite region and does not prove Wilf's conjecture.
No publication-priority claim is made.

## 1. Constants and conclusions

Fix an integer `d>=2`, and set

\[
\begin{gathered}
h_d=\frac1{8d},\qquad
r_d=\frac1{16d^2(d+1)},\qquad
\delta_d=d!h_dr_d^d,\\
P_d=1+32d(d-1)(d+1)^2,\qquad
Q_d=4d(d-1)(d+1),\\
\eta_d=\frac{\delta_d}{2P_d},\qquad
H_d=\frac{(d-1)P_d}{\delta_d},\qquad
B_d=\left\lceil\frac{(d+H_d)^d}{d!}\right\rceil.
\end{gathered}
\]

**Theorem A.** Every numerical semigroup with embedding dimension `d+1` and
multiplicity `m>=B_d` has strictly positive Wilf number.

**Theorem B.** Every counterexample of embedding dimension `d+1` satisfies

\[
\boxed{
d+2\le m<B_d,\qquad
a_i\le M\le
\frac{m(m-d)}2\bigl((d-1)(m-1)-2\bigr),
}
\tag{1}
\]

where `m<a_1<...<a_d` are the other minimal generators and `M=c+m-1`.
In particular there are only finitely many possible counterexamples in each
fixed embedding dimension `e>=3`. This statement concerns each fixed
embedding dimension separately; it gives no finite bound uniform over all
embedding dimensions.

## 2. Apéry arithmetic and the slack identity

For a minimally generated numerical semigroup

\[
S=\langle m,a_1,\ldots,a_d\rangle,\qquad m<a_1<\cdots<a_d,
\]

choose the lexicographically least factorization of every element of
`Ap(S,m)` using the `a_i`. The selected set `T` is a lower ideal in
`N^d`, has `m` elements, and contains `0,e_1,...,e_d`. A divisor of an
Apéry factorization is again Apéry, and replacing a divisor by a
lexicographically smaller factorization would replace the original
factorization by a lexicographically smaller one. This proves lower closure.

Labels `w(x)=sum a_i x_i` on `T` are bijective modulo `m`. For each minimal
excluded exponent `p`, its residue representative `q in T` has support
disjoint from that of `p`. Otherwise `p-e_i` and `q-e_i` would be distinct
points of `T` with equal residues. Two distinct minimal excluded exponents
sharing a positive coordinate cannot have equal residues, by the same
predecessor argument. Therefore:

\[
\boxed{T\text{ has at most one minimal excluded exponent of full support.}}
\tag{2}
\]

Write `M=max_T w=c+m-1`, and `Sigma=sum_T w`. If a coordinate line `ell`
has length `L_ell` and top `t_ell`, averaging along its consecutive integer
points and summing independently in each of the `d` directions gives

\[
D:=dmM-(d+1)\Sigma
=\sum_\ell L_\ell\bigl(M-w(t_\ell)\bigr)\ge0.
\tag{3}
\]

The Apéry genus formula gives, with `W_e=e(c-g)-c`,

\[
\boxed{mW_{d+1}=D-\frac{d-1}{2}m(m-1).}
\tag{4}
\]

## 3. A quantitative continuous gap in dimension d

Let

\[
\Delta=\{x\in\mathbb R_{\ge0}^d:\sum_i x_i\le1\}.
\]

Consider a positive-volume downset `K subset Delta` whose complement in the
nonnegative orthant is a finite union of closed upper orthants, at most one
of which has a vertex with all coordinates positive. This includes the
half-open rectangular cell sets used below. Let `mu` be the uniform mean of
`sum x_i` on `K`, and define `kappa_c=d-(d+1)mu`.

**Continuous gap lemma.** Under these hypotheses,

\[
\boxed{\kappa_c\ge\delta_d.}
\tag{5}
\]

### 3.1 Coordinate-fiber identities

For direction `j`, let `H_j(y)` be the length of the fiber over the other
coordinates `y`. Set `V=vol(K)`. Fubini's theorem gives

\[
\kappa_cV=\sum_{j=1}^d J_j,\qquad
J_j=\int H_j(y)\bigl(1-\sum y-H_j(y)\bigr)\,dy\ge0.
\tag{6}
\]

Indeed, `integral H_j^2=2 integral_K x_j`, and the other-coordinate term is
`integral_K sum_(i!=j) x_i`. This proves the identity and nonnegativity.
The same calculation in dimension `k` and simplex radius `L` gives the
continuous lower-ideal inequality `mean sum x_i <= kL/(k+1)`.

Let `R=min_i X_i` for uniform `X in K`. Partition, up to null ties, according
to the uniquely minimal coordinate `j` and its value `R=rho`. Subtract
`rho` from every other coordinate. The resulting conditional slice is a
`(d-1)`-dimensional downset in a simplex of radius `1-d rho`. The preceding
inequality implies

\[
\mathbb E[\sum_iX_i\mid j,R=\rho]
\le d\rho+\frac{d-1}{d}(1-d\rho)
=\frac{d-1}{d}+\rho.
\]

Thus

\[
\mu\le\frac{d-1}{d}+\mathbb ER.
\tag{7}
\]

If `kappa_c<1/(2d)`, it follows that

\[
\mathbb ER\ge\frac1{d(d+1)}-\frac{\kappa_c}{d+1}
>t:=\frac1{2d(d+1)}.
\]

There is consequently a point of `K` with every coordinate greater than `t`.
Lower closure then gives `[0,t]^d subset K`.

### 3.2 Propagating from the cube to any prescribed interior target

Abbreviate `h=h_d` and `r=r_d`. Suppose `K` contains `[0,t]^d`, and let
`z>=0` satisfy `sum z_i<=1-h`. Set

\[
v^{(0)}=(d+1)r\,\mathbf1,
\]

and, for `1<=j<=d`, let

\[
v^{(j)}_i=
\begin{cases}
z_i+(d-j+1)r,&i\le j,\\
(d-j+1)r,&i>j.
\end{cases}
\]

We have `(d+1)r<=t`, so `v^(0) in K`. Suppose `v^(j-1) in K` but
`v^(j) notin K`. Integrate direction-`j` fibers over the rectangle where

\[
\begin{cases}
y_i\in[z_i+(d-j+1)r,z_i+(d-j+2)r],&i<j,\\
y_i\in[(d-j+1)r,(d-j+2)r],&i>j.
\end{cases}
\]

Its `(d-1)`-dimensional volume is `r^(d-1)`. Membership of `v^(j-1)` gives
`H_j>=(d-j+2)r>=2r`; omission of `v^(j)` and lower closure give
`H_j<=z_j+(d-j+1)r`. Therefore the fiber's gap from the simplex boundary is
at least

\[
1-\sum_{i\le j}z_i-
\bigl(d(d-j+2)-1\bigr)r
\ge h-d(d+1)r=\frac h2.
\]

Consequently `J_j>=h r^d`. Since `V<=1/d!`, (6) gives

\[
\kappa_c\ge d!h r^d=\delta_d.
\]

It follows that if `kappa_c<delta_d`, no step can fail: every prescribed
`z>=0` with `sum z_i<=1-h` lies in `K`.

### 3.3 Contradicting the excluded-corner hypothesis

We have `delta_d<1/(2d)`, so a putative `kappa_c<delta_d` supplies the cube
and the preceding propagation result. Set

\[
\alpha=\frac1{2d},\quad
\beta=\frac12+\frac1{4d},\quad
b=\alpha\mathbf1,\quad
p=b+\beta e_1,\quad q=b+\beta e_2.
\]

Both `p` and `q` have coordinate sum `1+1/(4d)>1`, so are outside `K`.
For either point, replace any one of its coordinates by `h=1/(8d)`. Every
resulting witness has sum at most `1-h`; hence all `2d` witnesses belong to
`K`. The point `b`, of sum `1/2`, also belongs to `K`.

Take an excluded upper-orthant vertex below `p`. If it had a zero coordinate
`j`, it would also lie below the corresponding witness with coordinate `j`
replaced by `h`, contradicting that witness's membership. Thus it has full
support. The same reasoning applies below `q`. There is at most one
full-support excluded vertex, so these two vertices agree, and lie below
`min(p,q)=b`. That would exclude `b`, a contradiction. This proves (5).

## 4. Transferring the gap to a weighted integer lower ideal

Let `T subset N^d` be any finite lower ideal containing `0,e_1,...,e_d`,
with `m` elements and at most one full-support minimal excluded exponent.
Normalize positive weights `u_i` so `max_T sum u_i x_i=1`. Put

\[
U=\max u_i\le1,\quad v=\min u_i,\quad
\mu_i=\mathbb E[u_iX_i],\quad
\mu=\sum\mu_i,\quad \kappa=d-(d+1)\mu\ge0.
\]

For the largest integer coordinate `H_j(x_-j)` on a fiber, write

\[
\epsilon_j(x)=1-u_jH_j(x_{-j})-\sum_{i\ne j}u_ix_i\ge0.
\]

Uniformity on each discrete fiber gives

\[
\mathbb E\epsilon_j=1-\mu-\mu_j,
\quad\sum_j\mathbb E\epsilon_j=\kappa,
\quad\mu_j\ge\frac{1-d\kappa}{d+1}.
\tag{8}
\]

### 4.1 A discrete phase estimate

If `kappa<=1/(2d)`, then

\[
\boxed{U\le64(d+1)^2\kappa+8(d+1)v.}
\tag{9}
\]

To prove this, let `A=1/[2(d+1)]` and
`s_0=min(U/4,A/2)`. If `v>s_0/2`, the inequality
`s_0>=U/[4(d+1)]` immediately yields `U<8(d+1)v`.
Otherwise choose directions `j,k` of largest and smallest weight. They are
distinct in this case. Set `ell=floor(s_0/v)` and `s=ell v`. Then
`s_0/2<=s<=s_0<=U/4`, and (8) gives `mu_k>=A`.

For every `x in T` with `x_k>=ell`, both `x` and `x-ell e_k` belong to `T`.
Their nonnegative direction-`j` gaps differ by `-s` modulo `U`, so their sum
is at least `s`. The shift map is injective. Summing these pairs counts each
point's gap at most twice, and therefore

\[
2\kappa\ge
s\Pr(vX_k\ge s)
\ge s(\mu_k-s)
\ge\frac{s_0A}{4}
\ge\frac{U}{32(d+1)^2}.
\]

The probability estimate uses `0<=vX_k<=1` and
`Pr(Y>=s)>=EY-s`. This proves `U<=64(d+1)^2 kappa` in the remaining case,
and establishes (9).

### 4.2 Rectangular cells and cardinality

Put `sigma=sum u_i`, and form

\[
K=\bigcup_{x\in T}\prod_{i=1}^d
\left[\frac{u_ix_i}{1+\sigma},
\frac{u_i(x_i+1)}{1+\sigma}\right).
\]

This is a positive-volume downset in `Delta`. Its complement is the union
of upper orthants at the scaled minimal excluded exponents of `T`, so the
continuous gap lemma applies. Every cell has the same volume, giving

\[
\kappa_c=
\frac{\kappa+\frac{d-1}{2}\sigma}{1+\sigma}.
\]

Under the phase hypothesis `kappa<=1/(2d)`, (9) implies

\[
\boxed{\delta_d\le\kappa_c\le P_d\kappa+Q_dv.}
\tag{10}
\]

Finally `T subset {x: |x|_1<=floor(1/v)}`, so

\[
m\le\binom{\lfloor1/v\rfloor+d}{d}
\le\frac{(1/v+d)^d}{d!}.
\tag{11}
\]

Thus `v<=1/((d!m)^(1/d)-d)` whenever the denominator is positive.

## 5. Proof of the eventual theorem

For `m>=B_d`, let `x_m=(d!m)^(1/d)-d`. By definition `x_m>=H_d`, hence

\[
v\le\frac1{H_d}=\frac{\delta_d}{(d-1)P_d}.
\]

The elementary inequality `2Q_d<=(d-1)P_d` therefore gives
`Q_dv<=delta_d/2`. If `kappa<=1/(2d)`, (10) implies

\[
\kappa\ge\frac{\delta_d}{2P_d}=\eta_d.
\]

If the phase hypothesis fails, the same conclusion follows immediately from
`eta_d<1/(2d)`. Thus `kappa>=eta_d` in all cases.

Apply this to the preferred Apéry ideal with `u_i=a_i/M`. Since `a_min>m`,
(11) also gives

\[
\frac Mm>\frac M{a_{\min}}=\frac1v\ge x_m\ge H_d.
\]

Using (4),

\[
\begin{aligned}
W_{d+1}
&=\kappa M-\frac{d-1}{2}(m-1)\\
&>\eta_dmH_d-\frac{d-1}{2}(m-1)\\
&=\frac{d-1}{2}>0.
\end{aligned}
\]

This proves Theorem A. The constants are deliberately loose.

## 6. A simplex exclusion from residue injectivity

The following argument was independently checked during this continuation.

**Lemma.** If `d>=2` and `R>=2`, the standard discrete simplex

\[
\Delta_R=\{x\in\mathbb N^d:|x|_1\le R\}
\]

does not admit injective linear labels in a cyclic group of order
`m=|Delta_R|=binom(d+R,d)`.

**Proof.** Suppose it did. Consider

\[
E=\Delta_{R-1}-\Delta_1.
\]

If two elements `p-q` and `p'-q'` of `E` have equal residue, then
`p+q'` and `p'+q` belong to `Delta_R` and have equal residue. Injectivity on
`Delta_R` makes them equal as integer vectors. Consequently `p-q=p'-q'`.
Thus the labels are injective on `E` as well.

The nonnegative part of `E` is exactly `Delta_(R-1)`. Its remaining points
have one coordinate equal to `-1`, all others nonnegative, and the sum of
those other coordinates at most `R-1`. These `d` pieces are disjoint, giving

\[
|E|=\binom{d+R-1}{d}+d\binom{d+R-2}{d-1}.
\]

Subtracting `m` gives

\[
|E|-m=
\frac{(d-1)(R-1)}R\binom{d+R-2}{d-1}>0,
\]

contradicting injectivity into a group of order `m`. This proves the lemma.

## 7. Bounding the conductor and all generators

**Geometric lemma.** Suppose a finite lower ideal `T subset N^d` contains all
unit vectors and is not a standard simplex. With positive weights and the
notation of (3),

\[
\boxed{D\ge\frac{M}{m-d}.}
\tag{12}
\]

First, a finite lower ideal has every coordinate-line top maximal if and
only if it is a standard simplex. Indeed, if `x_i>0` and `x in T`, omission
of `x-e_i+e_j` would make `x-e_i` a direction-`j` line top that is not
maximal. Hence every unit transfer is allowed. Transfers connect the entire
integer layer of fixed total degree; a point of largest degree therefore
forces that whole layer and, by lower closure, every preceding layer.

Choose a least weight `beta` and let its axis have height `ell>=1`.
Write `epsilon=M-ell beta`. The axis line contributes `(ell+1)epsilon`
to (3). There is a nonmaximal line top, whose gap from `M` is at least
`beta`, because some coordinate successor is in `T`.

If that is the same axis line, `epsilon>=beta` and
`D>=(ell+1)epsilon>=ell beta+epsilon=M`.
Otherwise the two distinct lines give
`D>=(ell+1)epsilon+beta`, whence `ell D>=epsilon+ell beta=M`.
The axis points and the other unit vectors give `ell<=m-d`, proving (12).

For an Apéry ideal with `m>d+1`, the preceding simplex exclusion rules out
every standard simplex: `R=0,1` have too few points, and `R>=2` cannot have
residue-bijective labels. Thus (12) applies.

If `W_(d+1)<0`, integrality and (4) give

\[
D\le m\left(\frac{d-1}{2}(m-1)-1\right).
\]

Combining with (12) proves the upper bound in (1). Every minimal generator
is an Apéry element, so every `a_i<=M`.

For completeness the remaining multiplicity `m=d+1=e` satisfies Wilf
directly. Its Apéry set consists of `0` and its `m-1` other minimal
generators. If their maximum is `M`, their distinct integer values imply

\[
\Sigma\le(m-1)M-\frac{(m-1)(m-2)}2.
\]

The genus formula then gives

\[
W_m=(m-1)M-\Sigma-\frac{(m-1)(m-2)}2\ge0.
\]

This completes Theorem B.

## 8. Precise limitations

The continuous gap uses only the single full-support excluded-corner
restriction. The eventual multiplicity threshold uses that gap, a discrete
phase estimate, and elementary lattice-point counting. The finite conductor
bound additionally uses residue injectivity through the difference-set
simplex exclusion. Every component above is analytic; finite computations
are not dependencies of the conclusions.

The resulting finite regions are far too large for naive enumeration. None
of these statements proves that the finite region contains no
counterexample. In particular, the desired four-generator conclusion still
requires an additional argument or a feasible exhaustive certificate.

---

# Part II. Four generators: the cutoff 2 × 10¹⁴

# Continuous one-corner gap at least 1/10000

## Statement

Let K be a bounded positive-volume downset in the nonnegative orthant, with maximum total coordinate at most one. Suppose its complement is a finite union of closed upper orthants with vertices supported on at most two coordinates, together with at most one vertex supported on all three coordinates. Then

  kappa_c := 3 - 4 E_K(x+y+z) >= 1/10000.

All decimals below are exact rational numbers. This strengthens the preceding 1/1000000 bound; it does not prove Wilf's conjecture.

## Identities used

Write V=vol(K), and H_j(y) for the coordinate-j fiber endpoint. The coordinate-fiber moment identity gives

  kappa_c V = J_1+J_2+J_3,
  J_j=integral H_j(y)(1-sum(y)-H_j(y))dy >=0.

Since K lies in the unit simplex, V<=1/6. Therefore any lower bound J_j>=B implies kappa_c>=6B.

Slicing by the minimum coordinate r, and using the two-dimensional moment inequality in each translated slice, gives

  E_K(x+y+z) <= 2/3 + E_K min(x,y,z).

## Initial cube and bootstrap

Suppose kappa_c<1/10000. Then

  E min(x,y,z) >= 1/12-kappa_c/4 > .08.

Some point of K consequently has all coordinates greater than .08, so K contains [.0,.08]^3.

We claim q=(.16,.16,.16) belongs to K. First force membership of v1=(.26,.04,.04). If omitted, integrate x-fibers over y,z in [.04,.08]. They have H_x>=.08 by the initial cube and H_x<=.26 by omission. Their top deficits are at least 1-.26-.08-.08=.58. Thus

  kappa_c >= 6(.08)(.04)^2(.58) = .00044544 > .0001,

a contradiction. Hence v1 belongs.

Next force v2=(.21,.21,.02). If omitted, integrate y-fibers over x in [.21,.26], z in [.02,.04]. Membership of v1 gives H_y>=.04; omission gives H_y<=.21; top deficits are at least 1-.26-.21-.04=.49. Thus

  kappa_c >= 6(.04)(.05)(.02)(.49) = .0001176 > .0001.

Finally, if q were omitted, integrate z-fibers over x,y in [.16,.21]. Membership of v2 gives H_z>=.02, omission gives H_z<=.16, and top deficits are at least 1-.21-.21-.16=.42. Thus

  kappa_c >= 6(.02)(.05)^2(.42) = .000126 > .0001.

Therefore q belongs to K, and the downset contains [.0,.16]^3.

## Seven forced witnesses

The following propagation argument works in any permutation of the coordinates. Let q satisfy

  q1<=.25, q1+q2<=.5, q1+q2+q3<=.7502,

with nonnegative coordinates. Set

  v1=(q1+.12,.10,.10),
  v2=(q1+.07,q2+.07,.04).

If v1 were omitted, integrate x-fibers over y,z in [.10,.16]. Their heights are at least .16 and their top deficits are at least 1-q1-.12-.32>=.31. Therefore

  kappa_c >= 6(.16)(.06)^2(.31) = .00107136 > .0001.

So v1 belongs. If v2 were omitted, integrate y-fibers over x in [q1+.07,q1+.12], z in [.04,.10]. Their heights are at least .10 and their top deficits are at least 1-q1-q2-.12-.07-.10>=.21. Therefore

  kappa_c >= 6(.10)(.05)(.06)(.21) = .000378 > .0001.

So v2 belongs. If q were omitted, integrate z-fibers over x in [q1,q1+.07], y in [q2,q2+.07]. Their heights are at least .04 and their top deficits are at least 1-sum(q)-.14>=.1098. Therefore

  kappa_c >= 6(.04)(.07)^2(.1098) = .0001291248 > .0001.

Thus q belongs.

Now take p=(.5001,.25,.25), p'=(.25,.5001,.25), and b=(.25,.25,.25). Both p,p' lie outside the unit simplex. The three points obtained from p by replacing one coordinate by .0001, the three analogous points from p', and b all satisfy the propagation conditions after ordering their coordinates increasingly. Hence all seven belong to K.

Any excluded-orthant vertex below p must have full support: otherwise it also lies below one of p's three witnesses. The same applies to p'. The at-most-one-full-support-vertex assumption therefore forces the same vertex below both p,p', hence below their coordinatewise minimum b. This contradicts b's membership.

Therefore kappa_c>=1/10000, as claimed.

# Sharper discrete phase estimate

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

On the other hand,
\[
m\le\binom{\lfloor1/v\rfloor+3}{3}
\le\frac{(1/v+3)^3}{6}.
\]
If \(m\ge2\times10^{14}\), the exact integer inequality
\[
(100003)^3=1000090002700027
 <1200000000000000=6(2\times10^{14})
\]
forces \(v<1/100000\). Equation (S2) then gives
\(\kappa_c<1/10000\), contradicting the continuous lemma.
This proves \(W_4>0\) throughout the stated tail, including the exclusion
of equality there. The proof uses no enumeration of numerical semigroups.


---

# Part III. The interior-corner (1,1,1) class

## Scope and dependency

The structural theorem below is entirely analytic. It proves that a residue-bijective lower ideal in three variables whose minimal excluded set contains `(1,1,1)` has at most six coordinatewise maximal points.

For a genuine four-generated numerical semigroup, this implies Wilf by Theorem A of `prior/wilf_edim4_six_point_and_column_theorems_2026-09-05.md`: at most six Apéry elements in `[c,c+m)` suffice. That earlier theorem has a finite computer-assisted component. The deduction here does not reverify or eliminate that computational dependency. Thus the structural bound is analytic, while the stated Wilf corollary uses the previously certified six-point theorem.

No publication priority claim is made.

## Structural theorem

Let `T⊂N^3` be a finite nonempty lower ideal of size `m`, containing the three unit vectors. Suppose

`x ↦ A x1+B x2+C x3 (mod m)`

is bijective on `T`, and suppose `(1,1,1)` is a coordinatewise minimal excluded point. Then:

1. Each coordinate plane contains at most one minimal excluded point supported on both of its coordinates.
2. `T` has at most six coordinatewise maximal points.

### Boundary facts

If `p` is minimal excluded and `q∈T` represents its residue, their supports are disjoint. Otherwise subtracting a shared coordinate unit vector gives two distinct points of `T` with equal residues. Likewise, two distinct minimal excluded points sharing a positive coordinate cannot have the same residue: subtract that shared coordinate and use injectivity on `T`.

The interior point `(1,1,1)` therefore has representative zero, so

`A+B+C=0 (mod m)`.

### At most one mixed corner in a plane

Consider any mixed minimal excluded point `p=(u,v,0)`, where `u,v>=1`. By disjoint support its representative is `γ e3`. It cannot be zero, because `p` and `(1,1,1)` share positive coordinates and are distinct minimal excluded points. Thus `γ>=1`.

Let `h3=max{k : k e3∈T}`. Then `γ<=h3`. The point

`r=p-e1-e2=(u-1,v-1,0)`

belongs to `T`: it is coordinatewise below the included predecessor `p-e1`. Its residue is

`w(r)=w(p)-A-B=γC+C=(γ+1)C (mod m)`.

If `γ<h3`, then `(γ+1)e3∈T` as well. These are distinct points: the first has third coordinate zero, while the second has positive third coordinate. This gives a forbidden residue collision. Therefore `γ=h3`.

Every mixed corner of the first two coordinates must consequently have the same residue, namely `h3 C`. But any two such corners share both coordinates in their supports, so the boundary fact says their residues must be distinct. There is at most one. Permuting coordinates proves the first assertion.

The calculation would still distinguish the two points if `u=v=1`, since then `r=0` while `(γ+1)e3≠0`. Under the present minimal-interior-corner hypothesis that mixed corner cannot actually occur: `(1,1,0)` is a predecessor of `(1,1,1)` and lies in `T`.

### At most six maxima

Because `(1,1,1)` is excluded, every point of `T` has at least one zero coordinate. Thus `T` is the union of its three coordinate-plane sections.

Each section is a finite planar lower ideal with its two pure axis bounds and at most one mixed minimal excluded point. It is therefore a rectangle with at most one upper-right quadrant removed, and has at most two planar maximal points.

Every coordinatewise maximal point of `T` is maximal in each coordinate-plane section containing it. In particular it is in the union of the three sets of planar maxima. That union has at most `2+2+2=6` elements. This proves the second assertion.

## Wilf corollary

Let `S=<m,a1,a2,a3>` be minimally four-generated, and choose a preferred Apéry staircase `T` modulo `m`. If `(1,1,1)` is a minimal excluded point of `T`, the theorem gives at most six coordinatewise maxima.

Set `M=max_{x∈T} a·x=c+m-1`. Every point in the final Apéry window

`Z={x∈T : M-a·x<m}`

is coordinatewise maximal: a coordinate successor would add a generator larger than `m`, thereby exceeding `M`. Consequently `|Z|<=6`. The previously certified complete six-point theorem now gives `4|S∩[0,c)|>=c`.

## Diagnostic, not a proof dependency

A seeded 20,000-proposal experiment with generator residues summing to zero produced 16,478 minimally four-generated semigroups, of which 16,346 had the minimal corner `(1,1,1)`. Their maximal-point counts were:

| Maximal points | Observed semigroups |
|---:|---:|
| 3 | 582 |
| 4 | 3,972 |
| 5 | 3,054 |
| 6 | 8,738 |

The structural proof above is independent of this sample.

## A second generator-based class

## 1. Pure critical pairs eliminate all interior corners

**Theorem.** Suppose S=⟨m,A,B,C⟩ is minimally four-generated, m is its multiplicity, and a A=b m for positive integers a,b, where a is the least positive integer with a A∈⟨m,B,C⟩. No criticality assumption is made on b for the base m. Then every preferred Apéry factorization lower ideal T with respect to m has no full-support minimal excluded point.

**Proof.** For 0≤r<a, the element rA has no alternative factorization in the full generating set. Indeed, cancelling a shared A coefficient from an alternative factorization would give a positive multiple sA, s≤r<a, in ⟨m,B,C⟩. Thus rA is Apéry, its unique exponent is r e_A, and all these axis points belong to every preferred T. The exponent a e_A is excluded because aA=bm, so the pure A-axis has exactly a points.

Suppose p=(x,y,z) is a full-support minimal excluded exponent. Its residue representative has disjoint support from p, by the standard Apéry minimal-corner lemma. Therefore the representative is zero and xA+yB+zC=k m for some positive integer k. Since p−e_B belongs to T, its first coordinate satisfies x<a.

Both r=(0,y,z) and q=(a−x,0,0) are in T: the former is a strict divisor of p, the latter is one of the unique pure-axis representatives just proved. Subtracting b m=a A from the displayed relation gives

yB+zC=(a−x)A+(k−b)m.

Thus r and q are distinct elements of T with the same residue modulo m, contradicting residue injectivity. The sign of k−b is irrelevant to this residue contradiction. ∎

The argument applies to Chomicz's entire secondary class, because the multiplicity belongs to one of its two paired pure critical relations. It also applies more broadly whenever the first critical multiple of one nonmultiplicity generator is a multiple of the multiplicity. No lexicographic ordering issue arises: the required axis representatives are unique.

A lower ideal with no full-support minimal excluded point equals the intersection of its three pairwise projection cylinders. This gives a stronger restriction than the one-interior-corner condition used by the global cutoff.


## 1.1. A uniform cutoff for every fixed critical pure exponent

Under the theorem's hypotheses, let r be the number of mixed minimal excluded points in the BC coordinate plane. Then

r≤a,
number of coordinatewise maximal points of T ≤a(r+1),
number K of occupied compressed cells of T ≤a(a+r)²≤4a³.

Consequently, by the established compressed-cell slab theorem,

**m≥4a(a+r)²−2 implies W_4≥0; in particular m≥16a³−2 implies W_4≥0.**

These bounds place no restriction on conductor, type, or generator size.

**Proof.** Write F=T∩{x=0}, as a planar lower ideal in the BC coordinates. Every mixed minimal excluded point of F is a support-BC minimal excluded point of T. Its residue representative lies on the A-axis. Distinct such points have intersecting supports, so their representatives are distinct. The A-axis has a points, proving r≤a.

A finite planar lower ideal with r mixed minimal excluded points has r+1 maximal points. This follows immediately by listing its nonempty columns in increasing first coordinate: every strict drop of column height contributes one mixed excluded corner, and each constant-height run ends in one maximal point.

Because T has no interior excluded corner, it is its pairwise closure. Its slices have the form

F_x=F∩([0,B_x−1]×[0,C_x−1]), 0≤x<a,

where B_x and C_x are positive, nonincreasing integers; B_0,C_0 are the corresponding axis lengths of F. Intersecting a planar lower ideal with a rectangle cannot increase its number of maximal points: express F as the union of its r+1 anchored maximal boxes, intersect each box with the rectangle, and observe that the maximal points of the union are drawn from these r+1 clipped box tops. Therefore each F_x has at most r+1 maxima and T has at most a(r+1) maxima.

For the cell bound, recall that compression partitions each coordinate at all positive levels z_j+1 belonging to a maximal point z of T, together with level zero. Every maximal point of T is the top of a maximal point of one of its slices. In the B coordinate, each such positive level is either a B-coordinate level from a maximal point of F, or one of the truncation levels B_x, 1≤x<a. There are at most (r+1)+(a−1)=r+a such levels. The same bound holds in the C coordinate. The A coordinate has at most a intervals, since its integer range is 0,...,a−1. Hence K≤a(a+r)²≤4a³.

The established slab theorem states m≥4K−2⇒W_4≥0. Substitution gives the displayed cutoffs. ∎

**Complete exponent-two case.** If a=2, then the bound on maximal points is at most 2(2+1)=6. Thus the prior complete six-final-window theorem applies and proves Wilf for every such semigroup, without a multiplicity restriction. This deduction inherits that theorem's computer-assisted finite part. It is an easily checked generator criterion for a class already included in the project's six-point theorem, not a claim that the residual six-point class has been extended.

In particular, **if m divides 2A for any nonmultiplicity minimal generator A, then Wilf holds.** Minimality makes the first critical exponent at least two, while 2A being a multiple of m makes it at most two. Equivalently this covers every minimally four-generated semigroup ⟨2p,(2q+1)p,B,C⟩ whose multiplicity is 2p.

For a=3 the coarse multiplicity cutoff is m≥430. More generally, a putative counterexample in the critical pure-axis class must satisfy m≤16a³−3. The remaining finite ranges for a≥3 have not been exhaustively verified here.


In particular, if a nonmultiplicity minimal generator A satisfies m | 2A, its first critical exponent is exactly two: A itself is not representable by the other generators, while 2A is a multiple of m. The exponent-two corollary therefore applies.

The slab theorem used here is included in the archive as `boundary/slab_theorem.md`.

---

# Part IV. The remaining proof obligation

The prior analytic four-generator conductor reduction establishes
\[
W_4<0\quad\Longrightarrow\quad
M\le m(m-2),\qquad c\le m^2-3m+1,\qquad a_3\le m(m-2).
\]
Its full proof is included in the archive as
`dependencies/wilf_edim4_global_finite_reduction_2026-09-05.md`.
It treats full weighted staircases analytically and counts the line slack
created by low-weight excluded corners in all other cases. This sharper
bound is separate from the general conductor lemma in Part I.

Combining it with Part II and the published verification through multiplicity
19 leaves the necessary counterexample region
\[
\boxed{
20\le m<2\times10^{14},\qquad
m<a_1<a_2<a_3\le m(m-2),\qquad
c\le m^2-3m+1.
}
\]
The generators must be minimal and have greatest common divisor one. The
six-point theorem additionally forces at least seven final-window Apéry
points. Part III excludes the interior corner \((1,1,1)\).

**No theorem or completed enumeration here proves that this finite region is
empty. No numerical semigroup with negative Wilf number was found.**
The missing step is a universal inequality or an exhaustive certificate for
the surviving smaller-multiplicity staircases. Finiteness alone supplies
neither. The upper bound is much too large for a naive loop over generators.

## Other completed structural work

The archive includes full proofs of the following reductions.

- For an interior minimal excluded point \(p=(r,s,t)\), put \(P=r+s+t\).
  Each coordinate plane has at most \(P-2\) mixed minimal excluded points,
  and the whole staircase has at most \(P(P-1)\) coordinatewise maxima.
  This recovers the six-maxima bound at \(P=3\), but does not close
  \(P\ge4\).
- If the least multiple of some nonmultiplicity generator \(A\) that is
  representable by the other generators is \(aA=bm\), the staircase has
  **no** full-support minimal excluded point. This includes the secondary
  class in Chomicz's terminology. Absence of an interior corner does not
  force at most six final-window points.
- The secondary class has an exact description in terms of two matching
  quotients of two-generated semigroups, with additional membership
  implications stated in `round2/type/secondary_structure_report.md`.
  This does not yet give the conductor/genus estimate needed for Wilf.

## Failed closing arguments, with concrete certificates

1. **A stronger continuous gap of \(1/3\) is false.** The finite lower ideal
   \[
   T=\{(x,y,z)\in\mathbb N^3:x+y,x+z,y+z\le45,
                         \min(x,y,z)\le5\}
   \]
   has one interior corner \((6,6,6)\). Its normalized rectangular
   thickening has
   \(\kappa_c=84021/262721<1/3\). This disproves that auxiliary
   geometric claim; it is not a numerical-semigroup counterexample.
2. **Uniform inflation does not propagate a counterexample.** Keeping one
   generator \(a\) and multiplying the other three by \(q\), with
   \(\gcd(a,q)=1\), gives
   \[
   W'=qW+(q-1)(a-1).
   \]
   This moves the Wilf number upward. The exact analysis also excludes
   amplification through repeated such lifts while changing the retained
   generator. An individual four-generator counterexample would disprove
   the overall conjecture, but it would not automatically disprove every
   larger embedding-dimension case.
3. **The forest overlap certificate is not universal.** For
   \(S=\langle175,185,201,202\rangle\), the tested sufficient forest
   certificate is \(-9\), while the actual Wilf number is \(862\).
   Thus that certificate cannot close all remaining cases.
4. **Secondary does not imply small final window.**
   \(\langle1558,1599,1675,2546\rangle\) is secondary and has 12
   final-window points, conductor 62204, \(n=27157\), and \(W_4=46424\).
   It also disproves using the new no-interior theorem to infer the
   six-point hypothesis.

These failures are preserved so that later work does not silently reinstate
an invalid lemma.

## Exact computations and their scope

A complete finite classification covered all 4,095 lower ideals strictly
between the degree-three and degree-four coordinate-face staircases.
Seven fail the ordered geometric relaxation; residue arguments exclude all
seven. Each LP value was checked with rational primal and dual certificates.
This is a complete result for the specified family, not for all staircases.

A separate seeded diagnostic produced 91,122 minimally four-generated
semigroups and 65,012 distinct Apéry shapes at multiplicities 20 through
1,000. None failed the ordered geometric sufficient bound. The random and
targeted diagnostics are evidence for further conjectures, not proof
dependencies of Parts I or II. The archive identifies exhaustive runs and
nonexhaustive searches separately in their individual reports.

## Relation to primary literature

- A. Zhai, *An asymptotic result concerning a question of Wilf*,
  [arXiv:1111.2779](https://arxiv.org/abs/1111.2779). Lemma 3 is the
  weighted lower-ideal inequality underlying the line identity. Theorem 2
  establishes an approximate lower density bound \(n/c>1/e-\varepsilon\)
  outside a finite set, for fixed \(e\) and fixed \(\varepsilon>0\).
  That statement allows infinitely many violations tending to \(1/e\);
  it does not itself establish the finite-counterexample conclusion of
  Part I.
- M. Hellus, A. Rechenauer and R. Waldi, *Variants on a question of Wilf*,
  [arXiv:1804.06141](https://arxiv.org/abs/1804.06141), Proposition 2.6.
  The full-support corner restriction is established background; the short
  residue proof is restated in Part I.
- W. Bruns, P. A. García-Sánchez, C. O'Neill and D. Wilburne,
  [arXiv:1903.04342](https://arxiv.org/abs/1903.04342), and J. Kliem and
  C. Stump, *A new face iterator for polyhedra and more general finite locally
  branched lattices*,
  [arXiv:1905.01945](https://arxiv.org/abs/1905.01945), supply the published
  small-multiplicity verification through 19 used above.
- K. Chomicz, *The type and cardinality of minimal presentations of numerical
  semigroups with embedding dimension four*,
  [arXiv:2609.04000v1](https://arxiv.org/html/2609.04000v1), provides the
  primary/secondary classification used in the supplementary structural
  investigation. It does not settle Wilf in embedding dimension four.

A targeted primary-source comparison found no matching fixed-embedding-
dimension finiteness theorem. That search does not establish novelty; the
proofs and their correctness are the claims being presented for review.
