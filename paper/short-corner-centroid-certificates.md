# Exact centroid certificates for the short-corner low-height branch

## Status and purpose

This note completes roadmap task B4.4. It gives the exact acceptance
predicate for a centroid certificate and proves that an accepted certificate
covers every real weight vector \(w_i\ge1\) and every height allowance.
Together with the [B4.3 profile coverage proof](short-corner-profile-specification.md),
it specifies how exact point witnesses prove the low-height target.

The certificate is just a nonnegative rational combination of points.
Its slack vector is derived, not trusted. Clearing denominators reduces
verification to integer sums, and any valid certificate can be replaced by
one using at most three maximal points.

These are analytic semantics and conditional simplifications. They do not
prove that every eligible profile has a valid certificate, promote the
historical archive under V0, or discharge R4b.
[D4](../research/b4-simplification-decision.md) selects deterministic local
checks and two inline witnesses instead of replaying the archived dual list.
Sections 5--6 retain the legacy-list checking specification as an alternative,
not an additional selected proof dependency.

## 1. The local acceptance predicate

Let \(T\subseteq\mathbb N^3\) be a finite nonempty set, and write

\[
m=|T|,\qquad s=\sum_{x\in T}x.
\tag{1}
\]

In B4-low-FV, \(T\) is reconstructed from an eligible B4.3 profile key;
the local argument itself does not require lower closure or residue labels.

A rational witness is a finite list of distinct points \(x^{(j)}\in T\)
and coefficients \(y_j\in\mathbb Q_{\ge0}\). Define its residual vector by

\[
\beta_i=\sum_jy_jx_i^{(j)}-4s_i
\qquad(i=1,2,3).
\tag{2}
\]

The exact predicate is

\[
\boxed{
\sum_jy_j=3m,\qquad
\beta_i\ge0\ (i=1,2,3),\qquad
\sum_{i=1}^3\beta_i\ge m-1.
}
\tag{3}
\]

Point membership, coefficient nonnegativity, and every equality and
inequality in (3) must be checked exactly. Sparse-list duplicates are
rejected as noncanonical, although combining their coefficients would be a
mathematically equivalent witness. Zero coefficients are harmless; their
listed points must still belong to \(T\).

### Theorem 1.1 (certificate soundness)

If the local predicate holds, then, for all real \(w_i\ge1\) and all real
\(Q\ge\max_{x\in T}w\cdot x\),

\[
D_T(w,Q):=3mQ-4w\cdot s\ge m-1.
\tag{4}
\]

#### Proof

The mass identity and the definition of \(\beta\) give the exact decomposition

\[
\boxed{
D_T(w,Q)=
\sum_jy_j\bigl(Q-w\cdot x^{(j)}\bigr)
+\sum_{i=1}^3\beta_i(w_i-1)
+\sum_{i=1}^3\beta_i.
}
\tag{5}
\]

Each term in the first two sums is nonnegative. The last sum is at least
\(m-1\) by (3). This proves (4). ∎

No rationality of \(w,Q\), upper bound on \(Q\), optimization theorem, or
numerical tolerance is used. The weak endpoints \(w_i=1\), attained height
\(Q=\max_Tw\cdot x\), \(\beta_i=0\), and total residual \(m-1\) are all valid.

## 2. Why this is a centroid witness

The coefficients \(y_j/(3m)\) form a convex combination. Put

\[
\bar x=\frac sm,\qquad
q=\frac1{3m}\sum_jy_jx^{(j)}\in\operatorname{conv}(T).
\]

Then

\[
q=\frac43\bar x+\frac{\beta}{3m}.
\tag{6}
\]

Thus the witness supplies a point in the convex hull lying coordinatewise
above four thirds of the ordinary centroid, with total coordinate surplus
at least \((m-1)/(3m)\). Since \(Q\ge w\cdot q\), this is precisely the
geometric content of (4).

The word “dual” refers only to taking nonnegative combinations of the
constraints \(Q-w\cdot x\ge0\) and \(w_i-1\ge0\). The proof is the identity
(5); no claim about a solver optimum or strong duality is needed.

## 3. An equivalent integer predicate

Choose a positive integer \(d\) clearing the witness denominators, and put
\(n_j=dy_j\in\mathbb Z_{\ge0}\). Define

\[
r_i=\sum_jn_jx_i^{(j)}-4ds_i.
\]

The rational predicate (3) is equivalent to

\[
\boxed{
d\in\mathbb Z_{>0},\quad n_j\in\mathbb Z_{\ge0},\quad
\sum_jn_j=3md,\quad
r_i\ge0\ (i=1,2,3),\quad
\sum_ir_i\ge d(m-1).
}
\tag{7}
\]

Indeed \(r_i=d\beta_i\), so multiplying or dividing by \(d>0\) proves
equivalence. No requirement that \(d\) or the fractions be minimal is needed.
The corresponding integer identity is

