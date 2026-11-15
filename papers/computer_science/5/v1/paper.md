# Hidden-pricing bounds in the bid model of single-sample pricing and the MHR revelation gap

**Hongmin Li** (Institute of Science Tokyo; The University of Tokyo)

*This manuscript was prepared with AI assistance: the arguments, the step-function generator and the two verification programs were produced by AI models (Anthropic Claude, including its Fable model, and an OpenAI coding agent), directed by the author. The author is not a specialist in mechanism design and has not independently refereed every step; the material is released for verification by experts.*

## 1. Introduction

**Setting.** A seller faces one buyer with value $v\sim F$ and observes one independent sample $s\sim F$; $F$ is unknown to the seller but known to the buyer, who does not see $s$. For a mechanism $M$ and a class $\mathcal F$ of distributions, the prior-independent approximation ratio is $\beta(M,\mathcal F)=\sup_{F\in\mathcal F}\mathrm{OPT}(F)/\mathrm{Rev}_F(M)$, where $\mathrm{OPT}(F)=\max_p p(1-F(p))$ [1, Definition 2.1]. Let $\beta_{\mathrm{all}}$ be the infimum of $\beta(M,\mathcal F)$ over all mechanisms of FHL's model and $\beta_{\mathrm{rev}}$ the infimum over scale-invariant truthful mechanisms [1, Definition 7.1]. The revelation gap is $\beta_{\mathrm{rev}}/\beta_{\mathrm{all}}$ [1]. Throughout, $\mathcal F$ is the class of MHR distributions. Narrowing the gap for this class is posed as an open problem by Hartline in the EconCS problem collection [7].

**Known bounds.** FHL [1, Table 1] give $1.073\le\beta_{\mathrm{all}}\le 1.296$ and, citing Allouah and Besbes [3] together with [1, Lemma 7.2], $1.543\le\beta_{\mathrm{rev}}\le 1.575$, hence a gap in $[1.190,1.467]$ [1, Corollary 7.3]. Tang, Tao and Wang [2] consider a model in which the buyer reports a value and a distribution, so that the revelation principle applies; for MHR distributions they prove that no mechanism of their model is better than $2/(1+2\ln 2)$-approximate [2, Theorem 5.2], and they show by a discretized linear-programming computation that an optimal monotone hidden pricing mechanism is between $0.79$- and $0.796$-approximate [2, Proposition 4.1, Appendix B]. The upper value $0.796$ is not used here. TTW describe their model as richer than FHL's [2, Section 1.1]; Hartline's survey [4, Theorem 6.8] still lists $[0.772, 0.931]$ for the all-mechanism max–min ratio in FHL's setting (in the $[0,1]$ convention).

**Contribution.**

1. (Theorem 1) $\beta_{\mathrm{all}}\ge 1/2+\ln 2 = 1.19314\ldots$ in FHL's formal model. The direction needed is the inclusion of FHL's bid mechanisms in TTW's program, which holds for real-valued bids with any best-response selection. FHL's model requires positive densities [1, Section 2] while TTW's argument uses point masses; Lemma 2 removes point masses by smoothing.
2. (Theorem 3) TTW's discretized condition at $\Gamma=79/100$ holds rigorously: an explicit family of 148 step functions plus one linear function satisfies the continuous conditions of [2, Corollary 3.1] for all parameters, verified with ball/interval arithmetic by two programs written independently of each other.
3. (Theorem 4) A menu mechanism with real bids attains ratio at most $1/0.79$ (as an infimum over a family of mechanisms) in FHL's model, so $\beta_{\mathrm{all}}\le 1/0.79=1.26582\ldots$.
4. (Corollary 5) The revelation gap lies in $[0.79\,\beta^-, \beta^+/(1/2+\ln 2)]$ for any valid bounds $\beta^\pm$ on $\beta_{\mathrm{rev}}$.

The mathematical content of Theorems 1 and 4 is TTW's; what is new is the verification that their hypotheses are met by FHL's bid model, the smoothing step, the real-bid implementation of the guarantee, and a rigorous interval-arithmetic verification in place of a floating-point linear program.

