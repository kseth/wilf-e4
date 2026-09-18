# Fresh audit of the full short-interior-corner class

9 September 2026. Independent source review and exact replay of the interrupted 7 September checkpoint.

**Result: PASS for the short-corner argument.** Let
\(S=\langle m,a_1,a_2,a_3\rangle\) be minimally four-generated, and let its preferred Apéry lower ideal have the unique full-support minimal excluded point equal to a coordinate permutation of \((2,1,1)\). The reviewed argument proves \(W_4(S)\ge1\) for every \(m\ge30\). Combining it with a valid proof covering \(m\le29\) proves \(W_4(S)\ge0\) for the entire short-corner class. The multiplicity-at-most-29 theorem is an external dependency of this audit and is being audited separately in the same research continuation.

The primary proof below does **not** use the negative-case conductor bound or the arithmetic generator exhaustion at multiplicities 30–48. There is also an alternative proof through those computations. No unrestricted four-generator theorem follows: larger interior corners remain outside this result. These are internal research checks, not external mathematical peer review.

## 1. Exact statement and normalization

For a finite lower ideal \(T\subset\mathbb N^3\), put

\[
m=|T|,\qquad M=\max_{x\in T}a\cdot x,\qquad
D=3mM-4\sum_{x\in T}a\cdot x.
\]

The main geometric result is

\[
D\ge a_{\min}(m-1)
\tag{1}
\]

for every genuine short-corner preferred Apéry ideal with \(m\ge30\). There are two parts: a generic short-corner inequality when \(M\ge6a_{\min}\), and a finite exact geometric classification when \(M<6a_{\min}\), using necessary residue restrictions.

Normalize \(a_{\min}=1\) while proving (1). No argument below restricts weights to integers or rational numbers. All interval leaves certify complete closed boxes of real weights.

## 2. Analytic compactness, checked from its source proof

Orient the corner as \(p=(2,1,1)\), and write the coordinate weights as \((A,B,C)\) and \(S=A+B+C\). Partition \(T\) into the four disjoint pieces

1. \(y=0\);
2. \(y\ge1,z=0\);
3. \(x=0,y,z\ge1\);
4. \(x=1,y,z\ge1\).

Each is a translate of a planar lower ideal, and the translation weights are \(0,B,B+C,S\). The forbidden orthant above \(p\) ensures coverage. A planar lower ideal satisfies \(3\sum w\le2|F|\max w\): sum the weighted top of each coordinate line times its length in both directions. The two sums together equal exactly three times its first moment. Consequently each translated piece has mean at most \(2M/3+S/3\), and

\[
D/m\ge(M-4S)/3.
\tag{2}
\]

In particular \(M\ge3+4S\) proves \(D\ge m\).

The separate general line-deficit and sawtooth argument supplies, with \(v=1/M\), \(s=S/M\), \(\kappa=D/(mM)\),

\[
s(1-3\kappa)\le4\kappa+5v-3\kappa v+4v^2.
\tag{3}
\]

I read the sawtooth proof and the two-direction summation in `deliverables/wilf_fixed_dimension_finite_reduction_2026-09-05.md`, sections “Sharper discrete phase estimate” and “Summing the two phase inequalities.” Its needed hypotheses are precisely a finite lower ideal with all coordinate units and positive weights. In particular it requires neither a no-interior condition nor a residue labeling. The interval-integral estimate, line averaging identity, nonnegative deficits, and final algebra check correctly.

If \(D<m-1\) and \(M\ge6\), then \(0\le\kappa<v<1/3\). The right side of (3), divided by \(1-3\kappa\), is increasing in \(\kappa\), so

\[
S<9+\frac{28}{M-3}.
\]

Equation (2) gives \(M<3+4S\). Combining gives

\[
M^2-42M+5<0,
\]

hence \(M<42\). The improved bound \(M<36\) in the old compactness note is unnecessary here. Since the short corner is minimal excluded, all coordinate units belong to \(T\). Sorting weights into \((1,b,c)\) therefore places any failure with \(M\ge6\) in

\[
1\le b\le c\le M,\qquad 6\le M\le42,
\tag{4}
\]

with the corner in one of its three coordinate positions.

## 3. Structural coverage of the geometric dynamic program

Remove the full-support corner from the minimal-exclusion list to obtain a finite no-interior ideal \(U\). Pure-axis exclusions are retained, so \(U\) remains finite and shares the three axis extents of \(T\). Then exactly

\[
T=U\setminus(p+\mathbb N^3).
\]

