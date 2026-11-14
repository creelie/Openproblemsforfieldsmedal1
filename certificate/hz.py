"""High-precision certified zeros: x_j = round(2^b gamma_j) with a rigorous bound for |x_j - 2^b gamma_j|.

usage: python3 hz.py start count [b]      (b defaults to 11200; writes $CERT_DATA/hz_<b>_<start>.pkl)
Arb's zeta_zeros certifies that the n-th zero lies on the critical line and certifies the count (Turing's method).
"""
import os, sys, time, pickle
from flint import acb, arb, ctx
from common import DATA, BHI

s, cnt = int(sys.argv[1]), int(sys.argv[2])
b = int(sys.argv[3]) if len(sys.argv) > 3 else BHI
os.makedirs(DATA, exist_ok=True)
ctx.prec = b + 64
t = time.time()
zs = acb.zeta_zeros(s, cnt)
two_b = arb(2) ** b
out = []
for k, r in enumerate(zs):
    assert r.real == arb(0.5)
    v = r.imag * two_b
    xi = int((v.mid() + arb(0.5)).floor().unique_fmpz())
    d = float((abs(v - xi)).upper())
    assert d < 0.5001
    out.append((s + k, xi, d, r.imag.str(30)))
fn = os.path.join(DATA, "hz_%d_%05d.pkl" % (b, s))
pickle.dump(out, open(fn + ".tmp", "wb")); os.replace(fn + ".tmp", fn)
print("zeros %d..%d: %.1fs, max d=%.6f" % (s, s + cnt - 1, time.time() - t, max(o[2] for o in out)), flush=True)
