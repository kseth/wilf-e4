# Producer horn precomputation audit

10 September 2026.

**Status: unused performance experiment.** Root and the geometric-residual coordinator retained the stable producer because the measured improvement was modest. This variant and its benchmark are not part of the active proof-generation or verification chain.

`interval_all_corners_precomputed.cpp` is a separate producer variant. The central-box formula and the entire `main` routine are byte-identical to `interval_all_corners_parallel.cpp`. Thus corner ordering, symmetry restrictions, early-stop semantics, completion flags, and OpenMP behavior are unchanged. No running source or process was modified.

For transverse bounds `(u,v)`, the whole rectangle has

\[
N=(u+1)(v+1),\qquad
B=N(u_ju+u_kv),\qquad
L=\ell_ju+\ell_kv,
\]

where `B` is twice the transverse objective moment. When both transverse bounds reach the corner, the removed rectangle has

\[
R=(u-p_j+1)(v-p_k+1),
\]

and twice its transverse moment is

\[
R\bigl(u_j(p_j+u)+u_k(p_k+v)\bigr).
\]

The clipped profile subtracts this cardinality and moment. Its retained maximum is

\[
\max\{\ell_j(p_j-1)+\ell_kv,
        \ell_ju+\ell_k(p_k-1)\}.
\]

The whole profile is selected for `t<p_i`, and the clipped profile otherwise. Restoring the outward coordinate transforms the section score exactly into

\[
N(4u_it+q-3H_{\rm low})+2B.
\]

This is the original score with common terms collected; the nested-rectangle recurrence is unchanged. All profile and score quantities remain signed 64-bit integers within the existing audited domain bounds.

The producer retains full-minus-removed integration. The independent specialized verifier instead adds disjoint retained rectangles and boxes, so this optimization preserves their distinct integration methods.

The accepted large reference box was evaluated three times by each version, compiled identically. All bound, witness, corner-count, and completion fields matched exactly: `[-284291,1,1,3,1606,1]`. The measured average decreased from 0.23824 to 0.22132 seconds per box, approximately 1.076 times faster. This is a modest observed improvement, not a guaranteed speedup for every box. The exact record is `precomputed_producer_benchmark.json`.
