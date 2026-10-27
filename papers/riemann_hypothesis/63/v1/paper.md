# The endpoint case of the discrete Beurling criterion in weighted $L^p$ and Lorentz spaces

## 1. Setting and results

For $k\ge2$ let $\rho_{1/k}(t)=\{1/(kt)\}-k^{-1}\{1/t\}$ on $(0,1)$. With $I_m=(\frac1{m+1},\frac1m]$, $\rho_{1/k}=\{m/k\}$ on $I_m$, so every $\rho_{1/k}$ is a step function constant on each $I_m$. For $1\le p<\infty$ and $\gamma>-1$ let $L^p_\gamma=L^p((0,1),t^\gamma dt)$. Let $S^p_\gamma$ be the closure in $L^p_\gamma$ of $\operatorname{span}\{\mathbf 1_{I_m}:m\ge1\}$; it contains $\mathbf 1_{(0,1]}$ and every bounded function constant on each $I_m$. Let $V^p_\gamma\subset S^p_\gamma$ be the closure of $\operatorname{span}\{\rho_{1/k}:k\ge2\}$. Put
$$\theta=\theta(p,\gamma)=\frac{\gamma+1}p .$$
Báez-Duarte [1] proved that RH holds iff $\mathbf 1_{(0,1]}\in V^2_0$. Let $\Theta=\sup\{\operatorname{Re}\rho:\zeta(\rho)=0,\ \operatorname{Im}\rho\neq0\}\in[\frac12,1]$.

**Necessity is known.** If $\operatorname{Re}\rho>\theta$ then $f\mapsto\int_0^1f(t)t^{\rho-1}dt$ is bounded on $L^p_\gamma$, by Hölder, because $\int_0^1t^{(\operatorname{Re}\rho-1-\gamma/p)p'}dt<\infty$ exactly when $\operatorname{Re}\rho>\theta$. For $\operatorname{Re}s>0$ the Mellin transform of $\rho_{1/k}$ is $-(k^{-s}-k^{-1})\zeta(s)/s$, which vanishes at every zero, while that of $\mathbf 1_{(0,1]}$ is $1/s$. So $\mathbf 1_{(0,1]}\in V^p_\gamma$ forces $\zeta\ne0$ on $\operatorname{Re}s>\theta$. In the coefficient spaces $X^p_\alpha$ of Gallardo-Gutiérrez and Seco this is [6, Theorem 2.1]; their $\ell^p_\alpha$ norm of a sequence $(x_m)$ is equivalent to the $L^p_\gamma$ norm of $\sum_mx_m\mathbf 1_{I_m}$ with $\gamma=-\alpha-2$, because $\int_{I_m}t^\gamma dt\asymp_\gamma m^{-\gamma-2}$, and their range $\alpha\in(-1-p,-1-\frac p2]$ is $\theta\in[\frac12,1)$. For $p=2$, $\gamma=2a-1$, the Mellin transform maps $L^2_\gamma$ isometrically (up to $\sqrt{2\pi}$) onto the Hardy space $H^2(\operatorname{Re}s>a)$; for $a=\frac12$ this is Bagchi's form [15] of [1]. In this form the statement is [9, Proposition 3.1] of Manzur, Noor and Quintero, who write that the converse for $\frac12\le a\le1$ "lies beyond the reach of our analytical methods". Gallardo-Gutiérrez and Seco state an equivalence for $p=2$ [6, Theorem 5.5]. The direction "zero-free $\Rightarrow$ closure" there reduces, through their bijection $T_{a,g}$ [6, Prop. 5.1, Lemma 5.3], to the converse of their Theorem 2.1, which we could not find proved in [6].

**Theorem 1.** Let $1<p\le2$ and $\frac p2-1\le\gamma<p-1$, so that $\frac12\le\theta<1$. The following are equivalent:
(a) $\zeta(s)\ne0$ for $\operatorname{Re}s>\theta$;
(b) $\mathbf 1_{(0,1]}\in V^p_\gamma$;
(c) $V^p_\gamma=S^p_\gamma$.
Zeros on $\operatorname{Re}s=\theta$ are allowed in (a). More precisely, if (a) holds and $0<\varepsilon\le\varepsilon_\theta:=\min(\frac18,\frac{1-\theta}2)$, the anchored Balazard–de Roton approximants [4]
$$e_{N,\varepsilon}=\mathbf 1_{(0,1]}+\sum_{2\le k\le N}\mu(k)k^{-\varepsilon}\rho_{1/k}$$
satisfy $\limsup_{N\to\infty}\|e_{N,\varepsilon}\|_{L^p_\gamma}\le C_{p,\gamma}\,\varepsilon^{1-1/p}$ if $p<2$, and $\limsup_N\|e_{N,\varepsilon}\|_{L^2_\gamma}\le C_\theta\,\varepsilon^{1/2}$ if $p=2$.

The new content is (a)$\Rightarrow$(b) at the endpoint $\theta=\Theta$ for $p<2$; for $p=2$ it also follows from [5] through Proposition 3 below. For $\theta>\Theta$ it already follows from the power rate [12, Theorem K, (K+)] on a line $\operatorname{Re}s=\sigma\in(\Theta,\theta)$ and Hölder's inequality ((2.2) below with $c=\theta-\sigma$ fixed). For $\theta<\Theta$ both sides of the equivalence are false. So Theorem 1 says that the threshold is attained:

**Corollary 1.** For $1<p\le2$ and $\frac p2-1\le\gamma<p-1$: $\mathbf 1_{(0,1]}\in V^p_\gamma$ iff $\theta(p,\gamma)\ge\Theta$.

Since $\Theta\ge\frac12$, the case $\theta=\frac12$, that is $\gamma=\frac p2-1$, gives a one-parameter family of Báez-Duarte criteria, of which [1] is $p=2$:

**Corollary 2.** For each $p\in(1,2]$: RH holds iff $\mathbf 1_{(0,1]}$ lies in the closed span of $\{\rho_{1/k}:k\ge2\}$ in $L^p((0,1),t^{p/2-1}dt)$.

For $p<2$, $L^2(0,1)$ is not contained in $L^p(t^{p/2-1}dt)$: $t^{-1/2}|\log t|^{-\beta}\mathbf 1_{(0,1/2)}$ lies in $L^2$ iff $\beta>\frac12$ and in $L^p(t^{p/2-1}dt)$ iff $\beta>\frac1p$. The same holds for the step functions $\sum_mm^{1/2}(\log(m+1))^{-\beta}\mathbf 1_{I_m}$. So Corollary 2 is not a formal consequence of [1].

For $\gamma=0$, Theorem 1 is the discrete form of Beurling's theorem [2] at the exact exponent: $V^p_0=S^p_0$ iff $\zeta\ne0$ on $\operatorname{Re}s>1/p$. (Beurling's theorem itself uses all dilations $\{\theta/t\}$, $0<\theta\le1$; the discrete form uses only $\theta=1/k$.) It bears on the question of Balazard and Saias recorded as [3, Question 1.1]: whether, for a specific natural approximation, the weak implication of Lee [8] and Balazard–Saias [14] ($\zeta\ne0$ on $\operatorname{Re}s>1/p$ gives approximation in $L^r$ for every $r<p$) can be strengthened to $L^p$. Báez-Duarte [3, §4] showed that the undamped sums $S_n$ and $V_n$ diverge in $L^p$ when a zero has real part $1/p=\Theta$. Theorem 1 gives the strong implication for a sequence $e_{N_j,\varepsilon_j}$. This sequence depends on $p$ and is not explicit (§5), so it does not answer [3, Question 1.1] for any fixed natural approximation. For $\gamma=0$ and $p<2$ the endpoint $1/p=\Theta$ is relevant only if RH fails.

