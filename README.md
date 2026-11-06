# Riemann Hypothesis research

**Signed Liouville energies and the limits of maximal correlation bounds**  
Deep Bhattacharjee and Ushashi Bhattacharya. Version 2 research draft, 6 November 2026.

This revises [Preprints.org version 1](https://doi.org/10.20944/preprints202606.1350.v1). It develops two routes that bypass Chowla, through an exponentially smoothed Liouville sum and through balanced reciprocal-dilate approximation. The Riemann Hypothesis remains open. The revised paper distinguishes the results proved here, deductions from stated zero-free assumptions, and recent outside research.

- `paper/main.tex` is the TeX entry point. It includes the two other TeX files in the same directory. Figures are built with TikZ.
- `output/pdf/signed-liouville-energies-v2.pdf` is the compiled manuscript.
- `checks/verify.py` runs exact finite checks with the Python standard library.
- `docs/RESEARCH.md` records the proof routes, source scope, and author metadata.

From `paper/`, run `latexmk -pdf main.tex` or run `pdflatex main.tex` three times to resolve the references. From the repository root, run `python checks/verify.py`.

The signed Fejér energy has growth exponent twice the supremum of real parts of the nontrivial zeta zeros. The absolute collar would imply Dirichlet GRH. A deterministic Gram argument disproves its zero-loss endpoint for every sign sequence. The reciprocal-dilate results give a fixed-taper obstruction and an explicit coefficient-cost inequality for adaptive approximants. The character version supplies an equivalent signed-energy target for Dirichlet GRH. These statements use the inputs specified in the paper. The finite checks verify formulas and examples at the recorded sizes.

OpenGluon is the upstream research workspace ([creelie/OpenGluon](https://github.com/creelie/OpenGluon)). The proof and checker in this draft are readable and runnable without cloning that workspace.
