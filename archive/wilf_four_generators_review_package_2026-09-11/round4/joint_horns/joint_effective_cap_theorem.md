# Joint optimization of three effective-cap horns

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
