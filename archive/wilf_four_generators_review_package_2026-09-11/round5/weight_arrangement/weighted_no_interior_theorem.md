# A weighted integer theorem for no-interior lower ideals

7 September 2026. This theorem is computer assisted, with an exact rational
parameter-space certificate. It addresses the entire no-interior class
of size at least 30, not a finite grid of weights. It does not address
ideals with a full-support minimal excluded point.

## Statement

Let T be a finite lower ideal in N^3 containing the three coordinate unit
vectors. Assume no minimal point outside T has all three coordinates
positive. Let a_1,a_2,a_3>0, set m=|T|, and define

\[
M=\max_{x\in T}a\cdot x,
\qquad D=3mM-4\sum_{x\in T}a\cdot x.
\]

Then

\[
\boxed{m\ge30\ \Longrightarrow\ D\ge a_{\min}(m-1).}
\]

The argument uses the previously proved continuous no-interior mean
theorem and general lower-ideal phase estimate, together with a complete
exact certificate described below. In particular it does not assume that
equal weights minimize D.

## 1. Analytic reduction to a compact three-dimensional parameter set

Scale the weights by a_min and permute coordinates so they are (1,b,c),
with 1<=b<=c. Write M and D for these normalized quantities.

Suppose for contradiction D<m-1. Set

\[
v=1/M,\quad s=(1+b+c)/M,\quad \kappa=D/(mM).
\]

Then kappa<(m-1)/(mM)<v. The established phase estimate is

\[
s(1-3\kappa)\le4\kappa+5v-3\kappa v+4v^2.
\]

Unit-cube thickening preserves the no-interior property, and the
continuous mean theorem gives

\[
\kappa_c=\frac{\kappa+s}{1+s}\ge\frac13.
\]

The prior exact phase calculation now implies

\[
M<12+\sqrt{137}<24.
\]

For clarity, if v>=1/3 then M<=3 already. Otherwise substitution
kappa<v in the phase inequality yields

\[
\kappa_c<\frac{2v(5-v)}{1+6v+v^2},
\]

and comparison with 1/3 gives 7v^2-24v+1<0, hence the displayed bound.
This calculation requires no residue-bijection or semigroup hypothesis.

The exact central-box-and-horn cardinality bound for no-interior ideals
of total degree at most 4 is 29. Consequently m>=30 forces some point
of T to have total degree at least 5. Since all normalized weights are
at least 1, M>=5. Finally, the coordinate unit vectors belong to T,
so c<=M. Thus any counterexample has its parameters in the closed region

\[
\mathcal P=\{(b,c,M):1\le b\le c\le M,\ 5\le M\le24\}.
\]

It remains to exclude that entire real parameter region.

## 2. A stronger assertion on the compact parameter region

The exact certificate establishes the following:

> For every (b,c,M) in P, and every nonempty no-interior lower ideal T
> whose (1,b,c)-weighted height is at most M, one has m-D_M<=1,
> where D_M=3mM-4 sum_T (x_1+b x_2+c x_3).

The height M is an allowance here; it need not be attained. The assertion
therefore implies the desired contradiction when M is the actual
maximum. It also drops the cardinality and unit-vector hypotheses during
the computation, thereby enlarging the class to be checked.

## 3. Rigorous bounds on whole parameter boxes

Use a common scale q=4096. Consider a closed box with integer endpoints

\[
(B_0,C_0,H_0)\le q(b,c,M)\le(B_1,C_1,H_1).
\]

Define lower feasibility weights l=(q,B_0,C_0) and upper objective
weights u=(q,B_1,C_1). Every actual ideal in this box is contained in

\[
\{x\in\mathbb N^3:l\cdot x\le H_1\}.
\]

For each of its points, the actual scaled score is bounded above by

\[
q[4(x_1+b x_2+c x_3)-3M+1]
\le 4u\cdot x-3H_0+q.
\]

Thus an exact maximum of the upper expression over the enlarged
feasibility class is a rigorous upper bound simultaneously for every
real parameter in the box. Accept a box when this integer bound is at
most q. No interpolation assumption is used.

## 4. Exact horn dynamic program

The established no-interior structure theorem writes T as a central
integer box [0,A_1] x [0,A_2] x [0,A_3] with three disjoint outward horns.
Each horn is a nested sequence of rectangular cross sections.

For outward axis i and other axes j,k, a slice at coordinate t with
rectangle [0,r] x [0,s] is allowed when

\[
l_i t+l_jr+l_ks\le H_1.
\]

Its upper score is exactly

