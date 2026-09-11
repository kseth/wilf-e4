# Exact discrete horn optimization and a unit-weight theorem

7 September 2026. The unit-weight theorem below is proved. The proposed
extension to arbitrary positive weights remains unproved. None of these
results is a proof of four-generator Wilf by itself.

## 1. The completed unit-weight theorem

Let `T` be a finite lower ideal in `N^3`, containing the three coordinate
unit vectors, with no full-support minimal excluded point. Put

\[
m=|T|,\qquad R=\max_{x\in T}|x|_1,\qquad
D_1=3mR-4\sum_{x\in T}|x|_1.
\]

Then

\[
\boxed{m\ge30\quad\Longrightarrow\quad D_1\ge m.}
\]

This is stronger than the unit-weight target `D_1>=m-1`. The theorem uses
the completed continuous no-interior moment theorem and a small exact
integer dynamic program. The recurrence was independently audited; its
correctness, not random or floating-point search, supplies the finite
part of the proof.

### Large degree follows directly from the continuous theorem

Thicken every lattice point to its unit cube. The resulting continuous
no-interior lower set has maximum coordinate sum `R+3`, mean sum
`(sum_T |x|)/m+3/2`, and volume `m`. Its mean is at most `2(R+3)/3`.
Therefore

\[
\frac{D_1}{m}\ge\frac R3-2.
\]

For `R>=9`, this already gives `D_1>=m`.

### Exact recurrence for the remaining degrees

Fix `R` and define the additive score

\[
\Phi_R(T)=\sum_{x\in T}(4|x|_1-3R+1)=m-D_1.
\]

A horn starting at outward integer coordinate `t`, with transverse caps
`B,C`, has a rectangular slice `(u+1)(v+1)` at that level, where
`0<=u<=B`, `0<=v<=C`, and `t+u+v<=R`. The slice's exact score is

\[
(u+1)(v+1)(4t+2u+2v-3R+1).
\]

Let `H_t(B,C)` be the maximum horn score, allowing an empty horn. Then

\[
H_t(B,C)=\max\left(0,
\max_{\substack{u\le B,\,v\le C\\t+u+v\le R}}
\left[(u+1)(v+1)(4t+2u+2v-3R+1)+H_{t+1}(u,v)\right]\right),
\]

with `H_(R+1)=0`. The inner maximum is computed exactly by two-dimensional
prefix maxima. This recurrence considers every nested sequence of
rectangular slices, including arbitrary omissions and slack.

The audited clique-tree theorem writes every no-interior ideal as a
central box `[0,a]×[0,b]×[0,c]` with three disjoint such horns. Conversely
such a construction is a feasible lower ideal with no full-support
excluded corner. Thus the exact maximum of `Phi_R` is obtained by
maximizing

\[
\begin{aligned}
&(a+1)(b+1)(c+1)[2(a+b+c)-3R+1]\\
&\qquad +H_{a+1}(b,c)+H_{b+1}(a,c)+H_{c+1}(a,b)
\end{aligned}
\]

over `a,b,c>=0`, `a+b+c<=R`. Symmetry allows sorting the central triple.

The required exact results are:

| Degree allowance R | Maximum of Phi_R over every nonempty no-interior ideal |
|---:|---:|
| 5 | -4 |
| 6 | -17 |
| 7 | -20 |
| 8 | -23 |

All are negative, so `D_1>=m` in these cases too. The program also records
R=1,...,23, but R>=9 is not needed computationally.

Finally, the independent exact central-box cardinality calculation gives
`|T|<=29` when `R<=4`. It maximizes each feasible horn slice's cardinality
and then sums with the central box. Hence `m>=30` forces `R>=5`, completing
the theorem.

The main exact checker is `unit_weight_dp.py`; its output is
`unit_weight_dp_results.json`. It reconstructs one maximizer and checks
its cardinality, score, downward closure, and absence of an interior
excluded corner. The preceding cardinality checker is
`round4/discrete/max_no_interior_size.py`.

## 2. A general weighted dynamic program is available

For positive integer weights `a=(a_1,a_2,a_3)`, height allowance `M`, and
integer penalty `p`, consider

