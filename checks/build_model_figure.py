"""Render a PGFPlots model figure to PNG; no Liouville data are plotted."""
from pathlib import Path
import subprocess
import shutil

root = Path(__file__).resolve().parents[1]
out = root / "paper" / "figures"
tmp = root / "tmp" / "model-figure"
out.mkdir(exist_ok=True)
tmp.mkdir(parents=True, exist_ok=True)
source = r"""
\documentclass[tikz,border=5pt]{standalone}
\usepackage[T1]{fontenc}
\usepackage{lmodern,pgfplots}
\pgfplotsset{compat=1.18}
\begin{document}
\begin{tikzpicture}
\begin{axis}[
 width=13cm,height=6.1cm,
 xmin=0,xmax=18,ymin=-100,ymax=100,
 axis lines=left,grid=major,grid style={gray!18},
 xlabel={$t=\log X$},ylabel={Normalized leading term},
 title={Constructed comparison model; not Liouville data},
 title style={font=\small},
 tick label style={font=\small},
 label style={font=\small},
 legend style={at={(.02,.02)},anchor=south west,draw=none,
               fill=white,font=\small},
 samples=401,domain=0:18,
]
\addplot[blue!65!black,thick] {exp(x/4)*cos(deg(x))};
\addlegendentry{$e^{t/4}\cos t$}
\addplot[orange!65!black,dashed] {exp(x/4)};
\addlegendentry{envelopes $\pm e^{t/4}$}
\addplot[orange!65!black,dashed,forget plot] {-exp(x/4)};
\end{axis}
\end{tikzpicture}
\end{document}
"""
tex = tmp / "model.tex"
tex.write_text(source, encoding="utf-8")
latex = shutil.which("pdflatex") or r"C:\texlive\2023\bin\windows\pdflatex.exe"
p = subprocess.run([latex, "-interaction=nonstopmode", "-halt-on-error",
                    tex.name], cwd=tmp, capture_output=True, text=True)
if p.returncode:
    raise RuntimeError(p.stdout[-2200:])
p = subprocess.run(["pdftoppm", "-png", "-singlefile", "-r", "300",
                    str(tmp / "model.pdf"), str(out / "model-abel-gap")],
                   capture_output=True, text=True)
if p.returncode:
    raise RuntimeError(p.stderr)
(out / "model-abel-gap-source.tex").write_text(source, encoding="utf-8")
print("Saved TikZ/PGFPlots source and 300-dpi PNG: analytic model only.")
