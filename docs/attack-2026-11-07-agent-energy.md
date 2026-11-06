# Direct attack on the exponentially smoothed Liouville sum

The target is
\[
B(X)=\sum_{n\ge1}\lambda(n)e^{-n/X}
       =O_\varepsilon(X^{1/2+\varepsilon}).
\]
The following results are proved below without a zero-free-half-plane input. They give an explicit localization construction, the exact remaining signed energy, and quantitative tests of two proposed arithmetic routes. They do not establish the target estimate or RH. No claim of novelty is made for these analytic constructions.

## 1. Local positive energy controls a point with a logarithmic loss

This avoids the exponent loss obtained by using only a trivial derivative bound.

**Proposition.** Let \(|a_n|\le1\) be any complex sequence and set
\[
F(X)=\sum_{n\ge1}a_ne^{-n/X},\qquad
\mathcal H_F(X)=\int_{X/2}^{2X}|F(Y)|^2\,\frac{dY}{Y}.
\]
For \(X\ge1\), put \(m=\lceil8\log_2(2X)\rceil\). Then
\[
\boxed{\quad |F(X)|^2\le10(m+2)\mathcal H_F(X)+X^{-4}.\quad}       \tag{1}
\]
In particular the pointwise exponent and the dyadic local mean-square exponent agree up to the factor \(\log(2X)\).

**Proof.** Define
\[
G_X(z)=F\!\left(\frac{X}{1+z}\right)
      =\sum_{n\ge1}a_ne^{-n(1+z)/X}.
\]
The series is holomorphic for \(\Re z>-1\). On \(|z|\le1/2\),
\[
|G_X(z)|\le\frac1{e^{1/(2X)}-1}\le2X.
\]
Let \(P_m\) be its degree-\(m\) Taylor polynomial at zero. Cauchy's coefficient estimate gives, for \(|u|\le1/4\),
\[
|G_X(u)-P_m(u)|\le
 2X\sum_{j>m}(2|u|)^j
 \le2X\,2^{-m}=:\delta.
                                                        \tag{2}
\]
Importantly \(P_m(0)=G_X(0)=F(X)\) exactly.

Write \(L_j\) for the usual Legendre polynomials. Orthogonality on
\([-1/4,1/4]\) gives the evaluation kernel
\[
K_m(0,u)=2\sum_{j=0}^m(2j+1)L_j(0)L_j(4u).
\]
Every polynomial \(P\) of degree at most \(m\) satisfies
\[
P(0)=\int_{-1/4}^{1/4}K_m(0,u)P(u)\,du,\qquad
|P(0)|^2\le K_m(0,0)\int_{-1/4}^{1/4}|P(u)|^2\,du.       \tag{3}
\]
Here
\[
L_{2r+1}(0)=0,\qquad
L_{2r}(0)=(-1)^r\binom{2r}{r}4^{-r},\qquad
\left(\binom{2r}{r}4^{-r}\right)^2\le\frac1{r+1}.
\]
The last inequality follows by induction from the ratio
\((2r+1)/(2r+2)\): after squaring, the required comparison is
\((2r+1)^2(r+2)\le4(r+1)^3\). Consequently
\[
K_m(0,0)
=2\sum_{0\le r\le m/2}(4r+1)
       \left(\binom{2r}{r}4^{-r}\right)^2
\le8(\lfloor m/2\rfloor+1)\le4(m+2).                    \tag{4}
\]
Combining (2)--(4) and \(|P_m|^2\le2|G_X|^2+2\delta^2\) gives
\[
|F(X)|^2\le
 8(m+2)\int_{-1/4}^{1/4}|G_X(u)|^2\,du+4(m+2)\delta^2.
\]
Under \(Y=X/(1+u)\), the integral becomes
\[
\int_{4X/5}^{4X/3}|F(Y)|^2\frac{X}{Y^2}\,dY
\le\frac54\mathcal H_F(X).
\]
Also \(2^{-m}\le(2X)^{-8}\), so
\(\delta\le(128X^7)^{-1}\). For \(X\ge1\),
\(m+2\le16X\), by \(\log_2X\le2(X-1)\). Thus
\[
4(m+2)\delta^2\le\frac1{256X^{13}}\le X^{-4}.
\]
This proves (1).

