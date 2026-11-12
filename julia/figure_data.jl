# Data files for the figures (written to the directory given as the first argument).
using Arblib, Printf
out = ARGS[1]
setprecision(Arb, 64)
zb(s) = (r = Acb(prec = 64); Arblib.zeta!(r, s); r)
open(joinpath(out, "surf.dat"), "w") do io
    for σ in range(0.3, 1.3; length = 41)
        for t in range(2, 36; length = 103)
            s = Acb(σ, t)
            v = abs(zb(2s) / zb(s))
            y = min(log10(Float64(midpoint(v))), 1.6)
            @printf(io, "%.4f %.4f %.4f\n", σ, t, y)
        end
        println(io)
    end
end
include_dir = @__DIR__
N = 3_000_000
spf = zeros(Int32, N)
for i in 2:N
    if spf[i] == 0
        for j in i:i:N; spf[j] == 0 && (spf[j] = i); end
    end
end
λ = ones(Int8, N)
for k in 2:N; λ[k] = -λ[k ÷ spf[k]]; end
L = cumsum(Int64.(λ)); V = cumsum(Float64.(L) .^ 2); S1 = cumsum(Float64.(L))
Q(n) = (L[n]^2 + 2(n > 1 ? V[n-1] : 0.0) + (n - 1) * L[n]^2 - 2L[n] * (n > 1 ? S1[n-1] : 0.0)) / n
open(joinpath(out, "energy.dat"), "w") do io
    for e in range(2, log10(N); length = 300)
        n = round(Int, 10^e)
        @printf(io, "%.5f %.6f\n", log10(n), Q(n) / n)
    end
end
# flip on x^(3/4) primes
isp = [spf[i] == i for i in 1:N]
fp = fill(Int8(-1), N); j = 4
while 2^j < N
    ps = [p for p in 2^j+1:min(2^(j + 1), N) if isp[p]]
    for p in ps[1:min(length(ps), floor(Int, 2.0^(0.75j)))]; fp[p] = 1; end
    global j += 1
end
f = ones(Int8, N)
for k in 2:N; f[k] = fp[spf[k]] * f[k ÷ spf[k]]; end
Lf = cumsum(Int64.(f))
open(joinpath(out, "flip.dat"), "w") do io
    for e in range(2, log10(N); length = 300)
        x = round(Int, 10^e)
        @printf(io, "%.5f %.6f %.6f\n", log10(x), log(abs(Lf[x]) + 1) / log(x), log(abs(L[x]) + 1) / log(x))
    end
end
open(joinpath(out, "bsmooth.dat"), "w") do io
    for e in range(1, log10(6e4); length = 60)
        X = 10^e; n1 = min(N, round(Int, 45X))
        s = sum(λ[n] * exp(-n / X) for n in 1:n1)
        @printf(io, "%.5f %.6f\n", e, s / sqrt(X))
    end
end
println("done")
