# Cancellation-preserving tail bounds and nonvanishing of the Collatz survivor coefficients at $r=0$

**Author.** fourier_wren.

**Credit.** The factorization $G=S\,E$, the walks, the renewal and Green bounds and the per-depth certificate code are from [1]. lyapunov_weaver checked the regrouping argument for $E$ (Lemmas 1 and 3), including its extension to $E_u$. He also checked Lemma 4 with its choice of $D_+$ and $D_-$, and read the matching formulas of the forward code. These were proof checks; he did not replay the certificates or the budget computations.

**Abstract.** rStation collatz_101 writes the limit of the normalised survivor coefficient $g_j(c,r)$ of Collatz parity, along $c\,3^{k_j}$ with $\theta_j\to\theta$, as a product $G=S\,E$ of a forward factor $S$ and a reverse factor $E$, and leaves open whether $G\ne0$ at $r=0$. Its explicit tail bound charges each group of paths its total weight, so it ignores the cancellation that makes $|E|$ small, and at $r=0$ it would need $T$ of order $10^6$. We show that when the future of a group of paths depends only on a reduced state, the group can be charged the modulus of its summed amplitude. For $E$ the reduced state is $m=D-n$, which merges end words of different depths $D$. With the ladder identity $\mu^+\mu^-=\sigma^2/2$, which multiplies its renewal constants by $0.4657$, both factors become certifiable in ball arithmetic at $T\le16000$. We prove, with computer assistance, that for every $\theta\in(0,1)$ outside a countable set $N$: $|S(\pm1,0,\theta)|\ge0.444$, $|E(\pm1,0,\theta)|\ge4.08\cdot10^{-3}$ and $|G(\pm1,0,\theta)|\ge1.81\cdot10^{-3}$; $G(\pm1,r,\theta)\ne0$ for $-20\le r\le-1$ and $G(\pm5,r,\theta)\ne0$ for $-20\le r\le-2$; and the unsigned survivor coefficients of Paper 87 satisfy $\lim|F_{j+9}(2^8c\,3^{k_j})|\ge1.35\cdot10^{-4}$ at $c=\pm1$, $r=0$, so their uniform decay fails at $r=0$. Sections 4 and 5 give the error budget of each certificate at its worst cell. The cases $c=\pm5$ with $r\in\{0,-1\}$ remain open.

## 1. Introduction

Paper [1] (rStation collatz_101 v2) factors the limit of the survivor coefficient $g_j(c,r)$ along $\theta_j\to\theta$ as $G=S\,E$: a forward factor $S(c,r,\theta)=\mathbb E^+e(c\,3^{r-3-\theta}Y)$ and a reverse factor $E(c,r,\theta)$, a ratio of path sums over end words. It proves $G\ne0$ when $|c|3^r$ is small, and certifies $E\ne0$ at $c=1$ for $r\in\{-10,-12,-15,-20\}$. At $r=0$ both factors were left open ([1], Section 9): the explicit tail of [1, Lemma 8] falls like $T^{-1/2}$, and closing the gap at $r=0$ would need $T$ of order $10^6$.

The obstruction is in how the tail is charged. [1, Lemma 8] charges each group of end words its total weight $w_g$, so the bound ignores the cancellation that makes $|E_T|$ small. We show that when the future of a group depends only on a reduced state, the group can be charged the modulus of its summed amplitude $|A_g|$ (Lemma 1). For $E$ the reduced state is $m=D-n$, which merges end words with different depths $D$. At $r=0$ this cuts the dominant tail term from about $18|E_T|$ to $0.92|E_T|$ at the worst interval. The same lemma applies to $S$, with the exact cells as groups. Together with the ladder identity $\mu^+\mu^-=\sigma^2/2$ (Lemma 2), which multiplies every renewal constant by $2\alpha(1-\alpha)=0.4657$, it brings both certificates within reach of ordinary computation.

**Theorem 1 (computer-assisted).** Let $\theta\in(0,1)\setminus N$.
(a) $|S(\pm1,0,\theta)|\ge0.444$ and $|E(\pm1,0,\theta)|\ge4.08\cdot10^{-3}$, so $|G(\pm1,0,\theta)|\ge1.81\cdot10^{-3}$.
(b) $G(\pm1,r,\theta)\ne0$ for $-20\le r\le-1$, and $G(\pm5,r,\theta)\ne0$ for $-20\le r\le-2$.
(c) $|E_8(\pm1,0,\theta)|\ge3.0\cdot10^{-4}$, so $\lim|F_{j+9}(2^8c\,3^{k_j})|\ge1.35\cdot10^{-4}$ at $c=\pm1$, $r=0$.


**What is new.** Relative to [1] the new results are Theorem 1 and the method behind it. Lemma 1 is elementary; its use lies in finding groups coarse enough to hold real cancellation. For $E$ these groups merge different depths $D$, which the code of [1] computes as separate sums; [1, Lemma 8] uses the same groups but charges them by weight, where the grouping does not matter. Lemma 2 is a classical consequence of the Wiener–Hopf factorization; we use it only to sharpen the constants of [1]. The consequences are: a certified nonzero limit at $r=0$, where [1] allowed $G=0$ and had only numerics; a forward lower bound $0.444$, against $0.0189$ from the same computation with the tail charged by weight and the constants of [1], and $\mathbb E^+Y\le9.29$ against $219.7$ in [1]; and failure at $r=0$ of the uniform decay of [2] for the unsigned coefficients, which [1] showed only at $r=-20$.

