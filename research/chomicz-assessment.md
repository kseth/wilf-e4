# Assessment of Chomicz's L-shape construction

## Verdict

Chomicz's relation-based description does not presently replace a branch or
computed lemma in the proposed proof. It supplies the right geometric
language, a useful description of boundary relations, and a possible future
freedom to choose a favorable L-shape. The proof should cite it where the
three-dimensional L-shape is introduced, but should continue to use the
canonical lexicographic representatives and the direct results of Zhai and
Hellus--Rechenauer--Waldi for its formal inputs.

Primary source: Kazimierz Chomicz, “On numerical semigroups with embedding
dimension four,” [arXiv:2604.25653](https://arxiv.org/abs/2604.25653), version
3, 2026.

## The theorem-level comparison

| Chomicz result | Possible use here | Decision |
|---|---|---|
| Lemma 2.1 and Theorem 2.2: delete upper orthants arising from positive relations | Construct all Apéry exponent cubes and explain excluded regions | Geometric interpretation only; the universal procedure is longer than the initial-ideal route to F1 and F3 |
| Propositions 2.5 and 2.8: construct an L-shape in the principal and paired-relation cases | Replace the lexicographic representative set | Do not replace it: both constructions give the same proof interface, while lexicographic choice is canonical |
| Lemma 2.7: relation dichotomy after arranging the four generators | Simplify the seven-branch case split | Not directly usable because the arrangement need not preserve the distinguished generator as the multiplicity |
| Proposition 2.11: criterion for uniqueness of the L-shape | Choose among shapes to improve a centroid witness | Promising exploratory direction, but it cannot change the weighted moment and no witness-monotonicity theorem is supplied |
| Sections 3--5: Betti elements, catenary degree, and special families | Supply a uniform Wilf estimate | No direct contribution to the present general inequality |

The paper contains no Wilf-conjecture result. Its closing problems also mark
limits of the current relation analysis, so it should not be cited as though
it supplied an embedding-dimension-four reduction.

## Choice-invariance of the quantity being bounded

Let (T) contain one exponent vector (x(w)) for each
(w\in\operatorname{Ap}(S,m)), where (a\cdot x(w)=w). Then

\[
  a\mathbin\cdot\sum_{x\in T}x
  =\sum_{w\in\operatorname{Ap}(S,m)}w.
\]

Consequently (b\cdot s), and hence the moment deficit (D_0), is the same for
every L-shape of this fixed Apéry set. A different L-shape may change
(R), its minimal excluded points, and the witnesses (U_2) and (G). Thus the
only plausible simplification from nonuniqueness is to choose a geometry on
which the invariant bound is easier to certify.

Chomicz does not prove that one of the available L-shapes optimizes any of
these witnesses. Introducing a choice over L-shapes now would therefore add a
selection lemma without removing an existing obligation.

## B5 residue probe

The B5 enumeration has 431 shapes for which (U_2(T)<m) and the analytic axis
witness (G) is used. A separate exact probe applies necessary conditions for a
genuine Apéry L-shape:

1. the three generator residues modulo (m) are nonzero and pairwise distinct;
2. the full-support minimal corner has residue zero;
3. labels on the three coordinate axes are injective; and
4. the representative sharing a residue with a mixed minimal corner lies on
   the complementary coordinate axis (the support condition in F3).

The result is:

| outcome | shapes |
|---|---:|
| excluded by conditions 1--3 | 199 |
| survive 1--3 but are excluded by one mixed corner in condition 4 | 232 |
| unresolved | 0 |

The standard library-only checker is
[`check_b5_residue_fallbacks.py`](check_b5_residue_fallbacks.py). Run it from
the repository root with

```sh
python3 research/check_b5_residue_fallbacks.py
```

This is an exploratory audit, not a retained proof dependency. Replacing (G)
by this search would not reduce the amount of machine verification. Its value
is the sharper analytic target:

> Prove that every residue-compatible Apéry L-shape in the B5 domain satisfies
> (U_2(T)\ge m).

One possible route is to show directly that (U_2<m) forces precisely the
corner/axis incompatibility detected above, phrased in Chomicz's positive-
relation language. Until then, the existing local-or-axis theorem is the
cleaner proof interface.
