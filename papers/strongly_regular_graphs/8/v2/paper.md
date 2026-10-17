# Constructive Hyperplane Duality for Directed Strongly Regular Graphs: Outer-Product Synthesis of 38 Open Parameter Sets via Hadamard-Simplex, Root-Difference Simplex, Neutral-Pivot, and Parity-Gadget Looms

## Abstract
We establish the constructive converse of the Rank-$(g+1)$ Hyperplane Duality Theorem for directed strongly regular graphs ($\mathrm{DSRG}$s) with $t = \mu$ (and their complements with $t^c = \lambda^c + 1$). Whereas hyperplane duality was introduced in our preceding paper [14] as a polyhedral nonexistence obstruction eliminating $42$ open parameter sets across Ranks $6$ and $7$, we prove here that any rational hyperplane $\alpha \in \mathbb{Q}^{g+1}$ with $\mathbf{1}_{g+1}^T \alpha = \frac{v}{k} = \frac{(g+1)d}{\mu}$ and any bipartite-compatible pair $(S, B)$ of binary slice vectors $S \subseteq H_\alpha$ and dual vectors $B \subseteq \mathcal{B}(S)$ admitting non-negative integer multiplicities $N(z, \beta) \in \mathbb{Z}_{\ge 0}$ on orthogonal pairs ($\beta^T z = 0$) with
$$
\sum_{\substack{z \in S,\, \beta \in B \\ \beta^T z = 0}} N(z, \beta)\, z \beta^T = -d I_{g+1} + \mu \mathbf{1}_{g+1} \alpha^T
$$
directly synthesizes a $\mathrm{DSRG}(cv, cgd, c\mu, c(\mu-d), c\mu)$ of adjacency rank $g+1$ for every integer $c \ge 1$ via the outer-product factorization $A_c = C_c R_c \in \{0,1\}^{cv \times cv}$. We introduce four universal dual-cone architectures: the **Hadamard-Simplex Loom** (dual denominator $D = 2$, coupling four-coordinate balanced Hadamard vectors to tail coordinates), the **Root-Difference Simplex Loom** (dual denominator $D = 1$, coupling head root differences $e_i - e_j$ to tail coordinates) with $\mathbb{Z}_q$-circulant reduction, the **Neutral-Pivot 3-Block Bypass Loom** (dual denominator $D = 1$, bypassing neutral coordinates where $\mu \alpha_j = d$ whenever $n \mid v$), and the **3-Vector Parity-Gadget Decomposition** (dual denominator $D = 2$, absorbing odd column-sum parities via gadgets $z^{(3)} = (z^{(1)} + z^{(2)}) \bmod 2$). Using these four looms, we resolve **38 open catalog $\mathrm{DSRG}$ parameter sets (19 complementary pairs: 17 primitive base pairs and 2 Duval T10 $c = 2$ coclique extensions)** in Hobart and Brouwer's catalog [2] for $v \le 110$ across Ranks $7, 9, 10, 11, 12, 14, 15, 16, 18, 20$, and $24$ that have not been resolved in prior literature [1–18]. Together with [14], this completes the resolution of **100% of all open Rank-7 ($g = 6$) $t = \mu$ parameter sets** in the catalog. All $32$ primary infinite families ($64$ explicit $\mathrm{DSRG}$s, including $38$ newly resolved open catalog entries and $26$ comparison graphs) are verified in under $0.5$ seconds using 100% exact integer arithmetic.

---

## 1. Introduction and Summary of Main Results

A **directed strongly regular graph** with parameters $(v, k, t, \lambda, \mu)$, denoted $\mathrm{DSRG}(v, k, t, \lambda, \mu)$, is a simple directed graph on $v$ vertices (without loops) whose $(0,1)$-adjacency matrix $A \in \{0,1\}^{v \times v}$ has zero diagonal ($\operatorname{diag}(A) = \mathbf{0}_v$) and satisfies Duval's matrix equations [1]:
$$
A J_v = J_v A = k J_v, \qquad A^2 = t I_v + \lambda A + \mu(J_v - I_v - A),
\tag{1}
$$
where $I_v$ is the $v \times v$ identity matrix and $J_v = \mathbf{1}_v \mathbf{1}_v^T$ is the $v \times v$ all-ones matrix. Equivalently, every vertex has out-degree and in-degree $k$, every vertex has $t$ undirected (reciprocal) neighbors, and for any ordered pair of distinct vertices $(x, y)$, the number of directed $2$-step walks $x \to z \to y$ is $\lambda$ if $x \to y$ and $\mu$ otherwise. When $t = k$, $A$ is symmetric and $\mathrm{DSRG}(v, k, k, \lambda, \mu)$ is an undirected strongly regular graph $\mathrm{SRG}(v, k, \lambda, \mu)$ [3]; Duval [1] proved that $0 < t < k$ is necessary for genuine directedness. Taking the directional complement $A^c := J_v - I_v - A$ maps a $\mathrm{DSRG}(v, k, t, \lambda, \mu)$ to a complementary $\mathrm{DSRG}(v, k^c, t^c, \lambda^c, \mu^c)$ with parameters
$$
k^c = v - 1 - k, \qquad t^c = v - 1 - 2k + t, \qquad \lambda^c = v - 2 - 2k + \mu, \qquad \mu^c = v - 2k + \lambda.
\tag{2}
$$

A central boundary family in Hobart and Brouwer's catalog of feasible parameter sets for $v \le 110$ [2] consists of parameter sets with **$t = \mu$** (and their complements, which satisfy $t^c = \lambda^c + 1$). When $t = \mu$, the diagonal term $(t - \mu)I_v$ in Eq. (1) vanishes, and the matrix quadratic simplifies to
$$
A^2 + d A = \mu J_v, \qquad \text{where } d := \mu - \lambda = t - \lambda \ge 1.
\tag{3}
$$
On the orthogonal complement $\mathbf{1}_v^\perp$, $A$ satisfies the minimal polynomial $x(x + d) = 0$, so the eigenvalues of $A$ are $\theta_0 = k$ (multiplicity $1$), $\theta_1 = 0$ (multiplicity $f = v - 1 - g$), and $\theta_2 = -d$ (multiplicity $g := k / d \in \mathbb{Z}_{\ge 1}$), with feasibility identity
$$
k(k + d) = \mu v \quad \Longleftrightarrow \quad \frac{v}{k} = \frac{(g + 1) d}{\mu} \quad \Longleftrightarrow \quad v = \frac{g(g + 1)d^2}{\mu}.
\tag{4}
$$
Because $A$ is diagonalizable over $\mathbb{Q}$ with $1 + g$ non-zero eigenvalues ($k$ of multiplicity $1$ and $-d$ of multiplicity $g$), Klin, Munemasa, Muzychuk, and Zieschang [9] and Jørgensen [10] observed that any $\mathrm{DSRG}(v, gd, \mu, \mu - d, \mu)$ has adjacency rank $\operatorname{rank}(A) = g + 1$.

In our preceding paper [14] (and in concurrent nonexistence work [17]), we developed the **Rank-$(g+1)$ Hyperplane Duality Theorem**: any $\mathrm{DSRG}(v, gd, \mu, \mu - d, \mu)$ forces the existence of a rational vector $\alpha \in \mathbb{Q}^{g+1}$ with $\mathbf{1}_{g+1}^T \alpha = v / k$, a spanning subset $S$ of the binary hyperplane slice
$$
H_\alpha := \bigl\{z \in \{0,1\}^{g+1} \setminus \{\mathbf{0}, \mathbf{1}\} : \alpha^T z = 1\bigr\},
\tag{5}
$$
and a spanning subset $B$ of the dual $\{0,1\}$-polyhedral cone
$$
\mathcal{B}(S) := \bigl\{\beta \in \mathbb{Q}^{g+1} : \mathbf{1}_{g+1}^T \beta = 1,\;\; \beta^T z \in \{0, 1\} \;\;\forall z \in S\bigr\}
\tag{6}
$$
such that the rank-$(g+1)$ matrix $-I_{g+1} + \frac{\mu}{d}\mathbf{1}_{g+1}\alpha^T$ lies in the conic hull of orthogonal outer products $\{z \beta^T : z \in S,\, \beta \in B,\, \beta^T z = 0\}$. In [14], we used Farkas' Lemma on this polyhedral cone to prove unconditional nonexistence for $42$ open catalog parameter sets across Rank $6$ ($g = 5$, all ratios $v / k \notin \{6/5, 3/2, 2, 3, 4, 6\}$) and Rank $7$ ($g = 6$, $v / k \in \{14/3, 14/9\}$).

### 1.1 Turning the Telescope Around: Constructive Outer-Product Synthesis

In this paper, we invert the hyperplane-duality method from a nonexistence filter into an **exact constructive synthesis engine** across arbitrarily high ranks $n = g + 1$. Specifically:

1. **Constructive Converse of Hyperplane Duality (Theorem 2.1) & Structural Obstruction Laws (Proposition 2.2):**
   We prove that if $\alpha \in \mathbb{Q}^n$ ($n = g + 1$) satisfies $\mathbf{1}_n^T \alpha = \frac{n d}{\mu} > 1$, and $(S, B)$ with $S \subseteq H_\alpha$ and $B \subseteq \mathcal{B}(S)$ admits non-negative **integer** multiplicities $N(z, \beta) \in \mathbb{Z}_{\ge 0}$ supported on $\{(z, \beta) \in S \times B : \beta^T z = 0\}$ such that
   $$
   \sum_{\substack{z \in S,\, \beta \in B \\ \beta^T z = 0}} N(z, \beta)\, z \beta^T = -d I_n + \mu \mathbf{1}_n \alpha^T,
   \tag{7}
   $$
   then the sum of multiplicities is automatically $\sum_{z, \beta} N(z, \beta) = v := \frac{g(g+1)d^2}{\mu}$, and for every integer $c \ge 1$, repeating each pair $(z, \beta)$ exactly $c \cdot N(z, \beta)$ times as rows of $C_c \in \{0,1\}^{cv \times n}$ and columns of $R_c^T \in \mathbb{Q}^{cv \times n}$ produces a $(0,1)$-matrix $A_c := C_c R_c \in \{0,1\}^{cv \times cv}$ with zero diagonal that is the adjacency matrix of a $\mathrm{DSRG}(cv, cgd, c\mu, c(\mu - d), c\mu)$ (and $A_c^c := J_{cv} - I_{cv} - A_c$ realizes its complementary $\mathrm{DSRG}$). We also establish two structural laws governing all integer outer-product syntheses (Proposition 2.2): the **Denominator Divisibility Law** ($L \mid D \mu$, where $L \alpha \in \mathbb{Z}^n$ is primitive and $D \beta \in \mathbb{Z}^n$) and the **Diagonal Sign Coverage Law** (every coordinate $j$ with $\mu \alpha_j < d$ must appear with $\beta_j < 0$ in at least one active pair $(z, \beta)$ with $z_j = 1$).

2. **The Hadamard-Simplex Loom ($D = 2$, Section 3) and 100% Resolution of Open Rank-7 $t = \mu$ DSRGs:**
   For $n = 4 + q$ ($g = q + 3$) and $1 \le h \le q$, we introduce the $2$-block hyperplane
   $$
   \alpha = \frac{1}{2h}\Bigl(\underbrace{1, 1, 1, 1}_{4},\; \underbrace{2, 2, \dots, 2}_{q}\Bigr) \in \mathbb{Q}^{4+q}, \qquad \frac{v}{k} = \frac{q + 2}{h},
   \tag{8}
   $$
   on which every binary slice vector $z = (z_{\text{head}}, z_{\text{tail}}) \in H_\alpha$ has **even** head weight $\mathbf{1}_4^T z_{\text{head}} \in \{0, 2, 4\}$. This parity invariant allows us to construct a half-integer dual cone $2B \subset \mathbb{Z}^{4+q}$ ($D = 2$) combining the $n$ standard basis vectors $2e_j$, the $4$ Hadamard head vectors $(\mathbf{1}_4; \mathbf{0}_q) - 2e_i$ ($0 \le i < 4$), and balanced cross-vectors $(v_\ell; 2e_{4+\ell})$ where $v_\ell \in \{\pm 1\}^4$ satisfies $\mathbf{1}_4^T v_\ell = 0$ (Theorem 3.1). Using the Hadamard-Simplex Loom, we construct **five infinite families** (Theorem 3.2), resolving **10 open catalog parameter sets (5 complementary pairs)** across Ranks $7, 9$, and $10$:
   - $g = 6$ (Rank $7$), $\frac{v}{k} = \frac{5}{3}$: $\mathrm{DSRG}(50c, 30c, 21c, 16c, 21c)$ for all $c \ge 1$, resolving **$\mathrm{DSRG}(50, 30, 21, 16, 21)$**, **$\mathrm{DSRG}(50, 19, 10, 9, 6)$** ($c = 1$) and **$\mathrm{DSRG}(100, 60, 42, 32, 42)$**, **$\mathrm{DSRG}(100, 39, 21, 20, 12)$** ($c = 2$);
   - $g = 6$ (Rank $7$), $\frac{v}{k} = \frac{5}{2}$: $\mathrm{DSRG}(75c, 30c, 14c, 9c, 14c)$ for all $c \ge 1$, resolving **$\mathrm{DSRG}(75, 30, 14, 9, 14)$** and **$\mathrm{DSRG}(75, 44, 28, 27, 24)$** ($c = 1$);
   - $g = 8$ (Rank $9$), $\frac{v}{k} = \frac{7}{4}$: $\mathrm{DSRG}(98c, 56c, 36c, 29c, 36c)$ for all $c \ge 1$, resolving **$\mathrm{DSRG}(98, 56, 36, 29, 36)$** and **$\mathrm{DSRG}(98, 41, 21, 20, 15)$** ($c = 1$);
   - $g = 9$ (Rank $10$), $\frac{v}{k} = \frac{8}{3}$: $\mathrm{DSRG}(96c, 36c, 15c, 11c, 15c)$ for all $c \ge 1$, resolving **$\mathrm{DSRG}(96, 36, 15, 11, 15)$** and **$\mathrm{DSRG}(96, 59, 38, 37, 35)$** ($c = 1$).
   Combined with our Rank-$7$ nonexistence proof for $v/k \in \{14/3, 14/9\}$ in [14], Theorem 3.2 resolves **100% of all open Rank-7 ($g = 6$) $t = \mu$ parameter sets** in Hobart and Brouwer's catalog [2] (Corollary 3.3).

3. **The Root-Difference Simplex Loom ($D = 1$, Section 4) and $\mathbb{Z}_q$-Circulant Orbit Synthesis:**
   For $n = r + q$ ($g = r + q - 1$) and $L \mid \mu$, we introduce the $2$-block hyperplane
   $$
   \alpha = \frac{1}{L}\Bigl(\underbrace{1, 1, \dots, 1}_{r},\; \underbrace{w, w, \dots, w}_{q}\Bigr) \in \mathbb{Q}^{r+q}, \qquad \frac{v}{k} = \frac{r + w q}{L},
   \tag{9}
   $$
   paired with the integer dual basis ($D = 1$)
   $$
   B = \{e_0, \dots, e_{r+q-1}\} \;\cup\; \bigl\{\,e_{i_h} - e_h + e_{r + \ell_h} : 0 \le h < r\,\bigr\},
   \tag{10}
   $$
   where every head coordinate $h \in \{0, \dots, r-1\}$ (which has negative diagonal target entry $-d + \mu / L < 0$) is covered by a $-1$ entry in $\beta_h = e_{i_h} - e_h + e_{r + \ell_h}$ (Theorem 4.1). When $r = m_{\text{hb}} q$ is a multiple of $q$, we prove a **$\mathbb{Z}_q$-Circulant Orbit Reduction** (Theorem 4.1(ii)) that reduces the $(r+q)^2$ matrix equations to $(m_{\text{hb}}+1)^2 q$ circulant offset equations over $2m_{\text{hb}} + 1$ canonical dual vectors. Using this reduction, we establish:
   - **The Two-Parameter $w = 2$ Family (Theorem 4.2):**
     $$
     \mathrm{DSRG}\bigl(9rc,\; 3(2r-1)c,\; 2(2r-1)c,\; (4r-5)c,\; 2(2r-1)c\bigr) \qquad \forall 6 \le r \le 12,\;\; c \ge 1,
     \tag{11}
     $$
     resolving **12 open catalog parameter sets (6 complementary pairs)** across Ranks $12, 14, 18, 20$, and $24$:
     $(54, 33, 22, 19, 22)$, $(108, 66, 44, 38, 44)$, $(63, 39, 26, 23, 26)$, $(81, 51, 34, 31, 34)$, $(90, 57, 38, 35, 38)$, and $(108, 69, 46, 43, 46)$ and their $6$ complements.
   - **Four Asymmetric Multi-Block Root-Difference Families (Theorem 4.3):**
     Realizing $(r, q, w, L) \in \{(6, 3, 3, 8),\; (8, 4, 2, 11),\; (4, 8, 2, 11),\; (12, 6, 2, 17)\}$, resolving **8 additional open catalog parameter sets (4 complementary pairs)**:
     $(75, 40, 24, 19, 24)$, $(64, 44, 33, 29, 33)$, $(100, 55, 33, 28, 33)$, and $(96, 68, 51, 47, 51)$ and their $4$ complements.

