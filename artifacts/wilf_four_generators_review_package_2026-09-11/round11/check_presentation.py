from pathlib import Path
from collections import Counter
import re,json,hashlib
import fitz
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parents[1]
md=root/'deliverables/wilf_four_generators_review_manuscript_2026-09-11.md'
pdf=root/'deliverables/wilf_four_generators_review_manuscript_2026-09-11.pdf'
s=md.read_text();tags=re.findall(r'\\tag\{([^}]+)\}',s)
assert len(tags)==len(set(tags))==25
refs=set(re.findall(r'\(((?:G|C|HD|A)\d+)\)',s))
assert refs<=set(tags)
assert r'\nu=|P|' not in s and r'\tag{A1}' in s
doc=fitz.open(pdf)
out=root/'round11/pdf_build'
issues=[];images=[];pages=[]
for i,page in enumerate(doc):
    pix=page.get_pixmap(matrix=fitz.Matrix(1.1,1.1),alpha=False)
    dest=out/f'inspected-{i+1:02}.png';pix.save(dest);images.append(dest)
    for block in page.get_text('dict')['blocks']:
        if 'lines' not in block:continue
        for line in block['lines']:
            for span in line['spans']:
                x0,y0,x1,y1=span['bbox']
                if x0<20 or x1>page.rect.width-20 or y0<15 or y1>page.rect.height-12:
                    issues.append({'page':i+1,'bbox':span['bbox'],'text':span['text']})
    pages.append({'page':i+1,'words':len(page.get_text().split()),'links':len(page.get_links())})
assert not issues,issues
assert len(doc.get_toc())==9
assert len(doc[1].get_links())==9
assert all(0<=x['page']<len(doc) for x in doc[1].get_links())
for j in range(0,len(images),8):
    sheet=Image.new('RGB',(1240,940),'#d9e0e3')
    for k,p in enumerate(images[j:j+8]):
        im=Image.open(p).convert('RGB');im.thumbnail((295,425))
        x=(k%4)*310+7;y=(k//4)*470+25
        sheet.paste(im,(x,y));ImageDraw.Draw(sheet).text((x,y-18),p.stem,fill='#173344')
    sheet.save(out/f'inspected-contact-{j//8+1}.png')
manifest_checks=[]
for folder,filename in [('round10/local_centroid','local_centroid_manifest.json'),('round10/envelope','artifact_manifest.json')]:
    manifest=json.loads((root/folder/filename).read_text())
    for name,v in manifest['files'].items():
        expected=v['sha256'] if isinstance(v,dict) else v
        assert hashlib.sha256((root/folder/name).read_bytes()).hexdigest()==expected,name
        manifest_checks.append(str(Path(folder)/name))
record={'status':'passed','scope':'Editorial artifact and stored-record consistency only; no new exhaustive mathematical replay','equation_tags':tags,'references_resolve':True,'pdf_pages':len(doc),'pdf_bookmarks':len(doc.get_toc()),'toc_links':9,'text_outside_safe_page_box':issues,'tex_overfull_or_missing_character_warnings':json.loads((out/'layout_warnings.json').read_text()),'stored_manifest_hashes_checked':len(manifest_checks),'page_details':pages,'files':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [md,pdf]}}
(root/'round11/presentation_checks.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k not in ['page_details','files','equation_tags']},indent=2))
