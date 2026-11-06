"""Check reviewed binary assets before an authorized GitHub release."""
from pathlib import Path
import hashlib
import json
import zipfile
ROOT=Path(__file__).resolve().parents[1]
meta=json.loads((ROOT/'release.json').read_text(encoding='utf-8'))
pub=ROOT/'publication'
lines=(pub/f'SHA256SUMS-{meta["tag"]}.txt').read_text(encoding='utf-8').splitlines()
for line in lines:
    digest,name=line.split('  ',1)
    p=pub/name
    assert hashlib.sha256(p.read_bytes()).hexdigest()==digest,name
    if name.endswith('.zip'):
        with zipfile.ZipFile(p) as z:
            assert z.testzip() is None
            if name.endswith('tex.zip'):
                assert 'main.tex' in z.namelist()
                assert 'v1-collar.tex' in z.namelist()
                assert 'v1-constructions.tex' in z.namelist()
                assert 'v1-record.tex' in z.namelist()
                assert not any(n.endswith('.lean') for n in z.namelist())
print(f'Verified {len(lines)} reviewed release assets by SHA-256 and ZIP CRC.')
