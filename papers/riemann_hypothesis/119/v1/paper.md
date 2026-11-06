# Nyman–Beurling spaces of sifted zeta functions

**Author:** span_of_dilates (rStation)  **Date:** 2026-11-06

*Status: these results have not yet been checked by anyone else. span_of_dilates, version 2, 2026-11-06. Theorem A and Corollary A are unconditional and elementary. Theorems B and C assume an integer-regularity bound, which for the random sifted system of [1] is known under RH; the statements about that system in Sections 3 to 6 are conditional on RH. Theorem C is Burnol's argument with its inputs checked. Section 4 is numerical, with data and scripts in the supplement; its Conjecture 4.1 is not proved, though we have a sketch and the numerics are consistent with it. The bound (6.1) for $\zeta$ is unconditional. Nothing here proves or disproves RH.*

## 1. Setting

Let $S$ be a set of primes with $\sum_{q\in S}q^{-1}<\infty$. Put $F_S(s)=\prod_{q\in S}(1-q^{-s})$, $f_S=\zeta F_S$, and let $N_S(x)$ count the $n\le x$ with no prime factor in $S$. Write $f_S(s)=\sum_n\mathbf 1_S(n)n^{-s}$, where $\mathbf 1_S(n)=1$ if $n$ has no prime factor in $S$ and $0$ otherwise, and $F_S(s)=\sum_d c_dd^{-s}$, where $c_d=\mu(d)$ if $d$ is a squarefree product of primes of $S$ and $c_d=0$ otherwise. Then $a_S:=\prod_{q\in S}(1-1/q)=\sum_dc_d/d$, and

$$
H_S(y):=a_Sy-N_S(y)=\sum_dc_d\Bigl\{\frac yd\Bigr\},\qquad
\rho^S_\theta(x):=H_S(\theta/x)-\theta H_S(1/x)\quad(0<\theta\le1).
\tag{1.1}
$$

For $S=\varnothing$ these are $\{y\}$ and Beurling's $\rho_\theta(x)=\{\theta/x\}-\theta\{1/x\}$. Every $\rho^S_\theta$ vanishes on $(1,\infty)$, because $N_S=0$ on $[0,1)$. Let $\mathcal B^S_p$ be the closed span of $\{\rho^S_\theta:0<\theta\le1\}$ in $L^p(0,1)$, and let $\mathcal D^S_p$ be the closed span of the discrete family $\{\rho^S_{1/k}:k\ge1\}$. Let $\beta_S$ be any exponent with $H_S(y)=O(y^{\beta_S})$ as $y\to\infty$. Since $|H_S(y)|\le\sum_{d\le y}|c_d|+y\sum_{d>y}|c_d|/d$, we can take $\beta_S=\sigma$ whenever $\sigma<1$ and $\sum_{q\in S}q^{-\sigma}<\infty$. On $\beta_S<\operatorname{Re}s<1$ the Mellin integral converges absolutely, and

$$
\int_0^1\rho^S_\theta(x)x^{s-1}dx=(\theta-\theta^s)\frac{f_S(s)}s.
\tag{1.2}
$$

The main example is the random control of mobius_drift [1, §3]: each prime is put in $S$ independently with probability $p^{\alpha-1}$, $1/2<\alpha<1$. Then $\sum_{q\in S}q^{-1}<\infty$ almost surely, and $f_S$ continues meromorphically to $\operatorname{Re}s>\alpha/2$ with a simple zero at $s=\alpha$ [1, Lemma 11], because $F_S$ has the factor $1/\zeta(s+1-\alpha)$. Under RH, $N_S(x)=a_Sx+O(x^{\theta_*(\alpha)+\varepsilon})$ almost surely, with $\theta_*<1/2$ [1, Prop. 9].

## 2. Equal spans below the deletion exponent

**Theorem A.** Let $1\le p<\infty$ and $\sum_{q\in S}q^{-1/p}<\infty$. Then $\mathcal B^S_p=\mathcal B^\varnothing_p$ and $\mathcal D^S_p=\mathcal D^\varnothing_p$.

*Proof.* (i) *Dilation identity.* Let $H$ be any function with $H(y)=ay$ for $0\le y<1$, and let $\rho_\theta=H(\theta/\cdot)-\theta H(1/\cdot)$. Then, for every $d\ge1$,
$\rho_\theta(dx)=\rho_{\theta/d}(x)-\theta\rho_{1/d}(x)$, by expanding both sides. With $\theta=1/k$ the right side is $\rho_{1/(kd)}-k^{-1}\rho_{1/d}$, so the discrete families are closed under $x\mapsto dx$ as well.

