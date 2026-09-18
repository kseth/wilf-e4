# Independent audit of the arbitrary rectangular-horn bridge

Audited source: `round4/bellman/arbitrary_horn_bridge.md`.

**Outcome:** the analytic reduction passes this independent conceptual audit. I also independently reran and inspected `round4/bellman/verify_horn_bridge_identities.py`; all six signed transition, jump-gain, cross-turn, and balanced-tail polynomial identities passed exact rational coefficient checks. No counterexample or missing feasibility condition was found in the argument below.

## Fixed-sum product minimization

After sorting the caps `B<=C`, every genuine rectangle at sum `s` satisfies `x<=y`, `x<=B`, `y<=C`. Before the selected terminal rectangle `(u,v)`, nestedness imposes `x>=u` and `y>=v`. The proposed minimizer

`x_*(s)=max(u,s-C)`, `y_*(s)=min(C,s-u)`

is feasible: `u<=B`, `s-C<=B`, `u<=s/2`, and `s-C<=s/2` follow respectively from terminal feasibility, `s<=B+C`, `s>=u+v>=2u`, and `s<=B+C<=2C`. Its second coordinate is at least `v` because `s>=u+v` and `C>=v`. Both coordinates are monotone in `s`. The function `x(s-x)` is nondecreasing on the sorted interval `x<=s/2`, so this is indeed the product minimum. Replacing each early rectangle independently therefore yields a nested feasible sequence, while all of its associated slab coefficients are nonpositive.

## The strict-slack initial state

The virtual state `(r_0-C,C)` can have its first coordinate greater than `B`, or even greater than `C`. This is harmless: it is only the integration baseline and the left endpoint of the initial jump. It is never an actual rectangle of the resulting horn. The first actual rectangle is on the feasible L path. The final merging step only enlarges the initial jump, retaining the necessary length at least `r_0-C-B`. Thus no interval with a cap violation is introduced.

## Cross-turn endpoint elimination

For a fixed starting state and a fixed L path, changing the cross-turn jump's endpoint only exchanges a jump with an adjacent portion of the continuous baseline. The total wholly continuous baseline from that starting state to zero does not change with `q`. Hence the endpoint conclusion obtained from the derivative of the cross-turn gain applies to the total objective, not merely to an isolated term.

For a noninitial cross-turn jump, its starting state is genuine and has `x<=B<=C`; thus `x<=r/2` and the balanced-jump endpoint argument is applicable on `[0,x]`. The fixed-`x` jump from `(x,C)` to `(x,x)` has nonpositive gain relative to its continuous continuation because `C+x<=1`. If zero dominates that continuation, every preceding slab is still from the original negative-coefficient part. Removing the entire horn is consequently valid.

For an initial cross-turn jump, using `L=B` is valid because `2B<=B+C<=r_0`. The alternative endpoint is the actual admissible initial slab to `(B,B)`; the proof does not pretend the virtual starting rectangle is feasible.

## Merging the remaining jumps

On a branch with fixed side `C`, the full continuous baseline is an integral over the whole branch and does not depend on where particular jumps are placed. Each jump's correction depends only on its length. It is therefore valid to move later jumps adjacent to the initial jump before merging them. A later positive gain either has `C>=2/3`, or has length strictly larger than `3(2/3-C)/2`; in both cases the displayed superadditivity difference against any nonnegative initial length is nonnegative. The combined length cannot exceed the total branch length. Increasing the first-jump length preserves the strict-slack cap restriction.

## Approximation

Finite step approximation from below can preserve both rectangular nesting and the height constraint by taking each step's side lengths from the right endpoint in the original outward coordinate. Such approximations converge almost everywhere for bounded monotone profiles, and dominated convergence applies to volume and first moment. The same effective-cap envelope bounds each approximant, so the bound passes to the limit.

## Consequence and limits

Together with the independently audited joint effective-cap theorem in `joint_effective_cap_theorem.md`, this bridge proves the continuous mean bound at most `2M/3` for a central box and up to three arbitrary nested rectangular horns under the common height bound `M`. The connection to finite Apéry staircases still requires accounting for the discrete first moments; configurations with an interior corner are also outside this continuous no-interior theorem.
