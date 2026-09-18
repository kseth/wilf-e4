# Exact cardinality bound at a fixed degree for the corner (2,1,1)

7 September 2026. Entirely analytic; no residue assumptions or finite dynamic program are needed.

## Theorem

Let T be a finite lower ideal in N^3 whose only full-support minimal excluded exponent is p=(2,1,1). Assume `max_T(x+y+z)<=R`, where R is an integer. Necessarily R>=3, by minimality of p. Then

**`|T|<=2R²-R+3`.**

The bound is attained for every integer R>=3. In particular, degree at most5 implies |T|<=48.

## Upper bound

Write `Δ_R={x∈N^3: |x|<=R}`. Inside Δ_R, all points of `p+N^3` are absent from T. Their number is `binom(R-1,3)`, interpreted as zero for R=3. Thus this first restriction leaves

`binom(R+3,3)-binom(R-1,3)=2R²+2`

possible points.

For each integer j=1,...,R-1, consider

`q_j=(1,j,R-j)`.

Its degree is R+1, so q_j is absent from T; it is not coordinatewise above p. At least one of its three coordinate-plane projections

```
(0,j,R-j),  (1,0,R-j),  (1,j,0)
```

must therefore be absent from T. Otherwise q_j would belong to the pairwise projection closure U of T. Since the sole full-support excluded corner is p, `T=U\(p+N^3)`, which would put q_j in T, a contradiction.

For distinct values of j, these triples of projection points are disjoint. Within a triple the support patterns also differ, so its three points are distinct. All are in Δ_R, and all lie outside p+N^3 because they have a zero coordinate. Consequently these R-1 triples force at least R-1 additional distinct missing points. Therefore

`|T|<=2R²+2-(R-1)=2R²-R+3`.

At R=5 this is the particularly simple count `56-4-4=48`: the p-orthant removes p and its three immediate successors, and the four disjoint projection triples remove four further points.

## Sharpness

Let

```
T_R={x,y,z>=0:
     x+y<=R, x+z<=R,
     yz=0 or y+z<=R-1}
     \ ((2,1,1)+N^3).
```

This is a finite lower ideal. Before the p-orthant is cut, every exclusion has support at most two. The three predecessors of p belong for R>=3, so p is its sole full-support minimal excluded exponent.

Every point of T_R has degree at most R: if y,z are both positive then x is zero or one and y+z<=R-1; if either y or z vanishes, one of the first two pair bounds controls the total degree.

Compared with Δ_R, the set deletes exactly the p-orthant points and the R-1 points `(0,j,R-j)`, j=1,...,R-1. It thus attains the claimed cardinality.

## Weighted consequence

For arbitrary positive weights with `a_min=1`, any T of weighted height M<6 lies in Δ5. Hence a genuine p211 ideal with m>=49 must have normalized height M>=6. This holds regardless of which coordinate carries the minimum weight, and it holds after every coordinate permutation of p.

This is the lower endpoint needed to combine the completed generic high-height interval certificate with the separately verified multiplicity30--48 arithmetic calculation. An alternative proof uses the stronger arithmetic plane restrictions and the exact low-height weighted certificates, which cover every m>=30.
