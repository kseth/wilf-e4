# From the no-interior weighted certificate to all paired secondary semigroups

7 September 2026 research audit. This note checks mathematical implications and the mathematical domination implemented by the dynamic program. It does not independently traverse the saved interval tree. The tree and the earlier continuous/phase inputs must pass their separate audits before the resulting Wilf theorem is claimed.

## 1. Exact arithmetic implication of the interval target

Let S=<m,a1,a2,a3> be minimally four-generated with m its multiplicity, and let T be a preferred Apéry exponent ideal. Write N=|T|=m to distinguish cardinality from the normalized maximum. Relabel the other generators so A=a1<a2<a3. Every coordinate unit vector belongs to T: a minimal generator cannot have its predecessor by m in S. Put

w=(1,b,c)=(a1,a2,a3)/A, H=max_T w.x,
D=3NH-4 sum_T w.x.

The exact Apéry identity is

    m W4 = A D - m(m-1).                                      (1)

Suppose T has no full-support minimal excluded point and m>=30. Assume for contradiction W4<=0. Then D<=m(m-1)/A<m-1, since A>m. The previously proved continuous no-interior theorem and summed phase inequality, applied with kappa=D/(mH) and v=1/H, imply

    H < 12+sqrt(137) < 24.                                    (2)

This is the same argument as the prior discrete bridge; its only arithmetic input is kappa<v. All coordinates occur in T, so 1<=b<=c<=H.

If H<5, every exponent in T has total degree at most four, since all three normalized weights are at least one. The exact central-box/arm cardinality bound for no-interior ideals of total degree at most four is 29. Thus m>=30 implies H>=5.

Consequently all parameters lie in the interval certificate domain

    1<=b<=c<=H, 5<=H<=24.

The target proved by that certificate is

    N-D<=1, equivalently D>=N-1.                              (3)

Equations (1) and (3) give

    m W4 >= (A-m)(m-1) > 0,

contradicting W4<=0. Therefore, once the interval certificate is verified, every no-interior four-generator semigroup with m>=30 has W4>0.

There is no limiting or equality exception: A>=m+1, m>=30, and the conclusion is strict. The certificate includes H=5; equation (2) places H strictly below 24. The small-multiplicity range m<=29 is not settled by this argument alone.

## 2. Paired interior conditions give a critical pure relation

Let

    S=p<a,b>+q<c,d>, a<b, c<d,
    gcd(a,b)=gcd(c,d)=gcd(p,q)=1,

and suppose all four displayed generators are minimal. Assume the paired interior conditions

    pz in <c,d> => qz-a-b in <a,b>,
    qz in <a,b> => pz-c-d in <c,d>, for z>0.

These imply the equal quotient R=<a,b>/q=<c,d>/p.

Assume the multiplicity is pa; then the partner generator is pb and a(pb)=b(pa). This is its first critical multiple. Indeed if r<a and r(pb)=x(pa)+q beta with x>=0 and beta in <c,d>, coprimality gives beta=pz and rb-xa=qz for z>=0. For z=0, coprimality of a,b gives a|r, impossible. For z>0, the first interior condition gives qz-a-b in <a,b>. But ab-qz=(a-r)b+xa also belongs to <a,b>. Their sum is ab-a-b, the Frobenius number of <a,b>, a contradiction. The case in which the multiplicity is qc is identical.

## 3. A first critical pure relation excludes every full-support corner

Suppose a nonmultiplicity generator B has first critical multiple kB=ell m. For 0<=r<k, rB has a unique factorization in the full generating set: cancelling a common B coefficient in an alternative would yield a smaller critical multiple. Each such rB is Apéry and its exponent lies in every preferred ideal; k e_B is excluded. Thus this axis has exactly k points.

Suppose p=(x,y,z)>0 coordinatewise were a minimal excluded exponent, with x corresponding to B. Its preferred residue representative has disjoint support from p. To prove this directly, a shared positive coordinate could be cancelled, producing two distinct elements of T with the same residue; both would belong to T by the lower-ideal property and minimality of p. Hence its representative is zero, and

    xB+yC+zD = t m.

Since p-e_C belongs to T, 1<=x<k. Both (0,y,z) and (k-x,0,0) belong to T, and they are distinct. Their residues agree because kB is a multiple of m:

    yC+zD == -xB == (k-x)B mod m.

