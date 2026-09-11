# Fresh analytic audit: continuous transfer and the high-height reduction

11 September 2026.

**Outcome.** I found no incorrect inequality direction, missing phase,
support-creation problem, or endpoint gap in the analytic chain below.
This is a fresh derivation, rather than an adoption of earlier audit
conclusions. The continuous bound is conditional on the precisely stated
finite premise in Section 1. This audit does not by itself verify the
structural theorem or the finite dynamic programs supplying that premise,
nor does it establish the full four-generator theorem alone.

The checked source documents are `round7/uniform_gap_theorem.md` and
`round7/geometric_residual.md`. I also checked the clipping inequalities
against `round7/geometric_residual/certify_residual_parallel.py`.

## 1. The exact finite dependency

For each integer \(R\in\{18,19,20,21\}\), the dependency is:

> Every finite lower ideal \(E\subset\mathbb N^3\), including those
> missing coordinate unit vectors, with \(|x|_1\le R\) for every
> \(x\in E\), and at most one full-support minimal excluded point,
> satisfies
> \[
> 3R|E|-4\sum_{x\in E}|x|_1\ge4|E|.
> \tag{F}
> \]

The maximum degree need not equal \(R\). The empty set satisfies (F)
with both sides zero. Restricting (F) to sets containing coordinate units,
or to sets whose maximum degree equals \(R\), would be insufficient for
the translation argument. The existing finite theorem states the needed
broader scope. Its proof depends on the separately audited geometric
representation and exhaustive recurrence; those are not assumed merely
because a saved computation says PASS.

## 2. Transfer to continuous lower sets

Let \(K\subset\mathbb R_{\ge0}^3\) have positive volume, be contained in
the simplex \(|x|_1\le1\), and have complement a finite union of upper
orthants, with at most one full-support minimal generating vertex.
Boundary conventions have no effect on the integral. Put \(h=1/21\).

For \(r\in[0,h)^3\), define
\[
E_r=\{y\in\mathbb N^3:r+hy\in K\},\qquad
R_r=\left\lfloor\frac{1-|r|_1}{h}\right\rfloor,
\quad \epsilon_r=1-|r|_1-hR_r.
\]
The set \(E_r\) is a finite lower ideal, its points have degree at most
\(R_r\), and \(R_r\in\{18,19,20,21\}\). The value 21 occurs only
at \(r=0\); retaining it is harmless.

