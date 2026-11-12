# Exact finite identities used in the paper (integer and rational arithmetic only).
# Run: julia finite_identities.jl

fails = 0
report(name, ok) = (global fails; ok || (fails += 1); println(rpad(name, 70), ok ? "PASS" : "FAIL"))

# 1. Window energy and prefix identity, all sign strings of length 1..12:
#    Σ_t S(t)^2 = Σ_{j<n} (L_j^2 + (L_n - L_j)^2), and 2·Σ_t S(t)^2 ≥ n L_n^2.
ok = true; count = 0
for n in 1:12, bits in 0:(2^n - 1)
    s = [((bits >> (i - 1)) & 1) == 1 ? 1 : -1 for i in 1:n]
    P = [0; cumsum(s)]
    lhs = sum(sum(s[j] for j in 1:n if t < j <= t + n; init = 0)^2 for t in -n:n-1)
    rhs = sum(P[j+1]^2 + (P[n+1] - P[j+1])^2 for j in 0:n-1)
    global ok &= (lhs == rhs) && (2lhs >= n * P[n+1]^2)
    global count += 1
end
report("window energy = prefix form, $(count) sign strings, lengths 1..12", ok)

# 2. Completion identity in exact rationals for random integer prefixes.
ok = true
for trial in 1:2000
    n = rand(1:40); Lp = rand(-50:50, n)
    E = (Lp[n]^2 + sum((Lp[j]^2 + (Lp[n] - Lp[j])^2 for j in 1:n-1); init = 0)) // n
    C = (n + 1) // (2n) * Lp[n]^2 + 2 // n * sum(((Lp[j] - Lp[n] // 2)^2 for j in 1:n-1); init = 0 // 1)
    global ok &= (E == C)
end
report("completion identity, 2000 random prefix vectors", ok)

# 3. Liouville and Möbius tables up to LIMIT.
const LIMIT = 1024
lam = ones(Int, LIMIT); mu = ones(Int, LIMIT)
for p in 2:LIMIT
    all(p % d != 0 for d in 2:isqrt(p)) || continue
    for n in p:p:LIMIT; mu[n] *= -1; end
    pw = p
    while pw <= LIMIT
        for n in pw:pw:LIMIT; lam[n] *= -1; end
        pw *= p
    end
    for n in p^2:p^2:LIMIT; mu[n] = 0; end
end

# 4. Primitive correlation inversion: A(k) = Σ_{d|k} C(k/d), C(k) = Σ_{d|k} μ(d) A(k/d).
A = zeros(Int, LIMIT); C = zeros(Int, LIMIT)
for k in 2:LIMIT, a in 1:k-1
    t = lam[a] * lam[k-a]; A[k] += t
    gcd(a, k - a) == 1 && (C[k] += t)
end
ok = all(A[k] == sum(C[k÷d] for d in 1:k if k % d == 0) &&
         C[k] == sum(mu[d] * A[k÷d] for d in 1:k if k % d == 0) for k in 1:LIMIT)
report("primitive correlation divisor inversions, k = 1..$LIMIT", ok)

# 5. Principal-character lifting: λ(n)1_{p∤n} = λ(n) + λ(n/p)1_{p|n}.
ok = all((n % p != 0 ? lam[n] : 0) == lam[n] + (n % p == 0 ? lam[n÷p] : 0)
         for p in (2, 3, 5, 7, 11, 13, 17), n in 1:LIMIT)
report("principal-character lifting, seven primes, n = 1..$LIMIT", ok)

# 6. λ = μ * 1_squares, hence L(x) = Σ_{d ≤ √x} M(x/d^2).
Mf = cumsum(mu); Lf = cumsum(lam)
ok = all(Lf[x] == sum(Mf[x÷(d^2)] for d in 1:isqrt(x)) for x in 1:LIMIT)
report("L(x) = Σ_{d≤√x} M(x/d^2), x = 1..$LIMIT", ok)

# 7. Exact constants of the finite-Abel-jet example.
beta = 3 // 4; r = 1 // 8; sigma = 1 - r
delta = (8 // big(2)^40) / (1 - 1 // big(2)^560)
cbound = (7 // 3) / (1 - 2r)^2
mbound = cbound * maximum(factorial(k) // r^k for k in 0:3)
ok = sigma - beta == 1 // 8 && 0 < delta < 1 && cbound == 112 // 27 &&
     mbound == 114688 // 9 && mbound * delta / (1 - delta) < 1 // 10^6
report("Abel-jet constants: c = 112/27, m = 114688/9, jet error < 1e-6", ok)

# 8. Rudin-Shapiro: complementary identity |P_m|^2 + |Q_m|^2 = 2^{m+1} as an
#    identity of autocorrelations, and the block pattern P,Q,P,-Q.
function rs(m)
    P = [1]; Q = [1]
    for _ in 1:m
        P, Q = [P; Q], [P; -Q]
    end
    P, Q
end
acorr(v, h) = sum(v[i] * v[i+h] for i in 1:length(v)-h; init = 0)
ok = true
for m in 1:10
    P, Q = rs(m)
    global ok &= all(acorr(P, h) + acorr(Q, h) == (h == 0 ? 2^(m + 1) : 0) for h in 0:2^m-1)
end
P2, _ = rs(6); Pm, Qm = rs(4); B = 2^4
ok &= P2[1:B] == Pm && P2[B+1:2B] == Qm && P2[2B+1:3B] == Pm && P2[3B+1:4B] == -Qm
report("Rudin-Shapiro complementary identity (m ≤ 10) and block pattern", ok)

println("failures: $fails")
exit(fails == 0 ? 0 : 1)
