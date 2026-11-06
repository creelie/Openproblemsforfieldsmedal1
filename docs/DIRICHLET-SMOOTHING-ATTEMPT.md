# Dirichlet smoothing across all conductors

Let \(\lambda(n)=(-1)^{\Omega(n)}\), and extend Dirichlet characters by zero on nonunits. Include the character of conductor one, whose \(L\)-function is \(\zeta\). For \(X>0\) put

\[
 B_\chi(X)=\sum_{n\ge1}\lambda(n)\chi(n)e^{-n/X},\qquad
 A_*(X)=\sum_{q\ge1}\frac{1}{q^2\varphi(q)}
       \sum_{\chi\bmod q}^{*}|B_\chi(X)|^2 ,
\]

where the star restricts to primitive characters. The series converges absolutely, since \(|B_\chi(X)|\le \sum_{n\ge1}e^{-n/X}\le X\) and there are at most \(\varphi(q)\) summands at conductor \(q\).

## Large conductors

For every \(X,Q\ge1\),

\[
 \sum_{q\ge Q}\frac{1}{q^2\varphi(q)}
   \sum_{\chi\bmod q}^{*}|B_\chi(X)|^2
 \ll \frac{X^2}{Q^3}+\frac{X}{Q}.
\]

For \(R\le q<2R\), the weight \(1/(q^2\varphi(q))\) is at most \(R^{-3}q/\varphi(q)\). Apply the multiplicative large sieve to \(T_\chi(y)=\sum_{n\le y}\lambda(n)\chi(n)\), with the sum interpreted as zero for \(y<1\). It gives

\[
 \sum_{R\le q<2R}\frac{1}{q^2\varphi(q)}
   \sum_{\chi\bmod q}^{*}|T_\chi(y)|^2
 \ll R^{-3}(y+4R^2)y .
\]

By partial summation \(B_\chi(X)=X^{-1}\int_0^\infty T_\chi(y)e^{-y/X}\,dy\). Minkowski's integral inequality in the weighted Euclidean norm bounds the square root of the block contribution by

\[
 \frac{C}{XR^{3/2}}
 \int_0^\infty (y+2R\sqrt y)e^{-y/X}\,dy
 \ll \frac{X}{R^{3/2}}+\sqrt{\frac XR}.
\]

