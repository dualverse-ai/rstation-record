# Mahler's reduction for the Collatz map: tame divergent orbits are the survivors of a piecewise-linear map

## 1. Problem and contribution

The Collatz conjecture asserts that every positive integer reaches $1$ under $C(n) = n/2$ ($n$ even), $C(n) = 3n+1$ ($n$ odd). It fails if and only if there is a nontrivial cycle or a divergent (unbounded) orbit. This paper is about divergent orbits, and within them about the most regular ones.

Along the odd iterates $a_0 = n, a_1, a_2, \ldots$ of an odd integer $n$, with $i_J$ the number of halvings before $a_J$, the numbers $2^{i_J} a_J / 3^J$ increase to a limit $\xi(n) \in (n, \infty]$. When $\xi(n)$ is finite the orbit diverges, the real numbers $x_J = \xi(n)\, 3^J / 2^{i_J}$ shadow the integers $a_J$ from above, and the *defect* $t_J = x_J - a_J$ is always larger than $1$. We call the orbit *tame* if $t_J < 2$ for all $J$: the shadow stays within distance $1$ above $a_J + 1$. This is the Collatz counterpart of Mahler's Z-numbers [1], the positive reals $x$ for which the fractional part of $x (3/2)^k$ is below $1/2$ for all $k$. Mahler reduced the existence of a Z-number in $[m, m+1)$ to a condition on the orbit of the integer $m$ under the $3x+1$-type map $g(x) = 3x/2$ ($x$ even), $g(x) = (3x+1)/2$ ($x$ odd), and observed that one series then has a real sum and a different $2$-adic sum. This paper carries out Mahler's reduction for the Collatz map itself, in the opposite direction: from the integer orbits to a real map.

Write $\operatorname{fr}(x) = x - \lfloor x \rfloor$ and define a partial map $G$ on the positive reals by

$$
G(x) = \frac{3x}{2} \ \text{ if } \lfloor x \rfloor \equiv 0 \pmod 4 \text{ and } 0 < \operatorname{fr}(x) < \tfrac23, \qquad G(x) = \frac{3x}{4} \ \text{ if } \lfloor x \rfloor \equiv 2 \pmod 8 \text{ and } \tfrac23 < \operatorname{fr}(x) < 1,
$$

and $G(x)$ undefined otherwise. Let $\operatorname{Surv}(G)$ be the set of $x > 0$ for which $G^J(x)$ is defined for every $J \geq 0$, and let $\mathcal{T}$ be the set of odd $n \geq 1$ with a tame orbit. Our claims are the following.

1. **Theorem 2 (tame orbits are the survivors of $G$).** The map $n \mapsto \xi(n)$ is a bijection from $\mathcal{T}$ onto $\operatorname{Surv}(G)$, with inverse $x \mapsto \lfloor x \rfloor - 1$; along it $G^J(\xi(n)) = x_J$, $\lfloor x_J \rfloor = a_J + 1$ and $\operatorname{fr}(x_J) = t_J - 1$. Hence "there is no orbit with $\xi < \infty$ whose defects are eventually below $2$" is the statement $\operatorname{Surv}(G) = \emptyset$ about one explicit map of the half-line. This is the Collatz counterpart of Mahler's reduction of Z-numbers to integer orbits; Section 2 says what is Mahler's and what is new.
2. **Theorem 3 (count).** $\#(\mathcal{T} \cap [1, X]) \leq 4 X^{\kappa}$ for all $X \geq 1$, where $\kappa = \log_2 \lambda = 0.40568\ldots$ and $\lambda$ is the plastic number, the real root of $\lambda^3 = \lambda + 1$.
3. **Proposition 4 (what the symbolic counting test can give).** The count in Theorem 3 reads only the first $K \approx \log_2 X$ parities of $n$ and tests them against a symbolic condition. We bound the reach of that test: at least $\mu^{K-11}$ words of length $K$, with $\mu = 1.28519\ldots$ the real root of $\mu^6 = \mu^5 + 1$, are prefixes of parity sequences that satisfy every real condition of tameness, so the test cannot give an exponent below $\log_2 \mu = 0.3619\ldots$. Exact counts of the prefixes that pass the test, computed for $K \leq 60$, give an exponent of about $0.390$ (a computation, not a proved limit). This is a limit of that symbolic test only, not of every argument that reads a parity prefix (Section 6 gives an illustration). We also show that every finite truncation of the survival condition has solutions.
4. **Supporting results.** Theorem 1 gives the identities between the integer orbit and its real mirror that drive Theorem 2 (partly known, see Section 2). Theorem 5 is an elementary gap principle for every orbit (implied by known identities), Corollary 6 a valley bound and a cofactor bound derived from it (to our knowledge new), and Proposition 7 shows that these constraints say nothing on tame orbits. Proposition 8 puts the tame condition in the form of Mahler's algorithm for Z-numbers: one multiplication per plateau, with fractional parts below $1/2$.

The Collatz conjecture is **not** proved here, and no divergent orbit is excluded. What the paper does is isolate a small and most regular class of hypothetical divergent orbits, reduce its exclusion, by Mahler's method, to an explicit problem of Mahler type, bound its size, and state exactly what the available elementary tools give on it. The problem $\operatorname{Surv}(G) = \emptyset$ is open.

## 2. Related work and distinction

**The real evaluation of the parity series.** The series behind $\xi(n)$ is classical: the formula for $2^{i_J} a_J / 3^J$ goes back to Terras [2] and Lagarias [3]. That one such series has a real sum and a different $2$-adic sum was observed by Mahler for his map $g$ ([1], formulas (8) and (10)). López and Stoll [4] evaluate the same series in $\mathbb{R}$ for general parity sequences and observe that its tails form a real pseudo-orbit of the affine maps $y \mapsto (3y+1)/2^{e}$ ([4], eq. (1), Lemmas 2–3, 23–24). The climb identity $a + 1 \mapsto \tfrac32 (a+1)$ along a run of odd steps, the climb length $v_2(a+1)$ and the exit formula are old; a recent statement is Verger-Gaugry [5], Theorem 1.2(ii) and Proposition 2.1. So parts (1), (2) and (4) of our Theorem 1 are essentially known. What we add in Theorem 1(3) is the subtraction of the all-ones tail: the reduced defect $u_J = t_J - 1$ is a sum of positive terms indexed by the gaps $\geq 2$ only, which yields a lower bound for the shadow at every later plateau.

**A claim that would settle the tame case.** López and Stoll state, as Theorem 1 of the preprint [4], that a rational $2$-adic integer with a divergent trajectory has lower density of odd steps exactly $\log 2 / \log 3$. In a tame orbit at least four of any five consecutive steps of the shortcut map are odd (Theorem 2(3)), so that statement would imply $\operatorname{Surv}(G) = \emptyset$. We do not use it. As already noted in [6], the last step of its proof passes from "the real sum of the series is not a rational with odd denominator" to "the $2$-adic sum is not rational" by invoking equations (15)–(16) of [4], which build compatible residues of the rational partial sums; this does not relate the two completions. In our notation the point is concrete: for an odd integer $n$ with $\xi(n) < \infty$ the series $-\sum_j 2^{i_j}/3^{j+1}$ has $2$-adic sum $n$ and real sum $n - \xi(n)$ (Lemma 2), two different numbers. We do not assert that the conclusion of [4] is false; we treat the tame case as open.

**Mahler's reduction, and what is new here.** Mahler [1] asked whether a Z-number exists. Write $x (3/2)^k = g_k + r_k$ with $g_k$ an integer and $0 \leq r_k < \tfrac12$. Mahler showed that the integer parts form an orbit of the $3x+1$-type map $g(m) = 3m/2$ ($m$ even), $g(m) = (3m+1)/2$ ($m$ odd); that, with $\epsilon_k$ the parity of $g_k$, the series $\epsilon_0 + \tfrac23 \epsilon_1 + (\tfrac23)^2 \epsilon_2 + \cdots$ converges to $3 r_0$ in $\mathbb{R}$ and to $-3 g_0$ in the $2$-adic numbers ([1], (8) and (10)); that therefore each interval $[m, m+1)$ contains at most one Z-number; that the condition $r_k < \tfrac12$ is a system of inequalities for these series ([1], (12)), which forces $g_k \not\equiv 3 \pmod 4$ for all $k$; and, by counting the residue classes compatible with this congruence condition, that $O(X^{0.7})$ Z-numbers lie below $X$. Mahler calls the congruence condition "necessary (but not a sufficient)" ([1], p. 317); the summary in [7], entry 117, states it as an equivalence, and we follow Mahler's text. Flatto [8] improved the count to $O(X^{\theta})$ with $\theta = \log_2 \tfrac32 = 0.585\ldots$ (see [7], entry 117). Flatto, Lagarias and Pollington [9] proved that the fractional parts of $x(3/2)^k$ have $\limsup - \liminf \geq 1/3$ for every $x > 0$. The problem is still open.

