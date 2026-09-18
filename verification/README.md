# Verification companion

This directory supplies the code and certificates for Finite Lemmas 2.2–2.8
of the [manuscript](../manuscript/wilf-four-generators.pdf). Their mathematical
domains, reductions, and acceptance inequalities are stated in the paper.
[SPECIFICATION.md](SPECIFICATION.md) describes the algorithms, certificate
format and arithmetic bounds.

## Run

Use Python 3.10 or newer and a C++17 compiler available as `c++`:

```sh
python3 -I -B verify.py
```

Run from this directory, or invoke the script by its path. The complete run
freshly compiles and executes both implementations of all seven assertions,
checks exact input identities and interval coverage, and runs 35 rejection
tests. The runner executes from this directory using Python's standard
library and a C++17 compiler. The recorded isolated run took approximately
14 minutes.

The command writes [replay.json](replay.json), replacing the previous run
record. The manifest identifies verification inputs; the replay record
reports execution results and input hashes.

## Manuscript correspondence

| Finite lemma | Assertion / replay component | Evaluators |
|---|---|---|
| 2.2 (`finite:generator-box`) | Generator-box / `generator-box` | `generator_box_residues.cpp`, `generator_box_membership.cpp` |
| 2.3 (`finite:no-corner-interval`) | No-corner interval / `no-corner-interval` | `no_corner_interval_prefix.py`, `no_corner_interval_direct.py` |
| 2.4 (`finite:short-corner-high`) | Short-corner high / `short-corner-high` | `short_corner_high_prefix.cpp`, `short_corner_high_direct.cpp` |
| 2.5 (`finite:short-corner-low`) | Short-corner low / `short-corner-low` | `short_corner_low_offsets.py`, `short_corner_low_successors.py` |
| 2.6 (`finite:degree-six`) | Degree-six / `degree-six` | `degree_six_bits.cpp`, `degree_six_columns.cpp` |
| 2.7 (`finite:strip`) | Strip / `strip` | `strip_prefix.cpp`, `strip_points.cpp` |
| 2.8 (`finite:high-height`) | High-height / `high-height` | `high_height_subtract.cpp`, `high_height_disjoint.cpp` |

Evaluator files are in [code/](code). The two independent interval coverage
paths are `trees_integer.py` and `trees_rational.py`.
[data/](data) contains three topology-only interval certificates, named after
their assertions, totaling approximately 3.4 MB.
[manifest.json](manifest.json) identifies every checking input.
[verify.py](verify.py) manages compilation, execution, and result agreement.
