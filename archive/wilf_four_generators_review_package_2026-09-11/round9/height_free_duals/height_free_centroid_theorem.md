# A unified centroid-witness theorem for the residual low-degree ideals

11 September 2026. **All 3,742,041 exact certificates generated and independently replayed successfully.**

## Statement

Let T be a finite lower ideal in N^3 of total degree at most six, with m=|T|>=30, and with exactly one full-support minimal excluded point p of coordinate sum between five and seven. Assume the arithmetic corner, erosion, and pairwise surface restrictions specified in `round7/low_degree6/low_height_theorem.md`. Then there is a point y in conv(T) such that

\[
3m y_i\ge4\sum_{x\in T}x_i\quad(i=1,2,3),
\]

and

\[
3m\sum_i y_i-4\sum_{x\in T}\sum_i x_i\ge m-\frac{29}{10}.
\]

Moreover, y is a convex combination of at most three points of T in every generated certificate. Consequently, for **every** real vector b with b_i>=1 and every H>=max_T b.x, with no upper bound on H,

\[
\boxed{3mH-4\sum_{x\in T}b\cdot x\ge m-\frac{29}{10}.}
\]

This is a stronger, unified replacement for the two previous residual low-height certificate streams. It still relies on complete enumeration of a finite class of ideals. The residual proof can now split by **total degree**: degree at most six is covered here, while degree at least seven automatically gives H>=7 for b_i>=1 and is covered by the existing high-height theorem. It does not prove a general centroid theorem in all degrees or dimensions.

## Proof from the witnesses

Write s=sum_T x. Each verified dual is a nonnegative rational combination of columns (-x,1) for x in T and coordinate unit columns e1,e2,e3, possibly the redundant column e4. The column -e4, encoding H<=7, is forbidden by the new verifier. The combination equals (-4s,3m), and the sum of the multipliers on e1,e2,e3 is at least m-29/10.

In fact the completed registry never uses e4 either. If lambda_x are the point multipliers and beta_i the weight-bound multipliers, the four coefficient identities therefore say

\[
\sum_x\lambda_x=3m,\qquad
\sum_x\lambda_x x=4s+\beta,\qquad
\sum_i\beta_i\ge m-29/10.
\]

Taking y=(1/(3m))sum lambda_x x proves the two centroid statements. In the compact notation z=y and r=3mz-4sum_T x, this is precisely z in conv(T), r>=0 coordinatewise, and sum_i r_i>=m-29/10. This witness condition contains neither a weight variable nor a height cutoff. Conversely these statements imply the weighted inequality by H>=b.z and b.r>=sum r_i. The equivalence between a height-free nonnegative dual and such a witness follows from the displayed coefficient identities; the direct implication to every real weight vector needs only convexity and b_i>=1. Each basis has four columns, includes at least one coordinate weight bound, and hence uses at most three point columns.

## Exact finite coverage

The planar-profile enumeration and all arithmetic filters are unchanged. The only selection change is that the formerly separated cases with at most six coordinatewise maxima are included in the same run. The 3,742,041 accepted ideals are distributed among corner types as follows:

| Corner | Ideals |
|---|---:|
| (1,1,3) | 708,617 |
| (1,2,2) | 976,430 |
| (1,1,4) | 571,100 |
| (1,2,3) | 519,716 |
| (2,2,2) | 533,570 |
| (1,1,5) | 150,481 |
| (1,2,4) | 100,341 |
| (1,3,3) | 90,696 |
| (2,2,3) | 91,090 |
| **Total** | **3,742,041** |

The new common registry has 6,816 bases, compared with 10,246 bases across the two old registries. Its bases fall into 2,723 coordinate-symmetry types. The last symmetry count is descriptive; the actual verified stream uses full oriented bases. No claim is made that this registry is minimal.

The generator proposes candidate bases using its prior floating-point simplex implementation, with the H<=7 row removed. Acceptance requires exact determinant and adjugate identities and the rational lower bound. No floating-point value is trusted for a proof step.

The independent verifier imports no generator header. It constructs plane profiles by subsets and literal column-height arrays, recomputes all geometric filters, checks point containment, verifies the exact duals with its checked Bareiss/Cramer implementation, and consumes every assignment in order with no trailing bytes. It explicitly rejects column347, which would encode the removed height bound. The full run returned:

```json
{"status":"passed","profiles":1429,"bases":6816,"exact_weighted_duals":3742041,"floating_point_used":false}
```

All nine coverage records, moment-margin minima, and multiplicity histograms match the producer. The binary assignment stream contains 14,968,164 bytes: one little-endian uint32 basis index per ideal.

## Reproduction and provenance

Run the complete independent verifier using Python standard library and a C++17 compiler:

```sh
python3 round9/height_free_duals/verify_complete_certificate.py
```

The portable Python entry point first verifies the immutable input manifest, compiles the independent C++17 source in a temporary directory, copies the exact registries into that directory, runs a full replay, and checks every coverage field and histogram. It does not modify the archived proof files. The documented completed full C++ run is recorded in `independent_result.json` and `independent_stderr.txt`. The earlier Python `--records-only` check is correctly marked as a record comparison in `complete_independent_verification.json`; it is not a substitute for that completed full replay. A second full replay using the portable temporary-directory entry point is recorded in `portable_full_replay_result.json`.

The source modifications are narrowly scoped. Relative to `round7/low_degree6/certify_all.cpp`, the new generator includes both maxima counts, removes the H<=7 LP constraint, and rejects unexpected LP variables that could refer to that removed constraint. Relative to `round7/low_degree6/independent_verify.cpp`, the new verifier includes both maxima counts, enforces a total of 3,742,041, and rejects every registry reference to column347. The corresponding Python entry point changes the expected basis count, total, and the identity `q_ok=remaining`.

This is a new computer-assisted lemma and has undergone the stated in-session exact checks. External mathematical review and proof-assistant formalization have not been performed.
