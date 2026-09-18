# Independent audit of the unbounded R_g quotient family

7 September 2026.

**Verdict:** no gap was found in the proof for paired common quotient R_g=⟨3,3g+1,3g+2⟩ under the paired interior hypotheses. The case g≥2 has a complete analytic derivation and a separately reconstructed exact certificate. Together with the earlier g=1 audit, the stated family theorem W₄(S)≥1 is supported for every positive integer g. This remains a restricted-family theorem; it does not imply the unrestricted four-generator conjecture. The quotient genus is 2g.

Audited draft: `round4/secondary/quotient_three_progression_theorem.md`.

## 1. Parameter completeness and boundary cases

Orient q=ab−ua−vb so that 2u>b. Since 3q has an interior representation, the same strict-floor argument as in the g=1 audit yields

r=2b−3u>0, h=2u−b>0, s=a−3v>0,
a=3v+s, b=2r+3h, q=rv+(r+h)s.

In particular 3q=ra+sb. The two gap progressions are

(3j+1)q=ab−(r+2h−jr)a−(v−js)b,
(3j+2)q=ab−(h−jr)a−(2v−js)b.

Each displayed coefficient stays below its respective generator bound while positive. If one becomes nonpositive, the label belongs to A; all later labels of that progression belong to A by adding 3q. Consequently the numbers of gaps are the two minima of ceilings given in the draft.

Both minima equal g. The second forces ceil(h/r)≥g and ceil(2v/s)≥g. If ceil(h/r)>g, it forces ceil(2v/s)=g, hence ceil(v/s)≤ceil(g/2)<g for g≥2, contradicting the first minimum. Thus ceil(h/r)=g. Since h/r>g−1, ceil(1+2h/r)≥2g−1>g, and the first minimum forces ceil(v/s)=g.

Write h=(g−1)r+α and v=(g−1)s+β. At this point 0<α≤r and 0<β≤s. The strict upper inequalities require an argument, rather than just membership at the first nongap:

- If β=s, the first nongap (3g+1)q is a pure a multiple whose a coefficient is strictly between 0 and b. It has no positive-coefficient representation using both a and b, contradicting the interior hypothesis.
- If α=r, the first nongap (3g+2)q is a pure b multiple whose b coefficient is strictly between 0 and a. Again there is no interior representation.

Therefore 0<α<r and 0<β<s, with no parity exception. This proves the parameter domain in the draft is necessary and complete. The same independent orientation can be used on B. In particular r,s,R,T≥2, and the reciprocal integer bounds used later are legitimate.

## 2. Residue minima and the exact fiber distribution

The three relations

q=(r+h)a−vb,
2q=−ha+(v+s)b,
3q=ra+sb

give an independent way to prove the L-shape. If a nonnegative coordinate pair has i≥r+h, j≥v+s, or both i≥r and j≥s, respectively, one can replace its label by a strictly smaller label in the same q residue, using the displayed relation. Repeating terminates inside

T₀={0≤i<r+h, 0≤j<s} ∪ {0≤i<r, s≤j<v+s}.

Every residue modulo q is represented by A, since A is numerical. The set T₀ has exactly (r+h)s+rv=q coordinate pairs. Therefore its labels are pairwise distinct in residue and are precisely the least residue representatives. This argument avoids assuming that the coordinate shape is already a transversal.

A normalized fiber is I(H,K)=3N∪(3H+1+3N)∪(3K+2+3N), with H,K between 0 and g. Applying the canonical colon criteria to the two gap progressions gives exactly the two ceiling formulas in the draft.

The complete distribution can also be derived by horizontal bands:

- On 0≤j<β, H=g. The i interval of width α has K=g; each of the remaining g intervals has width r and K=0,…,g−1.
- On β≤j<s+β, H=g−1. Splitting at j=s accounts for the two different widths of T₀. This gives normalized counts x for K=g, 1−xy for K=g−1, and 1−y for each K=0,…,g−2.
- For each H=1,…,g−2, the corresponding band has height s and width r; its split at i=α gives normalized counts x and 1−x at K=g and g−1.
- On v≤j<v+s, H=0. Splitting at j=v+β and i=α gives counts xy at K=g and 1−xy at K=g−1.

