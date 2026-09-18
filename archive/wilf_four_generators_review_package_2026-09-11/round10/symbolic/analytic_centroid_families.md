# Analytic centroid witnesses for clipped boxes and clipped prisms

11 September 2026. These are direct proofs for explicitly described infinite
families. They use no Apéry arithmetic, enumeration, degree bound, or numerical
optimization. They do not claim that every residual ideal belongs to these
families.

Write `s(T)=sum_{x in T} x`, `m=|T|`. A centroid witness is a point
`z in conv(T)` with `r=3mz-4s(T)>=0` coordinatewise and a lower bound on
`|r|_1`. Such a witness implies, for every `b_i>=1`,

    3m max_T b.x - 4 b.s(T) >= |r|_1.

## 1. Every corner-clipped rectangular box has a stronger witness

Let `n_i,p_i` be integers with `1<=p_i<n_i`, and set

    T = product_i {0,...,n_i-1} \ (p + N^3),
    q_i=n_i-p_i, Q=q_1 q_2 q_3,
    N=n_1 n_2 n_3, m=N-Q.

Let `v^(i)` be the upper corner `(n_1-1,n_2-1,n_3-1)` with its
`i`-th coordinate replaced by `p_i-1`. All three points belong to T. Take

    z=(v^(1)+v^(2)+v^(3))/3.

The coordinate moment is

    2s_i=N(n_i-1)-Q(n_i+p_i-1)
        =m(n_i-1)-Q p_i.

Also `3z_i=3(n_i-1)-q_i`. Consequently

    r_i=3mz_i-4s_i=m(p_i-1)+2Q p_i >=0,
    |r|_1=m(|p|_1-3)+2Q|p|_1.

If `|p|_1>=4`, the total is at least m. If `p=(1,1,1)`, then

    m=(q_1+1)(q_2+1)(q_3+1)-Q
      =q_1q_2+q_1q_3+q_2q_3+q_1+q_2+q_3+1
      <=6Q+1,

because each `q_i>=1`. Thus in every case `|r|_1>=m-1`.

**Conclusion.** All such clipped boxes satisfy the desired centroid inequality
with constant 1 in place of 29/10. For the residual corners of coordinate sum
at least five, the stronger bound `|r|_1>=m` holds.

## 2. An exact planar centroid fact

For every nonempty finite lower ideal P in N^2,

    (3/(2|P|)) sum_{x in P} x belongs to conv(P).

For each horizontal and vertical coordinate line meeting P, give its upper
endpoint a weight equal to the number of points of P on that line. The total
weight is `2|P|`. In a fixed coordinate, the lines parallel to that coordinate
contribute twice the corresponding first moment; the perpendicular lines
contribute that first moment once. Their weighted sum is therefore `3s(P)`.
This proves the statement by an explicit convex combination.

## 3. Clipped prisms with an arbitrary planar lower ideal

Let P be any finite planar lower ideal containing `(a,b)`, where `a,b>=1`.
Let `1<=h<n` be integers and set

    L=P \ ((a,b)+N^2),
    u=|P|, v=|L|, q=n-h,
    T=(P x {0,...,n-1}) \ ((a,b,h)+N^3),
    m=hu+qv.

Thus the first h horizontal layers are P and the next q layers are L. Put

    z_P=(3/(2u))s(P), z_L=(3/(2v))s(L).

By Section 2 the following three points belong to conv(T):

    (z_P,h-1), (z_L,n-1), (a,b-1,n-1).

Their convex combination with respective weights

    8hu/(9m), 8qv/(9m), 1/9

is a centroid witness with the exact residual

    r_1=ma/3, r_2=m(b-1)/3, r_3=A/3,
    A=hu(n+2h-3)+3qv(n-2h-1).

Indeed, the first two terms contribute exactly `4s(T)/3m` in each planar
coordinate. For the vertical coordinate use

    2s_3(T)=uh(h-1)+vq(n+h-1).

