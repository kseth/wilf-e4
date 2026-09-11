# Independent audit of the arbitrary-weight theorem reduction

This note proves the reduction from arbitrary positive weights to the compact
parameter domain used by the interval certificate. The implication from a
**complete, verified** interval certificate on that domain is rigorous.
Completion and coverage of that certificate are separate obligations recorded
by its author and the structural auditor; this note does not substitute finite
sample checks for those obligations.

Let T be a finite lower ideal in N^3, containing e_1,e_2,e_3, with no
full-support minimal excluded point. Put

    m=|T|, M=max_T a·x, Σ=sum_T a·x, D=3mM−4Σ,

where a_i>0, and suppose m>=30. The desired statement is

    D >= a_min (m−1).

Both D and a_min scale linearly, so normalize a_min=1 and permute the axes
so a=(1,b,c), 1<=b<=c. Suppose for contradiction that D<m−1.

## 1. The lower endpoint M>=5 is exact

If M<5, every x in T satisfies |x|_1<=a·x<=M<5, hence |x|_1<=4.
The proved clique-tree representation decomposes T into a central box
[0,a_0]×[0,b_0]×[0,c_0] and three disjoint nested-rectangle arms. At total
degree allowance 4, a rectangle at an arm level t has endpoints u,v with
u<=cap_1, v<=cap_2, u+v<=4−t. Its largest possible cardinality is exactly

    max_{0<=u<=min(cap_1,4−t)} (u+1)(min(cap_2,4−t−u)+1).

Adding the central box and these slice bounds gives the following exhaustive
table over the 11 sorted central triples:

| Central triple | Cardinality upper bound |
|---|---:|
| (0,0,0) | 13 |
| (0,0,1) | 19 |
| (0,0,2) | 23 |
| (0,0,3) | 25 |
| (0,0,4) | 25 |
| (0,1,1) | 25 |
| (0,1,2) | 28 |
| (0,1,3) | 28 |
| (0,2,2) | 28 |
| (1,1,1) | 29 |
| (1,1,2) | 29 |

Thus m<=29, a contradiction. Therefore M>=5. The table is a finite
cardinality upper bound; it does not require compatibility of independent
maximizing slices. Incompatibility could only lower the cardinality.

## 2. Every failure has M<24

Set u_i=a_i/M, v=min_i u_i=1/M, s=sum_i u_i, and κ=D/(mM).
The supposition D<m−1 gives

    κ < (m−1)/(mM) < 1/M = v.

For any finite lower ideal, the coordinate-fiber identities give
κ=sum_j Eδ_j>=0, where δ_j is the nonnegative height deficit of the
j-fiber top. The existing summed sawtooth estimate is

    s(1−3κ) <= 4κ+5v−3κv+4v².                       (1)

Its derivation uses only the lower-ideal property and presence of the three
unit vectors. It makes no arithmetic residue assumption. Specifically,
writing μ_k=E[u_k X_k] for an axis of minimum weight and U=max_i u_i,

    2 Eδ_j (1+v+u_j) >= 2u_j μ_k − v(1+v), j≠k,
    μ_k=(1+κ)/4−Eδ_k,     sum_j Eδ_j=κ.

Sum the first two inequalities, use Eδ_j>=0 and
(s−v)−(1+v+U)<=0 (all u_i<=1), then U<=s−2v. Rearrangement gives (1).

The completed continuous no-interior moment theorem applies to unit-cube
thickening. Its maximum weight is M+sum_i a_i and its mean is
Σ/m+(sum_i a_i)/2. Therefore its normalized deficit is

    κ_c = (κ+s)/(1+s) >= 1/3.                        (2)

If v>=1/3 then M<=3, already contradicting Section 1. Otherwise v<1/3,
and κ<v. The function

    f_v(κ)=(4κ+5v−3κv+4v²)/(1−3κ)

is strictly increasing for κ<1/3, because its derivative has numerator
4+12v+12v²>0. By (1),

    s < f_v(v) = (9v+v²)/(1−3v).

The expression (κ+s)/(1+s) is increasing separately in κ and s for κ<1.
Combining the last display with κ<v gives

    κ_c < 2v(5−v)/(1+6v+v²).

With (2), multiplication by positive denominators yields

    7v²−24v+1 < 0.

This is impossible for v<=1/24: then both 7v² and 1−24v are nonnegative.
Hence v>1/24, proving M<24. The sharper root bound is
M<12+sqrt(137), but the interval certificate only needs 24.

## 3. Every failure is in the certified domain

Because e_2,e_3 belong to T, b<=M and c<=M. Combining the preceding steps,
any target failure must occur at

    1<=b<=c<=M,       5<=M<24.                        (3)

Thus a complete certificate proving m−D<=1 on the closed domain
1<=b<=c<=M, 5<=M<=24 proves the desired arbitrary-weight theorem.
There is no missing rationality or integrality assumption on b,c,M.
The interval method must bound every real parameter in a box, which it does
by the domination argument below.

## 4. Independent audit of the interval objective

Represent a box by lower and upper scaled endpoints
(b_-,c_-,M_-), (b_+,c_+,M_+), with positive common scale q.
The lower weights are (q,b_-,c_-); the upper weights are (q,b_+,c_+).
Every ideal feasible at a parameter in this box is contained in the enlarged
height region determined by the lower weights and upper height M_+.

At a slice with outward coordinate t and transverse integer endpoints u,v,
the exact scaled score q(m−D) is

    (u+1)(v+1) [4 a_i t + 2 a_j u + 2 a_k v − 3 M + q].

Coordinates and slice cardinalities are nonnegative. Consequently replacing
weights by their upper endpoints and M by its lower endpoint bounds this
score from above. The central-box formula has the same monotonicity.
The nested-rectangle recurrence then maximizes this upper objective over
an enlarged feasible class, so its output bounds every genuine ideal and
every real parameter in the box. Allowing empty horns or ideals lacking e_i
only enlarges the class, and hence is harmless for an upper bound.

The `tightened` operation enforces b<=c<=M only by raising lower bounds and
lowering upper bounds implied by those order inequalities. It excludes no
point of the target domain. The subdivision coverage remains a distinct
certificate obligation and must be checked, as must the DP bound at every
accepted leaf.

## 5. Independent implementation check

`audit_interval_dp.py` enumerates ideals by integer height arrays h(i,j),
not by central boxes or horn recurrences. Nonincreasing heights enforce the
lower-ideal property. At i,j>0, a positive height h(i,j) creates an excluded
full-support corner exactly when both preceding heights are strictly larger;
thus permissible positive heights equal min(h(i−1,j),h(i,j−1)). This supplies
an independent direct enumeration of the relevant ideals.

Six exact test boxes, including unequal lower/upper weights and heights,
contain 35,081 nonempty no-interior ideals in total. Their exact optima all
agree with the interval recurrence. This is an implementation audit of a
bounded sample, not a replacement for the analytic proof or full coverage
certificate. The output is `interval_dp_independent_checks.json`.

## Scope

When the separate complete interval certificate passes, this establishes

    m>=30 and no interior corner  =>  D>=a_min(m−1).

For a genuine four-generator preferred Apéry ideal, a_min>=m+1, so

    m W_4 = D−m(m−1) >= (a_min−m)(m−1) >= m−1.

Since W_4 is an integer, W_4>=1. This conclusion does not address smaller
no-interior ideals or ideals with an interior excluded corner.
