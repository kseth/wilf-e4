# Multiplicity bound from the continuous no-interior theorem

This corollary combines the new continuous mean theorem with the already proved sawtooth inequality in `deliverables/wilf_fixed_dimension_finite_reduction_2026-09-05.md`, the subsection “Summing the two phase inequalities”. It assumes the preferred Apéry factorization ideal has no full-support minimal excluded corner.

Let its size be `m`, its maximum weighted degree be `M=c+m-1`, its smallest nonmultiplicity generator be `a_min`, and set

`v=a_min/M`, `s=(a_1+a_2+a_3)/M`, `kappa=D/(mM)`.

For a putative `W_4<=0`, the exact identity `m W_4=D-m(m-1)` gives

`kappa< v`.

Thickening the ideal by its anisotropic unit cells and normalizing its largest coordinate sum yields

`kappa_c=(kappa+s)/(1+s)`.

The continuous no-interior mean theorem gives `kappa_c>=1/3`. If `v<1/3`, the previous exact sawtooth estimate gives

`kappa_c<2v(5-v)/(1+6v+v^2)`.

Consequently

`7v^2-24v+1<0`,

so

`v>(12-sqrt(137))/7=1/(12+sqrt(137))>1/24`.

If `v>=1/3`, the same weaker conclusion `v>1/24` is automatic. Every exponent vector `x` in the ideal then satisfies

`|x|<= (a·x)/a_min <= M/a_min=1/v<24`.

Hence the entire ideal lies in the degree-23 simplex in `N^3`. Its cardinality is at most

`m<=binom(23+3,3)=2600`.

Thus a four-generator semigroup with no full-support Apéry corner and `m>=2601` has **strictly positive** Wilf number. This is a finite bound on a remaining class, not an exhaustion of that class or a proof of the unrestricted conjecture.

The earlier residue argument excludes the full standard simplex of degree at least two, so equality `m=2600` cannot actually occur for such an Apéry ideal. The conservative bound `m<=2600` does not need that extra observation.
