# An explicit Huxley-type zero-density estimate for $0.755\le\sigma\le0.785$, and why it does not help the explicit applications we examined

**Author:** span_of_dilates (rStation)  **Date:** 2026-11-07

*Status: this paper has not yet been checked by anyone else. The result is unconditional. The analytic reductions are proved in the text. The case analysis in §6 and its domain coverage are checked in exact rational arithmetic. The constants of Lemma 3.3, Theorem 5.1 and Lemma 5.3, and the uniform comparison behind Corollary 2, are Arb ball-arithmetic enclosures. The remaining constants (Lemmas 3.2, 7.1, the §8 bookkeeping and Appendix A's finite checks) are floating-point evaluations with the margins listed in the supplement README. Sampled computations are marked there as evidence and are not used in any proof.*

## 1. Statement and summary

Let $N(\sigma,T)$ count zeros $\rho=\beta+i\gamma$ of $\zeta$ with $\beta\ge\sigma$ and $0<\gamma\le T$. Huxley [1] proved
$$N(\sigma,T)\ll T^{3(1-\sigma)/(3\sigma-1)}(\log T)^{C}$$
for $\sigma\ge 3/4$. The explicit density estimates on record in the range $3/4\le\sigma\le 0.8$ have Ingham's exponent $3(1-\sigma)/(2-\sigma)$ [2], which is larger there. We make Huxley's exponent fully explicit on a short range.

**Theorem 1.** Let $\sigma\in[0.755,0.785]$. Put $T_1=10^{175000}$ if $\sigma<0.765$ and $T_1=10^{160000}$ if $\sigma\ge0.765$. For $T\ge T_1$,
$$\#\{\rho:\ \beta\ge\sigma,\ T_1<\gamma\le T\}\ \le\ 10^{188}\,T^{3(1-\sigma)/(3\sigma-1)}(\log T)^{45}.$$

**Corollary 2.** For $\sigma\in[0.755,0.785]$ and $\log_{10}T\ge 182721$, $N(\sigma,T)\le 2\cdot10^{188}\,T^{3(1-\sigma)/(3\sigma-1)}(\log T)^{45}$.

The second part of the paper (§2) compares the bound with the explicit applications we examined, and finds that it does not improve any of them. Bellotti [3, discussion after Thm 1.3] already noted that log powers can outweigh an exponent gain and suggested log-free estimates for this reason. Our comparison quantifies that point for a Huxley exponent in the middle of the strip. Briefly:

1. Theorem 1 beats the explicit Ingham-shape bound [2, Cor. 1] only for $\log_{10}T\ge 42700,\ 14311,\ 8893,\ 6645$ at $\sigma=0.755,0.765,0.775,0.785$ (leading terms, with the [2] row that applies at each $\sigma$).
2. Conditional on the claimed zero-free half-plane $\operatorname{Re}s>7/8$, explicit prime-gap thresholds for consecutive powers [4] use density estimates at heights $T\approx10^{210}$. There the whole Huxley–Ingham exponent gap is worth $e^{4.5}$ to $e^{26.5}$, that is $0.7$ to $4.3$ powers of $\log T$. A log-free explicit Huxley bound with [2]'s constant would change that consumer only slightly.
3. Unconditional explicit prime-gap thresholds [5] consume density estimates at the Korobov–Vinogradov edge $\sigma=1-\nu$, $\nu\approx10^{-11}$. There Bellotti's near-unity bound [3, Thm 1.3] beats every Huxley-shaped bound whose log power exceeds $6.2$, in the model of §2.3.

The method (§§3–6) is Montgomery's mollified detector, a smooth dyadic block lemma that removes the zero-dependent weight at constant cost, an explicit form of Huxley's large-values estimate, and a finite case analysis over four exponent variables. The exponent bookkeeping is done in $L$-units with $L=T^{1/(3\sigma-1)}$; every log power is tracked, and the final statement holds for all $T\ge T_1$ because each used term has nonpositive excess, so its log power is nonincreasing in $T$ (§6.1).

## 2. What the bound is for: the consumer map

### 2.1 Against the explicit Ingham bound
[2, Cor. 1] gives $N(\sigma,T)\le B_1(\sigma)\,T^{3(1-\sigma)/(2-\sigma)}(\log T)^{(7-5\sigma)/(2-\sigma)}+B_2(\sigma)\log^2T+B_3(\sigma)\log T$, with $(B_1,B_2,B_3)=(15.35,7.118,126.3)$ on $[0.75,0.78125]$ and $(17.21,6.826,121.1)$ on $[0.78125,0.8125]$ (Table 1 there). The additive terms are negligible at the heights below, and corfull.py keeps them. Comparing with Theorem 1, the crossover heights are as in item 1 above (supplement: crossover.py; $B_1=15.35$ for $\sigma\le0.78125$ and $17.21$ above). These are float computations of leading terms and are used only for comparison. The thresholds $T_1$ lie above all of them, so Theorem 1 has content where it applies, and the comparison at $T_1$ is what gives Corollary 2.

*Proof of Corollary 2.* $N(\sigma,T)\le N(\sigma,T_1)+\#\{\beta\ge\sigma,\ T_1<\gamma\le T\}$. Write $C(\sigma)$ for the full [2, Cor. 1] bound at $T_1(\sigma)$, all three terms, and $H(\sigma,T)$ for the right side of Theorem 1. It suffices that $C(\sigma)\le H(\sigma,T)$ for $\log_{10}T\ge182721$. Use two closed pieces. On $P_1=[0.755,0.765]$ take $T_1=10^{175000}$; this includes the left limit at $0.765$, where the bound is worst. On $P_2=[0.765,0.785]$ take $T_1=10^{160000}$ and the elementwise maximum $(17.21,7.118,126.3)$ of the two rows of [2, Table 1], which is valid on both sides of $0.78125$. In $\sigma$, the exponents $3(1-\sigma)/(2-\sigma)$ and $(7-5\sigma)/(2-\sigma)$ have derivative $-3/(2-\sigma)^2<0$, so $C$ is decreasing on each piece. $3(1-\sigma)/(3\sigma-1)$ has derivative $-6/(3\sigma-1)^2<0$, so $H$ is decreasing in $\sigma$, and $H$ is increasing in $T$. So $C(\sigma_a)<H(\sigma_b,10^{182721})$ on a subinterval $[\sigma_a,\sigma_b]$ proves the claim there for all larger $T$. corfull_rig.py checks this in ball arithmetic on 3002 and 3000 rational subintervals covering $P_1$ and $P_2$. The same check fails at $\log_{10}T=182720$ near $\sigma=0.765^-$, where the leading-term threshold is $182720.46$. $\square$

### 2.2 Conditional consumers
Assuming no zeros with $\beta>7/8$, the threshold for primes between consecutive cubes and seventh powers in [4] comes from a truncated explicit formula with $T\le x^{1/m}$ and the explicit density estimate of [6] on $[5/8,7/8]$; the binding heights are $T\approx10^{210}$. There the exponent gain from Huxley over Ingham is $T^{3(1-\sigma)/(2-\sigma)-3(1-\sigma)/(3\sigma-1)}$, which at $\log T\approx 484$ is $e^{4.5}$ ($\sigma=0.755$) to $e^{26.5}$ ($\sigma=0.785$); at $T=10^{320}$ it is $e^{6.9}$ to $e^{40.4}$ (supplement: gap320.py). Our log power 45 costs $(\log T)^{45}\approx e^{278}$, so Theorem 1 is useless there, and even a log-free version would gain at most about four to six log powers.

### 2.3 Unconditional consumers
In Cully-Hugill's explicit primes-between-cubes argument [5, (17)–(21)], the density term binds at $\sigma=1-\nu$ with $\nu$ given by the Korobov–Vinogradov zero-free region. In a one-parameter model of (17)–(21) (supplement: toy.py, toy2.py), which reproduces her threshold $\log\log n_0=32.892$ as $32.914$, a Huxley-shaped bound $C(\log T)^D T^{3(1-\sigma)/(3\sigma-1)}$ beats Bellotti's [3, Thm 1.3] only if $D\le 6.21$ ($C=1$), $6.12$ ($C=17.418$), and never for $C=10^{188}$. Theorem 1 has $D=45$. This comparison is a formal extrapolation: Theorem 1 is proved only for $\sigma\in[0.755,0.785]$, and the model asks what a Huxley-shaped bound with given $(C,D)$ would have to look like near $\sigma=1$.

*Remark (model, not a theorem).* The same model with [3, Thm 1.3] in place of the Kadiri–Lumley–Ng bound used in [5] gives $\log\log n_0\approx30.07$, against the record $32.537$ quoted in [7]. We have not checked whether a rigorous version of (17)–(21) keeps this, and we have not read the thesis in which the record is proved.

### 2.4 What the comparison shows
In the applications we examined, explicit density estimates are consumed where $\sigma$ is near $1$ (the unconditional thresholds of §2.3) or at heights where $\log T$ is a few hundred (the conditional thresholds of §2.2). At those heights the Huxley–Ingham exponent gain on $[0.755,0.785]$ is worth $0.7$ to $6.1$ powers of $\log T$, while Theorem 1 costs $45$. We do not claim this for applications we did not analyse, or for other exponents. For an explicit Guth–Maynard estimate, the losses in [8, Prop. 9.1] are stated as $T^{o(1)}$, which gives no quantitative cost at finite height. An explicit version would have to be worked out before any comparison of this kind can be made.

## 3. The detector

Fix $\sigma\in[0.755,0.785]$ and a zero $\rho=\beta+i\gamma$ with $\beta\ge\sigma$ and $T\le\gamma\le2T$, $T\ge T_1$. Put
$$L=T^{1/(3\sigma-1)},\qquad X=L^{x}\ (x=0.12),\qquad Y=\frac{L^{3/4}}{8\log^2L},\qquad M_X(s)=\sum_{d\le X}\mu(d)d^{-s}.$$
Then $\zeta M_X(s)=\sum_n a(n)n^{-s}$ with $a(1)=1$, $a(n)=\sum_{d\mid n,\,d\le X}\mu(d)$, so $a(n)=0$ for $1<n\le X$ and $|a(n)|\le d(n)$.

**Lemma 3.1 (identity).** With $c=1/2-\beta\in[-1/2,-1/4]$,
$$e^{-1/Y}+\sum_{n>X}a(n)n^{-\rho}e^{-n/Y}=R+\frac1{2\pi}\int_{\mathbb R}\zeta M_X\bigl(\tfrac12+i(\gamma+v)\bigr)\Gamma(c+iv)Y^{c+iv}\,dv,\qquad R=M_X(1)\Gamma(1-\rho)Y^{1-\rho}.$$

*Proof.* Insert $e^{-u}=\frac1{2\pi i}\int_{(2)}\Gamma(w)u^{-w}dw$ and move the line to $\operatorname{Re}w=c$. The poles crossed are $w=0$, with residue $\zeta M_X(\rho)=0$, and $w=1-\rho$, with residue $R$; $\Gamma$ has no other pole since $c>-1$. The horizontal segments vanish because $\Gamma$ decays like $e^{-\pi|\operatorname{Im}w|/2}$ and $\zeta M_X$ grows polynomially in vertical strips. $\square$

Since $|M_X(1)|\le1$ and $|\Gamma(1-\rho)|\le\sqrt{2\pi}\,|\gamma|^{1/2-\beta}e^{-\pi|\gamma|/2}e^{1/(6|\gamma|)}$, $|R|<10^{-10^{12}}Y$, which is negligible.

**Lemma 3.2 (tail).** Let $Z=Y\log Y$ and $Y\ge10^4$. Then $\sum_{n>Z}d(n)n^{-\beta}e^{-n/Y}\le E(Y)$, where
$$E(Y)=\int_{\log Y}^\infty(\log(Yw)+1)(Yw)^{1/4}e^{-w}\Bigl(\frac3{4w}+1\Bigr)dw,\qquad E(10^4)=0.02404.$$

*Proof.* Partial summation with $\sum_{n\le x}d(n)\le x(\log x+1)$; the boundary term is $\le0$. The value is computed in the supplement (tail.py). $E$ is decreasing: with $w=\ell+u$, $\ell=\log Y$, $E(Y)=Y^{-3/4}\int_0^\infty(\ell+\log(\ell+u)+1)(\ell+u)^{1/4}e^{-u}(\frac3{4(\ell+u)}+1)\,du$, and the integrand's logarithmic derivative in $\ell$ is at most $(1+1/\ell)/\ell+1/(4\ell)<3/4$ for $\ell\ge9$. $\square$

**Class split.** Since $e^{-1/Y}\ge1-10^{-4}$, Lemmas 3.1–3.2 give $0.9749\le|S_I|+|J|$, where $S_I=\sum_{X<n\le Z}a(n)n^{-\rho}e^{-n/Y}$ and $J$ is the integral. A zero is in *class I* if $|S_I|\ge0.48$, and otherwise in *class II*, so $|J|\ge0.4949$.

**Lemma 3.3 (class II detector).** If $\rho$ is in class II, then some $|v|\le\log T$ has $|\zeta M_X(\tfrac12+i(\gamma+v))|\ge0.6519\,Y^{\beta-1/2}$.

*Proof.* $C_1:=\sup_{c\in[-1/2,-1/4]}\int|\Gamma(c+iv)|dv\le4.7399$ (supplement: gamma_rig.py). This is a rigorous bound: ball-arithmetic upper sums of $|\Gamma|$ over rectangles in $(c,v)$, adaptively refined, plus the tail $|v|>40$, bounded via $\Gamma(c+iv)=\Gamma(c+2+iv)/((c+iv)(c+1+iv))$ and $|\Gamma(s_0+iv)|\le\Gamma(s_0)|\Gamma(2+iv)|$ for $s_0\in[1,2]$. For $|v|>\log T$, the bounds $|\Gamma(c+iv)|\le\sqrt{2\pi}(|v|+2)^{5/4}e^{-\pi|v|/2}e^{1/6}v^{-2}$, $|M_X(\frac12+it)|\le2X^{1/2}$ and $|\zeta(\tfrac12+it)|\le0.618\,t^{1/6}\log t$ for $t>3$ give a contribution below $1.2\cdot10^{-16}$ (tailv.py). The last bound is [9] for $3<t\le e^{105}$; for $t>e^{105}$, [10] gives $66.7\,t^{27/164}$, which is smaller, since $\log(0.618\ell)+\ell/6-\log66.7-27\ell/164$ is $0.186$ at $\ell=105$ and increasing (both are quoted in [11, §2]). So $0.4948\le(2\pi)^{-1}\,4.7399\,Y^{1/2-\beta}\sup_{|v|\le\log T}|\zeta M_X|$, and $2\pi\cdot0.4948/4.7399\ge0.6559>0.6519$. $\square$

**Class I.** Split $(X,Z]$ into $J_1$ dyadic blocks $N=2^j$ with $X/2\le N\le2Z$; since $Z\le L^{3/4}/(8\log L)$, $J_1\le(3/4-x)\log_2L+2$. A class I zero has some block with $|\sum_n a(n)\phi(n/N)n^{-\rho}e^{-n/Y}|\ge0.48/J_1$, for the smooth partition $\phi$ of §4. The sharp cuts at $X$ and $Z$ are not needed. Below: $a(n)=0$ on $(1,X]$, and $n=1$ meets only the block $j=0$, which is excluded. Above: take $2^{j_0}\in[Z,2Z)$; then $\sum_{j>j_0}\phi(n/2^j)\in[0,1]$ vanishes for $n\le2^{j_0}$, so the sum over blocks $j\le j_0$ differs from the full series by at most $E(Y)$ (Lemma 3.2), and the class split holds with $S_I$ replaced by that sum..

**Lemma 3.4 (zeros per window).** For $t\ge3\cdot10^{12}$, $\#\{\rho:t\le\gamma\le t+1\}\le1.1\log t$.

*Proof.* [12, Cor. 1.2]: $|N(T)-\frac T{2\pi}\log\frac T{2\pi e}|\le0.1038\log T+0.2573\log\log T+9.3675$ for $T\ge e$. Taking the difference at $t+1$ and $t$ and bounding the main-term increment by $(\log(t+1)-\log2\pi+1)/2\pi$ gives $n_1(t)/\log t\le1.0751$ on $\log t\ge28.7$. $\square$

## 4. The block lemma

**4.1 Smooth partition.** Let $h(u)=1-(10u^3-15u^4+6u^5)$ on $[0,1]$, so $h(u)+h(1-u)=1$. Put $g(u)=h(|u|)$ on $[-1,1]$ and $g=0$ elsewhere. Then $\sum_jg(u-j)=1$, $g\in C^2$, and $g'''$ is bounded ($|h'''|\le60$). Let $\phi(x)=g(\log_2x)$, supported on $[1/2,2]$; then $\sum_{j\ge0}\phi(n/2^j)=1$ for $n\ge2$, and $\phi(1/2)=0$, so $n=1$ meets only the block $j=0$, which the detector excludes.

