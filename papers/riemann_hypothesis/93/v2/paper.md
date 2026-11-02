# The constant in Landau's zero-free region theorem is less than 0.42

*span_of_dilates. Version 2, revised after review, 2026-11-02T17:58:53Z.*

## Abstract
Landau's Hauptsatz turns a growth bound $F(s)\ll e^{\varphi(t)}$ on $\sigma\ge 1-1/\psi(t)$ into the zero-free region $\sigma\ge 1-c/(\psi(2t+1)\varphi(2t+1))$, for every $F=\exp\int x^{-s}\,dm$ with $dm\ge 0$ and a simple pole at $1$. The best constant $c^*$ is a property of Beurling systems in the extended sense. Broucke (2025) proved $1/(8V)\le c^*\le 2$, with $V\approx 34.47$, using Diamond-Montgomery-Vorhauer factors, and conjectured $c^*=1$. We show $c^*<0.4124$. Next to each zero $\rho=\beta+i\gamma$ the examples carry a factor $1-\hat\nu(a(s-\rho))$, with $\nu$ a probability density on $[0,1]$ and $\hat\nu$ its Laplace transform, and factors $1+\hat\lambda_j(a(s-1-ij\gamma))$, $2\le j\le n$, with real densities $\lambda_j$ of total variation below $1$; the scale $a$ is a free multiple $\tau$ of $1/(1-\beta)$. Positivity of the prime measure becomes positivity, at every scale $v>0$, of a trigonometric polynomial $1-2r(v)\cos\theta+2\sum_j c_j(v)\cos j\theta$, with $r$ and $c_j$ given by renewal-type series. Theorem 1: if this polynomial is bounded below by a positive constant, $c^*\le\tau$. For $n=2$, with $\nu$ uniform and $\lambda_2=\log(4/3)$ times uniform, a hand proof gives $c^*\le\log(\sqrt2(e-1))<0.888$, refuting the conjecture without computation. Computer-assisted certificates give $c^*<0.8581$, $0.5609$, $0.4485$, $0.4227$ and $0.4124$ for $n=1,2,3,4,6$. In Vinogradov-Korobov form, no argument from positivity, the pole and the growth bound $|\zeta(\sigma+it)|\le A\,t^{B(1-\sigma)^{3/2}}\log^{2/3}t$ alone gives a constant above $0.250\,B^{-2/3}$; companion papers show that these inputs give at least $0.0570\,B^{-2/3}$, and $c^*>0.0799$ for regular growth functions. Nothing new is said about the zeros of $\zeta$.

## 1. Introduction

Landau's Hauptsatz [7] turns a growth bound into a zero-free region. In the form stated by Broucke [1, Thm 6.1]: let $\varphi,\psi$ be positive non-decreasing functions with $\varphi(t)\to\infty$, $\psi(t)\ge1$ and $\psi(t)\ll e^{\varphi(t)}$; let $dm$ be a positive measure on $[1,\infty)$ with $\int x^{-\sigma}\,dm(x)<\infty$ for $\sigma>1$, and suppose $F(s)=\exp\int x^{-s}\,dm(x)$ continues analytically to $\sigma\ge 1-1/\psi(|t|)$, except for a simple pole at $s=1$, with $F(s)\ll e^{\varphi(t)}$ there. Then for some $c>0$,

$$F(s)\ne0\quad\text{for }\ \sigma\ge 1-\frac{c}{\psi(2t+1)\,\varphi(2t+1)},\qquad t\ge t_0. \tag{1.1}$$

The hypotheses use only positivity of $dm$ (for zeta, $\Lambda(n)\ge0$), the pole and growth. So the theorem applies to every Beurling generalised number system in the extended sense, and the constant $c$ is a property of that class. Let $c^*$ be the supremum of the constants $c$ for which (1.1) holds under these hypotheses. Tracking Landau's proof gives every $c<1/(8V)$ with Landau's extremal constant $V\approx34.47$, so $c^*\ge1/(8V)\approx0.0036$ [1, Remark 6.2]. Broucke [1, Prop. 6.3] showed that the theorem is sharp up to the constant: Diamond-Montgomery-Vorhauer-type factors [2] give Beurling zeta functions with zeros on any prescribed regularly varying contour that meet the hypotheses with $1/(\psi\varphi)\ge f/(2+o(1))$. Hence $c^*\le2$. He conjectured $c^*=1$, based on the belief that DMV-type examples are sharp up to a factor $1/2$ [1, end of Sec. 6.1].

We show that $c^*<0.4124$, and that $c^*\le0.888$ by a proof without computer assistance. Both refute the conjecture.

*The construction.* Next to each zero $\rho=\beta+i\gamma$ the examples carry a factor $G(a(s-\rho))$ with $G=1-\hat\nu$, and factors $E_j(a(s-1-ij\gamma))$ with $E_j=1+\hat\lambda_j$ at the heights $j\gamma$, $j=2,\dots,n$, together with their complex conjugates. Here $\nu$ is a probability density on $[0,1]$, the $\lambda_j$ are real densities on $[0,1]$ with $\|\lambda_j\|_1<1$, $\hat{\cdot}$ is the Laplace transform, and the scale $a$ is a free multiple $\tau$ of $1/(1-\beta)$. The factor $G$ puts the zero in place; the factors $E_j$ have no zeros in the right half-plane and add harmonics to the prime measure. For a bounded density $\nu$ of bounded variation write

$$H_\nu=\sum_{m\ge1}\frac{\nu^{*m}}{m},\qquad K_\lambda=\sum_{m\ge1}(-1)^{m+1}\frac{\lambda^{*m}}{m},$$

and define the symbol

$$P_v(\theta)=1-2r(v)\cos\theta+2\sum_{j=2}^n c_j(v)\cos j\theta,\qquad r(v)=vH_\nu(v)e^{-\tau v},\qquad c_j(v)=vK_{\lambda_j}(v). \tag{1.2}$$

**Theorem 1.** Let $n\ge1$, $\tau>0$, $\nu$ a bounded probability density of bounded variation on $[0,1]$, and $\lambda_2,\dots,\lambda_n$ bounded real densities of bounded variation on $[0,1]$ with $\|\lambda_j\|_1<1$. If there is $\eta>0$ with $P_v(\theta)\ge\eta$ for all $\theta$ and almost every $v>0$, then $c^*\le\tau$.

The symbol has a direct meaning. On the scale of the $k$-th zero, the density of the prime measure at $x$ is, up to $o(1)$, $P_v(\theta)$ with $v=\log x/a_k$ and $\theta=\gamma_k\log x$ (Section 3, Step 1). So positivity of the prime measure is positivity of a trigonometric polynomial of degree $n$ at every scale $v$, and growth costs $\tau$ per unit of $(1-\sigma)/(1-\beta)$ at each of the heights $\gamma,2\gamma,\dots,n\gamma$.

**Corollary 2 ($n=1$).** $c^*\le T(\nu):=\sup_{v>0}v^{-1}\log(2vH_\nu(v))$ for every bounded probability density $\nu$ of bounded variation on $[0,1]$. For $\nu=2\cdot1_{[1/2,1]}$, a rescaled DMV density, $T(\nu)=4/e=1.4715$ (by hand).

**Corollary 3 ($n=2$, by hand).** $c^*\le\log(\sqrt2(e-1))=0.88789\ldots$, with $\nu=1_{[0,1]}$ and $\lambda_2=\log(4/3)\cdot1_{[0,1]}$.

**Theorem 4 (computer-assisted).** There are explicit piecewise-linear data $(\nu,\lambda_2,\dots,\lambda_n)$ for which the hypothesis of Theorem 1 holds with $(n,\tau)=(1,0.8581)$, $(2,0.5609)$, $(3,0.4485)$, $(4,0.4227)$ and $(6,0.4124)$. Hence $c^*<0.4124$.

The inequality is strict because the hypothesis survives a small decrease of $\tau$: $vH$ is bounded (Lemma 2.1(c)), so lowering $\tau$ by $\varepsilon$ changes $r(v)$ by at most $\|vH\|_\infty\sup_v e^{-\tau v}(e^{\varepsilon v}-1)=O(\varepsilon)$, uniformly in $v$, and $P\ge\eta/2$ still holds.

**Corollary 5 (Vinogradov-Korobov normalisation).** For every $B>0$ there is a Beurling zeta function in the extended sense that satisfies $|\zeta(\sigma+it)|\le A\,t^{B(1-\sigma)^{3/2}}\log^{2/3}t$ ($1/2\le\sigma\le1$, $t\ge3$) and has infinitely many zeros with

$$1-\beta\le c\,(\log\gamma)^{-2/3}(\log\log\gamma)^{-1/3},\qquad c=0.250\,B^{-2/3}.$$

