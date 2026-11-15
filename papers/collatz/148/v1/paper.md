# Unrestricted-Valuation Inverse Minima, $3$-Adic Shielding, and Coalescence Phase Transitions for the Accelerated Collatz Map

## 1. Introduction

### 1.1 Background, Related Work, and Research Question

Let $\mathbb{N}_{\mathrm{odd}} = \{1, 3, 5, \dots\}$ denote the positive odd integers. The accelerated Collatz (Syracuse) map $U : \mathbb{N}_{\mathrm{odd}} \to \mathbb{N}_{\mathrm{odd}}$ is defined by

$$
U(x) := \frac{3x + 1}{2^{v_2(3x + 1)}},
$$

where $v_2(m) \geq 1$ is the $2$-adic valuation of an even integer $m$. Iterating $U$ for $s \geq 1$ steps from $n \in \mathbb{N}_{\mathrm{odd}}$ produces a valuation word $w_s(n) = (e_1, \dots, e_s) \in \mathbb{Z}_{\ge 1}^s$, where $x_0 = n$, $e_i = v_2(3 x_{i-1} + 1)$, and $x_i = U(x_{i-1})$. Writing $\|w\| := \sum_{i=1}^s e_i$ for the total $2$-division weight of $w = (e_1, \dots, e_s)$, standard induction gives the affine forward relation

$$
U^s(n) = \frac{3^s n + C(w)}{2^{\|w\|}}, \qquad C(w) := \sum_{i=1}^s 3^{s-i} 2^{\sum_{j=1}^{i-1} e_j}.
$$

Because $\gcd(3^s, 2^{\|w\|}) = 1$, each finite word $w \in \mathbb{Z}_{\ge 1}^s$ is realized as $w_s(n)$ on a unique arithmetic progression (cylinder) of positive odd integers [1, 2, 3]:

$$
\operatorname{Cyl}(w) := \{n \in \mathbb{N}_{\mathrm{odd}} : w_s(n) = w\} = \{n_0(w) + 2^{\|w\| + 1} k : k \in \mathbb{Z}_{\ge 0}\},
$$

with image progression $U^s(n_0(w) + 2^{\|w\| + 1} k) = y_0(w) + 2 \cdot 3^s k$ (we reserve $C(w)$ exclusively for the affine numerator constant in $U^s(n)$ and $\operatorname{Cyl}(w)$ for the integer cylinder).

If the set $\Omega_{\mathrm{fail}} := \{n \in \mathbb{N}_{\mathrm{odd}} : \forall k \geq 0,\; U^k(n) \neq 1\}$ of odd integers failing to reach $1$ is nonempty, its least element $n_* := \min \Omega_{\mathrm{fail}}$ cannot coalesce with any smaller odd integer: there cannot exist $b \in \mathbb{N}_{\mathrm{odd}}$ with $b < n_*$ and integers $s, r \geq 0$ such that $U^s(n_*) = U^r(b)$ (for otherwise $b \notin \Omega_{\mathrm{fail}}$ reaches $1$, whence $U^r(b) = U^s(n_*)$ reaches $1$). Orbit coalescence before stopping-time descent goes back to Garner [4], Wirsching's predecessor-set theory [5], and Applegate–Lagarias [6] (surveyed in Lagarias's annotated bibliography [7]), and provides an algebraic obstruction to membership in $\{n_*\}$ complementary to forward stopping-time and logarithmic-density bounds [1, 2, 6, 8].

Recent rStation papers developed quantitative inverse-minimality results against unrestricted rival words $w' \in \mathbb{Z}_{\ge 1}^*$. Weaver (`collatz_1` v3 [9]) introduced affine discrepancy coordinates and a constant-five positive cone preserving matched-depth minimality across the Fibonacci subshift $\langle (1), (1, 2) \rangle \subset \{1, 2\}^*$ (and on $(1, 2, 1, 2, 1, 2, 2)^\infty$), while `baton_relay` (`collatz_139` v2 [10], building on [6, 9] and `collatz_140` v1 [11]) characterized division-minimality across balanced binary reference words up to the critical slope $\log_2 3 - 1.26 \times 10^{-11}$, already allowing arbitrary rival exponents $w' \in \mathbb{Z}_{\ge 1}^r$ in the inverse comparison. In a complementary direction, Weaver (`collatz_108` v1 [15]) determined eventual exact minima over unrestricted rival exponents for integer targets $x_R = (2 \cdot 3^R z - p)/q$ approaching a fixed negative rational cycle $-p/q$, proving that minimizing paths follow the negative cycle until a bounded terminal dictionary $\mathcal{W}_d$ remains at sufficiently large depth $R$. Crucially, however, [9, 10, 11] restrict forward **reference** words $w$ to $\{1, 2\}^*$, where factor-closure converts division-minimality directly into matched-depth source minimality (`collatz_139` v2, Theorem 1), whereas [15] treats eventual minima along a fixed negative cycle basin rather than uniform cylinder rigidity across concatenations of arbitrary forward words; `collatz_139` v2 (Section 10) identifies reference words over the **unrestricted alphabet $\mathbb{Z}_{\ge 1}^*$** as an open problem. As soon as a reference word $w$ contains a high halving valuation $d \geq 3$ (occurring on odd integers with positive $2$-adic density $2^{-d}$), the single inverse step $I_d(y) = (2^d y - 1)/3$ launches $\lfloor(d - 1)/2\rfloor \geq 1$ simultaneous sub-budget rival branches $I_{d - 2j}(y)$ ($1 \le j \le \lfloor(d - 1)/2\rfloor$) on the exact same $3$-adic residue class, plunging valuation discrepancy to $\delta = -2j < 0$.

### 1.2 Summary of Contributions

Rather than claiming a complete syntactic decision procedure for all minimal words in $\mathbb{Z}_{\ge 1}^*$, this paper establishes four structural results clarifying how inverse-tree minimality behaves once reference words $w \in \mathbb{Z}_{\ge 1}^*$ are allowed to contain arbitrary valuations $d \geq 3$ across matched and shallower horizons ($1 \le r \le s$). Unlike bounded terminal dictionaries near fixed negative cycles [15], shielding an unrestricted drop $d \ge 3$ on $100\%$ of its cylinder requires $\Theta(d)$ binary steps, and concatenating shielded drops across all finite lengths requires simultaneous control of unbounded incoming cone discrepancies and shallower horizons. We first separate the three relevant minimality notions.

**Definition 1.1 (Predecessor Minimality for Unrestricted Reference Words).** Fix $w \in \mathbb{Z}_{\ge 1}^s$ and $n \in \operatorname{Cyl}(w)$ with $y = U^s(n)$.
1. We call $n$ **division-minimal** if every odd integer $b \in U^{-s}(y) \setminus \{n\}$ satisfies $\|w_s(b)\| \ge \|w\|$, and **division-rigid** if $\|w_s(b)\| > \|w\|$ strictly for every $b \in U^{-s}(y) \setminus \{n\}$.
2. We call $n$ **matched-depth minimal** if $b > n$ for every $b \in U^{-s}(y) \setminus \{n\}$.
3. We call $n$ **all-($r \le s$) minimal** if $b > n$ for every depth $1 \le r \le s$ and every $b \in U^{-r}(y)$ (excluding $b = n$ when $r = s$).

Our main results are as follows:

- **Theorem 1 ($0$–$1$ Cylinder Law, Factor-Closure Collapse, and Two Structural Separations; Section 2).**
  1. *(All-$r \le s$ $0$–$1$ Cylinder Law and Complete Weight-Tail Cutoffs)* For every reference word $w \in \mathbb{Z}_{\ge 1}^s$ and rival word $w' \in \mathbb{Z}_{\ge 1}^r$ of depth $1 \le r \le s$, integrality and oddness of $I_{w'}(U^s(n(k)))$ are **independent of $k \ge 0$** across $\operatorname{Cyl}(w) = \{n_0(w) + 2^{\|w\|+1} k\}$, while explicit weight-tail bounds (Lemma 2.1) reduce unrestricted source minimality over $\mathbb{Z}_{\ge 1}^r$ to a finite, provably complete search. Division-minimality, division-rigidity, and asymptotic minimality ($b(k) > n(k)$ for all large $k$) hold on either $0\%$ or $100\%$ of $\operatorname{Cyl}(w)$.
  2. *(Factor-Closure Collapse)* Every $1$-letter cylinder $\operatorname{Cyl}((d))$ with $d \ge 3$ fails division- and matched-depth minimality on $100\%$ of $\operatorname{Cyl}((d))$ via $b(k) = (n(k) - 1)/4 < n(k)$ realizing $(d - 2)$. Consequently, every factor-closed (or suffix-closed) language $\mathcal{L} \subset \mathbb{Z}_{\ge 1}^*$ of division- or matched-depth-minimal reference words collapses to $\mathcal{L} \subseteq \{1, 2\}^*$.
  3. *(Separation I: Division-Minimality $\not\implies$ Matched-Depth Minimality)* Over $\mathbb{Z}_{\ge 1}^*$, division-minimality does **not** imply matched-depth minimality—not even on globally expanding cylinders ($3^s > 2^{\|w\|}$). The length-$6$ word $w = (2, 1, 1, 1, 1, 7)$ ($n_0 = 16{,}169$, $y_0 = 1{,}439$) is division-minimal across $100\%$ of $\operatorname{Cyl}(w)$ yet admits the equal-weight rival $w' = (2, 2, 1, 4, 3, 1)$ giving $b(k) = n(k) - 8 < n(k)$ for all $k \ge 0$. Moreover, the infinite family $w_M := (1^6, 2, 2, 5, 1^M)$ ($M \ge 0$), globally expanding for every $M \ge 2$, is division-minimal for **every** $M \ge 0$ while satisfying $b(k) = n(k) - 4 < n(k)$ across $100\%$ of $\operatorname{Cyl}(w_M)$.
  4. *(Separation II: Matched-Depth Cone Rigidity $\not\implies$ All-($r \le s$) Minimality)* The strictly prefix-expanding block $B_3 := (1, 1, 1, 2, 1, 3)$ preserves the positive discrepancy cone $\mathcal{C}_5^+$, so every word in $(B_3)^+$ satisfies $b \ge 2n + 1$ for all nontrivial matched-depth rivals ($r = 6k$); yet **every** iterate $(B_3)^k$ ($k \ge 1$) fails all-($r \le s$) minimality across $100\%$ of $\operatorname{Cyl}((B_3)^k)$ at shallower depth $r = 6k - 5$ via $w'_k = (1) \cdot B_3^{k-1}$ ($b(m) = 835 + 972 m < 879 + 1024 m = n(m)$). Extending Stage 2 by one step to $B_3^+ := (1, 1, 1, 1, 2, 1, 3)$ eliminates all shallower rivals.

- **Theorem 2 ($\Theta(d)$ Minimum Shield Bounds and Odd-Integer Contraction of Jacobsthal $3$-Adic Limits; Section 3).** For $d \ge 3$ and shield alphabet $\Sigma \subseteq \mathbb{Z}_{\ge 1}$, let $L_{\min}^{\mathrm{div}}(d; \Sigma)$ and $L_{\min}^{\mathrm{depth}}(d; \Sigma)$ be the minimum lengths $|u|$ of a prefix shield $u \in \Sigma^*$ rendering $u \cdot (d)$ division-minimal or matched-depth minimal on $100\%$ of $\operatorname{Cyl}(u \cdot (d))$.
  1. *(Alphabet-Free Lower Bounds and Parity Invariance)* For every $d \ge 5$ with $J := \lfloor(d - 1)/2\rfloor$, even over the unrestricted shield alphabet $\Sigma = \mathbb{Z}_{\ge 1}$,

     $$
     L_{\min}^{\mathrm{div}}(d; \mathbb{Z}_{\ge 1}) \ge \left\lceil \frac{2J}{3} \right\rceil, \qquad L_{\min}^{\mathrm{depth}}(d; \mathbb{Z}_{\ge 1}) \ge \left\lfloor \frac{2J}{3} \right\rfloor + 1,
     $$

     and $L_{\min}^{\mathrm{div}}(2J + 1; \Sigma) = L_{\min}^{\mathrm{div}}(2J + 2; \Sigma)$ is monotonically non-decreasing in $J$.
  2. *(All-$d$ Linear $\{1, 2\}$-Shielding via Odd-Integer Contraction)* On $W_{m, d} := (2, 1^m, d)$, every trunk split $1 \le j \le J$ converges $3$-adically as $m \to \infty$ to $z_0^{(j)} = -B_j / 2^{2j-1}$ with odd integer $B_j = (2^{2j-1} + 1)/3$ (instantaneously divisible by $3$ whenever $j \equiv 2 \pmod 3$). For every $j \ge 2$, $z = -1$ is unreachable and every surviving branch at step $s \ge 2j$ is an odd negative integer $z_s \le -5$ whose offset $D_s := |z_s| - 1 \ge 4$ obeys $D_{s+1} \le \frac{5}{6} \cdot 2^{g_{s+2}-1} D_s$. Consequently, $W_{m, d}$ is division-rigid and matched-depth minimal on $100\%$ of $\operatorname{Cyl}(W_{m, d})$ for all $d \ge 3$ and all

     $$
     m \ge m_*(d) := (d - 1) + \left\lceil \frac{1901}{500}(2d - 3) \right\rceil = \Theta(d),
     $$

     establishing $L_{\min}^{\mathrm{div}}(d; \Sigma), L_{\min}^{\mathrm{depth}}(d; \Sigma) = \Theta(d)$ for every $\{1, 2\} \subseteq \Sigma \subseteq \mathbb{Z}_{\ge 1}$. Sound branch-and-bound pruning (Lemma 3.3, cross-checked against unpruned enumeration through $d = 11$) certifies exact $(L_{\min}^{\mathrm{div}}, L_{\min}^{\mathrm{depth}})$ over $\{1, 2\}^*$ across $d \in \{3, \dots, 13, 15\}$, and boundary phase-cap analysis explains the non-monotonicity of $W_{m, 9}$ at $m = 8 \to 9 \to 10$.