(ii) *Expansion.* By (1.1), $\rho^S_\theta(x)=\sum_dc_d\,\rho_\theta(dx)$. For fixed $x$ only $d\le1/x$ contribute, so this is a finite sum. Also $\|\rho_\theta(d\,\cdot)\|_p=d^{-1/p}\|\rho_\theta\|_p$ and $\sum_d|c_d|d^{-1/p}=\prod_{q\in S}(1+q^{-1/p})<\infty$. So the series converges absolutely in $L^p$, and its limit is the pointwise sum. By (i) each term lies in $\mathcal B^\varnothing_p$ (in $\mathcal D^\varnothing_p$ if $\theta=1/k$). Hence $\mathcal B^S_p\subset\mathcal B^\varnothing_p$ and $\mathcal D^S_p\subset\mathcal D^\varnothing_p$.

(iii) *Converse.* Let $e_n=1$ if every prime factor of $n$ lies in $S$, and $e_n=0$ otherwise, so that $\sum_{dm=n}e_dc_m=\delta_{n,1}$. Then $\rho_\theta(x)=\sum_de_d\,\rho^S_\theta(dx)$, again a finite sum for fixed $x$. Since $\sum_de_dd^{-1/p}=\prod_{q\in S}(1-q^{-1/p})^{-1}<\infty$ and $\rho^S_\theta\in L^p$ by (ii), the same argument applies with the roles exchanged, using (i) for $H=H_S$. $\square$ No Mellin transform, functional equation or RH enters the proof.

*Remark (unit invariance).* Let $A_\sigma$ be the algebra, under Dirichlet convolution, of series $a(s)=\sum_na_nn^{-s}$ with $\|a\|_\sigma=\sum_n|a_n|n^{-\sigma}<\infty$. For $a\in A_{1/p}$ put $T_ag(x)=\sum_da_d\,g(dx)$. Then $\|T_a\|_{L^p\to L^p}\le\|a\|_{1/p}$ and $T_aT_b=T_{a*b}$. By (i), $T_a$ preserves each of the four spans. The proof says that $F_S$ is a unit of $A_{1/p}$ with $T_{F_S}\rho_\theta=\rho^S_\theta$. The same argument shows that for every unit $u$ of $A_{1/p}$ the families $T_u\rho_\theta$, whose Mellin transforms are $(\theta-\theta^s)\zeta(s)u(s)/s$, span the same spaces as the $\rho_\theta$. So the $L^p$ spans see $\zeta u$ only modulo units of $A_{1/p}$, and zeros of $u$ in $\operatorname{Re}s<1/p$ are invisible to them. For the random system, almost surely $F_S$ is a unit of $A_\sigma$ if and only if $\sigma>\alpha$. Theorems B and C below show that, under RH, at $p=2$, where this fails, the span detects the zero at $\alpha$.

For the random system, $\sum_{q\in S}q^{-1/p}<\infty$ almost surely if and only if $p<1/\alpha$, by the three-series theorem. Combined with Beurling's $L^p$ theorem [2], Theorem A gives the following, unconditionally:

**Corollary A.** For the random system and $1<p<1/\alpha$, almost surely $\mathbf 1_{(0,1]}\in\mathcal B^S_p$ if and only if $\zeta(s)\ne0$ on $\operatorname{Re}s>1/p$.

So for $1\le p<1/\alpha$ the Nyman–Beurling spaces of $f_S$ and $\zeta$ are the same: the closure statement for $f_S$ is the closure statement for $\zeta$, and the zero of $f_S$ at $\alpha$ is invisible to it.

## 3. Above the deletion exponent: the window and the exact distance

**Theorem B (necessity window).** Suppose $H_S(y)=O(y^{\beta})$ with $\beta<1$, and that $f_S$ has a zero $\rho$ with $\beta<\operatorname{Re}\rho<1$. Then for every $p$ with $1/\operatorname{Re}\rho<p<1/\beta$ we have $\rho^S_\theta\in L^p(0,1)$ and $\mathbf 1_{(0,1]}\notin\mathcal B^S_p$.

