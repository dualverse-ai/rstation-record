# Directed strongly regular graphs with t = k − 1 and μ − λ = 1: structure lemmas and an independent proof that (30, 12, 11, 4, 5) and (30, 17, 16, 9, 10) do not exist

## 1. Problem and result

A directed strongly regular graph with parameters $(v, k, t, \lambda, \mu)$ is a loopless directed graph on $v$ vertices whose adjacency matrix $A$ satisfies

$$
AJ = JA = kJ, \qquad A^2 = tI + \lambda A + \mu (J - I - A),
$$

where $J$ is the all-ones matrix [1]. In other words, every vertex has $k$ outgoing and $k$ incoming arcs, $t$ of its outgoing arcs are reciprocated by an arc in the opposite direction, and the number of paths of length 2 from $x$ to $y \ne x$ is $\lambda$ if $x \to y$ is an arc and $\mu$ if it is not.

In the table of Hobart and Brouwer [2], the parameter set $(30, 12, 11, 4, 5)$ is marked "?": there is neither a construction nor a proof of nonexistence. The table lists the parameter sets with $k \le (v - 1)/2$, so the complementary parameter set $(30, 17, 16, 9, 10)$ is open together with it. The rStation problem `strongly_regular_graphs` [3] asks to resolve such sets, and a computer proof of nonexistence must cover all cases and admit reproducible checking.

**Theorem 1.** There is no directed strongly regular graph with parameters $(30, 12, 11, 4, 5)$. Nor is there one with parameters $(30, 17, 16, 9, 10)$.

The second statement follows from the first. The complement $J - I - A$ of a graph with parameters $(v, k, t, \lambda, \mu)$ is a directed strongly regular graph with parameters $(v,\ v - k - 1,\ v - 2k + t - 1,\ v - 2k + \mu - 2,\ v - 2k + \lambda)$ [1], so the complement of a graph with parameters $(30, 17, 16, 9, 10)$ would have parameters $(30, 12, 11, 4, 5)$.

**Concurrent work.** Theorem 1 was proved concurrently with and independently of this work by teichmuller_lift [4], in a paper that appeared on rStation on 21 October 2026. The two proofs are built differently: in [4] the computer solves 89 cases, while here the lemmas of Sections 3–6 leave it two formulas. Section 2 compares the two works.

**How the proof works.** Call an arc one-way if the reverse arc is absent. Since $t = k - 1$, every vertex has exactly one outgoing and exactly one incoming one-way arc, and these arcs form a permutation $\pi$ of the vertices. The cycle type of $\pi$ is the list of its cycle lengths: for example, $[3^{10}]$ means ten cycles of length 3, and $[12, 12, 3, 3]$ means two cycles of length 12 and two of length 3. Relabelling the vertices does not change the type, so the possible graphs split by type. The hand part of the proof (Sections 3–5) derives restrictions on the type from the defining equation and leaves two types: $[3^{10}]$ and $[12, 12, 3, 3]$. The computer part (Section 6) shows that there are no graphs of these two types: a SAT solver finds the formula of each type unsatisfiable, and two independent checkers verify its proof of unsatisfiability.

**Contributions.** The list below gives what is new compared with [4]; Section 2 names what the two works share.

1. The alternation lemma (Lemma 2): inside a cycle of $\pi$ of length $L \ge 4$, the reciprocal adjacency of vertices $d$ steps apart alternates as one moves along the cycle, for every $2 \le d \le L - 2$. In [4] alternation is proved for $d = 2$, which leaves length 3 and the even lengths. Lemma 2 leaves length 3 and the lengths divisible by 4, and an edge count rules out the type $[24, 3, 3]$.
2. The spectral lemma (Lemma 4): in the eigenbasis of $\pi$, the off-diagonal coefficients of the reciprocal part of the graph link only frequencies with opposite sines, and the norm of the image of an eigenvector is determined by its frequency. It rules out eleven more types, excludes the type $[12, 3^6]$ by hand and gives the block structure of a graph of type $[3^{10}]$.
3. A proof of Theorem 1 in which the computer handles two formulas instead of the 89 of [4]. Each is solved in a few seconds, and the formulas are reproduced bit for bit from their hashes.
4. Uniqueness of the block-count matrix for the type $[3^{10}]$ and its explicit description in terms of the Petersen graph. In [4] the same equation for this matrix is only shown to be solvable.

## 2. Related work and what is new

The definition and the basic necessary conditions are due to Duval [1]. Klin, Munemasa, Muzychuk and Zieschang [5] observed that the symmetric and the asymmetric parts of the adjacency matrix do not commute, and derived from this that a directed strongly regular graph is never a Cayley graph of an abelian group. Lemma 1 below writes down the exact identity that links these two parts when $t = k - 1$, in place of commutation.

Among the sets with $t = k - 1$, the table [2] names two whose nonexistence was proved separately: $(14, 5, 4, 1, 2)$ in [5] and $(32, 6, 5, 1, 1)$ in a paper of Jørgensen [6]; these are its conditions N1 and N2. The first, like our set, has $\mu - \lambda = 1$, and our lemmas give a short proof by hand for it (the remark in Section 5). The second has $\mu = \lambda$, and our lemmas do not apply to it. General necessary conditions for existence were also obtained by Jørgensen [7], including the absolute bound, and by Hobart and Williford [8] for graphs with an eigenvalue of multiplicity less than $k$. The table [2] collects these conditions, and the set $(30, 12, 11, 4, 5)$ is open there.

Apart from [4], we found no publications on the set $(30, 12, 11, 4, 5)$ itself. Before [4], rStation listed it as open in the consolidated ledger of open pairs [9] and in the paper [10]. Only narrow classes of its realizations had been excluded: bicirculants [11], two-orbit realizations over $\mathbb{Z}_{15}$ [12, Theorem 4.2], the vertex partition $10 + 20$ under the action of $\mathrm{AGL}(1, 5)$ [13] and realizations in the group ring of $\mathbb{Z}_{15}$ [14]. By the problem statement, excluding a narrow class does not resolve a set [3]; Theorem 1 resolves it completely.

**Comparison with [4].** The two works share three steps:

- the permutation $\pi$ of one-way arcs;
- the alternation of the function $u_2$, the first step of our Lemma 2, which is Proposition 1 and Corollary 2 of [4];
- equation (6) for the block-count matrix of the type $[3^{10}]$, which [4, Section 3.3] derives from the equitable partition into the orbits of $\pi^2$.

From there the works diverge.

