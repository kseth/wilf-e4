# The published multiplicity bound through 19

## Status and conclusion

This note completes roadmap task L1. It audits the two published inputs used
to remove multiplicities at most \(19\) from the proposed proof.

**Audit date:** 2026-09-12. Statements and metadata were checked against the
two versions of record, with their final arXiv revisions used to identify
numbering differences.

The exact combined statement available from the literature is:

> **Published multiplicity theorem.** Every numerical semigroup \(S\) with
> multiplicity \(m(S)\le 19\) satisfies Wilf's inequality
>
> \[
> c(S)\le e(S)|S\cap[0,c(S))|.
> \]

This is a theorem about **all numerical semigroups** in the indicated
multiplicity range. It is not restricted to embedding dimension four, to a
special class of semigroups, or to an additional arithmetic hypothesis.
Consequently it applies directly to the \(e(S)=4\) branch of this project.

The range is the union of two separately published results:

- Bruns, García-Sánchez, O'Neill, and Wilburne prove all \(m\le18\) in
  Theorem 4.3 of the version of record.
- Kliem and Stump prove \(m=19\) in Proposition 6.9 of the version of record.

No interpolation is involved: the first result covers the interval through
18 and the second covers the remaining value 19.

## 1. Multiplicities at most 18

The authoritative bibliographic record is:

> Winfried Bruns, Pedro A. García-Sánchez, Christopher O'Neill, and Dane
> Wilburne, “Wilf's conjecture in fixed multiplicity,” *International Journal
> of Algebra and Computation* **30** (2020), no. 4, 861--882.
> [doi:10.1142/S021819672050023X](https://doi.org/10.1142/S021819672050023X).

The [author-hosted version of record](https://www.home.uni-osnabrueck.de/wbruns/brunsw/pdf-article/S021819672050023X-1.pdf)
states in Theorem 4.3 that every numerical semigroup \(S\) with
\(m(S)\le18\) is Wilf. The paper was published on 13 March 2020; its accessible
[arXiv version](https://arxiv.org/abs/1903.04342) is arXiv:1903.04342v2,
dated 20 July 2019.

The theorem is computer-assisted. Algorithm 4.1 reduces a hypothetical
non-Wilf semigroup of fixed multiplicity to an integer-feasibility problem on
a face of the relaxed Kunz polyhedron, with a choice of maximal Apéry-poset
element determining the Frobenius residue. The computation enumerates the
relevant face orbits, discards faces already covered by the type and
high-embedding-dimension criteria, and proves the remaining violation regions
empty. The implementation uses a modified version of Normaliz and the unit
group symmetry of the Kunz cone.

Two scope cautions matter for later citation:

1. The theorem is numbered **4.3**, not 4.4. The latter is the authors'
   conjecture that the same feasibility regions are empty for all
   multiplicities.
2. The paper reports input files and some cone data for \(m=19\), but its
   theorem stops at \(m=18\). File availability or an extreme-ray count for
   \(m=19\) is not a proof of the \(m=19\) case.

## 2. Multiplicity 19

The authoritative bibliographic record is:

> Jonathan Kliem and Christian Stump, “A New Face Iterator for Polyhedra and
> for More General Finite Locally Branched Lattices,” *Discrete &
> Computational Geometry* **67** (2022), 1147--1173.
> [doi:10.1007/s00454-021-00344-x](https://doi.org/10.1007/s00454-021-00344-x).

The [open-access version of record](https://link.springer.com/article/10.1007/s00454-021-00344-x)
was published on 18 March 2022. Its Proposition 6.9 states that Wilf's
conjecture holds for \(m=19\). The abstract and Section 6 make the quantifier
explicit: the result concerns all numerical semigroups of multiplicity 19.
The corresponding [arXiv record](https://arxiv.org/abs/1905.01945) is
arXiv:1905.01945v2, dated 17 January 2020.

Kliem--Stump do not merely infer \(m=19\) from the Bruns et al. theorem. They
reuse its Kunz-face feasibility criterion and replace the face-lattice
enumeration by their memory-efficient depth-first iterator. They enumerate
bad face orbits under the unit-group action. Besides the two filters recorded
by Bruns et al., they use Eliahou's theorem that \(3e(S)\ge m(S)\) implies
Wilf; for the remaining orbits with \(3e<m\), they check that the associated
violation regions are empty. That computation yields Proposition 6.9.

The proposition is numbered **6.9** in the published article but **6.8** in
arXiv:1905.01945v2. The final manuscript should cite the published numbering
and may mention the arXiv numbering only when directing a reader to that
version.

## 3. Dependency and trust decision

The proof branch used in this repository is therefore simply

\[
\begin{array}{ll}
m\le18 &: \text{Bruns et al., Theorem 4.3},\\
m=19   &: \text{Kliem--Stump, Proposition 6.9}.
\end{array}
\]

Both are peer-reviewed, computer-assisted results and enter the project as
external inputs `[E]`. Under the repository's
[verification trust policy](../verification/trust-policy.md), their historical
computations are not relabeled as internal `[C]` components and are not part
of our eventual minimal proof-code package. Reproducing them could provide
additional assurance, but it is not a logical prerequisite for using the
published theorems. The manuscript must accurately describe their
computer-assisted nature and must not suggest that this project independently
replayed them.

This decision keeps the computational boundary concise: our finite
generator-box specification begins only at \(m=20\).