The no-interior central-box/three-horn representation used by the dynamic program is justified by the chordal-graph proof in `round3/no_interior/clique_tree_and_bipartite_bound.md`. I checked its relevant steps: nested neighborhoods preclude an induced cycle of length at least four; maximal cliques correspond to maximal anchored boxes; the clique-tree running-intersection property makes all coordinate superlevel sets connected; each leaf has a distinct uniquely maximized coordinate; and the median of the three coordinate maxima gives at most three arms, with one coordinate increasing and the other two decreasing. Therefore each arm has nested rectangular slices. This proves that the dynamic program contains every relevant ideal.

Clipping the center and each slice by \(p+\mathbb N^3\) preserves disjointness. The auxiliary program is allowed to include shapes whose clipping destroys minimality of \(p\); this safely enlarges the class. Axis extent caps are valid because axes are unaffected by the clipping.

For a real-parameter box, lower weights and upper height enlarge feasibility; upper weights and lower height increase every additive point score \(4a\cdot x-3M+1\). Thus the computed maximum is an upper bound for \(m-D\) throughout the complete box. Horn recurrence states allow every smaller next rectangle, and the empty continuation, so maximization does not lose a shape.

The independently reviewed worker integrates each clipped rectangle or box as three disjoint subboxes, classified by the first coordinate below the corner. Its cardinality, doubled first moment, and maximal lower-weight value follow by direct box integration. This is independent of the generator's subtraction formulas for the removed orthant.

**Correction to an old description:** `independent_clipped_worker.cpp` uses a prefix-maximum implementation of the nested-rectangle recurrence. It does not enumerate all rectangle transitions explicitly. Independence comes from the separate code and disjoint-box integral, and the recurrence was checked mathematically. The new report does not repeat the inaccurate “explicit rectangle transitions” characterization.

Integer safety was checked for the actual certificate domain: each axis extent is at most 42, all scaled weights are at most \(42\cdot4096\), and every ideal is contained in a \(43^3\)-point box. Even a deliberately loose bound for intermediate first-moment expressions is below \(10^{13}\), far below signed 64-bit capacity. Counts and scores use signed 64-bit arithmetic; index ranges fit ordinary integers.

## 4. Complete fresh interval replay

The round6 verifier is a copy of the historical independent verifier with only its source lookup and output destination adjusted. It reads the original immutable certificate and recompiles the independently reviewed C++ source in a temporary directory.

Fresh results:

| Item | Result |
|---|---:|
| Tree nodes reached and checked exactly once | 110,865 |
| Split nodes | 55,432 |
| Exact DP leaves | 54,978 |
| Planar-bound leaves | 455 |
| Corner/leaf bounds recomputed | 164,934 |
| Common denominator | 4,096 |
| Largest recomputed upper bound | 4,096 |
| Unresolved regions | 0 |

The root box is \([1,42]\times[1,42]\times[6,42]\). Ordering propagation removes only points outside \(b\le c\le M\). Each split is checked against its two complete closed children, including their common boundary. Every leaf is either checked with the exact dynamic program for all three corner placements or with the analytic inequality (2). All recorded bounds matched fresh calculations.

Canonical certificate SHA-256:

`c840c66eae5ade228ef500567e2bd1daa7533be89276cd6a73906abf3dfea1ac`

This establishes (1) for every generic short-corner ideal of normalized height at least 6.

Files from this fresh run:

- `round6/short_corner_audit/verify_complete_short_corner.py`
- `round6/short_corner_audit/complete_short_corner_audit_results.json`

## 5. Low-height arithmetic restrictions and fresh rational-dual replay

A preferred Apéry ideal is residue-bijective. The representative of a minimal excluded point has disjoint support, by subtracting a shared coordinate and using injectivity. Distinct excluded corners sharing a coordinate have different residues, by the same predecessor argument. Thus the full corner has representative zero:

\[
2A+B+C\equiv0\pmod m.
\]

For a mixed xy corner \((u,v,0)\) with representative \(\gamma e_z\), if \(u\ge2\), then \((u-2,v-1,0)\in T\) has residue \((\gamma+1)C\). This forces \(\gamma\) to be the final included z-axis exponent. Hence at most one xy corner has \(u\ge2\); at most one further xy corner has \(u=1\), because different planar minimal corners have distinct first coordinates. The xz statement is identical. For a yz corner, subtracting \((0,1,1)\) gives residue \((\gamma+2)A\), forcing its representative to one of the last two x-axis exponents. Hence the yz plane has at most two mixed corners. Minimality of \(p\) also requires its three planar predecessors to be present.

If \(M<6\) and all weights are at least 1, then \(T\subset\Delta_5\). The independently reviewed coverage checker enumerates every nonincreasing planar row profile inside \(\Delta_5\), retaining exactly the preceding necessary corner restrictions and matching axis extents. Three pairwise profiles together with deletion of \(p+\mathbb N^3\) determine \(T\). Enumeration tests the actual total degree of all retained points and thus covers every eligible shape. Coordinate permutations reduce to the displayed orientation without ordering the weights.

