# Slope–Ballot Duality, Exact Binary Escape Thresholds, and Parity-Trap Shifts Exceeding the $3/4$ Collatz Survival Barrier

## 1. Introduction and Summary of Main Results

### 1.1 Context, Related Work, and Open Questions

For odd positive integers $x \in 2\mathbb{Z}_{\ge 0} + 1$, the accelerated Collatz (Syracuse) map is

$$
U(x) := \frac{3x + 1}{2^{v_2(3x+1)}}, \qquad e(x) := v_2(3x+1) \in \mathbb{Z}_{\ge 1},
$$

which generates at horizon $T \ge 1$ the valuation word $w_T(n) = (e_1, \dots, e_T)$ along $x_0 = n$, $x_t = U(x_{t-1})$, $e_t = e(x_{t-1})$, with cumulative $2$-adic valuation sum $S_t := \sum_{j=1}^t e_j$ [1, 2, 3]. A central theme in Collatz dynamics—complementing stopping-time sieves [1, 2, 4, 5], difference-inequality bounds [6], almost-all descent [7], inverse-tree source analyses [8, 9, 10, 11], and mixed-polymer cycle exclusions [12]—is to compare a forward orbit $x_0 \to x_1 \to \dots \to x_T$ against all non-trivial inverse-tree predecessors $y \in U^{-m}(x_i) \setminus \{x_0, \dots, x_{i-1}\}$ ($1 \le m \le i \le T$) that merge into the trajectory from a smaller odd starting integer $y < n$.

Every $2$-adic cylinder $\mathrm{Cyl}(w) := \{n \ge 1 \text{ odd} : w_T(n) = w\}$ is a single arithmetic progression $n = n_0(w) + 2^{S_T + 1} q$ ($q \in \mathbb{Z}_{\ge 0}$, $1 \le n_0(w) < 2^{S_T + 1}$) carrying normalized $2$-adic Haar measure $\mu_2(\mathrm{Cyl}(w)) = 2^{-S_T}$ on $2\mathbb{Z}_2 + 1$. For $\mathrm{Cyl}(w)$ to avoid forward stopping ($U^i(n) < n$ for all sufficiently large $n \in \mathrm{Cyl}(w)$), $w$ must belong to the ballot-admissible non-descending set

$$
\mathcal{N}_T := \bigl\{w = (e_1, \dots, e_T) \in \mathbb{Z}_{\ge 1}^T : 2^{S_i} < 3^i \text{ for all } 1 \le i \le T\bigr\}. \tag{1.1}
$$

Under the geometric $2$-adic law $\mathbb{P}(e = k) = 2^{-k}$, Cramér large-deviation theory for the drift-free barrier $S_i < i \log_2 3$ yields an exponential decay base $2^{-I(\log_2 3)} \approx 0.94650458$ for $\mu_2(\mathcal{N}_T)$ [13, 14]. Forward non-descent $w \in \mathcal{N}_T$, however, does not preclude inverse coalescence: a trajectory in $\mathcal{N}_T$ can merge at step $i \le T$ with a distinct odd branch $y \in U^{-m}(x_i)$ satisfying $y < n$ uniformly for all sufficiently large $q$ in $\mathrm{Cyl}(w)$. The complementary cylinders—those surviving all class-uniform smaller-predecessor escapes across every prefix $1 \le i \le T$ and every inverse depth $1 \le m \le i$—form the all-prefix inverse-minimal family $\mathcal{I}_T \subseteq \mathcal{N}_T$ studied in [8, 15, 16]. Whereas stochastic branching models [13, 14], logarithmic- or natural-density trajectory absorption and quantitative synchronization theorems on integer intervals [7, 17], local $W$-digit inverse-policy entropy barriers [18], and canonical-height floor-sum cycle bounds [12, 19] analyze random ensembles, typical integer starts, local ternary policies, or periodic orbits, our focus here is deterministic cylinder-wise survival across all prefixes and measurable $3$-adic residue persistence along infinite valuation words.

At the conclusion of [11, 15, 16], three structural problems remained open:

1. **The $< 0.694$ static-cone ceiling and the $3/4$ binary barrier.** In [15], restricting to the unbounded-valuation free suffix-code monoid $\mathcal{M}_\infty$ preserving the static closed positive cone $\mathcal{C}_5^+ = \{(0, 0)\} \cup \{(d, c) : d \ge 1,\; 1 \le c \le 5(2^d - 1),\; 2 \nmid c\}$ gave combinatorial word growth $\lambda_{\mathrm{comb}}(\mathcal{M}_\infty) > 1.65$, while [16, Lemma 5.2] enclosed its $2$-adic Haar survival rate in $\lambda_{\mu_2}(\mathcal{M}_\infty) \in (0.693, 0.694)$ (and $\lambda_{\mu_2}(\mathcal{M}_\infty^\star) \in (0.692, 0.693)$, versus $(1 + \sqrt{3})/4 \approx 0.683013$ on the binary Fibonacci monoid $\langle(1), (1, 2)\rangle^*$). Because the unconstrained binary alphabet $\{1, 2\}^T$ has total $2$-adic Haar measure $(1/2 + 1/4)^T = (3/4)^T = 0.75^T$, **no binary subshift whatsoever can exceed $3/4 = 0.75$**. Whether the asymptotic survival base $\lambda_{\mu_2}(\mathcal{I}) := \limsup_{T \to \infty} \mu_2(\mathcal{I}_T)^{1/T}$ exceeds $3/4$, or whether larger valuations $e \ge 3$ force $\lambda_{\mu_2}(\mathcal{I}) \le 3/4$, was left open in [16, Section 5].
2. **Exact binary escape horizon and prefix non-monotonicity.** Balanced binary words $\mathcal{B}(\alpha)$ up to slope $\log_2 3 - 1.26 \times 10^{-11}$ were proved division-minimal outside the two excluded open bands $(32/21, 26/17) \cup (11/7, 19/12)$ (where failing windows of lengths $30$ and $23$ occur) in [11, Theorem 4], while unrestricted ballot words in $\mathcal{N}_T$ escape $\mathcal{I}_T$ already at $T = 4$ via $w = (1, 1, 1, 3)$ [15, 16]. For general (unbalanced) binary ballot words $\mathcal{N}_T \cap \{1, 2\}^T$, neither the exact minimum horizon $T_{\min}(\{1, 2\})$ at which $(\mathcal{N}_T \cap \{1, 2\}^T) \setminus \mathcal{I}_T \ne \emptyset$ nor the mechanism governing prefix shielding of downstream escapes had been determined.
3. **Compatibility with post-climb $3$-adic persistence.** In [10, 16], trajectories in $\langle(1), (1, 2)\rangle^{\mathbb{N}}$ and $(\mathcal{M}_\infty^\star)^{\mathbb{N}}$ were proved to leave a strictly positive $3$-adic Haar share of starting residues in $\mathbb{Z}_3^\times$ and $3\mathbb{Z}_3$ outside the measurable countable paid union $\mathcal{P}(w)$ across all horizons $t \ge 0$ and all extra inverse depths $u \ge 0$. That proof relied on $\delta = 0$ tie exclusion inside $\mathcal{C}_5^+$. Enlarging the cone slope beyond $5$ and admitting $e \in \{3, 4\}$ risks activating $\delta = 0$ ties such as $(0, 2)$—realizing integer collisions $U^t(n + 2) = U^t(n)$—which collapse $3$-adic persistence on $3\mathbb{Z}_3$.

In this paper, we resolve all three problems via exact symbolic arithmetic over $\mathbb{Z}[1/2] \hookrightarrow \mathbb{Z}_3$, establishing four main theorems:

- **Theorem 1 (Symbolic $\mathbb{Z}[1/2] \hookrightarrow \mathbb{Z}_3$ Pullback Automaton and Binomial Parity-Trap Law).** Class-uniform rival branches along any word $w \in \mathbb{Z}_{\ge 1}^T$ are governed by an exact symbolic pullback over $(d, c) \in \mathbb{Z} \times \mathbb{Z}[1/2]$ with normalized $3$-adic invariant $\theta = 2^{-d} c \in \mathbb{Z}_3$. States with $\theta \equiv 2 \pmod 3$ are annihilated in one backward step by every even valuation $e \in 2\mathbb{Z}_{\ge 1}$, whereas $\theta \equiv 1 \pmod 3$ is annihilated by every odd $e$. By $(4^k - 1)/3 \equiv k \pmod 3$, valuations $b \in \{3, 4\}$ birth a unique negative discrepancy $d' = -2$ ($k = 1, \theta' \equiv 2 \pmod 3$) annihilated in one step by any preceding even valuation $a \in 2\mathbb{Z}_{\ge 1}$, whereas every $b \ge 5$ simultaneously births incongruent discrepancies $d' \in \{-2, -4\}$ ($k \in \{1, 2\}$) that no single preceding letter can trap.
- **Theorem 2 (Slope–Ballot Duality and Parity-Trap Shifts of Finite Type Exceeding $3/4 = 0.75$).** Naive expansion to a uniform static cone $\beta > 5$ fails because $(1, 2)$ possesses an exact repelling separatrix $c^* = 5 \cdot 2^d - 1$; crossing $c^*$ via consecutive $2$s cascades into $c < 0$. By tracking left-resolving dyadic slope automata $\beta_v = k / q \in [1, 7]$ that gate $e = 2$ at $\beta_v \le 5$ and synchronize four suffix-free parity-trap atoms over $K \le 4$, we preserve strict open cones $\mathcal{K}^\circ(\beta_u)$ with zero violations across all unbounded rival exponents $g \in \mathbb{Z}_{\ge 1}$. A four-line telescoping identity (**Slope–Ballot Duality**) proves that cone invariance automatically bounds the forward ballot ratio $2^{S_m} / 3^m < \beta_{u_0} / \beta_{u_m} \le 7$ on every walk, eliminating the ballot barrier with zero exponential rate loss. Prepending $1^{10}$ guarantees strict finite-integer all-prefix survival ($q_0(w) = 0$) and certifies

$$
\lambda_{\mu_2}(\mathcal{I} \cap \{1, 2\}^*) \;\ge\; \frac{91{,}496{,}991{,}773{,}239}{123{,}558{,}943{,}184{,}692} \;>\; \mathbf{0.740512},
$$

$$
\mathbf{0.751095} \;<\; \frac{334{,}085{,}797{,}246{,}459}{444{,}797{,}811{,}679{,}880} \;\le\; \lambda_{\mu_2}(\mathcal{I}) \;\le\; 2^{-I(\log_2 3)} \;<\; \mathbf{0.94650458},
$$

crossing the binary barrier $3/4 = 0.75$ (already $> 0.750450$ at $q = 32$) and yielding an unconditional finite-$X$ survivor count $\ge c_0 X^{0.739469}$ up to horizon $\lfloor \log_3 X \rfloor$.
- **Theorem 3 (Zero-Truncation Binary Escape Thresholds and Non-Monotone Prefix Shielding).** Combining an exact ballot-drop discrepancy bound $d_\ell \le \min(22 - \ell, 12)$ with a monotone reverse-prefix ballot dominance recurrence requiring zero heuristic state truncation, we prove $(\mathcal{N}_T \cap \{1, 2\}^T) \setminus \mathcal{I}_T = \emptyset$ for all $1 \le T \le 18$, establish $T_{\min}(\{1, 2\}) = 19$ ($2$ of $130{,}384$ binary ballot words escape at $T = 19$, and $11$ of $256{,}460$ at $T = 20$), and establish $T_{\min}^{\mathrm{full}}(\{1, 2\}) = 22$ via an explicit witness $w_{22}$ reaching $(d, c) = (-2, -3/4)$. Because $(-2, -3/4)$ satisfies $c = 2^d - 1$, it is an algebraic fixed point of $(e = 1, g = 1)$: the pure-climb ray $1^M \cdot w_{22} \notin \mathcal{I}_{M+22}$ escapes for every $M \ge 0$, whereas inserting one $2$ shifts $(-2, -3/4) \mapsto (-2, -5/4)$ and restores $1^k \cdot (2) \cdot w_{22} \in \mathcal{I}_{k+23}$ for all $k \ge 5$.
- **Theorem 4 (Garden-of-Eden Dichotomy and Joint All-Horizon $3$-Adic Persistence Above $3/4$).** On $\mathcal{A}_{\{1, 2\}}(q, 7)$, a seven-state algebraic predecessor closure isolates $\{(0, 2), (1, 3)\}$ and $\{(1, 9), (2, 13)\}$ as unreachable Garden-of-Eden $2$-cycles across all $d \ge 0$ and all $q \ge 1$, and matches explicit walk witnesses on $8 \mid q$ to establish exact sets $\mathcal{R}_0 = \{(0, 0)\}$ and $\mathcal{R}_1 = \{(1, 1), (1, 5), (1, 7)\}$. Admitting $e = 3$ in unanchored $\mathcal{A}_{\mathrm{PT}}$ breaks Garden-of-Eden isolation via $(1, 1) \xrightarrow{3, g=3} (1, 3) \xrightarrow{2, g=1} (0, 2)$ on $w_{\mathrm{tie}} = (2, 1, 2, 3, 2, 1)$, realizing $U^6(n + 2) = U^6(n)$ and collapsing $3\mathbb{Z}_3$ at $u = 1$. Factoring $1^{10} = 1^6 \cdot 1^4$, however, compresses $\mathcal{K}^\circ(7)$ across $1^4$ via $\psi_{1^4}(7) = 59/27 < 5$ strictly into $\mathcal{C}_5^+ \setminus \{(0, 0)\}$, certifying simultaneous all-horizon ($t \ge 0$), all-depth ($u \ge 0$) $3$-adic persistence $\overline{\mathsf{Unpaid}}_\times(w) \ge \mathbf{0.19955319}$ and $\overline{\mathsf{Unpaid}}_3(w) \ge \mathbf{0.82429853}$ outside the countable union $\mathcal{P}(w)$ on every trajectory in $1^{10} \cdot \mathcal{A}_{\mathrm{PT}}(128, 7)^{\mathbb{N}}$.

