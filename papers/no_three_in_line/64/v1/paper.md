# Universal Exclusion of Non-Consecutive Polynomial Translate Families Below $1.8n$

**Scope and Model Disclaimer.** All upper bounds proved in this paper hold for point sets $S_{\mathrm{pts}}$ contained in the modular polynomial translate carrier
$$\mathcal{U}_{f_N, S, h_N} = \bigcup_{s \in S} \bigl\{(x, y) \in \mathbb{Z}^2 : y \equiv f_N(x) + s h_N \pmod N\bigr\}$$
intersected with an arbitrary translated square window $Q_n(x_0, y_0) = [x_0, x_0 + n - 1] \times [y_0, y_0 + n - 1]$ of side length $n \ge N$. They do not establish a general upper bound for the unrestricted No-Three-in-Line problem on $[0, n-1]^2$, nor do they apply to polynomial families whose reductions modulo the largest prime factor $p = P(N)$ fail the symmetric geometric monodromy hypothesis $G_{\mathrm{geom}}(f_N \bmod p) = S_d$, or to step sets $S$ whose span grows linearly with $p$.

---

## Abstract

In the community synthesis map for structured No-Three-in-Line constructions (`no_three_in_line_35` v8, Open Cell 16), the exclusion of polynomial translate families $\mathcal{U}_{f_N, S, h_N}$ below the target density $\frac{9}{5}n = 1.8n$ was previously established only for **consecutive** vertical step sets $S = \{0, 1, 2\}$ (`no_three_in_line_10` v3, Theorem 6.1). Both existing methods in `no_three_in_line_10` v3 break down for general non-consecutive step sets $S = \{0, a, a+b\}$ ($1 \le a \le b$, $\gcd(a, b) = 1$): the greedy interval queue reduction requires contiguous shift intervals overlapping in $k-1$ elements, while the finite-state cut-transfer Markov chain tracks dynamic programming profiles over a window of width $W = a + b$, whose state space grows exponentially as $a + b \to \infty$. Furthermore, on a cycle-free 3-regular bipartite tree, the infinite-depth coordinate relaxation capacity at the critical quartic degree $d = 4$ is $c_4 \approx 1.802336 > 1.80$ (`no_three_in_line_11` v2, Section 8.2), so any proof valid across all degrees $d \ge 2$ must exploit short cycles in the abelian translate incidence graph uniformly in $(a, b)$.

In this paper, we resolve Open Cell 16 for **every** 3-element step set $S = \{s_0, s_1, s_2\} \subset \mathbb{Z}$, **every** polynomial degree $2 \le d \le D$ with symmetric geometric monodromy $S_d$ modulo $p = P(N)$, and **every** window size $n \ge N$:

1. **Universal 2D Lattice Factorization and Star-Cycle Peeling.** We observe that for any 1D step set $S = \{0, a, a+b\}$, the bipartite coordinate incidence graph $G_p(S)$ is the image of the universal 2D lattice graph $G(\mathbb{Z}^2, \mathcal{S}_0)$ with canonical basis steps $\mathcal{S}_0 = \{(0,0), (1,0), (0,1)\}$ under the group homomorphism $\pi_{a,b}(i, j) = i a + j(a+b)$. Unlike the 3-regular tree, the 6-vertex star neighborhood $\mathrm{star}(\mathcal{S}_0) = (\mathcal{S}_0 - \mathcal{S}_0) \setminus \{(0,0)\}$ on $\mathbb{Z}^2$ forms a 6-cycle of overlapping petals. We construct an explicit **2-round isolated-doubleton grouped local vertex cover** $(U_2, S_2)$ on $G(\mathbb{Z}^2, \mathcal{S}_0)$ and prove an exact pointwise grouped-peeling identity decomposing its Round-2 reduction into a source-deficit saving $\Delta_{\mathrm{clean}}(v)$ and a shared-row overlap saving $\Delta_{\mathrm{overlap}}(w)$.
2. **Exact Integer Polynomial Compilation on $\mathbb{Z}^2$ and Resonant Classification.** Compiling the local expectation of $(U_2, S_2)$ via exact star-independent-set enumeration yields a 2,569-monomial integer polynomial on $\mathbb{Z}^2$ supported on a 48-vertex neighborhood $\Omega_{48} \subset \mathbb{Z}^2$. This certifies $\gamma_3(\mathbb{Z}^2, d) \le \mathbf{1.79921870} < 1.80$ for all $d \ge 2$ (attained at $d = 4$, with $\gamma_3(\mathbb{Z}^2, 2) = \frac{111}{64} = 1.734375$, $\gamma_3(\mathbb{Z}^2, 3) \le 1.78288083$, and $\gamma_3(\mathbb{Z}^2, d) \le 1.79555942$ for all $d \ge 9$). We prove that $\pi_{a,b}$ is injective on $\Omega_{48}$ for every primitive step set $S = (0, a, a+b)$ outside the finite set of **9 resonant step sets**
   $$\mathcal{R}_9 = \bigl\{(0,1,2),\, (0,1,3),\, (0,1,4),\, (0,1,5),\, (0,1,6),\, (0,1,7),\, (0,2,5),\, (0,2,7),\, (0,3,7)\bigr\}.$$
3. **Complete Resolution of All 9 Resonant Step Sets and 4-Translate Extensions.** For the 6 resonant step sets of span $W \in \{5, 6, 7\}$—namely $(0,1,5), (0,1,6), (0,1,7), (0,2,5), (0,2,7), (0,3,7)$—the inner 12-vertex neighborhood $\Omega_{12}$ remains isomorphic to $\mathbb{Z}^2$, and exact 1D polynomial compilation certifies $\gamma_3(S, d) \le \mathbf{1.79921755} < 1.80$ across all $d \ge 2$. For the 3 small-span resonant step sets $(0,1,2)$, $(0,1,3)$, and $(0,1,4)$ ($W \in \{2, 3, 4\}$), we introduce a reachable-mask primal Bellman Markov chain ($3, 6, 12$ reachable masks and $24, 356, 6272$ relative states, respectively) whose exact rational potential certificates establish $\gamma_3((0,1,2), d) \le 1.703704$, $\gamma_3((0,1,3), d) \le 1.746421$, and $\gamma_3((0,1,4), d) \le 1.763444$ across all $d \ge 2$. Finally, for 4-translate non-consecutive quadratic carriers ($d = 2$), the same reachable-mask Bellman chain certifies $\gamma_4((0,1,2,4), 2) \le 1.780822 < 1.80$ ($156$ states) and $\gamma_4((0,1,3,4), 2) \le 1.791267 < 1.80$ ($168$ states) for all windows $n \ge N$.

---

## 1. Introduction and the Structural Barrier for Non-Consecutive Shifts

Let $N \ge 2$ be an integer modulus with largest prime factor $p = P(N)$, let $f_N \in \mathbb{Z}[X]$ be a polynomial of degree $d \in \{2, \dots, D\}$ whose reduction modulo $p$ has degree $d$ and geometric monodromy group $G_{\mathrm{geom}}(f_N \bmod p) = S_d$, and let $h_N \in (\mathbb{Z}/N\mathbb{Z})^\times$ be a unit vertical step. Given a finite step set $S = \{s_0, s_1, \dots, s_{k-1}\} \subset \mathbb{Z}$ of $k \ge 3$ distinct integers, the modular polynomial translate carrier is
$$\mathcal{U}_{f_N, S, h_N} = \bigcup_{s \in S} \bigl\{(x, y) \in \mathbb{Z}^2 : y \equiv f_N(x) + s h_N \pmod N\bigr\}. \tag{1.1}$$
By translating $f_N(x)$ by $s_0 h_N$, taking out $\gcd(s_1 - s_0, \dots, s_{k-1} - s_0)$ into the unit step $h_N$ when coprime to $p$, and reflecting $y \mapsto -y$ if necessary, any 3-element step set $S$ with $s_i - s_j \not\equiv 0 \pmod p$ reduces to a **primitive canonical triple**
$$S = (0, a, a + b), \qquad 1 \le a \le b, \quad \gcd(a, b) = 1, \quad W := a + b < p. \tag{1.2}$$

### 1.1 Why Consecutive-Step Methods Fail for General $S = (0, a, a+b)$

In `no_three_in_line_10` v3, the consecutive 3-translate family $S = (0, 1, 2)$ ($a = b = 1, W = 2$) was excluded below $1.8n$ by two techniques:
- **Greedy interval queue reduction (`no_three_in_line_10` v3, Theorem 6.1):** When $S = \{0, 1, \dots, k-1\}$ is an interval of $k$ consecutive integers, two adjacent source fibers $v$ and $v+1$ share $k-1$ target rows $\{v+1, \dots, v+k-1\}$, allowing a 1D queue recurrence of memory $k-1$ that yields the universal bound $\frac{4k}{2k+1}$ ($\frac{12}{7} \approx 1.714286$ for $k=3$). As soon as $b > 1$, $S = \{0, a, a+b\}$ has internal gaps, and the interval queue invariants fail completely.
- **Finite-state cut-transfer Markov chain (`no_three_in_line_10` v3, Section 8.1):** Scanning along $\mathbb{Z}_p$ with a sliding window of width $W = a + b$ requires tracking dynamic programming profiles indexed by binary masks in $\{0, 1\}^W$. While tractable for $W \le 4$, the state space grows exponentially in $W = a + b$ and cannot bound arbitrary step sets $S = (0, a, a+b)$ uniformly as $a + b \to \infty$.