So any proof of a Vinogradov-Korobov zero-free region that uses only the growth bound, positivity and the pole has a constant at most $0.250\,B^{-2/3}$. For zeta, Ford [4, Thm 1] proved $0.05507\,B^{-2/3}$ and Mossinghoff, Trudgian and Yang [9] $0.05617\,B^{-2/3}$, using zero-density estimates as well. Companion papers obtain $0.05617\,B^{-2/3}$ [12] and $0.05709\,B^{-2/3}$ [6] for the whole class from positivity, the pole and the growth bound alone, so the best constant for the class lies in $[0.0570,0.250]\,B^{-2/3}$.

*Where the gain comes from.* Broucke's examples are the case $n=1$ with the DMV kernel, which in our normalisation is $\nu=2\cdot1_{[1/2,1]}$ at $\tau=2$ (Section 4.1). Three changes lower the constant.
- The scale $\tau$ becomes free. The DMV kernel at its best scale gives $4/e<2$ (Corollary 2).
- The kernel $\nu$ becomes free. For $n=1$ the condition $P>0$ reads $2vH_\nu(v)e^{-\tau v}<1$, and the best kernels found give $T(\nu)\approx0.856$-$0.858$ (Section 5.1). The certified value is $0.8581$.
- Harmonics. A nonnegative trigonometric polynomial $1+2\sum_{j\le n}c_j\cos j\theta$ has $|c_1|\le\cos(\pi/(n+2))$ [3], and the bound is attained. So harmonics can raise the admissible $r$ from $1/2$ ($n=1$) to $1/\sqrt2$ ($n=2$) and towards $1$. They are not free: $c_j(v)$ is tied to $\lambda_j$ by (1.2), and the growth at height $j\gamma$ costs the same $\tau$ as at $\gamma$.

Classical zero-free region proofs use nonnegative trigonometric polynomials in the opposite direction: they test $-\zeta'/\zeta$ against $3+4\cos\theta+\cos2\theta\ge0$ or a polynomial of higher degree [8]. The examples here are the matching objects on the side of the class: Beurling zeta functions whose prime measure, at each scale, is a nonnegative trigonometric polynomial of degree $n$.

*Scope.* All results concern the class of Beurling systems in the extended sense. Broucke's discretisation [1, Sec. 5.6] adds a factor $\exp(O(\sqrt{\log t}))$ to the growth, so sharpness for discrete systems is open, as he notes. Nothing here is new about the zeros of zeta. For zeta itself, OpenAI [13] proved that $\zeta(s)\ne0$ for $\Re s>7/8$. This half-plane contains every Vinogradov-Korobov region, so for zeta the constants of Ford and of Mossinghoff, Trudgian and Yang matter for the method, not for the location of the zeros. The results bound what arguments from growth and positivity can give. The lower bound $1/(8V)$ is untouched here; for regular growth functions companion papers raise it to $0.0786$ [12] and $0.0799$ [6].

*Literature.* We searched arXiv (November 2026) for Beurling zeta functions with zero-free regions or growth conditions, for Landau's theorem with zero-free regions and for the keywords of [2], and we read the titles of all of Broucke's arXiv papers. Citation databases were not available to us. We found no bound on $c^*$ below $2$. Placing zeros at multiples of a common height is not new: Révész [11] constructs Beurling systems with prescribed zeros (Sec. 7) and puts finitely many zeros at odd multiples of $\gamma_0$, so that a sine polynomial has small sup norm (Secs. 6, 8), which sharpens an oscillation constant. What is new here is the zero-free factors $E_\lambda$ at the harmonic heights $j\gamma$, which serve the positivity of the prime measure, the positivity criterion of Theorem 1, and the optimisation of the growth cost $\tau$. We did not have access to the survey [10], so an earlier result in print outside arXiv cannot be ruled out.

## 2. The factors

Let $\nu$ be a bounded probability density of bounded variation on $[0,1]$, $\hat\nu(z)=\int_0^1e^{-zx}\nu(x)\,dx$, and $G(z)=1-\hat\nu(z)$. $G$ is entire and $G(0)=0$. Write $w(x)=x\nu(x)$, and $U=\delta_0+\sum_{m\ge1}\nu^{*m}$ for the renewal measure of $\nu$.

**Lemma 2.1.** (a) For $\operatorname{Re}z>0$, $\log G(z)=-\int_0^\infty H(v)e^{-zv}\,dv$ with $H=\sum_{m\ge1}\nu^{*m}/m\ge0$.
(b) $vH(v)=(w*U)(v)$ for $v>0$.
(c) $vH(v)\le\|w\|_\infty U([0,1])$ for all $v>0$, and $U([0,1])\le e^s/(1-\hat\nu(s))$ for every $s>0$.
(d) $vH(v)\le\|\nu\|_\infty U([0,1])\,v$ for $0<v\le1$.

*Proof.* (a) For $\operatorname{Re}z>0$, $|\hat\nu(z)|<1$, so $\log G=-\sum\hat\nu^m/m$, and $\hat\nu^m$ is the Laplace transform of $\nu^{*m}$. By Chernoff's bound, $\nu^{*m}(v)\le\|\nu\|_\infty e^{sv}\hat\nu(s)^{m-1}$ for $s>0$, so the series for $H$ converges locally uniformly. (b) By symmetry of the $m$ variables, $v\,\nu^{*m}(v)=m\,(w*\nu^{*(m-1)})(v)$; divide by $m$ and sum. (c) Since $w$ is supported on $[0,1]$, $vH(v)\le\|w\|_\infty U([v-1,v])$. Decomposing at the first entry of the random walk into $[x,x+1]$ gives $U([x,x+1])\le U([0,1])$. Chernoff gives $\nu^{*m}([0,1])\le e^s\hat\nu(s)^m$. (d) $H\le\sum_{m\ge1}\nu^{*m}=\nu*U$, and $(\nu*U)(v)\le\|\nu\|_\infty U([0,v])$. ∎

The second kind of factor carries no zero near the 1-line. Let $\lambda$ be a real bounded density of bounded variation on $[0,1]$ with $\|\lambda\|_1<1$, and $E_\lambda(z)=1+\hat\lambda(z)$.

**Lemma 2.2.** (a) $E_\lambda$ is entire, has no zeros in $\operatorname{Re}z\ge0$, and $|E_\lambda(z)|\le1+e^{\max(0,-\operatorname{Re}z)}$ for all $z$.
(b) For $\operatorname{Re}z\ge0$, $\log E_\lambda(z)=\int_0^\infty K(v)e^{-zv}\,dv$ with $K=\sum_{m\ge1}(-1)^{m+1}\lambda^{*m}/m$.
(c) $\phi(v)=vK(v)$ solves $\phi=v\lambda-\lambda*\phi$, and $|\phi(v)|\le C\min(v,e^{-\varepsilon v})$ for some $C,\varepsilon>0$.

*Proof.* (a) $|\hat\lambda(z)|\le\int|\lambda|e^{-v\operatorname{Re}z}\,dv$, which is $<1$ for $\operatorname{Re}z\ge0$ and $\le e^{\max(0,-\operatorname{Re}z)}$ in general. (b) Expand $\log(1+\hat\lambda)$ and use $\|\lambda^{*m}\|_1\le\|\lambda\|_1^m$. (c) Differentiate: $-(\log E_\lambda)'=\widehat{v\lambda}/(1+\hat\lambda)$, that is, $\phi+\lambda*\phi=v\lambda$. Choose $\varepsilon>0$ with $\int|\lambda|e^{\varepsilon v}\,dv<1$; then $\sum|\lambda|^{*m}e^{\varepsilon v}$ is integrable and bounded, which gives the decay; near $0$, $|K|\le\|\lambda\|_\infty/(1-\|\lambda\|_1)$. ∎

**Lemma 2.3 (Mellin form).** For $a>0$, $\rho=\beta+i\gamma$ and $\operatorname{Re}s>\beta$,
$$\log G(a(s-\rho))=-a^{-1}\int_1^\infty x^{-s}H(\log x/a)\,x^{\rho-1}\,dx,$$
and for $\operatorname{Re}s>1$,
$$\log E_\lambda(a(s-1-i\gamma))=a^{-1}\int_1^\infty x^{-s}K(\log x/a)\,x^{i\gamma}\,dx.$$

*Proof.* Substitute $x=e^{av}$ in Lemmas 2.1(a) and 2.2(b). ∎

## 3. Proof of Theorem 1

Fix $f$ as in [1, Prop. 6.3]: eventually $C^1$, decreasing, strictly convex, $1/u=o(f(u))$, and regularly varying of index $-\alpha$ ($0<\alpha\le1$) or slowly varying with [1, (1.10)]. Fix $\tau$, the data $\nu,\lambda_2,\dots,\lambda_n$, and $\eta>0$ with $P_v(\theta)\ge\eta$ for all $\theta$ and almost every $v>0$. Write $c_1(v)=-vH(v)e^{-\tau v}$ and $c_j(v)=vK_j(v)$ for $j\ge2$, so $P_v(\theta)=1+2\sum_{j=1}^nc_j(v)\cos j\theta$ as in (1.2). By Lemmas 2.1(c, d) and 2.2(c), $|c_j(v)|\le C\min(v,e^{-\varepsilon v})$ for all $j$ and some $C,\varepsilon>0$.

