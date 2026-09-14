# Phase and rectangular thickening for finite lower ideals

## Status and purpose

This note completes task G4. It proves the dimension-three phase inequality
and the exact discrete-to-continuous thickening identity used in branches B2,
B4, and B6. It also records the strict and weak endpoints needed when those
branches are reduced to closed parameter boxes. There is no computer-assisted
assertion here.

The historical archive contains an earlier, coarser phase estimate in arbitrary
dimension. The present proof retains only the sharper dimension-three summed
inequality: it is shorter and is the estimate actually used by all three
downstream branches.

## 1. Common normalization

Let \(T\subseteq\mathbb N^3\) be a finite lower ideal containing
\(0,e_1,e_2,e_3\), and let \(m=|T|\). Fix positive weights
\(w=(w_1,w_2,w_3)\), and put

\[
H=\max_{x\in T}w\mathbin\cdot x,
\qquad B=w_1+w_2+w_3,
\qquad D_0=3mH-4w\mathbin\cdot\sum_{x\in T}x.
\tag{1}
\]

Since the coordinate units belong to \(T\), \(H\ge w_i\) for every \(i\).
Normalize by height:

\[
u_i=\frac{w_i}{H},\qquad
v=\min_i u_i,\qquad U=\max_i u_i,\qquad
\sigma=u_1+u_2+u_3=\frac BH.
\tag{2}
\]

Thus \(0<v\le U\le1\) and
\(\max_{x\in T}u\cdot x=1\). If \(X\) is uniformly distributed on \(T\),
write

\[
\mu_i=\mathbb E(u_iX_i),\qquad
\mu=\mu_1+\mu_2+\mu_3,
\qquad
\kappa=3-4\mu=\frac{D_0}{mH}.
\tag{3}
\]

For the preferred Apéry ideal, the notation of
[`foundations.md`](foundations.md) has
\(w_i=a_i/A\), where \(A=\min_i a_i\), and \(H=M/A\). Consequently

\[
u_i=\frac{a_i}{M},\qquad v=\frac1H,
\tag{4}
\]

after permuting coordinates so that a least weight comes first.

For \(j\in\{1,2,3\}\) and \(x\in T\), let \(t_j(x)\) be the top of the
coordinate-\(j\) line through \(x\), and define its normalized top slack by

\[
\delta_j(x)=1-u\mathbin\cdot t_j(x)\ge0,
\qquad \bar\delta_j=\mathbb E\delta_j(X).
\tag{5}
\]

The direction-\(j\) line-top identity in
[`coordinate-lines.md`](coordinate-lines.md) gives

\[
\bar\delta_j=1-\mu-\mu_j
=\frac{1+\kappa}{4}-\mu_j,
\qquad
\boxed{\bar\delta_1+\bar\delta_2+\bar\delta_3=\kappa.}
\tag{6}
\]

In particular, \(\kappa\ge0\). Notice that this conclusion uses only lower
closure and the maximum defining \(H\), not residue labels or any restriction
on the minimal excluded points.

## 2. Exact rectangular thickening

Let

\[
\Delta=\{y\in\mathbb R_{\ge0}^3:y_1+y_2+y_3\le1\}.
\]

For \(x\in T\), define the half-open box

\[
Q_x=\prod_{i=1}^3
\left[
\frac{w_ix_i}{H+B},
\frac{w_i(x_i+1)}{H+B}
\right),
\qquad
K=\bigcup_{x\in T}Q_x.
\tag{7}
\]

### Proposition 2.1 (thickening identity and excluded supports)

The set \(K\) is a bounded measurable downset of positive volume contained in
\(\Delta\). If \(Y\) is uniformly distributed on \(K\), then

\[
\boxed{
\kappa_c(K):=3-4\mathbb E(Y_1+Y_2+Y_3)
=\frac{D_0/m+B}{H+B}
=\frac{\kappa+\sigma}{1+\sigma}.
}
\tag{8}
\]

If \(P\) is the set of minimal points of
\(\mathbb N^3\setminus T\), then, in the nonnegative orthant,

\[
\mathbb R_{\ge0}^3\setminus K
=\bigcup_{p\in P}
\left(
\left(\frac{w_1p_1}{H+B},
             \frac{w_2p_2}{H+B},
             \frac{w_3p_3}{H+B}\right)
+\mathbb R_{\ge0}^3
\right).
\tag{9}
\]

Thus diagonal thickening preserves the support of every minimal excluded
point. In particular, the properties “no full-support minimal exclusion” and
“at most one full-support minimal exclusion” pass from \(T\) to \(K\).

#### Proof

Before division by \(H+B\), the boxes form the weighted rectangular grid with
side lengths \(w_1,w_2,w_3\). Lower closure of \(T\) makes their union a
downset. If \(y\in Q_x\), then

\[
y_1+y_2+y_3
<\frac{w\cdot x+B}{H+B}\le1,
\]