**On the values of $\beta_{\mathrm{rev}}$.** The numbers $1.543$ and $1.575$ are numerical bounds of Allouah and Besbes [3] as reported in [1, Theorem 7.1]; we could not access [3] and use them only through Corollary 5, which is stated for arbitrary $\beta^\pm$. FHL's class of truthful mechanisms is restricted to scale-invariant ones; Hartline's survey states that this restriction is without loss for the robust problem [4, Section 6.4, citing Hartline, Johnsen and Li] and reports the revelation max–min ratio bounds $[0.644, 0.648]$ from Allouah, Bahamou and Besbes [5] [4, Theorem 6.8]. If one uses $\beta^-=1/0.648$, $\beta^+=1/0.644$ instead, Corollary 5 gives $[1.21913, 1.30143]$.

## 2. Notation

For $\lambda\ge0$, $a>0$ let $\check F_{\lambda,a}(v)=1-e^{-\lambda v}$ for $0\le v<a$ and $\check F_{\lambda,a}(v)=1$ for $v\ge a$; for $b\ge 1$ let $\hat F_{1,b}(v)=1-e^{-(v-b)}$ for $v\ge b$, and $\hat F_{\lambda,b}$ its scaling by $1/\lambda$ [2, eq. (2)]. With $\mathrm{Rev}(p,F)=p\,(1-F(p^-))$, put $\mathrm{LB}(F,\Gamma)=\inf\{p:\mathrm{Rev}(p,F)\ge\Gamma\,\mathrm{OPT}(F)\}$ and $\mathrm{UB}(F,\Gamma)=\sup\{\cdot\}$ [2, Definition 2.6]. For $\lambda a\le 1$, $\mathrm{OPT}(\check F_{\lambda,a})=a e^{-\lambda a}$; for $\lambda b\ge1$, $\mathrm{OPT}(\hat F_{\lambda,b})=b$ [2, Lemma 2.3]. Both LB and UB are positively 1-homogeneous under scaling of the distribution.

A pricing policy $p$ maps distributions to prices; it is monotone if it is non-decreasing in first-order stochastic dominance. [2, Corollary 3.1] states: a monotone policy is $\Gamma$-approximate on the MHR class if and only if $p(\check F_{\lambda,a})\ge \mathrm{LB}(\check F_{\lambda,a},\Gamma)$ whenever $\lambda a\le 1$, and $p(\hat F_{\lambda,b})\le\mathrm{UB}(\hat F_{\lambda,b},\Gamma)$ whenever $\lambda b\ge1$. Let $H^\Gamma$ be the set of non-decreasing $h:\mathbb R_+\to\mathbb R_+$ with $\mathbb E_{\check F_{\lambda,a}}[h]\ge\mathrm{LB}(\check F_{\lambda,a},\Gamma)$ for all $\lambda a\le 1$ [2, Section 4].

## 3. The impossibility bound in the bid model

**Theorem 1.** In FHL's model, every mechanism $M=(\tilde x,\tilde p)$ satisfies $\beta(M,\mathcal F)\ge 1/2+\ln 2$. This holds whether $\mathcal F$ is read as all MHR distributions or as MHR distributions with positive density on a bounded support.

