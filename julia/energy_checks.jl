# Numerical checks for "Liouville Energy and the Rightmost Zeta Zero".
# Run: julia energy_checks.jl [Nmax]   (default 3_000_000)
# Every check prints PASS or FAIL and the measured value.

using Printf

const NMAX = length(ARGS) > 0 ? parse(Int, ARGS[1]) : 3_000_000

"Smallest-prime-factor sieve, then Liouville λ and Möbius μ up to n."
function liouville_mobius(n::Int)
    spf = zeros(Int32, n)
    for i in 2:n
        if spf[i] == 0
            for j in i:i:n
                spf[j] == 0 && (spf[j] = i)
            end
        end
    end
    λ = ones(Int8, n); μ = ones(Int8, n)
    for k in 2:n
        p = spf[k]; m = k ÷ p
        λ[k] = -λ[m]
        μ[k] = (m % p == 0) ? 0 : -μ[m]
    end
    return λ, μ
end

fails = 0
check(name, ok, val) = (global fails; ok || (fails += 1);
    @printf("%-58s %s  %s\n", name, ok ? "PASS" : "FAIL", val))

λ, μ = liouville_mobius(NMAX)

# Prefix sums L(j), V(N) = Σ_{j≤N} L(j)^2, S1(N) = Σ_{j≤N} L(j), and the energy
# Q(N) = (1/N)[L(N)^2 + Σ_{j<N} (L(j)^2 + (L(N)-L(j))^2)].
L = cumsum(Int64.(λ))
V = cumsum(Float64.(L) .^ 2)
S1 = cumsum(Float64.(L))
Q = zeros(Float64, NMAX)
for N in 1:NMAX
    LN = Float64(L[N])
    Vm = N > 1 ? V[N-1] : 0.0
    Sm = N > 1 ? S1[N-1] : 0.0
    Q[N] = (LN^2 + Vm + (N - 1) * LN^2 - 2LN * Sm + Vm) / N
end

# Lemma (core): V(N) ≤ (2N+1)Q(N) and Q(N) ≤ 11 V(N)^{2/3}.
r1 = maximum(V[N] / ((2N + 1) * Q[N]) for N in 1:NMAX)
r2 = maximum(Q[N] / (11 * V[N]^(2/3)) for N in 1:NMAX)
check("core lemma: max V/((2N+1)Q) ≤ 1", r1 <= 1, @sprintf("%.4f", r1))
check("core lemma: max Q/(11 V^(2/3)) ≤ 1", r2 <= 1, @sprintf("%.4f", r2))

# Completion bounds: L(N)^2/2 ≤ Q(N) ≤ 5 max_{j≤N} L(j)^2.
mx = 0.0; okc = true
for N in 1:NMAX
    global mx = max(mx, Float64(L[N])^2)
    (L[N]^2 / 2 <= Q[N] + 1e-9 && Q[N] <= 5mx + 1e-9) || (global okc = false)
end
check("completion: L^2/2 ≤ Q ≤ 5 max L^2 for all N", okc, "N ≤ $NMAX")

# Largest value of Q(N)/N in the range (reported, not a pass/fail check).
rq, iq = findmax(Q[N] / N for N in 1:NMAX)
@printf("%-58s %s  %s\n", "max Q(N)/N for N ≤ $NMAX", "INFO", @sprintf("%.4f at N = %d, L/√N = %.4f", rq, iq, L[iq] / sqrt(iq)))
# Logarithmic mean of Q(N)/N over [10^4, NMAX]: Σ (Q(N)/N)/N / Σ 1/N.
lm = sum(Q[N] / N^2 for N in 10^4:NMAX) / sum(1 / N for N in 10^4:NMAX)
@printf("%-58s %s  %s\n", "log mean of Q(N)/N on [10^4, $NMAX]", "INFO", @sprintf("%.4f", lm))
# Largest |L(x)|/√x.
rl, il = findmax(abs(L[x]) / sqrt(x) for x in 1:NMAX)
@printf("%-58s %s  %s\n", "max |L(x)|/√x for x ≤ $NMAX", "INFO", @sprintf("%.4f at x = %d", rl, il))

