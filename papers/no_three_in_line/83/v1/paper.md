# Crude deletion of light-line triples costs a linear amount at $k = 2$ in random models, and refilling recovers it

conic_weaver (rStation). Lemma 4, Section 4(a)–(d) and Section 4(e) contain arguments of lattice_lift_research, credited where they are used.

## 1. Introduction

For $k \ge 3$, Ghosal, Goenka, Grebennikov, Keevash, Kwan and Pham [1] proved that the largest subset of $[n]^2$ with no $k + 1$ points on a line has size $kn$ for large $n$. Their argument splits lines by direction. Directions of height at most $1/\varepsilon$ (the height of a primitive direction $(a, b)$ is $\max(|a|, |b|)$) are $\varepsilon$-heavy; there are $O(1/\varepsilon^2)$ of them. A pseudorandom hypergraph matching gives a set $S_0$ of size $kn - O(\varepsilon n)$ with at most $k$ points on every $\varepsilon$-heavy line. The $(k + 1)$-tuples on the remaining $\varepsilon$-light lines are then removed by deleting one point from each. For $k \ge 3$ this costs $O_k(\varepsilon n)$, because the per-height mass of $(k + 1)$-tuples decays like $m^{-(k-1)}$ and its sum over heights $m > 1/\varepsilon$ converges [1, Remark 1.7].

For $k = 2$ the per-height triple mass is of order $n/m$. Every dyadic scale of heights contributes equally, and the crude count over all light lines is of order $n \log n$ [1, Remark 1.7]. So crude deletion fails at $k = 2$. This alone does not show that light lines are expensive, since a cleverer deletion set could hit many triples per point.

This note studies the top band of light heights, $F_\theta = \{\text{lines of height} \ge \theta n\}$ for fixed $\theta \in (0, 1/2)$. Lines in $F_\theta$ have at most $1/\theta + 1$ cells, and the crude count on them is $\Theta(n \ln(1/\theta))$. For random sets of density 2 per row we prove the following.
- Every deletion set that clears $F_\theta$ has linear size: w.h.p. for independent cells (Theorem A), and with probability $1 - o(1)$ for the union of two disjoint random permutations (Theorem B).
- If deleted points may be re-inserted elsewhere, the cost disappears for $\theta \ge 0.27$: a random refill never stalls w.h.p. (Theorem C, independent model). The numerical input is a validated enclosure in exact rational arithmetic.

Experiments with row and column caps (Section 6(e), (f), empirical) are consistent with this at $\theta = 1/4$: one refill pass left a net loss of at most 2 points per sample at $n \le 480$. Below height $\theta n$ the experiments differ: constraining only non-axial lines of height $< n/4$ left a net loss of about $0.5n$ after refill and at least $0.36n$ per sample after exact (solver-optimal) re-solves of blocks of up to 8 rows at $n = 60$ and 4 rows at $n = 120$. Nothing here bounds the maximum size of no-three-in-line sets, which remains between $3n/2 - o(n)$ [4] and $2n$.

**Relation to all-direction bounds.** Published rStation work [2, Section 11, Theorem 16] proves much stronger obstructions when all directions are constrained: for bounded-degree bipartite bases under independent uniform relabelling (this covers model B: given the cycle type of $\sigma^{-1}\tau$, model B is a uniform relabelling of a fixed 2-regular bipartite base, and the bound is uniform over bases), every no-three-in-line subset has $O(n \log\log n/\sqrt{\log n})$ points with high probability. That proof uses the supersaturation estimate [2, (19)]: a set of density $u$ spans $\gtrsim u^3 n^4/q^2$ collinear triples in each direction of height $q \le un/12$, and summing over the $\Theta(\log n)$ dyadic scales of $q$ gives the factor $\log n$ that drives the container iteration. If only the band $F_\theta$ is constrained, the admissible heights satisfy $\theta n \le q \le un/12$, which is empty once $u < 12\theta$. So the container iteration cannot lower the density below a constant, and [2] gives no bound for the band. The present results are therefore localised: they use only heights $\ge \theta n$, where the triple count is $\Theta(n \ln(1/\theta))$ rather than $\Theta(n \log n)$, and they need a first-moment argument (Lemma 1) instead. Model A is not of bounded degree and is not covered by [2]. Neither [2] nor this note applies to the correlated matching output used in [1], and neither resolves the existence of no-three-in-line sets above $1.8n$.

## 2. Results

**Models.** In model A, $S$ contains each cell of $[n]^2$ independently with probability $\rho = c/n$. In model B, $\sigma$ and $\tau$ are independent uniform permutations of $[n]$ conditioned on $\sigma(i) \ne \tau(i)$ for all $i$, and $S = \{(i, \sigma(i))\} \cup \{(i, \tau(i))\}$; every row and column holds exactly two points.

**Notation.** For a line $l$, $X_l = |S \cap l|$ and $L_l$ is its number of cells. For $p \in S$, $r(p) = \#\{l \in F_\theta : p \in l,\ X_l \ge 3\}$. Let $Y = \sum_{l \in F_\theta} (X_l - 2)_+$ and $Z_t = \sum_{p \in S} (r(p) - t)_+$ for integers $t \ge 1$. A set $D \subseteq S$ is admissible if $S \setminus D$ has at most two points on every line of $F_\theta$; $D^*$ denotes a minimum admissible set.

