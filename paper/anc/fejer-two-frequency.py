"""Certify the two-frequency Fejer-energy lower bound 1811/2500.

Run with python-flint 0.9.0. All analytic values are Arb/Acb enclosures
at 128-bit precision. Frequency ordering uses a floating-point key only
to propose an order, then verifies strict separation using the balls.
"""

from itertools import product

from flint import __version__, acb, acb_series, arb, ctx, fmpq


def real_vector_pairing(z, w):
    return (
        1
        - (1 / (1 + z)).real
        - (1 / (1 + w)).real
        + (1 / (1 + z + w)).real
        + (1 / (1 + z + w.conjugate())).real
    )


def main():
    ctx.prec = 128
    ctx.cap = 2
    degree = 30
    half = arb(1) / 2
    zeros = acb.zeta_zeros(1, 2)
    if zeros[0].real != half or zeros[1].real != half:
        raise ArithmeticError("A zero enclosure is not on the critical line")
    if not arb(0) < zeros[0].imag < zeros[1].imag:
        raise ArithmeticError("The first two zero enclosures are not positive and disjoint")

    amplitudes = [-1 / half.zeta()]
    for zero in zeros:
        derivative = acb_series([zero, 1]).zeta()[1]
        if derivative.contains(0):
            raise ArithmeticError("A derivative enclosure contains zero")
        residue = (2 * zero).zeta() / (zero * derivative)
        amplitudes.append(2 * degree * abs(residue) / (degree + 1))

    frequencies = []
    for first, second in product(range(-degree, degree + 1), repeat=2):
        ordinate = first * zeros[0].imag + second * zeros[1].imag
        frequencies.append((float(ordinate.mid()), first, second, ordinate))
    frequencies.sort(key=lambda entry: entry[0])
    for previous, current in zip(frequencies, frequencies[1:]):
        if not previous[3] < current[3]:
            raise ArithmeticError("Two frequency enclosures are not strictly separated")

    poles = {(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)}
    regular_count = 0
    for _, first, second, ordinate in frequencies:
        if (first, second) in poles:
            continue
        if acb(half, ordinate).zeta().contains(0):
            raise ArithmeticError(f"Nonvanishing was not certified at {(first, second)}")
        regular_count += 1
    if len(frequencies) != 3721 or regular_count != 3716:
        raise ArithmeticError("The number of checked frequencies is incorrect")

    parameters = [acb(half), *zeros]
    bound = arb(0)
    for first, z in enumerate(parameters):
        for second, w in enumerate(parameters):
            bound += amplitudes[first] * amplitudes[second] * real_vector_pairing(z, w)
    threshold = arb(fmpq(1811, 2500))
    if not bound > threshold:
        raise ArithmeticError("The enclosure does not prove the rational threshold")

    print(f"python-flint {__version__}, precision {ctx.prec} bits")
    print(f"Fejer degree {degree} at each of two frequencies")
    print(f"Verified {len(frequencies)} strictly separated frequency enclosures")
    print(f"Verified nonvanishing on {regular_count} regular frequency enclosures")
    print(f"Squared vector norm: {bound}")
    print("Certified limsup Q_lambda(N)/N > 1811/2500")


if __name__ == "__main__":
    main()
