# Literature survey for the embedding-dimension-four project

**Status:** working research record, not a priority or completeness claim

**Search dates:** broad survey 2026-09-11; focused reduction refresh 2026-09-12;
structural-source check 2026-09-14; selected-proof refresh 2026-09-17

**Scope:** Wilf's conjecture, with emphasis on results that either dispose of
cases in embedding dimension four or supply machinery used by the proposed
proof in this repository.

## 1. Executive assessment

The literature review changes how the eventual paper must present the proof.
The preferred-factorization model of an Apéry set as a finite lower ideal is
not new: it occurs in Zhai's asymptotic work and is developed algebraically by
Hellus, Rechenauer, and Waldi. Their work also contains a residue-lattice
tiling and a minimal-exclusion result very close to the foundational exclusion
lemma in the present proof.[^zhai][^hrw] Those results should be cited at the
point of use, with only the precise strengthening needed here proved anew.

The likely new content is narrower and clearer: in three exponent variables,
the proposed proof seeks a *positive surplus* beyond the standard weighted
mean inequality for a finite lower ideal, strong enough to absorb the exact
Apéry correction term. Its seven geometric branches and their finite
certificates are the work that must be independently verified.

Existing theorems remove a substantial boundary before that argument starts.
For an embedding-dimension-four semigroup, a genuinely unresolved input to the
new proof may be assumed to satisfy

\[
  m\ge 20,\qquad c>3m,\qquad |S\cap[0,c)|\ge 13,
  \qquad \operatorname{type}(S)\ge 4.
\]

The first three restrictions follow respectively from fixed-multiplicity,
conductor-depth, and small-left-part results; the last follows from the
classical type bound.[^bruns][^kliem][^macaulay][^left12][^fgh]

As of the search date, no independent article or preprint was located that
claims Wilf's conjecture for *all* numerical semigroups of embedding dimension
four. This is a report of the searches performed, not evidence that no such
work exists. It must be checked again immediately before circulation, and the
manuscript should be shown privately to specialists in numerical semigroups.

## 2. The conjecture and the classical boundary

Let \(S\subseteq\mathbb N\) be a numerical semigroup. Write \(e\) for its
embedding dimension, \(m\) for its multiplicity, \(c\) for its conductor,
\(g=|\mathbb N\setminus S|\) for its genus, and
\(n=|S\cap[0,c)|=c-g\). Wilf's 1978 question is equivalent to

\[
  en\ge c.
\]

The original source is Wilf's *A Circle-of-Lights Algorithm for the
“Money-Changing Problem”*.[^wilf] A publication should cite the original
paper, not only later surveys.

Fröberg, Gottlieb, and Häggkvist established two facts that remain central:
the conjecture for \(e\le3\), and the type inequality \(g\le tn\), where \(t\)
is the type.[^fgh] Hence \(t\le e-1\) implies
\(c=n+g\le(t+1)n\le en\). Dobbs and Matthews gave another early treatment of
Wilf's question and several small cases.[^dobbs]

Delgado's survey is the best single orientation source through 2020, but the
eventual paper should cite the primary papers for every theorem actually used.
[^delgado-survey]

## 3. Established regions relevant to \(e=4\)

