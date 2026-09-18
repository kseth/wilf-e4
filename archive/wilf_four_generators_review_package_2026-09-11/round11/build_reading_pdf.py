from pathlib import Path
import subprocess, re, io, json
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from pypdf import PdfReader, PdfWriter

ROOT=Path(__file__).resolve().parents[1]
TMP=ROOT/'round11/pdf_build'
TMP.mkdir(exist_ok=True)
MD=ROOT/'deliverables/wilf_four_generators_review_manuscript_2026-09-11.md'
s=MD.read_text().replace(r'\nu=|P|',r'u=|P|')
s=re.sub(r'\n+(?=#+ )','\n\n',s)
MD.write_text(s)
body=s.split('### Abstract',1)[1].strip()
body='## Abstract\n\n'+body
# Math symbols in pipe tables must not be mistaken for column delimiters.
lines=[]
for line in body.splitlines():
    if line.startswith('|'):
        line=re.sub(r'\\\((.*?)\\\)',lambda m:r'\('+m[1].replace('|',r'\vert ')+r'\)',line)
    lines.append(line)
body='\n'.join(lines)
body=re.sub(r'^## ([^\n]+)$',r'# \1',body,flags=re.M)
body=re.sub(r'^### ([^\n]+)$',r'## \1',body,flags=re.M)
body=re.sub(r'^#### ([^\n]+)$',r'### \1',body,flags=re.M)
# Add a page break after the abstract; major sections begin on a fresh page.
body=body.replace('# 1. Main claim',r'\clearpage'+'\n\n# 1. Main claim')
for title in []:
    body=body.replace('# '+title,r'\clearpage'+'\n\n# '+title)
(TMP/'body.md').write_text(body)
header=r"""
\usepackage{xcolor}
\usepackage{titlesec}
\usepackage{needspace}
\usepackage{microtype}
\definecolor{ink}{HTML}{173344}
\definecolor{accent}{HTML}{157F82}
\titleformat{\section}{\Large\bfseries\color{ink}}{}{0em}{}
\titleformat{\subsection}{\large\bfseries\color{ink}}{}{0em}{}
\titleformat{\subsubsection}{\normalsize\bfseries\color{ink}}{}{0em}{}
\titlespacing*{\section}{0pt}{20pt}{12pt}
\titlespacing*{\subsection}{0pt}{15pt}{6pt}
\setlength{\parskip}{5pt}
\setlength{\emergencystretch}{3em}
\setcounter{secnumdepth}{0}
\AtBeginDocument{\hypersetup{colorlinks=true,linkcolor=ink,urlcolor=accent}}
\pagestyle{empty}
\AtBeginEnvironment{longtable}{\small}
\let\oldsection\section
\renewcommand{\section}{\Needspace{7\baselineskip}\oldsection}
"""
(TMP/'header.tex').write_text(header)
cmd=['pandoc',str(TMP/'body.md'),'-f','markdown+tex_math_single_backslash','--standalone','--toc','--toc-depth=1','--pdf-engine=xelatex',
     '-V','documentclass=article','-V','papersize=a4','-V','fontsize=11pt',
     '-V','geometry:top=23mm,bottom=23mm,left=23mm,right=23mm',
     '-V','mainfont=Latin Modern Roman','-V','sansfont=Latin Modern Sans','-V','monofont=Latin Modern Mono',
     '-V','linestretch=1.04','--include-in-header',str(TMP/'header.tex')]
# Keep editable TeX, and compile separately so layout warnings remain inspectable.
tex=ROOT/'round11/wilf_four_generators_review_manuscript.tex'
res=subprocess.run(cmd+['-t','latex','-o',str(tex)],capture_output=True,text=True)
if res.returncode: raise RuntimeError(res.stderr)
for _ in range(2):
    res=subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error','-output-directory',str(TMP),str(tex)],capture_output=True,text=True)
    (TMP/'compile_stdout.txt').write_text(res.stdout+res.stderr)
    if res.returncode: raise RuntimeError((res.stdout+res.stderr)[-6000:])
