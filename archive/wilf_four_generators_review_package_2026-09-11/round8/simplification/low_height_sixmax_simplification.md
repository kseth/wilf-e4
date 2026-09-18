# The residual low-height proof no longer needs the six-point theorem

11 September 2026.

**Status: complete exact certification and full independent replay passed.**

The prior residual low-height argument sent 380,607 shapes with at most six coordinatewise maximal points to the six-final-window theorem and certified the other 3,361,434 shapes by exact rational linear inequalities. This supplementary computation proves the same rational inequality for all 380,607 previously skipped shapes. Thus every one of the 3,742,041 surviving residual low-height shapes is now covered by the rational inequality. The six-point theorem is no longer a dependency of this residual branch. This change does not remove that theorem from the separate `(1,1,1)` corner branch.

## Exact statement

Let `T` be a preferred Apéry exponent lower ideal of a minimally four-generated numerical semigroup. Write

\[
m=|T|\ge30,\qquad A=\min(a_1,a_2,a_3),\qquad
b_i=a_i/A\ge1,\qquad H=\max\operatorname{Ap}(S,m)/A<7.
\]

Assume that the unique full-support minimal excluded point `p` has coordinate sum at least five. Then

\[
\boxed{3mH-4\sum_{x\in T}b\cdot x\ge m-\frac{29}{10}.}
\]

Here the weights are arbitrary real weights. No discretization of the weight variables is used.

Indeed, `T` has degree at most six and `p` has coordinate sum at most seven. Up to coordinate permutation the possible corners are

\[
(1,1,3),(1,2,2),(1,1,4),(1,2,3),(2,2,2),
(1,1,5),(1,2,4),(1,3,3),(2,2,3).
\]

Every genuine `T` is obtained from three compatible planar profiles by removing the upper orthant of `p`, and satisfies the plane-corner restrictions, the erosion restriction, and the pairwise surface restriction proved in `round7/low_degree6/low_height_theorem.md`. These are the same finite-shape coverage conditions as before. This supplementary computation changes only the terminal selection: it verifies the shapes with at most six maxima instead of skipping them.

## Certificate argument

Put `s_i=Σ_{x∈T}x_i`. Each certificate is a nonnegative rational combination of four columns from

\[
(-x_1,-x_2,-x_3,1)\quad(x\in T),\qquad
e_1,e_2,e_3,e_4,-e_4.
\]

The combination equals `(-4s_1,-4s_2,-4s_3,3m)`. The respective right-hand sides are zero for point constraints `H−b·x≥0`, one for the weight bounds `b_i≥1`, zero for `H≥0`, and negative seven for `−H≥−7`. The same combination of right-hand sides is at least `m−29/10`. Therefore the desired inequality follows for all feasible real weights and every `H≤7`.

The generator proposes four-column bases using a floating-point simplex routine when recent bases do not work. Acceptance requires exact integer determinant and adjugate computations, nonnegative rational multipliers, all four coefficient identities, and the exact lower bound. The independent verifier imports no generator header. It generates planar profiles as subsets, constructs literal column-height arrays, counts surfaces and erosion directly, and uses checked Bareiss determinants and Cramer's rule. Every referenced point constraint must belong to the current ideal. No floating-point arithmetic is used in verification.

The supplementary source changes are intentionally small and inspectable:

- `certify_sixmax.cpp` is a copy of the old generator with `maxima>6` skipped instead of `maxima<=6`. It writes to the directory given on its command line.
- `independent_verify_sixmax.cpp` is a copy of the independently implemented old verifier with the complementary maxima selection and an expected total of 380,607.
- The old sources and old certificate files were not modified.

## Full counts

| Corner | Newly verified shapes with at most six maxima | Prior complementary duals | Total dual-covered shapes |
|---|---:|---:|---:|
| `(1,1,3)` | 127,801 | 580,816 | 708,617 |
| `(1,2,2)` | 126,406 | 850,024 | 976,430 |
| `(1,1,4)` | 47,309 | 523,791 | 571,100 |
| `(1,2,3)` | 33,383 | 486,333 | 519,716 |
| `(2,2,2)` | 28,338 | 505,232 | 533,570 |
| `(1,1,5)` | 6,246 | 144,235 | 150,481 |
| `(1,2,4)` | 4,276 | 96,065 | 100,341 |
| `(1,3,3)` | 3,579 | 87,117 | 90,696 |
| `(2,2,3)` | 3,269 | 87,821 | 91,090 |
| **Total** | **380,607** | **3,361,434** | **3,742,041** |

All nine complete coverage records and all multiplicity histograms agree between the producer and independent verifier. Their preselection counts also agree with the old complementary run. The supplementary assignment stream contains exactly 1,522,428 bytes: one little-endian unsigned 32-bit index for each of 380,607 shapes, with no trailing bytes. The independent verifier checked all 4,513 registry bases and all assignments. The generator used 15,342 LP proposals and 365,265 recent-basis hits. There were zero failed certificates. A zero exact margin is allowed: only the non-strict lower bound is claimed.

## Consequence for Wilf

If `W_4<0`, its integrality and the Apéry moment identity give

\[
3mH-4\sum_{x\in T}b\cdot x
\le \frac{m(m-2)}{m+1}
=m-3+\frac{3}{m+1}
\le m-\frac{90}{31}.
\]

Because `90/31−29/10=1/310>0`, this contradicts the certificate. Thus this branch satisfies `W_4≥0` without using the six-point theorem. The result is a simplification of a branch already claimed complete, not an extension to higher embedding dimensions and not a claim of external mathematical review.

## Reproduction

The single verification entry point needs Python standard library and a C++17 compiler, checks every file hash, compiles the separate verifier, and replays all records in an isolated temporary directory without regenerating or modifying certificates:

```sh
python3 round8/simplification/verify_certificate.py
```

The C++ verifier can also be run directly from the archive root:

```sh
c++ -O3 -std=c++17 round8/simplification/independent_verify_sixmax.cpp -o /tmp/wilf_verify_sixmax
/tmp/wilf_verify_sixmax round8/simplification
```

The verifier replays every supplementary shape and prints a final JSON record with `exact_weighted_duals: 380607` and `floating_point_used: false`. Its final check consumes the entire assignment stream. The recorded result is `independent_result.json`; the count-comparison summary is `complete_checks.json`. Source and certificate hashes appear in `certificate_manifest.json`.

The optional producer can regenerate these supplementary certificates, overwriting the certificate files in its supplied directory:

```sh
c++ -O3 -std=c++17 round8/simplification/certify_sixmax.cpp -o /tmp/wilf_certify_sixmax
/tmp/wilf_certify_sixmax round8/simplification
```
