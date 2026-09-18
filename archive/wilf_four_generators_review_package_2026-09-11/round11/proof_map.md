# Definitive dependency map for the proposed four-generator proof

11 September 2026. This note reconciles the full Round 8 argument with the stronger Round 10 local centroid lemma. It is a logical and editorial audit of the existing sources and completed records; no exhaustive calculation was rerun for this note. The result remains a proposed computer-assisted proof pending external mathematical review. The finite verifiers are ordinary exact-arithmetic programs, not a proof-assistant formalization.

## 1. Common definitions and the main theorem

**Proposed theorem.** Every minimally four-generated numerical semigroup \(S\), with conductor \(c\), satisfies

\[
W_4(S):=4|S\cap[0,c)|-c\ge0.
\]

Write \(S=\langle m,a_1,a_2,a_3\rangle\), with \(m\) the multiplicity. Let \(T\subset\mathbb N^3\) be the lexicographically preferred exponent representatives of \(\operatorname{Ap}(S,m)\). Put

\[
A=\min_i a_i\ge m+1,\quad b=a/A,\quad
s=\sum_{x\in T}x,\quad M=\max\operatorname{Ap}(S,m),\quad H=M/A,
\]
\[
D=3mM-4a\cdot s,\qquad D_0=D/A=3mH-4b\cdot s,
\qquad R=\max_{x\in T}|x|_1.
\]

Then \(|T|=m\), \(T\) is a lower ideal containing every coordinate unit, its labels represent all residues modulo \(m\) once, and

\[
\boxed{mW_4=AD_0-m(m-1).} \tag{1}
\]

A minimal excluded point and its included residue representative have disjoint support. Distinct minimal excluded points sharing a positive coordinate have different residues. Therefore **there is at most one full-support minimal excluded point**; if it exists, call it \(p\), and \(a\cdot p\equiv0\pmod m\).

Sources: `round8/audit_lowheight.md`, sections 1–2; `round8/audit_sixpoint.md`, sections 2–3; the standard genus identity at the start of `deliverables/wilf_four_generator_research_2026-09-10.md`.

## 2. The exhaustive and disjoint case partition

First handle \(m\le29\). For \(m\ge30\), divide by the unique full-support corner, and only then divide the residual case by integer degree.

| Case | Exact input | Result used |
|---|---|---|
| \(m\le19\) | Published small-multiplicity theorem | \(W_4\ge0\) |
| \(20\le m\le29\) | Analytic negative-case conductor reduction, then complete generator-box verification | \(W_4\ge0\) |
| \(m\ge30\), no full-support corner | Weighted no-interior theorem | \(D_0\ge m-1\), hence \(W_4\ge1\) |
| \(m\ge30\), \(p=(1,1,1)\) | At most six maxima; six-final-window theorem | \(W_4\ge0\) |
| \(m\ge30\), \(p\) a permutation of \((2,1,1)\) | Short-corner weighted theorem | \(D_0\ge m-1\), hence \(W_4\ge1\) |
| \(m\ge30\), \(|p|_1\ge5\), \(R\le6\) | Round 10 local-or-axis centroid lemma and necessary surface/plane-corner restrictions | \(D_0\ge m\), hence \(W_4\ge2\) |
| \(m\ge30\), \(|p|_1\ge5\), \(R\ge7\) | \(H\ge R\ge7\), then high-height one-corner theorem | \(D_0\ge m-29/10\), hence \(W_4\ge0\) |

The rows are exhaustive because a positive integer triple has coordinate sum at least three; the only sum-three triple is \((1,1,1)\), and the only sum-four type is \((2,1,1)\). Integer degree is either at most six or at least seven. There is no omitted height boundary: the last row includes \(H=7\), while the penultimate row works at *every* normalized height.

The four-generator theorem is a composition of these named results. Its conclusion is nonnegativity; strict positivity has only been derived in the displayed subclasses.

## 3. Exact statements and sources of the retained inputs

### 3.1 Small multiplicities and analytic conductor reduction

For a genuine four-generator numerical semigroup,

\[
\boxed{W_4<0\ \Longrightarrow\ M\le m(m-2).} \tag{2}
\]

Consequently every generator other than \(m\) is at most \(m(m-2)\), since each is an Apéry element. For each \(m=20,\ldots,29\), one may therefore enumerate exactly

