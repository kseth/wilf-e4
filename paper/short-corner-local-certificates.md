# Deterministic local certificates for the short corner

## Status and purpose

This note supplies the low-height simplification selected by
[D4](../research/b4-simplification-decision.md). It replaces the stored
28,499-record dual family with a deterministic two-step construction and
two explicit exceptional witnesses. The finite profile check is retained;
it has not yet cleared R4b or the [V0 trust policy](../verification/trust-policy.md).

The analytic arguments below prove soundness, not the universal finite
assertion in Section 3. The profile family and its coverage remain exactly
those of [B4.3](short-corner-profile-specification.md).

## 1. The two-step construction

For a finite nonempty lower ideal \(T\subseteq\mathbb N^3\), put
\(m=|T|\), \(s=\sum_{x\in T}x\). Use the indexed coordinate lines,
lengths \(L_\ell\), and tops \(t_\ell\) from
[G2](coordinate-lines.md).
For each \(t\in T\), define

\[
\rho_2(t)=\max\{|v|_1:
v\in\mathbb N^3,\ |v|_1\le2,\ t+v\in T\},
\qquad
U_2(T)=\sum_\ell L_\ell\rho_2(t_\ell).
\tag{1}
\]

There are only ten possible offsets: zero, three coordinate units,
three doubled units, and three sums of distinct units. Zero is always
feasible. Choose any maximizing offset \(v_\ell\), and assign mass
\(L_\ell\) to \(u_\ell=t_\ell+v_\ell\in T\).

The G2 identities give

\[
\sum_\ell L_\ell=3m,\qquad
\beta:=\sum_\ell L_\ell u_\ell-4s
      =\sum_\ell L_\ell v_\ell\ge0,
\qquad
\sum_i\beta_i=U_2(T).
\tag{2}
\]

Repeated destinations can be combined. Thus \(U_2(T)\ge m-1\) supplies
an integer witness for the [B4.4 predicate](short-corner-centroid-certificates.md).
Equivalently, G2's endpoint-upgrade theorem proves, for every real
\(w_i\ge1\) and \(Q\ge\max_Tw\cdot x\),

\[
\boxed{3mQ-4w\cdot s\ge U_2(T).}
\tag{3}
\]

No maximal-point registry, optimization, rational reconstruction, weight
ordering, or stored multiplier is needed. Ties between maximizing offsets
do not affect \(U_2\) or soundness.

## 2. Two explicit exceptions

Write a canonical B4.3 profile key as \((f,g,h)\), in \(xy,xz,yz\) order.
Define

\[
\begin{aligned}
E_0={}&((4,3,3,2,0,0),\ (6,3,3,2,0,0),\ (6,4,2,2,0,0)),\\
E_1={}&((6,3,3,2,0,0),\ (4,3,3,2,0,0),\ (4,4,2,2,1,1)).
\end{aligned}
\tag{4}
\]

The second key is the first ideal with \(y,z\) exchanged. In particular,
the \(yz\) profile must be transposed as well as exchanging \(f,g\).
Both keys satisfy B4.3's profile, compatibility, and degree tests.

For \(T_0=T(E_0)\), the B4.3 column formula gives the following exact
counts and moments:

| \(x\)-level | Point count | Sum of \(x\) | Sum of \(y\) | Sum of \(z\) |
|---|---:|---:|---:|---:|
| 0 | 14 | 0 | 14 | 23 |
| 1 | 8 | 8 | 7 | 7 |
| 2 | 5 | 10 | 3 | 3 |
| 3 | 3 | 9 | 1 | 1 |
| Total | 30 | 27 | 25 | 34 |

Assign these nonnegative integer multipliers:

| Point in \(T_0\) | Multiplier |
|---|---:|
| \((0,0,5)\) | 38 |
| \((2,2,0)\) | 48 |
| \((3,1,0)\) | 4 |

Membership follows directly from the three profile tests. The total mass
is \(90=3m\), and the derived residual is

\[
\beta=(108,100,190)-4(27,25,34)=(0,0,54).
\tag{5}
\]

B4.4 therefore proves

\[
3mQ-4w\cdot s\ge54\ge29=m-1
\tag{6}
\]

for all admissible real weights and allowances. Exchanging \(y,z\)
gives the witness for \(E_1\), with residual \((0,54,0)\).
These are explicit arithmetic proofs, not cached archive success flags.

## 3. The retained finite contract

The selected replacement for replaying the legacy dual list is:

> **B4-low-local-FV.** Every key \(k\in\mathcal F_5^{\ge30}\) of B4.3
> satisfies
> \[
> \boxed{U_2(T(k))\ge |T(k)|-1
> \quad\text{or}\quad k\in\{E_0,E_1\}.}
> \tag{7}
> \]

If (7) is established under V0, (3) and the two exceptional witnesses
prove the original **B4-low-FV** statement for every key and all real
weights and height allowances. B4.3's coverage theorem then yields
\(D_0\ge m-1\) for every genuine B4 ideal with \(H<6\); G1 converts this
to \(W_4\ge1\).

The geometric family is unchanged. No maxima-count skip, empirical
cardinality cutoff, symmetry quotient, or realizability filter is added.
Equality \(U_2=m-1\) is accepted. Since the witnesses cover all allowances,
the resulting finite lemma also covers genuine degree-at-most-five
ideals whose weighted height is at least six; it does not cover
arbitrary higher-degree ideals.

## 4. R4b handoff and diagnostics

R4b must reconstruct every B4.3 key, its literal point set and cardinality,
and its coordinate lines. It must check (7) with integer arithmetic and
fail on any unexpected under-threshold key. The exceptional point
membership, counts, and residual identities above should also be
recomputed as defensive checks, not loaded from trusted cached data.

A materially separate path should generate plane profiles differently
and compute the gain using successor paths rather than the same list
of offsets. In a lower ideal, a two-step destination exists if and only
if some included one-step successor has an included successor; this
justifies that alternative representation. Both paths must check full
profile coverage and meet V0's audit and fresh-replay requirements.

No dual JSON input, SciPy dependency, denominator bound, or legacy
residual-vector loader belongs to this selected route. Arbitrary-precision
integers suffice. The B4.4 legacy schema safeguard remains relevant only
if the archived dual-list alternative is reinstated.

The [research diagnostic](../research/check_b4_local_route.py) reads
neither archived code nor certificates. Its enumeration-wide run on
2026-09-16 visited 28,499 eligible keys. Exactly the two keys (4) failed
the local test, each with \(m=30\) and \(U_2=27\). All local line identities
and both explicit witnesses agreed with reconstructed point sets.
This is an unaudited research run, not an independent R4b replay or an
analytic proof of (7).

The local construction is the G2 endpoint-upgrade method also used in
the residual B5 route. The exceptional multiplier was discovered in
the historical dual list and checked directly above; the archive is
not a proof input for the selected checker. This note makes no novelty
claim. Final branch attribution remains with L3.