| Hypothesis known to imply Wilf | Source | Consequence for this project |
|---|---|---|
| \(e\le3\) | Fröberg--Gottlieb--Häggkvist; Dobbs--Matthews | Explains why \(e=4\) is the first open embedding dimension. |
| \(t\le e-1\) | \(g\le tn\), Fröberg--Gottlieb--Häggkvist | A hard \(e=4\) case has \(t\ge4\). |
| \(c\le2m\) | Kaplan | Subsumed by the stronger \(c\le3m\) result below. |
| \(2e\ge m\) | Sammartano | For \(e=4\), handles only \(m\le8\). |
| \(c\le3m\) | Eliahou | A hard case has \(c>3m\). |
| \(3e\ge m\) | Eliahou | For \(e=4\), handles \(m\le12\). |
| \(\lvert S\cap[0,c)\rvert\le12\) | Eliahou--Marín-Aragón | A hard case has \(n\ge13\). |
| fixed \(m\le18\) | Bruns--García-Sánchez--O'Neill--Wilburne | Computer-assisted Kunz-cone verification. |
| fixed \(m=19\) | Kliem--Stump | Extends the verified range to \(m\le19\). |
| genus \(g\le100\) | Delgado--Eliahou--Fromentin | Independent large finite verification; not needed in the present route. |
| \(m\mid c\) and \(4e\ge m\) | Eliahou | For \(e=4\), gives \(m\le16\), already inside \(m\le19\). |
| almost symmetric | Barucci; D'Anna--Moscariello[^barucci][^danna] | Removes a structural family, but not the whole hard range. |

Kaplan's result is part of a broader study of numerical semigroups by genus.
[^kaplan] Sammartano proved the high-embedding-dimension criterion and several
other families.[^sammartano] Eliahou's Macaulay-theorem paper proves the
conductor bound \(c\le3m\), while the later graph-theoretic paper improves the
embedding-dimension threshold from \(m/2\) to \(m/3\).[^macaulay][^graph]
Eliahou and Marín-Aragón settle the case of at most twelve left elements.
[^left12]

The fixed-multiplicity computation uses Kunz polyhedra, their face structure,
and Apéry posets. Bruns et al., Theorem 4.3, prove the result for every
numerical semigroup with \(m\le18\). Kliem and Stump, Proposition 6.9 in the
published version, use a more efficient face iterator to settle every
numerical semigroup with \(m=19\).[^bruns][^kliem] These statements have no
embedding-dimension or other subclass restriction and together justify the
present cutoff at 20. The theorem-level source and scope check is recorded in
the [multiplicity-through-19 audit](multiplicity-through-19-audit.md).

The genus-100 verification is a separate tree-enumeration computation and is
valuable corroborating context, not a substitute for the proposed uniform
\(e=4\) proof.[^genus100]

## 4. Direct lineage of the proposed proof

### 4.1 Apéry sets and preferred factorizations

For \(S=\langle m,a_1,a_2,a_3\rangle\), the repository chooses one
factorization by \(a_1,a_2,a_3\) for each element of
\(\operatorname{Ap}(S,m)\), using a fixed lexicographic rule, and calls the set
of exponent vectors \(T\subseteq\mathbb N^3\).

This construction must not be presented as novel. Zhai chooses preferred
factorizations of Apéry elements and observes that their exponent vectors form
a finite downset. He then proves a weighted mean inequality for arbitrary
finite downsets in \(\mathbb N^d\).[^zhai] In the current notation and with
\(d=3\), that inequality supplies the nonnegative baseline for the moment
deficit. The proposed proof needs a quantified improvement over that baseline.

Hellus, Rechenauer, and Waldi explicitly recast the preferred representatives
as the complement of an Artinian monomial ideal. Their Proposition 2.3
identifies the excluded monomials with an initial ideal; Proposition 2.5 gives
the periodic residue-lattice tiling; and Proposition 2.6 gives the relevant
support restriction on minimal excluded points.[^hrw] These are direct
predecessors of facts F1 and F3 in the proof outline.

The reconstruction adopts the second approach: short self-contained proofs,
with explicit attribution and a theorem-by-theorem source map, now appear in
[`paper/foundations.md`](../paper/foundations.md).

### 4.2 The Apéry moment identity

The identity

\[
  g=\frac1m\sum_{w\in\operatorname{Ap}(S,m)}w-\frac{m-1}{2}
\]

is the classical Apéry-set genus formula; standard background is available in
Rosales and García-Sánchez's monograph.[^book] Combining it with the chosen
factorizations yields the repository's exact identity

\[
  mW_4(S)=A D_0-m(m-1).
\]

The algebraic rearrangement may be presented as a lemma of this paper, but the
underlying genus formula and the downset framework must be attributed.

