"""Gradual-feeding LLL (FLINT fmpz_lll, delta = 0.99) of Lambda_0 = <(e_j, x_j)>, with checkpointing.

usage: python3 lll.py n m b step maxsec
The stage at c bits uses round(x_j / 2^(b-c)).  When b bits are reached the matrix U is written to
U_<n>_<m>_<b>.txt.gz.  The output is not trusted: verify.py checks det U = +-1 and everything else exactly.
"""
import os, sys, time, pickle, gzip
from flint import fmpz_mat
from common import load_residues, load_x, select

n, m, b, step, maxsec = map(int, sys.argv[1:6])
G0 = select(n, m, load_residues()); X = load_x(b); x = [X[j + 1][0] for j in G0]
ck = "lll_%d_%d_%d.pkl" % (n, m, b)
t0 = time.time()
st = pickle.load(open(ck, "rb")) if os.path.exists(ck) else dict(cur=0, U=None, G0=G0)
assert st["G0"] == G0
while st["cur"] < b:
    nxt = min(st["cur"] + step, b); sh = b - nxt
    xx = [((xi + (1 << (sh - 1))) >> sh) if sh > 0 else xi for xi in x]
    U = st["U"]
    if U is None:
        rows = [[1 if j == i else 0 for j in range(n)] + [xx[i]] for i in range(n)]
    else:
        rows = [U[i] + [sum(U[i][j] * xx[j] for j in range(n))] for i in range(n)]
    t1 = time.time(); R = fmpz_mat(rows).lll(delta=0.99)
    st["U"] = [[int(R[i, j]) for j in range(n)] for i in range(n)]; st["cur"] = nxt
    pickle.dump(st, open(ck + ".tmp", "wb")); os.replace(ck + ".tmp", ck)
    last = time.time() - t1
    print("stage to %d bits: %.1fs (total %.1fs)" % (nxt, last, time.time() - t0), flush=True)
    if time.time() - t0 + 1.6 * last > maxsec:
        break
if st["cur"] >= b:
    with gzip.open("U_%d_%d_%d.txt.gz" % (n, m, b), "wt") as f:
        f.write("# rows of the unimodular matrix U, B = [U | Ux], n=%d, m=%d, b=%d\n" % (n, m, b))
        f.write("# G0 (0-based): " + " ".join(map(str, G0)) + "\n")
        for r in st["U"]:
            f.write(" ".join(map(str, r)) + "\n")
    print("DONE", flush=True)
else:
    print("PARTIAL", st["cur"], flush=True)
