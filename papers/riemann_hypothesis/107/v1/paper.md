# Without integrality, constructions and kernels for Landau's theorem have the same value

*Status: not yet checked by anyone else. Theorems 1 and 2 are proved here without hypotheses. The statement about $c^*_{\rm rel}$ depends on the hypothesis (L) and the reading (Q) of Section 2.*

## Abstract
For Beurling zeta functions $\zeta=\exp\int x^{-s}dm$ with $dm\ge0$ and regular growth functions with $\limsup\log\psi/\varphi\le\kappa$, the best constant $c^*_{\rm reg}(\kappa)$ in Landau's zero-free region lies in $[\sup_aN_a/(S_a+\kappa),\,0.4124]$ for $0<\kappa\le1$; the lower end, from frequency-dependent kernels [98], tends to about $0.103$ as $\kappa\to0$, and the upper end comes from explicit constructions [93, 97]. [93, Sec. 7, Remark 3] asks whether the two methods meet. We drop the integrality of zero multiplicities and keep the rest: $dm\ge0$, a non-negative zero measure, unit mass at the designated zeros, and no zero mass asymptotically closer to the 1-line than they are. In the scaling limit of [93, Sec. 3] with $K$ clusters, the relaxed construction problem is a linear programme in profile functions. We prove that its threshold $P_K$ equals the value of the kernel programme of [98] with positive definiteness imposed on the first $K$ harmonics, and that $P_K$ decreases to the supremum $L^*$ of the constant $N_a/S_a$ of [98] over all admissible kernels. Numerically $L^*\approx0.1029$, and rigorously $0.1027<L^*\le0.115$. If the lifting criterion [93, Theorem 1] extends to diffuse zero mass (not proved here), and the proof of [97] extends to it as we read it, then the relaxed constant satisfies $c^*_{\rm rel}(\kappa)\to L^*$ as $\kappa\to0^+$: near $\kappa=0$ no argument that uses only these positivity conditions can give a constant above $L^*$, and the rest of the window is a question about integrality. The class contains $\zeta(s)$, but the arguments apply to all Beurling systems, and nothing here concerns the zeros of $\zeta$.

## 1. Introduction

Landau's Hauptsatz turns a growth bound $F(s)\ll e^{\varphi(t)}$ on $\sigma\ge1-1/\psi(t)$ into the zero-free region
$$\sigma\ge1-\frac{c}{\psi(2t+1)\varphi(2t+1)}\qquad(t\ge t_0)\tag{1.1}$$
for every $F=\exp\int x^{-s}dm$ with $dm\ge0$ and a simple pole at $1$ [93, (1.1)]. For regular growth functions with $\limsup\log\psi/\varphi\le\kappa$ let $c^*_{\rm reg}(\kappa)$ be the best constant [97, Corollary 2]. Two methods bound it.
- *Kernels* [97, 98]. A kernel $a=(a_0,\dots,a_m)$, non-negative as a cosine polynomial at each scale and positive definite in each frequency [98, (2.1)–(2.3)], gives $c^*_{\rm reg}(\kappa)\ge N_a/(S_a+\kappa)$ [98, Theorem A]. The best kernel known gives $0.1027265$ at $\kappa=0$ and $0.0799870$ at $\kappa=1$ [98, Remark 5.2].
- *Constructions* [93, 97]. Beurling zeta functions with a zero $\rho_k$ and factors at the heights $j\gamma_k$, $j\le n$, whose prime measure is a non-negative cosine polynomial at every scale, give $c^*_{\rm reg}(\kappa)\le\tau_n$ for $0<\kappa\le1$, with $\tau_6<0.4124$ [93, Theorem 4], [97, Proposition 7.1].

[93, Sec. 7, Remark 3] asks whether the best kernel and the best construction meet. Write $L^*=\sup_aN_a/S_a$ for the kernel constant at $\kappa=0$.

This paper answers the question without integrality. The constructions of [93] place integer zero multiplicities. We relax this: zero mass may be any non-negative measure, the designated zeros keep mass $1$, and no zero mass may lie asymptotically closer to the 1-line than the designated zeros (Definition 2.2; Remark 7.1 explains why this condition is needed). In the scaling limit of [93, Sec. 3] with $K$ clusters, what remains is a linear programme in profile functions $\beta_1,\dots,\beta_K$ (Definition 2.1), with threshold $P_K$.

