## 1. Introduction, Prior Work, and Main Contributions

### 1.1 Background: Dimer Circuits and Stretch-Start Trough Windows

Let $T: \mathbb{Z}_{\mathrm{odd},\ge 1} \to \mathbb{Z}_{\mathrm{odd},\ge 1}$ denote the odd-accelerated Collatz (Syracuse) map
$$
T(z) = \frac{3z + 1}{2^{e(z)}}, \qquad e(z) := v_2(3z + 1) \ge 1,
$$
whose global convergence to $1$ is the Collatz conjecture [1]. In the string-rewriting investigation of Yolcu, Aaronson, and Heule [2] (Conjecture 4.14 and Proposition 4.15), termination of the minimal $11$-rule rewriting system $H$ is equivalent to the assertion that every nonconvergent positive Collatz orbit visits $\{5, 7\} \bmod 8$. Along odd trajectories avoiding $\{5, 7\} \bmod 8$, every step with $e(z) = 1$ forces $z \equiv 3 \pmod 8$ and $T(z) \equiv 1 \pmod 8$, so $e(T(z)) = 2$; hence complete $\{5, 7\} \bmod 8$-avoiding circuits concatenate **dimer circuits** $w = ((u_1, v_1), \ldots, (u_L, v_L)) \in (\mathbb{Z}_{\ge 1}^2)^L$ with valuation word
$$
e(w) = (1, 2)^{u_1} (2)^{v_1} \cdots (1, 2)^{u_L} (2)^{v_L}.
$$
Each circuit letter $\gamma = (u, v) \in \mathbb{Z}_{\ge 1}^2$ executes $2u + v$ odd Syracuse steps and $3u + 2v$ halvings, composing a rising dimer run $(1, 2)^u$ of slope $(9/8)^u$ centered at $-5$ with a standalone fall run $(2)^v$ of slope $(3/4)^v$ centered at $+1$ [3], [4]. On stretch-aligned circuit starts $z = 6Q + 1 \equiv 91 \pmod{144}$, the **stretch start** $Q \equiv 15 \pmod{24}$ evolves via $Q + 1 = 8^u a$, $9^u a - 1 = 4^v b$, and $Q' = 3^v b$ with $\gcd(a, 6) = 1$, $b \not\equiv 0 \pmod 4$, and $\gcd(b, 3) = 1$ [4], yielding the exact single-circuit affine branch
$$
\Phi_{u,v}(Q) = \frac{a_{u,v} Q + c_{u,v}}{b_{u,v}}, \qquad a_{u,v} := 3^{2u+v},\quad b_{u,v} := 2^{3u+2v},\quad c_{u,v} := 3^v(9^u - 8^u) > 0,
$$
and its inverse branch $\Phi_{u,v}^{-1}(Q) = (b_{u,v} Q - c_{u,v})/a_{u,v}$.

Consider a depth-$L$ stretch chain $Q_{-L} \mapsto \cdots \mapsto Q_0 \mapsto \cdots \mapsto Q_L$ centered at $Q_0 = Q \equiv 15 \pmod{24}$, with outward backward word $w_- = (\beta_1, \ldots, \beta_L) \in (\mathbb{Z}_{\ge 1}^2)^L$ ($\beta_c := (u_{-c+1}, v_{-c+1})$, tracing $Q_0 \mapsto Q_{-1} \mapsto \cdots \mapsto Q_{-L}$ under $\Phi_{\beta_1}^{-1}, \ldots, \Phi_{\beta_L}^{-1}$) and forward word $w_+ = (\alpha_1, \ldots, \alpha_L) \in (\mathbb{Z}_{\ge 1}^2)^L$ ($\alpha_c := (u_c, v_c)$, tracing $Q_0 \mapsto Q_1 \mapsto \cdots \mapsto Q_L$). Following [4], $Q$ is a **forward trough start** of depth $L$ ($Q \in \mathcal{T}_1(L)$) if $Q_c > Q$ for all $1 \le c \le L$, and a **two-sided trough centre** of depth $L$ ($Q \in \mathcal{T}_2(L)$) if $Q_c > Q$ for all $c \in \{-L, \ldots, L\} \setminus \{0\}$. Writing $R_c^+ = \sum_{j=1}^c (2u_j + v_j)$, $S_c^+ = \sum_{j=1}^c (3u_j + 2v_j)$, $R_c^- = \sum_{j=1}^c (2u_{-j+1} + v_{-j+1})$, and $S_c^- = \sum_{j=1}^c (3u_{-j+1} + 2v_{-j+1})$, $w_+$ is **forward-eligible** ($w_+ \in \mathcal{E}_L^+$) if $3^{R_c^+} > 2^{S_c^+}$ for all $1 \le c \le L$, and $w_-$ is **backward-eligible** ($w_- \in \mathcal{E}_L^-$) if $2^{S_c^-} > 3^{R_c^-}$ for all $1 \le c \le L$ [5]. Write $\mathcal{T}_1^e(L) \subseteq \mathcal{T}_1(L)$ and $\mathcal{T}_2^e(L) \subseteq \mathcal{T}_2(L)$ for the eligible subsets, $Q_{\min,1}(L) := \min \mathcal{T}_1(L)$, $Q_{\min,1}^e(L) := \min \mathcal{T}_1^e(L)$, $Q_{\min,2}(L) := \min \mathcal{T}_2(L)$, and $Q_{\min,2}^e(L) := \min \mathcal{T}_2^e(L)$, with base values $B_1 := Q_{\min,1}(1) = 14{,}847$ and $B_2 := Q_{\min,2}(1) = 1{,}047{,}039$ [4], [5].

### 1.2 Inherited Prior Work vs. Open Two-Sided Questions

We separate explicitly at the outset what is already proved in the literature from what is established here:

1. **Trough-floor cycle exclusions and three open two-sided problems (`collatz_71` v2 [4], `collatz_74` v2 [6], and `collatz_77` v2 [5]).** Paper [4] introduced the unrestricted exponential floor hypotheses $Q_{\min,1}(L) \ge B_1 A^{L-1}$ ($\mathrm{T}_1(A)$) and $Q_{\min,2}(L) \ge B_2 A^{L-1}$ ($\mathrm{T}_2(A)$), proved automatic forward distinctness on troughs ([4, Lemma 1]), certified $Q_{\min,1}(1 \ldots 3)$ and $Q_{\min,2}(1 \ldots 3)$, and excluded all nontrivial dimer cycles under $\mathrm{T}_1(1.90)$ or $\mathrm{T}_2(3.59)$. Paper [5] restricted these hypotheses to eligible windows ($\mathrm{T}_1^e(1.82)$ and $\mathrm{T}_2^e(3.29)$) via an early/late first-slope-dip split ([5, Lemma 3 and Theorem A], incorporating open-prefix product and height inequalities of `lyapunov_weaver` acknowledged therein), and combined a two-hour $C$ backward cycle sieve (`cyc12d.c`, yielding $x_{\min} > 2^{90}$ on cycles) with $920$ upper Farey fractions of $\theta := \log_2 3$ to exclude all dimer cycles with $M \le 983$ circuits ([5, Theorem C and Corollary D]), extending the $247$-run bound of [6]. Meanwhile, [4, Section 5] and [5, Section 7] left three explicit structural questions open on two-sided troughs:
   - *True vs. heuristic two-sided density rate:* Section 5 of [4] (and Section 7 of [5]) heuristically squared the forward Cramér inverse base $122.36$ to predict a two-sided union density of order $(1.5 \times 10^4)^{-L}$, while noting empirically at $L \le 3$ that backward $3$-adic eligibility decays near $16^{-L}$ rather than $122.36^{-L}$.
   - *Cylinder-residue repulsion and bi-adic junction coupling:* Section 5 of [4] noted that density sums bound cylinder measure rather than minimum integer representatives, leaving open whether distinct cylinders repel one another effectively and how forward $2$-adic and backward $3$-adic constraints couple Diophantinely across $Q$.
   - *Non-eligible open-window trough centres:* Section 5 of [4] found zero non-eligible trough centres at $L \le 3$ and asked whether non-eligible two-sided troughs exist at any depth $L$ or whether $\mathrm{T}_2^e(A)$ and $\mathrm{T}_2(A)$ coincide across all depths.
2. **Dictionary complexity, conditional finiteness collapse, and complementary orbit bounds (`collatz_15` v2 [7], `collatz_147` v1 [8], `collatz_8` v2 [9], `collatz_190` v1 [10], and `collatz_186`/`188`/`192` [11], [12], [13]).** Papers [7] and [8] established periodic-dictionary duration and fixed-fragment excursion bounds; [9] introduced dual-seed fixed-point homogenization; and [10] proved unbounded-circuit dual-anchor run concentration, collapsed the conditional trough-floor bases for *cycle finiteness* to every $A > 1$ via [7] (and proved no divergent dimer trajectory exists under $\mathrm{T}_1^e(A)$ for $A > 1$), and certified **one-sided forward** eligible minima $Q_{\min,1}^e(1 \ldots 9)$ alongside $\Sigma_+^e(L) < 122.359^{-L}$. Complementarily, [11], [12], and [13] established unconditional $2^{129}$ state floors, $-5$-neighbourhood occupation bounds, and irregular block-order constraints on hypothetical cycles. None of [7]–[13], however, analyzed backward $3$-adic cylinder survival, two-sided CRT trough minima beyond $L = 3$, pairwise swap cylinder repulsion, or unconditional open-window non-eligible absence.

### 1.3 Summary of Main New Results

Resolving all three open structural questions of [4, Section 5] and [5, Section 7], we establish four theorems verified by an AST-audited zero-floating-point Python suite:

- **Theorem 1 (Bi-Adic Esscher Measure Duality, Positive Backward Survival $P_\infty^-$, and Exact Two-Sided Union Density Rate; Section 2).** Normalizing single-letter forward $2$-adic cylinder densities $\mathbb{P}_+(u, v) = 21 \cdot 2^{-(3u+2v)}$ and outward backward $3$-adic cylinder densities $\mathbb{P}_-(u, v) = 16 \cdot 3^{-(2u+v)}$ on $\mathbb{Z}_{\ge 1}^2$, we prove the exact Esscher Radon–Nikodym identity $\mathbb{P}_-(u, v)/\mathbb{P}_+(u, v) = \frac{16}{21} e^{-X(u,v)}$ for $X(u, v) = (2u+v)\ln 3 - (3u+2v)\ln 2$, giving $M_-^{\mathrm{unnorm}}(-(1+t)) = M_+^{\mathrm{unnorm}}(t)$ across exact convergence strips $I_+$ and $I_- = -1 - I_+$. Because outward backward drift under $\mathbb{P}_-$ is strictly positive ($\mathbb{E}_-[-X] = \frac{51}{8}\ln 2 - \frac{15}{4}\ln 3 \approx +0.299017 > 0$), $P_L^- := 16^L \Sigma_-^e(L)$ satisfies $0 < P_{L-1}^- - P_L^- \le \rho_-^L$ ($\rho_- = 16 M_* \approx 0.130763$), enclosing $P_\infty^- := \lim_{L\to\infty} P_L^- \in [0.990624784996, 0.990624785001]$. Combining an elementary two-limit super-saddle tilt ($t_1 > \vartheta_*$, deterministic prefix $(3, 1)^m$, Markov ruin, and Chebyshev cap) with bi-adic cylinder realization proves $\lim_{L\to\infty} d_{\mathrm{nat}}(\mathcal{T}_2^e(L))^{-1/L} = 16/M_* \in [1957.747537287457, 1957.747537287458]$, resolving the $(1.5 \times 10^4)^L$ heuristic of [4], [5] and explaining the minimal-shell sawtooth $\Delta S_{\min}^+(L) \in \{8, 11\}$.
- **Theorem 2 (Catalan $\{2, 3\}$-Unit Dimer Commutators and 100% Effective Subspace-Free Swap Repulsion; Section 3).** Exploiting the Catalan identities $3^2 - 2^3 = 1$ and $2^2 - 3^1 = 1$, we prove that adjacent circuit swaps in Family I ($\{(u, 1), (u+1, 1)\}$) and Family II ($\{(1, v), (1, v+1)\}$) possess pure $\{2, 3\}$-unit affine commutators of opposite signs. Without invoking any ineffective Subspace theorem, elementary prime-power congruence inversion yields closed-form **100% effective** all-$L$ cylinder-residue separation $|Q_{w'} - Q_w| \ge 2^{\gamma_+ S_+ + c_+}$ ($\gamma_+ = (1 + \frac{7}{11}\theta)^{-1} > 0.49785$) on $\{(2, 1), (3, 1)\}^L$ and $|Q_{w'} - Q_w| \ge 3^{\gamma_- R_- + c_-}$ ($\gamma_- = (1 + \frac{7}{4\theta})^{-1} > 0.47525$) on outward backward $\{(1, 1), (1, 2)\}^L$, complemented by qualitative $(2^{S_+} 3^{R_-})^{1-\varepsilon}$ Ridout separation [14] on joined two-sided cylinders.
- **Theorem 3 (Fixed-Point Sign Separation $q_\alpha < 0 < q_\beta$ and Bi-Adic Homogeneous Junction Floors; Section 4).** Every forward-eligible letter $\alpha$ and backward-eligible letter $\beta$ satisfy $q_\alpha < 0 < q_\beta < Q$ on every two-sided trough centre $Q$, with exact backward power threshold $\Phi_\beta^{-n}(Q) - Q = ((b_\beta/a_\beta)^n - 1)(Q - q_\beta)$. At the homogeneous junction $(\beta^{L_-}, \alpha^{L_+})$, dividing the exact linear identity $A - B = K_{\alpha,\beta} > 0$ by $\gcd(A, B) \mid K_{\alpha,\beta}$ and applying Ridout's theorem [14] on $\mathbb{P}^1 \setminus \{0, 1, \infty\}$ upgrades the trivial one-sided bound $\max(2^{S_+}, 3^{R_-})$ to the qualitative bi-adic product $Q \ge C_{\alpha,\beta,\varepsilon}(2^{S_+} 3^{R_-})^{1-\varepsilon}$ (with *ineffective* constant $C_{\alpha,\beta,\varepsilon} > 0$), while Proposition A.1 proves an unconditional $2$-adic valuation staircase ruling out vanishing proper subsums for arbitrary block counts on $\{(1, 1), (1, 2)\} \times \{(2, 1), (3, 1)\}$.
- **Theorem 4 (Exact Meet-in-the-Middle Minima $Q_{\min,2}(1 \ldots 7)$, Unconditional Open-Window Non-Eligible Absence Through $L = 982$, Global Equivalence $\mathrm{T}_2^e(3.29) \iff \mathrm{T}_2(3.29)$, and Pure-Python $M \le 983$ Cycle Exclusion; Section 5).** Exact bi-adic CRT meet-in-the-middle search certifies $Q_{\min,2}(L) = Q_{\min,2}^e(L)$ for $1 \le L \le 7$, reaching $Q_{\min,2}(7) = 346{,}478{,}037{,}594{,}486{,}391{,}014{,}903{,}807$ ($x_{\min}(7) > 2^{90.74}$), and brackets $Q_{\min,2}(8) \in [389{,}787{,}792{,}293{,}797{,}189{,}891{,}766{,}779,\ 17{,}456{,}474{,}080{,}278{,}349{,}696{,}924{,}904{,}587{,}263]$. Combining open-prefix dip inequalities [4], [5] with Rhin's irrationality measure [15], [16] (shown unconditionally valid at **every** dip depth $i \ge 1$ via Bernoulli's inequality $\delta_j \le u_j/9$), we prove **unconditionally** across all $Q \in \mathbb{Z}_{\ge 1}$ and all $(u, v) \in \mathbb{Z}_{\ge 1}^2$ that $\mathcal{T}_2(L) = \mathcal{T}_2^e(L)$ for all $1 \le L \le 982$ and $\mathcal{T}_1(L) = \mathcal{T}_1^e(L)$ for all $1 \le L \le 634$, establish the all-depth equivalences $\mathrm{T}_2^e(A) \iff \mathrm{T}_2(A)$ ($A \ge 3.29$) and $\mathrm{T}_1^e(A) \iff \mathrm{T}_1(A)$ ($A \ge 1.82$), and provide a self-contained pure-Python verification of [5, Corollary D]'s $M \le 983$ dimer-cycle exclusion directly from $Q_{\min,2}(7)$.

