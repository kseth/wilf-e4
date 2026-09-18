# Wilf: a completed secondary-family proof and the remaining four-generator gap

**Research manuscript, 5 September 2026.**

This manuscript does **not** prove or disprove Wilf's conjecture for every
four-generated numerical semigroup. It contains a complete argument for an
unbounded family, additional proved reductions, and exact counterexamples
to two proposed closing lemmas. None of those auxiliary counterexamples is
a counterexample to Wilf.

The proofs received independent checks within this research session. The
polynomial certificates use exact rational arithmetic. This is not external
peer review, and no publication-priority claim is made.

## The completed family theorem

For a numerical semigroup \(S\), let \(c(S)\) be its conductor,
\(n(S)=|S\cap[0,c(S))|\), and \(W_4(S)=4n(S)-c(S)\).
Write \(A/q=\{k\in\mathbb N:qk\in A\}\).

Let \(A=\langle a,b\rangle\) and \(B=\langle c,d\rangle\) be
two-generated numerical semigroups, let \(p,q\) be coprime positive integers,
and assume \(S=pA+qB\) has exactly four minimal generators. If, for some
integer \(g\ge1\),
\[
A/q=B/p=R=\langle2,2g+1\rangle,
\]
and
\[
q(R\setminus\{0\})\subseteq(a+b)+A,
\qquad
p(R\setminus\{0\})\subseteq(c+d)+B,
\]
then
\[
\boxed{W_4(S)\ge1.}
\]

The parameter \(g\), the multiplicity and conductor of \(S\), and its
final-window cardinality are unrestricted. The proof derives exact genus
and conductor formulas, reduces the desired inequality to a piecewise
polynomial, and certifies its sign on sixteen regions. All 1,600 rational
coefficients in the nonnegative basis are nonnegative; all sixteen reverse
basis expansions agree exactly with the original polynomial.

For example, the theorem covers
\[
S=\langle3030,3725,3737,5066\rangle,
\quad c=134796,\quad n=48366,\quad W_4=58668.
\]
Its final window has sixteen Apéry points, so this example is beyond the
earlier six-point theorem's hypothesis.

Part I gives the complete invariant derivation, parameterization, theorem,
and certificate construction. The companion archive includes every
certificate coefficient and an executable standard-library checker.

## Additional results and their scope

| Result | Status and scope |
| --- | --- |
| A triple containing the multiplicity has gcd greater than one | Proved: \(W_4\ge2\). |
| Gcd of the other three generators exceeds one | Proved conductor descent; a minimum-conductor counterexample has gcd one for every triple. |
| No interior excluded corner and at most two pair-interaction types | Proved Wilf, using a discrete mean bound and Eliahou's published \(c\le3m\) theorem. |
| Any staircase with no interior excluded corner | Proved central-box/three-arm structure; the full moment inequality remains unproved. |
| Three full-cap arms, each with an initial plateau followed by arbitrary boundary profiles | Proved continuous mean at most \(2/3\) after normalization. This profile restriction is essential to the current proof. |
| An arbitrary arm based at outward coordinate at least \(1/3\), after normalizing maximum height to one | Proved explicit potential bound, including initial slack. Earlier-base arms still require a bound. |
| A staircase between successive three-face shells, radius at least five | Proved the ordered weighted inequality for every radius; exact polynomial and finite scalar certificates. |
| Every remaining four-generated semigroup | **Unresolved.** |

## Why these results do not complete the conjecture

The earlier finite-reduction manuscript gives the necessary counterexample
region
\[
20\le m<2\times10^{14},\qquad
m<a_1<a_2<a_3\le m(m-2),\qquad c\le m^2-3m+1.
\]
Its analytic arguments were audited again for degenerate limits in this
continuation. The new gcd theorem adds
\(\gcd(m,a_i,a_j)=1\) for every pair. A minimum-conductor counterexample
must have gcd one for all four triples. These conditions have not been
shown inconsistent, and the finite region has not been exhausted.

The new family theorem has a precise boundary: a common quotient can have
multiplicity at least three. The compatible paired example
\(A=\langle5,7\rangle,q=9,B=\langle5,8\rangle,p=11\) has common quotient
\(\langle3,4,5\rangle\), and gives \(S=\langle45,55,72,77\rangle\).
That semigroup satisfies Wilf, but the multiplicity-two quotient theorem
does not apply. The unrestricted primary class is also outside its scope.

There are two logically separate missing obligations:

1. For arbitrary no-interior staircases, the central-box/three-arm theorem
   still allows underfilled caps and multiple off-boundary plateaus. The
   proved boundary-profile inequality does not cover them. Even a proof of
   the full continuous inequality would require a discrete/arithmetic
   argument to settle every associated numerical semigroup.
2. The remaining interior-corner and general paired-quotient cases have not
   been eliminated by the new family theorem or the earlier finite reduction.

Consequently, neither a proof of emptiness nor a negative-Wilf semigroup is
provided here. The remaining work is a substantive universal inequality or
exhaustive certificate, not an omitted algebraic step.

## Exact failed closing lemmas

The adjoining-one-generator shortcut
\(n(T)+4(g(T)-g(S))\ge3(c(T)-c(S))\) is false even if one may choose
which nonmultiplicity generator to adjoin. The exact witness is
\(S=\langle31,171,251,553\rangle\), with \(W_4(S)=833>0\).
All three eligible three-generator bases violate that stronger shortcut.

The claim that every horn is optimized by a capped-balanced taper is also
false. For central sides \((1/5,2/5,2/5)\), an admissible alternating
boundary profile improves the best such taper by exactly \(1/120000\).
The improved profile still satisfies the combined three-horn inequality.
The broader theorem in Part V explicitly incorporates this improvement.

## Reproduction

Extract the companion archive and, from its top-level directory, run:

```sh
python3 round3/verify_checkpoint.py
```

This reruns the exact secondary polynomial certificate, independent Apéry
invariant checks, the shell certificate, the boundary-profile polynomial
identities, and the exact counterexample to the taper ansatz. The code and
the full rational coefficient data are both supplied. The analytic proofs
are necessary parts of the family theorems; checking numerical examples
alone would not establish them.

Historical finite-reduction manuscripts and their original verification
archive are retained under `dependencies/`. Exploratory LP/MILP and random
search records under `round3/` are labeled as diagnostics and are not used
to claim an exhaustive four-generator proof.

---

# Part I. Complete proof for the secondary quotient-two family

# Exact invariants for a secondary class with quotient multiplicity two

Date: 5 September 2026. Sections 1–4 prove exact invariant formulas. Section 6 completes Wilf for the secondary common-quotient multiplicity-two class using a finite exact rational polynomial certificate. This is an unrestricted family theorem, not a solution of all embedding dimension four. The formula expression and finite certificate were checked independently during the session; external review remains outstanding.

Let A=⟨a,b⟩ and B=⟨c,d⟩ be two-generated numerical semigroups, let p,q be coprime positive integers, and put

S=pA+qB=⟨pa,pb,qc,qd⟩.

Suppose

A/q=B/p=R=⟨2,2g+1⟩, g≥1.

The formulas in Sections 1–3 do not require the extra secondary criticality hypothesis. The parameterization in Section 4 uses it.

Write F_A=ab−a−b, F_B=cd−c−d, P=pq, X=pF_A+qF_B, and G_0=(X+P+1)/2.

## 1. Residue fibers and symmetry

For each residue u modulo q, let A_u be the least element of A in that residue. The normalized fiber

I_u={k≥0:A_u+qk∈A}

contains zero and is closed under addition of R. Hence it contains every even integer and has a least odd integer 2h_u+1, where 0≤h_u≤g. Therefore

I_u=⟨2,2h_u+1⟩=:R_{h_u},

where R_0=N. Similarly every normalized residue fiber of B modulo p is R_{k_v} for some 0≤k_v≤g.

Since p,q are coprime, the pairs (u,v) index all residue classes modulo pq. The corresponding S-fiber is exactly

pA_u+qB_v+pq(R_{h_u}+R_{k_v})
=pA_u+qB_v+pq R_{min(h_u,k_v)}.

The equality of sumsets follows because R_h⊆R_k if h≥k and R_h+R_k=R_{min(h,k)}.

Two-generated semigroups are symmetric. Reflection about F_A sends a residue u to u'=F_A−u modulo q, preserves its normalized fiber parameter h_u, and sends its minimum to

