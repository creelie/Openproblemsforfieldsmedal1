"""Exact finite checks of two new identities; no asymptotic or RH verification."""
from math import gcd, isqrt

LIMIT=1024
lam=[0]+[1]*LIMIT
mu=[0]+[1]*LIMIT
for p in range(2,LIMIT+1):
    if all(p%d for d in range(2,isqrt(p)+1)):
        for n in range(p,LIMIT+1,p):
            mu[n]*=-1
        power=p
        while power<=LIMIT:
            for n in range(power,LIMIT+1,power):
                lam[n]*=-1
            power*=p
        for n in range(p*p,LIMIT+1,p*p):
            mu[n]=0

A=[0]*(LIMIT+1)
C=[0]*(LIMIT+1)
for k in range(2,LIMIT+1):
    for a in range(1,k):
        term=lam[a]*lam[k-a]
        A[k]+=term
        if gcd(a,k-a)==1:
            C[k]+=term

for k in range(1,LIMIT+1):
    divisors=[d for d in range(1,k+1) if k%d==0]
    assert A[k]==sum(C[k//d] for d in divisors), k
    assert C[k]==sum(mu[d]*A[k//d] for d in divisors), k

for p in (2,3,5,7,11,13,17):
    for n in range(1,LIMIT+1):
        lhs=lam[n] if n%p else 0
        rhs=lam[n]+(lam[n//p] if n%p==0 else 0)
        assert lhs==rhs, (p,n)

print('PASS: direct gcd sums and both divisor inversions for k=1..1024.')
print('PASS: principal-character lifting coefficients for seven primes and n=1..1024.')
print('Scope: finite identities only. No critical upper bound or RH proof is checked.')
