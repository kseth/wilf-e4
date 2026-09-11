# Independent source audit of the degree-six certificate verifier

Date: 10 September 2026.

## Verdict and scope

I independently reviewed `independent_verify.cpp` against the producer
`certify_all.cpp` and its `exact_dual.hpp`. I found no concrete flaw in
the alternative profile enumeration, explicit height reconstruction,
erosion and surface formulas, point-constraint membership, or exact dual
checking. I also compared every saved coverage counter and histogram,
checked equality of the recorded rational minimum margins, and checked
the assignment-file length. I did not rerun the large verification.

The exact dual conclusion is

\[
3mM-4\sum_i a_i S_i\ge m-\frac{29}{10}
\]

under the explicit constraints `a_i >= 1`, `0 <= M <= 7`, and
`a dot x <= M` for every point of the enumerated ideal. The cap `M <= 7`
is used by column 347 and must remain part of the composed theorem. This
source audit does not independently prove that the arithmetic filters or
the previously established excluded classes cover every genuine Apéry
ideal; those are separate mathematical dependencies.

## Independent shape coverage

For a descending seven-subset `t_0 > ... > t_6` of `{0,...,13}`, the
formula `h_i=t_i-6+i` gives precisely a nonincreasing seven-row partition
with entries between zero and seven. Its inverse is `t_i=h_i+6-i`.
The condition `h_i <= 7-i` is exactly the planar degree-six constraint.
Excluding `h_0=0` removes only the empty plane. Thus the subset enumeration
covers every nonempty planar lower ideal, without importing the producer's
recursive enumeration. The resulting 1,429 profiles also agree with the
expected Catalan count minus one.

The direct predecessor test in `eligible` recognizes exactly the mixed
minimal excluded plane points. No positive mixed corner can have a
coordinate seven: its predecessor in the other coordinate would already
be outside the profile. Thus the loops from one through six are complete.
The proper-face membership test, total mixed-corner bound, and upper-corner
count agree with the producer's tests.

The nine generated sorted corners are exactly the positive triples of
coordinate sum five, six, or seven. The group indices enforce agreement
of all shared axis lengths. Given compatible xy, xz, and yz profiles,
the height

`H[x][y] = min(xz_height[x], yz_height[y])`

within the xy profile reconstructs the intersection of the three pairwise
conditions. Capping it at `p_3` when `x>=p_1` and `y>=p_2` removes exactly
the corner upper orthant. Compatibility and positivity of the corner
ensure that the coordinate-plane projections are retained. The maximum
column degree `x+y+H[x][y]-1` correctly tests the full degree restriction.

The point count and all three coordinate sums are then direct column
sums. In particular, the z contribution is `H(H-1)/2`. No producer bitset
or bit-shift calculation is used in this reconstruction.

## Erosion, surfaces, and maxima

With zero padding at coordinate seven, the explicit erosion height is

`A[x][y] = max(0, min(H[x][y]-1, H[x+1][y], H[x][y+1]))`.

It counts exactly the points whose three positive unit translates remain
in the ideal. Its erosion difference-set cardinality is `|A|` plus its
three coordinate-zero face cardinalities: shifts remaining in the
nonnegative orthant are already in the lower ideal, while the three new
negative-coordinate faces are disjoint. The implemented expression
`sum(A + [A>0])`, with the x-zero and y-zero face sums added, is precisely
that count.

For each column, simultaneous x and y surface points number
`max(0,H-max(H_x,H_y))`. Simultaneous x and z surface points number
`[H>H_x]`, and the y/z analogue is `[H>H_y]`. A maximal point exists at
the column top exactly when both inequalities are strict. These formulas
agree with the producer's surface intersections and maxima, including
all coordinate boundaries. The axis-length checks and the three factors
of twice the opposite axis length are aligned correctly.

## Exact dual verification

Point column `(-x,-y,-z,1)` encodes `M-a dot x >= 0`. Columns 343–345
encode the three weight lower bounds, column 346 encodes `M>=0`, and
column 347 encodes `-M>=-7`. Every point column in an assigned basis is
checked against the current explicit height array; a constraint from an
absent point cannot be used.

The independent verifier derives its inverse numerators by Cramer's rule,
using fraction-free Bareiss determinants rather than the producer's
recursive cofactor calculation. Row swaps have their determinant signs
tracked; every Bareiss division is checked for exactness. It independently
checks the matrix inverse identity against the positive determinant.

For each actual ideal, it recomputes the objective vector
`(-4*S_x,-4*S_y,-4*S_z,3*m)`, requires every multiplier numerator to be
nonnegative, and checks the exact reconstruction of that vector from the
basis columns. Its bound is consequently a nonnegative linear combination
of valid inequalities. The final integer margin test is exactly the
target bound above, including the allowed zero margin.

Arithmetic fits safely in the chosen types. Matrix entries have magnitude
at most six, determinants at most `4!*6^4`, and cofactors at most `3!*6^3`.
There are at most 84 points of degree at most six, bounding every objective
coordinate in magnitude by 2016. The resulting multiplier, inverse-check,
and margin calculations are far below signed 64-bit limits. Bareiss
products and rational-margin comparisons additionally use `__int128`.
The independent verifier uses no floating-point calculations.

## Saved-result comparison

All nine rows match the producer for the corner, every coverage-stage
counter, the maximum point count, the unit-weight diagnostic, and the
entire cardinality histogram. All nine recorded rational minimum margins
agree by cross multiplication. Their surviving counts sum to 3,361,434.
There are 5,733 registered bases and exactly 13,445,736 assignment bytes,
four bytes per surviving ideal. The verifier also checks premature EOF,
missing basis references, and extra trailing assignment bytes.

The independently checked assignment-file SHA-256 is

`5ef90115f09c42b7747436216f1897ddb2ee9e9b46e97d24e5c58de11f9cb1de`.

The reviewed independent-verifier source SHA-256 is

`d29a113f38dbf478cdf2ec83ddde4bbe5147ba776ccd5b68302abb95fc137a88`.

These checks support the reported complete replay for the stated
enumeration and constraints. They do not by themselves eliminate any
class outside that stated scope.
