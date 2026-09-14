# No-corner interval-certificate specification

## Status and purpose

This note completes roadmap task B2.2. It states the exact finite proposition
needed for the no-full-support-corner branch, proves that its score and horn
recurrence cover every ideal in that proposition, and specifies a closed-box
certificate whose acceptance implies the proposition for every real weight
in the compact B2.1 domain.

This is a **specification and coverage proof**, not a replay result. It does
not promote the archived interval tree, its producer, or its saved success
records into the proof. The next D2 gate asks whether the finite certificate
can be replaced analytically. If D2 retains it, R2 must audit and freshly
replay the exact checking paths required here.

## 1. The finite obligation

Let

\[
\mathcal P=
\{(b,c,H)\in\mathbb R^3:
 1\le b\le c\le H,\ 5\le H\le24\}.
\tag{1}
\]

For \(\theta=(b,c,H)\in\mathcal P\), put \(w_\theta=(1,b,c)\). Let
\(\mathcal I_\theta\) be the class of all nonempty finite lower ideals
\(T\subseteq\mathbb N^3\) such that

1. \(T\) has no full-support minimal excluded point; and
2. \(w_\theta\cdot x\le H\) for every \(x\in T\).

The number \(H\) is a height allowance; equality need not be attained.
For \(T\in\mathcal I_\theta\), define

\[
m=|T|,\qquad s=\sum_{x\in T}x,
\qquad D_H(T;\theta)=3mH-4w_\theta\mathbin\cdot s.
\tag{2}
\]

The retained finite statement is:

> **Finite obligation B2.2-FV.** For every
> \(\theta\in\mathcal P\) and every \(T\in\mathcal I_\theta\),
> \[
> \boxed{m-D_H(T;\theta)\le1.}
> \tag{FV}
> \]

This deliberately quantifies over a larger class than the branch requires.
There is no assumption that \(m\ge30\), that the coordinate units belong to
\(T\), that \(H\) is attained, or that \(T\) carries residue labels.

### Proposition 1.1 (sufficiency for B2)

B2.1 together with (FV) proves

\[
3m\max_{x\in T}w\cdot x
-4w\mathbin\cdot\sum_{x\in T}x
\ge(\min_iw_i)(m-1)
\tag{3}
\]

for every finite lower ideal in the B2 branch.

#### Proof

Scale and permute the weights to \((1,b,c)\). If (3) failed, B2.1 would put
the actual normalized height \(H=\max_Tw\cdot x\) in \(\mathcal P\). The ideal
would then belong to \(\mathcal I_{(b,c,H)}\), and (FV) would give
\(D_H\ge m-1\), a contradiction. Scaling back proves (3). \(\square\)

## 2. The additive score

For \(\theta=(b,c,H)\), assign each lattice point the score

\[
\phi_\theta(x)
=4(x_1+bx_2+cx_3)-3H+1.
\tag{4}
\]

Then

\[
\boxed{
\sum_{x\in T}\phi_\theta(x)
=4w_\theta\mathbin\cdot s-3mH+m
=m-D_H(T;\theta).
}
\tag{5}
\]

Thus (FV) asks for an upper bound on an additive point score. This is exactly
the setting of the G5 disjoint central-box/horn decomposition.

## 3. One closed parameter box

Fix the scale

\[
q=4096.
\tag{6}
\]

An integer endpoint pair

\[
L=(B_0,C_0,H_0),\qquad
U=(B_1,C_1,H_1),\qquad L_i\le U_i,
\]

represents the closed real box

\[
\mathcal B(L,U)=
\left[\frac{B_0}{q},\frac{B_1}{q}\right]
\times
\left[\frac{C_0}{q},\frac{C_1}{q}\right]
\times
\left[\frac{H_0}{q},\frac{H_1}{q}\right].
\tag{7}
\]

For a box meeting the ordered cone \(b\le c\le H\), define lower feasibility
weights, upper objective weights, and height endpoints by