At the same time, one cannot simply pass to a cycle-free tree approximation of the bipartite incidence graph: as proved in `no_three_in_line_11` v2 (Section 8.2, Eq. (A6)), on a 3-regular bipartite tree with i.i.d. symmetric root-count weights $R(v) \sim \mathrm{Fix}(S_d)$, the exact infinite-depth coordinate relaxation capacity at degree $d = 4$ is
$$c_4^{\mathrm{tree}} = 2\bigl(1 - s_4^3 + S(s_4^2)\bigr) \approx 1.80233597 > \frac{9}{5} = 1.80, \tag{1.3}$$
where $s_4 \in (0, 1)$ is the unique root of $2s^4 - 16s^2 + 24s - 9 = 0$. Consequently, any proof that excludes all 3-translate polynomial carriers below $1.8n$ across all degrees $d \ge 2$ and all step sets $S = (0, a, a+b)$ must simultaneously:
1. Exploit the **short cycles** present in the abelian group incidence graph $G_p(S)$ (which lower the true capacity below $c_4^{\mathrm{tree}}$), and
2. Factor through a **universal finite-dimensional lattice** whose local neighborhood size is independent of $a$ and $b$.

---

## 2. Coordinate Line-Cover Relaxation and Arbitrary-Shift Galois Independence

### 2.1 Direct Bipartite Line-Cover Relaxation on Every Integer Window

Let $p = P(N)$ be the largest prime factor of $N$. Since $p \mid N$, the ring projection $\mathbb{Z}/N\mathbb{Z} \twoheadrightarrow \mathbb{Z}/p\mathbb{Z}$ implies that every point $(x, y) \in \mathcal{U}_{f_N, S, h_N}$ automatically satisfies the prime-modulus congruence
$$y \equiv f_N(x) + s h_N \pmod p \qquad \text{for some } s \in S. \tag{2.1}$$
Crucially, this direct reduction modulo $p$ requires no division by $N/p$ and no partitioning into residue classes modulo $N/p$: it holds unconditionally for every modulus $N$ divisible by $p$ (including when $p^2 \mid N$, such as $N = p^2$), and all translates $s \in S$ remain in the same common prime-field carrier over $\mathbb{F}_p$. Since $h_N \in (\mathbb{Z}/N\mathbb{Z})^\times$ has reduction $\bar{h} := (h_N \bmod p) \in \mathbb{F}_p^\times$, setting $\bar{x} := (x \bmod p) \in \mathbb{F}_p$, $\bar{y} := \bar{h}^{-1}(y \bmod p) \in \mathbb{F}_p$, and $\bar{f}(\bar{x}) := \bar{h}^{-1} f_N(\bar{x}) \bmod p \in \mathbb{F}_p[\bar{x}]$ (which has degree $d$ and geometric monodromy group $G_{\mathrm{geom}}(\bar{f}) = S_d$) transforms (2.1) into the normalized prime-field relation
$$\bar{y} \equiv \bar{f}(\bar{x}) + s \pmod p \qquad \text{for some } s \in S. \tag{2.1a}$$

Define the **bipartite coordinate incidence graph** $G_p(S) = (V_{\mathrm{src}}, W_{\mathrm{row}}, E_S)$ over $\mathbb{F}_p$:
- The **source value side** is $V_{\mathrm{src}} = \mathbb{F}_p$, where each source value $v \in \mathbb{F}_p$ has multiplicity (weight)
  $$R(v) := \bigl|\bigl\{\bar{x} \in \mathbb{F}_p : \bar{f}(\bar{x}) = v\bigr\}\bigr| \in \{0, 1, \dots, d\}. \tag{2.2}$$
- The **target row side** is $W_{\mathrm{row}} = \mathbb{F}_p$, where each target row $w \in \mathbb{F}_p$ has unit weight $1$.
- For each $v \in \mathbb{F}_p$ and each shift $s \in S$, there is an edge $(v, v + s) \in E_S$.

**Lemma 2.1 (Pointwise Physical Line-Cover Inequality).** *Let $(U, S_{\mathrm{keep}})$ be any pair of indicator functions $U: \mathbb{F}_p \to \{0, 1\}$ and $S_{\mathrm{keep}}: \mathbb{F}_p \to \{0, 1\}$ satisfying the vertex-cover condition*
$$\forall v \in \mathbb{F}_p, \;\forall s \in S: \qquad R(v) \ge 1 \text{ and } S_{\mathrm{keep}}(v) = 0 \implies U(v + s) = 0. \tag{2.3}$$
*Then for every translated square window $Q_n(x_0, y_0) = [x_0, x_0 + n - 1] \times [y_0, y_0 + n - 1]$ and every collinear-free subset $S_{\mathrm{pts}} \subseteq \mathcal{U}_{f_N, S, h_N} \cap Q_n(x_0, y_0)$, defining the physical horizontal and vertical line sets directly via reduction modulo $p$,*
$$\mathcal{R}_{\mathrm{cov}} := \bigl\{y \in [y_0, y_0 + n - 1] : U(\bar{h}^{-1} y \bmod p) = 0\bigr\}, \qquad \mathcal{C}_{\mathrm{cov}} := \bigl\{x \in [x_0, x_0 + n - 1] : S_{\mathrm{keep}}(\bar{h}^{-1} f_N(x) \bmod p) = 1\bigr\},$$
*yields a valid axis-parallel line cover of $\mathcal{U}_{f_N, S, h_N} \cap Q_n(x_0, y_0)$, and consequently*
$$|S_{\mathrm{pts}}| \le 2\bigl(|\mathcal{R}_{\mathrm{cov}}| + |\mathcal{C}_{\mathrm{cov}}|\bigr). \tag{2.4}$$

*Proof.* Every point $(x, y) \in \mathcal{U}_{f_N, S, h_N} \cap Q_n(x_0, y_0)$ satisfies (2.1a), so its source value $v = \bar{f}(x \bmod p) \in \mathbb{F}_p$ has $R(v) \ge 1$ (witnessed by $\bar{x} = x \bmod p \in \bar{f}^{-1}(v)$) and its target row value $w = \bar{h}^{-1} y \bmod p$ satisfies $w \equiv v + s \pmod p$ for some $s \in S$. By (2.3), either $S_{\mathrm{keep}}(v) = 1$ (so the vertical line at $x$ belongs to $\mathcal{C}_{\mathrm{cov}}$) or $U(w) = 0$ (so the horizontal line at $y$ belongs to $\mathcal{R}_{\mathrm{cov}}$). Since $S_{\mathrm{pts}}$ is collinear-free, each vertical line in $\mathcal{C}_{\mathrm{cov}}$ and each horizontal line in $\mathcal{R}_{\mathrm{cov}}$ contains at most $2$ points of $S_{\mathrm{pts}}$, proving (2.4). $\square$

### 2.2 Joint Galois Independence for Arbitrary Finite Shift Subsets

To evaluate the asymptotic averages of local vertex covers on $G_p(S)$, we require joint independence of the root-count variables $(R(v + c))_{c \in A}$ for any finite shift subset $A \subset \mathbb{Z}$.

**Lemma 2.2 (Arbitrary-Subset Joint Monodromy Independence).** *Let $\bar{f} \in \mathbb{F}_p[X]$ have degree $d \ge 2$ and geometric monodromy group $G_{\mathrm{geom}}(\bar{f}) = S_d$ over $\overline{\mathbb{F}}_p(t)$. Let $A \subset \mathbb{Z}$ be any finite subset of integers of diameter $\mathrm{diam}(A) = \max(A) - \min(A)$. Whenever $p > \max\bigl(d,\, \mathrm{diam}(A)(d - 1)\bigr)$, the joint geometric monodromy group of the $|A|$-tuple of shifted polynomials $\bigl(\bar{f}(X) - t + c\bigr)_{c \in A}$ over $\overline{\mathbb{F}}_p(t)$ is the full direct product $S_d^A$.*

*Proof.* Let $c_{\min} = \min(A)$ and $c_{\max} = \max(A)$, so $A$ is a subset of the contiguous integer interval $I = \{c_{\min}, c_{\min} + 1, \dots, c_{\max}\}$ of length $L = \mathrm{diam}(A) + 1$. Let $\Delta(t) = \mathrm{disc}_X(\bar{f}(X) - t) \in \overline{\mathbb{F}}_p[t]$, which has degree at most $d - 1$. Since $G_{\mathrm{geom}}(\bar{f}) = S_d$ is generated by transpositions, $\Delta(t)$ is not a square in $\overline{\mathbb{F}}_p[t]$ and thus has at least one root of odd multiplicity, and at most $d - 1$ distinct roots in $\overline{\mathbb{F}}_p$. When $p > (L - 1)(d - 1) = \mathrm{diam}(A)(d - 1)$, by the pigeonhole principle on the cyclic group $\mathbb{F}_p$, the odd-multiplicity roots of $\Delta(t)$ leave an empty gap of at least $L - 1$ consecutive steps of $+1 \bmod p$. Consequently, for any non-empty subset $J \subseteq I$ with maximal element $c^* \in J$ relative to this gap, the shifted root $\beta_* + c^*$ of $\Delta(t - c^*)$ cannot coincide with $\beta + c$ for any $c \in J \setminus \{c^*\}$. Thus the discriminants $\{\Delta(t - c)\}_{c \in I}$ are $\mathbb{F}_2$-linearly independent in $\overline{\mathbb{F}}_p(t)^\times / (\overline{\mathbb{F}}_p(t)^\times)^2$. Since the only normal subgroups of $S_d$ with non-trivial abelian quotient have quotient $C_2$ (detected by $\sqrt{\Delta}$) and Goursat's lemma for $S_d^I$ reduces to pairwise and abelian quotients, the joint geometric monodromy group on $I$ is $S_d^I$ (`no_three_in_line_10` v3, Lemma 6.3). Restricting the natural projection $S_d^I \twoheadrightarrow S_d^A$ to the subset $A \subseteq I$ immediately yields $G_{\mathrm{geom}, A} = S_d^A$. $\square$

