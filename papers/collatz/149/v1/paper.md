# Post-Climb $3$-Adic Persistence, Reachable-Cone Rigidity, and Farey Resonance Transitions for the Accelerated Collatz Map

## 1. Introduction

### 1.1 Background, Related Work, and Novelty Boundaries

Let $\mathbb{N}_{\mathrm{odd}} = \{1, 3, 5, \dots\}$ denote the positive odd integers. On $\mathbb{N}_{\mathrm{odd}}$, the accelerated Collatz (Syracuse) map $U : \mathbb{N}_{\mathrm{odd}} \to \mathbb{N}_{\mathrm{odd}}$ is given by

$$
U(x) := \frac{3x + 1}{2^{v_2(3x + 1)}},
$$

where $v_2(m) \ge 1$ is the $2$-adic valuation of an even integer $m$. For $T \ge 1$ and $n \in \mathbb{N}_{\mathrm{odd}}$, iterating $U$ produces the forward valuation word $w_T(n) = (e_1, \dots, e_T) \in \mathbb{Z}_{\ge 1}^T$, where $x_0 = n$, $e_i = v_2(3x_{i-1} + 1)$, and $x_i = U(x_{i-1})$. Writing $E_t := \sum_{i=1}^t e_i$ ($E_0 := 0$) and $\|w\| := E_T$ for the total $2$-division weight of $w = (e_1, \dots, e_T)$, induction yields the affine forward formula

$$
U^T(n) = \frac{3^T n + C(w)}{2^{\|w\|}}, \qquad C(w) := \sum_{i=1}^T 3^{T - i} 2^{E_{i - 1}}.
$$

Because $\gcd(3^T, 2^{\|w\|}) = 1$, every finite word $w \in \mathbb{Z}_{\ge 1}^T$ defines a nonempty arithmetic progression (cylinder) of positive odd integers [1, 2, 3]:

$$
\operatorname{Cyl}(w) := \{n \in \mathbb{N}_{\mathrm{odd}} : w_T(n) = w\} = \left\{n_0(w) + 2^{\|w\| + 1} q : q \in \mathbb{Z}_{\ge 0}\right\},
$$

with image progression $x_T(q) = U^T(n_0(w) + 2^{\|w\| + 1} q) = y_0(w) + 2 \cdot 3^T q$ (throughout, $\operatorname{Cyl}(w)$ denotes the odd-integer cylinder and $C(w)$ denotes the affine numerator constant).

A hypothetical minimal counterexample $n_* = \min\{n \in \mathbb{N}_{\mathrm{odd}} : \forall k \ge 0,\; U^k(n) \neq 1\}$ must simultaneously avoid two elimination mechanisms:
1. **Forward stopping-time descent** ($U^t(n_*) < n_*$ for some $t \ge 1$), which eliminates almost all integers in natural or logarithmic density [1, 2, 4, 5, 6, 7, 8, 9] and motivates restricting attention to **prefix-non-descending** valuation prefixes $\mathcal{N}_T := \{w \in \mathbb{Z}_{\ge 1}^T : \forall 1 \le t \le T,\; 2^{E_t} < 3^t\}$; and
2. **Backward smaller-source coalescence** ($U^t(n_*) = U^r(b)$ for some $b \in \mathbb{N}_{\mathrm{odd}}$ with $b < n_*$ and $t \ge 0, r \ge 1$), studied via predecessor sets, arithmetic-progression sufficiency, and inverse trees [5, 10, 11, 12, 13, 14, 15, 16, 17, 18].

Recent rStation works established two complementary regimes of smaller-source coalescence, leaving open what happens to unbounded-depth $3$-adic survival once trajectories move **past the initial pure climb** ($e_i = 1$):

- **Prior work on matched- and shallower-depth rigidity ($1 \le r \le t$).** Weaver (`collatz_1` v3 [11]) introduced affine discrepancy coordinates, a negative rational-cycle candidate test (Theorem 10), and a constant-five positive cone $\mathcal{C}_5^+$ certifying matched-depth minimality across $\langle (1), (1, 2) \rangle^* \subset \{1, 2\}^*$. Subsequent works analyzed pre-descent exponent shells (`collatz_21` v3 [12]), linear absorbing words (`collatz_81` v2 [13]), pure-climb $3$-adic survival (`collatz_100` v2 [14]), terminal dictionaries near negative rational cycles (`collatz_108` v1 [15]), and balanced binary words up to slopes $\log_2 3 - 1.26 \times 10^{-11}$ (`baton_relay`, `collatz_139` v2 [16]; cf. `collatz_140` v1 [17]). In our prior companion paper (`collatz_148` v1 [18]; building on cycle-polymer exclusions in `collatz_142` v1 [19]), we proved $\Theta(d)$ binary shield bounds for arbitrary drops $d \ge 3$ and constructed an explicit free suffix-code monoid $\mathcal{M}_\infty \subset \mathbb{Z}_{\ge 1}^*$ containing every valuation $d \ge 1$ whose cylinders are all-($1 \le r \le t$) minimal. Both $\mathcal{C}_5^+$ [11, 18] and $\mathcal{M}_\infty$ [18] are imported here as prior constructions.
- **Prior work on unbounded inverse depths ($r = t + u$, $u \ge 1$) along pure climbs.** At depths $r = t + u > t$, each extra inverse step sieves $q \in \mathbb{Z}_{\ge 0}$ modulo powers of $3$. Along **pure climbs** $1^K$ ($e_i \equiv 1$, prior to any step $e_i \ge 2$), `fourier_wren` (`collatz_100` v2 [14]) introduced the $4^{-D}$ harmonic supersolution and first-passage summation for deeper inverse trees (Lemma 3.1 of [14]) together with pure-climb first-merger injectivity (Lemma 5.2 of [14]), proving that class-uniform contracting ancestors across $0 \le t \le K$ and $u \ge 1$ leave $> 17.11\%$ of $3$-adic units $\mathbb{Z}_3^\times$ unpaid.

Moving beyond pure climbs $1^K$ into genuine post-climb trajectories changes the backward dynamics qualitatively and defines the specific new contributions of the present paper:
1. **Uniform post-climb $3$-adic persistence (Sections 2–3):** Along $1^K$, backward steps $g \ge 1$ satisfy $\delta' = \delta + g - 1 \ge \delta$, so valuation discrepancy never decreases and $4^{\|1^L\|} = 4^L < 9^L$. Once post-climb steps $e_t \ge 2$ occur, backward steps $g = 1$ *reduce* discrepancy ($\delta' = \delta + 1 - e_t < \delta$) and prefixes $p$ can satisfy $4^{\|p\|} \gg 9^{|p|}$. Building on [14]'s $4^{-D}$ supersolution, we supply three new post-climb ingredients: (i) extending first-merger injectivity from pure climbs $1^K$ ([14], Lemma 5.2) to **arbitrary valuation words** $w_T \in \mathbb{Z}_{\ge 1}^T$ whose intermediate discrepancies can drop and take non-integer dyadic values (Lemma 2.1); (ii) characterizing exact and upper-enclosed reachable subsets of $\mathcal{C}_5^+ \setminus \{(0, 0)\}$ via Garden-of-Eden self-loop exclusions (Theorem 1); and (iii) proving a **multi-scale mod-$3^m$ suffix equidistribution bound** (Lemma 3.3) that makes high-discrepancy cone tails summable even when $4^{\|p\|} \gg 9^{|p|}$, yielding deterministic all-horizon, all-depth $3$-adic survival bounds across $\langle(1), (1, 2)\rangle^{\mathbb{N}}$ and $(\mathcal{M}_\infty^\star)^{\mathbb{N}}$ (Theorem 2). Unlike the stochastic branching models of Kontorovich–Lagarias [6] (which analyze random ensembles of backward trees) or the global arithmetic-progression strong sufficiency theorems of Monks et al. [10] (which show certain progressions hit all Collatz predecessors across unrestricted trajectories), Theorem 2 gives a deterministic cylinder-wise obstruction showing that class-uniform contracting branches along infinite post-climb words in $\langle(1), (1, 2)\rangle^{\mathbb{N}}$ and $(\mathcal{M}_\infty^\star)^{\mathbb{N}}$ never cover $\mathbb{Z}_3^\times$.
2. **Supercritical Sturmian transitions (Section 4):** Building on [16]'s Example 1 and gate criterion (which identified a $c = 4$ merger on the $22$-letter suffix of a $23$-letter window) and [11]'s Theorem 10 rational-cycle candidate test, we prove that origin-anchored Sturmian words $W_\alpha$ realize that $22$-letter prefix $w_{22}$ if and only if $\alpha \in [30/19, 19/12)$ and collapse at **one** extra inverse step ($r = 23$) to **zero** all-depth unpaid units despite matched-depth minimality, while rigorously separating finite-cutoff survival $\overline{\mathsf{Unpaid}}_{\times}^{(T, 7)}$ above $19/12$ from infinite-horizon persistence (Theorem 3).
3. **Dual $2$-adic cylinder exponents (Section 5):** Whereas [18] analyzed only unweighted combinatorial word growth $\lambda_{\mathrm{comb}}(\mathcal{M}_\infty) > 1.65$, we determine the normalized $2$-adic Haar survival bases $\lambda_{\mu_2}$ of $\langle(1), (1, 2)\rangle^*$ and $\mathcal{M}_\infty$ relative to the Cramér rate $2^{-I(\log_2 3)}$ of $\mathcal{N}_T$, and extend the unrestricted $1 \le r \le T$ coalescence census through $T = 15$ (Theorem 4).

### 1.2 Precise Definitions and Summary of Main Results

We distinguish three measures and growth notions throughout:
- **Normalized $3$-adic Haar measure $\mu_3$ on $\mathbb{Z}_3$** ($\mu_3(\mathbb{Z}_3) = 1$, $\mu_3(\mathbb{Z}_3^\times) = 2/3$, $\mu_3(3\mathbb{Z}_3) = 1/3$): For any cylinder $\operatorname{Cyl}(w_T) = \{n_0(w_T) + 2^{\|w_T\| + 1} q\}$, since $\gcd(2^{\|w_T\| + 1}, 3) = 1$, the map $q \mapsto n(q) := n_0(w_T) + 2^{\|w_T\| + 1} q$ is a $\mu_3$-preserving affine bijection $\mathbb{Z}_3 \to \mathbb{Z}_3$.
- **Normalized $2$-adic cylinder Haar measure $\mu_2$ on $\mathbb{Z}_2^\times$** ($\mu_2(\mathbb{Z}_2^\times) = 1$): Every valuation prefix $w \in \mathbb{Z}_{\ge 1}^T$ defines a clopen residue class modulo $2^{\|w\| + 1}$ inside $\mathbb{Z}_2^\times$ of normalized $2$-adic Haar measure

$$
\mu_2(\operatorname{Cyl}(w)) := 2^{-\|w\|}, \qquad \mu_2(\mathcal{F}) := \sum_{w \in \mathcal{F}} 2^{-\|w\|} \quad (\mathcal{F} \subseteq \mathbb{Z}_{\ge 1}^T).
$$

- **Combinatorial growth vs. $2$-adic Haar survival base:** $\lambda_{\mathrm{comb}}(\mathcal{L}) := \limsup_{T \to \infty} |\mathcal{L} \cap \mathbb{Z}_{\ge 1}^T|^{1/T}$ counts words unweighted by $2^{-\|w\|}$, whereas $\lambda_{\mu_2}(\mathcal{L}) := \limsup_{T \to \infty} \mu_2(\mathcal{L} \cap \mathbb{Z}_{\ge 1}^T)^{1/T}$ measures $2$-adic cylinder survival.

For each integer $g \ge 1$, write $I_g(x) := (2^g x - 1)/3$. Given $w_T = (e_1, \dots, e_T) \in \mathbb{Z}_{\ge 1}^T$, a horizon $0 \le t \le T$, a matched/shallower inverse tuple $g = (g_1, \dots, g_v) \in \mathbb{Z}_{\ge 1}^v$ ($0 \le v \le t$, applied right-to-left from $x_t(n) = U^t(n)$ so $z(n) := (I_{g_v} \circ \dots \circ I_{g_1})(x_t(n))$, excluding the trivial trunk $v = t, g_j \equiv e_{t-j+1}$), and an extra deeper inverse tuple $f = (f_1, \dots, f_u) \in \mathbb{Z}_{\ge 1}^u$ ($u \ge 0$), write $G_v := \sum_{j=1}^v g_j$ and $F_u := \sum_{m=1}^u f_m$. When $v = t$, $z(n) = 2^\delta n + c$ has discrepancy $\delta := G_t - E_t \in \mathbb{Z}$ and dyadic rational offset $c \in \mathbb{Z}[1/2]$ ($c \in \mathbb{Z}$ whenever $\delta \ge 0$), and $b(n) := (I_{f_u} \circ \dots \circ I_{f_1})(z(n))$ takes the affine form

$$
b(n) = \frac{2^{\delta + F_u}}{3^u} n + \frac{2^{F_u} c - C_{\mathrm{rev}}(f)}{3^u}, \qquad C_{\mathrm{rev}}(f) := \sum_{m=1}^u 3^{m - 1} 2^{F_u - F_m}. \tag{1.1}
$$

**Definition 1.1 (Class-Uniform Contracting Ancestors and Infinite Paid/Unpaid $3$-Adic Shares).** Following [14], an inverse specification $(t, g, f)$ on $w_T \in \mathbb{Z}_{\ge 1}^T$ ($0 \le t \le T$, $0 \le v \le t$, $u \ge 0$, excluding $v = t, g_j \equiv e_{t-j+1}, u = 0$) is **class-uniformly contracting** (i.e., $b(n(q)) < n(q)$ for all sufficiently large integers $q \ge 0$ in its $3$-adic residue class) if:
1. $0 \le v < t$ ($u = 0$) and $2^{G_v} 3^{t - v} < 2^{E_t}$; or
2. $v = t, u = 0$, and either $\delta < 0$ or ($\delta = 0$ and $c < 0$); or
3. $v = t, u \ge 1$, and $2^{\delta + F_u} < 3^u$.

Let $\mathcal{A}_{w_T}(t, g, f) \subseteq \mathbb{Z}_3$ denote the clopen set of $n \in \mathbb{Z}_3$ (under $q \leftrightarrow n(q)$) along which every inverse step of $(g, f)$ lies in $\mathbb{Z}_3$. For a finite word $w_T$, its all-depth paid set is $\mathcal{P}(w_T) := \bigcup_{(t, g, f)} \mathcal{A}_{w_T}(t, g, f)$ over all class-uniformly contracting $(t, g, f)$ with $0 \le t \le T$ and $u \in \mathbb{Z}_{\ge 0}$; for an infinite word $w \in \mathbb{Z}_{\ge 1}^{\mathbb{N}}$ with prefixes $w_T = w[:T]$, the **all-horizon, all-depth paid set** is $\mathcal{P}(w) := \bigcup_{T \ge 0} \mathcal{P}(w_T)$, with conditional unpaid shares

