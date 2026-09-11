# Lexicographic order cannot eliminate every interior corner

7 September 2026. Exact obstruction and additional necessary lattice conditions.

## 1. A smallest-cardinality obstruction

Let `S=<7,8,9,11>`. Its Apéry set modulo 7 is

`Ap(S,7)={0,8,9,11,17,19,20}`.

Each listed value has exactly one factorization in the three nonmultiplicity generators. Thus **every** coordinate lexicographic order, and indeed every possible selection of Apéry factorizations, gives the same set

`T={0,e1,e2,e3,e1+e2,e1+e3,e2+e3}`.

Its minimal excluded exponents are `2e1,2e2,2e3,(1,1,1)`. The last is a full-support corner, since all three of its immediate predecessors belong to `T`.

Therefore it is false that every four-generated numerical semigroup can be moved into the no-interior-corner class by changing its Apéry factorization order. The example has conductor 14, `n=5`, and `W_4=6`, so it is not a Wilf counterexample.

Seven is the smallest possible cardinality for an exponent lower ideal with a full-support minimal excluded point: all seven points of `{0,1}^3` except `(1,1,1)` must be included.

There are also order-independent nonunit interior corners. For

`S=<11,12,14,17>`,

the Apéry exponent set is exactly

`T={0,1,2} x {0,1} x {0,1} \ {(2,1,1)}`.

Every Apéry element again has a unique factorization. Its Apéry values are

`0,12,14,17,24,26,29,31,38,41,43`,

and its unique full-support corner is `(2,1,1)`. Here `c=33`, `n=13`, and `W_4=19`. Both examples are already settled Wilf families; their purpose is to refute a universal change-of-order shortcut.

The obstruction also occurs outside the six-final-window class. The semigroup

`S=<155,1552,1647,1651>`

has unique factorizations for all 155 Apéry elements, an unavoidable full-support corner `(1,7,4)`, and seven final-window points. Its exact invariants are

`M=18133`, `c=17979`, `n=6865`, `W_4=9481`.

The seven exponent vectors in the final window are

`(0,7,4),(1,2,8),(1,3,7),(1,4,6),(1,5,5),(1,6,4),(1,7,3)`.

This fixture rules out treating all order-independent full corners as automatically belonging to the six-point class. Its Wilf number is positive; no claim that it violates another established sufficient criterion is intended.

## 2. A sumset–difference-set obstruction stronger than merely counting corners

Let `T` have bijective linear labels in a group `G` of order `m`. Suppose finite integer sets `A,B` satisfy

`A+B subseteq T`.

Then

`|A-B|<=m`.

Indeed, equal labels on `a-b` and `a'-b'` give equal labels on `a+b'` and `a'+b`, both in `T`. Injectivity on `T` forces equality of these integer vectors, hence `a-b=a'-b'`. Thus labels are injective on `A-B` as well. This argument applies to any finite group labeling induced by a homomorphism; cyclicity is unnecessary.

An entire hierarchy follows. For any finite test set `B`, define the erosion

`A_B={x in Z^3: x+B subseteq T}`.

Every residue-bijective `T` must satisfy `|A_B-B|<=m`. The simplex difference-set exclusion in the earlier manuscript is one special case, but the condition applies to arbitrary shapes and arbitrary finite test sets.

## 3. Exact exclusion of the bad geometric one-corner example

For the auxiliary continuous counterexample's cell index set,

`T={x in N^3: x1+x2,x1+x3,x2+x3<=29; min(x)<=3}`,

take

`B={0,e1,e2,e3}`,

`A={x in T: x+B subseteq T}`.

The exact counts are

`|T|=4246`, `|A|=3241`, `|A-B|=4546`.

Since `4546>4246`, this `T` cannot admit any residue-bijective lattice labeling of the required index. This excludes it without using the separate bound on the number of mixed corners.

The result does not claim that the unit-simplex test suffices for all staircases. Coarsening profiles may defeat one test while preserving the bad centroid. The full hierarchy supplies additional necessary conditions; neither sufficiency nor a centroid theorem from it has been proved here.

## 4. Further exact constraints available from an actual interior corner

Write `Lambda=ker(Z^3 -> Z/mZ)` for the residue lattice. If `p` is a full-support minimal excluded exponent, then `p in Lambda`. For a mixed excluded corner `q` in a coordinate plane and its representative `h e_i` on the complementary axis, both

`q-h e_i in Lambda` and `q-h e_i-p in Lambda`.

None of these nonzero vectors can lie in `T-T`. More generally every nonzero vector of `Lambda` is excluded from `T-T`, since two points of `T` cannot have the same residue. The resulting translated-overlap exclusions retain the positions and sizes of mixed corners, not only their count.

If three such lattice vectors are linearly independent, the absolute value of their determinant is a positive integer multiple of `m`. This follows because they generate a sublattice of `Lambda`, whose index in `Z^3` is `m`. It is a further exact condition on candidate corner data, not a stand-alone sufficient labeling criterion.

No implication from these necessary conditions to the sharp continuous `2/3` centroid inequality for all genuine one-corner Apéry shapes has been completed.

## Verification

`lex_order_and_tiling_check.py` computes the three Apéry sets independently, enumerates all their factorizations, checks all six lexicographic orders, and verifies the displayed sumset–difference-set counts using exact integer arithmetic.