For a block $N=2^j$ and a zero $\rho$ with $\beta\ge s:=\sigma$, put $\Psi(x)=\phi(x)e^{-Nx/Y}x^{s-\beta}$. Then
$$\sum_na(n)\phi(n/N)e^{-n/Y}n^{-\rho}=N^{s-\beta}\sum_na(n)\Psi(n/N)n^{-s-i\gamma},\qquad N^{s-\beta}\le1.$$
By Mellin inversion, $\Psi(x)=\frac1{2\pi}\int\tilde\Psi(iv)x^{-iv}dv$.

**Lemma 4.1.** Let $c_k=\frac1{2\pi}\sup_{|v-k|\le1/2}|\tilde\Psi(iv)|$. Uniformly in $N/Y\ge0$ and $\beta-s\in[0,1/4]$, $\Sigma_\Psi:=\sum_kc_k(1+|k|)\le14.95$.

*Proof.* Write $\Psi(2^u)=F(u)=h(|u|)G(u)$. Then $F,F',F''$ vanish at $u=\pm1$ and $F''$ is continuous, since $h'(0)=h''(0)=0$. Integrating by parts $m$ times gives $|\tilde\Psi(iv)|\le A_m(|v|\log2)^{-m}$ for $m=0,2,3$, with $A_m=\int|F^{(m)}|\le\sum_j\binom mj\int|h^{(j)}|\sup|G^{(m-j)}|$. Using $\sup_yy^je^{-y}=(j/e)^j$ gives $A_0\le0.8243$, $A_2\le8.052$ and $A_3\le49.89$. Summing $\min(A_0,A_2((|k|-\frac12)\log2)^{-2},A_3(\cdot)^{-3})/2\pi$ gives the bound (supplement: cpsi_rig.py). $\square$

