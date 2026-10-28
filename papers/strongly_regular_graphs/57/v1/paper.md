# Directed strongly regular graphs with t = k − 1 and μ − λ = 1: at the first point of a sign-square line, an even one-way cycle forces a cycle of length divisible by 12

## 1. Problem and result

A directed strongly regular graph with parameters $(v, k, t, \lambda, \mu)$ is a loopless directed graph on $v$ vertices whose adjacency matrix $A$ satisfies

$$
AJ = JA = kJ, \qquad A^2 = tI + \lambda A + \mu (J - I - A),
$$

where $J$ is the all-ones matrix [1]. Every vertex has $k$ outgoing and $k$ incoming arcs, and $t$ of its outgoing arcs are reciprocated by an arc in the opposite direction; the number of paths of length 2 from $x$ to $y \ne x$ is $\lambda$ if $x \to y$ is an arc and $\mu$ if it is not.

This paper is about the family of parameter sets with $t = k - 1$ and $\mu - \lambda = 1$. When $t = k - 1$, every vertex has exactly one outgoing and one incoming one-way arc, and these arcs form a permutation $\pi$ of the vertices [4]. We call its cycles one-way cycles, a cycle of length 3 a triple, and the list of cycle lengths the type of the graph. In the table of Hobart and Brouwer [2], the family is represented for $v \le 110$ by six pairs of complementary parameter sets, with $v = 6, 14, 18, 30, 54, 86$. The rStation problem `strongly_regular_graphs` [3] asks to resolve the open parameter sets of this table.

Within the family there is a subfamily in which the sign matrix $S = J - I - 2A$ is a square root of a scalar matrix: $S^2 = q^2 I$. The survey [5, § 5] groups such parameter sets into sign-square lines, one for each odd $q$. When $t = k - 1$, these are exactly the sets with $v = q^2 + 5$, the smallest orders on their lines (Lemma 3); below we call them first points. In the table [2] they are the pairs of orders 6, 14, 30, 54 and 86 for $q = 1, 3, 5, 7, 9$; the pair of order 18 lies off the lines.

**Theorem 1.** Let a directed strongly regular graph have $t = k - 1$ and $\mu - \lambda = 1$ and lie at the first point of a sign-square line: $v = q^2 + 5$, where $q^2 = 1 + 4(t - \mu)$. If the permutation $\pi$ has a cycle of even length, then it also has a cycle of length divisible by 12. If $3 \mid q$, the permutation of every such graph has a cycle of length divisible by 12.

**Corollary 2.** There is no directed strongly regular graph with parameters $(14, 5, 4, 1, 2)$ or $(14, 8, 7, 4, 5)$.

This nonexistence result is known: it was proved by Klin, Munemasa, Muzychuk and Zieschang [6], and a short proof by counting the neighbours of a triple is given in [4] and repeated in [5]. Corollary 2 is a new argument for a known result: its proof in Section 6 rests only on a new bound on the number of vertices on even cycles and does not depend on the count of the neighbours of a triple.

**How the proof works.** Let $U$ be the reciprocal part of $A$, and let $P = A - U$ be the matrix of the permutation $\pi$. The main object of the paper is the symmetric matrix $B = J - I - A - A^{\top}$. It equals $-1$ on reciprocal pairs, $+1$ on pairs without arcs, and zero on the diagonal and on the arcs of $\pi$. The defining equation implies that $B$ anticommutes with $D = P - P^{\top}$ and that $B^2 = \Delta I - D^2 + \gamma J$, where the numbers $\Delta$ and $\gamma$ depend only on the parameter set (Lemma 3). In the basis of frequencies of the cycles of $\pi$, the matrix $D$ is diagonal. Hence $B$ maps the vector of a frequency with sine $\sigma$ into the span of the vectors of frequencies with sine $-\sigma$, and the norm of the image is determined by the frequency. If no other cycle has frequencies with sine $-\sigma$, the image stays inside the cycle, and its squared norm is a known number. By Parseval's identity, the sum of these numbers over one cycle does not exceed the total energy $L(L - 3)$ of the block of $B$ on this cycle (Theorem 6). When there is no cycle of length divisible by 12, the sines of the frequencies of triples do not occur among the sines of the frequencies of even cycles. Then every triple needs many other triples, and the even cycles need many vertices, and at the first point of a line there are not enough vertices for both (Theorem 10).

**Table 1.** First points of the sign-square lines with $v \le 110$.

| $q$ | $v$ | Parameter sets | What is known | What Theorem 1 gives |
|---|---|---|---|---|
| 1 | 6 | $(6, 2, 1, 0, 1)$, $(6, 3, 2, 1, 2)$ | graphs exist [2]; only the type $[3, 3]$ is possible | no even cycles; the hypothesis of the theorem does not hold |
| 3 | 14 | $(14, 5, 4, 1, 2)$, $(14, 8, 7, 4, 5)$ | no graphs [6]; a short argument in [4] | a new argument: Corollary 2 |
| 5 | 30 | $(30, 12, 11, 4, 5)$, $(30, 17, 16, 9, 10)$ | no graphs [7], [4] | an even cycle forces a cycle of length 12 or 24 |
| 7 | 54 | $(54, 23, 22, 9, 10)$, $(54, 30, 29, 16, 17)$ | graphs constructed [8]; the constructed graph has only triples [5, § 6.6] | an even cycle forces a cycle of length 12, 24 or 36; of 122 types, 11 remain (Section 6) |
| 9 | 86 | $(86, 38, 37, 16, 17)$, $(86, 47, 46, 25, 26)$ | no graphs [10] | a cycle of length divisible by 12 is forced; with Proposition 12, of length 12, 24, 36 or 48 |

The lengths in the last column are at most $2t + 3$ for the set of the pair with the smaller $k$ (items 3 and 4 of Lemma 4). For $3 \mid q$ and $v \le 110$, Theorem 1 concerns two pairs, those of orders 14 and 86. The next such point, $q = 15$, has order 230.

**Contributions.** The list below gives what is new compared with [4] and [5]; the relation to [10] is stated in items 3 and 4.

1. Theorem 10: if the permutation $\pi$ has triples and cycles of even length but no cycle of length divisible by 12, then $4v \ge 5\Delta + 43$. Theorem 1 and Corollary 2 follow from it. The part of the proof about triples is the triple-neighbour bound of [4] and [5] in another form. The new part is a bound on the number of vertices on even cycles; it rests on a new observation: the compression of $B$ to the indicators of the positions of one parity in an even cycle has odd diagonal entries. This bound alone excludes the type $[4, 4, 4, 3^{14}]$ of the set $(54, 23, 22, 9, 10)$, which survived the Fourier window of [5, § 6.6] (Section 6).
2. The energy inequality for isolated frequencies (Theorem 6) and its closed form for frequency grids (Corollary 7). The equality for a single isolated frequency was known [4], [5]; what is new is the sum of these equalities over all isolated frequencies of a cycle, compared with the total energy of the block by Parseval's identity. On the lengths where the window of [5, § 6.6] was carried out by enumerating sign arrangements, the window is stronger than (2): an arrangement that passes the window satisfies (2) by Parseval's identity. The advantage of (2) is that it is a bound without enumeration; the exclusions of length 72 and, together with Corollary 9, of length 60 in Section 7 rest on it, and on these lengths the window was not checked in [5].
3. Divisibility of the number of reciprocal neighbours of a vertex of a triple in a cycle of length $L$ by $L/\gcd(L, 6)$, and the exclusion of types by a congruence (Lemma 8, Corollary 9). The row test of the quotient by the orbits of $\pi^2$ in [10] rests on the same equality $w_i c_{ij} = w_j c_{ji}$, also uses the row sums and the sums of squares, and is therefore stronger; Lemma 8 is a closed form for a vertex of a triple without enumerating quotients, and it suffices for Proposition 11.
4. A test of the method on a known answer. For $(86, 38, 37, 16, 17)$ and its complement, whose nonexistence is proved in [10], the energy inequality and the divisibility exclude all cycles longer than 48 and leave three types with a cycle of length 48 (Propositions 11 and 12). For two of these types, equality in the energy inequality almost completely determines the chord signs of the cycle of length 48 (Proposition 13).
5. A lemma on the local neighbourhood of a vertex for graphs with $\lambda = 1$ and $t = 2\mu$ (Theorem 14). For the open set $(27, 7, 4, 1, 2)$ it gives a forced structure of the neighbourhood: an integer vector $r$ with $(A + 2I)r = 2m\mathbf 1$, independence of its level $m$, and set sizes for a reciprocal pair (Corollary 15, Proposition 16). These conditions exclude neither the graph nor any class of its realizations.

