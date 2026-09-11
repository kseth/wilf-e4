# A sharp three-horn inequality for full-cap plateaus and boundary profiles

## Statement and precise scope

Let `a,b,c>0`, with `S=a+b+c<=1`. Consider a central box `[0,a]×[0,b]×[0,c]` and three disjoint horns extending beyond its respective faces. In the horn extending beyond the coordinate `a`, let the other two side lengths be `u(t),v(t)`, where `a<=t<=1`.

This theorem assumes the following **specific feasible class**:

1. On `a<=t<=1-b-c`, the rectangle uses the full central caps: `u(t)=b`, `v(t)=c`.
2. On `1-b-c<=t<=1`, the profiles are nonnegative and nonincreasing, bounded by `b,c`, and satisfy `u(t)+v(t)=1-t`.

Impose the analogous conditions on the other two horns. The second condition permits arbitrary monotone boundary profiles, including alternating coordinate changes; it is not restricted to a balanced shrink.

Then, writing

`J_a=∫_a^1 u(t)v(t)[3t+(3/2)(u(t)+v(t))-2]dt`,

and defining `J_b,J_c` by coordinate permutation, we have

`J_a+J_b+J_c <= abc[2-(3/2)(a+b+c)]`.

Consequently the uniform mean of `x+y+z` on the union of the central box and horns is at most `2/3`.

The proof below optimizes the entire boundary portion of each horn. **It does not establish that arbitrary horns can be replaced by this class.** Profiles with underfilled initial caps or multiple off-boundary plateaus remain outside the theorem.

## 1. Exact optimization of a boundary horn

Let its two caps be `B>=C>=0`, with `R=B+C<=1`. Reverse time by setting `r=1-t`, so `0<=r<=R`. The boundary condition is `u+v=r` and both profiles are nondecreasing in `r`.

We may sort the two side lengths pointwise. Their product and sum stay unchanged; the larger sorted length is still at most `B`, the smaller is at most `C`, and both remain nondecreasing. Let `d` be their nonnegative difference. Then `d` is 1-Lipschitz and

`L(r)=max(0,r-2C) <= d(r) <= U(r)=min(r,2B-r)`.

The boundary contribution is

`Q=∫_0^R (2-3r)(r²-d(r)²)/8 dr`.

The coefficient of `d²` changes sign at `r0=2/3`.

If `R<=r0`, the maximizing profile minimizes `d` everywhere, so `d=L`.

If `R>=r0`, fix `v=d(r0)`. For `r<r0`, the smallest feasible difference is

`d_-(r)=max(L(r),v+r-r0)`.

For `r>r0`, the largest feasible difference is

`d_+(r)=min(U(r),v+r-r0)`.

These bounds follow directly from the 1-Lipschitz condition. They are attained simultaneously: both displayed functions are 1-Lipschitz, remain between `L` and `U`, and meet at `v`. The first maximizes the integrand where the coefficient is nonnegative, and the second where it is nonpositive. Thus they maximize the whole integral among profiles with the given value at `r0`.

Putting `q=(r0-v)/2`, the resulting profiles have the following one-tent form:

- for `0<=r<=2q`, the two side lengths are both `r/2`;
- for `2q<=r<=B+q`, they are `q` and `r-q`;
- for `B+q<=r<=B+C`, they are `B` and `r-B`.

Here `0<=q<=C`. The feasible envelope parameters when `R>=r0` form the smaller interval

`max(0,r0-B)<=q<=min(C,r0/2)`.

The integral of this one-tent profile, denoted `I(q;B,C)`, satisfies the exact derivative identity

`∂I/∂q = (B-q)²(1-B-2q)/2`.

Therefore its unrestricted maximum on `[0,C]` occurs at

`q*=min(C,(1-B)/2)`.

When `R>=r0`, this value lies in the feasible envelope interval: `B>=1/3` gives `(1-B)/2<=1/3` and `(1-B)/2>=2/3-B`; the condition `B+C>=2/3` handles the endpoint `q*=C`. When `R<=r0`, `B+2C<=3R/2<=1`, so the formula gives `q*=C`, agreeing with the earlier direct maximization.

This proves the boundary optimum for every pair of caps.

## 2. Gain over the balanced capped profile

The usual capped-balanced boundary profile is the endpoint `q=C`. Improvement is possible exactly when `B+2C>1`.

Put `w=B+2C-1` and `y=B-C`. Integrating the displayed derivative gives

`I((1-B)/2;B,C)-I(C;B,C)`

`= w²y²/8+w³y/24+w⁴/192`.

If `w<=0`, the gain is zero. Thus the exact gain is

`g(w_+,y)`, where `g(z,y)=z²y²/8+z³y/24+z⁴/192`.

For example, `B=C=2/5` gives gain `1/120000`. This is the explicit obstruction to assuming a capped-balanced taper is always optimal.

## 3. The canonical three-horn identity

Relabel the central sides so that `a<=b<=c`. Write

`δ=1-a-b-c`, `x=b-a`, `y=c-b`, and `e2=ab+ac+bc`.

For a horn starting at `a`, with sorted full caps `B>=C` and `a+B+C<=1`, its capped-balanced value is

`H(a;B,C)`

`=BC[R-(3/2)R²+((3/2)R-1/2)B+((3/2)R-1)C-B²/2-(3/4)BC]+C³/6-C⁴/4`,

where `R=1-a`. This integrates the full-cap initial plateau followed by the capped-balanced boundary profile.

Direct expansion gives the exact identity

`abc[2-(3/2)S]-H(a;c,b)-H(b;c,a)-H(c;b,a)`

`= δ² e2/2 + δ x²(2x+3y)/6 + x²(2x²+4xy+3y²)/12`.  (1)

All coefficients on the right are nonnegative. The accompanying checker verifies this as a polynomial identity with exact rational coefficients.

## 4. Allowing every boundary profile

For the horn extending beyond `a`, the caps are `B=c,C=b`, and its possible gain over `H(a;c,b)` is

`g((c+2b-1)_+,c-b)=g((x-δ)_+,y)`.

The horn extending beyond `b` has caps `c,a`. It cannot improve, because

`c+2a<=a+b+c<=1`.

Likewise the horn extending beyond `c` has caps `b,a`, with `b+2a<=1`, so it cannot improve either.

Consequently the left-side deficit in the theorem is at least the right side of (1) minus `g((x-δ)_+,y)`. Since `0<=(x-δ)_+<=x` and `g` is increasing in its first nonnegative argument, this is at least

`δ² e2/2 + δ x²(2x+3y)/6`

`+x²y²/8+(7/24)x³y+(31/192)x⁴ >=0`.

This proves the theorem.

For positive central sides, equality holds precisely when `δ=0` and `x=0`, provided the boundary horns themselves attain their optima. Thus the equality family includes every central box `(a,a,1-2a)`, `0<a<=1/3`, with its optimizing horns.

## Verification and remaining step

`fullcap_boundary_verify.py` uses only Python's standard library and exact rational polynomial arithmetic. It verifies the canonical sum identity, the one-tent derivative, its gain formula, and the final nonnegative remainder identity. The resulting flags are saved in `fullcap_boundary_verification.json`.

The analytic control argument in Section 1 is part of the proof; numerical optimization is not used. Extending this theorem to arbitrary underfilled caps and arbitrary off-boundary monotone profiles still requires an additional argument.