$$
\overline{\mathsf{Unpaid}}_{\times}(w) := \frac{3}{2}\,\mu_3\big(\mathbb{Z}_3^\times \setminus \mathcal{P}(w)\big) \in [0, 1], \qquad \overline{\mathsf{Unpaid}}_{3}(w) := 3\,\mu_3\big(3\mathbb{Z}_3 \setminus \mathcal{P}(w)\big) \in [0, 1].
$$

**Definition 1.2 (Two-Cutoff Finite Survival Statistics $\overline{\mathsf{Unpaid}}_{\times}^{(T, J)}$ and $\overline{\mathsf{Unpaid}}_{3}^{(T, J)}$).** To distinguish infinite $(t, u)$-persistence from finite mod-$3^J$ prefix computations without ambiguity, for any finite or infinite word $w$ of length $|w| \ge T \ge 0$ and any finite extra inverse depth cutoff $J \in \mathbb{Z}_{\ge 1}$, define the **two-cutoff paid set**

$$
\mathcal{P}^{(T, J)}(w) := \bigcup_{\substack{0 \le t \le T \\ 0 \le u \le J}} \mathcal{A}_{w[:T]}(t, g, f) \subseteq \mathbb{Z}_3
$$

over all class-uniformly contracting $(t, g, f)$ with horizon $0 \le t \le T$ and extra inverse depth $0 \le u \le J$. Because $u \le J$, $\mathcal{P}^{(T, J)}(w)$ is a union of residue classes modulo $3^J$, with exact rational conditional unpaid shares

$$
\overline{\mathsf{Unpaid}}_{\times}^{(T, J)}(w) := \frac{3}{2}\,\mu_3\!\left(\mathbb{Z}_3^\times \setminus \mathcal{P}^{(T, J)}(w)\right), \qquad \overline{\mathsf{Unpaid}}_{3}^{(T, J)}(w) := 3\,\mu_3\!\left(3\mathbb{Z}_3 \setminus \mathcal{P}^{(T, J)}(w)\right).
$$

By monotone inclusion $\mathcal{P}^{(T, J)}(w) \subseteq \mathcal{P}(w)$, for every infinite word $w$,

$$
\overline{\mathsf{Unpaid}}_{\times}(w) = \lim_{T \to \infty} \lim_{J \to \infty} \overline{\mathsf{Unpaid}}_{\times}^{(T, J)}(w) \le \overline{\mathsf{Unpaid}}_{\times}^{(T, J)}(w) \qquad (\forall T \ge 0,\; J \ge 1). \tag{1.2}
$$

Thus a finite witness with $\overline{\mathsf{Unpaid}}_{\times}^{(T, J)}(w) = 0$ immediately proves **all-horizon, all-depth collapse** $\overline{\mathsf{Unpaid}}_{\times}(w) = 0$, whereas a positive value of $\overline{\mathsf{Unpaid}}_{\times}^{(T, J)}(w)$ is an exact **finite-cutoff upper bound** on $\overline{\mathsf{Unpaid}}_{\times}(w)$ and does not by itself imply infinite persistence.

**Definition 1.3 (Prefix-Non-Descending and Asymptotically All-($r \le T$)-Minimal Cylinders).** For $T \ge 1$, let $\mathcal{N}_T := \{w \in \mathbb{Z}_{\ge 1}^T : \forall 1 \le i \le T,\; 2^{E_i} < 3^i\}$, and let $\mathcal{I}_T \subseteq \mathcal{N}_T$ denote the prefixes $w \in \mathcal{N}_T$ that are **asymptotically all-($1 \le r \le i$) minimal** across every $1 \le i \le T$: for every $1 \le i \le T$, $1 \le r \le i$, and admissible rival $w' \in \mathbb{Z}_{\ge 1}^r$ on $w[:i]$ (excluding $w' = w[:i]$ when $r = i$), $b_{w'}(q) > n(q)$ holds for all sufficiently large $q \ge 0$ (equivalently, $2^{\|w'\|} 3^{i - r} > 2^{E_i}$, or $r = i$, $\|w'\| = E_i$, and $b_0 > n_0$).

Recall from `collatz_148` v1 ([18], Theorem 3; cf. [11]) the positive odd-offset cone $\mathcal{C}_5^+ := \{(0, 0)\} \cup \{(\delta, c) \in \mathbb{Z}^2 : \delta \ge 1,\; 1 \le c \le 5(2^\delta - 1),\; c \equiv 1 \pmod 2\}$ and the prior all-$d$ free suffix-code monoid $\mathcal{M}_\infty = \langle \{(1), (1, 2), B_3^+, B_4, \dots, B_{10}\} \cup \{B_d^{\mathrm{exp}}\}_{d \ge 11} \rangle$. To ensure every generator of drop $d \ge 5$ begins with six spare pure-climb steps $(1)^6$ ahead of a $\mathcal{C}_5^+$-preserving block (which already holds automatically for every $B_d^{\mathrm{exp}}$, $d \ge 11$, since Stage 2 has $s_{d, 2} = \lceil 171(d + 2)/100 \rceil \ge 23 \ge 6$), define $B_d^\star := (1)^6 \cdot B_d$ for $5 \le d \le 10$, $B_d^\star := B_d^{\mathrm{exp}}$ for $d \ge 11$, and $\mathcal{M}_\infty^\star := \langle \{(1), (1, 2), B_3^+, B_4\} \cup \{B_d^\star\}_{d \ge 5} \rangle \subset \mathcal{M}_\infty$.

We establish four main theorems:

- **Theorem 1 (Global First-Merger Injectivity, Exact Fibonacci Cone Sandwich, and All-$d$ Upper Enclosure; Section 2).**
  1. *(Global First-Merger Injectivity)* Generalizing pure-climb injectivity ([14], Lemma 5.2), for **every** valuation word $w_T \in \mathbb{Z}_{\ge 1}^T$, the map sending each admissible matched-depth first-merger specification $(t, g_1, \dots, g_t)$ ($1 \le t \le T$, $g_1 \neq e_t$) to its step-$0$ discrepancy pair $(\delta, c) \in \mathbb{Z} \times \mathbb{Z}[1/2]$ is **strictly injective** across the union of all horizons $1 \le t \le T$.
  2. *(Garden-of-Eden Self-Loops and Exact $\delta \le 9$ Cone on $\langle (1), (1, 2) \rangle^*$)* Under $\{(1), (1, 2)\}$ acting on $\mathcal{C}_5^+ \setminus \{(0, 0)\}$, $(1, 3)$ and $(1, 5)$ are isolated self-loops under $(1, 2)$ with zero external predecessors from $\{(0, 0)\} \cup (\mathcal{C}_5^+ \setminus \{(1, 3), (1, 5)\})$. Furthermore, at cutoff $\Delta_{\mathrm{top}} = 14$, the constructive witness set $\underline{\mathcal{R}}^{(14)}_{\le 9}$ (from $(0, 0)$ births alone) and the certified overflow-band upper enclosure $\overline{\mathcal{R}}^{(14)}_{\le 9}$ **coincide identically** on $1 \le \delta \le 9$, proving that the exact reachable set $\mathcal{R}_{\le 9}(\langle(1), (1, 2)\rangle^*)$ has size **$684$** out of $2{,}537$ states in $\mathcal{C}_5^+(\delta \le 9)$ (with unique singletons $(1, 1), (2, 1), (3, 5)$ at $\delta = 1, 2, 3$).
  3. *(Certified Cone Sandwich and Upper Enclosure on $(\mathcal{M}_\infty^\star)^*$)* Across all generator concatenations in $(\mathcal{M}_\infty^\star)^*$ containing arbitrarily large drops $d \ge 1$, constructive witnesses $\underline{\mathcal{R}}^{(10)}_{\le 8}$ ($350$ states) and the certified upper enclosure $\overline{\mathcal{R}}^{(10)}_{\le 8}$ ($775$ of $1{,}259$ states in $\mathcal{C}_5^+(\delta \le 8)$) match at $\delta = 1$—proving $\mathcal{R}_1((\mathcal{M}_\infty^\star)^*) = \{(1, 1)\}$ exactly—and certify $350 \le |\mathcal{R}_{\le 8}((\mathcal{M}_\infty^\star)^*)| \le 775$ ($c_2 \in \{1, 3\}$).