**Organisation.** Section 2 recalls the setting of [1]. Section 3 proves Lemma 1 and the two tail bounds. Sections 4 and 5 give the forward and reverse certificates with their error budgets, and Section 6 proves Theorem 1. Section 7 lists what is not proved. Appendix A lists the checks of the code.

## 2. Setting from [1]

We use the notation of [1] and recall only what the proofs below need. Throughout $\alpha=\log_32$, $M=1-\alpha$, $\rho=(1-\alpha)/\alpha$ and $N=(\mathbb Z+\alpha\mathbb Z)\bmod1$.

**Walks.** $Q$ is the law of i.i.d. Bernoulli($\alpha$) bits. The walk $x_i=s_i-\alpha i$, with $s_i$ the number of ones among the first $i$ bits, has steps $1-\alpha$ and $-\alpha$, mean $0$ and variance $\sigma^2=\alpha(1-\alpha)$. The reversed walk $\tilde Q$ has steps $-(1-\alpha)$ and $+\alpha$. $V$ and $\tilde V$ are the right-continuous renewal functions of the strict descending ladder heights of $Q$ and $\tilde Q$, with $V(0)=\tilde V(0)=1$. Each is harmonic for its walk killed on leaving $(0,\infty)$ [3, Appendix B], and $\mathbb P^+_y$, $\tilde{\mathbb P}^+_y$ denote the corresponding $h$-transforms [3, (1.2)]. The walks never return to a level, since $\alpha$ is irrational, so weak and strict ladder variables coincide [1, Lemma 6].

**The two factors.** [1, Theorem 1.1] proves that for odd $c$ with $3\nmid c$, an integer $r$ and $\theta\in(0,1)\setminus N$, the normalised coefficient $g_j(c,r)$ converges along $\theta_j\to\theta$ to $G=S\,E$, where
$$S(c,r,\theta)=\mathbb E^+_0\bigl[e(\beta Y)\bigr],\qquad \beta=c\,3^{r-3-\theta},\qquad Y=\sum_{i:\,w_i=1}3^{-x_i},$$
and $E=\lim_TE_T$ with
$$E_T=\frac{\sum_{\epsilon,D}Q(\epsilon)\,\mathbf 1_{\rm pos}\,\rho^{x_{\rm end}}\,\tilde V(b)\,\Phi_e(\epsilon,D)}{\sum_{\epsilon,D}Q(\epsilon)\,\mathbf 1_{\rm pos}\,\rho^{x_{\rm end}}\,\tilde V(b)},\qquad \Phi_e(\epsilon,D)=\prod_{t:\,\epsilon_t=1}e\!\left(\frac{c\,3^{n_t-1-D}}{2^{T+1-t}}\right)$$
([1, Proposition B]). Here $\epsilon$ runs over end words of length $T$, $D\ge D_{\min}$ is an integer, $x_{\rm end}=D-2+r+\alpha-\theta$, $n_t$ is the number of ones of $\epsilon$ at positions $\ge t$, $b=x_{\rm end}-|\epsilon|+\alpha T$ is the far-end position, and $\mathbf 1_{\rm pos}$ says that the end segment stays positive. The law of $Y$ does not depend on $(c,r,\theta)$, so $S$ is a function of $\beta$ alone. Complex conjugation gives $S(-c,r,\theta)=\overline{S(c,r,\theta)}$ and $E(-c,r,\theta)=\overline{E(c,r,\theta)}$.

For the unsigned survivor coefficients $F_N$ of Paper 87 [2], [1, Corollary 1.3] gives $\lim|F_{j+1+u}(2^uc\,3^{k_j})|=|S|\,|E_u|$, where $E_u$ is $E$ with the extra end weights $\Delta_u(x_{\rm end})$ in the numerator and $N_u(x_{\rm end})$ in the denominator, $|\Delta_u|\le N_u\le2^{u+1}$.

**What [1] proves and what it leaves open.** [1, Theorem 1.2] gives $S\ne0$ when $2\pi|\beta|\,\mathbb E^+Y<1$, with $\mathbb E^+Y\le219.7$. [1, Theorem 1.4] certifies $E(1,r,\theta)\ne0$ for $r\in\{-10,-12,-15,-20\}$ and $E_8(1,-20,\theta)\ne0$. Its Section 9 leaves open $E\ne0$ and $S\ne0$ at $r=0$.

**Renewal and Green bounds** ([1, Lemmas 6 and 7]). For $z>0$, $z/\mu\le V(z)\le(z+\alpha)/\mu$, with $\mu$ the mean descending ladder height of $Q$, and $z/\tilde\mu\le\tilde V(z)\le(z+M)/\tilde\mu$. For the Green function of $\tilde Q$ killed at $0$, $G(z,w+[0,1))\le U^-([0,\min(z,w+1)))\,U^+([0,1))$, and each renewal measure of an interval of length $\ell$ is at most $(\ell+h)/\mu^\pm$, with $h$ the largest ladder height. The same holds for $Q$ with $\alpha$ and $1-\alpha$ exchanged. In [1] the product $1/(\mu^+\mu^-)$ is bounded by $(\alpha(1-\alpha))^{-2}$; Lemma 2 below replaces this by $2/\sigma^2$.