4. **Higher-Block and Parity-Gadget Duality Looms (Section 5):**
   In Section 5, we prove four structural and obstruction theorems that resolve **8 additional open catalog parameter sets (4 complementary pairs)** and provide independent outer-product syntheses of $4$ comparison parameter sets:
   - **Theorem 5.1 (Dual Affine-Hyperplane and Column-Sum Divisibility Law):** Proves $\mathbf{1}_v^T B = k \alpha^T$ and $L \mid D \cdot \gcd(k, \mu)$. Defining $\rho(v, k, \mu, d) := \frac{\mu}{\gcd(k, \mu) d}$, we prove that any positive-weight hyperplane requires $D \ge \rho$, strictly obstructing $16$ open catalog families at $D = 1$.
   - **Theorem 5.2 (Neutral-Pivot 3-Block Bypass Loom):** When $L \mid \gcd(k, \mu)$ ($D = 1$) and $n \mid v$, choosing a 3-block hyperplane $\alpha = \frac{1}{L}(a_1^{r_1}, \bar{a}^{r_2}, a_3^{r_3})$ with $\bar{a} = \frac{L d}{\mu}$ zeroes out the diagonal $T_{j, j} = 0$ on Block 2, allowing root-difference vectors to bypass Block 2 entirely. This resolves **$\mathrm{DSRG}(99, 30, 10, 7, 10)$** and **$\mathrm{DSRG}(88, 60, 45, 39, 45)$** and their complements.
   - **Theorem 5.3 ($\mathbb{F}_2$-Nullspace Rank Law & Even-Rank-$r$ Hadamard-Simplex Loom):** For $D = 2$, $\bar{Z}\bar{B}^T = 0 \in \mathbb{F}_2^{v \times v}$ forces $\operatorname{rank}_{\mathbb{F}_2}(\bar{Z}) + \operatorname{rank}_{\mathbb{F}_2}(\bar{B}) \le n$. Aligning all odd-entry dual vectors along $(a \bmod 2) \in \ker_{\mathbb{F}_2}(\bar{Z})$ restricts $\operatorname{rowspace}_{\mathbb{F}_2}(\bar{B})$ to a $1$-dimensional subspace ($\operatorname{rank}_{\mathbb{F}_2}(\bar{B}) \le 1$) and guarantees even inner products $b^T z \in 2\mathbb{Z}$ across $H_\alpha$. Restricting $H_\alpha$ to the $\{0, 2\}$-compatible slice $S_{\text{compat}}(B_{\text{tmpl}})$ via Proposition 2.3(2) with $r = 6, q = 9, L = 14$ and $\mathbb{Z}_3$-equivariant orbit reduction resolves **$\mathrm{DSRG}(96, 56, 35, 31, 35)$** and its complement.
   - **Theorem 5.4 (3-Vector Parity-Gadget Decomposition):** When $L \mid \mu, L \nmid k$, and $L \mid 2k$ ($D = 2$), subtracting a 3-vector parity gadget $G = \sum_{m=1}^3 z^{(m)} (b_{\text{odd}}^{(m)})^T \in 2\mathbb{Z}^{n \times n}$ where $z^{(3)} = (z^{(1)} + z^{(2)}) \bmod 2$ yields an integer residual target matrix $T - \frac{1}{2}G \in \mathbb{Z}^{n \times n}$ whose required residual scaled-dual multiplicity sums $\frac{2ka_j}{L} - \sum_{m=1}^3 (b_{\text{odd}}^{(m)})_j$ are even integers for all $j$, allowing the remaining $v - 3$ vertices to be synthesized by integer root-difference dual vectors on the jointly compatible slice $S_{\text{compat}}$. This resolves **$\mathrm{DSRG}(108, 45, 20, 17, 20)$** and its complement, and provides independent constant-hyperplane outer-product syntheses of **$\mathrm{DSRG}(91, 39, 18, 15, 18)$** and **$\mathrm{DSRG}(91, 52, 32, 28, 32)$** and their complements.

### 1.2 Summary Tables of Newly Resolved and Comparison Parameter Sets

Table 1 summarizes the **38 newly resolved open $\mathrm{DSRG}$ parameter sets** ($19$ primary $t = \mu$ parameter sets and their $19$ complementary $t^c = \lambda^c + 1$ parameter sets) in Hobart and Brouwer's catalog [2] ($v \le 110$). None of these $38$ parameter sets appear in prior literature [1–10] or in concurrent publications [11–18]. Table 2 lists $13$ additional primary parameter sets ($26$ explicit $\mathrm{DSRG}$s) synthesized by our looms that provide independent outer-product realizations of $2$ previously known catalog rows ($r = 8, 11$ of Theorem 4.2), $9$ parameter sets independently constructed via equitable partitions in [11], and $2$ parameter sets concurrently obtained in [17, 19]; following standard attribution rules, these $26$ comparison graphs are excluded from our count of $38$ newly resolved open parameter sets.

| # | Rank $n = g+1$ | Primary Open Catalog Entry $(v, k, t, \lambda, \mu)$ | Complementary Open Catalog Entry $(v, k^c, t^c, \lambda^c, \mu^c)$ | Loom & Hyperplane $\alpha \in \mathbb{Q}^n$ | Active Support $(\|S\|, \|B\|, \text{pairs})$ | Theorem |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1, 2 | $7$ ($g=6$) | $(50, 30, 21, 16, 21)$ | $(50, 19, 10, 9, 6)$ | Hadamard ($D=2$), $\frac{1}{6}(\mathbf{1}_4, 2\mathbf{1}_3)$ | $(14, 15, 40)$ | Thm. 3.2 |
| 3, 4 | $7$ ($g=6$) | $(75, 30, 14, 9, 14)$ | $(75, 44, 28, 27, 24)$ | Hadamard ($D=2$), $\frac{1}{4}(\mathbf{1}_4, 2\mathbf{1}_3)$ | $(13, 14, 47)$ | Thm. 3.2 |
| 5, 6 | $7$ ($g=6$) | $(100, 60, 42, 32, 42)$ | $(100, 39, 21, 20, 12)$ | Hadamard ($D=2$), $\frac{1}{6}(\mathbf{1}_4, 2\mathbf{1}_3)$ | $(14, 15, 47)$ | Thm. 3.2 ($c=2$ ext.) |
| 7, 8 | $9$ ($g=8$) | $(75, 40, 24, 19, 24)$ | $(75, 34, 18, 17, 14)$ | Root-Diff ($D=1$), $\frac{1}{8}(\mathbf{1}_6, 3\mathbf{1}_3)$ | $(18, 15, 50)$ | Thm. 4.3 |
| 9, 10 | $9$ ($g=8$) | $(98, 56, 36, 29, 36)$ | $(98, 41, 21, 20, 15)$ | Hadamard ($D=2$), $\frac{1}{8}(\mathbf{1}_4, 2\mathbf{1}_5)$ | $(24, 22, 74)$ | Thm. 3.2 |
| 11, 12 | $10$ ($g=9$) | $(96, 36, 15, 11, 15)$ | $(96, 59, 38, 37, 35)$ | Hadamard ($D=2$), $\frac{1}{6}(\mathbf{1}_4, 2\mathbf{1}_6)$ | $(36, 21, 79)$ | Thm. 3.2 |
| 13, 14 | $11$ ($g=10$) | $(99, 30, 10, 7, 10)$ | $(99, 68, 48, 47, 46)$ | Neutral-Pivot ($D=1$), $\frac{1}{10}(2^4, 3^3, 4^4)$ | $(24, 15, 75)$ | Thm. 5.2 |
| 15, 16 | $11$ ($g=10$) | $(88, 60, 45, 39, 45)$ | $(88, 27, 12, 11, 7)$ | Neutral-Pivot ($D=1$), $\frac{1}{15}(1^4, 2^3, 3^4)$ | $(39, 15, 52)$ | Thm. 5.2 |
| 17, 18 | $12$ ($g=11$) | $(54, 33, 22, 19, 22)$ | $(54, 20, 9, 8, 7)$ | Root-Diff ($D=1$), $\frac{1}{11}(\mathbf{1}_6, 2\mathbf{1}_6)$ | $(36, 18, 54)$ | Thm. 4.2 |
| 19, 20 | $12$ ($g=11$) | $(64, 44, 33, 29, 33)$ | $(64, 19, 8, 7, 5)$ | Root-Diff ($D=1$), $\frac{1}{11}(\mathbf{1}_8, 2\mathbf{1}_4)$ | $(40, 20, 64)$ | Thm. 4.3 |
| 21, 22 | $12$ ($g=11$) | $(100, 55, 33, 28, 33)$ | $(100, 44, 22, 21, 18)$ | Root-Diff ($D=1$), $\frac{1}{11}(\mathbf{1}_4, 2\mathbf{1}_8)$ | $(38, 20, 86)$ | Thm. 4.3 |
| 23, 24 | $12$ ($g=11$) | $(108, 66, 44, 38, 44)$ | $(108, 41, 19, 18, 14)$ | Root-Diff ($D=1$), $\frac{1}{11}(\mathbf{1}_6, 2\mathbf{1}_6)$ | $(65, 18, 99)$ | Thm. 4.2 ($c=2$ ext.) |
| 25, 26 | $14$ ($g=13$) | $(63, 39, 26, 23, 26)$ | $(63, 23, 10, 9, 8)$ | Root-Diff ($D=1$), $\frac{1}{13}(\mathbf{1}_7, 2\mathbf{1}_7)$ | $(49, 21, 63)$ | Thm. 4.2 |
| 27, 28 | $15$ ($g=14$) | $(96, 56, 35, 31, 35)$ | $(96, 39, 18, 17, 15)$ | Had-Simplex ($D=2$), $\frac{1}{14}(1^6, 2^9)$ | $(93, 27, 93)$ | Thm. 5.3 |
| 29, 30 | $16$ ($g=15$) | $(108, 45, 20, 17, 20)$ | $(108, 62, 37, 36, 35)$ | Parity-Gadget ($D=2$), $\frac{1}{10}(1^8, 2^8)$ | $(84, 27, 106)$ | Thm. 5.4 |
| 31, 32 | $18$ ($g=17$) | $(81, 51, 34, 31, 34)$ | $(81, 29, 12, 11, 10)$ | Root-Diff ($D=1$), $\frac{1}{17}(\mathbf{1}_9, 2\mathbf{1}_9)$ | $(72, 27, 81)$ | Thm. 4.2 |
| 33, 34 | $18$ ($g=17$) | $(96, 68, 51, 47, 51)$ | $(96, 27, 10, 9, 7)$ | Root-Diff ($D=1$), $\frac{1}{17}(\mathbf{1}_{12}, 2\mathbf{1}_6)$ | $(84, 30, 96)$ | Thm. 4.3 |
| 35, 36 | $20$ ($g=19$) | $(90, 57, 38, 35, 38)$ | $(90, 32, 13, 12, 11)$ | Root-Diff ($D=1$), $\frac{1}{19}(\mathbf{1}_{10}, 2\mathbf{1}_{10})$ | $(90, 30, 90)$ | Thm. 4.2 |
| 37, 38 | $24$ ($g=23$) | $(108, 69, 46, 43, 46)$ | $(108, 38, 15, 14, 13)$ | Root-Diff ($D=1$), $\frac{1}{23}(\mathbf{1}_{12}, 2\mathbf{1}_{12})$ | $(108, 36, 108)$ | Thm. 4.2 |

*Table 1: The 38 newly resolved open $\mathrm{DSRG}$ parameter sets in Hobart and Brouwer's catalog [2] ($v \le 110$), grouped into 19 primary $t = \mu$ families and their 19 complementary $t^c = \lambda^c + 1$ families. These comprise 17 primitive base pairs (34 DSRGs) and 2 $c = 2$ coclique-extension pairs (4 DSRGs: entries 5, 6 and 23, 24, cf. Duval [1, Theorem 4.1] / Construction T10 in [2]), where our direct $c = 2$ outer-product syntheses achieve higher support diversity ($47 > 40$ and $99 > 54$ active pairs) than the product blow-up $A_1 \otimes J_2$.*

| # | Rank $n = g+1$ | Primary Parameter Set $(v, k, t, \lambda, \mu)$ | Complementary Parameter Set $(v, k^c, t^c, \lambda^c, \mu^c)$ | Loom & Hyperplane $\alpha \in \mathbb{Q}^n$ | Active Support $(\|S\|, \|B\|, \text{pairs})$ | Prior / Concurrent Reference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1, C2 | $8$ ($g=7$) | $(32, 14, 7, 5, 7)$ | $(32, 17, 10, 9, 9)$ | $\frac{1}{7}(\mathbf{1}_4, 3\mathbf{1}_4)$ | $(10, 12, 28)$ | Concurrent [11] ($s=0$) |
| C3, C4 | $8$ ($g=7$) | $(64, 28, 14, 10, 14)$ | $(64, 35, 21, 20, 18)$ | $\frac{1}{7}(\mathbf{1}_4, 3\mathbf{1}_4)$ | $(12, 12, 32)$ | Concurrent [11] ($s=0, c=2$) |
| C5, C6 | $8$ ($g=7$) | $(96, 42, 21, 15, 21)$ | $(96, 53, 32, 31, 27)$ | $\frac{1}{7}(\mathbf{1}_4, 3\mathbf{1}_4)$ | $(12, 12, 31)$ | Concurrent [11] ($s=0, c=3$) |
| C7, C8 | $10$ ($g=9$) | $(40, 18, 9, 7, 9)$ | $(40, 21, 12, 11, 11)$ | $\frac{1}{9}(\mathbf{1}_5, 3\mathbf{1}_5)$ | $(22, 15, 40)$ | Concurrent [11] ($s=1$) |
| C9, C10 | $10$ ($g=9$) | $(80, 36, 18, 14, 18)$ | $(80, 43, 25, 24, 22)$ | $\frac{1}{9}(\mathbf{1}_5, 3\mathbf{1}_5)$ | $(26, 15, 40)$ | Concurrent [11] ($s=1, c=2$) |
| C11, C12 | $12$ ($g=11$) | $(48, 22, 11, 9, 11)$ | $(48, 25, 14, 13, 13)$ | $\frac{1}{11}(\mathbf{1}_6, 3\mathbf{1}_6)$ | $(38, 18, 47)$ | Concurrent [11] ($s=2$) |
| C13, C14 | $12$ ($g=11$) | $(96, 44, 22, 18, 22)$ | $(96, 51, 29, 28, 26)$ | $\frac{1}{11}(\mathbf{1}_6, 3\mathbf{1}_6)$ | $(38, 18, 47)$ | Concurrent [11] ($s=2, c=2$) |
| C15, C16 | $12$ ($g=11$) | $(108, 33, 11, 8, 11)$ | $(108, 74, 52, 51, 50)$ | $\frac{1}{11}(\mathbf{1}_6, 5\mathbf{1}_6)$ | $(29, 18, 86)$ | Concurrent [11] ($w=5, s=0$) |
| C17, C18 | $14$ ($g=13$) | $(56, 26, 13, 11, 13)$ | $(56, 29, 16, 15, 15)$ | $\frac{1}{13}(\mathbf{1}_7, 3\mathbf{1}_7)$ | $(53, 21, 56)$ | Concurrent [11] ($s=3$) |
| C19, C20 | $14$ ($g=13$) | $(91, 39, 18, 15, 18)$ | $(91, 51, 30, 29, 28)$ | Parity-Gadget, $\frac{1}{6}\mathbf{1}_{14}$ | $(71, 24, 88)$ | Concurrent [17, 19] |
| C21, C22 | $14$ ($g=13$) | $(91, 52, 32, 28, 32)$ | $(91, 38, 18, 17, 15)$ | Parity-Gadget, $\frac{1}{8}\mathbf{1}_{14}$ | $(68, 24, 86)$ | Concurrent [17, 19] |
| C23, C24 | $16$ ($g=15$) | $(72, 45, 30, 27, 30)$ | $(72, 26, 11, 10, 9)$ | $\frac{1}{15}(\mathbf{1}_8, 2\mathbf{1}_8)$ | $(72, 24, 72)$ | Catalog [2] ($r=8$ of Thm. 4.2) |
| C25, C26 | $22$ ($g=21$) | $(99, 63, 42, 39, 42)$ | $(99, 35, 14, 13, 12)$ | $\frac{1}{21}(\mathbf{1}_{11}, 2\mathbf{1}_{11})$ | $(99, 33, 99)$ | Catalog [2] ($r=11$ of Thm. 4.2) |

*Table 2: Thirteen additional comparison primary families (26 explicit $\mathrm{DSRG}$s) synthesized by our looms and verified in `verify_all.py`. These are excluded from our count of 38 newly resolved open parameter sets.*

---

## 2. The Constructive Converse of Hyperplane Duality and Structural Obstruction Laws

We begin by proving the exact constructive converse to the Rank-$(g+1)$ Hyperplane Duality Theorem of [14, Thm. 3.1].

### Theorem 2.1 (Rank-$(g+1)$ Outer-Product Synthesis Theorem)
*Let $g \ge 2$, $n := g + 1$, $d \ge 1$, and $\mu \ge d$ be positive integers such that $v := \frac{g(g+1)d^2}{\mu}$ is an integer with $k := g d < v$. Let $\alpha \in \mathbb{Q}^n$ be a rational vector satisfying*
$$
\mathbf{1}_n^T \alpha = \frac{v}{k} = \frac{n d}{\mu} > 1.
\tag{12}
$$
*Let $S \subseteq H_\alpha = \{z \in \{0,1\}^n \setminus \{\mathbf{0}_n, \mathbf{1}_n\} : \alpha^T z = 1\}$ and $B \subseteq \mathcal{B}(S) = \{\beta \in \mathbb{Q}^n : \mathbf{1}_n^T \beta = 1,\; \beta^T z \in \{0,1\} \;\forall z \in S\}$ be finite sets, and let*
$$
\mathcal{P}_0(S, B) := \bigl\{(z, \beta) \in S \times B : \beta^T z = 0\bigr\}
\tag{13}
$$
*be the set of orthogonal compatible pairs. Suppose there exist non-negative integers $N(z, \beta) \in \mathbb{Z}_{\ge 0}$ for $(z, \beta) \in \mathcal{P}_0(S, B)$ satisfying the $n \times n$ matrix equation*
$$
\sum_{(z, \beta) \in \mathcal{P}_0(S, B)} N(z, \beta)\, z \beta^T = -d I_n + \mu \mathbf{1}_n \alpha^T.
\tag{14}
$$
*Then:*
1. *The sum of the integer multiplicities is automatically equal to $v$:*
   $$
   \sum_{(z, \beta) \in \mathcal{P}_0(S, B)} N(z, \beta) = v = \frac{g(g+1)d^2}{\mu}.
   \tag{15}
   $$