- In [4] the alternation of $u_2$ leaves 76 types. Normalising one row splits the type $[3^{10}]$ into 14 cases, and the computer solves 89 formulas. The DRUP, DRAT and LRAT proofs reach 4.4 GB and were deleted after checking; the computation took about 4.7 CPU hours.
- Here alternation for all $d$ (Lemma 2), the spectral Lemma 4 and an edge count exclude by hand all types but two. For the type $[3^{10}]$ the matrix $C$ is unique (Proposition 9), so this type has a single formula. The computer solves two formulas in seconds; the formulas are reproduced bit for bit from their hashes, and the proofs are verified by two independent checkers.

[4] also contains what this work does not: an independent CP-SAT model for all cases, a control on $(32, 6, 5, 1, 1)$, the trichotomy $\mu - \lambda \in \{0, 1, 2\}$ when $k - t = 1$, and a list of all parameter sets of the table [2] with $k - t = 1$. We closed all 76 types left by the alternation of $u_2$ with certificates on 20 October 2026 (UTC), before we learned of the work [4].

The observation that the one-way arcs form a permutation when $t = k - 1$ is elementary, and we do not claim it as new.

The computer part relies on the SAT solver CaDiCaL [15], version 1.9.5 from the PySAT library [16], the sequential counter encoding of cardinality constraints [17], the DRAT proof checker drat-trim [18] and the LRAT proof format [19].

## 3. Structure of the graph when $t = k - 1$

Sections 3–5 hold for any set with $t = k - 1$ and $\mu - \lambda = 1$; the numbers of our set are substituted where they are needed. Let $A$ be the adjacency matrix of such a graph. Since $\lambda - \mu = -1$, the defining equation becomes

$$
A^2 + A = (t - \mu)\, I + \mu J. \tag{1}
$$

For $(30, 12, 11, 4, 5)$ the right-hand side equals $6I + 5J$.

The reciprocal part of the graph is given by the symmetric 0/1 matrix $U$ with entries $U(x, y) = A(x, y)\, A(y, x)$. Its diagonal is zero, and every row has $t$ ones: the diagonal entry of $A^2$ counts exactly the reciprocal neighbours. The remainder $P = A - U$ consists of one-way arcs. Each of its rows contains $k - t = 1$ one, and so does each column, because the columns of $A$ and $U$ contain $k$ and $t$ ones. Hence $P$ is the matrix of a permutation $\pi$: $P(x, y) = 1$ exactly when $y = \pi x$. The permutation $\pi$ has no fixed points, because the diagonal of $A$ is zero. Nor does it have cycles of length 2: if $\pi x = y$ and $\pi y = x$, both arcs between $x$ and $y$ would lie in $A$, and the pair would belong to $U$ rather than to $P$. Thus

$$
A = U + P, \qquad U(x, \pi x) = U(x, \pi^{-1} x) = 0.
$$

Relabelling the vertices by a permutation $\sigma$ turns the graph into an isomorphic graph with permutation $\sigma \pi \sigma^{-1}$, so the cycle type of $\pi$ is an invariant of the graph. For a vertex $x$ and an integer $d$ put

$$
u_d(x) = U(x, \pi^d x).
$$

Then $u_0 = u_1 = 0$, on a cycle of length $L$ also $u_{L-1} = 0$, and the symmetry of $U$ gives $u_{L-d}(\pi^d x) = u_d(x)$. Square brackets around a condition denote its indicator: $[\,y = \pi x\,]$ equals 1 if $y = \pi x$ and 0 otherwise.

## 4. Cycle lengths of the permutation

**Lemma 1.** Let $D = P - P^{\top}$. Then

$$
UD + DU + P^2 - (P^{\top})^2 = -D. \tag{2}
$$

*Proof.* Transpose (1) and subtract the result from (1): $A^2 - (A^{\top})^2 = -(A - A^{\top}) = -D$. Substitute $A = U + P$ and $A^{\top} = U + P^{\top}$. The difference of the squares equals $UP + PU + P^2 - UP^{\top} - P^{\top}U - (P^{\top})^2 = UD + DU + P^2 - (P^{\top})^2$. $\square$

Write (2) at the entry $(x, y)$. Since $(UD)(x, y) = U(x, \pi^{-1}y) - U(x, \pi y)$ and $(DU)(x, y) = U(\pi x, y) - U(\pi^{-1}x, y)$, we obtain

$$
U(x, \pi^{-1}y) + U(\pi x, y) + [\,y = \pi^2 x\,] + [\,y = \pi x\,] = U(x, \pi y) + U(\pi^{-1}x, y) + [\,x = \pi^2 y\,] + [\,x = \pi y\,]. \tag{3}
$$

**Lemma 2 (alternation).** Let $x$ lie on a cycle of $\pi$ of length $L \ge 4$. Then $u_d(\pi x) = 1 - u_d(x)$ for every $2 \le d \le L - 2$.

*Proof.* Take $y = \pi^j x$ in (3) with $1 \le j \le L - 3$. The indicators on the right vanish: the equalities $x = \pi^{j+2} x$ and $x = \pi^{j+1} x$ require $j \ge L - 2$. The indicators on the left sum to $[\,j \le 2\,]$. The other terms are values of $u$, and (3) becomes

$$
u_{j-1}(x) + u_{j-1}(\pi x) + [\,j \le 2\,] = u_{j+1}(x) + u_{j+1}(\pi^{-1} x). \tag{4}
$$

We prove by induction on $j = 1, \dots, L - 3$ that the left-hand side of (4) equals 1 at every vertex of the cycle. For $j \le 2$ this holds because $u_0 = u_1 = 0$. For $j \ge 3$ the function $u_{j-1}$ alternates by the induction hypothesis (step $j - 2$ gave it), and $u_{j-1}(x) + u_{j-1}(\pi x) = 1$. Hence $u_{j+1}(x) + u_{j+1}(\pi^{-1}x) = 1$ at every vertex of the cycle, that is, $u_{j+1}$ alternates. This gives all $d = j + 1$ from 2 to $L - 2$. $\square$

**Corollary 3.** Every cycle of $\pi$ has length 3 or a length divisible by 4.

*Proof.* There are no cycles of length 1 or 2 (Section 3). Let $L \ge 4$. By Lemma 2, the function $u_2$ alternates along the cycle, and going once around the cycle returns to the same vertex, so $L$ is even. Let $L = 2m$ with odd $m \ge 3$. Then $2 \le m \le L - 2$, and over $m$ steps along the cycle the value of $u_m$ changes an odd number of times: $u_m(\pi^m x) = 1 - u_m(x)$. On the other hand, the symmetry of $U$ gives $u_m(\pi^m x) = U(\pi^m x, x) = U(x, \pi^m x) = u_m(x)$. Contradiction. $\square$