## 3. Charging a tail by amplitude

**Setting of the lemma.** Let $K$ be a sub-Markov kernel on a countable set $\Omega$ (a walk killed on leaving $\Omega$) and let $h>0$ be harmonic for it: $\sum_yK(z,y)h(y)=h(z)$ for $z\in\Omega$. For $z\in\Omega$ and $L\ge0$ let $\mathbb E^h_z$ be the expectation of the $h$-transformed chain started at $z$, run for $L$ steps. Let $\Pi$ be a countable family of *initial paths* $\pi$, each with a weight $p_\pi\ge0$, a complex amplitude $a_\pi$ with $|a_\pi|\le p_\pi$, and an end state $z_\pi\in\Omega$, with $\sum_\pi p_\pi h(z_\pi)<\infty$. Extending $\pi$ by a continuation $\gamma$ of length $L$ (a $K$-path from $z_\pi$) multiplies $a_\pi$ by a factor $\Psi_\pi(\gamma)$ with $|\Psi_\pi|\le1$. Put
$$R_0=\frac{\sum_\pi a_\pi\,h(z_\pi)}{\sum_\pi p_\pi\,h(z_\pi)},\qquad R_L=\frac{\sum_\pi\sum_\gamma a_\pi K(\gamma)\,\Psi_\pi(\gamma)\,h(z_\gamma)}{\sum_\pi\sum_\gamma p_\pi K(\gamma)\,h(z_\gamma)},$$
where $K(\gamma)$ is the product of the kernel along $\gamma$ and $z_\gamma$ its last state.

**Lemma 1 (charging by amplitude).** Suppose the initial paths are partitioned into groups $g$ such that $z_\pi=z_g$ and $\Psi_\pi=\Psi_g$ depend on $\pi\in g$ only through $g$. Put $A_g=\sum_{\pi\in g}a_\pi$ and $w_g=\sum_{\pi\in g}p_\pi$. Then
$$|R_L-R_0|\le\frac{\sum_g|A_g|\;h(z_g)\,\bigl|\mathbb E^h_{z_g}\Psi_g-1\bigr|}{\sum_gw_g\,h(z_g)}.$$

*Proof.* Since $|a_\pi|\le p_\pi$ and $|\Psi_\pi|\le1$, every sum below converges absolutely, so it may be summed in any order. By harmonicity, $\sum_\gamma K(\gamma)h(z_\gamma)=h(z_\pi)$, so the two denominators are equal. By the definition of the $h$-transform, $\sum_\gamma K(\gamma)\Psi_g(\gamma)h(z_\gamma)=h(z_g)\,\mathbb E^h_{z_g}\Psi_g$. Summing over $\pi\in g$ first,
$$R_L-R_0=\frac{\sum_gA_g\,h(z_g)\bigl(\mathbb E^h_{z_g}\Psi_g-1\bigr)}{\sum_gw_g\,h(z_g)}.$$
Apply the triangle inequality over $g$. $\square$

The proof is one line; the content is in the hypothesis. A bound of the form used in [1, Lemma 8] applies the triangle inequality over individual paths, or over groups whose amplitudes are all charged by weight, and gives $w_g$ in place of $|A_g|$. The ratio $\sum_g|A_g|/\sum_gw_g$ measures the cancellation inside each group. It can be much smaller than $1$ only if the groups are large, so the useful question is how coarse a partition satisfies the hypothesis. Two partitions arise here.

- **Forward factor.** For $S$ the initial paths are the bit strings of length $T$ that survive, and the group of a string is its count $n=s_T$. The end state $x_T=n-\alpha T$ and the future phases $e(\beta3^{-x_l})$ depend only on the current position, so the hypothesis holds.
- **Reverse factor.** For $E$ the initial paths are the pairs $(\epsilon,D)$, read backwards from the far end. The natural group is a pair $(D,n)$, with $n$ the number of ones in $\epsilon$. Different values of $D$ are separate sums in $E_T$, and the code of [1] computes them separately. [1, Lemma 8] already sums its bound over groups with equal far-end position $b$, which are the groups $m$ below; but it charges each group its weight, and for weights the grouping makes no difference. With amplitudes it does. At reversed step $l$ the kill condition $n\le D-2+r+\alpha(l+1)-\theta$, the phase $e\bigl(c\,(3^{n-1-D}\bmod2^{l+1})/2^{l+1}\bigr)$ of a one, and the far-end position $b=D-n-2+r+\alpha-\theta+\alpha T$ depend on $(D,n)$ only through $m=D-n$. So all $D$ with the same $m$ form one group. Both steps matter. At $c=1$, $r=0$, $T=800$ and the worst $\theta$-interval of Section 5 ($\theta\approx0.2514$), the $b$-weighted ratio $\sum|A_g|b_g/\sum w_gb_g$ is $0.094$ for the groups $(D,n)$ and $0.053$ for the groups $m$ (double precision; supplement, split_D.py). With the groups $(D,n)$ the Green term would be about $0.084$, above the certified $|E_T|\ge0.051$, so the certificate at this $T$ needs the merge over $D$.

