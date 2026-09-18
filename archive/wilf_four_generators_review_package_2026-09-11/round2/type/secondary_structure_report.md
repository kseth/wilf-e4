# Secondary four-generated semigroups: a sharper structural reduction

Date: 5 September 2026. This establishes structural facts and excludes tempting shortcuts. It does not establish Wilf for the unrestricted secondary class.

## 1. Pure critical pairs eliminate all interior corners

**Theorem.** Suppose S=⟨m,A,B,C⟩ is minimally four-generated, m is its multiplicity, and a A=b m for positive integers a,b, where a is the least positive integer with a A∈⟨m,B,C⟩. No criticality assumption is made on b for the base m. Then every preferred Apéry factorization lower ideal T with respect to m has no full-support minimal excluded point.

**Proof.** For 0≤r<a, the element rA has no alternative factorization in the full generating set. Indeed, cancelling a shared A coefficient from an alternative factorization would give a positive multiple sA, s≤r<a, in ⟨m,B,C⟩. Thus rA is Apéry, its unique exponent is r e_A, and all these axis points belong to every preferred T. The exponent a e_A is excluded because aA=bm, so the pure A-axis has exactly a points.

Suppose p=(x,y,z) is a full-support minimal excluded exponent. Its residue representative has disjoint support from p, by the standard Apéry minimal-corner lemma. Therefore the representative is zero and xA+yB+zC=k m for some positive integer k. Since p−e_B belongs to T, its first coordinate satisfies x<a.

Both r=(0,y,z) and q=(a−x,0,0) are in T: the former is a strict divisor of p, the latter is one of the unique pure-axis representatives just proved. Subtracting b m=a A from the displayed relation gives

yB+zC=(a−x)A+(k−b)m.

Thus r and q are distinct elements of T with the same residue modulo m, contradicting residue injectivity. The sign of k−b is irrelevant to this residue contradiction. ∎

The argument applies to Chomicz's entire secondary class, because the multiplicity belongs to one of its two paired pure critical relations. It also applies more broadly whenever the first critical multiple of one nonmultiplicity generator is a multiple of the multiplicity. No lexicographic ordering issue arises: the required axis representatives are unique.

A lower ideal with no full-support minimal excluded point equals the intersection of its three pairwise projection cylinders. This gives a stronger restriction than the one-interior-corner condition used by the global cutoff.


## 1.1. A uniform cutoff for every fixed critical pure exponent

Under the theorem's hypotheses, let r be the number of mixed minimal excluded points in the BC coordinate plane. Then

r≤a,
number of coordinatewise maximal points of T ≤a(r+1),
number K of occupied compressed cells of T ≤a(a+r)²≤4a³.

Consequently, by the established compressed-cell slab theorem,

**m≥4a(a+r)²−2 implies W_4≥0; in particular m≥16a³−2 implies W_4≥0.**

These bounds place no restriction on conductor, type, or generator size.

**Proof.** Write F=T∩{x=0}, as a planar lower ideal in the BC coordinates. Every mixed minimal excluded point of F is a support-BC minimal excluded point of T. Its residue representative lies on the A-axis. Distinct such points have intersecting supports, so their representatives are distinct. The A-axis has a points, proving r≤a.

A finite planar lower ideal with r mixed minimal excluded points has r+1 maximal points. This follows immediately by listing its nonempty columns in increasing first coordinate: every strict drop of column height contributes one mixed excluded corner, and each constant-height run ends in one maximal point.

Because T has no interior excluded corner, it is its pairwise closure. Its slices have the form

F_x=F∩([0,B_x−1]×[0,C_x−1]), 0≤x<a,

where B_x and C_x are positive, nonincreasing integers; B_0,C_0 are the corresponding axis lengths of F. Intersecting a planar lower ideal with a rectangle cannot increase its number of maximal points: express F as the union of its r+1 anchored maximal boxes, intersect each box with the rectangle, and observe that the maximal points of the union are drawn from these r+1 clipped box tops. Therefore each F_x has at most r+1 maxima and T has at most a(r+1) maxima.

For the cell bound, recall that compression partitions each coordinate at all positive levels z_j+1 belonging to a maximal point z of T, together with level zero. Every maximal point of T is the top of a maximal point of one of its slices. In the B coordinate, each such positive level is either a B-coordinate level from a maximal point of F, or one of the truncation levels B_x, 1≤x<a. There are at most (r+1)+(a−1)=r+a such levels. The same bound holds in the C coordinate. The A coordinate has at most a intervals, since its integer range is 0,...,a−1. Hence K≤a(a+r)²≤4a³.

The established slab theorem states m≥4K−2⇒W_4≥0. Substitution gives the displayed cutoffs. ∎

