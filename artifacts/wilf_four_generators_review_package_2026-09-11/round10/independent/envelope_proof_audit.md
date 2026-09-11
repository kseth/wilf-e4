# Independent mathematical audit of the universal indicator envelope

Date: 2026-09-11.

This note audits the mathematical reduction in `round10/envelope/universal_centroid_envelope.md` and the corresponding independent verifier's model. It does not certify the archived high-height theorem anew, nor does this note substitute for the complete exact 44,281-cell replay. The latter must report success before the envelope theorem is treated as computationally established.

## Epigraph and finite direction reduction

For a fixed finite lower ideal, the epigraph minimization in four variables `(b1,b2,b3,H)` has a feasible pointed polyhedron. The line identity gives a finite lower bound of zero. A finite optimum of a linear objective on this pointed polyhedron is attained at a vertex.

At a vertex, four independent active constraints can be selected. At least one is a weight lower bound. Otherwise all four would be homogeneous equations `H=b·q` with independent rows, forcing `(b,H)=0`, contrary to `b_i>=1`. The remaining rank cases are exactly three point constraints plus one weight bound, two point constraints plus two weight bounds, and one point constraint plus three weight bounds.

For the first case, two independent point differences determine the normal direction by a cross product. Each normal component is the signed doubled area of a triangle projected into a coordinate simplex of side six. Its absolute value is at most 36. Thus enumeration of positive primitive integer vectors in `[1,36]^3`, followed by a check for a level set containing three noncollinear points of the degree-six simplex, is an exhaustive independent reconstruction.

For the second case, the two fixed weights equal one. The third is a ratio of integer point differences. The numerator is a difference of two coordinate sums, each between zero and six; the denominator is a nonzero coordinate difference of absolute value at most six. Thus the independent verifier's looser coordinate box `[1,12]^3` is sufficient. Requiring at least two entries to be minimal retains every such direction after primitive normalization.

At least one weight bound is active, so for primitive normal `n` the actual vertex weights are exactly `n/min(n)`. At an optimal epigraph vertex, `H` equals the support value, hence `h=min(n) H=n·q` for an included point. Mandatory predecessors of the full corner imply

`h >= max_i n·(p-e_i) = n·p-min(n)`.

Sorting the full corner while retaining all oriented weight directions preserves every case. The ambient cardinality and support-height restrictions remove only impossible cells.

## Indicator constraints

Every proposed row has a direct valid zero-one interpretation:

- Lower closure is the usual predecessor implication.
- The full-corner row excludes a missing positive point with all three predecessors present, except for the designated corner. Degree seven suffices because a minimal exclusion of a degree-six ideal has a predecessor of degree at most six.
- The erosion variable can be the indicator that all three immediate successors of a point are present. On a lower ideal, this also forces the point to be present. The local inequality and weighted global sum then recover the necessary erosion condition.
- The pair-surface variable can be the indicator that the point is present and both specified successors are absent. Its defining row and complementary-axis bound are valid.
- The mixed plane variable can be the indicator of a missing planar point whose two predecessors are present. All mixed minimal exclusions have degree at most seven. The two plane budgets are precisely the retained arithmetic restrictions in the envelope proof.

The count of variables is consistent: 84 point indicators, 56 erosion indicators, 252 pair-surface indicators, and 63 mixed plane indicators, totalling 455.

The independent verifier constructs all these rows directly, treats omitted outside-simplex point indicators as zero, and sets each mandatory predecessor indicator to one. No unsupported fractional-realizability assertion is used: only actual zero-one ideals must embed into the relaxation.

## Exact dual upper bound

For `Ax<=r`, `l<=x<=v`, and rational `lambda>=0`, the identity

`Q·x=lambda·Ax+(Q-A^T lambda)·x`

immediately gives

`Q·x <= lambda·r + sum_i max((Q-A^T lambda)_i l_i,(Q-A^T lambda)_i v_i)`.

The verifier uses only integer numerators with common positive denominator `10^6`, reconstructs every row, and evaluates this bound exactly. In particular, it need not trust floating-point LP feasibility, optimality, or zero residuals. The cardinality certificates use the same mechanism to show that the relaxation without the cardinality constraint has size strictly below 30.

One wording precision is needed: for a general relaxed indicator vector, the score `sum(u+4n·q-3h)t_q` is a **fixed-height** expression. It equals `u(m-D_T(n/u))` only when `h` is the actual support height of `T`. This condition holds for the vertex cell used in the proof, so the wording does not expose a mathematical gap. The relaxed upper bound does not by itself assert the same bound at every smaller height.

## Return to the centroid

Provided the exact cell replay succeeds, and provided the separately established high-height theorem applies to arbitrary normalized positive weights of the relevant ideal class, every epigraph vertex satisfies the required lower bound. Consequently the entire epigraph does.

Finite-dimensional LP duality gives nonnegative point multipliers and coordinate surplus multipliers satisfying

`sum lambda_x=3m`,

`sum lambda_x x=4s+beta`,

`sum beta_i>=m-29/10`.

Dividing the point combination by `3m` produces the desired centroid witness. Because the last lower bound is positive, a basic solution must have at least one positive coordinate multiplier. With four equality constraints, at most three positive point multipliers are then needed.

No gap was found in this argument. Its scope is the original residual class with all indicator restrictions; it should not be silently identified with the broader local two-step class, whose proof removes two of those restrictions by a different finite verification.