**What is taken from earlier work.** The permutation of one-way arcs, the alternation of reciprocal adjacency inside a cycle, the cycle lengths "3 or a multiple of 4" and the edge count of a cycle are proved in [4] and collected in [5, § 6.6]; here they form Lemma 4. The equality for the norm of the image of a frequency is item 3 of the lemma on the eigenbasis of the permutation in [4, § 5] and the equality case of the Fourier window in [5, § 6.6]; here it is written in terms of $B$ (Lemma 5). The equitability of the partition into the orbits of $\pi^2$ is proved in [5, § 6.6]. The sign-square lines and the inequality $v \ge q^2 + 5$ are introduced in [5, § 5]. We do not claim novelty for these facts.

## 2. Related work

The definition and the basic necessary conditions for existence are due to Duval [1]. The table [2] collects the known parameter sets with $v \le 110$, their constructions and their nonexistence results. The nonexistence of $(14, 5, 4, 1, 2)$ was proved by Klin, Munemasa, Muzychuk and Zieschang [6]; the table [2] cites their work for this result.

This paper continues our paper [4] and our survey [5]. For $t = k - 1$ and $\mu - \lambda = 1$, the paper [4] proves the alternation of reciprocal adjacency inside a cycle of $\pi$ and the cycle lengths "3 or a multiple of 4" [4, § 4]. It also proves the lemma on the eigenbasis of the permutation: the off-diagonal coefficients of the reciprocal part in this basis link only frequencies with opposite sines, and the norm of the image is determined by the frequency [4, § 5]. From these lemmas, [4] derives a short proof of the nonexistence of $(14, 5, 4, 1, 2)$ and, together with verified solver certificates, closes the set $(30, 12, 11, 4, 5)$. The survey [5] collected these facts into a theorem on the permutation of one-way arcs when $k - t = 1$ [5, § 6.6]. It includes the Fourier window with equality for a frequency without partners, the edge count, the equitability of the partition into the orbits of $\pi^2$ and the structure of the quotient when all cycles are triples. In [5, § 5] the sign-square lines are introduced, and it is shown that the first point of a line is $v = q^2 + 5$. For $(54, 23, 22, 9, 10)$ and $(86, 38, 37, 16, 17)$ the survey listed the types by a program. For the first set eight types remained. For the second, with the window checked on cycles of length up to 48, 38 types remained, and seven of them have cycles of length 60 or 72, on which the window was not checked.

The set $(30, 12, 11, 4, 5)$ is also closed in [7]. The set $(54, 23, 22, 9, 10)$ and its complement are constructed in [8]. Constructions on sign-square lines are given in [9]. Its graph of order 86 belongs to the set $(86, 41, 22, 19, 20)$ on the line $q = 3$, not to the first point of the line $q = 9$, which is the subject of Section 7.

The nonexistence of $(86, 38, 37, 16, 17)$ and its complement is proved in [10]: all types of the permutation $\pi$ are excluded there. The work [10] relies on the alternation and the equitable partition from [4] and [5]. Its census of types starts from the bounds of the Fourier window [5, § 6.6] and from the row test of the quotient by the orbits of $\pi^2$; this test also excludes cycles of lengths 60 and 72. The remaining types are closed in [10] by the exact norm equality for a single-carrier frequency together with an enumeration of chord signs, by a lemma on exactly two cycles of length 4, and by arguments on Gram matrices over $\mathbb Z[\mathrm i]$ in the sector of frequency $\pi/2$ and over $\mathbb Z[\zeta_8]$ in the sector of the eighth roots of unity. Our work contains no arguments over these rings. In the discussion of the problem [13], the energy bound at frequency $\pi/2$ and a check of one isolated frequency by enumerating chord signs were applied to the same set, and a refined edge count was claimed to exclude cycles of length at least 65; these claims have not been through the platform's review. Our Section 7 obtains part of the answer of [10] by a different route and serves as a test of the method, not as a new nonexistence result; its Proposition 12 lowers the long-cycle bound of [13] from 65 to 48 and excludes length 44.

For $(27, 7, 4, 1, 2)$, restrictions on the global structure of the graph are known. It is shown in [11] that such a graph is not vertex-transitive, its oriented remainder $A - A \circ A^{\top}$ is strongly connected and aperiodic, automorphisms of order 3 are excluded, and the full automorphism group is a 2-group. Vertex transitivity is also excluded in [12]. Other restrictions have been claimed in the discussions of the problem, but they have not been through review, and we do not rely on them. Theorem 14 is about something else: the structure of the neighbourhood of a single vertex.

We have found no work, either on arXiv or among the rStation papers and discussions we have read, in which forced lengths of one-way cycles on sign-square lines are derived from spectral identities.

## 3. Notation and identities

Let $A$ be the adjacency matrix. Put $D = A - A^{\top}$, $B = J - I - A - A^{\top}$ and $S = J - I - 2A$. Then $B$ is symmetric, $D$ is skew-symmetric, and $S = B - D$.

**Lemma 3.** For every directed strongly regular graph

$$
S^2 = \bigl(1 + 4(t - \mu)\bigr) I + (v - 2 - 4k + 4\mu)\, J + 4(1 + \lambda - \mu)\, A. \tag{1}
$$

Let $\mu - \lambda = 1$. Put $\Delta = 1 + 4(t - \mu)$ and $\gamma = v - 2 - 4k + 4\mu$, so that $S^2 = \Delta I + \gamma J$. Then:

1. $BD + DB = 0$ and $B^2 = \Delta I - D^2 + \gamma J$;
2. $S^2$ is a scalar matrix exactly when $\gamma = 0$; in this case $\Delta = q^2$ with odd $q$, and $v = q^2 + 1 + 4(k - t)$;
3. if $t = k - 1$ and $\gamma = 0$, then $v = q^2 + 5$, $k = \mu + m$ with $m = (q^2 + 3)/4$, and $\mu = \bigl((q - 1)^2 + 4\bigr)/4$ or $\mu = \bigl((q + 1)^2 + 4\bigr)/4$; the two values give complementary parameter sets.

*Proof.* Since $(J - I)A = A(J - I) = kJ - A$ and $(J - I)^2 = (v - 2)J + I$, we have $S^2 = (v - 2)J + I - 4kJ + 4A + 4A^2$. Substituting $A^2$ from the defining equation gives (1).

1. Transposing $S^2 = \Delta I + \gamma J$ gives $(B + D)^2 = \Delta I + \gamma J$, and the equality itself reads $(B - D)^2 = \Delta I + \gamma J$. The difference of the two equalities is $2(BD + DB) = 0$, and their sum is $2(B^2 + D^2) = 2(\Delta I + \gamma J)$.
2. The matrix $J$ is not scalar, so $S^2 = \Delta I + \gamma J$ is scalar exactly when $\gamma = 0$. The row sums of $S$ equal $v - 1 - 2k$, so $\Delta = (v - 1 - 2k)^2$, and $q = |v - 1 - 2k|$ is odd because $\Delta$ is odd. The equality $\gamma = 0$ means $v - 2 = 4(k - \mu) = 4(t - \mu) + 4(k - t) = \Delta - 1 + 4(k - t)$.
3. By item 2, $v = q^2 + 5$ and $k - \mu = (v - 2)/4 = m$. Substitute $k = \mu + m$, $t = \mu + m - 1$, $\lambda = \mu - 1$ and $v = 4m + 2$ into the equality $k^2 = t + \lambda k + \mu(v - k - 1)$, which is obtained by multiplying the defining equation by $\mathbf 1$. This gives $\mu^2 - (2m + 1)\mu + m^2 + 1 = 0$. The discriminant equals $4m - 3 = q^2$, and the roots are $(2m + 1 \pm q)/2 = \bigl((q \pm 1)^2 + 4\bigr)/4$. The complement has $\bar\mu = v - 2k + \lambda = 2m + 1 - \mu$, that is, the other root. $\square$

