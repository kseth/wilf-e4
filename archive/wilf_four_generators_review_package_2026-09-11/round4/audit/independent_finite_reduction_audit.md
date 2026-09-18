# Independent audit of the fixed-dimension finite reduction

7 September 2026. This is a fresh mathematical audit, not an external review or a proof of unrestricted Wilf.

## Outcome

I independently rederived the essential steps in:

- `deliverables/wilf_fixed_dimension_finite_reduction_2026-09-05.md`;
- Section 4 of `deliverables/wilf_edim4_global_finite_reduction_2026-09-05.md`;
- the scope assertions in `round3/audit/conceptual_stability_audit.md`.

I did not find a mathematical gap in the claimed eventual multiplicity theorem, its fixed-dimension finiteness corollary, or the sharper four-generator conductor bound. The checks below include the logical transitions that could fail under degeneration; this conclusion does not rest on rerunning the earlier numerical examples. The unrestricted four-generator conjecture remains outside these results.

## 1. The arithmetic input really is available in every fixed dimension

Let `T` be the lexicographically preferred Apéry exponent set for the nonmultiplicity generators. Divisor closure follows because both Apéry membership and lexicographic preference pass to divisors. Finiteness of a factorization fiber follows from positivity of all generator weights, so existence of its lexicographically least member does not create a well-ordering issue.

For an excluded minimal exponent `p` and its residue representative `q` in `T`, a positive coordinate common to `p` and `q` would give distinct points `p-e_i,q-e_i` in `T` with the same residue. Consequently their supports are disjoint. A full-support `p` therefore has representative zero. Two full-support excluded minimal exponents would have the same residue and a shared positive coordinate, and the same predecessor argument excludes them.

This proof works for every dimension and is not special to three variables. It also holds for ties in factorization weight: residue injectivity of the selected `T` is what is used. Hellus–Rechenauer–Waldi Proposition 2.6 independently states the corresponding result for lattice-tiling lower ideals; I checked the primary text rather than relying on its citation in the research manuscript.

## 2. The continuous argument does not lose thin shapes

For a positive-volume downset `K` inside the unit simplex in dimension `d`, direct fiber integration gives

`[d-(d+1)mu] vol(K) = sum_j integral H_j(y)(1-|y|-H_j(y)) dy`.

Every summand is nonnegative. Conditional slicing at the uniquely minimal coordinate `R=r` is legitimate almost everywhere: the ties are contained in finitely many coordinate-equality hyperplanes, hence have Lebesgue measure zero. The other coordinates, translated by `r`, form a lower ideal in a simplex of radius `1-dr`. Applying the same fiber identity in dimension `d-1` gives

`mu <= (d-1)/d + E R`.

Thus `kappa_c<1/(2d)` forces a point of `K` with every coordinate greater than `t=1/[2d(d+1)]`, and hence the whole closed cube `[0,t]^d` belongs to `K`. In particular a hypothetical sequence with deficit tending to zero cannot simultaneously have volume tending to zero. No compactness or unproved assertion about limiting orthant counts is needed.

For the propagation step, the rectangle in the manuscript is coordinatewise below the old point in its transverse coordinates and above the proposed omitted point in those coordinates. These two comparisons respectively give the lower and upper bounds on the fiber height. The total transverse-plus-top correction is exactly

`[d(d-j+2)-1]r <= d(d+1)r`.

With `r=1/[16d^2(d+1)]` and `h=1/(8d)`, this is at most `h/2`, while the old fiber height is at least `2r`. The resulting lower bound is `J_j >= h r^d`. Dividing by `vol(K)<=1/d!` produces precisely the stated `delta_d=d! h r^d`.

If no step can fail, all points of total coordinate at most `1-h` belong to `K`. The two outside points `p,q` and their witnesses then force two full-support excluded orthants below them. Replacing a coordinate by `h` really preserves domination by any excluded vertex whose corresponding coordinate is zero. The unique allowed full-support vertex would lie below `min(p,q)`, which was already forced into `K`. This contradiction is valid even with arbitrarily many lower-support excluded orthants.

The cell sets are half-open. Their complements inside the nonnegative orthant are exactly unions of closed upper orthants based at scaled excluded lattice exponents, not merely equal almost everywhere. Fiber endpoints can therefore be used as suprema without changing the integral argument. No boundary repair alters the excluded-corner count.

## 3. Anisotropic weights are explicitly controlled

For the discrete normalized lower ideal, write

