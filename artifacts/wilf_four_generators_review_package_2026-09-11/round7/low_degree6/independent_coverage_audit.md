# Independent complete audit of the degree-six weighted certificate

10 September 2026.

## Verdict and scope

The independent replay passed **all 3,361,434 exact weighted dual
certificates**, reconstructing every shape to which they are assigned.
Its coverage counts and complete multiplicity histograms agree exactly
with the producer for each of the nine interior corners.

The certificate proves the following statement. Suppose a finite lower
ideal \(T\subset\mathbb N^3\) has degree at most six, \(m=|T|\ge30\), a
unique full-support minimal excluded point of coordinate sum at least
five, more than six maximal points, and satisfies the necessary arithmetic
plane-corner, erosion, and surface restrictions below. Then

\[
3mM-4\sum_{x\in T}a\cdot x\ge m-\frac{29}{10}
\tag{1}
\]

for every \(a_1,a_2,a_3\ge1\) and every \(0\le M\le7\) satisfying
\(M\ge a\cdot x\) for all \(x\in T\).

**The upper height bound \(M\le7\) is essential to the stated certificate.**
Column 347 explicitly uses \(-M\ge-7\). The certificate makes no claim for
arbitrary larger heights.

For genuine Apéry ideals, (1) implies Wilf by the integer-slack argument
in Section 6. Omitted shapes are accounted for by named necessary
conditions or separately proved subclass theorems. This audit does not
independently reprove those prior six-point, small-multiplicity,
no-interior, or \((2,1,1)\) theorems.

## 1. Complete independent planar enumeration

A nonempty planar lower ideal of degree at most six has seven row lengths
\(h_0,\ldots,h_6\), with

\[
0\le h_i\le7-i,\qquad h_i\ge h_{i+1}.
\]

The producer generates these rows recursively. The independent verifier
instead traverses every seven-element subset of \(\{0,\ldots,13\}\).
Writing its elements in decreasing order \(t_0>\cdots>t_6\), it sets

\[
h_i=t_i-6+i.
\]

These are exactly all nonincreasing partitions in a \(7\times7\) box:
the order-statistic bounds give \(0\le h_i\le7\), successive differences
give monotonicity, and \(t_i=h_i+6-i\) is the inverse map. The restriction
\(h_i\le7-i\) then imposes the degree-six triangle. Removing the all-zero
profile leaves exactly 1,429 profiles.

Lexicographic sorting of the rows agrees with the producer's ascending
recursive ordering. This aligns the binary assignments; each assigned
dual is nevertheless checked against its current reconstructed shape.
The three profiles are combined in xy, xz, yz order, requiring equality
of each shared axis length. This ensures their pairwise intersection has
precisely the specified plane projections.

For \(M<7\), normalized weights \(a_i\ge1\) give
\(|x|_1\le a\cdot x\le M<7\), hence integer degree at most six. Thus the
enumeration covers every genuine ideal in the required low-height range.
The duals additionally allow the closed endpoint \(M=7\).

## 2. Corner range and arithmetic projection restrictions

For a full-support minimal excluded point \(p\), all predecessors
\(p-e_i\) belong to \(T\), so \(|p|_1\le7\). The previously settled
corners are \((1,1,1)\) and permutations of \((2,1,1)\). The independent
verifier generates all sorted positive triples with \(5\le|p|_1\le7\):

\[
(1,1,3),(1,2,2),(1,1,4),(1,2,3),(2,2,2),
(1,1,5),(1,2,4),(1,3,3),(2,2,3).
\]

Coordinate sorting is harmless because the allowed weights are arbitrary
and are permuted with the coordinates.

Each ij-plane is required to contain \((p_i,p_j)\), a proper face of
the minimal exclusion \(p\). Its mixed excluded corners must number at
most \(|p|_1-2\), with at most \(p_k\) dominating \((p_i,p_j)\).
Here is the arithmetic justification of those two bounds.

A mixed ij-corner \(q\) has a representative \(\gamma e_k\) with
\(\gamma>0\), because representatives have disjoint support and zero
already represents \(p\). Distinct such corners have distinct
representatives. If \(q_i\ge p_i,q_j\ge p_j\), then the included point
\(q-p_i e_i-p_j e_j\) has residue \((\gamma+p_k)a_k\).
If \(\gamma+p_k\le\max_Tx_k\), it collides with the included axis point
\((\gamma+p_k)e_k\). Thus only the last \(p_k\) positive axis
representatives are possible. The other corners have \(q_i<p_i\) or
\(q_j<p_j\), and their distinct positive coordinates allow at most
\((p_i-1)+(p_j-1)\) such corners. The total is at most \(|p|_1-2\).
This is also proved in round2/arithmetic/general_interior_corner_bound.md.

