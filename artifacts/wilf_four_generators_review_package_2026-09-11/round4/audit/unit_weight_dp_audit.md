# Audit of the unit-weight no-interior dynamic program

7 September 2026. Source: `round4/discrete_horns/unit_weight_dp.py`.

## Verified conclusion

Assuming the now separately audited continuous no-interior mean theorem, every finite nonempty no-interior lower ideal `T` in `N^3` with `m=|T|>=30` satisfies the unit-weight inequality

`D=3mR-4 sum_(x in T)|x| >= m`,

where `R=max_(x in T)|x|`.

This is slightly stronger than the originally proposed target `D>=m-1`. It is a unit-weight geometric theorem. Substitution of unequal semigroup generator weights is not justified by it.

## Completeness of the dynamic program

For a fixed degree ceiling `R`, its objective is the additive score

`sum_(x in T)(4|x|-3R+1)=m-D_R`.

The audited central-box/three-horn decomposition represents every no-interior lower ideal. A central integer box has top `(a,b,c)` with `a+b+c<=R`. Its score is exactly

`(a+1)(b+1)(c+1)[2(a+b+c)-3R+1]`.

For a horn slice at outward level `t`, a rectangle with top coordinates `(b,c)` contributes

`(b+1)(c+1)[4t+2b+2c-3R+1]`.

The future rectangle caps may only decrease. Thus the recurrence for `H[t][B][C]` takes the maximum of zero and every feasible rectangle's current score plus `H[t+1][b][c]`, over `b<=B,c<=C,t+b+c<=R`. The implementation realizes this maximum by prefix maxima in `B,C`. Its loop ordering ensures those prefix entries are already available. Choosing zero means stopping the horn entirely, rather than leaving a forbidden empty level followed by later nonempty levels.

The three horn regions are disjoint from each other and from the central box. Their optima can therefore be added independently at a fixed center. Permuting the center coordinates preserves the objective and admissible shapes for unit weights, so enumeration of sorted triples is sufficient.

The program may optimize over shapes whose actual degree is smaller than the ceiling `R`; this only enlarges the comparison class and is harmless for the asserted upper bound. Reconstruction checks verify that a returned optimum has the claimed score and is a lower ideal with no full-support excluded corner. Such checks alone would not prove completeness; the recurrence and decomposition above do so.

## Only four finite score computations are needed

The exact recomputation at degree ceilings 5, 6, 7, 8 gives respectively

`max(m-D_R) = -4,-17,-20,-23`.

These values are all negative. The independently checked central-box cardinality computation at degree 4 gives `|T|<=29`, so `m>=30` forces actual degree at least 5.

For actual degree `R>=9`, equal-weight thickening and the continuous theorem directly give

`[sum |x|]/m+3/2 <= (2/3)(R+3)`.

Therefore

`D/m >= R/3-2 >=1`.

Thus the general sawtooth cutoff 23, although valid, is unnecessary for this unit-weight result. Exact DP at degrees 5–8 plus the elementary degree-4 cardinality bound suffices.