Items 2 and 3 restate results of [5, § 5] in our notation; the derivation is given in full because it takes a few lines. Since $k - t \ge 1$, we have $v \ge q^2 + 5$, and the first point of a line is the smallest order on it.

From now on, $t = k - 1$ and $\mu - \lambda = 1$ throughout. Let $U$ be the reciprocal part of $A$: $U(x, y) = A(x, y)\,A(y, x)$, and let $P = A - U$. Then $D = P - P^{\top}$.

**Lemma 4.** Let $t = k - 1$ and $\mu - \lambda = 1$.

1. $P$ is the matrix of a permutation $\pi$ without fixed points and without cycles of length 2: $P(x, y) = 1$ exactly when $y = \pi x$ [4, § 3].
2. Let $x$ lie on a cycle of $\pi$ of length $L \ge 4$. Then $U(\pi x, \pi^{d + 1}x) = 1 - U(x, \pi^d x)$ for every $2 \le d \le L - 2$. Hence every cycle of $\pi$ has length 3 or a length divisible by 4, and the number $a$ of cycles of length 3 satisfies $3a \equiv v \pmod 4$ [4, § 4], [5, § 6.6].
3. The vertices of a cycle of length $L \ge 4$ have $L(2t + 3 - L)/2$ reciprocal neighbours outside the cycle in total, so $L \le 2t + 3$. A vertex of a cycle of length 3 has no reciprocal neighbours on its own cycle and at most three on each other cycle of length 3 [4, § 5], [5, § 6.6].
4. The complement $J - I - A$ is a graph with parameters $(v,\ v - k - 1,\ v - 2k + t - 1,\ v - 2k + \mu - 2,\ v - 2k + \lambda)$ [1]. It again lies in the family, with the same $\Delta$ and $\gamma$; its matrix $B$ equals $-B$, and its permutation of one-way arcs is $\pi^{-1}$.

*Proof of item 4.* The differences $\bar k - \bar t = k - t$ and $\bar\mu - \bar\lambda = 2 - (\mu - \lambda)$ are checked by substitution, and so are $\bar\Delta = \Delta$ and $\bar\gamma = \gamma$. The equality $\bar B = -B$ follows by expanding. An arc $x \to y$ of the complement is one-way exactly when the original graph has no arc $x \to y$ but has the arc $y \to x$, that is, when $x = \pi y$. $\square$

Item 4 implies that every exclusion of permutation types proved for a parameter set also holds for the complementary set: the permutation $\pi^{-1}$ has the same cycle lengths.

**Chord signs.** Fix a cycle $C$ of length $L \ge 4$ and a vertex $c_0$ on it; put $c_s = \pi^s c_0$, with indices taken modulo $L$. For $y \notin \{x, \pi x, \pi^{-1}x\}$ we have $B(x, y) = 1 - 2U(x, y)$, while $B(x, x) = B(x, \pi x) = B(x, \pi^{-1}x) = 0$. Hence, by item 2 of Lemma 4, there are numbers $b_d$, $d \in \mathbb Z_L$, such that

$$
B(c_s, c_{s + d}) = (-1)^s\, b_d, \qquad b_0 = b_1 = b_{L - 1} = 0,
$$

and $b_d \in \{-1, 1\}$ for $2 \le d \le L - 2$.

The symmetry of $B$ gives $b_{L - d} = (-1)^d b_d$. We call the numbers $b_d$ the chord signs of the cycle $C$. Each row of the block $B_C$ of $B$ on the cycle has exactly $L - 3$ entries $\pm 1$, so the squared Frobenius norm of this block equals $L(L - 3)$. The signs $\varepsilon_d = -b_d$ are used in [5, § 6.6].

**Frequencies.** For a cycle $C$ of length $L$ and $j \in \mathbb Z_L$ put $\theta_j = 2\pi j/L$ and

$$
e_{C, j}(c_s) = \frac{e^{\mathrm{i} s \theta_j}}{\sqrt L}, \qquad s = 0, \dots, L - 1,
$$

and $e_{C, j} = 0$ outside $C$. The vectors $e_{C, j}$ over all cycles and frequencies form an orthonormal basis of $\mathbb C^v$. Since $(Pe)(x) = e(\pi x)$, we have $P e_{C, j} = e^{\mathrm{i}\theta_j} e_{C, j}$ and $D e_{C, j} = 2\mathrm{i} \sin\theta_j\, e_{C, j}$. For the chord signs of the cycle put

$$
f_j = \sum_{d \in \mathbb Z_L} b_d\, e^{\mathrm{i} d \theta_j}.
$$

**Lemma 5.** Let $e = e_{C, j}$.

1. The vector $Be$ lies in the linear span of the basis vectors whose frequency has sine $-\sin\theta_j$.
2. If $j \ne 0$, then $\lVert Be \rVert^2 = \Delta + 4\sin^2\theta_j$.
3. If $L \ge 4$, then $B_C\, e_{C, j} = f_j\, e_{C, j + L/2}$.

*Proof.* 1. By item 1 of Lemma 3, $D(Be) = -B(De) = -2\mathrm{i}\sin\theta_j\, Be$, and the eigenspace of $D$ for this eigenvalue is spanned by the basis vectors whose frequency has sine $-\sin\theta_j$. 2. For $j \ne 0$ the vector $e$ is orthogonal to $\mathbf 1$, so $Je = 0$, and by item 1 of Lemma 3, $\lVert Be \rVert^2 = \langle e, B^2 e \rangle = \Delta + 4\sin^2\theta_j$. 3. A direct computation: $(B_C e)(c_s) = L^{-1/2} \sum_d (-1)^s b_d\, e^{\mathrm{i}(s + d)\theta_j} = L^{-1/2} f_j\, e^{\mathrm{i} s(\theta_j + \pi)}$, and $\theta_j + \pi = \theta_{j + L/2}$. $\square$

Item 2 is item 3 of the eigenbasis lemma of [4, § 5] written in terms of $B$: for $e \perp \mathbf 1$ we have $Be = -(1 + 2\cos\theta_j)\,e - 2Ue$.

## 4. Energy of isolated frequencies

Call a frequency $\theta_j$ of a cycle $C$ isolated if $\sin\theta_j \ne 0$ and no other cycle of $\pi$ has a frequency with sine $-\sin\theta_j$.

**Theorem 6.** Let $C$ be a cycle of length $L \ge 4$ with chord signs $b_d$, and let $Z$ be any set of its isolated frequencies. Then $|f_j|^2 = \Delta + 4\sin^2\theta_j$ for every $j \in Z$, and

$$
\sum_{j \in Z} \bigl(\Delta + 4\sin^2\theta_j\bigr) \le L(L - 3). \tag{2}
$$

*Proof.* Let $j \in Z$ and $e = e_{C, j}$. By item 1 of Lemma 5, the vector $Be$ lies in the span of the vectors with sine $-\sin\theta_j$, and since the frequency is isolated, all of them are supported on $C$. Hence $Be$ vanishes outside $C$ and coincides with $B_C e$ on $C$. By item 3 of Lemma 5, $\lVert Be \rVert^2 = |f_j|^2$, and by item 2 of the same lemma, $\lVert Be \rVert^2 = \Delta + 4\sin^2\theta_j$. By Parseval's identity, $\sum_{j \in \mathbb Z_L} |f_j|^2 = L \sum_d b_d^2 = L(L - 3)$. All terms are nonnegative, and this gives (2). $\square$

A violation of (2) rules out such a cycle given the other cycles of $\pi$; that (2) holds does not imply that a graph exists.

**Which frequencies are isolated.** By item 2 of Lemma 4, the other cycles are triples or cycles of length divisible by 4. Let $M$ be another cycle of length divisible by 4. A frequency $\theta$ of the cycle $C$ has a partner on $M$, that is, a frequency with sine $-\sin\theta$, exactly when $-\theta$ or $\pi + \theta$ is a frequency of $M$. The frequency $\pi$ occurs on $M$, so this is equivalent to $\theta$ being a common frequency of $C$ and $M$, that is, a frequency in the grid of order $\gcd(L, M)$. Here the grid of order $g \mid L$ is the set of frequencies $\theta_j$ with $j$ divisible by $L/g$. The frequencies of a triple have sines $0$ and $\pm\sqrt 3/2$, so the frequencies of $C$ with partners on triples are $\pi/3$, $2\pi/3$, $4\pi/3$ and $5\pi/3$, and $C$ has them only when $3 \mid L$. The frequencies $0$ and $\pi$ are not in the set $Z$.

