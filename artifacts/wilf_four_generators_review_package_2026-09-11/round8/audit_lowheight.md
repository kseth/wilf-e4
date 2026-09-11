# Adversarial audit of the low-height arithmetic and exact certificate

11 September 2026.

## Result and limits

I found no gap in the low-height arithmetic filters, the finite shape coverage,
or the exact weighted certificate. I reconstructed the mathematical reasons for
each rejection, inspected both the producer and the independent verifier, and
performed a fresh full replay from a separate `round8/lowheight_replay` copy.
Every one of the **3,361,434** assignments passed, and all intermediate counts
and all nine complete multiplicity histograms matched.

The resulting statement is precise: a genuine preferred Apéry ideal with
`m >= 30`, a full-support minimal excluded point of coordinate sum at least
five, and normalized height `H < 7` is covered either by the separately proved
six-final-window theorem or by the exact inequality

\[
3mH-4\sum_{x\in T}b\cdot x\ge m-\frac{29}{10}.
\]

This audit independently justifies the arithmetic filters. It does not reprove
the six-final-window theorem, the multiplicity-through-29 theorem, the
no-interior or `(2,1,1)` cases, or the higher-height certificate. Those remain
explicit dependencies of the overall composition. No external mathematical
review or proof-assistant formalization is asserted here.

## 1. The representative-set premises are sufficient

Write `phi(x)=a dot x mod m`. The preferred Apéry exponent set `T` is a finite
lower ideal and contains exactly one representative of each residue. The
arguments below only need these properties; they do not use a hidden metric,
generic-weight hypothesis, or a stronger kind of lattice tiling.

For completeness, choose the lexicographically least factorization of each
Apéry element into the three nonmultiplicity generators. If `y <= x` and
`x` is preferred, a strictly smaller weight representative of `y` would, after
adding `x-y`, contradict Apéry minimality at `x`. An equal-weight,
lexicographically smaller representative of `y` would contradict the preferred
choice at `x`, since lexicographic order is translation invariant. Thus `T`
is lower. Minimality of the four generators ensures the three coordinate
units belong to `T`.

Let `q` be a minimal excluded point and let `r in T` have its residue. If
`q_i > 0` and `r_i > 0`, the distinct points `q-e_i` and `r-e_i` lie in `T`
and have the same residue, which is impossible. Hence their supports are
disjoint. In particular, every full-support minimal exclusion represents
zero. Two such exclusions would have equal-residue predecessors in any
direction, so there is at most one full-support minimal exclusion `p`.

These observations also justify using the same arguments for coordinate-plane
corners: their absent coordinate is zero, so planar minimality is global
minimality.

## 2. Plane-corner restrictions, including the endpoint counts

Take `p=(r,s,t)` and a mixed `xy`-plane corner `q=(u,v,0)`. Its representative
is `gamma e_3`, with `0 <= gamma < n_3`, where `n_3` is the number of axis
points in `T`. Distinct mixed corners have distinct representatives: both have
their direction-one predecessor in `T`. Also `gamma != 0`, since otherwise
`q-e_1` and `p-e_1` would collide.

Suppose `u >= r` and `v >= s`. Then

\[
d=q-(r,s,0)\in T.
\]

To justify this membership explicitly, `r,s >= 1` implies
`d <= q-e_1`, whose membership follows from minimality of `q`. Moreover
`d != 0`, because the face `(r,s,0)` belongs to `T` and cannot equal the
excluded point `q`. Since `phi(p)=0`,

\[
\phi(d)=\phi((\gamma+t)e_3).
\]

The two exponent vectors are distinct: `d` is a nonzero plane point whereas
the latter is a positive axis point. If `gamma+t < n_3`, both would belong to
`T`; hence `gamma+t >= n_3`. The possible distinct `gamma` therefore lie in

\[
[\max(0,n_3-t),n_3-1]\cap\mathbb Z,
\]