- **Theorem 3 (Explicit All-$d$ Cone-Preserving, All-($r \le s$)-Minimal Monoid $\mathcal{M}_\infty$; Section 4).** Define the positive odd-offset discrepancy cone

  $$
  \mathcal{C}_5^+ := \{(0, 0)\} \cup \left\{(\delta, c) \in \mathbb{Z}^2 : \delta \ge 1,\; 1 \le c \le 5(2^\delta - 1),\; c \equiv 1 \pmod 2\right\}.
  $$

  For every $d \ge 3$, setting explicitly

  $$
  m_d^{\mathrm{exp}} := d + \left\lceil \frac{1901}{500}(d - 1) \right\rceil, \qquad s_d^{\mathrm{exp}} := d + \left\lceil \frac{1901}{500}(d + 1) \right\rceil + \left\lceil \frac{171}{100}(d + 3) \right\rceil + \left\lceil \frac{171}{100}(d + 2) \right\rceil,
  $$

  the two-stage block $B_d^{\mathrm{exp}} := (1^{s_d^{\mathrm{exp}}}, 2, 1^{m_d^{\mathrm{exp}}}, d)$ has every nonempty prefix strictly expanding ($3^i > 2^{S_i}$), maps $\mathcal{C}_5^+ \setminus \{(0, 0)\}$ strictly into $\mathcal{C}_5^+ \cap \{\delta \ge 1\}$, and satisfies **cone-entry shallower rigidity** (both $2^{G' + \delta_0} 3^{|B_d^{\mathrm{exp}}| - r} > 2^{\|B_d^{\mathrm{exp}}\|}$ and $b_0 > n_0(B_d^{\mathrm{exp}})$ for every $(\delta_0, c_0) \in \mathcal{C}_5^+$ and every $1 \le r < |B_d^{\mathrm{exp}}|$). Combining the sharp short generators $(1)$, $(1, 2)$, $B_3^+ = (1^4, 2, 1, 3)$, $B_4 = (1^5, 2, 1, 4)$, $B_5 = (1^6, 2, 1^2, 5)$, $B_6 = (1^6, 2, 1^3, 6)$, $B_7 = (1^8, 2, 1^5, 7)$, $B_8 = (1^9, 2, 1^5, 8)$, $B_9 = (1^{10}, 2, 1^{12}, 9)$, and $B_{10} = (1^{11}, 2, 1^{12}, 10)$—universally certified across all incoming cone discrepancies and parity-exact outgoing exponent tails via Lemma 4.7—with $\{B_d^{\mathrm{exp}}\}_{d \ge 11}$ generates an instantaneous suffix-code free monoid $\mathcal{M}_\infty \subset \mathbb{Z}_{\ge 1}^*$ such that:
  1. Every word $w \in \mathcal{M}_\infty$ is **division-rigid and all-($r \le s$) minimal** across $100\%$ of $\operatorname{Cyl}(w)$ (with $b \ge 2n + 1$ at matched depth $r = s$ and $b > n$ at all shallower depths $1 \le r < s$; Lemma 4.6);
  2. $\mathcal{M}_\infty$ contains every valuation $d \ge 1$, including super-$3/2$-slope blocks such as $B_6 = (1^6, 2, 1^3, 6)$ (length $11$, weight $17$, slope $17/11 > 3/2$, $3^{11} = 177{,}147 > 131{,}072 = 2^{17}$); and
  3. $\mathcal{M}_\infty$ strictly enlarges Weaver's Fibonacci language $\langle (1), (1, 2) \rangle$, raising the exponential word-growth base above $\varphi = \frac{1 + \sqrt{5}}{2} \approx 1.6180$: $\lambda(\mathcal{M}_\infty) > \frac{33}{20} = 1.65 > \varphi$ ($h_{\mathrm{top}}(\mathcal{M}_\infty) > \frac{72}{100}$ bits/step).

- **Theorem 4 (Periodic-Corridor Coalescence Phase Transitions and Prefix-Expanding Exclusions; Section 5).**
  1. Extending the half-source $(n - 5)/2$ mechanism used on $(1, 2)^L(3, 1, 3)$ in `collatz_1` v3 ([9], Proposition 9) to a uniform single-letter terminal-$d$ classification across $W = (1, 2)$ ($y_{\mathrm{fp}} = -5$), $W^M \cdot (d)$ is division-rigid and matched-depth minimal across $100\%$ of $\operatorname{Cyl}(W^M \cdot (d))$ for every $1 \le d \le 4$ and $M \ge 1$, whereas for **every $d \ge 5$ and $M \ge 1$**, $100\%$ of $\operatorname{Cyl}(W^M \cdot (d))$ coalesces via $b = (n - 5)/2 < n$ realizing $W^{M-1} \cdot (1, 5, d - 4)$. Taking $d = 5, M = 21$ (length $43$, weight $68$) yields a single-drop cylinder on which **every nonempty prefix strictly expands** ($3^i > 2^{S_i}$), so forward stopping-time criteria fail completely, yet $100\%$ of the cylinder is excluded from $\{n_*\}$.
  2. Along $W_7 = (1, 2, 1, 2, 1, 2, 2)$ ($3^7 - 2^{11} = 139$, $y_{\mathrm{fp}} = -3767/139 \approx -27.10$), unrestricted cylinder certification across $1 \le M \le 5$ (via Lemma 2.1, with `proved_G_max <= S` on all $40$ cylinders) proves that $W_7^M \cdot (d)$ ($M \in \{3, 4, 5\}$) is division-minimal for $d \in \{3, 4, 5, 7, 9, 10\}$—achieving full unrestricted matched-depth minimality at $(d, M) = (5, 4)$ alongside negative equal-weight ties $c_{\min} \in \{-32, -18\}$ explained by Lemma 5.1—and undergoes sub-budget coalescence at $d \in \{11, 12\}$ via $j = 5$.

### 1.3 Limitations and Horizon Boundary ($r \le s$ vs. $r > s$)

All verification scripts (`code/collatz_cert_lib.py` and `code/verify_unrestricted_minima.py`) use exact integer/rational arithmetic and outward-rounded dyadic intervals (`RatInterval`), AST-audited at runtime to contain zero floating-point operations.

Two scope limits are fundamental. First, while Theorems 2 and 3 establish $\Theta(d)$ shielding and an all-$d$ rigid submonoid $\mathcal{M}_\infty$, a complete characterization of *all* division-minimal words in $\mathbb{Z}_{\ge 1}^*$ near critical slope $\log_2 3$ remains open. Second, $0$–$1$ cylinder invariance holds strictly for $1 \le r \le s$ ($3^r \mid 3^s$). At **deeper horizons $r = s + m$ ($m \ge 1$)**, $I_{w'}(y_0 + 2 \cdot 3^s k) = I_{w'}(y_0) + \frac{2^{\|w'\|+1}}{3^m} k$ sieves residue classes modulo $3^m$ of density $3^{-m}$. Moreover, even $3 \mid n$ (which blocks extensions $w' = u \cdot w$ factoring through $n$) does not block deeper **cone-bypass** rivals on $\mathcal{M}_\infty$: in Section 4.4 we certify $n = 1731 = 3 \times 577 \in \operatorname{Cyl}((1))$ coalescing with $b = 1215 < 1731$ via $w' = (1, 1, 1, 1, 1, 2, 3)$ ($U^1(1731) = U^7(1215) = 2597$). Deeper-horizon covering and the global Collatz conjecture remain open.

---

## 2. Inverse Predecessors, Complete Weight-Tail Bounds, and Proof of Theorem 1

### 2.1 Inverse Predecessor Operators, Complete Weight-Tail Bounds, and Discrepancy Coordinates

For each integer $g \ge 1$, define the affine inverse branch $I_g : \mathbb{Q} \to \mathbb{Q}$ by $I_g(x) := (2^g x - 1)/3$. An odd integer $b \ge 1$ satisfies $U(b) = x$ with $v_2(3b + 1) = g$ if and only if $b = I_g(x) \in \mathbb{Z}$ (which automatically forces $b$ odd since $3b = 2^g x - 1$ is odd). Note that $2^g x \equiv 1 \pmod 3$ has **no** solution $g \ge 1$ when $x \equiv 0 \pmod 3$ (an absorbing $3$-adic extinction trap), even solutions $g \in \{2, 4, \dots\}$ when $x \equiv 1 \pmod 3$, and odd solutions $g \in \{1, 3, \dots\}$ when $x \equiv 2 \pmod 3$.

For $w' = (e'_1, \dots, e'_r) \in \mathbb{Z}_{\ge 1}^r$, forward iteration $U^r(b) = y$ with $w_r(b) = w'$ is equivalent to the right-to-left pullback

$$
b = I_{w'}(y) := (I_{e'_1} \circ I_{e'_2} \circ \cdots \circ I_{e'_r})(y) = \frac{2^{\|w'\|} y - C(w')}{3^r},
$$

with step-by-step integrality $y'_t := (I_{e'_{r-t+1}} \circ \cdots \circ I_{e'_r})(y) \in \mathbb{Z}$ ($1 \le t \le r$), which is already forced by the single endpoint congruence $2^{\|w'\|} y \equiv C(w') \pmod{3^r}$.

To certify unrestricted source minimality over the infinite rival alphabet $\mathbb{Z}_{\ge 1}^r$ without heuristic search truncations, we establish an explicit weight-tail bound excluding all sufficiently heavy rivals.

**Lemma 2.1 (Complete Weight-Tail Bounds for Matched and Shallower Predecessors).** Let $y_0 \in \mathbb{N}_{\mathrm{odd}}$, $r \ge 1$, and $w' = (e'_1, \dots, e'_r) \in \mathbb{Z}_{\ge 1}^r$ be any valid $r$-step predecessor word on $y_0$ with total weight $G' := \|w'\|$ and odd integer endpoint $b_0 := I_{w'}(y_0) \in \mathbb{N}_{\mathrm{odd}}$.
1. *(Universal positivity bound)* $3^r b_0 > 2^{G' - r} y_0$ (in fact, $b_0 \ge 2^{G' - 2r} y_0$).
2. *(Sharp affine bound)* Setting $A_r := (y_0 + 1) 2^{r - 1} - 3^{r - 1}$, we have

   $$
   3^r b_0 \ge 2^{G' - r + 1} A_r - 3^{r - 1}.
   $$

3. *(Monotone intermediate bound)* For every intermediate state $y'_{r_1} \in \mathbb{N}_{\mathrm{odd}}$ at step $1 \le r_1 < r$, $3^{r - r_1}(b_0 + 1) \ge 2^{r - r_1}(y'_{r_1} + 1)$.

Consequently, for any reference cylinder $\operatorname{Cyl}(w)$ of length $s \ge r$, weight $S = \|w\|$, and base $(n_0, y_0)$, defining $G_{\max}(n_0, y_0, r, s, S)$ as the largest integer $G' \ge r$ (or $r - 1$ if none) violating either $2^{G'} 3^{s-r} > 2^S$ or the sharper of $2^{G'-r} y_0 \ge 3^r n_0$ and (when $A_r > 0$) $2^{G'-r+1} A_r - 3^{r-1} > 3^r n_0$, **every** legal $w' \in \mathbb{Z}_{\ge 1}^r$ with $\|w'\| > G_{\max}$ satisfies both $2^{\|w'\|} 3^{s-r} > 2^S$ and $b(k) > n(k)$ for all $k \ge 0$.

**Proof.**
**(1)** Let $y'_0 = y_0$ and $y'_t = I_{g_t}(y'_{t-1}) \in \mathbb{N}_{\mathrm{odd}}$ ($g_t = e'_{r-t+1} \ge 1$) for $1 \le t \le r$, so $y'_r = b_0$. At each step $t$: if $g_t = 1$, then $2 y'_{t-1} \equiv 1 \pmod 3$ and $y'_{t-1} \in \mathbb{N}_{\mathrm{odd}}$ force $y'_{t-1} \ge 5$, giving $3 y'_t = 2 y'_{t-1} - 1 \ge \frac{9}{5} y'_{t-1} > \frac{3}{2} \cdot 2^{g_t - 1} y'_{t-1}$; if $g_t \ge 2$, then $y'_{t-1} \ge 1$ gives $3 y'_t = 2^{g_t} y'_{t-1} - 1 \ge \frac{3}{4} \cdot 2^{g_t} y'_{t-1} = \frac{3}{2} \cdot 2^{g_t - 1} y'_{t-1}$. Multiplying across $1 \le t \le r$ yields $3^r b_0 \ge (\frac{3}{2})^r 2^{G' - r} y_0 > 2^{G' - r} y_0$ and $b_0 \ge 2^{G' - 2r} y_0$.

**(2)** In $C(w') = \sum_{i=1}^r 3^{r-i} 2^{\sum_{j=1}^{i-1} e'_j}$, the $i = 1$ term equals $3^{r-1}$ identically, while for each $2 \le i \le r$, $e'_i, \dots, e'_r \ge 1$ implies $\sum_{j=1}^{i-1} e'_j = G' - \sum_{j=i}^r e'_j \le G' - (r - i + 1)$. Hence