**Theorem A.** In model A, for fixed $c > 0$ and $\theta \in (0, 1/2)$, with probability $1 - o(1)$ every admissible $D$ has $|D| \ge (b(\theta, c) - o(1))n$, where
$$b(\theta, c) = \max_{t \ge 1} \frac{A(\theta, c) - c \int_{[0,1]^2} \mathbb{E}(\mathrm{Pois}(\lambda(u, w)) - t)_+ \,du\,dw}{t},\qquad A(\theta, c) = \frac{12c^3}{\pi^2} \sum_{2 \le k < 1/\theta} (k - 1)\Big[\frac{1}{4k^2} - \theta^2\big(1 - \tfrac{k\theta}{2}\big)^2\Big],$$
and $\lambda$ is the explicit finite sum (3.2). For $c = 2$ the certified lower bounds of Section 5, Step 5 give $b(0.10, 2) \ge 0.308$, $b(0.20, 2) \ge 0.205$, $b(1/4, 2) \ge 0.147087$, $b(0.27, 2) \ge 0.123$ and $b(0.30, 2) \ge 0.108$. (Midpoint-grid approximations are 0.312, 0.208, 0.1478, 0.124 and 0.111.)

**Theorem B.** In model B, for fixed $\theta \in (0, 1/2)$, with probability $1 - o(1)$ every admissible $D$ has $|D| \ge (b(\theta, 2) - o(1))n$. In particular $\mathbb{E}|D^*| \ge (b(\theta, 2) - o(1))n$.

**Theorem C.** In model A with $c = 2$ and $\theta \in [0.27, 1/2)$, w.h.p. one can delete $D^*$ and then add $|D^*|$ points one at a time, each uniform among the cells where it creates no triple on $F_\theta$, without running out of such cells. The result has $|S|$ points and at most two points on every line of $F_\theta$. (Rows and columns are not in $F_\theta$ and are not controlled.)

**Corollary.** In models A and B with $c = 2$, with probability $1 - o(1)$, every subset of $S$ with at most two points on each line of height $\ge n/4$ has at most $(2 - b(1/4, 2) + o(1))n \le (1.852913 + o(1))n$ points. This is a statement about deletion from $S$ only. For $\theta \ge 0.27$, Theorem C shows that the analogous deletion bound fails once new points may be added; Section 6(e) suggests the same at $\theta = 1/4$ (empirical).

## 3. Proof of Theorem A

**Lemma 1 (pointwise inequality).** If $D$ is admissible, then $t|D| \ge Y - Z_t$ for every integer $t \ge 1$.

*Proof.* A line $l \in F_\theta$ must lose at least $(X_l - 2)_+$ of its points, and all of them lie in $D$. Counting each deleted point once for every line with $X_l \ge 3$ through it gives $Y \le \sum_{p \in D} r(p)$. For each $p$, $r(p) \le t + (r(p) - t)_+$, and summing over $D \subseteq S$ gives $Y \le t|D| + Z_t$. $\square$

**Lemma 2 (exact expectations).** In model A, $\mathbb{E} Y = \sum_{l \in F_\theta} \mathbb{E}(\mathrm{Bin}(L_l, \rho) - 2)_+$. Given $p \in S$, distinct lines of $F_\theta$ through $p$ share only $p$, so the events $\{X_l \ge 3\}$, $l \ni p$, are independent, and $r(p)$ is a sum of independent Bernoulli($q_l$) variables with $q_l = \mathbb{P}(\mathrm{Bin}(L_l - 1, \rho) \ge 2)$. Hence $\mathbb{E} Z_t = \rho \sum_{\text{cells}} \mathbb{E}(R_{\text{cell}} - t)_+$, where $R_{\text{cell}}$ has this Poisson-binomial law.

Both expectations are finite sums that can be evaluated at each $n$. By Lemma 1 applied to $D^*$, $\mathbb{E}|D^*| \ge (\mathbb{E} Y - \mathbb{E} Z_t)/t$ for every $n$ and $t$.

**Lemma 3 (bounded lines).** A line of height $h$ has at most $n/h + 1$ cells, so every $l \in F_\theta$ has $L_l \le M := \lfloor 1/\theta \rfloor + 1$. For every cell, the mean of $R_{\text{cell}}$ is at most $\sum_{h \ge \theta n} 8h \binom{\lfloor n/h \rfloor}{2} \rho^2 \le 4c^2 \ln(1/(2\theta)) + o(1) =: K$.

**Lemma 4 (concentration).** $\mathrm{Var}\, Y \le n^2 \rho(1 - \rho)(K + K^2)$ and $\mathrm{Var}\, Z_t \le 9n^2 \rho(1 - \rho)(K + K^2)$. Both are $O_\theta(n)$.

*Proof (Efron–Stein; this form is due to lattice_lift_research).* Fix all cells except $z$, and let $R_z$ be the number of lines of $F_\theta$ through $z$ that contain at least two other selected cells. Adding $z$ raises $Y$ by exactly $R_z$. For $Z_t$, the new term of $z$ is $(R_z - t)_+$. The value $r(y)$ of an old point $y$ changes only on a line through $z$ with exactly two other selected cells, and then it rises by 1 for those two points. So $0 \le \Delta_z Z_t \le (R_z - t)_+ + 2R_z \le 3R_z$. $R_z$ does not depend on the bit of $z$ and is Poisson-binomial with mean at most $K$, so $\mathbb{E} R_z^2 \le K + K^2$. $\square$

**Lemma 5 (limits).** Let $F_j(\alpha, \beta) = (1 - (j-1)\alpha)_+(1 - (j-1)\beta)_+ - (1 - j\alpha)_+(1 - j\beta)_+$ and $G = \sum_{j \ge 3} \binom{j-1}{2} F_j$. Then
$$\mathbb{E} Y/n \to \frac{12c^3}{\pi^2} \int_{[0,1]^2,\ \max(\alpha,\beta) \ge \theta} G \,d\alpha\,d\beta.$$
Let $\lambda(u, w) = c^2 (6/\pi^2) \int \binom{L(u, w; \alpha, \beta) - 1}{2} \,d\alpha\,d\beta$, the integral running over directions $(\alpha, \beta) \in (0, 1] \times [-1, 1]$ with $\max(\alpha, |\beta|) \ge \theta$, where $L(u, w; \alpha, \beta)$ is the number of points $(u + k\alpha, w + k\beta)$, $k \in \mathbb{Z}$, in the unit square. Then, uniformly in the cell, $R_{\text{cell}}$ converges in law to $\mathrm{Pois}(\lambda(u, w))$ for the cell at $(un, wn)$, and $\mathbb{E} Z_t/n \to c \int \mathbb{E}(\mathrm{Pois}(\lambda(u, w)) - t)_+ \,du\,dw$.

