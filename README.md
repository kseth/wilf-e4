# Wilf's conjecture in embedding dimension four

The reader-facing artifact is [prelim/](prelim/README.md): a standalone
preliminary proof, its necessary analytic details, and exact independent
verification code. Start with [the proof](prelim/proof.md), then its
[verification specification](prelim/verification.md).
No historical manuscript or research archive is needed to read or run it.

The theorem remains proposed: AI-assisted internal checking is not external
mathematical review or proof-assistant certification. Human authors are
responsible for the mathematics, computation, and attribution.

## Current state

| Item | State |
|---|---|
| Branches B1--B5 | Internally complete; B3 is entirely analytic |
| B6 analytic reductions and finite strip | Complete internally; \(5/42\) transfer established |
| B6 high-height verification | Internally complete; both fresh paths agree on all 47,088 leaves |
| Standalone PRELIM sources | Frozen; six shorter premises passed in an isolated copy, final high-height pair running |
| Attribution | Selected-source refresh dated 2026-09-17; bounded novelty assessment, not priority certification |
| External review, formalization choice, definitive TeX/PDF | Separate subsequent milestones |

From `prelim/`, reproduce the whole finite verification with
`python3 -I -B verify.py`. Only Python standard libraries and a C++17
compiler are required. The packet contains three topology-only trees,
about 3.4 MB total, and no saved dual/fallback lists or cached leaf bounds.

## Repository roles

| Location | Role |
|---|---|
| [prelim/](prelim/README.md) | Selected standalone reader/replay artifact |
| [ROADMAP.md](ROADMAP.md) | Live milestone status and remaining order |
| [paper/](paper) | Detailed reconstruction notes and frozen mathematical replay inputs |
| [verification/](verification) | Component audits and source-specific reconstruction replays |
| [literature/](literature/survey.md) | Broader dated survey and upstream theorem audits |
| [research/](research/prelim-synthesis-audit.md) | Route decisions, composition audit, and curation/QA conveniences |
| [artifacts/](artifacts) | Preserved research history; neither reader dependency nor blanket-certified package |

Some reconstruction notes deliberately preserve superseded alternatives or
status at a source-freeze checkpoint. They are not the current manuscript.
The PRELIM packet and roadmap identify the selected argument.
