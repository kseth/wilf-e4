# Wilf for paired secondary semigroups with quotient ⟨3,3g+1,3g+2⟩

7 September 2026. Family proof with exact rational certificates and a completed independent in-session audit. External review remains outstanding. This is not the unrestricted four-generator conjecture.

**Theorem.** Let A=⟨a,b⟩ and B=⟨c,d⟩ be two-generated numerical semigroups, p,q coprime, and S=pA+qB minimally four-generated. Assume

A/q=B/p=R_g=⟨3,3g+1,3g+2⟩,
q(R_g)₊⊆a+b+A, p(R_g)₊⊆c+d+B.

Then W₄(S)≥1 for every integer g≥1. The case g=1 is proved separately in `ordinary_three_theorem.md`. We prove g≥2 below. The quotient has genus 2g, so this family has unbounded quotient genus.

## 1. Complete positive parameterization for g≥2

As in the ordinary-three proof, orient the unique gap representation q=ab−ua−vb so that 2u>b. Since q and 2q are gaps but 3q has an interior representation, put

r=2b−3u>0, h=2u−b>0, s=a−3v>0.

Then

b=2r+3h, u=r+2h, a=3v+s,
q=rv+(r+h)s, 3q=ra+sb.

The two gap progressions have the exact representations

(3j+1)q=ab−(r+2h−jr)a−(v−js)b,
(3j+2)q=ab−(h−jr)a−(2v−js)b.

Until either displayed coefficient becomes nonpositive these are canonical gap representations; at the first nonpositive coefficient the value is represented in A and all later values in that progression are represented by adding 3q. Thus the numbers of gaps in the two progressions are respectively

min(ceil(1+2h/r),ceil(v/s)),
min(ceil(h/r),ceil(2v/s)).

Both equal g. For g≥2 this forces ceil(h/r)=ceil(v/s)=g. Indeed if the second minimum attained g through ceil(2v/s) while ceil(h/r)>g, then ceil(v/s)≤ceil(g/2)<g, contradicting the first minimum. Once ceil(h/r)=g, ceil(1+2h/r)≥2g−1>g, so the first minimum forces ceil(v/s)=g. The strict interior conditions at 3g+1 and 3g+2 exclude the upper endpoints. Therefore

h=(g−1)r+α, v=(g−1)s+β,
0<α<r, 0<β<s.

Consequently

a=(3g−2)s+3β,
b=(3g−1)r+3α,
q=(2g−1)rs+rβ+sα.

The same formulas describe B with positive integers R,T,α′,β′, with 0<α′<R and 0<β′<T. Its quotient divisor is p. Normalize

x=α/r, y=β/s, z=α′/R, w=β′/T,
Q=2g−1+x+y=q/(rs), P=2g−1+z+w=p/(RT),
A₀=3g−2+3y=a/s, B₀=3g−1+3x=b/r,
C₀=3g−2+3w=c/T, D₀=3g−1+3z=d/R.

## 2. Exact L-shape of residue minima

Use canonical coordinates ia+jb with 0≤i<b, j≥0. Such a label is the least in its q-residue exactly when none of its predecessors at distances q,2q,3q belongs to A. These three tests suffice because 3q∈A. The gap representations of q and 2q say that absence of the first two predecessors is exactly

i<r+h and j<v+s.

On this rectangle, absence of the third predecessor is i<r or j<s. Thus the residue minima form the disjoint L-shape

0≤i<r+h, 0≤j<s,

or

0≤i<r, s≤j<v+s.

Its size (r+h)s+rv=q also verifies the count.

A normalized fiber has the form

I(H,K)=3N ∪(3H+1+3N)∪(3K+2+3N),

with 0≤H,K≤g. At the minimum ia+jb the two thresholds are

H=max(0,min(ceil((r+2h−i)/r),ceil((v−j)/s))),
K=max(0,min(ceil((h−i)/r),ceil((2v−j)/s))).

Evaluating these on the two rectangles gives the following distribution, divided by rs. Every listed contribution is additive; the ranges do not overlap beyond the explicitly combined entries:

| Threshold pair | Normalized number of fibers |
|---|---:|
| (g,g) | xy |
| (g,k), 0≤k≤g−1 | y |
| (g−1,g) | x |
| (g−1,g−1) | 1−xy |
| (g−1,k), 0≤k≤g−2 | 1−y |
| (h₀,g), 1≤h₀≤g−2 | x |
| (h₀,g−1), 1≤h₀≤g−2 | 1−x |
| (0,g) | xy |
| (0,g−1) | 1−xy |

An empty range contributes nothing. The total is Q. For 1≤j<g, both marginal tail counts, divided by rs, are Q−j. At j=g they are

Pr-count(H≥g)/(rs)=y(g+x),
Pr-count(K≥g)/(rs)=x(g−1+2y).

In particular the normalized sum of fiber genera is

G_A=(g−1)(3g−2)+(3g−3)x+(3g−2)y+3xy.

Write G_B for the analogous expression in z,w.

## 3. A genus upper bound from the marginal tails

For two normalized fibers, direct residue addition gives

I(H,K)+I(H′,K′)=I(min(H,H′,K+K′+1), min(K,K′,H+H′)).

