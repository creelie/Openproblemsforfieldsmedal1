# Zeta Zeros and Signed Liouville Energies

A multipole theorem bounds the normalized Liouville energy from below by a sum of pole contributions. A positive Fejer weight and a certified finite calculation give an unconditional limsup lower bound strictly greater than 3257/5000. RH and Dirichlet GRH remain open.

[PDF](revision-v2.3.0/paper.pdf) · [TeX ZIP](revision-v2.3.0/tex.zip) · [Release](https://github.com/creelie/Openproblemsforfieldsmedal1/releases/tag/v2.3.0) · [Version DOI](https://doi.org/10.5281/zenodo.24025095)

<!-- current-2026-11-07-revision -->

## Earlier revision and repository guide

## Earlier revision and repository guide

# The Zero-Free Exponent of Signed Liouville Energies

Deep Bhattacharjee and Ushashi Bhattacharya · Research revision 2.2.0 · 7 November 2026

This expanded v2 retains the mathematical content of the original v1 with corrections. It proves identities, conditional criteria and counterexamples. **RH and Dirichlet GRH remain unproved.**

## Read and download

- [Paper PDF](paper/paper.pdf)
- [Complete compiling TeX ZIP](paper/tex.zip)
- [Release v2.2.0](https://github.com/creelie/Openproblemsforfieldsmedal1/releases/tag/v2.2.0)
- [Version DOI 10.5281/zenodo.24022872](https://doi.org/10.5281/zenodo.24022872)
- [Zenodo archive, all versions](https://doi.org/10.5281/zenodo.24014164)
- [Original v1](https://doi.org/10.20944/preprints202606.1350.v1)

## Results and limits

The signed Fejer energy has growth exponent exactly twice the rightmost-zero supremum. The paper derives zero-free and Dirichlet-character criteria, a local reconstruction kernel, the finite-prime comparison and logarithmic-order cancellation of its main term. The square-root remainder estimate is equivalent to RH and is not proved.

The maximal-correlation construction, its exponent figure, square-divisor expansion, terminal-range criterion and original literature context are integrated into the manuscript. [The v1 content map](docs/V1-CONTENT-MAP.md) records the changes. Original TeX and supplemental scripts are preserved under `source-history/v1/`.

## Reproduction

Compile `paper/main.tex` with pdfLaTeX, three passes. The source ZIP has `main.tex` at its root and contains all manuscript inputs and figures.

```sh
python checks/verify.py
python checks/attack_exact.py
python checks/v1_retention.py
python scripts/build_release.py
```

The exact finite checks complement the written proofs. They do not verify analytic asymptotics. The existing Lean file checks only the finite Gram-matrix core; the analytic results are not Lean-formalized. Its toolchain and axiom report are under `lean/`.

The original optional figure script requires NumPy and Matplotlib. The manuscript's exponent diagram uses native PGFPlots and needs no Python plotting library.

Authorship and AI assistance are separate: both named human authors remain credited; the paper records computational and AI-assisted preparation. No AI system is an author. License: CC BY 4.0.

The immutable release tag is archived by Zenodo. The attached PDF and TeX ZIP carry the subsequently verified version DOI; this bibliographic imprint does not alter the mathematical text.
