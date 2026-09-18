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
A fresh replay from an isolated copy passed both implementations of all seven
assertions and all 35 rejection tests; see the
[complete-run record](verification/replay.json).
