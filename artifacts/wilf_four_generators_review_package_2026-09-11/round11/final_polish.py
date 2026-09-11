from pathlib import Path
import re
p=Path('deliverables/wilf_four_generators_review_manuscript_2026-09-11.md')
s=p.read_text()
s=s.replace(r'\tag{A9}',r'\tag{A1}').replace('(A9)','(A1)')
s=s.replace(r'Indeed, \(g=(a\cdot s)/m-(m-1)/2\) and \(n=c-g\).',r'Indeed, the genus \(g=|\mathbb N\setminus S|\) satisfies \(g=(a\cdot s)/m-(m-1)/2\), and \(n=c-g\).')
s=s.replace('a full weighted ideal is first proved to satisfy Wilf;',r'a full weighted ideal \(T=\{x\in\mathbb N^3:a\cdot x\le M\}\) is first proved to satisfy Wilf;')
s=s.replace('## Appendix A. Universal parameter certificates as an alternative\n\n','## Appendix A. Universal parameter certificates as an alternative\n\nThis appendix concerns the degree-six residual class: \\(m\\ge30\\), exactly one full-support corner \\(p\\), and \\(5\\le|p|_1\\le7\\), with the original arithmetic restrictions, including erosion and the refined dominating-plane-corner bound. It is a separate route from the weaker-hypothesis theorem in Section 2.\n\n')
lines=[]
for line in s.splitlines():
    if line.startswith('|'):
        line=re.sub(r'\\\((.*?)\\\)',lambda m:r'\('+m[1].replace('|',r'\vert ')+r'\)',line)
    lines.append(line)
p.write_text('\n'.join(lines)+'\n')
p=Path('round11/build_reading_pdf.py')
s=p.read_text()
s=s.replace("for title in ['2. Explicit','3. Composition','4. Analytic','5. Extensions','6. Simplifications','Appendix A.','References and']:","for title in []:")
s=s.replace(r'\titlespacing*{\section}{0pt}{0pt}{12pt}',r'\titlespacing*{\section}{0pt}{20pt}{12pt}')
p.write_text(s)
