# D4: short-corner simplification decision

**Status date:** 2026-09-16

## Decision

Retain the high-height interval tree. Replace the low-height stored dual
family with the [deterministic local route](../paper/short-corner-local-certificates.md):
check the two-step line-top gain on every B4.3 profile, with two explicitly
proved exceptional witnesses.

This removes the 28,499-record dual list, its rational loader, and its
optimization producer from the selected proof inputs. It does **not**
remove the finite low-height profile check. No uniform symbolic
classification has been proved that establishes its predicate on all
profiles, and no analytic replacement covers the full high-height region.

D4 is closed as a bounded route-selection gate with this partial
simplification. R4a and the revised R4b are both still required; neither
computed lemma is established under V0 by the research diagnostics below.
The historical archive remains unchanged.

| Component | Selected route |
|---|---|
| High-height compactness | Retain B4.2's analytic \(H<36\) reduction. |
| High-height finite assertion | Retain the historical closed \(42\)-box tree, with clipped horns. |
| Low-height profile coverage | Retain B4.3 unchanged, including every eligible oriented key. |
| Low-height local soundness | Adopt the deterministic two-step construction from G2. |
| Local exceptions | Retain two inline three-point integer witnesses, related by \(y,z\) exchange. |
| Legacy low-height dual list | Not a selected proof input; no replay or curation is needed. |

## 1. What the low-height simplification accomplishes

For each coordinate-line top \(t\), choose an included dominating point at
distance at most two maximizing the coordinate-sum gain. There are only
ten candidate offsets. The G2 line identities derive a nonnegative
residual whose coordinate sum is \(U_2(T)\), giving

\[
3mQ-4w\cdot s\ge U_2(T)
\qquad(w_i\ge1,\ Q\ge\max_Tw\cdot x).
\tag{1}
\]

This is a witness construction, not an estimate at sampled weights.
The selected finite contract **B4-low-local-FV** is

\[
U_2(T(k))\ge |T(k)|-1
\quad\text{or}\quad k\in\{E_0,E_1\}
\quad\text{for every }k\in\mathcal F_5^{\ge30}.
\tag{2}
\]

The two keys and their exact witnesses are proved in the local note.
Each has \(m=30\), and its witness has residual sum 54, exceeding the
required 29. Thus (2) implies the original all-real-weight **B4-low-FV**
without any stored multiplier stream.

On 2026-09-16, the research command

    python3 -B research/check_b4_local_route.py

generated 81,373 compatible triples, 70,175 degree-filtered shapes, and
28,499 eligible keys. The local test passed on 28,497; exactly \(E_0,E_1\)
needed the explicit witnesses. The smallest nonexceptional margin over
\(m-1\) was one. All line-mass, line-moment, residual, and exceptional
witness checks passed.

The same command with Python's optimization flag produced identical
output; required checks use unconditional exceptions, not removable
assertions. A separate bounded diagnostic passed 316 successor-path and
exact-weight checks on the two exceptions, and checked their moment table,
the high-height example below, and rejection of an unrecognized exceptional
key. These additional checks do not supply full-family independent evidence.

This is an enumeration-wide research diagnostic, not a promoted R4b
replay. It shares profile-generation helpers with the B4.3 diagnostic,
so it is not an independent checking path. R4b must audit the selected
contract and run materially separate complete implementations.
Its acceptance test remains (2), not an observed count or stronger margin.

## 2. Exact obstructions to simpler replacements

### 2.1 The geometric low-height target needs the arithmetic filters

B4.1's sharp family \(T_5\), without the plane filters, has

\[
m=48,\qquad s=(61,55,55),\qquad H=5
\]

at unit weights. Its deficit is \(3\cdot48\cdot5-4\cdot171=36<47=m-1\).
Therefore the short corner and large multiplicity alone cannot justify
deleting the low-height verification. This abstract ideal violates the
B4.3 plane-corner restrictions; it is not a semigroup counterexample.

### 2.2 The B3 projection replacement does not extend unchanged

For the eligible profile \(E_0\), the maximal points are

\[
\begin{gathered}
(0,0,5),\ (0,1,3),\ (0,3,1),\ (1,1,2),\ (1,2,1),\\
(2,0,2),\ (2,2,0),\ (3,0,1),\ (3,1,0).
\end{gathered}
\]

Direct counting gives
\(P=40\), nine maximal points, maximal-degree sum 37, and axis-length
sum 11. Consequently

\[
\Phi(T(E_0),\operatorname{Max}(T(E_0)))
=40-27-37+11=-13.
\tag{3}
\]

It already has \(m=30\). The B3 argument
\(\Phi(T,K)<0\Rightarrow m\le29\) is therefore false under the B4
geometric profile hypotheses. In a semigroup realization the final window
might be smaller than \(K\), and residue compatibility might impose further
restrictions;
neither supplies a currently proved replacement.

### 2.3 Dominating endpoint upgrades alone cannot handle every profile

For \(E_0\), group coordinate lines by their best two-step gain and sum
their lengths:

| Direction | Gain zero | Gain one | Gain two | Total upgrade |
|---|---:|---:|---:|---:|
| \(x\) | 21 | 8 | 1 | 10 |
| \(y\) | 19 | 11 | 0 | 11 |
| \(z\) | 24 | 6 | 0 | 6 |