\[
\ell=(q,B_0,C_0),\qquad
u=(q,B_1,C_1),\qquad
h_-=H_0,\qquad h_+=H_1.
\tag{8}
\]

If \(\theta\in\mathcal B(L,U)\) and \(T\in\mathcal I_\theta\), then every
\(x\in T\) satisfies

\[
\ell\cdot x\le h_+.
\tag{9}
\]

Moreover, multiplying (4) by \(q\) gives the pointwise bound

\[
q\phi_\theta(x)
\le
\overline\phi_{L,U}(x)
:=4u\cdot x-3h_-+q.
\tag{10}
\]

Both directions are monotone because all coordinates of \(x\) are
nonnegative: lower weights and upper height enlarge the feasible lattice
region, while upper weights and lower height enlarge the objective. Hence

\[
q\bigl(m-D_H(T;\theta)\bigr)
\le\sum_{x\in T}\overline\phi_{L,U}(x).
\tag{11}
\]

No interpolation, continuity assumption, or rounding argument occurs here.
The endpoints in (7) enclose every real parameter in the box, including
irrational parameters.

## 4. Exact horn dynamic programming

For each coordinate \(i\), put

\[
N_i=\left\lfloor\frac{h_+}{\ell_i}\right\rfloor.
\tag{12}
\]

These are safe coordinate caps for the enlarged region (9). Fix an outward
coordinate \(i\), and let \(j,k\) be the other two coordinates. A rectangular
section at level \(t\), with transverse caps \(r,s\), is feasible when

\[
\ell_it+\ell_jr+\ell_ks\le h_+.
\tag{13}
\]

The exact sum of the upper point score (10) over that section is

\[
\boxed{
S_i(t,r,s)
=(r+1)(s+1)
\bigl(4u_it+2u_jr+2u_ks-3h_-+q\bigr).
}
\tag{14}
\]

Indeed, the section contains \((r+1)(s+1)\) points, while the two transverse
coordinate sums are

\[
(s+1)\frac{r(r+1)}2,\qquad
(r+1)\frac{s(s+1)}2.
\]

For \(0\le R\le N_j\) and \(0\le S\le N_k\), let
\(F_i(t;R,S)\) be the maximum score of a possibly empty nested horn beginning
at level \(t\), whose first transverse caps are at most \(R,S\). Set

\[
F_i(N_i+1;R,S)=0.
\tag{15}
\]

Backward induction uses

\[
\boxed{
F_i(t;R,S)=
\max\left\{
0,\
\max_{\substack{0\le r\le R,\ 0\le s\le S\\
                 \ell_it+\ell_jr+\ell_ks\le h_+}}
\bigl(S_i(t,r,s)+F_i(t+1;r,s)\bigr)
\right\}.
}
\tag{16}
\]

The zero option terminates the horn. Every nonempty section contains its axis
point, so lower closure forbids a later nonempty section after termination.
Every other transition chooses the current rectangle and passes exactly its
caps to the next level. Thus (16) covers every nested rectangular horn and
every possible stopping level. This is the score-specific instance of the G5
recurrence.

For implementations, define the exact candidate

\[
A_i(t;R,S)=
\begin{cases}
S_i(t,R,S)+F_i(t+1;R,S),&
\ell_it+\ell_jR+\ell_kS\le h_+,\\
-\infty,&\text{otherwise}.
\end{cases}
\]

Then (16) is equivalently evaluated by the two-dimensional prefix recurrence

\[
F_i(t;R,S)=
\max\{0,A_i(t;R,S),F_i(t;R-1,S),F_i(t;R,S-1)\},
\tag{17}
\]

with negative-index terms omitted. Induction on \(R+S\) proves that (17)
takes the maximum of the candidates for every \((r,s)\le(R,S)\). Prefix
maxima are therefore an implementation identity, not a restriction on horn
sections.

## 5. The central box and the complete box bound

For a possible central corner \(a=(a_1,a_2,a_3)\), write

