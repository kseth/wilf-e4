# Final arithmetic for the branch theorems

## Status and purpose

This note completes task G1. It contains no geometric or computer-assisted
assertion. Starting from the exact moment identity in
[`foundations.md`](foundations.md) and the routing in
[`case-partition.md`](case-partition.md), it converts the three kinds of branch
conclusion into Wilf's inequality.

The branch theorems themselves remain separate obligations. The assembly in
Section 3 is therefore conditional on those theorems.

## 1. Setup

Let

\[
S=\langle m,a_1,a_2,a_3\rangle
\]

be a minimally four-generated numerical semigroup. Retain the notation

\[
A=\min_i a_i,\qquad
D_0=3mH-4b\mathbin\cdot s,\qquad
W_4(S)=4|S\cap[0,c)|-c
\]

from the foundational note. Since each \(a_i\) is an integer strictly larger
than the multiplicity,

\[
A\ge m+1.
\tag{1}
\]

Proposition 4.2 of that note gives the exact identity

\[
\boxed{mW_4(S)=AD_0-m(m-1).}
\tag{2}
\]

By Proposition 3.1 of the foundational note, the four points
\(0,e_1,e_2,e_3\) have distinct residues modulo \(m\), so \(m\ge4\).
The number \(W_4(S)\) is an integer.

## 2. Conversion lemma

### Proposition 2.1

Under the setup above:

1. if \(D_0\ge m-1\), then \(W_4(S)\ge1\);
2. if \(D_0\ge m\), then
   \[
   W_4(S)\ge A-m+1\ge2;
   \]
3. if \(m\ge30\) and
   \[
   D_0\ge m-\frac{29}{10},
   \]
   then \(W_4(S)\ge0\).

#### Proof

For the first assertion, (1) and (2) give

\[
\begin{aligned}
mW_4(S)
&\ge A(m-1)-m(m-1)\\
&=(A-m)(m-1)\\
&\ge m-1>0.
\end{aligned}
\]

Thus \(W_4(S)>0\); its integrality gives \(W_4(S)\ge1\).

For the second assertion, (2) gives

\[
mW_4(S)
\ge Am-m(m-1)
=m(A-m+1).
\]

Division by \(m>0\), followed by (1), gives the claim.

For the last assertion, suppose instead that \(W_4(S)<0\). Integrality then
gives \(W_4(S)\le-1\), so (2) implies

\[
AD_0\le m(m-2).
\]

Because \(m\ge30\), (1) yields

\[
D_0
\le\frac{m(m-2)}A
\le\frac{m(m-2)}{m+1}
=m-3+\frac3{m+1}.
\]

Consequently

\[
m-D_0
\ge\frac{3m}{m+1}
\ge\frac{90}{31}
>\frac{29}{10},
\tag{3}
\]

where

\[
\frac{90}{31}-\frac{29}{10}=\frac1{310}.
\]

But the assumed lower bound on \(D_0\) says
\(m-D_0\le29/10\), contradicting (3). Therefore \(W_4(S)\ge0\).
\(\square\)

### Remark 2.2 (the endpoint)

The same proof shows that

\[
D_0\ge m-C,\qquad C<\frac{90}{31},
\]

is sufficient for every \(m\ge30\). The strict inequality is essential to
this arithmetic argument: at \(m=30\), the negative-integer estimate permits
the endpoint \(m-D_0=90/31\). The retained constant \(29/10\) lies below it
by exactly \(1/310\).

The third assertion uses negative integrality, whereas the first two
assertions are direct positive lower bounds. These mechanisms should not be
conflated in the branch proofs.

## 3. Conditional assembly

### Corollary 3.1

Assume the branch results recorded in the proof outline:

| Route | Branch conclusion | Arithmetic consequence |
|---|---|---|
| \(m\le19\) | \(W_4(S)\ge0\) | direct |
| \(20\le m\le29\) | \(W_4(S)\ge0\) | direct |
| B2: no full-support corner | \(D_0\ge m-1\) | \(W_4(S)\ge1\) by Proposition 2.1(1) |
| B3: \(p=(1,1,1)\) | \(W_4(S)\ge0\) | direct |
| B4: \(p\sim(2,1,1)\) | \(D_0\ge m-1\) | \(W_4(S)\ge1\) by Proposition 2.1(1) |
| B5: \(|p|_1\ge5,\ R\le6\) | \(D_0\ge m\) | \(W_4(S)\ge A-m+1\ge2\) by Proposition 2.1(2) |
| B6: \(|p|_1\ge5,\ R\ge7\) | \(D_0\ge m-29/10\) | \(W_4(S)\ge0\) by Proposition 2.1(3) |

Then every minimally four-generated numerical semigroup satisfies
\(W_4(S)\ge0\).

#### Proof

Proposition 2.1 of the case-partition note says that exactly one row applies.
The last column proves the desired conclusion in that row. \(\square\)

This corollary is an assembly rule, not an independent proof of the unproved
branch conclusions listed in its middle column.
