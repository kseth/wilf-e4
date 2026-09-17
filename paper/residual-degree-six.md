# Residual degree-six branch

## Scope and dependencies

This note reconstructs B5 for a preferred Apéry lower ideal \(T\), with
\(m=|T|\ge30\), unique full-support corner \(p\), and degree
\(R=\max_T|x|_1\le6\). Write \(P=|p|_1\); the case partition gives
\(5\le P\le7\).

The arithmetic inputs are the preferred representatives and collision rules
in [the foundations](foundations.md). All restrictions below are necessary,
not sufficient, for a geometric ideal to be an Apéry ideal. They impose no
maxima-count, erosion, or realizability skip.

## 1. B5.1: mixed plane corners

Each coordinate plane has at most \(P-2\) mixed minimal exclusions.

Fix the \(ij\)-plane and let \(k\) be its complementary coordinate.
A mixed corner \(q=q_i e_i+q_j e_j\) has representative
\(\gamma e_k\), with \(1\le\gamma\le h_k=\max_Tx_k\).
The representative is nonzero because \(q\) overlaps \(p\) and
the full corner has residue zero. Distinct plane corners have distinct
representatives by the collision rule.

There are at most \(p_i-1\) corners with \(q_i<p_i\), since the first
coordinates of an antichain of planar mixed corners are distinct. Likewise,
at most \(p_j-1\) have \(q_j<p_j\). These two upper bounds may overlap,
which only weakens their sum.

For every remaining corner, \(q_i\ge p_i,\ q_j\ge p_j\), and
\[
r=(q_i-p_i)e_i+(q_j-p_j)e_j\in T.
\]
Indeed \(r\le q-e_i\in T\). Since \(a\cdot p\equiv0\pmod m\),
the residue of \(r\) is \((\gamma+p_k)a_k\). If
\(\gamma+p_k\le h_k\), it collides with the distinct included point
\((\gamma+p_k)e_k\). Thus \(\gamma>h_k-p_k\), allowing at most \(p_k\)
distinct representatives.

Adding the three bounds gives
\[
(p_i-1)+(p_j-1)+p_k=P-2.
\]
This is a bound for each plane separately, not for the sum across planes.

## 2. B5.2: two-direction surface injection

For distinct coordinates \(i,j,k\), define
\[
F_i=\{x\in T:x+e_i\notin T\},\qquad n_k=1+\max_Tx_k.
\]
Then every residue-bijective finite lower ideal satisfies
\[
\boxed{|F_i\cap F_j|\le2n_k.}
\]
No degree or full-corner hypothesis is needed.

Let \(C_{ij}\) be the excluded points \(q\) with \(q_i,q_j>0\) and
both \(q-e_i,q-e_j\in T\). At each fixed \(k\)-level these are the mixed
corners of the nonempty planar slice. Every such slice is nonempty,
since its axis point belongs to \(T\).

