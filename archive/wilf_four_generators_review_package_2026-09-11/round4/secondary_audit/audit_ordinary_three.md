# Independent audit: paired common quotient ⟨3,4,5⟩

7 September 2026.

**Verdict:** the stated restricted-family theorem is supported by a complete analytic derivation and an independently reconstructed exact rational certificate. No unresolved inference was found in this audit. This does not prove Wilf for general four-generator semigroups, or for all common quotients of multiplicity three.

The audited draft is `round4/secondary/ordinary_three_theorem.md`. Its hypotheses are two-generated numerical semigroups A=⟨a,b⟩, B=⟨c,d⟩; coprime positive p,q; minimally four-generated S=pA+qB; common quotient A/q=B/p=⟨3,4,5⟩; and qR₊⊆a+b+A, pR₊⊆c+d+B. The conclusion is W₄(S)≥1.

## 1. The positive parameter reduction is complete

Since q is a positive gap, write q=ab−ua−vb with 0<u<b and 0<v<a. The positivity of q gives u/b+v/a<1. If both 2u≤b and 2v≤a, then 2q=(b−2u)a+(a−2v)b lies in A, contradicting the quotient. Both strict reverse inequalities are impossible by the preceding strict sum. Consequently exactly one of 2u>b or 2v>a holds. Interchange a and b so that 2u>b and 2v<a.

A positive-coefficient representation of kq exists exactly when

floor(ku/b)+floor(kv/a)≤k−2.

Indeed the two coefficients must be ℓb−ku and (k−ℓ)a−kv for an integer ℓ, and their strict positivity is exactly floor(ku/b)+1≤ℓ≤k−floor(kv/a)−1. Thus the interior condition for 3q forces u<2b/3 and v<a/3. The condition for 4q then forces v<a/4. All inequalities are strict, including boundary cases where ku/b or kv/a is an integer.

The quantities r=2b−3u, h=2u−b, v and z=a−4v are positive integers. Solving gives

a=4v+z, b=2r+3h, u=r+2h,
q=(2r+h)v+(r+h)z.

The same construction independently applies to B. The additional condition on 5q is not included in the later polynomial domain, which is a valid enlargement. It must still be retained in the theorem: arbitrary positive r,h,v,z need not give the specified common quotient.

## 2. Residue fibers and genus

A normalized residue fiber contains 0 and all integers ≥3, and so has exactly one of the four forms T=N\{1,2}, I=N\{1}, J=N\{2}, N. These are ideals over R; J is not itself a semigroup, and no closure under J+J is assumed.

Two-generator symmetry sends a type K fiber of minimum s to a type K* fiber of minimum F_A−q f(K)−s, where f(T),f(I),f(J),f(N)=(2,1,2,−1), and the dual permutation is T↔J, I↔I, N↔N. This follows by reflecting membership about F_A, including the negative positions relative to the fiber minimum.

For any positive gap t=ab−u₀a−v₀b, the labels s∈A for which s+t∉A are exactly i a+j b with 0≤i<u₀ and 0≤j<v₀. This follows by reducing the a coefficient to 0,…,b−1, and proves the count u₀v₀ without multiplicities.

The defects under translation by q in types T,I,J,N are (1,1,1,0), and those under 2q are (1,0,1,0). Since 2q=ab−ha−2vb and symmetry gives #T=#J, this proves

#T=#J=hv, #I=rv, sum of fiber genera=v(r+3h).

The sumset genera, in type order T,I,J,N, are exactly

| + | T | I | J | N |
|---|---:|---:|---:|---:|
| T | 2 | 1 | 1 | 0 |
| I | 1 | 1 | 0 | 0 |
| J | 1 | 0 | 0 | 0 |
| N | 0 | 0 | 0 | 0 |

Coprimality of p,q identifies pairs of residue classes with the pq residue classes of S. Their normalized fibers are exactly the sumsets of the corresponding A and B fibers. Counting the initial residue offsets gives (p−1)(q−1)/2, so the exact genus formula in the draft follows:

G=(X+pq+1)/2−pv(r+3h)−qV(R₀+3H)+vV(rR₀+rH+hR₀+4hH),

where X=pF_A+qF_B. This derivation does not rely on the sample checks.