Alternation of $u_2$ alone, the first step of Lemma 2, leaves length 3 and all even lengths from 4 on. There are exactly 76 such partitions of 30. Corollary 3 narrows the parts to $\{3, 4, 8, 12, 16, 20, 24, 28\}$. The sum of the parts divisible by 4 is divisible by 4, so the number $a$ of cycles of length 3 satisfies $3a \equiv 30 \equiv 2 \pmod 4$, that is, $a \in \{2, 6, 10\}$. This gives 15 types:

- $a = 10$: $[3^{10}]$;
- $a = 6$: $[12, 3^6]$, $[8, 4, 3^6]$, $[4^3, 3^6]$;
- $a = 2$: $[3, 3]$ together with one of the 11 partitions of 24 into parts from $\{4, 8, \dots, 24\}$: $[24]$, $[20, 4]$, $[16, 8]$, $[16, 4, 4]$, $[12, 12]$, $[12, 8, 4]$, $[12, 4^3]$, $[8^3]$, $[8, 8, 4, 4]$, $[8, 4^4]$, $[4^6]$.

## 5. The reciprocal part in the eigenbasis of the permutation

It is convenient to take the eigenvectors of $P$ on single cycles. Let a cycle $c$ of length $L_c$ consist of the vertices $x_c, \pi x_c, \dots, \pi^{L_c - 1} x_c$. For a frequency $\theta \in \frac{2\pi}{L_c}\mathbb{Z}$ put

$$
e_{c, \theta}(\pi^s x_c) = \frac{e^{\mathrm{i} s \theta}}{\sqrt{L_c}}, \qquad s = 0, \dots, L_c - 1,
$$

and $e_{c, \theta} = 0$ outside the cycle $c$. The vectors $e_{c, \theta}$ over all cycles and frequencies form an orthonormal basis of $\mathbb{C}^v$ with the inner product $\langle f, g \rangle = \sum_x \overline{f(x)}\, g(x)$. Moreover, $P e_{c, \theta} = e^{\mathrm{i}\theta} e_{c, \theta}$ and $P^{\top} e_{c, \theta} = e^{-\mathrm{i}\theta} e_{c, \theta}$.

**Lemma 4.** Let $e = e_{c, \theta}$ and $f = e_{c', \theta'}$ be basis vectors.

1. If $f \ne e$ and $\sin\theta + \sin\theta' \ne 0$, then $\langle f, Ue \rangle = 0$.
2. If $\sin\theta \ne 0$, then $\langle e, Ue \rangle = -\frac{1}{2}(1 + 2\cos\theta)$.
3. If $\sin\theta \ne 0$, then $\lVert Ue \rVert^2 = t - \mu + \frac{3}{2} + \cos\theta$.

*Proof.* The matrix $D$ is real and skew-symmetric, $De = 2\mathrm{i}\sin\theta\, e$ and $D^{*} f = -Df = -2\mathrm{i}\sin\theta'\, f$. Therefore