---

### 1.2 Precise Definitions and Quantifier Conventions

Throughout, let $\mathbb{O} := 2\mathbb{Z}_{\ge 0} + 1$ denote the odd positive integers. For any finite word $w = (e_1, \dots, e_T) \in \mathbb{Z}_{\ge 1}^T$, write $|w| := T$, $\|w\| := S_T = \sum_{j=1}^T e_j$, and $w_{a..b} := (e_a, \dots, e_b)$. By Hensel's lemma applied to $3 x_{t-1} + 1 \equiv 2^{e_t} \pmod{2^{e_t + 1}}$, $\mathrm{Cyl}(w) = \{n_0(w) + 2^{S_T + 1} q : q \in \mathbb{Z}_{\ge 0}\}$ for a unique odd base $1 \le n_0(w) < 2^{S_T + 1}$, and the $t$-th forward iterate along $\mathrm{Cyl}(w)$ is the exact affine function

$$
x_t(q) = U^t\bigl(n_0(w) + 2^{S_T + 1} q\bigr) = x_{t,0}(w) + 3^t \cdot 2^{S_T + 1 - S_t} q, \qquad x_{t,0}(w) := U^t(n_0(w)). \tag{1.2}
$$

**Definition 1.1 (Inverse Predecessor Branches and Forward Valuation Ordering).** For an odd integer $z \ge 1$ and a valuation tuple $g = (g_1, \dots, g_r) \in \mathbb{Z}_{\ge 1}^r$, define the single-step inverse map $\Psi_k(z) := (2^k z - 1)/3$. The composition $y = \Psi_{g_1} \circ \dots \circ \Psi_{g_r}(z)$ is a valid odd $r$-step predecessor of $z$ with **forward** valuation word $g$ (meaning $y = z_0 \xrightarrow{g_1} z_1 \to \dots \xrightarrow{g_r} z_r = z$, so $U^r(y) = z$ and $w_r(y) = g$) if and only if every backward iterate $z_{j-1} = \Psi_{g_j}(z_j)$ ($z_r := z$, $j = r, r - 1, \dots, 1$) is a positive integer; integrality of $(2^{g_j} z_j - 1)/3$ enforces $z_{j-1} \equiv 1 \pmod 2$ since $g_j \ge 1$, and $2^{g_j} z_j - 1 = 3 z_{j-1}$ enforces $v_2(3 z_{j-1} + 1) = g_j$.

**Definition 1.2 (Asymptotic vs. Strict All-Prefix Inverse-Minimal Cylinders).** Let $w = (e_1, \dots, e_T) \in \mathcal{N}_T$.
1. We say $w \in \mathcal{I}_T$ (**asymptotically all-prefix inverse-minimal**) if there exists $q_0(w) \in \mathbb{Z}_{\ge 0}$ such that for every $q \ge q_0(w)$, $n = n_0(w) + 2^{S_T + 1} q$ satisfies: for every prefix $1 \le i \le T$, every inverse depth $1 \le r \le i$, and every valid $r$-step predecessor $y = \Psi_{g_1} \circ \dots \circ \Psi_{g_r}(x_i(q))$ whose forward valuation word $g = (g_1, \dots, g_r)$ diverges from the trunk immediately prior to $x_i(q)$ (**$g_r \ne e_i$**), one has $y > n$.
2. We say $w \in \mathcal{I}_T^{\mathrm{strict}}$ (**strictly all-prefix inverse-minimal**) if $q_0(w) = 0$, i.e., $y > n$ holds for every integer $n \in \mathrm{Cyl}(w)$ ($q \ge 0$), with zero finite-size exceptions. Clearly $\mathcal{I}_T^{\mathrm{strict}} \subseteq \mathcal{I}_T \subseteq \mathcal{N}_T$.

