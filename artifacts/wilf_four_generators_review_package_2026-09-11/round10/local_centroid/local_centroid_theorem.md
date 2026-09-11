# A local centroid lemma for the residual four-generator class

11 September 2026. **Complete exact enumeration supports the strengthened inequality below. A structural proof eliminating the remaining enumeration has not been obtained.**

## The class

Let `T` be a finite lower ideal in `N^3`, `m=|T|>=30`, with total degree at most six. Assume that it has exactly one full-support minimal excluded point `p`, with `5<=|p|_1<=7`. Assume only these additional restrictions:

1. Every coordinate-plane projection has at most `|p|_1-2` mixed minimal excluded points.
2. For `F_i={x in T:x+e_i not in T}` and `n_i=1+max_T x_i`, one has `|F_i intersect F_j|<=2 n_k` when `{i,j,k}={1,2,3}`.

These are necessary conditions for the genuine Apéry ideals in the residual proof. The earlier erosion condition and the refined count of plane corners dominating the corresponding projection of `p` are not hypotheses of this lemma.

Write `s=sum_T x` and `q_i=max_T x_i`, so all `q_i>0`.

## Construction 1: move each coordinate-line top at most two steps

Partition `T` into nonempty lines in each of its three coordinate directions. For every such line, write `t` for its top and `L=t_i+1` for its length. Let

\[
\rho(t)=\max\{|v|_1:v\in\mathbb N^3,\ |v|_1\le2,\ t+v\in T\}.
\]

This number is either 0, 1, or 2 and uses only nine possible successors: the three one-step and six two-step moves. Choose one `v(t)` attaining it and define

\[
U_2(T)=\sum_\ell L_\ell\rho(t_\ell),\qquad
z_2=\frac1{3m}\sum_\ell L_\ell(t_\ell+v(t_\ell)).
\]

The coordinate-line identities

\[
\sum_\ell L_\ell=3m,\qquad
\sum_\ell L_\ell t_\ell=4s
\]

give

\[
z_2\in\operatorname{conv}(T),\quad
r_2=3mz_2-4s=\sum_\ell L_\ell v(t_\ell)\ge0,\quad
\sum_i(r_2)_i=U_2(T).
\]

To prove the moment identity, fix coordinate `j`. Lines in direction `j` contribute twice `sum_T x_j`, because `(t_j+1)t_j=2 sum_{k=0}^{t_j} k`. Each other direction contributes `sum_T x_j`, because coordinate `j` is constant on those lines.

## Construction 2: use only the three axis endpoints

Put

\[
G(T)=q_*\left(3m-4\sum_{i=1}^3\frac{s_i}{q_i}\right),\qquad q_*=\max_i q_i.
\]

If `G>=0`, assign mass `lambda_i=4s_i/(3m q_i)` to the point `q_i e_i`. Their total mass is at most one. Assign the remaining mass to any longest-axis endpoint. The resulting point `z_A` satisfies

\[
z_A\in\operatorname{conv}(T),\quad r_A=3mz_A-4s\ge0,
\quad \sum_i(r_A)_i=G(T).
\]

All its surplus is in the chosen longest-axis coordinate.

## The computer-assisted inequality

For the entire class stated above, the complete exact enumeration gives

\[
\boxed{\max\{U_2(T),G(T)\}\ge m.}
\]

Hence one of these two elementary constructions gives

\[
\boxed{z\in\operatorname{conv}(T),\qquad 3mz-4s\ge0,
\qquad\sum_i(3mz_i-4s_i)\ge m.}
\]

For every real vector `b` with `b_i>=1` and `H>=max_T b.x`, this proves

\[
3mH-4b\cdot s\ge b\cdot(3mz-4s)\ge m.
\]

This improves the previous `m-29/10` constant to `m`, covers a larger geometric class, and replaces millions of LP dual assignments with two explicit formulas. It still requires checking the finite class.

## Exact coverage

| Corner | Shapes | Pass local two-step construction | Need axis fallback | Minimum of `max(U2,G)-m` |
|---|---:|---:|---:|---:|
| (1,1,3) | 1,581,961 | 1,581,746 | 215 | 0 |
| (1,2,2) | 1,433,543 | 1,433,331 | 212 | 0 |
| (1,1,4) | 874,540 | 874,537 | 3 | 0 |
| (1,2,3) | 638,574 | 638,573 | 1 | 2 |
| (2,2,2) | 592,453 | 592,453 | 0 | 4 |
| (1,1,5) | 159,580 | 159,580 | 0 | 10 |
| (1,2,4) | 105,119 | 105,119 | 0 | 13 |
| (1,3,3) | 94,500 | 94,500 | 0 | 21 |
| (2,2,3) | 94,374 | 94,374 | 0 | 31 |
| **Total** | **5,574,644** | **5,574,213** | **431** | **0** |

Independently, the axis construction succeeds on 3,011,728 shapes; this overlaps the local construction. The fallback column counts only shapes where `U2<m`.

The exhaustive scope contains 85,392,579 axis-compatible profile triples, 26,252,336 of degree at most six, 26,153,719 of multiplicity at least thirty, and 5,574,644 passing the three pairwise surface bounds. There is no erosion rejection and no refined dominating-corner rejection.

## Verification

The bitset producer is `round10/ablation/local2_no_upper.cpp`. The independent source in this folder generates planar profiles from seven-element subsets and builds literal column-height arrays. It checks the same geometric class and computes the local move length through six explicit two-step membership tests. It directly checks both line identities for every accepted shape. The axis expression is computed with the integer denominator `q_1 q_2 q_3`. It does not use floating-point arithmetic, linear programming, a maximal-point registry, a reverse dynamic program, or any external certificate stream.

Run the complete independent replay using only Python standard library and a C++17 compiler:

```sh
python3 round10/local_centroid/verify_complete_local_centroid.py
```

The entry point checks the source manifest, compiles into a temporary directory, performs a fresh complete enumeration, and compares all nine coverage records and all multiplicity histograms. The final source checks output I/O failures and explicitly closes every diagnostic stream before reporting success. The records of one earlier auxiliary dump were incomplete; no proof step used that dump, and the portable replay reconstructs and validates all 431 fallback records before saving them.

## Implication and limitation

In the surrounding proposed Wilf argument, `A=min(a_1,a_2,a_3)>=m+1`, and

\[
mW_4=AD_0-m(m-1).
\]

For a genuine semigroup whose preferred Apéry ideal lies in this class, `D0>=m` therefore gives

\[
\boxed{W_4\ge A-m+1\ge2.}
\]

Other multiplicity, corner, and high-degree classes remain separate proof dependencies. External mathematical review and formalization have not been performed.

The analytic statement still to prove without enumeration is the simple inequality `max(U2,G)>=m` from the stated plane-corner and surface restrictions. One possible charging argument starts with the universal bound

\[
U_2(T)\ge3m-\sum_{u\in\operatorname{Max}(T)}(|u|_1+3),
\]

then uses the additional unit of gain at tops admitting a two-step successor. Both constructions and the line identities extend to `N^d`, with `3m` replaced by `dm` and `4s` by `(d+1)s`; the all-case bound for their union has only been verified in the stated three-coordinate finite class.