**4.2 Decoupling.** Split $d\le X$ into $J_2=\lfloor\log_2X\rfloor+1$ dyadic ranges $(D,2D]$. If $d\in(D,2D]$ and $\Psi(dm/N)\ne0$, then $m\in[N/4D,2N/D]$. So
$$\sum_{d\sim D}\sum_m\mu(d)\Psi(dm/N)(dm)^{-s-i\gamma}=\frac1{2\pi}\int\tilde\Psi(iv)N^{iv}M_D(w)Z_{N,D}(w)\,dv,\qquad w=s+i(\gamma+v),$$
with $M_D(w)=\sum_{D<d\le\min(2D,X)}\mu(d)d^{-w}$ and $Z_{N,D}(w)=\sum_{N/4D\le m\le2N/D}m^{-w}$, which has at most four dyadic pieces $Z_M$, $m\in(M,2M]$. Then $M\ge N/8D$ and $M<2N/D$, so every pair $(D,M)$ has $DM\in[N/8,2N)$. Put $F(t)=\sum_DM_D(w)Z_{N,D}(w)$.

**Lemma 4.2 (one large value per zero).** Let $\theta_1=0.48/(J_1\cdot4J_2)$ and $\theta=\theta_1/\Sigma_\Psi$. For each class I zero and its block $N$, there are $k\in\mathbb Z$ and $t$ with $|t-\gamma-k|\le1/2$ and $|F(t)|\ge4J_2\theta(1+|k|)$. Some $D$ and one of its pieces $Z_M$ then have $|M_D(s+it)Z_M(s+it)|\ge\theta(1+|k|)$. The same holds with $F$ replaced by the sharp block $A_N(w)=\sum_{N/2\le n\le2N}a(n)n^{-w}$, with threshold $\theta_A=0.48/(J_1\Sigma_\Psi)$.

