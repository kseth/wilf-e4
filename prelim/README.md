# Preliminary standalone proof packet

Start with [proof.md](proof.md). It states the proposed theorem, proves its
reductions, gives an exhaustive case partition, and specifies every retained
finite premise. [analytic-details.md](analytic-details.md) contains the three
longer analytic proofs. [verification.md](verification.md) explains the code,
data format, replay, and trusted boundary.

This directory is self-contained. Copying it elsewhere is sufficient to read
and replay the argument. No Git checkout, network access, research archive,
precomputed witness list, or third-party Python package is required.
Only the explicitly cited published multiplicity-at-most-19 result is taken
as an upstream theorem rather than replayed here.

## Reproduce

Use Python 3.10 or newer and a C++17 compiler available as `c++`.
From this directory:

```sh
python3 -I -B verify.py
```

The command freshly compiles and runs both checking paths for all seven
retained finite premises. It checks hashes, complete coverage, exact
predicates, negative tests, and independent agreement. It writes
[replay.json](replay.json), replacing any previous replay record.
No partial mode can certify the packet. The high-height component is the
longest computation; budget substantial CPU time rather than assuming an
interactive test. Native interval leaves use available cores, with at most
eight evaluator processes in total. Temporary executables are automatically removed.

## Minimal inventory

| Item | Purpose |
|---|---|
| Three linked documents above | Complete mathematical argument and verification specification |
| This README and [verify.py](verify.py) | Reader entry and complete replay |
| [code/](code) | Two independent evaluators/coverage paths per finite premise |
| [data/](data) | Three topology-only closed interval trees, about 3.4 MB combined |
| [manifest.json](manifest.json) | Exact source/document/data identities |
| [replay.json](replay.json) | One complete-run evidence record; never an acceptance input |

This is a preliminary computer-assisted proof, internally checked under the
stated trust boundary. It is neither externally reviewed nor formally
certified. AI assisted its development; human authors must take responsibility
for the mathematics, computation, and attribution. Definitive TeX/PDF
production and any proof-assistant work are subsequent decisions.
