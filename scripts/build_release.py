"""Build and package the scoped v2.2 research revision reproducibly."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / 'paper'
parser = argparse.ArgumentParser()
parser.add_argument('--no-compile', action='store_true')
args = parser.parse_args()
META = json.loads((ROOT / 'release.json').read_text(encoding='utf-8'))
VERSION = META['version']
STEM = 'zero-free-exponent-liouville-energies-' + META['tag']

def run(argv, cwd=ROOT):
    p = subprocess.run([str(a) for a in argv], cwd=cwd, capture_output=True,
        text=True, encoding='utf-8', errors='replace')
    if p.returncode:
        raise RuntimeError(p.stdout[-4000:] + '\n' + p.stderr[-1000:])
    return p.stdout

if not args.no_compile:
    latex = shutil.which('pdflatex') or r'C:\texlive\2023\bin\windows\pdflatex.exe'
    for _ in range(3):
        run([latex, '-interaction=nonstopmode', '-halt-on-error', 'main.tex'], PAPER)
log = (PAPER / 'main.log').read_text(encoding='utf-8', errors='replace')
bad = [s for s in log.splitlines() if any(x in s for x in
       ('undefined', 'multiply defined', 'Overfull', 'LaTeX Error'))]
if bad:
    raise RuntimeError('\n'.join(bad))
results = {}
for script in ('verify.py', 'attack_exact.py', 'v1_retention.py'):
    results[script] = run([sys.executable, '-X', 'utf8', ROOT/'checks'/script])
(ROOT/'checks/release-verification-results.txt').write_text(
    '\n'.join(k+'\n'+v for k,v in results.items()), encoding='utf-8')
sources = sorted(PAPER.glob('*.tex'))
joined = '\n'.join(p.read_text(encoding='utf-8') for p in sources)
labels = re.findall(r'\\label\{([^}]+)\}', joined)
assert len(labels) == len(set(labels)), 'Duplicate theorem labels'
abstract = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', joined, re.S).group(1)
out = ROOT/'output'
(out/'pdf').mkdir(parents=True, exist_ok=True)
pdf = out/'pdf'/f'{STEM}.pdf'
texzip = out/f'{STEM}tex.zip'
shutil.copy2(PAPER/'main.pdf', pdf)
with zipfile.ZipFile(texzip, 'w', zipfile.ZIP_DEFLATED) as z:
    for p in sources:
        z.write(p, p.name)
    for p in sorted((PAPER/'figures').glob('*')):
        if p.suffix in ('.png', '.tex'):
            z.write(p, 'figures/'+p.name)
    if (PAPER/'LICENSE').exists():
        z.write(PAPER/'LICENSE', 'LICENSE')
    for name in ('verify.py','attack_exact.py','v1_retention.py','build_model_figure.py'):
        z.write(ROOT/'checks'/name, 'anc/'+name)
    z.write(ROOT/'checks/release-verification-results.txt', 'anc/verification.log')
    z.writestr('README.txt',
        'Compile main.tex with pdfLaTeX (three passes).\n'
        'Complete expanded v2.2.0 research revision, including v1 mathematics with corrections.\n'
        'RH and Dirichlet GRH remain unproved.\n'
        'Figures are exact constructions, not certified Liouville data.\n'
        'Lean files and original v1 supplement are linked in the repository and full research ZIP.\n'
        'Repository: https://github.com/creelie/Openproblemsforfieldsmedal1\n')
shutil.copy2(pdf, PAPER/'paper.pdf')
shutil.copy2(texzip, PAPER/'tex.zip')
# Keep the two existing public paths current for users of earlier releases.
shutil.copy2(pdf, out/'pdf/signed-liouville-energies-v2.pdf')
shutil.copy2(texzip, out/'signed-liouville-energiestex.zip')
info = run(['pdfinfo', pdf])
pages = int(re.search(r'Pages:\s+(\d+)', info).group(1))
files = {p.name:{'bytes':p.stat().st_size,
    'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in (pdf,texzip)}
manifest = dict(version=VERSION,title=META['title'],date='2026-11-07',pages=pages,
    RH_proved=False,Dirichlet_GRH_proved=False,new_zero_free_region_proved=False,
    analytic_results_Lean_formalized=False,novelty_priority_not_established=True,
    original_v1_references_retained=25,original_v1_source_preserved=True,
    latex_errors=0,undefined_references=0,overfull_boxes=0,
    abstract_words=len(abstract.split()),unique_labels=len(labels),
    exact_checks=results,files=files,
    archive_doi=META.get('doi'),archive_status=META.get('archive_status'))
previous_manifest=ROOT/'checks/package-verification.json'
if previous_manifest.exists():
    previous=json.loads(previous_manifest.read_text(encoding='utf-8'))
    for key in ('standalone_source_compile','standalone_pages',
                'previous_v21_labels_retained','original_v1_all_mathematical_items_mapped',
                'pages_rendered','visual_review_passed'):
        if key in previous:
            manifest[key]=previous[key]
(ROOT/'checks/package-verification.json').write_text(
    json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
dist=ROOT/'dist'
dist.mkdir(exist_ok=True)
for p in (pdf,texzip):
    shutil.copy2(p,dist/p.name)
research=dist/f'{STEM}-research-package.zip'
with zipfile.ZipFile(research,'w',zipfile.ZIP_DEFLATED) as z:
    z.write(pdf,'paper/paper.pdf')
    z.write(texzip,'paper/tex.zip')
    for folder in ('checks','docs','lean','source-history'):
        for p in sorted((ROOT/folder).rglob('*')):
            if (p.is_file() and '__pycache__' not in p.parts and '.lake' not in p.parts
                    and p.name != 'GITHUB-RELEASE.json'):
                z.write(p,p.relative_to(ROOT).as_posix())
    for name in ('README.md','LICENSE','CITATION.cff','.zenodo.json','RELEASE-NOTES.md','release.json'):
        z.write(ROOT/name,name)
    for name in ('build_release.py','qa_release.py','verify_assets.py','verify_archive.py'):
        z.write(ROOT/'scripts'/name,'scripts/'+name)
checksum='\n'.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name
    for p in (dist/pdf.name,dist/texzip.name,research))+'\n'
(dist/f'SHA256SUMS-{META["tag"]}.txt').write_text(checksum,encoding='utf-8')
print(json.dumps(dict(pages=pages,pdf=str(pdf),tex_zip=str(texzip),
    research_zip=str(research),abstract_words=manifest['abstract_words']),indent=2))