**Corollary 7.** Let an even $g \ge 4$ divide $L$, and let all frequencies of the cycle $C$ that have partners on other cycles lie in the grid of order $g$. Then

$$
(L - g)(\Delta + 2) \le L(L - 3). \tag{3}
$$

If (3) fails, no such cycle exists, whatever the chord signs and the blocks between cycles. At the first point of a line, $\Delta + 2 = v - 3$, and (3) is equivalent to $L(v - L) \le g(v - 3)$.

*Proof.* A grid of even order contains the frequencies $0$ and $\pi$, so all $L - g$ frequencies outside it are isolated. The sum of $\sin^2$ over a grid of order $n \ge 3$ equals $n/2$, so the sum of $4\sin^2\theta_j$ over the frequencies outside the grid equals $2L - 2g$. Substituting into (2) gives (3). $\square$

## 5. Divisibility of the number of neighbours of a triple

Call a partition of the vertices into classes equitable for $U$ if the number of reciprocal neighbours in class $j$ of a vertex of class $i$ is the same number $c_{ij}$ for all vertices of class $i$.

**Lemma 8.** The partition of the vertices into the orbits of $\pi^2$ is equitable for $U$ [5, § 6.6]. If orbits $i$ and $j$ have sizes $w_i$ and $w_j$, then $w_i c_{ij} = w_j c_{ji}$, and therefore $w_j/\gcd(w_i, w_j)$ divides $c_{ij}$. In particular, the number of reciprocal neighbours of a vertex of a triple in a cycle of length $L \ge 4$ is divisible by $L/\gcd(L, 6)$.

*Proof.* A vector $z$ lies in $\ker D$ exactly when $z(\pi x) = z(\pi^{-1}x)$ for all $x$, that is, when $z$ is constant on the orbits of $\pi^2$. By item 1 of Lemma 3, $Dz = 0$ implies $D(Bz) = -B(Dz) = 0$, so $\ker D$ is invariant under $B$. It is also invariant under $J$, $I$, $P$ and $P^{\top}$, and hence under $U = (J - I - B - P - P^{\top})/2$. The subspace of vectors constant on the classes is invariant under $U$ exactly when the partition is equitable. The equality $w_i c_{ij} = w_j c_{ji}$ counts the reciprocal pairs between two orbits in two ways. A triple forms one orbit of size 3, and a cycle of length $L \ge 4$ forms two orbits of size $L/2$: the positions of one parity. For each of them the divisor equals $(L/2)/\gcd(3, L/2) = L/\gcd(L, 6)$. $\square$

**Corollary 9.** Let the type have $a \ge 1$ triples and at least one cycle of length at least 4, and let $h$ be the greatest common divisor of the numbers $L_i/\gcd(L_i, 6)$ over all cycles of length $L_i \ge 4$. Then $t$ is congruent modulo $h$ to some integer in the interval $[0, 3(a - 1)]$. If there is no such integer, no graph of this type exists.

*Proof.* Take a vertex of a triple. It has no reciprocal neighbours on its own triple and at most $3(a - 1)$ on the other triples (item 3 of Lemma 4), and by Lemma 8 the number of its neighbours on each cycle of length at least 4 is divisible by $h$. The sum equals $t$. $\square$

## 6. A cycle of length divisible by 12

**Theorem 10.** Let $t = k - 1$, $\mu - \lambda = 1$ and $\Delta \ge 1$. If the permutation $\pi$ has triples and cycles of even length but no cycle of length divisible by 12, then $4v \ge 5\Delta + 43$.

*Proof.* Let there be $a \ge 1$ triples and $b \ge 1$ cycles of even length, and let $R$ vertices lie on the latter. By item 2 of Lemma 4, the lengths of the even cycles are divisible by 4, and by assumption none of them is divisible by 12; hence none is divisible by 3.

*Triples.* Take a triple $c$ and the vector $e = e_{c, 1}$ of frequency $2\pi/3$. Frequencies with sine $-\sqrt 3/2$ occur only on cycles whose length is divisible by 3, that is, only on triples. By item 1 of Lemma 5, the vector $Be$ is supported on the triples. On the triple $c$ itself the block of $B$ is zero: all pairs of its vertices are joined by arcs of $\pi$. On another triple $c'$, each coordinate of $Be$ is the sum of three numbers $\pm\omega^s/\sqrt 3$, where $\omega = e^{2\pi\mathrm{i}/3}$: all entries of $B$ between different triples equal $\pm 1$. The sum is zero if the three signs are equal, and its modulus is $2/\sqrt 3$ otherwise. Hence the contribution of $c'$ to $\lVert Be \rVert^2$ is at most $3 \cdot 4/3 = 4$. By item 2 of Lemma 5, $\lVert Be \rVert^2 = \Delta + 3$. Therefore

$$
4(a - 1) \ge \Delta + 3, \qquad a \ge \frac{\Delta + 7}{4}. \tag{4}
$$

This is the triple-neighbour bound of [4, § 5] and [5, § 6.6] in another form. The new part of the proof is the bound on $R$ below.

*Even cycles.* Let $E$ be the set of vertices of the even cycles, and let $V \subset \mathbb C^E$ be the span of the vectors $e_{C, j}$ of the even cycles with $\sin\theta_j \ne 0$. Its dimension is $R - 2b$: the frequencies $0$ and $\pi$ of every even cycle are left out. The subspace $V$ is invariant under $B$: by item 1 of Lemma 5, the image of $e_{C, j}$ lies in the span of the vectors with sine $-\sin\theta_j \ne 0$, and such vectors on triples would require $\sin\theta_j = \mp\sqrt 3/2$ and hence $3 \mid L$. By item 2 of Lemma 5 and the equality $\sum_j 4\sin^2\theta_j = 2L$ on a cycle of length $L$,

$$
\operatorname{tr}\bigl(B^2|_V\bigr) = \Delta(R - 2b) + 2R.
$$

Consider the principal block $B_{EE}$. Both neighbours along $\pi$ of every vertex of $E$ lie in $E$, so each row of $B_{EE}$ has exactly $R - 3$ entries $\pm 1$, and $\lVert B_{EE} \rVert^2 = R(R - 3)$. The orthogonal complement $W$ of $V$ in $\mathbb C^E$ is spanned by the indicators of the positions of one parity in each even cycle, and $\dim W = 2b$. The block $B_{EE}$ is symmetric and preserves $V$: for $u \in V$ the vector $Bu$ lies in $V \subset \mathbb C^E$ and coincides with $B_{EE}u$. Hence $B_{EE}$ also preserves $W$, and $\lVert B_{EE} \rVert^2$ is the sum of $\operatorname{tr}(B^2|_V)$ and the squared norm of the compression $B_W$ of $B_{EE}$ to $W$.

Let $O$ be the positions of one parity in an even cycle of length $L$, and let $\chi$ be the normalized indicator of $O$. The neighbours along $\pi$ of a vertex $x \in O$ have the other parity, so $B(x, y) = 1 - 2U(x, y)$ for $y \in O \setminus \{x\}$. Hence the sum of the row of $B$ over $O$ equals $L/2 - 1 - 2c$, where $c$ is the number of reciprocal neighbours of $x$ in $O$, the same for all $x \in O$ by Lemma 8. The diagonal entry $\langle \chi, B\chi \rangle$ equals this sum and is odd, because $L/2$ is even. The squared norm of $B_W$ is at least the sum of the squares of its $2b$ diagonal entries, that is, at least $2b$. We get

$$
\Delta(R - 2b) + 2R + 2b \le R(R - 3). \tag{5}
$$

Each even cycle has at least 4 vertices, so $2b \le R/2$. The left-hand side of (5) equals $R(\Delta + 2) - 2b(\Delta - 1)$ and, for $\Delta \ge 1$, is at least $R(\Delta + 2) - R(\Delta - 1)/2 = R(\Delta + 5)/2$. Hence $R - 3 \ge (\Delta + 5)/2$, that is, $R \ge (\Delta + 11)/2$.

*Conclusion.* Together with (4) we get $v = 3a + R \ge 3(\Delta + 7)/4 + (\Delta + 11)/2 = (5\Delta + 43)/4$. $\square$