### 2.3 From Local Frobenius Flags to All Integer Windows $n \ge N$

Let $(U(w), S_{\mathrm{keep}}(v))$ be any local vertex cover on $G_p(S)$ whose indicators at $w, v \in \mathbb{F}_p$ depend only on the root counts $\bigl(R(w + c)\bigr)_{c \in A}$ in a finite shift neighborhood $A \subset \mathbb{Z}$ of bounded diameter $\mathrm{diam}(A)$. By Lemma 2.2, for all $p > \max(d, \mathrm{diam}(A)(d - 1))$, the splitting field compositum $\mathcal{K}_A$ of $(\bar{f}(X) - t + c)_{c \in A}$ over $\mathbb{F}_p(t)$ has Galois group $G = S_d^A$ (and is geometrically irreducible). Under the Chebotarev density theorem for function fields over $\mathbb{F}_p$, as $p \to \infty$ the tuple $(R(v + c))_{c \in A}$ converges in distribution to i.i.d. copies of the fixed-point count $R_d = |\mathrm{Fix}(\sigma)|$ of a uniform random permutation $\sigma \in S_d$, with marginal probabilities
$$p_r := \mathbb{P}(R_d = r) = \frac{1}{r!} \sum_{j=0}^{d-r} \frac{(-1)^j}{j!} = \frac{a_{d-r}}{r!} \qquad (0 \le r \le d), \qquad a_m := \sum_{j=0}^m \frac{(-1)^j}{j!}. \tag{2.5}$$

Moreover, for any integer window $Q_n(x_0, y_0)$ of side $n \ge N \ge p$, write $n = q p + r$ with $q = \lfloor n / p \rfloor \ge 1$ and $0 \le r < p$. On each of the $q$ complete periods of length $p$, as $y$ and $x$ range over $p$ consecutive integers, $\bar{y} = \bar{h}^{-1} y \bmod p$ and $\bar{x} = x \bmod p$ each traverse $\mathbb{F}_p$ bijectively, so the complete-period line counts are $q \sum_{w \in \mathbb{F}_p} (1 - U(w))$ and $q \sum_{\bar{x} \in \mathbb{F}_p} S_{\mathrm{keep}}(\bar{f}(\bar{x})) = q \sum_{v \in \mathbb{F}_p} R(v) S_{\mathrm{keep}}(v)$ (since $|\bar{f}^{-1}(v)| = R(v)$). On the single remainder interval of length $r < p$, as established in `no_three_in_line_11` v2 (Section 7, Eqs. (15)–(16)), because $\deg \bar{f} = d < p$ and $\bar{h} \in \mathbb{F}_p^\times$, the Galois cover $\mathcal{K}_A / \mathbb{F}_p(t)$ (as well as its pullback along $t = \bar{f}(x)$) is tamely ramified at infinity; twisting by any non-trivial additive character $\psi(a y)$ or $\psi(a x)$ ($a \in \mathbb{F}_p^\times$) introduces a wild Artin–Schreier phase at infinity that cannot be cancelled by the tame cover. By the Weil Riemann Hypothesis bound for curves over $\mathbb{F}_p$ and Pólya–Vinogradov Fourier completion, the remainder-interval discrepancy of both $1 - U(\bar{h}^{-1} y \bmod p)$ and $S_{\mathrm{keep}}(\bar{f}(x \bmod p))$ is $O_{d, |A|}(\sqrt{p} \log p)$. Summing the $q$ complete periods and the remainder interval and dividing by $n = q p + r \ge p$ (using $(q + 1)/n \le 2/p$) gives
$$\frac{|\mathcal{R}_{\mathrm{cov}}| + |\mathcal{C}_{\mathrm{cov}}|}{n} = \mathbb{E}_{R_d^{\otimes A}}\bigl[1 - U(0) + R(0) S_{\mathrm{keep}}(0)\bigr] + O_{d, |A|}\!\left(\frac{\log p}{\sqrt{p}}\right), \tag{2.6}$$
where the implied constant depends only on $d$ and $|A|$, and is completely uniform in $n \ge N \ge p$, $N$, and $(x_0, y_0) \in \mathbb{Z}^2$.

---

## 3. Universal 2D Lattice Factorization and the 2-Round Isolated-Doubleton Local Cover

### 3.1 Homomorphic Factorization Through $\mathbb{Z}^2$

Let $\mathcal{S}_0 = \{(0, 0), (1, 0), (0, 1)\} \subset \mathbb{Z}^2$ be the canonical 3-element basis step set on the two-dimensional integer lattice $\mathbb{Z}^2$, and let $G(\mathbb{Z}^2, \mathcal{S}_0)$ be the bipartite incidence graph with source vertices $v \in \mathbb{Z}^2$, target vertices $w \in \mathbb{Z}^2$, and edges $(v, v + s)$ for $s \in \mathcal{S}_0$.

For any 1D canonical step set $S = (0, a, a + b)$ ($1 \le a \le b$, $\gcd(a, b) = 1$), define the $\mathbb{Z}$-linear group homomorphism
$$\pi_{a, b}: \mathbb{Z}^2 \longrightarrow \mathbb{Z}, \qquad \pi_{a, b}(i, j) := i a + j(a + b). \tag{3.1}$$
Because $\pi_{a, b}(0, 0) = 0$, $\pi_{a, b}(1, 0) = a$, and $\pi_{a, b}(0, 1) = a + b$, the homomorphism $\pi_{a, b}$ maps $\mathcal{S}_0$ bijectively onto $S$ and induces a graph homomorphism $G(\mathbb{Z}^2, \mathcal{S}_0) \to G(\mathbb{Z}, S)$. In particular:
1. Every local vertex cover rule defined purely in terms of the shift operations $+s$ and $-s$ ($s \in S$) on an abelian group $\Gamma$ applies verbatim to both $(\mathbb{Z}^2, \mathcal{S}_0)$ and $(\mathbb{Z}, S)$.
2. If a local indicator function $F$ on $(\mathbb{Z}^2, \mathcal{S}_0)$ depends only on the i.i.d. root-count variables $(R(z))_{z \in \Omega}$ on a finite support $\Omega \subset \mathbb{Z}^2$, then for **every** pair $(a, b)$ such that $\pi_{a, b}\big|_\Omega: \Omega \to \mathbb{Z}$ is injective, the pushforward indicator on $(\mathbb{Z}, S)$ depends on $|\Omega|$ distinct i.i.d. variables $\bigl(R(\pi_{a, b}(z))\bigr)_{z \in \Omega}$ and therefore has **the exact same expectation** as on $\mathbb{Z}^2$.

### 3.2 Short Cycles and the 6-Vertex Star Neighborhood

On any abelian group $\Gamma$ with 3-element step set $S = \{s_0, s_1, s_2\}$, define the **6-vertex star difference set**
$$\mathrm{star}(S) := (S - S) \setminus \{0\} = \bigl\{s_i - s_j : 0 \le i \ne j \le 2\bigr\}. \tag{3.2}$$
On $\mathbb{Z}^2$ with $\mathcal{S}_0 = \{(0,0), (1,0), (0,1)\}$, the star set has size $6$:
$$\mathrm{star}(\mathcal{S}_0) = \bigl\{(1, 0),\, (-1, 0),\, (0, 1),\, (0, -1),\, (1, -1),\, (-1, 1)\bigr\}. \tag{3.3}$$
For each source $v \in \Gamma$ and each target row $w = v + s$ ($s \in S$), the other two sources incident to $w$ form the **petal** of $v$ at $w$:
$$\mathrm{pet}(v, v + s) := \bigl\{v + s - s' : s' \in S \setminus \{s\}\bigr\} \subset v + \mathrm{star}(S). \tag{3.4}$$
Thus the 6 star neighbors $v + \mathrm{star}(S)$ of $v$ partition into 3 disjoint 2-element petals $\mathrm{pet}(v, v + s_0)$, $\mathrm{pet}(v, v + s_1)$, and $\mathrm{pet}(v, v + s_2)$. Crucially, unlike on a 3-regular tree (where the 6 distance-2 neighbors of $v$ have no edges between them), on $\mathbb{Z}^2$ the two vertices within each petal $\mathrm{pet}(v, v+s) = \{v + s - s',\, v + s - s''\}$ differ by $(s'' - s') \in \mathrm{star}(S)$ (forming three triangles with $v$), AND each vertex in $\mathrm{pet}(v, v+s)$ is star-adjacent to vertices in the other two petals, forming a **6-cycle** in the star-adjacency graph on $\mathrm{star}(\mathcal{S}_0)$ ($12$ directed edges among the $6$ vertices of $\mathrm{star}(\mathcal{S}_0)$).

