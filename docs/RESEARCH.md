# Research and source notes

## Version changes

The posted June 2026 v1 is the base manuscript. The attached submission ZIP contains the corresponding TeX and PDF. The supplementary ZIP contains exponent and figure scripts. The revision keeps the two original authors. It gives the missing partial-summation argument, handles shift 1 separately, specifies empty and integer endpoints, and ties the spectral maximal argument to a single supported fixed-endpoint Bessel bound.

The exact finite model proofs, analytic equivalences and counterexamples are in the manuscript. The Liouville endpoint obstruction uses Tao's published logarithmic two-point theorem. The optional 7/8 and ordinary two-point deductions explicitly invoke the respective OpenAI manuscripts. The research draft neither reproduces the full external quasi-Riemann argument nor relies on it for the principal equivalences.

## Proof targets

- **Signed Fejér energy:** prove Q(N) = O(N^(1+epsilon)) for every fixed epsilon > 0. This is equivalent to RH. The weighted energy keeps the signs of different shifts.
- **Exponential smoothing:** bound the single smoothed sum of lambda(n) exp(-n/X) by O(X^(1/2+epsilon)). The Gamma multiplier has no zeros in the tested half-plane. Divisor-convolution weights that contain a zeta factor cancel the poles of the inverse and cannot be used for that test.
- **Reciprocal dilates:** approximate the constant at the unweighted L² norm. An explicit Riesz-smoothed Möbius polynomial gives a power rate in shifted norms to the right of a fixed zero-free threshold. A rescaled Mellin test rules out critical-norm convergence for all fixed bounded-variation tapers normalized at zero. The linear residual's growth exponent is exactly Θ − 1/2, where Θ is the supremum of real parts of the nontrivial zeros. For a scale-dependent logarithmic taper with one explicit balancing coefficient, boundedness on the interior interval is itself equivalent to RH. The required bound remains open.
- **Adaptive coefficient cost:** any finite approximants with residual norm d tending to zero require harmonic coefficient energy at least (12/pi² − o(1)) log(1/d). The manuscript gives an exact finite inequality before the asymptotic.
- **Maximal absolute collar:** the proposed power-loss bound implies Dirichlet GRH. A Gram-rank argument gives a logarithmic obstruction for every sign sequence and shows that the normalized energy tends to infinity along all dyadic scales. Independent signs and random completely multiplicative signs fail the power-loss target. The every-epsilon version for Liouville remains unresolved.

## Selected sources

- Original paper: [Preprints.org v1](https://doi.org/10.20944/preprints202606.1350.v1).
- Nyman–Beurling companion: [Preprints.org v2](https://doi.org/10.20944/preprints202506.0772.v2). The ordinary fractional-part basis is treated separately in the appendix. The proof attempt uses the balanced reciprocal basis.
- Pólya–Vinogradov companion: [Hexagon v3](https://hexagonmath.org/2610.00256v3). Proposition 3.7 supplies the Riesz-kernel analogy. Appendix B reproduces the credited 11/12 argument. The 7/8 Lean result is discussed separately.
- [OpenAI's 7/8 manuscript](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf), Theorem 1.1 and §§2, 3, 12–20. The newest supplied PDF is this same 199-page manuscript.
- [OpenAI's formalization scope](https://github.com/openai/math/blob/main/lean/docs/003.md).
- [Anthropic's critical-line result](https://www.anthropic.com/research/riemann-zeta) and [Lamzouri's independent treatment](https://arxiv.org/abs/2609.02882v2).
- [Guth–Maynard zero density](https://arxiv.org/abs/2405.20552v2) and [Platt–Trudgian finite-height verification](https://doi.org/10.1112/blms.12460).
- [Li–Sun–Wang on Liouville exponential sums](https://arxiv.org/abs/2611.03589v1), 2 November 2026. The divisor-convolution weight is used to explain the Mellin cancellation pitfall.
- [Tao's logarithmic two-point theorem](https://doi.org/10.1017/fmp.2016.6).

## Author metadata

The byline follows the posted v1. The recent addresses, emails and ORCIDs are copied from the supplied Pólya–Vinogradov v3, title and final pages. The qualifiers on the affiliations agree with [the recent Zenodo record](https://zenodo.org/records/23524276).

| Author | Affiliations as printed | ORCID | Published emails |
| --- | --- | --- | --- |
| Deep Bhattacharjee, corresponding author | Formerly, Electro-Gravitational Space Propulsion Laboratory (EGSPL), Bhubaneswar, Odisha 751030, India. Formerly, University of Calcutta, Senate House, 87/1 College Street, Kolkata 700073, West Bengal, India. | [0000-0003-0466-750X](https://orcid.org/0000-0003-0466-750X) | d.bhattacharjee@erl-forschung.de, itsdeep@live.com, egspl@proton.me |
| Ushashi Bhattacharya | Formerly, National Taiwan University, Taipei 106319, Taiwan. | [0009-0002-2254-3914](https://orcid.org/0009-0002-2254-3914) | rai.bhattacharya.in@gmail.com |

AI-assisted tools were used for literature triage, independent mathematical audit, manuscript development and exact finite checks. No review or approval of this draft by either author is implied by its preparation. The source documents are cited. Their PDFs are not needed for rebuilding the draft.

## Review scope

Three parallel agents contributed proof checks and constructions during this research attempt. The broad bounded-variation obstruction was checked in separate rounds, and the last proof uses the finite variation measure to give a direct Fourier contradiction. A later requested follow-up audit could not run because that agent reached its usage limit. The primary agent completed the coefficient-cost derivation and the deliverable checks. The paper has no Lean formalization. Novelty and journal suitability require further assessment against the literature.
