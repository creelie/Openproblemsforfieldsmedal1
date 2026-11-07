# Zero-Free Criteria from Signed Liouville Energies

Current research release [v2.8.0](https://github.com/creelie/Openproblemsforfieldsmedal1/releases/tag/v2.8.0). Version DOI: [10.5281/zenodo.24044460](https://doi.org/10.5281/zenodo.24044460).

Signed Liouville energies characterize zero-free half-planes for the zeta function. We derive a quantitative weighted-energy certificate and its pole-order boundary cost, together with exact decomposition and Abel-obstruction results. The critical energy upper bound needed for RH and the corresponding Dirichlet GRH bounds remain unproved.

## Current manuscript

- [PDF](papers/RH.pdf)
- [Compilable TeX ZIP](papers/RHtex.zip)
- [Next-version submission notes](papers/next-version-submission-notes.md)
- [AI provenance](papers/aiprovenance.md)
- [Release details](papers/release-details.md)

## Scope

The upper bound for the critical Liouville energy, or equivalently finiteness of every weighted energy J(sigma) for sigma > 1/2, is not proved. Dirichlet GRH is not proved.

## Source and checking

Current source is in `paper/`. Compile `main.tex` with pdfLaTeX at least three times. Ancillary scripts in `paper/anc/` document their own finite scope. Historical verification records and independent research material are retained outside `papers/`. Earlier manuscript versions are available through release tags, rather than duplicate active PDFs and ZIPs.

Adds the weighted Mellin energy certificate and a quantitative lower bound at a pole.
