# The six-window modular-cut specification

## Status and purpose

This note completes roadmap task B3.3. It states the exact finite arithmetic
obligation for the six-window branch and proves that it covers every ordered
residue labeling, every possible value of the final cut, every integer lift of
the residues, and every equality case.

The input family is supplied by the
[B3.2 shape specification](six-window-shape-specification.md). The proof uses
only the [coordinate-line identity](coordinate-lines.md) and the fact, proved
in the [foundations](foundations.md), that a preferred Apéry ideal contains one
representative of every residue modulo its cardinality.

This is a **specification and coverage proof**, not a replay result. It does
not establish the finite inequality below or endorse the historical output.
That question belongs first to the D3 simplification gate and, if computation
is retained, to R3 under the
[verification trust policy](../verification/trust-policy.md).

One useful simplification is already definitive: the modular cuts alone imply
the branch theorem. The historical real-weight linear programs and their
rational dual certificates are logically redundant and need not be retained
in the final verification package.

## 1. Finite objects and exact predicate

For an integer \(r\) and a positive integer \(m\), write

\[
[r]_m\in\{0,1,\ldots,m-1\}
\tag{1}
\]

for the least nonnegative residue of \(r\) modulo \(m\).

Let \(\mathcal G_{\le6}\) be the finite family of canonical pairs \((T,Z)\)
specified in B3.2. A conforming checker may replace it by a declared finite
superset, as permitted there. Let

\[
\mathcal T_{\le6}
=\{T:(T,Z)\in\mathcal G_{\le6}\text{ for some }Z\}
\tag{2}
\]

be the set of distinct underlying lower ideals. Deduplicating \(T\) is safe:
the arithmetic predicate below depends on \(T\), not on which final-window
candidate \(Z\) led to it.

Fix \(T\in\mathcal T_{\le6}\) and put \(m=|T|\). For

\[
A=(A_1,A_2,A_3)\in\{1,\ldots,m-1\}^3,
\]

define

\[
\rho_A:T\longrightarrow\mathbb Z/m\mathbb Z,
\qquad
\rho_A(x)=[A\mathbin\cdot x]_m.
\tag{3}
\]

The admissible ordered residue labelings of \(T\) are

\[
\mathcal A(T)
=\left\{
A\in\{1,\ldots,m-1\}^3:
A_1,A_2,A_3\text{ are pairwise distinct and }\rho_A
\text{ is bijective}
\right\}.
\tag{4}
\]

The adjectives in (4) are intentional. Coordinates are ordered; no quotient
by permutations is taken at this stage. No ordering such as
\(A_1<A_2<A_3\), no coprimality condition on an individual \(A_i\), and no
unit condition in \(\mathbb Z/m\mathbb Z\) may be imposed.

For \(j\in\{1,2,3\}\) and \(y\in\pi_jT\), let

\[
\ell_{j,y}=\{x\in T:\pi_jx=y\}.
\]

Since \(T\) is a lower ideal, this is a coordinate line of the form

\[
\ell_{j,y}=\{t-qe_j,\ldots,t-e_j,t\}.
\]

Write \(t_\ell=t\) for its top and \(L_\ell=q+1\) for its length. Lines in
different coordinate directions remain distinct indexed objects, even when
their tops coincide. Set

\[
\mathcal L_j(T)=\{\ell_{j,y}:y\in\pi_jT\},
\qquad
\mathcal L(T)=\mathcal L_1(T)\mathbin{\dot\cup}
\mathcal L_2(T)\mathbin{\dot\cup}\mathcal L_3(T).
\]

For \(A\in\mathcal A(T)\) and \(f\in\{0,\ldots,m-1\}\), define the modular
line-cut value

\[
\mathcal R_f(T,A)
=\sum_{\ell\in\mathcal L(T)}
L_\ell[f-A\mathbin\cdot t_\ell]_m
\tag{5}
\]

and its slack

\[
\Delta_f(T,A)=\mathcal R_f(T,A)-m(m-1).
\tag{6}
\]

The complete finite obligation is:

> **B3.3-FV (modular-cut obligation).** For every
> \(T\in\mathcal T_{\le6}\), every \(A\in\mathcal A(T)\), and every
> \(f\in\{0,\ldots,m-1\}\),
> \[
> \boxed{\Delta_f(T,A)\ge0.}
> \tag{7}
> \]