\[
\Phi_{a,M,p}(T)=\sum_{x\in T}[4a\cdot x-3M+p]=pm-D.
\]

For a horn in coordinate i, at outward integer level t, with remaining
weights beta,gamma and slice `[0,u]×[0,v]`, the exact contribution is

\[
(u+1)(v+1)[4a_it+2\beta u+2\gamma v-3M+p].
\]

Replace the degree constraint in the preceding recurrence by
`a_i t+beta u+gamma v<=M`. The same prefix-maximum recurrence computes the
exact optimum over every no-interior ideal within the weighted height
allowance. Central triples must now be enumerated without sorting,
because unequal weights remove that symmetry.

`weighted_dp.py` implements this recurrence with exact integer arithmetic.
For a fixed cardinality requirement `m>=L`, `weighted_size_dp.py` retains
cardinalities 0,...,L-1 exactly and caps all larger cardinalities at L.
The recurrence adds each slice cardinality and uses the same prefix
maxima; the three horns are combined by capped max-plus convolution.
It uses an integer sentinel for impossible states and reports feasibility
separately. These routines provide fixed-parameter certificates. They do
not establish any universal statement over all real weight triples.

## 3. What was checked about arbitrary weights

The natural open extension is

\[
m\ge30\quad\Longrightarrow\quad
3mM-4\sum_Ta\cdot x\ge a_{\min}(m-1).
\]

For genuine four-generator Apéry ideals, `a_min>=m+1`, so this inequality
would prove Wilf for the no-interior subclass of size at least 30.
It is not proved here.

A potentially simpler open sufficient statement is that, after
normalizing `a_min=1`, every no-interior ideal with `M>=5` satisfies
`m-D<=1`. Together with the degree<=4 cardinality bound, this would imply
the preceding statement. It too is unproved.

Two finite diagnostics were completed:

* All 2,300 integer normalized cases `(a_1,a_2,a_3)=(1,b,c)`,
  `1<=b<=c<=M<=23`. No unconstrained optimum violated `m-D<=1` at `M>=5`.
  Some smaller-height optima violate it; their largest maximizing
  cardinality is 29. The latter observation alone does not exclude a
  smaller positive score at a larger cardinality.
* A structured rational grid with integer weights `(10,b,c)`,
  `10<=b<=20`, `b<=c<=30`, and `40<=M<=90`: 8,976 cases. The target
  `10m-D<=10` for cardinality at least 30 passed in every case. Most
  cases were certified by the unconstrained DP or the exact Lagrange
  bound `max_T(20m-D)-300<=10`; one remaining case was settled by the
  capped-cardinality DP, which found no admissible ideal.

These grids are bounded computations, not proofs for all rational or
real parameters. They produced no counterexample to the open weighted
extension. The diagnostic output files explicitly record their scope.

## 4. Discrete endpoint convexity survives, with a cardinality caveat

For fixed weights, height M, a fixed central box, and a fixed nested
sequence of transverse rectangles in each horn, vary the outward right
endpoints `e_j`. If the rectangle cardinalities are `N_j`, the quadratic
coefficient of `sum_T a·x` at `e_j` is

\[
\frac{a_i}{2}(N_j-N_{j+1})\ge0.
\]

There are no cross terms in that first-moment contribution. Cardinality
m is affine in the endpoints. Consequently the violation functional

\[
4\sum_Ta\cdot x-3mM+m(m-1)
\]

is convex in the endpoint vector: its additional quadratic term is m²,
a positive-semidefinite rank-one form.

Without a cardinality constraint, the integer ordered-endpoint polytope
has integer vertices, so a maximum occurs at an endpoint pattern where,
after coalescing zero-length intervals, each right endpoint is

`floor((M-beta u-gamma v)/a_i)`.

This is a valid discrete extremal reduction for the unconstrained
geometric functional. It does not give a semigroup deformation. Fixing
m or imposing `m<=a_min-1` adds a cardinality constraint and requires
additional analysis; changing endpoints also generally destroys residue
bijection. Those constraints cannot be silently dropped when proving
Wilf for genuine semigroups.