### 4.3 Residue collisions and minimal exclusions

The current proof uses the following geometric consequences: a minimal
excluded point and the chosen point in the same residue class have disjoint
support; two minimal exclusions that overlap in a coordinate cannot carry the
same residue; and there is at most one full-support minimal exclusion. These
are essentially the embedding-dimension-four specialization of the lattice
and support structure in Hellus--Rechenauer--Waldi, especially Proposition
2.6.[^hrw]

The paper should isolate any genuinely stronger clause. If no clause is
stronger, F3 should be a cited proposition rather than a new lemma.

### 4.4 Kunz coordinates, Apéry posets, and geometric models

Kunz coordinates and Kunz polyhedra provide a different finite-dimensional
model of numerical semigroups of fixed multiplicity. Bruns et al. connect
faces to Apéry posets and reduce fixed-\(m\) verification to rational
polyhedral feasibility.[^bruns] That route supplies the \(m\le19\) boundary
but is not the same computation as the repository's enumeration of generator
triples for \(20\le m\le29\). The eventual paper must explain why the latter
search is exhaustive and why extending the published Kunz-cone computation
was not used instead.

There is also an established L-shape literature for factorizations in
embedding dimension four. Aguiló-Gost, García-Sánchez, and Llena show that the
number of associated L-shapes can be arbitrarily large in embedding dimension
four.[^lshapes] Chomicz's 2026 preprint gives a three-dimensional geometric
procedure for obtaining Apéry sets of arbitrary four-generated numerical
semigroups and applies it to special families.[^chomicz] It does not claim
Wilf's conjecture in embedding dimension four. It is nevertheless close enough
in geometry and timing that it must be discussed and compared explicitly.

### 4.5 What Chomicz changes in the present strategy

Chomicz describes an Apéry set by deleting upper orthants in
\(\mathbb N^3\) along relations whose labels are positive multiples of a
distinguished generator. Theorem 2.2 gives a universal relation-deletion
description. Propositions 2.5 and 2.8 construct three-dimensional L-shapes in
the main and exceptional relation configurations, and Proposition 2.11
characterizes when the L-shape is unique by equality of the ordinary and
distinguished-generator-positive pure relation orders.[^chomicz]

These results clarify the geometry but do not currently remove a lemma from
the proposed proof:

1. The lexicographic exponent set already has the two properties used
   throughout: it is a lower ideal and contains exactly one representative of
   every Apéry residue. Zhai and Hellus--Rechenauer--Waldi provide a shorter,
   more direct source for those precise facts.
2. Chomicz's relation dichotomy may require rearranging all four generators.
   The proof here must distinguish the multiplicity \(m\), since
   \(|\operatorname{Ap}(S,m)|=m\),
   \(\max\operatorname{Ap}(S,m)=c+m-1\), and \(A\ge m+1\) drive the moment
   normalization. Reordering away from \(m\) would therefore cost more than it
   saves.
3. Choosing a different L-shape cannot change the weighted moment:
   \(a\cdot\sum_{x\in T}x\) is the sum of the Apéry elements for every choice of
   their factorizations. It can change the corners and the auxiliary centroid
   witnesses, so nonuniqueness remains a possible way to simplify a future
   geometric proof, not the current numerical inequality itself.

The useful new research target is in B5. All 431 lower ideals for which the
local two-step witness fails were tested against necessary residue-relation
conditions. None can be a genuine Apéry L-shape: 199 fail using only the full
corner and the three axes, and each remaining shape fails after adding one
mixed corner and its complementary axis. This is consistent with Chomicz's
relation-deletion picture and suggests seeking a structural proof that an
actual Apéry L-shape always has the local witness. Until such a proof exists,
the manuscript should retain the analytic axis witness instead of adding a
second modular enumeration. The exact assessment and reproducible exploratory
check are in [`research/chomicz-assessment.md`](../research/chomicz-assessment.md).

### 4.6 Chordal graphs and clique trees

