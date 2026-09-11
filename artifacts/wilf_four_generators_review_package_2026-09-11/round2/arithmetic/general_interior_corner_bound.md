# Bounds from the location of the interior corner

Let `T` be a finite residue-bijective lower ideal in `N^3`, containing the three unit vectors, and let `p=(r,s,t)` be an interior minimal excluded point. Write `P=r+s+t` and `h_j=max{x_j:x∈T}`.

## Mixed corners per coordinate plane

Each coordinate plane has at most `P-2` mixed minimal excluded points.

For the xy plane, let `(u,v,0)` be such a corner. Its representative is `γ e3`, with `γ>0`; zero is excluded because this corner shares support with `p`, whose representative is zero.

If `u>=r` and `v>=s`, then `(u-r,v-s,0)∈T` and, using `rA+sB+tC=0 mod m`, its residue is `(γ+t)C`. If `γ+t<=h3`, this collides with the included point `(γ+t)e3`. Thus `γ>h3-t`. Such corners have distinct representatives, so there are at most `t` of them.

Among the other mixed corners, at most `r-1` have `u<r`, since distinct mixed corners in a planar downset have distinct positive first coordinates. At most `s-1` have `v<s`, by the same argument in the other coordinate. This gives at most `t+(r-1)+(s-1)=P-2` mixed corners. Coordinate permutation completes the proof.

The more precise statement retained by the proof is that all mixed corners lying beyond the two corresponding coordinates of `p` must represent one of the last `t` points of the opposite axis.

## A coarse bound on maximal points

Let `k_xy,k_xz,k_yz` denote the numbers of mixed corners in the coordinate planes. Then

`q <= r*(k_yz+1)+s*(k_xz+1)+t*(k_xy+1) <= P*(P-1)`.

Indeed every point of `T` has `x<r`, `y<s`, or `z<t`. For each fixed `i<r`, the slice `{(y,z):(i,y,z)∈T}` is the yz coordinate-plane section restricted by a rectangle: excluded corners supported on xy only impose an upper bound on `y`, those supported on xz only impose an upper bound on `z`, and the full interior corner is inactive at `i<r`. There is no second full interior corner, by residue injectivity. A rectangle restriction cannot increase the number of mixed corners in the yz section, so this slice has at most `k_yz+1` planar maximal points.

Every global maximal point with `x=i` is among those planar maxima. Sum over `0<=i<r` and apply the same argument to the other two coordinate slabs. This may count some points more than once, which is harmless for an upper bound. The preceding bound `k_ij<=P-2` yields `q<=P(P-1)`.

At `P=3` this recovers the sharp structural conclusion `q<=6` for the interior corner `(1,1,1)`. The general bound alone does not prove Wilf for `P>=4`.
