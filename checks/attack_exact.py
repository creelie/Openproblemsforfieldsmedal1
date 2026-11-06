"""Exact checks for the 7 November 2026 attack, not a proof of RH."""
from fractions import Fraction as F
from math import comb, factorial, gcd


def add(a, b):
    c = [F(0)] * max(len(a), len(b))
    for i, v in enumerate(a):
        c[i] += v
    for i, v in enumerate(b):
        c[i] += v
    return c


def mul(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            c[i + j] += v * w
    return c


def integral_symmetric(a, radius):
    return sum(
        (2 * v * radius ** (i + 1) / (i + 1)
         for i, v in enumerate(a) if i % 2 == 0), F(0)
    )


def legendre_checks():
    polynomials = [[F(1)], [F(0), F(1)]]
    for n in range(1, 20):
        p = add(
            [F(0)] + [(2 * n + 1) * c for c in polynomials[n]],
            [-n * c for c in polynomials[n - 1]],
        )
        polynomials.append([c / (n + 1) for c in p])
    cases = 0
    for m in range(21):
        kernel = [F(0)]
        for j in range(m + 1):
            p = polynomials[j]
            kernel = add(kernel, [
                2 * (2 * j + 1) * p[0] * c * 4 ** i
                for i, c in enumerate(p)
            ])
        for k in range(m + 1):
            value = integral_symmetric([F(0)] * k + kernel, F(1, 4))
            assert value == int(k == 0)
            cases += 1
        assert integral_symmetric(mul(kernel, kernel), F(1, 4)) == kernel[0]
        assert kernel[0] <= 4 * (m + 2)
    for r in range(101):
        assert F(comb(2 * r, r), 4 ** r) ** 2 <= F(1, r + 1)
    return cases


def diagonal_checks():
    exp_minus_one = [F(0)] + [F(1, factorial(j)) for j in range(1, 41)]
    poly = mul([F(12), F(-6), F(1)], exp_minus_one)
    poly[1] -= 12
    assert poly[:5] == [0] * 5
    for j in range(5, 41):
        assert poly[j] == F((j - 3) * (j - 4), factorial(j)) > 0
    return 36


def factors(n):
    result = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        result[n] = 1
    return result


def liouville(n):
    return (-1) ** sum(factors(n).values())


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def prime_convolutions():
    cases = 0
    for y in (2, 5, 11):
        def model(n):
            return (-1) ** sum(k for p, k in factors(n).items() if p <= y)

        def small(n):
            fac = factors(n)
            return 2 ** len(fac) * liouville(n) if all(p <= y for p in fac) else 0

        def rough(n):
            fac = factors(n)
            return 2 ** len(fac) * liouville(n) if all(p > y for p in fac) else 0

        for n in range(1, 501):
            ds = divisors(n)
            assert model(n) == sum(small(d) for d in ds)
            assert liouville(n) == sum(model(n // d) * rough(d) for d in ds)
            cases += 2
    return cases


def coprime_pairs():
    count = 0
    c = {k: sum(liouville(a) * liouville(k - a)
                for a in range(1, k) if gcd(a, k) == 1)
         for k in range(2, 151)}
    for n in range(2, 151):
        direct = sum(liouville(a) * liouville(n - a) for a in range(1, n))
        regrouped = sum(c[k] for k in divisors(n) if k >= 2)
        assert direct == regrouped
        count += 1
    for p in (2, 3, 5, 7, 11):
        for q in (2, 3, 5, 7, 11):
            assert sum(liouville(p * n) * liouville(q * n)
                       for n in range(1, 101)) == 100
    return count


def sign_certificate():
    a, b = F(7165, 10000), F(7166, 10000)
    lower = sum(F(1, 3) ** j / factorial(j) for j in range(13))
    upper = lower + F(1, 3) ** 13 / factorial(13) / (1 - F(1, 42))
    assert 1 / b < lower < upper < 1 / a
    assert b < 1
    bound = sum(
        b ** n if liouville(n) > 0 else -a ** n
        for n in range(1, 17)
    ) + b ** 17 / (1 - b)
    assert bound < -F(1, 20)
    # e>2 makes q=e^-1<1/2, whence q-q²/(1-q)>0.
    assert sum(F(1, factorial(j)) for j in range(3)) > 2
    return 2


def moment_interpolation():
    """Check the rational part of the explicit finite moment construction."""
    cases = 0
    for k in range(1, 11):
        s = [F((-1) ** j, j + 2) for j in range(k)]
        c = []
        for m in range(k):
            lagrange = [F(1)]
            for n in range(k):
                if n != m:
                    lagrange = mul(lagrange, [F(-n, m - n), F(1, m - n)])
            for n in range(k):
                assert sum(v * F(n) ** j for j, v in enumerate(lagrange)) == int(n == m)
            c.append(sum(v * s[j] for j, v in enumerate(lagrange)))
        for j in range(k):
            assert sum(c[m] * F(m) ** j for m in range(k)) == s[j]
            cases += 1
    return cases


if __name__ == "__main__":
    for name, fn in [
        ("Legendre reproduction and evaluation cost", legendre_checks),
        ("positive diagonal-error coefficients", diagonal_checks),
        ("finite-prime convolution identities", prime_convolutions),
        ("coprime pairs and coherent prime Gram", coprime_pairs),
        ("rational smoothed-sign certificates", sign_certificate),
        ("explicit finite moment interpolation", moment_interpolation),
    ]:
        print(f"PASS: {name} ({fn()} checks)")
    print("Scope: finite identities only; RH and the signed upper estimate remain unproved.")
