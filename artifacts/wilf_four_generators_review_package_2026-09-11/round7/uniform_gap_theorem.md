# An exact uniform gap and a four-generator multiplicity cutoff

Date: 10 September 2026.

## Scope and result

Let \(K\subset\mathbb R_{\ge0}^3\) have positive finite volume, lie in

\[
\{x:x_1+x_2+x_3\le1\},
\]

and have complement, within the nonnegative orthant, equal up to boundary
conventions to a finite union of upper orthants. Suppose at most one of
their coordinatewise minimal vertices has all three coordinates positive.
Then the computer-assisted argument below proves

\[
\boxed{\kappa_c(K):=3-4\mathbb E_K(X_1+X_2+X_3)\ge\frac5{42}.}
\tag{1}
\]

This class includes every diagonally scaled rectangular thickening of a
preferred four-generator Apéry ideal. The phase argument in Section 6
therefore gives

\[
\boxed{m\ge82{,}161\ \Longrightarrow\ W_4(S)>0.}
\tag{2}
\]

Here \(S=\langle m,a_1,a_2,a_3\rangle\) is minimally four-generated,

\[
W_4(S)=4|S\cap[0,c)|-c,
\]

and \(c\) is its conductor. This proves an eventual strict inequality. It
does not eliminate all smaller multiplicities or prove unrestricted Wilf.

The finite premise was independently implemented in two C++ programs.
Their 1,029 saved per-corner outputs were compared exactly in this audit.
A freshly written third implementation in JavaScript then recomputed every
one of those outputs. All 1,029 comparisons passed. The program does not
use floating-point approximations to certificate decisions: every computed
quantity is an exactly representable bounded integer.

## 1. The precise finite premise

For a nonempty finite lower ideal \(T\subset\mathbb N^3\), put

\[
m_T=|T|,\qquad
D_R(T)=3R m_T-4\sum_{x\in T}|x|_1.
\]

For each integer \(R\in\{18,19,20,21\}\), the finite calculation proves

\[
\boxed{T\subseteq\{|x|_1\le R\},\quad
T\text{ has at most one full-support minimal excluded point}
\quad\Longrightarrow\quad D_R(T)\ge4m_T.}
\tag{3}
\]

Neither equality of the actual maximum degree with \(R\), nor membership
of the coordinate unit vectors, is assumed. The empty ideal satisfies (3)
by equality and is handled separately. The recorded maxima are over
nonempty ideals, which explains why every maximum in the table is negative.

| Degree allowance \(R\) | Sorted positive corner configurations | Maximum of \(4m_T-D_R(T)\) |
|---:|---:|---:|
| 18 | 204 | -50 |
| 19 | 237 | -53 |
| 20 | 274 | -56 |
| 21 | 314 | -59 |

Each maximum is \(4-3R\), the value for the singleton ideal \({0}\).
The stronger negative values are unnecessary for (3).

## 2. Why the finite configuration range covers every ideal

A minimal excluded point \(p\notin T\) is one for which every smaller
nonnegative integer vector belongs to \(T\). If its three coordinates are
positive, its three immediate predecessors belong to \(T\). Consequently

\[
|p|_1-1\le R.
\]

All actual full-support corners therefore satisfy

\[
p_i\ge1,\qquad |p|_1\le R+1.
\tag{4}
\]

The unit-weight score and height constraint are invariant under coordinate
permutations, so it suffices to enumerate \(p_1\le p_2\le p_3\).
The nested loops in the certificate enumerate each such triple exactly once.

To represent an ideal with a full-support corner \(p\), delete that one
generator from the excluded monomial ideal. The remaining complement
defines a finite lower ideal \(U\), all of whose minimal excluded points
have support at most two. Then

\[
T=U\setminus(p+\mathbb N^3).
\tag{5}
\]

The pure-axis exclusions remain present, so \(U\) is finite. Moreover,
the positive corner removes no axis point. Each axis cap of \(U\) is
therefore at most \(R\), because the same axis points belong to \(T\).
An axis cap can be zero: this explicitly permits missing unit vectors.

If \(T\) has no full-support corner, take \(U=T\) and choose the inactive
corner \(p=(1,1,R-1)\). Its degree is \(R+1\), so its upper orthant does not
intersect \(T\). It satisfies (4) and the ordering requirement for these
four values of \(R\). Thus the no-interior cases are included in the same
finite calculation.

