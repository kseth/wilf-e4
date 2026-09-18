# Two genuine five-generator obstructions to the three-dimensional structure

These are structural obstructions to extending the current proof unchanged.
They are **not counterexamples to Wilf's conjecture**. Both are actual,
minimally five-generated numerical semigroups, with unique factorizations
for their displayed Apéry representatives.

## 1. A genuine Apéry ideal with a chordless four-cycle

Let

\[
S=\langle 9,12,15,19,20\rangle.
\]

Use coordinate weights \((19,20,12,15)\), and put

\[
T=\{0,e_1,e_2\}+\{0,e_3,e_4\}.
\]

Thus \(|T|=9\), and its weighted labels are
\(0,12,15,19,20,31,32,34,35\). Their residues modulo 9 are all distinct.
The minimal excluded points are exactly

\[
2e_1,\ e_1+e_2,\ 2e_2,\ 2e_3,\ e_3+e_4,\ 2e_4.
\]

In particular none has full support. They have the following strict
semigroup reductions:

\[
\begin{aligned}
2(19)&=20+2(9),&19+20&=12+3(9),\\
2(20)&=19+12+9,&2(12)&=15+9,\\
12+15&=3(9),&2(15)&=12+2(9).
\end{aligned}
\]

Every exponent outside \(T\) dominates one of these points, so its
weighted value minus 9 belongs to \(S\). Therefore every Apéry
factorization lies in \(T\). Since \(T\) supplies all nine distinct
residues, it is exactly the Apéry exponent ideal. This also proves
uniqueness of the Apéry factorizations. All five displayed generators
are minimal (as can be checked directly below 21).

The graph on the positive unit levels has edges

\[
\{1,3\},\quad\{1,4\},\quad\{2,3\},\quad\{2,4\}.
\]

It is the chordless cycle \(1-3-2-4-1\). Thus the coordinate-level graph
used in the three-variable argument is no longer necessarily chordal,
even for an actual Apéry ideal. The three-variable proof relies on an
induced cycle repeating one of three coordinate classes; four classes
allow precisely this obstruction.

There is also no decomposition into a central lower box plus four
coordinate horns whose transverse sections stay within that central
box. Indeed, the upper corner of any central box belongs to \(T\) and
uses at most two coordinates. If it uses two, they form an edge of this
cycle, and the complementary edge is also in \(T\). That point exceeds
the central corner in two coordinates. The same conclusion is immediate
for a central corner using at most one coordinate. A coordinate horn
could exceed it in only its own coordinate.

The semigroup has \(c=27\), \(n=9\), and \(W_5=18\).

## 2. Pair projections do not determine a genuine no-full-corner ideal

Let

\[
S=\langle14,21,29,30,32\rangle,
\]

use coordinate weights \((29,30,32,21)\), and set

\[
T=\{0,1\}^4\setminus\bigl((1,1,1,0)+\mathbb N^4\bigr).
\]

Its 14 points are labeled bijectively modulo 14: the first three bits,
with residue weights \(1,2,4\), take the values \(0,\ldots,6\), and
the last bit adds either 0 or 7. Its minimal excluded points are

\[
2e_1,\ 2e_2,\ 2e_3,\ 2e_4,\ (1,1,1,0).
\]

Their strict reductions are

\[
\begin{aligned}
2(29)&=30+2(14),&2(30)&=32+2(14),\\
2(32)&=29+21+14,&2(21)&=3(14),\\
29+30+32&=21+5(14).
\end{aligned}
\]

The same argument as above proves this is exactly the unique-factorization
Apéry ideal of this minimally five-generated semigroup.

There is no full-support minimal excluded point, but there is a
support-three exclusion. Every coordinate-pair projection of \(T\) is
the entire Boolean square \(\{0,1\}^2\). Their cylindrical intersection
is consequently all of \(\{0,1\}^4\), which wrongly includes
\((1,1,1,0)\) and \((1,1,1,1)\).

Thus two independent properties of the three-variable proof fail in
four variables: absence of a full-support corner no longer makes pair
projections sufficient, and even when pair projections are sufficient
the associated graph need not be chordal.

## 3. What this says about generalization

Embedding dimension \(e\) uses \(d=e-1\) Apéry exponent variables.
The present three-dimensional geometric classification is genuinely
specific to \(e=4\). Extending the proof to \(e=5\) needs additional
structure capable of treating higher-support exclusions and cycles of
pairwise compatibility. Merely replacing three horns by four does not
cover all actual Apéry ideals.

This does not obstruct dimension-independent arithmetic identities,
surface inequalities, residue injections, or a different geometric
classification. It identifies exactly why the current short structural
decomposition does not transfer automatically.

## Reproduction

Run `python3 round9/check_dimension_obstruction.py`.
The standard-library checker independently computes Apéry sets using
shortest paths, checks minimal generation by integer membership,
enumerates all minimal excluded points and strict reductions, verifies
the graph and pair projections, and writes
`round9/dimension_obstruction_checks.json`.
