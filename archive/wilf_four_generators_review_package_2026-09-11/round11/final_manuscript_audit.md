# Scope and assembly audit of the review manuscript

11 September 2026.

Reviewed file:
`deliverables/wilf_four_generators_review_manuscript_2026-09-11.md`.
The full reading manuscript was inspected. This was a mathematical scope,
equation-reference, assembly, and bibliography check. No exhaustive computation
was rerun, and the retained global theorems were not independently reproved in
this pass.

## Outcome

No new mathematical gap was identified in the reading manuscript's stated
centroid constructions, new plane-corner argument, general identities, or
case composition. The manuscript accurately presents itself as a synthesis
of a proposed computer-assisted proof, with full technical dependencies in
the archive and external review outstanding.

Five concrete assembly/bibliography corrections were reported to the assembler
and are present in the checked revision:

1. The conductor inequality and its references now use **G3**, leaving **G2**
   for the exposed-surface inequality.
2. The clipped-prism cardinality is defined as Latin **u**, consistent with
   the later formulas; the accidental Greek nu was removed.
3. The first initial for Jonathan Kliem is **J.**, not L.
4. The first initial for Anton Rechenauer is **A.**, not J.
5. The genus-100 paper has its actual title, **A verification of Wilf's
   conjecture up to genus 100**.

The assembler also defined the unnormalized deficit \(D=AD_0\) before its
use in the conductor synopsis and added direct citations for the published
small-multiplicity inputs.

## 1. The new plane-corner proof is valid

Let the unique full-support minimal exclusion be \(p=(r,s,t)\), and let
\(q=(u,v,0)\) be a mixed minimal exclusion in the first coordinate plane.
Such a planar exclusion is also a minimal exclusion of the full lower ideal:
its only positive coordinates are the first two. Its residue representative
has disjoint support and is therefore \(\gamma e_3\), where
\(0\le\gamma<n_3\).

Mixed plane corners have distinct first coordinates and distinct second
coordinates. Thus the union of those with \(u<r\) and those with \(v<s\)
has cardinality at most \((r-1)+(s-1)\).

For each remaining corner, \(u\ge r\) and \(v\ge s\). Set

\[
y=q-(r,s,0).
\]

This point belongs to \(T\), since it is nonnegative and is coordinatewise
at most \(q-e_1\in T\). It is nonzero: otherwise \(q=(r,s,0)\), whereas
\((r,s,0)\le p-e_3\in T\). As the residue representative of \(p\)
is zero, the modular calculation has the positive sign used in the text:

\[
a\cdot y\equiv(\gamma+t)a_3\pmod m.
\]

If \(\gamma+t<n_3\), the distinct included points \(y\) and
\((\gamma+t)e_3\) violate residue injectivity. They are distinct because
\(y\) is a nonzero point of the first coordinate plane. Therefore
\(\gamma\ge n_3-t\). There are at most \(t\) such axis representatives,
and distinct mixed corners have different representatives because they share
a positive coordinate. Combining the two groups proves the asserted
\(r+s+t-2\) bound.

The reading text compresses some of these one-line justifications, but its
argument and residue sign are correct. If desired for maximal readability,
the assembler may add the explicit observation
\(y\le q-e_1\in T\) and the reason \(y\ne0\). These are explanatory
additions, not repairs to the logic.

## 2. The slice-surface argument also has the stated scope

A mixed excluded corner in a planar slice need not be a global minimal
exclusion. Nevertheless its two planar predecessors are included, which is
all the residue argument needs. Any positive representative coordinate in
either planar direction would give equal residues after subtraction from
two distinct included points. Thus its representative lies on the
complementary axis. Distinct such corners across all slices have distinct
residues by the same predecessor subtraction.

There are at most \(n_k\) corners in the collection of all slices. The
number of maximal points in a nonempty planar lower ideal is one more than
its number of mixed exclusions, and exactly \(n_k\) slices are nonempty.
Their maxima are the points of \(F_i\cap F_j\). Hence the total is at most
\(2n_k\), as stated. There is no assertion that each slice separately has
at most two maxima.

The three-plane reconstruction is also correct. Every excluded exponent
dominates a minimal exclusion. In three coordinates every minimal exclusion
except the unique full-support one is visible in a plane projection; deleting
the full corner's upper orthant removes the remaining excluded exponents.

## 3. Main scope and arithmetic checks

- The preferred exponent representatives are defined consistently: lexicographic
  minimization at each Apéry label is compatible with addition, giving lower
  closure. Labels are injective modulo the multiplicity.
- The exact identity \(mW_4=AD_0-m(m-1)\) and its higher-dimensional
  counterpart are correct.
