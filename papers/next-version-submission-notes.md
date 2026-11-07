# Next-version submission notes

Title: Zero-Free Criteria from Signed Liouville Energies

Authors in manuscript order: Deep Bhattacharjee; Ushashi Bhattacharya

Submission route: Preprints.org, v1 to v2. The platform version is independent of GitHub release numbering.

Existing record: [v1](https://doi.org/10.20944/preprints202606.1350.v1). The v2 identifier is not claimed to exist before submission is accepted by the platform.

Research release: [v2.8.1](https://github.com/creelie/Openproblemsforfieldsmedal1/releases/tag/v2.8.1). Version DOI: [10.5281/zenodo.24045618](https://doi.org/10.5281/zenodo.24045618).

## Abstract to paste

Signed Liouville energies characterize zero-free half-planes for the zeta function. We derive a quantitative weighted-energy certificate and its pole-order boundary cost, together with exact decomposition and Abel-obstruction results. The critical energy upper bound needed for RH and the corresponding Dirichlet GRH bounds remain unproved.

## Changes in this revision

Adds the weighted Mellin energy certificate and a quantitative lower bound at a pole. Earlier manuscript material is retained. The title is unchanged. The abstract is shortened. Current submission files replace superseded compiled copies on the main branch.

## Scope that must remain visible

The upper bound for the critical Liouville energy, or equivalently finiteness of every weighted energy J(sigma) for sigma > 1/2, is not proved. Dirichlet GRH is not proved.

## Files

- `RH.pdf` is the current compiled manuscript.
- `RHtex.zip` has `main.tex` at its root, with required figures and ancillary checks.
- `aiprovenance.md` records the origin and checking scope of this revision.
- `release-details.md` identifies the current release and DOI.

Compile with pdfLaTeX at least three times. Upload the TeX ZIP when the platform compiles sources. Do not upload superseded PDFs or use a new-version suffix as an already assigned identifier.

## Checks and declarations

The current source compiles locally. Finite ancillary checks do not prove the remaining existence or uniform estimates. This revision has not supplied a new Lean formalization of its analytic or geometric arguments. The submitting authors must confirm the human-understanding, authorship, licence and platform declarations for the current additions.


## Bibliography and layout in v2.8.1

Corrects the Matomäki–Radziwiłł–Tao and Teräväinen journal records, completes publication metadata, adds verified DOI links, and merges the duplicate Titchmarsh entry. The compiled manuscript has 75 pages. See `bibliography-audit.md` for the source of every retained reference.
