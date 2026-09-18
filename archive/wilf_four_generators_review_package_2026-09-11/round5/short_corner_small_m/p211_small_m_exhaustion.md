# Exact short-corner congruence exhaustion at multiplicities 30 through 48

Research checkpoint: 7 September 2026.

**Theorem.** Let `S=<m,a,b,c>` be minimally four-generated, with
`30<=m<=48` and `m<a<b<c`. If at least one of

\[
2a+b+c\equiv0,\qquad a+2b+c\equiv0,\qquad a+b+2c\equiv0\pmod m
\tag{1}
\]

holds, then `W_4(S)>=0`.

In particular, this covers every preferred Apéry ideal having an interior
minimal excluded exponent that is a coordinate permutation of `(2,1,1)`
at one of these multiplicities. An interior minimal excluded exponent has
residue representative zero, so that corner implies (1). The computation
checks the larger union defined by (1); it does not presume the congruence
alone implies that the preferred corner is `(2,1,1)`.

The theorem depends on the already proved analytic conductor reduction,
which has no large-multiplicity hypothesis:

\[
W_4<0\quad\Longrightarrow\quad
M=\max\operatorname{Ap}(S,m)\le m(m-2),
\qquad a,b,c\le m(m-2).
\tag{2}
\]

Its full proof is §4 of
`deliverables/wilf_edim4_global_finite_reduction_2026-09-05.md`;
the immediately preceding `round5/small_multiplicity` proof and independent
audit also inspect its use in finite exhaustion. No counterexample satisfying
(1) is lost by restricting the sorted generators to the inclusive box in (2).

## Exact residue reduction

For every `m<a<b<B=m(m-2)`, the first complete program constructs the set
of all possible residues of `c` satisfying (1):

* `c=-2a-b mod m`;
* `c=-a-2b mod m`;
* every solution of `2c=-a-b mod m`.

For the third congruence, if `m` is odd, multiplication by `(m+1)/2`
inverts 2 modulo `m`. If `m` is even, there are no solutions when the
right side is odd; otherwise the two solutions are half the right side
and that value plus `m/2`. The resulting set contains at most four
residues. It is sorted and deduplicated.

Every corresponding integer `b<c<=B` is enumerated. For a residue `r`,
the exact number is

\[
\left\lfloor\frac{B-r}{m}\right\rfloor
-\left\lfloor\frac{b-r}{m}\right\rfloor.
\]

All divisions here have nonnegative numerators. The program partitions
the resulting domain into redundant smallest generator, redundant middle
generator, redundant largest generator, nontrivial total gcd, and valid
minimal four-generator numerical semigroups. The count partition is checked.

The independent second program constructs the permitted residue set by
testing **every** `r=0,...,m-1` against the three congruences directly. Thus it
does not reuse the first program's congruence-solving formulas.

## Two independent invariant calculations

`exhaust_p211_relations.cpp` uses exact cyclic residue shortest paths and
calculates

\[
W_4=\frac{3mM-4\sum\operatorname{Ap}(S,m)-m(m-1)}m.
\]

`independent_p211_membership.cpp` uses ordinary integer membership on
`[0,B]`, with exact membership of `[B-m+1,B]` deciding whether `M<=B`.
When that interval is present, closure under `+m` proves all larger
integers are present, so the complete genus `g` and conductor `C` are
obtained directly and `W_4=3C-4g`.

The proof of both invariant algorithms, including the two-pass cycle update
and exact last-window equivalence, is in
`round5/small_multiplicity/exhaustive_m20_m29_theorem.md`. Here the only
changed domain is the exact congruence union above. Both programs are
self-contained C++17 sources and use integer arithmetic for every inclusion,
invariant, and inequality test.

The recorded per-m counts and sequence checksums agree between the two
algorithms. The checksums concern `(a,b,c,M,sum Ap,W)` for all cases with
`M<=B`; they support reproducibility, while exact enumeration and the
algorithm proofs supply the certificate.

## Scope

The conclusion is `W_4>=0` over the entire infinite class satisfying (1)
at `30<=m<=48`, using (2) to cover its complement outside the finite box.
Positive box minima do not imply global strict positivity outside the box.

Together with the separate complete `m<=29` result, this handles the
`(2,1,1)` corner class through multiplicity 48. A proof for higher
multiplicities requires the separate weighted geometric argument. This
computation alone is not a theorem for all interior corners or all
four-generator numerical semigroups.

## Exact results

| m | Inclusive generator bound | Congruence-union triples | Minimal e4 semigroups | M within bound | Minimum W in box |
|---:|---:|---:|---:|---:|---:|
| 30 | 840 | 8,536,608 | 4,330,272 | 159,754 | 71 |
| 31 | 899 | 10,187,436 | 6,694,206 | 263,014 | 73 |
| 32 | 960 | 12,074,556 | 6,655,250 | 229,487 | 73 |
| 33 | 1,023 | 14,231,260 | 9,345,555 | 326,799 | 100 |
| 34 | 1,088 | 16,674,652 | 9,069,275 | 290,669 | 80 |
| 35 | 1,155 | 19,467,104 | 13,918,461 | 473,571 | 87 |
| 36 | 1,224 | 22,607,684 | 12,180,137 | 387,664 | 93 |
| 37 | 1,295 | 26,140,832 | 18,169,263 | 601,821 | 102 |
| 38 | 1,368 | 30,086,840 | 16,793,553 | 496,864 | 131 |
| 39 | 1,443 | 34,529,988 | 23,452,252 | 709,863 | 109 |
| 40 | 1,520 | 39,463,756 | 23,029,727 | 678,252 | 103 |
| 41 | 1,599 | 44,945,716 | 32,107,636 | 954,771 | 123 |
| 42 | 1,680 | 50,999,156 | 27,490,689 | 762,810 | 126 |
| 43 | 1,763 | 57,734,680 | 41,783,755 | 1,191,144 | 135 |
| 44 | 1,848 | 65,137,684 | 38,978,146 | 1,030,942 | 141 |
| 45 | 1,935 | 73,280,984 | 51,053,259 | 1,405,382 | 147 |
| 46 | 2,024 | 82,190,544 | 47,737,360 | 1,211,968 | 160 |
| 47 | 2,115 | 92,008,092 | 68,080,231 | 1,799,308 | 152 |
| 48 | 2,208 | 102,708,060 | 57,330,449 | 1,441,942 | 131 |
| **Total** | — | **803,005,632** | **508,199,476** | **14,416,025** | **71** |

Both complete programs reported zero negative Wilf numbers. The first program also found no zero Wilf number anywhere in its generator boxes; the second independently confirmed this in the entire necessary counterexample region. The minimum within these boxes is `W=71`, attained at `<30,31,35,49>`.

The recorded first and second runs took approximately 150.4 and 129.3 seconds, respectively. They ran concurrently, so these are sums of measured per-m wall durations, not standalone benchmark claims.

`verify_p211_exhaustion.py` compares both complete records, verifies every count partition and minimizing fixture, and additionally checks the explicit congruence solver against all residues for every residue pair at every multiplicity 30 through 48. Its recorded result is `p211_exhaustion_verification.json`.

To reproduce the full computation with a C++17 compiler and Python 3:

```sh
python3 /path/to/short_corner_small_m/verify_p211_exhaustion.py --rerun
```

Without `--rerun`, it checks the complete recorded certificate plus the exhaustive finite residue comparison. No nonstandard Python package is required.