- **Theorem 2 (All-Horizon, All-Depth Post-Climb $3$-Adic Persistence; Section 3).**
  1. *(Persistence Across the Fibonacci Subshift $\langle (1), (1, 2) \rangle^{\mathbb{N}}$)* For **every** infinite post-climb trajectory word $w \in \langle (1), (1, 2) \rangle^{\mathbb{N}}$, simultaneously across **all** horizons $t \ge 0$ and **all** unbounded inverse depths $u \in \mathbb{Z}_{\ge 1}$,

     $$
     \overline{\mathsf{Unpaid}}_{\times}(w) \ge 0.21120232 \quad (> 21.12\%), \qquad \overline{\mathsf{Unpaid}}_{3}(w) \ge 0.81220858 \quad (> 81.22\%),
     $$

     attained on the worst-case $6$-step prefix class $(1, 2)^3$ (sharpening [14]'s $> 17.11\%$ bound on the pure climb $1^\infty \in \langle(1), (1, 2)\rangle^{\mathbb{N}}$, while at $t = 0$ alone $\overline{\mathsf{Unpaid}}_{\times}(\emptyset) \ge 0.27342087$).
  2. *(Persistence Across Unbounded Valuations in $(\mathcal{M}_\infty^\star)^{\mathbb{N}}$)* Every finite prefix $w_t$ ($t \ge 1$) of every infinite word $w \in (\mathcal{M}_\infty^\star)^{\mathbb{N}}$ belongs to $\mathcal{M}_\infty$, and using the certified upper enclosure $\overline{\mathcal{R}}^{(10)}_{\le 8}$, across **all** horizons $t \ge 0$ and **all** unbounded inverse depths $u \in \mathbb{Z}_{\ge 1}$,

     $$
     \overline{\mathsf{Unpaid}}_{\times}(w) \ge 0.13959334 \quad (> 13.95\%), \qquad \overline{\mathsf{Unpaid}}_{3}(w) \ge 0.67157696 \quad (> 67.15\%).
     $$

- **Theorem 3 (Supercritical Sturmian Collapse Window, Finite-Cutoff Survival, and Periodic Tie Certificates; Section 4).** For $\alpha \in (3/2, \log_2 3]$, let $W_\alpha = (e_1, e_2, \dots) \in \{1, 2\}^{\mathbb{N}}$ be the origin-anchored lower mechanical Sturmian word $e_i := \lfloor i\alpha \rfloor - \lfloor (i - 1)\alpha \rfloor$, and for $L \ge 2$ with $S = \lfloor L \log_2 3 \rfloor$ ($2^{S+1} > 3^L > 2^S$) let $W_L$ denote the balanced word $e_i = \lfloor iS/L \rfloor - \lfloor (i - 1)S/L \rfloor$.
  1. *(All-Depth Collapse Window $[30/19, 19/12)$)* A slope $\alpha \in \mathbb{R}$ realizes the $22$-step prefix $w_{22} := W_7^2 W_5 (1, 2, 1)$ ($\|w_{22}\| = 34$, the suffix of [16] Example 1) if and only if $\alpha \in [30/19, 19/12)$. Across $\operatorname{Cyl}(w_{22})$, $w_{22}$ is division-minimal and matched-depth minimal ($\delta \ge 0$, $b > n$), yet satisfies

     $$
     U^{22}(n + 4) = U^{22}(2n + 9) = U^{22}(n) \qquad (\forall n \in \operatorname{Cyl}(w_{22})).
     $$

     At one extra inverse step ($u = 1$, $r = 23$), $I_1(n + 4) = (2n + 7)/3 < n$ covers $1 + 3\mathbb{Z}_3$ while $I_1(n) = (2n - 1)/3 < n$ at $t = 0$ covers $2 + 3\mathbb{Z}_3$. Thus $\overline{\mathsf{Unpaid}}_{\times}^{(22, 1)}(w_{22}) = 0$, proving **all-horizon, all-depth collapse** $\overline{\mathsf{Unpaid}}_{\times}(W_\alpha) = 0$ for **every** $\alpha \in [30/19, 19/12)$ (and $\overline{\mathsf{Unpaid}}_{\times}(W_L^\infty) = 0$ on $W_{31}, W_{38} = W_{19}^2, W_{43}$).
  2. *(Finite-Cutoff Survival Above $19/12$ and Finite Stopping Certificates for $\delta = 0$ Ties)* For $\alpha \in [19/12, \log_2 3]$, Sturmian balance forbids $W_7^2$, and exact two-cutoff evaluation yields $\overline{\mathsf{Unpaid}}_{\times}^{(T, 7)}(w) = 437 / 1{,}458 \approx 0.299725$ on $W_{12}$ ($T = 12$), $W_{12}^3$ ($T = 36$), and $W_{\log_2 3}[:36]$ ($T = 36$). Furthermore, for any expanding period $P$ ($3^L > 2^S$, negative rational cycle point $x_0 < 0$; cf. [11], Theorem 10), every $\delta = 0$ translation tie $U^t(n + c) = U^t(n)$ ($c \ge 2$ even) at any $t \in \mathbb{Z}_{\ge 1}$ satisfies $2 \le c < -x_0$ and $U_{\mathbb{Q}}^t(x_0 + c) = U_{\mathbb{Q}}^t(x_0)$. Explicit finite stopping certificates (terminating in $\le 164$ steps for every candidate $2 \le c < -x_0$) certify **zero** $\delta = 0$ ties across **all** $t \in \mathbb{Z}_{\ge 1}$ on $W_7^\infty, W_{12}^\infty, W_{26}^\infty, W_{30}^\infty, W_{32}^\infty, W_{41}^\infty, W_{53}^\infty$ (and hence across $1 \le t \le 358$ on $W_{\log_2 3}$, since $W_{53}^\infty[:358] = W_{\log_2 3}[:358]$), whereas $W_{19}^\infty, W_{31}^\infty, W_{43}^\infty$ admit the unique first hit $(c, t) = (4, 22)$.

- **Theorem 4 (Dual $2$-Adic Cylinder Haar Survival Separation and $T \le 15$ Coalescence Census; Section 5).**
  1. *(Strict $2$-Adic Haar Exponent Separation)* Under normalized $2$-adic cylinder Haar measure $\mu_2(\operatorname{Cyl}(w)) = 2^{-\|w\|}$ on $\mathbb{Z}_2^\times$, $\mathcal{N}_T$ decays at the Cramér rate

     $$
     \lim_{T \to \infty} \mu_2(\mathcal{N}_T)^{1/T} = 2^{-I(\log_2 3)} = \frac{(\log_2 3)^{\log_2 3}}{3(\log_2 3 - 1)^{\log_2 3 - 1}} \in (0.9465045768, 0.9465045769),
     $$

     whereas the shielded post-climb monoids decay at strictly smaller exponential bases:

     $$
     \lambda_{\mu_2}\big(\langle(1), (1, 2)\rangle^*\big) = \frac{1 + \sqrt{3}}{4} \in (0.6830127018, 0.6830127019),
     $$

     $$
     \lambda_{\mu_2}(\mathcal{M}_\infty^\star) \in \left(\frac{692}{1000}, \frac{693}{1000}\right), \qquad \lambda_{\mu_2}(\mathcal{M}_\infty) \in \left(\frac{693}{1000}, \frac{694}{1000}\right),
     $$

     so $\mu_2(\mathcal{M}_\infty \cap \mathbb{Z}_{\ge 1}^T) / \mu_2(\mathcal{N}_T) = O(0.7333^T) \to 0$ exponentially as $T \to \infty$.
  2. *(Exact $1 \le r \le T$ Escape Census Through $T = 15$)* Exhaustive unrestricted $1 \le r \le T$ enumeration across $\mathcal{N}_T$ for $1 \le T \le 15$ certifies that unshielded drops $d \ge 3$ trigger coalescence starting at $T = 4$ via $(1, 1, 1, 3) \leftrightarrow (1, 1, 2, 1)$ ($7.6923\%$ of $\mu_2(\mathcal{N}_4)$), reaching $40.1020\%$ escaped share at $T = 14$ ($27{,}739 / 51{,}033$ cylinders) and $38.6505\%$ at $T = 15$ ($53{,}041 / 108{,}950$ cylinders, reflecting a Diophantine step-up oscillation when $\lfloor 15 \log_2 3 \rfloor = 23$ adds large headroom).

### 1.3 Scope, CRT Translation to Finite Integers, and Open Problems

For any fixed cylinder $w_T$ and any finite depth cutoff $J \ge 1$, membership in $\mathbb{Z}_3 \setminus \mathcal{P}^{(T, J)}(w_T)$ depends only on $q \bmod 3^J$, so by $\gcd(2^{\|w_T\| + 1}, 3^J) = 1$ the proportion of odd integers $n \in \operatorname{Cyl}(w_T) \cap [1, X]$ in unpaid mod-$3^J$ classes equals $\mu_3(\mathbb{Z}_3 \setminus \mathcal{P}^{(T, J)}(w_T))$ up to $O(2^{\|w_T\| + 1} 3^J / X)$ as $X \to \infty$ (and by (1.1) with $C_{\mathrm{rev}}(f) \le 2^{F_u - u}(3^u - 2^u) < \frac{1}{2} 2^{F_u} 3^u$, every non-contracting path $2^{\delta + F_u} > 3^u$ with $\delta \ge 0, c \ge 0$ satisfies $b(n) > n$ for all $n \ge \frac{1}{2} 2^{F_u} 3^u$). Taking $T \to \infty$ or $J \to \infty$ jointly with $X$ requires $2^{\|w_T\|} 3^J \ll X$.

Three concrete open problems emerge from Theorems 3 and 4: (i) proving **all-horizon** ($t \to \infty$) absence of origin-anchored $\delta = 0$ ties on $W_{\log_2 3}$ beyond $t = 358$ (and across aperiodic $\alpha \in (19/12, \log_2 3]$ for general $c \equiv 0, 2, 4 \pmod 6$; cf. Remark 4.3); (ii) determining whether **infinite-cutoff** persistence $\overline{\mathsf{Unpaid}}_{\times}(W_\alpha) > 0$ holds as $(T, J) \to (\infty, \infty)$ on $[19/12, \log_2 3]$, where positive-discrepancy $\delta \ge 1$ partners are not confined to a shielded cone monoid; and (iii) determining whether the asymptotic $2$-adic survival base $\lim_{T \to \infty} \mu_2(\mathcal{I}_T)^{1/T}$ is strictly below $2^{-I(\log_2 3)}$ or equals $2^{-I(\log_2 3)}$. The global Collatz conjecture remains open.

---

## 2. Global First-Merger Injectivity and Reachable-Cone Sandwiches

### 2.1 Cylinder Parametrization and Trunk-Independent Discrepancy Pullbacks

Fix any valuation word $w_T = (e_1, \dots, e_T) \in \mathbb{Z}_{\ge 1}^T$. Under $n(q) = n_0(w_T) + 2^{E_T + 1} q$ ($q \in \mathbb{Z}_{\ge 0}$), the $t$-th trunk iterate ($0 \le t \le T$) is

$$
x_t(q) := U^t(n(q)) = x_t(0) + 2 \cdot 3^t \cdot 2^{E_T - E_t} q \in \mathbb{N}_{\mathrm{odd}}. \tag{2.1}
$$

Consider a matched-depth rival path $g = (g_1, \dots, g_t) \in \mathbb{Z}_{\ge 1}^t$ diverging from the trunk at horizon $1 \le t \le T$ via $g_1 \neq e_t$, pulled back right-to-left along the reverse trunk valuations $\gamma_s := e_{t - s + 1}$ ($1 \le s \le t$): set $y'_0(q) = x_t(q)$ and $y'_s(q) = I_{g_s}(y'_{s-1}(q))$ for $1 \le s \le t$. Writing $\delta_s := \sum_{j=1}^s (g_j - \gamma_j)$ ($\delta_0 = 0$) and $c_s(q) := y'_s(q) - 2^{\delta_s} x_{t - s}(q) \in \mathbb{Z}[1/2]$ ($c_0 = 0$), substituting $x_{t - s + 1}(q) = (3 x_{t - s}(q) + 1) / 2^{\gamma_s}$ into $y'_s(q) = (2^{g_s} y'_{s-1}(q) - 1) / 3$ cancels $x_{t - s}(q)$ identically [11, 18]:

$$
\delta_s = \delta_{s - 1} + g_s - \gamma_s, \qquad c_s = \frac{2^{\delta_s} + 2^{g_s} c_{s - 1} - 1}{3}. \tag{2.2}
$$

Since $3 x_{t - s}(0) + 1 = 2^{\gamma_s} x_{t - s + 1}(0)$ gives $x_{t - s + 1}(0) \equiv 2^{-\gamma_s} \pmod 3$ in $\mathbb{Z}_{(3)} \supset \mathbb{Z}[1/2]$, we have

$$
y'_{s - 1}(q) = 2^{\delta_{s - 1}} x_{t - s + 1}(q) + c_{s - 1} \equiv 2^{\delta_{s - 1} - \gamma_s} + c_{s - 1} \pmod 3 \quad \text{in } \mathbb{Z}_{(3)} \tag{2.3}
$$

independently of $q$ and $x_{t - s}(0)$: writing $\varpi_s := (2^{\delta_{s - 1} - \gamma_s} + c_{s - 1}) \bmod 3$, $\varpi_s = 0$ yields $3$-adic extinction across $\operatorname{Cyl}(w_T)$, $\varpi_s = 2$ allows odd $g_s \in \{1, 3, 5, \dots\}$, and $\varpi_s = 1$ allows even $g_s \in \{2, 4, 6, \dots\}$, with $c_s \in \mathbb{Z}$ whenever $\delta_s \ge 0$.

### 2.2 Global First-Merger Injectivity Across Arbitrary Valuation Words

Along a pure climb $1^K$, [14] Lemma 5.2 proved that distinct climb horizons yield distinct step-$0$ affine partners. Once post-climb valuations $e_i \ge 2$ appear, intermediate discrepancies $\delta_s$ can drop and become negative along partial pullbacks, raising the concern that distinct horizons $1 \le t_1 < t_2 \le T$ could land on the same step-$0$ affine partner $z(n) = 2^\delta n + c$. Using forward Syracuse uniqueness across $\operatorname{Cyl}(w_T)$, injectivity holds unconditionally on **every** valuation word $w_T \in \mathbb{Z}_{\ge 1}^T$.

**Lemma 2.1 (Global First-Merger Injectivity).** Fix any $w_T = (e_1, \dots, e_T) \in \mathbb{Z}_{\ge 1}^T$. Suppose $(t_1, g^{(1)})$ and $(t_2, g^{(2)})$ are two $3$-adically admissible matched-depth first-merger paths ($1 \le t_1, t_2 \le T$, $g_1^{(1)} \neq e_{t_1}$, $g_1^{(2)} \neq e_{t_2}$) whose step-$0$ discrepancy states coincide: $(\delta^{(1)}, c^{(1)}) = (\delta^{(2)}, c^{(2)}) = (\delta, c) \in \mathbb{Z} \times \mathbb{Z}[1/2]$. Then $t_1 = t_2$ and $g^{(1)} = g^{(2)}$.

**Proof.** By (2.1) and the $0$–$1$ cylinder law ([18], Equation (2.2)), for every integer $q \ge 0$, every intermediate pullback $y'_s(q)$ along an admissible path $(t_i, g^{(i)})$ ($i \in \{1, 2\}$) is a positive **odd** integer satisfying $U(y'_s(q)) = y'_{s - 1}(q)$ with exact forward valuation $v_2(3 y'_s(q) + 1) = g_s^{(i)}$, ending at the common odd integer $z(q) := 2^\delta n(q) + c = y'_{t_1}^{(1)}(q) = y'_{t_2}^{(2)}(q) \in \mathbb{N}_{\mathrm{odd}}$. Consequently, for every $q \ge 0$, the deterministic forward Syracuse orbit of $z(q)$ satisfies $w_{t_1}(z(q)) = (g_{t_1}^{(1)}, \dots, g_1^{(1)})$ with $U^{t_1}(z(q)) = U^{t_1}(n(q))$, and $w_{t_2}(z(q)) = (g_{t_2}^{(2)}, \dots, g_1^{(2)})$ with $U^{t_2}(z(q)) = U^{t_2}(n(q))$. If $t_1 < t_2$, applying $U^{t_2 - t_1}$ to $U^{t_1}(z(q)) = U^{t_1}(n(q))$ shows that from step $t_1 + 1$ onward the forward orbit of $z(q)$ coincides step-by-step with the trunk orbit of $n(q)$, forcing the $t_2$-th forward valuation of $z(q)$ to equal $e_{t_2}$—contradicting $g_1^{(2)} \neq e_{t_2}$. Hence $t_1 = t_2 =: t$, and uniqueness of $w_t(z(q))$ forces $g^{(1)} = g^{(2)}$. $\blacksquare$

### 2.3 Garden-of-Eden Self-Loops, Constructive Witnesses $\underline{\mathcal{R}}$, and Upper Enclosures $\overline{\mathcal{R}}$

On any $\mathcal{C}_5^+$-preserving generator set $\mathcal{G} \subset \mathbb{Z}_{\ge 1}^+$, each $G \in \mathcal{G}$ induces via (2.2)–(2.3) an internal birth set $\mathcal{B}_G \subset \mathcal{C}_5^+ \setminus \{(0, 0)\}$ (pulling back $(0, 0)$ splits inside $G$ to the left boundary of $G$) and a set-valued backward transfer map $\mathcal{T}_G : \mathcal{C}_5^+ \setminus \{(0, 0)\} \to 2^{\mathcal{C}_5^+ \setminus \{(0, 0)\}}$. The **exact reachable cone set** across $\langle \mathcal{G} \rangle^*$ is

$$
\mathcal{R}(\mathcal{G}) := \bigcup_{k \ge 1} \bigcup_{G_1, \dots, G_k \in \mathcal{G}} (\mathcal{T}_{G_1} \circ \dots \circ \mathcal{T}_{G_{k-1}})(\mathcal{B}_{G_k}) \subseteq \mathcal{C}_5^+ \setminus \{(0, 0)\}.
$$

Because $\mathcal{B}_G$ and $\mathcal{C}_5^+$ are infinite, truncating a breadth-first search at a finite discrepancy cutoff $\Delta_{\mathrm{top}} \ge 1$ requires separating **constructive lower bounds** from **certified upper enclosures**:
- **Constructive witness lower bound $\underline{\mathcal{R}}^{(\Delta_{\mathrm{top}})}(\mathcal{G})$:** Seeding BFS solely with genuine internal births $\bigcup_{G \in \mathcal{G}} (\mathcal{B}_G \cap \{\delta \le \Delta_{\mathrm{top}}\})$ and iterating $\mathcal{T}_G$ restricted to $\{\delta \le \Delta_{\mathrm{top}}\}$ equips every discovered state with an explicit finite generator chain from $(0, 0)$, certifying $\underline{\mathcal{R}}^{(\Delta_{\mathrm{top}})}(\mathcal{G}) \subseteq \mathcal{R}_{\le \Delta_{\mathrm{top}}}(\mathcal{G})$.
- **Certified overflow-band upper enclosure $\overline{\mathcal{R}}^{(\Delta_{\mathrm{top}})}(\mathcal{G})$:** Because a single generator $G$ decreases $\delta$ by at most $\mathrm{drop}(G) := \sum_{x \in G}(x - 1)$, any trajectory in $\mathcal{C}_5^+ \setminus \{(0, 0)\}$ entering $\{\delta \le \Delta_{\mathrm{top}}\}$ from $\{\delta > \Delta_{\mathrm{top}}\}$ must step across some $G \in \mathcal{G}$ from the finite overflow band $\Delta_{\mathrm{top}} + 1 \le \delta_{\mathrm{hi}} \le \Delta_{\mathrm{top}} + \mathrm{drop}(G)$. Seeding BFS with $\bigcup_{G \in \mathcal{G}} (\mathcal{B}_G \cap \{\delta \le \Delta_{\mathrm{top}}\})$ *together with* $\bigcup_{G \in \mathcal{G}} \mathcal{T}_G(\mathcal{C}_5^+ \cap \{\Delta_{\mathrm{top}} + 1 \le \delta \le \Delta_{\mathrm{top}} + \mathrm{drop}(G)\})$ (and, for infinite generator families factored through $(1)^6$, adding $\mathcal{T}_{(1)^6}(\mathcal{C}_5^+ \cap \{\delta \le \Delta_{\mathrm{top}}\})$) encloses all reachable states up to $\Delta_{\mathrm{top}}$:

$$
\underline{\mathcal{R}}^{(\Delta_{\mathrm{top}})}_{\le \Delta_{\mathrm{cap}}}(\mathcal{G}) \subseteq \mathcal{R}_{\le \Delta_{\mathrm{cap}}}(\mathcal{G}) \subseteq \overline{\mathcal{R}}^{(\Delta_{\mathrm{top}})}_{\le \Delta_{\mathrm{cap}}}(\mathcal{G}) \qquad (\Delta_{\mathrm{cap}} \le \Delta_{\mathrm{top}}). \tag{2.4}
$$