### 3.3 The Explicit 2-Round Isolated-Doubleton Grouped Local Vertex Cover

Let $\Gamma$ be an abelian group ($\Gamma = \mathbb{Z}^2$, $\mathbb{Z}$, or $\mathbb{F}_p$) equipped with a 3-element step set $S = \{s_0, s_1, s_2\}$ and a source weight function $R: \Gamma \to \{0, 1, \dots, d\}$. We define our **2-round isolated-doubleton grouped local vertex cover** $(U_2, S_2)$ in three deterministic local stages:

- **Round 0 (Star-Isolated Doubleton Initialization).** Eliminate a source $v \in \Gamma$ and cover all three of its incident target rows $v + S$ ($\mathrm{cov}_0(v) = 1$) if and only if either $R(v) \ge 3$, OR $R(v) = 2$ and at least one star neighbor $v + d$ ($d \in \mathrm{star}(S)$) has $R(v + d) \ge 2$:
  $$\mathrm{cov}_0(v) := \mathbf{1}_{\{R(v) \ge 3\}} + \mathbf{1}_{\{R(v) = 2 \text{ and } \exists d \in \mathrm{star}(S),\, R(v + d) \ge 2\}}. \tag{3.5}$$
  A target row $w \in \Gamma$ remains **uncovered** after Round 0 ($U_0(w) = 1$) if and only if none of its three incident sources $w - s$ ($s \in S$) has $\mathrm{cov}_0(w - s) = 1$:
  $$U_0(w) := \prod_{s \in S} \bigl(1 - \mathrm{cov}_0(w - s)\bigr) = \prod_{s \in S} Z(w - s), \tag{3.6}$$
  where $Z(u) := 1 - \mathrm{cov}_0(u) = \mathbf{1}_{\{R(u) \le 1\}} + \mathbf{1}_{\{R(u) = 2 \text{ and } \forall d \in \mathrm{star}(S),\, R(u+d) \le 1\}}$.
  Note the fundamental structural consequence of (3.5)–(3.6): for any finite subset $A \subset \Gamma$, if $I = \{u \in A : R(u) = 2 \text{ and } Z(u) = 1\}$ is the subset of surviving doubletons in $A$, then **$I$ must be an independent set in the star graph on $\Gamma$** (no two vertices of $I$ can differ by an element of $\mathrm{star}(S)$), and every star neighbor $u + d$ ($u \in I, d \in \mathrm{star}(S)$) must satisfy $R(u + d) \le 1$!

- **Round 1 (Singleton Degree-1 Peeling).** For each source $v \in \Gamma$, let $u_0(v) := \sum_{s \in S} U_0(v + s) \in \{0, 1, 2, 3\}$ be the number of target rows of $v$ left uncovered by Round 0. Any singleton source ($R(v) = 1$) with $u_0(v) \le 1$ can be removed from the source cover in exchange for covering its at most $1$ uncovered target row without increasing the cover size. Thus the surviving Round-1 source indicator is
  $$S_1(v) := \mathbf{1}_{\{R(v) = 1 \text{ and } u_0(v) \ge 2\}} + \mathbf{1}_{\{R(v) = 2 \text{ and } \mathrm{cov}_0(v) = 0\}}, \tag{3.7}$$
  and the Round-1 uncovered target-row indicator is
  $$U_1(w) := U_0(w) \prod_{s \in S} \mathbf{1}_{\{R(w - s) = 0 \text{ or } S_1(w - s) = 1\}}. \tag{3.8}$$

- **Round 2 (Grouped Peeling of Surviving Sources).** For each source $v \in \Gamma$, let $u_1(v) := \sum_{s \in S} U_1(v + s) \in \{0, 1, 2, 3\}$ be the number of target rows of $v$ remaining uncovered after Round 1. Define the **Round-2 peeled source set**
  $$P_2 := \bigl\{v \in \Gamma : S_1(v) = 1 \text{ and } u_1(v) \le R(v)\bigr\}, \tag{3.9}$$
  and set the final Round-2 source and target indicators to be
  $$S_2(v) := S_1(v)\bigl(1 - \mathbf{1}_{\{v \in P_2\}}\bigr), \qquad U_2(w) := U_1(w) \prod_{s \in S} \bigl(1 - \mathbf{1}_{\{w - s \in P_2\}}\bigr). \tag{3.10}$$

**Proposition 3.1 (Pointwise Validity and Exact Grouped-Peeling Identity).** *For every abelian group $\Gamma$, every 3-element step set $S \subset \Gamma$, and every weight configuration $R: \Gamma \to \{0, 1, \dots, d\}$:*
1. *Both $(U_1, S_1)$ and $(U_2, S_2)$ satisfy the vertex-cover condition (2.3) at every edge $(v, v + s)$.*
2. *On any finite periodic quotient $\Gamma = \mathbb{Z}_p$ (or in expectation under any translation-invariant measure on $\Gamma$), the total cover cost of $(U_2, S_2)$ satisfies the exact identity*
   $$\sum_{w} \bigl(1 - U_2(w)\bigr) + \sum_{v} R(v) S_2(v) = \sum_{w} \bigl(1 - U_1(w)\bigr) + \sum_{v} R(v) S_1(v) - \sum_{v} \Delta_{\mathrm{clean}}(v) - \sum_{w} \Delta_{\mathrm{overlap}}(w), \tag{3.11}$$
   *where the **clean source-deficit saving** $\Delta_{\mathrm{clean}}(v) \ge 0$ and the **shared-row overlap saving** $\Delta_{\mathrm{overlap}}(w) \ge 0$ are given pointwise by*
   $$\Delta_{\mathrm{clean}}(v) := \mathbf{1}_{\{v \in P_2\}}\bigl(R(v) - u_1(v)\bigr) \ge 0, \qquad \Delta_{\mathrm{overlap}}(w) := U_1(w) \max\bigl(0,\, m_2(w) - 1\bigr) \ge 0, \tag{3.12}$$
   *with $m_2(w) := \sum_{s \in S} \mathbf{1}_{\{w - s \in P_2\}} \in \{0, 1, 2, 3\}$ denoting the number of peeled sources in $P_2$ incident to target row $w$.*

*Proof.* (1) Suppose $R(v) \ge 1$ and $S_1(v) = 0$. If $\mathrm{cov}_0(v) = 1$, then $U_1(v + s) \le U_0(v + s) = 0$ for all $s \in S$ by (3.6). If $\mathrm{cov}_0(v) = 0$, then since $R(v) \ge 1$ and $S_1(v) = 0$, (3.7) forces $R(v) = 1$, and (3.8) directly sets $U_1(v + s) = 0$ for all $s \in S$. Thus $(U_1, S_1)$ is a valid vertex cover. For $(U_2, S_2)$, if $R(v) \ge 1$ and $S_2(v) = 0$, then either $S_1(v) = 0$ (so $U_2(v + s) \le U_1(v + s) = 0$ for all $s \in S$) or $v \in P_2$, in which case (3.10) sets $U_2(v + s) = 0$ for all $s \in S$.

(2) By (3.10), removing each $v \in P_2$ from $S_1$ decreases the source cost $\sum_v R(v) S_1(v)$ by $\sum_{v \in P_2} R(v)$. Simultaneously, a target row $w$ switches from $U_1(w) = 1$ to $U_2(w) = 0$ if and only if $U_1(w) = 1$ and $m_2(w) \ge 1$. For every $w$ with $U_1(w) = 1$, we have the elementary integer identity
$$\mathbf{1}_{\{m_2(w) \ge 1\}} = m_2(w) - \max\bigl(0,\, m_2(w) - 1\bigr). \tag{3.13}$$
Summing $U_1(w)\mathbf{1}_{\{m_2(w) \ge 1\}}$ over $w$ and interchanging the double sum $\sum_w U_1(w) m_2(w) = \sum_{v \in P_2} \sum_{s \in S} U_1(v + s) = \sum_{v \in P_2} u_1(v)$ gives
$$\sum_{w} \bigl(U_1(w) - U_2(w)\bigr) = \sum_{v \in P_2} u_1(v) - \sum_{w} U_1(w)\max\bigl(0,\, m_2(w) - 1\bigr). \tag{3.14}$$
Subtracting $\sum_{v \in P_2} R(v)$ from (3.14) yields (3.11)–(3.12). Finally, $\Delta_{\mathrm{clean}}(v) \ge 0$ holds by definition of $P_2$ ($u_1(v) \le R(v)$), and $\Delta_{\mathrm{overlap}}(w) \ge 0$ is immediate. $\square$

---

## 4. Exact Integer Polynomial Compilation on $\mathbb{Z}^2$ and Resonant Classification

Because $\Delta_{\mathrm{clean}}(v) \ge 0$ and $\Delta_{\mathrm{overlap}}(w) \ge 0$ are non-negative pointwise, any non-negative lower bounds $\Delta_{\mathrm{clean}}^{\mathrm{sub}}(v) \le \Delta_{\mathrm{clean}}(v)$ and $\Delta_{\mathrm{overlap}}^{\mathrm{sub}}(w) \le \Delta_{\mathrm{overlap}}(w)$ yield a rigorous upper bound on the asymptotic line-cover density:
$$\gamma_3(S, d) \le c_2^{\mathrm{UB}}(S, d) := 2\,\mathbb{E}_{R_d}\Bigl[1 - U_1(0) + R(0) S_1(0) - \Delta_{\mathrm{clean}}^{\mathrm{sub}}(0) - \Delta_{\mathrm{overlap}}^{\mathrm{sub}}(0)\Bigr]. \tag{4.1}$$

