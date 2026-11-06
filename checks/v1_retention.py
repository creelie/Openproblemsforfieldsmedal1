"""Exact finite checks for the v1 material carried into v2.2.

These identities do not establish asymptotic Liouville cancellation or RH.
"""
from fractions import Fraction as F
from math import gcd, isqrt

def mobius(n):
    sign = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    return -sign if n > 1 else sign

def liouville(n):
    sign = 1
    p = 2
    while p * p <= n:
        while n % p == 0:
            n //= p
            sign = -sign
        p += 1
    return -sign if n > 1 else sign

assert F(2) + F(1, 4) == F(9, 4)
assert F(2) + F(1, 8) - F(1, 4) == F(15, 8)
assert F(9, 4) - F(15, 8) == F(3, 8)
for n in range(1, 1001):
    assert liouville(n) == sum(mobius(n // (r*r))
        for r in range(1, isqrt(n)+1) if n % (r*r) == 0)
count = 0
for y in range(1, 25):
    for h in range(1, 25):
        direct = sum(liouville(n) * liouville(n+h) for n in range(1, y+1))
        expanded = 0
        for r in range(1, isqrt(y)+1):
            for s in range(1, isqrt(y+h)+1):
                inner = sum(mobius(n//(r*r))*mobius((n+h)//(s*s))
                    for n in range(1, y+1)
                    if n%(r*r)==0 and (n+h)%(s*s)==0)
                if h % (gcd(r,s)**2):
                    assert inner == 0
                expanded += inner
        assert direct == expanded
        count += 1
print('Exact rational exponent gap: 3 identities passed.')
print('Square-divisor identity: 1000 integers passed.')
print(f'Expanded correlation and gcd obstruction: {count} pairs passed.')