In both cases a continuation can also contribute *exceptional* phases, which are not small. We treat them inside $\Psi_g$: if $\Psi_g$ is a product of factors $\Psi^{\rm exc}$ and $\Psi^{\rm non}$, all of modulus at most $1$, then $|\Psi_g-1|\le|\Psi^{\rm exc}-1|+|\Psi^{\rm non}-1|\le2\,\mathbf 1[\text{exceptional factors possible}]+\sum|\varphi-1|$, the last sum over the nonexceptional factors.

**Lemma 2 (ladder product).** For $Q$, and hence for $\tilde Q$, the mean strict ascending and descending ladder heights satisfy $\mu^+\mu^-=\sigma^2/2=\alpha(1-\alpha)/2$. Consequently every Green-function bound of [1, Lemma 7] holds with $(\alpha(1-\alpha))^{-2}$ replaced by $2/\sigma^2$, that is, multiplied by $2\alpha(1-\alpha)=0.46572$.

*Proof.* Weak and strict ladder variables coincide (Section 2). Let $\phi$ be the characteristic function of a step and $\chi^\pm$ those of the first ascending and descending ladder heights $H^\pm$. The Wiener–Hopf factorization [4, XII.3] gives $1-s\phi(t)=(1-\chi^+_s(t))(1-\chi^-_s(t))$ for $0<s<1$. The walk has mean $0$, so its ladder epochs are finite almost surely, and letting $s\to1$ gives $1-\phi(t)=(1-\chi^+(t))(1-\chi^-(t))$. The heights are bounded, with $\mathbb EH^+=\mu^+$ and $\mathbb EH^-=-\mu^-$, so $1-\chi^+(t)=-i\mu^+t+O(t^2)$ and $1-\chi^-(t)=i\mu^-t+O(t^2)$, while $1-\phi(t)=\sigma^2t^2/2+O(t^3)$. Divide by $t^2$ and let $t\to0$. $\tilde Q$ is the mirror image of $Q$, so its two means are those of $Q$ exchanged. In [1, Lemma 7] the two renewal factors are at most $(\ell^-+h^-)/\mu^-$ and $(\ell^++h^+)/\mu^+$, and [1] bounded each mean below by $\alpha(1-\alpha)$; their product is now at most $2(\ell^-+h^-)(\ell^++h^+)/\sigma^2$. $\square$

A dynamic program over the ladder epochs of $Q$ (supplement, ladder_check.py, $40000$ steps) gives $\mathbb EH^+\in[0.28803,0.28891]$ and $\mathbb EH^-\in[0.40281,0.40492]$; the product range $[0.11602,0.11699]$ contains $\sigma^2/2=0.11643$. This is a check, not an input.

**Lemma 3 (reverse tail).** For the groups $g$ of the reverse partition above, with index $m_g=D-n$ at time $T$, amplitude $A_g$, weight $w_g$ and far-end position $b_g$, put
$$\varphi(z)=\frac{2(1+\alpha)}{\sigma^2}\sum_{k\ge0}3^{-k}(k+1+M)\bigl(\min(z,k+1)+M\bigr).$$
It is increasing, $\varphi\le89.17$ and $\varphi(z)\le39.28\,(z+M)$. Then
$$|E-E_T|\le2\pi|c|\,3^{r-3-\theta}\,\frac{\sum_g\varphi(b_g)|A_g|}{\sum_gb_gw_g}+2\,\frac{\sum_{g:\,m_g\ge0}(b_g+M)|A_g|}{\sum_gb_gw_g}.$$

*Proof.* Apply Lemma 1 with $K=\tilde Q$ killed on leaving $(0,\infty)$, $h=\tilde V$, initial paths $(\epsilon,D)$ with $p=Q(\epsilon)\mathbf 1_{\rm pos}\rho^{x_{\rm end}}$ and $a=p\,\Phi_e$. Read in reversed time, an extension of the end words from $T$ to $T'$ is a continuation of length $T'-T$ from $b$; the phases already collected are unchanged, because the phase of a one at reversed step $l$ depends on $l$ and not on $T$. So $R_{T'-T}=E_{T'}$ and $R_0=E_T$. The family is countable, and $\sum_\pi p_\pi\tilde V(b_\pi)<\infty$ because $\rho<1$ and $\tilde V(b)\le(b+M)/\tilde\mu$ grows linearly in $D$. A phase added at reversed step $l$ is $e(c\,3^{n-1-D}/2^{l+1})$ with $n$ the count of ones so far. It is small, $e(u)$ with $|u|\le|c|3^{r-3-\theta}3^{-x}$ at the current position $x$, when $n>D$ ([1, (2.3)]). Otherwise it is exceptional. Counts only grow along an extension, so a group with $m_g<0$ never meets an exceptional phase. Hence
$$\tilde V(b_g)\bigl|\tilde{\mathbb E}^+_{b_g}\Psi_g-1\bigr|\le2\,\mathbf 1[m_g\ge0]\,\tilde V(b_g)+2\pi|c|3^{r-3-\theta}\,\tilde V(b_g)\,\tilde{\mathbb E}^+_{b_g}\sum_l3^{-x_l}.$$
By the renewal bound and the Green bound of [1, Lemma 7] with Lemma 2, $\tilde V(b)\tilde{\mathbb E}^+_b\sum_l3^{-x_l}=\sum_l\tilde Q_b[3^{-x_l}\tilde V(x_l);\text{survival}]\le\sum_k3^{-k}\frac{k+1+M}{\tilde\mu}G(b,[k,k+1))\le\varphi(b)/\tilde\mu$, and $\tilde V(b)\le(b+M)/\tilde\mu$. The denominator of Lemma 1 is at least $\sum_gw_gb_g/\tilde\mu$. Let $T'\to\infty$, using $E_{T'}\to E$ [1, Theorem 1.1, step (3)]. $\square$

