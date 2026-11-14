"""Shared data access for the weak-independence certificate.

Data files (zeros and residues) live in the directory given by the
environment variable CERT_DATA, default ./data next to this file.
"""
import os, glob, gzip, pickle

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.environ.get("CERT_DATA", os.path.join(HERE, "data"))
BHI = 11200   # precision (bits) of the stored high-precision zeros


def load_residues():
    """List of (j, gamma_j, Re A_j, Im A_j) as Arb ball strings, j = 1, 2, ..."""
    Z = []
    for f in sorted(glob.glob(os.path.join(DATA, "lz_*.pkl"))):
        Z += pickle.load(open(f, "rb"))
    Z.sort(key=lambda z: z[0])
    assert [z[0] for z in Z] == list(range(1, len(Z) + 1)), "residue files must cover 1..m without gaps"
    return Z


def load_x(b):
    """dict j (1-based) -> (x_j, d_j) with x_j = round(2^b gamma_j) and rigorous |x_j - 2^b gamma_j| <= d_j."""
    D = {}
    for f in sorted(glob.glob(os.path.join(DATA, "hz_%d_*.pkl" % BHI))):
        for (j, xi, d, s) in pickle.load(open(f, "rb")):
            if b == BHI:
                D[j] = (xi, d)
            else:
                sh = BHI - b
                xb = (xi + (1 << (sh - 1))) >> sh
                # |xb - 2^b g| <= |xb - xi/2^sh| + |xi - 2^BHI g|/2^sh <= 1/2 + d/2^sh
                D[j] = (xb, 0.5 + (d / 2.0 ** sh if sh < 1000 else 0.0) + 1e-12)
    return D


def load_basis(path):
    """Read U and Gamma_0 (0-based indices) from a U_*.txt.gz file."""
    U, G0 = [], None
    with gzip.open(path, "rt") as f:
        for line in f:
            if line.startswith("# G0"):
                G0 = [int(t) for t in line.split(":", 1)[1].split()]
            elif not line.startswith("#"):
                U.append([int(t) for t in line.split()])
    return U, G0


def select(n, m, Z):
    """Indices (0-based) of the n ordinates among gamma_1..gamma_m with the largest k(gamma)|A_gamma|,
    k the Jurkat-Peyerimhoff kernel with T = gamma_{m+1}.  Any choice is admissible; this is an optimisation."""
    import math
    P = lambda s: float(s.split()[0][1:])
    T = P(Z[m][1])
    w = []
    for j in range(m):
        t = P(Z[j][1]) / T
        k = (1 - t) * math.cos(math.pi * t) + math.sin(math.pi * t) / math.pi
        w.append((-k * abs(complex(P(Z[j][2]), P(Z[j][3]))), j))
    return sorted(j for _, j in sorted(w)[:n])