The program does not require an enumerated \(p\) to be minimal excluded
in the resulting set. Allowing an inactive or nonminimal corner enlarges
the collection considered and is safe for the upper bound.

## 3. Central boxes, rectangular sections, and the exact recurrence

### 3.1 Representation of the no-interior closure

For a lower ideal \(U\) with no full-support minimal excluded point,
membership is determined by the three coordinate-plane projections:

\[
x\in U\quad\Longleftrightarrow\quad
(x_1,x_2,0),(x_1,0,x_3),(0,x_2,x_3)\in U.
\tag{6}
\]

Indeed, any omitted point dominates a minimal excluded point; its support
lies in one of those planes.

Here is the structural argument underlying the recurrence. Make graph
vertices \((i,t)\) for every coordinate \(i\) and every level between zero
and its axis cap. Vertices of one coordinate are all adjacent. Vertices
\((i,t),(j,s)\) with \(i\ne j\) are adjacent when \(t e_i+s e_j\in U\).
External neighborhoods are nested as the level increases. An induced cycle
of length at least four would repeat one of the three coordinate classes.
The repeated vertices must be adjacent, since that class is a clique.
The external neighbor of the higher repeated level is also adjacent to
the lower level, giving a forbidden chord. Thus the graph is chordal.

By the clique-tree theorem for chordal graphs, the maximal cliques admit
a tree with the running-intersection property. A maximal clique contains
coordinate prefixes, and by (6) its three coordinate maxima are a maximal
point of \(U\). The tree is therefore a tree on maximal boxes of \(U\)
such that every coordinate superlevel set of boxes is connected.

Each leaf has a coordinate strictly larger than that of its neighboring
box. Connectedness makes this a strict global maximum in that coordinate.
Different leaves cannot use the same coordinate, so there are at most three
leaves. Choose nodes attaining each coordinate maximum, and take their
tree median. Along the path from this central node toward the maximum of
coordinate \(i\), coordinate \(i\) is increasing and the other coordinates
are nonincreasing. The increasing coordinate is strictly increasing between
distinct consecutive maximal boxes, since otherwise one box would dominate
the other. Every branch reaches one of the selected maximum nodes, because
each terminal leaf has a strict coordinate maximum.

It follows that \(U\) is the disjoint union of a central integer box

\[
[0,c_1]\times[0,c_2]\times[0,c_3]
\]

and at most three parts. Part \(i\) lies at levels \(t>c_i\), and its
sections perpendicular to coordinate \(i\) are rectangles
\([0,u_t]\times[0,v_t]\), where both \(u_t\) and \(v_t\) are nonincreasing
and bounded by the corresponding central caps. This argument also covers
a path, a single box, and zero axis caps.

This is the representation proved in
`round3/no_interior/clique_tree_and_bipartite_bound.md`, Sections 1–3.
The standard clique-tree theorem is the only graph-theoretic input.

### 3.2 Scores and transitions

Fix \(R,p\). Define the exact point score

\[
f_R(x)=4|x|_1+4-3R.
\]

For a rectangle on outward axis \(i\) at level \(t\), let

\[
A_i(t,u,v)=\{x:x_i=t,\ 0\le x_j\le u,\ 0\le x_k\le v,\ x\not\ge p\}.
\]

Its score \(C_i(t,u,v)=\sum_{A_i(t,u,v)}f_R(x)\) and maximum degree
are calculated exactly. A section is feasible when every retained point
has degree at most \(R\). Its uncut upper-right corner may exceed \(R\)
when that corner has been removed; the retained degree is what matters.

Let \(H_i(t,b,c)\) be the largest possible score of a possibly empty
nested sequence of these sections starting at level \(t\), with transverse
caps at most \(b,c\). The exact recurrence is

\[
H_i(t,b,c)=\max\left(0,
\max_{\substack{0\le u\le b,\ 0\le v\le c\\ A_i(t,u,v)\ \mathrm{feasible}}}
\{C_i(t,u,v)+H_i(t+1,u,v)\}\right).
\tag{7}
\]

