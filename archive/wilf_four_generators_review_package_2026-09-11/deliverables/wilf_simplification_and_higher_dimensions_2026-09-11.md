# Simplifying the proposed four-generator Wilf proof and extending its methods

11 September 2026.

## Status and main findings

The preceding manuscript presents a complete computer-assisted argument for four generators, with exact certificate checks and in-session audits. It remains a proposed research proof pending external mathematical review; it has not been formalized in a proof assistant. This supplement records a new simplification, elementary dimension-independent deductions, and explicit limitations of the geometric method.

**Actual simplification:** the two residual low-height certificate streams can be replaced by one centroid-witness theorem. All **3,742,041** surviving low-degree shapes now have certificates valid for every real normalized weight vector, with no upper bound on normalized height. A separate verifier completed a full exact replay, and the portable verification entry point completed a second fresh replay. The new registry has **6,816** bases, compared with **10,246** across the two old registries.

This removes a weight-dependent case distinction and a duplicated certificate stream. It does **not** remove exhaustive finite-shape verification. An analytic replacement remains an open objective of this project.

**Generalization:** the exact Wilf moment identity, the negative-integer bridge, corner-support restrictions, surface budgets, and erosion inequalities all extend to arbitrary embedding dimension. The archived analytic manuscript also proposes an eventual-Wilf theorem at each fixed embedding dimension, but its remaining finite bounds are enormous and it requires review independently. Five or more generators have not been settled here.

**Structural obstruction:** two explicit, minimally five-generated numerical semigroups show why the three-coordinate box-and-horn classification does not simply extend by adding another coordinate.

## 1. A cleaner residual four-generator theorem

Let
\[
S=\langle m,a_1,a_2,a_3\rangle,\qquad
A=\min_i a_i,\qquad b_i=a_i/A\ge1.
\]
Choose the preferred Apéry factorization lower ideal \(T\subset\mathbb N^3\).
Put
\[
m=|T|,\quad s=\sum_{x\in T}x,\quad
M=\max_{x\in T}a\cdot x=c+m-1,\quad
H=M/A.
\]
Define
\[
D_0=3mH-4b\cdot s.
\]
The residual certificate target is \(D_0\ge m-29/10\).

### The verified centroid theorem

For every shape in the finite residual class specified below, there exists
\[
z\in\operatorname{conv}(T)
\]
such that, coordinatewise,
\[
r=3mz-4s\ge0,\qquad
\sum_{i=1}^3r_i\ge m-\frac{29}{10}.
\tag{1}
\]
Every constructed witness is a convex combination of at most three lattice points of \(T\).

The implication to all real normalized weights has a short proof:
\[
\begin{aligned}
3mH-4b\cdot s
&\ge 3m\,b\cdot z-4b\cdot s\\
&=b\cdot r\\
&\ge\sum_i r_i\\
&\ge m-\frac{29}{10}.
\end{aligned}
\tag{2}
\]
The first inequality is convexity; the third uses \(b_i\ge1\) and \(r_i\ge0\). No upper bound on \(H\) is used. In terms of the centroid \(\bar x=s/m\), the witness is a point of the convex hull lying coordinatewise beyond \((4/3)\bar x\), with the additional total surplus in (1).

### Exact scope of the finite class

The theorem applies to lower ideals \(T\subset\{x\in\mathbb N^3:|x|_1\le6\}\) with \(m\ge30\), one full-support minimal excluded point \(p\), and \(5\le|p|_1\le7\), satisfying the following necessary arithmetic restrictions.

1. Each coordinate-plane projection has at most \(|p|_1-2\) mixed minimal excluded points. Of those dominating the corresponding projection of \(p\), at most the opposite coordinate of \(p\) are allowed.
2. For \(B=\{0,e_1,e_2,e_3\}\) and \(E=T\ominus B=\{x:x+B\subseteq T\}\),
   \[
   |E|+\sum_i|E\cap\{x_i=0\}|\le m.
   \]
3. For \(F_i=\{x\in T:x+e_i\notin T\}\) and \(n_k=1+\max_T x_k\),
   \[
   |F_i\cap F_j|\le2n_k\qquad(\{i,j,k\}=\{1,2,3\}).
   \]

These restrictions are necessary for genuine preferred Apéry ideals. They are not asserted to characterize realizability. The complete finite enumeration treats the larger class passing these filters, so allowing nonrealizable shapes cannot omit a genuine case.

After sorting the coordinates of \(p\), the coverage is:

