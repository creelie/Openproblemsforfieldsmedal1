"""Certified zeros and residues A = zeta(2 rho)/(rho zeta'(rho)) at 192 bits.

usage: python3 lz.py start count          (writes $CERT_DATA/lz_<start>.pkl)
"""
import os, sys, time, pickle
from flint import acb, arb, ctx, acb_series
from common import DATA

ctx.prec = 192
s, cnt = int(sys.argv[1]), int(sys.argv[2])
os.makedirs(DATA, exist_ok=True)
t = time.time()
zs = acb.zeta_zeros(s, cnt)
out = []
for k, r in enumerate(zs):
    assert r.real == arb(0.5)
    zp = acb_series([r, 1], prec=2).zeta().coeffs()[1]
    A = (2 * r).zeta() / (r * zp)
    out.append((s + k, r.imag.str(60, radius=True), A.real.str(40, radius=True), A.imag.str(40, radius=True)))
pickle.dump(out, open(os.path.join(DATA, "lz_%05d.pkl" % s), "wb"))
print("residues %d..%d: %.1fs" % (s, s + cnt - 1, time.time() - t), flush=True)