### 4.1 Explicit Lower-Bound Events $\Delta_{\mathrm{clean}}^{\mathrm{sub}}(0)$ and $\Delta_{\mathrm{overlap}}^{\mathrm{sub}}(0)$

We define $\Delta_{\mathrm{clean}}^{\mathrm{sub}}(0) \le \Delta_{\mathrm{clean}}(0)$ and $\Delta_{\mathrm{overlap}}^{\mathrm{sub}}(0) \le \Delta_{\mathrm{overlap}}(0)$ by restricting to clean, disjoint local configurations on $\Omega_{12} := \Omega_3 \cup \partial\Omega_9$, where $\Omega_3 := -S = \{-s_0, -s_1, -s_2\}$ are the 3 sources incident to target row $w = 0$, and $\partial\Omega_9 := (\Omega_3 + \mathrm{star}(S)) \setminus \Omega_3$ are the 9 boundary petal sources of $\Omega_3$:

1. **Restricted Clean Deficit $\Delta_{\mathrm{clean}}^{\mathrm{sub}}(0)$:** We count $\Delta_{\mathrm{clean}}^{\mathrm{sub}}(0) = 1 \le \Delta_{\mathrm{clean}}(0)$ in two disjoint cases where $S_1(0) = 1$ and $u_1(0) \le R(0) - 1$:
   - *Isolated doubleton at $0$ ($R(0) = 2$ and $R(u) \in \{0, 1\}$ for all $u \in \mathrm{star}(S)$):* Here $U_0(s) = 1$ for all $s \in S$. We require that at least $2$ of the $3$ petals $\mathrm{pet}(0, s)$ ($s \in S$) contain a singleton $u$ ($R(u) = 1$) that is eliminated in Round 1 ($S_1(u) = 0$, i.e., both outer rows $w_2 \ne s$ of $u$ have $U_0(w_2) = 0$), which forces $u_1(0) \le 1 = R(0) - 1$.
   - *Surviving singleton at $0$ ($R(0) = 1$):* We require $u_0(0) \ge 2$ and $u_1(0) = 0$ (all uncovered Round-0 rows of $0$ are covered in Round 1 by eliminated singletons $u \in \mathrm{star}(S)$ with $R(u) = 1, S_1(u) = 0$), restricted to star configurations with at most one ambiguous isolated doubleton candidate $u \in \mathrm{star}(S)$ on any covered petal.

2. **Restricted Shared-Row Overlap $\Delta_{\mathrm{overlap}}^{\mathrm{sub}}(0)$:** When $U_1(0) = 1$, we decompose $\max(0, m_2(0) - 1)$ across the $3$ unordered pairs $\{v_a, v_b\} \subset \Omega_3$ (with third source $v_c$):
   - Note the exact pointwise identity on $\{0, 1\}^3$: if we assign weight $1$ to each pair $\{v_a, v_b\} \subseteq P_2 \cap \Omega_3$ when $R(v_c) = 0$, and weight $\frac{2}{3}$ to each pair $\{v_a, v_b\} \subseteq P_2 \cap \Omega_3$ when $R(v_c) = 1$, then the sum of weights over all pairs in $P_2 \cap \Omega_3$ is $1 \le \max(0, 2-1) = 1$ when $|P_2 \cap \Omega_3| = 2$, and $3 \times \frac{2}{3} = 2 = \max(0, 3-1)$ when $|P_2 \cap \Omega_3| = 3$!
   - For each ordered triple $(v_a, v_b, v_c)$ of $\Omega_3$, we include:
     - **Event $\mathcal{B}(v_a, v_b, v_c)$ ($R(v_a) = 1, R(v_b) = 2, R(v_c) \in \{0, 1\}$):** All 4 boundary neighbors $b_{v_b}$ of $v_b$ have $R \in \{0, 1\}$ (so $\mathrm{cov}_0(v_b) = 0$ and both outer petals of $v_b$ have $U_0 = 1$), at least one of the first two $R=1$ candidates in $b_{v_b}$ (ordered with the vertex $u_{\mathrm{bc}}$ shared between $v_b$ and $v_c$ placed last) has $S_1(u) = 0$ (so $u_1(v_b) \le 2 \implies v_b \in P_2$), and $v_a$ has exactly one $U_0 = 1$ outer petal (killed in Round 1 by an $R=1, S_1=0$ neighbor, so $u_1(v_a) = 1 \implies v_a \in P_2$). When $R(v_c) = 1$, we additionally require both private boundary neighbors $b_{v_c}^{\mathrm{priv}}$ of $v_c$ to have $R \le 1$ (guaranteeing $U_0 = 1$ on the petal of $v_c$ containing $u_{\mathrm{bc}}$, hence $S_1(v_c) = 1$ and $U_1(0) = 1$) and exclude $u_{\mathrm{bc}}$ from the Round-1 killers of $v_a, v_b$.
     - **Event $\mathcal{A}(\{v_a, v_b\}, v_c)$ ($R(v_a) = R(v_b) = 1, R(v_c) \in \{0, 1\}$):** Both $v_a$ and $v_b$ have exactly one $U_0 = 1$ outer petal, each killed in Round 1 by an $R=1, S_1=0$ boundary neighbor (with at most $2$ ambiguous $R=2$ boundary vertices in the $7$-vertex union $b_7 = b_{v_b} \cup b_{v_a}$), and the same $R(v_c) \in \{0, 1\}$ condition as above.

### 4.2 Exact Star-Independent-Set Polynomial Compilation

Let $p_0 = \mathbb{P}(R_d = 0)$, $o = \mathbb{P}(R_d = 1)$, $d_2 = \mathbb{P}(R_d = 2)$, $t_3 = \mathbb{P}(R_d \ge 3) = 1 - p_0 - o - d_2$, and $q = \mathbb{P}(R_d \le 1) = p_0 + o$. Fix an inner vertex set $V_{\mathrm{in}} \subset \Gamma$ on which the configuration $R\big|_{V_{\mathrm{in}}}$ is conditioned. For any subset of outer vertices $A \subset \Gamma \setminus V_{\mathrm{in}}$ and any subset of outer vertices $E \subset \Gamma \setminus V_{\mathrm{in}}$ forced to satisfy $R \le 1$, consider the joint event
$$\mathcal{E}(A, E) := \Bigl\{\forall z \in A,\, Z(z) = 1\Bigr\} \cap \Bigl\{\forall z \in E,\, R(z) \le 1\Bigr\}. \tag{4.2}$$

**Lemma 4.1 (Exact Star-Independent-Set Formula for Outer Expectations).** *Suppose that for every $z \in A$, all star neighbors of $z$ in $V_{\mathrm{in}}$ have already been conditioned in $R\big|_{V_{\mathrm{in}}}$, and let $F_{\mathrm{in}} := \{z \in A : \exists u \in V_{\mathrm{in}} \text{ with } R(u) \ge 2 \text{ and } z - u \in \mathrm{star}(S)\}$. Set $C := A \setminus (E \cup F_{\mathrm{in}})$. Then under i.i.d. weights $R(z) \sim R_d$ on $\Gamma \setminus V_{\mathrm{in}}$, the conditional probability of $\mathcal{E}(A, E)$ is given by the exact polynomial*
$$\mathbb{P}\bigl(\mathcal{E}(A, E) \;\big|\; R\big|_{V_{\mathrm{in}}}\bigr) = \sum_{\substack{I \subseteq C \\ I \text{ star-indep.}}} d_2^{|I|} \, q^{\bigl|(E \,\cup\, A \,\cup\, (\mathrm{nb}(I) \setminus V_{\mathrm{in}}))\bigr| - |I|}, \tag{4.3}$$
*where $I \subseteq C$ ranges over all subsets of $C$ that are independent sets in the star graph ($z_1 - z_2 \notin \mathrm{star}(S)$ for all $z_1, z_2 \in I$) and $\mathrm{nb}(I) := \bigcup_{z \in I} (z + \mathrm{star}(S))$.*

*Proof.* For each $z \in A$, $Z(z) = 1$ holds if and only if either $R(z) \le 1$ or ($R(z) = 2$ and $R(z + d) \le 1$ for all $d \in \mathrm{star}(S)$). Expanding $\prod_{z \in A} Z(z)$ according to the subset $I = \{z \in A : R(z) = 2 \text{ and } Z(z) = 1\} \subseteq A$ of surviving doubletons in $A$:
- If $I \cap (E \cup F_{\mathrm{in}}) \ne \emptyset$, the event is empty (since $z \in E \implies R(z) \le 1$, and $z \in F_{\mathrm{in}} \implies z$ has a star neighbor in $V_{\mathrm{in}}$ with $R \ge 2$, forcing $\mathrm{cov}_0(z) = 1$ and $Z(z) = 0$). Thus $I \subseteq C$.
- If $I$ contains two star-adjacent vertices $z_1, z_2 \in I$ ($z_1 - z_2 \in \mathrm{star}(S)$), then $R(z_1) = R(z_2) = 2$ forces $\mathrm{cov}_0(z_1) = \mathrm{cov}_0(z_2) = 1$, so the event is again empty. Thus $I$ must be an independent set in the star graph.
- For each star-independent subset $I \subseteq C$, the vertices $z \in I$ have $R(z) = 2$ (probability $d_2^{|I|}$), their inner star neighbors $\mathrm{nb}(I) \cap V_{\mathrm{in}}$ already satisfy $R \le 1$ (since $I \cap F_{\mathrm{in}} = \emptyset$), and the outer vertices forced to satisfy $R \le 1$ are precisely $(E \cup (A \setminus I)) \cup (\mathrm{nb}(I) \setminus V_{\mathrm{in}})$. Since $I \subseteq C = A \setminus E$ and $I \cap \mathrm{nb}(I) = \emptyset$, the set $I$ is disjoint from $E \cup (\mathrm{nb}(I) \setminus V_{\mathrm{in}})$ and contained in $A$, so the number of outer vertices forced to have $R \le 1$ is $|E \cup A \cup (\mathrm{nb}(I) \setminus V_{\mathrm{in}})| - |I|$, each occurring independently with probability $q = p_0 + o$. Summing over all star-independent $I \subseteq C$ yields (4.3). $\square$