The terminal condition is \(H_i(R+1,b,c)=0\). An absent section terminates
the part, since the sequence belongs to a lower ideal. The option zero
accounts for that termination. Every uncut section contains its axis
point, which survives because \(p>0\), so no nonempty section can occur
beyond \(R\).

For each central cap \(c\in\{0,\ldots,R\}^3\), clip the central box by
\(p+\mathbb N^3\), require its retained points to have degree at most \(R\),
and add its score to

\[
H_1(c_1+1,c_2,c_3)+H_2(c_2+1,c_1,c_3)+H_3(c_3+1,c_1,c_2).
\tag{8}
\]

The central box and these three parts are disjoint even before clipping.
Their score sum is exactly \(4m_T-D_R(T)\). The representation and the
recurrence cover every \(T\) in (3), with no assumptions on residue labels
or coordinate units. Taking the maximum over all central caps and all
corners (4) proves the scope of the finite premise.

### 3.3 Implementation independence and integer bounds

The canonical C++ evaluator uses closed cardinality and moment formulas
for boxes minus the clipped upper boxes. The separate C++ evaluator sums
literal point scores and uses explicit transitions over every allowed
subrectangle in (7).

The fresh JavaScript evaluator also sums literal points, but implements
the maximum in (7) by the monotone prefix identity: compare the current
rectangle with the optima for caps \((b-1,c)\) and \((b,c-1)\). This is
equivalent because every proper subrectangle reduces at least one cap.
It calculates central scores by three-dimensional prefix sums. It does
not use the canonical closed box-moment formulas.

For \(n=R+1\le22\), all signed intermediate expressions are bounded in
absolute value by \(8n^3(9R+4)<2^{31}\). Stored scores use signed 32-bit
integer arrays; intermediate JavaScript arithmetic remains exactly
representable because every integer is far below \(2^{53}\). A runtime
assertion checks the bound. The rational algebraic checks use `BigInt`.

The byte-identical prior record hash is

`936f87f13fffe2ed7cb18fd85ebc06536308648fcb4e43febe90c9a1184d7fad`.

The new complete recomputation passed all 1,029 individual comparisons,
not merely the four aggregate maxima.

## 4. Transfer the finite premise to continuous sections

Take \(h=1/21\). Decompose almost every point of the nonnegative orthant
uniquely as

\[
x=r+hy,\qquad r\in[0,h)^3,\quad y\in\mathbb N^3.
\]

For fixed \(r\), define \(T_r=\{y:r+hy\in K\}\). Each nonempty \(T_r\)
is a finite lower ideal. Under this map an excluded orthant with vertex
\(g\) has integer inverse-image vertex

\[
g'_i=\max\left(0,\left\lceil\frac{g_i-r_i}{h}\right\rceil\right).
\tag{9}
\]

A zero coordinate of \(g\) stays zero. Thus vertices supported on at most
two coordinates cannot create a full-support excluded vertex. The single
possible full-support vertex maps to at most one such vertex, and removing
redundant generators cannot increase that number. Boundary choices affect
only a null set of \(r\). This proves the required restriction for \(T_r\),
including sections lacking coordinate units.

Set

\[
R_r=\left\lfloor\frac{1-|r|_1}{h}\right\rfloor,
\qquad \varepsilon_r=1-|r|_1-hR_r.
\]

Since \(0\le |r|_1<3h\),

\[
R_r\in\{18,19,20,21\},\qquad0\le\varepsilon_r<h.
\]

Every point of \(T_r\) has degree at most \(R_r\). Direct expansion gives

\[
\begin{aligned}
\sum_{y\in T_r}(3-4|r+hy|_1)
&=hD_{R_r}(T_r)+(3\varepsilon_r-|r|_1)|T_r|\\
&\ge(4h-|r|_1)|T_r|,
\end{aligned}
\tag{10}
\]

where (3) was applied and the nonnegative remainder was discarded. Empty
sections contribute zero. Integration over \(r\in[0,h)^3\), followed by
division by the volume of \(K\), yields

\[
\kappa_c(K)\ge4h-\sum_{i=1}^3\mathbb E_K(X_i\bmod h).
\tag{11}
\]

There is no additional factor \(h^3\): the integral here is over the
continuous translation variable \(r\), and each map \(r\mapsto r+hy\)
has Jacobian one.

## 5. The exact remainder average

