# Wilf's inequality for four generators

Start with the [first-draft paper](manuscript/wilf-four-generators.pdf).

| Directory | Contents |
|---|---|
| [manuscript/](manuscript/README.md) | Self-contained TeX manuscript, bibliography, and PDF |
| [verification/](verification/README.md) | Code and certificates for Finite Lemmas 2.2–2.8, checking specification, and complete-run record |
| [archive/](archive/README.md) | Original GPT-6 Astra manuscript and exploratory artifacts, preserved for provenance |

Build the paper with `make -C manuscript pdf`.
Reproduce all seven computational assertions with
`python3 -I -B verification/verify.py`.
The [complete-run record](verification/replay.json) identifies checked inputs
and results for all seven assertions and 35 rejection tests.
