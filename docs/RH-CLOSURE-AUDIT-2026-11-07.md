# Audit of the remaining RH estimate

Date: 7 November 2026. Scope: `paper/local-energy.tex`,
`paper/abel-obstruction.tex`, `paper/mellin-positivity.tex`, and the
zero-free equivalences and classical additive estimate in `paper/main.tex`.

## Conclusion

The identities in the current argument do not prove RH. The remaining
prime-tail estimate is **equivalent to RH**, with the stated quantifiers.
There is, however, a valid additional consequence of the paper's existing
classical input: the exponential prime tail cancels its comparison main
term to every logarithmic order. Its square-root-sized error remains
unproved. The logarithmic consequence below should not be presented as a
new zero-free result or as an independently novel theorem.

## 1. Cancellation in the actual exponential kernel

Let

\[
B(X)=\sum_{n\ge1}\lambda(n)e^{-n/X},\qquad
y=(\log X)^2,
\]

and retain the manuscript's definitions of \(B_y,c_y,T_y\), so that

\[
B(X)=B_y(X)+T_y(X),\qquad
B_y(X)-c_yX=O(X^{1/2+o(1)}).
\]

The classical Davenport estimate already invoked in Section 3 implies,
at additive frequency zero, for every \(A>0\),

\[
L(t):=\sum_{n\le t}\lambda(n)
 =O_A\!\left(\frac{t}{(\log(2t))^A}\right).
\]

Partial summation gives the absolutely convergent identity

\[
B(X)=\frac1X\int_1^\infty L(t)e^{-t/X}\,dt.
\]

For \(1\le t\le\sqrt X\), the trivial bound \(|L(t)|\le t\) makes
the integral, after the factor \(1/X\), at most \(1/2\). For
\(t\ge\sqrt X\), \(\log(2t)\ge\tfrac12\log X\), and hence this
part has modulus at most

\[
\frac{C_A2^A}{X(\log X)^A}
 \int_0^\infty te^{-t/X}\,dt
 =\frac{C_A2^AX}{(\log X)^A}.
\]

It follows that \(B(X)=O_A(X/(\log X)^A)\). Substituting the exact
convolution identity gives the proved statement

\[
\boxed{\quad
T_y(X)=-c_yX+O_A\!\left(\frac{X}{(\log X)^A}\right)
\quad\text{for every fixed }A>0.\quad}
\]

Indeed \(X^{1/2+o(1)}=o(X/(\log X)^A)\) for each fixed \(A\).
The elementary bound \(c_y\ge y^{-2}=(\log X)^{-4}\) then gives

\[
\frac{T_y(X)}{c_yX}=-1+O_A((\log X)^{4-A}),
\]

so the ratio tends to \(-1\). This is exponential-kernel cancellation,
not merely an Abel-weight limit. It uses a classical cancellation theorem
already cited by the paper; it does not supply the stronger power saving.

## 2. Exact equivalence of the target and RH

Put \(R(X)=T_y(X)+c_yX\). The finite-prime theorem gives

\[
R(X)-B(X)=c_yX-B_y(X)=O(X^{1/2+o(1)}).
\]

Consequently the following assertions are equivalent:

1. For every \(\varepsilon>0\),
   \(R(X)=O_\varepsilon(X^{1/2+\varepsilon})\).
2. For every \(\varepsilon>0\),
   \(B(X)=O_\varepsilon(X^{1/2+\varepsilon})\).
3. RH.

For 1 iff 2, apply the displayed difference with a smaller positive
exponent. Assertion 2 iff 3 is the smoothed Mellin criterion already
proved in the paper: its transform is
\(\Gamma(s)\zeta(2s)/\zeta(s)\), whose numerator is nonzero at any
putative zero with real part greater than one half. Conversely, under RH
the reciprocal estimate and contour argument supplied in the manuscript
give the smoothed bound. Calling the prime-tail target a consequence of
the convolution identity, without an additional arithmetic estimate,
would assume an equivalent form of RH.

## 3. Why the proved Abel zero cannot finish the argument

For fixed \(y\),

\[
H_y(s)=\frac{\zeta(2s)}{\zeta(s)^2c_y(s)},\qquad
c_y(s)=\prod_{p\le y}\frac{1-p^{-s}}{1+p^{-s}}.
\]

Every finite Euler factor in \(c_y\) is holomorphic and nonzero on
\(\operatorname{Re}s>0\). If \(\rho\) were a zeta zero of order
\(r\) with \(\operatorname{Re}\rho>1/2\), the leading Laurent term
of this meromorphic continuation would be

\[
H_y(s)=
\frac{(r!)^2\zeta(2\rho)}
 {c_y(\rho)(\zeta^{(r)}(\rho))^2}
 (s-\rho)^{-2r}
 +O((s-\rho)^{1-2r}).
\]

Its coefficient is nonzero. A double zero at \(s=1\) therefore
coexists logically with genuine poles away from the real axis. The
argument must exclude those poles through a global arithmetic bound;
the local zero at one does not do so. The bounded-coefficient moment
construction in the appendix correctly illustrates this obstruction,
but is not multiplicative and must not be described as a counterexample
to an implication using the full arithmetic structure of Liouville.

## 4. Checks of the displayed analytic arguments

- The local Legendre reconstruction transfers a neighboring-scale
  mean-square upper bound to point evaluation. It does not prove that
  mean-square bound. Its stated Taylor remainder and kernel constants
  are consistent with the displayed estimates.
- The finite-prime comparison follows from the absolutely convergent
  convolution \(f_y=\mathbf 1*g_y\), and the polylogarithmic prime
  cutoff gives its stated square-root error with a subpower loss.
- Prime dilations are not orthogonal: for distinct primes \(p,q\),
  \(\lambda(pn)\lambda(qn)=1\) identically. The manuscript correctly
  retains this full off-diagonal contribution.
- The Mellin positivity statements give lower oscillation bounds.
  They do not furnish the upper estimate needed for RH. In particular,
  the proposed eventual-sign condition would also force simplicity of
  every critical zero, and remains unproved.
- The moment interpolation construction is analytic and valid for each
  fixed finite number of moments. Its constants may depend on that
  number. It constructs no sequence with every logarithmic moment zero.
- Finite rational checks support finite identities only. No infinite
  cancellation estimate or new Lean formalization follows from those
  checks.

## Publication consequence

The stronger title may describe the proved zero-free exponent identity.
The abstract should identify RH as the unresolved endpoint estimate.
The new logarithmic prime-tail consequence can be included with its
classical dependency stated, while the square-root prime-tail estimate
must remain an explicit open input.