The no-full-corner decomposition uses the standard fact that the maximal
cliques of a finite connected chordal graph can be arranged in a tree so that
the cliques containing any fixed graph vertex form a connected subtree. This
is the clique-tree form of the classical subtree characterization of chordal
graphs associated with Gavril.[^gavril] The survey did not find the
repository's application—building the compatibility graph of coordinate
levels and deriving a central box with at most three monotone horns—in the
reviewed numerical-semigroup or chordal-graph sources. It remains proposed new
content pending the L3 refresh and must not yet be presented as a priority
claim.

The reconstructed
[`central-box/three-horn note`](../paper/central-box-horns.md) includes a
short proof of the finite clique-tree lemma. The published graph theorem is
therefore attributed as an upstream structural source, while the lower-ideal
decomposition is proved within the artifact.

## 5. Other reductions and recent work

Moscariello and Sammartano prove an asymptotic result for fixed
\(\lceil m/e\rceil\), subject to restrictions on prime divisors of \(m\).
[^mosc-samm] Chatterjee and Narula's 2026 paper replaces that arithmetic
condition by \(\gcd(m,a_2)=1\) and improves the numerical threshold.[^chatterjee]
These results cover substantial infinite families but not every \(e=4\)
semigroup.

Spirito treats semigroups whose second generator is large relative to \(c\)
and \(m\).[^spirito] D'Anna and Moscariello give bounds in terms of \(e\) and
\(n\), as well as another proof for almost-symmetric semigroups.[^danna]
Eliahou's divset method proves Wilf under \(m\mid c\) and \(4e\ge m\).
[^divsets] Divsets are especially relevant conceptually because they are
divisor-closed monomial models, but for \(e=4\) their published numerical
threshold lies within the already known \(m\le19\) range.

Delgado, Kumar, and Marion derive sufficient conditions from the number of
elements in the first Kunz layer and study asymptotics by maximum primitive.
[^maximum-primitive] Yang and Zhang's April 2026 preprint develops first- and
cumulative-Kunz-layer criteria.[^first-layer] If
\(\eta=|S\cap(m,2m)|\), then \(\eta\le3\) when \(e=4\), since every element of
that interval is primitive. Consequently the broad first-layer criteria do
not reach the hard range \(m\ge20\).

Marashdeh's August 2026 preprint gives new type bounds and an exact
conductor-free decomposition of the Wilf number.[^marashdeh] It does not claim
the \(e=4\) case. A direct comparison with the moment identity finds that its
proved type bound does not supply the required factor of \(n\) in the
high-type range, while
the conjectural inequality that would close the gap is pointwise stronger
than Wilf's inequality. The classical type result does nevertheless give a
free geometric preprocessing rule: a preferred exponent ideal with at most
three coordinatewise maxima has type at most three and is already settled.
The [focused L2 audit](published-reduction-comparison.md) records the exact
calculation and its consequences for every branch.

Chomicz's September 2026 preprint relates the type \(t\) and minimal-
presentation cardinality \(\eta\) in embedding dimension four by
\(4t+5\ge\eta\ge t-11\).[^chomicz-type] The present route has no independent
bound on \(\eta\), so this result does not yield a new Wilf subcase or alter
the earlier L-shape assessment.

## 6. Attribution and novelty map

This table is the working rule for drafting. “Proposed new content” means only
that no match was found in this survey; it is not yet a defensible priority
claim.