*Proof of Full Non-Trivial Inverse-Tree Coverage under $g_r \ne e_i$.* Fix $q \ge 0$, $1 \le i \le T$, $1 \le m \le i$, and any non-trunk predecessor $y \in U^{-m}(x_i(q)) \setminus \{x_0(q), \dots, x_{i-1}(q)\}$ with forward orbit $y = y_0 \to y_1 \to \dots \to y_m = x_i(q)$ and valuation word $\tilde{g} = (\tilde{g}_1, \dots, \tilde{g}_m)$. Let $r \in \{1, \dots, m\}$ be the smallest forward step at which $y_r \in \{x_0(q), \dots, x_i(q)\}$. Because $U$ is deterministic and $y_m = x_i(q)$ while $y_0 \notin \{x_0(q), \dots, x_{i-1}(q)\}$, the remaining $m - r$ steps coincide with the trunk, so $y_r = x_{i'}(q)$ at $i' := i - m + r \in \{r, \dots, i\}$. Setting $g := (\tilde{g}_1, \dots, \tilde{g}_r)$, minimality of $r$ gives $y_{r-1} \ne x_{i'-1}(q)$ while $U(y_{r-1}) = x_{i'}(q) = U(x_{i'-1}(q))$; if $g_r = e_{i'}$, then $(3 y_{r-1} + 1)/2^{g_r} = (3 x_{i'-1}(q) + 1)/2^{e_{i'}}$ would force $y_{r-1} = x_{i'-1}(q)$, a contradiction. Hence $g_r \ne e_{i'}$, so $(i', r, g)$ is tested by Definition 1.2. (By contrast, requiring $g_1 \ne e_{i-r+1}$ would miss genuine smaller predecessors that share initial forward valuations before merging on a shorter step count: on $w = (1, 1, 1, 1, 3) \in \mathcal{N}_5$ with $n_0 = 223$ and $223 \to 335 \to 503 \to 755 \to 1133 \to 425$, the rival $111 = (223 - 1)/2 \to 167 \to 251 \to 377 \to 283 \to 425$ has forward word $g = (1, 1, 1, 2, 1)$ satisfying $g_5 = 1 \ne 3 = e_5$ while $g_1 = 1 = e_1$, and its depth-$4$ sub-branch from $167$ has $g = (1, 1, 2, 1)$ with $g_4 = 1 \ne 3 = e_5$.)

**Definition 1.3 ($2$-Adic Survival Rate and Measurable Countable-Union $3$-Adic Unpaid Shares).** For any family $\mathcal{F} = (\mathcal{F}_T)_{T \ge 1}$ with $\mathcal{F}_T \subseteq \mathbb{Z}_{\ge 1}^T$, define $\mu_2(\mathcal{F}_T) := \sum_{w \in \mathcal{F}_T} 2^{-\|w\|}$ and $\lambda_{\mu_2}(\mathcal{F}) := \limsup_{T \to \infty} \mu_2(\mathcal{F}_T)^{1/T}$. Following [10] and [16, Definition 1.1], for a finite word $w_T = (e_1, \dots, e_T) \in \mathbb{Z}_{\ge 1}^T$, consider all inverse specifications $(t, g, f)$ consisting of a horizon $0 \le t \le T$, a matched/shallower forward-indexed rival tuple $g = (g_1, \dots, g_v) \in \mathbb{Z}_{\ge 1}^v$ ($0 \le v \le t$, with $g_v \ne e_t$ whenever $v \ge 1$), and an extra deeper forward-indexed inverse tuple $f = (f_1, \dots, f_u) \in \mathbb{Z}_{\ge 1}^u$ ($u \ge 0$, with $u \ge 1$ when $v = 0$) that are **class-uniformly contracting**:
1. $1 \le v < t$, $u = 0$, and $2^{\|g\|} 3^{t - v} < 2^{S_t}$; or
2. $v = t$, $u = 0$, and either $\|g\| < S_t$ or ($\|g\| = S_t$ and $c_0 < 0$); or
3. $v = t$, $u \ge 1$, and $2^{\|g\| - S_t + \|f\|} < 3^u$ (including $t = v = 0, u \ge 1$ with $2^{\|f\|} < 3^u$).

For each such $(t, g, f)$, the set $\mathcal{A}_{w_T}(t, g, f) \subseteq \mathbb{Z}_3$ of $3$-adic starting values $n \in \mathbb{Z}_3$ along which all $v + u$ backward steps $\Psi_{f_1} \circ \dots \circ \Psi_{f_u} \circ \Psi_{g_1} \circ \dots \circ \Psi_{g_v}(x_t)$ lie in $\mathbb{Z}_3$ is either empty or a single clopen $3$-adic ball modulo $3^u$ (modulo $1$ when $u = 0$). Define the finite-horizon paid set $\mathcal{P}(w_T) := \bigcup_{(t, g, f)} \mathcal{A}_{w_T}(t, g, f)$ and, for an infinite word $w = (e_1, e_2, \dots) \in \mathbb{Z}_{\ge 1}^{\mathbb{N}}$ with prefixes $w_T := w_{1..T}$, define the **all-horizon, all-depth paid set** as the **measurable countable union**

$$
\mathcal{P}(w) := \bigcup_{T = 0}^{\infty} \mathcal{P}(w_T) \subseteq \mathbb{Z}_3. \tag{1.3}
$$

Because each $\mathcal{A}_{w_T}(t, g, f)$ is clopen, $\mathcal{P}(w)$ is an open Borel subset of $\mathbb{Z}_3$ with normalized $3$-adic Haar measure $\mu_3(\mathcal{P}(w)) = \lim_{T \to \infty} \mu_3(\mathcal{P}(w_T))$. The **all-horizon, all-depth conditional unpaid shares** on $\mathbb{Z}_3^\times = (1 + 3\mathbb{Z}_3) \sqcup (2 + 3\mathbb{Z}_3)$ ($\mu_3(\mathbb{Z}_3^\times) = 2/3$) and $3\mathbb{Z}_3$ ($\mu_3(3\mathbb{Z}_3) = 1/3$) are

$$
\overline{\mathsf{Unpaid}}_\times(w) := \frac{3}{2}\,\mu_3\bigl(\mathbb{Z}_3^\times \setminus \mathcal{P}(w)\bigr) \in [0, 1], \qquad \overline{\mathsf{Unpaid}}_3(w) := 3\,\mu_3\bigl(3\mathbb{Z}_3 \setminus \mathcal{P}(w)\bigr) \in [0, 1]. \tag{1.4}
$$

**Remark 1.4 (Open Countable Union $\mathcal{P}(w)$ vs. Topological Closure $\overline{\mathcal{P}(w)}$).** It is essential that $(1.3)$ defines $\mathcal{P}(w)$ as the measurable countable union $\bigcup_{T \ge 0} \mathcal{P}(w_T)$ rather than its $3$-adic topological closure $\overline{\mathcal{P}(w)}$. Even at horizon $t = 0$ alone, $\mathcal{P}(\emptyset) \cap \mathbb{Z}_3^\times$ is **topologically dense** in $\mathbb{Z}_3^\times$: given any unit ball $a + 3^m \mathbb{Z}_3 \subset \mathbb{Z}_3^\times$, one can choose $m$ successive inverse exponents so that all $m$ steps are integral on $a + 3^m \mathbb{Z}_3$ and stay in $\mathbb{Z}_3^\times$ through step $m - 1$ (among three consecutive exponents of the admissible parity, the quotient runs through all three residues modulo $3$), mapping $a + 3^m \mathbb{Z}_3$ surjectively onto $\mathbb{Z}_3$; restricting that image to $z \equiv -1 \pmod{3^L}$ admits $L$ further $\Psi_1$ steps via $\Psi_1^L(z) + 1 = (2/3)^L (z + 1)$, achieving $2^{F + L} / 3^{m + L} < 1$ for sufficiently large $L$. Thus $\overline{\mathcal{P}(w)} \supseteq \mathbb{Z}_3^\times$ for every $w$, whereas the unpaid complement $\mathbb{Z}_3^\times \setminus \mathcal{P}(w)$ is a compact nowhere-dense ("fat Cantor") set of strictly positive Haar measure whenever the countable union of clopen balls $\mathcal{P}(w) \cap \mathbb{Z}_3^\times$ has total $\mu_3$-measure $< 2/3$.

---

## 2. Symbolic $\mathbb{Z}[1/2] \hookrightarrow \mathbb{Z}_3$ Pullback Automaton and the Binomial Parity-Trap Law

### 2.1 Exact Equivalence Between Cylinder Lifting and Symbolic Dyadic Pullbacks

In [15, 16], inverse branches over a word $u = (e_1, \dots, e_r)$ were tracked by lifting $n_0(u) \pmod{2^{S_r+1}}$ and testing $3$-divisibility along concrete integers $x_{r,0}(u)$. We first establish that class-uniform predecessors depend solely on a purely symbolic automaton over $\mathbb{Z} \times \mathbb{Z}[1/2]$ embedded in $\mathbb{Z}_3$, eliminating integer CRT lifting during cone and threshold searches.

For $(d, c) \in \mathbb{Z} \times \mathbb{Z}[1/2]$ and $(e, g) \in \mathbb{Z}_{\ge 1}^2$, define the single-step **symbolic pullback operator** $\mathcal{P}_{e, g}(d, c)$ by setting $d' := d + g - e$ and $R := 2^{d'} + 2^g c - 1 \in \mathbb{Z}[1/2]$. Writing $R = a / 2^k$ in lowest terms ($k \ge 0$, $2 \nmid a$ when $a \ne 0$), define

$$
\mathcal{P}_{e, g}(d, c) := \begin{cases} (d',\; R / 3), & \text{if } 3 \mid a, \\ \bot, & \text{otherwise.} \end{cases} \tag{2.1}
$$

Because $2$ is invertible in $\mathbb{Z}_3$, $3 \mid a$ in $\mathbb{Z}$ is equivalent to $R \equiv 0 \pmod{3\mathbb{Z}_3}$ under the canonical embedding $\mathbb{Z}[1/2] \hookrightarrow \mathbb{Z}_3$.

**Theorem 1 (Symbolic Pullback Equivalence and Binomial Parity-Trap Law).**
1. *(Exact Cylinder Equivalence).* Fix any word $u = (e_1, \dots, e_r) \in \mathbb{Z}_{\ge 1}^r$ and any forward-indexed rival valuation sequence $g = (g_1, \dots, g_r) \in \mathbb{Z}_{\ge 1}^r$. Starting from $(d_r, c_r) := (0, 0)$, define $(d_{j-1}, c_{j-1}) := \mathcal{P}_{e_j, g_j}(d_j, c_j)$ backward for $j = r, r - 1, \dots, 1$. Then $\Psi_{g_1} \circ \dots \circ \Psi_{g_r}(x_r(q))$ is a valid odd $r$-step predecessor of $x_r(q)$ for at least one $q \in \mathbb{Z}_{\ge 0}$ on $\mathrm{Cyl}(u)$ if and only if $(d_0, c_0) \ne \bot$, in which case it is a valid odd $r$-step predecessor for all sufficiently large $q \in \mathbb{Z}_{\ge 0}$ and satisfies the exact identity

$$
y_0(q) = \Psi_{g_1} \circ \dots \circ \Psi_{g_r}(x_r(q)) = 2^{d_0} n(q) + c_0 \qquad \text{for every } n(q) = n_0(u) + 2^{S_r + 1} q \in \mathrm{Cyl}(u), \tag{2.2}
$$

where $d_0 = \sum_{j=1}^r (g_j - e_j) = \|g\| - S_r$ and $2^{\max(0, -d_0)} c_0 \in \mathbb{Z}$. Moreover, under Definition 1.2, any prefix $w_{1..i} \in \mathcal{N}_i$ fails asymptotic survival at suffix length $r \in \{1, \dots, i\}$ ($k := i - r$) if and only if $w_{k+1..i}$ admits a pullback diverging at its rightmost step ($g_r \ne e_i$) reaching $(d, c) \ne \bot$ with either $(k = 0 \text{ and } d < 0)$, $(k = 0, d = 0, c < 0)$, or $(k \ge 1 \text{ and } 2^d \cdot 3^k < 2^{S_k})$.
2. *(Normalized $3$-Adic Invariant and Parity Selection).* Set $\theta := 2^{-d} c \in \mathbb{Z}[1/2] \subseteq \mathbb{Z}_3$. Along any valid step $(d', c') = \mathcal{P}_{e, g}(d, c)$, $\theta' := 2^{-d'} c'$ satisfies

$$
3 \theta' = 1 + 2^e \theta - 2^{-d'}. \tag{2.3}
$$

Reducing $(2.3)$ modulo $3\mathbb{Z}_3$, feasibility requires $2^{-d'} \equiv 1 + 2^e \theta \pmod 3$:
   - If $\theta \equiv 2 \pmod 3$ and $e$ is **even** ($2^e \equiv 1 \pmod 3$), then $1 + 2^e \theta \equiv 0 \pmod 3$, which is impossible since $2^{-d'} \in \{1, 2\} \pmod 3$; hence $\mathcal{P}_{e, g}(d, c) = \bot$ for every $g \ge 1$.
   - Symmetrically, if $\theta \equiv 1 \pmod 3$ and $e$ is **odd** ($2^e \equiv 2 \pmod 3$), then $1 + 2^e \theta \equiv 0 \pmod 3$, so $\mathcal{P}_{e, g}(d, c) = \bot$ for every $g \ge 1$.
3. *(Binomial Parity-Trap Dichotomy at $K = 4$ vs. $K \ge 5$).* From $(0, 0)$ on a single step $b \ge 3$ ($g \ne b$), negative discrepancies $d' = g - b < 0$ satisfy $2^{d'} \equiv 1 \pmod 3$, forcing $d' = -2k$ ($1 \le k \le \lfloor (b-1)/2 \rfloor$, $g = b - 2k$) with

$$
c' = -\frac{1 - 2^{-2k}}{3} = -\frac{4^k - 1}{3 \cdot 4^k}, \qquad \theta' = 2^{2k} c' = -\frac{4^k - 1}{3} \equiv -k \equiv 2k \pmod 3, \tag{2.4}
$$

since $4^k - 1 = (4 - 1)\sum_{j=0}^{k-1} 4^j \equiv 3k \pmod 9$. Consequently:
   - For **$b \in \{3, 4\}$**, the unique negative-discrepancy state is $k = 1$, giving $(d', c') = (-2, -1/4)$ with $\theta' = -1 \equiv 2 \pmod 3$. By Part 2, every preceding even valuation $a \in 2\mathbb{Z}_{\ge 1}$ annihilates $(-2, -1/4)$ in one step ($\mathcal{P}_{a, g'}(-2, -1/4) = \bot$ for all $g' \ge 1$).
   - For **$b \ge 5$**, both $k = 1$ ($d' = -2, \theta' \equiv 2 \pmod 3$) and $k = 2$ ($d' = -4, c' = -5/16, \theta' \equiv 1 \pmod 3$) are simultaneously birthed on $b$: an even predecessor $a$ kills $k = 1$ while letting $k = 2$ survive, whereas an odd predecessor $a$ kills $k = 2$ while letting $k = 1$ survive.

*Proof.* For Part 1, proceed by backward induction from $j = r$, where $y_r(q) = x_r(q) = 2^0 x_r(q) + 0 \in \mathbb{Z}$ for all $q \in \mathbb{Z}_{\ge 0}$. Suppose at step $j$ that $y_j(q) = 2^{d_j} x_j(q) + c_j \in \mathbb{Z}$ for all $q \in \mathbb{Z}_{\ge 0}$. Substituting $x_j(q) = (3 x_{j-1}(q) + 1)/2^{e_j}$ into $3 y_{j-1}(q) = 2^{g_j} y_j(q) - 1$ yields

$$
3 y_{j-1}(q) = 2^{g_j}\!\left(2^{d_j} \frac{3 x_{j-1}(q) + 1}{2^{e_j}} + c_j\right) - 1 = 3 \cdot 2^{d_j + g_j - e_j} x_{j-1}(q) + \bigl(2^{d_j + g_j - e_j} + 2^{g_j} c_j - 1\bigr). \tag{2.5}
$$

Set $d_{j-1} = d_j + g_j - e_j$ and $R = 2^{d_{j-1}} + 2^{g_j} c_j - 1 \in \mathbb{Z}[1/2]$. Because $y_j(q) \in \mathbb{Z}$ and $g_j \ge 1$, the left-hand side $2^{g_j} y_j(q) - 1$ is already an integer for every $q \in \mathbb{Z}_{\ge 0}$. Embedding $(2.5)$ into $\mathbb{Z}_3$ (where $2$ is a unit and $3 \cdot 2^{d_{j-1}} x_{j-1}(q) \in 3\mathbb{Z}_3$), we obtain $2^{g_j} y_j(q) - 1 \equiv R \pmod{3\mathbb{Z}_3}$ for every $q \in \mathbb{Z}_{\ge 0}$. Since a rational integer belongs to $3\mathbb{Z}_3$ if and only if it is divisible by $3$ in $\mathbb{Z}$, we have $y_{j-1}(q) \in \mathbb{Z}$ for at least one $q \in \mathbb{Z}_{\ge 0}$ if and only if $R \in 3\mathbb{Z}_3$ ($3 \mid a$), in which case $y_{j-1}(q) = 2^{d_{j-1}} x_{j-1}(q) + R/3 \in \mathbb{Z}$ holds simultaneously for **every** $q \in \mathbb{Z}_{\ge 0}$. (Conversely, if $\mathcal{P}_{e_j, g_j}(d_j, c_j) = \bot$ at the largest failing index $j$, then $y_{j-1}(q) \notin \mathbb{Z}$ for all $q \in \mathbb{Z}_{\ge 0}$, violating Definition 1.1; indeed $v_3(y_{j-1}(q)) = -1$ and subsequent $\Psi_{g_\ell}$ steps strictly decrease $v_3$, so even $y_0(q) \notin \mathbb{Z}$.) When $(d_0, c_0) \ne \bot$, positivity $y_{j-1}(q) \ge 1$ ($1 \le j \le r$) holds for all sufficiently large $q$ since $2^{d_{j-1}} > 0$ and $x_{j-1}(q) \to \infty$ as $q \to \infty$. At suffix split $k = i - r \ge 1$, $x_k(q) = \frac{3^k}{2^{S_k}} n(q) + \kappa_k$ for a constant $\kappa_k > 0$, so $y_k(q) = 2^d \frac{3^k}{2^{S_k}} n(q) + (2^d \kappa_k + c) < n(q)$ for all large $q$ if and only if $2^d \cdot 3^k < 2^{S_k}$ (equality $2^d \cdot 3^k = 2^{S_k}$ is impossible for $k \ge 1$ by unique prime factorization).

For Part 2, dividing $3 c' = 2^{d'} + 2^g c - 1$ by $2^{d'} = 2^{d + g - e}$ yields $3 \theta' = 1 + 2^e (2^{-d} c) - 2^{-d'} = 1 + 2^e \theta - 2^{-d'}$, and $2^{-d'} \not\equiv 0 \pmod 3$ gives both parity annihilation rules immediately. For Part 3, setting $(d, c) = (0, 0)$ gives $R = 2^{d'} - 1 \equiv 0 \pmod{3\mathbb{Z}_3} \iff 2 \mid d'$; writing $d' = -2k$ gives $(2.4)$, and $(4^k - 1)/3 = \sum_{j=0}^{k-1} 4^j \equiv k \pmod 3$ completes the proof. $\blacksquare$

**Worked $2$-Step Toy Check.** On $w = (e_1, e_2) = (a, b)$ with forward rival word $g = (g_1, g_2)$ ($g_2 \ne b$), compare $(1, 3)$ against $(2, 3)$ and $(2, 5)$:
- At $j = 2$ ($e_2 = 3$), $(0, 0)$ pulls back for $g_2 \ne 3$ to $(d_1, c_1) = (-2, -1/4)$ ($g_2 = 1, \theta_1 \equiv 2 \pmod 3$) and to $(2m, (4^m - 1)/3)$ for $g_2 = 3 + 2m \ge 5$ (for $m = 1$, $(2, 1)$ at $g_2 = 5$ has $\theta_1 = 1/4 \equiv 1 \pmod 3$).
- Prepending odd $a = 1$ in $(1, 3)$: $(2, 1)$ ($\theta_1 \equiv 1$) dies on odd $a = 1$, while $(-2, -1/4)$ survives for even $g_1 \ge 2$, giving $(-2, -1/4) \xrightarrow{e_1=1,\, g_1=2} (-1, -1/2)$ with forward rival word $g = (2, 1)$ (on $\mathrm{Cyl}(1, 3)$, $n_0 = 19$, $U^2(19) = 11$, and rival $y_0 = 9 = \frac{19}{2} - \frac{1}{2} < 19$ follows $9 \xrightarrow{2} 7 \xrightarrow{1} 11$; prepending $1^3$ embeds this into $(1, 1, 1, 1, 3) \in \mathcal{N}_5 \setminus \mathcal{I}_5$).
- Prepending even $a = 2$ in $(2, 3)$: $(-2, -1/4)$ ($\theta_1 \equiv 2$) is annihilated on $a = 2$, while $(2, 1)$ survives for odd $g_1 = 2m - 1 \ge 1$ ($g_1 = 1 \implies (1, 1)$, $g_1 = 3 \implies (3, 5)$, etc.), so every surviving state on $(2, 3)$ satisfies $d_0 \ge 1$ and $c_0 \ge 1$.
- On $(2, 5)$, $b = 5$ births both $(-2, -1/4)$ ($g_2 = 3, \theta_1 \equiv 2$, killed by $a = 2$) and $(-4, -5/16)$ ($g_2 = 1, \theta_1 \equiv 1$, surviving $a = 2$), which escapes via $(-4, -5/16) \xrightarrow{e_1=2,\, g_1=1} (-5, -17/32)$ ($g = (1, 1)$).

In `code/verify_slope_ballot_parity.py` (Module 1), Theorem 1(1) is independently cross-checked against concrete integer cylinder preimages across all $313$ ballot-admissible words in $\bigcup_{T=1}^8 \mathcal{N}_T$ and on $w = (1, 1, 1, 1, 3)$ ($1{,}679$ cylinder-shift seam assertions, $0$ discrepancies).

---

## 3. Slope–Ballot Duality, Rogue-Separatrix Avoidance, and Parity-Trap Shifts Exceeding $3/4$

### 3.1 Why Naive Cone Expansion Fails: The $(1, 2)$ Rogue Separatrix $c^* = 5 \cdot 2^d - 1$

To exceed the binary survival ceiling inside $\mathcal{C}_5^+$, it is natural to ask whether one can simply enlarge a uniform static cone from $\beta = 5$ to some $\beta > 5$ (such as $\beta = 6$ or $\beta = 7$) on $\{1, 2\}^*$. That attempt fails because the $2$-step block $(1, 2)$ possesses an affine separatrix at slope $\beta^* = 5$ driven by the competing slope maps $\psi_1(\beta) := \frac{1 + 2\beta}{3}$ (contracting toward $1$) and $\psi_2(\beta) := \frac{1 + 4\beta}{3}$ (expanding for all $\beta > 0$).

Specifically, applying the discrepancy-reducing branch $g = 1$ on $e = 2$ followed by $g = 1$ on $e = 1$ to an affine boundary ansatz $c = \beta \cdot 2^d - 1$ ($d \ge 1$) yields:
1. After $e = 2, g = 1$: $d' = d - 1$ and $c' = \frac{2^{d-1} + 2(\beta \cdot 2^d - 1) - 1}{3} = \frac{4\beta + 1}{3} 2^{d-1} - 1 = \psi_2(\beta) 2^{d-1} - 1$.
2. After $e = 1, g = 1$: $d'' = d - 1$ and $c'' = \frac{2^{d-1} + 2(\psi_2(\beta) 2^{d-1} - 1) - 1}{3} = \frac{8\beta + 5}{9} 2^{d-1} - 1 = \psi_1(\psi_2(\beta)) 2^{d-1} - 1$.

The unique fixed point of $\psi_1 \circ \psi_2(\beta) = \frac{8\beta + 5}{9}$ is $\beta^* = 5$, corresponding to $c^*(d) = 5 \cdot 2^d - 1$ (for example, $(3, 39) \xrightarrow{2, g=1} (2, 27) \xrightarrow{1, g=1} (2, 19)$). Whenever consecutive $e = 2, g = 1$ steps occur without intervening $1$s, each step applies the expanding map $\psi_2(\beta) = \frac{4\beta + 1}{3}$ while dropping $d$ toward $0$. Once a trajectory reaches the critical $d = 0$ boundary point $(0, 4)$ ($c^*(0) = 5 \cdot 2^0 - 1 = 4$), subsequent alternating $(2, 1)$ steps breach $d = 0$ and cascade into negative $c$:

$$
(0, 4) \xrightarrow{2, g=1} (-1, 5/2) \xrightarrow{1, g=1} (-1, 3/2) \xrightarrow{2, g=1} (-2, 3/4) \xrightarrow{1, g=1} (-2, 1/4) \xrightarrow{2, g=1} (-3, -1/8) < 0. \tag{3.1}
$$

Equation $(3.1)$ isolates $(0, 4)$ as the exact cascade entry gate: by contrast, the smaller even $d = 0$ states $(0, 0)$ and $(0, 2)$ satisfy $R = 2^{-1} + 2c - 1 \in \{-1/2, 7/2\} \notin 3\mathbb{Z}_3$ on $e = 2, g = 1$, and never cross into $d < 0$.

### 3.2 Strict Open Slope Cones, Left-Resolving Dyadic Automata, and Slope–Ballot Duality

Equation $(3.1)$ reveals the exact mechanism needed to cross $\mathcal{C}_5^+$ safely: we do not need $\beta \le 5$ at every step, only the **strict inequality $c < 5 \cdot 2^d - 1$ immediately prior to an $e = 2$ step**, allowing the slope $\beta$ to expand up to $\psi_2(5) = 7$ immediately after $e = 2$ provided subsequent $e = 1$ steps contract $\beta$ via $\psi_1(\beta) = \frac{1 + 2\beta}{3}$ before the next $e = 2$ or parity-trap block.

Note first a universal parity invariant: for any state $(d, c)$ with $d \ge 0$ and $c \in \mathbb{Z}$ reachable from $(0, 0)$ along any word $u$, Theorem 1(1) gives $y_0(q) = 2^d n(q) + c \equiv 1 \pmod 2$ for odd $n(q)$, forcing $c \equiv 0 \pmod 2$ when $d = 0$ and $c \equiv 1 \pmod 2$ when $d \ge 1$ (abbreviated $c \equiv \mathbf{1}_{d \ge 1} \pmod 2$).

**Definition 3.1 (Parity-Admissible Strict Open Slope Cone $\mathcal{K}^\circ(\beta)$ and Slope Map $\psi_A$).** For any rational slope $\beta \ge 1$, define

$$
\mathcal{K}^\circ(\beta) := \{(0, 0)\} \;\cup\; \bigl\{(d, c) \in \mathbb{Z}_{\ge 0} \times \mathbb{Z}_{\ge 1} : c \equiv \mathbf{1}_{d \ge 1} \pmod 2 \;\text{ and }\; 1 \le c < \beta \cdot 2^d - 1\bigr\}. \tag{3.2}
$$

At $d = 0$ and $\beta = 5$, $\beta \cdot 2^0 - 1 = 4$, so the strict inequality $c < 4$ excludes the cascade gate $(0, 4)$. For $e \ge 1$, let $\psi_e(\beta) := \frac{1 + 2^e \beta}{3}$, and for an atom $A = (a_1, \dots, a_L) \in \mathbb{Z}_{\ge 1}^L$, define right-to-left composition $\psi_A(\beta) := \psi_{a_1}(\psi_{a_2}(\dots \psi_{a_L}(\beta)\dots))$.

**Lemma 3.2 (Unconditional One-Step Cone Monotonicity for $e \in \{1, 2\}$).** Let $\beta_v \ge 1$, with $\beta_v \le 5$ if $e = 2$. For every $(d, c) \in \mathcal{K}^\circ(\beta_v)$ and every $g \ge 1$ (with $g \ne e$ if $(d, c) = (0, 0)$) such that $(d', c') = \mathcal{P}_{e, g}(d, c) \ne \bot$, one has $(d', c') \in \mathcal{K}^\circ(\psi_e(\beta_v))$.

*Proof.* First check $d' = d + g - e \ge 0$: this is immediate if $e = 1$ or $d \ge 1$. If $e = 2$ and $d = 0$, then $(0, c) \in \mathcal{K}^\circ(\beta_v)$ with $\beta_v \le 5$ and $c$ even forces $c \in \{0, 2\}$; at $g = 1$ ($d' = -1$), $R = (4c - 1)/2 \in \{-1/2, 7/2\} \notin 3\mathbb{Z}_3$, so $g \ge 2$ and $d' \ge 0$. Since $d' \ge 0$ and $c \in \mathbb{Z}_{\ge 0}$, $3 c' = 2^{d'} + 2^g c - 1 \in \mathbb{Z}$ gives $c' \in \mathbb{Z}$ and $c' \equiv 3 c' \equiv 2^{d'} - 1 \equiv \mathbf{1}_{d' \ge 1} \pmod 2$. If $(d, c) = (0, 0)$, then $g \ne e$ and $3 \mid (2^{d'} - 1)$ force $d' \ge 2$ even, so $c' = (2^{d'} - 1)/3 \ge 1$ and $3 c' = 2^{d'} - 1 < (1 + 2^e \beta_v) 2^{d'} - 3 = 3(\psi_e(\beta_v) 2^{d'} - 1)$ since $1 + 2^e \beta_v \ge 3$ and $2 \cdot 2^{d'} > 2$. If $c \ge 1$, then $3 c' \ge 1 + 2 - 1 = 2 \implies c' \ge 1$, and $c < \beta_v \cdot 2^d - 1$ gives

$$
3 c' = 2^{d'} + 2^g c - 1 < 2^{d'} + 2^g(\beta_v \cdot 2^d - 1) - 1 = (1 + 2^e \beta_v) 2^{d'} - (2^g + 1) \le 3\,\psi_e(\beta_v) 2^{d'} - 3,
$$

whence $c' < \psi_e(\beta_v) 2^{d'} - 1$. $\blacksquare$

Synchronizing parity-trap atoms over $K \le 4$ requires one extra $1$ for $b = 4$ relative to $b = 3$: on $(1, 2, 3)$ at $\beta_v \le 7/4$, $b = 3$ births $(-2, -1/4)$ (annihilated by $2$) and positive states with $\psi_3(7/4) = 5$, giving $\psi_{(1,2,3)}(7/4) = \psi_1(\psi_2(5)) = \psi_1(7) = 5 \le 7$. On $b = 4$ at $\beta_v \le 7/4$, $(-2, -1/4)$ is likewise annihilated by $2$, but $\psi_4(7/4) = 29/3 > 5$ gives $\psi_{(1,2,4)}(7/4) = 247/27 > 7$ (for instance, $(4, 13) \in \mathcal{K}^\circ(7/4)$ pulls back via $(4, 13) \xrightarrow{4,1} (1, 9) \xrightarrow{2,1} (0, 6) \xrightarrow{1,1} (0, 4)$); prepending one extra $1$ in $(1, 1, 2, 4)$ contracts $\psi_{(1,1,2,4)}(7/4) = 521/81 < 7$ and annihilates $(0, 4)$ ($\theta = 4 \equiv 1 \pmod 3$) on the leading $1$.

**Lemma 3.3 (Unbounded-Exponent Tail and Core-Reentry Enclosure Across Parity-Trap Atoms).** Consider the four multi-letter parity-trap atom/cap pairs

$$
\mathcal{B}_{\mathrm{PT}}^{\mathrm{multi}} := \Bigl\{\bigl((1,2,3), \tfrac{7}{4}\bigr),\; \bigl((1,2,2,3), \tfrac{19}{16}\bigr),\; \bigl((1,1,2,4), \tfrac{7}{4}\bigr),\; \bigl((1,1,2,2,4), \tfrac{19}{16}\bigr)\Bigr\},
$$

and fix the finite discrepancy cutoff $d_{\mathrm{cut}} := 4$. For every $(A, \beta_{\mathrm{cap}}) \in \mathcal{B}_{\mathrm{PT}}^{\mathrm{multi}}$, every $\beta_v \in [1, \beta_{\mathrm{cap}}]$, and every $\beta_u \ge \psi_A(\beta_v)$:
1. *(Analytic high-discrepancy invariance).* Any $(d_{\mathrm{src}}, c_{\mathrm{src}}) \in \mathcal{K}^\circ(\beta_v)$ with $d_{\mathrm{src}} \ge 5 + \|A\| - |A|$ maintains $d_\ell \ge 5 \ge 1$ at every intermediate step of $A$ across **all** rival tuples $g \in \mathbb{Z}_{\ge 1}^{|A|}$; thus the positive-discrepancy inequality $3 c' < (1 + 2^e \beta) 2^{d'} - (2^g + 1) \le 3 \psi_e(\beta) 2^{d'} - 3$ holds at every letter $e \in A$ and every $g \in \mathbb{Z}_{\ge 1}$, yielding $d_{\mathrm{out}} \ge 5$ and $(d_{\mathrm{out}}, c_{\mathrm{out}}) \in \mathcal{K}^\circ(\psi_A(\beta_v)) \subseteq \mathcal{K}^\circ(\beta_u)$.
2. *(Lossless core-reentry exponent bounds).* After executing any backward step inside $A$ (or any proper prefix $A_{1..j}$), the remaining prefix contains only $1$s and at most two $2$s, so its remaining discrepancy drop is $\mathrm{rem\_drop} \le 2 < d_{\mathrm{cut}}$. Consequently, no intermediate state with $d' > d_{\mathrm{cut}} + \mathrm{rem\_drop}$ can re-enter $d_{\mathrm{out}} \le d_{\mathrm{cut}}$ within $A$: enumerating $1 \le g \le d_{\mathrm{cut}} + \mathrm{rem\_drop} - d + e$ on reentry inputs $5 \le d_{\mathrm{src}} \le 4 + \|A\| - |A|$ (`tail_atom_cache`) and $1 \le g \le 8 - d + e$ on core inputs $0 \le d \le 4$ (`pull_atom`) captures $100\%$ of transitions reaching $d_{\mathrm{out}} \le 4$.
3. *(Unbounded large-$g$ exits and intermediate $d < 0$ states).* Across all $(A, \beta_{\mathrm{cap}}) \in \mathcal{B}_{\mathrm{PT}}^{\mathrm{multi}}$ and all inputs in $\mathcal{K}^\circ(\beta_{\mathrm{cap}})$, only inputs with $0 \le d_{\mathrm{src}} \le 4$ can visit $d < 0$ inside $A$, and the **only** intermediate $d < 0$ states ever reached belong to $\{(-2, -1/4),\; (-1, 1/2),\; (-1, 3/2),\; (-1, 5/2)\}$ (`verify_lemma33_unbounded_atom_tails`). Specifically, $(-2, -1/4)$ immediately faces $e = 2$ and is annihilated for all $g \ge 1$; each $d = -1$ state satisfies $0 < c \le \beta_{\min} 2^{-1} - 1$ (where $\beta_{\min}$ propagates $\beta_v = 1$ right-to-left), so any exit to $d' = -1 + g - e \ge 0$ uses $g \ge e + 1 \ge 2$ ($-(2^g + 1) \le -5 < -3$) and satisfies $3 c' \le (1 + 2^e \beta_{\mathrm{cur}}) 2^{d'} - (2^g + 1) < 3(\psi_e(\beta_{\mathrm{cur}}) 2^{d'} - 1)$ across **all** $g \in \mathbb{Z}_{\ge 1}$, while zero $d < 0$ states survive to the left boundary of $A$. (Allowing $g = e$ on $(0, 0)$ at intermediate steps inside `pull_atom` only re-seeds internal proper-prefix trunk births already included in the upper enclosure.) $\blacksquare$

**Definition 3.4 (Left-Resolving Dyadic Slope Automata $\mathcal{A}_{\{1,2\}}(q, 7)$ and $\mathcal{A}_{\mathrm{PT}}(q, 7)$).** Fix $q \in \{4, 8, 16, 32, 64, 128\}$ and vertex set $V_q := \{\beta_k = k/q : q \le k \le 7q\}$ ($6q + 1$ vertices in $[1, 7]$). Given a finite suffix-free set of atom/cap pairs $(A, \beta_{\mathrm{cap}}(A))$, place a directed labeled edge $u \xrightarrow{A} v$ whenever

$$
\beta_v \le \beta_{\mathrm{cap}}(A) \qquad \text{and} \qquad \beta_u = \frac{\lceil q \cdot \psi_A(\beta_v) \rceil}{q} \le 7. \tag{3.3}
$$

Thus $\beta_u \ge \psi_A(\beta_v)$, and every pair $(v, A)$ has at most one incoming predecessor $u$. Because the atom set is suffix-free and the graph is left-resolving, distinct paths starting at a given right endpoint induce distinct valuation words without ambiguity. We define two nested families:
1. **Binary Cone SFT $\mathcal{A}_{\{1,2\}}(q, 7)$:** atoms $\mathcal{B}_{\mathrm{bin}} = \{((1), 7),\; ((2), 5)\}$.
2. **Parity-Trap SFT $\mathcal{A}_{\mathrm{PT}}(q, 7)$:** suffix-free atoms $\mathcal{B}_{\mathrm{PT}} := \mathcal{B}_{\mathrm{bin}} \cup \mathcal{B}_{\mathrm{PT}}^{\mathrm{multi}}$, i.e.,

$$
\mathcal{B}_{\mathrm{PT}} := \Bigl\{\bigl((1), 7\bigr),\; \bigl((2), 5\bigr),\; \bigl((1,2,3), \tfrac{7}{4}\bigr),\; \bigl((1,2,2,3), \tfrac{19}{16}\bigr),\; \bigl((1,1,2,4), \tfrac{7}{4}\bigr),\; \bigl((1,1,2,2,4), \tfrac{19}{16}\bigr)\Bigr\}. \tag{3.4}
$$

**Proposition 3.5 (Slope–Ballot Duality and Strict Finite-Integer Header Shielding).**
1. *(Four-Line Telescoping Bound).* For every $e \ge 1$ and $\beta > 0$, $\psi_e(\beta) = \frac{1 + 2^e \beta}{3} > \frac{2^e}{3} \beta$. By induction on $|A|$, $\psi_A(\beta) > \frac{2^{\|A\|}}{3^{|A|}} \beta$, so every edge $u \xrightarrow{A} v$ in $\mathcal{A}_{\{1,2\}}(q, 7)$ or $\mathcal{A}_{\mathrm{PT}}(q, 7)$ satisfies $\beta_u \ge \psi_A(\beta_v) > \frac{2^{\|A\|}}{3^{|A|}} \beta_v$. Along any path $u_0 \xrightarrow{A_1} u_1 \to \dots \xrightarrow{A_s} u_s$ of step length $m = \sum_{j=1}^s |A_j|$ and valuation sum $S_{\mathrm{walk}} = \sum_{j=1}^s \|A_j\|$, telescoping yields

$$
\frac{2^{S_{\mathrm{walk}}}}{3^m} \;<\; \prod_{j=1}^s \frac{\beta_{u_{j-1}}}{\beta_{u_j}} \;=\; \frac{\beta_{u_0}}{\beta_{u_s}} \;\le\; \frac{7}{1} \;=\; 7, \tag{3.5}
$$

and $2^{\|p\|} / 3^{|p|} < 7$ likewise holds at every intermediate prefix $p$ inside multi-letter atoms since $\psi_{A[:j]}(1) < \beta_u \le 7$ on all $660$ multi-step edges.
2. *(Strict Finite-Integer All-Prefix Survival $q_0(w) = 0$).* Prepending $1^5$ to any walk of $\mathcal{A}_{\{1,2\}}(q, 7)$ gives $2^{S_i} / 3^i < (2/3)^5 \cdot 7 = 224/243 < 1$ for all $i \ge 1$. Prepending $1^{10}$ to any walk of $\mathcal{A}_{\mathrm{PT}}(q, 7)$ gives $3^k / 2^{S_k} > 3^{10}/(7 \cdot 2^{10}) = 59{,}049 / 7{,}168 > 8$ for all $k \ge 10$ (and $\ge 3/2$ for $1 \le k \le 9$). Because cone invariance (Theorem 2(1)) places every atom-boundary pullback in $d \ge 0, c \ge 1$ ($y_k \ge x_k + 1 > n$) and the worst internal split inside multi-letter atoms occurs at $(d, c) = (-2, -1/4)$ on $e \in \{3, 4\}$—where $y_{i-1} = \frac{1}{4} x_{i-1} - \frac{1}{4} > \frac{59{,}049}{28{,}672} n - \frac{1}{4} > 2.059 n - 0.25 > n$ for every $n \ge 1$—every prefix of $1^5 \cdot \mathcal{A}_{\{1,2\}}(q, 7)^{\mathbb{N}}$ and $1^{10} \cdot \mathcal{A}_{\mathrm{PT}}(q, 7)^{\mathbb{N}}$ belongs to $\mathcal{I}_i^{\mathrm{strict}} \subseteq \mathcal{I}_i$. $\blacksquare$

---

### 3.3 Exact Certification Past $3/4 = 0.75$ and Two-Sided Asymptotic / Finite-$X$ Sandwiches

**Theorem 2 (Certified Dyadic Cone Invariance, Crossing $3/4$, and Two-Sided Sandwiches).**
1. *(Zero-Violation Cone Enclosure Across All Unbounded $g \in \mathbb{Z}_{\ge 1}$).* For every $q \in \{4, 8, 16, 32, 64, 128\}$, propagating an upper enclosure on the finite core $0 \le d \le 4$ across $V_q$ (`certify_sft_cone_closure`)—seeded from $(0, 0)$, from all $486$ internal proper-prefix births $\mathcal{P}_{A[:j]}((0, 0))$ ($1 \le j < |A|$), and from all $19{,}031$ tail-reentry states $d_{\mathrm{src}} \in \{5, \dots, 4 + \|A\| - |A|\}$ in $\mathcal{K}^\circ(\beta_v)$ entering $d \le 4$—together with Lemmas 3.2 and 3.3 for all unbounded $g \in \mathbb{Z}_{\ge 1}$ and $d \ge 5$, certifies that every reachable symbolic pullback state at vertex $u \in V_q$ along $\mathcal{A}_{\{1,2\}}(q, 7)$ and $\mathcal{A}_{\mathrm{PT}}(q, 7)$ lies strictly inside $\mathcal{K}^\circ(\beta_u)$ ($0$ violations across $26{,}975$ enclosed core states on $\mathcal{A}_{\{1,2\}}(128, 7)$ and $33{,}139$ enclosed core states on $\mathcal{A}_{\mathrm{PT}}(128, 7)$).
2. *(Certified $2$-Adic Survival Rates Exceeding $3/4$).* Expanding multi-letter atoms into unit-step edges weighted by $2^{-e}$, isolating the top strongly connected component via Tarjan's algorithm (aperiodic via unit self-transitions), and applying rational Collatz–Wielandt bounds (`cw_top_scc_bounds`) certifies

$$
\lambda_{\mu_2}\bigl(1^5 \cdot \mathcal{A}_{\{1,2\}}(128, 7)^*\bigr) \in \left[\frac{91{,}496{,}991{,}773{,}239}{123{,}558{,}943{,}184{,}692},\; 0.740513\right], \quad \text{so } \lambda_{\mu_2}(\mathcal{I} \cap \{1, 2\}^*) \ge \mathbf{0.740512}, \tag{3.6}
$$

$$
\lambda_{\mu_2}\bigl(1^{10} \cdot \mathcal{A}_{\mathrm{PT}}(128, 7)^*\bigr) \in \left[\frac{334{,}085{,}797{,}246{,}459}{444{,}797{,}811{,}679{,}880},\; 0.751096\right], \quad \text{so } \lambda_{\mu_2}(\mathcal{I}) \ge \mathbf{0.751095} > \frac{3}{4}. \tag{3.7}
$$

Combining $(3.7)$ with the exact Cramér ballot upper bound on $\mathcal{N}_T \supseteq \mathcal{I}_T$ establishes the unconditional two-sided sandwich

$$
\mathbf{0.751095} \;<\; \lambda_{\mu_2}(\mathcal{I}) \;\le\; \inf_{\vartheta < 0} 2^{-\vartheta \alpha_c} \mathbb{E}[2^{\vartheta e}] \;=\; (\alpha_c - 1)\left(\frac{2(\alpha_c - 1)}{\alpha_c}\right)^{-\alpha_c} \;\in\; [\mathbf{0.94650457},\; \mathbf{0.94650458}], \tag{3.8}
$$

where $\alpha_c := \log_2 3$.
3. *(Unconditional Finite-$X$ Integer Survivor Count).* For large $X \ge 1$, set $T(X) := \lfloor \log_3 X \rfloor$. Every $T$-step cylinder $\mathrm{Cyl}(w)$ generated by $1^{10} \cdot \mathcal{A}_{\mathrm{PT}}(128, 7)$ satisfies $2^{S(w)+1} < 2^{11} \cdot 7 \cdot 3^{T - 10} = \frac{14{,}336}{59{,}049} 3^T < 0.243 X$, and its certified combinatorial word-growth rate satisfies $\rho_{\mathrm{comb}}(\mathcal{A}_{\mathrm{PT}}(128, 7)) \le 1.897128 < 2.253285 \le 3 \lambda_{\mu_2}(\mathcal{A}_{\mathrm{PT}}(128, 7))$. Summing $\#(\mathrm{Cyl}(w) \cap [1, X]) > \frac{X}{2^{S(w)+1}} - 1$ over the top SCC yields an explicit constant $c_0 > 0$ such that for all sufficiently large $X$,

$$
\#\bigl\{1 \le n \le X \text{ odd} : \forall\, 1 \le i \le \lfloor \log_3 X \rfloor,\; \forall\, 1 \le m \le i,\; U^{-m}(U^i(n)) \cap [1, n - 1] = \emptyset\bigr\} \;\ge\; c_0\, X^{\mathbf{0.739469}}, \tag{3.9}
$$

whereas the count of odd integers $n \le X$ with $w_{\lfloor \log_3 X \rfloor}(n) \in \mathcal{N}_{\lfloor \log_3 X \rfloor}$ is at most $O(X^{\mathbf{0.949956}})$.

*Proof of $(3.8)$ and $(3.9)$.* Under i.i.d. $\mathrm{Geom}(1/2)$ valuations $\mathbb{P}(e_j = k) = 2^{-k}$, $\mu_2(\mathcal{N}_T) \le \mathbb{P}(S_T < T \alpha_c)$. Setting $u = 2^{\vartheta - 1} \in (0, 1/2)$ ($\vartheta < 0$), Markov's inequality gives

$$
\mu_2(\mathcal{N}_T) \;\le\; \inf_{0 < u < 1/2} (2u)^{-T \alpha_c} \Bigl(\sum_{k=1}^\infty u^k\Bigr)^T \;=\; \left(\inf_{0 < u < 1/2} (2u)^{-\alpha_c} \frac{u}{1 - u}\right)^T.
$$

Minimizing $(1 - \alpha_c) \ln u - \ln(1 - u)$ yields $\frac{1 - \alpha_c}{u} + \frac{1}{1 - u} = 0 \iff u^* = \frac{\alpha_c - 1}{\alpha_c} \in (0, 1/2)$ ($1 < \alpha_c < 2$), where $\frac{u^*}{1 - u^*} = \alpha_c - 1$, giving $(\alpha_c - 1)(2(\alpha_c - 1)/\alpha_c)^{-\alpha_c} \in [0.94650457, 0.94650458]$ via $160$-bit `RatInterval` arithmetic. For $(3.9)$, restricting to length-$(T - 10)$ walks inside the top strongly connected component $\mathcal{C}_{\max}$ of the step-expanded graph of $\mathcal{A}_{\mathrm{PT}}(128, 7)$ that start and end at base vertices in $V_{128}$ (positive density by aperiodicity), the positive Collatz–Wielandt lower eigenvector gives $\sum_w 2^{-\|w\|} \ge c_1 \lambda_{\mathrm{PT}}^T$ while the positive combinatorial upper eigenvector gives $\#\{w\} \le c_2 (1.897128)^T$. Since $2^{S(w)+1} < X$ at $T = \lfloor \log_3 X \rfloor$, each progression $n_0(w) + 2^{S(w)+1} q$ contributes $> \frac{X}{2^{S(w)+1}} - 1$ disjoint odd integers in $[1, X]$ belonging to $\mathcal{I}_T^{\mathrm{strict}}$ by Proposition 3.5(2). Summing over $w$ gives $\frac{X}{2} c_1 \lambda_{\mathrm{PT}}^T - c_2 (1.897128)^T \ge c_0 X^{1 + \log_3 \lambda_{\mathrm{PT}}}$ with $1 + \log_3(334{,}085{,}797{,}246{,}459 / 444{,}797{,}811{,}679{,}880) > 0.739469$. $\blacksquare$

| Grid $q$ | $\|V_q\|$ | $\mathcal{A}_{\{1,2\}}(q, 7)$ $\lambda_{\mu_2}$ lower | $\mathcal{A}_{\{1,2\}}$ enclosed core | $\mathcal{A}_{\mathrm{PT}}(q, 7)$ $\lambda_{\mu_2}$ lower | $\mathcal{A}_{\mathrm{PT}}$ $\rho_{\mathrm{comb}}$ upper | $\mathcal{A}_{\mathrm{PT}}$ enclosed core | Tail reentry seeds | Violations |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| $4$ | $25$ | $0.734974$ | $877$ | $0.741897$ | $1.850905$ | $1{,}019$ | $639$ | $0$ |
| $8$ | $49$ | $0.738828$ | $1{,}708$ | $0.747043$ | $1.877041$ | $2{,}084$ | $1{,}232$ | $0$ |
| $16$ | $97$ | $0.739697$ | $3{,}411$ | $0.749333$ | $1.888585$ | $4{,}137$ | $2{,}443$ | $0$ |
| $32$ | $193$ | $0.740165$ | $6{,}757$ | **$0.750450$** | $1.893411$ | $8{,}344$ | $4{,}823$ | $0$ |
| $64$ | $385$ | $0.740437$ | $13{,}515$ | **$0.750895$** | $1.896036$ | $16{,}669$ | $9{,}540$ | $0$ |
| $128$ | $769$ | **$0.740512$** | $26{,}975$ | **$0.751095$** | $1.897128$ | $33{,}139$ | $19{,}031$ | $0$ |

*Table 1: Certified rational Collatz–Wielandt progression of the binary cone SFT $\mathcal{A}_{\{1,2\}}(q, 7)$ and the suffix-free parity-trap SFT $\mathcal{A}_{\mathrm{PT}}(q, 7)$ across dyadic slope grids $q \in \{4, \dots, 128\}$ (`results/verify_slope_ballot_parity.json`, Module 2). Reported core state counts represent upper enclosures on $0 \le d \le 4$ seeded from $(0, 0)$, internal atom births, and high-$d$ reentry bounds. In every row, Collatz–Wielandt upper and lower bounds agree to $10^{-6}$, minimum discrepancy and offset satisfy $d \ge 0, c \ge 0$, and cone violations equal $0$; $80$ walks ($1{,}301$ prefixes) also passed independent integer inverse-tree stress checks.*

![Certified survival rate progression crossing 3/4 and rogue-separatrix cone phase portrait](supplement/figure-1.png)

*Figure 1: (a) Certified rational Collatz–Wielandt $2$-adic survival rates across dyadic slope grids $q \in \{4, 8, 16, 32, 64, 128\}$, comparing prior static-cone baselines ($\langle(1),(1,2)\rangle^*$ at $0.683013$ and $\mathcal{M}_\infty \in (0.693, 0.694)$ [16]), the binary cone SFT $\mathcal{A}_{\{1,2\}}(q, 7)$ ($0.740512 < 3/4$), and the parity-trap SFT $\mathcal{A}_{\mathrm{PT}}(q, 7)$ crossing the $3/4 = 0.75$ binary ceiling at $q = 32$ ($0.750450$) and reaching $0.751095$ at $q = 128$. (b) Symbolic cone phase portrait in $(d, c)$, contrasting $\mathcal{C}_5^+$ and $\mathcal{K}^\circ(7)$ against the rogue-separatrix cascade $(3.1)$ on the $T = 22$ binary witness $w_{22}$.*

---

## 4. Zero-Truncation Binary Escape Thresholds and Non-Monotone Prefix Shielding

In [11, Theorem 4], balanced binary words $\mathcal{B}(\alpha)$ up to slope $\log_2 3 - 1.26 \times 10^{-11}$ were proved division-minimal outside the two excluded open bands $(32/21, 26/17) \cup (11/7, 19/12)$, where balanced windows of lengths $30$ and $23$ fail matched-depth minimality (and on the $22$-letter Sturmian window $W_7^2 W_5 (1,2,1)$ studied in [11, 16], the horizon-$22$ collision $U^{22}(n + 4) = U^{22}(n)$ is a $\delta = 0$ tie $y = n + 4 > n$ rather than a smaller predecessor at $T = 22$). For general (unbalanced) binary ballot words $\mathcal{N}_T \cap \{1, 2\}^T$, we now determine the exact first-escape horizons via a reverse-prefix dynamic program free of heuristic discrepancy or state-table truncation.

**Lemma 4.1 (Exact Ballot-Drop Discrepancy Bound).** Let $w = (e_1, \dots, e_T) \in \mathcal{N}_T \cap \{1, 2\}^T$ with $T \le 22$. Because $2^{S_T} < 3^T$ and $2^{34} = 17{,}179{,}869{,}184 < 3^{22} = 31{,}381{,}059{,}609 < 2^{35} = 34{,}359{,}738{,}368$, $w$ satisfies $S_T \le 34$, so at most $S_T - T \le 12$ entries of $w$ equal $2$ (and for any $T \le 22$, $\sum_{j=1}^T (e_j - 1) \le 12$). Along any backward symbolic pullback $(d_r, c_r) = (0, 0) \to \dots \to (d_0, c_0)$ on a suffix of length $r \le T \le 22$, each step reduces discrepancy by at most $e_j - g_j \le e_j - 1 \in \{0, 1\}$, and at most $12$ steps have $e_j = 2$. Consequently, any intermediate state $(d_\ell, c_\ell)$ ($\ell$ steps from the right end of the suffix) capable of reaching $d_0 \le 0$ within $22$ total steps satisfies

$$
d_\ell \;\le\; \min(22 - \ell,\; 12). \tag{4.1}
$$

**Lemma 4.2 (Exact Reverse-Prefix Ballot Dominance and Frozen-Escape Recurrence).** For any non-empty word $u = (a_1, \dots, a_L) \in \{1, 2\}^L$, define its **worst-prefix ballot ratio** $M(u) := \max_{1 \le j \le L} 2^{a_1 + \dots + a_j} / 3^j \in \mathbb{Q}_{> 0}$. Then $u \in \mathcal{N}_L \iff M(u) < 1$, and prepending $e \in \{1, 2\}$ on the left obeys the exact monotone recurrence

$$
M(e \cdot u) \;=\; \max\!\left(\frac{2^e}{3},\; \frac{2^e}{3} M(u)\right) \;=\; \frac{2^e}{3} \max\bigl(1,\; M(u)\bigr). \tag{4.2}
$$

In particular, $M(u_1) \le M(u_2) \implies M(p \cdot u_1) \le M(p \cdot u_2)$ for every left prefix $p \in \{1, 2\}^*$. Building suffixes $u \in \{1, 2\}^L$ right-to-left from $(0, 0)$ (requiring $g_L \ne a_L$ at $L = 1$):
1. *(Active pullback states `best_at_L`):* Retaining a single witness minimizing $M(u)$ at each reachable $(d, c)$ satisfying $(4.1)$ (peak table size $15{,}943$ states) preserves $100\%$ of minimal-horizon full-depth escapes ($M(u) < 1$ with $d < 0$, or $d = 0$ and $c < 0$) and $100\%$ of minimal-ballot continuations.
2. *(Frozen intermediate-split escapes `frozen_at_L`):* By Theorem 1(1), a word $w = p \cdot u$ ($|p| = k \ge 1, |u| = r \ge 1, L = k + r$) escapes at suffix $u$ via $(d, c)$ ($d < 0$) if and only if $M(p \cdot u) < 1$ and $P(p) := 2^{\|p\|} / 3^k > 2^d$. Updating $(M_{\mathrm{new}}, P_{\mathrm{new}}, 2^d) = \bigl(\frac{2^e}{3}\max(1, M),\; \frac{2^e}{3} P,\; 2^d\bigr)$ whenever $P_{\mathrm{new}} > 2^d$ and retaining minimal $M$ per exact pair $(P, 2^d)$ is therefore $100\%$ exact without truncation across $1 \le L \le 22$. $\blacksquare$

**Theorem 3 (Exact Binary Escape Thresholds and Non-Monotone Prefix Shielding).**
1. *(Zero Escapes Through $T = 18$).* For every $1 \le T \le 18$, $(\mathcal{N}_T \cap \{1, 2\}^T) \setminus \mathcal{I}_T = \emptyset$: every binary ballot-admissible cylinder through horizon $18$ is asymptotically all-prefix inverse-minimal ($\mu_2(\mathcal{I}_{18} \cap \{1, 2\}^{18}) = \mu_2(\mathcal{N}_{18} \cap \{1, 2\}^{18}) = 0.00307063\dots$ across all $65{,}192$ words).
2. *(Exact Intermediate-Prefix Threshold $T_{\min}(\{1, 2\}) = 19$).* At $T = 19$, **exactly $2$ out of $130{,}384$** words in $\mathcal{N}_{19} \cap \{1, 2\}^{19}$ escape $\mathcal{I}_{19}$ (and $11$ out of $256{,}460$ escape at $T = 20$). An explicit witness at $T = 19$ is

$$
w_{19} = \bigl(1, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1\bigr) \in \mathcal{N}_{19} \setminus \mathcal{I}_{19}, \tag{4.3}
$$

with $S_{19} = 29$ ($2^{29} = 536{,}870{,}912 < 3^{19} = 1{,}162{,}261{,}467$), cylinder base $n_0(w_{19}) = 974{,}318{,}247$, and $x_{19,0} = 2{,}109{,}282{,}761$. At suffix length $r = 18$ ($k = 1$), the forward-indexed rival valuation word $g = (1^{11}, 2, 2, 1, 4, 3, 1, 3)$ ($g_{18} = 3 \ne 1 = e_{19}$, $\|g\| = 27$, $2^{27} \cdot 3^1 = 402{,}653{,}184 < 2^{29}$) yields $y_1(q) = 730{,}738{,}687 + 3 \cdot 2^{28} q$, satisfying $4 y_1(q) = 3 n(q) + 7$, hence $y_1(q) < n(q)$ for all $q \ge 0$.
3. *(Exact Full-Depth Threshold $T_{\min}^{\mathrm{full}}(\{1, 2\}) = 22$).* No word in $\mathcal{N}_T \cap \{1, 2\}^T$ escapes at full depth $r = T$ for $1 \le T \le 21$. At $T = 22$, full-depth escape first occurs on

$$
w_{22} = \bigl(1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1, 2, 1, 2, 2, 1\bigr), \tag{4.4}
$$

with $S_{22} = 34$, $n_0(w_{22}) = 34{,}086{,}759{,}079$, and $x_{22,0} = 62{,}263{,}490{,}321$. Pulling $(0, 0)$ backward along the forward-indexed rival word $g = (2, 1^{15}, 2, 2, 1, 4, 3, 3)$ ($g_{22} = 3 \ne 1 = e_{22}$) breaches $c^* = 5 \cdot 2^d - 1$ at $(3, 39) \xrightarrow{2, g=1} (2, 27)$ during the $2^4$ burst (Figure 1(b)) and cascades via $(3.1)$ to $(d_0, c_0) = (-2, -3/4)$, yielding $U^{22}(y_0(q)) = U^{22}(n(q))$ at $y_0(q) = (n(q) - 3)/4 < n(q)$ for all $q \ge 0$ ($y_0(0) = 8{,}521{,}689{,}769$).
4. *(Non-Monotone Prefix Shielding Dichotomy).*
   - **Pure-climb ray failure:** Any state satisfying $c = 2^d - 1$ is an exact algebraic fixed point of $(e = 1, g = 1)$ since $\mathcal{P}_{1, 1}(d, 2^d - 1) = (d, (2^d + 2(2^d - 1) - 1)/3) = (d, 2^d - 1)$. Because $(-2, -3/4)$ satisfies $-3/4 = 2^{-2} - 1$, prepending arbitrarily many $1$s leaves $(-2, -3/4)$ invariant: **$1^M \cdot w_{22} \in \mathcal{N}_{M+22} \setminus \mathcal{I}_{M+22}$ escapes at full depth for every $M \ge 0$.**
   - **Single-$2$ parity shift:** Inserting a single $e = 2$ before $w_{22}$ shifts $(-2, -3/4)$ on its unique $d \le 0$ continuation $g = 2$ to $\mathcal{P}_{2, 2}(-2, -3/4) = (-2, -5/4)$ ($g = 1$ gives $R = -19/8 \notin 3\mathbb{Z}_3$). On $(-2, -5/4)$, $\theta' = 4(-5/4) = -5 \equiv 1 \pmod 3$, which by Theorem 1(2) is annihilated in one step by $e = 1$. Consequently, $1^k \cdot (2) \cdot w_{22}$ fails forward ballot admissibility for $k \in \{0, 1\}$, escapes at intermediate split $r = 22$ for $2 \le k \le 4$, and belongs to **$\mathcal{I}_{k+23}$ across all prefixes for every $k \ge 5$** (Figure 2(b)).

*Proof.* Parts 1–3 follow from the exact reverse-prefix DP under Lemmas 4.1 and 4.2 (`verify_theorem3_binary_thresholds_and_shielding`), cross-checked via incremental Hensel cylinder DFS through $T = 20$ and direct evaluation of $U^{19}$ and $U^{22}$ on $n_0(w_{19})$ and $n_0(w_{22})$. For Part 4, on $1^M \cdot w_{22}$, $S_{M+22} = M + 34$ satisfies $2^{M+34} < 3^{M+22}$ for all $M \ge 0$, while iterating $\mathcal{P}_{1,1}(-2, -3/4) = (-2, -3/4)$ $M$ times yields $y_0(q) = (n(q) - 3)/4 < n(q)$ at full depth $r = M + 22$ for every $M \ge 0$. Conversely, on $1^k \cdot (2) \cdot w_{22}$, every negative-discrepancy state emerging from $w_{22}$ either dies on $e = 2$ or lands in $\theta' \equiv 1 \pmod 3$ and dies on the adjacent $e = 1$. At the split boundary immediately preceding $w_{22}$ (prefix $1^k \cdot (2)$ of length $k + 1$ and sum $S_{k+1} = k + 2$, suffix $w_{22}$ of length $r = 22$ reaching $(d, c) = (-2, -3/4)$), Theorem 1(1) shows that intermediate escape occurs if and only if

$$
2^{-2} \cdot 3^{k+1} < 2^{k+2} \iff 3^{k+1} < 2^{k+4} \iff k \le 4 \qquad \bigl(3^5 = 243 < 256 = 2^8,\;\; 3^6 = 729 > 512 = 2^9\bigr). \tag{4.5}
$$

Verifying $1^5 \cdot (2) \cdot w_{22} \in \mathcal{I}_{28}$ directly and noting that increasing $k \ge 5$ multiplies $3^{k'}/2^{S_{k'}}$ by $(3/2)^{k-5} \ge 1$ at every split inside $(2) \cdot w_{22}$ while all pullbacks crossing into $1^k$ have $d \ge 0, c \ge 1$, we conclude $1^k \cdot (2) \cdot w_{22} \in \mathcal{I}_{k+23}$ for all $k \ge 5$. $\blacksquare$

