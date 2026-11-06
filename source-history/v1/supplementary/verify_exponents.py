"""
Symbolic check of the exact rational exponent arithmetic used in the proof
of Theorem 5.2 (Coefficient-uniform failure) in:

  Maximal Large Sieve and Coefficient Uniform Failure for Liouville Correlations

The theorem chooses a dyadic H with X^(1/4)/2 < H <= X^(1/4). Constants do
not affect the X-exponents, so the exponent bookkeeping is the same as for
H = X^(1/4). This script does not compute any arithmetic function value
(no lambda, mu, or divisor sum is evaluated). It only checks, with exact
rational arithmetic via SymPy, the exponent identities used in the proof,
at eps = 1/8 and u = 1/4.
"""
from sympy import Rational, simplify

eps = Rational(1, 8)
u = Rational(1, 4)   # H is dyadic and comparable to X^u

# Energy produced by the constant sequence c_n = 1 on H < h <= 2H: ~ H * X^2,
# i.e. exponent 2 + u after absorbing H ~ X^u into the X-power.
energy_exponent = u + 2
assert energy_exponent == Rational(9, 4), energy_exponent

# Scale the coefficient-uniform collar property would allow:
#   C_eps * X^(2+eps) * H^{-1}, i.e. exponent 2 + eps - u.
allowed_exponent = 2 + eps - u
assert allowed_exponent == Rational(15, 8), allowed_exponent

# The gap between what is produced and what is allowed:
gap = simplify(energy_exponent - allowed_exponent)
assert gap == Rational(3, 8), gap
assert gap > 0

print("energy exponent       9/4 : checked, equals", energy_exponent)
print("allowed exponent     15/8 : checked, equals", allowed_exponent)
print("gap                   3/8 : checked, equals", gap)
print("All exponent identities used in Theorem 5.2 verified symbolically.")
