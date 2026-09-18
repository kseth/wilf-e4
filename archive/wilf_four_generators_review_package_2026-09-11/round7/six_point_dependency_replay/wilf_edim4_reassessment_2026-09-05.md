# Reassessing the embedding-dimension-four approach to Wilf

**5 September 2026.** This note follows the supplied August research checkpoint and `wilf_edim4_progress_2026-09-05.md`.

**Assessment:** keep the Apéry staircase and its global moment identity. Use the restrictions on minimal excluded monomials much earlier. Treat final-window counting as a useful sufficient test and a source of partial theorems, rather than assuming that its successive cardinality cases will solve the unrestricted problem.

**Proved here:** a forbidden projection-grid lemma; an explicit finite reduction for the six-point final-window case, implying Wilf in that case for multiplicity greater than 512; and the impossibility of an entire family of misleading abstract staircases. A short global estimate also handles the double-staircase family already settled in the literature. These are mathematical arguments, with separate computational diagnostics.

**Not proved:** Wilf for every four-generated numerical semigroup; the complete six-point case; a universal geometric stability bound; or a finite multiplicity cutoff for the unrestricted four-generator problem. No claim of novelty or priority is made for the lemmas below.

## 1. What the checkpoints actually tell us

Write
\[
S=\langle m,a_1,a_2,a_3\rangle,\qquad m<a_1<a_2<a_3,
\]
with four minimal generators. Let \(c\) be the conductor, \(n=|S\cap[0,c)|\), and \(W=4n-c\).

Choose preferred factorizations of the Apéry set with a fixed monomial order. Their exponent vectors form a lower ideal \(T\subset\mathbb N^3\). The map
\[
w(x)=a\cdot x
\]
labels its \(m\) points bijectively modulo \(m\). Put
\[
M=\max_T w=c+m-1,\qquad \Sigma=\sum_Tw.
\]
The exact identity to retain is
\[
\boxed{mW=3mM-4\Sigma-m(m-1).} \tag{1}
\]
Equivalently, \(D=3mM-4\Sigma\) is the sum, over all coordinate lines, of their lengths times the deficit of their top label from \(M\).

The earlier note proved Wilf when
\[
Z=\{x\in T:M-w(x)<m\}
\]
has at most five points. That partial theorem remains useful. The reason to change priorities is that its sufficient count criterion can perform arbitrarily poorly on positive examples.

| Checkpoint component | Assessment |
|---|---|
| Exact Apéry, boundary, reflection, and carry identities | Retain. These preserve the target quantity. |
| The sufficient projection count \(\Phi\) | Retain as a filter and for bounded-cardinality results. Its negative value is not evidence against Wilf. |
| Increasing \(|Z|\) one case at a time | A viable partial-results program, but presently lacks a mechanism covering unbounded \(|Z|\). |
| Requiring the stronger modular inequality for every cyclic cut | Useful diagnostic. It asks more than the actual semigroup inequality and removes information in the integer lifts of the generators. |
| Repairing the unrestricted conflict LP with more generic cuts | Low priority. The checkpoint already has an unbounded raw integrality gap and higher-denominator obstructions. |
| Cyclic-inflation descent | Retain as preprocessing. It is an exact reduction on genuine semigroups. |

For the family
\[
S_s=\langle s^2,s^2+1,s^2+s,s^2+s+1\rangle\quad(s\ge2),
\]
the checkpoint quantities are
\[
|Z|=2s-1,\quad \Phi=-(s-1)(s-2),\quad
W=\frac{s(s-1)(s-2)}3.
\]
Thus the count test deteriorates while the actual Wilf number grows. This is a loss in the estimate, not a difficult family for Wilf itself.

## 2. Literature that changes the choice of approach

This is a targeted primary-source review, not a claim to have checked every unpublished manuscript.