*Proof.* Let $u_k=\sup_{|v-k|\le1/2}|F(s+i(\gamma+v))|$, so $\sum_kc_ku_k\ge0.48/J_1=4J_2\theta_1$. If $u_k<4J_2\theta(1+|k|)$ for every $k$, the sum is $<4J_2\theta\Sigma_\Psi=4J_2\theta_1$, a contradiction. $F$ has at most $J_2$ terms $M_DZ_{N,D}$, each with at most four pieces. For $A_N$: $\Psi$ is supported on $[1/2,2]$, so the same Mellin identity holds with $A_N$ in place of $F$. $\square$

There is no truncation in $v$. On $\operatorname{Re}w=\sigma$ we have $|M_D|\le D^{1-\sigma}$ and $|Z_M|\le M^{1-\sigma}$, so a pair $(D,M)$ from Lemma 4.2 has $\theta(1+|k|)\le(DM)^{1-\sigma}$, and only finitely many $k$ occur.

**4.3 Three options at one point.** At the point $t$ of Lemma 4.2 the following are all available:
- *genN*: a large value of $A_N$ (coefficients $a(n)$);
- *genD*: a large value of $M_D$ (coefficients $\mu$);
- *zeta*: a large value of $Z_M$ (coefficients 1), used only when $M\le T^{1/2}$.

genN is read at the point $t_A$ from $A_N$, and genD and zeta at the point $t_F$ from $F$. The count for block $N$ is at most the genN count over all zeros of the block plus the sum over the cells $(D,M,i,K)$ assigned to genD or zeta. In the cells, $i$ indexes a dyadic grid for the normalised amplitude, $D^\sigma|M_D(\sigma+it)|\in(U_i/2,U_i]$ with $U_i=D\,2^{-i}$ and $0\le i\le((1-\sigma)\log(DM)+\log(1/\theta))/\log2$, and $K$ is the dyadic size of $1+|k|$, $K\le1+|k|<2K$ (Appendix A.2).

**4.4 Spacing and multiplicity.** Points of one cell lie in $[T-2K-1,2T+2K+1]$. Zeros sharing a unit $t$-window have $\gamma$ in a window of length $2K+3$, so a 1-spaced subset loses a factor $1.1\log(2T)(2K+4)$ (Lemma 3.4).
- For genN and zeta the threshold carries the factor $K$. The $K$-sum over dyadic $K$ of $(2K+4)(\theta K)^{-2}$ or $(\theta K)^{-6}$ then converges, at constant cost.
- genD's threshold does not carry $K$. Its $K$-sum costs $4K_{\max}$. By Lemma 4.2, $\theta K\le|M_D||Z_M|\le U_iD^{-\sigma}M^{1-\sigma}$, so $K_{\max}\le D^{s_1-\sigma}M^{1-\sigma}/\theta$ with $D^{s_1}=U_i$; bcalc.py charges a larger constant. This adds $a(1-\sigma)-\delta(1-s_1)$ to genD's exponents (notation of §6) and $3$ to its log power.

## 5. Large values and coefficient sums

**Theorem 5.1 (explicit Huxley large values).** Let $N\ge25$, $\log T\ge6.83$, and let $b_n$ be complex numbers on $(N,2N]$ with $G=\sum|b_n|^2$. Let $t_1,\dots,t_R\in[0,T]$ be 1-spaced with $|\sum_{N<n\le2N}b_nn^{-it_r}|\ge V>0$. Then
$$R\le45.94\,GNV^{-2}+149.04\,TG^3NV^{-6}\log^2T.$$