---

## 2. Bi-Adic Cylinders, Esscher Measure Duality, Positive Backward Survival, and True Density Rate

### 2.1 Coupled Bi-Adic Cylinder Realization and Backward Thresholds

Let $w_+ = (\alpha_1, \ldots, \alpha_L)$ have totals $(R_+, S_+) := (R_L^+, S_L^+)$ and composed forward map $\Phi_{w_+}(Q) = (3^{R_+} Q + C_+)/2^{S_+}$ ($C_+ > 0$), and let $w_- = (\beta_1, \ldots, \beta_L)$ have totals $(R_-, S_-) := (R_L^-, S_L^-)$ and composed outward inverse map $\Phi_{w_-}^{-1}(Q) = (2^{S_-} Q - C_-)/3^{R_-}$ ($C_- > 0$). Pulling back the stretch-start congruences $Q_L \equiv 7 \pmod 8$ in $\mathbb{Z}_2$ (with $Q \equiv 0 \pmod 3$) and $Q_{-L} \equiv 0 \pmod 3$ in $\mathbb{Z}_3$ (with $Q \equiv 7 \pmod 8$) determines exact cylinder congruences
$$
Q \equiv r_+(w_+) \pmod{24 \cdot 2^{S_+}}, \qquad Q \equiv r_-(w_-) \pmod{24 \cdot 3^{R_-}}, \qquad r_+(w_+) \equiv r_-(w_-) \equiv 15 \pmod{24}.
$$
Specifically, $3^{R_+} r_+(w_+) + C_+ \equiv 7 \cdot 2^{S_+} \pmod{2^{S_++3}}$ ensures odd intermediate cofactors $a_c, b_c$ (hence exact halving counts $3u_c, 2v_c$) at every forward step while $\Phi_{\alpha_c}$ maps $3\mathbb{Z}_3$ into $3\mathbb{Z}_3$; dually, $2^{S_-} r_-(w_-) - C_- \equiv 0 \pmod{3^{R_-+1}}$ ensures exact ternary valuations $v_3(Q_{-c+1}) = v_{-c+1}$ and $v_3(4^{v_{-c+1}} b_{-c+1} + 1) = 2u_{-c+1}$ at every inverse step while $Q \equiv 7 \pmod 8$ preserves $Q_{-c} \equiv 7 \pmod 8$ in $\mathbb{Z}_2$ (`forward_cylinder` and `backward_cylinder` in `verify_twosided_troughs.py`). Since $\gcd(2^{S_+}, 3^{R_-}) = 1$, Chinese Remainder Theorem (CRT) lifting merges $(w_-, w_+)$ into a **unique** coupled residue class
$$
Q \equiv r(w_-, w_+) \pmod{24 \cdot 2^{S_+} 3^{R_-}}, \qquad 0 \le r(w_-, w_+) < 24 \cdot 2^{S_+} 3^{R_-}.
$$
Whenever $w_+ \in \mathcal{E}_L^+$, $3^{R_c^+} > 2^{S_c^+}$ and $C_c^+ > 0$ imply $\Phi_{w_+\upharpoonright c}(Q) > Q$ automatically for every $Q > 0$ [5]. Whenever $w_- \in \mathcal{E}_L^-$, $\Phi_{w_-\upharpoonright c}^{-1}(Q) = (2^{S_c^-} Q - C_c^-)/3^{R_c^-} > Q$ holds if and only if $Q \ge Q_{\mathrm{thr}}(w_-)$, where
$$
Q_{\mathrm{thr}}(w_-) := \max\!\left(\{15\} \cup \left\{ \left\lfloor \frac{C_c^-}{2^{S_c^-} - 3^{R_c^-}} \right\rfloor + 1 : 1 \le c \le L \right\}\right)
$$
(which automatically forces $Q_{-c} > Q \ge 15$, so every backward predecessor is a valid stretch start). Define the unnormalized cylinder-density sums
$$
\Sigma_+^e(L) := \sum_{w_+ \in \mathcal{E}_L^+} 2^{-S_+(w_+)}, \qquad \Sigma_-^e(L) := \sum_{w_- \in \mathcal{E}_L^-} 3^{-R_-(w_-)}.
$$
Since $\sum_{u,v \ge 1} 2^{-(3u+2v)} = \frac{1/8}{7/8}\cdot\frac{1/4}{3/4} = \frac{1}{21}$ and $\sum_{u,v \ge 1} 3^{-(2u+v)} = \frac{1/9}{8/9}\cdot\frac{1/3}{2/3} = \frac{1}{16}$, the normalized single-letter laws on $\mathbb{Z}_{\ge 1}^2$ are $\mathbb{P}_+(u, v) := 21 \cdot 2^{-(3u+2v)}$ and $\mathbb{P}_-(u, v) := 16 \cdot 3^{-(2u+v)}$, with $\Sigma_+^e(L) = 21^{-L} \mathbb{P}_+^{\otimes L}(\mathcal{E}_L^+)$ and $\Sigma_-^e(L) = 16^{-L} P_L^-$ for the **backward $3$-adic eligibility survival probability** $P_L^- := 16^L \Sigma_-^e(L) = \mathbb{P}_-^{\otimes L}(\mathcal{E}_L^-)$.

### 2.2 Theorem 1: Esscher Duality, Backward Survival Sandwich, and Exact Union Density Rate

Write $X(u, v) := (2u + v)\ln 3 - (3u + 2v)\ln 2$ for the single-circuit log-slope, and define $M_+^{\mathrm{unnorm}}(t) := \sum_{u,v \ge 1} 2^{-(3u+2v)} e^{t X(u,v)}$ and $M_-^{\mathrm{unnorm}}(\tilde t) := \sum_{u,v \ge 1} 3^{-(2u+v)} e^{\tilde t (-X(u,v))}$.

**Theorem 1 (Esscher Measure Duality, All-$L$ Backward Survival Sandwich, and True Two-Sided Density Rate).**
1. *(Exact Esscher tilt and strip reflection.)* For every $(u, v) \in \mathbb{Z}_{\ge 1}^2$,
   $$
   \frac{\mathbb{P}_-(u, v)}{\mathbb{P}_+(u, v)} = \frac{16}{21}\, e^{-X(u,v)}.
   $$
   Consequently, $M_+^{\mathrm{unnorm}}(t) = \frac{3^{2t}/8^{1+t}}{1 - 3^{2t}/8^{1+t}} \cdot \frac{3^t/4^{1+t}}{1 - 3^t/4^{1+t}}$ converges on the open strip $I_+ := \bigl(-\frac{2\ln 2}{\ln(4/3)}, \frac{3\ln 2}{\ln(9/8)}\bigr)$, $M_-^{\mathrm{unnorm}}(\tilde t)$ converges on $I_- := -1 - I_+ = \bigl(-\frac{3\ln 2}{\ln(9/8)} - 1, \frac{2\ln 2}{\ln(4/3)} - 1\bigr)$, and for every $t \in I_+$,
   $$
   M_-^{\mathrm{unnorm}}(-(1 + t)) = M_+^{\mathrm{unnorm}}(t).
   $$
   The unique convex minimum $M_* := \min_{t \in I_+} M_+^{\mathrm{unnorm}}(t) \in [0.008172657452129236, 0.008172657452129237]$ is attained at $\vartheta_* \in \bigl[\frac{1860023650839347}{140737488355328}, \frac{3720047301678695}{281474976710656}\bigr] \approx 13.216263$ for $M_+^{\mathrm{unnorm}}$ and at $\tilde t_* = -(1 + \vartheta_*) \approx -14.216263$ for $M_-^{\mathrm{unnorm}}$, with normalized Chernoff factors $\rho_+ := 21 M_* \in [0.171625806494713959, 0.171625806494713960]$ and $\rho_- := 16 M_* \in [0.130762519234067778, 0.130762519234067779]$.
2. *(Positive backward drift and all-$L$ survival sandwich.)* Under $\mathbb{P}_-$, the outward step $-X(u, v)$ has strictly positive mean
   $$
   \mathbb{E}_-[-X] = \frac{51}{8}\ln 2 - \frac{15}{4}\ln 3 \in [0.299017193564240004, 0.299017193564240005] > 0.
   $$
   Hence for every $L \ge 1$ ($P_0^- := 1$), $0 < P_{L-1}^- - P_L^- \le \rho_-^L$. Thus $P_\infty^- := \lim_{L\to\infty} P_L^-$ satisfies $P_J^- - \frac{\rho_-^{J+1}}{1 - \rho_-} \le P_\infty^- \le P_J^-$ for every truncation depth $J \ge 1$, and at $J = 12$,
   $$
   P_\infty^- \in [0.990624784996663213,\ 0.990624785000422836], \qquad P_\infty^- \cdot 16^{-L} \le \Sigma_-^e(L) \le P_{\min(L,12)}^- \cdot 16^{-L}\quad (\forall L \ge 1).
   $$
3. *(Exact forward Cramér limit and realized two-sided natural density.)* For every $L \ge 1$, $\Sigma_+^e(L) \le M_*^L$ and $\lim_{L\to\infty} \Sigma_+^e(L)^{1/L} = M_*$. Moreover, for every fixed depth $L \ge 1$, $\mathcal{T}_2^e(L)$ possesses an exact natural density in $\mathbb{Z}_{\ge 1}$ equal to
   $$
   d_{\mathrm{nat}}(\mathcal{T}_2^e(L)) := \lim_{N \to \infty} \frac{|\mathcal{T}_2^e(L) \cap [1, N]|}{N} = \frac{1}{24}\,\Sigma_-^e(L)\,\Sigma_+^e(L),
   $$
   whose inverse $d_{\mathrm{nat}}(\mathcal{T}_2^e(L))^{-1}$ grows at the exact exponential base
   $$
   \lim_{L \to \infty} d_{\mathrm{nat}}(\mathcal{T}_2^e(L))^{-1/L} = \frac{16}{M_*} \in [1957.747537287457601366,\ 1957.747537287457601367].
   $$

*Proof.*
**(1)** Direct evaluation gives $\mathbb{P}_+(u, v) e^{-X(u,v)} = 21 \cdot 2^{-(3u+2v)} \cdot 2^{3u+2v} 3^{-(2u+v)} = \frac{21}{16} \mathbb{P}_-(u, v)$. Summing the independent geometric series over $u \ge 1$ and $v \ge 1$ converges iff $3^{2t} < 8^{1+t}$ and $3^t < 4^{1+t}$, i.e., $t \in I_+$, and substituting $\tilde t = -(1 + t)$ into $M_-^{\mathrm{unnorm}}(\tilde t) = \sum_{u,v \ge 1} 3^{-(2u+v)} (2^{3u+2v}/3^{2u+v})^{\tilde t}$ gives $\sum_{u,v \ge 1} 2^{-(3u+2v)} (3^{2u+v}/2^{3u+2v})^t = M_+^{\mathrm{unnorm}}(t)$. Strict log-convexity of $M_+^{\mathrm{unnorm}}$ on $I_+$ ensures a unique minimum $\vartheta_*$, enclosed in $200$-bit `RatInterval` arithmetic (`cramer_saddles` in `verify_twosided_troughs.py`).

