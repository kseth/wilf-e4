# The discrete consequence of the no-interior continuous theorem

7 September 2026, final update. The formerly conditional input has now been proved by the arbitrary-horn bridge and the joint effective-cap theorem. Consequently the multiplicity bound below is **unconditional within the no-interior subclass**, subject to those proofs. It does not prove unrestricted Wilf. The historical filename is retained for reproducibility.

Let T be a preferred Apéry lower ideal for a minimally four-generated numerical semigroup S with multiplicity m. Its coordinate weights are a_i>m; put

- M=max_{x in T} a·x=c+m−1;
- Σ=sum_{x in T} a·x;
- D=3mM−4Σ;
- W=4n−c, so mW=D−m(m−1).

Assume T has no full-support minimal excluded point. The independent clique-tree theorem gives a central box and at most three rectangular-fiber arms.

## 1. The continuous input, now proved

Every bounded finite-box continuous lower set of this no-interior kind satisfies

    E[w(X)] <= (2/3) max w.

This follows from `../bellman/arbitrary_horn_bridge.md` and `../joint_horns/joint_effective_cap_theorem.md`, using the clique-tree description and the optimal boundary-horn formula. The deductions below use that completed theorem.

## 2. Direct thickening loses a real endpoint correction

Thicken each lattice point x to x+[0,1]^3. The new volume is m, its mean weight is Σ/m+(a_1+a_2+a_3)/2, and its maximum is M+a_1+a_2+a_3. Thus the assumed continuous theorem yields only

    Σ/m <= 2M/3+(a_1+a_2+a_3)/6,

and hence

    W >= M/3−2(a_1+a_2+a_3)/3−(m−1).

The correction cannot simply be omitted. In fact there is an infinite family of no-interior ideals violating the uncorrected discrete mean bound.

For R>=1 let

    T_R={(x,y,z):x+y<=R, x+z<=R, yz=0}.

This is the union of two degree-R planar triangles sharing one axis. All defining excluded constraints have support at most two. With unit weights,

    m=(R+1)^2,
    M=R,
    Σ=R(R+1)(4R+5)/6,
    Σ/m=2R/3+R/[6(R+1)] > 2R/3.

Also

    3Σ−2mM=R(R+1)/2.

Consequently even a proposed correction 3Σ<=(2m+1)M fails for every R>=2. The size of the correction cannot be bounded by one maximum weight. This is an obstruction to a proof shortcut, not a counterexample to Wilf. The family has genuine Apéry realizations treated in the preceding checkpoint; their unequal arithmetic weights restore Wilf.

## 3. A valid phase bridge gives total exponent at most 23

Normalize u_i=a_i/M, set v=min u_i, s=sum u_i, and κ=D/(mM). The unit thickening has normalized deficit

    κ_c=(κ+s)/(1+s).

The continuous mean theorem is exactly κ_c>=1/3.

The previously proved sawtooth estimate, valid for every finite lower ideal containing the coordinate unit vectors, is

    s(1−3κ)<=4κ+5v−3κv+4v².                  (1)

For a nonpositive Wilf number,

    κ=(W+m−1)/M <=(m−1)/M <a_min/M=v.

If v>=1/3, then M/a_min<=3 already. If v<1/3, the right-hand bound for s in (1) is strictly increasing in κ. Substituting κ<v gives

    s<(9v+v²)/(1−3v),
    κ_c<2v(5−v)/(1+6v+v²).

Combining with κ_c>=1/3 yields

    7v²−24v+1<0,
    v>(12−sqrt(137))/7=1/(12+sqrt(137)).

Hence, in both cases,

    M/a_min<12+sqrt(137)<24.

Since a·x>=a_min |x|_1, every x in T has total exponent at most 23. The crude consequence is m<=binom(26,3)=2600.

The input (1) is proved in the previous fixed-dimension checkpoint, in the section "Summing the two phase inequalities". Its proof is independent of no-interior geometry and of the new continuous input.

## 4. The tripod structure improves the cutoff to 1836

For an integer degree limit R, choose the central point c=(c_1,c_2,c_3) supplied by the clique tree. It belongs to T, so c_i>=0 and sum c_i<=R.

Its central box contains at most

    (c_1+1)(c_2+1)(c_3+1)

points. Beyond this box, each point belongs to exactly one arm. In arm i, at outward integer level t>c_i, the remaining coordinates form a rectangle [0,u]×[0,v]. Its caps obey

    u<=c_j, v<=c_k, u+v<=R−t.

Therefore its cardinality is at most

    Q(c_j,c_k,R−t)
      =max_{0<=u<=min(c_j,R−t)} (u+1)(min(c_k,R−t−u)+1).

Summing the disjoint central box and arm layers gives the rigorous bound

    |T| <= B_R(c)
      :=prod_i(c_i+1)+sum_i sum_{t=c_i+1}^R Q(c_j,c_k,R−t).

The bound is invariant under coordinate permutations, so it is enough to enumerate sorted c_1<=c_2<=c_3 with sum c_i<=R. Exact integer evaluation at R=23 gives

    max_c B_23(c)=1836.

A maximizing sorted central triple is (7,7,8); (7,7,9) and (7,8,8) also attain the same bound. The standard-library checker `max_no_interior_size.py` implements exactly the displayed finite formula and supplies the full R=1,...,23 table in `max_no_interior_size_results.json`. The separate checker enumerates all ordered central triples and all feasible rectangle endpoint pairs and obtains the identical maximum.

Thus the conclusion is:

> A four-generator Apéry ideal with no full-support excluded corner and W<=0 has m<=1836. In particular m>=1837 forces strict Wilf in that subclass.

The reduction also applies without residues to the ordered geometric relaxation: if a_1>=m+1, a_2>=a_1+1, a_3>=a_2+1 and D<m(m−1), then κ<v by exactly the same argument. Therefore any such no-interior geometric failure is contained in Δ_23 and has m<=1836. This does not classify those finite shapes.

For genuine semigroups, the previously published small-multiplicity result m<=19 means any negative case remaining in that subclass would have 20<=m<=1836. No enumeration or analytic exclusion of that remaining interval is asserted here. The statement does not apply to ideals with a full-support excluded corner.

## 5. Exact verification and scope

The cutoff is a mathematical consequence of the completed continuous theorem, with a small finite integer computation for its last constant. It does not use floating-point optimizers as proof. The separate exploratory `probe_discrete_mean.py` and `optimize_phase_cutoff.py` scripts are diagnostics only; their numerical results are not inputs to this deduction. The infinite T_R formula already supplies exact counterexamples to the two proposed discrete shortcuts.
