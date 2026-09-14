# No-corner continuous bound and compactness reduction

## Status and purpose

This note completes task B2.1. It proves the continuous no-corner moment
inequality needed after rectangular thickening, the degree-four cardinality
bound \(29\), and the reduction of every possible failure in B2 to the closed
parameter region

\[
1\le b\le c\le H,\qquad 5\le H\le24.
\tag{1}
\]

All assertions in this note are analytic. The polynomial factorizations in
the continuous argument are explicit identities, not computer-assisted
lemmas. The interval certificate on (1) is the separate task B2.2.

The proof uses two earlier interfaces. The G5 decomposition supplies a
central box and at most three nested rectangular horns. The G4 thickening
identity and phase inequality then transfer the continuous estimate back to
the discrete ideal and bound its normalized height.

## 1. The compactness theorem

Let \(T\subseteq\mathbb N^3\) be a finite lower ideal containing
\(e_1,e_2,e_3\), and suppose that \(T\) has no full-support minimal excluded
point. For positive weights \(w=(w_1,w_2,w_3)\), put

\[
m=|T|,\qquad
\alpha=\min_i w_i,\qquad
M=\max_{x\in T}w\mathbin\cdot x,
\]

\[
D=3mM-4w\mathbin\cdot\sum_{x\in T}x.
\tag{2}
\]

### Theorem 1.1 (B2.1)

Assume \(m\ge30\). After scaling by \(\alpha\) and permuting the coordinates,
write the weights as \((1,b,c)\), with \(1\le b\le c\), and write

\[
H=\max_{x\in T}(x_1+bx_2+cx_3).
\tag{3}
\]

If \(D<\alpha(m-1)\), then

\[
1\le b\le c\le H,
\qquad
5\le H<12+\sqrt{137}<24.
\tag{4}
\]

Consequently every possible failure of the B2 weighted inequality occurs in
the closed region (1). The strict upper endpoint in (4) is deliberately
enlarged to the closed endpoint \(H=24\) for the later certificate.

The continuous inequality needed in the proof is reconstructed next.

## 2. Box-horn sets and their moment functional

Boundary faces never affect the integrals below. A *box-horn set of height
one* is the disjoint union, up to null sets, of a central box

\[
C=[0,a]\times[0,b]\times[0,c],
\qquad a,b,c\ge0,\qquad a+b+c\le1,
\tag{5}
\]

and at most three outward horns. The horn beyond the \(a\)-face has the form

\[
\{(t,y,z):a<t<1,\ 0<y<f(t),\ 0<z<g(t)\},
\tag{6}
\]

where \(f,g\) are nonnegative, nonincreasing finite step functions satisfying

\[
f(t)\le b,\qquad g(t)\le c,
\qquad t+f(t)+g(t)\le1.
\tag{7}
\]

The other two horns are defined by coordinate permutation. Empty horns and
zero-width sections are allowed.

For a measurable \(E\subseteq\mathbb R_{\ge0}^3\), define

\[
\mathcal J(E)=\int_E\bigl(3(x_1+x_2+x_3)-2\bigr)\,dx.
\tag{8}
\]

Thus \(\mathcal J(E)\le0\) is equivalent to

\[
\frac1{\operatorname{vol}E}
\int_E(x_1+x_2+x_3)\,dx\le\frac23
\tag{9}
\]

when \(E\) has positive volume. The central box contributes

\[
\mathcal J(C)
=abc\left(\frac32(a+b+c)-2\right).
\tag{10}
\]

The contribution of the horn (6) is

\[
\mathcal J_a(f,g)
=\int_a^1 f(t)g(t)
 \left(3t+\frac32(f(t)+g(t))-2\right)dt.
\tag{11}
\]

We next obtain a sharp enough common envelope for (11), then show that the
three envelopes are absorbed by the negative contribution (10).

## 3. The boundary-tail potential

It is convenient to give the formulas at an arbitrary height allowance
\(L>0\). For \(0\le x\le y\), define

\[
\begin{aligned}
P_L(x,y)={}&\frac{Lx^3}{6}-\frac{x^4}{4}
 +\frac{Lxy^2}{2}-\frac{3x^2y^2}{4}-\frac{xy^3}{2},\\
g(q,z)={}&\frac{q^2z^2}{8}+\frac{q^3z}{24}+\frac{q^4}{192},\\
Q_L(x,y)={}&P_L(x,y)
 +g\bigl((y+2x-L)_+,y-x\bigr).
\end{aligned}
\tag{12}
\]