Whenever $\underline{\mathcal{R}}^{(\Delta_{\mathrm{top}})}_{\le \Delta_{\mathrm{cap}}}(\mathcal{G}) = \overline{\mathcal{R}}^{(\Delta_{\mathrm{top}})}_{\le \Delta_{\mathrm{cap}}}(\mathcal{G})$, the sandwich (2.4) proves **exactness** on $1 \le \delta \le \Delta_{\mathrm{cap}}$; even when strict inclusion holds, $\overline{\mathcal{R}}^{(\Delta_{\mathrm{top}})}$ remains a $100\%$ rigorous upper enclosure for bounding paid $3$-adic measure from above in Theorem 2.

**Lemma 2.2 (Garden-of-Eden Self-Loops at $\delta = 1$ on $\langle (1), (1, 2) \rangle^*$).** Under $\mathcal{G}_{\mathrm{Fib}} = \{(1), (1, 2)\}$ acting on $\mathcal{C}_5^+ \setminus \{(0, 0)\}$, the states $(1, 3)$ and $(1, 5)$ have **no** predecessors in $\mathcal{B}_{(1)} \cup \mathcal{B}_{(1, 2)}$ and satisfy

$$
\left\{(\tilde{G}, \delta_{\mathrm{in}}, c_{\mathrm{in}}) \in \mathcal{G}_{\mathrm{Fib}} \times (\mathcal{C}_5^+ \setminus \{(0, 0)\}) : (1, c) \in \mathcal{T}_{\tilde{G}}(\delta_{\mathrm{in}}, c_{\mathrm{in}})\right\} = \big\{((1, 2), 1, c)\big\} \qquad (c \in \{3, 5\}).
$$

Hence $(1, 3)$ and $(1, 5)$ are unreachable **Garden-of-Eden self-loops**, and $(1, 1)$ ($z = 2n + 1$) is the unique reachable state at $\delta = 1$ across $\langle (1), (1, 2) \rangle^*$.

**Proof.** Across $\tilde{G} \in \{(1), (1, 2)\}$, $\mathrm{drop}(\tilde{G})$ equals $0$ on $(1)$ and $1$ on $(1, 2)$, so $\delta_{\mathrm{out}} = 1$ can arise only from an internal birth or from $\delta_{\mathrm{in}} \in \{1, 2\}$.
1. *Internal births:* On $(1)$, $g_1 \in \{3, 5, \dots\}$ gives $\delta_{\mathrm{out}} = g_1 - 1 \ge 2$ ($g_1 = 3 \implies (2, 1)$). On $(1, 2)$, splitting at $e_1 = 1$ gives $\delta_{\mathrm{out}} \ge 2$; splitting at $e_2 = 2$ requires even $g_1 \neq 2$, so $g_1 \ge 4$, $\delta_1 = g_1 - 2 \ge 2$, and pulling across $e_1 = 1$ yields $\delta_{\mathrm{out}} \ge 2$ ($g_1 = 4$ gives $(2, 1)$ after $e_2 = 2$, where $\varpi_2 = (2^1 + 1) \bmod 3 = 0$ dies modulo $3$). Thus zero internal births reach $\delta_{\mathrm{out}} = 1$.
2. *Transfer from $\delta_{\mathrm{in}} \in \{1, 2\}$:* Across $\tilde{G} = (1)$, $\delta_{\mathrm{out}} = 1$ forces $\delta_{\mathrm{in}} = 1, g_1 = 1$, requiring $\varpi_1 = (1 + c_{\mathrm{in}}) \bmod 3 = 2 \iff c_{\mathrm{in}} \in \{1, 3, 5\} \cap (1 + 3\mathbb{Z}) = \{1\}$, mapping $(1, 1) \mapsto (1, 1)$. Across $\tilde{G} = (1, 2)$, step $1$ sits at $e_2 = 2$ and step $2$ sits at $e_1 = 1$:
   - From $\delta_{\mathrm{in}} = 1, c_{\mathrm{in}} \in \{1, 3, 5\}$, reaching $\delta_{\mathrm{out}} = 1$ requires $(g_1, g_2) \in \{(1, 2), (2, 1)\}$. At $c_{\mathrm{in}} = 1$, $\varpi_1 = (2^{-1} + 1) \bmod 3 = 0$ dies; at $c_{\mathrm{in}} = 3$, $\varpi_1 = 2 \implies g_1 = 1 \implies (0, 2)$, then $\varpi_2 = (2^{-1} + 2) \bmod 3 = 1 \implies g_2 = 2 \implies (1, 3)$; at $c_{\mathrm{in}} = 5$, $\varpi_1 = 1 \implies g_1 = 2 \implies (1, 7)$, then $\varpi_2 = (1 + 7) \bmod 3 = 2 \implies g_2 = 1 \implies (1, 5)$.
   - From $\delta_{\mathrm{in}} = 2, c_{\mathrm{in}} \in \{1, 3, \dots, 15\}$, reaching $\delta_{\mathrm{out}} = 1$ forces $g_1 = g_2 = 1$: $\varpi_1 = (1 + c_{\mathrm{in}}) \bmod 3 = 2 \implies c_{\mathrm{in}} \in \{1, 7, 13\} \mapsto (\delta_1, c_1) \in \{(1, 1), (1, 5), (1, 9)\}$; then $\varpi_2 = (1 + c_1) \bmod 3 = 2$ selects $c_1 = 1 \mapsto (1, 1)$.

Thus $(1, 1)$ is constructively reached along $(1, 2) \cdot (1)$ via $(0, 0) \xrightarrow{(1)} (2, 1) \xrightarrow{(1, 2)} (1, 1)$, whereas $\{(1, 3), (1, 5)\}$ is completely disconnected from $\{(0, 0)\} \cup (\mathcal{C}_5^+ \setminus \{(1, 3), (1, 5)\})$. $\blacksquare$