**(2)** Under $\mathbb{P}_-$, $u$ and $v$ are independent geometric variables on $\mathbb{Z}_{\ge 1}$ with $\mathbb{E}_-[u] = \frac{9}{8}$ and $\mathbb{E}_-[v] = \frac{3}{2}$, giving $\mathbb{E}_-[-X] = (3 \cdot \frac{9}{8} + 2 \cdot \frac{3}{2})\ln 2 - (2 \cdot \frac{9}{8} + \frac{3}{2})\ln 3 = \frac{51}{8}\ln 2 - \frac{15}{4}\ln 3 > 0$. Any word in $\mathcal{E}_{L-1}^- \setminus \mathcal{E}_L^-$ satisfies $W_L := \sum_{j=1}^L (-X(\beta_j)) < 0$ (since $\theta \notin \mathbb{Q}$). Because $\tilde t_* = -(1 + \vartheta_*) < -14 < 0$ lies strictly in $(-\infty, 0) \cap I_-$, Markov's inequality on $\mathbf{1}_{\{W_L \le 0\}} \le e^{\tilde t_* W_L}$ yields
$$
0 < P_{L-1}^- - P_L^- \le \mathbb{P}_-^{\otimes L}(W_L \le 0) \le \bigl(16\,M_-^{\mathrm{unnorm}}(\tilde t_*)\bigr)^L = \rho_-^L.
$$
Summing over $L > J$ bounds $P_J^- - P_\infty^- \le \frac{\rho_-^{J+1}}{1 - \rho_-}$, which at $J = 12$ is at most $3.76 \times 10^{-12}$.

**(3)** For the upper bound, $w_+ \in \mathcal{E}_L^+$ implies $Z_L := \sum_{j=1}^L X(\alpha_j) > 0$, so $\Sigma_+^e(L) \le \sum_{w_+} 2^{-S_+(w_+)} e^{\vartheta_* Z_L} = M_*^L$. For the matching lower bound via elementary inequalities, fix any $t_1 \in (\vartheta_*, \sup I_+)$ and define the tilted i.i.d. law $\mathbb{Q}_{t_1}(u, v) := 2^{-(3u+2v)} e^{t_1 X(u,v)} / M_+^{\mathrm{unnorm}}(t_1)$ on $\mathbb{Z}_{\ge 1}^2$. By strict convexity of $\ln M_+^{\mathrm{unnorm}}$, $\mu_1 := \mathbb{E}_{\mathbb{Q}_{t_1}}[X] = (M_+^{\mathrm{unnorm}})'(t_1)/M_+^{\mathrm{unnorm}}(t_1) > 0$, $\sigma_1^2 := \mathrm{Var}_{\mathbb{Q}_{t_1}}(X) < \infty$, and $r_1 := \mathbb{E}_{\mathbb{Q}_{t_1}}[e^{-(t_1 - \vartheta_*)X}] = M_*/M_+^{\mathrm{unnorm}}(t_1) < 1$. Since $X(3, 1) = 7\ln 3 - 11\ln 2 > 0$, choose $m \ge 1$ such that $H_m := m X(3, 1)$ satisfies $e^{-(t_1 - \vartheta_*) H_m} / (1 - r_1) \le \frac{1}{4}$ (at the concrete certified witness $t_1 = 27/2$ and $m = 512$, `cramer_saddles.super_saddle` gives $H_{512} \in [33.621521, 33.621522]$ and ruin bound $\in [0.0341068, 0.0341069] < \frac{1}{4}$). On words $w_+ = (3, 1)^m \tilde w$ of length $L > m$, all first $m$ partial sums are positive, and union-bounding Markov's inequality over $1 \le k \le L - m$ shows $\mathbb{Q}_{t_1}^{\otimes(L-m)}(\exists k: H_m + \sum_{j=1}^k X(\tilde\alpha_j) \le 0) \le \sum_{k=1}^{L-m} e^{-(t_1 - \vartheta_*) H_m} r_1^k < \frac{1}{4}$. Simultaneously, Chebyshev's inequality gives $\mathbb{Q}_{t_1}^{\otimes(L-m)}(|\sum_{j=1}^{L-m} X(\tilde\alpha_j) - (L-m)\mu_1| > 2\sigma_1 \sqrt{L-m}) \le \frac{1}{4}$, leaving an event $\mathcal{G}_{L,m}$ of $\mathbb{Q}_{t_1}^{\otimes(L-m)}$-probability $\ge \frac{1}{2}$ with $(3, 1)^m \times \mathcal{G}_{L,m} \subset \mathcal{E}_L^+$ and $Z_L \le H_m + (L-m)\mu_1 + 2\sigma_1 \sqrt{L-m}$. Undoing the tilt gives
$$
\Sigma_+^e(L) \ge \frac{1}{2}\, 2^{-11m} M_+^{\mathrm{unnorm}}(t_1)^{L-m} e^{-t_1((L-m)\mu_1 + 2\sigma_1\sqrt{L-m})}.
$$
Taking $L$-th roots as $L \to \infty$ gives $\liminf_{L\to\infty} \Sigma_+^e(L)^{1/L} \ge M_+^{\mathrm{unnorm}}(t_1) e^{-t_1 \mu_1}$, and letting $t_1 \downarrow \vartheta_*$ ($\mu_1 \to 0$) yields $\lim_{L\to\infty} \Sigma_+^e(L)^{1/L} = M_*$.

Finally, deterministic forward/backward circuit parsing (`phi` and `phi_inverse`) makes the cylinder realizations $(w_-, w_+) \in \mathcal{E}_L^- \times \mathcal{E}_L^+$ pairwise disjoint on $\mathcal{T}_2^e(L)$. Every $Q \equiv r(w_-, w_+) \pmod{24 \cdot 2^{S_+} 3^{R_-}}$ with $Q \ge Q_{\mathrm{thr}}(w_-)$ belongs to $\mathcal{T}_2^e(L)$ (and even if accidental state collisions $Q_i = Q_j$ for $i \neq j$ are monitored, distinct $\{2,3\}$-slopes $3^R/2^S$ allow at most $\binom{2L+1}{2}$ integer solutions per cylinder), so each cylinder has natural density $(24 \cdot 2^{S_+} 3^{R_-})^{-1}$. Conversely, any $Q \in \mathcal{T}_2^e(L) \cap [1, N]$ has $S_+ \le C_L \log_2(6N + 1)$ and $R_- \le C'_L \log_3(6N + 1)$ by open-window height bounds ([5, Equation (10)]), so cylinders with $\max(S_+, R_-) > K$ vanish identically on $[1, N]$ unless $K \ll_L \log N$, and their density tail above $K$ is bounded by $\Sigma_-^e(L)\Sigma_+^e(L)$'s convergent tail. Letting $N \to \infty$ and $K \to \infty$ gives $d_{\mathrm{nat}}(\mathcal{T}_2^e(L)) = \frac{1}{24}\Sigma_-^e(L)\Sigma_+^e(L)$ and $\lim_{L\to\infty} d_{\mathrm{nat}}(\mathcal{T}_2^e(L))^{-1/L} = 16/M_*$. $\square$

| Depth $L$ | $P_L^- = 16^L \Sigma_-^e(L)$ | Drop $P_{L-1}^- - P_L^-$ | $\Sigma_+^e(L)$ | Stretch inverse density $(\Sigma_-^e(L)\Sigma_+^e(L))^{-1}$ | Minimal shell $S_{\min}^+(L)$ ($\Delta S_{\min}^+$) |
|---:|---:|---:|---:|---:|---:|
| $1$ | $0.991735661599$ | $8.2643 \times 10^{-3}$ | $5.602166 \times 10^{-4}$ | $2.879838 \times 10^{4}$ | $11$ ($+11$) |
| $2$ | $0.990650315956$ | $1.0853 \times 10^{-3}$ | $4.679937 \times 10^{-6}$ | $5.521786 \times 10^{7}$ | $19$ ($+8$) |
| $3$ | $0.990629936974$ | $2.0379 \times 10^{-5}$ | $1.053117 \times 10^{-8}$ | $3.926196 \times 10^{11}$ | $30$ ($+11$) |
| $4$ | $0.990624956927$ | $4.9800 \times 10^{-6}$ | $1.087313 \times 10^{-10}$ | $6.084376 \times 10^{14}$ | $38$ ($+8$) |
| $5$ | $0.990624823707$ | $1.3322 \times 10^{-7}$ | $3.181341 \times 10^{-13}$ | $3.327212 \times 10^{18}$ | $49$ ($+11$) |
| $6$ | $0.990624786602$ | $3.7105 \times 10^{-8}$ | $3.501928 \times 10^{-15}$ | $4.836192 \times 10^{21}$ | $57$ ($+8$) |
| $7$ | $0.990624785455$ | $1.1473 \times 10^{-9}$ | $1.156075 \times 10^{-17}$ | $2.343931 \times 10^{25}$ | $68$ ($+11$) |
| $8$ | $0.990624785095$ | $3.5938 \times 10^{-10}$ | $1.366376 \times 10^{-19}$ | $3.173077 \times 10^{28}$ | $76$ ($+8$) |
| $12$ | $0.990624785000$ | $3.0586 \times 10^{-14}$ | $2.841028 \times 10^{-28}$ | $1.000127 \times 10^{42}$ | $114$ ($+11$) |

*Table 1: Certified backward survival probabilities $P_L^-$, survival drops $P_{L-1}^- - P_L^- \le \rho_-^L$, forward eligible sums $\Sigma_+^e(L)$, stretch-progression inverse cylinder densities $(\Sigma_-^e(L)\Sigma_+^e(L))^{-1}$ (with global $\mathbb{Z}_{\ge 1}$ inverse natural density $d_{\mathrm{nat}}(\mathcal{T}_2^e(L))^{-1} = 24(\Sigma_-^e(L)\Sigma_+^e(L))^{-1}$), and minimal eligible forward halving shells $S_{\min}^+(L)$ (`twosided_trough_results.json`, `forward_density_exponent_cap = 520`, `backward_density_exponent_cap = 360`, exact geometric tails `< 10^{-29}`).*

![Certified two-sided trough minima through depth 7, depth-8 exclusion/witness bracket, inverse union-density trajectory, and backward 3-adic survival drop](supplement/figure-1.png)

*Remark 2.1 (Why $16/M_* \approx 1{,}957.75$ replaces $122.36^2 \approx 1.5 \times 10^4$, and the $\{8, 11\}$ sawtooth).* Under $\mathbb{P}_+$, the forward walk has negative drift $\mathbb{E}_+[X] = \frac{23}{21}\ln 3 - 2\ln 2 \approx -0.1823 < 0$, so staying above $0$ incurs exponential Cramér decay $\rho_+ = 21 M_* \approx 0.171626$ per step ($M_*^{-1} \approx 122.3592$). Under $\mathbb{P}_-$, by contrast, the Esscher tilt $e^{-X}$ flips the drift to $+\frac{51}{8}\ln 2 - \frac{15}{4}\ln 3 \approx +0.299017 > 0$, so $P_L^-$ converges to $P_\infty^- \approx 0.990624785 > 99\%$, contributing the unattenuated $3$-adic branching factor $16^{-L}$ up to a fixed multiplicative constant. Furthermore, the minimal forward halving sum $S_{\min}^+(L) = \min_{w_+ \in \mathcal{E}_L^+} S_+(w_+)$ advances by $\Delta S_{\min}^+(L) = (11, 8, 11, 8, 11, 8, 11, 8, 8, 11, 8, 11)$ for $L = 1 \ldots 12$ (`minimal_shell_steps`), alternating between $(3, 1)$ increments ($+11$) and $(2, 1)$ increments ($+8$) along the Christoffel word of $\log_2 3$ [10]. This alternation directly drives both the step-ratio oscillation of $d_{\mathrm{nat}}(\mathcal{T}_2^e(L))^{-1}$ ($\approx 1{,}453.5\times$ at $L = 5 \to 6$ vs. $\approx 4{,}846.6\times$ at $L = 6 \to 7$) and the observed dip-and-rebound in $Q_{\min,2}(L)$ ($114.08\times$ at $L = 5 \to 6$ followed by $119{,}241.22\times$ at $L = 6 \to 7$; Figure 1a).

---

## 3. Catalan $\{2, 3\}$-Unit Dimer Commutators and Pairwise Swap Repulsion

### 3.1 Exact $\{2, 3\}$-Unit Affine Commutators

To bound integer separation between distinct cylinders sharing the same modulus, let $w = w_{\mathrm{pre}}\,\gamma\,\delta\,w_{\mathrm{suf}}$ and $w' = w_{\mathrm{pre}}\,\delta\,\gamma\,w_{\mathrm{suf}}$ swap adjacent circuits $\gamma, \delta$ at index $j \in \{0, \ldots, L - 2\}$ ($0$-indexed, with prefix totals $(R_{\mathrm{pre}}, S_{\mathrm{pre}})$ on $w_{\mathrm{pre}}$). Writing $N_+(\gamma, \delta) := (a_\delta - b_\delta)c_\gamma - (a_\gamma - b_\gamma)c_\delta$, the two-step forward constant-term difference $\Delta_+(\gamma, \delta) := \Phi_{\gamma\delta}(0) - \Phi_{\delta\gamma}(0) = N_+(\gamma, \delta)/(b_\gamma b_\delta)$ and outward backward constant-term difference $\Delta_-(\gamma, \delta) := \Phi_{\gamma\delta}^{-1}(0) - \Phi_{\delta\gamma}^{-1}(0) = N_+(\gamma, \delta)/(a_\gamma a_\delta)$ normally contain composite prime divisors. On **Family I** ($\gamma = (u, 1), \delta = (u + 1, 1)$, $u \ge 1$) and **Family II** ($\gamma = (1, v), \delta = (1, v + 1)$, $v \ge 1$), however, Catalan's identities $3^2 - 2^3 = 1$ and $2^2 - 3^1 = 1$ annihilate the quadratic terms:
$$
N_+\bigl((u, 1), (u+1, 1)\bigr) = (27\cdot 9^u - 32\cdot 8^u)\cdot 3(9^u - 8^u) - (3\cdot 9^u - 4\cdot 8^u)\cdot 3(9\cdot 9^u - 8\cdot 8^u) = +2^{3u} 3^{2u+1},
$$
$$
N_+\bigl((1, v), (1, v+1)\bigr) = (27\cdot 3^v - 32\cdot 4^v)3^v - (9\cdot 3^v - 8\cdot 4^v)\cdot 3\cdot 3^v = -2^{2v+3} 3^v.
$$

