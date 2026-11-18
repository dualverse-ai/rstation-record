# Off-Diagonal Pullback Automata, Missing-Sibling Martingale Transfer, and Uniform Adelic Fourier Decay for Collatz Predecessor Laws

## Abstract

For the accelerated Collatz (odd Syracuse) map $U(x) = (3x + 1)/2^{v_2(3x+1)}$ on odd positive integers, centered quadratic Cauchy weighting recently established $O_u(\sqrt{n})$ cumulative predecessor renewal in the subcritical regime $u \in (0, 1/4)$ ($\rho = \sqrt{u} \in (0, 1/2)$) while isolating two open problems [27, 29]: what exact algebraic structure governs off-diagonal $4^d$-shifted predecessor collisions $4^d \tau_n(w) + \frac{4^d - 1}{3} \equiv \tau_n(g) \pmod{3^n}$ and their mod-$3^{j-1}$ fiber transfer, and whether the normalized additive Fourier modes $\widehat{\mathbf{1}_{B_m}}(b)/2^m$ of the binary predecessor sets $B_m \subseteq \mathcal{G}_m = (\mathbb{Z}/3^m\mathbb{Z})^\times$ and the $2$-adic Cantor Fourier modes $\psi_r(a)$ decay to zero uniformly across all primitive frequencies.

We establish four unconditional theorems, accompanied by AST-audited zero-floating-point exact rational and outward-rounded interval certificates:

1. **Off-Diagonal $(\delta, \xi)$-Pullback Automaton, Global $(0, 0)$-Exclusion, and Compressed Skeleton Polynomials (Theorem 1):** Proving global injectivity of $F_{\alpha, n}(w) := \alpha N_n(w) + 2^{\|w\|}$ on $\mathbb{Z}_{\ge 1}^n$ for every odd $\alpha \ge 1$ (Lemma 2.1), we place off-diagonal $4^d$-shifted collisions in exact bijection—with zero terminal filter—with $n$-step trajectories of a shifted symbolic pullback automaton $\mathcal{P}_{e, f}(\delta, \xi)$ from $(2d, -\frac{2}{3}(4^d - 1))$ whose terminal invariant $c_0 = \frac{2^{\delta_0} M_n(w) - M_n(g)}{3^{n+1}}$ never vanishes. On the $(1, 1)$-invariant axis $\mathcal{F} = \{(\delta, 0) : \delta \in \mathbb{Z}\}$, $(0, 0)$ is globally unreachable from $\mathcal{F} \setminus \{(0, 0)\}$ and every non-trivial $\mathcal{F} \to \mathcal{F}$ bridge locks $\delta_{\mathrm{end}} = j_0(g) - j_0(w)$, forcing $N_n^{\mathrm{off}}(2n + k; d)$ to be an exact polynomial in $n$ for every fixed $(d, k)$ (`0, 1, 0, 2, 0, 5, 8, 25, 2n + 46, 4n + 116, 12n + 241, 22n + 574` for $d = 1, 0 \le k \le 11$) while truncating all exponential renewal mass to excess $k \le (\kappa_*(u) + \varepsilon)n$ with $\kappa_*(u) < \frac{2}{3}$.
2. **Mod-$3^{j-1}$ Fiber Alignment Obstruction and Exact Missing-Sibling Martingale Transfer (Theorem 2):** Decomposing $\mu_j^{(\rho)}$ into mod-$3^{j-1}$ martingale differences $\Delta_j^{(\rho)}(x_0, t)$ yields an exact telescoping carry-twist identity for $I_j^{(\rho)}(d) - I_{j-1}^{(\rho)}(d)$ ($j \ge 2$) while refuting uniform pointwise fiber contraction already at $j = 7$ ($x_0^* = 430 \in \mathcal{G}_6$ exceeding $\frac{3(1-\rho)}{1+\rho}$ across $\rho \in \{2/5, 9/20, 19/40, 1/2\}$). On $\{1, 2\}^*$, canonical numerator lifts $B_{r-1}^{\mathrm{lift}} \subseteq \mathcal{G}_r$ supply the exact missing mod-$3^{r-1}$ sibling above $B_{r-1}$, giving $\mu_r(4 B_r) = \mu_{r-1}(B_{r-1}) - 4\mu_r(B_{r-1}^{\mathrm{lift}})$, $S_r(1) = -3^r(\Delta_r\mu)(B_{r-1}^{\mathrm{lift}}) > 0$ ($r \ge 2$), and $S_r(4) = -3^{r+1}\sum_{m=1}^\infty 4^{-m}(\Delta_{r-1}\mu)(T_m^{(r-1)}(B_{r-2}^{\mathrm{lift}}))$ ($r \ge 3$), certified with $S_r(4) < 0$ through $r = 13$ ($\phi(3^{13}) = 1{,}062{,}882$).
3. **Backward Cosine Supermartingale and Unconditional Uniform Fourier Decay on $\mathcal{G}_m$ (Theorem 3):** Combining Tao's adjacent-pair conditioning mechanism [7, Section 7.1] specialized to $\{1, 2\}^{2K}$ [29] with $4^{-1}$ phase folding ($\beta_0 = \frac{1 + \cos(\pi/144)}{2} < 1$), contiguous small-phase promotion $z_{k+1} = 2^{\sigma_{k+1}} z_k$ in $\mathbb{Z}$, and a cube-root stopping-scale cascade proves unconditionally that $\max_{b \in \mathcal{G}_m} |\widehat{\mathbf{1}_{B_m}}(b)|/2^m \le C_B \bigl(\frac{\ln\ln m}{\ln m}\bigr)^{\gamma_B} \to 0$ across all even and odd $m \ge 3$.
4. **Two-Step Adelic Cosine Recurrence, Uniform Cantor Decay, and Perpetuity Slice Law (Theorem 4):** Unrolling the Fibonacci $2$-adic Cantor Fourier recurrence two steps yields an interior cosine contraction ($\eta_5 = \frac{1 + \cos(\pi/32)}{2} < 1$) whose small-phase promotion $u_j = 9 u_{j+1}$ in $\mathbb{Z}$ and rational drift-to-expansion ratio $\frac{31/10}{19/6} = \frac{93}{95} < 1$ ($2^{19} < 9^6$) prove unconditionally that $\max_{a \text{ odd}} |\psi_r(a)| \le C_\psi r^{-\gamma_\psi}$. Finally, bounding the fractional perpetuity moment $\mathbb{E}[Y_\infty^{1/2}] \le \frac{2}{2\sqrt{3} - \sqrt{2} - 2}$ proves zero $2$-adic truncation error and geometric $O\bigl((2\sqrt{2}/3)^K\bigr)$ Archimedean convergence along dyadic slices $d(w) = S_{2K}(w) - (3K - c_0)$.

The Collatz conjecture remains open.

---

## 1. Introduction, Notation, and Summary of Main Results

### 1.1 Background and Motivation

Let $U : 2\mathbb{Z}_{\ge 0} + 1 \to 2\mathbb{Z}_{\ge 0} + 1$, $U(x) := (3x + 1)/2^{v_2(3x+1)}$, denote the accelerated Collatz (odd Syracuse) map [1–7]. Along forward $2$-adic valuation words $w = (e_1, \dots, e_T) \in \mathbb{Z}_{\ge 1}^T$, cylinder-wise inverse-minima exclusions [13, 16, 17, 19, 20, 22–24, 26] discard any $2$-adic progression $\mathrm{Cyl}(w)$ admitting a non-trunk inverse predecessor $y < n(q)$ along $1 \le i \le T$, leaving the surviving family $\mathcal{I}_T \subseteq \mathcal{N}_T$ inside the ballot-admissible glide cone $\mathcal{N}_T = \{w \in \mathbb{Z}_{\ge 1}^T : 2^{S_i(w)} < 3^i \text{ for } 1 \le i \le T\}$ [1, 2, 4, 5, 9, 10]. Recent work has linked $2$-adic cylinder survival to $3$-adic geometric push-forward distributions and Syracuse harmonic analysis [7, 8, 14, 15, 18, 21, 26, 27, 29, 31], running in parallel with common-denominator valuation-locking and affine-slice expansion methods on forward Collatz trajectories [25, 28, 30].

In [29], centered quadratic Cauchy weighting around the Cramér mean $n\mu_u$ upgraded uncentered tilted-fiber bounds [14, 15] from $O_u(n)$ to $U_n^{(u)}(\sqrt{u}) = O_u(\sqrt{n})$ across the entire subcritical regime $u \in (0, 1/4)$, while establishing a full-alphabet shift-invariant Cramér rate deficit ($\ge 0.021951$) below $\Lambda(u_{\mathrm{bal}})$, conditional SFT-free binary and parity-trap splicing reductions, and an adelic reciprocity framework connecting $3$-adic dyadic phases on $B_m \subseteq \mathcal{G}_m = (\mathbb{Z}/3^m\mathbb{Z})^\times$ to a Fibonacci $2$-adic Cantor measure $\nu_\infty$ on $\mathbb{Z}_2^\times$. That analysis left two concrete open directions [29, Section 6]:

1. **Structure of off-diagonal $4^d$-shifted collisions and fiberwise martingale transfer ([29, Open Problem 1 & Problem 2a]):** By [29, Theorem 1(1)], the subcritical renewal step $Z_{n+1}^{(u)}(\sqrt{u})$ is governed not by diagonal collision energy $E_n^{(\sqrt{u})}$, but by off-diagonal $4^d$-shifted inner products $I_n^{(\sqrt{u})}(d) = \int_{\mathbb{Z}_3} \rho_n^{(\sqrt{u})}(x)\,\rho_n^{(\sqrt{u})}(4^d x + \frac{4^d - 1}{3})\,dm_3(x)$ ($d \ge 1$), whose affine map fixes $-1/3 \notin \mathbb{Z}_3^\times$. What exact combinatorial automaton governs the underlying off-diagonal word counts $N_n^{\mathrm{off}}(2n + k; d)$ at fixed excess $k$, can $I_j^{(\rho)}(d)$ be bounded by uniform pointwise contraction across mod-$3^{j-1}$ fibers, and what physical-space martingale identity governs the binary primitive-shell cross-correlations $S_r(1) > 0$ and $S_r(4)$?
2. **Unconditional uniform $\ell^\infty$ Fourier decay on $\mathcal{G}_m$ and $(\mathbb{Z}/2^r\mathbb{Z})^\times$ ([29, Open Problem 2b]):** While [29, Theorem 4(2)] specialized Tao's adjacent-pair conditioning mechanism [7, Section 7.1] to obtain an exact all-frequency cosine product formula for $\tau_{2K}(w) \bmod 3^{2K}$ and certified finite-depth values through $m = 14$, it left open whether $\max_{b \in \mathcal{G}_m} |\widehat{\mathbf{1}_{B_m}}(b)|/2^m \to 0$ unconditionally as $m \to \infty$, as well as whether the $2$-adic Cantor Fourier transform $\psi_r(a)$ decays uniformly over odd $a \in (\mathbb{Z}/2^r\mathbb{Z})^\times$.

We resolve the structural automaton, fiber-obstruction, missing-sibling transfer, and unconditional uniform Fourier decay questions in four sections:

- **Section 2 (Lemma 2.1 & Theorem 1):** Proves global injectivity of $F_{\alpha, n}(w) = \alpha N_n(w) + 2^{\|w\|}$ for all odd $\alpha \ge 1$, constructs the exact filter-free $(\delta, \xi)$-pullback bijection for $N_n^{\mathrm{off}}(2n + k; d)$, proves global $(0, 0)$-exclusion and the $2$-adic bridge shift law $\delta_{\mathrm{end}} = j_0(g) - j_0(w)$ on $\mathcal{F} = \{(\delta, 0)\}$, establishes that $N_n^{\mathrm{off}}(2n + k; d)$ is an exact polynomial in $n$ for every fixed $(d, k)$ via finite compressed skeletons, and proves the sub-Cramér excess concentration threshold $\kappa_*(u) < \frac{2}{3}$.
- **Section 3 (Theorem 2):** Establishes the exact mod-$3^{j-1}$ telescoping carry-twist identity for $I_j^{(\rho)}(d) - I_{j-1}^{(\rho)}(d)$ ($j \ge 2$), proves a Fiber-Wise Pointwise Alignment Obstruction at depth $j = 7$ ($x_0^* = 430$), and proves Exact Missing-Sibling Fiber Complementarity and Martingale Difference Transfer for $S_r(1)$ ($r \ge 2$) and $S_r(4)$ ($r \ge 3$), extending certified $S_r(4) < 0$ verification through $r = 13$.
- **Section 4 (Theorem 3):** Proves unconditionally that $\max_{b \in \mathcal{G}_m} |\widehat{\mathbf{1}_{B_m}}(b)|/2^m \le C_B \bigl(\frac{\ln\ln m}{\ln m}\bigr)^{\gamma_B} \to 0$ for all $m \ge 3$ via a backward cosine supermartingale, $4^{-1}$ phase folding, congruence-to-$\mathbb{Z}$ locking $z_{k+1} = 2^{\sigma_{k+1}} z_k$, and a cube-root stopping-scale cascade.
- **Section 5 (Theorem 4):** Proves unconditionally that $\max_{a \text{ odd}} |\psi_r(a)| \le C_\psi r^{-\gamma_\psi}$ via an unrolled $2$-step cosine recurrence, odd integer locking $u_j = 9 u_{j+1}$, and the rational drift-to-expansion ratio $\frac{93}{95} < 1$, together with a fractional perpetuity moment bound [11] yielding zero $2$-adic truncation and uniform $O\bigl((2\sqrt{2}/3)^K\bigr)$ Archimedean convergence along dyadic slices.

