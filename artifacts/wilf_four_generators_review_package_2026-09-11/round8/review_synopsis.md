# Four-generator Wilf: strengthened proof and fresh adversarial review

11 September 2026.

This continuation tests the proposed proof's mathematical foundations and
reduces one of its dependencies. It does not treat a saved PASS label as a
substitute for proving that a finite calculation covers the intended class.
The result remains a proposed computer-assisted research proof; external
mathematical review and proof-assistant formalization have not been performed.

## 1. A new simplification of the low-height proof

The previous argument handled 3,361,434 residual low-height shapes by exact
rational duals and sent 380,607 shapes with at most six maxima to a separate
six-final-window theorem. This continuation supplies and independently
checks the same rational inequality for **all 380,607 of those additional
shapes**. The two complementary streams now give

\[
3mH-4\sum_{x\in T}b\cdot x\ge m-\frac{29}{10}
\]

for all **3,742,041** shapes surviving the necessary arithmetic filters.
The inequalities hold for every real vector b with b_i>=1, every
H>=max_T b.x, and H<=7. The added stream contains 4,513 exact bases;
each of its 380,607 assignments was checked independently using integer
determinants and rational arithmetic. No floating-point acceptance is used.

This removes the six-final-window theorem from the residual low-height
branch. That theorem remains a dependency for the separate corner (1,1,1)
class. The revised proof does not silently discard that remaining dependency.

The new certificate and complete independent replay are in
`round8/simplification/`. The old and new maxima predicates are complementary,
so their union covers every surviving shape, with no new geometric assumption.

## 2. Exact conclusion and proof composition

The claim under review is:

**Theorem.** Every minimally four-generated numerical semigroup S, with
conductor c, satisfies

\[
4|S\cap[0,c)|\ge c.
\]

Here is the complete logical route. It makes every infinite-to-finite
reduction explicit and identifies the computational dependencies.

Write S=<m,a_1,a_2,a_3>, with m the smallest generator. Choose the
lexicographically least exponent vector for each Apéry element. These
vectors form a lower ideal T of cardinality m, containing the three unit
vectors, and their integer labels represent every residue modulo m once.
If a minimal excluded point and its residue representative shared a
positive coordinate, subtracting that coordinate would contradict this
injectivity. A full-support excluded point must therefore represent zero,
and there can be at most one such point.

Set A=min_i a_i>=m+1, b_i=a_i/A, M=max Ap(S,m), H=M/A, and

\[
D_0=3mH-4\sum_{x\in T}b\cdot x,
\qquad W_4=4|S\cap[0,c)|-c.
\]

The genus identity gives

\[
mW_4=A D_0-m(m-1).
\tag{1}
\]