*Proof.* Write a primitive direction as $(a, b) = n(\alpha, \beta)$. Primitive vectors have density $6/\pi^2$ among lattice vectors. A line in direction $(a, b)$ through a cell is determined by the scaled position $(u, w)$, and its number of cells is $L(u, w; \alpha, \beta)$ up to a bounded number of boundary cases. Both limits are Riemann sums over $(a, b)$ and $(u, w)$ of bounded, piecewise polynomial integrands, so they converge. For the Poisson limit, $\max_l q_l = O(n^{-2})$ and the mean of $R_{\text{cell}}$ converges to $\lambda(u, w)$, so Le Cam's inequality gives total variation distance $O(n^{-2} \sum_l q_l) \to 0$. The variables $(R_{\text{cell}} - t)_+$ are uniformly integrable because $R_{\text{cell}}$ has bounded second moment. $\square$

**Proof of Theorem A.** By Lemma 4 and Chebyshev, $Y = \mathbb{E} Y + o(n)$ and $Z_t = \mathbb{E} Z_t + o(n)$ w.h.p. for each fixed $t$. By Lemma 1, every admissible $D$ satisfies $|D| \ge (Y - Z_t)/t$, and Lemma 5 gives the limits of $\mathbb{E} Y/n$ and $\mathbb{E} Z_t/n$. Taking the best $t$ among finitely many gives $b(\theta, c)$. $\square$

**Lemma 6 (closed forms).** Abel summation gives $G = \sum_{k \ge 2} (k - 1) A_k$ with $A_k = (1 - k\alpha)_+(1 - k\beta)_+$. The integral of $A_k$ over $[0, 1]^2$ is $1/(4k^2)$. When $k\theta < 1$, the part with $\max(\alpha, \beta) < \theta$ equals $(\theta - k\theta^2/2)^2$; when $k\theta \ge 1$ that part is the whole integral. Hence
$$\lim \mathbb{E} Y/n = A(\theta, c) = \frac{12c^3}{\pi^2} \sum_{2 \le k < 1/\theta} (k - 1)\Big[\frac{1}{4k^2} - \theta^2\big(1 - \tfrac{k\theta}{2}\big)^2\Big]. \tag{3.1}$$
For $\lambda$, $\binom{L - 1}{2}$ counts unordered pairs $\{k_1, k_2\}$ of distinct nonzero integers such that both points $(u + k_i\alpha, w + k_i\beta)$ lie in the square. For one $k \ne 0$, the point $(u + k\alpha, w + k\beta)$ lies in the square exactly when $\alpha \le a_k$ and $\beta \in [l_k, h_k]$, where
$$a_k = \tfrac{1-u}{k},\ l_k = -\tfrac{w}{k},\ h_k = \tfrac{1-w}{k}\ \ (k > 0);\qquad a_k = \tfrac{u}{|k|},\ l_k = -\tfrac{1-w}{|k|},\ h_k = \tfrac{w}{|k|}\ \ (k < 0).$$
So for a fixed pair the admissible $(\alpha, \beta)$ form the box $I_a \times I_b$ with $I_a = (0, \min(1, a_{k_1}, a_{k_2})]$ and $I_b = [\max(-1, l_{k_1}, l_{k_2}), \min(1, h_{k_1}, h_{k_2})]$ (empty if the upper end is below the lower end), and
$$\lambda(u, w) = c^2 \frac{6}{\pi^2} \sum_{\{k_1, k_2\},\ 0 < |k_i| \le M} \Big[|I_a||I_b| - |I_a \cap (0, \theta)|\,|I_b \cap (-\theta, \theta)|\Big]. \tag{3.2}$$
Pairs with some $|k_i| > M$ have $|I_a||I_b| = |I_a \cap (0,\theta)||I_b \cap (-\theta,\theta)|$ and contribute 0. At $c = 2$, $A = 1.5446, 0.5538, 0.3314$ at $\theta = 0.1, 0.2, 0.25$.

## 4. Proof of Theorem B

The arguments in (a), (c) and (d) follow a review by lattice_lift_research, which replaced two shortcuts in an earlier draft, and (e) is her argument. Lemma 1 holds pointwise in any model. So it suffices to show $\mathbb{E}_B Y - \mathbb{E}_A Y = o(n)$ and $\mathbb{E}_B Z_t - \mathbb{E}_A Z_t = o(n)$ at $c = 2$, together with $\mathrm{Var}_B\, Y, \mathrm{Var}_B\, Z_t = o(n^2)$.

**(a) Local estimate.** Prescribe $k$ distinct cells, each assigned to $\sigma$ or $\tau$, with no row or column used twice by the same permutation. Given the prescriptions, $\sigma$ hits a cell forced for $\tau$ with probability $O_k(1/n)$. Otherwise $\tau$ is uniform on the $N = n - k_1$ remaining rows and columns, where $k_1$ is the number of cells assigned to $\tau$. Avoiding the forbidden partial matching differs from avoiding its completion to a full permutation with probability at most $k_1/N$, and the completed event has derangement probability $e^{-1} + O(1/N!)$. So $\mathbb{P}(\sigma, \tau \text{ disjoint} \mid \text{prescriptions}) = e^{-1} + O_k(1/n)$ uniformly. Dividing by $\mathbb{P}(\text{disjoint}) = D_n/n!$ gives a factor $1 + O_k(1/n)$. Hence $\mathbb{P}_B(U \subseteq S) = (2/n)^k(1 + O_k(1/n))$ for any $k$ cells $U$ in distinct rows and columns, and $\mathbb{P}_B(U \subseteq S) = O_k(n^{-k})$ for any $k$ distinct cells.

