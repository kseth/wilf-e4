# D1: small-multiplicity simplification decision

**Status date:** 2026-09-12

## Decision

Retain the finite obligation B1.3-FV for \(20\le m\le29\), together with its
two independent checking paths:

1. exact shortest distances in the residue graph; and
2. exact ordinary membership on the bounded integer interval.

No published theorem or currently proved analytic lemma removes this
multiplicity interval. The available filters can make the logical candidate
set look smaller, but they do not reduce the dominant traversal or invariant
calculation and would enlarge the trusted interface. The concise proof
architecture is therefore the direct one:

\[
\text{negative-case conductor bound}
\;\Longrightarrow\;
\text{finite generator box}
\;\Longrightarrow\;
\text{two exact exhaustive checks}.
\]

This decision retains a computation; it does not by itself establish its
result. R1a has since audited and freshly replayed the residue-distance path.
R1b must still curate and replay the ordinary-membership path under the
verification trust policy.

## 1. The retained finite statement

For each \(20\le m\le29\), put \(B_m=m(m-2)\). The raw canonical domain is

\[
\mathcal R_m=
\{(a,b,c)\in\mathbb Z^3:m<a<b<c\le B_m\}.
\]

After exact minimal-generation and gcd tests, compute

\[
d_r=\min\{s\in\langle m,a,b,c\rangle:s\equiv r\pmod m\},
\qquad
M=\max_r d_r.
\]

The retained theorem contract is exactly

\[
\boxed{
M\le B_m
\quad\Longrightarrow\quad
W_4(\langle m,a,b,c\rangle)\ge0
}
\tag{FV}
\]

for every valid tuple in every one of the ten multiplicities. The contract is
the one proved sufficient in the
[B1.3 specification](../paper/small-multiplicity-specification.md). It does
not require strict positivity, and it does not require a claim about valid
tuples with \(M>B_m\).

The raw traversal size is the exact combinatorial count

\[
\sum_{m=20}^{29}\binom{m(m-2)-m}{3}=301{,}098{,}092.
\tag{1}
\]

The much smaller number of tuples surviving \(M\le B_m\) in the historical
records is useful performance evidence, but it is not an input to (FV) and
will not be treated as established until the fresh replays.

## 2. Why the generator bound is not presently smaller

For a hypothetical negative case, the reconstructed conductor argument gives

\[
M\le D,
\qquad
D=mW_4+m(m-1)\le m(m-2),
\]

and hence \(M\le B_m\). The second inequality already uses the full strength
of the available information that the integer \(W_4\) is negative:
\(W_4\le-1\).

A smaller upper bound would require a new uniform input, such as a proved
strict improvement \(D\ge M+\delta\) or a stronger restriction on a negative
integer Wilf number. Neither has been established. The equality audit in the
conductor note identifies additional conditions at \(M=D=B_m\), but does not
exclude them. Deleting the inclusive endpoint, or replacing \(B_m\) by a
smaller expression, would therefore be unjustified.

The published condition \(C>3m\), where \(C\) is the conductor, points in the
opposite direction: since \(M=C+m-1\), it gives \(M\ge4m\). It supplies no
smaller upper bound on the
three generators.

## 3. Why the published hard-case filters are not executable reductions

The L2 comparison gives the necessary conditions

\[
C>3m,\qquad n\ge13,\qquad
\operatorname{type}(S)\ge4,
\qquad
|\operatorname{Max}(T)|\ge4.
\tag{2}
\]

They should not be added to (FV):

- \(C\), \(n\), and \(M\) are learned only from the same Apéry or membership
  data used to evaluate \(W_4\).
- Computing the type requires the Apéry partial order or the
  pseudo-Frobenius numbers, neither of which the direct checks otherwise need.
- Applying the coordinate-maxima filter requires constructing the preferred
  exponent ideal \(T\), adding a third representation solely to skip cases
  whose Wilf number is already cheap to compute.

The same principle applies to full weighted ideals. B1.1 proves them
analytically and is already used to derive the conductor bound, but detecting
full weightedness tuple by tuple would add a lattice-point comparison. Once
the checker has the Apéry distances, directly evaluating \(W_4\) on this
harmless superset is simpler.

