# Wilf's conjecture in embedding dimension four: a proved extension and the remaining gap

**Date:** 5 September 2026  
**Starting point:** `wilf_edim4_research_state_2026-08-15(2).md`, supplied by Karthik Sethuraman.

**Outcome:** This work does **not** prove or disprove Wilf's conjecture for all numerical semigroups of embedding dimension four. It establishes a computer-assisted partial theorem extending the supplied document's final-window result from at most two elements to at most five. The finite verification is supplied as reproducible Python code. No claim of priority in the literature or independent peer review is made.

## 1. The result

Let
\[
S=\langle m,a_1,a_2,a_3\rangle
\]
be minimally four-generated, with multiplicity \(m\), conductor \(c\), and
\[
n=|S\cap[0,c)|,\qquad W=4n-c.
\]

**Theorem, with a finite computer-assisted part.** If
\[
\boxed{\bigl|\operatorname{Ap}(S,m)\cap[c,c+m)\bigr|\le5,}
\]
then \(W\ge0\).

There is no bound on the generators, multiplicity, conductor, or genus in this statement. The final-window cardinality is an invariant of the Apéry set; it does not depend on a choice of preferred factorizations.

The proof has four parts:

1. Re-derive the supplied exact boundary and reflection identities.
2. Obtain a sufficient inequality involving only coordinate projections and the final-window points.
3. Prove that, for at most five points, every failure of that sufficient inequality reduces to a finite list by coordinate compression and controlled expansion.
4. Exhaustively check residue completeness on that list. The surviving five pairs of shapes all satisfy the modular boundary inequality for every possible cut.

The three-point result has an 18-case classification printed below. The four- and five-point extensions use the supplied finite verifier.

## 2. Literature check and scope

The primary sources checked during this session did not supply a solution of the unrestricted embedding-dimension-four case.

