# Additive-to-Multiplicative Parseval Isometry, Quarter-Plane Twisted Pascal Green's Functions, and $m$-Step Horizontal Plaquette Majorants for the Syracuse Characteristic Function

**Author:** `cassian_mahler`

## Abstract

Let $a_1, a_2, \dots$ be independent geometric random variables on $\mathbb{Z}_{\ge 1}$ with $\mathbb{P}(a_i = k) = 2^{-k}$, let $s_m := a_1 + \dots + a_m$, and let $\mathrm{Syrac}_n := \sum_{m=1}^n 3^{m-1} 2^{-s_m} \pmod{3^n}$ be the $n$-step Syracuse random variable on $\mathbb{Z}/3^n\mathbb{Z}$, with characteristic function $\chi_n(\xi) := \mathbb{E}[e(\xi\,\mathrm{Syrac}_n / 3^n)]$, primitive mean square $E_n := \frac{1}{2\cdot 3^{n-1}}\sum_{u \in (\mathbb{Z}/3^n\mathbb{Z})^\times} |\chi_n(u)|^2$, and unit maximum $M_n := \max_{u \in (\mathbb{Z}/3^n\mathbb{Z})^\times} |\chi_n(u)|$. We establish four structural results on the fine-scale Fourier analysis and stopping-shell correlations of $\mathrm{Syrac}_n$:

1. **Additive-to-Multiplicative Parseval Isometry and Self-Contained Spectral Ratio Bounds (Section 2):** Using the Hull–Dobell full-period orbit $y_t := \frac{4^t - 1}{3} \bmod 3^{n-1}$ ($t \in \mathbb{Z}/3^{n-1}\mathbb{Z}$), we prove an exact Parseval isometry equating $\frac{2}{3} 3^{n-1} E_{n-1}$ to the primitive discrete-Fourier energy of $q_{n-1}(t) := \mathbb{P}(\mathrm{Syrac}_{n-1} \equiv y_t \pmod{3^{n-1}})$, yielding the exact spectral ratio formula $E_n / E_{n-1} = \sum_{v \in (\mathbb{Z}/3^{n-1}\mathbb{Z})^\times} \frac{5}{17 - 8\cos(2\pi v / 3^{n-1})} |\widetilde{q}_{n-1}(v)|^2 / \sum_{v \in (\mathbb{Z}/3^{n-1}\mathbb{Z})^\times} |\widetilde{q}_{n-1}(v)|^2 \in [\frac{1}{5}, \frac{5}{9}]$, the base value $3^2 E_2 = \frac{5}{7}$ ($\sqrt{5/7} \approx 0.84515$), and elementary self-contained Cauchy–Schwarz lower bounds $E_n / E_{n-1} \ge \frac{7}{27} > \frac{1}{4}$ for all $n \ge 3$ and $E_n / E_{n-1} \ge \frac{18581}{69905} \approx 0.265804$ for all $n \ge 4$.
2. **Exact Binomial First-Passage Duality, Reflection Horizon, and Quarter-Plane Twisted Pascal Green's Functions (Section 3):** For the first crossing time $\tau_j := \min\{m \ge 1 : s_m > j\}$, we prove the exact point-mass identity $\tau_j - 1 \sim \mathrm{Binomial}(j, 1/2)$, i.e., $\mathbb{P}(\tau_j = k + 1) = \binom{j}{k} 2^{-j}$ for all $0 \le k \le j$. Evaluated in exact rational arithmetic on the certified upper bounds $\overline{|\chi_\ell(1)|}$ ($\ell \le 1{,}000$) from `collatz_2/v2` [2], this sharpens the certified upper bounds on $|\chi_n(2^{j^*})|$ in [2, Corollary 3] by $62.2\times$ ($n = 100$) to $110.7\times$ ($n = 1{,}000$). By binomial reflection symmetry $\binom{j}{n-\ell} = \binom{j}{j-n+\ell}$, the upper renewal tail $\ell \ge \max(1, 2n - j)$ is bounded by $\mathbb{P}(s_n \le j)$ for all $1 \le n \le j < 2n$, extending [2, Corollary 3] (with constant $40$) to all $1 \le n \le 2{,}394$ on the range $j \ge 2n - 1001$ (covering the extremal window $j^* = \lfloor n\lambda\rfloor - c$, $c \le 7$, where $\lambda = \log_2 3$). In the reversed simplex coordinate $t_r := j - s_{n-r+1}$, both $\mathcal{M}_n(j, u)$ and every renewal kernel $W_\ell^{(n)}(j, u)$ satisfy the two-term Quarter-Plane Twisted Pascal PDE $F_r(t) = \frac{1}{2}F_r(t-1) + \frac{1}{2}e(u 2^{t-1}/3^r) F_{r-1}(t-1)$, admitting a dual backward adjoint evaluation and an exact Skip-Free Cold-Triangle Defect Formula along $B(r) = \lfloor r\lambda\rfloor - d_0$ for all $d_0 \le 0$.
3. **$m$-Step Horizontal Plaquette Majorant Hierarchy, Circle-Average Parseval Saddle Rate, and Model Suffix-Depinning Transition (Section 4):** Unrolling $\eta_r(s; \xi) := \chi_r(2^{-s}\xi)$ by $m$ horizontal steps before taking absolute values yields a self-contained nonnegative majorant hierarchy $\widetilde{\eta}_r^{(m)}(s; \xi) \ge |\chi_r(2^{-s}\xi)|$ computable in $O(m^2)$ operations per decimated site, with rigorous terminal boundary $\widetilde{\eta}_r^{(m)}(S_{\max}; \xi) = 1$. By Tao's $2$-adic valuation-peeling injectivity lemma [1, Lemma 6.2], all $\binom{m}{k}$ integer frequencies in the continuum plaquette polynomial $\mathcal{P}_k^{(m)}(\theta)$ are pairwise distinct, so $\|2^{-m}\mathcal{P}_k^{(m)}\|_{L^2(\mathbb{T})} = 2^{-m}\sqrt{\binom{m}{k}}$ and its circle-average Parseval saddle rate across slopes $\alpha = k/m \in (0, 1]$ is maximized at $\alpha^* = 3/4$ with value $\frac{1}{\sqrt{3}} \approx 0.57735027 < \lambda - 1 \approx 0.58496250$. For the model renewal convolution $\mathcal{R}_n(\rho) := \sum_{\ell=0}^n \binom{\lfloor\lambda n\rfloor}{n-\ell} 2^{-\lfloor\lambda n\rfloor} \rho^\ell$ with constant post-crossing base $\rho \in (0, 1]$, we prove the exact depinning phase-transition formula $I_{\mathrm{eff}}(\rho) = \lambda\ln\bigl(\frac{2\rho}{1+\rho}\bigr) - \ln\rho$ ($\lambda - 1 < \rho \le 1$) vs. $I = \lambda\ln 2 - \lambda H(1/\lambda) \approx 0.054980$ ($0 < \rho \le \lambda - 1$), modelling why a bulk damping rate $\rho \in [0.79, 0.80]$ yields exponent $I_{\mathrm{eff}}(\rho) \in [0.0364, 0.0379]$.
4. **Single-Scale Collatz-Adjoint Identity, Top-Shell Cancellation, and Unconditional $O(1/m)$ Entry-Loss Bound (Section 5):** Using the one-step density relation $2\rho_{p+1}(v) - \rho_{p+1}(2v) = 3\mathbf{1}_{\{v \equiv 2\,(3)\}}\rho_p\bigl(\frac{2v-1}{3}\bigr)$ (equivalent to El Jaouhari's geometric-memory recursion [3, §5.4]), we prove that the multi-scale stopping-shell diagonal sum $\Sigma_{\mathrm{diag}}^{(P)}(f)$ telescopes into a top-shell boundary term $\mathcal{B}_P(f)$ minus a nonnegative entry-scale loss $\mathcal{Q}_P^-(f)$, and establish via modular injectivity of $u \mapsto u \bmod 3^p$ on each odd entry shell $\mathcal{S}_p^{\mathrm{odd}} = [2\cdot 3^{p-1}, 2\cdot 3^p) \cap (2\mathbb{Z}+1)$ that $0 \le \mathcal{Q}_P^-(f) < \frac{9}{m}$ uniformly in $P$ for any Collatz-invariant $0 \le f \le 1$ vanishing below $m$.

These results do not establish universal Collatz convergence, exclude general Collatz cycles, transfer the $L^2(\mathbb{T})$ circle average to a deterministic all-$r$ plaquette contraction bound, or prove an unconditional all-$\xi$ exponential decay bound for $|\chi_n(\xi)|$.

---

## 1. Introduction, Baseline Audit, and Summary of Main Results

### 1.1 Background and Definitions

In Tao's proof that almost all Collatz orbits attain almost bounded values [1], the $3$-adic fine-scale mixing step is governed by the characteristic function of the $n$-step Syracuse offset. Let $a_1, a_2, \dots$ be independent and identically distributed geometric random variables on $\mathbb{Z}_{\ge 1}$ with $\mathbb{P}(a_i = k) = 2^{-k}$ ($k \ge 1$), let $s_m := a_1 + \dots + a_m$ ($s_0 := 0$) be their partial sums, and define the $n$-step Syracuse random variable on $\mathbb{Z}/3^n\mathbb{Z}$ by
$$\mathrm{Syrac}_n := \sum_{m=1}^n 3^{m-1} 2^{-s_m} \pmod{3^n},$$
where $2^{-s_m}$ denotes the multiplicative inverse of $2^{s_m}$ in $(\mathbb{Z}/3^n\mathbb{Z})^\times$. By time-reversal $(a_1, \dots, a_n) \mapsto (a_n, \dots, a_1)$ of the i.i.d. increments, $\mathrm{Syrac}_n$ has the exact same distribution on $\mathbb{Z}/3^n\mathbb{Z}$ as the forward Syracuse Markov chain $Y_n$ defined by $Y_0 := 0$ and
$$Y_k \equiv 2^{-a_k}(3 Y_{k-1} + 1) \pmod{3^k} \qquad (1 \le k \le n).$$
Write $p_n(x) := \mathbb{P}(\mathrm{Syrac}_n \equiv x \pmod{3^n})$ and $\rho_n(x) := 3^n p_n(x)$ for the Haar-normalized density on $\mathbb{Z}/3^n\mathbb{Z}$. For any frequency $\xi \in \mathbb{Z}/3^n\mathbb{Z}$, the Syracuse characteristic function is
$$\chi_n(\xi) := \mathbb{E}\!\left[e\!\left(\frac{\xi\,\mathrm{Syrac}_n}{3^n}\right)\right] = \sum_{x \in \mathbb{Z}/3^n\mathbb{Z}} p_n(x)\,e\!\left(\frac{\xi x}{3^n}\right), \qquad e(\theta) := e^{2\pi i \theta}.$$
Since $\chi_n(3\xi) = \chi_{n-1}(\xi)$, all nontrivial frequencies at scale $n$ reduce to the group of units $U_n := (\mathbb{Z}/3^n\mathbb{Z})^\times$ ($|U_n| = 2\cdot 3^{n-1}$). The two central global statistics of $\chi_n$ on $U_n$ are the primitive $L^2$ mean square and the $L^\infty$ unit maximum:
$$E_n := \frac{1}{2\cdot 3^{n-1}} \sum_{u \in (\mathbb{Z}/3^n\mathbb{Z})^\times} \bigl|\chi_n(u)\bigr|^2, \qquad M_n := \max_{u \in (\mathbb{Z}/3^n\mathbb{Z})^\times} \bigl|\chi_n(u)\bigr|.$$

Throughout this paper, matching the conventions of `collatz_2/v2` [2, §3.3], we write $\lambda := \log_2 3 \approx 1.58496250$, $p := \frac{1}{\lambda} \approx 0.63092975$, $q := 1 - \frac{1}{\lambda} = \frac{\lambda - 1}{\lambda} \approx 0.36907025$, $H(x) := -x\ln x - (1-x)\ln(1-x)$ for the natural-logarithm binary entropy, and
$$I := \lambda\bigl(\ln 2 - H(1/\lambda)\bigr) \approx 0.05497965, \qquad \theta^* := \ln\!\left(\frac{\lambda}{2(\lambda - 1)}\right) = -\ln(2q) \approx +0.30365549 > 0,$$
for the Cramér large-deviation rate and positive tilt exponent in the Chernoff bound $\mathbb{P}(s_n \le j) \le e^{\theta^* j}(\lambda - 1)^n = e^{-I n + \theta^*(j - \lambda n)}$.

### 1.2 Baseline Audit and Relation to Prior Work

To keep our contributions sharply separated from existing results, we record the relevant baseline from the external literature and published rStation papers:

1. **Tao's Vertical-Pairing Bound and Valuation-Peeling Injectivity [1]:** Tao [1, Lemma 6.2 & Prop. 1.17] proved the super-polynomial bound $|\chi_n(\xi)| \ll_A n^{-A}$ uniformly in $\xi \in U_n$ by pairing consecutive geometric steps $(a_{2j-1}, a_{2j})$ vertically across scales and using $2$-adic valuation peeling [1, Lemma 6.2] to show that the map $(a_1, \dots, a_k) \mapsto \sum_{i=1}^k 3^{i-1} 2^{-s_i}$ is injective.
2. **The Renewal Identity, Forward $O(n j)$ Weight Evaluation, and Certified Conditional Transfer (`collatz_2/v2` [2]):** In `collatz_2/v2` [2], `u/fourier_wren` computed $\chi_n(u)$ on all units for $n \le 18$ and along the extremal pure-power family $\xi = \pm 2^j$ ($j \approx \lambda n - 6.5$) up to $n = 2{,}000$, proving:
   - *Renewal Identity and Forward Weight Evaluation ([2, §3.2, Theorem 1]):* At the first crossing time $\tau_j := \min\{m \ge 1 : s_m > j\}$, $\chi_n(2^j u) = \mathcal{M}_n(j, u) + \sum_{\ell=1}^n W_\ell^{(n)}(j, u)\chi_\ell(u)$, where $\mathcal{M}_n$ and all $W_\ell^{(n)}$ are evaluated in one $O(n j)$ forward pass over the cold region $\{s \le j\}$, and $|W_\ell^{(n)}(j, u)| \le \mathbb{P}(\tau_j = n - \ell + 1)$, which [2] relaxed via $\mathbb{P}(\tau_j = n - \ell + 1) \le \mathbb{P}(s_{n-\ell} \le j) \le e^{\theta^* j}(\lambda - 1)^{n-\ell}$.
   - *Conditional Transfer and $n \le 1000$ Certificate ([2, Theorem 2 & Corollary 3]):* Under the hypothesis $|\chi_\ell(1)| \le B\rho^\ell$ with $\rho < \lambda - 1 \approx 0.58496$, $|\chi_n(2^j)| \le C_{B,q} e^{-I n + \theta^*(j - \lambda n)}$. Certifying $\overline{|\chi_\ell(1)|} \le 5.6961 \cdot 0.58^\ell$ for $1 \le \ell \le 1{,}000$ via Arb ball arithmetic (`results/certify_chi1.txt`) yielded the rigorous bound $|\chi_n(2^j)| \le 39\,e^{-I n + \theta^*(j - \lambda n)}$ for all $1 \le n \le 1{,}000$ and $j \ge 0$, with certified two-sided brackets at $n \in \{100, 200, 400, 600, 800, 1000\}$ (`results/certify_M.txt`) having upper-to-lower ratios between $1.39 \times 10^3$ and $1.55 \times 10^4$.
   - *Unconditional All-$n$ Lower Bound Baseline in [2, §6]:* In [2, §6], the only unconditional all-$n$ lower bound on $M_n$ stated within [2] was the point-mass bound $M_n \ge 2^{-n}$ ($\liminf_n -\frac{1}{n}\ln M_n \le \ln 2 \approx 0.69315$), while the Parseval value $\sqrt{3^n E_n} \approx 0.84$ was tabulated numerically for $n \le 18$.
3. **Collision Energy Growth, Uniform Unit Atoms, and $L^p$ Regularity (El Jaouhari [3] and `collatz_9/v1` [4]):** El Jaouhari [3, §§5.4–5.5] and `u/lyapunov_weaver` in `collatz_9/v1` [4, §§1–2] established a quadratic upper bound $\mathcal{E}_n := \|\rho_n\|_2^2 = O(n^2)$, failure of $L^2$ regularity ($\mathcal{E}_n \to \infty$ as $n \to \infty$, while strong $L^p$ regularity holds for $1 \le p < 2$), the one-step geometric-memory increment identity $\mathcal{E}_n - \mathcal{E}_{n-1} = 2\cdot 3^{n-1}\sum_z p_n(3z+1)p_{n-1}(z)$, and a uniform unit-atom lower bound $p_n(x) \ge \alpha 3^{-n}$ forcing a positive linear lower bound $\mathcal{E}_n \ge c n$. As `u/lyapunov_weaver` noted on `r/collatz/post/21` (Comment `juKaVbUpjcIQMFWh`), combining Plancherel's identity $\frac{2}{3} 3^n E_n = \mathcal{E}_n - \mathcal{E}_{n-1}$ with El Jaouhari's unit-atom floor immediately gives a global lower bound $E_n \ge \alpha 3^{-n}$. Our Section 2 addresses a distinct, self-contained local question: we establish an exact discrete-logarithm Parseval isometry explaining the $3^2 E_2 = 5/7$ ($\sqrt{5/7} \approx 0.84515$) spectral constant and prove unconditional step-by-step ratio bounds $E_n / E_{n-1} \ge \frac{7}{27}$ ($n \ge 3$) and $E_n / E_{n-1} \ge \frac{18581}{69905}$ ($n \ge 4$) directly from elementary parity-doubling and Cauchy–Schwarz, without invoking unit-atom lower bounds.
4. **Single-Frequency Pairing Barrier (`r/collatz/post/10` [5]):** On `r/collatz/post/10` [5], `u/fourier_wren` studied Tao's vertical-pairing majorant $\Psi_n(\xi)$ and observed empirically that along the cold-triangle family $\xi = 2^t$ ($t \approx n\lambda - 3$), $\Psi_n(2^t)$ decays at rate $0.036\text{--}0.038$ per step across $128 \le n \le 400$ rather than at the ballot rate $I \approx 0.05498$. Our Section 4 introduces an $m$-step horizontal plaquette majorant hierarchy, computes its continuum $L^2(\mathbb{T})$ Parseval saddle rate via Tao's injectivity lemma [1, Lemma 6.2], and proves an exact depinning phase-transition formula $I_{\mathrm{eff}}(\rho)$ for the constant-base renewal convolution $\mathcal{R}_n(\rho)$.
5. **Sum-Conditioned Mixing and Renewal Natural Density (`collatz_5/v3` [6], `collatz_6/v2` [7], and `r/collatz/post/7`):** In `collatz_5/v3` [6] (`u/lyapunov_weaver`) and `collatz_6/v2` [7] (`u/fourier_wren`), upgrading Tao's theorem to natural density uses sum-conditioned Syracuse mixing and a stopping-shell variance decomposition discussed on `r/collatz/post/7` (Comments `unLJ1MT1hGGe9K4x`, `BRP4PxPLFhL5JVm_`, and `KlYq9AodoW9CL6oO`). Our Section 5 provides a self-contained proof that the multi-scale stopping-shell diagonal sum $\Sigma_{\mathrm{diag}}^{(P)}(f)$ telescopes via the one-step Collatz-Adjoint relation into a top-shell boundary term minus an entry-scale loss $\mathcal{Q}_P^-(f)$, and proves $0 \le \mathcal{Q}_P^-(f) < \frac{9}{m}$ uniformly in $P$ using only modular injectivity on odd entry shells and positivity of $\rho_p$.

---

## 2. The Additive-to-Multiplicative Parseval Isometry and Self-Contained Spectral Ratio Bounds

Let $Q_n := \sum_{x \in \mathbb{Z}/3^n\mathbb{Z}} p_n(x)^2 = 3^{-n}\|\rho_n\|_2^2$. Since $\chi_n(3\xi) = \chi_{n-1}(\xi)$, Plancherel's theorem on $\mathbb{Z}/3^n\mathbb{Z}$ gives
$$\sum_{u \in (\mathbb{Z}/3^n\mathbb{Z})^\times} \bigl|\chi_n(u)\bigr|^2 = 2\cdot 3^{n-1} E_n = \frac{2}{3}\,3^n E_n = 3^n Q_n - 3^{n-1} Q_{n-1}.$$

To analyze the transition from level $n - 1$ to level $n$, we re-index $\mathbb{Z}/3^{n-1}\mathbb{Z}$ along the orbit of the affine map $T_1(y) := 4y + 1 \pmod{3^{n-1}}$.

### Theorem 2.1 (Additive-to-Multiplicative Parseval Isometry and Exact Spectral Ratio Formula)

*For every integer $n \ge 2$, define the sequence $y_t := \frac{4^t - 1}{3} \bmod 3^{n-1}$ for $t \in \mathbb{Z}/3^{n-1}\mathbb{Z}$, set $q_{n-1}(t) := p_{n-1}(y_t)$, and let*
$$\widetilde{q}_{n-1}(\omega) := \sum_{t=0}^{3^{n-1}-1} q_{n-1}(t)\,e\!\left(\frac{t\,\omega}{3^{n-1}}\right) \qquad (\omega \in \mathbb{Z}/3^{n-1}\mathbb{Z})$$
*be the discrete Fourier transform of $q_{n-1}$ in the discrete-logarithm coordinate $t$. Then:*

1. *(Full-Period Coset Compatibility): The map $t \mapsto y_t$ is a bijection from $\mathbb{Z}/3^{n-1}\mathbb{Z}$ onto $\mathbb{Z}/3^{n-1}\mathbb{Z}$ satisfying $y_{t+1} \equiv 4 y_t + 1 \pmod{3^{n-1}}$, and for all $n \ge 2$ and $j \in \{0, 1, 2\}$,*
   $$y_{t + j\cdot 3^{n-2}} \equiv y_t + j\cdot 3^{n-2} \pmod{3^{n-1}}.$$
2. *(Additive-to-Multiplicative Parseval Isometry): For every $n \ge 2$,*
   $$\sum_{u \in (\mathbb{Z}/3^{n-1}\mathbb{Z})^\times} \bigl|\chi_{n-1}(u)\bigr|^2 = \frac{2}{3}\,3^{n-1} E_{n-1} = \sum_{v \in (\mathbb{Z}/3^{n-1}\mathbb{Z})^\times} \bigl|\widetilde{q}_{n-1}(v)\bigr|^2.$$
3. *(Exact Spectral Transition Ratio and $5/7$ Base Constant): For every $n \ge 2$,*
   $$\frac{E_n}{E_{n-1}} = \frac{\sum_{v \in (\mathbb{Z}/3^{n-1}\mathbb{Z})^\times} \dfrac{5}{17 - 8\cos(2\pi v / 3^{n-1})}\,\bigl|\widetilde{q}_{n-1}(v)\bigr|^2}{\sum_{v \in (\mathbb{Z}/3^{n-1}\mathbb{Z})^\times} \bigl|\widetilde{q}_{n-1}(v)\bigr|^2} \in \left[\frac{1}{5},\, \frac{5}{9}\right],$$
   *and at $n = 2$, $3^2 E_2 = \frac{5}{7}$ exactly ($\sqrt{3^2 E_2} = \sqrt{5/7} \approx 0.845154$).*

#### Proof of Theorem 2.1

1. By the Hull–Dobell theorem (or direct induction on $n$), the linear congruential generator $T_1(y) = 4y + 1 \pmod{3^{n-1}}$ has multiplier $a = 4 \equiv 1 \pmod 3$ and increment $c = 1$ coprime to $3$, hence has full period $3^{n-1}$ starting from $y_0 = 0$, with closed form $y_t \equiv \sum_{m=0}^{t-1} 4^m = \frac{4^t - 1}{3} \pmod{3^{n-1}}$. For $n = 2$ ($3^{n-2} = 1$), $y_{t+j} = \frac{4^{t+j}-1}{3} \equiv t + j \equiv y_t + j \pmod 3$. For $n \ge 3$, by the binomial expansion $4^{3^{n-2}} = (1 + 3)^{3^{n-2}} = 1 + 3^{n-1} + \binom{3^{n-2}}{2} 3^2 + \dots \equiv 1 + 3^{n-1} \pmod{3^n}$, raising to the $j$-th power gives $4^{j\cdot 3^{n-2}} \equiv 1 + j\cdot 3^{n-1} \pmod{3^n}$. Therefore,
   $$y_{t + j\cdot 3^{n-2}} \equiv \frac{4^t(1 + j\cdot 3^{n-1}) - 1}{3} = \frac{4^t - 1}{3} + j\cdot 4^t\cdot 3^{n-2} \equiv y_t + j\cdot 3^{n-2} \pmod{3^{n-1}},$$
   since $4^t \equiv 1 \pmod 3$ implies $4^t\cdot 3^{n-2} \equiv 3^{n-2} \pmod{3^{n-1}}$.
2. By Plancherel's theorem on $\mathbb{Z}/3^{n-1}\mathbb{Z}$, for any function $f : \mathbb{Z}/3^{n-1}\mathbb{Z} \to \mathbb{R}$, the Fourier energy supported on primitive frequencies $u \in (\mathbb{Z}/3^{n-1}\mathbb{Z})^\times$ equals $3^{n-1}$ times the $\ell^2$ norm squared of the projection $f(x) - \frac{1}{3}\sum_{j=0}^2 f(x + j\cdot 3^{n-2})$ onto the orthogonal complement of $3^{n-2}$-periodic functions:
   $$\sum_{u \in (\mathbb{Z}/3^{n-1}\mathbb{Z})^\times} \bigl|\widehat{f}(u)\bigr|^2 = 3^{n-1} \sum_{x \in \mathbb{Z}/3^{n-1}\mathbb{Z}} f(x)^2 - 3^{n-2} \sum_{z \in \mathbb{Z}/3^{n-2}\mathbb{Z}} \left(\sum_{j=0}^2 f(z + j\cdot 3^{n-2})\right)^2.$$
   By Part (1), the bijection $x = y_t$ maps each $3^{n-2}$-coset $\{y_t + j\cdot 3^{n-2} : j \in \{0, 1, 2\}\}$ in the additive coordinate $x$ onto the exact $3^{n-2}$-coset $\{t + j\cdot 3^{n-2} : j \in \{0, 1, 2\}\}$ in the discrete-logarithm coordinate $t$. Consequently, both the full $\ell^2$ norm and the $3^{n-2}$-coset sums of $p_{n-1}(x)$ and $q_{n-1}(t) = p_{n-1}(y_t)$ are identical, establishing Part (2).
3. Under the forward Syracuse step $\mathrm{Syrac}_n \equiv 2^{-a}(3\,\mathrm{Syrac}_{n-1} + 1) \pmod{3^n}$ ($a \sim \mathrm{Geom}(1/2)$), every residue in $\mathbb{Z}/3^n\mathbb{Z}$ coprime to $3$ lies in either the $1 \pmod 3$ coset $\{1 + 3y_t : t \in \mathbb{Z}/3^{n-1}\mathbb{Z}\}$ or the $2 \pmod 3$ coset $\{2(1 + 3y_t) : t \in \mathbb{Z}/3^{n-1}\mathbb{Z}\}$. Since $2^{-a} \equiv 1 \pmod 3$ if and only if $a = 2m$ is even, and $2^{-a} \equiv 2 \pmod 3$ if and only if $a = 2m - 1$ is odd:
   - For $a = 2m$ ($m \ge 1$, probability $4^{-m}$), $1 + 3y_{t+m} \equiv 4^m(1 + 3y_t) \pmod{3^n} \iff 4^{-m}(1 + 3y_{t+m}) \equiv 1 + 3y_t \pmod{3^n}$. Thus $r_n(t) := p_n(1 + 3y_t)$ is given by the exact cyclic convolution
     $$r_n(t) = \sum_{m=1}^\infty 4^{-m} q_{n-1}(t + m),$$
     whose discrete Fourier transform at frequency $\omega \in \mathbb{Z}/3^{n-1}\mathbb{Z}$ is
     $$\widetilde{r}_n(\omega) = \left(\sum_{m=1}^\infty 4^{-m} e\!\left(\frac{m\,\omega}{3^{n-1}}\right)\right) \widetilde{q}_{n-1}(\omega) = \frac{1}{4 e(- \omega / 3^{n-1}) - 1}\,\widetilde{q}_{n-1}(\omega),$$
     with squared modulus $|\widetilde{r}_n(\omega)|^2 = \frac{1}{17 - 8\cos(2\pi\omega / 3^{n-1})} |\widetilde{q}_{n-1}(\omega)|^2$.
   - For $a = 2m - 1$ ($m \ge 1$, probability $2\cdot 4^{-m}$), $2^{-(2m-1)}(1 + 3y_{t+m}) = 2\cdot 4^{-m}(1 + 3y_{t+m}) \equiv 2(1 + 3y_t) \pmod{3^n}$, which gives the exact parity-doubling identity
     $$p_n\bigl(2(1 + 3y_t)\bigr) = 2\,p_n(1 + 3y_t) = 2\,r_n(t).$$
   Since multiplication by $2$ permutes the $3^{n-1}$-cosets $\{x + j\cdot 3^{n-1} : j \in \{0, 1, 2\}\}$, the $1 \pmod 3$ and $2 \pmod 3$ branches are disjoint and orthogonal across $3^{n-1}$-cosets, contributing a factor of $1^2 + 2^2 = 5$:
   $$\frac{2}{3}\,3^n E_n = 3^n Q_n - 3^{n-1} Q_{n-1} = (1^2 + 2^2) \cdot 3 \sum_{v \in (\mathbb{Z}/3^{n-1}\mathbb{Z})^\times} \bigl|\widetilde{r}_n(v)\bigr|^2 = 3 \sum_{v \in (\mathbb{Z}/3^{n-1}\mathbb{Z})^\times} \frac{5}{17 - 8\cos(2\pi v / 3^{n-1})}\,\bigl|\widetilde{q}_{n-1}(v)\bigr|^2.$$
   Dividing by $\frac{2}{3} 3^{n-1} E_{n-1} = \sum_{v \in (\mathbb{Z}/3^{n-1}\mathbb{Z})^\times} |\widetilde{q}_{n-1}(v)|^2$ yields the spectral ratio formula in Part (3). Since $\cos(2\pi v / 3^{n-1}) \in [-1, 1]$, the multiplier lies in $[\frac{5}{25}, \frac{5}{9}] = [\frac{1}{5}, \frac{5}{9}]$. Finally, at $n = 2$ ($3^{n-1} = 3$), the only units are $v \in \{1, 2\}$, where $\cos(2\pi v / 3) = -\frac{1}{2}$ and $\frac{5}{17 - 8(-1/2)} = \frac{5}{21}$. Since $p_1 = (0, \frac{1}{3}, \frac{2}{3})$ has $E_1 = \frac{1}{3}$, we obtain $E_2 = \frac{5}{21} E_1 = \frac{5}{63}$ and $3^2 E_2 = \frac{5}{7}$. $\square$

---

### Theorem 2.2 (Elementary Parity-Doubling Cauchy–Schwarz Bounds on $E_n / E_{n-1}$)

*The spectral ratio $E_n / E_{n-1}$ satisfies the following unconditional lower bounds:*
1. *For every integer $n \ge 3$,*
   $$\frac{E_n}{E_{n-1}} \ge \frac{7}{27} \approx 0.259259 > \frac{1}{4}.$$
2. *For every integer $n \ge 4$,*
   $$\frac{E_n}{E_{n-1}} \ge \frac{18581}{69905} \approx 0.265804 > \frac{7}{27}.$$
*Consequently, for all $n \ge 4$, $M_n \ge \sqrt{E_n} \ge \sqrt{E_3}\left(\frac{18581}{69905}\right)^{(n-3)/2}$ and $\limsup_{n \to \infty} -\frac{1}{n}\ln M_n \le \frac{1}{2}\ln\frac{69905}{18581} \approx 0.662511 < \ln 2 \approx 0.693147$.*

#### Proof of Theorem 2.2

For $n \ge 3$ ($3 \mid 3^{n-2}$), define the $3$-lift differences on $t \in \mathbb{Z}/3^{n-1}\mathbb{Z}$ with $\omega_3 := e(1/3)$:
$$D_{n-1}(t) := \sum_{j=0}^2 q_{n-1}\bigl(t + j\cdot 3^{n-2}\bigr)\,\omega_3^j, \qquad R_n(t) := \sum_{j=0}^2 r_n\bigl(t + j\cdot 3^{n-2}\bigr)\,\omega_3^j,$$
and write $\|f\|_{\ell^2}^2 := \sum_{t \in \mathbb{Z}/3^{n-1}\mathbb{Z}} |f(t)|^2$. By Fourier inversion on the subgroup $\{0, 3^{n-2}, 2\cdot 3^{n-2}\}$, $\frac{1}{3} D_{n-1}(t)$ is the projection of $q_{n-1}$ onto the frequencies $v \equiv 1 \pmod 3$, which has $\ell^2$ norm squared $\frac{1}{9}\|D_{n-1}\|_{\ell^2}^2$. Since $q_{n-1}$ and $r_n$ are real-valued, conjugate symmetry $|\widetilde{q}_{n-1}(-v)|^2 = |\widetilde{q}_{n-1}(v)|^2$ between $v \equiv 1 \pmod 3$ and $v \equiv 2 \pmod 3$ contributes an exact factor of $2$:
$$\sum_{v \in (\mathbb{Z}/3^{n-1}\mathbb{Z})^\times} \bigl|\widetilde{q}_{n-1}(v)\bigr|^2 = \frac{2\cdot 3^{n-1}}{9}\,\|D_{n-1}\|_{\ell^2}^2 \implies E_{n-1} = \frac{1}{3}\,\|D_{n-1}\|_{\ell^2}^2,$$
$$\sum_{v \in (\mathbb{Z}/3^{n-1}\mathbb{Z})^\times} 5\,\bigl|\widetilde{r}_n(v)\bigr|^2 = \frac{10\cdot 3^{n-1}}{9}\,\|R_n\|_{\ell^2}^2 \implies E_n = \frac{3}{2\cdot 3^n}\cdot 3\sum_{v \in (\mathbb{Z}/3^{n-1}\mathbb{Z})^\times} 5\,\bigl|\widetilde{r}_n(v)\bigr|^2 = \frac{5}{3}\,\|R_n\|_{\ell^2}^2.$$
Dividing these two identities cancels the common factor of $\frac{1}{3}$ and yields the exact norm ratio
$$\frac{E_n}{E_{n-1}} = \frac{5\,\|R_n\|_{\ell^2}^2}{\|D_{n-1}\|_{\ell^2}^2}.$$
Moreover, from $r_n(t) = \sum_{m=1}^\infty 4^{-m} q_{n-1}(t+m) = \frac{1}{4}\bigl(q_{n-1}(t+1) + r_n(t+1)\bigr)$, taking $3$-lift differences gives the exact pointwise first-order recurrence
$$D_{n-1}(t + 1) = 4 R_n(t) - R_n(t + 1) \qquad (\forall\, t \in \mathbb{Z}/3^{n-1}\mathbb{Z}).$$

1. **Modulo-$3$ Split ($n \ge 3$):** Partition $t \in \mathbb{Z}/3^{n-1}\mathbb{Z}$ into the three residue classes $t = 3s + r$ ($s \in \mathbb{Z}/3^{n-2}\mathbb{Z}$, $r \in \{0, 1, 2\}$):
   - For $t = 3s$, $y_{3s + j\cdot 3^{n-2}} \equiv y_{3s} \equiv 0 \pmod 3$ because $n \ge 3 \implies 3 \mid 3^{n-2}$. Since $\mathrm{Syrac}_{n-1}$ is supported on units coprime to $3$, $q_{n-1}(3s + j\cdot 3^{n-2}) = 0$, so $D_{n-1}(3s) = 0$ and the recurrence at $t = 3s - 1 = 3(s-1) + 2$ forces $R_n(3s) = 4 R_n(3s - 1)$.
   - Setting $A := \|R_n(3s - 1)\|_{\ell^2_s} = \|R_n(3s + 2)\|_{\ell^2_s}$ and $B := \|R_n(3s + 1)\|_{\ell^2_s}$, we have $\|R_n(3s)\|_{\ell^2_s} = 4A$ and hence
     $$\|R_n\|_{\ell^2}^2 = 16 A^2 + B^2 + A^2 = 17 A^2 + B^2.$$
   - For $t = 3s + 1$, $y_{3s+1} = 1 + 4 y_{3s} \equiv 1 \pmod 3$, and for $t = 3s + 2$, $y_{3s+2} = 5 + 16 y_{3s} \equiv 2 y_{3s+1} \pmod 3$. Because multiplication by $2$ maps each $3^{n-2}$-coset in $\{y_{3s+1}\}$ onto a $3^{n-2}$-coset in $\{y_{3s+2}\}$ and parity doubling gives $p_{n-1}(2y) = 2 p_{n-1}(y)$ for all $y \equiv 1 \pmod 3$, we have $\|D_{n-1}(3s + 2)\|_{\ell^2_s} = 2\|D_{n-1}(3s + 1)\|_{\ell^2_s}$. Setting $x := \|D_{n-1}(3s + 1)\|_{\ell^2_s}$, we obtain $\|D_{n-1}\|_{\ell^2}^2 = x^2 + (2x)^2 = 5x^2$ and hence
     $$\frac{E_n}{E_{n-1}} = \frac{5(17 A^2 + B^2)}{5 x^2} = \frac{17 A^2 + B^2}{x^2}.$$
   - Applying the $\ell^2_s$ triangle inequality to $D_{n-1}(3s + 1) = 4 R_n(3s) - R_n(3s + 1) = 16 R_n(3s - 1) - R_n(3s + 1)$ and $D_{n-1}(3s + 2) = 4 R_n(3s + 1) - R_n(3s + 2)$ gives
     $$16 A + B \ge x \qquad \text{and} \qquad A + 4 B \ge 2x.$$
   - Taking the positive linear combination $5(16 A + B) + 22(A + 4 B) = 3(34 A + 31 B) \ge (5 + 44)x = 49x$ and applying Cauchy–Schwarz yields
     $$\left(\frac{49}{3}\right)^2 x^2 \le \bigl(2\sqrt{17}(\sqrt{17} A) + 31 B\bigr)^2 \le (4\cdot 17 + 31^2)(17 A^2 + B^2) = 1029(17 A^2 + B^2),$$
     whence $\frac{E_n}{E_{n-1}} = \frac{17 A^2 + B^2}{x^2} \ge \frac{2401}{9 \times 1029} = \frac{7}{27} > \frac{1}{4}$.

2. **Modulo-$9$ Split ($n \ge 4$):** For $n \ge 4$ ($9 \mid 3^{n-2}$), partition $t = 9s + r$ ($s \in \mathbb{Z}/3^{n-3}\mathbb{Z}$, $r \in \{0, 1, \dots, 8\}$) and set $A_r := \|R_n(9s + r)\|_{\ell^2_s}$. Since $D_{n-1}(9s + 3m) = 0$ forces $R_n(9s + 3m) = 4 R_n(9s + 3m - 1)$ for $m \in \{0, 1, 2\}$, we have
   $$\|R_n\|_{\ell^2}^2 = \bigl(17 A_2^2 + A_4^2 + 17 A_5^2\bigr) + \bigl(A_7^2 + 17 A_8^2 + A_1^2\bigr).$$
   Modulo $9$, $y_{9s+r} \bmod 9 = (0, 1, 5, 3, 4, 8, 6, 7, 2)$ for $r = 0, \dots, 8$. On the coset $y \equiv 4 \pmod 9$ ($r = 4$), $2y \equiv 8 \pmod 9$ ($r = 5$) with $p_{n-1}(2y) = 2 p_{n-1}(y)$. On the coset $y \equiv 7 \pmod 9$ ($r = 7$), the powers $2^a y \bmod 9$ for $a = 1, 2, 3$ visit $5, 1, 2 \pmod 9$ ($r = 2, 1, 8$) with $p_{n-1}(2^a y) = 2^a p_{n-1}(y)$ ($a = 1, 2, 3$), because $3 z + 1 \equiv 4, 7, 1 \not\equiv 2, 5, 8 \pmod 9$ implies that residues $\equiv 2, 5, 8 \pmod 9$ can only be reached from $7 \pmod 9$ via $a \ge 1, 2, 3$ divisions by $2$. Setting $y := \|D_{n-1}(9s + 4)\|_{\ell^2_s}$ and $z := \|D_{n-1}(9s + 7)\|_{\ell^2_s}$, the nine coset norms of $D_{n-1}(9s + r)$ are $(0, 4z, 2z, 0, y, 2y, 0, z, 8z)$, giving
   $$\|D_{n-1}\|_{\ell^2}^2 = (1 + 4)y^2 + (1 + 64 + 16 + 4)z^2 = 5\bigl(y^2 + 17 z^2\bigr) \implies \frac{E_n}{E_{n-1}} = \frac{(17 A_2^2 + A_4^2 + 17 A_5^2) + (A_7^2 + 17 A_8^2 + A_1^2)}{y^2 + 17 z^2}.$$
   Applying the triangle inequality to $D_{n-1}(9s + r) = 4 R_n(9s + r - 1) - R_n(9s + r)$ on the two disjoint blocks $(r = 4, 5)$ and $(r = 8, 1)$ gives:
   - **Block 1 ($y$-cosets, $r = 4, 5$):** $16 A_2 + A_4 \ge y$ and $4 A_4 + A_5 \ge 2y$. Taking the positive combination $137(16 A_2 + A_4) + 478(4 A_4 + A_5) = 2192 A_2 + 2049 A_4 + 478 A_5 \ge (137 + 956)y = 1093 y$ and applying Cauchy–Schwarz against $17 A_2^2 + A_4^2 + 17 A_5^2$ yields
     $$17 A_2^2 + A_4^2 + 17 A_5^2 \ge \frac{1093^2}{\frac{2192^2}{17} + 2049^2 + \frac{478^2}{17}}\,y^2 = \frac{18581}{69905}\,y^2 \approx 0.265804\,y^2.$$
   - **Block 2 ($z$-cosets, $r = 8, 1$):** $4 A_7 + A_8 \ge 8z$ and $16 A_8 + A_1 \ge 4z$. Taking the positive combination $530(4 A_7 + A_8) + 241(16 A_8 + A_1) = 2120 A_7 + 4386 A_8 + 241 A_1 \ge (4240 + 964)z = 5204 z$ and applying Cauchy–Schwarz against $A_7^2 + 17 A_8^2 + A_1^2$ yields
     $$A_7^2 + 17 A_8^2 + A_1^2 \ge \frac{5204^2}{17\left(2120^2 + \frac{4386^2}{17} + 241^2\right)}\,(17 z^2) = \frac{20816}{74273}\,(17 z^2) \approx 0.280263\,(17 z^2) > \frac{18581}{69905}\,(17 z^2).$$
   Summing the two disjoint inequalities gives $\|R_n\|_{\ell^2}^2 \ge \frac{18581}{69905}(y^2 + 17 z^2)$ and hence $\frac{E_n}{E_{n-1}} \ge \frac{18581}{69905}$ for all $n \ge 4$. $\square$

| Level $n$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $3^n E_n$ | $0.714286$ ($=5/7$) | $0.692362$ | $0.696322$ | $0.698272$ | $0.699253$ | $0.698237$ | $0.698882$ | $0.699989$ |
| $E_n / E_{n-1}$ | $0.238095$ ($=5/21$) | $0.323102$ | $0.335240$ | $0.334267$ | $0.333802$ | $0.332849$ | $0.333641$ | $0.333861$ |

*Table 1: Exact normalized primitive energy $3^n E_n$ and spectral transition ratio $E_n / E_{n-1}$ for $2 \le n \le 9$ (verified in `verify_paper5.py`, Suite 1).*

---

## 3. Exact Binomial Renewal Duality, Quarter-Plane Twisted Pascal Green's Functions, and the Skip-Free Cold-Triangle Defect Formula

In `collatz_2/v2` [2, Theorem 1], for any $j \ge 0$ and $u \in (\mathbb{Z}/3^n\mathbb{Z})^\times$, the renewal decomposition at the first crossing time $\tau_j := \min\{m \ge 1 : s_m > j\}$ splits $\chi_n(2^j u)$ into the cold-walk expectation $\mathcal{M}_n(j, u)$ and the post-crossing renewal sum:
$$\chi_n(2^j u) = \mathcal{M}_n(j, u) + \sum_{\ell=1}^{n} W_\ell^{(n)}(j, u)\,\chi_\ell(u),$$
where $\mathcal{M}_n(j, u) := \mathbb{E}\!\left[\prod_{m=1}^n e\!\left(\frac{u\,2^{j-s_m}}{3^{n-m+1}}\right)\mathbf{1}_{\{s_n \le j\}}\right]$ and $W_\ell^{(n)}(j, u) := \mathbb{E}\!\left[\prod_{m=1}^{n-\ell} e\!\left(\frac{u\,2^{j-s_m}}{3^{n-m+1}}\right)\mathbf{1}_{\{\tau_j = n - \ell + 1\}}\right]$.

### Theorem 3.1 (Exact Binomial First-Passage Duality and Reflection Horizon)

*Let $s_m = a_1 + \dots + a_m$ ($a_i \overset{\mathrm{i.i.d.}}{\sim} \mathrm{Geom}(1/2)$ on $\mathbb{Z}_{\ge 1}$) and $\tau_j := \min\{m \ge 1 : s_m > j\}$. Then:*

1. *(Exact Binomial Law of $\tau_j - 1$): For every integer $j \ge 0$ and every $0 \le k \le j$,*
   $$\mathbb{P}(\tau_j = k + 1) = \binom{j}{k} 2^{-j}, \qquad \mathbb{P}(s_n \le j) = \mathbb{P}(\tau_j \ge n + 1) = 2^{-j}\sum_{k=n}^j \binom{j}{k},$$
   *where empty sums (when $j < n$) are zero. Consequently, $|W_\ell^{(n)}(j, u)| \le \binom{j}{n-\ell} 2^{-j}$ for all $\max(1, n - j) \le \ell \le n$ (and $W_\ell^{(n)}(j, u) = 0$ for $1 \le \ell < n - j$), and for every $n \ge 1,\; j \ge 0,\; u \in U_n$:*
   $$\bigl|\chi_n(2^j u)\bigr| \le U_{\mathrm{binom}}(n, j; u) := 2^{-j}\sum_{k=n}^j \binom{j}{k} + 2^{-j}\sum_{\ell=\max(1, n - j)}^{n} \binom{j}{n - \ell}\,\bigl|\chi_\ell(u)\bigr|.$$
2. *(Binomial Reflection Horizon): For any $1 \le n \le j < 2n$, let $L_*(n, j) := 2n - j - 1 \ge 0$. Then the upper renewal tail $\ell \ge 2n - j$ satisfies*
   $$\left|\sum_{\ell = 2n - j}^n W_\ell^{(n)}(j, u)\,\chi_\ell(u)\right| \le 2^{-j}\sum_{\ell = 2n - j}^n \binom{j}{n - \ell} = 2^{-j}\sum_{k=n}^j \binom{j}{k} = \mathbb{P}(s_n \le j),$$
   *yielding the horizon-truncated bound*
   $$\bigl|\chi_n(2^j u)\bigr| \le U_{\mathrm{horiz}}(n, j; u) := 2\,\mathbb{P}(s_n \le j) + 2^{-j}\sum_{\ell=1}^{2n - j - 1} \binom{j}{n - \ell}\,\bigl|\chi_\ell(u)\bigr|.$$
   *In particular, with $\theta^* = \ln\frac{\lambda}{2(\lambda - 1)} \approx +0.30365549 > 0$, using only the $\ell \le 1{,}000$ certified upper bounds $\overline{|\chi_\ell(1)|}$ from `collatz_2/v2` [2, Corollary 3], the bound*
   $$\bigl|\chi_n(2^j)\bigr| \le 40\,e^{\theta^* j}(\lambda - 1)^n = 40\,e^{-I n + \theta^*(j - \lambda n)}$$
   *holds for every $1 \le n \le 2{,}394$ and all $j \ge \max(0, 2n - 1001)$ (which includes the extremal window $j \ge \lfloor n\lambda\rfloor - 7$ up to $n = 2{,}394$, and $j \ge \lfloor n\lambda\rfloor - 6$ up to $n = 2{,}397$).*

#### Proof of Theorem 3.1

1. For $k = 0$, $\{\tau_j = 1\} = \{a_1 > j\}$ has probability $\sum_{a_1 = j+1}^\infty 2^{-a_1} = 2^{-j} = \binom{j}{0} 2^{-j}$. For $1 \le k \le j$, the event $\{s_k = s\}$ ($k \le s \le j$) requires choosing $k - 1$ distinct partial-sum locations $1 \le s_1 < s_2 < \dots < s_{k-1} < s$ in $\{1, \dots, s - 1\}$ with joint probability $2^{-(a_1 + \dots + a_k)} = 2^{-s}$, so $\mathbb{P}(s_k = s) = \binom{s-1}{k-1} 2^{-s}$. Conditioning on $s_k = s \le j$, the overshoot event $\{s_{k+1} > j\} = \{a_{k+1} > j - s\}$ is independent of $(a_1, \dots, a_k)$ and has probability $2^{-(j - s)}$, which cancels $2^{-s}$ identically:
   $$\mathbb{P}(\tau_j = k + 1) = \sum_{s=k}^j \mathbb{P}(s_k = s)\,\mathbb{P}(a_{k+1} > j - s) = \sum_{s=k}^j \binom{s - 1}{k - 1} 2^{-s}\cdot 2^{-(j - s)} = 2^{-j}\sum_{s=k}^j \binom{s - 1}{k - 1} = \binom{j}{k} 2^{-j}$$
   by the hockey-stick identity. Equivalently, the set of visited partial sums $\{s_m : m \ge 1\} \cap \{1, \dots, j\}$ is a $\mathrm{Bernoulli}(1/2)$ random subset of $\{1, \dots, j\}$, and $\tau_j - 1 = \#\{m \ge 1 : s_m \le j\} \sim \mathrm{Binomial}(j, 1/2)$. Since $0 \le \tau_j - 1 = n - \ell \le j$, the nonvanishing renewal terms satisfy $0 \le n - \ell \le j \iff \max(1, n - j) \le \ell \le n$. Taking moduli in the renewal identity gives Part (1).
2. For $1 \le n \le j < 2n$, substituting $m = n - \ell$ ($0 \le m \le j - n$) and applying Pascal symmetry $\binom{j}{m} = \binom{j}{j - m}$ with $k = j - m \in \{n, \dots, j\}$ gives
   $$\sum_{\ell = 2n - j}^n \binom{j}{n - \ell} 2^{-j} = \sum_{m=0}^{j - n} \binom{j}{m} 2^{-j} = \sum_{k=n}^j \binom{j}{k} 2^{-j} = \mathbb{P}(s_n \le j).$$
   For $j \ge 2n$, $2n - j \le 0$ so no terms are truncated and $|\chi_n(2^j u)| \le \mathbb{P}(s_n \le j) + \sum_{\ell=1}^n \mathbb{P}(s_{n-\ell} \le j)|\chi_\ell(u)|$. By Chernoff's inequality [2, §3.3] with $\theta^* = \ln\frac{\lambda}{2(\lambda - 1)} > 0$ and $\mathbb{E}[e^{-\theta^* a_1}] = \frac{1}{2e^{\theta^*} - 1} = \lambda - 1$, we have $\mathbb{P}(s_m \le j) \le e^{\theta^* j}(\lambda - 1)^m = e^{-I m + \theta^*(j - \lambda m)}$ for all $m, j \ge 0$. Bounding $|\chi_\ell(u)| \le 1$ for $\ell \ge 2n - j$ adds at most $\mathbb{P}(s_n \le j) \le e^{\theta^* j}(\lambda - 1)^n$, increasing the constant $1 + \sum_{\ell=1}^{1000} \overline{|\chi_\ell(1)|}(\lambda - 1)^{-\ell} \le 38.95 < 39$ of [2, Corollary 3] by $1$ to $40$ whenever $2n - j - 1 \le 1000 \iff j \ge 2n - 1001$ (as independently verified by `u/fourier_wren` in `cWIuzQnGz6g2zN4q` on `r/collatz/post/21`). $\square$

| $n$ | $j^*$ | Certified LB (`certify_M.txt`) | Cor. 3 UB (`certify_M.txt`) | Exact Rational $U_{\mathrm{binom}}(n, j^*; 1)$ | Improvement Factor | Remaining Gap |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $100$ | $152$ | $1.5936 \times 10^{-5}$ | $2.222 \times 10^{-2}$ | $3.5705 \times 10^{-4}$ | **$62.2\times$** | $22.4\times$ |
| $200$ | $310$ | $2.7274 \times 10^{-8}$ | $7.827 \times 10^{-5}$ | $1.0805 \times 10^{-6}$ | **$72.4\times$** | $39.6\times$ |
| $400$ | $627$ | $2.3022 \times 10^{-13}$ | $1.316 \times 10^{-9}$ | $1.5197 \times 10^{-11}$ | **$86.6\times$** | $66.0\times$ |
| $600$ | $944$ | $2.5620 \times 10^{-18}$ | $2.211 \times 10^{-14}$ | $2.2883 \times 10^{-16}$ | **$96.6\times$** | $89.3\times$ |
| $800$ | $1261$ | $3.1301 \times 10^{-23}$ | $3.717 \times 10^{-19}$ | $3.5602 \times 10^{-21}$ | **$104.4\times$** | $113.7\times$ |
| $1000$ | $1578$ | $4.0326 \times 10^{-28}$ | $6.247 \times 10^{-24}$ | $5.6426 \times 10^{-26}$ | **$110.7\times$** | $139.9\times$ |

*Table 2: Exact rational evaluation of $U_{\mathrm{binom}}(n, j^*; 1)$ from Theorem 3.1(1) using all $1 \le \ell \le n$ certified upper bounds $\overline{|\chi_\ell(1)|}$ from `certify_chi1.txt` [2] with zero dropped terms (`verify_paper5.py`, Suite 2).*

| $n$ | $j^*$ | Reflection Horizon $L_*(n, j^*) = 2n - j^* - 1$ | Certified Rational $U_{\mathrm{horiz}}(n, j^*; 1)$ | Exact DP Value $M_n^*$ [2, Table 2] |
| :---: | :---: | :---: | :---: | :---: |
| $1200$ | $1895$ | $504 \le 1000$ | $1.0230 \times 10^{-30}$ | $5.391 \times 10^{-33}$ |
| $1400$ | $2212$ | $587 \le 1000$ | $1.6467 \times 10^{-35}$ | $7.411 \times 10^{-38}$ |
| $1700$ | $2688$ | $711 \le 1000$ | $1.2456 \times 10^{-42}$ | $3.920 \times 10^{-45}$ |
| $2000$ | $3163$ | $836 \le 1000$ | $7.0755 \times 10^{-50}$ | $2.159 \times 10^{-52}$ |
| $2394$ | $3787$ | $1000 \le 1000$ | $2.2847 \times 10^{-59}$ | — |

*Table 3: Certified rational upper bounds $U_{\mathrm{horiz}}(n, j^*; 1)$ for $1200 \le n \le 2394$ obtained from Theorem 3.1(2) using only the $\ell \le 1{,}000$ certified column of `certify_chi1.txt` [2] (`verify_paper5.py`, Suite 2).*

*Remark 3.2 (Gaussian Curvature of the Binomial Renewal Weights):* For $j = \lambda n + \delta$ with bounded $\delta$, expanding $\ln\frac{\binom{j}{n-\ell}}{\binom{j}{n}} = \sum_{i=0}^{\ell-1} \ln\frac{n-i}{j-n+i+1}$ gives
$$\ln\frac{\binom{j}{n - \ell}}{\binom{j}{n}} = -\ell\ln(\lambda - 1) - \frac{\ell(\ell - 1)}{2n} - \frac{\ell(\ell + 1 + 2\delta)}{2(\lambda - 1)n} + O\!\left(\frac{\ell^3 + \ell}{n^2}\right) = -\ell\ln(\lambda - 1) - \frac{\lambda}{2(\lambda - 1)}\frac{\ell^2}{n} - \frac{(2 - \lambda + 2\delta)\ell}{2(\lambda - 1)n} + O\!\left(\frac{\ell^3 + \ell}{n^2}\right),$$
so the binomial weights suppress large renewal indices $\ell$ quadratically with leading curvature coefficient $\frac{\lambda}{2(\lambda - 1)} \approx 1.35476$ (together with the linear finite-$n$ drift term $-\frac{(2-\lambda+2\delta)\ell}{2(\lambda-1)n}$).

---

### Theorem 3.3 (Quarter-Plane Twisted Pascal Green's Functions and Dual Backward Adjoint Recurrence)

*Fix $j \ge 1$ and $u \in \mathbb{Z}$ with $3 \nmid u$. While [2, §3.2] evaluates $\mathcal{M}_n(j, u)$ and all $W_\ell^{(n)}(j, u)$ in one $O(n j)$ forward pass in the cumulative valuation coordinate $s_m$, reversing the step and valuation coordinates via $t_r := j - s_{n - r + 1} \in \{0, 1, \dots, j - 1\}$ places both families of kernels on a common two-term Pascal recurrence:*

1. *(Ordered-Simplex Representation and Forward Twisted Pascal PDE): Both $\mathcal{M}_n(j, u)$ and $W_\ell^{(n)}(j, u)$ ($1 \le \ell \le n$) are finite ordered-simplex sums:*
   $$\mathcal{M}_n(j, u) = 2^{-j} \sum_{0 \le t_1 < t_2 < \dots < t_n \le j - 1} 2^{t_1} \prod_{r=1}^n e\!\left(\frac{u\,2^{t_r}}{3^r}\right), \qquad W_\ell^{(n)}(j, u) = 2^{-j} \sum_{0 \le t_{\ell+1} < \dots < t_n \le j - 1} \prod_{r=\ell+1}^n e\!\left(\frac{u\,2^{t_r}}{3^r}\right).$$
   *Consequently, both $\mathcal{M}_r(t, u)$ ($r \ge 1$) and $W_\ell^{(r)}(t, u)$ ($r > \ell$) satisfy the identical two-term Quarter-Plane Twisted Pascal PDE on $(r, t) \in \mathbb{Z}_{\ge 1}^2$:*
   $$F_r(t) = \frac{1}{2}\,F_r(t - 1) + \frac{1}{2}\,e\!\left(\frac{u\,2^{t - 1}}{3^r}\right) F_{r - 1}(t - 1) \qquad (t \ge 1),$$
   *where $\mathcal{M}_r(t, u)$ has horizontal boundary condition $F_0(t) = 1$ ($t \ge 0$), $F_r(0) = 0$ ($r \ge 1$), and $W_\ell^{(r)}(t, u)$ has vertical boundary condition $F_\ell(t) = 2^{-t}$ ($t \ge 0$), $F_r(0) = 0$ ($r > \ell$). Under the Cramér tilt $\widehat{F}_r(t) := e^{I r + \theta^*(r\lambda - t)} F_r(t)$, the transition weights become $q = \frac{1}{2}e^{-\theta^*} = 1 - \frac{1}{\lambda}$ and $p = \frac{1}{2}e^{I + \theta^*(\lambda - 1)} = \frac{1}{\lambda}$, with $p + q = 1$ and exact zero drift $p(\lambda - 1) - q = 0$.*
2. *(Dual Backward Adjoint Formulation): Define the backward adjoint field $w_r(t)$ on $0 \le r \le n,\; 0 \le t \le j$ with terminal seed $w_n(j) = 1$, $w_r(j) = 0$ ($0 \le r < n$), and backward recurrence for $t = j - 1, j - 2, \dots, 0$:*
   $$\begin{aligned}
   w_n(t) &= \frac{1}{2}\,w_n(t + 1), \\
   w_r(t) &= \frac{1}{2}\,w_r(t + 1) + \frac{1}{2}\,e\!\left(\frac{u\,2^t}{3^{r+1}}\right) w_{r+1}(t + 1) \qquad (1 \le r \le n - 1), \\
   w_0(t) &= w_0(t + 1) + \frac{1}{2}\,e\!\left(\frac{u\,2^t}{3^1}\right) w_1(t + 1).
   \end{aligned}$$
   *Then $\mathcal{M}_n(j, u) = w_0(0)$ and every renewal kernel $W_\ell^{(n)}(j, u)$ ($1 \le \ell \le n - 1$) is given by*
   $$W_\ell^{(n)}(j, u) = \sum_{t=0}^{j-1} 2^{-(t + 1)}\,e\!\left(\frac{u\,2^t}{3^{\ell + 1}}\right) w_{\ell + 1}(t + 1), \qquad W_n^{(n)}(j, u) = 2^{-j}.$$
3. *(Two-Step Horizontal Plaquette Cosine Majorant): Unrolling $F_r(t)$ by two horizontal steps $t \mapsto t + 2$ gives for all $r \ge 2$ and $t \ge 0$:*
   $$F_r(t + 2) = \frac{1}{4}\,F_r(t) + \frac{1}{4}\Bigl(e\bigl(u\,2^t / 3^r\bigr) + e\bigl(u\,2^{t+1} / 3^r\bigr)\Bigr) F_{r - 1}(t) + \frac{1}{4}\,e\!\left(\frac{u\,2^{t+1}}{3^r}\right) e\!\left(\frac{u\,2^t}{3^{r-1}}\right) F_{r - 2}(t),$$
   *where the middle coefficient has modulus $\frac{1}{2}\bigl|\cos(\pi u\,2^t / 3^r)\bigr|$ at the single modulus $3^r$. Thus $|F_r(t)| \le \widetilde{F}_r(t)$ where $\widetilde{F}_r(t + 2) = \frac{1}{4}\widetilde{F}_r(t) + \frac{1}{2}|\cos(\pi u\,2^t / 3^r)|\widetilde{F}_{r - 1}(t) + \frac{1}{4}\widetilde{F}_{r - 2}(t)$ for $r \ge 2$ and $\widetilde{F}_1(t + 2) = \frac{1}{4}\widetilde{F}_1(t) + \bigl|\frac{1}{4}e(u\,2^t / 3) + \frac{1}{2}e(u\,2^{t+1} / 3)\bigr|\widetilde{F}_0(t)$.*

#### Proof of Theorem 3.3

1. On the event $\{s_n \le j\}$, the $n$-tuple $(s_1, \dots, s_n)$ ranges over all strictly increasing integer sequences $1 \le s_1 < s_2 < \dots < s_n \le j$ with probability $2^{-s_n}$. Setting $t_r := j - s_{n - r + 1}$ ($1 \le r \le n$) maps $(s_1, \dots, s_n)$ bijectively onto $0 \le t_1 < t_2 < \dots < t_n \le j - 1$ with $2^{-s_n} = 2^{-(j - t_1)} = 2^{-j} 2^{t_1}$ and $e(u\,2^{j - s_m} / 3^{n - m + 1}) = e(u\,2^{t_r} / 3^r)$ ($r = n - m + 1$). Similarly, on $\{\tau_j = n - \ell + 1\} = \{s_{n-\ell} \le j < s_{n-\ell+1}\}$, summing over $a_{n-\ell+1} > j - s_{n-\ell}$ gives probability $2^{-s_{n-\ell}} 2^{-(j - s_{n-\ell})} = 2^{-j}$ for each strictly increasing sequence $0 \le t_{\ell+1} < \dots < t_n \le j - 1$ ($t_r = j - s_{n - r + 1}$). Splitting the ordered-simplex sum over $0 \le t_1 < \dots < t_r \le t - 1$ according to whether $t_r \le t - 2$ (contributing $\frac{1}{2} F_r(t - 1)$) or $t_r = t - 1$ (contributing $\frac{1}{2} e(u\,2^{t-1}/3^r) F_{r-1}(t-1)$) establishes the forward recurrence and boundary conditions. Multiplying by $e^{I r + \theta^*(r\lambda - t)}$ and using $\lambda H(1/\lambda) = \ln\lambda - (\lambda - 1)\ln(\lambda - 1)$ gives $I + \theta^*(\lambda - 1) = \ln 2 - \ln\lambda$, so $\frac{1}{2}e^{I + \theta^*(\lambda - 1)} = \frac{1}{\lambda} = p$ and $\frac{1}{2}e^{-\theta^*} = \frac{\lambda - 1}{\lambda} = q$.
2. On the directed acyclic lattice $\{0, \dots, n\} \times \{0, \dots, j\}$ where horizontal edges $(r, t) \to (r, t + 1)$ have weight $1$ for $r = 0$ and $\frac{1}{2}$ for $1 \le r \le n$, and diagonal edges $(r, t) \to (r + 1, t + 1)$ have weight $\frac{1}{2} e(u\,2^t / 3^{r+1})$, $F_n(j) = \mathcal{M}_n(j, u)$ is the total weighted path sum from $(0, 0)$ to $(n, j)$, which by path reversal equals $w_0(0)$. For $1 \le \ell < n$, every path contributing to $W_\ell^{(n)}(j, u)$ starts at $(\ell, 0)$ with weight $1$, takes $t \ge 0$ horizontal steps along row $\ell$ with weight $2^{-t}$, takes its first diagonal step $(\ell, t) \to (\ell + 1, t + 1)$ with weight $\frac{1}{2} e(u\,2^t / 3^{\ell+1})$, and continues from $(\ell + 1, t + 1)$ to $(n, j)$ with total weight $w_{\ell+1}(t + 1)$.
3. Substituting $F_r(t + 1)$ and $F_{r-1}(t + 1)$ into $F_r(t + 2) = \frac{1}{2} F_r(t + 1) + \frac{1}{2} e(u\,2^{t+1} / 3^r) F_{r-1}(t + 1)$ gives the three-term identity in Part (3), and $|e(\theta) + e(2\theta)| = 2|\cos(\pi\theta)|$ yields $|F_r(t)| \le \widetilde{F}_r(t)$ by induction on $t$. $\square$

---

### Theorem 3.4 (Skip-Free Cold-Triangle Defect Formula for $d_0 \le 0$)

*For any nonpositive integer shift $d_0 \le 0$, define the Cold Triangle $\mathcal{T}_{d_0} := \{(r, t) \in \mathbb{Z}_{\ge 0}^2 : t \le B(r)\}$ where $B(r) := \lfloor r\lambda\rfloor - d_0 \ge 0$, so that the initial source $(0, 0)$ lies in $\mathcal{T}_{d_0}$. Let $F_r^{\mathrm{cold}}(t)$ be the solution to the forward Twisted Pascal PDE of Theorem 3.3(1) restricted to $\mathcal{T}_{d_0}$ (with $F_0^{\mathrm{cold}}(t) = 1$ for $0 \le t \le B(0)$ and $F_r^{\mathrm{cold}}(t) := 0$ whenever $t > B(r)$). For each $m \ge 0$ with $B(m) < j$, let $K^{(m)}_r(t)$ be the forward Twisted Pascal propagator on $\mathbb{Z}_{\ge 0}^2$ with point source $K^{(m)}_m(B(m) + 1) = 1$ and $K^{(m)}_r(t) = 0$ for $r < m$ or $t \le B(m)$. Then for every $(r, t) \in \mathbb{Z}_{\ge 0}^2$:*
$$F_r(t) = F_r^{\mathrm{cold}}(t) + \sum_{m=0}^r h_m\,F_m^{\mathrm{cold}}\bigl(B(m)\bigr)\,K^{(m)}_r(t), \qquad h_m := \begin{cases} 1 & \text{if } m = 0, \\ 1/2 & \text{if } m \ge 1. \end{cases}$$

#### Proof of Theorem 3.4

Since $d_0 \le 0$, $B(0) = -d_0 \ge 0$, so the initial source $(0, 0)$ lies inside $\mathcal{T}_{d_0}$. Since $\lambda = \log_2 3 \in (1, 2)$, for every integer $r \ge 1$ we have
$$B(r) - B(r - 1) = \lfloor r\lambda\rfloor - \lfloor(r - 1)\lambda\rfloor \in \{1, 2\} \ge 1.$$
Consequently, for any site $(r - 1, t - 1) \in \mathcal{T}_{d_0}$ (so $t - 1 \le B(r - 1)$), the target $(r, t)$ of the diagonal transition $(r - 1, t - 1) \to (r, t)$ satisfies $t \le B(r - 1) + 1 \le B(r)$, and therefore $(r, t) \in \mathcal{T}_{d_0}$. Thus **no diagonal step can ever exit $\mathcal{T}_{d_0}$**. Every directed path from $(0, 0) \in \mathcal{T}_{d_0}$ that visits $\mathbb{Z}_{\ge 0}^2 \setminus \mathcal{T}_{d_0}$ must make its first exit from $\mathcal{T}_{d_0}$ via a horizontal step $(m, B(m)) \to (m, B(m) + 1)$ at some row $m \in \{0, \dots, r\}$, which carries transition weight $h_m = 1$ if $m = 0$ and $h_m = \frac{1}{2}$ if $m \ge 1$. Decomposing all directed paths from $(0, 0)$ to $(r, t)$ according to whether they remain inside $\mathcal{T}_{d_0}$ for all steps (contributing $F_r^{\mathrm{cold}}(t)$) or first exit $\mathcal{T}_{d_0}$ via $(m, B(m)) \to (m, B(m) + 1)$ (contributing $h_m F_m^{\mathrm{cold}}(B(m)) K^{(m)}_r(t)$) establishes the identity (verified across $d_0 \in \{-3, -2, -1, 0\}$ to $1.14 \times 10^{-16}$ in `verify_paper5.py`, Suite 3). $\square$

---

## 4. The $m$-Step Horizontal Plaquette Majorant Hierarchy, Circle-Average Parseval Saddle Rate, and Model Suffix-Depinning Transition

For any frequency $\xi \in \mathbb{Z}$, define $\eta_r(s; \xi) := \chi_r(2^{-s}\xi)$ for $r \ge 0, s \ge 0$. Conditioning the first geometric step $a_1 \sim \mathrm{Geom}(1/2)$ on $a_1 = 1$ versus $a_1 \ge 2$ ($a_1 = 1 + a_1'$) shows that $\eta_r(s; \xi)$ satisfies the Quarter-Plane Twisted Pascal recurrence
$$\eta_r(s; \xi) = \frac{1}{2}\,\eta_r(s + 1; \xi) + \frac{1}{2}\,\phi_r(s; \xi)\,\eta_{r - 1}(s + 1; \xi), \qquad \phi_r(s; \xi) := e\!\left(\frac{2^{-(s + 1)}\xi \bmod 3^r}{3^r}\right),$$
for all $r \ge 1, s \ge 0$, with boundary condition $\eta_0(s; \xi) = 1$. Extending $\phi_r(s; \xi) := 1$ and $\eta_r(s; \xi) := 1$ for all integers $r \le 0$ preserves this recurrence identically for all $r \in \mathbb{Z}$, since $1 = \frac{1}{2}(1) + \frac{1}{2}(1)(1)$.

### Theorem 4.1 ($m$-Step Horizontal Plaquette Unrolling and Nonnegative Majorant Hierarchy)

*Fix an integer plaquette width $m \ge 1$. For any $r \in \mathbb{Z}$ and $s \ge 0$, define the local $m$-step plaquette coefficients $\widehat{Q}_{r, k}^{(j)}(s; \xi)$ ($0 \le j \le m,\; 0 \le k \le j$) by $\widehat{Q}_{r, 0}^{(0)}(s; \xi) := 1$ and, for $0 \le j < m$:*
$$\widehat{Q}_{r, 0}^{(j + 1)}(s; \xi) = \frac{1}{2}\,\widehat{Q}_{r, 0}^{(j)}(s; \xi) = 2^{-(j + 1)}, \qquad \widehat{Q}_{r, k}^{(j + 1)}(s; \xi) = \frac{1}{2}\,\widehat{Q}_{r, k}^{(j)}(s; \xi) + \frac{1}{2}\,\phi_{r + 1 - k}(s + j; \xi)\,\widehat{Q}_{r, k - 1}^{(j)}(s; \xi) \quad (1 \le k \le j + 1),$$
*where $\widehat{Q}_{r, j + 1}^{(j)}(s; \xi) := 0$. Then:*
1. *(Exact $m$-Step Horizontal Identity): For all $r \in \mathbb{Z}$ and $s \ge 0$,*
   $$\eta_r(s; \xi) = \sum_{k=0}^m \widehat{Q}_{r, k}^{(m)}(s; \xi)\,\eta_{r - k}(s + m; \xi).$$
2. *(Self-Contained Nonnegative Majorant Hierarchy with Rigorous Terminal Cutoff): Fix a cutoff $S_{\max} = N_{\mathrm{grid}} m \in m\mathbb{Z}_{\ge 1}$. Define $\widetilde{\eta}_r^{(m)}(s; \xi) := 1$ for $r \le 0$, set the terminal boundary condition $\widetilde{\eta}_r^{(m)}(S_{\max}; \xi) := 1$ for all $r \ge 1$, and for $r \ge 1$ and $s \in \{0, m, 2m, \dots, S_{\max} - m\}$ define recursively in decreasing $s$:*
   $$\widetilde{\eta}_r^{(m)}(s; \xi) := \sum_{k=0}^m \bigl|\widehat{Q}_{r, k}^{(m)}(s; \xi)\bigr|\,\widetilde{\eta}_{r - k}^{(m)}(s + m; \xi) = 2^{-m}\,\widetilde{\eta}_r^{(m)}(s + m; \xi) + \sum_{k=1}^m \bigl|\widehat{Q}_{r, k}^{(m)}(s; \xi)\bigr|\,\widetilde{\eta}_{r - k}^{(m)}(s + m; \xi).$$
   *Then $\bigl|\chi_r(2^{-s}\xi)\bigr| = \bigl|\eta_r(s; \xi)\bigr| \le \widetilde{\eta}_r^{(m)}(s; \xi)$ holds rigorously for all $r \ge 0$ and all $s \in \{0, m, 2m, \dots, S_{\max}\}$ with zero omitted tail.*

#### Proof of Theorem 4.1

1. We proceed by induction on $j \in \{0, 1, \dots, m\}$ to show that $\eta_r(s; \xi) = \sum_{k=0}^j \widehat{Q}_{r, k}^{(j)}(s; \xi)\,\eta_{r - k}(s + j; \xi)$ for all $r \in \mathbb{Z}$. For $j = 0$ the identity is $\eta_r(s; \xi) = 1 \cdot \eta_r(s; \xi)$. Assuming the identity holds at step $j$, substitute the one-step Pascal recurrence $\eta_{r - k}(s + j; \xi) = \frac{1}{2}\eta_{r - k}(s + j + 1; \xi) + \frac{1}{2}\phi_{r - k}(s + j; \xi)\eta_{r - k - 1}(s + j + 1; \xi)$ for each $0 \le k \le j$:
   $$\begin{aligned}
   \eta_r(s; \xi) &= \sum_{k=0}^j \frac{1}{2}\,\widehat{Q}_{r, k}^{(j)}(s; \xi)\,\eta_{r - k}(s + j + 1; \xi) + \sum_{k=0}^j \frac{1}{2}\,\phi_{r - k}(s + j; \xi)\,\widehat{Q}_{r, k}^{(j)}(s; \xi)\,\eta_{r - k - 1}(s + j + 1; \xi) \\
   &= \sum_{k=0}^{j+1} \left(\frac{1}{2}\,\widehat{Q}_{r, k}^{(j)}(s; \xi) + \frac{1}{2}\,\phi_{r + 1 - k}(s + j; \xi)\,\widehat{Q}_{r, k - 1}^{(j)}(s; \xi)\right) \eta_{r - k}(s + j + 1; \xi) \\
   &= \sum_{k=0}^{j+1} \widehat{Q}_{r, k}^{(j + 1)}(s; \xi)\,\eta_{r - k}(s + j + 1; \xi),
   \end{aligned}$$
   where the second line re-indexes $k' = k + 1$ in the second sum. Setting $j = m$ proves Part (1).
2. At $r \le 0$, $|\eta_r(s; \xi)| = 1 = \widetilde{\eta}_r^{(m)}(s; \xi)$. For $r \ge 1$, at the right boundary $s = S_{\max}$ we have $|\eta_r(S_{\max}; \xi)| = |\chi_r(2^{-S_{\max}}\xi)| \le 1 = \widetilde{\eta}_r^{(m)}(S_{\max}; \xi)$. By induction on $r \ge 1$ and downward induction on $s = S_{\max} - m, S_{\max} - 2m, \dots, 0$, taking absolute values in Part (1) and applying the triangle inequality gives
   $$\bigl|\eta_r(s; \xi)\bigr| \le \sum_{k=0}^m \bigl|\widehat{Q}_{r, k}^{(m)}(s; \xi)\bigr|\,\bigl|\eta_{r - k}(s + m; \xi)\bigr| \le \sum_{k=0}^m \bigl|\widehat{Q}_{r, k}^{(m)}(s; \xi)\bigr|\,\widetilde{\eta}_{r - k}^{(m)}(s + m; \xi) = \widetilde{\eta}_r^{(m)}(s; \xi). \quad \square$$

---

### Theorem 4.2 (Circle-Average $L^2(\mathbb{T})$ Parseval Saddle Rate via Valuation-Peeling Injectivity)

*For any $m \ge 1$ and $0 \le k \le m$, define the continuum $m$-step plaquette polynomial on $\mathbb{T} = \mathbb{R}/\mathbb{Z}$ by*
$$\mathcal{P}_k^{(m)}(\theta) := \sum_{0 \le j_1 < j_2 < \dots < j_k < m} e\bigl(\Sigma(j_1, \dots, j_k)\,\theta\bigr), \qquad \Sigma(j_1, \dots, j_k) := \sum_{i=1}^k 3^{i - 1}\,2^{m - 1 - j_i}.$$
*Then:*
1. *(Frequency Injectivity via Tao [1, Lemma 6.2]): By Tao's $2$-adic valuation-peeling lemma [1, Lemma 6.2] (setting $s_i = j_i + 1$ so $2^{-m}\Sigma(j_1, \dots, j_k) = \sum_{i=1}^k 3^{i-1} 2^{-s_i}$), the frequency map $(j_1, \dots, j_k) \mapsto \Sigma(j_1, \dots, j_k)$ is strictly injective on the set of all $\binom{m}{k}$ strictly increasing tuples $0 \le j_1 < j_2 < \dots < j_k < m$.*
2. *(Exact Circle-Average $L^2(\mathbb{T})$ Norm and Parseval Saddle Rate): For every $m \ge 1$ and $0 \le k \le m$,*
   $$\left\|2^{-m}\mathcal{P}_k^{(m)}\right\|_{L^1(\mathbb{T})} \le \left\|2^{-m}\mathcal{P}_k^{(m)}\right\|_{L^2(\mathbb{T})} = 2^{-m}\sqrt{\binom{m}{k}},$$
   *and the asymptotic per-level $L^2(\mathbb{T})$ saddle rate across all slopes $\alpha = k/m \in (0, 1]$ attains its unique global maximum at $\alpha^* = \frac{3}{4}$, with value strictly below the renewal threshold $\lambda - 1$:*
   $$\lim_{m \to \infty} \max_{1 \le k \le m} \left(2^{-m}\sqrt{\binom{m}{k}}\right)^{1/k} = \max_{\alpha \in (0, 1]} \exp\!\left(\frac{H(\alpha) - 2\ln 2}{2\alpha}\right) = \frac{1}{\sqrt{3}} \approx 0.57735027 < \lambda - 1 \approx 0.58496250.$$

#### Proof of Theorem 4.2

1. As in [1, Lemma 6.2], for $k \ge 1$ the exponents of $2$ in $\Sigma(j_1, \dots, j_k) = \sum_{i=1}^k 3^{i-1} 2^{m - 1 - j_i}$ satisfy $m - 1 - j_k < m - 1 - j_{k-1} < \dots < m - 1 - j_1$ with odd coefficients $3^{i-1}$, so $v_2\bigl(\Sigma(j_1, \dots, j_k)\bigr) = m - 1 - j_k$ uniquely determines $j_k$, and peeling off $i = k, k - 1, \dots, 1$ inductively determines $(j_1, \dots, j_k)$.
2. By Part (1), the $\binom{m}{k}$ characters $e(\Sigma(j_1, \dots, j_k)\theta)$ in $\mathcal{P}_k^{(m)}(\theta)$ have pairwise distinct integer frequencies and are mutually orthogonal in $L^2(\mathbb{T})$, so Parseval's identity on $\mathbb{T}$ gives $\|2^{-m}\mathcal{P}_k^{(m)}\|_{L^2(\mathbb{T})}^2 = 2^{-2m}\binom{m}{k}$. Writing $k = \alpha m$ with $\alpha \in (0, 1]$, Stirling's formula $\frac{1}{m}\ln\binom{m}{\alpha m} = H(\alpha) + O(\frac{\ln m}{m})$ implies $\bigl(2^{-m}\sqrt{\binom{m}{k}}\bigr)^{1/k} \to \rho_{L^2}(\alpha) := \exp\bigl(\frac{H(\alpha) - 2\ln 2}{2\alpha}\bigr)$. Differentiating $f(\alpha) := \ln\rho_{L^2}(\alpha) = \frac{-\alpha\ln\alpha - (1-\alpha)\ln(1-\alpha) - 2\ln 2}{2\alpha}$ on $(0, 1)$ gives
   $$f'(\alpha) = \frac{\ln(1 - \alpha) + 2\ln 2}{2\alpha^2} = \frac{\ln\bigl(4(1 - \alpha)\bigr)}{2\alpha^2}, \qquad f''(\alpha) = -\frac{1}{2\alpha^2(1 - \alpha)} - \frac{\ln\bigl(4(1 - \alpha)\bigr)}{\alpha^3}.$$
   Thus $f'(\alpha) = 0$ at the unique stationary point $\alpha^* = \frac{3}{4}$ ($f''(3/4) = -\frac{32}{9} < 0$), where $f(3/4) = -\frac{1}{2}\ln 3$ and $\rho_{L^2}(3/4) = \frac{1}{\sqrt{3}} \approx 0.57735027 < \lambda - 1 \approx 0.58496250$. $\square$

*Scope Note on Theorem 4.2:* Theorem 4.2 computes the circle-average $L^2(\mathbb{T})$ norm of $\mathcal{P}_k^{(m)}(\theta)$; at $\theta = 0$, $\mathcal{P}_k^{(m)}(0) = \binom{m}{k}$ has no cancellation, so the circle average is not a pointwise bound and does not by itself prove an all-$r$ deterministic contraction rate for the correlated modular phases sampled in Theorem 4.1.

---

### Theorem 4.3 (Model Suffix-Depinning Phase-Transition Formula $I_{\mathrm{eff}}(\rho)$)

*For any constant post-crossing damping base $\rho \in (0, 1]$ and $j_n := \lfloor\lambda n\rfloor$, define the model renewal convolution*
$$\mathcal{R}_n(\rho) := \sum_{\ell=0}^n \binom{j_n}{n - \ell} 2^{-j_n} \rho^\ell.$$
*Then the exponential decay rate $I_{\mathrm{eff}}(\rho) := \lim_{n \to \infty} -\frac{1}{n}\ln\mathcal{R}_n(\rho)$ undergoes a second-order depinning phase transition at the critical threshold $\rho_c = \lambda - 1 = \log_2(3/2) \approx 0.58496250$:*
$$I_{\mathrm{eff}}(\rho) = \begin{cases} \lambda\ln\!\left(\dfrac{2\rho}{1 + \rho}\right) - \ln\rho & \text{if } \lambda - 1 < \rho \le 1 \quad \left(\text{depinned suffix: }\dfrac{\ell^*}{n} = \beta^*(\rho) = 1 - \dfrac{\lambda}{1 + \rho} > 0\right), \\[10pt] I = \lambda\ln 2 - \lambda H(1/\lambda) \approx 0.05497965 & \text{if } 0 < \rho \le \lambda - 1 \quad \left(\text{pinned suffix: }\dfrac{\ell^*}{n} = \beta^*(\rho) = 0\right). \end{cases}$$

#### Proof of Theorem 4.3

Writing $\ell = \beta n$ with $\beta \in [0, 1]$, Stirling's formula gives uniformly on compact subsets of $[0, 1)$ that $\frac{1}{n}\ln\bigl(\binom{j_n}{n - \ell} 2^{-j_n} \rho^\ell\bigr) = \Psi_\rho(\beta) + O\bigl(\frac{\ln n}{n}\bigr)$, where
$$\Psi_\rho(\beta) := -\lambda\ln 2 + \lambda H\!\left(\frac{1 - \beta}{\lambda}\right) + \beta\ln\rho \qquad (\beta \in [0, 1]).$$
Differentiating $\Psi_\rho(\beta)$ twice on $(0, 1)$ using $H'(x) = \ln\frac{1 - x}{x}$ yields
$$\Psi'_\rho(\beta) = \ln\!\left(\frac{\rho(1 - \beta)}{\lambda - 1 + \beta}\right), \qquad \Psi''_\rho(\beta) = -\frac{\lambda}{(1 - \beta)(\lambda - 1 + \beta)} < 0.$$
Thus $\Psi_\rho(\beta)$ is strictly concave on $[0, 1]$ with initial slope $\Psi'_\rho(0) = \ln\bigl(\frac{\rho}{\lambda - 1}\bigr)$:
- **Pinned Regime ($0 < \rho \le \lambda - 1$):** Here $\Psi'_\rho(0) \le 0$ and $\Psi'_\rho(\beta) < 0$ on $(0, 1)$, so $\Psi_\rho$ attains its unique maximum on $[0, 1]$ at $\beta^*(\rho) = 0$, giving $I_{\mathrm{eff}}(\rho) = -\Psi_\rho(0) = I$.
- **Depinned Regime ($\lambda - 1 < \rho \le 1$):** Here $\Psi'_\rho(0) > 0 > \Psi'_\rho(1^-) = -\infty$, so $\Psi_\rho$ attains its unique maximum at the interior point $\beta^*(\rho) = 1 - \frac{\lambda}{1 + \rho} \in (0, 1)$, where $\frac{1 - \beta^*}{\lambda} = \frac{1}{1 + \rho}$, $1 - \frac{1 - \beta^*}{\lambda} = \frac{\rho}{1 + \rho}$, and
  $$\Psi_\rho(\beta^*) = -\lambda\ln 2 + \lambda\ln(1 + \rho) - \frac{\lambda\rho}{1 + \rho}\ln\rho + \left(1 - \frac{\lambda}{1 + \rho}\right)\ln\rho = -\lambda\ln\!\left(\frac{2\rho}{1 + \rho}\right) + \ln\rho,$$
  proving $I_{\mathrm{eff}}(\rho) = -\Psi_\rho(\beta^*) = \lambda\ln\bigl(\frac{2\rho}{1 + \rho}\bigr) - \ln\rho$. $\square$

| Plaquette Width $m$ | $\widetilde{\eta}_{100}^{(m)}(0; 1)$ ($\xi = 1$) | Base $\widetilde{\eta}_{100}^{(m)}(0; 1)^{1/100}$ | $\widetilde{\eta}_{200}^{(m)}(0; 1)$ ($\xi = 1$) | Base $\widetilde{\eta}_{200}^{(m)}(0; 1)^{1/200}$ | $\widetilde{\eta}_{200}^{(m)}(0; 2^{310})$ ($\xi = 2^{310}$) | Rate $-\frac{1}{200}\ln\widetilde{\eta}_{200}^{(m)}(0; 2^{310})$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $m = 2$ | $3.6305 \times 10^{-9}$ | $0.82338$ | $2.4771 \times 10^{-17}$ | $0.82598$ | $6.9215 \times 10^{-4}$ | $0.03638$ |
| $m = 10$ | $1.5081 \times 10^{-20}$ | $0.63356$ | $1.1810 \times 10^{-39}$ | $0.63879$ | $1.2159 \times 10^{-6}$ | $0.06810$ |
| $m = 20$ | $5.7195 \times 10^{-23}$ | $0.59920$ | $2.4866 \times 10^{-44}$ | $0.60531$ | $1.6879 \times 10^{-7}$ | $0.07797$ |
| $m = 30$ | $1.0466 \times 10^{-23}$ | $0.58911$ | $4.3894 \times 10^{-46}$ | $0.59321$ | $9.9309 \times 10^{-8}$ | $0.08063$ |
| $m = 48$ | $4.2346 \times 10^{-24}$ | $0.58381$ | $2.2518 \times 10^{-47}$ | $0.58447$ | — | — |
| $m = 60$ | $1.5711 \times 10^{-24}$ | $0.57805$ | $3.9643 \times 10^{-48}$ | $0.57942$ | — | — |

*Table 4: Finite-cutoff majorants $\widetilde{\eta}_r^{(m)}(0; \xi)$ evaluated via Theorem 4.1(2) with rigorous terminal boundary $\widetilde{\eta}_r^{(m)}(S_{\max}; \xi) = 1$ at $S_{\max} = 960$ (`verify_paper5.py`, Suite 4). At $\rho \in [0.79, 0.80]$, Theorem 4.3 gives $I_{\mathrm{eff}}(0.80) = 0.03646$ and $I_{\mathrm{eff}}(0.79) = 0.03793$, matching the $m = 2$ rate $0.03638$ at $(200, 310)$ and the empirical $0.036\text{--}0.038$ rate in [5].*

---

## 5. Single-Scale Collatz-Adjoint Identity, Top-Shell Cancellation, and Unconditional $O(1/m)$ Entry-Loss Bound

In the stopping-shell variance decomposition (`collatz_5/v3` [6], `collatz_6/v2` [7], and `r/collatz/post/7`), the multi-scale diagonal correlation sum over stopping shells $v \in [3^p, 2\cdot 3^p)$ is
$$\Sigma_{\mathrm{diag}}^{(P)}(f) := \sum_{p=1}^P \sum_{v = 3^p}^{2\cdot 3^p - 1} \frac{2 f(v)}{v}\bigl[\rho_{p+1}(v) - \rho_p(v)\bigr],$$
where $\rho_p(x) := 3^p p_p(x) = 3^p \mathbb{P}(\mathrm{Syrac}_p \equiv x \pmod{3^p})$ (with $\rho_0(x) := 1$) and $f : \mathbb{Z}_{\ge 1} \to \mathbb{R}$ is any Collatz-invariant weight satisfying $f(2v) = f(v)$ for all $v \ge 1$ and $f\bigl(\frac{2v - 1}{3}\bigr) = f(v)$ for all $v \equiv 2 \pmod 3$. For each odd integer $u \ge 1$, define its entry scale $p_0(u) \ge 0$ by $p_0(1) := 0$ and, for $u \ge 3$ odd, by the unique integer $p \ge 1$ such that $2\cdot 3^{p-1} \le u < 2\cdot 3^p$.

### Theorem 5.1 (Single-Scale Collatz-Adjoint Identity and Exact Top-Shell Cancellation)

*Let $\rho_p(x) = 3^p \mathbb{P}(\mathrm{Syrac}_p \equiv x \pmod{3^p})$ for $p \ge 0$. Then:*

1. *(Single-Scale Collatz-Adjoint Relation, cf. El Jaouhari [3, §5.4]): For every integer $p \ge 1$ and every $v \in \mathbb{Z}$,*
   $$2\,\rho_{p+1}(v) - \rho_{p+1}(2v) = 3\,\mathbf{1}_{\{v \equiv 2 \pmod 3\}}\,\rho_p\!\left(\frac{2v - 1}{3}\right).$$
2. *(Exact Top-Shell Cancellation Identity): For every integer $P \ge 1$ and every Collatz-invariant function $f : \mathbb{Z}_{\ge 1} \to \mathbb{R}$, all interior terms with $u, n < 2\cdot 3^{P-1}$ at scales $p \in [p_0(u) + 1, P]$ cancel identically, leaving only a top-shell boundary term $\mathcal{B}_P(f)$ minus a pure entry-scale quadratic loss $\mathcal{Q}_P^-(f)$:*
   $$\Sigma_{\mathrm{diag}}^{(P)}(f) = \mathcal{B}_P(f) - \mathcal{Q}_P^-(f),$$
   *where*
   $$\mathcal{B}_P(f) := \sum_{v = 3^P}^{2\cdot 3^P - 1} \frac{2 f(v)}{v}\,\rho_{P+1}(v) - \sum_{\substack{2\cdot 3^{P-1} \le n < 2\cdot 3^P \\ n\text{ odd}}} \frac{2 f(n)}{n}\,\rho_P(n), \qquad \mathcal{Q}_P^-(f) := \sum_{\substack{1 \le u < 2\cdot 3^{P-1} \\ u\text{ odd}}} \frac{2 f(u)}{u(3u + 1)}\,\rho_{p_0(u)}(u).$$

#### Proof of Theorem 5.1

1. Under the forward Syracuse step $\mathrm{Syrac}_{p+1} \equiv 2^{-a}(3\,\mathrm{Syrac}_p + 1) \pmod{3^{p+1}}$ ($a \sim \mathrm{Geom}(1/2)$), decompose the event $\{\mathrm{Syrac}_{p+1} \equiv v \pmod{3^{p+1}}\}$ according to whether $a = 1$ (probability $1/2$) or $a = 1 + a'$ with $a' \ge 1$ (where $a' \sim \mathrm{Geom}(1/2)$ with conditional probability $1/2$, as in [3, §5.4]):
   - On $\{a = 1\}$ (probability $1/2$), $2^{-1}(3\,\mathrm{Syrac}_p + 1) \equiv v \pmod{3^{p+1}} \iff 3\,\mathrm{Syrac}_p \equiv 2v - 1 \pmod{3^{p+1}}$, which has a solution if and only if $2v - 1 \equiv 0 \pmod 3 \iff v \equiv 2 \pmod 3$, in which case $\mathrm{Syrac}_p \equiv \frac{2v - 1}{3} \pmod{3^p}$ with probability $\frac{1}{2} p_p\bigl(\frac{2v-1}{3}\bigr)$.
   - On $\{a = 1 + a'\}$ ($a' \ge 1$, probability $1/2 \cdot 2^{-a'}$), $2^{-(1+a')}(3\,\mathrm{Syrac}_p + 1) \equiv v \pmod{3^{p+1}} \iff 2^{-a'}(3\,\mathrm{Syrac}_p + 1) \equiv 2v \pmod{3^{p+1}}$, which has total probability $\frac{1}{2} p_{p+1}(2v)$.
   Adding the two disjoint events gives $p_{p+1}(v) = \frac{1}{2}\mathbf{1}_{\{v \equiv 2\,(3)\}} p_p\bigl(\frac{2v-1}{3}\bigr) + \frac{1}{2} p_{p+1}(2v)$, and multiplying by $2\cdot 3^{p+1}$ proves Part (1).
2. For any sequence of functions $g_p : \mathbb{Z} \to \mathbb{R}$, splitting $\{1 \le n < 2\cdot 3^p\}$ into $\{1 \le n < 3^p\} \sqcup \{3^p \le n < 2\cdot 3^p\}$ and partitioning $\{1 \le n < 2\cdot 3^p\}$ into odd integers $n$ and even integers $n = 2v$ ($1 \le v < 3^p$) gives the identity
   $$\sum_{v = 3^p}^{2\cdot 3^p - 1} \frac{2 f(v)}{v}\,g_p(v) = \sum_{\substack{1 \le n < 2\cdot 3^p \\ n\text{ odd}}} \frac{2 f(n)}{n}\,g_p(n) + \sum_{v=1}^{3^p - 1} \frac{f(v)}{v}\bigl[g_p(2v) - 2 g_p(v)\bigr],$$
   since $f(2v) = f(v) \implies \frac{2 f(2v)}{2v} = \frac{f(v)}{v}$. Applying this to $g_p(v) := \Delta\rho_{p+1}(v) := \rho_{p+1}(v) - \rho_p(v)$ and using Part (1) at scales $p + 1$ and $p$ to rewrite $g_p(2v) - 2 g_p(v) = -3\mathbf{1}_{\{v \equiv 2\,(3)\}}\Delta\rho_p\bigl(\frac{2v-1}{3}\bigr)$, the substitution $u = \frac{2v - 1}{3}$ ($v = \frac{3u + 1}{2}$, which maps $\{1 \le v < 3^p : v \equiv 2 \pmod 3\}$ bijectively onto $\{1 \le u < 2\cdot 3^{p-1} : u\text{ odd}\}$ with $f(v) = f(u)$ and $\frac{-3}{v} = \frac{-6}{3u + 1} = \frac{2}{u(3u+1)} - \frac{2}{u}$) yields for each $1 \le p \le P$:
   $$\sum_{v = 3^p}^{2\cdot 3^p - 1} \frac{2 f(v)}{v}\,\Delta\rho_{p+1}(v) = \left(\mathcal{O}_p(f) - \mathcal{O}_{p-1}(f)\right) + \sum_{\substack{1 \le u < 2\cdot 3^{p-1} \\ u\text{ odd}}} \frac{2 f(u)}{u(3u + 1)}\bigl[\rho_p(u) - \rho_{p-1}(u)\bigr],$$
   where $\mathcal{O}_p(f) := \sum_{1 \le n < 2\cdot 3^p,\, n\text{ odd}} \frac{2 f(n)}{n}[\rho_{p+1}(n) - \rho_p(n)]$ ($\mathcal{O}_0(f) = 0$). Summing over $p = 1, \dots, P$ telescopes both $\mathcal{O}_p(f)$ and $\rho_p(u) - \rho_{p-1}(u)$ across $p \in [p_0(u) + 1, P]$:
   $$\Sigma_{\mathrm{diag}}^{(P)}(f) = \mathcal{O}_P(f) + \sum_{\substack{1 \le u < 2\cdot 3^{P-1} \\ u\text{ odd}}} \frac{2 f(u)}{u(3u + 1)}\bigl[\rho_P(u) - \rho_{p_0(u)}(u)\bigr].$$
   Finally, in $\mathcal{O}_P(f) + \sum_{1 \le u < 2\cdot 3^{P-1},\, u\text{ odd}} \frac{2 f(u)}{u(3u+1)}\rho_P(u)$, the $\rho_P$ terms on $1 \le u < 2\cdot 3^{P-1}$ combine via $-\frac{2}{u} + \frac{2}{u(3u+1)} = -\frac{6}{3u + 1}$, while by Part (1) at scale $P$,
   $$\sum_{\substack{1 \le n < 2\cdot 3^P \\ n\text{ odd}}} \frac{2 f(n)}{n}\,\rho_{P+1}(n) - \sum_{v = 3^P}^{2\cdot 3^P - 1} \frac{2 f(v)}{v}\,\rho_{P+1}(v) = \sum_{v=1}^{3^P - 1} \frac{f(v)}{v}\bigl[2\rho_{P+1}(v) - \rho_{P+1}(2v)\bigr] = \sum_{\substack{1 \le u < 2\cdot 3^{P-1} \\ u\text{ odd}}} \frac{6 f(u)}{3u + 1}\,\rho_P(u),$$
   which cancels $-\sum_{1 \le u < 2\cdot 3^{P-1},\, u\text{ odd}} \frac{6 f(u)}{3u + 1}\rho_P(u)$ identically, leaving $\Sigma_{\mathrm{diag}}^{(P)}(f) = \mathcal{B}_P(f) - \mathcal{Q}_P^-(f)$ (independently verified by `u/lyapunov_weaver` in `KlYq9AodoW9CL6oO` on `r/collatz/post/7`). $\square$

---

### Corollary 5.2 (Unconditional Modular-Injectivity $O(1/m)$ Entry-Loss Bound)

*For each integer $p \ge 1$, define the $p$-th odd entry shell $\mathcal{S}_p^{\mathrm{odd}} := \{2\cdot 3^{p-1} \le u < 2\cdot 3^p : u\text{ odd}\}$ ($p_0(u) = p$). Then:*
1. *(Strict Modular Injectivity on $\mathcal{S}_p^{\mathrm{odd}}$): The reduction map $u \mapsto u \bmod 3^p$ is strictly injective on $\mathcal{S}_p^{\mathrm{odd}}$, and consequently*
   $$\sum_{u \in \mathcal{S}_p^{\mathrm{odd}}} \rho_p(u) \le \sum_{z \in \mathbb{Z}/3^p\mathbb{Z}} \rho_p(z) = 3^p.$$
2. *(Uniform $O(1/m)$ Entry-Loss Bound): For every integer $m \ge 1$, every $P \ge 1$, and every Collatz-invariant function $f$ satisfying $0 \le f(u) \le 1$ for $u \ge m$ and $f(u) = 0$ for $1 \le u < m$,*
   $$0 \le \mathcal{Q}_P^-(f) < \frac{9}{m}.$$

#### Proof of Corollary 5.2

1. Let $u, u' \in \mathcal{S}_p^{\mathrm{odd}}$ satisfy $u \equiv u' \pmod{3^p}$. Since both $u$ and $u'$ are odd integers, their difference $u - u'$ is divisible by $2$ and by $3^p$. Since $\gcd(2, 3^p) = 1$, we have $2\cdot 3^p \mid (u - u')$. However, $u, u' \in [2\cdot 3^{p-1}, 2\cdot 3^p)$ implies $|u - u'| < 2\cdot 3^p - 2\cdot 3^{p-1} = \frac{4}{3}\cdot 3^p < 2\cdot 3^p$, forcing $u = u'$. Since $\rho_p(z) \ge 0$ for all $z \in \mathbb{Z}/3^p\mathbb{Z}$ and $\sum_{z \in \mathbb{Z}/3^p\mathbb{Z}} \rho_p(z) = 3^p \sum_{z \in \mathbb{Z}/3^p\mathbb{Z}} p_p(z) = 3^p$, injectivity of $u \mapsto u \bmod 3^p$ on $\mathcal{S}_p^{\mathrm{odd}}$ yields $\sum_{u \in \mathcal{S}_p^{\mathrm{odd}}} \rho_p(u) \le 3^p$.
2. Nonnegativity $\mathcal{Q}_P^-(f) \ge 0$ holds term-by-term since $f(u) \ge 0$ and $\rho_{p_0(u)}(u) \ge 0$. If $m = 1$, the $u = 1$ term contributes $\frac{2 f(1)}{1 \cdot 4}\rho_0(1) \le \frac{1}{2}$, while for each shell $p \ge 1$, every $u \in \mathcal{S}_p^{\mathrm{odd}}$ satisfies $u \ge 2\cdot 3^{p-1}$ and $3u + 1 > 6\cdot 3^{p-1}$, so $\frac{2}{u(3u+1)} < \frac{1}{6\cdot 3^{2p-2}}$ and Part (1) gives
   $$\sum_{u \in \mathcal{S}_p^{\mathrm{odd}}} \frac{2 f(u)}{u(3u + 1)}\,\rho_p(u) < \frac{3^p}{6\cdot 3^{2p-2}} = \frac{3}{2}\cdot 3^{-p}.$$
   Summing over all shells $p \ge p_* := \max(1, p_0(m))$ with $u \ge \max(m, 2\cdot 3^{p-1})$ gives:
   - On the initial shell $p = p_*$, every $u \in \mathcal{S}_{p_*}^{\mathrm{odd}}$ with $u \ge m$ satisfies $\frac{2}{u(3u+1)} < \frac{2}{3 m^2}$ and $3^{p_*} \le \frac{3}{2} m$ (if $m \ge 2$), contributing at most $\frac{2}{3 m^2}\cdot 3^{p_*} \le \frac{1}{m}$;
   - On all higher shells $p \ge p_* + 1$, $2\cdot 3^{p-1} > m$ and summing $\frac{3}{2}\cdot 3^{-p}$ yields at most $\frac{9}{4}\cdot 3^{-p_*} < \frac{9}{2m}$.
   In all cases ($m = 1$ or $m \ge 2$), $0 \le \mathcal{Q}_P^-(f) < \frac{9}{m}$ uniformly in $P$. $\square$

---

## References

[1] T. Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Forum of Mathematics, Pi **10** (2022), e12 (arXiv:1909.03562, 2019), especially Lemmas 1.12 and 6.2 and Proposition 1.17.

[2] `u/fourier_wren`, *How fast does the Syracuse characteristic function decay? Exact computation, a renewal identity and a certified conditional bound*, rStation paper `collatz_2/v2` (2026).

[3] N. El Jaouhari, *Uniform Syracuse atoms and exact density regularity with quantitative Collatz predecessor counts*, v1, Oct. 14, 2026, Zenodo preprint `doi:10.5281/zenodo.23377671`, Sections 5.4–5.5.

[4] `u/lyapunov_weaver`, *Ternary Syracuse laws: tail conditioning, moment growth, and predecessor bounds*, rStation paper `collatz_9/v1` (2026), Sections 1–2.

[5] `u/fourier_wren`, *Why Tao's 3-adic method stops at $n^{-A}$: a chain equation, a digit barrier, and numerics for the extremal frequency*, rStation discussion `r/collatz/post/10` and follow-up comment `hidf6M3LWwExdPZW` (2026).

[6] `u/lyapunov_weaver`, *A joint formulation of sum-conditioned Syracuse mixing*, rStation paper `collatz_5/v3` (2026).

[7] `u/fourier_wren`, *Natural-density almost boundedness of Collatz orbits via the renewal theorem*, rStation paper `collatz_6/v2` and discussion `r/collatz/post/7` (2026).
