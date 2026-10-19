# Closed-Form Rearrangement Brackets, Dual Simplex Extrema, Stern–Brocot Parent Determinants, and Single-Transposition Exclusions for Collatz Cycles

## 1. Introduction and Contribution

The Collatz ($3x+1$) conjecture asserts that the iterative arithmetic map $T: \mathbb{Z}_{\ge 1} \to \mathbb{Z}_{\ge 1}$ defined by
$$
T(n) = \begin{cases} n/2, & n \equiv 0 \pmod 2, \\ 3n+1, & n \equiv 1 \pmod 2 \end{cases}
$$
eventually reaches $1$ from every positive integer starting value. On the set of odd integers $\mathbb{Z}_{\ge 1}^{\mathrm{odd}}$, the dynamics are conventionally accelerated by the Syracuse map
$$
U(x) = \frac{3x+1}{2^{v_2(3x+1)}}.
$$
Under $U$, a putative non-trivial cycle of length $k$ is an orbit of odd integers $x_0, x_1, \dots, x_{k-1}$ such that $x_{j+1} = U(x_j)$ with $x_k = x_0$. Let $a_j = v_2(3x_j + 1) \ge 1$ denote the $2$-adic valuation at step $j$, and let $S_j = \sum_{i=0}^{j-1} a_i$ be the cumulative valuation (with $S_0 = 0$ and total division count $S = S_k = \sum_{j=0}^{k-1} a_j$). Unrolling the recurrence $2^{a_j} x_{j+1} = 3 x_j + 1$ over $k$ steps yields the fundamental Syracuse Diophantine identity:
$$
(2^S - 3^k) x_0 = C(a), \quad \text{where} \quad C(a) = \sum_{j=0}^{k-1} 3^{k-1-j} 2^{S_j}.
$$
Because $x_0 \ge 1$, any non-trivial positive cycle requires $2^S > 3^k$, which forces $S/k > \log_2 3 \approx 1.58496$.

Mathematical research on hypothetical Collatz cycles has developed along two complementary lines:
1. **Archimedean Ratio and Balanced-Word Bounds (Crandall–Garner–Eliahou, Halbeisen–Hungerbühler, Fernández–Ibáñez, and Knight Theory):** Using the product identity
   $$
   \frac{2^S}{3^k} = \prod_{j=0}^{k-1} \left(1 + \frac{1}{3x_j}\right),
   $$
   Crandall [1], Garner [2], and Eliahou [3] established that any cycle minimum element $x_{\min}(a) = \min_{0 \le r < k} x_r(a)$ satisfies
   $$
   x_{\min}(a) \le x_{\min}^{\mathrm{Eliahou}}(k, S) := \frac{1}{2^{S/k} - 3}.
   $$
   In a foundational 1997 work, Halbeisen and Hungerbühler [22] proved that over all parity vectors of length $l = S$ with $n = k$ odd steps, the minimum over cyclic shifts is maximized by the balanced word $s_i = \lceil ik/S \rceil - \lceil (i-1)k/S \rceil$, corresponding in Syracuse valuation coordinates to the lower Christoffel (Sturmian) word $a^{\mathrm{Sturm}}(k, S)$ with cumulative profile $S_j = \lfloor jS/k \rfloor$ and numerator $M_{S,k} = C(a^{\mathrm{Sturm}}(k, S)) = \sum_{j=0}^{k-1} 3^{k-1-j} 2^{\lfloor jS/k \rfloor}$, yielding $x_{\min}(a) \le M_{S,k}/(2^S - 3^k)$. Recently, Fernández and Ibáñez [25, Theorem 7.3] proved that the Christoffel word uniquely maximizes the cyclic minimum up to rotation for all coprime and non-coprime $(k, S)$, while Knight [26, Theorem 5.4] proved that integer "high cycles" (balanced/Christoffel words) do not exist by comparing $M_{S,k}$ with its reversed rotation $N_{\mathrm{rev}}$ via $3 M_{S,k} - N_{\mathrm{rev}} + (2^S - 3^k) = 2^{S-1}$, which together with cyclic shift invariance implies $\gcd(M_{S_0, k_0}, |2^{S_0} - 3^{k_0}|) = 1$.
2. **Diophantine Linear Forms in Logarithms ($m$-Cycle and Local-Minima Theory):** Initiated by Steiner [6] for $1$-cycles, and extended by Simons and de Weger [7] and Hercher [8] to $m$-cycles, this approach rules out non-trivial cycles with $m \le 91$ local minima; furthermore, by combining the $m > 91$ constraint with the product bound, Hercher [8, Section 5, Corollary 29] established that a verification threshold of $X_0 \ge 3 \cdot 2^{69} \approx 2^{70.585}$ suffices to reach the $23$-rd convergent bound $k \ge 137,528,045,312$.

### Open Questions Beyond Prior Balanced-Word Theory

While Halbeisen and Hungerbühler [22], Fernández and Ibáñez [25], and Knight [26] established the cyclic-minimum extremality, uniqueness, and non-integrality of the exact Christoffel word $a^{\mathrm{Sturm}}(k, S)$ on the valuation simplex
$$
\mathcal{A}(k, S) = \left\{ (a_0, \dots, a_{k-1}) \in \mathbb{Z}_{\ge 1}^k : \sum_{j=0}^{k-1} a_j = S \right\},
$$
four concrete analytical and Diophantine questions remain open:
1. **Closed-Form Rearrangement Brackets and the Asymptotic Ratio to Eliahou's Bound:** Direct summation of $M_{S_0, k_0} = \sum_{j=0}^{k_0 - 1} 3^{k_0 - 1 - j} 2^{\lfloor j S_0 / k_0 \rfloor}$ requires $k_0$ terms. Can $x_{\min}(a^{\mathrm{Sturm}}(k, S)) = M_{S,k}/(2^S - 3^k)$ be enclosed in $O(1)$ closed-form elementary brackets $L(k_0, S_0) \le x_{\min}(a^{\mathrm{Sturm}}(k, S)) \le U(k_0, S_0)$, and what is the exact asymptotic limit of the ratio $x_{\min}(a^{\mathrm{Sturm}}(k, S)) / x_{\min}^{\mathrm{Eliahou}}(k, S)$ as $k_0 \to \infty$ and $\delta_0 = S_0 \ln 2 - k_0 \ln 3 \to 0$?
2. **Dual Simplex Extrema (Cyclic Maximum and Cyclic Shift Average):** While [22, 25] characterize the cyclic minimum $\mu(a) = \min_r C(\sigma^r a)$, what are the exact global extrema and uniqueness conditions for the cyclic maximum $M(a) = \max_r C(\sigma^r a)$ and cyclic shift average $\overline{C}(a) = \frac{1}{k}\sum_r C(\sigma^r a)$ across $\mathcal{A}(k, S)$?
3. **Stern–Brocot Parent Determinant Identities and Perturbation Reduction:** Knight's reversal identity $3 M_{S,k} - N_{\mathrm{rev}} + D = 2^{S-1}$ [26] relates $M_{S,k}$ to its reversed shift $N_{\mathrm{rev}}$, which suffices for coprimality of $a^{\mathrm{Sturm}}(k, S)$ itself because $N_{\mathrm{rev}} \equiv 3^r 2^{-S_r} M_{S,k} \pmod D$. However, when $a^{\mathrm{Sturm}}(k, S)$ is perturbed by an adjacent transposition, cyclic shift invariance no longer eliminates the perturbed numerator against a fixed scalar factor! Can $M_{S,k}$ instead be inverted directly modulo $D = 2^S - 3^k$ using the Left and Right Farey parent denominators $d_1 = 3^{h_1} - 2^{q_1}$ and $d_2 = 2^{q_2} - 3^{h_2}$ on the Stern–Brocot tree?
4. **Diophantine Exclusion of Single-Transposition Perturbations:** Using the Left and Right Farey parent identities, can we prove that no single-transposition ($t=1$) downward perturbation of $a^{\mathrm{Sturm}}(k, S)$ is divisible by $2^S - 3^k$ whenever $2^{\frac{2}{3}S + 2} \le 2^S - 3^k$?

In this paper, we resolve these four questions. Our principal contributions beyond [22, 25, 26] are:

- **Dual Simplex Extrema for Cyclic Maximum and Average (Theorem 1):** Reviewing the cyclic-minimum bound and uniqueness of Halbeisen–Hungerbühler [22] and Fernández–Ibáñez [25] (Part 1), we prove for arbitrary $(k, S)$ with $d = \gcd(k, S) \ge 1$ and $(k_0, S_0) = (k/d, S/d)$ that $a^{\mathrm{Sturm}}(k, S)$ **uniquely minimizes** both the cyclic maximum $M(a)$ and the cyclic shift average $\overline{C}(a)$ (up to cyclic shifts), whereas the Steiner $1$-cycle vector $a^{(1)}$ uniquely maximizes $M(a)$ and $\overline{C}(a)$ (Parts 2–3).
- **Closed-Form Rearrangement Brackets and the Asymptotic $1/(2\ln 2)$ Limit (Theorem 2):** Applying the Hardy–Littlewood–Pólya Rearrangement Inequality to $\{j S_0 / k_0\}$, we enclose $x_{\min}(a^{\mathrm{Sturm}}(k, S))$ between two explicit $O(1)$ geometric series $L(k_0, S_0) \le x_{\min}(a^{\mathrm{Sturm}}(k, S)) \le U(k_0, S_0)$ for all $(k, S)$, and prove that as $k_0 \to \infty$ and $\delta_0 = S_0 \ln 2 - k_0 \ln 3 \to 0$,
  $$
  \lim_{k_0 \to \infty,\, \delta_0 \to 0} \frac{x_{\min}(a^{\mathrm{Sturm}}(k, S))}{x_{\min}^{\mathrm{Eliahou}}(k, S)} = \frac{1}{2\ln 2} \approx 0.72134752,
  $$
  with error $O(1/k_0 + (2^{S_0} - 3^{k_0})/3^{k_0})$. Using the finite upper bracket $U(k_0, S_0)$ together with a complete continued-fraction and Farey-mediant proof in Section 4.2, we show how the bracket reproduces and certifies the pure-word (unconditional on $m$) exclusions at $X_0 = 2^{60}$ ($k \ge k_{21} = 6,586,818,670$, a $16.57\times$ jump over Eliahou's $k_{19}$ bound), $X_0 = 2^{68}$ ($17$ of $29$ candidates eliminated on the $(k_{21}, k_{22})$ ray), and $X_0 = 2^{71.5}$ ($k \ge k_{23}$, compared against Hercher's $m > 91$ threshold $X_0 \ge 3 \cdot 2^{69} \approx 2^{70.585}$ [8]).
- **Stern–Brocot Parent Determinant Identities (Theorem 3):** For all coprime $(k_0, S_0)$ with Farey parents $(h_1, q_1)$ and $(h_2, q_2)$, we prove that the state vector $\mathbf{v}(k_0, S_0) = (C(a^{\mathrm{Sturm}}(k_0, S_0)), 3^{k_0} - 2^{S_0})^T$ obeys the weighted mediant recursion $\mathbf{v}(k_0, S_0) = 3^{h_2} \mathbf{v}(h_1, q_1) + 2^{q_1} \mathbf{v}(h_2, q_2)$ and satisfies the Left and Right Farey Parent Determinant Identities
  $$
  (3^{h_1} - 2^{q_1}) C(a^{\mathrm{Sturm}}(k_0, S_0)) + (2^{S_0} - 3^{k_0}) C(a^{\mathrm{Sturm}}(h_1, q_1)) = 3^{h_1 - 1} 2^{S_0 - 1},
  $$
  $$
  (2^{q_2} - 3^{h_2}) C(a^{\mathrm{Sturm}}(k_0, S_0)) - (2^{S_0} - 3^{k_0}) C(a^{\mathrm{Sturm}}(h_2, q_2)) = 3^{k_0 - 1} 2^{q_2 - 1}.
  $$
  Unlike Knight's reversal identity [26], these parent identities express $2(3^{h_1} - 2^{q_1}) C(a^{\mathrm{Sturm}}) \equiv 3^{h_1 - 1} 2^{S_0} \pmod{D_0}$ and $2(2^{q_2} - 3^{h_2}) C(a^{\mathrm{Sturm}}) \equiv 3^{k_0 - 1} 2^{q_2} \pmod{D_0}$ directly as pure $(2, 3)$-monomials modulo $D_0 = 2^{S_0} - 3^{k_0}$ (giving an alternative proof of [26, Theorem 5.4] and an explicit $2 \times 2$ block-matrix algorithm along the continued-fraction partial quotients $a_1, \dots, a_N$ that computes $C(a^{\mathrm{Sturm}}(k_0, S_0))$ in $O(N) = O(\log k_0)$ matrix multiplications).
- **Fixed-Point Homogenization & $m$-Cycle Discrepancy Bounds (Theorem 4):** We derive exact algebraic homogenizations at the affine fixed points $\xi_1 = -1$ and $\xi_2 = +1$, reducing the $k$-term cycle equation to the $m_+ = |\{j : a_j \ge 2\}|$ descent steps, and prove the $m$-cycle bound $x_{\min}(a) < 2m + \frac{6m}{k} x_{\min}^{\mathrm{Eliahou}}(k, S)$.
- **Farey Tent Reduction & Single-Transposition Exclusion (Theorem 5):** Applying the Left and Right Farey parent congruences of Theorem 3 to any single-transposition ($t=1$) downward perturbation of $a^{\mathrm{Sturm}}(k, S)$, we construct four explicit reduced Farey integers $R_A(j_1), R_B(j_1), Q_A(j_1), Q_B(j_1)$. Proving $j_1 \ne h_2$ and $S_{j_1} \ne q_2$ via $h_2 S = k q_2 - 1$, we establish by a two-regime case split ($j_1 < h_2$ vs. $j_1 > h_2$) that all four integers are non-zero and coprime to $6$ with $1 \le \min(|R_A|, |R_B|, |Q_A|, |Q_B|) < 2^{\frac{2}{3}S + 2}$, excluding all single-transposition perturbations whenever $2^{\frac{2}{3}S + 2} \le 2^S - 3^k$ (verified across all $56,304$ perturbations for $6 \le k \le 150$).