Its genus is at most min(H,H′)+min(K,K′). Therefore the normalized sum of genera of all paired sum fibers is at most

Ē=2[(g−1)PQ−g(g−1)(P+Q)/2+g(g−1)(2g−1)/6]
   +yw(g+x)(g+z)+xz(g−1+2y)(g−1+2w).

This follows by summing the products of the two marginal tail counts at each threshold j=1,…,g.

Set X=p(ab−a−b)+q(cd−c−d) and P_abs=pq. The exact residue genus identity from the ordinary-three proof consequently gives

G(S)≤(X+P_abs+1)/2−p(rs)G_A−q(RT)G_B+(rsRT)Ē.       (1)

## 4. Two self-dual fibers and a Frobenius lower bound

The symmetric numerical semigroup I(t,2t) has Frobenius number 6t−1 and is self-dual. Similarly I(2t+1,t) is symmetric and self-dual, with Frobenius number 6t+1. Each is closed under its own addition.

If g=2t is even, the distribution contains self-dual fibers

U=I(t,g), f(U)=6t−1,
V=I(g−1,t−1), f(V)=6t−5.

The L-shape supplies actual minima of these types with labels at most

ℓ_U=((t−1)s+β)b,
ℓ_V=(tr+α)a+βb.

For g=2 this remains valid, including the boundary index t−1=0.

If g=2t+1 is odd, the self-dual fibers are

U=I(g,t), f(U)=6t+1,
V=I(t,g−1), f(V)=6t−1,

with labels at most

ℓ_U=(tr+α)a,
ℓ_V=αa+(ts+β)b.

Define L_A=(ℓ_U+ℓ_V)/(2rs). Thus

L_A=[(t+x)A₀+(t−1+2y)B₀]/2 if g=2t,
L_A=[(t+2x)A₀+(t+y)B₀]/2 if g=2t+1.

Define L_B analogously.

Two-generator symmetry sends a minimum α_I of a self-dual fiber I to a maximum minimum F_A−q f(I)−α_I. Since I+I=I, pairing the largest such minima from A and B yields

F(S)≥X−P_abs f(I)−pα_I^A−qα_I^B.

Apply this for U and V and average. Their Frobenius numbers have mean 3g−3, so

F(S)≥X−P_abs(3g−3)−p(rs)L_A−q(RT)L_B.       (2)

## 5. Exact positive polynomial certificate

Let f(t)=min(t,1−t) on [0,1]. Positive integrality gives

1/r≤f(x), 1/s≤f(y), 1/R≤f(z), 1/T≤f(w).

Combining (1) and (2) in W₄=3(F+1)−4G and using these inverse-integer bounds yields

W₄(S)≥1+rsRT Ψ,

Ψ=P A₀B₀+Q C₀D₀−2PQ
 −3[PQ(3g−3)+P L_A+Q L_B]
 +4P G_A+4Q G_B−4Ē
 −P[f(x)A₀+f(y)B₀]−Q[f(z)C₀+f(w)D₀].

It remains to show Ψ≥0 for g≥2, 0≤x,y,z,w≤1. For even g write g=2t+2, and for odd g write g=2t+3, with t≥0. Split each of x,y,z,w into its lower and upper half, parametrized by (ε+T)/2, T∈[0,1]. This yields 32 rational polynomials.

Expand each in the ordinary power basis in the unbounded parameter t and the Bernstein basis in the four bounded variables. `quotient_three_progression_certificate.py` constructs every polynomial, converts every coefficient exactly, checks that all 2,048 coefficients are nonnegative, and reconstructs all 32 original polynomials exactly. No floating-point computation appears in this certificate. For the even regions the smallest coefficients are 44, 899/16, or 267/4; for every odd region the smallest coefficient is 272/3. All basis functions are nonnegative on their domains, so Ψ≥0. Therefore W₄(S)≥1. ∎

## Verification and remaining scope

`quotient_three_progression_checks.py` independently computes the q-residue minima of the two-generator sides and their exact fiber types, and compares the resulting distribution with Section 2. It also computes S invariants independently using shortest paths and checks the derived lower bound. The checked quotient parameters include g=2,3,4,5,8,12, with 60 minimally four-generated paired examples in total.

The theorem treats the entire common-quotient family R_g=⟨3,3g+1,3g+2⟩ under the paired interior conditions. It does not treat arbitrary multiplicity-three quotients, whose two nonzero Apéry thresholds can differ, or unrestricted four-generator semigroups.

For a concrete case beyond the earlier six-point and gcd-triple exclusions, g=2 gives S=⟨176,253,288,299⟩, with every triple gcd equal to one, final-window cardinality eight, and W₄=1942. Its multiplicity 176 is also inside the separate residual range m≤1836. For g=12, S=⟨10295,17111,26680,26751⟩ has every triple gcd one, final-window cardinality 36, and W₄=1314401. Exact final-window diagnostics are in `quotient_three_progression_final_windows.json`.

The independent audit is `../secondary_audit/audit_quotient_three_progression.md`. Its separate verifier independently reproduced all 2,048 coefficients, confirmed nonnegativity, and passed 7,776 rational reconstruction checks. The proof of parameter completeness, residue L-shape, full threshold distribution, and both parity-dependent self-dual fiber witnesses was also checked independently.
