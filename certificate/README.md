# Weak-independence certificate

Checks that 350 ordinates of zeros of ζ below the 8001st zero are 3160-independent in the sense of Anderson and Stark. This gives

- limsup Q(N)/N > 4.6242,
- liminf L(x)/√x < −2.5257,
- limsup L(x)/√x > 1.1562.

Requires Python 3 with `python-flint` 0.9 (FLINT and Arb).

| Step | Command | Time (one core) |
| :--- | :--- | :--- |
| residues A_γ at 192 bits | `python3 lz.py 1 8001` | minutes |
| zeros at 11264 bits | `python3 hz.py s 300` for s = 1, 301, …, 7801 | about 80 min |
| reduction (optional; `U_350_8000_10400.txt.gz` is included) | `python3 lll.py 350 8000 10400 500 100000` | about 100 min |
| exact check of the certificate | `python3 verify.py U_350_8000_10400.txt.gz 8000 10400` | about 4 min |
| constants in ball arithmetic | `python3 certify.py U_350_8000_10400.txt.gz 8000 3160` | seconds |

Data files go to `$CERT_DATA` (default `./data`). The reduction is not trusted: `verify.py` checks det U = ±1 exactly, computes the Gram–Schmidt norms exactly from a fraction-free LU decomposition, and runs an exhaustive Fincke–Pohst enumeration in ball arithmetic for each of the 7650 other ordinates.

Expected output of `verify.py`: `certified q-independent below gamma_8001 for q = 3160`.