Applying Lemma 4.1 via inclusion-exclusion over the petal row products in $1 - U_1(0)$, $S_1(0)$, $\Delta_{\mathrm{clean}}^{\mathrm{sub}}(0)$, and $\Delta_{\mathrm{overlap}}^{\mathrm{sub}}(0)$ compiles $3 \cdot c_2^{\mathrm{UB}}(S, d)$ into an **exact polynomial with integer coefficients**:
$$3 \cdot c_2^{\mathrm{UB}}(S, d) = \sum_{(e_0, e_1, e_2, e_3, e_q)} C_{e_0, e_1, e_2, e_3, e_q}(S)\, p_0^{e_0} o^{e_1} d_2^{e_2} t_3^{e_3} q^{e_q}, \qquad C_{e_0, e_1, e_2, e_3, e_q}(S) \in \mathbb{Z}. \tag{4.4}$$

### 4.3 Resonant Step-Set Classification on $\Omega_{48} \subset \mathbb{Z}^2$

Let $\Omega_{48} \subset \mathbb{Z}^2$ be the union of all 2D lattice vertices ever queried by $(U_1, S_1)$, $\Delta_{\mathrm{clean}}^{\mathrm{sub}}$, and $\Delta_{\mathrm{overlap}}^{\mathrm{sub}}$ across all 6 permutations of $\Omega_3 = \{(0,0), (-1,0), (0,-1)\}$:
$$\Omega_{48} = \bigcup_{v \in \Omega_{12}(\mathcal{S}_0)} \bigl(v + (\{(0,0)\} \cup \mathrm{star}(\mathcal{S}_0)) + (\{(0,0)\} \cup \mathrm{star}(\mathcal{S}_0))\bigr), \qquad |\Omega_{48}| = 48. \tag{4.5}$$

**Lemma 4.2 (Exact Classification of Resonant 3-Translate Step Sets).** *Let $S = (0, a, a + b)$ be a primitive canonical 3-translate step set ($1 \le a \le b$, $\gcd(a, b) = 1$). The linear homomorphism $\pi_{a, b}(i, j) = i a + j(a + b)$ fails to be injective on $\Omega_{48} \subset \mathbb{Z}^2$ if and only if $S$ belongs to the 9-element resonant set*
$$\mathcal{R}_9 := \bigl\{(0,1,2),\, (0,1,3),\, (0,1,4),\, (0,1,5),\, (0,1,6),\, (0,1,7),\, (0,2,5),\, (0,2,7),\, (0,3,7)\bigr\}. \tag{4.6}$$
*More specifically, across the nested sub-neighborhoods of $\Omega_{48}$:*
- *On $\mathrm{supp}(S_1) = \{(0,0)\} \cup \mathrm{star}(\mathcal{S}_0) \cup \mathrm{outer}_{12}$ ($19$ vertices), $\pi_{a, b}$ fails to be injective iff $S \in \{(0,1,2), (0,1,3), (0,1,4)\}$ ($3$ sets).*
- *On $\mathrm{supp}(U_1)$ ($27$ vertices), $\pi_{a, b}$ fails to be injective iff $S \in \{(0,1,2), (0,1,3), (0,1,4), (0,1,5), (0,2,5)\}$ ($5$ sets).*
- *On $\mathrm{supp}(\Delta_{\mathrm{clean}}^{\mathrm{sub}})$ ($37$ vertices), $\pi_{a, b}$ fails to be injective iff $S \in \{(0,1,2), (0,1,3), (0,1,4), (0,1,5), (0,1,6), (0,2,5)\}$ ($6$ sets).*
- *For every $S = (0, a, a+b) \notin \mathcal{R}_9$, the polynomial $C(S)$ in (4.4) is **identically equal** to the universal $\mathbb{Z}^2$ polynomial $C(\mathbb{Z}^2)$.*

*Proof.* Two distinct lattice points $(i_1, j_1), (i_2, j_2) \in \Omega_{48}$ have $\pi_{a, b}(i_1, j_1) = \pi_{a, b}(i_2, j_2)$ if and only if $\Delta i \cdot a + \Delta j \cdot (a + b) = 0$, where $(\Delta i, \Delta j) = (i_1 - i_2, j_1 - j_2) \ne (0, 0)$. Dividing by $g = \gcd(|\Delta i|, |\Delta j|)$ and choosing the sign so that $\Delta i' = \Delta i / g > 0$, coprimality $\gcd(a, a + b) = \gcd(a, b) = 1$ with $1 \le a \le b$ forces $a = -\Delta j'$ and $a + b = \Delta i'$ (so $b = \Delta i' + \Delta j'$), with $1 \le -\Delta j' \le \Delta i' + \Delta j'$. Since $\Omega_{48}$ has $\max_{(i_1,j_1),(i_2,j_2) \in \Omega_{48}} |\Delta i| = 7$, exhausting all $\binom{48}{2} = 1128$ pairs in $\Omega_{48}$ yields precisely the 9 primitive step sets in (4.6) (verified in `0.002s` by `verify_nonconsecutive_translates.py`). Finally, whenever $S \notin \mathcal{R}_9$, $\pi_{a, b}$ is injective on $\Omega_{48}$ (which already contains the star-neighborhood of every queried vertex), so $\pi_{a, b}$ is a local graph isomorphism on the support of every term in (4.1), establishing $C(S) = C(\mathbb{Z}^2)$. $\square$

### 4.4 Exact Rational Bounds on $\mathbb{Z}^2$ and the 6 Span-$\{5, 6, 7\}$ Resonant Step Sets

On $\mathbb{Z}^2$, our bitmask polynomial compiler (`verify_nonconsecutive_translates.py`) compiles the exact 2,569-monomial integer polynomial $3 \cdot c_2^{\mathrm{UB}}(\mathbb{Z}^2, d)$ in `0.36s`. Evaluating (4.4) in exact rational arithmetic for each degree $d \in \{2, 3, 4, 5, 6, 7, 8\}$ and bounding all degrees $d \ge 9$ simultaneously via the alternating-series interval enclosure
$$p_0 \in [a_9, a_{10}], \qquad o \in [a_9, a_8], \qquad d_2 \in \left[\tfrac{1}{2}a_7, \tfrac{1}{2}a_8\right], \qquad q \in [2a_9, a_{10} + a_8], \qquad t_3 \in \left[1 - q_{\max} - d_{2,\max},\, 1 - q_{\min} - d_{2,\min}\right] \tag{4.7}$$
(replacing each positive monomial coefficient by its upper interval endpoint and each negative monomial coefficient by its lower interval endpoint) yields **Theorem 4.3**:

**Theorem 4.3 (Universal Bound for Non-Resonant and Span-$\{5,6,7\}$ Resonant 3-Translate Families).** *For every non-resonant primitive step set $S = (0, a, a+b) \notin \mathcal{R}_9$ (i.e., on the universal lattice $\mathbb{Z}^2$) and for each of the 6 resonant step sets of span $W \in \{5, 6, 7\}$, the 2-round isolated-doubleton cover $(U_2, S_2)$ certifies $c_2^{\mathrm{UB}}(S, d) < \frac{9}{5} = 1.80$ for all $d \ge 2$:*

| Step Set $S$ | $d = 2$ | $d = 3$ | $d = 4$ (Worst Case) | $d = 5$ | $d = 6$ | $d = 7$ | $d = 8$ | All $d \ge 9$ (Interval) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$\mathbb{Z}^2$ (All $S \notin \mathcal{R}_9$)** | $1.73437500$ | $1.78288083$ | **$1.79921870$** | $1.79428352$ | $1.79548778$ | $1.79529572$ | $1.79531857$ | $1.79555942$ |
| **$S = (0, 1, 5)$** | $1.73437500$ | $1.78264155$ | **$1.79835551$** | $1.79348436$ | $1.79464933$ | $1.79446621$ | $1.79448697$ | $1.79472512$ |
| **$S = (0, 2, 5)$** | $1.73437500$ | $1.78252432$ | **$1.79805849$** | $1.79320911$ | $1.79436426$ | $1.79418276$ | $1.79420319$ | $1.79443947$ |
| **$S = (0, 1, 6)$** | $1.73437500$ | $1.78288083$ | **$1.79915868$** | $1.79423180$ | $1.79543211$ | $1.79524088$ | $1.79526356$ | $1.79550469$ |
| **$S = (0, 1, 7)$** | $1.73437500$ | $1.78288083$ | **$1.79921755$** | $1.79428279$ | $1.79548692$ | $1.79529489$ | $1.79531773$ | $1.79555859$ |
| **$S = (0, 2, 7)$** | $1.73437500$ | $1.78288083$ | **$1.79921587$** | $1.79428144$ | $1.79548543$ | $1.79529342$ | $1.79531626$ | $1.79555712$ |
| **$S = (0, 3, 7)$** | $1.73437500$ | $1.78288083$ | **$1.79921484$** | $1.79428056$ | $1.79548450$ | $1.79529251$ | $1.79531535$ | $1.79555622$ |