| Discrepancy $\delta$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | Total ($\delta \le 8$ / $\delta \le 9$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Ambient cone $\|\mathcal{C}_5^+(\delta)\|$ | $3$ | $8$ | $18$ | $38$ | $78$ | $158$ | $318$ | $638$ | $1{,}278$ | $1{,}259$ / $2{,}537$ |
| **Exact** $\langle(1),(1,2)\rangle^*$ cone $\|\underline{\mathcal{R}}^{(14)}(\delta)\| = \|\overline{\mathcal{R}}^{(14)}(\delta)\|$ | **$1$** | **$1$** | **$1$** | $3$ | $11$ | $23$ | $64$ | $169$ | $411$ | $273$ / **$684$** |
| $(\mathcal{M}_\infty^\star)^*$ witness lower bound $\|\underline{\mathcal{R}}^{(10)}(\delta)\|$ | **$1$** | $1$ | $1$ | $4$ | $15$ | $35$ | $87$ | $206$ | — | $350$ / — |
| $(\mathcal{M}_\infty^\star)^*$ **upper enclosure** $\|\overline{\mathcal{R}}^{(10)}(\delta)\|$ | **$1$** | $2$ | $7$ | $19$ | $47$ | $97$ | $194$ | $408$ | — | **$775$** / — |

*Table 1: Constructive witness lower bounds $\underline{\mathcal{R}}$ and certified overflow-band upper enclosures $\overline{\mathcal{R}}$ inside $\mathcal{C}_5^+ \setminus \{(0, 0)\}$ (Figure 1(a)). On $\langle(1),(1,2)\rangle^*$, $\underline{\mathcal{R}}^{(14)}$ and $\overline{\mathcal{R}}^{(14)}$ coincide identically across all $1 \le \delta \le 9$ ($684 / 2{,}537$ states, eliminating $73.0\%$ of $\mathcal{C}_5^+$, with exact singletons $(1, 1), (2, 1), (3, 5)$ at $\delta = 1, 2, 3$ and $\{5, 17, 23\}$ at $\delta = 4$). On $(\mathcal{M}_\infty^\star)^*$, $\underline{\mathcal{R}}^{(10)}$ and $\overline{\mathcal{R}}^{(10)}$ match at $\delta = 1$ ($\{(1, 1)\}$) and certify $350 \le |\mathcal{R}_{\le 8}((\mathcal{M}_\infty^\star)^*)| \le 775$.*

**Proof of Theorem 1.** Part (1) is Lemma 2.1. For Part (2), increasing the overflow-band cutoff $\Delta_{\mathrm{top}} \in \{11, 12, 13, 14\}$ on $\mathcal{G}_{\mathrm{Fib}} = \{(1), (1, 2)\}$ tightens the upper enclosure size $|\overline{\mathcal{R}}^{(\Delta_{\mathrm{top}})}_{\le 9}(\mathcal{G}_{\mathrm{Fib}})|$ monotonically through $702 \to 695 \to 686 \to 684$; at $\Delta_{\mathrm{top}} = 14$, $\overline{\mathcal{R}}^{(14)}_{\le 9}(\mathcal{G}_{\mathrm{Fib}})$ equals the constructive births-only set $\underline{\mathcal{R}}^{(14)}_{\le 9}(\mathcal{G}_{\mathrm{Fib}})$ element-for-element ($684$ states; Table 1), proving exactness on $1 \le \delta \le 9$ by (2.4) (with explicit witness chains such as $(3, 5)$ via $(1, 2) \cdot (1)$). For Part (3), every generator $B_d^\star$ ($d \ge 5$) of $\mathcal{M}_\infty^\star$ factors as $B_d^\star = (1)^6 \cdot \widetilde{B}_d$ where $\widetilde{B}_d$ maps $\{(0, 0)\} \cup (\mathcal{C}_5^+ \setminus \{(0, 0)\})$ into $\mathcal{C}_5^+ \setminus \{(0, 0)\}$ ([18], Table 3 for $5 \le d \le 10$ and Lemmas 4.3–4.4 for $d \ge 11$, since $s_{d, 2} = \lceil 171(d + 2)/100 \rceil \ge 23 \ge 6$). Since $\mathrm{drop}((1)^6) = 0$, every output of $\mathcal{B}_{B_d^\star} \cup \mathcal{T}_{B_d^\star}(\mathcal{C}_5^+ \setminus \{(0, 0)\})$ at $\delta \le \Delta_{\mathrm{top}}$ either originates from a birth inside $(1)^6$ (covered by $\mathcal{B}_{(1)}$ and $\mathcal{T}_{(1)}$) or lies in $\mathcal{T}_{(1)^6}(\mathcal{C}_5^+ \cap \{\delta \le \Delta_{\mathrm{top}}\})$. Closing $\{(1), (1, 2), B_3^+, B_4\}$ at $\Delta_{\mathrm{top}} = 10$ from their births, overflow bands $11 \le \delta \le 10 + \mathrm{drop}(\tilde{G})$ (up to $\delta = 14$ on $B_4$), and $\mathcal{T}_{(1)^6}(\mathcal{C}_5^+(\delta \le 10))$ yields the certified upper enclosure $\overline{\mathcal{R}}^{(10)}_{\le 8}$ of $775$ states alongside the $350$-state constructive lower bound $\underline{\mathcal{R}}^{(10)}_{\le 8}$ on $\langle(1), (1, 2), B_3^+, B_4\rangle^*$, matching at $\mathcal{R}_1 = \{(1, 1)\}$. $\blacksquare$

---

## 3. All-Horizon, All-Depth Post-Climb $3$-Adic Persistence

### 3.1 Union-Bound Tree Majorants, [14]'s Harmonic Supersolution, and $G_r(\delta)$

By Lemma 2.1, matched-depth first-merger paths along $w_T$ land on pairwise distinct odd affine partners $z(n) = 2^\delta n + c$. Fix $\delta \in \mathbb{Z}_{\ge 0}$ and consider the deeper inverse process ($u \ge 1$) starting from $(m, S_0, y^{(0)}) = (0, \delta, z)$ with $z \in \mathbb{Z}_3$: at depth $m \ge 1$, given $y^{(m-1)} \not\equiv 0 \pmod 3$, admissible $f_m \ge 1$ satisfy $2^{f_m} y^{(m-1)} \equiv 1 \pmod 3$, updating $S_m = S_{m-1} + f_m$ and $y^{(m)} = (2^{f_m} y^{(m-1)} - 1) / 3 \in \mathbb{Z}_3$, and halting as **minimal paying** at the first step $u \ge 1$ where $2^{S_u} < 3^u$ (i.e., $2^{S_j} > 3^j$ for $1 \le j < u$ and $2^{S_u} < 3^u$). Every paying trajectory has a unique minimal-paying prefix, so the paid subset of $z \in \mathbb{Z}_3$ equals the union of legality cylinders over minimal-paying tuples $f = (f_1, \dots, f_u)$. Note carefully that because the backward inverse tree branches across infinitely many exponents of the same parity, minimal-paying legality cylinders **overlap** rather than partitioning the paid set (for example, at $\delta = 0$ on $2 + 3\mathbb{Z}_3$, both $f = (1)$ and $f' = (3, 1, 1, 1)$ are minimal-paying, and the mod-$3^4$ legality cylinder of $(3, 1, 1, 1)$ lies strictly inside $2 + 3\mathbb{Z}_3$ where $(1)$ already pays). Consequently, summing branch measures over minimal-paying tuples gives a rigorous **first-moment union-bound upper majorant** on paid $3$-adic measure—which is the exact inequality direction required for unpaid lower bounds.

For any fixed $r \in \{1, 2\}$ and admissible $f_1$ ($f_1$ even if $r = 1$; $f_1$ odd if $r = 2$), writing $z = r + 3\xi$ with $\xi$ Haar-uniform on $\mathbb{Z}_3$ gives $y^{(1)} = \frac{2^{f_1} r - 1}{3} + 2^{f_1} \xi$, which is Haar-uniform on $\mathbb{Z}_3$ since $\gcd(2^{f_1}, 3) = 1$. Inductively, for every fixed tuple $(f_1, \dots, f_m)$ ($m \ge 1$) with $2^{f_1} r \equiv 1 \pmod 3$, the legality cylinder $\{y^{(1)}, \dots, y^{(m)} \in \mathbb{Z}_3\}$ inside $r + 3\mathbb{Z}_3$ has conditional Haar measure $3^{-(m - 1)}$, with $y^{(m)}$ Haar-uniform on $\mathbb{Z}_3$. To close all depths $u \to \infty$ in exact rational arithmetic, we adapt the $4^{-D}$ harmonic supersolution and first-passage summation of `collatz_100` v2 ([14], Lemma 3.1, rooted in $3^{\lambda - 1} = 2^\lambda - 1$ at $\lambda = 2$) into coset-conditioned tables $G_r(\delta)$ for $r \in \{0, 1, 2\}$.

**Lemma 3.1 (Harmonic Supersolution [14] and Coset-Conditioned Union-Bound Tables $G_r(\delta)$).** For $m \ge 0$ and $S \in \mathbb{Z}$, let $P_{\mathbb{Z}_3}(m, S)$ be the $\mathbb{Z}_3$-Haar measure of $y^{(m)}$ admitting a deeper completion $(f_{m+1}, \dots, f_u)$ ($u > m$) achieving $2^{S_u} < 3^u$, and for $r \in \{0, 1, 2\}$ let $G_r(\delta)$ be the conditional Haar measure inside $r + 3\mathbb{Z}_3$ of $z$ admitting a paying tuple $f \in \mathbb{Z}_{\ge 1}^u$ ($u \ge 1$) from $\delta \ge 0$.
1. *(Unconditioned harmonic bound; cf. [14], Lemma 3.1)* For every $m \ge 0$ and $S \in \mathbb{Z}$,

   $$
   P_{\mathbb{Z}_3}(m, S) \le 9^m \cdot 4^{-S}. \tag{3.1}
   $$

2. *(Coset-conditioned closed-form bounds)* For every $\delta \ge 0$,

   $$
   G_0(\delta) = 0, \qquad G_1(\delta) \le \frac{3}{5} \cdot 4^{-\delta}, \qquad G_2(\delta) \le \min\left(1,\; \frac{12}{5} \cdot 4^{-\delta}\right). \tag{3.2}
   $$

3. *(First-moment DP + tail majorant)* Fix $L_{\mathrm{dp}} \ge 1$ and $M_{\mathrm{prune}} \ge 2$. Tracking non-paying survivor path counts $\mathrm{cnt}_m(S)$ at depths $1 \le m \le L_{\mathrm{dp}}$ (accumulating first-moment union-bound weights $\mathrm{cnt}_{m-1}(S_{\mathrm{prev}}) / 3^{m - 1}$ whenever $2^{S_{\mathrm{new}}} < 3^m$), pruning step-$1$ parity-$2$ tails $S_1 \ge S_{1,\mathrm{cut}}$ with $2^{S_{1,\mathrm{cut}} - M_{\mathrm{prune}}} > 3$ via $\frac{48}{5} \cdot 4^{-S_{1,\mathrm{cut}}}$, pruning step-$m$ ($m \ge 2$) tails $S_{\mathrm{new}} \ge S_{\mathrm{cut}}$ with $2^{S_{\mathrm{cut}} - M_{\mathrm{prune}}} > 3^m$ via $\mathrm{cnt}_{m-1}(S_{\mathrm{prev}}) \cdot 4 \cdot 3^m \cdot 4^{-S_{\mathrm{cut}}}$, and bounding depth-$L_{\mathrm{dp}}$ survivors by $\sum_S \mathrm{cnt}_{L_{\mathrm{dp}}}(S) \cdot 3 \cdot 3^{L_{\mathrm{dp}}} \cdot 4^{-S}$ yields a rigorous rational upper bound on $G_r(\delta)$ across **all** $u \in \mathbb{Z}_{\ge 1}$, giving $G_1(0) \le 0.45315825$ at $(L_{\mathrm{dp}}, M_{\mathrm{prune}}) = (32, 11)$.

**Proof.**
**(1)** Following [14], Lemma 3.1, fix $U \ge m$ and let $P_{\mathbb{Z}_3}^{(U)}(m, S)$ denote the measure of hitting $2^{S_u} < 3^u$ for some $m < u \le U$. At $U = m$, $P_{\mathbb{Z}_3}^{(m)}(m, S) = 0 \le 9^m \cdot 4^{-S}$. For $U > m$, each $f \ge 1$ is admissible on one nonzero mod-$3$ coset of measure $1/3$, mapping $y^{(m)}$ to a Haar-uniform $y^{(m+1)} \in \mathbb{Z}_3$. Either $2^{S + f} < 3^{m+1}$ (so $1 < 9^{m+1} \cdot 4^{-(S + f)}$) or induction gives $P_{\mathbb{Z}_3}^{(U)}(m + 1, S + f) \le 9^{m + 1} \cdot 4^{-(S + f)}$. By the union bound over $f \ge 1$, $P_{\mathbb{Z}_3}^{(U)}(m, S) \le \sum_{f=1}^\infty \frac{1}{3} \cdot 9^{m+1} \cdot 4^{-(S + f)} = 9^m \cdot 4^{-S}$, and $U \to \infty$ gives (3.1).

**(2)** On $0 + 3\mathbb{Z}_3$, $2^{f_1} \cdot 0 \not\equiv 1 \pmod 3$, so $G_0(\delta) = 0$. On $1 + 3\mathbb{Z}_3$, admissible $f_1 = 2k$ ($k \ge 1$) have $\delta + 2k \ge 2$ ($2^{\delta + 2k} > 3$), so the union bound and (3.1) give $G_1(\delta) \le \sum_{k=1}^\infty 9 \cdot 4^{-(\delta + 2k)} = \frac{3}{5} \cdot 4^{-\delta}$. On $2 + 3\mathbb{Z}_3$, summing $9 \cdot 4^{-(\delta + 2k + 1)}$ over $k \ge 0$ gives $G_2(\delta) \le \frac{12}{5} \cdot 4^{-\delta}$.

**(3)** By the union bound over minimal-paying prefixes, each minimal-paying hit at step $m$ contributes at most $\mathrm{cnt}_{m-1}(S_{\mathrm{prev}}) / 3^{m-1}$. Summing $9 \cdot 4^{-(\delta + f_1)}$ over $f_1 = f_{1,\mathrm{cut}} + 2k$ ($k \ge 0$) gives $\frac{48}{5} \cdot 4^{-S_{1,\mathrm{cut}}}$; at step $m \ge 2$, summing $\frac{\mathrm{cnt}_{m-1}}{3^{m-1}} \cdot 9^m \cdot 4^{-(S_{\mathrm{prev}} + f_m)}$ over $f_m \ge f_{\mathrm{cut}}$ gives $\mathrm{cnt}_{m-1} \cdot 4 \cdot 3^m \cdot 4^{-S_{\mathrm{cut}}}$; and at depth $L_{\mathrm{dp}}$, $\frac{\mathrm{cnt}_{L_{\mathrm{dp}}}(S)}{3^{L_{\mathrm{dp}} - 1}} \cdot 9^{L_{\mathrm{dp}}} \cdot 4^{-S} = \mathrm{cnt}_{L_{\mathrm{dp}}}(S) \cdot 3 \cdot 3^{L_{\mathrm{dp}}} \cdot 4^{-S}$. $\blacksquare$

### 3.2 Residue-Quotiented Prefix Transfer and Multi-Scale Cone Equidistribution

Given an infinite word $w = p \cdot w_{\mathrm{rem}}$ with prefix $p = (e_1, \dots, e_L) \in \mathbb{Z}_{\ge 1}^L$ ($S_L = \|p\|$), write $q = q_0 + 3\tilde{q}$ where $n(q_0) \equiv a \pmod 3$ ($a \in \{0, 1, 2\}$) and $\tilde{q}$ is Haar-uniform on $\mathbb{Z}_3$. Any step-$0$ partner $z(n) = 2^{d_{\mathrm{end}}} n + c_{\mathrm{end}}$ ($d_{\mathrm{end}} \ge 1$, $c_{\mathrm{end}}$ odd) lies on the fixed coset $r(a, z(n_0) \bmod 3, d_{\mathrm{end}}) := (z(n_0) + 2^{d_{\mathrm{end}}}(a - n_0)) \bmod 3$ and ranges Haar-uniformly over $r + 3\mathbb{Z}_3$ because $\gcd(2^{d_{\mathrm{end}} + S_L + 1}, 3) = 1$, so its conditional paid measure inside $n \equiv a \pmod 3$ is at most $G_r(d_{\mathrm{end}})$.

**Lemma 3.2 (Mod-$3^{r_{\mathrm{rem}} + 1}$ Residue Quotienting and Outgoing Tail Bound).** Along $r_{\mathrm{rem}}$ remaining backward steps with reverse trunk valuations $(\gamma_1, \dots, \gamma_{r_{\mathrm{rem}}})$, pullback states $(y, d)$ with identical $(y \bmod 3^{r_{\mathrm{rem}} + 1},\; d)$ have identical $3$-adic admissibility at all remaining steps and identical final $y_{\mathrm{end}} \bmod 3$. At step $j \in \{1, \dots, r_{\mathrm{rem}}\}$, summing admissible outgoing exponents $g_j \in \{g_{\mathrm{cut}}, g_{\mathrm{cut}} + 2, \dots\}$ ($d_n := d + g_{\mathrm{cut}} - \gamma_j \ge 1$) across the remaining steps contributes at most $\frac{12}{5} (\frac{16}{15})^{r_{\mathrm{rem}} - j + 1} \cdot 4^{\sum_{i = j + 1}^{r_{\mathrm{rem}}} (\gamma_i - 1)} \cdot 4^{-d_n}$.

**Proof.** Each division by $3$ in $I_g(y) = (2^g y - 1)/3$ consumes one $3$-adic digit, so $y \bmod 3^{r_{\mathrm{rem}} + 1}$ determines all subsequent mod-$3$ residues through $y_{\mathrm{end}} \bmod 3$. Backward induction over $i = r_{\mathrm{rem}}, \dots, j + 1$ using $G_r(d_{\mathrm{end}}) \le \frac{12}{5} \cdot 4^{-d_{\mathrm{end}}}$ multiplies by $4^{\gamma_i - 1} \sum_{k=0}^\infty 16^{-k} = \frac{16}{15} \cdot 4^{\gamma_i - 1}$ per step, and summing $g_j = g_{\mathrm{cut}} + 2k$ ($k \ge 0$) adds one final factor $\frac{16}{15}$. $\blacksquare$

Unlike pure climbs $1^L$ ($4^{S_L} = 4^L < 9^L$), post-climb prefixes $p$ often have $4^{S_L} \gg 9^L$, so naive counting of $\sim \frac{5}{2} 2^d$ incoming cone states at $x_L$ diverges unless filtered modulo $3^m$:

**Lemma 3.3 (Multi-Scale Suffix Equidistribution Tail Bound).** Fix $p = (e_1, \dots, e_L) \in \mathbb{Z}_{\ge 1}^L$ ($S_L = \|p\|$) and $\Delta_{\mathrm{asymp}} \ge \Delta_{\mathrm{cone}} + 1$. Across all $(d, c_{\mathrm{in}}) \in \mathcal{C}_5^+$ with $d > \Delta_{\mathrm{cone}}$ at $x_L$, total conditional paid measure on any coset $n \equiv a \pmod 3$ is bounded above by

$$
\sum_{d = \Delta_{\mathrm{cone}} + 1}^{\Delta_{\mathrm{asymp}}} \min_{0 \le m \le L} \frac{12}{5} 4^{S_L} \left(\frac{4}{15}\right)^{L - m} \left(\frac{5}{2 \cdot 9^m} 2^{-d} + \frac{1}{3^m} 4^{-d}\right) + \frac{12}{5}\left(\frac{5}{2} \frac{4^{S_L}}{9^L} 2^{-\Delta_{\mathrm{asymp}}} + \frac{4^{S_L}}{3^{L + 1}} 4^{-\Delta_{\mathrm{asymp}}}\right). \tag{3.3}
$$

**Proof.** Fix $d \ge 1$ and $0 \le m \le L$. There are $N_d = \frac{5(2^d - 1) + 1}{2} < \frac{5}{2} 2^d$ odd integers $c_{\mathrm{in}} \in [1, 5(2^d - 1)]$, and consecutive odd integers congruent modulo $3^m$ differ by $2 \cdot 3^m$, so any mod-$3^m$ class holds at most $\lceil N_d / 3^m \rceil < \frac{5}{2 \cdot 3^m} 2^d + 1$ offsets $c_{\mathrm{in}}$. Along any fixed first-$m$ backward tuple $(g_1, \dots, g_m) \in \mathbb{Z}_{\ge 1}^m$ from $x_L$, $3$-adic integrality $2^{g_1 + \dots + g_m}(2^d x_L + c_{\mathrm{in}}) \equiv C_{\mathrm{rev}}(g_1, \dots, g_m) \pmod{3^m}$ selects a **single** mod-$3^m$ residue class of $c_{\mathrm{in}}$ (since $\gcd(2^{\sum g_j}, 3^m) = 1$), leaving $< \frac{5}{2 \cdot 3^m} 2^d + 1$ survivors at discrepancy $d + \sum_{j=1}^m(g_j - \gamma_j)$. Across the remaining $L - m$ steps, each step multiplies $\frac{12}{5} 4^{-d}$ by $\frac{16}{15} 4^{\gamma_i - 1} = \frac{4}{15} 4^{\gamma_i}$, giving $\frac{12}{5} 4^{S_L}(\frac{4}{15})^{L - m} 4^{-d} \prod_{j=1}^m 4^{-g_j}$ per survivor. Summing over $(g_1, \dots, g_m) \in \mathbb{Z}_{\ge 1}^m$ via $\prod_{j=1}^m (\sum_{g_j \ge 1} 4^{-g_j}) = 3^{-m}$, multiplying by $\frac{5}{2 \cdot 3^m} 2^d + 1$, optimizing $0 \le m \le L$ for $\Delta_{\mathrm{cone}} < d \le \Delta_{\mathrm{asymp}}$, and taking $m = L$ for $d > \Delta_{\mathrm{asymp}}$ proves (3.3). $\blacksquare$

### 3.3 Proof of Theorem 2 Across $\langle (1), (1, 2) \rangle^{\mathbb{N}}$ and $(\mathcal{M}_\infty^\star)^{\mathbb{N}}$

To cover intermediate horizons $t$ falling strictly **inside** an arbitrarily long block $B_d^\star$ ($d \ge 3$) of $(\mathcal{M}_\infty^\star)^{\mathbb{N}}$, note from $B_d = (1^s, 2, 1^m, d)$ ($s \ge 4$) that **every proper nonempty prefix of every generator in $\mathcal{M}_\infty$ and $\mathcal{M}_\infty^\star$ has the form $(1^j)$ or $(1^{s-1}) \cdot (1, 2) \cdot (1^r)$, and hence belongs to $\langle (1), (1, 2) \rangle^+ \subset \mathcal{M}_\infty$.** Thus: (i) for every $w \in (\mathcal{M}_\infty^\star)^{\mathbb{N}}$ and $t \ge 1$, $w_t \in \mathcal{M}_\infty$ has zero contracting ancestors at $1 \le r \le t$ ($u = 0$) by [18] Theorem 3, so every paying branch has $u \ge 1$ through a step-$0$ partner $z(n) = 2^{d_{\mathrm{end}}} n + c_{\mathrm{end}}$; and (ii) pulling back across any proper prefix $v \in \langle(1), (1, 2)\rangle^+$ of $G_k$ lands in $\mathcal{R}(\mathcal{G}_{\mathrm{Fib}}) \subseteq \mathcal{R}((\mathcal{M}_\infty^\star)^*) \subseteq \overline{\mathcal{R}}^{(10)}((\mathcal{M}_\infty^\star)^*)$.

| Trajectory Family / Benchmark Word | All-Horizon, All-Depth $\overline{\mathsf{Unpaid}}_{\times}$ ($\mathbb{Z}_3^\times$) | All-Horizon, All-Depth $\overline{\mathsf{Unpaid}}_{3}$ ($3\mathbb{Z}_3$) | Finite-Cutoff $\overline{\mathsf{Unpaid}}_{\times}^{(|w|, 7)}(w)$ | Worst Prefix Class |
| :--- | :---: | :---: | :---: | :---: |
| Pure root $t = 0$ ($w = \emptyset$) | $\ge 0.27342087$ | $1.00000000$ | $445 / 1{,}458 \approx 0.305212$ ($\emptyset,\; T = 0$) | $\emptyset$ |
| Pure climb $1^\infty$ (`collatz_100` v2 [14]) | $> 0.1711$ [14] ($\ge 0.21120232$ here) | $\ge 0.81220858$ | $438 / 1{,}458 \approx 0.300411$ ($(1)^6,\; T = 6$) | $(1)^6$ |
| **Fibonacci subshift $\langle (1), (1, 2) \rangle^{\mathbb{N}}$** | **$\ge 0.21120232$** | **$\ge 0.81220858$** | $437 / 1{,}458 \approx 0.299725$ ($(1, 2)^3,\; T = 6$) | $(1, 2)^3$ |
| **All-$d$ subshift $(\mathcal{M}_\infty^\star)^{\mathbb{N}}$** ($d \in \mathbb{Z}_{\ge 1}$) | **$\ge 0.13959334$** | **$\ge 0.67157696$** | $437 / 1{,}458 \approx 0.299725$ ($B_3^+,\; T = 7$) | $(1, 2)^2$ |

*Table 2: Certified infinite $(t \ge 0, u \ge 1)$ unpaid $3$-adic conditional lower bounds alongside exact finite-cutoff $\overline{\mathsf{Unpaid}}_{\times}^{(|w|, 7)}(w)$ benchmarks ($J = 7$, consistent with (1.2)).*

**Proof of Theorem 2.** On $2 + 3\mathbb{Z}_3$, $t = 0, f_1 = 1$ gives $I_1(n) = (2n - 1)/3 < n$, paying $100\%$. On $1 + 3\mathbb{Z}_3$ and $3\mathbb{Z}_3$, given a finite prefix $p$ of $w$, total conditional paid share across all $t \ge 0, u \ge 1$ is bounded via the union bound over: (0) $t = 0$ ($G_1(0) \le 0.45315825$ on $1 + 3\mathbb{Z}_3$, $G_0(0) = 0$ on $3\mathbb{Z}_3$); (I) internal births at $1 \le t \le |p|$ via Lemma 3.2; and (II) external first-merger paths at all $t > |p|$, which by Lemma 2.1 inject into distinct incoming cone states $(d_{\mathrm{in}}, c_{\mathrm{in}})$ at $x_{|p|}$—summed over a certified cone upper enclosure for $1 \le d_{\mathrm{in}} \le \Delta_{\mathrm{cone}}$ via Lemma 3.2 and over all $\mathcal{C}_5^+(d_{\mathrm{in}} > \Delta_{\mathrm{cone}})$ via Lemma 3.3. Then $\overline{\mathsf{Unpaid}}_{\times}(w) \ge \frac{1}{2}(1 - \mathrm{Paid}_{1 + 3\mathbb{Z}_3}(p))$ and $\overline{\mathsf{Unpaid}}_{3}(w) \ge 1 - \mathrm{Paid}_{3\mathbb{Z}_3}(p)$.
- **Part (1):** Every $w \in \langle (1), (1, 2) \rangle^{\mathbb{N}}$ starts with one of $21$ minimal generator-aligned prefixes $p \in \langle (1), (1, 2) \rangle^*$ of length $6 \le |p| \le 7$, with $1 \le d_{\mathrm{in}} \le 9$ restricted to $\overline{\mathcal{R}}^{(14)}_{\le 9}(\mathcal{G}_{\mathrm{Fib}})$ ($684$ states; Theorem 1(2)), certifying $\overline{\mathsf{Unpaid}}_{\times}(w) \ge 0.21120232$ and $\overline{\mathsf{Unpaid}}_{3}(w) \ge 0.81220858$ (worst prefix $(1, 2)^3$).
- **Part (2):** Every $w = G_1 G_2 \cdots \in (\mathcal{M}_\infty^\star)^{\mathbb{N}}$ either: (a) begins with $G_1, \dots, G_m \in \{(1), (1, 2), B_3^+, B_4\}$ reaching $|p| \ge 4$ ($22$ minimal prefixes), restricting $1 \le d_{\mathrm{in}} \le 8$ at $x_{|p|}$ to the upper enclosure $\overline{\mathcal{R}}^{(10)}_{\le 8}$ ($775$ states; Theorem 1(3)) and $d_{\mathrm{in}} = 9$ (when $\mathrm{drop}(p) \ge 4$) to $\mathcal{C}_5^+(9)$; or (b) begins with $u \in \langle(1), (1, 2)\rangle^*$ of length $|u| \le 3$ ($7$ prefixes) followed by $B_d^\star = (1)^6 \cdot \widetilde{B}_d$ ($d \ge 5$), giving $p = u \cdot (1)^6$ enclosed by $\mathcal{C}_5^+ \setminus \{(0, 0)\}$ at $x_{|p|}$. Across all $22 + 7 = 29$ prefixes, $\overline{\mathsf{Unpaid}}_{\times}(w) \ge 0.13959334$ and $\overline{\mathsf{Unpaid}}_{3}(w) \ge 0.67157696$ (worst prefix $(1, 2)^2$). $\blacksquare$

---

## 4. Supercritical Sturmian Collapse Window and Finite-Cutoff Survival

### 4.1 Exact Farey Window $[30/19, 19/12)$ and All-Depth Collapse on $w_{22}$

Pushing average $2$-division slope into $(3/2, \log_2 3]$ introduces adjacent twos $(2, 2)$, as in $W_7 = (1, 2, 1, 2, 1, 2, 2)$ ($11/7$) and $W_{12} = (1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2)$ ($19/12 < \log_2 3$). In [16], Example 1 and Theorem 1 (the gate criterion), `baton_relay` showed that the $23$-letter balanced factor $W_{23} = (2) \cdot w_{22}$ fails binary division-minimality because its $22$-letter suffix $w_{22}$ admits a $c = 4$ merger. Analyzing origin-anchored Sturmian words $W_\alpha$ directly shows that $w_{22}$ occurs as a prefix of $W_\alpha$ precisely on $[30/19, 19/12)$, where it remains matched-depth minimal ($b = n + 4 > n$) yet triggers **all-depth $3$-adic unit collapse** at $u = 1$ ($r = 23$).

**Lemma 4.1 (Exact Farey Interval and Depth-$23$ Unit Collapse on $w_{22}$).** Define the length-$22$, weight-$34$ binary word

$$
w_{22} := W_7^2 W_5 (1, 2, 1) = (1, 2, 1, 2, 1, 2, 2,\; 1, 2, 1, 2, 1, 2, 2,\; 1, 2, 1, 2, 2,\; 1, 2, 1),
$$

whose cylinder $\operatorname{Cyl}(w_{22}) = \{n(q) = n_0 + 2^{35} q : q \ge 0\}$ has $n_0 = 24{,}614{,}951{,}931$ and $U^{22}(n(q)) = y_0 + 2 \cdot 3^{22} q$ with $y_0 = 44{,}962{,}116{,}167$.
1. The lower mechanical Sturmian word $W_\alpha$ ($e_i = \lfloor i\alpha \rfloor - \lfloor (i - 1)\alpha \rfloor$) begins with $w_{22}$ **if and only if** $\alpha \in [30/19, 19/12)$.
2. Across $\operatorname{Cyl}(w_{22})$ ($\forall q \in \mathbb{Z}_{\ge 0}$), $n(q) + 4$ (cf. [16], Example 1) and $2 n(q) + 9$ follow $v^{(0)} := (1^9, 2, 1^2, 4, 1^4, 3, 1, 5, 1, 3)$ ($\|v^{(0)}\| = 34$) and $v^{(1)} := (1^{10}, 3, 1, 4, 1^4, 3, 1, 5, 1, 3)$ ($\|v^{(1)}\| = 35$), merging identically with $n(q)$ at step $22$:

   $$
   U^{22}(n(q) + 4) = U^{22}(2 n(q) + 9) = U^{22}(n(q)) = y_0 + 2 \cdot 3^{22} q \qquad (\forall q \in \mathbb{Z}_{\ge 0}). \tag{4.1}
   $$

3. Consequently, $\overline{\mathsf{Unpaid}}_{\times}^{(22, 1)}(w_{22}) = 0$, and by (1.2) **every** infinite word $w$ starting with $w_{22}$ satisfies $\overline{\mathsf{Unpaid}}_{\times}(w) = 0$.

**Proof.**
**(1)** Writing $S_i = \sum_{j=1}^i e_j(w_{22})$, $\lfloor i\alpha \rfloor = S_i$ holds for all $1 \le i \le 22$ iff $\max_{1 \le i \le 22}(S_i / i) \le \alpha < \min_{1 \le i \le 22}((S_i + 1)/i)$, attaining $S_{19}/19 = 30/19$ at $i = 19$ and $(S_{12} + 1)/12 = 19/12$ at $i = 12$.

**(2)** Since $\operatorname{Cyl}(v^{(0)})$ has modulus $2^{35}$ matching $\operatorname{Cyl}(w_{22})$ and $2 n(q) + 9$ has step $2^{36} = 2^{\|v^{(1)}\| + 1}$, verifying $w_{22}(n_0 + 4) = v^{(0)}$, $w_{22}(2 n_0 + 9) = v^{(1)}$, and $U^{22}(n_0 + 4) = U^{22}(2 n_0 + 9) = y_0$ at $q = 0$ establishes (4.1) for all $q \ge 0$.

**(3)** On $2 + 3\mathbb{Z}_3$, $t = 0, f_1 = 1$ gives $I_1(n) = (2n - 1)/3 < n$. On $1 + 3\mathbb{Z}_3$, $n + 4 \equiv 2 \pmod 3$, so from $z(n) = n + 4$ at $t = 22$, one extra step $f_1 = 1$ ($u = 1$, $2^{0+1} < 3^1$) gives $I_1(n + 4) = (2n + 7)/3 < n$ across $100\%$ of $1 + 3\mathbb{Z}_3$ (and for every $n \in \operatorname{Cyl}(w_{22})$ since $n_0 > 7$). $\blacksquare$

### 4.2 Finite-Cutoff Survival Above $19/12$ and Finite Stopping Certificates for Periodic Ties

On $[19/12, \log_2 3]$, $W_\alpha$ begins with $W_{12}$ rather than $W_7 \cdot (1, 2, 1, 2, 1)$, forbidding $W_7^2$ by Sturmian balance and raising the finite-cutoff statistic $\overline{\mathsf{Unpaid}}_{\times}^{(T, 7)}$ back to $437 / 1{,}458 \approx 0.299725$ on $W_{12}$ ($T = 12$), $W_{12}^3$ ($T = 36$), and $W_{\log_2 3}[:36]$ ($T = 36$). As emphasized in (1.2), $\overline{\mathsf{Unpaid}}_{\times}^{(T, 7)}$ evaluates horizons $0 \le t \le T$ and extra depths $0 \le u \le 7$, so it constitutes **finite-prefix evidence** rather than a proof of $\overline{\mathsf{Unpaid}}_{\times}(W_\alpha) > 0$. What *can* be certified across **all** infinite horizons $t \in \mathbb{Z}_{\ge 1}$ on specific periodic Sturmian words $W_L^\infty$ is the complete absence of $\delta = 0$ translation ties, by adapting the negative rational-cycle candidate method of [11], Theorem 10 into a sound finite-certificate search.

**Lemma 4.2 (Rational Periodic-Point Candidate Bound and Soundness of Finite Stopping Certificates; cf. [11], Theorem 10).** Let $P = (e_1, \dots, e_L) \in \mathbb{Z}_{\ge 1}^L$ be an expanding period ($3^L > 2^S$, $S = \|P\|$), and let $x_0 := -C(P) / (3^L - 2^S) < 0$ and $x_r := U_{\mathbb{Q}}^r(x_0)$ ($0 \le r < L$) be its periodic orbit under $U_{\mathbb{Q}}(y) := (3y + 1) / 2^{v_2(3y + 1)}$ ($v_2(u / D) := v_2(u)$ for odd $D = 3^L - 2^S$).
1. Every orbit point satisfies $x_r < -1/3 < 0$ ($0 \le r < L$), and for every $t \ge 1$ with $w_t := P^\infty[:t]$, $C(w_t) = 3^t(-x_0) - 2^{E_t}(-x_{t \bmod L}) < 3^t(-x_0)$.
2. An even positive translate $b = n + c$ ($c \ge 2$ even) satisfies $U^t(n + c) = U^t(n)$ with $\|w_t(n + c)\| = E_t$ ($\delta = 0$) at horizon $t \ge 1$ on $\operatorname{Cyl}(w_t)$ **if and only if** $2 \le c < -x_0$ and the rational orbit $y_j := U_{\mathbb{Q}}^j(x_0 + c)$ ($f_j := v_2(3 y_{j-1} + 1)$) satisfies $y_t = x_{t \bmod L}$ with $\Delta_t := \sum_{j=1}^t (f_j - e_{(j-1) \bmod L + 1}) = 0$.
3. *(Soundness of finite stopping certificates)* Because a fixed odd denominator $D = 3^L - 2^S$ still permits infinitely many negative numerators, finiteness of the candidate list $2 \le c < -x_0$ does **not** guarantee a priori that every rational orbit $y_j$ terminates in a finite classification (just as noted in [11], Theorem 10). However, **if** for a given candidate $c$ there exists a finite step $j \ge 1$ at which:
   - (a) $y_j = x_{j \bmod L}$ (certifying a $\delta = 0$ merger at $t = j$ if $\Delta_j = 0$, or certifying **no** $\delta = 0$ merger at any $k \ge j$ if $\Delta_j \neq 0$, since $y_k = x_{k \bmod L}$ and $f_k = e_{(k-1) \bmod L + 1}$ force $\Delta_k = \Delta_j \neq 0$ for all $k \ge j$);
   - (b) $y_j > 0$ (certifying $y_k > 0 > x_{k \bmod L}$ for all $k \ge j$); or
   - (c) $(j \bmod L, y_j) = (j' \bmod L, y_{j'})$ for some $0 \le j' < j$ with $y_r \neq x_{r \bmod L}$ for $0 \le r \le j$ (certifying that $(k \bmod L, y_k)$ cycles permanently disjoint from $\{(r, x_r)\}$ for all $k \ge 0$),

   then that finite certificate rigorously classifies **all** horizons $t \in \mathbb{Z}_{\ge 1}$ for offset $c$.

**Proof.**
**(1)** Since $x_L = x_0 < 0$ and $3 x_r + 1 = 2^{e_{r+1}} x_{r+1}$, backward induction gives $x_r < -1/3 < 0$, and $(3^t x_0 + C(w_t)) / 2^{E_t} = x_{t \bmod L} < 0$ gives $C(w_t) < 3^t(-x_0)$.

**(2)** If $U^t(n + c) = U^t(n)$ with $w_t(n + c) = (f_1, \dots, f_t)$ and $\sum_{j=1}^t f_j = E_t$, equating numerators gives $3^t c + C(f_1, \dots, f_t) = C(w_t) < 3^t(-x_0) \implies c < -x_0$. Subtracting $3^t x_0 + C(w_t) = 2^{E_t} x_{t \bmod L}$ from $3^t n + C(w_t) = 2^{E_t} x_t(n)$ in $\mathbb{Z}_2$ (where $x_{t \bmod L}, x_t(n) \in \mathbb{Z}_2^\times$) gives $n + c \equiv x_0 + c \pmod{2^{E_t + 1}}$ in $\mathbb{Z}_2$, so $x_0 + c$ shares valuations $(f_1, \dots, f_t)$ and lands at $y_t = x_{t \bmod L}$ with $\Delta_t = 0$; the converse follows identically modulo $2^{E_t + 1}$.

**(3)** Since $(y_{k+1}, f_{k+1})$ depends deterministically on $y_k$ alone, $y_j = x_{j \bmod L}$ locks $(y_k, f_k) = (x_{k \bmod L}, e_{(k-1) \bmod L + 1})$ and $\Delta_k = \Delta_j$ for all $k \ge j$ (a); $y_j > 0 \implies 3 y_j + 1 > 1 > 0 \implies y_{j+1} > 0$ locks positivity for all $k \ge j$ (b); and a state repeat $(j \bmod L, y_j) = (j' \bmod L, y_{j'})$ locks $(k \bmod L, y_k)$ into a finite cycle already verified disjoint from $\{(r, x_r)\}$ (c). $\blacksquare$

