# Four-generator Wilf: proof sources and certificates — revised 11 September 2026

Read `deliverables/wilf_four_generator_research_2026-09-10.md` first. Its dated scope
states the complete four-generator argument and distinguishes its proof
dependencies from diagnostic work. All final certificate gates have passed;
external mathematical review and proof-assistant formalization are outstanding.

The archive preserves proof sources and exact computation records. Inclusion
does not turn a failed or incomplete experiment into a universal certificate.
Historical conditional statements must be read with their later audits.

The 11 September review is in `round8/review_synopsis.md`. It records the
additional 380,607 independently verified low-height duals, so that all
3,742,041 surviving residual shapes now have the same rational certificate.
The separate (1,1,1) corner still uses the six-final-window theorem.

Run these core reproduction commands from the extracted archive root
(Python 3, Node.js, and C++17; do not disable Python assertions):

```
python3 round4/verify_completed_results.py
node round7/verify_uniform_gap.js
python3 round5/weight_arrangement/verify_interval_certificate.py
python3 round5/structural_audit/verify_complete_short_corner.py
python3 round5/interior_arithmetic/verify_low_height_weighted.py
python3 round5/small_multiplicity/verify_exhaustion.py --rerun
python3 round5/secondary_quotients/verify_secondary_implications.py
python3 round7/global_step/verify_surface_identities.py
python3 round7/low_degree6/verify_complete_certificate.py
python3 round8/simplification/verify_certificate.py
python3 round7/geometric_residual/verify_residual_certificate.py --certificate round7/geometric_residual/residual_parallel_interval_certificate.json --worker specialized --jobs 8
python3 round7/verify_type_fixture.py
```

The high-height command above uses no cache and freshly recomputes all
47,088 accepted leaves. The frozen certificate has SHA-256
`173fe6ec196b3d2adabad313749482542ad3492b5f6b4e398e76bbe6e52e405c`.
The saved report `independent_full_tree_replay_47088_checks.json` in that
directory records the first complete observed independent replay. Historical
prefixes and checkpoints are not substitutes for this final certificate.

The independent rational verification does not require the floating-point
optimizers used to propose certificates. Some exploratory scripts do require
SciPy/NumPy. A complete fresh replay of the older six-point dependency uses
SciPy for discovery; its runner changes to its own working directory:

```
python3 round7/six_point_dependency_replay/run_six_point_verification.py
```

To check the stored six-point rational certificates using only Python's
standard library, first change to that subtree:

```
cd round7/six_point_dependency_replay
python3 verify_six_certificates.py
python3 verify_corner_completion.py
python3 wilf_column_bound.py
```

The complete unit-weight one-corner result is separately reproducible from
the archive root with
`python3 round5/weighted_analytic/one_corner/verify_unit_one_corner_theorem.py`.

MANIFEST.json records the SHA-256 digest of every included payload. Replays
may regenerate timing records. Compiled executables and third-party library
installations are excluded. Binary files, when present, are exact witness
indices, not executable code.