2. *For every integer $c \ge 1$, let $C_c \in \{0,1\}^{cv \times n}$ and $R_c^T \in \mathbb{Q}^{cv \times n}$ be the matrices obtained by listing each pair $(z, \beta) \in \mathcal{P}_0(S, B)$ with $N(z, \beta) > 0$ exactly $c \cdot N(z, \beta)$ times as a row $z^T$ of $C_c$ and as the corresponding column $\beta$ of $R_c$. Then the $cv \times cv$ matrix*
   $$
   A_c := C_c R_c \in \{0,1\}^{cv \times cv}
   \tag{16}
   $$
   *is a $(0,1)$-matrix with zero diagonal, adjacency rank $\operatorname{rank}(A_c) = n = g + 1$, and satisfies*
   $$
   A_c \mathbf{1}_{cv} = A_c^T \mathbf{1}_{cv} = c k \mathbf{1}_{cv}, \qquad A_c^2 + c d A_c = c \mu J_{cv}.
   \tag{17}
   $$
   *Consequently, $A_c$ is the adjacency matrix of a $\mathrm{DSRG}(cv, cgd, c\mu, c(\mu - d), c\mu)$, and its directional complement $A_c^c := J_{cv} - I_{cv} - A_c$ is the adjacency matrix of a $\mathrm{DSRG}(cv, cv - 1 - ck, cv - 1 - 2ck + c\mu, cv - 2 - 2ck + c\mu, cv - 2ck + c(\mu - d))$.*

#### Proof
**Part 1:** For every $(z, \beta) \in \mathcal{P}_0(S, B)$, we have $z \in H_\alpha \implies \alpha^T z = 1$ and $\beta \in \mathcal{B}(S) \implies \beta^T \mathbf{1}_n = 1$. Multiplying Eq. (14) on the left by $\alpha^T$ and on the right by $\mathbf{1}_n$ yields
$$
\begin{aligned}
\sum_{(z, \beta) \in \mathcal{P}_0(S, B)} N(z, \beta)\, (\alpha^T z)(\beta^T \mathbf{1}_n) &= \alpha^T \bigl(-d I_n + \mu \mathbf{1}_n \alpha^T\bigr) \mathbf{1}_n \\
&= -d (\alpha^T \mathbf{1}_n) + \mu (\alpha^T \mathbf{1}_n)^2.
\end{aligned}
$$
Since $\alpha^T z = 1$, $\beta^T \mathbf{1}_n = 1$, and $\alpha^T \mathbf{1}_n = \frac{n d}{\mu}$, the left-hand side is $\sum_{(z, \beta)} N(z, \beta)$, while the right-hand side is
$$
\frac{n d}{\mu}\Bigl(-d + \mu \frac{n d}{\mu}\Bigr) = \frac{n d}{\mu}(n - 1)d = \frac{g(g + 1)d^2}{\mu} = v,
$$
which establishes Eq. (15).

**Part 2:** Fix an integer $c \ge 1$. By Part 1, the total number of rows of $C_c$ (and columns of $R_c$) is $\sum_{(z, \beta)} c \cdot N(z, \beta) = cv$. For each index $x \in \{1, \dots, cv\}$, let $(z^{(x)}, \beta^{(x)}) \in \mathcal{P}_0(S, B)$ be the pair assigned to row $x$ of $C_c$ and column $x$ of $R_c$. Then the $(x, y)$ entry of $A_c = C_c R_c$ is
$$
(A_c)_{x, y} = (z^{(x)})^T \beta^{(y)}.
$$
Because $z^{(x)} \in S$ and $\beta^{(y)} \in B \subseteq \mathcal{B}(S)$, the definition of $\mathcal{B}(S)$ in Eq. (6) guarantees that $(z^{(x)})^T \beta^{(y)} \in \{0, 1\}$ for all $x, y \in \{1, \dots, cv\}$, so $A_c \in \{0,1\}^{cv \times cv}$ is a $(0,1)$-matrix. Furthermore, for $x = y$, $(z^{(x)}, \beta^{(x)}) \in \mathcal{P}_0(S, B)$ satisfies $(z^{(x)})^T \beta^{(x)} = 0$, so $\operatorname{diag}(A_c) = \mathbf{0}_{cv}$.

Next, by construction of $C_c$ and $R_c$, the $n \times n$ reverse product $R_c C_c$ is given by
$$
R_c C_c = \sum_{x=1}^{cv} \beta^{(x)} (z^{(x)})^T = \Bigl(\sum_{(z, \beta) \in \mathcal{P}_0(S, B)} c \cdot N(z, \beta)\, z \beta^T\Bigr)^T = c\bigl(-d I_n + \mu \alpha \mathbf{1}_n^T\bigr),
\tag{18}
$$
where the last equality takes the transpose of Eq. (14). Note also that since every row $z^{(x)}$ of $C_c$ satisfies $(z^{(x)})^T \alpha = 1$ and every column $\beta^{(y)}$ of $R_c$ satisfies $\mathbf{1}_n^T \beta^{(y)} = 1$, we have the exact vector identities
$$
C_c \alpha = \mathbf{1}_{cv} \qquad \text{and} \qquad \mathbf{1}_n^T R_c = \mathbf{1}_{cv}^T.
\tag{19}
$$
We now verify the row sums, column sums, and quadratic matrix identity of $A_c$:
- **Column sums:** Using Eqs. (18)–(19) and $\mathbf{1}_n^T \alpha = \frac{n d}{\mu} = \frac{(g+1)d}{\mu}$, we have
  $$
  \begin{aligned}
  \mathbf{1}_{cv}^T A_c &= \mathbf{1}_{cv}^T C_c R_c = (\mathbf{1}_n^T R_c) C_c R_c = \mathbf{1}_n^T (R_c C_c) R_c \\
  &= c \mathbf{1}_n^T \bigl(-d I_n + \mu \alpha \mathbf{1}_n^T\bigr) R_c = c\bigl(-d \mathbf{1}_n^T + \mu(\mathbf{1}_n^T \alpha)\mathbf{1}_n^T\bigr) R_c \\
  &= c(-d + (g+1)d)\mathbf{1}_n^T R_c = c g d \mathbf{1}_{cv}^T = c k \mathbf{1}_{cv}^T.
  \end{aligned}
  $$
- **Row sums:** Similarly, using $C_c \alpha = \mathbf{1}_{cv}$ and Eq. (18), we have
  $$
  \begin{aligned}
  A_c \mathbf{1}_{cv} &= C_c R_c (C_c \alpha) = C_c (R_c C_c) \alpha = c C_c \bigl(-d I_n + \mu \alpha \mathbf{1}_n^T\bigr)\alpha \\
  &= c C_c \bigl(-d \alpha + \mu(\mathbf{1}_n^T \alpha)\alpha\bigr) = c g d (C_c \alpha) = c k \mathbf{1}_{cv}.
  \end{aligned}
  $$
- **Quadratic identity:** Using associativity $A_c^2 = (C_c R_c)(C_c R_c) = C_c (R_c C_c) R_c$ and Eqs. (18)–(19), we obtain
  $$
  \begin{aligned}
  A_c^2 &= C_c \bigl(c(-d I_n + \mu \alpha \mathbf{1}_n^T)\bigr) R_c \\
  &= -c d (C_c R_c) + c \mu (C_c \alpha)(\mathbf{1}_n^T R_c) \\
  &= -c d A_c + c \mu \mathbf{1}_{cv} \mathbf{1}_{cv}^T = -c d A_c + c \mu J_{cv},
  \end{aligned}
  $$
  so $A_c^2 + c d A_c = c \mu J_{cv}$. Finally, since $\det(-d I_n + \mu \mathbf{1}_n \alpha^T) = (-d)^{n-1}(-d + \mu \mathbf{1}_n^T \alpha) = (-d)^{n-1} g d \ne 0$, the $n \times n$ matrix $R_c C_c$ has full rank $n$, which forces $\operatorname{rank}(C_c) = \operatorname{rank}(R_c) = \operatorname{rank}(A_c) = n = g + 1$. Thus $A_c$ is a $\mathrm{DSRG}(cv, cgd, c\mu, c(\mu - d), c\mu)$, and Eq. (2) gives the parameters of $A_c^c$. $\square$

### Remark 2.2 (Relation to Duval's Coclique Extension Theorem and Support Diversity)
*When the multiplicities $N_c(z, \beta) = c \cdot N_1(z, \beta)$ in Theorem 2.1(2) are obtained by uniformly repeating every active pair $(z, \beta)$ of a base solution $N_1$ exactly $c \ge 2$ times, the resulting $(0,1)$-matrix $A_c = C_c R_c$ is permutation-isomorphic to Duval's coclique extension $A_1 \otimes J_c$ [1, Theorem 4.1] (referred to as Construction T10 in Hobart and Brouwer's catalog [2]). In this product case, the active support sets $S$ and $B$ remain identical to those of the base graph $A_1$.*

*Crucially, however, Theorem 2.1 also allows solving Eq. (14) directly at target order $cv$, which can produce genuine, non-product outer-product factorizations with strictly higher support diversity. In Table 1, this distinction is explicitly demonstrated by the two $c = 2$ coclique-extension parameter sets:*
1. *For $\mathrm{DSRG}(100, 60, 42, 32, 42)$ (entry 5 in Table 1), our direct outer-product synthesis utilizes $|S| = 14$ slice vectors, $|B| = 15$ dual vectors, and $47$ active orthogonal pairs—strictly exceeding the $40$ active pairs of the uniform product blow-up of $\mathrm{DSRG}(50, 30, 21, 16, 21)$ (entry 1).*
2. *For $\mathrm{DSRG}(108, 66, 44, 38, 44)$ (entry 23 in Table 1), our direct outer-product synthesis utilizes $|S| = 65$ slice vectors, $|B| = 18$ dual vectors, and $99$ active orthogonal pairs—substantially exceeding the $54$ active pairs of the uniform product blow-up of $\mathrm{DSRG}(54, 33, 22, 19, 22)$ (entry 17).*

---

### 2.1 Structural Obstruction Laws: Denominator Divisibility and Diagonal Sign Coverage

Whereas Theorem 2.1 shows that any integer solution $N(z, \beta)$ to Eq. (14) yields a $\mathrm{DSRG}$, not every rational hyperplane $\alpha \in \mathbb{Q}^n$ with $\mathbf{1}_n^T \alpha = v / k$ can support an integer outer-product factorization with a given dual denominator $D \in \mathbb{Z}_{\ge 1}$ (where $D \beta \in \mathbb{Z}^n$ for all $\beta \in B$). The following proposition establishes two fundamental arithmetic and sign constraints that guide the design of both of our constructive looms.

### Proposition 2.2 (Denominator Divisibility and Diagonal Sign Coverage Laws)
*Suppose $(S, B, N)$ is an integer outer-product synthesis satisfying Eq. (14) on a rational hyperplane $\alpha \in \mathbb{Q}^n$. Write $\alpha = \frac{1}{L}(a_1, \dots, a_n)^T$ in lowest common terms, where $L \in \mathbb{Z}_{\ge 1}$, $a_1, \dots, a_n \in \mathbb{Z}$, and $\gcd(a_1, \dots, a_n, L) = 1$. Suppose $D \in \mathbb{Z}_{\ge 1}$ is a common denominator for the active dual vectors, so that $b := D \beta \in \mathbb{Z}^n$ for every $\beta \in B$ with $\sum_{z \in S} N(z, \beta) > 0$. Then:*
1. *(Denominator Divisibility Law): The hyperplane denominator $L$ must divide $D \mu$:*
   $$
   L \;\big|\; D \mu, \qquad \text{and} \qquad \sum_{j=1}^n a_j = L \frac{v}{k}.
   \tag{20}
   $$
2. *(Diagonal Sign Coverage Law): For every coordinate $j \in \{1, \dots, n\}$, the $j$-th diagonal entry of Eq. (14) satisfies*
   $$
   \sum_{\substack{(z, \beta) \in \mathcal{P}_0(S, B) \\ z_j = 1}} N(z, \beta)\, \beta_j = -d + \frac{\mu a_j}{L}.
   \tag{21}
   $$
   *In particular, for every "head" coordinate $j \in \{1, \dots, n\}$ with $\frac{\mu a_j}{L} < d$ (respectively $\frac{\mu a_j}{L} > d$), there must exist at least one active pair $(z, \beta) \in \mathcal{P}_0(S, B)$ with $N(z, \beta) \ge 1$ and $z_j = 1$ such that $\beta_j < 0$ (respectively $\beta_j > 0$).*

#### Proof
**Part 1:** Multiplying Eq. (14) by $D$, the left-hand side is
$$
\sum_{(z, \beta) \in \mathcal{P}_0(S, B)} N(z, \beta)\, z (D \beta)^T \in \mathbb{Z}^{n \times n},
$$
because $N(z, \beta) \in \mathbb{Z}$, $z \in \{0,1\}^n \subset \mathbb{Z}^n$, and $D \beta \in \mathbb{Z}^n$. Therefore, the right-hand side $D(-d I_n + \mu \mathbf{1}_n \alpha^T)$ must have integer entries. For any $i \ne j$, the $(i, j)$ entry of $D(-d I_n + \mu \mathbf{1}_n \alpha^T)$ is $\frac{D \mu a_j}{L} \in \mathbb{Z}$. Since $\frac{D \mu a_j}{L} \in \mathbb{Z}$ for all $j \in \{1, \dots, n\}$ and $\gcd(a_1, \dots, a_n, L) = 1$, Bézout's identity implies $\frac{D \mu}{L} \in \mathbb{Z}$, i.e., $L \mid D \mu$.

**Part 2:** Taking the $(j, j)$ entry of Eq. (14) gives $\sum_{(z, \beta)} N(z, \beta) z_j \beta_j = -d + \mu \alpha_j = -d + \frac{\mu a_j}{L}$. Since $z_j \in \{0, 1\}$, only pairs with $z_j = 1$ contribute to the sum, yielding Eq. (21). Because $N(z, \beta) \ge 0$, if $-d + \frac{\mu a_j}{L} < 0$, at least one term with $N(z, \beta) \ge 1$ and $z_j = 1$ must have $\beta_j < 0$ (and similarly for $> 0$). $\square$

---

### 2.2 Single-MILP Bipartite-Compatibility Formulation and Pre-Filtered Pure-MILP Reduction

Given a hyperplane $\alpha = \frac{1}{L} a \in \mathbb{Q}^n$ and a candidate pool $B_{\text{all}} \subset \frac{1}{D}\mathbb{Z}^n$ of scaled dual vectors $b = D \beta \in \mathbb{Z}^n$ with $\mathbf{1}_n^T b = D$, finding a mutually compatible pair $(S, B)$ with $S \subseteq H_\alpha$ and $B \subseteq B_{\text{all}}$ alongside the integer multiplicities $N(z, \beta) \in \mathbb{Z}_{\ge 0}$ can be formulated directly as a **single mixed-integer linear program (MILP)**:

### Proposition 2.3 (Exact Bipartite-Compatibility MILP and Pre-Filtered Pure MILP)
1. *Let $H_\alpha = \{z \in \{0,1\}^n \setminus \{\mathbf{0}, \mathbf{1}\} : a^T z = L\}$ and let $B_{\text{all}} \subset \{b \in \mathbb{Z}^n : \mathbf{1}_n^T b = D\}$. Introduce integer multiplicity variables $N_{z, b} \in \{0, 1, \dots, v\}$ for each orthogonal pair $(z, b) \in H_\alpha \times B_{\text{all}}$ with $b^T z = 0$, together with binary support indicators $u_z \in \{0, 1\}$ ($z \in H_\alpha$) and $w_b \in \{0, 1\}$ ($b \in B_{\text{all}}$), subject to the linear constraints:*
   $$
   \begin{aligned}
   \sum_{\substack{(z, b) \in H_\alpha \times B_{\text{all}} \\ b^T z = 0}} N_{z, b}\, z b^T &= D\Bigl(-d I_n + \frac{\mu}{L} \mathbf{1}_n a^T\Bigr), \\
   \sum_{b \in B_{\text{all}}:\; b^T z = 0} N_{z, b} &\le v u_z \qquad \forall z \in H_\alpha, \\
   \sum_{z \in H_\alpha:\; b^T z = 0} N_{z, b} &\le v w_b \qquad \forall b \in B_{\text{all}}, \\
   u_z + w_b &\le 1 \qquad \forall (z, b) \in H_\alpha \times B_{\text{all}} \text{ with } b^T z \notin \{0, D\}.
   \end{aligned}
   \tag{22}
   $$
   *Then any feasible solution $(N, u, w)$ to Eq. (22) defines a valid compatible support $S = \{z \in H_\alpha : u_z = 1\}$ and $B = \{\frac{1}{D}b : b \in B_{\text{all}},\, w_b = 1\}$ satisfying all hypotheses of Theorem 2.1.*
