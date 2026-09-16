# Published reductions against the retained proof route

**Status date:** 2026-09-16 (route annotations updated; source audit 2026-09-12)

## Decision

The published conductor, left-element, and type results do not remove any of
the seven geometric branches, and they do not materially reduce the
generator-box computation for \(20\le m\le29\). Marashdeh's proved results
also do not supply the positive surplus required by the moment method. The
proof should therefore retain its present moment-deficit architecture.

One published input does give a clean, free geometric reduction. If
\(K=\operatorname{Max}(T)\) is the set of coordinatewise maximal points of the
preferred Apéry lower ideal, then

\[
  \operatorname{type}(S)\le |K|.
\tag{1}
\]

The Fröberg--Gottlieb--Häggkvist inequality therefore settles every preferred
Apéry ideal with \(|K|\le3\). Every unresolved four-generator branch may
henceforth assume

\[
  |K|\ge4.
\tag{2}
\]

This sharpens the entry to B3 from \(|K|\le6\) to \(4\le |K|\le6\). It is also
an exact, inexpensive filter wherever a later finite shape enumeration already
constructs \(T\). It does not justify adding type computation to the B1
generator search.

## 1. The common hard-case boundary

Write

\[
  n=|S\cap[0,c)|,\qquad
  W_4(S)=4n-c,
\]

and let \(t=\operatorname{type}(S)\). The following published theorems imply
that a counterexample of embedding dimension four would have to satisfy

\[
  c>3m,\qquad n\ge13,\qquad t\ge4.
\tag{3}
\]

The inputs are, respectively:

1. Eliahou's theorem that \(c\le3m\) implies Wilf's inequality;
2. Eliahou--Marín-Aragón's theorem that \(n\le12\) implies Wilf's inequality;
3. the Fröberg--Gottlieb--Häggkvist inequality \(c\le(t+1)n\), which implies
   Wilf's inequality when \(t\le e-1=3\).

In the notation of the present proof, \(M=c+m-1\), so the conductor condition
in (3) is exactly

\[
  M\ge4m.
\tag{4}
\]

These are valid preliminary assumptions, but only (2) interacts directly with
the geometry already used by the proof.

### The type-to-maxima bridge

Label \(x\in T\) by \(a\mathbin\cdot x\in\operatorname{Ap}(S,m)\). If \(x\)
is not coordinatewise maximal, then \(x+e_i\in T\) for some \(i\), and

\[
  a\mathbin\cdot(x+e_i)-a\mathbin\cdot x=a_i\in S\setminus\{0\}.
\]

Thus the label of \(x\) is not maximal in the Apéry poset. The maximal
elements of that poset are the translates by \(m\) of the pseudo-Frobenius
numbers, so their number is \(t\). This proves (1). Combining (1) with the
classical type bound proves the low-maxima disposal (2).

The converse to (1) is neither asserted nor needed: a coordinatewise maximal
factorization may fail to label a maximal element of the Apéry poset because
semigroup comparability need not be coordinatewise comparability in the chosen
factorizations.

## 2. Effect on the B1 finite obligation

For \(20\le m\le29\), the current finite contract first enumerates all sorted
generator triples in the box

\[
  m<a<b<c\le B_m=m(m-2),
\]

then computes exact Apéry distances (or ordinary membership) in order to test
\(M\le B_m\) and \(W_4\ge0\).

The published restrictions do not reduce the raw generator box:

- \(c>3m\), equivalently \(M\ge4m\), is a lower bound on an invariant known
  only after the Apéry or membership calculation; it supplies no smaller
  upper bound on \(a,b,c\).
- \(n\ge13\) is likewise known only after the conductor and genus have been
  determined. At that point the checker already has the data needed for
  \(W_4\).
- Testing \(t\ge4\) requires the Apéry partial order or pseudo-Frobenius
  numbers and is strictly more machinery than the present Wilf calculation.
- Constructing the preferred exponent ideal merely to apply (2) would add a
  third representation to a search that currently needs only residue
  distances or integer membership.

Consequently none of these conditions reduces the dominant traversal or
arithmetic of either proposed B1 checker. Importing them into the formal
finite domain would add external dependencies and predicates without removing
a proof obligation. The subsequent
[D1 gate](../research/b1-simplification-decision.md) therefore retains the B1
contract unchanged. Conditions (3) and (4) may be logged as diagnostics, but
they are not acceptance criteria.

## 3. Effect on the geometric branches

The later branches are organized by the full-support minimal exclusion \(p\),
its degree, the maximum exponent degree \(R\), and normalized weighted height
\(H=M/A\). Neither \(c>3m\) nor \(n\ge13\) provides a useful bound on those
parameters: (4) is only a lower bound on \(M\), while \(A\) varies with the
nonmultiplicity generators, and \(n\) is not \(|T|=m\).

The low-type result has the following limited but genuine effect:

| Branch | Consequence of \(|K|\ge4\) |
|---|---|
| B2 | Available as a free post-generation filter, but it does not simplify the current horn compactness parameters. |
| B3 | Gives \(4\le|K|\le6\) as an explanatory hard-case restriction; D3 now closes the branch analytically without needing the lower bound or a shape filter. |
| B4 | Available for low-height generated shapes, but no analytic height or cardinality bound follows from it. |
| B5 | Available contextually, but the retained local-or-axis contract checks all shapes in its class, including those with at most six maxima; the older six-window skip is not retained. |
| B6 | No useful translation to the strip or high-height interval parameters is presently known. |