| Component in this repository | Current attribution decision |
|---|---|
| Wilf inequality and notation | Wilf; use standard modern notation. |
| Apéry genus identity | Classical; cite a standard numerical-semigroup source. |
| Lexicographically preferred Apéry factorizations | Attribute to Zhai and Hellus--Rechenauer--Waldi. |
| Preferred representatives form a finite lower ideal | Attribute to Zhai; also cite the monomial-ideal formulation of Hellus--Rechenauer--Waldi. |
| Weighted mean inequality for a finite lower ideal | Attribute to Zhai. |
| Residue-lattice tiling and support/exclusion lemma | Attribute to Hellus--Rechenauer--Waldi. |
| Kunz/Apéry-poset verification through \(m=19\) | Bruns et al.; Kliem--Stump. |
| Disposal of exponent ideals with at most three maxima | Fröberg--Gottlieb--Häggkvist, plus the elementary comparison between Apéry-poset and coordinatewise maxima. |
| Three-dimensional L-shape context and relation-deletion construction | Aguiló-Gost--García-Sánchez--Llena; Chomicz. The proof retains the canonical lexicographic L-shape. |
| Clique-tree theorem for chordal graphs | Attribute the standard graph theorem to Gavril; retain a self-contained proof of the needed finite form. |
| Central-box/three-horn decomposition | Proposed new lower-ideal application of the clique-tree theorem; prove it explicitly and avoid a priority claim before L3. |
| Exact moment-deficit reformulation | Short derived lemma; cite its classical and Zhai inputs. |
| Positive surplus estimates for three-dimensional lower ideals | Proposed new content; audit branch by branch. |
| Seven-case geometric partition | Proposed new content; search terminology and adjacent extremal results before claiming novelty. |
| Finite certificates attached to the branches | New computational artifact if independently reproduced and fully specified. |

## 7. Consequences for reconstruction

The literature suggests the following order, before any TeX manuscript is
written:

1. Independently review the self-contained reconstruction of F1--F3 in
   `paper/foundations.md`, retaining only any genuinely new strengthening.
2. Use Proposition 4.4 of `paper/foundations.md` as the baseline and formulate
   one “surplus theorem” that contains exactly the new burden.
3. Apply all known reductions first: \(m\ge20\), \(c>3m\), \(n\ge13\), and
   \(t\ge4\). Test whether the Marashdeh decomposition gives more.
4. Re-examine the seven cases for overlap. In particular, look for a single
   structural inequality that replaces several shape enumerations.
5. Keep the fixed-multiplicity search and the lower-ideal searches as separate
   lemmas with separate checkers. Their exhaustiveness arguments are
   mathematically different.
6. Ask at least two numerical-semigroup specialists to review the attribution
   map and the claimed gap in the literature before a public priority claim.

This order should reduce both exposition and computation. It also prevents a
long polished paper from being built around a lemma that is already available
in stronger published form.

## 8. Computation and proof verification

The literature contains two useful precedents for computational reporting:
the Kunz-cone verification through multiplicity 19 and the numerical-semigroup
tree verification through genus 100.[^bruns][^kliem][^genus100] Both state the
mathematical reduction separately from implementation. This repository should
do the same for each retained computation:

- a theorem-level input/output specification;
- a proof that the generated objects exhaust the stated finite class;
- exact arithmetic only;
- a small, deterministic implementation with pinned build instructions;
- hashes or canonical summaries of certificates;
- an independent replay checker that is simpler than the generator; and
- recorded counts treated as diagnostics, never as the proof of exhaustion.

A full formalization should wait until the mathematical route stabilizes.
There is now a directly relevant starting point: Bartoletti, Bonzio, and
Ferrara have formalized numerical semigroups and certified computations of
gaps, small elements, Apéry sets, multiplicity, conductor, and Frobenius number
in Rocq.[^rocq] A 2026 Lean development around Fel's conjecture shows that
research-level numerical-semigroup algebra can also be packaged with a machine
checked proof, although it does not supply a general numerical-semigroup
library for the present argument.[^fel]

The highest-value formal-verification target here is not the entire manuscript
at first. It is the narrow interface between mathematics and computation:

1. formalize or conventionally prove F1--F3 and the moment identity;
2. specify finite shape/certificate datatypes;
3. verify each certificate with a very small trusted checker; and
4. only then decide whether porting the analytic surplus lemmas to Rocq or Lean
   is worth the cost.

An independently written checker plus human review is more urgent than a large
formalization generated from the same AI-produced proof.

## 9. Responsible presentation and priority