These bands prove every entry of the proposed table and remain valid when g=2, for which the intermediate range is empty. They give total count Q and the marginal tail counts Q−j for 1≤j<g, y(g+x) at H≥g, and x(g−1+2y) at K≥g. Thus the closed expression G_A in the draft is exact.

## 3. The genus inequality has the correct direction

Residue addition gives

I(H,K)+I(H′,K′)=I(min(H,H′,K+K′+1),min(K,K′,H+H′)).

The extra terms correspond to adding two residue-2 positions or two residue-1 positions. Therefore the genus is at most min(H,H′)+min(K,K′). Summing each minimum by its marginal tails gives exactly Ē in the draft. The residue formula then yields the stated upper bound on G(S), with all scale factors rs and RT in the correct places.

Because W₄=3(F+1)−4G, an upper bound on G is the useful direction. The proof does not mistake Ē for the exact double sum.

## 4. Self-duality, parity, and the conductor witnesses

I(t,2t) is a numerical semigroup of genus 3t and Frobenius number 6t−1; I(2t+1,t) is a numerical semigroup of genus 3t+1 and Frobenius number 6t+1. Their closure follows respectively from K≤2H and H≤2K+1. The equality F=2G−1 implies symmetry, so both are self-dual under the residue reflection. Each also satisfies I+I=I.

For g=2t, the two chosen types I(t,g) and I(g−1,t−1) are exactly these forms, with Frobenius numbers 6t−1 and 6t−5. Their proposed coordinate witnesses are

(i,j)=(0,(t−1)s+β),
(i,j)=(tr+α,β).

Both lie in T₀, and direct substitution in the threshold formulas gives precisely the asserted types. This includes t=1: the second type is I(1,0), a valid symmetric numerical semigroup with Frobenius number 1.

For g=2t+1≥3, the types I(g,t) and I(t,g−1) have Frobenius numbers 6t+1 and 6t−1. Their witnesses are

(i,j)=(tr+α,0),
(i,j)=(α,ts+β).

Again both lie in T₀ and have the stated threshold pairs. Thus every witness is an actual residue minimum; the proof needs only that the smallest minimum of the type is no larger than this witness.

Reflection of the largest minima of a self-dual type gives the branch F(S)≥X−pq f(I)−pα_I^A−qα_I^B. The two branch Frobenius numbers average to 3g−3 in either parity. Averaging their lower bounds proves equation (2), with no need to assume the witnesses are the smallest minima of their types.

## 5. Normalization and the independent 2,048-coefficient certificate

Combining the upper genus bound with the lower Frobenius bound gives the displayed Ψ after division by rsRT. In the normalized term X/(rsRT), the only inverse integer terms are

−P[A₀/r+B₀/s]−Q[C₀/R+D₀/T].

Positive integrality of α,r−α,β,s−β and their B analogues gives the four bounds by min(x,1−x), etc. Every inverse-integer coefficient is negative, so replacing reciprocals by those upper bounds gives a lower bound on W₄, as required.

For a fixed parity and a fixed half-box, Ψ has degree at most three in the nonnegative parameter t and degree at most one separately in each of the four bounded coordinates. These degree bounds follow term by term from the displayed formula; no numerical degree detection is needed.

The independent verifier evaluates Ψ at the sixteen bounded corners and interpolates its cubic in t from t=0,1,2,3. If the forward differences are d₀,d₁,d₂,d₃, the ordinary power coefficients are

d₀, d₁−d₂/2+d₃/3, d₂/2−d₃/2, d₃/6.

Since the bounded coordinates are separately affine, corner values are exactly their degree-one Bernstein coefficients. This reconstructs all 2,048 coefficients without importing the original polynomial class or conversion routine. Every coefficient agrees with the proposal, and every coefficient is nonnegative. The interpolation nodes and the proved degree bounds already establish the exact polynomial identity; additional rational off-grid reconstruction checks also pass.

Files:

- `verify_quotient_three_progression.py`
- `independent_progression_certificate.json`

Run from the workspace root:

`python3 round4/secondary_audit/verify_quotient_three_progression.py`

The original certificate was also rerun successfully. This completes the audit of the infinite family, without treating sample enumeration as a proof or extending its hypotheses to arbitrary multiplicity-three quotients.
