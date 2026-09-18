# Simplifying the four-generator certificate argument

11 September 2026. This note distinguishes an actual lossless compression of existing certificates from proposed replacements for exhaustive coverage. It does not supply a new noncomputational proof or resolve higher embedding dimensions.

## A concrete compression already available

I read both completed low-height assignment streams and their exact basis registries. The original stream has 3,361,434 assignments and 5,733 bases; its complementary stream has 380,607 assignments and 4,513 bases. All registered bases occur at least once.

| Representation | Distinct basis types |
|---|---:|
| Two separate registries | 10,246 |
| Combined, removing identical column sets | 6,662 |
| Combined, also identifying coordinate permutations | 2,589 |

A type in the last row is a four-column rational dual template together with a coordinate permutation. Replacing both registries by this common registry, with an orientation attached to each assignment, loses no mathematical information. This reduces repetition, but it still requires a coverage argument for the shapes.

The distribution of recorded assignments is concentrated: 54 symmetry types account for at least 50%, 515 for at least 90%, 797 for at least 95%, and 1,456 for at least 99%. These are *recorded-assignment* statistics, not assertions that fewer types cannot prove additional shapes. A basis chosen by the generator need not be the only basis that works.

More structurally, 3,632,415 of the 3,742,041 assigned proofs (97.07%) use no upper bound on H. Only 109,626 assigned proofs use H <= 7. None uses the redundant lower bound H >= 0. The bases use only 72 different lattice-point constraints. Their precise distribution is:

| Point constraints | Weight lower bounds | Uses H <= 7 | Assignments |
|---:|---:|:---:|---:|
| 3 | 1 | No | 2,946,058 |
| 2 | 2 | No | 654,873 |
| 2 | 1 | Yes | 93,155 |
| 1 | 3 | No | 31,484 |
| 1 | 2 | Yes | 16,471 |

These facts suggest a geometric witness theorem, rather than a search over millions of individual ideals.

## The low-height certificates have a clean convex-hull interpretation

Write m=|T| and s=sum_{x in T}x, and set delta=29/10. Suppose there is a point y in conv(T) with

    3m y_i >= 4s_i for i=1,2,3,
    3m (y_1+y_2+y_3) - 4(s_1+s_2+s_3) >= m-delta.

Then, for every b_i>=1 and every H>=max_{x in T} b.x,

    3mH - 4 b.s >= b.(3my-4s) >= m-delta.

This is a direct proof: H>=b.y follows by convexity, and the second inequality follows coordinate by coordinate. It uses no height cutoff. Equivalently, the convex hull of T meets a specific translated positive orthant at sufficient coordinate sum.

Every recorded certificate that omits H<=7 is exactly a witness of this form: its nonnegative point multipliers sum to 3m, and its weight-bound multipliers are 3my-4s. At most three lattice points are used in the existing certificates. Therefore a fruitful analytic target is a *centroid domination lemma* for genuine preferred Apéry ideals satisfying the arithmetic corner and surface restrictions. That lemma is currently a target, not established here.

There is already a particularly simple family. If T contains (r1,0,0), (0,r2,0), and (0,0,r3), then it is enough to prove

    r1(3m - 4s2/r2 - 4s3/r3) - 4s1 >= m-delta.

The point multipliers are 3m-4s2/r2-4s3/r3, 4s2/r2, and 4s3/r3; the displayed inequality ensures their nonnegativity when m>=30. The remaining multiplier is on b1>=1. The single template (r1,r2,r3)=(6,5,5), including coordinate permutations, accounts for 191,314 recorded assignments. Thus a recognizable axis-intercept inequality already explains a substantial portion of the computational proof.

A caution: these identities certify each fixed ideal. Turning them into a short theorem requires proving that one suitable witness always exists from the structural and arithmetic hypotheses. The registry statistics do not establish that universal assertion.

## A precise way to replace the high-height search

The high-height computation maximizes the additive score

    f(x)=4 b.x + 1 - 3H

over a box with three horns, after removing one upper orthant. For a horn along coordinate i, let C_i(t,r,s) denote its retained section at coordinate t with transverse rectangle [0,r] times [0,s], and write g_i(t,r,s)=sum_{x in C_i(t,r,s)} f(x). These section scores are explicit polynomials, separately on either side of the corner cut.

A closed-form majorant V_i(t,r,s) would replace every state in the dynamic program if it satisfied:

