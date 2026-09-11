# Exact one-corner dynamic program and necessary geometric obstructions

The new recurrence below is exact for each fixed positive integer weight
triple, height allowance, and full-support excluded corner. The completed
bounded run does not prove a universal weighted inequality.

## Representation and finite range

If T has at most one full-support minimal excluded point p>0, remove that
one generator from the excluded monomial ideal and call the resulting
lower ideal U. Then

    T = U \ (p+N^3),

and U has no interior excluded corner. The pure-axis exclusions remain, so
U is finite. Its coordinate-axis points survive the cut, and consequently
its axis caps are at most floor(M/a_i), even though some other points in U
may have weight greater than M. The previous clique-tree theorem decomposes
U into a central box and three rectangular-fiber horns.

For unit weights, minimality of an actual corner p implies every p−e_i
belongs to T. Thus |p|_1<=R+1. Coordinate symmetry allows enumerating sorted
positive p. Ideals having no full-support corner are also covered: choose a
positive p of degree R+1, which lies outside any ideal of degree at most R,
and take U=T. (The runs here have R>=3.)

## Exact clipping formulas

At outward coordinate t on axis i, a U-horn slice is [0,u]×[0,v]. Let the
other indices be j,k and weights beta=a_j, gamma=a_k. The full slice has

    N=(u+1)(v+1),
    sum w = N [a_i t + (beta u + gamma v)/2].

If t>=p_i, u>=p_j, v>=p_k, delete its upper rectangle
[p_j,u]×[p_k,v]. Its cardinality is

    N_removed=(u−p_j+1)(v−p_k+1),

and its weight sum is

    N_removed [a_i t + beta(p_j+u)/2 + gamma(p_k+v)/2].

The maximum weight of the retained slice is then

    a_i t + max(beta(p_j−1)+gamma v,
                beta u+gamma(p_k−1)).

When the cut is inactive, use the full-rectangle maximum. These formulas
are integer-valued; the implementation checks the divisibility by two.

The clipped central box has the analogous full-box moments minus its
upper subbox. If the cut is active, its retained maximum is the maximum
of the three faces obtained by c_i -> p_i−1.

Use these retained cardinalities and moments in the previous nested-horn
recurrence, and declare a slice feasible exactly when its retained maximum
is at most M. Its score is

    4 sum w + N(penalty−3M).

The central box must satisfy its own retained-height bound. Do not impose
sum_i a_i c_i<=M on the uncut central point: that point may have been
deleted. `one_corner_dp.py` implements this distinction explicitly.

## Exact unit-weight results, R=3,...,8

The objective is m−D=4Σ+(1−3R)m. Every positive maximizer has actual height R.
The maximum at R=8 is attained by the singleton with actual height zero;
using a larger allowance penalizes it, which is harmless for an upper bound.

| Height allowance R | Maximum m−D | Cardinality of a maximizing ideal | Corner of that ideal |
|---|---:|---:|---|
| 3 | 16 | 19 | (1,1,1) |
| 4 | 19 | 31 | (1,1,1) |
| 5 | 16 | 46 | (1,1,1) |
| 6 | 4 | 64 | (1,1,1) |
| 7 | −20 | 85 | (1,1,1) |
| 8 | −23 | 1 | none |

This table by itself records score maxima, not maximum cardinalities among
all failing ideals. The latter distinction matters. Nevertheless, the
largest failure cardinality over this entire bounded range is **exactly 64**:

* For R<=5, even the full degree-five simplex has only 56 points.
* At R=6, every p other than (1,1,1) has maximum score at most −1. For
  p=(1,1,1), all retained points lie on the three coordinate planes; their
  full degree-six union has 64 points.
* At R=7,8, the maximum score is negative.
* The degree-six union of the three coordinate-plane triangles attains
  m=64 and m−D=4>1, so the bound 64 is attained.

This bounded run alone does not address R>=9. The separate
`unit_one_corner_theorem.md` subsequently combines larger exact strips
with decimation to prove the sharp unbounded threshold m>=65.

