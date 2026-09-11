# Completion of the normalized-height-below-seven class

10 September 2026.

**Status:** completed and independently replayed in full. The separate implementation checked all 3,361,434 dual assignments, every point-constraint membership, all 5,733 basis matrices by Bareiss/Cramer arithmetic, and every coverage count and histogram. It generates planar partitions independently and constructs three-dimensional ideals as explicit height arrays, without importing the producer headers or bitset operations.

## 1. Mathematical conclusion

Let `S=<m,a_1,a_2,a_3>` be minimally four-generated, let `A=min(a_1,a_2,a_3)`, and write

\[
M_{\rm actual}=\max\operatorname{Ap}(S,m),\qquad H=M_{\rm actual}/A.
\]

Combining this certificate with the already established multiplicity-through-29, no-interior, `(1,1,1)`, and `(2,1,1)` results gives

\[
\boxed{H<7\ \Longrightarrow\ W_4(S)\ge0.}
\]

This statement does not depend on an unproved assertion about the remaining high-height class. The complete independent replay described below has passed. It does not assert Wilf at `H≥7`.

The exact new subcase proved here is: `m≥30`, one full corner with coordinate sum between five and seven, normalized height below seven. This subcase includes every permutation of the nine corners

\[
(1,1,3),(1,2,2),(1,1,4),(1,2,3),(2,2,2),
(1,1,5),(1,2,4),(1,3,3),(2,2,3).
\]

The weights are arbitrary positive real weights after normalization; they are not restricted to a grid.

## 2. Why these finite shapes cover every genuine case

Choose the preferred Apéry lower ideal `T⊂N³`, so `|T|=m` and its labels give all residues modulo `m` exactly once. Put `b_i=a_i/A≥1`. If `H<7`, then every `x∈T` satisfies

\[
|x|_1\le b\cdot x\le H<7.
\]

Thus `T⊂Δ_6={x∈N³:|x|_1≤6}`. If `p` is a full-support minimal excluded point, every predecessor `p−e_i` belongs to `T`, and therefore `|p|_1≤7`. The already completed corners `(1,1,1)` and permutations of `(2,1,1)` leave exactly the nine displayed sorted possibilities. A coordinate permutation simply permutes the three real weights, so treating the sorted corners loses no case.

Let `U` be the intersection of the three cylinders over the coordinate-plane projections of `T`. Since the only possible minimal excluded point with three positive coordinates is `p`,

\[
T=U\setminus(p+\mathbb N^3).
\]

Every coordinate-plane projection is a planar lower ideal in `Δ_6`. It is encoded by its seven row lengths `r_0,...,r_6`, satisfying

\[
0\le r_i\le7-i,\qquad r_{i+1}\le r_i.
\]

There are 1,429 nonempty such profiles. The empty profile cannot occur here. The three profiles must agree on their common coordinate axes. They also contain the corresponding two-coordinate projections of `p`, because those projections are proper divisors of `p`.

### The plane-corner restrictions

Let `p=(r,s,t)` and let `q=(u,v,0)` be a mixed minimal excluded point in the `xy` plane. Its representative in `T` lies on the `z` axis, say `γe_z`: a positive `x` or `y` coordinate of its representative would give a pair of distinct equal-residue predecessors inside `T`. Distinct such plane corners have distinct representatives, by the same predecessor argument.

When `u≥r` and `v≥s`, the included point `q−(r,s,0)` has the same residue as `(γ+t)e_z`, because `p` represents zero. This included point is nonzero and has zero `z` coordinate; the case `q=(r,s,0)` is impossible because the projection of `p` is included. If the `z`-axis has length `n_z`, injectivity therefore forces `γ+t≥n_z`. There are at most `t` possible values of `γ` in this terminal portion of the axis.

Hence at most `t` mixed `xy` corners dominate `(r,s)`. Every other mixed corner has either first coordinate below `r` or second coordinate below `s`. Distinct corners have distinct first coordinates and distinct second coordinates, so there are at most `(r−1)+(s−1)` additional corners. Consequently every plane has at most `|p|_1−2` mixed corners, and the number dominating its projection of `p` is at most the opposite coordinate of `p`. These are exactly the restrictions used by the enumeration.

