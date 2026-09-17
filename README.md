# Wilf's conjecture in embedding dimension four

Start with the [TeX paper draft](manuscript/wilf-four-generators.pdf), whose
sources and build instructions are in [manuscript/](manuscript/README.md).
The frozen [prelim/](prelim/README.md) packet contains the selected Markdown
proof, its necessary analytic details, and exact independent verification
code. Its [verification specification](prelim/verification.md) describes
the complete replay. No historical manuscript or research archive is needed
to read, compile, or run these artifacts.

The theorem remains proposed: AI-assisted internal checking is not external
mathematical review or proof-assistant certification. Human authors are
responsible for the mathematics, computation, and attribution.

## Current state

| Item | State |
|---|---|
| Branches B1--B6 | Internally complete; B3 is entirely analytic |
| Standalone PRELIM | Complete isolated replay: all seven finite premises pass on both independent paths |
| Attribution | Selected-source refresh dated 2026-09-17; bounded novelty assessment, not priority certification |
| TeX/PDF draft | Initial self-contained draft; all analytic proofs included; frozen code remains unchanged |
| External review, formalization choice, definitive release | Separate subsequent milestones |

From `prelim/`, reproduce the whole finite verification with
`python3 -I -B verify.py`. Only Python standard libraries and a C++17
compiler are required. The packet contains three topology-only trees,
about 3.4 MB total, and no saved dual/fallback lists or cached leaf bounds.
The [complete-run record](prelim/replay.json) matches the frozen manifest,
includes 35 rejection tests, and confirms execution outside the Git checkout.

## Repository roles

| Location | Role |
|---|---|
| [prelim/](prelim/README.md) | Selected standalone reader/replay artifact |
| [manuscript/](manuscript/README.md) | Preliminary TeX paper and compiled PDF; no historical reading dependencies |
| [ROADMAP.md](ROADMAP.md) | Live milestone status and remaining order |
| [paper/](paper) | Detailed reconstruction notes and frozen mathematical replay inputs |
| [verification/](verification) | Component audits and source-specific reconstruction replays |
| [literature/](literature/survey.md) | Broader dated survey and upstream theorem audits |
| [research/](research/prelim-synthesis-audit.md) | Route decisions, composition audit, and curation/QA conveniences |
| [artifacts/](artifacts) | Preserved research history; neither reader dependency nor blanket-certified package |

Some reconstruction notes deliberately preserve superseded alternatives or
status at a source-freeze checkpoint. They are not the current manuscript.
The PRELIM packet and roadmap identify the selected argument.
