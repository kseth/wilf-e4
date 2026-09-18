# Bounded diagnostic for the continuous mean of genuine Apéry cells

7 September 2026. **No theorem is established by this diagnostic.**

For a minimally four-generated numerical semigroup
`S=<m,a,b,c>`, write `M=max Ap(S,m)`, `Sigma=sum Ap(S,m)`, and `s=a+b+c`.
The preferred Apéry cell thickening has normalized continuous mean

\[
\mu_{\rm cell}=\frac{\Sigma/m+s/2}{M+s}.
\]

Thus a counterexample to `mu_cell<=2/3` is exactly a tuple with

\[
6\Sigma-4mM-ms>0.
\]

Two bounded simulated-annealing runs targeted this objective over genuine
minimally four-generated numerical semigroups. Each used 324,000 proposals,
seed 74619243, and the fixed multiplicities
`20,25,29,31,47,73,113,155,181,293,467,751,1213,1979,3181`.
They used exact integer Apéry invariants for every proposal; floating-point
arithmetic only directed the heuristic search. This is **not** a complete
enumeration of a finite domain.

The second run required the necessary condition for an interior corner

\[
d(-a)+a=d(-b)+b=d(-c)+c,
\]

where `d(r)` is the minimum Apéry label in residue `r`. If an interior
minimal excluded point `p` exists, each predecessor `p-e_j` belongs to the
preferred ideal and has residue `-a_j`, proving the equality. Requiring
this condition focuses the search but does not assert that it is sufficient
for a preferred interior corner; the final fixture was reconstructed exactly.

Neither run found a positive failure numerator. The best final fixtures were:

| Run | Generators | Exact normalized cell mean | Failure numerator | Preferred interior corners |
|---|---|---:|---:|---|
| Unrestricted diagnostic | `<751,12234,23930,26072>` | `172061/269412` | −68,013,564 | none |
| Interior-focused diagnostic | `<1213,1214,2478,4952>` | `22661/35859` | −18,122,220 | `(1,6,9)` |

The interior fixture has `M=63074`, `Sigma=49733000`, conductor `61862`,
and Wilf number `24010`. Its cell mean is approximately `0.63195`, below
`2/3`. An independent Python heap computation reconstructed preferred
lexicographic factorizations of every Apéry element and all minimal excluded
exponents; the full exact data are preserved in the fixture JSON files.

Files:

* `targeted_probe.cpp`: bounded diagnostic source; run without arguments
  for the unrestricted objective, or with `--interior` for the necessary
  interior-condition filter.
* `targeted_probe_results.json`, `interior_probe_results.json`: recorded
  diagnostics. `valid_candidates` counts valid four-generator proposals
  before the additional interior filter.
* `verify_worst_fixture.py`: independent exact heap and lower-ideal checker.
* `targeted_probe_results_fixture_exact.json`,
  `interior_probe_results_fixture_exact.json`: all Apéry labels and preferred
  exponents, exact cell means and excluded corners for the final fixtures.

The unrestricted mean theorem for genuine Apéry ideals with an interior
corner remains unproved and unrefuted by this computation. A failed generic
non-Apéry geometric extension from prior work is a separate obstruction;
these computations neither remove it nor turn it into a semigroup
counterexample.
