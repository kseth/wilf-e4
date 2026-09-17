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