![Binary escape census through T=20, non-monotone prefix shielding on w22, and joint 2-adic / 3-adic persistence](supplement/figure-2.png)

*Figure 2: (a) Exact zero-truncation binary ballot census across $1 \le T \le 20$, showing $0$ escaping words for $1 \le T \le 18$, $2$ escapes out of $130{,}384$ at $T_{\min}(\{1,2\}) = 19$, and $11$ out of $256{,}460$ at $T = 20$. (b) Non-monotone prefix shielding on $w_{22}$: pure-climb prefixes $1^M \cdot w_{22}$ escape for every $M \ge 0$, whereas $1^k \cdot (2) \cdot w_{22}$ transitions sharply into $\mathcal{I}_{k+23}$ at $k = 5$ via $(4.5)$. (c) Simultaneous certified $2$-adic survival rate $\lambda_{\mu_2}$ and all-horizon $3$-adic unpaid shares outside $\mathcal{P}(w)$ across trajectory shifts (Table 2).*

---

## 5. Garden-of-Eden Dichotomy and Joint All-Horizon $3$-Adic Persistence Above $3/4$

### 5.1 Unconditional Garden-of-Eden Closure on $\mathcal{A}_{\{1,2\}}(q, 7)$ vs. Tie Breakdown at $e = 3$