Extend \(Q_L\) symmetrically in \(x,y\).

### Lemma 3.1 (boundary-tail optimum)

Suppose a horn is already on the height boundary: in reverse time
\(r=L-t\), its transverse sides are nondecreasing functions with sum \(r\),
ending at caps \(x\le y\). Its contribution is at most \(Q_L(x,y)\).

#### Proof

By scaling, take \(L=1\). At each \(r\), sort the two sides and write their
difference as \(d(r)\ge0\). Sorting preserves the sum, product, caps, and
monotonicity. The boundary contribution becomes

\[
\int_0^{x+y}\frac{(2-3r)(r^2-d(r)^2)}8\,dr.
\tag{13}
\]

The two sides are nondecreasing precisely when \(d\) is \(1\)-Lipschitz.
The cap conditions give

\[
\max(0,r-2x)\le d(r)\le\min(r,2y-r).
\tag{14}
\]

The coefficient of \(-d^2\) changes sign only at \(r=2/3\). After fixing
\(d(2/3)\), the optimal admissible function is therefore the smallest one
allowed by (14) to the left of \(2/3\), and the largest one allowed to its
right. Writing \(q=(2/3-d(2/3))/2\), the associated transverse sides are

\[
\begin{cases}
(r/2,r/2),&0\le r\le2q,\\
(q,r-q),&2q\le r\le y+q,\\
(r-y,y),&y+q\le r\le x+y.
\end{cases}
\tag{15}
\]

The same profile follows directly from pointwise product maximization if
\(x+y\le2/3\). When \(x+y\ge2/3\), feasibility gives

\[
\max(0,2/3-y)\le q\le\min(x,1/3).
\]

Let \(I(q;x,y)\) denote the integral in (13) for (15). Direct integration
gives

\[
\frac{\partial I}{\partial q}
=\frac{(y-q)^2(1-y-2q)}2.
\tag{16}
\]

Hence the optimum is attained at

\[
q_*=\min\left(x,\frac{1-y}{2}\right).
\tag{17}
\]

In the second case above, \(y\ge1/3\), so \(q_*\) lies in the displayed
feasible interval. The endpoint \(q=x\) has value \(P_1(x,y)\). If
\(q_*<x\), integration of (16) from \(q_*\) to \(x\) shows that the
improvement is

\[
g(y+2x-1,y-x).
\tag{18}
\]

Equations (12) and (18) prove the claim for \(L=1\); homogeneity gives the
general statement. \(\square\)

## 4. Reducing an arbitrary horn to one slab

For \(a+x+y\le L\), put

\[
F_L(a;x,y)=Q_L(x,y)
 +\frac{3a-L}{2}xy(L-a-x-y),
\tag{19}
\]

and, whenever \(a+B+C\le L\), define

\[
U_L(a;B,C)=
\max_{0\le x\le B,\ 0\le y\le C}F_L(a;x,y).
\tag{20}
\]

The term added to \(Q_L\) is the contribution of a constant initial slab
from \(t=a\) to \(t=L-x-y\).

### Lemma 4.1 (one-slab envelope)

Every finite-step horn based at \(a\), with transverse caps \(B,C\) and
height allowance \(L\), has contribution at most \(U_L(a;B,C)\).

#### Proof

Scale to \(L=1\), and sort the two transverse coordinates so \(B\le C\).
First fix the finite list of nested rectangle states and vary only the
outward endpoints of their slabs. The objective is a separable convex
quadratic in those endpoints: the quadratic coefficient at an endpoint is
\(3(A_i-A_{i+1})/2\ge0\), where \(A_i\) is the area of the \(i\)-th rectangle
and \(A_{n+1}=0\). A maximum on the endpoint polytope is attained at a
vertex. A block of equal endpoints at such a vertex either begins at \(a\)
or meets one of its height bounds. Removing zero-length slabs leaves every
surviving slab tight at its right endpoint.

Reverse time by \(r=1-t\), and write

\[
A(r)=1-\frac32r.
\]

If a tight slab starts at reverse time \(r\), ends with rectangle \((x,y)\),
and \(x+y=s\le r\), its exact contribution is

\[
A(r)(r-s)xy.
\tag{21}
\]

For transitions wholly inside \(r\le2/3\), any monotone boundary
interpolation has area at least that of the smaller endpoint rectangle, while
\(A(r)\ge0\). Filling those transitions therefore weakly increases the
objective. Lemma 3.1 then bounds the filled tail.