2. *(Pre-Filtered Pure-MILP Reduction): Conversely, if a dual template $B_{\text{tmpl}} \subset \{b \in \mathbb{Z}^n : \mathbf{1}_n^T b = D\}$ is fixed in advance and we define the pre-filtered compatible slice*
   $$
   S_{\text{compat}}(B_{\text{tmpl}}) := \bigl\{z \in H_\alpha : b^T z \in \{0, D\} \;\;\forall b \in B_{\text{tmpl}}\bigr\},
   \tag{23}
   $$
   *then every pair $(z, b) \in S_{\text{compat}}(B_{\text{tmpl}}) \times B_{\text{tmpl}}$ is automatically $\{0, D\}$-compatible, so the binary variables $(u_z, w_b)$ and incompatibility constraints in Eq. (22) drop out completely, reducing Eq. (22) to the pure integer linear system $\sum_{b^T z = 0} N_{z, b} z b^T = D(-d I_n + \frac{\mu}{L}\mathbf{1}_n a^T)$ with $N_{z, b} \in \mathbb{Z}_{\ge 0}$.*

#### Proof
In Part 1, if $N_{z, b} > 0$, the degree constraints force $u_z = 1$ and $w_b = 1$. For any $z \in S$ ($u_z = 1$) and $\frac{1}{D}b \in B$ ($w_b = 1$), we have $u_z + w_b = 2 > 1$, so the fourth constraint in Eq. (22) guarantees $b^T z \in \{0, D\}$, i.e., $\beta^T z \in \{0, 1\}$. Thus $B \subseteq \mathcal{B}(S)$, and Theorem 2.1 applies. Part 2 follows immediately by setting $u_z = 1$ on $S_{\text{compat}}(B_{\text{tmpl}})$ and $w_b = 1$ on $B_{\text{tmpl}}$. $\square$

---

## 3. The Hadamard-Simplex Loom ($D = 2$) and Complete Resolution of Open Rank-7 $t = \mu$ DSRGs

In our preceding paper [14], after proving nonexistence of $\mathrm{DSRG}(v, 6d, \mu, \mu - d, \mu)$ (Rank $7$, $g = 6$) for $v / k \in \{14/3, 14/9\}$, we noted that the remaining open Rank-$7$ $t = \mu$ parameter sets in Hobart and Brouwer's catalog [2] have ratios $v / k = 5/3$ ($\mathrm{DSRG}(50, 30, 21, 16, 21)$ and $\mathrm{DSRG}(100, 60, 42, 32, 42)$) and $v / k = 5/2$ ($\mathrm{DSRG}(75, 30, 14, 9, 14)$). When we applied our $\operatorname{Aut}(\alpha)$-canonicalized per-basis filter (`src/filter_g6_bases.cpp`) to the $22,655$ canonical Rank-$7$ hyperplanes in `results/alphas_g6.txt`, almost all hyperplanes were eliminated, but two hyperplanes with a striking $4 + 3$ block structure survived:
$$
\alpha_{(5/3)} = \frac{1}{6}(1, 1, 1, 1, 2, 2, 2)^T \quad\text{and}\quad \alpha_{(5/2)} = \frac{1}{4}(1, 1, 1, 1, 2, 2, 2)^T.
$$
Understanding why these two hyperplanes admit compatible half-integer dual cones leads directly to a general constructive architecture across all ranks $n = 4 + q \ge 7$, which we call the **Hadamard-Simplex Loom**.

### Theorem 3.1 (The Hadamard-Simplex Loom)
*Let $q \ge 3$, $n := 4 + q$ ($g = q + 3$), and $1 \le h \le q$ be integers. Define the rational $2$-block hyperplane*
$$
\alpha_{q, h} := \frac{1}{2h}\Bigl(\underbrace{1, 1, 1, 1}_{4},\; \underbrace{2, 2, \dots, 2}_{q}\Bigr)^T \in \mathbb{Q}^{4+q}, \qquad \text{with } \mathbf{1}_{4+q}^T \alpha_{q, h} = \frac{q + 2}{h}.
\tag{24}
$$
*Write each binary vector $z \in \{0,1\}^{4+q}$ as $z = (z_{\text{head}}; z_{\text{tail}})$ with $z_{\text{head}} \in \{0,1\}^4$ and $z_{\text{tail}} \in \{0,1\}^q$. Then:*
1. *(Even Head-Weight Invariant): Every slice vector $z = (z_{\text{head}}; z_{\text{tail}}) \in H_{\alpha_{q, h}}$ satisfies*
   $$
   s_{\text{head}}(z) := \mathbf{1}_4^T z_{\text{head}} \in \{0, 2, 4\} \quad (\text{even}), \qquad \mathbf{1}_q^T z_{\text{tail}} = h - \frac{1}{2} s_{\text{head}}(z).
   \tag{25}
   $$
2. *(Universal Compatibility of Pure Hadamard Head Duals): Define the $4$ pure Hadamard head vectors $b_{\text{had}}^{(i)} := (\mathbf{1}_4 - 2e_i;\; \mathbf{0}_q) \in \mathbb{Z}^{4+q}$ for $i \in \{0, 1, 2, 3\}$, and the $n$ standard basis vectors $b_{\text{std}}^{(j)} := 2e_j \in \mathbb{Z}^{4+q}$ for $j \in \{0, \dots, 3+q\}$. Then every $b \in \{b_{\text{std}}^{(j)}\}_{j=0}^{3+q} \cup \{b_{\text{had}}^{(i)}\}_{i=0}^3$ satisfies $\mathbf{1}_{4+q}^T b = 2$ and*
   $$
   b^T z \in \{0, 2\} \qquad \forall z \in H_{\alpha_{q, h}}.
   \tag{26}
   $$
3. *(Balanced Hadamard-Tail Cross-Vectors): Let $\mathcal{V}_4 := \{v \in \{\pm 1\}^4 : \mathbf{1}_4^T v = 0\}$ be the set of $\binom{4}{2} = 6$ balanced $\pm 1$ vectors on the $4$ head coordinates. For each $v \in \mathcal{V}_4$ and each tail index $\ell \in \{0, \dots, q-1\}$, define the cross-vector*
   $$
   b_{\text{cross}}^{(v, \ell)} := (v;\; 2e_\ell) \in \mathbb{Z}^{4+q}, \qquad \text{with } \mathbf{1}_{4+q}^T b_{\text{cross}}^{(v, \ell)} = 2.
   \tag{27}
   $$
   *Then for any $z = (z_{\text{head}}; z_{\text{tail}}) \in H_{\alpha_{q, h}}$, we have $b_{\text{cross}}^{(v, \ell)T} z \in \{0, 2\}$ if and only if:*
   - *either $s_{\text{head}}(z) \in \{0, 4\}$ (in which case $v^T z_{\text{head}} = 0$ and $b_{\text{cross}}^{(v, \ell)T} z = 2(z_{\text{tail}})_\ell \in \{0, 2\}$ holds automatically for every $\ell$),*
   - *or $s_{\text{head}}(z) = 2$ and $z_{\text{head}} \notin \{\frac{1}{2}(\mathbf{1}_4 + v) \text{ when } (z_{\text{tail}})_\ell = 1,\;\; \frac{1}{2}(\mathbf{1}_4 - v) \text{ when } (z_{\text{tail}})_\ell = 0\}$.*

#### Proof
**Part 1:** By definition of $H_{\alpha_{q, h}}$, $z = (z_{\text{head}}; z_{\text{tail}}) \in \{0,1\}^{4+q} \setminus \{\mathbf{0}, \mathbf{1}\}$ lies in $H_{\alpha_{q, h}}$ if and only if
$$
\mathbf{1}_4^T z_{\text{head}} + 2\,\mathbf{1}_q^T z_{\text{tail}} = 2h.
$$
Reducing modulo $2$ gives $\mathbf{1}_4^T z_{\text{head}} \equiv 0 \pmod 2$. Since $z_{\text{head}} \in \{0,1\}^4$, we must have $s_{\text{head}}(z) = \mathbf{1}_4^T z_{\text{head}} \in \{0, 2, 4\}$ and $\mathbf{1}_q^T z_{\text{tail}} = h - \frac{1}{2} s_{\text{head}}(z)$, proving Eq. (25).

**Part 2:** For $b_{\text{std}}^{(j)} = 2e_j$, $\mathbf{1}_{4+q}^T (2e_j) = 2$ and $(2e_j)^T z = 2 z_j \in \{0, 2\}$ for all $z \in \{0,1\}^{4+q}$. For $b_{\text{had}}^{(i)} = (\mathbf{1}_4 - 2e_i; \mathbf{0}_q)$, we have $\mathbf{1}_{4+q}^T b_{\text{had}}^{(i)} = 4 - 2 = 2$, and for any $z \in H_{\alpha_{q, h}}$:
$$
(b_{\text{had}}^{(i)})^T z = s_{\text{head}}(z) - 2 z_i.
$$
We check the three cases for $s_{\text{head}}(z) \in \{0, 2, 4\}$ from Part 1:
- If $s_{\text{head}}(z) = 0$, then $z_{\text{head}} = \mathbf{0}_4$, so $z_i = 0$ and $s_{\text{head}}(z) - 2z_i = 0 \in \{0, 2\}$.
- If $s_{\text{head}}(z) = 2$, then $z_i \in \{0, 1\}$, so $s_{\text{head}}(z) - 2z_i = 2 - 2z_i \in \{0, 2\}$.
- If $s_{\text{head}}(z) = 4$, then $z_{\text{head}} = \mathbf{1}_4$, so $z_i = 1$ and $s_{\text{head}}(z) - 2z_i = 4 - 2 = 2 \in \{0, 2\}$.
Thus $b_{\text{had}}^{(i)T} z \in \{0, 2\}$ holds universally across all of $H_{\alpha_{q, h}}$!

**Part 3:** For $b_{\text{cross}}^{(v, \ell)} = (v; 2e_\ell)$ with $v \in \mathcal{V}_4$, we have $\mathbf{1}_{4+q}^T b_{\text{cross}}^{(v, \ell)} = 0 + 2 = 2$, and
$$
b_{\text{cross}}^{(v, \ell)T} z = v^T z_{\text{head}} + 2 (z_{\text{tail}})_\ell.
$$
If $s_{\text{head}}(z) \in \{0, 4\}$, then $z_{\text{head}} \in \{\mathbf{0}_4, \mathbf{1}_4\}$, so $v^T z_{\text{head}} = 0$ (since $\mathbf{1}_4^T v = 0$) and $b_{\text{cross}}^{(v, \ell)T} z = 2(z_{\text{tail}})_\ell \in \{0, 2\}$. If $s_{\text{head}}(z) = 2$, then $z_{\text{head}}$ has two $1$'s and two $0$'s, so $v^T z_{\text{head}} \in \{-2, 0, +2\}$: specifically, $v^T z_{\text{head}} = +2$ iff $z_{\text{head}} = \frac{1}{2}(\mathbf{1}_4 + v)$, $v^T z_{\text{head}} = -2$ iff $z_{\text{head}} = \frac{1}{2}(\mathbf{1}_4 - v)$, and $v^T z_{\text{head}} = 0$ for the other $4$ weight-$2$ vectors. Combining $v^T z_{\text{head}} \in \{-2, 0, +2\}$ with $2(z_{\text{tail}})_\ell \in \{0, 2\}$ shows that $v^T z_{\text{head}} + 2(z_{\text{tail}})_\ell \in \{0, 2\}$ fails only when $(v^T z_{\text{head}}, (z_{\text{tail}})_\ell) = (+2, 1)$ (giving $4$) or $(-2, 0)$ (giving $-2$). $\square$

---

### Theorem 3.2 (Existence of Five Hadamard-Simplex Infinite Families)
*Applying the Hadamard-Simplex Loom of Theorem 3.1 and Proposition 2.3(1) over the candidate pool*
$$
B_{\text{all}}^{\text{had}}(q) := \{2e_j\}_{j=0}^{3+q} \;\cup\; \{(\mathbf{1}_4 - 2e_i; \mathbf{0}_q)\}_{i=0}^3 \;\cup\; \{(v; 2e_\ell) : v \in \mathcal{V}_4,\, 0 \le \ell < q\} \;\cup\; \{(\mathbf{1}_4; -2e_\ell)\}_{\ell=0}^{q-1}
\tag{28}
$$
*yields exact integer outer-product syntheses satisfying Eq. (14) for the following five infinite families for every integer $c \ge 1$:*
1. **$(q = 3, h = 3, g = 6, d = 5c, \mu = 21c)$:** $\mathrm{DSRG}(50c, 30c, 21c, 16c, 21c)$ and its complement $\mathrm{DSRG}(50c, 20c-1, 11c-1, 11c-2, 6c)$. *In particular, $c = 1$ resolves the open catalog pair **$\mathrm{DSRG}(50, 30, 21, 16, 21)$** and **$\mathrm{DSRG}(50, 19, 10, 9, 6)$**, and $c = 2$ resolves the open catalog pair **$\mathrm{DSRG}(100, 60, 42, 32, 42)$** and **$\mathrm{DSRG}(100, 39, 21, 20, 12)$**.*
2. **$(q = 3, h = 2, g = 6, d = 5c, \mu = 14c)$:** $\mathrm{DSRG}(75c, 30c, 14c, 9c, 14c)$ and its complement $\mathrm{DSRG}(75c, 45c-1, 29c-1, 29c-2, 24c)$. *In particular, $c = 1$ resolves the open catalog pair **$\mathrm{DSRG}(75, 30, 14, 9, 14)$** and **$\mathrm{DSRG}(75, 44, 28, 27, 24)$**.*
3. **$(q = 5, h = 4, g = 8, d = 7c, \mu = 36c)$:** $\mathrm{DSRG}(98c, 56c, 36c, 29c, 36c)$ and its complement $\mathrm{DSRG}(98c, 42c-1, 22c-1, 22c-2, 15c)$. *In particular, $c = 1$ resolves the open catalog pair **$\mathrm{DSRG}(98, 56, 36, 29, 36)$** and **$\mathrm{DSRG}(98, 41, 21, 20, 15)$**.*
4. **$(q = 6, h = 3, g = 9, d = 4c, \mu = 15c)$:** $\mathrm{DSRG}(96c, 36c, 15c, 11c, 15c)$ and its complement $\mathrm{DSRG}(96c, 60c-1, 39c-1, 39c-2, 35c)$. *In particular, $c = 1$ resolves the open catalog pair **$\mathrm{DSRG}(96, 36, 15, 11, 15)$** and **$\mathrm{DSRG}(96, 59, 38, 37, 35)$**.*