*In particular, at the critical quartic degree $d = 4$ on $\mathbb{Z}^2$, the exact rational value is*
$$c_2^{\mathrm{UB}}(\mathbb{Z}^2, 4) = \frac{298558878835918682348830616036741983367}{165938070412604949627456920525331234816} \approx 1.7992187001 < \frac{9}{5} = 1.80, \tag{4.8}$$
*decomposed into the Round-1 baseline $c_1(\mathbb{Z}^2, 4) \approx 1.81268866$, the clean deficit saving $-2\mathbb{E}[\Delta_{\mathrm{clean}}^{\mathrm{sub}}] \approx -0.01075960$, and the shared-row overlap saving $-2\mathbb{E}[\Delta_{\mathrm{overlap}}^{\mathrm{sub}}] \approx -0.00271036$.*

---

## 5. Reachable-Mask Primal Bellman Markov Chains for Small-Span Resonant Sets and 4-Translate Extensions

It remains to resolve the 3 small-span resonant step sets $S \in \{(0, 1, 2), (0, 1, 3), (0, 1, 4)\}$ ($W \in \{2, 3, 4\}$), where $\mathrm{supp}(S_1)$ undergoes self-intersection in 1D. We formulate a **reachable-mask primal Bellman Markov chain** that is simpler and more compact than the dual posterior-law transfer operator of `no_three_in_line_10` v3.

### 5.1 Reachable-Mask Primal Bellman Recursion and Potential Certificates

Let $S = (0 = s_0 < s_1 < \dots < s_{k-1} = W)$ be a $k$-element step set of span $W$ on a contiguous block of sources $j \in \{0, 1, \dots, L-1\}$ with clipped source weights $\tilde{r}_j = \min(R(j), k) \in \{0, 1, \dots, k\}$. Any subset of eliminated sources $E \subseteq \{0, \dots, L-1\}$ defines a valid vertex cover $V_{\mathrm{keep}} = \{0, \dots, L-1\} \setminus E$ and $U_{\mathrm{cov}} = \bigcup_{j \in E} (j + S)$ of cost $\sum_{j \notin E} \tilde{r}_j + |U_{\mathrm{cov}}|$.

Scanning $j = 0, 1, \dots, L-1$ from left to right, let $m_j \in \{0, 1\}^W$ be the $W$-bit binary mask whose bit $b_t(m_j)$ ($0 \le t < W$) equals $1$ if and only if target row $j + t$ has already been covered by some eliminated source $i < j$. Define the elimination mask $B_{\mathrm{elim}} := \sum_{i=1}^{k-1} 2^{s_i - 1}$. At step $j$, given mask $m_j$:
- **Keep source $j$ ($e_j = 0$):** Target row $j$ is retired with indicator $b_0(m_j) \in \{0, 1\}$, we pay step cost $b_0(m_j) + \tilde{r}_j$, and the mask transitions to $m_{\mathrm{keep}}(m_j) := m_j \gg 1$.
- **Eliminate source $j$ ($e_j = 1$):** Target row $j = j + s_0$ is covered (paying step cost $1$), target rows $j + s_1, \dots, j + s_{k-1}$ are marked as covered, and the mask transitions to $m_{\mathrm{elim}}(m_j) := (m_j \gg 1) \mid B_{\mathrm{elim}}$.

Let $\mathcal{M}_S \subseteq \{0, 1\}^W$ be the finite set of masks reachable from $m_0 = 0$ under $m_{\mathrm{keep}}$ and $m_{\mathrm{elim}}$. Note that because $m_{\mathrm{elim}}$ simultaneously sets bit $W - 1$ and bits $s_i - 1$, $|\mathcal{M}_S|$ is strictly smaller than $2^W$:
- For $S = (0, 1, 2)$ ($W = 2$): $|\mathcal{M}_S| = 3$ masks $\{0, 1, 3\}$.
- For $S = (0, 1, 3)$ ($W = 3$): $|\mathcal{M}_S| = 6$ masks $\{0, 1, 2, 3, 5, 7\}$.
- For $S = (0, 1, 4)$ ($W = 4$): $|\mathcal{M}_S| = 12$ masks (since bit $3 = 1 \implies$ bit $0 = 1$).
- For $k = 4$, $S = (0, 1, 2, 4)$ ($W = 4$): $|\mathcal{M}_S| = 8$ masks; for $S = (0, 1, 3, 4)$ ($W = 4$): $|\mathcal{M}_S| = 7$ masks.

