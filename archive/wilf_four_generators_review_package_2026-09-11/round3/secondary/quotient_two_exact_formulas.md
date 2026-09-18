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
