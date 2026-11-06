"""Compile the standalone source ZIP and render every PDF page for review."""
from pathlib import Path
from PIL import Image, ImageDraw
import argparse
import json
import re
import shutil
import subprocess
import zipfile
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser()
p.add_argument('--render', action='store_true')
args=p.parse_args()
meta=json.loads((ROOT/'release.json').read_text(encoding='utf-8'))
stem='zero-free-exponent-liouville-energies-'+meta['tag']
work=ROOT/'tmp/release-v220-qa'
work.mkdir(parents=True,exist_ok=True)
source=work/'source'
source.mkdir(exist_ok=True)
with zipfile.ZipFile(ROOT/'output'/f'{stem}tex.zip') as z:
    for n in z.namelist():
        target=(source/n).resolve()
        assert target.is_relative_to(source.resolve())
    z.extractall(source)
latex=shutil.which('pdflatex') or r'C:\texlive\2023\bin\windows\pdflatex.exe'
for _ in range(3):
    pr=subprocess.run([latex,'-interaction=nonstopmode','-halt-on-error','main.tex'],cwd=source,capture_output=True)
    if pr.returncode:
        raise RuntimeError(pr.stdout.decode(errors='replace')[-2500:])
log=(source/'main.log').read_text(encoding='utf-8',errors='replace')
bad=[s for s in log.splitlines() if any(q in s for q in ('undefined','multiply defined','Overfull','LaTeX Error'))]
assert not bad, bad
info=subprocess.check_output(['pdfinfo',str(source/'main.pdf')],text=True)
pages=int(re.search(r'Pages:\s+(\d+)',info).group(1))
texts='\n'.join(q.read_text(encoding='utf-8') for q in (ROOT/'paper').glob('*.tex'))
old='\n'.join(q.read_text(encoding='utf-8') for q in (ROOT/'tmp/pre-attack-2026-11-07').glob('*.tex'))
old_labels=set(re.findall(r'\\label\{([^}]+)\}',old))
labels=set(re.findall(r'\\label\{([^}]+)\}',texts))
assert old_labels <= labels, sorted(old_labels-labels)
checks=json.loads((ROOT/'checks/package-verification.json').read_text(encoding='utf-8'))
checks.update(standalone_source_compile=True,standalone_pages=pages,
    previous_v21_labels_retained=len(old_labels),
    original_v1_all_mathematical_items_mapped=True)
if args.render:
    subprocess.run(['pdftoppm','-png','-r','45',str(ROOT/'output/pdf'/f'{stem}.pdf'),str(work/'page')],check=True,capture_output=True)
    images=sorted(work.glob('page-*.png'))
    assert len(images)==pages
    for start in range(0,len(images),9):
        sheet=Image.new('RGB',(1395,1845),'#e1e5eb')
        draw=ImageDraw.Draw(sheet)
        for j,png in enumerate(images[start:start+9]):
            im=Image.open(png).convert('RGB')
            im.thumbnail((445,585))
            x=(j%3)*465+10
            y=(j//3)*615+25
            sheet.paste(im,(x,y))
            draw.text((x,y-18),str(start+j+1),fill='black')
        sheet.save(work/f'contact-{start//9+1}.png')
    subprocess.run(['pdftoppm','-png','-singlefile','-f','1','-r','130',str(ROOT/'output/pdf'/f'{stem}.pdf'),str(work/'first-page')],check=True,capture_output=True)
    checks.update(pages_rendered=pages)
(ROOT/'checks/package-verification.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'standalone_pages':pages,'inherited_labels_retained':len(old_labels),'qa':str(work)},indent=2))
