# Independent audit of the (2,1,1) interior-corner cell bound

7 September 2026. **PASS.** The new arithmetic/compression argument and the
complete exact certificate prove that a preferred Apéry ideal with full
minimal excluded point `(2,1,1)` has at most 68 occupied cells in a partition
refining the earlier slab partition. The earlier slab theorem therefore
proves Wilf whenever `m>=270`. Coordinate permutations are harmless.

## Arithmetic restrictions

The full corner represents zero. For an xy minimal corner `(u,v,0)` represented
by `gamma e_z`, if `u>=2` then `(u-2,v-1,0)` is an included proper predecessor
with residue `(gamma+1)C`. If `gamma+1` were still on the included z axis,
these would be two distinct included representatives. Consequently
`gamma=h_z`. Distinct mixed corners have distinct residues, so at most one
xy corner has `u>=2`. At most one further xy corner can have `u=1`, since
different planar corners have different first coordinates. The same proof
applies to xz corners.

For a yz corner the analogous predecessor has residue `(gamma+2)A`, forcing
`gamma` into `{h_x-1,h_x}`. Thus there are at most two yz corners. Zero is
unavailable as a mixed-corner representative because the full corner already
uses it and intersects every mixed support. These arguments do not assume
any ordering among A, B, and C.

The forbidden planar corners below `(2,1,1)` are correctly excluded in both
programs. There is at most one full-support minimal excluded point by the
earlier residue-injectivity lemma, so no additional interior constraints
have been omitted from the template description.

## Rank compression and template coverage

Every positive minimal-exclusion coordinate gives a partition cut. In x,
the integer cut below 2 can only be 1. The full corner supplies 2, and each
of the xy and xz planes supplies at most one cut above 2. The pure bound is
strictly larger than every mixed x-coordinate. Therefore all possible orders
of occurring cuts embed in levels `0,...,5` with full coordinate fixed at 2
and pure bound sent to 5.

In each of y and z there is the full-corner cut 1, at most four further mixed
cuts, and the final pure bound. Levels `0,...,6` suffice. Shared cuts remain
shared; absent levels remain absent from the counted partition. In particular,
the code does not equate the 180 points of the encompassing normalized grid
with the number of occupied compressed cells.

A planar antichain has strictly increasing first coordinates and strictly
decreasing second coordinates. Enumerating its size as 0, 1, or 2 and imposing
the stated x restrictions gives precisely 45 choices on xy, 45 on xz, and
125 on yz. Every genuinely possible order pattern is included. Templates
need not admit residue labels; this enlargement is safe for an upper bound.

## Exact count and partition compatibility

I reviewed both programs. `cell_bound.py` counts the allowable z intervals at
each pair of occurring x,y cuts. Its z-cap always exists because the pure z
bound is among the corners. The index of that cap equals exactly the number
of allowed z intervals.

The independent `verify_cell_bound.py` constructs the full normalized grid,
deletes the excluded upper orthants, and retains only points corresponding to
occurring cuts. This gives one representative for every occupied cell.

I reran the latter complete checker. It enumerated **253,125 templates** and
returned **maximum 68 occupied cells**. The output is preserved as
`interior_211_cell_replay.json`. It agrees with both original exact outputs.

If z is a maximal included point, then z+e_i dominates a minimal excluded q.
Since q is not below z, necessarily `q_i=z_i+1`. Thus every slab-partition cut
used by the earlier theorem appears in the present corner partition. The
corner partition refines that partition, so its occupied-cell count is an
upper bound on the slab theorem's K. Substituting `K<=68` into `m>=4K-2`
gives the claimed 270 threshold.

## General (k,1,1) family and scope

The same proof allows at most k xy/xz/yz corners and at most one xy or xz
corner with x coordinate at least k. There are at most k x intervals below k,
at most three at or above k, and at most `2k+2` y and z intervals. Above k,
only the first y row or first z column can be occupied, giving at most
`4k+3` cells per slice. Thus the analytic bound

\[
K\le k(2k+2)^2+3(4k+3)
\]

and the stated consequent multiplicity cutoff are valid, although weaker
than the finite certificate at k=2.

This does not prove the entire (2,1,1) class. Combining the present result
with the separately completed multiplicity-20–29 theorem leaves the range
**30<=m<=269** for that class. It does not settle other full-corner shapes.