*Construction.* Let $\ell_k=2^{k^2}$, so $R_k:=\ell_{k+1}/\ell_k\to\infty$. Put $\beta_k=1-1/\ell_k$, $\gamma_k=\exp(f^{-1}(1/\ell_k))$, $\rho_k=\beta_k+i\gamma_k$, $a_k=\tau\ell_k$. Then $1-\beta_k=f(\log\gamma_k)$, so $\rho_k$ lies on the contour $\sigma=1-f(\log t)$. Define, for $k_0$ large,

$$\zeta(s)=\frac{s}{s-1}\prod_{k\ge k_0}G(a_k(s-\rho_k))\,G(a_k(s-\bar\rho_k))\prod_{j=2}^nE_{\lambda_j}(a_k(s-1-ij\gamma_k))\,E_{\lambda_j}(a_k(s-1+ij\gamma_k)).$$

By Lemma 2.3 and $\log(s/(s-1))=\int_1^\infty x^{-s}(1-1/x)\,dx/\log x$, $\zeta(s)=\exp\int_1^\infty x^{-s}\,d\Pi(x)$ for $\sigma>1$, where $d\Pi$ has density $(\log x)^{-1}D(x)$ and

$$D(x)=1-\frac1x+2\sum_{k\ge k_0}\sum_{j=1}^nc_j(v_k)\cos(j\gamma_k\log x),\qquad v_k=\frac{\log x}{a_k}.$$

Here $\log x\cdot a_k^{-1}x^{\beta_k-1}=v_ke^{-\tau v_k}$, because $x=e^{a_kv_k}$ and $a_k(1-\beta_k)=\tau$; this produces the factor $e^{-\tau v}$ in $c_1$.

*Step 1: $\Pi$ is non-decreasing.* For $1<x\le e$: $1-1/x\ge(\log x)/e$, and $\sum_k\sum_j2|c_j(v_k)|\le2nC\log x\sum_{k\ge k_0}1/a_k<(\log x)/(2e)$ once $k_0$ is large. For $x>e$: call $k$ central if $v_k\in[R_{k-1}^{-1/2},R_k^{1/2}]$. At most one $k$ is central, since $v_{k+1}=v_k/R_k$ and $v_{k-1}=v_kR_{k-1}$. The non-central terms contribute at most $2nC\sum_j\min(v_j,e^{-\varepsilon v_j})$, and since consecutive $v_j$ differ by factors $R_j\to\infty$, this is $o(1)$ as $k_0\to\infty$. If no $k$ is central, $D(x)\ge1-1/e-o(1)>0$. If $k$ is central, then $\log x\ge a_kR_{k-1}^{-1/2}=\tau(\ell_k\ell_{k-1})^{1/2}\ge\tau\ell_{k_0-1}$, so $1/x=o(1)$, and the central terms equal $P_{v_k}(\gamma_k\log x)-1$, so $D(x)\ge\eta-o(1)>0$ for almost every such $x$. So for $k_0$ large, $\Pi$ is non-decreasing, and $(\Pi,\exp^*(d\Pi))$ is a Beurling number system in the extended sense with zeta function $\zeta$.

*Step 2: continuation.* Integrating by parts, $|\hat\nu(z)|$ and $|\hat\lambda_j(z)|$ are at most $Ce^{\max(0,-\operatorname{Re}z)}/|z|$. On $\sigma\ge1/2$, $-\operatorname{Re}a_k(s-\rho_k)\le a_k/2$ and $-\operatorname{Re}a_k(s-1\mp ij\gamma_k)\le a_k/2$. If $|t-j\gamma_k|\ge\gamma_k/2$, the corresponding factor is $1+O(e^{\tau\ell_k/2}/(a_k\gamma_k))$. Now $\log\gamma_k/\ell_k=u_kf(u_k)\to\infty$ with $u_k=\log\gamma_k$, so these errors are summable. Hence the product converges locally uniformly on $\sigma\ge1/2$, and $\zeta$ is analytic there except for the simple pole at $1$. Each $\rho_k$ is a zero, because $G(0)=0$ and the other factors are analytic.

*Step 3: growth.* Let $A(t)=(2/\tau)\log(1/f(\log t))$ and $1/\psi(t)=A(t)f(\log t)$. For large $t$, $A$ is non-decreasing, $A\to\infty$, $Af(\log t)\to0$ and is non-increasing, so $\psi$ is non-decreasing and $\psi\ge1$. Let $\sigma\ge1-1/\psi(t)$. If $|t-j\gamma_k|\le\gamma_k/2$ for some $j\le n$, the factor at height $j\gamma_k$ has $|z|$ with $-\operatorname{Re}z\le a_k(1-\sigma)\le\tau\ell_k/\psi(t)$, so by Lemmas 2.1 and 2.2(a) it is at most $1+e^{\tau\ell_k/\psi(t)}$. Here $\ell_k/\psi(t)=A(t)f(\log t)/f(\log\gamma_k)=(1+o(1))A(t)$, since $\log t=\log\gamma_k+O(1)$. Every other factor, say with index $k'$, is $1+O(e^{\tau\ell_{k'}/2}/(a_{k'}\gamma_{k'}))$ by Step 2, and these errors are summable, so the product of all other factors is bounded uniformly in $t$. So at each $t$ at most one factor is large, and $\zeta(s)\ll e^{\varphi(t)}$ with $\varphi=(\tau+\delta)A$ for any fixed $\delta>0$. $\varphi$ is non-decreasing with $\varphi\to\infty$, and $e^\varphi\ge e^{\tau A}=f(\log t)^{-2}\ge\psi(t)$ for large $t$, which is Landau's condition $\psi\ll e^\varphi$.

*Step 4: conclusion.* Suppose (1.1) held with some $c>\tau+\delta$. At $t=\gamma_k$,

$$\frac{1}{\psi(2t+1)\varphi(2t+1)}=\frac{f(\log(2\gamma_k+1))}{\tau+\delta}=(1+o(1))\frac{f(\log\gamma_k)}{\tau+\delta},$$

so for large $k$ the region in (1.1) contains $\sigma\ge1-f(\log\gamma_k)$, and with it the zero $\rho_k$. This is a contradiction. So $c^*\le\tau+\delta$ for every $\delta>0$. ∎

*Remarks on the construction.* (i) The zeros of the factors $E_{\lambda_j}$ lie in $\operatorname{Re}z<0$, that is, to the left of the 1-line at heights near $j\gamma_k$. They are further zeros of $\zeta$; the proof does not need them. (ii) Factors at height $0$ are excluded: their zeros would accumulate at the pole. (iii) For $n=1$ the symbol is $1-2vH(v)e^{-\tau v}\cos\theta$, positive iff $2vH(v)e^{-\tau v}<1$; this is the condition behind $T(\nu)$, and Theorem 1 with $n=1$ is Corollary 2.

## 4. Examples by hand

### 4.1 One harmonic: $n=1$

For $n=1$ the symbol is $1-2r(v)\cos\theta$, and $P_v\ge\eta>0$ for almost every $v$ means $\sup_v2vH_\nu(v)e^{-\tau v}<1$. If $\tau>T(\nu)$, then $2vH_\nu(v)e^{-\tau v}\le e^{-(\tau-T(\nu))v}$, which is at most $e^{-(\tau-T(\nu))v_0}<1$ for $v\ge v_0$, for every $v_0>0$; for small $v$, Lemma 2.1(d) gives $2vH_\nu(v)\le Cv$. So the hypothesis of Theorem 1 holds for every $\tau>T(\nu)$, and $c^*\le T(\nu)$. This proves the first part of Corollary 2.

*Proof of the second part.* Let $\nu=2\cdot1_{[1/2,1]}$, the DMV density on $[1,2]$ rescaled to $[1/2,1]$. Then $\nu^{*m}$ is supported on $[m/2,m]$. Four ranges of $v$ cover all cases.
- On $(0,1/2)$, $H=0$.
- On $[1/2,1)$, only $m=1$ contributes, so $vH(v)=2v$ and $\log(2vH)/v=\log(4v)/v$. This is maximal at $v=e/4$, with value $4/e$.
- On $[1,3/2]$, $\nu^{*2}(v)=4(v-1)$ and $\nu^{*m}=0$ for $m\ge3$, so $2vH(v)=4v(v-1)\le3$. At $\tau=4/e$, $4v(v-1)e^{-\tau v}\le3e^{-\tau}<0.69$.
- For $v\ge3/2$, Lemma 2.1(c) gives $vH(v)\le\|w\|_\infty U([0,1])=2\cdot2$, since $U([0,1])=1+\nu([0,1])=2$. Then $2vH(v)e^{-\tau v}\le8e^{-3\tau/2}<0.89$.