`epsilon_j = 1-u_j H_j-sum_(i!=j) u_i X_i`.

Conditional uniformity along a coordinate fiber gives

`E epsilon_j=1-mu-mu_j`,
`sum_j E epsilon_j=kappa`,
`mu_j >= (1-d kappa)/(d+1)`.

In the coarse phase lemma, set `A=1/[2(d+1)]` and `s0=min(U/4,A/2)`. Since `U<=1`, the claimed bound `s0>=U/[4(d+1)]` is correct. In the nontrivial case `v<=s0/2`, the largest and smallest weight directions are necessarily different. With `ell=floor(s0/v)`, the shift has weight `s=ell v` in `[s0/2,s0]`.

The two nonnegative gaps have difference congruent to `-s` modulo `U`, so their sum is at least `min(s,U-s)=s`; the bound `s<=U/4` is more than sufficient. The shift is injective and each point can be counted at most twice. Also, for `0<=Y<=1`, the elementary inequality `P(Y>=s)>=E Y-s` is valid. These facts give

`2 kappa >= s P(v X_k>=s) >= s0 A/4 >= U/[32(d+1)^2]`.

The constant in `U<=64(d+1)^2 kappa+8(d+1)v` is therefore conservative, not missing a factor of two. Very large aspect ratios have not been excluded by assumption. If cardinality tends to infinity and `kappa` tends to zero, the count forces `v` to zero and the phase lemma then forces `U` to zero.

Equal-volume cell thickening gives exactly

`kappa_c = [kappa+(d-1)sigma/2]/(1+sigma)`.

Combining `sigma<=d U` with the phase lemma produces the stated `P_d,Q_d`. The direction of the cardinality inference is also correct:

`m <= (1/v+d)^d/d!` implies `v <= 1/[(d!m)^(1/d)-d]`.

Finally the strict inequality `a_min>m` supplies `M/m>1/v`; using it in the exact Wilf identity is what yields strict positivity at the stated large-multiplicity threshold.

## 4. The stronger three-dimensional phase transfer is sound

The sawtooth proof does not require commensurable weights. For the real residue function `[x]_U` and `r>=0`,

`[x+r]_U <= [x]_U+r`.

The intervals used for consecutive fiber points are adjacent, so their union is a single interval of length `L v`. For any interval of length `h=qU+r`, its residue integral is at least `(qU^2+r^2)/2`. A full number of periods has fixed integral; the residual arc of length `r` has minimum integral `r^2/2`. Cauchy–Schwarz then gives the displayed lower bound `U h^2/[2(h+U)]`.

The weighted average over fibers uses point weights, hence `v E L=2 mu_k+v`; no uniform-over-fibers average is substituted. This proves, for both `j!=k`,

`2 E(delta_j)(1+v+u_j) >= 2u_j mu_k-v(1+v)`.

After adding, substituting `mu_k=(1+kappa)/4-E(delta_k)` leaves a coefficient on `E(delta_k)` equal to the middle weight minus `1+v`, which is nonpositive. Thus discarding that term goes in the stated direction. Substitution of `U<=sigma-2v` gives

`sigma(1-3kappa) <= 4kappa+5v-3kappa v+4v^2`.

Under `W_4<=0`, one has `kappa<(a_min/M)=v`, so for `v<1/3`,

`kappa_c < 2v(5-v)/(1+6v+v^2) < 10v`.

All six lower bounds in the explicit three-dimensional box propagation exceed `1/10000`: respectively `0.00044544`, `0.0001176`, `0.000126`, `0.00107136`, `0.000378`, `0.0001291248`. They are exact terminating rational values. The seven final witnesses satisfy the stated inequalities after coordinate permutation.

The final numerical comparison is exact:

`100003^3=1000090002700027 < 1200000000000000=6(2*10^14)`.

Thus `m>=2*10^14` forces `v<1/100000` and contradicts the continuous gap if `W_4<=0`.

## 5. The independent general conductor argument closes fixed-m escape

In the nonsimplex lemma, a line top that is not coordinatewise maximal has a coordinate successor in `T`. Its weight deficit is therefore at least the least weight `beta`. The least-weight axis has height `ell`, and its deficit is `epsilon=M-ell beta`.

- If it is the same line, `epsilon>=beta`, so `(ell+1)epsilon>=M`.
- If it is a different line, their two contributions give `D>=(ell+1)epsilon+beta`, hence `ell D>=M`.