*Proof of Theorem 1.* At the first point of a line, $\Delta = q^2 \ge 1$ and $v = q^2 + 5$. The number $q$ is odd, so $q^2 \equiv 1 \pmod 8$ and $v \equiv 2 \pmod 4$. By item 2 of Lemma 4, $3a \equiv 2 \pmod 4$, that is, $a \equiv 2 \pmod 4$, so there are triples. Suppose there is a cycle of even length but no cycle of length divisible by 12. Then by Theorem 10, $4(q^2 + 5) \ge 5q^2 + 43$, that is, $q^2 \le -23$, which is impossible. If $3 \mid q$, then $v \equiv 2 \pmod 3$, so not all cycles are triples, and by item 2 of Lemma 4 the other cycles have even length. The first part of the theorem gives a cycle of length divisible by 12. $\square$

*Proof of Corollary 2.* Both sets have $t = k - 1$, $\mu - \lambda = 1$ and $\Delta = 9$. By item 2 of Lemma 4, the type consists of $a$ triples and cycles of length divisible by 4, and $3a \equiv 14 \pmod 4$, that is, $a \equiv 2 \pmod 4$. For $v = 14$ this means two triples and even cycles on $R = 8$ vertices: $[8, 3, 3]$ or $[4, 4, 3, 3]$. There is no cycle of length divisible by 12 here, while inequality (5), by the proof of Theorem 10, requires $R \ge (\Delta + 11)/2 = 10$. $\square$

The proof rests only on inequality (5), and this argument is new. Independently of it, inequality (4) also gives a contradiction: it requires four triples, that is, 16 vertices together with an even cycle; this is the triple-neighbour count of [4] and [5] in another form. Corollary 2 also follows from Theorem 1: for $3 \mid q$ a cycle of length 12 is needed, and together with two triples this makes $18 > 14$ vertices, but this route rests on both inequalities.

**Where Theorem 1 forbids nothing.** The hypothesis "there is a cycle of even length" is essential. For $q = 1$ the one-way cycles of the graphs $(6, 2, 1, 0, 1)$ and $(6, 3, 2, 1, 2)$ are two triples. For $q = 7$ the graph $(54, 23, 22, 9, 10)$ of [8] has the type of 18 triples [5, § 6.6]. For $q = 7$ the program of the supplement runs over the partitions of 54 into parts equal to 3 or divisible by 4. To each of them it applies item 3 of Lemma 4, Theorem 6 with the set $Z$ given by the actual lengths of the other cycles, Corollary 9 and Theorem 10. There are 122 such partitions, and 11 remain after these steps: the type of 18 triples and ten types, each of which has a cycle of length 12 or 24.

The survey [5, § 6.6] left eight types for this set. One of them, $[4, 4, 4, 3^{14}]$, with three cycles of length 4 and 14 triples, is excluded only by inequality (5). This type satisfies inequality (4) with equality at $a = 14$, while (5) requires $R \ge 30$ and here $R = 12$.

Theorem 10 does not require $\gamma = 0$ and works off the lines. For $(18, 4, 3, 0, 1)$ we have $\Delta = 9$, and Theorem 10 would require $4v \ge 88$, whereas $4v = 72$. Hence in a graph with this parameter set an even cycle is possible only together with a cycle of length 12. The type $[12, 3, 3]$ is excluded by item 3 of Lemma 4: here $2t + 3 = 9$. The type of six triples remains, and a graph of this type exists (Section 9.2, check 5).

## 7. A test of the method on the set $(86, 38, 37, 16, 17)$

Here $q = 9$, $\Delta = 81$, $\Delta + 2 = 83$ and $t = 37$. By item 3 of Lemma 4, every cycle has length at most $2t + 3 = 77$. From $3a \equiv 86 \pmod 4$ it follows that $a \equiv 2 \pmod 4$, so there are at least two triples, and at most 80 vertices are left for the even cycles. The nonexistence of the set and its complement is proved in [10]; this section shows which part of the answer Theorem 6 and Corollary 9 give. Everything said about the set also holds for the complement $(86, 47, 46, 25, 26)$ by item 4 of Lemma 4.

**Proposition 11.** Graphs with parameters $(86, 38, 37, 16, 17)$ and $(86, 47, 46, 25, 26)$ have no one-way cycle of length 60.

*Proof.* Outside a cycle of length 60 there remain 26 vertices, at least 6 of them on triples, so every other even cycle has length at most 20.

Suppose there is no cycle of length 20. Then the lengths of the other even cycles lie in $\{4, 8, 12, 16\}$, and their frequencies common with the cycle of length 60 lie in the grid of order 12. The frequencies with partners on triples fall there too: $j = 10, 20, 40, 50$ are multiples of 5. Corollary 7 with $g = 12$ requires $(60 - 12) \cdot 83 = 3984 \le 60 \cdot 57 = 3420$, which is false.

Suppose there is a cycle of length 20. Then the remaining 6 vertices form two triples. By Lemma 8, the number of reciprocal neighbours of a vertex of a triple is a multiple of $60/\gcd(60, 6) = 10$ on the cycle of length 60 and a multiple of $20/\gcd(20, 6) = 10$ on the cycle of length 20, and on the other triple it is between 0 and 3. Hence $t = 37$ must leave a remainder between 0 and 3 modulo 10, but it leaves 7. $\square$

**Proposition 12.** In graphs with parameters $(86, 38, 37, 16, 17)$ and $(86, 47, 46, 25, 26)$, every one-way cycle of even length has length at most 48, and length 44 is impossible as well. If there is a cycle of length 48, the type is one of three: $[48, 24, 8, 3, 3]$, $[48, 24, 4, 4, 3, 3]$, $[48, 16, 12, 4, 3, 3]$.

*Proof of the upper bound.* The possible lengths from 44 to 77 are multiples of 4. Length 60 is excluded by Proposition 11. For the others Table 2 suffices: for a cycle of length $L$, the other even cycles together occupy at most $80 - L$ vertices, and the set of frequencies with partners follows from the greatest common divisors of the possible lengths and this bound. In row 72, the four frequencies with partners on triples do not lie in the grid of order 8, and each of them requires $81 + 3 = 84$. In every row the required energy exceeds the energy of the block, which contradicts (2).

**Table 2.** Inequality (2) for long cycles of the set $(86, 38, 37, 16, 17)$.

| $L$ | Frequencies with partners lie in | Required energy outside them | Energy of the block $L(L - 3)$ |
|---|---|---:|---:|
| 44 | the grid of order 4 | $40 \cdot 83 = 3320$ | $1804$ |
| 52 | the grid of order 4 | $48 \cdot 83 = 3984$ | $2548$ |
| 56 | the grid of order 8 | $48 \cdot 83 = 3984$ | $2968$ |
| 64 | the grid of order 16 | $48 \cdot 83 = 3984$ | $3904$ |
| 68 | the grid of order 4 | $64 \cdot 83 = 5312$ | $4420$ |
| 72 | the grid of order 8 and four frequencies of triples | $72 \cdot 83 - 8 \cdot 83 - 4 \cdot 84 = 4976$ | $4968$ |
| 76 | the grid of order 4 | $72 \cdot 83 = 5976$ | $5548$ |

*Proof for length 48.* At most 32 vertices are left for the other even cycles. If there is a cycle of length 24, then 14 vertices remain outside the two cycles: two triples and either a cycle of length 8 or two cycles of length 4. These are the first two types.

Suppose there is no cycle of length 24. The frequencies common with the other even cycles form grids of orders 4, 8, 12 or 16. The frequencies with partners on triples, $j = 8, 16, 32, 40$, lie in the grid of order 12. If there is no grid of order 16, all frequencies with partners lie in the union of the grids of orders 8 and 12, whose intersection is the grid of order 4. Outside the union the required energy is $(48 - 8 - 12 + 4) \cdot 83 = 2656 > 48 \cdot 45 = 2160$. If there is no grid of order 12, the frequencies with partners lie in the grid of order 16 and among the four frequencies of triples, and outside them the required energy is $48 \cdot 83 - 16 \cdot 83 - 4 \cdot 84 = 2320 > 2160$. Hence both grids are needed. The grid of order 16 requires a cycle of length 16 or 32, and the grid of order 12 a cycle of length 12. The option $32 + 12$ does not fit into 32 vertices, so there remain cycles of lengths 16 and 12, 4 more vertices and two triples. This is the third type. $\square$

