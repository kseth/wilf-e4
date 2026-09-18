# A one-slab bridge for arbitrary rectangular horns

**Status:** complete analytic proof; independently audited by two separate reviewers.
The companion exact coefficient checker passes all six identities used below.
This proves a geometric horn reduction, not Wilf's conjecture by itself.

Normalize maximum coordinate sum to one. Fix `a,B,C>=0` with
`a+B+C<=1`. A horn based at `a` has nested rectangular fibers
`f(t)<=B`, `g(t)<=C`, and `t+f(t)+g(t)<=1`. Write

\[
J_H=\int f(t)g(t)\left(3t+\frac32(f(t)+g(t))-2\right)dt.
\]

For caps `(x,y)`, let `Q(x,y)` denote the supremum of this objective over
continuous monotone profiles on the height boundary, starting at
`t=1-x-y` with caps `(x,y)` and ending at zero. This is the previously
proved exact boundary potential; its formula is not needed in the proof
below. The value zero is available by taking a zero cap.

## Theorem

\[
\boxed{J_H\le
\max_{0\le x\le B,\;0\le y\le C}
\left[\left(1-\frac32(1-a)\right)
(1-a-x-y)xy+Q(x,y)\right].}
\]

Thus every arbitrary horn is dominated by one initial constant slab with
effective caps, followed by a continuous boundary horn. The first slab
runs from `a` to `1-x-y`. The theorem allows strict central slack.

The already proved late-horn theorem handles `a>=1/3`. We prove the
remaining case `a<1/3`.

## 1. Exact transition and interpolation formulas

Set `A(r)=1-3r/2` and reverse time `r=1-t`. The endpoint-convexity lemma
reduces any finite step horn to an endpoint-tight staircase of at least
its objective. If consecutive tight cap sums are `r>s`, and the later
rectangle is `(x,y)` with `x+y=s`, its exact slab payoff is

\[
A(r)(r-s)xy.\tag{1}
\]

The initial reverse time is `r_0=1-a`; the initial rectangle need not fill
its caps, so there need not be a rectangle at `r_0`.

On a boundary branch with one transverse side fixed at `c`, replace a
continuous segment of length `d` in the other side by one tight slab.
The **jump gain over continuity** is

\[
g_c(d)=\frac c4d^2(2d+3c-2).\tag{2}
\]

It depends only on the jump length, not its location along the branch.
Also

\[
g_c(d+e)-g_c(d)-g_c(e)
 =\frac{3c}{2}de\left(d+e+c-\frac23\right).\tag{3}
\]

Both identities follow by integrating `c(r-c)A(r)` along the boundary.

## 2. The negative part can be moved to an L-shaped boundary path

Sort transverse coordinates at every state, and sort the original caps,
so `B<=C` and every actual state is `(x_i,y_i)` with `x_i<=y_i`.
Sorting preserves nesting, cap bounds, sums, products, and objective.

If every nonzero slab ends at reverse time greater than `2/3`, every slab
has nonpositive payoff by (1), so the empty horn dominates. Otherwise,
let `(u,v)`, `u<=v`, be the first staircase state with
`t:=u+v<=2/3`. From this state onward the late boundary bridge applies.
Replace that tail by the capped-balanced continuous boundary profile
with value `P(u,v)`. In particular `u<=1/3`.

All preceding slab coefficients `A(r_previous)` are nonpositive. For
any preceding state of sum `s>=u+v`, nestedness and caps imply

\[
x\ge u,\qquad y\le C,\qquad x\le y.
\]

Consequently the smallest possible product at that sum is attained at

\[
x_*(s)=\max(u,s-C),\qquad
 y_*(s)=\min(C,s-u).\tag{4}
\]

Indeed `x(s-x)` is nondecreasing for `x<=s/2`, and (4) is its smallest
feasible `x`. This state is feasible: `x_*<=B`, `y_*<=C`,
`x_*<=y_*`, and both coordinates are nondecreasing in `s`.
At `s=u+v`, it equals `(u,v)`. Replacing every earlier state using (4)
therefore preserves nesting and weakly increases every early slab payoff.

All actual states now lie on the L path

\[
(B,C)\longrightarrow(u,C)\longrightarrow(u,u),
\]

followed by the balanced diagonal to zero. Its first branch holds `C`
fixed, and its second holds `u` fixed. The initial reverse time can be
represented formally by the virtual state `(x_0,C)`, where

\[
x_0=r_0-C\ge B.
\]

The part with first coordinate above `B` is only a device for computing
jump gains: the first actual jump necessarily covers it. Every profile
constructed below retains a first jump of length at least `x_0-B`, unless
it is replaced by an explicitly admissible one-slab profile.

## 3. Jumps wholly on the smaller-side branch can be filled

A jump on the branch with fixed side `u` has length

\[
d\le C-u\le1-2u.
\]

The last inequality uses `C+u<=B+C<=1`. Hence

\[
2d+3u-2\le-u\le0,
\]

so (2) shows its gain is nonpositive. Replace all such jumps by
continuity. The balanced tail is already continuous. At most one jump
can cross the turn of the L path.

## 4. A cross-turn jump reduces to the turn or to balance