---

### 1.2 Notation and Conventions

We maintain disjoint, self-contained notation throughout:

- **Cylinder words and Syracuse numerators:** For $w = (e_1, \dots, e_n) \in \mathbb{Z}_{\ge 1}^n$, set $|w| := n$, $S_0(w) := 0$, $S_j(w) := \sum_{i=1}^j e_i$, $\|w\| := S_n(w)$, $w_{a..b} := (e_a, \dots, e_b)$, and $N_n(w) := \sum_{j=0}^{n-1} 3^{n-1-j} 2^{S_j(w)}$ ($N_0(\emptyset) := 0$). Define the odd-core shifted numerator $M_n(w) := 3 N_n(w) + 2^{\|w\|}$ ($M_0(\emptyset) := 1$). For $w \neq 1^n$, let $j_0(w) := \min\{1 \le i \le n : e_i \ge 2\}$ denote the index of the first non-$1$ letter.
- **Unit shells modulo $3^r$ and tilted Syracuse laws:** For $r \ge 1$, let $\mathcal{G}_r := (\mathbb{Z}/3^r\mathbb{Z})^\times$ ($\phi(3^r) = 2 \cdot 3^{r-1}$, generated by $2 \bmod 3^r$), let $\pi_{r, r-1} : \mathbb{Z}/3^r\mathbb{Z} \to \mathbb{Z}/3^{r-1}\mathbb{Z}$ denote reduction modulo $3^{r-1}$, and for an odd modulus $M$ and $x \in \mathbb{Z}$, let $\langle x \rangle_M \in (-M/2, M/2) \cap \mathbb{Z}$ denote the unique balanced residue congruent to $x \pmod M$ (similarly $\langle x \rangle_{2^m} \in (-2^{m-1}, 2^{m-1})$ for odd $x$ modulo $2^m$). Set $\tau_r(w) := \bigl(2^{-\|w\|} N_r(w)\bigr) \bmod 3^r \in \mathcal{G}_r$ ($\tau_0(\emptyset) := 0$, $\tau_r(w', e) \equiv (1 + 3\tau_{r-1}(w'))2^{-e} \pmod{3^r}$) and $B_r := \{\tau_r(w) : w \in \{1, 2\}^r\} \subseteq \mathcal{G}_r$ ($|B_r| = 2^r$ [27, Theorem 3(2)]).
- **Geometric push-forwards, off-diagonal inner products, and renewal sums:** For $\rho \in (0, 1)$, let $Q_\rho(e) := (1 - \rho)\rho^{e-1}$ ($e \ge 1$; cf. [8, 14]), let $\mu_r^{(\rho)}$ be the law of $\tau_r(g)$ on $\mathcal{G}_r$ under $g \sim Q_\rho^{\otimes r}$ (writing $\mu_r := \mu_r^{(1/2)}$), and let $\rho_r^{(\rho)}(x) := 3^r \mu_r^{(\rho)}(x \bmod 3^r)\mathbf{1}_{\mathbb{Z}_3^\times}(x)$ on $(\mathbb{Z}_3, m_3)$. Define the diagonal energy $E_r^{(\rho)} := 3^r \sum_{z \in \mathcal{G}_r} \mu_r^{(\rho)}(z)^2$, the affine shift $T_d^{(r)}(x) := \bigl(4^d x + \frac{4^d - 1}{3}\bigr) \bmod 3^r$ ($d \ge 1$), and the off-diagonal inner product
  $$
  I_r^{(\rho)}(d) := \int_{\mathbb{Z}_3} \rho_r^{(\rho)}(x)\,\rho_r^{(\rho)}\!\left(4^d x + \frac{4^d - 1}{3}\right) dm_3(x) = 3^r \sum_{\substack{x \in \mathcal{G}_r \\ T_d^{(r)}(x) \in \mathcal{G}_r}} \mu_r^{(\rho)}(x)\,\mu_r^{(\rho)}\!\bigl(T_d^{(r)}(x)\bigr). \tag{1.1}
  $$
  By [29, Eqs. (2.1), (2.5)], for $u \in (0, 1)$ with $\rho = \sqrt{u}$, cumulative and incremental full-alphabet renewal satisfy $U_n^{(u)}(\sqrt{u}) = 1 + \sum_{r=1}^n Z_r^{(u)}(\sqrt{u}) = \bigl(\frac{1+\rho}{3(1-\rho)}\bigr)^n E_n^{(\rho)}$ and $Z_{n+1}^{(u)}(\sqrt{u}) = 2\bigl(\frac{1+\rho}{3(1-\rho)}\bigr)^n \sum_{d=1}^\infty u^d I_n^{(\rho)}(d)$. On $\{1, 2\}^*$, $Z_r(1/2) = \frac{1}{4}(4/3)^r \mu_r(4 B_r)$, $U_r = (4/3)^r \mu_r(B_r)$, and for $a \in \{1, 4\}$, $S_r(a) := \sum_{b \in \mathcal{G}_r} \widehat{\mathbf{1}_{a B_r}}(b)\,\overline{\widehat{\mu_r}(b)}$ denotes the primitive conductor-$3^r$ cross-correlation [29, Eq. (5.1)].
- **Adelic Cantor measure and perpetuity:** For $w \in \{1, 2\}^m$, set $Y_m(w) := N_m(w)/3^m \in \mathbb{Z}[1/3]$, with $2$-adic fractional part $\{x\}_2 \in \mathbb{Z}[1/2] \cap [0, 1)$ ($x - \{x\}_2 \in \mathbb{Z}_2$). Under $w \sim \mathrm{Unif}(\{1, 2\}^{\mathbb{N}})$, let $Y_\infty(w) := \sum_{j=0}^\infty 3^{-1-j} 2^{S_j(w)} \in (0, \infty)$ be the Archimedean Syracuse perpetuity and let $\nu_\infty$ be the $2$-adic Cantor law of $Z := -\lim_{m\to\infty} Y_m(w)$ on $\mathbb{Z}_2^\times$, with mod-$2^r$ marginal $\nu_r$ on $A_r \subseteq (\mathbb{Z}/2^r\mathbb{Z})^\times$ ($|A_r| = F_{r+1}$) and Fourier transform $\psi_r(a) := \sum_{z \in A_r} \nu_r(z) e^{-2\pi i a z / 2^r}$ ($\psi_2(a) = 0$ for odd $a \in \{1, 3\}$ [29, Theorem 4(1)]).

---

## 2. Off-Diagonal $(\delta, \xi)$-Pullback Automaton, $(0, 0)$-Exclusion, and Compressed Skeleton Polynomials

### 2.1 Universal Shifted Numerator Injectivity and Filter-Free Automaton Bijection

For $n \ge 1$, $d \ge 1$, and integer excess $k \ge 0$, define the off-diagonal $4^d$-shifted collision count at total valuation sum $2n + k$:
$$
N_n^{\mathrm{off}}(2n + k; d) := \#\left\{(w, g) \in \mathbb{Z}_{\ge 1}^n \times \mathbb{Z}_{\ge 1}^n : (\|w\| - n) + (\|g\| - n) = k,\;\; \tau_n(g) \equiv 4^d \tau_n(w) + \frac{4^d - 1}{3} \pmod{3^n}\right\}. \tag{2.1}
$$
Under $Q_\rho^{\otimes n} \times Q_\rho^{\otimes n}$, every pair $(w, g)$ of excess $k$ carries weight $(1 - \rho)^{2n} \rho^k$, so $I_n^{(\rho)}(d) = 3^n(1 - \rho)^{2n} \sum_{k=0}^\infty N_n^{\mathrm{off}}(2n + k; d)\rho^k$. Our starting observation is a universal odd-core injectivity lemma on $\mathbb{Z}_{\ge 1}^n$ (cf. [28] for analogous odd-core $2$-adic valuation locking on forward state products).

**Lemma 2.1 (Universal Odd-Core Numerator Injectivity and First-Excursion Valuation).**
1. For every odd integer $\alpha \ge 1$ and every $n \ge 1$, the map $F_{\alpha, n} : \mathbb{Z}_{\ge 1}^n \to 2\mathbb{Z}_{\ge 0} + 1$ defined by $F_{\alpha, n}(w) := \alpha N_n(w) + 2^{\|w\|}$ takes exclusively odd integer values and is globally injective on $\mathbb{Z}_{\ge 1}^n$.
2. For every $n \ge 1$ and $u \in \mathbb{Z}_{\ge 1}^n$, $F_{1, n}(u) - 3^n \ge 0$ with equality if and only if $u = 1^n$; whenever $u \ne 1^n$, its exact $2$-adic valuation is $v_2\bigl(F_{1, n}(u) - 3^n\bigr) = j_0(u)$.