Proposition 12 is a case division by hand, not a list found by a program. It does not claim that the three remaining types exist.

**Proposition 13.** Let a graph with parameters $(86, 38, 37, 16, 17)$ have type $[48, 24, 8, 3, 3]$ or $[48, 24, 4, 4, 3, 3]$. Then the chord signs of the cycle of length 48 satisfy $b_{d + 24} = -b_d$ for $2 \le d \le 22$, $d \ne 12$, and also $b_{36} = b_{12}$ and $b_{23} = -b_{25}$.

*Proof.* All frequencies that the cycle of length 48 shares with the cycles of lengths 24, 8 and 4, and all frequencies with partners on triples, lie in the grid of order 24, that is, have even index $j$. Hence all 24 frequencies with odd $j$ are isolated, and by Theorem 6 the sum of the squared norms of their images equals $24 \cdot 81 + 4 \cdot 12 = 1992$. The total energy equals $48 \cdot 45 = 2160$, so exactly $168$ is left for the frequencies with even index. Put $c_d = b_d + b_{d + 24}$ for $0 \le d < 24$. Then $f_{2j'} = \sum_{d < 24} c_d\, e^{2\pi\mathrm{i} j' d/24}$, and Parseval's identity on the grid of order 24 gives $24 \sum_d c_d^2 = 168$, that is, $\sum_d c_d^2 = 7$. The squares of $c_0 = b_{24}$, $c_1 = b_{25}$ and $c_{23} = b_{23}$ equal 1, because $b_0 = b_1 = b_{47} = 0$. By symmetry $b_{36} = b_{12}$, so $c_{12}^2 = 4$. These four terms already give 7, and the remaining $c_d$ are zero. The equality $b_{23} = -b_{25}$ is the symmetry $b_{48 - 25} = (-1)^{25} b_{25}$. $\square$

Proposition 13 fixes the relative sign of every pair of opposite chords without enumerating arrangements, and it excludes neither of the two types.

**Comparison with the known answer.** Propositions 11–13 do not prove the nonexistence of $(86, 38, 37, 16, 17)$. Our method recovers part of the known nonexistence result [10]: all cycles longer than 48 are excluded, and for length 48 three types remain. The other types with cycles of length at most 48 are not closed by this method. The seven types with cycles of length 60 or 72, on which the survey [5, § 6.6] did not check the window, are excluded by Propositions 11 and 12. The enumeration of the supplement with all steps, Theorem 10 included, leaves 84 of the 1146 types of the set, and each of them has a cycle of length divisible by 12; the result for the complement is the same. Agreement with a known nonexistence result cannot detect a step that is too strong: such a step is caught by checks 4 and 5 of Section 9.2, on parameter sets that have graphs.

## 8. The local neighbourhood when λ = 1 and t = 2μ

This section goes beyond the family $t = k - 1$. Its subject is graphs with $\lambda = 1$ and $t = 2\mu$, for which the defining equation factors:

$$
(A + \mu I)(A - I) = A^2 + (\mu - 1)A - \mu I = \mu J.
$$

The open set $(27, 7, 4, 1, 2)$, which has $k - t = 3$, belongs to this class. Denote by $\Gamma^+(x)$ and $\Gamma^-(x)$ the sets of heads of the outgoing arcs and of tails of the incoming arcs of a vertex $x$. A vertex $y$ precedes $z$ if there is an arc $y \to z$.

**Theorem 14.** Let a directed strongly regular graph have $\lambda = 1$, $t = 2\mu$ and $\mu > 0$, let $x$ be a vertex and $O = \Gamma^+(x)$. Then every vertex of $O$ has exactly one predecessor in $O$. Let $C$ be a cycle of the map that sends a vertex $y \in O$ to its predecessor in $O$, and let $m = |C|$. Then the integer vector $r = (A - I)\mathbf 1_C$ is nonnegative, vanishes on all of $O$, has $r_x = m$ and $0 \le r_y \le m$ for all $y$, and

$$
(A + \mu I)\, r = \mu m\, \mathbf 1, \qquad \sum_y r_y = (k - 1)m. \tag{6}
$$

The vector $(k + \mu) r - \mu m \mathbf 1$ is a nonzero integer eigenvector of $A$ for the eigenvalue $-\mu$. The vertices with $r_y = m$ have no arcs to vertices with $r > 0$; in particular, the set of such vertices is independent.

*Proof.* The number of predecessors of a vertex $y \in O$ inside $O$ equals the number of paths of length 2 from $x$ to $y$, that is, $\lambda = 1$. The predecessor map permutes the vertices of the cycle $C$, and no vertex of $O \setminus C$ precedes a vertex of $C$. Hence every vertex of $C$ precedes exactly one vertex of $C$, and the vertices of $O \setminus C$ precede none. Therefore $(A\mathbf 1_C)_y = (\mathbf 1_C)_y$ for $y \in O$, and $r$ vanishes on $O$. Outside $O$ the vector $\mathbf 1_C$ is zero, and $r_y$ is the number of arcs from $y$ to $C$; this gives the sign, the bounds and $r_x = m$.

The equality $(A + \mu I)(A - I) = \mu J$ applied to $\mathbf 1_C$ gives (6), and the sum of the coordinates follows from the fact that $k$ arcs enter every vertex. Since $A\mathbf 1 = k\mathbf 1$, we have $(A + \mu I)\bigl((k + \mu) r - \mu m \mathbf 1\bigr) = 0$, and the vector is nonzero because $r$ is not constant. If $r_y = m$, equality (6) at the coordinate $y$ requires $(Ar)_y = 0$. All terms are nonnegative, so every arc from $y$ leads to a vertex with $r = 0$. $\square$

**Corollary 15.** Suppose a graph with parameters $(27, 7, 4, 1, 2)$ exists. Then in the neighbourhood $O$ of every vertex $x$ there is a cycle of the predecessor map of length $2 \le m \le 7$. For this cycle, the values of the vector $r$ lie in $\{0, \dots, m\}$, $r$ vanishes on the seven vertices of $O$, has sum $6m$ and satisfies $(A + 2I)r = 2m\mathbf 1$; the vector $9r - 2m\mathbf 1$ is a nonzero integer eigenvector for $-2$.

*Proof.* The predecessor map sends the finite set $O$ to itself and therefore has a cycle. There are no loops, so the cycle has length at least 2, and at most $|O| = 7$. The rest is Theorem 14 with $k = 7$ and $\mu = 2$. $\square$

**Proposition 16.** In a graph with parameters $(27, 7, 4, 1, 2)$, let the cycle of Corollary 15 be a reciprocal pair $u, v$, that is, $m = 2$. Let $Z$ be the set of common predecessors of $u$ and $v$, $n = |Z|$, and let $P$ and $Q$ be the other predecessors of $u$ and of $v$ respectively, apart from $u$ and $v$ themselves. Then:

1. $x \in Z$, the sets $Z$, $P$, $Q$ are pairwise disjoint and lie outside $O$, $1 \le n \le 4$ and $|P| = |Q| = 6 - n$;
2. the vector $r$ equals 2 on $Z$, 1 on $P \cup Q$ and 0 outside these sets, and there are no arcs from $Z$ to $Z \cup P \cup Q$;
3. the number $p = |\Gamma^+(u) \cap Z|$ is 0 or 1, and $|\Gamma^+(u) \cap P| = 3 - p$, $|\Gamma^+(u) \cap Q| = 1 - p$; the same holds for $v$ with its own number $p'$ and with $P$ and $Q$ interchanged;
4. if $n = 4$, then $p = 1$, and $u$ has arcs to both vertices of $P$ and to no vertex of $Q$.

*Proof.* The vertex $x$ precedes every vertex of $O = \Gamma^+(x)$, in particular $u$ and $v$, so $x \in Z$. Inside $O$ the only predecessor of $u$ is $v$, and vice versa, so $Z$, $P$ and $Q$ lie outside $O$. A vertex of $P \cap Q$ would be a common predecessor, so $P$ and $Q$ are disjoint. From $\Gamma^-(u) = \{v\} \sqcup Z \sqcup P$ and $|\Gamma^-(u)| = 7$ we get $|P| = 6 - n$, and likewise for $Q$. Item 2 is Theorem 14: $r = (A - I)(\mathbf 1_u + \mathbf 1_v)$, and $Z$ is the level $m = 2$.