It remains to control the earlier transitions, where \(A(r)\le0\). If none
of the states reaches reverse time at most \(2/3\), all terms in (21) are
nonpositive and the empty horn dominates. Otherwise let \((u,v)\), \(u\le v\),
be the first tight state with \(u+v\le2/3\). At every earlier state of sum
\(s\), nestedness and the cap conditions allow its product to be replaced by
the smaller product at

\[
x_*(s)=\max(u,s-C),\qquad
y_*(s)=\min(C,s-u).
\tag{22}
\]

Indeed \(x(s-x)\) is increasing for \(x\le s/2\); the pair in (22) is
nested as \(s\) varies, respects \(B,C\), and ends at \((u,v)\). Since the
coefficient in (21) is nonpositive, this replacement can only increase the
objective. All earlier states now lie on the L-shaped boundary path

\[
(B,C)\longrightarrow(u,C)\longrightarrow(u,u).
\tag{23}
\]

The possibly slack initial position is represented only for bookkeeping by
the virtual state \((x_0,C)\), where \(x_0=1-a-C\ge B\). The first actual
jump covers the virtual excess.

We now compare a jump on (23) with filling the same part of the boundary
path continuously. Along a branch with one fixed side \(c\), a jump of
length \(d\) has gain

\[
G_c(d)=\frac c4d^2(2d+3c-2),
\tag{24}
\]

and two jumps satisfy

\[
G_c(d+e)-G_c(d)-G_c(e)
=\frac{3c}{2}de\left(d+e+c-\frac23\right).
\tag{25}
\]

These follow by integrating \(c(r-c)A(r)\). On the second branch of (23),
the fixed side is \(u\), and every jump has
\(d\le C-u\le1-2u\). Thus \(2d+3u-2\le-u\), so (24) is nonpositive and all
such jumps may be filled.

At most one jump crosses the turn in (23). Suppose it starts at
\((u+p,C)\) and ends at \((u,C-q)\). If its gain over the continuous L-path
is denoted by \(G(p,q;u,C)\), direct integration gives

\[
\frac{\partial G}{\partial q}
=\frac u2(p+q)(3p+3q+3u-2).
\tag{26}
\]

This derivative changes sign at most once, from negative to positive, so the
maximum occurs at \(q=0\) or \(q=C-u\). The continuous baseline from the
jump's start through the remaining tail is independent of \(q\), so the same
endpoint conclusion applies to the whole continuation. The first choice
moves the jump entirely onto the fixed-\(C\) branch.

For the balanced endpoint, a jump from reverse time \(r\) to \((z,z)\),
followed by the balanced tail, has value

\[
E_r(z)=A(r)(r-2z)z^2+\frac23z^3-\frac32z^4,
\]

with

\[
E_r'(z)=-6z\left(z-\frac r2\right)
              \left(z-r+\frac23\right).
\tag{27}
\]

On \(0\le z\le R\le r/2\), the maximum of \(E_r\) is therefore at \(0\) or
\(R\). For a noninitial crossing jump, take \(R\) to be the smaller side of
its genuine starting state; the second endpoint is a fixed-smaller-side jump
and is dominated by filling. For the initial crossing jump, take \(R=B\),
which is valid because \(2B\le B+C\le1-a\). Its second endpoint is the
admissible initial slab ending at \((B,B)\). If the zero endpoint wins, every
earlier term still lies in the nonpositive part, so the empty horn dominates.
Thus the crossing jump either disappears or is replaced by an admissible
one-slab construction.

All remaining jumps lie on the fixed-\(C\) branch. Retain the first jump,
including any mandatory initial slack, and fill every later jump whose gain
in (24) is nonpositive. If a later jump of length \(e\) has positive gain,
then either \(C\ge2/3\), or

\[
e>\frac32\left(\frac23-C\right)>\frac23-C.
\]

Equation (25) shows that merging it into the first jump cannot decrease the
total gain. The individual gains depend only on jump lengths, so the jump and
continuous lengths may be reordered along the same branch before merging.
Their total length, the continuous baseline, nestedness, and the initial cap
constraint are unchanged. Repetition leaves a single initial jump followed
by a boundary profile.

If that jump ends at effective caps \((x,y)\), its contribution together with
the optimal continuation is \(F_1(a;x,y)\). The effective caps lie inside
\((B,C)\), so (20) proves the lemma. \(\square\)