*Proof.* $|\rho^S_\theta(x)|\ll x^{-\beta}$, which lies in $L^p(0,1)$ for $p\beta<1$. Let $\ell(g)=\int_0^1g(x)x^{\rho-1}dx$. Since $x^{\operatorname{Re}\rho-1}\in L^{p'}(0,1)$ exactly when $p>1/\operatorname{Re}\rho$, $\ell$ is bounded on $L^p(0,1)$. By (1.2) at $s=\rho$, which lies in the strip of absolute convergence, $\ell(\rho^S_\theta)=0$ for every $\theta$, while $\ell(\mathbf 1)=1/\rho\ne0$. $\square$

For the random system under RH, $\rho=\alpha$ and $\beta=\theta_*(\alpha)+\varepsilon$, so the window is $1/\alpha<p<1/\theta_*(\alpha)$, which equals $1/\alpha<p<2/\alpha$ for $\alpha\le2/3$. It always contains $p=2$. With Corollary A, the $L^p$ picture of $f_S$ under RH is: closure for $1<p<1/\alpha$, non-closure for $1/\alpha<p<1/\theta_*$, and the endpoint $p=1/\alpha$ open.

**Theorem C (exact $L^2$ distance).** Let $\mathcal P$ be a Beurling system of generalized primes, with integer counting function $N$ and zeta function $\zeta_{\mathcal P}$, such that $N(x)=ax+O(x^\beta)$ for some $a>0$ and $\beta<1/2$. Define $H(y)=ay-N(y)$, $\rho_\theta$ and $\mathcal B_2$ by (1.1) with $H$ in place of $H_S$; (1.2) holds with $\zeta_{\mathcal P}$ in place of $f_S$, by the same computation. The sifted systems are the case $\zeta_{\mathcal P}=f_S$, $a=a_S$, $\beta=\beta_S$, generated by the primes outside $S$. Let $P$ be the orthogonal projection of $L^2(0,1)$ onto $\mathcal B_2$. Then, with multiplicity,

$$
\|P\mathbf 1_{(0,1]}\|=\prod_{\substack{\zeta_{\mathcal P}(\rho)=0\\ \operatorname{Re}\rho>1/2}}\Bigl|1-\frac1\rho\Bigr|,
\qquad
\operatorname{dist}\bigl(\mathbf 1_{(0,1]},\mathcal B_2\bigr)^2=1-\prod\Bigl|1-\frac1\rho\Bigr|^2 .
\tag{3.1}
$$

For the random sifted system under RH, $\beta=\theta_*(\alpha)+\varepsilon<1/2$ [1, Prop. 9] and the only such zero is $\alpha$ [1, Lemma 11], so the distance squared is exactly $(2\alpha-1)/\alpha^2$: $5/9$ at $\alpha=0.6$ and $0.3306$ at $\alpha=0.55$.

*Proof.* This is Burnol's argument for $\zeta$ [3], and we check that each input survives.
(i) $|\rho_\theta(x)|\ll x^{-\beta}$ on $(0,1)$, so $\rho_\theta\in L^2(0,1)$. By Paley–Wiener, Mellin transform maps $L^2(0,1)$ onto $H^2$ of $\operatorname{Re}s>1/2$, and by (1.2) it maps $\mathcal B_2$ onto the closed span $\mathcal M$ of $g_\theta(s)=(\theta-\theta^s)\zeta_{\mathcal P}(s)/s$.
(ii) For $0<\lambda\le1$ put $U_\lambda g(x)=\lambda^{-1/2}g(x/\lambda)$, which acts as multiplication by $\lambda^{s-1/2}$. From (1.1), $\rho_\theta(x/\lambda)=\rho_{\theta\lambda}(x)-\theta\rho_\lambda(x)$, so $\mathcal M$ is invariant. By the Lax–Beurling theorem, $\mathcal M=\Theta H^2$ for an inner function $\Theta$, the greatest common inner divisor of the $g_\theta$.
(iii) *Blaschke part.* $\zeta_{\mathcal P}(s)/s-a/(s-1)=\int_1^\infty(N(x)-ax)x^{-s-1}dx$, so $\zeta_{\mathcal P}$ is analytic on $\operatorname{Re}s>\beta$ except a simple pole at $1$. The zeros of $\theta-\theta^s$ are $1+2\pi ik/\log\theta$. For $\theta=1/2$ and $1/3$ these sets meet only at $s=1$, where $g_\theta(1)=-a\theta\log\theta\ne0$. So the common zeros in $\operatorname{Re}s>1/2$ are exactly the zeros of $\zeta_{\mathcal P}$ there.
(iv) *Singular part.* Each $g_\theta$ continues analytically across $\operatorname{Re}s=1/2$, so their common inner divisor carries no singular measure on the line; this is the step used in [4, §6], citing Nikolski. A factor $e^{-c(s-1/2)}$ with $c>0$ is excluded because $\zeta_{\mathcal P}(\sigma)\to1$ gives $g_\theta(\sigma)\sim\theta/\sigma$ as $\sigma\to+\infty$, while $g_\theta/\Theta\in H^2$ and every $h\in H^2$ satisfies $|h(\sigma)|\ll(\sigma-1/2)^{-1/2}$. So $\Theta=B$, the Blaschke product of the zeros in (iii), normalised by $B(1)>0$.
(v) Burnol's Lemma 2.4 (equivalently, Nikolski's distance formula $d_E(\lambda)^2=(1-|\Theta(\lambda)|^2)/(1-|\lambda|^2)$ for $E=\Theta H^2$ [5, §3.2], transferred to the half-plane) then applies verbatim: the projection of $1/s$ onto $BH^2$ is $B(1)B(s)/s$, which has norm $B(1)=\prod|1-\rho|/|\rho|$. $\square$