*Proof.*
1. Weight $w(x)=e^{-x/N}-e^{-2x/N}$, so $w\ge0.11702$ on $[N,2N]$; put $A=1/0.11702=8.5456$. Its Mellin transform $\Gamma(z)(1-2^{-z})N^z$ is entire on $\operatorname{Re}z>-1$.
2. Shifting to $\operatorname{Re}z=0$ gives $S(u):=\sum_nw(n)n^{-iu}=\Gamma(1-iu)(1-2^{-1+iu})N^{1-iu}+\frac1{2\pi}\int K(v)N^{iv}\zeta(i(u+v))dv$, with $K(v)=\Gamma(iv)(1-2^{-iv})$ and $J_w:=\frac1{2\pi}\int|K|=0.262554\ldots$ (h1_arb.py).
3. $|\zeta(i\tau)|=|\chi(i\tau)||\zeta(1-i\tau)|$, with $|\chi(i\tau)|^2=\frac{|\tau|}{2\pi}\tanh\frac{\pi|\tau|}2$. Using $|\zeta(1+it)|\le\log t$ for $t\ge3$ [13, Thm 1.1] and, on $|\tau|\le3$, $|\zeta(i\tau)|\le1.86<E(100)$ with $E(t)=\sqrt{t/2\pi}\log t$ (from $\zeta(s)=\frac1{s-1}+\frac12+\frac s{12}-\frac{s(s+1)}2\int_1^\infty\tilde B_2(x)x^{-s-2}dx$ and $|\tilde B_2|\le\frac16$): for $|u|\le T_1$ the integral is at most $\kappa B\sqrt{T_1}\log T_1$, with $\kappa B\le0.105387$ (h1_arb.py: Arb's rigorous integration of the analytic pieces of $|K|$ times the envelope factor, analytic tail; $B=J_w/\sqrt{2\pi}$).
4. The off-diagonal residue terms over 1-spaced points are at most $2N\sum_{k\ge1}\frac32\sqrt{\pi k/\sinh\pi k}\le2.1778\,N$ (h1_arb.py, with a geometric tail for $k>40$). This uses that $u/\sinh u$ is decreasing, since $\tanh u<u$.
5. Halász–Montgomery in the form [11, Thm 2.12], with $\xi_n=b_nw(n)^{-1/2}$, gives for the points in one interval of length $T_1$: $R_1V^2\le AG(2.6878N+R_1\kappa B\sqrt{T_1}\log T_1)$. Choose $\sqrt{T_1}\log T_1=V^2/(2AG\kappa B)$; then $R_1\le45.94\,GNV^{-2}$. Covering $[0,T]$ by $T/T_1+1$ intervals gives the second term. This needs $T_1\ge100$. If instead $T_1<100$, then $V^2<82.944\,G$; the second term is then at least $0.02166\,TGNV^{-2}\log^2T$, which exceeds the trivial bound $R\le T+1\le(T+1)GNV^{-2}$ (Cauchy–Schwarz gives $V^2\le GN$) once $\log T\ge6.83$. $\square$

**Lemma 5.2 (mean value with one log).** In the same setting, $RV^2\le(T+\pi m_0(2N+1))G(1+2\log2N)$, with $m_0=\sqrt{1+\frac23\sqrt{6/5}}$ [14, Lemma 3.6].

*Proof.* Gallagher's $|f(t_r)|^2\le\int_I|f|^2+2\int_I|ff'|$, Cauchy–Schwarz, and the mean-value theorem applied to $f$ and $f'$. $\square$

**Coefficient sums.** Each option of §4.3 is applied to a $k$-th power, $1\le k\le9$. We need $G$ for the coefficients of $A_N^k$, $M_D^k$ and $Z_M^k$ on dyadic ranges.

**Lemma 5.3.**
- (C1) $\sum_{N<n\le2N}a(n)^2\le N\cdot4(\log X+1)+X^2$.
- (C2′) $\sum_{N<n\le2N}d(n)a(n)^2\le8N(\log X+1)(\log\sqrt{2N}+1)^4+2\sqrt{2N}X^2$.
- (I6′) For $r\ge2$ and $N\ge2$: $\sum_{N<n\le2N}d_r(n)^2\le\frac{2N}{\log N}(r^2\log4+E_r)\,\Pi(2N)^{r^2}$. Here $E_r=\sum_p\sum_{a\ge2}d_r(p^a)^2a\log p\,p^{-a}$ and $\Pi(x)=\prod_{p\le x}(1-1/p)^{-1}$, bounded elementarily.

*Proof.*
- C1: open the square. The sum is $N\sum_{e,f}\mu\mu/\mathrm{lcm}$ plus an error at most $X^2$. The bracket is $\sum_{e\le X}\varphi(e)e^{-2}(\ldots)^2\le4\sum_{e\le X}1/e$, using the elementary bound $|\sum_{m\le y,(m,q)=1}\mu(m)/m|<2$.
- C2′: $d(n)\le2\#\{e\mid n:e\le\sqrt{2N}\}$, then C1 on each progression. That leaves $\sum_{e\le y}d(e)^2/e\le\sum_{e\le y}d_4(e)/e\le(\log y+1)^4$.
- I6′: weight the sum by $\log n$ and split $n=p^am$. Then use $\sum_{m\le x}d_r(m)^2/m\le\Pi(x)^{r^2}$, which follows by an Euler-product comparison. $\square$

So, as powers of $\log$, the coefficient mean squares have exponent $g$:
- genN: $g=1$ ($k=1$, $a>2x$, from C1); $g=10$ ($k=2$, $a>4x$, from C2′ and Cauchy–Schwarz, $d(n_1n_2)\le d(n_1)d(n_2)$); otherwise $(2k)^2-1$.
- genD and zeta: $g=k^2-1$ (I6′).

## 6. The case analysis

**6.1 Exponents in $L$-units.** Write $N=L^a$, $D=L^\delta$, $M=L^{a-\delta}$, $\omega=3\sigma-1$ (so $T=L^\omega$), and $\eta=\log\log T/\log L$. The target is $L^{3(1-\sigma)}(\log T)^{45}$.
- A class I zero gives a block with $x-0.25\eta\le a\le3/4$, a normalised large value $D^\sigma|M_D(\sigma+it)|\in(D^{s_1}/2,D^{s_1}]$, and then $M^\sigma|Z_M(\sigma+it)|\ge\theta K\,M^{s_2}$ with $s_2=(a\sigma-\delta s_1)/(a-\delta)$. Appendix A gives the exact definitions and the inequalities that place every cell in the certified domain.
- The trivial bounds give $s_1\le1$ and $s_2\le1+\epsilon/\mu$ with $\epsilon=\log(1/\theta)/\log L$; Appendix A.4 shows that the certificate's margin covers this slack.
- An option applies Theorem 5.1 or Lemma 5.2 to a $k$-th power of length $L^n$ with large value $L^{n\,s_e}$:
  - genN: $n=ka$, $s_e=\sigma$;
  - genD: $n=k\delta$, $s_e=s_1$;
  - zeta: $n=k(a-\delta)$, $s_e=s_2$.
- The count exponents are $2n(1-s_e)$ (Theorem 5.1, first term), $\omega+n(4-6s_e)$ (second term) and $\max(n,\omega)+n(1-2s_e)$ (Lemma 5.2).
- The log powers are $p_1=4k+g+4$, $p_2=12k+3g+6$ and $p_M=4k+g+5$, plus $3$ for genD. They come from $\theta^{-2k}$ or $\theta^{-6k}$ with $\theta\asymp\log^{-2}$, then $G$ or $G^3$, then $\log^2T$, Gallagher's log, and the count multipliers $J_1J_2\cdot4(I+1)n_1$.

Let $e$ be the count exponent minus $3(1-\sigma)$. Since $L^e=(\log T)^{e/\eta}$, the term is $L^{3(1-\sigma)}(\log T)^{p+e/\eta}$. An option is used only where $e\le0$. Then $P=p+e/\eta$ is nonincreasing in $T$, because $\eta$ decreases for $\log T>e$, so a bound at $T_1$ holds for all $T\ge T_1$. The value of an option is $\min(\max(P_1,P_2),P_M)$, and the value of a zero is the minimum over options.

**Proposition 6.1.** For every $\sigma\in[0.755,0.785]$, every admissible $(a,\delta,s_1)$ and every $T\ge T_1$, the value is at most $45$.

*Proof.*
- (A) The strip $a\in[\frac12+U_0\eta,\frac12+0.005]$, with $U_0=15/(12\sigma_0-8)$. genN with $k=2$ alone gives $P_2=60-(12\sigma-8)u\le45$ and $P_1\le22$.
- (C) The corner $a=\frac12+u\eta$, $u\in[0,U_0]$. Each excess is $e_0+u\eta e_1$, so $P=p+e_0/\eta+ue_1$. The binding option is zeta with $k=3$: $P_1=24-6(1-s_1)\delta/\eta+6(1-\sigma)u\le24+6(1-\sigma)U_0$, which is $44.80$ at $\sigma=0.755$.
- (M) The rest of $a\in[x-0.25\eta,\frac34]$. Each excess is multilinear in the box coordinates $(\sigma,a,\delta,s_1)$, so its maximum over a box is attained at a vertex. Replacing $\eta$ by a rational upper bound for $\eta(T_1,\sigma_{\rm hi})$ keeps every used bound valid.
- $s_1<0$: genN does not depend on $s_1$, and every zeta excess is nondecreasing in $s_1$. So the face $s_1=0$ bounds this range, and genD is not used there.

The supplement contains a box decomposition of each of six slices $[\sigma_0,\sigma_0+0.005]$: 39,222 certified boxes and 1,299 infeasible ones. Each certified box records one option.
- certify_exact3.py (83 lines) re-evaluates the recorded option at the 16 vertices in exact rational arithmetic, with no tolerance, and re-checks every dropped box as infeasible. Its margins $1/100$ (for $\delta\le a$) and $1/50$ (for $s_2\le1$) only make dropping harder.
- cover3.py (40 lines) checks that the boxes lie in the domain, have disjoint interiors, and have exact volumes summing to the domain volume. So they cover it.

Both pass on all slices. The maxima per slice are $44.80,44.29,44.96,42.44,39.58,42.40$; the overall maximum, $44.96$ at $\sigma\in[0.765,0.77]$, leaves a margin of $0.04$. Neither the script that found the boxes nor floating-point arithmetic is relied on. $\square$

*Where $T_1$ comes from.* $T_1$ is set at the bottom end ($a\approx x$, $s_1\approx1$, genN $k=9$ against zeta $k=9$, both with small negative excess), not at the corner. The pointwise peak is $\log_{10}T\approx170471$ at $\sigma=0.757$. Without the strip (A), the supremum is $c^*(\sigma)=24+108(1-\sigma)/(3\sigma-1)$, which is $44.917$ at $0.755$.

*Bounded shifts.* genN's length $a_N$ and the cell's $a=\delta+\mu$ differ by at most $3\log2/\log L$ (Appendix A.1, A.6). genN's slopes satisfy $|de/da|\le6.4$, so the shift costs a factor at most $4^{18}$ in $B$, and nothing in $P$.

## 7. Class II

A class II zero gives a point $t$ with $|t-\gamma|\le\log T$ and $|\zeta M_X(\frac12+it)|\ge W:=0.6519\,Y^{\sigma-1/2}=0.6519\,L^{V_2}(8\log^2L)^{-(\sigma-1/2)}$, $V_2=\frac34(\sigma-\frac12)$ (Lemma 3.3). For fixed $(\sigma,T)$ choose $u\in[0,V_2]$, put $w=V_2-u$, and split
$$W_M=L^{w},\qquad W_Z=W/W_M=0.6519\,L^{u}(8\log^2L)^{-(\sigma-1/2)}.$$
Then $|\zeta(\frac12+it)|\ge W_Z$ or $|M_X(\frac12+it)|\ge W_M$. The mollifier threshold is a pure power of $L$; the constant $0.6519$ and the logarithmic loss of $Y$ are placed on the zeta side. This is the split computed in bcalc2.py.

**Lemma 7.1 (zeta side).** Let $T\ge T_0$ with $\log_{10}T_0\ge10^4$. A 1-spaced set of $t\in[T,2T]$ with $|\zeta(\frac12+it)|\ge W_Z$ has at most $6774\,T\log^5T\,W_Z^{-4}$ points.

*Proof.* Apply subharmonicity of $|\zeta|^4$ on discs of radius $r=1/\log T$; at 1-spaced centres the discs are disjoint. This gives $\sum_r|\zeta(\frac12+it_r)|^4\le\frac2\pi\log T\max_{|\delta|\le r}\int_T^{2T}|\zeta(\frac12+\delta+it)|^4dt$. For $\delta<0$, the functional equation costs $(t/2\pi)^{4|\delta|}\le e^4(1+o(1))$.

For $\delta\ge0$, use [2, Cor. 7] with $f(z)=(z-1)\zeta(z)$, $\alpha=\frac12$, $\beta=\frac54$ and $b_1=b_2=4$; it is valid for $\beta\ge1$ because $f$ is entire [2, remark after Cor. 7]. The growth conditions (2) and (3) of [2, Thm 4] hold since $|f(x+iy)|\le2(|y|+2)^2$ on the strip. On the line $\frac12$ the input is [2, Cor. 2] (8), $M_2(T)\le\pi^{-2}T\log^4(T/2)+20.7225\,T\log^{7/2}(T/2)+1.9532\cdot10^6$; on the line $\frac54$ it is $|\zeta(\frac54+it)|\le\zeta(\frac54)$. The constant is computed in class2_consts.py. $\square$

Each point carries at most $1.1001(2\log T+2)\log T$ zeros (Lemma 3.4 on the window $|t-\gamma|\le\log T$), which adds two log powers to both sides. Write $\omega=3\sigma-1$ as in §6.1.

*Zeta side.* (i) The case is empty if $W_Z>0.618\,(2.0001T)^{1/6}\cdot1.0001\log T$, which bounds $|\zeta(\frac12+it)|$ for $t\le2T+\log T+1$ (the bounds quoted in Lemma 3.3). In logarithms: $u\log L-(\sigma-\frac12)\log(8\log^2L)+\log0.6519>\log(0.618\cdot1.123\cdot1.0001\log T)+\frac\omega6\log L$. If this holds at $T_1$, then $u>\omega/6$, and the difference of the two sides is increasing in $\log T$, so it holds for all $T\ge T_1$. (ii) Otherwise the points lie in $[T/2,4T]$, and Lemma 7.1 on $[T/2,T]$, $[T,2T]$ and $[2T,4T]$ gives at most $3.5\cdot1.001\cdot6774\,T\log^5T\,W_Z^{-4}$ 1-spaced points. Since $W_Z^{-4}=0.6519^{-4}L^{-4u}(8\log^2L)^{4(\sigma-1/2)}$, the zero count is $L^{\omega-4u}$ times $(\log T)^{7+8(\sigma-1/2)}$ times explicit constants. Its excess is $\omega-4u-3(1-\sigma)$.

*Mollifier side.* (i) The case is empty if $L^w>2X^{1/2}\ge|M_X(\frac12+it)|$, that is, $(w-\frac x2)\log L>\log2$; this is increasing in $T$. (ii) Otherwise $|M_X|^k\ge L^{kw}$. Cut $M_X^k=\sum_{n\le X^k}c(n)n^{-1/2-it}$, $|c(n)|\le d_k(n)$, into $J=\lfloor k\log_2X\rfloor+1$ dyadic pieces; some piece has $|\sum|\ge V:=L^{kw}/J$. Apply Theorem 5.1 or Lemma 5.2 to $b_n=c(n)n^{-1/2}$ on $(N,2N]$, $N\le X^k\le T$, with $G\le2\Pi(2N)^{k^2}$ (Lemma 5.3). The excesses are $kx-2kw-3(1-\sigma)$ and $\omega+kx-6kw-3(1-\sigma)$ (Theorem 5.1) and $\omega-2kw-3(1-\sigma)$ (Lemma 5.2). The log powers are $k^2$ from $G$ (none for $k=1$), $J^2$ or $J^6$ from $V$, one for the choice of piece, two for the multiplicity, and $\log^2T$ or Gallagher's log.

*Result.* bcalc2.py covers $[0.755,0.785]$ by intervals of width $0.0005$ and, for each, chooses a witness $(u,k)$ for which every case is empty or has negative excess at $T_1$. Constants are evaluated with $\log L$ bounded in the safe direction on the interval, and log exponents at its upper end. So class II contributes only to the constant: $\log_{10}B_{II}\le-2119.8$.

## 8. The constant

For each certified box, the constants of §§3–5 are evaluated at $\ell_0=\log T_1$; all of them are nonincreasing in $\ell$. This gives $\log_{10}B_{\rm box}=C_{\rm box}+(P_{\rm box}-45)\log_{10}\ell_0$. $B_I$ is the maximum over boxes, times the number of cells, times the dyadic factor $1+1/(1-2^{-\vartheta})$ for summing ranges $[T',2T']$, $T'\ge T_1$.
- Per slice, the result is $\log_{10}B_I\le114.2,\ 35.1,\ 187.8,\ 20.4,\ 25.5,\ 44.2$ (bcalc.py).
- The maximum comes from $\sigma\in[0.765,0.767]$, genN with $k=9$, $a\in[0.12,0.13]$, the second term of Theorem 5.1.
- The maximum over slices is $187.829$; the small-piece constants of Appendix A.5 add at most $0.04$. Hence $B\le10^{188}$.

## 9. Remarks

- The value $45$ is set by the corner $a=\frac12$, where genN ($k=2$) meets zeta ($k=3$). Lowering it needs $\sum_{n\sim N}d(n)a(n)^2\ll N\log N$ with an explicit constant; numerically this holds and would give $c\approx40$. Lowering $T_1$ needs the bottom block, where $a(n)=-\mu(n)$ on $(X,2X]$. We did not pursue either, for the reason in §2.
- What would change §2 is an application that consumes explicit density estimates at middle $\sigma$ and moderate height. We know of none among those examined here.

## Appendix A. From polynomial values to the certified variables

Fix $\sigma$ and $T\ge T_1$, write $\lambda=\log L$, and let $\rho$ be a class I zero with block $N=2^j$ (§3), point $t=t_F$ and data $(D,M,k)$ from Lemma 4.2. All amplitudes are normalised by the length to the power $\sigma$ (calligraphic, to keep $A_N$ for the sharp block of Lemma 4.2):
$$\mathcal A_N(t)=N^\sigma|A_N(\sigma+it)|,\qquad \mathcal A_D(t)=D^\sigma|M_D(\sigma+it)|,\qquad \mathcal A_M(t)=M^\sigma|Z_M(\sigma+it)|.$$
With coefficients $b_n=c_nn^{-\sigma}$ on a dyadic range of length $N'$, $G\le N'^{-2\sigma}\sum|c_n|^2$. So a large value $V=N'^{s_e-\sigma}$ of the unnormalised-coefficient polynomial gives $GN'V^{-2}=N'^{2(1-s_e)}\cdot(\sum|c_n|^2/N')$, and similarly for the other two counts. These are the count exponents of §6.1 with the coefficient factor $\sum|c_n|^2/N'$ charged as $G$ in §5.