A_{u'}=F_A+q−2qh_u−A_u.

This follows directly by reflecting the set A_u+qR_{h_u}: R_h is symmetric with Frobenius number 2h−1. Consequently, among fibers with a fixed parameter h, the largest and smallest minima add to F_A+q−2qh. The same fact holds for B.

## 2. A genus formula using colon-ideal counts

For 1≤j≤g write the unique gap representation

(2j−1)q=ab−u_j a−v_j b,
1≤u_j<b, 1≤v_j<a,

and define

D_j^A=u_jv_j,
D_{g+1}^A=0,
H_j^A=D_j^A−D_{j+1}^A.

Define D_j^B,H_j^B analogously using the gaps (2j−1)p of B.

**Colon-ideal fact.** If z=ab−u a−v b is a positive gap of A, then

{s∈A:s+z∈A}=(ua+A)∪(vb+A),

and the complement of this ideal in A has exactly uv elements. To prove this, use the unique representation s=i a+j b with 0≤i<b. Membership in the ideal is equivalent to i≥u or j≥v. The excluded rectangle 0≤i<u,0≤j<v has uv distinct labels.

In a normalized fiber R_h, the number of elements s for which s+(2j−1) is excluded equals max(h−j+1,0): they are the even positions 0,2,...,2(h−j). Thus

D_j^A=Σ_u max(h_u−j+1,0),
H_j^A=|{u:h_u≥j}|,
Σ_u h_u=D_1^A.

The same identities hold for B. The elementary identity min(h,k)=Σ_{j≥1}1_{h≥j}1_{k≥j} now gives

**g(S)=G_0−pD_1^A−qD_1^B+Σ_{j=1}^g H_j^A H_j^B.**

For completeness, the residue count is as follows. If A_u=u+qα_u, the A-fiber contributes α_u+h_u gaps; therefore Σα_u=g(A)−D_1^A. The analogous statement holds for B. Each S-fiber contributes its initial shift plus min(h_u,k_v) gaps. The residue-offset sum from p u+q v equals (p−1)(q−1)/2. Hence

g(S)=(p−1)(q−1)/2+p(g(A)−D_1^A)+q(g(B)−D_1^B)+Σ_j H_j^A H_j^B,

which is the displayed formula since g(A)=(F_A+1)/2 and g(B)=(F_B+1)/2.

## 3. A conductor formula from the least colon elements

For j=0,...,g, let

δ_A(j)=min{s∈A:s+(2j+1)q∈A},
δ_B(j)=min{s∈B:s+(2j+1)p∈B}.

For j<g the colon-ideal fact gives

δ_A(j)=min(a u_{j+1},b v_{j+1}),
δ_B(j)=min(c u'_{j+1},d v'_{j+1}),

while δ_A(g)=δ_B(g)=0.

Then

**F(S)=X+P−L, where L=min_{0≤j≤g}{2Pj+pδ_A(j)+qδ_B(j)}.**

**Proof.** For each realized fiber parameter h let d_A(h) be the smallest A_u among fibers of type h, and define d_B(k) similarly. Treat unrealized types as having minimum infinity. The fiber and symmetry identities of Section 1 give

F(S)=X+P−min_{h,k}{2P max(h,k)+p d_A(h)+q d_B(k)}.

Indeed the largest label in a fiber gap equals pA_u+qB_v+P(2min(h,k)−1), and the maximum A_u within type h is F_A+q−2qh−d_A(h).

In a fiber R_h, the least position s with s+(2j+1)∈R_h is 2max(h−j,0). Therefore

δ_A(j)=min_h{d_A(h)+2q max(h−j,0)},

and similarly for B. Substituting these expressions into 2Pj+pδ_A(j)+qδ_B(j), the coefficient of 2P is

j+max(h−j,0)+max(k−j,0)≥max(h,k).

Equality is attained by j=max(h,k). Thus the two minima are equal, proving the conductor formula. ∎

Combining Sections 2–3 gives the exact Wilf expression

W_4(S)=X+P+1−3L+4pD_1^A+4qD_1^B−4Σ_j H_j^A H_j^B.

## 4. Positive secondary parameters and two conductor branches

Assume now the secondary interior property

qR*⊆(a+b)+A, pR*⊆(c+d)+B.

Write q=ab−u_1a−v_1b. Since 2q−a−b∈A, necessarily

2q=r a+s b,
r=b−2u_1>0, s=a−2v_1>0.

Successive odd gaps have representations u_j=u_1−(j−1)r and v_j=v_1−(j−1)s, until at least one coefficient ceases to be positive. Put α=u_g, β=v_g. Then

a=2β+(2g−1)s,
b=2α+(2g−1)r,
q=rβ+sα+(2g−1)rs,
u_j=α+(g−j)r,
v_j=β+(g−j)s.

All r,s,α,β are positive integers. The first represented odd multiple also has an interior representation precisely when α<r or β<s; equality at the stopping coefficient without strictness in the other coordinate would give only a pure-axis representation below or at ab.

Swapping a,b if needed, assume sα≤rβ. Then

0<τ=α/r≤υ=β/s, τ<1,

and the colon minima always use the same branch:

δ_A(j)=a(α+(g−1−j)r), 0≤j<g.

Indeed a u_{j+1}−b v_{j+1}=(2j+1)(sα−rβ). Apply the same construction to B with positive parameters r',s',α',β', normalized 0<σ=α'/r'≤ω=β'/s', σ<1.

For j<g, the quantities 2Pj+pδ_A(j)+qδ_B(j) form a nonincreasing arithmetic progression. To see this, set k=2g−1, Q=k+τ+υ, P'=k+σ+ω. After dividing its slope by rr'ss', it is

P'(k+2τ)−Q(k+2ω)
=−k[(υ−τ)+(ω−σ)]−2(υω−τσ)≤0.

Consequently the conductor correction simplifies to only two branches:

**L=min{2pq(g−1)+paα+qcα', 2pqg}.**

The genus data also simplify:

D_1^A=(α+(g−1)r)(β+(g−1)s),
H_j^A=q−2jrs for j<g,
H_g^A=αβ,

and similarly for B. Thus the entire class has explicit polynomial genus expressions and a two-branch conductor expression. Section 6 supplies an exact certificate proving that their Wilf expression is strictly positive.

## 5. Exact independent invariant checks

`quotient_two_formulas.py` computes only the closed formulas above, then compares them with independent shortest-path Apéry invariants. The five checked examples have quotient genera 1,4,7,10,9. The genus-four example is

S=⟨3030,3725,3737,5066⟩,
g(S)=86430, F(S)=134795, W_4(S)=58668,

and its final window contains sixteen Apéry points, so the formulas apply beyond the earlier six-point restriction. Exact data are in `quotient_two_checks.json`.


## 6. Completion of the family theorem

**Theorem.** Let S=p⟨a,b⟩+q⟨c,d⟩ be a minimally four-generated secondary semigroup in its paired critical form. If its common quotient is

⟨a,b⟩/q=⟨c,d⟩/p=⟨2,2g+1⟩, g≥1,

then **W_4(S)≥1**.

There is no bound on the multiplicity of S, its conductor, type, or final-window size in the hypothesis. The common-quotient genus g is unbounded. The separate quotient R=N is an ordinary gluing and is already a known Wilf case.

**Proof.** Use the positive secondary parameters of Section 4, orienting each pair so that

x=α/r≤y=β/s, 0<x<1,
z=α'/r'≤w=β'/s', 0<z<1.

Put A_scale=rs, B_scale=r's', h=g−1≥0, k=2h+1,

Q=k+x+y=q/A_scale,
P=k+z+w=p/B_scale,
D_A=(h+x)(h+y), D_B=(h+z)(h+w),

H=hPQ−h(h+1)(P+Q)+(2/3)h(h+1)(2h+1)+xyzw,

L_h=2PQh+P(k+2y)x+Q(k+2w)z.

These are the exact normalized values of the genus sum and the first conductor branch: H=Σ_j H_j^A H_j^B/(A_scale B_scale), and the actual normalized correction L/(A_scale B_scale) is at most L_h. The elementary positive-integer bounds give

1/r≤min(x,1−x), 1/s≤min(y,1),
1/r'≤min(z,1−z), 1/s'≤min(w,1).

For example, r x=α≥1 and r(1−x)=r−α≥1; likewise s y=β≥1 and s≥1. Define f(t)=min(t,1−t) for t∈[0,1], and j(t)=min(t,1) for t≥0. Substitution into the exact Wilf expression yields

W_4(S)≥A_scale B_scale Ψ(h,x,y,z,w)+1,

where

Ψ=P(k+2x)(k+2y)+Q(k+2z)(k+2w)+PQ
  +4P D_A+4Q D_B−4H−3L_h
  −P[f(x)(k+2y)+j(y)(k+2x)]
  −Q[f(z)(k+2w)+j(w)(k+2z)].

The following finite certificate proves Ψ≥0 on the entire relaxed domain

h≥0, 0≤x≤1, y≥x, 0≤z≤1, w≥z.

For each of the sixteen flags ε_x,ε_z,ε_y,ε_w∈{0,1}, substitute

x=(ε_x+X)/2, z=(ε_z+Z)/2, with X,Z∈[0,1].

If ε_y=0, put y=x+(1−x)Y with Y∈[0,1], so f(x) selects its appropriate half-interval branch and j(y)=y. If ε_y=1, put y=1+Y with Y≥0 and j(y)=1. Apply the same construction to w with Z,W and ε_w. These substitutions cover the domain, allowing shared boundary points. On each region Ψ becomes an ordinary polynomial with rational coefficients.

Expand that polynomial in the Bernstein basis in each bounded variable and in the ordinary power basis in h and any unbounded Y,W. Every basis function is nonnegative on its region. The exact rational coefficient conversion is

b_i=Σ_{e≤i} c_e binom(i,e)/binom(d,e)

in each bounded coordinate of degree d; use the tensor product for multiple coordinates, and leave unbounded power exponents unchanged.

The certificate `../audit/quotient_two_certificate.py` constructs Ψ independently, performs these substitutions and exact conversions using Python's Fraction arithmetic, and verifies all 1,600 coefficients as nonnegative. It also expands each Bernstein representation back into the power basis and checks exact equality with the original polynomial on all sixteen regions. No numerical optimization or floating-point sign test occurs in this proof. The complete rational coefficient data are in `../audit/quotient_two_certificate_full.json`, and a separate proof audit is in `../audit/quotient_two_wilf_certificate.md`. The counts, repeated over the four choices of ε_x,ε_z, are:

| Region for y,w | Coefficients per choice of ε_x,ε_z | Smallest coefficient |
| --- | ---: | ---: |
| y≤1, w≤1 | 144 | 8/3 |
| y≤1, w≥1 | 96 | 0 |
| y≥1, w≤1 | 96 | 0 |
| y≥1, w≥1 | 64 | 0 |

Consequently Ψ≥0. Since A_scale B_scale>0, the Wilf bound above gives W_4(S)≥1. ∎

This proof has an analytic reduction and a finite exact polynomial-certificate step. The certificate's normalized polynomial, inverse-integer bounds, domain substitutions, and Bernstein conversion were independently audited, and all sixteen coefficient calculations were independently rerun.

## 7. An explicit infinite parameter family and the precise remaining scope

For every positive g not divisible by three, let

A_g=⟨2g+1,4g⟩, q_g=4g+1,
B_g=⟨2g+3,4g⟩, p_g=4g+3.

The generator pairs are coprime, and gcd(p_g,q_g)=1. They arise in Section 4 from (r,s,α,β)=(2,1,1,1) and (r',s',α',β')=(2,1,1,2), respectively, so both quotients are ⟨2,2g+1⟩ and the strict interior property holds. Their two paired critical values are distinct. Hence they give secondary semigroups with arbitrarily large common-quotient genus, all covered by the theorem. Their four generators are

(4g+3)(2g+1), 4g(4g+3), (4g+1)(2g+3), 4g(4g+1).

The theorem also includes the verified example ⟨3030,3725,3737,5066⟩ with final-window cardinality sixteen. Thus its hypothesis is not restricted to the prior six-point case.

**The common quotient can have multiplicity greater than two.** For example,

A=⟨5,7⟩, q=9,
B=⟨5,8⟩, p=11

have equal quotient ⟨3,4,5⟩. The interior condition holds on its generators 3,4,5 and therefore on every positive quotient element. The resulting secondary semigroup

S=⟨45,55,72,77⟩

has critical values 360=8·45=5·72 and 385=7·55=5·77, type eight, conductor 396, n=171 and W_4=288. It lies outside the new multiplicity-two quotient theorem (while its three-point final window is covered by the earlier theorem). General common quotients of multiplicity at least three and the unrestricted primary class remain unresolved by this argument.

## 8. Exact arithmetic criterion for the general secondary interior condition

The following criterion was derived independently by the coordinating researcher and checked here. It applies to every quotient, without a multiplicity-two assumption.

Let A=⟨a,b⟩ with coprime a,b≥2, let q be positive, and let R=A/q. Then

qR*⊆(a+b)+A

if and only if

lcm(q,a)>ab and lcm(q,b)>ab,

or equivalently

q/gcd(q,a)>b and q/gcd(q,b)>a.

**Proof.** Every element of A has a unique canonical form ia+jb with 0≤i<b and j≥0. If i,j are positive, the element is in (a+b)+A. If i=0 and j≥a+1, use instead

jb=ba+(j−a)b,

whose two coefficients are positive. The only remaining canonical forms are ia with 0≤i<b and jb with 0≤j≤a. None has a representation with both coefficients positive: equality ia=i'a+j'b with j'>0 forces j'≥a and hence i≥b+1, while equality jb=i'a+j'b with i'>0 forces i'≥b and hence j≥a+1. Consequently

A\((a+b)+A)={ia:0≤i≤b}∪{jb:1≤j<a}.

The positive multiples of q in A are exactly qR*. The smallest positive multiple of q on the a-axis is lcm(q,a), and the corresponding b-axis value is lcm(q,b). Thus avoiding the displayed boundary is precisely the pair of strict inequalities above. ∎

For paired data S=p⟨a,b⟩+q⟨c,d⟩ with a common quotient, the full secondary interior property is therefore equivalent to these four arithmetic inequalities:

q/gcd(q,a)>b, q/gcd(q,b)>a,
p/gcd(p,c)>d, p/gcd(p,d)>c.

The one-sided interior property places no uniform bound on the quotient multiplicity. For example, for every odd N≥3 take A=⟨N,N+1⟩ and q=N+2. Both arithmetic inequalities hold. The quotient R=A/q has multiplicity exactly (N+1)/2. Indeed, if 1≤k<(N+1)/2, the canonical representation of qk, if it existed, would require a coefficient of N+1 at least 2k; that already contributes 2k(N+1)>(N+2)k. At k=(N+1)/2 the identity

(N+2)k=(N+1−k)N+(2k−N)(N+1)

has nonnegative coefficients and proves membership. This unbounded example concerns one side of the quotient condition; producing a paired secondary semigroup with the same quotient requires a second compatible two-generator quotient and coprime scale factors. The explicit paired multiplicity-three example in Section 7 already shows why the family theorem in Section 6 cannot cover all secondary semigroups.



---

# Part II. Independent exact certificate audit

# Exact positivity certificate for the secondary quotient-two family

5 September 2026. This is a completed proof for the specified unbounded family. It does not prove the unrestricted four-generator conjecture. The proof and certificate were independently checked by the invariant-formula and audit agents; external mathematical review remains outstanding.

## The theorem certified

Let

\[
S=p\langle a,b\rangle+q\langle c,d\rangle
\]

be a minimally four-generated numerical semigroup, with coprime positive integers \(p,q\), two-generated numerical semigroups \(A=\langle a,b\rangle\) and \(B=\langle c,d\rangle\), and

\[
A/q=B/p=R=\langle2,2g+1\rangle,\qquad g\ge1.
\]

Assume the secondary interior property

\[
q(R\setminus\{0\})\subseteq (a+b)+A,
\qquad
p(R\setminus\{0\})\subseteq(c+d)+B.
\]

Then its Wilf number satisfies

\[
W_4(S)=4|S\cap[0,c(S))|-c(S)\ge1.
\]

In particular, this proves Wilf strictly for every secondary semigroup whose common quotient has multiplicity two. There is no bound on \(g\), the multiplicity or conductor of \(S\), its type, or its final-window cardinality.

## Analytic inputs and their audit

The exact genus and conductor formulas are proved in `../secondary/quotient_two_exact_formulas.md`, Sections 1–4. They have been independently audited, with attention to the following potential failure points.

1. Every normalized residue fibre is exactly \(\langle2,2h+1\rangle\), including \(h=0\), because it contains all even positions and a tail of odd positions. Reflection by two-generated symmetry preserves \(h\) and sends the minimum to \(F_A+q-2qh-A_u\). For \(h=0\), the normalized Frobenius number is \(-1\); the same expression remains valid.
2. For a positive gap \(z=ab-ua-vb\), the colon ideal is \((ua+A)\cup(vb+A)\). Its complement is the rectangle of canonical factorizations \(0\le i<u,0\le j<v\), hence has \(uv\) elements. This justifies the finite differences used in the genus expression, rather than merely matching examples.
3. In the conductor calculation, minimizing over normalized fibre types commutes with minimizing over \(0\le j\le g\): the elementary expression \(j+(h-j)_++(k-j)_+\) is at least \(\max(h,k)\), with equality at \(j=\max(h,k)\). Unrealized fibre types contribute infinity and cause no extra assumption.
4. The secondary hypothesis supplies the strict integer inequalities needed below. Its positive parameters can be oriented as

\[
\begin{aligned}
a&=2\beta+(2g-1)s,& b&=2\alpha+(2g-1)r,
&q&=r\beta+s\alpha+(2g-1)rs,\\
c&=2\beta'+(2g-1)s',& d&=2\alpha'+(2g-1)r',
&p&=r'\beta'+s'\alpha'+(2g-1)r's',
\end{aligned}
\]

with all parameters positive integers and

\[
0<x=\alpha/r\le y=\beta/s,\quad x<1,
\qquad
0<z=\alpha'/r'\le w=\beta'/s',\quad z<1.
\]

For clarity about strictness, the gap representation of the final missing odd multiple is \((2g-1)q=ab-\alpha a-\beta b\). For the next odd multiple set \(U=\alpha-r,V=\beta-s\), so \((2g+1)q=ab-Ua-Vb\). Both \(U,V>0\) would still give a gap. If \(U,V\ge0\) with a zero coefficient, this is a pure-axis element at most \(ab\) which cannot remain in \(A\) after subtracting \(a+b\). If \(U<0\), subtraction has the nonnegative representation \((-U-1)a+(a-V-1)b\); the other case is symmetric. Thus the required interior property forces \(\alpha<r\) or \(\beta<s\), and after ordering the ratios, it forces \(x<1\). Consequently

\[
\frac1r\le\min(x,1-x),\quad \frac1s\le\min(y,1),
\quad \frac1{r'}\le\min(z,1-z),\quad \frac1{s'}\le\min(w,1).
\]

These bounds use both \(\alpha\ge1\) and \(r-\alpha\ge1\). Discarding the strict secondary condition would invalidate the latter bound.

## Reduction to one piecewise polynomial

Put \(V=rsr's'>0\), \(h=g-1\ge0\), \(k=2h+1\),

\[
Q=k+x+y,\qquad P=k+z+w,
\qquad D_A=(h+x)(h+y),\quad D_B=(h+z)(h+w).
\]

The normalized genus-product sum and an upper bound for the normalized conductor correction are

\[
H=hPQ-h(h+1)(P+Q)+\frac23h(h+1)(2h+1)+xyzw,
\]

\[
L_h=2PQh+P(k+2y)x+Q(k+2w)z.
\]

In fact \(H=V^{-1}\sum_jH_j^AH_j^B\) and \(L/V\le L_h\). The proof below only needs this inequality; it does not assume which of the two conductor branches attains the minimum.

Define \(f(t)=\min(t,1-t)\) on \([0,1]\) and \(j(t)=\min(t,1)\) on \([0,\infty)\). The exact invariant expression and the inverse-integer bounds give

\[
W_4(S)\ge V\,\Psi(h,x,y,z,w)+1,
\]

where

\[
\begin{aligned}
\Psi={}&P(k+2x)(k+2y)+Q(k+2z)(k+2w)+PQ\\
&+4PD_A+4QD_B-4H-3L_h\\
&-P\{f(x)(k+2y)+j(y)(k+2x)\}\\
&-Q\{f(z)(k+2w)+j(w)(k+2z)\}.
\end{aligned}
\]

For example, the negative term \(p(a+b)/V\) is

\[
P\left(\frac{k+2y}{r}+\frac{k+2x}{s}\right)
\le P\{f(x)(k+2y)+j(y)(k+2x)\}.
\]

All sign directions therefore agree with the lower bound on \(W_4\). It remains to prove \(\Psi\ge0\) on the relaxed domain

\[
h\ge0,\quad 0\le x\le1,\quad y\ge x,
\quad 0\le z\le1,\quad w\ge z.
\]

## The exact finite certificate

For each \((\epsilon_x,\epsilon_z,\epsilon_y,\epsilon_w)\in\{0,1\}^4\), substitute

\[
x=(\epsilon_x+X)/2,\quad z=(\epsilon_z+Z)/2,
\qquad X,Z\in[0,1].
\]

When \(\epsilon_y=0\), put \(y=x+(1-x)Y\), with \(Y\in[0,1]\). When \(\epsilon_y=1\), put \(y=1+Y\), with \(Y\ge0\). Apply the corresponding choice to \(w\) using \(z,W,\epsilon_w\). These sixteen regions cover the domain, including all shared boundaries. The functions \(f,j\) have a fixed polynomial expression on each region.

In the variable order \((h,X,Y,Z,W)\), retain the power basis for unbounded variables, and use the Bernstein basis

\[
B_i^d(t)=\binom di t^i(1-t)^{d-i}
\]

in each bounded coordinate. Every resulting tensor-product basis function is nonnegative on its region. If \(c_e\) are the power coefficients, the mixed-basis coefficients are exactly

\[
b_\ell=
\sum_{\substack{e_i\le\ell_i\ (i\text{ bounded})\\
e_i=\ell_i\ (i\text{ unbounded})}}
c_e\prod_{i\text{ bounded}}
\frac{\binom{\ell_i}{e_i}}{\binom{d_i}{e_i}}.
\]

`quotient_two_certificate.py` performs this conversion using only exact rational arithmetic. It then performs a separate reverse calculation: every Bernstein basis function is expanded as \(\binom di t^i(1-t)^{d-i}\), and the resulting power polynomial is required to equal the original polynomial coefficient by coefficient. Thus the conversion is checked by an exact identity, as well as by an independent human audit of the formula.

The outcomes below hold for each of the four choices of \((\epsilon_x,\epsilon_z)\).

| Bounds on \(y,w\) | Coordinate degrees \((h,X,Y,Z,W)\) | Coefficients | Minimum |
| --- | --- | ---: | ---: |
| \(y\le1,w\le1\) | \((3,2,1,2,1)\) | 144 | \(8/3\) |
| \(y\le1,w\ge1\) | \((3,2,1,1,1)\) | 96 | 0 |
| \(y\ge1,w\le1\) | \((3,1,1,2,1)\) | 96 | 0 |
| \(y\ge1,w\ge1\) | \((3,1,1,1,1)\) | 64 | 0 |

All \(4(144+96+96+64)=1600\) rational coefficients are nonnegative, and all sixteen reverse expansions are exact. Hence \(\Psi\ge0\), proving \(W_4(S)\ge1\).

## Reproduction and files

Run with a standard Python 3 installation; no third-party package is needed:

```sh
python round3/audit/quotient_two_certificate.py
```

The program asserts all coefficient signs, all reverse expansion identities, and the total coefficient count. Its final line is:

```text
PASS: all 1600 coefficients are nonnegative; all 16 basis expansions reconstruct exactly.
```

The full certificate `quotient_two_certificate_full.json` records the region flags, bounded coordinates, coordinate degrees, original power coefficients, and every mixed-basis coefficient as an exact rational number. `quotient_two_certificate_summary.json` records the compact per-region results. These are finite exact proof data, not a parameter search or floating-point evidence.

The original exact invariant formulas also agree with independent shortest-path Apéry computations on the five examples recorded in `../secondary/quotient_two_checks.json`. Those computations provide implementation checks; the family theorem follows from the analytic identities and the exact polynomial certificate.



---

# Part III. Arithmetic reductions and an exact failed extension lemma

# Arithmetic reductions and the failed three-generator extension shortcut

5 September 2026. The reductions below are proved; they do not close the
unrestricted four-generator conjecture.

## 1. A common divisor in a triple containing the multiplicity settles Wilf

Let S=⟨m,a₁,a₂,a₃⟩ be minimally four-generated. If

    d=gcd(m,aᵢ,aⱼ)>1,

then W₄(S)≥2. In particular, every counterexample must satisfy

    gcd(m,aᵢ,aⱼ)=1 for all distinct i,j.

To prove this, denote the remaining generator by b, and put

    R=⟨m/d,aᵢ/d,aⱼ/d,b⟩.

The generating set of R need not be minimal. Since gcd(d,b)=1, multiplication
by d permutes residues modulo b, and

    Ap(S,b)=d Ap(R,b).

Indeed a minimal representative modulo b cannot use b in a factorization;
the other three generators are precisely the d-scaled generators of R other
than b. Applying the Apéry genus and conductor formulas gives

    c(S)=d c(R)+(d−1)(b−1),
    g(S)=d g(R)+(d−1)(b−1)/2,
    W₄(S)=d W₄(R)+(d−1)(b−1).

For any semigroup generated by at most four elements, the weighted lower-ideal
bound gives W₄(R)≥−(m(R)−1). This follows either by padding the selected
factorization ideal to three coordinates or from Zhai's bound and the actual
embedding dimension. Here m(R)=m/d. As b≥m+1,

    W₄(S)≥−m+d+(d−1)(b−1)≥(d−2)m+d≥2.

No bounded search is used in this proof.

## 2. The other triple supplies a conductor descent

If d=gcd(a₁,a₂,a₃)>1, let R=⟨m,a₁/d,a₂/d,a₃/d⟩. The same formulas, with
retained generator b=m, show

    W₄(S)=d W₄(R)+(d−1)(m−1).

Therefore a negative W₄(S) forces W₄(R)<0. Such an R must still have embedding
dimension four, since Wilf is known in embedding dimensions at most three.
Moreover c(R)<c(S). Consequently a counterexample of minimum conductor would
have gcd one for **every** triple of minimal generators.

This is a minimal-counterexample reduction. It does not assert that every
four-generated semigroup with gcd(a₁,a₂,a₃)>1 satisfies Wilf.

## 3. Exact adjoining-one-generator identities

Let T=⟨m,a,b⟩ be a three-generated numerical semigroup, and let
S=T+zN remain minimally four-generated with multiplicity m. Write

    Δ=c(T)−c(S),   H=g(T)−g(S),   n(T)=c(T)−g(T).

Direct substitution gives the exact identity

    W₄(S)=W₃(T)+n(T)+4H−3Δ.

If bᵣ is the least element of T in residue r modulo m, then the Apéry labels
of S are given exactly by

    wᵣ=min₀≤k<m/gcd(m,z) {kz+b_[r−kz]ₘ}.

There is no need for larger k: a block of m/gcd(m,z) copies of z is a positive
multiple of m and cannot improve a least representative.

The tempting stronger bound n(T)+4H≥3Δ is false, even if one is allowed to
choose which nonmultiplicity generator is adjoined. For

    S=⟨31,171,251,553⟩,
    c(S)=1327, n(S)=540, W₄(S)=833,

all three choices fail that stronger bound:

| Adjoined z | Three-generator base | W₃(T) | n(T)+4H−3Δ |
| ---: | --- | ---: | ---: |
| 171 | ⟨31,251,553⟩ | 1404 | −571 |
| 251 | ⟨31,171,553⟩ | 1270 | −437 |
| 553 | ⟨31,171,251⟩ | 883 | −50 |

The exact identities hold in every row; all three triples have gcd one.
This is a counterexample to the proposed closing lemma, not to Wilf.
`three_plus_one.py` checks the Apéry min-plus formula and the displayed
invariants using integer arithmetic; its results are retained in
`three_plus_one_results.json`.

## Background

A. Zhai, *An asymptotic result concerning a question of Wilf*, Theorem 1 and
Lemma 3, https://arxiv.org/abs/1111.2779, supplies the established weighted
lower-ideal bound used in Section 1. The deflation formulas above are derived
explicitly so that their scope, including nonminimal generating sets for R,
is clear. No publication-priority claim is made.



---

# Part IV. No-interior structure and the bipartite Wilf theorem

# No-interior-corner ideals: clique trees and a settled bipartite subclass

## Scope

Let T be a finite lower ideal in N^3 with no coordinatewise minimal excluded point supported on all three coordinates. Equivalently, membership is determined by its three pair projections:

  (x,y,z) belongs to T iff (x,y,0), (x,0,z), (0,y,z) all belong to T.

The equivalence follows by choosing a minimal excluded point below any omitted point.

This note proves a structural clique-tree description and a moment bound for the subclass with a bipartite interaction graph. It does not prove the conjectural continuous mean bound 2M/3 for the full no-interior class.

## 1. A chordal graph encodes the maximal boxes

For coordinate i let h_i be its largest axis exponent. Introduce graph vertices (i,r), 0<=r<=h_i. Vertices from the same coordinate class are all adjacent. Vertices (i,r),(j,s), i!=j, are adjacent exactly when r e_i+s e_j belongs to T. The zero vertices are universal.

Within one coordinate class, the external neighborhood of a lower level contains that of any higher level. This is downward closure.

Every induced cycle of length at least four would repeat a coordinate class. Since that class is a clique, its repeated vertices must be exactly two adjacent cycle vertices. Name their levels r<s. The other cycle neighbor of (i,s) lies outside this class and is also adjacent to (i,r), by nested external neighborhoods. That edge is a chord, a contradiction. Thus the graph is chordal.

A maximal clique contains every level below each of its coordinate maxima. Its three maxima form a point of T, by pairwise determination. Conversely, every point of T gives the clique consisting of the three coordinate prefixes. Hence maximal graph cliques correspond bijectively to maximal points z of T, or equivalently to their boxes B_z=[0,z] intersected with N^3.

The clique-tree theorem for chordal graphs therefore supplies a tree on these maximal boxes such that the boxes containing any graph vertex form a connected subtree. In particular, for every coordinate i and level r,

  {z maximal in T:z_i>=r}

is a connected subtree. Intersections of connected subtrees of a tree are connected, so the boxes containing any point x also form a connected subtree.

## 2. Exact tree inclusion-exclusion

Let E be the edges of such a tree, and let z meet z' denote the coordinatewise minimum. Since a nonempty finite tree has one more vertex than edge, pointwise counting gives

  1_T = sum_z 1_{B_z} - sum_{zz' in E} 1_{B_(z meet z')}.

Consequently

  |T| = sum_z prod_i(z_i+1) - sum_{zz' in E} prod_i(min(z_i,z'_i)+1),