\[
m<a_1<a_2<a_3\le m(m-2).
\]

The conductor is correspondingly at most \(m^2-3m+1\). The proof of (2) is analytic: a full weighted ideal is first proved to satisfy Wilf; otherwise a minimal excluded point of weight at most \(M\) forces \(D\ge M\), while negative integer \(W_4\) gives \(D\le m(m-2)\). It does not rely on the six-point enumeration or on a large-multiplicity theorem.

Sources:

- `round8/audit_sixpoint.md`, section 7: reconstructed analytic proof of (2).
- `round5/small_multiplicity/exhaustive_m20_m29_theorem.md`: complete finite domain and arithmetic calculations.
- `round6/audit_enumerations.md`: independent code audit, coverage, two algorithms, and integer-safety checks.
- `round6/audit_enumerations_data/small_replay_2026-09-09.json`: completed fresh full-run record.
- Published multiplicity-through-19 source identified in the earlier manuscript: Kliem and Stump, `https://arxiv.org/html/1905.01945v2`, together with its cited predecessor through 18. This external input must stay explicit in a publication manuscript and its bibliographic statement should be checked directly.

The two full arithmetic programs cover **301,098,092** sorted generator triples and **180,719,029** minimal four-generator numerical semigroups in the proved boxes. Positive minima in those boxes do not prove strict positivity for generators outside the boxes: (2) excludes only a negative case.

### 3.2 No full-support corner

**Abstract weighted theorem.** If \(T\subset\mathbb N^3\) is a finite lower ideal containing the coordinate units, with no full-support minimal exclusion and \(|T|=m\ge30\), then

\[
3m\max_T a\cdot x-4a\cdot s\ge a_{\min}(m-1).
\]

This theorem does not require residue labels. It uses the central-box/three-horn structural theorem, the continuous no-interior bound, the general phase inequality, the degree-four cardinality bound 29, and a closed real-parameter interval certificate on \(1\le b\le c\le H\), \(5\le H\le24\).

Sources:

- `round5/weight_arrangement/weighted_no_interior_theorem.md`.
- `round5/weight_arrangement/verify_interval_certificate.py` and `independent_interval_verification.json`.
- `round5/structural_audit/weighted_no_interior_audit.md`, `independent_interval_dp_results.json`, and `independent_interval_coverage_results.json`.
- `round8/audit_structure.md`: complete reconstructed central-box/three-horn argument.
- `round8/audit_phase.md`: phase and thickening interface.

Recorded complete coverage: **50,885 nodes**, **24,912 DP leaves**, **531 analytic leaves**, zero unresolved leaves. The second independent DP implementation uses explicit rectangle transitions; distinguish its leaf replay from the separate tree-coverage proof.

### 3.3 The corner \((1,1,1)\)

When \(p=(1,1,1)\), every mixed corner of a coordinate plane must represent the terminal point on the complementary axis. Residue injectivity therefore allows at most one mixed corner in each plane. Since every included point has a zero coordinate, the whole ideal has at most six maximal points.

Let \(Z=\{x\in T:M-a\cdot x<m\}\). Every point of \(Z\) is maximal, so \(|Z|\le6\). The six-final-window theorem gives \(W_4\ge0\).

Sources:

- `round2/arithmetic/interior_corner_111.md`.
- `round8/audit_sixpoint.md`, sections 2–6 and 8, and `round7/six_point_fresh_math_audit.md`.
- `prior/wilf_edim4_six_point_and_column_theorems_2026-09-05.md`.
- `round7/six_point_dependency_replay/run_six_point_verification.py` and `six_full_run_results.json`.

The sufficient verification route is compression, all admissible insertions and extensions, all ordered residue-bijective labelings, then **all modular cuts**. It covers arbitrary integer lifts and equality walls. It need not retain auxiliary LP certificates. The six-point arithmetic record has **930** ordered residue labelings and **23,002** modular-cut checks; the complete runner additionally covers \(|Z|\le5\).

This remains an explicit dependency after Round 10. It was removed from the *residual low-degree branch*, not from the whole proof.

### 3.4 The corner \((2,1,1)\) and permutations

**Genuine short-corner theorem.** For the preferred Apéry ideal of a minimally four-generated semigroup, if \(m\ge30\) and \(p\) is a permutation of \((2,1,1)\), then \(D_0\ge m-1\).

Its preferred proof has two parts:

1. A generic geometric inequality for normalized height \(H\ge6\), using planar slicing, phase compactness \(H<42\) for a failure, and an exact closed interval certificate.
2. If \(H<6\), degree is at most five; necessary residue restrictions yield **70,175** eligible shapes, of which **28,499** have cardinality at least 30. Their exact rational centroid duals establish the same bound for all real normalized weights.

Sources:

- `round5/one_corner_extension/short_corner_weighted_theorem.md`.
- `round6/audit_short_corner.md`.
- `round6/short_corner_audit/verify_complete_short_corner.py`, `complete_short_corner_audit_results.json`, and `low_height_independent_replay.json`.
- `round5/interior_arithmetic/verify_low_height_weighted.py` and associated proof data.

The interval replay covers **110,865 nodes**, **54,978 DP leaves**, **455 analytic leaves**, and **164,934** corner-placement bounds, with no unresolved region. The rational low-height record verifies all **28,499** shapes.

The separate computation over \(m=30,\ldots,48\) satisfying one of three short-corner congruences is an *alternative proof*. Its **803,005,632** triples and **508,199,476** semigroups need not appear among the essential gates of the preferred presentation.

### 3.5 The new local centroid lemma

For a lower ideal \(T\subset\mathbb N^3\) of degree at most six and cardinality \(m\ge30\), assume exactly one full-support minimal exclusion \(p\) with \(5\le|p|_1\le7\). Require only:

- **Each** coordinate plane has at most \(|p|_1-2\) mixed minimal excluded points. This is not a bound on the sum over the three planes.
- With \(F_i=\{x\in T:x+e_i\notin T\}\) and \(n_k=1+\max_T x_k\), one has \(|F_i\cap F_j|\le2n_k\) whenever \(\{i,j,k\}=\{1,2,3\}\).

The first restriction follows from disjoint-support residue representatives and the zero residue of \(p\); the second follows by injecting mixed exclusions of the planar slices into the complementary axis. Their analytic proofs remain in `round8/audit_lowheight.md`, sections 2 and 4. Neither the erosion argument nor the refined dominating-corner count is needed now.

For every coordinate line \(\ell\), let its length be \(L_\ell\), its top \(t_\ell\), and

\[
\rho(t)=\max\{|v|_1: v\in\mathbb N^3,\ |v|_1\le2,\ t+v\in T\},\qquad
U_2=\sum_\ell L_\ell\rho(t_\ell).
\]

With \(q_i=\max_T x_i>0\), let

\[
G=q_*\left(3m-4\sum_i\frac{s_i}{q_i}\right),\qquad q_*=\max_iq_i.
\]

Both constructions are proved analytically: they give \(D_0\ge U_2\) and, whenever positive, \(D_0\ge G\), for every \(b_i\ge1\). The remaining computer-assisted assertion is

\[
\boxed{\max\{U_2(T),G(T)\}\ge m.} \tag{3}
\]

Equivalently one of the explicit witnesses yields \(z\in\operatorname{conv}(T)\), \(3mz-4s\ge0\) coordinatewise, and total surplus at least \(m\).

Sources: `round10/local_centroid/local_centroid_theorem.md`, `independent_two_step.cpp`, `verify_complete_local_centroid.py`, `portable_replay_result.json`; independent audit at `round10/independent/final_local_class_audit.json` and the final section of `proof_audit.md`.

Completed exact replay: **85,392,579** axis-compatible profile triples; **26,252,336** of degree at most six; **26,153,719** of cardinality at least thirty; **5,574,644** passing the surface bounds. Local moves suffice for **5,574,213**; the remaining **431** use the axis witness. All fallbacks were independently reconstructed with Python fractions. The independent implementation uses no LP, per-shape certificate stream, or external optimizer.

For a genuine residual ideal of degree at most six, the bound \(|p|_1\le7\) is automatic: each \(p-e_i\) belongs to \(T\). Thus (3) gives exactly the needed result, without an upper-height hypothesis.

### 3.6 Residual high degree

**Abstract high-height theorem.** If \(T\subset\mathbb N^3\) is a finite lower ideal with exactly one full-support minimal excluded point \(p\), \(|p|_1\ge5\), and positive weights of minimum one, then

\[
H\ge7\quad\Longrightarrow\quad D_0\ge m-29/10.
\]