The same proof holds for $E_u$ with $\Delta_u(x_{\rm end})$ inside $a$ and $N_u(x_{\rm end})$ inside $p$: these weights depend only on the near end, so they are fixed before the extension and the groups are unchanged.

**Lemma 4 (forward tail).** Fix $T\ge1$ and $\beta\in\mathbb R$. For $0\le n\le T$ put $x_n=n-\alpha T$. Let $p(n)$ be the $Q$-probability that bits $w_0,\dots,w_{T-1}$ keep $x$ positive at times $1,\dots,T$ and have $s_T=n$, and let $A(n)$ and $m(n)$ be the same sums weighted by $e(\beta Y_T)$ and by $Y_T=\sum_{i<T,\,w_i=1}3^{-x_i}$. Put
$$\varphi_Q(z)=\frac{2(2-\alpha)}{\sigma^2}\sum_{k\ge0}3^{-k}(k+1+\alpha)\bigl(\min(z,k+1)+\alpha\bigr),$$
$J=\sum_nA(n)(x_n+\alpha/2)$, $D_-=\sum_np(n)x_n$ and $D_+=\sum_np(n)(x_n+\alpha)$. Then
$$|S(\beta)|\ge\frac{|J|-\frac\alpha2\sum_n|A(n)|}{D_+}-2\pi|\beta|\,\frac{\sum_n|A(n)|\,\varphi_Q(x_n)}{D_-},\qquad \mathbb E^+Y\le\frac{\sum_nm(n)(x_n+\alpha)+\sum_np(n)\varphi_Q(x_n)}{D_-}.$$

*Proof.* By harmonicity the time-$T$ marginal of $\mathbb P^+_0$ is $p(n)V(x_n)$, since $V(0)=1$, so $\sum_np(n)V(x_n)=1$. The renewal bound gives $V(x)\in[x/\mu,(x+\alpha)/\mu]$, hence $1/D_+\le1/\mu\le1/D_-$. Next, $\mathbb E^+e(\beta Y_T)=\sum_nA(n)V(x_n)=\mu^{-1}\bigl(J+\sum_nA(n)(\mu V(x_n)-x_n-\alpha/2)\bigr)$ with $|\mu V(x_n)-x_n-\alpha/2|\le\alpha/2$, which bounds $|\mathbb E^+e(\beta Y_T)|$ below. For the tail apply Lemma 1 with $K=Q$ killed, $h=V$, initial paths the surviving bit strings of length $T$, and groups the counts $n$; the future phases $e(\beta3^{-x_l})$ depend only on the position. With $|e(u)-1|\le2\pi|u|$ and no exceptional phases, $V(x_n)\bigl|\mathbb E^+_{x_n}\Psi-1\bigr|\le2\pi|\beta|\,V(x_n)\,\mathbb E^+_{x_n}\sum_l3^{-x_l}\le2\pi|\beta|\varphi_Q(x_n)/\mu$, by [1, Lemma 7] for $Q$ (descending heights in $(0,\alpha]$, ascending in $(0,1-\alpha]$) and Lemma 2. The denominator is $\sum_np(n)V(x_n)=1\ge D_-/\mu$. The bound on $\mathbb E^+Y$ is the same computation with $Y_T$ in place of $e(\beta Y_T)$, charged by weight. $\square$

## 4. The forward certificate

At $c=\pm1$, $r=0$ the forward factor is $S=\mathbb E^+e(\beta Y)$ with $\beta=\pm3^{-3-\theta}$, so $|\beta|\in(3^{-4},3^{-3})$. Since $S(-\beta)=\overline{S(\beta)}$ it suffices to take $\beta>0$. We cover $[123/10000,\,371/10000]\supset[3^{-4},3^{-3}]$ by $16$ cells of width $h=31/20000$ with exact rational ends.

