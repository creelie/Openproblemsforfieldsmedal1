# Computational verification files

Maximal Large Sieve and Coefficient Uniform Failure for Liouville Correlations  
Deep Bhattacharjee and Ushashi Bhattacharya, 2026

## What this contains

This is a theoretical mathematics paper. The comparison figure in the
manuscript (Figure 1, Section 5) is drawn natively in LaTeX/TikZ and
needs no external file to compile; the PDF and TEX deliverable is fully
self-contained.

The scripts here are independent, optional verification aids:

- `verify_exponents.py` symbolically checks the exact rational exponent
  arithmetic used in the proof of Theorem 5.2: the values 9/4 and 15/8,
  and the gap 3/8 between them. The theorem uses a dyadic H comparable
  to X^(1/4), and constants are irrelevant to the exponent calculation.
  No arithmetic function value is computed.
- `make_figure.py` independently reproduces a plot equivalent to Figure 1,
  by plotting the two explicit exponent functions 2+u and 2-u and marking
  u = 1/4. The annotation is placed away from the blue curve to avoid the
  overlap visible in narrow PDF viewers.

Neither script is required to compile the manuscript. Both are supplied
only so a reader can independently check the bookkeeping behind Theorem
5.2 and reproduce an equivalent picture of it.

## How to run

```bash
pip install sympy matplotlib numpy
python3 verify_exponents.py
python3 make_figure.py
```

`verify_exponents.py` prints the three checked exponent identities and exits
normally if and only if all assertions pass. `make_figure.py` writes a PDF
plot to the current directory; that generated PDF is not included in this
archive because the paper already contains the figure natively in LaTeX.