To unite $> 3/4$ $2$-adic survival with all-horizon $3$-adic persistence $(1.3)$–$(1.4)$, we classify low-discrepancy states $(d, c)$ ($d \in \{0, 1\}$) reachable along $\mathcal{A}_{\{1,2\}}(q, 7)$ and $\mathcal{A}_{\mathrm{PT}}(q, 7)$. Any reachable $(0, c)$ with $c > 0$ creates a $\delta = 0$ tie $U^t(n + c) = U^t(n)$; for $c = 2$, taking extra depth $u = 1$ with $f_1 = 1$ gives $y_{-1} = (2(n + 2) - 1)/3 = \frac{2}{3} n + 1 < n$, an odd integer across $100\%$ of $n \equiv 0 \pmod 3$, collapsing $\overline{\mathsf{Unpaid}}_3$ to $0$.

**Theorem 4 (Garden-of-Eden Dichotomy and All-Horizon, All-Depth $3$-Adic Persistence on $1^{10} \cdot \mathcal{A}_{\mathrm{PT}}(128, 7)^{\mathbb{N}}$).**
1. *(Unconditional Garden-of-Eden Isolation on $\mathcal{A}_{\{1,2\}}(q, 7)$).* Define the seven-state set

$$
\mathcal{G}_{\mathrm{GoE}} := \bigl\{(0, 2),\; (0, 4),\; (1, 3),\; (1, 9),\; (1, 11),\; (2, 9),\; (2, 13)\bigr\}. \tag{5.1}
$$