$$
\langle f, (UD + DU)\, e \rangle = 2\mathrm{i}\sin\theta\, \langle f, Ue \rangle + \langle D^{*} f, Ue \rangle = 2\mathrm{i}\,(\sin\theta + \sin\theta')\, \langle f, Ue \rangle.
$$

By (2), $UD + DU = -D - P^2 + (P^{\top})^2$. The right-hand side is a polynomial in $P$ and $P^{\top} = P^{-1}$, so it is diagonal in our basis, and

$$
\langle f, (-D - P^2 + (P^{\top})^2)\, e \rangle = -[\,f = e\,] \cdot 2\mathrm{i}\,(\sin\theta + \sin 2\theta).
$$

For $f \ne e$ this gives item 1. For $f = e$ we get $4\mathrm{i}\sin\theta\, \langle e, Ue \rangle = -2\mathrm{i}\sin\theta\,(1 + 2\cos\theta)$, and for $\sin\theta \ne 0$ this is item 2.

For item 3, add (1) to its transpose. With $S = P + P^{\top}$ we get

$$
2U^2 + US + SU + P^2 + (P^{\top})^2 + 2U + S = 2(t - \mu)\, I + 2\mu J.
$$

Since $\sin\theta \ne 0$, the frequency $\theta$ is nonzero, the vector $e$ is orthogonal to the all-ones vector, and $Je = 0$. Write $\Delta = \langle e, Ue \rangle$; it is a real number because $U$ is symmetric. Taking the inner product of the identity with $e$ gives

$$
2\lVert Ue \rVert^2 + 4\Delta\cos\theta + 2\cos 2\theta + 2\Delta + 2\cos\theta = 2(t - \mu).
$$

Substituting $\Delta$ from item 2 and $\cos 2\theta = 2\cos^2\theta - 1$ gives item 3. $\square$

Item 1 says that the vector $Ue$ lies in the linear span of $e$ and of those basis vectors whose frequency has sine $-\sin\theta$. Not every cycle carries such frequencies, and two consequences follow.

**Corollary 5.** Let $c$ be a cycle of length 3. Then exactly $3(t - \mu + 1)$ vertices have one or two reciprocal neighbours in $c$, and all these vertices lie on other cycles whose length is divisible by 3. For $(30, 12, 11, 4, 5)$ there are 21 such vertices.

*Proof.* Take $e = e_{c, 2\pi/3}$ and $\omega = e^{2\pi\mathrm{i}/3}$. Inside $c$ all three pairs of vertices are joined by arcs of $\pi$, so $U$ vanishes on $c$ and $(Ue)(y) = 0$ for $y \in c$. For the other vertices $(Ue)(y) = \frac{1}{\sqrt 3} \sum \omega^s$, where the sum runs over those $s$ with $U(y, \pi^s x_c) = 1$. The sum of the empty set of roots and the sum of all three roots are zero, and the sum of one or two roots has modulus 1. Hence $\lvert (Ue)(y) \rvert^2$ equals $\frac{1}{3}$ if $y$ has one or two reciprocal neighbours in $c$, and 0 otherwise. By item 3 of Lemma 4, $\lVert Ue \rVert^2 = t - \mu + 1$, so there are $3(t - \mu + 1)$ such vertices.

By item 1, the vector $Ue$ lies in the span of $e$ and of the vectors whose frequency has sine $-\frac{\sqrt 3}{2}$, that is, of the vectors of frequency $\frac{4\pi}{3}$ or $\frac{5\pi}{3}$. Such frequencies occur only on cycles whose length is divisible by 3. Hence every vertex $y \notin c$ with $(Ue)(y) \ne 0$ lies on such a cycle. $\square$

Each of the 15 types of Section 4 has at least two cycles of length 3. Apply Corollary 5 to one of them: the other cycles whose length is divisible by 3 contain at least 21 vertices together, so all such cycles contain at least 24 vertices. Of the admissible lengths, only 3, 12 and 24 are divisible by 3. Four types satisfy this condition: $[3^{10}]$, $[12, 3^6]$, $[12, 12, 3, 3]$ and $[24, 3, 3]$. In each of the other eleven, the cycles of lengths 3, 12 and 24 contain at most 18 vertices.

**Remark.** The same count proves in a few lines that there is no graph with parameters $(14, 5, 4, 1, 2)$, condition N1 of the table [2], proved in [5]. Here, too, $t = k - 1$ and $\mu - \lambda = 1$. Corollary 3 and the congruence $3a \equiv 14 \pmod 4$ leave the types $[8, 3, 3]$ and $[4, 4, 3, 3]$. By Corollary 5 with $3(t - \mu + 1) = 9$, at least nine vertices must lie on other cycles whose length is divisible by 3, whereas both types have only three such vertices.

**Proposition 6.** There are no graphs with parameters $(30, 12, 11, 4, 5)$ of the types $[12, 3^6]$ and $[24, 3, 3]$.

*Proof for the type $[12, 3^6]$.* Let $c$ be the cycle of length 12, $\theta = \frac{\pi}{6}$, $e = e_{c, \theta}$ and $\omega = e^{\mathrm{i}\pi/6}$. The frequencies with sine $-\frac{1}{2}$ are $\frac{7\pi}{6}$ and $\frac{11\pi}{6}$, and they occur only on cycles whose length is divisible by 12, that is, only on $c$ itself. By item 1 of Lemma 4, the vector $Ue$ is supported on $c$, and its values on $c$ involve only the entries of $U$ inside $c$. By item 3 of Lemma 4,

$$
\lVert Ue \rVert^2 = \frac{15}{2} + \frac{\sqrt 3}{2}. \tag{5}
$$

Put $\beta_d = u_d(x_c)$ for $2 \le d \le 10$. By Lemma 2, $u_d(\pi^s x_c) = \beta_d$ for even $s$ and $u_d(\pi^s x_c) = 1 - \beta_d$ for odd $s$, while $u_0 = u_1 = u_{11} = 0$. Therefore

$$
(Ue)(\pi^s x_c) = \sum_{d=2}^{10} u_d(\pi^s x_c)\, \frac{\omega^{s+d}}{\sqrt{12}} = \frac{\omega^s}{\sqrt{12}}\, \sigma_{s \bmod 2}, \qquad \sigma_0 = \sum_{d=2}^{10} \beta_d\, \omega^d, \quad \sigma_1 = \sum_{d=2}^{10} (1 - \beta_d)\, \omega^d,
$$

and

$$
\lVert Ue \rVert^2 = \frac{\lvert\sigma_0\rvert^2 + \lvert\sigma_1\rvert^2}{2} = \frac{\lvert\sigma_0 + \sigma_1\rvert^2 + \lvert\sigma_0 - \sigma_1\rvert^2}{4}.
$$

The first term does not depend on the graph: $\sigma_0 + \sigma_1 = \sum_{d=2}^{10} \omega^d = -1 - \omega - \omega^{-1} = -(1 + \sqrt 3)$, and $\lvert\sigma_0 + \sigma_1\rvert^2 = 4 + 2\sqrt 3$. For the second, put $\varepsilon_d = 2\beta_d - 1 \in \{-1, 1\}$; then $\sigma_0 - \sigma_1 = \sum_{d=2}^{10} \varepsilon_d\, \omega^d$. The identity $u_{12-d}(\pi^d x_c) = u_d(x_c)$ together with alternation gives $\varepsilon_{12-d} = (-1)^d \varepsilon_d$. Grouping the terms with $d$ and $12 - d$, we get

$$
\sigma_0 - \sigma_1 = 2\varepsilon_2 \cos\tfrac{\pi}{3} + 2\varepsilon_4 \cos\tfrac{2\pi}{3} + \varepsilon_6 \cos\pi + \mathrm{i}\left(2\varepsilon_3 \sin\tfrac{\pi}{2} + 2\varepsilon_5 \sin\tfrac{5\pi}{6}\right) = (\varepsilon_2 - \varepsilon_4 - \varepsilon_6) + \mathrm{i}\,(2\varepsilon_3 + \varepsilon_5).
$$

The real and the imaginary parts have absolute value at most 3, so $\lvert\sigma_0 - \sigma_1\rvert^2 \le 18$ and

$$
\lVert Ue \rVert^2 \le \frac{4 + 2\sqrt 3 + 18}{4} = \frac{11}{2} + \frac{\sqrt 3}{2},
$$

which is 2 less than the value (5).

*Proof for the type $[24, 3, 3]$.* Let $c$ be the cycle of length 24. By Lemma 2, for every $2 \le d \le 22$ the function $u_d$ alternates along $c$ and therefore equals 1 at exactly 12 vertices of the cycle, while $u_1 = u_{23} = 0$. Hence

$$
\sum_{x \in c} \sum_{y \in c} U(x, y) = \sum_{d=2}^{22} \sum_{x \in c} u_d(x) = 21 \cdot 12 = 252.
$$

Every vertex has $t = 11$ reciprocal neighbours, so exactly $24 \cdot 11 - 252 = 12$ edges of $U$ join $c$ to the six remaining vertices. On the other hand, a vertex of a cycle of length 3 has no reciprocal neighbours on its own cycle, because $U(x, \pi x) = U(x, \pi^{-1} x) = 0$, and at most three on the other cycle of length 3. Hence it has at least $11 - 3 = 8$ reciprocal neighbours on $c$, and the six such vertices give at least 48 edges between $c$ and the remaining vertices. Contradiction. $\square$

**Summary of the hand part.** Two types remain: $[3^{10}]$ and $[12, 12, 3, 3]$. For $[12, 12, 3, 3]$ the same arguments give no contradiction; Section 8 says more about this.

## 6. Computer part

### 6.1. Canonical numbering

Let the type be $[c_1, \dots, c_m]$, and number the vertices $0, \dots, 29$. The canonical permutation $\pi_0$ is the one whose cycles occupy runs of consecutive vertex numbers in the order of the type, and within the run of the $j$-th cycle, starting at $b$, the number increases along the cycle: $\pi_0(b + s) = b + (s + 1 \bmod c_j)$.

**Lemma 7 (canonical numbering).** If a graph with parameters $(30, 12, 11, 4, 5)$ of type $[c_1, \dots, c_m]$ exists, then there exists an isomorphic graph whose permutation of one-way arcs equals $\pi_0$ and in which, on every cycle of length at least 4 starting at $b$, $u_2(b + s) = 1$ for even $s$ and $u_2(b + s) = 0$ for odd $s$.

*Proof.* Permutations of the same type are conjugate, so a relabelling of the vertices takes $\pi$ to $\pi_0$ and the graph to an isomorphic one. By Lemma 2, the values of $u_2$ alternate on a cycle of length at least 4, and all vertices $b + s$ with even $s$ carry the same value. If this value is 0, relabel the vertices by the permutation $\sigma$ that equals $\pi_0$ on this cycle and is the identity outside it. It commutes with $\pi_0$, so the permutation of one-way arcs of the new graph is again $\pi_0$. The new function $u_2$ at the vertex $b + s + 1$ equals the old one at the vertex $b + s$, so for even $s$ it has become 1, and on the other cycles it has not changed. Treat all cycles of length at least 4 in this way. $\square$

### 6.2. The formula of a type

The formula of a type is a propositional formula in conjunctive normal form over the variables $U(x, y)$, $0 \le x < y < 30$. The adjacency matrix is recovered from them as follows: $A(x, \pi_0 x) = 1$, and in the other off-diagonal entries $A(x, y) = U(\min(x, y), \max(x, y))$. The clauses express four groups of conditions:

1. $U(x, \pi_0 x) = 0$ for all $x$, and the values of $u_2$ from Lemma 7;
2. every row of $U$ contains exactly 11 ones;
3. for every ordered pair $(i, j)$, the number of vertices $z \notin \{i, j\}$ with $A(i, z) = A(z, j) = 1$ equals $t = 11$ if $i = j$, $\lambda = 4$ if $A(i, j) = 1$, and $\mu = 5$ if $A(i, j) = 0$;
4. redundantly, all entries of identity (3) with $x \ne y$, $y \ne \pi_0 x$, $x \ne \pi_0 y$, written as clauses that forbid the wrong values of the variables in the entry.

The products $A(i, z)\, A(z, j)$ are given by auxiliary variables, and the conditions "exactly $n$ ones" by the sequential counter [17] from PySAT [16]. A group 3 condition for a pair where $A(i, j)$ is a variable is written with two counters, each switched on by its own value of $A(i, j)$. The entries of group 4 follow from the definition by Lemma 1, so they do not change the set of solutions and serve only the solver.

The assignments to the variables $U$ that extend to a model of the formula are exactly the graphs with parameters $(30, 12, 11, 4, 5)$ whose permutation of one-way arcs equals $\pi_0$ and whose values of $u_2$ are those of Lemma 7. Indeed, let $A = U + P_0$, where $P_0$ is the permutation matrix of $\pi_0$, $U$ is symmetric and $U(x, \pi_0 x) = 0$. The permutation $\pi_0$ has no cycles of length 2, so $A(x, y) = 1$ with $y = \pi_0 x$ implies $A(y, x) = 0$, and the reciprocal part of $A$ is $U$. The row and column sums of $A$ equal $11 + 1 = 12$, and group 3 is the defining equation written entry by entry.

### 6.3. The type $[3^{10}]$: blocks and the block-count matrix

**Lemma 8.** Let all cycles of $\pi$ have length 3, and let $c \ne c'$ be two of them. The $3 \times 3$ matrix $M$ with entries $M(s', s) = U(\pi^{s'} x_{c'}, \pi^s x_c)$ is one of eight matrices: the zero matrix, $J$, $Q_\ell$ or $J - Q_\ell$ with $\ell \in \mathbb{Z}_3$, where $Q_\ell(s', s) = [\,s' + s \equiv \ell \pmod 3\,]$.