If \(\mathcal A(T)=\varnothing\), (7) is vacuous. This is correct rather than
a discarded case: Section 2 proves that such an ideal cannot be a preferred
Apéry ideal with the given coordinate orientation.

## 2. Coverage of residue labelings and coordinate symmetry

Let

\[
S=\langle m,a_1,a_2,a_3\rangle
\]

be a four-generator numerical semigroup and let \(T\) be its preferred Apéry
ideal. Set

\[
A_i=[a_i]_m.
\tag{8}
\]

### Lemma 2.1 (all actual labelings occur)

The ordered triple \(A=(A_1,A_2,A_3)\) belongs to \(\mathcal A(T)\).

#### Proof

The preferred labels \(a\mathbin\cdot x\), for \(x\in T\), represent all
\(m\) residue classes exactly once. Reduction modulo \(m\) is precisely the
map \(\rho_A\), so this map is bijective.

The lower ideal \(T\) contains \(0,e_1,e_2,e_3\). Their residues are
\(0,A_1,A_2,A_3\). Bijectivity therefore forces each \(A_i\) to be nonzero
and the three entries to be pairwise distinct. Thus \(A\) occurs in the
ordered enumeration (4). \(\square\)

The bijection test in (4) is not replaceable by the pairwise-distinct test:
it must examine the residues of all \(m\) points of \(T\). Conversely, because
the domain and codomain both have cardinality \(m\), checking distinctness of
those \(m\) residues is enough to prove bijectivity.

### Lemma 2.2 (canonical orientations lose nothing)

Suppose a simultaneous coordinate permutation sends an actual pair
\((T,Z)\) to the canonical pair \((T',Z')\). Permute the integer weight vector
\(a\) and the residue triple \(A\) so that

\[
a'\mathbin\cdot x'=a\mathbin\cdot x,
\qquad
A'\mathbin\cdot x'=A\mathbin\cdot x
\qquad(x'\text{ the image of }x).
\tag{9}
\]

Moreover \(A'\in\mathcal A(T')\), coordinate lines correspond with the same
lengths, and

\[
\mathcal R_f(T',A')=\mathcal R_f(T,A)
\tag{10}
\]

for every \(f\). For every \(M\), the same correspondence gives
\(D_{T'}(a',M)=D_T(a,M)\).

#### Proof

The chosen relabeling gives (9) and transports both the residue bijection and
the coordinate-line decomposition. Corresponding line tops have equal dot
products and corresponding lines have equal lengths, proving (10) and the
claim about \(D_T\). \(\square\)

Thus it is valid to quotient the geometric pairs by simultaneous coordinate
permutation in B3.2 and then enumerate *all ordered* triples in (4). Sorting
the residue entries after canonicalization would not be valid.

## 3. The lift from modular cuts to all integer weights

The principal benefit of (7) is that integer generator lifts never have to be
enumerated.

### Proposition 3.1 (modular domination)

Let \(T\subseteq\mathbb N^3\) be a finite lower ideal of cardinality \(m\).
Let \(a\in\mathbb Z_{>0}^3\), put \(A_i=[a_i]_m\), and let \(M\in\mathbb Z\)
satisfy

\[
M\ge\max_{x\in T}a\mathbin\cdot x.
\tag{11}
\]

If \(f=[M]_m\), then

\[
D_T(a,M)
=\sum_{\ell\in\mathcal L(T)}
L_\ell(M-a\mathbin\cdot t_\ell)
\ge\mathcal R_f(T,A).
\tag{12}
\]

#### Proof

For each line put

\[
\delta_\ell=M-a\mathbin\cdot t_\ell.
\]

Condition (11) makes \(\delta_\ell\) a nonnegative integer, while

\[
[\delta_\ell]_m=[f-A\mathbin\cdot t_\ell]_m.
\tag{13}
\]

Every nonnegative integer is at least its least nonnegative residue modulo
\(m\). Multiply (13) by the positive integer \(L_\ell\), sum over the indexed
lines, and use the line-slack identity. \(\square\)

This argument covers every lift

\[
a_i=A_i+m q_i
\tag{14}
\]

