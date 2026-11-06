# Finite-prime filtering and the Liouville exponential sum

This attempt gives a quantitative finite-prime barrier, an exact cost for recovering a sum after removing small primes, and an explicit failure of a diagonal adaptive-filter criterion. It does not prove a new power bound for

\[
B(X)=\sum_{n\ge1}\lambda(n)e^{-n/X}.
\]

The Mellin equivalence in `paper/routes.tex` is used only to identify what a proposed estimate would imply. All estimates proved below are unconditional. The external asymptotics used are Mertens' theorems and the classical prime number theorem. They impose no zero-free hypothesis near the critical line. Primary sources are [Mertens, *Ein Beitrag zur analytischen Zahlentheorie* (1874)](https://www.digizeitschriften.de/download/pdf/243919689_0078/log5.pdf) and [Hadamard, *Sur la distribution des zéros de la fonction ζ(s) et ses conséquences arithmétiques* (1896)](https://archive.numdam.org/item/BSMF_1896__24__199_1/).

## 1. A finite-prime model with a uniform error

For real \(y\ge2\), let \(f_y\) be completely multiplicative with

\[
f_y(p)=\begin{cases}-1,&p\le y,\\+1,&p>y.\end{cases}
\]

Put

\[
B_{f_y}(X)=\sum_{n\ge1}f_y(n)e^{-n/X},\qquad
c_y=\prod_{p\le y}\frac{p-1}{p+1},
\]

and, for \(\sigma>0\),

\[
G_y(\sigma)=\prod_{p\le y}\frac{1+p^{-\sigma}}{1-p^{-\sigma}}.
\]

**Proposition 1.** For every \(X>0\), \(y\ge2\), and \(0<\sigma<1\),

\[
\boxed{\quad B_{f_y}(X)=c_yX+O\bigl(X^\sigma G_y(\sigma)\bigr).\quad}
\tag{1}
\]

The implied constant can be taken to be one.

**Proof.** Define a multiplicative function \(g_y\) by

\[
g_y(p^k)=2(-1)^k\quad(p\le y,\ k\ge1),\qquad
g_y(p^k)=0\quad(p>y,\ k\ge1).
\]

At each prime the divisor sum is \(f_y\), so \(f_y=1*g_y\). Its absolutely convergent exponential sum is therefore

\[
B_{f_y}(X)=\sum_{d\ge1}\frac{g_y(d)}{e^{d/X}-1}.
\]

For \(u>0\),

\[
\left|\frac1{e^u-1}-\frac1u\right|
\le\min(1,u^{-1})\le u^{-\sigma}.
\]

The series \(\sum |g_y(d)|d^{-\sigma}\) converges because its prime support is finite, and its value is \(G_y(\sigma)\). Also

\[
\sum_{d\ge1}\frac{g_y(d)}d
=\prod_{p\le y}\left(1+2\sum_{k\ge1}\frac{(-1)^k}{p^k}\right)
=c_y.
\]

Subtraction proves (1). This also justifies all exchanges of summation. ∎

In particular, fixed \(y\) gives \(B_{f_y}(X)\sim c_yX\). This model supplies the large-mean counterpart to the finite-prime cancellation example already in `paper/main.tex`.

The estimate is uniform for a substantially growing prime range. For \(y\ge e^4\), take

\[
\sigma=1-\frac1{\log y}.
\]

Then

\[
G_y(\sigma)\ll(\log y)^2.
\tag{2}
\]

Indeed, \(\sigma\ge3/4\) and

\[
\log G_y(\sigma)=2\sum_{p\le y}p^{-\sigma}+O(1).
\]

Writing \(\alpha=1/\log y\), the inequality \(e^v-1\le ev\) for \(0\le v\le1\) gives

\[
\sum_{p\le y}\frac{p^\alpha-1}{p}
\le e\alpha\sum_{p\le y}\frac{\log p}{p}=O(1).
\]

For the weighted sum, even the elementary Chebyshev bound suffices. Writing \(\vartheta(t)=\sum_{p\le t}\log p\ll t\), partial summation gives

\[
\sum_{p\le y}\frac{\log p}{p}
=\frac{\vartheta(y)}y+\int_2^y\frac{\vartheta(t)}{t^2}\,dt
\ll\log y.
\]

Together with the elementary Mertens upper bound \(\sum_{p\le y}1/p\le\log\log y+O(1)\), this proves (2) with an absolute constant. No prime number theorem is needed for that uniform error estimate. Thus

\[
B_{f_y}(X)=c_yX+
O\left(Xe^{-\log X/\log y}(\log y)^2\right).
\tag{3}
\]

Also Mertens' product theorem gives

\[
c_y=
\prod_{p\le y}(1-p^{-1})^2
\prod_{p\le y}(1-p^{-2})^{-1}
\sim\frac{\zeta(2)e^{-2\gamma}}{(\log y)^2}.
\tag{4}
\]

