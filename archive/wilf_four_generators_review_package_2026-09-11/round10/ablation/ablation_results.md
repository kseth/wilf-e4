# Structural-filter ablation for the two explicit centroid constructions

11 September 2026. These experiments simplify the hypotheses of the finite
low-degree theorem. They do not remove enumeration of the remaining finite class.

## Successful enlargement

Retain the following restrictions:

- T is a finite lower ideal in N^3, reconstructed from its three planar
  projections and deletion of one upper orthant p+N^3.
- The unique full-support minimal exclusion p has positive coordinates and
  `5<=|p|_1<=7`; all proper divisors of p are included.
- Every point has total degree at most six and `m=|T|>=30`.
- Each coordinate plane has at most `|p|_1-2` mixed minimal excluded points.
- For distinct i,j,k, the pair-surface count satisfies
  `|F_i intersection F_j|<=2n_k`, where `F_i={x in T:x+e_i not in T}` and
  `n_k=1+max_T x_k`.

**Neither erosion nor the refined bound on plane corners dominating the
projection of p is needed in this finite lemma.**

Let U2 be the line-endpoint construction using only extensions by at most two
coordinate steps, and let G be the axis-intercept construction. In the notation
of the accompanying centroid theorem,

    U2 = sum_{i,t in F_i}(t_i+1) min(2,max_{u in T,u>=t}(|u|_1-|t|_1)),
    G  = max_i q_i (3m-4 sum_i s_i/q_i),
    q_i=n_i-1, s_i=sum_{x in T}x_i.

The expression in U2 is computed solely by membership of t+e_j and
t+e_j+e_k; no global maximization is performed in the final producer.

The exact producer `local2_no_upper.cpp` checked

    max(U2,G)>=m

for all **5,574,644** retained ideals. Its counts are:

| Corner | Retained ideals | U2 alone succeeds | Axis fallback needed |
|---|---:|---:|---:|
| (1,1,3) | 1,581,961 | 1,581,746 | 215 |
| (1,2,2) | 1,433,543 | 1,433,331 | 212 |
| (1,1,4) | 874,540 | 874,537 | 3 |
| (1,2,3) | 638,574 | 638,573 | 1 |
| (2,2,2) | 592,453 | 592,453 | 0 |
| (1,1,5) | 159,580 | 159,580 | 0 |
| (1,2,4) | 105,119 | 105,119 | 0 |
| (1,3,3) | 94,500 | 94,500 | 0 |
| (2,2,3) | 94,374 | 94,374 | 0 |
| **Total** | **5,574,644** | **5,574,213** | **431** |

All arithmetic is integer; the axis expression is compared after multiplying
by the least common multiple of its three positive denominators. This broad
class contains the 3,742,041 original residual ideals.

## Intermediate ablations and replay scope

- Removing erosion alone gives 3,909,378 ideals, all satisfying
  `max(U,G)>=m`, where U allows an arbitrary extension to a dominating maximum.
  Both the bitset producer and a separate literal-height/reverse-DP replay
  completed and agreed on all nine counts. The independent result is
  `independent_result.json` in this directory.
- Removing erosion and the refined dominating-corner restriction gives
  5,574,644 ideals. Both the arbitrary-extension producer and the final local-U2
  producer passed this class.
- Removing the total mixed-corner count while retaining the refined restriction
  leaves the same 3,909,378 ideals: the total count follows geometrically from
  the refined condition plus at most `p_i+p_j-2` remaining mixed corners.

The separate line-upgrade agent is responsible for the final independent local-U2
replay on the full 5,574,644 class and its final theorem/portable entry point.
The no-erosion independent replay recorded in this directory must not be confused
with that larger final replay.

## Why the total plane-corner restriction was retained

Dropping both plane-corner restrictions produces exact failures of these two
chosen witness formulas. The fixtures are explicitly recorded and independently
checked by direct set membership in `check_fixtures.py`:

| Fixture | Corner | m | Degree | U | U2 | G |
|---|---|---:|---:|---:|---:|---:|
| only_surface_first_failure.json | (1,1,3) | 33 | 5 | 31 | 30 | 31 |
| only_surface_weak_first_failure.json | (1,2,2) | 33 | 5 | 30 | 30 | 30 |

Both have axis lengths (5,5,6), satisfy every pair-surface bound, and even satisfy
the old erosion restriction. Their yz-plane has four mixed exclusions, exceeding
the bound three. The second fixture fails even the earlier target `m-29/10=30.1`
for both U and G. These are failures of the selected formulas, **not**
counterexamples to the centroid inequality or to Wilf. Other convex-hull
witnesses can work for the same shape; no contrary claim follows from this test.

## Reproduction

Run the exact final producer from the project root:

```sh
g++ -std=c++17 -O3 round10/ablation/local2_no_upper.cpp -o /tmp/wilf_local2_ablation
/tmp/wilf_local2_ablation
python3 round10/ablation/check_fixtures.py
```

The producer writes its named records only inside this directory. Historical
certificate files are not read or modified. It uses the same complete planar
profile enumeration and axis-compatible cylinder reconstruction as the existing
finite proof, with strictly fewer rejection predicates. The final local-U2
construction checks all one- and two-step nonnegative coordinate increments,
including two steps in the same coordinate, with explicit coordinate-boundary
checks to prevent bit-index wraparound.