which contains at most `t` values. This remains valid when `t >= n_3`;
it does not require a tacit assumption that the terminal interval has positive
left endpoint.

All other mixed corners satisfy `u < r` or `v < s`. In a planar lower ideal,
mixed minimal excluded corners have pairwise distinct positive first
coordinates, and pairwise distinct positive second coordinates: two with the
same coordinate would be comparable, contradicting minimality. There are at
most `r-1` of the first kind and `s-1` of the second kind. Double counting
corners satisfying both conditions is harmless for an upper bound. Therefore

\[
\#\{\text{mixed }xy\text{ corners}\}\le r+s+t-2,
\qquad
\#\{q:q\ge(r,s,0)\}\le t.
\]

All three coordinate orientations follow by relabeling. These are exactly
the two restrictions enforced by `eligible` in the verifier.

The coarser maximal-point estimate in
`round2/arithmetic/general_interior_corner_bound.md` is also valid. In a
slice `x=i<r`, the unique full-support exclusion is inactive. Conditions
supported on `xy` or `xz` restrict the `yz` projection by an axis-aligned
rectangle. Truncating a planar staircase by a rectangle cannot increase its
number of mixed corners, so there are at most `k_yz+1` planar maxima in that
slice. Every global maximum belongs to at least one of the slabs
`x<r`, `y<s`, or `z<t`, giving

\[
|\operatorname{Max}T|
\le r(k_{yz}+1)+s(k_{xz}+1)+t(k_{xy}+1)
\le (r+s+t)(r+s+t-1).
\]

## 3. Ordinary erosion is a necessary arithmetic condition

Let `B={0,e_1,e_2,e_3}` and `E={x:x+B subset T}`. This is lower. If
`phi(x-b)=phi(x'-b')` with `x,x' in E`, then
`phi(x+b')=phi(x'+b)`. Both latter vectors belong to `T`, so their equality
as residues implies equality as integer vectors and therefore
`x-b=x'-b'`. Thus `phi` is injective on `E-B`.

The nonnegative part of `E-B` is precisely `E`, by lower closure. Every
remaining vector has one coordinate equal to `-1` and all other coordinates
nonnegative; the three possible negative faces are pairwise disjoint.
Consequently

\[
|E-B|=|E|+\sum_i|E\cap\{x_i=0\}|\le m.
\]

This proof includes the case `E` is empty and needs no convexity assumption.

## 4. The surface injection is valid for all genuine ideals

Set `F_i={x in T:x+e_i notin T}`. For distinct `i,j,k`, consider the excluded
points `q` with `q_i,q_j > 0` and both `q-e_i,q-e_j in T`. They are the mixed
minimal exclusions of the nonempty planar slices perpendicular to `k`.

Every nonempty finite planar lower ideal with `h` maximal points has `h-1`
mixed minimal exclusions. One direct verification orders its positive row
lengths: each strict drop to another positive length gives one mixed corner,
and each constant run gives one maximal point. Summing over the `n_k`
nonempty slices therefore gives

\[
|C_{ij}|=|F_i\cap F_j|-n_k.
\]

For `q in C_ij`, its representative `r` has `r_i=r_j=0`, by comparing the
two corresponding predecessors in `T`. Distinct members of `C_ij` have
distinct residues, since their direction-`i` predecessors belong to `T`.
Thus their representatives inject into the `k` axis, giving

\[
|C_{ij}|\le n_k,
\qquad |F_i\cap F_j|\le 2n_k.
\]

This remains true even though a member of `C_ij` need not be a *globally*
minimal exclusion: only the two specified predecessor memberships are used.
That distinction does not invalidate the argument.

I also checked the exact dilation calculation in `global_step_audit.md`.
In a block dilation with factors `L_i,L_j >= 2`, eroding in directions
`i,j` and adjoining the two negative faces gives precisely
`L_k(|F_i intersection F_j|-2n_k)` excess points over the dilated domain.
This is consistent with the direct injection and supplies a second proof;
the low-height certificate requires only the direct theorem above.