\[
n(a)=\prod_{i=1}^3(a_i+1).
\]

The central box is feasible in the enlarged region when

\[
\ell\cdot a\le h_+.
\tag{18}
\]

Its exact upper score is

\[
\boxed{
C(a)=n(a)\bigl(2u\cdot a-3h_-+q\bigr),
}
\tag{19}
\]

because the sum of coordinate \(i\) over the box is \(n(a)a_i/2\).

Define the integer box bound

\[
\boxed{
\mathcal V(L,U)=
\max_{\substack{0\le a_i\le N_i\\\ell\cdot a\le h_+}}
\left[
C(a)+
\sum_{i=1}^3
F_i(a_i+1;a_j,a_k)
\right],
}
\tag{20}
\]

where \(j,k\) are the two transverse coordinates for the \(i\)-th term.

### Proposition 5.1 (whole-box domination)

For every \(\theta\in\mathcal B(L,U)\) with \(b\le c\le H\), and every
\(T\in\mathcal I_\theta\),

\[
q\bigl(m-D_H(T;\theta)\bigr)\le\mathcal V(L,U).
\tag{21}
\]

#### Proof

By G5, \(T\) is a disjoint central anchored box together with at most three
nested rectangular horns. Its central corner belongs to \(T\), so (9) gives
(18). Equations (14) and (19) are the exact sums of the enlarged point score
over its disjoint pieces. Equation (16) bounds each actual horn.

The three horn optimizations in (20) are independent. This may admit triples
of horns which do not arise simultaneously from a lower ideal, but it only
enlarges the maximum. Maximizing over every feasible central corner and using
(11) proves (21). \(\square\)

Consequently a closed box is a valid *DP leaf* whenever

\[
\mathcal V(L,U)\le q.
\tag{22}
\]

## 6. Analytic and empty leaves

B2.1 proves the allowance-height inequality

\[
\frac{D_H(T;\theta)}m
\ge\frac{H-2(1+b+c)}3
\tag{23}
\]

for every \(T\in\mathcal I_\theta\). Therefore

\[
H\ge2(1+b+c)+3
\quad\Longrightarrow\quad
m-D_H(T;\theta)\le0.
\tag{24}
\]

For a whole closed box, (24) follows from the endpoint condition

\[
H_0\ge2(q+B_1+C_1)+3q.
\tag{25}
\]

Such a box is a valid *analytic leaf*, including equality in (25). A box
whose intersection with the ordered cone is empty is an *empty leaf*. These
three leaf types exhaust the permitted acceptance rules:

1. empty ordered intersection;
2. the weak analytic test (25); or
3. the exact integer DP test (22).

No sampled test, floating-point bound, stored producer decision, or strict
version of a weak inequality is an acceptance rule.

## 7. Tightening to the ordered cone

For raw endpoints \(L=(B_0,C_0,H_0)\) and
\(U=(B_1,C_1,H_1)\), define

\[
L^\sharp=
(B_0,\max(B_0,C_0),\max(B_0,C_0,H_0)),
\tag{26}
\]

\[
U^\sharp=
(\min(B_1,C_1,H_1),\min(C_1,H_1),H_1).
\tag{27}
\]

Every point of \(\mathcal B(L,U)\) satisfying \(b\le c\le H\) lies in
\(\mathcal B(L^\sharp,U^\sharp)\), and conversely every ordered point of the
latter box lies in the former. Thus

\[
\mathcal B(L,U)\cap\{b\le c\le H\}
=
\mathcal B(L^\sharp,U^\sharp)\cap\{b\le c\le H\}.
\tag{28}
\]

If some coordinate of \(L^\sharp\) exceeds the corresponding coordinate of
\(U^\sharp\), the ordered intersection is empty. Otherwise all leaf tests
and splits are applied to the tightened endpoints. Although the tightened
box may still contain unordered points, including them in the DP bound only
enlarges the comparison class.

## 8. The closed interval tree

