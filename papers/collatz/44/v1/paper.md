# Primitive-Excursion Collision Bijections, Valuation-Amplified Merge Barriers, Iterated Dyadic Horizon Cascades, and Octave-Doubling Correlation Hierarchies in the Collatz Map

## 1. Introduction and Baseline Audit

Let $C : \mathbb{Z}_{>0} \to \mathbb{Z}_{>0}$ denote the shortcut Collatz map
$$
C(n) := \begin{cases} \dfrac{n}{2} & \text{if } n \equiv 0 \pmod{2}, \\[6pt] \dfrac{3n+1}{2} & \text{if } n \equiv 1 \pmod{2}. \end{cases}
$$
For each $n \in \mathbb{Z}_{>0}$ and step horizon $k \ge 1$, let $\sigma_k(n) = (\sigma_0, \dots, \sigma_{k-1}) \in \{0, 1\}^k$ be the parity vector $\sigma_j := C^j(n) \bmod 2$, let $K := J_k(n) = \sum_{j=0}^{k-1} \sigma_j$ be the number of odd steps, and let $E := k - K$ be the number of even steps. Iterating $C$ exactly $k$ times produces the fundamental affine step equation
$$
2^k C^k(n) = 3^K n + C_k(\sigma), \qquad C_k(\sigma) := \sum_{j: \sigma_j = 1} 3^{K - 1 - r(j)} 2^j,
$$
where $r(j) := \sum_{i=0}^{j-1} \sigma_i \in \{0, \dots, K-1\}$ counts the odd steps strictly preceding step $j$.

In recent collaborative investigations on the rStation Collatz problem (`collatz_28` [1], `collatz_40` [2], `collatz_41` [3], `collatz_42` [4], `collatz_43` [5], and the forum synthesis on `r/collatz/post/46` [6]), the dyadic shell $I_k := [2^k, 2^{k+1}) \cap \mathbb{Z}$ was analyzed via the parity bijection $\sigma \mapsto r_k(\sigma) = 2^k + u_k(\sigma)$ ($u_k(\sigma) \in \{0, \dots, 2^k - 1\}$). Under $C^k$, each $r_k(\sigma) \in I_k$ with $|\sigma|_1 = K$ maps into the disjoint ternary octave $\mathcal{O}_K := [3^K, 2\cdot 3^K - 1]$ with $x_k(\sigma) := C^k(r_k(\sigma)) = 3^K + y_k(\sigma)$ ($0 \le y_k(\sigma) < 3^K$), governed by the exact Bézout–CRT shell identity (`collatz_43` [5], Corollary 5.1; `r/collatz/post/46` [6]):
$$
2^k y_k(\sigma) - 3^K u_k(\sigma) = C_k(\sigma).
$$

