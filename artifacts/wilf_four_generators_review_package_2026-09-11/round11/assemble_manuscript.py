from pathlib import Path
import re
root=Path('/workspace/scratch/a8c8677e5545')
local=(root/'deliverables/wilf_centroid_local_constructions_2026-09-11.md').read_text()
proof=(root/'round11/proof_map.md').read_text()
dims=(root/'round11/dimensions_section.md').read_text()
def between(s,a,b):
    return s.split(a,1)[1].split(b,1)[0].strip()
def prefix_equations(s,p):
    s=re.sub(r'\\tag\{(\d+)\}',lambda m:r'\tag{'+p+m[1]+'}',s)
    s=re.sub(r'(?<!\w)\(([1-9])\)',lambda m:'('+p+m[1]+')',s)
    return s
def subordinate(s):
    s=re.sub(r'^### \d+\.\d+ (.*)$',r'#### \1',s,flags=re.M)
    s=re.sub(r'^## \d+\. (.*)$',r'### \1',s,flags=re.M)
    return s
front=r"""# Wilf's inequality for four generators
## A proposed computer-assisted proof, explicit centroid witnesses, and dimensional limits

**Review manuscript · 11 September 2026**

### Abstract

We organize a proposed computer-assisted proof of Wilf's inequality for numerical semigroups of embedding dimension four. The main simplification is a pair of explicit, weight-independent centroid constructions: move coordinate-line endpoints upward by at most two steps, or combine the axis endpoints. For the specified residual class, exact finite verification shows that one construction always succeeds. This strengthens the normalized moment bound to \(D_0\ge m\), removes two auxiliary hypotheses, and replaces per-ideal linear-programming certificates with direct formulas.

The manuscript gives the complete case partition and identifies each retained analytic or computational dependency. It also proves the centroid criterion directly for infinite clipped-box and clipped-prism families. The moment identity and witness formulas extend to all embedding dimensions, but their coverage does not. Equality examples rule out the strongest unrestricted centroid statement, and two actual five-generator Apéry ideals exhibit geometric obstructions to a direct extension.

**Status.** This is a proposed research proof with completed exact checks and in-session audits. External mathematical review and proof-assistant formalization remain outstanding. The main manuscript is a readable synthesis; the accompanying technical archive contains the detailed retained proofs, source code, certificates, and replay records. No unrestricted theorem for five or more generators is claimed.

## 1. Main claim and notation

A numerical semigroup is a cofinite additive submonoid \(S\subseteq\mathbb N\), where \(\mathbb N\) includes zero. Its multiplicity \(m\) is its smallest positive element, its conductor \(c\) is the least integer with \(c+\mathbb N\subseteq S\), and its embedding dimension \(e\) is the number of minimal generators. Put \(n=|S\cap[0,c)|\). Wilf's inequality is \(en\ge c\).

**Proposed theorem.** Every minimally four-generated numerical semigroup satisfies
\[
W_4(S)=4n-c\ge0.
\]
The logical coverage is given in Section 3. The stronger strict inequalities below apply only to the indicated subclasses.

Write \(S=\langle m,a_1,a_2,a_3\rangle\). The Apéry set is
\[
\operatorname{Ap}(S,m)=\{w\in S:w-m\notin S\}.
\]
Choose the lexicographically least factorization in \(a_1,a_2,a_3\) of each Apéry element, and let \(T\subseteq\mathbb N^3\) be the resulting exponent set. These representatives form a lower ideal: if \(y\le x\in T\), its label is Apéry, and any lexicographically earlier factorization of \(y\)'s label would also give an earlier factorization of \(x\)'s label. The labels \(a\cdot x\) represent all residues modulo \(m\) exactly once; hence \(|T|=m\).

Set
\[
A=\min_i a_i\ge m+1,\quad b=a/A,\quad s=\sum_{x\in T}x,
\]
\[
M=\max\operatorname{Ap}(S,m)=c+m-1,\quad H=M/A,\quad
R=\max_{x\in T}|x|_1,
\]
\[
D_0=3mH-4b\cdot s.
\]
The Apéry genus formula gives
\[
\boxed{mW_4=AD_0-m(m-1).} \tag{G1}
\]
Indeed, \(g=(a\cdot s)/m-(m-1)/2\) and \(n=c-g\). The inequality \(H\ge R\) follows from \(b_i\ge1\).

### Arithmetic structure of the ideal

A minimal excluded point is an exponent outside \(T\) whose immediate predecessors in every positive coordinate belong to \(T\). Such a point and its included residue representative have disjoint supports: subtracting a common positive coordinate would otherwise give two distinct included points of the same residue. Distinct minimal exclusions sharing a positive coordinate likewise have different residues.

Consequently there is at most one full-support minimal exclusion \(p\). If it exists, its residue representative is zero. Every other minimal exclusion has support at most two. Intersecting the three coordinate-plane cylinders and deleting \(p+\mathbb N^3\) therefore reconstructs \(T\) exactly.

Two necessary restrictions will be used in the finite centroid theorem. Write \(p=(r,s,t)\) temporarily and \(n_i=1+\max_Tx_i\).

First, each plane has at most \(|p|_1-2\) mixed minimal exclusions. In the first two coordinates, let \(q=(u,v,0)\) be such an exclusion. Its representative is \(\gamma e_3\). Exclusions with \(u<r\) or \(v<s\) contribute at most \(r-1+s-1\), since mixed corners have distinct first coordinates and distinct second coordinates. Otherwise \(q-(r,s,0)\) is a nonzero point of \(T\), with the same residue as \((\gamma+t)e_3\). If \(\gamma+t<n_3\), residue injectivity is violated. Thus \(\gamma\ge n_3-t\), leaving at most \(t\) distinct representatives. The total is at most \(r+s+t-2\). This bound applies separately in each plane.

Second, define the exposed surfaces
\[
F_i=\{x\in T:x+e_i\notin T\}.
\]
Mixed excluded corners in planar slices inject by their residues into the complementary axis. A nonempty planar lower ideal has one more maximal point than mixed excluded corners. Summing over the \(n_k\) nonempty slices gives
\[
|F_i\cap F_j|\le2n_k,\qquad\{i,j,k\}=\{1,2,3\}. \tag{G2}
\]
Detailed versions of these predecessor arguments are retained in the archive. No erosion assumption is needed for the primary centroid theorem.

## 2. Explicit centroid witnesses

"""
centroid=between(local,'## 2. The centroid target','## 6. Direct proofs for unbounded families')
centroid='### The centroid target\n\n'+centroid
centroid=re.sub(r'^## \d+\. (.*)$',r'### \1',centroid,flags=re.M)
centroid=centroid.replace('### Finite coverage','#### Finite coverage').replace('### A shorter Wilf deduction','#### A shorter Wilf deduction')
centroid=centroid.replace('The earlier experiments used \\(U\\); the final simplified theorem uses \\(U_2\\).','The finite theorem below uses \\(U_2\\).')
centroid=centroid.replace('The class is larger than the previous 3,742,041-shape class because two\nfilters have been removed. The improvement is in the hypotheses, proof\nconstruction, and verification burden, not a reduction in this shape count.','These are ideal/profile cases after sorting the full corner, not numerical semigroups or all coordinate-permutation orbits. The weaker hypotheses enlarge the class; the simplification is in the witnesses and checking machinery.')
centroid=centroid.replace('The earlier comparison of \\(90/31\\) with \\(29/10\\) is unnecessary for\nthis residual low-degree class.','The high-height integer-negativity comparison in Section 3 is unnecessary for this residual low-degree class.')
# Enrich the compact coverage table with the genuinely required fallback counts.
counts=[('1,1,3','1,581,961','215'),('1,2,2','1,433,543','212'),('1,1,4','874,540','3'),('1,2,3','638,574','1'),('2,2,2','592,453','0'),('1,1,5','159,580','0'),('1,2,4','105,119','0'),('1,3,3','94,500','0'),('2,2,3','94,374','0')]
table='| Corner | Ideal/profile cases | Axis fallbacks |\n|---|---:|---:|\n'
for p,n,f in counts: table+=f'| \\(({p})\\) | {n} | {f} |\n'
table+='| **Total** | **5,574,644** | **431** |'
centroid=re.sub(r'\| Corner \| Shapes checked \|.*?\| \*\*Total\*\* \| \*\*5,574,644\*\* \|',lambda _:table,centroid,flags=re.S)
centroid=prefix_equations(centroid,'C')
partition=between(proof,'## 2. The exhaustive and disjoint case partition','## 3. Exact statements and sources of the retained inputs')
partition=partition.replace('Round 10 local-or-axis','Local-or-axis')
inputs=between(proof,'## 3. Exact statements and sources of the retained inputs','## 4. Final arithmetic, once for all branches')
inputs=re.sub(r'### 3\.5 The new local centroid lemma.*?(?=### 3\.6)',r'''### Residual degree at most six

The theorem in Section 2 applies. The lower bound on the corner sum is the definition of the residual branch; its upper bound is automatic because each predecessor of the corner has degree at most six. The two arithmetic restrictions were proved in Section 1. Thus the conclusion is \\(D_0\\ge m\\), for every normalized weight vector, regardless of height.

''',inputs,flags=re.S)
inputs=re.sub(r'^### 3\.\d+ (.*)$',r'### \1',inputs,flags=re.M)
inputs=inputs.replace('Published multiplicity-through-19 source identified in the earlier manuscript: Kliem and Stump, '+chr(96)+'https://arxiv.org/html/1905.01945v2'+chr(96)+', together with its cited predecessor through 18. This external input must stay explicit in a publication manuscript and its bibliographic statement should be checked directly.','Published input: [Bruns, García-Sánchez, O’Neill and Wilburne](https://arxiv.org/abs/1903.04342) prove the conjecture through multiplicity 18; [Kliem and Stump](https://arxiv.org/abs/1905.01945) extend it to multiplicity 19.')
inputs=re.sub(r'The separate computation over \\\(m=30,\\ldots,48\\\).*?preferred presentation\.', 'The archived short-corner generator enumeration is an alternative, not a dependency of this chosen route.',inputs,flags=re.S)
# Keep long path lists in the archive's proof map rather than the reading text.
inputs=re.sub(r'Sources:\n\n(?:- .*\n)+', 'Detailed proofs, implementation sources, and completed records are indexed in the accompanying proof map.\n',inputs)
inputs=inputs.replace('The certificate SHA-256 is '+chr(96)+'173fe6ec196b3d2adabad313749482542ad3492b5f6b4e398e76bbe6e52e405c'+chr(96)+'.','Its certificate hash is preserved in the proof map and archive manifest.')
inputs=prefix_equations(inputs,'G')
arithmetic=between(proof,'## 4. Final arithmetic, once for all branches','## 5. What should be removed from the main proof presentation')
arithmetic=prefix_equations(arithmetic,'G')
global_part='\n\n## 3. Composition of the four-generator argument\n\n'+partition+'\n\n'+inputs+'\n\n### Final arithmetic\n\n'+arithmetic+'\n\nThese implications complete the proposed case composition, conditional on the retained theorems and finite verifications whose proofs and records accompany this manuscript. The reading text does not replace those technical dependencies.\n'
families=between(local,'## 6. Direct proofs for unbounded families','## 7. What is still missing from an analytic replacement')
families='\n\n## 4. Analytic families without enumeration\n\n'+families
dimensions=dims.split('## 1. The arithmetic and centroid formulations in arbitrary dimension',1)[1].split('## 7. A focused continuation',1)[0].strip()
dimensions='### The arithmetic and centroid formulations in arbitrary dimension\n\n'+dimensions
dimensions=re.sub(r'^## \d+\. (.*)$',r'### \1',dimensions,flags=re.M)
dimensions='\n\n## 5. Extensions to higher embedding dimensions\n\nThe formulas below distinguish general identities from sufficient structural families and unproved coverage claims. No novelty claim is made for the identities or special families.\n\n'+dimensions
closing=r"""
## 6. Simplifications, evidence, and remaining limitations

### What has become simpler

The primary residual lemma is now a statement about two explicit quantities, \(U_2(T)\) and \(G(T)\). Its proof uses elementary convex combinations; it needs no per-shape LP bases, determinants, or rational certificate stream. The stronger bound \(D_0\ge m\) gives \(W_4\ge2\) directly in that class. The erosion and refined dominating-corner filters have been removed from this lemma, though related restrictions remain in other arguments.

The global partition uses integer degree: \(R\le6\) invokes the explicit witnesses, while \(R\ge7\) implies \(H\ge7\). This avoids a weight-dependent boundary in the primary centroid computation. Earlier eventual-multiplicity thresholds, duplicate low-height certificate streams, and alternative short-corner generator searches are not needed simultaneously. Their records are retained as history and alternative evidence.

A complete proof without finite computation has not been obtained. The exact unresolved *simplification target* is to prove structurally that the stated residual corner and surface hypotheses force
\[
\max\{U_2(T),G(T)\}\ge|T|.
\]
This implication has been checked exhaustively on the finite class; it is not an uncovered case in the proposed computer-assisted argument.

### Reproducibility and scope of the evidence

The consolidated archive includes a proof map, original retained proofs, source code, certificates, and completed replay records. A manifest identifies the payload by SHA-256. Run the commands below from the extracted archive root.

For the primary residual theorem:
"""
ticks=chr(96)*3
closing+='\n'+ticks+'text\npython3 round10/local_centroid/verify_complete_local_centroid.py\n'+ticks+'\n'
closing+=r"""
This portable driver compiles the independent C++17 enumeration, checks all nine coverage totals and the coordinate-line identities, and reconstructs the 431 axis fallbacks using Python fractions. The archived full run passed. This component requires no external optimizer.

For the alternative parameter-envelope theorem:
"""
closing+='\n'+ticks+'text\npython3 round10/envelope/verify_universal_envelope.py\n'+ticks+'\n'
closing+=r"""
The independent verifier rebuilds the rows and checks exact rational multipliers with standard-library integer arithmetic. Its archived complete run passed. It is an alternative to the primary centroid component, not an extra mandatory gate.

The retained global branches have their own verifiers and analytic reductions. The proof map lists those sources and completed records. Source inspection, hash validation, bounded symbolic checks, full finite replay, and external mathematical review are distinct forms of evidence. The editorial pass producing this reading manuscript checked consistency and presentation; it did not rerun every global calculation.

### Limits and promising next improvements

The two explicit witnesses do not provide a universal coverage theorem for arbitrary lower ideals. Local moves alone fail on eligible shapes, and one-step moves plus the axis witness also fail. Removing every mixed-plane-corner restriction permits examples where even unrestricted monotone moves and the axis construction miss the target. These are failures of a proposed criterion, not counterexamples to Wilf or necessarily to the centroid inequality.

The most useful further simplification is a structural proof of the two-witness alternative for the stated residual class. A second possibility is a short symbolic rule for the parameter-envelope multipliers in Appendix A. Neither has been established here. The clipped-box and clipped-prism identities give infinite test families, but do not classify all admissible ideals.

Beyond four generators, the moment identity, integer contradiction threshold, and explicit witness formulas survive. What remains missing is a higher-dimensional coverage theorem that handles equality families, compatibility cycles, and intermediate-support exclusions. The separate fixed-dimension finite reduction has its own analytic review obligations and enormous bounds; it does not supply a practical five-generator verification.

The proposed four-generator proof should therefore be assessed through its complete analytic dependency chain and exact finite coverage, with external mathematical review still outstanding.
"""
envelope=local.split('## 9. A second completed route: no enumeration of individual ideals',1)[1].strip()
envelope=prefix_equations(envelope,'A')
envelope=envelope.replace('A separate argument developed during this investigation removes','A separate argument removes')
envelope='\n\n## Appendix A. Universal parameter certificates as an alternative\n\n'+envelope
refs=r"""
## References and technical source guide

The classical weighted-ideal and asymptotic literature provides context, not external validation of the new proposed proof.

1. W. Bruns, P. A. García-Sánchez, C. O’Neill and D. Wilburne, *Wilf’s conjecture in fixed multiplicity* (2019). [arXiv:1903.04342](https://arxiv.org/abs/1903.04342). Published multiplicities through 18.
2. L. Kliem and C. Stump, *A new face iterator for polyhedra and more general finite locally branched lattices* (2019; revised 2020). [arXiv:1905.01945](https://arxiv.org/abs/1905.01945). Published multiplicity 19.
3. A. Zhai, *An asymptotic result concerning a question of Wilf* (2011). [arXiv:1111.2779](https://arxiv.org/abs/1111.2779). Approximate fixed-embedding-dimension bounds must be distinguished from exact eventual Wilf.
4. M. Hellus, J. Rechenauer and R. Waldi, *Variants on a question of Wilf* (2018). [arXiv:1804.06141](https://arxiv.org/abs/1804.06141). Weighted lower ideals and sufficient cases.
5. M. Delgado, S. Eliahou and J. Fromentin, *Wilf’s conjecture and numerical semigroups with genus up to 100* (2023). [arXiv:2310.07742](https://arxiv.org/abs/2310.07742). Genus-bounded verification is a different finite restriction.

The archive's current source map is round11/proof_map.md. The final local theorem and portable verifier are in round10/local_centroid; the alternative envelope is in round10/envelope; the analytic family proofs are in round10/symbolic. The higher-dimensional derivations and editorial audit are in round11. Earlier global reductions and completed records retain their original relative paths, as indexed by the proof map. The large historical research manuscript is preserved for provenance; its interleaved checkpoints are superseded by the case partition in the present reading manuscript.
"""
out=front+centroid+global_part+families+dimensions+closing+envelope+refs
out=out.replace('\u2011','-').replace('\u00a0',' ')
(root/'deliverables/wilf_four_generators_review_manuscript_2026-09-11.md').write_text(out)
print('Manuscript:',len(out.split()),'words;',len(out),'characters')