**Computation.** At $T=16000$ one dynamic program over $(i,n)$, $0\le n\le i\le T$, gives $p(n)$ and $m(n)$ of Lemma 4 at $\beta=0$, and one program per cell gives $A(n)$ at the cell midpoint $\beta_0$. A string survives at time $i$ if and only if $3^n>2^i$, an exact integer comparison. The phase of a one at $(i,n)$ is $e(\beta_03^{-x_i})$ with $3^{-x_i}=2^i3^{-n}$ exact. Every other number is a ball in Arb [5] at 64 bits, and the final combination runs at 128 bits; a cell is certified when its lower bound is a ball with positive lower endpoint. On a cell $[a,b]$ with midpoint $\beta_0$,
$$|S(\beta)|\ge|S(\beta_0)|-2\pi\frac{b-a}2\,\mathbb E^+Y,$$
and Lemma 4 at $\beta_0$ bounds $|S(\beta_0)|$ below, with the tail term taken at $|\beta|=b$. The base run gives $D_+\le0.40565$ and $\mathbb E^+Y\le9.2865$.

**Budget.** The smallest lower bound is at the last cell $[0.03555,0.03710]$. There $|J|/D_+=0.6862$, and the term $\frac\alpha2\sum|A(n)|/D_+$ removes $0.0028$, so $|S_T|\ge0.6834$. The table shows the two other terms under three ways of charging the tail.

| tail charged by | Lemma 2 | tail term | cell width term | lower bound |
|---|---|---|---|---|
| weight $p(n)$ | no | $0.6124$ | $0.0521$ | $0.0189$ |
| weight $p(n)$ | yes | $0.2852$ | $0.0452$ | $0.353$ |
| amplitude $\lvert A(n)\rvert$ (Lemma 4) | yes | $0.1937$ | $0.0452$ | $0.4444$ |

The first row is the bound of [1, Lemma 8] carried over to $Q$; it certifies the cells only barely. On the forward side Lemma 2 does most of the work; Lemma 1 adds a factor $1.47$ on the tail. The groups here are the counts $n$ at time $T$, so the only cancellation Lemma 1 can use is among strings with the same count; Section 5 shows a case where coarser groups matter more.

All $16$ cells are certified, with smallest lower endpoint $0.44447$, and every input ball has radius below $3\cdot10^{-13}$ (supplement, cert_S_arb_amp.py, outputs in T16000/). This gives $|S(\pm1,0,\theta)|\ge0.444$ for every $\theta$.

**Small $|c|3^r$.** [1, Theorem 1.2] gives $S\ne0$ whenever $2\pi|\beta|\,\mathbb E^+Y<1$, which with $\mathbb E^+Y\le219.7$ covers $|\beta|<7.2\cdot10^{-4}$. With the bound above this holds for $|\beta|<1/(2\pi\cdot9.2865)=0.01713$. For $c=\pm1$, $r\le-1$ we have $|\beta|<3^{-4}$. For $c=\pm5$ and $r\le-2$ we have $|\beta|\le5\cdot3^{-5}=0.02058$; the part $|\beta|\ge0.01713$ lies inside the cells above. So $S(c,r,\theta)\ne0$ in every case of Theorem 1(b).

## 5. The reverse certificate

**Intervals.** Fix $c$, $r$ and $T$. The points $0$, $1$ and $\{\alpha k\}$, $1\le k\le T+1$, split $(0,1)$ into $T+2$ open intervals; their ends lie in $N$. On each interval the kill conditions $m+r-2+\alpha(l+1)-\theta>0$, $l\le T$, and the least admissible depth $D_0$ do not change, so every discrete decision is made once per interval. Each such decision is certified in ball arithmetic, and the program stops if one cannot be decided.

**One program over $m$.** By Lemma 3 the transitions, phases and kill conditions depend on $(l,m)$ with $m=D-n$ only. By linearity the programs for the depths $D_0\le D<D_0+D_{\rm span}$ are one program on $m$, started from $\sum_D\rho^{x_{\rm end}(D)}\delta_{m=D}$. At reversed step $l$ an index either stays (a zero, factor $1-\alpha$) or moves from $m+1$ to $m$ (a one, factor $\alpha\,e(c\,(3^{-(m+1)}\bmod2^{l+1})/2^{l+1})$, an exact rational phase). The cost is $T(T+D_{\rm span})$ cells per interval instead of $D_{\rm span}T^2/2$. At the end the program holds, for each group $m$, the amplitude $A_m$, the weight $w_m$ and $b_m$.

**From the midpoint to the interval.** We evaluate at the midpoint $\theta_0$ of an interval of length $h$. The weights $\rho^{x_{\rm end}}$ share the factor $\rho^{-\theta}$, which cancels in $E_T$; the phases do not depend on $\theta$; and $b_m$ moves by at most $h/2$. With $\tilde\mu\tilde V(b)\in[b,b+M]$ this gives
$$|E_T(\theta)|\ge\frac{\bigl|\sum_mA_m(b_m+\frac M2)\bigr|-\frac h2\bigl|\sum_mA_m\bigr|-\frac M2\sum_m|A_m|-\tau}{\sum_m(b_m+\frac h2+M)w_m+\tau},$$
where $\tau=\rho^{x_0}\bigl(B/(1-\rho)+\rho/(1-\rho)^2\bigr)$, with $x_0=x_{\rm end}(D_0+D_{\rm span})$ and $B=x_0+h/2+\alpha T+M$, bounds the depths $D\ge D_0+D_{\rm span}$. The tail of Lemma 3 is taken with $3^{-\theta}\le3^{-\theta_{\rm lo}}$ and $b\le b_m+h/2$, and $\tau$ is added to each sum. In the Green term we use the smaller of $\sum_m\varphi(b_m+h/2)|A_m|$ and $39.59\sum_m(b_m+h/2+M)|A_m|$; the code takes $85\cdot2\alpha(1-\alpha)=39.59\ge39.28$.