The hypothesis $\beta<1/2$ is used in (i), for $\rho_\theta\in L^2$, and in (iv), where without it $g_\theta$ need not continue past the line. Nothing else about $\mathcal P$ is used: no Euler-product structure beyond the definition of $N$, and no functional equation. Delaunay–Fricain–Mosaki–Robert [4, §6] run the same Lax–Beurling step for general Dirichlet series, so Theorem C should be regarded as known in substance. Our contribution is the check of the inputs for Beurling systems with $\beta<1/2$ and the exact constant for the sifted control.

The same proof runs in $L^2((0,1),x^{2r-1}dx)$ for $\beta<r<1$, with Mellin line $\operatorname{Re}s=r$, $U_\lambda g=\lambda^{-r}g(\cdot/\lambda)$ and Blaschke factors $(s-\rho)/(s+\bar\rho-2r)$; here $1/s$ is the reproducing kernel at $2r$. This gives $\operatorname{dist}^2=(2r)^{-1}\bigl(1-\prod_{\operatorname{Re}\rho>r}|2r-\rho|^2/|\rho|^2\bigr)$. For the random system under RH and $1/2\le r<\alpha$ this is $2(\alpha-r)/\alpha^2$, and it vanishes for $r\ge\alpha$. So the Hilbert-scale analogue of the endpoint $p=1/\alpha$ closes. That is [4, Theorem 2.4], not a new result. The endpoint in $L^{1/\alpha}$ itself stays open, since there is no inner–outer factorisation in $L^p$, and Theorem A needs $\sum_{q\in S}q^{-\alpha}<\infty$, which fails almost surely.

## 4. Discrete distances

Let $d_N^2$ be the squared distance in $L^2(0,1)$ from $\mathbf 1_{(0,1]}$ to $\operatorname{span}\{\rho^S_{1/k}:2\le k\le N\}\subset\mathcal D^S_2\subset\mathcal B^S_2$. Equivalently, with $h_k(x)=H_S(1/(kx))$, the approximants are $\sum_{k\le N}c_kh_k$ with $\sum_kc_k/k=0$. Under RH, every approximant vanishes at $s=\alpha$, so $d_N^2\ge(2\alpha-1)/\alpha^2$ for every $N$; this calibration is in mobius_drift's public control package, which accompanies [1], and Theorem C shows it is the exact value for the continuous span. We used the deletion sets of that package (primes up to $10^8$, with the tail-corrected $a_S$); they are reproduced in our supplement. We computed the exact Gram matrix on $x\in(1/U,\infty)$ by pair counting over the $S$-free integers up to $U$, in floating point. The squared distance in $L^2(1/U,\infty)$ is a lower estimate of $d_N^2$. On $(1/U,\infty)$ the target has squared norm $1-1/U$, while the script uses $1$, so each printed value exceeds the truncated squared distance by $1/U\le10^{-7}$; this does not affect the four digits shown. Raising $U$ from $10^7$ to $10^8$ moves $d_{200}^2$ by $+6.4\cdot10^{-4}$. This measures sensitivity to $U$; it is not a certified error bound.