bodypdf=TMP/'wilf_four_generators_review_manuscript.pdf'
W,H=A4
cover=TMP/'cover.pdf'
c=canvas.Canvas(str(cover),pagesize=A4)
c.setTitle("Wilf's inequality for four generators")
c.setFillColor(HexColor('#173344'));c.rect(0,0,W,H,fill=1,stroke=0)
c.setFillColor(HexColor('#2EB8AE'));c.rect(52,H-107,48,4,fill=1,stroke=0)
c.setFillColor(HexColor('#AEDDD9'));c.setFont('Helvetica',10)
c.drawString(52,H-78,'MATHEMATICAL RESEARCH  /  REVIEW MANUSCRIPT')
c.setFillColor(white);c.setFont('Times-Roman',34)
c.drawString(52,H-167,"Wilf's inequality")
c.drawString(52,H-209,'for four generators')
c.setFillColor(HexColor('#D8E7ED'));c.setFont('Helvetica',13)
for i,line in enumerate(['A proposed computer-assisted proof,','explicit centroid witnesses, and dimensional limits']):
    c.drawString(53,H-252-20*i,line)
c.setStrokeColor(HexColor('#41616D'));c.line(52,H-310,W-52,H-310)
style=ParagraphStyle('cover',fontName='Helvetica',fontSize=11,leading=17,textColor=HexColor('#E0EAEE'))
items=[
('EXPLICIT CONSTRUCTIONS','Two-step endpoint moves and axis combinations replace per-ideal optimization certificates in the residual class.'),
('COMPLETE PROOF MAP','The four-generator case partition identifies every retained analytic and computational dependency.'),
('EXTENSIONS AND LIMITS','General moment identities and infinite sufficient families, with concrete obstructions in five-generator ideals.')
]
y=H-346
for title,desc in items:
    c.setFillColor(HexColor('#6BD4CA'));c.setFont('Helvetica-Bold',9);c.drawString(53,y,title)
    p=Paragraph(desc,style);_,h=p.wrap(W-108,100);p.drawOn(c,53,y-12-h);y-=105
c.setFillColor(HexColor('#112733'));c.roundRect(42,60,W-84,104,8,fill=1,stroke=0)
p=Paragraph('<b>Proposed research proof.</b> Recorded exact checks have passed. External mathematical review and proof-assistant formalization remain outstanding.',style)
_,h=p.wrap(W-126,90);p.drawOn(c,63,146-h)
c.setFillColor(HexColor('#ADC5CD'));c.setFont('Helvetica',9);c.drawString(63,79,'11 September 2026  |  Reading edition with technical archive')
c.save()
reader=PdfReader(str(bodypdf))
writer=PdfWriter()
writer.append(reader,import_outline=True)
writer.insert_page(PdfReader(str(cover)).pages[0],0)
# Footer overlays retain the mathematical body and all clickable annotations.
for i,page in enumerate(list(writer.pages)[1:],1):
    stream=io.BytesIO();footer=canvas.Canvas(stream,pagesize=A4)
    footer.setStrokeColor(HexColor('#CBD8DE'));footer.setLineWidth(.5);footer.line(65,42,W-65,42)
    footer.setFillColor(HexColor('#5A6B73'));footer.setFont('Helvetica',8)
    footer.drawString(65,29,'Wilf / Four generators / Proposed research proof')
    footer.drawRightString(W-65,29,str(i))
    footer.save();stream.seek(0)
    page.merge_page(PdfReader(stream).pages[0])
writer.add_metadata({'/Title':"Wilf's inequality for four generators",'/Subject':'Proposed computer-assisted proof, centroid simplifications and dimensional limits','/Author':'Research manuscript prepared with ChatGPT','/Keywords':'Wilf conjecture; numerical semigroup; Apery ideal; centroid; computer-assisted proof'})
out=ROOT/'deliverables/wilf_four_generators_review_manuscript_2026-09-11.pdf'
with out.open('wb') as f: writer.write(f)
log=(TMP/'wilf_four_generators_review_manuscript.log').read_text(errors='replace')
warnings=[x for x in log.splitlines() if 'Overfull' in x or 'Missing character' in x]
(TMP/'layout_warnings.json').write_text(json.dumps(warnings,indent=2))
print(json.dumps({'pdf':str(out),'pages':len(writer.pages),'bytes':out.stat().st_size,'layout_warnings':warnings},indent=2))
