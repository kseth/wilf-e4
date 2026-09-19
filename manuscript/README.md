# Manuscript

Start with [the PDF](wilf-four-generators.pdf) or [main.tex](main.tex).
The manuscript includes the analytic argument, seven finite
assertions, extensions, related work, bibliography, and construction history
crediting GPT-6 Astra and GPT-5.6 Sol via Codex.

## Build

From this directory, run `make pdf` with a standard TeX installation
providing `latexmk`, pdfLaTeX, and BibTeX. No shell escape or downloaded
assets are used. Intermediates stay in the ignored `build/` directory; the
reader-facing PDF is retained alongside its sources.

## Self-sufficiency audit

The eight TeX files and `references.bib` contain all analytic proofs,
finite-family definitions, reductions, and final arithmetic. Every internal
reference resolves, and all 15 bibliography entries are cited. The
warning-free 37-page PDF also builds from an isolated copy of the ten
source/build inputs, with identical rendered text.

The seven computational assertions are established by the accompanying
[verification code and certificates](../verification/README.md), mapped there
to Finite Lemmas 2.2–2.8 and their stable TeX labels. The published results
for multiplicities at most 18 and exactly 19 are explicitly cited in
Section 2.6. All other needed elementary upstream ingredients are proved
in the paper.

Reading and building the manuscript requires no archive, reconstruction
notes, or Markdown proof. Replaying the finite assertions requires only
`verification/`, Python's standard library, and a C++17 compiler. Numerical
width bounds and implementation details are in its
[specification](../verification/SPECIFICATION.md).