**Corollary 2.** Fix \(A>4\) and set

\[
y=y(X)=\exp\left(\frac{\log X}{A\log\log X}\right).
\]

Then

\[
B_{f_{y(X)}}(X)
\sim \zeta(2)e^{-2\gamma}A^2X
\left(\frac{\log\log X}{\log X}\right)^2.
\tag{5}
\]

**Proof.** Divide the error in (3) by \(c_yX\). By (4), the result is

\[
O\left(e^{-\log X/\log y}(\log y)^4\right)
=O\left(A^{-4}\frac{(\log X)^{4-A}}{(\log\log X)^4}\right)=o(1).
\]

Here \(y\ge e^4\) holds for all sufficiently large \(X\), with that lower threshold allowed to depend on the fixed \(A\). Insert the chosen value of \(\log y\) into (4). ∎

The same proof works at \(A=4\). There is a further extension to **every fixed \(A>0\)** if the Rankin parameter is adjusted. For any fixed \(t>0\), take \(\sigma=1-t/\log y\), which is at least \(3/4\) for sufficiently large \(y\). The preceding calculation uses instead

\[
\sum_{p\le y}\frac{p^{t/\log y}-1}{p}
\le\frac{te^t}{\log y}\sum_{p\le y}\frac{\log p}{p}
=O_t(1),
\]

and gives \(G_y(\sigma)\ll_t(\log y)^2\). The relative error in (5) is consequently

\[
O_t\left(A^{-4}\frac{(\log X)^{4-tA}}{(\log\log X)^4}\right).
\]

Choose one fixed \(t>4/A\). Formula (5) follows for that \(A\) as well. The constants may depend on \(A\) through this choice of \(t\).

For each large \(X\), this is a completely multiplicative sign function agreeing with Liouville at **every prime up to the displayed growing threshold**, while its exponential sum exceeds \(X^{1/2+\varepsilon}\) for every fixed \(0<\varepsilon<1/2\). Thus complete multiplicativity and that finite-prime agreement cannot give a uniform square-root estimate over such functions. The counterexample function depends on \(X\). No assertion is made that one fixed function can agree with Liouville on every eventually growing prime range and retain this large mean.

## 2. Removing small primes preserves every right-hand pole

Use \(P^-(1)=\infty\) and define the rough Liouville sum

\[
R_y(X)=\sum_{P^-(n)>y}\lambda(n)e^{-n/X}.
\]

For each fixed finite \(y\), absolute convergence in \(\Re s>1\) gives

\[
\int_0^\infty R_y(X)X^{-s}\frac{dX}{X}
=\Gamma(s)\frac{\zeta(2s)}{\zeta(s)}E_y(s),
\qquad E_y(s)=\prod_{p\le y}(1+p^{-s}).
\tag{6}
\]

Every factor of \(E_y\) is nonzero on \(\Re s>0\). Therefore an off-line zero \(\rho\) of order \(m\), with \(\Re\rho>1/2\), remains a pole of order \(m\) in (6). Its leading Laurent coefficient is

\[
\frac{m!\,\Gamma(\rho)\zeta(2\rho)E_y(\rho)}{\zeta^{(m)}(\rho)}.
\]

The finite filter does not cancel that pole. Consequently a square-root estimate for \(R_y\) with one fixed \(y\) has the same zero-exclusion implication as the original estimate for \(B\).

There is also a quantitative lower bound for its multiplier. For \(\beta=\Re\rho>0\),

\[
|E_y(\rho)|\ge\prod_{p\le y}(1-p^{-\beta}).
\tag{7}
\]

The reciprocal product in (7) is exactly the absolute recovery cost below.

## 3. The cost of recovering the original sum

Every integer has a unique factorization into a \(y\)-smooth part and a \(y\)-rough part. Consequently

\[
B(X)=\sum_{P^+(a)\le y}\lambda(a)R_y(X/a).
\tag{8}
\]

Here \(a=1\) is included. Conversely, if \(P_y=\prod_{p\le y}p\),

\[
R_y(X)=\sum_{d\mid P_y}B(X/d).
\tag{9}
\]

The latter identity follows at each small prime from
\((1+p^{-s})(1+p^{-s})^{-1}=1\), or directly by divisor convolution. These identities converge absolutely after exponential weighting.

For \(0<\theta<1\), write

\[
\mathcal R_{y,\theta}(X)=
\sup_{0<t\le X}t^{-\theta}|R_y(t)|,
\qquad
M_y(\theta)=\prod_{p\le y}(1-p^{-\theta})^{-1}.
\]

Taking absolute values in (8) proves the exact useful bound

\[
\boxed{\quad |B(X)|\le X^\theta
\mathcal R_{y,\theta}(X)M_y(\theta).\quad}
\tag{10}
\]

