# Preliminary TeX manuscript

This directory contains the TeX draft of Karthik Sethuraman's proposed
computer-assisted proof. It is separate from the frozen PRELIM verification
packet. The paper includes its complete analytic arguments; reading or
compiling it requires no historical manuscript or research notes.

Start with [the PDF](wilf-four-generators.pdf) or [main.tex](main.tex).
The mathematical sections conclude with extensions to embedding dimension
greater than four and related work. A construction-history section follows,
covering the initial GPT-6 Astra iterations, subsequent reconstruction
with GPT-5.6 Sol via Codex, attribution, and exact computer aids. There
is no separate responsibility section.

Build locally with `make pdf` from this directory, using a standard TeX
installation with `latexmk`, pdfLaTeX, and BibTeX. No shell escape or downloaded
assets are used. Build intermediates stay in the ignored `build/` directory;
the reader-facing PDF is retained alongside its sources.

`proof.tex` and `analytic.tex` transcribe the selected PRELIM argument,
with TeX theorem environments and cross-references. `verification.tex`
describes the seven retained finite premises and the accompanying artifact.
The bibliography cites primary sources and identifies the versions of
recent preprints. The extension section states only proved identities,
a conditional mesh transfer, and a lower-ideal obstruction; it claims no
uniform theorem for more than four generators.

The accompanying code remains in [../prelim/](../prelim/README.md).
Run `python3 -I -B verify.py` there to recompute every retained finite premise.
Its frozen manifest and complete replay have not been changed by TeX drafting.
This is an initial manuscript, not a final reviewed release.

## Draft checks

The initial draft passes the editorial comparison against PRELIM: 186
displayed formulas and 941 inline mathematical expressions are preserved,
apart from numbering and the local full-weighted label notation. Its 153
labels resolve and all 15 bibliography entries are cited. The converged
38-page build has no warnings. A cold build from just the ten required
source/build files outside the checkout produces identical rendered text,
without PRELIM, Git, or historical files present.

After `make pdf`, the repository-level authoring check is
`python3 -I -B research/audit_tex_draft.py` (run from the repository root;
requires Poppler's `pdftotext`). It checks transcription and build hygiene,
not the correctness of the deductions or computational premises.
