"""Certify two numerical consequences of the Liouville energy pole bounds.

Requires python-flint 0.9.0. The FLINT zeta zero routines isolate the zeros
rigorously. All arithmetic after isolation uses outward-rounded Arb balls.
See https://flintlib.org/doc/acb_dirichlet/index.html#zeros-of-the-riemann-zeta-function.
"""

from flint import __version__, acb, acb_series, arb, ctx, fmpq


def residue_at_zero(zero):
    derivative = acb_series([zero, 1]).zeta()[1]
    if derivative.contains(0):
        raise ArithmeticError("The derivative enclosure contains zero")
    return (2 * zero).zeta() / (zero * derivative)


def main():
    ctx.prec = 128
    ctx.cap = 2
    half = arb(1) / 2
    zero_count = 1000
    zeros = acb.zeta_zeros(1, zero_count)
    if len(zeros) != zero_count:
        raise ArithmeticError("The number of isolated zeros is incorrect")

    last_ordinate = arb(0)
    positive_bias = -1 / half.zeta()
    multipole_bound = 2 * positive_bias**2 / 3
    for zero in zeros:
        if zero.real != half or not last_ordinate < zero.imag:
            raise ArithmeticError("The positive critical zero boxes are not ordered and disjoint")
        last_ordinate = zero.imag
        residue = residue_at_zero(zero)
        norm_squared = 2 - 2 * (1 / (1 + zero)).real
        # Both conjugate zeros contribute equally. Positive ordinates are
        # disjoint and nonzero, so the negative ordinates are distinct too.
        multipole_bound += 2 * norm_squared * abs(residue) ** 2

    first = zeros[0]
    degree = 100
    last_harmonic = first.imag
    for frequency in range(2, degree + 1):
        harmonic = frequency * first.imag
        if not last_harmonic < harmonic:
            raise ArithmeticError("The positive harmonic boxes are not disjoint")
        last_harmonic = harmonic
        if acb(half, harmonic).zeta().contains(0):
            raise ArithmeticError(f"Harmonic {frequency} was not excluded")

    amplitude = 2 * arb(degree) * abs(residue_at_zero(first)) / (degree + 1)
    oscillatory_norm = 1 + 1 / (1 + 2 * half)
    oscillatory_norm += (1 / (1 + 2 * first)).real - 2 * (1 / (1 + first)).real
    cross = 1 - 1 / (1 + half) - (1 / (1 + first)).real
    cross += 2 * (1 / (1 + half + first)).real
    positive_weight_bound = 2 * positive_bias**2 / 3
    positive_weight_bound += 2 * positive_bias * amplitude * cross
    positive_weight_bound += amplitude**2 * oscillatory_norm

    if not multipole_bound > arb(fmpq(45769, 100000)):
        raise ArithmeticError("The multiple-pole bound missed 45769/100000")
    if not positive_weight_bound > arb(fmpq(3257, 5000)):
        raise ArithmeticError("The positive-weight bound missed 3257/5000")

    print(f"python-flint {__version__}, precision {ctx.prec} bits")
    print(f"Verified {zero_count} disjoint positive simple critical zero boxes")
    print(f"Multiple-pole lower bound: {multipole_bound}")
    print(f"Verified the {degree - 1} higher harmonic boxes are disjoint and zero-free at the tested points")
    print(f"Positive-weight lower bound: {positive_weight_bound}")


if __name__ == "__main__":
    main()