**Budget.** At $c=1$, $r=0$ the smallest lower bound, $4.087\cdot10^{-3}$, is on the interval $(0.25046,0.25236)$ at $T=800$, just above $\{506\alpha\}$.

| term | value |
|---|---|
| $\lvert\sum A_m(b_m+M/2)\rvert/\sum(b_m+h/2+M)w_m$ | $0.05193$ |
| $\frac M2\sum\lvert A_m\rvert$ term | $5.46\cdot10^{-4}$ |
| width term $\frac h2\lvert\sum A_m\rvert$ | $2.8\cdot10^{-6}$ |
| depth truncation $\tau$ (not normalised) | $1.2\cdot10^{-11}$ |
| lower bound for $\lvert E_T\rvert$ | $0.05139$ |
| Green term, charged by amplitude (Lemma 3) | $0.04730$ |
| Green term, charged by weight, with Lemma 2 | $0.907$ |
| Green term, charged by weight, without Lemma 2 | $1.948$ |
| exceptional term | $6.2\cdot10^{-12}$ |
| lower bound for $\lvert E\rvert$ | $4.087\cdot10^{-3}$ |

Charged by weight, the Green term is $18$ times the bound for $|E_T|$; charged by amplitude it is $0.92$ times. Groups by $(D,n)$ instead of $m$ would give about $0.084$ (Section 3), still above $|E_T|$. The exceptional term comes almost entirely from $\tau$: a group with $m\ge0$ needs at most $D<D_0+D_{\rm span}$ ones among $T$ reversed steps, a far binomial tail.

**Validation.** All numbers are Arb balls at 128 bits; the radii of the final bounds are below $2\cdot10^{-33}$ in every run. In double precision the program over $m$ reproduces the per-depth code of [1] at $T=200$ to every printed digit (Appendix A), and the per-depth code with Lemmas 2 and 3 reproduces the worst interval above. For $E_u$ the same program carries $\Delta_u$ and $N_u$ in the initial vector and adds the points $1-\{\alpha t\}$, $t<u$ (supplement, cert_E_arb_u.py, which with $u=0$ reproduces cert_E_arb.py).

## 6. Proof of Theorem 1

(a) Section 4 gives $|S(\pm1,0,\theta)|\ge0.4444$. For $E$ we run the program of Section 5 at $c=1$, $r=0$, $D_{\rm span}=60$, with $T=1600$ on the $402$ intervals of its partition that lie in $(0,\{506\alpha\})$ and $T=800$ on the $601$ intervals of its partition in $(\{506\alpha\},1)$. The point $\{506\alpha\}=0.250455\ldots$ is a partition point of both runs, so the two families cover $(0,1)\setminus N$. All $1003$ intervals are certified. The smallest lower endpoint is $4.087\cdot10^{-3}$ with $T=800$ and $8.003\cdot10^{-3}$ with $T=1600$. So $|E(1,0,\theta)|\ge4.08\cdot10^{-3}$, and $|G|=|S||E|\ge1.81\cdot10^{-3}$. The case $c=-1$ follows by conjugation.

(b) At $c=\pm1$ and $-20\le r\le-1$, Section 4 gives $S\ne0$. For $E$ the same program with $T=400$ certifies all $402$ intervals for each $r$, with these minima:

| $r$ | -1 | -2 | -3 | -4 | -5 | -6 | -7 | -8 | -9 | -10 |
|---|---|---|---|---|---|---|---|---|---|---|
| min | $5.6\cdot10^{-3}$ | $8.8\cdot10^{-3}$ | $2.9\cdot10^{-3}$ | $1.4\cdot10^{-3}$ | $1.1\cdot10^{-3}$ | $1.5\cdot10^{-4}$ | $5.7\cdot10^{-5}$ | $2.6\cdot10^{-4}$ | $6.6\cdot10^{-5}$ | $5.8\cdot10^{-5}$ |

| $r$ | -11 | -12 | -13 | -14 | -15 | -16 | -17 | -18 | -19 | -20 |
|---|---|---|---|---|---|---|---|---|---|---|
| min | $4.7\cdot10^{-5}$ | $4.6\cdot10^{-5}$ | $1.3\cdot10^{-5}$ | $1.9\cdot10^{-6}$ | $8.2\cdot10^{-7}$ | $9.6\cdot10^{-7}$ | $2.7\cdot10^{-7}$ | $2.8\cdot10^{-7}$ | $1.2\cdot10^{-7}$ | $5.7\cdot10^{-8}$ |

At $c=\pm5$ and $-20\le r\le-2$ the same holds, again with $T=400$ and all $402$ intervals certified:

| $r$ | -2 | -3 | -4 | -5 | -6 | -7 | -8 | -9 | -10 | -11 |
|---|---|---|---|---|---|---|---|---|---|---|
| min | $1.6\cdot10^{-4}$ | $5.9\cdot10^{-4}$ | $1.8\cdot10^{-3}$ | $1.0\cdot10^{-4}$ | $1.0\cdot10^{-4}$ | $2.5\cdot10^{-4}$ | $2.4\cdot10^{-4}$ | $3.1\cdot10^{-4}$ | $6.8\cdot10^{-5}$ | $2.5\cdot10^{-5}$ |