| Corner \(p\) | Certified shapes |
|---|---:|
| \((1,1,3)\) | 708,617 |
| \((1,2,2)\) | 976,430 |
| \((1,1,4)\) | 571,100 |
| \((1,2,3)\) | 519,716 |
| \((2,2,2)\) | 533,570 |
| \((1,1,5)\) | 150,481 |
| \((1,2,4)\) | 100,341 |
| \((1,3,3)\) | 90,696 |
| \((2,2,3)\) | 91,090 |
| **Total** | **3,742,041** |

The earlier exclusions and structural arguments covering small multiplicity, no full-support corner, and corners \((1,1,1)\) and permutations of \((2,1,1)\) are still dependencies of the global proof. This theorem concerns its residual class.

### The improved proof split

Let \(R=\max_{x\in T}|x|_1\).

| Residual case | Applicable result |
|---|---|
| \(R\le6\) | The new centroid theorem, valid at all normalized heights |
| \(R\ge7\) | \(H=\max_T b\cdot x\ge R\ge7\), so the existing high-height theorem applies |

Thus the branch criterion depends only on the ideal, not on the weights.

Finally,
\[
mW_4=AD_0-m(m-1).
\]
If \(W_4<0\), integrality and \(A\ge m+1\) give
\[
m-D_0\ge\frac{3m}{m+1}\ge\frac{90}{31}>
\frac{29}{10}\qquad(m\ge30).
\]
The difference between the last two constants is exactly \(1/310\). Hence (2) excludes a negative Wilf number in the residual low-degree class.

## 2. What has been simplified, and what would remove the computation

The new certificates have a uniform mathematical meaning. Their point multipliers sum to \(3m\); their three weight-bound multipliers are exactly the coordinates of \(r\) in (1). The height-upper-bound column is forbidden. The completed registry also uses no redundant lower-height column.

The new 6,816 oriented bases comprise 2,723 types under coordinate permutation. Those counts describe this registry; they are not proved minima. The old registry's separate compression statistics should not be confused with these new counts.

The best candidate for an analytic replacement is now explicit:

> Derive the centroid witness (1) directly from the residue restrictions and the geometry of a lower ideal, without listing each ideal.

Even a handful of symbolic sufficient conditions that exhaust the structural possibilities would be useful. The recorded bases provide examples of such conditions, but grouping them by symmetry does not prove that the groups exhaust an unbounded family.

For instance, suppose \(T\) contains the three axis points \(r_1e_1,r_2e_2,r_3e_3\). The condition
\[
r_1\left(3m-\frac{4s_2}{r_2}-\frac{4s_3}{r_3}\right)-4s_1
\ge m-\frac{29}{10}
\tag{3}
\]
provides a witness: use point multipliers
\[
3m-\frac{4s_2}{r_2}-\frac{4s_3}{r_3},\qquad
\frac{4s_2}{r_2},\qquad
\frac{4s_3}{r_3}.
\]
For \(m\ge30\), (3) ensures their nonnegativity; only the first coordinate has surplus. This is a concrete family of symbolic proofs, but it is not known here to cover all remaining shapes.

For the high-height branch, another precise target is a closed-form majorant for the horn dynamic program. If the score of a retained horn section is \(g_i(t,r,s)\), a function \(V_i(t,r,s)\) satisfying
\[
V_i\ge0,\quad
V_i(t,r,s)\ge V_i(t,r-1,s),\quad
V_i(t,r,s)\ge V_i(t,r,s-1),
\]
\[
V_i(t,r,s)\ge g_i(t,r,s)+V_i(t+1,r,s)
\]
with the appropriate terminal condition dominates the optimal horn score by backward induction. An additional inequality bounding the central score plus the three initial \(V_i\) values by \(29/10\) would replace the corresponding dynamic-program search. A short piecewise polynomial formula would be an analytic advance; defining \(V_i\) as the existing dynamic program would not.

The arithmetic hypotheses cannot simply be dropped at low height. An archived abstract one-corner ideal has \(m=48,H=5,\sum|x|_1=170\), so \(D_0=40\) and \(m-D_0=8\). It fails the residue-derived corner and erosion restrictions and is not an Apéry counterexample. It demonstrates why a universal statement about arbitrary one-corner lower ideals is too strong.

The broader connection between Wilf's question and weighted monomial lower ideals already appears in [Hellus, Rechenauer and Waldi, “Variants on a question of Wilf”](https://arxiv.org/abs/1804.06141). The proposed centroid lemma is a specific target arising from our certificates, not a claim that the general strategy is new.

## 3. The arithmetic core in arbitrary embedding dimension