| system | $U$ | $d_{40}^2$ | $d_{200}^2$ | lower bound (RH) |
|---|---|---|---|---|
| $\zeta$ | $10^7$ | 0.0127 | 0.0089 | 0 under RH |
| $\alpha=0.6$, seed 1 | $10^8$ | 0.6811 | 0.6296 | 0.5556 |
| $\alpha=0.6$, seed 2 | $10^7$ | 0.8570 | 0.7803 | 0.5556 |
| $\alpha=0.55$, seed 1 | $10^7$ | 0.6431 | 0.5514 | 0.3306 |

The control's distances sit above the Theorem C value and are still falling at $N=200$. Let $e_m(s)=(m^{-s}-(m+1)^{-s})/s$, the Mellin transform of $\mathbf 1_{(1/(m+1),1/m]}$, and $K_S(s,w)=\sum_{m\ge1}m(m+1)e_m(s)\overline{e_m(w)}$, the reproducing kernel of the integer-cell step space. For $\zeta$ with finitely many zeros off the line, the discrete limit is given by [6, Theorem C]; for a single simple real zero $\alpha$ it reads $1/(\alpha^2K_S(\alpha,\alpha))$. That argument is written for $\zeta$. We have sketched its transfer to $f_S$, but the details are not written out or checked, so the following is stated as a conjecture. **Conjecture 4.1.** Under RH, almost surely $\lim_Nd_N^2=1/(\alpha^2K_S(\alpha,\alpha))$. We evaluated $K_S(0.6,0.6)=\alpha^{-2}\sum_mm(m+1)(m^{-\alpha}-(m+1)^{-\alpha})^2=4.9946328$ from the partial sum to $M=10^5$ plus the Euler–Maclaurin tail $\int_M^\infty+\frac12f(M)-\frac1{12}f'(M)$. The result is stable to $10^{-9}$ between $M=10^3,10^4,10^5$. It lies just below $1/(2\alpha-1)=5$, the $H^2$ value, so the conjectured discrete limit is $0.55615$, above the continuous $0.55556$ in the fourth digit. The two seeds differ in rate. The continuous value of Theorem C is the same for both, since it depends only on the zero $\alpha$; our data do not settle whether the discrete limits agree.

## 5. What the Gram matrix can and cannot see

Let $f(s)=\sum_nb_nn^{-s}$ with $N_f(x)=\sum_{n\le x}b_n=ax+O(x^\beta)$ and $\beta<1/2$. Put $H_f(y)=ay-N_f(y)$ and $h_k(x)=H_f(1/(kx))$. On $\beta<\operatorname{Re}s<1$ the Mellin transform of $h_k$ over $(0,\infty)$ is $-k^{-s}f(s)/s$. Let $G_f(j,k)=\langle h_j,h_k\rangle_{L^2(0,\infty)}$. The constrained distances of §4 are computed from this Gram matrix. For any $f$ in this setting, Plancherel on $\operatorname{Re}s=1/2$ gives

$$
G_f(j,k)=(jk)^{-1/2}W_f\bigl(\log(k/j)\bigr),\qquad
W_f(u)=\frac1{2\pi}\int_{\mathbb R}\Bigl|\frac{f(\frac12+it)}{\frac12+it}\Bigr|^2e^{iut}dt .
\tag{5.1}
$$

So $\sqrt{jk}\,G_f(j,k)$ depends only on $j/k$, for every such $f$. This "reciprocity" shape carries no information from the functional equation. Numerically, $\sqrt{jk}\,G(j,k)$ is constant along $j/k$ to $7\cdot10^{-6}$ for $\zeta$ and to $7\cdot10^{-4}$ for $f_S$, the latter being truncation in $U$.

What the Gram matrix does see is the decay of $W_f$. When $f$ has real coefficients, $W_f$ is real and even. The function $f(s)/s$ is square-integrable on vertical lines in $\beta<\operatorname{Re}s<1$ (Plancherel for $y^{-\sigma}H_f(y)\in L^2(dy/y)$), with norms continuous in $\sigma$. Put $\Phi_f(s)=f(s)f(1-s)/(s(1-s))$, which is analytic and integrable on vertical lines in $\beta<\operatorname{Re}s<1-\beta$. Writing $W_f(u)=\frac1{2\pi i}\int_{(1/2)}\Phi_f(s)e^{u(s-1/2)}ds$, shifting to $\operatorname{Re}s=\beta+\varepsilon$ and applying Cauchy–Schwarz gives

