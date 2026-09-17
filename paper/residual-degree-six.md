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