## Two exact obstructions to the unrestricted geometric target

Let F_R={x in N^3: |x|_1<=R, min_i x_i=0}. Then

    m=(3R²+3R+2)/2,
    Σ=R(R+1)(2R+1)/2,
    D=R(R−1)(R−2)/2.

For R=6, m=64, Σ=273, D=60, so D<m−1. Its full-support corner is (1,1,1).
This refutes the attempted extension of the no-interior geometric theorem
to every at-most-one-interior ideal with m>=30. It is not a Wilf
counterexample; the previous arithmetic face-shell theorem covers genuine
semigroups in this family.

There is also a p=(1,1,2) obstruction:

    T={x+y<=4 or xy=0; x+z<=5; y+z<=5} \ ((1,1,2)+N^3).

Its axis caps are implicit in these inequalities. Direct enumeration gives
m=48, M=5, Σ=171, D=36, hence m−D=12. It has four mixed xy-plane excluded
corners, (1,4,0),(2,3,0),(3,2,0),(4,1,0). This violates the necessary
at-most-two mixed-corner condition derived for a genuine p=(1,1,2) Apéry
ideal. Thus residue arithmetic excludes this obstruction. Its exact points
and moments are in `p112_counterexample.json`.

## Cardinality bound at degree six

Running the same recurrence with objective equal to cardinality (moment
multiplier and height multiplier both zero, penalty one) gives exact maximum
cardinalities:

| Degree allowance | Maximum cardinality with at most one full-support corner |
|---|---:|
| 3 | 19 |
| 4 | 31 |
| 5 | 48 |
| 6 | 71 |
| 7 | 101 |

Consequently m>=72 forces normalized height M/a_min>=7. This is a useful
lower endpoint for a prospective one-corner interval certificate. A compact
upper endpoint and a weighted inequality on that domain are not proved here.

## Independent implementation audit

`audit_one_corner_dp.py` enumerates lower ideals by their height arrays h(i,j),
without using the central-box or horn representation. At i,j>0, the only
extra positive height allowed below min(h(i−1,j),h(i,j−1)) is p_3, and only
at (i,j)=(p_1,p_2). This independently enforces at most the permitted full
corner. Five fixed-parameter cases, including unequal weights, enumerate
106,717 ideals in total and agree exactly with the clipped-horn optima and
maximizing cardinalities. This finite check audits implementation; the
preceding representation and recurrence arguments establish its scope.

The score witnesses are independently checked for cardinality, first moment,
actual height, downward closure, and the list of full-support excluded
corners. All computations use standard-library integer arithmetic.

## A compact way to enforce arithmetic plane-corner budgets

For the no-interior closure U with a central box c and horns, project onto
a coordinate plane (i,j). Let k_ij be the number of distinct j-cap values
in horn i, with k_ij=0 for an empty horn. Each distinct cap plateau yields
exactly one maximal point of that plane projection. Horns i and j yield
incomparable maximal points, because each lies strictly outside the central
box in its own outward coordinate. The central point (c_i,c_j) survives
as a maximal point exactly when neither horn is nonempty with its first
transverse cap equal to the corresponding central cap. Denote this indicator
by epsilon_ij. Hence the number of plane maximal points is

    k_ij+k_ji+epsilon_ij.

A finite two-dimensional lower ideal has one fewer mixed minimal excluded
point than maximal points (sort maximal points by increasing first
coordinate). Therefore its mixed-corner count is exactly

    k_ij+k_ji+epsilon_ij−1.

In particular, a budget of at most two mixed corners restricts this sum to
at most three. It can be tracked by small cap-change counters on each horn.
For the p=(2,1,1) extra restriction that at most one mixed corner has x>=2,
the only additional case to check is a plane having three maximal points:
then the first, largest-other-coordinate maximal point must have x=0.
This is a terminal-cap-zero flag in the corresponding other-axis horn
(or the central x coordinate if that horn is empty).

This gives a correct finite-state design for an arithmetic-aware DP. The
extra-state implementation is not supplied or claimed complete here.