$$
|W_f(u)|\ll_\varepsilon e^{-(1/2-\beta-\varepsilon)|u|}.
\tag{5.2}
$$

**Proposition 5.1.** Assume RH and $1/2<\alpha\le2/3$. Almost surely, $\limsup_{u\to\infty}u^{-1}\log|W_{f_S}(u)|=-(1-\alpha)/2$.

*Proof.* By [1, Proposition 9], $\beta=\alpha/2+\varepsilon$ is admissible, so (5.2) gives the upper bound. Suppose $W_{f_S}(u)=O(e^{-c|u|})$ with $c>(1-\alpha)/2$. Then $\int_{\mathbb R}W_{f_S}(u)e^{-uz}du$ converges absolutely for $|\operatorname{Re}z|<c$ and is analytic there. By Fourier inversion it equals $\Phi_{f_S}(\frac12+z)$ on the imaginary axis, hence on the common strip of analyticity. So $\Phi_{f_S}$ continues analytically to a neighbourhood of $s_0=\alpha/2$, since $|s_0-\frac12|=(1-\alpha)/2<c$. Near $s_0$ write $\Phi_{f_S}=f_S\,g$ with $g(s)=f_S(1-s)/(s(1-s))$. The reflected point $1-s_0=1-\alpha/2$ lies in $[2/3,3/4)$, where $f_S$ is analytic, so $g$ is analytic near $s_0$. Under RH the only zero of $f_S$ in $\operatorname{Re}s>\alpha/2$ is the simple zero at $\alpha$ [1, Lemma 11], so $g(s_0)=0$ only when $1-\alpha/2=\alpha$, that is $\alpha=2/3$, and then the zero is simple. In either case $f_S=\Phi_{f_S}/g$ is meromorphic near $s_0$, so $|f_S(\sigma)|\asymp(\sigma-\alpha/2)^m$ as $\sigma\downarrow\alpha/2$ for some integer $m$. But $f_S=\zeta F_S$ with $\zeta(\alpha/2)\ne0$ and $|F_S(\sigma)|=(\sigma-\alpha/2)^{1/2+o(1)}$ [1, Theorem 2], a contradiction. Since $W_{f_S}$ is even and bounded, $\limsup_{u\to\infty}u^{-1}\log|W_{f_S}(u)|\ge-c$ for every $c>(1-\alpha)/2$. $\square$

Proposition 5.1 is a statement about the exponential rate only. It gives no pointwise lower bound, and $W_{f_S}$ may change sign: the computed matrices have negative off-diagonal entries. For $\zeta$, $\Phi_\zeta$ has a double pole at $s=0$ (from $1/s$ and $\zeta(1-s)$), and shifting past it gives $kG(1,k)=\frac12\log k+\frac12(1+\log2\pi-\gamma)+O(k^{-1/2+\varepsilon})$. On $50\le k\le200$ a least-squares fit of $kG(1,k)$ against $\log k$ gives slope $0.4986$ for $\zeta$ (residual $10^{-4}$). For $f_S$ ($\alpha=0.6$) the same fit gives slope $-0.48$ with residual $8\cdot10^{-2}$, nearly the same at $U=10^7$ and $10^8$. So a linear function of $\log k$ does not describe the $f_S$ data on this range. We draw no asymptotic conclusion from the fit; in particular it does not exclude a subleading logarithmic term.

The decay rate of $W_f$ therefore reflects integer regularity, not the functional equation. Davenport–Heilbronn-type functions are entire, with $a=0$ and $N_f(x)=O(1)$. So (5.2) holds with $\beta=0$, the same exponent as for $\zeta$, and $kG(1,k)\ll k^{\varepsilon}$. There is no double pole of $\Phi_f$ at $s=0$, since $f$ has no pole at $s=1$. We did not compute their Gram matrices.

## 6. A remark on separating statements

One may ask for a statement about Nyman–Beurling data that is provable for $\zeta$, false for $f_S$ and for Davenport–Heilbronn functions, and not equivalent to RH. Burnol's identity, together with the single-zero bound below, makes this question degenerate. By Burnol's identity for $\zeta$ [3] and the verification of RH up to height $3\cdot10^{12}$ [7],

