# Independent audit of the uniform-gap argument

Date: 10 September 2026.

## Verdict and scope

I independently read `uniform_gap_theorem.md`, the fresh evaluator
`verify_uniform_gap.js`, and its saved verification report. I also inspected
the referenced clique-tree argument and the phase estimate in
`round6/audit_foundations.md`. I found no concrete mathematical or
implementation gap in the argument establishing

\[
\kappa_c\ge5/42,
\qquad m\ge82{,}161\Longrightarrow W_4>0.
\]

This was an independent source and mathematical audit, plus a fresh check
of the saved output files and hashes. I did not rerun the dynamic program.
This audit does not prove unrestricted four-generator Wilf or verify every
other subclass claim made in earlier research notes.

## Coverage of the finite premise

For a full-support minimal excluded point, each immediate predecessor is
in the ideal. Thus its coordinate sum is at most the degree allowance plus
one. Coordinate permutation symmetry justifies sorted positive corner
triples. Removing that excluded generator leaves the pure-axis exclusions
intact, so the no-interior closure remains finite. Its axis caps are at
most the allowance because the positive corner removes no axis point.

Zero axis caps are present in the implementation. Hence sections missing
coordinate units, including lower-dimensional ideals, are covered. The
singleton is also included. The inactive corner `(1,1,R-1)` has degree
`R+1`; its upper orthant misses every ideal of degree at most `R`. This
includes all no-interior ideals. The empty ideal satisfies the desired
inequality separately.

I checked the central-box representation from the clique-tree argument.
Nested external neighborhoods exclude induced cycles. The connected
coordinate superlevel sets imply that every leaf is the strict global
maximum of some coordinate, giving at most three leaves. Paths from the
median of the three coordinate maximum nodes are increasing in their
outward coordinate and nonincreasing in the other two. The resulting
central box and three nested rectangular parts cover the closure, including
the degenerate cases with zero caps.

## Implementation and recorded results

The JavaScript evaluator retains a point precisely when it lies outside
the prescribed upper orthant. Its two-dimensional prefix sums calculate
clipped section scores, and prefix maxima calculate the maximum retained
degree. The recurrence combines each feasible section with a continuation
whose caps do not increase. Taking maxima with zero terminates a part;
taking maxima with the two smaller cap states covers every proper
subrectangle. The terminal allocation includes level `R+1`.

The three-dimensional central prefix calculation uses the correct
inclusion-exclusion signs for scores and ordinary maxima for degrees.
It tests retained points, so an excluded high corner cannot incorrectly
invalidate an otherwise feasible clipped box. The three parts and central
box are disjoint. Their array coordinate orderings agree with the
transverse-coordinate orderings used to construct them.

All source inputs, scores, indices, and prefix operations are integers.
There is ample space below the signed 32-bit bound: even the conservative
bound `8*(R+1)^3*(9*R+4)` is below `2^31` for these four degrees. Feasible
part scores are bounded by their point counts times `R+4`. JavaScript
intermediates are consequently far below the exact-integer limit `2^53`.
The separate algebraic assertions use `BigInt`.

I independently checked the verification report's source and input hashes,
equality of all three saved strips, the complete sorted-triple enumeration,
and all recorded signs. The 1,029 configurations partition as follows:

| R | Configurations | Maximum of 4m-D_R |
|---:|---:|---:|
| 18 | 204 | -50 |
| 19 | 237 | -53 |
| 20 | 274 | -56 |
| 21 | 314 | -59 |

These checks agree with the report's statement that the fresh evaluator
fully recomputed all configurations. My check verifies those saved records
and their linkage to the inspected source; it is not a fourth execution.

## Continuous transfer

Under `x=r+h*y`, inverse images of excluded orthants have the stated
coordinatewise ceiling vertices. A zero coordinate remains zero, and
deleting redundant vertices cannot create additional full-support
vertices. Thus each nonempty section meets the exact finite premise.
The allowance is in `{18,19,20,21}` for `h=1/21`, even when the actual
section degree is smaller.

The expansion of the defect and the integration in the translation
variable are correct. There is no Jacobian factor `h^3`, since for each
fixed lattice point the variable being integrated is `r`, with map
`r -> r+h*y` of Jacobian one. Empty sections contribute zero, and boundary
conventions affect only a null set.

Each coordinate fiber of the downset starts at zero. For its length
`H=q*h+t`, the remainder integral is `(q*h^2+t^2)/2 <= h*H/2`.
Fubini therefore gives a mean remainder at most `h/2` in every coordinate.
The resulting gap is exactly `4h-3h/2=5/42`.

## Phase estimate and strict cutoff

I independently checked the phase derivation: successive minimum-axis
fiber intervals concatenate; the sawtooth integral lower bound and the
fiber-length-weighted identity `v E(L)=2 mu_k+v` have the correct
coefficients. On summing the two estimates, the discarded slack coefficient
is four times the middle normalized weight minus `4(1+v)`, which is
nonpositive. This yields the displayed summed phase inequality.

The Apéry genus and thickening identities give `0<=kappa<v` under
`W_4<=0`. The substitution in the summed phase estimate is strictly
increasing in `kappa`, with derivative numerator `4+12v+12v^2`.
Combining with the continuous gap yields

\[
89v^2-390v+5<0.
\]

For `H=1/v`, the polynomial `5H^2-390H+89` is positive at `H=78`
and increasing thereafter. Hence `H<78`; the integer degree is at most
77, and the lattice count is `binomial(80,3)=82160`. The branch
`v>=1/3` gives at most 20 points. The use of `W_4<=0`, rather than only
`W_4<0`, correctly proves the strict positive conclusion above the cutoff.

No conclusion eliminating the remaining smaller-multiplicity region
follows from this audit.
