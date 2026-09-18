# Wilf in four generators: consolidated review package

11 September 2026.

**Read `deliverables/wilf_four_generators_review_manuscript_2026-09-11.pdf` or its Markdown counterpart first.** That reading manuscript is the canonical presentation of the current argument. It states a proposed computer-assisted proof of Wilf's inequality for embedding dimension four, identifies every retained dependency, and separates the analytic constructions from the remaining finite verifications. External mathematical review and proof-assistant formalization have not been performed.

This package contains the earlier full proof archive's contents, followed by the two subsequent simplification rounds and the current editorial review. Historical notes may have superseded scope statements, constants, bibliography, and reproduction priorities. Their inclusion preserves evidence and provenance; the current reading manuscript governs the interpretation of the proof. Failed experiments and partial results remain labeled as such.

## Reading order

1. `deliverables/wilf_four_generators_review_manuscript_2026-09-11.pdf` (or `.md`): presentation, definitions, proof composition, higher-dimensional results and limitations.
2. `round11/proof_map.md`: exact case partition, dependency paths, retained replay counts, and which historical computations are unnecessary for the selected route.
3. `round10/local_centroid/local_centroid_theorem.md`: the preferred local centroid lemma and explicit witnesses.
4. `round11/final_manuscript_audit.md` and `round11/editorial_audit.md`: current in-session review. Other Round 11 review notes are included alongside these.
5. The earlier manuscripts and audit files referenced by the proof map, for the complete analytic and computational foundations.

The two preceding simplification memoranda are included under `deliverables/`: `wilf_simplification_and_higher_dimensions_2026-09-11.md` and `wilf_centroid_local_constructions_2026-09-11.md`.

## Preferred centroid route

The local construction moves each coordinate-line top at most two coordinate steps. The second construction uses the three axis endpoints. Both provide explicit convex-hull witnesses; no linear programming or per-shape certificate registry is required.

On the stated degree-at-most-six residual class, the remaining computer-assisted assertion is that one construction has surplus at least the ideal's cardinality. The two independent implementations cover **5,574,644** shapes. The local construction succeeds on **5,574,213**, and the other **431** use the axis construction. The assertion that these formulas cover every member of the class is still exhaustive verification. The erosion and refined dominating-corner restrictions are no longer needed for this route.

From the extracted archive root, run:

```sh
python3 round10/local_centroid/verify_complete_local_centroid.py
```

Requirements: Python 3 standard library and a C++17 compiler. The script verifies its source manifest, compiles into a temporary directory, performs a complete fresh enumeration, compares all nine coverage records and multiplicity histograms, and independently reconstructs all 431 fallbacks with exact Python fractions. The recorded session run took about 25 seconds; this is not a runtime guarantee for other machines.

The high-degree branch still uses the earlier high-height theorem. Other multiplicity and corner classes retain their separate proofs. A successful local-centroid run alone does not reprove the full four-generator result.

## Other retained global proof components

The complete mathematical dependency map is `round11/proof_map.md`. These principal commands reproduce its older finite components; run them from the extracted archive root, and do not disable Python assertions.

```sh
node round7/verify_uniform_gap.js
python3 round5/weight_arrangement/verify_interval_certificate.py
python3 round6/short_corner_audit/verify_complete_short_corner.py
python3 round5/interior_arithmetic/verify_low_height_weighted.py
python3 round5/small_multiplicity/verify_exhaustion.py --rerun
python3 round7/geometric_residual/verify_residual_certificate.py --certificate round7/geometric_residual/residual_parallel_interval_certificate.json --worker specialized --jobs 8
```

These cover, respectively, the finite input to the continuous gap, no-interior intervals, short-corner intervals, short-corner low-height duals, multiplicities 20 through 29 in the analytically justified generator boxes, and the residual high-height certificate. Some commands require Node.js or C++17 as well as Python. The source notes explain the associated analytic reductions and why the finite domains cover all intended cases.

The last command supplies no cache and freshly recomputes every accepted high-height leaf. The completed recorded run contains **47,088** accepted leaves and **35,852,138** full Cartesian corner cases; it is not a sample. Its fixed certificate SHA-256 is:

`173fe6ec196b3d2adabad313749482542ad3492b5f6b4e398e76bbe6e52e405c`

The remaining six-final-window dependency applies to the corner `(1,1,1)`. Its full historical runner is:

```sh
python3 round7/six_point_dependency_replay/run_six_point_verification.py
```

That runner regenerates discovery data and uses SciPy/NumPy. Verification of the saved six-point rational certificates is smaller and uses Python's standard library, but is **not** a replacement for reproducing the full combinatorial coverage. The corresponding local commands, after changing to that subtree, are:

```sh
python3 verify_six_certificates.py
python3 verify_corner_completion.py
python3 wilf_column_bound.py
```

The negative-case conductor reduction used for small multiplicities is an analytic dependency; checking bounded generator tuples alone does not establish its infinite scope. Likewise, the published small-multiplicity-through-19 result remains an explicit external mathematical input.

## Alternative routes and historical material

The universal-indicator route is an alternative centroid proof with **44,281** finite parameter checks, rather than an enumeration of individual ideals:

```sh
python3 round10/envelope/verify_universal_envelope.py
```

It uses only Python's standard library to verify the stored exact rational combinations. It retains the original arithmetic restrictions and the high-height theorem, and supplies the weaker surplus `m - 29/10`. It is not needed alongside the preferred local route. Its producer uses SciPy, but independent verification does not import the producer or use an optimizer.

Round 9's height-free dual registry, earlier residual low-height duals, and the alternative short-corner generator enumeration are preserved for provenance. They are not additional necessary gates of the selected current proof. Binary `.bin` files in these directories are exact witness indices used by historical verifiers, not compiled executables.

`round10/symbolic/analytic_centroid_families.md` gives direct proofs for clipped boxes and specified clipped prisms. Their bounded algebra checks are diagnostics; the displayed formulas prove their infinite-family statements. The discussion of higher embedding dimensions does not establish unrestricted Wilf for any embedding dimension greater than four. Genuine five-generator structural examples explain why the three-coordinate horn decomposition does not simply extend.

## Integrity and reproduction boundaries

`MANIFEST.json` records the SHA-256 digest and byte length of every payload except itself. The old root README and manifest have moved to:

- `archive_notes/legacy_2026-09-10_README.md`
- `archive_notes/legacy_2026-09-10_MANIFEST.json`

The legacy manifest refers to the legacy archive's original root names. Its recorded source archive hash identifies that version; the consolidated root manifest describes the current paths. No historical proof-file content was silently overwritten during merging.

To verify the files immediately after extraction:

```sh
python3 round11/build_review_package.py --verify-extracted
```

To verify the consolidated ZIP itself from the original workspace:

```sh
python3 round11/build_review_package.py --verify-existing deliverables/wilf_four_generators_review_package_2026-09-11.zip
```

These are **payload and hash checks only**. They confirm complete inclusion of the retained proof-map paths, all Round 10 proof-manifest entries, and the final payload hashes. They run no mathematical verifier and must not be reported as fresh proof replays. Reproduction commands may regenerate timing or diagnostic files, so a post-replay hash difference should be inspected against that command's documented outputs.

The build script can also reconstruct the consolidated ZIP from the original workspace with its legacy ZIP and finalized reading PDF. It is included for assembly provenance; it is unnecessary for mathematical verification. Compiled executables, Python caches, PDF build images, and temporary build files are excluded. Python/C++/JavaScript sources, exact proof data, `.bin` witness assignments, and the current TeX source are retained.