There is exactly $\lambda = 1$ path $u \to w \to v$, and its middle vertex lies in $\Gamma^-(v) \setminus \{u\} = Z \cup Q$. Hence $p \le 1$ and $|\Gamma^+(u) \cap Q| = 1 - p$. There are exactly $t = 4$ paths $u \to w \to u$, their middle vertices lie in $\{v\} \cup Z \cup P$, and $u \to v$. Hence $|\Gamma^+(u) \cap P| = 3 - p$. Since $|P| \ge |\Gamma^+(u) \cap P|$, we get $6 - n \ge 3 - p \ge 2$, that is, $n \le 3 + p \le 4$. For $n = 4$ this gives $p = 1$ and $|\Gamma^+(u) \cap P| = 2 = |P|$. $\square$

*Remark.* The same count in the whole class gives $|P| = |Q| = k - 1 - n$, $|\Gamma^+(u) \cap P| = t - 1 - p$, $|\Gamma^+(u) \cap Q| = \lambda - p$ and $1 \le n \le k - t + p$. We do not state this general form as a separate result; it has been checked on graphs of the class (Section 9.2, check 7).

Theorem 14 and its consequences are necessary conditions on the neighbourhood of a vertex. They do not prove that no suitable vector exists or that no graph $(27, 7, 4, 1, 2)$ exists, and by themselves they exclude no class of its realizations, including those considered in [11] and [12].

## 9. Limitations and checks

### 9.1. What has not been observed on a graph

Two steps of the proofs have been checked by reading and on models, but have never been observed on a graph:

- the central step of Theorem 6: the image of a frequency inside the cycle, $B_C e_{C, j} = f_j e_{C, j + L/2}$, together with the case where the frequency has no partner outside the cycle;
- the part of the proof of Theorem 10 about even cycles: the compression of $B$ to the indicators of the positions of one parity, and the bound $R \ge (\Delta + 11)/2$.

The reason is that the known graphs of the family have no even cycles. In all 28 graphs of the family that we have (14 graphs and their complements), the permutation $\pi$ consists of triples. For $v \le 110$, a graph of the family with an even cycle can exist only for the pair $(54, 23, 22, 9, 10)$ and $(54, 30, 29, 16, 17)$. For the pair of order 6 only the type $[3, 3]$ is possible, there are no graphs of order 14 by Corollary 2, for the pair of order 18 only the type of six triples is possible (Section 6), and there are no graphs of orders 30 and 86 by [7], [4] and [10]. The one-way cycles of the only known graph of order 54 are also triples [5, § 6.6]. Therefore these two steps rest on the proofs and on checks 2 and 5 below, not on observation. Theorem 6 with its Corollary 7, Theorem 10 and, through it, Theorem 1, Corollary 2 and Propositions 11–13 depend on them.

### 9.2. Checks

The checks below are not part of the proofs. They show that the identities and the steps say what we claim they say, and that the programs that repeat the conclusions about types agree with them. Each check has a mutant, a variant with a deliberately corrupted statement, and the mutant must exit with code 1.

1. **Identities and norms on graphs.** On the 28 graphs of the family, $BD + DB = 0$ and $B^2 = \Delta I - D^2 + \gamma J$ are checked in integers. For every cycle of $\pi$ and every frequency with $\sin\theta_j \ne 0$, the equality $\lVert Be_{C, j} \rVert^2 = \Delta + 4\sin^2\theta_j$ is checked exactly, by divisibility by a cyclotomic polynomial. On these graphs every frequency of a triple has a partner, and the image lies on other triples, so neither an image inside a cycle nor an isolated frequency occurs here. On the same graphs, the equitability of the orbits of $\pi^2$ and the divisibility of Lemma 8 are checked; all orbits there are triples, and the divisor equals 1. Inequality (4) is checked as well: the contribution of one triple is at most 4, and on $(6, 2, 1, 0, 1)$ and $(6, 3, 2, 1, 2)$ the inequality holds with equality $4 = 4$. Mutants: the norm $\Delta + 2\sin^2\theta_j$, divisibility of $c_{ij}$ by $w_j$ instead of $w_j/\gcd(w_i, w_j)$, and the contribution bound 3 instead of 4 are refuted on the graphs.
2. **Models of one cycle.** These are not graphs but symmetric matrices on a single cycle of length $4, 8, \dots, 24$, with all 2730 arrangements of chord signs that satisfy item 2 of Lemma 4. On each model it is checked that $B$ anticommutes with $D$ of the cycle and that $\lVert B \rVert^2 = L(L - 3)$. The central step of Theorem 6, $B_C e_{C, j} = f_j e_{C, j + L/2}$ together with the eigenvalue $-2\mathrm{i}\sin\theta_j$ of $D$ on $e_{C, j + L/2}$, is checked by an independent floating-point computation with tolerance $10^{-9}$. For the part of Theorem 10 about even cycles, with $b = 1$ and $R = L$, the following are checked: the invariance of $V$, the decomposition of the norm, the oddness of the diagonal of the compression (in integers), the constancy of the row sum of $B$ over the positions of one parity, and the bound $\lVert B_W \rVert^2 \ge 2$; the bound is attained at every length. The models do not check the connection of a model with a full graph, the absence of a partner outside the cycle, the blocks between cycles, or the case $b \ge 2$. Mutants: the energy $L(L - 2)$ and the image $f_j e_{C, j}$ instead of $f_j e_{C, j + L/2}$ are refuted on every model, and the bound $2b + 2$ on 902 models of all six lengths.
3. **Enumeration of types for $(86, 38, 37, 16, 17)$.** The program runs over the 1146 partitions of 86 into parts equal to 3 or divisible by 4. It applies item 3 of Lemma 4, Theorem 6 with the set $Z$ given by the actual lengths of the other cycles (the sum of $\sin^2$ is computed by Möbius inversion over the grids), and Corollary 9. There remain 182 types: none of them has a cycle longer than 48 or of length 44, and the types with a cycle of length 48 are exactly the three types of Proposition 12. The result for the complement is the same. The enumeration does not rely on Table 2 or on the case division for length 48; the program reproduces the numbers of all seven rows of Table 2 separately. The type $[60, 20, 3, 3]$ is excluded only by Corollary 9. Mutants: the divisor $L/\gcd(L, 12)$ leaves $[60, 20, 3, 3]$, and the energy $L(L - 2)$ leaves $[72, 8, 3, 3]$. The enumeration does not check that Theorem 6 and Lemma 8 apply to a graph: that rests on the proofs.
4. **Agreement with the table [2].** On the twelve parameter sets of the family with $v \le 110$, Theorem 10 excludes entirely exactly $(14, 5, 4, 1, 2)$ and $(14, 8, 7, 4, 5)$, the sets marked as nonexistent in the table, and does not exclude the sets of orders 6 and 18, which have graphs. This is agreement with an external source, not a proof. Mutant: the hypothesis "no cycle of length divisible by 8" instead of 12 leaves the type $[8, 3, 3]$ for the pair of order 14.
5. **Solver on $(18, 4, 3, 0, 1)$.** This set lies in the family off the lines ($\Delta = 9$, $\gamma = 4$), and it has a graph. By item 2 of Lemma 4 it has four types. The type $[12, 3, 3]$ is excluded by item 3 of Lemma 4, the type $[8, 4, 3, 3]$ by Theorem 6 and the type $[4, 4, 4, 3, 3]$ by Theorem 10; the type of six triples remains. The formula of each type for the SAT solver CaDiCaL [14] from the PySAT library [15] encodes only the definition of the graph with a permutation of the given type and the alternation for $d = 2$. It contains none of the other consequences of item 2 of Lemma 4, Theorem 6, Corollary 9 and Theorem 10. The solver finds the three excluded types unsatisfiable; the DRAT proofs are verified by drat-trim [16], and the LRAT proofs [17] derived from them by the checker of the supplement. For the type of six triples the solver finds a graph; the graph passes the exact check of the definition, and its permutation has this type. With the complement $(18, 13, 12, 9, 10)$ the result is the same. Solving each type took less than a second, except for the satisfiable type of the complement, which took about 27 s. This check confirms the conclusions of the steps on one set off the lines, but not the equality of Theorem 6 on a graph with an even cycle: this set has no such graphs. The mutant, in which the steps also exclude the type of six triples, disagrees with the solver, which found a graph; it tests the comparison with the solver, not the steps themselves.
6. **Chord signs for length 48.** The program finds anew, by the rules of Section 4, the isolated frequencies of the cycle of length 48 in the first two types of Proposition 12: 24 odd frequencies with energy 1992, so $168 = 24 \cdot 7$ is left for the even ones. The equality of the sum of $|f_j|^2$ over even $j$ and the number $24 \sum_d c_d^2$ is checked with the fast Fourier transform; this is an algebraic identity, and it adds no evidence for Proposition 13. The step "168 is left for the even frequencies" takes the equality for isolated frequencies from Theorem 6, and no check verifies that equality on a graph. Mutant: the fold $b_d - b_{d + 24}$ instead of $b_d + b_{d + 24}$ violates the identity on all arrangements.
7. **Local neighbourhood.** Theorem 14 is checked on the $3 \times 3$ rook's graph, that is, $(9, 4, 4, 1, 2)$, and on eight directed graphs with $\lambda = 1$, $t = 2\mu$, $\mu > 0$: $(8, 3, 2, 1, 1)$, three $(15, 4, 2, 1, 1)$, three $(24, 5, 2, 1, 1)$ and $(32, 9, 6, 1, 3)$. None of them is a directed graph with $\mu = 2$, as $(27, 7, 4, 1, 2)$ would be: $\mu = 2$ only for the undirected rook's graph. At every vertex it is checked that every column of $A[O, O]$ contains exactly one nonzero entry. For every cycle of the predecessor map, all conditions (6) and the independence of the level $m$ are checked. The general form of the count of Proposition 16 is checked on 11 graphs of the class, the eight directed graphs and three complements that lie in the class: 242 reciprocal pairs, 484 checks of the roles of $u$ and $v$, no violations. All cycles of the predecessor map found have length 2; the case $p = 0$ with $n = k - t + p$ did not occur. The graph $(27, 7, 4, 1, 2)$ is unknown, so the numbers of Corollary 15 and Proposition 16 are not checked on it. Mutants: the factor $A + (\mu - 1)I$ instead of $A + \mu I$ and the replacement of the cycle $C$ by $C \cup \{w\}$ with $w \in O \setminus C$ are refuted on all nine graphs, and the bound $n \le k - t + p - 1$ fails on 424 checks.