## 5. Complete low-height coverage

For normalized weights `b_i>=1`, height `H<7` forces every retained integer
point to have total degree at most six. If `p` is minimal excluded,
`p-e_i in T` forces `|p| <= 7`. After the prior corners `(1,1,1)` and
permutations of `(2,1,1)` are removed, the nine sorted positive triples of
sums five through seven are precisely the displayed enumeration. Sorting
the corner does not sort or restrict the weights: the dual domain contains
all three independent weights `b_i>=1`. Therefore no corner orientation is
lost.

The ideal is exactly the intersection of the three cylinders over its plane
projections, with `p+N^3` removed. Indeed, every excluded point lies above a
minimal exclusion; any minimal exclusion other than `p` has support at most
two and is detected by a corresponding plane projection. Conversely every
retained point satisfies all these conditions.

Each plane profile has seven nonincreasing row lengths, with
`0 <= h_i <= 7-i`. The verifier enumerates these by seven-element subsets
of `{0,...,13}` using `h_i=t_i-6+i` for decreasing `t_i`. The inverse is
`t_i=h_i+6-i`; this proves bijective coverage. The number of nonempty valid
profiles is 1,429. Restricting mixed-corner loops to coordinates one through
six is safe: a mixed corner with coordinate seven would already have its
predecessor in the other direction outside the degree-six plane.

The shared-axis equalities are implemented for every pair of projections.
They ensure the reconstructed three-dimensional intersection retains exactly
the specified plane projections. Requiring each projection of `p` to belong
to the corresponding plane ensures that all `p-e_i` belong to the
intersection before the orthant cut, so this construction introduces no
unnoticed stronger exclusion below `p`.

The independent height-array implementation calculates cardinality and all
moments directly. Its erosion, surface, and maxima formulas are exact:

\[
E(x,y)=\max(0,\min(h(x,y)-1,h(x+1,y),h(x,y+1))),
\]

\[
Q_{xy}=\sum_{x,y}\max(0,h(x,y)-\max(h(x+1,y),h(x,y+1))),
\]

\[
Q_{xz}=\#\{(x,y):h(x,y)>h(x+1,y)\},
\quad
Q_{yz}=\#\{(x,y):h(x,y)>h(x,y+1)\}.
\]

A column has a coordinatewise maximal point exactly when its top is above
both neighboring column tops. The zero padding at index seven handles all
boundaries correctly. Every final-window Apéry point in `[c,c+m)` is
coordinatewise maximal, since adding a nonmultiplicity generator greater
than `m` would exceed `M=c+m-1`. Thus the six-maxima rejection has exactly
the stated prior six-final-window theorem as its dependency.

## 6. Exact dual verification and arithmetic safety

For each surviving shape, let `s_i=sum_T x_i`. The objective vector is
`d=(-4s_1,-4s_2,-4s_3,3m)`. A point-column `(-x_1,-x_2,-x_3,1)` is the valid
constraint `H-b dot x>=0`. The other columns encode `b_i>=1`, `H>=0`, and
`-H>=-7`. Their right sides are respectively one, zero, and negative seven.

The verifier checks membership of every point-column in the current
reconstructed ideal. It independently reconstructs each basis inverse by
Bareiss determinants and Cramer's rule, verifies the inverse identity, and
then checks nonnegative coefficient numerators and the exact equation
`C lambda=d`. Its final integer inequality is exactly

\[
10\big(\text{lower-bound numerator}\big)-(10m-29)\det C\ge0,
\]

with a positive determinant convention. The bound therefore follows from a
nonnegative rational combination of valid inequalities. There is no
floating-point acceptance criterion. The upper-height column is explicitly
used, so this certificate cannot be applied without `H<=7`.