The certificate root is the integer box

\[
L_{\mathrm{root}}=(q,q,5q),\qquad
U_{\mathrm{root}}=(24q,24q,24q).
\tag{29}
\]

Its ordered part is exactly the scaled parameter region \(\mathcal P\).
A certificate is a finite rooted binary tree. Every node records its raw
integer endpoints and exactly one of the following types.

- An **empty node** satisfies the inverted-endpoint test after (26)--(27).
- An **analytic node** has nonempty tightened endpoints satisfying (25).
- A **DP node** has nonempty tightened endpoints and records the integer
  \(\mathcal V(L^\sharp,U^\sharp)\), recomputed by (12)--(20), with value at
  most \(q\).
- A **split node** has nonempty tightened endpoints, an axis \(i\), an integer
  split point \(d\) with
  \[
  L^\sharp_i<d<U^\sharp_i,
  \tag{30}
  \]
  and two children with raw boxes
  \[
  [L^\sharp,U^\sharp\text{ with }U^\sharp_i=d],
  \qquad
  [L^\sharp\text{ with }L^\sharp_i=d,U^\sharp].
  \tag{31}
  \]

The two children in (31) are closed and share the wall at \(d/q\). They cover
the entire tightened parent; duplicate coverage of the wall is harmless.
Combining this fact with (28) proves inductively that every ordered point of
the root reaches at least one leaf.

### Theorem 8.1 (accepted tree implies the finite obligation)

If a finite tree rooted at (29) satisfies every local condition above, every
reachable node occurs exactly once, every stored node is reachable, and every
branch ends in an empty, analytic, or DP leaf, then (FV) holds.

#### Proof

Fix \(\theta\in\mathcal P\). At a split, (28) and (31) send \(\theta\) to at
least one child. Finiteness and the absence of unterminated nodes send it to a
leaf. An empty leaf cannot contain \(\theta\). At an analytic leaf, (24)--(25)
give \(m-D_H\le0\). At a DP leaf, Proposition 5.1 and (22) give
\(q(m-D_H)\le q\). Thus \(m-D_H\le1\) for every
\(T\in\mathcal I_\theta\). \(\square\)

The split locations and the scale \(4096\) do not discretize
\(\mathcal P\). They describe finitely many closed rational boxes, each of
which is proved simultaneously for all real parameters it contains.

## 9. Exactness, termination, and failure behavior

A conforming checker must use integers for all endpoint, feasibility, score,
and recurrence calculations. Within the root, \(\ell_i\ge q\) and
\(h_+\le24q\), so every feasible point has total degree at most \(24\).
There are at most

\[
\binom{27}{3}=2925
\]

such lattice points. Also \(u_i\le24q\), and throughout the root

\[
-71q\le\overline\phi_{L,U}(x)\le2290q.
\]

For \(q=4096\), the absolute value of any score in (20) is therefore at most

\[
2925\cdot2290\cdot4096
=27{,}436{,}032{,}000<2^{63}.
\tag{32}
\]

Signed 64-bit arithmetic is sufficient for the specified quantities, though
arbitrary-precision integers make the checker simpler. An implementation must
separately bound any packed indices, sentinels, or transformed quantities it
introduces.

The checker must fail closed on:

1. an unrecognized schema version, a scale other than \(4096\), or a root
   other than (29);
2. noninteger, malformed, inverted, missing, duplicated, or out-of-range
   fields;
3. an invalid node kind, split axis, split point, or child box;
4. a node reached more than once, an unreachable stored node, a cycle, a
   missing child, or an unterminated branch;
5. an empty or analytic leaf which fails its exact endpoint predicate;
6. a DP leaf whose stored value differs from a fresh recomputation or exceeds
   \(q\);
7. an unresolved or unsupported node, arithmetic overflow, or an incomplete
   traversal.

Expected node counts, timings, hashes, and historical success flags are not
acceptance predicates.

## 10. Required checking paths