- Marashdeh's 12 August 2026 preprint explicitly states that its new bounds do not prove Wilf or settle cases beyond the classical type bound; see the discussion following Theorem 1.2: [arXiv:2608.12531v1](https://arxiv.org/html/2608.12531v1).
- Chomicz's April 2026 paper develops a procedure for computing four-generated Apéry sets and applies it to particular families: [arXiv:2604.25653v1](https://arxiv.org/html/2604.25653v1). It is not a general proof of Wilf.
- Bacher's paper was revised after the supplied handoff: version 7 is dated 27 August 2026. Its abstract reports verification through conductor 200: [arXiv:2604.25051v7](https://arxiv.org/abs/2604.25051v7).
- The lattice restriction used in Section 9 is Proposition 2.6 of Hellus, Rechenauer, and Waldi, *Variants on a question of Wilf*: [arXiv:1804.06141](https://arxiv.org/pdf/1804.06141). A short proof is included here.

This is a dated, targeted check, not an exhaustive claim about every unpublished manuscript. None of the new finite classification below depends on a published fixed-multiplicity verification.

## 3. Audited exact identities

### 3.1 Preferred factorizations

Choose the least factorization of each Apéry element using \(a_1,a_2,a_3\), with a fixed monomial order to break ties. Let \(T\subset\mathbb N^3\) be the resulting exponent vectors, and write
\[
w(x)=a_1x_1+a_2x_2+a_3x_3.
\]

Then \(T\) is a finite lower ideal, \(|T|=m\), and the labels \(w(x)\) give exactly one representative of each residue modulo \(m\). In particular \(0,e_1,e_2,e_3\in T\).

For completeness, if \(y\le x\in T\), an expression showing that \(w(y)-m\in S\) would also show \(w(x)-m\in S\). Thus \(w(y)\) is Apéry. Replacing \(y\) by a smaller preferred factorization inside \(x\) contradicts the multiplicative monomial order. This proves downward closure.

Put
\[
M=\max_{x\in T}w(x),\qquad \Sigma=\sum_{x\in T}w(x).
\]
The Apéry formulas give
\[
M=c+m-1,\qquad g=\frac{\Sigma}{m}-\frac{m-1}{2},
\]
and hence
\[
\boxed{mW=m(3M-m+1)-4\Sigma.} \tag{1}
\]

### 3.2 Coordinate boundary

Partition \(T\) into coordinate lines. A line \(\ell\) in direction \(j\) has length \(L_\ell\) and top \(t_\ell\). Along it,
\[
L_\ell w(t_\ell)=\sum_{x\in\ell}w(x)+a_j\binom{L_\ell}{2}.
\]
Since \(\sum_{\ell\parallel e_j}\binom{L_\ell}{2}=\sum_{x\in T}x_j\),
\[
D:=\sum_{j,\ell\parallel e_j}L_\ell(M-w(t_\ell))
=3mM-4\Sigma.
\]
Consequently,
\[
\boxed{D=mW+m(m-1).} \tag{2}
\]

### 3.3 Reflection and carries

Define
\[
q_j(x)=\left\lfloor\frac{a_jx_j}{m}\right\rfloor,
\quad \alpha_j(x)=[a_jx_j]_m,
\quad \lambda(x)=\left\lfloor\frac{\alpha_1(x)+\alpha_2(x)+\alpha_3(x)}m\right\rfloor,
\]
and \(\Lambda=\sum_x\lambda(x)\). Here \([u]_m\) is the representative in \(\{0,\ldots,m-1\}\).

Let \(b(x)=\lfloor(M-w(x))/m\rfloor\). Counting left elements by residue gives
\[
n=\sum_x b(x),\qquad
g=\sum_{x,j}q_j(x)+\Lambda.
\]
If \(\rho_j\) reflects a point within its coordinate line, set
\[
\gamma_j(x)=b(\rho_jx)-q_j(x).
\]
Because \(w(\rho_jx)=w(t_\ell)-a_jx_j\), we have \(\gamma_j(x)\ge0\). Reflection permutes each line, so
\[
\boxed{W=\sum_{x,j}\gamma_j(x)-\Lambda.} \tag{3}
\]

Write
\[
M-w(t_\ell)=mh_\ell+\beta_\ell,\qquad 0\le\beta_\ell<m,
\]
and, for \(A_j=[a_j]_m\), define
\[
R_A(L)=\sum_{k=0}^{L-1}[kA]_m,
\quad C_A(L,\beta)=\#\{0\le k<L:[kA]_m+\beta\ge m\}.
\]
The reflection sum on a line is \(Lh+C_A(L,\beta)\). Residue completeness gives
\[
m\Lambda=\sum_{x,j}\alpha_j(x)-\binom m2.
\]
Combining these equalities proves
\[
\boxed{mW=\binom m2+\sum_{j,\ell\parallel e_j}s_\ell,}
\qquad
s_\ell=mL_\ell h_\ell+mC_{A_j}(L_\ell,\beta_\ell)-R_{A_j}(L_\ell). \tag{4}
\]

These are algebraic derivations, not conclusions inferred from random testing. The test program separately checks them against exact Apéry computations.

## 4. From the exact identity to a projection criterion

Define the final-window points
\[
Z=\{x\in T:M-w(x)<m\},\qquad k=|Z|.
\]
Their labels are exactly \(\operatorname{Ap}(S,m)\cap[c,c+m)\). Every point of \(Z\) is maximal in \(T\): a successor would increase its label by \(a_j>m\), exceeding \(M\).

Call a line **deep** if its top is outside \(Z\). Its \(h_\ell\ge1\). The residues of its axis prefix are distinct, include zero, and therefore satisfy
\[
R_A(L)\le\frac{(L-1)(2m-L)}2.
\]
It follows that
\[
\boxed{s_\ell\ge m+\binom{L_\ell}{2}\ge m\quad\text{on every deep line}.} \tag{5}
\]

For \(1\le r\le\max_{z\in Z}z_j\), put
\[
u_{j,r}=[ra_j]_m,\qquad
z_{j,r}=\#\{z\in Z:z_j\ge r\},
\]
\[
c_{j,r}=\#\{z\in Z:z_j\ge r,\ M-w(z)+u_{j,r}\ge m\}.
\]
All these used nonzero axis residues are distinct. Let \(B_{\rm off}\) be the sum of nonzero residues not used by these prefixes, and define
\[
\Delta_Z=\sum_{j=1}^3\sum_{r=1}^{\max_{z\in Z}z_j}
\bigl((z_{j,r}-1)u_{j,r}-mc_{j,r}\bigr).
\]
**Indexing clarification:** this sum is over used prefix levels only. Extending the term \(z_{j,r}-1\) to all positive integers would be incorrect.

Paying one copy of each used axis residue out of \(\binom m2\) in (4) yields
\[
\boxed{mW=B_{\rm off}+\sum_{\ell\text{ deep}}s_\ell-\Delta_Z.} \tag{6}
\]

Let \(\pi_j\) delete coordinate \(j\), and set
\[
B(T)=\sum_{j=1}^3|\pi_j(T)|,
\]
\[
E(Z)=\sum_{z\in Z}|z|_1-\sum_{j=1}^3\max_{z\in Z}z_j.
\]
The number of deep lines is \(d_Z=B(T)-3k\): every final-window point tops precisely three lines, distinct in each direction. Also
\[
E(Z)=\sum_{j,r}(z_{j,r}-1),\qquad
\Delta_Z\le(m-1)E(Z).
\]
Define
\[
\boxed{\Phi(T,Z)=B(T)-3k-E(Z)=d_Z-E(Z).}
\]
Equations (5) and (6) give the useful sufficient bound
\[
\boxed{mW\ge m\Phi(T,Z)+E(Z).} \tag{7}
\]
In particular \(\Phi(T,Z)\ge0\) proves Wilf.

This criterion retains only the number of repeated prefixes and deep lines. It is sufficient, not necessary.

## 5. Coordinate compression: the finite-reduction theorem

For any finite antichain \(Z\subset\mathbb N^3\), write
\[
U(Z)=\bigcup_{z\in Z}\{x:0\le x\le z\},\qquad
\Phi_0(Z)=\Phi(U(Z),Z).
\]
Every \(T\) containing \(Z\) as maximal points contains \(U(Z)\), and projections are monotone. Thus
\[
\Phi(T,Z)\ge\Phi_0(Z). \tag{8}
\]

### 5.1 Exact change under insertion of a coordinate level

Choose direction \(i\) and threshold \(h\) at an occurring coordinate value. Increase coordinate \(i\) by one for every point of
\[
H=\{z\in Z:z_i\ge h\}.
\]
Let \(b=|H|\), and let \(p,q\) be the maxima of the other two coordinates on \(H\).

The projection which deletes coordinate \(i\) is unchanged. The two other projections gain \(p+1\) and \(q+1\) points. The sum of all coordinates increases by \(b\), and the sum of coordinate maxima increases by one. Therefore
\[
\boxed{\Delta\Phi_0=p+q+3-b.} \tag{9}
\]

Because \(Z\) is an antichain, its projection to the other two coordinates is injective. Otherwise two points would differ only in coordinate \(i\), making them comparable. Consequently
\[
b\le(p+1)(q+1).
\]
For \(1\le b\le5\), this gives:

| \(b\) | Minimum possible \(p+q\) | Lower bound on \(\Delta\Phi_0\) |
|---:|---:|---:|
| 1 | 0 | 2 |
| 2 | 1 | 2 |
| 3 | 2 | 2 |
| 4 | 2 | 1 |
| 5 | 3 | 1 |

Thus **every coordinate-level insertion strictly increases \(\Phi_0\) when \(|Z|\le5\)**.

### 5.2 Compression and exhaustive reconstruction

In each coordinate, replace the smallest occurring value by zero and replace successive distinct values by successive integers. This preserves all coordinate comparisons and hence the antichain property. A compressed \(k\)-point antichain lies in \(\{0,\ldots,k-1\}^3\), with each coordinate using an initial interval of integers.

Every original antichain is recovered from its compressed version by the level insertions just described, including insertions below the minimum to recover translations.

If \(\Phi_0(Z)<0\), its compressed version also has negative score. Along its reconstruction every intermediate score is negative, since the score strictly increases. Starting from all compressed negative antichains, retain only insertions whose new score is negative. This procedure finds **every** negative antichain for \(k\le5\) and terminates.

For example, the minimum compressed score for \(k=5\) is \(-5\). There can be at most four insertions along a negative reconstruction. This is an a priori bound on the computation, not a search cutoff chosen from observed examples.

### 5.3 Exhausting all possible larger ideals

For each resulting \(Z\), start with \(U(Z)\) and add one point at a time subject to:

- all immediate predecessors are already present;
- the added point does not dominate any point of \(Z\);
- the resulting \(\Phi(T,Z)\) remains negative.

Every finite lower ideal containing \(U(Z)\) and retaining \(Z\) as maximal points can be reached by such successive additions. Along any path to a negative final ideal, projection monotonicity ensures that every intermediate ideal also has negative score.

There are only finitely many such ideals: \(B(T)<3k+E(Z)\) bounds all projection cardinalities, hence all coordinate extents. Thus this second enumeration is exhaustive and finite as well.

Together, Sections 5.1–5.3 reduce the theorem to a finite check of explicitly generated objects. They are the reason the computation below proves an infinite class rather than merely testing bounded generators.

## 6. The complete three-point classification

Up to permutation of the three coordinates, there are 18 compressed antichains with three points. The table lists \(\Phi_0\):

| Compressed antichain | \(\Phi_0\) |
|---|---:|
| \((0,0,1),(0,1,0),(1,0,0)\) | 0 |
| \((0,0,1),(0,2,0),(1,1,0)\) | 2 |
| \((0,0,1),(1,2,0),(2,1,0)\) | 5 |
| \((0,0,2),(0,1,1),(0,2,0)\) | 1 |
| \((0,0,2),(0,1,1),(1,1,0)\) | 2 |
| \((0,0,2),(0,1,1),(1,2,0)\) | 5 |
| \((0,0,2),(0,2,0),(1,1,1)\) | 5 |
| \((0,0,2),(0,2,1),(1,1,0)\) | 5 |
| \((0,0,2),(1,1,1),(1,2,0)\) | 5 |
| \((0,0,2),(1,1,1),(2,2,0)\) | 9 |
| \((0,0,2),(1,2,0),(2,1,1)\) | 9 |
| \((0,1,1),(1,0,1),(1,1,0)\) | 0 |
| \((0,1,1),(1,0,1),(1,2,0)\) | 3 |
| \((0,1,1),(1,0,1),(2,2,0)\) | 7 |
| \((0,1,1),(1,0,2),(1,2,0)\) | 6 |
| \((0,1,1),(1,0,2),(2,1,0)\) | 6 |
| \((0,1,1),(1,0,2),(2,2,0)\) | 10 |
| \((0,1,2),(1,2,0),(2,0,1)\) | 9 |

All scores are nonnegative. Equations (8) and (9) extend this to arbitrary coordinates and larger ideals, and (7) proves \(W\ge0\).

The exhaustive generation rule is simple: each coordinate column is a surjection from three labeled points onto \(\{0,\ldots,r\}\), with \(r<3\); discard comparable rows and identify coordinate permutations. The verifier implements the same rule for \(k=1,\ldots,5\).

For one or two points, the same enumeration has respectively one or two compressed configurations, all with nonnegative score. Thus the present proof also independently covers the supplied handoff's smaller cases.

## 7. Four and five points: finite arithmetic completion

### 7.1 Enumeration ledger

All calculations below use integers and finite sets. No numerical optimizer or floating-point tolerance is involved.

| \(k\) | Compressed antichains up to coordinate permutation | Negative compressed antichains | Negative antichains after all insertions | Negative \((T,Z)\) pairs after all extensions | Largest \(|T|\) among these pairs |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 0 | 0 | 0 | — |
| 2 | 2 | 0 | 0 | 0 | — |
| 3 | 18 | 0 | 0 | 0 | — |
| 4 | 287 | 1 | 2 | 2 | 12 |
| 5 | 8,340 | 58 | 131 | 198 | 38 |

The last enumeration fixes a canonical representative of \(Z\) and enumerates its ideal extensions; it need not identify extensions related by a symmetry that fixes \(Z\). Such harmless redundancy does not affect completeness.

For each full-dimensional candidate ideal \(T\), set \(m=|T|\). Enumerate every ordered triple of distinct residues
\[
A_1,A_2,A_3\in\{1,\ldots,m-1\}
\]
and retain it exactly when \(x\mapsto A\cdot x\pmod m\) is bijective on \(T\). Every genuine minimally four-generated Apéry staircase is covered: \(e_1,e_2,e_3\in T\) forces those residues to be nonzero and distinct.

Among the two negative pairs for \(k=4\), both admit such labelings. Among the 198 for \(k=5\), exactly three do. Therefore only five pairs require any further argument.

### 7.2 The modular certificate

For every cut \(f\in\{0,\ldots,m-1\}\), compute
\[
\mathcal R_f(T,A)=\sum_{j,\ell\parallel e_j}
L_\ell[f-A\cdot t_\ell]_m.
\]
If the actual maximum has residue \(f=[M]_m\), then each actual top deficit dominates its least nonnegative residue, so
\[
D\ge\mathcal R_f(T,A).
\]
By (2),
\[
\mathcal R_f(T,A)\ge m(m-1)\quad\Longrightarrow\quad W\ge0. \tag{10}
\]

The remaining finite check tests (10) for **all cuts**, not just a conjectured maximum cut. This covers all possible integer lifts \(a_j=A_j+m q_j\), with arbitrarily large \(q_j\), whenever those lifts realize the shape as an Apéry set.

### 7.3 The five surviving pairs

Write \(U(Z)\) for the union of principal boxes as above.

1. \(k=4,m=8\):
   \[
   Z=\{(0,0,2),(0,1,1),(1,0,1),(1,1,0)\},\quad T=U(Z).
   \]
2. \(k=4,m=12\):
   \[
   Z=\{(0,0,3),(0,1,2),(1,0,2),(1,1,1)\},\quad T=U(Z).
   \]
3. \(k=5,m=9\):
   \[
   Z=\{(0,0,2),(0,1,1),(0,2,0),(1,0,1),(2,0,0)\},\quad T=U(Z).
   \]
4. \(k=5,m=15\):
   \[
   Z=\{(0,0,3),(0,1,2),(1,1,1),(2,0,1),(2,1,0)\},
   \]
   \[
   T=U(Z)\cup\{(0,2,0)\}.
   \]
5. \(k=5,m=15\):
   \[
   Z=\{(0,1,2),(0,2,1),(1,1,1),(2,0,1),(2,1,0)\},\quad T=U(Z).
   \]

The certificate results are:

| Pair | \(m\) | \(\Phi(T,Z)\) | Bijective residue triples | Cuts tested | Minimum of \(\mathcal R_f-m(m-1)\), over all triples and cuts |
|---:|---:|---:|---:|---:|---:|
| 1 | 8 | -2 | 4 | 32 | 0 |
| 2 | 12 | -1 | 4 | 48 | 0 |
| 3 | 9 | -2 | 24 | 216 | 0 |
| 4 | 15 | -1 | 8 | 120 | 15 |
| 5 | 15 | -2 | 8 | 120 | 15 |

There are 48 residue labelings and 536 cut checks in this last step. All are nonnegative. The JSON output records every surviving triple and every cut value.

**Conclusion of the proof.** If \(\Phi(T,Z)\ge0\), use (7). Otherwise Sections 5–7 exhaust every possibility for \(|Z|\le5\), and (10) proves Wilf in each surviving case. This proves the stated partial theorem.

## 8. Why this is not a proof for all embedding dimension four

The sufficient count inequality is false for genuine Apéry staircases with larger final windows. The supplied handoff already contains the family
\[
S_s=\langle s^2,s^2+1,s^2+s,s^2+s+1\rangle,\qquad s\ge2.
\]
Its staircase can be taken as
\[
T_s=\{(x,y,z)\in\mathbb N^3:x+y+z\le s-1,\ xy=0\}.
\]
Its final window is the top degree \(s-1\), giving
\[
k=2s-1,\qquad E(Z)=2(s-1)(s-2),\qquad
d_Z=(s-1)(s-2).
\]
Thus
\[
\boxed{\Phi(T_s,Z)=-(s-1)(s-2)<0\quad(s\ge3).}
\]
Nevertheless its Wilf number is
\[
W(S_s)=\frac{s(s-1)(s-2)}3\ge0.
\]
For instance \(S_5=\langle25,26,30,31\rangle\) has \(k=9\), \(E=24\), \(d_Z=12\), \(\Phi=-12\), and \(W=20\).

This is not a counterexample to Wilf. It is an explicit obstruction to extending the count argument without the weights and carry terms. It also shows that no universal bound of five on the final-window cardinality can close the problem.

The general exact target remains
\[
\boxed{\Delta_Z\le B_{\rm off}+\sum_{\ell\text{ deep}}s_\ell.} \tag{11}
\]
The present theorem removes \(|Z|\le5\) from the unresolved regime. It does not establish (11) for every \(|Z|\ge6\).

## 9. What happens at six points

### 9.1 Strict compression can fail

For six points, (9) can equal zero: \(b=6\), \(p=1\), \(q=2\). As a concrete example, let
\[
Z_h=\{(i,j,h+3-i-j):0\le i\le1,\ 0\le j\le2\},\qquad h\ge0.
\]
Then
\[
|U(Z_h)|=6h+15,\qquad \Phi_0(Z_h)=-8
\]
for every \(h\). Thus simply retaining all negative expansions no longer terminates. This family refutes strict coordinate-expansion monotonicity for arbitrary six-point antichains.

The compiled diagnostic enumeration found 345,988 compressed six-point antichains up to coordinate permutation, with 2,264 having negative score and minimum score \(-9\). These are finite shape counts only, not a proof about all six-point final windows.

### 9.2 A lattice restriction excludes the displayed infinite family

**Lemma.** If a finite lower ideal \(T\subset\mathbb N^3\) admits a residue-bijective linear labeling modulo \(|T|\), its complement has at most one minimal point with all three coordinates positive.

**Proof.** Let \(p\) be such a point and \(q\in T\) its unique residue representative. For each \(i\), \(p-e_i\in T\). If \(q_i>0\), then \(q-e_i\in T\) has the same residue as \(p-e_i\), forcing \(q=p\), impossible. Hence \(q=0\), so \(p\) has residue zero. If \(p'\) were another such point, then \(p-e_1\) and \(p'-e_1\) would be distinct points of \(T\) with equal residues. Contradiction. This is the full-support assertion of Hellus–Rechenauer–Waldi, Proposition 2.6. ∎

Now suppose a lower ideal \(T\) contains \(Z_h\) as maximal points. Consider
\[
p_1=(1,1,h+2),\qquad p_2=(1,2,h+1).
\]
Each dominates a point of \(Z_h\), so neither is in \(T\). Every immediate predecessor of either point belongs to \(U(Z_h)\subset T\). They are therefore two distinct minimal complement points with all coordinates positive, contradicting the lemma.

Consequently **no member of this displayed infinite family can occur as the final-window points of a residue-bijective staircase**, even if additional lower-ideal points are allowed.

This exclusion is useful, but it is not an exhaustive argument for six points. In particular, coordinate compression need not preserve residue feasibility or the full set of minimal complement points. One cannot simply delete an impossible compressed shape and assume all of its stretched extensions are impossible. No such shortcut is used in the theorem for at most five points.

## 10. Verification and reproducibility

The accompanying archive contains:

- `verify_final_window.py`: the complete finite part of the theorem, generated from scratch; only Python's standard library is required.
- `wilf_work.py`: exact Dijkstra computation of Apéry representatives, primitive-generator checks, and independent checks of (1)–(6).
- `verification-results.json`: full enumeration totals, the five surviving pairs, all 48 residue triples, all 536 cut values, and exact semigroup examples.
- `verification-run.log`: concise successful run output.
- `enumerate_compressed.cpp` and `check_residue_labels.cpp`: independent compiled implementations used to cross-check the compressed-shape and residue-label classifications. The label-checking program uses a 64-bit residue mask and is intended for the enumerated shapes of size at most 38.
- `negative_compressed_6.json`: the six-point diagnostic list, explicitly outside the proved theorem.

Run the complete partial-theorem verifier from the extracted directory:

```bash
python verify_final_window.py
```

The successful run in this session completed in about seven seconds. Runtime is informational; the verification assertions and integer output are the evidence.

The Python enumeration independently reproduced the compiled counts 18, 287, and 8,340 for three, four, and five compressed points, respectively, and the same 40 residue labelings for the five-point exceptions. The compiled and Python programs organize candidate generation differently.

Separately, exact identity checks passed on 2,590 minimally four-generated semigroups among 3,000 seeded proposals. The random seed was 20260905; multiplicities were sampled from 20 through 600 and the other proposed generators below \(10m\). Those tests validate the formulas and implementation on examples; they are **not** part of the infinite-class proof and do not establish the general conjecture. They can be repeated with:

```bash
python wilf_work.py --random 3000
```

No old historical search counts from the supplied handoff were treated as newly reproduced evidence.

## 11. Final claim ledger

| Claim | Status |
|---|---|
| Exact Apéry moment, coordinate boundary, reflection, and final-window identities | Re-derived here and checked on exact examples |
| Coordinate insertion formula (9) | Proved analytically |
| Strict increase under insertion for antichains of size at most five | Proved analytically |
| Exhaustive reduction to compressed antichains and finite ideal extensions | Proved analytically |
| Nonnegative projection criterion for one, two, or three final-window points | Proved by finite classification; three-point table printed above |
| Classification and modular completion for four and five points | Computer-assisted proof, with source and complete output |
| Wilf whenever the final-window cardinality is at most five | Proved by the preceding chain |
| Displayed six-point zero-increment family is not residue feasible | Proved using the minimal-complement lemma |
| Every six-point final window satisfies Wilf | Not proved here |
| Every four-generated numerical semigroup satisfies Wilf | Not proved here |
| A counterexample to Wilf | None obtained |
| Newness of the partial theorem relative to all published literature | Not established |

The requested global proof or disproof has not been obtained. The durable advance is the complete, reproducible extension from two to five final-window elements, together with an explicit account of where its finite-reduction argument stops.