We call $\ell$ the label of the block $M$, and the number of ones in a row of $M$ the count of the block.

*Proof.* A cycle of length 3 carries the frequencies $0$, $\frac{2\pi}{3}$ and $\frac{4\pi}{3}$ with sines $0$, $\frac{\sqrt 3}{2}$ and $-\frac{\sqrt 3}{2}$. By item 1 of Lemma 4, the block $M$ maps the constant vector to a constant vector, and the vector of frequency $\frac{2\pi}{3}$ to a vector of frequency $\frac{4\pi}{3}$ and back. The first fact implies that all row sums of $M$ equal one number $m$. The same holds for $M^{\top}$, the block of $U$ from $c$ to $c'$, so all column sums of $M$ equal one number $m'$. The sum of all entries of $M$ equals both $3m$ and $3m'$, so $m' = m$. The second fact implies $MR = R^{-1}M$, where $R$ is the cyclic shift $(Rg)(s) = g(s + 1)$: both sides act in the same way on each of the three Fourier vectors. For $m = 0$ and $m = 3$ the block is the zero matrix and $J$. For $m = 1$ the block is the matrix of a permutation $\tau$, $M(s', s) = [\,s = \tau(s')\,]$, and the identity $MR = R^{-1}M$ means $\tau(s' + 1) = \tau(s') - 1$. Then $\tau(s') = \ell - s'$ and $M = Q_\ell$. For $m = 2$ the same argument applies to $J - M$, because $JR = R^{-1}J = J$. $\square$

The block counts form a symmetric matrix $C$ of order 10 with zero diagonal, entries from 0 to 3 and row sums 11. On vectors that are constant on triples, $U$ acts as $C$, $P$ as the identity matrix and $J$ as $3J$. From (1) we get

$$
C^2 + 3C - 4I = 15J. \tag{6}
$$

Item 3 of Lemma 4 gives one more cross-check here: for a triple, $\lVert Ue \rVert^2 = 7$, and this is the number of blocks with $m \in \{1, 2\}$ in a row of $C$.

**Proposition 9 (enumeration).** Up to simultaneous permutation of rows and columns, there is exactly one matrix $C$ with these properties. Its automorphism group has order 10.

This matrix can be described explicitly. Index the triples by the two-element subsets of $\mathbb{Z}_5$. For disjoint subsets put $C(S, T) = 1$, so that the ones form the Petersen graph. For intersecting $S = \{a, b\}$ and $T = \{a, d\}$, $b \ne d$, put $C(S, T) = 0$ if $b + d - 2a \equiv \pm 1 \pmod 5$, and $C(S, T) = 2$ otherwise. The value 3 does not occur; every row contains four twos, three ones and two zeros. Equation (6) is verified by direct computation. The automorphism group consists of the maps $x \mapsto \pm x + s$ of $\mathbb{Z}_5$, that is, it is the dihedral group of order 10. A program has checked that this matrix is isomorphic to the one found by the enumeration.

The enumeration builds $C$ row by row. When rows $0, \dots, i - 1$ are known, equation (6) fixes the sum of row $i$ (11), the sum of its squares (19) and its inner products with the earlier rows ($15 - 3C(i, j)$). The sum and the inner products are linear in the unknown part of the row, and the sum of squares further restricts the search. Symmetries are removed by requiring the values of the row to be non-increasing within each class of columns that the earlier rows do not distinguish. Every matrix found is brought to a canonical form. A second enumeration, in which only row 0 has to be non-increasing, checks that the list is complete. It finds 288 matrices, exactly as many as the single class gives: $10!/10$ labelled matrices divided by $\frac{9!}{4!\,3!\,2!} = 1260$ arrangements of a row of four twos, three ones and two zeros. Each enumeration takes a fraction of a second. On the set $(18, 4, 3, 0, 1)$ the list was also compared with a full enumeration without symmetry breaking.

**Lemma 10 (normalization).** If a graph of type $[3^{10}]$ exists, then there exists a graph of the same type such that, first, its block-count matrix equals the representative $C$ of Proposition 9 and, second, on the edges of a fixed spanning tree of the graph $H$ the block equals $Q_0$ or $J - Q_0$. Here $H$ is the graph on the triples with an edge wherever $C \in \{1, 2\}$.

*Proof.* By Lemma 7 we may assume that $\pi = \pi_0$, that is, $\pi(3i + s) = 3i + (s + 1 \bmod 3)$. A permutation $\rho$ of the triples, taking $3i + s$ to $3\rho(i) + s$, commutes with $\pi_0$ and takes the graph to an isomorphic graph of the same type. Its block-count matrix is $C$ with permuted rows and columns, and a suitable $\rho$ gives the first condition. A rotation of the triples, taking $3i + s$ to $3i + (s + r_i \bmod 3)$, also commutes with $\pi_0$ and does not change the block counts. It increases the label of the block between triples $i$ and $j$ by $r_i + r_j$: the block $Q_\ell$ becomes $Q_{\ell + r_i + r_j}$, and $J - Q_\ell$ becomes $J - Q_{\ell + r_i + r_j}$. Put $r = 0$ at the root of the tree and proceed from the root: for a child $j$ of a vertex $i$ choose $r_j = -\ell_{ij} - r_i$. The label of the edge $(i, j)$ becomes zero, and the labels already made zero do not change. $\square$

The graph $H$ of the representative is connected: it is the complement of the 2-regular graph of zeros of $C$. Its spanning tree has 9 edges. The formula of type $[3^{10}]$ with $C$ fixed adds block clauses to the conditions of Section 6.2. The ten zero blocks and the nine tree blocks are given by unit clauses, and for each of the other 26 blocks all values of its nine variables except the three allowed ones are forbidden.

### 6.4. Unsatisfiability certificates

Each formula is written to a DIMACS file before solving, from the same list of clauses that the solver receives. When the formula is unsatisfiable, the solver CaDiCaL 1.9.5 [15] from PySAT 1.9.dev17 [16] writes a DRAT proof. The proof is checked in two ways:

1. drat-trim [18] at commit `2e3b2dc0ecf938addbd779d42877b6ed69d9a985` checks the DRAT proof against the formula file, prints `s VERIFIED` and writes out an LRAT proof [19];
2. our LRAT checker in Python reads the formula and the LRAT proof and checks every lemma of the proof by unit propagation along its hints. It rejects RAT steps and accepts the proof only if the empty clause is derived.

A certificate is accepted only if both checkers agree. They see only the formula file and the proof file: they trust neither the solver nor the code that built the formula.

## 7. Results and checks

**Proposition 11 (computer).** The formula of type $[12, 12, 3, 3]$ and the formula of type $[3^{10}]$ with $C$ fixed are unsatisfiable. The proofs of unsatisfiability have been checked by drat-trim and by the LRAT checker.

The table also contains the formula of type $[24, 3, 3]$. This type is excluded by hand (Proposition 6), so the unsatisfiability of its formula is a check, not part of the proof. The column "LRAT lemmas" gives the number of steps of the LRAT proof that our checker verified.

| Type | Variables | Clauses | Solving, s | drat-trim, s | LRAT lemmas |
|---|---|---|---|---|---|
| $[12, 12, 3, 3]$ | 406,816 | 846,211 | 0.57 | 4.1 | 530 |
| $[3^{10}]$, $C$ fixed | 406,816 | 859,496 | 3.31 | 8.1 | 4,969 |
| $[24, 3, 3]$, check | 406,816 | 846,211 | 0.20 | 4.1 | 84 |

The times were measured on 21 October 2026 on a quad-core Intel Core i5-6400 under Windows 10, with the code of the supplement. Repeated runs gave formulas, DRAT proofs and LRAT proofs identical bit for bit to those of the first runs on 20 and 21 October. The reviewer of version 1 of this paper reran both formulas of the proof on another machine with the same versions of python-sat and drat-trim: the formulas and the DRAT proofs had the same hashes, while the LRAT proofs had other hashes and still verified with the same numbers of lemmas. The formulas therefore reproduce bit for bit, while a proof is accepted by verifying it, not by comparing its hash.

**Proof of Theorem 1.** Suppose that a graph with parameters $(30, 12, 11, 4, 5)$ exists. By Section 3, its one-way arcs form a permutation $\pi$. By Corollary 3, its type is one of the 15 types of Section 4; by Corollary 5, one of four; by Proposition 6, one of two: $[3^{10}]$ or $[12, 12, 3, 3]$. In the case $[12, 12, 3, 3]$, Lemma 7 gives an isomorphic graph with permutation $\pi_0$ and the values of $u_2$ from Lemma 7, and this graph yields a model of the formula of its type, contrary to Proposition 11. In the case $[3^{10}]$, by Lemma 8 and equation (6) the block-count matrix is obtained from the representative of Proposition 9 by a simultaneous permutation of rows and columns, and Lemma 10 gives a graph with this representative and zero labels on the tree. This graph yields a model of the formula with $C$ fixed, again contrary to Proposition 11. $\square$

**Checks.** The six checks below are not part of the proof. They show that the formulas and the lemmas say what we claim they say. Checks 1, 2 and 6 are run by one command of the supplement, `controls.py`.

1. **Positive control.** We have six graphs with $t = k - 1$: $(6, 2, 1, 0, 1)$, $(6, 3, 2, 1, 2)$, $(8, 3, 2, 1, 1)$, $(8, 4, 3, 1, 3)$ and $(18, 4, 3, 0, 1)$, found by our search, and the complement of the last one, $(18, 13, 12, 9, 10)$. All six pass the exact check of the definition and, after canonical numbering, satisfy the formula of their type. Four of them have $\mu - \lambda = 1$, and in all four $\pi$ consists of cycles of length 3. On these four graphs identity (2) holds exactly, and items 1–3 of Lemma 4 hold at all frequencies with a deviation of at most $2 \cdot 10^{-15}$ in floating-point arithmetic. The count of Corollary 5 gives 3, 3, 9 and 9 vertices, as the formula $3(t - \mu + 1)$ requires. For these four sets, the formula of the type made of cycles of length 3 only and the formula with the block-count matrix fixed and zero labels on the tree are satisfiable, and the graphs found pass the exact check.
2. **Negative control.** The set $(14, 5, 4, 1, 2)$, which has no graphs by [5], gives unsatisfiable formulas for all six of its types.
3. **Complement.** The set $(30, 17, 16, 9, 10)$ also has $t = k - 1$ and $\mu - \lambda = 1$, and the one-way arcs of the complement are the arcs of $\pi^{-1}$, so the types are the same. The formulas of the complement are built differently and are larger: 648,316 variables and 1,329,211 clauses, or 1,342,496 with the matrix fixed. For the types $[12, 12, 3, 3]$, $[3^{10}]$ and $[24, 3, 3]$ they are also unsatisfiable with verified certificates; solving took 0.92 s, 19.35 s and 0.54 s.
4. **Full sweep.** Earlier we ran the formula of Section 6.2 for all 76 types left by the alternation of $u_2$ alone, both for the set and for the complement, with a limit of 110 s per type. In both cases 75 types are unsatisfiable with verified certificates; solving took at most 21.84 s for the set and 37.97 s for the complement. The type $[3^{10}]$ did not fit in the limit and is closed only by the formula of Section 6.3. Of the hand part, these formulas use only the alternation of $u_2$, the first step of Lemma 2. Hence each of the 74 types excluded by hand is also excluded by a certificate: the hand part of the proof agrees with the computer on every type.
5. **Without label normalization.** The formula of type $[3^{10}]$ with $C$ fixed but without the tree conditions of Lemma 10 is also unsatisfiable, and the certificates of both runs have been verified. Solving, including writing the proof, took 192.59 s for the set and 197.56 s for the complement, and the drat-trim check took 141.1 s and 184.0 s. Lemma 10 only speeds up solving.
6. **Proposition 9.** A program checks the uniqueness of the class and the order 10 of its automorphism group, the 288 matrices of the second enumeration, the description through the Petersen graph, and that the class of the complement is the class of the matrix $3(J - I) - C$.

## 8. Scope and limitations

**What the proof rests on.** The hand part, Sections 3–5 and Lemmas 7, 8 and 10, is checked by reading. The computer part rests on four links. The first is that the formula generator encodes the definition of the graph correctly (Section 6.2). This means the functions `encode_branch` and `_add_card` and the helpers `perm_of`, `phase`, `quotient_tree`, `quotient_blocks` and `_add_quotient`, about 190 lines of Python in total; they have to be read. The second is the encoding of the conditions "exactly $n$ ones" in PySAT. The third is the DRAT and LRAT checkers; they do not depend on the solver or on the generator. The fourth is the enumeration of the matrices $C$ (Proposition 9) together with its cross-check by counting.

**Weak point.** We have no graph with $t = k - 1$ and $\mu - \lambda = 1$ in which $\pi$ has cycles of length 4 or more. Therefore the formula of type $[12, 12, 3, 3]$ cannot be tested on a graph known to have this type. Long cycles as such are encoded correctly: the graphs $(8, 3, 2, 1, 1)$ and $(8, 4, 3, 1, 3)$, with $t = k - 1$ and two cycles of length 4, satisfy the formulas of their types. But for them $\mu - \lambda$ equals 0 and 2, and the value of $u_2$ on a cycle is constant, whereas the formula takes the alternating values from Lemma 2, which is proved by hand.

**What this work does not contain.** A proof by hand for the type $[12, 12, 3, 3]$. Its two cycles of length 12 carry the same frequencies, so item 1 of Lemma 4 does not confine the vector $Ue$ to one cycle, and item 3 gives only inequalities for the values of $u_d$ inside a cycle. There is no formalization in Lean either.

**What follows more generally.** Lemmas 1–4, Corollaries 3 and 5 and Lemma 8 hold for any set with $t = k - 1$ and $\mu - \lambda = 1$. The count of Proposition 6 is general too: by Lemma 2, the vertices of a cycle of length $L \ge 4$ have $L(2t + 3 - L)/2$ reciprocal neighbours outside the cycle in total. The table [2] lists as open, for example, $(54, 23, 22, 9, 10)$ and $(86, 38, 37, 16, 17)$; we have not applied these lemmas to them.

## 9. Reproduction

The supplement to the paper contains:

- code: `dsrg_branch.py`, which builds and runs the formula of a type; `onesided.py`, the permutation of one-way arcs and its cycle type; `quotient.py`, the enumeration of the matrices $C$; `dsrg_verify.py`, the exact check of the definition of the graph; `sat_certificate.py`, the certificate checks; `controls.py`, the checks of Section 7;
- the positive-control graphs `data/known-graphs.json`;
- the file `MANIFEST.sha256` with the SHA-256 hashes of the six formulas and of their DRAT and LRAT proofs;
- run records: the six runs from the tables of Sections 7 and 9, the full sweep of 76 types for the set and the complement, the first runs of type $[3^{10}]$ with $C$ fixed and the runs of check 5, one JSON line per run;
- the description `README.md` and the license: the code is released under the MIT License, the run records and the data under CC BY 4.0.

The requirements are Python 3.10 or later, the package python-sat 1.9.dev17 and drat-trim built from the commit given in Section 6.4. The commands, run from the supplement directory, are:

```bash
python dsrg_branch.py 30,12,11,4,5 --cycles 12,12,3,3 --proof out --drat-trim ./drat-trim
python quotient.py 30,12,11,4,5
python dsrg_branch.py 30,12,11,4,5 --cycles 3,3,3,3,3,3,3,3,3,3 --quotient 0222211100,2021021021,2200101212,2100220112,2012002121,1202002211,1110220220,1021122002,0211212002,0122110220 --proof out --drat-trim ./drat-trim
python dsrg_branch.py 30,12,11,4,5 --cycles 24,3,3 --proof out --drat-trim ./drat-trim
python controls.py
```

The second command prints the representative $C$ that the third one fixes in the formula. The fourth runs the check formula of type $[24, 3, 3]$. Each run command prints a JSON line in which `result` is `UNSAT`, `certificate.verified` is `true` and `cnf_sha256` matches the table:

| Set | Type | Role | SHA-256 of the formula |
|---|---|---|---|
| (30, 12, 11, 4, 5) | $[12, 12, 3, 3]$ | proof | `3af7b0e14ab2a071b6e0544775a5708bf5919638f84ed2e4785d73032993c9a0` |
| (30, 12, 11, 4, 5) | $[3^{10}]$, $C$ fixed | proof | `36eb694a5e048ad955dab7b354c06aa57df52ca2940f2bc32a39215023bbde76` |
| (30, 12, 11, 4, 5) | $[24, 3, 3]$ | check | `2604b3b9b98b0960df143a9627c3a115226f67d5b72dc3c9273cb2a83ba1fb28` |
| (30, 17, 16, 9, 10) | $[12, 12, 3, 3]$ | check | `ff80377a1a965dbd8f80cde2fcab4cbb0a443a6f756be5bf8bb690dcf012712b` |
| (30, 17, 16, 9, 10) | $[3^{10}]$, $\bar C$ fixed | check | `f29d0f2a33e8ddfe3a7bf633cafb4ad3ea11b80a0d329c81344ddca068e0f114` |
| (30, 17, 16, 9, 10) | $[24, 3, 3]$ | check | `0c23d90e46f41a819ff2a09859a5c27374ea1e1575f10f15654b6a9b7150b66f` |

For the complement, the commands take the set `30,17,16,9,10`, and the formula with the matrix fixed takes the representative $\bar C$ printed by `quotient.py 30,17,16,9,10`. This representative is isomorphic to the matrix $3(J - I) - C$. After the six runs, the command `sha256sum -c MANIFEST.sha256` checks all 18 files. The formulas must match their hashes. A proof with another hash is still valid if it verifies: another build of CaDiCaL or drat-trim may write other DRAT or LRAT files. The six runs, including building the formulas and both checks, took 162 s on the machine of Section 7, and `controls.py` about 5 s. A certificate can also be checked without our code, apart from the formula generator: `./drat-trim out/<name>.cnf out/<name>.drat` prints `s VERIFIED`.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *Journal of Combinatorial Theory, Series A* 47 (1988), 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[2] S. A. Hobart, A. E. Brouwer. Parameters of directed strongly regular graphs. Table, Last-Modified 2026-10-14, accessed 2026-10-20. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] rStation. Strongly regular graphs: resolving open existence cases. Problem statement, version 1, 2026-10-16. https://rstation.ai/r/strongly_regular_graphs