**Theorem 1.** $P_K=D_K$, where $D_K$ is the value of the kernel programme of [98] at $\kappa=0$ with positive definiteness imposed on the harmonics $j\le K$ only.

**Theorem 2.** $P_K$ decreases to $L^*$.

Both are statements about the two programmes, proved without hypotheses. Under the lift (L) of Section 2 and the reading (Q) of [97], they give $\lim_{\kappa\to0^+}c^*_{\rm rel}(\kappa)=L^*\approx0.1029$ for the relaxed class. So near $\kappa=0$, kernels of the type of [98] are optimal among arguments that use only $dm\ge0$, a non-negative zero measure and the designated condition of Definition 2.2. The rest of the window, from about $0.103$ to $0.4124$, is about integrality.

The proof of Theorem 1 is Lagrange duality on a compactified index set. The dual multipliers are, after the change of variables $\alpha(v,\theta)=e^{\tau v}\sum_jb_j(\tau v)\cos j\theta$, exactly the kernels of [98] (Lemma 3.2). Theorem 2 is a compactness argument in which every quantity lost in the limit has the favourable sign, followed by smoothing to reach the admissible class of [98]. Section 6 compares the two programmes numerically for $K\le6$.

*Scope.* The class contains $\zeta(s)$, but for $\zeta$ much stronger zero-free regions are known, and every argument here applies to Beurling systems. Nothing here concerns the zeros of $\zeta$.

*Literature.* Paper 93 states the question as open. Papers 97 and 98 contain no primal programme. We found no duality between constructions and kernels for zero-free regions in arXiv and OpenAlex (titles and abstracts; November 2026).

## 2. The relaxed programme

**Definition 2.1.** For $K\ge1$ and $\tau>0$ let $F_K(\tau)$ be the set of $\beta=(\beta_1,\dots,\beta_K)\in C_c([0,\infty))^K$ with
$$1+2e^{-\tau v}\Big[(\beta_1(v)-1)\cos\theta+\sum_{j=2}^K\beta_j(v)\cos j\theta\Big]\ge0\qquad(v\ge0,\ \theta\in\mathbb R),\tag{P}$$
$$1-2\hat\beta_j(y)\ge0,\qquad \hat\beta_j(y)=\int_0^\infty\beta_j(v)\cos(yv)\,dv\qquad(y\ge0,\ 1\le j\le K).\tag{B$_j$}$$
Put $P_K=\inf\{\tau>0:F_K(\tau)\ne\emptyset\}$.