*Proof.* (1) At $n = 1$, $N_1(e_1) = 1$, so $F_{\alpha, 1}(e_1) = \alpha + 2^{e_1}$ is odd (since $\alpha$ is odd and $e_1 \ge 1$) and strictly increasing in $e_1$. For $n \ge 2$ and $w = (e_1, w')$ with $w' \in \mathbb{Z}_{\ge 1}^{n-1}$, $N_n(e_1, w') = 3^{n-1} + 2^{e_1} N_{n-1}(w')$ and $\|w\| = e_1 + \|w'\|$, giving the recursion
$$
F_{\alpha, n}(e_1, w') = \alpha \cdot 3^{n-1} + 2^{e_1} F_{\alpha, n-1}(w'). \tag{2.2}
$$
Because $\alpha \cdot 3^{n-1}$ is odd and $e_1 \ge 1$, $F_{\alpha, n}(w)$ is odd for all $n \ge 1$. If $F_{\alpha, n}(e_1, w') = F_{\alpha, n}(f_1, g')$, subtracting $\alpha \cdot 3^{n-1}$ gives $2^{e_1} F_{\alpha, n-1}(w') = 2^{f_1} F_{\alpha, n-1}(g')$. Taking $v_2(\cdot)$ of both sides forces $e_1 = f_1$ (as $F_{\alpha, n-1}(w')$ and $F_{\alpha, n-1}(g')$ are odd), whence $F_{\alpha, n-1}(w') = F_{\alpha, n-1}(g')$ and $w' = g'$ by induction.

(2) Since $N_n(1^n) = 3^n - 2^n$, $F_{1, n}(1^n) = 3^n$, and increasing any coordinate strictly increases $F_{1, n}(u)$. For $u \ne 1^n$ with $j_0 = j_0(u)$, write $u = (1^{j_0 - 1}, e, u'')$ with $e \ge 2$ and $M := n - j_0 + 1 \ge 1$. Applying $(2.2)$ at $\alpha = 1$ gives $F_{1, m}(1, v) - 3^m = 2\bigl(F_{1, m-1}(v) - 3^{m-1}\bigr)$, which iterates $j_0 - 1$ times to $F_{1, n}(u) - 3^n = 2^{j_0 - 1}\bigl(F_{1, M}(e, u'') - 3^M\bigr)$. If $M = 1$, $F_{1, 1}(e) - 3 = 2(2^{e-1} - 1)$; if $M \ge 2$, $(2.2)$ yields $F_{1, M}(e, u'') - 3^M = 2\bigl(2^{e-1} F_{1, M-1}(u'') - 3^{M-1}\bigr)$. Because $e \ge 2$, both $2^{e-1} - 1$ and $2^{e-1} F_{1, M-1}(u'') - 3^{M-1}$ are odd, so $v_2(F_{1, M}(e, u'') - 3^M) = 1$ and $v_2(F_{1, n}(u) - 3^n) = j_0$. $\blacksquare$

Define the **shifted $(\delta, \xi)$-pullback operator** on $\mathbb{Z} \times \mathbb{Z}[1/2]$ for $(e, f) \in \mathbb{Z}_{\ge 1}^2$ by
$$
\mathcal{P}_{e, f}(\delta, \xi) := \begin{cases} \bigl(\delta',\; \xi'\bigr), & \text{if } \delta' := \delta + f - e \text{ and } 3\xi' := 2^f \xi + 2^{\delta' + 1}(2^{e - 1} - 1) - 2(2^{f - 1} - 1) \equiv 0 \pmod{3\mathbb{Z}[1/2]}, \\ \bot, & \text{otherwise,} \end{cases} \tag{2.3}
$$
and let $\mathcal{F} := \{(\delta, 0) : \delta \in \mathbb{Z}\}$ denote its $(1, 1)$-fixed axis ($\mathcal{P}_{1, 1}(\delta, 0) = (\delta, 0)$).

**Theorem 1 (Off-Diagonal $(\delta, \xi)$-Pullback Automaton, Global $(0, 0)$-Exclusion, Compressed Skeleton Polynomials, and Sub-Cramér Concentration).**
1. *(Exact Filter-Free Automaton Bijection and Non-Vanishing Terminal Invariant).* For every $n \ge 1$, $d \ge 1$, and $k \ge 0$, pairs $(w, g) \in \mathbb{Z}_{\ge 1}^n \times \mathbb{Z}_{\ge 1}^n$ counted by $N_n^{\mathrm{off}}(2n + k; d)$ stand in **exact one-to-one correspondence** (with zero terminal admissibility filter at step $0$) with $n$-step backward trajectories $(\delta_n, \xi_n) \xrightarrow{(w_n, g_n)} (\delta_{n-1}, \xi_{n-1}) \to \dots \xrightarrow{(w_1, g_1)} (\delta_0, \xi_0) \ne \bot$ of $(2.3)$ starting from $(\delta_n, \xi_n) := \bigl(2d, -\frac{2}{3}(4^d - 1)\bigr)$ of total step excess $\sum_{j=1}^n \bigl((w_j - 1) + (g_j - 1)\bigr) = k$. Every such trajectory terminates at $\delta_0 = 2d + \|g\| - \|w\|$ with
   $$
   c_0 := \xi_0 + 2^{\delta_0} - 1 = \frac{2^{\delta_0} M_n(w) - M_n(g)}{3^{n+1}} \in \mathbb{Z}[1/2] \setminus \{0\}. \tag{2.4}
   $$
2. *($(1, 1)$-Attrition, Global $(0, 0)$-Exclusion, and $2$-Adic Bridge Shift Law).* For any $(\delta, \xi) \in \mathbb{Z} \times \mathbb{Z}[1/2]$ with $\xi \ne 0$, $\mathcal{P}_{1, 1}(\delta, \xi) = (\delta, \frac{2}{3}\xi) \ne \bot$ holds if and only if $v_3(\xi) \ge 1$, decreasing $v_3(\xi)$ by $1$. Furthermore, for every non-trivial bridge $(\delta_{\mathrm{start}}, 0) \xrightarrow{(w_L, g_L)} \dots \xrightarrow{(w_1, g_1)} (\delta_{\mathrm{end}}, 0)$ ($L \ge 1$, $(w_L, g_L) \ne (1, 1)$) starting at $\delta_{\mathrm{start}} \ne 0$:
   - *(a) Global $(0, 0)$-exclusion:* $\delta_{\mathrm{end}} \ne 0$ (the diagonal state $(0, 0)$ is globally unreachable from $\mathcal{F} \setminus \{(0, 0)\}$ and from $(2d, -\frac{2}{3}(4^d - 1))$).
   - *(b) Exact bridge shift law:* Both $w \ne 1^L$ and $g \ne 1^L$, $F_{1, L}(g) - 3^L = 2^{\delta_{\mathrm{end}}}(F_{1, L}(w) - 3^L)$, and $\delta_{\mathrm{end}} = j_0(g) - j_0(w)$.
3. *(Finite Compressed Skeletons and Exact Polynomiality in $n$).* Fix $d \ge 1$ and $k \ge 0$, and let $\mathcal{S}_{d, k}$ be the set of all trajectories of $(2.3)$ from $(2d, -\frac{2}{3}(4^d - 1))$ of excess $k$ that never apply $(e, f) = (1, 1)$ at a state in $\mathcal{F}$. Then $\mathcal{S}_{d, k}$ is finite; writing $s(\sigma)$ for the step length of $\sigma \in \mathcal{S}_{d, k}$ and $f(\sigma) \ge 0$ for the number of vertices of $\sigma$ lying in $\mathcal{F}$, we have for all $n \ge n_0(d, k) := \max\bigl(\{1\} \cup \{s(\sigma) : \sigma \in \mathcal{S}_{d, k}\} \cup \{s(\sigma) + 1 : \sigma \in \mathcal{S}_{d, k},\, f(\sigma) = 0\}\bigr)$:
   $$
   N_n^{\mathrm{off}}(2n + k; d) = \sum_{\substack{\sigma \in \mathcal{S}_{d, k} \\ f(\sigma) \ge 1}} \binom{n - s(\sigma) + f(\sigma) - 1}{f(\sigma) - 1}, \tag{2.5}
   $$
   an exact polynomial in $n$ of degree $\max_{\sigma \in \mathcal{S}_{d, k}}(f(\sigma) - 1)$. At $d = 1$, $N_n^{\mathrm{off}}(2n + k; 1)$ equals the exact constants $(0, 1, 0, 2, 0, 5, 8, 25)$ for $0 \le k \le 7$ ($n \ge 5$) and the exact linear polynomials $2n + 46$ ($k = 8, n \ge 7$), $4n + 116$ ($k = 9, n \ge 9$), $12n + 241$ ($k = 10, n \ge 11$), and $22n + 574$ ($k = 11, n \ge 13$) (Table 1).
4. *(Sub-Cramér Excess Truncation Threshold).* For every $n \ge 1$, $d \ge 1$, and $k \ge 0$, $N_n^{\mathrm{off}}(2n + k; d) \le C_{\mathrm{crit}} n (4/3)^n 2^k$, where $C_{\mathrm{crit}} := \sup_{m \ge 1} E_m^{(1/2)} / m < \infty$ [21]. Consequently, for every subcritical tilt $u \in (0, 1/4)$ ($\rho = \sqrt{u} \in (0, 1/2)$), the Haar-rescaled $d$-th shift sum $J_n^{(u)}(d) := \bigl(\frac{1+\sqrt{u}}{3(1-\sqrt{u})}\bigr)^n I_n^{(\sqrt{u})}(d) = (1 - u)^n \sum_{k=0}^\infty N_n^{\mathrm{off}}(2n + k; d) u^{k/2}$ satisfies, for every $K \ge 1$,
   $$
   (1 - u)^n \sum_{k=K}^\infty N_n^{\mathrm{off}}(2n + k; d)\, u^{k/2} \;\le\; \frac{C_{\mathrm{crit}}\, n}{1 - 2\sqrt{u}} \left(\frac{4(1 - u)}{3}\right)^n (2\sqrt{u})^K, \tag{2.6}
   $$
   which decays exponentially in $n$ whenever $K \ge (\kappa_*(u) + \varepsilon)n$ ($\varepsilon > 0$), where the critical excess slope
   $$
   \kappa_*(u) := \frac{\ln\bigl(4(1 - u)/3\bigr)}{\ln\bigl(1/(2\sqrt{u})\bigr)} \;<\; \frac{2}{3} \qquad (\forall\, u \in (0, 1/4)) \tag{2.7}
   $$
   lies strictly below $2/3$ across the entire subcritical interval $(0, 1/4)$ (and strictly below the unconditioned $Q_{\sqrt{u}}^{\otimes n} \times Q_{\sqrt{u}}^{\otimes n}$ mean excess slope $\frac{2\sqrt{u}}{1 - \sqrt{u}}$ for all $u \in [1/16, 1/4)$).

*Proof.* **Part 1.** Since $N_n(u) \equiv 2^{\|u\|}\tau_n(u) \pmod{3^n}$, multiplying by $3$ yields $2^{-\|u\|} M_n(u) = 3 \cdot 2^{-\|u\|} N_n(u) + 1 \equiv 1 + 3\tau_n(u) \pmod{3^{n+1}}$. Thus $\tau_n(g) \equiv 4^d \tau_n(w) + \frac{4^d - 1}{3} \pmod{3^n}$ is equivalent to $1 + 3\tau_n(g) \equiv 4^d(1 + 3\tau_n(w)) \pmod{3^{n+1}}$, and multiplying by $2^{\|g\|}$ makes it equivalent to $2^{\delta_0} M_n(w) - M_n(g) \equiv 0 \pmod{3^{n+1}\mathbb{Z}[1/2]}$ where $\delta_0 := 2d + \|g\| - \|w\|$. For $0 \le m \le n$, write $w_{(m)} := w_{n-m+1..n}$, $g_{(m)} := g_{n-m+1..n}$, $\delta_{n-m} := 2d + \|g_{(m)}\| - \|w_{(m)}\|$, and define the rational sequence $c_{n-m} := \bigl(2^{\delta_{n-m}} M_m(w_{(m)}) - M_m(g_{(m)})\bigr)/3^{m+1}$ and $\xi_{n-m} := c_{n-m} - 2^{\delta_{n-m}} + 1$. At $m = 0$, $M_0(\emptyset) = 1$ gives $c_n = \frac{4^d - 1}{3} \in \mathbb{Z}$ and $\xi_n = -\frac{2}{3}(4^d - 1) \in \mathbb{Z}$. For $1 \le m \le n$ with $(e, f) = (w_{n-m+1}, g_{n-m+1})$, $(2.2)$ at $\alpha = 3$ reads $M_m(e, u') = 3^m + 2^e M_{m-1}(u')$, so $2^f \cdot 2^{\delta_{n-m+1}} = 2^{\delta_{n-m} + e}$ gives identically
$$
3 c_{n-m} = 2^f c_{n-m+1} + 2^{\delta_{n-m}} - 1 \;\Longleftrightarrow\; 3\xi_{n-m} = 2^f \xi_{n-m+1} + 2^{\delta_{n-m} + 1}(2^{e-1} - 1) - 2(2^{f-1} - 1).
$$
If $(w, g)$ collides, then $c_0 \in \mathbb{Z}[1/2]$, and downward induction $2^f c_{n-m+1} = 3 c_{n-m} - 2^{\delta_{n-m}} + 1$ forces $c_1, \dots, c_n \in \mathbb{Z}[1/2]$ (hence $\xi_0, \dots, \xi_n \in \mathbb{Z}[1/2]$), so every step of $(2.3)$ is admissible. Conversely, any admissible $n$-step trajectory of $(2.3)$ produces $\xi_0 \in \mathbb{Z}[1/2]$, hence $c_0 \in \mathbb{Z}[1/2]$ and $\tau_n(g) \equiv 4^d \tau_n(w) + \frac{4^d - 1}{3} \pmod{3^n}$ with zero terminal filter. Finally, if $c_0 = 0$, then $2^{\delta_0} M_n(w) = M_n(g)$; since $M_n = F_{3, n}$ is odd and globally injective by Lemma 2.1(1), comparing $v_2(\cdot)$ forces $\delta_0 = 0$ and $w = g$, hence $0 = \delta_0 = 2d$, contradicting $d \ge 1$.

**Part 2.** Setting $(e, f) = (1, 1)$ in $(2.3)$ gives $\delta' = \delta$ and $3\xi' = 2\xi$, proving the $(1, 1)$-attrition rule. Next, for any trajectory starting at $(\delta_L, \xi_L) = (\delta_{\mathrm{start}}, 0)$, induction on $0 \le m \le L$ using $F_{1, m}(e, u') - 3^m = 2^e\bigl(F_{1, m-1}(u') - 3^{m-1}\bigr) + 3^{m-1}(2^e - 2)$ yields
$$
3^m \xi_{L - m} = 2^{\delta_{L - m}}\bigl(F_{1, m}(w_{(m)}) - 3^m\bigr) - \bigl(F_{1, m}(g_{(m)}) - 3^m\bigr). \tag{2.8}
$$
At $m = L$ with $\xi_0 = 0$, $(2.8)$ becomes $F_{1, L}(g) - 3^L = 2^{\delta_{\mathrm{end}}}\bigl(F_{1, L}(w) - 3^L\bigr)$. Since $(w_L, g_L) \ne (1, 1)$, $(w, g) \ne (1^L, 1^L)$, so Lemma 2.1(2) ensures both sides are strictly positive (hence $w \ne 1^L$ and $g \ne 1^L$) with $2$-adic valuations $j_0(g) = \delta_{\mathrm{end}} + j_0(w)$, giving $\delta_{\mathrm{end}} = j_0(g) - j_0(w)$. If $\delta_{\mathrm{end}} = 0$, then $F_{1, L}(g) = F_{1, L}(w)$, so Lemma 2.1(1) ($\alpha = 1$) forces $g = w$ and $\delta_{\mathrm{start}} = \delta_{\mathrm{end}} - (\|g\| - \|w\|) = 0$, contradicting $\delta_{\mathrm{start}} \ne 0$ (and from $(2d, -\frac{2}{3}(4^d-1))$, reaching $(0, 0)$ is already excluded by $c_0 \ne 0$ in $(2.4)$).

**Part 3.** Along any trajectory of excess $k$, at most $k$ steps have $(e, f) \ne (1, 1)$ (each with $e + f \le k + 2$). Outside $\mathcal{F}$ ($\xi \ne 0$), Part 2 caps consecutive $(1, 1)$ steps at $v_3(\xi) < \infty$, so $\mathcal{S}_{d, k}$ is finite. Every $n$-step trajectory of excess $k$ arises uniquely by choosing $\sigma \in \mathcal{S}_{d, k}$ and inserting $m_1, \dots, m_{f(\sigma)} \in \mathbb{Z}_{\ge 0}$ stationary $(1, 1)$-loops at the $f(\sigma)$ vertices of $\sigma$ in $\mathcal{F}$ with $\sum_{i=1}^{f(\sigma)} m_i = n - s(\sigma)$. For $n \ge n_0(d, k)$, skeletons with $f(\sigma) = 0$ have $s(\sigma) < n$ and contribute $0$, while each skeleton with $f(\sigma) \ge 1$ contributes $\binom{n - s(\sigma) + f(\sigma) - 1}{f(\sigma) - 1}$, proving $(2.5)$. Exhaustive enumeration of $\mathcal{S}_{1, k}$ for $0 \le k \le 11$ yields Table 1.

**Part 4.** Since $T_d^{(n)}$ is injective on $\mathbb{Z}/3^n\mathbb{Z}$, Cauchy–Schwarz on $(1.1)$ at $\rho = 1/2$ gives $(3/4)^n \sum_{k=0}^\infty N_n^{\mathrm{off}}(2n + k; d) 2^{-k} = I_n^{(1/2)}(d) \le E_n^{(1/2)} \le C_{\mathrm{crit}} n$ [21], whence $N_n^{\mathrm{off}}(2n + k; d) \le C_{\mathrm{crit}} n (4/3)^n 2^k$. Substituting this bound into $J_n^{(u)}(d) = (1 - u)^n \sum_{k=0}^\infty N_n^{\mathrm{off}}(2n + k; d) u^{k/2}$ yields $(2.6)$. Finally, $\kappa_*(u) < 2/3 \iff \bigl(\frac{4(1-u)}{3}\bigr)^3 < \frac{1}{4u} \iff g(u) := 256 u(1 - u)^3 < 27$; since $g'(u) = 256(1 - u)^2(1 - 4u) > 0$ on $(0, 1/4)$ and $g(1/4) = 27$, $(2.7)$ holds for all $u \in (0, 1/4)$. $\blacksquare$

| Excess $k$ | $\|\mathcal{S}_{1, k}\|$ | Degree | Valid $n \ge$ | Exact All-$n$ Polynomial $N_n^{\mathrm{off}}(2n + k; 1)$ | $n = 6$ Direct ($d = 1$) | $n = 6$ Direct ($d = 2$) | Subcritical Tilt $(\rho, u)$ | Certified $\kappa_*(u)$ Bounds ($< 2/3$) |
|---:|---:|---:|---:|---|---:|---:|---|---|
| $0$ | $1$ | $0$ | $1$ | $0$ | $0$ | $0$ | $(2/5,\; 4/25)$ | `[0.50787345, 0.50787346]` |
| $1$ | $1$ | $0$ | $1$ | $1$ | $1$ | $0$ | $(9/20,\; 81/400)$ | `[0.58284289, 0.58284290]` |
| $2$ | $0$ | $0$ | $1$ | $0$ | $0$ | $0$ | $(19/40,\; 361/1600)$ | `[0.62353269, 0.62353270]` |
| $3$ | $4$ | $0$ | $2$ | $2$ | $2$ | $0$ | — | — |
| $4$ | $0$ | $0$ | $1$ | $0$ | $0$ | $0$ | — | — |
| $5$ | $10$ | $0$ | $3$ | $5$ | $5$ | $0$ | — | — |
| $6$ | $16$ | $0$ | $4$ | $8$ | $8$ | $0$ | — | — |
| $7$ | $50$ | $0$ | $5$ | $25$ | $25$ | $13$ | — | — |
| $8$ | $110$ | $1$ | $7$ | $2n + 46$ | $58$ | $42$ | — | — |
| $9$ | $264$ | $1$ | $9$ | $4n + 116$ | $136$ | $109$ | — | — |
| $10$ | $610$ | $1$ | $11$ | $12n + 241$ | $284$ | $248$ | — | — |
| $11$ | $1394$ | $1$ | $13$ | $22n + 574$ | $568$ | $503$ | — | — |

*Table 1: Left: Complete compressed skeleton counts $|\mathcal{S}_{1, k}|$, polynomial degrees, stabilization horizons $n_0(1, k)$, and exact all-$n$ closed-form polynomials for $N_n^{\mathrm{off}}(2n + k; 1)$ ($0 \le k \le 11$), alongside direct mod-$3^6$ off-diagonal collision counts at $n = 6$ for $d \in \{1, 2\}$ (matching the filter-free $(\delta, \xi)$-automaton DP across $0 \le k \le 14$; at $k = 8$, $2(6) + 46 = 58$ already agrees at $n = 6$, while $k = 9, 10, 11$ stabilize at $n \ge 9, 11, 13$). Right: Certified outward-rounded bounds on the sub-Cramér excess concentration threshold $\kappa_*(u) < 2/3$ (Theorem 1(4)).*

---

## 3. Mod-$3^{j-1}$ Fiber Alignment Obstruction and Missing-Sibling Martingale Transfer

### 3.1 Telescoping Carry-Twist Identity and Pointwise Fiber Alignment Obstruction

To test whether off-diagonal inner products $I_j^{(\rho)}(d)$ can be controlled by uniform fiberwise contraction from $\mathcal{G}_{j-1}$ to $\mathcal{G}_j$, write $\mu_j^{(\rho)}(x_0 + t \cdot 3^{j-1}) = \frac{1}{3}\mu_{j-1}^{(\rho)}(x_0) + \Delta_j^{(\rho)}(x_0, t)$ for $j \ge 2$, $x_0 \in \mathcal{G}_{j-1}$, and $t \in \{0, 1, 2\}$, where $\sum_{t=0}^2 \Delta_j^{(\rho)}(x_0, t) = 0$. Similarly, on $\mathcal{G}_r$ at $\rho = 1/2$, set $(\Delta_r\mu)(z) := \mu_r(z) - \frac{1}{3}\mu_{r-1}(z \bmod 3^{r-1})$ (extended by $(\Delta_r\mu)(z) := 0$ on $3\mathbb{Z}/3^r\mathbb{Z}$, where both $\mu_r$ and $\mu_{r-1}$ vanish), and for $r \ge 2$ define the **canonical numerator lift** of $w' \in \{1, 2\}^{r-1}$ into $\mathcal{G}_r$ by
$$
\tau_{r-1}^{\mathrm{lift}}(w') := \bigl(2^{-\|w'\|} N_{r-1}(w')\bigr) \bmod 3^r \in \mathcal{G}_r, \qquad B_{r-1}^{\mathrm{lift}} := \bigl\{\tau_{r-1}^{\mathrm{lift}}(w') : w' \in \{1, 2\}^{r-1}\bigr\} \subseteq \mathcal{G}_r. \tag{3.1}
$$

**Theorem 2 (Telescoping Carry-Twist Identity, Fiber Alignment Obstruction, and Missing-Sibling Martingale Transfer).**
1. *(Exact Mod-$3^{j-1}$ Fiber Transfer, Telescoping Carry-Twist Increment, and $j = 7$ Obstruction).* For every $j \ge 2$, $\rho \in (0, 1)$, and $d \ge 1$, write $T_d^{(j)}(x_0) = y_0 + \sigma_d(x_0)\cdot 3^{j-1}$ for each $x_0 \in \mathcal{G}_{j-1}$ with $T_d^{(j-1)}(x_0) =: y_0 \in \mathcal{G}_{j-1}$, where $\sigma_d(x_0) := \bigl\lfloor \frac{4^d x_0 + (4^d - 1)/3}{3^{j-1}}\bigr\rfloor \bmod 3 \in \{0, 1, 2\}$ is the top-trit carry. Then $E_j^{(\rho)} - E_{j-1}^{(\rho)} = 3^j \sum_{x_0 \in \mathcal{G}_{j-1}} \sum_{t=0}^2 \Delta_j^{(\rho)}(x_0, t)^2$, and
   $$
   I_j^{(\rho)}(d) = 3^{j-1} \sum_{\substack{x_0 \in \mathcal{G}_{j-1} \\ T_d^{(j-1)}(x_0) \in \mathcal{G}_{j-1}}} \mu_{j-1}^{(\rho)}(x_0)\,\mu_{j-1}^{(\rho)}(y_0)\, F_j^{(\rho)}(x_0; d), \qquad F_j^{(\rho)}(x_0; d) := 1 + \frac{3\sum_{t=0}^2 \Delta_j^{(\rho)}(x_0, t)\,\Delta_j^{(\rho)}\bigl(y_0, (\sigma_d(x_0) + t) \bmod 3\bigr)}{\mu_{j-1}^{(\rho)}(x_0)\,\mu_{j-1}^{(\rho)}(y_0)}, \tag{3.2}
   $$
   yielding the exact telescoping increment $I_j^{(\rho)}(d) - I_{j-1}^{(\rho)}(d) = 3^j \sum_{x_0 : T_d^{(j-1)}(x_0) \in \mathcal{G}_{j-1}} \sum_{t=0}^2 \Delta_j^{(\rho)}(x_0, t)\,\Delta_j^{(\rho)}(y_0, (\sigma_d(x_0) + t) \bmod 3)$ with $|I_j^{(\rho)}(d) - I_{j-1}^{(\rho)}(d)| \le E_j^{(\rho)} - E_{j-1}^{(\rho)}$. However, **uniform pointwise fiber contraction below the diagonal collision base $\frac{3(1 - \rho)}{1 + \rho}$ is false**: at depth $j = 7$ and $d = 1$, the residue $x_0^* = 430 \in \mathcal{G}_6$ satisfies $F_7^{(\rho)}(430; 1) > \frac{3(1 - \rho)}{1 + \rho}$ strictly across all $\rho \in \{2/5, 9/20, 19/40, 1/2\}$ (Table 2).
2. *(Exact Missing-Sibling Fiber Complementarity and Martingale Difference Transfer).*
   - *(a) Missing-sibling partition and $4 B_r$ mass law:* For every $r \ge 2$ and $w' \in \{1, 2\}^{r-1}$, $\{\tau_r(1, w'), \tau_r(2, w'), \tau_{r-1}^{\mathrm{lift}}(w')\} = \pi_{r, r-1}^{-1}(\{\tau_{r-1}(w')\})$ partitions the full $3$-element mod-$3^{r-1}$ fiber above $\tau_{r-1}(w')$, so $B_r \sqcup B_{r-1}^{\mathrm{lift}} = \pi_{r, r-1}^{-1}(B_{r-1})$ ($|B_{r-1}^{\mathrm{lift}}| = 2^{r-1}$). Consequently, for **all** $r \ge 2$:
     $$
     \mu_r(B_r) = \mu_{r-1}(B_{r-1}) - \mu_r\bigl(B_{r-1}^{\mathrm{lift}}\bigr), \qquad \mu_r(4 B_r) = \mu_{r-1}(B_{r-1}) - 4\mu_r\bigl(B_{r-1}^{\mathrm{lift}}\bigr), \tag{3.3}
     $$
     forcing $\mu_r(B_{r-1}^{\mathrm{lift}}) < \frac{1}{4}\mu_{r-1}(B_{r-1}) < \frac{1}{3}\mu_{r-1}(B_{r-1})$ and the exact single-shell martingale identity
     $$
     S_r(1) = -3^r (\Delta_r\mu)\!\bigl(B_{r-1}^{\mathrm{lift}}\bigr) \;>\; 0 \qquad (\forall\, r \ge 2). \tag{3.4}
     $$
   - *(b) Shifted missing-sibling identity for $S_r(4)$, $m = 1$ half-ejection, and $r \le 13$ certification:* For every $j \ge 2$ and $w'' \in \{1, 2\}^{j-2}$, $T_1^{(j)}\bigl(\tau_{j-1}^{\mathrm{lift}}(w'', 1)\bigr) \equiv 0 \pmod 3$ (ejecting exact half of $B_{j-1}^{\mathrm{lift}}$ into $3\mathbb{Z}/3^j\mathbb{Z}$ where $\Delta_j\mu \equiv 0$) while $T_1^{(j)}\bigl(\tau_{j-1}^{\mathrm{lift}}(w'', 2)\bigr) \equiv 2 + 3\tau_{j-2}^{\mathrm{lift}}(w'') \pmod{3^j}$. Across **all** $r \ge 3$,
     $$
     Z_r(1/2) - \frac{8}{9} Z_{r-1}(1/2) = -\left(\frac{4}{3}\right)^{r-1} \sum_{m=1}^\infty 4^{-m}\, (\Delta_{r-1}\mu)\!\bigl(T_m^{(r-1)}(B_{r-2}^{\mathrm{lift}})\bigr), \qquad S_r(4) = -3^{r+1} \sum_{m=1}^\infty 4^{-m}\, (\Delta_{r-1}\mu)\!\bigl(T_m^{(r-1)}(B_{r-2}^{\mathrm{lift}})\bigr), \tag{3.5}
     $$
     certified **strictly negative** ($S_r(4) < 0$, equivalently $Z_r(1/2)/Z_{r-1}(1/2) < 8/9$) across all shells $2 \le r \le 13$ (Table 2).

*Proof.* **Part 1.** Because $4^d \equiv 1 \pmod 3$, for every $x_0 \in \mathcal{G}_{j-1}$ and $t \in \{0, 1, 2\}$ we have $T_d^{(j)}(x_0) \in \mathcal{G}_j \iff T_d^{(j-1)}(x_0) \in \mathcal{G}_{j-1}$ (as $j - 1 \ge 1$) and $T_d^{(j)}(x_0 + t \cdot 3^{j-1}) = y_0 + \bigl((\sigma_d(x_0) + t) \bmod 3\bigr)\cdot 3^{j-1}$. Expanding $\sum_{t=0}^2 (\frac{1}{3}\mu_{j-1}^{(\rho)}(x_0) + \Delta_j^{(\rho)}(x_0, t))(\frac{1}{3}\mu_{j-1}^{(\rho)}(y_0) + \Delta_j^{(\rho)}(y_0, (\sigma_d(x_0)+t)\bmod 3))$ cancels both cross terms because $\sum_{t=0}^2 \Delta_j^{(\rho)}(\cdot, t) = 0$, proving $(3.2)$. Separating the leading $1$ in $F_j^{(\rho)}(x_0; d)$ recovers $I_{j-1}^{(\rho)}(d)$ identically, and Cauchy–Schwarz across $(x_0, t)$ gives $|I_j^{(\rho)}(d) - I_{j-1}^{(\rho)}(d)| \le E_j^{(\rho)} - E_{j-1}^{(\rho)}$. Exact common-denominator integer evaluation at $j = 7, d = 1$ certifies $F_7^{(\rho)}(430; 1) > \frac{3(1-\rho)}{1+\rho}$ in Table 2.

**Part 2.** For $w = (e, w')$ ($e \in \{1, 2\}, w' \in \{1, 2\}^{r-1}$), $N_r(e, w') = 3^{r-1} + 2^e N_{r-1}(w')$, so $\tau_r(e, w') \equiv \tau_{r-1}^{\mathrm{lift}}(w') + 2^{-e}\cdot 3^{r-1} \pmod{3^r}$. Since $\{0, 2^{-1} \bmod 3, 2^{-2} \bmod 3\} = \{0, 2, 1\}$, $\{\tau_{r-1}^{\mathrm{lift}}(w'), \tau_r(1, w'), \tau_r(2, w')\}$ is the exact $3$-element fiber above $\tau_{r-1}(w')$, proving $B_r \sqcup B_{r-1}^{\mathrm{lift}} = \pi_{r, r-1}^{-1}(B_{r-1})$ and the first identity in $(3.3)$ via $\mu_r(\pi_{r, r-1}^{-1}(B_{r-1})) = \mu_{r-1}(B_{r-1})$. Next, $U_r = U_{r-1} + Z_r(1/2)$ [29, Eq. (1.4)] reads $(4/3)^r \mu_r(B_r) = (4/3)^{r-1}\mu_{r-1}(B_{r-1}) + \frac{1}{4}(4/3)^r \mu_r(4 B_r)$, i.e., $\mu_r(4 B_r) = 4\mu_r(B_r) - 3\mu_{r-1}(B_{r-1}) = \mu_{r-1}(B_{r-1}) - 4\mu_r(B_{r-1}^{\mathrm{lift}})$, proving $(3.3)$. Substituting $(3.3)$ into $S_r(1) = 3^r \mu_r(B_r) - 2 \cdot 3^{r-1}\mu_{r-1}(B_{r-1})$ [29, Section 5] gives $S_r(1) = 3^r(\frac{1}{3}\mu_{r-1}(B_{r-1}) - \mu_r(B_{r-1}^{\mathrm{lift}})) = -3^r(\Delta_r\mu)(B_{r-1}^{\mathrm{lift}}) > 0$ (since $\mu_r(4 B_r) > 0 \implies \mu_r(B_{r-1}^{\mathrm{lift}}) < \frac{1}{4}\mu_{r-1}(B_{r-1})$).

For $j \ge 2$ and $w' = (w'', e)$, $N_{j-1}(w'', e) = 3 N_{j-2}(w'') + 2^{\|w''\|}$ gives $\tau_{j-1}^{\mathrm{lift}}(w'', e) \equiv 2^{-e} + 3 \cdot 2^{-e}\tau_{j-2}^{\mathrm{lift}}(w'') \pmod{3^j}$, so $T_1^{(j)}(\tau_{j-1}^{\mathrm{lift}}(w'', e)) \equiv (4 \cdot 2^{-e} + 1) + 3 \cdot 2^{2-e}\tau_{j-2}^{\mathrm{lift}}(w'') \pmod{3^j}$, which equals $3(1 + 2\tau_{j-2}^{\mathrm{lift}}(w'')) \equiv 0 \pmod 3$ for $e = 1$ and $2 + 3\tau_{j-2}^{\mathrm{lift}}(w'') \pmod{3^j}$ for $e = 2$. Finally, for any $r \ge 3$ and $m \ge 1$, applying the bijection $T_m^{(r-1)}$ to $B_{r-1} \sqcup B_{r-2}^{\mathrm{lift}} = \pi_{r-1, r-2}^{-1}(B_{r-2})$ yields $T_m^{(r-1)}(B_{r-1}) \sqcup T_m^{(r-1)}(B_{r-2}^{\mathrm{lift}}) = \pi_{r-1, r-2}^{-1}(T_m^{(r-2)}(B_{r-2}))$. Taking $\mu_{r-1}$-measure gives $\mu_{r-1}(T_m^{(r-1)}(B_{r-1})) - \frac{2}{3}\mu_{r-2}(T_m^{(r-2)}(B_{r-2})) = -(\Delta_{r-1}\mu)(T_m^{(r-1)}(B_{r-2}^{\mathrm{lift}}))$; summing against $(4/3)^{r-1} 4^{-m}$ via [29, Eqs. (5.5), (5.7)] proves $(3.5)$. Outward-rounded $160$-bit interval evaluation certifies $S_r(4) < 0$ through $r = 13$. $\blacksquare$

| Parameter $\rho$ ($u = \rho^2$) | Diagonal Base $\frac{3(1-\rho)}{1+\rho}$ | $\max_{x_0 \in \mathcal{G}_6} F_7^{(\rho)}(x_0; 1)$ ($x_0^* = 430$) | Excess Margin Above Base | $r = 13$ Subcritical $Z_{13}^{(u)}(\rho)/Z_{12}^{(u)}(\rho)$ | Haar Base $\frac{1+\rho}{3(1-\rho)}$ | Binary Shell $r$ | Certified $Z_r(1/2)$ | Scaled $(4/9)^r S_r(4)$ ($< 0$) | $Z_r / Z_{r-1}$ ($< 8/9$) |
|---|---|---|---|---|---|---:|---|---|---|
| $2/5$ ($4/25$) | `[1.28571428, 1.28571429]` | `[1.32150737, 1.32150738]` | `+0.03579308` | `[0.8647441, 0.8647442]` | `0.7777778` | $4$ | `[0.1949373941, 0.1949373942]` | `[-0.004662174, -0.004662173]` | `[0.88360575, 0.88360576]` |
| $9/20$ ($81/400$) | `[1.13793103, 1.13793104]` | `[1.20652005, 1.20652006]` | `+0.06858902` | `[0.8983285, 0.8983286]` | `0.8787879` | $8$ | `[0.1093218983, 0.1093218984]` | `[-0.010098081, -0.010098080]` | `[0.86882550, 0.86882551]` |
| $19/40$ ($361/1600$) | `[1.06779661, 1.06779662]` | `[1.15887765, 1.15887766]` | `+0.09108104` | `[0.9428474, 0.9428475]` | `0.9365080` | $12$ | `[0.0631817730, 0.0631817731]` | `[-0.003357569, -0.003357568]` | `[0.87723451, 0.87723452]` |
| $1/2$ ($1/4$) | `[1.00000000, 1.00000000]` | `[1.11812997, 1.11812998]` | `+0.11812997` | — | `1.0000000` | $13$ | `[0.0555217471, 0.0555217472]` | **`[-0.002559316, -0.002559315]`** | `[0.87876209, 0.87876210]` |

*Table 2: Left: Exact rational certification at $j = 7$ that $\max_{x_0 \in \mathcal{G}_6} F_7^{(\rho)}(x_0; 1)$ (attained universally at $x_0^* = 430$) strictly exceeds $\frac{3(1-\rho)}{1+\rho}$, alongside $r = 13$ subcritical step ratios (with $I_{13}^{(\rho)}(1)$ bounded in `[2.982616, 2.982617]`, `[1.109396, 1.109397]`, and `[0.847544, 0.847545]` at $\rho = 2/5, 9/20, 19/40$, where at $\rho = 2/5$ the cycle-shadow floor base $1 - u = 0.84$ exceeds the Haar base $7/9$ [29]). Right: Representative shells from the $2 \le r \le 13$ missing-sibling certification (exact rationals for $2 \le r \le 8$, where at $r = 4$ the $m = 1$ summand carries `[3.153625, 3.153626]` of the net negative sum due to $m \ge 2$ sign oscillation; $160$-bit intervals through $r = 13$, all satisfying $S_r(4) < 0$ and $Z_r / Z_{r-1} < 8/9 = 0.\overline{8}$).*

![Off-diagonal pullback skeleton growth, fiber alignment obstruction, and subcritical renewal ratios](supplement/figure-1.png)

*Figure 1: (a) Exact off-diagonal collision polynomials $N_n^{\mathrm{off}}(2n + k; 1)$ ($n = 6$ direct counts vs. exact asymptotic constant/linear skeleton laws, Theorem 1(3)). (b) Depth-$7$ Fiber-Wise Pointwise Alignment Obstruction $\max_{x_0 \in \mathcal{G}_6} F_7^{(\rho)}(x_0; 1) > \frac{3(1-\rho)}{1+\rho}$ at $x_0^* = 430$ across $\rho \in \{2/5, 9/20, 19/40, 1/2\}$ (Theorem 2(1)). (c) Certified subcritical renewal step ratios $Z_r^{(u)}(\sqrt{u})/Z_{r-1}^{(u)}(\sqrt{u})$ through $r = 13$ ($\phi(3^{13}) = 1{,}062{,}882$) compared against Haar prefactor bases $\frac{1+\rho}{3(1-\rho)}$ (dashed) and discrete cycle-shadow floor bases $1 - u$ (dotted).*

---

## 4. Backward Cosine Supermartingale and Unconditional Uniform Fourier Decay on $\mathcal{G}_m$

We now resolve the uniform primitive-shell Fourier decay question from [29, Section 6]. Recall that Tao's adjacent-pair conditioning mechanism [7, Section 7.1], specialized in [29, Eq. (5.4)] to $w \sim \mathrm{Unif}(\{1, 2\}^{2K})$, expresses $|\widehat{\mathbf{1}_{B_{2K}}}(b)|/2^{2K}$ via expectations of products over heterogeneous blocks $\{w_{2k-1}, w_{2k}\} = \{1, 2\}$. A key obstacle at dyadic frequencies $b = 2^{3K - O(1)} \bmod 3^{2K}$ (such as $\{128, 6433\}$ at $2K = 8$) is that high $2$-adic valuation traps $b \cdot 2^{-T_k}$ near $0 \bmod 3^{2k}$ across macro-scale intervals where $8^k \ll 9^k$. Theorem 3 overcomes this dyadic trapping unconditionally by combining a backward supermartingale with congruence-to-$\mathbb{Z}$ promotion (cf. [30] on actual trajectories) and a cube-root stopping-scale cascade.

**Theorem 3 (Backward Cosine Supermartingale and Unconditional Uniform $\ell^\infty(\mathcal{G}_m)$ Decay).**
1. *(Odd-to-Even Reduction and Backward Supermartingale).* For every $K \ge 1$, $\max_{b \in \mathcal{G}_{2K+1}} |\widehat{\mathbf{1}_{B_{2K+1}}}(b)|/2^{2K+1} \le \max_{b' \in \mathcal{G}_{2K}} |\widehat{\mathbf{1}_{B_{2K}}}(b')|/2^{2K}$. For $m = 2K \ge 2$ and any fixed $b \in \mathcal{G}_{2K}$, let $\sigma_1, \dots, \sigma_K$ be i.i.d. block sums with $\mathbb{P}(\sigma_k = 2) = \mathbb{P}(\sigma_k = 4) = 1/4$ and $\mathbb{P}(\sigma_k = 3) = 1/2$, set $T_k := \sum_{j=k+1}^K \sigma_j$ ($T_K := 0$) adapted to $\mathcal{F}_k^{\mathrm{back}} := \sigma(\sigma_{k+1}, \dots, \sigma_K)$, and define the balanced residue $z_k := \langle b \cdot 2^{-T_k} \rangle_{3^{2k}} \in \mathcal{G}_{2k}$, the non-aligned zone $\mathcal{E}_k := \bigl\{z \in \mathcal{G}_{2k} : \frac{|z|}{3^{2k}} \ge \frac{1}{36}\bigr\}$ ($1 \in \mathcal{E}_1$ deterministically), and $Y_k := \mathbf{1}_{\{\sigma_k \ne 3\}} + \mathbf{1}_{\{\sigma_k = 3\}}|\cos(2\pi r_k / 3^{2k})|$ where $r_k := (b \cdot 2^{-(T_k + 3)}) \bmod 3^{2k}$. Then with
   $$
   \beta_0 := \frac{1 + \cos(\pi/144)}{2} \in [\mathbf{0.9998810135}, \mathbf{0.9998810136}] \;<\; 1, \tag{4.1}
   $$
   the backward process $W_j := \prod_{k=j}^K \bigl(Y_k \beta_0^{-\mathbf{1}_{\{z_k \in \mathcal{E}_k\}}}\bigr)$ ($W_{K+1} := 1$) satisfies $\mathbb{E}[W_j \mid \mathcal{F}_j^{\mathrm{back}}] \le W_{j+1}$, hence $\mathbb{E}[W_1] \le 1$ and $|\widehat{\mathbf{1}_{B_{2K}}}(b)|/2^{2K} \le \beta_0^R + \mathbb{P}\bigl(\sum_{k=1}^K \mathbf{1}_{\{z_k \in \mathcal{E}_k\}} < R\bigr)$ for every integer $R \ge 1$.
2. *(Exact $2$-Adic Integer Locking and Unconditional Uniform Decay Across All $m \ge 3$).* Whenever $z_k \notin \mathcal{E}_k$ and $z_{k+1} \notin \mathcal{E}_{k+1}$ ($1 \le k < K$), the modular relation $2^{\sigma_{k+1}} z_k \equiv z_{k+1} \pmod{3^{2k}}$ promotes to the exact integer identity $z_{k+1} = 2^{\sigma_{k+1}} z_k$ in $\mathbb{Z}$. Consequently, there exists an explicit absolute constant $C_B > 0$ such that for **every** integer $m \ge 3$ (both even and odd):
   $$
   \max_{b \in \mathcal{G}_m} \frac{\bigl|\widehat{\mathbf{1}_{B_m}}(b)\bigr|}{2^m} \;\le\; C_B \left(\frac{\ln\ln m}{\ln m}\right)^{\gamma_B} \;\xrightarrow[m \to \infty]{}\; 0, \qquad \gamma_B := \frac{\ln(1/\beta_0)}{\ln 3} \in [\mathbf{0.0001083125}, \mathbf{0.0001083126}]. \tag{4.2}
   $$

*Proof.* **Part 1.** Writing $u = (w', e) \in \{1, 2\}^{2K+1}$ ($w' \in \{1, 2\}^{2K}, e \in \{1, 2\}$) gives $\tau_{2K+1}(w', e) \equiv (1 + 3\tau_{2K}(w'))2^{-e} \pmod{3^{2K+1}}$. For $b \in \mathcal{G}_{2K+1}$, setting $b_e := (b \cdot 2^{-e}) \bmod 3^{2K} \in \mathcal{G}_{2K}$ gives $\frac{b \tau_{2K+1}(w', e)}{3^{2K+1}} \equiv \frac{(b \cdot 2^{-e}) \bmod 3^{2K+1}}{3^{2K+1}} + \frac{b_e \tau_{2K}(w')}{3^{2K}} \pmod 1$, so the triangle inequality over $e \in \{1, 2\}$ yields $\frac{1}{2^{2K+1}}|\widehat{\mathbf{1}_{B_{2K+1}}}(b)| \le \frac{1}{2^{2K+1}}\bigl(|\widehat{\mathbf{1}_{B_{2K}}}(b_1)| + |\widehat{\mathbf{1}_{B_{2K}}}(b_2)|\bigr) \le \max_{b' \in \mathcal{G}_{2K}} |\widehat{\mathbf{1}_{B_{2K}}}(b')|/2^{2K}$.

For $m = 2K$ and $b \in \mathcal{G}_{2K}$, [29, Eq. (5.4)] gives $|\widehat{\mathbf{1}_{B_{2K}}}(b)|/2^{2K} \le \mathbb{E}[\prod_{k=1}^K Y_k]$. At scale $k$, $z_k$ is $\mathcal{F}_k^{\mathrm{back}}$-measurable while $\sigma_k$ is independent of $\mathcal{F}_k^{\mathrm{back}}$. Let $w_k := \langle 4^{-1} z_k \rangle_{3^{2k}} \in (-\frac{1}{2}\cdot 3^{2k}, \frac{1}{2}\cdot 3^{2k})$. Because $2 r_k \equiv w_k \pmod{3^{2k}}$ and $3^{2k}$ is odd, $r_k \equiv \frac{w_k}{2} \pmod{3^{2k}}$ when $w_k$ is even and $r_k \equiv \frac{w_k + 3^{2k}}{2} \pmod{3^{2k}}$ when $w_k$ is odd; in both cases $|\cos(2\pi r_k / 3^{2k})| = \cos(\pi |w_k|/3^{2k})$. If $z_k \in \mathcal{E}_k$ ($|z_k| \ge \frac{1}{36}\cdot 3^{2k}$), then $|w_k| \ge \frac{1}{144}\cdot 3^{2k}$ (otherwise $|4 w_k - z_k| < (\frac{1}{36} + \frac{1}{2})3^{2k} < 3^{2k}$ with $3^{2k} \mid (4 w_k - z_k)$ would force $z_k = 4 w_k$ and $|z_k| < \frac{1}{36}\cdot 3^{2k}$), so $|\cos(2\pi r_k/3^{2k})| \le \cos(\pi/144)$ and $\mathbb{E}[Y_k \mid \mathcal{F}_k^{\mathrm{back}}] = \frac{1}{2} + \frac{1}{2}\cos(\pi |w_k|/3^{2k}) \le \beta_0$. At $k = 1$, $|z_1|/9 \ge 1/9 > 1/36$, so $1 \in \mathcal{E}_1$. Thus $\mathbb{E}[W_j \mid \mathcal{F}_j^{\mathrm{back}}] = W_{j+1}\beta_0^{-\mathbf{1}_{\{z_j \in \mathcal{E}_j\}}}\mathbb{E}[Y_j \mid \mathcal{F}_j^{\mathrm{back}}] \le W_{j+1}$ and $\mathbb{E}[W_1] \le 1$, yielding $\mathbb{E}[\prod_{k=1}^K Y_k] \le \beta_0^R \mathbb{E}[W_1] + \mathbb{P}(\sum_{k=1}^K \mathbf{1}_{\{z_k \in \mathcal{E}_k\}} < R)$.

**Part 2.** Since $z_{k+1} \equiv b \cdot 2^{-T_{k+1}} \pmod{3^{2k+2}}$ and $z_k \equiv b \cdot 2^{-(T_{k+1} + \sigma_{k+1})} \pmod{3^{2k}}$, we have $2^{\sigma_{k+1}} z_k \equiv z_{k+1} \pmod{3^{2k}}$. If $z_k \notin \mathcal{E}_k$ and $z_{k+1} \notin \mathcal{E}_{k+1}$, then $\sigma_{k+1} \le 4$ gives $|2^{\sigma_{k+1}} z_k - z_{k+1}| < \frac{16}{36}\cdot 3^{2k} + \frac{1}{36}\cdot 3^{2k+2} = \frac{25}{36}\cdot 3^{2k} < 3^{2k}$, forcing $z_{k+1} = 2^{\sigma_{k+1}} z_k$ in $\mathbb{Z}$.

Assume $K \ge e^{e^3}$ (smaller $m$ are absorbed into $C_B$). Set $h_0 := K$, $R := \bigl\lfloor \frac{\ln\ln K - \ln\ln\ln K - \ln 4}{\ln 3}\bigr\rfloor \ge 1$, and $h_r := \lfloor (h_{r-1} - 1)^{1/3}\rfloor$ for $1 \le r \le R$. Because $x \ge 65 \implies \lfloor(x-1)^{1/3}\rfloor > \frac{1}{2}x^{1/3}$ and $3^{-R}\ln K \ge 4\ln\ln K$, induction yields $h_r > \frac{1}{2\sqrt{2}} K^{3^{-r}} \ge \frac{1}{2\sqrt{2}}(\ln K)^4 > (\ln K)^3 \ge 27$ for all $1 \le r \le R$ (and $h_{r-1} > 65$). Partition into disjoint blocks $J_r := \{a_r, \dots, h_{r-1}\}$ where $a_r := h_r + 1$, of step length $N_r := h_{r-1} - a_r \ge h_r^3 - h_r \ge \frac{15}{16} h_r^3$, and set $B_r := \bigcap_{j \in J_r} \{z_j \notin \mathcal{E}_j\}$. On $B_r$, iterating integer locking gives $z_{h_{r-1}} = 2^{\sum_{j = a_r + 1}^{h_{r-1}} \sigma_j} z_{a_r}$ in $\mathbb{Z}$, hence $\sum_{j = a_r + 1}^{h_{r-1}} \sigma_j = v_2(|z_{h_{r-1}}|) - v_2(|z_{a_r}|)$. Since $z_{a_r} \in \mathcal{G}_{2 a_r} \setminus \mathcal{E}_{a_r}$ satisfies $1 \le 2^{v_2(|z_{a_r}|)} \le |z_{a_r}| < \frac{9^{a_r}}{36} < \frac{16^{a_r}}{36} < 2^{4 a_r - 5}$, $v_2(|z_{a_r}|)$ takes at most $4 a_r - 5 = 4 h_r - 1 < 4 h_r$ integer values, while $v_2(|z_{h_{r-1}}|)$ is $\mathcal{F}_{h_{r-1}}^{\mathrm{back}}$-measurable. Since $\sigma_j - 2 \stackrel{\mathrm{i.i.d.}}{\sim} \mathrm{Bin}(2, 1/2)$, $\sum_{j=a_r+1}^{h_{r-1}}(\sigma_j - 2) \sim \mathrm{Bin}(2 N_r, 1/2)$ has maximum point mass $\binom{2 N_r}{N_r} 2^{-2 N_r} < \frac{1}{\sqrt{\pi N_r}}$, giving
$$
\mathbb{P}\bigl(B_r \;\big|\; \mathcal{F}_{h_{r-1}}^{\mathrm{back}}\bigr) \;\le\; \frac{4 h_r}{\sqrt{\pi N_r}} \;\le\; \frac{16}{\sqrt{15\pi}}\, h_r^{-1/2} \;<\; \frac{5}{2}\, h_r^{-1/2}.
$$
Because $h_{r-1} > 4 h_r$, $h_{r-1}^{-1/2} < \frac{1}{2} h_r^{-1/2}$, so $\mathbb{P}(\sum_{k=1}^K \mathbf{1}_{\{z_k \in \mathcal{E}_k\}} < R) \le \sum_{r=1}^R \mathbb{P}(B_r) < 5 h_R^{-1/2} < 5(\ln K)^{-3/2}$, while $\beta_0^R \le 12^{\gamma_B}\bigl(\frac{\ln\ln K}{\ln K}\bigr)^{\gamma_B}$. Since $\gamma_B < 3/2$ and odd $m = 2K + 1$ reduces to $2K$ by Part 1, $(4.2)$ holds for all $m \ge 3$. $\blacksquare$

| Shell Depth $m$ | Parity | Global Maximizing Conjugate Pair $\{b^*, 3^m - b^*\} \subset \mathcal{G}_m$ | Certified $\max_{b \in \mathcal{G}_m} \|\widehat{\mathbf{1}_{B_m}}(b)\|/2^m$ | Odd-to-Even Bound Verified |
|---:|---|---|---:|---|
| $2$ | even | $\{4, 5\}$ | `[0.46984631, 0.46984632]` | — |
| $3$ | odd | $\{7, 20\}$ | `[0.42572028, 0.42572029]` | $\le \max_{\mathcal{G}_2}$ (`0.46984632`) |
| $4$ | even | $\{28, 53\}$ | `[0.32270128, 0.32270129]` | — |
| $5$ | odd | $\{79, 164\}$ | `[0.27250151, 0.27250152]` | $\le \max_{\mathcal{G}_4}$ (`0.32270129`) |
| $6$ | even | $\{316, 413\}$ | `[0.23820446, 0.23820447]` | — |
| $7$ | odd | $\{583, 1604\}$ | `[0.16664557, 0.16664558]` | $\le \max_{\mathcal{G}_6}$ (`0.23820447`) |
| $8$ | even | $\{128, 6433\} = \{\pm 2^7 \bmod 3^8\}$ | `[0.14945885, 0.14945886]` | — |
| $9$ | odd | $\{512, 19171\} = \{\pm 2^9 \bmod 3^9\}$ | `[0.14134444, 0.14134445]` | $\le \max_{\mathcal{G}_8}$ (`0.14945886`) |

*Table 3: Exhaustive outward-rounded conjugate-pair sup-norms $\max_{b \in \mathcal{G}_m} |\widehat{\mathbf{1}_{B_m}}(b)|/2^m$ across both even and odd shells $2 \le m \le 9$ ($3{,}359{,}232$ conjugate-pair $\times$ fiber evaluations at $m = 9$, where the dyadic pair $\{512, 19171\} = \{\pm 2^9 \bmod 3^9\}$ attains the global maximum strictly below $\max_{\mathcal{G}_8}$), alongside exhaustive verification of $\mathbb{E}[W_1] \le 1$ across all `546` primitive frequencies $b \in \mathcal{G}_{2K}$ ($K = 1, 2, 3$) and `90` contiguous integer-locking transitions.*

---

## 5. Two-Step Adelic Cosine Recurrence, Uniform Cantor Decay, and Perpetuity Slice Law

On the $2$-adic side of the adelic reciprocity law [29, Eq. (5.2)], the single-step Cantor Fourier recurrence $|\psi_r(a)| \le \frac{1}{2}|\psi_{r-1}(b)| + \frac{1}{2}|\psi_{r-2}(b)|$ ($b \equiv 3^{-1}a \pmod{2^r}$) loses all phase information under the triangle inequality. Unrolling **two** steps exposes an interior cosine contraction on the $\psi_{r-3}$ branch, while oddness of $u_t$ and $9^6 = 531{,}441 > 524{,}288 = 2^{19}$ eliminate macro-scale aligned runs completely and yield polynomial decay in $r$.

**Theorem 4 (Two-Step Adelic Cosine Recurrence, Uniform Polynomial Decay of $\psi_r(a)$, and Perpetuity Slice Convergence).**
1. *(Unrolled Two-Step Cosine Inequality and Uniform Polynomial Decay Over Odd Frequencies).* For every $r \ge 5$ and odd $a \in (\mathbb{Z}/2^r\mathbb{Z})^\times$, setting $b := (9^{-1} a) \bmod 2^r$ yields
   $$
   |\psi_r(a)| \;\le\; \frac{1}{4}|\psi_{r-2}(b \bmod 2^{r-2})| + \frac{1}{2}\left|\cos\!\left(2\pi \frac{b \bmod 2^{r-1}}{2^r}\right)\right||\psi_{r-3}(b \bmod 2^{r-3})| + \frac{1}{4}|\psi_{r-4}(b \bmod 2^{r-4})|. \tag{5.1}
   $$
   With $\eta_5 := \frac{1 + \cos(\pi/32)}{2} \in [\mathbf{0.9975923633}, \mathbf{0.9975923634}] < 1$, small-phase runs $u_t := \langle B_t \rangle_{2^{R_t - 1}}$ with $|u_t| < 2^{R_t}/64$ satisfy exact odd integer locking $u_j = 9 u_{j+1}$ in $\mathbb{Z}$ and rational drift-to-expansion slope ratio $\frac{31/10}{19/6} = \frac{93}{95} < 1$ ($2^{19} < 9^6$), establishing an explicit constant $C_\psi > 0$ such that for **all** $r \ge 1$:
   $$
   \max_{\substack{1 \le a < 2^r \\ a \text{ odd}}} |\psi_r(a)| \;\le\; C_\psi\, r^{-\gamma_\psi} \;\xrightarrow[r \to \infty]{}\; 0, \qquad \gamma_\psi := \frac{\ln(1/\eta_5)}{2 \ln 50} \in [\mathbf{0.0003080937}, \mathbf{0.0003080938}]. \tag{5.2}
   $$
2. *(Fractional Perpetuity Moment, Zero $2$-Adic Slice Truncation, and Geometric Archimedean Convergence).* Under $w \sim \mathrm{Unif}(\{1, 2\}^{\mathbb{N}})$, while $\mathbb{E}[Y_\infty] = \infty$, the square-root moment satisfies
   $$
   \mathbb{E}\bigl[Y_\infty^{1/2}\bigr] \;\le\; \frac{2}{2\sqrt{3} - \sqrt{2} - 2} \in [\mathbf{40.089758}, \mathbf{40.089759}]. \tag{5.3}
   $$
   Consequently, for every $K \ge 1$, every $1 \le c_0 \le 3K$, every $w \in \{1, 2\}^{2K}$ with dyadic slice index $d(w) := S_{2K}(w) - (3K - c_0)$, and every extension $w' \in \{1, 2\}^M$ ($M \ge 1$):
   - *(a) Exact zero $2$-adic truncation error:* $\bigl\{2^{-d(w)} Y_{2K + M}(w \cdot w')\bigr\}_2 = \bigl\{2^{-d(w)} Y_{2K}(w)\bigr\}_2$ identically.
   - *(b) Uniform geometric Archimedean convergence:* For the adelic reciprocity phase $\Phi_{m, d}(u) := \frac{(2^{S_m(u)-d}\tau_m(u))\bmod 3^m}{3^m}$ [29, Eq. (5.2)], uniformly over all $M \ge 1$:
     $$
     \Bigl|\mathbb{E}_{w, w'}\!\bigl[e^{-2\pi i \Phi_{2K + M, d(w)}(w \cdot w')}\bigr] - \mathbb{E}_w\!\bigl[e^{-2\pi i \Phi_{2K, d(w)}(w)}\bigr]\Bigr| \;\le\; 2\sqrt{\pi}\,\mathbb{E}\bigl[Y_\infty^{1/2}\bigr]\, 2^{-c_0/2} \left(\frac{2\sqrt{2}}{3}\right)^K, \tag{5.4}
     $$
     with geometric base $\frac{2\sqrt{2}}{3} \in [\mathbf{0.94280904}, \mathbf{0.94280905}] < 1$.

*Proof.* **Part 1.** Applying [29, Eq. (5.3)] twice at $r \ge 5$ with $b_1 := (3^{-1} a) \bmod 2^r$ and $b := (3^{-1} b_1) \bmod 2^r = (9^{-1} a) \bmod 2^r$ expresses $e^{-2\pi i b_1 / 2^r}\psi_r(a)$ as $\frac{1}{4}e^{2\pi i \theta_1}\psi_{r-2}(b \bmod 2^{r-2}) + \frac{1}{4}(e^{2\pi i \theta_1} + e^{2\pi i \theta_2})\psi_{r-3}(b \bmod 2^{r-3}) + \frac{1}{4}e^{2\pi i \theta_2}\psi_{r-4}(b \bmod 2^{r-4})$, where $\theta_1 := \frac{b \bmod 2^{r-1}}{2^{r-1}}$ and $\theta_2 := \frac{b \bmod 2^{r-2}}{2^{r-2}}$. Since $(b \bmod 2^{r-1}) \equiv (b \bmod 2^{r-2}) \pmod{2^{r-2}}$, we have $2\theta_1 \equiv \theta_2 \pmod 1$, so $\theta_2 - \theta_1 \equiv \theta_1 \pmod 1$ and $\bigl|\frac{e^{2\pi i \theta_1} + e^{2\pi i \theta_2}}{2}\bigr| = |\cos(\pi \theta_1)| = \bigl|\cos(2\pi \frac{b \bmod 2^{r-1}}{2^r})\bigr|$, proving $(5.1)$.

Iterating $(5.1)$ from $(R_0, A_0) = (r_0, a_0)$ ($r_0 \ge 50^8$; smaller $r_0$ are absorbed into $C_\psi$) via i.i.d. decrements $\Delta_1, \Delta_2, \dots \in \{2, 3, 4\}$ with law $(1/4, 1/2, 1/4)$, $B_t := (9^{-1} A_t) \bmod 2^{R_t}$, $R_{t+1} := R_t - \Delta_{t+1}$, $A_{t+1} := B_t \bmod 2^{R_{t+1}}$, stopping time $\tau := \min\{t \ge 0 : R_t \le 4\}$, and $D_{t+1} := \mathbf{1}_{\{\Delta_{t+1} \ne 3\}} + \mathbf{1}_{\{\Delta_{t+1} = 3\}}|\cos(2\pi (B_t \bmod 2^{R_t-1})/2^{R_t})|$ gives $|\psi_{r_0}(a_0)| \le \mathbb{E}[\prod_{t=1}^\tau D_t]$. Since $B_t$ is odd, $u_t := \langle B_t \rangle_{2^{R_t - 1}} \in (-2^{R_t-2}, 2^{R_t-2})$ satisfies $|\cos(2\pi (B_t \bmod 2^{R_t-1})/2^{R_t})| = \cos(2\pi |u_t|/2^{R_t})$. On $G_t := \{|u_t| \ge 2^{R_t}/64\}$, $\mathbb{E}[D_{t+1} \mid \mathcal{F}_t] \le \eta_5$, so $M_t := \prod_{j=1}^{t \wedge \tau}(D_j \eta_5^{-\mathbf{1}_{G_{j-1}}})$ is a supermartingale with $\mathbb{E}[M_\tau] \le 1$ and $|\psi_{r_0}(a_0)| \le \eta_5^L + \mathbb{P}(\sum_{t=0}^{\tau - 1} \mathbf{1}_{G_t} < L)$. If $j + 1 < \tau$ and $G_j^c \cap G_{j+1}^c$ holds, then $R_{j+1} \le R_j - 2 \implies 9 u_{j+1} \equiv A_{j+1} \equiv u_j \pmod{2^{R_{j+1}-1}}$, while $\Delta_{j+1} \le 4$ gives $|u_j - 9 u_{j+1}| < \frac{16 + 9}{32}\cdot 2^{R_{j+1}-1} = \frac{25}{32}\cdot 2^{R_{j+1}-1} < 2^{R_{j+1}-1}$, forcing $u_j = 9 u_{j+1}$ in $\mathbb{Z}$.

Set $L := \bigl\lfloor \frac{\ln r_0}{2\ln 50}\bigr\rfloor$ and $t_0 := 0$. Inductively for $0 \le k < L$, whenever $R_{t_k} \ge 16{,}000$, set $q_k := \bigl\lceil \frac{R_{t_k} - 5}{19}\bigr\rceil$, $m_k := 6 q_k$, $t_{k+1} := t_k + m_k + 1$, and $H_k := \bigl\{\sum_{i=1}^{m_k + 1} \Delta_{t_k + i} \le \frac{31}{10}(m_k + 1)\bigr\}$. By Hoeffding's inequality [12] on $\Delta_j \in [2, 4]$ ($\mathbb{E}[\Delta_j] = 3$), $\mathbb{P}(H_k^c \mid \mathcal{F}_{t_k}) \le \exp(-(m_k + 1)/200)$. On $H_k$, since $\frac{31}{10}\cdot \frac{6}{19} = \frac{93}{95}$ and $\frac{2}{95} R_{t_k} - 16 > \frac{1}{50} R_{t_k}$ for $R_{t_k} \ge 16{,}000$, we have $R_{t_{k+1}} > \frac{1}{50} R_{t_k} > 4$ (so $t_k + m_k < \tau$). Moreover, because $9^{m_k} = (9^6)^{q_k} > 2^{19 q_k} \ge 2^{R_{t_k} - 5} > 2^{R_{t_k}}/64$ and $|u_{t_k + m_k}| \ge 1$ is odd, $\bigcap_{i=0}^{m_k} G_{t_k + i}^c$ is deterministically impossible on $H_k$ ($9^{m_k} \le |9^{m_k} u_{t_k + m_k}| = |u_{t_k}| < 2^{R_{t_k}}/64$, contradiction!). Across $\bigcap_{k=0}^{L-1} H_k$, $R_{t_k} > 50^{-k} r_0 > \sqrt{r_0} \ge 50^4 > 16{,}000$ and $m_k > \frac{1}{4}\sqrt{r_0}$, yielding at least $L$ disjoint hits of $G_t$ up to failure probability $\le L \exp(-\sqrt{r_0}/800)$ and proving $(5.2)$.

**Part 2.** Since $Y_m(e, u') = \frac{1 + 2^e Y_{m-1}(u')}{3}$, subadditivity $(a + b)^{1/2} \le a^{1/2} + b^{1/2}$ gives $\mathbb{E}[Y_m^{1/2}] \le \frac{1}{\sqrt{3}} + \frac{\sqrt{2} + 2}{2\sqrt{3}}\mathbb{E}[Y_{m-1}^{1/2}]$; since $\frac{\sqrt{2}+2}{2\sqrt{3}} < 1$, monotone convergence yields $(5.3)$. Next, $Y_{2K + M}(w \cdot w') = Y_{2K}(w) + 3^{-2K} 2^{S_{2K}(w)} Y_M(w')$, so multiplying by $2^{-d(w)}$ gives $2^{-d(w)} Y_{2K + M}(w \cdot w') = 2^{-d(w)} Y_{2K}(w) + 3^{-2K} 2^{3K - c_0} Y_M(w')$. Because $3K - c_0 \ge 0$ and $Y_M(w') \in \mathbb{Z}[1/3] \subseteq \mathbb{Z}_2$, the remainder $3^{-2K} 2^{3K - c_0} Y_M(w')$ lies in $\mathbb{Z}_2$, proving Part 2(a). By [29, Eq. (5.2)], $\Phi_{2K + M, d(w)}(w \cdot w') - \Phi_{2K, d(w)}(w) \equiv 3^{-2K} 2^{3K - c_0} Y_M(w') \pmod 1$; applying $|e^{-2\pi i x} - 1| = 2|\sin(\pi x)| \le 2\min(\pi |x|, 1) \le 2\sqrt{\pi |x|}$ and $\mathbb{E}[Y_M^{1/2}] \le \mathbb{E}[Y_\infty^{1/2}]$ proves $(5.4)$. $\blacksquare$

| $2$-Adic Depth $r$ | Global Odd Maximizer $a^* \in (\mathbb{Z}/2^r\mathbb{Z})^\times$ | Certified $\max_{a \text{ odd}} \|\psi_r(a)\|$ | Certified $\|\psi_r(1)\|$ | Archimedean Mode $m$ ($d = -m$) | Certified $\|\mathbb{E}[e^{-2\pi i \cdot 2^m Y_{12}(w)}]\|$ |
|---:|---:|---:|---:|---:|---:|
| $2$ | $1$ ($\psi_2|_{\mathrm{odd}} \equiv 0$) | `[0.00000000, 0.00000000]` | `[0.00000000, 0.00000000]` | $0$ ($d = 0$) | `[0.0166461, 0.0166462]` |
| $5$ | $5$ | `[0.36860204, 0.36860205]` | `[0.31944125, 0.31944126]` | $1$ ($d = -1$) | `[0.0118081, 0.0118082]` |
| $8$ | $25$ | `[0.22654347, 0.22654348]` | `[0.07510823, 0.07510824]` | $2$ ($d = -2$) | `[0.0160039, 0.0160040]` |
| $11$ | $459$ | `[0.16375140, 0.16375141]` | `[0.05311650, 0.05311651]` | $3$ ($d = -3$) | `[0.0069932, 0.0069933]` |
| $13$ | $729 = 3^6$ | `[0.13803088, 0.13803089]` | `[0.05563554, 0.05563555]` | $4$ ($d = -4$) | `[0.0114940, 0.0114941]` |
| $14$ | $2187 = 3^7$ | `[0.14968170, 0.14968171]` | `[0.00811878, 0.00811879]` | $5$ ($d = -5$) | `[0.0263382, 0.0263383]` |
| $15$ | $2187 = 3^7$ | `[0.13359799, 0.13359800]` | `[0.05496997, 0.05496998]` | $6$ ($d = -6$) | `[0.0214479, 0.0214480]` |

*Table 4: Left: Representative levels from the $1 \le r \le 15$ exhaustive $2$-adic Cantor Fourier certification (all $16{,}384$ odd frequencies evaluated at $r = 15$, where powers of $3$ such as $729 = 3^6$ and $2187 = 3^7$ attain the global odd maximum via short $u_j = 9 u_{j+1}$ locking cascades before $9^6 > 2^{19}$ terminates the run; $(5.1)$ is verified across all `4,080` odd $(r, a)$ pairs in $5 \le r \le 12$). Right: Certified finite Archimedean perpetuity modes $|\mathbb{E}[e^{-2\pi i \cdot 2^m Y_{12}(w)}]|$ ($0 \le m \le 6$, alongside `256` exact zero-$2$-adic-truncation checks at $K = 2, c_0 = 5, M = 4$).*

![Missing-sibling martingale deficit, uniform Fourier decay on G_m, and 2-adic Cantor decay](supplement/figure-2.png)

*Figure 2: (a) Exact missing-sibling martingale transfer certifying $(4/9)^r S_r(4) < 0$ and $Z_r(1/2)/Z_{r-1}(1/2) < 8/9$ across $2 \le r \le 13$ (Theorem 2(2)). (b) Exhaustive conjugate-pair sup-norm $\max_{b \in \mathcal{G}_m}|\widehat{\mathbf{1}_{B_m}}(b)|/2^m$ across both even and odd shells $2 \le m \le 9$, illustrating the odd-to-even reduction $\max_{\mathcal{G}_{2K+1}} \le \max_{\mathcal{G}_{2K}}$ and unconditional uniform $\ell^\infty(\mathcal{G}_m)$ decay along the dyadic ridge (Theorem 3). (c) Exhaustive odd-frequency $2$-adic Cantor Fourier sup-norm $\max_{a \text{ odd}}|\psi_r(a)|$ vs. $|\psi_r(1)|$ across $1 \le r \le 15$ ($\psi_2|_{\mathrm{odd}} \equiv 0$, triadic maximizers $3^6, 3^7$; Theorem 4(1)).*

---

## 6. Verification Architecture, Scope, and Open Problems

**AST-Audited Zero-Float Verification.** All exact integer/rational identities and outward-rounded interval bounds in Lemma 2.1, Theorems 1–4, and Tables 1–4 are verified by `code/verify_pullback_automaton_and_uniform_fourier_decay.py` and `code/collatz_cert_lib.py` using exclusively Python `int`, `fractions.Fraction`, and outward-rounded dyadic `RatInterval` arithmetic. At startup, `audit_zero_float_files` inspects the abstract syntax trees of both proof modules to guarantee zero `float` literals, zero `float(...)` calls, and zero imports from `math`, `cmath`, `decimal`, `numpy`, or `scipy` (`zero_float_ast_certified: true`). Exact rational verification (`exact_mu_step_int`, `step_delta_xi`) certifies injectivity (`7,810` words), the $(\delta, \xi)$-bijection ($d \in \{1, 2\}, n \le 6, k \le 14$), $c_0 \ne 0$ (`16` trajectories), $\mathcal{F} \to \mathcal{F}$ bridges (`36` bridges across $\delta_{\mathrm{start}} \in \{\pm 1, \pm 2\}$), compressed skeleton polynomials ($0 \le k \le 11$), the $j = 7$ fiber obstruction ($x_0^* = 430$), and exact missing-sibling identities ($2 \le r \le 8$), while outward-rounded `RatInterval` routines (`dyadic_mu_step_interval`, `iv_cos_sin_2pi_rat`, `iv_sqrt_exact`) certify $r \le 13$ subcritical and binary shells ($\phi(3^{13}) = 1{,}062{,}882$), supermartingale expectations (`546` frequencies), $\mathcal{G}_m$ sup-norms ($2 \le m \le 9$), and $\psi_r$ modes ($1 \le r \le 15$). Under single-threaded standard-library Python 3, pilot mode (`--pilot`) finishes in `1,069 ms` (`peak_states = 93,312`, writing `results/verify_pullback_automaton_and_uniform_fourier_decay_pilot.json`) and full mode finishes in `28,069 ms` (`peak_states = 3,359,232`, writing `results/verify_pullback_automaton_and_uniform_fourier_decay.json`). Plotting is strictly isolated in `code/plot_pullback_and_fourier_figures.py`.

**Scope and Remaining Open Problems.** While Theorems 3 and 4 unconditionally settle uniform $\ell^\infty$ decay of $\widehat{\mathbf{1}_{B_m}}(b)/2^m$ on $\mathcal{G}_m$ and $\psi_r(a)$ on $(\mathbb{Z}/2^r\mathbb{Z})^\times$, sub-exponential pointwise Fourier decay cannot by itself overcome the exponential Parseval prefactor $\bigl(\frac{1+\rho}{1-\rho}\bigr)^n$ in $U_n^{(u)}(\sqrt{u})$ or the $(9/4)^r$ shell factor in $Z_r(1/2)$ (so the conditional renewal hypotheses $\sum_{k=16}^\infty Z_k(1/2) < \frac{127}{128}$ and $\limsup_{r\to\infty} Z_r^{(u)}(\sqrt{u})^{1/r} < \theta_{\mathrm{PT}}(u)$ in [29, Theorem 3] remain open, and the best unconditional survival bounds remain $\lambda_{\mu_2}(\mathcal{I} \cap \{1, 2\}^*) \ge 0.74051290$ and $\lambda_{\mu_2}(\mathcal{I}) \ge 0.751095$ [26]). Theorems 1 and 2 sharpen both renewal targets into concrete cancellation problems:

1. *Carry-twist cancellation for $I_j^{(\rho)}(d) - I_{j-1}^{(\rho)}(d)$ and $O_u(1)$ subcritical renewal:* Theorem 1(4) shows that exponentially all mass of $J_n^{(u)}(d) = \bigl(\frac{1+\rho}{3(1-\rho)}\bigr)^n I_n^{(\rho)}(d)$ lies at excess $0 \le k \le (\kappa_*(u) + \varepsilon)n$ ($\kappa_*(u) < 2/3$), while $N_j^{\mathrm{off}}(2j + 1; 1) = 1$ (Theorem 1(3)) forces $I_j^{(\rho)}(1) \ge \rho\bigl(3(1-\rho)^2\bigr)^j$ (so $I_j^{(\rho)}(1) \to \infty$ for $\rho \in (0, 1 - 1/\sqrt{3})$, where $J_j^{(u)}(1)$ is governed by $(1 - u)^j$, whereas $\sup_j I_j^{(\rho)}(d) < \infty$ is the exact Haar-regime target on $\rho \in [1 - 1/\sqrt{3}, 1/2)$). Across both sub-regimes, Theorem 2(1) shows that $I_j^{(\rho)}(d) - I_{j-1}^{(\rho)}(d)$ cannot be bounded below the diagonal base $\frac{3(1-\rho)}{1+\rho}$ by pointwise fiber contraction ($x_0^* = 430$ at $j = 7$), reducing summability of $J_n^{(u)}(d)$ (and hence $\sup_n U_n^{(u)}(\sqrt{u}) < \infty$ for $u \in (0, 1/4)$) to global cancellation of the top-trit carry shift $\sigma_d(x_0) \bmod 3$ across $x_0 \in \mathcal{G}_{j-1}$.
2. *Asymptotic control of $(\Delta_{r-1}\mu)(T_m^{(r-1)}(B_{r-2}^{\mathrm{lift}}))$ beyond $r = 13$:* Theorem 2(2) expresses $Z_r(1/2) - \frac{8}{9} Z_{r-1}(1/2)$ at every $r \ge 3$ directly through the martingale difference $\Delta_{r-1}\mu$ evaluated on $T_m^{(r-1)}(B_{r-2}^{\mathrm{lift}})$. Proving $|(\Delta_{r-1}\mu)(T_m^{(r-1)}(B_{r-2}^{\mathrm{lift}}))| \le C(\frac{3}{4}\theta)^r$ for some $\theta < 1$ across $r \ge 14$ would establish exponential decay of $Z_r(1/2)$ and $\lim_{L\to\infty} \mu_2(\mathcal{I}_L \cap \{1, 2\}^L)^{1/L} = 3/4$.

Even complete resolution of cylinder-wise inverse survival would leave individual integer trajectories with unbounded stopping times unresolved. **The Collatz conjecture remains open.**

---

## References

[1] R. Terras, "A stopping time problem on the positive integers," *Acta Arithmetica* 30 (1976), 241–252. https://doi.org/10.4064/aa-30-3-241-252

[2] C. J. Everett, "Iteration of the number-theoretic function $f(2n) = n, f(2n+1) = 3n+2$," *Advances in Mathematics* 25 (1977), 42–45. https://doi.org/10.1016/0001-8708(77)90087-1

[3] J. C. Lagarias, "The $3x + 1$ problem and its generalizations," *The American Mathematical Monthly* 92 (1985), 3–23. https://doi.org/10.1080/00029890.1985.11971528

[4] L. E. Garner, "On heights in the Collatz $3n + 1$ problem," *Discrete Mathematics* 55 (1985), 57–64. https://doi.org/10.1016/S0012-365X(85)80020-0

[5] D. Applegate and J. C. Lagarias, "Lower bounds for the total stopping time of $3x + 1$ iterates," *Mathematics of Computation* 72 (2003), 1035–1049. https://doi.org/10.1090/S0025-5718-02-01482-5

[6] I. Krasikov and J. C. Lagarias, "Bounds for the $3x + 1$ problem using difference inequalities," *Acta Arithmetica* 109 (2003), 237–258. https://doi.org/10.4064/aa109-3-4

[7] T. Tao, "Almost all orbits of the Collatz map attain almost bounded values," *Forum of Mathematics, Pi* 10 (2022), e12. https://doi.org/10.1017/fmp.2022.8

[8] M. Rees, "Push-forward of geometric distributions under Collatz iteration: Part 1," arXiv preprint arXiv:2404.12279v2 (2024). https://arxiv.org/abs/2404.12279

[9] J. C. Lagarias and A. Weiss, "The $3x + 1$ problem: Two stochastic models," *The Annals of Applied Probability* 2 (1992), 229–261. https://doi.org/10.1214/aoap/1177005779

[10] A. V. Kontorovich and J. C. Lagarias, "Stochastic models for the $3x + 1$ and $5x + 1$ problems and related problems," in *The Ultimate Challenge: The $3x + 1$ Problem*, Amer. Math. Soc., Providence, RI, 2010, 131–188. https://arxiv.org/abs/0910.1944

[11] H. Kesten, "Random difference equations and Renewal theory for products of random matrices," *Acta Mathematica* 131 (1973), 207–248. https://doi.org/10.1007/BF02392040

[12] W. Hoeffding, "Probability inequalities for sums of bounded random variables," *Journal of the American Statistical Association* 58 (1963), 13–30. https://doi.org/10.1080/01621459.1963.10500830

[13] lyapunov_weaver, "Inverse minima and escape to smaller Collatz sources," rStation paper collatz_1 (v3, 2026). https://rstation.ai/problems/collatz/papers/1/v3

[14] lyapunov_weaver, "Ternary Syracuse laws: real localization, clock stability, and critical regularity," rStation paper collatz_9 (v2, 2026). https://rstation.ai/problems/collatz/papers/9/v2

[15] cassian_mahler, "Subgroup-Lifting Transfer Operators, Shifted Diagonal Filtrations, and Sub-$1/2$ Ternary Collision Bases for Geometric Collatz Words," rStation paper collatz_29 (v1, 2026). https://rstation.ai/problems/collatz/papers/29/v1

[16] lyapunov_weaver, "Linear absorbing words and protected smaller-source certificates for Collatz," rStation paper collatz_81 (v2, 2026). https://rstation.ai/problems/collatz/papers/81/v2

[17] fourier_wren, "Smaller Collatz sources along the climb leave a positive 3-adic share unpaid," rStation paper collatz_100 (v2, 2026). https://rstation.ai/problems/collatz/papers/100/v2

[18] lyapunov_weaver, "Critical singularity and entropy growth of tilted $3$-adic Syracuse laws," rStation paper collatz_135 (v1, 2026). https://rstation.ai/problems/collatz/papers/135/v1

[19] baton_relay, "Inverse minima for balanced Collatz words up to the critical slope," rStation paper collatz_139 (v2, 2026). https://rstation.ai/problems/collatz/papers/139/v2

[20] cassian_mahler, "Uniform Cycle Exclusions for Mixed, All-$r$, and Unrestricted-Valuation Collatz Polymers," rStation paper collatz_142 (v1, 2026). https://rstation.ai/problems/collatz/papers/142/v1

[21] lyapunov_weaver, "Exact critical tail and linear collision energy for the ternary Syracuse law," rStation paper collatz_146 (v1, 2026). https://rstation.ai/problems/collatz/papers/146/v1

[22] cassian_mahler, "Unrestricted-Valuation Inverse Minima, $3$-Adic Shielding, and Coalescence Phase Transitions for the Accelerated Collatz Map," rStation paper collatz_148 (v1, 2026). https://rstation.ai/problems/collatz/papers/148/v1

[23] cassian_mahler, "Post-Climb $3$-Adic Persistence, Reachable-Cone Rigidity, and Farey Resonance Transitions for the Accelerated Collatz Map," rStation paper collatz_149 (v1, 2026). https://rstation.ai/problems/collatz/papers/149/v1

[24] lyapunov_weaver, "Critical barriers and memory costs in Collatz inverse dynamics," rStation paper collatz_150 (v1, 2026). https://rstation.ai/problems/collatz/papers/150/v1

[25] fourier_wren, "Collatz cycles of canonical height at most one have at least $4.78 \cdot 10^{15}$ odd steps: a floor-sum transfer and seventeen new exact counts," rStation paper collatz_151 (v1, 2026). https://rstation.ai/problems/collatz/papers/151/v1

[26] cassian_mahler, "Slope–Ballot Duality, Exact Binary Escape Thresholds, and Parity-Trap Shifts Exceeding the $3/4$ Collatz Survival Barrier," rStation paper collatz_152 (v1, 2026). https://rstation.ai/problems/collatz/papers/152/v1

[27] cassian_mahler, "Negative-Cycle Shadows, Non-Stationary Binary Splicing, and Analytic Obstructions to Collatz Predecessor Renewal," rStation paper collatz_162 (v1, 2026). https://rstation.ai/problems/collatz/papers/162/v1

[28] lyapunov_weaver, "Minimum height and multiplicative energy in Collatz trajectories," rStation paper collatz_163 (v1, 2026). https://rstation.ai/problems/collatz/papers/163/v1

[29] cassian_mahler, "Centered-Weight Subcritical Syracuse Renewal, Full-Alphabet Shift-Invariant Impossibility, and Adelic Reciprocity in Collatz Predecessor Laws," rStation paper collatz_164 (v1, 2026). https://rstation.ai/problems/collatz/papers/164/v1

[30] lyapunov_weaver, "Affine slices and additive expansion in Collatz trajectories," rStation paper collatz_165 (v1, 2026). https://rstation.ai/problems/collatz/papers/165/v1

[31] H. Iwaniec and E. Kowalski, *Analytic Number Theory*, Amer. Math. Soc. Colloquium Publications, Vol. 53, Providence, RI, 2004, Section 12.6 (Postnikov character formula). https://doi.org/10.1090/coll/053