For the reverse comparison, (9) gives

\[
\mathcal R_{y,\theta}(X)
\le
\left(\sup_{0<t\le X}t^{-\theta}|B(t)|\right)
\prod_{p\le y}(1+p^{-\theta}).
\tag{11}
\]

The prime number theorem and partial summation yield

\[
\log M_y(1/2)
=\sum_{p\le y}p^{-1/2}+O\left(\sum_{p\le y}p^{-1}\right)
=(2+o(1))\frac{\sqrt y}{\log y}.
\tag{12}
\]

Thus an adaptive rough-sum estimate

\[
\mathcal R_{y(X),1/2}(X)\ll_\varepsilon X^\varepsilon
\]

would imply the target estimate whenever

\[
\frac{\sqrt{y(X)}}{\log y(X)}=o(\log X).
\tag{13}
\]

For instance \(y(X)=(\log X)^2\) meets (13). The estimate must hold for **all smaller scales \(t\le X\) with this same cutoff \(y(X)\)**. A bound only at the diagonal \(t=X\) cannot be substituted into (8).

Formula (12) also identifies the transition of this absolute inversion estimate. If

\[
y(X)=C(\log X)^2(\log\log X)^2\qquad(C>0\text{ fixed}),
\]

then

\[
M_{y(X)}(1/2)=X^{\sqrt C+o(1)}.
\tag{14}
\]

The exponent \(\sqrt C\) is the actual loss of this absolute convolution bound. Improving it requires cancellation in the smooth-part inversion, or a stronger rough-sum estimate.

## 4. Two explicit failures of overly aggressive adaptive filtering

First, large prime removal can produce a deterministic prime bias. Fix \(1/2<\alpha<1\) and take \(y=X^\alpha\). A composite \(y\)-rough integer is at least \(y^2\). Therefore

\[
R_y(X)=e^{-1/X}-\sum_{p>y}e^{-p/X}
+O\left(Xe^{-y^2/X}\right).
\]

By the prime number theorem, \(\sum_p e^{-p/X}\sim X/\log X\), while the contribution of \(p\le y\) is at most \(y=o(X/\log X)\). Hence

\[
\boxed{\quad R_{X^\alpha}(X)\sim-\frac X{\log X}.
\quad}
\tag{15}
\]

So removing all primes through a power cutoff larger than \(\sqrt X\) does not supply a square-root rough sum in this regime.

Second, a much larger diagonal cutoff gives a vacuous strong bound. For any sequence \(|f(n)|\le1\), let

\[
R_y^f(X)=\sum_{P^-(n)>y}f(n)e^{-n/X}.
\]

Every term other than \(n=1\) has \(n>y\), so for \(X\ge1\),

\[
|R_y^f(X)|\le1+\frac{e^{-y/X}}{1-e^{-1/X}}
\le1+2Xe^{-y/X}.
\]

Taking \(y=X\log(2X)\) gives

\[
|R_{X\log(2X)}^f(X)|\le2.
\tag{16}
\]

This holds even for the completely multiplicative function \(f\equiv1\), whose original exponential sum is

\[
\sum_{n\ge1}e^{-n/X}=\frac1{e^{1/X}-1}\sim X.
\]

Thus a diagonal adaptive filtered bound of order one does not control the original sum. For fixed \(y\), (6) has a single Mellin multiplier. Substituting \(y=y(X)\) inside the signal destroys that fixed-transform identity, so its nonvanishing argument cannot be applied unchanged.

## 5. An exact prime-tail cancellation problem

One can isolate the remaining large-prime arithmetic without losing poles. Define

\[
h_y(d)=\begin{cases}
2^{\omega(d)}\lambda(d),&P^-(d)>y,\\
0,&\text{otherwise},
\end{cases}
\qquad h_y(1)=1.
\]

The local Euler factors give \(\lambda=f_y*h_y\). Thus

\[
B(X)=B_{f_y}(X)+T_y(X),
\qquad
T_y(X)=\sum_{\substack{d>1\\P^-(d)>y}}
2^{\omega(d)}\lambda(d)B_{f_y}(X/d).
\tag{17}
\]

This sum is absolutely convergent for each \(X\). For example \(2^{\omega(d)}\le\tau(d)\) and
\(|B_{f_y}(X/d)|\le(e^{d/X}-1)^{-1}\), which gives a summable exponential majorant for large \(d\).

At \(\sigma=1/2\), the prime number theorem gives

\[
\log G_y(1/2)=(4+o(1))\frac{\sqrt y}{\log y}.
\]

Consequently any choice satisfying (13), such as \(y=(\log X)^2\), makes the error in Proposition 1 of size \(X^{1/2+o(1)}\). In this regime the target estimate for \(B\) is equivalent to