Fix all coordinates of a point of \(K\) except coordinate \(i\). Downward
closure makes its fiber an interval from zero to a length \(H\ge0\),
up to endpoints. Writing \(H=qh+t\), where \(q\ge0\) is an integer and
\(0\le t<h\), gives

\[
\int_0^H (x\bmod h)\,dx
=\frac{qh^2+t^2}{2}
\le\frac{h(qh+t)}2
=\frac{hH}{2}.
\tag{12}
\]

Integrate over the other coordinates. Fubini's theorem gives

\[
\mathbb E_K(X_i\bmod h)\le\frac h2.
\]

Applying this for all three coordinates in (11) proves

\[
\kappa_c(K)\ge4h-\frac{3h}{2}
=\frac{5h}{2}=\frac5{42},
\]

as asserted in (1). This averaging step is essential to the stated
constant; the pointwise bound \(|r|_1<3h\) would give only \(1/21\).

## 6. The discrete phase estimate and the Apéry consequence

Choose the preferred factorization ideal \(T\) for
\(\operatorname{Ap}(S,m)\). Write

\[
M=\max_{x\in T}a\cdot x=c+m-1,\qquad
\Sigma=\sum_{x\in T}a\cdot x,\qquad
D=3mM-4\Sigma.
\]

The exact genus identity is

\[
mW_4=D-m(m-1).
\tag{13}
\]

Normalize \(u_i=a_i/M\), \(v=\min_i u_i\), \(U=\max_i u_i\),
\(s=\sum_i u_i\), \(\kappa=D/(mM)\), and
\(\mu_i=\mathbb E_T(u_iX_i)\). The coordinate units belong to \(T\), so
\(u_i\le1\). The rectangular thickening of \(T\), with side lengths
\(u_1,u_2,u_3\), has maximum total coordinate \(1+s\). After rescaling
it into the unit simplex, its mean and defect give the exact identity

\[
\kappa_c=\frac{\kappa+s}{1+s}.
\tag{14}
\]

Its excluded orthant vertices have exactly the supports of the discrete
minimal excluded points. The preferred Apéry ideal has at most one
full-support excluded point: its representative must have disjoint support,
hence must be zero; distinct excluded points with intersecting supports
have distinct residues. These facts follow by subtracting a common
positive coordinate and using residue injectivity on \(T\). Thus (1)
applies to the thickening.

For completeness, the phase estimate used next can be derived as follows.
Let \(\delta_j(x)\) be the nonnegative normalized slack of the top of the
coordinate-\(j\) line through \(x\). Coordinate fibers give

\[
\bar\delta_j=1-\sum_i\mu_i-\mu_j
=\frac{1+\kappa}{4}-\mu_j,
\qquad \sum_j\bar\delta_j=\kappa.
\tag{15}
\]

Choose \(k\) of minimum weight \(v\). On a \(k\)-fiber of length \(L\),
the residue of \(\delta_j(t)\) modulo \(u_j\), \(j\ne k\), is
\([A-tv]_{u_j}\) for a fixed \(A\). For \(0\le r\le v\),

\[
[A-tv+r]_{u_j}\le\delta_j(t)+r.
\]

The \(L\) associated intervals concatenate into one interval of length
\(h_0=Lv\). Every interval of that length has sawtooth integral at least

\[
\frac{q u_j^2+r_0^2}{2}
\ge\frac{h_0^2}{2(q+1)}
\ge\frac{u_jh_0^2}{2(h_0+u_j)},
\]

where \(h_0=q u_j+r_0\), \(0\le r_0<u_j\). The first inequality uses
the minimum remainder-arc integral \(r_0^2/2\); the next uses
Cauchy–Schwarz. Since \(h_0\le1+v\), comparison with the preceding upper
integral gives

\[
\operatorname{mean}_{\rm fiber}\delta_j
\ge\frac{u_jvL}{2(1+v+u_j)}-\frac v2.
\]

Averaging with fiber-length weights and using
\(v\mathbb E L=2\mu_k+v\) yields

\[
2\bar\delta_j(1+v+u_j)
\ge2u_j\mu_k-v(1+v).
\tag{16}
\]