1. V_i>=0, including a zero terminal condition beyond the feasible axis range.
2. V_i(t,r,s)>=V_i(t,r-1,s) and V_i(t,r,s)>=V_i(t,r,s-1) whenever the smaller section exists.
3. V_i(t,r,s)>=g_i(t,r,s)+V_i(t+1,r,s) whenever that retained section fits below H.
4. For every allowed central box with endpoints (a,b,c), its retained score plus V_1(a+1,b,c)+V_2(b+1,a,c)+V_3(c+1,a,b) is at most 29/10.

Backward induction proves that each V dominates the true horn optimum. Summing the central score and the three horn majorants proves m-D<=29/10. A piecewise polynomial formula for V with a number of pieces independent of H would be a substantial analytic simplification. Defining V to be the dynamic program itself merely renames the original computation and does not meet that goal.

For example, before clipping, the section score is

    (r+1)(s+1)[4 b_i t + 2 b_j r + 2 b_k s + 1 - 3H].

If t>=p_i, r>=p_j, and s>=p_k, subtract

    (r-p_j+1)(s-p_k+1)
    [4 b_i t + 2 b_j(r+p_j) + 2 b_k(s+p_k) + 1 - 3H].

Thus the local inequalities needed for a polynomial majorant are explicit. The difficulty is allowing the optimal transverse rectangle to change and shrink repeatedly as t advances; a proof assuming all horn sections are maximally filled omits allowed ideals. Matching the three horns against the negative central contribution is also essential: separately summing positive section scores is generally much weaker.

## A known obstruction that the simplification must respect

The abstract one-corner lower ideal in `round7/erosion_fixture.md` has p=(1,2,2), unit weights, m=48, H=5, and sum |x|=170. Thus D=3mH-4 sum |x|=40 and m-D=8. It refutes the unrestricted geometric assertion m-D<=29/10 at low heights.

It does not refute Wilf. Its planar mixed corner counts (5,4,4) exceed the allowed bound |p|-2=3, and its erosion expansion has 55 points while T has only 48. Therefore no additive residue-bijective labeling exists. Any analytic replacement that tries to cover all abstract one-corner ideals at all heights must fail; a valid replacement must retain arithmetic information or restrict the height range.

## Reproducibility and limits

`analyze_dual_compression.py` reads the complete original and supplementary binary assignment streams; it computes exact column-set equality, all six coordinate permutations, frequency counts, and the column-category distribution. Its results are `dual_compression_statistics.json`. This is a lossless analysis of existing proofs, not an additional certification of their coverage.

A separate test in `test_common_duals.py` retests the 100 most frequent symmetry types, in every orientation, against the already-existing diagnostic sample `round7/low_degree6/weighted_candidates_sample.tsv`, retaining its shapes that satisfy the pairwise surface restrictions. All determinant, multiplier, membership, and lower-bound tests are integer computations. Its output, when complete, is `common_dual_sample_results.json`. This sample is neither exhaustive nor a randomized holdout; no universal conclusion may be drawn from its coverage rate.

## A completed simplification obtained during this analysis

The originally proposed height-free centroid target has now been established for the *entire existing finite low-degree survivor class*. Removing H<=7 from the generator's LP and including both former maxima selections produced exact witnesses for all 3,742,041 ideals. A full independent replay passed, enforcing that no height-upper-bound column appears. The combined registry has 6,816 bases (2,723 symmetry types). The theorem and portable verification entry point are in `round9/height_free_duals/`.

Thus the residual proof may split by degree, rather than normalized weight-dependent height: degree<=6 uses the new centroid-witness theorem, and degree>=7 automatically has H>=7, so uses the existing high-height theorem. This simplifies dependencies and removes the duplicated original/supplementary low-height argument; it does not remove the finite shape enumeration. The physical archive of historical certificates need not be rewritten to state this replacement.

The common-basis sample test also completed. On 34,807 complete eligible rows from the previously existing diagnostic file, the top one, five, ten, twenty, fifty, and one hundred symmetry types certified respectively 11,156; 24,606; 28,510; 30,217; 33,022; and 34,084 shapes. Thus 100 types suffice for 97.92% of this diagnostic sample, including orientations. One incomplete trailing input row was excluded explicitly. These are exact certificate checks, but the sample itself does not constitute a universal proof.
