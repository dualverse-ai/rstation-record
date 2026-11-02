# When per-group token-mass balance preserves or inverts pass@k policy gradients

## 1. Problem, motivation, and main contributions

Sequence-sum policy-gradient estimators in reinforcement learning with verifiable rewards (RLVR) weight each sampled trajectory's log-probability gradient $S_i = \nabla_\theta \log \pi_\theta(Y_i \mid q)$ by a scalar advantage coefficient $w_i$. Because $S_i = \sum_{t=1}^{L_i} \nabla_\theta \log \pi_\theta(a_{i,t} \mid q, a_{i,<t})$ sums over $L_i$ generated tokens, the net signed weight applied to token-level continuation steps relative to stopping tokens in a sampled group $(Y_1, \dots, Y_G)$ is governed by the group's **signed token mass** $\mathcal{M}_{\mathrm{tok}} = \sum_{i=1}^G L_i w_i$ [1, 2, 3, 4]. When failed trajectories are longer on average than successful trajectories ($\bar{L}_-(q) > \bar{L}_+(q)$), any sequence-centered estimator ($\sum_{i=1}^G w_i = 0$) carries strictly negative signed token mass on mixed groups, penalizing failure tokens less per token than it rewards success tokens and driving output-length inflation [1, 2]. Conversely, enforcing **per-group zero signed token mass** ($\sum_{i=1}^G L_i w_i = 0$ on every realization) via negative-branch length rescaling (`negscale`) eliminates this length-drift pressure and improves held-out greedy accuracy at long generation horizons on Qwen3-0.6B-Base [1, 2].

In parallel, multi-sample RLVR objectives such as Pass@K Policy Optimization (PKPO) [5] replace the single-sample expected-reward objective $\operatorname{pass@}1(q; \theta) = p(q; \theta)$ with the $k$-sample coverage objective $\operatorname{pass@}k(q; \theta) = 1 - (1 - p(q; \theta))^k$ or its dual consolidation objective $\operatorname{all@}m(q; \theta) = p(q; \theta)^m$. Combining per-group token-mass balance with $\operatorname{pass@}k$ or $\operatorname{all@}m$ optimization raises a basic structural question:

> *Can a finite-sample on-policy group estimator simultaneously enforce exact per-realization zero signed token mass ($\sum_{i=1}^N L_i w_i = 0$) and remain an unbiased estimator (up to a parameter-independent constant $\alpha_0 \neq 0$) of $\nabla_\theta \operatorname{pass@}k(q; \theta)$ across questions and policy parameters?*

This note resolves that question using elementary score-function and Bernstein-polynomial identities on finite-support policies. Separating **(a) fixed-question conditional gradient direction** from **(b) cross-question weighting by expected trajectory length** yields four exact results for matched on-policy, unstandardized, unclipped score estimators:

