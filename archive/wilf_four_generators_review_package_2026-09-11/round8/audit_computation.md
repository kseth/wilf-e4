# Fresh audit of the four-generator high-height computation

11 September 2026. This audit reviews the source and challenges the optimization model; it does not infer correctness from a saved `PASS` label. Its scope is the high-height interval certificate. The analytic compactness estimates and general structural theorem are explicit external dependencies.

## Current disposition

The source review has found no defect in interval clipping, integer arithmetic, corner enumeration, horn optimization, complete-tree coverage, or the independent replay protocol. A fresh no-cache replay from newly copied C++ sources **passed all 47,088 DP leaves and all 35,852,138 Cartesian corner cases**. The complete tree has zero pending or unresolved nodes. No failure or required repair was found in this component.

## Sources inspected

- `round7/geometric_residual/interval_all_corners_parallel.cpp`
- `round7/geometric_residual/certify_residual_parallel.py`
- `round7/geometric_residual/independent_specialized_piece_worker.cpp`
- `round7/geometric_residual/verify_residual_certificate.py`

The canonical certificate has SHA-256 `173fe6ec196b3d2adabad313749482542ad3492b5f6b4e398e76bbe6e52e405c`. I independently recomputed this hash. The frozen prior replay cache also has its advertised hash, `1cf1a33b466fbd0a11406da0dc2b2c80ca46fe9f7f18c1dc7d35abb32ff696e7`, with 47,088 distinct node IDs and 35,852,138 Cartesian corner cases. These provenance checks alone do not certify the numerical bounds; the new run deliberately uses no cache.

## Parameter enclosure and complete corner domain

The root encloses all normalized ordered parameters satisfying `1 <= b <= c <= H`, `7 <= H < 78`. Each clipping step follows only the asserted necessary failure bounds `S < 9 + 28/(H-3)` and `5H < 42 + 37S`, together with ordering. Upper grid endpoints are rounded upward. In particular `(Sbound-q)/2` uses ceiling, not floor. Twenty iterations need not reach a fixed point: stopping early retains extra possible points and is harmless. Denominators stay positive because every reachable lower height is at least `7q`.

The final verifier independently reconstructs the clipping with rational numbers, traverses every node exactly once, rejects unreachable or duplicated nodes, checks the exact root, and checks that each pair of closed children covers the clipped parent including the splitting face. Empty boxes must actually be empty. Accepted leaves require completion and a bound at most `29q/10`.

For an actual minimal full-support excluded point `p`, `p-e_1` belongs to the ideal, where the first weight is normalized to one. Thus `lower_weight.p <= upper_height + q`; all weights are at least `q`, giving `sum(p) <= floor(upper_height/q)+1`. The primary positive-composition loop includes every such point with sum at least five. Its two symmetry restrictions require equality of both objective and feasibility coefficients in the exchanged directions. The independent Cartesian loop applies no symmetry restriction and covers the same full corner domain.

## Objective, feasibility, and dynamic recurrence

The integer point objective is `4*upper_weight.x + q - 3*lower_height`. Replacing the weights by upper endpoints increases the objective; replacing the feasibility weights by lower endpoints and the permitted height by its upper endpoint enlarges the feasible family. Thus the computed maximum is an upper bound for the actual scaled quantity `q(m-D)`.

For a fixed corner and horn direction, the retained section is a rectangle with its corner orthant removed when the outward coordinate reaches the excluded coordinate. The primary worker uses full-rectangle subtraction; the independent worker partitions the section into two disjoint rectangles. Their formulas are the direct arithmetic-series count, twice the weighted moment, and largest feasibility weight of those retained points.

For each outward position `t`, the recurrence maximizes over stopping, shrinking either transverse side, or keeping a feasible current section and continuing with a section no larger in either transverse direction. The recurrence therefore includes every nested rectangular horn. In the specialized worker, the running row maximum and preceding-row maximum implement exactly the maximum over every smaller transverse rectangle. The terminal horn value is zero.

The three horns begin immediately beyond the corresponding sides of the center. Their retained points and the center are disjoint. The center's clipped set is partitioned into the three disjoint boxes selected by the first coordinate below `p`. A box is feasible precisely when every retained point is feasible; the code computes this by the maxima of its nonempty component boxes. All lower coefficients are positive, so each component maximum lies at its upper corner.

Completeness for *all* ideals still uses the mathematical statement that an ideal without a full-support minimal excluded point admits a center and three nested rectangular horns. The separate workers share this optimization model. To challenge that shared assumption computationally, I also built the independent cylinder enumeration described below.