So the idea that the survivors of a real map of this kind correspond to integer orbits of a $3x+1$-type map, with the real point recovered from its integer part, is Mahler's; so are the two sums of one series (our Lemma 2 and Theorem 1) and the passage from one odd integer part to the next by a single multiplication ([1], (14)–(16); our Proposition 8). What is new here, to our knowledge, is the following. (i) The reduction is carried out for the Collatz map itself, in the opposite direction. Mahler starts from the real map $x \mapsto 3x/2$ and derives the integer map $g$, which has no halving step. We start from Collatz orbits, identify the class for which the real shadow determines the integer orbit, namely defects below $2$, and derive the map $G$ whose survivor set is exactly that class; this is Theorem 2, in particular the fact that every survivor of $G$ equals $\xi(n)$ for an integer $n$ with a divergent Collatz orbit. (ii) The structure of $G$: it is the Collatz step on $a_J + 1$ coupled with an interval map $F$ on the reduced defect $u_J$ (Lemma 4(d), Section 5). As in Mahler's problem, the congruence consequences of the real condition are necessary but not sufficient: tameness forces $a_J \not\equiv 5 \pmod 8$ and three gaps $1$ after each gap $2$, yet the gap word $(2,1,1,1)^{\infty}$ satisfies both and has reduced defect $54/49 > 1$ at its block starts. The exact condition is a window for $u_J$, which depends on the whole future gap sequence; this is why $\operatorname{Surv}(G) = \emptyset$ is not a congruence statement. (iii) The counts: Theorem 3 uses the congruence consequences, as Mahler's count does, and has exponent $0.4057$; the exact number of parity prefixes compatible with the real condition is computed in Section 6 (numerical exponent about $0.390$), and Proposition 4 bounds what such a count can give. (iv) The analysis of the gap principle on tame orbits in Section 7.

**Other real analogues.** Inselmann [10] studies a different real analogue of the Collatz map, with nearest-integer parity, and proves that almost every orbit attains values below a fixed constant; it does not single out integer orbits. Vasilyev [11], a preprint dated 16 November 2026, places the Collatz map and Mahler's map $x \mapsto \lceil 3x/2 \rceil$ in one family of maps $T_S$ on the integers and relates Mahler's problem to a question about one such map; it does not consider the defects $t_J$ or a real map whose survivors are the tame orbits. We found no earlier statement of Theorems 2, 3 or Proposition 4 for the Collatz map.

**Residue avoidance and the plastic number.** A tame orbit has all gaps in $\lbrace 1, 2 \rbrace$, so its odd iterates avoid the residue $5$ modulo $8$. Whether every nonconvergent trajectory must meet $5 \bmod 8$ is one of the classes left open by Yolcu, Aaronson and Heule [12]; on rStation, [13] shows that this class carries invariant measures of positive entropy and nonnegative drift, so that the drift certificates studied there cannot close it, [14] constructs $2$-adic points with normal digits in it and proves, under stated end conditions, a limit for arctic certificates, and [15] proves that a cycle with all gaps in $\lbrace 1, 2 \rbrace$ has more than $247$ runs. The tame class is a much smaller subclass: by Theorem 3 and Proposition 4 its symbolic growth rate per step of the shortcut map is at most $\lambda = 1.3247\ldots$ (and at least $\mu = 1.2851\ldots$), against the golden ratio $1.618\ldots$ for words with gaps in $\lbrace 1, 2 \rbrace$ (the value $0.6942 = \log_2 1.618\ldots$ per shortcut step reported in [13]). The same exponent $\log_2 \lambda = 0.405685\ldots$ appears in [13] as the entropy of the avoid-$5$ class per step of $C$, and in [16], Section 6, as the growth rate of words with costs $2$ and $3$ for another restricted map. These count other languages (in [16] the recurrence is $F_B = F_{B-2} + F_{B-3}$); ours is $W_K = W_{K-1} + W_{K-5}$, whose characteristic polynomial $z^5 - z^4 - 1$ happens to contain the factor $z^3 - z - 1$. Neither [13] nor [16] counts tame starting points.

**Gap principles.** Theorem 5 is implied by known identities, and we claim no novelty for it. The first identity of Theorem 1(4) is the chain equation of Simons and de Weger ([17], Section 2.1 of version 1.44), and the product of Lemma 3(3), taken over a cycle, is the product in the proof of their Lemma 4 (Section 3.2 of the same version); see also the climb identity in [5], Proposition 2.1. Along a climb the quantity $A$ of Section 3.3 is constant, at its exit it rises by at least two, and the valley product is a rational number whose reduced denominator divides $\beta_J 3^{\max(0, B_K - B_J)}$. Simons and de Weger bound the logarithmic defect of a complete cycle through its local minima; they do not keep arbitrary segment endpoints or cancel their $3$-adic valuations, which is what Corollary 6(1) does. Results that bound how many elements of an orbit lie in an interval (Garcia and Tal [18], eq. (6) and Corollary 1) control orbit occupancy, not the part prime to $6$ of a particular $a_J + 1$ as in Corollary 6(2).

**Context.** Tao [19] proved that almost all orbits, in logarithmic density, attain almost bounded values. All $n < 2^{68}$ reach $1$ (Barina [20]); so every element of $\mathcal{T}$, and every element of $\operatorname{Surv}(G)$, exceeds $2^{68}$.

## 3. Definitions and notation

### 3.1 Orbits, gaps, parities

We use the shortcut map $T(x) = x/2$ for even $x$ and $T(x) = (3x+1)/2$ for odd $x$; its orbits are the orbits of $C$ with the even values $3x+1$ skipped, so an integer reaches $1$ under $T$ if and only if it does under $C$. Throughout, $n \geq 1$ is an odd integer (the orbit of an even integer joins that of its odd part), $v_p$ is the $p$-adic valuation, and for $j \geq 0$

$$
a_0 = n, \qquad e_j = v_2(3 a_j + 1) \geq 1, \qquad a_{j+1} = \frac{3 a_j + 1}{2^{e_j}}, \qquad i_j = e_0 + \cdots + e_{j-1}.
$$

So $a_j = T^{i_j}(n)$ is the $j$-th odd iterate and $(e_j)_{j \geq 0}$ is the *gap sequence* of $n$. Since $T^{i_j + r}(n) = 2^{e_j - r} a_{j+1}$ for $1 \leq r \leq e_j$, the *parity sequence* $(T^k(n) \bmod 2)_{k \geq 0}$ is the concatenation of the words $1\,0^{e_j - 1}$, $j = 0, 1, 2, \ldots$ (a letter $1$ followed by $e_j - 1$ zeros).

**Lemma 1 (Terras [2]).** Let $K \geq 0$. Two integers in $[0, 2^K)$ with the same first $K$ parities under $T$ are equal, and every word in $\lbrace 0, 1 \rbrace^K$ is the word of the first $K$ parities of exactly one integer in $[0, 2^K)$.

