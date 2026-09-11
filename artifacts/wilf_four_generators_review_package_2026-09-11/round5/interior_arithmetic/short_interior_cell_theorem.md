# A finite reduction for the interior corner (2,1,1)

7 September 2026. This is a sufficient theorem and a finite reduction; it does not yet prove the entire (2,1,1) class. All coordinate permutations are included.

## Theorem

Let `S=<m,A,B,C>` be a minimally four-generated numerical semigroup. Suppose its preferred Apéry lower ideal has the full-support minimal excluded exponent `(2,1,1)`. Then

**`m>=270` implies `W_4(S)>=0`.**

A negative example in this class must therefore have `30<=m<=269`, using the separately completed multiplicity-29 theorem for the lower endpoint. The new upper endpoint depends on the previously proved slab theorem, and on the exact finite certificate below. No claim of publication priority is made.

## Arithmetic input

For a residue-bijective ideal `T`, a minimal excluded point has a representative in `T` with disjoint support. Minimal excluded points sharing a positive coordinate have distinct representatives. In particular, `(2,1,1)` represents zero:

`2A+B+C=0 mod m`.

Consider a mixed xy-corner `(u,v,0)` with representative `gamma e_z`. Let `h_z` be the last included exponent on the z axis. If `u>=2`, then `(u-2,v-1,0)` is included and has residue `(gamma+1)C`. Injectivity forces `gamma=h_z`. Distinct such corners have distinct representatives, so there is at most one with `u>=2`. There is at most one additional corner with `u=1`, because first coordinates of distinct corners of a planar lower ideal are distinct. Hence there are at most two xy-corners, and at most one has `u>=2`. Exactly the same assertion holds in the xz plane.

For a yz-corner `(0,v,w)`, subtracting `(0,1,1)` gives an included point with residue `(gamma+2)A`. Therefore its x-axis representative is one of `h_x-1,h_x`. There are at most two yz-corners.

Minimality of the full corner also forbids xy-corners with `u<=2,v<=1`, xz-corners with `u<=2,w<=1`, and the yz-corner `(0,1,1)`.

## Compression and completeness of the finite templates

Partition each axis at zero and at every positive coordinate occurring in a minimal excluded exponent. The whole ideal is a union of cells of this rectangular partition. A separate positive coordinate of a pure bound is included as the final cut.

In the x coordinate, cuts below 2 can only be 1. The full corner supplies 2. Above 2, the xy and xz planes supply at most one cut each, and the pure x bound supplies the final cut. Thus every possible order pattern embeds into the ordered levels `0,1,2,3,4,5`, preserving the numerical positions of 1 and 2. The final pure bound can always be sent to 5; unused levels do not count as partition cuts.

In y, the full corner supplies 1, the xy plane supplies at most two additional cuts, the yz plane supplies at most two additional cuts, and the pure bound is last. All possible order patterns therefore embed into `0,1,2,3,4,5,6`, with the pure bound sent to 6. The same holds in z.

These maps preserve all coordinate equalities and strict orders. Consequently they preserve the excluded-corner antichain, which rectangular cells are occupied, and the number of occupied cells. They are used to count cells only; no preservation of multiplicity, residue labeling, or Wilf number under compression is asserted.

It suffices to enumerate the following finite templates:

- Pure bounds `(5,0,0),(0,6,0),(0,0,6)` and full corner `(2,1,1)`.
- An xy planar antichain of size 0, 1, or 2 with coordinates in `[1,4] x [1,5]`, at most one first coordinate at least 2, and no point below `(2,1)`.
- The identical possibilities in the xz plane.
- A yz planar antichain of size 0, 1, or 2 with coordinates in `[1,5]^2`, excluding `(1,1)`.

There are 45 choices for each of the first two plane antichains and 125 for the third. Thus there are exactly

`45*45*125=253125`

templates. Each is itself a minimal-corner antichain; the restrictions above ensure that a plane corner does not dominate or lie below the full corner.

## Exact certificate

For each template, count included rectangular cells whose lower endpoint uses an occurring cut on each axis. The discovery implementation `cell_bound.py` evaluates each xy slice and sums the number of allowed z intervals. The separate implementation `verify_cell_bound.py` constructs all 180 lattice cells in the normalized box as an integer bitset, deletes upper orthants, then intersects with the bitset of occurring-cut representatives. The second implementation imports no code from the first.

Both exact integer programs return

**`K<=68`.**

The bound is attained in the geometric template class by the corners

```
(5,0,0), (0,6,0), (0,0,6), (2,1,1),
(1,5,0), (3,2,0), (1,0,5), (4,0,2),
(0,3,4), (0,4,3).
```

This geometric sharpness does not assert that the attaining template admits a genuine Apéry labeling.

The slab theorem uses a partition at coordinates `z_i+1` of maximal points `z`. Every such coordinate occurs among the minimal-exclusion cuts: since `z+e_i` is excluded, it dominates a minimal excluded `q`; because `q` cannot be below `z`, its ith coordinate must equal `z_i+1`. Thus the present corner partition refines that partition, and the slab theorem's occupied-cell count is also at most 68.

The previously proved slab theorem says `m>=4K-2` implies `W_4>=0`. Substituting `K<=68` yields `m>=270` and proves the theorem.

## An analytic bound for all (k,1,1) corners

The same argument yields a less sharp but entirely analytic family of sufficient cutoffs. For full corner `(k,1,1)`, each plane has at most k mixed corners, but each xy or xz plane has at most one corner with x coordinate at least k. The x-axis partition therefore has at most k intervals below k and at most three intervals at or above k. Each y/z axis has at most `2k+2` intervals. Below k, bound the occupied cross section by the full `(2k+2)^2` grid; at or above k the full corner leaves only the first y row or first z column, with at most `4k+3` cells. Hence

`K<=k(2k+2)^2+3(4k+3)=4k^3+8k^2+16k+9`.

Therefore

**full corner `(k,1,1)` and `m>=16k^3+32k^2+64k+34` imply Wilf.**

At k=2 this gives the weaker analytic cutoff 418; the exact 68-cell certificate improves it to 270. At k=1 the previously proved six-maxima theorem is stronger and already covers every multiplicity.

## What remains

Neither the compressed-cell count nor the tested examples exclude all genuine ideals with `(2,1,1)` and `30<=m<=269`. A six-maxima argument cannot do so: actual examples have seven or eight coordinatewise maximal points. The weaker proposal of at most six *final-window* points remains unproved by this note.

A diagnostic confined to the full-corner relation tested 10,629 actual `(2,1,1)` Apéry ideals; the largest observed final-window count was four. That observation is not a proof and is not used above.

## Dependencies and exact output

- Prior full-corner residue bound: `round2/arithmetic/general_interior_corner_bound.md`.
- Prior slab theorem, restated at `deliverables/wilf_fixed_dimension_finite_reduction_2026-09-05.md`, section 1.1 of the pure-critical-pair discussion.
- Complete discovery output: `cell_bound_complete.json`.
- Independent integer output: `independent_cell_bound.json`.