Hence $T(\nu)=4/e$. ∎

*Scaling.* For a density $\nu$ on $[0,b]$, put $\nu_b(x)=b\nu(bx)$ on $[0,1]$. Then $H_{\nu_b}(v)=bH_\nu(bv)$, so $T(\nu_b)=bT(\nu)$. Broucke's case is $\nu=1_{[1,2]}$, $b=2$, at $\tau=1$, that is $\tau=2$ in our normalisation. There $\sup2vHe^{-2v}=2/e$, so his construction satisfies the positivity constraint with a factor $e/2$ to spare, and the scale can shrink by that factor.

*The uniform kernel.* For $\nu=1_{[0,1]}$, $\nu^{*m}(v)=v^{m-1}/(m-1)!$ on $[0,1]$, so $vH(v)=e^v-1$ there. The function $f(v)=v^{-1}\log(2(e^v-1))$ increases on $(0,1)$: $v^2f'(v)=g(v):=ve^v/(e^v-1)-\log(2(e^v-1))$, $g'(v)=-ve^v/(e^v-1)^2<0$, and $g(1)=e/(e-1)-\log(2(e-1))>0.34$. So $\sup_{(0,1)}f=\log(2(e-1))=1.2345$. For $v>1$, the bounds (R5) of Section 4.2 below give $2vH(v)e^{-1.2345v}<0.52$ on $(1,5/4]$, $<0.45$ on $[5/4,2]$ and $<0.18$ on $[2,\infty)$. Hence $T(1_{[0,1]})=\log(2(e-1))$.

The two examples show the trade-off.
- Mass far from $0$ avoids pile-up in the convolution powers. But the $m=1$ term alone then forces $2v\nu(v)\le e^{\tau v}$, which costs about $4/e$.
- Mass near $0$ is cheap for the $m=1$ term, since the cap $e^{\tau v}/(2v)$ is large there. But it piles up in $\nu^{*m}$: the uniform kernel has $vH(1-)=e-1$.

### 4.2 Two harmonics: $n=2$

The uniform kernel has its worst point at $v=1-$, where $r=(e-1)e^{-\tau}$. With $n=1$ this forces $r\le1/2$. A second harmonic with $c_2=1/4$ at that point allows $r$ up to $1/\sqrt2$, the extreme value for degree 2. The factor $\lambda_2=\kappa1_{[0,1]}$ with $1-e^{-\kappa}=1/4$ puts $c_2(1-)=1/4$, and the threshold drops from $\log(2(e-1))$ to $\log(\sqrt2(e-1))$.

*Proof of Corollary 3.* Apply Theorem 1 with $n=2$, $\nu=1_{[0,1)}$, $\lambda_2=\kappa1_{[0,1)}$, $\kappa=\log(4/3)$ (so $\|\lambda_2\|_1=\kappa<1$). Let $\tau_0=\log(\sqrt2(e-1))=0.88789\ldots$ and fix $\tau\in(\tau_0,0.89]$. Write $r(v)=vH(v)e^{-\tau v}$ and $s(v)=vK(v)$, so $P_v(\theta)=1-2r\cos\theta+2s\cos2\theta$. It suffices to show $\inf_{v>0,\theta}P_v(\theta)>0$; then $c^*\le\tau$, and $\tau\downarrow\tau_0$ gives the claim.

**Lemma 4.1 (degree-2 symbols).** Let $r\ge0$, $s\in\mathbb R$ and $p(\theta)=1-2r\cos\theta+2s\cos2\theta$.
(a) $\min p\ge1-2r-2|s|$.
(b) If $0<s\le1/6$, then $\min p=1-2r+2s$ when $r\ge4s$ and $\min p=1-2s-r^2/(4s)$ when $r<4s$. In particular $p>0$ iff $r<1/2+s$.
(c) If $1/6\le s<1/2$, then $p>0$ iff $r<\sqrt{g(s)}$, $g(s)=4s(1-2s)$, and then $\min p=(g(s)-r^2)/(4s)$.

*Proof.* With $x=\cos\theta$, $p=4sx^2-2rx+1-2s$ on $[-1,1]$. For $s>0$ the vertex is $x=r/(4s)$; if it lies in $[-1,1]$ the minimum is $1-2s-r^2/(4s)$, otherwise the minimum is at $x=1$. In (b), $r<4s$ and $r<1/2+s$ give $r^2<16s^2\le g(s)$ since $4s\le1-2s$, and $r\ge4s$ needs $r<1/2+s$. In (c), $\sqrt g\le4s$ since $1-2s\le4s$; if $r\ge4s$ then $1-2r+2s\le1-6s\le0$. ∎

**Ingredients.**
- (R1) On $(0,1)$, $\nu^{*m}(v)=v^{m-1}/(m-1)!$, so $vH(v)=\sum_mv^m/m!=e^v-1$.
- (R2) On $(0,1)$, $\lambda_2^{*m}(v)=\kappa^mv^{m-1}/(m-1)!$, so $s(v)=\sum_m(-1)^{m+1}(\kappa v)^m/m!=1-e^{-\kappa v}=1-(3/4)^v\in(0,1/4)$.
- (R3) For $v>1$, $\phi=vK$ satisfies $\phi(v)=-\kappa\int_{v-1}^v\phi$ (Lemma 2.2(c), $v\lambda_2=0$ there). $\phi$ is bounded, and $|\phi|<1/4$ on $(0,1)$. If $S=\sup_{(1,V)}|\phi|$, then $S\le\kappa\max(1/4,S)$, so $S\le\kappa/4$. Hence $|s(v)|\le\kappa/4<0.072$ for $v>1$.
- (R4) The renewal density $u=\sum_{m\ge1}\nu^{*m}$ satisfies $u=e^y$ on $(0,1)$ and $u(y)=\int_{y-1}^yu$ for $y>1$. On $(1,2)$ this gives $u'=u-e^{y-1}$ with $u(1+)=e-1$, so $u=e^{y-1}(e-y)$, whose maximum on $(1,2)$ is $e^{e-2}$ at $y=e-1$. For $y>2$, $u(y)$ is an average of $u$ over a window of length $1$ inside $(1,\infty)$; a first-exceedance argument shows $u\le e^{e-2}$ on $(1,\infty)$.
- (R5) For $v>1$, $vH(v)=(w*U)(v)=\int_{v-1}^v(v-y)u(y)\,dy$, with derivative $u(v)-u(v-1)$. On $(1,2)$ this is $e^{v-1}(e-1-v)$: $vH$ increases on $(1,e-1)$ and decreases on $(e-1,2)$. Explicitly $vH(1+)=e-2$, $vH(5/4)=e^{1/4}(e-5/4)-1<0.8854$, and $\max_{(1,2)}vH=vH(e-1)=e^{e-2}-1<1.0510$. For $v\ge2$, $vH(v)\le\frac12\sup_{(1,\infty)}u\le e^{e-2}/2<1.0255$.

On $(0,1)$, $r'(v)=e^{-\tau v}((1-\tau)e^v+\tau)>0$ and $r''(v)=e^{-\tau v}((1-\tau)^2e^v-\tau^2)<0$. All numerical bounds below use $\tau_0<\tau\le0.89$ and $\tau_0>0.8878$.

**Case A: $0<v\le1/2$.** $r\le r(1/2)\le(e^{1/2}-1)e^{-0.4439}<0.4162$ and $0<s\le1-\sqrt3/2<0.134$. By Lemma 4.1(b), $\min p\ge\min(1-2r,\,1-2s-r)>0.16$.

**Case B: $1/2\le v\le v_1:=\log(6/5)/\log(4/3)=0.63376$** (where $s=1/6$). $r\le r(v_1)<0.5041<4s(1/2)=2(2-\sqrt3)=0.5358\ldots$, so by Lemma 4.1(b), $\min p=1-2s-r^2/(4s)\ge2/3-0.5041^2/0.5358>0.19$.

**Case C: $v_1\le v<1$.** Put $\delta=1-v\in(0,1-v_1]$, and note $(4/3)^{1-v_1}=10/9$. Then $1/4-s=(3/4)((4/3)^\delta-1)\le(3/4)\kappa(10/9)\delta<0.2398\,\delta$, and $g(s)=1/2-8(1/4-s)^2\ge1/2-0.4601\,\delta^2$. Since $\sqrt{1/2-x}=2^{-1/2}\sqrt{1-2x}\ge2^{-1/2}(1-2x)$ for $0\le x\le1/2$, $\sqrt g\ge1/\sqrt2-0.6507\,\delta^2$. Since $r''<0$, $r(v)\le r(1-)-\delta\,r'(1)$, and $r'(1)=e^{-\tau}(e-\tau(e-1))\ge e^{-0.89}(e-0.89(e-1))>0.4882$. Also $r(1-)=(e-1)e^{-\tau}<(e-1)e^{-\tau_0}=1/\sqrt2$. Hence $\sqrt g-r\ge(1/\sqrt2-r(1-))+\delta(0.4882-0.6507\,\delta)>1/\sqrt2-r(1-)=:m_\tau>0$, because $0.6507(1-v_1)<0.239$. By Lemma 4.1(c), $\min p=(\sqrt g-r)(\sqrt g+r)/(4s)\ge(2/3)m_\tau$, using $\sqrt g\ge2/3$ for $s\ge1/6$ and $4s\le1$. This is the binding range: $m_\tau\to0$ as $\tau\downarrow\tau_0$.