A finite nonempty planar lower ideal with \(h\) maximal points has
\(h-1\) mixed corners: its positive column heights have \(h\) constant
blocks, and the boundaries between successive positive blocks are exactly
its mixed corners. This includes a single row, a single column, and a
rectangle. Thus
\[
|C_{ij}|=|F_i\cap F_j|-n_k.
\]
If \(\rho(q)\in T\) is the representative of \(q\), a positive
\(i\)-coordinate of \(\rho(q)\) would give distinct included points
\(q-e_i,\rho(q)-e_i\) of the same residue. Therefore \(\rho(q)_i=0\);
likewise \(\rho(q)_j=0\).
Distinct \(q,q'\in C_{ij}\) cannot have the same residue, since their
distinct \(i\)-predecessors would collide. Hence \(q\mapsto\rho(q)\)
injects \(C_{ij}\) into the \(k\)-axis, which contains exactly \(n_k\)
points. The bound follows.

Slice corners need not be globally minimal exclusions: the proof uses
only the two displayed predecessor conditions. It does not incorrectly
apply the full minimal-corner theorem to a slice.

## 3. B5.3: local and axis soundness

Put \(s=\sum_Tx\), \(q_i=\max_Tx_i>0\), and \(q_*=\max_iq_i\).
The positivity follows from the included predecessors of the full corner.
For real weights \(w_i\ge1\) and allowance \(Q\ge\max_Tw\cdot x\), write
\[
D_Q=3mQ-4w\cdot s,\qquad
G=q_*\left(3m-4\sum_i\frac{s_i}{q_i}\right).
\]
G2's endpoint-upgrade identity and the generic
[two-step construction](short-corner-local-certificates.md#1-the-two-step-construction)
already prove \(D_Q\ge U_2(T)\).

If \(C=3m-4\sum_i s_i/q_i\ge0\), assign mass \(4s_i/q_i\) to
the included axis point \(q_i e_i\), and the remaining mass \(C\)
to any longest-axis endpoint \(q_*e_j\). These masses are nonnegative
and total \(3m\). Their weighted point sum is
\[
4s+Cq_*e_j,
\]
so their residual from \(4s\) is coordinatewise nonnegative and has sum \(G\).
Every destination has weight at most \(Q\). Consequently
\[
D_Q\ge w_jCq_*\ge G.
\]
If \(C<0\), the line-slack baseline gives \(D_Q\ge0>G\);
there is no nonnegative-mass axis witness in that case.
In either case,
\[
\boxed{D_Q\ge\max\{U_2(T),G(T)\}.}
\]
This is an analytic all-real-weight statement. A finite proof that the
right side is at least \(m\) therefore establishes the B5 target
\(D_0\ge m\), and G1 gives \(W_4\ge A-m+1\ge2\).

The exact axis test uses no rational arithmetic at runtime. With
\(d=q_1q_2q_3>0\),
\[
G\ge m\quad\Longleftrightarrow\quad
q_*\left(3md-4\sum_i s_i\prod_{j\ne i}q_j\right)\ge md.
\]

## 4. B5.4: exhaustive finite profiles

Sort the positive coordinates of \(p\) by a simultaneous permutation of
coordinates and weights. The canonical corners are
\[
\begin{split}
&(1,1,3),(1,2,2),(1,1,4),(1,2,3),(2,2,2),\\
&(1,1,5),(1,2,4),(1,3,3),(2,2,3).
\end{split}
\]
There is no ordering requirement on the weights: the conclusion of Section 3
is symmetric and quantifies over every real \(w_i\ge1\).

A plane profile is \(f=(f_0,\ldots,f_6)\) with
\[
0\le f_x\le7-x,\qquad f_0\ge f_1\ge\cdots\ge f_6,
\]
encoding \(\{(x,y):0\le y<f_x\}\).
Let \(\ell(f)\) count the positive columns. Its mixed corners are exactly
\((x,f_x)\) at the strict drops \(1\le x<\ell(f)\).
For the \(ij\)-plane retain profiles with
\[
f_{p_i}\ge p_j+1,\qquad
\#\{x:1\le x<\ell(f),\ f_x<f_{x-1}\}\le P-2.
\]
The required entry includes the projection of \(p-e_k\).

For \(xy,xz,yz\) profiles \(f,g,h\), impose
\[
\ell(f)=\ell(g),\quad f_0=\ell(h),\quad g_0=h_0,
\]
and reconstruct
\[
T=\{(x,y,z):y<f_x,\ z<g_x,\ z<h_y,\ (x,y,z)\not\ge p\}.
\]
All coordinates are in \(\{0,\ldots,6\}\).
Retain exactly triples for which every reconstructed point has degree at
most six, \(|T|\ge30\), and the three surface bounds of Section 2 hold.
No other filter is selected.

### Coverage and uniqueness

The reconstruction has exactly the three input plane sections: matching
axes ensure that the other pair tests include every point in each
specified plane, and the positive \(p\)-orthant does not meet that plane.
The required entries and monotonicity include every \(p-e_i\); hence
\(p\) is a minimal exclusion. An excluded point violating a pair test
cannot be a full-support minimal exclusion. Every other excluded point
dominates \(p\). Thus \(p\) is its sole full-support corner.

Conversely, take any genuine B5 ideal after orienting \(p\).
Its sections are the displayed profiles by the degree bound and Section 1.
They have matching axes. If reconstruction added a point outside the
ideal, that point would dominate a minimal exclusion other than \(p\).
Such an exclusion lies in a plane, contradicting the corresponding pair
test. Therefore reconstruction recovers the genuine ideal exactly.
Sections 1--2 prove that it survives every selected filter.
Each oriented ideal determines one ordered profile triple.

Enumeration can recursively choose bounded nonincreasing entries.
A different exhaustive representation chooses seven distinct integers
\(13\ge t_0>\cdots>t_6\ge0\), and sets
\[
f_i=t_i-6+i.
\]
This is a bijection with nonincreasing seven-row profiles in a \(7\times7\)
box: conversely \(t_i=f_i+6-i\) are strictly descending and in the stated
range. Applying \(f_i\le7-i\) imposes the degree-six planar cap.
Empty profiles cannot satisfy the required entry.
Shared-axis indexing removes only incompatible triples.
All generation is finite, with at most \(1430^3\) triples per corner.

### The finite obligation

> **B5-FV.** For every reconstructed ideal in the family above,
> \[
> \boxed{\max\{U_2(T),G(T)\}\ge |T|.}
> \]

Exact checking can use the scalar local gain and the denominator-cleared
axis inequality of Section 3. That section proves soundness for all real
weights and allowances; the coverage theorem transfers B5-FV to every
genuine B5 ideal. This is a specification, not yet an established finite lemma.

Since \(T\subseteq\Delta_6\), \(m\le84\), \(s_i\le504\), and \(1\le q_i\le6\).
All local values, axis numerators and rational-margin cross products fit
below \(2^{30}\) in absolute value. Counts over the crude nine-corner
generation bound fit below \(2^{35}\). Require signed value types with at
least 63 value bits and unsigned counters with at least 64 bits.
Only diagnostic checksums may use defined unsigned modular overflow.
No floating-point arithmetic or negative-infinity sentinel is needed.