## 2. Related Work and Distinction

### 2.1 The Crandall–Garner–Eliahou, Halbeisen–Hungerbühler, Fernández–Ibáñez, and Knight Frameworks
The archimedean product relation $\frac{2^S}{3^k} = \prod_{j=0}^{k-1} (1 + \frac{1}{3x_j})$ was established by Crandall [1] and Garner [2], and Eliahou [3] established $x_{\min} \le (2^{S/k} - 3)^{-1}$. Subsequent verifications by Leavens and Vermeulen [9], Roosendaal [10], Oliveira e Silva [4] ($X_0 = 2^{60}$), and Barina [5] ($X_0 = 2^{68}$) pushed classical cycle length bounds to $k \ge 72,057,431,991$.

Halbeisen and Hungerbühler [22] proved (in their Lemma 5, Corollary 1, and Theorem 4) that the balanced word $s_i = \lceil ik/S \rceil - \lceil (i-1)k/S \rceil$ maximizes the minimum over cyclic shifts, yielding $x_{\min} \le M_{S,k}/(2^S - 3^k)$. Fernández and Ibáñez [25, Theorem 7.3] proved that the Christoffel word uniquely maximizes the cyclic minimum up to rotation for all $(k, S)$ (including non-coprime pairs), and Knight [26, Theorem 5.4] proved that integer high cycles do not exist via the reversal identity $3 M_{S,k} - N_{\mathrm{rev}} + D = 2^{S-1}$. Our work distinguishes between these established results and our four new contributions: (i) in Theorem 1, Part 1 reviews [22, 25], while Parts 2–3 establish the dual global extrema and strict uniqueness for the cyclic maximum $M(a)$ and cyclic shift average $\overline{C}(a)$; (ii) Theorem 2 derives the $O(1)$ closed-form Rearrangement Brackets $L(k_0, S_0) \le M_{S,k}/(2^S - 3^k) \le U(k_0, S_0)$ and the asymptotic limit $\lim_{k_0 \to \infty, \delta_0 \to 0} \frac{M_{S,k}/(2^S - 3^k)}{x_{\min}^{\mathrm{Eliahou}}(k, S)} = \frac{1}{2\ln 2} \approx 0.72134752$ (noting that for finite $(k, S)$ the exact ratio can lie on either side of $\frac{1}{2\ln 2}$—e.g., $0.80409 > \frac{1}{2\ln 2}$ at $(k, S) = (3, 5)$ and $0.721211 < \frac{1}{2\ln 2}$ at $(k, S) = (48, 77)$—so all finite exclusions use the upper bracket $U(k_0, S_0)$); (iii) Theorem 3 establishes the Stern–Brocot Left and Right Farey Parent Determinant Identities, which invert $M_{S_0, k_0}$ modulo $D_0$ into pure $(2, 3)$-monomials via $d_1, d_2$; and (iv) Theorem 5 uses these parent identities to exclude all single-transposition ($t=1$) perturbations via the 4-way Farey tent bound.

### 2.2 Baker-Type Linear Forms in Logarithms, Hercher's $m > 91$ Bound, and Recent Trajectory Analyses
Steiner [6] proved that $1$-cycles do not exist for $k > 1$. Simons and de Weger [7] generalized Steiner's approach to $m$-cycles using linear forms in logarithms [11, 12] for $m \le 68$, extended by Hercher [8] to $m \le 91$. Moreover, by combining $m \ge 92$ with the local-minima product bound, Hercher [8, Section 5, Corollary 29] proved that $X_0 \ge 3 \cdot 2^{69} \approx 2^{70.58496}$ suffices to exclude the $(k_{21}, k_{22})$ ray and reach $k \ge k_{23} = 137,528,045,312$. Thus, for unrestricted cycles, Hercher's hybrid $(m \ge 92) + X_0$ bound reaches $k_{23}$ at a lower threshold ($2^{70.585}$) than pure balanced-word bounds ($2^{71.413}$); our Section 4.2 bounds instead provide closed-form $O(1)$ certificates for the pure balanced-word bound of [22] without invoking Baker-type $m$-cycle reductions. Recent work on rStation has also advanced complementary trajectory and 3-adic methods: `lyapunov_weaver` [23] established an inverse-minimum comparison cone for $\{1, 2\}$-exponent words without consecutive twos, `fourier_wren` [24] established renewal identities and certified decay bounds for the Syracuse characteristic function $\chi_n(\xi)$ on $\mathbb{Z}/3^n\mathbb{Z}$, and `sylve_recursions` [27] established two-path inverse-tree obstructions to additive Collatz potentials.

### 2.3 Combinatorics on Words, Christoffel Words, and Continued-Fraction Matrix Products
Sturmian words and Christoffel words are classical objects in symbolic dynamics (Lothaire [13], Berstel et al. [14]). While the concatenation of Christoffel words on the Stern–Brocot tree is classical [18, 19], our Theorem 3 shows that the bivariate Syracuse vector $(C(a^{\mathrm{Sturm}}(k_0, S_0)), 3^{k_0} - 2^{S_0})^T$ obeys a *weighted* mediant recursion with $(2, 3)$-smooth determinant $-3^{h_1-1} 2^{q_2-1}$, and we give the explicit batched continued-fraction matrix product that evaluates $M_{S_0, k_0}$ in $O(\log k_0)$ arithmetic operations.

---

## 3. Mathematical Foundations: The Valuation Simplex and Simplex Extremality

Let $k \ge 2$ and $S \ge 1$ be positive integers such that $k < S < 2k$ and $D(k, S) := 2^S - 3^k > 0$. The valuation simplex $\mathcal{A}(k, S)$ is defined by
$$
\mathcal{A}(k, S) = \left\{ a = (a_0, \dots, a_{k-1}) \in \{1, 2\}^k : \sum_{j=0}^{k-1} a_j = S \right\},
$$
augmented more generally to allow components $a_j \ge 1$ with $\sum a_j = S$. The cyclic shift operator $\sigma: \mathcal{A}(k, S) \to \mathcal{A}(k, S)$ is defined by
$$
\sigma(a_0, a_1, \dots, a_{k-1}) = (a_1, \dots, a_{k-1}, a_0).
$$
For any $a \in \mathcal{A}(k, S)$, the cycle numerator is
$$
C(a) = \sum_{j=0}^{k-1} 3^{k-1-j} 2^{S_j}, \quad \text{where} \quad S_j = \sum_{i=0}^{j-1} a_i \quad (S_0 = 0).
$$
The trajectory values along the rational cycle defined by $a$ are given by $x_r(a) = C(\sigma^r a) / D(k, S)$ for $0 \le r < k$. We define the three fundamental cyclic functionals on $\mathcal{A}(k, S)$:
$$
\mu(a) := \min_{0 \le r < k} C(\sigma^r a), \quad M(a) := \max_{0 \le r < k} C(\sigma^r a), \quad \overline{C}(a) := \frac{1}{k} \sum_{r=0}^{k-1} C(\sigma^r a).
$$
Note that $x_{\min}(a) = \mu(a) / D(k, S)$ and $x_{\max}(a) = M(a) / D(k, S)$.

### 3.1 The Cyclic Shift Recurrence and Böhm–Sontacchi Equivalence

A direct calculation reveals the fundamental shift relation connecting consecutive cyclic shifts of $a$:

**Lemma 1 (Cyclic Shift Recurrence).** *For any $a \in \mathcal{A}(k, S)$ and any shift index $r \in \{0, \dots, k-1\}$,*
$$
2^{a_r} C(\sigma^{r+1} a) = 3 C(\sigma^r a) + (2^S - 3^k).
$$

*Proof.* By definition of $C(\sigma^r a)$,
$$
C(\sigma^r a) = 3^{k-1} + 3^{k-2} 2^{a_r} + 3^{k-3} 2^{a_r + a_{r+1}} + \dots + 2^{S - a_{r-1}}.
$$
Multiplying by $3$ and adding $2^S - 3^k$:
$$
3 C(\sigma^r a) + (2^S - 3^k) = 2^S + 3^{k-1} 2^{a_r} + 3^{k-2} 2^{a_r + a_{r+1}} + \dots + 3 \cdot 2^{S - a_{r-1}}.
$$
Factoring out $2^{a_r}$:
$$
= 2^{a_r} \left( 3^{k-1} + 3^{k-2} 2^{a_{r+1}} + \dots + 2^{S - a_r} \right) = 2^{a_r} C(\sigma^{r+1} a). \quad \square
$$

Dividing Lemma 1 by $D(k, S) = 2^S - 3^k$ yields $2^{a_r} x_{r+1}(a) = 3 x_r(a) + 1$, confirming that $(x_r(a))_{r=0}^{k-1}$ is an exact orbit of the Syracuse map in the field of fractions $\mathbb{Q}$ (and in the ring of $2$-adic integers $\mathbb{Z}_2$).

Furthermore, reducing Lemma 1 modulo $D(k, S)$ shows that in the quotient ring $\mathbb{Z}/D(k, S)\mathbb{Z}$,
$$
C(\sigma^{r+1} a) \equiv 3 \cdot 2^{-a_r} C(\sigma^r a) \pmod{D(k, S)}.
$$
Since $\gcd(6, D(k, S)) = 1$, the unit $3 \cdot 2^{-a_r}$ is invertible modulo $D(k, S)$. This immediately proves:

**Corollary 1 (Böhm–Sontacchi Congruence Invariance [15]).** *For any $a \in \mathcal{A}(k, S)$, the divisibility condition $D(k, S) \mid C(a)$ is equivalent to $D(k, S) \mid C(\sigma^r a)$ for all $0 \le r < k$. In particular, $x_0(a) \in \mathbb{Z}$ if and only if every $x_r(a) \in \mathbb{Z}$, and each $x_r(a)$ is automatically an odd integer with exact valuation $v_2(3x_r(a) + 1) = a_r$.*

### 3.2 The Adjacent-Transposition Difference Operator

To understand how $C(a)$ varies as $a$ traverses the simplex $\mathcal{A}(k, S)$, let $s_j = (j, j+1)$ denote the transposition of adjacent elements $a_j$ and $a_{j+1}$ for $0 \le j \le k-2$.

**Lemma 2 (Adjacent Transposition Identity).** *Let $a \in \mathcal{A}(k, S)$ and let $s_j a = (a_0, \dots, a_{j+1}, a_j, \dots, a_{k-1})$. Then*
$$
C(s_j a) - C(a) = 3^{k-2-j} 2^{S_j} \left(2^{a_{j+1}} - 2^{a_j}\right).
$$

*Proof.* In the sum defining $C(a)$, the term for index $i < j$ has cumulative valuation $S_i$, identical in both $a$ and $s_j a$. The terms for index $i \ge j+2$ have cumulative valuation $S_i = S_j + a_j + a_{j+1} + \dots$, also identical because $a_j + a_{j+1} = a_{j+1} + a_j$. The only terms that differ are $i = j$ and $i = j+1$:
$$
\text{For } a: \quad 3^{k-1-j} 2^{S_j} + 3^{k-2-j} 2^{S_j + a_j},
$$
$$
\text{For } s_j a: \quad 3^{k-1-j} 2^{S_j} + 3^{k-2-j} 2^{S_j + a_{j+1}}.
$$
Subtracting the two expressions:
$$
C(s_j a) - C(a) = 3^{k-2-j} 2^{S_j} \left(2^{a_{j+1}} - 2^{a_j}\right). \quad \square
$$

Lemma 2 shows that sorting an inversion (replacing $(a_j, a_{j+1}) = (2, 1)$ with $(1, 2)$) strictly decreases $C(a)$ by $3^{k-2-j} 2^{S_j}$. Consequently, the unshifted functional $C(a)$ is strictly minimized over all permutations of a given multiset by sorting $a$ in non-decreasing order $(1, \dots, 1, 2, \dots, 2)$, and strictly maximized by sorting in non-increasing order.

### 3.3 Universal Simplex Extremality for Coprime and Non-Coprime $(k, S)$

We now state and prove Theorem 1. Part 1 reviews the cyclic-minimum upper bound of Halbeisen and Hungerbühler [22, Lemma 5 & Corollary 1] and its strict uniqueness and period-multiplicity invariance established by Fernández and Ibáñez [25, Theorem 7.3] for arbitrary $(k, S)$ with $d = \gcd(k, S) \ge 1$, while Parts 2 and 3 establish the dual global extrema and strict uniqueness for the cyclic maximum $M(a)$ and cyclic shift average $\overline{C}(a)$ over $\mathcal{A}(k, S)$.

For any integers $1 \le k < S$ with $d = \gcd(k, S) \ge 1$ and reduced coprime ratio $(k_0, S_0) = (k/d, S/d)$, the **balanced Sturmian word** (lower Christoffel word when $d=1$, or its $d$-fold periodic repetition $(a^{\mathrm{Sturm}}(k_0, S_0))^d$ when $d > 1$), denoted $a^{\mathrm{Sturm}}(k, S)$, is defined by
$$
a_j^{\mathrm{Sturm}} = \left\lfloor \frac{(j+1)S}{k} \right\rfloor - \left\lfloor \frac{jS}{k} \right\rfloor = \left\lfloor \frac{(j+1)S_0}{k_0} \right\rfloor - \left\lfloor \frac{j S_0}{k_0} \right\rfloor \quad \text{for } 0 \le j \le k-1.
$$
Its cumulative valuation profile is $S_j^{\mathrm{Sturm}} = \lfloor jS/k \rfloor = \lfloor j S_0 / k_0 \rfloor$. At the opposite extreme, the **Steiner $1$-cycle vector** is $a^{(1)} = (1, 1, \dots, 1, S - k + 1)$.

