# Independent audit of the three-horn structure and a sharp continuous subclass

## Structural audit

The proof in `round3/no_interior/clique_tree_and_bipartite_bound.md` is valid.
For a finite lower ideal in three dimensions whose excluded minimal points
have support at most two, membership is determined by the three pair
projections. In the graph of coordinate levels, levels in a coordinate
class form a clique and their external neighborhoods are nested. Any
induced cycle of length at least four repeats a class. Its repeated levels
must be adjacent, and nesting then supplies a chord. Hence the graph is
chordal, with its maximal cliques corresponding to maximal boxes.

A clique tree supplies connected superlevel sets for each coordinate.
A leaf has a coordinate value larger than its neighbor's. Connectedness
implies that this coordinate value exceeds that at every other node.
Thus this leaf owns the unique global maximum of that coordinate. Different
leaves own different coordinates, giving at most three leaves.

One detail worth making explicit in the median argument is that **every
leaf must be among any chosen three coordinate-maximum nodes**. Its owned
global maximum has no other attaining node. The subtree spanned by the
three chosen nodes therefore includes every leaf and is the whole tree.
Their median partitions the tree into at most three arms, each with exactly
one coordinate maximum beyond the median. Along that arm the associated
coordinate increases and the other two decrease, by connectedness of
coordinate superlevel sets. Distinct maximal boxes prevent a stationary
outward coordinate between consecutive nodes.

This proves the central-box plus three rectangular-fiber horns description.
No assertion about the unproved full moment inequality is needed for this
structural result.

## Moment notation

After positive diagonal scaling, take the height functional to be `x+y+z`
and its maximum to be `M`. Put

\[
\mathcal J(K)=\int_K(3(x+y+z)-2M)\,dV.
\]

The desired mean bound is precisely `J(K)<=0`. A central box with side
lengths `a,b,c` and `a+b+c=M` contributes `-Mabc/2`.

For an outward coordinate `t`, a horn fiber `[0,f(t)]×[0,g(t)]` contributes

\[
f(t)g(t)\left(3t+\frac32(f(t)+g(t))-2M\right)dt.
\]

## A sharp maximal-product taper family

Assume the central box lies on the height boundary: `a+b+c=M`.
For a horn whose two initial side lengths are `x<=y`, start its outward
coordinate at `t=M-x-y`. Keep the smaller side equal to `x` while the other
side decreases as `M-t-x`, until `t=M-2x`. Thereafter set both sides equal
to `(M-t)/2`, until `t=M`. These fibers are nested and all their upper
corners have height `M`.

Writing `u=M-t`, this horn's contribution is exactly

\[
\begin{aligned}
J(x,y)
&=\int_{2x}^{x+y}x(u-x)\left(M-\frac32u\right)du
  +\int_0^{2x}\frac{u^2}{4}\left(M-\frac32u\right)du\\
&=\frac{Mx^3}{6}-\frac{x^4}{4}
  +\frac{Mxy^2}{2}-\frac{3x^2y^2}{4}-\frac{xy^3}{2}.
\end{aligned}
\]

Suppose `a<=b<=c`, and write `p=b-a`, `q=c-b`. Adding the three horns and
the central box, direct polynomial expansion gives

\[
\boxed{\mathcal J(K)
 =J(b,c)+J(a,c)+J(a,b)-\frac{Mabc}{2}
 =-\frac{p^4}{6}-\frac{p^3q}{3}-\frac{p^2q^2}{4}\le0.}
\]

This proves the desired continuous mean bound for this entire family.
Equality holds whenever the two smallest central sides agree. In
particular, the central cube of side `M/3` together with three horns of
equal fiber sides `(M-t)/2` has mean `2M/3`. For `M=1` its volume is `1/9`.

## What remains unproved

The taper family has not been proved extremal among arbitrary nested horn
profiles. An individual full-cap horn can have a negative contribution,
whereas omitting it contributes zero, so maximizing each horn cannot be
replaced automatically by the displayed full-cap construction. Effective
initial caps, arbitrary profiles, and a central corner of height below `M`
remain to be controlled. The structural theorem alone does not bridge
these gaps.

## Arbitrary profiles on the height boundary

