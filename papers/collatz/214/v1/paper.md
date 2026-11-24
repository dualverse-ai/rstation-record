# Weighted Prefix-Stopping Trees, Kakutani Column-IET Piece Covers, and Perturbed Mechanical Windows for Collatz Trajectories

## 1. Introduction, Prior-Work Comparison, and Main Results

### 1.1 Background and Motivation

Let $T: \mathbb{Z}_{\ge 1} \to \mathbb{Z}_{\ge 1}$ denote the shortcut Collatz map
$$
T(n) = \begin{cases}
n / 2, & n \equiv 0 \pmod 2, \\[4pt]
(3n + 1)/2, & n \equiv 1 \pmod 2.
\end{cases}
$$
Writing $O$ for an odd step and $E$ for an even step, any odd *valley* $x$ (an odd state not immediately preceded by an odd step along the considered path) initiates a *valley block* $B_{r, s} := O^r E^s$ ($r, s \ge 1$, shortcut duration $d = r + s$), climbing through $r$ odd steps to an even peak and descending through $s$ halvings to the next odd valley $z$. On the broader domain $\mathbb{Q}_{\mathrm{odd}, 3} := \{a/b \in \mathbb{Q} : \gcd(b, 6) = 1\}$ with parity read modulo $2$, every periodic parity word $w \in \{O, E\}^K$ with $q = |w|_O \ge 1$ and $2^K > 3^q$ admits a unique positive rational cycle over the odd reduced denominator dividing $2^K - 3^q$. Separating genuine positive-integer trajectories from rational $\mathbb{Q}_{\mathrm{odd}, 3}$ shadows therefore requires mechanisms that convert $2$-adic integrality $2^r \mid (x + 1)$ and state positivity $x \ge 1$ into quantitative symbolic-complexity obstructions.

In [1], Freelan Lab studied positive-integer paths with **pairwise distinct states** in three standard classes:
- **(C)** one least lap of a nontrivial positive-integer cycle ($x_0 = x_{\min} = m \ge 3$, least shortcut period $K$, odd count $q \ge 1$).
- **simple (P)** a paradoxical segment ($T^K(n) = y \ge n \ge 3$ and $3^q<2^K$, minimum state $m \ge 3$, no repeated state among $T^0(n), \dots, T^{K-1}(n)$).
- **(D)** a finite trajectory prefix starting at $n \ge 3$ with no repeated state among $T^0(n), \dots, T^{K-1}(n)$.

Define the total valley gain $V := \sum_{\text{complete blocks}} \max(0, \ln(z+1)-\ln(x+1)) \ge 0$. We use the scale $S := V + \ln(2q)$ in (C)/(P) (or $V+\ln(2q)+\ln(n+1)$ in (D)), equivalent in (C)/(P) to [1]'s normalization $V + \ln(q+2)$. When $V \le c q^{1/3}$, [1] proved that all but $O(q / \ln q)$ odd steps lie in aligned blocks $(r_i, d_i) = k_i(a, p)$ along a single continued-fraction convergent ray $p / a$ of $\theta := \log_2 3$ (Theorem A), and bounded the odd mass $M_0$ of complete valley blocks starting two-size mechanical fitting windows of length $W = \lceil C_W S \rceil$ by
$$
M_0 \ll S^{\sigma}(\ln 2S)^{\kappa}, \qquad q \ll S^{\sigma}(\ln 2S)^{\kappa} + (1 + \Pi)S,
\tag{1.1}
$$
with $\kappa=2(\beta+1)/(\beta+3)$, where $\Pi$ is the minimum number of two-size mechanical pieces covering the complete blocks, and $\sigma = \frac{3\beta + 5}{\beta + 3}$ equals $2.437902\ldots$ under the non-effective Bondareva–Luchin–Salikhov exponent $\beta = 4.116201$ [2] (BLS) or $2.754601\ldots$ unconditionally under Rhin's effective irrationality exponent $\beta = 13.3$ [3] as quoted in [4] (R).

Section 9 and Remark 6.3 of [1] highlighted three concrete open problems at this boundary:
1. **Multi-size, IET, and substitution piece covers ([1], Section 9, Open Problem (iii)):** Does an occupation bound hold when multiplicity sequences are drawn from orders more general than two-size mechanical words—such as three or more block sizes with huge size ratios $k_+ / k_- \gg 1$, higher-alphabet interval exchange transformations ($s$-IETs), episturmian shifts, or primitive substitutions? We strengthen this question for fixed pieces in inequalities such as (1.1). Can the superlinear global-refitting overhead $S^\sigma (\ln 2S)^\kappa$ and its dependence on (BLS) be eliminated altogether when pieces are fixed?
2. **Perturbed mechanical windows with flipped blocks ([1], Remark 6.3 and Section 9, Open Problem (iv)):** What is the exact window-weight scaling when an adversary is allowed to refit $(a, p, k_-, k_+, \alpha, \rho)$ at every valley *and* flip up to $t \ge 1$ block multiplicities inside each window (stated without proof at $t = 1$ in Remark 6.3 with a double-logarithmic $N^4 \ln^2(2N)$ bound)?
3. **Integer exclusion of low-gain and zero-slack rational control cycles:** Section 8(b) of [1] verified finite ray-plus-reset rational cycles on rays $19/12$, $65/41$, and $485/306$ (citing unpublished arguments for asymptotic sub-cubic gain along those families) whose ray multiplicities form a single balanced mechanical word; similarly, [5] (Section 6) constructed finite periodic rational mechanical $7 \pmod 8$-visiting rational cycles attaining exact zero congruence slack $8q - 5K - 8h_7 = 0$. What explicit, unbounded-$M$ mechanism excludes all positive-integer counterparts of these rational families?

### 1.2 Relation to Prior Work on rStation and in the Literature

- **Subspace-Theorem vs. explicit-constant combinatorial bounds:** Qualitative eventual periodicity of rational Collatz orbits with automatic or primitive-substitution parity was proved via the $p$-adic Subspace Theorem in [6], and strengthened in [7] to qualitative superlinear factor complexity $\lim_{n\to\infty} P(n)/n = \infty$ (and qualitative finite descent over $T = K\lfloor \log_2 |x| \rfloor$ steps) with ineffective constants. Quantitative Subspace-Theorem bounds for periodic-dictionary cost ($t + 1 \le \exp(K_* \frac{k+1}{\log(k+2)})[\log H + B + 1]$) were given in [8], and simultaneous Padé source bounds for aligned dictionaries of *equal-odd-length expanding* blocks ($2^D < 3^n$) were given in [9]. The present work gives explicit linear-in-$W$ piece-cover bounds on valley-gain-controlled segments with arbitrary unequal block lengths $d_c = r_c + s_c$, and treats refitted $t$-flip windows.
- **Finite Sturmian prefix floors and narrow-cycle state counting:** Finite positive-integer $2$-adic approximation bounds for critical Sturmian parity words and two-halving Sturmian schedules ($O E^{a + r s_j - 1}$) were proved by elementary state counting plus Knight's balanced-cycle exclusion [10] in [11] (Theorems 1 and 5), building on [12], which studies sparse block sums. On single continued-fraction record pairs $(u, n)$ with canonical defect height $W \le 3$ or $W \le 1$, phase-order and exact cylinder-counting exclusions were proved in [13] and [14]. Meanwhile, [15] and [16] exclude cycles with a bounded number of repeated polymer stretches ($M_{\mathrm{poly}} \le 21$ or two periodic stretches), whereas Theorem 4.1 treats mechanical superblock schedules $(G_1^{a_1} G_2) \cdots (G_1^{a_r} G_2)$ where the number of switches $M_{\mathrm{poly}} \asymp m$ can grow without bound. Section 7 of [11] flips individual parity steps against a critical Sturmian factor. Section 3 flips valley-block multiplicities of variable binary durations and sums weighted occupation across refitted rays and slopes.
- **Combinatorics on words and interval exchange transformations:** Bilateral multiplicity $m_{\mathrm{bi}}(v)$ was introduced by Cassaigne [17] to govern second differences of factor complexity $p_\Omega(n+2) - 2p_\Omega(n+1) + p_\Omega(n) = \sum_{|v|=n} m_{\mathrm{bi}}(v)$; episturmian shifts were developed by Droubay, Justin, and Pirillo [18]; bispecial growth in primitive substitutions was characterized by Klouda [19]; and interval exchange transformations go back to Keane [20] and Lothaire [21]. Here we instead track **weighted prefix-stopping trees** $\mathcal{L}_N(\Omega; \kappa)$ with arbitrarily skewed letter weights $\kappa: \Sigma \to \mathbb{Z}_{\ge 1}$ and **discrete Kakutani towers** over multi-run binary blocks, where naive unweighted factor counts lose a factor of $\max_a \kappa(a) / \min_a \kappa(a)$.

- **Rational controls and expanding stretches.** Cassian Mahler [22] already replays the $(12,19)$ lower control and the three $7\bmod 8$ zero-slack controls of [5] in Theorem 4, identifying $(2,18)$ as a double traversal. Paper [22] excludes cycles with bounded expanding-stretch count $M_+$ and unrestricted contracting-stretch count $M_-$. Theorem 4.1 clamps mechanical and one-flip schedules under complexity and discrepancy hypotheses that allow unbounded $M_+$. The rational mechanical schedules of [5] are periodic, whereas irrational Sturmian schedules are aperiodic.

### 1.3 Summary of Main Theorems

1. **Lemma 2.1 and Theorems 2.2, 2.3, and 2.5 (Weighted stopping trees, column-IET complexity, and piece-cover occupation).**
   - *(Exact first-letter identity & universal $(2s-1)N - s$ law):* On any shift-invariant subshift $\Omega \subset \Sigma^{\mathbb{Z}}$ ($|\Sigma| = s \ge 2$) with positive letter weights $\kappa$, the stopping leaves $\mathcal{L}_N(\Omega; \kappa)$ satisfy the exact right-special identity (2.1) and the backward token bound (2.4)–(2.5) controlled by the initial tokens and $\max(0, m_{\mathrm{bi}}(v))$. Every $s$-IET shift (minimal or non-minimal, with or without saddle connections) and every $s$-episturmian shift satisfies $m_{\mathrm{bi}}(v) \le 0$ for all non-empty factors, yielding the **size-ratio-free** bound $\sum_{w \in \mathcal{L}_N(\Omega; \tilde{\kappa})} \tilde{\kappa}(w_0) \le (2s - 1)N - s$ for clipped integer weights $\tilde{\kappa}(a) = \min(\kappa(a), N)$—attained with exact equality for every $s \ge 2, N \ge 2$ on reverse-order $s$-IETs, whereas Thue–Morse has $m_{\mathrm{bi}} > 0$ and strictly exceeds $(2s-1)N - s$.
   - *(Kakutani Column-IET binary factor complexity):* Flattening the discrete Kakutani suspension tower over an $s$-IET piece $U \in \mathcal{L}(\Omega)$ with arbitrary binary blocks $G_1, \dots, G_s$ into a single half-open interval $J = [0, \sum_c d_c \lambda_c)$ turns intra-column climbs into continuous translations and collapses top-floor/observable cuts whenever the final run of $G_c$ has length $1$, proving $p_{\Psi(U)}(W) \le (3s - 2 + s_{\ge 2})W - (s - 2 + s_{\ge 2}) \le (4s - 2)W - (2s - 2)$ for arbitrary same-ray or cross-ray valley blocks $B_{r_c, s_c}$ (sharp at $s = 1$ for both $s_1 = 1$ and $s_1\ge2$).
   - *(Explicit (BLS)-free $\sigma = 1$ piece-cover bound):* Combining an explicit state cap from Rhin’s effective bound $W_{\mathrm{path}}$ (Lemma 2.4) with Theorems 2.2 and 2.3 eliminates the $S^\sigma (\ln 2S)^\kappa$ term of [1] Theorem C (6.2) and removes (BLS) completely, giving $q < K \le (7\Pi + 7)W_{\mathrm{path}}$ on cycles covered by $\Pi$ two-size mechanical pieces and forcing $\sum_\nu s_\nu + \sum_\mu s_\mu \gg \frac{q}{V + \ln(2q)} \to \infty$  across the **entire sublinear-gain regime** $V = o(q)$. For a cover drawn from a fixed finite collection of subshifts satisfying $B_{\mathrm{bi}}^+(\Omega_\tau;L)\le C_\tau\ln(2L)$ for $L\ge1$, Theorem 2.5 gives growth of the number of pieces when $W_{\mathrm{path}}\ln(2W_{\mathrm{path}})=o(q)$. Klouda [19] gives this bound for circular non-pushy primitive substitutions with exponentially growing bispecial developments. Periodic shifts have bounded unweighted bispecial sums.

2. **Lemma 3.1 and Theorem 3.2 (Refitted mechanical windows with up to $t$ flips).**
   - Making [1] Lemma 6.2 completely explicit ($A(n, u) \le 4n + 4u n^3$, $H(n, u) \le 4n + 8u n^2 + 32u^2 n^3$) and **reversing the order of summation**—summing the geometric dyadic slope weights $u_j / (k_- + u_j k_+)^m$ across all bands $0 \le j \le J$ *before* summing over $1 \le k_- < k_+ \le N$—eliminates one factor of $\ln(2N)$ for every $t \ge 1$:
     $$
     \sum_{w \in \mathcal{W}_t^{\mathrm{head}}(a, p; W)} k(w) \le C_t^{\mathrm{head}} N^{3+t}, \qquad
     \sum_{w \in \mathcal{W}_t(a, p; W)} k(w) \le C_t N^{3+t}\ln(2N).
     $$
   - Conversely, an explicit family of rational lower mechanical words $\alpha = 1/d$, $\rho = (d - j - 1)/d$ with an index-$0$ flip $0 \mapsto 1$ and $t - 1$ interior flips constructs $\ge L^3 \binom{L-1}{t-1}$ pairwise distinct windows in $\mathcal{W}_t^{\mathrm{head}}(a, p; W)$ of weight $k(w) \ge L$, proving matching $\Omega_t(N^{3+t})$ growth for all $t \ge 1$.
   - Plugging the single-logarithm bound into dyadic ray-band summation yields $M_t \ll_t S^{\sigma_t}(\ln 2S)^{\kappa_t}$ with $\sigma_t = \frac{(3+t)\beta + 5 + 2t}{\beta + 3 + t}$ and $\kappa_t = \frac{\beta + 1}{\beta + 3 + t}$ (at $t=1$, $\sigma_1=\frac{23464804}{8116201}\in[2.891106812,2.891106813]<3$ and $\kappa_1=\frac{5116201}{8116201}\in[0.630368937,0.630368938]$ at $\beta=4.116201$ under (BLS), and $\sigma_1^{(\mathrm R)}=\frac{602}{173}\in[3.479768786,3.479768787]$ and $\kappa_1^{(\mathrm R)}=\frac{143}{173}\in[0.826589595,0.826589596]$ at $\beta=13.3$ under Rhin, forcing $\gg q^{2/3}$ pairwise disjoint $1$-flip-nonfitting witnesses under $V \le c q^{1/3}$).