\[
dD_T(w,Q)=
\sum_jn_j(Q-w\cdot x^{(j)})
+\sum_ir_i(w_i-1)+\sum_ir_i.
\tag{8}
\]

A future curated record therefore needs only its profile key, point list,
positive denominator \(d\), and nonnegative integers \(n_j\). The point set,
cardinality, first moment, residual, and lower bound are reconstructed.
Any retained integer checker must use arbitrary-precision arithmetic or
prove sufficient fixed-width bounds; no denominator bound is assumed here.
This is a format option, not a migration of the immutable archive.

## 4. Three maximal points suffice

### Proposition 4.1 (lossless certificate sparsification)

If \(T\) admits a rational witness satisfying (3), it admits one supported
on at most three points of \(K=\operatorname{Max}(T)\). Its residual may be
chosen coordinatewise at least as large as the original residual.

#### Proof

First move each listed point \(x\) to a maximal point \(k(x)\ge x\) of
the finite set \(T\), and combine coefficients with the same destination.
The mass is unchanged, while every coordinate of the weighted point sum
weakly increases. Thus the residual weakly increases and (3) is preserved.
Remove zero coefficients.

Suppose there are more than four positive coefficients. The vectors
\((1,x^{(j)})\in\mathbb Q^4\) are linearly dependent, so there is a nonzero
rational vector \(c\) with

\[
\sum_jc_j=0,\qquad \sum_jc_jx^{(j)}=0.
\tag{9}
\]

It has both positive and negative entries. With
\(t=\min_{c_j>0}y_j/c_j>0\), replace \(y_j\) by \(y_j-tc_j\).
All coefficients remain nonnegative and at least one becomes zero.
Both the mass and weighted point sum are preserved. Repeating this
elementary affine-dependence reduction leaves at most four points.
The same reduction applies to four affinely dependent points.

It remains to handle four affinely independent points. Their augmented
vectors form an invertible rational \(4\times4\) matrix. Therefore there
is a rational vector \(c\) satisfying

\[
\sum_{j=1}^4c_j=0,\qquad
\sum_{j=1}^4c_jx^{(j)}=(1,1,1).
\tag{10}
\]

Again \(c\) has both signs. Set
\(t=\min_{c_j<0}y_j/(-c_j)>0\), and replace \(y_j\) by \(y_j+tc_j\).
The coefficients remain nonnegative, at least one vanishes, and the mass
is unchanged. Each residual coordinate increases by \(t\). This gives a
valid certificate on at most three maximal points.

All operations are rational. No new supporting points are introduced
during reduction, and clearing denominators gives (7) if desired. ∎

The usual affine-dependence part is the elementary Carathéodory reduction
in three dimensions. The final diagonal move uses the fact that increasing
all three residual coordinates preserves the predicate.

This does not assert that every B4.3 profile has a witness. It says that an
already valid witness can be simplified. Legacy replay may accept any
finite support satisfying (3); a three-point restriction is optional unless
an explicitly checked compressed format is adopted.

## 5. Exact record checking and legacy alignment

A checker starts from the canonical B4.3 key, reconstructs \(T\), and
recomputes \(m,s\). It does not accept the serialized statistics as inputs
to (3). For a rational record, the essential tests are:

| Item | Required exact test |
|---|---|
| Profile key | Three six-entry integer vectors; all B4.3 eligibility conditions hold. |
| Point list | Distinct triples of nonnegative integers, all belonging to reconstructed \(T\). |
| Multipliers | Exact nonnegative rationals; mass is exactly \(3m\). |
| Residual | Compute exactly the three coordinates in (2); all are nonnegative. |
| Bound | The sum of those three residual coordinates is at least \(m-1\). |

Integers must be integers, not booleans or floating-point values.
Legacy rational fields are strings \(p\) or \(p/q\), where \(p\) is a
base-ten integer with an optional leading minus sign and \(q\) is a positive
base-ten integer. A loader rejects zero or negative
denominators, decimal/exponent encodings, missing fields, wrong dimensions,
and malformed data; it must not round or repair failed identities.
Duplicated JSON object members must be rejected rather than silently
overwritten.

The historical record has fields named \(\mathrm{rows}\),
\(\mathrm{m}\), \(\mathrm{sums}\), \(\mathrm{dual}\),
\(\mathrm{beta}\), and \(\mathrm{lower\_bound}\). Their meanings are:

- \(\mathrm{rows}\) is the canonical oriented profile key.
- Each \(\mathrm{dual}\) entry gives \(x^{(j)}\) and \(y_j\).
- The cached \(\mathrm{m}\) and three integer \(\mathrm{sums}\) must equal
  the reconstructed statistics.