The final paper and repository should state plainly that AI systems were used
to discover, reorganize, and implement portions of the argument, while named
human authors take responsibility for every claim. The historical archive
should remain available, but the reviewable artifact should distinguish:

- mathematical statements and proofs;
- machine-verification specifications and code;
- search logs and certificates; and
- historical AI transcripts or intermediate manuscripts.

Before submission, the authors should obtain independent mathematical review,
repeat the literature search, compare directly with the closest papers, and
contact authors of the most directly upstream work where appropriate. Until
that happens, repository language should say “proposed proof,” not “proof of
the conjecture.”

## 10. Search method and known limitations

### Selected-proof refresh, 2026-09-17 (L3)

The final selected route was compared with fresh primary-source searches
for Wilf in embedding dimension four, four generators, weighted lower
ideals, central boxes/horns, and the finite-to-continuous constant \(5/42\).
No earlier uniform four-generator proof or directly matching horn/surplus
statement was located. This is a bounded negative search result, not a
priority certification.

The refreshed source versions are Zhai's original preprint,
Hellus--Rechenauer--Waldi v2, Chomicz's L-shape v3 and type/presentation v1,
Marashdeh v1, and Delgado--Kumar--Marion v2.
The inherited Apéry, weighted-moment, support, and clique-tree ingredients
remain explicitly attributed.[^zhai][^hrw][^chomicz][^chomicz-type][^marashdeh][^maximum-primitive][^gavril]
Published Bruns Theorem 4.3 and Kliem--Stump Proposition 6.9 remain the
only selected external computational premise.[^bruns][^kliem]
The first-layer results still lie below the retained hard multiplicity
range; the unreviewed first-Kunz-layer preprint is not used as a theorem
input.[^first-layer]

One additional 2026 primary source, Hellus--Hübl--Rechenauer, concerns
semigroups whose largest minimal generator equals \(2g+1\) and related
families. Its stated special-family scope supplies no demonstrated uniform
replacement for this route.[^largest-generator]
No new skip rule is inferred from that abstract.
The standalone preliminary proof retains only references relevant to its
chosen argument; this broader survey remains a research record, not an
extra reader dependency.

### Earlier search coverage and remaining limitations

The search combined backward references from Delgado's survey and recent Wilf
papers with forward searches for “Wilf conjecture,” “embedding dimension
four,” “four generators,” “Apéry set,” “Kunz,” “lower ideal,” “divset,” and
formal verification. Journal pages, DOI records, arXiv abstracts/full text,
and author-hosted manuscripts were preferred over secondary summaries. Recent
searches included arXiv and web-indexed publications through 2026-09-11,
with the focused refreshes dated above.

Limitations remain. MathSciNet and zbMATH citation graphs were not exhaustively
audited; not every paywalled paper was read line by line; and very recent or
unindexed work may be missing. The propositions attributed to
Hellus--Rechenauer--Waldi and the comparison with Chomicz should be checked
against final pagination when the bibliography is converted to BibTeX.

## Sources

