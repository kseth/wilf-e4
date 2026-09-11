# Independent audit of the arbitrary-horn one-slab bridge

7 September 2026. Source: `round4/bellman/arbitrary_horn_bridge.md`.

## Outcome

The proposed bridge withstands an independent mathematical audit. I found no unresolved logical gap. It reduces every nested rectangular horn, including a horn with strict initial slack, to one initial constant slab followed by a continuous boundary profile of at least its objective.

This is a reduction theorem for the continuous no-interior-corner argument. It proves neither its separate joint-envelope inequality nor a discrete Wilf theorem. In particular it does not overcome the exact one-interior-corner obstruction recorded in `one_corner_extension_obstruction.md`.

## 1. Finite horns can be made endpoint-tight

For fixed nested rectangle states with areas `A_i`, the objective as a function of their ordered outward endpoints has a quadratic term `(3/2)(A_i-A_(i+1))t_i^2` at each endpoint, with `A_(n+1)=0`, and no mixed quadratic terms. It is convex because areas are nonincreasing. The feasible endpoint polytope is compact and has constraints `a<=t_1<=...<=t_n` and `t_i<=1-u_i-v_i`.

A convex function on this polytope has a maximizing vertex. At such a vertex, a block of equal endpoints is either at `a` or at an upper bound. The upper bounds are nondecreasing with the state index, so the first index in a nonzero-length block is the one that can bind. Removing zero-length slabs therefore leaves every surviving slab endpoint tight. This supplies the precise endpoint lemma used in the source; it does not assume that filling arbitrary jumps helps.

In reversed time `r=1-t`, a tight slab ending with caps `(x,y)` of sum `s` and starting at `r>=s` integrates to

`A(r)(r-s)xy`, where `A(r)=1-3r/2`.

The source's fixed-side jump gain `g_c(d)=c d^2(2d+3c-2)/4` and merge identity are consistent with direct integration. The gain can have either sign; the proof does not simply assume all jumps can be filled.

## 2. The positive part can be filled

For completeness, when a tight transition lies entirely at reversed times at most `2/3`, choose any monotone boundary interpolation between its two tight states. Its rectangle area is at least that of the smaller endpoint rectangle. Because `A(r)>=0` throughout the interval, its integral is at least

`xy integral_s^r A(z) dz >= xy(r-s)A(r)`.

Thus this interpolation dominates the slab. Repeating this fills the late portion. An initial mandatory slack slab is retained. The optimal capped-balanced boundary tail is then available as a further replacement. This also proves the easy `a>=1/3` case without presuming pointwise monotonicity of the original signed integrand in the caps.

## 3. The negative-part product minimization preserves feasibility

Sort the caps as `B<=C` and sort every rectangle's two side lengths. Pointwise minimum and maximum of two nonincreasing functions remain nonincreasing. Sorting also preserves the original cap bounds: the smaller sorted side is at most `B`, and the larger is at most `C`.

Let `(u,v)` be the first positive-area tight state whose sum is at most `2/3`. At each earlier state of sum `s`, nestedness implies that the smaller side is at least `u`, the larger side is at most `C`, and the smaller side is at most `s/2`. The product `x(s-x)` increases on that interval. Its minimum is attained at

`x_*(s)=max(u,s-C)`, `y_*(s)=min(C,s-u)`.

These states remain feasible: `s<=B+C` for every actual state, so `x_*<=B`; `s>=u+v` and `C>=v` give `y_*>=v`; `s<=2C` gives `x_*<=y_*`. Both sides are nondecreasing in `s`, so all modified states remain nested. Each altered slab has its starting reversed time greater than `2/3`, hence a nonpositive coefficient. Minimizing its endpoint product therefore weakly improves the objective.

The virtual initial state `(r_0-C,C)` may violate the first cap, but it is used only for a continuous baseline calculation. The actual first jump must cover the whole virtual excess. The later operations preserve that requirement.

## 4. Small-side and cross-turn jumps are correctly eliminated

On the branch with fixed smaller side `u`, any jump length satisfies `d<=C-u<=1-2u`. Therefore `2d+3u-2<=-u`, so its jump gain is nonpositive. Filling it is valid.

For the unique possible cross-turn jump, the derivative of its gain with respect to its ending drop `q` is

`G_q=(u/2)(p+q)(3p+3q+3u-2)`.

The derivative has at most a negative-to-positive sign change, so maximizing over its closed feasible interval reduces to the two endpoints. The continuous baseline from the jump's start through the entire remaining tail is independent of `q`, which is necessary for this derivative argument to apply to the whole continuation rather than only an isolated gain.

The balanced-ending endpoint is bounded using

`F_r'(z)=-6z(z-r/2)(z-r+2/3)`.

On `0<=z<=L<=r/2`, its only possible interior extremum is a minimum. For a noninitial jump starting at the actual state `(x,C)`, the choice `L=x` is feasible because `x<=C`. The endpoint `F_r(x)` is then a jump wholly along a fixed-small-side branch and is bounded by the corresponding continuous tail. If the zero endpoint wins, the entire earlier prefix was in the negative part, so zero dominates the whole horn.

For an initial cross-turn jump, the choice `L=B` is valid because `2B<=B+C<=r_0`. The resulting one-slab profile ends at `(B,B)`, which satisfies both original caps. This handles the case where the formal initial state's first coordinate exceeds `B` or even exceeds `C`.

## 5. The final jump merge remains valid with strict initial slack

Once the preceding replacements finish, all discontinuities lie on the fixed-`C` branch. Retain its first jump, including a possibly negative gain, because it covers mandatory initial slack. When there is no initial slack or jump, a zero-length first jump is permissible. Remove all later jumps with nonpositive gain by filling them.

For a remaining positive-gain jump of length `e`, either `C>=2/3`, or positivity implies `e>(3/2)(2/3-C)>2/3-C`. Therefore for any initial length `d>=0`,

`g_C(d+e)-g_C(d)-g_C(e)=(3C/2)de(d+e+C-2/3)>=0`.

This is the needed merge inequality even when the first jump itself has negative gain. The proof does not require a false unconditional two-jump domination statement.

Relocation is valid by reordering jump lengths and continuous lengths along the same fixed-`C` interval. Their total length and the wholly continuous baseline remain unchanged, while the individual jump gains depend only on their lengths. Increasing the initial jump preserves the cap constraint. The total merged length cannot exceed the full branch length. Thus the resulting profile has one admissible initial slab and a continuous continuation, which can be bounded by the optimal boundary potential `Q`.

The source incorporated the zero-length initial-jump and interval-reordering clarifications during this audit.

## 6. Passage to general monotone profiles

Approximation from below by finite step functions preserves cap bounds and the height constraint. The volume and first moment converge by dominated convergence on the fixed bounded domain. The integrand need not be monotone in the cap values; convergence, rather than objective monotonicity under this approximation, is what is used. The same fixed envelope bounds every approximant, so it bounds the limit.

## Verification scope

The six rational polynomial identities in `round4/bellman/verify_horn_bridge_identities.py` were rerun and passed. These exact algebra checks complement the feasibility and sign audit above; the checks alone would not establish the geometric reduction.