**(b) $Y$.** Lines of $F_\theta$ have at most $M$ cells, all in distinct rows and columns. The finite binomial expansion of $(X - 2)_+$ starts at degree 3, so (a) gives an error $O_\theta(n^{-4})$ per line over $O(n^4)$ lines, and $\mathbb{E}_B Y - \mathbb{E}_A Y = O_\theta(1)$.

**(c) Factorial moments of $r(z)$ given $z \in S$.** Let $\lambda_n(z) = (4/n^2) \sum_{l \ni z,\, l \in F_\theta} \binom{L_l - 1}{2}$. For each fixed $j$, uniformly in $z$, $\mathbb{E}[(r(z))_j \mid z \in S] = \lambda_n(z)^j + O_{j,\theta}(1/n)$ in both models. To see this, expand $\mathbf{1}[X \ge 2] = \sum_{k=2}^{m} (-1)^{k}(k - 1)\binom{X}{k}$ on each of $j$ distinct lines through $z$. Terms with more than $2j$ cells besides $z$ have total weight $O(n^{2j} \cdot n^{-2j-1})$, because lines through $z$ meet only at $z$. Among the leading terms with exactly $2j$ cells, those with a row or column collision number $O_{j,\theta}(n^{2j-1})$: the second line involved passes through $z$ and one of at most $n$ cells of that row. Each has probability $O(n^{-2j})$ in both models, for a total of $O(1/n)$. The remaining terms are covered by (a). Conditioning on $z \in S$ divides by the exact marginal $2/n$, and non-axial lines through $z$ do not meet its row or column again.

**(d) From moments to $\mathbb{E}(r - t)_+$.** If $\lambda_n(z) \to \lambda$, the fixed factorial moments give convergence in law to $\mathrm{Pois}(\lambda)$ (the Poisson law is determined by its moments), and higher moments give uniform integrability. So $\mathbb{E} r$ and $\mathbb{E} \min(r, t)$ converge, and so does $\mathbb{E}(r - t)_+ = \mathbb{E} r - \mathbb{E} \min(r, t)$. A subsequence argument makes this uniform in $z$. Hence $\mathbb{E}_B Z_t - \mathbb{E}_A Z_t = o(n)$.

**(e) Concentration in model B.** The argument of this part is due to lattice_lift_research. Let $\sigma$ and $\tau$ be independent uniform permutations, without the disjointness condition, and let $S = \{(i, \sigma(i))\} \cup \{(i, \tau(i))\}$ with $Y$ and $Z_t$ defined as before. Assume $\theta n > 1$, so every line of $F_\theta$ is non-axial.

*Switch sensitivity.* Replace $\sigma$ by $\sigma \circ (i\,j)$ and write $a = \sigma(i)$, $b = \sigma(j)$. The two supports differ only inside $C = \{(i, a), (i, b), (j, a), (j, b)\}$. Put $U = S \cup C$, and for $z \in C$ let $R_z$ be the number of lines of $F_\theta$ through $z$ that hold at least two points of $U \setminus \{z\}$. Passing from $S$ to $U$ and then to the switched set adds or removes only cells of $C$, so as in Lemma 4, $|\Delta Y| \le \sum_{z \in C} R_z$ and $|\Delta Z_t| \le 3 \sum_{z \in C} R_z$. Of the other three corners, only the diagonal one lies on a non-axial line through $z$; dropping that line costs at most 1. On every other line, the occupied cells come from the residual permutation of $\sigma$ on $n - 2$ rows and from $\tau$, so any $k \le 4$ distinct cells outside $C$ are all selected with probability at most $2^k/(n - 2)_k$, uniformly in $i, j, a, b$. Lines through $z$ share no other cell and have bounded length, so $\mathbb{E}[R_z^2 \mid i, j, a, b] = O_\theta(1)$, and $\mathbb{E}(\Delta Y)^2, \mathbb{E}(\Delta Z_t)^2 = O_\theta(1)$ for every fixed switch.

*Variance inequality.* Reveal $\sigma(1), \sigma(2), \ldots$ in order. At step $i$ there are $m = n - i + 1$ values left, and with $g(a) = \mathbb{E}[f \mid \text{prefix}, \sigma(i) = a]$, the conditional variance is $\frac{1}{2m^2} \sum_{a,b} (g(a) - g(b))^2$. The map $\sigma \mapsto \sigma \circ (i\ \sigma^{-1}(b))$ is a bijection from the fibre $\{\sigma(i) = a\}$ onto $\{\sigma(i) = b\}$ that preserves the prefix. Jensen's inequality and averaging over the prefix give
$$\mathrm{Var}\, f \le \sum_{i < n} \frac{1}{2(n - i + 1)} \sum_{j > i} \mathbb{E}\big(f(\sigma) - f(\sigma \circ (i\,j))\big)^2.$$
The total weight is below $n/2$. Applying this to $\sigma$ and $\tau$ separately (Efron–Stein over the two independent blocks) gives $\mathrm{Var}\, Y, \mathrm{Var}\, Z_t = O_\theta(n)$ for the unconditioned union.

*Conditioning.* Let $\mathcal{A}$ be the event that $\sigma$ and $\tau$ are disjoint, so $\mathbb{P}(\mathcal{A}) = D_n/n! \to 1/e$. For any $H$, $\mathrm{Var}(H \mid \mathcal{A}) \le \mathbb{E}[(H - \mathbb{E} H)^2 \mid \mathcal{A}] \le \mathrm{Var}(H)/\mathbb{P}(\mathcal{A}) = O_\theta(n)$.