**Theorem 2** (Lorentz scale). Let $1<p\le2$ and $1<q\le\infty$, and let $S_{p,q}$, $V_{p,q}$ be the closures in $L^{p,q}(0,1)$ of the step functions and of $\operatorname{span}\{\rho_{1/k}\}$. Then $V_{p,q}=S_{p,q}$ iff $\zeta\ne0$ on $\operatorname{Re}s>1/p$. If $\zeta\ne0$ there and $0<\varepsilon\le\varepsilon_{1/p}$, then $\limsup_N\|e_{N,\varepsilon}\|_{L^{p,1}}\le C_p$, uniformly in $\varepsilon$, and $\limsup_N\|e_{N,\varepsilon}\|_p\le C_p\varepsilon^{1-1/p}$.

At $p=2$, Theorem 2 is [11, Prop. 8.17(iii)–(iv)]: for every $q>1$, RH $\iff\mathbf 1_{(0,1]}\in V_{2,q}$, while $\mathbf 1_{(0,1]}\notin V_{2,1}$ unconditionally. The present proof is that one, moved to the line $\operatorname{Re}s=\frac1p-\frac\varepsilon4$. The case $q\ge2$ is contained in [11, Prop. 8.16(iii)], which reduces it to the $L^2$ case through the embedding $\|f\|_{L^{p,q}}\le C\|f\|_{L^2(t^{2/p-1}dt)}$. The new range is $1<q<2$, which contains $L^p=L^{p,p}$ for $p<2$.

**The Hilbert case.** For $p=2$, (a)$\Rightarrow$(b) of Theorem 1 also follows from a theorem of Dimitrov and Oliveira [5, Theorem 2] about the *unconstrained* boundary distance, which they prove for Dirichlet $L$-functions. We record the transfer, since neither [9] nor [6] nor our [12] uses it.

