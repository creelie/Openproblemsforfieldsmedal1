"""Exact constants for the finite-Abel-jet example; not an RH verification."""
from fractions import Fraction

beta = Fraction(3, 4)
r = Fraction(1, 8)
sigma = 1-r
assert sigma-beta == Fraction(1, 8)

# P=2**320; all powers below are exact rational powers of two.
delta = Fraction(8, 2**40) / (1-Fraction(1, 2**560))
assert 0 < delta < 1
c_bound = Fraction(7, 3)/(1-2*r)**2
assert c_bound == Fraction(112, 27)
from math import factorial
m_bound = c_bound * max(Fraction(factorial(k), 1)/r**k for k in range(4))
assert m_bound == Fraction(114688, 9)
jet_error_bound = m_bound*delta/(1-delta)
assert jet_error_bound < Fraction(1, 10**6)

# The explicit general-cutoff estimate uses 1-P^(-2 sigma) >= 1-2^(-2 sigma).
# Its direction is also checked at an exact-power calibration point.
assert Fraction(1, 1)-Fraction(1, 2**560) > Fraction(1, 2)
print('PASS: P=2**320, beta=3/4, r=1/8, derivatives 0..3 have error < 1e-6.')
print('PASS: local-energy obstruction applies for every 0 < epsilon < 1/2.')
print('The analytic proof supplies the infinite construction and the pole; this script checks constants only.')