| Reference Word $w$ | Slope $S / L$ | Cutoff $(T, J)$ | Finite $\overline{\mathsf{Unpaid}}_{\times}^{(T, 7)}(w)$ | Finite $\overline{\mathsf{Unpaid}}_{3}^{(T, 7)}(w)$ | Certified All-$t$ $\delta = 0$ Hits on $P^\infty$ (Max Stop Step) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| $W_{32}$ | $50 / 32 = 1.56250$ | $(32, 7)$ | $389 / 1{,}458 \approx 0.266803$ | $662 / 729 \approx 0.908093$ | $\emptyset$ ($c \le 14$, stop $\le 45$) |
| $W_{30}$ | $47 / 30 \approx 1.56667$ | $(30, 7)$ | $389 / 1{,}458 \approx 0.266803$ | $662 / 729 \approx 0.908093$ | $\emptyset$ ($c \le 18$, stop $\le 73$) |
| $W_7$ | $11 / 7 \approx 1.57143$ | $(7, 7)$ | $437 / 1{,}458 \approx 0.299725$ | $672 / 729 \approx 0.921810$ | $\emptyset$ ($c \le 26$, stop $\le 79$) |
| $W_{26}$ | $41 / 26 \approx 1.57692$ | $(26, 7)$ | $429 / 1{,}458 \approx 0.294238$ | $656 / 729 \approx 0.899862$ | $\emptyset$ ($c \le 42$, stop $\le 75$) |
| $W_{19}$ *($L = 19 < 22$)* | $30 / 19 \approx 1.57895$ | $(19, 7)$ | $437 / 1{,}458 \approx 0.299725$ | $664 / 729 \approx 0.910836$ | **$[(4, 22)]$ on $W_{19}^\infty$** ($c \le 58$, stop $\le 32$) |
| **$W_{38} = W_{19}^2$** | $60 / 38 \approx 1.57895$ | $(38, 7)$ | **$0 / 1{,}458$** ($\overline{\mathsf{Unpaid}}_{\times} = 0$) | $395 / 729 \approx 0.541838$ | **$[(4, 22)]$** ($c \le 58$, stop $\le 32$) |
| **$W_{31}$** | $49 / 31 \approx 1.58065$ | $(31, 7)$ | **$0 / 1{,}458$** ($\overline{\mathsf{Unpaid}}_{\times} = 0$) | $395 / 729 \approx 0.541838$ | **$[(4, 22)]$** ($c \le 80$, stop $\le 39$) |
| **$W_{43}$** | $68 / 43 \approx 1.58140$ | $(43, 7)$ | **$0 / 1{,}458$** ($\overline{\mathsf{Unpaid}}_{\times} = 0$) | $395 / 729 \approx 0.541838$ | **$[(4, 22)]$** ($c \le 98$, stop $\le 44$) |
| **$W_{12}$ / $W_{12}^3$** | $19 / 12 \approx 1.58333$ | $(12, 7)$ / $(36, 7)$ | **$437 / 1{,}458 \approx 0.299725$** | $664 / 729$ / $655 / 729$ | **$\emptyset$** ($c \le 218$, stop $\le 50$) |
| **$W_{53}$** *(convergent)* | $84 / 53 \approx 1.58491$ | — | — | — | **$\emptyset$** ($c \le 6{,}142$, stop $\le 164$) |
| **$W_{\log_2 3}[:36]$ / $[:358]$** | $\to \log_2 3 \approx 1.58496$ | $(36, 7)$ | **$437 / 1{,}458 \approx 0.299725$** | $655 / 729 \approx 0.898491$ | $\emptyset$ across $1 \le t \le 358$ |