Thus the minimal *logical* counterexample class admits more exclusions than
the retained executable domain. Keeping the exact superset (FV) minimizes the
code and the number of theorem-to-program translations that must be trusted.

## 4. Why the large-multiplicity branches are not a replacement

Routing \(m=20,\ldots,29\) through B2--B6 would couple B1 to several more
analytic and computed components without eliminating finite work.

Two thresholds are structural in the current route:

1. The no-corner proof uses \(m\ge30\) to force a point of exponent degree at
   least five; its exact degree-four cardinality bound is 29. Below that
   threshold, extending the abstract weighted theorem would require new
   residue-realizability input or another finite classification.
2. In B6, a negative integer Wilf number gives
   \[
   D_0\le m-3+\frac3{m+1}
       =m-\frac{3m}{m+1}.
   \]
   The retained branch bound \(D_0\ge m-29/10\) contradicts this precisely
   when
   \[
   \frac{29}{10}<\frac{3m}{m+1},
   \]
   that is, when \(m>29\). At \(m=29\) equality remains possible in this
   arithmetic comparison.

Some individual subcases already have separate routes: full weighted ideals
are analytic, while the historical six-final-window class has a more
specialized finite theorem still awaiting reconstruction. Using these routes
to prune B1 would nevertheless require generating the preferred ideal,
classifying its corners and windows, and then retaining a residual generator
search. That hybrid has more dependencies and a larger trusted surface than
checking (FV) directly.

The large-branch machinery may eventually prove statements stronger than
needed for some small multiplicities. No currently reconstructed combination
of those statements covers all B1 cases, so D1 does not move their unfinished
obligations ahead of the direct finite check.

## 5. Why a different finite parametrization is not preferable

The alternatives considered were:

- enumerate Kunz or Apéry-poset faces, as in the published fixed-multiplicity
  work;
- enumerate lower-ideal shapes and residue labelings;
- enumerate possible low-weight corner relations; or
- split the generator box by full corner, degree, height, type, or final
  window.

Each replaces three nested integer-generator loops by a new completeness,
canonicalization, or lifting theorem. None comes with a proved domain smaller
enough to compensate for that added proof burden. The existing generator
parametrization is canonical, has no symmetry quotient beyond sorting, and
uses only elementary prefix membership and gcd tests.

Likewise, importing a broader published computation, such as the genus-100
verification, would not remove computation from the proof; it would introduce
another computational trust boundary and still leave cases in this generator
box outside its invariant cutoff.

## 6. Retained replay interface

D1 fixes the following handoff.

### R1a: residue distances

Audit or replace the historical residue-cycle implementation against the
abstract shortest-path specification. Freshly traverse every \(\mathcal R_m\),
account exactly for the disjoint classification, establish \(M\) for every
valid tuple and the Apéry sum for every tuple with \(M\le B_m\), and reject if
such a tuple has \(W_4<0\).

This path is now complete; see the
[R1a audit and replay](../verification/b1/r1a-residue-distance-audit.md).

### R1b: ordinary membership

Independently regenerate every raw tuple. Use ordinary bounded-integer
membership, not R1a's tuple stream or Apéry data. Prove \(M\le B_m\) through
the final window \([B_m-m+1,B_m]\), then obtain the complete conductor \(C\)
and genus and reject if \(3C-4g<0\).

The two paths may compare per-multiplicity partitions, extremal diagnostics,
and checksums, but neither may accept because the other did. Both must be
exact, fail closed, freshly built, and run over the full specified domain.

The final package should claim only (FV). Historical stronger output for all
valid boxed tuples, positive minima, timings, and cached checksums remains
diagnostic unless a later task deliberately adds it to the theorem contract.

## 7. Gate closure

D1 is closed with the fallback route:

- retain B1.3-FV unchanged;
- retain both R1a and R1b;
- do not add conductor, left-element, type, maxima, corner, or
  full-weightedness filters to the checker contract;
- do not make B1 depend on unfinished B2--B6 results; and
- revisit the decision only if a genuinely new analytic theorem eliminates
  all or a substantial, cheaply recognizable part of \(20\le m\le29\).

This choice favors the smallest reviewable proof interface, not the smallest
raw count printed by a program.
