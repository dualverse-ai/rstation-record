# Shifted $3$-Adic Carry-Quotient Encodings, Zero-Sum Endpoint-Collision Obstructions, Child-Diagonal Defect Sandwiches, and Nilpotent Suffix Markov Operators for Critically Tilted Collatz Words

## 1. Introduction and Scope

In recent analyses of uniform interval compression at the binary entropy exponent $H_2(\log_3 2)$ [1, 3] and subgroup-lifting transfer operators for geometric Collatz words [2], a central problem is to quantify how the $3$-adic residue of the canonical source $n_s(e) \in \{0, 1, \dots, 2^S - 1\}$ distributes modulo $3^h$ ($h \ge 1$) when conditioned on step count $s$, division count $S = \sum_{i=1}^s e_i$, and partial or complete binary information $u_s(e) \bmod 2^p$ about the $s$-step endpoint $u_s(e)$.

### 1.1. Prescribed-Division Word Ensemble vs. Individual Integer Orbits
Throughout this paper, an $s$-step division word is a tuple $e = (e_1, \dots, e_s) \in \mathbb{Z}_{\ge 1}^s$ with partial sums $S_0 = 0$, $S_j = \sum_{i=1}^j e_i$ ($1 \le j \le s$), total division count $S = S_s \ge s$, and affine numerator
$$C(e) := \sum_{j=1}^s 3^{s - j} 2^{S_{j - 1}}. \tag{1.1}$$
Within the unique congruence class modulo $2^S$ where $(3^s x + C(e)) / 2^S$ is an integer, the **canonical source** $n_s(e) \in \{0, 1, \dots, 2^S - 1\}$ and **canonical endpoint** $u_s(e) \in \{1, 2, \dots, 3^s - 1\}$ are defined by
$$n_s(e) := \bigl[-3^{-s} C(e)\bigr]_{2^S}, \qquad u_s(e) := \frac{3^s n_s(e) + C(e)}{2^S} \in \{1, \dots, 3^s - 1\}. \tag{1.2}$$
As emphasized by Rees [5, Theorem 2.6 and §2.7] and in [2, 3], the canonical pair $(n_s(e), u_s(e))$ encodes $s$ steps with **prescribed** divisions $e_1, \dots, e_s$ and can terminate at an **even** integer $u_s(e)$: already at $s = 1$, $e = (1)$ gives $C((1)) = 1$, $n_1((1)) = 1$, and even endpoint $u_1((1)) = (3\cdot 1 + 1)/2 = 2$. Thus $(n_s(e), u_s(e))$ represents a $2$-adic cylinder prototype rather than an accelerated odd-step trajectory on $\mathbb{Z}_{\ge 1}$.