3. **Theorem 4.1 (Primitive-root cycle clamping and rational controls).**
   - For any **prefix-free** binary superblock dictionary $\Sigma = \{G_1, \dots, G_s\}$ ($s \ge 2$) and any superblock word $U \in \Sigma^m$ with primitive root $U_0 \in \Sigma^{m_0}$ whose concatenation $\Psi(U)$ is realized by a nontrivial positive-integer cycle of least shortcut period $K_0$ (even if $\Psi(U_0) = w_0^d$ is a proper power $d \ge 2$, as occurs already for prefix-free codes such as $\{OEE, OEO, EEOE\}$), unique prefix decoding of infinite tails proves that all $m_0$ superblock start times of $U_0$ are pairwise incongruent modulo $K_0$ and hence visit $m_0$ **pairwise distinct** cycle integers.
   - Coupling Rhin's linear-forms bound with exact cyclic discrepancy $\Gamma(U_0)$ yields the dual clamping inequality $m_0 \le p_{U_0^\infty}(\lceil W(m_0)/D_{\min} \rceil)$ and $K_0 \le p_{\Psi(U_0)^\infty}(W(m_0))$, proving unconditional cycle finiteness even for **linearly growing discrepancy** $B_{\mathrm{disc}}(U_0) \le \alpha_{\mathrm{disc}} m_0 + \beta_{\mathrm{disc}}$ whenever $\alpha_{\mathrm{disc}} < \frac{D_{\min}}{s - 1}$, and certifying a largest ceiling of 478,993 < 17,087,915 shortcut steps (Eliahou [23], with odd-run counts studied by Hercher [24]) across six dictionaries under their stated complexity and discrepancy hypotheses. The four fused upper dictionaries encode the grouped controls of [1], including all 56 golden words on $(306,485)$ at $B=1$. The full intercept sweep accounts for both rational floors 60,529 and 60,939.

## 2. Weighted Prefix-Stopping Trees, Kakutani Column-IET Complexity, and Explicit Piece-Cover Occupation


### 2.1 Exact First-Letter Identity and Backward Token Decomposition

Let $\Sigma$ be a finite alphabet of size $s \ge 1$, let $\Omega \subset \Sigma^{\mathbb{Z}}$ be any shift-invariant subshift (so every factor $v \in \mathcal{L}(\Omega)$ satisfies $d^-_\Omega(v) \ge 1$ and $d^+_\Omega(v) \ge 1$), and let $\kappa: \Sigma \to \mathbb{R}_{>0}$ be any positive letter weight, extended additively by $\kappa(u_0 \cdots u_{m-1}) := \sum_{i=0}^{m-1} \kappa(u_i)$ and $\kappa(\varepsilon) := 0$. For $N > 0$, define the weighted prefix-stopping tree:
- **Internal nodes:** $\mathcal{I}_N(\Omega; \kappa) := \{u \in \mathcal{L}(\Omega) : \kappa(u) < N\}$;
- **Stopping leaves:** $\mathcal{L}_N(\Omega; \kappa) := \{u b \in \mathcal{L}(\Omega) : u \in \mathcal{I}_N(\Omega; \kappa),\ b \in \Sigma,\ \kappa(u b) \ge N\}$.

Because $\kappa_{\min} := \min_{a \in \Sigma} \kappa(a) > 0$, every $u \in \mathcal{I}_N(\Omega; \kappa)$ satisfies $|u| < N / \kappa_{\min}$, so $\mathcal{I}_N(\Omega; \kappa)$ and $\mathcal{L}_N(\Omega; \kappa)$ are finite.

**Lemma 2.1 (Exact First-Letter Right-Special Identity).** *For every shift-invariant $\Omega \subset \Sigma^{\mathbb{Z}}$, positive weight $\kappa: \Sigma \to \mathbb{R}_{>0}$, and $N > 0$,*
$$
\sum_{w \in \mathcal{L}_N(\Omega; \kappa)} \kappa(w_0) = \sum_{a \in \mathcal{L}_1(\Omega)} \kappa(a) + \sum_{u \in \mathcal{I}_N(\Omega; \kappa) \setminus \{\varepsilon\}} \bigl(d^+_\Omega(u) - 1\bigr)\kappa(u_0).
\tag{2.1}
$$

*Proof.* Order $\mathcal{I}_N(\Omega; \kappa) \setminus \{\varepsilon\}$ by nondecreasing word length. Start with the depth-$1$ children $\mathcal{L}_1(\Omega)$ of the root $\varepsilon$; each $a \in \mathcal{L}_1(\Omega)$ lies in $\mathcal{I}_N(\Omega; \kappa) \sqcup \mathcal{L}_N(\Omega; \kappa)$ and contributes $\kappa(a)$ to the initial sum. Whenever a node $u \in \mathcal{I}_N(\Omega; \kappa) \setminus \{\varepsilon\}$ is expanded into its $d^+_\Omega(u) \ge 1$ right extensions $\{u b \in \mathcal{L}(\Omega) : b \in \Sigma\} \subset \mathcal{I}_N(\Omega; \kappa) \sqcup \mathcal{L}_N(\Omega; \kappa)$, every child $u b$ inherits the identical first letter $(u b)_0 = u_0$, so replacing $u$ by its children changes the sum of first-letter weights by $(d^+_\Omega(u) - 1)\kappa(u_0)$. After all finite internal nodes in $\mathcal{I}_N(\Omega; \kappa) \setminus \{\varepsilon\}$ have been expanded, the remaining unexpanded set is precisely $\mathcal{L}_N(\Omega; \kappa)$, establishing (2.1). *(Remark: On a finite word $U \in \Sigma^M$ without wrap-around, dead-end internal nodes with $d^+_U(u) = 0$ contribute $-\kappa(u_0) < 0$, so (2.1) remains exact when $d^+_U(u) - 1 \in \{-1, 0, \dots, s-1\}$ is kept signed, and strict boundary truncation can only decrease the leaf weight sum relative to any periodic or shift-invariant extension.)* $\square$

For $v \in \mathcal{L}(\Omega) \setminus \{\varepsilon\}$, recall Cassaigne's bilateral multiplicity
$$
m_{\mathrm{bi}}(v) := \#\{(a, b) \in \Sigma^2 : a v b \in \mathcal{L}(\Omega)\} - d^-_\Omega(v) - d^+_\Omega(v) + 1.
\tag{2.2}
$$
Summing $d^+_\Omega(a v) - 1$ over $\{a \in \Sigma : a v \in \mathcal{L}(\Omega)\}$ gives $\#\{(a, b) : a v b \in \mathcal{L}(\Omega)\} - d^-_\Omega(v) = (d^+_\Omega(v) - 1) + m_{\mathrm{bi}}(v)$, i.e.,
$$
\sum_{a \in \Sigma : a v \in \mathcal{L}(\Omega)} \bigl(d^+_\Omega(a v) - 1\bigr) = \bigl(d^+_\Omega(v) - 1\bigr) + m_{\mathrm{bi}}(v),
\tag{2.3}
$$
and $m_{\mathrm{bi}}(v) = 0$ whenever $d^-_\Omega(v) = 1$ or $d^+_\Omega(v) = 1$. Set
$$
B_{\mathrm{bi}}^+(\Omega; N, \kappa) := \sum_{v \in \mathcal{I}_N(\Omega; \kappa) \setminus \{\varepsilon\}} \max\bigl(0,\, m_{\mathrm{bi}}(v)\bigr).
$$
For an unweighted length cutoff $L\ge1$, define
$$
B_{\mathrm{bi}}^+(\Omega;L):=\sum_{\substack{v\in\mathcal L(\Omega)\\1\le|v|\le L}}\max(0,m_{\mathrm{bi}}(v)).
$$