The producer detects mixed corners by row drops. The independent
verifier instead tests their definition: \((x,y)\) absent, but
\((x-1,y)\) and \((x,y-1)\) present. Coordinates 1 through 6 suffice;
coordinate-seven exclusions lie above a pure-axis exclusion.

Every ideal in the class is the intersection of these three plane
projections with \(p+\mathbb N^3\) removed, since every other minimal
exclusion has support at most two. The ideal determines its projections
and its unique full-support corner. No further unclassified geometric
shape is omitted by this representation.

## 3. Independent height-array reconstruction and filters

The producer uses 343-bit masks and shifts. The independent verifier uses
an \(8\times8\) array of integer column heights, with terminal row and
column zero. For xy, xz, yz row profiles \(a,b,c\), respectively, its
height \(H(x,y)\) is zero if \(y\ge a_x\); otherwise it is
\(\min(b_x,c_y)\), further capped at \(p_z\) when
\(x\ge p_x,y\ge p_y\). Thus
\(T=\{(x,y,z):0\le z<H(x,y)\}\).

The retained maximum degree of a nonempty column is \(x+y+H(x,y)-1\).
Cardinality and moments are independently computed as

\[
m=\sum H,\quad S_x=\sum xH,\quad S_y=\sum yH,\quad
S_z=\sum H(H-1)/2.
\]

For \(B=\{0,e_1,e_2,e_3\}\), the erosion
\(A=\{x:x+B\subset T\}\) has heights

\[
E(x,y)=\max(0,\min(H(x,y)-1,H(x+1,y),H(x,y+1))).
\]

Since \(A\) is lower, the nonnegative part of \(A-B\) is exactly \(A\);
the remaining points form three disjoint negative faces. Consequently

\[
|A-B|=\sum E+\#\{E>0\}+\sum_yE(0,y)+\sum_xE(x,0).
\tag{2}
\]

For a genuine residue representative set, labels are injective on
\(A-B\): equality of labels on \(a-b\) and \(a'-b'\) gives equality
on \(a+b'\) and \(a'+b\), both in \(T\), hence equality as integer
vectors. Thus \(|A-B|\le m\). Every erosion rejection violates this
necessary condition.

Let \(F_i=\{x\in T:x+e_i\notin T\}\) and \(n_i=1+\max_Tx_i\).
The arithmetic theorem in round7/global_step_audit.md proves

\[
|F_i\cap F_j|\le2n_k,\qquad\{i,j,k\}=\{1,2,3\}.
\tag{3}
\]

Its proof uses difference-set injectivity on a rectangular dilation, with
no restriction on weights or multiplicity. The independent direct counts
are

\[
\begin{aligned}
Q_{xy}&=\sum\max(0,H(x,y)-\max(H(x+1,y),H(x,y+1))),\\
Q_{xz}&=\#\{H(x,y)>H(x+1,y)\},\\
Q_{yz}&=\#\{H(x,y)>H(x,y+1)\}.
\end{aligned}
\]

The first counts common x- and y-top points in a column. The other two
count its z-top point when that point also lies on the indicated side.
These formulas use no shifted-bitset expression.

The number of coordinatewise maximal points is

\[
K=\#\{H(x,y)>H(x+1,y)\text{ and }H(x,y)>H(x,y+1)\}.
\]

Cases \(K\le6\) use the separately certified six-point Wilf theorem:
each final-window Apéry element in \([c,c+m)\) is maximal, because
adding a nonmultiplicity generator larger than \(m\) would exceed the
largest Apéry value \(c+m-1\). This is a named prior theorem dependency,
not a claim that (1) holds for arbitrary geometric ideals with six maxima.

## 4. Exhaustive counts

Every independent intermediate count and multiplicity histogram matches
the producer, separately for all nine corners.

| Stage | Configurations |
|---|---:|
| Compatible projections satisfying plane restrictions | 55,199,298 |
| Degree at most six | 17,808,013 |
| Cardinality at least 30 | 17,727,110 |
| Ordinary erosion inequality | 12,575,521 |
| All three surface inequalities | 3,742,041 |
| Removed by the six-maxima theorem | 380,607 |
| Exact weighted duals checked | 3,361,434 |

The last two rows partition the preceding row. The dual counts are:

| Corner | Exact duals |
|---|---:|
| \((1,1,3)\) | 580,816 |
| \((1,2,2)\) | 850,024 |
| \((1,1,4)\) | 523,791 |
| \((1,2,3)\) | 486,333 |
| \((2,2,2)\) | 505,232 |
| \((1,1,5)\) | 144,235 |
| \((1,2,4)\) | 96,065 |
| \((1,3,3)\) | 87,117 |
| \((2,2,3)\) | 87,821 |

Matching counts alone would be insufficient. A valid exact dual was also
checked for every individual shape reconstructed by the independent code.

## 5. Exact verification of every weighted dual

For \(v=(a_1,a_2,a_3,M)\), the available inequalities are

\[
(-x_1,-x_2,-x_3,1)\cdot v\ge0\quad(x\in T),
\]

\[
e_i\cdot v\ge1\ (i=1,2,3),\quad e_4\cdot v\ge0,\quad
-e_4\cdot v\ge-7.
\]

The objective vector is \(d=(-4S_x,-4S_y,-4S_z,3m)\).
Column IDs 0 through 342 encode the point
\((\lfloor q/49\rfloor,\lfloor(q\bmod49)/7\rfloor,q\bmod7)\).
IDs 343–345 encode \(a_i\ge1\), ID 346 encodes \(M\ge0\), and ID 347
encodes \(M\le7\).

For each of the 5,733 registry entries, the independent verifier computes
the four-column determinant by fraction-free Bareiss elimination,
reconstructs the inverse numerator by Cramer's rule on unit right-hand
sides, and checks the exact inverse identity. This differs from the
producer's recursive cofactor/adjugate method. All positive determinants
agree with the registry.

For every shape the verifier then:

1. Reads the next explicitly little-endian uint32 basis ID.
2. Checks that each point column **belongs to this reconstructed ideal**.
3. Solves \(C\lambda=d\) exactly, verifies all multipliers are nonnegative,
   and checks the cleared-denominator equation again.
4. Checks
   \[
   \lambda_{343}+\lambda_{344}+\lambda_{345}-7\lambda_{347}
   \ge m-\frac{29}{10}.
   \]

Absent columns contribute zero. The final test, for positive determinant
\(q\), is exactly
\(10(\text{bound numerator})-(10m-29)q\ge0\).
No LP solver, tolerance, rounded coefficient, or floating-point sign test
appears in the independent verifier.

The assignment file contains exactly 13,445,736 bytes, four per residual
shape. Early exhaustion, invalid references, or trailing bytes cause
failure. No shape can silently lack a certificate.

## 6. The integer-slack implication

Let \(A=a_{\min}\ge m+1\), normalize all weights and the height by \(A\),
and set \(D_0=D/A\). A negative integer Wilf number would imply

\[
D\le m(m-2),\qquad
D_0\le\frac{m(m-2)}{m+1}=m-3+\frac3{m+1}.
\]

Therefore, for \(m\ge30\),

\[
m-D_0\ge\frac{3m}{m+1}\ge\frac{90}{31}>\frac{29}{10},
\]

contradicting (1). The last difference is exactly \(1/310\).
A zero rational margin in (1) is sufficient to prove \(W_4\ge0\);
no strict geometric inequality is assumed.

## 7. Reproduction and named external dependencies

Run:

    python3 round7/low_degree6/verify_complete_certificate.py

The runner compiles independent_verify.cpp in a temporary directory,
performs the entire independent enumeration and exact dual replay,
compares all coverage records, and writes
complete_independent_verification.json with SHA-256 hashes. It resolves
all files relative to its own path, so an isolated extracted copy works.
Requirements are a C++17 compiler and Python's standard library; no
optimization package or producer header is required.

The explicit --records-only option compares saved records without the
full replay and marks that weaker scope. The delivered full-run report
uses the default complete replay.

Required inputs are independent_verify.cpp, verify_complete_certificate.py,
dual_bases.jsonl, dual_assignments.bin, and certification.jsonl.
Outputs are independent_verification.jsonl and
complete_independent_verification.json. The producer sources are
provenance and are neither imported nor executed.

The larger Wilf composition additionally requires the preferred Apéry
construction, the completed multiplicity-at-most-29 result, the
no-interior and \((2,1,1)\) subclasses, the six-point theorem, the surface
inequality, and a separate proof for normalized heights at least seven.
The plane-corner restriction, ordinary erosion necessity, and exact
integer-slack implication are included above.

This audit closes the stated low-height certificate. It does not declare
the separate higher-height work complete.