*Concrete depth-$2$ backward sign check.* Take $w_- = ((1, 1), (1, 2))$ and $w'_- = ((1, 2), (1, 1))$ ($j = 0$, $v = 1$, $R_- = 7$, $S_- = 12$, $S_{\mathrm{pre}} = R_{\mathrm{pre}} = 0$, modulus $24 \cdot 3^7 = 52{,}488$). Composing outward inverse maps gives $\Phi_{w_-}^{-1}(Q) = (4096 Q - 627)/2187$ with $r_-(w_-) = 1{,}815$, and $\Phi_{w'_-}^{-1}(Q) = (4096 Q - 531)/2187$ with $r_-(w'_-) = 42{,}975$, so $D := r_-(w'_-) - r_-(w_-) = +41{,}160 = 8 \cdot 3 \cdot 1{,}715$. Pulling back $0 \pmod 3$ across $3^{R_-}$ gives $4096 D \equiv 531 - 627 = -96 = -3 \cdot 2^5 \pmod{3^8}$, and dividing by the unit $2^5$ modulo $3^8$ yields $2^7 D = 5{,}268{,}480 = 803 \cdot 3^8 - 3 \equiv -3^1 \pmod{3^8}$.

### 3.2 Theorem 2: Effective Subspace-Free Swap Repulsion and Two-Sided Ridout Separation

