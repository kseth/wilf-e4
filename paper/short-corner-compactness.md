# Short-corner planar bounds and high-height compactness

## Status and purpose

This note completes roadmap task B4.2. Two elementary planar partitions and
the [G4 phase cutoff](phase-and-thickening.md#5-downstream-forms-and-endpoint-audit)
show that every possible failure of the high-height short-corner target lies
in the closed real parameter domain

\[
\mathcal K_{36}=
\{(b,c,H):1\le b\le c\le H,\ 6\le H\le36\}.
\tag{1}
\]

The actual failure bound is strict: \(H<36\). This improves the simpler
\(H<42\) reduction underlying the historical interval certificate.
That certificate's larger closed domain still contains (1); no certificate
needs to be altered to use this analytic improvement.

This note proves only the reduction and analytic acceptance rules, not that
the target holds throughout (1). No interval-tree coverage, dynamic-program
bound, residue filter, or historical success count is certified here.

## 1. The compactness theorem

Let \(T\subseteq\mathbb N^3\) be a finite lower ideal whose sole full-support
minimal exclusion is a coordinate permutation of \((2,1,1)\). For positive
weights \(a=(a_1,a_2,a_3)\), put

\[
A=\min_i a_i,\qquad w=\frac aA,\qquad
m=|T|,\qquad s=\sum_{x\in T}x,
\]
\[
H=\max_{x\in T}w\mathbin\cdot x,\qquad
B=w_1+w_2+w_3,\qquad D_0=3mH-4w\mathbin\cdot s.
\tag{2}
\]

Thus \(\min_i w_i=1\). Minimality of the corner and lower closure imply
\(0,e_1,e_2,e_3\in T\), so \(w_i\le H\). The
[B4.1 split](short-corner-height-split.md) identifies \(H\ge6\) as the
high-height side and places every \(m\ge49\) there.

### Theorem 1.1 (B4.2)

If \(H\ge6\) and \(D_0<m-1\), then

\[
B<9+\frac{28}{H-3},\qquad
5H^2-180H+47<0,\qquad H<36.
\tag{3}
\]

After sorting the weights into \((1,b,c)\), the parameters lie in (1), with
the corner in one of the three positions

\[
(2,1,1),\qquad(1,2,1),\qquad(1,1,2).
\tag{4}
\]

The proof does not require residue labels or \(m\ge30\). In fact it uses
only the exclusion of the short-corner orthant and inclusion of the
coordinate units, not uniqueness of the full-support exclusion.

## 2. The planar mean inequality

### Lemma 2.1

Let \(F\subseteq\mathbb N^2\) be a nonempty finite lower ideal, with positive
linear weight \(q(x,y)=rx+ty\). If \(n=|F|\) and \(Q=\max_Fq\), then

\[
3\sum_{z\in F}q(z)\le2nQ.
\tag{5}
\]

#### Proof

Let \(s_F=\sum_{z\in F}z\). In the horizontal line family, the sum of line
length times line top is \((2(s_F)_1,(s_F)_2)\): the variable coordinate
has twice its line sum, and the other coordinate is constant. In the
vertical family the corresponding vector is
\(((s_F)_1,2(s_F)_2)\). Together they give \(3s_F\).
Each family partitions \(F\), so their total line length is \(2n\).
Every top has weight at most \(Q\); taking weighted sums proves (5). ∎

This is the dimension-two line-sum form of the standard weighted downset
inequality; its dimension-three bookkeeping is proved in
[G2](coordinate-lines.md). The upstream weighted inequality is attributed
in the [foundations](foundations.md#4-the-moment-identity-and-baseline-f2).

Embed \(F\) in a coordinate plane. A translate \(u+F\subseteq T\) then has
offset \(h=w\cdot u\). Since \(\max_Fw\cdot z\le H-h\), its mean weight
satisfies

\[
\operatorname{mean}_{u+F}(w\cdot x)
\le h+\frac23(H-h)=\frac{2H+h}{3}.
\tag{6}
\]

Empty pieces are omitted, and a one-point piece is covered by (5).

## 3. Two planar partitions

Orient the corner as \((2,1,1)\), write coordinates as \((x,y,z)\), and
write the normalized weights as

\[
w=(\lambda,\mu,\nu),\qquad B=\lambda+\mu+\nu,\qquad
\min(\lambda,\mu,\nu)=1.
\tag{7}
\]

This orientation does not require \(\lambda=1\).

### First partition

The following four pieces are disjoint and cover \(T\):

| Piece condition within \(T\) | Translation \(u\) | Free coordinates after translation | Offset \(w\cdot u\) |
|---|---|---|---|
| \(y=0\) | \((0,0,0)\) | \(x,z\) | \(0\) |
| \(y\ge1,\ z=0\) | \((0,1,0)\) | \(x,y\) | \(\mu\) |
| \(x=0,\ y,z\ge1\) | \((0,1,1)\) | \(y,z\) | \(\mu+\nu\) |
| \(x=1,\ y,z\ge1\) | \((1,1,1)\) | \(y,z\) | \(B\) |

Coverage follows because \(x\ge2,\ y,z\ge1\) would dominate the excluded
corner. In every row, subtracting the translation leaves a planar lower
ideal: decreasing a free coordinate preserves both membership in \(T\) and
the row condition.

The largest offset is \(B\), so (6) immediately gives the simple bound

\[
\frac{w\cdot s}{m}\le\frac{2H+B}{3},
\qquad
\boxed{\frac{D_0}{m}\ge\frac{H-4B}{3}.}
\tag{8}
\]

For a refinement, let the four sizes be \(n_1,\ldots,n_4\). Lower closure
maps the fourth piece injectively into the third by changing \(x=1\) to
\(x=0\); hence \(n_4\le n_3\) and \(n_4/m\le1/2\). The size-weighted
average offset satisfies

\[
\begin{aligned}
\bar h
&=\frac{\mu(n_2+n_3+n_4)+\nu(n_3+n_4)+\lambda n_4}{m}\\
&\le\mu+\nu+\frac{\lambda}{2}
=B-\frac{\lambda}{2}=:L_1.
\end{aligned}
\tag{9}
\]

### Second partition

Exchange \(y,z\), if necessary, so that \(\mu\le\nu\); the corner is
unchanged. Another disjoint cover is:

| Piece condition within \(T\) | Translation \(u\) | Free coordinates after translation | Offset \(w\cdot u\) |
|---|---|---|---|
| \(x=0\) | \((0,0,0)\) | \(y,z\) | \(0\) |
| \(x=1\) | \((1,0,0)\) | \(y,z\) | \(\lambda\) |
| \(x\ge2,\ y=0\) | \((2,0,0)\) | \(x,z\) | \(2\lambda\) |
| \(x\ge2,\ y\ge1,\ z=0\) | \((2,1,0)\) | \(x,y\) | \(2\lambda+\mu\) |

The same lower-closure and forbidden-orthant arguments apply. Its average
offset is at most

\[
L_2=2\lambda+\min(\mu,\nu).
\tag{10}
\]

Applying (6) to both partitions proves

\[
\frac{w\cdot s}{m}\le\frac{2H+L}{3},
\qquad
\frac{D_0}{m}\ge\frac{H-4L}{3},
\qquad L=\min(L_1,L_2).
\tag{11}
\]

### A uniform refinement

Normalization implies either \(\lambda=1\) or \(\min(\mu,\nu)=1\).

If \(\lambda=1\), then
\(L\le B-1/2\) and \(L\le(B+3)/2\). Taking three fifths of the first
bound and two fifths of the second gives

\[
L\le\frac45B+\frac3{10}.
\]

If \(\min(\mu,\nu)=1\), then
\(L\le B-\lambda/2\) and \(L\le2\lambda+1\). Taking four fifths of the
first and one fifth of the second gives
\(L\le4B/5+1/5\). Thus in every orientation,

\[
\boxed{L\le\frac45B+\frac3{10},\qquad
\frac{D_0}{m}\ge\frac H3-\frac{16B}{15}-\frac25.}
\tag{12}
\]

## 4. Proof of the compactness theorem

Assume \(H\ge6\) and \(D_0<m-1\). In particular \(D_0/m<1\).
The G4 line-slack identity gives \(D_0\ge0\). With

\[
v=\frac1H,\qquad \sigma=\frac BH,\qquad
\kappa=\frac{D_0}{mH},
\]

we have \(0\le\kappa<v\le1/6\). The G4 summed phase inequality is

\[
\sigma(1-3\kappa)
\le4\kappa+5v-3\kappa v+4v^2.
\tag{13}
\]

Division by \(1-3\kappa>0\) is legitimate. For fixed \(v\), the derivative
of the resulting right side has numerator \(4+12v+12v^2>0\), so substituting
the strict bound \(\kappa<v\) yields

\[
B<\frac{9H+1}{H-3}=9+\frac{28}{H-3}.
\tag{14}
\]

On the other hand, (12) and \(D_0/m<1\) imply

\[
H<\frac{21}{5}+\frac{16}{5}B
<33+\frac{448}{5(H-3)}.
\tag{15}
\]

Multiplying by the positive number \(5(H-3)\) gives

\[
5H^2-180H+47<0.
\tag{16}
\]

This polynomial equals \(47\) at \(H=36\), and is strictly increasing for
\(H\ge36\). Therefore (16) forces \(H<36\).

Sorting the weights into \((1,b,c)\) preserves the weighted ideal and
deficit under the same coordinate permutation. Since \(e_i\in T\), their
weights give \(1\le b\le c\le H\). The doubled coordinate of the corner
must still be allowed in all three positions in (4). This proves Theorem
1.1 and the closed envelope (1). ∎

For comparison, using only (8) gives \(H<3+4B\). Together with (14) this
implies

\[
H^2-42H+5<0,\qquad H<42.
\tag{17}
\]

Thus the simpler historical \(42\)-box also follows from proved analytic
estimates, without needing the refinement.

## 5. Acceptance rules, closed domains, and scope

Both the simple and refined planar bounds are weak inequalities. Consequently

\[
H\ge3+4B\ \Longrightarrow\ D_0\ge m,
\]
\[
5H\ge21+16B\ \Longrightarrow\ D_0\ge m.
\tag{18}
\]

Equality in either condition is sufficient; it must not be discarded.
The same bounds and acceptance rules hold with a height allowance
\(Q\ge\max_Tw\cdot x\), using \(3mQ-4w\cdot s\) as the deficit:
only an upper bound on every piece's weight was used in Section 3.
The phase cutoff, by contrast, was applied with the attained maximum \(H\).

For a whole parameter box with \(H\ge H_0,\ b\le b_1,\ c\le c_1\), the
orientation-independent sufficient rules are therefore

\[
H_0\ge3+4(1+b_1+c_1)
\quad\text{or}\quad
5H_0\ge21+16(1+b_1+c_1).
\tag{19}
\]

These analytic rules do not require any discretization of the real weights.
They say nothing about boxes that fail both tests.

There is a useful additional weight bound on possible failures. Since
\(H\ge6\), (14) gives \(B<55/3\). For sorted weights,

\[
b\le\frac{B-1}{2}<\frac{26}{3}<9,\qquad
c\le B-2<\frac{49}{3}<17.
\tag{20}
\]

Hence a smaller closed rectangular envelope is
\([1,9]\times[1,17]\times[6,36]\), intersected with \(b\le c\le H\).
The height-dependent phase bound (14) and polynomial bound (16) may also be
relaxed to weak inequalities for safe closed-domain clipping. None of these
optional restrictions requires changing an existing certificate.

For the retained historical alternative, its ordered domain
\(6\le H\le42,\ 1\le b\le c\le H\) contains (1). Its extra boundary and
parameter points only enlarge the proposed finite obligation. The endpoint
\(H=6\) remains included, while \(H=36\) is harmlessly included in the new
closed envelope despite the strict failure cutoff.

B4.3 and B4.4 still owe the low-height profile/filter and centroid-dual
arguments. D4 must decide whether either B4 certificate family is necessary,
and R4a must audit and replay any retained high-height certificate. No B4
weighted theorem is declared complete by this note.

## 6. Provenance and attribution boundary

The simple partition and \(42\)-box are in the historical
[short-corner weighted theorem](../artifacts/wilf_four_generators_review_package_2026-09-11/round5/one_corner_extension/short_corner_weighted_theorem.md).
The paired-offset refinement, second partition, and \(36\)-bound are in the
earlier [short-corner compactness note](../artifacts/wilf_four_generators_review_package_2026-09-11/round5/interior_arithmetic/short_corner_weighted_compactness.md).
This reconstruction adopts that stronger analytic reduction while preserving
compatibility with the later, deliberately larger certificate domain.

The planar baseline is inherited weighted downset machinery, proved here in
its needed two-dimensional form. G4 supplies the already reconstructed phase
estimate. No continuous one-corner gap, arithmetic plane-corner theorem,
L-shape construction change, or computational assertion is imported. Branch
novelty and final upstream attribution remain subject to L3.

On 2026-09-16, bounded exact-rational diagnostics passed for 621 planar
weight/profile combinations and 9,150 short-corner weight/parameter
combinations, checking the partitions, translated lower closure, mean
bounds, phase inequality, and height-allowance rules. Another 145 rational
height samples checked the elimination identities in (16)--(17).
These are consistency diagnostics, not proof dependencies or certificate
replays; the arguments above cover arbitrary real positive weights.
