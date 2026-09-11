# A sharp unit-weight theorem for at most one interior corner

**Theorem.** Let T be a finite lower ideal in N^3 with at most one
full-support minimal excluded point. Put

    m=|T|, R=max_{x in T}|x|_1,
    D=3mR−4 sum_{x in T}|x|_1.

Then

    m>=65  =>  D>=m.

The cardinality threshold 65 cannot be replaced by 64. This is an
unbounded unit-weight theorem. It does not prove the arbitrary-weight
inequality needed for genuine four-generator Apéry ideals.

## 1. Exact finite inputs

The exact clipped-horn recurrence is proved in `one_corner_results.md`.
It includes every lower ideal with at most one full-support excluded
corner and does not require the coordinate unit vectors to belong.
A full-support minimal excluded p satisfies |p|_1<=R+1 because its three
immediate predecessors belong to T. Thus the finite range of corners is
complete; coordinate symmetry permits sorting p.

The recurrence is implemented in `one_corner_dp.py` using exact integers,
and in the optimized C++17 translation `one_corner_unit_dp.cpp`. Direct
height-array enumeration independently checked the Python recurrence on
106,717 ideals, including unequal weights. The C++ and Python versions
agree on all six heights R=3,...,8 for the target objective.

The exact strip results are:

* For every R=7,...,16, max_T(m−D_R)<=0.
* For every R=14,...,34, max_T(3m−D_R)<=0.
* At R=6, every allowed full-support corner other than (1,1,1) has
  max_T(m−D_R)<=−1.

Here D_R uses the stated allowance R, even when a particular ideal has a
smaller actual height. This strengthens the scope of each upper bound and
is exactly what decimation requires.

More precisely, the first strip's maxima are −20 at R=7 and 1−3R at
R=8,...,16. Every maximum in the second strip is 3−3R. They are all
strictly negative. The complete exact records are
`unit_target_strip.jsonl` and `unit_decimation_strip.jsonl`.

## 2. Decimation preserves the corner condition

For a positive integer L and r∈{0,...,L−1}^3, define

    T_r={y∈N^3:r+Ly∈T}.

Each nonempty T_r is a finite lower ideal. If an upper orthant excluded
from T has vertex g, its inverse image has vertex

    g'_i=max(0,ceil((g_i−r_i)/L)).

A zero coordinate of g stays zero in g'. Consequently an excluded vertex
supported on at most two coordinates cannot acquire full support. The
single possible full-support vertex maps to at most one full-support
vertex; removal of redundant generators cannot increase that number.
Thus T_r has at most one full-support minimal excluded point. Some T_r
lack one or more unit vectors, which the finite recurrence permits.

## 3. Exact defect identity with the floor correction

Write m_r=|T_r| and

    R_r=floor((R−|r|_1)/L),
    η_r=R−|r|_1−L R_r,       0<=η_r<=L−1.

Each point of T_r has degree at most R_r. With

    D_r=3m_r R_r−4 sum_{y in T_r}|y|_1,

direct substitution of |r+Ly|_1=|r|_1+L|y|_1 gives

    D = sum_r [L D_r+(3η_r−|r|_1)m_r].              (1)

Empty residue classes contribute zero and may be omitted. If all the
nonempty classes satisfy D_r>=3m_r, then

    L D_r+(3η_r−|r|_1)m_r
      >=(3L−|r|_1)m_r
      >=3m_r,

because |r|_1<=3(L−1). Summing (1) gives D>=3m.

## 4. A finite strip covers every R>=17

For R>=17, take L=floor(R/17)>=1. Then

    17<=R/L<34.

Also |r|_1/L<=3−3/L, so

    14<=floor((R−|r|_1)/L)<=33.

Therefore every nonempty class T_r lies in the checked strip R_r=14,...,34.
The second finite input proves D_r>=3m_r, and Section 3 gives D>=3m.
This covers every height R>=17 without further enumeration.

For 7<=R<=16, the first finite input already gives D>=m. Hence every
ideal of height R>=7 satisfies D>=m.

## 5. Cardinality reduces the remaining heights

If R<=5 then T is contained in the degree-five simplex, which has
binom(8,3)=56 points. Thus m>=65 implies R>=6.

At R=6, a full-support corner p=(1,1,1) excludes all points with three
positive coordinates. Such a T is contained in the union F_6 of the
three coordinate-plane degree-six triangles, and |F_6|=64. Therefore
m>=65 excludes this corner. Every other one-corner ideal at R=6 satisfies
D>=m by the third finite input. A no-interior ideal can be included by
choosing an inactive positive corner of degree seven (for example (1,1,5))
and taking its pairwise closure to be itself.

This completes the theorem.

## 6. Sharpness

For

    F_R={x∈N^3:|x|_1<=R, min_i x_i=0},

inclusion-exclusion gives

    |F_R|=(3R²+3R+2)/2,
    sum_{F_R}|x|_1=R(R+1)(2R+1)/2,
    D(F_R)=R(R−1)(R−2)/2.

At R=6, |F_6|=64 and D(F_6)=60<63=|F_6|−1. Its only full-support
minimal excluded point is (1,1,1). Thus even the weaker target D>=m−1
fails at cardinality 64.

## Verification and limitations

`verify_unit_one_corner_theorem.py` compiles the C++17 implementation in a
temporary directory, reruns both finite strips, compares all exact outputs
with the records, and compares the six overlapping heights against the
Python recurrence. It checks the low-height corner exclusion and the sharp
example. A C++17 compiler and Python's standard library are required; no
floating-point value enters a certificate decision.

The analytic decimation lemma was independently checked by the parameter
arrangement agent. The full theorem and C++ translation have been submitted
for another in-session audit. This is not external mathematical review.

The theorem controls unit weights. It does not imply the statement for
unequal positive weights: residue decimation then incurs the correction
−a·r, which requires a weighted bound on each residue class. Treating that
correction as the unit-weight correction would be invalid.
