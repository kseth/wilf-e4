# Specialized independent worker: disjoint-piece formulas

10 September 2026.

`independent_specialized_piece_worker.cpp` evaluates the same independently audited interval dynamic program as `independent_residual_point_worker.cpp`. It changes the computation of section and center statistics. It does not import generating-worker source, subtract an excluded box from a full-box moment, prune corner permutations, or alter the parameter domain.

Let the fixed outward coordinate be `t` in direction `i`, and let the transverse rectangle be `[0,u]×[0,v]` in directions `j,k`. If `t<p_i`, the whole rectangle is retained. Otherwise its retained part is the disjoint union

\[
[0,\min(u,p_j-1)]\times[0,v]
\quad\sqcup\quad
[p_j,u]\times[0,\min(v,p_k-1)],
\]

where an interval with its lower endpoint above its upper endpoint is empty. If `u<p_j` or `v<p_k`, the entire rectangle is retained and the code uses its direct formula.

For a nonempty rectangle `[a,b]×[0,d]`, its cardinality, twice its transverse objective moment, and maximum transverse feasibility weight are respectively

\[
N=(b-a+1)(d+1),
\]
\[
2\Sigma_{\rm transverse}
=N\bigl(u_j(a+b)+u_kd\bigr),
\]
\[
M_{\rm transverse}=\ell_jb+\ell_kd.
\]

Here `u` denotes the upper interval weights used to bound the score, and `ell` the lower interval weights used for feasibility. Add counts and moments over the two disjoint rectangles and take the maximum of their maxima. Restoring the fixed outward coordinate adds `u_i tN` to the moment and `ell_i t` to the maximum. Consequently the section score is

\[
N(4u_it+q-3H_{\rm low})+2(2\Sigma_{\rm transverse}).
\]

The transverse statistics are independent of `t` within each of the two cases `t<p_i` and `t≥p_i`, so they are precomputed. This removes repeated prefix-array integration while leaving the dynamic-program recurrence unchanged.

For a central box `[0,x]×[0,y]×[0,z]`, if any upper coordinate is below its corner coordinate, the whole box is retained. Otherwise the retained points partition into three disjoint boxes according to the first coordinate below the corner:

\[
[0,p_x-1]\times[0,y]\times[0,z],
\]
\[
[p_x,x]\times[0,p_y-1]\times[0,z],
\]
\[
[p_x,x]\times[p_y,y]\times[0,p_z-1].
\]

For any integer box `L≤x≤U`, direct one-dimensional arithmetic-series summation gives

\[
N=\prod_i(U_i-L_i+1),\qquad
2\Sigma=N\sum_i u_i(L_i+U_i),\qquad
M=\sum_i\ell_iU_i.
\]

The worker spells these expressions out for all three pieces, then adds their counts and moments and takes their largest feasibility weight. The center score combines with the same three horn states as in the point-integrating worker.

The full Cartesian loop over positive corner coordinates is unchanged. It retains every corner of coordinate sum at least five obeying the existing weighted corner cap; there is no symmetry reduction.

## Bounded integer arithmetic

In the certificate domain the scale is 4,096, normalized weights are between one and 78, and the upper normalized height is at most 78. Thus every integer interval weight is at most `78·4096=319488`, and every axis array has at most 79 point positions. A horn array contains at most `80·79²=499280` entries, so its integer indices are comfortably within the signed 32-bit range.

A box has at most `79³=493039` points. Even the deliberately loose bound obtained by allowing all three coordinates to reach 78 gives an upper point weight below 75 million. A doubled moment is therefore below 74 trillion. The center score and the three horn contributions, bounded separately without using their disjointness, remain below one quadrillion in absolute value. All score, weight, count-product, and moment arithmetic uses signed 64-bit integers, whose positive limit exceeds nine quintillion. These bounds also cover the smaller-scale comparison boxes.

The program is not being asserted safe for arbitrarily large external scales or arbitrary unbounded inputs. The stated bounds concern precisely the independently checked interval certificate domain. Floating-point arithmetic is absent from the worker.

## Comparisons

All five saved comparison boxes produced exactly the same integer bound, first maximizing corner, and Cartesian corner count as the point-integrating worker. These include both positive and negative interval bounds.

The controlled batch benchmark compiled both workers with identical flags, `g++ -std=c++17 -O3 -march=native`. It repeated the four small boxes 100 times each and the larger box three times, checking every repeated output. Speedups were approximately 2.62, 2.36, 2.23, 2.71, and 2.99. On the larger box the average evaluation time decreased from 0.52086 seconds to 0.17447 seconds.

Exact comparison records are `independent_specialized_piece_comparisons.json` and `independent_specialized_piece_batch_benchmark.json`. Timing comparisons establish performance only; the formulas above and the unchanged optimization recurrence justify the mathematical computation. No existing worker, verifier, or active process was modified during this task.
