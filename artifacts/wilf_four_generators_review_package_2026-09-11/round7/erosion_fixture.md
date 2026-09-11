# A residual-corner geometric counterexample, excluded by arithmetic

This note records a **counterexample to an auxiliary geometric inequality**, not
a counterexample to Wilf's conjecture. All counts below are reproduced by the
standalone standard-library checker `verify_erosion_fixture.py`.

Define a finite lower ideal by its heights:

\[
T=\{(x,y,z):0\le z<h_{x,y}\},
\]

where the six rows indexed by \(x=0,\ldots,5\), with entries indexed by \(y\), are

\[
(6,5,4,3,2,1),\quad(4,4,2,2),\quad(3,3,2),\quad(2,2),\quad(2),\quad(1).
\]

An absent entry has height zero. The entries are nonincreasing in both directions,
so this defines a lower ideal. Its unique full-support minimal excluded point is
\(p=(1,2,2)\), with \(|p|_1=5\). For unit weights,

\[
m=48,\qquad M=5,\qquad \sum_{x\in T}|x|_1=170,
\]

and therefore

\[
D=3mM-4\sum_{x\in T}|x|_1=40,\qquad m-D=8.
\]

Thus both the proposed geometric bound \(D\ge m-1\) and the weaker
\(m-D\le29/10\) fail even for \(m\ge30\) and a residual full corner of degree
five. Merely excluding the already settled corners \((1,1,1)\) and permutations
of \((2,1,1)\) does not make either generic geometric assertion true.

## Plane restrictions exclude this ideal

The mixed minimal excluded points on the three coordinate planes have counts
\((5,4,4)\), indexed by the omitted coordinate. These exceed the previously
derived Apéry limit \(|p|_1-2=3\). The counts of those plane corners dominating
the corresponding two-coordinate projection of \(p\) are \((3,3,3)\); these
exceed the respective complementary-coordinate limits \((1,2,2)\).

## A separate exclusion by residue injectivity

Let \(B=\{0,e_1,e_2,e_3\}\) and define

\[
A=\{x\in T:x+B\subseteq T\}.
\]

Direct enumeration gives

\[
|A|=23,\qquad |A-B|=55>48=|T|.
\]

This prohibits every additive residue labeling that is injective on \(T\) and
takes values in a group of order \(48\). Indeed, suppose \(\phi\) is such a
labeling and two elements \(a-b,a'-b'\in A-B\) have the same label. Then
\(a+b',a'+b\in T\) have the same label. Injectivity on \(T\) forces their
equality as vectors, hence \(a-b=a'-b'\). Therefore \(\phi\) would be injective
on \(A-B\), contradicting \(|A-B|>48\).

The obstruction is independent of the particular generator weights and does not
use the plane-corner bounds.

## Intersecting-corner distinctness alone does not exclude it

There are 17 minimal excluded points and 120 pairs with intersecting supports.
For a cyclic residue labeling modulo 48, the necessary full-corner relation is
\(a+2b+2c\equiv0\pmod{48}\). Enumerating all \(48^2=2304\) resulting triples:

- 192 assign different residues to every pair of corners with intersecting
  supports.
- None assigns distinct residues to all 48 points of \(T\).

For example, \((a,b,c)\equiv(42,1,2)\pmod{48}\) passes the intersecting-corner
check, while the points \((0,2,0)\) and \((0,0,1)\) in \(T\) collide.
Thus this weaker corner-labeling restriction does not replace the full Apéry
residue condition or its erosion consequences.

## Status

All statements in this note are exact finite calculations or the injection
argument above. The fixture establishes a failure of the generic residual
geometric shortcut. It makes no claim about whether the desired inequality holds
for every **genuine** preferred Apéry ideal in the remaining class.
