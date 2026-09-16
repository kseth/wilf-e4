# D3: three-plane simplification decision

**Status date:** 2026-09-16

## Decision

Adopt the analytic
[three-plane projection theorem](../paper/three-plane-projection.md).
Remove the compressed-shape, residue-label, and modular-cut computation from
the retained B3 branch. R3 is no longer required and has not been executed.

The successful replacement uses more of the actual branch hypotheses than
the historical six-window theorem did:

\[
p=(1,1,1)
\quad\Longrightarrow\quad
\text{three plane sections, each with at most one mixed corner}.
\]

A direct geometric count now proves

\[
\Phi(T,\operatorname{Max}(T))<0
\quad\Longrightarrow\quad |T|\le29.
\tag{1}
\]

The case partition already routes B3 only when \(m=|T|\ge30\).
The projection score is therefore nonnegative, and G3 proves \(W_4\ge0\).
There is no residual computed assertion in this branch.

This is an internally checked analytic proof, not an external review or
formalization. The main theorem remains proposed while B4--B6 and the later
review tasks are unfinished.

## 1. Why the broader six-window target was unnecessary

B3.2 and B3.3 reconstructed a theorem for *every* preferred Apéry ideal with
at most six final-window points. That theorem allows no full-support corner,
or a full-support corner other than \((1,1,1)\). Its negative-score shapes can
have three-dimensional interiors and many mixed corners in a plane.

The B3 routing cell is much narrower. Minimal exclusion of \((1,1,1)\)
forbids every three-positive-coordinate point and includes the three pair
points \(e_i+e_j\). The opposite-axis argument of B3.1 further permits only
one mixed corner per plane. Each plane frontier is therefore a rectangle, a
two-mixed-maxima split frontier, or a one-mixed-maximum side cap.

These stronger structural facts are lost when the only retained hypothesis
is \(|Z|\le6\). The analytic replacement restores them rather than seeking a
uniform improvement on the broader shape enumeration.

## 2. The replacement and its key accounting

The proof separates the origin, positive axes, and positive plane interiors.
For each plane it records the mixed-point count, a frontier correction, and
any capped-axis length. The aggregate quantities satisfy

\[
m=1+h+B+C,\qquad B\le C+s+N,\qquad N\ge2J.
\tag{2}
\]

Here \(h\) is the sum of the three axis lengths, \(s\le3\) counts split
frontiers, \(N\) charges side-capped axes, and \(J\) counts the lengths of
globally maximal axes. Each globally maximal axis must be capped in both
incident planes, which explains the factor two.

Writing \(k=|\operatorname{Max}(T)|\le6\) and

\[
Q=h+C+N-J,
\]

the exact projection-score identity is

\[
\Phi(T,\operatorname{Max}(T))=Q+3-3k.
\tag{3}
\]

A strictly negative integer score gives \(Q\le14\). Equations (2) then yield

\[
m\le1+2Q-h+s\le1+28-3+3=29.
\tag{4}
\]

This is the entire cardinality reduction. No compressed seed list, insertion
argument, lower-ideal extension queue, residue feasibility, weight ordering,
integer-lift enumeration, or numerical solver enters it.

For the actual final window \(Z\subseteq K=\operatorname{Max}(T)\), adding
points only increases \(E\), so \(\Phi(T,Z)\ge\Phi(T,K)\). Consequently the
ordinary G3 inequality applies directly at \(m\ge30\). It accepts the
projection equality boundary and permits \(Z\) to be a proper subset of \(K\).

## 3. The multiplicity hypothesis cannot simply be deleted

The geometric claim \(\Phi(T,K)\ge0\) is false without a size condition.
Take the origin, axes of positive lengths two, and in each coordinate plane
the positive points \((1,1),(1,2),(2,1)\). This is a 16-point lower ideal with
full corner \((1,1,1)\) and one mixed corner \((2,2)\) in each plane.

It has six maxima, \(P=24\), and \(E(K)=12\), so

\[
\Phi(T,K)=24-18-12=-6.
\]

This is a geometric obstruction to removing the size hypothesis, not a
semigroup counterexample. Smaller multiplicities are already handled by B1.
The new result is exactly the B3 branch theorem needed by the partition, not
an analytic proof of the unrestricted six-window theorem.

## 4. Dependency audit

Removing the broader six-window theorem must not leave a hidden skip rule in
another branch.

- B1's retained generator-box checks do not use six-window or corner
  classification.
- B2's retained horn theorem and interval checks are geometric and do not
  invoke the six-window theorem.
- B4's retained high-height tree and low-height short-corner certificates do
  not use a six-maxima skip.
- The obsolete residual low-height LP route did skip shapes with at most six
  maxima. The selected B5 local-or-axis contract does not: it quantifies over
  the entire specified class. In its
  [historical independent implementation](../artifacts/wilf_four_generators_review_package_2026-09-11/round10/local_centroid/independent_two_step.cpp),
  the six-maxima counter is diagnostic, with no rejection or skip following
  it.
- B6's strip and interval contracts do not invoke the six-window theorem.

Thus the selected proof spine does not require the broader theorem elsewhere.
B4.3 and B5.4 must preserve that property when their finite domains are
specified: no rejection based solely on six maxima is authorized by D3.
Their later replay audits must also check for such hidden exclusions.

The B3.2 and B3.3 notes remain available as fully specified alternatives for
the broader theorem, but their finite assertions are not established or
promoted under V0. They should be excluded from the eventual minimal proof
package unless a separately justified future task requires them.

## 5. Bounded diagnostic

The standalone
[diagnostic script](check_b3_planar_bound.py) constructs literal point sets
from all ordered plane profiles with bounded axis lengths, independently of
the archived search and certificates. It recomputes lower closure, maxima,
projection sizes, and maximal degrees, and checks all identities and
inequalities used in the analytic proof. For negative profiles it also checks
every nonempty subset of the maximal set.

Command:

    python3 research/check_b3_planar_bound.py --axis-limit 5

The run checked 166,375 ordered profiles. There were 25 negative-score
profiles: 3 with four maxima, 9 with five, and 13 with six. Their largest
cardinality was 21 and their minimum score was \(-6\). All identities and
inequalities agreed.

These are bounded diagnostics only. They do not supply coverage for arbitrary
axis lengths, prove a sharper cutoff, or establish B3.3-FV. Theorem 1.1's
symbolic argument supplies the unbounded coverage and is the retained proof.
The script is a research aid, not required release proof code.

## 6. Gate closure and attribution

D3 is closed with a proved replacement:

1. retain B3.1's opposite-axis and plane-frontier lemma;
2. retain the new three-plane negative-score bound;
3. apply G3 using \(m\ge30\) and final-window subset monotonicity;
4. remove all B3 finite verification and discharge the conditional R3 edge;
5. keep the broader six-window specifications as explicitly superseded
   alternatives, with no implied replay; and
6. proceed to B4.1 in the ready queue.

The inherited preferred-ideal, exclusion, and projection inputs remain
attributed in the foundations and G3 notes. This decision makes no novelty or
priority claim for the new counting lemma; L3 will search its precise final
statement before manuscript attribution is frozen.