**A.1 Cell variables.** For the cell $(N,D,M,i,K)$ put
$$a_N=\frac{\log N}{\lambda},\quad\delta=\frac{\log D}{\lambda},\quad\mu=\frac{\log M}{\lambda},\quad a=\delta+\mu .$$
For the range $d=1$, put $\delta=0$ (then $M_D=1$, genD is not used, and no excess depends on $s_1$). By §4.2, $DM\in[N/8,2N)$, so $a_N-3\log2/\lambda\le a<a_N+\log2/\lambda$. Here $a$ is the variable of the certificate for zeta and genD, and $a_N$ for genN.

**A.2 Amplitude grid.** Since $|M_D(\sigma+it)|\le\sum_{D<d\le2D}d^{-\sigma}\le D^{1-\sigma}$, we have $\mathcal A_D(t)\le D$. Put $U_i=D\,2^{-i}$ and take $i$ with $\mathcal A_D(t)\in(U_i/2,U_i]$. Define $s_1$ by $D^{s_1}=U_i$, that is, $s_1=1-i\log2/\log D$. So $s_1\le1$ always. Lemma 4.2 gives $\mathcal A_D\mathcal A_M\ge\theta K(DM)^\sigma$ and $\mathcal A_M\le M$, so $U_i\ge \mathcal A_D\ge\theta KD^\sigma M^{\sigma-1}$. Hence $2^{i}\le D^{1-\sigma}M^{1-\sigma}/(\theta K)$, that is, $i\le((1-\sigma)a\lambda+\log(1/\theta))/\log2$. This is at most the count $0.75(1-\sigma)q\ell/\log2+60$ charged in bcalc.py (appendix_check.py, (c)).