so \(K\subseteq\Delta\). The boxes have disjoint interiors and the same
positive volume \(w_1w_2w_3/(H+B)^3\).

The mean of the coordinate sum on \(Q_x\) is

\[
\frac{w\cdot x+B/2}{H+B}.
\]

Equal cell volumes therefore give

\[
\mathbb E(Y_1+Y_2+Y_3)
=\frac{w\cdot\mathbb E X+B/2}{H+B}.
\]

Substitution into the definition of \(\kappa_c\), followed by (1)--(3),
proves (8).

For (9), first work in the unscaled grid. The unique half-open grid box
containing \(z\in\mathbb R_{\ge0}^3\) has index

\[
\left(\left\lfloor\frac{z_1}{w_1}\right\rfloor,
      \left\lfloor\frac{z_2}{w_2}\right\rfloor,
      \left\lfloor\frac{z_3}{w_3}\right\rfloor\right).
\]

This index lies outside \(T\) exactly when it dominates some \(p\in P\),
which is equivalent to \(z_i\ge w_ip_i\) for all \(i\). Rescaling proves
(9). Positive diagonal scaling preserves both coordinatewise minimality and
zero coordinates, so the support assertion follows. \(\square\)

The half-open convention matters only on cell boundaries; it is what makes
the complement in (9) a union of closed upper orthants without an exceptional
boundary set. It has no effect on the volume or mean calculation.

## 3. A sawtooth integral

For \(q>0\), write \([r]_q\in[0,q)\) for the representative of \(r\) modulo
\(q\).

### Lemma 3.1

Every interval \(I\subseteq\mathbb R\) of length \(h\ge0\) satisfies

\[
\int_I[r]_q\,dr\ge\frac{qh^2}{2(h+q)}.
\tag{10}
\]

#### Proof

Write \(h=nq+r_0\), where \(n\in\mathbb N\) and \(0\le r_0<q\). The interval
contains \(n\) complete periods and one arc of length \(r_0\) on the residue
circle. A complete period has integral \(q^2/2\), while an arc of length
\(r_0\) has integral at least \(r_0^2/2\), with equality for the arc beginning
at residue zero. Hence

\[
\int_I[r]_q\,dr
\ge\frac{nq^2+r_0^2}{2}
\ge\frac{h^2}{2(n+1)}
\ge\frac{qh^2}{2(h+q)}.
\]

The middle inequality is Cauchy--Schwarz applied to \(n\) copies of \(q\)
and one copy of \(r_0\); the last uses \(n+1\le(h+q)/q\). The case \(h=0\)
is immediate. \(\square\)

## 4. The phase inequality

Choose an index \(k\) with \(u_k=v\). For either of the other two indices,
write \(j\ne k\).

### Proposition 4.1 (one-direction phase estimate)

For each \(j\ne k\),

\[
\boxed{
2\bar\delta_j(1+v+u_j)
\ge2u_j\mu_k-v(1+v).
}
\tag{11}
\]

#### Proof

Fix a coordinate-\(k\) line of length \(L\), parametrized by
\(x(t)=x(0)+te_k\) for \(0\le t<L\). Modulo \(u_j\), the slack of the top of
the coordinate-\(j\) line through \(x(t)\) has the form

\[
\delta_j(x(t))\equiv\theta-tv\pmod{u_j}
\]

for a constant \(\theta\) depending on the line. Since the slack is
nonnegative,

\[
[\theta-tv]_{u_j}\le\delta_j(x(t)).
\]

For \(0\le r\le v\), the elementary sawtooth bound

\[
[\theta-tv+r]_{u_j}
\le[\theta-tv]_{u_j}+r
\le\delta_j(x(t))+r
\]

holds whether or not the residue wraps through zero. The \(L\) intervals
\([\theta-tv,\theta-tv+v]\) concatenate, up to endpoints, into a single
interval \(I\) of length \(h=Lv\). Integration and Lemma 3.1 give

\[
\frac{u_jh^2}{2(h+u_j)}
\le\int_I[r]_{u_j}\,dr
\le v\sum_{t=0}^{L-1}\delta_j(x(t))+\frac{Lv^2}{2}.
\]

The line top belongs to \(T\), so \(v(L-1)\le1\) and \(h\le1+v\).
After division by \(Lv\),

\[
\frac1L\sum_{t=0}^{L-1}\delta_j(x(t))
\ge\frac{u_jvL}{2(1+v+u_j)}-\frac v2.
\tag{12}
\]

Average (12) over the coordinate-\(k\) lines, weighting a line by its length
divided by \(m\). If their lengths are \(L_F\), then

\[
\frac v m\sum_F L_F^2
=\frac v m\sum_F\bigl(L_F(L_F-1)+L_F\bigr)
=2\mu_k+v.
\tag{13}
\]

Substitution into the averaged form of (12) gives exactly (11). \(\square\)