## 5. The joint three-horn inequality

### Lemma 5.1 (joint envelope)

If \(a,b,c\ge0\), \(S=a+b+c\le L\), then

\[
\boxed{
U_L(a;b,c)+U_L(b;a,c)+U_L(c;a,b)
\le abc\left(2L-\frac32S\right).
}
\tag{28}
\]

#### Proof

For \(x\le y\), first omit the boundary-tail gain from (12) and write

\[
H_L(a;x,y)=P_L(x,y)
 +\frac{3a-L}{2}xy(L-a-x-y).
\tag{29}
\]

Let \(r=L-a-x-y\). Direct differentiation gives

\[
(H_L)_y=\frac{xr}{2}\,[3(a+y)-L].
\tag{30}
\]

Where the gain in (12) is active, it is nondecreasing in \(y\). Hence, for
fixed \(x\), \(F_L(a;x,y)\) first decreases and then increases as \(y\) runs
from \(x\) to its allowed cap; its maximum is at the diagonal or at the full
larger cap. If \(a+x\ge L/3\), (30) sends the diagonal endpoint to the full
cap. If \(a+x\le L/3\), the gain vanishes on the diagonal segment and

\[
\frac d{dt}H_L(a;t,t)
=-6t\left(t-\frac{L-a}{2}\right)
       \left(t-\left(\frac L3-a\right)\right)\le0
\tag{31}
\]

for \(0\le t\le x\). That diagonal endpoint is at most zero, which is
attained by the empty horn. Thus, for \(B\ge C\),

\[
U_L(a;B,C)=\max_{0\le x\le C}F_L(a;x,B).
\tag{32}
\]

Relabel the central sides so that \(a\le b\le c\), and first take the
saturated case \(L=S\). The gain in (12) vanishes for the horns based at
\(b\) and \(c\). For the gain-free expression, one also has

\[
2(H_L)_x=(a-x)(x-y)^2
 +r\,[x^2+2ay-yr],
\tag{33}
\]

where \(a\) in this formula denotes the horn's base and \(y\) its full larger
cap. Equation (33) is nonnegative in the two relevant ranges. Consequently
the \(b\)- and \(c\)-horns take their full smaller cap \(a\). Only the horn
based at the smallest side remains to be optimized.

Indeed, for the \(b\)-horn one has \(0\le x\le a\le b\), larger cap \(c\),
and \(r=a-x\); for the \(c\)-horn the larger cap is \(b\) and the same
relations hold. Both terms on the right of (33) are then nonnegative.

For \(0\le x\le b\), set

\[
\Delta=\frac{abcS}{2}-F_S(a;x,c)
       -H_S(b;a,c)-H_S(c;a,b).
\tag{34}
\]

Three nonnegative polynomial identities cover its entire domain. In the
gain-free range \(x\le a\), substitute

\[
x=p,\quad a=p+q,\quad b=p+q+r,\quad c=p+q+r+s.
\]

Then

\[
\begin{aligned}
\Delta={}&\frac34p^2(q+r)^2
 +\frac12p(q+r)^2(s+r+2q)\\
&+q^2\left[\frac{(s+2r)^2}{4}
 +\frac23q(s+2r)+\frac12q^2\right]\ge0.
\end{aligned}
\tag{35}
\]

In the remaining gain-free range \(a\le x\le(a+b)/2\), substitute

\[
a=p,\quad x=p+q,\quad b=p+q+r,\quad c=p+q+r+s.
\]

Then

\[
\begin{aligned}
\Delta={}&\frac34p^2r^2+\frac12pr^2(s+r+2q)
 +\frac12qr^2(s+r)\\
&+q^2\left[\frac{(s+2r)^2}{4}+\frac{r^2}{4}\right]
 +\frac13q^3(s+2r)+\frac16q^4\ge0.
\end{aligned}
\tag{36}
\]

Finally, the gain is active exactly when \(x\ge(a+b)/2\). Substitute

\[
a=p,\quad x=p+2q+r,\quad b=p+2q+2r,
\quad c=p+2q+2r+s.
\]

After including the gain in \(F_S\), identity (34) becomes

\[
\begin{aligned}
\Delta={}&\frac34p^2r^2+\frac12pr^2(s+3r+4q)\\
&+s^2\left(\frac14r^2+qr+\frac12q^2\right)\\
&+s\left(\frac{11}{6}r^3+7qr^2+7q^2r+\frac73q^3\right)\\
&+\frac{31}{12}r^4+\frac{34}{3}qr^3
 +\frac{33}{2}q^2r^2+\frac{31}{3}q^3r
 +\frac{31}{12}q^4\ge0.
\end{aligned}
\tag{37}
\]

