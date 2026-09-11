# Independent audit: two explicit centroid constructions

Date: 2026-09-11.

## Scope and outcome

This audit concerns only the new centroid replacement for the finite degree-six residual class. It does not independently audit the rest of the proposed Wilf proof or establish that the four-generator conjecture is publicly accepted.

The two constructions are valid for every finite coordinatewise lower ideal in three variables with positive axis lengths. A fresh exhaustive replay then establishes that, on all **3,742,041** members of the already specified residual finite class, one of these constructions achieves the stronger bound

\[
3m\max_{x\in T}b\cdot x-4b\cdot\sum_{x\in T}x\ge m
\qquad(b_1,b_2,b_3\ge1).
\]

This removes all shape-specific LP bases and replaces them with two explicit formulas. It does **not** remove finite shape enumeration: the statement that one formula succeeds on every residual shape is still established by exhaustive exact arithmetic.

## 1. Coordinate-line construction

Put \(s=\sum_{x\in T}x\), \(m=|T|\). For every coordinate line \(\ell\) meeting \(T\), let \(L_\ell\) be its length and \(t_\ell\) its top point. If the line is parallel to coordinate \(i\), lower closure gives \(L_\ell=(t_\ell)_i+1\).

There are two elementary identities:

\[
\sum_\ell L_\ell=3m,
\qquad
\sum_\ell L_\ell t_\ell=4s.
\]

The first counts each point once in each coordinate direction. To verify the second in coordinate \(j\), the lines parallel to \(j\) contribute twice the sum of coordinate \(j\): \(L(L-1)=2\sum_{k=0}^{L-1}k\). Each of the other two families contributes that coordinate sum once.

For each line, choose a point \(u_\ell\in T\) dominating \(t_\ell\) and having maximal total degree among such points. Define

\[
U(T)=\sum_\ell L_\ell\bigl(|u_\ell|_1-|t_\ell|_1\bigr),
\qquad
z_L=\frac1{3m}\sum_\ell L_\ell u_\ell.
\]

The first identity makes \(z_L\) a convex combination of points of \(T\). The second gives

\[
r_L=3mz_L-4s
=\sum_\ell L_\ell(u_\ell-t_\ell)\ge0,
\qquad
|r_L|_1=U(T).
\]

For \(b_i\ge1\) and \(H=\max_T b\cdot x\),

\[
3mH-4b\cdot s\ge b\cdot r_L\ge U(T).
\]

This construction uses no weight vector and no linear program.

## 2. Axis-simplex construction

Let \(q_i=\max_T x_i>0\), let \(q=\max_iq_i\), and select \(j\) with \(q_j=q\). Each \(q_i e_i\) belongs to \(T\). Set

\[
G(T)=q\left(3m-4\sum_i\frac{s_i}{q_i}\right).
\]

If \(G>0\), put

\[
\lambda_i=\frac{4s_i}{3m q_i},
\qquad
\gamma=1-\sum_i\lambda_i>0,
\qquad
z_A=\sum_i\lambda_i q_i e_i+\gamma q_j e_j.
\]

The coefficients are nonnegative and sum to one. Direct subtraction yields

\[
3mz_A-4s=G e_j\ge0.
\]

Consequently \(3mH-4b\cdot s\ge G\) for all \(b_i\ge1\). If \(G\le0\), the same lower bound follows from the coordinate-line bound \(U\ge0\), so for every such lower ideal

\[
\boxed{3mH-4b\cdot s\ge\max\{U(T),G(T)\}.}
\]

No claim of nonnegative axis barycentric coefficients is made when \(G<0\).

## 3. A cheaper lower bound, and its measured limitation

If a line top is not globally maximal, it has a dominating point of degree at least one larger. A maximal point \(u\) is the top of exactly one line in each direction, whose total lengths are \(|u|_1+3\). Therefore

\[
U(T)\ge C(T):=3m-\sum_{u\in\operatorname{Max}(T)}(|u|_1+3).
\]

The replay checks this inequality on every residual shape as an additional implementation cross-check. However, using \(\max(C,G)\) instead of \(\max(U,G)\) leaves **79** shapes below the old threshold \(m-29/10\), and its worst deficit relative to \(m\) is \(-6\). Thus this cheap estimate cannot replace \(U\) throughout the class without another argument.

## 4. Independent exhaustive replay

The source `verify_two_centroids.cpp` starts from the separate round9 literal-height enumerator. It does not include any producer source/header or read LP bases or assignments. It constructs planar profiles by seven-element subsets of a fourteen-element set, converts these into row heights, and constructs three-dimensional shapes using scalar column heights. It uses neither the producer's recursive profile generator nor its three-dimensional bitset representation.

The nine sorted full-corner types are

\[
(1,1,3),(1,2,2),(1,1,4),(1,2,3),(2,2,2),
(1,1,5),(1,2,4),(1,3,3),(2,2,3).
\]

The original eligibility, degree, size, erosion, and surface filters are retained. Shapes with at most six maximal points are counted but are **not omitted** from this replay.

For every surviving shape, a scalar suffix recurrence computes

\[
B(x)=\max\{|u|_1:u\in T,\ u\ge x\}.
\]

The program then directly sums \((t_i+1)(B(t)-|t|_1)\) over all coordinate tops. For the axis bound, it uses the product denominator \(L=q_1q_2q_3\), rather than the producer's least common multiple, and compares the integer numerator against \(mL\). No floating-point arithmetic is used. All operands have magnitude far below the signed 64-bit range.

The final replay requires for **every** shape

\[
U\ge m\quad\text{or}\quad G\ge m.
\]

Results:

| Corner | Shapes | Minimum of \(\max(U,G)-m\) |
|---|---:|---:|
| \((1,1,3)\) | 708,617 | 0 |
| \((1,2,2)\) | 976,430 | 0 |
| \((1,1,4)\) | 571,100 | 1 |
| \((1,2,3)\) | 519,716 | 2 |
| \((2,2,2)\) | 533,570 | 4 |
| \((1,1,5)\) | 150,481 | 14 |
| \((1,2,4)\) | 100,341 | 22 |
| \((1,3,3)\) | 90,696 | 27 |
| \((2,2,3)\) | 91,090 | 33 |
| Total | **3,742,041** | **0** |

The line construction alone reaches \(m\) on **3,741,763** shapes. The axis construction reaches \(m\) on **2,090,810** shapes. Their union is the entire class; there are **278** shapes requiring the axis construction if the line construction is tried first.

For comparison with the earlier threshold: \(U\ge m-2\) succeeds on 3,741,920 shapes, leaving 121 axis fallbacks. Those 121 satisfy \(G-m\ge8\). These older 121 fallbacks must not be confused with the **278** fallbacks for the stronger threshold \(m\).

Every old filter count and every size histogram agrees exactly with the nine records in `round9/height_free_duals/independent_verification.jsonl`. The comparison includes profile compatibility counts, degree cut, size cut, erosion cut, surface cut, the six-maxima diagnostic, and final size histograms. This is a diagnostic cross-check; the new centroid inequalities are checked directly and do not depend on any old LP certificate.

The nine minimum witnesses are saved as explicit point clouds in `worst_witnesses.json`. Separate Python `Fraction` calculations recomputed their moments, axis intercepts, line values, and axis values. They also constructed explicit line barycenters and checked their coordinate surpluses.

## 5. Consequence for the residual semigroup class

Using the already established identity

\[
mW_4=A\left(3mH-4b\cdot s\right)-m(m-1),
\]

where \(A\ge m+1\) is the smallest nonmultiplicity generator, the new residual bound gives

\[
W_4\ge A-m+1\ge2.
\]

This consequence is conditional only on the earlier identification of the residual semigroup class with shapes surviving the stated filters and on the displayed standard moment identity. It does not replace the earlier arguments for other semigroup classes.

## 6. General-dimensional construction

Both explicit constructions extend to \(d\) coordinate variables. Across all coordinate lines,

\[
\sum L=dm,\qquad \sum Lt=(d+1)s.
\]

Thus the same upward line choice supplies a centroid witness for

\[
dm\max_T b\cdot x-(d+1)b\cdot s
\]

with nonnegative surplus of total size \(U_d\). The axis expression becomes

\[
G_d=q_{\max}\left(dm-(d+1)\sum_i\frac{s_i}{q_i}\right).
\]

Therefore the weighted expression is at least \(\max(U_d,G_d)\). What remains dimension-specific is proving a sufficiently strong lower bound for these explicit expressions on the relevant class of ideals.

## Reproduction

From the workspace or archive root, with C++17 available:

```sh
g++ -std=c++17 -O3 round10/independent/verify_two_centroids.cpp -o /tmp/wilf_two_centroids
/tmp/wilf_two_centroids round10/independent
```

The executable regenerates `coverage.jsonl`, `line_exceptions.jsonl`, and `successive_extrema.jsonl`, and prints its final status to standard output. Its exit status is nonzero on any failed shape. `comparison_result.json` and `worst_witnesses.json` record the independent record comparison and exact extremal calculations performed during this audit.

## Subsequent refinement: local two-step construction on a larger class

A later independent replay uses only successors at coordinate distance at most two. Let

\[
\ell_2(t)=\max\{|v|_1:v\in\mathbb N^3,\ |v|_1\le2,\ t+v\in T\},
\quad
U_2(T)=\sum_i\sum_{t\in F_i}(t_i+1)\ell_2(t).
\]

The same line construction proves \(D_T(b)\ge U_2(T)\), since the selected successor still dominates its line top. It requires only three one-step and six two-step membership possibilities. No search over maximal points is needed.

The broadest currently successful class drops the erosion condition and the refined bound on mixed plane corners above the full corner's projection. It retains the total mixed-plane-corner budget \(|p|-2\), the pair-surface bounds, the degree-six restriction, \(m\ge30\), and the nine full-corner types.

The symbolic agent's bitset producer and the separate literal-height implementation `round10/local_centroid/independent_two_step.cpp` agree on all nine records. I inspected both complete sources and their exact predicates, independently compared their completed result records, and found no gap. The scalar code checks the six two-step directions directly and requires \(U_2\ge m\) or \(G\ge m\) at every shape.

The expanded class contains **5,574,644** shapes. The two-step construction reaches \(m\) on **5,574,213**, the axis construction reaches \(m\) on **3,011,728**, and their union is the whole class. There are **431** axis fallbacks when the two-step construction is tried first. Per-corner minima of \(\max(U_2,G)-m\) are

`0, 0, 0, 2, 4, 10, 13, 21, 31`.

The exact source hashes, retained predicates, and matched counts are recorded in `final_local_class_audit.json`. This is the preferred local construction; the original full-upgrade replay above remains a separate reproducible historical check.

The portable historical replay can be invoked as:

```sh
python3 round10/independent/verify_complete_centroid.py
```

It requires only Python's standard library and a C++17 compiler. It verifies its source manifest, compiles in a temporary directory, performs all 3,742,041 historical shape checks, compares every filter and histogram record against a small locally included baseline, and recomputes the nine extremal witnesses with exact Python rational arithmetic. It reads no old LP registry, assignment stream, or old archive.
