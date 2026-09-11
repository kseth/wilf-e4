# Secondary-semigroup branch of the fifth research round

The completed work is `no_interior_secondary_implication_audit.md`, with exact auxiliary checks in `verify_secondary_implications.py` and their output in `secondary_implication_checks.json`.

It proves that a verified no-interior theorem at multiplicity at least 30 implies Wilf for the entire paired secondary class, without waiting for the separate multiplicity-20-through-29 enumeration. The new useful lower bound is that a common quotient of multiplicity at least three forces the original semigroup multiplicity to be at least 35; this bound is sharp.

The initial `probe.py` and `probe_universal.py` explored normalized multiplicity-three quotient fibers with unequal thresholds. They use floating-point arithmetic and are diagnostics only. No theorem or certificate depends on them. That narrower line was paused when the broader no-interior certificate became available. These probes are not evidence that every unequal-threshold inequality holds.