All variables in (35)--(37) are nonnegative. These cases prove (28) when
\(L=S\).

It remains to allow central slack. Fix effective smaller caps

\[
0\le x\le b,\qquad0\le y,z\le a,
\]

for the horns based at \(a,b,c\), respectively; by (32), their larger caps
are \(c,c,b\). First omit the possible gain and define

\[
\begin{aligned}
G(L)={}&abc\left(2L-\frac32S\right)
 -H_L(a;x,c)-H_L(b;y,c)-H_L(c;z,b).
\end{aligned}
\tag{38}
\]

For \(L=S+\delta\), direct expansion gives

\[
G(S+\delta)=G(S)+\delta\Lambda
 +\frac{\delta^2}{2}(cx+cy+bz),
\tag{39}
\]

where

\[
\begin{aligned}
\Lambda={}&2abc-f_a(x)-f_b(y)-f_c(z),\\
f_a(t)={}&\frac{t^3}{6}+\frac{ct^2}{2}+c(a-b)t,\\
f_b(t)={}&\frac{t^3}{6}+\frac{ct^2}{2}+c(b-a)t,\\
f_c(t)={}&\frac{t^3}{6}+\frac{bt^2}{2}+b(c-a)t.
\end{aligned}
\tag{40}
\]

These three functions are convex on their intervals; \(f_b,f_c\) are
nondecreasing, while \(f_a\) is maximized at \(0\) or \(b\). At those two
endpoint choices, respectively,

\[
\Lambda\ge
a^2\left(\frac{b+c}{2}-\frac a3\right)\ge0,
\]

\[
\Lambda\ge
\frac{(b-a)^2[2(b-a)+3(c-b)]}{6}\ge0.
\tag{41}
\]

Thus the gain-free deficit is nondecreasing in \(L\). At \(L=S\), it is
nonnegative for every \(x,y,z\): equations (35)--(37) handle the largest
possible \(b\)- and \(c\)-horns, whose full smaller cap is \(a\).

Only the horn based at \(a\) can have the extra gain from (12), because
\(c+2y\le S\) and \(b+2z\le S\) for the other two. Its gain

\[
g((c+2x-L)_+,c-x)
\]

is nonincreasing in \(L\). Subtracting it preserves the monotonicity of the
full deficit. Since the saturated deficit is nonnegative by (35)--(37), it
remains nonnegative for \(L\ge S\). Maximizing the three horns independently
proves (28). \(\square\)

### Theorem 5.2 (continuous no-corner inequality)

Every positive-volume box-horn set \(K\) of height one satisfies

\[
\boxed{
\frac1{\operatorname{vol}K}
\int_K(x_1+x_2+x_3)\,dx\le\frac23.
}
\tag{42}
\]

#### Proof

Apply Lemma 4.1 to the three horns and then Lemma 5.1 with \(L=1\).
Their total contribution to (8) is at most

\[
abc\left(2-\frac32(a+b+c)\right),
\]

which is the negative of the central contribution (10). Hence
\(\mathcal J(K)\le0\), which is (42). \(\square\)

This theorem is stated only for the finite-step sets needed here. The same
proof extends to arbitrary bounded monotone horn profiles by step
approximation and dominated convergence, but that extension is not part of
the retained B2 interface.

## 6. Application to rectangular thickening

Return to the discrete ideal \(T\), and normalize the weights to
\((1,b,c)\). Let \(K\) be the half-open rectangular thickening constructed in
G4. It lies in the unit simplex. By G4, the absence of a full-support minimal
exclusion is preserved. By G5, after positive diagonal scaling \(K\) is a
box-horn set of the form used in Theorem 5.2. Therefore its continuous
deficit satisfies

\[
\boxed{\kappa_c(K)\ge\frac13.}
\tag{43}
\]

This is the continuous input denoted by \(\gamma=1/3\) in the G4 downstream
formulas. It is now proved rather than left implicit.

## 7. The degree-four cardinality bound

### Lemma 7.1

If \(T\) has no full-support minimal exclusion and every point of \(T\) has
total degree at most four, then

\[
|T|\le29.
\tag{44}
\]

#### Proof

