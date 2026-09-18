# Audit of the short-corner congruence exhaustion, multiplicities 30–48

7 September 2026. **PASS.** Both complete outputs agree at every multiplicity
30 through 48. I reviewed the new congruence solver and tuple iterator, and
ran `round5/short_corner_small_m/verify_p211_exhaustion.py`, including its
complete independent test of the residue-solving formulas.

For sorted generators `m<a<b<c`, any permutation of a full corner (2,1,1)
implies at least one of

\[
2a+b+c\equiv0,\quad a+2b+c\equiv0,\quad a+b+2c\equiv0\pmod m.
\]

This uses the previously proved zero representative of a full corner. The
enumeration deliberately includes the larger congruence-defined class; it
does not presume that a congruence is sufficient for that Apéry shape.

The first program correctly solves the first two congruences for c. For the
third, if m is odd then `(m+1)/2` inverts 2. If m is even the right side must
be even; its half and that half plus m/2 give exactly the two solutions.
Sorting and deduplication avoid counting intersections more than once.

For each resulting residue r, the difference of floors

\[
\lfloor(B-r)/m\rfloor-\lfloor(b-r)/m\rfloor
\]

counts exactly the integers in `(b,B]` of that residue. Here `B=m(m-2)` and
both numerators are nonnegative, so C++ division agrees with mathematical
floor. The quotient/residue loop covers those same values exactly once and
in increasing order. All interval endpoints are correct.

The second program tests every residue against the three original
congruences instead of using the solver. The verifying script compares those
two descriptions for every residue pair `(a mod m,b mod m)` and every
m=30,...,48. This complete finite test passed.

The remaining minimality tests, gcd condition, distance update, direct
membership algorithm, and last-window bound have the same logic as the
separately audited multiplicity-20–29 programs. The new programs retain
those algorithms correctly. In particular, a redundant smallest generator
is discarded before any stale distance or membership vector could be read.
The bit windows have width at most 48, below the unsigned 64-bit limit.

The complete common results are 803,005,632 raw congruence-union triples,
508,199,476 minimal four-generator semigroups in the generator box, and
14,416,025 cases with maximum Apéry value at most B. There are no negative
Wilf values. Per-multiplicity counts, minima, witnesses, and checksums agree.
The checksums support reproducibility; the algorithm and complete domain
provide the exhaustive certificate.

The earlier negative-case bound `W4<0 => M<=m(m-2)` covers every omitted
generator or conductor outside the box. Therefore the correct conclusion is
**W4>=0 for the entire infinite congruence-defined class at m=30,...,48**.
As in the earlier audit, absence of zero values inside the box is not used
to assert strict positivity outside it.

This supplies the small-multiplicity component for a complete (2,1,1)
theorem once the independent arbitrary-weight proof at m>=49 is included.