Suppose a cross-turn jump starts at `(u+p,C)`, ends at `(u,C-q)`, and is
followed by the continuous smaller-side branch and balanced tail. Here
`p,q>=0` and `q<=C-u`. Its gain over the L-shaped continuous path between
those endpoints is

\[
\begin{aligned}
G(p,q;u,C)=\frac14\bigl(&3C^2p^2+2Cp^3-2Cp^2
 +6p^2qu+6pq^2u+6pqu^2-4pqu\\
 &+2q^3u+3q^2u^2-2q^2u\bigr).
\end{aligned}\tag{5}
\]

Direct differentiation gives

\[
\frac{\partial G}{\partial q}
 =\frac u2(p+q)\bigl(3p+3q+3u-2\bigr).\tag{6}
\]

For fixed `p,u,C`, this derivative changes sign at most once, from
negative to positive. Thus the maximum on `0<=q<=C-u` is attained at
`q=0` or `q=C-u`. The continuous baseline from the jump's start all the
way to zero is independent of `q`, so the same endpoint statement holds
for the whole jump plus its continuation.

The endpoint `q=0` leaves a jump entirely on the first branch, followed
by a continuous tail. It remains to eliminate the balanced endpoint
`q=C-u`.

Let `r` be the reverse time at the start of this balanced-ending jump.
A jump to `(z,z)` followed by the balanced boundary tail has value

\[
F_r(z)=A(r)(r-2z)z^2+\frac23z^3-\frac32z^4.
\]

Its derivative factors as

\[
F_r'(z)=-6z\left(z-\frac r2\right)
                 \left(z-r+\frac23\right).\tag{7}
\]

On every interval `0<=z<=L<=r/2`, this derivative changes sign at most
once, from negative to positive. Therefore

\[
F_r(z)\le\max\{0,F_r(L)\}.\tag{8}
\]

There are two cases.

* **The cross-turn jump is not the initial jump.** Its starting state is
  an actual state `(x,C)`, with `x<=B<=C` and `r=x+C<=1`. Take `L=x` in
  (8). The value `F_r(x)` is a jump along the fixed-`x` branch from
  `(x,C)` to `(x,x)`, followed by the balanced tail. By Section 3 this is
  bounded by its continuous capped-balanced boundary value `P(x,C)`.
  Thus the cross-turn jump and all its continuation are bounded by
  `max(0,P(x,C))`. If the zero alternative is used, all earlier slabs
  were in the negative part, and their sum is nonpositive; the entire
  horn is dominated by zero. Otherwise replace this jump and tail by
  the continuous profile with value `P(x,C)`.

* **The cross-turn jump is the initial jump.** Its formal start may have
  `x_0>B`. Apply (8) with `r=r_0` and `L=B`; this is valid because
  `B<=C` and `B+C<=r_0` imply `B<=r_0/2`. The zero alternative again
  suffices, or `F_(r_0)(B)` is attained by one initial slab to `(B,B)`
  followed by its balanced boundary tail. This is an admissible
  one-slab profile and is already bounded by the theorem's envelope.

Consequently, unless a one-slab profile or zero has already dominated
the whole horn, all remaining jumps lie on the first, fixed-`C` branch.

## 5. All remaining jumps merge into one initial jump

The remaining profile consists of jumps and continuous intervals along
a fixed-`C` branch, followed by a continuous boundary tail. Relative to
its wholly continuous baseline, each jump contributes (2).

Retain the first jump, of length `d_0>=x_0-B`, even if its gain is
negative. If `x_0=B` and there is no initial jump, insert a zero-length
initial jump; this changes neither feasibility nor the objective. Replace every later jump of nonpositive gain by continuity.
For each remaining later jump of length `e`, its gain is positive. If
`C<2/3`, positivity implies

\[
e>\frac32\left(\frac23-C\right)>\frac23-C.
\]

If `C>=2/3`, the expression `d+e+C-2/3` is automatically nonnegative.
In either case (3) proves that merging this jump into the initial jump
weakly increases their total gain. Location independence in (2) permits
reordering the finite list of jump lengths and continuous lengths along
this fixed-`C` interval, preserving their total length, so this jump can
be placed directly after the initial jump before merging. This does not
slide a jump through another state while pretending those states remain
fixed; it constructs a new nested boundary/slab profile with the same
continuous baseline and the same individual jump gains. The merged length
never exceeds the total fixed-`C` branch length, and only increases the
initial jump length, so the cap constraint remains satisfied.

After finitely many merges, there is a single initial jump, followed by
an entirely continuous boundary profile. Its effective caps are within
`(B,C)`. Replacing its continuous continuation by the optimal one, with
value `Q`, proves the desired envelope inequality.

## 6. General monotone profiles

Approximate a bounded nested rectangular profile from below by finite
step profiles, preserving its cap and height constraints. Their volumes
and first moments converge by dominated convergence. Every finite step
profile is bounded by the same envelope, as just proved. Passing to the
limit establishes the theorem for arbitrary monotone profiles.

## Scope

The independently proved joint bound in
`../joint_horns/joint_effective_cap_theorem.md` bounds the three one-slab
envelopes against a central box. Together these results complete the
continuous no-interior-corner mean inequality. The present note does not
supply a discrete Wilf argument, and does not treat an interior corner.