There is a stronger theorem when the central corner has height `M` and
**every** horn fiber top has height `M`. This allows arbitrary nested
rectangular fibers, not just the prescribed taper above.

Write `u=M-t` along a horn. Its two sides satisfy `f(u)+g(u)=u`, and both
are nondecreasing in `u`. Relabel them pointwise as their minimum and
maximum. This preserves monotonicity and the ordered endpoint caps
`x<=y`; hence assume `f<=g`. The function `f` is nondecreasing and
1-Lipschitz, is at most `u/2`, and ends at `f(x+y)=x`. The horn integral is

\[
\int_0^{x+y} f(u)(u-f(u))\left(M-\frac32u\right)du.
\]

For `u<=u_*=2M/3`, this integrand increases with `f` on `0<=f<=u/2`.
For `u>=u_*`, it decreases with `f`. If the horn extends past `u_*`, fix
`k=f(u_*)`. On the positive part, monotonicity gives
`f(u)<=min(u/2,k)`, and this upper envelope is admissible. On the negative
part, monotonicity and the terminal cap give
`f(u)>=max(k,u-y)`, and this lower envelope is admissible. Thus a maximizing
profile has exactly three phases:

\[
f(u)=\begin{cases}
u/2,&0\le u\le2k,\\
k,&2k\le u\le y+k,\\
u-y,&y+k\le u\le x+y.
\end{cases}
\]

Admissibility requires
`max(0,u_*-y)<=k<=min(x,u_*/2)`. If the whole horn lies before `u_*`, the
pointwise maximizing profile is simply `f(u)=min(u/2,x)`.

For the three-phase profile the integral is

\[
J(k,y)+\int_{y+k}^{x+y} y(u-y)\left(M-\frac32u\right)du,
\]

whose derivative in `k` is

\[
\frac12(k-y)^2(M-2k-y).
\]

Now order the central sides `a<=b<=c`, with sum `M`. The horn outward in
coordinate `c` lies entirely in the positive part. For the horn outward in
coordinate `b`, the maximizing `k` is its full smaller cap `a`. Only the
horn outward in coordinate `a` can improve the full-cap taper; its optimum
is `k=(a+b)/2`, which lies in the admissible interval because `c>=M/3`.

Set `p=b-a`, `q=c-b`. The last horn's improvement over the full-cap taper
is exactly

\[
\int_0^{p/2}\frac12(q+r)^2(p-2r)\,dr
 =\frac{p^2q^2}{8}+\frac{p^3q}{24}+\frac{p^4}{192}.
\]

Combining with the full-cap identity proves

\[
\boxed{\mathcal J(K)
 \le-\frac{p^2q^2}{8}-\frac{7p^3q}{24}
     -\frac{31p^4}{192}\le0.}
\]

Thus **all** nested horn profiles on the height boundary satisfy the
desired mean bound. Allowing slack `t+f(t)+g(t)<M` remains outside this
argument: then `f+g=u` and the resulting 1-Lipschitz constraint are lost.

## Effective-cap family and useful derivative factorizations

An enlarged family allows an outward central coordinate `a` and effective
fiber caps `x<=y` whose sum is at most `M-a`. Hold these caps constant until
`t=M-x-y`, then use the taper above. Its horn contribution is

\[
H(a;x,y)=J(x,y)+\frac{xy}{2}(M-a-x-y)(3a-M).
\]

The initial constant slab gives the extra term. Direct differentiation
yields

\[
\frac{\partial H}{\partial y}
 =\frac{x}{2}(M-a-x-y)\bigl(3(a+y)-M\bigr),
\]

and on the diagonal,

\[
\frac{d}{dz}H(a;z,z)
 =z(M-a-2z)\bigl(3(a+z)-M\bigr).
\]

In the admissible ranges, the only possible interior sign changes of these
derivatives are from negative to positive. Hence for fixed smaller cap,
the larger cap maximizes at an endpoint: equal to the smaller cap, or at
its allowed upper bound. Along the equal-cap branch the maximum is again
at an endpoint. Thus optimization within this enlarged family can be
reduced to a zero horn, an endpoint with equal caps, or a saturated larger
cap with only the smaller cap varying. This observation reduces the
dimension of a numerical or symbolic search; it is not an extremality
proof for arbitrary horn profiles.
