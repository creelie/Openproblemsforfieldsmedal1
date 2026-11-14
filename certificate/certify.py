"""Ball-arithmetic value of the right side of (A:eq:weakind) and the Anderson-Stark bounds for L(x)/sqrt(x).

usage: python3 certify.py U_file m q
Kernel: Jurkat-Peyerimhoff with T = gamma_{m+1} - 1e-6, so gamma_m < T < gamma_{m+1}.
"""
import sys
from flint import arb, acb, ctx
from common import load_residues, load_basis

Ufile = sys.argv[1]; m, q = int(sys.argv[2]), int(sys.argv[3])
_, G0 = load_basis(Ufile); assert max(G0) < m
Z = load_residues()
ctx.prec = 128
g = [arb(z[1]) for z in Z]; A = [acb(arb(z[2]), arb(z[3])) for z in Z]
pi = arb.pi(); T = g[m] - arb("1e-6"); assert T > g[m - 1]


def kJP(x):
    t = x / T
    return (1 - t) * (t * pi).cos() + (t * pi).sin() / pi


def gram(s, z):   # <w_s, w_z> in L^2((0,1); C^2)
    zc = z.conjugate()
    return 1 - 1 / (1 + s) - 1 / (1 + zc) + 2 / (1 + s + zc)


a = -1 / acb(0.5).zeta().real
coef = [(acb(0.5), a)]; S = arb(0)
for i in G0:
    S += kJP(g[i]) * abs(A[i])
    bb = 2 * arb(q) / (q + 1) * kJP(g[i]) * abs(A[i]); rho = acb(0.5, g[i])
    coef += [(rho, bb / 2), (rho.conjugate(), bb / 2)]
tot = acb(0)
for (s, c) in coef:
    for (z, d) in coef:
        tot += c * d * gram(s, z)
print("|Gamma_0| = %d, q = %d, kernel T = gamma_%d - 1e-6" % (len(G0), q, m + 1))
print("sum k_T|A| =", S.str(15))
print("liminf L/sqrt x <=", (-a - 2 * arb(q) / (q + 1) * S).str(12))
print("limsup L/sqrt x >=", (-a + 2 * arb(q) / (q + 1) * S).str(12))
print("limsup Q(N)/N   >=", tot.real.str(15))