and, for any positive weights a,

  sum_T a.x = (1/2) [sum_z |B_z| a.z
                    -sum_{zz' in E} |B_(z meet z')| a.(z meet z')].

The same identity holds for the union of the corresponding continuous boxes and its volume and first moments. Thus the general inclusion-exclusion over exponentially many subsets reduces to tree vertices and edges.

## 3. At most three leaves and a three-arm description

If z is a leaf with neighbor z', then z_i>z'_i for some coordinate i, since distinct maximal points are incomparable. The connected-superlevel-set property implies that z_i exceeds the value of coordinate i at every other node: otherwise the path to another such node would cross z'. Different leaves cannot use the same coordinate. Therefore the clique tree has at most three leaves; it is a path or a tripod, aside from the single-box case.

Choose one node where each coordinate reaches its global maximum, and let z0 be the median of those three nodes in the tree. Every component beyond z0 contains at most one of the three chosen maximum nodes. Along an arm toward the maximum of coordinate i, coordinate i is nondecreasing and the other two coordinates are nonincreasing, by connectedness of every coordinate superlevel set. The increasing coordinate is strictly increasing between consecutive nodes, since otherwise the later maximal point would be dominated by the earlier one.

After thickening to boxes, or after any positive diagonal coordinate scaling, this yields a central box [0,c_1]x[0,c_2]x[0,c_3] and at most three disjoint arms. Arm i lies beyond x_i=c_i and below the other two central coordinate bounds. Each cross section perpendicular to its outward coordinate is a rectangle, and its two side lengths are nonincreasing functions of the outward coordinate.

This reduces the unproved full continuous mean bound to an inequality for a central box plus at most three rectangular-fiber arms. The arms' intersections are exactly contained in the central box.

## 4. The bipartite interaction moment theorem

Define an interaction graph on {1,2,3}: join i and j if some minimal excluded point has support {i,j}. Pure-axis excluded points impose only individual bounds. If this graph is bipartite with color classes A,B, then for all positive weights a,

  E_T[a.X] <= (2/3) max_T a.x.                         (B)

Proof: no excluded constraint involves two coordinates of the same color class. Holding the other class fixed therefore gives a rectangular fiber in the coordinates of one class. Simultaneously moving all coordinates in A to their fiber tops stays in T. Conditional uniformity on each finite interval 0,...,H implies that its top coordinate equals twice its conditional mean. Writing mu_i=E[a_i X_i] and mu=sum_i mu_i, the expected weight after this simultaneous move is mu+sum_{i in A}mu_i, and is at most M. The analogous B move gives mu+sum_{i in B}mu_i<=M. Adding yields 3mu<=2M.

The identical argument works for continuous downsets, using uniform intervals [0,H] and their endpoints. Thus (B) holds in both settings, without a discretization correction.

## 5. Wilf consequence of the bipartite subclass

For a four-generator Apéry ideal, D=3mM-4 sum_T a.x and mW=D-m(m-1). Therefore (B) gives

  W >= M/3-(m-1).

This proves Wilf whenever M>=3m-3, equivalently conductor c>=2m-2. The remaining conductors lie in the already published c<=3m range. Combining those facts proves Wilf for the entire bipartite interaction subclass.

Accordingly, an unresolved no-interior counterexample must involve minimal excluded pair corners of all three support types {1,2},{1,3},{2,3}.

## 6. What does not follow

The full no-interior interaction graph may be a triangle. The bipartite simultaneous-update argument then supplies only the ordinary three-coordinate bound. Tree inclusion-exclusion alone does not yet provide the required sign for the first-moment expression. No proof of the desired universal continuous bound mu<=2M/3, or a complete classification of ordered geometric LP failures, is asserted here.



---

# Part V. The sharp full-cap boundary-profile theorem

# A sharp three-horn inequality for full-cap plateaus and boundary profiles

## Statement and precise scope

Let `a,b,c>0`, with `S=a+b+c<=1`. Consider a central box `[0,a]×[0,b]×[0,c]` and three disjoint horns extending beyond its respective faces. In the horn extending beyond the coordinate `a`, let the other two side lengths be `u(t),v(t)`, where `a<=t<=1`.

This theorem assumes the following **specific feasible class**:

1. On `a<=t<=1-b-c`, the rectangle uses the full central caps: `u(t)=b`, `v(t)=c`.
2. On `1-b-c<=t<=1`, the profiles are nonnegative and nonincreasing, bounded by `b,c`, and satisfy `u(t)+v(t)=1-t`.

Impose the analogous conditions on the other two horns. The second condition permits arbitrary monotone boundary profiles, including alternating coordinate changes; it is not restricted to a balanced shrink.

Then, writing

`J_a=∫_a^1 u(t)v(t)[3t+(3/2)(u(t)+v(t))-2]dt`,

and defining `J_b,J_c` by coordinate permutation, we have

`J_a+J_b+J_c <= abc[2-(3/2)(a+b+c)]`.

Consequently the uniform mean of `x+y+z` on the union of the central box and horns is at most `2/3`.

The proof below optimizes the entire boundary portion of each horn. **It does not establish that arbitrary horns can be replaced by this class.** Profiles with underfilled initial caps or multiple off-boundary plateaus remain outside the theorem.

## 1. Exact optimization of a boundary horn

Let its two caps be `B>=C>=0`, with `R=B+C<=1`. Reverse time by setting `r=1-t`, so `0<=r<=R`. The boundary condition is `u+v=r` and both profiles are nondecreasing in `r`.

We may sort the two side lengths pointwise. Their product and sum stay unchanged; the larger sorted length is still at most `B`, the smaller is at most `C`, and both remain nondecreasing. Let `d` be their nonnegative difference. Then `d` is 1-Lipschitz and

`L(r)=max(0,r-2C) <= d(r) <= U(r)=min(r,2B-r)`.

The boundary contribution is

`Q=∫_0^R (2-3r)(r²-d(r)²)/8 dr`.

The coefficient of `d²` changes sign at `r0=2/3`.

If `R<=r0`, the maximizing profile minimizes `d` everywhere, so `d=L`.

If `R>=r0`, fix `v=d(r0)`. For `r<r0`, the smallest feasible difference is

`d_-(r)=max(L(r),v+r-r0)`.

For `r>r0`, the largest feasible difference is

`d_+(r)=min(U(r),v+r-r0)`.

These bounds follow directly from the 1-Lipschitz condition. They are attained simultaneously: both displayed functions are 1-Lipschitz, remain between `L` and `U`, and meet at `v`. The first maximizes the integrand where the coefficient is nonnegative, and the second where it is nonpositive. Thus they maximize the whole integral among profiles with the given value at `r0`.

Putting `q=(r0-v)/2`, the resulting profiles have the following one-tent form:

- for `0<=r<=2q`, the two side lengths are both `r/2`;
- for `2q<=r<=B+q`, they are `q` and `r-q`;
- for `B+q<=r<=B+C`, they are `B` and `r-B`.

Here `0<=q<=C`. The feasible envelope parameters when `R>=r0` form the smaller interval

`max(0,r0-B)<=q<=min(C,r0/2)`.

The integral of this one-tent profile, denoted `I(q;B,C)`, satisfies the exact derivative identity

`∂I/∂q = (B-q)²(1-B-2q)/2`.

Therefore its unrestricted maximum on `[0,C]` occurs at

`q*=min(C,(1-B)/2)`.

When `R>=r0`, this value lies in the feasible envelope interval: `B>=1/3` gives `(1-B)/2<=1/3` and `(1-B)/2>=2/3-B`; the condition `B+C>=2/3` handles the endpoint `q*=C`. When `R<=r0`, `B+2C<=3R/2<=1`, so the formula gives `q*=C`, agreeing with the earlier direct maximization.

This proves the boundary optimum for every pair of caps.

## 2. Gain over the balanced capped profile

The usual capped-balanced boundary profile is the endpoint `q=C`. Improvement is possible exactly when `B+2C>1`.

Put `w=B+2C-1` and `y=B-C`. Integrating the displayed derivative gives

`I((1-B)/2;B,C)-I(C;B,C)`

`= w²y²/8+w³y/24+w⁴/192`.

If `w<=0`, the gain is zero. Thus the exact gain is

`g(w_+,y)`, where `g(z,y)=z²y²/8+z³y/24+z⁴/192`.

For example, `B=C=2/5` gives gain `1/120000`. This is the explicit obstruction to assuming a capped-balanced taper is always optimal.

## 3. The canonical three-horn identity

Relabel the central sides so that `a<=b<=c`. Write

`δ=1-a-b-c`, `x=b-a`, `y=c-b`, and `e2=ab+ac+bc`.

For a horn starting at `a`, with sorted full caps `B>=C` and `a+B+C<=1`, its capped-balanced value is

`H(a;B,C)`

`=BC[R-(3/2)R²+((3/2)R-1/2)B+((3/2)R-1)C-B²/2-(3/4)BC]+C³/6-C⁴/4`,

where `R=1-a`. This integrates the full-cap initial plateau followed by the capped-balanced boundary profile.

Direct expansion gives the exact identity

`abc[2-(3/2)S]-H(a;c,b)-H(b;c,a)-H(c;b,a)`

`= δ² e2/2 + δ x²(2x+3y)/6 + x²(2x²+4xy+3y²)/12`.  (1)

All coefficients on the right are nonnegative. The accompanying checker verifies this as a polynomial identity with exact rational coefficients.

## 4. Allowing every boundary profile

For the horn extending beyond `a`, the caps are `B=c,C=b`, and its possible gain over `H(a;c,b)` is

`g((c+2b-1)_+,c-b)=g((x-δ)_+,y)`.

The horn extending beyond `b` has caps `c,a`. It cannot improve, because

`c+2a<=a+b+c<=1`.

Likewise the horn extending beyond `c` has caps `b,a`, with `b+2a<=1`, so it cannot improve either.

Consequently the left-side deficit in the theorem is at least the right side of (1) minus `g((x-δ)_+,y)`. Since `0<=(x-δ)_+<=x` and `g` is increasing in its first nonnegative argument, this is at least

`δ² e2/2 + δ x²(2x+3y)/6`

`+x²y²/8+(7/24)x³y+(31/192)x⁴ >=0`.

This proves the theorem.

For positive central sides, equality holds precisely when `δ=0` and `x=0`, provided the boundary horns themselves attain their optima. Thus the equality family includes every central box `(a,a,1-2a)`, `0<a<=1/3`, with its optimizing horns.

## Verification and remaining step

`fullcap_boundary_verify.py` uses only Python's standard library and exact rational polynomial arithmetic. It verifies the canonical sum identity, the one-tent derivative, its gain formula, and the final nonnegative remainder identity. The resulting flags are saved in `fullcap_boundary_verification.json`.

The analytic control argument in Section 1 is part of the proof; numerical optimization is not used. Extending this theorem to arbitrary underfilled caps and arbitrary off-boundary monotone profiles still requires an additional argument.



---

# Part VI. Exact obstruction to the simpler taper ansatz

# The capped-balanced single-horn ansatz is false

This note concerns only single-horn profile optimization. It does **not** provide a counterexample to Wilf's conjecture, or to the combined three-horn inequality.

## Functional and candidate family

Put \(R=1-a\), and reverse the variable by \(r=1-t\). The functional becomes

\[
J[u,v]=\int_0^R uv\,[1-3r+\tfrac32(u+v)]\,dr,
\]

where \(u,v\) are nondecreasing, \(0\le u\le b\), \(0\le v\le c\), and \(u+v\le r\). We assume \(b+c\le R\).

For chosen caps \(U\ge V\), the candidate capped-balanced profile is

\[
(u,v)=\begin{cases}
(r/2,r/2),&0\le r\le2V,\\
(r-V,V),&2V\le r\le U+V,\\
(U,V),&U+V\le r\le R.
\end{cases}
\]

Direct integration gives

\[
\boxed{
J_R(U,V)=UV\left[R-\tfrac32R^2+
(\tfrac32R-\tfrac12)U+(\tfrac32R-1)V
-\tfrac12U^2-\tfrac34UV\right]
+\tfrac16V^3-\tfrac14V^4.
}
\]

The derivative identities are

\[
\boxed{\partial_U J_R=V(R-U-V)(1-\tfrac32R+\tfrac32U)}
\]

and

\[
\boxed{\partial_V J_R=
\tfrac12(U-V)^2(1-U-2V)+
U(R-U-V)(1-\tfrac32R+\tfrac32V).}
\]

For fixed \(V\), the derivative in \(U\) changes sign at most once, from negative to positive. Thus the maximum in the larger cap lies at \(U=V\) or its allowed upper endpoint. On the balanced branch,

\[
J_R(d,d)=(R-\tfrac32R^2)d^2+(3R-\tfrac43)d^3-\tfrac32d^4,
\]

\[
\frac{d}{dd}J_R(d,d)=d(R-2d)(2-3R+3d).
\]

This branch likewise attains its maximum at one of its two endpoints.

## Exact counterexample

Take

\[
a=\tfrac15,\qquad b=c=\tfrac25,\qquad R=\tfrac45.
\]

First establish the best value within the candidate family. By symmetry suppose \(U\ge V\). The preceding derivative reduction leaves the balanced branch or \(U=2/5\). On the balanced branch the maximum is at \(d=0\) or \(d=2/5\). On the other branch,

\[
\partial_V J_{4/5}(2/5,V)
=(\tfrac25-V)(V^2-\tfrac1{10}V+\tfrac1{25})
\ge0.
\]

The quadratic is strictly positive because it equals
\((V-1/20)^2+3/80\). Hence the maximum over **all chosen candidate caps** is

\[
\max_{0\le U,V\le2/5}J_{4/5}(U,V)
=J_{4/5}(2/5,2/5)=\frac8{1875}.
\]

Now choose a different feasible profile:

\[
(u,v)=\begin{cases}
(r/2,r/2),&0\le r\le3/5,\\
(3/10,r-3/10),&3/5\le r\le7/10,\\
(r-2/5,2/5),&7/10\le r\le4/5.
\end{cases}
\]

Both coordinates are continuous and nondecreasing, they stay in \([0,2/5]\), and \(u+v=r\) throughout. Direct exact integration gives

\[
\boxed{J[u,v]=\frac{171}{40000}
=\frac8{1875}+\frac1{120000}
>\max_{U,V}J_{4/5}(U,V).}
\]

Equivalently, the excess over the balanced profile is

\[
-\int_{3/5}^{7/10}(r/2-3/10)^2(1-3r/2)\,dr
-\int_{7/10}^{4/5}(r/2-2/5)^2(1-3r/2)\,dr
=\frac1{120000}.
\]

The obstruction is the sign change at \(r=2/3\). At larger \(r\), maximizing the product \(uv\) while keeping \(u+v=r\) decreases the objective. A controlled departure from balance, followed by a second capped segment, improves the integral.

## A family of improving profiles

For equal caps \(B\), endpoint \(R=2B\), and a parameter \(0\le q\le B\), use

\[
(u,v)=\begin{cases}
(r/2,r/2),&0\le r\le2q,\\
(q,r-q),&2q\le r\le B+q,\\
(r-B,B),&B+q\le r\le2B.
\end{cases}
\]

The difference from the fully balanced profile is

\[
\Delta(B,q)=\frac{(B-q)^3[3(B+q)-2]}{12}.
\]

For \(1/3<B\le1/2\), this expression is maximized at
\(q=(1-B)/2\), giving

\[
\boxed{\Delta_{\max}(B)=\frac{(3B-1)^4}{192}>0.}
\]

For \(B=2/5\), this is precisely the exact counterexample above. This family only proves improvement over the full balanced profile; the comparison with the optimum over every capped-balanced profile was established explicitly at \(B=2/5\).

## The smaller selected cap can also optimize in the interior

Even inside the candidate family, reducing to both full caps is invalid. For

\[
R=17/20,\quad b=3/5,\quad c=1/4,
\]

on the \(U=b\) branch,

\[
\partial_V J_R=\frac{123}{4000}-\frac{21}{100}V+\frac12V^2-V^3.
\]

This is positive at \(V=1/5\) and negative at \(V=1/4\), yielding an interior local maximum. Its derivative is strictly decreasing over this interval, so the maximum there is unique. A correct finite-dimensional candidate optimization must allow roots of this cubic.

## Verification files and scope

`exact_counterexample.py` uses only Python's exact rational arithmetic and checks all three pieces, feasibility at segment endpoints, exact integrals, and the strict gain. `exact_counterexample.json` records its output. `probe.py` and `probe_results.json` record the exploratory numerical search that found the profile; the proof above does not depend on floating-point optimization.

The general monotone single-horn optimization remains open in this note. The capped-balanced optimality ansatz cannot supply its missing proof.



---

# Part VII. Unbounded face-shell theorem

# An elementary certificate for all three-face shells of radius at least five

This is a self-contained geometric argument, with exact finite arithmetic tables. It makes no claim of research novelty.

## Statement

For an integer \(R\ge5\), let
\[
F_R=\{x\in\mathbb N^3:|x|\le R,\ \min_i x_i=0\}.
\]
Suppose \(F_R\subseteq T\subseteq F_{R+1}\), put \(m=|T|\), and let the real weights satisfy
\[
a_1\ge m+1,\qquad a_2\ge a_1+1,\qquad a_3\ge a_2+1.
\]
Then
\[
\boxed{3m\max_{x\in T}(a\cdot x)-4\sum_{x\in T}a\cdot x\ \ge\ m(m-1).}
\]
No arithmetic realizability, residue bijection, or numerical-semigroup condition on \(T\) is used.

## Common notation and identity

Write
\[
n=|F_R|=1+\frac{3R(R+1)}2,\quad K=\frac{R(R+1)(2R+1)}6,
\quad L=3(R+1),\quad s=m-n.
\]
Each coordinate has sum \(K\) on \(F_R\), and the outer shell has \(L\) points. Set
\[
c=a_3,\quad u=c-a_1,\quad t=c-a_2,\quad z=u+t,
\quad M=\max_T a\cdot x.
\]
The weight assumptions imply
\[
u\ge2,\quad t\ge1,\quad t\le u-1,\quad
c\ge m+1+u,\quad z\ge3,\quad c\ge m+\tfrac32+\tfrac z2.
\]
For \(s>0\), let \(d=(R+1)c-M\). Since \(Rc\le M\le(R+1)c\), we have \(0\le d\le c\). For an outer-shell point \(x=(x_1,x_2,x_3)\), its deficiency from \((R+1)c\) is \(u x_1+t x_2\). Every selected outer-shell point has deficiency at least \(d\). Consequently, with
\[
B=3n-s>0,\qquad A=(R+1)B-12K,\qquad G=A-B=\frac{R(R-1)(R-2)}2-Rs,
\]
the desired left side \(D\) obeys
\[
\begin{aligned}
D
&\ge 3mM-4K(3c-z)-4sM\\
&=B((R+1)c-d)-12Kc+4Kz\\
&=Ac+4Kz-Bd.\tag{1}
\end{aligned}
\]
This inequality is the only estimate on the sum of the chosen shell points.

## The unsupplemented shape \(s=0\), for every \(R\ge5\)

Here \(M=Rc\) and, on writing \(Q=R(R-1)(R-2)/2\),
\[
D\ge Qc+12K\ge Q(n+3)+12K.
\]
Put \(E_0=Q(n+3)+12K-n(n-1)\). If \(v=R-5\), direct polynomial expansion gives
\[
4E_0=240+2028v+1536v^2+453v^3+60v^4+3v^5>0.
\]
This proves the assertion when \(s=0\).

## All radii \(R\ge13\)

Using only \(M\ge Rc\) and \(z\ge3\) in (1) gives
\[
D\ge (Q-Rs)c+12K.
\]
For \(0\le s\le L\) the coefficient is positive: its smallest value is
\[
Q-RL=\frac{R(R^2-9R-4)}2>0.
\]
Therefore it suffices to prove
\[
E(s)=(Q-Rs)(n+s+3)+12K-(n+s)(n+s-1)\ge0.
\]
This is a concave quadratic in \(s\), with leading coefficient \(-(R+1)\). Its minimum on \([0,L]\) is at an endpoint. The endpoint \(s=0\) was proved above. For \(v=R-13\), the other endpoint has expansion
\[
4E(L)=39264+124860v+33708v^2+3549v^3+168v^4+3v^5>0.
\]
This proves every \(R\ge13\), with no computational range cutoff assumption.

## The seven radii \(6\le R\le12\)

Let \(k=L-s\) be the number of omitted shell points and define
\[
J=\min\left(R+1,\left\lceil\frac{k}{2}\right\rceil\right).
\]
We claim \(d\le Ju\). If \(J\le R\), the two outer edges issuing from \((0,0,R+1)\) contain \(2J+1>k\) distinct points with \(x_1+x_2\le J\); all of their deficiencies are at most \(Ju\). At least one is selected. If \(J=R+1\), every shell point has deficiency at most \((R+1)u\). This proves the claim, including \(J=0\).

Since \(z\ge u+1\), equation (1) yields
\[
D\ge f(c,u)=Ac+4K(u+1)-B\min(c,Ju),\quad
u\ge2,\quad c\ge m+1+u.\tag{2}
\]
The exact minimum of this piecewise-linear convex function is elementary. For \(J=0\) or \(1\), its only relevant vertex is \((c,u)=(m+3,2)\), giving
\[
V_0=A(m+3)+12K-2BJ.
\]
For \(J\ge2\), the additional vertex is the intersection of \(c=Ju\) and \(c=m+1+u\), giving
\[
V_1=\frac{(GJ+4K)(m+1)}{J-1}+4K.
\]
In all the cases in this section \(m+1>2(J-1)\), so this vertex belongs to the domain. The recession slopes are \(A\), \(G+4K\), and \(GJ+4K\) (the latter when \(J\ge2\)); they are all nonnegative. For \(J=0\), the slopes are \(A\) and \(A+4K\).

The following table lists the exact smallest value of \(\min(V_0,V_1)-m(m-1)\) over the indicated finite range \(1\le s\le3(R+1)\); \(V_1\) is omitted when \(J\le1\). Substitution of the displayed formulas verifies every row using rational arithmetic. The accompanying script checks every individual value and all recession slopes.

| \(R\) | Minimum slack | A minimizing \(s\) | Corresponding \(J\) |
|---:|---:|---:|---:|
| 6 | \(422\) | 10 | 6 |
| 7 | \(3662\) | 11 | 7 |
| 8 | \(73896/7\) | 12 | 8 |
| 9 | \(92977/4\) | 13 | 9 |
| 10 | \(400820/9\) | 14 | 10 |
| 11 | \(78003\) | 15 | 11 |
| 12 | \(1408782/11\) | 16 | 12 |

Thus (2) proves these seven radii.

## Radius \(R=5\)

Here \(n=46\), \(K=55\), and \(L=18\). Normalize a shell deficiency by \(z=u+t\), and put \(v=t/z\in(0,1/2)\). Its normalized value is
\[
x_1(1-v)+x_2v.
\]
Uniformly in \(v\), the number of shell points with normalized deficiency at most the integer \(h\) is at least the following value \(N_h\):

| \(h\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| \(N_h\) | 1 | 4 | 8 | 13 | 15 | 17 | 18 |

These counts have short direct proofs:

- \(h=0\): the point \((0,0,6)\).
- \(h=1\): the three points \((0,j,6-j)\), \(0\le j\le2\), and \((1,0,5)\).
- \(h=2\): if \(v\le1/3\), all seven points \((0,j,6-j)\), plus \((1,0,5)\) and \((2,0,4)\), qualify. If \(v>1/3\), the five points on that first edge with \(j\le4\) and the three points \((i,0,6-i)\), \(1\le i\le3\), qualify.
- \(3\le h\le5\): all seven points \((0,j,6-j)\), the \(h\) points \((i,0,6-i)\), \(1\le i\le h\), and the \(h\) points \((i,6-i,0)\), \(1\le i\le h\), qualify. For the last group, \(i+(6-2i)v\le\max(i,3)\le h\). The three groups are disjoint.
- \(h=6\): all eighteen points qualify.

Choose the smallest listed \(h\) with \(N_h>18-s\). Since only \(18-s\) shell points are omitted, this proves \(d\le hz\). Equation (1) gives
\[
D\ge Ac+4Kz-B\min(c,hz),\qquad
z\ge3,\quad c\ge m+\tfrac32+\tfrac z2.\tag{3}
\]
The first vertex gives
\[
U_0=A(m+3)+12K-3Bh.
\]
For \(h\ge1\), the other vertex, \(c=hz\), gives
\[
U_1=\frac{(Gh+4K)(m+3/2)}{h-1/2}.
\]
It belongs to the domain because \((m+3/2)/(h-1/2)>3\). The recession slopes \(A\), \(G/2+4K\), and \(Gh+4K\) are positive for all these cases. When \(h=0\), only \(U_0\) is needed; its recession slopes are also positive.

Every case has positive slack:

| \(s\) | \(h\) | \(\min(U_0,U_1)-m(m-1)\) |
|---:|---:|---:|
| 1 | 6 | \(12108/11\) |
| 2 | 5 | \(1264\) |
| 3 | 5 | \(8627/9\) |
| 4 | 4 | \(9630/7\) |
| 5 | 4 | \(1050\) |
| 6 | 3 | \(2056\) |
| 7 | 3 | \(1713\) |
| 8 | 3 | \(1356\) |
| 9 | 3 | \(985\) |
| 10 | 3 | \(600\) |
| 11 | 2 | \(2826\) |
| 12 | 2 | \(2454\) |
| 13 | 2 | \(2068\) |
| 14 | 2 | \(1668\) |
| 15 | 1 | \(1623\) |
| 16 | 1 | \(1192\) |
| 17 | 1 | \(747\) |
| 18 | 0 | \(648\) |

Together with the \(s=0\) proof, this proves radius five and completes the theorem.

## Scope

This settles every one-shell extension \(F_R\subseteq T\subseteq F_{R+1}\) for \(R\ge5\), uniformly over an unbounded range of radii and weights. It does not assert that arbitrary three-face order ideals have this form, and it does not settle Wilf's conjecture in embedding dimension four.

The exact arithmetic checker is `face_shell_verify.py`. It requires only Python's standard library and produces `face_shell_verification.json`. It does not enumerate subsets of the shell, perform floating-point optimization, or use any numerical-semigroup enumeration.



---

# Part VIII. An arbitrary-arm theorem for bases at least one third

# A universal potential for horns based at or beyond one third

Normalize the maximum height to `M=1`. Let a horn start at outward
coordinate `a>=1/3`, with transverse caps `B,C>=0` satisfying
`a+B+C<=1`. Its transverse fibers are rectangles with nonincreasing side
lengths `f(t)<=B`, `g(t)<=C`, and satisfy `t+f(t)+g(t)<=1`.
The moment defect of the horn is

\[
\mathcal J_H=\int f(t)g(t)
  \left(3t+\frac32(f(t)+g(t))-2\right)dt.
\]

Write `x=min(B,C)`, `y=max(B,C)`, and define

\[
J(x,y)=\frac{x^3}{6}-\frac{x^4}{4}
 +\frac{xy^2}{2}-\frac{3x^2y^2}{4}-\frac{xy^3}{2},
\]

\[
\boxed{H(a;x,y)=J(x,y)
 +\frac{xy}{2}(1-a-x-y)(3a-1).}
\]

Then the universal bound is

\[
\boxed{\mathcal J_H\le H(a;x,y).}
\]

Equality is attained by holding the full caps constant from `t=a` to
`t=1-x-y`, then holding the smaller cap fixed while decreasing the larger
cap until they agree, and finally decreasing both equally to zero along
the height boundary. Central slack is allowed in this theorem.

## 1. Endpoint normalization for finite staircase horns

Suppose the horn has constant fibers `(f_j,g_j)` on intervals
`(t_(j-1),t_j]`, where `t_0=a`. Put `p_j=f_j g_j` and `s_j=f_j+g_j`.
The endpoint constraints are

\[
a\le t_1\le\cdots\le t_N,
\qquad t_j\le1-s_j.
\]

For fixed side lengths, the objective is

\[
\sum_j p_j(t_j-t_{j-1})
 \left(\frac32(t_j+t_{j-1}+s_j)-2\right).
\]

After collecting endpoint terms, this is a separable convex quadratic:
the quadratic coefficient of `t_j` is `3(p_j-p_(j+1))/2>=0`, where
`p_(N+1)=0`. A maximum on the compact endpoint polytope occurs at a vertex.

At a vertex, after deleting zero-length intervals, each surviving interval
ends at its height bound `t_j=1-s_j`. Indeed a block of equal endpoints
that touches neither `a` nor an upper bound could be moved slightly in both
directions, contradicting extremality. The upper bounds `1-s_j` are
nondecreasing, so a nonzero interval's active bound is its own upper bound.

Thus it suffices to bound staircase horns with every surviving right
endpoint on the height boundary.

## 2. Filling the tail has the correct sign here

Keep the first constant rectangle, with caps `(b,c)`, from `a` to its tight
right endpoint `1-b-c`. Between every subsequent pair of tight endpoints,
interpolate the two side lengths monotonically so that `f+g=1-t`.
Linear interpolation suffices. It lies above the original constant
rectangle on that interval.

Set `u=1-t`. If the original rectangle has product `p_0` and side sum `s`,
the interpolated rectangle has product `p>=p_0`, and the pointwise gain in
moment-defect integrands is

\[
(p-p_0)\left(1-\frac32u\right)+\frac32p_0(u-s)\ge0.
\]

Both terms are nonnegative because `u<=1-a<=2/3` and `u>=s`. Extend the
last tight rectangle to zero along the boundary as well; its added defect
is nonnegative for the same reason.

On this boundary tail the defect integrand is
`fg(1-3u/2)`, with nonnegative coefficient. For fixed `u=f+g` and starting
caps `(b,c)`, the product is maximized by keeping the smaller cap fixed
until the two sides balance, then reducing them together. This pointwise
maximizer is a valid nested profile. Consequently the original horn is
bounded by `H(a;min(b,c),max(b,c))`.

## 3. The full caps maximize the potential

For `x<=y`, write `r=1-a-x-y>=0`. Direct differentiation gives

\[
H_y=\frac{x r}{2}\bigl(3(a+y)-1\bigr),
\]

\[
H_x=\frac12\left[(a-x)(x-y)^2
       +r\bigl(x^2+2ay-yr\bigr)\right].
\]

The first derivative is nonnegative because `a>=1/3`. Also
`x<=(1-a)/2<=a` and `r<=1-a<=2a`, so every term in the second derivative
is nonnegative. Symmetry handles an interchange of the ordered caps.
Thus the potential is nondecreasing in both transverse caps. Replacing
the first rectangle's caps with the full bounds `(B,C)` proves the theorem.

General bounded monotone profiles follow by approximation with finite
step profiles from below and convergence of their volumes and first
moments. The finite staircase case already includes the cell unions
arising from finite lower ideals.

## 4. An exact obstruction to a stronger boundary-only potential

It is false that an arbitrary horn is bounded by the larger of zero and
the optimum among boundary profiles using its original transverse caps.
Take central sides

\[
(a,B,C)=\left(\frac1{20},\frac3{20},\frac45\right).
\]

For the horn outward in coordinate `a`, reduce the smaller effective cap
to `x=1/20`, keep `y=4/5`, and use a constant prefix followed by the
balanced taper. Exact integration gives

\[
H\left(\frac1{20};\frac1{20},\frac45\right)
 =\frac{613}{1920000}>0.
\]

The optimum over boundary profiles with the original caps `(3/20,4/5)`
is instead `-1/4800`, using the boundary-profile theorem in
`horns_audit.md`. Thus clipping that boundary potential at zero still
fails. Effective caps and slack must be addressed for bases below `1/3`.
This example refutes only that proposed horn potential; it does not refute
the full mean inequality or Wilf's conjecture.

## Status of the remaining Bellman problem

For a tight state with transverse side sum `r`, a jump to caps `(x,y)`
earns

\[
\left(1-\frac32r\right)(r-x-y)xy.
\]

A prospective earlier-base potential takes the supremum of one such jump
followed by the exact boundary-profile potential. Numerical dynamic
programming suggests that additional jumps do not improve it. A Bellman
inequality proving that statement, and a bound summing the resulting
three horn potentials against the central-box deficit, remain unresolved.
No general no-interior-corner moment theorem is asserted here.



---

# Part IX. Scope audit

# Final bounded audit of the arithmetic and structural reductions

5 September 2026. Verdict: the three reviewed reductions are valid within their stated scopes. One displayed algebra typo in the secondary appendix was corrected; no theorem changes. No parameter enumeration was needed for this audit.

## 1. Deflating a triple containing the multiplicity

Reviewed `../gcd_and_extension_reductions.md`. Put \(d=\gcd(m,a_i,a_j)>1\), let \(b\) be the remaining generator, and let \(R=\langle m/d,a_i/d,a_j/d,b\rangle\). The claims remain valid when this displayed generating set is not minimal.

Since \(\gcd(d,b)=1\), multiplication by \(d\) permutes residues modulo \(b\). An Apéry-minimal representative modulo \(b\) in either semigroup has no \(b\) in any factorization. Consequently \(\operatorname{Ap}(S,b)=d\operatorname{Ap}(R,b)\) as sets. This yields the displayed conductor, genus and \(W_4\) identities, without a gluing or membership hypothesis on \(b\) in the three-generator part.

The multiplicity of \(R\) is exactly \(\mu=m/d\), because the other displayed generators are larger. Let \(e_R\) be its actual embedding dimension. For \(2\le e_R\le4\), Zhai's Theorem 1 gives

\[
W_{e_R}(R)\ge-\frac{(\mu-1)(e_R-2)}2.
\]

Since \(W_4(R)=W_{e_R}(R)+(4-e_R)n(R)\), this implies \(W_4(R)\ge-(\mu-1)\). The case \(R=\mathbb N\) has \(\mu=1\) and \(W_4(R)=0\), so it also causes no exception. Therefore

\[
W_4(S)\ge-m+d+(d-1)(b-1)
\ge(d-2)m+d\ge2.
\]

The other-triple reduction is correctly stated only for a counterexample of minimum conductor. Its deflation may change multiplicity, but it strictly decreases conductor and preserves negativity of \(W_4\). If its actual embedding dimension falls below four, known Wilf in dimensions at most three contradicts that negativity. Thus minimum-conductor counterexamples have gcd one in every triple; the argument does not settle all semigroups whose three nonmultiplicity generators share a divisor.

Primary source checked directly: A. Zhai, *An asymptotic result concerning a question of Wilf*, Theorem 1 and Lemma 3, [arXiv:1111.2779](https://arxiv.org/pdf/1111.2779). The new gcd deduction uses only the stated lower bound, not Zhai's asymptotic theorem.

## 2. No-interior ideals and the bipartite case

Reviewed `../no_interior/clique_tree_and_bipartite_bound.md`. The graph and tree claims are valid for nonempty finite lower ideals, as intended for Apéry ideals. An independent second audit also checked Sections 1–3.

An induced cycle of length at least four repeats a coordinate class. Nested external neighborhoods make the two adjacent repeated-class vertices create a chord. Thus the graph is chordal. Its maximal cliques are exactly the maximal boxes, and the clique-tree running-intersection property gives the exact tree inclusion-exclusion formula.

Every leaf uniquely maximizes at least one coordinate, so distinct leaves use distinct coordinates and there are at most three leaves. For completeness, every leaf is among the three selected coordinate-maximum nodes; hence their minimal connecting subtree is the entire clique tree. There is no branch omitted by the median/three-arm description. Along an arm, its outward coordinate increases and the other coordinates decrease; incomparability forces strict growth of the outward coordinate between consecutive nodes.

For the bipartite moment bound, the no-interior assumption is essential: together with the bipartite pair-corner graph it implies that each color-class fibre is a rectangle. If \(\mu_A,\mu_B\) are the weighted coordinate means, moving all coordinates of a color class to its fibre top gives

\[
2\mu_A+\mu_B\le M,\qquad \mu_A+2\mu_B\le M.
\]

The factor two is exact on every finite interval \(0,\ldots,H\), including \(H=0\). Thus \(\mu\le2M/3\) has no discrete endpoint error. For an Apéry ideal,

\[
W_4\ge M/3-(m-1),
\]

which settles \(M\ge3m-3\), equivalently \(c\ge2m-2\). The complementary conductor range is contained in the published \(c\le3m\) range. Hence the entire bipartite no-interior subclass satisfies Wilf. A triangle interaction graph is outside this moment argument; the manuscript correctly leaves it unresolved.

Primary source checked directly: S. Eliahou, *Wilf's conjecture and Macaulay's theorem*, J. Eur. Math. Soc. **20** (2018), 2105–2129, DOI 10.4171/JEMS/807, [published article](https://ems.press/content/serial-article-files/32312). The theorem covers every embedding dimension and includes the endpoint \(c=3m\).

## 3. Secondary common-quotient certificate and arithmetic appendix

The completed certificate theorem assumes the paired form with a common quotient \(\langle2,2g+1\rangle\) and the secondary interior property. Its conclusion \(W_4\ge1\) has no bound on \(g\) or on semigroup invariants. It does not cover arbitrary common quotients or the primary class. The exact invariant formulas, strict integer parameter condition, normalized inequality, 1,600 nonnegative rational coefficients and sixteen exact reconstruction identities were already audited in `quotient_two_wilf_certificate.md`; this scope check found no additional issue.

Section 8's general arithmetic criterion is valid:

\[
q(A/q)^*\subseteq(a+b)+A
\iff \operatorname{lcm}(q,a)>ab\ \text{ and }\ \operatorname{lcm}(q,b)>ab.
\]

It follows from the exact boundary

\[
A\setminus((a+b)+A)
=\{ia:0\le i\le b\}\cup\{jb:1\le j<a\}.
\]

The draft incorrectly displayed \(jb=(b-1)a+(j-a)b\). The coordinator corrected it to \(jb=ba+(j-a)b\), whose two coefficients are positive when \(j\ge a+1\). The boundary set, strict lcm inequalities, and all subsequent conclusions are unchanged. The equality cases \(\operatorname{lcm}=ab\) are correctly excluded.

The unbounded one-sided quotient example is explicitly labeled one-sided, and the paired quotient-multiplicity-three example correctly demonstrates that the certificate family does not exhaust all secondary semigroups. These scope qualifications should remain in the final report.


---

# Primary background sources

- A. Zhai, *An asymptotic result concerning a question of Wilf*,
  https://arxiv.org/abs/1111.2779. The weighted lower-ideal bound is used in
  the gcd reduction.
- S. Eliahou, *Wilf's conjecture and Macaulay's theorem*,
  https://arxiv.org/abs/1703.01761. Its \(c\le3m\) theorem completes the
  conductor ranges in the bipartite subclass.
- J. R. S. Blair and B. W. Peyton, *An introduction to chordal graphs and
  clique trees*, ORNL/TM-12203, 1992,
  https://people.math.binghamton.edu/zaslav/Oldcourses/580.S13/blair-peyton.chordal-graphs-clique-trees.ornl1992.pdf.
  The clique-tree theorem supplies the standard graph-theoretic input.
- M. Hellus, A. Rechenauer and R. Waldi, *Variants on a question
  of Wilf*, https://arxiv.org/abs/1804.06141. Proposition 2.6 supplies the
  established unique full-support-corner restriction.
- C. Cisto, *On some numerical semigroup transforms*,
  https://arxiv.org/abs/2209.05803. The archive examines an existing transform
  as a conditional counterexample descent; it does not furnish a universal
  descent in this work.
- *The type and cardinality of minimal presentations of numerical
  semigroups with embedding dimension four*,
  https://arxiv.org/html/2609.04000v1. This is background for the paired
  secondary classification. The family theorem above states all of its
  own hypotheses explicitly and proves its invariant formulas directly.

The manuscript's remaining-gap statement is a statement about the scope
of these arguments. No claim is made that bounded tests establish the
unrestricted conjecture or that every theorem here is new in the literature.