*Reduction.* Fix $M$ and, for each $F$, a best response $b(\cdot,F)$ [1, Section 2]. Setting $x(s,v,F)=\tilde x(b(v,F),s)$ and $t(s,v,F)=\tilde p(b(v,F),s)$ defines a direct mechanism in TTW's sense: incentive compatibility with respect to a joint misreport $(v',F')$ is the inequality $\mathbb E_{s\sim F}[v\tilde x(b(v,F),s)-\tilde p(b(v,F),s)]\ge \mathbb E_{s\sim F}[v\tilde x(b',s)-\tilde p(b',s)]$ with $b'=b(v',F')$, which is the best-response property; individual rationality and revenue are unchanged, since FHL's individual rationality is the interim condition $\max_b v\,\tilde x(b,F)-\tilde p(b,F)\ge0$ for all $v$ and $F$ [1, Section 2], which is TTW's. Hence any ratio guarantee of $M$ on a class is a feasible value of TTW's program on that class, and every upper bound TTW derive from a subset of the IC and IR constraints applies to $M$. No reporting of distributions and no tie-breaking rule is needed in this direction. If point masses belong to the class, [2, Theorem 5.2] with $c=1$ and $F_0(v)=2(1-1/v)$ on $[1,2]$ (which is MHR [2, Section 5]) applies verbatim and gives $\Gamma\le 2/(1+2\ln2)$. Under the positive-density reading we use:

**Lemma 2 (smoothing).** Let $\varepsilon\in(0,1)$, $G_u$ the uniform distribution on $[u,u+\varepsilon]$, and $F_0^\varepsilon$ the law of $X+Y$ with $X\sim F_0$, $Y\sim U[0,\varepsilon]$ independent. All these distributions are MHR, with bounded support and a density that is positive on the interior of the support (densities are defined up to null sets). If $M$ is $\Gamma$-approximate on $\{G_u: u\in[1,2]\}\cup\{F_0^\varepsilon\}$, then $\Gamma\le (2+3\varepsilon+C\varepsilon)/(1+2\ln 2)$ for an absolute constant $C$.

*Proof.* Uniform distributions have non-decreasing hazard rate, and the MHR property is preserved under convolution [6, Chapter 4]; supports are $[u,u+\varepsilon]$ and $[1,2+\varepsilon]$ with positive density. Fix a bid $b'$ (the best response of some type under $F_0^\varepsilon$). Under prior $G_u$, the buyer of value $w$ can deviate to $b'$, so her equilibrium utility is at least $\mathbb E_{s\sim G_u}[w\tilde x(b',s)-\tilde p(b',s)]\ge \mathbb E_{s\sim G_u}[s\tilde x(b',s)-\tilde p(b',s)]-\varepsilon$ since $|w-s|\le\varepsilon$. Averaging over $w\sim G_u$ and using that expected utility equals expected welfare minus revenue, at most $(u+\varepsilon)-\Gamma\,\mathrm{OPT}(G_u)\le (1-\Gamma)u+\varepsilon$, we get $\mathbb E_{s\sim G_u}[s\tilde x(b',s)-\tilde p(b',s)]\le(1-\Gamma)u+2\varepsilon$. Since $F_0^\varepsilon$ is the mixture of $G_u$ over $u\sim F_0$, integrating gives
$$\mathbb E_{s\sim F_0^\varepsilon}[s\,x_0(s,v)-t_0(s,v)]\le (1-\Gamma)\,\mathbb E_{F_0^\varepsilon}[s]+2\varepsilon \quad\text{for all } v,$$
the analogue of [2, eq. (7)], where $x_0,t_0$ are the induced rules under $F_0^\varepsilon$. The remaining steps of [2, Theorem 5.2] use only this integrated constraint at the top type $\bar v=2+\varepsilon$ (which lies in the support) and IC/IR under $F_0^\varepsilon$. Write $x_0(v)=\mathbb E_s[x_0(s,v)]$, $t_0(v)=\mathbb E_s[t_0(s,v)]$. Since $x_0(s,\bar v)\le1$ and $s\le\bar v$, $\mathbb E_s[s\,x_0(s,\bar v)]\ge\mathbb E[s]-\bar v+\bar v x_0(\bar v)$; the envelope formula with $u(0)\ge0$ gives $t_0(\bar v)\le\bar v x_0(\bar v)-\int_0^{\bar v}x_0$; together $\Gamma\,\mathbb E[s]\le\bar v-\int_0^{\bar v}x_0+2\varepsilon$. Myerson's lemma gives $\Gamma\,\mathrm{OPT}(F_0^\varepsilon)\le\mathbb E[t_0(v)]\le\int_0^{\bar v}(vf_0^\varepsilon-(1-F_0^\varepsilon))x_0\,dv$. Adding, and using $0\le x_0\le1$, with $c=1$:
$$\Gamma\,\big(\mathbb E_{F_0^\varepsilon}[s]+\mathrm{OPT}(F_0^\varepsilon)\big)\le \bar v+2\varepsilon+\int_0^{\bar v}\big(f_0^\varepsilon(v)v-(1-F_0^\varepsilon(v))-1\big)^+dv.$$
Here $\mathbb E_{F_0^\varepsilon}[s]=2\ln 2+\varepsilon/2$ and $\mathrm{OPT}(F_0^\varepsilon)\ge\mathrm{OPT}(F_0)=1$ because $F_0^\varepsilon$ dominates $F_0$. For $v\in[1+\varepsilon,2]$, $f_0^\varepsilon(v)=(F_0(v)-F_0(v-\varepsilon))/\varepsilon$ and $F_0^\varepsilon(v)=\varepsilon^{-1}\int_{v-\varepsilon}^vF_0$; Taylor expansion with $f_0=2/v^2$, $f_0'=-4/v^3$ shows that the integrand equals $\varepsilon/v^2+O(\varepsilon^2)$, using $vf_0-(1-F_0)-1=0$ on $[1,2]$. On $[1,1+\varepsilon]\cup[2,2+\varepsilon]$ the integrand is bounded (densities are at most $2$, $v\le 3$), contributing $O(\varepsilon)$. Collecting terms proves the lemma. $\square$

Letting $\varepsilon\to0$ proves Theorem 1 under the positive-density reading; a larger class only increases $\beta(M,\mathcal F)$.

## 4. Rigorous verification of the guarantee $\Gamma=0.79$

Let $A_k=1+k/50$ ($0\le k\le 450$, so $A_{450}=10$). For a vector $(h[0],\dots,h[450])$ define the step function $h(s)=h[0]$ for $s\le A_0$, $h(s)=h[k]$ for $A_{k-1}<s\le A_k$, and $h(s)=h[450]+e\,(s-10)$ for $s>10$, as in [2, Appendix B].

**Theorem 3.** Let $\Gamma=79/100$ and $c=0.8525$. There are 148 intervals $[b_{j-1},b_j]$ covering $[1,3.8]$ and step functions $h_1,\dots,h_{148}$ of the above form (given in the supplement; each is the running maximum of a stored floating-point vector, which raises entries by at most $1.8\times10^{-13}$) such that:
(i) each $h_j$ and the function $s\mapsto c\,s$ belong to $H^\Gamma$;
(ii) $\mathbb E_{\hat F_{1,b}}[h_j]\le\mathrm{UB}(\hat F_{1,b},\Gamma)$ for all $b\in[b_{j-1},b_j]$;
(iii) $c\,(b+1)=\mathbb E_{\hat F_{1,b}}[cs]\le \mathrm{UB}(\hat F_{1,b},\Gamma)$ for all $b\ge 3.8$.

*Method of verification.* All decisions are made in interval arithmetic on exact dyadic inputs. For (ii), $\mathbb E_{\hat F_{1,b}}[h]$ is non-decreasing in $b$ for non-decreasing $h$ [2, Lemma B.3] and $U(b)=\mathrm{UB}(\hat F_{1,b},\Gamma)$, the root $U>b$ of $U e^{-(U-b)}=\Gamma b$, satisfies $U'(b)=(1-1/b)/(1-1/U)\ge0$, so it suffices to compare $\mathbb E_{\hat F_{1,b_j}}[h_j]$ with $\mathrm{UB}(\hat F_{1,b_{j-1}},\Gamma)$; UB is enclosed by interval bisection. For (i), on each $(A_{k-1},A_k]$ the expectation $\mathbb E_{\check F_{\lambda,a}}[h]$ does not depend on $a$ [2, Lemma B.1] and is non-increasing in $\lambda$ [2, Lemma B.2], while $\mathrm{LB}(\check F_{\lambda,a},\Gamma)$ is enclosed over parameter boxes; $\lambda$ is subdivided in the variable $t=\lambda a$ with step $0.0025$, giving 181,139 cells over $a\in[1,10]$. The case $a\le1$ follows from $h[0]\ge \Gamma$ (checked for every cell) and $\mathrm{LB}(\check F_{\lambda,a},\Gamma)\le\Gamma a\le\Gamma$; the case $a>10$ follows from the slope-$e$ tail and $|\partial_a\mathrm{LB}|\le1$ [2, Lemma 2.5]. For (iii), where $c(b+1)>b$ the inequality is $\log\big(c(1+1/b)\big)+b-c(b+1)\ge\log\Gamma$; the left side has derivative $1-c-1/(b(b+1))>0$ for $b\ge3.8$ and the left side exceeds $\log\Gamma$ by about $0.0177$ at $b=3.8$, and for $b\ge c/(1-c)$ one has $c(b+1)\le b\le\mathrm{UB}$. The smallest margin in (ii) is $4.4\times10^{-3}$, attained near $b\approx1.75$, close to TTW's tightest instance.

The step functions were produced by linear programs in floating point; their correctness is checked a posteriori. A first checker uses `mpmath` interval arithmetic on the fixed grid above with explicit floating-point error bounds. A second checker was written from TTW's text and the data file alone, without access to the first. It uses Arb ball arithmetic, treats the stored values as exact dyadic rationals, and covers $\lambda$ adaptively: for each step $(A_{i-1},A_i]$ it bounds the needed LB at $a^*=\min(A_i,1/\lambda)$ and certifies $\log(\text{revenue at }H)-\log(\Gamma\,\mathrm{OPT})\ge0$ on whole $\lambda$-boxes by a mean-value bound (702,247 step–box verifications); it proves the tail $a>10$ from $0\le \partial_a\mathrm{LB}\le 1\le e\,e^{-\lambda a}$, and the linear case analytically for all $b\ge3.8$. Both checkers accept the data. The second also detected that the stored vectors have rounding-level decreases in 19 of the 148 cells, which is why Theorem 3 uses running maxima (the first checker applies the same repair). Perturbation tests: the first checker rejects data with values of $h$ lowered by $2\times10^{-3}$; the second rejects a value lowered by $3\times10^{-3}$, a monotonicity violation, $\Gamma=0.80$, and $c=0.95$.

## 5. The guarantee in the bid model

**Theorem 4.** In FHL's model, for every $\eta\in(0,1)$ there is a mechanism with $\beta(M,\mathcal F)\le 1/((1-\eta)\,0.79)$. Hence $\beta_{\mathrm{all}}\le 1/0.79$.

*Proof.* Let $\mathcal H=\{h_1,\dots,h_{148}, cs, es\}$ with the functions of Theorem 3, and consider the menu $\mathcal I=\{s\mapsto k\,g(s/k): g\in\mathcal H, k>0\}$. A bid encodes either "opt out" or a pair $(g,k)\in\mathcal H\times(0,\infty)$; a finite set times an interval embeds in $\mathbb R$. On opt-out nothing happens; on $(g,k)$ the buyer receives the item and pays $(1-\eta)\,k\,g(s/k)\ge0$. A buyer with prior $F$ and value $v$ obtains utility $v-(1-\eta)\mathbb E_F[k\,g(s/k)]$ from $(g,k)$, so she participates when $v>(1-\eta)p_M(F)$ with $p_M(F)=\min_{\mathcal I}\mathbb E_F[\,\cdot\,]$, and pays $(1-\eta)p_M(F)$ in expectation. The minimum is attained: for fixed $g$, $k\mapsto\mathbb E_F[k\,g(s/k)]$ is lower semicontinuous (left-continuous non-decreasing $g$, Fatou), tends to $+\infty$ as $k\to\infty$ when $g$ is a step function (as then $g\ge g(0)\ge 0.79$), and tends to $\mathbb E_F[e\,s]$ as $k\to0$ by dominated convergence, which is the value of the menu item $es$; for linear $g$ the item does not depend on $k$.

$p_M$ is a minimum of expectations of non-decreasing functions, hence a monotone policy. Each menu item lies in $H^\Gamma$: $\mathbb E_{\check F_{\lambda,a}}[k\,g(s/k)]=k\,\mathbb E_{\check F_{\lambda k,a/k}}[g]\ge k\,\mathrm{LB}(\check F_{\lambda k,a/k},\Gamma)=\mathrm{LB}(\check F_{\lambda,a},\Gamma)$, since $(\lambda k)(a/k)=\lambda a\le1$ and LB is 1-homogeneous; for $es$ use $e>c$. Thus $p_M(\check F_{\lambda,a})\ge\mathrm{LB}$. For $\hat F_{\lambda,b}$ with $\lambda b\in[b_{j-1},b_j]$, the item $(h_j,1/\lambda)$ gives $p_M(\hat F_{\lambda,b})\le\lambda^{-1}\mathbb E_{\hat F_{1,\lambda b}}[h_j]\le\lambda^{-1}\mathrm{UB}(\hat F_{1,\lambda b},\Gamma)=\mathrm{UB}(\hat F_{\lambda,b},\Gamma)$; for $\lambda b>3.8$ use $cs$ and Theorem 3(iii). By [2, Corollary 3.1], posting $p_M(F)$ is $0.79$-approximate on all MHR distributions. With prices scaled by $1-\eta$, every type $v\ge p_M(F)$ strictly prefers to participate, so the revenue is at least $(1-\eta)p_M(F)(1-F(p_M(F)^-))\ge (1-\eta)\,0.79\,\mathrm{OPT}(F)$ under any tie-breaking. Restricting to distributions with positive density only lowers the supremum. $\square$

## 6. The revelation gap

**Corollary 5.** For MHR distributions, $1/2+\ln2\le\beta_{\mathrm{all}}\le1/0.79$. Consequently, if $\beta^-\le\beta_{\mathrm{rev}}\le\beta^+$, then
$$0.79\,\beta^-\ \le\ \beta_{\mathrm{rev}}/\beta_{\mathrm{all}}\ \le\ \beta^+/(1/2+\ln 2).$$
With the values $\beta^-=1.543$, $\beta^+=1.575$ of [1, Theorem 7.1] (from [3]) this is $[1.21897, 1.32004]$, improving $[1.190,1.467]$ of [1, Corollary 7.3]. With $\beta^\pm$ from $[0.644,0.648]$ as reported in [4, Theorem 6.8] (from [5]) it is $[1.21913,1.30143]$.

In particular, the gap is non-trivial with lower bound above $1.2$, and the remaining uncertainty in $\beta_{\mathrm{all}}$ is the interval $[0.79, 0.838]$ of [2], whose upper end comes from the same program as Theorem 1.

## Data availability

The supplement contains the 148 step functions (`cover.json.gz`), the generator, both checkers with their logs, and perturbation tests.

## References

[1] Y. Feng, J. D. Hartline, Y. Li. Revelation gap for pricing from samples. STOC 2021; arXiv:2102.13496.

[2] Z. G. Tang, Y. Tao, S. Wang. Pricing with a hidden sample. EC 2026; arXiv:2602.18038.

[3] A. Allouah, O. Besbes. Sample-based optimal pricing. Proceedings of the 2019 ACM Conference on Economics and Computation (EC 2019).

[4] J. D. Hartline. Prior-robust mechanism design (survey), arXiv:2610.01805.

[5] A. Allouah, A. Bahamou, O. Besbes. Pricing with samples. Operations Research 70(2):1088–1104, 2022.

[6] R. E. Barlow, F. Proschan. Mathematical Theory of Reliability. Wiley, 1965.

[7] J. D. Hartline. Revelation gap for MHR pricing from one sample. Problem in the EconCS open-problem collection, https://github.com/aieconcs/econcs-bench (revelation-gap-mhr-pricing).
