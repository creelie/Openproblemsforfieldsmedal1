"""Create the reviewed publication assets from the repository sources."""
from argparse import ArgumentParser
from hashlib import sha256
import json
from pathlib import Path
import shutil
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATHS = [
    ".gitignore", ".zenodo.json", "CITATION.cff", "LICENSE", "README.md",
    "RELEASE-NOTES.md", "release.json", ".github/workflows/release.yml",
    "paper/main.tex", "paper/routes.tex", "paper/ordinary-dilates.tex",
    "paper/dirichlet-smoothing.tex",
    "paper/LICENSE", "checks/verify.py", "checks/verification-results.txt",
    "docs/RESEARCH.md", "docs/INPUTS.sha256", "docs/DIRICHLET-SMOOTHING-ATTEMPT.md",
    "scripts/make_release.py",
    "lean/GramCore.lean", "lean/lean-toolchain", "lean/lakefile.toml",
    "lean/README.md", "lean/logs/GramCore.build.log",
]


def make_zip(destination, entries):
    with ZipFile(destination, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(entries.items()):
            info = ZipInfo(name, (2026, 11, 6, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    with ZipFile(destination) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("Archive failed its CRC check")


def main():
    parser = ArgumentParser()
    parser.add_argument("--pdf", type=Path, default=ROOT / "paper" / "main.pdf")
    args = parser.parse_args()
    pdf = args.pdf.read_bytes()
    if not pdf.startswith(b"%PDF-"):
        raise ValueError("Expected a compiled PDF")
    missing = [name for name in SOURCE_PATHS if not (ROOT / name).is_file()]
    if missing:
        raise FileNotFoundError(", ".join(missing))
    results = (ROOT / "checks" / "verification-results.txt").read_text(encoding="utf-8")
    if len(results.splitlines()) != 10 or any(not line.startswith("PASS ") for line in results.splitlines()):
        raise ValueError("Expected all ten finite-check groups to pass")
    release = json.loads((ROOT / "release.json").read_text(encoding="utf-8"))
    destination = ROOT / "dist"
    destination.mkdir(exist_ok=True)
    output = ROOT / "output"
    (output / "pdf").mkdir(parents=True, exist_ok=True)
    stable_pdf = output / "pdf" / "signed-liouville-energies-v2.pdf"
    stable_pdf.write_bytes(pdf)
    pdf_asset = destination / stable_pdf.name
    shutil.copyfile(stable_pdf, pdf_asset)
    tex_entries = {
        path.name: path.read_bytes() for path in (ROOT / "paper").glob("*.tex")
    }
    tex_entries["LICENSE"] = (ROOT / "paper" / "LICENSE").read_bytes()
    tex_entries["COMPILE.txt"] = (
        "The main file is main.tex. All figures use TikZ.\n"
        "Run latexmk -pdf main.tex, or pdflatex main.tex three times.\n"
    ).encode()
    source_asset = output / "signed-liouville-energiestex.zip"
    make_zip(source_asset, tex_entries)
    shutil.copyfile(source_asset, destination / source_asset.name)
    entries = {name: (ROOT / name).read_bytes() for name in SOURCE_PATHS}
    entries["output/pdf/" + stable_pdf.name] = pdf
    entries["output/" + source_asset.name] = source_asset.read_bytes()
    manifest = {
        "version": release["version"], "repository": release["repository"],
        "RH_proved": False, "Dirichlet_GRH_proved": False,
        "files": {name: sha256(data).hexdigest() for name, data in sorted(entries.items())},
    }
    entries["MANIFEST.json"] = json.dumps(manifest, indent=2).encode() + b"\n"
    package = destination / ("RiemannHypothesis-" + release["tag"] + ".zip")
    make_zip(package, entries)
    assets = (pdf_asset, destination / source_asset.name, package)
    hashes = "".join(sha256(path.read_bytes()).hexdigest() + "  " + path.name + "\n" for path in assets)
    (destination / "SHA256SUMS.txt").write_text(hashes, encoding="utf-8")
    print(json.dumps({"assets": [path.name for path in assets], "checks": "PASS"}, indent=2))


if __name__ == "__main__":
    main()