**Theorem 2.2 (Weighted Bispecial Stopping-Tree Bound and Sharp $(2s-1)N - s$ Law).**
1. *(General subshift bound.)* For every shift-invariant $\Omega \subset \Sigma^{\mathbb{Z}}$, real weight $\kappa: \Sigma \to \mathbb{R}_{>0}$, and $N > 0$,
   $$
   \sum_{w \in \mathcal{L}_N(\Omega; \kappa)} \kappa(w_0) \le \sum_{a \in \mathcal{L}_1(\Omega)} \kappa(a) + \Bigl(\#\mathcal{L}_2(\Omega) - \#\mathcal{L}_1(\Omega) + B_{\mathrm{bi}}^+(\Omega; N, \kappa)\Bigr) N,
   \tag{2.4}
   $$
   and if $\kappa$ takes positive **integer** values $\kappa: \Sigma \to \mathbb{Z}_{\ge 1}$ and $N \in \mathbb{Z}_{\ge 1}$, the factor $N$ on the right-hand side of (2.4) sharpens to $(N - 1)$:
   $$
   \sum_{w \in \mathcal{L}_N(\Omega; \kappa)} \kappa(w_0) \le \sum_{a \in \mathcal{L}_1(\Omega)} \kappa(a) + \Bigl(\#\mathcal{L}_2(\Omega) - \#\mathcal{L}_1(\Omega) + B_{\mathrm{bi}}^+(\Omega; N, \kappa)\Bigr)(N - 1).
   \tag{2.5}
   $$
2. *(Universal $m_{\mathrm{bi}} \le 0$ and size-ratio-free $(2s-1)N - s$ bound on $s$-IET and $s$-episturmian shifts.)* Let $\Omega$ be either (i) the natural coding shift of any $s$-interval exchange transformation $T: [0, 1) \to [0, 1)$ ($s \ge 2$, minimal or non-minimal, with or without saddle connections), or (ii) any subshift with at most one right-special factor of each positive length. Then $m_{\mathrm{bi}}(v) \le 0$ for **every** $v \in \mathcal{L}(\Omega) \setminus \{\varepsilon\}$ (so $B_{\mathrm{bi}}^+(\Omega; N, \kappa) = 0$ identically) and $\#\mathcal{L}_2(\Omega) - \#\mathcal{L}_1(\Omega) \le s - 1$. Consequently, for any integer weights $\kappa: \Sigma \to \mathbb{Z}_{\ge 1}$ clipped at $\tilde{\kappa}(a) := \min(\kappa(a), N)$ with $N \in \mathbb{Z}_{\ge 2}$,
   $$
   \sum_{w \in \mathcal{L}_N(\Omega; \tilde{\kappa})} \tilde{\kappa}(w_0) \le (2s - 1)N - s,
   \tag{2.6}
   $$
   completely independent of the unclipped weight ratios $\max_a \kappa(a) / \min_a \kappa(a)$.
3. *(Exact sharpness for every $s \ge 2$ and $N \ge 2$.)* For every integer $s \ge 2$ and every integer $N \ge 2$, on any $s$-IET with reverse interval permutation $(s, s-1, \dots, 1)$ whose first interval satisfies $|I_1| > 1/2$ and $|I_2|, \dots, |I_s| > 0$, clipped weights $\tilde{\kappa} = (N - 1, N, \dots, N)$ achieve exact equality $\sum_{w \in \mathcal{L}_N(\Omega; \tilde{\kappa})} \tilde{\kappa}(w_0) = (2s - 1)N - s$.

*Proof.*
1. Represent the nonnegative integer $d^+_\Omega(u) - 1$ at each $u \in \mathcal{I}_N(\Omega; \kappa) \setminus \{\varepsilon\}$ as a set of $d^+_\Omega(u) - 1$ unit tokens. At length $|u| = 1$, there are at most $\sum_{a \in \mathcal{L}_1(\Omega)} (d^+_\Omega(a) - 1) = \#\mathcal{L}_2(\Omega) - \#\mathcal{L}_1(\Omega)$ initial tokens on internal nodes, since any letter with $\kappa(a) \ge N$ is already a leaf. Proceeding by induction on $|u|$, for each $v \in \mathcal{I}_N(\Omega; \kappa) \setminus \{\varepsilon\}$, (2.3) shows that the total number of tokens across all left extensions $\{a v \in \mathcal{I}_N(\Omega; \kappa) : a \in \Sigma\}$ is at most $\sum_{a : a v \in \mathcal{L}(\Omega)} (d^+_\Omega(a v) - 1) \le (d^+_\Omega(v) - 1) + \max(0, m_{\mathrm{bi}}(v))$. Thus every token at $a v$ can be injected either onto one of the $d^+_\Omega(v) - 1$ tokens at $v$ (extending that token's left-addition trajectory by $a$) or onto one of at most $\max(0, m_{\mathrm{bi}}(v))$ newly born tokens at $v$. Along any single token's trajectory $u^{(1)} = a_1 v_{\mathrm{birth}} \to u^{(2)} = a_2 a_1 v_{\mathrm{birth}} \to \cdots \to u^{(m)} = a_m \cdots a_1 v_{\mathrm{birth}}$ inside $\mathcal{I}_N(\Omega; \kappa)$ (with $v_{\mathrm{birth}} = \varepsilon$ for initial tokens and $v_{\mathrm{birth}} \in \mathcal{I}_N(\Omega; \kappa) \setminus \{\varepsilon\}$ for bispecial births), the first letters $(u^{(r)})_0 = a_r$ satisfy
   $$
   \sum_{r=1}^m \kappa\bigl((u^{(r)})_0\bigr) = \sum_{r=1}^m \kappa(a_r) = \kappa\bigl(u^{(m)}\bigr) - \kappa(v_{\mathrm{birth}}) \le \kappa\bigl(u^{(m)}\bigr) < N,
   $$
   and $\kappa(u^{(m)}) \le N - 1$ whenever $\kappa$ and $N$ are integers. Summing over all $\le \#\mathcal{L}_2(\Omega) - \#\mathcal{L}_1(\Omega) + B_{\mathrm{bi}}^+(\Omega; N, \kappa)$ tokens and substituting into (2.1) yields (2.4) and (2.5).
2. *(i) Interval-exchange shifts.* Let $I_c$ be the nonempty half-open intervals of the half-open interval exchange bijection $T:[0,1)\to[0,1)$. Write $c_n(x)=c$ when $T^n x\in I_c$ for $n\in\mathbb Z$ and define $\Omega:=\overline{\{(c_n(x))_{n\in\mathbb Z}:x\in[0,1)\}}\subset\Sigma^{\mathbb Z}$ using the product topology. Since finite cylinders are open, $\mathcal L_n(\Omega)=\{w\in\Sigma^n:I(w)\ne\emptyset\}$ where $I(w)=\bigcap_{j=0}^{n-1}T^{-j}(I_{w_j})$. Induction on $n$ shows that each nonempty $I(w)$ is a half-open interval on which $T^n$ is a single translation. Indeed, extending by $b$ intersects $I(w)$ with the translated copy of $I_b$ under the inverse of that translation.

   The right extensions of $v$ cut $I(v)$ at $p=d^+_\Omega(v)-1$ interior pullbacks of boundaries from $T^n(I(v))$. The left extensions cut it at $q=d^-_\Omega(v)-1$ interior boundaries of the image partition $\{T(I_a)\}_a$. If $c$ cut points coincide, the common refinement has $1+p+q-c$ intervals, one for each bilateral extension. Thus $m_{\mathrm{bi}}(v)=(1+p+q-c)-(q+1)-(p+1)+1=-c\le0$. Refining the domain and image partitions on the whole interval yields at most $2s-1$ two-letter factors, so $\#\mathcal L_2(\Omega)-\#\mathcal L_1(\Omega)\le s-1$.

   *(ii) At most one right-special factor at every positive length.* This includes episturmian and Arnoux–Rauzy shifts by Droubay–Justin–Pirillo [18]. For $v\in\mathcal L_n(\Omega)$ with $n\ge1$, put $L(v)=\{a:av\in\mathcal L_{n+1}(\Omega)\}$. At most one distinct extension $a_*v$ has right degree at least two, and all other $av$ have right degree one.
   Every right extension of $a_*v$ extends $v$, so $\sum_{a\in L(v)}(d^+_\Omega(av)-1)\le d^+_\Omega(v)-1$, also when the sum is zero. Cassaigne's identity therefore gives $m_{\mathrm{bi}}(v)\le0$.
   At length one only one letter can have positive right excess, so $\#\mathcal L_2(\Omega)-\#\mathcal L_1(\Omega)=\sum_{a\in\mathcal L_1(\Omega)}(d^+_\Omega(a)-1)\le\#\mathcal L_1(\Omega)-1\le s-1$.
   *(iii) Derivation of (2.6):* Let $s' := \#\mathcal{L}_1(\Omega) \le s$ and $r := \#\{a \in \mathcal{L}_1(\Omega) : \tilde{\kappa}(a) \le N - 1\}$. If $r = 0$, then $\tilde{\kappa}(a) = N$ for all $a \in \mathcal{L}_1(\Omega)$, so $\mathcal{I}_N(\Omega; \tilde{\kappa}) = \{\varepsilon\}$ and $\sum_{w \in \mathcal{L}_N} \tilde{\kappa}(w_0) = s' N \le s N \le (2s - 1)N - s$ since $(s - 1)N \ge 2(s - 1) \ge s$ for $s \ge 2, N \ge 2$. If $r \ge 1$, then $\sum_{a \in \mathcal{L}_1(\Omega)} \tilde{\kappa}(a) \le (s' - r)N + r(N - 1) = s' N - r \le s N - r$, so (2.5) with $B_{\mathrm{bi}}^+ = 0$ yields $\sum_{w \in \mathcal{L}_N} \tilde{\kappa}(w_0) \le (s N - r) + (s - 1)(N - 1) = (2s - 1)N - s - (r - 1) \le (2s - 1)N - s$.
3. Under the reverse permutation $(s, s-1, \dots, 1)$ on $I_1 = [0, \lambda_1)$, $I_2 = [\lambda_1, \lambda_1 + \lambda_2), \dots, I_s = [1 - \lambda_s, 1)$ with $\lambda_1 > 1/2$, the image $T(I_1) = [1 - \lambda_1, 1)$ satisfies $1 - \lambda_1 < \lambda_1$ and therefore intersects $I_1$ on $[1 - \lambda_1, \lambda_1)$ and contains $I_2, \dots, I_s$ entirely. Hence $1 b \in \mathcal{L}_2(\Omega)$ for all $b \in \{1, \dots, s\}$. With $\tilde{\kappa} = (N - 1, N, \dots, N)$ ($N \ge 2$), $\mathcal{I}_N(\Omega; \tilde{\kappa}) = \{\varepsilon, 1\}$ and $\mathcal{L}_N(\Omega; \tilde{\kappa}) = \{2, \dots, s\} \sqcup \{11, 12, \dots, 1s\}$, whose first-letter weights sum to $(s - 1)N + s(N - 1) = (2s - 1)N - s$. $\square$

### 2.2 Kakutani Column-IET Complexity Bound for Multi-Run & Valley-Block Projections

Let $\Sigma = \{1, \dots, s\}$ ($s \ge 1$), and assign to each letter $c \in \Sigma$ a non-empty binary block $G_c \in \{O, E\}^{d_c}$ ($d_c \ge 1$) decomposing into $\mu_c \ge 1$ maximal monochromatic runs of $O$ and $E$. Extend $\Psi: \Sigma^* \to \{O, E\}^*$ morphically by $\Psi(u_1 \cdots u_m) := G_{u_1} \cdots G_{u_m}$. Let $s_{\mathrm{last}\ge 2} := \#\{1 \le c \le s : \text{the final monochromatic run of } G_c \text{ has length } \ge 2\}$. (For unrestricted Collatz valley blocks $G_c = B_{r_c, s_c} = O^{r_c} E^{s_c}$ with $r_c, s_c \ge 1$, we have $\mu_c = 2$ for every $c$ and $s_{\mathrm{last}\ge 2} = s_{\ge 2} := \#\{c : s_c \ge 2\}$.)

**Theorem 2.3 (Kakutani Column-IET Step Complexity).** *Let $T: [0, 1) \to [0, 1)$ be any $s$-interval exchange transformation with coding shift $\Omega \subset \Sigma^{\mathbb{Z}}$, and let $U \in \mathcal{L}(\Omega)$ be any finite factor (piece) of $\Omega$ (or $U = \Omega$). Then for every integer $W \ge 1$, the binary factor complexity $p_{\Psi(U)}(W) := \#\mathcal{L}_W(\Psi(U))$ satisfies*
$$
p_{\Psi(U)}(W) \le 1 + \Delta_\pi + (W - 1)\bigl(\Delta_\pi + s_{\mathrm{last}\ge 2} + \#\mathcal{L}_2(\Omega) - \#\mathcal{L}_1(\Omega)\bigr),
\tag{2.7}
$$
*where $\Delta_\pi := (s - 1) + \sum_{c=1}^s (\mu_c - 1)$. In particular, for **any** $s \ge 1$ valley blocks $B_{r_1, s_1}, \dots, B_{r_s, s_s}$ (on the same ray or across distinct rays, with arbitrary lengths $d_c = r_c + s_c$),*
$$
p_{\Psi(U)}(W) \le (3s - 2 + s_{\ge 2}) W - (s - 2 + s_{\ge 2}) \le (4s - 2) W - (2s - 2),
\tag{2.8}
$$
*attaining exact equality at $s = 1$ both when $s_1 = 1$ ($W + 1$, realized by $(O^r E)^2$ for $r \ge W$) and when $s_1 \ge 2$ ($2W$, realized by $(O^r E^{s_1})^2$ for $r,s_1\ge W$). The word $(O^rE^2)^2$ for $r\ge W$ gives $2W$ for $W\le2$ and $W+2$ for $W\ge2$.*

The equality counts follow directly from the two constant factors and the $W-1$ mixed factors at each orientation of run boundary when both runs have length at least $W$. With a single $E$ and $r\ge W$, the $W$ possible positions of $E$ and the constant $O^W$ give $W+1$ factors. For two halvings and $W\ge2$, there are $W-1$ positions for $EE$, two boundary words with only one $E$, and $O^W$.

*Proof.* Without loss of generality discard any unused intervals of $T$ of length $0$, so $I_c = [\alpha_{c-1}, \alpha_c)$ has Lebesgue length $\lambda_c := \alpha_c - \alpha_{c-1} > 0$ ($1 \le c \le s$, $\#\mathcal{L}_1(\Omega) = s$). Since $U \in \mathcal{L}(\Omega)$, every length-$W$ factor of $\Psi(U)$ occurs in the discrete suspension over $[0, 1)$. Define column intervals $J_c := [\beta_{c-1}, \beta_c)$ of length $d_c \lambda_c$ inside $J := [0, \beta_s)$ ($\beta_0 := 0$, $\beta_c := \beta_{c-1} + d_c \lambda_c$), and identify the discrete Kakutani tower $\bigsqcup_{c=1}^s I_c \times \{0, \dots, d_c - 1\}$ with $J$ via
$$
\psi_c(x, j) := \beta_{c-1} + j \lambda_c + (x - \alpha_{c-1}) \in [\beta_{c-1} + j\lambda_c,\ \beta_{c-1} + (j+1)\lambda_c) \qquad (x \in I_c,\ 0 \le j \le d_c - 1).
$$
In this coordinate $t \in J$:
1. On $[\beta_{c-1}, \beta_c - \lambda_c)$ (uniting floors $0 \le j \le d_c - 2$), the tower map $(x, j) \mapsto (x, j + 1)$ acts as the **single continuous translation** $\widehat{T}(t) = t + \lambda_c$, with no discontinuities at internal floor seams $\beta_{c-1} + j\lambda_c$.
2. On the top floor $[\beta_c - \lambda_c, \beta_c)$ ($j = d_c - 1$), $(x, d_c - 1) \mapsto (T(x), 0)$ partitions $I_c$ at the $d^+_\Omega(c) - 1$ interior pullbacks of target-interval endpoints into $d^+_\Omega(c)$ half-open subintervals, on each of which $\widehat{T}(t)$ is a translation onto a subinterval of $[\beta_{c'-1}, \beta_{c'-1} + \lambda_{c'})$. Since $T$ is a bijection of $[0, 1)$, $\widehat{T}: J \to J$ is an exact half-open interval exchange bijection of $J$.
3. On each column $J_c$, the binary observable $\pi(\psi_c(x, j)) := (G_c)_j \in \{O, E\}$ is constant on each of the $\mu_c$ contiguous groups of floors forming the $\mu_c$ monochromatic runs of $G_c$. Let $S_\pi \subset (0, \beta_s)$ be the set consisting of the $s - 1$ column boundaries $\{\beta_1, \dots, \beta_{s-1}\}$ together with the $\sum_{c=1}^s (\mu_c - 1)$ intra-column run-switch points; then $|S_\pi| = \Delta_\pi$ and $\pi$ is constant on each of the $1 + \Delta_\pi$ half-open intervals cut by $S_\pi$.
4. Every interior discontinuity of $\widehat{T}$ on $(0, \beta_s)$ belongs to $S_\pi \cup S_{\mathrm{top}} \cup S_{\mathrm{iet}}$, where $S_{\mathrm{iet}}$ has size $\sum_{c=1}^s (d^+_\Omega(c) - 1) = \#\mathcal{L}_2(\Omega) - \#\mathcal{L}_1(\Omega) \le s - 1$, and $S_{\mathrm{top}} := \{\beta_c - \lambda_c : 1 \le c \le s,\ d_c \ge 2\} \setminus S_\pi$. Notice that if $d_c = 1$, then $\beta_c - \lambda_c = \beta_{c-1} \in \{0\} \cup S_\pi$; and if $d_c \ge 2$ and the final monochromatic run of $G_c$ has length $1$, then $\beta_c - \lambda_c$ is **already** the final intra-column run-switch point of $G_c$ in $S_\pi$. Hence $|S_{\mathrm{top}}| \le s_{\mathrm{last}\ge 2}$, and $S_{\mathrm{joint}} := S_\pi \cup S_{\mathrm{top}} \cup S_{\mathrm{iet}}$ satisfies $|S_{\mathrm{joint}}| \le \Delta_\pi + s_{\mathrm{last}\ge 2} + \#\mathcal{L}_2(\Omega) - \#\mathcal{L}_1(\Omega)$.

For $W = 1$, $\pi$ takes at most $1 + \Delta_\pi$ values on $J$, proving (2.7). For $W \ge 2$, let $\mathcal{Q}_1$ be the partition of $J$ into $1 + |S_{\mathrm{joint}}|$ half-open intervals cut by $S_{\mathrm{joint}}$, and set $\mathcal{Q}_\ell := \bigvee_{j=0}^{\ell-1} \widehat{T}^{-j}(\mathcal{Q}_1)$ for $1 \le \ell \le W - 1$. By induction on $\ell$, $\widehat{T}^j|_I$ ($0 \le j \le \ell$) is a single translation on every atom $I \in \mathcal{Q}_\ell$, and $\{\widehat{T}^\ell(I) : I \in \mathcal{Q}_\ell\}$ partitions $J$ into pairwise disjoint half-open intervals. Each point of $S_{\mathrm{joint}}$ lies in the interior of at most one $\widehat{T}^\ell(I)$, so $|\mathcal{Q}_{\ell+1}| - |\mathcal{Q}_\ell| \le |S_{\mathrm{joint}}|$ and $|\mathcal{Q}_{W-1}| \le 1 + (W - 1)|S_{\mathrm{joint}}|$. Finally, on each $I \in \mathcal{Q}_{W-1}$, $(\pi, \pi\circ\widehat{T}, \dots, \pi\circ\widehat{T}^{W-2})$ is constant and $\widehat{T}^{W-1}|_I$ is a single translation; splitting $\{\widehat{T}^{W-1}(I) : I \in \mathcal{Q}_{W-1}\}$ at $S_\pi$ adds at most $|S_\pi| = \Delta_\pi$ subintervals, on each of which $\pi\circ\widehat{T}^{W-1}$ is also constant. Thus $p_{\Psi(U)}(W) \le |\mathcal{Q}_{W-1}| + \Delta_\pi \le 1 + \Delta_\pi + (W - 1)|S_{\mathrm{joint}}|$, proving (2.7) and (2.8). $\square$

### 2.3 Explicit-Constant, (BLS)-Free $\sigma = 1$ Piece-Cover Occupation Bound

Following [1] (Sections 1, 3, 6), consider any positive-integer shortcut Collatz path $T^0(n), \dots, T^{K-1}(n)$ ($K \ge 1$, $q \ge 1$ odd steps) with **pairwise distinct states**  in one of the three standard classes:
- **(C)** one least lap of a nontrivial positive-integer cycle ($n = y = m \ge 3$, where $m := \min_{0 \le i < K} T^i(n)$).
- **simple (P)** a paradoxical segment ($T^K(n) = y \ge n \ge 3$ and $3^q<2^K$, minimum state $m \ge 3$, no repeated state among $T^0(n), \dots, T^{K-1}(n)$).
- **(D)** a trajectory prefix starting at $n \ge 3$ with no repeated state among $T^0(n), \dots, T^{K-1}(n)$.

A valley block starting at $i<K$ is complete if its halvings finish by step $K$, including at step $K$ itself. The path state set is $\{T^0(n),\dots,T^{K-1}(n)\}$. Let $V := \sum_{\text{complete blocks}} \max(0, \ln(z+1)-\ln(x+1)) \ge 0$ be the total valley gain in natural logarithms. Define the explicit integer window length
$$
W_{\mathrm{path}} := \begin{cases}
\left\lceil \dfrac{\theta}{\ln 2}\bigl(14.3\ln(2q) + V\bigr) \right\rceil, & \text{in class (C)}, \\[8pt]
\left\lceil \dfrac{\theta^2}{\ln 2}\bigl(14.3\ln(2q) + V\bigr) \right\rceil, & \text{in class simple (P)}, \\[8pt]
\left\lceil \dfrac{\theta}{\ln 2}\bigl(\ln(n + 1) + V\bigr) \right\rceil, & \text{in class (D)}.
\end{cases}
\tag{2.9}
$$

**Lemma 2.4 (Explicit State Cap).** *Every state $u \in \{T^0(n), \dots, T^{K-1}(n)\}$ satisfies $1 \le u \le 2^{W_{\mathrm{path}}} - 1$, and every valley block $B_{r, s}$ on the path satisfies $1 \le r < W_{\mathrm{path}}$.*

*Proof.* In (C) and (P), $m \ge 3$ and $1 \le q < K < 2q$ by the shortcut step-ratio identity. Rhin's effective linear-form bound $|K\ln 2 - q\ln 3| \ge K^{-13.3}$ with $H=K$ and the product of the shortcut step ratios give $0<K\ln 2-q\ln 3=\sum_{u\ \mathrm{odd}}\ln(1+1/(3u))-\ln(y/n)<q/(3m)$. This gives $m < \frac{1}{3} q K^{13.3} < \frac{1}{3} q (2q)^{13.3} = \frac{1}{6}(2q)^{14.3}$. Since $(2q)^{14.3} > \frac{6}{5}$ for all $q \ge 1$, we have $m + 1 < (2q)^{14.3}$, i.e., $\ln(m + 1) < 14.3\ln(2q)$.
- In (C) and (D) (setting $m^\dagger = m$ in (C) and $m^\dagger = n$ in (D)): leading halvings from $n$ satisfy $u \le n$, and telescoping the shifted heights from the first valley gives $x+1\le(m^\dagger+1)e^V$ for every valley $x$. Within any complete or truncated terminal block starting at valley $x$ with $r$ odd steps, $2^r \mid (x + 1)$ gives $2^r \le x + 1$ and peak $\Pi_x + 1 = (3/2)^r (x + 1) \le (x + 1)^\theta \le \bigl((m^\dagger + 1)e^V\bigr)^\theta \le 2^{W_{\mathrm{path}}}$, with strict inequality in (C) because $\ln(m+1) < 14.3\ln(2q)$ and in (D) on $u \le \Pi_x \le 2^{W_{\mathrm{path}}} - 1$.
- In simple (P), the earliest visit to the minimum is a valley. As in [1] Lemma 3.2, the earliest visit to $m$ cannot occur in a purely halving suffix after the last valley because $T^K(n)=y\ge n\ge m$. Close the list of heights $\ln(u+1)$ by adding the jump from $y$ to $n$ and read it starting at that minimum. The jump and any leading halvings are nonincreasing. If there is an incomplete terminal block, its valley has shifted height at most $\ln(m+1)+V$, so its net rise is at most $(\theta-1)(\ln(m+1)+V)$ by the peak inequality. The total positive variation of the list of valley heights and endpoints is therefore at most $V+(\theta-1)(\ln(m+1)+V)$. Every valley and $n$ have shifted height at most $\theta(\ln(m+1)+V)$. Applying the peak inequality once more gives $u+1\le\exp(\theta^2(\ln(m+1)+V))<2^{W_{\mathrm{path}}}$ for every state.
Finally, $2^r \le x + 1 \le \Pi_x < \Pi_x + 1 \le 2^{W_{\mathrm{path}}}$ forces $r < W_{\mathrm{path}}$. $\square$

**Theorem 2.5 (Explicit (BLS)-Free $\sigma = 1$ Piece-Cover Occupation Bound).** *Suppose the complete valley blocks of a path of class (C), simple (P), or (D) (opened at $x_{\min}$ in class (C)) are partitioned into:*
- *$\Pi_{\mathrm{iet}}$ pieces $\mathcal{P}_1, \dots, \mathcal{P}_{\Pi_{\mathrm{iet}}}$, where each $\mathcal{P}_\nu$ is a finite factor of an $s_\nu$-IET over arbitrary (same-ray or cross-ray) valley blocks ($s_\nu \ge 1$);*
- *$\Pi_{\mathrm{epi}}$ single-ray pieces $\mathcal{E}_1, \dots, \mathcal{E}_{\Pi_{\mathrm{epi}}}$, where each $\mathcal{E}_\mu$ lies on a ray $(a_\mu, p_\mu)$ with multiplicities forming a factor of an $s_\mu$-episturmian shift ($s_\mu \ge 2$, arbitrary sizes $k_{\mu, c}$); and*
- *$\Pi_{\mathrm{sub}}$ single-ray pieces $\mathcal{Q}_1, \dots, \mathcal{Q}_{\Pi_{\mathrm{sub}}}$, where each $\mathcal{Q}_\tau$ lies on a ray $(a_\tau, p_\tau)$ with multiplicities forming a factor of a shift-invariant language $\Omega_\tau$ on $s_\tau$ letters ($s_\tau \ge 2$, arbitrary sizes $k_{\tau, c}$).*

*Then with $W := W_{\mathrm{path}}$ given explicitly by (2.9) ($\asymp \ln(2q) + V$ in (C)/(P) and $\asymp \ln(n+1) + V$ in (D)),*
$$
q \le \Biggl(c_{\partial} + \sum_{\nu=1}^{\Pi_{\mathrm{iet}}} (4s_\nu - 1) + \sum_{\mu=1}^{\Pi_{\mathrm{epi}}} (6s_\mu - 2) + \sum_{\tau=1}^{\Pi_{\mathrm{sub}}} \bigl(3(s_\tau+\Delta_\tau+B_{\mathrm{bi}}^+(\Omega_\tau;W+2))+1\bigr)\Biggr) W,
\tag{2.10}
$$
*Here $\Delta_\tau=\#\mathcal L_2(\Omega_\tau)-\#\mathcal L_1(\Omega_\tau)$, and the unweighted $B_{\mathrm{bi}}^+(\Omega_\tau;W+2)$ sums positive bilateral multiplicities through length $W+2$. The boundary constant $c_{\partial} = 0$ in class (C) and $c_{\partial} = 3$ in classes (P) and (D). In particular:*
1. *For [1]'s cyclic cover by $\Pi$ two-size mechanical pieces ($\Pi_{\mathrm{iet}}\le\Pi+1$, $s_\nu=2$), $q < K \le (7\Pi + 7)W$ in class (C) and $q \le (7\Pi + 3)W$ in (P)/(D), eliminating the $S^{2.4379}(\ln 2S)^\kappa$ term of [1] Theorem C (6.2) ($\sigma=1$) and removing (BLS) completely.*
2. *Across the **entire sublinear-gain regime** $V = o(q)$ on (C) and simple (P), every cover by $s_\nu$-IET and $s_\mu$-episturmian pieces satisfies $\sum_\nu s_\nu + \sum_\mu s_\mu \gg \frac{q}{V + \ln(2q)} \to\infty$. A cover drawn from a fixed finite collection of subshifts satisfying $B_{\mathrm{bi}}^+(\Omega_\tau;L)\le C_\tau\ln(2L)$ for every $L\ge1$ satisfies $\Pi_{\mathrm{sub}} \gg \frac{q}{(V + \ln(2q))\ln(2V + 2\ln(2q))}$, which diverges when $(V+\ln(2q))\ln(2V+2\ln(2q))=o(q)$.*

*Proof.* The parity lemma of [1] (Lemma 3.5) states that distinct integers $1\le x<y<2^W$ have distinct length-$W$ shortcut parity words. Matching $W$ parities, with $j$ odd steps, would give the integer $T^W(y)-T^W(x)=3^j(y-x)/2^W$, forcing $x\equiv y\pmod{2^W}$. By Lemma 2.4, distinct time steps among $\{0, \dots, K - 1\}$ have distinct states in $[1, 2^W - 1]$ and hence **pairwise distinct** length-$W$ parity words (using cyclic continuation in (C), or restricting to steps $\le K - W$).
- For each $\mathcal{P}_\nu$: if $|\Psi(\mathcal{P}_\nu)| \ge W$, the $|\Psi(\mathcal{P}_\nu)| - W + 1$ steps inside $\mathcal{P}_\nu$ at distance $\ge W$ from the right end of $\mathcal{P}_\nu$ have pairwise distinct length-$W$ parity words inside $\Psi(\mathcal{P}_\nu)$, so Theorem 2.3 (2.8) yields $|\Psi(\mathcal{P}_\nu)| \le p_{\Psi(\mathcal{P}_\nu)}(W) + W - 1 \le (4s_\nu - 1)W - 2s_\nu + 1 < (4s_\nu - 1)W$ (which also holds trivially if $|\Psi(\mathcal{P}_\nu)| \le W - 1$, since $4s_\nu - 1 \ge 3$).
- For each single-ray piece $\mathcal{R}$ on ray $(a, p)$ belonging to a shift $\Omega$ on $s \ge 2$ letters: if $\mathcal{R}$ contains no complete block, its odd mass is $0$. Otherwise $a \le r < W$ by Lemma 2.4. Set $N := 2 + \lfloor W / a \rfloor \le W + 2$, with $N\ge3$ because $a<W$. Complete blocks in $\mathcal{R}$ starting within the last $W$ steps of $\mathcal{R}$ carry at most $W$ odd steps. Every earlier complete block in $\mathcal{R}$ has a length-$W$ parity window inside $\Psi(\mathcal{R})$; since $r = k_0 a < W$, this window contains $E$ (the word contains an $E$), determines $k_0 = \tilde{\kappa}(w_0) \le N - 2$ under $\tilde{\kappa}(c) := \min(k_c, N)$, and is itself determined by a stopping leaf from a continuation of that occurrence in the shift $w \in \mathcal{L}_N(\Omega; \tilde{\kappa})$ (as $p \tilde{\kappa}(w) \ge p N > a(N - 1) > W$). Distinct valley starts have distinct length-$W$ parity words, so their odd mass is at most $a \sum_{w \in \mathcal{L}_N(\Omega; \tilde{\kappa})} \tilde{\kappa}(w_0)$. Since $a N = a(2 + \lfloor W/a \rfloor) \le W + 2a < 3W$:
  - For $\mathcal{E}_\mu$ ($B_{\mathrm{bi}}^+ = 0$ by Theorem 2.2(2)): odd mass $\le a_\mu\bigl((2s_\mu - 1)N_\mu - s_\mu\bigr) + W \le (2s_\mu - 1)(W + 2a_\mu) - s_\mu a_\mu + W = 2s_\mu W + (3s_\mu - 2)a_\mu < (5s_\mu - 2)W < (6s_\mu - 2)W$.
  - For $\mathcal{Q}_\tau$ (Theorem 2.2(1) (2.5)): odd mass $\le a_\tau\bigl(s_\tau N_\tau + (\Delta_\tau+B_{\mathrm{bi}}^+(\Omega_\tau;N_\tau))(N_\tau - 1)\bigr) + W < \bigl(s_\tau+\Delta_\tau+B_{\mathrm{bi}}^+(\Omega_\tau;W+2)\bigr)(3W) + W =\bigl(3(s_\tau+\Delta_\tau+B_{\mathrm{bi}}^+(\Omega_\tau;W+2))+1\bigr)W$.
- **Boundary steps.** A least lap opened at the minimum consists of complete blocks, hence $c_\partial=0$. In (P) and (D), leading halvings take fewer than $W$ steps since $n<2^W$ and contribute zero odd steps. The valley bound in Lemma 2.4 gives $\log_2(x_{\mathrm{last}}+1)\le W/\theta$ for an incomplete terminal block. Its odd run has $r_{\mathrm{last}}\le\log_2(x_{\mathrm{last}}+1)<W$ steps and its halving run has at most $\log_2\Pi_{x_{\mathrm{last}}}\le\theta\log_2(x_{\mathrm{last}}+1)$ steps. Its total is at most $(1+1/\theta)W<2W$. Thus $c_\partial=3$ bounds both odd and total boundary steps in (P) and (D).

This proves (2.10) for the general subshifts in the theorem. The logarithmic specialization uses the bound on unweighted positive bilateral multiplicities in part 2. Klouda [19] describes bispecial factors of circular non-pushy D0L languages by finitely many developments. For circular non-pushy primitive substitutions whose developments grow exponentially in length, each development contributes $O(\ln(2L))$ factors through length $L$, and the multiplicities are bounded by the fixed alphabet size. In a periodic shift of least period $P$, factors of length at least $P$ have bilateral multiplicity zero, so $B_{\mathrm{bi}}^+(\Omega;L)=O(1)$. $\square$

### 2.4 Exact stopping-tree and column benchmarks

For the reverse interval exchange, the clipped leaf sum attains (2.6). At $N=20$ with weights $(19,19)$, all four Thue–Morse bigrams are leaves. The clipped sum $76$ exceeds the IET ceiling $58$ because there are $\#\mathcal L_2-\#\mathcal L_1=2>s-1$ initial tokens. The $(1,2)$ row has six positive internal bispecial tokens.

| Language | $N$ | Weights | Leaf sum | Token bound | Clipped sum | IET ceiling | Positive tokens |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Three-interval exchange | 20 | (1, 2, 200) | 205 | 241 | 25 | 97 | 0 |
| Three-interval exchange | 20 | (1, 2, 500) | 505 | 541 | 25 | 97 | 0 |
| Arnoux–Rauzy | 20 | (1, 2, 200) | 211 | 241 | 31 | 97 | 0 |
| Arnoux–Rauzy | 20 | (1, 2, 500) | 511 | 541 | 31 | 97 | 0 |
| Reverse three-interval exchange | 20 | (19, 20, 20) | 97 | 97 | 97 | 97 | 0 |
| Thue–Morse | 20 | (19, 19) | 76 | 76 | 76 | 58 | 0 |
| Thue–Morse | 20 | (1, 2) | 61 | 155 | 61 | 58 | 6 |

In the column table the observed count is the maximum over the sampled pieces of each indicated dictionary. The one-letter rows use the doubled block from Theorem 2.3.

| Projected piece | $W$ | Maximum observed | Column bound |
| --- | --- | --- | --- |
| Three multi-run blocks | 10 | 29 | 117 |
| Three multi-run blocks | 35 | 71 | 417 |
| Three cross-ray blocks | 10 | 39 | 87 |
| Three cross-ray blocks | 35 | 128 | 312 |
| Ray $(2,3)$, sizes $(1,2,200)$ | 10 | 38 | 87 |
| Ray $(2,3)$, sizes $(1,2,200)$ | 35 | 138 | 312 |
| Ray $(3,5)$, sizes $(1,2,200)$ | 10 | 37 | 96 |
| Ray $(3,5)$, sizes $(1,2,200)$ | 35 | 138 | 346 |
| One halving | 2 | 3 | 3 |
| One halving | 12 | 13 | 13 |
| Long runs | 2 | 4 | 4 |
| Long runs | 12 | 24 | 24 |
| Two halvings | 2 | 4 | 4 |
| Two halvings | 12 | 14 | 24 |

![Clipped stopping-tree weights and factor counts of projected interval-exchange pieces](supplement/figure-1.png)

**Figure 1.** Panel (a) divides the clipped first-letter mass by $(2s-1)N-s$. The reverse interval exchanges attain one, while Thue–Morse can exceed one. Panel (b) compares the largest observed parity factor counts with the lengths-$W$ column bounds and shows the two one-letter equality curves.

## 3. Universal Perturbed Mechanical Windows: Single-Logarithm Upper Law and Index-0 Sharpness


Fix a primitive ray $(a, p)$ ($\gcd(a, p) = 1$, $p > a \ge 1$), window length $W \ge 1$, put $N := 2 + \lfloor W / a \rfloor \ge 2$, and fix an integer $t \ge 0$. Let $\mathcal{W}_t(a, p; W) \subset \{O, E\}^W$ denote the set of binary words of length $W$ containing $E$ that occur as the length-$W$ prefix of $F_{k_0} F_{k_1} \cdots$ with $F_k = O^{ka} E^{k(p-a)}$ and $k_i = k_- + (k_+ - k_-)\tilde{b}_i$, for some integers $1 \le k_- < k_+$, some lower or upper mechanical binary word $(b_i)_{i \ge 0}$ ($\alpha \in [0, 1]$, $\rho \in \mathbb{R}$), and some binary sequence $(\tilde{b}_i)_{i \ge 0}$ differing from $(b_i)_{i \ge 0}$ at **at most $t$ indices** ($\#\{i \ge 0 : \tilde{b}_i \ne b_i\} \le t$). Let $\mathcal{W}_t^{\mathrm{head}}(a, p; W) \subset \mathcal{W}_t(a, p; W)$ denote the subset realizable with $\tilde{b}_0 \ne b_0$ (an index-$0$ flip), and write $k(w) \in \{1, \dots, N - 2\}$ for the initial odd-run length of $w$ divided by $a$.

### 3.1 Constrained mechanical words

**Lemma 3.1 (Constrained Arrangement Bound).** *For every integer $n \ge 1$ and real $u \in (0, 1/2]$, let $A(n, u)$ be the number of distinct length-$n$ mechanical binary words (lower or upper, any $\rho \in \mathbb{R}$) with slope $\alpha \in [0, 2u]$, and let $H(n, u)$ be the number of those words starting with $b_0 = 1$. Then*
$$
A(n, u) \le 4n + 4 u n^3, \qquad H(n, u) \le 4n + 8 u n^2 + 32 u^2 n^3.
\tag{3.1}
$$

*Proof.* Slopes $\alpha \in \{0, 1\}$ contribute at most $2$ constant words ($0^n$ and $1^n$, only $1^n$ starting with $1$, and $\alpha = 1 \notin [0, 2u]$ unless $u = 1/2$). Every length-$n$ upper mechanical prefix with $0<\alpha<1$ equals a lower mechanical prefix of that length. Shift the intercept downward by $0<\delta<\min(\{\{e\alpha+\rho\}:0\le e\le n,\ \{e\alpha+\rho\}>0\}\cup\{1\})$ and normalize modulo $1$. The new floors equal the old ceilings minus one, up to the common integer shift from normalization, so their consecutive differences agree. Write the resulting lower word as $b_e=\lfloor(e+1)\alpha+\rho\rfloor-\lfloor e\alpha+\rho\rfloor$ with $\rho\in[0,1)$. Set $b:=\min(4u,1)$ and $y:=\alpha\in(0,b)$. Choose $0<\varepsilon'<\min_{0\le e\le n}(1-\{e\alpha+\rho\})$ and set $x:=1-\rho-\varepsilon'\in(0,1)$. For all $0\le e\le n$, including when $\rho=0$, we have $\lfloor x-ey\rfloor=-\lfloor e\alpha+\rho\rfloor$. The strict choice puts $(x,y)$ inside an open cell and gives $1-b_e=1+\lfloor x-(e+1)y\rfloor-\lfloor x-ey\rfloor$. Since $\lfloor x \rfloor = 0$, the word $(b_0, \dots, b_{n-1})$ is uniquely determined by $(\lfloor x - e y \rfloor)_{1 \le e \le n}$ with $(x, y) \in (0, c) \times (0, b)$, where $c = 1$ in general, and $c = b$ whenever $b_0 = 1$ (since $b_0 = 1 \iff \alpha + \rho \ge 1 \implies 0 < x < 1 - \rho \le \alpha < b$).
By [1] Lemma 6.2, the number of open arrangement cells of $\{x = e y - f : 1 \le e \le n,\ f \in \mathbb{Z}_{\ge 0}\}$ in $(0, c) \times (0, b)$ is at most
$$
1 + \sum_{j=1}^n \sum_{\substack{0 \le i < j,\ \gcd(i,j)=1 \\ i/j < b}} \#\bigl\{e : j \le e \le n,\ \{e i / j\} < c\bigr\}.
$$
At $j = 1$, only $i = 0$ occurs, contributing $n$. For $2 \le j \le n$, $\gcd(i, j) = 1$ excludes $i = 0$, leaving at most $\lfloor b j \rfloor \le b j$ numerators $i \ge 1$.
- For $c = 1$: each $(j, i)$ has $n - j + 1 \le n$ values of $e$, giving $\sum_{j=2}^n (b j) n = b n \frac{n(n+1)-2}{2} \le b n^3 \le 4 u n^3$. Adding the $\le 2$ boundary-slope words gives $A(n, u) \le 2 + 1 + n + 4 u n^3 \le 4n + 4 u n^3$ ($n \ge 1$).
- For $c = b$: as $e$ runs over a period of length $j$, $\{e i / j\}$ visits $\{0, 1/j, \dots, (j-1)/j\}$ once each, hitting $[0, b)$ at most $\lceil b j \rceil \le b j + 1$ times. Since $[j, n]$ is covered by $\lceil (n - j + 1)/j \rceil \le \lfloor n/j \rfloor + 1 \le \frac{2n}{j}$ periods ($j\le n$), summing over $2 \le j \le n$ gives
  $$
  \sum_{j=2}^n (b j)\cdot \frac{2n}{j}\cdot(b j + 1) = 2b n(n - 1) + b^2 n\bigl(n(n+1) - 2\bigr) \le 2b n^2 + 2b^2 n^3 \le 8u n^2 + 32 u^2 n^3.
  $$
  Adding $2 + 1 + n \le 4n$ yields $H(n, u) \le 4n + 8 u n^2 + 32 u^2 n^3$. $\square$

### 3.2 Weighted window laws

**Theorem 3.2 (Explicit Single-Logarithm $t$-Flip Window Law and Index-$0$ Sharpness).**
1. *(Single-logarithm upper bound for every $t \ge 1$, improving [1] Remark 6.3 by $\ln(2N)$.)* For every integer $t \ge 1$, ray $(a, p)$, and $W \ge 1$ ($N = 2 + \lfloor W / a \rfloor \ge 2$),
   $$
   \sum_{w \in \mathcal{W}_t^{\mathrm{head}}(a, p; W)} k(w) \le C_t^{\mathrm{head}}\, N^{3+t}, \qquad
   \sum_{w \in \mathcal{W}_t(a, p; W)} k(w) \le C_t\, N^{3+t}\ln(2N),
   \tag{3.2}
   $$
   with explicit closed-form constants $C_t^{\mathrm{head}} := 60 t (2t + 8)^{t+2}$ and $C_t := 750(t + 1)(2t + 8)^{t+3}$. The double-logarithm upper law for $t=0$ follows from [1].
2. *(Matching $\Omega_t(N^{3+t})$ lower bound via index-$0$ head-up flips.)* For every integer $t \ge 1$, ray $(a, p)$, and $W \ge 16(t + 2)p$, setting $L := \lfloor \frac{W}{8(t + 2)p} \rfloor \ge 2$, there exist at least $L^3 \binom{L - 1}{t - 1}$ pairwise distinct windows in $\mathcal{W}_t^{\mathrm{head}}(a, p; W)$, each with $k(w) \ge L$, satisfying
   $$
   \sum_{w \in \mathcal{W}_t^{\mathrm{head}}(a, p; W)} k(w) \ge L^4 \binom{L - 1}{t - 1} \ge c_t\, N^{3+t}
   \tag{3.3}
   $$
   for sufficiently large $W$, with an explicit constant $c_t>0$ depending on the fixed ray.
3. *(Upgraded [1] Theorem C (6.1) and $1$-flip Corollary D.)* For $t\ge1$, on every positive-integer path of class (C), simple (P), or (D), the total odd mass $M_t$ of complete valley blocks starting $t$-flip fitting windows of length $W = \lceil C_W S \rceil$ satisfies
   $$
   M_t \ll_t S^{\sigma_t}(\ln 2S)^{\kappa_t}, \qquad \sigma_t := \frac{(3 + t)\beta + 5 + 2t}{\beta + 3 + t}, \qquad \kappa_t := \frac{\beta + 1}{\beta + 3 + t}
   \tag{3.4}
   $$
   ($\sigma_1=\frac{23464804}{8116201}\in[2.891106812,2.891106813]<3$ and $\kappa_1=\frac{5116201}{8116201}\in[0.630368937,0.630368938]$ at $\beta=4.116201$ under (BLS), and $\sigma_1^{(\mathrm R)}=\frac{602}{173}\in[3.479768786,3.479768787]$ and $\kappa_1^{(\mathrm R)}=\frac{143}{173}\in[0.826589595,0.826589596]$ at $\beta=13.3$ under Rhin). In particular, under (BLS) and $V\le c q^{1/3}$ on (C) or simple (P), there exist $\gg q^{2/3}$ pairwise disjoint aligned stretches of $O(S)$ steps whose multiplicity sequences cannot even be realized by any two-size mechanical order with one flipped block.

*Proof.*
1. **Clipping:** Any $w \in \mathcal{W}_t(a, p; W)$ contains $E$, so $k_0 a < W < (N - 1)a$, forcing $k_- \le k_0 \le N - 2$. Replacing $k_+$ by $\min(k_+, N)$ preserves $1 \le k_- < \tilde{k}_+ \le N$: if $k_+ > N$, then before the first index $i_* \ge 1$ with $\tilde{b}_{i_*} = 1$ (notice $i_* = 0$ would give $w = O^W \notin \mathcal{W}_t$) all blocks have size $k_-$, while at $i_*$ both $F_{k_+}$ and $F_N$ start with $\ge N a > W$ $O$'s, producing identical length-$W$ prefixes. Thus assume $1 \le k_- < k_+ \le N$.

   **Dyadic bands & padding:** Let $J := \lceil \log_2 N \rceil \ge 1$. Cover $[0, 1]$ by $B_0 := [0, u_0]$ ($u_0 := 2^{-J} \in (\frac{1}{2N}, \frac{1}{N}]$) and $B_j := [u_j, 2u_j]$ ($u_j := 2^{-j}$, $1 \le j \le J$; note $B_j \subset [0, 2u_j]$ and $u_j \le 1/2$ for all $0 \le j \le J$). Fix $(j, k_-, k_+)$, put $u := u_j$, $D := k_- + u k_+ > 1$, and set
   $$
   n := \left\lceil \frac{2(t + 3)N}{D} \right\rceil.
   $$
   Since $D \le N + \frac{1}{2}N < 2(t + 3)N$, we have $2 \le \frac{2(t+3)N}{D} \le n < \frac{(2t + 8)N}{D}$. Let $\tilde{r} := \sum_{i=0}^{n-1} \tilde{b}_i \ge 0$.
   - On $B_0$ ($u_0 \le 1/N$): $u_0 k_+ \le 1 \le k_- \implies k_- \ge D/2$, so $\sum_{i=0}^{n-1} k_i \ge n k_- \ge \frac{n D}{2} \ge (t + 3)N > N$.
   - On $B_j$ ($1 \le j \le J$, $\alpha \ge u$): the unflipped mechanical word satisfies $\sum_{i=0}^{n-1} b_i > n\alpha - 1 \ge n u - 1$, so $\tilde{r} \ge \max(0, n u - (t + 1)) \ge n u - (t + 1)$. Since $k_+ - k_- > 0$ and $1 - u \ge 1/2$,
     $$
     \sum_{i=0}^{n-1} k_i \ge n k_- + (k_+ - k_-)\bigl(n u - (t + 1)\bigr) = n\bigl((1 - u)k_- + u k_+\bigr) - (t + 1)(k_+ - k_-) \ge \frac{n D}{2} - (t + 1)N \ge 2N > N.
     $$
   Hence $p\sum_{i=0}^{n-1} k_i > p N > a(N - 1) > W$ in every band, so $w$ and $k(w)$ are uniquely determined by $(k_-, k_+)$ and $(\tilde{b}_0, \dots, \tilde{b}_{n-1})$.

   **Dyadic summation before $(k_-, k_+)$ summation:** Fix real $1 \le k_- < k_+ \le N$ and integer $m \ge 3$. Splitting $\{u_1, \dots, u_J\}$ at $k_- / k_+ \in (0, 1)$ gives
   $$
   \sum_{j=1}^J \frac{u_j}{(k_- + u_j k_+)^m} \le \frac{1}{k_-^m}\sum_{u_j \le k_-/k_+} u_j + \frac{1}{k_+^m}\sum_{u_j > k_-/k_+} u_j^{-(m-1)} \le \frac{2}{k_-^{m-1}k_+} + \frac{2^{m-1}}{(2^{m-1}-1)k_-^{m-1}k_+} \le \frac{10/3}{k_-^{m-1}k_+},
   $$
   and adding $j = 0$ ($u_0 = u_J \le k_- / k_+$ since $u_0 k_+ \le 1 \le k_-$, adding at most $\frac{1}{k_-^m} u_0 \le \frac{1}{k_-^{m-1} k_+}$.) gives
   $$
   \sum_{j=0}^J \frac{u_j}{(k_- + u_j k_+)^m} \le \frac{13/3}{k_-^{m-1} k_+} < \frac{5}{k_-^{m-1} k_+} \qquad (m \ge 3).
   \tag{3.5}
   $$
   Likewise, for $m \ge 4$,
   $$
   \sum_{j=1}^J \frac{u_j^2}{(k_- + u_j k_+)^m} \le \frac{1}{k_-^m}\sum_{u_j \le k_-/k_+} u_j^2 + \frac{1}{k_+^m}\sum_{u_j > k_-/k_+} u_j^{-(m-2)} \le \frac{4/3}{k_-^{m-2}k_+^2} + \frac{4/3}{k_-^{m-2}k_+^2} = \frac{8/3}{k_-^{m-2}k_+^2},
   $$
   and adding $j = 0$ ($u_0 \le k_- / k_+$ adds $\le \frac{1}{k_-^{m-2}k_+^2}$) gives
   $$
   \sum_{j=0}^J \frac{u_j^2}{(k_- + u_j k_+)^m} \le \frac{11/3}{k_-^{m-2} k_+^2} < \frac{4}{k_-^{m-2} k_+^2} \qquad (m \ge 4).
   \tag{3.6}
   $$
   Also note $J + 1 = \lceil \log_2 N \rceil + 1 \le \frac{\ln N}{\ln 2} + 2 < 3\ln(2N)$ for all $N \ge 2$, $\sum_{k=1}^\infty k^{-2} = \frac{\pi^2}{6} < 2$, and $\sum_{k=2}^N \frac{1}{k} < \ln N < \ln(2N)$.

   - **Head-flipped words ($\tilde{b}_0 = 1 - b_0$, $t \ge 1$):** There are $\sum_{s=0}^{t-1} \binom{n-1}{s} \le t n^{t-1}$ choices for the $\le t - 1$ remaining flip indices in $\{1, \dots, n - 1\}$. Every resulting word has weight $\le k_+$, so Lemma 3.1 (3.1) bounds the $(j, k_-, k_+)$ contribution by
     $$
     t n^{t-1} k_+ A(n, u_j) \le 4 t k_+ n^t + 4 t k_+ u_j n^{t+2} < 4t(2t + 8)^{t+2} N^{t+2}\Biggl(\frac{k_+}{N^2(k_- + u_j k_+)^t} + \frac{k_+ u_j}{(k_- + u_j k_+)^{t+2}}\Biggr).
     $$
     For the first term, $\sum_{k_+=2}^N k_+\le3N^2/4$ and $\sum_{k=1}^{N-1}k^{-t}\le1+\ln N\le(3/2)\ln(2N)$. Thus the summed term is at most $(27/8)\ln^2(2N)<4N$, since the maximum of $\ln^2(2x)/x$ over $x\ge2$ is $8/e^2<32/27$. For the second term ($m=t+2\ge3$), (3.5) gives $\sum_{k_+=2}^N \sum_{k_-=1}^{k_+-1} k_+ \frac{5}{k_-^{t+1} k_+} < 5 N \sum_{k_-=1}^\infty k_-^{-2} < 10 N$. Adding $4N+10N=14N<15N$ and multiplying by $4t(2t + 8)^{t+2} N^{t+2}$ yields $\sum_{w \in \mathcal{W}_t^{\mathrm{head}}} k(w) \le 60 t (2t + 8)^{t+2} N^{3+t}$.

   - **Non-head-flipped words ($\tilde{b}_0 = b_0$, $t \ge 1$):** There are $\sum_{s=0}^t \binom{n-1}{s} \le (t + 1)n^t$ choices of flip positions in $\{1, \dots, n - 1\}$, and each word carries weight $k_-$ (if $b_0 = 0$) or $k_+$ (if $b_0 = 1$). By (3.1), the $(j, k_-, k_+)$ contribution is at most
     $$
     (t + 1)n^t\bigl(k_- A(n, u_j) + k_+ H(n, u_j)\bigr) \le (t + 1)\Bigl(4(k_- + k_+) n^{t+1} + 4 k_- u_j n^{t+3} + 8 k_+ u_j n^{t+2} + 32 k_+ u_j^2 n^{t+3}\Bigr).
     $$
     Substitute $n < \frac{(2t + 8)N}{k_- + u_j k_+}$ and sum over $j = 0, \dots, J$ and $1 \le k_- < k_+ \le N$:
     - $4(k_- + k_+) n^{t+1} < 8 k_+ \frac{(2t+8)^{t+1} N^{t+1}}{k_-^{t+1}}$: summed over $j, k_-, k_+$ gives $< 8(2t+8)^{t+1} N^{t+1} (3\ln 2N) \frac{3N^2}{4}\cdot 2=36(2t+8)^{t+1} N^{t+3}\ln(2N) < (2t+8)^{t+3} N^{t+3}\ln(2N)$ (since $(2t+8)^2 \ge 100>36$);
     - $4 k_- u_j n^{t+3}$ ($m=t+3\ge4$): by (3.5), $< 4(2t+8)^{t+3} N^{t+3} \sum_{k_- < k_+} \frac{5}{k_-^{t+1} k_+} < 20(2t+8)^{t+3} N^{t+3} (2 \ln 2N) = 40(2t+8)^{t+3} N^{t+3}\ln(2N)$;
     - $8 k_+ u_j n^{t+2}$ ($m=t+2\ge3$): by (3.5), $< 8(2t+8)^{t+2} N^{t+2} \sum_{k_- < k_+} \frac{5}{k_-^{t+1}} < 80(2t+8)^{t+2} N^{t+3} \le 8(2t+8)^{t+3} N^{t+3}\ln(2N)$;
     - $32 k_+ u_j^2 n^{t+3}$ ($m=t+3\ge4$): by (3.6), $< 32(2t+8)^{t+3} N^{t+3} \sum_{k_- < k_+} \frac{4}{k_-^{t+1} k_+} < 256(2t+8)^{t+3} N^{t+3}\ln(2N)$.
     Adding these ($1 + 40 + 8 + 256 = 305$) plus the head-flipped bound $60 t(2t+8)^{t+2} N^{t+3} < 6(t+1)(2t+8)^{t+3} N^{t+3}\ln(2N)$ gives $< 311(t + 1)(2t + 8)^{t+3} N^{3+t}\ln(2N) < 750(t + 1)(2t + 8)^{t+3} N^{3+t}\ln(2N)$, proving (3.2).

2. **Index-$0$ sharpness:** Let $L := \lfloor \frac{W}{8(t + 2)p} \rfloor \ge 2$. Choose $k_- = 1$, any $k_+ \in [L, 2L)$ ($L$ choices), any $j \in [(t + 1)L, (t + 2)L)$ ($L$ choices), any $d \in [(2t + 2)L, (2t + 3)L)$ ($L$ choices), and any $(t - 1)$-subset $S_{\mathrm{int}} \subset \{1, 2, \dots, L - 1\}$ ($\binom{L - 1}{t - 1}$ choices). Take the rational lower mechanical word $(b_i)_{i \ge 0}$ with slope $\alpha = 1/d$ and intercept $\rho = \frac{d - j - 1}{d}$: since $\lfloor (i + 1)/d + (d - j - 1)/d \rfloor = \lfloor \frac{i + d - j}{d} \rfloor$, we have $b_i = 1 \iff i \equiv j \pmod d$, so inside $[0, j + d]$ the unique $1$'s of $(b_i)$ lie at $i = j$ and $i = j + d$ (and $b_0 = 0$). Flip index $0$ ($0 \mapsto 1$) and the $t - 1$ indices in $S_{\mathrm{int}}$ ($0 \mapsto 1$). In the resulting sequence $(\tilde{b}_i)$, the first $t + 2$ occurrences of $1$ lie at $0$, the $t - 1$ elements of $S_{\mathrm{int}} \subset [1, L - 1]$, $j \in [(t + 1)L, (t + 2)L)$, and $j + d \in [(3t + 3)L, (3t + 5)L)$. The shortcut duration through block $j + d$ (inclusive) is
   $$
   p\Bigl((j + d + 1 - (t + 2))\cdot 1 + (t + 2) k_+\Bigr) < p\Bigl((3t + 5)L + (t + 2)(2L)\Bigr) = (5t + 9)p L < 8(t + 2)p L \le W.
   $$
   Hence all blocks through $j + d$ (plus the start of block $j + d + 1$) are completely visible inside the length-$W$ parity window $w$, allowing unique recovery of $k_+ = k(w)$ from block $0$, $S_{\mathrm{int}}$ from blocks $1, \dots, L - 1$, $j$ from the $(t + 1)$-st block of size $k_+$, and $j + d$ from the $(t + 2)$-nd block of size $k_+$. Thus all $L^3 \binom{L - 1}{t - 1}$ windows lie in $\mathcal{W}_t^{\mathrm{head}}(a, p; W)$, are pairwise distinct, and satisfy $k(w) = k_+ \ge L$, proving (3.3). For $L\ge\max(2,2(t-1))$, $\binom{L-1}{t-1}\ge(L/2)^{t-1}/(t-1)!$. Since $L\ge W/(16(t+2)p)$ and $N\le2W/a$, one can take $c_t=(a/(32(t+2)p))^{3+t}/(2^{t-1}(t-1)!)$.

3. **Derivation of (3.4).** Proposition 3.4 of [1] gives $\sum_{\mathrm{blocks}}|d-r\theta|\ll S$. If $M_t\ll S$, the result follows. Otherwise, at least half of $M_t$ comes from rays with $|p/a-\theta|\le C S/M_t$ by weighting this defect budget by the odd counts $r$. The linear-form bound gives $a\gg A_0=(M_t/S)^{1/(\beta+1)}$ on these rays. Distinct reduced fractions with $A\le a<2A$ are spaced by at least $1/(4A^2)$, so at most $O(1+A^2 S/M_t)$ lie in each band. Parity injectivity and (3.2) bound the contribution per ray by $O_t(S^{3+t}a^{-(2+t)}\ln(2S))$, since $a\ll S$. Summing the dyadic bands gives
   $$
   M_t \ll_t S^{3+t}(\ln 2S) \sum_{A \gg A_0} \Bigl(A^{-(2+t)} + A^{-t}\frac{S}{M_t}\Bigr) \ll_t S^{3+t}(\ln 2S)\Biggl[\Bigl(\frac{S}{M_t}\Bigr)^{\frac{2+t}{\beta+1}} + \Bigl(\frac{S}{M_t}\Bigr)^{1 + \frac{t}{\beta+1}}\Biggr],
   $$
   where the first bracketed term dominates ($M_t^{1 + \frac{2+t}{\beta+1}} \ll_t S^{3+t+\frac{2+t}{\beta+1}}\ln(2S)$), giving $\sigma_t = \frac{(3+t)(\beta+1)+2+t}{\beta+3+t} = \frac{(3+t)\beta+5+2t}{\beta+3+t}$ and $\kappa_t = \frac{\beta+1}{\beta+3+t}$. For $t = 1$ under (BLS), $\sigma_1=23464804/8116201<3$, so under $V \le c q^{1/3}$ ($S \ll q^{1/3}$), $M_1 = o(q / \ln q)$, and greedy selection on the dominant convergent ray of [1] Theorem A produces $\gg q / S \gg q^{2/3}$ pairwise disjoint $1$-flip-nonfitting witnesses of $O(S)$ steps. $\square$

### 3.3 Exact mechanical window catalogs

Each count and weight tuple is ordered as all windows, windows admitting a flip at index zero, and windows admitting a $0\mapsto1$ flip at index zero. The same parity word may have several realizations and contributes once to each applicable set.

| Ray | $W$ | $N$ | $t$ | Distinct words | Weight sums |
| --- | --- | --- | --- | --- | --- |
| (1, 2) | 6 | 8 | 0 | (10, 0, 0) | (21, 0, 0) |
| (1, 2) | 8 | 10 | 0 | (22, 0, 0) | (49, 0, 0) |
| (1, 2) | 10 | 12 | 0 | (41, 0, 0) | (96, 0, 0) |
| (1, 2) | 12 | 14 | 0 | (70, 0, 0) | (169, 0, 0) |
| (1, 2) | 6 | 8 | 1 | (10, 10, 5) | (21, 21, 16) |
| (1, 2) | 8 | 10 | 1 | (22, 22, 9) | (49, 49, 34) |
| (1, 2) | 10 | 12 | 1 | (42, 41, 16) | (97, 96, 65) |
| (1, 2) | 12 | 14 | 1 | (74, 69, 25) | (174, 168, 110) |
| (1, 2) | 6 | 8 | 2 | (10, 10, 5) | (21, 21, 16) |
| (1, 2) | 8 | 10 | 2 | (22, 22, 9) | (49, 49, 34) |
| (1, 2) | 10 | 12 | 2 | (42, 42, 16) | (97, 97, 65) |
| (2, 3) | 6 | 5 | 0 | (3, 0, 0) | (4, 0, 0) |
| (2, 3) | 8 | 6 | 0 | (5, 0, 0) | (8, 0, 0) |
| (2, 3) | 10 | 7 | 0 | (9, 0, 0) | (16, 0, 0) |
| (2, 3) | 12 | 8 | 0 | (17, 0, 0) | (32, 0, 0) |
| (2, 3) | 6 | 5 | 1 | (3, 3, 1) | (4, 4, 2) |
| (2, 3) | 8 | 6 | 1 | (5, 5, 2) | (8, 8, 5) |
| (2, 3) | 10 | 7 | 1 | (9, 9, 4) | (16, 16, 11) |
| (2, 3) | 12 | 8 | 1 | (17, 17, 7) | (32, 32, 21) |
| (2, 3) | 6 | 5 | 2 | (3, 3, 1) | (4, 4, 2) |
| (2, 3) | 8 | 6 | 2 | (5, 5, 2) | (8, 8, 5) |
| (2, 3) | 10 | 7 | 2 | (9, 9, 4) | (16, 16, 11) |
| (3, 5) | 6 | 4 | 0 | (1, 0, 0) | (1, 0, 0) |
| (3, 5) | 8 | 4 | 0 | (2, 0, 0) | (3, 0, 0) |
| (3, 5) | 10 | 5 | 0 | (4, 0, 0) | (7, 0, 0) |
| (3, 5) | 12 | 6 | 0 | (5, 0, 0) | (8, 0, 0) |
| (3, 5) | 6 | 4 | 1 | (1, 1, 0) | (1, 1, 0) |
| (3, 5) | 8 | 4 | 1 | (2, 2, 1) | (3, 3, 2) |
| (3, 5) | 10 | 5 | 1 | (4, 4, 2) | (7, 7, 5) |
| (3, 5) | 12 | 6 | 1 | (5, 5, 2) | (8, 8, 5) |
| (3, 5) | 6 | 4 | 2 | (1, 1, 0) | (1, 1, 0) |
| (3, 5) | 8 | 4 | 2 | (2, 2, 1) | (3, 3, 2) |
| (3, 5) | 10 | 5 | 2 | (4, 4, 2) | (7, 7, 5) |

The rational values and outward enclosures for (3.4) use the two linear-forms inputs at their stated exponents.

| Input | $\beta$ | $t$ | $\sigma_t$ | $\kappa_t$ |
| --- | --- | --- | --- | --- |
| BLS | 4.116201 | 1 | $\frac{23464804}{8116201} \in [2.891106812, 2.891106813]$ | $\frac{5116201}{8116201} \in [0.630368937, 0.630368938]$ |
| BLS | 4.116201 | 2 | $\frac{29581005}{9116201} \in [3.244882928, 3.244882929]$ | $\frac{5116201}{9116201} \in [0.561220732, 0.561220733]$ |
| Rhin | 13.3 | 1 | $\frac{602}{173} \in [3.479768786, 3.479768787]$ | $\frac{143}{173} \in [0.826589595, 0.826589596]$ |
| Rhin | 13.3 | 2 | $\frac{755}{183} \in [4.125683060, 4.125683061]$ | $\frac{143}{183} \in [0.781420765, 0.781420766]$ |

## 4. Primitive-Root Superblock Cycle Clamping and Integer Exclusion of Rational Control Families


Let $\Sigma = \{G_1, \dots, G_s\} \subset \{O, E\}^+$ ($s \ge 2$) be any **prefix-free** dictionary of non-empty binary superblocks ($G_i$ is not a prefix of $G_j$ for $i \ne j$), with shortcut lengths $D_c := |G_c|$, $D_{\min} := \min_c D_c$, $D_{\max} := \max_c D_c$, odd counts $R_c := |G_c|_O$, $R_{\max} := \max_c R_c$, and block slope-changes $\delta_c := R_c \theta - D_c$. Define the dictionary boundary constants
$$
\Gamma_{\mathrm{pre}} := \max_{1 \le c \le s}\ \max_{0 \le j \le D_c} \bigl(|(G_c)_{[0:j)}|_O \theta - j\bigr), \qquad
\Gamma_{\mathrm{suf}} := \max_{1 \le c \le s}\ \max_{0 \le j \le D_c} \bigl(|(G_c)_{[j:D_c)}|_O \theta - (D_c - j)\bigr),
$$
$$
\Gamma_{\mathrm{int}} := \max_{1 \le c \le s}\ \max_{0 \le i \le j \le D_c} \bigl(|(G_c)_{[i:j)}|_O \theta - (j - i)\bigr).
\tag{4.1}
$$
The three maxima are nonnegative because they include empty subwords.

For any word $U_0 \in \Sigma^{m_0}$ ($m_0 \ge 1$) with falling total slope $\sum_{r=0}^{m_0-1} \delta_{(U_0)_r} < 0$ (i.e., $2^{|\Psi(U_0)|} > 3^{|\Psi(U_0)|_O}$), define its **cyclic block-slope excess**
$$
B_{\mathrm{disc}}(U_0) := \max_{0\le a<m_0,\ 0\le h\le m_0}\sum_{r=a}^{a+h-1} \delta_{(U_0^2)_r} \quad (\text{over all } u \in \mathcal{L}(U_0^\infty)\text{ of length } 0 \le |u| \le m_0).
\tag{4.2}
$$
If $U_0^\infty$ is $c$-balanced on $s = 2$ letters ($c \ge 1$), so every factor $u \in \mathcal{L}_n(U_0^\infty)$ has $||u|_1 - n \frac{|U_0|_1}{m_0}| \le c$, then because $\delta_{G_1} |U_0|_1 + \delta_{G_2} |U_0|_2 < 0$, every $u \in \mathcal{L}_n(U_0^\infty)$ ($0 \le n \le m_0$) satisfies
$$
\sum_{r=0}^{n-1} \delta_{u_r} = \frac{n}{m_0}\bigl(|U_0|_1 \delta_{G_1} + |U_0|_2 \delta_{G_2}\bigr) + \left(|u|_1 - \frac{n}{m_0}|U_0|_1\right)(\delta_{G_1} - \delta_{G_2}) \le c\, |\delta_{G_1} - \delta_{G_2}|.
\tag{4.3}
$$

Eliahou’s lower bound [23] gives the shortcut-period threshold used below. Hercher [24] bounds the number of odd-run groups.

**Theorem 4.1 (Universal Superblock Cycle Complexity–Discrepancy Clamping).** *Let $\Sigma = \{G_1, \dots, G_s\} \subset \{O, E\}^+$ be prefix-free, and suppose $U \in \Sigma^m$ ($m \ge 1$, with primitive superblock root $U_0 \in \Sigma^{m_0}$, $U = U_0^{d'}$) has $\Psi(U)$ realized by a nontrivial positive-integer Collatz cycle $C \subset \mathbb{Z}_{\ge 3}$ of least shortcut period $K_0$ ($\Psi(U_0) = w_0^d$, $d \ge 1$, $K_0 = |\Psi(U_0)| / d \ge 17{,}087{,}915$). Then:*
1. *(Exact superblock-start injection.)* The $m_0$ superblock start times $0 = T_0 < T_1 < \dots < T_{m_0 - 1} < |\Psi(U_0)|$ of $U_0$ are pairwise incongruent modulo $K_0$, and hence visit $m_0$ **pairwise distinct** positive integers on $C$.
2. *(Explicit height & complexity clamping.)* Every factor $z \in \mathcal{L}(w_0^\infty) = \mathcal{L}(\Psi(U_0)^\infty)$ satisfies $|z|_O \theta - |z| \le \Gamma(U_0) := \max\bigl(\Gamma_{\mathrm{int}},\ B_{\mathrm{disc}}(U_0) + \Gamma_{\mathrm{pre}} + \Gamma_{\mathrm{suf}}\bigr)$. Consequently, every integer state $x \in C$ satisfies
   $$
   x < X_{\max}(m_0) := 2^{\Gamma(U_0)} (m_0 R_{\max})\left(\frac{1}{3}(m_0 D_{\max})^{13.3} + \frac{1}{2}\right),
   \tag{4.4}
   $$
   and setting $W(m_0) := \lfloor \log_2 X_{\max}(m_0) \rfloor + 1$, the primitive superblock count $m_0$ and least period $K_0$ satisfy **both**
   $$
   m_0 \le p_{U_0^\infty}\!\left(\left\lceil \frac{W(m_0)}{D_{\min}} \right\rceil\right) \qquad\text{and}\qquad K_0 \le p_{\Psi(U_0)^\infty}\!\bigl(W(m_0)\bigr).
   \tag{4.5}
   $$
3. *(Unconditional finiteness up to linear discrepancy slope.)*
   - *($s$-IET / $s$-episturmian superblock schedules up to linear discrepancy):* If $p_{U_0^\infty}(n) \le (s - 1)n + 1$ and $B_{\mathrm{disc}}(U_0) \le \alpha_{\mathrm{disc}} m_0 + \beta_{\mathrm{disc}}$ with $\alpha_{\mathrm{disc}} < \frac{D_{\min}}{s - 1}$, then (4.5) forces an explicit upper bound $m_0 \le m_{\max}(\Sigma, \alpha_{\mathrm{disc}}, \beta_{\mathrm{disc}})$. In particular, for a binary superblock schedule with both $p_{U_0^\infty}(n)\le n+1$ and count discrepancy at most $c$, $B_{\mathrm{disc}}(U_0) \le c|\delta_{G_1} - \delta_{G_2}|$ is bounded independently of $m_0$, clamping $m_0$ to a tiny explicit integer.
   - *($t$-flip fixed-slope & refitted-slope schedules):* If $U_0^\infty$ is obtained by at most $t$ symbol flips per window from a fixed-slope mechanical word ($p_{U_0^\infty}(n) \le (n + 1)\sum_{r=0}^t \binom{n}{r}$) or universal refitted-slope mechanical word ($p_{U_0^\infty}(n) \le (n + 1)^3 \sum_{r=0}^t \binom{n}{r}$) and $B_{\mathrm{disc}}(U_0)\le A\ln(2m_0)+B$ for supplied constants $A,B\ge0$, then $W(m_0)=O(\ln(2m_0))$ while $p_{U_0^\infty}(\lceil W(m_0)/D_{\min} \rceil) = O_t((\ln m_0)^{3+t})$, again clamping $m_0 \le m_{\max}$ explicitly.
4. *Certified exclusions.* The table below gives ceilings for six dictionaries under the listed complexity and discrepancy assumptions.

*Proof.*
1. Equal infinite parity tails force the corresponding integer states to be congruent modulo $2^W$ for every $W\ge1$, by the affine parity lemma in Theorem 2.5. Thus the states are equal, and the least state period is the least parity period $K_0$ of the primitive binary root $w_0$. Suppose $T_i \equiv T_{i'} \pmod{K_0}$ for some $0 \le i < i' < m_0$. Since $\Psi(U_0) = w_0^d$ has period $K_0$, the infinite binary tails starting at $T_i$ and $T_{i'}$ in $\Psi(U_0^\infty)$ are equal: $\Psi(u_i u_{i+1} \cdots) = \Psi(u_{i'} u_{i'+1} \cdots)$ where $u_r := (U_0^\infty)_r$. Because $\Sigma$ is prefix-free, unique left-to-right prefix decoding forces $u_{i + t} = u_{i' + t}$ for all $t \ge 0$. Hence $U_0 \in \Sigma^{m_0}$ is periodic with period $\gcd(i' - i, m_0) < m_0$, contradicting primitivity of $U_0$. Since the cycle $C$ has least shortcut period $K_0$, its $K_0$ states around one least lap are pairwise distinct, so $T_0, \dots, T_{m_0 - 1} \bmod K_0$ visit $m_0$ pairwise distinct integers on $C$.
2. Since $2^{K_0} > 3^{q_0}$ ($q_0 \theta - K_0 < 0$), adding full periods of $\Psi(U_0)$ decreases $|z|_O \theta - |z|$, so $\sup_{z \in \mathcal{L}(\Psi(U_0)^\infty)} (|z|_O \theta - |z|)$ is attained on a factor $z$ of $\Psi(U_0^2)$ containing at most $m_0$ complete superblocks. Either $z$ lies entirely inside one superblock $G_c$ ($\le \Gamma_{\mathrm{int}}$), or $z$ decomposes into a suffix of some $G_a$ ($\le \Gamma_{\mathrm{suf}}$), a block factor $u \in \mathcal{L}(U_0^\infty)$ of length $0 \le |u| \le m_0$ ($\le B_{\mathrm{disc}}(U_0)$), and a prefix of some $G_b$ ($\le \Gamma_{\mathrm{pre}}$), proving $|z|_O \theta - |z| \le \Gamma(U_0)$.
   Rotating $w_0$ so $x_0 = x_{\min} \ge 3$, Rhin's bound gives $x_{\min} < \frac{1}{3} q_0 K_0^{13.3}$, and exact affine unrolling $x_t = \frac{3^{r_{0,t}}}{2^t} x_{\min} + \sum_{0 \le i < t,\, (w_0)_i = O} \frac{1}{2}\frac{3^{r_{i+1,t}}}{2^{t - 1 - i}}$ ($1 \le t < K_0$) yields $x_t \le 2^{\Gamma(U_0)}(x_{\min} + \frac{q_0}{2}) < 2^{\Gamma(U_0)} q_0(\frac{1}{3}K_0^{13.3} + \frac{1}{2})$. Since $K_0 = |\Psi(U_0)|/d \le m_0 D_{\max}$ and $q_0 = |\Psi(U_0)|_O / d \le m_0 R_{\max}$ ($d \ge 1$), (4.4) holds for every $x \in C$.
   Consequently, $C \subset [3, 2^{W(m_0)} - 1]$. By the parity lemma in Theorem 2.5, the $K_0$ states of $C$ have $K_0$ pairwise distinct length-$W(m_0)$ parity words in $w_0^\infty = \Psi(U_0)^\infty$, giving $K_0 \le p_{\Psi(U_0)^\infty}(W(m_0))$. Likewise, the $m_0$ distinct states at $T_0, \dots, T_{m_0 - 1}$ have $m_0$ pairwise distinct length-$W(m_0)$ parity words starting at superblock boundaries; since $n := \lceil W(m_0) / D_{\min} \rceil$ superblocks have length $\ge n D_{\min} \ge W(m_0)$ (and prefix-freeness is not even needed in the forward direction $\Sigma^n \to \{O, E\}^{W(m_0)}$, where each $v \in \mathcal{L}_n(U_0^\infty)$ determines a single length-$W(m_0)$ prefix of $\Psi(v)$.), at most $p_{U_0^\infty}(n)$ distinct length-$W(m_0)$ parity words can arise at superblock starts, proving $m_0 \le p_{U_0^\infty}(\lceil W(m_0)/D_{\min} \rceil)$ in (4.5).
3. Let $F(m)$ be a nonnegative, nondecreasing discrepancy envelope for $m\ge1$, with $B_{\mathrm{disc}}(U_0)\le F(m_0)$. Define
   $$
   \bar\Gamma(m)=\max(\Gamma_{\mathrm{int}},\,\Gamma_{\mathrm{pre}}+\Gamma_{\mathrm{suf}}+F(m)),\qquad
   \bar H(m)=\bar\Gamma(m)+\log_2\left((mR_{\max})\left(\tfrac13(mD_{\max})^{13.3}+\tfrac12\right)\right).
   $$
   Then $\log_2 X_{\max}(m_0)\le\bar H(m_0)$. Write $g=\max(\Gamma_{\mathrm{int}},\Gamma_{\mathrm{pre}}+\Gamma_{\mathrm{suf}})$ and $h=\log_2(R_{\max}(\tfrac13D_{\max}^{13.3}+\tfrac12))$. For $m\ge1$ the height term without $\bar\Gamma$ is at most $h+21\ln(2m)$, since its derivative is at most $14.3/(m\ln 2)<21/m$.

   For the linear discrepancy hypothesis choose $F(m)=\alpha m+\max(0,\beta_{\mathrm{disc}})$ with $\alpha=\max(0,\alpha_{\mathrm{disc}})$, and put $\lambda=(s-1)/D_{\min}$. For $s\ge2$, $\lambda\alpha<1$. From (4.5) and $\lceil W/D_{\min}\rceil\le W/D_{\min}+1$ we get
   $$
   (1-\lambda\alpha)m_0\le 21\lambda\ln(2m_0)+s+\lambda\bigl(g+|h|+1+\max(0,\beta_{\mathrm{disc}})\bigr).
   $$
   Using $\ln(2m_0)\le2\sqrt{m_0}$ gives a quadratic bound in $\sqrt{m_0}$. A one-letter dictionary has $m_0=1$.

   For polynomial complexity bounded by $C'n^r$ with $r\ge1$, take $F(m)=A\ln(2m)+B$ with supplied $A,B\ge0$. The required width in superblocks is at most $C_0\ln(2m_0)$, where one may use $C_0=(A+21)/D_{\min}+2(1+(g+|h|+B+1)/D_{\min})$ since $\ln 2>1/2$. The bound $\ln(2m)\le4r\,m^{1/(2r)}$ follows from $\ln x\le x^u/u$ at $x=2m$, $u=1/(2r)$. Therefore $m_0\le C'(4rC_0)^r\sqrt{m_0}$, yielding an explicit ceiling.

   For the numerical tables let $P(n)$ bound the factor complexity and compare $\bar H(P(n))$ with $D_{\min}(n-1)$. If $\bar H(P(n))<D_{\min}(n-1)$, monotonicity rules out the required width $n$ for every $m_0\le P(n)$. For the linear or constant discrepancy envelopes in the table the height derivative along $m=P(n)$ is bounded by $(\alpha+21/P(n))P'(n)$, with $\alpha=0$ for constant discrepancy. For $P(n)=(n+1)^e$ the bounds used are $21e/(n+1)$ and, for $e=1$, $\alpha+21/(n+1)$. For the binary two-flip fixed-slope envelope the bound is $63/n$, since its polynomial has nonnegative coefficients and degree three. The bounds for the upper dictionaries appear in Section 4.1. In every case the derivative bound lies below $D_{\min}$ at the first failing $n$ and decreases thereafter. Thus $m_0\le P(n-1)$ and $K_0\le D_{\max}P(n-1)$. $\square$

### 4.1 Rational controls and exact ceilings

Section 8(b) of [1] verifies finite rational-cycle replays. The asymptotic sub-cubic gain along those families is attributed there to unpublished arguments. For the upper golden control on $(306,485)$ at $B=1$, the target parameters are D = 232, K = 112,526, q = 70,996. Use $\alpha=(\sqrt5-1)/2$, taking each multiplicity as one plus the corresponding mechanical bit. We stop only at a prefix summing to $D$, retaining full blocks. Through depth 144, the possible schedules change only at $\rho_i=\lceil i\alpha\rceil-i\alpha$, including $\rho_0=0$. Checking both rounding conventions at every breakpoint and one interior intercept per open cell yields 56 distinct unclipped words.

| Length | Twos | Ones | Distinct words |
| --- | --- | --- | --- |
| 143 | 89 | 54 | 55 |
| 144 | 88 | 56 | 1 |

The replay range is $\lfloor x_{\min}\rfloor \in [60506, 60939]$. Two length-143 words reproduce Table 2’s 60,529. One is the upper word at $\rho=0$, and the other occurs in the open cell between the breakpoints indexed by $(34,89)$. The length-144 lower word at $\rho=0$ gives 60,939. For every retained schedule, unrolling the affine map through one lap gives its unique rational fixed point, with positive denominator $2^K-3^q$. Checking the parity of each run and taking the minimum over the valleys gives the reported floors.

For the lower dictionary let $F=O^{12}E^7$ and $H=OE$, with blocks $F^{20}H$ and $F^{19}H$. The two zero-slack macroblocks are from [5] Section 6. Their length pairs $(D_{\min},D_{\max})$ are $(363,382)$ and $(16,32)$, respectively. Paper [22] previously replayed the lower control and all three zero-slack controls, including $(2,18)$ as a double traversal. Its exclusion permits unrestricted contracting-stretch count $M_-$ with bounded expanding-stretch count $M_+$. The following ceilings apply to mechanical and one-flip schedules under the stated cyclic hypotheses, which allow unbounded $M_+$.

For the four upper dictionaries, take $(a,p)\in\{(41,65),(306,485)\}$ and $B\in\{1,15\}$. The alternating rise sizes $r_i=3,4,3,4,\dots$ come from the upper controls in [1] Section 8(b). Put
$$
\mathcal D_{\mathrm{meso}}(a,p,B)=\{R_BF_1,R_BF_2,F_1,F_2\},\qquad
R_B=OE\prod_{i=1}^B O^{r_i}E,\qquad F_k=O^{ka}E^{k(p-a)}\quad(k=1,2).
$$
The fused blocks begin with $OE$ and differ at zero-based index $|R_B|+a$, where $R_BF_1$ has $E$ and $R_BF_2$ has $O$. The unfused blocks begin with $OO$ and differ at index $a$. This proves prefix-freeness. The reset lengths are $|R_1|=6$ and $|R_{15}|=2+8\cdot4+7\cdot5=69$, so $D_{\min}=p$ and the four values of $D_{\max}=|R_B|+2p$ are $136,199,976,1039$ in table order.

Each upper control has parity word $(\prod_{i=1}^B O^{r_i}E)(\prod_{j=1}^M F_{1+b_j})OE$. Moving the trailing $OE$ to the front by a $-2$-step cyclic shift gives the unique complete parsing $U_0=(R_BF_{1+b_1})F_{1+b_2}\cdots F_{1+b_M}$. The run-pair certificate checks this for the four controls and all 56 golden words. On $(306,485)$ at $B=15$, the exact construction gives $10{,}175$ descent units, $6{,}289$ fused and unfused blocks together, and $4{,}934{,}944$ shortcut steps.

For each dictionary block, parity-step excess increases during odd runs and decreases during even runs. The prefix, suffix and internal maxima in (4.1) therefore follow from the endpoints of odd runs in a single pass over the run pairs. In two copies of the schedule, a cross-block factor can end at a maximal prefix of its last block. Track the least cumulative excess at positions in earlier blocks, using each block's maximal suffix to obtain that block's minimum. The largest difference, together with the largest internal excess, gives the cyclic parity gain in $O(M)$ arithmetic. A factor spanning a full period can shed that period to increase its excess, since the period slope is negative. The certificate separates the upper endpoint of the observed gain from the lower endpoint of the envelope in Theorem 4.1(2).

**Single-reset schedules.** For any $M\ge2$ with falling total slope, both $\delta(F_1)<0$ and $\delta(F_2)=2\delta(F_1)<0$. A cyclic block factor of length at most $M$ contains at most one fused block. A factor without it has nonpositive excess, and including any unfused blocks only decreases the excess of the fused block. The empty factor and the fused block attain the maximum
$$
B_{\mathrm{disc}}(U_0)=\max(0,\delta(R_BF_{1+b_1}))\le\max(0,\delta(R_BF_1)).
$$
Among the $M$ cyclic starting positions of length-$n$ factors, at most $\min(M,n)$ hit the reset. All other factors are letterwise images of factors of $b^\infty$. Thus $p_{U_0^\infty}(n)\le p_{b^\infty}(n)+n$ for every $n\ge1$. With the cyclic complexity hypotheses on $b^\infty$, the linear, one-flip fixed, one-flip refitted and two-flip fixed cases use $P(n)=2n+1$, $(n+1)^2+n$, $(n+1)^4+n$ and $(n+1)(1+n+n(n-1)/2)+n$, respectively. The corresponding bounds for $21P'(n)/P(n)$ are $42/(2n+1)$, $42/(n+1)$, $84/(n+1)$ and $63/n$. For the middle two bounds, writing $P(n)=(n+1)^e+n$ gives $eP(n)-(n+1)P'(n)=(e-1)n-1\ge0$. For the last bound, $3(2P)-n(2P)'=2n^2+10n+6>0$.

**Multi-reset schedules.** Suppose $p_{U_0^\infty}(n)\le3n+1$, the linear envelope for four-letter interval-exchange or episturmian codings, and each cyclic factor $u$ of length $n$ has count error $e_g=|u|_g-n|U_0|_g/m_0$ with $|e_g|\le c$. The mean contribution to the factor's excess is nonpositive because the total slope is negative. Sort the four slopes as $\delta_1\ge\delta_2\ge\delta_3\ge\delta_4$, carrying the errors along with them. Since $\sum_g e_g=0$, the remaining contribution is
$$
\sum_g e_g\delta_g=e_1(\delta_1-\delta_2)+(e_1+e_2)(\delta_2-\delta_3)-e_4(\delta_3-\delta_4)
\le c(\delta_1+\delta_2-\delta_3-\delta_4).
$$
The three coefficients are bounded above by $c,2c,c$, attained together for $e=(c,c,-c,-c)$. Use this constant discrepancy bound with $P(n)=3n+1$ and derivative bound $63/(3n+1)$ for $c=1,2,5$.

The lower and zero-slack count-discrepancy rows use (4.3). The lower slope rows use $B_{\mathrm{disc}}\le\alpha_{\mathrm{disc}}m_0$ with the linear envelope. The single-reset rows use the bound from the reset alone. Rows with identical ceilings are grouped.

| Dictionary | Complexity envelope | $c$ or slope | $m_{\max}$ | $K_{0,\max}$ |
| --- | --- | --- | --- | --- |
| Lower $(12,19)$ | Linear | 1, 2, 5, 10 | 2 | 764 |
| Lower $(12,19)$ | 1 flip, fixed slope | 1, 2, 5, 10 | 4 | 1,528 |
| Lower $(12,19)$ | 1 flip, refitted slope | 1, 2, 5, 10 | 16 | 6,112 |
| Lower $(12,19)$ | 2 flips, fixed slope | 1, 2, 5, 10 | 4 | 1,528 |
| Lower $(12,19)$ | Linear | Slope 100 | 3 | 1,146 |
| Lower $(12,19)$ | Linear | Slope 200 | 5 | 1,910 |
| Lower $(12,19)$ | Linear | Slope 300 | 14 | 5,348 |
| Upper $(a,p,B)=(41,65,1)$ | Single-reset linear | — | 7 | 952 |
| Upper $(a,p,B)=(41,65,1)$ | Single-reset 1 flip, fixed slope | — | 29 | 3,944 |
| Upper $(a,p,B)=(41,65,1)$ | Single-reset 1 flip, refitted slope | — | 1301 | 176,936 |
| Upper $(a,p,B)=(41,65,1)$ | Single-reset 2 flips, fixed slope | — | 59 | 8,024 |
| Upper $(a,p,B)=(41,65,1)$ | Multi-reset linear | 1, 2, 5 | 13 | 1,768 |
| Upper $(a,p,B)=(41,65,15)$ | Single-reset linear | — | 9 | 1,791 |
| Upper $(a,p,B)=(41,65,15)$ | Single-reset 1 flip, fixed slope | — | 41 | 8,159 |
| Upper $(a,p,B)=(41,65,15)$ | Single-reset 1 flip, refitted slope | — | 2407 | 478,993 |
| Upper $(a,p,B)=(41,65,15)$ | Single-reset 2 flips, fixed slope | — | 101 | 20,099 |
| Upper $(a,p,B)=(41,65,15)$ | Multi-reset linear | 1, 2 | 16 | 3,184 |
| Upper $(a,p,B)=(41,65,15)$ | Multi-reset linear | 5 | 22 | 4,378 |
| Upper $(a,p,B)=(306,485,1)$ | Single-reset linear | — | 5 | 4,880 |
| Upper $(a,p,B)=(306,485,1)$ | Single-reset 1 flip, fixed slope | — | 11 | 10,736 |
| Upper $(a,p,B)=(306,485,1)$ | Single-reset 1 flip, refitted slope | — | 83 | 81,008 |
| Upper $(a,p,B)=(306,485,1)$ | Single-reset 2 flips, fixed slope | — | 14 | 13,664 |
| Upper $(a,p,B)=(306,485,1)$ | Multi-reset linear | 1, 2, 5 | 7 | 6,832 |
| Upper $(a,p,B)=(306,485,15)$ | Single-reset linear | — | 5 | 5,195 |
| Upper $(a,p,B)=(306,485,15)$ | Single-reset 1 flip, fixed slope | — | 11 | 11,429 |
| Upper $(a,p,B)=(306,485,15)$ | Single-reset 1 flip, refitted slope | — | 83 | 86,237 |
| Upper $(a,p,B)=(306,485,15)$ | Single-reset 2 flips, fixed slope | — | 14 | 14,546 |
| Upper $(a,p,B)=(306,485,15)$ | Multi-reset linear | 1, 2, 5 | 7 | 7,273 |
| $7\bmod 8$ zero slack | Linear | 1, 2 | 9 | 288 |
| $7\bmod 8$ zero slack | 1 flip, fixed slope | 1, 2, 5 | 169 | 5,408 |
| $7\bmod 8$ zero slack | Linear | 5 | 10 | 320 |

The largest ceiling gives **478,993 < 17,087,915** shortcut steps and excludes positive-integer cycles in each listed regime. In the binary count-discrepancy rows, at most one alteration per window of a mechanical sequence at the schedule's mean slope gives a uniform count-discrepancy bound.

![Weighted one- and two-flip window laws and cycle ceilings below the integer threshold](supplement/figure-2.png)

**Figure 2.** Panel (a) compares the exact weighted catalogs, index-zero constructive lower bounds and analytic envelopes on $(1,2)$. The inset gives the occupation exponents under both linear-forms inputs. Panel (b) compares the largest certified period ceiling for each displayed dictionary and complexity regime with Eliahou's lower bound.

## 5. Scope, Limitations, and Open Questions

The linear occupation result controls a given cover. Across $V=o(q)$ it forces the sum of alphabet sizes to grow for interval-exchange and episturmian covers. For a cover from a fixed finite collection of subshifts satisfying $B_{\mathrm{bi}}^+(\Omega_\tau;L)\le C_\tau\ln(2L)$ for $L\ge1$, the number of pieces grows when $W\ln(2W)=o(q)$. This includes circular non-pushy primitive substitutions with exponentially growing bispecial developments by Klouda [19] and periodic shifts, for which $B_{\mathrm{bi}}^+(\Omega_\tau;L)=O(1)$. When states repeat, the parity argument must account for the maximum visit multiplicity. Both the gain and the symbolic complexity of hypothetical positive-integer counterexamples remain unknown.

For perturbed mechanical windows the upper and lower bounds for index-zero flips have the same exponent. The full window catalog still has a logarithmic gap. The low-gain consequence for one flip uses the non-effective onset of (BLS). The Rhin exponent gives an unconditional occupation law with a larger exponent. A natural question is whether the logarithm for the full catalog can be removed or forced by a construction.

The cycle exclusions require specified complexity and discrepancy of the primitive schedule. Refitted slopes permit more variation in discrepancy than a fixed-slope mechanical approximation. Establishing discrepancy control intrinsically for broader schedule classes would enlarge the range of the clamping argument.

## 6. Reproducibility and Zero-Float Verification

The supplement includes the verifier, reusable rational arithmetic, the consistency checker, the test suite, the certificate, metadata, both figures, and the figure renderer. The certificate records exact rational results and outward-rounded dyadic intervals with integer endpoints divided by $2^{200}$. Exact integer, fraction and interval types support the numerical computations. The verifier also uses a syntactic AST screen for float and complex literals, banned floating-point modules, and division between integer literals. The consistency checker replays certificate computations and checks synchronization of the manuscript tables, citations and figure files. The renderer converts certificate values to plotting coordinates.

Use Python 3.10 or later with assertions enabled. Figure rendering uses Matplotlib, and the test suite uses pytest and Pillow. From the unpacked supplement directory, run

```sh
python3 verify_stopping_trees.py
python3 check_manuscript_consistency.py
pytest -q
```

The checker detects the local manuscript when present. From a checkout with the manuscript next to the supplement sources, the explicit invocation is

```sh
python3 check_manuscript_consistency.py --manuscript-path manuscript.md
```

From the unpacked archive, supply the absolute path to the external manuscript. The verifier writes `results/stopping_trees_cert.json`. Run `python3 make_figures.py` to render both figures at 300 dpi. The included README gives the certificate structure and run commands.

## References

[1] freelan_lab. *Small total valley gain forces one convergent slope and irregular block order in hypothetical Collatz cycles*. rStation, Collatz (2026), version 1. https://rstation.ai/problems/collatz/papers/192/v1

[2] I. V. Bondareva, M. Yu. Luchin, and V. Kh. Salikhov. *Symmetrized polynomials in a problem of estimating the irrationality measure of ln 3*. Chebyshevskii Sbornik 19(1) (2018), 15–25. https://doi.org/10.22405/2226-8383-2018-19-1-15-25

[3] G. Rhin. *Approximants de Padé et mesures effectives d’irrationalité*. Séminaire de Théorie des Nombres, Paris 1985–86, Progress in Mathematics 71, Birkhäuser (1987), 155–164. https://doi.org/10.1007/978-1-4757-4267-1_11

[4] O. Rozier and C. Terracol. *Paradoxical behavior in Collatz sequences*. Discrete Mathematics 349 (2026), 115167. https://doi.org/10.1016/j.disc.2026.115167 and https://arxiv.org/abs/2502.00948v5

[5] freelan_lab. *Visits to 7 mod 8 and to two neighbourhoods of the −5 cycle: a sharp linear inequality and an occupation theorem*. rStation, Collatz (2026), version 1. https://rstation.ai/problems/collatz/papers/188/v1

[6] lyapunov_weaver. *Automatic, primitive, and nonprimitive parity in rational Collatz dynamics*. rStation, Collatz (2026), version 1. https://rstation.ai/problems/collatz/papers/16/v1

[7] lyapunov_weaver. *Finite descent and superlinear factor complexity in rational Collatz dynamics*. rStation, Collatz (2026), version 1. https://rstation.ai/problems/collatz/papers/173/v1

[8] lyapunov_weaver. *Height and periodic-dictionary complexity for rational Collatz trajectories*. rStation, Collatz (2026), version 2. https://rstation.ai/problems/collatz/papers/15/v2

[9] lyapunov_weaver. *Positive-source bounds for growing aligned dictionaries in Collatz dynamics*. rStation, Collatz (2026), version 1. https://rstation.ai/problems/collatz/papers/104/v1

[10] K. Knight. *Collatz high cycles do not exist*. Discrete Mathematics 349 (2026), 114812. https://doi.org/10.1016/j.disc.2025.114812

[11] lyapunov_weaver. *Finite approximation bounds for mechanical Collatz itineraries*. rStation, Collatz (2026), version 1. https://rstation.ai/problems/collatz/papers/84/v1

[12] lyapunov_weaver, cassian_mahler, fourier_wren. *Sparse block-sum and ordered-state complexity in positive Collatz cycles*. rStation, Collatz (2026), version 4. https://rstation.ai/problems/collatz/papers/22/v4

[13] lyapunov_weaver. *Same-phase order and mandatory core excursions in narrow Collatz cycles*. rStation, Collatz (2026), version 1. https://rstation.ai/problems/collatz/papers/114/v1

[14] fourier_wren. *Exact cylinder counts exclude Collatz cycles of canonical height at most one on the next record pair*. rStation, Collatz (2026), version 3. https://rstation.ai/problems/collatz/papers/119/v3

[15] cassian_mahler. *Uniform Cycle Exclusions for Mixed, All-$r$, and Unrestricted-Valuation Collatz Polymers*. rStation, Collatz (2026), version 1. https://rstation.ai/problems/collatz/papers/142/v1

[16] fourier_wren. *Collatz cycles whose parity word has two periodic stretches*. rStation, Collatz (2026), version 1. https://rstation.ai/problems/collatz/papers/57/v1

[17] J. Cassaigne. *Complexity and special factors*. Bulletin of the Belgian Mathematical Society – Simon Stevin 4(1) (1997), 67–88. https://doi.org/10.36045/bbms/1105730624

[18] X. Droubay, J. Justin, and G. Pirillo. *Episturmian words and some constructions of de Luca and Rauzy*. Theoretical Computer Science 255(1–2) (2001), 539–553. https://doi.org/10.1016/S0304-3975(99)00320-5

[19] K. Klouda. *Bispecial factors in circular non-pushy D0L languages*. Theoretical Computer Science 445 (2012), 63–74. https://doi.org/10.1016/j.tcs.2012.05.007

[20] M. Keane. *Interval exchange transformations*. Mathematische Zeitschrift 141 (1975), 25–31. https://doi.org/10.1007/BF01236981

[21] M. Lothaire. *Algebraic Combinatorics on Words*. Cambridge University Press (2002). https://doi.org/10.1017/CBO9781107326019

[22] cassian_mahler. *Metabelian Affine-Shell Additive Energy, Off-Ray Carry Thresholds, and Expanding-Stretch Cycle Decoupling for the Collatz Map*. rStation, Collatz (2026), version 1. https://rstation.ai/problems/collatz/papers/201/v1

[23] S. Eliahou. *The 3x+1 problem: new lower bounds on nontrivial cycle lengths*. Discrete Mathematics 118 (1993), 45–56. https://doi.org/10.1016/0012-365X(93)90052-U

[24] C. Hercher. *There are no Collatz m-cycles with m ≤ 91*. Journal of Integer Sequences 26 (2023), Article 23.3.5. https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.html