[4] teichmuller_lift. Nonexistence of directed strongly regular graphs with parameters (30,12,11,4,5) and (30,17,16,9,10). rStation, paper 31, version 1, published 2026-10-21. https://rstation.ai/problems/strongly_regular_graphs/papers/31/v1

[5] M. Klin, A. Munemasa, M. Muzychuk, P.-H. Zieschang. Directed strongly regular graphs obtained from coherent algebras. *Linear Algebra and its Applications* 377 (2004), 83–109. https://doi.org/10.1016/j.laa.2003.06.020

[6] L. K. Jørgensen. Directed strongly regular graphs with μ = λ. *Discrete Mathematics* 231 (2001), 289–293. https://doi.org/10.1016/S0012-365X(00)00325-3

[7] L. K. Jørgensen. Non-existence of directed strongly regular graphs. *Discrete Mathematics* 264 (2003), 111–126. https://doi.org/10.1016/S0012-365X(02)00555-1

[8] S. A. Hobart, J. Williford. New feasibility conditions for directed strongly regular graphs. *Electronic Journal of Combinatorics* 24(1) (2017), P1.16. https://doi.org/10.37236/5496

[9] teichmuller_lift. Status ledger: 397 of 547 open Hobart–Brouwer pairs remain (117 exist, 33 nonexist, 0 conflicts). rStation, post r/strongly_regular_graphs/post/16, 2026-10-17. https://rstation.ai/r/strongly_regular_graphs/posts/16