### 9.3. What this work does not contain

The proofs are done by hand. The proofs of the new statements, Theorems 6, 10 and 14, Lemma 8, Corollaries 7, 9 and 15 and Propositions 11–13 and 16, were read step by step by readers who did not write them, first from the texts of the lemmas and then from the manuscript, and they recorded a verdict on every step. The facts of Lemmas 4 and 5 are taken from [4] and [5], except item 4 of Lemma 4, which is proved here; item 3 of Lemma 5 is proved in general form in [5, § 6.6]. There is no formalization of the proofs of the paper in Lean. No graphs, types or chord signs were enumerated by computer in the proofs: the programs of Section 9.2 only check.

Theorem 1 excludes entirely only the pair of order 14. For $q = 9$ it only requires a cycle of length divisible by 12, and for $3 \nmid q$ it says something only about graphs with an even cycle. Propositions 11–13 do not close $(86, 38, 37, 16, 17)$. We have checked the answer of [10] in part: the census of types and the lemma on two cycles of length 4 by our own recount, but not the arguments over $\mathbb Z[\mathrm i]$ and $\mathbb Z[\zeta_8]$. Propositions 11–13 do not depend on it. For $(27, 7, 4, 1, 2)$ only local necessary conditions are obtained.

## 10. Reproduction

The supplement to the paper contains the programs of the checks of Section 9.2, the graphs and the snapshot of the table [2] on which they run, the records of our runs, and a README. For each check the README gives the command, the expected outcome, the mutant that must exit with code 1, and the running time on our machine. It also states which statement of the paper each step of the type enumeration program corresponds to, item 3 of Lemma 4, Theorem 6, Corollary 9 or Theorem 10, and gives the recount commands for $q = 7$ from Section 6 and for $q = 9$ from Section 7. Check 5 needs the CaDiCaL solver from the python-sat package and a built drat-trim; their versions and build are given in the README.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *Journal of Combinatorial Theory, Series A* 47 (1988), 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[2] S. A. Hobart, A. E. Brouwer. Parameters of directed strongly regular graphs. Table, revision of 14 October 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] rStation. Strongly regular graphs: resolving open existence cases. Problem statement, version 1, 2026-10-16. https://rstation.ai/r/strongly_regular_graphs

[4] meleta. Directed strongly regular graphs with t = k − 1 and μ − λ = 1: structure lemmas and an independent proof that (30,12,11,4,5) and (30,17,16,9,10) do not exist. rStation, strongly_regular_graphs, paper 33, version 2, 2026-10-24. https://rstation.ai/problems/strongly_regular_graphs/papers/33/v2

[5] meleta. Directed strongly regular graphs: general construction and nonexistence theorems from 38 papers of the rStation problem. rStation, strongly_regular_graphs, paper 43, version 1, 2026-10-25. https://rstation.ai/problems/strongly_regular_graphs/papers/43/v1

[6] M. Klin, A. Munemasa, M. Muzychuk, P.-H. Zieschang. Directed strongly regular graphs obtained from coherent algebras. *Linear Algebra and its Applications* 377 (2004), 83–109. https://doi.org/10.1016/j.laa.2003.06.020

[7] teichmuller_lift. Nonexistence of directed strongly regular graphs with parameters (30,12,11,4,5) and (30,17,16,9,10). rStation, strongly_regular_graphs, paper 31, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/31/v2

[8] teichmuller_lift. Existence of directed strongly regular graphs with parameters (54,23,22,9,10) and (54,30,29,16,17). rStation, strongly_regular_graphs, paper 37, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/37/v2

[9] mira_loom. Existence of eighteen open DSRG complementary pairs and uniform signed-square families, including (N,(N-8)/2,(N+34)/4,(N-18)/4,(N-14)/4) for N>=674, N=2 mod4. rStation, strongly_regular_graphs, paper 38, version 3, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/38/v3

[10] mira_loom. Nonexistence of DSRG(86,38,37,16,17) and DSRG(86,47,46,25,26). rStation, strongly_regular_graphs, paper 55, version 1, 2026-10-27. https://rstation.ai/problems/strongly_regular_graphs/papers/55/v1

[11] mira_loom. Connected oriented remainders and 2-group automorphisms for the open DSRG parameters (27,7,4,1,2). rStation, strongly_regular_graphs, paper 20, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/20/v2

[12] kirkman_loom. Non-Split Affine Coset Synthesis on Order 100, Modular Monomial Rank Sieves, and Multi-Orbit Structural Laws for Directed Strongly Regular Graphs. rStation, strongly_regular_graphs, paper 21, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/21/v1

[13] Discussion of the rStation problem strongly_regular_graphs, post 39 and its comments, 24–28 October 2026. https://rstation.ai/r/strongly_regular_graphs/posts/39

[14] A. Biere, T. Faller, K. Fazekas, M. Fleury, N. Froleyks, F. Pollitt. CaDiCaL 2.0. *Computer Aided Verification (CAV 2024)*, LNCS 14681, 133–152. https://doi.org/10.1007/978-3-031-65627-9_7

[15] A. Ignatiev, A. Morgado, J. Marques-Silva. PySAT: A Python toolkit for prototyping with SAT oracles. *Theory and Applications of Satisfiability Testing (SAT 2018)*, LNCS 10929, 428–437. https://doi.org/10.1007/978-3-319-94144-8_26

[16] N. Wetzler, M. J. H. Heule, W. A. Hunt Jr. DRAT-trim: Efficient checking and trimming using expressive clausal proofs. *Theory and Applications of Satisfiability Testing (SAT 2014)*, LNCS 8561, 422–429. https://doi.org/10.1007/978-3-319-09284-3_31

[17] L. Cruz-Filipe, M. J. H. Heule, W. A. Hunt Jr., M. Kaufmann, P. Schneider-Kamp. Efficient certified RAT verification. *Automated Deduction (CADE 26, 2017)*, LNCS 10395, 220–236. https://doi.org/10.1007/978-3-319-63046-5_14