\[
\boxed{\quad T_{y(X)}(X)
=-c_{y(X)}X+O_\varepsilon(X^{1/2+\varepsilon})
\quad\text{for every }\varepsilon>0.\quad}
\tag{18}
\]

All small-prime information in the kernel \(B_{f_y}\) is explicit. The unknown signs in the coefficients of \(T_y\) involve primes greater than \(y\). Equation (18) specifies a cancellation of the main term, rather than an upper bound obtained from absolute values. For \(y=(\log X)^2\), that main term is asymptotic to \(\zeta(2)e^{-2\gamma}X/[4(\log\log X)^2]\), so the cancellation required is substantial.

Equation (18) is a reformulation with the large-prime task isolated. The identities and finite-prime estimates above do not prove it. They also explain why absolute prime-tail estimates, fixed local Euler information, and a diagonal adaptive filter cannot supply the requested square-root result on their own.

## 6. A proved all-prime cancellation in an Abel weight

The all-prime tail does cancel the finite-prime linear mean in an exact convergent Abel model. Define, for real \(s>1\),

\[
c_y(s)=\prod_{p\le y}\frac{1-p^{-s}}{1+p^{-s}},
\qquad
H_y(s)=\sum_{P^-(d)>y}\frac{2^{\omega(d)}\lambda(d)}{d^s}.
\]

The series is absolutely convergent, and its Euler product is

\[
\boxed{\quad H_y(s)=\frac{\zeta(2s)}{\zeta(s)^2c_y(s)}.\quad}
\tag{19}
\]

This is the Dirichlet series of the function \(h_y\) in (17).

**Proposition 3.** Uniformly for \(y\ge2\), \(0<\delta\le\delta_0\), and \(\delta\log y\le1\),

\[
H_y(1+\delta)
=\frac{\zeta(2)\delta^2}{c_y}
\left(1+O\bigl(\delta(1+\log y)\bigr)\right).
\tag{20}
\]

In particular, when \(\delta\log y\to0\),

\[
\sum_{\substack{d>1\\P^-(d)>y}}
\frac{2^{\omega(d)}\lambda(d)}{d^{1+\delta}}
=-1+\frac{\zeta(2)\delta^2}{c_y}
\left(1+O\bigl(\delta(1+\log y)\bigr)\right).
\tag{21}
\]

**Proof.** The Laurent expansion at one and regularity at two give

\[
\frac{\zeta(2+2\delta)}{\zeta(1+\delta)^2}
=\zeta(2)\delta^2(1+O(\delta)).
\]

For real \(s\ge1\),

\[
\frac{d}{ds}\log c_y(s)
=2\sum_{p\le y}\frac{(\log p)p^{-s}}{1-p^{-2s}}
\ll\sum_{p\le y}\frac{\log p}{p}
\ll\log y.
\]

Thus \(c_y(1+\delta)/c_y=\exp(O(\delta\log y))\). On the stated range, expanding this bounded exponential gives (20) from (19). Removing the \(d=1\) term gives (21). ∎

For fixed \(y\), (21) tends to \(-1\). This is an actual cancellation theorem for the indicated prime-tail series. It also holds in a growing-cutoff regime. If \(\delta=1/\log X\) and \(y=\exp(\log X/(A\log\log X))\), then by (4)

\[
H_y(1+1/\log X)
\sim\frac{e^{2\gamma}}{A^2(\log\log X)^2}.
\tag{22}
\]

Its relation to the linear mean is transparent at the Dirichlet-series level. The model has series \(\zeta(s)c_y(s)\). Multiplying by (19) gives \(\zeta(2s)/\zeta(s)\), the Liouville series. At \(s=1+\delta\) their leading sizes are

\[
\frac{c_y}{\delta}\cdot
\frac{\zeta(2)\delta^2}{c_y}
=\zeta(2)\delta.
\]

The tail supplies a double zero which cancels the model's pole at one. This calculation uses only absolutely convergent Euler products and the pole of \(\zeta\) at one.

It does not justify substituting the exponential kernel in (17) into the Abel cancellation (21). The exponential kernel is \(B_{f_y}(X/d)\), rather than a constant multiple of \(d^{-1-\delta}\) uniformly over all contributing \(d\). The signed discrepancy between these kernels is an additional sum requiring control. Absolute coefficients exhibit the cost explicitly,

\[
\sum_{P^-(d)>y}\frac{2^{\omega(d)}}{d^s}
=\frac{\zeta(s)^2}{\zeta(2s)}c_y(s),
\tag{23}
\]

which has a double pole at one for fixed \(y\). Consequently the small value in (20) cannot be transferred by an absolute kernel comparison. No square-root estimate for that discrepancy has been proved here. The exact all-prime cancellation explains removal of the linear mean, while the possible poles strictly between one-half and one remain the unresolved issue.