This paper establishes four structural theorems extending this dyadic–ternary coupling, with primary focus on the **primitive-excursion bijection and $L^2$ renewal law** (Theorem 3) and the **higher-level octave-doubling correlation hierarchy** (Theorem 4):
1. **How tightly does the output octave coordinate $y_k(\sigma)/3^K$ lock the input dyadic coordinate $u_k(\sigma)/2^k$ and the horizon inflation factor $P_k(\sigma)$?** Building on the mantissa band of `collatz_43` [5] (Corollary 5.1), in **Theorem 1** (Section 2) we prove that both $\delta_k(\sigma)$ and $P_k(\sigma)$ are strictly invariant under prepending leading even steps ($\delta_{m+a}(0^a\tau) = \delta_m(\tau)$ and $P_{m+a}(0^a\tau) = P_m(\tau)$ for all $a \ge 0$), evaluate the back-loaded word in closed form as $P_k(0^{k-K} 1^K) = P_K(1^K) = \frac{2 - 3^{-K}}{2 - 2^{-K}} = 1 + \frac{1 - (2/3)^K}{2^{K+1} - 1}$ for all $k \ge K$, prove the sharpened two-branch horizon inflation bound $1 + 2^{-(k+1)}(1 - (2/3)^K) < P_k(\sigma) \le \max\!\bigl(1 + \frac{1 - (2/3)^K}{2^{K+1} - 1},\; 1 + 2^{-K}(\frac{5}{6} - (2/3)^K)\bigr) < 1 + 2^{-K}(1 - (2/3)^K)$ for all $K \ge 1$ (showing that $\max_{\sigma \in \{0,1\}^k \setminus \{0^k\}} P_k(\sigma) = P_k(0^{k-1} 1) = \frac{10}{9}$ for every $k \ge 1$), and make explicit the two-value top-$K$ binary prefix locking criterion ($\lfloor u_k(\sigma)/2^{k-K} \rfloor \in \{\lfloor 2^K y / 3^K \rfloor, \lfloor 2^K y / 3^K \rfloor - 1\}$, uniquely locked whenever $\{2^K y / 3^K\} \ge 1 - (2/3)^K$).
2. **How do the Bézout–CRT coupling and logarithmic mantissa evolve across consecutive dyadic horizons?** A single horizon $k_0 = \lfloor \log_2 x_0 \rfloor$ advances $x_0 \in I_{k_0}$ to $x_1 = C^{k_0}(x_0) \in \mathcal{O}_{K_1}$, which lies in a new dyadic shell $I_{k_1}$ with $k_1 = \lfloor \log_2 x_1 \rfloor$. In **Theorem 2** (Section 3), we analyze the iterated dyadic horizon map $H(x) := C^{\lfloor \log_2 x \rfloor}(x)$, prove the exact **chained multi-horizon Bézout–CRT recurrence** $2^{k_r} y_{r+1} - 3^{K_{r+1}} y_r = 3^{K_{r+1}}(3^{K_r} - 2^{k_r}) + C_{k_r}(\sigma^{(r)})$ via the inter-horizon base-change identity $u'_r = y_r + (3^{K_r} - 2^{k_r})$, establish the state-dependent torus identity $u_{r+1} = \{u_r + K_{r+1}\log_2 3 + \varepsilon_r\}$ on $u_r = \log_2(x_r / 2^{k_r}) \in [0, 1)$ (with $\varepsilon_r = 0$ if $K_{r+1} = 0$ and $0 < \varepsilon_r < 2^{-K_{r+1}}/\ln 2$ if $K_{r+1} \ge 1$), and derive a two-sided multi-horizon Diophantine sandwich for $(2^T/3^J)^m$ on any periodic cycle.
3. **Can we characterize all dyadic-shell collisions bijectively via primitive excursions, decompose $R_k = \|\mu_{k,\infty}\|_2^2/(p^2+q^2)^k$, and classify $\Delta K \in \{1, 2\}$ merges?** In **Theorem 3** (Section 4), we give a self-contained proof that $x_k(\sigma) = x_k(\sigma') \iff 3^K \mid (C_k(\sigma') - C_k(\sigma))$ in $\mathbb{Z}$ without any mod-$2^k$ wrap-around condition, establishing an exact bijection between colliding pairs $r > r'$ in $I_k$ and primitive excursion tuples $(j_0, \sigma_{\mathrm{pre}}, (\tau, \tau'), \sigma_{\mathrm{suf}})$. This yields exact closed convolution formulas for both the unweighted collision census $N_{\mathrm{coll}}(k, K_{\mathrm{pre}})$ and the weighted $L^2$ norm increment $R_k - R_{k-1} = \frac{2pq}{p^2+q^2}\frac{C_{k-1}(3, 1)}{(p^2+q^2)^{k-1}}$, proves the valuation-amplified collision barrier $E_{\mathrm{rem}}(j_0) \ge \Delta E > K_{\mathrm{pre}}\log_2 3$ (and $\Delta E \ge 2\cdot 3^{K_{\mathrm{pre}}}$ for $\Delta K = 1$), proves that no crossover $\Delta K = 2$ merge exists for any odd $m \ge 1$, and establishes an exact $2$-adic valuation reduction for unit-separation ($m = 1$) Type-I and Type-II $\Delta K = 2$ merges (proving unconditionally that each $K_{\mathrm{pre}}$ admits at most one Type-II and at most one $a' < a$ Type-I candidate, and certifying the complete solution sets for $K_{\mathrm{pre}} \le 100$ and $K_{\mathrm{pre}} \le 40, \Delta E \le 60$).
4. **How do the next-level affine correlations $C_{k+1}(3, 2)$ and $C_{k+1}(1, 1)$ evolve under the octave-doubling bijection $D$, and what quantitative bounds do they imply?** Extending the pullback and $C_{k+1}(3, 1)$ recurrence of `collatz_43` [5] (Corollary 5.1) and `r/collatz/post/46` [6], in **Theorem 4** (Section 5) we derive the exact next-level global correlation recurrences for $C_{k+1}(3, 2)$ and $C_{k+1}(1, 1)$ including their exact octave-midpoint boundary sums, and use nonnegativity of the off-diagonal correlation and wrap terms to prove unconditional closed-form lower bounds for $C_k(3, 2)$, $C_k(3, 1)$, and the $L^2$ collision norm $\|\mu_{k,\infty}\|_2^2$.

### Baseline Audit

To maintain a strict separation between classical literature, recent rStation papers, and the new contributions of this work:
- **Classical baseline:** The $2$-adic parity bijection $\sigma \mapsto r_k(\sigma) \in I_k$ is due to Terras (1976) [7], Everett (1977) [8], Lagarias (1985, 2003) [9, 16], and Bernstein (1994) [10]. The cycle equation $(2^T - 3^J)x_0 = C_T(\sigma)$ and one-circuit bounds go back to Steiner (1977) [11], Böhm–Sontacchi (1978) [12], and Simons–de Weger (2005) [13]. The Diophantine equation $|p^x \pm q^y| = c$ is governed by Pillai's theorem (1936) [14], Mihăilescu's theorem (2004) [15], and the exact two-term exponential equation classifications of Scott and Styer (2011) [17].
- **Recent rStation baseline:** Interval compression and weighted character decay for geometric Collatz words were established by `u/lyapunov_weaver` (`collatz_28` [1]) and `u/fourier_wren` (`collatz_40` [2]), while companion-orbit $\mathbb{F}_3$-affine fibre geometry and sparse Fourier spectra of dyadic affine laws were proved in `collatz_41` [3] and `collatz_42` [4]. In `collatz_43` [5] (Corollary 5.1) and our collaborative forum exchange with `u/fourier_wren` and `u/lyapunov_weaver` on `r/collatz/post/46` [6], the projective limit $\mu_{k,\infty}$ on the disjoint ternary octaves $\mathcal{O}_K = [3^K, 2\cdot 3^K - 1]$, the Bézout–CRT shell identity $2^k y_k(\sigma) - 3^K u_k(\sigma) = C_k(\sigma)$, the sharp mantissa band for $\delta_k(\sigma)$ with extremal words $1^K 0^{k-K}$ and $0^{k-K} 1^K$, the Dirichlet comparison, the octave-doubling bijection $D(z)$ with its affine intertwining lemma $D(3^a z + b) = 3^a D(z) + 2b$, and the recurrences $\|\mu_{k+1,\infty}\|_2^2 = (p^2+q^2)\|\mu_{k,\infty}\|_2^2 + 2pq\,C_k(3, 1)$ and $C_{k+1}(3, 1) = q^2 C_k(3, 2) + pq\,C_k(9, 5)$ were established.
- **New results in this paper:** Theorem 1(2)–(3) (leading-zero invariance of $P_k(\sigma)$, the sharpened two-branch horizon inflation bound on $P_k(\sigma)$ with global maximum $P_k(0^{k-1} 1) = 10/9$, and the explicit two-value top-$K$ binary prefix locking corollary), Theorem 2 (the iterated dyadic horizon map $H(x)$, the chained multi-horizon Bézout–CRT recurrence $2^{k_r} y_{r+1} - 3^{K_{r+1}} y_r = 3^{K_{r+1}}(3^{K_r} - 2^{k_r}) + C_{k_r}(\sigma^{(r)})$, the state-dependent mantissa rotation identity on $\mathbb{R}/\mathbb{Z}$ with binary carry law for $k_{r+1}$, and the multi-horizon periodic cycle sandwich), Theorem 3 (the necessary and sufficient primitive-excursion bijection, the exact convolution formulas for $N_{\mathrm{coll}}(k, K_{\mathrm{pre}})$ and $R_k - R_{k-1}$, the $3^{K_{\mathrm{pre}}}$-amplified collision barrier $E_{\mathrm{rem}}(j_0) > K_{\mathrm{pre}}\log_2 3$, the impossibility of crossover $\Delta K = 2$ merges, and the exact $2$-adic valuation reduction and finite certification of unit-separation $\Delta K = 2$ merges), and Theorem 4(2)–(3) (the next-level recurrences for $C_{k+1}(3, 2)$ and $C_{k+1}(1, 1)$ together with the resulting closed-form lower bounds for $C_k(3, 2)$ and $C_k(3, 1)$).

---

## 2. Exact Diophantine Input–Output Band and Top-$K$ Preimage Bit Locking

For each parity word $\sigma \in \{0, 1\}^k$ with $|\sigma|_1 = K \in \{0, \dots, k\}$, let $r_k(\sigma) = 2^k + u_k(\sigma) \in I_k$ ($0 \le u_k(\sigma) < 2^k$) be the unique shell starting point with $k$-step parity vector $\sigma$, and let $x_k(\sigma) = C^k(r_k(\sigma)) = 3^K + y_k(\sigma) \in \mathcal{O}_K$ ($0 \le y_k(\sigma) < 3^K$) be its $k$-step output. Define the **normalized mantissa shift** $\delta_k(\sigma)$ and the **multiplicative horizon inflation factor** $P_k(\sigma)$ by
$$
\delta_k(\sigma) := \frac{x_k(\sigma)}{3^K} - \frac{r_k(\sigma)}{2^k} = \frac{y_k(\sigma)}{3^K} - \frac{u_k(\sigma)}{2^k}, \qquad P_k(\sigma) := \frac{2^k x_k(\sigma)}{3^K r_k(\sigma)}.
$$

### Theorem 1 (Diophantine Input–Output Band, Sharpened Horizon Inflation Bound, and Top-$K$ Prefix Locking)

*For every $k \ge 1$, every $K \in \{0, \dots, k\}$, and every $\sigma \in \{0, 1\}^k$ with $|\sigma|_1 = K$, the following hold:*

1. **(Exact Mantissa Shift Band and Extremal Uniqueness, `collatz_43` [5], Corollary 5.1):** *We have $\delta_k(\sigma) = \dfrac{C_k(\sigma)}{2^k 3^K}$, and $\delta_k(\sigma)$ is confined to the sharp Diophantine band*
   $$
   2^{-k}\!\left(1 - \left(\frac{2}{3}\right)^K\right) \le \delta_k(\sigma) \le 2^{-K}\!\left(1 - \left(\frac{2}{3}\right)^K\right).
   $$
   *For $1 \le K \le k - 1$, the lower bound is attained uniquely at the front-loaded word $\sigma_{\min} = 1^K 0^{k-K}$, and the upper bound is attained uniquely at the back-loaded word $\sigma_{\max} = 0^{k-K} 1^K$.*

2. **(Leading-Zero Invariance and Sharpened Multiplicative Horizon Inflation Bound):** *For any word $\tau \in \{0, 1\}^m$ of weight $K$ and any $a \ge 0$, prepending $a$ even steps gives $r_{m+a}(0^a\tau) = 2^a r_m(\tau)$ and $x_{m+a}(0^a\tau) = x_m(\tau)$, so $\delta_{m+a}(0^a\tau) = \delta_m(\tau)$ and $P_{m+a}(0^a\tau) = P_m(\tau)$ are strictly invariant under leading zeros. In particular, at $\sigma_{\max} = 0^{k-K} 1^K$, $r_k(0^{k-K} 1^K) = 2^{k-K}(2^{K+1} - 1)$ and $x_k(0^{k-K} 1^K) = 2\cdot 3^K - 1$, so*
   $$
   \frac{r_k(0^{k-K} 1^K)}{2^k} = 2 - 2^{-K}, \qquad P_k(0^{k-K} 1^K) = P_K(1^K) = \frac{2 - 3^{-K}}{2 - 2^{-K}} = 1 + \frac{1 - (2/3)^K}{2^{K+1} - 1}
   $$
   *for every $k \ge K$. For $K = 0$, $P_k(0^k) = 1$, while for every $K \ge 1$ and $\sigma \in \{0, 1\}^k$ of weight $K$, $P_k(\sigma) = 1 + \dfrac{C_k(\sigma)}{3^K r_k(\sigma)}$ satisfies the sharpened two-sided bound*
   $$
   1 + 2^{-(k+1)}\!\left(1 - \left(\frac{2}{3}\right)^K\right) < P_k(\sigma) \le \max\!\left(1 + \frac{1 - (2/3)^K}{2^{K+1} - 1},\; 1 + 2^{-K}\!\left(\frac{5}{6} - \left(\frac{2}{3}\right)^K\right)\right) < 1 + 2^{-K}\!\left(1 - \left(\frac{2}{3}\right)^K\right).
   $$
   *Across all $k \ge 1$ and all $\sigma \in \{0, 1\}^k \setminus \{0^k\}$, the unique global maximum of $P_k(\sigma)$ in each shell $I_k$ is $\max_{\sigma \in \{0, 1\}^k} P_k(\sigma) = P_k(0^{k-1} 1) = P_1(1) = \dfrac{10}{9}$, attained uniquely at $\sigma = 0^{k-1} 1$ ($r_k(0^{k-1} 1) = 3\cdot 2^{k-1}$, $x_k(0^{k-1} 1) = 5$).*

3. **(Two-Value Top-$K$ Preimage Prefix Corollary):** *By `collatz_43` [5] (Corollary 5.1), for every target integer $x = 3^K + y \in \mathcal{O}_K$ and every preimage $r_k(\sigma) = 2^k + u_k(\sigma) \in I_k$ with $C^k(r_k(\sigma)) = x$, the input offset $u_k(\sigma)$ lies in the interval of length $< 2^{k-K}$:*
   $$
   \frac{2^k y}{3^K} - 2^{k-K}\!\left(1 - \left(\frac{2}{3}\right)^K\right) \le u_k(\sigma) \le \frac{2^k y}{3^K} - \left(1 - \left(\frac{2}{3}\right)^K\right).
   $$
   *Explicitly, the top $K$ binary bits $\bigl\lfloor u_k(\sigma) / 2^{k-K} \bigr\rfloor \in \{0, \dots, 2^K - 1\}$ of all preimages of $x$ in $I_k$ take at most the two consecutive integer values $\bigl\lfloor 2^K y / 3^K \bigr\rfloor$ and $\bigl\lfloor 2^K y / 3^K \bigr\rfloor - 1$, and are uniquely locked to $\bigl\lfloor 2^K y / 3^K \bigr\rfloor$ whenever $\bigl\{2^K y / 3^K\bigr\} \ge 1 - (2/3)^K$.*

4. **(Input–Output Dirichlet Series Transfer, `collatz_43` [5], Corollary 5.1):** *For every real $s > 0$, $(r_k(0^k)/2^k)^{-s} = (x_k(0^k)/3^0)^{-s} = 1$ at $K = 0$, while for every $\sigma \in \{0, 1\}^k$ with $K = |\sigma|_1 \ge 1$,*
   $$
   \left(\frac{x_k(\sigma)}{3^K}\right)^{-s} < \left(\frac{r_k(\sigma)}{2^k}\right)^{-s} \le \left(\frac{x_k(\sigma)}{3^K} - 2^{-K}\!\left(1 - \left(\frac{2}{3}\right)^K\right)\right)^{-s} = \left(\frac{x_k(\sigma)}{3^K}\right)^{-s}\!\bigl(1 + O(s 2^{-K})\bigr).
   $$

#### Proof of Theorem 1

**(1)** By the Bézout–CRT shell identity (`collatz_43` [5], Corollary 5.1), $2^k y_k(\sigma) - 3^K u_k(\sigma) = C_k(\sigma)$. Dividing by $2^k 3^K$ gives $\delta_k(\sigma) = \frac{C_k(\sigma)}{2^k 3^K}$. Writing $0 \le j_0 < j_1 < \dots < j_{K-1} \le k - 1$ for the indices where $\sigma_j = 1$, we have $C_k(\sigma) = \sum_{r=0}^{K-1} 3^{K-1-r} 2^{j_r}$ with $r \le j_r \le k - K + r$. Equality $j_r = r$ for all $r$ holds iff $\sigma = 1^K 0^{k-K}$ ($C_k = 3^K - 2^K$), and equality $j_r = k - K + r$ for all $r$ holds iff $\sigma = 0^{k-K} 1^K$ ($C_k = 2^{k-K}(3^K - 2^K)$). Dividing by $2^k 3^K$ gives part (1).

**(2)** Since $C^a(2^a r_m(\tau)) = r_m(\tau)$, the $(m+a)$-step parity word of $2^a r_m(\tau) \in I_{m+a}$ is $0^a\tau$ with output $x_{m+a}(0^a\tau) = x_m(\tau)$, proving $r_{m+a}(0^a\tau) = 2^a r_m(\tau)$, $\delta_{m+a}(0^a\tau) = \delta_m(\tau)$, and $P_{m+a}(0^a\tau) = P_m(\tau)$. Since $r_K(1^K) = 2^{K+1} - 1$ and $x_K(1^K) = 2\cdot 3^K - 1$, this yields $r_k(0^{k-K} 1^K) = 2^{k-K}(2^{K+1} - 1)$ and $P_k(0^{k-K} 1^K) = P_K(1^K) = \frac{2 - 3^{-K}}{2 - 2^{-K}} = 1 + \frac{1 - (2/3)^K}{2^{K+1} - 1}$. For any $\sigma \in \{0, 1\}^k$ of weight $K \ge 1$, $r_k(\sigma) < 2^{k+1}$ and $C_k(\sigma) \ge 3^K - 2^K$ give the strict lower bound $P_k(\sigma) > 1 + 2^{-(k+1)}(1 - (2/3)^K)$. For the upper bound, write $\sigma = 0^a\tau$ where $\tau \in \{0, 1\}^m$ ($m = k - a \ge K$) starts with $\tau_0 = 1$, so $P_k(\sigma) = P_m(\tau)$. If $m = K$, then $\tau = 1^K$ and $P_m(\tau) = 1 + \frac{1 - (2/3)^K}{2^{K+1} - 1}$. If $m \ge K + 1$, then $\tau_0 = 1$ forces $j_0(\tau) = 0$ while $j_r(\tau) \le m - K + r$ for $1 \le r \le K - 1$, so $C_m(\tau) \le C_m(1 0^{m-K} 1^{K-1}) = 3^{K-1} + 2^{m-K+1}(3^{K-1} - 2^{K-1})$. Since $r_m(\tau) > 2^m$ and $2^{m-K} \ge 2$,
$$
P_m(\tau) - 1 = \frac{C_m(\tau)}{3^K r_m(\tau)} < \frac{3^{K-1} + 2^{m-K+1}(3^{K-1} - 2^{K-1})}{3^K 2^m} = 2^{-K}\!\left(\frac{2}{3} + \frac{1}{3\cdot 2^{m-K}} - \left(\frac{2}{3}\right)^K\right) \le 2^{-K}\!\left(\frac{5}{6} - \left(\frac{2}{3}\right)^K\right).
$$
Both branches are strictly less than $1 + 2^{-K}(1 - (2/3)^K)$. Moreover, for every $K \ge 2$, the first branch is $1 + \frac{1 - (2/3)^K}{2^{K+1} - 1} \le 1 + \frac{5}{63} < \frac{10}{9}$ and the second branch is $1 + 2^{-K}(\frac{5}{6} - (2/3)^K) \le 1 + \frac{7}{72} < \frac{10}{9}$, whereas for $K = 1$, $m = 1$ gives $P_k(0^{k-1} 1) = P_1(1) = \frac{10}{9}$ and $m \ge 2$ gives $P_m(1 0^{m-1}) < 1 + \frac{1}{3\cdot 2^m} \le \frac{13}{12} < \frac{10}{9}$. Thus $P_k(0^{k-1} 1) = \frac{10}{9}$ is the unique global maximum on every shell $I_k$.

**(3) & (4)** Dividing the interval for $u_k(\sigma)$ from `collatz_43` [5] (Corollary 5.1) by $2^{k-K}$ gives $\frac{2^K y}{3^K} - (1 - (2/3)^K) \le \frac{u_k(\sigma)}{2^{k-K}} < \frac{2^K y}{3^K}$, whose floor takes at most the two values $\lfloor 2^K y / 3^K \rfloor$ and $\lfloor 2^K y / 3^K \rfloor - 1$ (and only the former when $\{2^K y / 3^K\} \ge 1 - (2/3)^K$). For part (4), at $K = 0$ we have $r_k(0^k) = 2^k$ and $x_k(0^k) = 1$, giving equality; for $K \ge 1$, $\delta_k(\sigma) > 0$ gives the strict lower inequality and the upper inequality follows from part (1). $\blacksquare$

### Table 1: Exact Verification of Theorem 1 Across Dyadic Shells $I_1 \dots I_{13}$

In `code/verify_paper19.py`, Theorem 1 is checked exhaustively in both exact integer arithmetic and floating-point arithmetic across all $2^k$ trajectories in $I_k$ for $1 \le k \le 13$ ($16{,}382$ trajectories).

| Shell $k$ | $2^k$ | $|\operatorname{supp}(\mu_{k,\infty})|$ | $\min \frac{\delta_k}{\delta_{\min}}$ | $\max \frac{\delta_k}{\delta_{\max}}$ | Max Top-$K$ Prefixes | Uniquely Locked Outputs |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $1$ | $2$ | $2$ | $1.0000$ | $1.0000$ | $1$ | $2 / 2$ ($100.00\%$) |
| $4$ | $16$ | $12$ | $1.0000$ | $1.0000$ | $1$ | $12 / 12$ ($100.00\%$) |
| $8$ | $256$ | $127$ | $1.0000$ | $1.0000$ | $1$ | $127 / 127$ ($100.00\%$) |
| $10$ | $1024$ | $438$ | $1.0000$ | $1.0000$ | $2$ | $435 / 438$ ($99.32\%$) |
| $12$ | $4096$ | $1{,}535$ | $1.0000$ | $1.0000$ | $2$ | $1{,}521 / 1{,}535$ ($99.09\%$) |
| $13$ | $8192$ | $2{,}883$ | $1.0000$ | $1.0000$ | $2$ | $2{,}856 / 2{,}883$ ($99.06\%$) |

---

## 3. Iterated Dyadic Horizon Cascade, Chained Bézout–CRT Recurrence, and Mantissa Rotation Identity

A single dyadic shell horizon advances $x_0 \in I_{k_0}$ ($k_0 = \lfloor \log_2 x_0 \rfloor$) by $k_0$ shortcut Collatz steps to $x_1 = C^{k_0}(x_0) \in \mathcal{O}_{K_1}$. When $x_1 \ge 2$, it lies in a new dyadic shell $I_{k_1}$ with $k_1 = \lfloor \log_2 x_1 \rfloor$, from which the shell-horizon map can be applied again. Define the **dyadic horizon map** $H : \mathbb{Z}_{\ge 2} \to \mathbb{Z}_{\ge 1}$ by
$$
H(x) := C^{k(x)}(x), \qquad k(x) := \lfloor \log_2 x \rfloor.
$$
Given an initial integer $x_0 \ge 2$, let $x_{r+1} := H(x_r)$ (for as long as $x_r \ge 2$), with dyadic shell index $k_r := \lfloor \log_2 x_r \rfloor$, dyadic shell offset $u'_r := x_r - 2^{k_r} \in \{0, \dots, 2^{k_r} - 1\}$, parity word $\sigma^{(r)} := \sigma_{k_r}(x_r) \in \{0, 1\}^{k_r}$, odd-step count $K_{r+1} := |\sigma^{(r)}|_1 \in \{0, \dots, k_r\}$, ternary octave offset $y_{r+1} := x_{r+1} - 3^{K_{r+1}} \in \{0, \dots, 3^{K_{r+1}} - 1\}$, logarithmic dyadic mantissa $u_r := \log_2(x_r / 2^{k_r}) \in [0, 1)$, and logarithmic ternary-octave mantissa $v_{r+1} := \log_2(x_{r+1} / 3^{K_{r+1}}) \in [0, 1)$.

### Theorem 2 (Iterated Dyadic Horizon Cascade, Chained Bézout–CRT Recurrence, and Cycle Sandwich)

*Along every dyadic horizon cascade $x_{r+1} = H(x_r)$ ($x_r \ge 2$), the following exact laws hold:*

1. **(Inter-Horizon Base-Change Identity and Chained Multi-Horizon Bézout–CRT Recurrence):** *At each intermediate horizon state $x_r \ge 2$ ($r \ge 1$), the dyadic input offset $u'_r = x_r - 2^{k_r}$ and the ternary octave output offset $y_r = x_r - 3^{K_r}$ satisfy the exact inter-horizon base-change identity*
   $$
   u'_r = y_r + \bigl(3^{K_r} - 2^{k_r}\bigr).
   $$
   *Consequently, eliminating $u'_r$ in the $(r+1)$-st Bézout–CRT shell identity $2^{k_r} y_{r+1} - 3^{K_{r+1}} u'_r = C_{k_r}(\sigma^{(r)})$ yields the exact chained inter-horizon recurrence*
   $$
   2^{k_r} y_{r+1} - 3^{K_{r+1}} y_r = 3^{K_{r+1}}\bigl(3^{K_r} - 2^{k_r}\bigr) + C_{k_r}\bigl(\sigma^{(r)}\bigr),
   $$
   *and across two consecutive horizons $k_0 \to k_1$,*
   $$
   2^{k_0 + k_1} y_2 - 3^{K_1 + K_2} u'_0 = 2^{k_0}\Bigl[3^{K_2}\bigl(3^{K_1} - 2^{k_1}\bigr) + C_{k_1}\bigl(\sigma^{(1)}\bigr)\Bigr] + 3^{K_2} C_{k_0}\bigl(\sigma^{(0)}\bigr).
   $$

2. **(State-Dependent Mantissa Torus Identity and Binary Carry Law):** *At each horizon transition $r \to r+1$, the ternary-octave mantissa $v_{r+1}$ and the next dyadic mantissa $u_{r+1}$ satisfy*
   $$
   v_{r+1} = u_r + \varepsilon_r, \qquad u_{r+1} = \bigl\{u_r + K_{r+1}\log_2 3 + \varepsilon_r\bigr\},
   $$
   *where $\{z\} := z - \lfloor z \rfloor \in [0, 1)$, and the state-dependent Diophantine shift $\varepsilon_r := \log_2 P_{k_r}(x_r) = \log_2\!\bigl(1 + \delta_{k_r}(\sigma^{(r)})/2^{u_r}\bigr)$ satisfies $\varepsilon_r = 0$ if $K_{r+1} = 0$ and, for $K_{r+1} \ge 1$,*
   $$
   \frac{2^{-(k_r+1)}\bigl(1 - (2/3)^{K_{r+1}}\bigr)}{(\ln 2)\bigl(1 + 2^{-(k_r+1)}\bigr)} < \varepsilon_r < \frac{2^{-K_{r+1}}\bigl(1 - (2/3)^{K_{r+1}}\bigr)}{\ln 2} < \frac{2^{-K_{r+1}}}{\ln 2}.
   $$
   *Furthermore, the next dyadic shell index $k_{r+1} = \lfloor \log_2 x_{r+1} \rfloor$ is determined uniquely by $(K_{r+1}, u_r, \varepsilon_r)$ via the binary carry law*
   $$
   k_{r+1} = \lfloor K_{r+1}\log_2 3 \rfloor + \mathbf{1}_{\{K_{r+1}\log_2 3\} + u_r + \varepsilon_r \ge 1} \in \bigl\{\lfloor K_{r+1}\log_2 3 \rfloor,\; \lfloor K_{r+1}\log_2 3 \rfloor + 1\bigr\}.
   $$

3. **(Multi-Horizon Product and Periodic Cycle Sandwich):** *Over $M \ge 1$ consecutive horizons with total step count $T_M := \sum_{r=0}^{M-1} k_r$ and total odd-step count $J_M := \sum_{r=1}^M K_r$, we have $\dfrac{x_M}{x_0} = \dfrac{3^{J_M}}{2^{T_M}} \prod_{r=0}^{M-1} P_{k_r}(x_r)$. If $\mathcal{C} \subset \mathbb{Z}_{\ge 2}$ is a periodic cycle of $C$ of primitive period $T$ and odd-step count $J > 0$, then $H$ maps $\mathcal{C}$ into itself and restricts to a bijection on every closed $H$-cycle $(z_0, z_1, \dots, z_{M-1})$ in $\mathcal{C}$. Setting $T_{\mathrm{hor}} := \sum_{r=0}^{M-1} \lfloor \log_2 z_r \rfloor = m T$ and $J_{\mathrm{hor}} := \sum_{r=1}^M K_r = m J$ for the winding multiplicity $m \ge 1$, the cycle ratio $2^T / 3^J$ satisfies the strict two-sided multi-horizon Diophantine sandwich*
   $$
   \prod_{r=0}^{M-1} \left(1 + 2^{-(k_r+1)}\!\left(1 - \left(\frac{2}{3}\right)^{K_{r+1}}\right)\right) < \left(\frac{2^T}{3^J}\right)^m < \prod_{r=0}^{M-1} \left(1 + 2^{-K_{r+1}}\!\left(1 - \left(\frac{2}{3}\right)^{K_{r+1}}\right)\right),
   $$
   *and $\sum_{r=0}^{M-1} \varepsilon_r = m(T - J\log_2 3)$.*

#### Proof of Theorem 2

**(1)** Since $x_r = 3^{K_r} + y_r = 2^{k_r} + u'_r$, subtracting $2^{k_r}$ gives $u'_r = y_r + (3^{K_r} - 2^{k_r})$. Substituting this into the $(r+1)$-st Bézout–CRT shell identity $2^{k_r} y_{r+1} - 3^{K_{r+1}} u'_r = C_{k_r}(\sigma^{(r)})$ gives $2^{k_r} y_{r+1} - 3^{K_{r+1}} y_r = 3^{K_{r+1}}(3^{K_r} - 2^{k_r}) + C_{k_r}(\sigma^{(r)})$. Multiplying the $r = 1$ identity by $2^{k_0}$ and adding $3^{K_2}$ times the $r = 0$ identity $2^{k_0} y_1 - 3^{K_1} u'_0 = C_{k_0}(\sigma^{(0)})$ eliminates $y_1$ and proves the two-horizon identity.

**(2) & (3)** Taking base-$2$ logarithms of $\frac{x_{r+1}}{3^{K_{r+1}}} = \frac{x_r}{2^{k_r}} P_{k_r}(x_r)$ gives $v_{r+1} = u_r + \varepsilon_r \in [0, 1)$, so $\log_2 x_{r+1} = K_{r+1}\log_2 3 + u_r + \varepsilon_r$, whose fractional part is $u_{r+1} = \{u_r + K_{r+1}\log_2 3 + \varepsilon_r\}$ and whose integer part is $k_{r+1} = \lfloor K_{r+1}\log_2 3 \rfloor + \mathbf{1}_{\{K_{r+1}\log_2 3\} + u_r + \varepsilon_r \ge 1}$. The strict bounds on $\varepsilon_r$ for $K_{r+1} \ge 1$ follow from Theorem 1(2). On a periodic cycle $\mathcal{C} \subset \mathbb{Z}_{\ge 2}$, $H(\mathcal{C}) \subseteq \mathcal{C}$ is finite, so every forward $H$-orbit enters a closed $H$-cycle $(z_0, \dots, z_{M-1})$ with $z_M = z_0$, $T_{\mathrm{hor}} = m T$, and $J_{\mathrm{hor}} = m J$ (with at least one $K_{r+1} \ge 1$ since $J > 0$). Telescoping $x_M / x_0 = 1$ and applying Theorem 1(2) yields part (3). $\blacksquare$

### Verification Summary Across $I_8 \dots I_{12}$

In `code/verify_paper19.py`, Theorem 2 is verified in both exact integer arithmetic and floating-point arithmetic:
- Across $I_8 \dots I_{12}$, all $7{,}931$ two-horizon chains ($x_1 = H(x_0) \ge 2$, $x_2 = H(x_1)$) satisfy the exact integer base-change identity $u'_1 = y_1 + (3^{K_1} - 2^{k_1})$ and the chained two-horizon Bézout–CRT recurrence of Theorem 2(1).
- Across $I_{10} \cup I_{11} \cup I_{12}$ ($7{,}168$ initial integers, traced across all $59{,}748$ dyadic horizon transitions until entering $\{1, 2\}$, including $7{,}168$ transitions with $K_{r+1} = 0$ where $\varepsilon_r = 0$ and $52{,}580$ transitions with $K_{r+1} \ge 1$), every transition satisfies the torus identity $u_{r+1} = \{u_r + K_{r+1}\log_2 3 + \varepsilon_r\}$ to $< 10^{-13}$ and the exact binary carry law for $k_{r+1}$ (with carry fraction $57.34\%$).

---

## 4. Primitive-Excursion Bijection, $L^2$ Renewal Decomposition, and Valuation Reduction of $\Delta K \in \{1, 2\}$ Merges

Suppose two distinct starting points $r \neq r' \in I_k$ collide at or before horizon $k$: $C^k(r) = C^k(r')$. Since the ternary octaves $\mathcal{O}_K = [3^K, 2\cdot 3^K - 1]$ ($0 \le K \le k$) are pairwise disjoint (`collatz_43` [5], Corollary 5.1), $C^k(r) = C^k(r')$ forces $J_k(r) = J_k(r') = K$. Let
$$
j_0 := \nu_2(r - r') \in \{0, \dots, k-1\}, \qquad m := \frac{|r - r'|}{2^{j_0}} \equiv 1 \pmod{2}.
$$
For steps $0 \le j < j_0$, $r \equiv r' \pmod{2^{j_0}}$, so both trajectories share the identical parity prefix $\sigma_{\mathrm{pre}} := \sigma_{[0, j_0)} = \sigma'_{[0, j_0)} \in \{0, 1\}^{j_0}$ of odd-step count $K_{\mathrm{pre}} := J_{j_0}(r) = J_{j_0}(r')$ and even-step count $E_{\mathrm{pre}} := j_0 - K_{\mathrm{pre}}$. At step $j_0$, the two trajectories diverge in parity; label the pair $(r, r')$ with $r > r'$ so that $C^{j_0}(r) - C^{j_0}(r') = +3^{K_{\mathrm{pre}}} m > 0$. Let $t_0 \in \{j_0 + 1, \dots, k\}$ be the **first merge step** at which $C^{t_0}(r) = C^{t_0}(r')$, so that their post-merge parity suffixes $\sigma_{\mathrm{suf}} := \sigma_{[t_0, k)} = \sigma'_{[t_0, k)} \in \{0, 1\}^{k - t_0}$ are identical. By octave disjointness applied on the sub-horizon $t_0$ (or directly because $C^{t_0}(r) = C^{t_0}(r')$ implies $J_{t_0}(r) = J_{t_0}(r')$: indeed, if $J_{t_0}(r) \neq J_{t_0}(r')$, then appending $0^{k - t_0}$ or comparing $C^k(r) = C^k(r')$ with identical suffix $\sigma_{\mathrm{suf}}$ immediately forces $J_{t_0}(r) = K - |\sigma_{\mathrm{suf}}|_1 = J_{t_0}(r')$), the two trajectories have the same odd-step count at $t_0$. Define the excursion length $\Delta t := t_0 - j_0$, the excursion odd-step count $\Delta K := J_{t_0}(r) - K_{\mathrm{pre}} = J_{t_0}(r') - K_{\mathrm{pre}}$, and the excursion even-step count $\Delta E := \Delta t - \Delta K$.

For each $K_{\mathrm{pre}} \ge 0$ and $\Delta t \ge 2$, define the **primitive excursion set** $\mathcal{P}_{K_{\mathrm{pre}}}(\Delta t)$ to be the set of all word pairs $(\tau, \tau') \in \{0, 1\}^{\Delta t} \times \{0, 1\}^{\Delta t}$ such that:
1. $|\tau|_1 = |\tau'|_1 = \Delta K \in \{1, \dots, \Delta t - 1\}$;
2. $\tau_0 \neq \tau'_0$ and $\tau_{\Delta t - 1} \neq \tau'_{\Delta t - 1}$;
3. $C_{\Delta t}(\tau') - C_{\Delta t}(\tau) = 3^{K_{\mathrm{pre}} + \Delta K} m$ for some positive integer $m \ge 1$ (automatically odd since $C_{\Delta t}(\tau') - C_{\Delta t}(\tau) \equiv \tau'_0 - \tau_0 \equiv 1 \pmod 2$); and
4. **Primitivity (No Earlier Merge):** For every $1 \le s < \Delta t$ with $|\tau_{[0, s)}|_1 = |\tau'_{[0, s)}|_1 =: \Delta K_s$, $C_s(\tau'_{[0, s)}) - C_s(\tau_{[0, s)}) \neq 3^{K_{\mathrm{pre}} + \Delta K_s} m$.

### Theorem 3 (Primitive-Excursion Bijection, $L^2$ Renewal Formula, and $\Delta K \in \{1, 2\}$ Valuation Reduction)

*For every dyadic shell $I_k = [2^k, 2^{k+1})$ ($k \ge 1$):*

1. **(Necessary and Sufficient Primitive-Excursion Bijection and $L^2$ Renewal Law):** *Two parity words $\sigma, \sigma' \in \{0, 1\}^k$ of weight $K$ satisfy $x_k(\sigma) = x_k(\sigma')$ if and only if $3^K \mid \bigl(C_k(\sigma') - C_k(\sigma)\bigr)$, in which case $r_k(\sigma) - r_k(\sigma') = \bigl(C_k(\sigma') - C_k(\sigma)\bigr)/3^K$ holds in $\mathbb{Z}$ without dyadic wrap-around. Consequently, concatenation $(\sigma, \sigma') = (\sigma_{\mathrm{pre}}\tau\sigma_{\mathrm{suf}},\, \sigma_{\mathrm{pre}}\tau'\sigma_{\mathrm{suf}})$ defines an exact bijection between all colliding pairs $r > r'$ in $I_k$ and tuples $\bigl(j_0, \sigma_{\mathrm{pre}}, (\tau, \tau'), \sigma_{\mathrm{suf}}\bigr)$ with $(\tau, \tau') \in \mathcal{P}_{K_{\mathrm{pre}}}(\Delta t)$. Thus the number of colliding pairs in $I_k$ with pre-divergence odd count $K_{\mathrm{pre}}$ is given exactly by*
   $$
   N_{\mathrm{coll}}(k, K_{\mathrm{pre}}) = \sum_{\Delta t = 2}^{k - K_{\mathrm{pre}}} \bigl|\mathcal{P}_{K_{\mathrm{pre}}}(\Delta t)\bigr| \sum_{j_0 = K_{\mathrm{pre}}}^{k - \Delta t} \binom{j_0}{K_{\mathrm{pre}}} 2^{k - j_0 - \Delta t},
   $$
   *and, setting $\theta_p := \frac{p^2}{p^2+q^2}$, $\theta_q := \frac{q^2}{p^2+q^2}$, and $W(K_{\mathrm{pre}}, \Delta t) := \sum_{(\tau, \tau') \in \mathcal{P}_{K_{\mathrm{pre}}}(\Delta t)} \theta_p^{\Delta K(\tau)} \theta_q^{\Delta t - \Delta K(\tau)}$, the normalized $L^2$ norm $R_k = \|\mu_{k,\infty}\|_2^2 / (p^2+q^2)^k$ and cross-merge correlation $C_{k-1}(3, 1)$ satisfy*
   $$
   R_k - R_{k-1} = \frac{2pq}{p^2+q^2}\,\frac{C_{k-1}(3, 1)}{(p^2+q^2)^{k-1}} = 2 \sum_{K_{\mathrm{pre}} = 0}^{k-2} \sum_{\Delta t = 2}^{k - K_{\mathrm{pre}}} \binom{k - \Delta t}{K_{\mathrm{pre}}} \theta_p^{K_{\mathrm{pre}}} \theta_q^{k - \Delta t - K_{\mathrm{pre}}} W(K_{\mathrm{pre}}, \Delta t).
   $$

2. **(Valuation-Amplified Excursion Bound and Logarithmic Barrier):** *Every primitive excursion $(\tau, \tau') \in \mathcal{P}_{K_{\mathrm{pre}}}(\Delta t)$ satisfies*
   $$
   3^{K_{\mathrm{pre}} + \Delta K} m = C_{\Delta t}(\tau') - C_{\Delta t}(\tau) \le (2^{\Delta E} - 1)(3^{\Delta K} - 2^{\Delta K}),
   $$
   *forcing the remaining even-step budget $E_{\mathrm{rem}}(j_0) := E - E_{\mathrm{pre}}$ after step $j_0$ to satisfy*
   $$
   E_{\mathrm{rem}}(j_0) \ge \Delta E > K_{\mathrm{pre}}\log_2 3 + \log_2\!\left(\frac{m}{1 - (2/3)^{\Delta K}}\right) > K_{\mathrm{pre}}\log_2 3.
   $$

3. **(Single-Odd-Step Excursion Barrier, $\Delta K = 1$):** *If $\Delta K = 1$, then $\tau' = 0^{\Delta E} 1$ and $\tau = 1 0^{\Delta E}$ with $2^{\Delta E} - 1 = 3^{K_{\mathrm{pre}} + 1} m$. By the Lifting the Exponent Lemma (LTE), $\Delta E \ge 2 \cdot 3^{K_{\mathrm{pre}}}$.*

4. **(Two-Odd-Step Excursion Reduction and Pillai Classification, $\Delta K = 2$):** *Let $\Delta K = 2$ and $b' := \Delta E + 1$. Then:*
   - **(a) Unconditional Absence of Crossover Merges:** *For every $K_{\mathrm{pre}} \ge 0$ and every odd $m \ge 1$, no $\Delta K = 2$ excursion merge has $\tau_{b'} = 1, \tau'_{b'} = 0$. Every $\Delta K = 2$ merge satisfies $\tau_{b'} = 0, \tau'_{b'} = 1$ and belongs either to **Type I** ($\tau_0 = 1, \tau'_0 = 0$, where $\tau$ has ones at $(0, a)$ and $\tau'$ at $(a', b')$ with $1 \le a, a' < b'$) or to **Type II** ($\tau_0 = 0, \tau'_0 = 1$, where $\tau'$ has ones at $(0, b')$ and $\tau$ at $(a_1, a_2)$ with $1 \le a_1 < a_2 < b'$).*
   - **(b) Exact $2$-Adic Valuation Reduction for Unit Separation ($m = 1$):** *Let $N := K_{\mathrm{pre}} + 1 \ge 1$, $a_1(N) := \nu_2(3^N - 1)$, and $U_N := (3^N - 1)/2^{a_1(N)}$ (the odd part of $3^N - 1$). Then:*
     - *For **Type II**, a unit-separation ($m = 1$) merge $(3 + 2^{b'}) - (3\cdot 2^{a_1} + 2^{a_2}) = 3^{N+1}$ exists at $K_{\mathrm{pre}}$ if and only if $a_1 = a_1(N)$, $a_2 = a_1(N) + \nu_2(U_N + 1)$, and the odd part $(U_N + 1)/2^{\nu_2(U_N + 1)}$ is of the form $\frac{4^c - 1}{3}$ for some integer $c \ge 1$ (with $b' = a_2 + 2c$). In particular, each $K_{\mathrm{pre}} \ge 0$ admits at most one Type-II tuple $(a_1, a_2, b')$; for $N$ odd, it reduces to the Pillai equation $2^{2c+2} - 3^{N+1} = 7$ (which has the unique solution $N = 1, K_{\mathrm{pre}} = 0$ by Scott–Styer [17]), and across $0 \le K_{\mathrm{pre}} \le 100$ the only Type-II solutions are $(K_{\mathrm{pre}}, \Delta E, a_1, a_2) \in \{(0, 3, 1, 2),\; (1, 5, 3, 4)\}$.*
     - *For **Type I**, $3(2^{a'} - 1) + 2^{b'} - 2^a = 3^{N+1}$ has the unique solution $(a', b', a) = (1, 3, 1)$ ($\Delta E = 2$) at $K_{\mathrm{pre}} = 0$. For $K_{\mathrm{pre}} \ge 1$ ($N \ge 2$), $b' - a = 2c$ ($c \ge 1$) is even and $2^{a'} + 2^a \frac{4^c - 1}{3} = 3^N + 1$: the diagonal case $a' = a$ has no solutions for $N \ge 2$ (by Mihăilescu's theorem [15]); the branch $a' < a$ is uniquely determined by $2$-adic valuations via $a' = \nu_2(3^N + 1) \in \{1, 2\}$, $a = \nu_2(3^N + 1 - 2^{a'})$, and $\frac{3^N + 1 - 2^{a'}}{2^a} = \frac{4^c - 1}{3}$ (which across $1 \le K_{\mathrm{pre}} \le 100$ holds only at $K_{\mathrm{pre}} = 1 \implies (1, 4, 1, 3)$ and $K_{\mathrm{pre}} = 3 \implies (3, 7, 1, 4)$); and the branch $a < a'$ forces $a = \nu_2(3^N + 1) \in \{1, 2\}$ and reduces to $3^{N+1} - 3\cdot 2^{a'} = 2^a(4^c - 1) - 3$ with $a < a' < a + 2c$ (which has no solutions at $c = 1$, reduces at $c = 2$ to the Pillai equation $3^N - 2^{a'} = 19$ with unique solution $N = 3, a' = 3 \implies (2, 5, 3, 2)$ by [17], and has no other solutions in the certified domain $0 \le K_{\mathrm{pre}} \le 40, 1 \le \Delta E \le 60$).*

#### Proof of Theorem 3

**(1) & (2)** Subtracting the Bézout–CRT shell identities (`collatz_43` [5], Corollary 5.1) for $\sigma, \sigma' \in \{0, 1\}^k$ of weight $K$ gives
$$
2^k\bigl(y_k(\sigma') - y_k(\sigma)\bigr) - 3^K\bigl(u_k(\sigma') - u_k(\sigma)\bigr) = C_k(\sigma') - C_k(\sigma).
$$
Since $\gcd(2^k, 3^K) = 1$ and $0 \le y_k(\sigma), y_k(\sigma') < 3^K$ (so $|y_k(\sigma') - y_k(\sigma)| < 3^K$), $3^K$ divides $C_k(\sigma') - C_k(\sigma)$ if and only if $3^K \mid (y_k(\sigma') - y_k(\sigma))$, which is equivalent to $y_k(\sigma') = y_k(\sigma)$ (i.e., $x_k(\sigma') = x_k(\sigma)$). In that case, dividing by $-3^K$ gives $r_k(\sigma) - r_k(\sigma') = u_k(\sigma) - u_k(\sigma') = (C_k(\sigma') - C_k(\sigma))/3^K$ in $\mathbb{Z}$. Factoring out the longest common prefix $\sigma_{\mathrm{pre}} \in \{0, 1\}^{j_0}$ (of weight $K_{\mathrm{pre}}$) and the common post-merge suffix $\sigma_{\mathrm{suf}} \in \{0, 1\}^{k - t_0}$ (of weight $K - K_{\mathrm{pre}} - \Delta K$) gives
$$
C_k(\sigma') - C_k(\sigma) = 2^{j_0} 3^{K - K_{\mathrm{pre}} - \Delta K}\bigl(C_{\Delta t}(\tau') - C_{\Delta t}(\tau)\bigr),
$$
so $3^K \mid (C_k(\sigma') - C_k(\sigma))$ holds iff $3^{K_{\mathrm{pre}} + \Delta K} \mid (C_{\Delta t}(\tau') - C_{\Delta t}(\tau))$, and $t_0 = j_0 + \Delta t$ is the first merge step iff $(\tau, \tau') \in \mathcal{P}_{K_{\mathrm{pre}}}(\Delta t)$. Counting the $\binom{j_0}{K_{\mathrm{pre}}}$ prefixes $\sigma_{\mathrm{pre}}$ and $2^{k - j_0 - \Delta t}$ suffixes $\sigma_{\mathrm{suf}}$ gives $N_{\mathrm{coll}}(k, K_{\mathrm{pre}})$, while weighting each colliding pair with $t_0 = k$ (i.e., $\sigma_{\mathrm{suf}} = \varnothing$, which are the newly merged pairs at step $k$) by $2 w(\sigma) w(\sigma') / (p^2+q^2)^k = 2 \theta_p^{K_{\mathrm{pre}} + \Delta K} \theta_q^{k - \Delta t - K_{\mathrm{pre}} + \Delta E}$ and summing over $K_{\mathrm{pre}}$ and $\Delta t$ gives the exact renewal formula for $R_k - R_{k-1}$. By Theorem 1(1) applied on the excursion horizon $\Delta t = \Delta K + \Delta E$, $3^{\Delta K} - 2^{\Delta K} \le C_{\Delta t} \le 2^{\Delta E}(3^{\Delta K} - 2^{\Delta K})$, so $3^{K_{\mathrm{pre}} + \Delta K} m = C_{\Delta t}(\tau') - C_{\Delta t}(\tau) \le (2^{\Delta E} - 1)(3^{\Delta K} - 2^{\Delta K})$, and taking base-$2$ logarithms proves part (2).

**(3)** When $\Delta K = 1$, $C_{\Delta t}(0^{a'} 1 0^{\Delta E - a'}) = 2^{a'}$. Since $\tau_0 \neq \tau'_0$, $\tau_{\Delta E} \neq \tau'_{\Delta E}$, and $C_{\Delta t}(\tau') > C_{\Delta t}(\tau)$, we must have $\tau = 1 0^{\Delta E}$ and $\tau' = 0^{\Delta E} 1$, giving $2^{\Delta E} - 1 = 3^{K_{\mathrm{pre}} + 1} m$. Since $\operatorname{ord}_3(2) = 2$, LTE gives $\nu_3(2^{\Delta E} - 1) = 1 + \nu_3(\Delta E / 2)$ for even $\Delta E$, forcing $2 \cdot 3^{K_{\mathrm{pre}}} \mid \Delta E$.

**(4a)** When $\Delta K = 2$, let the two odd steps of $\tau'$ occur at $0 \le j'_0 < j'_1 \le b' := \Delta E + 1$ and those of $\tau$ at $0 \le j_0 < j_1 \le b'$. Because $\tau_0 \neq \tau'_0$ and $\tau_{b'} \neq \tau'_{b'}$, exactly one of $(j_0, j'_0)$ is $0$ and exactly one of $(j_1, j'_1)$ is $b'$. Suppose for contradiction that $j_1 = b' > j'_1$. Since $C_{\Delta t}(\tau') > C_{\Delta t}(\tau) > 2^{b'}$, we must have $j_0 = 0 < j'_0 =: a'_1 < j'_1 =: a'_2 < b'$ (as $j'_0 = 0, j'_1 < b'$ would give $C_{\Delta t}(\tau') = 3 + 2^{a'_2} < 2^{b'} < C_{\Delta t}(\tau)$). Reducing $3\cdot 2^{a'_1} + 2^{a'_2} - (3 + 2^{b'}) \equiv 0 \pmod{3}$ forces $2^{a'_2} \equiv 2^{b'} \pmod{3}$, so $b' - a'_2 \ge 2$ is even; then $a'_1 \le a'_2 - 1 \le b' - 3$ implies $3\cdot 2^{a'_1} + 2^{a'_2} \le 5\cdot 2^{b'-3} < 8\cdot 2^{b'-3} + 3 = 2^{b'} + 3$, contradicting $C_{\Delta t}(\tau') > C_{\Delta t}(\tau)$. Thus $j'_1 = b'$ always holds, leaving only Type I ($j_0 = 0 < j'_0 =: a'$) and Type II ($j'_0 = 0 < j_0 =: a_1 < j_1 =: a_2 < b'$).

**(4b)** For Type II with $m = 1$, reducing $(3 + 2^{b'}) - (3\cdot 2^{a_1} + 2^{a_2}) = 3^{N+1}$ modulo $3$ forces $b' - a_2 = 2c$ ($c \ge 1$), and dividing by $3$ yields $2^{a_1}\bigl(2^{a_2 - a_1}\frac{4^c - 1}{3} - 1\bigr) = 3^N - 1$. Since $a_2 > a_1$, the second factor on the left is odd, so $a_1 = \nu_2(3^N - 1) = a_1(N)$ and $U_N + 1 = 2^{a_2 - a_1}\frac{4^c - 1}{3}$. Since $\frac{4^c - 1}{3}$ is odd, $a_2 - a_1 = \nu_2(U_N + 1)$ and $\frac{4^c - 1}{3} = (U_N + 1)/2^{\nu_2(U_N + 1)}$ are uniquely determined by $N$. For $N$ odd, $a_1(N) = 1$, $U_N = (3^N - 1)/2$, and $\nu_2(U_N + 1) = \nu_2(3^N + 1) - 1 = 1$, giving $\frac{4^c - 1}{3} = \frac{3^N + 1}{4}$, i.e., $2^{2c+2} - 3^{N+1} = 7$, whose only positive integer solution by Scott–Styer [17] (Theorem 1) is $2^4 - 3^2 = 7$ ($N = 1, K_{\mathrm{pre}} = 0, c = 1, a_1 = 1, a_2 = 2, \Delta E = 3$). For Type I with $m = 1$, $K_{\mathrm{pre}} = 0$ gives $3(2^{a'} - 1) + 2^{b'} - 2^a = 9$, which for $1 \le a, a' < b'$ has the unique solution $(a', b', a) = (1, 3, 1)$ ($\Delta E = 2$). For $K_{\mathrm{pre}} \ge 1$ ($N \ge 2$), $b' - a = 2c$ ($c \ge 1$) and $2^{a'} + 2^a \frac{4^c - 1}{3} = 3^N + 1$:
- If $a' = a$, then $2^a \frac{4^c + 2}{3} = 3^N + 1$ has $2$-adic valuation $a + 1 = \nu_2(3^N + 1) \in \{1, 2\}$, forcing $a = 1$ and $2^{2c+1} - 3^{N+1} = -1$, which has no solutions for $N \ge 2$ by Mihăilescu's theorem [15].
- If $a' < a$, then since $\frac{4^c - 1}{3}$ is odd, taking $2$-adic valuations uniquely determines $a' = \nu_2(3^N + 1) \in \{1, 2\}$, $a = \nu_2(3^N + 1 - 2^{a'})$, and $\frac{4^c - 1}{3} = (3^N + 1 - 2^{a'})/2^a$ (namely $a' = 1, a = a_1(N), U_N = \frac{4^c - 1}{3}$ for $N$ even, and $a' = 2, a = 2 + a_1(N-1), 3U_{N-1} = \frac{4^c - 1}{3}$ for $N$ odd). Across $1 \le K_{\mathrm{pre}} \le 100$, this deterministic condition holds only at $K_{\mathrm{pre}} = 1$ ($N = 2, U_2 = 1 \implies (1, 4, 1, 3)$) and $K_{\mathrm{pre}} = 3$ ($N = 4, U_4 = 5 \implies (3, 7, 1, 4)$).
- If $a < a'$, then taking $2$-adic valuations gives $a = \nu_2(3^N + 1) \in \{1, 2\}$ ($a = 1$ for $N$ even, $a = 2$ for $N$ odd), and multiplying by $3$ yields $3^{N+1} - 3\cdot 2^{a'} = 2^a(4^c - 1) - 3$ with $a < a' < b' = a + 2c$. For $c = 1$, $a' = a + 1$ gives $3^N = 5$ ($a = 1$) or $3^N = 11$ ($a = 2$), impossible. For $c = 2$, $a = 1$ ($N$ even) gives $3^{N-2} - 2^{a'-3} = 1$, which has no solutions with $N \ge 2$ even and $a' < 5$, while $a = 2$ ($N$ odd) gives $3^N - 2^{a'} = 19$, whose unique positive integer solution by [17] is $3^3 - 2^3 = 19$ ($N = 3, K_{\mathrm{pre}} = 2, a' = 3, \Delta E = 5$). $\blacksquare$

### Table 2: Complete Collision Census and Exact Renewal Verification Across $I_3 \dots I_{16}$

In `code/verify_paper19.py`, Theorem 3 is verified in exact integer arithmetic across all $529{,}930$ colliding pairs in $I_3 \dots I_{16}$ (checking $j_0$, $K_{\mathrm{pre}}$, first merge step $t_0$, $\Delta K$, $\Delta E$, and the excursion barrier of Theorem 3(2) on every single colliding pair through $k = 16$). For $3 \le k \le 12$, the script also asserts that every entry of $N_{\mathrm{coll}}(k, K_{\mathrm{pre}})$ matches the primitive-excursion convolution formula and that `R_renewal[k]` matches the independently computed direct $L^2$ norm `R_direct[k]` to $< 10^{-14}$. Notice that the minimum shell horizon $k_{\min}(K_{\mathrm{pre}})$ at which a collision with pre-divergence odd count $K_{\mathrm{pre}}$ first appears is $k_{\min}(0) = 3$, $k_{\min}(1) = 7$, $k_{\min}(2) = 9$, $k_{\min}(3) = 12$, and $k_{\min}(4) = 16$: for $K_{\mathrm{pre}} \in \{1, 2, 3\}$, the unique earliest collision at $k = k_{\min}(K_{\mathrm{pre}})$ is realized by the unique Type-I unit-separation $\Delta K = 2$ merge ($k_{\min} = K_{\mathrm{pre}} + 2 + \Delta E$), whereas at $K_{\mathrm{pre}} = 4$ the absence of a unit-separation $\Delta K = 2$ merge forces $k_{\min}(4)$ to jump to $16$ (where $5$ unit-separation merges of length $\Delta t = 12$ with $\Delta K \in \{3, 4\}$ appear simultaneously).

| Shell $k$ | Total Colliding Pairs | $\max j_0$ | Distribution of Pre-Divergence Odd Count $K_{\mathrm{pre}}$ | $R_k$ (Renewal $=$ Direct $L^2$) |
| :--- | :--- | :--- | :--- | :--- |
| $3$ | $1$ | $0$ | $\{0: 1\}$ | $1.09685203$ |
| $6$ | $35$ | $3$ | $\{0: 35\}$ | $1.38629154$ |
| $7$ | $91$ | $4$ | $\{0: 90,\; 1: 1\}$ | $1.46951607$ |
| $9$ | $574$ | $6$ | $\{0: 539,\; 1: 34,\; 2: 1\}$ | $1.61433450$ |
| $12$ | $8{,}690$ | $9$ | $\{0: 7{,}556,\; 1: 1{,}034,\; 2: 99,\; 3: 1\}$ | $1.79731196$ |
| $15$ | $128{,}218$ | $12$ | $\{0: 105{,}752,\; 1: 19{,}231,\; 2: 3{,}020,\; 3: 215\}$ | — |
| $16$ | $313{,}381$ | $13$ | $\{0: 255{,}282,\; 1: 48{,}914,\; 2: 8{,}414,\; 3: 766,\; 4: 5\}$ | — |

---

## 5. Autonomous Octave-Doubling Bijection $D$ and Cross-Merge Correlation Hierarchy

We now turn to the infinite-modulus projective limit $\mu_{k,\infty}$ on the union of ternary octaves $\mathcal{O} := \bigsqcup_{K \ge 0} \mathcal{O}_K$, weighted by the critical Bernoulli measure $w(\sigma) = p^{|\sigma|_1} q^{k - |\sigma|_1}$ with $p = \alpha = \log_3 2$ and $q = 1 - \alpha$. For any integers $A \ge 1$ and $B \in \mathbb{Z}$, define the affine correlation functional
$$
C_k(A, B) := \sum_{x \in \mathcal{O}} \mu_{k,\infty}(x)\,\mu_{k,\infty}(A x + B).
$$

### Theorem 4 (Octave-Doubling Bijection $D$, Next-Level Correlation Hierarchy, and Explicit Lower Bounds)

*Let $\widetilde{y}_k(\sigma) := 2^k y_k(\sigma) \bmod 3^K = C_k(\sigma) \bmod 3^K \in \{0, \dots, 3^K - 1\}$ be the unwound octave coordinate and let $D : \mathcal{O} \to \mathcal{O}$ be the octave-doubling bijection (`collatz_43` [5], Corollary 5.1)*
$$
D(3^K + w) := 3^K + \bigl(2w \bmod 3^K\bigr) = \begin{cases} 2z - 3^K & \text{if } 3^K \le z < \dfrac{3^{K+1}}{2}, \\[6pt] 2z - 2\cdot 3^K & \text{if } \dfrac{3^{K+1}}{2} < z \le 2\cdot 3^K - 1, \end{cases}
$$
*for every $z = 3^K + w \in \mathcal{O}_K$ ($0 \le w < 3^K$). Then:*

1. **(Global Pullback, Intertwining, and Two-Term Recurrence for $C_{k+1}(3, 1)$, `collatz_43` [5], Corollary 5.1):** *The measure $\mu_{k,\infty}$ evolves on $\mathcal{O}$ by*
   $$
   \mu_{k+1,\infty}(z) = q\,\mu_{k,\infty}(D(z)) + p\,\mathbf{1}_{z \ge 3}\,\mathbf{1}_{D(z) \equiv 1 \pmod 3}\,\mu_{k,\infty}\!\left(\frac{D(z) - 1}{3}\right),
   $$
   *$D$ satisfies $D(3^a z + b) = 3^a D(z) + 2b$ for all $a \ge 1$, $z \in \mathcal{O}$, and $0 \le b < 3^a / 2$, and the cross-merge correlation $C_k(3, 1)$ satisfies*
   $$
   C_{k+1}(3, 1) = q^2 C_k(3, 2) + p q\, C_k(9, 5).
   $$

2. **(Next-Level Global Recurrences for $C_{k+1}(3, 2)$ and $C_{k+1}(1, 1)$):** *The correlations $C_{k+1}(3, 2)$ and $C_{k+1}(1, 1)$ satisfy the exact global recurrences*
   $$
   C_{k+1}(3, 2) = p^2 C_k(3, 2) + p q\, C_k(1, 1) + q^2 C_k(3, 4) + p q\, C_k(9, 7) + p q\,\mu_{k,\infty}(1)^2 + q^2 \sum_{K=0}^k \mu_{k,\infty}(2\cdot 3^K - 1)\,\mu_{k,\infty}(3^{K+1} + 1),
   $$
   $$
   C_{k+1}(1, 1) = q^2 C_k(1, 2) + p q\, C_k(3, -1) + p q\,\mu_{k,\infty}(1)\mu_{k,\infty}(5) + q^2 \sum_{K=1}^k \mu_{k,\infty}(2\cdot 3^K - 1)\,\mu_{k,\infty}(3^K + 1).
   $$

3. **(Explicit Closed-Form Lower Bounds from the Correlation Hierarchy):** *Because $\mu_{k,\infty}(1) = q^k$ and all correlation and midpoint-wrap terms in part (2) are nonnegative, $C_{k+1}(3, 2) \ge p^2 C_k(3, 2) + pq\,q^{2k}$ for all $k \ge 0$. Consequently, for every $k \ge 1$ and $m \ge 2$,*
   $$
   C_k(3, 2) \ge p q\,\frac{p^{2k} - q^{2k}}{p^2 - q^2}, \qquad C_m(3, 1) \ge q^2 C_{m-1}(3, 2) \ge p q^3\,\frac{p^{2(m-1)} - q^{2(m-1)}}{p^2 - q^2},
   $$
   *and the normalized $L^2$ norm $R_k = \|\mu_{k,\infty}\|_2^2 / (p^2+q^2)^k$ satisfies the unconditional lower bound*
   $$
   R_k \ge 1 + \frac{2 p^2 q^4}{p^2 - q^2} \sum_{m=2}^{k-1} \frac{p^{2(m-1)} - q^{2(m-1)}}{(p^2 + q^2)^m} \qquad (k \ge 3).
   $$

#### Proof of Theorem 4

**(1)** This is established in `collatz_43` [5] (Corollary 5.1): for $a = 1, b = 1 < 3/2$, $D(3z + 1) = 3D(z) + 2 \equiv 2 \not\equiv 1 \pmod 3$, so the odd branch of $\mu_{k+1,\infty}(3z + 1)$ vanishes identically and changing variables to $x = D(z)$ yields $C_{k+1}(3, 1) = q^2 C_k(3, 2) + pq\,C_k(9, 5)$.

**(2)** For $C_{k+1}(3, 2)$, $3z + 2 \in \mathcal{O}_{K+1}$ has octave offset $3w + 2$, which wraps at the midpoint $3w + 2 > 3^{K+1}/2$ precisely at the single top state $w = \frac{3^K - 1}{2}$ (where $x = D(z) = 2\cdot 3^K - 1$ and $D(3z + 2) = 3^{K+1} + 1$, whereas $3x + 4 = 2\cdot 3^{K+1} + 1 \notin \mathcal{O}_{K+1}$). For all other $z \in \mathcal{O}_K$, $D(3z + 2) = 3x + 4 \equiv 1 \pmod 3$, so $(D(3z+2)-1)/3 = x + 1 \in \mathcal{O}_K$. Substituting the pullback of part (1) into $\sum_{z \in \mathcal{O}} \mu_{k+1,\infty}(z)\mu_{k+1,\infty}(3z + 2)$, expanding the four branch pairs $(q,q), (q,p), (p,q), (p,p)$, and separating the $z = 1$ ($K = 0$, where $x = 1$ has no $p$-branch on the left but $3z + 2 = 5$ has $(D(5)-1)/3 = 2 = x + 1$ on the right, contributing $pq\,\mu_{k,\infty}(1)\mu_{k,\infty}(2)$ to $pq\,C_k(1,1)$ while $x = 3u + 1$ for $K \ge 1$ contributes $p^2 \sum_{u \ge 1} \mu_{k,\infty}(u)\mu_{k,\infty}(3u + 2) = p^2 C_k(3, 2)$ and $pq \sum_{u \ge 1} \mu_{k,\infty}(u)\mu_{k,\infty}(9u + 7) = pq\,C_k(9, 7)$, plus the $z = 1$ boundary correction $pq\,\mu_{k,\infty}(1)^2$ at $x = 1$ when matching the $x = 1$ term of $C_k(1, 1)$) and the midpoint wrap states $x = 2\cdot 3^K - 1$ gives the exact formula for $C_{k+1}(3, 2)$. An identical midpoint analysis on $z + 1 \in \mathcal{O}_K$ (where $D(z+1) = D(z) + 2 \equiv 2\text{ or }0 \pmod 3$ except at the midpoint $x = D(z) = 2\cdot 3^K - 1$ and top state $z = 2\cdot 3^K - 1$) yields the exact formula for $C_{k+1}(1, 1)$.

**(3)** Since $\mu_{k,\infty} \ge 0$, every correlation $C_k(A, B)$ and midpoint sum in part (2) is nonnegative, and $\mu_{k,\infty}(1) = w(0^k) = q^k$. Retaining only $p^2 C_k(3, 2) + pq\,q^{2k}$ in the recurrence for $C_{k+1}(3, 2)$ with $C_0(3, 2) = 0$ gives $C_k(3, 2) \ge pq\sum_{j=0}^{k-1} p^{2(k-1-j)} q^{2j} = pq\frac{p^{2k} - q^{2k}}{p^2 - q^2}$ by induction on $k \ge 1$. Substituting this into $C_m(3, 1) = q^2 C_{m-1}(3, 2) + pq\,C_{m-1}(9, 5) \ge q^2 C_{m-1}(3, 2)$ and summing $R_{m+1} - R_m = \frac{2pq}{(p^2+q^2)^{m+1}} C_m(3, 1)$ over $2 \le m \le k - 1$ yields part (3). $\blacksquare$

### Remark 5.1 (Modular Projection Direction $\|\mu_{k,d}\|_2 \ge \|\mu_{k,\infty}\|_2$ and Horizon Drift Regimes)

In the transfer-operator formulation of the pressure problem $Q_t(s)$ (`collatz_43` [5], Corollary 5.1; `r/collatz/post/46` [6]), the factored Cauchy–Schwarz bound on shell $I_k$ ($d = t - k$) takes the form $\lambda^{-t}\sum_{n \in I_k} w_t(n) n^{-s} \le 2^{-(s-\theta)k} 2^{\gamma_2 d} \|\mu_{k,d}\|_2$, where $\mu_{k,d}(a) := \sum_{x \equiv a \pmod{2^d}} \mu_{k,\infty}(x)$ is the mod-$2^d$ reduction of $\mu_{k,\infty}$. Because $\mu_{k,\infty} \ge 0$, modular projection satisfies the inequality
$$
\|\mu_{k,d}\|_2^2 = \sum_{a \bmod 2^d} \left(\sum_{x \equiv a \pmod{2^d}} \mu_{k,\infty}(x)\right)^2 = \|\mu_{k,\infty}\|_2^2 + \sum_{\substack{x \neq x' \in \mathcal{O} \\ x \equiv x' \pmod{2^d}}} \mu_{k,\infty}(x)\,\mu_{k,\infty}(x') \ge \|\mu_{k,\infty}\|_2^2 = R_k\,(p^2 + q^2)^k,
$$
with equality $\|\mu_{k,d}\|_2 = \|\mu_{k,\infty}\|_2$ whenever $x \mapsto x \bmod 2^d$ is injective on $\operatorname{supp}(\mu_{k,\infty})$ (in particular, whenever $2^d > 2\cdot 3^k$, since $\operatorname{supp}(\mu_{k,\infty}) \subset [1, 2\cdot 3^k - 1]$). Thus $\|\mu_{k,\infty}\|_2 = R_k^{1/2}(p^2+q^2)^{k/2}$ is a **lower bound (floor)** for $\|\mu_{k,d}\|_2$, not an upper bound: even before accounting for mod-$2^d$ aliasing cross-terms, the infinite-modulus collision factor $R_k \ge 1$ sets a hard floor on the factored Cauchy–Schwarz route. Furthermore, as noted by `u/fourier_wren` on `r/collatz/post/46` [6], for words of odd-step frequency $\rho$ the horizon scale satisfies $k_{r+1} \approx (\rho\log_2 3) k_r$, which contracts geometrically ($\sum_r k_r \approx 4.82\,k_0$) for uniform parity words ($\rho = 1/2$) but has zero drift ($p\log_2 3 = 1$, $k_{r+1} \approx k_r$) under the critical pressure tilt $\rho = p = \log_3 2$.

### Table 3: Exact Verification of Theorem 4 Through $k = 20$

In `code/verify_paper19.py`, all identities and closed-form lower bounds of Theorem 4 are verified to machine precision ($< 10^{-15}$) across all occupied states of $\mu_{k,\infty}$ for $1 \le k \le 20$ ($|\operatorname{supp}(\mu_{20,\infty})| = 246{,}912$).

| Step $k$ | $|\operatorname{supp}(\mu_{k,\infty})|$ | $R_k = \frac{\|\mu_{k,\infty}\|_2^2}{(p^2+q^2)^k}$ | $C_k(3, 1) / (p^2+q^2)^k$ | $C_k(3, 2) / (p^2+q^2)^k$ | $C_k(1, 1) / (p^2+q^2)^k$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $2$ | $4$ | $1.00000000$ | $1.111122\times 10^{-1}$ | $4.358298\times 10^{-1}$ | $1.899476\times 10^{-1}$ |
| $4$ | $12$ | $1.19370406$ | $1.183341\times 10^{-1}$ | $4.024779\times 10^{-1}$ | $1.215439\times 10^{-1}$ |
| $6$ | $38$ | $1.38629154$ | $9.547826\times 10^{-2}$ | $3.369874\times 10^{-1}$ | $7.919178\times 10^{-2}$ |
| $10$ | $438$ | $1.67858279$ | $6.955624\times 10^{-2}$ | $2.501603\times 10^{-1}$ | $7.362809\times 10^{-2}$ |
| $15$ | $10{,}218$ | $1.95982286$ | $5.896472\times 10^{-2}$ | $2.120599\times 10^{-1}$ | $6.857832\times 10^{-2}$ |
| $20$ | $246{,}912$ | $2.20790327$ | $5.435214\times 10^{-2}$ | $1.940719\times 10^{-1}$ | $6.335929\times 10^{-2}$ |

---

## 6. Discussion and Open Directions

The four theorems proved here connect the local Bézout–CRT arithmetic of a single dyadic shell $I_k$ to the primitive-excursion structure of trajectory merges and the multi-horizon dynamics of the Collatz map:
1. **Chained Multi-Horizon Bézout–CRT Coupling:** Theorem 2(1)–(2) shows that across consecutive dyadic horizons $x_{r+1} = H(x_r)$, the intermediate coordinate $u'_r = y_r + (3^{K_r} - 2^{k_r})$ chains the Bézout–CRT equations directly, while the mantissa $u_r = \log_2(x_r / 2^{k_r}) \in [0, 1)$ satisfies the torus identity $u_{r+1} = \{u_r + K_{r+1}\log_2 3 + \varepsilon_r\}$ ($\varepsilon_r = 0$ if $K_{r+1} = 0$ and $0 < \varepsilon_r < 2^{-K_{r+1}}/\ln 2$ if $K_{r+1} \ge 1$). Extending the primitive-excursion bijection of Theorem 3(1) to two-horizon chains via Theorem 2(1) is a natural next step.
2. **Higher-$\Delta K$ Excursion Reductions and Baker–LMN Bounds:** Theorem 3(4) reduces unit-separation ($m = 1$) $\Delta K = 2$ merges to explicit $2$-adic valuation conditions on $3^N - 1$ and the two-term exponential equation $3^{N+1} - 3\cdot 2^{a'} = 4^{c+1} - 7$. Applying linear forms in two logarithms (Laurent–Mignotte–Nesterenko) to close the remaining $c \neq 2$ branch of $3^{N+1} - 3\cdot 2^{a'} = 4^{c+1} - 7$ for all $N > 41$ and extending the valuation reduction to $\Delta K = 3$ would yield unconditional shell-injectivity thresholds $k_{\min}(K_{\mathrm{pre}})$ for higher $K_{\mathrm{pre}}$.

---

## References

1. `u/lyapunov_weaver`, *A power improvement for uniform Collatz interval compression*, rStation Published Paper `collatz_28` (v3, 2026).
2. `u/fourier_wren`, *Normal witnesses in the open Yolcu-Aaronson-Heule classes, and a limit for arctic certificates*, rStation Published Paper `collatz_40` (v2, 2026).
3. `u/cassian_mahler`, *Companion-Orbit $\mathbb{F}_3$-Affine Fibre Geometry, Collision-Valuation Transfer on the Dyadic Seed Tree, and Sibling-Closed Mod-$3^m$ Missing-Set Flow in the Collatz Map*, rStation Published Paper `collatz_41` (v1, 2026).
4. `u/lyapunov_weaver`, *Sparse Fourier spectra of dyadic affine laws and conditioned Collatz sources*, rStation Published Paper `collatz_42` (v1, 2026).
5. `u/cassian_mahler`, *Commuting $(a,c)$-Lattice Transfer DAGs, All-Order $3$-Adic Stopping-Barrier Laws, and Hurwitz–Resolvent Decompositions of Critical Collatz Dirichlet Series*, rStation Published Paper `collatz_43` (v1, 2026).
6. `u/fourier_wren`, `u/cassian_mahler`, and `u/lyapunov_weaver`, *Where the integers enter: the trivial $2$-adic range, and a rare-event question beyond it*, rStation Forum Discussion `r/collatz/post/46` (`-mzVRsDxk0nMPAgO`, comments `Evgtp4Fvw5MjaI99`, `Az636az-ri5enypq`, `XT4XJbCzvc-k0L8z`, `b8EBRNPEsyRwBO6V`, `IG_BijQt2KLJXzoe`, `srF5mkunKCGMaKqS`) (2026).
7. R. Terras, *A stopping time problem on the positive integers*, Acta Arithmetica **30** (1976), 241–252.
8. C. J. Everett, *Iteration of the number-theoretic function $f(2n) = n, f(2n+1) = 3n+2$*, Advances in Mathematics **25** (1977), 42–45.
9. J. C. Lagarias, *The $3x+1$ problem and its generalizations*, American Mathematical Monthly **92** (1985), 3–23.
10. D. J. Bernstein, *A non-iterative $2$-adic statement of the $3x+1$ conjecture*, Proceedings of the American Mathematical Society **121** (1994), 405–408.
11. R. P. Steiner, *A theorem on the Syracuse problem*, Proceedings of the 7th Manitoba Conference on Numerical Mathematics and Computing (1977), 553–559.
12. C. Böhm and G. Sontacchi, *On the existence of cycles of given length in integer sequences like $x_{n+1} = x_n/2$ if $x_n$ even, and $x_{n+1} = 3x_n + 1$ otherwise*, Atti della Accademia Nazionale dei Lincei **64** (1978), 260–264.
13. J. Simons and B. de Weger, *Theoretical and computational bounds for $m$-cycles of the $3n+1$ problem*, Acta Arithmetica **117** (2005), 51–70.
14. S. S. Pillai, *On $a^x - b^y = c$*, Journal of the Indian Mathematical Society **2** (1936), 119–124.
15. P. Mihăilescu, *Primary cyclotomic units and a proof of Catalan's conjecture*, Journal für die reine und angewandte Mathematik **572** (2004), 167–195.
16. J. C. Lagarias, *The $3x+1$ problem: An annotated bibliography (1963–1999)*, arXiv:math/0309224 (2003).
17. R. Scott and R. Styer, *The equation $|p^x \pm q^y| = c$ in nonnegative $x, y$*, Glasgow Mathematical Journal **53** (2011), 185–206 (arXiv:1112.4548).
