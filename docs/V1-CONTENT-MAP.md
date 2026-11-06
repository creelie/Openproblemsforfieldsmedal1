# V1 content retention in the expanded v2.2.0

## Final integration status

All mathematical items listed below have now been integrated in the 54-page v2.2.0 manuscript. The repaired terminal criterion is Proposition 2.2; the explicit original power gap is Corollary 2.5 and Figure 1; the square-divisor expansion is Lemma 2.6. Appendix F records the continuity and restored literature context. All 25 original references survive, six under existing keys and nineteen restored with updated metadata. Original source and supplement are preserved byte-for-byte. The audit below records the pre-integration findings for traceability, not outstanding omissions.

# Original-v1 content map before the v2.2.0 integration

This compares the original Sections 1--7 and back matter with the current paper/main.tex and companions **before** integration. The revision is stronger, but it does not yet retain every original item explicitly. No paper was edited during this audit.

Original manuscript archive: C:\Users\user\Downloads\preprints-218992-manuscript (1).zip.
SHA-256: B48C36CDB9D643F6FA46CD7671CEDA73527E64DFA095C18AE2302218ED5E6C64.

Original extracted TeX: tmp/v1-latest/Maximal_Large_Sieve_and_Coefficient_Uniform_Failure_for_Liouville_Correlations.tex.
SHA-256: 55729D158F484C139BCA9994B83D2FDF8C1A01848968F0008A370AA939F6AB07.

## Section map

| Original item | Current location/status | Required action |
| --- | --- | --- |
| Section 1: Liouville definition, Euler product and summatory criterion | The introduction and thm:equiv/sec:zero retain and strengthen them; the Perron appendix supplies the converse. | Identify the original criterion as the special case. The original promised its complex-analytic proof in Section 2, but did not actually supply it there. Keep the full revised proof. |
| Section 1: endpoint versus arithmetic distinction | Introduction, sec:collar and sec:sieve. | Retain the motivation, qualified by the common-support Bessel hypothesis. |
| Section 2: square identity and collar definition | Strengthened to additive twists in lem:square/eq:square. | Keep current integer/empty-range conventions. The dyadic blocks omit h=1, which needs its separate O(N) contribution. |
| Section 2: terminal-eta proposition prop:collarimp | Only a prose summary remains after lem:square. | Restore its two explicit hypotheses and proof, treating the crossing dyadic block. Draft supplied separately. |
| Section 3: endpoint duality | Strengthened to exact independently attained endpoints in lem:square. | Its mathematical content is retained. Do not restore the original erroneous maximizing phase. |
| Section 4: dyadic initial-segment lemma | Contained in the proof of thm:bessel. | May be separately identified for traceability; the revised proof retains both logarithmic factors. |
| Section 4: maximal spectral theorem and corollary | Correctly generalized by thm:bessel and the common-support example. | Do not restore arbitrary translated-interval input. Choose a dyadic support containing all of (N,2N]. |
| Section 5: coefficient-uniform construction | prop:uniform gives the exact maximum, hence is stronger. | Restore the original explicit eta in (0,3/4), epsilon=1/8 corollary: H comparable to N^(1/4), exponents 9/4 and 15/8, ratio at least N^(3/8)/32. Currently these numbers are omitted. |
| Section 5: exponent-gap figure fig:gap | **Omitted.** The new RS/window/model diagrams are different. | Restore curves 2+u versus 2-u and marked u=1/4. Explain that the blue line suppresses epsilon; the explicit theorem uses 2+1/8-u. Plot u<1, since H=N is empty. |
| Section 5: square-divisor lemma | Both identities appear near the vector transfer in dirichlet-smoothing.tex. | Restore its short prime-power proof and original correlation application. |
| Section 5: leading ordinary Möbius-correlation stratum | **Omitted as a correlation expansion.** | Add the finite r,s expansion, compatibility gcd(r,s)^2 dividing h, and leading r=s=1 stratum. Other strata involve affine forms with growing parameters. |
| Section 6: collar open problem and RH implication | thm:grh strengthens it to additive twists and Dirichlet GRH. | Explicitly retain RH as a special case. Distinguish the disproved zero-loss endpoint from the still-open every-epsilon hypothesis. |
| Section 6: extended background literature | Much omitted; selected MR/MRT/Tao results survive elsewhere. | Restore a short accurately scoped background paragraph and the missing references. |
| Section 6: finite-height RH and Mertens comparison | Platt--Trudgian retained; Odlyzko--te Riele omitted. | Restore the Mertens context without claiming they displayed an explicit integer counterexample. |
| Section 7: conclusions | The logical distinction survives in the introduction/open-estimate discussions. | A compact explicit recap would retain section-level coverage. Qualify “endpoint never the bottleneck” by the required genuine spectral/Bessel input. |

