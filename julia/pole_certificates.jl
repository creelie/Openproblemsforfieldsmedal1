# Ball-arithmetic certificates for the pole-energy lower bounds.
# Requires Arblib.jl (FLINT/Arb). All values are rigorous enclosures; a bound is
# certified only when the enclosure lies strictly above the rational threshold.
# Run: julia pole_certificates.jl

using Arblib

const PREC = 128
setprecision(Arb, PREC)

"The first n zeros of zeta in the upper half-plane, as rigorous Acb enclosures."
function zeta_zeros(n)
    v = AcbVector(n; prec = PREC)
    ccall((:acb_dirichlet_zeta_zeros, Arblib.libflint), Cvoid,
          (Ptr{Arblib.acb_struct}, Ref{Int}, Int, Int), v, Ref(1), n, PREC)
    return [Acb(v[i]) for i in 1:n]
end

zeta_ball(s::Acb) = (r = Acb(prec = PREC); Arblib.zeta!(r, s); r)

"ζ'(s) as a ball, via the jet (ζ(s), ζ'(s))."
function zeta_derivative(s::Acb)
    v = AcbVector(2; prec = PREC)
    ccall((:acb_dirichlet_zeta_jet, Arblib.libflint), Cvoid,
          (Ptr{Arblib.acb_struct}, Ref{Arblib.acb_struct}, Cint, Int, Int), v, s, 0, 2, PREC)
    return Acb(v[2])
end

residue(z) = zeta_ball(2z) / (z * zeta_derivative(z))
contains_zero(x::Acb) = Arblib.contains_zero(x)
re(x::Acb) = real(x)

function main()
    fails = 0
    half = Arb(1) / 2
    zs = zeta_zeros(1000)

    # Zero boxes: real part exactly 1/2, ordinates strictly increasing.
    ordered = all(Arblib.isexact(real(z)) && Arblib.isequal(real(z), half) for z in zs) &&
              all(imag(zs[k]) < imag(zs[k+1]) for k in 1:length(zs)-1)
    println("1000 zero boxes on Re s = 1/2, disjoint and ordered: ", ordered ? "PASS" : "FAIL")
    ordered || (fails += 1)
    all(!contains_zero(zeta_derivative(z)) for z in zs) || (fails += 1)

    # Multiple-pole lower bound: 2 b^2/3 + Σ 2 K(ρ) |res_ρ|^2, b = -1/ζ(1/2).
    b = -1 / real(zeta_ball(Acb(half)))
    bound = 2 * b^2 / 3
    for z in zs
        K = 2 - 2 * re(1 / (1 + z))
        bound += 2 * K * abs(residue(z))^2
    end
    ok1 = bound > Arb(45769) / 100000
    println("multiple-pole bound > 0.45769: ", ok1 ? "PASS" : "FAIL", "   value ", bound)
    ok1 || (fails += 1)

    # Positive-weight bound with Fejér degree 100 at the first zero.
    z1 = zs[1]; deg = 100
    harmonics_ok = all(!contains_zero(zeta_ball(Acb(half, k * imag(z1)))) for k in 2:deg)
    println("99 higher harmonics of the first ordinate are zero-free: ", harmonics_ok ? "PASS" : "FAIL")
    harmonics_ok || (fails += 1)
    amp = 2 * Arb(deg) * abs(residue(z1)) / (deg + 1)
    osc = 1 + 1 / (1 + 2half) + re(1 / (1 + 2z1)) - 2 * re(1 / (1 + z1))
    cross = 1 - 1 / (1 + half) - re(1 / (1 + z1)) + 2 * re(1 / (1 + half + z1))
    pw = 2 * b^2 / 3 + 2 * b * amp * cross + amp^2 * osc
    ok2 = pw > Arb(3257) / 5000
    println("positive-weight bound > 0.6514: ", ok2 ? "PASS" : "FAIL", "   value ", pw)
    ok2 || (fails += 1)

    # Two-frequency bound with degree 30 at the first two zeros.
    deg2 = 30
    z = zs[1:2]
    pairing(u, w) = 1 - re(1 / (1 + u)) - re(1 / (1 + w)) + re(1 / (1 + u + w)) + re(1 / (1 + u + conj(w)))
    amps = [b; [2 * deg2 * abs(residue(zz)) / (deg2 + 1) for zz in z]]
    freqs = [(Float64(midpoint(i * imag(z[1]) + j * imag(z[2]))), i, j, i * imag(z[1]) + j * imag(z[2]))
             for i in -deg2:deg2 for j in -deg2:deg2]
    sort!(freqs; by = first)
    separated = all(freqs[k][4] < freqs[k+1][4] for k in 1:length(freqs)-1)
    poles = Set([(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)])
    regular = [f for f in freqs if !((f[2], f[3]) in poles)]
    nonvanishing = all(!contains_zero(zeta_ball(Acb(half, f[4]))) for f in regular)
    params = [Acb(half); z]
    tf = sum(amps[i] * amps[j] * pairing(params[i], params[j]) for i in 1:3, j in 1:3)
    ok3 = separated && nonvanishing && length(freqs) == 3721 && length(regular) == 3716 &&
          tf > Arb(1811) / 2500
    println("two-frequency bound > 0.7244 (3721 frequencies, 3716 regular): ", ok3 ? "PASS" : "FAIL",
            "   value ", tf)
    ok3 || (fails += 1)

    println("failures: $fails")
    return fails
end

exit(main() == 0 ? 0 : 1)