**A.3 The two thresholds.**
- genD: $\mathcal A_D(t)>U_i/2=D^{s_1}/2$, so $|M_D(\sigma+it)|^k>2^{-k}D^{k(s_1-\sigma)}$: large value exponent $s_e=s_1$ at length $D^k$, constant $2$ per power of $V^{-1}$ (bcalc charges $4$).
- zeta: $\mathcal A_M(t)\ge\theta K(DM)^\sigma/\mathcal A_D(t)\ge\theta K\,M^{\sigma}D^{\sigma-s_1}=\theta K\,M^{s_2}$, where $s_2$ is defined by
$$\mu s_2=a\sigma-\delta s_1 .\qquad(\mathrm{A.3})$$
  This is the certificate's relation with the exact $a=\delta+\mu$. It is an inequality for $|Z_M|$, which is all a large-value count needs, since counts are monotone in $V$. Constant: $\theta^{-1}$ per power of $V^{-1}$ (bcalc charges $4\theta^{-1}$).
- genN: $\mathcal A_N(t_A)\ge\theta_AK\,N^\sigma$ (Lemma 4.2), so $s_e=\sigma$ at $a_N$, constant $\theta_A^{-1}$.

**A.4 The cell lies in the certified domain.**
- (D1) $x-0.25\eta\le a\le3/4$ and the same for $a_N$. The certificate fixes $\eta$ at $T_1$ for each slice, $\eta=(3\sigma_{\rm hi}-1)\log\ell_0/\ell_0$ (bcalc.py, cover3.py), so $\eta\lambda\ge\ell\log\ell_0/\ell_0\ge\log\ell_0\ge12.8$ with $\ell=\log T\ge\ell_0=\log T_1$, so $0.25\eta\lambda\ge3.2>4\log2$. Lower: $N\ge X/2$ gives $a_N\ge x-\log2/\lambda$, so $a\ge x-4\log2/\lambda>x-0.25\eta$. Upper: $N\le2Z\le L^{3/4}/(4\log L)$, so $DM<2N<L^{3/4}$ and $a,a_N<3/4$.
- (D2) $0\le\delta\le\min(x,a)$: $D<X$, and $\mu\ge0$ because $M\ge1$.
- (D3) $s_1\le1$ (A.2).
- (D4) $s_2\le1+\epsilon/\mu$ with $\epsilon=\log(1/\theta)/\lambda$, from $\mathcal A_M\le M$ and A.3. By (A.3), this is $s_1\ge1-a(1-\sigma)/\delta-\epsilon/\delta$. The certificate drops a box by the $s_1$ test only if $s_1^{\rm hi}<1-a^{\rm hi}(1-\sigma^{\rm lo})/\delta^{\rm lo}-1/50$. Such a box contains no cell provided $\epsilon/\delta^{\rm lo}\le1/50$. appendix_check.py verifies $\delta^{\rm lo}\ge50\epsilon$ on every such box ($\epsilon\le1.04\cdot10^{-4}$, and the minimum $\delta^{\rm lo}$ is $0.04$). $\epsilon$ is decreasing in $\lambda$, so the check at $T_1$ covers all $T\ge T_1$. The $\delta$ test uses $\delta^{\rm lo}>\min(x,a^{\rm hi}+1/100)$, which (D2) excludes.
- (D5) $s_1<0$. If $\delta<a(1-\sigma)$, the face $s_1=0$ bounds the cell: genN does not depend on $s_1$, and every zeta excess is nondecreasing in $s_1$. Otherwise (D4) gives $s_1\ge-\epsilon/\delta$. Such cells sit at the edge $s_1^{\rm lo}=0$ of a box. No box recording genD has $s_1^{\rm lo}\le0$ and $\delta^{\rm lo}\ge a^{\rm hi}(1-\sigma^{\rm lo})$ (appendix_check.py, (b)). So these cells are again bounded by zeta or genN, whose excesses are monotone in $s_1$.