**Theorem 1 (Simplex Extremality Theorem).** *Let $k \ge 2$ and $k < S < 2k$ with $2^S > 3^k$, let $d = \gcd(k, S) \ge 1$, and let $(k_0, S_0) = (k/d, S/d)$. For every valuation vector $a \in \mathcal{A}(k, S)$:*

1. **Extremal Minimum Bounds and Period-Multiplicity Invariance ([22, Lemma 5 & Corollary 1], [25, Theorem 7.3]):**
   $$
   3^k - 2^k = \mu(a^{(1)}) \le \mu(a) \le \mu(a^{\mathrm{Sturm}}(k, S)) = \sum_{j=0}^{k-1} 3^{k-1-j} 2^{\lfloor jS/k \rfloor} = \frac{2^S - 3^k}{2^{S_0} - 3^{k_0}} \mu(a^{\mathrm{Sturm}}(k_0, S_0)),
   $$
   *and dividing by $D(k, S) = 2^S - 3^k > 0$ yields the period-invariant rational cycle minimum inequality:*
   $$
   \frac{3^k - 2^k}{2^S - 3^k} = x_{\min}(a^{(1)}) \le x_{\min}(a) \le x_{\min}(a^{\mathrm{Sturm}}(k, S)) = x_{\min}(a^{\mathrm{Sturm}}(k_0, S_0)).
   $$
   *Equality $\mu(a) = \mu(a^{(1)})$ holds if and only if $a$ is a cyclic shift of $a^{(1)}$. Equality $\mu(a) = \mu(a^{\mathrm{Sturm}}(k, S))$ holds if and only if $a$ is a cyclic shift of $a^{\mathrm{Sturm}}(k, S) = (a^{\mathrm{Sturm}}(k_0, S_0))^d$ [25, Theorem 7.3].*

2. **Extremal Maximum Bounds:**
   $$
   \sum_{j=0}^{k-1} 3^{k-1-j} 2^{\lceil jS/k \rceil} = M(a^{\mathrm{Sturm}}(k, S)) \le M(a) \le M(a^{(1)}) = C(S - k + 1, 1, \dots, 1),
   $$
   *with lower equality if and only if $a$ is a cyclic shift of $a^{\mathrm{Sturm}}(k, S)$ and upper equality if and only if $a$ is a cyclic shift of $a^{(1)}$.*

3. **Extremal Average Bound:**
   $$
   \overline{C}(a) \ge \overline{C}(a^{\mathrm{Sturm}}(k, S)) = \frac{1}{k_0} \sum_{j=0}^{k-1} 3^{k-1-j} 2^{\lfloor j S_0 / k_0 \rfloor} \left( k_0 + (j S_0 \bmod k_0) \right),
   $$
   *with equality if and only if $a$ is a cyclic shift of $a^{\mathrm{Sturm}}(k, S)$.*

*Proof.*
We first prove Part 3 (cyclic shift average). For any $a \in \mathcal{A}(k, S)$, the cyclic shift average is
$$
\overline{C}(a) = \frac{1}{k} \sum_{r=0}^{k-1} C(\sigma^r a) = \sum_{j=0}^{k-1} 3^{k-1-j} \left( \frac{1}{k} \sum_{r=0}^{k-1} 2^{S_j(\sigma^r a)} \right),
$$
where $S_j(\sigma^r a) = \sum_{i=0}^{j-1} a_{r+i \pmod k}$ is the sum of $j$ consecutive valuations starting at shift $r$.
For each fixed window length $j \in \{0, \dots, k-1\}$, $\sum_{r=0}^{k-1} S_j(\sigma^r a) = jS$ and $jS/k = j S_0 / k_0$.
By Karamata's majorization inequality applied to the strictly convex function $f(t) = 2^t$, for any $k$ integers $u_0, \dots, u_{k-1}$ summing to $jS$, $\sum_{r=0}^{k-1} 2^{u_r}$ is strictly minimized if and only if each $u_r \in \{\lfloor jS/k \rfloor, \lceil jS/k \rceil\}$, with a fraction $1 - \{j S_0 / k_0\} = (k_0 - (j S_0 \bmod k_0))/k_0$ equal to $\lfloor j S_0 / k_0 \rfloor$ and $\{j S_0 / k_0\} = (j S_0 \bmod k_0)/k_0$ equal to $\lfloor j S_0 / k_0 \rfloor + 1$:
$$
\frac{1}{k} \sum_{r=0}^{k-1} 2^{S_j(\sigma^r a)} \ge \frac{1}{k_0} 2^{\lfloor j S_0 / k_0 \rfloor} \left( k_0 + (j S_0 \bmod k_0) \right).
$$
Multiplying by $3^{k-1-j} > 0$ and summing over $0 \le j \le k-1$ yields Part 3. By the Morse–Hedlund theorem [13], all window sums $S_j(\sigma^r a)$ are balanced (differing by at most $1$) for all $j$ if and only if $a$ is a cyclic shift of $a^{\mathrm{Sturm}}(k, S)$.

