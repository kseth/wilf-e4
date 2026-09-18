# A universal potential for horns based at or beyond one third

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

## 4. An exact obstruction to a stronger boundary-only potential

It is false that an arbitrary horn is bounded by the larger of zero and
the optimum among boundary profiles using its original transverse caps.
Take central sides

\[
(a,B,C)=\left(\frac1{20},\frac3{20},\frac45\right).
\]

For the horn outward in coordinate `a`, reduce the smaller effective cap
to `x=1/20`, keep `y=4/5`, and use a constant prefix followed by the
balanced taper. Exact integration gives

\[
H\left(\frac1{20};\frac1{20},\frac45\right)
 =\frac{613}{1920000}>0.
\]

The optimum over boundary profiles with the original caps `(3/20,4/5)`
is instead `-1/4800`, using the boundary-profile theorem in
`horns_audit.md`. Thus clipping that boundary potential at zero still
fails. Effective caps and slack must be addressed for bases below `1/3`.
This example refutes only that proposed horn potential; it does not refute
the full mean inequality or Wilf's conjecture.

## Status of the remaining Bellman problem

For a tight state with transverse side sum `r`, a jump to caps `(x,y)`
earns

\[
\left(1-\frac32r\right)(r-x-y)xy.
\]

A prospective earlier-base potential takes the supremum of one such jump
followed by the exact boundary-profile potential. Numerical dynamic
programming suggests that additional jumps do not improve it. A Bellman
inequality proving that statement, and a bound summing the resulting
three horn potentials against the central-box deficit, remain unresolved.
No general no-interior-corner moment theorem is asserted here.