### Theorem 4.2 (summed phase inequality)

Under the normalization of Section 1,

\[
\boxed{
\sigma(1-3\kappa)
\le4\kappa+5v-3\kappa v+4v^2.
}
\tag{14}
\]

No hypothesis on residue labels or minimal excluded points is required.

#### Proof

Sum (11) over the two indices \(j\ne k\). Since every slack is nonnegative,
(6) gives

\[
(\sigma-v)\mu_k
\le(1+v+U)(\kappa-\bar\delta_k)+v(1+v).
\tag{15}
\]

Use \(\mu_k=(1+\kappa)/4-\bar\delta_k\). The result is

\[
\frac{(\sigma-v)(1+\kappa)}4
\le(1+v+U)\kappa+v(1+v)
+\bar\delta_k\bigl[(\sigma-v)-(1+v+U)\bigr].
\tag{16}
\]

If the remaining weights are \(w\le U\), the coefficient in brackets is
\(w-1-v\le0\), because \(w\le1\). We may discard that term. Moreover,
\(U\le\sigma-2v\), and \(\kappa\ge0\), so

\[
(\sigma-v)(1+\kappa)
\le4\kappa(1+\sigma-v)+4v(1+v).
\]

Expansion and rearrangement give (14). \(\square\)

## 5. Downstream forms and endpoint audit

For the Apéry normalization, permute the weights and write
\(w=(1,b,c)\), so that

\[
1\le b\le c\le H,
\qquad B=1+b+c,
\qquad v=\frac1H,
\qquad \sigma=\frac BH.
\tag{17}
\]

All later uses begin with a putative failure satisfying \(D_0<m\). By (3),

\[
0\le\kappa<v.
\tag{18}
\]

If \(H>3\), division of (14) by \(1-3\kappa>0\) is legitimate. For fixed
\(v\), the resulting right side is strictly increasing in \(\kappa\), because
its derivative has numerator

\[
4+12v+12v^2>0.
\]

Using the strict inequality in (18) and then substituting (17) gives the
common phase cutoff

\[
\boxed{B<9+\frac{28}{H-3}.}
\tag{19}
\]

Now suppose a continuous theorem for the relevant excluded-orthant class
supplies the weak bound \(\kappa_c(K)\ge\gamma\). Equation (8) gives the
always-valid lower estimate

\[
\boxed{
\frac{D_0}{m}\ge\gamma H-(1-\gamma)B.
}
\tag{20}
\]

Under the failure hypothesis (18), the same identity instead gives the strict
clipping condition

\[
\boxed{\gamma H<1+(1-\gamma)B.}
\tag{21}
\]

The three later applications are as follows.

1. **B2 (no full-support corner).** The
   [B2.1 compactness note](no-corner-compactness.md) proves the continuous
   gap \(\gamma=1/3\). If \(H\le3\), then \(H<24\) already. If \(H>3\),
   combine (19) and (21) to obtain

   \[
   H^2-24H+7<0,
   \qquad H<12+\sqrt{137}<24.
   \tag{22}
   \]

   Also, (20) becomes

   \[
   \frac{D_0}{m}\ge\frac{H-2B}{3}.
   \tag{23}
   \]

   Hence the analytic leaf condition \(H\ge2B+3\) proves \(D_0\ge m\),
   including equality at the endpoint.

2. **B4 (the corner \(p\sim(2,1,1)\)).** The separate planar estimate used
   in that branch is \(D_0/m\ge(H-4B)/3\). If \(H\ge6\) and \(D_0<m\), it
   gives \(H<3+4B\). Combining this strict inequality with (19) gives

   \[
   H^2-42H+5<0,
   \qquad H<42.
   \tag{24}
   \]

3. **B6 (residual degree at least seven).** The later finite-to-continuous
   theorem supplies \(\gamma=5/42\), while the branch itself has \(H\ge7\).
   Equations (19) and (21) give

   \[
   5H<42+37B,
   \qquad 5H^2-390H+89<0,
   \qquad H<78.
   \tag{25}
   \]

The actual failure regions are therefore open at the respective integer upper
bounds 24, 42, and 78. A finite certificate may harmlessly cover the larger
closed boxes ending at those integers. Conversely, (20) is a weak inequality:
equality in a leaf condition such as \(H=2B+3\) must be retained and is
already sufficient.
These conventions prevent the later interval arguments from losing either a
boundary failure or a valid analytic leaf.

## 6. Retained interface

The rest of the proof may use G4 through the following four statements only:

1. the exact thickening identity (8) and support preservation (9);
2. the phase inequality (14), valid for every finite lower ideal containing
   the coordinate units;
3. the common strict cutoff (19) whenever \(H>3\) and \(D_0<m\);
4. the weak and strict continuous consequences (20)--(21).

The numerical bounds (22), (24), and (25) are algebraic corollaries, not
additional lemmas or computational inputs.