[^wilf]: Herbert S. Wilf, “A Circle-of-Lights Algorithm for the
    ‘Money-Changing Problem’,” *American Mathematical Monthly* **85** (1978),
    562--565. [doi:10.1080/00029890.1978.11994639](https://doi.org/10.1080/00029890.1978.11994639).

[^fgh]: Ralf Fröberg, Christian Gottlieb, and Roland Häggkvist, “On numerical
    semigroups,” *Semigroup Forum* **35** (1987), 63--83.
    [doi:10.1007/BF02573091](https://doi.org/10.1007/BF02573091).

[^dobbs]: David E. Dobbs and Gretchen L. Matthews, “On a question of Wilf
    concerning numerical semigroups,” in *Focus on Commutative Rings Research*
    (Nova Science, 2006), 193--202.
    [Author-hosted manuscript](https://personal.math.vt.edu/gmatthews/wilf.pdf).

[^delgado-survey]: Manuel Delgado, “Conjecture of Wilf: a survey,” in
    *Numerical Semigroups*, Springer INdAM Series **40** (2020), 39--62.
    [arXiv:1902.03461](https://arxiv.org/abs/1902.03461).

[^kaplan]: Nathan Kaplan, “Counting numerical semigroups by genus and some
    cases of a question of Wilf,” *Journal of Pure and Applied Algebra* **216**
    (2012), 1016--1032.
    [doi:10.1016/j.jpaa.2011.10.038](https://doi.org/10.1016/j.jpaa.2011.10.038).

[^sammartano]: Alessio Sammartano, “Numerical semigroups with large embedding
    dimension satisfy Wilf's conjecture,” *Semigroup Forum* **85** (2012),
    439--447. [arXiv:1111.1863](https://arxiv.org/abs/1111.1863).

[^macaulay]: Shalom Eliahou, “Wilf's conjecture and Macaulay's theorem,”
    *Journal of the European Mathematical Society* **20** (2018), 2105--2129.
    [arXiv:1703.01761](https://arxiv.org/abs/1703.01761).

[^graph]: Shalom Eliahou, “A graph-theoretic approach to Wilf's conjecture,”
    *Electronic Journal of Combinatorics* **27** (2020), Paper 2.15.
    [arXiv:1909.03699](https://arxiv.org/abs/1909.03699).

[^left12]: Shalom Eliahou and Daniel Marín-Aragón, “On numerical semigroups
    with at most 12 left elements,” *Communications in Algebra* **49** (2021),
    2402--2422.
    [doi:10.1080/00927872.2021.1871621](https://doi.org/10.1080/00927872.2021.1871621).

[^bruns]: Winfried Bruns, Pedro A. García-Sánchez, Christopher O'Neill, and
    Dane Wilburne, “Wilf's conjecture in fixed multiplicity,” *International
    Journal of Algebra and Computation* **30** (2020), no. 4, 861--882.
    [doi:10.1142/S021819672050023X](https://doi.org/10.1142/S021819672050023X);
    [arXiv:1903.04342](https://arxiv.org/abs/1903.04342).

[^kliem]: Jonathan Kliem and Christian Stump, “A New Face Iterator for
    Polyhedra and for More General Finite Locally Branched Lattices,”
    *Discrete & Computational Geometry* **67** (2022), 1147--1173.
    [doi:10.1007/s00454-021-00344-x](https://doi.org/10.1007/s00454-021-00344-x);
    [arXiv:1905.01945](https://arxiv.org/abs/1905.01945).

[^genus100]: Manuel Delgado, Shalom Eliahou, and Jean Fromentin, “A
    verification of Wilf's conjecture up to genus 100,” *Journal of Algebra*
    **664** (2025), 150--163.
    [arXiv:2310.07742](https://arxiv.org/abs/2310.07742).

[^divsets]: Shalom Eliahou, “Divsets, numerical semigroups and Wilf's
    conjecture,” *Communications in Algebra* **53** (2025), 2025--2048.
    [doi:10.1080/00927872.2024.2428807](https://doi.org/10.1080/00927872.2024.2428807).

[^danna]: Marco D'Anna and Alessio Moscariello, “Bounds for invariants of
    numerical semigroups and Wilf's conjecture,” *Mathematische Zeitschrift*
    **304** (2023), article 35.
    [arXiv:2208.14090](https://arxiv.org/abs/2208.14090).

[^barucci]: Valentina Barucci, “On propinquity of numerical semigroups and
    one-dimensional local Cohen--Macaulay rings,” in *Commutative Algebra and
    Its Applications* (De Gruyter, 2009), 49--60.
    [doi:10.1515/9783110213188.49](https://doi.org/10.1515/9783110213188.49).

[^zhai]: Alex Zhai, “An asymptotic result concerning a question of Wilf,”
    [arXiv:1111.2779](https://arxiv.org/abs/1111.2779).

[^hrw]: Michael Hellus, Anton Rechenauer, and Rolf Waldi, “Variants on a
    question of Wilf,” [arXiv:1804.06141](https://arxiv.org/abs/1804.06141).

[^book]: J. C. Rosales and P. A. García-Sánchez, *Numerical Semigroups*,
    Developments in Mathematics **20**, Springer, 2009.
    [doi:10.1007/978-1-4419-0160-6](https://doi.org/10.1007/978-1-4419-0160-6).

[^lshapes]: F. Aguiló-Gost, P. A. García-Sánchez, and D. Llena, “On the
    number of L-shapes in embedding dimension four numerical semigroups,”
    *Discrete Mathematics* **338** (2015), 2168--2178.
    [arXiv:1505.01464](https://arxiv.org/abs/1505.01464).

[^chomicz]: Kazimierz Chomicz, “On numerical semigroups with embedding
    dimension four,” [arXiv:2604.25653](https://arxiv.org/abs/2604.25653),
    version 3, 2026.

[^mosc-samm]: Alessio Moscariello and Alessio Sammartano, “On a conjecture by
    Wilf about the Frobenius number,” *Mathematische Zeitschrift* **280**
    (2015), 47--53.
    [arXiv:1408.5331](https://arxiv.org/abs/1408.5331).

[^chatterjee]: Tapas Chatterjee and Palak Narula, “A note on Wilf's
    Conjecture,” *Semigroup Forum* (2026).
    [doi:10.1007/s00233-026-10640-8](https://doi.org/10.1007/s00233-026-10640-8).

[^spirito]: Dario Spirito, “Wilf's conjecture for numerical semigroups with
    large second generator,” *Journal of Algebra and Its Applications* **20**
    (2021), 2150197.
    [arXiv:1710.09245](https://arxiv.org/abs/1710.09245).

[^maximum-primitive]: Manuel Delgado, Neeraj Kumar, and Claude Marion, “On
    counting numerical semigroups by maximum primitive and Wilf's conjecture,”
    [arXiv:2501.04417](https://arxiv.org/abs/2501.04417), version 2, 2026.

[^first-layer]: Yaoran Yang and Yutong Zhang, “Wilf's Conjecture from the First
    Kunz Layer,” Preprints.org (2026), not peer reviewed.
    [doi:10.20944/preprints202604.0551.v1](https://doi.org/10.20944/preprints202604.0551.v1).

[^marashdeh]: Mohammad F. Marashdeh, “An upper bound for the type of a
    numerical semigroup, and a reduction of Wilf's conjecture,”
    [arXiv:2608.12531](https://arxiv.org/abs/2608.12531), 2026.

[^chomicz-type]: Kazimierz Chomicz, “The type and cardinality of minimal
    presentations of numerical semigroups with embedding dimension four,”
    [arXiv:2609.04000](https://arxiv.org/abs/2609.04000), version 1, 2026.

[^gavril]: Fănică Gavril, “The intersection graphs of subtrees in trees are
    exactly the chordal graphs,” *Journal of Combinatorial Theory, Series B*
    **16** (1974), 47--56.
    [doi:10.1016/0095-8956(74)90094-X](https://doi.org/10.1016/0095-8956(74)90094-X).

[^rocq]: Massimo Bartoletti, Stefano Bonzio, and Marco Ferrara, “Certified
    Algorithms for Numerical Semigroups in Rocq,” in *CICM 2025*, LNCS 16136,
    340--356. [arXiv:2505.23205](https://arxiv.org/abs/2505.23205).

[^fel]: Evan Chen et al., “Fel's Conjecture on Syzygies of Numerical
    Semigroups,” [arXiv:2602.03716](https://arxiv.org/abs/2602.03716), 2026;
    accompanying [Lean repository](https://github.com/AxiomMath/fel-polynomial).

[^largest-generator]: Michael Hellus, Reinhold Hübl, and Anton Rechenauer,
    “Numerical semigroups with \(a_e=2g+1\),”
    [arXiv:2604.21948](https://arxiv.org/abs/2604.21948), version 1, 2026.