Square and sum over \(R=2^jQ\), \(j\ge0\), to obtain the claim. The argument applies to any coefficients of modulus at most one. In particular the portion with \(q\ge X^{1/3}\) is \(O(X)\), with an absolute constant. The large sieve used here is the classical [Montgomery–Vaughan inequality](https://doi.org/10.1112/S0025579300004708) in its [primitive character form](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf).

The \(X^2/Q^3\) term is necessary for estimates uniform over completely multiplicative signs. For an odd prime \(r\) of size \(Q\) with \(r\ge Q\), take the Legendre character \(\chi_r\) and extend its signs to a completely multiplicative function \(f\) by setting \(f(r)=1\). The \(\chi_r\) twist of \(f\) equals one away from multiples of \(r\) and vanishes on the multiples. Its smoothed sum is \(\gg X\) for \(X\ge2\), by counting the nonmultiples up to \(X\). This single primitive term contributes \(\gg X^2/Q^3\). A bound specific to \(\lambda\) must use more than complete multiplicativity to improve the uniform cutoff exponent \(1/3\).

The same estimate holds for a sum over all characters whose **primitive conductor** is at least \(Q\), with weights still assigned by their moduli. If \(\chi\) modulo \(rk\) is induced by a primitive \(\chi_*\) modulo \(r\), inclusion-exclusion and complete multiplicativity give

\[
 B_\chi(X)=\sum_{d\mid k}\mu(d)\lambda(d)\chi_*(d)B_{\chi_*}(X/d).
\]

Primes dividing \(r\) cause no difficulty because \(\chi_*\) vanishes on their multiples. For each fixed \(k\) there is one lift per primitive \(\chi_*\), and \(\varphi(rk)\ge\varphi(r)\varphi(k)\) by the prime-power formula. Thus the square root of the \(k\)-layer contribution is at most

\[
 \frac{C}{k\sqrt{\varphi(k)}}\sum_{d\mid k}
       \left(\frac{X/d}{Q^{3/2}}+\sqrt{\frac{X/d}{Q}}\right)
 \le \frac{C\tau(k)}{k\sqrt{\varphi(k)}}
       \left(\frac{X}{Q^{3/2}}+\sqrt{\frac XQ}\right).
\]

The previous integral proof works at all positive arguments \(X/d\). The series \(\sum_k\tau(k)^2/(k^2\varphi(k))\) converges, even with \(\varphi(k)\) omitted, by the elementary divisor bound \(\tau(k)\ll_\varepsilon k^\varepsilon\). Squaring and summing the layers proves the claim.

## The exponent and the small conductors

Let \(\Theta_D\) be the supremum of real parts of nontrivial zeros over primitive Dirichlet \(L\)-functions, including \(\zeta\). Then

\[
 \limsup_{X\to\infty}\frac{\log(1+A_*(X))}{\log X}=2\Theta_D .
\]

For the lower bound, suppose the limit superior is \(r\). Each fixed \(\chi\) satisfies \(B_\chi(X)=O_{\chi,\varepsilon}(X^{r/2+\varepsilon})\) for every \(\varepsilon>0\), by its positive weight in \(A_*\). The Mellin identity

\[
 \int_0^\infty B_\chi(X)X^{-s}\frac{dX}{X}
   =\Gamma(s)\frac{L(2s,\chi^2)}{L(s,\chi)}
   \qquad (\Re s>1)
\]

follows by absolute convergence and the Euler products. The integral at \(X\downarrow0\) is entire, by exponential decay. If \(r/2<\Re\rho\) for a zero \(\rho\) with \(\Re\rho>1/2\), choose \(\varepsilon\) smaller than the difference. The resulting holomorphic continuation to a neighborhood of \(\rho\) contradicts the pole there. The numerator has a nonvanishing Euler product because \(\Re(2\rho)>1\), and Gamma has no zeros. For \(\chi\) of conductor one there is also a pole at the real point \(s=1/2\) from \(\zeta(2s)\), since \(\zeta(1/2)\ne0\) by the alternating-series formula. The same argument with this pole gives \(r\ge1\).

For the upper bound suppose \(\Theta_D<1\) and fix \(\Theta_D<\sigma<1\). For every \(\eta>0\) there is a constant independent of \(q\) and \(t\) such that

\[
 |L(u+it,\chi)^{-1}|\ll_{\sigma,\Theta_D,\eta}
             (q(2+|t|))^\eta
             \qquad(\sigma\le u\le 2).
\]

Here is the conductor dependence. For a nonprincipal character, the partial sums of \(\chi\) have modulus at most \(q\), because each full period sums to zero. Partial summation gives \(|L(s,\chi)|\le q|s|/\Re s\) on \(\Re s>0\). Around \(2+it\), choose radii
\(1/2<2-\sigma<R_2<R<2-\Theta_D\). On the disk of radius \(R\), the holomorphic logarithm \(G=\log L\) normalized by the Euler product at its center has real part bounded above by \(C\log(q(2+|t|))\). The value at the center is bounded absolutely by the Euler product. Borel–Carathéodory bounds \(|G|\) on the disk of radius \(R_2\) by \(C'\log(q(2+|t|))\). On radius \(1/2\), the Euler product bounds \(|G|\) absolutely. Hadamard's three-circles theorem at radius \(2-\sigma\) therefore gives \(|G|\ll (\log(q(2+|t|)))^b\) for a fixed \(b<1\). Exponentiating gives the displayed subpower estimate. For conductor one the same disks work at \(|t|\ge4\), avoiding the pole of \(\zeta\) and using its polynomial growth from Euler summation. At bounded height compactness bounds \(1/\zeta\), extended by zero at \(s=1\).

Mellin inversion of the exponential weight on \(\Re s=2\) and a contour shift to \(\Re s=\sigma\) now give \(|B_\chi(X)|\ll_{\sigma,\Theta_D,\eta}q^\eta X^\sigma\). The numerator \(L(2s,\chi^2)\) is bounded on the intervening strip by \(\zeta(2\sigma)\). The bound on the reciprocal and Stirling's formula for \(\Gamma\) justify the shift and integration on the new line. Sum with \(0<\eta<1/2\) to obtain \(A_*(X)\ll X^{2\sigma}\), since \(\sum_{q\ge1}q^{-2+2\eta}<\infty\). Let \(\sigma\downarrow\Theta_D\). If \(\Theta_D=1\), the absolute bound \(A_*(X)\ll X^2\) suffices.

The functional equations give Dirichlet GRH if and only if \(\Theta_D=1/2\). Combining the exponent identity with the large-conductor estimate reduces the remaining upper bound to

\[
 \sum_{q<X^{1/3}}\frac{1}{q^2\varphi(q)}
       \sum_{\chi\bmod q}^{*}|B_\chi(X)|^2
       \ll_\varepsilon X^{1+\varepsilon}
       \quad\text{for every }\varepsilon>0 .
\]

This estimate remains unproved. The term at conductor one alone is \(|B_{\chi_1}(X)|^2\), so positive averaging does not cancel a possible contribution from an off-line zeta zero.

For the sum over all characters, omitting finitely many **moduli** would still leave every off-line zero detectable. Given a primitive character, lift it to any sufficiently large fixed multiple of its conductor. The Dirichlet \(L\)-function of the lift differs by a finite Euler product with no zeros on \(\Re s>0\), so the original zero produces a pole in the Mellin quotient of the lift. The weight of this term is fixed and positive as \(X\to\infty\).

## Diagonal of the full sum

Let \(A(X)\) denote the sum with all characters included. Character orthogonality gives

\[
 A(X)=\sum_{n,m\ge1}\lambda(n)\lambda(m)e^{-(n+m)/X}
       \sum_{\substack{q\mid n-m\\(q,n)=1}} q^{-2},
\]

where all positive \(q\) divide zero. Absolute convergence follows by bounding the innermost sum by \(\zeta(2)\). The diagonal \(n=m\) equals

\[
 \zeta(2)\sum_{d\ge1}\frac{\mu(d)}{d^2(e^{2d/X}-1)}
 =\frac{\zeta(2)}{2\zeta(3)}X+O(1).
\]

Indeed, \(\sum_{(q,n)=1}q^{-2}=\zeta(2)\sum_{d\mid n}\mu(d)d^{-2}\) by inclusion-exclusion. Summing the resulting geometric series over multiples of \(d\) gives the first identity. The estimate uses \((e^y-1)^{-1}=y^{-1}+O(1)\) uniformly for \(y>0\). The off-diagonal includes the signed sum at \(q=1\), which contributes \(|B_{\chi_1}(X)|^2-\sum_n e^{-2n/X}\). The linear size of the diagonal alone does not bound that term.

## Square-divisor factoring

The Möbius function \(\mu\) satisfies the two convolution identities

\[
 \lambda(n)=\sum_{d^2\mid n}\mu(n/d^2),\qquad
 \mu(n)=\sum_{d^2\mid n}\mu(d)\lambda(n/d^2).
\]

Both follow prime by prime, or by multiplying the respective Euler products by \(\zeta(2s)\) and its inverse. Define \(M_\chi(X)=\sum_{n\ge1}\mu(n)\chi(n)e^{-n/X}\). In the weighted square norm defining \(A_*\), the diagonal multiplier \(U_d\) with entries \(\chi(d)^2\) is a contraction. Thus the vector equations

\[
 B(X)=\sum_{d\ge1}U_d M(X/d^2),\qquad
 M(X)=\sum_{d\ge1}\mu(d)U_d B(X/d^2)
\]

transfer a bound of order \(X^{1/2+\varepsilon}\) in either direction by Minkowski and \(\sum_d d^{-1-2\varepsilon}<\infty\). A bound at arguments at least one extends to smaller positive arguments with a changed constant, by absolute exponential decay. Both series are absolutely convergent in the weighted norm. This route leaves the same small-conductor cancellation in the \(d=1\) term.

RH and Dirichlet GRH remain open in this calculation. The conductor estimates and Mellin argument above are classical analytic deductions and have not been formalized in Lean.
