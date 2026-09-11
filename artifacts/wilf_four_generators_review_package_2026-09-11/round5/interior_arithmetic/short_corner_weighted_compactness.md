# A compact arbitrary-weight domain for the corner (2,1,1)

7 September 2026. Analytic reduction. The separate high-height interval search has completed with zero unresolved boxes; its independent all-leaf audit is recorded by the structural auditor. This note proves the analytic implications, not that external certificate replay.

Let `T` be a finite lower ideal containing the unit vectors, whose only full-support minimal excluded exponent is `p=(2,1,1)`. Put

`m=|T|, M=max_T(Ax+By+Cz), Σ=sum_T(Ax+By+Cz), D=3mM-4Σ`.

Normalize `min(A,B,C)=1`. Suppose `D<m-1`. Then **`M<36`**. This upper bound does not use a continuous one-corner mean theorem or the arithmetic mixed-corner restrictions.

## Planar line-sum inequality

For any finite planar lower ideal `F` with positive linear weight `w`,

`3 sum_F w <= 2|F| max_F w`.

To see this, sum, over both coordinate directions, the column cardinality times the weight of its top. The result is exactly `3 sum_F w`, while each column top is bounded by the global maximum. Thus any translate `u+F` contained in `T` has mean weight at most

`(2/3)M+(1/3)w(u)`.

The assertion is also valid for an empty part, after omitting it.

## First planar partition

Every point of `T` lies in exactly one of the following four parts:

1. `y=0`, a planar lower ideal with translation weight 0;
2. `y>=1,z=0`, a translated planar lower ideal with translation weight B;
3. `x=0,y,z>=1`, with translation weight B+C;
4. `x=1,y,z>=1`, with translation weight A+B+C.

There are no points with x>=2 and y,z>=1, because p is excluded. After translation, each part is a planar lower ideal. If the third and fourth parts have cardinalities m_3,m_4, then m_4<=m_3 by the lower-ideal property. The weighted average of the four translation weights is therefore at most

`L_1=A/2+B+C`.

It follows that `Σ/m <= 2M/3+L_1/3`.

For the simpler, slightly weaker reduction, ignore this pairing and use the maximum translation weight `S=A+B+C`. Then `Σ/m<=2M/3+S/3`; this alone will imply M<42 below.

## Second planar partition

Alternatively split into

- x=0;
- x=1;
- x>=2,y=0;
- x>=2,y>=1,z=0.

The translation weights are 0,A,2A,2A+B. Exchange y,z if necessary to put the smaller of B,C in the last expression. Hence the same mean is at most `2M/3+L_2/3`, where

`L_2=2A+min(B,C)`.

Set `L=min(L_1,L_2)` and `S=A+B+C`. The normalization forces either A=1 or min(B,C)=1.

If A=1, then

`L<=min(S-1/2,(S+3)/2)`.

Taking three fifths of the first bound and two fifths of the second gives

`L<=4S/5+3/10`.

If min(B,C)=1, then

`L<=min(S-A/2,2A+1)`.

Taking four fifths of the first bound and one fifth of the second gives

`L<=4S/5+1/5`.

Consequently the uniform bound is

`Σ/m <= 2M/3+(4S/5+3/10)/3`.

It yields

`D/m >= M/3-(4/3)(4S/5+3/10)`.

Since D/m<1, necessarily

`M<21/5+16S/5`.                                      (A)

## The existing phase estimate bounds S

Write `v=1/M`, `s=S/M`, and `κ=D/(mM)`. The weighted lower-ideal inequality gives κ>=0, and the assumed failure gives κ<v. The prior exact summed sawtooth estimate is

`s(1-3κ)<=4κ+5v-3κv+4v²`.

It requires only a finite lower ideal and the three unit vectors. For M>3, so v<1/3, the expression on the right divided by 1-3κ is increasing in κ. Substitution of the strict bound κ<v gives

`S<(9M+1)/(M-3)=9+28/(M-3)`.                         (B)

If M<=3 there is already nothing to prove about M<36. For M>3, combine (A) and (B):

`M<33+448/[5(M-3)]`,

and therefore

`5M²-180M+47<0`.

For M>=36 the left side is positive (equal to47 at36 and strictly increasing thereafter). This contradiction proves M<36.

The simpler first-partition bound gives `M<3+4S`, and with (B) gives `M²-42M+5<0`, hence M<42. This version may be more convenient in a certificate implementation that uses the inexpensive analytic test `M>=3+4S` to close parameter boxes.

## Elementary generic lower endpoint at multiplicity 49

If M<6, normalization gives T contained in the degree-five simplex Δ5 of56 points. The excluded orthant p+N^3 removes four of them: p and p+e_i. For j=1,2,3,4, the point q_j=(1,j,5-j) has degree6 and is not above p. At least one of its three coordinate-plane projections must be absent fromT; if all three were present, pairwise closure and the absence of any other full-support corner would force q_j intoT. The four triples of projections are pairwise disjoint, lie insideΔ5, and are disjoint from the four p-orthant points. At least eight points are therefore absent, so m<=48.

Consequently, for m>=49 the normalized height satisfies M>=6, with no plane-corner-count hypothesis. This proof works after any permutation of the coordinates. The stronger exact degree-R formula m<=2R²-R+3 and its extremizers are proved in `short_corner_cardinality_theorem.md`.

## Lower endpoint for genuine arithmetic corner data

The residue argument in `short_interior_cell_theorem.md` bounds each coordinate plane to at most two mixed excluded corners; at most one xy/xz corner has x coordinate at least2. An exact enumeration of all lower ideals with these restrictions and total degree at most4 gives 3928 ideals, of maximum cardinality29.

Thus for m>=30 and these necessary arithmetic corner restrictions, normalized weighted height must satisfy M>=5. Every potential weighted-target failure in this class lies in `5<=M<36` (or in the convenient enlarged interval `5<=M<=42`).

## Proof compositions and the status of their dependencies

The exact low-height certificate in `low_height_weighted_certificate.py` has completed: all70175 permitted ideals in degree5 were enumerated, and all28499 with m>=30 have verified rational duals proving the target for every A,B,C>=1. Their minimum margin is19. The separate standard-library coverage and dual replay is recorded in `low_height_independent_replay.json`. This supplies the range `5<=M<6`.

The separate arbitrary-weight interval certificate `round5/one_corner_extension/short_corner_complete_certificate.json` covers all real ordered weights, all three placements of the doubled coordinate, and `6<=M<=42`. Its completed search has110865 nodes,54978 DP leaves,455 analytic leaves, and zero unresolved boxes. The independent all-leaf audit is a separate proof obligation recorded in the structural audit directory. Once that audit passes, this interval certificate and the exact low-height dual replay finish the weighted target for all m>=30. For an actual Apéry ideal, rescaling gives

`D>=a_min(m-1)>= (m+1)(m-1)`,

so `mW_4=D-m(m-1)>=m-1`, and integer-valued W_4 is at least1.

The lower multiplicities are covered separately by the completed multiplicity29 theorem; this note does not reproduce that proof.

There is also a second route to the full arithmetic p211 theorem that does not use the low-height LP certificate. The elementary generic cardinality lemma gives M>=6 for m>=49, and the interval certificate covers that entire upper range. The separately completed necessary-congruence-union computation covers m=30,...,48, and the multiplicity29 theorem covers the rest. This is the route used in the root proof composition; the low-height LP result supplies an independent stronger geometric statement.