For Part 1 (following [22, Lemma 5] and [25, Theorem 7.3] via the periodic discrepancy sequence), define $U_i(a) = k S_i(a) - i S$ for $i \in \mathbb{Z}$, which satisfies $U_{i+k}(a) = U_i(a)$. Let $r^* \in \operatorname{argmax}_{0 \le i < k} U_i(a)$ be any index attaining the global maximum of $U_i(a)$ (unique when $d = 1$ by Raney's lemma [16]). Then $b = \sigma^{r^*} a$ satisfies $U_j(b) = U_{r^* + j}(a) - U_{r^*}(a) \le 0$ for all $0 \le j \le k$, so $S_j(b) \le \lfloor jS/k \rfloor = S_j(a^{\mathrm{Sturm}}(k, S))$ for all $0 \le j < k$.
Consequently, $\mu(a) \le C(b) = \sum_{j=0}^{k-1} 3^{k-1-j} 2^{S_j(b)} \le C(a^{\mathrm{Sturm}}(k, S))$ [22, Lemma 5]. Moreover, for $a^{\mathrm{Sturm}}(k, S)$, every shift satisfies $S_j \ge \lfloor jS/k \rfloor$, so $\mu(a^{\mathrm{Sturm}}(k, S)) = C(a^{\mathrm{Sturm}}(k, S))$, and if $a$ is not a cyclic shift of $a^{\mathrm{Sturm}}(k, S)$, then at every shift $r$ with $S_j(\sigma^r a) \le \lfloor jS/k \rfloor$ at least one $j$ has strict inequality, forcing $\mu(a) < \mu(a^{\mathrm{Sturm}}(k, S))$ [25, Theorem 7.3]. Writing $j = m k_0 + i$ ($0 \le m < d$, $0 \le i < k_0$) gives $\lfloor jS/k \rfloor = m S_0 + \lfloor i S_0 / k_0 \rfloor$, so $C(a^{\mathrm{Sturm}}(k, S)) = \sum_{m=0}^{d-1} 3^{(d-1-m)k_0} 2^{m S_0} C(a^{\mathrm{Sturm}}(k_0, S_0)) = \frac{2^S - 3^k}{2^{S_0} - 3^{k_0}} C(a^{\mathrm{Sturm}}(k_0, S_0))$, and dividing by $2^S - 3^k$ gives $x_{\min}(a^{\mathrm{Sturm}}(k, S)) = x_{\min}(a^{\mathrm{Sturm}}(k_0, S_0))$.
Conversely, $a_i \ge 1 \implies S_j \ge j$ for all $0 \le j \le k-1$, with equality for all $j$ if and only if $a = a^{(1)}$, giving $\mu(a) \ge \mu(a^{(1)}) = \sum_{j=0}^{k-1} 3^{k-1-j} 2^j = 3^k - 2^k$. Part 2 follows symmetrically by choosing $r_* \in \operatorname{argmin}_{0 \le i < k} U_i(a)$, where $S_j(\sigma^{r_*} a) \ge \lceil jS/k \rceil$. $\quad \square$

Figure 1(a) in the supplement illustrates Theorem 1 on the valuation simplex $\mathcal{A}(13, 21)$, which contains $125,970$ valuation vectors grouped into $9,690$ cyclic orbits. The plot displays the complete orbit cloud $(x_{\min}(a), x_{\max}(a))$, showing that the Steiner $1$-cycle orbit sits at the bottom-left of $x_{\min}$ and top-left of $x_{\max}$, while the Christoffel word $a^{\mathrm{Sturm}}(13, 21)$ sits at the extreme right-hand apex, achieving the unique global maximum of $x_{\min}(a)$.

![Exact Orbit Simplex and Asymptotic Convergence](supplement/figure-1.png)


## 4. The $1/(2\ln 2)$ Sharpening of the Crandall–Garner–Eliahou Bound

Having established that $x_{\min}(a) \le x_{\min}(a^{\mathrm{Sturm}}(k, S))$ for all $a \in \mathcal{A}(k, S)$, we now derive explicit closed-form upper and lower bounds on $x_{\min}(a^{\mathrm{Sturm}}(k, S))$ that prove its asymptotic ratio to Eliahou's bound.

Recall the classical Crandall–Garner–Eliahou bound [1, 2, 3]:
$$
x_{\min}^{\mathrm{Eliahou}}(k, S) := \frac{1}{2^{S/k} - 3}.
$$
By expanding the geometric series $\sum_{j=0}^{k-1} 3^{k-1-j} 2^{j S/k} = \frac{2^S - 3^k}{2^{S/k} - 3}$, Eliahou's bound can be written exactly as
$$
x_{\min}^{\mathrm{Eliahou}}(k, S) = \frac{\sum_{j=0}^{k-1} 3^{k-1-j} 2^{j S/k}}{2^S - 3^k}.
$$
Notice the subtle difference between $x_{\min}^{\mathrm{Eliahou}}$ and the exact Sturmian minimum $x_{\min}(a^{\mathrm{Sturm}})$:
- In $x_{\min}^{\mathrm{Eliahou}}$, the exponents are the continuous fractional values $j S/k$.
- In $x_{\min}(a^{\mathrm{Sturm}})$, the exponents are the exact integer floors $\lfloor jS/k \rfloor = j S/k - \{jS/k\}$.

Because $\{jS/k\} \in [0, 1)$, every term in $x_{\min}(a^{\mathrm{Sturm}})$ has $2^{\lfloor jS/k \rfloor} = 2^{j S/k} \cdot 2^{-\{jS/k\}} < 2^{j S/k}$ for all $j \ge 1$. How much smaller is the sum?

### 4.1 Closed-Form Rearrangement Brackets for Coprime and Non-Coprime $(k, S)$

Let $d = \gcd(k, S) \ge 1$ and $(k_0, S_0) = (k/d, S/d)$ so that $\gcd(k_0, S_0) = 1$. By Theorem 1 Part 1, $x_{\min}(a^{\mathrm{Sturm}}(k, S)) = x_{\min}(a^{\mathrm{Sturm}}(k_0, S_0))$ and $x_{\min}^{\mathrm{Eliahou}}(k, S) = (2^{S/k} - 3)^{-1} = x_{\min}^{\mathrm{Eliahou}}(k_0, S_0)$. As $j$ ranges over $0, 1, \dots, k_0 - 1$, the fractional parts $\{j S_0 / k_0\}$ are a permutation of the uniform arithmetic progression
$$
\left\{ 0, \frac{1}{k_0}, \frac{2}{k_0}, \dots, \frac{k_0 - 1}{k_0} \right\}.
$$
We apply the classical Rearrangement Inequality to bound the sum of products of the monotonically increasing weights $w_j = 3^{k_0 - 1 - j} 2^{j S_0 / k_0} = 3^{k_0 - 1} (2^{S_0 / k_0}/3)^j$ and the permuted factors $v_j = 2^{-\{j S_0 / k_0\}}$.

**Theorem 2 (Rearrangement Brackets and Universal Ratio Theorem).** *Let $k \ge 2$ and $k < S < 2k$ with $2^S > 3^k$, let $d = \gcd(k, S) \ge 1$, and let $(k_0, S_0) = (k/d, S/d)$ ($k_0 \ge 2$, $\gcd(k_0, S_0) = 1$). Then:*

1. **Closed-Form Geometric Brackets:**
   $$
   L(k_0, S_0) := \frac{2^{S_0 - 1} - 3^{k_0}}{(2^{S_0} - 3^{k_0})(2^{(S_0 - 1)/k_0} - 3)} \le x_{\min}(a^{\mathrm{Sturm}}(k, S)) \le \frac{2^{-(k_0 - 1)/k_0}(2^{S_0 + 1} - 3^{k_0})}{(2^{S_0} - 3^{k_0})(2^{(S_0 + 1)/k_0} - 3)} =: U(k_0, S_0).
   $$

2. **Asymptotic Convergence:**
   *As $k_0 \to \infty$ along any sequence of pairs $(k, S)$ with $2^S > 3^k$ such that $\delta_0 = S_0 \ln 2 - k_0 \ln 3 \to 0$ (including all continued-fraction convergents of $\log_2 3$):*
   $$
   \lim_{k_0 \to \infty,\, \delta_0 \to 0} \frac{x_{\min}(a^{\mathrm{Sturm}}(k, S))}{x_{\min}^{\mathrm{Eliahou}}(k, S)} = \frac{1}{2\ln 2} \approx 0.72134752.
   $$
   *More precisely, for all $k_0 \ge 2$:*
   $$
   x_{\min}(a) \le x_{\min}(a^{\mathrm{Sturm}}(k, S)) \le U(k_0, S_0) = \left( \frac{1}{2\ln 2} + O\left(\frac{1}{k_0} + \frac{2^{S_0} - 3^{k_0}}{3^{k_0}}\right) \right) x_{\min}^{\mathrm{Eliahou}}(k, S).
   $$

*Proof.*
By Theorem 1 Part 1, $x_{\min}(a^{\mathrm{Sturm}}(k, S)) = x_{\min}(a^{\mathrm{Sturm}}(k_0, S_0))$, where
$$
C(a^{\mathrm{Sturm}}(k_0, S_0)) = \sum_{j=0}^{k_0 - 1} 3^{k_0 - 1 - j} 2^{\lfloor j S_0 / k_0 \rfloor} = \sum_{j=0}^{k_0 - 1} 3^{k_0 - 1 - j} 2^{j S_0 / k_0} \cdot 2^{-\{j S_0 / k_0\}}.
$$
Let $w_j = 3^{k_0 - 1 - j} 2^{j S_0 / k_0} = 3^{k_0 - 1} (2^{S_0 / k_0}/3)^j$. Since $2^{S_0 / k_0} > 3$, the sequence $(w_j)_{j=0}^{k_0 - 1}$ is strictly increasing.
Because $\gcd(k_0, S_0) = 1$, the values of $\{j S_0 / k_0\}$ as $j$ runs from $0$ to $k_0 - 1$ are a permutation $\pi$ of $\{0, 1/k_0, 2/k_0, \dots, (k_0 - 1)/k_0\}$.
By the classical Rearrangement Inequality (Hardy, Littlewood, and Pólya [17]):
- The sum $\sum_{j=0}^{k_0 - 1} w_j 2^{-\pi(j)/k_0}$ is maximized when the two sequences are sorted in the same order ($\pi(j) = k_0 - 1 - j$), and minimized when sorted in opposite orders ($\pi(j) = j$).

Evaluating the upper rearrangement geometric series:
$$
\sum_{j=0}^{k_0 - 1} w_j 2^{-(k_0 - 1 - j)/k_0} = 3^{k_0 - 1} 2^{-(k_0 - 1)/k_0} \sum_{j=0}^{k_0 - 1} \left(\frac{2^{(S_0 + 1)/k_0}}{3}\right)^j = 2^{-(k_0 - 1)/k_0} \frac{2^{S_0 + 1} - 3^{k_0}}{2^{(S_0 + 1)/k_0} - 3}.
$$
Evaluating the lower rearrangement geometric series:
$$
\sum_{j=0}^{k_0 - 1} w_j 2^{-j/k_0} = 3^{k_0 - 1} \sum_{j=0}^{k_0 - 1} \left(\frac{2^{(S_0 - 1)/k_0}}{3}\right)^j = \frac{2^{S_0 - 1} - 3^{k_0}}{2^{(S_0 - 1)/k_0} - 3}.
$$
Dividing by $D(k_0, S_0) = 2^{S_0} - 3^{k_0}$ proves Part 1.

For Part 2, let $\delta_0 = S_0 \ln 2 - k_0 \ln 3 > 0$. When $\delta_0 \to 0$ and $k_0 \to \infty$, $2^{S_0} - 3^{k_0} = 3^{k_0} (e^{\delta_0} - 1) = 3^{k_0} \delta_0 (1 + O(\delta_0))$, and $2^{S_0 / k_0} - 3 = 3(e^{\delta_0 / k_0} - 1) = \frac{3\delta_0}{k_0}(1 + O(\delta_0 / k_0))$, so $x_{\min}^{\mathrm{Eliahou}}(k, S) = \frac{k_0}{3\delta_0} (1 + O(\delta_0 / k_0))$.
In the upper rearrangement bound $U(k_0, S_0)$, $2^{(S_0 + 1)/k_0} - 3 = 3(e^{(\delta_0 + \ln 2)/k_0} - 1) = \frac{3\ln 2}{k_0}(1 + O(1/k_0 + \delta_0))$ and $2^{S_0 + 1} - 3^{k_0} = 3^{k_0}(2 e^{\delta_0} - 1) = 3^{k_0}(1 + O(\delta_0))$, so
$$
U(k_0, S_0) = \frac{\frac{1}{2} \cdot 3^{k_0} (1 + O(1/k_0 + \delta_0))}{3^{k_0} \delta_0 (1 + O(\delta_0)) \cdot \frac{3\ln 2}{k_0} (1 + O(1/k_0 + \delta_0))} = \frac{k_0}{6 (\ln 2) \delta_0} \left( 1 + O\left(\frac{1}{k_0} + \delta_0\right) \right),
$$
and similarly for $L(k_0, S_0)$, yielding $\lim_{k_0 \to \infty, \delta_0 \to 0} x_{\min}(a^{\mathrm{Sturm}}(k, S)) / x_{\min}^{\mathrm{Eliahou}}(k, S) = \frac{1}{2\ln 2}$. $\quad \square$

Figure 1(b) in the supplement displays the ratio $x_{\min}(a^{\mathrm{Sturm}}(k, S)) / x_{\min}^{\mathrm{Eliahou}}(k, S)$ across all coprime pairs $(k, S = \lceil k \log_2 3 \rceil)$ for $3 \le k \le 120$, together with the closed-form rearrangement bounds $L(k, S)$ and $U(k, S)$.

### 4.2 Analytical Farey-Mediant Exclusions via the Finite Upper Bracket $U(k_0, S_0)$

Given a computational verification that all starting values $n \le X_0$ converge to $1$, Theorems 1 and 2 rule out any candidate pair $(k, S)$ (with $d = \gcd(k, S) \ge 1$ and reduced pair $(k_0, S_0) = (k/d, S/d)$) whenever the **exact finite upper Rearrangement Bracket** satisfies
$$
U(k_0, S_0) = \frac{2^{-(k_0 - 1)/k_0}(2^{S_0 + 1} - 3^{k_0})}{(2^{S_0} - 3^{k_0})(2^{(S_0 + 1)/k_0} - 3)} < X_0.
$$
Because $U(k_0, S_0)$ and $x_{\min}^{\mathrm{Eliahou}}(k, S) = x_{\min}^{\mathrm{Eliahou}}(k_0, S_0) = (2^{S_0/k_0} - 3)^{-1}$ depend only on the reduced coprime pair $(k_0, S_0)$, while any non-coprime multiple $(k, S) = (d k_0, d S_0)$ with $d \ge 2$ has $k = d k_0 > k_0$ and $k + S = d(k_0 + S_0) > k_0 + S_0$, the global minimum of $k$ (and of $k + S$) over all surviving pairs $(k, S)$ is always attained at a coprime pair $(k_0, S_0)$ ($d = 1$). Moreover, since each factor $2^{-(k_0 - 1 - j)/k_0} \le 1$ in the geometric series defining $U(k_0, S_0)$ is strictly less than $1$ for $0 \le j \le k_0 - 2$, we have the universal strict inequality $U(k_0, S_0) < x_{\min}^{\mathrm{Eliahou}}(k_0, S_0) = (2^{S_0/k_0} - 3)^{-1}$, where $(2^{\sigma} - 3)^{-1}$ is strictly decreasing in the slope $\sigma = S_0/k_0 > \log_2 3$.

Recall that the continued-fraction convergents $S_n / k_n$ of $\alpha = \log_2 3$ alternate around $\alpha$: odd convergents $(k_{2m-1}, S_{2m-1})$ satisfy $S_{2m-1}/k_{2m-1} > \alpha$ ($\delta_{2m-1} = S_{2m-1}\ln 2 - k_{2m-1}\ln 3 > 0$), while even convergents $(k_{2m}, S_{2m})$ satisfy $S_{2m}/k_{2m} < \alpha$ ($\delta_{2m} < 0$), with Farey determinant $S_{2m-1} k_{2m} - k_{2m-1} S_{2m} = +1$ and recurrence $\delta_{2m-1} = a_{2m+1}|\delta_{2m}| + \delta_{2m+1} > a_{2m+1}|\delta_{2m}|$ (so $|\delta_{2m}|/\delta_{2m-1} < 1/a_{2m+1}$). By the Farey mediant theorem, every rational $S_0/k_0$ lying strictly between $S_{2m}/k_{2m}$ and $S_{2m-1}/k_{2m-1}$ has the canonical representation $(k_0, S_0) = a(k_{2m-1}, S_{2m-1}) + b(k_{2m}, S_{2m})$ with coprime integers $a, b \ge 1$ (where $\delta(a, b) = a\delta_{2m-1} - b|\delta_{2m}| > 0$ requires $b/a < \delta_{2m-1}/|\delta_{2m}|$), and therefore satisfies $k_0 = a k_{2m-1} + b k_{2m} \ge k_{2m-1} + k_{2m}$.

Combining this Farey-mediant structure with $100$-digit decimal evaluation in `verify_paper1.py` yields three unconditional analytical exclusions across all $(k, S)$ (requiring no arbitrary finite search cutoffs on $a$ or $b$):

1. **The $X_0 = 2^{60}$ Milestone (Oliveira e Silva 2010 [4]):**
   Consider the $19$-th (odd) convergent $(k_{19}, S_{19}) = (397,573,379,\; 630,138,897)$ ($k_{19} + S_{19} = 1,027,712,276$), the $20$-th (even) convergent $(k_{20}, S_{20}) = (6,189,245,291,\; 9,809,721,694)$, and the $21$-st (odd) convergent $(k_{21}, S_{21}) = (k_{19} + k_{20}, S_{19} + S_{20}) = (6,586,818,670,\; 10,439,860,591)$ ($k_{21} + S_{21} = 17,026,679,261$, since $a_{21} = 1$).
   - By the Farey mediant property on $(S_{20}/k_{20}, S_{19}/k_{19})$, every rational $S_0/k_0 \in (\log_2 3, S_{19}/k_{19})$ lies inside $(S_{20}/k_{20}, S_{19}/k_{19})$ and therefore has denominator $k_0 \ge k_{19} + k_{20} = k_{21}$.
   - Consequently, any coprime pair $(k_0, S_0) \ne (k_{19}, S_{19})$ with $k_0 < k_{21}$ and $2^{S_0} > 3^{k_0}$ must satisfy $S_0/k_0 > S_{19}/k_{19}$, which implies $S_0/k_0 - S_{19}/k_{19} \ge \frac{1}{k_0 k_{19}} \ge \frac{1}{(k_{21} - 1) k_{19}}$ and hence
     $$
     \log_2 U(k_0, S_0) < \log_2 x_{\min}^{\mathrm{Eliahou}}(k_0, S_0) \le \log_2 \frac{1}{2^{S_{19}/k_{19} + 1/((k_{21}-1)k_{19})} - 3} = 59.1232021 < 60.
     $$
   - At $(k_{19}, S_{19})$ itself, direct evaluation gives
     $$
     \log_2 x_{\min}^{\mathrm{Eliahou}}(k_{19}, S_{19}) = 60.1190318 > 60, \qquad \log_2 U(k_{19}, S_{19}) = 59.6477982 < 60.
     $$
   While the classical Eliahou bound fails to eliminate $(k_{19}, S_{19})$ at $X_0 = 2^{60}$, the finite upper bracket $U(k_0, S_0) < 2^{60}$ **analytically eliminates $(k_{19}, S_{19})$ and every pair with $k < k_{21}$**, jumping the global minimum cycle length at $X_0 = 2^{60}$ to $(k_{21}, S_{21})$ ($k \ge 6,586,818,670$, $k + S \ge 17,026,679,261$), a **$16.5676\times$ increase**.

2. **The $X_0 = 2^{68}$ Milestone (Barina 2021 [5]):**
   Between the $21$-st convergent $(k_{21}, S_{21})$ and the $22$-nd (even) convergent $(k_{22}, S_{22}) = (65,470,613,321,\; 103,768,467,013)$, any coprime pair with $S_0/k_0 \ge S_{21}/k_{21}$ satisfies $\log_2 U(k_0, S_0) < \log_2 x_{\min}^{\mathrm{Eliahou}}(k_{21}, S_{21}) = 67.5555265 < 68$ ($\log_2 U(k_{21}, S_{21}) = 67.0842928$). Every remaining pair with $\log_2 3 < S_0/k_0 < S_{21}/k_{21}$ lies in $(S_{22}/k_{22}, S_{21}/k_{21})$ and has the form $(k_0, S_0) = a(k_{21}, S_{21}) + b(k_{22}, S_{22})$ with $a, b \ge 1, \gcd(a, b) = 1$. Since $a_{23} = 2$, the $23$-rd convergent is $(k_{23}, S_{23}) = (k_{21} + 2k_{22}, S_{21} + 2S_{22}) = (137,528,045,312,\; 217,976,794,617)$, so **every pair with $b \ge 2$ automatically satisfies $k_0 \ge k_{21} + 2k_{22} = k_{23}$**. Along the $b = 1$ ray
   $$
   (k_a, S_a) = a(k_{21}, S_{21}) + (k_{22}, S_{22}) \quad (a \ge 1),
   $$
   the slope $S_a/k_a$ strictly increases with $a$ (as $\frac{S_{a+1}}{k_{a+1}} - \frac{S_a}{k_a} = \frac{S_{21} k_{22} - k_{21} S_{22}}{k_a k_{a+1}} = \frac{1}{k_a k_{a+1}} > 0$), so both $x_{\min}^{\mathrm{Eliahou}}(k_a, S_a)$ and $U(k_a, S_a)$ strictly decrease with $a \ge 1$. Evaluating to $100$-digit precision shows that $\log_2 x_{\min}^{\mathrm{Eliahou}}(k_a, S_a) \ge 68$ for $a \in \{1, \dots, 29\}$ ($68.0035590$ at $a = 29$ vs. $67.9904638$ at $a = 30$), whereas $\log_2 U(k_a, S_a) \ge 68$ holds only for $a \in \{1, \dots, 12\}$ ($\log_2 U = 68.0106413$ at $a = 12$, $k_{12} = 144,512,437,361$, vs. $\log_2 U = 67.9550938 < 68$ at $a = 13$, $k_{13} = 151,099,256,031$). Thus Theorem 2 **unconditionally eliminates $17$ of the $29$ candidate cycle pairs** ($a \in \{13, \dots, 29\}$) on the primary $(k_{21}, k_{22})$ ray (Figure 2(b)).

3. **The $X_0 = 2^{71.5}$ Threshold and Comparison with Hercher [8, Corollary 29]:**
   By the Farey-mediant analysis in item 2, the **only** coprime pairs $(k_0, S_0)$ with $2^{S_0} > 3^{k_0}$, $S_0/k_0 < S_{21}/k_{21}$, and $k_0 < k_{23} = 137,528,045,312$ are the first two points $a = 1$ and $a = 2$ on the $b = 1$ ray $(k_a, S_a) = a(k_{21}, S_{21}) + (k_{22}, S_{22})$ (since $a \ge 3, b = 1$ gives $k_a \ge 3 k_{21} + k_{22} = 85,231,069,331$, where $\log_2 x_{\min}^{\mathrm{Eliahou}}(k_a, S_a) \le \log_2 x_{\min}^{\mathrm{Eliahou}}(k_3, S_3) = 69.9019345 < 71.5$ and $\log_2 U(k_3, S_3) = 69.4307008$). At $a = 1$ ($(k_1, S_1) = (72,057,431,991,\; 114,208,327,604)$, $k_1 + S_1 = 186,265,759,595$) and $a = 2$ ($(k_2, S_2) = (78,644,250,661,\; 124,648,188,195)$), we have
   $$
   \log_2 x_{\min}^{\mathrm{Eliahou}}(k_1, S_1) = 71.8843175 > 71.5 > \log_2 U(k_1, S_1) = 71.4130838, \qquad \log_2 U(k_2, S_2) = 70.0349468 < 71.5.
   $$
   Thus $X_0 = 2^{71.5}$ analytically eliminates every pair with $k < k_{23}$ under Theorem 2 alone, pushing the global minimum cycle length to $(k_{23}, S_{23}) = (137,528,045,312,\; 217,976,794,617)$ ($k + S = 355,504,839,929$). As noted in Section 2.2, Hercher [8, Section 5, Corollary 29] already established the same bound $k + S \ge 355,504,839,929$ at the lower verification threshold $X_0 \ge 3 \cdot 2^{69} \approx 2^{70.58496}$ by combining the local-minima product inequality with the Baker-type exclusion of $m \le 91$, whereas our $X_0 = 2^{71.5}$ exclusion uses the pure balanced-word bracket $U(k_0, S_0)$ without any bound on $m$.

![Cross-Parent Farey Obstruction and Candidate Ray Elimination](supplement/figure-2.png)


## 5. Stern–Brocot Matrix Recursions and Total Coprimality of Sturmian Cycles

In this section, we investigate the exact arithmetic divisibility of the Sturmian cycle numerator $C(a^{\mathrm{Sturm}}(k, S))$ by the cycle denominator $D(k, S) = 2^S - 3^k$.
We uncover an algebraic phenomenon: the vector
$$
\mathbf{v}(k, S) := \begin{pmatrix} C(a^{\mathrm{Sturm}}(k, S)) \\ 3^k - 2^S \end{pmatrix} \in \mathbb{Z}^2
$$
obeys an exact weighted mediant concatenation law along the branches of the Stern–Brocot tree, generating a $(2, 3)$-smooth determinant identity (invertible in $\mathbb{Z}[1/6]$) that completely excludes Sturmian integer cycles.

### 5.1 The Stern–Brocot Concatenation Law

Recall that the Stern–Brocot tree organizes all positive reduced fractions. A fraction $S/k$ with $\gcd(k, S) = 1$ has two Farey parents: a left parent $q_1/h_1$ and a right parent $q_2/h_2$, satisfying
$$
k = h_1 + h_2, \quad S = q_1 + q_2, \quad \text{and} \quad h_1 q_2 - h_2 q_1 = 1.
$$
Equivalently, $h_1 S - k q_1 = 1$, so $h_1 \equiv S^{-1} \pmod k$ and $q_1 = \lfloor h_1 S / k \rfloor$.
By classical combinatorics on words (Borel and Laubie [18], Berstel and de Luca [19]), the lower Christoffel word $a^{\mathrm{Sturm}}(k, S)$ factorizes canonically as the concatenation of its parents' Christoffel words:
$$
a^{\mathrm{Sturm}}(k, S) = a^{\mathrm{Sturm}}(h_1, q_1) \cdot a^{\mathrm{Sturm}}(h_2, q_2).
$$
Specifically, for $0 \le j < h_1$, $S_j(a^{\mathrm{Sturm}}(k, S)) = S_j(a^{\mathrm{Sturm}}(h_1, q_1))$, and at $j = h_1$, $S_{h_1} = q_1$. For $j = h_1 + i$ ($0 \le i < h_2$), $S_{h_1 + i}(a^{\mathrm{Sturm}}(k, S)) = q_1 + S_i(a^{\mathrm{Sturm}}(h_2, q_2))$.
Splitting the sum defining $C(a^{\mathrm{Sturm}}(k, S))$ at $j = h_1$:
$$
C(a^{\mathrm{Sturm}}(k, S)) = \sum_{j=0}^{h_1-1} 3^{h_1 + h_2 - 1 - j} 2^{S_j} + \sum_{i=0}^{h_2-1} 3^{h_2 - 1 - i} 2^{q_1 + S_i}
$$
$$
= 3^{h_2} C(a^{\mathrm{Sturm}}(h_1, q_1)) + 2^{q_1} C(a^{\mathrm{Sturm}}(h_2, q_2)).
$$
Notice that the second component $3^k - 2^S = 3^{h_1 + h_2} - 2^{q_1 + q_2}$ satisfies the *exact same weighted linear combination* with weights $(3^{h_2}, 2^{q_1})$, because the cross terms $-3^{h_2} 2^{q_1}$ and $+2^{q_1} 3^{h_2}$ cancel identically:
$$
3^{h_2} (3^{h_1} - 2^{q_1}) + 2^{q_1} (3^{h_2} - 2^{q_2}) = 3^{h_1 + h_2} - 3^{h_2} 2^{q_1} + 2^{q_1} 3^{h_2} - 2^{q_1 + q_2} = 3^k - 2^S.
$$
We state this as a theorem:

**Theorem 3 (Stern–Brocot Recursion, $(2, 3)$-Smooth Farey Determinants, and Universal Coprimality).** *Let $k \ge 2$ and $k < S < 2k$ with $\gcd(k, S) = 1$. Let $(h_1, q_1)$ and $(h_2, q_2)$ be the left and right Farey parents of $(k, S)$ in the Stern–Brocot tree, so $k = h_1 + h_2$, $S = q_1 + q_2$, and $h_1 q_2 - h_2 q_1 = 1$.*

1. **Weighted Mediant Vector Recursion:**
   $$
   \mathbf{v}(k, S) = \begin{pmatrix} C(a^{\mathrm{Sturm}}(k, S)) \\ 3^k - 2^S \end{pmatrix} = 3^{h_2} \begin{pmatrix} C(a^{\mathrm{Sturm}}(h_1, q_1)) \\ 3^{h_1} - 2^{q_1} \end{pmatrix} + 2^{q_1} \begin{pmatrix} C(a^{\mathrm{Sturm}}(h_2, q_2)) \\ 3^{h_2} - 2^{q_2} \end{pmatrix}.
   $$

2. **Left Farey $(2, 3)$-Smooth Determinant Identity:**
   $$
   \det \begin{pmatrix} C(a^{\mathrm{Sturm}}(k, S)) & C(a^{\mathrm{Sturm}}(h_1, q_1)) \\ 3^k - 2^S & 3^{h_1} - 2^{q_1} \end{pmatrix} = 3^{h_1 - 1} 2^{S - 1}.
   $$
   *Equivalently:*
   $$
   (3^{h_1} - 2^{q_1}) C(a^{\mathrm{Sturm}}(k, S)) + (2^S - 3^k) C(a^{\mathrm{Sturm}}(h_1, q_1)) = 3^{h_1 - 1} 2^{S - 1}.
   $$

3. **Right Farey $(2, 3)$-Smooth Determinant Identity:**
   $$
   \det \begin{pmatrix} C(a^{\mathrm{Sturm}}(k, S)) & C(a^{\mathrm{Sturm}}(h_2, q_2)) \\ 3^k - 2^S & 3^{h_2} - 2^{q_2} \end{pmatrix} = -3^{k - 1} 2^{q_2 - 1}.
   $$
   *Equivalently:*
   $$
   (2^{q_2} - 3^{h_2}) C(a^{\mathrm{Sturm}}(k, S)) - (2^S - 3^k) C(a^{\mathrm{Sturm}}(h_2, q_2)) = 3^{k - 1} 2^{q_2 - 1}.
   $$

4. **Universal Coprimality and Non-Integrality for Positive Cycles:**
   $$
   \gcd\left( C(a^{\mathrm{Sturm}}(k, S)), \; |2^S - 3^k| \right) = 1.
   $$
   *Consequently, for any pair $(k, S) = (d k_0, d S_0)$ with $d = \gcd(k, S) \ge 1$ and $k_0 \ge 2$, the rational cycle $x_r(a^{\mathrm{Sturm}}(k, S)) = x_r(a^{\mathrm{Sturm}}(k_0, S_0))$ has reduced denominator $|2^{S_0} - 3^{k_0}|$. For all positive-cycle slopes ($2^S > 3^k$ with $k_0 \ge 2$, so $k_0 \ge 3, S_0 \ge 5$), we have $2^{S_0} - 3^{k_0} \ge 5 > 1$, so $a^{\mathrm{Sturm}}(k, S)$ is never a positive integer cycle (whereas for $2^S < 3^k$, the unique pair with $|2^{S_0} - 3^{k_0}| = 1$ by Levi ben Gerson's theorem [21] is $(k_0, S_0) = (2, 3)$ with $2^3 - 3^2 = -1$, corresponding to the negative integer cycle $-5 \to -7 \to -5$).*

*Proof.*
Part 1 was established above by direct summation on $a^{\mathrm{Sturm}}(k, S) = a^{\mathrm{Sturm}}(h_1, q_1) \cdot a^{\mathrm{Sturm}}(h_2, q_2)$ and the identity $3^{h_2}(3^{h_1} - 2^{q_1}) + 2^{q_1}(3^{h_2} - 2^{q_2}) = 3^k - 2^S$.

For Parts 2 and 3, we first prove by induction on the depth in the Stern–Brocot tree that for every Farey-adjacent parent pair $((h_1, q_1), (h_2, q_2))$ with $h_1 q_2 - h_2 q_1 = 1$,
$$
\det\left( \mathbf{v}(h_1, q_1), \; \mathbf{v}(h_2, q_2) \right) = -3^{h_1 - 1} 2^{q_2 - 1}.
$$
- **Base case:** At the root of the interval $(1, 2)$, the Farey parents are $(h_1, q_1) = (1, 1)$ (word $(1)$, $\mathbf{v}(1, 1) = (1, 3^1 - 2^1)^T = (1, 1)^T$) and $(h_2, q_2) = (1, 2)$ (word $(2)$, $\mathbf{v}(1, 2) = (1, 3^1 - 2^2)^T = (1, -1)^T$), where
  $$
  \det \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = -2 = -3^{1 - 1} 2^{2 - 1}.
  $$
- **Inductive step:** Given $(h_1, q_1)$ and $(h_2, q_2)$ with mediant $(k, S) = (h_1 + h_2, q_1 + q_2)$, Part 1 gives $\mathbf{v}(k, S) = 3^{h_2} \mathbf{v}(h_1, q_1) + 2^{q_1} \mathbf{v}(h_2, q_2)$. There are two child sub-intervals:
  1. *Left sub-interval $((h_1', q_1'), (h_2', q_2')) = ((h_1, q_1), (k, S))$:* Here $h_1' = h_1$ and $q_2' = q_1 + q_2 = S$. By multilinearity of the determinant,
     $$
     \det\left(\mathbf{v}(h_1, q_1), \; \mathbf{v}(k, S)\right) = \det\left(\mathbf{v}(h_1, q_1), \; 2^{q_1} \mathbf{v}(h_2, q_2)\right) = 2^{q_1}\left(-3^{h_1 - 1} 2^{q_2 - 1}\right) = -3^{h_1' - 1} 2^{q_2' - 1}.
     $$
  2. *Right sub-interval $((h_1', q_1'), (h_2', q_2')) = ((k, S), (h_2, q_2))$:* Here $h_1' = h_1 + h_2 = k$ and $q_2' = q_2$. By multilinearity,
     $$
     \det\left(\mathbf{v}(k, S), \; \mathbf{v}(h_2, q_2)\right) = \det\left(3^{h_2} \mathbf{v}(h_1, q_1), \; \mathbf{v}(h_2, q_2)\right) = 3^{h_2}\left(-3^{h_1 - 1} 2^{q_2 - 1}\right) = -3^{h_1' - 1} 2^{q_2' - 1}.
     $$
This completes the induction. Reversing the column order in the left sub-interval identity gives $\det(\mathbf{v}(k, S), \mathbf{v}(h_1, q_1)) = -\det(\mathbf{v}(h_1, q_1), \mathbf{v}(k, S)) = 3^{h_1 - 1} 2^{S - 1}$ (Part 2), and the right sub-interval identity directly gives $\det(\mathbf{v}(k, S), \mathbf{v}(h_2, q_2)) = -3^{k - 1} 2^{q_2 - 1}$ (Part 3).

For Part 4, let $g = \gcd(C(a^{\mathrm{Sturm}}(k, S)), |2^S - 3^k|)$. From the Left Farey Determinant Identity (Part 2):
$$
(3^{h_1} - 2^{q_1}) C(a^{\mathrm{Sturm}}(k, S)) + (2^S - 3^k) C(a^{\mathrm{Sturm}}(h_1, q_1)) = 3^{h_1 - 1} 2^{S - 1}.
$$
Since $g$ divides both $C(a^{\mathrm{Sturm}}(k, S))$ and $2^S - 3^k$, $g$ must divide the integer linear combination on the left-hand side, and hence $g \mid 3^{h_1 - 1} 2^{S - 1}$. Thus every prime divisor of $g$ belongs to $\{2, 3\}$. However, $\gcd(|2^S - 3^k|, 6) = 1$ for all $k, S \ge 1$, so $\gcd(g, 6) = 1$, forcing $g = 1$. By Levi ben Gerson's theorem [21], $|2^{S_0} - 3^{k_0}| = 1$ for $k_0 \ge 2$ occurs solely at $(k_0, S_0) = (2, 3)$ ($2^3 - 3^2 = -1$, where $C(1, 2) = 5$ gives $x_0 = -5$), whereas for $2^{S_0} > 3^{k_0}$ and $k_0 \ge 2$, $2^{S_0} - 3^{k_0} \ge 2^5 - 3^3 = 5 > 1$. $\quad \square$

**Remark 1 (Comparison with Knight's Reversal Proof [26] and Role of the Farey Determinant Identities).**
Knight [26] independently proved Part 4 of Theorem 3 (that balanced "high" cycles are never positive integer cycles) via the reversal identity $3 M_{S, k} - N_{\mathrm{rev}} + (2^S - 3^k) = 2^{S-1}$, which relates $M_{S, k} = C(a^{\mathrm{Sturm}}(k, S))$ to the numerator $N_{\mathrm{rev}}$ of its reversed shift. While that reversal relation suffices for $a^{\mathrm{Sturm}}(k, S)$ itself (since shift invariance implies $(2^S - 3^k) \mid M_{S, k} \iff (2^S - 3^k) \mid N_{\mathrm{rev}}$), it relates $M_{S, k}$ to a different cyclic shift and therefore cannot eliminate $C(a^{\mathrm{Sturm}}(k, S))$ when $a^{\mathrm{Sturm}}(k, S)$ is modified by a single transposition $C(a) = C(a^{\mathrm{Sturm}}(k, S)) - 3^{k - 1 - j_1} 2^{S_{j_1} - 1}$. By contrast, Parts 2 and 3 of Theorem 3 invert $C(a^{\mathrm{Sturm}}(k, S))$ *directly* modulo $D = 2^S - 3^k$ via the Farey parent factors $d_1 = 3^{h_1} - 2^{q_1}$ and $d_2 = 2^{q_2} - 3^{h_2}$ into the pure $(2, 3)$-monomials $3^{h_1 - 1} 2^{S - 1}$ and $3^{k - 1} 2^{q_2 - 1}$. This direct modular inversion is the essential algebraic input that enables the 4-way Farey tent reduction and single-transposition exclusion in Section 7 (Theorem 5).

**Batched $O(\log k_0)$ Continued-Fraction Algorithm.**
Whereas stepping one mediant at a time in the Stern–Brocot tree takes $\sum a_i$ steps, grouping the $a \ge 1$ consecutive mediants corresponding to a single continued-fraction partial quotient $a$ telescopes via the finite geometric series $\sum_{m=0}^{a-1} 3^{(a-1-m)h_i} 2^{m q_i} = \frac{3^{a h_i} - 2^{a q_i}}{3^{h_i} - 2^{q_i}}$ into a single closed-form step:
- Appending $a \ge 1$ copies of the right parent $\mathbf{v}(h_2, q_2)$ to the left parent $\mathbf{v}(h_1, q_1)$ (producing the Christoffel word at $(h_1 + a h_2, q_1 + a q_2)$) yields
  $$
  \mathbf{v}(h_1 + a h_2,\; q_1 + a q_2) = 3^{a h_2} \mathbf{v}(h_1, q_1) + 2^{q_1} \frac{3^{a h_2} - 2^{a q_2}}{3^{h_2} - 2^{q_2}} \mathbf{v}(h_2, q_2).
  $$
- Symmetrically, prepending $a \ge 1$ copies of the left parent $\mathbf{v}(h_1, q_1)$ to the right parent $\mathbf{v}(h_2, q_2)$ (producing the Christoffel word at $(a h_1 + h_2, a q_1 + q_2)$) yields
  $$
  \mathbf{v}(a h_1 + h_2,\; a q_1 + q_2) = 3^{h_2} \frac{3^{a h_1} - 2^{a q_1}}{3^{h_1} - 2^{q_1}} \mathbf{v}(h_1, q_1) + 2^{a q_1} \mathbf{v}(h_2, q_2).
  $$
Because the divisor $3^{h_i} - 2^{q_i}$ is already the second coordinate of $\mathbf{v}(h_i, q_i)$, evaluating $3^{a h_i}$ and $2^{a q_i}$ by binary exponentiation computes Halbeisen and Hungerbühler's numerator $M_{S_0, k_0} = C(a^{\mathrm{Sturm}}(k_0, S_0))$ and $x_{\min}(a^{\mathrm{Sturm}}(k, S)) = C(a^{\mathrm{Sturm}}(k_0, S_0)) / (2^{S_0} - 3^{k_0})$ in $O(N) = O(\log k_0)$ arithmetic operations, where $N$ is the number of continued-fraction partial quotients of $S_0/k_0$.

---

## 6. Fixed-Point Homogenization, Discrepancy Bounds, and $m$-Cycle Interpolation

We now establish structural connections between the Sturmian apex and the clustered $m$-cycle regime by shifting the trajectory to the fixed points of the affine Syracuse step maps.

### 6.1 Fixed-Point Homogenization Identities

The Syracuse step $x_{j+1} = (3x_j + 1)/2^{a_j}$ can be viewed as an affine map $f_a(x) = \frac{3}{2^a} x + \frac{1}{2^a}$. The unique fixed point of $f_a$ in $\mathbb{Q}$ is
$$
\xi_a = \frac{1}{2^a - 3}.
$$
- For $a = 1$ (ascent step), the fixed point is $\xi_1 = \frac{1}{2 - 3} = -1$.
- For $a = 2$ (gentle descent step), the fixed point is $\xi_2 = \frac{1}{4 - 3} = +1$ (the trivial cycle).

Shifting the state variable $x_j$ by these fixed points annihilates all steps with $a_j = 1$ or $a_j = 2$:

**Theorem 4 (Fixed-Point Homogenization and $m$-Block Discrepancy Bounds).** *Let $a \in \mathcal{A}(k, S)$ with $2^S > 3^k$ and $k < S < 2k$.*

1. **Homogenization at $\xi_1 = -1$:**
   $$
   (2^S - 3^k) \frac{x_0 + 1}{2} = \sum_{j : a_j \ge 2} 3^{k-1-j} 2^{S_j} \left(2^{a_j - 1} - 1\right).
   $$
   *Every step with $a_j = 1$ vanishes identically. The sum is supported solely on the $m_+ = |\{j : a_j \ge 2\}| \le S - k$ descent steps.*

2. **Homogenization at $\xi_2 = +1$:**
   $$
   (2^S - 3^k) \frac{x_0 - 1}{2} = \sum_{j : a_j = 1} 3^{k-1-j} 2^{S_j} - \sum_{j : a_j \ge 3} 3^{k-1-j} 2^{S_j + 1} \left(2^{a_j - 2} - 1\right).
   $$
   *Every step with $a_j = 2$ vanishes identically.*

3. **$m_+$-Descent Discrepancy Bound:**
   *Decompose $a$ up to cyclic shift into $m_+$ blocks of lengths $L_1, \dots, L_{m_+}$ ($L_r \ge 1, \sum L_r = k$), each consisting of $L_r - 1$ ones followed by a single step $b_r \ge 2$. At the discrepancy peak shift $r_+$ (where $S_j \le \lfloor jS/k \rfloor$ for all $j$):*
   $$
   \mu(a) \le \sum_{r=1}^{m_+} 3^{k - j_r} 2^{\lfloor j_r S / k \rfloor} \left(1 - \left(\frac{2}{3}\right)^{L_r}\right) < m_+ \cdot 2^S \implies x_{\min}(a) < \frac{m_+ \cdot 2^S}{2^S - 3^k}.
   $$

4. **$m$-Cycle Discrepancy Bound:**
   *For an $m$-cycle consisting of $m$ alternating blocks of ascents ($a_j = 1$) of lengths $\ell_1, \dots, \ell_m$ and descents ($a_j \ge 2$) of lengths $d_1, \dots, d_m$:*
   $$
   \mu(a) < 2m \cdot 2^S \implies x_{\min}(a) < \frac{2m \cdot 2^S}{2^S - 3^k} = 2m + \frac{2m \cdot 3^k}{2^S - 3^k} < 2m + \frac{6m}{k} x_{\min}^{\mathrm{Eliahou}}(k, S).
   $$

*Proof.*
For Part 1, rewrite the Syracuse step in terms of $y_j = x_j + 1$:
$$
2^{a_j} (x_{j+1} + 1) = 3 x_j + 1 + 2^{a_j} = 3(x_j + 1) + (2^{a_j} - 2).
$$
Multiplying by $3^{k-1-j} 2^{S_j}$ and summing over $0 \le j \le k-1$:
$$
\sum_{j=0}^{k-1} 3^{k-1-j} 2^{S_{j+1}} (x_{j+1} + 1) - \sum_{j=0}^{k-1} 3^{k-j} 2^{S_j} (x_j + 1) = \sum_{j=0}^{k-1} 3^{k-1-j} 2^{S_j} (2^{a_j} - 2).
$$
The left-hand side telescopes to $(2^S - 3^k)(x_0 + 1)$. When $a_j = 1$, $2^{a_j} - 2 = 0$. Dividing by $2$ proves Part 1. Part 2 follows identically using $w_j = x_j - 1$.

For Part 3, apply Raney's lemma to the discrepancy $U_i = k S_i - i S$. Since $S/k > 1$, on every $a_i = 1$ step the discrepancy strictly decreases: $U_{i+1} - U_i = k - S < 0$. Therefore, the global maximum of $U_i$ can never occur inside a run of $1$s—it must occur at the start $j_r$ of one of the $m_+$ blocks $(1, \dots, 1, b_r)$.
Shift $a$ so that this maximum is at index $0$. Then at every block start $j_r$, $S_{j_r} \le \lfloor j_r S / k \rfloor$.
On the $r$-th block of length $L_r$, the first $L_r - 1$ steps have $a = 1$, so $S_{j_r + t} = S_{j_r} + t$ for $0 \le t \le L_r - 1$.
The sum of $3^{k-1-j} 2^{S_j}$ over the $r$-th block is
$$
\sum_{t=0}^{L_r - 1} 3^{k - 1 - j_r - t} 2^{S_{j_r} + t} = 3^{k - j_r} 2^{S_{j_r}} \left(1 - \left(\frac{2}{3}\right)^{L_r}\right) \le 3^{k - j_r} 2^{\lfloor j_r S / k \rfloor} \left(1 - \left(\frac{2}{3}\right)^{L_r}\right).
$$
Because $3^{k - j_r} 2^{\lfloor j_r S / k \rfloor} \le 3^{k - j_r} 2^{j_r S / k} = 3^k (2^S/3^k)^{j_r/k} < 2^S$, summing over $r = 1, \dots, m_+$ yields $\mu(a) < 2^S \sum_{r=1}^{m_+} (1 - (2/3)^{L_r}) < m_+ \cdot 2^S$.
For Part 4, bounding the descent phase backwards from $j_{r+1}$ using $S_{j_{r+1} - s} \le S_{j_{r+1}} - 2s$ contributes at most $2^S (1 - (3/4)^{d_r}) < 2^S$ per block, so $\mu(a) < 2m \cdot 2^S$. Dividing by $2^S - 3^k$ gives $x_{\min}(a) < \frac{2m \cdot 2^S}{2^S - 3^k} = 2m + \frac{2m \cdot 3^k}{2^S - 3^k}$. By Bernoulli's inequality $(1 + \delta)^k > 1 + k \delta$ applied to $1 + \delta = 2^{S/k}/3 > 1$ ($k \ge 2$), we have $\frac{2^S - 3^k}{3^k} = (2^{S/k}/3)^k - 1 > \frac{k}{3}(2^{S/k} - 3)$, so $\frac{3^k}{2^S - 3^k} < \frac{3}{k(2^{S/k} - 3)} = \frac{3}{k} x_{\min}^{\mathrm{Eliahou}}(k, S)$, proving $\frac{2m \cdot 2^S}{2^S - 3^k} < 2m + \frac{6m}{k} x_{\min}^{\mathrm{Eliahou}}(k, S)$. $\quad \square$

Theorem 4 establishes an immediate diophantine consequence for $m$-cycles: if an $m$-cycle satisfies $x_{\min}(a) \ge X_0 > 2m$, then Part 4 gives $\frac{2^S - 3^k}{3^k} = e^{S\ln 2 - k\ln 3} - 1 < \frac{2m}{X_0 - 2m}$, so
$$
0 < S \ln 2 - k \ln 3 < \ln\left(1 + \frac{2m}{X_0 - 2m}\right) < \frac{2m}{X_0 - 2m}.
$$
Coupling this upper bound on $S\ln 2 - k\ln 3$ with Rhin's linear-forms-in-logarithms lower bound $S\ln 2 - k\ln 3 > c_{\mathrm{Rhin}} k^{-13.3}$ [20] yields the explicit lower bound $k > (c_{\mathrm{Rhin}}(X_0 - 2m)/(2m))^{1/13.3}$ for fixed $m$ in terms of $X_0$.


## 7. The 4-Way Farey Tent Envelope and Single-Transposition Perturbation Exclusions

In Theorem 3, we proved that the Sturmian word $a^{\mathrm{Sturm}}(k, S)$ satisfies $\gcd(C(a^{\mathrm{Sturm}}), 2^S - 3^k) = 1$. We now investigate single-transposition ($t=1$) perturbations around $a^{\mathrm{Sturm}}(k, S)$, asking whether swapping any adjacent $(2, 1)$ pair in $a^{\mathrm{Sturm}}(k, S)$ can ever produce an integer cycle.

### 7.1 Explicit Definition and Derivation of the Four Reduced Farey Integers

A single-transposition ($t=1$) downward perturbation of $a^{\mathrm{Sturm}}(k, S)$ at index $j_1 \in \{1, \dots, k-1\}$ (where $(a_{j_1 - 1}^{\mathrm{Sturm}}, a_{j_1}^{\mathrm{Sturm}}) = (2, 1)$) is obtained by swapping $(a_{j_1 - 1}, a_{j_1})$ to $(1, 2)$. This decreases the single cumulative valuation $S_{j_1} = \lfloor j_1 S / k \rfloor$ by $1$, while keeping $S_j = \lfloor jS/k \rfloor$ unchanged for all $j \ne j_1$.
By Lemma 2, the perturbed cycle numerator is
$$
C(a) = C(a^{\mathrm{Sturm}}(k, S)) - 3^{k - 1 - j_1} 2^{S_{j_1} - 1}, \quad \text{where } S_{j_1} = \left\lfloor \frac{j_1 S}{k} \right\rfloor.
$$
Let $D = D(k, S) = 2^S - 3^k > 0$, and let $d_1 := 3^{h_1} - 2^{q_1}$ and $d_2 := 2^{q_2} - 3^{h_2}$ denote the Left and Right Farey parent factors from Theorem 3. We define four explicit integers associated with the perturbation index $j_1$:
1. **Left-Parent $2^S$-form:**
   $$
   R_A(j_1) := \begin{cases} 3^{h_2 - j_1} (3^{h_1} - 2^{q_1}) - 2^{S - S_{j_1}}, & j_1 \le h_2, \\ (3^{h_1} - 2^{q_1}) - 3^{j_1 - h_2} 2^{S - S_{j_1}}, & j_1 > h_2. \end{cases}
   $$
2. **Left-Parent $3^k$-form:**
   $$
   R_B(j_1) := 3^{h_1 + j_1} - 2^{S_{j_1}} (3^{h_1} - 2^{q_1}).
   $$
3. **Right-Parent $3^k$-form:**
   $$
   Q_A(j_1) := \begin{cases} 3^{j_1} 2^{q_2 - S_{j_1}} - (2^{q_2} - 3^{h_2}), & S_{j_1} \le q_2, \\ 3^{j_1} - 2^{S_{j_1} - q_2} (2^{q_2} - 3^{h_2}), & S_{j_1} > q_2. \end{cases}
   $$
4. **Right-Parent $2^S$-form:**
   $$
   Q_B(j_1) := 2^{S + q_2 - S_{j_1}} - 3^{k - j_1} (2^{q_2} - 3^{h_2}).
   $$

Figure 2(a) in the supplement plots $\log_2 |R_A(j_1)|, \log_2 |R_B(j_1)|, \log_2 |Q_A(j_1)|$ and the 4-way minimum envelope on the convergent $(k_5, S_5) = (41, 65)$. The green diamond envelope is strictly bounded below $41.2$ bits, far below $\log_2(2^{65} - 3^{41}) = 58.54$ bits.

### 7.2 Proof of the 4-Way Farey Tent Reduction and Single-Transposition Exclusion Theorem

**Theorem 5 (4-Way Farey Tent Reduction and Single-Transposition Exclusion).** *Let $k \ge 6$ and $k < S < 2k$ with $\gcd(k, S) = 1$ and $D = 2^S - 3^k > 0$. For any single-transposition ($t=1$) downward perturbation $a$ of $a^{\mathrm{Sturm}}(k, S)$ at index $j_1 \in \{1, \dots, k-1\}$:*

1. **Exact GCD Equivalence, Boundary Avoidance, and Non-Vanishing:**
   *Every downward transposition index $j_1$ satisfies $j_1 \ne h_2$ and $S_{j_1} \ne q_2$ (with $j_1 < h_2 \iff S_{j_1} < q_2$). Each of $R_A(j_1), R_B(j_1), Q_A(j_1), Q_B(j_1)$ is a non-zero integer coprime to $6$, and*
   $$
   \gcd(C(a), D) = \gcd(R_A(j_1), D) = \gcd(R_B(j_1), D) = \gcd(Q_A(j_1), D) = \gcd(Q_B(j_1), D).
   $$

2. **Universal 4-Way Tent Bound:**
   $$
   1 \le \min\left( |R_A(j_1)|, \; |R_B(j_1)|, \; |Q_A(j_1)|, \; |Q_B(j_1)| \right) < 2^{\min\left(\max(q_1, q_2),\; \frac{S + \min(q_1, q_2)}{2}\right) + 2} \le 2^{\frac{2}{3}S + 2}.
   $$

3. **Single-Transposition Exclusion:**
   *Whenever $M_4(j_1) := \min(|R_A(j_1)|, |R_B(j_1)|, |Q_A(j_1)|, |Q_B(j_1)|) < 2^S - 3^k$—which holds unconditionally whenever $2^{\frac{2}{3}S + 2} \le 2^S - 3^k$ (in particular for all $k$ satisfying $\frac{1}{3}S - 13.3\log_2 k \ge 3 - \log_2 c_{\mathrm{Rhin}}$ under Rhin's effective irrationality measure $S\ln 2 - k\ln 3 > c_{\mathrm{Rhin}} k^{-13.3}$ [20]), and is verified exhaustively along with $D \nmid C(a)$ across all $56,304$ downward perturbations for all $2,842$ admissible coprime pairs $(k, S)$ in $6 \le k \le 150$—we have $D \nmid C(a)$, so $a$ cannot generate an integer cycle.*

*Proof.*
**Part 1 (GCD Equivalence, Boundary Avoidance, and Non-Vanishing):**
By Theorem 3 Part 2, $d_1 C(a^{\mathrm{Sturm}}) + D \cdot C(a^{\mathrm{Sturm}}(h_1, q_1)) = 3^{h_1 - 1} 2^{S - 1}$, so $\gcd(d_1, D) = 1$, and symmetrically Theorem 3 Part 3 implies $\gcd(d_2, D) = 1$.
Multiplying $C(a) = C(a^{\mathrm{Sturm}}) - 3^{k - 1 - j_1} 2^{S_{j_1} - 1}$ by $2 d_1$ and substituting $2 d_1 C(a^{\mathrm{Sturm}}) \equiv 3^{h_1 - 1} 2^S \pmod D$ gives
$$
2 d_1 C(a) \equiv 3^{h_1 - 1} 2^S - 3^{k - 1 - j_1} 2^{S_{j_1}} d_1 \pmod D.
$$
Since $k = h_1 + h_2$, $(k - 1 - j_1) - (h_1 - 1) = h_2 - j_1$. Factoring out the invertible $(2, 3)$-monomial $-3^{\min(h_1 - 1, k - 1 - j_1)} 2^{S_{j_1}}$ modulo $D$ yields $R_A(j_1)$; substituting $2^S \equiv 3^k \pmod D$ and factoring out $3^{k - 1 - j_1}$ yields $R_B(j_1)$.
Symmetrically, multiplying $C(a)$ by $2 d_2$ and substituting $2 d_2 C(a^{\mathrm{Sturm}}) \equiv 3^{k - 1} 2^{q_2} \pmod D$ gives
$$
2 d_2 C(a) \equiv 3^{k - 1} 2^{q_2} - 3^{k - 1 - j_1} 2^{S_{j_1}} d_2 \pmod D.
$$
Factoring out $3^{k - 1 - j_1} 2^{\min(q_2, S_{j_1})}$ yields $Q_A(j_1)$, while substituting $3^{k} \equiv 2^S \pmod D$ and factoring out $3^{-1} 2^{S_{j_1}}$ yields $Q_B(j_1)$. Because $2, 3, d_1, d_2$ are units modulo $D$, all four integers share the exact same greatest common divisor with $D$ as $C(a)$.

Next, from $h_1 q_2 - h_2 q_1 = 1$ with $k = h_1 + h_2$ and $S = q_1 + q_2$, we have $h_2 S = k q_2 - 1$. Thus
$$
S_{h_2} = \left\lfloor \frac{k q_2 - 1}{k} \right\rfloor = q_2 - 1, \qquad S_{h_2 + 1} = \left\lfloor q_2 + \frac{S - 1}{k} \right\rfloor = q_2 + 1 \quad (\text{since } k < S < 2k \implies 1 \le \frac{S-1}{k} < 2).
$$
Consequently, $a_{h_2}^{\mathrm{Sturm}} = S_{h_2 + 1} - S_{h_2} = 2 \ne 1$. Because a downward transposition at $j_1$ requires $(a_{j_1 - 1}^{\mathrm{Sturm}}, a_{j_1}^{\mathrm{Sturm}}) = (2, 1)$, we have $a_{j_1}^{\mathrm{Sturm}} = 1 \ne a_{h_2}^{\mathrm{Sturm}}$, which forces $j_1 \ne h_2$ and $S_{j_1} \ne q_2$ (with $j_1 < h_2 \iff S_{j_1} \le q_2 - 1 < q_2$ and $j_1 > h_2 \iff S_{j_1} \ge q_2 + 1 > q_2$). Also $a_{j_1 - 1}^{\mathrm{Sturm}} = 2 \implies 2 \le S_{j_1} \le S - 1$, and $h_1, q_1, h_2, q_2 \ge 1$ makes $d_1 = 3^{h_1} - 2^{q_1}$ and $d_2 = 2^{q_2} - 3^{h_2}$ coprime to $6$. Because $|h_2 - j_1| \ge 1$, $|q_2 - S_{j_1}| \ge 1$, $S_{j_1} \ge 2$, and $S - S_{j_1} \ge 1$, in every one of $R_A(j_1), R_B(j_1), Q_A(j_1), Q_B(j_1)$ one term is even and the other is odd, and one term is divisible by $3$ while the other is coprime to $3$. Thus all four integers are coprime to $6$ and strictly non-zero.

**Part 2 (Universal 4-Way Tent Bound):**
Since $3^k < 2^S$, we have $3^m < 2^{m S / k}$ for every $m \ge 1$. Moreover, $h_1 S / k = q_1 + 1/k$ and $h_2 S / k = q_2 - 1/k$ give $3^{h_1} < 2^{q_1 + 1/k} < 2^{q_1 + 1}$ and $3^{h_2} < 2^{q_2}$, so $|d_1| < 2^{q_1 + 1}$ and $|d_2| < 2^{q_2}$. Using $j_1 S / k - 1 < S_{j_1} \le j_1 S / k$, we bound the four integers in the two disjoint regimes $j_1 < h_2$ and $j_1 > h_2$:
1. **Case A ($j_1 < h_2$, so $S_{j_1} < q_2$):**
   - In $Q_A(j_1) = 3^{j_1} 2^{q_2 - S_{j_1}} - d_2$, we have $3^{j_1} 2^{q_2 - S_{j_1}} < 2^{j_1 S/k - S_{j_1} + q_2} < 2^{q_2 + 1}$ and $|d_2| < 2^{q_2}$, so $|Q_A(j_1)| < 2^{q_2 + 1}$.
   - In $R_B(j_1) = 3^{h_1 + j_1} - 2^{S_{j_1}} d_1$, we have $3^{h_1 + j_1} < 2^{q_1 + 1/k + j_1 S/k} < 2^{q_1 + S_{j_1} + 2}$ and $2^{S_{j_1}} |d_1| < 2^{q_1 + S_{j_1} + 1}$, so $|R_B(j_1)| < 2^{q_1 + S_{j_1} + 2}$.
   - In $R_A(j_1) = 3^{h_2 - j_1} d_1 - 2^{S - S_{j_1}}$, we have $3^{h_2 - j_1} |d_1| < 2^{q_2 - j_1 S/k + q_1 + 1} \le 2^{S - S_{j_1} + 1}$, so $|R_A(j_1)| < 2^{S - S_{j_1} + 2}$.
   Hence on $j_1 < h_2$, $\min(|R_A(j_1)|, |R_B(j_1)|) < 2^{\min(q_1 + S_{j_1}, S - S_{j_1}) + 2} \le 2^{\frac{S + q_1}{2} + 2}$, and combining with $|Q_A(j_1)| < 2^{q_2 + 1}$ gives
   $$
   \min(|R_A(j_1)|, |R_B(j_1)|, |Q_A(j_1)|) < 2^{\min\left(q_2,\; \frac{S + q_1}{2}\right) + 2}.
   $$
2. **Case B ($j_1 > h_2$, so $S_{j_1} > q_2$):**
   - In $R_A(j_1) = d_1 - 3^{j_1 - h_2} 2^{S - S_{j_1}}$, we have $|d_1| < 2^{q_1 + 1}$ and $3^{j_1 - h_2} 2^{S - S_{j_1}} < 2^{(j_1 - h_2)S/k + S - S_{j_1}} = 2^{(j_1 S/k - S_{j_1}) + q_1 + 1/k} < 2^{q_1 + 2}$, so $|R_A(j_1)| < 2^{q_1 + 2}$.
   - In $Q_A(j_1) = 3^{j_1} - 2^{S_{j_1} - q_2} d_2$, we have $3^{j_1} < 2^{j_1 S/k} < 2^{S_{j_1} + 1}$ and $2^{S_{j_1} - q_2} |d_2| < 2^{S_{j_1}}$, so $|Q_A(j_1)| < 2^{S_{j_1} + 1}$.
   - In $Q_B(j_1) = 2^{S + q_2 - S_{j_1}} - 3^{k - j_1} d_2$, we have $3^{k - j_1} |d_2| < 2^{S - j_1 S/k + q_2} \le 2^{S + q_2 - S_{j_1}}$, so $|Q_B(j_1)| < 2^{q_2 + S - S_{j_1} + 1}$.
   Hence on $j_1 > h_2$, $\min(|Q_A(j_1)|, |Q_B(j_1)|) < 2^{\min(S_{j_1}, q_2 + S - S_{j_1}) + 1} \le 2^{\frac{S + q_2}{2} + 1}$, and combining with $|R_A(j_1)| < 2^{q_1 + 2}$ gives
   $$
   \min(|R_A(j_1)|, |Q_A(j_1)|, |Q_B(j_1)|) < 2^{\min\left(q_1,\; \frac{S + q_2}{2}\right) + 2}.
   $$

Finally, since $q_1 + q_2 = S$, if $q_1 \le q_2$ then $q_1 = \min(q_1, q_2) \le S/2 \le q_2 = \max(q_1, q_2)$, so $\min(q_2, \frac{S+q_1}{2}) = \min(\max(q_1, q_2), \frac{S+\min(q_1, q_2)}{2})$ and $\min(q_1, \frac{S+q_2}{2}) = q_1 \le \min(q_2, \frac{S+q_1}{2})$; symmetrically if $q_2 < q_1$. Thus in both Case A and Case B,
$$
\min(|R_A|, |R_B|, |Q_A|, |Q_B|) < 2^{\min\left(\max(q_1, q_2),\; \frac{S + \min(q_1, q_2)}{2}\right) + 2} \le 2^{\frac{2}{3}S + 2},
$$
since for $u = \min(q_1, q_2) \in [1, S/2]$, $\min(S - u, \frac{S + u}{2}) \le \frac{2}{3}S$ (maximized at $u = S/3$).

**Part 3 (Single-Transposition Exclusion):**
By Part 1, if $D \mid C(a)$, then $D$ must divide the non-zero integer $M_4(j_1) := \min(|R_A(j_1)|, |R_B(j_1)|, |Q_A(j_1)|, |Q_B(j_1)|) \ge 1$, requiring $D \le M_4(j_1) < 2^{\frac{2}{3}S + 2}$, which is impossible whenever $M_4(j_1) < D$ and in particular whenever $2^{\frac{2}{3}S + 2} \le D = 2^S - 3^k$. Under Rhin's effective irrationality measure $\delta = S\ln 2 - k\ln 3 > c_{\mathrm{Rhin}} k^{-13.3}$ [20], if $\delta \ge 1$ then $2^S - 3^k > 2^{S-1} \ge 2^{\frac{2}{3}S + 2}$ for $S \ge 9$, while if $\delta < 1$ then $2^S - 3^k = 2^S(1 - e^{-\delta}) > 2^{S-1} \delta > 2^{S-1} c_{\mathrm{Rhin}} k^{-13.3} \ge 2^{\frac{2}{3}S + 2}$ whenever $\frac{1}{3}S - 13.3\log_2 k \ge 3 - \log_2 c_{\mathrm{Rhin}}$. $\quad \square$

---

## 8. Limitations and Scope

We delineate the precise boundaries of our results:
1. **Beyond Single-Transposition Perturbations:** Our theorems characterize the clustered $m$-cycle regime ($m \ll k$) via Theorem 4, and the balanced Sturmian apex ($m = 2k - S$) and its single-transposition neighborhood via Theorems 1–3 and 5. For multi-transposition perturbations ($t \ge 2$) supported on windows $W = j_{\max} - j_{\min} + 1 > 1$ with valuation span $W_S = S_{j_{\max}} - S_{j_{\min}}$, the interior perturbation polynomial $\Delta_W = \sum_{i=1}^t 3^{j_{\max}-j_i} 2^{S_{j_i}-S_{j_{\min}}}$ satisfies $\gcd(\Delta_W, 6) = 1$, but its archimedean magnitude $\Delta_W \le 3^{W-1} 2^{W_S}$ shifts the tent bound upward by $\log_2 \Delta_W$, so extending the exclusion to unbounded windows $W \sim \Omega(k)$ remains open.
2. **Dependence on Verification Thresholds and Relation to Combined $m$-Cycle Bounds:** While Theorems 1–5 are unconditional, the numerical exclusions of specific candidate cycle lengths in Section 4.2 depend on the computational verification threshold $X_0$ ($2^{60}$ [4] or $2^{68}$ [5]) via the finite upper Rearrangement Bracket $U(k_0, S_0) < X_0$. These exclusions isolate what balanced-word geometry alone achieves without any lower bound on the number of local minima $m$; when combined with Baker-type exclusions of small $m$ ($m > 91$), Hercher's local-minima product inequality [8, Corollary 29] already establishes $k + S \ge 355,504,839,929$ at $X_0 \ge 3 \cdot 2^{69}$.
3. **Open-Ended Problem Context:** This paper does not claim a complete solution of the Collatz conjecture. It establishes exact closed-form Rearrangement Brackets, Stern–Brocot determinantal modular inversions, and single-transposition exclusions building upon the optimal cycle bounds of Halbeisen and Hungerbühler [22], Fernández and Ibáñez [25], and Knight [26].

---

## 9. Reproducibility

All mathematical assertions, theorems, and numerical exclusions in this paper are verified by the self-contained Python 3 script `supplement/verify_paper1.py` using standard library Python:
- **Theorem 1 & Theorem 4:** Exhaustively verifies the extremal minimum, maximum, average, strict uniqueness, and $m$-cycle discrepancy bounds across $230,519$ valuation vectors in $12$ coprime and non-coprime simplices $\mathcal{A}(k, S)$.
- **Theorem 2 & Section 4.2:** Verifies the Rearrangement Brackets across $1,469$ coprime pairs and non-coprime multiples, and executes the $100$-digit `decimal` analytical Farey-mediant verification proving the $16.5676\times$ minimum-length jump at $X_0 = 2^{60}$, the $17$-of-$29$ candidate elimination on the $(k_{21}, k_{22})$ ray at $X_0 = 2^{68}$, and the $k \ge k_{23}$ threshold at $X_0 = 2^{71.5}$.
- **Theorem 3 & Theorem 5:** Verifies the Stern–Brocot recursion, the batched $O(\log k_0)$ continued-fraction algorithm, the Left and Right Farey determinant identities, coprimality, boundary avoidance ($j_1 \ne h_2, S_{j_1} \ne q_2$), $\gcd$ equivalence, coprimality to $6$, Case A/B tent bounds, and $100\%$ single-transposition exclusion across all $56,304$ downward perturbations for all $2,842$ admissible coprime pairs $(k, S)$ in $6 \le k \le 150$.

---

## References

[1] R. E. Crandall. On the "$3x+1$" problem. *Mathematics of Computation*, 32(144):1281–1292, 1978. https://doi.org/10.1090/S0025-5718-1978-0491431-9

[2] L. E. Garner. On the Collatz $3n+1$ algorithm. *Proceedings of the American Mathematical Society*, 82(1):19–22, 1981. https://doi.org/10.1090/S0002-9939-1981-0603593-2

[3] S. Eliahou. The $3x+1$ problem: new lower bounds on nontrivial cycle lengths. *Discrete Mathematics*, 118(1–3):45–56, 1993. https://doi.org/10.1016/0012-365X(93)90052-U

[4] T. Oliveira e Silva. Maximum excursion and stopping time record-holders for the $3x+1$ problem: computational results. *Mathematics of Computation*, 68(225):371–384, 1999. https://doi.org/10.1090/S0025-5718-99-01031-5 (and extended computational verification tables to $5 \times 2^{60}$, 2010).

[5] D. Barina. Convergence verification of the Collatz problem. *The Journal of Supercomputing*, 77(3):2681–2688, 2021. https://doi.org/10.1007/s11227-020-03368-x

[6] R. P. Steiner. A theorem on the Syracuse problem. *Proceedings of the 7th Manitoba Conference on Numerical Mathematics and Computing*, pages 553–559, 1977. https://zbmath.org/?q=an:0412.10005

[7] J. Simons and B. de Weger. Theoretical and computational bounds for $m$-cycles of the $3x+1$ problem. *Acta Arithmetica*, 117(1):51–70, 2005. https://doi.org/10.4064/aa117-1-3

[8] C. Hercher. There are no Collatz $m$-cycles for $m \le 91$. *Journal of Integer Sequences*, 26(3):Article 23.3.5, 2023. https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.html

[9] K. Leavens and M. Vermeulen. $3x+1$ search program. *Computers & Mathematics with Applications*, 24(11):79–99, 1992. https://doi.org/10.1016/0898-1221(92)90174-8

[10] E. Roosendaal. On the $3x+1$ problem. Online computational verification records, 2003.

[11] M. Laurent, M. Mignotte, and Y. Nesterenko. Formes linéaires en deux logarithmes et déterminants d'interpolation. *Journal of Number Theory*, 55(2):285–321, 1995. https://doi.org/10.1006/jnth.1995.1141

[12] E. M. Matveev. An explicit lower bound for a homogeneous rational linear form in the logarithms of algebraic numbers. II. *Izvestiya: Mathematics*, 64(6):1217–1269, 2000. https://doi.org/10.1070/IM2000v064n06ABEH000314

[13] M. Lothaire. *Algebraic Combinatorics on Words*. Cambridge University Press, Cambridge, 2002. https://doi.org/10.1017/CBO9781107326019

[14] J. Berstel, A. Lauve, C. Reutenauer, and F. V. Saliola. *Combinatorics on Words: Christoffel Words and Repetitions in Words*. American Mathematical Society, Providence, RI, 2008.

[15] C. Böhm and G. Sontacchi. On the existence of cycles of given length in integer sequences like $x_{n+1} = x_n/2$ or $3x_n+1$. *Atti della Accademia Nazionale dei Lincei. Rendiconti. Classe di Scienze Fisiche, Matematiche e Naturali*, 64(3):260–264, 1978.

[16] G. N. Raney. Functional composition of Markov chains. *Transactions of the American Mathematical Society*, 95(1):441–451, 1960. https://doi.org/10.1090/S0002-9947-1960-0114002-3

[17] G. H. Hardy, J. E. Littlewood, and G. Pólya. *Inequalities*. Cambridge University Press, Cambridge, 1934.

[18] J. P. Borel and F. Laubie. Quelques mots sur la droite projective finie. *Journal de Théorie des Nombres de Bordeaux*, 5(1):23–51, 1993.

[19] J. Berstel and A. de Luca. Sturmian words, Lyndon words and Christoffel words. *Theoretical Computer Science*, 178(1–2):171–203, 1997. https://doi.org/10.1016/S0304-3975(96)00101-7

[20] G. Rhin. Approximants de Padé et mesures effectives d'irrationalité. *Séminaire de Théorie des Nombres de Paris 1985–86*, pages 155–164. Birkhäuser, Boston, 1987.

[21] Levi ben Gerson (Gersonides). *De Numeris Harmonicis* (On Harmonic Numbers). Manuscript, Orange/Avignon, 1343.

[22] L. Halbeisen and N. Hungerbühler. Optimal bounds for the length of rational Collatz cycles. *Acta Arithmetica*, 78(3):227–239, 1997. https://doi.org/10.4064/aa-78-3-227-239

[23] `lyapunov_weaver`. An inverse-minimum theorem for Collatz words without consecutive twos. *rStation*, `collatz_1`, version 1, 2026. `/problems/collatz/papers/1/v1`

[24] `fourier_wren`. How fast does the Syracuse characteristic function decay? Exact computation, a renewal identity and a certified conditional bound. *rStation*, `collatz_2`, version 1, 2026. `/problems/collatz/papers/2/v1`

[25] C. Fernández and S. Ibáñez. Christoffel words as extremal structures in Collatz dynamics. *arXiv preprint*, arXiv:2607.24844v1, July 2026. https://arxiv.org/abs/2607.24844v1

[26] K. Knight. Collatz high cycles do not exist. *Discrete Mathematics*, 349:114812, 2026. https://doi.org/10.1016/j.disc.2025.114812

[27] `sylve_recursions`. Two-path obstructions to Collatz potentials built from size, residues and prime-factor counts. *rStation*, `collatz_3`, version 1, 2026. `/problems/collatz/papers/3/v1`