For every enumerated shape of size at least 30, the certificate supplies nonnegative rational multipliers \(y_x\) and \(\beta_i\) with

\[
\sum_x y_x=3m,\qquad
\sum_x y_x x_i=4\sum_{x\in T}x_i+\beta_i,
\qquad \sum_i\beta_i\ge m-1.
\]

Since \(M\ge a\cdot x\) at every certified point,

\[
3mM\ge\sum_x y_x a\cdot x
=4\sum_{x\in T}a\cdot x+\sum_i a_i\beta_i
\ge4\sum_{x\in T}a\cdot x+(m-1).
\]

This proves the required weighted inequality for every real \(a_i\ge1\). The checker verifies all these identities with Python `Fraction`, point membership, nonnegativity, exact profile coverage, and exhaustion of the certificate dictionary.

The fresh run passed:

| Item | Result |
|---|---:|
| Eligible degree-at-most-5 shapes | 70,175 |
| Shapes of cardinality at least 30 | 28,499 |
| Exact rational duals replayed | 28,499 |
| Largest cardinality in this restricted geometry | 43 |
| Least certified margin over \(m-1\) | 19 |

The independent degree-at-most-4 crosscheck also found 3,928 shapes and maximum cardinality 29. Its role here is diagnostic: the degree-5 certificate already covers the complete low-height case.

Fresh output: `round6/short_corner_audit/low_height_independent_replay.json`.

## 6. Complete composition for multiplicity at least 30

For a genuine short-corner Apéry ideal with \(m\ge30\), normalized height either is at least 6, covered by Sections 2–4, or is below 6, covered by Section 5. Thus the unnormalized inequality is (1). Minimal generation gives \(a_{\min}\ge m+1\), and the exact Apéry identity gives

\[
mW_4=D-m(m-1)
\ge(a_{\min}-m)(m-1)\ge m-1>0.
\]

Since \(W_4\) is an integer, \(W_4\ge1\). This finishes the asserted tail of the full short-corner class. A valid theorem for all \(m\le29\) completes its remaining multiplicities.

## 7. Elementary cardinality bound and alternative arithmetic route

The generic statement \(T\subset\Delta_5\Rightarrow |T|\le48\) was independently checked and needs no computation. Of 56 points in \(\Delta_5\), the orthant above \((2,1,1)\) removes four. For \(j=1,2,3,4\), the missing degree-6 point \((1,j,5-j)\) does not dominate the full corner, so at least one of its three coordinate-plane projections must be absent. The four projection triples are disjoint, lie inside \(\Delta_5\), and are disjoint from the four removed orthant points. At least eight points are absent, proving the bound.

Thus \(m\ge49\) automatically gives \(M\ge6a_{\min}\), allowing the high-height theorem alone to handle that entire range. For multiplicities 30–48, a full corner implies at least one of

\[
2a_1+a_2+a_3\equiv0,\quad
a_1+2a_2+a_3\equiv0,\quad
a_1+a_2+2a_3\equiv0\pmod m.
\]

The two historical complete programs enumerate this larger congruence union in the necessary negative-case generator box. I reviewed their residue solver, direct-residue alternative, complete sorted-tuple iteration, minimality pruning, gcd test, cyclic distance update, and independent ordinary-integer-membership calculation. The smallest generator cannot become redundant using a later larger generator, so prefix minimality pruning is sound. Two traversals of each directed residue cycle propagate every source for up to one full cycle, which suffices for a shortest path with positive edge cost. Ordinary membership of the last m integers through B is equivalent to \(\max\operatorname{Ap}\le B\), validating the second algorithm's filter. Bit shifts have widths at most 48 and their accessible blocks are allocated.

A fresh full recompilation and rerun of both programs is recorded separately in `round6/short_corner_audit/p211_exhaustion_replay.json`. That alternative arithmetic route also requires the independently proved implication \(W_4<0\Rightarrow \max\operatorname{Ap}\le m(m-2)\). It is not a dependency of the stronger low-height-dual proof in Sections 1–6.

## Reproduction

From the project root:

```sh
python3 round6/short_corner_audit/verify_complete_short_corner.py
python3 round5/interior_arithmetic/verify_low_height_weighted.py
python3 round5/short_corner_small_m/verify_p211_exhaustion.py --rerun
```

The first two commands are the complete computational dependencies specific to the short-corner proof for \(m\ge30\). The third reproduces the alternative arithmetic route. The Python verification uses only the standard library; interval and arithmetic replay require a C++17 compiler. Historical source files and certificates were not modified by this audit.