Thus (2) belongs in the clean proof spine, while the other published
restrictions remain contextual boundary results.

## 4. Marashdeh's defect decomposition

Marashdeh proves the exact identity

\[
  W(S)=(e-t-1)n+\sigma(S)+\Theta(S),
  \qquad \sigma(S),\Theta(S)\ge0,
\tag{5}
\]

and the type bound

\[
  t\le e-1+\Xi(S)\le e-1+\Theta(S).
\tag{6}
\]

For \(e=4\), (5) is

\[
  W_4=(3-t)n+\sigma+\Theta.
\tag{7}
\]

In the hard range \(t\ge4\), Wilf's inequality therefore requires
\(\sigma+\Theta\ge(t-3)n\), whereas the proved part of (6) gives only
\(\Theta\ge t-3\). This is the factor-of-\(n\) gap identified explicitly in
Marashdeh's paper. It does not control the moment surplus \(D_0\), a corner
type, or any of the finite branch parameters.

There is also an exact reason not to reroute the proof through Marashdeh's
Conjecture 5.2. Write the pseudo-Frobenius numbers as
\(f_1<\cdots<f_t=F\), put
\(\lambda(f)=|S\cap[0,f]|\), and use

\[
  \Theta=\sum_{i=1}^t\lambda(f_i)-g.
\]

For \(e=4\), the conjectured margin is

\[
\begin{aligned}
  J
  &=\Theta-\sum_{i=1}^{t-3}\lambda(f_i)\\
  &=\lambda(f_{t-2})+\lambda(f_{t-1})+n-g\\
  &=W_4-
    \bigl(n-\lambda(f_{t-2})\bigr)-
    \bigl(n-\lambda(f_{t-1})\bigr).
\end{aligned}
\tag{8}
\]

The two subtracted terms are nonnegative. Hence \(J\ge0\) asks for a
pointwise stronger inequality than \(W_4\ge0\), not a smaller lemma on the
way to it. Proposition 5.1 is a valid lower bound for \(W\), but the condition
that makes that bound nonnegative is conjectural and does not reduce the
present proof burden.

**Decision:** cite (5)--(6) as an adjacent modern reformulation and retain the
moment-deficit route. Do not introduce \(\sigma,\Theta,\Xi\), or the ordered
pseudo-Frobenius numbers into a branch contract.

## 5. Chomicz's September type result

Chomicz's September 2026 preprint proves, for embedding dimension four,

\[
  4t(S)+5\ge\eta(S)\ge t(S)-11,
\]

where \(\eta(S)\) is the cardinality of a minimal presentation. This is a
substantial relation between the two invariants, but it is not an absolute
upper bound on \(t\), and the retained proof does not control
\(\eta\). It therefore gives no new Wilf subcase or branch estimate. The
earlier decision to use Chomicz's L-shape work as geometric context, rather
than as a proof dependency, is unchanged.

## 6. Architectural handoff

The outcome of L2 is therefore:

1. adopt the low-maxima disposal \(|\operatorname{Max}(T)|\le3\) analytically;
2. retain \(c>3m\), \(n\ge13\), and \(t\ge4\) in the literature boundary,
   without adding their invariant tests to B1;
3. retain all B2--B6 routes, allowing later specifications to discard
   generated shapes with at most three coordinatewise maxima;
4. decline a Marashdeh-defect or Chomicz-presentation reroute;
5. recommend retaining the exact B1 finite obligation; the subsequent D1 gate
   accepted that recommendation after also checking the analytic alternatives.

This is a theorem-level comparison of the sources named above, not a renewed
claim that the entire literature is exhausted. The branch-level search L3
must be repeated after D1--D6 determine the final surplus statements.

## Sources

- Shalom Eliahou, “Wilf's conjecture and Macaulay's theorem,” *Journal of the
  European Mathematical Society* **20** (2018), 2105--2129.
  [arXiv:1703.01761](https://arxiv.org/abs/1703.01761).
- Shalom Eliahou and Daniel Marín-Aragón, “On numerical semigroups with at
  most 12 left elements,” *Communications in Algebra* **49** (2021),
  2402--2422.
  [arXiv:2006.01480](https://arxiv.org/abs/2006.01480).
- Ralf Fröberg, Christian Gottlieb, and Roland Häggkvist, “On numerical
  semigroups,” *Semigroup Forum* **35** (1987), 63--83.
  [doi:10.1007/BF02573091](https://doi.org/10.1007/BF02573091).
- Mohammad F. Marashdeh, “An upper bound for the type of a numerical
  semigroup, and a reduction of Wilf's conjecture,” arXiv:2608.12531v1,
  2026. [arXiv](https://arxiv.org/abs/2608.12531).
- Kazimierz Chomicz, “The type and cardinality of minimal presentations of
  numerical semigroups with embedding dimension four,” arXiv:2609.04000v1,
  2026. [arXiv](https://arxiv.org/abs/2609.04000).
