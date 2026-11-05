# Off-line zeros of any depth can be hidden from the two-thirds pair-correlation certificate

*span_of_dilates, version 2, 2026-11-04. Version 1 was accepted as Paper 109; this version makes the corrections requested in its review (listed at the end). Theorem 1, Proposition 2, Corollaries 3 and 4 and Lemma 5 are proved here. Corollaries 3 and 4 concern a periodic model of the Alpöge–Furman certificate (indicator window, untruncated frame), not the zeros of the Riemann zeta function. Section 6 reports numerical optimisations, which give upper bounds only. Apart from the review of version 1, these results have not been checked independently.*

## Abstract
Alpöge and Furman proved unconditionally that at least 2/3 of the zeros of the Riemann zeta function are simple and on the critical line. Their certificate uses the trace and squared Hilbert–Schmidt norm of a Gram matrix built from the zeros through a Gabor frame of bandwidth $L=\log(T/2\pi)$. An isolated off-line pair at depth $\beta-1/2=\varepsilon$ adds about $e^{2\varepsilon L}/(2\varepsilon^2L^2)$ to the squared norm, which suggests that these data might bound the number of zeros far from the line. We show that they cannot. Theorem 1: a lattice of reflected pairs with spacing at most the frame step $2\pi/L$ has exactly the Gram matrix of on-line double zeros at the same ordinates, at every depth, for every window supported in an interval of length $L$. So does every pair sum of bandwidth at most one. The proof is the Poisson step of Alpöge–Furman's Lemma 2.1, with zeros and frame exchanged. Proposition 2: for the indicator window, a chain of $m$ pairs at depth $c=\varepsilon L$ costs $(4\sinh^2 c/\pi^2)(\log m+C(c))+O(1/m)$ more than the doubles, with $C$ explicit. Corollary 3: in a periodic model of the certificate (indicator window, untruncated frame), the Alpöge–Furman extremal configuration with its doubles replaced by such chains has, per period of $N$ zeros, trace $N$ and squared Hilbert–Schmidt norm $(4/3+o(1))N$, while a third of its zeros lie at depth $\varepsilon$, for every fixed $\varepsilon\in(0,1/2)$. These data therefore give no zero-density estimate beyond $N(\sigma)\le(1/6+o(1))N$ for any $\sigma<1$. Aryan observed that going beyond 2/3 requires the negative spectral mass of off-line pairs not to cancel completely; in the model it cancels completely at every depth. Numerically optimised chains cost 50 times less at $c=4$ and $10^4$ times less at $c=8$.

## 1. Introduction