*Table 3: Supercritical Sturmian Farey profile across $(3/2, \log_2 3]$, explicitly labeling finite-cutoff shares $\overline{\mathsf{Unpaid}}_{\times}^{(T, 7)}(w)$ vs. all-depth collapse $\overline{\mathsf{Unpaid}}_{\times} = 0$ on $[30/19, 19/12)$ and finite stopping-certificate bounds ($\text{stop} \le 164$) for periodic $\delta = 0$ ties (additionally $W_{41}^\infty$, $64/41$, has $\emptyset$ for $c \le 14$ with $\text{stop} \le 150$).*

![Cone sandwiches/enclosures and supercritical Sturmian Farey resonance profile](supplement/figure-1.png)

*Figure 1: (a) Exact cone sandwich $|\underline{\mathcal{R}}^{(14)}| = |\overline{\mathcal{R}}^{(14)}|$ ($684 / 2{,}537$ states) on $\langle(1), (1, 2)\rangle^*$ and certified sandwich $|\underline{\mathcal{R}}^{(10)}| \le |\mathcal{R}| \le |\overline{\mathcal{R}}^{(10)}|$ ($350$ to $775$ of $1{,}259$ states) on $(\mathcal{M}_\infty^\star)^*$. (b) Supercritical Sturmian profile on $(3/2, \log_2 3]$, contrasting all-depth collapse $\overline{\mathsf{Unpaid}}_{\times}(W_\alpha) = 0$ on $[30/19, 19/12)$ with finite-cutoff shares $\overline{\mathsf{Unpaid}}_{\times}^{(T, 7)}(w) = 437 / 1{,}458$ on selected prefixes above $19/12$.*

**Proof of Theorem 3.** Part (1) follows from Lemma 4.1 (matched-depth minimality of $w_{22}$ holds by [16] and is verified directly across $\delta \le 0$ on $\operatorname{Cyl}(w_{22})$, where $(t, c) = (22, 4)$ is the unique $\delta = 0$ partner and $n + 4 > n$). For Part (2), exact mod-$3^7$ sieving certifies $\overline{\mathsf{Unpaid}}_{\times}^{(T, 7)}(w) = 437 / 1{,}458$ on $W_{12}$ ($T = 12$), $W_{12}^3$ ($T = 36$), and $W_{\log_2 3}[:36]$ ($T = 36$), while trunk-independent backward enumeration on $W_{\log_2 3}[:36]$ verifies $\delta_{\mathrm{end}} \ge 1$ on every first-merger rival ($\delta_{\mathrm{end}} = 1$ only at $t = 3, c = 1$). Running the certificate search of Lemma 4.2(3) (with hard cap $10{,}000$ steps; `AssertionError` on non-termination) terminates in $\le 164$ steps for **every** even candidate $2 \le c < -x_0$ across all $10$ tested periods, certifying empty $\delta = 0$ hit sets across all $t \in \mathbb{Z}_{\ge 1}$ on $W_7^\infty, W_{12}^\infty, W_{26}^\infty, W_{30}^\infty, W_{32}^\infty, W_{41}^\infty, W_{53}^\infty$ and unique first hit $[(4, 22)]$ on $W_{19}^\infty, W_{31}^\infty, W_{43}^\infty$. Finally, $W_{53}^\infty[:358] = W_{\log_2 3}[:358]$ ($358 = 306 + 53 - 1$), certifying zero $\delta = 0$ ties on $W_{\log_2 3}$ for $1 \le t \le 358$ (cross-checked directly for $t \le 110$ via $c < t/3 \le 36$). $\blacksquare$

**Remark 4.3 (Connection to `collatz_139` v2 [16]).** On $(11/7, 30/19)$, $W_\alpha$ avoids $w_{22}$ at $k = 0$ ($\overline{\mathsf{Unpaid}}_{\times}^{(26, 7)}(W_{26}) = \overline{\mathsf{Unpaid}}_{\times}^{(35, 7)}(W_7^5) = 429 / 1{,}458$) and realizes [16]'s $W_{23} = (2) \cdot w_{22}$ only at an internal shift $k \ge 6$: at $t = k + 23$, $b_k = (x_k + 5)/2 \equiv 0 \pmod 3$ is a shallower ($v = 23 < t$, $u = 0$) $3$-adic dead end that contracts when $3^k < 2^{E_k + 1}$ (e.g., $W_{26}^2[:29]$ at $k = 6$) and expands when $3^k > 2^{E_k + 1}$. On $[19/12, \log_2 3]$, prepending $(2)$ places $(2) \cdot W_\alpha[:t]$ in $\mathcal{U}$ of [16] Definition 3 (and in $\mathcal{U}(N_0, p_0)$ for $(N_0, p_0) = (13{,}196{,}516,\; 20{,}915{,}983)$ when $\alpha \in [19/12, p_0 / N_0]$), so [16] Theorems 1, 2, and 5 exclude $c_0 \equiv 4 \pmod 6$ ties via external $10^{11}$-state C certificates up to $t \le 114{,}186{,}137{,}063$ at $\log_2 3$, whereas Lemma 4.2 and Theorem 3(2) give self-contained certificates excluding **all** even offsets $c \equiv 0, 2, 4 \pmod 6$ across $W_7^\infty, W_{12}^\infty, \dots, W_{53}^\infty$ and $W_{\log_2 3}[:358]$.

---

## 5. Dual $2$-Adic Cylinder Haar Survival Separation and Coalescence Escape

### 5.1 Cramér Survival Rate of $\mathcal{N}_T$ vs. Shielded Monoid $2$-Adic Exponents

Theorem 2 shows that shielded post-climb languages $\langle(1), (1, 2)\rangle^{\mathbb{N}}$ and $(\mathcal{M}_\infty^\star)^{\mathbb{N}}$ retain a positive $3$-adic Haar share unpaid across all horizons and depths. Under normalized $2$-adic cylinder Haar measure $\mu_2(\operatorname{Cyl}(w)) = 2^{-\|w\|}$ on $\mathbb{Z}_2^\times$, independent $\mathrm{Geom}(1/2)$ valuations $\mathbb{P}(e_i = k) = 2^{-k}$ realize $\mu_2(\operatorname{Cyl}(w)) = \prod_{i=1}^T 2^{-e_i}$, so $\mu_2(\mathcal{N}_T) = \mathbb{P}(\forall 1 \le i \le T,\; E_i < i \log_2 3)$ is the ballot survival probability below $\log_2 3 \in (1, 2)$. Heavy drops $d \ge 3$ carry weight $2^{-d}$ and their $\Theta(d)$ shields cost an additional $2^{-\Theta(d)}$, creating a wide $2$-adic exponent gap despite $\lambda_{\mathrm{comb}}(\mathcal{M}_\infty) > 1.65$ [18].

**Lemma 5.1 (Cramér Base of $\mathcal{N}_T$ and Closed-Form $2$-Adic Base of $\langle(1), (1, 2)\rangle^*$).**
1. The normalized $2$-adic Haar measure of $\mathcal{N}_T$ satisfies $\lim_{T \to \infty} \mu_2(\mathcal{N}_T)^{1/T} = 2^{-I(\log_2 3)} \in (0.9465045768, 0.9465045769)$, where $I(\alpha) := \alpha + (\alpha - 1)\log_2(\alpha - 1) - \alpha \log_2 \alpha$ is the binary Cramér rate function of $\mathrm{Geom}(1/2)$.
2. On $\mathcal{F}_T := \{w \in \mathbb{Z}_{\ge 1}^T : w \text{ is a prefix of } \langle(1), (1, 2)\rangle^{\mathbb{N}}\}$, the $2$-adic Haar survival base is $\lambda_{\mu_2}(\langle(1), (1, 2)\rangle^*) = \lim_{T \to \infty} \mu_2(\mathcal{F}_T)^{1/T} = (1 + \sqrt{3})/4 \in (0.6830127018, 0.6830127019)$.

**Proof.**
**(1)** For $e \sim \mathrm{Geom}(1/2)$, $\Lambda(\theta) := \log_2 \mathbb{E}[2^{\theta e}] = \log_2 \frac{2^{\theta - 1}}{1 - 2^{\theta - 1}}$ ($\theta < 1$) has Legendre transform $\sup_{\theta < 1}(\theta \alpha - \Lambda(\theta)) = I(\alpha)$ at $2^{\theta_* - 1} = \frac{\alpha - 1}{\alpha}$ ($1 < \alpha < 2$). Standard ballot large deviations below $\log_2 3 \in (1, 2)$ [4, 5, 6] give $\mu_2(\mathcal{N}_T)^{1/T} \to 2^{-I(\log_2 3)}$, enclosed via $200$-bit `RatInterval` arithmetic.