Along any binary trajectory preserving $\mathcal{K}^\circ(7)$ with $e = 2$ gated at $\mathcal{K}^\circ(5)$, every predecessor of $\mathcal{G}_{\mathrm{GoE}}$ inside $\mathcal{K}^\circ(\beta_{\mathrm{cap}}(e))$ already belongs to $\mathcal{G}_{\mathrm{GoE}}$ (forming two closed Garden-of-Eden $2$-cycles $(0, 2) \xleftrightarrow{1,2} (1, 3)$ and $(1, 9) \xleftrightarrow{1,2} (2, 13)$ plus dead-end feeders $(0, 4), (1, 11), (2, 9)$). Since $(0, 0) \notin \mathcal{G}_{\mathrm{GoE}}$, $\mathcal{G}_{\mathrm{GoE}}$ is unreachable across all $d \ge 0$ and all $q \ge 1$. Moreover, for every multiple $q$ of $8$ (including $q = 128$), the explicit words $(2, 1)$, $(2, 2, 2, 2, 1)$, and $(2, 2, 2, 2, 1, 2, 1)$ are admissible in $\mathcal{A}_{\{1,2\}}(8, 7) \subseteq \mathcal{A}_{\{1,2\}}(q, 7)$ and realize $(1, 1), (1, 5), (1, 7)$ from $(0, 0)$, proving the exact reachable sets