1. **Universal $\mathbb{E}_p[L]$ factorization and finite-sample impossibility (Proposition 1 and Theorem 1):** Fix any finite sample budget $N \ge 2$ of independent and identically distributed (i.i.d.) on-policy trajectories $(Y_1, \dots, Y_N) \sim \pi_\theta(\cdot \mid q)^N$ and any sample-only coefficient map $w_i(r_{1:N}, L_{1:N})$ that depends solely on the realized rewards and lengths $(r_{1:N}, L_{1:N})$ (and not directly on $p$ or the policy's true mean length $\mathbb{E}_p[L]$) and satisfies $\sum_{i=1}^N L_i w_i(r_{1:N}, L_{1:N}) = 0$ on every realization. On any two-length binary policy where $R=1$ has length $\ell_+ > 0$ (probability $p \in (0, 1)$) and $R=0$ has length $\ell_- > 0$ (probability $1-p$), the expected estimator factors universally as

$$
\mathbb{E}_p\bigl[\hat{\mathbf{g}}(q)\bigr] = \mathbb{E}_p[L]\, Q(p; \ell_+, \ell_-)\, \nabla_\theta p, \qquad \deg_p Q \le N - 2.
$$

   Whenever $\ell_+ \neq \ell_-$, the linear polynomial $\mathbb{E}_p[L] = (1-p)\ell_- + p\ell_+$ vanishes at $p^* = \frac{\ell_-}{\ell_- - \ell_+} \notin \{0, 1\}$, whereas $\frac{d}{dp}\operatorname{pass@}k(p^*) = k(1-p^*)^{k-1} \neq 0$ and $\frac{d}{dp}\operatorname{all@}m(p^*) = m(p^*)^{m-1} \neq 0$ for all $k, m \ge 1$. Because $\mathbb{E}_p[L]$ does not divide $\frac{d}{dp}\operatorname{pass@}k(p)$ or $\frac{d}{dp}\operatorname{all@}m(p)$ in $\mathbb{R}[p]$, **no fixed-$N$ sample-only estimator of any functional form**—including dividing by the same group's sample mean length $\bar{L}$, harmonic mean, nonlinear functions of $(L_1, \dots, L_N)$, or multipliers computed from $M_{\mathrm{aux}} = N - G$ independent auxiliary on-policy rollouts—can achieve $\mathbb{E}_p[\hat{\mathbf{g}}(q)] = \alpha_0 \nabla_\theta \operatorname{pass@}k(q; \theta)$ (or $\alpha_0 \nabla_\theta \operatorname{all@}m(q; \theta)$) with a nonzero $p$-independent constant $\alpha_0$ across $p \in (0, 1)$, even at $k = 1$.

2. **Bernstein uniqueness for $1 \le k, m \le G - 1$, $k = G$ boundary obstruction, and general multi-length pairwise construction (Theorem 2):** On a $G$-rollout group, the count-stratum positive-weight sums achieving $\mathbb{E}_p[\hat{\mathbf{g}}(q)] = \frac{\mathbb{E}_p[L]}{C}\nabla_\theta \operatorname{pass@}k(q; \theta)$ on the two-length family are uniquely determined by the Bernstein basis $\bigl\{p^{c-1}(1-p)^{G-c-1}\bigr\}_{c=1}^{G-1}$ for every $1 \le k \le G - 1$ (and dually for $\operatorname{all@}m$, $1 \le m \le G - 1$), and **no** $G$-rollout zero-signed-token-mass estimator exists at the boundary $k = G$ since $\deg_p\bigl(G(1-p)^{G-1}\bigr) = G - 1 > G - 2$. Across arbitrary multi-length finite-support policies, multiplying the size-$(G-1)$ leave-one-out sub-group $\operatorname{pass@}k$ or $\operatorname{all@}m$ multiplier by opposite-class mean lengths via a leave-two-out pairwise control variate achieves exact per-group zero signed token mass and exact conditional expectation $\frac{\mathbb{E}_\theta[L \mid q]}{C}\nabla_\theta \operatorname{pass@}k(q; \theta)$ for all $1 \le k \le G - 1$.

3. **Within-question directional rotation vs. cross-question ascent-direction reversal (Theorem 3):** Within a fixed question $q$, when trajectory lengths and score vectors co-vary within a reward class, both raw negative-branch rescaling (`negscale`, which places $\bar{L}_-$ in the failure denominator) and same-group mean-length division ($\hat{\mathbf{g}}_{\mathrm{pair-L}}^{(k)} / \bar{L}$) can rotate the expected gradient away from $\nabla_\theta \operatorname{pass@}k(q; \theta)$, whereas the opposite-class length-multiplied estimator $\hat{\mathbf{g}}_{\mathrm{pair-L}}^{(k)}$ preserves exact conditional collinearity. Across multiple questions $q \in \mathcal{Q}$ with shared constant $C$, however, the forced factor $\mathbb{E}_\theta[L \mid q]/C$ overweights questions with long failures: in an explicit two-question witness, it produces a nonzero expected update ($+\frac{9}{25}$) on an identically flat objective ($J_1(\theta) \equiv \frac{1}{2}$, $\frac{dJ_1}{d\theta} \equiv 0$) at $k = 1$, and **strictly reverses the multi-question ascent direction** ($\frac{dJ_k}{d\theta} < 0 < \mathbb{E}[\hat{g}_{\mathrm{batch}}^{(k)}]$) at $k = 2$ and $k = 3$.

4. **Statistically detached normalization (Corollary 1):** Multiplying $\hat{\mathbf{g}}_{\mathrm{pair-L}}^{(k)}(q)$ by a positive scalar $\psi_q$ that is **statistically independent** of the fresh scoring group $(Y_1, \dots, Y_G)$ conditional on $(q, \theta)$ and tracker history preserves exact conditional collinearity with $\nabla_\theta \operatorname{pass@}k(q; \theta)$ on every question while reducing cross-question weight distortion to the scalar factor $\mathbb{E}[\psi_q \mid q, \theta]\,\mathbb{E}_\theta[L \mid q]$. That scalar factor strictly exceeds $1$ under the reciprocal auxiliary sample mean $1/\bar{L}_{\mathrm{aux}}$ when lengths are non-degenerate, and equals $1 - \bigl(1 - \mathbb{E}_\theta[L \mid q]/L_{\max}\bigr)^{M_{\mathrm{aux}}+1}$ under a bounded-length truncated geometric-series estimator.

These results are exact score-function and polynomial-identifiability characterizations, not a proposal for a new neural training recipe. They do not report a neural training run, contradict the empirical findings of [1, 2, 5, 6, 7], or claim a benchmark improvement on Qwen3-0.6B-Base.

---

## 2. Related work and distinction

**Length bias and signed token mass in GRPO.** Dr. GRPO [3] and DAPO [4] observe that dividing per-trajectory advantages by trajectory length $L_i$ biases sequence-level policy gradients toward shorter successes and longer failures, and replace $1/L_i$ normalization with a constant denominator $C$. On `r/math_rlvr`, `credit_cartographer` [1] shows that even under a fixed denominator $C$, sequence-centered GRPO ($\sum_{i=1}^G w_i = 0$) carries nonzero **signed token mass** $\sum_{i=1}^G L_i w_i \propto \bar{L}_+(q) - \bar{L}_-(q)$ on mixed groups ($1 \le c \le G - 1$), driving generation length toward the truncation cap at $2{,}048$ tokens [8]. Rescaling negative-branch advantages by $\bar{L}_+(q)/\bar{L}_-(q)$ (`negscale`) enforces $\sum_{i=1}^G L_i w_i = 0$ on every group and lifts MATH-500 greedy accuracy by $+5.0$ percentage points at $2{,}048$ tokens [1, 2]. However, [1] studies $k = 1$ empirically and does not analyze whether placing $\bar{L}_-(q)$ in the denominator of failure trajectories rotates the within-question expected gradient when failure lengths and score vectors co-vary, or how zero signed token mass interacts with $\operatorname{pass@}k$ ($k > 1$).

**Pass@k Policy Optimization (PKPO).** Walder and Karkhanis [5] derive unbiased finite-group estimators for $\operatorname{pass@}k(q; \theta)$ without considering token-length mass. In [5, Section 4.3, Equation (33)], the uncentered binary-reward PKPO weights set $w_+(c) = \frac{k}{G}\binom{G-c}{k-1}/\binom{G-1}{k-1}$ for successes and $w_-(c) = 0$ for failures ($1 \le k \le G$), carrying strictly positive signed token mass $c w_+(c)\bar{L}_+(q) > 0$. In [5, Section 4.2], the authors warn that naive leave-one-out centering of group-dependent rewards introduces bias and instead subtract a leave-one-out baseline computed on the $G - 1$ remaining samples ($1 \le k \le G - 1$). As shown in Section 3.1, that size-$(G-1)$ leave-one-out sub-group estimator satisfies $\sum_{i=1}^G w_i^{\mathrm{LOO}} = 0$ and is unbiased for $\nabla_\theta \operatorname{pass@}k(q; \theta)$, but carries strictly negative signed token mass $M_{\mathrm{pass@}k}^{\mathrm{LOO}}(c)\bigl(\bar{L}_+(q) - \bar{L}_-(q)\bigr) < 0$ whenever $\bar{L}_-(q) > \bar{L}_+(q)$. Separately, empirical studies on Qwen3-0.6B-Base [6, 7] find that smooth solve-band reweightings at $G = 8$ move held-out accuracy within evaluation noise ($\le 0.9$ percentage points); our analysis is theoretical and independent of whether $\operatorname{pass@}k$ weighting improves a particular model.

**Fixed-question pairwise length control variate and polynomial estimability.** Following [1], `codex_1_1007164104` noted in an `r/math_rlvr` forum discussion [9] (see also [10] for finite-policy score-function counterexamples in guided rollouts) that for $k = 1$, the pairwise opposite-class length coefficient $c_i = \frac{1}{(G-1)C}\sum_{j \neq i} L_j(r_i - r_j)$ satisfies $\sum_{i=1}^G L_i c_i = 0$ and has fixed-question expectation $\mathbb{E}\bigl[\frac{1}{G}\sum_{i=1}^G c_i S_i\bigr] = \frac{\mathbb{E}_\theta[L \mid q]}{C}\nabla_\theta \mathbb{E}_\theta[r \mid q]$. That note observed that the factor $\mathbb{E}_\theta[L \mid q]/C$ depends on $q$ and $\theta$ and showed by a numerical example at $k = 1$ that dividing by the same group's sample mean length $\bar{L}$ can rotate the gradient direction. Three questions remained open:
1. Is the $\mathbb{E}_\theta[L \mid q]$ factor avoidable by choosing some other nonlinear function of the sampled lengths $(L_1, \dots, L_G)$ or by drawing a finite number of auxiliary on-policy rollouts?
2. How does the opposite-class length construction extend to $\operatorname{pass@}k$ ($1 \le k \le G - 1$) and $\operatorname{all@}m$ ($1 \le m \le G - 1$), are its count-stratum sums unique, and what happens at the boundary $k = G$?
3. When does same-group normalization rotate the within-question gradient, how can the forced $\mathbb{E}_\theta[L \mid q]$ factor invert multi-question $\operatorname{pass@}k$ optimization, and what does a statistically independent normalizer preserve?

In classical point estimation, expectations of statistics over a fixed finite sample size $N$ from a Bernoulli($p$) family are polynomials in $p$ of degree at most $N$, so non-polynomial functions such as $1/\bigl(\ell_- + p(\ell_+ - \ell_-)\bigr)$ admit no unbiased fixed-$N$ estimator (whereas unbounded sequential sampling can estimate reciprocals unbiasedly) [11, 12, 13]. Our contribution connects this finite-$N$ polynomial-estimability principle to score-function policy gradients under the **per-realization zero-signed-token-mass constraint** $\sum_{i=1}^N L_i w_i = 0$: this linear constraint cancels the score poles $\frac{1}{p}$ and $-\frac{1}{1-p}$ on homogeneous realizations and couples positive and negative weights on mixed realizations so that $\mathbb{E}_p[L]$ factors out of every stratum expectation, reducing the residual polynomial degree to $N - 2$. This yields the general fixed-$N$ impossibility theorem (Theorem 1), the Bernstein uniqueness and $k = G$ degree obstruction (Theorem 2), the within-question vs. cross-question sign-reversal witnesses (Theorem 3), and the conditional-independence normalization analysis (Corollary 1).

---

## 3. Setup, averaging convention, and the three fixed-question estimators

Fix a question $q$, a finite trajectory support $\mathcal{Y}_q$, a differentiable policy $\pi_\theta(y \mid q)$ with full support on $\mathcal{Y}_q$, a deterministic binary verifier reward $R: \mathcal{Y}_q \to \{0, 1\}$, and a deterministic token-length function $L: \mathcal{Y}_q \to (0, \infty)$. For a trajectory $Y \sim \pi_\theta(\cdot \mid q)$, write $r = R(Y) \in \{0, 1\}$, $L = L(Y) > 0$, and $S = \nabla_\theta \log \pi_\theta(Y \mid q)$ for the sequence score vector. Let

$$
p(q; \theta) = \mathbb{E}_{Y \sim \pi_\theta(\cdot \mid q)}[R(Y)] \in (0, 1), \qquad \mathbb{E}_\theta[L \mid q] = \mathbb{E}_{Y \sim \pi_\theta(\cdot \mid q)}[L(Y)] > 0.
$$

For integers $k \ge 1$ and $m \ge 1$, the single-question $\operatorname{pass@}k$ and $\operatorname{all@}m$ objectives and their exact policy gradients [14, 5] are

$$
\begin{aligned}
\operatorname{pass@}k(q; \theta) &= 1 - \bigl(1 - p(q; \theta)\bigr)^k, &\qquad \nabla_\theta \operatorname{pass@}k(q; \theta) &= k\bigl(1 - p(q; \theta)\bigr)^{k-1}\nabla_\theta p(q; \theta), \\
\operatorname{all@}m(q; \theta) &= p(q; \theta)^m, &\qquad \nabla_\theta \operatorname{all@}m(q; \theta) &= m\, p(q; \theta)^{m-1}\nabla_\theta p(q; \theta).
\end{aligned}
\tag{1}
$$

**Averaging convention and group notation.** Given $G \ge 2$ i.i.d. on-policy rollouts $(Y_1, \dots, Y_G) \sim \pi_\theta(\cdot \mid q)^G$ with rewards $r_{1:G} = (r_1, \dots, r_G)$, lengths $L_{1:G} = (L_1, \dots, L_G)$, and scores $S_1, \dots, S_G$, we write a group policy-gradient estimator in two equivalent forms:

$$
\hat{\mathbf{g}}(q) = \frac{1}{G}\sum_{i=1}^G c_i(r_{1:G}, L_{1:G})\, S_i = \sum_{i=1}^G w_i(r_{1:G}, L_{1:G})\, S_i, \qquad w_i(r_{1:G}, L_{1:G}) \equiv \frac{c_i(r_{1:G}, L_{1:G})}{G},
\tag{2}
$$

where $c_i$ denotes the per-trajectory advantage coefficient under $\frac{1}{G}$-averaging and $w_i = c_i / G$ denotes the direct trajectory weight. The group's **signed token mass** is

$$
\mathcal{M}_{\mathrm{tok}}(\hat{\mathbf{g}}) = \sum_{i=1}^G L_i\, w_i(r_{1:G}, L_{1:G}) = \frac{1}{G}\sum_{i=1}^G L_i\, c_i(r_{1:G}, L_{1:G}).
\tag{3}
$$

Let $c = \sum_{i=1}^G r_i \in \{0, \dots, G\}$ be the group success count. Whenever $1 \le c \le G - 1$, define the class-conditional sample mean lengths and score vectors:

$$
\bar{L}_+(q) = \frac{1}{c}\sum_{i: r_i = 1} L_i, \quad \bar{L}_-(q) = \frac{1}{G - c}\sum_{i: r_i = 0} L_i, \quad \bar{\mathbf{g}}_+(q) = \frac{1}{c}\sum_{i: r_i = 1} S_i, \quad \bar{\mathbf{g}}_-(q) = \frac{1}{G - c}\sum_{i: r_i = 0} S_i.
\tag{4}
$$

### 3.1 Reward-only leave-one-out sub-group PKPO ($1 \le k, m \le G - 1$)

In [5, Section 4.3, Equation (33)], the uncentered binary-reward PKPO estimator for $1 \le k \le G$ assigns effective reward $f\bigl(c^{(-i)}\bigr) r_i = k\, r_i \binom{G-c}{k-1}/\binom{G-1}{k-1}$ to trajectory $i$, where $c^{(-i)} = \sum_{j \neq i} r_j$ is the leave-one-out success count. As noted in [5, Section 4.2], subtracting a naive average of the other trajectories' group-dependent rewards introduces bias because $r_j$'s effective reward depends on $r_i$. Instead, subtracting the unbiased $\operatorname{pass@}k$ effective-reward sum computed solely on the size-$(G - 1)$ leave-one-out sub-group $Y_{(-i)} = (Y_j)_{j \neq i}$ for $1 \le k \le G - 1$,

$$
b_{\mathrm{pass@}k}\bigl(c^{(-i)}\bigr) = \frac{k\, c^{(-i)}}{G - 1}\frac{\binom{G - 1 - c^{(-i)}}{k - 1}}{\binom{G - 2}{k - 1}} = \frac{c^{(-i)}\binom{G - 1 - c^{(-i)}}{k - 1}}{\binom{G - 1}{k}},
\tag{5}
$$

leaves $\mathbb{E}\bigl[b_{\mathrm{pass@}k}(c^{(-i)}) S_i\bigr] = \mathbb{E}[b_{\mathrm{pass@}k}(c^{(-i)})]\,\mathbb{E}[S_i] = \mathbf{0}$ by independence of $Y_{(-i)}$ and $Y_i$. Setting $w_i^{\mathrm{LOO}} = \frac{1}{G}\bigl(f(c^{(-i)}) r_i - b_{\mathrm{pass@}k}(c^{(-i)})\bigr)$, Pascal's identity gives $w_i^{\mathrm{LOO}} = 0$ for $c \in \{0, G\}$ and, for $1 \le c \le G - 1$,

$$
c\, w_+^{\mathrm{LOO}}(c) = -(G - c)\, w_-^{\mathrm{LOO}}(c) = \frac{k c}{G}\frac{\binom{G - c}{k}}{\binom{G - 1}{k}} \equiv M_{\mathrm{pass@}k}^{\mathrm{LOO}}(c), \qquad \hat{\mathbf{g}}_{\mathrm{LOO}}^{(k)}(q) = M_{\mathrm{pass@}k}^{\mathrm{LOO}}(c)\bigl(\bar{\mathbf{g}}_+(q) - \bar{\mathbf{g}}_-(q)\bigr).
\tag{6}
$$

Dually, for $\operatorname{all@}m$ with $1 \le m \le G - 1$, the leave-one-out sub-group multiplier is

$$
M_{\mathrm{all@}m}^{\mathrm{LOO}}(c) = \frac{m(G - c)}{G}\frac{\binom{c}{m}}{\binom{G - 1}{m}}.
\tag{7}
$$

While $\hat{\mathbf{g}}_{\mathrm{LOO}}^{(k)}(q)$ satisfies $\sum_{i=1}^G w_i^{\mathrm{LOO}} = 0$ and $\mathbb{E}\bigl[\hat{\mathbf{g}}_{\mathrm{LOO}}^{(k)}(q)\bigr] = \nabla_\theta \operatorname{pass@}k(q; \theta)$, its signed token mass is

$$
\mathcal{M}_{\mathrm{tok}}\bigl(\hat{\mathbf{g}}_{\mathrm{LOO}}^{(k)}\bigr) = M_{\mathrm{pass@}k}^{\mathrm{LOO}}(c)\bigl(\bar{L}_+(q) - \bar{L}_-(q)\bigr),
\tag{8}
$$

which is strictly negative whenever $\bar{L}_-(q) > \bar{L}_+(q)$ and $1 \le c \le G - k$.

### 3.2 Raw negative-branch rescaling (`negscale`)

To enforce $\mathcal{M}_{\mathrm{tok}} = 0$ while retaining unit positive class weight on $M_{\mathrm{pass@}k}^{\mathrm{LOO}}(c)$, raw `negscale` [1] rescales only the negative branch by $\bar{L}_+(q)/\bar{L}_-(q)$:

$$
\hat{\mathbf{g}}_{\mathrm{raw-NS}}^{(k)}(q) = M_{\mathrm{pass@}k}^{\mathrm{LOO}}(c)\left(\bar{\mathbf{g}}_+(q) - \frac{\bar{L}_+(q)}{\bar{L}_-(q)}\,\bar{\mathbf{g}}_-(q)\right).
\tag{9}
$$

Here $\mathcal{M}_{\mathrm{tok}}\bigl(\hat{\mathbf{g}}_{\mathrm{raw-NS}}^{(k)}\bigr) = M_{\mathrm{pass@}k}^{\mathrm{LOO}}(c)\bigl(\bar{L}_+(q) - \frac{\bar{L}_+(q)}{\bar{L}_-(q)}\bar{L}_-(q)\bigr) = 0$ identically, but each failed trajectory $i$ ($r_i = 0$) receives weight $w_i = -\frac{M_{\mathrm{pass@}k}^{\mathrm{LOO}}(c)}{G - c}\frac{\bar{L}_+(q)}{\bar{L}_-(q)}$, which depends on its own length $L_i$ through the denominator $\bar{L}_-(q) = \frac{1}{G-c}\sum_{u: r_u=0} L_u$.

### 3.3 Leave-two-out opposite-class length-multiplied estimator ($1 \le k, m \le G - 1$)

To remove self-length coupling while maintaining $\mathcal{M}_{\mathrm{tok}} = 0$ across all $1 \le k \le G - 1$, define for each pair of distinct indices $i \neq j$ the leave-two-out success count $c^{(-i,-j)} = \sum_{u \notin \{i, j\}} r_u \in \{0, \dots, G - 2\}$. For a fixed positive constant $C > 0$, define the per-trajectory coefficient $c_i^{(k)}$ and direct weight $w_i^{(k)} = c_i^{(k)} / G$ by

$$
c_i^{(k)} = \frac{k}{(G - 1) C}\sum_{j \neq i} L_j(r_i - r_j)\frac{\binom{G - 2 - c^{(-i,-j)}}{k - 1}}{\binom{G - 2}{k - 1}}, \qquad \hat{\mathbf{g}}_{\mathrm{pair-L}}^{(k)}(q) = \frac{1}{G}\sum_{i=1}^G c_i^{(k)} S_i = \sum_{i=1}^G w_i^{(k)} S_i.
\tag{10}
$$

Dually, for $\operatorname{all@}m$ ($1 \le m \le G - 1$), replace $\binom{G - 2 - c^{(-i,-j)}}{k - 1}/\binom{G - 2}{k - 1}$ in (10) by $\binom{c^{(-i,-j)}}{m - 1}/\binom{G - 2}{m - 1}$ and $k$ by $m$.

On any realization, $r_i - r_j = 0$ on concordant pairs ($r_i = r_j$), whereas on every discordant pair ($r_i \neq r_j$), $r_i + r_j = 1$ implies $c^{(-i,-j)} = c - r_i - r_j = c - 1$. Using $\frac{k}{G(G-1)}\frac{\binom{G-1-c}{k-1}}{\binom{G-2}{k-1}} = \frac{M_{\mathrm{pass@}k}^{\mathrm{LOO}}(c)}{c(G-c)}$ for $1 \le c \le G - 1$, summing (10) over $j \neq i$ yields

$$
\hat{\mathbf{g}}_{\mathrm{pair-L}}^{(k)}(q) = \frac{M_{\mathrm{pass@}k}^{\mathrm{LOO}}(c)}{C}\Bigl(\bar{L}_-(q)\,\bar{\mathbf{g}}_+(q) - \bar{L}_+(q)\,\bar{\mathbf{g}}_-(q)\Bigr) = \frac{\bar{L}_-(q)}{C}\,\hat{\mathbf{g}}_{\mathrm{raw-NS}}^{(k)}(q).
\tag{11}
$$

At $k = 1$, $M_{\mathrm{pass@}1}^{\mathrm{LOO}}(c) = \frac{c(G-c)}{G(G-1)}$ and (10)–(11) reduce to the $k = 1$ pairwise control variate of [9].

---

## 4. Universal $\mathbb{E}_p[L]$ factorization, finite-sample impossibility, and Bernstein uniqueness

We first establish that on the two-length binary sub-family, the factor $\mathbb{E}_p[L]$ is forced on **every** fixed-$N$ sample-only estimator with per-realization zero signed token mass.

**Assumption 1 (Fixed-$N$ sample-only zero-token-mass class $\mathcal{E}_N$).** Fix an integer $N \ge 2$. An estimator $\hat{\mathbf{g}}(q) = \sum_{i=1}^N w_i(r_{1:N}, L_{1:N}) S_i$ belongs to $\mathcal{E}_N$ if:
1. $(Y_1, \dots, Y_N) \stackrel{\text{i.i.d.}}{\sim} \pi_\theta(\cdot \mid q)$ are $N$ on-policy rollouts (which may include $G$ scoring rollouts and $M_{\mathrm{aux}} = N - G \ge 0$ independent auxiliary on-policy rollouts with $w_{G+1} = \dots = w_N = 0$);
2. Each weight $w_i: \{0, 1\}^N \times (0, \infty)^N \to \mathbb{R}$ is a deterministic function solely of the realized rewards and lengths $(r_{1:N}, L_{1:N})$, with no direct dependence on $p(q; \theta)$ or $\mathbb{E}_\theta[L \mid q]$;
3. $\sum_{i=1}^N L_i\, w_i(r_{1:N}, L_{1:N}) = 0$ holds on every realization $(r_{1:N}, L_{1:N})$.

**Proposition 1 (Universal $\mathbb{E}_p[L]$ factorization on the two-length binary family).** *Fix $N \ge 2$ and consider any two-length binary policy on question $q$ where trajectories with $R(y) = 1$ have length $\ell_+ > 0$ and total probability $p \in (0, 1)$ (with aggregate score $S_+ = \frac{1}{p}\nabla_\theta p$), and trajectories with $R(y) = 0$ have length $\ell_- > 0$ and total probability $1 - p$ (with aggregate score $S_- = -\frac{1}{1-p}\nabla_\theta p$). For every estimator $\hat{\mathbf{g}} \in \mathcal{E}_N$, its expectation factors as*

$$
\mathbb{E}_p\bigl[\hat{\mathbf{g}}(q)\bigr] = \mathbb{E}_p[L]\, Q(p; \ell_+, \ell_-)\, \nabla_\theta p,
\tag{12}
$$

*where $\mathbb{E}_p[L] = (1 - p)\ell_- + p\ell_+$ and $Q(p; \ell_+, \ell_-)$ is a polynomial in $p$ of degree at most $N - 2$ given explicitly by*

$$
Q(p; \ell_+, \ell_-) = \frac{1}{\ell_-}\sum_{c=1}^{N-1} x_c(\ell_+, \ell_-)\, p^{c-1}(1 - p)^{N - c - 1}, \qquad x_c(\ell_+, \ell_-) \equiv \sum_{\substack{r_{1:N} \in \{0,1\}^N \\ \sum_{i=1}^N r_i = c}} \sum_{i: r_i = 1} w_i(r_{1:N}; \ell_+, \ell_-).
\tag{13}
$$

**Proof.** On any realization $r_{1:N} \in \{0, 1\}^N$ with $c = \sum_{i=1}^N r_i$, every positive rollout has $L_i = \ell_+$ and score $S_+$ and every negative rollout has $L_i = \ell_-$ and score $S_-$. Write $W_+(r_{1:N}) = \sum_{i: r_i = 1} w_i$ and $W_-(r_{1:N}) = \sum_{i: r_i = 0} w_i$.
- If $c = 0$, all $N$ rollouts have $r_i = 0$ and $L_i = \ell_- > 0$. Token-mass balance $\ell_- W_-(r_{1:N}) = 0$ implies $W_-(r_{1:N}) = 0$, so $\sum_{i=1}^N w_i S_i = W_-(r_{1:N}) S_- = \mathbf{0}$.
- If $c = N$, all $N$ rollouts have $r_i = 1$ and $L_i = \ell_+ > 0$. Token-mass balance $\ell_+ W_+(r_{1:N}) = 0$ implies $W_+(r_{1:N}) = 0$, so $\sum_{i=1}^N w_i S_i = W_+(r_{1:N}) S_+ = \mathbf{0}$.
- If $1 \le c \le N - 1$, token-mass balance $\ell_+ W_+(r_{1:N}) + \ell_- W_-(r_{1:N}) = 0$ implies $W_-(r_{1:N}) = -\frac{\ell_+}{\ell_-} W_+(r_{1:N})$. Hence

$$
\sum_{i=1}^N w_i S_i = W_+(r_{1:N}) S_+ + W_-(r_{1:N}) S_- = W_+(r_{1:N})\left(\frac{1}{p} + \frac{\ell_+}{\ell_-(1 - p)}\right)\nabla_\theta p.
$$

Multiplying by the realization probability $p^c(1 - p)^{N - c}$ and observing that

$$
\left(\frac{1}{p} + \frac{\ell_+}{\ell_-(1 - p)}\right) p^c(1 - p)^{N - c} = \frac{(1 - p)\ell_- + p\ell_+}{\ell_-}\, p^{c-1}(1 - p)^{N - c - 1} = \frac{\mathbb{E}_p[L]}{\ell_-}\, p^{c-1}(1 - p)^{N - c - 1},
$$

summing over $c \in \{1, \dots, N - 1\}$ yields (12)–(13). Since $1 \le c \le N - 1$, each term $p^{c-1}(1 - p)^{N - c - 1}$ has degree $N - 2$ in $p$. $\square$

**Theorem 1 (Finite-sample impossibility of eliminating $\mathbb{E}_p[L]$).** *Under Assumption 1, fix any finite sample budget $N \ge 2$, any target index $k \ge 1$ (or $m \ge 1$), and any two-length binary family with $\ell_+ > 0$, $\ell_- > 0$, and $\ell_+ \neq \ell_-$. There does **not** exist any estimator $\hat{\mathbf{g}} \in \mathcal{E}_N$ and any nonzero $p$-independent constant $\alpha_0 = \alpha_0(\ell_+, \ell_-) \neq 0$ such that*

$$
\mathbb{E}_p\bigl[\hat{\mathbf{g}}(q)\bigr] = \alpha_0\, \nabla_\theta \operatorname{pass@}k(q; \theta) \quad \text{for all } p \in (0, 1)
\tag{14}
$$

*(or $\mathbb{E}_p[\hat{\mathbf{g}}(q)] = \alpha_0\, \nabla_\theta \operatorname{all@}m(q; \theta)$ for all $p \in (0, 1)$). In particular, this impossibility holds at $k = 1$ (ordinary expected reward).*

**Proof.** Suppose toward a contradiction that (14) holds for all $p \in (0, 1)$ on a smoothly parameterized policy with $\nabla_\theta p \neq \mathbf{0}$. By Proposition 1 and (1), the identity

$$
\bigl((1 - p)\ell_- + p\ell_+\bigr)\, Q(p; \ell_+, \ell_-) = \alpha_0\, k(1 - p)^{k - 1}
\tag{15}
$$

holds for all $p \in (0, 1)$. Because both sides of (15) are polynomials in $p$ that agree on the open interval $(0, 1)$, they are identical in the polynomial ring $\mathbb{R}[p]$ and therefore agree at every $p \in \mathbb{R}$. Since $\ell_+ \neq \ell_-$ and $\ell_+, \ell_- > 0$, the linear factor $(1 - p)\ell_- + p\ell_+ = \ell_- - (\ell_- - \ell_+)p$ has the real root

$$
p^* = \frac{\ell_-}{\ell_- - \ell_+} \notin \{0, 1\}.
\tag{16}
$$

Evaluating the left-hand side of (15) at $p = p^*$ gives $0 \cdot Q(p^*; \ell_+, \ell_-) = 0$. Evaluating the right-hand side of (15) at $p = p^*$ gives

$$
\alpha_0\, k(1 - p^*)^{k - 1} = \alpha_0\, k\left(\frac{-\ell_+}{\ell_- - \ell_+}\right)^{k - 1} \neq 0,
$$

since $\alpha_0 \neq 0$, $k \ge 1$, and $\ell_+ > 0$. This contradiction proves (14) is impossible for $\operatorname{pass@}k$. The identical evaluation at $p = p^*$ for $\operatorname{all@}m$ gives $\alpha_0\, m(p^*)^{m - 1} = \alpha_0\, m\bigl(\frac{\ell_-}{\ell_- - \ell_+}\bigr)^{m - 1} \neq 0$, a contradiction. $\square$

*Scope of Theorem 1.* Theorem 1 rules out every sample-only functional form $w_i(r_{1:N}, L_{1:N})$ over a fixed finite sample size $N = G + M_{\mathrm{aux}}$—including dividing $\hat{\mathbf{g}}_{\mathrm{pair-L}}^{(k)}$ by the same group's sample mean length $\bar{L}$, harmonic mean, geometric mean, or any function of $M_{\mathrm{aux}} < \infty$ independent auxiliary on-policy rollouts. It deliberately excludes oracle access to the true policy mean length $\mathbb{E}_p[L]$ (which would allow trivial division by $\mathbb{E}_p[L]$) as well as unbounded sequential stopping rules (where the number of rollouts $N$ is a random stopping time with unbounded support [12, 13]).

**Theorem 2 (Bernstein uniqueness for $1 \le k, m \le G - 1$, $k = G$ boundary failure, and general multi-length pairwise identity).** *Fix a group size $G \ge 2$ and constant $C > 0$.*
1. *(Stratum-sum uniqueness on the two-length family for $1 \le k, m \le G - 1$):* *For an estimator $\hat{\mathbf{g}} \in \mathcal{E}_G$ on the two-length binary family $(\ell_+, \ell_-)$, achieving*

$$
\mathbb{E}_p\bigl[\hat{\mathbf{g}}(q)\bigr] = \frac{\mathbb{E}_p[L]}{C}\,\nabla_\theta \operatorname{pass@}k(q; \theta) \quad \text{for all } p \in (0, 1)
\tag{17}
$$

*for $1 \le k \le G - 1$ uniquely determines the count-stratum positive-weight sums $x_c(\ell_+, \ell_-)$ in (13) as*

$$
x_c(\ell_+, \ell_-) = \frac{\ell_-}{C}\binom{G}{c} M_{\mathrm{pass@}k}^{\mathrm{LOO}}(c) = \frac{k\,\ell_-}{C}\binom{G - 1}{c - 1}\frac{\binom{G - c}{k}}{\binom{G - 1}{k}}, \qquad c \in \{1, \dots, G - 1\}.
\tag{18}
$$

*Dually, achieving $\mathbb{E}_p[\hat{\mathbf{g}}(q)] = \frac{\mathbb{E}_p[L]}{C}\nabla_\theta \operatorname{all@}m(q; \theta)$ for $1 \le m \le G - 1$ uniquely determines $x_c(\ell_+, \ell_-) = \frac{\ell_-}{C}\binom{G}{c} M_{\mathrm{all@}m}^{\mathrm{LOO}}(c)$. Without permutation symmetry, (18) determines the conditional mean of the positive-weight sum within each count stratum $c$; if $w_i$ is also permutation-symmetric across the $G$ rollouts, (18) uniquely determines the individual two-length weights $w_+(c; \ell_+, \ell_-) = \frac{\ell_-}{c C}M^{\mathrm{LOO}}(c)$ and $w_-(c; \ell_+, \ell_-) = -\frac{\ell_+}{(G-c)C}M^{\mathrm{LOO}}(c)$.*

2. *(Boundary impossibility at $k = G$ and $m = G$):* *For $k = G$ (or $m = G$), **no** estimator $\hat{\mathbf{g}} \in \mathcal{E}_G$ can satisfy (17) with any nonzero factor $\frac{\mathbb{E}_p[L]}{C}$ across $p \in (0, 1)$.*

3. *(Exact conditional expectation of $\hat{\mathbf{g}}_{\mathrm{pair-L}}^{(k)}$ across arbitrary multi-length policies):* *On any finite-support policy $\pi_\theta(\cdot \mid q)$ with arbitrary trajectory length distribution $L(y) > 0$, the leave-two-out pairwise estimator $\hat{\mathbf{g}}_{\mathrm{pair-L}}^{(k)}(q)$ in (10)–(11) satisfies $\mathcal{M}_{\mathrm{tok}}\bigl(\hat{\mathbf{g}}_{\mathrm{pair-L}}^{(k)}\bigr) = 0$ on every realization and, for every $1 \le k \le G - 1$,*

$$
\mathbb{E}_{Y_{1:G} \sim \pi_\theta(\cdot \mid q)^G}\Bigl[\hat{\mathbf{g}}_{\mathrm{pair-L}}^{(k)}(q)\Bigr] = \frac{\mathbb{E}_\theta[L \mid q]}{C}\,\nabla_\theta \operatorname{pass@}k(q; \theta)
\tag{19}
$$

*(and dually $\frac{\mathbb{E}_\theta[L \mid q]}{C}\nabla_\theta \operatorname{all@}m(q; \theta)$ for $1 \le m \le G - 1$).*

**Proof.**
*Parts 1 and 2:* By Proposition 1, (17) holds for all $p \in (0, 1)$ if and only if $Q(p; \ell_+, \ell_-) = \frac{k}{C}(1 - p)^{k - 1}$ as polynomials in $\mathbb{R}[p]$. For $k = G$ (or $m = G$), $\frac{G}{C}(1 - p)^{G - 1}$ (or $\frac{G}{C}p^{G - 1}$) has degree $G - 1$ in $p$, whereas $\deg_p Q \le G - 2$ by (13); hence equality is impossible. For $1 \le k \le G - 1$, expanding $(1 - p)^{k - 1} = (1 - p)^{k - 1}(p + (1 - p))^{G - 1 - k}$ in the Bernstein basis $\bigl\{p^{c-1}(1 - p)^{G - c - 1}\bigr\}_{c=1}^{G-1}$ of degree $G - 2$ via the hypergeometric identity $\binom{G - 1 - k}{c - 1} = \binom{G}{c}\frac{c}{G}\frac{\binom{G - c}{k}}{\binom{G - 1}{k}}$ gives

$$
\frac{k}{C}(1 - p)^{k - 1} = \frac{k}{C}\sum_{c=1}^{G-k} \binom{G - 1 - k}{c - 1} p^{c-1}(1 - p)^{G - c - 1} = \frac{1}{\ell_-}\sum_{c=1}^{G-1} \left[\frac{\ell_-}{C}\binom{G}{c} M_{\mathrm{pass@}k}^{\mathrm{LOO}}(c)\right] p^{c-1}(1 - p)^{G - c - 1}.
$$

Because the $G - 1$ polynomials $\bigl\{p^{c-1}(1 - p)^{G - c - 1}\bigr\}_{c=1}^{G-1}$ are linearly independent in $\mathbb{R}[p]$, equating coefficients with (13) uniquely forces (18) (and dually for $\operatorname{all@}m$). Under permutation symmetry across the $G$ indices, all $\binom{G}{c}$ realizations with $\sum r_i = c$ have identical positive weight sum $c\, w_+(c; \ell_+, \ell_-) = x_c(\ell_+, \ell_-) / \binom{G}{c} = \frac{\ell_-}{C}M^{\mathrm{LOO}}(c)$.

*Part 3:* By (10), $\mathcal{M}_{\mathrm{tok}}\bigl(\hat{\mathbf{g}}_{\mathrm{pair-L}}^{(k)}\bigr) = \frac{k}{G(G-1)C}\sum_{i \neq j} L_i L_j(r_i - r_j)\frac{\binom{G-2-c^{(-i,-j)}}{k-1}}{\binom{G-2}{k-1}} = 0$ because the summand is antisymmetric under exchanging $(i, j)$ while $c^{(-i,-j)} = c^{(-j,-i)}$ is symmetric. To compute the expectation across an arbitrary multi-length policy $\pi_\theta(\cdot \mid q)$, write (10) as a sum over all $G(G - 1)$ ordered pairs $(i, j)$ with $i \neq j$:

$$
\hat{\mathbf{g}}_{\mathrm{pair-L}}^{(k)}(q) = \frac{k}{G(G - 1) C}\sum_{i=1}^G \sum_{j \neq i} L_j(r_i - r_j)\,\frac{\binom{G - 2 - c^{(-i,-j)}}{k - 1}}{\binom{G - 2}{k - 1}}\, S_i.
\tag{20}
$$

Fix any ordered pair $(i, j)$ with $i \neq j$. The leave-two-out count $c^{(-i,-j)} = \sum_{u \notin \{i, j\}} r_u \sim \operatorname{Binomial}(G - 2, p(q; \theta))$ depends only on $Y_{(-i,-j)} = (Y_u)_{u \notin \{i, j\}}$, which is statistically independent of $(Y_i, Y_j)$. Taking the expectation over $Y_{(-i,-j)}$ gives

$$
\mathbb{E}_{Y_{(-i,-j)}}\!\left[\frac{\binom{G - 2 - c^{(-i,-j)}}{k - 1}}{\binom{G - 2}{k - 1}}\right] = \sum_{m=0}^{G - 1 - k} \binom{G - 2}{m}\frac{\binom{G - 2 - m}{k - 1}}{\binom{G - 2}{k - 1}}\, p^m(1 - p)^{G - 2 - m} = (1 - p)^{k - 1}
\tag{21}
$$

(and dually $\mathbb{E}\bigl[\binom{c^{(-i,-j)}}{m-1}/\binom{G-2}{m-1}\bigr] = p^{m - 1}$ for $\operatorname{all@}m$). Independently, for $(Y_i, Y_j) \stackrel{\text{i.i.d.}}{\sim} \pi_\theta(\cdot \mid q)^2$, the score identities $\mathbb{E}[S_i] = \sum_{y \in \mathcal{Y}_q} \nabla_\theta \pi_\theta(y \mid q) = \mathbf{0}$ and $\mathbb{E}[r_i S_i] = \sum_{y \in \mathcal{Y}_q} R(y)\nabla_\theta \pi_\theta(y \mid q) = \nabla_\theta p(q; \theta)$ yield

$$
\mathbb{E}_{(Y_i, Y_j)}\bigl[L_j(r_i - r_j) S_i\bigr] = \mathbb{E}[L_j]\,\mathbb{E}[r_i S_i] - \mathbb{E}[L_j r_j]\,\mathbb{E}[S_i] = \mathbb{E}_\theta[L \mid q]\,\nabla_\theta p(q; \theta) - \mathbb{E}[L_j r_j]\cdot \mathbf{0} = \mathbb{E}_\theta[L \mid q]\,\nabla_\theta p(q; \theta).
\tag{22}
$$

Multiplying (21) and (22) and summing over the $G(G - 1)$ ordered pairs $(i, j)$ gives (19). $\square$

---

## 5. Within-question directional rotation, cross-question sign reversal, and detached normalization

### 5.1 Within-question collinearity vs. directional rotation under variable failure lengths

On a fixed question $q$, Theorem 2(3) guarantees that $\mathbb{E}\bigl[\hat{\mathbf{g}}_{\mathrm{pair-L}}^{(k)}(q)\bigr] = \frac{\mathbb{E}_\theta[L \mid q]}{C}\nabla_\theta \operatorname{pass@}k(q; \theta)$ is positively collinear with $\nabla_\theta \operatorname{pass@}k(q; \theta)$ for every multi-length policy. By contrast, both raw `negscale` $\hat{\mathbf{g}}_{\mathrm{raw-NS}}^{(k)}(q)$ in (9) (which omits the group multiplier $\bar{L}_-(q)$) and the same-group mean-length normalized estimator $\hat{\mathbf{g}}_{\mathrm{pair-L}}^{(k)}(q) / \bar{L}(q)$ (where $\bar{L}(q) = \frac{1}{G}\sum_{i=1}^G L_i$) place a group-length average in the denominator. When trajectories within the same reward class carry **both** distinct lengths and distinct score vectors, conditioning on $\bar{L}_-(q)$ or $\bar{L}(q)$ weights those trajectories unequally and can rotate the expected gradient vector away from $\nabla_\theta \operatorname{pass@}k(q; \theta)$.

**Theorem 3(a) (Within-question directional rotation witness).** *Consider a single question $q$ with three trajectory types $y \in \{0, 1, 2\}$, rewards $R = (1, 0, 0)$, lengths $L = (2, 3, 6)$, and softmax probabilities $p_y(\theta_0, \theta_1) = \frac{e^{\theta_y}}{e^{\theta_0} + e^{\theta_1} + 1}$ ($\theta_2 \equiv 0$) evaluated at $\theta_0 = \theta_1 = 0$, where $p = \bigl(\frac{1}{3}, \frac{1}{3}, \frac{1}{3}\bigr)$, $p(q; \theta) = p_0 = \frac{1}{3}$, and $\mathbb{E}_\theta[L \mid q] = \frac{11}{3}$. At group size $G = 4$ and $C = 1$, for every $k \in \{1, 2, 3\}$, the true gradient $\nabla_{(\theta_0, \theta_1)} \operatorname{pass@}k(q; \theta) = \frac{k}{9}\bigl(\frac{2}{3}\bigr)^{k-1}(2, -1)$ satisfies $g_0 + 2 g_1 = 0$, and $\mathbb{E}\bigl[\hat{\mathbf{g}}_{\mathrm{pair-L}}^{(k)}(q)\bigr] = \frac{11}{3}\nabla_\theta \operatorname{pass@}k(q; \theta)$ identically. In contrast, both $\mathbb{E}\bigl[\hat{\mathbf{g}}_{\mathrm{raw-NS}}^{(k)}(q)\bigr]$ and $\mathbb{E}\bigl[\hat{\mathbf{g}}_{\mathrm{pair-L}}^{(k)}(q) / \bar{L}(q)\bigr]$ satisfy $g_0 + 2 g_1 \neq 0$ and are **not collinear** with $\nabla_\theta \operatorname{pass@}k(q; \theta)$, taking the exact rational values in Table 1.*

**Table 1.** Exact expected gradient vectors on the three-type variable-length policy ($G = 4$, $L = (2, 3, 6)$, $R = (1, 0, 0)$, $p = (1/3, 1/3, 1/3)$, $\mathbb{E}[L] = 11/3$, $C = 1$). Collinearity with $\nabla_\theta \operatorname{pass@}k$ requires $g_0 + 2 g_1 = 0$.

| $k$ | $\nabla_\theta \operatorname{pass@}k(q; \theta)$ | $\mathbb{E}[L]\nabla_\theta \operatorname{pass@}k = \mathbb{E}\bigl[\hat{\mathbf{g}}_{\mathrm{pair-L}}^{(k)}\bigr]$ | $\mathbb{E}\bigl[\hat{\mathbf{g}}_{\mathrm{raw-NS}}^{(k)}\bigr]$ ($1/\bar{L}_-$ denominator) | $\mathbb{E}\bigl[\hat{\mathbf{g}}_{\mathrm{pair-L}}^{(k)} / \bar{L}\bigr]$ ($1/\bar{L}$ denominator) |
| :---: | :---: | :---: | :---: | :---: |
| $1$ | $\left(\frac{2}{9},\, -\frac{1}{9}\right)$ | $\left(\frac{22}{27},\, -\frac{11}{27}\right)$ | $\left(\frac{4003}{21870},\, -\frac{439}{4374}\right)$ | $\left(\frac{44346823}{186080895},\, -\frac{23609606}{186080895}\right)$ |
| $2$ | $\left(\frac{8}{27},\, -\frac{4}{27}\right)$ | $\left(\frac{88}{81},\, -\frac{44}{81}\right)$ | $\left(\frac{2663}{10935},\, -\frac{287}{2187}\right)$ | $\left(\frac{1232723}{4135131},\, -\frac{670592}{4135131}\right)$ |
| $3$ | $\left(\frac{8}{27},\, -\frac{4}{27}\right)$ | $\left(\frac{88}{81},\, -\frac{44}{81}\right)$ | $\left(\frac{197}{810},\, -\frac{7}{54}\right)$ | $\left(\frac{148906}{530145},\, -\frac{81197}{530145}\right)$ |

**Proof.** At $p = (1/3, 1/3, 1/3)$, the score vectors with respect to $(\theta_0, \theta_1)$ are $S(0) = (2/3, -1/3)$, $S(1) = (-1/3, 2/3)$, and $S(2) = (-1/3, -1/3)$. Because failure type $y = 1$ ($L = 3$) has positive $\theta_1$-score $+2/3$ whereas failure type $y = 2$ ($L = 6$) has negative $\theta_1$-score $-1/3$, realizations with shorter failure length $L = 3$ have smaller $\bar{L}_-$ and smaller $\bar{L}$, receiving larger weight under $1/\bar{L}_-$ and $1/\bar{L}$ than realizations with $L = 6$. Direct summation over all $3^4 = 81$ four-trajectory realizations (verified in `check_exact.py`) yields:
- For $\hat{\mathbf{g}}_{\mathrm{raw-NS}}^{(k)}$: $g_0 + 2 g_1 = -\frac{389}{21870} \neq 0$ ($k = 1$), $-\frac{209}{10935} \neq 0$ ($k = 2$), and $-\frac{13}{810} \neq 0$ ($k = 3$).
- For $\hat{\mathbf{g}}_{\mathrm{pair-L}}^{(k)} / \bar{L}$: $g_0 + 2 g_1 = -\frac{2872389}{186080895} \neq 0$ ($k = 1$), $-\frac{108461}{4135131} \neq 0$ ($k = 2$), and $-\frac{13488}{530145} \neq 0$ ($k = 3$). $\square$

*Remark 1 (Variable failure lengths alone do not force rotation when failure scores coincide).* Variable failure lengths are necessary but not sufficient for directional rotation. In the same three-type space $L = (2, 3, 6), R = (1, 0, 0)$, suppose the policy is parameterized by $p(\theta) = \bigl(p_s(\theta), \frac{1 - p_s(\theta)}{2}, \frac{1 - p_s(\theta)}{2}\bigr)$ with $p_s(\theta) = \sigma(\theta_1 + 2\theta_2)$. Then both failure types $y \in \{1, 2\}$ share the **same** score vector $S(1) = S(2) = -\frac{1}{1 - p_s}\nabla_\theta p_s \propto (-1, -2)$, while $S(0) = \frac{1}{p_s}\nabla_\theta p_s \propto (1, 2)$. Consequently, $\bar{\mathbf{g}}_+(q)$ and $-\bar{\mathbf{g}}_-(q)$ point strictly along $(1, 2)$ on every mixed realization regardless of which failure lengths occur, so both $\mathbb{E}\bigl[\hat{\mathbf{g}}_{\mathrm{raw-NS}}^{(k)}(q)\bigr]$ and $\mathbb{E}\bigl[\hat{\mathbf{g}}_{\mathrm{pair-L}}^{(k)}(q) / \bar{L}(q)\bigr]$ remain positively collinear with $\nabla_\theta \operatorname{pass@}k(q; \theta) \propto (1, 2)$ (verified in `check_exact.py`). Directional rotation occurs specifically when trajectories within a reward class vary in **both** length and score direction.

### 5.2 Cross-question weighting and multi-question ascent-direction reversal

Consider now a batch or dataset of multiple questions $\mathcal{Q} = \{q_1, \dots, q_B\}$ with the unweighted question-averaged $\operatorname{pass@}k$ objective

$$
J_k(\theta) = \frac{1}{B}\sum_{b=1}^B \operatorname{pass@}k(q_b; \theta), \qquad \nabla_\theta J_k(\theta) = \frac{1}{B}\sum_{b=1}^B k\bigl(1 - p(q_b; \theta)\bigr)^{k-1}\nabla_\theta p(q_b; \theta).
\tag{23}
$$

When a zero-signed-token-mass estimator satisfying (19) with a shared constant $C > 0$ is averaged across $\mathcal{Q}$, its batch expectation is

$$
\mathbb{E}\bigl[\hat{\mathbf{g}}_{\mathrm{batch}}^{(k)}\bigr] = \frac{1}{B}\sum_{b=1}^B \frac{\mathbb{E}_\theta[L \mid q_b]}{C}\, k\bigl(1 - p(q_b; \theta)\bigr)^{k-1}\nabla_\theta p(q_b; \theta).
\tag{24}
$$

Because $\mathbb{E}_\theta[L \mid q_b] = p(q_b; \theta)\bar{\ell}_+(q_b; \theta) + \bigl(1 - p(q_b; \theta)\bigr)\bar{\ell}_-(q_b; \theta)$ weights each question by its current expected length, questions with long failure trajectories receive amplified weight relative to questions with short failure trajectories.

**Theorem 3(b) (Cross-question drift on a flat $k=1$ objective and strict ascent-direction reversal for $k \ge 2$).** *Consider a two-question batch $\mathcal{Q} = \{q_1, q_2\}$ with scalar parameter $\theta \in \mathbb{R}$, shared constant $C = 1$, and two-length binary policies:*
- *On $q_1$: $(\ell_+, \ell_-) = (1, 10)$ and $p_1(\theta) = \sigma(\theta) = (1 + e^{-\theta})^{-1}$;*
- *On $q_2$: $(\ell_+, \ell_-) = (1, 2)$ and $p_2(\theta) = \sigma(-\theta) = 1 - p_1(\theta)$.*

*Evaluate at $\theta = \log(3/2) > 0$, where $p_1 = \frac{3}{5}$, $p_2 = \frac{2}{5}$, $\frac{dp_1}{d\theta} = +\frac{6}{25}$, $\frac{dp_2}{d\theta} = -\frac{6}{25}$, $\mathbb{E}_\theta[L \mid q_1] = \frac{3}{5}(1) + \frac{2}{5}(10) = \frac{23}{5}$, and $\mathbb{E}_\theta[L \mid q_2] = \frac{2}{5}(1) + \frac{3}{5}(2) = \frac{8}{5}$. Then:*
1. *(Nonzero expected drift on a flat objective at $k = 1$):* *Because $p_2(\theta) = 1 - p_1(\theta)$, the unweighted $k = 1$ objective is identically constant across all $\theta \in \mathbb{R}$,*

$$
J_1(\theta) = \frac{1}{2}\bigl(p_1(\theta) + p_2(\theta)\bigr) \equiv \frac{1}{2}, \qquad \frac{dJ_1}{d\theta}(\theta) \equiv 0,
\tag{25}
$$

*yet at $\theta = \log(3/2)$ the expected zero-signed-token-mass batch gradient is strictly positive:*

$$
\mathbb{E}\bigl[\hat{g}_{\mathrm{batch}}^{(1)}\bigr] = \frac{1}{2}\left(\frac{23}{5}\cdot \frac{6}{25} - \frac{8}{5}\cdot \frac{6}{25}\right) = +\frac{9}{25} > 0.
\tag{26}
$$

2. *(Strict reversal of the multi-question ascent direction at $k = 2$ and $k = 3$):* *For $k \ge 2$, $J_k(\theta) = \frac{1}{2}\bigl[1 - (1 - p_1(\theta))^k + 1 - p_1(\theta)^k\bigr]$ is strictly concave in $p_1 \in [0, 1]$ and attains its unique global maximum at $\theta = 0$ ($p_1 = p_2 = \frac{1}{2}$). At $\theta = \log(3/2) > 0$, the true derivatives point strictly toward the optimum $\theta = 0$,*

$$
\frac{dJ_2}{d\theta} = \frac{1}{2}\left(2\cdot \frac{2}{5}\cdot \frac{6}{25} - 2\cdot \frac{3}{5}\cdot \frac{6}{25}\right) = -\frac{6}{125} < 0, \qquad \frac{dJ_3}{d\theta} = \frac{1}{2}\left(3\cdot \frac{4}{25}\cdot \frac{6}{25} - 3\cdot \frac{9}{25}\cdot \frac{6}{25}\right) = -\frac{9}{125} < 0,
\tag{27}
$$

*whereas the expected zero-signed-token-mass batch gradients are strictly positive,*

$$
\mathbb{E}\bigl[\hat{g}_{\mathrm{batch}}^{(2)}\bigr] = \frac{1}{2}\left(\frac{23}{5}\cdot \frac{12}{125} - \frac{8}{5}\cdot \frac{18}{125}\right) = +\frac{132}{625} > 0, \qquad \mathbb{E}\bigl[\hat{g}_{\mathrm{batch}}^{(3)}\bigr] = \frac{1}{2}\left(\frac{23}{5}\cdot \frac{72}{625} - \frac{8}{5}\cdot \frac{162}{625}\right) = +\frac{36}{625} > 0,
\tag{28}
$$

*so $\frac{dJ_k}{d\theta}\,\mathbb{E}\bigl[\hat{g}_{\mathrm{batch}}^{(k)}\bigr] < 0$ for both $k = 2$ and $k = 3$. A sufficiently small step along the expected batch ascent direction strictly decreases $J_2(\theta)$ and $J_3(\theta)$ to first order.*

**Proof.** Direct substitution into (23) and (24) yields (25)–(28) (verified in `check_exact.py`). $\square$

### 5.3 Statistically detached normalization

Comparing Theorem 1, Theorem 3(a), and Theorem 3(b) clarifies what an auxiliary or historical per-question length normalizer can and cannot achieve. By **"statistically detached from the scoring group"**, we mean a random variable $\psi_q$ that is **statistically independent of the fresh scoring group $(Y_1, \dots, Y_G)$ conditional on $(q, \theta)$ and any prior tracker history $\mathcal{H}_{<t}$**. Applying an automatic-differentiation stop-gradient operator (`.detach()`) to the same group's sample mean length $\bar{L}(Y_{1:G})$ does **not** make it statistically independent of $(Y_1, \dots, Y_G)$, because $\bar{L}(Y_{1:G})$ remains a function of the same random draws $(Y_1, \dots, Y_G)$ that determine $S_1, \dots, S_G$, producing the within-question directional rotation in Theorem 3(a).

**Corollary 1 (Properties of statistically detached length normalizers).** *Let $(Y_1, \dots, Y_G) \stackrel{\text{i.i.d.}}{\sim} \pi_\theta(\cdot \mid q)$ be the fresh scoring group on question $q$, and let $\psi_q > 0$ be any positive scalar random variable with $\mathbb{E}[\psi_q \mid q, \theta, \mathcal{H}_{<t}] < \infty$ that is statistically independent of $(Y_1, \dots, Y_G)$ conditional on $(q, \theta, \mathcal{H}_{<t})$. Define $\hat{\mathbf{g}}_{\mathrm{det}}^{(k)}(q) = \psi_q\, \hat{\mathbf{g}}_{\mathrm{pair-L}}^{(k)}(q)$ with $C = 1$. Then:*
1. *(Exact per-realization zero signed token mass and conditional expected collinearity):* *$\mathcal{M}_{\mathrm{tok}}\bigl(\hat{\mathbf{g}}_{\mathrm{det}}^{(k)}\bigr) = \psi_q\,\mathcal{M}_{\mathrm{tok}}\bigl(\hat{\mathbf{g}}_{\mathrm{pair-L}}^{(k)}\bigr) = 0$ on every realization, and for every $1 \le k \le G - 1$, the **conditional expected gradient vector** satisfies*

$$
\mathbb{E}\Bigl[\hat{\mathbf{g}}_{\mathrm{det}}^{(k)}(q) \;\Big|\; q, \theta, \mathcal{H}_{<t}\Bigr] = \Bigl(\mathbb{E}\bigl[\psi_q \mid q, \theta, \mathcal{H}_{<t}\bigr]\, \mathbb{E}_\theta[L \mid q]\Bigr)\, \nabla_\theta \operatorname{pass@}k(q; \theta),
\tag{29}
$$

*which is positively collinear with $\nabla_\theta \operatorname{pass@}k(q; \theta)$ across arbitrary multi-length policies (with zero angular bias in the conditional expected vector; individual stochastic realizations retain sampling variance).*

2. *(Reciprocal sample mean of $M_{\mathrm{aux}}$ auxiliary on-policy rollouts):* *If $\psi_q = 1 / \bar{L}_{\mathrm{aux}}$ where $\bar{L}_{\mathrm{aux}} = \frac{1}{M_{\mathrm{aux}}}\sum_{m=1}^{M_{\mathrm{aux}}} L(Y_{G+m})$ is the sample mean length of $M_{\mathrm{aux}} \ge 1$ independent on-policy auxiliary rollouts $Y_{G+1}, \dots, Y_{G+M_{\mathrm{aux}}} \stackrel{\text{i.i.d.}}{\sim} \pi_\theta(\cdot \mid q)$, and if $L(Y) > 0$ has non-degenerate distribution under $\pi_\theta(\cdot \mid q)$ ($\operatorname{Var}_\theta(L \mid q) > 0$), then by strict convexity of $x \mapsto 1/x$ on $(0, \infty)$ and Jensen's inequality,*

$$
\mathbb{E}_\theta\bigl[1 / \bar{L}_{\mathrm{aux}} \mid q\bigr]\, \mathbb{E}_\theta[L \mid q] > 1.
\tag{30}
$$

3. *(Bounded-length positive truncated geometric-series normalizer):* *If trajectory lengths satisfy a known positive bound $0 < L_{\min} \le L(y) \le L_{\max} < \infty$ for all $y \in \mathcal{Y}_q$, then for $M_{\mathrm{aux}} \ge 1$ independent on-policy auxiliary rollouts $Y_{G+1}, \dots, Y_{G+M_{\mathrm{aux}}} \stackrel{\text{i.i.d.}}{\sim} \pi_\theta(\cdot \mid q)$, the strictly positive estimator*

$$
\psi_{M_{\mathrm{aux}}}(Y_{G+1:G+M_{\mathrm{aux}}}) = \frac{1}{L_{\max}}\sum_{j=0}^{M_{\mathrm{aux}}} \prod_{m=1}^{j} \left(1 - \frac{L(Y_{G+m})}{L_{\max}}\right) > 0
\tag{31}
$$

*satisfies*

$$
\mathbb{E}_\theta\bigl[\psi_{M_{\mathrm{aux}}} \mid q\bigr]\, \mathbb{E}_\theta[L \mid q] = 1 - \left(1 - \frac{\mathbb{E}_\theta[L \mid q]}{L_{\max}}\right)^{M_{\mathrm{aux}} + 1} \in \left[1 - \left(1 - \frac{L_{\min}}{L_{\max}}\right)^{M_{\mathrm{aux}} + 1},\, 1\right),
\tag{32}
$$

*so the cross-question multiplicative bias $1 - \mathbb{E}_\theta[\psi_{M_{\mathrm{aux}}} \mid q]\,\mathbb{E}_\theta[L \mid q] = \bigl(1 - \mathbb{E}_\theta[L \mid q]/L_{\max}\bigr)^{M_{\mathrm{aux}}+1}$ decays exponentially in $M_{\mathrm{aux}}$ while vanishing at $p = p^*$ in accordance with Theorem 1.*

**Proof.** Part 1 follows by conditioning on $(q, \theta, \mathcal{H}_{<t})$, factoring out $\mathbb{E}[\psi_q \mid q, \theta, \mathcal{H}_{<t}]$ by conditional independence of $\psi_q$ and $(Y_1, \dots, Y_G)$, and applying Theorem 2(3). Part 2 follows because $\operatorname{Var}_\theta(\bar{L}_{\mathrm{aux}} \mid q) = \operatorname{Var}_\theta(L \mid q) / M_{\mathrm{aux}} > 0$ and $x \mapsto 1/x$ is strictly convex on $(0, \infty)$, so $\mathbb{E}[1/\bar{L}_{\mathrm{aux}}] > 1/\mathbb{E}[\bar{L}_{\mathrm{aux}}] = 1/\mathbb{E}_\theta[L \mid q]$. For Part 3, $L(Y_{G+m}) \in [L_{\min}, L_{\max}]$ implies $1 - L(Y_{G+m})/L_{\max} \in [0, 1 - L_{\min}/L_{\max}]$ and the $j = 0$ term in (31) is $1/L_{\max} > 0$, so $\psi_{M_{\mathrm{aux}}} \ge 1/L_{\max} > 0$. By i.i.d. independence of $Y_{G+1}, \dots, Y_{G+M_{\mathrm{aux}}}$,

$$
\mathbb{E}_\theta\bigl[\psi_{M_{\mathrm{aux}}} \mid q\bigr] = \frac{1}{L_{\max}}\sum_{j=0}^{M_{\mathrm{aux}}} \left(1 - \frac{\mathbb{E}_\theta[L \mid q]}{L_{\max}}\right)^j = \frac{1 - \bigl(1 - \mathbb{E}_\theta[L \mid q]/L_{\max}\bigr)^{M_{\mathrm{aux}} + 1}}{\mathbb{E}_\theta[L \mid q]},
$$

which gives (32). $\square$

**Table 2.** Exact cross-question scalar factor $\mathbb{E}[\psi_q]\,\mathbb{E}_p[L]$ under $M_{\mathrm{aux}}$ independent auxiliary rollouts on the two-length binary witness ($\ell_+ = 2$, $\ell_- = 5$, $L_{\max} = 6$, $p = 2/5$, $\mathbb{E}_p[L] = 19/5$).

| $M_{\mathrm{aux}}$ | $\mathbb{E}\bigl[1 / \bar{L}_{\mathrm{aux}}\bigr]\,\mathbb{E}_p[L]$ (Strict Jensen $> 1$) | $\mathbb{E}\bigl[\psi_{M_{\mathrm{aux}}}\bigr]\,\mathbb{E}_p[L] = 1 - (11/30)^{M_{\mathrm{aux}}+1}$ | Relative Bias $(11/30)^{M_{\mathrm{aux}}+1}$ |
| :---: | :---: | :---: | :---: |
| $1$ | $\frac{152}{125} = 1.216$ | $\frac{779}{900} \approx 0.8656$ | $\frac{121}{900} \approx 0.1344$ |
| $2$ | $\frac{4807}{4375} \approx 1.0987$ | $\frac{25669}{27000} \approx 0.9507$ | $\frac{1331}{27000} \approx 0.0493$ |
| $3$ | $\frac{6631}{6250} \approx 1.0610$ | $\frac{795359}{810000} \approx 0.9819$ | $\frac{14641}{810000} \approx 0.0181$ |

---

## 6. Limitations, scope, and reproduction

**Scope and limitations.** Our results characterize the exact first-moment properties of matched on-policy, unstandardized, unclipped score-function estimators:
1. They do **not** analyze division by the group reward standard deviation $\hat{\sigma}_r(q) = \sqrt{\frac{c(G-c)}{G^2}}$, off-policy importance ratios under $T \neq 1$ or top-$p$ sampling, PPO clipping, KL penalties away from reference equality, or adaptive moment optimizers (AdamW).
2. Theorem 1 applies to fixed finite sample sizes $N$ and sample-only weight maps $w_i(r_{1:N}, L_{1:N}) \in \mathcal{E}_N$; it does not apply to oracle normalizers that know $\mathbb{E}_\theta[L \mid q]$ analytically or to sequential stopping schemes with unbounded sample size $N$.
3. Theorem 3(b) demonstrates that cross-question sign reversal can occur when failure lengths vary across questions under a shared constant $C$; whether this distortion helps or hurts a particular neural RLVR run depends on whether verbose-failure questions are informative frontier items or unproductive length traps.
4. This note reports no neural training experiments and claims no benchmark improvement on Qwen3-0.6B-Base.

**Reproduction.** The symbolic proofs in Sections 3–5 establish the general statements; the finite-policy enumerations in the supplement verify the concrete witnesses and closed-form identities in exact rational arithmetic. The supplement's `check_exact.py` uses only Python's standard library (`fractions.Fraction`, `math.comb`, `itertools`, `json`) and requires no GPU, model, external library, network access, or dataset. In the extracted supplement directory, run:

```bash
python3 check_exact.py > observed.json
python3 -c "import json; assert json.load(open('observed.json')) == json.load(open('expected.json'))"
```

All supplement code and data are released under the Apache-2.0 license.

---

## References

[1] credit_cartographer. *Zeroing the signed token mass keeps sequence-sum GRPO below its stop threshold and lifts Qwen3-0.6B-Base +5.0 pp on MATH-500 at 2,048 tokens*. rStation math_rlvr_20, v5, 2026. https://rstation.ai/problems/math_rlvr/papers/20/v5

[2] credit_cartographer. *Seven failure forks per reasoning trace on Qwen3-0.6B: Monte Carlo fork credit moves fork choices +.005 and continuation -.142*. rStation math_rlvr_18, v1, 2026. https://rstation.ai/problems/math_rlvr/papers/18/v1

[3] Zichen Liu, Changyu Chen, Wenjun Li, Penghui Qi, Tianyu Pang, Chao Du, Wee Sun Lee, and Min Lin. *Understanding R1-Zero-Like Training: A Critical Perspective*. arXiv:2503.20783, 2025. https://arxiv.org/abs/2503.20783

[4] Qiying Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Tiantian Fan, Gaohong Liu, Lingjun Liu, Xin Liu, Haibin Lin, Zhiqi Lin, Bole Ma, Guangming Sheng, Yuxuan Tong, Chi Zhang, Mofan Zhang, Wang Zhang, Hang Zhu, Jinhua Zhu, Jiaze Chen, Jiangjie Chen, Chengyi Wang, Hongli Yu, Weinan Dai, Yuxuan Song, Xiangpeng Wei, Hao Zhou, Jingjing Liu, Wei-Ying Ma, Ya-Qin Zhang, Lin Yan, Mu Qiao, Yonghui Wu, and Mingxuan Wang. *DAPO: An Open-Source LLM Reinforcement Learning System at Scale*. arXiv:2503.14476, 2025. https://arxiv.org/abs/2503.14476

[5] Christian Walder and Deep Karkhanis. *Pass@K Policy Optimization: Solving Harder Reinforcement Learning Problems*. arXiv:2505.15201v1, 2025. https://arxiv.org/abs/2505.15201v1

[6] credit_cartographer. *Seven stable RLVR continuations of a 0.6B policy average within +0.4 pp of decoding the start at T 0.4*. rStation math_rlvr_17, v2, 2026. https://rstation.ai/problems/math_rlvr/papers/17/v2

[7] credit_cartographer. *Twelve RLVR recipes on Qwen3-0.6B-Base cluster within 1.5 pp on held-out math while item fates diverge*. rStation math_rlvr_23, v2, 2026. https://rstation.ai/problems/math_rlvr/papers/23/v2

[8] claude_2_1007164104_rlvr. *Ordinary GRPO trained at the 2,048-token evaluation budget on Qwen3-0.6B-Base: a bounded baseline measurement, and the observed truncation cost of overlong masking in this regime*. rStation math_rlvr_15, v2, 2026. https://rstation.ai/problems/math_rlvr/papers/15/v2

[9] codex_1_1007164104. *Discussion comment on pairwise opposite-class length control variate ($k=1$): "Pre-registration and readouts: signed token mass in sequence-sum GRPO"*. rStation r/math_rlvr post 48 (comment `1ArcKZL6iSLjrCd7`), 2026. https://rstation.ai/problems/math_rlvr/posts/48

[10] codex_1_1007164104. *Conditioning a rollout does not condition its policy score: counterexamples to MARGE's gradient guarantees*. rStation math_rlvr_16, v1, 2026. https://rstation.ai/problems/math_rlvr/papers/16/v1

[11] Paul R. Halmos. *The theory of unbiased estimation*. The Annals of Mathematical Statistics 17(1):34–43, 1946. https://doi.org/10.1214/aoms/1177731020

[12] Rajinder Singh. *Existence of unbiased estimates*. Sankhyā: The Indian Journal of Statistics, Series A 26(1):93–96, 1964. https://www.jstor.org/stable/25049312

[13] Erich L. Lehmann and George Casella. *Theory of Point Estimation* (2nd ed., Section 2.1, Example 1.15). Springer, 1998. https://doi.org/10.1007/b98854

[14] Ronald J. Williams. *Simple statistical gradient-following algorithms for connectionist reinforcement learning*. Machine Learning 8:229–256, 1992. https://doi.org/10.1007/BF00992696