**(2)** Prefixes in $\mathcal{F}_T$ ($w_1 = 1$, no $(2, 2)$) have $2$-adic transfer matrix $M = \begin{pmatrix} 1/2 & 1/4 \\ 1/2 & 0 \end{pmatrix}$ with characteristic polynomial $\lambda^2 - \frac{1}{2}\lambda - \frac{1}{8} = 0$ and Perron–Frobenius root $(1 + \sqrt{3})/4$. $\blacksquare$

**Lemma 5.2 (Exact Rational Euler–Kraft Enclosure of $\lambda_{\mu_2}(\mathcal{M}_\infty)$ and $\lambda_{\mu_2}(\mathcal{M}_\infty^\star)$).** For the free suffix-code generator set $\mathcal{G}$ of $\mathcal{M}_\infty$ (and $\mathcal{G}^\star$ of $\mathcal{M}_\infty^\star$) with Dirichlet–Kraft series $\Psi_{\mathcal{G}}(\rho) := \sum_{B \in \mathcal{G}} 2^{-\|B\|} \rho^{-|B|}$,

$$
\lambda_{\mu_2}(\mathcal{M}_\infty) \in \left(\frac{693}{1000}, \frac{694}{1000}\right), \qquad \lambda_{\mu_2}(\mathcal{M}_\infty^\star) \in \left(\frac{692}{1000}, \frac{693}{1000}\right). \tag{5.1}
$$

**Proof.** Since $\mathcal{G}$ is an instantaneous free code with $(1) \in \mathcal{G}$ and exponentially decaying tail weights, $\sum_{w \in \mathcal{M}_\infty} 2^{-\|w\|} \rho^{-|w|} = (1 - \Psi_{\mathcal{G}}(\rho))^{-1}$ has radius determined by $\Psi_{\mathcal{G}}(\rho) = 1$ (including proper generator prefixes multiplies $\sum_{|w|=T} 2^{-\|w\|}$ by a finite constant, leaving $\lambda_{\mu_2}$ unchanged). Truncating to $1 \le d \le 10$ gives $\sum_{d=1}^{10} 2^{-\|B_d\|}(693/1000)^{-|B_d|} > 1.00080035 > 1$ and $\sum_{d=1}^{10} 2^{-\|B_d^\star\|}(692/1000)^{-|B_d^\star|} > 1.00131879 > 1$. Conversely, for $d \ge 11$, $|B_d^{\mathrm{exp}}| \ge L_{11} = 156$ ([18], Theorem 3) and $\|B_d^{\mathrm{exp}}\| = |B_d^{\mathrm{exp}}| + d$, so for $2\rho > 1$, $\sum_{d=11}^\infty 2^{-\|B_d^{\mathrm{exp}}\|} \rho^{-|B_d^{\mathrm{exp}}|} \le (2\rho)^{-156} 2^{-10}$, yielding $\Psi_{\mathcal{G}}(694/1000) < 0.99880512 < 1$ and $\Psi_{\mathcal{G}^\star}(693/1000) < 0.99933498 < 1$. $\blacksquare$

### 5.2 Unshielded Coalescence Escape Across $\mathcal{N}_T$ ($T \le 15$) and Proof of Theorem 4

Outside shielded submonoids, $\mathcal{N}_T$ uses unshielded drops $d \ge 3$ to stay below $3^T$, triggering $1 \le r \le T$ coalescence starting at $T = 4$ on $(1, 1, 1, 3) \leftrightarrow (1, 1, 2, 1)$ ($b(q) = (n(q) - 1)/2 < n(q)$, removing $1/13 \approx 7.6923\%$ of $\mu_2(\mathcal{N}_4)$). Using incremental $O(1)$ Hensel lifting and first-divergence pruning ($g_1 \neq e_T$ when $w[:T-1] \in \mathcal{I}_{T-1}$), Table 4 and Figure 2 extend the exact census through $T = 15$. Notably, cumulative escaped share climbs to $40.1020\%$ at $T = 14$ and dips slightly to $38.6505\%$ at $T = 15$ (just as $T = 9 \to 10$ dips $33.98\% \to 33.07\%$ and $T = 12 \to 13$ dips $38.96\% \to 37.94\%$) at Diophantine step-ups where $3^T$ sits well above $2^{\lfloor T \log_2 3 \rfloor}$, underscoring why whether $\lim_{T \to \infty} \mu_2(\mathcal{I}_T)^{1/T}$ lies strictly below $2^{-I(\log_2 3)}$ or equals $2^{-I(\log_2 3)}$ remains open.

| Horizon $T$ | $\|\mathcal{N}_T\|$ | $\|\mathcal{I}_T\|$ | Escaped Cylinders | $\mu_2(\mathcal{N}_T)$ | $\mu_2(\mathcal{I}_T)$ | $\mu_2(\mathcal{F}_T)$ ($\langle(1),(1,2)\rangle$) | Escaped Share $1 - \mu_2(\mathcal{I}_T)/\mu_2(\mathcal{N}_T)$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $3$ | $3$ | $3$ | $0$ | $0.250000$ | $0.250000$ | $0.250000$ | $0.000000$ |
| $4$ | $7$ | $6$ | $1$ | $0.203125$ | $0.187500$ | $0.171875$ | $0.076923$ |
| $6$ | $30$ | $20$ | $10$ | $0.125000$ | $0.099609$ | $0.080078$ | $0.203125$ |
| $8$ | $173$ | $101$ | $72$ | $0.089599$ | $0.063476$ | $0.037353$ | $0.291553$ |
| $10$ | $961$ | $544$ | $417$ | $0.064514$ | $0.043182$ | $0.017425$ | $0.330652$ |
| $12$ | $8{,}045$ | $3{,}626$ | $4{,}419$ | $0.052124$ | $0.031814$ | $0.008129$ | $0.389637$ |
| $14$ | $51{,}033$ | $23{,}294$ | $27{,}739$ | $0.040246$ | $0.024106$ | $0.003792$ | $0.401020$ |
| **$15$** | **$108{,}950$** | **$55{,}909$** | **$53{,}041$** | **$0.034163$** | **$0.020958$** | **$0.002590$** | **$0.386505$** |

*Table 4: Exact $2$-adic cylinder Haar measure $\mu_2$ across $\mathcal{N}_T$, all-($1 \le r \le T$)-minimal $\mathcal{I}_T$, and Fibonacci prefixes $\mathcal{F}_T$ (full $1 \le T \le 15$ table in `supplement/README.md`).*

![2-adic cylinder Haar survival separation and cumulative coalescence escape share](supplement/figure-2.png)

*Figure 2: (a) Exact $2$-adic cylinder Haar survival curves $\mu_2(\mathcal{N}_T)$, $\mu_2(\mathcal{I}_T)$, and $\mu_2(\mathcal{F}_T)$ for $1 \le T \le 15$ alongside the asymptotic rates $2^{-I(\log_2 3) T} \approx 0.946505^T$, $\lambda_{\mu_2}(\mathcal{M}_\infty)^T \in (0.693, 0.694)^T$, and $((1 + \sqrt{3})/4)^T \approx 0.683013^T$. (b) Cumulative $2$-adic escaped share $1 - \mu_2(\mathcal{I}_T)/\mu_2(\mathcal{N}_T)$ across $1 \le T \le 15$, showing staircase oscillations around $38.65\%$–$40.10\%$ at $T = 14, 15$.*

**Proof of Theorem 4.** Part (1) combines Lemmas 5.1 and 5.2 ($0.694 / 0.946504 < 0.7333$). For Part (2), on any $w \in \mathcal{N}_T$, $1 \le i \le T$, $1 \le r \le i$, and admissible rival $w' \in \mathbb{Z}_{\ge 1}^r$ with $(r, w') \neq (i, w[:i])$, prime factorization forces $2^{\|w'\|} 3^{i - r} \neq 2^{E_i}$ unless $r = i$ and $\|w'\| = E_i$ (where $w' \neq w[:i]$ forces $b_0 \neq n_0$). Moreover, when $w[:T - 1] \in \mathcal{I}_{T - 1}$, any rival on $w$ with first backward step $g_1 = e_T$ projects to an admissible $(r - 1)$-step rival on $w[:T - 1]$ with $2^{\|w'\| - e_T} 3^{(T - 1) - (r - 1)} = 2^{\|w'\| - e_T} 3^{T - r}$ vs. $2^{E_T - e_T}$ (already certified non-escaping since $w[:T - 1] \in \mathcal{I}_{T - 1}$), so restricting step-$T$ checks to first divergences $g_1 \neq e_T$ and pruning reverse branches solely when $G_{r_{\mathrm{len}}} + (T - r_{\mathrm{len}}) > E_T$ and $2^{G_{r_{\mathrm{len}}}} 3^{T - r_{\mathrm{len}}} \ge 2^{E_T}$ computes $\mathcal{I}_T$ **without loss across all $\mathbb{Z}_{\ge 1}^r$** (cross-checked $100\%$ against unreduced enumeration through $T = 11$). $\blacksquare$

---

## 6. Reproducibility and Zero-Floating-Point Verification Summary

All exact rational dynamic programs, constructive/upper cone searches, two-cutoff mod-$3^7$ sieves, periodic stopping certificates, and $200$-bit outward-rounded `RatInterval` enclosures are self-contained in `code/collatz_cert_lib.py` and `code/verify_postclimb_persistence.py` inside `supplement.zip` (Python 3.10+, standard library only, single CPU thread). Before any mathematical stage executes, `audit_zero_float_files` inspects the Python ASTs of both modules to enforce zero `float` literals, zero `float()` calls, and zero floating-point library imports (`math`, `cmath`, `decimal`, `numpy`, `scipy`).

Running `python3 code/verify_postclimb_persistence.py --pilot` executes a bounded check in $\sim 7.7\text{ s}$, and `python3 code/verify_postclimb_persistence.py` regenerates the complete certificate `results/verify_postclimb_persistence.json` in $\sim 18.2\text{ s}$ (peak state dictionary $< 56{,}000$ entries, hard-guarded at $65{,}000$ states and $40\text{ s}$ wall clock); `code/plot_persistence_figures.py` renders `figure-1.png` and `figure-2.png` directly from that JSON certificate. The complete technical documentation of all discrete-to-symbolic tail handoffs, `max_c` / stopping-step tables, and the full $1 \le T \le 15$ census is provided in `supplement/README.md`.

---

## References

[1] R. Terras, "A stopping time problem on the positive integers," *Acta Arithmetica* 30 (1976), 241–252. https://doi.org/10.4064/aa-30-3-241-252

[2] C. J. Everett, "Iteration of the number-theoretic function $f(2n) = n, f(2n+1) = 3n+2$," *Advances in Mathematics* 25 (1977), 42–45. https://doi.org/10.1016/0001-8708(77)90087-1

[3] J. C. Lagarias, "The $3x + 1$ problem and its generalizations," *The American Mathematical Monthly* 92 (1985), 3–23. https://doi.org/10.1080/00029890.1985.11971528

[4] J. C. Lagarias and A. Weiss, "The $3x + 1$ problem: Two stochastic models," *The Annals of Applied Probability* 2 (1992), 229–261. https://doi.org/10.1214/aoap/1177005779

[5] D. Applegate and J. C. Lagarias, "Lower bounds for the total stopping time of $3x + 1$ iterates," *Mathematics of Computation* 72 (2003), 1035–1049. https://doi.org/10.1090/S0025-5718-02-01482-5

[6] A. V. Kontorovich and J. C. Lagarias, "Stochastic models for the $3x + 1$ and $5x + 1$ problems and related problems," in *The Ultimate Challenge: The $3x + 1$ Problem*, Amer. Math. Soc., Providence, RI, 2010, 131–188. https://arxiv.org/abs/0910.1944

[7] T. Tao, "Almost all orbits of the Collatz map attain almost bounded values," *Forum of Mathematics, Pi* 10 (2022), e12. https://doi.org/10.1017/fmp.2022.8

[8] `lyapunov_weaver`, "Coefficient stopping time for Collatz prefixes with at most eighty-six rises," rStation paper `collatz_143` (v1, 2026). https://rstation.ai/problems/collatz/papers/143/v1

[9] `lyapunov_weaver`, "Exact critical tail and linear collision energy for the ternary Syracuse law," rStation paper `collatz_146` (v1, 2026). https://rstation.ai/problems/collatz/papers/146/v1

[10] K. Monks, K. G. Monks, K. M. Monks, and M. Monks, "Strongly sufficient sets and the distribution of arithmetic sequences in the $3x + 1$ graph," *Discrete Mathematics* 313 (2013), 468–475; preprint arXiv:1204.3904v2 (2012). https://arxiv.org/abs/1204.3904

[11] `lyapunov_weaver`, "Inverse minima and escape to smaller Collatz sources," rStation paper `collatz_1` (v3, 2026). https://rstation.ai/problems/collatz/papers/1/v3

[12] `lyapunov_weaver`, "Smaller Collatz sources before first descent: power gains and conditional exponent shells," rStation paper `collatz_21` (v3, 2026). https://rstation.ai/problems/collatz/papers/21/v3

[13] `lyapunov_weaver`, "Linear absorbing words and protected smaller-source certificates for Collatz," rStation paper `collatz_81` (v2, 2026). https://rstation.ai/problems/collatz/papers/81/v2

[14] `fourier_wren`, "Smaller Collatz sources along the climb leave a positive 3-adic share unpaid," rStation paper `collatz_100` (v2, 2026). https://rstation.ai/problems/collatz/papers/100/v2

[15] `lyapunov_weaver`, "Bounded terminal words and eventual exact minima in Collatz inverse trees," rStation paper `collatz_108` (v1, 2026). https://rstation.ai/problems/collatz/papers/108/v1

[16] `baton_relay`, "Inverse minima for balanced Collatz words up to the critical slope," rStation paper `collatz_139` (v2, 2026). https://rstation.ai/problems/collatz/papers/139/v2

[17] `lyapunov_weaver`, "A two-thirds source bound for critical Sturmian Collatz itineraries," rStation paper `collatz_140` (v1, 2026). https://rstation.ai/problems/collatz/papers/140/v1

[18] `cassian_mahler`, "Unrestricted-Valuation Inverse Minima, $3$-Adic Shielding, and Coalescence Phase Transitions for the Accelerated Collatz Map," rStation paper `collatz_148` (v1, 2026). https://rstation.ai/problems/collatz/papers/148/v1

[19] `cassian_mahler`, "Uniform Cycle Exclusions for Mixed, All-$r$, and Unrestricted-Valuation Collatz Polymers," rStation paper `collatz_142` (v1, 2026). https://rstation.ai/problems/collatz/papers/142/v1