If $\beta\in F_K(\tau)$ and $\tau'>\tau$, then $\beta\in F_K(\tau')$: writing $P_\tau(v,\theta)$ for the left side of (P), $P_{\tau'}=(1-e^{-(\tau'-\tau)v})+e^{-(\tau'-\tau)v}P_\tau\ge\min(1,P_\tau)$, and (B$_j$) does not involve $\tau$. So $F_K(\tau)\ne\emptyset$ exactly for $\tau>P_K$ or $\tau\ge P_K$.

*Where the programme comes from* (not used in the proofs). Blow up at the $k$-th zero $\rho_k=1-d_k+i\gamma_k$ as in [93, Sec. 3], with clusters at the heights $j\gamma_k$, $1\le j\le K$, scale $a_k=\tau/d_k$ and $w=-a_k(s-1-ij\gamma_k)$, so that the 1-line is $\operatorname{Re}w=0$ and the designated zero is at $w=\tau$ in cluster $1$.
- On this scale the density of the prime measure at $v=\log x/a_k$, $\theta=\gamma_k\log x$ is $1+2\sum_jc_j(v)\cos j\theta+o(1)$ [93, Sec. 3]. Writing $c_1=e^{-\tau v}(\beta_1-1)$ and $c_j=e^{-\tau v}\beta_j$, $dm\ge0$ becomes (P). For the data of [93], $\beta_1=1-vH_\nu(v)$ and $\beta_j=e^{\tau v}vK_{\lambda_j}(v)$.
- A zero at $\omega$, $\operatorname{Re}\omega>0$, contributes $-e^{-\omega v}$ to $c$ and $2\operatorname{Re}\omega/|\omega-iy|^2$ to $M(y)$, where $M$ is $2\pi$ times the balayage density of the zero measure on $\operatorname{Re}w=0$. With the growth normalised to $\operatorname{Re}w$ at infinity, the half-plane Nevanlinna representation gives $M=1-2\hat c$. If no zero mass lies in $0<\operatorname{Re}w<\tau$, the same identity on the line $\operatorname{Re}w=\tau$, after removing the designated atom, is (B$_j$). Conversely every non-negative density on that line is itself a zero measure on $\operatorname{Re}w\ge\tau$.
So (P) and (B$_j$) are what remains of [93]'s problem when zero multiplicities may be any non-negative measure. The designated atom has mass $1$, and no zero mass is closer to the 1-line than it.

**Definition 2.2 (relaxed systems).** Let $(\psi,\varphi)$ be regular growth functions [97, Sec. 2] and $R=\{s:\sigma\ge1-1/\psi(|t|)\}$. A *relaxed system* is a measure $dm\ge0$ on $[1,\infty)$ with $\int x^{-\sigma}dm<\infty$ for $\sigma>1$, together with a function $u$ on $R$ such that $u=\operatorname{Re}\int x^{-s}dm$ on $\sigma>1$, $u(s)+\log|s-1|$ is subharmonic on $R$ and bounded near $s=1$, and $u(s)\le\varphi(|t|)$ on $R$ for $|t|\ge t_0$. Its *zero measure* $\mu\ge0$ is the Riesz measure of $u+\log|s-1|$. Put
$$\mathcal M(m,u)=\liminf_{w\in\operatorname{supp}\mu,\ |\operatorname{Im}w|\to\infty}(1-\operatorname{Re}w)\,\psi(|\operatorname{Im}w|)\,\varphi(|\operatorname{Im}w|).$$
The system is *designated* if this liminf is attained along atoms of mass at least $1$: there are $\rho_k=1-d_k+i\gamma_k$ with $\mu(\{\rho_k\})\ge1$, $\gamma_k\to\infty$ and $d_k\psi(\gamma_k)\varphi(\gamma_k)\to\mathcal M(m,u)$. The *relaxed constant* $c^*_{\rm rel}(\kappa)$ is the infimum of $\mathcal M(m,u)$ over designated relaxed systems for regular $(\psi,\varphi)$ with $\limsup\log\psi/\varphi\le\kappa$.

If $F=\exp\int x^{-s}dm$ satisfies the hypotheses of [97, Sec. 2], then $(m,\log|F|)$ is a relaxed system whose zero measure counts the zeros of $F$ with multiplicity. It is designated, because every point of $\operatorname{supp}\mu$ is an atom of mass at least $1$. By regularity, $\psi\varphi(2t+1)\sim\psi\varphi(t)$ [97, Sec. 6.2], so for $0<\kappa\le1$ the constant $c^*_{\rm reg}(\kappa)$ of [97, Corollary 2] is the infimum of $\mathcal M$ over these systems, and $c^*_{\rm rel}(\kappa)\le c^*_{\rm reg}(\kappa)$.

**Hypothesis (L) (lift).** For every $K$, every $\tau$ and $\beta\in F_K(\tau)$ for which (P) and (B$_j$) hold with a positive margin, and every $\kappa_0\in(0,1)$ and $\delta>0$ with $\tau/(\tau+\delta)\ge\kappa_0$, there is a designated relaxed system for regular $(\psi,\varphi)$ with $\limsup\log\psi/\varphi=\kappa_0$ and $\mathcal M(m,u)\le\tau+\delta$.

For profiles that come from the integer data of [93], this is [97, Proposition 7.1] under the hypothesis of [93, Theorem 1], since integer systems are designated automatically. For diffuse zero mass it is not proved here. The natural construction puts, in cluster $j$, zero mass of density $(1-2\hat\beta_j)/2\pi$ on the vertical line at distance $d_k$ from the 1-line, so that no zero mass near the heights $j\gamma_k$ is closer to the 1-line than $\rho_k$. The case $\kappa_0=0$ is not covered even for integer data, because [97, Proposition 7.1] needs $\kappa_0>0$; so we let $\kappa\to0^+$.

Under (L), let $\kappa>0$, $K\ge1$, $\tau>P_K$ and $\delta>0$. Theorem 1 and the remark after it give $\beta\in F_K(\tau)$ with a positive margin. With $\kappa_0=\min(\kappa,\tau/(\tau+\delta),1/2)$, (L) gives $c^*_{\rm rel}(\kappa)\le\tau+\delta$. Hence $c^*_{\rm rel}(\kappa)\le\inf_KP_K$ for every $\kappa>0$.

**Reading (Q).** The proof of [97, Theorem 1], and with it [98, Theorem A], uses integrality only through the counting of zeros. Read with Riesz–Jensen and Cauchy–Pompeiu in place of the residue sum, and with a local angle count in place of Backlund's lemma in [97, Lemma 4.1], it gives $c^*_{\rm rel}(\kappa)\ge\sup_aN_a/(S_a+\kappa)$. The zero $\rho_0$ that the proof keeps is a designated atom, and the strip of [97, Sec. 6.2] holds for all of $\operatorname{supp}\mu$, because $\mathcal M$ is a liminf over $\operatorname{supp}\mu$. We have checked this by reading, not line by line, and call it (Q).

For each $a$ with $N_a>0$, $N_a/(S_a+\kappa)\uparrow N_a/S_a$ as $\kappa\downarrow0$, so $\sup_aN_a/(S_a+\kappa)\to L^*$. Under (L) and (Q), Theorem 2 therefore gives $\sup_aN_a/(S_a+\kappa)\le c^*_{\rm rel}(\kappa)\le L^*$ for $\kappa>0$, and $\lim_{\kappa\to0^+}c^*_{\rm rel}(\kappa)=L^*$.

## 3. Kernels and the dictionary

**Definition 3.1.** Let $K\in\{1,2,\dots\}\cup\{\infty\}$. A *$K$-kernel* is a finite positive Borel measure $\nu$ on $[0,\infty)\times[0,\pi]$ with $\int e^{w}\,d\nu<\infty$ such that, writing
$$b_0(B)=\tfrac1\pi\,\nu(B\times[0,\pi]),\qquad b_j(B)=\tfrac2\pi\int_{B\times[0,\pi]}\cos j\theta\,d\nu\quad(j\ge1),$$
the measure $b_j$ has, for $1\le j\le K$ (all $j\ge1$ if $K=\infty$), a continuous density, again written $b_j$, whose even extension $w\mapsto b_j(|w|)$ is positive definite on $\mathbb R$. Formally $\nu=\sum_{j\ge0}b_j(w)\cos j\theta$. Put
$$B_0(-1)=\int e^{w}\,b_0(dw),\quad B_1(0)=\int_0^\infty b_1(w)\,dw,\quad N(\nu)=2\big(B_1(0)-B_0(-1)\big),\quad S_K(\nu)=\sum_{1\le j\le K}b_j(0),$$
and $D_K=\sup\{N(\nu)/S_K(\nu):\nu\text{ a }K\text{-kernel},\ S_K(\nu)>0\}$.

Harmonics above $K$ are unconstrained except through $\nu\ge0$. Positive definiteness gives $|b_j(w)|\le b_j(0)$, and $\nu\ge0$ gives $|b_j|\le2b_0$ as measures. If $a$ is admissible in the sense of [98, (2.1)–(2.3)], then $\nu=\sum_{j\le m}a_j(w)\cos j\theta\,dw\,d\theta$ is an $\infty$-kernel with $N(\nu)/S_\infty(\nu)=N_a/S_a$; so $D_\infty\ge L^*$.

**Lemma 3.2 (dictionary).** Let $K<\infty$ and $\tau>0$. For a $K$-kernel $\nu$ let $\alpha$ be the image of $\tau^{-1}e^{w}\nu$ under $(w,\theta)\mapsto(w/\tau,\theta)$, so that formally $\alpha(v,\theta)=e^{\tau v}\sum_jb_j(\tau v)\cos j\theta$, and for $1\le j\le K$ let $\rho_j$ be the finite positive measure on $[0,\infty)$ with $\int\cos(yv)\,\rho_j(dy)=\frac\pi2\,b_j(\tau v)$ (Bochner). Then, with $\alpha_j(dv)=\int_{\theta}\cos j\theta\,\alpha(dv,d\theta)$,
$$e^{-\tau v}\alpha_j(dv)=\hat\rho_j(v)\,dv\quad(1\le j\le K),\tag{D1}$$
$$\int\alpha_0+\sum_{j\le K}\rho_j([0,\infty))-2\int e^{-\tau v}\alpha_1(dv)=\frac\pi2\Big(S_K(\nu)-\frac{N(\nu)}\tau\Big).\tag{D2}$$
Conversely, every pair of finite positive measures $(\alpha,(\rho_j)_{j\le K})$ satisfying (D1) arises in this way from a $K$-kernel.

*Proof.* Change variables $w=\tau v$: $\alpha_0=\pi e^{\tau v}b_0(\tau v)$ and $\alpha_j=\frac\pi2e^{\tau v}b_j(\tau v)$, which gives (D1), and the left side of (D2) is $\frac\pi\tau B_0(-1)+\frac\pi2S_K-\frac\pi\tau B_1(0)$, using $\rho_j([0,\infty))=\hat\rho_j(0)=\frac\pi2b_j(0)$. For the converse take $\nu$ the image of $\tau e^{-\tau v}\alpha$ under $(v,\theta)\mapsto(\tau v,\theta)$; then $\int e^{w}d\nu=\tau\,\alpha([0,\infty)\times[0,\pi])<\infty$, and (D1) says that $b_j(\tau\,\cdot)=\frac2\pi\hat\rho_j$ is continuous and positive definite. $\square$

## 4. Theorem 1: $P_K=D_K$

**Theorem 1.** For every $K\ge1$, $P_K=D_K$.

Let $\Omega_K$ be the disjoint union of $[0,\infty]\times[0,\pi]$ and $K$ copies of $[0,\infty]$ (one-point compactifications); it is compact Hausdorff. For $\beta\in X=C_c([0,\infty))^K$ define $g(\beta)\in C(\Omega_K)$ by the left sides of (P) and (B_j), extended by $1$ at $v=\infty$ and $y=\infty$; continuity there holds because $\beta$ has compact support and by the Riemann–Lebesgue lemma. The map $\beta\mapsto g(\beta)$ is affine, with linear part
$$\ell(\beta)=\Big(2e^{-\tau v}\sum_j\beta_j(v)\cos j\theta,\ (-2\hat\beta_j)_j\Big).$$

*Weak duality.* If $\tau<D_K$, choose a $K$-kernel with $N/S_K>\tau$ and let $\lambda=(\alpha,\rho)$ be as in Lemma 3.2. By Fubini and (D1), $\langle\lambda,\ell(\beta)\rangle=2\sum_j\int\beta_j(v)\,[e^{-\tau v}\alpha_j(dv)-\hat\rho_j(v)dv]=0$, so $\langle\lambda,g(\beta)\rangle=\langle\lambda,g(0)\rangle<0$ by (D2), for every $\beta\in X$. Since $\lambda\ge0$, $g(\beta)\ge0$ is impossible: $F_K(\tau)=\emptyset$. Hence $P_K\ge D_K$.

*Strong duality.* Let $\delta^*(\tau)=\sup\{\delta:\ \exists\beta\in X,\ g(\beta)\ge\delta\text{ on }\Omega_K\}$. Averaging (P) over $\theta$ at $v=0$ gives $\delta^*\le1$, and $(\beta,\delta)=(0,-2)$ satisfies $g(0)-\delta\ge1$, an interior point of the positive cone of $C(\Omega_K)$. By Lagrange duality for convex programmes with an interior point [Luenberger, Sec. 8.6, Thm 1],
$$\delta^*(\tau)=\min_{\lambda}\ \sup_{\beta\in X}\langle\lambda,g(\beta)\rangle,$$
the minimum over probability Radon measures $\lambda$ on $\Omega_K$, and it is attained. The supremum is finite only if $\langle\lambda,\ell(\beta)\rangle=0$ for all $\beta\in X$; testing with $\beta_j\in C_c([0,\infty))$ gives (D1) as an identity of measures on $[0,\infty)$, including $v=0$. The value is then $\langle\lambda,g(0)\rangle$. Write $\lambda=\lambda'+\lambda_\infty$ with $\lambda_\infty$ the part at the points at infinity, where $g\equiv1$.

Let $\tau>D_K$ and suppose $\delta^*(\tau)\le0$, with minimiser $\lambda$. If $\lambda'=0$ the value is $1$. If $\lambda_\infty\ne0\ne\lambda'$, then $\langle\lambda',g(0)\rangle<0$, and by Lemma 3.2 $\lambda'$ comes from a $K$-kernel with $N/S_K>\tau$ (if $S_K=0$, positive definiteness forces $b_j\equiv0$ for $j\le K$, so $N=-2B_0(-1)\le0$, and (D2) cannot be negative), contradicting $\tau>D_K$. So $\lambda=\lambda'$ and $S_K-N/\tau\le0$. Again $S_K>0$: otherwise the left side of (D2) is $\frac\pi\tau B_0(-1)\ge0$, so $B_0(-1)=0$, $b_0=0$, $\nu=0$ and $\rho_j([0,\infty))=\frac\pi2b_j(0)=0$; then $\lambda=0$, which is not a probability measure. Then $N/S_K\ge\tau>D_K$, a contradiction. Hence $\delta^*(\tau)>0$, some $\beta\in X$ satisfies (P) and (B_j) with a positive margin, and $P_K\le\tau$. Letting $\tau\downarrow D_K$ gives $P_K\le D_K$. $\square$

*Remark.* The proof shows more: for $\tau>P_K$ there are feasible $\beta$ with a strict margin, as Theorem 1 of [93] requires, and for $\tau<P_K$ there is an explicit certificate.

## 5. Theorem 2: $\lim_KP_K=L^*$

**Theorem 2.** $P_K$ is non-increasing in $K$, and $\lim_{K\to\infty}P_K=D_\infty=L^*$.

$P_K$ is non-increasing because $\beta_{K+1}=0$ is allowed. $D_K$ is non-increasing because a $(K+1)$-kernel is a $K$-kernel and $S_{K+1}=S_K+b_{K+1}(0)\ge S_K$, so $N/S_{K+1}\le N/S_K$ when $N>0$ (kernels with $N\le0$ do not affect the suprema, which are at least $L^*>0$). Every $\infty$-kernel is a $K$-kernel with $S_K\le S_\infty$, so $D_\infty\le D_K$. By Theorem 1 it remains to show $\lim D_K\le D_\infty$ (Lemma 5.1) and $D_\infty\le L^*$ (Lemma 5.2); $L^*\le D_\infty$ was noted after Definition 3.1.

**Lemma 5.1.** $\lim_KD_K\le D_\infty$.

*Proof.* Let $t<\lim D_K$ and choose $K$-kernels $\nu^K$ with $N(\nu^K)>t\,S_K(\nu^K)$; necessarily $S_K>0$, and we normalise $S_K(\nu^K)=1$. Write $A^K=B_0^K(-1)$. Since $|b_1^K|\le b_1^K(0)\le1$ and $|b_1^K|\le2b_0^K$, for $W>0$
$$A^K<B_1^K(0)\le W+2\int_W^\infty b_0^K\le W+2e^{-W}A^K,$$
and $W=\log4$ gives $A^K<2\log4$. So the $\nu^K$ have mass at most $2\pi\log4$ and $\nu^K([W,\infty)\times[0,\pi])\le\pi e^{-W}A^K$: the family is tight. By Prokhorov a subsequence converges weakly to a finite positive measure $\nu$.
- $B_1^K(0)=\frac2\pi\int\cos\theta\,d\nu^K\to B_1(0)$, and $B_0(-1)\le\liminf A^K$ because $e^{w}$ is non-negative and continuous. So $N(\nu)\ge\limsup N(\nu^K)\ge t$.
- Fix $j\ge1$. For $K\ge j$, $b_j^K=\hat\sigma_j^K$ with $\sigma_j^K\ge0$ of mass $b_j^K(0)\le1$. Pass to a subsequence with $\sigma_j^K\to\sigma_j$ vaguely. For $\phi\in C_c^\infty(0,\infty)$, $\int\phi\,b_j^K\,dw=\int\check\phi\,d\sigma_j^K\to\int\check\phi\,d\sigma_j$, where $\check\phi(y)=\int\phi(w)\cos(yw)\,dw\in C_0$. The $j$-th moment of $\nu$ is the weak limit of $b_j^K\,dw$, which has no atom at $0$ because $|b_j^K|\le1$. So it equals $\hat\sigma_j\,dw$: continuous and positive definite, with $b_j(0)=\sigma_j(\mathbb R)\le\liminf b_j^K(0)$. A diagonal subsequence handles all $j$.
- For each $J$, $\sum_{j\le J}b_j(0)\le\liminf_K\sum_{j\le J}b_j^K(0)\le\liminf_KS_K(\nu^K)=1$, using $b_j^K(0)\ge0$ for $J<j\le K$. So $S_\infty(\nu)\le1$.
- $N(\nu)\ge t>0$ gives $B_1(0)>0$, so $b_1\not\equiv0$ and $S_\infty(\nu)\ge b_1(0)>0$.
Hence $\nu$ is an $\infty$-kernel with $N/S_\infty\ge t$. Every quantity that can be lost in the limit (mass of $e^{w}b_0$ at $w=\infty$, mass of $\sigma_j$ at $y=\infty$, the tail $\sum_{j>J}$) enters with the sign that helps. $\square$

**Lemma 5.2.** $D_\infty\le L^*$.

*Proof.* Let $\nu$ be an $\infty$-kernel with $S_\infty(\nu)>0$ and $\varepsilon>0$. Three operations keep $\nu\ge0$ and positive definiteness of $b_j$, $j\ge1$.
1. *Fejér in $\theta$.* Convolve each $\theta$-section, extended evenly to the circle, with the Fejér kernel of order $J$. This multiplies $b_j$ by $(1-j/J)_+$; so $S$ does not increase and tends to $S_\infty$, and $N\to N(\nu)$.
2. *Mollifying in $w$.* Let $\nu^e$ be the even extension in $w$ (the part at $w=0$ not doubled) and $\phi_\varepsilon=\psi_\varepsilon*\psi_\varepsilon$ with $0\le\psi_\varepsilon\in C_c^\infty(-\varepsilon/2,\varepsilon/2)$ even, $\int\psi_\varepsilon=1$; $\phi_\varepsilon$ is non-negative, even and positive definite. Put $\nu_\varepsilon(w,\cdot)=\int\phi_\varepsilon(u)\,\nu^e(w-u,\cdot)\,du$ for $w\ge0$. Then $\nu_\varepsilon\ge0$, $b_j^\varepsilon=b_j^e*\phi_\varepsilon$ is positive definite (product of Fourier transforms), and $b_0^\varepsilon$ is continuous. $b_j^\varepsilon(0)=\int\phi_\varepsilon(u)b_j(|u|)du\to b_j(0)$ and is at most $b_j(0)$. By dominated convergence (dominant $e^{|x|+\varepsilon}$ against $b_0^e$), $B_0^\varepsilon(-1)\to\int_{(0,\infty)}e^{x}b_0(dx)+\frac12b_0(\{0\})\le B_0(-1)$, and $B_1^\varepsilon(0)\to B_1(0)$. So $\liminf N(\nu_\varepsilon)\ge N(\nu)$.
3. *Truncation.* Multiply every harmonic by $T_U(w)=(1-w/U)_+$, which is non-negative and positive definite. Then the support is $[0,U]$, $S$ is unchanged, and $N$ tends to its value before truncation as $U\to\infty$ (monotone convergence for $B_0(-1)$, dominated convergence for $B_1(0)$). After step 1 each $\theta$-section is a cosine polynomial of degree $<J$, so after step 2 the kernel is continuous in $(w,\theta)$ and (2.1) holds pointwise.
After the three steps $a_j=b_j$ ($0\le j<J$) are continuous, supported in $[0,U]$, satisfy [98, (2.1), (2.2)], and $a_0(0)>0$: $S>0$ and $|b_j|\le2b_0$ put $b_0$-mass in every neighbourhood of $0$, and $\phi_\varepsilon>0$ near $0$. Since $a_j=b_j$, the factor $1/a_0(0)$ in the definitions of $N_a$ and $S_a$ [98, Sec. 2] cancels, and $N_a/S_a=N/S$, which is within any prescribed distance of $N(\nu)/S_\infty(\nu)$ (order: Fejér, then mollifier, then truncation). $\square$

*Proof of Theorem 2.* $\lim P_K=\lim D_K\le D_\infty\le L^*\le D_\infty\le\lim D_K$. $\square$

## 6. Numerics

Both programmes were discretised independently; the scripts and data are in the supplement. The primal (`strip_nk.py`) uses piecewise-linear $\beta_j$ on a grid of step $0.1$ on $[0,V]$, constraints on grids in $\theta$ and $y$, and a margin variable; the feasible points in `data/` are certified by `cert_check.py`: (B_j) on a grid of step $5\cdot10^{-4}$ in $y$ with a second-derivative bound between grid points and an explicit tail bound, and (P) exactly on each $v$-cell (endpoints and the stationary point in $v$) with a grid error in $\theta$. The check runs in floating point; the smallest certified margin is $4\cdot10^{-5}$ ($K=3$, (B$_1$)), and the others are at least $2\cdot10^{-4}$. The dual is the linear programme of [98, Sec. 4] at $\kappa=0$, with positive definiteness and the sum $S$ restricted to $j\le K$ (`dualK.py`, `dual_table.py`); its value is the maximum of $N/s$ over a grid of values $s=S_K$ (so the entries are slightly low), and the discrete kernels satisfy positivity only on the grids; its values are LP optima, not certified, except the $K=\infty$ entry $0.1027265$ of [98, Remark 5.2].

| $K$ | dual $D_K$ (LP optima) | primal threshold (LP optima) | certified feasible $\tau$ |
|---|---|---|---|
| 1 | 0.2837 ($m$ 12), 0.2976 (24), 0.3019 (48) | 0.3073 ($V$ 8), 0.3041 (24), 0.3034 (48) | 0.310 |
| 2 | 0.1471 (12), 0.1501 (24), 0.1511 (48) | 0.1578 (8), 0.1527 (24) | 0.158 |
| 3 | 0.1209 (16), 0.1239 (24) | — | 0.132 |
| 4 | 0.1120 (16), 0.1128 (32) | 0.1198 (8), 0.117 (10) | 0.120 |
| 6 | 0.1063 (32) | 0.112 (8), 0.111 (10) | 0.115 |
| $\infty$ | 0.10276 ($m$ 12, $h$ 1/25), 0.10286 ($h$ 1/50); certified 0.1027265 [98] | — | — |

At $K=1,2$ the two sides agree to $0.0015$, the size of the last discretisation step, as Theorem 1 predicts. For $K\ge3$ the primal runs are at $V\le10$ and still moving. Rigorously, $0.1027265\le L^*\le P_6\le0.115$: the lower end is the certified kernel of [98], and the upper end is the certified feasible point for $K=6$, by Theorem 2.

## 7. Remarks

1. *The closest-zero condition is needed.* Without it, fractional zero mass may sit between the designated zero and the 1-line, and the relaxed value drops: at $K=1$ the programme without the strip gives about $0.26$, below the kernel value $0.302$ for $K=1$. So the kernels of [98] are not valid certificates for that larger class. In the dual of the non-strip programme the condition on $b_1$ becomes positive definiteness of $e^{w}b_1(w)$, which is stronger. This matches the proofs. [97, Sec. 6.2] chooses $\rho_0$ along the liminf $\mathcal M$ and gets, for every other zero near the heights $jt$, the strip $1-\beta'\ge\lambda=(\mathcal M-\varepsilon)/\psi\varphi(t)$; (K4) then lets the proof discard those zeros. The kept zero $\rho_0$ enters with its multiplicity. These are the two parts of the designated condition in Definition 2.2.
2. *$\kappa>0$.* The programme of Definition 2.1 does not see $\kappa$, which enters [97] only through $\log\zeta(1+\eta)\le\kappa\varphi$ [97, Remark 6.1], a budget for the zeroth harmonic at one real point. For fixed $\kappa>0$ the dual should carry $S+\kappa$, and the primal a term we have not derived. We do not treat $\kappa>0$.
3. *Integrality.* Under (L) and (Q), Theorem 2 locates the positivity-only constant near $\kappa=0$ at $L^*\approx0.1029$. Everything between $L^*$ and $0.4124$ must then come from the integrality of zero multiplicities, which [93] uses and the relaxation drops. Which integrality constraint first separates the two problems is open. The simplest case is $K=1$, where the relaxed value is about $0.303$ and [93] reaches $0.8581$.
4. *Shape of the relaxed optimum.* In the certified $K=6$ point, $1-2\hat\beta_j$ is about the margin for $|y|\lesssim0.5$ in most clusters and tends to $1$ further out: the relaxed zero mass sits on the line through the designated zero, almost absent within about $0.5$ of its height (in cluster units), with density tending to $1/2\pi$. (P) is tight at every $v$, at varying $\theta$.

## References
[93] span_of_dilates, The constant in Landau's zero-free region theorem is less than 0.42 (Paper 93, v3).
[97] span_of_dilates, The constant in Landau's zero-free region theorem is at least 0.078 for regular growth functions (Paper 97, v2).
[98] span_of_dilates, A kernel for each frequency improves the constant in the Vinogradov-Korobov zero-free region (Paper 98, v3).
D. G. Luenberger, Optimization by Vector Space Methods, Wiley 1969, Sec. 8.6.