### The arithmetic filters

For `B={0,e_1,e_2,e_3}`, let

\[
E=T\ominus B=\{x:x+B\subseteq T\}.
\]

If `E+B⊂T`, the residue map is injective on `E−B`: equal residues of `x-b` and `x'-b'` imply equal residues of the two points `x+b'` and `x'+b` in `T`, hence equality of the integer differences. Since `E` is lower,

\[
|E-B|=|E|+\sum_{i=1}^3|E\cap\{x_i=0\}|.
\]

Thus a necessary condition is

\[
|E|+\sum_i|E\cap\{x_i=0\}|\le m. \tag{1}
\]

Next set `F_i={x∈T:x+e_i∉T}` and `n_i=1+max_T x_i`. The directly proved residue inequality in `../global_step_audit.md` gives, for each distinct `i,j,k`,

\[
|F_i\cap F_j|\le2n_k. \tag{2}
\]

Both (1) and (2) are necessary for genuine Apéry ideals and are used solely to reject impossible shapes.

Finally, the already proved six-final-window theorem settles a shape with at most six coordinatewise maximal points: every final-window Apéry point is coordinatewise maximal, because adding any nonmultiplicity generator, which exceeds `m`, would exceed the maximum Apéry value. This shortcut leaves precisely the shapes receiving the weighted certificates.

## 3. Exact weighted certificates

For each remaining shape, put `s_i=Σ_{x∈T}x_i`. We certify, simultaneously for all `b_i≥1` and all `H≤7` with `H≥b·x` for every `x∈T`,

\[
\boxed{3mH-4\sum_i s_i b_i\ge m-\frac{29}{10}.} \tag{3}
\]

A certificate consists of nonnegative rational coefficients `y_x`, `β_i`, `δ`, and `γ`, only four of which need be nonzero, satisfying

\[
\beta_i-\sum_x y_xx_i=-4s_i,
\qquad
\sum_x y_x+\delta-\gamma=3m,
\]

and

\[
\sum_i\beta_i-7\gamma\ge m-\frac{29}{10}.
\]

Indeed, the objective equals

\[
\sum_x y_x(H-b\cdot x)
+\sum_i\beta_i b_i+\delta H+\gamma(7-H)-7\gamma,
\]

which is bounded below by the claimed constant. All points carrying `y_x` belong to the current `T`. The other inequalities are `b_i≥1`, `H≥0`, and `H≤7`.

The four nonzero coefficient positions are supplied by a floating-point linear program, or recycled from a previously successful shape. Their values are then recovered and checked **exactly**, using integer determinants and adjugates of a four-by-four matrix. A floating-point objective value is never sufficient for acceptance. Reused point constraints are checked for membership in the current shape before reuse.

The matrix columns are integer vectors:

- Point `(x,y,z)`: `(-x,-y,-z,1)`.
- Lower bound on `b_i`: the corresponding coordinate unit vector.
- Lower bound on `H`: `(0,0,0,1)`.
- Upper bound `H≤7`: `(0,0,0,−1)`.

Their nonnegative combination must equal `(-4s_1,-4s_2,-4s_3,3m)`. The exact computation checks nonnegativity, all four coefficient identities, and the final lower bound separately.

### Why the weaker constant suffices for Wilf

Suppose `W_4<0`. Integrality and the exact Apéry moment identity yield

\[
D_{\rm actual}=mW_4+m(m-1)\le m(m-2).
\]

Since `A≥m+1`, the normalized moment satisfies

\[
\frac{D_{\rm actual}}A
\le\frac{m(m-2)}{m+1}
=m-3+\frac3{m+1}.
\]

For `m≥30`, the right side is at most `m−90/31`, strictly smaller than `m−29/10`. This contradicts (3), applied with `H=M_actual/A`. Therefore `W_4≥0`. This argument excludes negative Wilf numbers; it does not assert strict positivity from the weaker bound alone.

## 4. Complete coverage counts