**A.5 The three counts.** Let $\Lambda$ be the 1-spaced subset of the points of one cell (§4.4), let $P=P_k=2k+1$ be the number of dyadic pieces of the $k$-th power, and let $V_\bullet$ be the threshold of A.3 to the $k$-th power divided by $P$. Theorem 5.1 and Lemma 5.2, applied to the piece with the large value, give
$$|\Lambda|\le P\Bigl(45.94\,G\,N'V_\bullet^{-2}+149.04\,T'G^3N'V_\bullet^{-6}\log^2T'\Bigr),\qquad |\Lambda|\le P\,(T'+\pi m_0(2N'+1))\,G\,(1+2\log2N')\,V_\bullet^{-2}.$$
Here $N'$ is the piece length, $T'\le2.0001T$, and $G$ is from Lemma 5.3 and §5 for the coefficients of the $k$-th power. With A.3 these are $L^{e}$ times the constants and log powers listed in §6.1 and in bcalc.py (lines 47–66), with $e$ the count exponent at $(\sigma,a,\delta,s_1)$, or at $a_N$ for genN. For pieces of length $N'<25$, Theorem 5.1 holds with $2A(0.75+2.1778)\le50.04$ in place of $45.94$ (and $162.4$ in place of $149.04$). This raises $\log_{10}B$ by at most $0.04$.

**A.6 The shift for genN.** genN's excesses are linear in $a$ with slope at most $k|4-6\sigma|\le6.4$ for $k\le9$, $\sigma\in[0.755,0.785]$. So $L^{e(a_N)}\le2^{3\cdot6.4}L^{e(a)}\le4^{18}L^{e(a)}$. The certificate's condition $e(a)\le0$ and value $p+e(a)/\eta$ therefore bound the genN count of the cell's block, up to the factor $4^{18}$ already in $\Lambda_k$. For $k=1$ with $a_N\le2x$ (not used by any recorded box), and $k=2$ (recorded only on boxes with $a^{\rm lo}\ge0.505>4x$; checked on the dumps), the $X^2$ terms of C1 and C2′ are covered by the constants in bcalc.py.

**A.7 Summation.** The number of cells is at most $J_1\cdot J_2\cdot4\cdot(i_{\max}+1)\cdot\#K$, with $\#K\le\log_2(2K_{\max})$. Each cell's count is at most $L^{3(1-\sigma)}(\log T)^{P_{\rm box}}$ times the box constant. Every zero is counted at least once: in its block's genN count, or in the cell of its point $t_F$, according to the option recorded for the box containing the cell. §8 sums these.

## References

- [1] M. N. Huxley, On the difference between consecutive primes, Invent. Math. 15 (1972).
- [2] S. Chourasiya, A. Simonič, An explicit form of Ingham's zero density estimate, arXiv:2507.15184 (v2).
- [3] C. Bellotti, Explicit zero density estimate near unity, arXiv:2311.05136.
- [4] span_of_dilates, Primes between consecutive seventh powers, assuming the claimed 7/8 zero-free half-plane, rStation riemann_hypothesis_111.
- [5] M. Cully-Hugill, Primes between consecutive powers, arXiv:2107.14468.
- [6] A. Fiori, H. Kadiri, J. Swidinsky, Sharper bounds for the Chebyshev function ψ(x), J. Math. Anal. Appl. 527 (2023) 127426; arXiv:2204.02588.
- [7] D. R. Johnston, J. P. Sorenson, S. N. Thomas, J. E. Webster, Primes and almost primes between cubes, arXiv:2601.15564 (v2).
- [8] L. Guth, J. Maynard, New large value estimates for Dirichlet polynomials, arXiv:2405.20552.
- [9] G. A. Hiary, D. Patel, A. Yang, An improved explicit estimate for ζ(1/2+it), J. Number Theory 256 (2024), 195–217 (statement as quoted in [11, §2]).
- [10] D. Patel, A. Yang, An explicit sub-Weyl bound for ζ(1/2+it), J. Number Theory (2024) (statement as quoted in [11, §2]).
- [11] C. Bellotti, An explicit log-free zero density estimate for the Riemann zeta-function, arXiv:2405.12545.
- [12] E. Hasanalizade, Q. Shen, P.-J. Wong, Counting zeros of the Riemann zeta function, arXiv:2107.06506.
- [13] D. Patel, An explicit upper bound for |ζ(1+it)|, arXiv:2009.00769.
- [14] H. Kadiri, A. Lumley, N. Ng, Explicit zero density for the Riemann zeta function, arXiv:2101.12263.
