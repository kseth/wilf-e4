from pathlib import Path
p=Path('deliverables/wilf_four_generators_review_manuscript_2026-09-11.md')
s=p.read_text()
s=s.replace(r'D_0=3mH-4b\cdot s.',r'D_0=3mH-4b\cdot s,\qquad D=AD_0.')
# Surface inequality G2 is distinct from the conductor reduction G3.
start=s.index('### Small multiplicities and analytic conductor reduction')
s=s[:start]+s[start:].replace(r'\tag{G2}',r'\tag{G3}').replace('(G2)','(G3)')
s=s.replace('This remains an explicit dependency after Round 10. It was removed from the *residual low-degree branch*, not from the whole proof.','This remains a dependency of the exceptional-corner branch. The residual low-degree branch uses the explicit centroid theorem instead.')
s=s.replace('This supplement simplifies its centroid part.','The present constructions simplify the residual centroid branch.')
s=s.replace('Thus the earlier comparison of \\(90/31\\) with \\(29/10\\) is unnecessary for\nthis residual low-degree class.','The high-height comparison in Section 3 is unnecessary for this residual low-degree class.')
s=s.replace('2. L. Kliem and C. Stump','2. J. Kliem and C. Stump')
s=s.replace('M. Hellus, J. Rechenauer and R. Waldi','M. Hellus, A. Rechenauer and R. Waldi')
s=s.replace('M. Delgado, S. Eliahou and J. Fromentin, *Wilf’s conjecture and numerical semigroups with genus up to 100*','M. Delgado, S. Eliahou and J. Fromentin, *A verification of Wilf’s conjecture up to genus 100*')
needle='### Small multiplicities and analytic conductor reduction\n\n'
s=s.replace(needle,needle+'The published input is [Bruns, García-Sánchez, O’Neill and Wilburne](https://arxiv.org/abs/1903.04342) through multiplicity 18 and [Kliem and Stump](https://arxiv.org/abs/1905.01945) for multiplicity 19.\n\n')
s=s.replace(r'\nu=|P|',r'u=|P|')
p.write_text(s)