Use the G5 decomposition with central point
\(q=(q_1,q_2,q_3)\). Necessarily \(|q|_1\le4\). At horn \(i\), level
\(t>q_i\), its rectangular section has caps \(r\le q_j\), \(s\le q_k\) and
\(t+r+s\le4\). Consequently

\[
\begin{aligned}
|T|\le{}&\prod_{i=1}^3(q_i+1)\\
&+\sum_{i=1}^3\sum_{t=q_i+1}^4
\max_{\substack{0\le r\le q_j,\ 0\le s\le q_k\\t+r+s\le4}}
(r+1)(s+1).
\end{aligned}
\tag{45}
\]

Dropping the nesting relation between successive sections only enlarges this
upper bound. The expression is symmetric in \(q\), so the possible sorted
central triples and their values in (45) are:

| \(q\) | Bound in (45) | \(q\) | Bound in (45) |
|---|---:|---|---:|
| \((0,0,0)\) | 13 | \((0,0,1)\) | 19 |
| \((0,0,2)\) | 23 | \((0,0,3)\) | 25 |
| \((0,0,4)\) | 25 | \((0,1,1)\) | 25 |
| \((0,1,2)\) | 28 | \((0,1,3)\) | 28 |
| \((0,2,2)\) | 28 | \((1,1,1)\) | 29 |
| \((1,1,2)\) | 29 |  |  |

These are all partitions into at most three parts of an integer at most four.
The largest entry is \(29\), proving (44). \(\square\)

## 8. Proof of the compactness theorem

Scale (2) by \(\alpha\), permute the coordinates, and use the notation
\((1,b,c)\), \(H\), and \(D_0=D/\alpha\). Suppose

\[
D_0<m-1.
\tag{46}
\]

Since \(e_2,e_3\in T\), their weights occur among the attained heights, so

\[
1\le b\le c\le H.
\tag{47}
\]

If \(H<5\), then every \(x\in T\) satisfies

\[
|x|_1\le x_1+bx_2+cx_3\le H<5.
\]

Thus every point has integer total degree at most four, and Lemma 7.1 gives
\(m\le29\), contrary to the hypothesis. Hence

\[
H\ge5.
\tag{48}
\]

Put \(B=1+b+c\). The failure (46) implies \(D_0<m\). The G4 phase estimate,
with \(H>3\), therefore gives the strict bound

\[
B<9+\frac{28}{H-3}.
\tag{49}
\]

The continuous estimate (43) and the strict G4 clipping formula with
\(\gamma=1/3\) give

\[
\frac H3<1+\frac{2B}{3},
\qquad H<3+2B.
\tag{50}
\]

Combining (49) and (50), then multiplying by \(H-3>0\), yields

\[
H^2-24H+7<0.
\tag{51}
\]

The upper root is \(12+\sqrt{137}\), while the lower root is below one.
Together with (48), this proves (4) and Theorem 1.1. \(\square\)

For later analytic leaves, let \(H\) be any allowance at least the actual
weighted height, and define

\[
D_H=3mH-4(1,b,c)\mathbin\cdot\sum_{x\in T}x.
\]

Thickening with denominator \(H+1+b+c\), rather than the attained height plus
the weight sum, still produces a box-horn set inside the unit simplex. If
\(K_H\) denotes this thickening, the same coordinate-sum calculation as in
G4 gives the exact identity

\[
3-4\mathbb E_{K_H}(Y_1+Y_2+Y_3)
=\frac{D_H/m+1+b+c}{H+1+b+c}.
\]

The continuous no-corner estimate (43) bounds the left side below by
\(1/3\). Rearrangement gives

\[
\boxed{
\frac{D_H}{m}\ge\frac{H-2(1+b+c)}3.
}
\tag{52}
\]

Thus, even when the allowance is not attained,

\[
H\ge2(1+b+c)+3\quad\Longrightarrow\quad D_H\ge m,
\tag{53}
\]

including equality in the hypothesis. This is the exact whole-box analytic
acceptance rule used in B2.2.

## 9. Retained interface

The rest of B2 may use this note through the following statements only:

1. the continuous no-corner deficit \(\kappa_c\ge1/3\) in (43);
2. the degree-four cardinality bound \(|T|\le29\) in (44);
3. every failure with \(m\ge30\) lies in the closed region (1);
4. the weak analytic-leaf rule (52)--(53).

The boundary-potential optimization is a proof of item 1, not an additional
computational obligation. The only remaining B2 verification is the exact
horn-DP and closed interval coverage specified in B2.2.
