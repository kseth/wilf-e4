# A genuinely unequal three-arm vertex in the weighted geometric relaxation

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