| Source | Relevant contribution and limitation |
|---|---|
| Zhai, *An asymptotic result concerning a question of Wilf*, [arXiv:1111.2779](https://arxiv.org/pdf/1111.2779), especially the concluding remarks | Identifies the equal-weight simplex as the equality configuration in the lower-ideal estimate and suggests studying quantitative departure from it. This supports a global deficit approach, but does not supply the needed exact correction. |
| Hellus–Rechenauer–Waldi, *Variants on a question of Wilf*, [arXiv:1804.06141](https://arxiv.org/pdf/1804.06141), Proposition 2.6 and Remark 2.9 | Gives the lattice restriction on minimal excluded monomials used below. It also already settles semigroups with the double-staircase shape. |
| Chomicz, *On numerical semigroups with embedding dimension four*, [arXiv:2604.25653v1](https://arxiv.org/html/2604.25653v1) | Develops Apéry computations from generator relations. This is relevant to retaining actual boundary relations. Its family calculations also caution against assuming a uniformly bounded number of presentation relations. |
| Bruns–García-Sánchez–O'Neill–Wilburne, *Wilf's conjecture in fixed multiplicity*, [author-hosted paper](https://www.home.uni-osnabrueck.de/wbruns/brunsw/pdf-article/S021819672050023X-1.pdf), Section 4 | Uses exact polyhedral and integer-feasibility formulations. It is a sound model for checking a fixed structural class, rather than relying on a relaxation of arbitrary residue selections. It does not bound multiplicity for our unrestricted problem. |
| Marashdeh, *An upper bound for the type of a numerical semigroup, and a reduction of Wilf's conjecture*, [arXiv:2608.12531v1](https://arxiv.org/html/2608.12531v1), discussion after Theorem 1.2 | The author explicitly distinguishes the new overlap bound from what Wilf needs: a factor of \(n\) is still missing. This does not remove our obstruction simply by changing to a type/overlap formulation. |
| Chatterjee–Narula, *A note on Wilf's Conjecture*, [publisher abstract](https://link.springer.com/article/10.1007/s00233-026-10640-8), published 22 May 2026 | Improves a result formulated for fixed \(\lceil m/e\rceil\), with an arithmetic hypothesis. Fixing \(e=4\) leaves that ratio unbounded, so this should not be read as a solution of the four-generator case. Only the publisher abstract was reviewed here. |

The sources examined do not provide a proof of the unrestricted embedding-dimension-four case. The preference for the combined boundary/moment route below is our assessment, not a theorem that it must succeed.

## 3. The boundary restriction should be used before relaxation

Let \(C\) be the set of coordinatewise minimal elements of \(\mathbb N^3\setminus T\). For \(p\in C\), let \(q(p)\in T\) be the representative of its residue.

### 3.1 Disjoint supports

\[
\boxed{\operatorname{supp}(p)\cap\operatorname{supp}(q(p))=\varnothing.} \tag{2}
\]

Indeed, if both have a positive \(i\)-th coordinate, then \(p-e_i\) and \(q(p)-e_i\) are in \(T\) and have the same residue. Injectivity forces \(p=q(p)\), a contradiction.

Likewise, two distinct members of \(C\) whose supports intersect cannot have the same residue: subtract a shared coordinate vector from both.

It follows that there is at most one member of \(C\) with all three coordinates positive. If it exists, its residue is zero. This recovers the relevant consequence of HRW Proposition 2.6 directly.

In three variables, a corner supported on two coordinates has its residue representative on the remaining axis. Consequently its actual reduction relation has the form
\[
\alpha a_i+\beta a_j=\gamma a_k+\kappa m,
\qquad \gamma,\kappa\ge0. \tag{3}
\]
The nonnegative integer \(\kappa\) is useful information, not merely a congruence to discard. Zero is possible when there is a factorization tie.

If an interior corner exists, the representatives of the two-coordinate corners are nonzero. For a fixed coordinate plane these representatives are distinct. Thus, if the remaining axis has \(t\) nonzero points of \(T\), that plane has at most \(t\) such corners. Equality gives a permutation of the entire nonzero axis, and therefore a useful sum congruence.

### 3.2 An exact height description

Define
\[
F=\{(i,j):(i,j,0)\in T\},\qquad
h(i,j)=\#\{k:(i,j,k)\in T\},
\]
and set \(P_i=h(i,0)\), \(Q_j=h(0,j)\).

If there is no interior corner, then
\[
\boxed{h(i,j)=\min(P_i,Q_j)\quad((i,j)\in F).} \tag{4}
\]
If the unique interior corner is \((\alpha,\beta,\gamma)\), then
\[
\boxed{h(i,j)=
\begin{cases}
\min(P_i,Q_j,\gamma),&i\ge\alpha,\ j\ge\beta,\\
\min(P_i,Q_j),&\text{otherwise}.
\end{cases}} \tag{5}
\]

Proof: every excluded point dominates a minimal excluded point. Exclusions supported on at most two coordinates are determined by the three coordinate-plane sections. Any remaining exclusion must dominate the unique interior corner. This proves both formulas.

In particular, horizontal slices are intersections of a fixed planar lower ideal with nested rectangles. At height \(\gamma\), if present, the planar lower ideal changes once, by removing its upper-right quadrant starting at \((\alpha,\beta)\).

This description retains every layer and makes no assumption that a generator residue equals one. The planar boundary sequences can still have unbounded complexity; it is not a finite classification by itself.

The moments become
\[
m=\sum_F h(i,j),
\]
\[
\Sigma=\sum_F\left[h(i,j)(a_1i+a_2j)+a_3\binom{h(i,j)}2\right], \tag{6}
\]
\[
M=\max_F\bigl(a_1i+a_2j+a_3(h(i,j)-1)\bigr).
\]
Equations (3)–(6) are the proposed working representation.

## 4. Removing the six-point compression obstruction

### 4.1 A forbidden projection grid

**Lemma.** The coordinatewise maximal points of a lower ideal with at most one interior minimal excluded point cannot contain six points
\[
(x_i,y_j,z_{ij}),\qquad i\in\{0,1\},\ j\in\{0,1,2\},
\]
where \(x_0<x_1\) and \(y_0<y_1<y_2\). The same holds for every permutation of the coordinates.

**Proof.** Maximality makes the six points an antichain, so the \(z_{ij}\) strictly decrease along either increasing row or column coordinate. At \((x_1,y_1)\),
\[
P_{x_1}\ge z_{10}+1>z_{11}+1,
\qquad Q_{y_1}\ge z_{01}+1>z_{11}+1.
\]
Since the column height is exactly \(z_{11}+1\), formula (5) forces the interior cap to be active and gives \(\gamma=z_{11}+1\). Applying the same argument at \((x_1,y_2)\) gives \(\gamma=z_{12}+1\). This contradicts \(z_{11}>z_{12}\). If no interior corner exists, the first strict inequality already contradicts (4). ∎

Thus the bipartite incidence graph of any two-coordinate projection of the maximal points contains no complete \(2\times3\) grid. This is a statement about equality and order of coordinate levels, so it survives arbitrary strictly increasing relabeling of those levels.

This last observation matters: an impossible compressed shape need not generally stay impossible after stretching. Here the specific reason for impossibility does stay invariant.

### 4.2 Strict gain under insertion is restored for six points

Recall the earlier notation
\[
B(T)=\sum_{j=1}^3|\pi_jT|,
\quad E(Z)=\sum_{z\in Z}|z|_1-\sum_j\max_Z z_j,
\]
\[
\Phi(T,Z)=B(T)-3|Z|-E(Z).
\]
The audited sufficient estimate is
\[
mW\ge m\Phi(T,Z)+E(Z). \tag{7}
\]

For \(U(Z)=\bigcup_{z\in Z}[0,z]\), inserting one coordinate level moves a subset \(H\subseteq Z\). If \(b=|H|\), and \(p,q\) are the other-coordinate maxima on \(H\), then
\[
\Delta\Phi(U(Z),Z)=p+q+3-b. \tag{8}
\]
For \(b\le5\) this is at least one. With \(|Z|=6\), the only additional possibility for a nonpositive increment is
\[
b=6,\quad (p,q)=(1,2)\text{ or }(2,1).
\]
Indeed, the projection of an antichain is injective, so \(b\le(p+1)(q+1)\). In the displayed case, all six cells of the corresponding rectangle must occur. The grid lemma excludes it.

Rank compression preserves the forbidden-grid property. Every step in reconstructing a genuine six-point \(Z\) from its compressed version therefore increases \(\Phi(U(Z),Z)\) by at least one.

### 4.3 An explicit multiplicity bound

**Theorem.** If \(|Z|=6\) and \(\Phi(T,Z)<0\), then \(m=|T|\le512\). Consequently,
\[
\boxed{|Z|=6\text{ and }m>512\quad\Longrightarrow\quad W\ge0.} \tag{9}
\]

**Proof.** In one coordinate column of a rank-compressed six-point set, the sum of entries minus their maximum is at most 10. To see this, if the occurring levels are \(0,\ldots,r\), put the remaining \(5-r\) entries at \(r\). The resulting upper bound is
\[
\frac{r(r+1)}2+(5-r)r-r\le10\qquad(0\le r\le5).
\]
Hence the compressed \(E\) is at most 30. Each projection contains the six distinct projected points of \(Z\), so \(B(U(Z))\ge18\). Thus its compressed score is at least \(-30\).

If the final \(\Phi(T,Z)\) is negative, so is \(\Phi(U(Z),Z)\), by projection monotonicity. Strict gain under every insertion now allows at most 29 insertions. Each insertion changes \(E\) by \(b-1\le5\). Therefore the final \(E\) is at most
\[
30+5\cdot29=175.
\]
Negativity of \(\Phi(T,Z)=B(T)-18-E(Z)\) gives \(B(T)\le192\). The finite Loomis–Whitney inequality and arithmetic–geometric mean give
\[
|T|^2\le|\pi_1T|\,|\pi_2T|\,|\pi_3T|
\le\left(\frac{192}{3}\right)^3=512^2.
\]
This proves the bound. For \(m>512\), (7) proves Wilf. ∎

The proof is independent of the compressed-shape enumeration files. The number 512 is deliberately coarse. The earlier six-point computation listed 2,264 negative compressed seeds, of which 2,253 pass the grid exclusion; these counts are diagnostics, not inputs to (9).

The complete six-point theorem still requires checking the remaining shapes and their arithmetic realizations. A finite list of shapes does not by itself bound the generators; Section 7 explains how to retain their unbounded integer lifts exactly.

## 5. Two other obstructions can be disposed of rigorously

### 5.1 The old 68-point shape is excluded before modular optimization

The checkpoint's shape
\[
T_{\rm bad}=\{x:|x|\le4\}\cup\{x:|x|\in\{5,6\},\ x_1x_2x_3=0\}
\]
has six interior minimal excluded points:
\[
(1,1,3),(1,2,2),(1,3,1),(2,1,2),(2,2,1),(3,1,1).
\]
It violates (2) and its consequences. Its failure of a broad geometric inequality remains a valid counterexample to that broad inequality, but it cannot obstruct a theorem restricted to genuine Apéry staircases.

### 5.2 Even one interior corner is not enough: a whole impossible family

Consider the three-face staircase
\[
T_d=\{(x,y,z)\in\mathbb N^3:x+y+z\le d,\ xyz=0\},\quad d\ge2.
\]
It has
\[
m=1+\frac{3d(d+1)}2
\]
points and exactly one interior minimal excluded point, \((1,1,1)\).

**Proposition.** No \(T_d\), \(d\ge2\), admits a linear residue bijection modulo \(|T_d|\).

**Proof.** Suppose its axis labels are \(A,B,C\) modulo \(m\). The interior corner gives
\[
A+B+C\equiv0\pmod m.
\]
The \(d\) minimal excluded points
\[
(i,d+1-i,0),\qquad 1\le i\le d,
\]
have distinct residues, by the shared-support argument. Their representatives lie on the third axis, and cannot be zero because their supports intersect that of the interior corner. They therefore permute \(C,2C,\ldots,dC\).

Set \(N=d(d+1)/2\). Summing these residues gives
\[
N(A+B)\equiv NC\pmod m,
\]
so \(2NC\equiv0\). Multiplying by three and using \(6N=2m-2\) yields \(2C\equiv0\). But \(0\) and \((0,0,2)\) are distinct points of \(T_d\). This contradicts injectivity. ∎

This proof illustrates a concrete mechanism to explore: when a plane's corner representatives exhaust an axis, sum the forced permutation and combine it with other boundary relations. It eliminates infinitely many false candidates at once.

For an explicit warning against using geometry alone, take \(T_3\) with weights \((30,32,33)\). Here
\[
m=19,\quad M=99,\quad\Sigma=1330,\quad D=323<342=m(m-1).
\]
The formal expression (1) gives \(W=-1\), and even \(30+32+33\equiv0\pmod{19}\) holds. Nevertheless, \(3\cdot30\equiv33\pmod{19}\), so two points of the proposed staircase collide. The genuine semigroup \(\langle19,30,32,33\rangle\) has \(W=69\).

## 6. A global estimate handles the double staircase uniformly

Let
\[
B_s=\{(x,y,z):x+y+z\le s-1,\ xy=0\},\quad s\ge2.
\]
For any genuine four-generator Apéry labeling of this shape, we obtain
\[
\boxed{W\ge\frac{(s-1)(s-2)(s-3)}3\ge0.} \tag{10}
\]

Here is the calculation. The size is \(m=s^2\), and the coordinate sums are \((P,P,Q)\), where
\[
P=\frac{s(s-1)(s+1)}6,\qquad
Q=\frac{s(s-1)(2s-1)}6\ge P.
\]
If \(v\) is the largest generator weight, then \(M=(s-1)v\). The three weights are distinct integers, so rearrangement gives
\[
\Sigma\le P(v-2)+P(v-1)+Qv=(2P+Q)v-3P.
\]
Consequently
\[
D\ge\frac{s(s-1)(s-2)}3v+12P.
\]
Since \(v\ge m+3=s^2+3\), subtraction of \(m(m-1)\) gives
\[
D-m(m-1)\ge\frac{s^2(s-1)(s-2)(s-3)}3,
\]
which proves (10).

HRW Remark 2.9 already proves Wilf for this shape class. The point of this reconstructed estimate is methodological: its single formula handles unbounded final-window size and retains the distinct integer weights that the count relaxation loses.

## 7. A concrete replacement for the unrestricted conflict LP

### 7.1 Fast sufficient certificates from moments

For a fixed shape \(T\), let \(s_T=\sum_{x\in T}x\) and define
\[
\eta(T)=\min_{u_1,u_2,u_3\ge1}
\left(3m\max_{x\in T}u\cdot x-4u\cdot s_T\right).
\]
Then \(D\ge(m+1)\eta(T)\). Thus
\[
(m+1)\eta(T)\ge m(m-1)
\]
is a sufficient shape certificate. This is a four-variable linear program after introducing the maximum as a variable.

A better version uses the actual generator order and minimizes \(D\) under
\[
a_1\ge m+1,\quad a_2-a_1\ge1,\quad a_3-a_2\ge1,
\quad M\ge a\cdot x\ (x\in T).
\]
Positive lower bounds can be certified by rational LP duals. They prove Wilf for every realization covered by the constraints, including arbitrarily large generators.

Failure of such a certificate is not a counterexample. Even the genuine shape of \(\langle5,6,8,9\rangle\),
\[
\{0,e_1,2e_1,e_2,e_3\},
\]
has ordered-LP minimum \(D=16<20\), attained at fictitious weights \((6,11,12)\). Those weights collide on the proposed shape. Thus even knowing that a shape is realizable does not justify arbitrary new weights on it.

### 7.2 Exact conditions for a fixed shape and residue vector

Fix a lower ideal \(T\) of size \(m\) containing \(0,e_1,e_2,e_3\), and a residue vector \(A\in\{1,\ldots,m-1\}^3\) that is bijective on \(T\). Write
\[
a_j=A_j+m q_j,\qquad q_j\in\mathbb Z_{\ge1}.
\]
Use lexicographic tie-breaking. For each minimal excluded \(p\), let \(r(p)\in T\) be its residue representative. Then the preferred-Apéry condition is exactly
\[
a\cdot(p-r(p))\ge
\begin{cases}
0,&r(p)<_{\rm lex}p,\\
m,&r(p)>_{\rm lex}p.
\end{cases} \tag{11}
\]

Necessity follows from minimality of Apéry representatives and the tie rule. For sufficiency, replace any occurrence of a corner \(p\) in an exponent vector by \(r(p)\). The residue is unchanged and the pair consisting of weight and lexicographic order strictly decreases. Translation preserves this decrease, and positive integer weights make reduction terminate. Its endpoint lies in \(T\). Residue bijectivity makes the endpoint unique, and its weight is no larger than the starting weight. It is therefore the least semigroup representative of that residue, with the required tie rule.

For each possible maximal-label point \(z\in T\), append \(a\cdot z\ge a\cdot x\) for all \(x\in T\) and
\[
m(3a\cdot z-m+1)-4a\cdot s_T\le-m. \tag{12}
\]
The remaining question is integer feasibility in the **three** variables \(q_1,q_2,q_3\), with generator-order constraints if desired. Equations (11)–(12) retain the actual integer lifts. They do not ask for every arbitrary cyclic cut to work. The Apéry characterization itself also allows redundant generating sets; minimality of the four proposed generators is a separate check when identifying an embedding-dimension-four semigroup.

This is a finite exact test for a fixed \((T,A)\), even though the generators are unbounded. It provides a principled arithmetic completion of the six-point finite reduction. It does not bound how many shapes must be treated for unrestricted \(|Z|\).

## 8. What was checked computationally

The mathematical proofs above do not rely on random sampling. The accompanying programs check formulas and expose weaknesses of proposed relaxations.

- Exact Apéry computations verified the double-staircase formulas for \(2\le s\le30\), including the negative \(\Phi\) values and positive \(W\).
- The three-face formulas and corner descriptions were checked for \(2\le d\le16\). Independent bounded residue enumeration at \(d=2,3,4\) found no feasible labels, consistent with the all-\(d\) proof.
- The 68-point and 19-point false obstructions were reproduced exactly.
- The six-point bound's constants \(10,30,29,175,192,512\) were checked separately; the proof of the unbounded statement is Section 4.
- A seeded sample of 500 generator proposals yielded 453 minimally four-generated semigroups. The height reconstruction, sparse boundary relations, and absence of projected grids were checked directly. Both geometric certificate versions passed these 453 examples.
- A separate exhaustive bounded diagnostic over \(20\le m\le40\), \(m<a_1<a_2<a_3<2m\), found 82,036 numerical semigroups and 29,633 distinct preferred shapes. The ordered geometric certificate passed every shape. Every LP optimum used in that diagnostic was checked by exact rational primal and dual arithmetic.
- The last observation does **not** imply that all larger shapes pass, that all generator ranges pass, or that there is a finite universal geometric cutoff. The small genuine-shape failure in Section 7 is retained explicitly to prevent overinterpreting the pass rate.

## 9. Recommended research priorities

1. Use the projected-grid restriction to finish a targeted six-point classification, with (11)–(12) available when the stronger all-cuts test fails. The explicit bound (9) makes this a finite structural problem.
2. For the unrestricted case, seek inequalities for the height representation (4)–(6), supplemented by the sparse corner relations (3). Use global moment certificates to handle large parameter families at once.
3. Treat geometrically failing shapes as candidates for arithmetic exclusion. The saturated axis-permutation argument in Section 5 is a demonstrated example of such an exclusion, not a promise that all failures have that form.
4. Seek a quantitative stability or descent theorem that reduces the unrestricted set of remaining shapes. No such theorem has been proved here. Merely observing that a finite collection of LPs passes would leave this central gap untouched.

The useful change is to exploit what makes an Apéry staircase realizable before attempting a universal inequality on its relaxed geometry. The six-point grid obstruction is removed by precisely this change, while the unrestricted problem remains open in this work.