$$
\mathcal{R}_0\bigl(\mathcal{A}_{\{1,2\}}(q, 7)\bigr) = \{(0, 0)\}, \qquad \mathcal{R}_1\bigl(\mathcal{A}_{\{1,2\}}(q, 7)\bigr) = \{(1, 1),\; (1, 5),\; (1, 7)\}. \tag{5.2}
$$

2. *(Garden-of-Eden Breakdown at $e = 3$ on Unanchored $\mathcal{A}_{\mathrm{PT}}$).* At $e = 3$, the transition $(1, 1) \xrightarrow{3, g=3} (1, 3) \xrightarrow{2, g=1} (0, 2)$ bridges the reachable state $(1, 1)$ directly into the binary Garden-of-Eden $2$-cycle. Specifically, $w_{\mathrm{tie}} = (2, 1, 2, 3, 2, 1)$ ($S_6 = 11$, $n_0 = 3{,}769$) is admissible in $\mathcal{A}_{\mathrm{PT}}(q, 7)$ and satisfies the exact cylinder-wide collision

$$
U^6(n + 2) = U^6(n) \qquad \text{for every } n = 3{,}769 + 4{,}096 q \in \mathrm{Cyl}(w_{\mathrm{tie}}), \tag{5.3}
$$

with forward-indexed rival valuation word $g = (1, 2, 1, 3, 1, 3)$ ($g_6 = 3 \ne 1 = e_6$), collapsing $\overline{\mathsf{Unpaid}}_3(w_{\mathrm{tie}} \cdot \dots) = 0$ at extra depth $u = 1$.
3. *($1^4$ Cone Compression and Certified All-Horizon, All-Depth $3$-Adic Persistence on $1^{10} \cdot \mathcal{A}_{\mathrm{PT}}(128, 7)^{\mathbb{N}}$).* Factor the $1^{10}$ header as $1^{10} = 1^6 \cdot 1^4$. Iterating $\psi_1$ four times compresses $\beta_{\max} = 7$ via $7 \mapsto 5 \mapsto \frac{11}{3} \mapsto \frac{25}{9} \mapsto \frac{59}{27}$:

$$
\psi_{1^4}(7) = \left(\frac{2}{3}\right)^4 (7 - 1) + 1 = \frac{59}{27} < 5. \tag{5.4}
$$

Consequently, every non-trivial pullback entering step $6$ from any continuation in $1^4 \cdot \mathcal{A}_{\mathrm{PT}}(128, 7)^{\mathbb{N}}$ (including $1^{10} \cdot w_{\mathrm{tie}} \in \mathcal{I}_{16}^{\mathrm{strict}}$) satisfies $d' \ge 1$ and $1 \le c' < \frac{59}{27} 2^{d'} - 1 \le 5(2^{d'} - 1)$, lying strictly inside $\mathcal{C}_5^+ \setminus \{(0, 0)\}$ (enclosed by at most $335$ integer states on $1 \le d' \le 8$, with $d' = 1$ compressed to the singleton $\{(1, 1)\}$). Propagating this $335$-state compressed enclosure plus the $\mathcal{C}_5^+$ tail across $1^6$ via exact rational conditional cost tables $G_r(\delta)$ and multi-scale mod-$3^m$ equidistribution certifies that every infinite word $w \in 1^{10} \cdot \mathcal{A}_{\mathrm{PT}}(128, 7)^{\mathbb{N}}$ simultaneously achieves $\lambda_{\mu_2} \ge 0.751095 > 3/4$ and leaves

$$
\overline{\mathsf{Unpaid}}_\times(w) \;\ge\; \mathbf{0.19955319} \;>\; 19.95\%, \qquad \overline{\mathsf{Unpaid}}_3(w) \;\ge\; \mathbf{0.82429853} \;>\; 82.42\% \tag{5.5}
$$

outside the measurable countable union $\mathcal{P}(w)$ across all horizons $t \ge 0$ and all unbounded extra inverse depths $u \ge 0$.

