# Paired secondary semigroups with common quotient ⟨3,4,5⟩ satisfy Wilf

7 September 2026. This is a new family argument within the current research session, not an unrestricted four-generator proof. External review remains outstanding.

**Theorem.** Let A=⟨a,b⟩ and B=⟨c,d⟩ be two-generated numerical semigroups, let p,q be coprime positive integers, and suppose S=pA+qB is minimally four-generated. Suppose

A/q=B/p=R=⟨3,4,5⟩,

qR₊⊆a+b+A and pR₊⊆c+d+B.

Then W₄(S)=4n(S)−c(S)≥1.

The common quotient here has precisely the gaps 1,2. The theorem does not cover arbitrary multiplicity-three quotients.

## 1. Positive integer parameters

Write the unique gap representation

q=ab−u a−v b, 0<u<b, 0<v<a.

Because 2q is also a gap, exactly one of 2u>b and 2v>a holds. Interchanging a,b if necessary gives 2u>b. The condition that 3q has a representation using positive coefficients of both generators then implies

b/2<u<2b/3, 0<v<a/3.

Indeed if u≥2b/3 or v≥a/3, the canonical gap representation of 3q either remains a gap or reaches a pure-axis boundary. Similarly the interior representation of 4q gives 4v<a. Put

r=2b−3u>0, h=2u−b>0, z=a−4v>0.

Then r,h,v,z are positive integers and

b=2r+3h, u=r+2h, a=4v+z,
q=(2r+h)v+(r+h)z.

The condition on 5q imposes an additional restriction, but our inequality will hold on the larger domain where all four parameters are merely positive. Apply the same construction to B, using positive integers R₀,H,V,Z:

d=2R₀+3H, c=4V+Z,
p=(2R₀+H)V+(R₀+H)Z.

For completeness, the assertions about the gap boundaries can be checked without an implicit choice of representation. For any positive integer k, a positive-coefficient representation of kq exists exactly when

ceil(ku/b)+ceil(kv/a)≤k,

with a ceiling increased by one when its argument is an integer. This is obtained by choosing the least positive coefficients congruent to −ku modulo b and −kv modulo a. At k=3 and k=4 it gives the strict inequalities above.

## 2. Four normalized residue-fiber types

For each residue modulo q let Aᵢ be its least element in A and put Iᵢ={k≥0:Aᵢ+qk∈A}. Since Iᵢ contains 0 and all integers ≥3, it is one of

T={0,3,4,5,…},
I={0,2,3,4,…},
J={0,1,3,4,…},
N={0,1,2,3,…}.

Two-generator symmetry pairs a fiber K with its normalized dual

K*={k≥0:f(K)−k∉K},

where f(K) is its largest missing integer, with f(N)=−1. Here T*=J, J*=T, I*=I and N*=N. In particular the numbers of T and J fibers are equal. If α_K is the least fiber minimum Aᵢ of type K, symmetry says that the largest minimum of type K* is

F_A−q f(K)−α_K,

where F_A=ab−a−b.

For a positive gap t=ab−u₀a−v₀b, the number of s∈A with s+t∉A is u₀v₀: in the canonical representation s=i a+j b, 0≤i<b, the excluded set is exactly the rectangle i<u₀,j<v₀.

Apply this to q and 2q=ab−h a−2v b. Translation by q has one defect in each T,I,J fiber; translation by 2q has one defect in each T,J fiber. Thus, writing the numbers of T,J fibers as t and of I fibers as s,

2t+s=uv=(r+2h)v,
2t=2hv.

Consequently

#T=#J=hv, #I=rv,
Σᵢ genus(Iᵢ)=v(r+3h).

The corresponding counts for B are HV, R₀V and V(R₀+3H).

## 3. Exact genus and two conductor lower bounds

Let P=pq and X=pF_A+qF_B. The pair of residues of A modulo q and B modulo p indexes the S-residue classes modulo P. Its normalized fiber is the sumset Iᵢ+Jⱼ. The only sumsets with positive genus are

T+T (genus 2), T+I and I+T (genus 1),
T+J and J+T (genus 1), I+I (genus 1).

The residue-offset count therefore gives the exact genus

G(S)=(X+P+1)/2−pv(r+3h)−qV(R₀+3H)+E,

where

E=vV(rR₀+rH+hR₀+4hH).

This uses the general residue formula

G(S)=(X+P+1)/2−pΣgenus(Iᵢ)−qΣgenus(Jⱼ)+Σgenus(Iᵢ+Jⱼ).

We need only two conductor branches, rather than the full maximum over sixteen type pairs.

