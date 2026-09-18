# Wilf simplification and dimension-generalization supplement

11 September 2026.

Read the research memorandum in the deliverables directory first. This archive supplies the new all-weight centroid certificates and the higher-dimensional structural examples. It supplements the previous complete four-generator proof archive; it does not contain a second copy of all earlier high-height certificates.

## Complete new certificate replay

From the extracted archive root:

~~~sh
python3 round9/height_free_duals/verify_complete_certificate.py
~~~

Requirements: Python 3 standard library and a C++17 compiler supporting GCC/Clang's 128-bit integer and population-count extensions, available as "c++".

The entry point checks immutable hashes, builds the independent verifier in a temporary directory, regenerates all enumerated shapes, checks all 3,742,041 assignments exactly, and compares every coverage field. It does not overwrite archived certificate inputs or outputs. No optimization package is needed.

A successful actual run is recorded in round9/height_free_duals/portable_full_replay_result.json. The "--records-only" option only compares existing records and hashes; it is not a new mathematical replay.

## Five-generator structural examples

~~~sh
python3 round9/check_dimension_obstruction.py
~~~

This independently computes both Apéry sets by shortest paths, checks minimal generators and excluded corners, and verifies the cycle and projection obstructions. It writes round9/dimension_obstruction_checks.json. The semigroups both satisfy Wilf.

## What is included

- The new research memorandum, centroid theorem, exact registry, binary assignments, generation source, separate verification source, portable entry point, and observed replay records.
- General-dimension elementary proofs and the two explicit five-generator examples.
- The archived 5 September fixed-dimension analytic manuscript, included for review of the proposed quantitative finite-reduction result. Its historical status statements refer to that date.
- Selected previous notes and sources documenting the low-degree arithmetic filters and the exact source changes.
- Old-registry compression statistics and diagnostic sample results. Their optional analysis scripts require original input streams from the previous complete proof archive; they are not needed for the new certificate replay.

MANIFEST_SHA256.json at archive root records every included payload's hash and size, excluding itself. The inner certificate manifest independently records the immutable new proof inputs.

## Status

The preceding four-generator proof and the new simplification remain proposed research results pending external mathematical review. The exact checks described here completed successfully in this session. No proof-assistant formalization or proof for unrestricted embedding dimension five is claimed.