Sum (16) for \(j\ne k\), use (15), and bound \(u_j\le U\le s-2v\).
The coefficient of \(\bar\delta_k\) in this substitution is the middle
weight minus \(1+v\), hence nonpositive. Discarding this term and
rearranging gives

\[
s(1-3\kappa)\le4\kappa+5v-3\kappa v+4v^2.
\tag{17}
\]

This is the summed phase lemma (S1) in
`deliverables/wilf_fixed_dimension_finite_reduction_2026-09-05.md`.
Its independent foundational review is `round6/audit_foundations.md`.

Suppose \(W_4\le0\). From (13),

\[
0\le\kappa=\frac{W_4+m-1}{M}
\le\frac{m-1}{M}<v.
\tag{18}
\]

Nonnegativity here follows from the coordinate-line slack identity.
If \(v<1/3\), the right side of (17), divided by \(1-3\kappa\), is
strictly increasing in \(\kappa\). Its derivative numerator is
\(4+12v+12v^2>0\). Consequently

\[
s<\frac{9v+v^2}{1-3v}.
\]

The expression in (14) is increasing in both \(\kappa\) and \(s\) when
\(\kappa<1\). Therefore

\[
\frac5{42}\le\kappa_c
<\frac{2v(5-v)}{1+6v+v^2}.
\tag{19}
\]

Cross multiplication gives

\[
89v^2-390v+5<0.
\]

Writing \(H=1/v=M/a_{\min}\), we obtain

\[
5H^2-390H+89<0.
\]

The polynomial is positive at \(H=78\) (its value is \(89\)) and is
strictly increasing on \([78,\infty)\). Thus \(H<78\). Since each
\(x\in T\) satisfies \(a_{\min}|x|_1\le a\cdot x\le M\),

\[
T\subseteq\{|x|_1\le77\},\qquad
m\le\binom{80}{3}=82{,}160.
\]

If \(v\ge1/3\), the same elementary lattice count instead gives
\(m\le\binom63=20\). Both branches show that a nonpositive \(W_4\)
requires \(m\le82{,}160\), proving (2), including strictness.

## 7. Reproduction and audit record

From the repository root, run

```sh
node round7/verify_uniform_gap.js
```

This fully recomputes the finite strip using the fresh JavaScript
implementation, checks the complete corner enumeration, compares all
scores to both older C++ output files, checks exact algebraic identities,
and writes:

- `round7/uniform_gap_js_strip.txt`: all 1,029 newly computed scores;
- `round7/uniform_gap_verification.json`: exact comparison and summary;
- `round7/uniform_gap_prior_comparison.json`: separately recorded comparison
  of the two historical output files.

The option `--records-only` checks saved records and identities without
recomputing the recurrence, and marks this weaker scope in the output.
The delivered verification record was produced by the default full run.

Historical source and output dependencies are:

- `round6/uniform_gap/canonical_strip.cpp` and `canonical_strip.txt`;
- `round5/weighted_analytic/one_corner/one_corner_unit_dp.cpp`;
- `round6/uniform_gap/independent_strip.cpp` and `independent_strip.txt`.

The canonical wrapper includes the round5 evaluator. The independent C++
file is standalone. Neither compiled binary is needed in an archive.
The older `independent_strip_worker.cpp` is another implementation using
disjoint box integration; its output is not silently substituted for the
literal-point `independent_strip.cpp` output compared in this audit.

The JavaScript program is newly written on 10 September, not a recovered
artifact from a prior message. The exact saved C++ outputs were inspected
and compared; their binaries were not redundantly rerun in this audit,
because every score was independently recomputed by the new evaluator.

## 8. Remaining limits

The integer strip is exhaustive for the precisely stated geometric class;
it is not a sampling grid. Its continuous extension uses exact integration
over all translations. The tail bound additionally uses the Apéry and
phase lemmas proved above.

None of these arguments establishes \(W_4\ge0\) for every
\(30\le m\le82{,}160\). The independently established strong conductor
reduction still says that a negative example has

\[
M\le m(m-2),\quad a_3\le m(m-2),\quad c\le m^2-3m+1.
\]

Combining this with separately completed subclass theorems narrows the
remaining question, but does not eliminate it. External mathematical
review and formal verification have not been performed. The in-session
mathematical reasoning, separate implementations, and exact outputs are
made explicit here so those conclusions can be reviewed.
