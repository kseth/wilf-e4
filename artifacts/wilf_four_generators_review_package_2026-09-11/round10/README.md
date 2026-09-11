# Centroid proof simplification: reproducible supplement

11 September 2026.

Start with deliverables/wilf_centroid_local_constructions_2026-09-11.md.
This supplement preserves two alternative centroid arguments and direct
analytic proofs for infinite structural families.

## A. Explicit local or axis witness

From the extracted archive root:

~~~sh
python3 round10/local_centroid/verify_complete_local_centroid.py
~~~

Requirements: Python 3 standard library and GCC or Clang with C++17 support.

This independently enumerates all 5,574,644 ideals in the enlarged residual
class and checks two explicit formulas with integer arithmetic. It requires
no per-shape certificate, linear program, optimization library, or older
proof archive. The supplied completed run took about 25 seconds in the
session environment; runtime elsewhere may differ.

The verifier compiles and runs in a temporary directory, compares all
coverage and multiplicity records, independently reconstructs all 431
axis fallbacks using Python fractions, and refreshes its diagnostic
fallback and replay records. Mathematical inputs are identified by
local_centroid_manifest.json.

The exact consequence is D_0>=m for every normalized real weight vector.
The remaining finite assertion is that at least one explicit construction
attains the target. The erosion and refined plane-corner filters are absent.

## B. Universal indicator inequalities

~~~sh
python3 round10/envelope/verify_universal_envelope.py
~~~

Requirements: Python 3 standard library only. No SciPy or producer code is
imported by this verifier.

It independently reconstructs 2,425 primitive directions, all 44,281
parameter cells, and a common collection of indicator inequalities. It
then verifies the archived rational combinations with integer arithmetic.
There are 40,115 moment certificates and 4,166 exact cardinality exclusions.
The completed run took about 50 seconds in the session environment.

This route enumerates no individual ideals. It retains finite parameter
verification, the original arithmetic filters, and the earlier high-height
theorem. Its all-height consequence is D_0>=m-29/10, not the stronger
constant of route A. The high-height theorem and the other pieces of the
global four-generator argument remain in the preceding proof archive.

The compressed certificate file is the main large payload in this archive.
SciPy is used only if regenerating proposed multipliers with the separate
producer, which is unnecessary for verification.

## C. Direct analytic families

Read round10/symbolic/analytic_centroid_families.md for proofs covering
corner-clipped boxes and clipped prisms with arbitrary planar staircase
bases. The companion check_analytic_families.py verifies bounded algebraic
examples, but the symbolic arguments establish the infinite-family claims.

## Supporting records and limits

- round10/independent contains separate audits of the two constructions,
  the final expanded class, and the universal indicator argument.
- round10/ablation records which hypotheses were removed and exact failures
  of attempted further extensions.
- round10/line_upgrade retains the intermediate all-length construction and
  original-class checks, for provenance. Its older counts and thresholds
  are not the final theorem's counts.
- The bounded random probe is diagnostic only and proves no universal claim.

The original four-generator proof and these supplements remain proposed
research results pending external mathematical review. No proof-assistant
formalization is claimed. Neither finite-computation route has yet been
replaced by a fully analytic proof for all residual ideals.

MANIFEST_SHA256.json records every packaged payload's hash and size,
excluding itself. Inner manifests identify the principal proof files.