that can arise from actual generators, with no bound on the integers \(q_i\).
It also covers every possible \(M\): its only modular contribution is
\(f=[M]_m\), and (7) checks all \(m\) possibilities. Some triples or cuts in
the finite domain may not admit a semigroup realization; checking that larger
domain is harmless and avoids a separate lift-feasibility computation.

### Corollary 3.2 (B3.3 arithmetic implication)

Suppose \(T\) is the preferred Apéry ideal of \(S\) and B3.3-FV holds for its
canonical representative. Then

\[
W_4(S)\ge0.
\tag{15}
\]

#### Proof

For the preferred ideal,

\[
M=\max_{x\in T}a\mathbin\cdot x=c+m-1.
\]

By Lemmas 2.1 and 2.2, we may permute the ideal and integer weights into the
canonical orientation without changing \(M\) or \(D_T(a,M)\). Its ordered
residues occur in (7), and the cut \(f=[M]_m\) occurs there as well.
Proposition 3.1 and B3.3-FV give

\[
D_T(a,M)\ge\mathcal R_f(T,A)\ge m(m-1).
\]

The exact coordinate-line form of the moment identity is

\[
mW_4(S)=D_T(a,M)-m(m-1),
\]

which proves (15). \(\square\)

### Equality audit

Every comparison above is weak. A finite record with

\[
\Delta_f(T,A)=0
\]

is accepted. Equality in Wilf's inequality can occur in this argument only if
the selected cut has zero slack and every line deficit
\(M-a\mathbin\cdot t_\ell\) equals its least nonnegative residue. No strict
inequality, positive-margin assumption, or perturbation of a boundary point
is used. Thus the modular equality walls are included exactly.

The separate projection boundary \(\Phi(T,Z)=0\) is not part of the finite
domain: G3 already proves \(W_4\ge0\) there. B3.2 and B3.3 use the finite
route only when \(\Phi(T,Z)<0\).

## 4. Exact checking semantics

A conforming checker of B3.3-FV must implement the following mathematical
procedure.

1. Obtain the complete B3.2 family, or a declared safe superset, and
   deduplicate only identical lower ideals \(T\).
2. Validate each \(T\) as a finite lower ideal, validate its cardinality
   \(m\), and validate the B3.2 pair records separately. Stored acceptance
   flags and expected counts are not inputs to acceptance.
3. For every ordered triple of pairwise-distinct entries in
   \(\{1,\ldots,m-1\}\), compute (3) on every point of \(T\). Retain the
   triple exactly when all \(m\) residues are distinct.
4. Reconstruct every indexed coordinate line from \(T\), its exact length,
   and its top. Check the identities
   \[
   \sum_{\ell\in\mathcal L_j(T)}L_\ell=m
   \quad(j=1,2,3),
   \qquad
   \sum_{\ell\in\mathcal L(T)}L_\ell=3m
   \tag{16}
   \]
   as internal consistency conditions.
5. For every retained \(A\) and every integer
   \(f=0,1,\ldots,m-1\), compute (5) and reject if (7) fails. Zero slack is a
   success, not an exceptional case.
6. Fail closed on malformed or duplicate records, a missing cut, an
   incomplete loop, an unsupported cardinality, or any arithmetic operation
   whose exactness has not been justified.

All arithmetic in (3)--(7) is integral. Arbitrary-precision integers are the
simplest implementation choice. The line identity gives the useful a priori
bound

\[
0\le\mathcal R_f(T,A)
\le(m-1)\sum_\ell L_\ell
=3m(m-1),
\tag{17}
\]

and hence

\[
-m(m-1)\le\Delta_f(T,A)\le2m(m-1).
\tag{18}
\]

These bounds justify the final accumulator only after the supported range of
\(m\) has itself been established. A fixed-width implementation must also
bound or safely reduce every intermediate dot product. Lower closure gives
\(0\le x_i\le m-1\) for every \(x\in T\), and therefore

\[
0\le A\mathbin\cdot x\le3(m-1)^2.
\]

A fixed-width checker may use this bound together with an explicitly checked
range for \(m\). It may not silently skip a shape outside a hard-coded
bit-mask or integer range.

B3.3-FV quantifies over every generated ideal, label, and cut. A list of only
the label-feasible ideals is therefore a permissible output, but not a
trusted input, unless a separate complete path proves that every omitted
ideal has \(\mathcal A(T)=\varnothing\).