The construction also explicitly reconstructs the point from neighboring
scales:
\[
F(X)=\int_{-1/4}^{1/4}K_m(0,u)
              F\!\left(\frac{X}{1+u}\right)\,du+\mathcal R_X,
\quad
|\mathcal R_X|\le\sqrt{2(m+2)}\,\delta.
                                                        \tag{5}
\]
Indeed the kernel reproduces \(P_m\), and its \(L^1\) norm is at most
\(\sqrt{K_m(0,0)/2}\). Its \(L^2\) cost is \(O(\sqrt{\log X})\).

The kernel construction is a standard orthogonal-polynomial method. The
normalization and reproducing identity agree with the
[Christoffel--Darboux kernel in NIST DLMF, Section 18.2(v)](https://dlmf.nist.gov/18.2.v).
All estimates needed here were derived explicitly above.

For the actual Liouville sum, (1) shows that the useful positive-energy
target is
\[
\mathcal H_B(X)\ll_\varepsilon X^{1+\varepsilon}.        \tag{6}
\]
This implication does not prove (6).

## 2. Exact diagonal and signed off-diagonal

Define
\[
K(v)=\int_{1/2}^{2}e^{-v/t}\,\frac{dt}{t}
    =\int_{1/2}^{2}e^{-vu}\,\frac{du}{u},\qquad v>0.
\]
Absolute convergence justifies expansion:
\[
\begin{split}
\mathcal H_B(X)
 &=\sum_{n,r\ge1}\lambda(n)\lambda(r)
                   K((n+r)/X)\\
 &=\mathcal D(X)+
 2\sum_{h\ge1}\sum_{n\ge1}
       \lambda(n)\lambda(n+h)K((2n+h)/X),               \tag{7}\\
\mathcal D(X)
 &=\int_{X/2}^{2X}\frac1{e^{2/Y}-1}\,\frac{dY}{Y}.
\end{split}
\]
The diagonal has the rigorous bounds
\[
\boxed{\quad
0<\mathcal D(X)-\left(\frac{3X}{4}-\log2\right)
 <\frac1{4X}.
\quad}                                                  \tag{8}
\]

To verify the constants, for every \(t>0\),
\[
0<
\frac1{e^t-1}-\frac1t+\frac12
<\frac t{12}.                                           \tag{9}
\]
The left inequality is equivalent to
\((t-2)e^t+t+2>0\). The latter function and its first derivative vanish
at zero, while its second derivative is \(te^t>0\).
For the right inequality, multiplication by \(12t(e^t-1)\) reduces it to
\[
(t^2-6t+12)(e^t-1)-12t
 =\sum_{j\ge5}\frac{(j-3)(j-4)}{j!}t^j>0.
\]
Substitute \(t=2/Y\) and integrate. The two leading terms give
\(3X/4-\log2\); the error is bounded by
\((1/6)\int_{X/2}^{2X}Y^{-2}\,dY=1/(4X)\).

Thus the diagonal is already at the requested scale. The exact missing
estimate is a **signed upper bound** for the double sum in (7).
Replacing its summands by absolute values gives a bound of order \(X^2\),
since \(K\) is positive and there are order \(X^2\) relevant pairs.
An \(O(X^{1+\varepsilon})\) upper bound cannot be read off from the
positivity of the whole energy.

Complete multiplicativity provides another exact organization, but not a
bound. Write \(n=da,r=db\), with \((a,b)=1\). Since
\(\lambda(da)\lambda(db)=\lambda(a)\lambda(b)\), one obtains
\[
\mathcal H_B(X)=\sum_{k\ge2}c(k)
       \int_{X/2}^{2X}\frac1{e^{k/Y}-1}\frac{dY}{Y},
\quad
c(k)=\sum_{\substack{1\le a<k\\(a,k)=1}}
                    \lambda(a)\lambda(k-a).            \tag{10}
\]
The term \(c(2)=1\) is precisely (8). All other terms are coprime
additive correlations. The sum is absolutely convergent at each \(X\),
because \(|c(k)|\le\varphi(k)\) and the kernel decays exponentially in
\(k/X\). Formula (10) isolates the arithmetic cancellation instead of
eliminating it.

## 3. The exact logarithmic identity

Let \(\Lambda\) be the von Mangoldt function. The correct convolution is
\[
\boxed{\quad
(\lambda\log)(n)
 =(\lambda*(\lambda\Lambda))(n),\qquad
\lambda(d)\Lambda(d)
 =2\mathbf1_{d=\square}\Lambda(\sqrt d)-\Lambda(d).
\quad}                                                  \tag{11}
\]
The first equality follows directly from complete multiplicativity and
\(\sum_{d\mid n}\Lambda(d)=\log n\).
For the second equality, both sides vanish unless \(d\) is a prime
power; at \(d=p^j\), they are \((-1)^j\log p\).
Equivalently, the logarithmic derivative of
\(\zeta(2s)/\zeta(s)\) gives (11) in \(\Re s>1\).

Therefore the exact smoothed identity is
\[
\boxed{\quad
\sum_{n\ge1}\lambda(n)\log n\,e^{-n/X}
 =2\sum_{d\ge1}\Lambda(d)B(X/d^2)
     -\sum_{d\ge1}\Lambda(d)B(X/d).
\quad}                                                  \tag{12}
\]
All double sums converge absolutely for fixed \(X\). For example their
absolute majorants are bounded by
\(\sum_d\Lambda(d)/(e^{d/X}-1)\) and
\(\sum_d\Lambda(d)/(e^{d^2/X}-1)\), respectively.
The identity is not an estimate: its main prime contribution still
contains the unknown sums \(B(X/p)\).

Two proposed positivity shortcuts fail:

* Prime dilations of the actual Liouville sequence are maximally
  correlated, not orthogonal. For any distinct primes \(p,q\) and
  integer \(N\ge1\),
  \[
  \sum_{n\le N}\lambda(pn)\lambda(qn)=N.                 \tag{13}
  \]
  Hence a prime-index second moment contains a full coherent
  off-diagonal. Discarding it would invalidate Cauchy--Schwarz.
* One cannot assign a positive sign to every scale product in (12).
  In fact \(B(1)>0\) and \(B(3)<-1/20\), so
  \(B(3)B(3/3)<0\). Here
  \[
  B(1)\ge e^{-1}-\frac{e^{-2}}{1-e^{-1}}>0.
  \]
  For a rational certificate of the second statement put
  \(a=7165/10000\), \(b=7166/10000\). Taylor bounds for \(e^{1/3}\)
  give \(a<e^{-1/3}<b\). With the actual values of \(\lambda(n)\) for
  \(n\le16\), an upper bound for \(B(3)\) is
  \[
  \sum_{n\in\{1,4,6,9,10,14,15,16\}}b^n
  -\sum_{n\in\{2,3,5,7,8,11,12,13\}}a^n
  +\frac{b^{17}}{1-b}<-\frac1{20}.                      \tag{14}
  \]
  This last inequality is an exact rational comparison. It was checked
  with integer numerator/denominator arithmetic. The bounds for the
  exponential can be reproduced by summing its series through degree
  12: if \(S_{12}=\sum_{j=0}^{12}(1/3)^j/j!\), then
  \(1/b<S_{12}\) and
  \(S_{12}+((1/3)^{13}/13!)/(1-1/42)<1/a\).
  This finite example does not rule out an additional asymptotic
  positivity theorem; it proves that such a theorem does not follow
  from the identity alone.

Thus (12) is a sound starting identity, but no contraction or
power-saving follows from taking absolute values or dropping its
prime-pair terms.

## 4. A quantitative obstruction to truncating to small primes

For \(y\ge2\), let \(f_y\) be completely multiplicative, with
\[
f_y(p)=-1\quad(p\le y),\qquad f_y(p)=1\quad(p>y).
\]
This is the natural small-prime truncation of Liouville. Define
\[
B_y(X)=\sum_{n\ge1}f_y(n)e^{-n/X},\quad
P_y=\prod_{p\le y}\frac{p-1}{p+1},\quad
A_y(\sigma)=\prod_{p\le y}\frac{1+p^{-\sigma}}{1-p^{-\sigma}}.
\]
For every \(X>0\) and \(0<\sigma<1\),
\[
\boxed{\quad |B_y(X)-XP_y|\le X^\sigma A_y(\sigma).\quad} \tag{15}
\]

**Proof.** Write \(f_y=1*h_y\). Prime by prime,
\[
h_y(p^j)=2(-1)^j\quad(j\ge1,\ p\le y),\qquad
h_y(p^j)=0\quad(p>y).
\]
Therefore
\[
B_y(X)=\sum_{d\ge1}\frac{h_y(d)}{e^{d/X}-1},\quad
\sum_{d\ge1}\frac{h_y(d)}d=P_y,\quad
\sum_{d\ge1}\frac{|h_y(d)|}{d^\sigma}=A_y(\sigma).
\]
These sums converge absolutely, since only finitely many primes support
\(h_y\). By (9) and \(e^t-1>t\),
\[
0\le \frac1t-\frac1{e^t-1}
 \le\min(1/2,1/t)\le t^{-\sigma}.
\]
Subtract \(X\sum h_y(d)/d\) and apply this inequality term by term.

There is an elementary growing-cutoff consequence, without PNT or RH.
For \(\sigma=1/2\),
\[
\log A_y(1/2)
\le4\sum_{p\le y}p^{-1/2}\le8\sqrt y.
\]
The first bound uses
\(\log((1+t)/(1-t))\le2t/(1-t^2)\) at \(t=p^{-1/2}\).
Also, putting \(r=\lfloor y\rfloor\),
\[
P_y\ge\prod_{n=2}^r\frac{n-1}{n+1}
     =\frac2{r(r+1)}\ge\frac1{y^2}.                     \tag{16}
\]
Thus, uniformly for \(2\le y\le(\log X)^2/1024\),
\[
B_y(X)=XP_y+O(X^{3/4}),\qquad
B_y(X)\ge\frac{X}{2y^2}
\quad\text{for sufficiently large }X.                  \tag{17}
\]
Indeed \(8\sqrt y\le(\log X)/4\); the error in (15) is at most
\(X^{3/4}\), while \(X/y^2\) dominates this uniformly in that range.

Hence this truncation has a nearly linear positive bias even though it
agrees with Liouville at every prime up to a growing cutoff. The missing
effect is cancellation involving the primes above \(y\). Bounding that
effect by absolute values cannot produce the target estimate.
Equation (17) is a statement about the explicit model \(f_y\), not an
assertion that the actual Liouville sum has this bias.

## 5. What the attempted routes do and do not supply

The established construction (1)/(5) is useful when an averaged bound is
available: it converts neighboring-scale \(L^2\) control to pointwise
control with a logarithmic cost. The energy expansion (7) gives its
precise arithmetic target. A proof of
\[
2\sum_{h\ge1}\sum_{n\ge1}
 \lambda(n)\lambda(n+h)K((2n+h)/X)
\ll_\varepsilon X^{1+\varepsilon}
\]
would supply (6), hence the desired pointwise bound. That signed upper
bound was not proved in this audit.

The exact identities (10)--(13) retain a coherent off-diagonal;
complete multiplicativity does not make it disappear. The truncation
theorem (15)--(17) shows quantitatively why information at only small
primes does not supply the missing global cancellation.

Published almost-all-short-interval results do not state the critical
bound (6). In particular,
[Matomäki--Radziwiłł, Annals of Mathematics 183 (2016), 1015--1056](https://annals.math.princeton.edu/2016/183-3/p06)
compares short averages with long averages. Applying that comparison
does not by itself establish the square-root size of the long average.
This is why its relative cancellation cannot be substituted for the
missing energy estimate above.

These arguments use neither the external quasi-Riemann manuscript nor
an unverified formalization. The Legendre facts have their classical
source noted above; the arithmetic identities and finite-product bounds
were derived directly. No full RH proof or new zero-free region results.