Write
\[
S=\langle m,a_1,\ldots,a_d\rangle,\qquad e=d+1,
\]
and let \(T\subset\mathbb N^d\) be its preferred Apéry lower ideal. Put
\[
M=\max_T a\cdot x,\qquad
D_d=dmM-(d+1)\sum_T a\cdot x.
\]
Then
\[
\boxed{mW_{d+1}=D_d-\frac{d-1}{2}m(m-1).}
\tag{4}
\]
Indeed, the genus is \(\sum_Ta\cdot x/m-(m-1)/2\); substitute \(c=M-m+1\) and \(W_e=e(c-g)-c\).

If a coordinate line has length \(L_\ell\) and top \(t_\ell\), summing arithmetic progressions gives
\[
D_d=\sum_{\ell\text{ in all }d\text{ directions}}
L_\ell(M-a\cdot t_\ell)\ge0.
\tag{5}
\]
With \(A=\min_i a_i\ge m+1\), (4), (5), and integrality yield
\[
\boxed{W_{d+1}<0\ \Longrightarrow\
\frac{d-1}{2}m-\frac{D_d}{A}\ge\frac{dm}{m+1}.}
\tag{6}
\]
For five generators, the quantity to bound is therefore
\[
\frac32m-\frac{D_4}{A},
\]
against \(4m/(m+1)\). No bound sufficient to settle it universally is proved here.

Residue-injectivity also proves, in every dimension:

- A minimal excluded point and its representative in \(T\) have disjoint support. Subtracting a common positive coordinate otherwise gives distinct equal-residue points inside \(T\).
- There is at most one full-support minimal excluded point: its representative must be zero, and two such exclusions would have equal-residue predecessors.
- For any nonempty coordinate set \(I\), let \(C_I\) consist of excluded points whose predecessor in every direction of \(I\) belongs to \(T\). If \(\pi_I\) deletes the coordinates in \(I\), then
  \[
  |C_I|\le|\pi_I T|.
  \]
  Their residue representatives lie in the complementary coordinate face and are distinct.
- For \(F_i=\{x\in T:x+e_i\notin T\}\),
  \[
  |F_i\cap F_j|\le2|\pi_{\{i,j\}}T|.
  \]
  A planar slice with \(h\) maxima has \(h-1\) mixed excluded corners. Summing this identity over slices and applying the preceding injection proves the bound.
- If \(E+B\subseteq T\), then \(|E-B|\le m\). Equal residues of \(x-b\) and \(x'-b'\) force equality of \(x+b'\) and \(x'+b\), both in \(T\). Taking \(B=\{0,e_1,\ldots,e_d\}\) gives the corresponding erosion inequality.

These are necessary conditions with proofs independent of the exhaustive four-generator certificates. They do not yet imply Wilf in all dimensions.

## 4. A general transfer principle and the archived finite reduction

The discrete-to-continuous transfer also generalizes. Suppose translated-grid samples of a structural class satisfy
\[
dR|T|-(d+1)\sum_T|x|_1\ge\lambda|T|
\]
for the degree allowances \(R\in\{N-d,\ldots,N\}\). For a downset \(K\) in the unit simplex, integration over grid offsets gives
\[
d-(d+1)\mathbb E_K|X|_1\ge\frac{\lambda-d/2}{N}.
\tag{7}
\]
The correction \(d/(2N)\) follows by integrating the fractional grid offset along initial coordinate intervals. The detailed proof is in the accompanying general-dimension note. A positive margin in the next dimension requires establishing its finite premise and handling the discrete phase correction; it is not supplied automatically by the four-generator case.

The earlier manuscript, “Wilf research continuation: finite reduction and new four-generator classes” (5 September), proposes a separate analytic theorem: for every fixed \(d\ge2\), sufficiently large multiplicity has strictly positive \(W_{d+1}\), and all possible exceptions have explicit finite generator bounds.

Its stated constants are
\[
\delta_d=\frac{d!}{8d}\left(\frac1{16d^2(d+1)}\right)^d,\quad
P_d=1+32d(d-1)(d+1)^2,\quad
H_d=\frac{(d-1)P_d}{\delta_d},\quad
B_d=\left\lceil\frac{(d+H_d)^d}{d!}\right\rceil.
\]
The proposed conclusion is \(m\ge B_d\Rightarrow W_{d+1}>0\), with every remaining counterexample satisfying
\[
d+2\le m<B_d,\qquad
a_i\le M\le
\frac{m(m-d)}2\big((d-1)(m-1)-2\big).
\tag{8}
\]
For five generators, \(B_4\) is approximately \(4.706\times10^{66}\). This is an explicit finite reduction under the archived analytic argument, not a practical exhaustive search and not a five-generator proof. That argument requires its own external review; the new centroid certificates do not validate it.