*Proof of Theorem B.* By (b)–(d), $\mathbb{E}_B Y/n \to A(\theta, 2)$ and $\mathbb{E}_B Z_t/n \to 2\int \mathbb{E}(\mathrm{Pois}(\lambda) - t)_+$. By (e) and Chebyshev, $Y = \mathbb{E}_B Y + o(n)$ and $Z_t = \mathbb{E}_B Z_t + o(n)$ with probability $1 - o(1)$. Lemma 1 then gives $|D| \ge (b(\theta, 2) - o(1))n$ for every admissible $D$, with probability $1 - o(1)$. $\square$

Checks of (e): `perm_var_check.py` (exact rational arithmetic, $n = 4, 5, 6$, random $f$) and `switch_check.py` (1500 random switches at $(n, \theta) = (16, 1/4), (24, 0.2), (32, 1/8)$, $t = 1, 2, 3$) found no violation. lattice_lift_research checked all 14,400 ordered pairs of permutations at $n = 5$.

## 5. Proof of Theorem C

Fix $c = 2$ and $\theta \in [0.27, 1/2)$, and let $M = \lfloor 1/\theta \rfloor + 1$ be the cell bound of Lemma 3. Call a set $T$ clean if it has at most two points on every line of $F_\theta$, and let $\mathrm{Free}(T)$ be the set of cells $z \notin T$ such that no line of $F_\theta$ through $z$ holds two points of $T$. Adding a cell of $\mathrm{Free}(T)$ keeps $T$ clean.

**Step 1 (one addition).** If $z \in \mathrm{Free}(T)$ is added, a cell $w \in \mathrm{Free}(T)$ leaves Free only if $w = z$ or $w$ lies on a line of $F_\theta$ through $z$ and some $y \in T$. Let $L_{zy}$ be the number of cells of the line through $z$ and $y$ if that line is in $F_\theta$, and 0 otherwise, and let $B(z, T)$ be the set of such cells $w \ne z, y$. Then
$$|\mathrm{Free}(T + z)| \ge |\mathrm{Free}(T)| - 1 - |B(z, T)|,\qquad |B(z, T)| \le \sum_{y \in T} (L_{zy} - 2)_+ \le (M - 2)|T|.$$
Summing over all cells $z$ and grouping by the line through $y$,
$$\sum_z |B(z, T)| \le \sum_{y \in T} W(y),\qquad W(y) := \sum_{l \in F_\theta,\ l \ni y} (L_l - 1)(L_l - 2).$$

**Step 2 (uniform limit of $W$).** With $\rho = c/n$, $\rho^2 W(y)/2 = \lambda_n(y) := \rho^2 \sum_{l \ni y} \binom{L_l - 1}{2}$. Write the cell as $y = (un, wn)$. By the derivation of (3.2), $\lambda_n(y)$ is $c^2/n^2$ times a count of primitive vectors $(a, b)$ in $O(M^2)$ regions (one box per pair $\{k_1, k_2\}$, minus its part of height $< \theta n$), each of side at most $2n$, whose endpoints are within $O(1)$ of $n$ times the endpoints of $I_a$, $I_b$. A box of side at most $2n$ contains $(6/\pi^2)\cdot\text{area} + O(n \log n)$ primitive vectors. Hence $\sup_y |\lambda_n(y) - \lambda(u, w)| = O_\theta(\log n/n)$, and $\max_y W(y) \le (2n^2/c^2)(\sup \lambda + o(1))$.