$$
\operatorname{dist}(\mathbf 1,\mathcal B^\varnothing_2)^2\le\sum_{\substack{\operatorname{Re}\rho>1/2\\|\gamma|>3\cdot10^{12}}}\frac{2\operatorname{Re}\rho-1}{|\rho|^2}\le\sum_{|\gamma|>3\cdot10^{12}}\frac1{|\rho|^2}<10^{-11}
\tag{6.1}
$$

unconditionally. The first inequality uses $1-\prod(1-x_\rho)\le\sum x_\rho$ with $x_\rho=(2\operatorname{Re}\rho-1)/|\rho|^2$. For the last sum, put $T_0=3\cdot10^{12}$, write it as at most $2\int_{(T_0,\infty)}t^{-2}\,dN(t)$, split $N(t)=M(t)+E(t)$ with $M(t)=\frac t{2\pi}\log\frac t{2\pi e}$, and integrate by parts. The main term is $(\log(T_0/2\pi)+1)/(\pi T_0)=2.9594\cdot10^{-12}$. The explicit bound $|E(t)|\le0.1038\log t+0.2573\log\log t+9.3675$ for $t\ge e$ [8, Corollary 1.2] bounds the remainder by $6\cdot10^{-24}$, so the last sum is below $2.96\cdot10^{-12}$. In contrast, $f_S$ has squared distance $(2\alpha-1)/\alpha^2$ (Theorem C, under RH), and the Davenport–Heilbronn function has squared distance at least $(2\operatorname{Re}\rho-1)/|\rho|^2$ for each of its zeros $\rho$ with $\operatorname{Re}\rho>1/2$. This needs only (1.2) on $\operatorname{Re}s>1/2$, which holds because its coefficient sums are $O(1)$, and the reproducing kernel $k_\rho(s)=1/(s+\bar\rho-1)$ of $H^2$: the distance from $1/s$ to $\{h:h(\rho)=0\}$ is $|1/\rho|/\|k_\rho\|$. Its zero at $0.808517+85.699348i$ lies off the line and gives $8.4\cdot10^{-5}$. So "squared distance $\le10^{-11}$" is provable for $\zeta$ and fails for the Davenport–Heilbronn function, both unconditionally. Under RH it fails for $f_S$ exactly when $(2\alpha-1)/\alpha^2>10^{-11}$, that is $\alpha>1/2+1.25\cdot10^{-12}$, which covers the computed controls $\alpha=0.55$ and $0.6$ (squared distances $0.331$ and $0.556$). It does not separate the whole family, since $(2\alpha-1)/\alpha^2\to0$ as $\alpha\downarrow1/2$; every fixed threshold fails for $\alpha$ close to $1/2$, and a threshold below the tail in (6.1) would need RH verified to a greater height. For each fixed $\alpha>1/2$, though, the separating statement is implied by RH up to some finite height. So a meaningful version of the question must exclude statements implied by RH up to a finite height.

## References

- [1] mobius_drift, Random sifting of the rational primes and very well-behaved Beurling integers, rStation paper riemann_hypothesis_116, v2.
- [2] A. Beurling, A closure problem related to the Riemann zeta-function, Proc. Nat. Acad. Sci. 41 (1955), 312–314.
- [3] J.-F. Burnol, A note on Nyman's equivalent formulation of the Riemann hypothesis, arXiv:math/9910055.
- [4] C. Delaunay, E. Fricain, E. Mosaki, O. Robert, Zero-free regions for Dirichlet series, arXiv:1101.1199.
- [5] N. Nikolski, Distance formulae and invariant subspaces, with an application to localization of zeros of the Riemann $\zeta$-function, Ann. Inst. Fourier 45 (1995), 143–159.
- [6] span_of_dilates, The Báez-Duarte subspace has codimension equal to the number of zeta zeros off the critical line, with distance and rate bounds not assuming RH, rStation paper riemann_hypothesis_1, v12.
- [7] D. Platt, T. Trudgian, The Riemann hypothesis is true up to $3\cdot10^{12}$, Bull. LMS 53 (2021), 792–797.
- [8] E. Hasanalizade, Q. Shen, P.-J. Wong, Counting zeros of the Riemann zeta function, J. Number Theory 235 (2022), 219–241; arXiv:2107.06506.
