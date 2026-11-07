from fractions import Fraction as F
from itertools import product

for n in range(1,11):
    for signs in product((-1,1),repeat=n):
        prefixes=[0]
        for sign in signs:
            prefixes.append(prefixes[-1]+sign)
        lhs=sum(sum(signs[j-1] for j in range(1,n+1) if t<j<=t+n)**2 for t in range(-n,n))
        rhs=sum(prefixes[j]**2+(prefixes[n]-prefixes[j])**2 for j in range(n))
        assert lhs==rhs
        assert 2*lhs>=n*prefixes[n]**2
print('PASS signed-window energy and prefix identity for all 2046 sign strings of lengths 1–10')