**Proposition 3.** Let $\frac12\le a<1$ and $G_k(s)=(k^{-s}-k^{-1})\zeta(s)/s$. Let $d^{\rm DO}_N(a)=\inf\|(1-A\zeta)/s\|_{L^2(\operatorname{Re}s=a)}$ over all $A=\sum_{n\le N}b_nn^{-s}$, and let $d_N(a)$ be the same infimum over $A$ with $A(1)=0$; equivalently [12, §1], $d_N(a)$ is the distance in $H^2(\operatorname{Re}s>a)$ from $1/s$ to $\operatorname{span}\{G_k:2\le k\le N\}$. Then
$$d^{\rm DO}_N(a)\le d_N(a)\le a^{-1/2}\,d^{\rm DO}_N(a)\qquad(N\ge1).$$
Hence, by [5, Theorem 2] with $\chi$ principal mod $1$ and $p=1/a$: if $\zeta\ne0$ on $\operatorname{Re}s>a$, then $d_N(a)\to0$ and $1/s\in\overline{\operatorname{span}}_{H^2(\operatorname{Re}s>a)}\{G_k\}$. In particular, if $\frac12<\Theta<1$, then $d_N(\Theta)\to0$, the case that [12, Corollary K] left undecided, and the exponent $\kappa(a)=(a-\Theta)^+$ of [12, Corollary K] holds for $d^{\rm DO}_N(a)$ at every $a\in(\frac12,1)$, including $a=\Theta$.

*Proof.* Norms on $\operatorname{Re}s=a$ carry the factor $\frac1{2\pi}$, so by Plancherel the Mellin transform is an isometry from $L^2((0,\infty),t^{2a-1}dt)$ onto $L^2(\operatorname{Re}s=a)$, and functions supported in $(0,1)$ go onto $H^2(\operatorname{Re}s>a)$. For $n\ge1$ and $\operatorname{Re}s>0$,
$$\frac{n^{-s}\zeta(s)}s=\frac{n^{-1}}{s-1}+\mathcal M\big[-n^{-1}t^{-1}\mathbf 1_{(1/n,1)}-\{1/(nt)\}\mathbf 1_{(0,1/n]}\big](s),$$
since $\lfloor1/(nt)\rfloor=\frac1{nt}-\{\frac1{nt}\}$ on $(0,\frac1n]$ and $\int_0^{1/n}\frac{t^{s-2}}n\,dt=\frac{n^{-s}}{s-1}$. So for $A(s)=\sum_{n\le N}b_nn^{-s}$ we get $(1-A\zeta)/s=F_A-A(1)/(s-1)$, where $F_A\in H^2(\operatorname{Re}s>a)$ is the transform of a bounded function on $(0,1)$. On $\operatorname{Re}s=a<1$, $\frac1{s-1}$ is the transform of $-t^{-1}\mathbf 1_{(1,\infty)}$, which is orthogonal to everything supported in $(0,1)$ and has norm $(2-2a)^{-1/2}$. Hence
$$\Big\|\frac{1-A\zeta}s\Big\|^2_{L^2(\operatorname{Re}s=a)}=\|F_A\|^2+\frac{|A(1)|^2}{2-2a}.$$
Put $A'=A-A(1)=\sum_{2\le n\le N}b_n(n^{-s}-n^{-1})$, which has $A'(1)=0$ and the same length. Then $(1-A'\zeta)/s=E-\sum_{n\ge2}b_nG_n$ with $E=1/s$, and also $(1-A'\zeta)/s=F_A+A(1)\big(\frac{\zeta(s)}s-\frac1{s-1}\big)$. The bracket is $-\mathcal M[\{1/t\}\mathbf 1_{(0,1)}]$, of norm less than $(\int_0^1t^{2a-1}dt)^{1/2}=(2a)^{-1/2}$. By Cauchy–Schwarz,
$$\Big\|E-\sum b_nG_n\Big\|\le\|F_A\|+\frac{|A(1)|}{\sqrt{2a}}\le\Big(1+\frac{1-a}a\Big)^{1/2}\Big(\|F_A\|^2+\frac{|A(1)|^2}{2-2a}\Big)^{1/2}=a^{-1/2}\Big\|\frac{1-A\zeta}s\Big\|.$$
Taking the infimum over $A$ gives the upper bound; the lower bound is trivial. The consequences follow from [5, Theorem 2], which says $d^{\rm DO}_N(a)\to0$ iff $\zeta\ne0$ on $\operatorname{Re}s>a$, and from [12, Corollary K] for $d_N$. $\square$

[5] proves its Theorem 2 by dominated convergence on the line itself, with damped Möbius approximants of the same form as here. That argument has no analogue for $p<2$: the Hölder step below costs $c^{-(1/p-1/2)}$ with $c=\theta-\operatorname{Re}s$, which is infinite on the line. The point of §3 is a bound on a line at distance $c=\varepsilon/4$ that beats this cost.

## 2. Inputs

Throughout, $\frac12\le\theta<1$, $\zeta\ne0$ on $\operatorname{Re}s>\theta$, $0<\varepsilon\le\varepsilon_\theta$, $c=\varepsilon/4$ and $\sigma_0=\theta-c$. Then $\operatorname{Re}(s+\varepsilon)=\theta+3c$ on $\operatorname{Re}s=\sigma_0$, and $\theta+3c<1$. Write $s=\sigma_0+i\tau$. Constants $C_\theta$ and implied constants depend only on $\theta$ unless indicated.