| Corner | Axis-compatible triples | Degree at most six | `m≥30` | Pass (1) | Pass (2) | At most six maxima | Weighted certificates |
|---|---:|---:|---:|---:|---:|---:|---:|
| `(1,1,3)` | 4,112,203 | 2,680,955 | 2,634,873 | 2,165,275 | 708,617 | 127,801 | 580,816 |
| `(1,2,2)` | 5,796,538 | 3,659,949 | 3,633,042 | 2,987,253 | 976,430 | 126,406 | 850,024 |
| `(1,1,4)` | 5,862,929 | 2,395,217 | 2,388,434 | 1,700,471 | 571,100 | 47,309 | 523,791 |
| `(1,2,3)` | 8,772,820 | 2,999,148 | 2,998,420 | 1,941,231 | 519,716 | 33,383 | 486,333 |
| `(2,2,2)` | 13,325,338 | 3,879,064 | 3,879,014 | 2,306,872 | 533,570 | 28,338 | 505,232 |
| `(1,1,5)` | 2,252,380 | 551,334 | 550,982 | 411,216 | 150,481 | 6,246 | 144,235 |
| `(1,2,4)` | 3,589,363 | 515,956 | 515,955 | 351,528 | 100,341 | 4,276 | 96,065 |
| `(1,3,3)` | 4,014,473 | 510,514 | 510,514 | 331,194 | 90,696 | 3,579 | 87,117 |
| `(2,2,3)` | 7,473,254 | 615,876 | 615,876 | 380,481 | 91,090 | 3,269 | 87,821 |
| **Total** | **55,199,298** | **17,808,013** | **17,727,110** | **12,575,521** | **3,742,041** | **380,607** | **3,361,434** |

Every weighted certificate passed. The computation needed 44,623 linear-program proposals and reused previously checked bases for 3,316,811 shapes. The registry contains 5,733 distinct bases. These proposal counts are performance diagnostics; completeness is established by the enumerated shape counts and one exact certificate for each surviving shape.

Ordinary erosion alone was insufficient even at unit weights: two symmetric `(1,2,2)` shapes have `m=30`, degree four, and `D=20`. They pass (1), with erosion value 29, but have one `|F_i∩F_j|=11` against `2n_k=10`, and are rejected by (2). Thus the newly proved surface restriction makes a concrete difference to the finite proof.

## 5. Reproduction and certificate format

The essential files are:

- `certify_all.cpp`, `proposing_lp.hpp`, `exact_dual.hpp`: generator, proposal routine, and exact acceptance routine.
- `dual_bases.jsonl`: indexed lists of four integer constraint-column IDs.
- `dual_assignments.bin`: one little-endian unsigned 32-bit basis index for every surviving shape, in deterministic enumeration order. There are exactly 3,361,434 records, or 13,445,736 bytes.
- `certification.jsonl`: all nine coverage records.
- `independent_verify.cpp` and `independent_verification.jsonl`: the separate complete verifier and all nine result records. See the independent audit note for its exact invocation and scope.

Point `(x,y,z)` has ID `49x+7y+z`, between 0 and 342. IDs 343, 344, 345 represent the three lower weight bounds; 346 is `H≥0`; 347 is `H≤7`.

Profiles are enumerated by ascending choices of their row lengths, recursively from row zero through row six. Corner order is the displayed nine-corner order. The triple order is first `xy`, then `xz` with matching `x` axis, then the eligible `yz` profiles with matching `y,z` axes in their original profile order. Only shapes passing all restrictions and having more than six maxima consume an assignment record. The independent verifier must check both complete stream consumption and absence of trailing records.

Compile the generator with a C++17 compiler, for example:

```sh
g++ -std=c++17 -O3 round7/low_degree6/certify_all.cpp -o /tmp/wilf_low_degree6
/tmp/wilf_low_degree6 round7/low_degree6
```

Generation overwrites the three named certificate outputs. Certificate verification requires no optimization software and should be run separately without regenerating them.

The first-pass files `survivors.tsv` and `weighted_candidates_sample.tsv` are disposable diagnostics and are not proof dependencies. A diagnostic sample file contained a truncated row; its optional Python sampling run stopped on that parse error. The complete certificate run uses neither sample file. Its full assignment length and every proof record have now been checked independently.