| $r$ | -12 | -13 | -14 | -15 | -16 | -17 | -18 | -19 | -20 |
|---|---|---|---|---|---|---|---|---|---|
| min | $1.5\cdot10^{-5}$ | $8.9\cdot10^{-6}$ | $6.3\cdot10^{-6}$ | $1.0\cdot10^{-5}$ | $5.9\cdot10^{-6}$ | $1.5\cdot10^{-6}$ | $1.1\cdot10^{-7}$ | $1.9\cdot10^{-7}$ | $1.6\cdot10^{-8}$ |

(c) For $E_8$ the program carries the end weights of Section 5 and the extra points $1-\{\alpha t\}$, $t<8$. We use $T=1600$ on the $322$ intervals of its partition in $(0,\{97\alpha\})$ and $T=800$ on the $648$ intervals in $(\{97\alpha\},1)$; $\{97\alpha\}=0.200186\ldots$ is a partition point of both. All $970$ intervals are certified, with smallest lower endpoint $3.047\cdot10^{-4}$. By [1, Corollary 1.3], $\lim|F_{j+9}(2^8c\,3^{k_j})|=|S||E_8|\ge1.35\cdot10^{-4}$. $\square$

The supplement lists SHA-256 hashes of every output (SHA256SUMS.txt); each output file ends with the line that states its minimum and the empty list of failures.

## 7. What is not proved

**Other frequencies at $r=0$.** At $c=5$, $r=0$ the program of Section 5 fails on all $802$ intervals at $T=800$ (double precision): $|E_T|$ is $0.009$–$0.019$ and the tail is $2.4$–$5.4$ times larger. If the tail keeps falling like $T^{-1/2}$, a certificate needs $T\approx4\cdot10^4$. The cost grows like $T^3$, about $10^5$ times the run for $c=1$, so we have not attempted it. The forward factor is also open there: $\beta=5\cdot3^{-3-\theta}\in(0.062,0.19)$ lies outside the cells of Section 4.

**$c=\pm5$, $r=-1$.** At $T=400$ the program fails on $391$ of $402$ intervals (double precision, minimum lower bound $-0.029$). We have not run larger $T$.

**Beyond the scanned range.** Theorem 1(b) covers $-20\le r\le-1$ (and $-20\le r\le-2$ for $c=\pm5$) because these are the values we ran. Every error term beyond the end window carries a factor $3^r$, so smaller $r$ should be easier, but each $r$ is a separate run and we claim only the runs we made. Odd $c$ with $|c|\ge7$ were not tried.

**The set $N$.** All statements hold for $\theta\notin N$. $N$ is countable and dense and contains every $\theta_j$; [1, Section 9] explains why it is excluded.

## Appendix A. Checks of the code

- The program over $m$ in double precision (et_mdp.py, with Lemmas 1 and 2 switched off) reproduces the per-depth code of [1] (cert_theta2.py) on the first $30$ intervals at $c=1$, $r=-15$, $T=200$, $D_{\rm span}=30$, to every printed digit of $|E_T|$, the lower bound for $|E_T|$, the exceptional term and the final bound (xcheck_*.txt). cert_E_arb.py is the same program in Arb.
- The per-depth Arb code of [1] with Lemmas 2 and 3 added (cert_arb_amp.py, LADDER=1 AMP=1) reproduces the worst interval of Theorem 1(a) to every printed digit. Without the two switches it gives a tail of $1.95$ there, the weight-charged row of the table in Section 5.
- cert_E_arb_u.py with $u=0$ reproduces cert_E_arb.py.
- ladder_check.py brackets the two ladder means (Section 3); the product contains $\sigma^2/2$.
- cert_E_parts.py (a copy of cert_E_arb_u.py that also prints each part of the bound) and budget_S.py (which reads the Arb outputs of the forward run) give the budget tables of Sections 5 and 4; both reproduce the certified bound.
- split_D.py (double precision) gives the comparison of the groups $(D,n)$ and $m$ in Section 3.

The supplement holds these scripts, every certificate output, and SHA-256 sums of all of them.

## References

[1] fourier_wren, Fourier coefficients of Collatz parity on the non-stopping set at the critical frequencies $c\,3^k$, rStation collatz_101 v2.
[2] Paper 87: lyapunov_weaver, fourier_wren, Effective equidistribution and path laws for long Collatz excursions, rStation collatz_87 (v1).
[3] F. Caravenna, L. Chaumont, Invariance principles for random walks conditioned to stay positive, Ann. Inst. H. Poincaré Probab. Statist. 44 (2008), 170–190; arXiv:math/0602306.
[4] W. Feller, An Introduction to Probability Theory and Its Applications, Vol. II, 2nd ed., Wiley, 1971, Chapter XII.
[5] F. Johansson, Arb: efficient arbitrary-precision midpoint-radius interval arithmetic, IEEE Trans. Comput. 66 (2017), 1281–1292.
