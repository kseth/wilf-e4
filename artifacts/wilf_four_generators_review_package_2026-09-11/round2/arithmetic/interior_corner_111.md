# The interior-corner (1,1,1) class satisfies Wilf

## Scope and dependency

The structural theorem below is entirely analytic. It proves that a residue-bijective lower ideal in three variables whose minimal excluded set contains `(1,1,1)` has at most six coordinatewise maximal points.

For a genuine four-generated numerical semigroup, this implies Wilf by Theorem A of `prior/wilf_edim4_six_point_and_column_theorems_2026-09-05.md`: at most six Apéry elements in `[c,c+m)` suffice. That earlier theorem has a finite computer-assisted component. The deduction here does not reverify or eliminate that computational dependency. Thus the structural bound is analytic, while the stated Wilf corollary uses the previously certified six-point theorem.

No publication priority claim is made.

## Structural theorem

Let `T⊂N^3` be a finite nonempty lower ideal of size `m`, containing the three unit vectors. Suppose

`x ↦ A x1+B x2+C x3 (mod m)`

is bijective on `T`, and suppose `(1,1,1)` is a coordinatewise minimal excluded point. Then:

1. Each coordinate plane contains at most one minimal excluded point supported on both of its coordinates.
2. `T` has at most six coordinatewise maximal points.

### Boundary facts

If `p` is minimal excluded and `q∈T` represents its residue, their supports are disjoint. Otherwise subtracting a shared coordinate unit vector gives two distinct points of `T` with equal residues. Likewise, two distinct minimal excluded points sharing a positive coordinate cannot have the same residue: subtract that shared coordinate and use injectivity on `T`.

The interior point `(1,1,1)` therefore has representative zero, so

`A+B+C=0 (mod m)`.

### At most one mixed corner in a plane

Consider any mixed minimal excluded point `p=(u,v,0)`, where `u,v>=1`. By disjoint support its representative is `γ e3`. It cannot be zero, because `p` and `(1,1,1)` share positive coordinates and are distinct minimal excluded points. Thus `γ>=1`.

Let `h3=max{k : k e3∈T}`. Then `γ<=h3`. The point

`r=p-e1-e2=(u-1,v-1,0)`

belongs to `T`: it is coordinatewise below the included predecessor `p-e1`. Its residue is

`w(r)=w(p)-A-B=γC+C=(γ+1)C (mod m)`.

If `γ<h3`, then `(γ+1)e3∈T` as well. These are distinct points: the first has third coordinate zero, while the second has positive third coordinate. This gives a forbidden residue collision. Therefore `γ=h3`.

Every mixed corner of the first two coordinates must consequently have the same residue, namely `h3 C`. But any two such corners share both coordinates in their supports, so the boundary fact says their residues must be distinct. There is at most one. Permuting coordinates proves the first assertion.

The calculation would still distinguish the two points if `u=v=1`, since then `r=0` while `(γ+1)e3≠0`. Under the present minimal-interior-corner hypothesis that mixed corner cannot actually occur: `(1,1,0)` is a predecessor of `(1,1,1)` and lies in `T`.

### At most six maxima

Because `(1,1,1)` is excluded, every point of `T` has at least one zero coordinate. Thus `T` is the union of its three coordinate-plane sections.

Each section is a finite planar lower ideal with its two pure axis bounds and at most one mixed minimal excluded point. It is therefore a rectangle with at most one upper-right quadrant removed, and has at most two planar maximal points.

Every coordinatewise maximal point of `T` is maximal in each coordinate-plane section containing it. In particular it is in the union of the three sets of planar maxima. That union has at most `2+2+2=6` elements. This proves the second assertion.

## Wilf corollary

Let `S=<m,a1,a2,a3>` be minimally four-generated, and choose a preferred Apéry staircase `T` modulo `m`. If `(1,1,1)` is a minimal excluded point of `T`, the theorem gives at most six coordinatewise maxima.

Set `M=max_{x∈T} a·x=c+m-1`. Every point in the final Apéry window

`Z={x∈T : M-a·x<m}`

is coordinatewise maximal: a coordinate successor would add a generator larger than `m`, thereby exceeding `M`. Consequently `|Z|<=6`. The previously certified complete six-point theorem now gives `4|S∩[0,c)|>=c`.

## Diagnostic, not a proof dependency

A seeded 20,000-proposal experiment with generator residues summing to zero produced 16,478 minimally four-generated semigroups, of which 16,346 had the minimal corner `(1,1,1)`. Their maximal-point counts were:

| Maximal points | Observed semigroups |
|---:|---:|
| 3 | 582 |
| 4 | 3,972 |
| 5 | 3,054 |
| 6 | 8,738 |

The structural proof above is independent of this sample.
