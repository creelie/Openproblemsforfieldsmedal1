"""Rigorous check that Gamma_0 is q-independent below T, from a reduced basis.

usage: python3 verify.py U_file m b
(i)  exact Gram-Schmidt norms of B = [U | Ux] from the fraction-free LU of its integer Gram matrix;
(ii) for every ordinate gamma* <= gamma_m outside Gamma_0, exhaustive enumeration (Fincke-Pohst) around the
     orthogonal projection of x_{gamma*} e_{n+1}, with exact rational Gram-Schmidt data evaluated in Arb.
"""
import time, sys, math
from fractions import Fraction as Fr
from flint import fmpz_mat, fmpz, arb, ctx
from common import load_x, load_basis
Ufile = sys.argv[1]; m, b = int(sys.argv[2]), int(sys.argv[3]); qcap = 10**7
t0 = time.time()
U, G0 = load_basis(Ufile); n = len(G0); X = load_x(b); mt = m
x = [X[j+1][0] for j in G0]
assert max(G0) < mt <= m
targets = [j for j in range(1, mt+1) if (j-1) not in set(G0)]
delta = Fr(max(X[j][1] for j in range(1, mt+1)))          # rigorous, covers Gamma_0 and all targets
assert delta < Fr(1, 2) + Fr(1, 1000)
Um = fmpz_mat(U); dU = Um.det(); assert dU in (1, -1), dU      # B=[U|Ux] is a basis of Lambda_0
rows = [U[i] + [sum(U[i][j]*x[j] for j in range(n))] for i in range(n)]
Bp = fmpz_mat(rows + [[0]*n + [1]]); Gp = Bp*Bp.transpose()
Pm, L, Dm, Uu = Gp.fflu()
assert Pm == fmpz_mat([[1 if p == q else 0 for q in range(n+1)] for p in range(n+1)])
D = [fmpz(1)] + [Uu[i, i] for i in range(n+1)]                 # D[i+1] = i-th leading minor (0-based i)
assert all(d > 0 for d in D)
print("basis/Gram/fflu: %.1fs, max entry bits %d" % (time.time()-t0, max(abs(int(v)).bit_length() for r in rows for v in r[:n])), flush=True)
r = [Fr(int(D[i+1]), int(D[i])) for i in range(n)]            # |b_i*|^2 exactly
rmin = min(r); imin = r.index(rmin)
c0 = n*(1 + delta*delta*n)                                    # R0(q)^2 = (q+1)^2 c0
k = int(math.isqrt(int(rmin/c0)) + 2)
while k*k*c0 >= rmin: k -= 1
q0 = min(k - 1, qcap)
print("(i): min|b*|^2 = %.6e (index %d), max q with (i) certified: %d" % (float(rmin), imin, k-1), flush=True)
def R1sq(q): return n*q*q + (delta*(n*q + 1))**2
P = b + 256; ctx.prec = P
ra = [None]*n; mu = {}; v = [None]*n
def rr(i):
    if ra[i] is None: ra[i] = arb(int(D[i+1]))/arb(int(D[i]))
    return ra[i]
def MU(j, i):
    if (j, i) not in mu: mu[(j, i)] = arb(int(Uu[i, j]))/arb(int(D[i+1]))
    return mu[(j, i)]
def V(i):
    if v[i] is None: v[i] = arb(int(Uu[i, n]))/arb(int(D[i+1]))
    return v[i]
def cvp(xs, R2):
    """Return (min lower bound of |p-u|^2 over u with |p-u|^2 possibly <= R2, or None if none), nodes."""
    R2a = arb(R2.numerator)/arb(R2.denominator)
    best = [None]; nodes = [0]; xa = arb(xs)
    def rec(i, us, part):        # us: dict j->u_j for j>i chosen
        nodes[0] += 1
        if nodes[0] > 2_000_000: raise RuntimeError("enumeration too large")
        c = xa*V(i)
        for j, uj in us.items(): c -= uj*MU(j, i)
        cz = int(c.mid().floor().unique_fmpz()); f = float((c - cz).mid())
        rem = float((R2a - part).upper()); ri = rr(i)
        half = math.sqrt(max(rem, 0.0)/float(ri.lower()))*1.000001 + 1e-9
        for kk in range(math.floor(f - half) - 1, math.ceil(f + half) + 2):
            u = cz + kk; e = (c - u)**2*ri; np_ = part + e
            if np_.lower() > R2a.upper(): continue
            if i == 0:
                lb = float(np_.lower())
                if best[0] is None or lb < best[0]: best[0] = lb
            else:
                us2 = dict(us); us2[i] = u; rec(i-1, us2, np_)
    rec(n-1, {}, arb(0))
    return best[0], nodes[0]
R2max = R1sq(q0)
worst = None; totnodes = 0; t1 = time.time(); found = []
for js in targets:
    lb, nd = cvp(X[js][0], R2max); totnodes += nd
    if lb is not None: found.append((js, lb))
    if worst is None or nd > worst[1]: worst = (js, nd)
print("(ii): %d targets, %.1fs, total nodes %d, max nodes %d (gamma_%d); targets with a lattice point within R1(q0): %d"
      % (len(targets), time.time()-t1, totnodes, worst[1], worst[0], len(found)), flush=True)
q = q0
for js, lb in found:
    while q > 0 and float(R1sq(q)) >= lb*(1 - 1e-12): q -= 1
print("RESULT n=%d m=%d b=%d delta=%.6f: certified q-independent below gamma_%d for q = %d (q0 from (i) = %d)" % (n, m, b, float(delta), mt+1, q, q0), flush=True)