**Complete exponent-two case.** If a=2, then the bound on maximal points is at most 2(2+1)=6. Thus the prior complete six-final-window theorem applies and proves Wilf for every such semigroup, without a multiplicity restriction. This deduction inherits that theorem's computer-assisted finite part. It is an easily checked generator criterion for a class already included in the project's six-point theorem, not a claim that the residual six-point class has been extended.

In particular, **if m divides 2A for any nonmultiplicity minimal generator A, then Wilf holds.** Minimality makes the first critical exponent at least two, while 2A being a multiple of m makes it at most two. Equivalently this covers every minimally four-generated semigroup ⟨2p,(2q+1)p,B,C⟩ whose multiplicity is 2p.

For a=3 the coarse multiplicity cutoff is m≥430. More generally, a putative counterexample in the critical pure-axis class must satisfy m≤16a³−3. The remaining finite ranges for a≥3 have not been exhaustively verified here.

## 2. Exact characterization by two equal quotient semigroups

Write

A_0=⟨a,b⟩, B_0=⟨c,d⟩,
S=p A_0+q B_0=⟨pa,pb,qc,qd⟩,

gcd(a,b)=gcd(c,d)=gcd(p,q)=1,

with all four displayed generators minimal. Assume the two intended pure critical values pab and qcd are distinct.

**Proposition.** The two values pab and qcd have precisely their intended pure-pair factorizations if and only if, for every integer z>0,

pz∈B_0 ⇒ qz−a−b∈A_0,
qz∈A_0 ⇒ pz−c−d∈B_0.

In that case each displayed pure-pair relation is critical, and

A_0/q = B_0/p =: R,

where A_0/q={z∈N:qz∈A_0}.

**Proof.** An unwanted factorization of pab uses a positive contribution from q B_0. Since gcd(p,q)=1, it takes the form

pab=p u+q(pz), where z>0, u=ab−qz∈A_0, pz∈B_0.

Conversely every such z gives an unwanted factorization. The two-generated semigroup A_0 is symmetric with Frobenius number ab−a−b. Its symmetry identity, valid for all integers, says

ab−qz∉A_0 ⇔ qz−a−b∈A_0.

This proves the first implication's equivalence to excluding unwanted factorizations of pab; the other pair is identical. An earlier cross relation for a proper positive multiple of pa or pb would, after addition of a nonnegative pure multiple, give an unwanted factorization of pab. Thus the intended pure-pair relations are critical. Each displayed implication implies membership in the other quotient, so the quotients coincide. ∎

If q∈A_0 or p∈B_0, the quotient equality forces both, and S is the ordinary gluing of two two-generated semigroups; this is a known Wilf class. If the secondary semigroup is not this gluing, then both scales are gaps:

q≤ab−a−b, p≤cd−c−d.

The criterion is also a practical exact parameterization: enumerate two-generator quotients R with the stated interior property, match equal R, and choose coprime scales.

## 3. Secondary does not imply gluing, small type, or a small final window

The shortcut 'every secondary semigroup is a gluing' is false. For

S=⟨55,68,85,99⟩=11⟨5,9⟩+17⟨4,5⟩,

the only factorizations of 495 are 9·55 and 5·99; the only factorizations of 340 are 5·68 and 4·85. These are the critical pairs. But 17∉⟨5,9⟩, and S has type five, excluding any complete-intersection gluing decomposition of four generators.

The shortcut 'secondary type≤6' is false as well:

⟨4323,4800,4960,6026⟩=131⟨33,46⟩+160⟨30,31⟩

is secondary and has type eleven.

Finally, secondary semigroups need not have final-window cardinality at most six. For

S=⟨1558,1599,1675,2546⟩=67⟨25,38⟩+41⟨38,39⟩,

the exact quotient R has gaps

1,2,3,5,6,7,9,10,13,14,17,

and the exact invariants are

m=1558, c=62204, n=27157, W_4=46424, |Ap(S,m)∩[c,c+m)|=12.

A further secondary example

⟨3030,3725,3737,5066⟩=149⟨25,34⟩+101⟨30,37⟩

has common quotient gaps {1,3,5,7}, conductor 134796, n=48366, W_4=58668, and final-window cardinality sixteen.

These examples satisfy Wilf, and their projection-score certificates in the existing method are positive. Their role is to disprove the proposed structural shortcuts, not to claim newly settled individual semigroups.

## 4. Remaining target

The zero-interior-corner class is still not proved Wilf here. In particular, the theorem of Section 1 does not bound its number of maximal points. The common quotient in Section 2 likewise does not supply a conductor/genus formula that closes the inequality. A possible continuous bound 'mean weight≤two thirds of maximum' for pairwise-closed continuous downsets remains unproved; its naive discrete counterpart is false already for {0,e_1,e_2,e_3} with equal weights. No such bound is used as a theorem in this report.

Source context: Kazimierz Chomicz, *The type and cardinality of minimal presentations of numerical semigroups with embedding dimension four*, arXiv:2609.04000v1, Sections 2.1–2.3, https://arxiv.org/html/2609.04000v1.