If D2 retains this certificate, R2 must provide both of the following.

### Path A: compact exact checker

A small checker must parse the complete tree, reconstruct the expected raw
box at every node from its parent, check the closed coverage rules, recompute
every DP leaf by (17)--(20), and check every analytic and empty leaf. It must
not import the discovery producer.

### Path B: separated coverage and recurrence checks

A materially separate path must:

1. walk the tree independently and establish the root-to-leaf closed-box
   coverage without trusting Path A's traversal state; and
2. recompute every DP leaf from the direct rectangle recurrence (16), rather
   than Path A's prefix recurrence (17).

The two parts may share the immutable certificate and basic integer/JSON
facilities, but not producer-generated acceptance decisions or cached leaf
bounds. The recurrence replay alone does not establish tree coverage, and the
coverage walk alone does not establish a leaf inequality.

A fresh runner must reject sample or prefix modes, require all leaves, reject
optimized execution that disables correctness checks, record the hashes of
the specification, certificate, and checker sources, and emit the environment
and count fields required by V0.

The discovery producer is outside the trusted boundary. Once the tree is
declared immutable proof data, correctness requires complete fresh checking of
that data, not regeneration by the heuristic which originally found it.

## 11. Audit of the historical candidate

The frozen archive contains a candidate implementation with the following
roles.

| Historical file | Candidate role | Present status |
|---|---|---|
| [interval_certificate.py](../artifacts/wilf_four_generators_review_package_2026-09-11/round5/weight_arrangement/interval_certificate.py) | Discovery producer and prefix-DP tree generator | Untrusted producer |
| [full_interval_certificate.json](../artifacts/wilf_four_generators_review_package_2026-09-11/round5/weight_arrangement/full_interval_certificate.json) | Immutable candidate proof data | Not yet promoted |
| [verify_interval_certificate.py](../artifacts/wilf_four_generators_review_package_2026-09-11/round5/weight_arrangement/verify_interval_certificate.py) | Combined tree and flat prefix-DP checker | Candidate Path A |
| [independent_interval_dp.py](../artifacts/wilf_four_generators_review_package_2026-09-11/round5/structural_audit/independent_interval_dp.py) | Explicit-transition leaf checker | Candidate recurrence part of Path B |
| [independent_interval_coverage.py](../artifacts/wilf_four_generators_review_package_2026-09-11/round5/structural_audit/independent_interval_coverage.py) | Independent tree walk | Candidate coverage part of Path B |

The archived tree reports \(50{,}885\) nodes: \(25{,}442\) splits,
\(24{,}912\) DP leaves, and \(531\) analytic leaves. Its largest recorded
accepted numerator is \(4096\). These are provenance and regression
diagnostics only.

The candidate architecture matches the mathematical contract, but it is not
yet a conforming release component:

1. its essential checks use Python assertions, which optimized execution can
   disable, and no current runner rejects that mode;
2. its records lack the V0 schema version, specification hash, repository
   commit, complete command, environment, and explicit fresh/cache-free
   fields;
3. the explicit-transition checker permits a sample mode which a final runner
   must reject;
4. the coverage checker has fixed relative paths rather than a packaged
   command-line interface; and
5. the discovery producer, redundant degree-four calculation, generated
   outputs, and proof checkers have not yet been reduced to a minimal
   post-D2 package.

These are R2 and S3 packaging obligations if D2 retains the computation. They
do not invalidate the mathematical specification, and no archived result is
used here as proof of (FV).

## 12. Retained interface

The later proof may use B2.2 only through the following implication:

> an exact, fail-closed acceptance of a complete tree satisfying Sections
> 3--10 proves B2.2-FV, and B2.1 plus B2.2-FV proves the B2 weighted theorem.

At the present roadmap stage, the contract and its coverage theorem are
complete, but B2.2-FV itself remains unproved under V0. It will become a proof
dependency only if D2 retains the interval tree and R2 completes the required
fresh and independent checks.
