# Four-generator type reduction: exact reformulation and obstruction

Date: 10 September 2026.

**Outcome.** The paper's proven type bound does not close the remaining Apéry class. A useful exact reformulation reduces its stronger conjecture to a correction involving the last three gaps. An independently checked genuine four-generator example with full corner `(1,7,4)` disproves the natural attempt to replace the full redundancy defect by the paper's lower bound. No counterexample to Wilf or to the paper's stronger conjecture was obtained.

## 1. Source and audited inputs

Mohammad F. Marashdeh, [*An upper bound for the type of a numerical semigroup, and a reduction of Wilf's conjecture*](https://arxiv.org/html/2608.12531v1), arXiv:2608.12531v1, 12 August 2026.

Sections 3–5 were checked directly. Write `PF={f_1<...<f_t}`, `F=f_t`, `c=F+1`, `n=|S∩[0,c)|`, `g=c−n`, and `λ(f)=|S∩[0,f]|`. The incidence count gives `Θ=Σ_i λ(f_i)−g`. Descending each residue class gives `Θ≥Ξ`, with

\[
\Xi=\sum_{w\in\operatorname{Ap}(S,m)\setminus\{0\}}
\left\lfloor\frac wm\right\rfloor(\nu(w-m)-1),
\qquad
\nu(x)=|\{f\in\mathrm{PF}:f-x\in S\}|.
\]

Theorem 4.4 proves `t≤e−1+Ξ≤e−1+Θ`. Proposition 5.1 supplies a sufficient inequality, and Conjecture 5.2 asserts that inequality universally. The latter is explicitly unproved and pointwise stronger than Wilf. Neither the type bound nor the associated genus bound resolves the case `t≥e`.

The incidence identity is a surjective finite-set count. The bound on Ξ uses only that `ν(w−jm)≥ν(w−m)` along the gaps of a residue. These arguments are valid; the obstacle is the size of the lower bound, not an error in those steps.

## 2. A direct four-generator reformulation

The following algebra and final-gap analysis are our deductions from the definitions. For `e=4` and `t≥4`, define the margin in the paper's stronger inequality by

\[
J(S)=\Theta-\sum_{i=1}^{t-3}\lambda(f_i).
\]

Cancelling the first `t−3` summands gives the exact identity

\[
\boxed{J(S)=\lambda(f_{t-2})+\lambda(f_{t-1})+\lambda(F)-g.}
\tag{1}
\]

Since `λ(F)=n` and `W_4=3n−g`, this is equivalently

\[
\boxed{J(S)=W_4-P(S),\qquad
P(S)=\bigl(n-\lambda(f_{t-2})\bigr)
     +\bigl(n-\lambda(f_{t-1})\bigr).}
\tag{2}
\]

Thus the stronger conjecture asks for `W_4≥P(S)`. In particular, proving Wilf itself would not automatically prove this stronger statement. The correction is nonnegative and can be strictly positive.

### The correction in the current residual class

Let

\[
k=|\operatorname{Ap}(S,m)\cap[c,c+m)|.
\]

The gaps in `[c−m,c)` correspond bijectively to these Apéry elements by adding `m`. Every such gap `f` is pseudo-Frobenius: for `s∈S\{0}`, `s≥m` implies `f+s≥c`.

If `k≥3`, the three largest gaps lie in this interval, are all pseudo-Frobenius, and therefore equal `f_{t-2},f_{t-1},F`. There is one gap after `f_{t-1}` and two after `f_{t-2}`. Counting the remaining integers gives

\[
n-\lambda(f_{t-1})=F-f_{t-1}-1,
\qquad
n-\lambda(f_{t-2})=F-f_{t-2}-2.
\]

Consequently,

\[
\boxed{P(S)=2F-f_{t-1}-f_{t-2}-3.}
\tag{3}
\]

Each of the two counted sets consists of nongaps in the last interval of length `m`, which contains exactly `m−k` nongaps. Hence

\[
\boxed{0\le P(S)\le2(m-k).}
\tag{4}
\]

The earlier six-point theorem restricts any still-possible counterexample to `k≥7`, so (3) applies throughout that residual class. The easy sufficient condition

\[
W_4\ge2(m-k)
\]

would imply the stronger conjecture there. We have **not** established this sufficient condition universally. It is stronger than necessary even for the stronger conjecture.

## 3. Why the proved lower bound cannot simply be substituted

Consider the genuine minimally four-generated numerical semigroup

\[
S=\langle155,1552,1647,1651\rangle.
\]

Its preferred Apéry ideal has unique full-support minimal excluded point `(1,7,4)`. Its exact invariants are

| Quantity | Value |
|---|---:|
| Multiplicity `m` | 155 |
| Conductor `c` | 17,979 |
| Genus `g` | 11,114 |
| Number of left elements `n` | 6,865 |
| Type `t` | 13 |
| Final-window count `k` | 7 |
| Wilf number `W_4` | 9,481 |
| Full redundancy `Θ` | 65,609 |
| Residue-chain lower bound `Ξ` | 22,130 |
| Required sum `Σ_{i≤10} λ(f_i)` | 56,287 |

The pseudo-Frobenius numbers and their left counts are:

| `f` | `λ(f)` |
|---:|---:|
| 12,360 | 2,417 |
| 13,813 | 3,337 |
| 16,157 | 5,168 |
| 16,351 | 5,326 |
| 17,511 | 6,421 |
| 17,610 | 6,512 |
| 17,879 | 6,772 |
| 17,883 | 6,775 |
| 17,887 | 6,778 |
| 17,891 | 6,781 |
| 17,895 | 6,784 |
| 17,899 | 6,787 |
| 17,978 | 6,865 |

Thus

\[
\Xi-\sum_{i\le10}\lambda(f_i)=-34,157<0,
\]

whereas

\[
J(S)=\Theta-\sum_{i\le10}\lambda(f_i)=9,322>0.
\]

The final-gap correction is `159`, and `9,481−159=9,322` independently checks (2). The proved lower bound loses too much information even on a genuine Apéry ideal with exactly the sort of interior corner remaining in the project. This example **does not** refute Wilf or Marashdeh's conjecture. It refutes only the stronger auxiliary assertion obtained by replacing Θ by Ξ.

An even simpler covering approach is impossible when `t>3`: the reflected gap sets associated with any three pseudo-Frobenius numbers cannot cover all gaps. A fourth pseudo-Frobenius number is maximal in the semigroup order and therefore cannot be dominated by any of those three. Cardinality inequality (1), if true, must exploit enough overlapping incidences to compensate for those uncovered gaps; it cannot follow from a literal three-set covering.

## 4. Verification and bounded search

`type_probe.py` computes Apéry representatives by exact shortest paths with lexicographic tie breaking, then evaluates the defects by residue formulas. Its deterministic diagnostic run proposed 12,000 tuples with `30≤m≤499` and the other generators at most `4m`. There were 7,885 minimally four-generated cases with `t≥4`, including 2,863 with `t≥7`. Of the 7,885, exactly 6,367 failed the proposed Ξ substitute. None failed `J≥0`.

Those counts describe a bounded diagnostic search; they are not a proof beyond the individual examples.

`verify_type_fixture.py` independently checks the displayed fixture by Boolean integer membership up to 18,133. A terminal block of 155 consecutive members proves that all later integers belong to the semigroup. It then counts the gaps, pseudo-Frobenius numbers, and domination incidences directly. Separate integer loops enumerate all nonmultiplicity factorizations below the largest Apéry value and recover the unique full corner. All assertions passed. The output is `type_fixture_independent_verification.json`.

No root proof dependencies or existing reports were modified. This note gives a precise alternative remaining inequality and a verified obstruction to one natural sufficient bound; it does not close the unrestricted four-generator conjecture.