\[
(r+1)(s+1)(4u_it+2u_jr+2u_ks-3H_0+q).
\]

Let H_i(t;B,C) be the largest upper score for a horn starting at t,
with transverse caps B,C. Its recurrence is

\[
H_i(t;B,C)=\max\left(0,
\max_{\substack{0\le r\le B,\ 0\le s\le C\\
l_it+l_jr+l_ks\le H_1}}
\left\{(r+1)(s+1)(4u_it+2u_jr+2u_ks-3H_0+q)
+H_i(t+1;r,s)\right\}\right).
\]

The boundary beyond floor(H_1/l_i) is zero. Every nested rectangle
sequence is covered, with the zero option representing an empty
remainder. Two-dimensional prefix maxima evaluate the inner maximum
exactly.

For every central A with l dot A<=H_1, add its score

\[
\prod_i(A_i+1)(2u\cdot A-3H_0+q)
\]

to the three independent horn scores starting at A_i+1. Maximizing this
sum over all such A gives the required box bound. Central points are
enumerated without symmetry restrictions; weights are unequal.

## 5. Complete parameter-space coverage

Start from the closed box

\[
[1,24]\times[1,24]\times[5,24].
\]

At each node, tighten endpoints using b<=c<=M. For raw endpoints L,U,
the retained rectangle is

\[
L'=(L_b,\max(L_b,L_c),\max(L_b,L_c,L_M)),
\]

\[
U'=(\min(U_b,U_c,U_M),\min(U_c,U_M),U_M).
\]

Every point of the raw box satisfying the order constraints lies in
this retained rectangle. If an interval is empty the feasible
intersection is empty. Otherwise either accept the retained rectangle
or divide one of its intervals at an integer midpoint. Both children
include that midpoint, so all boundaries are covered. Tightening can
discard only points outside the ordered region.

A second acceptance test follows directly from the continuous theorem:

\[
M\ge2(1+b+c)+3\quad\Longrightarrow\quad D_M\ge m.
\]

Indeed unit thickening gives D_M/m >= [M-2(1+b+c)]/3. Thus a whole box
passes this test when H_0>=2(q+B_1+C_1)+3q.

The complete tree contains **50,885 nodes and 25,443 accepted leaves**,
with **zero unresolved leaves**. Every split, endpoint, and bound is
stored in `full_interval_certificate.json`. The subdivision heuristic
has no mathematical role beyond selecting a tree; the final verifier
checks the resulting tree and all its closed leaves directly.

The independent verifier imports no generator code. It verifies:

1. The root is the stated full box.
2. Each retained rectangle contains every ordered point of its parent.
3. Each split has two exactly matching closed children.
4. Every recorded node is reached exactly once, and every branch ends
   at an accepted leaf.
5. Every leaf satisfies either the analytic test or an independently
   implemented integer horn-DP bound at most q.

The independent replay passed all **24,912 DP leaves** and **531 analytic
leaves**, as well as every split. Its largest accepted integer bound is
4096=q. A second adversarial audit independently replayed every DP leaf
using explicit rectangle transitions rather than prefix maxima; it too
passed, together with its own clipping and coverage checks. These are
separate in-session audits, not external peer review.

The output file is `independent_interval_verification.json`. This is a
finite certificate for all real parameters in P, not merely rational
parameters with denominator 4096: the integer endpoints describe
closed real boxes.

## 6. Consequence for genuine four-generator Apéry ideals

For a minimally four-generated numerical semigroup with multiplicity m,
preferred Apéry weights satisfy a_min>=m+1. Also

\[
mW_4=D-m(m-1).
\]

Therefore the theorem implies

\[
mW_4\ge(a_{\min}-m)(m-1)>0
\]

whenever m>=30 and the preferred Apéry ideal has no full-support
minimal excluded point. Since W_4 is integral, it is at least 1.

The small no-interior multiplicities and the one-interior-corner class
are separate obligations. Nothing in this certificate establishes the
weighted inequality for the latter class.

## Reproduction

All programs in this directory use only the Python standard library.

```
python3 interval_certificate.py --max-nodes 100000 --output full_interval_certificate.json
python3 verify_interval_certificate.py full_interval_certificate.json
```

Earlier analytic inputs are in
`round4/discrete/conditional_discrete_bridge.md`,
`round4/bellman/arbitrary_horn_bridge.md`,
`round4/joint_horns/joint_effective_cap_theorem.md`, and the prior
no-interior clique-tree and phase-estimate proofs. The R=4 cardinality
input is independently rechecked inside `verify_interval_certificate.py`.