The multiplicity-through-29 result excludes m<=29. Its new cases 20,...,29
use the analytic implication W_4<0 => M<=m(m-2), hence the same bound on
the nonmultiplicity generators. Exhaustion of this proved finite domain
therefore covers arbitrary generator sizes. The external small-multiplicity
input is the published work through multiplicity 19; the multiplicity-19
result and its predecessor through multiplicity 18 are stated in
[Kliem and Stump's paper](https://arxiv.org/html/1905.01945v2).

For m>=30, the completed no-interior and short-corner theorems give
D_0>=m-1 for their stated classes. The corner (1,1,1) has at most six maxima:
its zero residue forces each plane to have at most one mixed excluded
corner. The six-final-window theorem supplies Wilf for that class.
Every other positive full-support corner p has |p|_1>=5.

Suppose a remaining semigroup had W_4<0. Since W_4 is an integer, (1) gives

\[
D_0\le\frac{m(m-2)}{A}
\le m-3+\frac3{m+1},
\]

and therefore

\[
m-D_0\ge\frac{3m}{m+1}\ge\frac{90}{31}
>\frac{29}{10}.
\tag{2}
\]

The strict margin at m=30 is exactly 1/310.

If H<7, every point of T has total degree at most six, and every immediate
predecessor of p is included, so 5<=|p|_1<=7. Up to coordinate permutation,
there are nine positive corner types. Three planar projections determine
the ideal after removing p's upper orthant. The full enumeration includes
every compatible projection triple. The plane-corner, erosion, and surface
filters are necessary consequences of residue injectivity, proved in the
low-height audit. The combined 3,742,041 rational certificates now give
m-D_0<=29/10 directly throughout this branch, contradicting (2).

If H>=7, sort the weights as (1,b,c), and write S_w=1+b+c,
v=1/H, s=S_w/H, and kappa=D_0/(mH). The coordinate-line slack identity
gives kappa>=0, and (2) gives kappa<v. The phase lemma is

\[
s(1-3\kappa)\le4\kappa+5v-3\kappa v+4v^2.
\tag{3}
\]

It implies S_w<9+28/(H-3). The rectangular thickening of T preserves the
at-most-one-full-support-corner property. The continuous deficit theorem
and its exact thickening identity give

\[
\frac5{42}\le\frac{\kappa+s}{1+s},
\qquad 5H<42+37S_w.
\tag{4}
\]

Combining these necessary conditions yields 5H^2-390H+89<0, hence H<78.
Since the coordinate units belong to T, 1<=b<=c<=H. Every putative
failure therefore lies in the closed root box 1<=b,c<=78, 7<=H<=78.

The exact interval certificate covers that box. Each clip retains all
parameters satisfying the necessary failure conditions; upper endpoints
are rounded outward. Closed children cover each clipped parent. At every
accepted leaf, lower weights and the upper height enlarge the feasible
ideal class, while upper weights and the lower height enlarge the score
m-D_0. All positive corners with |p|_1>=5 are included because
p-e_1 in T implies b.p<=H+1. Removing p leaves a finite no-interior ideal,
covered by the central-box and nested-rectangle decomposition proved in
the structural audit. The exact dynamic program optimizes over all those
pieces after clipping, including every underfilled rectangular section.

Every accepted leaf bounds m-D_0 by 29/10. The complete tree has 47,229
splits, 47,088 accepted leaves, 142 empty leaves, and no unresolved nodes.
Thus this branch also contradicts (2). The alternatives H<7 and H>=7
are exhaustive, including H=7. Negative W_4 is impossible in the composed
argument. The conclusion is nonnegativity; a strict global inequality is
not asserted.

## 3. What the fresh mathematical audits challenge

The review was divided by mathematical dependency, with explicit
instructions to reconstruct proofs instead of inheriting earlier verdicts.

| Dependency | Independent mathematical question |
|---|---|
| Shape representation | Does every no-interior ideal admit the stated disjoint box-and-rectangular-section representation, including paths and degenerate axes? |
| Continuous and phase bounds | Do the translated-grid transfer, residue average, thickening correction, and inequality directions hold without a generic-weight assumption? |
| Arithmetic exclusions | Is every plane-corner, erosion, and surface rejection necessary for a genuine residue-bijective Apéry ideal? |
| Six-final-window theorem | Are compression, insertion, and extension exhaustive, and does the modular-cut certificate cover arbitrary integer lifts? |
| High-height computation | Does the implementation cover all corners and real boxes, use safe integer arithmetic, and match a direct shape enumeration on a separate small domain? |

The six-final-window audit also reconstructs the analytic conductor
reduction, including exclusion of the apparent six-column full-weighted
case. The structural audit gives a precise tree-median argument, rather
than assuming that a matching dynamic-program implementation establishes
the geometry.

The finite structural, phase, and genuine-semigroup probes in these audits
are falsification checks. Their bounded success does not replace the
corresponding analytic proofs. The uniform-gap theorem's finite strip at
degrees 18,19,20,21 remains an explicit proof dependency.

The completed source-difference audit in `round8/root_supplement_audit.json`
also checks that the new low-height sources change only the maxima
predicate and expected assignment count. Both certificate streams have
identical preselection counts for all nine corner types, and their
assignment counts sum to every surviving shape. This directly checks the
interface where the simplified proof combines them.

## 4. Reproduction and audit records

The full sources and saved exact records remain in the accompanying
archive. The fresh low-height replay is under `round8/lowheight_replay/`.
The extra 380,607 assignments and their independent verifier are under
`round8/simplification/`. The fresh high-height replay is under
`round8/high_height_replay/`; it uses copied sources and no saved leaf cache.

The fixed high-height certificate SHA-256 is
`173fe6ec196b3d2adabad313749482542ad3492b5f6b4e398e76bbe6e52e405c`.
Its accepted-leaf bound is at most 11,824 in scale 4096, strictly below
29*4096/10. Empty eligible-corner lists are treated as vacuous exclusions,
not as finite maxima over nonempty sets.

The fresh high-height run completed successfully in about 886 seconds.
Its report records **47,088 newly replayed leaves**, **35,852,138 Cartesian
corner cases**, and **zero cached checks**. It is a complete-tree run,
with neither sampling nor coverage-only mode. The fresh original
low-height replay checked all 3,361,434 assignments, and the supplementary
stream checked all 380,607 additional assignments. All requested replay
gates in this continuation have therefore completed.

The completion-and-provenance ledger is
`round8/final_review_completion.json`. Its checker,
`python3 round8/verify_review_completion.py`, validates the saved run
scopes, exact source/certificate hashes, and complete counts. That small
ledger check is expressly distinguished from rerunning the computations.

The final audit ledger records completed results and exact scope. A fresh
full run is distinguished from checking saved records. Compiler execution
and exact integer verification are computer-assisted evidence; no claim of
a proof-assistant-certified theorem is made.

## 5. Interpretation

This continuation found a substantive simplification of the proposed proof,
and the completed mathematical reviews have not identified a gap. All
requested fresh full replays also passed.
It does not constitute external peer review. The earlier phrase
"complete proof" describes the scope of the presented argument: all
four-generator cases are accounted for by named analytic and finite
components. It must not be read as a claim that outside specialists have
already accepted those components.

The work concerns embedding dimension four. It supplies neither a proof
for every higher embedding dimension nor a counterexample to the general
conjecture. Repeating confidence statements cannot establish either claim;
the reproducible argument is the material to assess.