Let $V_j: \mathcal{M}_S \to \mathbb{Z}_{\ge 0}$ be the minimum cumulative step cost to reach mask $m \in \mathcal{M}_S$ at step $j$, initialized at $V_0 \equiv 0$. The Bellman transition $V_{j+1} = T_{\tilde{r}_j}(V_j)$ is
$$V_{j+1}(m') = \min\Bigl(\min_{m : m_{\mathrm{keep}}(m) = m'} \bigl(V_j(m) + b_0(m) + \tilde{r}_j\bigr),\; \min_{m : m_{\mathrm{elim}}(m) = m'} \bigl(V_j(m) + 1\bigr)\Bigr). \tag{5.1}$$
Subtracting the base value $V_{j+1}(0)$ defines the relative profile $u_j(m) := V_j(m) - V_j(0)$ on a finite reachable state space $\Sigma_S \subset \mathbb{Z}^{\mathcal{M}_S}$ with deterministic step increment $\Delta(u, r) := (T_r(u))(0)$ and next state $\tau(u, r) := T_r(u) - \Delta(u, r)\mathbf{1}$.

**Proposition 5.1 (Non-Asymptotic Potential Bound and Stochastic Dominance for $d \ge 7$).**
1. *For any rational potential vector $h: \Sigma_S \to \mathbb{Q}$ and any source weight law $p = (p_0, \dots, p_k)$, let*
   $$\lambda(h; p) := \max_{u \in \Sigma_S} \left(\sum_{r=0}^k p_r \bigl(\Delta(u, r) + h(\tau(u, r))\bigr) - h(u)\right). \tag{5.2}$$
   *Then for every finite block length $L \ge 1$, the expected minimum vertex cover cost on $\{0, \dots, L-1\}$ satisfies $\frac{1}{L}\mathbb{E}[\mathrm{Cost}_L] \le \lambda(h; p) + \frac{\mathrm{osc}(h) + W}{L}$, and hence $\gamma_k(S, d) \le 2\,\lambda(h; p)$ across all windows $n \ge N$.*
2. *For $k = 3$ and all degrees $d \ge 7$, the clipped fixed-point law $\tilde{R}_d = \min(R_d, 3)$ is stochastically dominated in the usual stochastic order ($\le_{\mathrm{st}}$) by the fixed rational law*
   $$Z := \left(\frac{1854}{5040} - \frac{1}{5040},\; \frac{1855}{5040} - \frac{1}{720},\; \frac{915}{5040} - \frac{1}{240},\; \frac{445}{5040}\right) = \left(\frac{1853}{5040},\; \frac{1848}{5040},\; \frac{894}{5040},\; \frac{445}{5040}\right). \tag{5.3}$$
   *Since the minimum vertex cover cost is monotonically non-decreasing in $(\tilde{r}_0, \dots, \tilde{r}_{L-1})$, $\gamma_3(S, d) \le 2\,\lambda(h; Z)$ for all $d \ge 7$.*

*Proof.* (1) For every $j$, $\mathbb{E}[\Delta(u_j, \tilde{r}_j) + h(u_{j+1}) - h(u_j) \mid u_j] \le \lambda(h; p)$. Summing over $j = 0, \dots, L-1$ telescopes $h(u_L) - h(u_0) \ge -\mathrm{osc}(h)$, and adding the terminal mask cost $\mathrm{popcount}(m_L) \le W$ gives $\mathbb{E}[\mathrm{Cost}_L] \le L\lambda(h; p) + \mathrm{osc}(h) + W$. For any fixed finite block length $L \ge 1$ (independent of $p$) and each phase $t \in \{0, \dots, L-1\}$, applying the optimal $L$-step cover to the local block $\{v - t, \dots, v - t + L - 1\}$ at $v \in \mathbb{F}_p$ (and covering the $W$ boundary target rows at the end of each block) defines a valid vertex cover $(U^{(L, t)}(w), S_{\mathrm{keep}}^{(L, t)}(v))$ on $G_p(S)$ whose indicators depend only on the bounded shift neighborhood $A_L = [-L - W, L + W]$ of fixed diameter $2(L + W)$. Applying Lemma 2.1 and (2.6) to each phase $t \in \{0, \dots, L-1\}$ and averaging over $t$ yields $\limsup_{N \to \infty} \sup_{n \ge N} |S_{\mathrm{pts}}|/n \le 2\lambda(h; p) + \frac{2(\mathrm{osc}(h) + W)}{L}$ for every fixed $L \ge 1$. Since $L \ge 1$ is arbitrary, letting $L \to \infty$ gives $\gamma_k(S, d) \le 2\,\lambda(h; p)$.

(2) By the alternating series theorem for $a_m = \sum_{j=0}^m (-1)^j / j!$, for all $d \ge 7$ we have $p_0(d) = a_d \ge a_7 = \frac{1854}{5040} > \frac{1853}{5040} = Z_0$, $p_0(d) + p_1(d) = a_d + a_{d-1} \ge a_7 + a_6 - \frac{1}{720} = \frac{3701}{5040} = Z_0 + Z_1$, and $p_0(d) + p_1(d) + p_2(d) = a_d + a_{d-1} + \frac{1}{2}a_{d-2} \ge a_7 + a_6 + \frac{1}{2}a_5 - \frac{1}{720} - \frac{1}{240} = \frac{4595}{5040} = Z_0 + Z_1 + Z_2$. Hence $\mathbb{P}(\tilde{R}_d \le r) \ge \mathbb{P}(Z \le r)$ for all $r \in \{0, 1, 2, 3\}$, so $\tilde{R}_d \le_{\mathrm{st}} Z$. $\square$

### 5.2 Exact Rational Certificates for $(0,1,2), (0,1,3), (0,1,4)$ and 4-Translate Carriers

Running `solve_bellman_chain` in `verify_nonconsecutive_translates.py` constructs $\Sigma_S$, computes the rational potential vector $h: \Sigma_S \to 10^{-9}\mathbb{Z}$, and evaluates the exact rational upper bound $2\,\lambda(h; p)$ via integer arithmetic over the common denominator $5040 \times 10^9$ in `0.62s`:

| Step Set $S$ | $\|\mathcal{M}_S\|$ | $\|\Sigma_S\|$ | $d = 2$ | $d = 3$ | $d = 4$ | $d = 5$ | $d = 6$ | Law $Z$ (All $d \ge 7$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$S = (0, 1, 2)$** | $3$ | $24$ | $1.666667$ | **$1.703704$** | $1.699257$ | $1.700794$ | $1.699738$ | $1.703200$ |
| **$S = (0, 1, 3)$** | $6$ | $356$ | $1.708333$ | $1.741984$ | $1.741544$ | $1.743994$ | $1.742767$ | **$1.746421$** |
| **$S = (0, 1, 4)$** | $12$ | $6272$ | $1.719062$ | $1.756750$ | $1.759450$ | $1.760823$ | $1.759979$ | **$1.763444$** |

Combining Theorem 4.3 with the table above establishes our main result:

**Theorem 5.2 (Main Theorem: Universal Exclusion of All 3-Translate Polynomial Families).** *For every degree bound $D \ge 2$, every 3-element step set $S = \{s_0, s_1, s_2\} \subset \mathbb{Z}$, every sequence of moduli $N \to \infty$ with $P(N) \to \infty$ and $\gcd(s_1 - s_0, s_2 - s_0, P(N)) = 1$, every polynomial $f_N \in \mathbb{Z}[X]$ of degree $d \in \{2, \dots, D\}$ with $G_{\mathrm{geom}}(f_N \bmod P(N)) = S_d$, and every unit step $h_N \in (\mathbb{Z}/N\mathbb{Z})^\times$, every collinear-free subset $S_{\mathrm{pts}} \subseteq \mathcal{U}_{f_N, S, h_N} \cap Q_n(x_0, y_0)$ in any translated square window of side $n \ge N$ satisfies*
$$\limsup_{N \to \infty} \sup_{n \ge N} \sup_{x_0, y_0 \in \mathbb{Z}} \frac{|S_{\mathrm{pts}}|}{n} \le \gamma_3(S, d) \le \mathbf{1.79921870} < \frac{9}{5} = 1.80. \tag{5.4}$$

**Proposition 5.3 (Extension to Non-Consecutive 4-Translate Quadratic Families).** *For $k = 4$ translates and quadratic polynomials ($d = 2$, where $R_2 \in \{0, 2\}$ with $p_0 = p_2 = \frac{1}{2}$), the reachable-mask Bellman Markov chain certifies that for the non-consecutive step sets $S = (0, 1, 2, 4)$ ($8$ masks, $156$ states) and $S = (0, 1, 3, 4)$ ($7$ masks, $168$ states), every collinear-free subset $S_{\mathrm{pts}} \subseteq \mathcal{U}_{f_N, S, h_N} \cap Q_n(x_0, y_0)$ ($n \ge N$) satisfies*
$$\gamma_4\bigl((0, 1, 2, 4),\, 2\bigr) \le \mathbf{1.780822} < 1.80, \qquad \gamma_4\bigl((0, 1, 3, 4),\, 2\bigr) \le \mathbf{1.791267} < 1.80. \tag{5.5}$$

---

## 6. Finite-Prime Verification and Determinant-Verified Collinear-Free Witnesses

The standalone standard-library script `verify_nonconsecutive_translates.py` (total runtime `2.94s`) executes all exact rational certifications in Sections 4–5 and performs live finite-prime checks on explicit modular polynomial translate carriers $\mathcal{U}_{f, S, 1} \subset \mathbb{F}_p^2$ for the symmetric quartic $f(x) = x^4 + x^2 + x \pmod p$:

1. **Finite-Prime Cover and Grouped-Peeling Identity Verification ($p = 4001$):** On $p = 4001$ with $f(x) = x^4 + x^2 + x \pmod{4001}$, the script constructs $G_p(S)$ for $S \in \{(0,1,3), (0,1,4), (0,1,5), (0,2,5), (0,1,7), (0,11,29)\}$, runs the 2-round isolated-doubleton algorithm $(U_2, S_2)$, verifies that $100\%$ of carrier edges are covered (`assert U2[(v + s) % p] == 0`), confirms the exact integer identity $c_2 = c_1 - \Delta_{\mathrm{clean}} - \Delta_{\mathrm{overlap}}$ of Proposition 3.1, and records the physical line-cover capacities $2 c_2 / p$:
   - $S = (0, 1, 3)$: $2 c_1 / p = 1.779555$, $2\Delta_{\mathrm{clean}}/p = 0.014496$, $2\Delta_{\mathrm{overlap}}/p = 0.001500 \implies 2 c_2 / p = \mathbf{1.763559} < 1.80$.
   - $S = (0, 1, 5)$: $2 c_1 / p = 1.809048$, $2\Delta_{\mathrm{clean}}/p = 0.013997$, $2\Delta_{\mathrm{overlap}}/p = 0.009998 \implies 2 c_2 / p = \mathbf{1.785054} < 1.80$.
   - $S = (0, 2, 5)$: $2 c_1 / p = 1.800550$, $2\Delta_{\mathrm{clean}}/p = 0.005999$, $2\Delta_{\mathrm{overlap}}/p = 0.007998 \implies 2 c_2 / p = \mathbf{1.786553} < 1.80$.
   - $S = (0, 1, 7)$: $2 c_1 / p = 1.812047$, $2\Delta_{\mathrm{clean}}/p = 0.011497$, $2\Delta_{\mathrm{overlap}}/p = 0.006498 \implies 2 c_2 / p = \mathbf{1.794051} < 1.80$.
   - $S = (0, 11, 29)$: $2 c_1 / p = 1.806548$, $2\Delta_{\mathrm{clean}}/p = 0.007498$, $2\Delta_{\mathrm{overlap}}/p = 0.005499 \implies 2 c_2 / p = \mathbf{1.793552} < 1.80$.

2. **Determinant-Verified Collinear-Free Finite Witnesses ($p = 53$):** On $p = 53$ with $f(x) = x^4 + x^2 + x \pmod{53}$ and $S \in \{(0, 1, 3), (0, 2, 5), (0, 1, 7)\}$ ($159$ carrier points each), the script constructs maximal collinear-free subsets $S_{\mathrm{pts}} \subset \mathcal{U}_{f, S, 1} \cap [0, 52]^2$ of sizes $49, 51, 49$, verifies via all $\binom{|S_{\mathrm{pts}}|}{3}$ exact $2 \times 2$ determinants $(x_1 - x_0)(y_2 - y_0) - (y_1 - y_0)(x_2 - x_0) \ne 0$ in $\mathbb{Z}$ that no three points are collinear, and confirms the pointwise line-cover bound $|S_{\mathrm{pts}}| \le 2 c_2$ ($49 \le 90$, $51 \le 94$, $49 \le 90$).

---

## References

1. `no_three_in_line_35` v8, *Community Synthesis Map for Structured No-Three-in-Line Families* (Open Cell 16: Non-consecutive vertical polynomial translates).
2. `no_three_in_line_10` v3, *Periodic-Support Capacity Framework and Exclusion of Consecutive Polynomial Translates*.
3. `no_three_in_line_11` v2, *Branch-Orbit Independence, Coordinate Allocation Limits, and Three-Output Rational Families*.
4. M. Leconte, M. Lelarge, and L. Massoulié, *Bipartite graph structures for efficient balancing of heterogeneous loads*, ACM SIGMETRICS (2012).
5. J. Salez, *Weighted matchings on locally tree-like graphs*, Random Structures & Algorithms **43** (2013), 377–397.