Thus \(U_2=27<29\). The profiles give
\(\Delta_3\subseteq T(E_0)\subseteq\Delta_5\).
Every coordinate-line top therefore has degree at least three, so every
dominating destination has coordinate-sum gain at most two.
Every line top consequently has the same best gain
even if arbitrarily distant dominating destinations are allowed.
The total 27 is therefore the maximum obtainable by independently
moving each line's existing mass to a dominating point.
The transposed key has the same obstruction.

The explicit witness redistributes mass between incomparable points.
It proves the target but is not such an endpoint upgrade. Increasing
the allowed local move length cannot remove these two exceptions.

Equal weights are also insufficient for selecting the worst weighted
deficit. For \(E_0\), unit weights give \(D=106\). At
\(w=(5/4,5/4,1)\), \(H=5\) and \(D=54\). The explicit witness proves
\(D\ge54\) for all admissible weights and allowances, so this unequal
vertex is a global minimum. Neither example asserts semigroup realization.

## 3. Why the high-height tree remains

The planar bounds and phase inequality exclude large height but do not
settle the lattice-sensitive compact remainder. For a concrete admissible
geometric profile, use \(E_0\) with \(w=(3/2,3/2,1)\).
It has \(H=6\), \(B=4\), and actual deficit 92. The two-partition bound
has offset \(L=13/4\), giving only

\[
D/m\ge(6-4L)/3=-7/3.
\]

Both B4.2 planar leaf tests fail, and the phase cutoff admits these
parameters. Thus those scalar estimates alone do not prove even this
profile's target, although its explicit witness does. This illustrates
insufficiency of the estimates, not a failure of the target.
The selected finite local route covers degree at most five only; no
extension to all higher-degree profiles is proved here.

Nor can the completed B2 no-corner theorem be applied to the unclipped
ideal with the retained height. For the same profile, its pairwise
reconstruction \(U\) includes \((2,2,1)\), of weight seven, while
\(T=U\setminus((2,1,1)+\mathbb N^3)\) has height six.
Deleting the orthant changes the height. A bound requiring height six
for \(U\) would have a false hypothesis.

After clipping, horn feasibility depends on maxima of surviving faces
and on floors of real weighted height constraints. A symbolic case
analysis would have to resolve those regimes or provide a joint
discrete potential controlling every nested horn sequence. No such
complete replacement has been proved in this bounded gate.
The existing interval tree is the selected exact representation of
that residual case analysis, not evidence that an analytic proof is impossible.

## 4. Retained high-height contract and R4a handoff

Use sorted weights \(w=(1,b,c)\), all three corner positions
\(p\in\{(2,1,1),(1,2,1),(1,1,2)\}\), and the closed domain

\[
1\le b\le c\le Q,\qquad 6\le Q\le42.
\tag{4}
\]

The retained **B4-high-FV** assertion is: for every finite nonempty lower
ideal \(U\) with no full-support corner, if
\(T=U\setminus(p+\mathbb N^3)\) is nonempty and
\(\max_Tw\cdot x\le Q\), write \(m=|T|\), \(s=\sum_{x\in T}x\).
The required conclusion is

\[
m-(3mQ-4w\cdot s)\le1.
\tag{5}
\]

The [high-height interval specification](../paper/short-corner-interval-specification.md)
derives its exact clipped statistics, recurrence, whole-box domination,
coverage theorem, and fixed-width arithmetic bounds.

This geometric superset does not require \(p\) to remain minimal,
multiplicity at least 30, residue labels, or plane-corner filters.
Its height constraint is on \(T\), **not** \(U\).
The axis points are unchanged by deletion since every \(p_i>0\), so all
coordinates of \(U\) are nevertheless bounded by \(\lfloor Q/w_i\rfloor\).
G5's clipped central-box/three-horn decomposition therefore supplies a
finite recurrence for every parameter box.

B4.2 places every genuine high-height failure in the smaller \(36\)-box;
the historical \(42\)-box safely contains it. Keep the immutable
historical tree rather than requiring a new producer or smaller tree.
Endpoints, including \(Q=6\), remain closed and covered.

R4a must audit the retained slice and central-box statistics, exact
whole-box score domination, recurrence, clipping, and closed child
coverage. It must recompute every required leaf, reject partial or
unsupported runs, establish arithmetic bounds, and supply a materially
separate checking path under V0. Cached leaf bounds and historical
success flags are not accepted mathematical inputs.
The discovery producer, redundant sampling tools, and legacy success
records do not belong in the final minimal checker package.

## 5. Gate closure

The retained B4 chain is now:

1. B4.1 routes by attained normalized height;
2. B4.2 and the retained high-height tree require R4a;
3. B4.3's unchanged finite family, local soundness, and two inline
   exceptions require the revised R4b;
4. either completed finite route gives \(D_0\ge m-1\), then G1 gives
   \(W_4\ge1\).

B4.4 remains the analytic soundness interface for the exceptional witnesses.
Its legacy record-loader specification is an alternative, not an
additional selected proof dependency. The archived dual list may remain
as immutable research history but need not be curated into release data.

At gate closure, R4a was recommended next; the current queue is maintained
in the [roadmap](../ROADMAP.md). The earlier gate decisions remain unchanged.
L3 will refresh attribution for the precise retained local and weighted
statements; this decision makes no novelty or impossibility claim.