## 3. Exact fiber minima and Frobenius formulas

The draft needs only upper bounds α_I≤ha and α_N≤2vb. Both labels are actual fiber minima of the asserted type. It suffices to rule out their predecessors at distances q,2q,3q: any predecessor at distance k≥4 gives one of these after adding a nonnegative multiple of 3q. Each of the six predecessor identities in the draft has negative b coefficient when normalized to an a coefficient in 0,…,b−1. Also ha+q is a gap, ha+2q belongs to A, and both 2vb+q and 2vb+2q belong to A. This verifies every membership assertion used in the proof.

The stronger exact type-minimum vector used by the check script is also correct:

(α_T,α_I,α_J,α_N)=(0,ha,vb,min(2vb,ha+vb)).

To establish this, write s=i a+j b canonically. The two colon membership conditions are

s+q∈A iff i≥u or j≥v;
s+2q∈A iff i≥h or j≥2v.

A label of type I must therefore lie in ha+A, and one of type J in vb+A. A label of type N lies in ua+A, 2vb+A or ha+vb+A. Since ua−2vb=2hv+(r+2h)z>0, the last minimum is min(2vb,ha+vb). The q,2q,3q predecessors of vb are respectively

−(r+h)a+2vb, ha−(v+z)b, −ra−zb,

and those of ha+vb are

−ra+2vb, −(2r+h)a+3vb, (h−r)a−zb.

Their canonical b coefficients are all negative. The relevant positive shifts have the claimed memberships by the colon criteria. Thus these labels really are residue minima, rather than merely labels occurring higher in a fiber.

For the exact formula, let i,j index the original types. Reflection gives the largest fiber minima in the dual types, and their sumset contributes its Frobenius position. Hence

F(S)=X−minᵢⱼ[pαᵢ+qβⱼ+pq(fᵢ+fⱼ−f(Kᵢ*+Kⱼ*))].

This has exactly the signs and indexing in `ordinary_three_checks.py`.

For the theorem, the I+I and N+N branches alone give

F≥X−pq−pha−qHc,
F≥X+pq−2pvb−2qVd.

Their average is a valid lower bound on F. Combining it with W₄=3(F+1)−4G gives the inequality (★) in the draft, including the additive constant 1. No inequality reverses in this step.

## 4. Normalization and exact positivity certificate

Put x=r/h, y=z/v, X₀=R₀/H, Y=Z/V. After dividing (★) minus 1 by hvHV, its expression before replacing reciprocal integer parameters is

P₀[(4+y)(2x+3)−(4+y)/h−(2x+3)/v]
+Q[(4+Y)(2X₀+3)−(4+Y)/H−(2X₀+3)/V]
−2P₀Q+4P₀(x+3)+4Q(X₀+3)−4(xX₀+x+X₀+4)
−(3/2)[P₀(4x+y+10)+Q(4X₀+Y+10)],

where Q=2x+1+(x+1)y, P₀=2X₀+1+(X₀+1)Y. Collecting yields the draft's Φ, with reciprocal parameters still in place of f(x),f(y),f(X₀),f(Y). The coefficients of all four reciprocal parameters are nonpositive. Since r,h,v,z,R₀,H,V,Z are positive integers, 1/h≤min(x,1) and the three analogous inequalities hold. Thus the replacement gives a lower bound in the required direction.

On each of the sixteen regions split at coordinate 1, Φ is separately affine in all four transformed coordinates. An independent verifier reconstructs its mixed Bernstein/power coefficients using endpoint evaluations and finite differences, without importing the original polynomial code. All 256 coefficients agree exactly with the proposed certificate and are nonnegative. The verifier also checks the collection identity at all 256 Boolean vertices of its eight separately affine formal variables, proving that identity, and independently reconstructs every region polynomial, with additional rational off-grid evaluations.

Files: `verify_ordinary_three.py`, `independent_certificate.json`. Run from the workspace root:

`python3 round4/secondary_audit/verify_ordinary_three.py`

The original rational certificate was also rerun successfully. These finite exact verifications, together with the analytic reductions above, prove the stated restricted-family result. They do not amount to enumerating the unrestricted four-generator search space.