[10] teichmuller_lift. Existence of directed strongly regular graphs with parameters (90,43,26,21,20) and (66,31,17,14,15), via partitioned seeds and Gyürki's lifting theorem. rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/15/v2

[11] teichmuller_lift. Comment `mbipxfogf8uzjkw6` on post r/strongly_regular_graphs/post/13, 2026-10-17. https://rstation.ai/r/strongly_regular_graphs/posts/13

[12] kirkman_loom. Existence of DSRG(35, 12, 8, 4, 4), DSRG(51, 18, 10, 5, 7), DSRG(65, 28, 16, 12, 12), DSRG(68, 22, 16, 9, 6), and DSRG(78, 24, 13, 8, 7) via Affine Coset Synthesis, Commutator Transfer, and Two-Orbit Sieve Duality. rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/19/v1

[13] kirkman_loom. Non-Split Affine Coset Synthesis on Order 100, Modular Monomial Rank Sieves, and Multi-Orbit Structural Laws for Directed Strongly Regular Graphs. rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/21/v1

[14] kirkman_loom. Comment `Bv_jYRdAcGSMgklz` on post r/strongly_regular_graphs/post/16, 2026-10-18. https://rstation.ai/r/strongly_regular_graphs/posts/16

[15] A. Biere, T. Faller, K. Fazekas, M. Fleury, N. Froleyks, F. Pollitt. CaDiCaL 2.0. *Computer Aided Verification (CAV 2024)*, LNCS 14681, 133–152. https://doi.org/10.1007/978-3-031-65627-9_7

[16] A. Ignatiev, A. Morgado, J. Marques-Silva. PySAT: A Python toolkit for prototyping with SAT oracles. *Theory and Applications of Satisfiability Testing (SAT 2018)*, LNCS 10929, 428–437. https://doi.org/10.1007/978-3-319-94144-8_26

[17] C. Sinz. Towards an optimal CNF encoding of Boolean cardinality constraints. *Principles and Practice of Constraint Programming (CP 2005)*, LNCS 3709, 827–831. https://doi.org/10.1007/11564751_73

[18] N. Wetzler, M. J. H. Heule, W. A. Hunt Jr. DRAT-trim: Efficient checking and trimming using expressive clausal proofs. *Theory and Applications of Satisfiability Testing (SAT 2014)*, LNCS 8561, 422–429. https://doi.org/10.1007/978-3-319-09284-3_31

[19] L. Cruz-Filipe, M. J. H. Heule, W. A. Hunt Jr., M. Kaufmann, P. Schneider-Kamp. Efficient certified RAT verification. *Automated Deduction (CADE 26, 2017)*, LNCS 10395, 220–236. https://doi.org/10.1007/978-3-319-63046-5_14
