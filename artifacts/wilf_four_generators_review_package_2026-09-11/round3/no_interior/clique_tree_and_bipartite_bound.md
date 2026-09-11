# No-interior-corner ideals: clique trees and a settled bipartite subclass

## Scope

Let T be a finite lower ideal in N^3 with no coordinatewise minimal excluded point supported on all three coordinates. Equivalently, membership is determined by its three pair projections:

  (x,y,z) belongs to T iff (x,y,0), (x,0,z), (0,y,z) all belong to T.

The equivalence follows by choosing a minimal excluded point below any omitted point.

This note proves a structural clique-tree description and a moment bound for the subclass with a bipartite interaction graph. It does not prove the conjectural continuous mean bound 2M/3 for the full no-interior class.

## 1. A chordal graph encodes the maximal boxes

For coordinate i let h_i be its largest axis exponent. Introduce graph vertices (i,r), 0<=r<=h_i. Vertices from the same coordinate class are all adjacent. Vertices (i,r),(j,s), i!=j, are adjacent exactly when r e_i+s e_j belongs to T. The zero vertices are universal.

Within one coordinate class, the external neighborhood of a lower level contains that of any higher level. This is downward closure.

Every induced cycle of length at least four would repeat a coordinate class. Since that class is a clique, its repeated vertices must be exactly two adjacent cycle vertices. Name their levels r<s. The other cycle neighbor of (i,s) lies outside this class and is also adjacent to (i,r), by nested external neighborhoods. That edge is a chord, a contradiction. Thus the graph is chordal.

A maximal clique contains every level below each of its coordinate maxima. Its three maxima form a point of T, by pairwise determination. Conversely, every point of T gives the clique consisting of the three coordinate prefixes. Hence maximal graph cliques correspond bijectively to maximal points z of T, or equivalently to their boxes B_z=[0,z] intersected with N^3.

The clique-tree theorem for chordal graphs therefore supplies a tree on these maximal boxes such that the boxes containing any graph vertex form a connected subtree. In particular, for every coordinate i and level r,

  {z maximal in T:z_i>=r}

is a connected subtree. Intersections of connected subtrees of a tree are connected, so the boxes containing any point x also form a connected subtree.

## 2. Exact tree inclusion-exclusion

Let E be the edges of such a tree, and let z meet z' denote the coordinatewise minimum. Since a nonempty finite tree has one more vertex than edge, pointwise counting gives

  1_T = sum_z 1_{B_z} - sum_{zz' in E} 1_{B_(z meet z')}.

Consequently

  |T| = sum_z prod_i(z_i+1) - sum_{zz' in E} prod_i(min(z_i,z'_i)+1),

and, for any positive weights a,

  sum_T a.x = (1/2) [sum_z |B_z| a.z
                    -sum_{zz' in E} |B_(z meet z')| a.(z meet z')].

The same identity holds for the union of the corresponding continuous boxes and its volume and first moments. Thus the general inclusion-exclusion over exponentially many subsets reduces to tree vertices and edges.

## 3. At most three leaves and a three-arm description

If z is a leaf with neighbor z', then z_i>z'_i for some coordinate i, since distinct maximal points are incomparable. The connected-superlevel-set property implies that z_i exceeds the value of coordinate i at every other node: otherwise the path to another such node would cross z'. Different leaves cannot use the same coordinate. Therefore the clique tree has at most three leaves; it is a path or a tripod, aside from the single-box case.

Choose one node where each coordinate reaches its global maximum, and let z0 be the median of those three nodes in the tree. Every component beyond z0 contains at most one of the three chosen maximum nodes. Along an arm toward the maximum of coordinate i, coordinate i is nondecreasing and the other two coordinates are nonincreasing, by connectedness of every coordinate superlevel set. The increasing coordinate is strictly increasing between consecutive nodes, since otherwise the later maximal point would be dominated by the earlier one.

After thickening to boxes, or after any positive diagonal coordinate scaling, this yields a central box [0,c_1]x[0,c_2]x[0,c_3] and at most three disjoint arms. Arm i lies beyond x_i=c_i and below the other two central coordinate bounds. Each cross section perpendicular to its outward coordinate is a rectangle, and its two side lengths are nonincreasing functions of the outward coordinate.

This reduces the unproved full continuous mean bound to an inequality for a central box plus at most three rectangular-fiber arms. The arms' intersections are exactly contained in the central box.

## 4. The bipartite interaction moment theorem

Define an interaction graph on {1,2,3}: join i and j if some minimal excluded point has support {i,j}. Pure-axis excluded points impose only individual bounds. If this graph is bipartite with color classes A,B, then for all positive weights a,

  E_T[a.X] <= (2/3) max_T a.x.                         (B)

Proof: no excluded constraint involves two coordinates of the same color class. Holding the other class fixed therefore gives a rectangular fiber in the coordinates of one class. Simultaneously moving all coordinates in A to their fiber tops stays in T. Conditional uniformity on each finite interval 0,...,H implies that its top coordinate equals twice its conditional mean. Writing mu_i=E[a_i X_i] and mu=sum_i mu_i, the expected weight after this simultaneous move is mu+sum_{i in A}mu_i, and is at most M. The analogous B move gives mu+sum_{i in B}mu_i<=M. Adding yields 3mu<=2M.

The identical argument works for continuous downsets, using uniform intervals [0,H] and their endpoints. Thus (B) holds in both settings, without a discretization correction.

## 5. Wilf consequence of the bipartite subclass

For a four-generator Apéry ideal, D=3mM-4 sum_T a.x and mW=D-m(m-1). Therefore (B) gives

  W >= M/3-(m-1).

This proves Wilf whenever M>=3m-3, equivalently conductor c>=2m-2. The remaining conductors lie in the already published c<=3m range. Combining those facts proves Wilf for the entire bipartite interaction subclass.

Accordingly, an unresolved no-interior counterexample must involve minimal excluded pair corners of all three support types {1,2},{1,3},{2,3}.

## 6. What does not follow

The full no-interior interaction graph may be a triangle. The bipartite simultaneous-update argument then supplies only the ordinary three-coordinate bound. Tree inclusion-exclusion alone does not yet provide the required sign for the first-moment expression. No proof of the desired universal continuous bound mu<=2M/3, or a complete classification of ordered geometric LP failures, is asserted here.
