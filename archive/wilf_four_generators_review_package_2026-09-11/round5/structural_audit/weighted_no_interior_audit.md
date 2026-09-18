# Independent audit of the completed weighted no-interior theorem

7 September 2026. This audit concerns the exact mathematical and programmatic
chain in `../weight_arrangement/weighted_no_interior_theorem.md`. It is an
independent in-session audit, not external peer review.

## Verdict

**PASS.** For a finite no-interior lower ideal containing the three coordinate
unit vectors, cardinality at least 30, and arbitrary positive coordinate
weights, the new argument proves

\[
3mM-4\sum_T a\cdot x\ge a_{\min}(m-1).
\]

The interval computation certifies a whole real parameter domain. It is not
a sampled grid or an inference about the cardinality of one maximizing ideal.
I found no gap in the analytic reduction, the class of ideals optimized, the
interval upper bounds, the treatment of empty arms, or the domain coverage.

## Analytic reduction

Normalize and permute weights to `(1,b,c)`, with `1<=b<=c`. A putative failure
`D<m-1` gives `kappa=D/(mM)<1/M=v`. The previously proved phase inequality and
continuous no-interior theorem therefore imply

\[
M<12+\sqrt{137}<24.
\]

In the case `v>=1/3` this follows immediately from `M<=3`. Otherwise
`1-3*kappa>0`; the rational upper bound for the weight sum is increasing in
`kappa`, and substituting `kappa<v` gives the displayed strict bound. Thus the
argument does not presume nonnegative Wilf or residue injectivity.

The coordinate-unit hypothesis ensures `c<=M`. The degree-four no-interior
cardinality maximum is 29, checked again independently by enumerating every
central triple and every possible rectangle at every outward level. Therefore
`m>=30` forces `M>=5`. Together these facts put every counterexample in
`1<=b<=c<=M`, `5<=M<=24`.

## Exact interval domination

For a closed box with scaled lower endpoint `(B0,C0,H0)` and upper endpoint
`(B1,C1,H1)`, use `(q,B0,C0)` to enlarge the set of permitted integer points
and `(q,B1,C1)` together with `H0` to increase every point's score. Coordinates
are nonnegative, so both inequalities have the correct direction. Optimizing
this enlarged problem is a valid simultaneous upper bound for every real
parameter in the box, including irrational parameters and all box boundaries.

The central-box decomposition is exhaustive by the earlier clique-tree
theorem. At each horn level its entire cross section is an anchored rectangle;
future sections are nested. The recurrence either ends the horn or chooses
one feasible rectangle and continues with those same transverse caps. It
covers every permitted sequence. The central box and its three outward horns
are disjoint; their moment formulas and array coordinate permutations are
correct. Conversely, even if the dynamic program were to include additional
objects, that would only enlarge its upper bound.

The generator's two-dimensional prefix maxima evaluate the displayed explicit
rectangle maximum exactly. There is no restriction to equal weights, one
particular central point, positive-length arms, or fixed cardinality.

The analytic leaf rule is also valid: unit-cube thickening gives

\[
D_M/m\ge [M-2(1+b+c)]/3.
\]

Thus `M>=2(1+b+c)+3` implies `m-D_M<=0`, stronger than the target 1. The
implemented box test uses the smallest height and largest weight sum and is
therefore sufficient throughout its box.

## Independent reproduction

I wrote `independent_interval_dp.py` without importing the generating program
or its verifier. Its horn computation explicitly enumerates every pair of
rectangle side lengths and recursively continues each candidate. It does not
use prefix maxima. It replayed **all 24,912 DP leaves**, obtaining exactly the
recorded integer bound at each one, and separately checked **all 531 analytic
leaves**. This was a complete replay, not a sample. The output is
`independent_interval_dp_results.json`.

I also wrote `independent_interval_coverage.py`. It independently propagates
the ordering inequalities to a fixed point, checks the exact closed child
boxes at every split, verifies that no reachable node is reused, and checks
that every recorded node is reached. All **50,885 nodes** passed: 25,442 splits
and 25,443 accepted leaves, with no unresolved node. The output is
`independent_interval_coverage_results.json`.

The scale 4096 specifies interval endpoints; it does not discretize the
parameters being certified. Closed children overlap at their split and cover
their parent's entire retained ordered region. Tightening removes only points
outside `b<=c<=M`.

The generating agent's separately written flat-array verifier also reports a
complete pass. That extra check is consistent with, but not a substitute for,
the independent recurrence and coverage checks above.

## Wilf consequence and its limits

For a genuine minimally four-generated semigroup, `a_min>=m+1` and
`m W4=D-m(m-1)`. Therefore for `m>=30` and a no-interior preferred Apéry ideal,

\[
mW_4\ge(a_{\min}-m)(m-1)>0.
\]

Hence `W4>=1`. This completes the previously missing unequal-weight argument
for that cardinality range. Smaller cardinalities use separate results. The
theorem does not cover a preferred Apéry ideal with a full-support minimal
excluded point.

## Reproduction

From the archived project root:

```
python3 round5/structural_audit/independent_interval_dp.py
python3 round5/structural_audit/independent_interval_coverage.py
```

Both programs use only Python's standard library. The first consumes the
complete tree certificate in `round5/weight_arrangement/` and takes about a
minute in this environment. Its sampled option was an initial diagnostic;
the default invocation and the final recorded result check every leaf.