## Original errors not to restore

1. **Duality phase:** for \(v_h=\omega_hC_h(Y_h)=|C_h(Y_h)|\), use \(\beta_h=v_h/\|v\|_2\). The original extra factor \(\overline{\omega_h}\) can make opposite terms cancel. Without the phases, use \(\beta_h=\overline{C_h(Y_h)}/\|C\|_2\). The current lemma is correct.
2. **Support:** \(N<2^K\le4N\) does not guarantee coverage of (N,2N]. Choose \(K=\lceil\log_2(2N)\rceil\), so \(2N\le2^K<4N\).
3. **Spectral cutoff:** a support-tied spectral large sieve is not automatically uniform for arbitrary short intervals translated far out. The revised common-support theorem repairs this.
4. **Floors:** the original equalities \(\sum_{n\le Y}1=Y\) and \(C_h^*(X)=X-h\) require integral endpoints. Keep the revised integer convention.
5. **Worst case:** the exponent 2+u is a maximum attained by the constant sequence, not the size of every bounded sequence.
6. **Conditional scope:** the original data statement saying that all results are unconditional theorems must not be read as proving its open collar hypothesis. State that the implications, identities and counterexamples are proved while the arithmetic estimate remains open.
7. **Endpoint illustration:** the “different wall for each h” prose illustrates abstract endpoint arrays; it does not itself construct a single arithmetic sequence realizing arbitrary prescribed arrays.

## Supplements and declarations

The available matching-ID supplement is C:\Users\user\Downloads\preprints-218992-supplementary.zip.
SHA-256: 5D29E6FA93BEEC9B37CB540F19D72C0D25B2D8271785311067A72EC0BE10EA4B.
It contains verify_exponents.py, make_figure.py, README.md and manifest.json.
The older preprints-229857-supplementary.zip has a different archive hash.

The first script verifies 9/4, 15/8 and 3/8 with SymPy; the second reproduces the omitted exponent figure. Neither was present in the inspected current checks directory. Preserve the original inputs and include current equivalents or compatibility scripts, updating stale theorem-number annotations.

Original separate funding, data availability, supplementary materials, computational/AI tools, ethics and COI declarations are absent as separate headings in the current short reproduction section. Restore them with accurate descriptions of the new checks and formalization scope. Do not newly certify author review of all added material solely because that sentence appeared in v1. The two-author byline is retained. Updated current affiliations can appropriately replace obsolete v1 designations.

## Bibliography coverage and metadata checks

The original has 25 entries. Six survive under current keys:
titchmarsh; deshouillers-iwaniec → di; matomaki-radziwill → mr-short;
matomaki-radziwill-tao → mrt; tao-logchowla → tao; platt-trudgian → pt.

The 19 omitted keys, supplied in the accompanying draft snippets, are:
apostol, iwaniec-kowalski, iwaniec-spectral, friedlander-iwaniec,
bombieri, montgomery, selberg, odlyzko-teriele, sarnak-letter,
bourgain-sarnak-ziegler, matomaki-radziwill-tao-signs, tao-teravainen,
klurman, teravainen-binary, teravainen-walker, chavez,
krishnamoorthy-chowla, pascadi, granville-soundararajan.

Specific primary-source checks:

- **Krishnamoorthy:** [arXiv:2501.10962v2](https://arxiv.org/abs/2501.10962v2) confirms Krishnarjun Krishnamoorthy, the title, 10 March 2025 revision, and related published DOI [10.1090/proc/17544](https://doi.org/10.1090/proc/17544). The publisher page was inaccessible; the snippet therefore does not invent a verified volume/page range.
- **Chavez:** [arXiv:2409.02106v10](https://arxiv.org/abs/2409.02106v10) confirms the preprint title and 14 May 2026 revision. The [publisher record](https://doi.org/10.1142/S1793042126500934) gives the journal title **Correlations of the Möbius and Liouville functions with their partial sums**, International Journal of Number Theory, published 13 May 2026. The reciprocal-derivative statements assume RH and simplicity and include numerical evidence; this reference is not an unconditional RH input.
- **Pascadi:** [Cambridge's published article](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/large-sieve-inequalities-for-exceptional-maass-forms-and-the-greatest-prime-factor-of-n21/DC9B30CB4824955671C7B018C473863A) confirms Forum of Mathematics Pi **14** (2026), e8, 1--54, DOI **10.1017/fmp.2026.10025**.
- **Teräväinen--Walker:** [Springer](https://link.springer.com/article/10.1007/s00209-025-03770-2) supplies the complete metadata: Mathematische Zeitschrift **310** (2025), article 75, DOI **10.1007/s00209-025-03770-2**.

This is a content-retention audit, not a fresh theorem-by-theorem verification of all 25 cited works. Restoring a reference must not enlarge the scope of what it is cited to prove.