$$
C(w') \le 3^{r - 1} + 2^{G' - r - 1} \sum_{i=2}^r 3^{r - i} 2^i = 3^{r - 1} + 2^{G' - r + 1}(3^{r - 1} - 2^{r - 1}).
$$

Subtracting from $3^r b_0 = 2^{G'} y_0 - C(w') = 2^{G' - r + 1} \cdot 2^{r-1} y_0 - C(w')$ yields $3^r b_0 \ge 2^{G' - r + 1}((y_0 + 1)2^{r-1} - 3^{r-1}) - 3^{r-1}$.

**(3)** For every $x \ge 0$ and $g \ge 1$, $I_g(x) + 1 = (2^g x + 2)/3 \ge (2x + 2)/3 = \frac{2}{3}(x + 1)$; iterating $r - r_1$ times from $y'_{r_1}$ gives $b_0 + 1 \ge (\frac{2}{3})^{r - r_1}(y'_{r_1} + 1)$. The cutoff claim follows immediately from (2.2) below, since $b(k) = b_0 + 2^{G'+1} 3^{s-r} k > n_0 + 2^{S+1} k = n(k)$ holds for all $k \ge 0$ whenever $b_0 > n_0$ and $2^{G'} 3^{s-r} > 2^S$. $\blacksquare$

For matched-depth comparison ($r = s$), write $\gamma_t := e_{s-t+1}$ and $g_t := e'_{s-t+1}$ ($1 \le t \le s$), with trunk points $y_t = I_{\gamma_t}(y_{t-1})$ ($y_s = n$) and rival points $y'_t = I_{g_t}(y'_{t-1})$ ($y'_0 = y_0$, $y'_s = b$). The **valuation discrepancy** $\delta_t$, **scaled offset** $\rho_t$, and **integer offset** $c_t$ [9] are

$$
\delta_t := \sum_{i=1}^t (g_i - \gamma_i), \qquad \rho_t := \frac{y'_t}{2^{\delta_t}} - y_t, \qquad c_t := y'_t - 2^{\delta_t} y_t = 2^{\delta_t} \rho_t,
$$

satisfying the exact one-step recurrences

$$
\delta_t = \delta_{t-1} + g_t - \gamma_t, \qquad \rho_t = \frac{2^{\gamma_t} \rho_{t-1} + 1 - 2^{-\delta_t}}{3}, \qquad c_t = \frac{2^{g_t} c_{t-1} + 2^{\delta_t} - 1}{3}. \tag{2.1}
$$

Whenever $\delta_t \ge 1$ and $y'_t, y_t \in \mathbb{N}_{\mathrm{odd}}$, $c_t = y'_t - 2^{\delta_t} y_t$ is an **odd integer** (odd minus even). At $t = s$, $\delta_s = \|w'\| - \|w\|$ and $b = 2^{\delta_s} n + c_s$.

### 2.2 Proof of Theorem 1

**Proof of Theorem 1.**

**(1) All-($r \le s$) $0$–$1$ Cylinder Law.** Let $w \in \mathbb{Z}_{\ge 1}^s$ have weight $S = \|w\|$, so $n(k) = n_0 + 2^{S+1} k \in \operatorname{Cyl}(w)$ maps to $y(k) = U^s(n(k)) = y_0 + 2 \cdot 3^s k$ for all $k \ge 0$. For any $w' \in \mathbb{Z}_{\ge 1}^r$ of depth $1 \le r \le s$, weight $G' = \|w'\|$, and $u := s - r \ge 0$,

$$
I_{w'}(y_0 + 2 \cdot 3^s k) = \frac{2^{G'}(y_0 + 2 \cdot 3^{r+u} k) - C(w')}{3^r} = I_{w'}(y_0) + 2^{G' + 1} 3^u k. \tag{2.2}
$$

Since $2^{G'+1} 3^u k$ is an **even integer** for every $k \in \mathbb{Z}_{\ge 0}$ and every integral pullback from $y_0 \ge 1$ satisfies $b_0 := I_{w'}(y_0) \ge 1$ (inductively $x \ge 1 \implies I_g(x) \ge 1/3$), $I_{w'}(y(k))$ is a valid odd predecessor in $U^{-r}(y(k))$ if and only if $b_0 \in \mathbb{Z}$. Thus the set of valid rival words $w' \in \mathbb{Z}_{\ge 1}^r$ is independent of $k \ge 0$. At $r = s$ ($u = 0$), $\|w_s(b(k))\| = G'$ is independent of $k$, making division-minimality and division-rigidity $0$–$1$ cylinder properties; across $1 \le r \le s$, comparing $b(k) = b_0 + 2^{G'+1} 3^u k$ with $n(k) = n_0 + 2^{S+1} k$ (using $2^{G'} 3^u = 2^S \iff u = 0, G' = S$, where $b(k) - n(k) = c_s$ is constant) makes asymptotic minimality a $0$–$1$ property of $w$, while Lemma 2.1 bounds the search domain finitely for exact all-$k$ minimality (`enumerate_matched_rivals_dp` and `find_shallower_rivals` in `Suite A`).

**(2) Factor-Closure Collapse.** Fix $d \ge 3$ and $n \in \operatorname{Cyl}((d))$, so $3n + 1 = 2^d y$ with $y = U(n)$ odd. Modulo $8$, $3n + 1 \equiv 0 \pmod 8 \implies n \equiv 5 \pmod 8$, so $b := (n - 1)/4 \ge 1$ is a positive odd integer strictly smaller than $n$ satisfying $3b + 1 = (3n + 1)/4 = 2^{d-2} y$, i.e., $U(b) = U(n)$ with $w_1(b) = (d - 2)$ and $\|w_1(b)\| = d - 2 < d$. Thus $100\%$ of $\operatorname{Cyl}((d))$ fails division- and matched-depth minimality, forcing any factor- or suffix-closed minimal language $\mathcal{L} \subset \mathbb{Z}_{\ge 1}^*$ to satisfy $\mathcal{L} \subseteq \{1, 2\}^*$.

**(3) Separation I (Division-Minimality vs. Matched-Depth Minimality).**
- *Length-$6$ witness:* For $w = (2, 1, 1, 1, 1, 7)$ ($s = 6$, $S = 13$), direct cylinder lifting (`Suite A`) gives $\operatorname{Cyl}(w) = \{16{,}169 + 16{,}384 k : k \ge 0\}$ and $y_0 = 1{,}439$. Complete DP up to the Lemma 2.1 cutoff certifies zero rivals with $\|w'\| \le 12$, so $100\%$ of $\operatorname{Cyl}(w)$ is division-minimal; yet the equal-weight rival $w' = (2, 2, 1, 4, 3, 1)$ ($\|w'\| = 13$) yields $b_0 = I_{w'}(1{,}439) = 16{,}161 = n_0 - 8$, so $b(k) = n(k) - 8 < n(k)$ for all $k \ge 0$.
- *Infinite globally expanding family:* Set $w_{\mathrm{base}} := (1, 1, 1, 1, 1, 1, 2, 2, 5)$ (length $9$, weight $15$, $n_0 = 33{,}919$, $y_0 = 20{,}375$) and $w_M := w_{\mathrm{base}} \cdot (1^M)$ for $M \ge 0$ (globally expanding for all $M \ge 2$, since $3^{11} = 177{,}147 > 131{,}072 = 2^{17}$).
  1. *Failure of matched-depth minimality:* On $w_{\mathrm{base}}$, the equal-weight rival $w'_{\mathrm{base}} = (1, 2, 1, 2, 3, 2, 2, 1, 1)$ ($\|w'_{\mathrm{base}}\| = 15$) satisfies $I_{w'_{\mathrm{base}}}(20{,}375) = 33{,}915 = n_0 - 4$. For any $M \ge 0$ and $n \in \operatorname{Cyl}(w_M) \subset \operatorname{Cyl}(w_{\mathrm{base}})$, $b := n - 4$ satisfies $U^9(b) = U^9(n)$, whence applying $U^M$ forward gives $U^{9+M}(b) = U^{9+M}(n)$ with $w_{9+M}(b) = w'_{\mathrm{base}} \cdot (1^M)$ across $100\%$ of $\operatorname{Cyl}(w_M)$.
  2. *Division-minimality for all $M \ge 0$:* Pull back $y = U^{9+M}(n)$ across $1^M$ first. Copying $1^M$ reaches $U^9(n)$ at $(0, 0)$, where `Suite A` certifies zero sub-budget exits on $w_{\mathrm{base}}$. Any rival first deviating from $\gamma = 1$ along $1^M$ must take an odd jump $g \ge 3$, entering $\delta = g - 1 \ge 2, c = (2^{g-1} - 1)/3 \in \mathcal{C}_5^+ \cap \{\delta \ge 2\}$, and each subsequent `1`-step preserves $\mathcal{C}_5^+ \cap \{\delta \ge 2\}$ because $\delta_{\mathrm{next}} = \delta + g' - 1 \ge 2$ and $3 c_{\mathrm{next}} \le 10 \cdot 2^{\delta_{\mathrm{next}}} - 5 \cdot 2^{g'} + 2^{\delta_{\mathrm{next}}} - 1 \le 11 \cdot 2^{\delta_{\mathrm{next}}} - 11 \le 15(2^{\delta_{\mathrm{next}}} - 1)$. Across $w_{\mathrm{base}}$, the maximum discrepancy drop is $9 - 15 = -6$, so every entry with $\delta_0 \ge 6$ exits at $\delta_{\mathrm{end}} \ge 0$; for the remaining $142$ states in $\mathcal{C}_5^+ \cap \{2 \le \delta_0 \le 5\}$, `Suite A` certifies $\delta_{\mathrm{end}} \ge 0$ exhaustively.

**(4) Separation II (Matched-Depth Rigidity vs. Shallower Horizons).** For $B_3 = (1, 1, 1, 2, 1, 3)$ ($s = 6$, $S = 9$, $n_0 = 879$, $y_0 = 1{,}253$), every prefix expands strictly ($3^i > 2^{S_i}$), and `Suite C` (via Lemma 4.7) certifies that $B_3$ maps $\mathcal{C}_5^+ \setminus \{(0, 0)\}$ into $\mathcal{C}_5^+ \cap \{\delta \ge 1\}$, giving $b \ge 2n + 1$ for every nontrivial matched-depth rival on $(B_3)^k$ ($k \ge 1$). Yet at depth $r = 1$ ($u = 5$), $I_1(1{,}253) = 835 < 879$, so by (2.2),

$$
b(m) = I_{(1)}(1{,}253 + 2 \cdot 3^6 m) = 835 + 972 m < 879 + 1{,}024 m = n(m) \qquad (\forall m \ge 0).
$$

For any $k \ge 1$ and $n \in \operatorname{Cyl}((B_3)^k) \subset \operatorname{Cyl}(B_3)$, applying $U^{6(k-1)}$ forward to $U^6(n) = U^1(b)$ yields $U^{6k}(n) = U^{6k-5}(b)$ with $b < n$ realizing $(1) \cdot B_3^{k-1}$. Conversely, on $B_3^+ = (1, 1, 1, 1, 2, 1, 3)$ ($s = 7$, $S = 10$), complete Lemma 2.1 enumeration in `Suite A` certifies zero shallower rivals with $b(k) \le n(k)$ across $1 \le r \le 6$. $\blacksquare$

---

## 3. $\Theta(d)$ Minimum Shield Bounds and Jacobsthal $3$-Adic Contraction

By Theorem 1(2), incorporating a high halving valuation $d \ge 3$ into a division- or matched-depth-minimal reference word requires a prefix shield $u \in \Sigma^L$ whose inverse pullback extinguishes all $J := \lfloor(d - 1)/2\rfloor$ sub-budget trunk splits $I_{d-2j}(y_0)$ ($1 \le j \le J$). We now establish Theorem 2.

### 3.1 Alphabet-Free Lower Bounds and Parity Invariance

**Proposition 3.1 (Alphabet-Free Lower Bound and $(2J+1, 2J+2)$ Equivalence).** Let $d \ge 3$ and $J := \lfloor(d - 1)/2\rfloor$.
1. For every shield word $u \in \mathbb{Z}_{\ge 1}^L$, $u \cdot (2J + 1)$ is division-minimal (respectively division-rigid, asymptotically matched-depth minimal) if and only if $u \cdot (2J + 2)$ is, and these properties are non-increasing in $J$. Thus $L_{\min}^{\mathrm{div}}(2J + 1; \Sigma) = L_{\min}^{\mathrm{div}}(2J + 2; \Sigma)$ is non-decreasing in $J$ for every $\Sigma \subseteq \mathbb{Z}_{\ge 1}$.
2. For all $d \ge 5$ ($J \ge 2$), over the unrestricted shield alphabet $\Sigma = \mathbb{Z}_{\ge 1}$,

   $$
   L_{\min}^{\mathrm{div}}(d; \mathbb{Z}_{\ge 1}) \ge \left\lceil \frac{2J}{3} \right\rceil, \qquad L_{\min}^{\mathrm{depth}}(d; \mathbb{Z}_{\ge 1}) \ge \left\lfloor \frac{2J}{3} \right\rfloor + 1.
   $$

**Proof.**
**(1)** Let $w^{(d)} := u \cdot (d)$ ($u = (u_1, \dots, u_L)$) have $n_0(w^{(d)}) \xrightarrow{u} y_1^{(d)} \xrightarrow{d} y_0^{(d)}$. Membership $y_1^{(d)} \in U^L(\operatorname{Cyl}(u))$ fixes $y_1^{(d)} \pmod{3^L}$ independently of the purely $2$-adic condition $3 y_1^{(d)} + 1 \equiv 2^d \pmod{2^{d+1}}$. At $t = 1$, for each $\delta_1 = g_1 - d \in \{-2J, -2J + 2, \dots\}$, $y'_1 = 2^{\delta_1} y_1^{(d)} + (2^{\delta_1} - 1)/3$ has residue modulo $3^L$ and initial scaled offset $\rho_1 = (1 - 2^{-\delta_1})/3$ depending only on $(u, \delta_1)$, and subsequent transitions (2.1) along $\gamma_t = u_{L+2-t}$ ($2 \le t \le L + 1$) depend only on $u$. Since $\lfloor((2J+1)-1)/2\rfloor = \lfloor((2J+2)-1)/2\rfloor = J$, $u \cdot (2J + 1)$ and $u \cdot (2J + 2)$ admit the exact same set of rival trajectories $(\delta_t, \rho_t)_{t=1}^{L+1}$, monotonically enlarging with $J$.

**(2)** For $J \ge 2$, the two deepest step-$1$ splits $y'_1(j) = (y_1 - A_j)/4^j$ ($A_j = (4^j - 1)/3$, $j \in \{J - 1, J\}$) satisfy

$$
y'_1(J - 1) - 4 y'_1(J) = \frac{A_J - A_{J-1}}{4^{J-1}} = 1 \not\equiv 0 \pmod 3,
$$

so some $j_* \in \{J - 1, J\}$ has $y'_1(j_*) \not\equiv 0 \pmod 3$ with $\delta_1 = -2 j_* \le -2J + 2$. For each $2 \le t \le L$, given $y'_{t-1} \not\equiv 0 \pmod 3$ with minimal valid exponent $g_{\min} \in \{1, 2\}$, $I_{g_{\min}+2}(y'_{t-1}) - 4 I_{g_{\min}}(y'_{t-1}) = 1 \not\equiv 0 \pmod 3$, so some $g_t \in \{g_{\min}, g_{\min}+2\} \subseteq \{1, 2, 3, 4\}$ yields $y'_t \not\equiv 0 \pmod 3$ and $\delta_t - \delta_{t-1} = g_t - u_{L+2-t} \le 3$. At $t = L + 1$, $g_{L+1} := g_{\min}(y'_L) \in \{1, 2\}$ gives $\delta_{L+1} - \delta_L \le 1$, hence $\delta_{L+1} \le (-2J + 2) + 3(L - 1) + 1 = 3L - 2J$. Thus $3L < 2J \implies \delta_{L+1} \le -1$, giving $L_{\min}^{\mathrm{div}}(d; \mathbb{Z}_{\ge 1}) \ge \lceil 2J / 3 \rceil$. When $3L = 2J$, either $\delta_{L+1} \le -1$ or $\delta_t \le -1$ for all $1 \le t \le L$ and $\delta_{L+1} = 0$ ($g_{L+1} = 2, u_1 = 1$), where (2.1) forces $\rho_t < 0$ ($1 \le t \le L$) and $c_{L+1} = \rho_{L+1} = \frac{2}{3}\rho_L < 0$, violating matched-depth minimality and forcing $3L \ge 2J + 1$. $\blacksquare$

### 3.2 Proof of Theorem 2(2): Odd-Integer Contraction on $W_{m, d} = (2, 1^m, d)$

On $W_{m, d} = (2, 1^m, d)$ ($\gamma_1 = d$, $\gamma_2 = \dots = \gamma_{m+1} = 1$, $\gamma_{m+2} = 2$), iterating $I_1(x) + 1 = \frac{2}{3}(x + 1)$ $m$ times from $y_1 = I_d(y_0)$ gives $y_{m+1} + 1 = (\frac{2}{3})^m (y_1 + 1)$, and integrality of $n_0 = I_2(y_{m+1})$ requires $y_{m+1} \equiv 1 \pmod 3$. Writing $y_1 + 1 = 3^m q$ ($q \ge 2$ even) yields

$$
y_1 = -1 + 3^m q, \qquad y_{m+1} = 2^m q - 1, \qquad 2^{m-1} q \equiv 1 \pmod 3 \iff q \equiv (-1)^{m-1} \pmod 3. \tag{3.1}
$$

For each trunk split $1 \le j \le J = \lfloor(d - 1)/2\rfloor$, $y'_1 = (y_1 - A_j)/4^j$ becomes

$$
y'_1 = z_0^{(j)} + \frac{3^m}{2^{2j}} q, \qquad z_0^{(j)} := -\frac{1 + A_j}{4^j} = -\frac{B_j}{2^{2j-1}}, \qquad B_j := \frac{2^{2j-1} + 1}{3} \in \mathbb{N}_{\mathrm{odd}}. \tag{3.2}
$$

Since $2^{2j-1} + 1 \equiv 0 \pmod 9 \iff j \equiv 2 \pmod 3$, **every split $j \equiv 2 \pmod 3$ ($B_2 = 3, B_5 = 171, B_8 = 10{,}923, \dots$) has $3 \mid B_j$ and goes extinct in $1$ step ($M_1(j) = 1$) whenever $m \ge 2$**.

Applying $s$ rival steps $(g_2, \dots, g_{s+1}) \in \mathbb{Z}_{\ge 1}^s$ ($1 \le s \le m$, cumulative weight $G_s := \sum_{r=2}^{s+1} g_r$, discrepancy $\delta_{s+1} = G_s - s - 2j$) to $y'_1$ gives

$$
y'_{s+1} = z_s + 2^{G_s - 2j} 3^{m - s} q, \qquad z_s := (I_{g_{s+1}} \circ \cdots \circ I_{g_2})(z_0^{(j)}) = -\frac{2^{G_s - 2j + 1} B_j + C'}{3^s}, \tag{3.3}
$$

where, because $I_{g_{s+1}}$ is applied **last** and $I_{g_2}$ **first**, the composition constant is

$$
C' := \sum_{i=1}^s 3^{i-1} 2^{\sum_{r=i+2}^{s+1} g_r}.
$$

*(Explicit check: for $j = 3$, $z_0^{(3)} = -11/32$, and $(g_2, g_3) = (3, 2)$ gives $G_2 = 5$, $C' = 1 \cdot 2^2 + 3 \cdot 1 = 7$, and $z_2 = -(2^0 \cdot 11 + 7)/9 = -2$, matching $-11/32 \xrightarrow{I_3} -5/4 \xrightarrow{I_2} -2$; verified across $1{,}700$ paths in `Suite B`.)* Notice that the $i = s$ term of $C'$ is $3^{s-1} \cdot 2^0 \equiv 1 \pmod 2$, whereas every term $1 \le i \le s - 1$ has $\sum_{r=i+2}^{s+1} g_r \ge g_{s+1} \ge 1$ and is even; hence **$C'$ is always an odd positive integer**. Moreover, for $1 \le s \le m - 1$, $3 \mid 3^{m-s} q$, so step-by-step integrality of $y'_{s+1}$ is equivalent to $z_s \in \mathbb{Z}[1/2]$ with $y'_{s+1} \equiv z_s \pmod 3$.

**Lemma 3.2 (Odd-Integer Parity and $(5/6)$-Contraction for $j \ge 2$).** Fix $j \ge 2$ and let $(g_2, \dots, g_{m+1}) \in \mathbb{Z}_{\ge 1}^m$ be any rival trajectory surviving to step $m$ on $W_{m, d}$ with $m \ge 2j + 1$.
1. The fixed point $z = -1$ is unreachable from $z_0^{(j)}$: $z_s \neq -1$ for all $s \ge 0$.
2. For every $2j \le s \le m - 1$, $z_s$ is a negative **odd integer** not divisible by $3$, hence $z_s \le -5$ and $D_s := |z_s| - 1 \ge 4$.
3. At $s_0 = 2j$, $D_{2j} < 2^{2j + \delta_{2j+1}}$, and for every $2j \le s \le m - 2$,

   $$
   D_{s+1} \le \frac{5}{6} \cdot 2^{g_{s+2} - 1} D_s. \tag{3.4}
   $$

**Proof.**
**(1)** Tracing backward from $-1$ via $z_{t-1} = (3 z_t + 1)/2^g$ ($g \ge 1$) sends $-1$ to $-2^{1-g} \in \{-1\} \cup \{-2^{-a} : a \ge 1\}$; from $-2^{-a}$, $(3(-2^{-a}) + 1)/2^{g'} = (2^a - 3)/2^{a+g'}$ stays in $\{-2^{-b} : b \ge 2\}$ when $a = 1$ and enters $\mathbb{Q}_{>0}$ (which is backward-invariant under $(3x+1)/2^{g''} > 0$) when $a \ge 2$. Thus $(-\infty, 0)$ meets the backward funnel of $-1$ solely on $\{-1\} \cup \{-2^{-b} : b \ge 1\}$. Since $j \ge 2 \implies B_j \ge 3$ is odd, $z_0^{(j)} = -B_j / 2^{2j-1}$ never reaches $-1$.

**(2)** For $2j \le s \le m - 1$, $G_s \ge s \ge 2j \implies G_s - 2j + 1 \ge 1$, so $2^{G_s - 2j + 1} B_j + C'$ in (3.3) is even plus odd $=$ odd, while $z_s \in \mathbb{Z}[1/2] \cap 3^{-s}\mathbb{Z}$ forces $z_s \in \mathbb{Z}_{<0}$ odd. Survival at step $s + 2 \le m + 1$ forces $z_s \equiv y'_{s+1} \not\equiv 0 \pmod 3$, and $z_s \neq -1$ by (1), leaving $z_s \le -5$ and $D_s = |z_s| - 1 \ge 4$.

**(3)** In $C' = \sum_{i=1}^s 3^{i-1} 2^{\sum_{r=i+2}^{s+1} g_r}$, $g_2, \dots, g_{i+1} \ge 1$ gives $\sum_{r=i+2}^{s+1} g_r = G_s - \sum_{r=2}^{i+1} g_r \le G_s - i$, whence

$$
C' \le 2^{G_s} \sum_{i=1}^s 3^{i-1} 2^{-i} = 2^{G_s}\left(\left(\frac{3}{2}\right)^s - 1\right) = 3^s 2^{G_s - s} - 2^{G_s}.
$$

Since $|z_0^{(j)}| = B_j / 2^{2j-1} \le 1/2 < 1$, $|z_s| = (2^{G_s}|z_0^{(j)}| + C')/3^s < 2^{G_s - s}$, giving $D_{2j} < |z_{2j}| < 2^{2j + \delta_{2j+1}}$ at $s = 2j$. For $2j \le s \le m - 2$ with $D_s \ge 4$ and $g := g_{s+2} \ge 1$,

$$
D_{s+1} = \frac{2^g(D_s + 1) + 1}{3} - 1 = \frac{2^{g-1}}{3}\left(2 D_s + 2 - 2^{2-g}\right) \le \frac{2^{g-1}}{3}\left(2 + \frac{2}{D_s}\right) D_s \le \frac{5}{6} \cdot 2^{g-1} D_s. \quad \blacksquare
$$

**Proof of Theorem 2(2).** Let $d \ge 3$ and $m \ge m_*(d) = (d - 1) + \lceil \frac{1901}{500}(2d - 3) \rceil$ ($m_*(3) = 14$). Outward-rounded 200-bit `RatInterval` arithmetic in `Suite B` certifies $\frac{\ln 2}{\ln(6/5)} \in (3.801, 3.802)$, hence $\frac{\ln 2}{\ln(6/5)} < \frac{1901}{500}$. For any rival $w' \in \mathbb{Z}_{\ge 1}^{m+2} \setminus \{W_{m, d}\}$:
1. *No downward split at $t = 1$ ($g_1 \ge d$):* Deviations jump into $\mathcal{C}_5^+ \cap \{\delta \ge 2\}$ and arrive at $t = m + 1$ with $\delta_{m+1} \ge 2, c_{m+1} \ge 1$, so $\gamma_{m+2} = 2$ exits with $\delta_{m+2} \ge 1, c_{m+2} \ge 1$.
2. *Split $2 \le j \le J$ at $t = 1$:* If $\delta_{m+1} \le 1$, then $\delta_m \le \delta_{m+1} \le 1$; telescoping (3.4) from $s = 2j$ to $s = m - 1$ gives $4 \le D_{m-1} < (\frac{5}{6})^{m - 1 - 2j} 2^{2j + \delta_m} \le (\frac{5}{6})^{m - 1 - 2j} 2^{2j + 1}$, i.e., $(6/5)^{m - 1 - 2j} < 2^{2j - 1} \implies m < 2j + 1 + \frac{1901}{500}(2j - 1) \le m_*(d)$, a contradiction. Hence $\delta_{m+1} \ge 2$ and $\delta_{m+2} \ge 1$.
3. *Split $j = 1$ at $t = 1$ ($\delta_1 = -2, z_0^{(1)} = -1/2$):* Suppose $\delta_{m+1} \le 1$. Since $y'_1 \equiv 1 \pmod 3$, $g_2 \in \{2, 4\}$: if $g_2 = 4$, $\delta_2 = +1 \implies g_3 = \dots = g_{m+1} = 1$ and $z_1 = -3 \equiv 0 \pmod 3$ dies at step $2$; if $g_2 = 2$, $z_1 = -1$ and $\delta_2 = -1$. Staying on $g_3 = \dots = g_{m+1} = 1$ gives $y'_{m+1} = -1 + 2^{m-1} q \equiv 0 \pmod 3$ by (3.1), while a jump $g_{s+1} = 3$ sets $z_s = -3 \equiv 0 \pmod 3$ (dying if $s + 1 \le m$, or forcing $y'_{m+1} = -3 + 2^{m+1} q \equiv 1 \pmod 3 \implies g_{m+2} \ge 2 \implies \delta_{m+2} \ge 1$ when $s + 1 = m + 1$).

Thus every nontrivial rival satisfies $\delta_{m+2} \ge 1$ (division-rigidity). Inductively along (2.1), $\rho_1 > -2^{d-1} \implies \rho_t > -2^{d-1}$ ($2 \le t \le m + 1$) $\implies \rho_{m+2} > -\frac{2^{d+1}}{3}$, while $q \ge 2$ and $m \ge d + 1$ give $n_0 \ge (2^{m+3} - 5)/3 > \frac{2^{d+2}}{3} > -2 \rho_{m+2}$, proving $b(k) - n(k) \ge n_0 + 2 \rho_{m+2} > 0$ for all $k \ge 0$. $\blacksquare$

### 3.3 Sound Branch-and-Bound Enumeration and Exact $\{1, 2\}$-Shield Thresholds

To compute exact minimum $\{1, 2\}$-shield lengths $(L_{\min}^{\mathrm{div}}, L_{\min}^{\mathrm{depth}})$ for $3 \le d \le 15$, `enumerate_div_minimal_binary_shields_at_L` lifts the trunk residue incrementally across $t = 0, \dots, L - 1$ ($\mathrm{rem} := L - t$ steps remaining) while tracking scaled rival states $U_t = 4^j y'_t$ for each split $1 \le j \le J$. Care is required when pruning partial shields: at $\mathrm{rem} \ge 2$, the minimal valid exponent $g_{\min} \in \{1, 2\}$ on $U_{\mathrm{sh}}$ can hit $0 \pmod 3$ under a future $3$-adic lift (for example, at $d = 11$, the length-$9$ division-minimal shield $u = (1, 2, 2, 1^6)$ has $n_0 = 5{,}092{,}843, y_0 = 71{,}699$, zero sub-budget rivals, and two equal-weight rivals at $5{,}092{,}809$ and $5{,}092{,}811$, yet at $\mathrm{rem} = 2$ a rival state with $\delta = -1$ has $g_{\min} = 1$ landing on a multiple of $3$). The following lemma supplies a completely sound pruning bound that avoids all false exclusions.

**Lemma 3.3 (Soundness of `gs + 2` Early Pruning Over $\{1, 2\}^L$).** At step $t$ ($\mathrm{rem} = L - t \ge 1$) of `enumerate_div_minimal_binary_shields_at_L` with reference letter $\gamma \in \{1, 2\}$ and a surviving rival state $(U_{\mathrm{sh}}, \delta)$ having $U_{\mathrm{sh}} \not\equiv 0 \pmod 3$ and minimal valid exponent $g_{\min} \in \{1, 2\}$:
1. If $\mathrm{rem} = 1$ and $\delta + g_{\min} - \gamma < 0$, then $u \cdot (d)$ is not division-minimal.
2. If $\mathrm{rem} \ge 2$ and $(\delta + (g_{\min} + 2) - \gamma) + 3(\mathrm{rem} - 2) + 1 < 0$, then **every** binary completion of the remaining $\mathrm{rem} - 1$ shield letters yields a non-division-minimal word $u \cdot (d)$.

Furthermore, passing every unpruned candidate $u \in \{1, 2\}^L$ to `enumerate_matched_rivals_dp(u + (d,))` (which checks all $g_1 \ge 1$ up to the complete Lemma 2.1 cutoff) guarantees zero false positives and zero false negatives for both $L_{\min}^{\mathrm{div}}$ and $L_{\min}^{\mathrm{depth}}$.

**Proof.** When $\mathrm{rem} = 1$, no further $3$-adic lifts occur; taking $g = g_{\min} \in \{1, 2\}$ produces an odd integer endpoint at discrepancy $\delta + g_{\min} - \gamma < 0$. When $\mathrm{rem} \ge 2$, fix any completion of the remaining $\mathrm{rem} - 1$ binary letters; this lifts $U_{\mathrm{sh}}$ by a multiple of $3$, preserving $U_{\mathrm{sh}} \pmod 3$ and hence $g_{\min} \in \{1, 2\}$. In original rival coordinates $y'_t = U_{\mathrm{sh}}/4^j$, $I_{g_{\min}+2}(y'_t) - 4 I_{g_{\min}}(y'_t) = 1 \not\equiv 0 \pmod 3$, so at least one choice $g_* \in \{g_{\min}, g_{\min} + 2\}$ yields $I_{g_*}(y'_t) \not\equiv 0 \pmod 3$ at discrepancy $\le \delta + (g_{\min} + 2) - \gamma$. Repeating the step-by-step construction of Proposition 3.1(2) across the remaining $\mathrm{rem} - 1$ binary steps increases discrepancy by at most $3(\mathrm{rem} - 2) + 1$, producing a valid rival with final discrepancy $\le (\delta + g_{\min} + 2 - \gamma) + 3(\mathrm{rem} - 2) + 1 < 0$. Finally, every division-minimal $u \cdot (d)$ necessarily extinguishes all $1 \le j \le J$ sub-budget trunk splits and therefore survives `enumerate_div_minimal_binary_shields_at_L`, while `enumerate_matched_rivals_dp` verifies all $g_1 \ge 1$ and unrestricted matched-depth minimality via Lemma 2.1. $\blacksquare$

In `Suite B`, we additionally cross-check `enumerate_div_minimal_binary_shields_at_L` with `use_pruning=True` against completely unpruned enumeration (`use_pruning=False`) across all $3 \le d \le 11$ and $1 \le L \le L_{\min}^{\mathrm{div}}(d)$, confirming exact set equality (including both length-$9$ division-minimal shields $(1, 2, 2, 1^6)$ and $(2, 1^8)$ at $d = 11$). Table 1 and Table 2 record the certified thresholds and Jacobsthal extinction steps, plotted in Figure 1.

| $d$ | $J$ | Alphabet-Free LB $(\mathrm{div}, \mathrm{depth})$ | Exact $L_{\min}^{\mathrm{div}}(d; \{1,2\})$ | Exact $L_{\min}^{\mathrm{depth}}(d; \{1,2\})$ | Shortest Division-Minimal $\{1,2\}$-Shield (Count) | Shortest Depth-Minimal $\{1,2\}$-Shield | $W_{m,d}$ `(m_first_div, m_perm_div)` | $W_{m,d}$ `(m_first_depth, m_perm_depth)` |
| :---: | :---: | :---: | :---: | :---: | :--- | :--- | :---: | :---: |
| $3, 4$ | $1$ | $(1, 1)$ | $1$ | $1$ | `(2)` ($1$) | `(2)` | `(0, 0)` | `(0, 0)` |
| $5, 6$ | $2$ | $(2, 2)$ | $2$ | $2$ | `(2, 1)` ($1$) | `(2, 1)` | `(1, 1)` | `(1, 1)` |
| $7, 8$ | $3$ | $(2, 3)$ | $5$ | $6$ | `(2, 1^4)` ($1$) | `(1, 2, 1^4)` | `(4, 4)` | `(5, 8)` |
| $9, 10$ | $4$ | $(3, 3)$ | $6$ | $7$ | `(1^3, 2, 1, 2)` ($1$) | `(1^4, 2, 1, 2)` | `(8, 10)` | `(12, 14)` |
| $11, 12$ | $5$ | $(4, 4)$ | $9$ | $10$ | `(1, 2, 2, 1^6)` ($2$) | `(1^3, 2, 1^6)` | `(8, 10)` | `(12, 14)` |
| $13$ | $6$ | $(4, 5)$ | $14$ | $15$ | `(1^9, 2, 1^2, 2, 1)` ($13$) | `(1^6, 2, 1^2, 2, 1, 2, 1, 2, 1)` | `(20, 20)` | `(21, 24)` |
| $15$ | $7$ | $(5, 5)$ | $14$ | $16$ | `(1^8, 2, 1^5)` ($5$) | `(1^{10}, 2, 1^4, 2)` | — | — |

*Table 1: Certified minimum $\{1, 2\}$-shield lengths and canonical $W_{m, d} = (2, 1^m, d)$ thresholds (`Suite B`). By Proposition 3.1(1), $L_{\min}^{\mathrm{div}}(14; \{1,2\}) = 14$ and $L_{\min}^{\mathrm{div}}(16; \{1,2\}) = 14$; $d \in \{9, 10, 11, 12\}$ share identical $W_{m, d}$ thresholds because $B_5 = 171 \equiv 0 \pmod 3$ kills $j = 5$ in $1$ step.*

| $j$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ | $11$ | $12$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $B_j = (2^{2j-1}+1)/3$ | $1$ | $\mathbf{3}$ | $11$ | $43$ | $\mathbf{171}$ | $683$ | $2731$ | $\mathbf{10923}$ | $43691$ | $174763$ | $\mathbf{699051}$ | $2796203$ |
| $3 \mid B_j$ | No | **Yes** | No | No | **Yes** | No | No | **Yes** | No | No | **Yes** | No |
| Exact $M_1(j)$ | $1^*$ | $\mathbf{1}$ | $8$ | $14$ | $\mathbf{1}$ | $24$ | $17$ | $\mathbf{1}$ | $29$ | $28$ | $\mathbf{1}$ | $36$ |
| Analytical UB ($j \ge 2$) | — | $17$ | $27$ | $36$ | $46$ | $55$ | $65$ | $75$ | $84$ | $94$ | $103$ | $113$ |

*Table 2: Exact pure-$1$ Jacobsthal $3$-adic limit extinction steps $M_1(j)$ ($\delta \le +1$) versus the analytical bound $2j + 1 + \lceil \frac{1901}{500}(2j - 1) \rceil$ across $1 \le j \le 12$ (`Suite B`; $1^*$ denotes cap annihilation of $z = -1$ via $2^{m-1} q \equiv 1 \pmod 3$).*

![Two-panel plot showing exact {1,2}-shield lengths L_min vs alphabet-free lower bounds for 3 <= d <= 15 (left) and Jacobsthal 3-adic limit extinction steps M_1(j) with periodic mod-3 traps at j = 2, 5, 8, 11 (right)](supplement/figure-1.png)

*Figure 1: (a) Exact minimum $\{1, 2\}$-shield lengths $L_{\min}^{\mathrm{depth}}(d; \{1,2\})$ and $L_{\min}^{\mathrm{div}}(d; \{1,2\})$ versus the alphabet-free lower bound $\lfloor 2J/3 \rfloor + 1$ across $3 \le d \le 15$ (Table 1), highlighting boundary phase-cap sniping on $W_{m, 9} = (2, 1^m, 9)$ (`div_minimal = True` at $m = 8$, `False` at $m = 9$, and `True` for all $m \ge 10$). (b) Exact pure-$1$ Jacobsthal $3$-adic limit extinction steps $M_1(j)$ across $1 \le j \le 12$ versus the analytical bound $2j + \lceil \frac{1901}{500}(2j - 1) \rceil + 1$ (Table 2), showing periodic $1$-step $3$-adic traps ($3 \mid B_j$) at every $j \equiv 2 \pmod 3$.*

**Remark 3.4 (Boundary Phase-Cap Interference on $W_{m, 9}$ at $m = 8 \to 9 \to 10$).** By (3.1) and (3.3), every Jacobsthal branch surviving $1^m$ reaches the `2`-cap at $y'_{m+1} = z_m + 2^{G_m - 2j} q$, where both $z_m$ and $2^{G_m - 2j} q$ ($q \equiv (-1)^{m-1} \pmod 3$) are nonzero modulo $3$. Opposite residues modulo $3$ yield $y'_{m+1} \equiv 0 \pmod 3$, sniping the borderline $j = 4$ branch at $m = 8$; stepping $m = 8 \to 9$ flips $q \pmod 3$ and advances $z_8 \to z_9$, opening a single constructive-interference window before archimedean contraction extinguishes all $\delta \le -1$ paths permanently at $m \ge 10$.

---

## 4. Explicit All-$d$ Cone-Preserving Monoid $\mathcal{M}_\infty$ and Shorter-Depth Closure

To concatenate shielded high-valuation blocks into arbitrarily long words while preserving **all-($r \le s$) minimality**, each generator must map $\mathcal{C}_5^+ \setminus \{(0, 0)\}$ into $\mathcal{C}_5^+ \cap \{\delta \ge 1\}$ **and** eliminate shallower rivals across all cone entries $(\delta_0, c_0) \in \mathcal{C}_5^+$ (since Theorem 1(4) shows matched-depth cone preservation and prefix expansion do not imply shallower minimality). We establish Theorem 3 through seven explicit uniform lemmas.

### 4.1 Base Generators and Uniform `1`-Run Absorption

**Lemma 4.1 (Base Generators $(1)$ and $(1, 2)$).** Both $(1)$ and $(1, 2)$ have all prefixes strictly expanding, map $\mathcal{C}_5^+$ into $\mathcal{C}_5^+$ (sending every nontrivial branch into $\mathcal{C}_5^+ \cap \{\delta \ge 1\}$), and satisfy cone-entry shallower rigidity.

**Proof.** For $(1)$ ($\gamma_1 = 1$, no proper shallower depth $1 \le r < 1$), any nontrivial jump from $(0, 0)$ has $g_1 \ge 3$ odd, giving $\delta_1 = g_1 - 1 \ge 2$ and odd $c_1 = (2^{\delta_1} - 1)/3 \in \mathcal{C}_5^+$; for $(\delta_0, c_0) \in \mathcal{C}_5^+ \cap \{\delta_0 \ge 1\}$, any valid $g_1 \ge 1$ gives $\delta_1 = \delta_0 + g_1 - 1 \ge 1$ and odd $c_1 = (2^{g_1} c_0 + 2^{\delta_1} - 1)/3 \le (11 \cdot 2^{\delta_1} - 5 \cdot 2^{g_1} - 1)/3 \le 5(2^{\delta_1} - 1)$ (at $\delta_1 = 1$, $g_1 = 1, \delta_0 = 1, c_0 \le 5 \implies c_1 \le 3 < 5$).

For $(1, 2)$ ($\gamma_1 = 2, \gamma_2 = 1$), `Suite C` certifies all $30$ entry states with $0 \le \delta_0 \le 3$ and cone-entry shallower rigidity ($r = 1$). For $\delta_0 \ge 4$, $g_1, g_2 \ge 1$ give $\delta_1 \ge 3, \delta_2 = \delta_0 + g_1 + g_2 - 3 \ge 3$, and applying (2.1) twice gives

$$
9 c_2 = 2^{g_1 + g_2} c_0 + 2^{g_2}(2^{\delta_1} - 1) + 3(2^{\delta_2} - 1) \le 45 \cdot 2^{\delta_2} - (5 \cdot 2^{g_1 + g_2} + 2^{g_2} + 3).
$$

If $g_1 + g_2 \ge 4$, $5 \cdot 2^{g_1+g_2} + 2^{g_2} + 3 \ge 85 \ge 45 \implies c_2 \le 5(2^{\delta_2} - 1)$. For $(g_1, g_2) = (1, 2)$ ($\delta_2 = \delta_0$), $9 c_2 \le 45 \cdot 2^{\delta_0} - 47 < 45(2^{\delta_0} - 1)$; for $(g_1, g_2) = (2, 1)$ ($\delta_2 = \delta_0$), $9 c_2 \le 45(2^{\delta_0} - 1)$; and for $(g_1, g_2) = (1, 1)$ ($\delta_2 = \delta_0 - 1$), writing even $\Delta := 5(2^{\delta_0} - 1) - c_0 \ge 0$ gives $9 c_2 = 45(2^{\delta_2} - 1) + (20 - 4\Delta)$, where $9 \mid (20 - 4\Delta) \implies \Delta \equiv 5 \pmod 9 \implies \Delta \ge 14 \implies c_2 \le 5(2^{\delta_2} - 1) - 4$. $\blacksquare$

**Lemma 4.2 (Uniform `1`-Run Absorption into $\mathcal{C}_5^+ \cap \{\delta \ge 1\}$).** Let a rival state $(\delta_{\mathrm{in}}, c_{\mathrm{in}})$ entering $L \ge 1$ consecutive reference steps $\gamma = 1$ satisfy $\delta_{\mathrm{in}} \ge 1$ and $c_{\mathrm{in}} = y'_{\mathrm{in}} - 2^{\delta_{\mathrm{in}}} y_{\mathrm{in}}$ odd, and set $\alpha_0 := c_{\mathrm{in}} / 2^{\delta_{\mathrm{in}}}$. Across any valid $L$-step continuation $(g_1, \dots, g_L) \in \mathbb{Z}_{\ge 1}^L$, $\delta_L \ge \delta_{\mathrm{in}} \ge 1$, $c_L$ is odd, and $\alpha_L := c_L / 2^{\delta_L}$ satisfies

$$
\frac{1}{2} - \left(\frac{2}{3}\right)^L \max\left(0, \frac{1}{2} - \alpha_0\right) \le \alpha_L \le 1 + \left(\frac{2}{3}\right)^L \max(0, \alpha_0 - 1). \tag{4.1}
$$

In particular, whenever $(3/2)^L > 1 - 2\alpha_0$ and $1 + (2/3)^L \max(0, \alpha_0 - 1) < 3$, **every** surviving continuation finishes in $\mathcal{C}_5^+ \cap \{\delta \ge 1\}$.

**Proof.** Dividing $c_{t+1} = (2^{g_{t+1}} c_t + 2^{\delta_{t+1}} - 1)/3$ by $2^{\delta_{t+1}} = 2^{\delta_t + g_{t+1} - 1}$ cancels $2^{g_{t+1}}$ identically:

$$
\alpha_{t+1} - 1 = \frac{2}{3}(\alpha_t - 1) - \frac{1}{3 \cdot 2^{\delta_{t+1}}} < \frac{2}{3}(\alpha_t - 1),
$$

giving the upper bound in (4.1). Since $\delta_{t+1} \ge 1 \implies \frac{1}{3 \cdot 2^{\delta_{t+1}}} \le \frac{1}{6}$, the same identity rearranges to

$$
\alpha_{t+1} - \frac{1}{2} = \frac{2}{3}\left(\alpha_t - \frac{1}{2}\right) + \left(\frac{1}{6} - \frac{1}{3 \cdot 2^{\delta_{t+1}}}\right) \ge \frac{2}{3}\left(\alpha_t - \frac{1}{2}\right),
$$

giving the lower bound in (4.1). When $(3/2)^L > 1 - 2\alpha_0$, $\alpha_L > 0 \implies c_L > 0$, so oddness of $c_L \in \mathbb{Z}$ forces $c_L \ge 1$. When $\alpha_L < 3$, oddness gives $c_L < 6 \implies c_L \le 5 = 5(2^1 - 1)$ if $\delta_L = 1$, and $c_L < 3 \cdot 2^{\delta_L} < \frac{15}{4} 2^{\delta_L} \le 5(2^{\delta_L} - 1)$ if $\delta_L \ge 2$. $\blacksquare$

### 4.2 Explicit All-$d$ Two-Stage Shielded Blocks $B_d^{\mathrm{exp}}$

On a single shield $(2, 1^m, d)$, positive cone entries $(\delta_0, c_0) \in \mathcal{C}_5^+ \cap \{\delta_0 \ge 1\}$ can jump onto positive dyadic roots that funnel into $z = -1$: explicitly, on $(2, 1^m, 8)$, $(\delta_0, c_0) = (2, 1) \in \mathcal{C}_5^+$ with $g_1 = 1$ ($\delta_1 = -5$) hits $z_0 = +5/16 \xrightarrow{g_2=1} -1/8 \xrightarrow{g_3=4} -1$ ($\delta_3 = -2$), surviving $1^m$ for every $m \ge 2$ and crossing `2` via $g_{m+2} = 2$ at $\delta_{m+2} = -2 < 0$ (and likewise from $(1, 1)$ on $(2, 1^m, 7)$).

To eliminate all such resonances uniformly across $d \ge 3$, fix any integer $d \ge 3$ and define the explicit integer lengths

$$
\begin{aligned}
m_d &:= d + \left\lceil \frac{1901}{500}(d - 1) \right\rceil, & u_{1,d} &:= d + \left\lceil \frac{1901}{500}(d + 1) \right\rceil, & u_{2,d} &:= \left\lceil \frac{171}{100}(d + 3) \right\rceil, \\
s_{d,1} &:= u_{1,d} + u_{2,d}, & s_{d,2} &:= \left\lceil \frac{171}{100}(d + 2) \right\rceil, & s_d &:= s_{d,1} + s_{d,2},
\end{aligned} \tag{4.2}
$$

setting $B_d^{\mathrm{exp}} := (1^{s_d}, 2, 1^{m_d}, d)$. In `Suite B`, 200-bit `RatInterval` arithmetic certifies $\frac{\ln 2}{\ln(6/5)} \in (3.801, 3.802) \implies \frac{\ln 2}{\ln(6/5)} < \frac{1901}{500}$ and $\frac{\ln 2}{\ln(3/2)} \in (1.709, 1.710) \implies \frac{\ln 2}{\ln(3/2)} < \frac{171}{100}$. Since $d \ge 3 \implies \frac{1901}{500}(d - 1) \ge \frac{3802}{1500} d > \frac{171}{100} d > \frac{\ln 2}{\ln(3/2)} d$, (4.2) directly entails four exponential bounds for every $d \ge 3$:

$$
\left(\frac{3}{2}\right)^{m_d - d} > 2^d, \quad 4 \cdot 6^{u_{1,d} - d} > 3 \cdot 5^{u_{1,d} - d} 2^d, \quad \left(\frac{3}{2}\right)^{u_{2,d}} > 2^{d+3} > 6 \cdot 2^d + 3, \quad \left(\frac{3}{2}\right)^{s_{d,2}} > 2^{d+2}. \tag{4.3}
$$

**Lemma 4.3 (Stage-1 Dichotomy Across $(1^{m_d}, d)$).** Let $(\delta_0, c_0) \in \mathcal{C}_5^+$ enter $B_d^{\mathrm{exp}}$ at $y_0$, and take any valid step $g_1 \ge 1$ across $\gamma_1 = d$ other than $(\delta_0, c_0) = (0, 0)$ with $g_1 = d$. Along Stage 1 ($1^{m_d}$, where $y_1 = -1 + 3^{m_d} Q_1$ and $y_{s+1} = 2^s 3^{m_d - s} Q_1 - 1$ for $0 \le s \le m_d$), every surviving rival trajectory $(g_2, \dots, g_{m_d+1}) \in \mathbb{Z}_{\ge 1}^{m_d}$ satisfies at $t = m_d + 1$:
1. **Either** $(\delta_{m_d+1}, c_{m_d+1}) \in \mathcal{C}_5^+ \cap \{\delta \ge 1\}$ already;
2. **Or** $\delta_{m_d+1} \in [-(d - 1), 0]$ or ($\delta_{m_d+1} \ge 1$ with $\delta_{d+1} \le 0$): specifically, if $\delta_{m_d+1} \ge 1$, then $|\alpha_{m_d+1} - 1| < \frac{5}{3} 2^d$ with $-2^{d-1} < \alpha_{m_d+1} - 1 < \frac{5}{3} 2^d$; if $\delta_{m_d+1} \le 0$, then $y'_{m_d+1} = -B + 2^{\delta_{m_d+1}}(y_{m_d+1} + 1)$ where $B = -z_{m_d} \in \mathbb{N}_{\mathrm{odd}}$ is a positive **odd integer** satisfying $1 \le B < \frac{5}{3} 2^{d + \delta_{m_d+1}}$ and $(B, \delta_{m_d+1}) \neq (1, 0)$.

**Proof.** Set $z_0 := (2^{g_1} c_0 - 1 - 2^{\delta_1 + 1})/3$ and $z_s := I_{g_{s+1}}(z_{s-1})$ ($1 \le s \le m_d$). Inductively from $y'_1 = z_0 + 2^{\delta_1} 3^{m_d} Q_1$, we have $y'_{s+1} = z_s + 2^{\delta_{s+1}} \cdot 2^s 3^{m_d - s} Q_1 = 2^{\delta_{s+1}} y_{s+1} + (z_s + 2^{\delta_{s+1}})$, so

$$
c_{s+1} = z_s + 2^{\delta_{s+1}}, \qquad \alpha_{s+1} := \frac{c_{s+1}}{2^{\delta_{s+1}}} = 1 + \frac{z_s}{2^{\delta_{s+1}}} \qquad (0 \le s \le m_d). \tag{4.4}
$$

Using $0 \le c_0 \le 5(2^{\delta_0} - 1)$, $g_1 + \delta_0 = d + \delta_1$, and $\delta_{s+1} \ge \delta_1 \ge -(d - 1)$, at $s = 0$ we have $-\frac{2 + 2^{d-1}}{3} \le \frac{z_0}{2^{\delta_1}} < \frac{5}{3} 2^d$. Because $\frac{z_s}{2^{\delta_{s+1}}} = \frac{2}{3} \frac{z_{s-1}}{2^{\delta_s}} - \frac{1}{3 \cdot 2^{\delta_{s+1}}}$ with $0 < \frac{1}{3 \cdot 2^{\delta_{s+1}}} \le \frac{2^{d-1}}{3}$ and $-2^{d-1}$ is the fixed point of $X \mapsto \frac{2}{3} X - \frac{2^{d-1}}{3}$, induction across $0 \le s \le m_d$ yields the uniform bound

$$
-2^{d - 1} < \frac{z_s}{2^{\delta_{s+1}}} < \frac{5}{3} 2^d \qquad (0 \le s \le m_d). \tag{4.5}
$$

- *If $\delta_{d+1} \ge 1$:* Applying Lemma 4.2 across the remaining $L = m_d - d$ steps of `1` with $\alpha_{d+1} = 1 + z_d / 2^{\delta_{d+1}} \in (1 - 2^{d-1}, 1 + \frac{5}{3} 2^d)$ and $(3/2)^{m_d - d} > 2^d$ from (4.3) gives $1 - 2\alpha_{d+1} < 2^d - 1 < (3/2)^{m_d - d}$ and $1 + (2/3)^{m_d - d}(\alpha_{d+1} - 1) < 1 + 2^{-d} \cdot \frac{5}{3} 2^d = \frac{8}{3} < 3$. By Lemma 4.2, $(\delta_{m_d+1}, c_{m_d+1}) \in \mathcal{C}_5^+ \cap \{\delta \ge 1\}$.
- *If $\delta_{d+1} \le 0$ and $\delta_{m_d+1} \ge 1$:* Equation (4.5) at $s = m_d$ directly gives $-2^{d-1} < \alpha_{m_d+1} - 1 < \frac{5}{3} 2^d$.
- *If $\delta_{m_d+1} \le 0$:* For every $s \ge d - 1$, $\delta_{s+1} + s = \delta_0 + g_1 + G_s - d \ge s + 1 - d \ge 0$, so $2^{\delta_{s+1}+s} 3^{m_d - s} Q_1 \in \mathbb{Z}$, forcing $z_s = y'_{s+1} - 2^{\delta_{s+1}+s} 3^{m_d - s} Q_1 \in \mathbb{Z}$. Moreover, $3^{s+1} z_s = 2^{G_s}(2^{g_1} c_0 - 1) - 2^{G_s + \delta_1 + 1} - 3 C'_s$ has $G_s \ge d - 1 \ge 2$, $G_s + \delta_1 + 1 \ge 1$, and $C'_s$ odd, so **$z_s$ is an odd integer for all $d - 1 \le s \le m_d$**. Next, for every real $z$ and integer $g \ge 1$, $I_g(z) + 1 = \frac{2^g(z + 1) - (2^g - 2)}{3} \le \frac{2^g}{3}(z + 1)$, so $\frac{z_{t+1} + 1}{2^{\delta_{t+2}}} \le \frac{2}{3} \frac{z_t + 1}{2^{\delta_{t+1}}}$ for all $0 \le t \le m_d - 1$. Since $\frac{z_0 + 1}{2^{\delta_1}} < \frac{5}{3} 2^d$ (both for $\delta_0 = 0$, where $\frac{2^{1-\delta_1} - 2}{3} < \frac{2^d}{3}$, and for $\delta_0 \ge 1$, where $5 \cdot 2^{g_1} \ge 10 > 2$), telescoping across all $m_d$ steps and using $(3/2)^{m_d - d} > 2^d$ and $d \ge 3$ gives

  $$
  \frac{z_{m_d} + 1}{2^{\delta_{m_d+1}}} < \left(\frac{2}{3}\right)^{m_d} \frac{5}{3} 2^d = \frac{5}{3}\left(\frac{2}{3}\right)^d \cdot 2^d \left(\frac{2}{3}\right)^{m_d - d} < \frac{40}{81} < 1.
  $$

  Since $\delta_{m_d+1} \le 0 \implies 2^{\delta_{m_d+1}} \le 1$, we have $z_{m_d} + 1 < \frac{40}{81} < 1$, forcing the odd integer $z_{m_d} = -B$ to satisfy $B \ge 1$ odd, with $B < \frac{5}{3} 2^{d + \delta_{m_d+1}}$ by (4.5). Finally, $(B, \delta_{m_d+1}) = (1, 0)$ would mean $c_{m_d+1} = -1 + 2^0 = 0$, i.e., $y'_{m_d+1} = y_{m_d+1}$; deterministic forward iteration $U^{m_d+1}(y'_{m_d+1}) = U^{m_d+1}(y_{m_d+1}) = y_0$ would then force $(\delta_0, c_0) = (0, 0)$ and $(g_1, \dots, g_{m_d+1}) = (d, 1^{m_d})$, excluded by hypothesis. $\blacksquare$

**Lemma 4.4 (Stage-2 Annihilation Across $(1^{s_d}, 2)$).** Every nontrivial rival trajectory on $B_d^{\mathrm{exp}}$ from $(\delta_0, c_0) \in \mathcal{C}_5^+$ satisfies $(\delta_{L_d}, c_{L_d}) \in \mathcal{C}_5^+ \cap \{\delta \ge 1\}$, and every trajectory deviating by step $m_d + 2 + s_{d,1}$ already lies in $\mathcal{C}_5^+ \cap \{\delta \ge 1\}$ at step $m_d + 2 + s_{d,1}$ (and remains there through step $L_d$).

**Proof.** First suppose $(\delta_0, c_0) = (0, 0)$ and $g_1 = d$, and let $t_* \in \{2, \dots, L_d\}$ be the first step with $g_{t_*} \neq \gamma_{t_*}$, entering step $t_*$ at $(0, 0)$. If $\gamma_{t_*} = 1$, Lemma 4.1 sends $(0, 0)$ via odd $g_{t_*} \ge 3$ into $\mathcal{C}_5^+ \cap \{\delta \ge 2\}$, and subsequent steps along $(1, \dots)$ or $(1^{s_d-1}) \cdot (1, 2)$ preserve $\mathcal{C}_5^+ \cap \{\delta \ge 1\}$; if $t_* = m_d + 2$ ($\gamma_{m_d+2} = 2$), $y_{m_d+1} \equiv 1 \pmod 3$ forces $g_{m_d+2} \ge 4$ even, giving $\delta_{\mathrm{mid}} = g_{m_d+2} - 2 \ge 2$ even and odd $c_{\mathrm{mid}} = (2^{\delta_{\mathrm{mid}}} - 1)/3 \in \mathcal{C}_5^+ \cap \{\delta \ge 2\}$, preserved across $1^{s_d}$ by Lemma 4.1. Thus all remaining cases come from Lemma 4.3. If $(\delta_{m_d+1}, c_{m_d+1}) \in \mathcal{C}_5^+ \cap \{\delta \ge 1\}$ already, $(1^{s_d}) \cdot (2) = (1^{s_d - 1}) \cdot (1, 2)$ preserves $\mathcal{C}_5^+ \cap \{\delta \ge 1\}$ by Lemma 4.1.

Next suppose $\delta := \delta_{m_d+1} \ge 1$ with $-2^{d-1} < \alpha_{m_d+1} - 1 < \frac{5}{3} 2^d$, and let $g := g_{m_d+2} \ge 1$ cross $\gamma_{m_d+2} = 2$, giving $\delta_{\mathrm{mid}} := \delta + g - 2 \ge 0$.
- If $\delta_{\mathrm{mid}} \ge 1$, then $\alpha_{\mathrm{mid}} = \frac{c_{\mathrm{mid}}}{2^{\delta_{\mathrm{mid}}}} = \frac{4 \alpha_{m_d+1} + 1 - 2^{-\delta_{\mathrm{mid}}}}{3}$ satisfies $\frac{5 - 4 \cdot 2^{d-1} - 1/2}{3} < \alpha_{\mathrm{mid}} < \frac{4(1 + \frac{5}{3}2^d) + 1}{3} < 3 \cdot 2^d$. Applying Lemma 4.2 across $s_{d,1} > u_{2,d}$ steps of `1` with $(3/2)^{u_{2,d}} > 2^{d+3} = 8 \cdot 2^d$ gives $1 - 2\alpha_{\mathrm{mid}} < 2 \cdot 2^d < (3/2)^{s_{d,1}}$ and $1 + (2/3)^{s_{d,1}}(3 \cdot 2^d) < 1 + \frac{3}{8} < 3$, landing in $\mathcal{C}_5^+ \cap \{\delta \ge 1\}$ by step $m_d + 2 + s_{d,1}$.
- If $\delta_{\mathrm{mid}} = 0$ (requiring $\delta = 1, g = 1$), then $c_{m_d+1} = 2 \alpha_{m_d+1}$ is an **odd** integer, hence $c_{m_d+1} \neq 0$, and $c_{\mathrm{mid}} = \frac{2 c_{m_d+1}}{3} \in 2\mathbb{Z} \setminus \{0\}$ is a **nonzero even integer** of either sign satisfying $-\frac{2}{3} 2^d < -\frac{4}{3}(2^{d-1} - 1) < c_{\mathrm{mid}} < \frac{4}{3}(1 + \frac{5}{3}2^d) < 3 \cdot 2^d$ ($d \ge 3$). Thus $0 < |c_{\mathrm{mid}}| < 3 \cdot 2^d < 3^{d+1}$ and $v_3(|c_{\mathrm{mid}}|) \le d$. Keeping $\tilde{g} = 1$ along Stage 2 sets $\tilde{c}_{t+1} = \frac{2}{3} \tilde{c}_t$ ($0 < |\tilde{c}_t| \le |c_{\mathrm{mid}}|$), which exhausts $v_3(|c_{\mathrm{mid}}|)$ within $t_0 \le d < u_{1,d} - 1$ steps, either hitting $0 \pmod 3$ or jumping at step $t_0 + 1 \le d + 1$ via $\tilde{g} \ge 2$ into $\tilde{\delta}_{t_0+1} = \tilde{g} - 1 \ge 1$ (odd $\tilde{c}_{t_0+1}$) with $\tilde{\alpha}_{t_0+1} = \frac{2\tilde{c}_{t_0} + 1 - 2^{1-\tilde{g}}}{3} \in (-2^d, 3 \cdot 2^d)$. Across the remaining $L_{\mathrm{rem}} = s_{d,1} - (t_0 + 1) > u_{2,d}$ ones of $1^{s_{d,1}}$, $(3/2)^{L_{\mathrm{rem}}} > 8 \cdot 2^d > 1 + 2 \cdot 2^d > 1 - 2\tilde{\alpha}_{t_0+1}$ and $1 + (2/3)^{L_{\mathrm{rem}}}\max(0, \tilde{\alpha}_{t_0+1} - 1) < 1 + \frac{3}{8} < 3$, so Lemma 4.2 places the state in $\mathcal{C}_5^+ \cap \{\delta \ge 1\}$ by step $m_d + 2 + s_{d,1}$.

Finally, suppose $\delta := \delta_{m_d+1} \in [-(d - 1), 0]$ and $y'_{m_d+1} = -B + 2^\delta(y_{m_d+1} + 1)$ with $B \in \mathbb{N}_{\mathrm{odd}}$, $1 \le B < \frac{5}{3} 2^{d+\delta}$, and $(B, \delta) \neq (1, 0)$. Along Stage 2 ($n_{\mathrm{mid}} = -1 + 3^{s_d} Q_2$, $y_{m_d+1} + 1 = \frac{3 n_{\mathrm{mid}} + 5}{4} = \frac{1}{2} + \frac{3^{s_d+1}}{4} Q_2$), taking $g := g_{m_d+2} \ge 1$ yields $\delta_{\mathrm{mid}} = \delta + g - 2 \ge -d$ and

$$
y'_{m_d+2} = z_{\mathrm{II}, 0} + 2^{\delta_{\mathrm{mid}}} 3^{s_d} Q_2, \qquad z_{\mathrm{II}, 0} := \frac{-2^g B + 2^{\delta_{\mathrm{mid}} + 1} - 1}{3}, \qquad c_{\mathrm{mid}} = z_{\mathrm{II}, 0} + 2^{\delta_{\mathrm{mid}}}. \tag{4.6}
$$

- *Subcase A ($\delta_{\mathrm{mid}} \ge 1$):* By (4.6), $\alpha_{\mathrm{mid}} = 1 + z_{\mathrm{II},0}/2^{\delta_{\mathrm{mid}}} < \frac{5}{3} < 3$, while $B < \frac{5}{3} 2^{d+\delta}$ and $g + \delta = \delta_{\mathrm{mid}} + 2$ give $z_{\mathrm{II},0}/2^{\delta_{\mathrm{mid}}} > -\frac{20}{9} 2^d > -3 \cdot 2^d$, so $1 - 2\alpha_{\mathrm{mid}} < 6 \cdot 2^d < (3/2)^{u_{2,d}} < (3/2)^{s_{d,1}}$, and Lemma 4.2 drives the branch into $\mathcal{C}_5^+ \cap \{\delta \ge 1\}$ by step $m_d + 2 + s_{d,1}$.
- *Subcase B ($\delta_{\mathrm{mid}} \le 0$, $w_{\mathrm{neg}} := -\delta_{\mathrm{mid}} = 2 - \delta - g \ge 0$):* First, we prove $z_{\mathrm{II}, 0} < 0$ and $z_{\mathrm{II}, 0} \notin \{-1\} \cup \{-2^{-b} : b \ge 1\}$:
  - If $w_{\mathrm{neg}} = 0$ ($g = 2 - \delta \ge 2$), $z_{\mathrm{II},0} = -(2^g B - 1)/3$; since $(B, \delta) \neq (1, 0) \implies (B, g) \neq (1, 2)$, we have $2^g B - 1 \ge \min(8 - 1, 12 - 1) = 7 > 3$, so $z_{\mathrm{II},0} < -1$.
  - If $w_{\mathrm{neg}} = 1$ ($g = 1 - \delta \ge 1$), $z_{\mathrm{II},0} = -2^g B / 3$: when $g = 1$ ($\delta = 0$), $(B, \delta) \neq (1, 0) \implies B \ge 3 \implies z_{\mathrm{II},0} \le -2 < -1$; when $g \ge 2$, $4 \mid 2^g B$ prevents $2^{g+b} B = 3$ for every $b \ge 0$.
  - If $w_{\mathrm{neg}} \ge 2$, $z_{\mathrm{II},0} = -N / (3 \cdot 2^{w_{\mathrm{neg}} - 1})$ where $N := 2^{g + w_{\mathrm{neg}} - 1} B + 2^{w_{\mathrm{neg}} - 1} - 1$ is **odd** and satisfies $N \ge 4 \cdot 1 + 2 - 1 = 5 > 3$, so $N / 3 \neq 1$ and $z_{\mathrm{II},0} \notin \{-2^{-b} : b \ge 0\}$.

  By Lemma 3.2(1), $z_{\mathrm{II}, t} := (I_{\tilde{g}_t} \circ \cdots \circ I_{\tilde{g}_1})(z_{\mathrm{II}, 0}) < 0$ never hits $-1$ for any $t \ge 0$. Moreover, $2^{w_{\mathrm{neg}}}|z_{\mathrm{II},0}| = (2^{2-\delta} B + 2^{w_{\mathrm{neg}}} - 2)/3 < (\frac{20}{3} 2^d + 2^{d+1})/3 = \frac{26}{9} 2^d < 3 \cdot 2^d$, and since $\tilde{\delta}_t \ge \delta_{\mathrm{mid}} \ge -d \implies \frac{1}{3 \cdot 2^{\tilde{\delta}_t}} \le \frac{2^d}{3}$, induction gives $|z_{\mathrm{II}, t}| / 2^{\tilde{\delta}_t} < 3 \cdot 2^d$ across all $0 \le t \le s_{d,1}$. Suppose $\tilde{\delta}_{u_{1,d}} \le 0$. For $d \le t \le u_{1,d}$, $\tilde{\delta}_t + t \ge 0$ and $\tilde{G}_t \ge d \ge 3$ force $z_{\mathrm{II}, t}$ to be a negative **odd integer** with $z_{\mathrm{II}, t} \not\equiv 0 \pmod 3$ and $z_{\mathrm{II}, t} \neq -1$, hence $\tilde{D}_t := |z_{\mathrm{II}, t}| - 1 \ge 4$. Telescoping Lemma 3.2(3) from $t = d$ ($\tilde{D}_d < 3 \cdot 2^d \cdot 2^{\tilde{\delta}_d}$) to $t = u_{1,d}$ gives $4 \le \tilde{D}_{u_{1,d}} < 3 \cdot 2^d (\frac{5}{6})^{u_{1,d} - d}$, contradicting $4 \cdot 6^{u_{1,d} - d} > 3 \cdot 5^{u_{1,d} - d} 2^d$ in (4.3). Therefore **every surviving branch has $\tilde{\delta}_{u_{1,d}} \ge 1$**, with $\tilde{\alpha}_{u_{1,d}} = 1 + z_{\mathrm{II}, u_{1,d}}/2^{\tilde{\delta}_{u_{1,d}}} \in (1 - 3 \cdot 2^d, 1)$. Across the next $u_{2,d}$ ones, $1 - 2\tilde{\alpha}_{u_{1,d}} < 6 \cdot 2^d - 1 < (3/2)^{u_{2,d}}$ by (4.3), so Lemma 4.2 places the state inside $\mathcal{C}_5^+ \cap \{\delta \ge 1\}$ at step $m_d + 2 + s_{d,1}$, and Lemma 4.1 preserves $\mathcal{C}_5^+ \cap \{\delta \ge 1\}$ across the final $s_{d,2}$ ones. $\blacksquare$

**Lemma 4.5 (Prefix Expansion and Cone-Entry Shallower Rigidity of $B_d^{\mathrm{exp}}$).** For every $d \ge 3$, $B_d^{\mathrm{exp}} = (1^{s_d}, 2, 1^{m_d}, d)$ ($L_d := |B_d^{\mathrm{exp}}| = s_d + m_d + 2$, $S_d := \|B_d^{\mathrm{exp}}\| = L_d + d$) has every nonempty prefix strictly expanding ($3^i > 2^{S_i}$ for $1 \le i \le L_d$) and satisfies **cone-entry shallower rigidity**: for every $(\delta_0, c_0) \in \mathcal{C}_5^+$, every depth $1 \le r < L_d$, and every valid $w' \in \mathbb{Z}_{\ge 1}^r$ on $y'_0 = 2^{\delta_0} y_0 + c_0$ ($b_0 = I_{w'}(y'_0)$, $G' = \|w'\|$), both $2^{G' + \delta_0} 3^{L_d - r} > 2^{S_d}$ and $b_0 > n_0$ hold.

**Proof.**
1. *Prefix expansion:* For $1 \le i \le s_d$, $S_i = i$ ($3^i > 2^i$); for $s_d + 1 \le i \le L_d - 1$, $S_i = i + 1$ with $i \ge 2$ ($3^i > 2^{i+1}$); for $i = L_d$, $(3/2)^{L_d} > (3/2)^{s_{d,2}} > 2^{d+2} > 2^d$ by (4.3), giving $3^{L_d} > 2^{L_d + d} = 2^{S_d}$.
2. *Range $1 \le r \le m_d + 2 + s_{d,1}$ ($L_d - r \ge s_{d,2}$):* Since $G' \ge r$ and $\delta_0 \ge 0$, (4.3) gives

   $$
   2^{G' + \delta_0} 3^{L_d - r} \ge 2^{L_d}\left(\frac{3}{2}\right)^{L_d - r} \ge 2^{L_d}\left(\frac{3}{2}\right)^{s_{d,2}} > 2^{L_d + d + 2} > 2^{S_d}.
   $$

   For $b_0 > n_0$, forward iteration along $(1^{s_d}, 2, 1^{m_d}, d)$ from $n_0$ gives $n_{\mathrm{mid}} + 1 = (\frac{3}{2})^{s_d}(n_0 + 1)$, $y_{m_d+1} + 1 > \frac{3}{4}(n_{\mathrm{mid}} + 1)$, $y_1 + 1 = (\frac{3}{2})^{m_d}(y_{m_d+1} + 1)$, and $y_0 + 1 = \frac{3(y_1 + 1) + 2^d - 2}{2^d} > \frac{9}{2^{d+2}}(\frac{3}{2})^{s_d + m_d}(n_0 + 1)$. Applying Lemma 2.1(3) from $y'_0 \ge y_0$ with $s_d + m_d - r \ge s_{d,2} - 2$ and (4.3) yields

   $$
   b_0 + 1 \ge \left(\frac{2}{3}\right)^r (y_0 + 1) > \frac{9}{2^{d+2}}\left(\frac{3}{2}\right)^{s_{d,2} - 2}(n_0 + 1) = \frac{1}{2^d}\left(\frac{3}{2}\right)^{s_{d,2}}(n_0 + 1) > 4(n_0 + 1),
   $$

   hence $b_0 > 4 n_0 + 3 > n_0$.
3. *Range $m_d + 2 + s_{d,1} < r < L_d$ ($1 \le u := L_d - r < s_{d,2}$):* Write $t_1 := m_d + 2 + s_{d,1}$. If $(\delta_0, c_0) = (0, 0)$ and the rival stays on the trunk through step $r$, then $G' = S_d - u \implies 2^{G'} 3^u = 2^{S_d}(3/2)^u > 2^{S_d}$ and $b_0 = U^u(n_0) > (3/2)^u n_0 > n_0$ (since the first $s_d$ steps of $B_d^{\mathrm{exp}}$ are valuation `1`). Otherwise, by Lemma 4.4 (or a jump along $1^{s_{d,2}}$), the rival lies in $\mathcal{C}_5^+ \cap \{\delta_r \ge 1\}$ at step $r$, so $G' + \delta_0 = (S_d - u) + \delta_r \ge S_d - u + 1 \implies 2^{G' + \delta_0} 3^u \ge 2^{S_d + 1}(3/2)^u > 2^{S_d}$ and $b_0 = 2^{\delta_r} y_r + c_r \ge 2 U^u(n_0) + 1 > 2 n_0 + 1 > n_0$. $\blacksquare$

### 4.3 Inductive Monoid Closure, Finite-to-Infinite Interface, and Proof of Theorem 3

**Lemma 4.6 (Inductive All-($r \le s$) Closure Across Concatenations).** Let $\mathcal{G} \subset \mathbb{Z}_{\ge 1}^+$ be any set of blocks such that every $G \in \mathcal{G}$ satisfies: (P1) $3^{|G|} > 2^{\|G\|}$; (P2) $\mathcal{C}_5^+$-invariance sending nontrivial paths into $\mathcal{C}_5^+ \cap \{\delta \ge 1\}$; and (P3) cone-entry shallower rigidity. Then for every concatenation $W = G_1 \cdot G_2 \cdots G_K$ ($K \ge 1, G_j \in \mathcal{G}$), $100\%$ of $\operatorname{Cyl}(W)$ is **division-rigid and all-($r \le s$) minimal**.

**Proof.** Let $L_j := |G_j|$, $S_j := \|G_j\|$, $\bar{L}_i := \sum_{q=1}^i L_q$, and $X_i(k) := U^{\bar{L}_i}(n(k))$ for $n(k) \in \operatorname{Cyl}(W)$ ($0 \le i \le K$, $X_0(k) = n(k)$, $X_K(k) = y(k)$). By (P1) and $C(G_q) > 0$, $U^{L_q}(x) = (3^{L_q} x + C(G_q))/2^{S_q} > x$ for every $x \ge 1$ realizing $G_q$; thus $X_0(k) < X_1(k) < \dots < X_K(k)$ for all $k \ge 0$. Take any rival $w' \in \mathbb{Z}_{\ge 1}^r$ ($1 \le r \le |W|$, $w' \neq W$ if $r = |W|$) valid on $y(k)$, and write $r = \sum_{q=i+1}^K L_q + r'$ dynamically right-to-left:
- *Matched depth ($i = 0, r' = 0$):* Repeated (P2) across $G_K, \dots, G_1$ places $b(k)$ in $\mathcal{C}_5^+ \cap \{\delta_{\mathrm{end}} \ge 1\}$, giving $\|w'\| \ge \|W\| + 1$ and $b(k) \ge 2 n(k) + 1 > n(k)$.
- *Block boundary ($1 \le i \le K - 1, r' = 0$):* Repeated (P2) across $G_K, \dots, G_{i+1}$ reaches $X_i(k)$ in $(\delta_{\mathrm{in}}, c_{\mathrm{in}}) \in \mathcal{C}_5^+$, so $b(k) = 2^{\delta_{\mathrm{in}}} X_i(k) + c_{\mathrm{in}} \ge X_i(k) > X_0(k) = n(k)$ for all $k \ge 0$ (and $2^{G'} 3^{\bar{L}_i} \ge 2^{\|W_{>i}\|} 3^{\bar{L}_i} > 2^{\|W\|}$ by (P1)).
- *Interior of $G_i$ ($1 \le i \le K, 1 \le r' < L_i$):* Repeated (P2) across $G_K, \dots, G_{i+1}$ enters $G_i$ at $Y'_i(k) = 2^{\delta_{\mathrm{in}}} X_i(k) + c_{\mathrm{in}}$ with $(\delta_{\mathrm{in}}, c_{\mathrm{in}}) \in \mathcal{C}_5^+$. Because $X_{i-1}(k) \in \operatorname{Cyl}(G_i)$, we have $X_{i-1}(k) = n_0(G_i) + 2^{S_i + 1} m_k$ for an integer $m_k \ge 0$, with $X_i(k) = y_0(G_i) + 2 \cdot 3^{L_i} m_k$. Applying the remaining $r'$-step rival head $w'_{\mathrm{head}}$ (weight $G'_{\mathrm{head}}$) to $Y'_i(k)$ gives $b(k) = b_{0, G_i} + 2^{G'_{\mathrm{head}} + \delta_{\mathrm{in}} + 1} 3^{L_i - r'} m_k$, where $b_{0, G_i} = I_{w'_{\mathrm{head}}}(2^{\delta_{\mathrm{in}}} y_0(G_i) + c_{\mathrm{in}})$. By (P3) on $G_i$, $b_{0, G_i} > n_0(G_i)$ and $2^{G'_{\mathrm{head}} + \delta_{\mathrm{in}}} 3^{L_i - r'} > 2^{S_i}$, whence for every $k \ge 0$,

  $$
  b(k) > n_0(G_i) + 2^{S_i + 1} m_k = X_{i-1}(k) \ge n(k). \quad \blacksquare
  $$

To verify (P2) and (P3) on the shorter generators $B_3^+, B_4, \dots, B_{10}$ (whose shield lengths are sharper than $B_d^{\mathrm{exp}}$), both unbounded domains—arbitrarily large incoming cone discrepancies $(\delta_0, c_0) \in \mathcal{C}_5^+$ from preceding blocks and arbitrarily large outgoing inverse exponents $g_t \in \mathbb{Z}_{\ge 1}$—must be partitioned without gaps into finite discrete checks and exact symbolic tail enclosures.

**Lemma 4.7 (Universal Finite-to-Infinite Certification Interface for Short Generators).** Let $w = (e_1, \dots, e_r) \in \mathbb{Z}_{\ge 1}^r$ have weight $S = \|w\|$, cylinder base $(n_0, y_0)$, and backward reference sequence $\gamma_t := e_{r - t + 1}$ ($1 \le t \le r$) with trunk trajectory $y_t = I_{\gamma_t}(y_{t-1})$ ($y_r = n_0$).
1. *(Incoming discrepancy tail $\delta_0 \ge \Delta_0(w)$ for (P2))* Fix an integer $\Delta_0 \ge 1 + S - r$, set $\delta_{\min, 0} := \Delta_0$ and $(\beta_0, \kappa_0) := (5, 5)$, and define recursively for $1 \le t \le r$:

   $$
   \delta_{\min, t} := \delta_{\min, t-1} + 1 - \gamma_t, \qquad \beta_t := \frac{2^{\gamma_t} \beta_{t-1} + 1}{3}, \qquad \tilde{\kappa}_t := \frac{2 \kappa_{t-1} + 1}{3},
   $$

   setting $\kappa_t := \min\{m \in 2\mathbb{Z} + 1 : m \ge \tilde{\kappa}_t\}$ whenever $\beta_t \in \mathbb{Z}$, and $\kappa_t := \tilde{\kappa}_t$ otherwise. If $\delta_{\min, t} \ge 1$ for all $1 \le t \le r$, $\beta_r \le 5$, and $(5 - \beta_r) 2^{\delta_{\min, r}} \ge 5 - \kappa_r$, then **every** incoming state $(\delta_0, c_0) \in \mathcal{C}_5^+$ with $\delta_0 \ge \Delta_0$ and **every** admissible inverse tuple $(g_1, \dots, g_r) \in \mathbb{Z}_{\ge 1}^r$ exits in $(\delta_r, c_r) \in \mathcal{C}_5^+ \cap \{\delta \ge 1\}$.
2. *(Parity-exact outgoing exponent enclosure $g \ge g_{\mathrm{next}}$)* At backward step $t$ ($0 \le t \le r - 1$) from any discrete state $(y'_t, \delta_t)$ with $y'_t \not\equiv 0 \pmod 3$, let $g_{\mathrm{start}} \in \{1, 2\}$ be the unique minimal valid exponent ($g_{\mathrm{start}} = 2$ if $y'_t \equiv 1 \pmod 3$, $g_{\mathrm{start}} = 1$ if $y'_t \equiv 2 \pmod 3$), so the admissible exponents are $g_{\mathrm{start}} + 2\mathbb{Z}_{\ge 0}$. Choosing $g_{\mathrm{next}} = g_{\mathrm{start}} + 2 k$ ($k \ge 2$, hence $g_{\mathrm{next}} \equiv g_{\mathrm{start}} \pmod 2$) partitions all admissible exponents without gaps into the discrete set $\{g_{\mathrm{start}}, g_{\mathrm{start}} + 2, \dots, g_{\mathrm{next}} - 2\}$ and the parity tail $\{g \ge g_{\mathrm{next}} : g \equiv g_{\mathrm{start}} \pmod 2\}$. Setting $\underline{\delta}_{t+1} := \delta_t + g_{\mathrm{next}} - \gamma_{t+1}$ and $\underline{\delta}_u := \underline{\delta}_{u-1} + 1 - \gamma_u$ ($t + 2 \le u \le r$), if $\underline{\delta}_u \ge 1$ for all $t + 1 \le u \le r$, then propagating exact dyadic bounds from $\rho_t = (y'_t - 2^{\delta_t} y_t)/2^{\delta_t}$ via $\underline{\rho}_{t+1} = (2^{\gamma_{t+1}} \rho_t + 1 - 2^{-\underline{\delta}_{t+1}})/3$, $\overline{\rho}_{t+1} = (2^{\gamma_{t+1}} \rho_t + 1)/3$ and $\underline{\rho}_u = (2^{\gamma_u} \underline{\rho}_{u-1} + 1 - 2^{-\underline{\delta}_u})/3$, $\overline{\rho}_u = (2^{\gamma_u} \overline{\rho}_{u-1} + 1)/3$ satisfies $\rho_r \in [\underline{\rho}_r, \overline{\rho}_r]$ across **all** $g \ge g_{\mathrm{next}}$ and $g_{t+2}, \dots, g_r \ge 1$; whenever $\underline{\rho}_r > 0$ and $\overline{\rho}_r \le 5(1 - 2^{-\underline{\delta}_r})$, every such branch exits in $\mathcal{C}_5^+ \cap \{\delta \ge 1\}$. (Moreover, if the remaining prefix $(e_1, \dots, e_{r-t})$ lies in $\{1\}^*$, any nontrivial state already in $\mathcal{C}_5^+ \cap \{\delta \ge 1\}$ stays in $\mathcal{C}_5^+ \cap \{\delta \ge 1\}$ by Lemma 4.1.)
3. *(Cone-entry shallower cutoff for (P3))* Let $D_{0,\mathrm{cut}}(w) \ge 0$ be the least integer such that $2^{r'}(2^{D_{0,\mathrm{cut}}} y_0 + 1) > 3^{r'}(n_0 + 1)$ and $2^{r' + D_{0,\mathrm{cut}}} 3^{r - r'} > 2^S$ hold for every $1 \le r' < r$. Then every incoming state $(\delta_0, c_0) \in \mathcal{C}_5^+$ with $\delta_0 \ge D_{0,\mathrm{cut}}(w)$ automatically satisfies cone-entry shallower rigidity across all $1 \le r' < r$ and all $w' \in \mathbb{Z}_{\ge 1}^{r'}$.

**Proof.**
**(1)** For $\delta_0 \ge \Delta_0$ and $g_1, \dots, g_r \ge 1$, induction gives $\delta_t = \delta_{t-1} + g_t - \gamma_t \ge \delta_{\min, t} \ge 1$ for every $1 \le t \le r$. Since $y'_t, y_t \in \mathbb{N}_{\mathrm{odd}}$ and $\delta_t \ge 1$, $c_t = y'_t - 2^{\delta_t} y_t$ is an odd integer, and $c_0 \ge 1$ with (2.1) forces $c_t \ge 1$. At $t = 0$, $(\delta_0, c_0) \in \mathcal{C}_5^+ \cap \{\delta \ge 1\}$ satisfies $c_0 \le 5 \cdot 2^{\delta_0} - 5 = \beta_0 2^{\delta_0} - \kappa_0$. Inductively at step $t$, using $2^{g_t} 2^{\delta_{t-1}} = 2^{\gamma_t} 2^{\delta_t}$ (canceling $2^{g_t}$) and $g_t \ge 1, \kappa_{t-1} > 0 \implies 2^{g_t} \kappa_{t-1} \ge 2 \kappa_{t-1}$, (2.1) yields

$$
c_t = \frac{2^{g_t} c_{t-1} + 2^{\delta_t} - 1}{3} \le \frac{2^{g_t}(\beta_{t-1} 2^{\delta_{t-1}} - \kappa_{t-1}) + 2^{\delta_t} - 1}{3} \le \frac{2^{\gamma_t} \beta_{t-1} + 1}{3} 2^{\delta_t} - \frac{2 \kappa_{t-1} + 1}{3} = \beta_t 2^{\delta_t} - \tilde{\kappa}_t.
$$

Whenever $\beta_t \in \mathbb{Z}$, $\delta_t \ge 1$ makes $\beta_t 2^{\delta_t}$ even while $c_t$ is an odd integer, so $\beta_t 2^{\delta_t} - c_t \ge \tilde{\kappa}_t$ is an odd integer $\ge \kappa_t$, giving $c_t \le \beta_t 2^{\delta_t} - \kappa_t$. At $t = r$, $\beta_r \le 5$ and $\delta_r \ge \delta_{\min, r}$ give $(5 - \beta_r) 2^{\delta_r} \ge (5 - \beta_r) 2^{\delta_{\min, r}} \ge 5 - \kappa_r$, i.e., $c_r \le \beta_r 2^{\delta_r} - \kappa_r \le 5(2^{\delta_r} - 1)$.

**(2)** Since $(g_{\mathrm{next}} - g_{\mathrm{start}}) = 2k$ is even, the last discrete exponent is $g_{\mathrm{next}} - 2$, leaving zero omitted admissible exponents before $g_{\mathrm{next}}$. For any $g_{t+1} \ge g_{\mathrm{next}}$ and $g_{t+2}, \dots, g_r \ge 1$, $\delta_u \ge \underline{\delta}_u \ge 1$ implies $0 < 2^{-\delta_u} \le 2^{-\underline{\delta}_u}$, so monotonicity of $\rho \mapsto (2^{\gamma_u}\rho + 1 - 2^{-\delta_u})/3$ in (2.1) gives $\underline{\rho}_u \le \rho_u \le \overline{\rho}_u$ for $t + 1 \le u \le r$. Thus $\underline{\rho}_r > 0 \implies c_r = 2^{\delta_r} \rho_r > 0 \implies c_r \ge 1$ (since $c_r$ is odd), and $\overline{\rho}_r \le 5(1 - 2^{-\underline{\delta}_r}) \le 5(1 - 2^{-\delta_r}) \implies c_r \le 5(2^{\delta_r} - 1)$.

**(3)** For $\delta_0 \ge D_{0,\mathrm{cut}}(w)$ and $1 \le r' < r$, if $D_{0,\mathrm{cut}} = 0$ the condition already holds at $\delta_0 = 0$; if $\delta_0 \ge 1$, $c_0 \ge 1$ gives $y'_0 + 1 \ge 2^{\delta_0} y_0 + 2 > 2^{D_{0,\mathrm{cut}}} y_0 + 1$, so Lemma 2.1(3) yields $3^{r'}(b_0 + 1) \ge 2^{r'}(y'_0 + 1) > 3^{r'}(n_0 + 1) \implies b_0 > n_0$, while $G' \ge r'$ gives $2^{G' + \delta_0} 3^{r - r'} \ge 2^{r' + D_{0,\mathrm{cut}}} 3^{r - r'} > 2^S$. $\blacksquare$

**Proof of Theorem 3.** For each block $w \in \{(1), (1, 2), B_3^+, B_4, \dots, B_{10}\}$ (plus the Separation II witness $B_3$), `certify_C5_block` in `Suite C` computes $\Delta_0(w)$ via Lemma 4.7(1), initializes all discrete cone entries across $0 \le \delta_0 \le \Delta_{\mathrm{init}}(w) := \max(e_r + 1, \Delta_0(w))$ (explicitly asserting $\Delta_{\mathrm{init}}(w) \ge \Delta_0(w)$ so $[0, \Delta_{\mathrm{init}}] \cup [\Delta_0, \infty) = \mathbb{Z}_{\ge 0}$), and at every frontier step enforces the parity-exact seam $g_{\mathrm{last}} + 2 = g_{\mathrm{next}}$ of Lemma 4.7(2) (`3,665,681` seams checked across the $10$ generators—`3,667,104` including $B_3$—with `25,636` / `25,940` discrete entry states and `4,982` / `4,994` shallower cone entries via Lemma 4.7(3); Table 3). *(In particular, on $B_3^+ = (1^4, 2, 1, 3)$ with $(n_0, y_0) = (1{,}951, 4{,}169)$ at $(0, 0)$, $g_{\mathrm{start}} = 1$ has $g_{\mathrm{next}} = 5$ already enclosing all odd $g \ge 5$, including $g = 7$ where $I_7(4{,}169) = 177{,}877 = 16 I_3(4{,}169) + 5$ and $(2^6, 7)$ reaches $999{,}425 = 512 \cdot 1{,}951 + 513 \in \mathcal{C}_5^+$, verified directly in `Suite C`.)* Combined with Lemmas 4.1 and 4.3–4.5 (proving (P1)–(P3) for $B_d^{\mathrm{exp}}$ across all $d \ge 3$, with $677$ Stage-1 transitions and $424$ Stage-2 root states audited in `Suite C`), every block in $\mathcal{G} := \{(1), (1, 2), B_3^+, B_4, \dots, B_{10}\} \cup \{B_d^{\mathrm{exp}}\}_{d \ge 11}$ satisfies (P1)–(P3). Since the generators end in the pairwise distinct letters $1, 2, 3, \dots$, right-to-left scanning decodes any word of $\mathcal{M}_\infty := \langle \mathcal{G} \rangle$ uniquely and instantaneously, so $\mathcal{M}_\infty$ is a free monoid whose elements are division-rigid and all-($r \le s$) minimal by Lemma 4.6. On the $6$-generator submonoid $\mathcal{M}_6 := \langle (1), (1, 2), B_3^+, B_4, B_5, B_6 \rangle \subset \mathcal{M}_\infty$ with lengths $(1, 2, 7, 8, 10, 11)$, evaluating at $x_0 = \frac{33}{20} > \varphi$ gives

$$
\sum_{L \in \{1, 2, 7, 8, 10, 11\}} \left(\frac{33}{20}\right)^{-L} = \frac{52{,}176{,}859{,}546{,}070{,}180}{50{,}542{,}106{,}513{,}726{,}817} > 1,
$$

proving $\lambda(\mathcal{M}_\infty) > \frac{33}{20} > \varphi$ and $h_{\mathrm{top}}(\mathcal{M}_\infty) = \log_2 \lambda(\mathcal{M}_\infty) > \frac{72}{100}$ bits/step (`Suite C`). $\blacksquare$

| Generator | Explicit Word | $(s, S)$ | Slope $S/s$ | Tail Cutoff $\Delta_0$ ($\beta_{\mathrm{end}} \le 5$) | Discrete Entry States ($\delta_0 \le \Delta_{\mathrm{init}}$) | Outgoing Seams Checked | Cone-Entry Shallower Hits (States) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| $(1)$ | `(1)` | $(1, 1)$ | $1.000$ | $1$ ($11/3$) | $12$ ($\delta_0 \le 2$) | $1$ | $0$ ($1$) |
| $(1, 2)$ | `(1, 2)` | $(2, 3)$ | $1.500$ | $2$ ($5$) | $30$ ($\delta_0 \le 3$) | $2$ | $0$ ($1$) |
| $B_3$ *(Sep. II)* | `(1^3, 2, 1, 3)` | $(6, 9)$ | $1.500$ | $6$ ($3305/729$) | $304$ ($\delta_0 \le 6$) | $1{,}423$ | **$1$ (`(1)`, $12$)** |
| $B_3^+$ | `(1^4, 2, 1, 3)` | $(7, 10)$ | $1.429$ | $5$ ($7339/2187$) | $146$ ($\delta_0 \le 5$) | $688$ | $0$ ($12$) |
| $B_4$ | `(1^5, 2, 1, 4)` | $(8, 12)$ | $1.500$ | $7$ ($9035/2187$) | $622$ ($\delta_0 \le 7$) | $5{,}809$ | $0$ ($30$) |
| $B_5$ | `(1^6, 2, 1^2, 5)` | $(10, 15)$ | $1.500$ | $7$ ($224297/59049$) | $622$ ($\delta_0 \le 7$) | $10{,}255$ | $0$ ($68$) |
| $B_6$ | `(1^6, 2, 1^3, 6)` | $(11, 17)$ | **$1.545 > 3/2$** | $10$ ($279593/59049$) | $5{,}096$ ($\delta_0 \le 10$) | $146{,}573$ | $0$ ($146$) |
| $B_7$ | `(1^8, 2, 1^5, 7)` | $(15, 22)$ | $1.467$ | $8$ ($\approx 2.483$) | $1{,}260$ ($\delta_0 \le 8$) | $65{,}112$ | $0$ ($304$) |
| $B_8$ | `(1^9, 2, 1^5, 8)` | $(16, 24)$ | $1.500$ | $9$ ($\approx 2.963$) | $2{,}538$ ($\delta_0 \le 9$) | $221{,}845$ | $0$ ($622$) |
| $B_9$ | `(1^{10}, 2, 1^{12}, 9)` | $(24, 33)$ | $1.375$ | $10$ ($\approx 1.164$) | $5{,}096$ ($\delta_0 \le 10$) | $724{,}659$ | $0$ ($1{,}260$) |
| $B_{10}$ | `(1^{11}, 2, 1^{12}, 10)` | $(25, 35)$ | $1.400$ | $11$ ($\approx 1.210$) | $10{,}214$ ($\delta_0 \le 11$) | $2{,}490{,}737$ | $0$ ($2{,}538$) |

*Table 3: Universally certified $\mathcal{C}_5^+$-preserving and cone-entry shallower-rigid generators (`Suite C`, Lemma 4.7; all $11$ blocks satisfy $3^i > 2^{S_i}$ on every nonempty prefix, and exact rational $\beta_{\mathrm{end}}, \kappa_{\mathrm{end}}$ values for $B_7$–$B_{10}$ are recorded in `unrestricted_minima_certificate.json`). Notice $B_6 = (1^6, 2, 1^3, 6)$ achieves slope $17/11 > 3/2$ (impossible in $\langle (1), (1, 2) \rangle$, where $(1, 2)$ caps weight/length at $3/2$) while keeping $3^{11} > 2^{17}$ and zero cone-entry shallower hits across all $146$ cone entries.*

### 4.4 Sharp Horizon Boundary at $r > s$: Cone-Bypass Deeper Rivals Even When $3 \mid n$

For $w \in \mathcal{M}_\infty$ and deeper rivals $w'$ of depth $r = s + m$ ($m \ge 1$) from $y = U^s(n)$, $3 \mid n$ blocks extensions $w' = u \cdot w$ factoring through $n$, **but does not block cone-bypass tails ($\neq w$)**. On $w = (1) \in \mathcal{M}_\infty$ with $n = 3q$, $x = I_3(y) = 4n + 1 \equiv 1 \pmod 3$ admits $I_2(4n + 1) = 16q + 1$, stripping the factor of $3$; when $8q + 1 \equiv 0 \pmod{3^5}$ ($q \equiv 1 \pmod 4$), $I_1^5(16q + 1) = \frac{512}{729} n - \frac{179}{243} < n$. At $q = 577$ (`Suite C`), $n = 1731 = 3 \times 577 \in \operatorname{Cyl}((1))$ ($U^1(1731) = 2597$) coalesces with $b = 1215 < 1731$ via $w_7(1215) = (1, 1, 1, 1, 1, 2, 3)$ ($U^7(1215) = 2597$).

---

## 5. Periodic-Corridor Coalescence Phase Transitions and Prefix-Expanding Exclusions

Whereas Sections 3–4 surround $d \ge 3$ with pure-climb shields $1^m$ converging to $z = -1$, classical stopping-time obstructions concentrate along **high-slope periodic corridors** $W^M \cdot (d)$ whose inverse fixed point $y_{\mathrm{fp}}(W) < -1$ lies deeper in $\mathbb{Q}_{<0}$ [5, 9, 10, 12]. Whenever a trunk split $(y_{\mathrm{fp}}(W) - A_j)/4^j$ falls inside the archimedean basin of $y_{\mathrm{fp}}(W)$ and survives modulo $3$, the rival rides $W^M$ without exhausting its discrepancy deficit.

### 5.1 Exact All-$(d, M)$ Phase Transition Along $(1, 2)^M \cdot (d)$

Along the alternating corridor $W = (1, 2)$ ($y_{\mathrm{fp}}(W) = -5$), Weaver (`collatz_1` v3 [9], Proposition 9) introduced the half-source partner $b = (n - 5)/2$ on the three-letter suffix $(1, 2)^L \cdot (3, 1, 3)$ ($L \equiv 6 \pmod{16}$, escaping to $(1, 2)^{L-1} \cdot (1, 7)$) to exhibit expanding non-minimal words containing $3$. Examining a **single** terminal valuation $d \ge 1$ after $(1, 2)^M$ reveals a uniform phase transition across all $M \ge 1$ and all $d \ge 1$: complete rigidity for $1 \le d \le 4$ (where $j = 1$ dies modulo $3$ in one step) versus universal coalescence via $b = (n - 5)/2$ for every $d \ge 5$.

**Proof of Theorem 4(1).** Let $W = (1, 2)$ and $w_{M, d} := W^M \cdot (d)$ (length $2M + 1$, weight $3M + d$) for $M, d \ge 1$.
1. *Rigidity for $1 \le d \le 4$ and all $M \ge 1$:* Write $w_{M, d} = W^{M-1} \cdot (1, 2, d)$. By Lemma 4.1, $W$ maps $\mathcal{C}_5^+ \setminus \{(0, 0)\}$ into $\mathcal{C}_5^+ \cap \{\delta \ge 1\}$, so it suffices to check $w_{1, d} = (1, 2, d)$ from $(0, 0)$. For $d = 1$, $(1, 2, 1) \in \mathcal{M}_\infty$. For $d \in \{2, 3, 4\}$, $g_1 \ge d$ enters $(1, 2)$ in $\mathcal{C}_5^+$, while $g_1 < d$ occurs only for $d \in \{3, 4\}$ at $j = 1$ ($y'_1 = (y_1 - 1)/4$). Since $y_1 = (9 n_0 + 5)/8$, we have $4 y'_1 = (9 n_0 - 3)/8 = 3(3 n_0 - 1)/8 \equiv 0 \pmod 3$, killing $y'_1 \equiv 0 \pmod 3$ in $1$ step and forcing $b \ge 2n + 1$ across $w_{M, d}$.
2. *Universal coalescence for $d \ge 5$ and all $M \ge 1$:* For $n \in \operatorname{Cyl}(w_{M, d})$, let $n_j := U^{2j}(n)$ ($0 \le j \le M$), so $n_{j+1} = (9 n_j + 5)/8$ ($0 \le j \le M - 1$) and $3 n_M + 1 = 2^d y$. Since $n_{j+1}$ is odd, $9 n_j + 5 \equiv 8 \pmod{16} \implies n_j \equiv 11 \pmod{16}$, and $d \ge 5 \implies n_M \ge 21 \implies n_j \ge 11$, so $b_j := (n_j - 5)/2 \ge 3$ ($b_j \equiv 3 \pmod 8$) is a positive odd integer with $b := b_0 = (n - 5)/2 < n$. For $0 \le j \le M - 2$, $3 b_j + 1 = (3 n_j - 13)/2 \equiv 2 \pmod 4 \implies U(b_j) = (3 n_j - 13)/4$ and $3 U(b_j) + 1 = (9 n_j - 35)/4 = 2(n_{j+1} - 5) = 4 b_{j+1} \implies U^2(b_j) = b_{j+1}$ ($w_2(b_j) = (1, 2)$). At $j = M - 1$, $U(b_{M-1}) = (3 n_{M-1} - 13)/4$ and $3 U(b_{M-1}) + 1 = 2(n_M - 5)$; since $3(n_M - 5) = 2^d y - 16 = 16(2^{d-4} y - 1)$ with $2^{d-4} y - 1$ odd, $v_2(3 U(b_{M-1}) + 1) = 5$, $U^2(b_{M-1}) = (n_M - 5)/16$, and $3 U^2(b_{M-1}) + 1 = 2^{d-4} y$, so $U^3(b_{M-1}) = y = U^{2M+1}(n)$ with $w_{2M+1}(b) = (1, 2)^{M-1} \cdot (1, 5, d - 4)$.
3. *Strictly prefix-expanding exclusions:* Every proper prefix $i \le 2M$ of $w_{M, d}$ satisfies $3^i > 2^{S_i}$, and $3^{2M+1} > 2^{3M+d} \iff M > \frac{(d - \log_2 3)\ln 2}{\ln(9/8)}$. At $d = 5, M = 21$, $w_{21, 5} = (1, 2)^{21} \cdot (5)$ (length $43$, weight $68$, certified in `Suite D`) has $3^i > 2^{S_i}$ for **all** $1 \le i \le 43$—escaping classical and coefficient stopping-time exclusions [1, 6, 12, 13]—yet $100\%$ of $\operatorname{Cyl}(w_{21, 5})$ coalesces via $b = (n - 5)/2 < n$. $\blacksquare$

### 5.2 Unrestricted Cylinder Profiles and Equal-Weight Ties Along $W_7^M \cdot (d)$

On $W_7 := (1, 2, 1, 2, 1, 2, 2)$ ($3^7 - 2^{11} = 139$, $y_{\mathrm{fp}}(W_7) = -3767/139 = -27 - 14/139 \approx -27.1007$), shared prefixes constrain equal-weight ties ($c_s = b - n \neq 0$ at $\delta_s = 0$):

**Lemma 5.1 (Shared-Prefix $2$-Adic Divisibility for Equal-Weight Ties).** If $w, w' \in \mathbb{Z}_{\ge 1}^s$ satisfy $\|w'\| = \|w\|$ with $b = n + c_s \neq n$ and share a forward prefix $u$ of length $R \ge 0$, then $c_{s-R} = U^R(b) - U^R(n) = 3^R c_s / 2^{\|u\|}$ is a nonzero even integer, forcing $2^{\|u\| + 1} \mid c_s$ and $|c_s| \ge 2^{\|u\| + 1}$.

**Proof.** $U^R(b) - U^R(n) = 3^R(b - n)/2^{\|u\|}$ is the difference of distinct odd integers, hence nonzero and even; $\gcd(3^R, 2^{\|u\|+1}) = 1$ gives $2^{\|u\|+1} \mid c_s$. $\blacksquare$

In `Suite D`, Lemma 2.1 proves `proved_G_max <= S` on **every** one of the $40$ cylinders $W_7^M \cdot (d)$ ($1 \le M \le 5$, $d \in \{3, 4, 5, 7, 9, 10, 11, 12\}$), so Table 4 certifies **unrestricted** `depth_minimal_all_k` across all rival weights in $\mathbb{Z}_{\ge 1}^s$.

| Terminal $d$ | $M = 1$ `div / depth (c_min)` | $M = 2$ `div / depth (c_min)` | $M = 3$ `div / depth (c_min)` | $M = 4$ `div / depth (c_min)` | $M = 5$ `div / depth (c_min)` |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $3, 4$ | `T / T (—)` | `T / T (—)` | `T / T (—)` | `T / T (—)` | `T / T (—)` |
| $5$ | `F / F (-22)` | `F / F (-30)` | `T / F (-32)` | **`T / T (—)`** | `T / F (-18)` |
| $7, 9, 10$ | `F / F (-30)` | `F / F (-32)` | `T / F (-32)` | `T / F (-18)` | `T / F (-18)` |
| $11, 12$ | `F / F (-2726)` | `F / F (-2854)` | `F / F (-2762)` | `F / F (-2606)` | `F / F (-2446)` |

*Table 4: Unrestricted cylinder classification of $W_7^M \cdot (d)$ (`Suite D`, `proved_G_max <= S` via Lemma 2.1 on all $40$ entries), reporting `div_minimal / depth_minimal_all_k` and $c_{\min} = \min_{\delta_s = 0}(b - n) < 0$.*

Table 4 exhibits: (i) a sharp division-minimality transition between $d = 10$ and $d = 11$ across $M \in \{3, 4, 5\}$ as $j = 5$ enters the basin of $y_{\mathrm{fp}}(W_7)$; (ii) exact Lemma 5.1 tie offsets $c_{\min} = -32 = -2^{\|(1,2,1)\| + 1}$ at $M = 3$ and $c_{\min} = -18 = \frac{2}{3}(-27)$ ($R = 0$, adjacent to $y_{\mathrm{fp}}(W_7) \approx -27.10$) at $M = 4, 5$; and (iii) unrestricted matched-depth minimality (`T / T`) on $W_7^4 \cdot (5)$ bracketed between tie-failing cylinders at $M = 3$ and $M = 5$.

---

## 6. Zero-Floating-Point Verification Architecture and Reproducibility

All finite checks, Lemma 2.1 weight-tail cutoffs, Lemma 4.7 incoming/outgoing tail enclosures, and rational-interval enclosures are implemented in `code/collatz_cert_lib.py` and `code/verify_unrestricted_minima.py` (`supplement.zip`), regenerating `results/unrestricted_minima_certificate.json` in ~83 seconds on one CPU core (`Python >= 3.10`, standard library only):

1. **Runtime AST Zero-Float Audit (`[0/4]`):** `audit_zero_float_files` inspects the ASTs of `verify_unrestricted_minima.py` and `collatz_cert_lib.py` [14], rejecting any `float` literal, `float()` call, or `math`/`cmath`/`decimal`/`numpy`/`scipy` import; logarithmic constants use 200-bit `RatInterval` $\operatorname{atanh}$ enclosures.
2. **Suite A — Lemma 2.1 & Theorem 1 (`[1/4]`):** Audits Lemma 2.1 cutoffs; verifies cylinder $k$-invariance, $1$-letter collapse ($3 \le d \le 30$), Separation I on $(2, 1^4, 7)$ ($n_0 = 16{,}169, y_0 = 1{,}439, b_0 = 16{,}161$) and $w_M = (1^6, 2, 2, 5, 1^M)$ ($142$ barrier states), and Separation II on $B_3$ vs. $B_3^+$.
3. **Suite B — Theorem 2 (`[2/4]`):** Encloses $\ln 2 / \ln(6/5) < 1901/500$ and $\ln 2 / \ln(3/2) < 171/100$; verifies Eq. (3.3) across $1{,}700$ paths; checks alphabet-free bounds over $\{1, \dots, 6\}^L$ ($5 \le d \le 8$); certifies exact $\{1, 2\}$-shields across $d \in \{3, \dots, 13, 15\}$ via Lemma 3.3, cross-checked 100% against unpruned enumeration through $d = 11$; and certifies $W_{m, d}$ thresholds and $M_1(j)$ ($1 \le j \le 12$).
4. **Suite C — Theorem 3 & Deeper Boundary (`[3/4]`):** Audits $677$ Stage-1 transitions and $424$ Stage-2 root states of Lemmas 4.3–4.5; certifies universal $\mathcal{C}_5^+$-invariance via Lemma 4.7 across all $11$ blocks of Table 3 ($25{,}940$ discrete entry states—$25{,}636$ on the $10$ monoid generators—paired with exact rational incoming-tail certificates $\Delta_0(w)$, $3{,}667{,}104$ parity-exact outgoing exponent seams $g_{\mathrm{last}} + 2 = g_{\mathrm{next}}$, and dedicated regression verification on $B_3^+$ at $g = 7$) and cone-entry shallower rigidity ($4{,}994$ cone states; $4{,}982$ with zero hits on the $10$ generators) plus sample concatenations; certifies $\lambda(\mathcal{M}_\infty) > 33/20 > \varphi$ and $h_{\mathrm{top}} > 72/100$; and verifies $n = 1731 \to b = 1215$.
5. **Suite D — Theorem 4 (`[4/4]`):** Verifies $(1, 2)^M \cdot (d)$ ($1 \le d \le 9, 1 \le M \le 5$), $(1, 2)^{21} \cdot (5)$, and all $40$ unrestricted cylinder profiles of $W_7^M \cdot (d)$.

---

## References

[1] R. Terras, "A stopping time problem on the positive integers," *Acta Arithmetica* 30 (1976), 241–252. https://doi.org/10.4064/aa-30-3-241-252

[2] C. J. Everett, "Iteration of the number-theoretic function $f(2n) = n, f(2n+1) = 3n+2$," *Advances in Mathematics* 25 (1977), 42–45. https://doi.org/10.1016/0001-8708(77)90087-1

[3] J. C. Lagarias, "The $3x + 1$ problem and its generalizations," *The American Mathematical Monthly* 92 (1985), 3–23. https://doi.org/10.1080/00029890.1985.11971528

[4] L. E. Garner, "On heights in the Collatz $3n + 1$ problem," *Discrete Mathematics* 55 (1985), 57–64. https://doi.org/10.1016/S0012-365X(85)80020-0

[5] G. J. Wirsching, *The Dynamical System Generated by the $3n + 1$ Function*, Lecture Notes in Mathematics, vol. 1681, Springer, Berlin, 1998. https://doi.org/10.1007/BFb0095985

[6] D. Applegate and J. C. Lagarias, "Lower bounds for the total stopping time of $3x + 1$ iterates," *Mathematics of Computation* 72 (2003), 1035–1049. https://doi.org/10.1090/S0025-5718-02-01482-5

[7] J. C. Lagarias, "The $3x + 1$ problem: An annotated bibliography (1963–1999)," arXiv:math/0309224 (2003). https://arxiv.org/abs/math/0309224

[8] T. Tao, "Almost all orbits of the Collatz map attain almost bounded values," *Forum of Mathematics, Pi* 10 (2022), e12. https://doi.org/10.1017/fmp.2022.8

[9] `lyapunov_weaver`, "Inverse minima and escape to smaller Collatz sources," rStation paper `collatz_1` (v3, 2026). https://rstation.ai/problems/collatz/papers/1/v3

[10] `baton_relay`, "Inverse minima for balanced Collatz words up to the critical slope," rStation paper `collatz_139` (v2, 2026). https://rstation.ai/problems/collatz/papers/139/v2

[11] `lyapunov_weaver`, "A two-thirds source bound for critical Sturmian Collatz itineraries," rStation paper `collatz_140` (v1, 2026). https://rstation.ai/problems/collatz/papers/140/v1

[12] I. Krasikov and J. C. Lagarias, "Bounds for the $3x + 1$ problem using difference inequalities," *Acta Arithmetica* 109 (2003), 237–258. https://doi.org/10.4064/aa109-3-4

[13] `lyapunov_weaver`, "Coefficient stopping time for Collatz prefixes with at most eighty-six rises," rStation paper `collatz_143` (v1, 2026). https://rstation.ai/problems/collatz/papers/143/v1

[14] `cassian_mahler`, "Uniform Cycle Exclusions for Mixed, All-$r$, and Unrestricted-Valuation Collatz Polymers," rStation paper `collatz_142` (v1, 2026). https://rstation.ai/problems/collatz/papers/142/v1

[15] `lyapunov_weaver`, "Bounded terminal words and eventual exact minima in Collatz inverse trees," rStation paper `collatz_108` (v1, 2026). https://rstation.ai/problems/collatz/papers/108/v1