*Proof.* For Part 1, for each $(d', c') \in \mathcal{G}_{\mathrm{GoE}}$ in $(5.1)$, $M := 3 c' + 1 - 2^{d'} \in \{6, 12, 8, 26, 32, 24, 36\} > 0$ admits only finitely many factorizations $2^g c = M$ ($1 \le g \le v_2(M)$, $d = d' + e - g \ge 0$, $c \equiv \mathbf{1}_{d \ge 1} \pmod 2$, $(d, c) \in \mathcal{K}^\circ(\beta_{\mathrm{cap}}(e))$):
- $(0, 2)$ ($M = 6$): $(g, c) = (1, 3) \implies (0, 3)$ (invalid parity) or $(1, 3) \in \mathcal{G}_{\mathrm{GoE}}$.
- $(0, 4)$ ($M = 12$): $(1, 6) \implies (0, 6) \notin \mathcal{K}^\circ(7)$ or $(1, 6)$ (invalid parity); $(2, 3) \implies (-1, 3)$ or $(0, 3)$ (invalid).
- $(1, 3)$ ($M = 8$): $(1, 4) \implies (d \ge 1, 4)$ (invalid parity); $(2, 2) \implies (0, 2) \in \mathcal{G}_{\mathrm{GoE}}$ or $(1, 2)$ (invalid parity); $(3, 1) \implies (-1, 1)$ or $(0, 1)$ (invalid).
- $(1, 9)$ ($M = 26$): $(1, 13) \implies (1, 13) \notin \mathcal{K}^\circ(7)$ ($13 \not< 13$) or $(2, 13) \in \mathcal{G}_{\mathrm{GoE}}$.
- $(1, 11)$ ($M = 32$): even $c \in \{16, 8, 4, 2\}$ requires $d = 0$, giving $(0, 8) \notin \mathcal{K}^\circ(7)$ ($e = 1, g = 2$) or $(0, 4) \in \mathcal{G}_{\mathrm{GoE}}$ ($e = 2, g = 3$); $(5, 1)$ gives $d = e - 4 < 0$.
- $(2, 9)$ ($M = 24$): $(1, 12), (2, 6)$ give $d \ge 1$ with even $c$; $(3, 3)$ gives $(0, 3)$ (invalid parity) or $(1, 3) \in \mathcal{G}_{\mathrm{GoE}}$.
- $(2, 13)$ ($M = 36$): $(1, 18)$ gives $d \ge 2$ with even $c$; $(2, 9)$ gives $(1, 9) \in \mathcal{G}_{\mathrm{GoE}}$ or $(2, 9) \in \mathcal{G}_{\mathrm{GoE}}$.

Since $\mathcal{K}^\circ(7)$ contains $\{0, 2, 4\}$ at $d = 0$ and $\{1, 3, 5, 7, 9, 11\}$ at $d = 1$, excluding $\mathcal{G}_{\mathrm{GoE}}$ proves $\mathcal{R}_0 \subseteq \{(0, 0)\}$ and $\mathcal{R}_1 \subseteq \{(1, 1), (1, 5), (1, 7)\}$ for all $q \ge 1$. When $q = 8m$ ($m \ge 1$), $\lceil 8m x \rceil / (8m) \le \lceil 8 x \rceil / 8$ and monotonicity of $\psi_e$ imply that every walk in $\mathcal{A}_{\{1,2\}}(8, 7)$ starting from $\beta_{\mathrm{end}} = 1$ remains a valid walk in $\mathcal{A}_{\{1,2\}}(q, 7)$, so the verified $\mathcal{A}_{\{1,2\}}(8, 7)$ witnesses $(2, 1)$, $(2, 2, 2, 2, 1)$, and $(2, 2, 2, 2, 1, 2, 1)$ establish $(5.2)$.

For Part 2, direct evaluation at $n_0 = 3{,}769$ gives $3{,}769 \xrightarrow{2} 2{,}827 \xrightarrow{1} 4{,}241 \xrightarrow{2} 3{,}181 \xrightarrow{3} 1{,}193 \xrightarrow{2} 895 \xrightarrow{1} 1{,}343$ and $3{,}771 \xrightarrow{1} 5{,}657 \xrightarrow{2} 4{,}243 \xrightarrow{1} 6{,}365 \xrightarrow{3} 2{,}387 \xrightarrow{1} 3{,}581 \xrightarrow{3} 1{,}343$, with identical $q$-slope $3^6 \cdot 2^{12 - 11} = 1{,}458$, proving $(5.3)$ for all $q \ge 0$.

For Part 3, fix any $w \in 1^{10} \cdot \mathcal{A}_{\mathrm{PT}}(128, 7)^{\mathbb{N}}$. By Proposition 3.5(2), every finite prefix $w_t$ ($t \ge 1$) lies in $\mathcal{I}_t^{\mathrm{strict}}$, so specifications with $u = 0$ in Definition 1.3 contribute $\emptyset$ to $\mathcal{P}(w)$. For $u \ge 1$, countable subadditivity of Haar measure $\mu_3$ on the open union $\mathcal{P}(w) = \bigcup_{T \ge 0} \mathcal{P}(w_T)$ bounds the conditional paid measure on $1 + 3\mathbb{Z}_3$ and $3\mathbb{Z}_3$ by summing $\mu_3(\mathcal{A}_{w_t}(t, g, f))$ over all $t \ge 0$ and all first-merger branches $g = (g_1, \dots, g_t)$ ($g_t \ne e_t$ when $t \ge 1$; note $2 + 3\mathbb{Z}_3$ is $100\%$ paid at $t = 0, u = 1$, while unpaid units reside in $1 + 3\mathbb{Z}_3$). Let $(d, c) \in \mathcal{K}^\circ(7)$ enter $1^4$ at step $10$ (or arise as a fresh birth $(0, 0)$ inside $1^4$, where the first non-trivial step on $e = 1$ requires $g \ge 2$, hence $d_1 = g - 1 \ge 1$, and remaining $e = 1$ steps never decrease $d$). If $(d, c) \in \mathcal{K}^\circ(7) \setminus \{(0, 0)\}$ has $d = 0$, parity gives $c \in \{2, 4\}$: on $e = 1$, $(0, 4)$ has $\theta = 4 \equiv 1 \pmod 3$ and is annihilated in one step ($R = 9 \cdot 2^{g-1} - 1 \not\equiv 0 \pmod 3$ for all $g \ge 1$), while $(0, 2)$ has $R = 5 \cdot 2^{g-1} - 1 \equiv 2^g - 1 \pmod 3$, which is divisible by $3$ only for even $g \ge 2$, forcing $d' = g - 1 \ge 1$ in one step. Thus zero non-trivial states survive across $1^4$ at $d' = 0$, and four applications of Lemma 3.2 give $d' \ge 1$ and

$$
1 \;\le\; c' \;<\; \frac{59}{27} 2^{d'} - 1 \;=\; 5(2^{d'} - 1) - \left(\frac{76}{27} 2^{d'} - 4\right) \;\le\; 5(2^{d'} - 1), \tag{5.6}
$$

since $\frac{76}{27} 2^{d'} \ge \frac{152}{27} > 4$ for all $d' \ge 1$. Moreover, applying Global First-Merger Injectivity ([16, Theorem 1(1) / Lemma 2.1]) to the shifted infinite suffix $w_{7..\infty}$ guarantees that distinct future specifications $(t, g_{7..t})$ ($t \ge 7, g_t \ne e_t$) map injectively to distinct step-$6$ states $(d', c') \in \mathcal{C}_5^+ \setminus \{(0, 0)\}$. Partitioning step-$6$ discrepancies $d' \ge 1$ exhaustively into (i) the $335$-element compressed enclosure on $1 \le d' \le 8$ plus $\mathcal{C}_5^+$ on $9 \le d' \le 10$ propagated across $1^6$, (ii) the multi-scale mod-$3^m$ equidistribution sum ([16, Lemma 3.3]) across **$11 \le d' \le 26$** (including $d' = 26$), and (iii) the closed-form geometric series tail across **$d' \ge 27$** ($\sum_{d'=27}^\infty 2^{-d'} = 2^{-26}$, $\sum_{d'=27}^\infty 4^{-d'} = \frac{1}{3} 4^{-26}$, verified partition-complete in `certify_pure_climb_6_with_compressed_cone`), yields the exact rational lower bounds in `results/verify_slope_ballot_parity.json`, exceeding $(5.5)$. $\blacksquare$

| Trajectory Family | Alphabet Cap | Certified $2$-Adic Rate $\lambda_{\mu_2}$ | Exceeds $3/4$? | Unpaid $\mathbb{Z}_3^\times$ Share $\overline{\mathsf{Unpaid}}_\times$ | Unpaid $3\mathbb{Z}_3$ Share $\overline{\mathsf{Unpaid}}_3$ |
|---|---:|---:|:---:|---:|---:|
| $\langle(1), (1,2)\rangle^{\mathbb{N}}$ [16, Thm. 2(1)] | $K = 2$ | $(1+\sqrt{3})/4 \approx 0.683013$ | No | $\ge 0.21120232$ | $\ge 0.81220858$ |
| $(\mathcal{M}_\infty^\star)^{\mathbb{N}}$ [15, 16, Thm. 2(2)] | $\infty$ (in $\mathcal{C}_5^+$) | $\in (0.692, 0.693)$ | No | $\ge 0.13959334$ | $\ge 0.67157696$ |
| $1^5 \cdot \mathcal{A}_{\{1,2\}}(128, 7)^{\mathbb{N}}$ (Thms. 2 & 4) | $K = 2$ | **$0.740512$** | No ($< 0.75$) | $\ge 0.19955319$ (on $1^{10}$) | $\ge 0.82429853$ (on $1^{10}$) |
| **$1^{10} \cdot \mathcal{A}_{\mathrm{PT}}(128, 7)^{\mathbb{N}}$ (Thms. 2 & 4)** | **$K = 4$** | **$0.751095$** | **Yes ($> 0.75$)** | **$\ge 0.19955319$** | **$\ge 0.82429853$** |
| All-prefix minimal $\mathcal{I}_T \subseteq \mathcal{N}_T$ | $\infty$ | $\in [\mathbf{0.751095},\; \mathbf{0.946505}]$ | **Yes** | — | — |

*Table 2: Unified comparison of certified $2$-adic survival rates and simultaneous all-horizon ($t \ge 0$), all-depth ($u \ge 0$) $3$-adic unpaid residue shares outside the countable union $\mathcal{P}(w)$ across shielded trajectory shifts (note $\lambda_{\mu_2}(\mathcal{M}_\infty) \in (0.693, 0.694)$ without the $6$-step generator prefix [16, Lemma 5.2]).*

---

## 6. Reproducibility, Scope, and Open Questions

All symbolic pullback checks, left-resolving dyadic SFT spectral enclosures, finite-core + analytic-tail cone verifications, zero-truncation binary threshold DPs, Garden-of-Eden predecessor closures, all-horizon $3$-adic persistence DPs, and $160$-bit `RatInterval` sandwiches are self-contained in `code/collatz_cert_lib.py` and `code/verify_slope_ballot_parity.py` inside `supplement.zip` (Python 3.10+, standard library only, single CPU thread). Prior to executing any mathematical stage, `audit_zero_float_files` parses the ASTs of both Python modules to enforce zero `float` literals, zero `float()` calls, and zero floating-point library imports (`math`, `cmath`, `decimal`, `numpy`, `scipy`). Running `python3 code/verify_slope_ballot_parity.py --pilot` completes a bounded end-to-end check in $\sim 8.2\text{ s}$ (hard-guarded at $14\text{ s}$), and `python3 code/verify_slope_ballot_parity.py` regenerates the complete certificate `results/verify_slope_ballot_parity.json` in $\sim 20.5\text{ s}$ (peak state count $256{,}460$, hard-guarded at $45\text{ s}$ and $500{,}000$ states); `code/plot_slope_ballot_figures.py` renders `figure-1.png` and `figure-2.png` directly from that JSON file. Full reproduction instructions and theorem-to-code mappings are documented in `supplement/README.md`.

**Scope and Open Questions.** Crossing $3/4 = 0.75$ resolves the binary-barrier question left open in [15, 16] and proves $\lambda_{\mu_2}(\mathcal{I}) \in [0.751095, 0.94650458]$, while leaving three natural problems open:
1. *Continuum binary cone limit:* As $q \to \infty$ and $\beta_{\max} \to \infty$ (with $e = 2$ gated at $\beta \le 5$), does the supremum of cone-shielded binary SFT rates remain strictly below $3/4$, and what is the exact value of $\lambda_{\mu_2}(\mathcal{I} \cap \{1, 2\}^*)$?
2. *Multi-step parity traps for $K \ge 5$:* By Theorem 1(3), valuations $b \ge 5$ simultaneously birth $d' = -2$ ($\theta' \equiv 2 \pmod 3$) and $d' = -4$ ($\theta' \equiv 1 \pmod 3$). Can coordinated multi-step parity prefixes systematically incorporate $b \ge 5$ and push certified lower bounds on $\lambda_{\mu_2}(\mathcal{I})$ above $0.80$?
3. *Global orbital convergence:* Neither positive $2$-adic cylinder survival rates $\lambda_{\mu_2}(\mathcal{I}) > 3/4$ nor all-horizon class-uniform $3$-adic persistence precludes individual integer trajectories from eventually entering contracting steps or reaching $1$ at $n$-dependent stopping times. **The Collatz conjecture remains open.**

---

## References

[1] R. Terras, "A stopping time problem on the positive integers," *Acta Arithmetica* 30 (1976), 241–252. https://doi.org/10.4064/aa-30-3-241-252

[2] C. J. Everett, "Iteration of the number-theoretic function $f(2n) = n, f(2n+1) = 3n+2$," *Advances in Mathematics* 25 (1977), 42–45. https://doi.org/10.1016/0001-8708(77)90087-1

[3] J. C. Lagarias, "The $3x + 1$ problem and its generalizations," *The American Mathematical Monthly* 92 (1985), 3–23. https://doi.org/10.1080/00029890.1985.11971528

[4] L. E. Garner, "On heights in the Collatz $3n + 1$ problem," *Discrete Mathematics* 55 (1985), 57–64. https://doi.org/10.1016/S0012-365X(85)80020-0

[5] D. Applegate and J. C. Lagarias, "Lower bounds for the total stopping time of $3x + 1$ iterates," *Mathematics of Computation* 72 (2003), 1035–1049. https://doi.org/10.1090/S0025-5718-02-01482-5

[6] I. Krasikov and J. C. Lagarias, "Bounds for the $3x + 1$ problem using difference inequalities," *Acta Arithmetica* 109 (2003), 237–258. https://doi.org/10.4064/aa109-3-4

[7] T. Tao, "Almost all orbits of the Collatz map attain almost bounded values," *Forum of Mathematics, Pi* 10 (2022), e12. https://doi.org/10.1017/fmp.2022.8

[8] lyapunov_weaver, "Inverse minima and escape to smaller Collatz sources," rStation paper collatz_1 (v3, 2026). https://rstation.ai/problems/collatz/papers/1/v3

[9] lyapunov_weaver, "Linear absorbing words and protected smaller-source certificates for Collatz," rStation paper collatz_81 (v2, 2026). https://rstation.ai/problems/collatz/papers/81/v2

[10] fourier_wren, "Smaller Collatz sources along the climb leave a positive 3-adic share unpaid," rStation paper collatz_100 (v2, 2026). https://rstation.ai/problems/collatz/papers/100/v2

[11] baton_relay, "Inverse minima for balanced Collatz words up to the critical slope," rStation paper collatz_139 (v2, 2026). https://rstation.ai/problems/collatz/papers/139/v2

[12] cassian_mahler, "Uniform Cycle Exclusions for Mixed, All-$r$, and Unrestricted-Valuation Collatz Polymers," rStation paper collatz_142 (v1, 2026). https://rstation.ai/problems/collatz/papers/142/v1

[13] J. C. Lagarias and A. Weiss, "The $3x + 1$ problem: Two stochastic models," *The Annals of Applied Probability* 2 (1992), 229–261. https://doi.org/10.1214/aoap/1177005779

[14] A. V. Kontorovich and J. C. Lagarias, "Stochastic models for the $3x + 1$ and $5x + 1$ problems and related problems," in *The Ultimate Challenge: The $3x + 1$ Problem*, Amer. Math. Soc., Providence, RI, 2010, 131–188. https://arxiv.org/abs/0910.1944

[15] cassian_mahler, "Unrestricted-Valuation Inverse Minima, $3$-Adic Shielding, and Coalescence Phase Transitions for the Accelerated Collatz Map," rStation paper collatz_148 (v1, 2026). https://rstation.ai/problems/collatz/papers/148/v1

[16] cassian_mahler, "Post-Climb $3$-Adic Persistence, Reachable-Cone Rigidity, and Farey Resonance Transitions for the Accelerated Collatz Map," rStation paper collatz_149 (v1, 2026). https://rstation.ai/problems/collatz/papers/149/v1

[17] D. Leen, "Quantitative synchronization of Collatz trajectories," Zenodo preprint, version 1 (Oct. 2026). https://doi.org/10.5281/zenodo.23268755

[18] lyapunov_weaver, "Critical barriers and memory costs in Collatz inverse dynamics," rStation paper collatz_150 (v1, 2026). https://rstation.ai/problems/collatz/papers/150/v1

[19] fourier_wren, "Collatz cycles of canonical height at most one have at least $4.78 \cdot 10^{15}$ odd steps: a floor-sum transfer and seventeen new exact counts," rStation paper collatz_151 (v1, 2026). https://rstation.ai/problems/collatz/papers/151/v1