Substitution gives the displayed formula. Therefore it suffices to show

    A>=0, A>=m(4-a-b).

The following infinite subfamilies satisfy `r>=0` and `|r|_1>=m`:

1. `h>=3`, with arbitrary `a,b>=1` and `n>h`.
2. `h=2`, `n>=4`, and `a+b>=3`.
3. `h=2`, `n=3`, and either `a+b>=4`, or `a+b=3` and `7v<=6u`.
4. `h=1`, `n>=3`, and `a+b>=4`.

Here is a proof of the numerical assertions valid for all parameters, not a
finite parameter check. Since `0<v<=u`, the ratio A/m is a linear-fractional
function of `v/u` and lies between its endpoint values

    a_0=n+2h-3,
    f_h(n)=3n-8h-3+8h^2/n.

For `h>=3`, both are at least 2. For the second endpoint, this is equivalent to

    3n^2-(8h+5)n+8h^2>=0.

Its discriminant is `-32h^2+80h+25<=-23` for `h>=3`, so it is strictly
positive for every real n. Thus `A>=2m` and `a+b>=2` completes case 1.

For `h=2,n>=4`, `a_0>=5` and

    f_2(n)-1=(3n-8)(n-4)/n>=0.

Thus `A>=m`, proving case 2. At `h=2,n=3`,

    A=8u-6v>0,
    A-m=6u-7v,

which proves case 3. For `h=1,n>=3`, both coefficients in
`A=u(n-1)+3(n-1)v(n-3)` are nonnegative, proving case 4.

The construction is asymmetric only in its chosen vertical coordinate; every
coordinate permutation is allowed. No assertion that a general three-dimensional
lower ideal is a clipped prism is used.

## 4. Scope and useful next step

These formulas cover every corner-clipped box, and many clipped prisms whose
planar base has an arbitrary number of staircase steps. In particular, clipping
a prism at a coordinate at least three always admits a direct witness with total
surplus at least m. The planar base may have unbounded size and unequal axis
lengths. This is a stronger conceptual family than a fixed finite certificate
template.

General residual ideals have nonrectangular restrictions in all three coordinate
planes and need not be prisms. Extending the construction through unions of
prisms requires controlling the first moments of overlaps; a convex mixture of
individual witnesses cannot simply subtract those overlaps. That extension has
not been proved here.

## 5. The clipped-box witness survives in higher dimensions

For `d>=3`, define a d-dimensional clipped box by the same formulas, with
`N=product n_i`, `Q=product(n_i-p_i)`, and `m=N-Q`. Take z to be the average
of its d truncated upper vertices. The same first-moment calculation gives

    r_i=dmz_i-(d+1)s_i
       =((d-3)/2)m(n_i-1)+m(p_i-1)+((d+1)/2)Qp_i.

All coordinates are nonnegative. For `d>=4`, using `n_i-1>=p_i>=1`,

    sum_i r_i >= d(d-3)m/2 >= (d-1)m/2,

where the last inequality is `d^2-4d+1>=0`, valid for every integer `d>=4`.
Consequently every normalized positive weight vector satisfies

    dm max_T b.x -(d+1) b.s(T) >= (d-1)m/2.

If this T is a preferred Apéry ideal for a minimally `(d+1)`-generated numerical
semigroup, the general moment identity and `A=min a_i>=m+1` imply

    mW_(d+1) >= ((d-1)/2)m[(m+1)-(m-1)] >0.

This is an analytic sufficient structural family in every higher dimension.
It does not assert that arbitrary Apéry ideals are clipped boxes or that a
general higher-dimensional decomposition into such boxes is available. No
claim about novelty relative to existing literature is made.

The companion Python check verifies the displayed identities with exact rational
arithmetic on bounded examples and probes whether the 121 recorded failures of
the canonical line-top construction belong to these families. The proofs above,
not those examples, establish the infinite-family conclusions.
