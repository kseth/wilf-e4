# Reproducing the six-point Wilf theorem and the column theorem

Read `wilf_edim4_six_point_and_column_theorems_2026-09-05.md` first. The results are:

- A computer-assisted proof of Wilf for every minimally four-generated numerical
  semigroup whose Apéry set has at most six elements in `[c,c+m)`.
- An analytic sufficient theorem in every embedding dimension `e >= 4`: if a
  preferred Apéry staircase has `A` columns in some direction, with minimum
  column length `h`, then `2*A*(h-1) >= m` implies `e*n-c >= e-2`.
- An analytic, order-invariant criterion for a prescribed antichain to remain
  maximal in a lower ideal with at most one interior minimal excluded point.

This package does not prove unrestricted Wilf and does not assert novelty.

## Full reproduction

Requirements: Python 3, a C++17 compiler available as `c++`, and SciPy for
discovering moment certificates. The recorded run used Python 3.12.13 and
SciPy 1.17.0. Do not use `python -O`; assertions perform exact checks.

Extract the archive into a directory in which its generated JSON files and
logs may be overwritten, then run:

```bash
python3 run_six_point_verification.py
```

The complete recorded run took about 48 seconds. It includes the previous
`|Z| <= 5` proof and generates every compressed six-point antichain, all relevant
expansions and extensions, and every residue-bijective labeling. The mathematical
proof of exhaustiveness is in the note. No generator or conductor cutoff is used.

The runner writes `six_full_run_results.json`; stage logs are named there.
The 64-point limit in the C++ residue checker is guarded by an assertion on the
exhaustively generated shapes: their largest size is 56.

## Check stored certificates without SciPy

Only the Python standard library is needed for:

```bash
python3 verify_six_certificates.py
python3 verify_corner_completion.py
python3 wilf_column_bound.py
```

The first command checks exact rational primal and dual certificates for all
71 residue-feasible shapes, plus all 23,002 modular cuts for 930 residue
labelings. It verifies arithmetic soundness of the stored certificates; generation
completeness also uses the analytic proof and the full enumeration above.

The other two commands provide diagnostics for the analytically proved
completion and column theorems. Their finite tests alone are not proofs of the
general statements. The completion fixtures include an example requiring a
proper extension of the lower hull, so simply rejecting every lower hull with
two interior corners would be an incorrect substitute for the criterion.

## Files

`enumerate_compressed.cpp`, `wilf_six_point.py`, and `extend_six_point.py`
generate the finite structural candidates. `check_residue_labels.cpp` exhausts
residue labelings. `certify_six_point.py` generates the exact arithmetic records;
SciPy suggestions are accepted only after rational primal and dual checks.

The `six_*.json` files store the generated sets, certificates, and results.
`six_arithmetic_results.json` contains all dual witnesses and modular slacks.
Shape indices refer to `six_candidate_shapes.json` and use zero-based numbering.

`verify_final_window.py`, `wilf_work.py`, and `wilf_reassessment.py` are dependencies
from the preceding research. The earlier progress note is included unchanged
for its `|Z| <= 5` proof and full reflection bookkeeping. The reassessment note
is included as historical context; its statement that six points remain
unfinished is superseded by the new note.

`six-point-SHA256SUMS.json` records hashes of all other files shipped in this subtree. It is refreshed when the dated archive is assembled.
Compiled binaries and temporary residue-input files are regenerated, not shipped.