- The local/axis theorem visibly states degree at most six, \(m\ge30\),
  the unique corner condition, and the two retained arithmetic restrictions.
  Neither its \(D_0\ge m\) conclusion nor its \(W_4\ge2\) consequence
  is promoted to all semigroups.
- The degree partition includes its boundary: degree at least seven implies
  \(H\ge7\), while the local theorem is valid at every normalized height.
- The table retains small multiplicities, no full-support corner, the two
  exceptional corner types, and the high-height theorem as separate inputs.
- The negative-integer comparison uses
  \(90/31-29/10=1/310\), with the correct direction.
- Positive minima from the bounded generator-box checks are correctly not
  used to assert positive Wilf number for arbitrary generators outside the box.
- The 5,574,644 ideal/profile count and 431 fallback count are correctly
  distinguished from numerical semigroups and coordinate-permutation orbits.
- The envelope appendix retains its stronger arithmetic hypotheses and its
  separate high-height dependency. It claims only \(D_0\ge m-29/10\)
  globally over normalized weights, despite a better margin in its checked
  low-height parameter cells.

## 4. Higher-dimensional limitations are presented accurately

The identity \(\sum L_\ell t_\ell=(d+1)s\), centroid target
\(|r|_1\ge(d-1)m/2\), and negative-integer threshold \(dm/(m+1)\)
are consistent. The proposed five-generator threshold \(39/10\) is labelled
as sufficient and unproved. Its displayed strict margin \(1/410\) is correct.

The ordinary-semigroup equality example is correct and directly excludes a
universal positive-surplus statement for every genuine Apéry ideal. For
\(T=\{0,e_1,\ldots,e_d\}\), any convex combination has coordinate sum
at most one, giving the claimed nonpositive total residual.

The clipped-box residual identity and its sufficient positive lower bound
hold for \(d\ge4\). The manuscript identifies this as an infinite structural
family, not a classification or a proof of all higher-dimensional cases.
The two concrete five-generator examples are explicitly identified as failures
of proposed geometric extensions, not Wilf counterexamples.

The enormous fixed-dimension bound is attached to a separate archived proposed
analytic theorem with its own review obligations. It is not presented as a
consequence of the four-generator centroid computations or as a feasible
five-generator enumeration.

## 5. Bibliography checked against primary source pages

The following arXiv pages were opened during this audit:

- [Bruns, García-Sánchez, O'Neill and Wilburne](https://arxiv.org/abs/1903.04342):
  author names, title, and the claim for multiplicities through 18 agree.
- [Kliem and Stump](https://arxiv.org/abs/1905.01945): the first author is
  Jonathan Kliem; the title agrees; version two states the multiplicity-19
  result.
- [Zhai](https://arxiv.org/abs/1111.2779): the title and author agree. Its
  approximate asymptotic conclusion is correctly distinguished from exact
  eventual Wilf.
- [Hellus, Rechenauer and Waldi](https://arxiv.org/abs/1804.06141): the second
  author is Anton Rechenauer; the corrected entry agrees with the primary page.
- [Delgado, Eliahou and Fromentin](https://arxiv.org/abs/2310.07742): the
  corrected title is *A verification of Wilf's conjecture up to genus 100*.

No statement that this literature externally validates the new proof appears
in the manuscript.

## 6. Equation-reference and correction check

For the checked revision, the script-level audit found 25 unique equation
tags and no duplicate tags. Every explicit parenthesized equation reference
resolves to a declared tag. The known notation and bibliography corrections
above were present. The equation-tag sequence is

`G1, G2, C1, C2, C3, C4, C5, C6, C7, C8, G3, HD1, ..., HD13, A9`.

The single appendix tag `A9` is harmless but could be renamed `A1` as a
cosmetic cleanup, provided its two references are changed together.

The SHA-256 of that checked revision was

`0f848d569cddc7509cf5c100220ad8d27062b2bda6f4e0a1d1367d4b606020a8`.

Later presentation-only edits may change this hash; it records the review
snapshot rather than prescribing a final artifact identifier.

## 7. Optional final prose polish

The mathematical reading is coherent as written. Three small optional edits
would make it read more like a unified manuscript:

1. Replace the remaining phrase "after Round 10" and the two phrases "This
   supplement" with references to the present proof/manuscript.
2. Define "full weighted ideal" in the conductor synopsis as
   \(T=\{x\in\mathbb N^3:a\cdot x\le M\}\), and define the genus
   \(g=|\mathbb N\setminus S|\) the first time the genus formula is used.
3. Open Appendix A by explicitly saying it concerns the degree-six residual
   class, with the two additional necessary restrictions from its detailed
   envelope proof. This prevents a reader encountering the appendix alone
   from mistaking its fixed-ideal discussion for an arbitrary-ideal theorem.

These are readability recommendations. No new unverified mathematical claim
or computational obligation is required by this audit.