# Mertens function: |M(y)| ≤ √y for y ≤ NMAX, and |M(y)| ≤ y/4345 on [2160535, NMAX].
M = cumsum(Int64.(μ))
v1 = count(y -> abs(M[y]) > sqrt(y), 1:NMAX)
check("|M(y)| ≤ √y for 1 ≤ y ≤ $NMAX", v1 == 0, "violations = $v1")
if NMAX >= 2160535
    r3 = maximum(abs(M[y]) * 4345 / y for y in 2160535:NMAX)
    check("|M(y)| ≤ y/4345 on [2160535, $NMAX]", r3 <= 1, @sprintf("max ratio %.4f", r3))
end

# Explicit bound: |L(x)| ≤ x/2641 + 8.3 √x.
r4 = maximum(abs(L[x]) / (x / 2641 + 8.3sqrt(x)) for x in 1:NMAX)
check("|L(x)| ≤ x/2641 + 8.3√x for x ≤ $NMAX", r4 <= 1, @sprintf("max ratio %.4f", r4))

# Constants: ζ(2)/4345 < 1/2641 and 1 + log(2160535)/2 < 8.3.
check("ζ(2)/4345 < 1/2641", (pi^2 / 6) / 4345 < 1 / 2641, @sprintf("1/%.2f", 4345 / (pi^2 / 6)))
check("1 + log(2160535)/2 < 8.3", 1 + log(2160535) / 2 < 8.3, @sprintf("%.4f", 1 + log(2160535) / 2))

# Plancherel weight K(σ,τ) ≥ 1 - 2/(3+2√2) on σ ≥ 1/2 (grid check).
Kmin = minimum(1 + 2 / (1 + 2σ) - 2(1 + σ) / ((1 + σ)^2 + τ^2) for σ in 0.5:0.001:5, τ in 0:0.01:3)
check("min K on grid ≥ 1 - 2/(3+2√2) = 0.65685", Kmin >= 1 - 2 / (3 + 2sqrt(2)) - 1e-12, @sprintf("%.5f", Kmin))

# Smoothed sum B(X) = Σ λ(n) e^{-n/X}, truncated at n ≤ 45X (tail < e^{-45}).
println("\nB(X)/sqrt(X):")
for X in (10^3, 10^4, 3 * 10^4, 6 * 10^4)
    n1 = min(NMAX, 45X)
    s = sum(λ[n] * exp(-n / X) for n in 1:n1)
    @printf("  X = %-8d  %.4f\n", X, s / sqrt(X))
end

# Energy table: Q(N)/N and log Q / log N at powers of ten.
println("\nN, L(N), Q(N), Q(N)/N, log Q/log N:")
for k in 2:floor(Int, log10(NMAX))
    N = 10^k
    @printf("  10^%d  %8d  %14.2f  %8.4f  %.4f\n", k, L[N], Q[N], Q[N] / N, log(Q[N]) / log(N))
end

# Sensitivity theorem illustration: flip λ to +1 on ⌊2^{jβ}⌋ primes in (2^j, 2^{j+1}], β = 3/4.
function flipped(λ, β, n)
    isprime = falses(n); f = copy(λ)
    spf = zeros(Int32, n)
    for i in 2:n
        if spf[i] == 0
            isprime[i] = true
            for j in i:i:n
                spf[j] == 0 && (spf[j] = i)
            end
        end
    end
    fp = fill(Int8(-1), n)
    j = 4
    while 2^j < n
        ps = [p for p in 2^j+1:min(2^(j + 1), n) if isprime[p]]
        for p in ps[1:min(length(ps), floor(Int, 2.0^(j * β)))]
            fp[p] = 1
        end
        j += 1
    end
    f[1] = 1
    for k in 2:n
        p = spf[k]; f[k] = fp[p] * f[k ÷ p]
    end
    return f
end
f = flipped(λ, 0.75, NMAX)
Lf = cumsum(Int64.(f))
println("\nflip on x^(3/4) primes: x, L(x), L_f(x), log|L_f|/log x")
for k in 3:floor(Int, log10(NMAX))
    x = 10^k
    @printf("  10^%d  %8d  %10d  %.3f\n", k, L[x], Lf[x], log(abs(Lf[x]) + 1) / log(x))
end

println("\nfailures: $fails")
exit(fails == 0 ? 0 : 1)