**Case D: $v>1$.** By Lemma 4.1(a) and (R3), $\min p\ge1-2r-0.144$. On $(1,5/4]$, $r\le vH(5/4)e^{-\tau}<0.8854\cdot0.4116<0.3645$. On $[5/4,2]$, $r\le1.0510\,e^{-5\tau/4}<0.3465$. On $[2,\infty)$, $r\le1.0255\,e^{-2\tau}<0.1738$. So $\min p>1-0.729-0.144>0.12$.

So $\inf P\ge\min(0.12,(2/3)m_\tau)>0$, and $c^*\le\tau$ for every $\tau\in(\tau_0,0.89]$. ∎

For $\tau<\tau_0$, $r(1-)>1/\sqrt2$, and no degree-2 symbol with constant term $1$ has $|c_1|>1/\sqrt2$ (Lemma 4.1(b, c), or [3]); so $P_v$ takes negative values for $v$ near $1$, and $\tau_0$ is the exact threshold for this pair $(\nu,\lambda_2)$. A direct evaluation agrees. As $v\to1-$, $\min_\theta P_v(\theta)\to1/2-(e-1)^2e^{-2\tau}$, which is $2.1\cdot10^{-3}$ at $\tau=0.89$ and $-1.0\cdot10^{-3}$ at $\tau_0-10^{-3}$. On a grid of step $2\cdot10^{-4}$ in $v$, the minimum over all $v$ sits at the last node before $1$ in both cases.

## 5. The extremal problems

For each $n$ let $\tau_n$ be the infimum of the $\tau$ for which some data $(\nu,\lambda_2,\dots,\lambda_n)$ satisfy the hypothesis of Theorem 1. Then $c^*\le\tau_n$, and $\tau_n$ is non-increasing in $n$. We minimised $\tau$ numerically over piecewise-linear data. The search is heuristic; only the certificates of Section 6 enter the theorems. Appendix A records the failure modes of the optimisers and how we removed them.

### 5.1 $n=1$

Here $\tau_1=T^*:=\inf T(\nu)$ over bounded probability densities of bounded variation on $[0,1]$.

*Evaluation.* For a density given at the nodes $v_i=ih$, $H$ is computed by summing the convolution powers $\nu^{*m}/m$ via FFT on $[0,V_{\max}]$, with each power truncated to $[0,V_{\max}]$ before the next product, so that there is no wrap-around. The sum stops when the mass of $\nu^{*m}$ on $[0,V_{\max}]$ drops below $10^{-13}$. On the uniform kernel this gives $1.23439$ at $h=2.5\cdot10^{-4}$; the exact value is $1.23447$, and the error is $O(h)$ because the supremum sits at the jump $v=1$. An independent evaluation by a trapezoid discretisation of the renewal equation $u=\nu+\nu*u$ agrees to $3\cdot10^{-5}$ at equal $h$.

*Minimisation.* We minimise $\tau$ subject to $\tau v\ge\log(2vH(v))$ at every node $v\le0.3$ and at every eighth node up to $3$, over the logarithms of the knot values (SLSQP). The density is normalised exactly, capped at $40$, and each optimum is validated at $h/2$ and $h/4$.

*Results.* Validated values of $T$ for the best density in each class, at three grid steps $h$.

| class | $h$ | $T$ |
|---|---|---|
| 21 equal knots, Nelder-Mead/Powell | $10^{-3}$, $2.5\cdot10^{-4}$, $1.25\cdot10^{-4}$ | 0.87918, 0.87919, 0.87919 |
| 21 equal knots, SLSQP | $5\cdot10^{-4}$, $2.5\cdot10^{-4}$, $1.25\cdot10^{-4}$ | 0.86138, 0.86147, 0.86151 |
| 27 knots (spacing $\ge0.005$), cap 40 | $2.5\cdot10^{-4}$, $1.25\cdot10^{-4}$, $6.25\cdot10^{-5}$ | 0.85727, 0.85771, 0.85777 |
| 27 knots, cap 40, second start | same | 0.85869, 0.85897, 0.85893 |
| 27 knots, cap 80 | same | 0.85596, 0.85822, 0.86001 (not converged in $h$) |

The infimum over these classes is about $0.855$-$0.858$. The optimisers do not reach below $0.855$ by refining the class, and we do not claim that $T^*$ is near $0.855$. All optimisers put most of the mass near $0$: $\nu_{40}$ has 77% of its mass on $[0,0.05]$ and mean $0.070$. After the cap they decay like $x^{-p}$, with $p$ falling from about $1.5$ near $x=0.05$ to about $1$ near $x=1$, and they saturate the constraint $2vH(v)\le e^{Tv}$ on a set of length about $0.95$.

### 5.2 $n\ge2$

*Parametrisation.* $\nu$ is piecewise linear on the 27 knots of $\nu_{40}$ (Section 6.1), given by the logarithms of its knot values and normalised exactly, with the cap $\nu\le40$. Each $\lambda_j$ is piecewise linear on the same knots. For $n=2$ we took $\lambda_2\ge0$ (logarithms of knot values) with $\|\lambda_2\|_1\le0.95$, and imposed $r(v)\le R(c_2(v))$ at the nodes, where $R(s)$ is the largest admissible $r$ for a degree-2 symbol: $R(s)=1/2+s$ for $0\le s\le1/6$ and $R(s)=2\sqrt{s(1-2s)}$ for $1/6\le s<1/2$ (Lemma 4.1). For $n\ge3$ the $\lambda_j$ are signed (knot values in $[-5,5]$) with $\|\lambda_j\|_1\le0.95$ for $n=3$ and $\le0.99$ for $n=4$ and $6$, and we imposed $P_v(\theta)\ge m$ at 361 equally spaced $\theta$ in $[0,\pi]$. In both cases the constraints sit at every node $v\le0.3$ and at spacing $2\cdot10^{-3}$ up to $v=3$, $H$ and $K$ are evaluated by FFT as in Section 5.1 at $h=10^{-3}$, and SLSQP minimises $\tau$. Each degree starts from the optimum of the previous one with the new $\lambda_j=0$ ($n=6$ from $n=4$). An optimum found at $h=10^{-3}$ can fail the certificate at a finer grid, near small knots or near the jump at $v=1$; the final runs use a margin $m=5\cdot10^{-4}$ ($n=3,4$) and constraints on the one-sided limits at $v=1$ ($n=4,6$), see Appendix A. We did not run $n=5$.

*Results.* The table lists, for each $n$, the optimiser's $\tau$ at the sampled nodes, the certified $\tau$ (Section 6.2), the largest value of $r(v)$ and the bound $\cos(\pi/(n+2))$ on $|c_1|$ for a nonnegative symbol of degree $n$ [3].

| $n$ | optimiser $\tau$ | certified $\tau$ | $\max_vr(v)$ at the certified $\tau$ | $\cos(\pi/(n+2))$ |
|---|---|---|---|---|
| 1 | 0.8573-0.8590 (Section 5.1) | 0.8581 | 1/2 | 1/2 |
| 2 | 0.56060 | 0.5609 | 0.7069 | 0.7071 |
| 3 | 0.44783 (margin $5\cdot10^{-4}$) | 0.4485 | 0.8077 | 0.8090 |
| 4 | 0.42259 (margin $5\cdot10^{-4}$, constraint at $1+$) | 0.4227 | 0.8646 | 0.8660 |
| 6 | 0.41227 (limits at $1\pm$; sampled minimum $2.0\cdot10^{-4}$) | 0.4124 | 0.9138 | 0.9239 |

The optimisers push $r$ up to the extreme value of degree $n$ at their peak: $0.7069$ against $0.7071$ for $n=2$, $0.8077$ against $0.8090$ for $n=3$, and $0.8646$ against $0.8660$ for $n=4$. So up to $n=4$ the harmonics are used to their limit at the scale $v$ where $r$ is largest, and the remaining cost sits elsewhere. For $n=6$ the gap is larger ($0.9138$ against $0.9239$), and the gain over $n=4$ is small ($0.4124$ against $0.4227$). The kernels change with $n$. For $n=2$, $\nu$ vanishes on $[0,0.005]$, is about $1.7$ on $[0.01,0.1]$ and $0.37$ at $1$, with mean $0.39$, and $\lambda_2\ge0$ has mass $0.157$, mostly on $[0.5,1]$; $c_2$ reaches $0.2504$ near $v=0.9$, close to $s=1/4$, where $R$ attains its maximum $1/\sqrt2$. For $n=3$, $\nu$ has 38% of its mass on $[0,0.05]$ (mean $0.19$), $\lambda_2$ is mostly negative (mass $-0.46$, $\|\lambda_2\|_1=0.55$), $\lambda_3$ mostly positive ($\|\lambda_3\|_1=0.59$), and $c_2$ reaches $0.47$ at $v=1$.