If an excluded orthant has vertex \(g\), its preimage has vertex
\[
g'_i=\max\left(0,\left\lceil\frac{g_i-r_i}{h}\right\rceil\right).
\]
A coordinate with \(g_i=0\) still has \(g'_i=0\). Therefore taking
preimages cannot convert a vertex supported on at most two coordinates
into a full-support vertex. Deleting redundant generators cannot create
new vertices: the minimal generators are a subset of the generating list.
Consequently \(E_r\) has at most one full-support minimal excluded point.
This conclusion also covers empty sections.

For each section, direct expansion, followed by (F), gives
\[
\begin{aligned}
\sum_{y\in E_r}(3-4|r+hy|_1)
 &=h\left(3R_r|E_r|-4\sum_{y\in E_r}|y|_1\right)
   +(3\epsilon_r-|r|_1)|E_r|\\
 &\ge (4h-|r|_1)|E_r|.
\end{aligned}
\]
Each map \(r\mapsto r+hy\) has Jacobian one. Integrating over \(r\)
thus partitions integration over \(K\), with no additional \(h^3\)
factor. For a uniformly distributed \(X\) on \(K\), this proves
\[
3-4\mathbb E|X|_1\ge4h-\sum_i\mathbb E(X_i\bmod h).
\tag{1}
\]

To bound a remainder average, fix the other two coordinates. The fiber
in coordinate \(i\) is an interval \([0,L]\). If \(L=qh+t\),
\(0\le t<h\), then
\[
\int_0^L(x\bmod h)\,dx
 =\frac{qh^2+t^2}{2}\le\frac{hL}{2}.
\]
Fubini gives \(\mathbb E(X_i\bmod h)\le h/2\). Inserting this in
(1) yields the claimed conditional continuous theorem
\[
\boxed{3-4\mathbb E|X|_1\ge\frac5{42}.}
\tag{2}
\]

## 3. Exact discrete slack identities

Let \(T\subset\mathbb N^3\) be a finite lower ideal containing the
coordinate units. Let \(u_i>0\) satisfy
\(\max_{x\in T}u\cdot x=1\). Write
\[
m=|T|,\quad
\mu_i=\frac1m\sum_{x\in T}u_ix_i,\quad
\kappa=3-4\sum_i\mu_i,\quad
v=\min_i u_i,\quad s=\sum_i u_i.
\]
The unit condition implies \(u_i\le1\).

For \(x\in T\), let \(\tau_j(x)\) be the largest coordinate \(j\)
on the coordinate-\(j\) fiber through \(x\), and set
\[
\delta_j(x)=1-u_j\tau_j(x)-\sum_{i\ne j}u_ix_i\ge0.
\]
Every such fiber consists of the consecutive levels
\(0,\ldots,\tau_j\). The average coordinate on it is \(\tau_j/2\).
Averaging with fiber-length weights therefore gives
\[
\bar\delta_j=1-\sum_i\mu_i-\mu_j
             =\frac{1+\kappa}{4}-\mu_j,
\qquad \sum_j\bar\delta_j=\kappa\ge0.
\tag{3}
\]
This proves the nonnegativity used later; no unproved Wilf inequality is
being inserted at this point.

## 4. A fully expanded phase argument

Choose \(k\) with \(u_k=v\), and fix \(j\ne k\). On a
coordinate-\(k\) fiber with levels \(t=0,\ldots,L-1\), there is a
constant \(A\) such that
\[
\delta_j(t)\equiv A-tv\pmod {u_j}.
\]
The top coordinate in direction \(j\) may change arbitrarily with
\(t\); it contributes an integer multiple of \(u_j\), which is why
this congruence still holds. For \(0\le r\le v\), nonnegativity gives
\[
[A-tv+r]_{u_j}=[\delta_j(t)+r]_{u_j}\le\delta_j(t)+r.
\tag{4}
\]
The intervals \([A-tv,A-tv+v]\), for all these \(t\), concatenate
into one interval of length \(h_0=Lv\), with only endpoint overlaps.

For a sawtooth of period \(u>0\), an interval of length
\(h_0=qu+r_0\), \(0\le r_0<u\), has integral at least
\[
\frac{qu^2+r_0^2}{2}
\ge\frac{h_0^2}{2(q+1)}
\ge\frac{u h_0^2}{2(h_0+u)}.
\tag{5}
\]
The first lower bound follows by taking \(q\) complete periods and
using that the smallest integral over an arc of length \(r_0\) is
\(r_0^2/2\). The second inequality is Cauchy--Schwarz applied to
\(q\) copies of \(u\) and one copy of \(r_0\). The third uses
\(q+1\le(h_0+u)/u\). This remains valid when \(q=0\) or \(r_0=0\).

The normalized height bound gives \((L-1)v\le1\), hence
\(h_0\le1+v\). Comparing (4), integrated and summed, with (5) for
\(u=u_j\), and dividing by \(Lv\), gives
\[
\operatorname{mean}_{\text{fiber}}\delta_j
\ge\frac{u_jvL}{2(1+v+u_j)}-\frac v2.
\]
If fibers are weighted by their cardinalities, then
\(v\mathbb E L=2\mu_k+v\). Thus
\[
2\bar\delta_j(1+v+u_j)
\ge2u_j\mu_k-v(1+v).
\tag{6}
\]

For clarity, here is the complete algebra from these two inequalities
to the summed phase estimate. Write the other two weights as \(w\le U\).
Then \(s=v+w+U\), \(w\le1\), and \(U\le s-2v\). Summing (6) and
bounding its left side above by
\(2(1+v+U)(\kappa-\bar\delta_k)\) gives
\[
\frac{(s-v)(1+\kappa)}{2}
\le2(1+v+U)\kappa
  +2(w-1-v)\bar\delta_k+2v(1+v).
\]
The middle term is nonpositive. Dropping it enlarges the right side.
Using \(U\le s-2v\), multiplying by two, and collecting terms proves
\[
\boxed{s(1-3\kappa)
\le4\kappa+5v-3\kappa v+4v^2.}
\tag{7}
\]
In particular, the fact that the coefficient is nonpositive, and the
direction of the bound on the left side before rearrangement, have both
been checked explicitly.

## 5. Thickening and normalization

Take the disjoint, up to boundaries, boxes
\[
\prod_i[u_ix_i,u_i(x_i+1)),\qquad x\in T,
\]
and scale their union by \(1/(1+s)\). The resulting continuous lower
set \(K\) lies in the unit simplex. All boxes have equal volume, so
\[
\mathbb E_K|X|_1=\frac{\sum_i\mu_i+s/2}{1+s},
\qquad
\boxed{\kappa_c(K)=\frac{\kappa+s}{1+s}.}
\tag{8}
\]
The complement vertices are exactly the scaled vertices of the discrete
excluded monomial ideal. Positive diagonal scaling changes no supports.
Therefore an ideal with at most one full-support minimal excluded point
has a thickening in the scope of (2).

## 6. Compactness of every possible high-height failure

Normalize the original weights to \(a=(1,b,c)\), with
\(1\le b\le c\), and put
\[
H=\max_{x\in T}a\cdot x,\quad
D=3mH-4\sum_{x\in T}a\cdot x,\quad S=1+b+c.
\]
Then \(u=a/H\), \(v=1/H\), \(s=S/H\), and \(\kappa=D/(mH)\).
Suppose \(H\ge7\) and \(m-D>29/10\). Equation (3) implies
\(0\le\kappa<v<1/3\). By (7),
\[
s\le\frac{4\kappa+5v-3\kappa v+4v^2}{1-3\kappa}
 <\frac{9v+v^2}{1-3v}.
\]
The derivative of the displayed rational function of \(\kappa\)
has positive numerator \(4+12v+12v^2\). The strict inequality follows
from \(\kappa<v\). Multiplying by \(H\) gives
\[
\boxed{S<9+\frac{28}{H-3}.}
\tag{9}
\]

Equations (2) and (8) give \(5H\le42D/m+37S\). Since the proposed
failure has \(D/m<1\),
\[
\boxed{5H<42+37S.}
\tag{10}
\]
Combining (9) and (10), and multiplying by the positive \(H-3\), yields
\[
5H^2-390H+89<0.
\tag{11}
\]
At \(H=78\), the polynomial equals 89; its derivative is positive
throughout \([78,\infty)\). Consequently
\[
\boxed{7\le H<78.}
\]
The units give \(c\le H\). Hence the initial closed real box used by
the interval certificate contains every potential high-height failure.
The closed endpoint \(H=78\) is merely an over-enclosure of an impossible
endpoint. No residue-labeling or multiplicity bound is used in this
geometric compactness argument.

## 7. Clipping inequalities and outward rounding

For a closed box with \(H\ge H_0>3\), (9) gives
\(S<9+28/(H_0-3)\). Replacing that upper bound by its ceiling on the
\(1/q\) grid only enlarges the possible set. Call the rounded bound
\(S_*\). Ordering gives \(1+2b\le S\), hence
\(b<(S_*-1)/2\). Also \(c<S_*-1-b_0\). These are exactly the two
weight upper bounds in the producer, with outward ceilings. Finally,
\(S\le\min(S_*,1+b_1+c_1)\), and (10) gives the height upper bound
\((42+37S_{\mathrm{upper}})/5\), again rounded upward.

Ordering propagation only replaces a lower bound by another necessary
lower bound or an upper bound by another necessary upper bound. Every
individual clipping step therefore preserves every genuine failure.
Iterating twenty times and then stopping is safe even if a fixed point has
not been reached; stopping can retain extra points, but cannot erase a
possible failure. The initial domain has \(H_0\ge7\), so the denominator
\(H_0-3\) cannot vanish or reverse sign.

This verifies the analytic justification of the clipping code. It does
not replace verification that the final tree covers the root or that each
dynamic-program bound is valid; those are separate certificate obligations.

## 8. Fresh exact checks and limitations

Run

```sh
python3 round8/check_phase_exact.py
```

This standalone standard-library program imports no prior proof verifier.
It independently enumerates all 980 lower ideals in a \(3\times3\times3\)
cube using plane partitions. For each of the 930 ideals containing the
coordinate units, it checks all 64 positive integer weight triples in
\(\{1,2,3,4\}^3\), using exact `Fraction` arithmetic.

The completed run checked:

| Check | Number |
|---|---:|
| Weighted lower ideals | 59,520 |
| Individual phase inequalities (6), including tied minima | 167,400 |
| Summed phase inequalities (7) | 59,520 |
| Thickening identities (8) | 59,520 |
| Exact sawtooth interval lower bounds | 16,121 |
| Exact remainder-fiber bounds | 343 |

It also verifies the slack gap \(90/31-29/10=1/310\), the cutoff
polynomial at 78, \(\binom{80}{3}=82,160\), and the rational algebra
used in the height conversion. All checks passed; the actual result is
`round8/check_phase_exact.json`.

These bounded checks are sanity checks for the independently written
analytic proof. They are not used to extrapolate to all ideals and are
not described as a fresh replay of the finite strip or the final interval
certificate. The remaining dependency for the uniform gap is (F), with
exactly the scope in Section 1.