**Two concrete fiber minima.** The label ha is the least element of a residue fiber of type I, and 2vb is the least element of a fiber of type N. To see minimality, it is enough to check subtraction by q,2q,3q: since 3q∈A, any earlier element at distance kq with k≥4 would imply one of these three predecessors exists. In the canonical representation with a-coefficient between 0 and b−1, each of the following predecessors has negative b-coefficient:

ha−q=−ra+vb,
ha−2q=(−2r−h)a+2vb,
ha−3q=(h−r)a−(v+z)b;

2vb−q=−(r+h)a+3vb,
2vb−2q=ha−zb,
2vb−3q=−ra+(v−z)b.

Reducing a negative a-coefficient modulo b only decreases the b-coefficient by a, preserving negativity. Also ha+q is a gap and ha+2q∈A, so the first fiber is I; both 2vb+q and 2vb+2q belong to A, so the second is N. Thus α_I≤ha and α_N≤2vb. The same bounds hold on the B side.

Symmetry and I+I=I now give

F(S)≥X−P−pha−qHc.

Symmetry and N+N=N give

F(S)≥X+P−2pvb−2qVd.

Taking their arithmetic mean cancels P:

F(S)≥X−½[p(ha+2vb)+q(Hc+2Vd)].

Combining this bound with the exact genus gives

W₄(S)≥1+X−2P+4pv(r+3h)+4qV(R₀+3H)−4E
             −(3/2)[p(ha+2vb)+q(Hc+2Vd)].       (★)

## 4. A four-variable nonnegative polynomial

Normalize

x=r/h, y=z/v, X₀=R₀/H, Y=Z/V,
Q=2x+1+(x+1)y=q/(hv),
P₀=2X₀+1+(X₀+1)Y=p/(HV).

Let f(t)=min(t,1). Positive integrality gives

1/h≤f(x), 1/v≤f(y), 1/H≤f(X₀), 1/V≤f(Y).

After dividing the right side of (★), apart from its constant 1, by hvHV, substitution gives

W₄(S)≥1+hvHV Φ(x,y,X₀,Y),

Φ=P₀ A(x,y)+Q A(X₀,Y)−4(xX₀+x+X₀+4),

A(x,y)=4x+xy+y/2+8−f(x)(4+y)−f(y)(2x+3).

We prove Φ≥0 on the relaxed domain x,y,X₀,Y≥0. Split each variable at 1, yielding sixteen regions. For a lower variable use t=T∈[0,1], and for an upper variable use t=1+T, T≥0. The resulting polynomial has degree at most one in each of the four variables. Expand bounded coordinates in the degree-one Bernstein basis {1−T,T}, and leave unbounded coordinates in the ordinary power basis {1,T}. Every basis function is nonnegative.

The sixteen coefficients on each region are all nonnegative. The exact smallest coefficients for the flags (x,y,X₀,Y), with 0=lower and 1=upper, are:

| Flags | Minimum |
|---|---:|
| 0000 | 0 |
| 0001 | 11/2 |
| 0010 | 7 |
| 0011 | 7 |
| 0100 | 11/2 |
| 0101 | 1 |
| 0110 | 9/2 |
| 0111 | 3/2 |
| 1000 | 7 |
| 1001 | 9/2 |
| 1010 | 7 |
| 1011 | 6 |
| 1100 | 7 |
| 1101 | 3/2 |
| 1110 | 6 |
| 1111 | 2 |

`ordinary_three_certificate.py` constructs Φ using exact rational arithmetic, performs all sixteen conversions, verifies all 256 coefficients, and expands each representation back to the original polynomial. The complete rational data are in `ordinary_three_certificate.json`. This is a finite exact identity certificate, not a parameter search. Consequently Φ≥0, and (★) proves W₄(S)≥1. ∎

## 5. Independent checks and scope

`ordinary_three_checks.py` computes the exact fiber formulas and separately computes semigroup invariants using shortest paths modulo the multiplicity. One hundred minimally four-generated examples with coprime p,q passed the exact genus and conductor comparisons and the lower bound. These checks support the derivation but are not the argument for the unbounded family.

The previously uncovered example A=⟨5,7⟩, q=9, B=⟨5,8⟩, p=11 gives S=⟨45,55,72,77⟩. Its exact invariants are F=395, genus 225 and W₄=288. The intermediate bound (★) already gives W₄≥67.

This theorem extends the completed common-quotient multiplicity-two family to the next ordinary quotient. General quotients of multiplicity three, ordinary quotients of multiplicity at least four, and unrestricted primary four-generator semigroups remain outside these two family arguments.
