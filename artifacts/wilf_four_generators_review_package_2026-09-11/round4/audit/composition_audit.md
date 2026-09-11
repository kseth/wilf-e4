# Composition audit: continuous no-interior theorem and its consequences

7 September 2026. This audit checks compatibility of the component theorems. It does not expand the numerical searches or claim unrestricted Wilf.

## Conclusion

The newly completed components compose correctly. They establish the continuous no-interior moment inequality and the unconditional implication

`no full-support Apéry corner and W_4<=0 => m<=1836`.

For every negative secondary semigroup in the paired-quotient class, they also force the **common quotient's conductor** to be at most 40. This is not a bound of 40 on the conductor of the original four-generated semigroup, and it does not require choosing a conductor-minimal counterexample.

## 1. Structure, horn reduction, and joint inequality have matching hypotheses

The finite clique-tree argument applies to a finite box lower set whose membership is determined by its pair projections. This is exactly the no-full-support-complement-generator condition for the half-open finite-cell model. An arbitrary finite coordinate grid can be compressed to integer levels: the graph and connected-superlevel argument use only coordinate order, so unequal interval widths do not affect the decomposition.

It yields a central anchored box with side lengths `a,b,c>=0` and at most three arms. Each arm lies beyond one central face, remains below the other two central caps, and has nested rectangular fibers. The central box belongs to the set, so `a+b+c<=M`, where `M` is the supremum of total coordinate. Each arm satisfies the same height restriction `t+f(t)+g(t)<=M`.

These are precisely the hypotheses of `round4/bellman/arbitrary_horn_bridge.md`. Positive scaling by `M` transfers its normalization `M=1` to general `M>0`. Its one-slab value is exactly

`Q_M(x,y)+(3a-M)xy(M-a-x-y)/2`,

which is the function `F_M` in `round4/joint_horns/joint_effective_cap_theorem.md`. The boundary potential `Q_M` in both statements is the same sorted-cap one-tent optimum from `round3/horns_optimization/fullcap_boundary_theorem.md`. The earlier false balanced-taper ansatz is not reinstated: the extra boundary gain is included in `Q_M`.

For the functional `J=3 integral(x+y+z)-2M volume`, the central box contributes

`abc[3(a+b+c)/2-2M]`.

The joint theorem bounds the sum of the three horn contributions by its negative. Regions are disjoint apart from boundaries, so their volumes and first moments add. Consequently `J<=0`, or

`mean(x+y+z)<=2M/3`.

Empty arms and zero-width cross sections are allowed. Zero caps give zero contribution, and the joint certificates use nonnegative variables without division by a central side. Thus degenerate sections do not invalidate the composition. For a wholly zero-volume set the integral inequality is trivial; the uniform mean is asserted only for positive-volume sets. Closing or opening the finitely many boundary faces changes neither integrals nor the relevant supremum.

Older component notes still describe the bridge as missing or the consequence as conditional. Those statements describe their earlier checkpoint status; the new bridge supplies the missing hypothesis rather than altering it.

## 2. The discrete consequence retains the endpoint correction

For an Apéry ideal `T` of size `m`, put `M=max a.x`, `Sigma=sum_T a.x`, `s=(a_1+a_2+a_3)/M`, `v=a_min/M`, and `kappa=(3mM-4Sigma)/(mM)`.

Anisotropic cell thickening preserves the support of every excluded generator and therefore the no-interior hypothesis. Its equal cell volumes give exactly

`kappa_c=(kappa+s)/(1+s)`.

The continuous theorem supplies `kappa_c>=1/3`; it does not supply an uncorrected discrete mean bound. For `W_4<=0`, the exact Apéry identity and `a_min>m` give `kappa<v`. The previously proved summed sawtooth inequality then gives, when `v<1/3`,

`kappa_c<2v(5-v)/(1+6v+v^2)`.

Hence `7v^2-24v+1<0`, so `1/v<12+sqrt(137)<24`. The case `v>=1/3` satisfies the same weaker conclusion directly. Every exponent in `T` thus has integer total degree at most 23.

At a central integer triple of total degree at most 23, the existing cardinality formula bounds each arm layer by the largest admissible rectangle. It is an upper bound even if independently optimal rectangles at different levels were not nested. Maximizing this finite formula over all sorted central triples gives 1836, as independently checked in the existing exact cardinality computation. Thus every such `T` with `W_4<=0` has `m<=1836`. In particular `m>=1837` forces strict positivity in this subclass.

## 3. The secondary quotient-conductor bound applies to all negative cases

Write a secondary semigroup in the established paired form

`S=p<a,b>+q<c,d>`, with `a<b`, `c<d`, `gcd(a,b)=gcd(c,d)=1`,

and common quotient `R=<a,b>/q=<c,d>/p`. Its interior conditions include

`q R_+ subseteq a+b+<a,b>` and `p R_+ subseteq c+d+<c,d>`.

These conditions themselves imply `q>b` and `p>d`; no triple-gcd exclusion is needed. To see the first, let `h=gcd(a,q)`. The positive integer `a/h` belongs to `R`, since its multiple by `q` is `(q/h)a`. If `q/h<=b`, this multiple cannot belong to `a+b+<a,b>`: an equality

`ta=(u+1)a+(v+1)b`, with `t<=b`,

would, by coprimality, imply `t-u-1>=b`, a contradiction. Therefore `q/h>b`, and in particular `q>b`. The other pair gives `p>d` identically.

Let `C=c(R)`. The two-generator Frobenius formula and `q>=b+1` show that every integer `n>=a-1` belongs to `R`, because

`nq >= (a-1)(b+1) > ab-a-b`.

Thus `C<=a-1`; similarly `C<=c-1`. Also `p>=d+1>=c+2` and `q>=b+1>=a+2`. Therefore

`m(S)=min(pa,qc)>=(C+1)(C+3)`.

Every secondary semigroup has no full-support preferred Apéry corner by the previously proved pure-critical-pair argument. If it has `W_4<0` (indeed if `W_4<=0`), the new multiplicity consequence gives `m<=1836`. But `C>=41` would force

`m >=42*44=1848>1836`.

Hence `c(R)<=40` for every negative secondary semigroup in this class. No minimal-conductor choice or inverse-inflation step occurs in this deduction.

## Remaining scope

None of these compositions covers a preferred Apéry ideal with a full-support corner. The exact geometric extension counterexample and the unavoidable-corner semigroup examples remain valid. The bound `c(R)<=40` also does not by itself prove Wilf for all secondary cases with quotient conductor at most 40.