**Theorem 2 (Catalan $\{2, 3\}$-Unit Commutators, 100% Effective Swap Repulsion, and Two-Sided Ridout Separation).**
1. *(Exact signed swap congruences.)* For every $u, v \ge 1$,
   $$
   \Delta_+\bigl((u, 1), (u+1, 1)\bigr) = +\frac{3^{2u+1}}{2^{3u+7}}, \qquad \Delta_-\bigl((u, 1), (u+1, 1)\bigr) = +\frac{2^{3u}}{3^{2u+3}},
   $$
   $$
   \Delta_+\bigl((1, v), (1, v+1)\bigr) = -\frac{3^v}{2^{2v+5}}, \qquad \Delta_-\bigl((1, v), (1, v+1)\bigr) = -\frac{2^{2v+3}}{3^{v+5}}.
   $$
   Consequently, if $w = w_{\mathrm{pre}}\,\gamma\,\delta\,w_{\mathrm{suf}}$ and $w' = w_{\mathrm{pre}}\,\delta\,\gamma\,w_{\mathrm{suf}}$ swap adjacent circuits at index $j$ with prefix totals $(R_{\mathrm{pre}}, S_{\mathrm{pre}})$, then any cylinder representatives $Q_w, Q_{w'}$ ($D := Q_{w'} - Q_w$) satisfy:
   - *Forward Family I ($\gamma = (u, 1), \delta = (u + 1, 1)$):* $3 \mid D$ and $3^{R_{\mathrm{pre}} + 2u + 3} D \equiv +2^{S_{\mathrm{pre}} + 3u} \pmod{2^{S_+ + 3}}$, hence $2^{S_{\mathrm{pre}} + 3u} \parallel D$ and
     $$
     |D| \ge B_{\mathrm{eff}}^+(w, j) := \max\!\left(3 \cdot 2^{S_{\mathrm{pre}} + 3u},\ \left\lceil \frac{2^{S_+ + 3} - 2^{S_{\mathrm{pre}} + 3u}}{3^{R_{\mathrm{pre}} + 2u + 3}} \right\rceil\right).
     $$
   - *Outward Backward Family II ($\gamma = (1, v), \delta = (1, v + 1)$):* $8 \mid D$ and $2^{S_{\mathrm{pre}} + 2v + 5} D \equiv -3^{R_{\mathrm{pre}} + v} \pmod{3^{R_- + 1}}$, hence $3^{R_{\mathrm{pre}} + v} \parallel D$ and
     $$
     |D| \ge B_{\mathrm{eff}}^-(w, j) := \max\!\left(8 \cdot 3^{R_{\mathrm{pre}} + v},\ \left\lceil \frac{3^{R_- + 1} - 3^{R_{\mathrm{pre}} + v}}{2^{S_{\mathrm{pre}} + 2v + 5}} \right\rceil\right).
     $$
2. *(Closed-form 100% effective all-$L$ separation on minimal alphabets.)* On the forward Sturmian alphabet $\mathcal{B}_+ = \{(2, 1), (3, 1)\}^L$ ($L \ge 2$), every adjacent swap $(2, 1) \leftrightarrow (3, 1)$ satisfies
   $$
   |Q_{w'} - Q_w| \ge 2^{\gamma_+ S_+(w) + c_+}, \qquad \gamma_+ := \frac{1}{1 + \frac{7}{11}\theta} \in [0.497856107024886624,\ 0.497856107024886625] > \frac{9957}{20000},
   $$
   with explicit constant $c_+ \in [-0.221282863247299782, -0.221282863247299781]$. Dually, on the outward backward alphabet $\mathcal{B}_- = \{(1, 1), (1, 2)\}^L$ ($L \ge 2$), every adjacent swap $(1, 1) \leftrightarrow (1, 2)$ satisfies
   $$
   |Q_{w'} - Q_w| \ge 3^{\gamma_- R_-(w) + c_-}, \qquad \gamma_- := \frac{1}{1 + \frac{7}{4\theta}} \in [0.475256468514540130,\ 0.475256468514540131] > \frac{1901}{4000},
   $$
   with explicit constant $c_- \in [-0.105943054030886229, -0.105943054030886228]$.
3. *(Joined two-sided Ridout separation — ineffective.)* Fixing $w_-$ and swapping $(u, 1) \leftrightarrow (u + 1, 1)$ in $w_+$ (with $u \le u_0$) forces $24 \cdot 3^{R_-} \mid D$ in addition to $3^{R_{\mathrm{pre}} + 2u + 3} D \equiv +2^{S_{\mathrm{pre}} + 3u} \pmod{2^{S_+ + 3}}$; symmetrically, fixing $w_+$ and swapping $(1, v) \leftrightarrow (1, v + 1)$ in $w_-$ (with $v \le v_0$) forces $24 \cdot 2^{S_+} \mid D$ in addition to $2^{S_{\mathrm{pre}} + 2v + 5} D \equiv -3^{R_{\mathrm{pre}} + v} \pmod{3^{R_- + 1}}$. By Ridout's theorem [14] at $\{\infty, 2, 3\}$, for every $\varepsilon > 0$ there exists an *ineffective* constant $C_{\varepsilon,u_0,v_0} > 0$ such that every joined swap pair satisfies $|Q_{w'} - Q_w| \ge C_{\varepsilon,u_0,v_0} (2^{S_+} 3^{R_-})^{1-\varepsilon}$.

*Proof.*
**(1)** Composing $w_{\mathrm{pre}}$ ($Q \mapsto (3^{R_{\mathrm{pre}}} Q + C_{\mathrm{pre}})/2^{S_{\mathrm{pre}}}$), the two-step block, and $w_{\mathrm{suf}}$ ($Q \mapsto (3^{R_{\mathrm{suf}}} Q + C_{\mathrm{suf}})/2^{S_{\mathrm{suf}}}$) shifts $\Phi_w(0) - \Phi_{w'}(0)$ by $3^{R_{\mathrm{suf}}} \Delta_+(\gamma, \delta) / 2^{S_{\mathrm{suf}}}$. Pulling back $7 \pmod 8$ gives $3^{R_+} (Q_{w'} - Q_w) \equiv 2^{S_+} (\Phi_w(0) - \Phi_{w'}(0)) \pmod{2^{S_+ + 3}}$; for Family I, $2^{S_+} \cdot 3^{R_{\mathrm{suf}}} \frac{3^{2u+1}}{2^{3u+7} 2^{S_{\mathrm{suf}}}} = 2^{S_{\mathrm{pre}} + 3u} 3^{R_{\mathrm{suf}} + 2u + 1}$ (since $S_+ - S_{\mathrm{suf}} - (3u + 7) = S_{\mathrm{pre}} + (6u + 7) - 3u - 7 = S_{\mathrm{pre}} + 3u$), and dividing by the unit $3^{R_{\mathrm{suf}} - 2}$ modulo $2^{S_+ + 3}$ gives $3^{R_{\mathrm{pre}} + 2u + 3} D \equiv +2^{S_{\mathrm{pre}} + 3u} \pmod{2^{S_+ + 3}}$. Since $S_{\mathrm{pre}} + 3u \le S_+ - 3(u + 1) - 4 < S_+ + 3$, $2^{S_{\mathrm{pre}} + 3u} \parallel D$; moreover, $3^{R_{\mathrm{pre}} + 2u + 3} D = +2^{S_{\mathrm{pre}} + 3u}$ is impossible in $\mathbb{Z}$ because $3^{R_{\mathrm{pre}} + 2u + 3} > 1$ is odd, so $|3^{R_{\mathrm{pre}} + 2u + 3} D| \ge 2^{S_+ + 3} - 2^{S_{\mathrm{pre}} + 3u}$, establishing $B_{\mathrm{eff}}^+$. Outward backward Family II follows symmetrically from $\Phi_{w_-}^{-1}(0) - \Phi_{w'_-}^{-1}(0) = 2^{S_{\mathrm{suf}}} \Delta_-(\gamma, \delta) / 3^{R_{\mathrm{suf}}}$: since $R(1, v) + R(1, v + 1) = 2v + 5$ and $S(1, v) + S(1, v + 1) = 4v + 8$, pulling back $0 \pmod 3$ modulo $3^{R_- + 1}$ yields $2^{S_-} D \equiv 3^{R_-}(\Phi_{w_-}^{-1}(0) - \Phi_{w'_-}^{-1}(0)) = -2^{S_{\mathrm{suf}} + 2v + 3} 3^{R_{\mathrm{pre}} + v} \pmod{3^{R_- + 1}}$. Dividing by the unit $2^{S_{\mathrm{suf}} + 2v + 3}$ modulo $3^{R_- + 1}$ (using $S_- - (S_{\mathrm{suf}} + 2v + 3) = S_{\mathrm{pre}} + 2v + 5$) gives $2^{S_{\mathrm{pre}} + 2v + 5} D \equiv -3^{R_{\mathrm{pre}} + v} \pmod{3^{R_- + 1}}$ (`swap_parameters` in `twosided_theory_cert.py`), and $|2^{S_{\mathrm{pre}} + 2v + 5} D| \ge 3^{R_- + 1} - 3^{R_{\mathrm{pre}} + v}$ because $2^{S_{\mathrm{pre}} + 2v + 5} D = -3^{R_{\mathrm{pre}} + v}$ is impossible in $\mathbb{Z}$ ($2 \nmid 3^{R_{\mathrm{pre}} + v}$), establishing $B_{\mathrm{eff}}^-$.

**(2)** On $\mathcal{B}_+ = \{(2, 1), (3, 1)\}^L$ ($u = 2$, $L \ge 2$), every prefix letter satisfies $\frac{R}{S} \le \max(\frac{5}{8}, \frac{7}{11}) = \frac{7}{11}$, so $R_{\mathrm{pre}} \le \frac{7}{11} S_{\mathrm{pre}}$, and $(S_+ + 3) - (S_{\mathrm{pre}} + 6) \ge 22 - 6 = 16$. Taking a geometric weighted average with weight $1 - \gamma_+$ on $3 \cdot 2^{S_{\mathrm{pre}} + 6}$ and weight $\gamma_+$ on $(1 - 2^{-16}) 2^{S_+ + 3} 3^{-(R_{\mathrm{pre}} + 7)} \ge (1 - 2^{-16}) 2^{S_+ + 3 - \theta(\frac{7}{11} S_{\mathrm{pre}} + 7)}$ cancels $S_{\mathrm{pre}}$ identically because $(1 - \gamma_+) - \gamma_+ \frac{7}{11}\theta = 0 \iff \gamma_+ = (1 + \frac{7}{11}\theta)^{-1}$. Using $6(1 - \gamma_+) - 7\theta\gamma_+ = -\frac{35}{11}\theta\gamma_+$, this yields $|D| \ge 2^{\gamma_+ S_+ + c_+}$ with $c_+ = \gamma_+(3 - \frac{35}{11}\theta + \log_2(1 - 2^{-16})) + (1 - \gamma_+)\log_2 3$ (`repulsion_audit` in `twosided_theory_cert.py`). Dually, on $\mathcal{B}_- = \{(1, 1), (1, 2)\}^L$ ($v = 1$, $L \ge 2$), every letter satisfies $\frac{S}{R} \le \max(\frac{5}{3}, \frac{7}{4}) = \frac{7}{4}$ and $(R_- + 1) - (R_{\mathrm{pre}} + 1) \ge 7$; weighting $8 \cdot 3^{R_{\mathrm{pre}} + 1}$ by $1 - \gamma_-$ and $(1 - 3^{-7}) 3^{R_- + 1} 2^{-(S_{\mathrm{pre}} + 7)}$ by $\gamma_- = (1 + \frac{7}{4\theta})^{-1}$ gives $|D| \ge 3^{\gamma_- R_- + c_-}$ with $c_- = \gamma_-(1 - \frac{21}{4\theta} + \log_3(1 - 3^{-7})) + (1 - \gamma_-)\log_3 8$.

**(3)** For a joined forward swap ($w_-$ fixed, $(u, 1) \leftrightarrow (u + 1, 1)$ swapped in $w_+$), $Q_{w'} \equiv Q_w \equiv r_-(w_-) \pmod{24 \cdot 3^{R_-}}$ gives $24 \cdot 3^{R_-} \mid D$, while $2^{S_{\mathrm{pre}} + 3u} \parallel D$ (note $3u \ge 3$ for all $u \ge 1$, so $8 \mid 2^{S_{\mathrm{pre}} + 3u}$ automatically) forces $2^{S_{\mathrm{pre}} + 3u} 3^{R_- + 1} \mid D$. Moreover, $3^{R_{\mathrm{pre}} + 2u + 3} D - 2^{S_{\mathrm{pre}} + 3u} = 2^{S_+ + 3} M$ for a nonzero integer $M$. Dividing $3^{R_{\mathrm{pre}} + 2u + 3} D - 2^{S_+ + 3} M = 2^{S_{\mathrm{pre}} + 3u}$ by $g := \gcd(3^{R_{\mathrm{pre}} + 2u + 3} D, 2^{S_+ + 3} M) = 2^{S_{\mathrm{pre}} + 3u}$ produces coprime integers $U - V = 1$ with $3^{R_- + R_{\mathrm{pre}} + 2u + 4} \mid U$ and $2^{S_+ + 3 - S_{\mathrm{pre}} - 3u} \mid V$. Applying Ridout's theorem [14] on $\mathbb{P}^1 \setminus \{0, 1, \infty\}$ gives $\max(U, V) \ge c_\varepsilon (2^{S_+ - S_{\mathrm{pre}} - 3u} 3^{R_- + R_{\mathrm{pre}}})^{1-\varepsilon}$, so $|D| = 2^{S_{\mathrm{pre}} + 3u} U / 3^{R_{\mathrm{pre}} + 2u + 3} \ge C_{\varepsilon,u_0} (2^{S_+} 3^{R_-})^{1-\varepsilon}$. The backward joined swap is completely symmetric. $\square$

| Depth $L$ | Fam. I $\min \frac{\log_2 |D|}{S_+}$ | Fam. I $\min \frac{\log_2 B_{\mathrm{eff}}^+}{S_+}$ | Closed-form $\gamma_+ + \frac{c_+}{S_{\max}^+}$ | Fam. II $\min \frac{\log_3 |D|}{R_-}$ | Fam. II $\min \frac{\log_3 B_{\mathrm{eff}}^-}{R_-}$ | Closed-form $\gamma_- + \frac{c_-}{R_{\max}^-}$ |
|---:|---:|---:|---:|---:|---:|---:|
| $2$ | $0.997923$ | $0.573968$ | $0.486210$ | $1.381642$ | $0.513797$ | $0.460122$ |
| $3$ | $1.041429$ | $0.577221$ | $0.489660$ | $1.031289$ | $0.589279$ | $0.464662$ |
| $4$ | $0.974446$ | $0.495014$ | $0.491534$ | $1.053035$ | $0.477814$ | $0.467107$ |
| $5$ | $0.981825$ | $0.512717$ | $0.492710$ | $0.920790$ | $0.523105$ | $0.468635$ |
| $6$ | $0.950415$ | $0.495263$ | $0.493517$ | $0.922499$ | $0.473600$ | $0.469681$ |
| $7$ | $0.943413$ | $0.508602$ | $0.494106$ | $0.948183$ | $0.489603$ | $0.470441$ |
| $8$ | $0.973928$ | $0.495379$ | $0.494553$ | $0.915313$ | $0.477511$ | $0.471019$ |
| $9$ | $0.962697$ | $0.506162$ | $0.494906$ | $0.929263$ | $0.479186$ | $0.471473$ |

*Table 2: Exhaustive adjacent-swap cylinder repulsion on $\mathcal{B}_+ = \{(2, 1), (3, 1)\}^L$ (Family I, base $2$) and $\mathcal{B}_- = \{(1, 1), (1, 2)\}^L$ (Family II, base $3$) across depths $2 \le L \le 9$ (`repulsion.binary_depth_profile`), comparing empirical minimum cylinder gaps against $B_{\mathrm{eff}}^\pm$ and the closed-form Theorem 2(2) lower bounds converging to $\gamma_+ \approx 0.497856$ and $\gamma_- \approx 0.475256$. All `2,504` joined two-sided swap pairs across $2 \le L \le 5$ (`joined_pair_counts`) are also audited directly.*

![Adjacent-swap cylinder repulsion across depths 2 through 9 and open-prefix non-eligible exclusion horizons](supplement/figure-2.png)

---

## 4. Two-Sided Fixed-Point Sign Separation and Bi-Adic Coupling Floors

Why does coupling a backward word $w_-$ to a forward word $w_+$ force $Q$ so much higher than $\max(2^{S_+}, 3^{R_-})$ on structured words? Each single-circuit affine map $\Phi_\gamma(Q) = (a_\gamma Q + c_\gamma)/b_\gamma$ ($a_\gamma = 3^{2u+v} \neq b_\gamma = 2^{3u+2v}$, $c_\gamma = 3^v(9^u - 8^u) > 0$) has a unique rational fixed point
$$
q_\gamma := \frac{c_\gamma}{b_\gamma - a_\gamma} = -\frac{c_\gamma}{a_\gamma - b_\gamma}, \qquad \Phi_\gamma(Q) - q_\gamma = \frac{a_\gamma}{b_\gamma}(Q - q_\gamma), \qquad \Phi_\gamma^{-1}(Q) - q_\gamma = \frac{b_\gamma}{a_\gamma}(Q - q_\gamma).
$$
Crucially, forward-eligible and backward-eligible letters place their fixed points on **opposite sides of zero**.

**Theorem 3 (Two-Sided Fixed-Point Sign Separation and Homogeneous Bi-Adic Ridout Floor).**
1. *(Strict opposite-sign fixed-point separation and power threshold invariance.)* For every forward-eligible letter $\alpha$ ($a_\alpha > b_\alpha$), $q_\alpha = -c_\alpha/(a_\alpha - b_\alpha) < 0$. For every backward-eligible letter $\beta$ ($b_\beta > a_\beta$), $q_\beta = +c_\beta/(b_\beta - a_\beta) > 0$, and for every $n \ge 1$,
   $$
   \Phi_\beta^{-n}(Q) - Q = \left(\left(\frac{b_\beta}{a_\beta}\right)^n - 1\right)(Q - q_\beta),
   $$
   so $\Phi_\beta^{-n}(Q) > Q$ holds if and only if $Q > q_\beta$, with $n$-independent backward threshold $Q_{\mathrm{thr}}(\beta^n) = \max(15, \lfloor q_\beta \rfloor + 1)$. Consequently, on every two-sided trough centre $Q$ with outer boundary letters $\beta_1 \in \mathcal{E}_1^-$ and $\alpha_1 \in \mathcal{E}_1^+$,
   $$
   q_{\alpha_1} < 0 < q_{\beta_1} < Q.
   $$
2. *(Homogeneous bi-adic Ridout floor — ineffective.)* Fix any $\beta \in \mathcal{E}_1^-$ and $\alpha \in \mathcal{E}_1^+$, and write $q_\alpha = n_\alpha / d_\alpha$ and $q_\beta = n_\beta / d_\beta$ in lowest terms ($d_\alpha, d_\beta \ge 1$). On any homogeneous two-sided window $(w_-, w_+) = (\beta^{L_-}, \alpha^{L_+})$ ($L_-, L_+ \ge 1$) with step totals $(R_-, S_-)$ and $(R_+, S_+)$, every integer representative $Q \in \mathcal{T}_2^e(\beta^{L_-}, \alpha^{L_+})$ satisfies the nonzero linear identity
   $$
   A - B = K_{\alpha,\beta} := d_\alpha n_\beta - d_\beta n_\alpha > 0, \qquad A := d_\beta(d_\alpha Q - n_\alpha) > 0,\quad B := d_\alpha(d_\beta Q - n_\beta) > 0,
   $$
   with $2^{S_+} \mid A$ and $3^{R_-} \mid B$. Hence for every $\varepsilon > 0$ there exists an *ineffective* constant $C_{\alpha,\beta,\varepsilon} > 0$ (depending only on $\alpha, \beta, \varepsilon$) such that
   $$
   Q \ge C_{\alpha,\beta,\varepsilon}\,\bigl(2^{S_+} 3^{R_-}\bigr)^{1-\varepsilon}.
   $$

*Proof.*
**(1)** Since $c_\gamma = 3^v(9^u - 8^u) > 0$ for all $u, v \ge 1$, $q_\gamma = c_\gamma / (b_\gamma - a_\gamma)$ has the exact sign of $b_\gamma - a_\gamma$. Iterating $\Phi_\beta^{-1}(Q) - q_\beta = (b_\beta/a_\beta)(Q - q_\beta)$ gives $\Phi_\beta^{-n}(Q) - q_\beta = (b_\beta/a_\beta)^n (Q - q_\beta)$, and subtracting $Q - q_\beta$ gives the exact identity for $\Phi_\beta^{-n}(Q) - Q$; since $(b_\beta/a_\beta)^n > 1$, positivity is equivalent to $Q > q_\beta$.

**(2)** Along $\alpha^{L_+}$, $Q_{L_+} - q_\alpha = (3^{R_+}/2^{S_+})(Q - q_\alpha)$ gives $d_\alpha Q_{L_+} - n_\alpha = (3^{R_+}/2^{S_+})(d_\alpha Q - n_\alpha) \in \mathbb{Z}$; since $\gcd(3^{R_+}, 2^{S_+}) = 1$, $2^{S_+} \mid (d_\alpha Q - n_\alpha) \mid A$. Along $\beta^{L_-}$, $d_\beta Q_{-L_-} - n_\beta = (2^{S_-}/3^{R_-})(d_\beta Q - n_\beta) \in \mathbb{Z}$ gives $3^{R_-} \mid (d_\beta Q - n_\beta) \mid B$. Because $q_\alpha < 0 < q_\beta < Q$, both $A > 0$ and $B > 0$, while $A - B = d_\alpha n_\beta - d_\beta n_\alpha = d_\alpha d_\beta (q_\beta - q_\alpha) = K_{\alpha,\beta} > 0$ is a fixed positive integer (for $\beta = (1, 1)$ with $q_{(1,1)} = 3/5$ and $\alpha = (3, 1)$ with $q_{(3,1)} = -651/139$, $K_{\alpha,\beta} = 139 \cdot 3 - 5 \cdot (-651) = 3{,}672$, audited across $1 \le L \le 6$ in `block_junctions.one_block_witnesses`). Dividing by $g := \gcd(A, B) \ge 1$ (which satisfies $g \mid K_{\alpha,\beta}$) yields coprime positive integers $A' = A/g$ and $B' = B/g$ with $A' - B' = K' := K_{\alpha,\beta}/g \in [1, K_{\alpha,\beta}]$, $\operatorname{ord}_2(A') \ge S_+ - v_2(K_{\alpha,\beta})$, and $\operatorname{ord}_3(B') \ge R_- - v_3(K_{\alpha,\beta})$. Applying Ridout's theorem [14] to the rational approximation $B'/A' = 1 - K'/A'$ to $1$ at $\{\infty, 2, 3\}$ gives $(2^{S_+ - v_2(K_{\alpha,\beta})} 3^{R_- - v_3(K_{\alpha,\beta})})/A' \ll_{\alpha,\beta,\varepsilon} (A')^\varepsilon$, i.e., $A \ge A' \gg_{\alpha,\beta,\varepsilon} (2^{S_+} 3^{R_-})^{1-\varepsilon}$, and $Q > A/(d_\alpha d_\beta) + q_\alpha$ yields the claim. $\square$

*Remark 4.1 (Scope on multi-block junctions).* For multi-block words $(\beta_1^{m_1} \cdots \beta_{k_-}^{m_{k_-}}, \alpha_1^{n_1} \cdots \alpha_{k_+}^{n_{k_+}})$, telescoping around successive fixed points $q_{\beta_r}, q_{\alpha_s}$ produces a $(k_- + k_+ + 1)$-term $S$-unit linear form whose internal block-switch coefficients grow with the intermediate exponents unless the switch ratios are bounded; accordingly, Theorem 3(2) states the $(2^{S_+} 3^{R_-})^{1-\varepsilon}$ bound strictly for homogeneous $1$-block junctions, while Proposition A.1 in Appendix A.2 proves unconditionally via an exact $2$-adic valuation staircase that **zero** proper subsums vanish for *arbitrary* block counts $(k_-, k_+)$ and *arbitrary* block lengths on $\mathcal{B}_- \times \mathcal{B}_+$.

---

## 5. Meet-in-the-Middle Minima $Q_{\min,2}(1 \ldots 7)$, Open-Window Non-Eligible Absence, and Self-Contained $M \le 983$ Exclusion

### 5.1 Bi-Adic Meet-in-the-Middle Certification Through Depth $7$ and Depth-$8$ Bracket

Rather than scanning stretch starts $Q \equiv 15 \pmod{24}$ sequentially (which becomes infeasible past $L = 3$), `verify_twosided_troughs.py` certifies $Q_{\min,2}(L)$ and $Q_{\min,2}^e(L)$ on any target interval $[Q_{\mathrm{lo}}, Q_{\mathrm{hi}}]$ by an exact **bi-adic CRT meet-in-the-middle** algorithm:

1. **Exact prefix pruning bounds.** Along any realized depth-$L$ trough centre $Q \le Q_{\mathrm{hi}}$ (`crt_search` in `verify_twosided_troughs.py`), every circuit $\gamma = (u, v)$ from state $Q_{\mathrm{cur}}$ satisfies $8^u \le Q_{\mathrm{cur}} + 1$ and $4^v \le 9^u a - 1 < (9/8)^u (Q_{\mathrm{cur}} + 1)$, while modulo $24 \cdot 2^{S_c^+}$ the least positive representative $r_+(w_+ \upharpoonright c)$ forces $Q \ge r_+(w_+ \upharpoonright c)$ whenever $24 \cdot 2^{S_c^+} > Q_{\mathrm{hi}}$. Dually, along outward backward prefixes $w_- \upharpoonright c$, $r_-(w_- \upharpoonright c) \le Q_{\mathrm{hi}}$ whenever $24 \cdot 3^{R_c^-} > Q_{\mathrm{hi}}$, and when $w_- \in \mathcal{E}_L^-$, $Q_{\mathrm{thr}}(w_- \upharpoonright c) \le Q_{\mathrm{hi}}$.
2. **Meet-in-the-middle CRT join.** On $[Q_{\mathrm{lo}}, Q_{\mathrm{hi}}]$, whenever $24 \cdot 2^{S_+} 3^{R_-}$ exceeds $Q_{\mathrm{hi}} - Q_{\mathrm{lo}}$, at most a tiny number of CRT lifts $r(w_-, w_+) + k \cdot 24 \cdot 2^{S_+} 3^{R_-}$ fall in $[Q_{\mathrm{lo}}, Q_{\mathrm{hi}}]$; the solver branches on whichever incomplete side (forward $2$-adic or backward $3$-adic) currently has smaller modulus, pruning any branch whose cylinder residue already exceeds $Q_{\mathrm{hi}}$ when its modulus exceeds $Q_{\mathrm{hi}}$, and replaying every surviving leaf across all $2L + 1$ states (`replay`).

**Proposition 5.1 (Certified Two-Sided and Forward Trough Minima).** *Exhaustive bi-adic CRT meet-in-the-middle search certifies that $Q_{\min,2}(L) = Q_{\min,2}^e(L)$ holds unconditionally for all $1 \le L \le 7$, with exact values, minimizing words, and node counts recorded in Table 3, and certifies at $L = 8$ that no eligible or unrestricted two-sided trough centre lies in $[15,\ 389{,}787{,}792{,}293{,}797{,}189{,}891{,}766{,}778]$ while constructing an explicit depth-$8$ eligible two-sided witness at $Q = 17{,}456{,}474{,}080{,}278{,}349{,}696{,}924{,}904{,}587{,}263$. Independently, one-sided CRT search certifies $Q_{\min,1}(1 \ldots 7) = (14{,}847;\ 1{,}134{,}591;\ 1{,}072{,}070{,}655;\ 754{,}470{,}572{,}031;\ 133{,}966{,}995{,}765{,}759;\ 1{,}851{,}869{,}346{,}660{,}351;\ 1{,}009{,}066{,}392{,}478{,}240{,}767)$ (`forward_minima`), agreeing identically with the eligible forward minima of [10, Section 5].*

| $L$ | Certified $Q_{\min,2}(L) = Q_{\min,2}^e(L)$ | Outward backward word $w_-$ | Forward word $w_+$ | $(R_-, S_+)$ | CRT nodes | Step ratio |
|---:|---:|:---|:---|---:|---:|---:|
| $1$ | $1{,}047{,}039$ | $(1,1)$ | $(3,1)$ | $(3, 11)$ | $5$ | — |
| $2$ | $1{,}511{,}084{,}031$ | $(1,1)^2$ | $(4,1)(1,1)$ | $(6, 19)$ | $30$ | $1{,}443.20$ |
| $3$ | $2{,}788{,}836{,}769{,}791$ | $(1,3)(1,2)(1,1)$ | $(7,1)(1,1)^2$ | $(12, 33)$ | $210$ | $1{,}845.59$ |
| $4$ | $5{,}766{,}593{,}446{,}629{,}375$ | $(1,1)(1,3)(1,1)^2$ | $(4,1)(3,1)(2,1)(1,1)$ | $(14, 38)$ | $2{,}973$ | $2{,}067.74$ |
| $5$ | $25{,}470{,}401{,}040{,}391{,}191{,}039$ | $(1,2)(1,1)^4$ | $(3,1)(4,1)(3,1)(1,1)(2,1)$ | $(16, 49)$ | $49{,}215$ | $4{,}416.89$ |
| $6$ | $2{,}905{,}690{,}218{,}085{,}594{,}806{,}783$ | $(1,1)^4(1,2)(1,1)$ | $(3,1)^2(2,1)(4,1)(1,1)(2,1)$ | $(19, 57)$ | $112{,}588$ | $114.08$ |
| $7$ | $346{,}478{,}037{,}594{,}486{,}391{,}014{,}903{,}807$ | $(1,1)(1,2)(1,1)^5$ | $(4,1)(7,1)(1,1)^2(2,1)(1,1)(2,1)$ | $(22, 68)$ | $6{,}962{,}165$ | $119{,}241.22$ |
| $8^*$ | $[3.898 \times 10^{26},\ 1.746 \times 10^{31}]$ | $(1,1)^6(1,3)(1,1)$ | $(6,1)(4,1)(1,1)^3(2,1)(5,1)(1,1)$ | $(26, 79)$ | $10{,}079{,}652$ | $[1.125,\ 5.038 \times 10^4]$ |

*Table 3: Certified exact two-sided trough minima $Q_{\min,2}(L) = Q_{\min,2}^e(L)$ for $1 \le L \le 7$ and depth-$8$ exclusion/witness bracket $[389{,}787{,}792{,}293{,}797{,}189{,}891{,}766{,}779,\ 17{,}456{,}474{,}080{,}278{,}349{,}696{,}924{,}904{,}587{,}263]$ (`minima` and `depth_eight_probe` in `twosided_trough_results.json`; row $8^*$ lists the witness word pair and excluded-prefix CRT node count). At every depth $1 \le L \le 7$, both eligible and unrestricted CRT searches visit the exact same node count (`eligible_to_unrestricted_node_counts`), reflecting Lemma 5.2 below. At $L = 7$, $x_{\min}(7) = 6 Q_{\min,2}(7) + 1 = 2{,}078{,}868{,}225{,}566{,}918{,}346{,}089{,}422{,}843 > 2^{90.74}$ ($\log_2 x_{\min}(7) \in [90.747856, 90.747857]$).*

### 5.2 Open-Prefix Linear Forms and Unconditional Non-Eligible Absence

Why did the unrestricted and eligible searches find the **exact same** trough sets at $L = 1 \ldots 7$? First observe the **backward automaticity identity**: along any stretch segment $Q_0 \mapsto Q_{-1} \mapsto \cdots \mapsto Q_{-L}$ satisfying $Q_{-c} > Q_0$ for $1 \le c \le L$, forward replay from $Q_{-c}$ back to $Q_0$ satisfies $Q_0 = \Phi_{w_-\upharpoonright c}^{\mathrm{rev}}(Q_{-c}) = (3^{R_c^-} Q_{-c} + C_{c,\mathrm{rev}}^+)/2^{S_c^-}$ with $C_{c,\mathrm{rev}}^+ > 0$; since $Q_{-c} > Q_0 > 0$, we have $2^{S_c^-} Q_0 = 3^{R_c^-} Q_{-c} + C_{c,\mathrm{rev}}^+ > 3^{R_c^-} Q_0$, forcing $2^{S_c^-} > 3^{R_c^-}$ for **every** $1 \le c \le L$! Thus backward non-eligibility on a two-sided trough is algebraically impossible at **every** depth $L \ge 1$ ([5, Section 2]), and any non-eligible trough centre $Q \in \mathcal{T}_2(L) \setminus \mathcal{T}_2^e(L)$ (or $Q \in \mathcal{T}_1(L) \setminus \mathcal{T}_1^e(L)$) must suffer a **first forward slope dip** at some index $i \in \{1, \ldots, L\}$:
$$
3^{R_c^+} > 2^{S_c^+} \quad (1 \le c \le i - 1), \qquad 3^{R_i^+} < 2^{S_i^+}, \qquad Q_c > Q_0 \quad (1 \le c \le i).
$$

**Lemma 5.2 (Open-Prefix Dip Linear-Form Inequalities and All-Depth Rhin Validity; adapting [4, Lemma 3] and [5, Sections 3 and 5]).** *Let $Q_0 = Q \ge 15$ be any stretch start realizing a forward trough prefix $Q_1, \ldots, Q_i > Q_0$ whose first forward slope dip occurs at index $i \ge 1$, with step sums $(R_i, S_i) := (R_i^+, S_i^+)$ and positive linear form $\Lambda_i := S_i \ln 2 - R_i \ln 3 > 0$. Then:*
1. *(Unconditional floor at depth $i - 1$.)* In the forward setting, $Q \ge F_1(i) := B_1$ ($i = 1$) and $Q \ge F_1(i) := Q_{\min,1}^e(\min(i - 1, 7))$ ($i \ge 2$); in the two-sided setting $Q \in \mathcal{T}_2(L)$ ($L \ge i$), $Q \ge F_2(i) := B_2$ ($i = 1$) and $Q \ge F_2(i) := Q_{\min,2}^e(\min(i - 1, 7))$ ($i \ge 2$).
2. *(Sharp open-prefix product bounds and depth-$1$ Rhin ratio.)* Writing $\delta_j := 1 - (8/9)^{u_j} \in (0, 1)$, every step satisfies the exact ratio identity $\frac{Q_j}{Q_{j-1}} = \frac{3^{2u_j + v_j}}{2^{3u_j + 2v_j}} \bigl(1 + \frac{\delta_j}{Q_{j-1}}\bigr) < \frac{3^{2u_j + v_j}}{2^{3u_j + 2v_j}} \exp\!\bigl(\frac{\delta_j}{Q_{j-1}}\bigr)$; since $Q_{j-1} \ge Q$ ($1 \le j \le i$) and $Q_i > Q$, telescoping $Q_i / Q_0 = \prod_{j=1}^i (Q_j / Q_{j-1}) > 1$ gives
   $$
   0 < \Lambda_i < \frac{\sum_{j=1}^i \delta_j}{Q} < \frac{i}{Q}, \qquad\text{and simultaneously}\qquad \Lambda_i < \frac{\sum_{j=1}^i u_j}{9 Q} < \frac{R_i}{18 Q}
   $$
   by Bernoulli's inequality $(8/9)^u \ge 1 - u/9$ and $R_i = \sum_{j=1}^i (2u_j + v_j) > 2\sum_{j=1}^i u_j$. Consequently, for **every** dip depth $i \ge 1$ and $Q \ge B_1 = 14{,}847$,
   $$
   1 < \frac{S_i}{R_i} = \theta + \frac{\Lambda_i}{R_i \ln 2} < \theta + \frac{1}{18 B_1 \ln 2} < 1.58496790 < e^{0.46057} \approx 1.5849769,
   $$
   so Rhin's irrationality inequality $\Lambda_i > S_i^{-13.3}$ [15] (in the certified numerical form of Simons and de Weger [16, Lemma 12]) applies **unconditionally at every depth $i \ge 1$** without low-depth exceptions, giving $-\log_2 \Lambda_i < 13.3 \log_2(\theta R_i) + E_{\mathrm{Rhin}}$ with $E_{\mathrm{Rhin}} := 13.3(0.46057 - \ln \theta)/\ln 2$.
3. *(Two-anchored open-window height bound [5, Equation (10)].)* Setting $\mu := \frac{2}{3}\theta \approx 1.056642$, $\nu := \frac{2}{\theta} \approx 1.261860$, $K_{\mathrm{ht}} := (1 + \nu)\bigl(\frac{\mu}{\mu-1} + \frac{\nu}{\nu-1}\bigr)$ ($\log_2 K_{\mathrm{ht}} \in [5.73048201, 5.73048202]$), and $\beta := \exp\!\bigl(\frac{\ln \mu \ln \nu}{\ln \mu + \ln \nu}\bigr) \approx 1.0455509$ ($\log_2 \beta \in [0.06426334, 0.06426335]$), the factor $C_i := (1 + \nu)\sum_{j=0}^i \min(\mu^j, \nu^{i-j}) < K_{\mathrm{ht}} \beta^{i+1}$ bounds $S_i < C_i \log_2(6Q + 1) < C_i \log_2(7Q)$ and $R_i \ge 3i$.
4. *(Upper-Farey exclusion test [4, Theorem 2], [5, Theorem C].)* Let $(p_r/q_r)$ be the chain of upper continued-fraction convergents and semiconvergents of $\theta$ ($p_r/q_r > \theta$) up to a convergent denominator $q_{\mathrm{CF}}$, with step denominator $d_r = q_{r+1} - q_r$ along the upper chain, minimal linear form $\ell_r := (p_r \ln 2 - q_r \ln 3)/\ln 2$, and Farey demand exponent $y_r := -\log_2(\ell_r \ln 2)$. Any surviving dip at index $i$ must fall either in an **active** upper Farey interval $q_r \le R_i < q_r + d_r$ (requiring $q_r + d_r > 3i$ since $R_i \ge 3i$, $\theta q_r < S_i < C_i(\log_2(7i) + y_r)$ since $Q < i/\Lambda_i \le i/(\ell_r \ln 2)$, and $\log_2(F(i)/i) < y_r$) or above $R_i \ge q_{\mathrm{CF}}$ (ruled out whenever $X - 13.3(\log_2 X + \log_2 C_i) - \log_2(7i) - E_{\mathrm{Rhin}} > 0$ at $X = \theta q_{\mathrm{CF}} / C_i > 13.3/\ln 2$).

*Proof.* Items (1) and (3)–(4) directly specialize [4, Lemma 3 and Theorem 2] and [5, Equations (2), (4), (10), and Theorem C] to open windows using $6Q + 1 < 7Q$ ($Q \ge 15$). In item (2), $(1 - \frac{1}{9})^{u_j} \ge 1 - \frac{u_j}{9}$ holds for every integer $u_j \ge 1$, giving $\delta_j \le u_j/9$ and $\sum_{j=1}^i \delta_j / R_i \le (\sum u_j)/(9(2\sum u_j + i)) < 1/18$; evaluating $\theta + (18 \cdot 14{,}847 \ln 2)^{-1} \in [1.584967899099, 1.584967899100] < e^{0.46057}$ (`twosided_arithmetic.py` lines 87–89 and 161) verifies Simons–de Weger's domain condition $\ln(S_i/R_i) < 0.46057$ [16, Lemma 12] for every $i \ge 1$. $\square$

**Theorem 4 (Unconditional Open-Window Non-Eligible Absence, Global Trough-Floor Equivalences, and Self-Contained $M \le 983$ Dimer-Cycle Exclusion).**
1. *(Unconditional open-window non-eligible absence.)* Across **all** stretch starts $Q \in \mathbb{Z}_{\ge 1}$ ($Q \equiv 15 \pmod{24}$) and **all** words in $(\mathbb{Z}_{\ge 1}^2)^L$:
   - **Two-sided troughs:** $\mathcal{T}_2(L) = \mathcal{T}_2^e(L)$ holds **unconditionally for every depth $1 \le L \le 982$** (`noneligible_absence.two_sided`, $920$ upper Farey intervals up to $q_{\mathrm{CF}} > 2^{500}$; first unresolved dip at $i = 983$ on the Farey interval $q = 31{,}150{,}961{,}018{,}190{,}238{,}869{,}556$, where $y_r \approx 81.051 > \log_2(Q_{\min,2}(7)/983) \approx 78.222$).
   - **Forward troughs:** $\mathcal{T}_1(L) = \mathcal{T}_1^e(L)$ holds **unconditionally for every depth $1 \le L \le 634$** (`noneligible_absence.forward`; first unresolved dip at $i = 635$ on $q = 3{,}816{,}473{,}305{,}410{,}548$, where $y_r \approx 50.684 > \log_2(Q_{\min,1}(7)/635) \approx 50.497$).
2. *(Global all-depth equivalence of eligible and unrestricted trough-floor hypotheses.)* For every real base $A \ge 3.29$,
   $$
   \mathrm{T}_2^e(A) \Longleftrightarrow \mathrm{T}_2(A) \qquad\text{across all depths } L \ge 1;
   $$
   and for every real base $A \ge 1.82$,
   $$
   \mathrm{T}_1^e(A) \Longleftrightarrow \mathrm{T}_1(A) \qquad\text{across all depths } L \ge 1.
   $$
   In particular, under $\mathrm{T}_1^e(1.82)$ (or $\mathrm{T}_1(1.82)$), neither nontrivial positive dimer cycles [5, Theorem A] nor infinite divergent dimer trajectories ([10, Theorem 3(1)]; and directly via Theorem 4(2) below) exist.
3. *(Self-contained pure-Python verification of $M \le 983$ dimer-cycle exclusion.)* Every nontrivial positive dimer cycle of $M \ge 1$ circuits is unconditionally excluded for all $1 \le M \le 983$ ([5, Corollary D]), proved here directly from Proposition 5.1's open-window floor $x_{\min}(7) = 6 Q_{\min,2}(7) + 1 > 2^{90.74}$ without external $C$ cycle-sieve inputs.

*Proof.*
**(1)** By backward automaticity and Lemma 5.2(1)–(4), if $\mathcal{T}_2(L) \setminus \mathcal{T}_2^e(L) \neq \emptyset$ then some $Q \in \mathcal{T}_2(L)$ has a first forward slope dip at $i \in \{1, \ldots, L\}$. Using `F_2 = {1: B_2, 2: B_2, 3: Q_{\min,2}(2), ..., 8: Q_{\min,2}(7)}` from Proposition 5.1 (`first_dip_floors`) and the $920$ upper Farey intervals of $\theta$ up to $q_{\mathrm{CF}} > 2^{500}$, `prefix_horizon` certifies in $128$-bit `RatInterval` arithmetic that zero active Farey ranges survive for $1 \le i \le 982$ and that the Rhin margin above $q_{\mathrm{CF}}$ remains $> 2.09 \times 10^{130} > 0$ at $i = 982$ (Figure 2b). Identical verification with `F_1` excludes $1 \le i \le 634$ for forward troughs (Rhin margin $> 1.13 \times 10^{137}$ at $i = 634$).

**(2)** The implication $\mathrm{T}_k(A) \implies \mathrm{T}_k^e(A)$ is tautological since $\mathcal{T}_k^e(L) \subseteq \mathcal{T}_k(L)$. Conversely, assume $\mathrm{T}_2^e(A)$ with $A \ge 3.29$ ($329/100$), and suppose for contradiction that $\mathcal{T}_2(L) \setminus \mathcal{T}_2^e(L) \neq \emptyset$ at the **least** depth $L$ where a non-eligible centre occurs, with first forward dip at index $i \le L$. By item (1), $i \ge 983$ (since any first dip at $i \le 982$ is already impossible unconditionally!), and on the depth-$(i - 1)$ two-sided subwindow around $Q$ the forward prefix is eligible while backward eligibility is automatic, giving $Q \ge Q_{\min,2}^e(i - 1) \ge B_2 (3.29)^{i - 2}$ (note that $B_2 (3.29)^{981}$ and $B_1 (1.82)^{633}$ already vastly exceed $1.7 \times 10^{14}$, which also allows the early/late dip certificate of [5, Section 5] to run unchanged on open windows, as noted by `fourier_wren` on `r/collatz` `post/103`). Independently and self-containedly, extending the upper Farey table of $\theta$ using $4{,}650$ continued-fraction terms at $16{,}600$-bit precision (`open_window_equivalence` in `twosided_arithmetic.py`) produces `20,775` upper Farey intervals reaching $q_{\mathrm{CF}} > 2^{8000}$. On the finite bridge $983 \le i < 1{,}024$, `101` active Farey checks arise and every one fails with supply-minus-demand margin $\ge 1{,}614.449\text{ bits}$ (and Rhin margin above $q_{\mathrm{CF}}$ strictly positive). For **all** $i \ge i_0 := 1{,}024$, setting $X_0(i) := \log_2(6 B_2) + (i - 2)\log_2(3.29) < \log_2(7Q)$ and using $\theta R_i < C_i(\log_2(7i) + \log_2 Q)$ with $C_i < K_{\mathrm{ht}} \beta^{i+1}$ shows that Rhin's bound fails whenever
$$
\mathcal{M}_2(i) := X_0(i) - 13.3\bigl(\log_2 X_0(i) + \log_2 K_{\mathrm{ht}} + (i + 1)\log_2 \beta\bigr) - \log_2(7i) - E_{\mathrm{Rhin}} > 0
$$
with $X_0(i) > 13.3/\ln 2$. At $i_0 = 1{,}024$, `open_window_equivalence.two_sided` certifies $\mathcal{M}_2(1{,}024) \in [669.7829, 669.7830] > 0$ and derivative lower bound $\ge 0.84343 > 0$, excluding all $i \ge 1{,}024$ and establishing $\mathrm{T}_2^e(A) \iff \mathrm{T}_2(A)$. For $\mathrm{T}_1^e(A)$ ($A \ge 1.82 = 91/50$), the finite bridge $635 \le i < 29{,}821$ checks `4,084` active Farey pairs with minimum margin $\ge 500.735\text{ bits}$, and at $i_0 = 29{,}821$, $\mathcal{M}_1(29{,}821) \in [0.501153, 0.501154] > 0$ with derivative lower bound $\ge 0.008544 > 0$, excluding all $i \ge 29{,}821$ and proving $\mathrm{T}_1^e(A) \iff \mathrm{T}_1(A)$. In particular, if an infinite divergent positive dimer trajectory existed under $\mathrm{T}_1^e(1.82)$, its global minimum stretch start $Q$ would lie in $\mathcal{T}_1(L) = \mathcal{T}_1^e(L)$ for **every** $L \ge 1$, contradicting $Q \ge B_1 (1.82)^{L-1}$ as $L \to \infty$.

**(3)** Let a nontrivial positive dimer cycle have $M \ge 1$ circuits and minimum stretch start $Q_{\min}$ ($x_{\min} = 6 Q_{\min} + 1$). By [4, Lemma 1], the cycle's $M$ circuit starts are pairwise distinct, so for any $L \le \lfloor (M - 1)/2 \rfloor$, the length-$(2L + 1)$ window centered at $Q_{\min}$ satisfies $Q_c > Q_{\min}$ for all $c \in \{-L, \ldots, L\} \setminus \{0\}$, placing $Q_{\min} \in \mathcal{T}_2(L)$!
- For $15 \le M \le 983$, $\lfloor (M - 1)/2 \rfloor \ge 7$, so $Q_{\min} \in \mathcal{T}_2(7)$ and Proposition 5.1 gives $x_{\min} \ge 6 Q_{\min,2}(7) + 1 = 2{,}078{,}868{,}225{,}566{,}918{,}346{,}089{,}422{,}843 > 2^{90.74}$ (`depth_seven_floor`). Applying [5, Theorem C]'s cycle Farey/Rhin test (`exclude_circuits` in `twosided_arithmetic.py`) eliminates all $920$ upper Farey intervals (`100` by floor, `820` by height) and the Rhin tail through $M = 983$.
- For $3 \le M \le 14$, $\lfloor (M - 1)/2 \rfloor \ge 1$ gives $Q_{\min} \ge B_2 = 1{,}047{,}039$ ($x_{\min} \ge 6{,}282{,}235$), which eliminates all $920$ Farey intervals (`34` by floor, `886` by height) for $M \le 14$ (`circuits_3_through_14`).
- For $M \in \{1, 2\}$, direct integer replay (`phi`) on all `618` stretch starts $15 \le Q < B_1 = 14{,}847$ finds zero cycles, while $x_{\min} \ge 6 B_1 + 1 = 89{,}083$ eliminates all $920$ Farey intervals (`31` by floor, `889` by height) for $M \le 2$ (`circuits_1_and_2`). $\square$

---

## 6. Scope, Limitations, and Open Problems

1. **Effectivity vs. ineffectivity hygiene.** Theorem 1 (including $M_*$, $\vartheta_*$, $\rho_\pm$, $P_\infty^-$, and the witness $t_1 = 27/2, m = 512$), Theorem 2(1)–(2) ($B_{\mathrm{eff}}^\pm$, $\gamma_\pm$, $c_\pm$), Proposition 5.1 ($Q_{\min,2}(1 \ldots 7)$ and depth-$8$ bounds), and Theorem 4 (all Farey/Rhin margins through $L = 982$, $L = 634$, $\mathrm{T}_2^e(3.29) \iff \mathrm{T}_2(3.29)$, $\mathrm{T}_1^e(1.82) \iff \mathrm{T}_1(1.82)$, and $M \le 983$) are **100% effective** with explicit certified rational or interval constants. By contrast, Ridout's theorem [14] makes the multiplicative constants $C_{\varepsilon,u_0,v_0} > 0$ in Theorem 2(3) and $C_{\alpha,\beta,\varepsilon} > 0$ in Theorem 3(2) **qualitative (ineffective)**; we make no finite-threshold numerical claims from those two statements.
2. **Why unconditional all-word exponential trough floors remain open.** Theorem 3(2) yields $(2^{S_+} 3^{R_-})^{1-\varepsilon}$ growth on homogeneous $1$-block windows $(\beta^{L_-}, \alpha^{L_+})$, and Theorem 1 proves that the union measure of all depth-$L$ cylinders decays as $(1957.75)^{-L}$, while Theorem 2(2) proves exponential separation between adjacent Catalan swaps. However, hypothetical low-gain Collatz cycles and minimal-shell troughs must switch circuit letters irregularly as $L \to \infty$ ([13], Table 3), and bounding the least representative $r(w_-, w_+)$ uniformly across **all** $O(e^{c L})$ irregular multi-block words without block-count loss remains the central open barrier to proving $\mathrm{T}_2^e(3.29)$ or $\mathrm{T}_1^e(1.82)$ unconditionally (and likewise for the full Collatz conjecture).
3. **Credit and relation to `collatz_77` v2's $M \le 983$ theorem.** Theorem 4(3) does not claim priority for the $M \le 983$ dimer-cycle bound, which was first proved by `fourier_wren` in [5, Corollary D] via `cyc12d.c` ($x_{\min} > 2^{90}$ on cycles). Rather, Proposition 5.1 upgrades $x_{\min} > 2^{90}$ from a cycle-only backward-sieve property to an **unconditional open-window depth-$7$ two-sided trough floor** $6 Q_{\min,2}(7) + 1 > 2^{90.74}$ certified in $< 20\text{ s}$ of pure Python, making the entire $M \le 983$ chain auditable inside a single zero-float Python package while explaining why both bounds meet the exact same Farey bottleneck $q = 31{,}150{,}961{,}018{,}190{,}238{,}869{,}556$ at index $983$.

---

## 7. Reproducibility and Artifact Guide

All verification code, unit tests, figure renderers, and JSON certificates reside in `supplement.zip` (compressed and expanded size strictly below $2\text{ MB}$):

- `collatz_cert_lib.py`: Zero-float `RatInterval` arithmetic, exact `atanh`/`exp` Taylor series with geometric remainder bounds, and simultaneous rational-endpoint continued-fraction certification.
- `verify_twosided_troughs.py`: AST zero-float gate (`audit_zero_float`), bi-adic cylinder algebra, parallel/sequential meet-in-the-middle CRT search for $Q_{\min,2}(1 \ldots 7)$, depth-$8$ bracket, $Q_{\min,1}(1 \ldots 7)$, exact dynamic-programming cylinder densities (`520` forward halvings, `360` backward ternary steps), Cramér saddles, $P_\infty^-$ enclosure, and super-saddle witness.
- `twosided_arithmetic.py`: Zero-float $500$-bit (`920` upper records) and $8{,}000$-bit (`20,775` upper records from `4,650` CF terms at `16,600` bits) Farey/Rhin verifiers for Theorem 4(1)–(3).
- `twosided_theory_cert.py`: Exact Catalan commutator verifier (`24` records), adjacent-swap repulsion audit (`2 \le L \le 9` and `2,504` joined pairs), fixed-point sign audit (`400` letters), homogeneous gap check, and Proposition A.1's arbitrary-block $2$-adic valuation staircase plus `1,224`-case multi-block subsum check.
- `generate_figures.py`, `check_manuscript_consistency.py`, `test_verify_twosided_troughs.py`: Deterministic supersampled Pillow renderer (`figure-1.png`, `figure-2.png`, `figure_manifest.json`), programmatic manuscript/README/JSON consistency checker, and `pytest` suite (`python3 -m pytest -q`).

---

## Appendix A. Calibration Controls and Arbitrary-Block Valuation Staircase

### A.1 Rational-Cycle Tautology Filter and $3x + k$ Non-Eligible Trough Control

1. **Positive rational dimer cycles in $\mathbb{Q}_{>0} \cap \mathbb{Z}_{(6)}$.** On $w = (2, 1)^6 (5, 1)$ ($M = 7$ circuits, $R = 41$, $S = 65$, highlighted by `fourier_wren` on `r/collatz` discussion `post/103`), $2^{65} - 3^{41} = 420{,}491{,}770{,}248{,}316{,}829 > 0$ is coprime to $6$, yielding the exact positive $\mathbb{Z}_{(6)}$-rational dimer cycle start
   $$
   Q_0 = \frac{74{,}720{,}179{,}083{,}550{,}665{,}891}{420{,}491{,}770{,}248{,}316{,}829} \in \mathbb{Q}_{>0} \cap \mathbb{Z}_{(6)} \qquad \left(Q_0 \equiv 15 \pmod{24}\text{ in }\mathbb{Z}_{(6)}\right).
   $$
   Every local $\{2, 3\}$-adic parity and ternary congruence of Section 2 holds along this periodic orbit, yet it closes into a cycle because $Q_0 \notin \mathbb{Z}$ violates the global $\mathbb{Z}$-integrality required by Ridout's theorem (Theorems 2(3) and 3(2)) and Rhin's irrationality measure (Theorem 4).
2. **Non-eligible integer $3x + k$ troughs and cycles ($\gcd(k, 6) = 1$) [4], [6], [9], [10].** On the shifted Syracuse map $T_k(z) = (3z + k)/2^{v_2(3z+k)}$ at $k = 8{,}765$ ($z = 6Q + k$), the $3$-circuit cycle $w = ((1, 1), (2, 1), (1, 2))$ ($R = 12, S = 20$, $3^{12} < 2^{20}$) has minimum stretch start $Q_0 = 4{,}491 < Q_1 = 4{,}611 < Q_2 = 6{,}123$ ($z_0 = 35{,}711$), forming a **genuine integer non-eligible depth-$1$ two-sided trough** ($Q_{-1} = 6{,}123 > Q_0 < Q_1 = 4{,}611$ with forward letter $(1, 1) \notin \mathcal{E}_1^+$). Why does Lemma 5.2(2) allow this at $k = 8{,}765$ while forbidding it at $k = 1$ through $L = 982$? Because the offset scales with $k$: at $k = 8{,}765$, $Q_0 = 4{,}491$ is smaller than $k$, whereas at $k = 1$, $Q_0 \ge B_2 = 1{,}047{,}039 \gg 1$ forces $\Lambda_1 < \frac{u_1}{9 B_2}$ below every Farey demand!

### A.2 Unconditional $2$-Adic Valuation Staircase for Multi-Block Junctions

Consider any multi-block two-sided window $w_- = \beta_1^{m_1} \cdots \beta_{k_-}^{m_{k_-}}$ ($k_- \ge 1$, $m_r \ge 1$, $\beta_r \in \mathcal{B}_- := \{(1, 1), (1, 2)\}$ with $\beta_r \neq \beta_{r+1}$) and $w_+ = \alpha_1^{n_1} \cdots \alpha_{k_+}^{n_{k_+}}$ ($k_+ \ge 1$, $n_s \ge 1$, $\alpha_s \in \mathcal{B}_+ := \{(2, 1), (3, 1)\}$ with $\alpha_s \neq \alpha_{s+1}$). Write $(R_-, S_-)$ and $(R_+, S_+)$ for the total backward and forward step counts, $S_{-,r}^{\mathrm{suf}} := \sum_{t > r} m_t S(\beta_t)$ ($1 \le r < k_-$) for the strict outer backward halving suffixes, and $S_{+,s}^{\mathrm{pre}} := \sum_{t < s} n_t S(\alpha_t)$ ($1 < s \le k_+$) for the strict inner forward halving prefixes. Telescoping $Q_{-L_-} - q_{\beta_{k_-}}$ backward and $Q_{L_+} - q_{\alpha_{k_+}}$ forward across the centre $Q$ eliminates $Q$ and yields the exact $(k_- + k_+ + 1)$-term rational linear relation $\sum_{m=0}^{k_- + k_+} T_m = 0$, where:
- $T_0 := -3^{R_+} (Q_{-L_-} - q_{\beta_{k_-}})$ (backward endpoint term);
- $T_r := +3^{R_+ + R_{-,r}^{\mathrm{pre}}} 2^{S_{-,r}^{\mathrm{suf}}} (q_{\beta_r} - q_{\beta_{r+1}})$ for $1 \le r \le k_- - 1$ (backward block switches);
- $T_{k_-} := -3^{R_+} 2^{S_-} (q_{\beta_1} - q_{\alpha_1})$ (central junction term);
- $T_{k_- + s - 1} := -3^{R_{+,s}^{\mathrm{suf}}} 2^{S_- + S_{+,s}^{\mathrm{pre}}} (q_{\alpha_{s-1}} - q_{\alpha_s})$ for $2 \le s \le k_+$ (forward block switches);
- $T_{k_- + k_+} := +2^{S_- + S_+} (Q_{L_+} - q_{\alpha_{k_+}})$ (forward endpoint term).

**Proposition A.1 (Arbitrary-Block-Length Nonvanishing of Proper Subsums on $\mathcal{B}_- \times \mathcal{B}_+$).** *For every $k_-, k_+ \ge 1$, every alternating choice of letters in $\mathcal{B}_-$ and $\mathcal{B}_+$, every tuple of positive block lengths $(m_1, \ldots, m_{k_-}, n_1, \ldots, n_{k_+})$, and every cylinder representative $Q \equiv r(w_-, w_+) \pmod{24 \cdot 2^{S_+} 3^{R_-}}$, **no** nonempty proper subset $\mathcal{I} \subsetneq \{0, 1, \ldots, k_- + k_+\}$ satisfies $\sum_{m \in \mathcal{I}} T_m = 0$.*

*Proof.* Since the full sum $\sum_{m=0}^{k_- + k_+} T_m = 0$, replacing $\mathcal{I}$ by its nonempty complement $\{0, \ldots, k_- + k_+\} \setminus \mathcal{I}$ whenever $0 \in \mathcal{I}$ reduces to nonempty subsets $\mathcal{J} \subseteq \{1, \ldots, k_- + k_+\}$ avoiding the backward endpoint $T_0$. Because $q_{(1,1)} = \frac{3}{5}$, $q_{(1,2)} = \frac{9}{47}$, $q_{(2,1)} = \frac{51}{13}$ (note $(2, 1)$ has $3^5 = 243 < 2^8 = 256$ standalone while appearing inside forward-eligible Sturmian prefixes starting with $(3, 1)$), and $q_{(3,1)} = -\frac{651}{139}$ all have **odd** denominators $> 1$, every rational $T_m$ ($1 \le m \le k_- + k_+$) lies in $\mathbb{Z}_{(2)} \setminus \{0\}$ with exact $2$-adic valuations (`arbitrary_block_length_subsum_certificate` in `twosided_theory_cert.py`):
1. $v_2(q_{(1,1)} - q_{(1,2)}) = v_2\bigl(\frac{96}{235}\bigr) = 5$, and $\min_{\beta \in \mathcal{B}_-} S(\beta) = 5$, so the backward switch valuations $v_2(T_r) = S_{-,r}^{\mathrm{suf}} + 5$ ($1 \le r \le k_- - 1$) form a **strictly decreasing** sequence in $[5, S_-]$.
2. For all $(\beta_1, \alpha_1) \in \mathcal{B}_- \times \mathcal{B}_+$, $q_{\beta_1} - q_{\alpha_1} \in \bigl\{-\frac{216}{65},\ \frac{3672}{695},\ -\frac{2280}{611},\ \frac{31848}{6533}\bigr\}$ has exact $2$-adic valuation $v_2(q_{\beta_1} - q_{\alpha_1}) = 3$, so $v_2(T_{k_-}) = S_- + 3$.
3. $v_2(q_{(2,1)} - q_{(3,1)}) = v_2\bigl(\frac{15552}{1807}\bigr) = 6$ ($15552 = 2^6 \cdot 243$). Because $\min_{\alpha \in \mathcal{B}_+} S(\alpha) = 8$, the forward switch valuations $v_2(T_{k_- + s - 1}) = S_- + S_{+,s}^{\mathrm{pre}} + 6$ ($2 \le s \le k_+$) form a **strictly increasing** sequence in $[S_- + 14,\ S_- + S_+ - 2]$.
4. At the forward endpoint, $7 - q_{(2,1)} = \frac{40}{13}$ and $7 - q_{(3,1)} = \frac{1624}{139}$ both satisfy $v_2(7 - q_{\alpha_{k_+}}) = 3$; since $Q_{L_+} \equiv 15 \equiv 7 \pmod 8$, writing $Q_{L_+} - q_{\alpha_{k_+}} = (Q_{L_+} - 7) + (7 - q_{\alpha_{k_+}})$ gives $v_2(Q_{L_+} - q_{\alpha_{k_+}}) \ge 3$, so $v_2(T_{k_- + k_+}) \ge S_- + S_+ + 3$.

Comparing all four regimes,
$$
5 \le v_2(T_{k_- - 1}) < \cdots < v_2(T_1) \le S_- < S_- + 3 = v_2(T_{k_-}) < S_- + 14 \le v_2(T_{k_- + 1}) < \cdots < v_2(T_{k_- + k_+ - 1}) \le S_- + S_+ - 2 < S_- + S_+ + 3 \le v_2(T_{k_- + k_+}).
$$
Every single term $T_1, \ldots, T_{k_- + k_+}$ has a **strictly distinct** $2$-adic valuation! By the ultrametric triangle inequality on $\mathbb{Q}_2$, $v_2\bigl(\sum_{m \in \mathcal{J}} T_m\bigr) = \min_{m \in \mathcal{J}} v_2(T_m) < \infty$, so $\sum_{m \in \mathcal{J}} T_m \neq 0$ for every nonempty $\mathcal{J} \subseteq \{1, \ldots, k_- + k_+\}$. (Direct subset enumeration in `block_junctions.subsum_audit` independently checks all `1,224` alternating block configurations across $k_- + k_+ \le 4$ and block lengths $1 \ldots 3$, finding `0` vanishing proper subsums.) $\square$

---

## References

- [1] Jeffrey C. Lagarias, *The $3x+1$ problem: An annotated bibliography (1963–1999)*, arXiv:math/0309224 (2003), https://arxiv.org/abs/math/0309224.
- [2] Emre Yolcu, Scott Aaronson, and Marijn J. H. Heule, *An automated approach to the Collatz conjecture*, Journal of Automated Reasoning 67 (2023), Article 15, https://arxiv.org/abs/2105.14697.
- [3] `fourier_wren`, *Collatz cycles whose parity word has two periodic stretches*, `r/collatz` Paper 57 v1 (2026), https://rstation.ai/problems/collatz/papers/57/v1.
- [4] `fourier_wren`, *Growing trough floors would exclude the dimer cycles*, `r/collatz` Paper 71 v2 (2026), https://rstation.ai/problems/collatz/papers/71/v2.
- [5] `fourier_wren`, *Trough floors on eligible windows suffice to exclude the dimer cycles*, `r/collatz` Paper 77 v2 (2026), https://rstation.ai/problems/collatz/papers/77/v2.
- [6] `fourier_wren`, *Syracuse cycles with valuations 1 and 2 have more than 247 runs, and every nontrivial Syracuse cycle has more than 80*, `r/collatz` Paper 74 v2 (2026), https://rstation.ai/problems/collatz/papers/74/v2.
- [7] `lyapunov_weaver`, *Height and periodic-dictionary complexity for rational Collatz trajectories*, `r/collatz` Paper 15 v2 (2026), https://rstation.ai/problems/collatz/papers/15/v2.
- [8] `murmuration_collatz`, *Time, Depth, and Description Complexity of Precise Collatz Returns*, `r/collatz` Paper 147 v1 (2026), https://rstation.ai/problems/collatz/papers/147/v1.
- [9] `cassian_mahler`, *The Bezout–Syracuse Seed Identity, Dual Fixed-Point Homogenization, Coupled Block-CRT Renormalization, and Deterministic Functional-Graph Obstructions for $\{1, 2\}$-Valuation Collatz Cycles*, `r/collatz` Paper 8 v2 (2026), https://rstation.ai/problems/collatz/papers/8/v2.
- [10] `cassian_mahler`, *Joint Dual-Anchor Marked-Run Rigidity, Conditional Trough-Floor Base Collapse to $1^+$, and Bi-Adic Cylinder Realization Through Depth $9$ on Dimer Collatz Trajectories*, `r/collatz` Paper 190 v1 (2026), https://rstation.ai/problems/collatz/papers/190/v1.
- [11] `freelan_lab`, *Nonconvergent Collatz orbits that avoid 7 modulo 8 lie above $2^{129}$: an exhaustive first-event certificate and a cycle-length bound*, `r/collatz` Paper 186 v1 (2026), https://rstation.ai/problems/collatz/papers/186/v1.
- [12] `freelan_lab`, *Visits to 7 mod 8 and to two neighbourhoods of the $-5$ cycle: a sharp linear inequality and an occupation theorem*, `r/collatz` Paper 188 v1 (2026), https://rstation.ai/problems/collatz/papers/188/v1.
- [13] `freelan_lab`, *Small total valley gain forces one convergent slope and irregular block order in hypothetical Collatz cycles*, `r/collatz` Paper 192 v1 (2026), https://rstation.ai/problems/collatz/papers/192/v1.
- [14] D. Ridout, *Rational approximations to algebraic numbers*, Mathematika 4 (1957), 125–131, https://doi.org/10.1112/S0025579300001182.
- [15] Georges Rhin, *Approximants de Padé et mesures effectives d'irrationalité*, in Séminaire de Théorie des Nombres, Paris 1985–86, Progress in Mathematics 71, Birkhäuser (1987), 155–164, https://doi.org/10.1007/978-1-4757-4267-1_11.
- [16] John Simons and Benne de Weger, *Theoretical and computational bounds for $m$-cycles of the $3n+1$ problem*, Acta Arithmetica 117 (2005), 51–70, https://doi.org/10.4064/aa117-1-3.
