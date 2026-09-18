# Replacing shape enumeration by a universal indicator envelope

11 September 2026. This is a proposed computer-assisted simplification of the residual centroid lemma. It is independent of the 3,742,041 individual shape assignments and of their centroid bases. It retains a finite verification over rational parameter cells, and uses the separately proved high-height theorem. External mathematical review remains outstanding.

**Certificate status: completed.** Exact generation and independent standard-library replay both passed all 44,281 cells: 40,115 exact moment bounds and 4,166 exact cardinality exclusions. The greatest certified normalized score is −999,992/1,000,000. The independent replay took49.75 seconds and imported neither the producer nor SciPy. The result records are `universal_envelope_generation_result.json` and `universal_envelope_independent_result.json`. The preliminary floating-point scan had maximum score−1; its numerical outcomes are diagnostics, not proof evidence.

## 1. Statement and dependencies

Let T be a finite lower ideal in N³, of total degree at most six, with m=|T|≥30 and exactly one full-support minimal excluded point p, whose coordinate sum is between five and seven. Assume the plane-corner, erosion, and pairwise exposed-surface restrictions previously proved necessary for preferred Apéry ideals. Define s=Σ_T x.

The target conclusion is the existence of z∈conv(T) satisfying

    3mz−4s≥0 coordinatewise,
    Σ_i(3mz_i−4s_i)≥m−29/10.

The universal envelope below supplies a new route to this conclusion using only:

1. An analytic reduction to a finite set of weight directions.
2. Exact dual certificates for 44,281 universal parameter cells. No individual ideal is enumerated.
3. The existing independent theorem at normalized height H≥7, namely m−D≤29/10 for the relevant one-full-corner class.

This is not a proof free of finite computation. Its purpose is to replace shape-specific certificates with universal combinations of a fixed collection of arithmetic indicator inequalities.

## 2. Why finitely many directions suffice

For b_i≥1, let H_T(b)=max_{x∈T}b·x and

    D_T(b)=3mH_T(b)−4b·s.

The epigraph program minimizes 3mH−4b·s subject to b_i≥1 and H≥b·x for all x∈T. It is bounded below. Indeed, if an i-coordinate line through T has length L and top point t, direct summation gives

    3mH−4Σ_T b·x = Σ_(coordinate lines in all three directions) L(H−b·t) ≥0.

The feasible epigraph has no line, so its finite minimum is achieved at a vertex. At least one weight lower bound is active: otherwise four independent homogeneous point equalities would force b=0. Four independent active rows can therefore be chosen in one of three forms:

* Three point equalities and one weight lower bound. The positive weight direction is a cross product of two differences of points of Δ₆.
* Two point equalities and two weight lower bounds. Two weights equal one; the third is determined by the point difference.
* One point equality and three weight lower bounds. All weights equal one.

Let N consist of all primitive positive integer directions from these constructions in the ambient simplex Δ₆, including candidates that may never support an actual ideal. This is a universal superset, independent of T. Exact construction gives 2,425 directions, or 416 up to coordinate permutation. Their largest primitive coordinate is30.

For an independent exhaustive reconstruction, all positive triangle normals lie in [1,36]³: a normal component is the doubled area of a projected triangle in the coordinate triangle of side6, hence at most36 before removal of a common divisor. Searching all primitive positive vectors in that box for a level plane containing three noncollinear lattice points independently recovers the same triangle directions. The two-fixed-weight cases are checked separately. The supplied independent verifier performs this reconstruction.

Write b=n/u where n∈N and u=min_i n_i. At an epigraph vertex its height has the form H=h/u with h=n·q for q∈T. If H≥7, the independent high-height theorem applies. If H<7, necessary conditions are

    n·p−u≤h<7u,
    |{q∈Δ₆ : n·q≤h and q is not coordinatewise ≥p}|≥30.

The first condition follows because every p−e_i belongs to T. Since one may sort p by a coordinate permutation while retaining every oriented direction n, exactly the nine archived corner types suffice. These conditions leave44,281 triples(p,n,h).

Thus it suffices to prove the desired weighted inequality for those universal cells. This reduction is for the all-height centroid conclusion and uses the high-height theorem at any minimizing vertex with H≥7. The stronger observed bound at low-height parameter vertices must not be promoted to a stronger bound for every arbitrary low-height weight without a separate argument.

## 3. The indicator relaxation

Fix(p,n,h), and put t_q=1(q∈T) for q∈Δ₆. Outside Δ₆ define t_q=0. The common relaxation has455 variables in[0,1]; all auxiliary variables have an indicator interpretation for an actual ideal.

**Bounds and lower closure.** Set t_q=0 when n·q>h or q≥p coordinatewise. Set t_(p−ei)=1 for all i. Require Σt_q≥30 and t_q≤t_(q−ei) whenever q_i>0.