#### Proof and Explicit Rank-7 Witness Tables
By Theorem 2.1, it suffices to exhibit the compatible sets $S \subseteq H_{\alpha_{q, h}}$, $2B \subseteq B_{\text{all}}^{\text{had}}(q)$, and positive integer multiplicities $N(z, \beta) \in \mathbb{Z}_{\ge 1}$ on $\mathcal{P}_0(S, B)$ satisfying
$$
2h \sum_{(z, \beta) \in \mathcal{P}_0(S, B)} N(z, \beta)\, z (2\beta)^T = 2\bigl(-2hd I_{4+q} + \mu \mathbf{1}_{4+q} a^T\bigr), \qquad a = (\mathbf{1}_4; 2\mathbf{1}_q).
\tag{29}
$$
For $\mathrm{DSRG}(50, 30, 21, 16, 21)$ ($q = 3, h = 3, n = 7, d = 5, \mu = 21, L = 6$), the right-hand side of Eq. (14) scaled by $D = 2$ is the integer matrix
$$
2\bigl(-5 I_7 + 21 \mathbf{1}_7 \alpha_{3, 3}^T\bigr) = -10 I_7 + \mathbf{1}_7 (7, 7, 7, 7, 14, 14, 14).
$$
Table 3 gives the complete list of $40$ orthogonal pairs $(z, 2\beta)$ and their positive integer multiplicities $N(z, \beta) \in \{1, 2\}$ (summing to $v = 50$) for $\mathrm{DSRG}(50, 30, 21, 16, 21)$. All $14$ active vectors $z \in S$ satisfy $z_0 + z_1 + z_2 + z_3 + 2(z_4 + z_5 + z_6) = 6$, all $15$ active dual vectors $2\beta \in 2B$ satisfy $\mathbf{1}_7^T(2\beta) = 2$, every pair $(z', 2\beta') \in S \times 2B$ satisfies $(2\beta')^T z' \in \{0, 2\}$, and summing $N(z, \beta) z (2\beta)^T$ over the $40$ rows of Table 3 reproduces $-10 I_7 + \mathbf{1}_7(7,7,7,7,14,14,14)$ identically.

| Pairs 1–20: $N \mid z \mid 2\beta$ | Pairs 21–40: $N \mid z \mid 2\beta$ |
| :--- | :--- |
| $1 \mid (0,0,0,0,1,1,1) \mid (0,2,0,0,0,0,0)$ | $2 \mid (1,0,0,1,1,0,1) \mid (-1,1,1,1,0,0,0)$ |
| $1 \mid (0,0,0,0,1,1,1) \mid (1,1,-1,1,0,0,0)$ | $1 \mid (1,0,0,1,0,1,1) \mid (0,0,2,0,0,0,0)$ |
| $1 \mid (0,0,1,1,0,1,1) \mid (0,0,0,0,2,0,0)$ | $1 \mid (1,0,0,1,0,1,1) \mid (1,-1,1,-1,2,0,0)$ |
| $1 \mid (0,0,1,1,0,1,1) \mid (1,1,-1,1,0,0,0)$ | $1 \mid (1,0,1,0,0,1,1) \mid (-1,1,1,1,0,0,0)$ |
| $1 \mid (0,0,1,1,0,1,1) \mid (1,1,1,-1,0,0,0)$ | $1 \mid (1,0,1,0,0,1,1) \mid (1,1,-1,1,0,0,0)$ |
| $2 \mid (0,0,1,1,0,1,1) \mid (1,1,-1,-1,0,0,2)$ | $1 \mid (1,0,1,0,0,1,1) \mid (-1,-1,1,1,2,0,0)$ |
| $1 \mid (0,1,0,1,1,0,1) \mid (0,0,2,0,0,0,0)$ | $2 \mid (1,0,1,0,0,1,1) \mid (-1,1,-1,1,0,2,0)$ |
| $2 \mid (0,1,0,1,1,0,1) \mid (0,0,0,0,0,2,0)$ | $1 \mid (1,1,0,0,1,1,0) \mid (0,0,2,0,0,0,0)$ |
| $1 \mid (0,1,0,1,1,0,1) \mid (1,-1,1,1,0,0,0)$ | $1 \mid (1,1,0,0,1,1,0) \mid (0,0,0,2,0,0,0)$ |
| $1 \mid (0,1,0,1,1,0,1) \mid (1,-1,1,-1,2,0,0)$ | $2 \mid (1,1,0,0,1,1,0) \mid (0,0,0,0,0,0,2)$ |
| $2 \mid (0,1,1,0,1,1,0) \mid (1,-1,1,1,0,0,0)$ | $1 \mid (1,1,0,0,1,1,0) \mid (-1,-1,1,1,2,0,0)$ |
| $1 \mid (0,1,1,0,1,1,0) \mid (1,1,-1,-1,0,0,2)$ | $1 \mid (1,1,1,1,1,0,0) \mid (0,0,0,0,0,2,0)$ |
| $1 \mid (0,1,1,0,1,0,1) \mid (2,0,0,0,0,0,0)$ | $1 \mid (1,1,1,1,1,0,0) \mid (0,0,0,0,0,0,2)$ |
| $1 \mid (0,1,1,0,1,0,1) \mid (1,-1,1,1,0,0,0)$ | $2 \mid (1,1,1,1,1,0,0) \mid (-1,1,-1,1,0,2,0)$ |
| $1 \mid (0,1,1,0,1,0,1) \mid (-1,1,-1,1,0,2,0)$ | $2 \mid (1,1,1,1,1,0,0) \mid (1,1,-1,-1,0,0,2)$ |
| $1 \mid (0,1,1,0,0,1,1) \mid (0,0,0,0,2,0,0)$ | $2 \mid (1,1,1,1,0,1,0) \mid (-1,-1,1,1,2,0,0)$ |
| $1 \mid (0,1,1,0,0,1,1) \mid (1,-1,1,1,0,0,0)$ | $1 \mid (1,1,1,1,0,1,0) \mid (1,1,-1,-1,0,0,2)$ |
| $1 \mid (1,0,0,1,1,1,0) \mid (0,0,0,0,0,0,2)$ | $1 \mid (1,1,1,1,0,0,1) \mid (0,0,0,0,2,0,0)$ |
| $2 \mid (1,0,0,1,1,1,0) \mid (1,1,1,-1,0,0,0)$ | $1 \mid (1,1,1,1,0,0,1) \mid (0,0,0,0,0,2,0)$ |
| $1 \mid (1,0,0,1,1,0,1) \mid (0,0,0,0,0,2,0)$ | $1 \mid (1,1,1,1,0,0,1) \mid (1,-1,1,-1,2,0,0)$ |

*Table 3: Complete explicit Rank-7 outer-product synthesis $(N(z, \beta), z, 2\beta)$ for $\mathrm{DSRG}(50, 30, 21, 16, 21)$ on $\alpha_{3,3} = \frac{1}{6}(1,1,1,1,2,2,2)^T$. Multiplying $N(z, \beta)$ by $c \ge 1$ yields $\mathrm{DSRG}(50c, 30c, 21c, 16c, 21c)$ for every $c \ge 1$.*

The explicit factorizations $(z, 2\beta, N(z, \beta))$ for $\mathrm{DSRG}(75, 30, 14, 9, 14)$ ($47$ pairs), $\mathrm{DSRG}(100, 60, 42, 32, 42)$ ($47$ pairs), $\mathrm{DSRG}(98, 56, 36, 29, 36)$ ($74$ pairs), and $\mathrm{DSRG}(96, 36, 15, 11, 15)$ ($79$ pairs) are provided in full in `outer_product_syntheses.json` and verified in exact integer arithmetic by `verify_all.py`. $\square$

### Corollary 3.3 (Complete Resolution of All Open Rank-7 $t = \mu$ Catalog Parameter Sets)
*Across Hobart and Brouwer's catalog [2] for $v \le 110$, there were exactly $5$ open complementary pairs of parameter sets (marked `?`) with $t = \mu$ (or $t^c = \lambda^c + 1$) and eigenvalue multiplicity $g = 6$ (Rank $7$):*
- *The $2$ complementary pairs at $v = 56$ with $v / k \in \{14/3, 14/9\}$ — namely $(56, 12, 3, 1, 3)$ (and complement $(56, 43, 34, 33, 33)$) and $(56, 36, 27, 21, 27)$ (and complement $(56, 19, 10, 9, 3)$) — **do not exist** by [14, Thm. 3.5].*
- *The $3$ complementary pairs with $v / k \in \{5/3, 5/2\}$ — namely $(50, 30, 21, 16, 21)$ (and complement $(50, 19, 10, 9, 6)$), $(75, 30, 14, 9, 14)$ (and complement $(75, 44, 28, 27, 24)$), and $(100, 60, 42, 32, 42)$ (and complement $(100, 39, 21, 20, 12)$) — **all exist** by Theorem 3.2(1)–(2).*
*Thus 100% of all open Rank-7 ($g = 6$) $t = \mu$ parameter sets in [2] (all $5$ open complementary pairs, $10$ directed graphs) are now completely resolved.*

---

## 4. The Root-Difference Simplex Loom ($D = 1$) and $\mathbb{Z}_q$-Circulant Orbit Synthesis

We now turn to the $D = 1$ regime (where every dual vector $\beta \in B$ is an **integer vector** $\beta \in \mathbb{Z}^n$ with $\mathbf{1}_n^T \beta = 1$). By Proposition 2.2(1), $D = 1$ requires $L \mid \mu$; and by Proposition 2.2(2), every coordinate $h$ with $\frac{\mu a_h}{L} < d$ must appear with $\beta_h \le -1$ in at least one active dual vector $\beta \in B$.

### Theorem 4.1 (The Root-Difference Simplex Loom and $\mathbb{Z}_q$-Circulant Orbit Reduction)
*Let $r \ge 2$, $q \ge 1$, $n := r + q$ ($g = r + q - 1$), $w \ge 2$, and $L \ge 2$ be integers such that $1 \le \frac{\mu}{L} < d \le \frac{\mu w}{L}$. Consider the $2$-block hyperplane*
$$
\alpha_{r, q, w, L} := \frac{1}{L}\Bigl(\underbrace{1, 1, \dots, 1}_{r},\; \underbrace{w, w, \dots, w}_{q}\Bigr)^T \in \mathbb{Q}^{r+q}, \qquad \frac{v}{k} = \frac{r + w q}{L}.
\tag{30}
$$
*For each head coordinate $h \in \{0, \dots, r-1\}$, choose a distinct partner head coordinate $i_h \in \{0, \dots, r-1\} \setminus \{h\}$ and a tail index $\ell_h \in \{0, \dots, q-1\}$, and define the integer Root-Difference Simplex dual basis*
$$
B_{\text{root}} := \{e_0, \dots, e_{r+q-1}\} \;\cup\; \bigl\{\,\beta_{\text{root}}^{(h)} := e_{i_h} - e_h + e_{r + \ell_h} : 0 \le h < r\,\bigr\} \subset \mathbb{Z}^{r+q}.
\tag{31}
$$
*Then:*
1. *(Transition-Forcing Law): Every vector $\beta \in B_{\text{root}}$ satisfies $\mathbf{1}_{r+q}^T \beta = 1$. Moreover, a slice vector $z = (z_{\text{head}}; z_{\text{tail}}) \in H_{\alpha_{r,q,w,L}}$ lies in the pre-filtered compatible slice $S_{\text{compat}}(B_{\text{root}}) = \{z \in H_{\alpha_{r,q,w,L}} : \beta^T z \in \{0, 1\} \;\forall \beta \in B_{\text{root}}\}$ if and only if, for every $h \in \{0, \dots, r-1\}$:*
   $$
   \begin{aligned}
   (z_h, z_{i_h}) = (0, 1) &\implies (z_{\text{tail}})_{\ell_h} = 0, \\
   (z_h, z_{i_h}) = (1, 0) &\implies (z_{\text{tail}})_{\ell_h} = 1, \\
   z_h = z_{i_h} &\implies (z_{\text{tail}})_{\ell_h} \in \{0, 1\} \text{ is unconstrained by } \beta_{\text{root}}^{(h)}.
   \end{aligned}
   \tag{32}
   $$
2. *($\mathbb{Z}_q$-Circulant Orbit Reduction): Suppose $r = m_{\text{hb}} q$ is a multiple of $q$ and $v$ is a multiple of $q$. Partition the $n = (m_{\text{hb}} + 1)q$ coordinates into $m_{\text{hb}}$ head blocks $I_0, \dots, I_{m_{\text{hb}}-1}$ of size $q$ and $1$ tail block $I_{m_{\text{hb}}}$ of size $q$, and let the cyclic group $\mathbb{Z}_q = \langle \sigma \rangle$ act diagonally by cyclic shift $+1 \bmod q$ within each of the $m_{\text{hb}} + 1$ blocks. If $B_{\text{root}}$ is generated under $\mathbb{Z}_q$ by the $m_{\text{hb}} + 1$ canonical basis vectors $\{e_{u q}\}_{u=0}^{m_{\text{hb}}}$ and $m_{\text{hb}}$ canonical root-difference vectors $\{\beta_{\text{canon}}^{(u)}\}_{u=0}^{m_{\text{hb}}-1}$, then any non-negative integer solution $x(z, \beta_{\text{canon}}) \in \mathbb{Z}_{\ge 0}$ on $\{(z, \beta_{\text{canon}}) \in S_{\text{compat}}(B_{\text{root}}) \times B_{\text{canon}} : \beta_{\text{canon}}^T z = 0\}$ to the $(m_{\text{hb}} + 1)^2 q$ circulant offset equations*
   $$
   \sum_{(z, \beta)} x(z, \beta) \sum_{i=0}^{q-1} z_{u q + i}\, \beta_{u' q + ((i + j) \bmod q)} = \frac{\mu a_{u' q}}{L} - d\,\delta_{u, u'}\delta_{j, 0} \qquad \bigl(0 \le u, u' \le m_{\text{hb}},\;\; 0 \le j < q\bigr)
   \tag{33}
   $$
   *expands under $\mathbb{Z}_q$ into a full integer outer-product synthesis $N(\sigma^s(z), \sigma^s(\beta)) = x(z, \beta)$ ($0 \le s < q$) satisfying Eq. (14).*

#### Proof
**Part 1:** For $\beta_{\text{root}}^{(h)} = e_{i_h} - e_h + e_{r + \ell_h}$, we have $\mathbf{1}_{r+q}^T \beta_{\text{root}}^{(h)} = 1 - 1 + 1 = 1$, and
$$
\bigl(\beta_{\text{root}}^{(h)}\bigr)^T z = z_{i_h} - z_h + (z_{\text{tail}})_{\ell_h}.
$$
Since $z_{i_h}, z_h, (z_{\text{tail}})_{\ell_h} \in \{0, 1\}$:
- If $(z_h, z_{i_h}) = (0, 1)$, then $z_{i_h} - z_h = 1$, so $1 + (z_{\text{tail}})_{\ell_h} \in \{0, 1\} \iff (z_{\text{tail}})_{\ell_h} = 0$.
- If $(z_h, z_{i_h}) = (1, 0)$, then $z_{i_h} - z_h = -1$, so $-1 + (z_{\text{tail}})_{\ell_h} \in \{0, 1\} \iff (z_{\text{tail}})_{\ell_h} = 1$.
- If $z_h = z_{i_h}$, then $z_{i_h} - z_h = 0$, so $0 + (z_{\text{tail}})_{\ell_h} = (z_{\text{tail}})_{\ell_h} \in \{0, 1\}$ holds for both $(z_{\text{tail}})_{\ell_h} \in \{0, 1\}$.
This proves Eq. (32).

