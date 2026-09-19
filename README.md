# Wilf's inequality for four generators

This repository contains a computer-assisted proof of Wilf's conjecture for
numerical semigroups with four minimal generators, with a self-contained
manuscript and reproducible code for its finite computations.

Start with the [Current Manuscript](manuscript/wilf-four-generators.pdf).

| Directory | Contents |
|---|---|
| [manuscript/](manuscript/README.md) | Self-contained TeX manuscript, bibliography, and PDF |
| [verification/](verification/README.md) | Code and certificates for Finite Lemmas 2.2–2.8, checking specification, and complete-run record |
| [archive/](archive/README.md) | Original GPT-6 Astra manuscript and exploratory artifacts, preserved for provenance |

The interval certificates are subdivision trees: the checkers verify complete
coverage and recompute the bounds. Input hashes identify tested files; result
fingerprints compactly compare the two checkers' outputs.

Build the paper with `make -C manuscript pdf`.
With Python 3.10 or newer and a C++17 compiler, reproduce all seven
computational assertions with
`python3 -I -B verification/verify.py`.
The current complete replay passed both implementations of all seven
assertions and all 67 rejection tests; see the
[complete-run record](verification/replay.json).