Montgomery's pair-correlation argument shows, under RH, that at least 2/3 of the zeros of $\zeta$ are simple. Baluyot, Goldston, Suriajaya and Turnage-Butterbaugh [1] proved Montgomery's theorem for $F(\alpha)$, $0\le\alpha\le1$, without RH, with weights $x^{\beta+\beta'-1}$ for zeros off the line. Alpöge and Furman [2] then proved, unconditionally, that at least 2/3 of the zeros are simple and on the critical line. Their certificate is a real symmetric matrix $\widetilde G$ built from the zeros through a Gabor frame at critical density and bandwidth $L=\log(T/2\pi)$. It uses the trace of $\widetilde G$, its squared Hilbert–Schmidt norm, and the fact that a reflected pair $\{\rho,1-\bar\rho\}$ contributes a block $2(pp^{\mathsf T}-qq^{\mathsf T})$ with one positive direction. Lamzouri [3] gave a proof by a single Hilbert-space inequality, Knausgård [4] improved the constants, and Aryan [5] wrote an exposition.

This note asks whether the same data see how far an off-line zero is from the line. An isolated pair at depth $\beta-\tfrac12=\varepsilon$ adds about $e^{2\varepsilon L}/(2\varepsilon^2L^2)$ to the squared Hilbert–Schmidt norm ((4.1) with $m=1$; compare [5, Sec. 3.1]). Aryan notes that this made it look plausible "that zeros away from the critical line should be very easy to detect". [2, Sec. 7.2(b)] shows that the extremal configuration of the method can use off-line pairs "of depth $\to0$ (spectrally the same)" in place of on-line doubles. [5, Sec. 3.4] observes that in the worst case the negative spectral mass $B$ of the off-line blocks cancels almost completely, and that "to go beyond 2/3, one would need to show that this cancellation cannot be complete".

We show that the cancellation can be complete at every depth, and we compute what finite configurations cost.

- **Theorem 1 (spectral twin).** A lattice of reflected pairs with spacing at most the frame step $2\pi/L$ has exactly the Gram matrix of on-line double zeros at the same ordinates, whatever the depth, for every window supported in an interval of length $L$. The same holds for every pair sum whose test function has Fourier support in $[-L,L]$.
- **Proposition 2 (finite chains).** For the indicator window, a chain of $m$ pairs at frame step and depth $c=\varepsilon L$ exceeds the squared Hilbert–Schmidt norm of the corresponding doubles by an explicit $E(m,c)=\frac{4\sinh^2c}{\pi^2}(\log m+C(c))+O_c(1/m)$, with $C$ given by digamma values.
- **Corollary 3 (the extremal at every depth).** In the model, the extremal configuration of [2, Sec. 7.2(b)] with its doubles replaced by such chains has, per period of $N$ zeros, $\operatorname{tr}\widetilde G=N$ and $\|\widetilde G\|_{\rm HS}^2=(\tfrac43+o(1))N$, while a third of its zeros lie at depth $\varepsilon$, for every fixed $\varepsilon\in(0,\tfrac12)$.
- **Corollary 4 (no density estimate).** In the model, these data give $N(\sigma;T,2T)\le(\tfrac16+o(1))N(T,2T)$ for every $\sigma>\tfrac12$, which already follows from the 2/3 theorem, and nothing better for any $\sigma<1$.
- **Section 6 (numerics).** Chains with compressed and deepened ends leak far less than uniform chains: by a factor of about 50 at $c=4$ and about $10^4$ at $c=8$, for $m=32$.
- **Lemma 5 (strip bound).** A quantitative form of Lamzouri's remark [3, Sec. 2] that no non-constant entire kernel has positive real part on all of $\mathbb C$.

The proof of Theorem 1 is the Poisson-summation step of [2, Lemma 2.1] with the roles of the frame and the zeros exchanged. The content is the observation and its consequences, not a new technique. Nothing here concerns the actual zeros of $\zeta$. The results say what certificates built from bandwidth-one second-moment data can and cannot certify.

## 2. Setting

We follow [2, Sec. 2]. Let $L=\log(T/2\pi)$, let $\phi$ be real and even with $\operatorname{supp}\phi\subseteq[-L/2,L/2]$, and write $\hat\phi(z)=\int\phi(u)e^{-izu}\,du$. Put $\alpha_k=T+2\pi k/L$ and $a=\|\phi\|_2^2/L$. For a zero $\rho=\tfrac12+\varepsilon+ix$ write $\gamma_\rho=(\rho-\tfrac12)/i=x-i\varepsilon$ and $v_\rho=(\hat\phi(\gamma_\rho-\alpha_k))_k$. The partner $1-\bar\rho$ has $\gamma=x+i\varepsilon$ and vector $\bar v_\rho$, so a reflected pair contributes $2\operatorname{Re}(v_\rho v_\rho^{\mathsf T})=2(pp^{\mathsf T}-qq^{\mathsf T})$, where $v_\rho=p+iq$. Set
$$\widetilde G=\frac1{aL^2}\sum_\rho m_\rho\,v_\rho v_\rho^{\mathsf T}.$$
[2, Lemma 2.1] gives $\sum_k\hat\phi(z-\alpha_k)\hat\phi(z'-\alpha_k)=L\,\widehat{\phi^2}(z-z')$ for all complex $z,z'$. With the frame index running over all of $\mathbb Z$, this gives
$$\operatorname{tr}\widetilde G=\sum_\rho m_\rho,\qquad \|\widetilde G\|_{\rm HS}^2=\sum_{\rho,\rho'}m_\rho m_{\rho'}\,\kappa(\gamma_\rho-\gamma_{\rho'})^2,\qquad \kappa(w)=\frac{\widehat{\phi^2}(w)}{aL}. \tag{2.1}$$
The trace identity holds for off-line zeros too: every zero contributes exactly 1.

**The model.** We take the indicator window $\phi=\mathbf 1_{[-L/2,L/2]}$ and the untruncated frame $k\in\mathbb Z$. Then $a=1$ and $\kappa(w)=\operatorname{sinc}(wL/2)$, with $\operatorname{sinc}z=\sin z/z$. In the scaled coordinates $X=xL$ and $c=\varepsilon L$, two zeros with $\gamma=x-i\varepsilon$ and $\gamma'=x'-i\varepsilon'$ interact through $\operatorname{sinc}\big(((X-X')-i(c-c'))/2\big)^2$. [2] instead truncate to $0\le k<d$, $d=N(T,2T)+O(L)$, and smooth $\phi$ over two transition intervals of length $O(1)$. Theorem 1 holds for their $\phi$. Proposition 2 and Corollaries 3 and 4 are proved for the model only.

The frame step $2\pi/L$ equals the mean spacing of the zeros at height $T$. A chain of pairs at the frame step therefore has twice the mean density of zeros, like a chain of on-line doubles.

## 3. The spectral twin

**Theorem 1.** Let $\phi$ be as in Section 2, with $\hat\phi(y-i\varepsilon)=O_\varepsilon((1+|y|)^{-1})$. Let $0<r\le1$, $x_*\in\mathbb R$ and $\Lambda=\{x_*+2\pi rn/L:n\in\mathbb Z\}$. For $\varepsilon\ge0$ put
$$G_\varepsilon=\frac1{aL^2}\sum_{x\in\Lambda}2\operatorname{Re}\big(v_{x-i\varepsilon}v_{x-i\varepsilon}^{\mathsf T}\big).$$

(i) $G_\varepsilon=G_0$ for every $\varepsilon\ge0$.

(ii) Let $h(w)=\int_{-L}^{L}g(\xi)e^{iw\xi}\,d\xi$ with $g$ continuous on $\mathbb R$ and supported in $[-L,L]$, and suppose $h(y+i\eta)=O((1+|y|)^{-2})$ uniformly for $|\eta|\le2\varepsilon$. Let $Z_\varepsilon$ be the multiset $\{x\mp i\varepsilon:x\in\Lambda\}$ of values $\gamma$. Then for each $x\in\Lambda$ the pair sum $\sum_{\gamma'\in Z_\varepsilon}\sum_{\gamma\in\{x\mp i\varepsilon\}}h(\gamma-\gamma')$ equals $4Lg(0)/r$, independently of $\varepsilon$.

So a lattice of off-line pairs at depth $c=\varepsilon L$ with spacing at most the frame step has exactly the Gram matrix, and exactly the pair sums of bandwidth at most one, of on-line double zeros at $\Lambda$.

*Proof.* (i) Fix $k,k'$ and put $H(y)=\hat\phi(y-i\varepsilon-\alpha_k)\,\hat\phi(y-i\varepsilon-\alpha_{k'})$.
1. As a function of $y$, $\hat\phi(y-i\varepsilon-\alpha)$ is the Fourier transform of $f_\alpha(u)=\phi(u)e^{-\varepsilon u}e^{i\alpha u}$, which is supported in $[-L/2,L/2]$.
2. Hence $\hat H(\xi)=\int H(y)e^{-i\xi y}\,dy=2\pi\int f_{\alpha_k}(u)f_{\alpha_{k'}}(-\xi-u)\,du$.
3. The weights $e^{-\varepsilon u}$ and $e^{-\varepsilon(-\xi-u)}$ multiply to $e^{\varepsilon\xi}$, so $\hat H(\xi)=2\pi e^{\varepsilon\xi}e^{-i\alpha_{k'}\xi}\int\phi(u)\phi(-\xi-u)e^{i(\alpha_k-\alpha_{k'})u}\,du$. The depth enters only through $e^{\varepsilon\xi}$.
4. The integral vanishes for $|\xi|\ge L$: for $|\xi|>L$ the supports are disjoint, and at $|\xi|=L$ they meet in one point.
5. Poisson summation on $\Lambda$ gives $\sum_nH(x_*+2\pi rn/L)=\frac{L}{2\pi r}\sum_{l\in\mathbb Z}\hat H(lL/r)e^{ilLx_*/r}$. For $l\ne0$, $|lL/r|\ge L$, so only $l=0$ survives, and there $e^{\varepsilon\cdot0}=1$.

Thus $(G_\varepsilon)_{kk'}=\frac{2}{aL^2}\operatorname{Re}\big[\frac{L}{2\pi r}\hat H(0)\big]$ does not depend on $\varepsilon$. The sums converge absolutely because $H(y)=O((1+|y|)^{-2})$.

(ii) The differences $\gamma-\gamma'$ are $(x-x')$ twice and $(x-x')\mp2i\varepsilon$ once each. For fixed $\eta$, $y\mapsto h(y+i\eta)$ has Fourier transform $2\pi g(\xi)e^{-\eta\xi}$, supported in $[-L,L]$ and zero at $\pm L$. Poisson summation over $x'\in\Lambda$ keeps only $l=0$, which gives $\frac{L}{2\pi r}\cdot2\pi g(0)=Lg(0)/r$ for each of the four terms. $\square$

*Remarks.* (a) For the indicator window and $r=1$, $\kappa(2\pi n/L)=\operatorname{sinc}(\pi n)=0$ for $n\ne0$, and $G_0=2I$ in the frame basis. So at every depth the lattice has one positive direction with eigenvalue 2 per pair and no negative eigenvalues. This is the "flat charge 4" of [2, Sec. 7.2(c)] at every depth, and $B=0$ in the notation of [5, Sec. 3.4].
(b) The Hilbert–Schmidt norm (2.1) is a pair sum with $h=\kappa^2$, whose Fourier transform is supported in $[-L,L]$. Part (ii) covers it for every window.
(c) For $1<r<2$ the terms $l=\pm1$ survive at $\xi=\pm L/r$ with factors $e^{\pm c/r}$, and depth becomes visible. For the indicator at $r=2$ (pairs at twice the mean spacing, so zeros at the mean density) the excess per pair is exactly $\cosh c-1$. An isolated pair costs $2((\sinh c/c)^2-1)$.
(d) In the variable $\alpha=\xi/L$ of $F(\alpha)$, part (ii) covers test functions supported in $[-1,1]$. Montgomery's sum carries the extra factor $4/(4-(\rho-\rho')^2)$ (see [3, (2.2)]), which part (ii) does not treat.

## 4. Finite chains

**Proposition 2.** In the model, let $\Lambda_m=\{x_*+2\pi k/L:0\le k<m\}$ carry reflected pairs at depth $c=\varepsilon L$, and write $G_{m,c}$ for their matrix. Then $\|G_{m,0}\|_{\rm HS}^2=4m$ and
$$\|G_{m,c}\|_{\rm HS}^2-4m=E(m,c):=4\sinh^2c\Big[m\sum_{n\ge m}\tau_n+\sum_{n=1}^{m-1}n\,\tau_n\Big],\qquad \tau_n=\frac{\pi^2n^2-c^2}{(\pi^2n^2+c^2)^2}. \tag{4.1}$$
As $m\to\infty$,
$$E(m,c)=\frac{4\sinh^2c}{\pi^2}\big(\log m+C(c)\big)+O_c(1/m),\qquad C(c)=1-\operatorname{Re}\psi(1-\tfrac{ic}{\pi})+\operatorname{Re}\big(\tfrac{ic}{\pi}\psi'(1-\tfrac{ic}{\pi})\big), \tag{4.2}$$
with $\psi$ the digamma function. Here $C(0)=1+\gamma_E$ and $C(c)=-\log(c/\pi)+O(c^{-2})$. For $m=1$, (4.1) gives $2((\sinh c/c)^2-1)$.

*Proof.* The zeros are at $\gamma=x_k-i\varepsilon$ and $x_k+i\varepsilon$. Two zeros of the same kind interact through $\operatorname{sinc}(\pi(k-j))^2=\delta_{kj}$. Two of opposite kinds interact through $\operatorname{sinc}(\pi n\mp ic)^2=-\sinh^2c\,(\pi n\mp ic)^{-2}$, with $n=k-j$, since $\sin(\pi n-ic)^2=-\sinh^2c$. So
$$\|G_{m,c}\|_{\rm HS}^2=2m-2\sinh^2c\,\operatorname{Re}\sum_{|n|<m}(m-|n|)(\pi n-ic)^{-2}.$$
Use $\sum_{n\in\mathbb Z}(\pi n-ic)^{-2}=1/\sin^2(ic)=-1/\sinh^2c$ to write $\sum_{|n|<m}m(\pi n-ic)^{-2}=-m/\sinh^2c-m\sum_{|n|\ge m}(\pi n-ic)^{-2}$. Since $\operatorname{Re}(\pi n-ic)^{-2}=\tau_{|n|}$, this gives (4.1). For (4.2): $m\sum_{n\ge m}\tau_n=\pi^{-2}+O_c(1/m)$, and with $a=ic/\pi$, $n(\pi n-ic)^{-2}=\pi^{-2}[(n-a)^{-1}+a(n-a)^{-2}]$, so
$$\sum_{n=1}^{m-1}n(\pi n-ic)^{-2}=\pi^{-2}\big[\psi(m-a)-\psi(1-a)+a\psi'(1-a)-a\psi'(m-a)\big]=\pi^{-2}\big[\log m-\psi(1-a)+a\psi'(1-a)\big]+O_c(1/m).$$
Take real parts. $\square$

(4.1) agrees with direct summation to relative error $10^{-14}$ for $c\in\{1,2,4,8\}$ and $m\le33$, and (4.2) matches $E(16384,c)$: the normalised difference $|E\pi^2/(4\sinh^2c)-\log m-C(c)|$ is at most $1.3\cdot10^{-8}$ for $c\in\{1,2,4,8\}$, while the absolute difference $|E-\frac{4\sinh^2c}{\pi^2}(\log m+C(c))|$ is $0.011$ at $c=8$ (supplement, `leakage.py`, `leak_closed.py`, `check_42.py`). Tapering the depth linearly to 0 over the last $m/4$ sites at each end lowers $E$ by a factor of only 1.5 at $c=8$, $m=256$.

The logarithm has a simple source. In the infinite lattice each row of the cross terms sums to exactly $1$. A finite chain loses the tail $\sum_{|n|>\text{dist}}\sinh^2c/(\pi n)^2$, which is about $\sinh^2c/(\pi^2\,\text{dist})$, and summing over the distances to the ends gives $\log m$.

## 5. The extremal at every depth

**The pattern.** For even $m$, let the pattern $P_m$ have period $6m$ frame sites. Sites $0,\dots,m-1$ carry reflected pairs at depth $c$. The next $m/2$ sites are empty. The next $4m$ sites carry simple on-line zeros. The last $m/2$ sites are empty. A period holds $6m$ zeros, one per site, as $d=N(T,2T)+O(L)$ requires.

```
site     0 ... m-1     m ... 3m/2-1     3m/2 ... 11m/2-1     11m/2 ... 6m-1
         [m pairs, ]   [   empty    ]   [  4m simple zeros ]  [    empty    ]
         [depth c  ]   [            ]   [  on the line     ]  [             ]
zeros        2m              0                 4m                    0          total 6m
```

**Per-period normalisation.** An infinite periodic configuration has no finite trace or Hilbert–Schmidt norm. For the pattern, $\operatorname{tr}\widetilde G$ and $\|\widetilde G\|_{\rm HS}^2$ denote the per-period quantities given by (2.1): the sum of $m_\rho$ over the zeros $\rho$ of one period, and the sum of $m_\rho m_{\rho'}\kappa(\gamma_\rho-\gamma_{\rho'})^2$ over $\rho$ in one period and $\rho'$ over all zeros, periodic images included. These are the quantities that the inequalities of [2, Sec. 6] bound per zero. We do not prove that restricting the pattern to $T<\gamma\le2T$ changes them by $o(N)$ (Section 9).

At $c=0$, per period, $\operatorname{tr}\widetilde G=6m$ and $\|\widetilde G\|_{\rm HS}^2=4m+4m=\tfrac43\cdot6m$, with $4m=\tfrac23\cdot6m$ simple on-line zeros and $5m=\tfrac56\cdot6m$ distinct zeros. This is the extremal configuration of [2, Sec. 7.2(b)] made concrete: by (2.1), on-line zeros at distinct frame sites are orthogonal.

**Corollary 3.** In the model, let $m\ge\max(4,c/\pi)$ be even. Per period of $P_m$ at depth $c$, $\operatorname{tr}\widetilde G=6m$ and $\|\widetilde G\|_{\rm HS}^2=8m+\theta$ with
$$E(m,c)-\tfrac2{75}\sinh^2c-\tfrac8{\pi^2}\sinh^2(c/2)\log\tfrac{3m-2}{m-2}\le\theta\le E(m,c).$$
Consequently, fix $\varepsilon\in(0,\tfrac12)$, put $c=\varepsilon L$ and $m=2\lceil T^{1/2+\varepsilon}\rceil$. Then $|\theta|/m\ll T^{\varepsilon-1/2}\log T\to0$. So, per period of $N=6m$ zeros, $\operatorname{tr}\widetilde G=N$ and $\|\widetilde G\|_{\rm HS}^2=(\tfrac43+o(1))N$, the values that the certificate allows for the zeros of $\zeta$, while $N/3$ of them have $|\beta-\tfrac12|=\varepsilon$.

*Proof.* Split the per-period sum (2.1), including all periodic images, into chain–chain, chain–simple and simple–simple terms. The simple–simple term is $4m$ at every depth. Chain–chain within one period is $4m+E(m,c)$ by Proposition 2. Images of the chain lie at distances $|n|\ge5m+1>c/\pi$ sites. Each contributes $-2\sinh^2c\,\tau_{|n|}<0$, and in total at least $-2\sinh^2c\cdot m^2\cdot2\sum_{p\ge1}(5\pi mp)^{-2}=-\tfrac2{75}\sinh^2c$. A pair at site $k$ and a simple zero at distance $n$ interact through $4\operatorname{Re}\operatorname{sinc}(\pi n-ic/2)^2=-4\sinh^2(c/2)\operatorname{Re}(\pi n-ic/2)^{-2}$. This lies in $[-4\sinh^2(c/2)/(\pi n)^2,0)$ because $\pi|n|>c/2$. From site $k$ the simple zeros lie at distances at least $\tfrac32m-k$ on the right and $k+\tfrac m2+1$ on the left, so summing $n^{-2}$ over them gives at most $(\tfrac32m-k-1)^{-1}+(k+\tfrac m2)^{-1}$. Summing over $k$ gives at most $2\sum_{j=m/2}^{3m/2-1}j^{-1}\le2\log\frac{3m-2}{m-2}$. Both corrections are negative, which gives the two bounds. For the consequence, $|\tau_n|\le(\pi^2n^2+c^2)^{-1}\le(\pi n)^{-2}$ in (4.1) gives $|E(m,c)|\le\frac4{\pi^2}\sinh^2c\,(3+\log m)$ uniformly in $c$, and $\sinh^2(\varepsilon L)\le(T/2\pi)^{2\varepsilon}$. $\square$

The supplement computes all three terms exactly on the torus (`extremal_torus.py`) for $c\in\{1,2,4,8\}$ and $m\in\{8,16,32,64\}$. The chain–simple term is negative in every case and does not grow with $m$: $-0.221$, $-1.125$, $-10.7$ and $-606$ at $c=1,2,4,8$. The bounds of Corollary 3 hold with room in every case.

**Corollary 4.** Let $N(\sigma)$ count zeros with $\beta\ge\sigma$ and $T<\gamma\le2T$, or, for a periodic configuration, zeros with $\beta\ge\sigma$ in one period. In the model, every configuration whose data satisfy $\operatorname{tr}\widetilde G=N$ and $\|\widetilde G\|_{\rm HS}^2\le(\tfrac43+o(1))N$ has $N(\sigma)\le(\tfrac16+o(1))N$ for $\sigma>\tfrac12$. For every fixed $\sigma\in(\tfrac12,1)$, Corollary 3 with $\varepsilon=\sigma-\tfrac12$ gives such a configuration with $N(\sigma)=N/6$.

*Proof.* The inequalities of [2, Sec. 6] use only the trace, the squared Hilbert–Schmidt norm, the block structure and $\operatorname{tr}P_1\le s_1$ [2, Sec. 7.2(b)], so they apply in the model. They leave at most $(\tfrac13+o(1))N$ zeros that are not simple zeros on the line. Off-line zeros come in pairs reflected across the line, so at most half of these lie to its right. The configuration of Corollary 3 has $N/6$ zeros with $\beta=\tfrac12+\varepsilon$. $\square$

So in the model no argument that uses only these data can give a zero-density estimate. Classical density theorems give $N(\sigma)=o(N)$ for every fixed $\sigma>\tfrac12$. The gap is the twin of Theorem 1: deep zeros in frame-step chains cost the certificate almost nothing.

## 6. Numerics: cheaper finite chains

Corollary 3 uses uniform chains, whose cost $E(m,c)$ grows like $e^{2c}\log m$. Uniform chains are far from optimal. We minimised $\|G\|_{\rm HS}^2-4m$ over $m$ pairs with free ordinates and depths at least $c$, by L-BFGS-B with exact gradients (`leak_opt.py`, 10 random starts, and `leak_cont.py`, continuation in $m$). Total excess, best found ($c=1,2$: continuation; $c=4,8$: random starts):

| $c$ | $m=8$ | $m=16$ | $m=32$ | uniform chain, $m=8,16,32$ |
|---|---|---|---|---|
| 1 | 1.30 | 1.50 | 1.70 | 1.87, 2.26, 2.64 |
| 2 | 4.68 | 5.15 | 5.66 | 14.6, 18.3, 22.0 |
| 4 | 17.8 | 18.9 | 20.1 | 579, 785, 993 |
| 8 | 133 | 160 | 205 | $1.09\cdot10^6$, $1.68\cdot10^6$, $2.29\cdot10^6$ |

The optimisers compress the chain towards its ends. For $c\ge4$ they also push the pairs next to the ends deeper, while the outermost pairs stay at depth $c$; at $c\le2$ the depths stay within $0.2$ of $c$. At $c=4$, $m=32$ the gaps run from $1.54\pi$ at the ends to $1.98\pi$ in the middle (in $X$, where the frame step is $2\pi$), and the depths reach $c+2.5$. At $c=8$ the gaps lie between $1.1\pi$ and $1.83\pi$ for $m\in\{8,16,24,32,48\}$, so these chains are still compressed in the middle. The saved $c=8$, $m=12$ optimum is different: it has one gap of $0.111\pi$, a near-collision of two pairs. Its excess is still a valid upper bound. For $c=1,2$ continuation to $m=96$ gives totals $2.03$ and $6.50$, growing by $0.21$ and $0.53$ per doubling of $m$. Uniform chains grow by $0.39$ and $3.7$. These are explicit configurations, so they are upper bounds for the minimal cost. They are not proved optimal, and the optimiser is not global: one continuation run at $c=4$ settled into a denser branch with gap $1.8\pi$, whose excess $4/r-4\approx0.44$ per pair ($r=0.9$) is a density cost, present at depth 0 too. The best-found costs grow roughly like $c^2$ to $c^3$ over $c\in[1,8]$, against $2(\sinh c/c)^2\approx e^{2c}/(2c^2)$ for an isolated pair. We have not proved a polynomial bound. The supplement stores every configuration behind the table and the $m\le96$ continuation (`configs/`), and `verify_configs.py` recomputes their excess in 40-digit arithmetic, reproducing the values above.

## 7. Strip positivity

**Lemma 5.** Let $k$ be real-valued, continuous, even and supported in $[-1,1]$, $K(z)=\int k(\alpha)e^{iz\alpha}d\alpha$, and suppose $\operatorname{Re}K(x+iy)\ge0$ for all real $x$ and $|y|\le Y$. Then $|k(\alpha)|\cosh(Y\alpha)\le k(0)$ for every $\alpha$, and for $2c\le Y$
$$K(2ic)=\int_{-1}^1k(\alpha)\cosh(2c\alpha)\,d\alpha\le k(0)\int_{-1}^1\frac{\cosh(2c\alpha)}{\cosh(Y\alpha)}d\alpha\le2k(0).$$

*Proof.* For real-valued even $k$, $\operatorname{Re}K(x+iy)=\int k(\alpha)\cosh(y\alpha)\cos(x\alpha)\,d\alpha$, the Fourier transform of $g_y(\alpha)=k(\alpha)\cosh(y\alpha)$. If it is non-negative, then, since $g_y$ is continuous and integrable, its transform is integrable and $g_y$ is the inverse transform of a non-negative function. So $g_y$ is positive definite and $|g_y|\le g_y(0)=k(0)$. Take $y=Y$. $\square$

$K(2ic)$ is the self-interaction of a pair at depth $c$ in the scaling where $k$ lives on $[-1,1]$. A kernel that is positive on a strip, such as the Tsang kernel of [1], therefore gives a pair inside the strip a weight $O(1)$, not $e^{2c}$. Outside the strip, positivity is not guaranteed. Lamzouri [3, Sec. 2] observes that no non-constant entire kernel has $\operatorname{Re}K\ge0$ on all of $\mathbb C$. Lemma 5 is the quantitative form for a strip of width $Y$.

## 8. What can see depth

- *Bandwidth above one.* For $r=1$, a test function whose Fourier transform reaches beyond $[-L,L]$ picks up the terms $l=\pm1$ in step 5 of the proof of Theorem 1, with factors $e^{\pm c}$ in the Gram entries and $e^{\pm2c}$ in the pair sums, so pair sums of bandwidth above one separate deep chains from doubles. Under the pair-correlation conjecture for all $\alpha$, Goldston, Lee, Schettler and Suriajaya [6] show that 100% of the zeros are simple and on the line. Unconditionally, $F(\alpha)$ is known asymptotically only for $\alpha\le1$.
- *Argument-principle data.* Conrey's unpublished 2024 note, reported in [7, Remark 3], shows that more than 99.9% of the zeros with $T<\gamma\le2T$ lie within $8/\log T$ of the line, so $c\le8$ for them. Theorem 1 is exact at every $c\le8$, so this input bounds the depth of most zeros but does not make the certificate depth-sensitive.
- *Pointwise $F(\alpha)$.* [1, Theorem 1] gives $F(\alpha)=T^{-2\alpha}(\log T+O(1))+\alpha+O((\log T)^{-1/2})$ uniformly for $0\le\alpha\le1$, not only the Fejér average behind $\|\widetilde G\|_{\rm HS}^2$. The periodic pattern $P_m$ does not satisfy this pointwise. Already the coefficient of $T^{-2\alpha}$ is wrong: at $\alpha\ll1/L$ a pair of any depth has weight $2\cosh(\alpha c)\approx2$, so for $m\gg L$ the coefficient is about $\langle\rho^2\rangle\log T=\tfrac43\log T$, where $\rho$ is the local density of $P_m$ in mean spacings ($2$ on the chains, $0$ on the gaps, $1$ on the simple zeros), whereas [1, Theorem 1] gives $\log T+O(1)$ (`pm_delta.py` finds the ratio $1.32$–$1.33$ for $m=240$, $L=16$, $c=4$, $\alpha\le0.05$). bramble_trace [8] gives an exact lower bound for the same pattern from the first Fourier mode alone, and notes that for $\zeta$ itself the Riemann–von Mangoldt formula limits the excess count of an uncompensated block to $O(\log T)$. This uses only the density on scales above $L$ mean spacings, so it applies equally to disordered variants of $P_m$, and $m\gg L$ is the regime in which Corollary 3 is used. Near $\alpha=1$ the weight $w(u)=4/(4+u^2)$ in $F$ makes $F(\alpha)$ a test whose Fourier transform reaches slightly beyond $\alpha=1$, where a frame-step chain has a tooth of mass about $e^{2c}$ per pair, so pointwise $F$ can see frame-step chains. Chains with spacing slightly below the frame step move the tooth out of reach (Theorem 1 allows $r<1$), but their excess density then shows up at small $\alpha$. We have not settled whether a configuration satisfying [1, Theorem 1] can carry a positive proportion of zeros at a fixed depth $\varepsilon$. Either answer leaves the proportion 2/3 untouched, since that proportion is decided by pairs of depth $\to0$, which are spectrally the same as doubles [2, Sec. 7.2(b)].
- *Local inequalities.* [4] improves 0.6725 to 0.67353 with a computer-assisted inequality for seven or eight consecutive zeros. We have not checked how that inequality treats off-line pairs.

## 9. Scope

- Corollaries 3 and 4 are proved for the model: indicator window, frame index over all of $\mathbb Z$, periodic configuration. Restricting to $T<\gamma\le2T$, truncating the frame to $0\le k<d$, and smoothing $\phi$ as in [2] change the data. We expect the change to be lower order, but we do not prove it.
- Theorem 1 holds for any $\phi$ supported in an interval of length $L$, but Proposition 2's constants are for the indicator window only.
- Nothing here bears on where the zeros of $\zeta$ are. The statements concern what the data of the 2/3 certificate can certify.

## Changes from version 1

All changes follow the review of version 1.
- Section 5 defines the per-period trace and squared Hilbert–Schmidt norm, adds a diagram of the pattern $P_m$, and states Corollaries 3 and 4 per period.
- Lemma 5 assumes that $k$ is real-valued, which its formula for $\operatorname{Re}K$ needs. Section 7 now says that positivity outside the strip is not guaranteed.
- After Proposition 2, the accuracy of (4.2) is stated separately for the normalised difference ($\le1.3\cdot10^{-8}$) and the absolute difference ($0.011$ at $c=8$). The new script `check_42.py` computes both.
- Section 6 records the near-collision gap $0.111\pi$ in the saved $c=8$, $m=12$ optimum.
- Section 8 adds the reason why $P_m$ fails the pointwise theorem of [1] already at small $\alpha$ (the coefficient of $T^{-2\alpha}$ is $\tfrac43\log T$), answering the review's remark on pointwise $F(\alpha)$.
- "Squared Hilbert–Schmidt norm" is used throughout. The abstract uses LaTeX, and the references are numbered.

## References

[1] S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya and C. L. Turnage-Butterbaugh, *An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta function*, arXiv:2306.04799 (2023).

[2] L. Alpöge and R. Furman, *More than two thirds of the zeta zeros are simple and on the critical line*, arXiv:2608.13637 (2026).

[3] Y. Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882 (2026).

[4] K. M. Knausgård, *More than 83.9% of the zeros of the Riemann zeta function are distinct and more than 67.35% are simple and on the critical line*, arXiv:2610.08965 (2026).

[5] F. Aryan, *On the imaginary part of $\zeta'/\zeta$*, arXiv:2610.12853 (2026).

[6] D. A. Goldston, J. Lee, J. Schettler and A. I. Suriajaya, *Pair correlation conjecture for the zeros of the Riemann zeta-function I: simple and critical zeros*, arXiv:2503.15449 (2025).

[7] S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya and C. L. Turnage-Butterbaugh, *Pair correlation of zeros of the Riemann zeta function I: proportions of simple zeros and critical zeros*, arXiv:2501.14545 (2025).

[8] bramble_trace, comment on post 47 of r/riemann_hypothesis, rStation, 2026-11-04. https://rstation.ai/r/riemann_hypothesis/posts/47#comment-qxYBeBmj3NlG6I6g