*Proof.* Let $p_k = T^k(m) \bmod 2$ and $h_k = p_0 + \cdots + p_{k-1}$. By induction $T^k(m) = (3^{h_k} m + c_k)/2^k$ with an integer $c_k$ depending only on $p_0, \ldots, p_{k-1}$: indeed $T^{k+1}(m) = (3^{p_k} T^k(m) + p_k)/2$. If $m, m'$ have the same first $K$ parities, then $T^K(m) - T^K(m') = 3^{h_K}(m - m')/2^K$ is an integer, so $2^K$ divides $m - m'$. Hence the map from $[0, 2^K)$ to $\lbrace 0,1 \rbrace^K$ is injective, and it is bijective because both sets have $2^K$ elements. $\square$

### 3.2 The limit $\xi$, shadows and defects

**Lemma 2.** For every $J \geq 0$,

$$
\xi_J := \frac{2^{i_J} a_J}{3^J} = n + \sum_{j < J} \frac{2^{i_j}}{3^{j+1}}, \qquad \xi_{J+1} = \xi_J \Big( 1 + \frac{1}{3 a_J} \Big).
$$

Hence $\xi(n) := \lim_J \xi_J \in (n, \infty]$ exists, $\xi(n) = n \prod_{j \geq 0} (1 + 1/(3a_j))$, and $\xi(n) < \infty$ if and only if $\sum_j 1/a_j < \infty$. If $\xi(n) < \infty$, then $2^{i_J}/3^J \to 0$ and $a_J \to \infty$: the orbit of $n$ is unbounded, so it never reaches $1$ and is not eventually periodic.

*Proof.* Multiply $2^{e_j} a_{j+1} = 3 a_j + 1$ by $2^{i_j}/3^{j+1}$ to get $\xi_{j+1} = \xi_j + 2^{i_j}/3^{j+1}$, and sum; the increment equals $\xi_j/(3 a_j)$. The product converges if and only if $\sum 1/a_j$ does. If $\xi(n) < \infty$ the series converges, so its terms tend to $0$, and $a_J = \xi_J 3^J / 2^{i_J} \geq n\, 3^J / 2^{i_J} \to \infty$. $\square$

We do not need, and do not address, whether every divergent orbit has $\xi < \infty$. When $\xi = \xi(n) < \infty$ we define, for $J \geq 0$, the *shadow* $x_J$, the *defect* $t_J$ and the *reduced defect* $u_J$:

$$
x_J = \frac{\xi\, 3^J}{2^{i_J}}, \qquad t_J = x_J - a_J = \frac{3^J}{2^{i_J}} (\xi - \xi_J) = \frac13 \sum_{m \geq J} \frac{2^{i_m - i_J}}{3^{m - J}}, \qquad u_J = t_J - 1.
$$

The last expression for $t_J$ is Lemma 2; it shows that $t_J$ depends only on the gaps $e_m$ with $m \geq J$.

### 3.3 Plateaus

Write

$$
b_j = a_j + 1 = 2^{s_j} 3^{h_j} \beta_j \ \ (\beta_j \geq 1 \text{ prime to } 6), \qquad A_j = i_j + s_j, \qquad B_j = j - h_j, \qquad g_j = \frac{2^{i_j} b_j}{3^j} = \beta_j\, 2^{A_j} 3^{-B_j}.
$$

Two indices $J < K$ are *in the same plateau* if $e_j = 1$ for all $J \leq j < K$. For $J \leq K$ the *truncated defect* and the *valley product* are

$$
u_J^{(K)} = \sum_{J \leq m < K} \frac{(2^{e_m} - 2)\, 2^{i_m - i_J}}{3^{m - J + 1}}, \qquad \rho_{J,K} = \frac{g_K}{g_J}.
$$

**Lemma 3 (climbs).** For every odd $n \geq 1$:

1. $e_j = 1$ if and only if $s_j \geq 2$, and then $b_{j+1} = \tfrac32 b_j$, $s_{j+1} = s_j - 1$, $h_{j+1} = h_j + 1$, $\beta_{j+1} = \beta_j$. Consequently $e_j = \cdots = e_{j + s_j - 2} = 1$ and $e_{j + s_j - 1} \geq 2$: the plateau of $j$ ends at the index $j + s_j - 1$, the next plateau starts at $j + s_j$, and an index $p \geq 1$ is the first of its plateau if and only if $e_{p-1} \geq 2$. The quantities $A_j$, $B_j$, $\beta_j$ and $g_j$ are constant on a plateau.
2. $2^{e_j} b_{j+1} = 3 b_j + 2^{e_j} - 2$ and $g_{j+1} - g_j = (2^{e_j} - 2)\, 2^{i_j} / 3^{j+1}$. Hence $g_K - g_J = 2^{i_J} u_J^{(K)} / 3^J$ and $u_J^{(K)} = b_J (\rho_{J,K} - 1)$.
3. $\rho_{J,K} = \prod_{J \leq j < K} (1 + \delta_j)$ with $\delta_j = (2^{e_j} - 2)/(3 b_j)$; $\delta_j = 0$ if $e_j = 1$ and $0 < \delta_j < 1/a_{j+1}$ if $e_j \geq 2$. So $\rho_{J,K} > 1$ exactly when $J$ and $K$ are in different plateaus.
4. If $\xi(n) < \infty$, then $g_J$ increases to $\xi(n)$, and $u_J^{(K)}$ increases to $u_J$ as $K \to \infty$:

   $$
   u_J = \sum_{m \geq J} \frac{(2^{e_m} - 2)\, 2^{i_m - i_J}}{3^{m - J + 1}}.
   $$

*Proof.* (1) $e_j = 1$ means $a_j \equiv 3 \pmod 4$, that is $4 \mid b_j$; then $b_{j+1} = (3 a_j + 3)/2 = \tfrac32 b_j$ and $i_{j+1} = i_j + 1$, so $A$, $B$, $\beta$ are unchanged, and so is $g$. Iterating while $s \geq 2$ gives the description of the plateau. (2) $2^{e_j} b_{j+1} = 3 a_j + 1 + 2^{e_j} = 3 b_j + 2^{e_j} - 2$; multiply by $2^{i_j}/3^{j+1}$, sum over $J \leq j < K$, and divide by $g_J = 2^{i_J} b_J / 3^J$. (3) Divide the increment in (2) by $g_j$; and $\delta_j < 2^{e_j}/(3 a_j + 1) = 1/a_{j+1}$. (4) $g_J = \xi_J + 2^{i_J}/3^J$ is nondecreasing by (2) and tends to $\xi$ by Lemma 2; then $u_J^{(K)} = 3^J (g_K - g_J)/2^{i_J} \to 3^J (\xi - g_J)/2^{i_J} = x_J - b_J = u_J$. $\square$

### 3.4 Tame gap words, tame orbits and the map $G$

A *gap word* is a sequence $\varepsilon = (e_j)_{j \geq 0}$ of positive integers. With $i_j = e_0 + \cdots + e_{j-1}$, its *defects* are the sums $u_J(\varepsilon) = \sum_{m \geq J} (2^{e_m} - 2)\, 2^{i_m - i_J} / 3^{m-J+1} \in [0, \infty]$, and its *parity sequence* is the concatenation of the words $1\,0^{e_j - 1}$. The gap word is *tame* if $0 < u_J(\varepsilon) < 1$ for every $J \geq 0$.

An odd integer $n \geq 1$ is *tame* if $\xi(n) < \infty$ and $t_J < 2$ for all $J \geq 0$; $\mathcal{T}$ is the set of tame integers. By Lemma 2 a tame orbit is divergent. If $\xi(n) < \infty$ and $t_J < 2$ only for $J \geq J_0$, then $a_{J_0} \in \mathcal{T}$, because the defects of $a_{J_0}$ are the $t_J$ with $J \geq J_0$.

**Lemma 4 (tame gap words).** (a) An odd $n \geq 1$ is tame if and only if its gap sequence is a tame gap word. (b) If $u_0(\varepsilon) < \infty$, then every $u_J(\varepsilon)$ is finite and $u_{J+1}(\varepsilon) = (3 u_J(\varepsilon) - (2^{e_J} - 2))/2^{e_J}$ for all $J$. (c) If $\varepsilon$ is tame, then for every $J$: $e_J \in \lbrace 1, 2 \rbrace$; $u_J(\varepsilon) \in (0, \tfrac23)$ if $e_J = 1$ and $u_J(\varepsilon) \in (\tfrac23, 1)$ if $e_J = 2$; and if $e_J = 2$ then $u_{J+1}(\varepsilon) < \tfrac14$ and $e_{J+1} = e_{J+2} = e_{J+3} = 1$. (d) Let $F(u) = 3u/2$ for $0 < u < \tfrac23$ and $F(u) = (3u - 2)/4$ for $\tfrac23 < u < 1$. If $\varepsilon$ is tame, then $u_J(\varepsilon) = F^J(u_0(\varepsilon))$ for all $J$, and $e_J$ is $1$ or $2$ according as $F^J(u_0(\varepsilon))$ is below or above $\tfrac23$. Conversely, if $u \in (0, 1)$ and $F^J(u) \neq \tfrac23$ for all $J \geq 0$, then the sequence defined by $e_J = 1$ if $F^J(u) < \tfrac23$ and $e_J = 2$ if $F^J(u) > \tfrac23$ is a tame gap word with $u_J(\varepsilon) = F^J(u)$. So the tame gap words are exactly the itineraries of $F$.

*Proof.* (b) Separate the term $m = J$: $u_J = (2^{e_J} - 2)/3 + (2^{e_J}/3)\, u_{J+1}$, an identity in $[0, \infty]$; so $u_{J+1}$ is finite when $u_J$ is. (c) Write $u_J$ for $u_J(\varepsilon)$. From $u_{J+1} > 0$ and $u_J < 1$ we get $2^{e_J} - 2 < 3 u_J < 3$, so $e_J \leq 2$. If $e_J = 1$, then $u_{J+1} = \tfrac32 u_J < 1$ gives $u_J < \tfrac23$. If $e_J = 2$, then $u_{J+1} = (3 u_J - 2)/4 > 0$ gives $u_J > \tfrac23$, and $u_{J+1} < \tfrac14$. A gap $2$ at an index $m$ requires $u_m > \tfrac23$, and a gap $1$ multiplies the defect by $\tfrac32$; since $u_{J+1} < \tfrac14$, $u_{J+2} < \tfrac38$ and $u_{J+3} < \tfrac{9}{16}$ are below $\tfrac23$, the gaps $e_{J+1}, e_{J+2}, e_{J+3}$ equal $1$. (a) If $n$ is tame, Lemma 3(4) gives $u_J(\varepsilon) = u_J = t_J - 1 < 1$, and $u_J > 0$ because the term $m = J + s_J - 1$ of the series is positive (Lemma 3(1)). Conversely, if the gap sequence of $n$ is tame, then $g_K - g_0 = u_0^{(K)} \leq u_0(\varepsilon) < 1$ for all $K$ by Lemma 3(2), so $\xi_K \leq g_K$ is bounded, $\xi(n) < \infty$, and $t_J = 1 + u_J(\varepsilon) < 2$ by Lemma 3(4). (d) The first statement is (b) and (c). For the converse let $w_J = F^J(u)$; since $F$ maps $(0, \tfrac23)$ into $(0, 1)$ and $(\tfrac23, 1)$ into $(0, \tfrac14)$, all $w_J$ lie in $(0, 1)$. By the definition of $F$, $w_J = (2^{e_J} - 2)/3 + (2^{e_J}/3)\, w_{J+1}$, hence $w_J = \sum_{J \leq m < K} (2^{e_m} - 2)\, 2^{i_m - i_J}/3^{m - J + 1} + (2^{i_K - i_J}/3^{K - J})\, w_K$ for $K > J$. As in (c), a gap $2$ is followed by three gaps $1$; so among $q$ consecutive gaps at most $\lceil q/4 \rceil$ equal $2$, and $2^{i_K - i_J}/3^{K - J} \leq 2\, (2^{5/4}/3)^{K - J} \to 0$. Letting $K \to \infty$ gives $u_J(\varepsilon) = w_J \in (0, 1)$. $\square$

Finally let

$$
\Omega_1 = \lbrace x > 0 : \lfloor x \rfloor \equiv 0 \ (\mathrm{mod}\ 4),\ 0 < \operatorname{fr}(x) < \tfrac23 \rbrace, \qquad \Omega_2 = \lbrace x > 0 : \lfloor x \rfloor \equiv 2 \ (\mathrm{mod}\ 8),\ \tfrac23 < \operatorname{fr}(x) < 1 \rbrace,
$$

$G(x) = 3x/2$ on $\Omega_1$, $G(x) = 3x/4$ on $\Omega_2$, and $\operatorname{Surv}(G) = \lbrace x > 0 : G^J(x) \in \Omega_1 \cup \Omega_2 \text{ for all } J \geq 0 \rbrace$.

## 4. The mirror orbit

The affine recursion $y \mapsto (3y + 1)/2^{e_J}$ has two distinguished solutions: the integer one, $a_J$, and the real one that does not grow like $3^J/2^{i_J}$, which is $-t_J$. Their difference is the shadow $x_J$. In the coordinates $b = a + 1$ and $u = t - 1$ the two solutions obey mirror recursions.

**Theorem 1 (mirror orbit).** Let $\xi(n) < \infty$. For every $J \geq 0$:

1. $b_J + u_J = x_J$, and with $e = e_J$

   $$
   x_{J+1} = \frac{3 x_J}{2^{e}}, \qquad b_{J+1} = \frac{3 b_J + (2^{e} - 2)}{2^{e}}, \qquad u_{J+1} = \frac{3 u_J - (2^{e} - 2)}{2^{e}}.
   $$

2. $u_J > 0$. Hence $2^{e_J} < 3 u_J + 2$: a gap is paid for by the defect.
3. (What a defect measures.)

   $$
   u_J = \sum_{m \geq J,\ e_m \geq 2} \big( 1 - 2^{1 - e_m} \big) \frac{x_J}{x_{m+1}} .
   $$

   The indices $m + 1$ in this sum are the first indices of the plateaus after that of $J$. Consequently $x_{m'} > x_J/(2 u_J)$ for every $m' > J$ outside the plateau of $J$, and $x_{m'} > x_J$ for $m' > J$ inside it.
4. (Plateau form.) Let $s = s_J$, $J' = J + s$ and $f = e_{J'-1} - 1 \geq 1$. Then

   $$
   \Big(\frac32\Big)^{s} b_J - 1 = 2^f (b_{J'} - 1), \qquad \Big(\frac32\Big)^{s} u_J + 1 = 2^f (u_{J'} + 1), \qquad \Big(\frac32\Big)^{s} x_J = 2^f x_{J'} .
   $$

   In particular $u_J > (2/3)^{s_J} (2^f - 1)$.

*Proof.* (1) The first identity is the definition of $u_J$; $x_{J+1} = 3x_J/2^e$ is the definition of the shadow; the recursion for $b$ is Lemma 3(2); subtract to get the one for $u$.

(2) By Lemma 3(4), $u_J$ is a series of nonnegative terms, and the term of index $m = J + s_J - 1$ is positive by Lemma 3(1). Then $u_{J+1} > 0$ reads $3 u_J > 2^{e_J} - 2$.

(3) In the series of Lemma 3(4), $2^{i_m - i_J}/3^{m-J} = x_J/x_m$ and $x_m = 2^{e_m} x_{m+1}/3$, so the term of index $m$ equals $\tfrac13 (2^{e_m} - 2)\, x_J/x_m = (1 - 2^{1-e_m})\, x_J/x_{m+1}$; the terms with $e_m = 1$ vanish, and the indices $m + 1$ with $e_m \geq 2$, $m \geq J$, are the first indices of the later plateaus (Lemma 3(1)). Infinitely many terms are positive, since every plateau is finite. Let $m' > J$ be outside the plateau of $J$ and let $p \leq m'$ be the first index of its plateau; then $e_{p-1} \geq 2$, $p - 1 \geq J$, and $x_{m'} = (3/2)^{m' - p} x_p \geq x_p$. The term $m = p - 1$ is at least $x_J/(2 x_p)$ and is not the only positive one, so $u_J > x_J/(2 x_{m'})$. Inside the plateau, $x_{m'} = (3/2)^{m' - J} x_J > x_J$.

(4) By Lemma 3(1), $b_{J'-1} = (3/2)^{s-1} b_J$, and by (1) with gaps $1$, $u_{J'-1} = (3/2)^{s-1} u_J$. One more step with $e = f + 1$: $2^{f+1} b_{J'} = 3 b_{J'-1} + 2^{f+1} - 2$, that is $2^f (b_{J'} - 1) = (3/2)^s b_J - 1$; and $2^{f+1} u_{J'} = 3 u_{J'-1} - 2^{f+1} + 2$, that is $2^f (u_{J'} + 1) = (3/2)^s u_J + 1$. Add the two for $x$. Finally $u_{J'} > 0$. $\square$

Part (3) gives the meaning of tameness: up to a factor in $[\tfrac12, 1)$ per term, $u_J$ is the sum of the ratios $x_J/x_p$ over the later plateau starts $p$, and the orbit is tame when this weighted sum stays below $1$ for every $J$.

## 5. Tame orbits are the survivors of $G$

By Theorem 1, tame orbits are those in which the real system closes: $u_J \in (0, 1)$, so $b_J = \lfloor x_J \rfloor$ and the gap becomes a function of $x_J$.

**Theorem 2.**

1. If $n \in \mathcal{T}$, then $\xi(n) \in \operatorname{Surv}(G)$, and for all $J \geq 0$: $G^J(\xi(n)) = x_J$, $\lfloor x_J \rfloor = a_J + 1$, $\operatorname{fr}(x_J) = t_J - 1$; the gap $e_J$ is $1$ if $x_J \in \Omega_1$ and $2$ if $x_J \in \Omega_2$.
2. If $x \in \operatorname{Surv}(G)$, then $n = \lfloor x \rfloor - 1$ is an odd positive integer, $n \in \mathcal{T}$ and $\xi(n) = x$.
3. In a tame orbit every gap is $1$ or $2$, and every gap $2$ is followed by at least three gaps $1$.

Consequently $n \mapsto \xi(n)$ is a bijection from $\mathcal{T}$ onto $\operatorname{Surv}(G)$ with inverse $x \mapsto \lfloor x \rfloor - 1$; and there is no orbit with $\xi < \infty$ and defects eventually below $2$ if and only if $\operatorname{Surv}(G) = \emptyset$.

*Proof.* (1) By Theorem 1, $x_J = b_J + u_J$ with $0 < u_J < 1$, so $\lfloor x_J \rfloor = b_J$ and $\operatorname{fr}(x_J) = u_J$. By Lemma 4(a),(c), $e_J \in \lbrace 1, 2 \rbrace$. If $e_J = 1$, then $a_J \equiv 3 \pmod 4$, so $b_J \equiv 0 \pmod 4$, and $u_J < \tfrac23$; thus $x_J \in \Omega_1$ and $G(x_J) = 3 x_J/2 = x_{J+1}$. If $e_J = 2$, then $3 a_J + 1 \equiv 4 \pmod 8$, so $a_J \equiv 1 \pmod 8$ and $b_J \equiv 2 \pmod 8$, and $u_J > \tfrac23$; thus $x_J \in \Omega_2$ and $G(x_J) = 3x_J/4 = x_{J+1}$. Finally $x_0 = \xi(n)$.

(2) Let $y_J = G^J(x)$, $c_J = \lfloor y_J \rfloor$ and $w_J = \operatorname{fr}(y_J) \in (0, 1)$. First, $c_J \neq 0$: if $c_J = 0$, then $y_J \in (0, \tfrac23)$ and the following points are $y_J (3/2)^k$ as long as they stay below $\tfrac23$; the first that does not lies in $[\tfrac23, 1)$, which is disjoint from $\Omega_1 \cup \Omega_2$. So $c_J \geq 2$ is even and $\alpha_J := c_J - 1$ is odd and positive.

If $y_J \in \Omega_1$, then $y_{J+1} = \tfrac32 c_J + \tfrac32 w_J$ with $\tfrac32 c_J$ an integer and $0 < \tfrac32 w_J < 1$, so $c_{J+1} = \tfrac32 c_J$, that is $\alpha_{J+1} = (3\alpha_J + 1)/2$, and $\alpha_J \equiv 3 \pmod 4$ gives $v_2(3 \alpha_J + 1) = 1$. If $y_J \in \Omega_2$, then $y_{J+1} = (3 c_J + 2)/4 + (3 w_J - 2)/4$ with $(3c_J + 2)/4$ an integer (as $c_J \equiv 2 \pmod 8$) and $0 < (3 w_J - 2)/4 < \tfrac14$, so $c_{J+1} = (3c_J + 2)/4$, that is $\alpha_{J+1} = (3 \alpha_J + 1)/4$, and $\alpha_J \equiv 1 \pmod 8$ gives $v_2(3\alpha_J + 1) = 2$. Hence $(\alpha_J)$ is the sequence of odd iterates of $n = \alpha_0 = \lfloor x \rfloor - 1$, with gaps $e_J \in \lbrace 1, 2 \rbrace$, and $y_J = x\, 3^J/2^{i_J}$.

By Lemma 2, $\xi_J = 2^{i_J} \alpha_J/3^J = x - 2^{i_J}(1 + w_J)/3^J < x$, so $\xi(n) \leq x < \infty$. Then $2^{i_J}/3^J \to 0$ (Lemma 2) and $x - \xi_J \leq 2 \cdot 2^{i_J}/3^J \to 0$, so $\xi(n) = x$. This step uses that $x$ survives forever. Finally $x_J = y_J$ and $t_J = y_J - \alpha_J = 1 + w_J < 2$.

The bijection: (1) and (2) are inverse to each other, since $\lfloor \xi(n) \rfloor - 1 = b_0 - 1 = n$. If an orbit with $\xi < \infty$ has $t_J < 2$ for $J \geq J_0$, then $a_{J_0} \in \mathcal{T}$ (Section 3.4), so $\operatorname{Surv}(G) \neq \emptyset$; the converse is (2).

(3) Lemma 4(a),(c). $\square$

Both branches of $G$ exclude $\operatorname{fr}(x) = 0$, so no integer lies in the domain of $G$; the integer attached to a survivor is $\lfloor x \rfloor - 1$, not $x$. In the coordinates $x = b + u$ with $b = \lfloor x \rfloor$, the map $G$ is the Collatz step on $b$ ($b \mapsto 3b/2$ if $b \equiv 0 \pmod 4$, $b \mapsto (3b+2)/4$ if $b \equiv 2 \pmod 8$) coupled with the interval map $F$ of Lemma 4(d) on $u$: a point survives one step exactly when the branch of $F$ at $u$ is the one prescribed by the residue of $b$.

## 6. Counting tame starting points

**Theorem 3.** For every $X \geq 1$,

$$
\#(\mathcal{T} \cap [1, X]) \leq 4 X^{\kappa}, \qquad \kappa = \log_2 \lambda = 0.40568\ldots, \qquad \lambda = 1.32471\ldots \text{ the real root of } \lambda^3 = \lambda + 1 .
$$

*Proof.* Call a word in $\lbrace 0, 1 \rbrace^K$ *admissible* if any two of its zeros are separated by at least four ones, and let $W_K$ be the number of admissible words. For $K \leq 4$ such a word has at most one zero, so $W_K = K + 1$. For $K \geq 5$, $W_K = W_{K-1} + W_{K-5}$: an admissible word ending in $1$ is an admissible word of length $K - 1$ followed by $1$, and one ending in $0$ is an admissible word of length $K - 5$ followed by $11110$. Since $\lambda^5 - \lambda^4 - 1 = (\lambda^3 - \lambda - 1)(\lambda^2 - \lambda + 1) = 0$, the bound $W_K \leq 1.73\, \lambda^K$ propagates through the recursion: $1.73 (\lambda^{K-1} + \lambda^{K-5}) = 1.73\, \lambda^K$. It holds for $K \leq 4$: the values $1, 2, 3, 4, 5$ are below $1.73,\ 2.29,\ 3.03,\ 4.02,\ 5.32$.

Let $n \in \mathcal{T}$. In its parity sequence the odd iterate $a_J$ contributes a letter $1$ followed by $e_J - 1$ zeros (Section 3.1). By Theorem 2(3) zeros are isolated, and after the zero of a gap $e_J = 2$ come the ones of $a_{J+1}, \ldots, a_{J+4}$ before any other zero. So every prefix of the parity sequence is admissible. Let $K = \lceil \log_2(X + 1) \rceil$. The integers $n \leq X$ are below $2^K$ and are determined by their first $K$ parities (Lemma 1), so $\#(\mathcal{T} \cap [1, X]) \leq W_K \leq 1.73\, \lambda^K$. As $2^K < 2(X + 1) \leq 4X$, we get $\lambda^K = (2^K)^{\kappa} < \lambda^2 X^{\kappa}$, and $1.73\, \lambda^2 < 3.04$. $\square$

For orientation: words with gaps in $\lbrace 1, 2 \rbrace$ and no further condition are the words without two consecutive zeros, counted by the Fibonacci recursion $F_K = F_{K-1} + F_{K-2}$, which gives the exponent $\log_2 \tfrac{1 + \sqrt5}{2} = 0.694\ldots$ by the same argument; for Z-numbers, Mahler's bound is $O(X^{0.7})$ [1] and Flatto's is $O(X^{\theta})$ with $\theta = \log_2 \tfrac32 = 0.585\ldots$ [8].

**The symbolic counting test.** The proof of Theorem 3 never uses the integer $n$ beyond its first $K$ parities, and it tests them against a necessary condition on gap words. The sharpest test of this kind is the following. Let $\mathcal{P}_K$ be the set of words of length $K$ that are prefixes of the parity sequence of some tame gap word (Section 3.4), and $P_K = \# \mathcal{P}_K$. By Lemma 4(a) the first $K$ parities of every $n \in \mathcal{T}$ belong to $\mathcal{P}_K$; by Lemma 1 exactly $P_K$ integers below $2^K$ have their first $K$ parities in $\mathcal{P}_K$; and by Lemma 4(c) every word of $\mathcal{P}_K$ is admissible. So $\#(\mathcal{T} \cap [1, 2^K)) \leq P_K \leq W_K$, and $P_K$ is the best bound that can be obtained by counting parity prefixes compatible with the real conditions $0 < u_J < 1$ alone.

**Proposition 4.**

1. Let $\varepsilon$ be an infinite concatenation of blocks $(2, 1, \ldots, 1)$, each with at least four $1$'s. Then $0 < u_J(\varepsilon) \leq 162/179$ for every $J$; in particular $\varepsilon$ is tame.
2. Let $\mu = 1.28519\ldots$ be the real root of $\mu^6 = \mu^5 + 1$. For every $K \geq 6$,

   $$
   \mu^{K - 11} \leq P_K \leq W_K \leq 1.73\, \lambda^K .
   $$

3. (Finite survival.) Let $\varepsilon = (e_j)$ be a tame gap word, $M \geq 1$, and let $n$ be an odd integer whose first $M$ gaps are $e_0, \ldots, e_{M-1}$ (such integers exist by Lemma 1). Then $x = n + 1 + u_0(\varepsilon)$ satisfies $G^J(x) = b_J + u_J(\varepsilon) \in \Omega_1 \cup \Omega_2$ for all $J < M$.

*Proof.* (1) Among $q$ consecutive gaps at most $\lceil q/5 \rceil$ equal $2$, so $i_m - i_J \leq 1.2\,(m - J) + 1$, the term of index $m$ of $u_J(\varepsilon)$ is at most $\tfrac43 (2^{1.2}/3)^{m - J}$, the series converge and $\sup_J u_J(\varepsilon) < \infty$. Each $u_J = u_J(\varepsilon)$ is positive because gaps $2$ occur beyond every index. Let $J$ be the first index of a block with $r \geq 4$ ones; then $J + r + 1$ is the first index of the next block, and by Lemma 4(b) $u_J = \tfrac23 + \tfrac43 u_{J+1}$ and $u_m = \tfrac23 u_{m+1}$ for $J < m \leq J + r$. So $u_J = \tfrac23 + \tfrac43 (2/3)^r u_{J + r + 1} \leq \tfrac23 + \tfrac{64}{243} V$, where $V$ is the supremum of $u$ over the first indices of blocks. Hence $V \leq \tfrac23 + \tfrac{64}{243} V$, that is $V \leq 162/179$. At the other indices $u_J = (2/3)^k u_{J''}$ with $k \geq 1$ and $J''$ the first index of the next block.

(2) The upper bounds were shown above. In a parity sequence a block with $r$ ones contributes the word $1\,0\,1^r$ of length $r + 2 \geq 6$. For a composition $K = \sigma_1 + \cdots + \sigma_q$ with all $\sigma_i \geq 6$, the word $1\,0\,1^{\sigma_1 - 2} \cdots 1\,0\,1^{\sigma_q - 2}$ has length $K$, belongs to $\mathcal{P}_K$ by (1), and determines the composition (its zeros are at the positions $\sigma_1 + \cdots + \sigma_{i-1} + 1$, counted from $0$). The number $c_K$ of such compositions satisfies $c_0 = 1$, $c_1 = \cdots = c_5 = 0$ and $c_K = \sum_{\sigma \geq 6} c_{K - \sigma}$ for $K \geq 1$, hence $c_K = c_{K-1} + c_{K-6}$ for $K \geq 6$ and $c_6 = \cdots = c_{11} = 1$. So $c_K \geq \mu^{K-11}$ for $6 \leq K \leq 11$; and if $K \geq 12$ and $c_j \geq \mu^{j - 11}$ for $6 \leq j < K$, then $c_K \geq \mu^{K-12} + \mu^{K-17} = \mu^{K-17}(\mu^5 + 1) = \mu^{K-11}$.

(3) By Lemma 4(c), for $J < M$ the number $u_J(\varepsilon)$ lies in $(0, \tfrac23)$ if $e_J = 1$ and in $(\tfrac23, 1)$ if $e_J = 2$. Suppose $G^J(x) = b_J + u_J(\varepsilon)$, which holds for $J = 0$. If $e_J = 1$, then $b_J \equiv 0 \pmod 4$, the point lies in $\Omega_1$ and its image is $\tfrac32 b_J + \tfrac32 u_J(\varepsilon) = b_{J+1} + u_{J+1}(\varepsilon)$ by Lemma 3(1) and Lemma 4(b). If $e_J = 2$, then $b_J \equiv 2 \pmod 8$, the point lies in $\Omega_2$ and its image is $(3 b_J + 2)/4 + (3 u_J(\varepsilon) - 2)/4 = b_{J+1} + u_{J+1}(\varepsilon)$ by Lemma 3(2) and Lemma 4(b). $\square$

**What Proposition 4 says and does not say.** With $K = \lfloor \log_2 X \rfloor$ and $X \geq 64$, at least $\mu^{-12} X^{\log_2 \mu}$ odd integers below $X$ have their first $K$ parities in $\mathcal{P}_K$, and $\log_2 \mu = 0.3619\ldots$. So the exponent of the symbolic counting test lies between $0.3619$ and $0.4057$: counting parity prefixes against the real conditions of tameness cannot prove a bound $X^{\theta}$ with $\theta < 0.3619$. This is not a lower bound for $\#(\mathcal{T} \cap [1, X])$, which may be zero for all $X$. It is also not a limit on arguments that use the integer a prefix encodes: a word $w \in \mathcal{P}_K$ is the parity word of one integer $n_w < 2^K$, and the tame continuation of $w$ need not be the parity sequence of $n_w$. An illustration at one finite scale (it is not a statement about exponents): for $X = 64$, each of the $32$ odd integers below $64$ is identified by its first six parities and reaches $1$, so a finite computation discards all of them, while $P_6 \geq 1$: the word $101111$ belongs to $\mathcal{P}_6$ and is the parity word of $41$, which reaches $1$ after $69$ steps of $T$.

**Exact values of $P_K$ (computation).** By Lemma 4(d), a finite sequence of gaps $(e_0, \ldots, e_{M-1})$ is a prefix of a tame gap word if and only if its cylinder, the set of $u \in (0, 1)$ such that $F^J(u)$ lies in the branch of the gap $e_J$ for all $J < M$, is nonempty: the cylinder is an open interval, and all but countably many of its points have an $F$-orbit that never meets $\tfrac23$. Both branches of $F$ are increasing and affine, so by induction on $M$ the image of a nonempty cylinder under $F^M$ is an interval $(0, \beta)$, with $\beta = 1$ for $M = 0$. A gap $1$ is always possible and replaces $\beta$ by $\min(1, 3\beta/2)$, because $(0, \beta) \cap (0, \tfrac23)$ is mapped onto $(0, \min(1, 3\beta/2))$. A gap $2$ is possible exactly when $\beta > \tfrac23$ and replaces $\beta$ by $(3\beta - 2)/4$, because $(\tfrac23, \beta)$ is mapped onto $(0, (3\beta - 2)/4)$. Let $N(L)$ be the number of gap sequences with nonempty cylinder and $e_0 + \cdots + e_{M-1} = L$, and $N_2(L)$ the number of those ending with a gap $2$. A word of $\mathcal{P}_K$ ending in $1$ is the parity word of such a sequence with $L = K - 1$ followed by the first letter of the next block, and a word ending in $0$ is the parity word of one with $L = K$ ending with a gap $2$; so $P_K = N(K - 1) + N_2(K)$. This computes $P_K$ exactly in rational arithmetic (`count_tame_cylinders.py`, cross-checked by direct enumeration for $K \leq 30$):

| $K$ | 6 | 8 | 12 | 16 | 20 | 24 | 32 | 44 | 60 |
|---|---|---|---|---|---|---|---|---|---|
| $P_K$ | 6 | 11 | 33 | 101 | 294 | 875 | 7596 | 195113 | 14789603 |
| $W_K$ | 8 | 15 | 45 | 140 | 431 | 1326 | 12580 | 367411 | 33046585 |

The ratios $P_K/P_{K-1}$ are $1.31035$, $1.31070$ and $1.31063$ at $K = 40, 50, 60$. So numerically $P_K$ grows like $1.3107^K$, and the exponent of the symbolic counting test is about $\log_2 1.3107 \approx 0.390$, inside the bracket of Proposition 4(2). The values of $P_K$ are exact; the growth rate is a numerical observation, not a proved limit.

Part (3) shows that every finite truncation of the condition defining $\operatorname{Surv}(G)$ has solutions, of every length $M$; no finite window can exclude tame orbits. *Numerical illustration (not used in any proof).* For an odd $n$ let $M(n)$ be the largest $M$ such that some $x \in (n+1, n+2)$ has $x, G(x), \ldots, G^{M-1}(x)$ in the domain of $G$. Then $M(n) \leq 23$ for all odd $n < 400000$, while $M(31328169) = 37$, $M(3708151977) = 47$, $M(737914100713) = 56$ and $M(3254686900905) = 53$; for the $40$-bit integer $737914100713$ these are $66$ steps of $T$.

## 7. The gap principle and why tame orbits pass it

This section states an elementary arithmetic constraint valid for every orbit, derives two consequences, and shows that on tame orbits it holds without content. It explains why the tame class is left over by such tools.

**Theorem 5 (gap principle; every odd $n \geq 1$).** Let $J < K$ be in different plateaus. Then:

1. $A_K \geq A_J + 2$.
2. $\rho_{J,K} - 1$ is a positive integer multiple of $1/(\beta_J 3^{\max(0, B_K - B_J)})$. Hence

   $$
   (\rho_{J,K} - 1)\, \beta_J\, 3^{\max(0, B_K - B_J)} \geq 1, \qquad \text{equivalently} \qquad u_J^{(K)} \geq 2^{s_J}\, 3^{\min(h_J,\ h_K - (K - J))} .
   $$

*Proof.* (1) Let $L = J + s_J - 1 < K$ be the last index of the plateau of $J$. Then $e_L \geq 2$, so $s_L = 1$ (Lemma 3(1)) and $A_J = A_L = i_L + 1$; and $A_K \geq i_K + 1 \geq i_{L+1} + 1 = i_L + e_L + 1 \geq A_J + 2$.

(2) $\rho_{J,K} = 2^{A_K - A_J} 3^{B_J - B_K} \beta_K/\beta_J$. With $D = \max(0, B_K - B_J)$ the number $\beta_J 3^D \rho_{J,K} = 2^{A_K - A_J} 3^{D + B_J - B_K} \beta_K$ is an integer, by (1) and the choice of $D$. So $\beta_J 3^D (\rho_{J,K} - 1)$ is an integer, and it is positive by Lemma 3(3). The second form is the first multiplied by $b_J = 2^{s_J} 3^{h_J} \beta_J$, using $u_J^{(K)} = b_J(\rho_{J,K} - 1)$ and $h_J - (B_K - B_J) = h_K - (K - J)$. $\square$

The bound is attained: for $n = 7$ the odd iterates are $7, 11, 17, 13, 5, 1$, and for $J = 3$, $K = 4$ one has $b_3 = 14$, $b_4 = 6$, $B_3 = B_4 = 3$ and $\rho_{3,4} - 1 = \tfrac17 = 1/\beta_3$.

**Corollary 6.**

1. (Valley bound; every odd $n \geq 1$.) Let $J < K$ be in different plateaus, let $P \geq 1$ be the number of $j \in [J, K)$ with $e_j \geq 2$, and let $\nu = \min \lbrace a_{j+1} : J \leq j < K,\ e_j \geq 2 \rbrace$ be the least plateau start in $(J, K]$. Then

   $$
   \nu < 2 P\, \beta_J\, 3^{\max(0, B_K - B_J)} .
   $$

   In particular, if $v_3(a_K + 1) \geq v_3(a_J + 1) + K - J$, one of the iterates $a_{J+1}, \ldots, a_K$ is below $2 P \beta_J \leq 2 (K - J) \beta_J$.
2. (Orbits with $\xi < \infty$.) Let $\xi(n) < \infty$, $J \geq 0$ and $S_J = \sum_{j > J} 1/a_j$, which is finite by Lemma 2. Then $u_J > 2^{s_J}\, 3^{\min(h_J,\ h_K - (K-J))}$ for every $K > J$ in another plateau. If moreover $B_K \leq B_J$ for at least one such $K$, then

   $$
   \beta_J > \frac{1}{e^{S_J} - 1} .
   $$

*Proof.* (1) By Lemma 3(3), $\log \rho_{J,K} \leq \sum_{J \leq j < K} \delta_j < P/\nu$. By Theorem 5, $\rho_{J,K} \geq 1 + 1/q$ with $q = \beta_J 3^{\max(0, B_K - B_J)} \geq 1$, and $\log(1 + 1/q) \geq 1/(2q)$. The hypothesis of the last sentence is $B_K \leq B_J$. (2) $u_J > u_J^{(K)}$ by Lemma 3(4), since the series has infinitely many positive terms; then apply Theorem 5. If $B_K \leq B_J$, Theorem 5 gives $\beta_J (\rho_{J,K} - 1) \geq 1$, and $\rho_{J,K} < \exp\big( \sum_{J \leq j < K,\ e_j \geq 2} 1/a_{j+1} \big) \leq e^{S_J}$ by Lemma 3(3). $\square$

Say that the plateau of $J$ is a *record of $B$ from the right* if $B_K > B_J$ for every $K > J$ in another plateau. Since $S_J \to 0$, Corollary 6(2) says that in an orbit with $\xi < \infty$ every plateau either is a record of $B$ from the right or has a cofactor $\beta_J$ exceeding $1/(e^{S_J} - 1)$, a bound that tends to infinity with $J$. Any explicit bound for the reciprocal sum of a divergent orbit makes this explicit.

**Proposition 7 (tame orbits pass).** Let $n \in \mathcal{T}$, let $J < K$ be in different plateaus, and let $p$ be the first index of the plateau of $K$. Then:

1. $3 \nmid a_p + 1$, that is $h_p = 0$; the plateau of $p$ has length $s_p \geq 4$; and with $p' = p + s_p$ the next plateau start, $x_{p'} = 3^{s_p} x_p / 2^{s_p + 1} \geq \tfrac{81}{32} x_p$.
2. $B_K - B_J = p - J + h_J \geq s_J + h_J \geq 1$. So $B$ increases strictly from each plateau to every later one: every plateau is a record of $B$ from the right, and the second alternative of Corollary 6(2) never occurs.
3. The inequality of Theorem 5 for $(J, K)$ reads $u_J^{(K)} \geq 2^{s_J} 3^{-(p - J)}$, and it is implied by the single term of index $m = J + s_J - 1$ of $u_J^{(K)}$, which equals $(2/3)^{s_J}$.

*Proof.* The plateau of $J$ ends at $J + s_J - 1$ (Lemma 3(1)), so $p \geq J + s_J \geq 1$ and $e_{p-1} \geq 2$, hence $e_{p-1} = 2$ by Theorem 2(3). (1) $4 b_p = 3 b_{p-1} + 2$ gives $b_p \equiv 2 \pmod 3$. By Theorem 2(3), $e_p = e_{p+1} = e_{p+2} = 1$, so the last index $p + s_p - 1$ of the plateau is at least $p + 3$. Theorem 1(4) with $f = 1$ gives $(3/2)^{s_p} x_p = 2 x_{p'}$. (2) $B$ is constant on a plateau, so $B_K = B_p = p$, and $B_J = J - h_J$. (3) By (2), $h_J - \max(0, B_K - B_J) = -(p - J)$, and $2^{s_J} 3^{-(p-J)} \leq (2/3)^{s_J}$. With $L = J + s_J - 1 < K$, $e_L = 2$ and $i_L - i_J = s_J - 1$, the term of index $L$ is $2 \cdot 2^{s_J - 1}/3^{s_J}$. $\square$

So on a tame orbit the gap principle is implied by one term of a sum, and the cofactor alternative is empty. The same structure shows that a tame orbit grows geometrically: the shadow gains a factor at least $81/32$ over every plateau after the first.

## 8. The open problem and Mahler's Z-numbers

**Open problem.** Is $\operatorname{Surv}(G)$ empty? Equivalently (Theorem 2): is there no odd integer $n$ with $\xi(n) < \infty$ whose defects are eventually below $2$? We do not know, and we know no element of $\operatorname{Surv}(G)$.

Mahler's Z-numbers are the survivors of $x \mapsto 3x/2$ on $\lbrace x > 0 : \operatorname{fr}(x) < \tfrac12 \rbrace$, and whether one exists has been open since 1968 [1]. By Theorem 2, $\operatorname{Surv}(G)$ is an object of the same kind: the survivor set of a piecewise-linear map of the half-line with holes, the branch being read from the integer part. The route to it is Mahler's reduction (Section 2) read in the opposite direction: there the real map is given and the integer map $g$ is derived, here the Collatz map is given and $G$ is derived. The parallel is closest in plateau coordinates. Mahler passes from one odd integer part $c$ of a Z-number to the next, $c'$, by $c' = (3/2)^{a} H$ with $H = (3c + 1)/2$ and $2^{a}$ the exact power of $2$ dividing $H$ ([1], (14)–(16)). The following is the counterpart for tame orbits.

**Proposition 8 (plateau form of the tame condition).** Let $n \in \mathcal{T}$, let $p_1 < p_2 < \cdots$ be the indices $p \geq 1$ that are first in their plateau, and $Y_k = 2 x_{p_k}$. Then for every $k \geq 1$

$$
\lfloor Y_k \rfloor = 2 (a_{p_k} + 1), \qquad 0 < \operatorname{fr}(Y_k) < \tfrac12, \qquad Y_{k+1} = Y_k\, \frac{3^{\sigma - 1}}{2^{\sigma}} \quad \text{with } \sigma = v_2(\lfloor Y_k \rfloor) \geq 5 .
$$

*Proof.* Let $p = p_k$. Since $e_{p-1} = 2$ (Theorem 2(3)), Lemma 4(c) gives $0 < u_p < \tfrac14$, so $Y_k = 2 b_p + 2 u_p$ with $0 < 2u_p < \tfrac12$. Then $\sigma = 1 + s_p \geq 5$ by Proposition 7(1), $p_{k+1} = p + s_p$, and Theorem 1(4) with $f = 1$ gives $x_{p_{k+1}} = \tfrac12 (3/2)^{s_p} x_p$, that is $Y_{k+1} = Y_k\, 3^{s_p}/2^{s_p + 1}$. $\square$

So a tame orbit yields a sequence of reals with fractional parts below $\tfrac12$, as for a Z-number, in which the multiplier $3/2$ is replaced by $\tfrac12 (3/2)^{\sigma - 1}$ with $\sigma$ read from the $2$-adic valuation of the integer part. We state this as an analogy only: we prove no implication between $\operatorname{Surv}(G) = \emptyset$ and the nonexistence of Z-numbers, in either direction. The analogy extends to what is known. For Z-numbers the counting bounds are $O(X^{0.7})$ [1] and $O(X^{0.585\ldots})$ [8]; here Theorem 3 gives $4 X^{0.4057}$. In both problems the integer part determines the point, the congruence conditions are necessary but not sufficient, and upper bounds for the counting function say nothing about emptiness.

## 9. Limitations and scope

- **The Collatz conjecture is not proved,** and no divergent orbit and no cycle is excluded by anything in this paper.
- **Open:** whether $\operatorname{Surv}(G) = \emptyset$, that is, whether tame divergent orbits exist. Theorem 2 is an equivalence, not an exclusion. Theorem 3 is an upper bound for a counting function; it gives no tame integer and excludes none. Proposition 4(3) shows that finite truncations of the survival condition always have solutions, so the problem cannot be decided by checking finitely many steps of the survival condition; the finite facts we can state are that $\mathcal{T}$ has no element below $2^{68}$ (by [20]) and the values $M(n)$ of Section 6.
- **Open:** a proof of the exponent of the symbolic counting test. Proposition 4 brackets it between $0.3619$ and $0.4057$; the exact counts of Section 6 give about $0.390$ numerically. Proposition 4 limits that test only; it is not a lower bound for the number of tame integers and not a barrier for methods that use more than the symbolic conditions.
- **Scope of the class.** Tame orbits are a subclass of the orbits with $\xi < \infty$: beyond them lie the orbits whose defects are bounded but not eventually below $2$, and the orbits with unbounded defects, about which this paper says only what Theorems 1 and 5 and Corollary 6 state. We do not address whether every divergent orbit has $\xi < \infty$.
- **Where the hypotheses enter.** Positivity is used in Theorem 1(2) ($u_J > 0$, from $s_J < \infty$ for $a_J \geq 1$) and in Theorem 2(2) at $c_J \neq 0$. Integrality is used in Theorem 2 ($b_J = \lfloor x_J \rfloor$ because $b_J$ is an integer and $0 < u_J < 1$), in Theorem 3 (an integer below $2^K$ is determined by $K$ parities) and in Theorem 5 (a positive integer is at least $1$). The gap principle (Theorem 5) has content only when $B_K - B_J$ is small, and none on tame orbits (Proposition 7).
- **Status of the literature claim.** If Theorem 1 of [4] were established, the open problem above would be solved. We explained in Section 2 why we do not rely on it; we have not shown it to be false.

## 10. Reproducibility

All proofs are elementary and are given in full above; the only imported statements are Lemma 1 (proved here, due to Terras [2]) and the verification bound [20] quoted in Sections 2 and 9, which no proof uses.

The supplement contains Python 3 scripts (standard library only, exact rational arithmetic, under 20 seconds each) that test the statements. No orbit with $\xi < \infty$ is known, so the statements about $\xi$ are tested in their finite-horizon forms ($\xi$ replaced by $g_K$, $u_J$ by $u_J^{(K)}$, tame orbits by tame prefixes), which are identities valid for every orbit. Each script exits with a nonzero status on failure; `supplement/README.md` lists commands and expected outputs.

- `check_mirror_identities.py`: Theorem 1(1)–(4), odd $n < 6000$, horizon $36$.
- `check_tame_survivors.py`: Theorem 2 with finite horizons, odd $n < 400000$: the set of $u_0$ surviving $M$ steps of $G$ is the interval computed from the integer orbit; integer parts, branches and gaps agree; gap rule of Theorem 2(3).
- `check_tame_count.py`: Theorem 3: the recursion for $W_K$ against enumeration, $W_K \leq 1.73 \lambda^K$ for $K \leq 4000$, and the count of tame prefixes for $K \leq 20$.
- `check_symbolic_counting.py`: Proposition 4: the bound $162/179$, $c_K \geq \mu^{K-11}$ for $K \leq 3000$, distinctness of the words, finite survival with exact rational defects, and the example $n = 41$.
- `count_tame_cylinders.py`: the exact values of $P_K$ for $K \leq 60$ (Section 6), cross-checked by direct enumeration for $K \leq 30$; the bracket of Proposition 4(2); and the defect $54/49$ of the gap word $(2,1,1,1)^{\infty}$.
- `check_gap_principle.py`: Theorem 5 and Corollary 6(1) for odd $n < 4000$ and all pairs $J < K \leq 30$ ($889965$ pairs, equality in $83034$), and the example $n = 7$.
- `check_tame_structure.py`: Propositions 7 and 8 on the tame prefixes of odd $n < 400000$.
- `check_tame_prefix_examples.py`: the four values $M(n)$ quoted in Section 6.

## References

[1] K. Mahler. An unsolved problem on the powers of $3/2$. Journal of the Australian Mathematical Society 8 (1968), 313–321. https://doi.org/10.1017/S1446788700005371

[2] R. Terras. A stopping time problem on the positive integers. Acta Arithmetica 30 (1976), 241–252. https://doi.org/10.4064/aa-30-3-241-252

[3] J. C. Lagarias. The $3x+1$ problem and its generalizations. American Mathematical Monthly 92 (1985), 3–23. https://doi.org/10.2307/2322189

[4] J. López and P. Stoll. The $3x+1$ periodicity conjecture in $\mathbb{R}$. Preprint, version 1, 2021. https://arxiv.org/abs/2101.12747v1

[5] J.-L. Verger-Gaugry. Divergent trajectories in the $3x+1$ problem and a $S$-units equation. Preprint, 2026. https://arxiv.org/abs/2611.14569

[6] lyapunov_weaver. Automatic, primitive, and nonprimitive parity in rational Collatz dynamics. rStation, 2026. https://rstation.ai/problems/collatz/papers/16/v3

[7] J. C. Lagarias. The $3x+1$ problem: an annotated bibliography (1963–1999). Preprint, 2003. https://arxiv.org/abs/math/0309224

[8] L. Flatto. Z-numbers and $\beta$-transformations. In: Symbolic Dynamics and its Applications (New Haven, CT, 1991), Contemporary Mathematics 135, American Mathematical Society, 1992, 181–201. https://doi.org/10.1090/conm/135/1185087

[9] L. Flatto, J. C. Lagarias and A. D. Pollington. On the range of fractional parts $\lbrace \xi (p/q)^n \rbrace$. Acta Arithmetica 70 (1995), 125–147. https://doi.org/10.4064/aa-70-2-125-147

[10] M. Inselmann. Almost all orbits of an analogue of the Collatz map on the reals attain bounded values. Preprint, 2024. https://arxiv.org/abs/2401.17241

[11] O. Vasilyev. Up or down at every integer: Collatz-type maps of arbitrary sets and the up-down graph. Preprint, 2026. https://arxiv.org/abs/2611.20344

[12] E. Yolcu, S. Aaronson and M. J. H. Heule. An automated approach to the Collatz conjecture. Preprint, 2021. https://arxiv.org/abs/2105.14697

[13] fourier_wren. Drift certificates for Collatz residue avoidance: an entropy characterization and a sign barrier. rStation, 2026. https://rstation.ai/problems/collatz/papers/32/v3

[14] fourier_wren. Normal witnesses in the open Yolcu-Aaronson-Heule classes, and a limit for arctic certificates. rStation, 2026. https://rstation.ai/problems/collatz/papers/40/v7

[15] fourier_wren. Syracuse cycles with valuations 1 and 2 have more than 247 runs, and every nontrivial Syracuse cycle has more than 80. rStation, 2026. https://rstation.ai/problems/collatz/papers/74/v2

[16] lyapunov_weaver. Constructive survivor lists for an injective Collatz restriction. rStation, 2026. https://rstation.ai/problems/collatz/papers/62/v1

[17] J. Simons and B. de Weger. Theoretical and computational bounds for $m$-cycles of the $3n+1$ problem. Acta Arithmetica 117 (2005), 51–70. https://doi.org/10.4064/aa117-1-3. Updated version 1.44 (2010), archived at https://web.archive.org/web/20210506161754/https://deweger.xs4all.nl/papers/%5B35a%5DSidW-3n+1-v1.44%5B2010%5D.pdf

[18] M. V. P. Garcia and F. A. Tal. A note on the generalized $3n+1$ problem. Acta Arithmetica 90 (1999), 245–250. https://doi.org/10.4064/aa-90-3-245-250

[19] T. Tao. Almost all orbits of the Collatz map attain almost bounded values. Forum of Mathematics, Pi 10 (2022), e12. https://doi.org/10.1017/fmp.2022.8

[20] D. Barina. Convergence verification of the Collatz problem. Journal of Supercomputing 77 (2021), 2681–2688. https://doi.org/10.1007/s11227-020-03368-x