This exact eventual claim must be distinguished from the published asymptotic result that, for fixed embedding dimension \(e\) and every fixed \(\varepsilon>0\), \(n/c\ge1/e-\varepsilon\) outside a finite set. The latter allows violations approaching \(1/e\) and does not alone give finitely many exact Wilf counterexamples. See [Alex Zhai, “An asymptotic result concerning a question of Wilf”](https://arxiv.org/abs/1111.2779).

## 5. Why five generators require new geometry

The obstruction occurs in actual numerical semigroups, not only in abstract lower ideals.

First, take
\[
S=\langle9,12,15,19,20\rangle.
\]
In coordinate weights \((19,20,12,15)\), its Apéry ideal is
\[
T=\{0,e_1,e_2\}+\{0,e_3,e_4\}.
\]
Its nine labels are \(0,12,15,19,20,31,32,34,35\), with distinct residues modulo 9. Its minimal exclusions are
\[
2e_1,\ e_1+e_2,\ 2e_2,\ 2e_3,\ e_3+e_4,\ 2e_4.
\]
Each has a strict reduction by a positive multiple of 9; for example \(19+20=12+3\cdot9\). These reductions certify that the displayed set is exactly the Apéry ideal.

The positive-unit compatibility graph is \(K_{2,2}\), with edges \(13,14,23,24\): it contains a chordless four-cycle. It has no full-support excluded corner, but no decomposition into one central lower box and four coordinate horns of the previous form. Any central box corner uses at most two coordinates; some included pair then exceeds it in two directions, whereas a coordinate horn can exceed it in only one.

Second, take
\[
S=\langle14,21,29,30,32\rangle.
\]
In coordinate weights \((29,30,32,21)\), its Apéry ideal is
\[
T=\{0,1\}^4\setminus\big((1,1,1,0)+\mathbb N^4\big).
\]
Its pair projections are all complete Boolean squares, yet a support-three corner is excluded. Pair projections therefore do not determine membership even in the absence of a full-support excluded corner.

These examples satisfy Wilf, with \(W_5=18\) and \(65\), respectively. They refute only the proposed direct extension of the geometric classification. Their exact reductions and independent shortest-path checks are supplied in the accompanying note and script.

## 6. Recommended mathematical direction

For simplifying four generators, first pursue the centroid witness (1) from the arithmetic restrictions, using the small point configurations in the exact registry to identify symbolic sufficient conditions. Independently, seek a closed-form horn majorant satisfying the local inequalities in Section 2.

For higher dimensions, retain the residue injections and exact moment bridge (6), but work with geometry that permits compatibility cycles and exclusions supported on more than two coordinates. An extension that assumes a central box plus one horn per coordinate misses genuine five-generator Apéry ideals.

Neither analytic replacement has been completed here. The completed result of this investigation is the stronger all-weight centroid certificate theorem and the accompanying precise account of which methods generalize.

## 7. Evidence and reproduction

The accompanying archive is a supplement to the previous complete proof archive, not a replacement for its high-height certificates or earlier case proofs.

The portable command

~~~sh
python3 round9/height_free_duals/verify_complete_certificate.py
~~~

checks immutable hashes, compiles a separate C++17 verifier in a temporary directory, regenerates all finite shapes, checks every exact rational certificate, and compares all nine coverage records and multiplicity histograms. It requires Python standard library and a compiler supporting the integer extensions used by GCC/Clang. The observed portable run recorded:

~~~json
{
  "status": "passed",
  "full_independent_recomputation_this_run": true,
  "profiles": 1429,
  "bases": 6816,
  "exact_weighted_duals": 3742041,
  "floating_point_used": false
}
~~~

The actual JSON record nests the last four fields under its run summary. The verifier explicitly rejects the removed height-upper-bound column and consumes the complete assignment stream with no trailing bytes. Floating-point optimization is used only to propose candidate bases during generation; all acceptance and independent replay checks are exact.

The two five-generator examples are independently reproducible with

~~~sh
python3 round9/check_dimension_obstruction.py
~~~

The archived old-registry compression statistics and diagnostic sample results are descriptive. They are not substitutes for exhaustive coverage. The full old registry inputs remain in the previous proof archive; the new height-free certificate replay is self-contained in this supplement.