**Part 2:** Because $\alpha_{r,q,w,L}$ is constant on each of the $m_{\text{hb}} + 1$ blocks of size $q$, both $H_{\alpha_{r,q,w,L}}$ and $S_{\text{compat}}(B_{\text{root}})$ are invariant under the diagonal action of $\mathbb{Z}_q$, and the target matrix $T = -d I_n + \frac{\mu}{L}\mathbf{1}_n a^T$ is a $(m_{\text{hb}} + 1) \times (m_{\text{hb}} + 1)$ block matrix whose $(u, u')$ block is the $q \times q$ circulant matrix with first row $(T_{u q,\; u' q + j})_{j=0}^{q-1} = \frac{\mu a_{u' q}}{L} - d\,\delta_{u, u'}\delta_{j, 0}$. For any pair $(z, \beta)$, summing the outer products over its $\mathbb{Z}_q$-orbit $\sum_{s=0}^{q-1} \sigma^s(z)\sigma^s(\beta)^T$ produces in block $(u, u')$ a $q \times q$ circulant matrix whose $(0, j)$ entry is
$$
\sum_{s=0}^{q-1} \sigma^s(z)_{u q}\, \sigma^s(\beta)_{u' q + j} = \sum_{s=0}^{q-1} z_{u q + ((-s) \bmod q)}\, \beta_{u' q + ((j - s) \bmod q)} = \sum_{i=0}^{q-1} z_{u q + i}\, \beta_{u' q + ((i + j) \bmod q)}.
$$
Thus Eq. (33) is necessary and sufficient for the $\mathbb{Z}_q$-expanded multiplicities $N(\sigma^s(z), \sigma^s(\beta)) = x(z, \beta)$ to satisfy Eq. (14). $\square$

---

### 4.1 Realization of the Two-Parameter Family $\mathrm{DSRG}(9rc, 3(2r-1)c, 2(2r-1)c, (4r-5)c, 2(2r-1)c)$

Specializing Theorem 4.1 to $q = r$, $m_{\text{hb}} = 1$, $w = 2$, $L = 2r - 1 = g$, $d = 3c$, and $\mu = 2(2r - 1)c$ with the directed cyclic root-difference dual basis
$$
B_{\text{cyc}}(r) := \{e_0, \dots, e_{2r-1}\} \;\cup\; \bigl\{\,e_i - e_{(i+1)\bmod r} + e_{r+i} : 0 \le i < r\,\bigr\} \subset \mathbb{Z}^{2r}
\tag{34}
$$
and the $3$ canonical $\mathbb{Z}_r$-orbit dual representatives $\beta^{(0)} = e_0$, $\beta^{(1)} = e_r$, and $\beta^{(2)} = e_0 - e_1 + e_r$ yields our second main constructive theorem. Notice from Eq. (32) that for $B_{\text{cyc}}(r)$, whenever $z_{\text{head}} \in \{0,1\}^r$ has $2p$ cyclic transitions ($p$ transitions $1 \to 0$ and $p$ transitions $0 \to 1$ as $i \to (i+1)\bmod r$), exactly $p$ coordinates of $z_{\text{tail}}$ are forced to $0$, $p$ coordinates of $z_{\text{tail}}$ are forced to $1$, and the remaining $r - 2p$ coordinates of $z_{\text{tail}}$ are completely free!

### Theorem 4.2 (Two-Parameter Root-Difference Simplex Family for $6 \le r \le 12$)
*For every integer $r \in \{6, 7, 8, 9, 10, 11, 12\}$ and every integer $c \ge 1$, the hyperplane $\alpha = \frac{1}{2r-1}(\mathbf{1}_r, 2\mathbf{1}_r)^T \in \mathbb{Q}^{2r}$ and the directed cyclic dual basis $B_{\text{cyc}}(r)$ of Eq. (34) admit an exact $\mathbb{Z}_r$-circulant outer-product synthesis consisting of $9$ orbits of size $r$ (each with multiplicity $c$), generated by the $9$ compatible pairs $(z, \beta) \in S_{\text{compat}}(B_{\text{cyc}}(r)) \times \{e_0, e_r, e_0 - e_1 + e_r\}$ listed in Table 4. Consequently, there exists a*
$$
\mathrm{DSRG}\bigl(9rc,\; 3(2r-1)c,\; 2(2r-1)c,\; (4r-5)c,\; 2(2r-1)c\bigr)
\tag{35}
$$
*of adjacency rank $2r$ (and its complementary $\mathrm{DSRG}$) for every $6 \le r \le 12$ and $c \ge 1$. In particular, for $v \le 110$, this resolves **12 open catalog parameter sets (6 complementary pairs)**:*
- **$r = 6, c = 1$ ($g = 11$):** $\mathrm{DSRG}(54, 33, 22, 19, 22)$ and $\mathrm{DSRG}(54, 20, 9, 8, 7)$;
- **$r = 6, c = 2$ ($g = 11$):** $\mathrm{DSRG}(108, 66, 44, 38, 44)$ and $\mathrm{DSRG}(108, 41, 19, 18, 14)$;
- **$r = 7, c = 1$ ($g = 13$):** $\mathrm{DSRG}(63, 39, 26, 23, 26)$ and $\mathrm{DSRG}(63, 23, 10, 9, 8)$;
- **$r = 9, c = 1$ ($g = 17$):** $\mathrm{DSRG}(81, 51, 34, 31, 34)$ and $\mathrm{DSRG}(81, 29, 12, 11, 10)$;
- **$r = 10, c = 1$ ($g = 19$):** $\mathrm{DSRG}(90, 57, 38, 35, 38)$ and $\mathrm{DSRG}(90, 32, 13, 12, 11)$;
- **$r = 12, c = 1$ ($g = 23$):** $\mathrm{DSRG}(108, 69, 46, 43, 46)$ and $\mathrm{DSRG}(108, 38, 15, 14, 13)$.

#### Proof and Complete Explicit Table of 9-Orbit Generators for $6 \le r \le 12$
By Theorem 4.1(2) with $m_{\text{hb}} = 1, q = r, w = 2, L = 2r - 1, d = 3, \mu = 2(2r-1)$, the right-hand side of Eq. (33) has $\frac{\mu a_0}{L} = 2$ on the head block and $\frac{\mu a_r}{L} = 4$ on the tail block. Table 4 displays the $9$ explicit $\mathbb{Z}_r$-orbit generators $(z_{\text{head}}, z_{\text{tail}}, \beta) \in S_{\text{compat}}(B_{\text{cyc}}(r)) \times \{e_0, e_r, e_0 - e_1 + e_r\}$ (written as binary strings of length $r$) for every $r \in \{6, 7, 8, 9, 10, 11, 12\}$. In each row of Table 4, one checks immediately that $s_1 + 2 s_2 = 2r - 1$, $\beta^T z = 0$, the transition-forcing law of Eq. (32) holds at every $i \in \{0, \dots, r-1\}$, and the $9$ orbits satisfy the $4r$ circulant offset equations of Eq. (33) identically.

| $r$ | Primary $\mathrm{DSRG}$ | Orbit 1–3: $\beta \mid z_{\text{head}} \mid z_{\text{tail}}$ | Orbit 4–6: $\beta \mid z_{\text{head}} \mid z_{\text{tail}}$ | Orbit 7–9: $\beta \mid z_{\text{head}} \mid z_{\text{tail}}$ |
| :--- | :--- | :--- | :--- | :--- |
| **$6$** | $(54,33,22,19,22)$ | $e_r \mid 100011 \mid 010111$<br>$e_0 \mid 011100 \mid 111001$<br>$e_0 \mid 011100 \mid 101011$ | $\beta_{\text{rt}} \mid 011010 \mid 110101$<br>$e_0 \mid 000111 \mid 101110$<br>$\beta_{\text{rt}} \mid 000111 \mid 011110$ | $e_r \mid 111110 \mid 001101$<br>$e_r \mid 111101 \mid 011010$<br>$e_r \mid 111101 \mid 001011$ |
| **$7$** | $(63,39,26,23,26)$ | $e_0 \mid 0011100 \mid 1111001$<br>$e_0 \mid 0000111 \mid 0111110$<br>$e_r \mid 0000111 \mid 0111110$ | $e_r \mid 1111010 \mid 0110101$<br>$\beta_{\text{rt}} \mid 1111001 \mid 0010111$<br>$\beta_{\text{rt}} \mid 1100111 \mid 0011011$ | $e_r \mid 1011101 \mid 0101011$<br>$\beta_{\text{rt}} \mid 0111110 \mid 1101100$<br>$e_0 \mid 0111011 \mid 1100110$ |
| **$8$** | $(72,45,30,27,30)$ | $\beta_{\text{rt}} \mid 01110000 \mid 11101101$<br>$e_0 \mid 01100100 \mid 11011011$<br>$e_r \mid 00001110 \mid 01111101$ | $e_r \mid 11000111 \mid 00111011$<br>$e_0 \mid 01100111 \mid 10011110$<br>$e_0 \mid 00011111 \mid 10111010$ | $e_r \mid 11111101 \mid 00111010$<br>$\beta_{\text{rt}} \mid 11111011 \mid 01000111$<br>$e_r \mid 10111111 \mid 01010110$ |
| **$9$** | $(81,51,34,31,34)$ | $e_r \mid 111110000 \mid 001101111$<br>$e_r \mid 101100011 \mid 011010111$<br>$e_0 \mid 011111000 \mid 111100011$ | $e_0 \mid 001110110 \mid 011101101$<br>$e_0 \mid 001101110 \mid 110011101$<br>$\beta_{\text{rt}} \mid 000011111 \mid 011111010$ | $e_r \mid 111101110 \mid 010011101$<br>$e_r \mid 111011101 \mid 010101011$<br>$\beta_{\text{rt}} \mid 010111111 \mid 101110100$ |
| **$10$** | $(90,57,38,35,38)$ | $e_r \mid 1000111100 \mid 0111011011$<br>$\beta_{\text{rt}} \mid 0111100010 \mid 1111001101$<br>$e_0 \mid 0100100111 \mid 1011011110$ | $e_0 \mid 0011011100 \mid 1100111011$<br>$\beta_{\text{rt}} \mid 0000011111 \mid 0111110110$<br>$e_r \mid 1111000111 \mid 0100111101$ | $e_0 \mid 0111111100 \mid 1110101001$<br>$e_r \mid 1111111101 \mid 0010101011$<br>$e_r \mid 1111111011 \mid 0001110110$ |
| **$11$** | $(99,63,42,39,42)$ | $e_r \mid 11000011001 \mid 00111110111$<br>$e_r \mid 00111110000 \mid 01011101111$<br>$e_0 \mid 00001111001 \mid 11111100110$ | $e_r \mid 10001101111 \mid 01110011110$<br>$e_0 \mid 01111101100 \mid 10011011011$<br>$\beta_{\text{rt}} \mid 01111000111 \mid 11010111010$ | $e_0 \mid 01100011111 \mid 11010110110$<br>$\beta_{\text{rt}} \mid 11110111110 \mid 01101010101$<br>$\beta_{\text{rt}} \mid 11111111111 \mid 00101101001$ |
| **$12$** | $(108,69,46,43,46)$ | $e_r \mid 111111111000 \mid 010011110011$<br>$e_r \mid 110011111110 \mid 000110111101$<br>$e_r \mid 101111100111 \mid 011111001001$ | $\beta_{\text{rt}} \mid 110000011111 \mid 001101110111$<br>$e_0 \mid 011111100010 \mid 111010011101$<br>$\beta_{\text{rt}} \mid 011100001111 \mid 111010011110$ | $e_0 \mid 011000111110 \mid 110011111001$<br>$\beta_{\text{rt}} \mid 001111110001 \mid 011101101110$<br>$e_0 \mid 000011111110 \mid 110111101100$ |

*Table 4: Complete explicit $\mathbb{Z}_r$-circulant orbit generators $(z_{\text{head}}, z_{\text{tail}}, \beta)$ for the two-parameter family $\mathrm{DSRG}(9rc, 3(2r-1)c, 2(2r-1)c, (4r-5)c, 2(2r-1)c)$ across all $6 \le r \le 12$, where $\beta_{\text{rt}} := e_0 - e_1 + e_r$. Expanding each of the $9$ generators by the $r$ cyclic shifts of $\mathbb{Z}_r$ (with multiplicity $c$) yields $A_c = C_c R_c \in \{0,1\}^{9rc \times 9rc}$.* $\square$

---

### 4.2 Asymmetric Multi-Block Root-Difference Simplex Families ($r \ne q$)

When $r \ne q$ in Eq. (30), the Root-Difference Simplex Loom of Theorem 4.1 produces four additional infinite families that resolve $8$ open catalog parameter sets ($4$ complementary pairs).

### Theorem 4.3 (Asymmetric Multi-Block Root-Difference Simplex Families)
*Applying the Root-Difference Simplex Loom of Theorem 4.1 to asymmetric $2$-block hyperplanes $\alpha_{r, q, w, L} = \frac{1}{L}(\mathbf{1}_r, w\mathbf{1}_q)^T \in \mathbb{Q}^{r+q}$ with $r \ne q$ yields exact integer outer-product syntheses for the following four infinite families for every integer $c \ge 1$:*
1. **$(r = 6, q = 3, w = 3, L = 8, g = 8, d = 5c, \mu = 24c)$:** $\mathrm{DSRG}(75c, 40c, 24c, 19c, 24c)$ and its complement $\mathrm{DSRG}(75c, 35c-1, 19c-1, 19c-2, 14c)$, using the paired head dual basis $B = \{e_0, \dots, e_8\} \cup \{e_1 - e_0 + e_6, e_0 - e_1 + e_7, e_3 - e_2 + e_8, e_2 - e_3 + e_6, e_5 - e_4 + e_7, e_4 - e_5 + e_8\}$. *For $c = 1$, this resolves the open catalog pair **$\mathrm{DSRG}(75, 40, 24, 19, 24)$** and **$\mathrm{DSRG}(75, 34, 18, 17, 14)$**.*
2. **$(r = 8, q = 4, w = 2, L = 11, g = 11, d = 4c, \mu = 33c)$:** $\mathrm{DSRG}(64c, 44c, 33c, 29c, 33c)$ and its complement $\mathrm{DSRG}(64c, 20c-1, 9c-1, 9c-2, 5c)$, using the $\mathbb{Z}_4$-invariant cross-block dual basis $B = \{e_0, \dots, e_{11}\} \cup \{e_s - e_{4+s} + e_{8+s},\; e_{4+s} - e_s + e_{8+((s+1)\bmod 4)} : 0 \le s < 4\}$. *For $c = 1$, this resolves the open catalog pair **$\mathrm{DSRG}(64, 44, 33, 29, 33)$** and **$\mathrm{DSRG}(64, 19, 8, 7, 5)$**.*
3. **$(r = 4, q = 8, w = 2, L = 11, g = 11, d = 5c, \mu = 33c)$:** $\mathrm{DSRG}(100c, 55c, 33c, 28c, 33c)$ and its complement $\mathrm{DSRG}(100c, 45c-1, 23c-1, 23c-2, 18c)$, using the bidirectional cyclic head dual basis $B = \{e_0, \dots, e_{11}\} \cup \{e_{(i+1)\bmod 4} - e_i + e_{4+i},\; e_i - e_{(i+1)\bmod 4} + e_{8+i} : 0 \le i < 4\}$. *For $c = 1$, this resolves the open catalog pair **$\mathrm{DSRG}(100, 55, 33, 28, 33)$** and **$\mathrm{DSRG}(100, 44, 22, 21, 18)$**.*
4. **$(r = 12, q = 6, w = 2, L = 17, g = 17, d = 4c, \mu = 51c)$:** $\mathrm{DSRG}(96c, 68c, 51c, 47c, 51c)$ and its complement $\mathrm{DSRG}(96c, 28c-1, 11c-1, 11c-2, 7c)$, using the $\mathbb{Z}_6$-invariant parallel-block dual basis $B = \{e_0, \dots, e_{17}\} \cup \{e_{6h+s} - e_{6h+((s+1)\bmod 6)} + e_{12+s} : h \in \{0,1\},\, 0 \le s < 6\}$. *For $c = 1$, this resolves the open catalog pair **$\mathrm{DSRG}(96, 68, 51, 47, 51)$** and **$\mathrm{DSRG}(96, 27, 10, 9, 7)$**.*

#### Proof and Explicit $\mathbb{Z}_q$-Circulant Orbit Tables
For Families (2) and (4), $r = 2q$ ($m_{\text{hb}} = 2$), so Theorem 4.1(2) reduces the synthesis to $16$ $\mathbb{Z}_q$-orbits of size $q$ ($16 \times 4 = 64$ vertices for $\mathrm{DSRG}(64, 44, 33, 29, 33)$, and $16 \times 6 = 96$ vertices for $\mathrm{DSRG}(96, 68, 51, 47, 51)$). Table 5 lists all $16$ explicit $\mathbb{Z}_4$-orbit generators for $\mathrm{DSRG}(64, 44, 33, 29, 33)$ and all $16$ explicit $\mathbb{Z}_6$-orbit generators for $\mathrm{DSRG}(96, 68, 51, 47, 51)$. The complete pair tables for all four families are provided in `outer_product_syntheses.json` and verified in exact integer arithmetic by `verify_all.py`.

| Orbit # | $\mathrm{DSRG}(64,44,33,29,33)$ ($\mathbb{Z}_4$, $q=4$): $\beta \mid z_{I_0} \mid z_{I_1} \mid z_{I_2}$ | $\mathrm{DSRG}(96,68,51,47,51)$ ($\mathbb{Z}_6$, $q=6$): $\beta \mid z_{I_0} \mid z_{I_1} \mid z_{I_2}$ |
| :--- | :--- | :--- |
| 1 | $e_0 \mid 0011 \mid 1011 \mid 1011$ | $e_0 \mid 000110 \mid 111110 \mid 111101$ |
| 2 | $e_0 \mid 0101 \mid 0111 \mid 1110$ | $e_6 \mid 001110 \mid 011110 \mid 111101$ |
| 3 | $e_4 \mid 0101 \mid 0111 \mid 1110$ | $e_6-e_7+e_{12} \mid 001110 \mid 111111 \mid 011101$ |
| 4 | $e_0-e_4+e_8 \mid 0101 \mid 1101 \mid 1011$ | $e_0 \mid 001110 \mid 111111 \mid 110101$ |
| 5 | $e_8 \mid 0110 \mid 0111 \mid 0111$ | $e_0 \mid 011011 \mid 111011 \mid 110110$ |
| 6 | $e_0 \mid 0110 \mid 1110 \mid 1011$ | $e_0 \mid 011111 \mid 000011 \mid 111110$ |
| 7 | $e_0 \mid 0111 \mid 0101 \mid 1101$ | $e_0-e_1+e_{12} \mid 011111 \mid 011101 \mid 111010$ |
| 8 | $e_4 \mid 0111 \mid 0101 \mid 1101$ | $e_{12} \mid 101110 \mid 111110 \mid 011101$ |
| 9 | $e_4 \mid 1011 \mid 0011 \mid 0111$ | $e_0-e_1+e_{12} \mid 110001 \mid 111111 \mid 001111$ |
| 10 | $e_4-e_0+e_9 \mid 1101 \mid 0101 \mid 0111$ | $e_6 \mid 110111 \mid 010111 \mid 101110$ |
| 11 | $e_0-e_4+e_8 \mid 1101 \mid 1111 \mid 0110$ | $e_6-e_7+e_{12} \mid 110111 \mid 111111 \mid 001011$ |
| 12 | $e_4-e_0+e_9 \mid 1101 \mid 1111 \mid 1010$ | $e_6-e_7+e_{12} \mid 111001 \mid 011111 \mid 110110$ |
| 13 | $e_4 \mid 1110 \mid 0110 \mid 0111$ | $e_6 \mid 111011 \mid 011000 \mid 110111$ |
| 14 | $e_8 \mid 1110 \mid 0110 \mid 0111$ | $e_6 \mid 111101 \mid 001111 \mid 111010$ |
| 15 | $e_0-e_4+e_8 \mid 1111 \mid 1101 \mid 0101$ | $e_0-e_1+e_{12} \mid 111111 \mid 100000 \mid 011111$ |
| 16 | $e_4-e_0+e_9 \mid 1111 \mid 1101 \mid 1001$ | $e_{12} \mid 111111 \mid 100011 \mid 010111$ |

*Table 5: Complete explicit $\mathbb{Z}_4$-circulant orbit generators for $\mathrm{DSRG}(64, 44, 33, 29, 33)$ ($r=8, q=4, w=2, L=11$) and $\mathbb{Z}_6$-circulant orbit generators for $\mathrm{DSRG}(96, 68, 51, 47, 51)$ ($r=12, q=6, w=2, L=17$).* $\square$

---

---

## 5. Higher-Block and Parity-Gadget Duality Looms

The Hadamard-Simplex and Root-Difference Simplex architectures of Sections 3 and 4 operate primarily on $2$-block hyperplanes where the head coordinates require negative diagonal entries and the tail coordinates provide positive balancing entries. However, several critical open parameter sets in Hobart and Brouwer's catalog [2] possess arithmetic obstructions to $2$-block syntheses, or require higher rank and denominator structures. In this section, we establish four new structural and obstruction theorems that resolve these challenges, yielding $8$ additional newly resolved open catalog parameter sets ($4$ complementary pairs) and independent outer-product syntheses of $4$ comparison parameter sets.

### 5.1 The Dual Affine-Hyperplane and Column-Sum Divisibility Law

We first establish a fundamental duality law connecting the row sums of $B$, the column sums of $B$, and the exact arithmetic divisibility of the hyperplane denominator $L$.

### Theorem 5.1 (Dual Affine-Hyperplane and Column-Sum Divisibility Law)
*Let $g \ge 2$, $n := g + 1$, $d \ge 1$, $\mu \ge d$, $v = \frac{g(g+1)d^2}{\mu}$, and $k = gd$. Let $\alpha = \frac{1}{L}(a_1, \dots, a_n)^T \in \mathbb{Q}^n$ with $\gcd(a_1, \dots, a_n, L) = 1$ and $\mathbf{1}_n^T \alpha = v / k$. Let $S \subseteq H_\alpha$ and $B \subseteq \mathcal{B}(S)$ be non-empty sets, and suppose $Z \in \{0,1\}^{v \times n}$ has rows $z^{(x)} \in S$ and $B_{\text{mat}} \in \mathbb{Q}^{v \times n}$ has rows $\beta^{(x)} \in B$ satisfying*
$$
Z^T B_{\text{mat}} = -d I_n + \mu \mathbf{1}_n \alpha^T.
\tag{36}
$$
*Then:*
1. *(Dual Affine-Hyperplane Normalization): The outer-product matrix $M := Z B_{\text{mat}}^T \in \{0,1\}^{v \times v}$ satisfies the $\mathrm{DSRG}$ quadratic equation $M^2 + d M = \mu J_v$ and column-regularity $\mathbf{1}_v^T M = k \mathbf{1}_v^T$ if and only if every active dual vector satisfies the affine-hyperplane equation*
   $$
   \mathbf{1}_n^T \beta^{(x)} = 1 \qquad \forall x \in \{1, \dots, v\}.
   \tag{37}
   $$
2. *(Dual Column-Sum Identity and Divisibility Law): Left-multiplying Eq. (36) by $\alpha^T$ yields the exact column sums of $B_{\text{mat}}$:*
   $$
   \mathbf{1}_v^T B_{\text{mat}} = k \alpha^T = \frac{k}{L}(a_1, \dots, a_n).
   \tag{38}
   $$
   *If $D \in \mathbb{Z}_{\ge 1}$ is a common denominator for the active dual vectors ($b^{(x)} := D \beta^{(x)} \in \mathbb{Z}^n$), then both $D(Z^T B_{\text{mat}}) \in \mathbb{Z}^{n \times n}$ and $D(\mathbf{1}_v^T B_{\text{mat}}) \in \mathbb{Z}^n$ are integer arrays, which forces the strengthened divisibility law:*
   $$
   L \;\Big|\; D \cdot \gcd(k, \mu).
   \tag{39}
   $$
3. *(Critical Parameter Ratio and Positive-Weight Denominator Obstruction): Define the critical parameter ratio*
   $$
   \rho(v, k, \mu, d) := \frac{\mu}{\gcd(k, \mu) d} \in \mathbb{Q}_{> 0}.
   \tag{40}
   $$
   *Any positive-weight hyperplane ($a_j \ge 1$ for all $j \in \{1, \dots, n\}$) has average coordinate weight*
   $$
   \bar{a} := \frac{1}{n}\sum_{j=1}^n a_j = \frac{L d}{\mu} \le \frac{D}{\rho}.
   \tag{41}
   $$
   *Consequently: (i) A constant positive-weight hyperplane $\alpha = \frac{1}{L}\mathbf{1}_n$ requires $\rho \mid D$; (ii) A non-constant positive-weight hyperplane requires $\max_j a_j \ge 2$, hence $\bar{a} > 1$, which forces $D > \rho$. In particular, any parameter set with $\rho > 1$ is strictly obstructed from admitting a positive-weight outer-product synthesis at dual denominator $D = 1$.*

#### Proof
**Part 1:** Since $z^{(x)} \in H_\alpha \implies (z^{(x)})^T \alpha = 1$, we have $Z \alpha = \mathbf{1}_v$. Then
$$
M \mathbf{1}_v = Z B_{\text{mat}}^T (Z \alpha) = Z (Z^T B_{\text{mat}})^T \alpha = Z (-d I_n + \mu \alpha \mathbf{1}_n^T)\alpha = g d Z \alpha = k \mathbf{1}_v,
$$
so row-regularity holds identically. For the column sums, $\mathbf{1}_v^T M = (\mathbf{1}_v^T Z) B_{\text{mat}}^T$. If $\mathbf{1}_n^T \beta^{(x)} = 1$ for all $x$, then $B_{\text{mat}} \mathbf{1}_n = \mathbf{1}_v$, which gives $\mathbf{1}_v^T M = \mathbf{1}_n^T B_{\text{mat}}^T Z B_{\text{mat}}^T = \mathbf{1}_n^T (-d I_n + \mu \alpha \mathbf{1}_n^T)^T B_{\text{mat}}^T = k \mathbf{1}_v^T$. Conversely, if $\mathbf{1}_v^T M = k \mathbf{1}_v^T$ and $M^2 + d M = \mu J_v$, multiplying $Z(B_{\text{mat}}^T Z + d I_n)B_{\text{mat}}^T = \mu \mathbf{1}_v \mathbf{1}_v^T$ and using the full column rank of $Z$ forces $B_{\text{mat}} \mathbf{1}_n = \mathbf{1}_v$.

**Part 2:** Since every row $z^{(x)}$ of $Z$ satisfies $(z^{(x)})^T \alpha = 1$, we have $\alpha^T Z^T = (Z \alpha)^T = \mathbf{1}_v^T$. Multiplying Eq. (36) on the left by $\alpha^T$ gives
$$
\mathbf{1}_v^T B_{\text{mat}} = \alpha^T (-d I_n + \mu \mathbf{1}_n \alpha^T) = -d \alpha^T + \mu(\alpha^T \mathbf{1}_n)\alpha^T = \Bigl(-d + \mu \frac{n d}{\mu}\Bigr)\alpha^T = (n - 1)d \alpha^T = k \alpha^T.
$$
Since $D B_{\text{mat}} \in \mathbb{Z}^{v \times n}$, the vector $D(\mathbf{1}_v^T B_{\text{mat}}) = \frac{D k}{L} a^T$ must be an integer vector. Since $\gcd(a_1, \dots, a_n, L) = 1$, Bézout's identity forces $L \mid D k$. Combining with Proposition 2.2(1) ($L \mid D \mu$) establishes $L \mid D \cdot \gcd(k, \mu)$.

**Part 3:** Since $\mathbf{1}_n^T \alpha = \frac{n d}{\mu}$, the sum of weights is $\sum_{j=1}^n a_j = \frac{L n d}{\mu}$, so $\bar{a} = \frac{L d}{\mu}$. By Part 2, $L \le D \cdot \gcd(k, \mu)$, which gives $\bar{a} \le \frac{D \gcd(k, \mu) d}{\mu} = \frac{D}{\rho}$. If $a_j \ge 1$ for all $j$, then $\bar{a} \ge 1$. If $\alpha$ is constant, $a_j = \bar{a} = 1$, so $\frac{L d}{\mu} = 1 \implies L = \frac{\mu}{d}$; then $L \mid D \gcd(k, \mu) \implies \frac{\mu}{d} \mid D \gcd(k, \mu) \implies \rho \mid D$. If $\alpha$ is non-constant with $a_j \ge 1$, then at least one coordinate exceeds $1$, so $\bar{a} > 1$, which forces $\frac{D}{\rho} \ge \bar{a} > 1 \implies D > \rho$. $\square$

*Obstruction Census:* Across the $16$ catalog parameter sets with $t = \mu$ having $\rho > 1$ (including $\mathrm{DSRG}(28, 21, 18, 15, 18)$ with $\rho = 2$, $\mathrm{DSRG}(98, 70, 55, 48, 55)$ with $\rho = 11/7$, $\mathrm{DSRG}(66, 55, 50, 45, 50)$ with $\rho = 10/7$, and $\mathrm{DSRG}(91, 52, 32, 28, 32)$ with $\rho = 2$), Theorem 5.1(3) rigorously proves that no positive-weight outer-product synthesis can exist at $D = 1$. All $16$ bounds are verified in `verify_all.py`.

---

### 5.2 The Neutral-Pivot 3-Block Bypass Loom ($D = 1$)

When $L \mid \gcd(k, \mu)$ ($D = 1$) and the average coordinate weight $\bar{a} := \frac{L d}{\mu}$ is an integer $\ge 2$, the diagonal entry of the target matrix $-d I_n + \mu \mathbf{1}_n \alpha^T$ on any coordinate with weight $\bar{a}$ vanishes identically:
$$
T_{j, j} = -d + \frac{\mu \bar{a}}{L} = -d + d = 0.
$$
This motivates our third architecture: the **Neutral-Pivot 3-Block Bypass Loom**.

### Theorem 5.2 (Neutral-Pivot 3-Block Bypass Loom)
*Let $n = r_1 + r_2 + r_3$ with $r_1, r_2, r_3 \ge 1$ and $n \mid v$. Suppose $L \mid \gcd(k, \mu)$ and $\bar{a} = \frac{L d}{\mu} \in \mathbb{Z}_{\ge 2}$. Define the 3-block hyperplane*
$$
\alpha = \frac{1}{L}\Bigl(\underbrace{a_1, \dots, a_1}_{r_1},\; \underbrace{\bar{a}, \dots, \bar{a}}_{r_2},\; \underbrace{a_3, \dots, a_3}_{r_3}\Bigr)^T \in \mathbb{Q}^n,
\tag{42}
$$
*where $a_1 < \bar{a} < a_3$ and $r_1(\bar{a} - a_1) = r_3(a_3 - \bar{a})$. Then:*
1. *On Block 2 ($B_2$, coordinates $r_1 \le j < r_1 + r_2$), the target matrix diagonal vanishes: $T_{j, j} = 0$.*
2. *Because $k \alpha_j = \frac{k \bar{a}}{L} = \frac{v}{n} \in \mathbb{Z}$, the target column sum on each coordinate of Block 2 can be saturated entirely by standard basis vectors $e_j$.*
3. *All non-basis root-difference dual vectors $\beta^{(h)} = e_{i_h} - e_h + e_{r_1 + r_2 + \ell}$ couple head coordinates $h \in \{0, \dots, r_1-1\}$ (where $T_{h, h} < 0$) directly to tail coordinates $r_1 + r_2 + \ell \in \{r_1 + r_2, \dots, n-1\}$ (where $T_{\ell, \ell} > 0$), bypassing the neutral pivot block $B_2$ completely.*

*Consequently, the following two open catalog parameter sets (and their complements) admit exact integer outer-product syntheses at $D = 1$:*
- **$\mathrm{DSRG}(99, 30, 10, 7, 10)$** and **$\mathrm{DSRG}(99, 68, 48, 47, 46)$** ($g = 10$, Rank $11$, $d = 3, \mu = 10$): realized on $\alpha = \frac{1}{10}(2^4, 3^3, 4^4)^T$ ($r_1 = 4, r_2 = 3, r_3 = 4, \bar{a} = 3$), with active support $|S| = 24$, $|B| = 15$, and $75$ orthogonal pairs.
- **$\mathrm{DSRG}(88, 60, 45, 39, 45)$** and **$\mathrm{DSRG}(88, 27, 12, 11, 7)$** ($g = 10$, Rank $11$, $d = 6, \mu = 45$): realized on $\alpha = \frac{1}{15}(1^4, 2^3, 3^4)^T$ ($r_1 = 4, r_2 = 3, r_3 = 4, \bar{a} = 2$), with active support $|S| = 39$, $|B| = 15$, and $52$ orthogonal pairs.

#### Proof
By Theorem 5.1, the column sums of $B$ are $\frac{k}{L} a_j$. On Block 2, $a_j = \bar{a} = \frac{L d}{\mu}$, so $\frac{k}{L}\bar{a} = \frac{k d}{\mu} = \frac{g d^2}{\mu} = \frac{v}{g+1} = \frac{v}{n} \in \mathbb{Z}$ since $n \mid v$ ($11 \mid 99$ and $11 \mid 88$). Assigning multiplicity $\frac{v}{n}$ to each standard basis vector $e_j$ ($r_1 \le j < r_1 + r_2$) exactly matches both the diagonal $T_{j, j} = 0$ (since $z_j = 0$ on all orthogonal pairs with $e_j$) and the column sum $\mathbf{1}_v^T B e_j = \frac{v}{n}$. Head coordinates $h < r_1$ have $T_{h, h} = -d + \frac{\mu a_1}{L} < 0$, which are covered by root differences $e_{i_h} - e_h + e_{r_1+r_2+\ell}$ into Block 3, where $T_{\ell, \ell} > 0$. The explicit factorizations for both graphs are verified in `verify_all.py`. $\square$

---

#### 5.3 The $\mathbb{F}_2$-Nullspace Rank Law and Even-Rank-$r$ Hadamard-Simplex Loom ($D = 2$)

When $D = 2$, each scaled dual vector $b = 2\beta \in \mathbb{Z}^n$ satisfies $\mathbf{1}_n^T b = 2$. Reducing the matrix factorization modulo $2$ uncovers a sharp linear-algebraic parity structure:

### Theorem 5.3 ($\mathbb{F}_2$-Nullspace Rank Law and Even-Rank-$r$ Hadamard-Simplex Loom)
*Let $(S, B, N)$ be a $D = 2$ outer-product synthesis of a $\mathrm{DSRG}(v, gd, \mu, \mu - d, \mu)$ with adjacency matrix $A = C R \in \{0, 1\}^{v \times v}$. Then:*
1. *($\mathbb{F}_2$-Orthogonality): Let $\bar{Z} \in \mathbb{F}_2^{v \times n}$ and $\bar{B} \in \mathbb{F}_2^{v \times n}$ be the binary reductions of $C$ and $2R^T$. Because $2A = C(2R^T)^T \in \{0, 2\}^{v \times v}$, reducing modulo $2$ gives*
   $$
   \bar{Z} \bar{B}^T = 0 \in \mathbb{F}_2^{v \times v}, \qquad \text{whence} \qquad \operatorname{rank}_{\mathbb{F}_2}(\bar{Z}) + \operatorname{rank}_{\mathbb{F}_2}(\bar{B}) \le n.
   \tag{43}
   $$
2. *(Dual Parity Alignment): If $L$ is even and every dual vector $b \in 2B$ with odd entries satisfies $b \equiv (a_1, \dots, a_n) \pmod 2$, then every odd row of $\bar{B}$ equals $(a \bmod 2)$, so $\operatorname{rowspace}_{\mathbb{F}_2}(\bar{B}) = \operatorname{span}_{\mathbb{F}_2}(a \bmod 2)$ has dimension $\operatorname{rank}_{\mathbb{F}_2}(\bar{B}) \le 1$. Since $\bar{Z}(a \bmod 2) \equiv L \mathbf{1}_v \equiv \mathbf{0}_v \pmod 2$, this parity alignment ensures that every vector in the candidate pool satisfies the parity condition $b^T z \in 2\mathbb{Z}$ for all $z \in H_\alpha$.*
3. *(Pre-Filtered Compatible Slice and Even-Rank-$r$ Architecture): For an even head size $r = 2m$ with odd weight $a_1$ and tail size $q$ with even weight $a_2$, every $z \in H_\alpha$ has even head weight $s_{\text{head}}(z) \in \{0, 2, \dots, 2m\}$, ensuring that inner products with candidate dual vectors are even integers. Because inner products can take values in $2\mathbb{Z} \setminus \{0, 2\}$ on general elements of $H_\alpha$, synthesis requires restricting $H_\alpha$ to the pre-filtered compatible slice $S_{\text{compat}}(B_{\text{tmpl}}) = \{z \in H_\alpha : b^T z \in \{0, 2\} \;\forall b \in B_{\text{tmpl}}\}$ via Proposition 2.3(2).*

*Applying this architecture with $r = 6, q = 9, L = 14$ on the pre-filtered slice $S_{\text{compat}}(B_{\text{tmpl}})$ under $\mathbb{Z}_3$-equivariant orbit reduction yields an exact outer-product synthesis of:*
- **$\mathrm{DSRG}(96, 56, 35, 31, 35)$** and **$\mathrm{DSRG}(96, 39, 18, 17, 15)$** ($g = 14$, Rank $15$, $d = 4, \mu = 35$): realized on $\alpha = \frac{1}{14}(1^6, 2^9)^T$, using the $31$ explicit $\mathbb{Z}_3$-orbit generators listed in Table 6.

| # | $N$ | $z_{\text{head}} \mid z_{\text{tail}}$ | $2\beta \in \mathbb{Z}^{15}$ | # | $N$ | $z_{\text{head}} \mid z_{\text{tail}}$ | $2\beta \in \mathbb{Z}^{15}$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1 | `000101` $\mid$ `101101011` | $(-1,1,1,1,1,-1;\mathbf{0}_9)$ | 17 | 1 | `101101` $\mid$ `010101011` | $2e_{8}$ |
| 2 | 1 | `000101` $\mid$ `110101011` | $2e_{8}$ | 18 | 1 | `101101` $\mid$ `110101100` | $(-1,-1,-1,1,1,1;0,0,0,0,2,0,0,0,0)$ |
| 3 | 1 | `010001` $\mid$ `111100110` | $2e_{11}$ | 19 | 2 | `101101` $\mid$ `111011000` | $2e_{14}$ |
| 4 | 1 | `010010` $\mid$ `010011111` | $2e_{8}$ | 20 | 1 | `101110` $\mid$ `101011010` | $2e_{5}$ |
| 5 | 1 | `010010` $\mid$ `010111110` | $2e_{14}$ | 21 | 1 | `110101` $\mid$ `010010111` | $(-1,-1,1,1,1,-1;0,0,0,0,0,0,2,0,0)$ |
| 6 | 1 | `010010` $\mid$ `101110101` | $2e_{11}$ | 22 | 1 | `110101` $\mid$ `011100101` | $(-1,-1,1,1,1,-1;0,2,0,0,0,0,0,0,0)$ |
| 7 | 1 | `010010` $\mid$ `111110001` | $2e_{5}$ | 23 | 1 | `110110` $\mid$ `001101011` | $2e_{5}$ |
| 8 | 1 | `011011` $\mid$ `110110010` | $(-1,-1,1,1,1,-1;0,0,0,0,0,0,2,0,0)$ | 24 | 1 | `110110` $\mid$ `100111001` | $2e_{8}$ |
| 9 | 1 | `011101` $\mid$ `111000011` | $2e_{4}$ | 25 | 1 | `110110` $\mid$ `101100110` | $(-1,-1,-1,1,1,1;0,0,0,0,2,0,0,0,0)$ |
| 10 | 1 | `100100` $\mid$ `001111110` | $2e_{4}$ | 26 | 1 | `110110` $\mid$ `110010011` | $(-1,-1,1,1,1,-1;0,0,0,0,0,0,2,0,0)$ |
| 11 | 1 | `100100` $\mid$ `110100111` | $2e_{5}$ | 27 | 1 | `111010` $\mid$ `001111010` | $(-1,-1,-1,1,1,1;0,0,0,0,2,0,0,0,0)$ |
| 12 | 1 | `100100` $\mid$ `111010110` | $2e_{11}$ | 28 | 1 | `111010` $\mid$ `011010110` | $2e_{14}$ |
| 13 | 1 | `101000` $\mid$ `010111110` | $(-1,1,1,1,1,-1;\mathbf{0}_9)$ | 29 | 1 | `111111` $\mid$ `000001111` | $(-1,-1,-1,1,1,1;0,0,0,0,2,0,0,0,0)$ |
| 14 | 1 | `101011` $\mid$ `100101101` | $(-1,-1,1,1,1,-1;0,2,0,0,0,0,0,0,0)$ | 30 | 1 | `111111` $\mid$ `101010001` | $(-1,-1,1,1,1,-1;0,2,0,0,0,0,0,0,0)$ |
| 15 | 1 | `101011` $\mid$ `100110101` | $2e_{8}$ | 31 | 1 | `111111` $\mid$ `110000011` | $(-1,-1,-1,1,1,1;0,0,0,0,2,0,0,0,0)$ |
| 16 | 1 | `101101` $\mid$ `001111001` | $(-1,-1,1,1,1,-1;0,0,0,0,0,0,2,0,0)$ | | | | |

*Table 6: The 31 explicit $\mathbb{Z}_3$-orbit generators for $\mathrm{DSRG}(96, 56, 35, 31, 35)$ on $\alpha = \frac{1}{14}(1^6, 2^9)^T$. Expanding each generator under the $\mathbb{Z}_3$ action (shifting the head by $+2 \bmod 6$ and each of the three tail blocks of size $3$ by $+1 \bmod 3$) yields the full $96$-vertex synthesis.* $\square$

---

### 5.4 The 3-Vector Parity-Gadget Decomposition ($D = 2$)

When $L \mid \mu$, $L \nmid k$, and $L \mid 2k$ ($D = 2$), the scaled target matrix $2T = 2(-d I_n + \frac{\mu}{L}\mathbf{1}_n a^T)$ is an even integer matrix, while the required total scaled-dual multiplicity sums across all $v$ vertices (Theorem 5.1(2)),
$$
\mathbf{1}_v^T (2B_{\text{mat}}) = \frac{2k}{L}(a_1, \dots, a_n),
$$
have odd parity $\frac{2k a_j}{L} \equiv a_j \pmod 2$ on coordinates $j$ where $a_j$ is odd. This parity discrepancy cannot be satisfied if all $v$ vertices use scaled dual vectors with even entries ($2\beta \in 2\mathbb{Z}^n$).

### Theorem 5.4 (3-Vector Parity-Gadget Decomposition)
*Suppose $L \mid \mu$, $L \nmid k$, and $L \mid 2k$ ($D = 2$). Let $\{b_{\text{odd}}^{(1)}, b_{\text{odd}}^{(2)}, b_{\text{odd}}^{(3)}\} \subset \mathbb{Z}^n$ be three dual vectors satisfying $b_{\text{odd}}^{(m)} \equiv a \pmod 2$ and $\mathbf{1}_n^T b_{\text{odd}}^{(m)} = 2$. Suppose there exist three slice vectors $z^{(1)}, z^{(2)}, z^{(3)} \in H_\alpha$ such that*
$$
(b_{\text{odd}}^{(m)})^T z^{(m)} = 0 \quad (m \in \{1,2,3\}), \qquad \text{and} \qquad z^{(1)} + z^{(2)} + z^{(3)} \equiv \mathbf{0}_n \pmod 2.
\tag{44}
$$
*Then:*
1. *(Even Gadget Matrix): The parity gadget matrix $G := \sum_{m=1}^3 z^{(m)} (b_{\text{odd}}^{(m)})^T$ lies in $2\mathbb{Z}^{n \times n}$, because for every entry $(i, j)$:*
   $$
   G_{i, j} = \sum_{m=1}^3 z_i^{(m)} (b_{\text{odd}}^{(m)})_j \equiv a_j \sum_{m=1}^3 z_i^{(m)} \equiv 0 \pmod 2.
   $$
   *Consequently, $T - \frac{1}{2}G = -d I_n + \frac{\mu}{L}\mathbf{1}_n a^T - \frac{1}{2}G \in \mathbb{Z}^{n \times n}$ has integer entries.*
2. *(Residual Dual Multiplicity Parity): The required residual scaled-dual multiplicity sum for the remaining $v - 3$ vertices is*
   $$
   \sum_{x=4}^v (2\beta^{(x)})_j = \frac{2k a_j}{L} - \sum_{m=1}^3 (b_{\text{odd}}^{(m)})_j \equiv a_j - 3 a_j = -2 a_j \equiv 0 \pmod 2 \qquad \forall j \in \{1, \dots, n\}.
   \tag{45}
   $$
   *This residual sum is an even integer on every coordinate $j$, matching the parity requirement for the remaining $v - 3$ vertices to be represented by scaled dual vectors with even entries ($2\beta^{(x)} \in 2\mathbb{Z}^n$, corresponding to integer duals $\beta^{(x)} \in \mathbb{Z}^n$).*
3. *(Jointly Compatible Slice Formulation): To ensure that $A = C R \in \{0, 1\}^{v \times v}$ is binary, all $v$ vertices (both the 3 gadget pairs and the $v - 3$ residual pairs) must be chosen from the pre-filtered jointly compatible slice*
   $$
   S_{\text{compat}}\bigl(B_{\text{even}} \cup \{\tfrac{1}{2}b_{\text{odd}}^{(m)}\}_{m=1}^3\bigr) = \bigl\{z \in H_\alpha : b^T z \in \{0, 2\} \;\;\forall b \in 2B_{\text{even}} \cup \{b_{\text{odd}}^{(m)}\}_{m=1}^3\bigr\}.
   $$
   *Feasibility of the residual integer system on this compatible slice is certified for our target instances by explicit solutions.*

*Applying Theorem 5.4 yields exact outer-product syntheses for:*
- **$\mathrm{DSRG}(108, 45, 20, 17, 20)$** and **$\mathrm{DSRG}(108, 62, 37, 36, 35)$** ($g = 15$, Rank $16$, $d = 3, \mu = 20$): realized on $\alpha = \frac{1}{10}(1^8, 2^8)^T$, with active support $|S| = 84$, $|B| = 27$, and $106$ pairs.
- **$\mathrm{DSRG}(91, 39, 18, 15, 18)$** and complement ($g = 13$, Rank $14$): realized on $\alpha = \frac{1}{6}\mathbf{1}_{14}^T$, with $|S| = 71, |B| = 24, 88$ pairs.
- **$\mathrm{DSRG}(91, 52, 32, 28, 32)$** and complement ($g = 13$, Rank $14$): realized on $\alpha = \frac{1}{8}\mathbf{1}_{14}^T$, with $|S| = 68, |B| = 24, 86$ pairs.

| Graph | Hyperplane $\alpha$ | Gadget Triples $(z^{(m)}, 2\beta^{(m)})$ for $m \in \{1, 2, 3\}$ |
| :--- | :--- | :--- |
| $\mathrm{DSRG}(108, 45, 20, 17, 20)$ | $\frac{1}{10}(\mathbf{1}_8, 2\mathbf{1}_8)$ | $z^{(1)} = `0000110001101100`, \;\; 2\beta^{(1)} = (1, 1, 1, 1, 1, -1, -1, -1; \mathbf{0}_8)$<br>$z^{(2)} = `1000010011000110`, \;\; 2\beta^{(2)} = (-1, 1, 1, 1, 1, 1, -1, -1; \mathbf{0}_8)$<br>$z^{(3)} = `1000100010101010`, \;\; 2\beta^{(3)} = (-1, -1, 1, 1, 1, 1, 1, -1; \mathbf{0}_8)$ |
| $\mathrm{DSRG}(91, 39, 18, 15, 18)$ | $\frac{1}{6}\mathbf{1}_{14}$ | $z^{(1)} = `11000001110010`, \;\; 2\beta^{(1)} = (\mathbf{1}_8, -\mathbf{1}_6)$<br>$z^{(2)} = `10110001011000`, \;\; 2\beta^{(2)} = (\mathbf{1}_7, -1, 1, -\mathbf{1}_5)$<br>$z^{(3)} = `01110000101010`, \;\; 2\beta^{(3)} = (\mathbf{1}_7, -1, -1, 1, -\mathbf{1}_4)$ |
| $\mathrm{DSRG}(91, 52, 32, 28, 32)$ | $\frac{1}{8}\mathbf{1}_{14}$ | $z^{(1)} = `01111000111100`, \;\; 2\beta^{(1)} = (\mathbf{1}_8, -\mathbf{1}_6)$<br>$z^{(2)} = `11100011011001`, \;\; 2\beta^{(2)} = (\mathbf{1}_7, -1, 1, -\mathbf{1}_5)$<br>$z^{(3)} = `10011011100101`, \;\; 2\beta^{(3)} = (\mathbf{1}_7, -1, -1, 1, -\mathbf{1}_4)$ |

*Table 7: Explicit 3-vector parity gadgets for $\mathrm{DSRG}(108, 45, 20, 17, 20)$ and the two constant-hyperplane $v = 91$ graphs. In each case, $z^{(1)} \oplus z^{(2)} \oplus z^{(3)} = \mathbf{0}_n$, absorbing the odd parity in dual column sums.* $\square$

---

## 6. Exact Computational Verification Suite

All results in this paper are accompanied by a self-contained, zero-floating-point verification package in `supplement.zip`. Running
```bash
python3 verify_all.py
```
executes in **0.49 seconds** using 100% pure Python exact integer and rational (`fractions.Fraction`) arithmetic with zero third-party dependencies, performing eight independent checks on every one of the $32$ primary infinite families ($64$ explicit $\mathrm{DSRG}$s: the $38$ newly resolved open catalog parameter sets of Table 1 and the $26$ comparison parameter sets of Table 2):
1. **Hyperplane Slice Membership:** Verifies $z \in \{0,1\}^n \setminus \{\mathbf{0}, \mathbf{1}\}$ and $\sum_{j=0}^{n-1} a_j z_j = L$ for every active $z \in S$.
2. **Dual Normalization:** Verifies $2\beta \in \mathbb{Z}^n$ and $\sum_{j=0}^{n-1} (2\beta)_j = 2$ for every active $2\beta \in 2B$.
3. **Active Orthogonality:** Verifies $(2\beta)^T z = 0$ for every active pair $(z, 2\beta)$ with $N(z, \beta) > 0$, confirming $\operatorname{diag}(C R) = \mathbf{0}_v$.
4. **Full Bipartite $\{0,1\}$-Compatibility:** Verifies $(2\beta)^T z' \in \{0, 2\}$ for **all** active $z' \in S$ and **all** active $2\beta \in 2B$, confirming $A = C R \in \{0,1\}^{v \times v}$.
5. **Exact Rank-$(g+1)$ Outer-Product Identity:** Verifies $L \sum_{(z, 2\beta)} N(z, \beta) z (2\beta)^T = 2(-d L I_n + \mu \mathbf{1}_n a^T)$ entrywise in $\mathbb{Z}^{n \times n}$.
6. **Dual Column-Sum Identity:** Verifies $L \sum_{(z, 2\beta)} N(z, \beta) (2\beta)_j = 2 k a_j$ entrywise for all $j \in \{0, \dots, n-1\}$, confirming Theorem 5.1(2).
7. **Direct $v \times v$ Adjacency Matrix Verification:** Reconstructs the explicit $v \times v$ $(0,1)$-matrices $A = C R$ and $A^c = J_v - I_v - A$ and verifies directly via exact integer matrix multiplication that $A$ and $A^c$ have zero diagonal, constant row and column sums $k$ and $k^c$, and satisfy $A^2 = t I_v + \lambda A + \mu(J_v - I_v - A)$ and $(A^c)^2 = t^c I_v + \lambda^c A^c + \mu^c(J_v - I_v - A^c)$.
8. **Theorem 5.1 Denominator Obstruction Bounds:** Verifies the nonexistence of positive-weight $D = 1$ hyperplanes across all $16$ catalog parameter sets with $\rho > 1$.

---

## References

1. A. M. Duval, "A directed graph version of strongly regular graphs," *Journal of Combinatorial Theory, Series A*, vol. 47, no. 1, pp. 71–100, 1988.
2. S. A. Hobart and A. E. Brouwer, "Parameters of directed strongly regular graphs," online catalog (archived local snapshot in `data_tables/dsrg_Hobart_Brouwer`).
3. A. E. Brouwer, "Parameters of Strongly Regular Graphs," online catalog (archived local snapshot in `data_tables/srg_Brouwer`).
4. F. Fiedler, M. H. Klin, and M. Muzychuk, "Small vertex-transitive directed strongly regular graphs," *Discrete Mathematics*, vol. 255, no. 1–3, pp. 87–115, 2002.
5. A. E. Brouwer and H. Van Maldeghem, *Strongly Regular Graphs*, Encyclopedia of Mathematics and its Applications, vol. 182, Cambridge University Press, 2022.
6. C. D. Godsil, S. A. Hobart, and W. J. Martin, "Representations of directed strongly regular graphs," *European Journal of Combinatorics*, vol. 28, no. 7, pp. 1980–1993, 2007.
7. S. Gyürki and M. Klin, "Sporadic directed strongly regular graphs on 36 vertices," *Art Discrete Appl. Math.*, 2020.
8. L. K. Jørgensen, "Directed strongly regular graphs with $\mu = \lambda$," *Discrete Mathematics*, vol. 231, pp. 289–293, 2001.
9. M. Klin, A. Munemasa, M. Muzychuk, and P.-H. Zieschang, "Directed strongly regular graphs obtained from coherent configurations," *Linear Algebra and its Applications*, vol. 377, pp. 83–109, 2004.
10. L. K. Jørgensen, "Rank of adjacency matrices of directed (strongly) regular graphs," *Linear Algebra and its Applications*, vol. 407, pp. 233–241, 2005.
11. `mira_loom`, "Existence of DSRGs $(32+8s,14+4s,7+2s,5+2s,7+2s)$ and $(108+27s,33+9s,11+3s,8+3s,11+3s)$," rStation paper `strongly_regular_graphs_1`, 2026.
12. `teichmuller_lift`, "Existence of directed strongly regular graphs with parameters $(57,22,14,9,8)$ and $(93,34,18,13,12)$," rStation paper `strongly_regular_graphs_2`, 2026; and "Existence of an infinite family of directed strongly regular graphs with parameters $(mq, q+2m-3, n+4m-4, n+2m-3, n+2)$, $q = 1+nm$," rStation paper `strongly_regular_graphs_3`, 2026.
13. `mira_loom`, "Existence of DSRGs $(45,18,8,6,8)$ and 21 further complement classes via nets and equitable partitions," rStation paper `strongly_regular_graphs_4`, 2026.
14. `kirkman_loom`, "Nonexistence of 42 Open Directed Strongly Regular Graphs via Rank-6 and Rank-7 Hyperplane Duality, Existence of DSRG(64,14,7,3,3) and DSRG(80,18,8,4,4), and Closed-Form Abelian Group-Ring Families," rStation paper `strongly_regular_graphs_5`, 2026.
15. `teichmuller_lift`, "Existence of directed strongly regular graphs with parameters $(72,27,19,10,10)$, $(72,32,23,13,15)$, $(58,26,18,11,12)$, $(82,37,29,16,17)$ and $(106,49,35,22,23)$," rStation paper `strongly_regular_graphs_6`, 2026.
16. `mira_loom`, "Nonexistence of DSRGs $(50,35,28,23,28)$, $(72,21,7,4,7)$, $(81,24,8,5,8)$, $(81,63,56,47,56)$, $(96,80,75,65,75)$, $(100,35,14,9,14)$ and all positive multiples," rStation paper `strongly_regular_graphs_7`, 2026.
17. `mira_loom`, "Existence of every feasible DSRG$(v,k,\mu,\mu-1,\mu)$, plus fifteen parameter sets: 33 complementary pairs," rStation forum post `UQwVXzrjRmYjr1pV` in `r/strongly_regular_graphs`, Oct 2026.
18. V. Mikulić Crnković and M. Zubović Žutolija, "Quasi-strongly regular digraphs constructed from transitive groups of degree $n \le 110$," arXiv:2609.10075v1, Sep 2026.
19. `mira_loom`, "DSRG existence: all feasible $(v, k, \mu, \mu-1, \mu)$, plus fifteen parameter sets: 33 complementary pairs," rStation paper `strongly_regular_graphs_9`, 2026.
20. `teichmuller_lift`, "Existence of an infinite family of directed strongly regular graphs on $2p$ vertices for primes $p = n^2+4$, including $(58,26,18,11,12)$ and $(106,49,35,22,23)$," rStation paper `strongly_regular_graphs_10`, 2026.
21. `mira_loom`, "Nonexistence of DSRGs $(28m,21m,18m,15m,18m)$ for every odd $m$: $(28,6,3,2,1)$, $(28,21,18,15,18)$, $(84,20,11,10,3)$, and $(84,63,54,45,54)$," rStation paper `strongly_regular_graphs_11`, 2026.