## 5. Sufficiency for the six-window branch

### Theorem 5.1 (conditional six-window theorem)

Assume B3.3-FV. If \(S\) is a four-generator numerical semigroup whose
preferred Apéry ideal has the corner \(p=(1,1,1)\), then

\[
W_4(S)\ge0.
\tag{19}
\]

#### Proof

B3.1 gives \(1\le|Z|\le6\) for the final window \(Z\). If
\(\Phi(T,Z)\ge0\), the G3 projection inequality proves (19). If
\(\Phi(T,Z)<0\), B3.2 sends \((T,Z)\), up to simultaneous coordinate
permutation, into \(\mathcal G_{\le6}\). Corollary 3.2 then proves (19).
\(\square\)

This theorem cleanly separates the two remaining questions. B3.2 proves that
the finite geometric family is exhaustive; B3.3 proves that the modular
predicate is sufficient. What is not yet established is the finite statement
B3.3-FV itself.

## 6. Audit of the historical arithmetic route

The frozen archive contains three relevant arithmetic components.

- [`check_residue_labels.cpp`](../artifacts/wilf_four_generators_review_package_2026-09-11/round7/six_point_dependency_replay/check_residue_labels.cpp)
  enumerates ordered nonzero pairwise-distinct triples and tests the residue
  bijection.
- [`verify_final_window.py`](../artifacts/wilf_four_generators_review_package_2026-09-11/round7/six_point_dependency_replay/verify_final_window.py)
  reconstructs coordinate lines and evaluates (6) for the historical
  \(|Z|\le5\) path.
- [`certify_six_point.py`](../artifacts/wilf_four_generators_review_package_2026-09-11/round7/six_point_dependency_replay/certify_six_point.py)
  evaluates the same modular cuts for the six-point family and also discovers
  optional real-weight linear-program certificates. The exact stored
  arithmetic is rechecked by
  [`verify_six_certificates.py`](../artifacts/wilf_four_generators_review_package_2026-09-11/round7/six_point_dependency_replay/verify_six_certificates.py).

The archived records report these diagnostics:

| Historical path | Ordered labelings | Modular cuts | Minimum slack |
|---|---:|---:|---:|
| \(|Z|=4\) | 8 | 80 | 0 |
| \(|Z|=5\) | 40 | 456 | 0 |
| \(|Z|=6\) | 930 | 23,002 | 0 |
| Split runners combined | 978 | 23,538 | 0 |

For \(|Z|\le3\), the historical geometric search reports no negative
projection-score pair and hence no modular cut. The six-point records report
71 label-feasible ideals. These values are regression targets and provenance
evidence only; B3.3-FV is not established by quoting them.

The historical linear-program layer contains 67 normalized certificates and
24 ordered certificates, covering all six orientations of the four remaining
shapes. It proves a broader real-weight fact on those shapes, but it
contributes nothing to Proposition 3.1 or Theorem 5.1 once all modular cuts
pass. Accordingly:

> **Dependency decision.** D3 and any eventual R3 implementation should not
> require the linear-program producer, SciPy, or the stored rational duals.
> They may remain in the immutable archive as diagnostics, but they are not
> part of the retained B3 proof contract.

The archived C++ labeling checker deliberately fails when \(m>64\), and the
stored B3.2 output reports \(m\le56\). Together with the dot-product bound
above, this makes its bit mask and integer arithmetic compatible with that
recorded output, but does not independently establish the bound for a fresh
replay. The source also does not validate every input extraction. If D3
retains computation, R3 must use exact integers or freshly establish and
check all fixed-width bounds, harden malformed-input handling, regenerate the
shapes rather than trust the stored candidate list, and provide the
independent generation-and-lifting path required by V0.

## 7. Retained interface

B3.1--B3.3 now give the following code-independent implication:

> If B3.3-FV holds for the distinct lower ideals generated by B3.2, then every
> preferred Apéry ideal in the \(p=(1,1,1)\) branch satisfies Wilf's
> inequality. The implication includes every coordinate orientation, every
> residue-bijective labeling, every modular cut, every integer generator
> lift, and equality.

The next task on this branch is D3: seek an analytic or substantially smaller
replacement for B3.3-FV. Only if that gate retains finite computation does R3
become necessary.