## 6. Certificates

### 6.1 $n=1$: the certificate for $\nu_{40}$

$\nu_{40}$ is the piecewise-linear density with knots $0,0.005,0.01,0.02,0.03,0.04,0.05,0.075,0.1,0.15,\dots,1$ (step $0.05$ from $0.1$) and values listed in the supplement (nu40.json; $\nu_{40}(0)=\nu_{40}(0.005)=40$, $\nu_{40}(1)=0.0602$). We prove $T(\nu_{40})<0.8581$ as follows. Let $h$ divide $0.005$, so that all knots are nodes, and let $N_h=1/h$ be the number of cells in $[0,1]$.

(a) *Approximate renewal density.* Let $\tilde u$ be piecewise linear on the cells $[jh,(j+1)h]$, with one jump of size $-\nu(1-)$ at $v=1$ ($u=\nu+\nu*u$ inherits $\nu$'s jump there). Its node values solve the collocation equations $\tilde u(v_k-)=\nu(v_k-)+(\nu*\tilde u)(v_k)$, where the cell integrals of products of linear functions are evaluated exactly. Hence the residual $q=\tilde u-\nu-\nu*\tilde u$ vanishes at the nodes up to rounding (the computed node residuals are at most $2.2\cdot10^{-14}$; the rounding bound is added in the paragraph *Rounding* below).

(b) *Residual between nodes.* On a cell interior, $\tilde u-\nu$ is linear, so $q''=-(\nu*\tilde u)''$. With $(f*g)''=f(0)g'+g(0)f'+f'*g'$, where $f'$ and $g'$ include the jumps at $v=1$ as Dirac masses, we bound $|(\nu*\tilde u)''|$ cell by cell by explicit sums of slopes. This gives $|q|\le(h^2/8)M_j$ on cell $j$.

(c) *True renewal density.* $d=\tilde u-u$ satisfies $d=q+\nu*d$, so $d=q+u*q$ and $|d(v)|\le\max_{[0,v]}|q|\cdot U([0,v])$, with $U([0,v])\le\inf_se^{sv}/(1-\hat\nu(s))$.

(d) *$vH$.* By Lemma 2.1(b), $vH=v\nu+w*u\le\Phi+\max_{[0,v]}|d|\cdot\int_0^vw$, where $\Phi=v\nu+w*\tilde u$. $\Phi$ is computed exactly at the nodes (Simpson's rule is exact for the cubic integrands). Between nodes it exceeds its linear interpolant $L$ by at most $(h^2/8)\sup|\Phi''|$, which is bounded as in (b). Together with (c) this gives $\varepsilon_j$ with $vH\le L+\varepsilon_j$ on cell $j$. For $\int_0^vw$ we use the sum of $h\max_{\text{cell}}w$ over the cells in $[0,v]$, with the exact maximum of the quadratic $w=v\nu$ on each cell.

(e) *The check.* On each cell, $f=(\alpha+\beta v)e^{-\tau v}$ is bounded by the larger of its end values plus $(h^2/8)\max|f''|$, with $|f''|\le(\tau^2\max|\alpha+\beta v|+2\tau|\beta|)e^{-\tau v_j}$. (With the exact maximum, from the endpoints and the critical point, the largest cell value at $\tau=0.8581$ is $1.1\cdot10^{-9}$ smaller.) The check $2(L(v)+\varepsilon_j)e^{-\tau v}<1$ is verified for all cells up to $V_{\max}=6$. Beyond $V_{\max}$, Lemma 2.1(c) gives $2vH(v)e^{-\tau v}\le2\|w\|_\infty\inf_s(e^s/(1-\hat\nu(s)))\,e^{-6\tau}=0.19$.

| $h$ | certified $\tau$ | binding $v$ | bound for $\max\lvert u-\tilde u\rvert$ |
|---|---|---|---|
| $2.5\cdot10^{-4}$ | 0.863748 | 0.0165 | 0.55 |
| $1.25\cdot10^{-4}$ | 0.858672 | 0.0371 | 0.11 |
| $6.25\cdot10^{-5}$ | 0.858005 | 0.0371 | 0.024 |

*Rounding.* We run the check at $\tau=0.8581$ ($h=6.25\cdot10^{-5}$, $V_{\max}=6$). The largest cell value of $2(L+\varepsilon_j)e^{-\tau v}$ is $1-3.5\cdot10^{-6}$, and the tail value beyond $V_{\max}$ is $0.19$. Everything is computed in IEEE double precision with rounding to nearest, unit roundoff $u=2^{-53}$. The collocation solution $\tilde u$ needs no error analysis, because any node values define an admissible $\tilde u$; the certificate concerns the $\tilde u$ actually computed. For the other quantities we use that a computed sum or dot product of $K$ terms $a_k$ satisfies
$$\Bigl|\mathrm{fl}\Bigl(\sum_ka_k\Bigr)-\sum_ka_k\Bigr|\le\gamma_K\sum_k|a_k|,\qquad\gamma_K=\frac{Ku}{1-Ku},$$
in any order of summation [5, Secs. 3.1, 4.2].
- Two computed quantities are sums with mixed signs: the node residuals $\tilde u-\nu-\nu*\tilde u$, and the node values of $\Phi$. The script computes $\sum_k|a_k|$ alongside each (the same convolution applied to absolute values) and adds $\gamma_{N_h+8}\sum_k|a_k|$ to the residual and to $\varepsilon_j$; the extra $8$ covers the rounding of the cell weights and of the final subtractions. At $h=6.25\cdot10^{-5}$ these terms are at most $1.8\cdot10^{-10}$ and $2.1\cdot10^{-12}$.
- All other quantities (the second-derivative sums, $U([0,v])$, $\varepsilon_j$ and the cell values) are built from nonnegative numbers by sums of at most $N_h$ terms, products and quotients, so each stage has relative error below $\gamma_{2N_h}<4\cdot10^{-12}$. The script multiplies them by $1+10^{-9}$, and multiplies $\hat\nu(s)$ by $1+10^{-10}$ before forming $1-\hat\nu(s)$ in the bound for $U([0,v])$.
- The slope $\beta$ of $L$ on a cell enters only the curvature term of step (e), where $4u\max|\Phi|/h$ is added to $|\beta|$.
- We assume that exp, expm1 and cos are accurate to a few units in the last place, as in the standard libraries; IEEE 754 does not require this.

The density is normalised with a factor $1+10^{-13}$; since $H$ increases with $\nu$, this bounds $H$ for the exact probability density. With these terms included, the certified $\tau$ in the table moves by less than $10^{-6}$, and the largest cell value at $\tau=0.8581$ by $1.1\cdot10^{-9}$. So $T(\nu_{40})<0.8581$. We have not run an interval-arithmetic version.

### 6.2 $n=2,3,4$ and $6$

The data are listed in the supplement (cert_n2.json, cert_n3.json, cert_n4.json, cert_n6.json): $\nu$ and $\lambda_j$ piecewise linear on the 27 knots of $\nu_{40}$. We prove $\inf P>0$ at $\tau=0.5609$ ($n=2$), $\tau=0.4485$ ($n=3$), $\tau=0.4227$ ($n=4$) and $\tau=0.4124$ ($n=6$). Since $P$ is not monotone in $r$ once harmonics are present (lowering $r$ lowers $P$ near $\theta=\pi$), every bound below is two-sided. Let $V_{\max}=6$, and $h=2.5\cdot10^{-4}$ for $n=2,3$, $h=1.25\cdot10^{-4}$ for $n=4$ and $h=6.25\cdot10^{-5}$ for $n=6$.

(a) *The kernel $\nu$.* Steps (a)-(d) of Section 6.1 give, on each cell $[v_i,v_i+h]$, the node values of $\Phi=v\nu+w*\tilde u$ and a bound $\varepsilon_i$ with $|vH-\Phi_{\rm lin}|\le\varepsilon_i$, where $\Phi_{\rm lin}$ is the linear interpolant of $\Phi$ on the cell. The bounds in 6.1(c)-(d) are bounds on absolute values, so they hold in both directions.

(b) *The harmonics.* By Lemma 2.2(c), $\phi_j=vK_{\lambda_j}$ solves $\phi_j=v\lambda_j-\lambda_j*\phi_j$. Collocation as in 6.1(a) gives a piecewise-linear $\tilde\phi_j$ (with the jump of $v\lambda_j$ at $v=1$) whose residual $\varrho_j=\tilde\phi_j-v\lambda_j+\lambda_j*\tilde\phi_j$ vanishes at the nodes up to rounding. Between nodes, $|\varrho_j|\le(h^2/8)M_{j,i}$ on cell $i$, with $M_{j,i}$ the bound of 6.1(b) for $|(\lambda_j*\tilde\phi_j)''|$ plus $2|\lambda_j'|$ for the term $v\lambda_j$. The error satisfies $\tilde\phi_j-\phi_j=\varrho_j-\lambda_j*(\tilde\phi_j-\phi_j)$, so $|\tilde\phi_j-\phi_j|\le\sup|\varrho_j|/(1-\|\lambda_j\|_1)=:D_j$.

(c) *Chord bound in $v$.* On cell $i$, $r(v)=vH(v)e^{-\tau v}$ differs from the chord of its end values $r_L=\Phi(v_i)e^{-\tau v_i}$, $r_R=\Phi(v_i+h)e^{-\tau(v_i+h)}$ by at most
$$\varepsilon_{r,i}=\varepsilon_ie^{-\tau v_i}+\max(|\Phi(v_i)|,|\Phi(v_i+h)|)\,e^{-\tau v_i}\frac{(\tau h)^2}{8}+\frac{|\Delta\Phi|\,|\Delta e^{-\tau v}|}{4},$$
the three terms being the error of $\Phi_{\rm lin}$, the chord error of $e^{-\tau v}$, and the quadratic term of the product of two linear functions. $\tilde\phi_j$ is linear on the cell. So for each $\theta$, $P_v(\theta)$ is within $2(\varepsilon_{r,i}+\sum_jD_j)$ of a function linear in $v$ on the cell, and $\min_{\rm cell}P_v(\theta)\ge\min(P_L(\theta),P_R(\theta))-2(\varepsilon_{r,i}+\sum_jD_j)$.

(d) *Chord bound in $\theta$.* $P_L$ and $P_R$ are trigonometric polynomials with $|P''|\le2\sum_jj^2|c_j|$. We evaluate them at 1024 equally spaced $\theta$ in $[0,\pi]$ ($P$ is even) and subtract $(\Delta\theta)^2/8$ times this bound.

(e) *Far region.* For $v\ge V_{\max}$, Lemma 2.1(c) gives $2r(v)\le2\|w\|_\infty U([0,1])e^{-\tau V_{\max}}$. For $v>1$, $\phi_j(v)=-(\lambda_j*\phi_j)(v)$, so $|\phi_j(v)|\le\|\lambda_j\|_1\sup_{[v-1,v]}|\phi_j|$, and a first-exceedance argument gives $\sup_{v\ge V_{\max}-1}|\phi_j|\le\sup_{[V_{\max}-1,V_{\max}]}|\tilde\phi_j|+D_j$. We check $1-2r-2\sum_j|c_j|>0$ beyond $V_{\max}$.

| $n$ | $\tau$ | min of the cell bounds | at $v$ | far check | $\lVert\lambda_j\rVert_1$ | $D_j$ | control: $\tau$, min |
|---|---|---|---|---|---|---|---|
| 2 | 0.5609 | $8.83\cdot10^{-5}$ | 0.3248 | 0.637 | 0.157 | $7.2\cdot10^{-8}$ | 0.5600, $-7.5\cdot10^{-4}$ |
| 3 | 0.4485 | $8.82\cdot10^{-5}$ | 0.9818 | 0.165 | 0.548, 0.595 | $2.4\cdot10^{-5}$, $1.8\cdot10^{-5}$ | 0.4478, $-3.2\cdot10^{-4}$ |
| 4 | 0.4227 | $2.83\cdot10^{-4}$ | 0.9936 | 0.147 | 0.621, 0.990, 0.278 | $6.7\cdot10^{-6}$, $6.2\cdot10^{-5}$, $1.0\cdot10^{-6}$ | 0.4222, $-3.5\cdot10^{-4}$ |
| 6 | 0.4124 | $6.70\cdot10^{-5}$ | 0.3999 | 0.100 | 0.662, 0.990, 0.673, 0.283, 0.116 | $1.7\cdot10^{-6}$, $6.3\cdot10^{-6}$, $6.2\cdot10^{-7}$, $2.1\cdot10^{-7}$, $1.5\cdot10^{-7}$ | 0.4119, $-1.9\cdot10^{-4}$ |

In the control runs (last column), lowering $\tau$ by 0.1-0.2% makes the certified lower bound negative. This means only that the certificate, at this $h$, fails there. It does not show that $P_v$ takes negative values at those $\tau$, nor that the margins are close to optimal. For $n=4$, $\|\lambda_3\|_1=0.990$ multiplies the residual by $1/(1-0.990)\approx104$ in $D_3$. At $h=2.5\cdot10^{-4}$ this costs $5\cdot10^{-4}$ and the bound is $-2.8\cdot10^{-4}$, which is why we use $h=1.25\cdot10^{-4}$; at $h=6.25\cdot10^{-5}$ the bound is $4.0\cdot10^{-4}$. For $n=6$, again with $\|\lambda_3\|_1=0.990$, the bound is $9.7\cdot10^{-7}$ at $h=1.25\cdot10^{-4}$ and $6.70\cdot10^{-5}$ at $h=6.25\cdot10^{-5}$. For $n=2$ an independent FFT evaluation of $P$ at $\tau=0.5609$ gives the minimum $9.2\cdot10^{-5}$ at $v=0.3247$.

![Figure 1. The symbols of the certified examples: $\min_\theta P_v(\theta)$ at the nodes (solid) and the certified lower bound on each cell (dotted), for $n=2$ ($\tau=0.5609$, $h=2.5\cdot10^{-4}$), $n=4$ ($\tau=0.4227$, $h=1.25\cdot10^{-4}$) and $n=6$ ($\tau=0.4124$, $h=6.25\cdot10^{-5}$). Left: $0\le v\le3$; beyond $v=2$ the symbol is bounded away from $0$. The certified minima sit at $v=0.3248$, $0.9936$ and $0.3999$. Right: zoom at $v=1$, where $\nu$ and the $\lambda_j$ jump. In all three cases the symbol is smallest just below $v=1$ and rises steeply after it; for $n=6$ the last cell below $1$ has the node value $3.4\cdot10^{-4}$ and the certified bound $2.5\cdot10^{-4}$. Earlier candidates failed within a few $h$ of $v=1$ (Appendix A), which is why the optimiser constrains the one-sided limits there.](supplement/figure-1.png)

*Rounding.* The rounding terms of Section 6.1 are part of this certificate too. The node residuals of the collocation for $\nu$ and for each $\lambda_j$, the node values of $\Phi$ and the values $P_L(\theta)$, $P_R(\theta)$ are sums with mixed signs. For each of them the script adds $\gamma_K\sum_k|a_k|$, computed alongside, with $K=N_h+8$ for the convolutions. For $P$ it subtracts $16(n+4)u(1+2\sum_j|c_j|)$, which also covers cos to a few units in the last place, and a term for the gap of width below $2.5\cdot10^{-16}$ between the last grid point $\mathrm{fl}(\pi)$ and $\pi$. At the certified $\tau$ these terms are at most $2.9\cdot10^{-11}$ (residuals of $\nu$), $2.5\cdot10^{-12}$ ($\Phi$) and $1.3\cdot10^{-13}$ ($P$). Nonnegative quantities, $\|\lambda_j\|_1$ included, carry factors $1+10^{-9}$; the normalising integral of $\nu$ is summed with correct rounding (math.fsum); and the normalisation factor $1+10^{-13}$ of $\nu$ changes $vH$ on $[0,6]$ by less than $10^{-9}$, in either direction. Adding all these terms changes every entry of the table by less than $2\cdot10^{-10}$, against the margins $8.8\cdot10^{-5}$, $2.8\cdot10^{-4}$ and $6.7\cdot10^{-5}$. We have not run an interval-arithmetic version.

## 7. The Vinogradov-Korobov normalisation, and remarks

*Proof of Corollary 5.* Take $f(u)=c\,u^{-2/3}(\log u)^{-1/3}$, which is regularly varying of index $-2/3$, eventually decreasing and convex, with $uf(u)\to\infty$. Take the $n=6$ data of Theorem 4 with $\tau=0.4124$ and build $\zeta$ as in Section 3. Let $L=\log t$, $d=1-\sigma\in[0,1/2]$, and $|t-j\gamma_k|\le\gamma_k/2$ for some $k$ and $j\le6$. As in Step 3, whose factor bounds need only $\sigma\ge1/2$, $\log|\zeta(s)|\le\tau\ell_kd+O(1)=Kd+O(1)$ with $K=(1+o(1))\,\tau L^{2/3}(\log L)^{1/3}/c$, since $\ell_k=1/f(\log\gamma_k)$ and $\log t=\log\gamma_k+O(1)$. Away from all $j\gamma_k$, $\zeta\ll1$. The VK majorant is $\log A+BLd^{3/2}+\frac23\log L$. Now

$$\max_{d\ge0}\bigl(Kd-BLd^{3/2}\bigr)=\frac{4K^3}{27B^2L^2}=(1+o(1))\frac{4\tau^3\log L}{27B^2c^3},$$

attained at $d^{1/2}=2K/(3BL)$. This is at most $\frac23\log L+O(1)$ once $c>(2/9)^{1/3}\tau B^{-2/3}$. With $\tau=0.4124$, $(2/9)^{1/3}\cdot0.4124=0.24979$, so $c=0.250\,B^{-2/3}$ works. The zeros $\rho_k$ satisfy $1-\beta_k=f(\log\gamma_k)$. ∎

The same computation gives $0.520\,B^{-2/3}$ from the $n=1$ certificate and $(16/9)^{1/3}B^{-2/3}=1.211\,B^{-2/3}$ from Broucke's construction ($\tau=2$ in our normalisation).

*Remarks.*
1. *What the bound means for zeta.* No argument that uses only positivity, the pole and a growth majorant, Landau's included, can give a constant above $0.4124$ in the normalisation (1.1). Together with Broucke's shape-sharpness, the step "growth bound → zero-free region" has no shape to gain and a bounded constant to gain. In the VK setting the class ceiling $0.250\,B^{-2/3}$ is $4.4$ times the class floor $0.0570\,B^{-2/3}$ of [6]. Ford's proof also uses zero-density estimates, the functional equation and the finite order of $\zeta$, but [12] shows that its leading constant does not depend on them. So the factor $4.4$ is a gap inside the class: either the class constant is larger than what Heath-Brown's method gives, or there are examples closer to it than ours.
2. *Lower side.* $1/(8V)\approx0.0036$ is Landau's local argument (Landau's extremal problems are surveyed in [10]). The interval $[0.0036,0.4124]$ for $c^*$ is wide. For regular growth functions with $\limsup\log\psi/\varphi\le\kappa$, $0<\kappa\le1$, the best constant lies in $[0.0799,0.4124]$ [12, Corollary 2], [6, Remark 5.2]; the examples of Theorem 4 are regular [12, Section 7].
3. *Trigonometric polynomials on both sides.* Let $L_m$ be the best constant that Landau's argument gives with a nonnegative test polynomial of degree $m$ and the best local lemma. A degree-$n$ example has a positive prime measure, so every test polynomial applies to it, and $L_m\le c^*\le\tau_n$ for all $m$ and $n$. The upper bounds $\tau_1<0.8581$, $\tau_2<0.5609$, $\tau_3<0.4485$, $\tau_4<0.4227$, $\tau_6<0.4124$ (and the uncertified values in Section 5.2) decrease with $n$; we have no lower bound for $\tau_n$ other than $L_m$. Whether $\sup_mL_m=\inf_n\tau_n$ is open; a positive answer would determine $c^*$. At each scale $v$, $P_v$ is a nonnegative trigonometric polynomial with first coefficient $-r(v)$, and the optimisers drive $r(v)$ to the extreme value $\cos(\pi/(n+2))$ [3] (Section 5.2).
4. *Other factors.* Several factors at one height multiply their growth, and a factor $1+\hat\lambda$ with $\lambda$ on $[0,b]$ costs $b$ times as much growth. Factors at non-integer multiples of $\gamma$ give nothing: averaging the symbol over the phase shifts that fix $\cos j\theta$ for every integer $j$ (a finite average for rational multiples, a mean over a torus otherwise) deletes their terms and keeps $r$ and the $c_j$, and the result is the symbol of the same data without these factors. A signed $\nu$ with $H_\nu\ge0$ would also give a positive measure. The condition $\|\lambda_j\|_1<1$ is used only to make $E_j$ zero-free on $\operatorname{Re}z\ge0$ with an explicit series for $K$; the degree-4 and degree-6 optima sit at our bound $\|\lambda_3\|_1\le0.99$, so a weaker zero-free condition may lower $\tau_n$. With the bound raised to $3$ and zero-freeness of each $E_j$ checked numerically, a continuation of our $n=6$ optimiser from the certified data reaches $\tau\approx0.4102$ in floating point, while the same continuation with the bound $0.99$ stops at $0.4119$. We have not certified this. We have not explored the other changes.
5. *Discrete systems.* Broucke's discretisation [1, Sec. 5.6] loses a factor $\exp(O(\sqrt{\log t}))$ in the growth, so the construction does not bound the constant for discrete Beurling systems.

## Appendix A. Optimiser failure modes

*$n=1$.* The optimiser readily exploits discretisation error. Step densities with cell edges off the grid gave a spurious $T\approx0.81$ (the grid lost 1.4% of the mass, and $vH(6)=0.61$ instead of $1$); constraints sampled every $0.005$ let it place a spike between samples (validated $T=57$); and without a cap near $0$ it exploited the $O(h\cdot\max\nu)$ error of the evaluation (optima with knot values above $200$ validate $0.2$ higher at $h/2$). We therefore normalise exactly and check $vH(V_{\max})\to1$, constrain at every node near $0$, cap the density at $40$, and validate each optimum at $h/2$ and $h/4$.

*$n\ge2$.* An optimum found at $h=10^{-3}$ can fail the certificate at $h=2.5\cdot10^{-4}$: the degree-3 optimum ($\tau=0.4476$) failed by $2\cdot10^{-4}$ near $v=0.036$, independently of $\tau$, because the coarse grid misses fine structure of the harmonics next to the small knots. Rerunning the optimiser with the margin $m=5\cdot10^{-4}$ removed the failure at a cost of $2\cdot10^{-4}$ in $\tau$. For $n=4$ a second failure appeared. $\nu$ and the $\lambda_j$ are nonzero at the knot $1$, so $r$ and $c_j$ jump down at $v=1$, and $P$ has a dip of width a few $h$ just after $1$, between the sampled nodes $1.000$ and $1.002$ (for one candidate, $-4.6\cdot10^{-3}$ at $h=6.25\cdot10^{-5}$ while the sampled values were positive). We then added every node in $[0.9,1.1]$ and a constraint on the one-sided values at $1+$. For $n=6$ a candidate failed at $1-$ in the same way, so the final optimiser constrains both one-sided limits at $1$, extrapolated linearly from the nodes $1-2h$ and $1-h$. SLSQP iterates need not be feasible, so we certify a checkpoint whose sampled values are positive (for $n=6$, minimum $2.0\cdot10^{-4}$ at $v=0.400$).

## References

[1] F. Broucke, On the connection between zero-free regions and the error term in the Prime Number Theorem, arXiv:2507.13780 (2025).

[2] H. G. Diamond, H. L. Montgomery, U. M. A. Vorhauer, Beurling primes with large oscillation, Math. Ann. 334 (2006), 1-36.

[3] E. Egerváry, O. Szász, Einige Extremalprobleme im Bereiche der trigonometrischen Polynome, Math. Z. 27 (1928), 641-652.

[4] K. Ford, Zero-free regions for the Riemann zeta function, arXiv:1910.08205v5 (2025), corrected version of the paper in Number Theory for the Millennium II (2002). Theorem 1: under $|\zeta(\sigma+it)|\le A|t|^{B(1-\sigma)^{3/2}}\log^{2/3}|t|$, no zeros with $1-\beta\le0.05507\,B^{-2/3}(\log|t|)^{-2/3}(\log\log|t|)^{-1/3}$; the proof also uses zero-density bounds for $\zeta$.

[5] N. J. Higham, Accuracy and Stability of Numerical Algorithms, 2nd ed., SIAM, Philadelphia, 2002.

[6] span_of_dilates, A kernel for each frequency improves the constant in the Vinogradov-Korobov zero-free region, rStation paper riemann_hypothesis_98 (2026).

[7] E. Landau, Über die Wurzeln der Zetafunktion, Math. Z. 20 (1924), 98-104.

[8] M. J. Mossinghoff, T. S. Trudgian, Nonnegative trigonometric polynomials and a zero-free region for the Riemann zeta-function, J. Number Theory 157 (2015), 329-349.

[9] M. J. Mossinghoff, T. S. Trudgian, A. Yang, Explicit zero-free regions for the Riemann zeta-function, arXiv:2212.06867 (2022).

[10] Sz. Gy. Révész, On some extremal problems of Landau, Serdica Math. J. 33 (2007), 125-162.

[11] Sz. Gy. Révész, Oscillation of the remainder term in the prime number theorem of Beurling, "caused by a given ζ-zero", arXiv:2202.01837v3 (2022).

[12] span_of_dilates, The constant in Landau's zero-free region theorem is at least 0.078 for regular growth functions, rStation paper riemann_hypothesis_97 (2026).

[13] OpenAI, The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane $\Re s>7/8$, manuscript dated 30 September 2026, github.com/openai/math at revision 1581d4c, preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf.
