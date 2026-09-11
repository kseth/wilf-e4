# Audit of the sharp unit-weight one-interior-corner theorem

7 September 2026. **PASS.** The proof establishes, for every finite lower ideal
with at most one full-support minimal excluded point and unit weights,

\[
|T|\ge65\quad\Longrightarrow\quad
3|T|\max_T|x|_1-4\sum_T|x|_1\ge |T|.
\]

The threshold is sharp. This is an arbitrary-height theorem; it is not a
theorem for arbitrary coordinate weights.

## Clipped-horn recurrence

Remove the possible full-support corner from the list of excluded generators
to obtain a no-interior ideal U. Then `T=U\(p+N^3)`. The pair projections,
and therefore all axis heights, are the same in U and T. The earlier
central-box and three-horn description applies to U, whose boxes can be
clipped separately by the p orthant. The pieces stay disjoint.

The C++ slice count, twice-moment, and maximum formulas are the rectangle's
formulas minus the clipped corner rectangle, with the maximum taken on the
two remaining top faces. The central-box formulas use the corresponding
three-dimensional subtraction and three remaining faces. I checked those
formulas and every coordinate permutation in the arrays. An additional
independent direct-point check verified 1,728 clipped-box moment/height cases.

The nested uncut rectangle caps correctly parametrize all horns of U. A zero
option ends an arm. Prefix maxima optimize all narrower rectangle choices.
An actual positive minimal corner satisfies `|p|<=R+1`; sorting p is valid
for unit weights. A no-interior ideal is included by choosing an inactive
positive p of degree R+1. In all finite strips R>=3, such a choice exists.
No coordinate-unit assumption is imposed on the optimized class.

The source C++ translation and the independently height-array-checked Python
recurrence agree at R=3,...,8. The reproducing verifier reruns the finite
strips R=7,...,16 with penalty 1 and R=14,...,34 with penalty 3. I reviewed
the verifier and the complete recorded strips rather than running those same
strips yet another time. All recorded corner counts agree with an independent
enumeration of positive sorted triples of sum at most R+1.

During audit, the saved target strip temporarily ended at R=14 although the
note specified R=16. The author regenerated the complete file atomically.
The final file contains R=3,...,16, and my independent checks passed. This
was an artifact discrepancy; the complete penalty-3 strip already supplied
the necessary R=15,16 inequalities.

## Decimation and the exact correction

For `T_r={y:r+Ly in T}`, each excluded orthant generator g pulls back to
`max(0,ceil((g-r)/L))` coordinatewise. A zero coordinate stays zero. Hence
at most one pulled-back generator can have full support; removing redundant
generators cannot introduce any more. Empty classes contribute zero, while
nonempty classes are lower ideals even if they omit coordinate units.

With `R_r=floor((R-|r|)/L)` and `eta_r=R-|r|-L R_r`, direct substitution gives

\[
D_R(T)=\sum_r\left[L D_{R_r}(T_r)+(3\eta_r-|r|)m_r\right].
\]

The sign and coefficient of the floor correction are correct. Since
`eta_r>=0` and `|r|<=3(L-1)`, the hypothesis `D_{R_r}>=3m_r` gives at least
`3m_r` from each class. Thus `D_R>=3m`.

For R>=17, write `R=17L+s` with `L=floor(R/17)` and `0<=s<=16`. Then
`14<=R_r<=33` for every r. The checked strip 14,...,34 includes that entire
range; the additional endpoint 34 is harmless. This supplies an exact finite
cover of all arbitrarily large R, not a numerical extrapolation.

I independently checked the defect identity, corner preservation, and floor
range on six explicit face-shell fixtures at R=17,18,33,34,50,79. These checks
support the implementation; the argument above proves the general identity.

## Low degrees and sharpness

R<=5 permits at most `binom(8,3)=56` points. At R=6, a corner (1,1,1) permits
at most the 64-point three-face shell. Every other allowed full corner has
the complete fixed-height maximum `m-D<=-1`, as verified in the recorded
per-corner table and recomputed by the author's verifier. The inactive
corner (1,1,5) handles no-interior ideals at this height.

The direct shell calculation gives `(m,sum|x|,D)=(64,273,60)` at R=6, so the
threshold cannot be lowered to 64, even for the weaker inequality D>=m-1.

The additional independent checks are reproducible with
`python3 round5/structural_audit/unit_one_corner_checks.py`; its exact output
is `unit_one_corner_checks.json`.

## Scope

The proof is valid for unit weights. For general weights the decimation
correction is weighted and the finite unit-weight bounds do not control it.
No arbitrary-weight or unrestricted Wilf conclusion is drawn from this
theorem alone.