**No second full corner.** For every positive q of degree at most7 except p, require

    t_q ≥ t_(q−e1)+t_(q−e2)+t_(q−e3)−2.

If all three predecessors are present, the only allowed missing point is p. Points of degree above7 cannot be minimal excluded points of a degree-six ideal.

**Erosion.** For |q|≤5 introduce e_q with

    e_q ≥ t_(q+e1)+t_(q+e2)+t_(q+e3)−2t_q,
    Σ_(|q|≤5)(1+# {i:q_i=0})e_q ≤ Σ_q t_q.

For an actual ideal choose e_q=1(q,q+e1,q+e2,q+e3∈T). The local row is valid for every zero-one lower ideal, and the sum is precisely the necessary erosion restriction.

**Pairwise exposed surfaces.** For each i<j and q∈Δ₆ introduce w_(ij,q) with

    w_(ij,q) ≥ t_q−t_(q+ei)−t_(q+ej),
    Σ_q w_(ij,q) ≤ 2 Σ_(q on the complementary coordinate axis) t_q.

For an actual ideal choose w_(ij,q)=1(q∈F_i∩F_j). This is the previously derived |F_i∩F_j|≤2n_k restriction; the origin is included in the axis count.

**Mixed plane corners.** For q=a e_i+b e_j with a,b≥1 and a+b≤7 introduce c_q with

    c_q ≥ t_(q−ei)+t_(q−ej)−t_q−1,
    Σ_(q in the ij plane) c_q ≤ |p|−2,
    Σ_(q_i≥p_i,q_j≥p_j) c_q ≤ p_k.

For an actual ideal choose c_q to indicate a mixed minimal excluded point of that coordinate plane. All possible plane corners have degree at most7.

Every genuine residual Apéry ideal embeds into this relaxation by its indicators. Fractional feasible points need not represent ideals; this makes the relaxation larger and its upper bound valid for all actual ideals. The relaxed rows are used only as necessary conditions.

## 4. Exact certificate mechanism

The integer-scaled score to maximize is

    Q(t)=Σ_(q∈Δ₆)(u+4n·q−3h)t_q = u(m−D_T(n/u)).

Write all common linear rows as Ax≤r and the variable box as l≤x≤v, with integer endpoints0 or1. For any nonnegative rational λ,

    Q(x) ≤ λ·r + Σ_i max{(Q−Aᵀλ)_i l_i,(Q−Aᵀλ)_i v_i}.

This formula is a complete proof of each envelope upper bound. It does not require exact solution of an LP or zero residual coefficients. The producer obtains candidate λ from a floating-point solver, rounds each nonnegative multiplier to a nonnegative integer divided by10⁶, and then evaluates the displayed bound using integer arithmetic. Every coefficient residual is handled by the box formula. Acceptance requires the exact upper bound to be at most(29/10)u.

When the relaxation with m≥30 is infeasible, a second certificate removes the cardinality row and instead bounds Σt_q strictly below30. This is again an ordinary exact upper-bound certificate. The relaxed second program is feasible: the box[0,p] minus its top point lies below the mandatory height, obeys all geometric and arithmetic rows, and has no second full corner. No floating-point infeasibility judgment is accepted without the cardinality certificate.

The independent verifier uses Python standard-library integers only. It reconstructs all directions by a different algorithm, all44,281 cells, and each of the584 moment rows (583 after removing the cardinality row). It imports neither the producer nor the optimization library. Every certificate is checked by direct row addition and the displayed box maximization, with exact ordered stream consumption.

## 5. Return to the centroid

The complete exact parameter replay has passed. Consequently no epigraph vertex below height7 can violate m−D≤29/10. The high-height theorem excludes a violation at any remaining vertex. Thus D_T(b)≥m−29/10 for every b_i≥1.

Finite-dimensional LP duality then supplies nonnegative point multipliers λ_x and coordinate multipliers β_i with

    Σ_x λ_x=3m,
    Σ_x λ_x x=4s+β,
    Σ_i β_i≥m−29/10.

The point z=(Σ_x λ_x x)/(3m) has exactly the desired centroid properties. Since m−29/10>0, a basic dual solution has at least one coordinate multiplier and at most three point multipliers.

The argument therefore proves the same residual centroid existence statement without enumerating individual ideals or importing any earlier per-shape centroid certificate. It does not provide a single closed formula for z, and still requires a finite universal parameter replay.

## Reproduction

Generate proposed multipliers (SciPy is used only here):

    python3 round10/envelope/certify_universal_envelope.py

Independently replay the archived exact certificate with Python standard library:

    python3 round10/envelope/verify_universal_envelope.py

The principal payload is `universal_envelope_certificates.jsonl.gz`. `generate_normal_cases.py` and `probe_envelope.py` are the producer sources; `verify_universal_envelope.py` independently reconstructs the proof inequalities. The preliminary `fractional_*probe.json` records are diagnostics and are not proof dependencies.