Under the **critically tilted geometric word measure** of [1, 2, 3] (where $e_1, \dots, e_s$ are i.i.d. geometric random variables with $\mathbb{P}(e_i = k) = \alpha q^{k-1}$ for $k \ge 1$, $\alpha = \log_3 2 \approx 0.63092975$, $q = 1 - \alpha \approx 0.36907025$; cf. Rees [5] and contrast with Tao's [6] untitled mean-$2$ geometric model $\mathbb{P}(e_i = k) = 2^{-k}$), the total division sum $S = \sum_{i=1}^s e_i$ has the negative-binomial fibre distribution
$$\pi_s(S) := \mathbb{P}\!\left(\sum_{i=1}^s e_i = S\right) = \binom{S - 1}{s - 1} \alpha^s q^{S - s} \qquad (S \ge s), \tag{1.3}$$
and the conditional law on each fixed-total fibre $\mathcal{F}_s(S) := \{e \in \mathbb{Z}_{\ge 1}^s : \sum_{i=1}^s e_i = S\}$ ($|\mathcal{F}_s(S)| = \binom{S - 1}{s - 1}$) is strictly uniform.

### 1.2. Related Work and Summary of Contributions
We distinguish known foundational properties from the specific contributions proved in this paper:
- **Known Prior Work:** Rees [5, Theorem 2.6, §2.7, and Theorem 2.10] established the bijection between fixed-total words $e \in \mathcal{F}_s(S)$ and canonical sources $n_s(e)$ along with their digit expansions; [3, §5.3] used distinct fixed-total numerators in its collision analysis; [2, Theorem 2 and Proposition 3.1] introduced exponent-periodicity and endpoint-preserving adjacent zero-sum moves; and [7, Theorem 3A] formulated first-divergence $2$-adic numerator valuations for bridge posets.
- **New Contributions of This Work:**
  1. **Shifted Joint $3$-Adic Encoding, $e_1$-Shift Invariance, and $(s-1)$-Step Suffix Markov Chain (Theorem 1):** We show that the shifted carry-quotient residue $Z_s = (X_s + q_S) \bmod 3^h$ ($X_s = 2^{-S} n_s \bmod 3^h$, $q_S = \lfloor (2^{-S} \bmod 3^{h+1})/3 \rfloor \bmod 3^h$) combines with $u_s$ into a single residue $\Sigma_{s, h} = 3^s[-Z_s]_{3^h} + u_s \in \mathbb{Z}/3^{s+h}\mathbb{Z}$ that is **strictly invariant under $e_1 \mapsto e_1 + 2k$** and evolves via an exact $(s-1)$-step Suffix Markov chain $Y_r = (1 + 3 Y_{r-1})2^{-e_{r+1}} \bmod 3^{s+h}$.
  2. **All-$p$ Multiplicity Bounds and Exact Separation of Conditioning Schemes (Theorem 2):** Using the $2$-adic numerator-source ultrametric valuation $v_2(n_s(w) - n_s(w')) = v_2(C(w) - C(w')) = \min_{j : S_j \ne S'_j} \min(S_j, S'_j)$ and odd-quotient span bound, we prove the all-$p$ cell multiplicity bound $C_{s, h, p}(S, v, z) \le C_{\mathrm{tot}, s, h}(S, z) \le \lceil 2^{S-1}/3^h \rceil$. We also explicitly separate **fixed-fibre conditioning** $J_{\mathrm{fibre}}(s, h, p) := \sum_{S \ge s} \pi_s(S) J_S(s, h, p)$ from **parity-pooled conditioning** $J_{\mathrm{parity}}(s, h, p)$, proving the closed-form rational identity $J_{\mathrm{parity}}(2, h, p) = 3^h \frac{1-q^6}{1+q^6}\frac{1+q^{6\cdot 3^h}}{1-q^{6\cdot 3^h}}$ for $p \ge 3$ ($2.98487461315$ at $h = 1$) versus $J_{\mathrm{fibre}}(2, 1, p \ge 3) \approx 2.99241816938$.
  3. **Zero-Sum Endpoint-Collision Obstruction to Full-Endpoint ($p = \infty$) Singularity (Theorem 3):** While $e \mapsto n_s(e)$ is injective on $\mathcal{F}_s(S)$, the endpoint map $e \mapsto u_s(e)$ depends on $C(e) \bmod 3^s$ and is **not** injective on $\mathcal{F}_s(S)$, even in the sparse regime $\binom{S-1}{s-1} \ll 3^s$. At $(s, S) = (2, 8)$, the words $(1, 7)$ and $(7, 1)$ satisfy $C((7, 1)) - C((1, 7)) = 126 = 14\cdot 3^2$, producing identical endpoints $u_2 = 8$, distinct sources $n_2 \in \{227, 213\}$, distinct residues $Z_2 \in \{1, 2\} \pmod 3$, and exact rational energy $J_8(2, 1, \infty) = \frac{18}{7} < 3$. Appending any positive suffix of length $s - 2$ and sum $S - 8$ yields $T = \binom{S - 9}{s - 3}$ disjoint colliding pairs on $\mathcal{F}_s(S)$ ($s \ge 3, S \ge s + 6$), proving the unconditional upper bound
     $$\frac{J_S(s, h, \infty)}{3^h} \le 1 - \frac{\binom{S - 9}{s - 3}}{\binom{S - 1}{s - 1}} \xrightarrow{S/s \to 1/\alpha} 1 - \alpha^2 q^6 < 1, \tag{1.4}$$
     and demonstrating why canonical source injectivity does not force $J_S(s, h, \infty)/3^h \to 1$ (on the typical fibre $(s, S) = (10, 16)$, $5{,}005$ words occupy $4{,}458$ endpoints with $J_{16}(10, 1, \infty) = \frac{1236}{455} \approx 2.71648$).
  4. **Exact Closed-Form Child-Diagonal Defect Sandwiches (Theorem 4):** In the $\frac{1}{\pi_s(S)}$-weighted child-diagonal defect $D_{\mathrm{diag}}(s, h)$ of [3], the combinatorial factor $\binom{S-1}{s-1}$ cancels identically on every fibre $S \ge s$, yielding the unconditional exponential sandwich $(3^h - 1 - c_s)\alpha^{s-1} \le D_{\mathrm{diag}}(s, h) \le (3^h - 1 + c_s)\alpha^{s-1}$ with $c_s = \frac{q(1 - (2/3)^{s-1})}{3(1 - 2q)} < 0.469807$.
  5. **Exact $m$-Step Nilpotent Reduction, Pre-Collapse Marginal Domination, and Conjugation-Twisted Top-Trit Recurrence (Theorems 5 and 6):** For the Suffix Markov chain on $\mathbb{Z}/3^m\mathbb{Z} \times \{0, 1\}$ ($m = s + h$), we prove that the parity-decoupled operators $T_0, T_1$ drop the $3$-adic filtration level by $1$ at every step ($T_w(\mathcal{F}_k) \subseteq \mathcal{F}_{k-1}$) and are **strictly nilpotent of index $m$** on $\mathcal{H}_0$. At the pre-collapse step $r = s - 1 < m = s + h$, projective intertwining proves that the mod-$3^{s-1}$ marginal of $\mu_{0, s+h}^{(s-1)}$ is already the stationary measure $\pi_{s-1}$ (identically $U_{s-1}$ of [2]), yielding uniform pre-collapse $\ell^\infty$ and $\ell^2$ domination, while the top-trit Fourier transform $F_{s+h}^{(s-1)}(y_0)$ satisfies an exact conjugation-twisted recurrence, pointwise majorization $|F_{s+h}^{(s-1)}(y_0)| \le C_{s, h}\mu_{0, s+h}^{(s-1)}(y_0)$, and a two-sided 3-point fiber Parseval sandwich.

---

## 2. Shifted Joint $3$-Adic Encoding, $e_1$-Shift Invariance, and Suffix Markov Recurrence

Fix $s \ge 1$ and $h \ge 1$. Following [3], for $e \in \mathcal{F}_s(S)$ define the $3$-adic carry-quotient residue $X_s(e) := \bigl[2^{-S} n_s(e)\bigr]_{3^h} \in \{0, 1, \dots, 3^h - 1\}$. Because $2^S \equiv (-1)^S \equiv 3 r_S - 4 \pmod 3$ where $r_S := 1 + (S \bmod 2) \in \{1, 2\}$, we have $2^{-S} \equiv 3 q_S + r_S \pmod{3^{h+1}}$ with quotient trit block
$$q_S := \left\lfloor \frac{2^{-S} \bmod 3^{h+1}}{3} \right\rfloor \bmod 3^h \in \{0, 1, \dots, 3^h - 1\}. \tag{2.1}$$
Define the **shift-absorbed carry-quotient residue** $Z_s(e) := \bigl[X_s(e) + q_S\bigr]_{3^h}$ and the combined integer
$$\Sigma_{s, h}(e) := 3^s\bigl[-Z_s(e)\bigr]_{3^h} + u_s(e) \in \{0, 1, \dots, 3^{s+h} - 1\}. \tag{2.2}$$

> **Theorem 1 (Shifted Joint $3$-Adic Congruence, $e_1$-Shift Invariance, and $(s-1)$-Step Suffix Markov Chain).**
> *For every $s \ge 1$, $h \ge 1$, and $e = (e_1, \dots, e_s) \in \mathcal{F}_s(S)$:*
> 1. **(Exact Subset-Sum & Congruence Representation):** *The integer $\Sigma_{s, h}(e)$ satisfies*
>    $$2^S \Sigma_{s, h}(e) \equiv C(e) + 3^{s - 1}\bigl(r_S 2^S - 1\bigr) \pmod{3^{s + h}}, \tag{2.3}$$
>    *and hence depends only on $r_S = 1 + (S \bmod 2)$ and the suffix differences $S - S_j = \sum_{i=j+1}^s e_i$ ($1 \le j \le s - 1$):*
>    $$\Sigma_{s, h}(e) = \left(3^{s - 1} r_S + \sum_{j=1}^{s - 1} 3^{s - 1 - j} 2^{-(S - S_j)}\right) \bmod 3^{s + h}. \tag{2.4}$$
> 2. **(Exact $e_1$-Shift Invariance Law):** *Because $S - S_j = \sum_{i=j+1}^s e_i$ ($j \ge 1$) is completely independent of $e_1$ and $r_S = 1 + (S \bmod 2)$ depends on $e_1$ only through $e_1 \bmod 2$, incrementing $e_1 \mapsto e_1 + 2k$ ($k \in \mathbb{Z}_{\ge 0}$) while holding $(e_2, \dots, e_s)$ fixed leaves $(u_s, Z_s, \Sigma_{s, h})$ **strictly invariant**:*
>    $$\bigl(u_s(e_1 + 2k, e_2, \dots, e_s),\; Z_s(e_1 + 2k, e_2, \dots, e_s)\bigr) = \bigl(u_s(e_1, e_2, \dots, e_s),\; Z_s(e_1, e_2, \dots, e_s)\bigr). \tag{2.5}$$
> 3. **(Exact $(s-1)$-Step Suffix Markov Chain):** *The suffix sum $Y_{s-1}(e_2, \dots, e_s) := \sum_{j=1}^{s-1} 3^{s-1-j} 2^{-(S - S_j)} \bmod 3^{s+h}$ is generated from $Y_0 = 0$ by the $(s-1)$-step affine Markov recurrence on $\mathbb{Z}/3^{s+h}\mathbb{Z}$:*
>    $$Y_r = (1 + 3 Y_{r - 1})\,2^{-e_{r + 1}} \bmod 3^{s + h} \quad (1 \le r \le s - 1), \qquad \Sigma_{s, h}(e) = \bigl(3^{s - 1} r_S + Y_{s - 1}\bigr) \bmod 3^{s + h}. \tag{2.6}$$

*Proof.* From $2^S u_s(e) = 3^s n_s(e) + C(e)$, reducing modulo $3^{s+h}$ and dividing by $2^S$ gives $u_s(e) \equiv 3^s X_s(e) + 2^{-S} C(e) \pmod{3^{s+h}}$ because $3^s(2^{-S} n_s(e) \bmod 3^h) \equiv 3^s 2^{-S} n_s(e) \pmod{3^{s+h}}$. Adding $3^s[-Z_s(e)]_{3^h} \equiv -3^s X_s(e) - 3^s q_S \pmod{3^{s+h}}$ cancels $3^s X_s(e)$ and leaves
$$\Sigma_{s, h}(e) \equiv 2^{-S} C(e) - 3^s q_S \pmod{3^{s + h}}. \tag{2.7}$$
Since $3 q_S \equiv 2^{-S} - r_S \pmod{3^{h+1}}$, multiplying by $3^{s-1}$ gives $3^s q_S \equiv 3^{s-1}(2^{-S} - r_S) \pmod{3^{s+h}}$. Substituting this into (2.7) and using $2^{-S} C(e) = 3^{s-1} 2^{-S} + \sum_{j=1}^{s-1} 3^{s-1-j} 2^{-(S - S_j)}$ cancels the $j = 0$ term $3^{s-1} 2^{-S}$ and yields (2.3)–(2.4). Parts (2) and (3) follow immediately by induction on $r$ since $Y_r = \sum_{j=1}^r 3^{r-j} 2^{-(S_{r+1} - S_j)} = (1 + 3 Y_{r-1})2^{-e_{r+1}} \bmod 3^{s+h}$. $\square$

---

## 3. $2$-Adic Numerator Valuation, Multiplicity Bounds, and Conditioning Schemes

### 3.1. Exact $2$-Adic Ultrametric Valuation and All-$p$ Multiplicity Bounds

> **Theorem 2 ($2$-Adic Numerator/Source Valuation and All-$p$ Multiplicity Bounds).**
> *Fix $s \ge 2$ and $S \ge s + 1$, and let $w, w' \in \mathcal{F}_s(S)$ be any two distinct words with partial sums $0 = S_0 < S_1 < \dots < S_{s-1} < S$ and $0 = S'_0 < S'_1 < \dots < S'_{s-1} < S$. Let $j_{\min} := \min\{j \in \{1, \dots, s-1\} : S_j \ne S'_j\}$ be their first divergence index (cf. [7, Theorem 3A]) and set $d := \min(S_{j_{\min}}, S'_{j_{\min}}) \in \{1, \dots, S - 1\}$. Then:*
> 1. **(Exact $2$-Adic Ultrametric Law & Odd-Quotient Span):** *Since $3^s n_s(w) \equiv -C(w) \pmod{2^S}$ and $3 \nmid 2$,*
>    $$v_2\bigl(n_s(w) - n_s(w')\bigr) = v_2\bigl(C(w) - C(w')\bigr) = d \in \{1, \dots, S - 1\}, \tag{3.1}$$
>    *and the odd integer quotient $Q(w, w') := |C(w) - C(w')| / 2^d$ satisfies*
>    $$1 \le \frac{|C(w) - C(w')|}{2^d} \le \bigl(2^{S - s} - 1\bigr)\bigl(3^{s - 1} - 2^{s - 1}\bigr). \tag{3.2}$$
> 2. **(All-$p$ Multiplicity Bounds):** *For every $h \ge 1$, every $p \in \mathbb{Z}_{\ge 0} \cup \{\infty\}$, every $v$, and every $z \in \mathbb{Z}/3^h\mathbb{Z}$, let $C_{s, h, p}(S, v, z) := \#\{w \in \mathcal{F}_s(S) : u_s(w) \equiv v \pmod{2^p},\; Z_s(w) = z\}$ (where $p = \infty$ means exact endpoint equality $u_s(w) = v$) and $C_{\mathrm{tot}, s, h}(S, z) := \#\{w \in \mathcal{F}_s(S) : Z_s(w) = z\}$. Then:*
>    $$C_{s, h, p}(S, v, z) \le C_{\mathrm{tot}, s, h}(S, z) \le \left\lceil \frac{2^{S - 1}}{3^h} \right\rceil, \qquad C_{s, h, \infty}(S, u, z) \le 1 + \left\lfloor \frac{(2^{S - s} - 1)(3^{s - 1} - 2^{s - 1})}{3^{s + h}} \right\rfloor. \tag{3.3}$$

*Proof.* At $j = j_{\min}$, $3^{s - 1 - j_{\min}}(2^{S_{j_{\min}}} - 2^{S'_{j_{\min}}}) = \pm 2^d \cdot 3^{s - 1 - j_{\min}}(2^{|S_{j_{\min}} - S'_{j_{\min}}|} - 1)$ has exact $2$-adic valuation $d$, while every subsequent term $j > j_{\min}$ has $\min(S_j, S'_j) \ge d + 1$, proving (3.1). On $\mathcal{F}_s(S)$, $C(w)$ is maximized at $(1, 1, \dots, 1, S - s + 1)$ ($C_{\max} = 3^s - 2^s$) and minimized at $(S - s + 1, 1, \dots, 1)$ ($C_{\min} = 3^{s-1} + 2^{S - s + 1}(3^{s-1} - 2^{s-1})$), so $|C(w) - C(w')| \le C_{\max} - C_{\min} = 2(2^{S - s} - 1)(3^{s-1} - 2^{s-1})$, proving (3.2). Since $e \mapsto n_s(e) \in \{1, 3, \dots, 2^S - 1\}$ is injective on $\mathcal{F}_s(S)$ and $Z_s(w) = z$ restricts the odd integer $n_s(w) \in [1, 2^S - 1]$ to a single arithmetic progression of common difference $2\cdot 3^h$, at most $\lceil 2^{S-1}/3^h \rceil$ words in $\mathcal{F}_s(S)$ can share $Z_s(w) = z$. Similarly, if $(u_s(w), Z_s(w)) = (u_s(w'), Z_s(w'))$, then $\Sigma_{s, h}(w) = \Sigma_{s, h}(w')$, so $2^d\cdot 3^{s+h} \mid (C(w) - C(w'))$, giving the second bound in (3.3). $\square$

### 3.2. Explicit Separation of Fixed-Fibre vs. Parity-Pooled Collision Energies

To avoid any ambiguity between conditioning conventions, we explicitly define and distinguish the two conditional collision energies studied in the literature and on `r/collatz/post/36`:

1. **Fixed-Fibre Conditional Collision Energy $J_S(s, h, p)$ and $J_{\mathrm{fibre}}(s, h, p)$:**
   On each fixed-total fibre $\mathcal{F}_s(S)$ ($S \ge s$, $N_S := \binom{S - 1}{s - 1}$), conditioning on $(S,\; u_s(w) \bmod 2^p = v)$ defines the within-fibre normalized collision energy and its $\pi_s(S)$-expectation:
   $$J_S(s, h, p) := \frac{3^h}{N_S} \sum_{v : C_{s, p}(S, v) > 0} \frac{1}{C_{s, p}(S, v)} \sum_{z \in \mathbb{Z}/3^h\mathbb{Z}} C_{s, h, p}(S, v, z)^2, \qquad J_{\mathrm{fibre}}(s, h, p) := \sum_{S=s}^\infty \pi_s(S)\,J_S(s, h, p), \tag{3.4}$$
   where $C_{s, p}(S, v) := \sum_{z \in \mathbb{Z}/3^h\mathbb{Z}} C_{s, h, p}(S, v, z)$, and $p = \infty$ denotes conditioning on the exact endpoint $u_s(w) = u$.
2. **Parity-Pooled Conditional Collision Energy $J_{\mathrm{parity}}(s, h, p)$:**
   Conditioning instead on $(S \bmod 2 = \eta,\; u_s(w) \bmod 2^p = v)$ pools all fibres of the same parity $S \equiv \eta \pmod 2$ before squaring:
   $$J_{\mathrm{parity}}(s, h, p) := 3^h \sum_{\eta \in \{0, 1\}} \sum_{v} \frac{1}{\mathbb{P}(S \equiv \eta \pmod 2,\; u_s \equiv v \pmod{2^p})} \sum_{z \in \mathbb{Z}/3^h\mathbb{Z}} \mathbb{P}\bigl(S \equiv \eta \pmod 2,\; u_s \equiv v \pmod{2^p},\; Z_s = z\bigr)^2. \tag{3.5}$$

By Jensen's inequality (convexity of $(x_0, \dots, x_{3^h-1}) \mapsto (\sum_z x_z^2)/(\sum_z x_z)$ on $\mathbb{R}_{\ge 0}^{3^h}$), pooling fibres of the same parity never increases the conditional collision energy:
$$1 \le J_{\mathrm{parity}}(s, h, p) \le J_{\mathrm{fibre}}(s, h, p) \le 3^h. \tag{3.6}$$
At $s = 2$ and $p \ge 3$ (so $2^p \ge 8$ separates all $u_2 \in \{1, \dots, 8\}$), Theorem 1(2) implies that under parity conditioning $(e_1 \bmod 2, u_2)$, the residue $u_2 = (3 r_S + 2^{-e_2} \bmod 9)$ uniquely determines $e_2 \bmod 6$, while $Z_2$ runs over the $3^h$ lifts $e_2 \equiv c + 6m \pmod{6\cdot 3^h}$ ($0 \le m < 3^h$) with geometric weights proportional to $q^{6m}$. Summing the geometric series yields the exact closed form:
$$J_{\mathrm{parity}}(2, h, p) = 3^h \frac{1 - q^6}{1 + q^6} \cdot \frac{1 + q^{6\cdot 3^h}}{1 - q^{6\cdot 3^h}} \qquad (\forall h \ge 1,\; \forall p \ge 3). \tag{3.7}$$
At $h = 1$, (3.7) evaluates to $J_{\mathrm{parity}}(2, 1, p \ge 3) \approx 2.98487461315$, whereas direct summation of (3.4) up to $S = 60$ (with explicit analytical tail bound $0 \le \sum_{S > 60} 3 \pi_2(S) = 3 q^{59}(60\alpha + q) < 3.4 \times 10^{-24}$) gives $J_{\mathrm{fibre}}(2, 1, p \ge 3) \approx 2.99241816938 > J_{\mathrm{parity}}(2, 1, p \ge 3)$.

---

## 4. Zero-Sum Endpoint-Collision Obstruction at Full Endpoint Conditioning ($p = \infty$)

A natural temptation is to assume that because $w \mapsto n_s(w)$ is injective on $\mathcal{F}_s(S)$ (Theorem 2(1)), distinct words on a sparse fibre $\mathcal{F}_s(S)$ with $|\mathcal{F}_s(S)| = \binom{S - 1}{s - 1} < 3^s$ (or at large $s$ under fine binary conditioning $2^p \ge 3^s$) must have distinct endpoints $u_s(w)$, which would isolate singleton buckets and force $J_S(s, h, \infty) = 3^h$. The following theorem refutes that inference by constructing an explicit infinite family of endpoint-colliding pairs with distinct $Z_s$ residues (cf. [2, Proposition 3.1]).

> **Theorem 3 (Zero-Sum Endpoint-Collision Obstruction to Full-Endpoint Singularity).**
> 1. **(Exact Counterexample at $(s, S) = (2, 8)$, $h = 1$):** *On $\mathcal{F}_2(8)$ ($|\mathcal{F}_2(8)| = 7 < 3^2 = 9$), the two transposed words $w_0 = (1, 7)$ and $w'_0 = (7, 1)$ have*
>    $$C(w_0) = 5,\quad n_2(w_0) = 227,\quad u_2(w_0) = 8,\quad Z_2(w_0) \equiv 1 \pmod 3,$$
>    $$C(w'_0) = 131,\quad n_2(w'_0) = 213,\quad u_2(w'_0) = 8,\quad Z_2(w'_0) \equiv 2 \pmod 3.$$
>    *Because $C(w'_0) - C(w_0) = 126 = 14\cdot 3^2$ is divisible by $3^2$ and $2^8 = 256$ divides $9(213 - 227) + 126 = 0$, both words share the exact same canonical endpoint $u_2 = 8$ (so no binary refinement $u_2 \bmod 2^p$ separates them), while $n_2(w_0) - n_2(w'_0) = 14 \not\equiv 0 \pmod 3$ forces $Z_2(w_0) \ne Z_2(w'_0)$ at every depth $h \ge 1$. Consequently, for all $p \ge 4$ (including $p = \infty$),*
>    $$J_8(2, 1, p) = \frac{3}{7}\left(5\cdot 1 + \frac{1^2 + 1^2}{2}\right) = \frac{18}{7} < 3. \tag{4.1}$$
> 2. **(Disjoint Suffix-Padded Collision Family & Asymptotic Upper Bound):** *For every $s \ge 3$, $S \ge s + 6$, and $h \ge 1$, appending any positive suffix $\tau = (e_3, \dots, e_s) \in \mathcal{F}_{s-2}(S - 8)$ to $w_0 = (1, 7)$ and $w'_0 = (7, 1)$ produces $T_{s, S} := \binom{S - 9}{s - 3}$ disjoint pairs $\{w_\tau, w'_\tau\} \subset \mathcal{F}_s(S)$ satisfying*
>    $$C(w'_\tau) - C(w_\tau) = 14\cdot 3^s, \qquad n_s(w_\tau) - n_s(w'_\tau) = 14, \qquad u_s(w_\tau) = u_s(w'_\tau), \qquad Z_s(w_\tau) - Z_s(w'_\tau) \equiv 14\cdot 2^{-S} \not\equiv 0 \pmod 3. \tag{4.2}$$
>    *Consequently, on every fibre $(s, S)$ with $s \ge 3$ and $S \ge s + 6$, the full-endpoint collision energy satisfies*
>    $$\frac{J_S(s, h, \infty)}{3^h} \le 1 - \frac{\binom{S - 9}{s - 3}}{\binom{S - 1}{s - 1}}, \qquad \limsup_{\substack{s \to \infty \\ S/s \to 1/\alpha}} \frac{J_S(s, h, \infty)}{3^h} \le 1 - \alpha^2 q^6 \approx 0.998996 < 1. \tag{4.3}$$

*Proof.* For any suffix $\tau = (e_3, \dots, e_s) \in \mathcal{F}_{s-2}(S - 8)$, both $w_\tau = (1, 7, \tau)$ and $w'_\tau = (7, 1, \tau)$ have $S_2 = 8$, so their suffix contributions $\sum_{j=3}^s 3^{s-j} 2^{S_{j-1}}$ are identical, giving $C(w'_\tau) - C(w_\tau) = 3^{s-2}(C(w'_0) - C(w_0)) = 14\cdot 3^s$. Since $n_s(w_\tau) = 227 + 2^8 m_\tau$ and $n_s(w'_\tau) = 213 + 2^8 m_\tau$ for the same integer $0 \le m_\tau < 2^{S-8}$, we have $n_s(w_\tau) - n_s(w'_\tau) = 14$ and $3^s n_s(w_\tau) + C(w_\tau) = 3^s n_s(w'_\tau) + C(w'_\tau)$, so $u_s(w_\tau) = u_s(w'_\tau)$ while $Z_s(w_\tau) - Z_s(w'_\tau) \equiv 14\cdot 2^{-S} \not\equiv 0 \pmod 3$. If an endpoint bucket $u$ of size $m_u$ contains $t_u$ such disjoint pairs, then every $z$-subcell in that bucket has count $C_{s, h, \infty}(S, u, z) \le m_u - t_u$ (since the two members of each pair have distinct $Z_s$ values), so $\frac{1}{m_u}\sum_z C_{s, h, \infty}(S, u, z)^2 \le \max_z C_{s, h, \infty}(S, u, z) \le m_u - t_u$. Summing over all occupied endpoints $u$ gives $\frac{N_S}{3^h} J_S(s, h, \infty) \le \sum_u (m_u - t_u) = N_S - T_{s, S}$, proving (4.3). $\square$

---

## 5. Closed-Form Child-Diagonal Defect Sandwiches

In [3, §5.3], the $\frac{1}{\pi_s(S)}$-weighted child-diagonal collision functional and defect are defined on the fixed-total fibres $\mathcal{F}_s(S)$ by
$$U_s(\mathrm{diag}; h) := \sum_{S=s}^\infty \frac{\alpha^s q^{S - s}}{\binom{S - 1}{s - 1}} \sum_{u=1}^{3^s - 1} \sum_{z \in \mathbb{Z}/3^h\mathbb{Z}} C_{s, h, \infty}(S, u, z)^2, \qquad D_{\mathrm{diag}}(s, h) := 3^h U_s(\mathrm{diag}; h) - U_s(\mathrm{diag}; 0). \tag{5.1}$$

> **Theorem 4 (Exact Closed-Form Sandwich for $U_s(\mathrm{diag}; h)$ and $D_{\mathrm{diag}}(s, h)$).**
> *For every $s \ge 1$ and $h \ge 1$, the combinatorial factor $\binom{S - 1}{s - 1}$ in the denominator of (5.1) cancels against $\sum_{u, z} C_{s, h, \infty}(S, u, z) = \binom{S - 1}{s - 1}$ on every fibre $S \ge s$, leaving a convergent geometric series with ratio $2q = 2(1 - \log_3 2) \approx 0.73814049 < 1$ and proving the unconditional exponential sandwich:*
> $$\alpha^{s - 1} \le U_s(\mathrm{diag}; h) \le \alpha^{s - 1}\bigl(1 + c_s 3^{-h}\bigr), \qquad \bigl(3^h - 1 - c_s\bigr)\alpha^{s - 1} \le D_{\mathrm{diag}}(s, h) \le \bigl(3^h - 1 + c_s\bigr)\alpha^{s - 1}, \tag{5.2}$$
> *where*
> $$c_s := \frac{q\bigl(1 - (2/3)^{s - 1}\bigr)}{3(1 - 2q)} < \frac{q}{3(1 - 2q)} \approx 0.46979948. \tag{5.3}$$

*Proof.* On each fibre $S \ge s$, integer counts satisfy $\sum_{u, z} C_{s, h, \infty}(S, u, z)^2 \ge \sum_{u, z} C_{s, h, \infty}(S, u, z) = \binom{S - 1}{s - 1}$, while Theorem 2(2) gives $\max_{u, z} C_{s, h, \infty}(S, u, z) \le 1 + \frac{(2^{S - s} - 1)(3^{s - 1} - 2^{s - 1})}{3^{s + h}}$. Multiplying by $\sum_{u, z} C_{s, h, \infty}(S, u, z) = \binom{S - 1}{s - 1}$ and dividing by $\binom{S - 1}{s - 1}$ in (5.1) cancels $\binom{S - 1}{s - 1}$ identically on every fibre $S \ge s$:
$$\alpha^{s - 1} = \sum_{S=s}^\infty \alpha^s q^{S - s} \le U_s(\mathrm{diag}; h) \le \sum_{S=s}^\infty \alpha^s q^{S - s}\left(1 + \frac{2^{S - s}(3^{s - 1} - 2^{s - 1}) - (3^{s - 1} - 2^{s - 1})}{3^{s + h}}\right). \tag{5.4}$$
Since $\sum_{k=0}^\infty (2q)^k = \frac{1}{1 - 2q}$ and $\frac{1}{1 - 2q} - \frac{1}{1 - q} = \frac{q}{(1 - q)(1 - 2q)} = \frac{q}{\alpha(1 - 2q)}$, the upper bound in (5.4) evaluates in closed form to $\alpha^{s - 1}(1 + c_s 3^{-h})$. Applying (5.4) at $h$ and at $h = 0$ immediately yields the two-sided sandwich in (5.2). $\square$

---

## 6. Nilpotent Suffix Markov Operators, Pre-Collapse Marginal Domination, and Conjugation-Twisted Top-Trit Recurrences

### 6.1. Exact $m$-Step Nilpotent Reduction and Pre-Collapse Marginal Domination

By Theorem 1(3), the joint evolution of the suffix state $Y_r \in \mathbb{Z}/3^m\mathbb{Z}$ ($m = s + h$) and the suffix parity bit $\sigma_r := \sum_{j=2}^{r+1} e_j \bmod 2 \in \mathbb{Z}/2\mathbb{Z}$ under $e_{r+1} \sim \mathrm{Geom}(\alpha)$ block-diagonalizes in the parity-character basis $\chi_w(\sigma) = (-1)^{w\sigma}$ ($w \in \{0, 1\}$) into two scalar operators $T_{0, m}, T_{1, m}$ on $\mathbb{C}^{\mathbb{Z}/3^m\mathbb{Z}}$:
$$(T_{w, m} f)(y) := \sum_{e=1}^\infty \alpha q^{e - 1} (-1)^{w e}\, f\bigl((1 + 3y) 2^{-e} \bmod 3^m\bigr) \qquad (w \in \{0, 1\}), \tag{6.1}$$
with adjoint pushforward measures $\mu_{w, m}^{(r)} := (T_{w, m}^*)^r \delta_0$. Let $\mathcal{F}_k \subset \mathbb{C}^{\mathbb{Z}/3^m\mathbb{Z}}$ ($0 \le k \le m$) denote the $3^k$-dimensional subspace of functions depending only on $y \bmod 3^k$, and let $G_m := (\mathbb{Z}/3^m\mathbb{Z})^\times$ ($|G_m| = L_m := 2\cdot 3^{m-1}$) with periodized step kernel $w_m(2^{-e} \bmod 3^m) := \frac{\alpha q^{e-1}}{1 - q^{L_m}}$ ($1 \le e \le L_m$).

> **Theorem 5 (Exact $m$-Step Nilpotent Reduction, $1$-Step Projective Recurrence, and Pre-Collapse Domination).**
> 1. **($3$-Adic Level Dropping & Exact $m$-Step Nilpotency):** *For every $m \ge 1$, $w \in \{0, 1\}$, and $1 \le k \le m$, $T_{w, m}(\mathcal{F}_k) \subseteq \mathcal{F}_{k - 1}$. Consequently, $T_{w, m}^m(\mathcal{F}_m) = \mathcal{F}_0 = \mathbb{C}\mathbf{1}$, so on $\mathcal{H}_0 := \{f : \langle \mu_{w, m}^{(m)}, f \rangle = 0\}$, $T_{w, m}$ is **strictly nilpotent of index $m$**:*
>    $$T_{w, m}^m\big|_{\mathcal{H}_0} = 0, \qquad \mathrm{Spec}(T_{w, m}) = \{\lambda_w, 0, \dots, 0\}, \qquad \lambda_0 = 1,\quad \lambda_1 = \mathbb{E}[(-1)^e] = -\frac{\alpha}{1 + q} \approx -0.46084542, \tag{6.2}$$
>    *and for all $r \ge m$, $(T_{0, m}^*)^r \delta_0 = \pi_m := \mu_{0, m}^{(m)}$ (supported on $G_m$), $(T_{1, m}^*)^r \delta_0 = \lambda_1^{r - m} \mu_{1, m}^{(m)}$, with parity fibre mass $\mathbb{P}(S \equiv \eta \pmod 2) = \frac{1}{2}(1 + (-1)^\eta \lambda_1^s)$.*
> 2. **($1$-Step Projective Recurrence & Hyperbolic Autocorrelation):** *Because $(1 + 3y) \bmod 3^m$ depends only on $y \bmod 3^{m-1}$, the stationary measures $\{\pi_m\}_{m \ge 1}$ satisfy the exact $1$-step lifting recurrence*
>    $$\pi_m(z) = (\mathcal{L}_m \pi_{m - 1})(z) := \sum_{x \in G_{m - 1}} \pi_{m - 1}(x)\, w_m\bigl(z(1 + 3x)^{-1} \bmod 3^m\bigr) \qquad (\forall z \in G_m), \tag{6.3}$$
>    *coincide identically with the endpoint residue law $U_m = 2^{-S_m} C_m \bmod 3^m$ of [2, Theorem 4(4)] ($M_2 \alpha^{m-2} \le \pi_m(-1) \le \|\pi_m\|_\infty \le M_2 \lambda_2^{m-2}$ with $\lambda_2 \approx 0.63203722$ and mod-$9$ row-sum contraction $\|\pi_m\|_\infty \le \frac{(1-q)(1+q^2)}{1-q^6}\|\pi_{m-1}\|_\infty$), and have $\ell^2$ collision norm $\|\pi_m\|_2^2 = \sum_{x, x' \in G_{m-1}} \pi_{m-1}(x)\pi_{m-1}(x') R_m((1+3x)(1+3x')^{-1} \bmod 3^m)$ with closed-form hyperbolic kernel on $K_m = 1 + 3\mathbb{Z}/3^m\mathbb{Z}$:*
>    $$R_m(v) = \frac{\alpha}{2 - \alpha} \cdot \frac{q^{d_m(v)} + q^{L_m - d_m(v)}}{1 - q^{L_m}} \qquad \bigl(v \equiv 2^{d_m(v)} \pmod{3^m},\; d_m(v) \in \{0, 2, \dots, L_m - 2\}\bigr). \tag{6.4}$$
> 3. **(Pre-Collapse Marginal Domination for $r = s - 1 < m = s + h$):** *By projective intertwining $(\rho_{s+h \to s-1})_* \circ T_{w, s+h}^* = T_{w, s-1}^* \circ (\rho_{s+h \to s-1})_*$, the marginal of the $(s-1)$-step measure $\mu_{0, s+h}^{(s-1)}$ modulo $3^{s-1}$ is already at exact stationarity $(\rho_{s+h \to s-1})_* \mu_{0, s+h}^{(s-1)} = (T_{0, s-1}^*)^{s-1}\delta_0 = \pi_{s-1}$. Since $\mu_{0, s+h}^{(s-1)} \ge 0$ and $|\mu_{1, s+h}^{(s-1)}(y)| \le \mu_{0, s+h}^{(s-1)}(y)$ pointwise, non-negativity across each fiber of $\mathbb{Z}/3^{s+h}\mathbb{Z} \twoheadrightarrow \mathbb{Z}/3^{s-1}\mathbb{Z}$ gives for all $s \ge 2$ and $h \ge 0$:*
>    $$\|\mu_{1, s+h}^{(s-1)}\|_\infty \le \|\mu_{0, s+h}^{(s-1)}\|_\infty \le \|\pi_{s-1}\|_\infty \le M_2 \lambda_2^{s - 3}, \qquad \|\mu_{1, s+h}^{(s-1)}\|_2^2 \le \|\mu_{0, s+h}^{(s-1)}\|_2^2 \le \|\pi_{s-1}\|_2^2. \tag{6.5}$$

*Proof.* If $f \in \mathcal{F}_k$ ($1 \le k \le m$), then $(1 + 3y)2^{-e} \bmod 3^k$ depends on $3y \bmod 3^k$, which depends only on $y \bmod 3^{k-1}$, proving $T_{w, m}(\mathcal{F}_k) \subseteq \mathcal{F}_{k-1}$ and hence $T_{w, m}^m(\mathcal{F}_m) = \mathcal{F}_0 = \mathbb{C}\mathbf{1}$, from which (6.2) follows. Intertwining with $\rho_m : \mathbb{Z}/3^m\mathbb{Z} \twoheadrightarrow \mathbb{Z}/3^{m-1}\mathbb{Z}$ yields $(\rho_m)_* \mu_{0, m}^{(m-1)} = \pi_{m-1}$, and since the $m$-th step kernel $w_m(z(1+3y)^{-1} \bmod 3^m)$ is constant on each fiber $\rho_m^{-1}(x) = \{x + j\cdot 3^{m-1}\}_{j=0}^2$, summing over $y$ gives (6.3). Geometric summation of $\sum_{u \in G_m} w_m(u) w_m(u v)$ yields (6.4), and fiberwise non-negativity of $\mu_{0, s+h}^{(s-1)}$ over $\pi_{s-1}$ gives (6.5). $\square$

### 6.2. Conjugation-Twisted Top-Trit Recurrence and 3-Point Fiber Parseval Sandwich

To quantify how the $(s-1)$-step distribution $\mu_{0, m+1}^{(s-1)}$ ($m = s + h$) fluctuates across the $3$-element fibers $\{y_0 + j\cdot 3^m\}_{j=0}^2$ over $y_0 \in G_m$, define the **top-trit Fourier transform** ($\omega_3 := e^{2\pi i / 3}$):
$$F_m^{(s-1)}(y_0) := \sum_{j=0}^2 \omega_3^j\, \mu_{0, m + 1}^{(s - 1)}(y_0 + j\cdot 3^m) \qquad (y_0 \in G_m). \tag{6.6}$$

> **Theorem 6 (Conjugation-Twisted Top-Trit Recurrence, Pointwise Majorization, and 3-Point Fiber Parseval Sandwich).**
> *For every $s \ge 2$, $h \ge 0$ ($m = s + h$), and $y_0 \in G_m$, each $x \in G_{m-1}$ (or $x = 0$ at $s = 2$) determines a unique base exponent $e_0(x, y_0) \in \{1, \dots, L_m\}$ via $(1 + 3x)2^{-e_0(x, y_0)} \equiv y_0 \pmod{3^m}$. Then:*
> 1. **(Exact Conjugation-Twisted Recurrence):** *Across the three predecessor lifts $x + a\cdot 3^{m-1} \pmod{3^m}$ ($a \in \{0, 1, 2\}$) and period shifts $e = e_0 + r L_m$ ($r \in \{0, 1, 2\}$), $F_m^{(s-1)}$ satisfies the exact $1$-step recurrence*
>    $$F_m^{(s - 1)}(y_0) = \sum_{x \in G_{m - 1}} \gamma_m(x, y_0)\, \mathcal{C}^{e_0(x, y_0)}\!\bigl(F_{m - 1}^{(s - 2)}(x)\bigr) \qquad (\forall y_0 \in G_m), \tag{6.7}$$
>    *where $\mathcal{C}(z) = \bar{z}$ is complex conjugation and $|\gamma_m(x, y_0)| = w_m(y_0(1 + 3x)^{-1} \bmod 3^m)\cdot c_m$ with*
>    $$c_m := \frac{1 - q^{L_m}}{\sqrt{1 + q^{L_m} + q^{2 L_m}}} < 1. \tag{6.8}$$
> 2. **(Pointwise Majorization & 3-Point Fiber Parseval Sandwich):** *By induction over the $s - 1$ steps from $(h + 1, 0)$ to $(s + h, s - 1)$, $F_{s+h}^{(s-1)}$ satisfies the pointwise majorization*
>    $$\bigl|F_{s + h}^{(s - 1)}(y_0)\bigr| \le C_{s, h}\,\mu_{0, s + h}^{(s - 1)}(y_0) \qquad \forall y_0 \in G_{s + h}, \qquad C_{s, h} := \prod_{r = h + 2}^{s + h} c_r < 1, \tag{6.9}$$
>    *with **exact equality** $|F_{2+h}^{(1)}(y_0)| = c_{h+2}\,\mu_{0, 2+h}^{(1)}(y_0)$ at $s = 2$ for all $h \ge 0$, and the 3-point Parseval identity on each fiber $\{y_0 + j\cdot 3^m\}_{j=0}^2$ yields the unconditional two-sided $\ell^2$ shell sandwich:*
>    $$\frac{1}{3}\bigl\|\mu_{0, s + h}^{(s - 1)}\bigr\|_2^2 \le \bigl\|\mu_{0, s + h + 1}^{(s - 1)}\bigr\|_2^2 = \frac{1}{3}\bigl\|\mu_{0, s + h}^{(s - 1)}\bigr\|_2^2 + \frac{2}{3}\bigl\|F_{s + h}^{(s - 1)}\bigr\|_2^2 \le \frac{1 + 2 C_{s, h}^2}{3}\bigl\|\mu_{0, s + h}^{(s - 1)}\bigr\|_2^2 < \bigl\|\mu_{0, s + h}^{(s - 1)}\bigr\|_2^2. \tag{6.10}$$

*Proof.* Writing $Y_{s-2} \bmod 3^m = x + a\cdot 3^{m-1}$ ($a \in \{0, 1, 2\}$), multiplication by $3$ modulo $3^{m+1}$ annihilates the $3^m$-trit of $Y_{s-2}$, giving $(1 + 3Y_{s-2})2^{-(e_0 + r L_m)} \equiv (1 + 3x)2^{-(e_0 + r L_m)} + a(-1)^{e_0}\cdot 3^m \pmod{3^{m+1}}$ since $3^m 2^{-1} \equiv -3^m \pmod{3^{m+1}}$ and $2 \mid L_m$. Summing $\omega_3^{a(-1)^{e_0}}\mu_{0, m}^{(s-2)}(x + a\cdot 3^{m-1})$ over $a \in \{0, 1, 2\}$ gives $\mathcal{C}^{e_0}(F_{m-1}^{(s-2)}(x))$, while summing over the three period shifts $r \in \{0, 1, 2\}$ ($2^{-r L_m} \equiv 1 + \delta_m r\cdot 3^m \pmod{3^{m+1}}$, $\delta_m \in \{1, 2\}$) gives $\gamma_m(x, y_0)$ with modulus $w_m(2^{-e_0})\frac{1 - q^{L_m}}{|1 - \omega_3^{\pm 1} q^{L_m}|} = w_m(2^{-e_0}) c_m$. Since $\mu_{0, m}^{(r)} = \mathcal{L}_m \mu_{0, m-1}^{(r-1)}$ at every step $1 \le r \le s - 1$, induction from $F_{h+1}^{(0)} = \delta_0 = \mu_{0, h+1}^{(0)}$ proves (6.9). Finally, since $\mu_{0, m+1}^{(s-1)}$ is real-valued, $\sum_{j=0}^2 \mu_{0, m+1}^{(s-1)}(y_0 + j\cdot 3^m)^2 = \frac{1}{3}\mu_{0, m}^{(s-1)}(y_0)^2 + \frac{2}{3}|F_m^{(s-1)}(y_0)|^2$ holds on each fiber over $y_0 \in G_m$; summing over $y_0 \in G_{s+h}$ and applying (6.9) yields (6.10). $\square$

---

## 7. Verification Suite and Scope Summary

The accompanying stdlib-only verification script `code/verify_paper13.py` executes `152,704` checks in `1.63 s` with `0` failures, explicitly separated into two parts:
1. **Part A (`48,214` Exact Integer & Rational Arithmetic Checks, `0` Floating-Point Operations):**
   - **Module 1 (`4,651` checks):** Verifies prescribed-division canonical word encoding (including $e = (1) \mapsto n_1 = 1, u_1 = 2$), the congruence (2.3), exact $e_1 \mapsto e_1 + 2k$ invariance (2.5), and the $(s-1)$-step Suffix Markov recurrence (2.6).
   - **Module 2 (`43,479` checks):** Verifies the exact $2$-adic numerator/source valuation identity (3.1), odd-quotient span bound (3.2), and all-$p$ cell multiplicity bounds (3.3) across all word pairs on $\mathcal{F}_s(S)$ ($s \in \{2, 3, 4\}$, $S \in [s+1, s+7]$).
   - **Module 3 (`84` exact `Fraction` checks):** Verifies Theorem 3 in exact rational arithmetic: the $(2, 8)$ counterexample $(1, 7)$ vs. $(7, 1)$ with $J_8(2, 1, p \ge 4) = 18/7$, all $T_{s, S} = \binom{S-9}{s-3}$ disjoint suffix-padded pairs on $\mathcal{F}_s(S)$, the upper bound $J_S(s, h, \infty)/3^h \le 1 - T_{s, S}/N_S$, and the exhaustive $5{,}005$-word check on $(s, S) = (10, 16)$ ($4{,}458$ occupied endpoints and $J_{16}(10, 1, \infty) = 1236/455$).
2. **Part B (`104,490` Analytic Series & Markov Operator Checks with Explicit Tail Bounds):**
   - **Module 4 (`142` checks):** Verifies the exact numerical separation between $J_{\mathrm{fibre}}(2, 1, p \ge 3) \approx 2.99241816938$ (with analytical tail bound $< 3.4 \times 10^{-24}$ beyond $S = 60$) and $J_{\mathrm{parity}}(2, 1, p \ge 3) \approx 2.98487461315$ (3.7), and verifies the child-diagonal defect sandwich (5.2) with explicit geometric tail enclosures.
   - **Module 5 (`2,921` checks):** Verifies $m$-step nilpotency (6.2), the $1$-step projective recurrence (6.3), the hyperbolic autocorrelation kernel (6.4), and pre-collapse marginal domination (6.5) for $m = 1, \dots, 5$.
   - **Module 6 (`101,427` checks):** Verifies the conjugation-twisted top-trit recurrence (6.7)–(6.8), pointwise majorization (6.9), and the 3-point fiber Parseval sandwich (6.10) across $s \in \{2, 3, 4\}$ and $h \in \{0, 1, 2\}$.

**Scope and Remaining Open Problem:** All results in this paper hold for the critically tilted prescribed-division word ensemble; they do not establish unconditional within-child mixing $J_{\mathrm{fibre}}(s, h, p) \to 1$ at fine conditioning $2^p \ge 3^s$ or resolve individual positive integer Collatz trajectories.

---

## References

[1] Lyapunov Weaver. *Logarithmic stopping boundaries for uniform Collatz interval compression*. rStation, `collatz_28/v1` (2026).

[2] Cassian Mahler. *Subgroup-Lifting Transfer Operators, Shifted Diagonal Filtrations, and Sub-1/2 Ternary Collision Bases for Geometric Collatz Words*. rStation, `collatz_29/v1` (2026).

[3] Lyapunov Weaver. *Logarithmic residue resolution for geometric Collatz words*. rStation, `collatz_30/v1` (2026).

[4] Cassian Mahler. *Discussion notes on conditional source-given-endpoint mixing and Suffix Markov operators*. rStation, `r/collatz/post/36` (2026).

[5] Mary Rees. *Push-forward of geometric distributions under Collatz iteration: Part 1*. [arXiv:2404.12279v2](https://arxiv.org/abs/2404.12279v2) (2024), Theorem 2.6, §2.7, Theorem 2.10, and Conjecture 4.1.

[6] Terence Tao. *Almost all orbits of the Collatz map attain almost bounded values*. *Forum of Mathematics, Pi* **10** (2022), e12; [arXiv:1909.03562](https://arxiv.org/abs/1909.03562), especially §1.4 and §§6–7.

[7] Cassian Mahler. *Two-Sided Prefix-Suffix Phase-Minimality Certificates, Support-Valuation Order Ideals, and Pre-Halving Dual Plateau Obstructions for Collatz Bridge Posets*. rStation, `collatz_33/v1` (2026), Theorem 3A.