The unit vectors in the other directions imply `ell<=m-d`, proving `D>=M/(m-d)`. The characterization that all line tops are maximal only for a standard simplex is valid because every unit transfer is then allowed. Fixed-degree lattice layers are connected by those transfers.

The difference-set proof excludes a standard simplex of radius `R>=2`. If two vectors in `Delta_(R-1)-Delta_1` have equal residues, the corresponding sums lie in `Delta_R`, where injectivity applies. The difference set has excess cardinality

`[(d-1)(R-1)/R] binom(d+R-2,d-1)>0`.

This removes the only exception to the geometric bound once `m>d+1`. The remaining case `m=d+1=e` is separately handled and really does permit the familiar infinite equality families.

Consequently the eventual multiplicity result plus this conductor bound excludes infinitely many negative Wilf numbers with multiplicity fixed. The fixed-dimension finiteness conclusion is not obtained merely by mistaking the multiplicity bound for a bound on all semigroups.

## 6. The sharper four-generator conductor bound survives a separate audit

For a full weighted staircase, each point

`(floor((M-by)/a)+1,y,0)`

is minimal excluded: subtraction of its first coordinate crosses the weight threshold, and subtraction of its second does so because `b>=a`. The disjoint-support representatives therefore give the projection count `h2<=h3+1`. If a mixed projection point occurs, its corresponding full-support excluded point represents zero; zero is unavailable to the former representatives, so `h2<=h3`. Uniqueness of the full-support corner then yields `h2=h3=2`, giving precisely the six-column triangle as the only additional case.

In the six-column exclusion, the origin and mixed columns lie in the same cyclic subgroup generated by `a`, because `E a+b+d=0`. Their residues occupy the consecutive interval from `-E a` through `(A-1)a`. Their disjointness forces the subgroup order `r>=A+E`. The forbidden first permutation of the two boundary representatives yields a positive multiple of `r` strictly smaller than `A+E`. The other permutation and its symmetric analogue yield

`B+F=2B-C=2F-G=r`,

forcing `C+G=0`. Every strict inequality used follows from the full weighted condition. No assumption that `a` generates the entire residue group was made.

For the remaining three- and four-column projections, the boundary estimate pays for each distinct positive axis residue once using `binom(m,2)`. Axis residues are indeed pairwise distinct across the three directions because the corresponding axis points belong to `T`. The additional copies are counted exactly by `E(Z)`. The subsequent formulas for `Phi(T,K)` are respectively `2A-4` and `2A-6`, both nonnegative at the required minimum column lengths.

Finally, a low-weight excluded corner `p` contributes through its predecessor lines exactly

`M+(|p|-1)(M-w(p))>=M`.

The line length is exactly `p_j`, not merely bounded by it, since `p-e_j` is in `T` and its next point is excluded. Distinct minimal excluded corners cannot claim the same directional line. If the staircase is not full weighted, at least one such corner exists. This proves the audited implication

`W_4<0 => M<=m(m-2), c<=m^2-3m+1`.

## 7. Scope and comparison with primary literature

The verified chain implies a strict density gap as multiplicity tends to infinity with embedding dimension fixed. It does not imply a strict density gap as conductor alone tends to infinity. The family `S_q=<e,qe+1,...,qe+e-1>` has fixed multiplicity `e`, unbounded conductor, and `W=0`, so that latter assertion would be false.

Zhai's Theorem 2 gives a lower density approaching `1/e` from below outside a finite set for any fixed positive tolerance. It does not itself imply that there are finitely many counterexamples. Zhai's concluding Question 1 asks about the density infimum as multiplicity tends to infinity. The strict gap claimed here would answer the equality-to-`1/e` part negatively for `e>=3`, but does not determine the optimal limiting value. I found no contradiction in the primary sources inspected; this limited search does not establish publication priority.

Sources directly consulted on 7 September 2026:

- A. Zhai, *An asymptotic result concerning a question of Wilf*, Theorems 1–2 and Question 1: https://arxiv.org/html/1111.2779v1
- M. Hellus, A. Rechenauer and R. Waldi, *Variants on a question of Wilf*, Propositions 2.5–2.6: https://arxiv.org/pdf/1804.06141
- W. Bruns et al., *Wilf's conjecture in fixed multiplicity*, primary published text: https://www.home.uni-osnabrueck.de/wbruns/brunsw/pdf-article/S021819672050023X-1.pdf

This audit provides no inequality eliminating the finite residual region and no counterexample in that region. A successful eventual theorem is substantial evidence about the tail, but it cannot be presented as the missing unrestricted four-generator proof.