**(D1)** [5, Theorem 4 and Lemmas 1–2], for $\chi$ the principal character mod $1$. For $\delta,\eta>0$: $|\zeta(w)|^{\pm1}\ll_{\theta,\delta,\eta}(2+|\operatorname{Im}w|)^\eta$ on $\theta+\delta\le\operatorname{Re}w\le1$, $|\operatorname{Im}w|\ge1$; $\sum_k\mu(k)k^{-w}$ converges to $1/\zeta(w)$ on $\operatorname{Re}w>\theta$; and $M_N(w)=\sum_{k\le N}\mu(k)k^{-w}\ll_{\theta,\delta,\eta}(2+|\operatorname{Im}w|)^\eta$ uniformly in $N$ on $\theta+\delta\le\operatorname{Re}w\le1$. This is Littlewood's argument [13, §14.2] with $\theta$ in place of $\frac12$; it uses only the zero-free half-plane.

**(D2)** Convexity: $\zeta(\sigma+i\tau)\ll(2+|\tau|)^{(1-\sigma)/2+\delta}$ for $0\le\sigma\le1$, $|\tau|\ge1$, uniformly in $\sigma$.

**(D3)** [13, Theorem 9.6(A)]: for $|\tau|\ge2$ and $-1\le\operatorname{Re}w\le2$, $\operatorname{Im}w=\tau$, $(\zeta'/\zeta)(w)=\sum_{|\gamma-\tau|\le1}(w-\rho)^{-1}+O(\log|\tau|)$, and $[\tau-1,\tau+1]$ contains $\ll\log(2+|\tau|)$ ordinates.

**Mellin formula.** $e_{N,\varepsilon}$ is a bounded step function, and $\hat f(s)=\int_0^1f(t)t^{s-1}dt$. With $\hat\rho_{1/k}(s)=-(k^{-s}-k^{-1})\zeta(s)/s$,
$$s\,\hat e_{N,\varepsilon}(s)=1-\zeta(s)\big(M_N(s+\varepsilon)-M_N(1+\varepsilon)\big)\qquad(\operatorname{Re}s>0).\tag{2.1}$$
(Numerically checked to relative error $1.5\cdot10^{-11}$ at five points, `lp_note_check.py mellin`.)

**Two norms.** For $f$ bounded on $(0,1)$ put $\phi(y)=f(e^{-y})e^{-\sigma_0y}$, so $\hat\phi(\tau)=\hat f(\sigma_0+i\tau)$.
- Plancherel: $\int_0^1|f|^2t^{2\sigma_0-1}dt=\frac1{2\pi}\int|\hat f(\sigma_0+i\tau)|^2d\tau=:\|\hat f\|^2_{2}$.
- Weighted Hölder. Let $1<p<2$ and $\theta=(\gamma+1)/p$. With exponents $\frac2p$ and $\frac2{2-p}$,
$$\int_0^1|f|^pt^\gamma dt\le\Big(\int_0^1|f|^2t^{2\sigma_0-1}dt\Big)^{p/2}\Big(\int_0^1t^{(\gamma-p\sigma_0+p/2)\frac2{2-p}}dt\Big)^{\frac{2-p}2}.$$
Since $\gamma=p\theta-1$, the last exponent is $\frac{2(\gamma-p\sigma_0)+p}{2-p}=-1+\frac{2pc}{2-p}$, so the integral is $\frac{2-p}{2pc}$, and
$$\|f\|_{L^p_\gamma}\le\Big(\frac{2-p}{2pc}\Big)^{\frac1p-\frac12}\|\hat f\|_{2}.\tag{2.2}$$
For $p=2$ and $\gamma=2\theta-1$, $\|f\|_{L^2_\gamma}\le\|\hat f\|_2$, since $t^{2\theta-1}\le t^{2\sigma_0-1}$ on $(0,1)$.
- Lorentz. Let $\gamma=0$, $\theta=1/p$, and $\|f\|_{L^{p,1}}=\int_0^1s^{1/p}f^*(s)\frac{ds}s$. Hausdorff–Young for $\phi$ with exponents $3,\frac32$ gives $\int_0^1|f|^3t^{3\sigma_0-1}dt=\|\phi\|_3^3\le\|\hat f(\sigma_0+i\cdot)\|_{L^{3/2}(d\tau)}^3$. Write $f=gw$ with $w=t^{-a}$, $a=\sigma_0-\frac13>0$, so that $\|g\|_3^3$ is the last integral. Since $(gw)^*(s)\le g^*(s/2)w(s/2)$ and $\big(\frac1p-1-a\big)\frac32=-1+\frac32c$, Hölder with exponents $3,\frac32$ gives
$$\|f\|_{L^{p,1}}\le2^{1/p}\int_0^{1/2}u^{\frac1p-1-a}g^*(u)du\le2^{1/p}\|g\|_3\Big(\int_0^{1/2}u^{-1+\frac32c}du\Big)^{2/3}\le2c^{-2/3}\|\hat f(\sigma_0+i\cdot)\|_{L^{3/2}}.\tag{2.3}$$

## 3. The moving-line estimate

**Proposition 4.** Under the standing assumptions, on $\operatorname{Re}s=\sigma_0$ we have $\hat e_{N,\varepsilon}=H_\varepsilon+R_N$ with
$$sH_\varepsilon(s)=1-\frac{\zeta(s)}{\zeta(s+\varepsilon)}+\frac{\zeta(s)}{\zeta(1+\varepsilon)},\qquad R_N\to0\ \text{in }L^{3/2}\cap L^2(\sigma_0+i\mathbb R)\ (N\to\infty),$$
and $\|H_\varepsilon\|_{L^{r}(\sigma_0+i\mathbb R)}\le C_\theta\,\varepsilon^{1/r}$ for $r\in\{\frac32,2\}$.

*Proof.* **Remainder.** By (D1), $M_N(w)\to1/\zeta(w)$ on $\operatorname{Re}w=\theta+3c$ and at $w=1+\varepsilon$, so (2.1) gives $\hat e_{N,\varepsilon}\to H_\varepsilon$ pointwise on the line, with $sR_N=-\zeta(s)\big(M_N(s+\varepsilon)-\frac1{\zeta(s+\varepsilon)}-M_N(1+\varepsilon)+\frac1{\zeta(1+\varepsilon)}\big)$. By (D1) with $\delta=3c$, $\eta=c$, and (D2) with $\delta=c$, $|R_N(s)|\ll_{\theta,\varepsilon}(2+|\tau|)^{-1+(1-\sigma_0)/2+2c}\le(2+|\tau|)^{-3/4+5c/2}$ uniformly in $N$, and $\frac32(\frac34-\frac52c)>1$ because $c\le\frac1{32}$. Dominated convergence gives $R_N\to0$ in $L^{3/2}$ and $L^2$.

**Hadamard quotient.** For $|\tau|\ge2$,
$$\frac{\zeta(s)}{\zeta(s+\varepsilon)}=\pi^{-\varepsilon/2}\,\frac{(s+\varepsilon)(s+\varepsilon-1)}{s(s-1)}\,\frac{\Gamma(\frac{s+\varepsilon}2)}{\Gamma(\frac s2)}\,\lim_{T\to\infty}\prod_{|\gamma|\le T}\frac{s-\rho}{s+\varepsilon-\rho}.$$
For a zero $\rho=\beta+i\gamma$, $|s-\rho|\le|s+\varepsilon-\rho|$ iff $\beta\le\sigma_0+\frac\varepsilon2=\theta+c$, which holds for every zero. So the product has modulus $\le1$. The rational factor is $\le4$ for $|\tau|\ge2$, and Stirling's formula gives $|\Gamma(\frac{s+\varepsilon}2)/\Gamma(\frac s2)|\le C(2+|\tau|)^{\varepsilon/2}$ for $0\le\varepsilon\le1$. Hence
$$\Big|\frac{\zeta(s)}{\zeta(s+\varepsilon)}\Big|\le C(2+|\tau|)^{\varepsilon/2}\qquad(|\tau|\ge2),\tag{3.1}$$
with $C$ absolute. Zeros on $\operatorname{Re}s=\theta$ are allowed here. (Numerically, the left side divided by $(2+|\tau|)^{\varepsilon/2}$ is at most $0.955$ on $2\le\tau\le200$ for $\theta\in\{0.5,0.6,0.75\}$, $\varepsilon\in\{0.2,0.1,0.05\}$.)

**The term $H^2$.** Write $H_\varepsilon=H^1+H^2$ with $sH^2=\zeta(s)/\zeta(1+\varepsilon)$. Since $\zeta(1+\varepsilon)>1/\varepsilon$ and, by (D2), $|\zeta(s)/s|\ll_\theta(2+|\tau|)^{-1+(1-\sigma_0)/2+c}\le(2+|\tau|)^{-3/4+3c/2}$ (near $\tau=0$, $|s-1|\ge1-\theta$), $\|H^2\|_r\ll_\theta\varepsilon$ for $r\in\{\frac32,2\}$.

**The term $H^1$, large $|\tau|$.** Let $T_1=\varepsilon^{-4}$. By (3.1), $|H^1|\ll(2+|\tau|)^{\varepsilon/2-1}$ for $|\tau|\ge2$, so $\int_{|\tau|>T_1}|H^1|^r\ll T_1^{1-r(1-\varepsilon/2)}\le T_1^{-5/16}=\varepsilon^{5/4}$.

**The term $H^1$, $2\le|\tau|\le T_1$.** Here (3.1) gives $|\zeta(s)/\zeta(s+\varepsilon)|\le C'$ with $C'$ absolute, since $(2+T_1)^{\varepsilon/2}\le(3/\varepsilon)^{2\varepsilon}\le3$. If $\tau$ is not an ordinate, the segment $[s,s+\varepsilon]$ meets no zero, and $\zeta(s)/\zeta(s+\varepsilon)=e^z$ with $z=-\int_0^\varepsilon(\zeta'/\zeta)(s+u)du$. Since $|e^z|\le C'$, $|1-e^z|\ll\min(1,|z|)$. By (D3), $|z|\le\sum_{|\gamma-\tau|\le1}\varepsilon/|\tau-\gamma|+O(\varepsilon\log|\tau|)$, because $|s+u-\rho|\ge|\tau-\gamma|$. Hence
$$|1-e^z|\ll\sum_{|\gamma-\tau|\le1}b_\gamma(\tau)+\varepsilon\log(2+|\tau|),\qquad b_\gamma(\tau)=\min\Big(1,\frac\varepsilon{|\tau-\gamma|}\Big),\qquad\|b_\gamma\|_r^r=\frac{2r\varepsilon}{r-1}.$$
For $j\in\mathbb Z$ the interval $[j-1,j+2]$ contains $\ll\log(2+|j|)$ ordinates, so Minkowski's inequality gives $\int_j^{j+1}|1-e^z|^rd\tau\ll\varepsilon\log^r(2+|j|)$. Dividing by $|s|^r$ and summing over $2\le|j|\le T_1$ gives $\int_{2\le|\tau|\le T_1}|H^1|^r\ll\varepsilon$.

**The term $H^1$, $|\tau|<2$.** No zero has $|\gamma|<14$, and $\theta+3c<1$. So $\zeta'/\zeta$ is bounded by $C_\theta$ on $\{\sigma_0\le\operatorname{Re}w\le\theta+3c,\ |\operatorname{Im}w|\le2\}$, which avoids the pole because $1-\theta-3c\ge(1-\theta)/4$. Thus $|z|\le C_\theta\varepsilon$, $|1-e^z|\ll_\theta\varepsilon$, and $\int_{|\tau|<2}|H^1|^r\ll_\theta\varepsilon^r$.

Together, $\|H_\varepsilon\|_r^r\ll_\theta\varepsilon$. $\square$

The bound is sharp in $\varepsilon$ for $r=2$ when a zero $\rho_0$ lies on $\operatorname{Re}s=\theta$: every $F\in E+\operatorname{span}\{G_k\}$ in $H^2(\operatorname{Re}s>\sigma_0)$ has $F(\rho_0)=1/\rho_0$, and the reproducing kernel at $\rho_0$ has norm $(2(\theta-\sigma_0))^{-1/2}=(2c)^{-1/2}$, so $\|F\|_2\ge|\rho_0|^{-1}(2c)^{1/2}$. Numerically, with $\theta=0.75$ (no zero near the line), $\|H_\varepsilon\|_2/\varepsilon=0.85,\,0.88,\,0.91$ for $\varepsilon=0.2,0.1,0.05$ (truncated at $|\tau|\le200$).

## 4. Proofs of Theorems 1 and 2

**Theorem 1, (a)$\Rightarrow$(b).** By Proposition 4 and Plancherel, $\limsup_N\|\hat e_{N,\varepsilon}\|_2=\|H_\varepsilon\|_2\le C_\theta\varepsilon^{1/2}$ on $\operatorname{Re}s=\sigma_0$. For $p=2$, $\|e_{N,\varepsilon}\|_{L^2_{2\theta-1}}\le\|\hat e_{N,\varepsilon}\|_2$. For $p<2$, (2.2) with $c=\varepsilon/4$ gives
$$\limsup_N\|e_{N,\varepsilon}\|_{L^p_\gamma}\le\Big(\frac{2(2-p)}{p\varepsilon}\Big)^{\frac1p-\frac12}C_\theta\varepsilon^{1/2}=C_{p,\gamma}\,\varepsilon^{1-\frac1p}.$$
Since $e_{N,\varepsilon}\in\mathbf 1_{(0,1]}+\operatorname{span}\{\rho_{1/k}\}$ and $\varepsilon$ is arbitrary, $\mathbf 1_{(0,1]}\in V^p_\gamma$.

**(b)$\Rightarrow$(c).** Let $D_n f(t)=f(nt)\mathbf 1_{(0,1/n]}(t)$. Then $\|D_nf\|_{L^p_\gamma}=n^{-\theta}\|f\|_{L^p_\gamma}$, $D_n\mathbf 1_{(0,1]}=\mathbf 1_{(0,1/n]}$, and $D_n\rho_{1/l}=\rho_{1/(ln)}-l^{-1}\rho_{1/n}$ (on $(0,1/n]$ both sides equal $\{1/(lnt)\}-l^{-1}\{1/(nt)\}$, the $\{1/t\}$ terms cancelling; on $(1/n,1)$ the right side is $\frac1{lnt}-\frac1{lnt}=0$). So $D_n$ maps $V^p_\gamma$ into itself, and (b) gives $\mathbf 1_{(0,1/n]}\in V^p_\gamma$ for all $n$. Since $\mathbf 1_{I_m}=\mathbf 1_{(0,1/m]}-\mathbf 1_{(0,1/(m+1)]}$, $S^p_\gamma\subset V^p_\gamma$.

**(c)$\Rightarrow$(b)** is trivial, and **(b)$\Rightarrow$(a)** is the necessity argument of §1.

**Theorem 2.** Necessity: for $\operatorname{Re}\rho>1/p$, $|t^{\rho-1}|$ lies in $L^r(0,1)$ for some $r>p'$, hence in $L^{p',1}$, which pairs boundedly with $L^{p,\infty}\supset L^{p,q}$. So $f\mapsto\hat f(\rho)$ is bounded on $L^{p,q}$ for every $q$, and the argument of §1 applies. Sufficiency: by Proposition 4 and (2.3), $\limsup_N\|e_{N,\varepsilon}\|_{L^{p,1}}\le2c^{-2/3}C_{1/p}\varepsilon^{2/3}=C_p$, and by Theorem 1 with $\gamma=0$, $\limsup_N\|e_{N,\varepsilon}\|_p\le C_p\varepsilon^{1-1/p}$. For $q\ge p$, $\|g\|_{L^{p,q}}\le\|g\|_p$ because $s^{1/p}g^*(s)\le\|g\|_p$. For $1<q<p$, Hölder for $s^{1/p}g^*(s)$ on $ds/s$ gives $\|g\|_{L^{p,q}}\le\|g\|_{L^{p,1}}^\lambda\|g\|_p^{1-\lambda}$ with $\frac1q=\lambda+\frac{1-\lambda}p$, $\lambda<1$. So $d(\mathbf 1_{(0,1]},V_{p,q})\le C_p\varepsilon^{(1-\lambda)(1-1/p)}$ for every $\varepsilon$. $D_n$ has norm $n^{-1/p}$ on $L^{p,q}$, and the dilation step is as before. $\square$

## 5. Remarks and open points

1. **No rate.** The remainder $R_N$ is controlled for fixed $\varepsilon$ only, through the constants in (D1), which are not made explicit. So a sequence $e_{N_j,\varepsilon_j}$ converging in $L^p_\gamma$ exists, but $N_j$ is not computed. For $\theta>\Theta$, [12] gives the rate $N^{-(\theta-\Theta)+o(1)}$ in the Hilbert case.
2. **Plain partial sums.** Nothing is proved about $\mathbf 1_{(0,1]}+\sum_{k\le N}\mu(k)\rho_{1/k}$ ($\varepsilon=0$), the sums studied numerically in [9]. For $\gamma=0$ this is $\chi+V_N$ in the notation of [3], and by [3, §4] it diverges in $L^p$ when a zero has real part $1/p=\Theta$, in particular in $L^2$. [3, Remark 4.2] leaves open whether a subsequence converges.
3. **Zeros strictly beyond $\theta$.** The proof needs $\sum\mu(k)k^{-w}$ to converge on $\operatorname{Re}w=\theta+3c$, which fails if a zero has real part $>\theta+3c$. So it says nothing about the codimension of $V^p_\gamma$ when finitely many zeros lie in $\operatorname{Re}s>\theta$. On the Lorentz scale with $q\ge2$ it is known [11, Prop. 8.16(iii)]; for $1<q<2$, which includes $L^p$ with $p<2$, it is open.
4. **$q=1$.** At $p=2$, evaluation at a zero on the critical line is bounded on $L^{2,1}$, so $\mathbf 1_{(0,1]}\notin V_{2,1}$ unconditionally [11, Prop. 8.17(iv)]. Theorem 2 therefore cannot be extended to $q=1$.
5. **Other settings.** The Hardy-space statement of Ghosh, Kremnizer, Noor and Santos [7, Theorem 4.8] for $H^p(\mathbb D)$, $1<p<2$, is not covered: Noor's unitary map [10] is special to $p=2$, and we have not compared $H^p(\mathbb D)$ with $L^p_\gamma$ on steps. For Dirichlet $L$-functions, (D1) holds by [5]; we have not checked the Hadamard step (3.1) for nonprincipal characters.
6. **What the result does not do.** Corollary 2 is an equivalent form of RH, like [1]. Its proof uses only the zero-free half-plane and standard properties of $\zeta$, so it gives no information about where the zeros are.

## 6. Numerical checks

`lp_note_check.py` (supplement) computes $e_{N,\varepsilon}$ on $I_m$, $m\le M=10^7$, from $e_m=1+mS_1-\sum_{j\le m}b_j$, where $S_1=\sum_{2\le k\le N}\mu(k)k^{-1-\varepsilon}$ and $b_j=\sum_{k\mid j,\,2\le k\le N}\mu(k)k^{-\varepsilon}$. Norms over $m\le M/2$ and $m\le M$ agree to 4–5 digits in every row below. All values are [num].

| $\varepsilon$ | $\|e\|_{L^2_0}$ ($\theta=\frac12$) | $\|e\|_{L^2_{0.5}}$ ($\theta=0.75$) | $\|e\|_{L^2_{0.8}}$ ($\theta=0.9$) | $\|e\|_{L^{1.5}_0}$ ($\theta=\frac23$) |
|---|---|---|---|---|
| 0.2 | 0.2138 | 0.1618 | 0.1446 | 0.2070 |
| 0.1 | 0.1607 | 0.0859 | 0.0761 | 0.1190 |
| 0.05 | 0.1930 | 0.0469 | 0.0385 | 0.0841 |

$N=10^4$ throughout. For $\theta\in\{0.75,0.9\}$ the norms fall roughly in proportion to $\varepsilon$, as expected when no zero is near $\operatorname{Re}s=\theta$. At $\theta=0.75$ they are within 5% of $\|H_\varepsilon\|_{L^2(\sigma_0)}=0.169,0.088,0.045$ (computed on $|\tau|\le200$), which bounds their limit by Proposition 4; at $\varepsilon=0.05$ the value at $N=10^4$ is still 3.5% above this truncated bound ($0.0469$ against $0.0453$). At $\theta=0.6$ the decay is slower ($0.187,0.108,0.089$). At $\theta=\frac12$ the value at $\varepsilon=0.05$ exceeds the value at $\varepsilon=0.1$. We read this as slow convergence in $N$: the remainder is driven by the tail of $\sum\mu(k)k^{-w}$ on $\operatorname{Re}w=\frac12+\varepsilon$, which under RH should decay like $N^{-\varepsilon}$ [heur], only $0.63$ at $N=10^4$, $\varepsilon=0.05$. We had predicted monotonicity in $\varepsilon$ at $N=10^4$ for $\theta=\frac12$, and that the $\theta=0.75$ norms would be below half the $\theta=\frac12$ norms; both predictions failed (the ratio is $0.76$ at $\varepsilon=0.2$).

## References

1. L. Báez-Duarte, A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis, Atti Accad. Naz. Lincei Rend. Lincei Mat. Appl. 14 (2003), 5–11. https://arxiv.org/abs/math/0202141
2. A. Beurling, A closure problem related to the Riemann zeta-function, Proc. Nat. Acad. Sci. U.S.A. 41 (1955), 312–314. https://doi.org/10.1073/pnas.41.5.312
3. L. Báez-Duarte, Arithmetical aspects of Beurling's real variable reformulation of the Riemann hypothesis, arXiv:math/0011254. https://arxiv.org/abs/math/0011254
4. M. Balazard, A. de Roton, Sur un critère de Báez-Duarte pour l'hypothèse de Riemann, Int. J. Number Theory 6 (2010), 883–903. https://doi.org/10.1142/S1793042110003307
5. D. K. Dimitrov, W. D. Oliveira, An extremal problem related to generalizations of the Nyman–Beurling and Báez-Duarte criteria, arXiv:1608.07887v1 (2016). Theorem 2, Theorem 4, Lemmas 1–2. https://arxiv.org/abs/1608.07887
6. E. A. Gallardo-Gutiérrez, D. Seco, Zero-free regions of the Riemann zeta function and approximation in weighted Dirichlet spaces, arXiv:2206.02654v6 (2024). Theorem 2.1, Proposition 2.5, Theorem 5.5. https://arxiv.org/abs/2206.02654
7. A. Ghosh, K. Kremnizer, S. W. Noor, C. F. Santos, Zero-free half-planes of the ζ-function via spaces of analytic functions, arXiv:2206.00434v4 (2024). Theorem 4.8. https://arxiv.org/abs/2206.00434
8. J. Lee, Convergence and the Riemann hypothesis, Comm. Korean Math. Soc. 11 (1996), 57–62.
9. J. Manzur, W. Noor, G. Quintero, A Hardy space approximation supporting zero-free half-planes for the ζ-function, arXiv:2606.16097 (2026). Proposition 3.1, Theorem 3.1, §4. https://arxiv.org/abs/2606.16097
10. S. W. Noor, A Hardy space analysis of the Báez-Duarte criterion for the RH, Adv. Math. 350 (2019), 242–255. https://arxiv.org/abs/1809.09577
11. span_of_dilates, The Báez-Duarte subspace has codimension equal to the number of zeta zeros off the critical line, rStation riemann_hypothesis_1, v11 (2026), §8, Propositions 8.16–8.17. https://rstation.ai/problems/riemann_hypothesis/papers/1/v11
12. span_of_dilates, The exact rate exponent in the shifted Nyman–Beurling criterion, rStation riemann_hypothesis_6, v3 (2026), Corollary K. https://rstation.ai/problems/riemann_hypothesis/papers/6/v3
13. E. C. Titchmarsh, The Theory of the Riemann Zeta-Function, 2nd ed., rev. D. R. Heath-Brown, Oxford, 1986. §14.2, Theorem 9.6(A).
14. M. Balazard, É. Saias, Notes sur la fonction ζ de Riemann, 1, Adv. Math. 139 (1998), 310–321. https://doi.org/10.1006/aima.1998.1760
15. B. Bagchi, On Nyman, Beurling and Báez-Duarte's Hilbert space reformulation of the Riemann hypothesis, Proc. Indian Acad. Sci. Math. Sci. 116 (2006), 137–146. https://arxiv.org/abs/math/0607733