All coordinates of the ideal before clipping are bounded by the height-derived axis limits: its pure-axis points survive a full-support corner cut. Thus the array limits do not truncate any needed center or horn. In the exact certificate domain each axis has at most 79 positions and flattened allocation indices are below 500,000. Counts, moments and scores use signed 64-bit integers. Bounding every coordinate and every weight by their largest domain values gives magnitudes below `10^15`, including the threshold multiplication by ten, far below `2^63-1`.

The minimum-integer sentinel only occurs when the corner list is empty. It is never multiplied inside the C++ producer; the Python verifier handles its threshold comparison with arbitrary-precision integers. Each nonempty corner computation has the origin as a feasible center and hence returns a finite score.

## Parallel completion and independent replay

Every primary `solve` call has private arrays. Parallel updates to the maximum, its witness and the count occur inside a critical region; the stop flag is atomic. A stop can only change the flag from false to true. Therefore an accepted completion flag implies that no corner was skipped and that every eligible corner satisfied the threshold. Early stopping on a failing bound only forces subdivision.

The verifier's subprocesses process separate leaf lists. Every replay must equal the stored exact maximum and must include at least the primary corner count; the independent worker actually enumerates all Cartesian corners. Nonsampled full replay asserts that every DP leaf was recomputed or checked against a matching prior record. In the new run, **no prior records are used**. Sources were copied to a new directory without executables, so the selected worker is compiled afresh rather than accepted through a modification-time check.

## Independent challenge without a horn decomposition

`round8/high_height_replay/brute_plane_cylinders.cpp` lists the three coordinate-plane lower ideals directly, matches their shared axis lengths, intersects their cylinders, and removes the orthant above `p`. Requiring each coordinate projection of `p` to belong to its plane ideal makes `p` a minimal excluded point. Every retained point is scored individually. There is no center, horn, or horn recurrence in this brute implementation.

The first challenge compared 53 exact parameter/corner cases, including nonconstant unequal interval weights. It enumerated 3,051,656 feasible ideals and computed 106,370,551 individual point scores. The brute maxima agreed exactly with the horn maxima in every case. These are finite consistency checks, not a replacement for the structural proof. Sources, complete rows, and counts are in `round8/high_height_replay/challenge_horn_model.py` and `brute_plane_cylinder_checks.json`.

Four additional weighted height-seven cases passed, with 1,577,910 feasible ideals; see `brute_weighted_height7_checks.json`. A larger exhaustive unit-weight height-seven check with `p=(1,2,2)` also passed: 1,278,654,031 compatible plane triples, 543,537,300 feasible ideals, and 35,562,744,901 individually scored points. Its direct maximum was -28, safely below the horn bound -20. This strict overbound is allowed because the horn program enlarges the class. The second completed unit-weight height-seven case, `p=(2,2,2)`, enumerated 299,057,140 feasible ideals and also gave direct maximum -28 versus horn bound -20. Both complete rows are preserved in `brute_height7_completed_cases.json`. The third optional batch case was interrupted and is not counted.

## Fresh full replay

Started from copied source and certificate bytes with:

```sh
python3 round8/high_height_replay/verify_residual_certificate.py \
  --certificate round8/high_height_replay/residual_parallel_interval_certificate.json \
  --worker specialized --jobs 8
```

No `--cache`, `--sample`, `--checkpoint`, or `--coverage-only` flag was supplied. The process writes `round8/high_height_replay/independent_residual_complete_checks.json`; stdout is preserved as `full_replay_stdout.txt`. Final outcome: **PASS**, process exit code zero. Every one of the 47,088 accepted leaves was recomputed in this run, covering all 35,852,138 Cartesian corner cases. Cached leaves and cached cases are both zero; `sampled=false` and `coverage_only=false`. Complete rational tree coverage records 47,229 splits, 47,088 DP leaves and 142 empty leaves, with no pending or unresolved node. Runtime was 886.345886 seconds.

`fresh_replay_provenance.json` records the exact command and hashes of the copied certificate, all worker sources, verifier, final report and stdout. I checked the copied certificate and all copied proof sources byte-for-byte against the audited originals after completion. The new full replay therefore supersedes the need to rely on the earlier mixed-worker cache history for the numerical high-height gate.

This concludes the delegated source and computational audit. Its conclusion remains conditional on the separately audited analytic compactness and structural theorems; finite model challenges are not presented as a proof of either dependency.
