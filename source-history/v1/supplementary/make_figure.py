"""
Reproducibility script for the schematic comparison figure in Section 5
("Coefficient-uniform failure") of:

  Maximal Large Sieve and Coefficient Uniform Failure for Liouville Correlations
  Deep Bhattacharjee and Ushashi Bhattacharya, 2026

This script regenerates collar_gap_figure.pdf. It plots, on an exponent
axis u in [0,1] (with H = X^u), the two competing exponents:

  - coefficient-blind correlation energy exponent:   2 + u   (red)
  - exponent the Liouville collar argument needs:     2 - u   (blue)

and marks the explicit point u = 1/4 used in Theorem 5.2. No numerical
data about lambda(n) or any arithmetic function is computed; the figure
is a plot of two explicit linear functions of u together with one marked
point. The annotation is positioned away from the blue curve to avoid
visual overlap in narrow mobile PDF viewers.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

u = np.linspace(0, 1, 400)
energy_blind = 2 + u
energy_needed = 2 - u

fig, ax = plt.subplots(figsize=(6.0, 4.2))

ax.plot(u, energy_blind, color="#b22222", linewidth=2.0,
        label=r"coefficient-blind energy exponent $2+u$")
ax.plot(u, energy_needed, color="#1f4e96", linewidth=2.0,
        label=r"exponent the collar argument needs $2-u$")
ax.fill_between(u, energy_needed, energy_blind, where=(energy_blind >= energy_needed),
                 color="#b22222", alpha=0.08)

u0 = 0.25
ax.plot([u0], [2 + u0], marker="o", color="#b22222", markersize=5, zorder=5)
ax.annotate(r"$u=1/4$ (Theorem 5.2)",
            xy=(u0, 2 + u0), xytext=(0.33, 2.42),
            fontsize=8, color="#444444",
            bbox=dict(boxstyle="square,pad=0.12", fc="white", ec="none", alpha=0.95),
            arrowprops=dict(arrowstyle="-", color="#888888", lw=0.8,
                             shrinkA=2, shrinkB=5))

ax.set_xlabel(r"shift exponent $u$ where $H = X^{u}$")
ax.set_ylabel(r"exponent of $X$")
ax.set_xlim(0, 1)
ax.set_ylim(1.0, 3.1)
ax.legend(loc="upper center", fontsize=9, frameon=False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(alpha=0.25, linewidth=0.5)

fig.tight_layout()
fig.savefig("collar_gap_figure.pdf")
print("wrote collar_gap_figure.pdf")