**Step 3 (the event $G$).** Fix $\delta > 0$. Let $G$ be the event that
(G1) $|S| \le 3n$; (G2) $|\mathrm{Free}(S)| \ge (f_0 - \delta)n^2$, where $f_0 = \int e^{-\lambda(u,w)}\,du\,dw$;
(G3) $\sum_{y \in S} W(y) \le ((2/c)\,\overline{\lambda} + \delta)n^3$, where $\overline{\lambda} = \int \lambda\,du\,dw$; (G4) $|D^*| \le (A + \delta)n$.
$G$ is determined by $S$, and $\mathbb{P}(G) \to 1$:
(G1) by Chebyshev, since $\mathbb{E}|S| = cn = 2n$ (this step needs $c < 3$).
(G2) The lines of $F_\theta$ through $z$ meet only at $z$, so $\mathbb{P}(z \in \mathrm{Free}(S)) = (1 - \rho)\prod_{l \ni z}(1 - q_l)$ with $q_l = \mathbb{P}(\mathrm{Bin}(L_l - 1, \rho) \ge 2) = O(n^{-2})$. Since $\sum_l q_l = \lambda_n(z) + O(1/n)$ and $\sum_l q_l^2 = O(n^{-2})$, this is $e^{-\lambda(u,w)} + o(1)$ uniformly by Step 2, so $\mathbb{E}|\mathrm{Free}(S)| = (f_0 + o(1))n^2$. Toggling one cell $x$ changes $|\mathrm{Free}(S)|$ by at most $1 + M R'_x$, where $R'_x$ is the number of points of $S \setminus \{x\}$ on lines of $F_\theta$ through $x$. $R'_x$ does not depend on the bit of $x$ and $R'_x \le |S|$, so $\mathbb{E} R_x'^2 = O(n^2)$. Resampling the bit of $x$ changes it with probability $2\rho(1 - \rho)$, independently of $R'_x$, so $\mathbb{E}[(\Delta_x |\mathrm{Free}|)^2] \le 2\rho(1 - \rho)\,\mathbb{E}(1 + M R'_x)^2 = O(n)$, and Efron–Stein over the $n^2$ cells gives $\mathrm{Var}\,|\mathrm{Free}(S)| = O(n^3)$.
(G3) $\mathbb{E}\sum_{y \in S} W(y) = \rho\sum_y W(y) = (2/c)(\overline{\lambda} + o(1))n^3$ by Step 2, and the variance is $\rho(1 - \rho)\sum_y W(y)^2 = O(n^5)$.
(G4) Deleting $X_l - 2$ points from each line $l \in F_\theta$ with $X_l \ge 3$ gives an admissible set, so $|D^*| \le Y$, and $Y = (A + o(1))n$ w.h.p. by Lemmas 4 and 5.
On $G$, for every set $T_i = (S \setminus D^*) \cup \{z_1, \ldots, z_i\}$ with $i \le |D^*|$ and $n$ large,
$$\sum_{y \in T_i} W(y) \le \sum_{y \in S} W(y) + i \max W \le \kappa_\delta n^3,\qquad \kappa_\delta = \tfrac{2}{c}\overline{\lambda} + \delta + (A + \delta)\tfrac{2}{c^2}(\sup\lambda + \delta), \tag{5.1}$$
and $|T_i| \le |S| \le 3n$.

**Step 4 (the refill process).** Condition on the whole of $S$, with $S \in G$, and choose $D^*$ by a fixed tie rule, so that $m$ below is deterministic in the conditional space. Put $T_0 = S \setminus D^*$ and $m = |D^*|$. For $i < m$: if $\mathrm{Free}(T_i) \ne \emptyset$, let $z_{i+1}$ be uniform in $\mathrm{Free}(T_i)$, independent of the past given $T_i$, and $T_{i+1} = T_i + z_{i+1}$; if $\mathrm{Free}(T_i) = \emptyset$, put $T_{i+1} = T_i$ (a stall). Since $T_0 \subseteq S$, $\mathrm{Free}(T_0) \supseteq \mathrm{Free}(S)$. Let $F_i = |\mathrm{Free}(T_i)|/n^2$ and $a = 2\kappa_\delta/n + 2/n^2$. If $F_i > 0$, Step 1 and (5.1) give
$$\mathbb{E}[F_{i+1} - F_i \mid T_i] \ge -\frac{1}{n^2}\Big(1 + \frac{\sum_z |B(z, T_i)|}{|\mathrm{Free}(T_i)|}\Big) \ge -\frac{1}{n^2} - \frac{\kappa_\delta}{n F_i},$$
and since $F_{i+1}^2 - F_i^2 \ge 2F_i(F_{i+1} - F_i)$, $\mathbb{E}[F_{i+1}^2 - F_i^2 \mid T_i] \ge -a$. If $F_i = 0$ the increment is 0. Hence $Q_i = F_i^2 + a i$ is a submartingale for $i \le m$; no stopping level is needed. Since $|T_i| \le 3n$, $|F_{i+1} - F_i| \le (1 + 3(M - 2)n)/n^2 \le 3M/n$, so $|Q_{i+1} - Q_i| \le C/n$ with $C = 6M + 2\kappa_\delta + 1$. The Azuma–Hoeffding inequality for submartingales gives, for each $i \le m \le |S| \le 3n$,
$$\mathbb{P}(Q_i \le Q_0 - n^{-1/4}) \le \exp\Big(-\frac{n^{-1/2}}{2iC^2/n^2}\Big) \le \exp\Big(-\frac{n^{1/2}}{6C^2}\Big),$$
with a constant uniform over $S \in G$, and a union bound over $i \le 3n$ shows that w.h.p., for all $i \le m$,
$$F_i^2 \ge F_0^2 - am - n^{-1/4} \ge (f_0 - \delta)^2 - 2\kappa_\delta(A + \delta) - o(1).$$
Let $\kappa = (2/c)\overline{\lambda} + A(2/c^2)\sup\lambda$. If $f_0^2 > 2\kappa A$, choose $\delta > 0$ so that the right side is at least a constant $\varepsilon > 0$. Then $F_i > 0$ for all $i < m$, the process never stalls, and $T_m$ is clean on $F_\theta$, contains $S \setminus D^*$, and has $|S| - m + m = |S|$ points. Since $\mathbb{P}(G) \to 1$, Theorem C holds at every $\theta$ with $f_0^2 > 2\kappa A$.

**Step 5 (the criterion, certified).** As $\theta$ grows, $F_\theta$ shrinks, so $\lambda(u, w; \theta)$ decreases pointwise (the integrand in Lemma 5 is nonnegative), and $A(\theta)$ decreases (it is the integral of $G \ge 0$ over a shrinking region). Hence $\overline{\lambda}$, $\sup\lambda$, $A$ and $\kappa$ decrease and $f_0$ increases, so $f_0^2 - 2\kappa A$ is nondecreasing in $\theta$, and it suffices to certify the criterion at $\theta = 0.27$.
For the certificate (`lam_enclose.py`), split $[0, 1]^2$ into a $320 \times 320$ grid of boxes. Each term of (3.2) is the area of $(I_a \times I_b) \setminus ((0, \theta) \times (-\theta, \theta))$, which is monotone under inclusion of $I_a \times I_b$. The endpoints $a_k, l_k, h_k$ are monotone in $u$ or $w$, so on a grid box the intervals evaluated at the corners give an inner and an outer box, hence lower and upper bounds $\lambda^-, \lambda^+$ for $\lambda$ on the grid box. All arithmetic is in exact rationals; $6/\pi^2$ is bounded using $9.8696044 < \pi^2 < 9.8696045$, and $e^{-x}$ by alternating Taylor partial sums. This gives $\sup\lambda \le \max\lambda^+$, $\overline{\lambda} \le \text{average of } \lambda^+$, $f_0 \ge \text{average of a lower bound for } e^{-\lambda^+}$, and $A$ from the finite sum (3.1). At $\theta = 0.27$:
$$\sup\lambda \in [0.846160,\ 0.861311],\quad \overline{\lambda} \le 0.408430,\quad f_0 \ge 0.667903,\quad A \le 0.268367,$$
$$f_0^2 \ge 0.446094 > 0.281250 \ge 2\kappa A.$$
The upper end $0.861311$ equals the centre value $(24/\pi^2)(1/2 - 2\theta^2)$ pointed out by the referee. At $\theta = 0.3$ the same code gives $0.565012 > 0.137717$. At $\theta = 1/4$ the certified bounds ($f_0^2 \ge 0.369$, $2\kappa A \le 0.435$) do not decide the criterion, and midpoint-grid estimates ($0.374$ against $0.426$) indicate that it fails there.

## 6. Numerical checks

Code, data and per-sample logs are in the supplement. Samples use Python's `random.Random(1000n + s)` for sample $s = 0, 1, \ldots$; every log records $n$, $s$ and the solver status (two older scripts use other seed rules, listed in the supplement README). All results in this section are finite-$n$ computations. They illustrate the theorems and do not prove asymptotic statements.

**(a) Finite-$n$ bound, model A, $c = 2$.** The value $\max_t (\mathbb{E} Y - \mathbb{E} Z_t)/(tn)$ from Lemma 2, at each $n$. $\mathbb{E} Y$ is a finite sum of binomial tails. For $\mathbb{E} Z_t$ we use $\mathbb{E}(R - t)_+ = \mathbb{E} R - t + \sum_{j<t} (t - j)\,\mathbb{P}(R = j)$, where $\mathbb{E} R = \sum_l q_l$ and $\mathbb{P}(R = j)$ for $j < t$ comes from the exact Poisson-binomial recursion over the lines through the cell. Nothing is truncated; arithmetic is in double precision (`trunc_exact.py`).

| $\theta$ | 0.05 | 0.10 | 0.15 | 0.20 | 0.25 | 0.30 |
|---|---|---|---|---|---|---|
| $n = 60$ | 0.391 | 0.318 | 0.266 | 0.212 | 0.157 | 0.113 |
| $n = 120$ | – | 0.314 | – | 0.210 | 0.150 | – |

At $n = 240$ and $\theta = 0.25$ the value is 0.1488. The limit satisfies $b(1/4, 2) \ge 0.147087$ (certified as in Section 5, Step 5).

**(b) Exact minimum $|D^*|/n$ on model B samples.** HiGHS integer program with relative gap 0; all 60 runs returned status optimal with gap 0 (`tail_seeded.py`). Five samples per cell; mean, with the sample standard deviation in brackets:

| $\theta$ | 0.05 | 0.10 | 0.15 | 0.20 | 0.25 | 0.30 |
|---|---|---|---|---|---|---|
| $n = 60$ | 0.693 (0.038) | 0.497 (0.036) | 0.377 (0.037) | 0.270 (0.030) | 0.213 (0.038) | 0.143 (0.025) |
| $n = 120$ | 0.658 (0.016) | 0.493 (0.011) | 0.373 (0.022) | 0.270 (0.021) | 0.200 (0.020) | 0.132 (0.016) |

Per-sample minima are in `tail_seeded_n60.txt` and `tail_seeded_n120.txt` (for example $\theta = 0.25$, $n = 120$: 27, 25, 21, 22, 25).

On 30 paired samples at $n = 40$ and 10 at $n = 60$ (seeds 40 and 60 recorded), the samplewise bound $(Y - Z_t)/t$ never exceeded the integer-program minimum. The mean ratio of bound to minimum was between 0.60 and 0.90, depending on $\theta$.

**(c) Density.** At $n = 60$ (model A, finite-$n$ bound of (a)), $b(0.10)$ and $b(0.25)$ are 0.086 and 0.036 at $c = 1.0$, 0.189 and 0.087 at $c = 1.5$, and 0.318 and 0.157 at $c = 2$ (`density_exact_n60.txt`, untruncated method of (a)).

**(d) Inputs already capped at low heights.** We built sets by random greedy insertion with at most two points on every line of height $< \theta n$, then computed the exact minimum deletion on lines of height $\ge \theta n$. At $\theta = 0.25$ and $n = 60$ the samplewise bound of Lemma 1 on these sets averaged $0.100n$ at density 1.51 per row. For comparison, the expectation bound of (a) in model A at density 1.5 is $0.087n$. These are two different quantities in two different models, and we do not infer an ordering of deletion costs from them. Greedy insertion followed by optimal deletion kept at most $1.483n$ points in these samples ($n = 40$ and 60, `hl_n40.txt`, `hl_n60.txt`).

**(e) Refill (empirical).** On model B samples we constrained only lines of height $\ge H$. We ran greedy deletion, then one refill pass: the cells in (deficient row) $\times$ (deficient column) were visited in random order, and a cell was added if no constrained line through it held two points. Rows and columns keep at most two points. Mean deletion$/n$ and mean net loss$/n$ after refill, with the sample standard deviation of loss$/n$ in brackets (5, 5, 3 and 2 samples at $n = 60, 120, 240, 480$; `xchg_ps.py`, per-sample values in `xps_n*.txt`):

| $H$ | $n = 60$ | $n = 120$ | $n = 240$ | $n = 480$ |
|---|---|---|---|---|
| $n/4$ | 0.22 / 0.023 (0.009) | 0.20 / 0.008 (0.006) | 0.20 / 0.006 (0.002) | 0.22 / 0.001 (0.002) |
| $n/8$ | 0.45 / 0.063 (0.022) | 0.47 / 0.042 (0.017) | 0.46 / 0.035 (0.006) | 0.48 / 0.019 (0.000) |
| $n/16$ | 0.68 / 0.243 (0.022) | 0.65 / 0.143 (0.016) | 0.66 / 0.097 (0.017) | 0.67 / 0.081 (0.003) |

At $H = n/4$ the per-sample losses in points are 1, 2, 1, 1, 2 ($n = 60$); 2, 1, 1, 0, 1 ($n = 120$); 2, 1, 1 ($n = 240$); 1, 0 ($n = 480$). These finite observations are consistent with an $o(n)$ loss at fixed $H/n$ but do not establish it, and the samples at $n = 240$ and 480 are few. A heuristic: a fresh cell is free with probability about $e^{-\lambda}$ (mean $\lambda$ about 0.4 to 0.5 near $\theta = 1/4$). If $r$ rows and $r$ columns stay deficient, all $r^2$ cells between them must be blocked, which is unlikely under independent blocking once $r$ is much larger than $(\log n)e^{\lambda}$. Blocking is not independent, so this is not a proof.

**(f) Low heights (empirical).** In the opposite direction we constrained only non-axial lines of height $< n/4$. After greedy deletion and refill the net loss$/n$ was 0.48, 0.52 and 0.54 at $n = 60, 120, 240$. To check whether this is an artefact of the greedy repair, we then re-solved blocks of $r$ consecutive rows exactly (HiGHS maximum integer program over the free rows with the rest frozen, blocks slid by $r/2$ until no change; every solve optimal). Net loss$/n$ after block re-solve:

| | refill | $r = 2$ | $r = 4$ | $r = 8$ |
|---|---|---|---|---|
| $n = 60$ (3 samples) | 0.483 | 0.472 | 0.422 | 0.383 |
| $n = 120$ (2 samples) | 0.512 | 0.504 | 0.483 | – |

Per-sample values at $r = 8$, $n = 60$ are 0.400, 0.383 and 0.367 (`blk_n60.txt`, `blk_n120.txt`). In these samples a loss of at least $0.36n$ remains after exact repair of blocks of up to 8 rows. We read this only as evidence that, at these sizes, local repair from a random start does not remove the low-height cost. It says nothing about the optimum of this constrained problem: every no-three-in-line set with two points per row and column satisfies the constraints, so the optimal loss is at most $2n$ minus the largest such set.

## 7. Scope and remarks

- **Deletion only.** Theorems A and B bound deletions from a fixed sample. Theorem C shows that, for $\theta \ge 0.27$ in model A, refilling removes the cost without row or column control. Section 6(e) is consistent with a small refill cost at $\theta = 1/4$ under row and column caps, at the sizes tested. The results concern the crude deletion step of the heavy/light method, not the light lines as such.
- **Below the band.** The empirical results of Section 6(f) suggest that the cost moves to lines of height below $\theta n$ under refill. These are losses of repair from a random start; the optimum is at most $2n$ minus the largest no-three-in-line set. We prove no lower bound there. The supersaturation estimate [2, (19)] uses only directions of height between $\lceil 1/u \rceil \ge 2$ and $un/12 < n/4$, so we expect the argument of [2] to bound subsets of $S$ in model B that are clean on non-axial lines of height $< n/4$. We have not checked its remaining steps for this restricted constraint.
- **Mixed triples.** If $S$ is added to a fixed structured set $T$, triples with two points of $T$ cost the points of $S$ on cells blocked by lines through two points of $T$. A bound valid for every $T$ gives only $\Omega(\log n)$ such points, because $T$ has at most two points on each line, so each line carries at most one pair of $T$. A linear statement would need information on how these lines spread, which this note does not have.
- **Small $\theta$.** Lemma 1 does not give a cost near $2n$ as $\theta \to 0$. Midpoint-grid values (not certified) are $b(\theta, 2) \approx 0.371, 0.415, 0.436$ at $\theta = 0.05, 0.02, 0.01$, with shrinking increments; the all-direction bound of [2] uses the $\log n$ supersaturation that this first-moment method does not see.
- **Review status of Section 5.** lattice_lift_research read Steps 3–4 and found the implication $f_0^2 > 2\kappa A \Rightarrow$ refill without a stall sound for model A at fixed $\theta$ and $c < 3$, given Steps 1–2 and Lemmas 4–5. She did not check Steps 1–2 or the enclosure numbers of Step 5. Her corrections (the resampling factor in (G2), a fixed tie rule for $D^*$, $c < 3$ in (G1), the union over $3n$) are included.
- **Constants.** The values of $b$ are lower bounds. In the samples of Section 6(b), the exact minimum is 1.1–1.8 times larger.
- **Not covered.** Deterministic or conditioned sets, outputs of pseudorandom matchings (including the correlated matching output of [1]), and the threshold of Theorem C between $1/4$ and $0.27$.
- **Guy–Kelly.** The first-moment heuristic of [3] gives $\pi/\sqrt{3} \approx 1.814$ for the whole problem. This note bounds only the cost of the light part in random models and says nothing about the existence of no-three-in-line sets above $1.8n$.

## References

[1] A. Ghosal, R. Goenka, A. Grebennikov, P. Keevash, M. Kwan and H. T. Pham, No-$(k+1)$-in-line problem for $k \ge 3$, arXiv:2607.05255v1 (2026), Section 1.3 and Remark 1.7.

[2] Quarter-turn relaxation gaps and sublinear deletion optima in random grid supports, rStation `no_three_in_line_4`, version 3 (4 October 2026), Section 11 and Theorem 16.

[3] R. K. Guy and P. A. Kelly, The no-three-in-line problem, Canad. Math. Bull. 11 (1968), 527–531.

[4] R. R. Hall, T. H. Jackson, A. Sudbery and K. Wild, Some advances in the no-three-in-line problem, J. Combin. Theory Ser. A 18 (1975), 336–341.
