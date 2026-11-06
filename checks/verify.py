"""Exact finite checks for the Liouville v2 research draft.

These checks exercise the finite formulas. They do not check zeta zeros
or establish any of the analytic asymptotic estimates.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, gcd


def correlations(sequence):
    return [
        sum(a * b for a, b in zip(sequence, sequence[lag:]))
        for lag in range(len(sequence))
    ]


def check_windows():
    cases = 0
    for n in range(1, 9):
        for a in product((-1, 1), repeat=n):
            c = correlations(a)
            prefix = [0]
            for sign in a:
                prefix.append(prefix[-1] + sign)
            assert prefix[-1] ** 2 == c[0] + 2 * sum(c[1:])
            for h in range(1, n + 3):
                windows = [
                    prefix[min(n, t + h)] - prefix[max(0, t)]
                    for t in range(1 - h, n)
                ]
                energy = sum(value * value for value in windows)
                from_shifts = h * c[0] + 2 * sum(
                    (h - j) * c[j] for j in range(1, min(h, n))
                )
                assert energy == from_shifts
                assert energy * (n + h - 1) >= h * h * prefix[-1] ** 2
                if h == n:
                    from_boundary = F(n + 1, 2) * prefix[-1] ** 2
                    from_boundary += 2 * sum(
                        (p - F(prefix[-1], 2)) ** 2 for p in prefix[1:-1]
                    )
                    assert energy == from_boundary
                cases += 1
    return cases


def check_rudin_shapiro():
    p = q = (1,)
    cases = 0
    for _ in range(11):
        h = len(p)
        assert [a + b for a, b in zip(correlations(p), correlations(q))] == (
            [2 * h] + [0] * (h - 1)
        )
        four_blocks = p + q + p + tuple(-value for value in q)
        assert sum(four_blocks[i] * four_blocks[2 * h + i] for i in range(h)) == h
        p, q = p + q, p + tuple(-value for value in q)
        cases += 1
    return cases


def check_random_sign_moments():
    cases = 0
    for h in range(1, 5):
        total = total_sq = 0
        for a in product((-1, 1), repeat=3 * h):
            value = sum(
                sum(a[i] * a[i + lag] for i in range(h)) ** 2
                for lag in range(h + 1, 2 * h + 1)
            )
            total += value
            total_sq += value * value
            cases += 1
        count = 2 ** (3 * h)
        assert F(total, count) == h * h
        assert F(total_sq, count) - h ** 4 == 4 * h * comb(h, 2)
    return cases


def prime_factors(n):
    factors = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        factors[n] = 1
    return factors


def check_finite_prime_model():
    prescribed = {2: -1, 3: -1, 5: -1}
    cutoff = 3
    period = (2 * 3 * 5) ** cutoff
    assert sum(F(1, p ** cutoff) for p in prescribed) <= F(1, 4)

    def sign(n):
        answer = 1
        for p, exponent in prime_factors(n).items():
            factor = prescribed.get(p, 1 if p % 3 == 1 else -1)
            answer *= factor ** exponent
        return answer

    for p, value in prescribed.items():
        assert sign(p) == value
    cases = 0
    for shift in (period, 2 * period, 3 * period):
        correlation = 0
        for n in range(1, 501):
            product_sign = sign(n) * sign(n + shift)
            if all(n % p ** cutoff for p in prescribed):
                assert product_sign == 1
            correlation += product_sign
            assert 2 * correlation >= n
            cases += 1
    return cases


def fractional_product_integral(j, k):
    integral = F(0)
    cuts = sorted({F(a, j) for a in range(j + 1)} | {F(a, k) for a in range(k + 1)})
    for a, b in zip(cuts, cuts[1:]):
        u, v = (j * a).__floor__(), (k * a).__floor__()
        integral += F(j * k, 3) * (b ** 3 - a ** 3)
        integral -= F(j * v + k * u, 2) * (b ** 2 - a ** 2)
        integral += u * v * (b - a)
    return integral


def check_sawtooth():
    cases = 0
    for j in range(1, 13):
        for k in range(1, 13):
            assert fractional_product_integral(j, k) == F(1, 4) + F(
                gcd(j, k) ** 2, 12 * j * k
            )
            cases += 1
    for m in (1, 2, 3, 5, 8, 16, 32, 64):
        phi = [0] + [sum(gcd(n, a) == 1 for a in range(1, n + 1)) for n in range(1, m + 1)]
        j2 = [0] + [sum(gcd(gcd(n, a), b) == 1 for a in range(n) for b in range(n))
                    for n in range(1, m + 1)]
        total = sum(F(phi[n] ** 2, j2[n]) for n in range(1, m + 1))
        t = 6 * total / (1 + 3 * total)
        u = [F(0)] + [t * F(phi[n], j2[n]) / total for n in range(1, m + 1)]
        c = [F(0)] * (m + 1)
        for n in range(m, 0, -1):
            c[n] = n * (u[n] - sum(c[a] / a for a in range(2 * n, m + 1, n)))
        assert sum(c) == t
        for j in range(1, m + 1):
            assert sum(c[k] * (F(1, 4) + F(gcd(j, k) ** 2, 12 * j * k))
                       for k in range(1, m + 1)) == F(1, 2)
        assert 1 - sum(c) / 2 == 1 / (1 + 3 * total)
        cases += 1
    return cases


def check_reciprocal_dilates():
    cases = 0
    for n in range(1, 17):
        for j in range(1, 31):
            x = F(j, 13)
            y = 1 / x
            z = y / n
            direct = z % 1 - (y % 1) / n
            assert direct == F(y.__floor__(), n) - z.__floor__()
            if x > 1:
                assert direct == 0
            cases += 1
    return cases


def check_riesz_rescaling():
    mobius = [0]
    coefficients = [0]
    for n in range(1, 32):
        factors = prime_factors(n)
        mobius.append(0 if any(e > 1 for e in factors.values()) else (-1) ** len(factors))
        value = 1
        for p in factors:
            value *= 1 - p
        coefficients.append(value)
    cases = 0
    for m in (5, 11, F(49, 3), 31):
        weights = [F(0)] + [
            mobius[n] * (1 - F(n) / m) for n in range(1, int(m) + 1)
        ]
        d_one = sum(weights[n] / n for n in range(1, len(weights)))
        for j in range(4, int(4 * m) + 1):
            y = F(j, 4)
            left = 1 + sum(
                weights[n] * (F(y.__floor__(), n) - (y / n).__floor__())
                for n in range(1, len(weights))
            )
            right = y.__floor__() * d_one + F(sum(coefficients[1:int(y) + 1])) / m
            assert left == right
            cases += 1
    return cases


def check_adaptive_inversion():
    cases = 0
    cutoff = 40
    mu = [0] + [
        0 if any(e > 1 for e in prime_factors(n).values())
        else (-1) ** len(prime_factors(n))
        for n in range(1, cutoff + 1)
    ]
    for size in range(2, 10):
        for denominator in (1, 3, 7):
            a = [F(0)] * (cutoff + 1)
            for n in range(2, size + 1):
                a[n] = F((-1) ** n * (n % 4 + 1), denominator)
            constant = sum(a[n] / n for n in range(2, size + 1))
            values = [F(0)] + [
                1 + k * constant - sum(a[n] * (k // n) for n in range(2, size + 1))
                for k in range(1, cutoff + 1)
            ]
            differences = [F(0)] + [
                values[k] - values[k - 1] for k in range(1, cutoff + 1)
            ]
            for n in range(2, cutoff + 1):
                reconstructed = -sum(
                    mu[n // r] * differences[r] for r in range(1, n + 1) if n % r == 0
                )
                assert reconstructed == a[n] - mu[n]
            for k in (2, 5, 13, 27, 40):
                partial_norm = sum(values[j] ** 2 / (j * (j + 1)) for j in range(1, k + 1))
                difference_energy = sum(differences[r] ** 2 / r for r in range(1, k + 1))
                assert difference_energy <= 4 * k * partial_norm
                coefficient_error = sum((a[n] - mu[n]) ** 2 / n for n in range(2, k + 1))
                harmonic = sum(F(1, n) for n in range(1, k + 1))
                assert coefficient_error <= 4 * k * harmonic ** 2 * partial_norm
                cases += 1
    return cases


def check_character_windows():
    cases = 0
    for n in range(1, 25):
        # chi(2)=i modulo 5, so chi(1,2,3,4)=(1,i,-i,-1).
        character = ((0, 0), (1, 0), (0, 1), (0, -1), (-1, 0))
        sequence = []
        for k in range(1, n + 1):
            sign = (-1) ** sum(prime_factors(k).values())
            real, imag = character[k % 5]
            sequence.append((sign * real, sign * imag))
        prefix = [(0, 0)]
        for real, imag in sequence:
            prefix.append((prefix[-1][0] + real, prefix[-1][1] + imag))
        energy = 0
        for t in range(1 - n, n):
            left, right = prefix[max(0, t)], prefix[min(n, t + n)]
            energy += (right[0] - left[0]) ** 2 + (right[1] - left[1]) ** 2
        endpoint = sum(x * x for x in prefix[-1])
        boundary = endpoint + sum(
            sum(x * x for x in value)
            + (prefix[-1][0] - value[0]) ** 2 + (prefix[-1][1] - value[1]) ** 2
            for value in prefix[1:-1]
        )
        assert boundary == energy
        assert 2 * energy >= n * endpoint
        cases += 1
    return cases


def check_gram_overlap():
    p = q = (1,)
    while len(p) < 1600:
        p, q = p + q, p + tuple(-value for value in q)
    cases = 0
    for h_small, h_large in ((8, 64), (16, 128), (64, 512)):
        total = 3 * h_large
        liouville = tuple(
            (-1) ** sum(prime_factors(n).values()) for n in range(1, total + 1)
        )
        for a in (tuple(1 for _ in range(total)), p[:total], liouville):
            width = 3
            starts_small = range(3 * h_small // 2 + 1, 7 * h_small // 4 + 1)
            starts_large = range(3 * h_large // 2 + 1, 7 * h_large // 4 + 1)
            cross_trace = sum(
                sum(a[n + r] * a[m + r] for r in range(width)) ** 2
                for n in starts_small for m in starts_large
            )
            cross_trace = F(cross_trace, len(starts_small) * len(starts_large))
            energy = 0
            for lag in range(h_large + 1, 2 * h_large + 1):
                value = maximum = 0
                for n in range(total - lag):
                    value += a[n] * a[n + lag]
                    maximum = max(maximum, abs(value))
                energy += maximum ** 2
            assert cross_trace <= F(16 * energy, h_large)
            cases += 1
    return cases


if __name__ == "__main__":
    checks = {
        "window identities and bounds": check_windows,
        "Rudin-Shapiro complementary blocks": check_rudin_shapiro,
        "independent-sign moments": check_random_sign_moments,
        "complete multiplicativity model": check_finite_prime_model,
        "ordinary-dilate Gram and minimizer": check_sawtooth,
        "balanced reciprocal-dilate identities": check_reciprocal_dilates,
        "linear Riesz rescaling": check_riesz_rescaling,
        "adaptive coefficient inversion and bounds": check_adaptive_inversion,
        "complex Dirichlet-character windows": check_character_windows,
        "separated Gram-window overlap": check_gram_overlap,
    }
    for name, check in checks.items():
        print(f"PASS {name}: {check()} cases")