- The cached \(\mathrm{beta}\) must contain **exactly three** rationals and
  equal (2) coordinate by coordinate.
- The cached \(\mathrm{lower\_bound}\) must equal the sum of that derived
  three-coordinate residual.

The historical producer minimizes the linear expression

\[
3mQ-4w\cdot s
\quad\text{subject to}\quad
Q-w\cdot x\ge0\ (x\in K),\quad w_i\ge1.
\tag{11}
\]

Using maximal points loses no height constraint: every point of \(T\)
lies below one and the weights are positive. Its solver marginals propose
the nonnegative \(y_j,\beta_i\). The mathematical acceptance conditions
are (2)--(3), not a floating-point success flag or an approximately equal
coefficient vector. SciPy, an optimum value, and the rational-reconstruction
heuristic are discovery tools only, not dependencies of an exact checker.

### A schema safeguard for the legacy replay alternative

The archived independent verifier checks the first three coordinate
identities but does not explicitly enforce that the stored
\(\mathrm{beta}\) list has length three. It then sums the whole list.
Without a strict schema check, extra nonnegative entries could inflate the
claimed bound without appearing in any coefficient identity.

For example, take \(T=\{0,e_1,e_2,e_3\}\), \(m=4\), \(s=(1,1,1)\), and
give each \(e_i\) multiplier four. The true residual is zero, so (3) fails.
A malformed cached vector \((0,0,0,3)\) would satisfy the weakened
three-coordinate checks and report bound three. But at \(w=(1,1,1)\),
\(Q=1\), the actual deficit is zero, not at least \(m-1=3\).
This toy set is not a B4 profile; it exhibits why the local predicate must
sum exactly the residual coordinates it has checked.

A structural inspection found exactly three cached residual entries in
every saved historical record. Thus this is a loader safeguard, not evidence
that the saved mathematical certificates are invalid. Any reinstated
legacy replay must nevertheless check the schema explicitly, alongside
the exact identities and coverage;
the historical checker is not promoted unchanged by this note.

## 6. Complete-family acceptance and conditional composition

A replay of the legacy dual-list alternative must:

1. generate every key in \(\mathcal F_5^{\ge30}\) from B4.3, without a
   maxima-count skip or an empirical cardinality cutoff;
2. validate record schemas and reject duplicate profile keys;
3. match exactly one record to each generated key, reconstruct its
   \(T,m,s\), and check the local predicate;
4. reject missing records, unused records, failed identities, unsupported
   encodings, or partial runs with a nonzero exit; and
5. produce the fresh replay and independent-check evidence required by
   [V0](../verification/trust-policy.md).

Correctness checks must be unconditional, or the runner must enforce that
all required assertions remain enabled.

Coverage is equality of the generated and checked key sets, not equality
of counts. The reported number 28,499, recorded margins, and stored
success flags are not substitutes for this check. A zero exact margin over
\(m-1\) is acceptable.

If those obligations are discharged, Theorem 1.1 proves B4-low-FV for the
entire profile family. B4.3 then covers every genuine low-height B4 ideal;
choosing \(w_i=a_i/A\) and \(Q=H\) gives \(D_0\ge m-1\).
The [final-arithmetic lemma](final-arithmetic.md) converts this to
\(W_4(S)\ge1\) for that low-height subcase.

The high-height theorem remains a separate obligation. No full B4 theorem
or completed low-height finite lemma is asserted at this stage.

## 7. Provenance and bounded diagnostics

The historical [producer](../artifacts/wilf_four_generators_review_package_2026-09-11/round5/interior_arithmetic/low_height_weighted_certificate.py)
and [independent verifier](../artifacts/wilf_four_generators_review_package_2026-09-11/round5/interior_arithmetic/verify_low_height_weighted.py)
use the same mathematical mass, coordinate, and residual-sum identities.
This reconstruction derives the residual, makes schema dimensions explicit,
and supplies the integer and sparse-point alternatives without modifying
the archive. These are standard nonnegative-constraint and convex-geometric
arguments, not new residue assumptions; L3 retains the final attribution
refresh.

On 2026-09-16, a structural inspection of the archived list found 28,499
records, each with three cached residual entries. Their listed supports
have sizes one, two, or three. This is schema/provenance evidence only,
not point-membership, coefficient, or family-coverage verification.

Bounded exact diagnostics also checked five archive records, at indices
0, 7,124, 14,249, 21,374, and 28,498, and four synthetic witnesses.
They verified the rational/integer equivalence and three-point reductions,
including both affine dependence and the independent four-point diagonal
move. The slack identity passed 1,728 rational weight/allowance tests, with
unit weights, attained heights, zero residual coordinates, and zero target
margin included. Twelve malformed or invalid inputs were rejected.
These samples are consistency evidence only; no complete dual or key-set
coverage replay was performed.