There are at most 84 points in the degree-six simplex; each coordinate is
at most six. Matrix entries have magnitude at most six. The crude bounds
`4! 6^4` for determinants, `3! 6^3` for cofactors, and `4*84*6=2016` for
objective-coordinate magnitudes already place all inverse identities,
multiplier sums, objective checks, and margin calculations far below the
signed 64-bit limit. The Bareiss products and rational-margin comparisons
use 128-bit intermediate arithmetic. There is no plausible overflow gap
within this finite domain.

Each residual shape consumes exactly one explicitly little-endian uint32
basis identifier. Missing records, invalid basis references, point
nonmembership, negative multipliers, failed reconstruction, and trailing
bytes all produce errors. Consequently matching total counts alone are not
being used as a substitute for checking individual assignments.

## 7. Fresh complete replay and independent falsification probe

The fresh replay command was:

```sh
python3 round8/lowheight_replay/verify_complete_certificate.py
```

It compiled the inspected independent C++ verifier and recomputed every
shape and every exact assignment. It did not use the `--records-only`
option. The resulting record is
`round8/lowheight_replay/complete_independent_verification.json`.

| Stage | Fresh verified count |
|---|---:|
| Compatible projection triples | 55,199,298 |
| Degree at most six | 17,808,013 |
| Cardinality at least 30 | 17,727,110 |
| Erosion passes | 12,575,521 |
| Surface passes | 3,742,041 |
| Six-maxima dependency | 380,607 |
| Exact weighted assignments | 3,361,434 |
| Distinct exact bases | 5,733 |

The replayed assignment-file SHA-256 is
`5ef90115f09c42b7747436216f1897ddb2ee9e9b46e97d24e5c58de11f9cb1de`.
The inspected independent-verifier source SHA-256 is
`d29a113f38dbf478cdf2ec83ddde4bbe5147ba776ccd5b68302abb95fc137a88`.

As an independent attempt to falsify the arithmetic assumptions on genuine
semigroups, `round8/probe_lowheight_genuine.py` generated 30,000 deterministic
candidate generator quadruples, built value/lexicographic Apéry
representatives by Dijkstra, and directly formed excluded corners, erosion
difference sets, surface intersections, and residue maps. Among 28,002
numerical candidates, 23,692 were minimally four-generated; 5,976 had a full
corner and 4,494 had height below seven. All tested necessary conditions
held. There were 146 examples in the residual low-height class, across
eight of the nine sorted corner types; their reconstruction and weighted
bound checks also passed. No Wilf counterexample occurred; the smallest
observed Wilf number was zero.

That deterministic probe is a falsification check, not exhaustive evidence
for the theorem. Its exact results and sample hash are in
`round8/probe_lowheight_genuine_checks.json`. The mathematical coverage and
the full certificate replay above are the substantive verification.

The probe explicitly tests each sorted generator for membership in the
semigroup generated by its predecessors. During review I corrected an initial
diagnostic shortcut that treated coordinate-unit membership as a converse
test for irreducibility: a reducible generator can still win a lexicographic
factorization tie. The final probe was rerun with direct irreducibility
checks, and the counts above are from that corrected run. No proof or
certificate step uses the invalid converse.

## 8. Exact implication for Wilf

Let `A=min(a_i)>=m+1`, `D=3mM-4 sum Ap(S,m)`, and `D_0=D/A`. The exact
Apéry moment identity is

\[
mW_4=D-m(m-1).
\]

A negative integer Wilf number implies `D<=m(m-2)`, hence for `m>=30`

\[
D_0\le\frac{m(m-2)}{m+1}
=m-3+\frac3{m+1}
\le m-\frac{90}{31}
<m-\frac{29}{10}.
\]

The last strict separation is exactly `1/310`. This contradicts the exact
weighted certificate whenever that certificate is used; shapes assigned to
the six-maxima class are settled by their named prior theorem. The argument
proves nonnegativity of the Wilf number in the stated low-height class. It
does not replace the weaker conclusion by an unjustified claim of strict
positivity.

No repair to the existing low-height proof or certificate was required.