No residue, cardinality, plane-corner, surface, or erosion restriction is needed for this geometric theorem. Its infinite-to-finite reduction uses the phase inequality and the continuous gap \(5/42\) to place any failure in \(1\le b\le c\le H\), \(7\le H<78\). The certificate covers the corresponding closed root box through 78.

Sources:

- `round7/geometric_residual.md`.
- `round7/uniform_gap_theorem.md`: the continuous-gap premise and grid transfer.
- `round7/verify_uniform_gap.js`: third independent exact finite-strip computation.
- `round8/audit_structure.md`, `audit_phase.md`, and `audit_computation.md`.
- `round8/high_height_replay/independent_residual_complete_checks.json` and `full_replay_stdout.txt`.
- `round8/final_review_completion.json`: provenance ledger, not another mathematical replay.

The continuous gap retains an exact finite-strip dependency: allowances **18, 19, 20, 21**, with **1,029** sorted corner configurations in total. The high-height tree has **94,459 nodes**: **47,229 splits**, **47,088 DP leaves**, **142 empty leaves**. The fresh no-cache replay recomputed **35,852,138** full Cartesian corner cases, with zero unresolved nodes and zero cached checks. The certificate SHA-256 is `173fe6ec196b3d2adabad313749482542ad3492b5f6b4e398e76bbe6e52e405c`.

## 4. Final arithmetic, once for all branches

If \(D_0\ge m-1\), equation (1) gives

\[
mW_4\ge(A-m)(m-1)>0,
\]

so integrality yields \(W_4\ge1\). If \(D_0\ge m\), it gives

\[
W_4\ge A-m+1\ge2.
\]

For the weaker high-height bound, suppose \(W_4<0\). As \(W_4\) is an integer,

\[
D_0\le\frac{m(m-2)}A\le\frac{m(m-2)}{m+1}
=m-3+\frac3{m+1}.
\]

Hence, when \(m\ge30\),

\[
m-D_0\ge\frac{3m}{m+1}\ge\frac{90}{31}>
\frac{29}{10},\qquad \frac{90}{31}-\frac{29}{10}=\frac1{310}.
\]

This contradicts the high-height theorem. The distinction between this integer-negativity argument and the stronger direct positive bound should be retained.

## 5. What should be removed from the main proof presentation

The following are no longer essential to the chosen proof route:

1. Both residual low-height LP streams, their combined **3,742,041** assignments, and the intermediate Round 9 height-free registry of **6,816** bases.
2. The residual erosion filter and the refined dominating-plane-corner filter.
3. The former residual shortcut using the six-final-window theorem. Retain that theorem specifically for \(p=(1,1,1)\).
4. The alternate short-corner arithmetic enumeration at multiplicities 30–48, because the low-height centroid-dual proof already completes that branch.
5. The universal-envelope alternative with **44,281** parameter checks. It is useful as an independent alternative and a research direction, but weaker than the chosen local centroid bound and not needed simultaneously.
6. All earlier eventual multiplicity cutoffs and fixed-dimension finite reductions. These can be discussed as separate consequences/extensions; they are unnecessary for the shortest global four-generator chain.
7. Failed approaches, exploratory scans, and historical weaker constants. Preserve them in a research-history supplement, not as interleaved parts of the proof.

No retained small-case theorem is bypassed by the Round 10 lemma: it explicitly assumes \(m\ge30\) and \(|p|_1\ge5\). The clipped-box and clipped-prism analytic formulas prove valuable infinite families, but no result identifies all \((1,1,1)\), \((2,1,1)\), or no-interior ideals with those families. Such an identification must not be implied.

## 6. Reviewer-important limitations

- Exact integer checks establish finite statements only after their complete mathematical coverage is justified. The analytic reductions, implementation logic, and replay records should be presented separately.
- The local formulas themselves are elementary; the assertion that their union works for every residual shape is still exhaustive and computer-assisted.
- The older archives contain historical scope statements, now superseded by this case partition. A presentable manuscript should cite canonical statements once and move history to an appendix.
- Closed parameter boxes cover irrational weights and boundary points. Rational grid sampling would not do so; no such sampling is used as the proof certificate.
- Source-hash and record consistency checks are not fresh full replays. This note inspected completed records and did not rerun the exhaustive computations.
- The result is a proposed argument covering every four-generator case; it is not a claim of external peer acceptance, a formalized theorem, or a solution for higher embedding dimensions.
