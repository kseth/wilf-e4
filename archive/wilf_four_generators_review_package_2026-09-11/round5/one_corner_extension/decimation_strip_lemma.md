# Decimation transfers a finite height strip to all large heights

Let T be a finite lower ideal in N^3 with at most one full-support
minimal excluded point. Fix positive weights a=(1,b,c), put S=1+b+c,
and let M be any height allowance for T. For an integer L>=1 and
r in {0,...,L-1}^3, define

\[
T_r=\{y\in\mathbb N^3:r+Ly\in T\},\qquad
M_r=(M-a\cdot r)/L.
\]

Every nonempty T_r is a lower ideal with at most one full-support
minimal excluded point. Indeed an excluded orthant with corner g pulls
back to the orthant with corner

\[
\left(\max\{0,\lceil(g_i-r_i)/L\rceil\}\right)_{i=1}^3.
\]

An original support-at-most-two corner stays supported on at most two
coordinates; only the single original full corner can retain full
support. Redundant pulled-back corners can be removed. No unit-vector
assumption on T_r is needed.

Write D(V;H)=3|V|H-4 sum_V a dot y. Direct substitution gives the exact
identity

\[
D(T;M)=\sum_r\left[L D(T_r;M_r)-(a\cdot r)|T_r|\right].
\]

Suppose S<=C and, for some H_0>C, a finite parameter-strip certificate
proves D(V;H)>=C|V| for every nonempty one-corner lower ideal V, every
allowed weight triple, and every allowance H in [H_0-C,2H_0]. Then
the same inequality holds at every M>=H_0. To see this, take
L=floor(M/H_0). Since

\[
H_0\le M/L<2H_0,\qquad
0\le(a\cdot r)/L\le(1-1/L)S<C,
\]

all nonempty classes have M_r in the certified strip. Their individual
contributions are at least

\[
[LC-(a\cdot r)]|T_r|\ge[LC-(L-1)S]|T_r|\ge C|T_r|.
\]

Summing proves the claim. This is a conditional transfer lemma; it does
not assert that the required arbitrary-weight strip is already
certified.

For unit weights and integer R, it is enough to certify integer
allowances. Put R_r=floor((R-|r|)/L) and
eta_r=R-|r|-LR_r. The exact version is

\[
D(T;R)=\sum_r\left[L D(T_r;R_r)+(3\eta_r-|r|)|T_r|\right],
\qquad 0\le\eta_r<L.
\]

Thus D(T_r;R_r)>=3|T_r| implies D(T;R)>=3|T|. With H_0=17, L=floor(R/17)
and R>=17, all relevant integer R_r lie between 14 and 33. The unit
weight project independently completed this finite strip using its
clipped-horn DP; see `round5/weighted_analytic/one_corner`.
