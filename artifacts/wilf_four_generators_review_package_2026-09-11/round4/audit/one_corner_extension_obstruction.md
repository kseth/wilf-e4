# One interior corner defeats the proposed 2/3 continuous bound

7 September 2026. Exact independent counterexample to an auxiliary geometric inequality, not a counterexample to Wilf's conjecture.

## Result

Even if every continuous lower ideal without a full-support excluded corner satisfies `mean(x+y+z)<=2M/3`, that assertion does **not** extend to lower ideals with one full-support excluded corner. Here `M` is the maximum total coordinate on the set, or its supremum for half-open sets.

The obstruction occurs both for an elementary polytope with one orthant removed and for a finite union of unit cells whose complement is a finite union of upper orthants. Thus it cannot be dismissed as a boundary or infinite-representation issue.

## 1. Elementary continuous family

Set

`U={x,y,z>=0: x+y<=1, x+z<=1, y+z<=1}`,

and, for `0<t<1/2`, remove the upper orthant:

`K_t=U \ [t,infinity)^3`.

Every excluded condition defining `U` has support at most two. The additional condition introduces one full-support excluded vertex, `(t,t,t)`.

Write `V(A)=vol(A)` and `I(A)=integral_A(x+y+z)`. The set `U` has

`V(U)=1/4`, `I(U)=7/32`, `M(U)=3/2`.

For a direct derivation, slice according to which coordinate is minimal and its value `r`. After translating the other two coordinates by `r`, the cross-section is the triangle of radius `1-2r`. There are three equal contributions, each with area `(1-2r)^2/2`. Its conditional mean total coordinate is

`3r+(2/3)(1-2r)=2/3+(5/3)r`.

Integration over `0<=r<=1/2` gives the displayed volume and first moment.

Let `lambda=1-2t`. The removed region is exactly

`R_t=t(1,1,1)+lambda U`,

so

`V(K_t)=(1-lambda^3)/4`,

`I(K_t)=[7-(7+10t)lambda^3]/32`,

`M(K_t)=1+t`.

The last equality is a supremum if the excluded orthant is closed: a retained point has a coordinate below `t`, while the other pair sums to at most one; points approaching `(t,1/2,1/2)` attain the bound in the limit. Closing the retained boundary changes no integral.

The normalized mean is therefore

`rho(t)=[7-(7+10t)(1-2t)^3]/[8(1+t)(1-(1-2t)^3)]`.

Subtracting `2/3` gives

`rho(t)-2/3 = t^2(3-16t+14t^2)/[3(1+t)(1-(1-2t)^3)]`.

It is positive whenever

`0<t<(8-sqrt(22))/14`.

In particular, at `t=1/10`,

`V(K)=61/500`, `I(K)=363/4000`, `M(K)=11/10`,

`mean(K)/M(K)=165/244 = 2/3+7/732`.

Equivalently its normalized four-dimensional slack is

`3-4 mean(K)/M(K)=18/61<1/3`.

The original set `U` itself satisfies the proposed no-interior-corner bound, since its mean is `7/8`, below `(2/3)M(U)=1`. Thus this is specifically a failure of the extension across a single removed orthant.

## 2. Finite-orthant counterexample

To remain within the exact finite cell class used for Apéry thickening, take

`T={(x,y,z) in N^3: x+y,x+z,y+z<=29; min(x,y,z)<=3}`,

and

`K=union_(v in T) [v_1,v_1+1) x [v_2,v_2+1) x [v_3,v_3+1)`.

The minimal excluded exponents consist of:

- the three pure bounds `30e_i`;
- the 29 mixed bounds on each coordinate plane, whose two positive coordinates sum to 30;
- the single full-support exponent `(4,4,4)`.

Every point excluded by a pair bound has a coordinate-plane excluded predecessor below it; every remaining excluded point dominates `(4,4,4)`. These are all the minimal exclusions.

Exact finite sums yield

`|T|=4246`, `sum_(v in T)|v|=92724`, `max_(v in T)|v|=32`.

Consequently

`V(K)=4246`, `I(K)=92724+(3/2)4246=99093`, `M(K)=35`,

and

`mean(K)/M(K)=99093/148610 = 2/3+59/445830>2/3`.

The complement of this `K` in the nonnegative orthant is exactly a finite union of closed upper orthants. It has exactly one full-support minimal vertex. The inequality therefore fails in the precise continuous cell setting as well.

These are geometric examples. They do not carry a verified residue-bijective Apéry labeling. In fact the finite example has 29 mixed corners on a coordinate plane, exceeding the earlier necessary arithmetic bound `P-2=10` for a full-support corner of coordinate sum `P=12`; it cannot be an Apéry staircase of the required kind.

## 3. The missing term in the deletion argument

Let `K=U\R`, set `M_U=sup_U(x+y+z)` and `M_K=sup_K(x+y+z)`, and use the target functional

`J(A;M)=3I(A)-2M V(A)`.

The exact identity is

`J(K;M_K)=J(U;M_U)+2(M_U-M_K)V(U)-[3I(R)-2M_K V(R)]`.

Knowing `J(U;M_U)<=0` leaves a positive height-loss contribution `2(M_U-M_K)V(U)`. Removing points decreases both the first moment and the admissible height, and the latter change cannot be discarded.

For the explicit `t=1/10` example the three terms are

`J(U;M_U)=-3/32`,

`2(M_U-M_K)V(U)=1/5`,

`3I(R)-2M_K V(R)=64/625`.

Their sum is

`J(K;M_K)=77/20000>0`.

Hence no proof based solely on the no-full-corner `2/3` bound and orthant deletion can establish the same constant for the one-corner class. Arithmetic restrictions could still rule out relevant geometric examples, but such restrictions would be additional input.

## Verification

`one_corner_extension_check.py` recomputes the rational family values, the exact finite cell counts, all minimal excluded corners of the finite example, and the cut-removal identity using the Python standard library. It is a certificate for these counterexamples only.