This contradicts residue injectivity. Thus every paired secondary semigroup satisfying Section 2 has no full-support preferred Apéry corner. No choice of term order is needed beyond the ordinary preferred lower-ideal construction.

## 4. Common quotient multiplicity at least three forces m>=35

The interior conditions imply q>b and p>d. For example let h=gcd(a,q). The integer a/h belongs to R. Hence (q/h)a belongs to a+b+<a,b>. If q/h<=b, an equality

    (q/h)a=(u+1)a+(v+1)b

would force q/h-u-1 to be a positive multiple of b, impossible. Thus q/h>b and q>b; similarly p>d.

Suppose the multiplicity of R is at least three. Then q and 2q are gaps of <a,b>, and p and 2p are gaps of <c,d>. We claim a>=5. If a<=4, let k in {0,...,a-1} be determined by q==kb mod a. Because q>b and q is a gap, k>=2: the cases k=0,1 would already represent q in <a,b>. The only possibilities are

- a=3,k=2, in which 2q==b mod 3;
- a=4,k=2, in which 2q==0 mod 4;
- a=4,k=3, in which 2q==2b mod 4.

In all three cases 2q>2b supplies a nonnegative representation in <a,b>, a contradiction. Thus a>=5. Identically c>=5. Since b>=a+1, d>=c+1, q>=b+1 and p>=d+1,

    m=min(pa,qc)>=(5+2)*5=35.                                (4)

Therefore the m>=30 no-interior theorem alone settles every secondary semigroup whose common quotient has multiplicity at least three. No enumeration at m=20,...,29 is needed for this implication.

The lower bound 35 is sharp: S=<35,40,48,49>=8<5,6>+7<5,7> satisfies the paired interior conditions and has common quotient <3,4,5>. Its Frobenius number is 205, genus 127 and W4=110. The attached exact checker verifies these data and the degree-four maximum 29 independently.

## 5. The other common quotients are already covered

If R has multiplicity two, R=<2,2g+1> for some g>=1. The complete paired-quotient theorem for that unbounded family was proved in the prior checkpoint; it gives W4>=1, including all its small-multiplicity cases.

If R has multiplicity one, R=N, so q belongs to <a,b> and p belongs to <c,d>. This is a gluing of two symmetric two-generator semigroups and is itself symmetric; hence W4=c(S)>0. One may verify the symmetry without citing a gluing theorem. The Apéry sets modulo q and p have maxima F_A+q and F_B+p. Their paired sums form the Apéry set of S modulo pq, so

    F_S=pF_A+qF_B+pq.

The corresponding residue-sum genus identity, with G_A=(F_A+1)/2 and G_B=(F_B+1)/2, gives G_S=(F_S+1)/2. Therefore W4=3(F_S+1)-4G_S=F_S+1=c(S)>0.

Thus, conditional only on successful verification of the new weighted certificate and its stated prior inputs, all paired secondary semigroups satisfy strict Wilf. This implication does not settle primary semigroups with a full-support preferred Apéry corner.


## 6. Additional check of the interval dynamic program

I read `../weight_arrangement/interval_certificate.py` line by line. For a parameter box, admissibility is relaxed using its lower coordinate weights and upper height. Every actual feasible ideal therefore remains feasible for the upper-bound DP. The objective is the sum of point scores `4w.x-3H+1`; replacing its weights by upper weights and H by the lower height increases every score.

For a rectangle `[0,b] x [0,c]` in the layer at outward level t, the score sum is exactly its cardinality times `4w_axis*t+2w_j*b+2w_k*c-3H+1`. For the central box it is its cardinality times `2w.center-3H+1`. These agree with the source.

The DP can stop a horn, choose its current cap rectangle and continue at the next level with that rectangle's caps, or decrease either current cap. Thus future rectangular sections are nested, and every allowed nested horn occurs in the recurrence. All three coordinate index orders match the central-box horn calls. Empty arms are allowed by the zero option.

The separate continuous-leaf condition is `H>=2(1+b+c)+3`. The proved continuous thickening inequality gives `D/N>=H/3-2(1+b+c)/3>=1`, hence `N-D<=0`, which is stronger than the target `N-D<=1`. The interval implementation uses the lower height and upper sum of weights, so its leaf condition is valid throughout the box.

This analytic check does not assert that all saved leaves satisfy their recorded bounds or that their tree covers the initial domain. Those are the explicit duties of the independent tree verifier.
