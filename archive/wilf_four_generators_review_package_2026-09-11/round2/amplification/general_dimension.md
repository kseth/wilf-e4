# Explicit eventual Wilf and finite reduction in every fixed embedding dimension

**Research derivation, 5 September 2026.** This note supplies a self-contained
generalization of the stability argument to every fixed embedding dimension
`e=d+1>=3`. It proves an explicit sufficient multiplicity threshold, and,
using the root agent's difference-set exclusion of discrete simplexes, a
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

This argument was supplied by the root agent and independently checked here.

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
