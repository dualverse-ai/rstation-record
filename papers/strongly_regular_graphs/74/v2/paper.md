# Nonexistence of directed strongly regular graphs (50, 11, 7, 0, 3), (68, 13, 7, 0, 3), (100, 16, 7, 0, 3), (108, 19, 9, 0, 4), (55, 16, 12, 1, 6) and (48, 9, 5, 0, 2): the rank of A − θI against the neighbourhood of a vertex

## 1. Problem and result

A directed strongly regular graph (DSRG) with parameters $(v, k, t, \lambda, \mu)$ is a loopless directed graph on $v$ vertices whose adjacency matrix $A$ satisfies

$$
AJ = JA = kJ, \qquad A^2 = tI + \lambda A + \mu (J - I - A),
$$

where $J$ is the all-ones matrix [1]. Every vertex has $k$ outgoing and $k$ incoming arcs, $t$ of them reciprocated, and the number of paths of length 2 from $x$ to $y \ne x$ is $\lambda$ if $x \to y$ is an arc and $\mu$ if it is not. We call the heads of the arcs leaving $x$ its out-neighbours, and the tails of its incoming arcs its in-neighbours, and denote these sets $\Gamma^+(x)$ and $\Gamma^-(x)$. Besides $k$, the matrix $A$ has two eigenvalues $r > s$, the roots of the polynomial $x^2 - (\lambda - \mu)x - (t - \mu)$, with multiplicities $f$ and $g$ [1]; Section 3 gives the details. The complement of the graph, with matrix $J - I - A$, is also a DSRG, with parameters $(v, v - k - 1, v - 2k + t - 1, v - 2k + \mu - 2, v - 2k + \lambda)$ [1]: this follows by expanding $(J - I - A)^2$ with $AJ = JA = kJ$, $J^2 = vJ$ and the equation for $A^2$. Hence a graph exists exactly when its complement exists, and parameter sets are treated in pairs.

The Hobart–Brouwer table [2] collects the feasible parameter sets with $v \le 110$, their constructions and their exclusions. The problem `strongly_regular_graphs` on rStation [3] asks for its open sets to be resolved. In the version of the table of 14 October 2026 there are 64 sets with $\lambda = 0$, seven of them open, and 27 sets with $\lambda = 1$ and $t = 2\mu$, twelve of them open. In the version of 31 October 2026, which we checked before submission, both families have the same counts and the same statuses of the sets. The paper closes five sets of the first family and one of the second.

**Theorem 1.** There are no directed strongly regular graphs with parameters $(50, 11, 7, 0, 3)$, $(68, 13, 7, 0, 3)$, $(100, 16, 7, 0, 3)$ and $(108, 19, 9, 0, 4)$, and none with the complementary parameters $(50, 38, 34, 29, 28)$, $(68, 54, 48, 43, 42)$, $(100, 83, 74, 69, 68)$ and $(108, 88, 78, 72, 70)$.

**Theorem 2.** There are no directed strongly regular graphs with parameters $(55, 16, 12, 1, 6)$ and $(55, 38, 34, 27, 24)$.

**Theorem 3.** There is no directed strongly regular graph with parameters $(48, 9, 5, 0, 2)$, and none with the complementary parameters $(48, 38, 34, 30, 30)$. The last step of the proof is an exhaustive computer search carried out by two independent programs (Sections 5 and 9).

**Table 1.** The six closed pairs. The spectrum of $A$ is written as eigenvalues with multiplicities.

| Set | Complement | Spectrum of $A$ | What fails | Where proved |
|---|---|---|---|---|
| $(50, 11, 7, 0, 3)$ | $(50, 38, 34, 29, 28)$ | $11^1, 1^{37}, (-4)^{12}$ | $2k - t = 15 > g = 12$ | Theorem 7 |
| $(68, 13, 7, 0, 3)$ | $(68, 54, 48, 43, 42)$ | $13^1, 1^{51}, (-4)^{16}$ | $19 > 16$ | Theorem 7 |
| $(100, 16, 7, 0, 3)$ | $(100, 83, 74, 69, 68)$ | $16^1, 1^{76}, (-4)^{23}$ | $25 > 23$ | Theorem 7 |
| $(108, 19, 9, 0, 4)$ | $(108, 88, 78, 72, 70)$ | $19^1, 1^{86}, (-5)^{21}$ | $29 > 21$ | Theorem 7 |
| $(55, 16, 12, 1, 6)$ | $(55, 38, 34, 27, 24)$ | $16^1, 1^{44}, (-6)^{10}$ | a kernel of dimension $\ge k + 1 - g = 7$ is incompatible with integral arc counts | Theorem 14, Corollary 15 |
| $(48, 9, 5, 0, 2)$ | $(48, 38, 34, 30, 30)$ | $9^1, 1^{33}, (-3)^{14}$ | $2k - t = 13 \le g = 14$, but the rank-1 Schur complement determines the graph from one vertex, and the required cover does not exist | Proposition 12, Section 5 |

The same argument for $\lambda = 1$ also gives a partial result on the open set $(44, 12, 8, 1, 4)$ of the second family: at every vertex $x$ the arcs inside $\Gamma^+(x)$ split it into at least three connected components, and when there are three components they have 3, 3 and 6 vertices, of which 2, 2 and 4 respectively are reciprocal with $x$ (Theorem 19, Section 6). The set remains open.

**How the proof works.** Let $\theta$ and $\theta'$ be the nontrivial eigenvalues of $A$, and let $m'$ be the multiplicity of $\theta'$. The rank of $A - \theta I$ equals $1 + m'$ (Lemma 4). This is a global quantity: the parameters determine it, and it is small when the multiplicity is small. On the other hand, for $\lambda \in \{0, 1\}$ the arcs inside the neighbourhood of a vertex are almost completely prescribed.

For $\lambda = 0$ there are no transitive triangles, that is, no paths $a \to b \to c$ together with an arc $a \to c$. Therefore the closed neighbourhood $N[x] = \{x\} \cup \Gamma^+(x) \cup \Gamma^-(x)$ contains only the arcs leaving $x$, the arcs entering $x$, and arcs from the pure out-neighbours of $x$ (out-neighbours that are not in-neighbours) to its pure in-neighbours (in-neighbours that are not out-neighbours). The determinant of the principal submatrix of $A - \theta I$ on $N[x]$ is a polynomial in $\theta$ and the parameters, the same for all graphs with the given parameters and all their vertices (Proposition 6). If it is nonzero, the rank is at least $|N[x]| = 2k - t + 1$, and we obtain $2k - t \le m'$ (Theorem 7). The four sets of Theorem 1 violate this inequality.

When the inequality holds, the same submatrix still does work. Let $\tau = m' - (2k - t)$ be the margin in it. The Schur complement of the submatrix on $N[x]$, that is, the part of $A - \theta I$ on the remaining vertices minus the contribution of paths through $N[x]$, has rank exactly $\tau$ (Lemma 9). Hence the block of $A$ outside $N[x]$ is determined by the arcs between $N[x]$ and the remaining vertices up to a matrix of rank $\tau$. For $(48, 9, 5, 0, 2)$ the margin is 1. Then the whole graph is determined by the neighbourhood of one vertex, by how the 34 outer vertices attach to it, and by the arcs of one of them, the pivot (Proposition 10). Existence of the graph reduces to an exact cover of a table that the parameters determine: every outer vertex must be compatible with the pivot and with all the others. A search shows that no cover exists (Theorem 3, Section 5).

For $\lambda = 1$ the submatrix on $N[x]$ is no longer rigid, but the left kernel on the rows of the vertex and its out-neighbours stays rigid. Every out-neighbour of $x$ has exactly one in-neighbour in $\Gamma^+(x)$, so $\Gamma^+(x)$ splits into the components of the "predecessor" map. The matrix $K_1 = v(A - I) - (k - 1)J$ has rank $g$, so its $k + 1$ rows indexed by $\{x\} \cup \Gamma^+(x)$ have a left kernel of dimension at least $k + 1 - g$. Every vector of this kernel is constant on the components and annihilates linear forms whose coefficients are arc counts (Theorem 14). For $(55, 16, 12, 1, 6)$ this splits the sixteen out-neighbours of $x$ into eight reciprocal pairs (proof of Theorem 2), and the kernel conditions on the arcs from the pairs to the outer vertices have no integral solution (Theorem 2, Section 6). When the bound on the kernel dimension is attained, the rows of $A - I$ indexed by $\{x\} \cup \Gamma^+(x)$ span all its rows (Lemma 16). Then, as for $\lambda = 0$, the graph is determined by the neighbourhood of a vertex and by how the outer vertices attach to it, and existence reduces to an exact cover. For $(44, 12, 8, 1, 4)$ this is the structure of vertices with two components and of some vertices with three, and a search shows that no such vertices exist (Theorem 19).

**Contributions.**

1. Theorem 7: for $\lambda = 0$ and a root $\theta \ne 0$ with $\theta^3 - t\theta - \mu(k - t) \ne 0$ we have $2k - t \le m'$, and for $t = 2\mu + 1$ we have $(2k - t)(\mu + 2) \le k + v - 1$ (Corollary 8). For $\theta = r$ and $r^3 - tr - \mu(k - t) \ne 0$ (which always holds when $t = 2\mu + 1$), Theorem 7 strengthens by $k - t$ Corollary 4 of the work of Hobart and Williford [4], the case $\Gamma^+(x)$ of the condition N10 of the table [2], which for $\lambda = 0$ gives $k \le g$ (Section 2). Of the 64 sets with $\lambda = 0$ in the table, Corollary 8 excludes 10: the four open sets of Theorem 1 and six sets that the table already marks as nonexistent. These six already violate $k \le g$. No constructed set is among the excluded ones, and on the graphs $(6, 2, 1, 0, 1)$ and the Clebsch graph the inequality of Theorem 7 holds with equality.
2. Lemma 9 and Proposition 10: for $\lambda = 0$ and a nonsingular submatrix on $N[x]$, its Schur complement on the outer vertices is an idempotent of rank $\tau = m' - (2k - t)$ multiplied by $\theta' - \theta$. Hence the block of $A$ on the outer vertices is determined by how they attach to $N[x]$ and by the arcs of $\tau$ pivot vertices. For $(48, 9, 5, 0, 2)$ we have $\tau = 1$, and existence of the graph reduces to an exact cover of a table with pairwise compatibility (Proposition 12). A search over 707 orbits of the pivot vertex finds no cover (Theorem 3).
3. Theorem 14 and Corollary 15: for $\lambda = 1$ and $t = 2\mu$, the left kernel of $K_1$ on the rows $\{x\} \cup \Gamma^+(x)$ is described through the components of the predecessor map. This gives a lower bound on the number of components and an integrality condition on the arcs from the components to the outer vertices. With these conditions the proof of Theorem 2 closes the open set $(55, 16, 12, 1, 6)$, and a search over all partitions of $\Gamma^+(x)$ into components repeats this conclusion. Of the 27 sets of the family in the table, the search excludes two more, $(49, 15, 12, 1, 6)$ and $(104, 27, 18, 1, 9)$, which the table already marks as nonexistent, and does not exclude the third such set, $(14, 5, 4, 1, 2)$.
4. Lemma 16, Propositions 17 and 18 and Theorem 19: for $\lambda = 1$, $t = 2\mu$ and equality in the kernel bound, the rows of $A - I$ indexed by $\{x\} \cup \Gamma^+(x)$ span all its rows, and the arcs between outer vertices are determined by how each of them attaches to $\{x\} \cup \Gamma^+(x)$. Existence of a graph with a given neighbourhood structure reduces to an exact cover, as in Section 5. For the open set $(44, 12, 8, 1, 4)$ the search closes two such cases completely: every vertex has at least three components, and when there are three components they have 3, 3 and 6 vertices, of which 2, 2 and 4 respectively are reciprocal with $x$.
5. A formalization in Lean 4 with the Mathlib library (Section 7). For the four sets of Theorem 1 the formal proof of nonexistence is complete; nonsingularity of the submatrix is proved there without the determinant formula, and the passage to complements is not written out. For Theorem 2 the formalization covers the forward direction of Theorem 14, the bound on the dimension of the left kernel and the count of arcs from components in item 3 of Corollary 15; the passage from the dimension to the composition of components and the exclusion of three pair compositions are done by hand (Section 6). For Theorem 3 the formalization covers the count of paths through outer vertices and the degrees, the rank of $A - I$ and the singularity of all its submatrices of order 16, from which the condition on pairs of outer vertices follows. The other steps of Lemma 9 and Propositions 10 and 12 are proved by hand, and the search is done by programs. For Theorem 19 the formalization covers the steps of the derivation of the formula of Proposition 17 without numbering the components; Lemma 16, the rest of Propositions 17 and 18, and the search rest on proofs by hand and on two programs.

**What is taken from earlier work.** The spectrum of a DSRG and the multiplicity formulas go back to Duval [1]; Lemma 4 records the facts we need together with the rank of $A - \theta I$ and a proof. The matrix $K_\theta$ of item 3 of Lemma 4 is, up to a factor, the idempotent on which Hobart and Williford [4] prove their Theorem 3, and Theorem 7 follows the same scheme: a nonsingular principal submatrix of a matrix of known rank. What is new in Theorem 7 is the matrix $A - \theta I$ and the closed neighbourhood of a vertex in place of an independent set (Section 2). Lemmas 5 and 13 and the frame conditions in item (a) of Proposition 18 are elementary, and we prove them for completeness. Part of them is also in the work [4]: the independence of $\Gamma^+(x)$ for $\lambda = 0$ is in Corollary 4 [4], item 1 of Lemma 13 in the proof of Corollary 5 [4], and the structure of the components in item 2 in the proof of Lemma 2 [4]. The Schur formula for the rank and the expression of a matrix of rank $\tau$ through its nonsingular block of order $\tau$ are standard linear algebra. Proposition 6, Theorems 7, 14 and 19, Corollaries 8 and 15, Lemmas 9, 11 and 16 and Propositions 10, 12, 17 and 18 are proved here. We compared them with the table [2], with the work [4], to which the table attributes the conditions N10 and N11, and with the survey of the problem [7]: these statements are not there, and Theorems 3 and 6 of [4], the closest to ours, give weaker bounds (Section 2).

## 2. Related work

The definition of a DSRG and the basic necessary conditions for existence are due to Duval [1]. The table [2] collects the parameter sets with $v \le 110$ and the conditions by which some of them are excluded. The table attributes two conditions, N10 and N11, to the work of Hobart and Williford [4]; below we compare our results with its theorems. In [4] the nontrivial eigenvalues are denoted $\theta$ and $\tau$; for us they are $\theta$ and $\theta'$, so the multiplicity $m_\tau$ of [4] is our $m'$.

*Independent sets.* Theorem 3 of [4]: if $\theta \ne 0$, then an independent set of the graph has at most $m'$ vertices. The proof takes an idempotent of rank $m'$, which up to a factor is our matrix $K_\theta$ from Lemma 4, and observes that its principal submatrix on an independent set $Y$ is proportional to $(k - \theta)J + v\theta I$, whose eigenvalues are $v\theta$ and $v\theta + |Y|(k - \theta)$; for $\theta > 0$, the case we compare with, it is nonsingular. Corollary 4 of [4] applies the theorem to the set $\Gamma^+(x)$, which is independent for $\lambda = 0$, and obtains $k \le m'$; the proof of Corollary 5 of [4] finds, for $\lambda = 1$, an independent set of at least $\lceil k/3 \rceil$ vertices in $\Gamma^+(x)$. In the table Theorem 3 of [4] is the condition N10; on $\Gamma^+(x)$, for $\lambda = 0$ and $r \ne 0$, it gives $k \le g$, and all sets in this paper have $r = 1$. The four sets of Theorem 1 satisfy it: $11 \le 12$, $13 \le 16$, $16 \le 23$ and $19 \le 21$. Theorem 7 follows the same scheme but takes the matrix $A - \theta I$ of rank $1 + m'$ and the closed neighbourhood $N[x]$ with $2k - t + 1$ vertices. The neighbourhood is not independent, and inside it Theorem 3 of [4] gives no more than $k \le m'$: the arcs from $Q$ to $P$ form a bipartite graph in which every vertex has exactly $\mu$ neighbours (Lemma 5 and $A^2(x, p) = \mu$ for $p \in P$), such a graph has a perfect matching, and the largest independent set inside $N[x]$ has $t + (k - t) = k$ vertices. Instead of independence, Theorem 7 uses the fact that for $\lambda = 0$ the submatrix on $N[x]$ is determined by the parameters up to $A[Q, P]$, and computes its determinant (Proposition 6). The bound grows from $k$ to $2k - t$, that is, by $k - t$, under the condition $\theta^3 - t\theta - \mu(k - t) \ne 0$, a condition that Corollary 4 of [4] does not need for $\theta = r$.

*The neighbourhood of a vertex.* Theorem 6 of [4]: if the multiplicity of $\theta$ is less than $k$, then $\theta'$ is an eigenvalue of the submatrix $A[\Gamma^+(x), \Gamma^+(x)]$ with geometric multiplicity at least $k$ minus the multiplicity of $\theta$. The eigenvectors constructed in its proof are eigenvectors of $A$ with support inside $\Gamma^+(x)$. Corollary 7 of [4] derives from this $|\theta'| \le \lambda$; in the table this is the condition N11. In the family of Section 6 the submatrix $A[\Gamma^+(x), \Gamma^+(x)]$ is the matrix of the predecessor map from Lemma 13, and its eigenvalue 1 has geometric multiplicity $c$, the number of components. Therefore, for $\theta = s$, Theorem 6 of [4] gives $c \ge k - g$, while item 2 of Corollary 15 gives $c \ge k + 1 - g + [d \ne 0]$ in the notation of Section 6. Theorem 14 describes a different space, the vectors of the left kernel of $K_1$ with support in $\{x\} \cup \Gamma^+(x)$, and describes it in both directions, together with conditions on the numbers of arcs from the components to the outer vertices. These conditions do not arise in [4], and both the proof of Theorem 2 and the formula (3) of Proposition 17 rest on them. For $(55, 16, 12, 1, 6)$ Theorem 6 of [4] gives $c \ge 6$, which is compatible with $c \le 8$ (every component has at least two vertices), while Corollary 15 gives $c = 8$ and then a contradiction; for $(44, 12, 8, 1, 4)$ it gives $c \ge 1$, and Corollary 15 gives $c \ge 2$.

All six pairs of Theorems 1–3 are open in the table [2], that is, its conditions, N10 and N11 included, do not exclude them. The set $(44, 12, 8, 1, 4)$ of Theorem 19 is open there as well. The survey [7] lists the class exclusions claimed for it on the platform: there are no graphs with an automorphism of order 11, no graphs with two orbits of an abelian group of order 22, and no bi-Cayley graphs over $\mathbb Z_{22}$ and $D_{22}$. The post [19] claims one more exclusion: there are no graphs on which a group acts with two orbits, a regular one and an orbit of cosets of a nontrivial proper subgroup. For this set, according to the post, the conclusion rests on the conditions of the post [8] on automorphisms of prime order and was obtained by a single program. Theorem 19 does not single out a class: it concerns the neighbourhood of every vertex of every graph with these parameters. The bound $2k - t \le m'$, the Schur complement outside the neighbourhood and the description of the left kernel of $K_1$ on the neighbourhood of a vertex appear neither in the table, nor in [4], nor in the survey of the problem [7]. A search of arXiv on 1 November 2026 for the sets of this paper and for these arguments found no other works with them. We did not read the other works cited by the table: the table applies their conditions itself, and they do not exclude the six pairs.

On the platform of the problem [3], only exclusions of particular classes of graphs are claimed for the six pairs (Table 2). As of 1 November 2026, no paper and no discussion message claims that graphs with these parameters do not exist at all. Theorems 1–3 neither use nor check these claims: they exclude all graphs with the given parameters, not a class.

**Table 2.** What is claimed on the platform about the six pairs, in the papers and in the discussion of the problem as of 1 November 2026. The claims are paraphrased; we did not check them.

| Set | Claimed class exclusions |
|---|---|
| $(50, 11, 7, 0, 3)$ | is in the list of 39 sets for which the sieve [5] excludes graphs on which an abelian group acts semiregularly with $1 + \lvert s\rvert/r$ orbits, all of them cocliques; the order of the automorphism group is not divisible by 7 or 11 [8] |
| $(68, 13, 7, 0, 3)$ | the order of the automorphism group is not divisible by 7, 11 or 13 [8]; there is no automorphism of order 17 [9]; there are no Cayley graphs over one of the groups of order 68 [10]; there are no graphs on which a group acts with a regular orbit and an orbit of cosets of a nontrivial proper subgroup [19] |
| $(100, 16, 7, 0, 3)$ | is in the list of the sieve [5]; graphs invariant under the action of $\mathbb F_{25} \rtimes \mathbb F_5^\times$ and one more class of graphs are excluded [6], [7]; the order of the automorphism group is not divisible by 11 or 13 [8] |
| $(108, 19, 9, 0, 4)$ | is in the list of the sieve [5]; the order of the automorphism group is not divisible by 11 or 13 [8] |
| $(55, 16, 12, 1, 6)$ | the order of the automorphism group is not divisible by 7 [8]; there is no automorphism of order 11 [9]; there are no Cayley graphs over one of the groups of order 55 [10]; there are no graphs on which a group acts with a regular orbit and an orbit of cosets of a nontrivial proper subgroup [19] |
| $(48, 9, 5, 0, 2)$ | is in the list of the sieve [5]; there are no graphs on which an abelian group of order 24 acts semiregularly with two orbits [13], [7]; the order of the automorphism group is divisible only by 2 and 3 [8]; there are no graphs in the class of Kautz covers and in several other classes given by lifts and group actions [14]; there are no graphs with an involution of the class considered in the post [15]; none of the seven graphs with parameters $(48, 13, 7, 2, 4)$ held by the author of the post [20] contains a graph with these parameters as a spanning subgraph; in the auxiliary count of the appendix of [21] there are no graphs on which $S_3 \times S_3$ acts with a regular orbit and an orbit of 12 points |

The post [9] states explicitly that it does not close the rows $(68, 13, 7, 0, 3)$ and $(55, 16, 12, 1, 6)$.

## 3. The rank of $A - \theta I$

The nontrivial eigenvalues of a DSRG are the roots of the polynomial $x^2 - (\lambda - \mu)x - (t - \mu)$ [1]. In this paper $\mu \ne 0$ and the discriminant $\Delta = (\lambda - \mu)^2 + 4(t - \mu)$ is positive; this holds for all the sets under discussion. Denote the roots by $r > s$ and their multiplicities as eigenvalues of $A$ by $f$ and $g$. For a root $\theta$ let $\theta'$ be the other root and $m'$ its multiplicity, let $E_\theta = \ker(A - \theta I)$ over $\mathbb R$, and let $\mathbf 1$ be the all-ones vector.

**Lemma 4.** Let $\mu \ne 0$, $\Delta > 0$ and $\{\theta, \theta'\} = \{r, s\}$. Then:

1. $(A - \theta I)(A - \theta' I) = \mu J$ and $(k - \theta)(k - \theta') = v\mu \ne 0$;
2. $\mathbb R^v = \langle \mathbf 1 \rangle \oplus E_\theta \oplus E_{\theta'}$, hence $\operatorname{rank}(A - \theta I) = 1 + m'$; moreover, $f + g = v - 1$ and $k + fr + gs = 0$;
3. the matrix $K_\theta = v(A - \theta I) - (k - \theta)J$ has rank $m'$, and its image is $E_{\theta'}$.

*Proof.* 1. The roots satisfy $\theta + \theta' = \lambda - \mu$ and $\theta\theta' = \mu - t$, so $(A - \theta I)(A - \theta' I) = A^2 - (\lambda - \mu)A + (\mu - t)I = \mu J$ by the definition. The row sums of this equation give $(k - \theta)(k - \theta') = v\mu$.

2. From $\mathbf 1^\top A = k\mathbf 1^\top$ it follows that $A$ maps $\mathbf 1^\perp$ into itself. If $Au = \theta u$, then $k\mathbf 1^\top u = \theta \mathbf 1^\top u$, and since $k \ne \theta$, the vector $u$ lies in $\mathbf 1^\perp$; the same holds for $\theta'$. On $\mathbf 1^\perp$ the matrix $J$ acts as zero, and by item 1 we have $(A - \theta I)(A - \theta' I) = 0$ there, with distinct real roots. Hence $A$ is diagonalizable on $\mathbf 1^\perp$ and $\mathbf 1^\perp = E_\theta \oplus E_{\theta'}$. Together with $A\mathbf 1 = k\mathbf 1$ this gives the decomposition, $\dim E_\theta + m' = v - 1$ and $\operatorname{rank}(A - \theta I) = v - \dim E_\theta = 1 + m'$. The equations for $f$ and $g$ are the dimension of $\mathbf 1^\perp$ and the zero trace of $A$.

3. $K_\theta \mathbf 1 = v(k - \theta)\mathbf 1 - (k - \theta)v\mathbf 1 = 0$. On $\mathbf 1^\perp$ the matrix $K_\theta$ coincides with $v(A - \theta I)$: on $E_\theta$ it is zero, and on $E_{\theta'}$ it is multiplication by $v(\theta' - \theta) \ne 0$. $\square$

The lemma constrains every piece of $A - \theta I$: a nonsingular submatrix of order $n$ requires $n \le 1 + m'$, and $p$ rows of $K_\theta$ have a left kernel of dimension at least $p - m'$. Sections 4 and 6 find such pieces where the parameters fix their structure. Section 5 shows that when the margin in the bound is small, such a piece also determines the rest of the matrix.

## 4. The closed neighbourhood when λ = 0

In this section $\lambda = 0$. Fix a vertex $x$ and put $\Gamma^+ = \Gamma^+(x)$, $\Gamma^- = \Gamma^-(x)$, $N[x] = \{x\} \cup \Gamma^+ \cup \Gamma^-$, $M = \Gamma^+ \cap \Gamma^-$, $Q = \Gamma^+ \setminus \Gamma^-$ and $P = \Gamma^- \setminus \Gamma^+$. The vertices of $M$ are joined to $x$ reciprocally, $Q$ consists of the pure out-neighbours of $x$, and $P$ of its pure in-neighbours.

**Lemma 5.** If $\lambda = 0$, then:

1. if $a \to b$ and $b \to c$, there is no arc $a \to c$;
2. the sets $\Gamma^+$ and $\Gamma^-$ are independent, there are no arcs from $\Gamma^-$ to $\Gamma^+$, and inside $N[x]$ there are only arcs from $x$ to $\Gamma^+$, from $\Gamma^-$ to $x$, and from $Q$ to $P$;
3. every vertex of $Q$ has exactly $\mu$ out-neighbours in $P$;
4. $|M| = t$, $|Q| = |P| = k - t$ and $|N[x]| = 2k - t + 1$.

*Proof.* 1. If $a \to b \to c$ and $a \to c$, then $a \ne c$ because there are no loops, and the path $a \to b \to c$ gives $A^2(a, c) \ge 1$, contrary to $A^2(a, c) = \lambda = 0$.

2. An arc $a \to b$ inside $\Gamma^+$ together with $x \to a$ and $x \to b$ gives a forbidden triple; an arc inside $\Gamma^-$ gives the triple $a \to b \to x$ with $a \to x$; an arc from $a \in \Gamma^-$ to $b \in \Gamma^+$ gives the triple $a \to x \to b$ with $a \to b$. Now let $a \to b$ be an arc inside $N[x]$ not incident with $x$. Its tail $a$ is not in $\Gamma^-$, because arcs from $\Gamma^-$ go neither to $\Gamma^-$ nor to $\Gamma^+$; so $a \in Q$. Its head $b$ is not in $\Gamma^+$, because $\Gamma^+$ is independent; so $b \in P$.

3. For $q \in Q$ there is no arc $q \to x$, so there are exactly $\mu$ paths of length 2 from $q$ to $x$. These are paths $q \to y \to x$ with $y \in \Gamma^-$, and by item 2 all such $y$ lie in $P$.

4. $|M| = A^2(x, x) = t$, hence $|\Gamma^+ \cup \Gamma^-| = 2k - t$ and $|Q| = |P| = k - t$, while $x \notin \Gamma^+ \cup \Gamma^-$. $\square$

**Proposition 6.** If $\lambda = 0$, then for every $\theta \ne 0$

$$
\det (A - \theta I)[N[x], N[x]] = (-1)^{t + 1}\, \theta^{2k - t - 2} \bigl(\theta^3 - t\theta - \mu(k - t)\bigr).
$$

The determinant depends neither on the graph nor on the vertex. In particular, when $\theta^3 - t\theta - \mu(k - t) \ne 0$ the submatrix is nonsingular.

*Proof.* Order $N[x]$ as follows: $x$, then $M$, $Q$ and $P$. By Lemma 5 the submatrix $L = (A - \theta I)[N[x], N[x]]$ has the form

$$
L = \begin{pmatrix} -\theta & \mathbf 1^\top & \mathbf 1^\top & 0 \\ \mathbf 1 & -\theta I & 0 & 0 \\ 0 & 0 & -\theta I & A_{QP} \\ \mathbf 1 & 0 & 0 & -\theta I \end{pmatrix},
$$

where $A_{QP} = A[Q, P]$ is the matrix of arcs from $Q$ to $P$, whose row sums equal $\mu$ by item 3 of Lemma 5. The block $L'$ on $M \cup Q \cup P$ is block upper triangular, and $\det L' = (-\theta)^{2k - t}$. Let $b^\top = (\mathbf 1^\top, \mathbf 1^\top, 0)$ be the off-diagonal row of $x$, and $c = (\mathbf 1, 0, \mathbf 1)$ the column of $x$. The solution $y$ of the system $L'y = c$ is $y_M = -\theta^{-1}\mathbf 1$, $y_P = -\theta^{-1}\mathbf 1$, and $-\theta y_Q + A_{QP} y_P = 0$ gives $y_Q = -\mu\theta^{-2}\mathbf 1$. Therefore $b^\top y = -t\theta^{-1} - \mu(k - t)\theta^{-2}$, and by the Schur formula

$$
\det L = \det L' \cdot \bigl(-\theta - b^\top y\bigr) = (-\theta)^{2k - t} \bigl(-\theta + t\theta^{-1} + \mu(k - t)\theta^{-2}\bigr) = (-1)^{2k - t + 1}\, \theta^{2k - t - 2}\bigl(\theta^3 - t\theta - \mu(k - t)\bigr).
$$

It remains to note that $(-1)^{2k - t + 1} = (-1)^{t + 1}$. $\square$

For example, for $(50, 11, 7, 0, 3)$ and $\theta = 1$ the neighbourhood $N[x]$ has 16 vertices, and the determinant equals $(-1)^8 (1 - 7 - 12) = -18$ at every vertex of every graph with these parameters. The rank of $A - I$ is then $1 + g = 13 < 16$.

**Theorem 7.** Let $\lambda = 0$, $\mu \ne 0$, $\Delta > 0$, and let the root $\theta$ satisfy $\theta \ne 0$ and $\theta^3 - t\theta - \mu(k - t) \ne 0$. Then $2k - t \le m'$, where $m'$ is the multiplicity of the other root $\theta'$.

*Proof.* By Proposition 6 the principal submatrix of order $|N[x]| = 2k - t + 1$ is nonsingular, so $\operatorname{rank}(A - \theta I) \ge 2k - t + 1$. By Lemma 4 this rank equals $1 + m'$. $\square$

**Corollary 8.** Let $\lambda = 0$, $\mu > 0$ and $t = 2\mu + 1$. Then $(2k - t)(\mu + 2) \le k + v - 1$.

*Proof.* The polynomial $x^2 + \mu x - (\mu + 1) = (x - 1)(x + \mu + 1)$ has roots $r = 1$ and $s = -(\mu + 1)$, and $\Delta = (\mu + 2)^2 > 0$. By Lemma 4, $k + f - (\mu + 1)g = 0$ and $f + g = v - 1$, whence $g = (k + v - 1)/(\mu + 2)$. Take $\theta = 1$. Since $t = |M| \le k$, the expression $1 - t - \mu(k - t)$ is at most $1 - t = -2\mu < 0$. Theorem 7 gives $2k - t \le g$, and it remains to multiply by $\mu + 2$. $\square$

*Proof of Theorem 1.* All four sets have $\lambda = 0$ and $t = 2\mu + 1$, and the inequality of Corollary 8 fails: $15 \cdot 5 = 75 > 60$ for $(50, 11, 7, 0, 3)$, $19 \cdot 5 = 95 > 80$ for $(68, 13, 7, 0, 3)$, $25 \cdot 5 = 125 > 115$ for $(100, 16, 7, 0, 3)$ and $29 \cdot 6 = 174 > 126$ for $(108, 19, 9, 0, 4)$. A graph exists if and only if its complement exists, so the complements do not exist either. $\square$

**The bound is attained.** On the graph $(6, 2, 1, 0, 1)$ with $\theta = -1$, $\theta' = 0$ we have $2k - t = 3 = m'$. On the Clebsch graph, the undirected strongly regular graph $(16, 5, 0, 2)$, which as a DSRG has parameters $(16, 5, 5, 0, 2)$, with $\theta = 1$ we have $2k - t = 5 = g$. In both cases $N[x]$ gives a nonsingular principal submatrix of full rank of $A - \theta I$, and one cannot add one to the left-hand side of Theorem 7.

## 5. The Schur complement outside the neighbourhood when λ = 0

Theorem 7 takes only one thing from Proposition 6: the submatrix of $A - \theta I$ on $N[x]$ is nonsingular, so the rank of the whole matrix is at least its order. When the bound holds, the same submatrix says more: it determines the rest of the matrix up to a matrix whose rank equals the margin in the bound. For $(48, 9, 5, 0, 2)$ this rank is 1, and existence of the graph reduces to a finite search at one vertex.

In this section $\lambda = 0$, $\mu \ne 0$, $\Delta > 0$, and the root $\theta$ satisfies $\theta \ne 0$ and $\rho = \theta^3 - t\theta - \mu(k - t) \ne 0$. As in Sections 3 and 4, $\theta'$ is the other root, $m'$ its multiplicity, $x$ a vertex, and $M$, $Q$ and $P$ the parts of its neighbourhood. Put $N(x) = N[x] \setminus \{x\} = \Gamma^+ \cup \Gamma^-$, the open neighbourhood, $\overline N = V \setminus N[x]$, the set of outer vertices, and $\tau = m' - (2k - t)$, the margin in the bound of Theorem 7. Write the blocks

$$
L = (A - \theta I)[N[x], N[x]], \qquad B = A[N[x], \overline N], \qquad C = A[\overline N, N[x]], \qquad F = C L^{-1} B,
$$

where $L$ is nonsingular by Proposition 6. The Schur complement of the block $L$ in $A - \theta I$ is the matrix $T = (A - \theta I)[\overline N, \overline N] - F$ on the outer vertices. Denote its diagonal by $d_w = T(w, w)$.

**Lemma 9.** Under these assumptions:

1. the vector $\hat y = (1 + \theta/\mu)\, e_x + \mu^{-1} \mathbf 1_{\Gamma^-}$ satisfies $(A - \theta I)\hat y = \mathbf 1$, and the vector $\check y = (1 + \theta/\mu)\, e_x + \mu^{-1} \mathbf 1_{\Gamma^+}$ satisfies $\check y^\top (A - \theta I) = \mathbf 1^\top$; hence $C L^{-1} \mathbf 1 = \mathbf 1$ and $\mathbf 1^\top L^{-1} B = \mathbf 1^\top$;
2. $BC = \Phi$, where $\Phi = \mu J - L^2 - (\theta - \theta')L$: for $n, n' \in N[x]$ exactly $\Phi(n, n')$ outer vertices $w$ lie on a path $n \to w \to n'$;
3. $BT = 0$, $TC = 0$ and $T^2 = (\theta' - \theta)T$. Hence $T/(\theta' - \theta)$ is an idempotent, $\operatorname{rank} T = \tau$, and the trace of $T$ equals $\tau(\theta' - \theta)$.

*Proof.* 1. Column $x$ of the equation $A^2 = tI + \mu(J - I - A)$ gives $(A \mathbf 1_{\Gamma^-})_y = t[y = x] + \mu(1 - [y = x] - A(y, x))$, and $A e_x = \mathbf 1_{\Gamma^-}$. For $y \ne x$ the coordinate $y$ of the vector $(A - \theta I)\hat y$ equals $(1 + \theta/\mu)A(y, x) + 1 - A(y, x) - (\theta/\mu)A(y, x) = 1$. For $y = x$ it equals $t/\mu - \theta(1 + \theta/\mu) = (t - \mu\theta - \theta^2)/\mu = 1$, because $\theta^2 + \mu\theta = t - \mu$. The support of $\hat y$ lies in $N[x]$, so the rows of $N[x]$ give $L \hat y_{N[x]} = \mathbf 1$, and the rows of $\overline N$ give $C \hat y_{N[x]} = \mathbf 1$; hence $C L^{-1}\mathbf 1 = \mathbf 1$. For $\check y$ the same argument runs along row $x$.

2. Put $H = A - \theta I$. Since $\theta + \theta' = -\mu$ and $\theta\theta' = \mu - t$, Lemma 4 gives $H(H + (\theta - \theta')I) = (A - \theta I)(A - \theta' I) = \mu J$. The block $(N[x], N[x])$ of this equation is $L^2 + BC + (\theta - \theta')L = \mu J$.

3. Substitute $H[\overline N, \overline N] = F + T$ into the block $(N[x], \overline N)$: $LB + B(F + T) + (\theta - \theta')B = \mu J$. By item 2, $BF = BCL^{-1}B = \mu J L^{-1} B - LB - (\theta - \theta')B$, and by item 1, $J L^{-1} B = J$. What remains is $BT = 0$. In the same way the block $(\overline N, N[x])$ gives $TC = 0$. In the block $(\overline N, \overline N)$, that is, in $CB + (F + T)^2 + (\theta - \theta')(F + T) = \mu J$, the products $FT$ and $TF$ vanish, and $F^2 = CL^{-1}(BC)L^{-1}B = \mu J - CB - (\theta - \theta')F$ by items 1 and 2. What remains is $T^2 + (\theta - \theta')T = 0$. By the Schur formula $\operatorname{rank} H = \operatorname{rank} L + \operatorname{rank} T$, where $\operatorname{rank} H = 1 + m'$ by Lemma 4 and $\operatorname{rank} L = 2k - t + 1$. The trace of an idempotent equals its rank. $\square$

For a given neighbourhood $N[x]$ the matrix $F$ depends only on how the outer vertices attach to $N(x)$: $F(w, w') = C(w, \cdot)\, L^{-1} B(\cdot, w')$, and there are no arcs between $x$ and the outer vertices. Call the pair of sets $(\Gamma^+(w) \cap N(x), \Gamma^-(w) \cap N(x))$ the *type* of an outer vertex $w$. Then $F(w, w')$ is determined by the types of $w$ and $w'$, and by Lemma 9 $A[\overline N, \overline N] = \theta I + F + T$, where the rank of $T$ is $\tau$. When $\tau = 0$ the block of $A$ on the outer vertices is determined by the types completely. This is how the graph $(6, 2, 1, 0, 1)$ with $\theta = -1$ and the Clebsch graph with $\theta = 1$ are built; on them the bound of Theorem 7 is attained (Section 4).

**Proposition 10.** Let $\tau \ge 1$. Then $T$ has a nonsingular principal submatrix $T[R, R]$ of order $\tau$, and $T = T[\cdot, R]\, T[R, R]^{-1}\, T[R, \cdot]$. In particular, when $\tau = 1$ there is an outer vertex $w_0$ with $d_0 = d_{w_0} \ne 0$, and for all outer vertices $w$ and $w'$

$$
T(w, w') = \frac{T(w, w_0)\, T(w_0, w')}{d_0}, \qquad d_w\, d_{w'} = T(w, w')\, T(w', w).
$$

Therefore, for $w \ne w'$ the arc $A(w, w') = F(w, w') + T(w, w_0)\,T(w_0, w')/d_0$ is determined by the types of the vertices $w$, $w'$ and $w_0$ and by the arcs between $w_0$ and the vertices $w$, $w'$: for $w \ne w_0$ we have $T(w, w_0) = A(w, w_0) - F(w, w_0)$ and $T(w_0, w) = A(w_0, w) - F(w_0, w)$.

*Proof.* The matrix $\Pi = T/(\theta' - \theta)$ is an idempotent of rank $\tau$ (Lemma 9), and its eigenvalues are $\tau$ ones and zeros. The sum of the principal minors of $\Pi$ of order $\tau$ equals the $\tau$-th elementary symmetric function of the eigenvalues, that is, 1, so one of these minors is nonzero; for $T$ the same minor is multiplied by $(\theta' - \theta)^\tau$. The columns of $T[\cdot, R]$ are linearly independent and the rank of $T$ is $\tau$, so they form a basis of the image and $T = T[\cdot, R]\, X$ for some matrix $X$. The rows of $R$ give $T[R, \cdot] = T[R, R]\, X$, whence the formula. When $\tau = 1$ we have $R = \{w_0\}$, and the second equation says that the minors of order 2 of a matrix of rank 1 vanish. $\square$

We call the vertex $w_0$ the *pivot*. When $\tau \ge 2$ the same role is played by the $\tau$ pivot vertices of the set $R$ (Section 8).

**The set $(48, 9, 5, 0, 2)$.** Lemma 11 collects what the search needs to know about it.

**Lemma 11.** Let $(v, k, t, \lambda, \mu) = (48, 9, 5, 0, 2)$ and $\theta = 1$. Then $\theta' = -3$, $m' = g = 14$, $\rho = -12$, $|M| = 5$, $|Q| = |P| = 4$, $|N(x)| = 13$, there are 34 outer vertices, $\tau = 1$, and the trace of $T$ equals $-4$. Moreover:

1. the arcs from $Q$ to $P$ form a bipartite graph in which every vertex has exactly two arcs: a cycle of length 8 or two cycles of length 4;
2. the row and the column $x$ of the matrix $\Phi$ are zero, and on $N(x)$, in the order $M$, $Q$, $P$,
$$
\Phi[N(x), N(x)] = \begin{pmatrix} 3I + J & J & 2J \\ 2J & 3I + 2J & 2(J - A_{QP}) \\ J & J & 3I + 2J \end{pmatrix},
$$
where $A_{QP} = A[Q, P]$. Every vertex of $M$ and $P$ has 8 out-neighbours among the outer vertices, every vertex of $Q$ has 7; every vertex of $M$ and $Q$ has 8 in-neighbours among the outer vertices, every vertex of $P$ has 7;
3. let $\alpha_w = |\Gamma^+(w) \cap Q|$, $\beta_w = |\Gamma^-(w) \cap P|$, let $\nu_2(w, w')$ be the number of paths $w \to n \to w'$ with $n \in N(x)$, and let $\nu_3(w, w')$ be the number of paths $w \to q \to p \to w'$ with $q \in Q$ and $p \in P$. Then for outer vertices $w$ and $w'$
$$
F(w, w') = \frac{(1 + \alpha_w)(1 + \beta_{w'})}{3} - \nu_2(w, w') - \nu_3(w, w'), \qquad d_w = -1 - \frac{(1 + \alpha_w)(1 + \beta_w)}{3} + \nu_2(w, w) + \nu_3(w, w),
$$
and the number $3d_w$ is an integer;
4. distinct outer vertices have distinct types.

*Proof.* The roots of the polynomial $x^2 + 2x - 3$ are $1$ and $-3$. By Lemma 4, $f + g = 47$ and $9 + f - 3g = 0$, whence $g = 14$ and $f = 33$. Next, $\rho = 1 - 5 - 8 = -12$; $|M| = t = 5$ and $|Q| = |P| = k - t = 4$ by Lemma 5; $\tau = 14 - 13 = 1$, and the trace of $T$ equals $1 \cdot (-3 - 1) = -4$ by Lemma 9.

1. By Lemma 5 every $q \in Q$ has exactly two out-neighbours in $P$. For $p \in P$ there is no arc $x \to p$, so there are exactly $\mu = 2$ paths $x \to o \to p$. Their middle vertices lie in $\Gamma^+$, and by Lemma 5 in $Q$. A bipartite graph on $4 + 4$ vertices in which every vertex has two arcs is a union of even cycles of length at least 4.

2. By Lemma 9, $\Phi(n, n') = (BC)(n, n')$ is the value of $A^2(n, n')$ from the definition minus the paths of length 2 inside $N[x]$, and Lemma 5 gives the paths inside $N[x]$. For example, for $m \ne m'$ in $M$ there is no arc, $A^2(m, m') = \mu = 2$, inside $N[x]$ there is one path $m \to x \to m'$, and $\Phi(m, m') = 1$; for $q \in Q$ and $p \in P$ with an arc $q \to p$ we have $A^2(q, p) = \lambda = 0$ and $\Phi(q, p) = 0$. There are no arcs from $x$ to the outer vertices, so the row and the column $x$ are zero. The degrees are $k = 9$ minus the arcs inside $N[x]$: a vertex of $M$ has one out-neighbour inside $N[x]$, namely $x$, a vertex of $Q$ has two, in $P$, and a vertex of $P$ has one, namely $x$; vertices of $M$ and $Q$ have one in-neighbour inside $N[x]$, namely $x$, and a vertex of $P$ has two, in $Q$.

3. Let $\xi = B(\cdot, w')$ and $z = L^{-1}\xi$. By Lemma 5 the only out-neighbour of $i \in \Gamma^-$ inside $N[x]$ is $x$, the out-neighbours of $q \in Q$ are two vertices of $P$, and those of $x$ are the vertices of $\Gamma^+$. Therefore the rows of $Lz = \xi$ give $z_i = z_x - \xi_i$ for $i \in \Gamma^-$, $z_q = \sum_{q \to p} z_p - \xi_q$ for $q \in Q$, and $\sum_{o \in \Gamma^+} z_o = z_x$, since there is no arc $x \to w'$. Substitute the first two equations into the third. Every $p \in P$ has exactly two in-neighbours in $Q$, and $w'$ has exactly $\mu = 2$ in-neighbours in $\Gamma^+$ and $\beta_{w'}$ in-neighbours in $P$, so $12 z_x = 2 + 2\beta_{w'}$. Finally, $F(w, w') = \sum_{n \in \Gamma^+(w) \cap N(x)} z_n$. The vertex $w$ has exactly 2 out-neighbours in $\Gamma^-$ and $\alpha_w$ out-neighbours in $Q$, and the subtracted terms $\xi_n$ and $\xi_p$ add up to $\nu_2(w, w')$ and $\nu_3(w, w')$. We obtain $F(w, w') = 2(1 + \alpha_w) z_x - \nu_2(w, w') - \nu_3(w, w')$, which is the first formula. The second follows from $d_w = (A - I)(w, w) - F(w, w) = -1 - F(w, w)$.

4. Let $w \ne w'$ have the same type. Then they share two in-neighbours in $\Gamma^+$, and by item 1 of Lemma 5 there are no arcs between $w$ and $w'$. The value $F(w, w')$ depends on the out-neighbours of $w$ and the in-neighbours of $w'$, and the in-neighbours of $w'$ are the same as those of $w$. Therefore $F(w, w') = F(w, w)$ and $T(w, w') = -F(w, w) = 1 + d_w$; likewise $T(w', w) = 1 + d_w$ and $d_{w'} = d_w$. The equation $d_w d_{w'} = T(w, w')T(w', w)$ of Proposition 10 gives $d_w^2 = (1 + d_w)^2$, that is, $d_w = -1/2$. But $3d_w$ is an integer by item 3, a contradiction, so the types are distinct. $\square$

**Remark.** The Schur complement can also be taken with respect to the open neighbourhood. Inside $N(x)$ there are only arcs from $Q$ to $P$ (Lemma 5), so the matrix $E$ of these arcs on $N(x)$ satisfies $E^2 = 0$, and $(E - \theta I)^{-1} = -(\theta I + E)/\theta^2$. For $(48, 9, 5, 0, 2)$ with $\theta = 1$ this gives the integral matrix

$$
Y = (A - I)[\overline N, \overline N] + A[\overline N, N(x)]\, A[N(x), \overline N] + A[\overline N, Q]\, A_{QP}\, A[P, \overline N] = \frac{(\mathbf 1 + \alpha)(\mathbf 1 + \beta)^\top}{3} + T.
$$

The first expression is the Schur complement of the block $(A - I)[N(x), N(x)] = E - I$ in $(A - I)[V \setminus \{x\}, V \setminus \{x\}]$, the second is item 3 of Lemma 11. Hence $\operatorname{rank} Y \le 2$. The proof of Theorem 3 does not use the remark; its core is formalized (Section 7).

**Symmetries and types.** Fix a vertex $x$ and label $Q$ and $P$ so that the graph of arcs from $Q$ to $P$ coincides with one of the two graphs of item 1 of Lemma 11. Permutations of $M$ and pairs of permutations of $Q$ and $P$ that preserve the arcs from $Q$ to $P$ preserve $N[x]$, $L$ and $\Phi$ and map types to types without changing $F$ and $d$. We call them symmetries of the frame; for the cycle there are $5! \cdot 8 = 960$ of them, for two cycles $5! \cdot 32 = 3840$. A type is admissible if a vertex $w$ of this type has exactly two in-neighbours in $\Gamma^+$ and exactly two out-neighbours in $\Gamma^-$, and the subgraph on $N[x] \cup \{w\}$ contains no transitive triangle. The type of every outer vertex is admissible: there is no arc $x \to w$, so there are exactly $\mu = 2$ paths $x \to o \to w$, and likewise for paths from $w$ to $x$. There are 57 920 admissible types for the cycle and 58 912 for two cycles. The symmetries of the frame split them into 415 and 418 orbits, and 352 and 355 of these have $d \ne 0$; in total there are 707 such orbits. The *key* of an orbit is the smallest code, in a fixed order, of a type in it; the keys order the orbits.

**Proposition 12.** Suppose a graph with parameters $(48, 9, 5, 0, 2)$ exists, and let $x$ be any of its vertices. Then, for a suitable labelling of $Q$ and $P$, there is an outer vertex $w_0$ with $d_0 \ne 0$ whose type is the fixed representative of its orbit, and the key of its orbit is not greater than the key of any outer vertex with $d \ne 0$. Each of the other 33 outer vertices $w$ is given by a triple: the type of $w$, $a_w = A(w_0, w)$ and $b_w = A(w, w_0)$. The triples satisfy five conditions.

- (a) *Pair minor:* $d_0\, d_w = (a_w - F(w_0, w))(b_w - F(w, w_0))$.
- (b) *Arcs to the pivot:* the arc $w_0 \to w$ does not close a transitive triangle with the third vertex in $N[x]$, and without this arc there are at most $\mu$ paths $w_0 \to n \to w$ with $n \in N[x]$. The same holds for $w \to w_0$.
- (c) *Types:* the types of all 34 outer vertices are distinct, and if $d_w \ne 0$, the key of the orbit of the type of $w$ is not smaller than the key of the pivot.
- (d) *Compatibility:* for any two triples the numbers $A(w, w')$ and $A(w', w)$ given by the formula of Proposition 10 equal 0 or 1. An arc between $w$ and $w'$ does not close a transitive triangle with the third vertex in $N[x] \cup \{w_0\}$, and without the arc there are at most $\mu$ paths of length 2 between them through $N[x] \cup \{w_0\}$.
- (e) *Cover:* for any $n, n' \in N(x)$ exactly $\Phi(n, n')$ of the 34 outer vertices lie on a path $n \to w \to n'$. Every vertex of $N(x)$ has as many out-neighbours and in-neighbours among the outer vertices as item 2 of Lemma 11 prescribes. The pivot $w_0$ has exactly $7 - \alpha_{w_0}$ out-neighbours and $7 - \beta_{w_0}$ in-neighbours among the other outer vertices, and every $w$ has exactly $7 - \alpha_w$ and $7 - \beta_w$.

*Proof.* By Lemma 11, $\tau = 1$ and the trace of $T$ equals $-4$, so $d_w \ne 0$ for at least one outer vertex. Among such vertices take $w_0$ with the smallest orbit key and apply the symmetry of the frame that maps its type to the representative of the orbit; keys, $F$ and $d$ do not change. Condition (a) is the second equation of Proposition 10 with $w' = w_0$, and the arc formula in (d) is its first equation. The rest of (b) and (d) is the definition of a graph with $\lambda = 0$ and $\mu = 2$ on a subgraph: over an arc there are no paths of length 2, without an arc there are exactly $\mu$ of them in the whole graph, and no more than that in a subgraph. Condition (c) is item 4 of Lemma 11 and the choice of $w_0$. The first two parts of (e) are item 2 of Lemma 9 and item 2 of Lemma 11. The last part: an outer vertex has 9 out-neighbours, of which 2 lie in $\Gamma^-$ and $\alpha_w$ in $Q$, and 9 in-neighbours, of which 2 lie in $\Gamma^+$ and $\beta_w$ in $P$. $\square$

**Search.** For each of the 707 pivot orbits, the search program looks for 33 triples satisfying (a)–(e). It first builds the candidates, the triples satisfying (a)–(c), and the rows of their pairwise compatibility (d). Everything is computed exactly, in integers: the matrix $12 L^{-1}$ is integral. Then the program solves an exact cover problem with pairwise compatibility. There are 197 cells: 169 pairs $(n, n')$ from $N(x)$, 13 cells each for the out-degrees and in-degrees of the vertices of $N(x)$, and two cells for the degrees of the pivot. The required number of a cell is what remains after the contribution of the pivot, and a candidate enters the cells touched by its type and its arcs to the pivot. The depth-first search takes the cell with the fewest fitting candidates and branches over them; in the branch of the $i$-th candidate, the candidates of the same cell with smaller indices are excluded. Hence every cover occurs in exactly one branch, the branch of its candidate with the smallest index in that cell, and the search is complete. The search counts the degrees of the chosen triples from the last part of (e) as it goes and prunes branches where they are already violated.

Of the 352 pivot orbits of the cycle, 38 admit no cover already at the root; for two cycles, 90 of 355 do. The search over the remaining 314 and 265 orbits visited 36 012 and 12 620 nodes and found no cover.

*Proof of Theorem 3.* If the graph exists, Proposition 12 gives a cover satisfying (a)–(e) for one of the 707 pivot orbits of one of the two graphs of arcs from $Q$ to $P$. The search exhausted all 707 orbits and found no cover. The complement of a DSRG is again a DSRG, so the complement $(48, 38, 34, 30, 30)$ does not exist either. $\square$

The last step rests on a computer search, not on Lean. Therefore it was repeated by a second program, written independently of the first, with a different set of conditions and a different order of orbits (Section 9, check 8). The outcome is the same: none of the 707 orbits has the required set of triples.

## 6. The out-neighbours of a vertex when λ = 1 and t = 2μ

In this section $\lambda = 1$, $t = 2\mu$ and $0 < t < k < v - 1$. Then $x^2 + (\mu - 1)x - \mu = (x - 1)(x + \mu)$, so $r = 1$, $s = -\mu$, $\Delta = (\mu + 1)^2 > 0$, and by Lemma 4 $(\mu + 1)g = k + v - 1$. The row sums of the equation for $A^2$ give $k^2 = t + k + \mu(v - k - 1)$, that is,

$$
\mu(v - k + 1) = k(k - 1). \tag{1}
$$

By Lemma 4 the matrix $K_1 = v(A - I) - (k - 1)J$ has rank $g$. Fix a vertex $x$ and put $\Gamma^+ = \Gamma^+(x)$, $M = \Gamma^+ \cap \Gamma^-(x)$, $S = \{x\} \cup \Gamma^+$ and $Z = V \setminus S$; the set $Z$ has exactly $v - k - 1$ vertices.

**Lemma 13.** If $\lambda = 1$, then:

1. every vertex $y \in \Gamma^+$ has exactly one in-neighbour in $\Gamma^+$; denote it by $\mathrm{pred}(y)$. The arcs inside $\Gamma^+$ are exactly the arcs $\mathrm{pred}(y) \to y$, and $\mathrm{pred}(y) \ne y$;
2. every component $U_1, \dots, U_c$ of the graph of the map $\mathrm{pred}$ on $\Gamma^+$ contains exactly one cycle, and $n_i = |U_i| \ge 2$;
3. let $m_i = |M \cap U_i|$, and for $z \in Z$ let $\ell_i(z) = |\Gamma^-(z) \cap U_i|$ be the number of arcs from $U_i$ to $z$. Then $\sum_i m_i = t$, $\sum_i \ell_i(z) = \mu$ for every $z \in Z$, and $\sum_{z \in Z} \ell_i(z) = (k - 1)n_i - m_i$.

*Proof.* 1. The in-neighbours of $y$ in $\Gamma^+$ correspond to the paths $x \to u \to y$, and there are $A^2(x, y) = \lambda = 1$ of them. There are no loops, so $\mathrm{pred}(y) \ne y$.

2. This is the graph of a map of a finite set into itself without fixed points: each of its components has one cycle, of length at least 2.

3. $\sum_i m_i = |M| = A^2(x, x) = t$. For $z \in Z$ there is no arc $x \to z$, and $\sum_i \ell_i(z) = A^2(x, z) = \mu$. The vertices of $U_i$ have $k n_i$ outgoing arcs in total. Of these, $m_i$ go to $x$ and $n_i$ go inside $\Gamma^+$: by item 1 every vertex of $\Gamma^+$ receives one arc from $\Gamma^+$, from its predecessor, and $y$ and $\mathrm{pred}(y)$ lie in the same component. The remaining $(k - 1)n_i - m_i$ arcs go to $Z$. $\square$

The matrix $D$ has $c$ columns, one per component, and rows of two kinds: the row $d = (k m_i - t n_i)_i$ and the rows $h_z = (2\ell_i(z) - m_i)_i$ for all $z \in Z$. For $a \in \mathbb R^c$ put

$$
w_a = \tfrac12 \Bigl(\sum_i a_i m_i\Bigr) e_x + \sum_i a_i \mathbf 1_{U_i},
$$

where $e_x$ is the unit vector of the vertex $x$ and $\mathbf 1_{U_i}$ is the indicator of the component.

**Theorem 14.** Let $\lambda = 1$, $t = 2\mu$ and $0 < t < k < v - 1$. A vector $w$ supported in $S$ satisfies $w^\top K_1 = 0$ if and only if $w = w_a$ for some $a$ with $Da = 0$. For $a = \mathbf 1$ we get $w_{\mathbf 1} = \mu e_x + \mathbf 1_{\Gamma^+}$, the row $x$ of the matrix $A + \mu I$.

*Proof.* Let $W = \sum_{y \in S} w_y$ and $\kappa = (k - 1)W/v$. Column $z$ of the equation $w^\top K_1 = 0$, after division by $v$, reads $\sum_{y \in S} w_y A(y, z) - w_z [z \in S] = \kappa$. The in-neighbours of $x$ inside $S$ are the vertices of $M$. The in-neighbours of $z \in \Gamma^+$ inside $S$ are $x$ and $\mathrm{pred}(z)$. The in-neighbours of $z \in Z$ inside $S$ lie in $\Gamma^+$, because there is no arc $x \to z$. Therefore the columns give three kinds of equations:

$$
w(M) - w_x = \kappa, \qquad w_z - w_{\mathrm{pred}(z)} = w_x - \kappa \ \ (z \in \Gamma^+), \qquad \sum_{y \in \Gamma^+} w_y A(y, z) = \kappa \ \ (z \in Z).
$$

The right-hand side of the second equation, $\delta = w_x - \kappa$, is the same for all $z \in \Gamma^+$. At a vertex where $w$ is maximal on $\Gamma^+$ we get $\delta \ge 0$, and where it is minimal, $\delta \le 0$. Hence $\delta = 0$: the vector $w$ is constant along the arcs $\mathrm{pred}(z) \to z$, that is, it equals some $a_i$ on each component $U_i$, and $w_x = \kappa$.

The first equation gives $\sum_i a_i m_i = 2w_x$. The equation $\kappa = w_x$ reads $v w_x = (k - 1)(w_x + \sum_i a_i n_i)$, that is, $(v - k + 1) w_x = (k - 1)\sum_i a_i n_i$, and with (1), $k w_x = \mu \sum_i a_i n_i$. Substituting $w_x = \frac12\sum_i a_i m_i$ and $t = 2\mu$, we get $d \cdot a = 0$. The third equation becomes $\sum_i a_i \ell_i(z) = \frac12\sum_i a_i m_i$, that is, $h_z \cdot a = 0$.

Conversely, let $Da = 0$ and $w = w_a$. From $d \cdot a = 0$ the same computation in reverse order gives $\kappa = w_x$. Then the first equation follows from $\sum_i a_i m_i = 2w_x$, the second from $w$ being constant on the components, and the third from $h_z \cdot a = 0$. For $a = \mathbf 1$ we have $\sum_i m_i = t = 2\mu$, $d \cdot \mathbf 1 = kt - tk = 0$ and $h_z \cdot \mathbf 1 = 2\mu - t = 0$ by Lemma 13. $\square$

We call the number $c - (k + 1 - g)$ the slack of the vertex, and write $[d \ne 0]$ for 1 if $d \ne 0$ and 0 if $d = 0$.

**Corollary 15.** Under the assumptions of Theorem 14:

1. $c - \operatorname{rank} D = \dim \ker D \ge k + 1 - g$;
2. the slack is at least $[d \ne 0]$, that is, $c \ge k + 1 - g + [d \ne 0]$, and $d = 0$ exactly when $m_i / n_i = t/k$ for all $i$;
3. let the slack be exact, that is, equal to $[d \ne 0]$. If $d \ne 0$, then every row $h_z$ equals $\gamma_z d$ for a number $\gamma_z$, every $\ell_i(z) = (m_i + \gamma_z d_i)/2$ is an integer in the interval $[0, n_i]$, and

$$
\sum_{z \in Z} \gamma_z = -\frac{k - 1}{\mu}. \tag{2}
$$

If $d = 0$, then all $h_z = 0$ and all $m_i$ are even.

*Proof.* 1. The rows of $K_1$ indexed by $S$ are $k + 1$ rows of a matrix of rank $g$, so the vectors $w$ supported in $S$ with $w^\top K_1 = 0$ form a space of dimension at least $k + 1 - g$. The map $a \mapsto w_a$ is linear and injective, because $w_a$ on $\Gamma^+$ recovers $a$, and by Theorem 14 it maps $\ker D$ onto this space.

2. The row $d$ belongs to $D$, so $\operatorname{rank} D \ge [d \ne 0]$, and item 1 gives the inequality. The equation $d = 0$ means $k m_i = t n_i$ for all $i$.

3. With exact slack, item 1 gives $\operatorname{rank} D \le c - (k + 1 - g) = [d \ne 0]$. If $d \ne 0$, the rank of $D$ equals 1, and every row $h_z$ is a multiple of $d$. Then $\ell_i(z) = (m_i + \gamma_z d_i)/2$, and this is a number of arcs. By Lemma 13 the sum of the rows $h_z$ equals

$$
\sum_{z \in Z} h_{z, i} = 2\bigl((k - 1)n_i - m_i\bigr) - (v - k - 1)m_i = 2(k - 1)n_i - (v - k + 1)m_i,
$$

and by (1) this is $-\frac{k - 1}{\mu}(k m_i - 2\mu n_i) = -\frac{k - 1}{\mu} d_i$. Hence $\bigl(\sum_z \gamma_z\bigr) d = -\frac{k - 1}{\mu} d$ and equation (2). If $d = 0$, the rank of $D$ is zero, $h_z = 0$, and the number of arcs $\ell_i(z) = m_i/2$ is an integer. $\square$

*Proof of Theorem 2.* For $(55, 16, 12, 1, 6)$ we have $t = 12 = 2\mu$, $g = 70/7 = 10$ and $k + 1 - g = 7$. There are at most eight components, because $|\Gamma^+| = 16$ and $n_i \ge 2$. The equation $d = 0$ requires $m_i/n_i = 3/4$, that is, $4 \mid n_i$ and $c \le 4 < 7$, contrary to item 2 of Corollary 15. Hence $d \ne 0$ and $c \ge 8$, that is, $c = 8$ and all $n_i = 2$. Every component is a reciprocal pair $y \leftrightarrow y'$ with $\mathrm{pred}(y) = y'$ and $\mathrm{pred}(y') = y$, and the slack is exact: $8 - 7 = 1 = [d \ne 0]$.

A pair contains $m_i \in \{2, 1, 0\}$ vertices of $M$. Let $a$, $b$ and $e$ be the numbers of pairs with $m_i = 2$, $1$ and $0$. Then $a + b + e = 8$ and $2a + b = t = 12$, and there are three compositions: $(a, b, e) = (4, 4, 0)$, $(5, 2, 1)$ and $(6, 0, 2)$. Here $d_i = 16 m_i - 24$, that is, $8$, $-8$ and $-24$. By item 3 of Corollary 15, at every vertex $z \in Z$ one number $\gamma_z$ gives all $\ell_i(z) = (m_i + \gamma_z d_i)/2 \in \{0, 1, 2\}$:

- for $m_i = 2$ we have $\ell_i(z) = 1 + 4\gamma_z$, hence $\gamma_z \in \{-1/4, 0, 1/4\}$ and the number $8\gamma_z$ is even;
- for $m_i = 1$ we have $\ell_i(z) = (1 - 8\gamma_z)/2$, and this is an integer only if $8\gamma_z$ is odd;
- for $m_i = 0$ we have $\ell_i(z) = -12\gamma_z$, hence $\gamma_z \in \{0, -1/12, -1/6\}$.

The compositions $(4, 4, 0)$ and $(5, 2, 1)$ contain pairs with $m_i = 2$ and with $m_i = 1$, and for any of the 38 vertices of $Z$ the number $8\gamma_z$ would have to be both even and odd. In the composition $(6, 0, 2)$ there is one common value, $\gamma_z = 0$ for every $z$, and the sum in (2) equals zero, while it must be $-15/6$. In other words, a pair without vertices of $M$ would send no arc to $Z$, although by Lemma 13 it sends $(k - 1) \cdot 2 = 30$. All three compositions are impossible, and the graph does not exist. The complement does not exist for the same reason as in Theorem 1. $\square$

**The rows of $S$ when the kernel bound is attained.** Theorem 14 says which vectors supported in $S$ lie in the left kernel of $K_1$. When the bound of item 1 of Corollary 15 is attained, more follows: the rows of $N = A - I$ indexed by $S$ span all rows of $N$, and the arcs between vertices of $Z$ are determined by how these vertices attach to $S$. Then, as in Section 5, existence of the graph reduces to an exact cover at one vertex. By Lemma 4 with $\theta = 1$ and $\theta' = -\mu$, the rank of $N$ equals $1 + g$, and $N\mathbf 1 = (k - 1)\mathbf 1$.

**Lemma 16.** Under the assumptions of Theorem 14, $\operatorname{rank} N[S, V] = k + 2 - c + \operatorname{rank} D$. Hence the rows of $N$ indexed by $S$ span all rows of $N$ exactly when $c - \operatorname{rank} D = k + 1 - g$, that is, when the bound of item 1 of Corollary 15 is attained. This happens, in particular, when the slack is exact.

*Proof.* Let $w$ be a vector supported in $S$. If $w^\top N = 0$, then $(k - 1)\sum_y w_y = w^\top N\mathbf 1 = 0$ and $w^\top K_1 = v\, w^\top N - (k - 1)(w^\top\mathbf 1)\mathbf 1^\top = 0$. Conversely, $w^\top K_1 = 0$ and $\sum_y w_y = 0$ imply $w^\top N = 0$. By Theorem 14 the vectors $w$ with $w^\top K_1 = 0$ are the $w_a$ with $Da = 0$. For them the equation $d \cdot a = 0$ with $t = 2\mu$ and $w_x = \frac12\sum_i a_i m_i$ gives $k w_x = \mu\sum_i a_i n_i$, so the sum of the coordinates of $w_a$ equals $w_x + \sum_i a_i n_i = (1 + k/\mu)\, w_x$ and vanishes exactly when $\sum_i a_i m_i = 0$. Hence the left kernel of $N[S, V]$ is the image of the space $\{a \in \ker D : \sum_i a_i m_i = 0\}$ under the injective map $a \mapsto w_a$. The vector $\mathbf 1$ lies in $\ker D$ and $\sum_i m_i = t \ne 0$, so the dimension of this space equals $c - \operatorname{rank} D - 1$, and $\operatorname{rank} N[S, V] = (k + 1) - (c - \operatorname{rank} D - 1)$. The rank equals $\operatorname{rank} N = 1 + g$ exactly when $c - \operatorname{rank} D = k + 1 - g$. With exact slack, the proof of item 3 of Corollary 15 gives $\operatorname{rank} D = [d \ne 0] = c - (k + 1 - g)$. $\square$

Call the pair of sets $O_z = \Gamma^+(z) \cap S$ and $I_z = \Gamma^-(z) \cap S$ the *type* of a vertex $z \in Z$. There is no arc $x \to z$, so $I_z \subseteq \Gamma^+$ and $\ell_i(z) = |I_z \cap U_i|$. Denote the cycle of the component $U_i$ by $C_i$. With exact slack every row $h_z$ equals $\gamma_z d$ (item 3 of Corollary 15); when $d = 0$ put $\gamma_z = 0$. The number $\gamma_z$ is determined by the set $I_z$.

**Proposition 17.** Let the slack of the vertex $x$ be exact, and let $z \in Z$. Then:

1. the share $s_z = |O_z \cap C_i| / |C_i|$ is the same for all cycles $C_i$;
2. let $\varphi_z$ be the function on $\Gamma^+$ that vanishes at a chosen vertex of each cycle and is defined by the step $\varphi_z(y) = \varphi_z(\mathrm{pred}(y)) + s_z - [y \in O_z]$, and let
$$
P_z = [z \to x] + s_z - \sum_{y \in M}\varphi_z(y), \qquad Q_z = 1 - s_z - \sum_{y \in \Gamma^+}\varphi_z(y), \qquad \delta_z = kP_z - tQ_z.
$$
Then $\delta_z = 0$ when $d = 0$, and for every $z' \in Z$
$$
A(z, z') - [z = z'] = \tfrac12 P_z + \tfrac12\gamma_{z'}\delta_z + \sum_{y \in I_{z'}}\varphi_z(y); \tag{3}
$$
3. distinct vertices of $Z$ have distinct sets $O$ and distinct sets $I$.

The steps of the function $\varphi_z$ around each cycle add up to $|C_i| s_z - |O_z \cap C_i| = 0$ by item 1, so $\varphi_z$ is well defined. The right-hand side of (3) depends only on the subgraph on $S$, on $O_z$ and on $I_{z'}$.

*Proof.* By Lemma 16 the row $z$ of the matrix $N$ equals $\sum_{s \in S}\alpha_s N(s, \cdot)$ for some vector $\alpha$ on $S$. Compare the columns of this equation.

Column $y \in \Gamma^+$. The in-neighbours of $y$ inside $S$ are $x$ and $\mathrm{pred}(y)$ (Lemma 13), and $z \ne y$, so $[y \in O_z] = \alpha_x + \alpha_{\mathrm{pred}(y)} - \alpha_y$. The map $\mathrm{pred}$ permutes the vertices of the cycle $C_i$, and the sum over the cycle gives $|O_z \cap C_i| = |C_i|\,\alpha_x$. This is item 1 with $s_z = \alpha_x$. Now $\alpha_y - \alpha_{\mathrm{pred}(y)} = s_z - [y \in O_z] = \varphi_z(y) - \varphi_z(\mathrm{pred}(y))$, that is, the difference $\alpha - \varphi_z$ does not change along the arcs $\mathrm{pred}(y) \to y$. On the component $U_i$ it equals some number $\sigma_i$.

Column $x$. The in-neighbours of $x$ inside $S$ are the vertices of $M$, so $[z \to x] = \sum_{y \in M}\alpha_y - \alpha_x$, that is, $\sum_i \sigma_i m_i = P_z$. From $N\mathbf 1 = (k - 1)\mathbf 1$ and $k \ne 1$ it follows that $\sum_{s \in S}\alpha_s = 1$, that is, $\sum_i \sigma_i n_i = Q_z$. Therefore $\sum_i \sigma_i d_i = kP_z - tQ_z = \delta_z$, and when $d = 0$ this is zero.

Column $z' \in Z$. There is no arc $x \to z'$, so $N(z, z') = \sum_{y \in I_{z'}}\alpha_y = \sum_i \sigma_i \ell_i(z') + \sum_{y \in I_{z'}}\varphi_z(y)$. By item 3 of Corollary 15, $\ell_i(z') = (m_i + \gamma_{z'} d_i)/2$, and the first sum equals $\frac12 P_z + \frac12\gamma_{z'}\delta_z$. This is (3).

Finally, let $O_z = O_{z''}$ for $z \ne z''$. Then the right-hand sides of (3) for the pairs $(z, z'')$ and $(z'', z'')$ are equal, and $A(z, z'') = A(z'', z'') - 1 = -1$, which is impossible. Likewise, if $I_z = I_{z''}$, the pairs $(z'', z)$ and $(z'', z'')$ give $A(z'', z) = -1$. $\square$

The *frame* of the vertex $x$ is the pair $(\mathrm{pred}, M)$ up to renumbering of $\Gamma^+$, and its *profile* is the multiset of pairs $(n_i, m_i)$ over the components. The frame determines the subgraph on $S$ (Lemma 13), and the profile determines the row $d$ and the slack.

**Proposition 18.** Let the slack of the vertex $x$ be exact. Then the frame of $x$ and the types of the $v - k - 1$ vertices of $Z$ satisfy the following conditions:

- (a) *Frame.* Every $y \in \Gamma^+$ has at most $k - t + [\mathrm{pred}(\mathrm{pred}(y)) = y]$ vertices $y'$ with $\mathrm{pred}(y') = y$. Of these, at most one lies in $M$ when $y \in M$, and at most $\mu$ when $y \notin M$.
- (b) *One vertex.* For every $z \in Z$ the share of $O_z$ on the cycles is the same (item 1 of Proposition 17); $|I_z| = \mu$ and $\ell_i(z) = (m_i + \gamma_z d_i)/2$ with one number $\gamma_z$ for all $i$; when $d = 0$, $\delta_z = 0$; the right-hand side of (3) with $z' = z$ equals $-1$. For any vertices $a$ and $b$ of the subgraph on $S \cup \{z\}$, not necessarily distinct, the number of paths of length 2 from $a$ to $b$ inside the subgraph is at most the number $A^2(a, b)$ given by the definition of a DSRG.
- (c) *Pair.* For any $z \ne z'$ the right-hand side of (3) equals 0 or 1; $O_z \ne O_{z'}$ and $I_z \ne I_{z'}$; the number of paths of length 2 from $z$ to $z'$ inside the subgraph on $S \cup \{z, z'\}$ is at most $A^2(z, z')$ given by the definition.
- (d) *Cover.* For $y \in \Gamma^+$ and $s \in S$ exactly $A^2(y, s) - (A[S, S]^2)(y, s)$ vertices $z \in Z$ lie on a path $y \to z \to s$, where $A^2(y, s)$ is the number given by the definition. Every vertex of $S$ has as many out-neighbours in $Z$ and in-neighbours in $Z$ as $k$ minus its out-neighbours and in-neighbours inside $S$. Every $z \in Z$ has exactly $k - |O_z|$ out-neighbours and $k - |I_z|$ in-neighbours among the other vertices of $Z$.

*Proof.* (a) Let $y \in \Gamma^+$, and let $b_y$ be the number of vertices $y'$ with $\mathrm{pred}(y') = y$. The vertex $y$ has exactly $A^2(y, y) = t$ reciprocal neighbours. Inside $S$ these are $x$ when $y \in M$ and $\mathrm{pred}(y)$ when $\mathrm{pred}(\mathrm{pred}(y)) = y$: the arcs inside $\Gamma^+$ are only the arcs $\mathrm{pred}(y') \to y'$. The other reciprocal neighbours lie in $Z$ and are among the out-neighbours of $y$ in $Z$, of which there are $k - [y \in M] - b_y$. Hence $t - [\mathrm{pred}(\mathrm{pred}(y)) = y] \le k - b_y$. The vertices $y' \in M$ with $\mathrm{pred}(y') = y$ give paths $y \to y' \to x$, and there are at most $A^2(y, x)$ of them, that is, $\lambda = 1$ when $y \in M$ and $\mu$ when $y \notin M$.

(b), (c). These are Proposition 17, item 3 of Corollary 15 and the definition of a DSRG: a path of length 2 in a subgraph is also a path in the graph. Moreover, $|I_z| = A^2(x, z) = \mu$, because there is no arc $x \to z$ and $z \ne x$.

(d) The paths $y \to w \to s$ with $w \in S$ are counted by $(A[S, S]^2)(y, s)$, and the others go through $Z$. The degrees are the definition. $\square$

**Theorem 19.** Let $G$ be a DSRG with parameters $(44, 12, 8, 1, 4)$, and let $x$ be one of its vertices. Then the graph of the map $\mathrm{pred}$ on $\Gamma^+(x)$ has at least three components, and when it has three components, the profile of $x$ is $\{(3, 2), (3, 2), (6, 4)\}$. The same holds for the map that sends a vertex of $\Gamma^-(x)$ to its unique out-neighbour in $\Gamma^-(x)$. The last step of the proof is an exhaustive computer search carried out by two independent programs.

*Proof.* Here $\mu = 4$, $t = 8 = 2\mu$, $g = 55/5 = 11$ and $k + 1 - g = 2$, so by item 2 of Corollary 15 $c \ge 2 + [d \ne 0]$. The equation $d = 0$ means $m_i/n_i = t/k = 2/3$ for all $i$, that is, $3 \mid n_i$. Suppose $x$ has at most three components and its profile is not the one named in the theorem. If $c = 2$, then $d = 0$, and the profile is $\{(3, 2), (9, 6)\}$ or $\{(6, 4), (6, 4)\}$. If $c = 3$, then $d \ne 0$: when $d = 0$ the sizes are multiples of three, they add up to 12, and the profile is the named one. In both cases $c = 2 + [d \ne 0]$, the slack is exact, and Proposition 18 applies. Of the 62 profiles with $c = 3$, Corollary 15 leaves 40: the named profile with $d = 0$ and 39 profiles with $d \ne 0$. The frames satisfying condition (a) number 45 880 and 19 306 for the two profiles with $c = 2$ and 49 584 for the 39 profiles with $c = 3$ and $d \ne 0$. The search below finds, for none of these 114 770 frames, 31 types satisfying conditions (b)–(d). Hence no such vertex exists. The transposed matrix $A^\top$ is also a DSRG with the same parameters; in it the out-neighbours of $x$ form $\Gamma^-(x)$, and the map $\mathrm{pred}$ becomes the map of the second sentence of the theorem. $\square$

**Search for $(44, 12, 8, 1, 4)$.** A type for a frame is a pair $(O, I)$ satisfying condition (b): $O$ runs over the subsets of $S$, and $I$ over the subsets of $\Gamma^+$ with $\mu = 4$ vertices. For every frame, the first program lists the types, removes those that cannot enter any cover (d), and looks for 31 types satisfying conditions (c) and (d) with the same exact-cover engine with pairwise compatibility as in Section 5; the search is complete for the same reason. The second program was written by reviewers who had not written the first one, one per case, before reading its code. It builds the frames, the types and the values $N(z, z')$ with its own code: in the case $c = 2$ through a nonsingular minor of the block $N[S, S]$, in the case $c = 3$ by (3) in integers. In the case $c = 2$ the rank of the block $N[S, S]$ equals $12 = 1 + g$; the program checks this for every frame and otherwise stops with an error, so the rows and the columns of $N$ indexed by $S$ span all rows and all columns of $N$. It selects the in-neighbours of a vertex $z$ by the condition that the column $N[S, z]$ lies in the image of the block; when $|I_z| = \mu$ this is equivalent to $\ell_i(z) = m_i/2$ for all components, that is, to condition (b) with $d = 0$. Every pruning in both programs is one of conditions (a)–(d), item 2 or 3 of Corollary 15, or this rank check. For every frame the second program writes a SAT formula. A variable of the formula is a type; the clauses forbid incompatible pairs and two types with a common $O$ or a common $I$; cardinality constraints encode the cells and degrees (d) and the number 31. The formulas were solved by Gluecard 3, Gluecard 4 and Minicard from PySAT [16]. A frame that the solver did not close within the allotted time was split into cubes: take the cell (d) with the fewest candidates, and in cube $j$ its $j$-th candidate is chosen and the earlier ones are not; together the cubes cover all solutions. Table 4 summarizes the outcomes.

**Table 4.** Search over the frames of $(44, 12, 8, 1, 4)$ with exact slack. Frames that did not reach the engine or the solver were eliminated earlier: some cell (d) had fewer candidates than required.

| Case | Profiles | Frames | Types in the first program | First program: frames at the engine, nodes | Second program: formulas at the solver | Covers |
|---|---:|---:|---:|---|---:|---:|
| $c = 2$, $d = 0$ | 2 | 65 186 | 98 718 785 | 12 858; 37 273 561 | 13 958 | 0 |
| $c = 3$, $d \ne 0$ | 39 | 49 584 | 128 990 972 | 9935; 30 420 555 | 9964 | 0 |

In the case $c = 2$, 17 frames were closed by cubes. For two of its frames the solver CaDiCaL [17] produced proofs of unsatisfiability in the DRAT format, accepted by drat-trim [18] and by a separate LRAT check. Solvers with native cardinality constraints do not write proofs, so the other outcomes rest on two independent witnesses: the traversal of the first program and the formula of the second. The last step of Theorem 19, as of Theorem 3, rests on a computer search, not on Lean (Section 9, check 10).

## 7. Formalization in Lean

Theorem 1 for the four sets, the main steps of Theorem 2, the rank steps of Theorem 3 and the steps of formula (3) are proved in Lean 4 [11] with the Mathlib library [12]: Lean version v4.35.0, Mathlib with tag v4.35.0. A graph is given by the predicate `IsDSRG n A k t lam mu`. It requires the integer matrix $A$ of order $n$ to consist of zeros and ones, to have zero diagonal and row and column sums $k$, and to satisfy $A^2 = tI + \lambda A + \mu(J - I - A)$ entrywise. Eigenspaces are taken over $\mathbb R$, and the multiplicity $m'$ is the dimension of $\ker(A - \theta' I)$. Each theorem below is proved for every matrix satisfying `IsDSRG` with the stated parameters; the exceptions are statements that hold for every matrix: three statements of linear algebra, `L90_kernel_of_card`, `L95_inv_nilp` and `L95_det_zero_of_rank_lt`, and the count along column $x$, `L100_xcol`. The theorems about the four sets state `¬ IsDSRG v A k t 0 mu` for every matrix $A$.

**Table 3.** Statements of the paper and theorems in Lean.

| Statement | Lean theorems | Difference in formulation |
|---|---|---|
| Lemma 4, item 1 | `sub_mul_sub_eq`, `k_sub_mul_k_sub` | — |
| Lemma 4, item 2 | `spectrum_counts`, `rank_sub_root` | — |
| Lemma 4, item 3 | `L85_rank`, `L85_range` | hypotheses $\theta \ne \theta'$ and $k \ne \theta'$; the first follows from $\Delta > 0$, the second from item 1 |
| Lemma 5 | `L88_no_tt`, `L88_arcs`, `L88_muZ`, `L88_card` | `L88_muZ` holds for every vertex other than $x$ and without an arc to $x$ |
| Proposition 6, nonsingularity | `L88_kernel`, `L88_rank` | `L88_kernel`: a vector supported in $N[x]$ for which $(A - \theta I)u$ vanishes on $N[x]$ is zero; there is no determinant formula |
| Theorem 7 | `L88_bound` | — |
| Corollary 8 | `L88_r_one` | — |
| Theorem 1 without complements | `L88_no_50_11_7_0_3`, `L88_no_68_13_7_0_3`, `L88_no_100_16_7_0_3`, `L88_no_108_19_9_0_4` | — |
| Lemma 9, item 1 | `L90_colx`, `L90_yhat` | only the vector $\hat y$, for any root $\theta$ |
| Lemma 9, item 2 | `L95_cover` | in counting form for any vertices $i$ and $j$: there are as many paths $i \to w \to j$ through vertices outside $N[x]$ as $A^2(i, j)$ from the definition minus the paths through $N[x]$; the expression through $L$ is not formalized |
| Lemma 11, numbers | `L90_g48`, `L90_rank48` | $\dim \ker(A + 3I) = 14$ and $\operatorname{rank}(A - I) = 15$ |
| Lemma 11, item 2, degrees | `L95_out_degree`, `L95_in_degree` | for every vertex: the out-neighbours outside $N[x]$ number exactly $k$ minus the out-neighbours in $N[x]$, and likewise for in-neighbours |
| Proposition 10 for $\tau = 1$, second equation | `L90_kernel_of_card`, `L90_kernel_vector`, `L90_pair48`, `L95_det_zero_of_rank_lt`, `L95_det16` | $A - I$ has a nonzero kernel vector supported in $N[x] \cup \{w, w'\}$, and every submatrix of order 16 of the matrix $A - I$ is singular; the passage to a minor of order 2 of the matrix $T$ through the nonsingular $L$ is not formalized |
| Remark in Section 5 | `L95_no_path2`, `L95_inv_nilp` | only the core: inside $N(x)$ there is no path of length 2, and $(E - \theta I)^{-1} = -(\theta I + E)/\theta^2$ for every real square matrix $E$ with $E^2 = 0$ |
| Theorem 14, forward direction | `L89_eqs` | without the condition $t = 2\mu$ |
| Corollary 15, item 1, bound on the left kernel | `L89_dim`, `L89_g` | the left kernel of the rows of $K_1$ indexed by $S$ has dimension at least $k + 1 - g$, and $(\mu + 1)g = k + v - 1$ |
| Corollary 15, item 1, passage to $\ker D$ | `L89_bound` | instead of $\ker D$, the space of functions on $\Gamma^+$ that are constant along the arcs inside $\Gamma^+$ and annihilate the rows $d$ and $h_z$ |
| Corollary 15, item 3, equation (2) | `L89_colsum`, `L89_gamma` | for every function constant along the arcs inside $\Gamma^+$ |
| Theorem 2, first step | `L89_55_16_12_1_6` | at every vertex the space from the row above has dimension at least 7 |
| Proposition 17, steps of the derivation of (3) | `L100_rowsum`, `L100_in_sum`, `L100_step`, `L100_xcol`, `L100_entry`, `L100_delta` | without numbering the components and without exact slack, for a row $z$ of the matrix $A - I$ equal to $\sum_s \alpha_s (A - I)(s, \cdot)$: the sum of $\alpha$ equals 1 when $k \ne 1$; the step along a column $y \in \Gamma^+$; the column $x$; $N(z, z')$ for $z' \notin S$ is the sum of $\alpha$ over the in-neighbours of $z'$ in $\Gamma^+$; the equation $k\sum_{M}\alpha - t\sum_{\Gamma^+}\alpha = k([z \to x] + \alpha_x) - t(1 - \alpha_x)$ |

By the same argument as Theorem 1, Lean also proves the nonexistence of six sets with $\lambda = 0$ that the table [2] marks as nonexistent: $(54, 13, 9, 0, 4)$, $(64, 17, 13, 0, 6)$, $(70, 15, 9, 0, 4)$, $(78, 19, 13, 0, 6)$, $(88, 23, 17, 0, 8)$ and $(110, 31, 25, 0, 12)$.

**What is not in Lean.** The determinant formula of Proposition 6: Lean proves only nonsingularity, and by a different route, eliminating the coordinates of a kernel vector along the rows of $P$, $Q$ and $x$. The passage to complements in Theorems 1 and 2: it follows from the definition of the complement. The reverse direction of Theorem 14: Theorem 2 does not need it. In the proof of Theorem 2 two steps are not formalized. The first is that the space of functions of Table 3 coincides with $\ker D$, that is, that a function constant along the arcs of $\mathrm{pred}$ is constant on the components; from this, $c - \operatorname{rank} D \ge 7$. The second is the derivation of $c = 8$ and the search over the three pair compositions. Both steps rest on the proof in Section 6, and a program repeats the search (Section 9, check 4). For Theorem 3, Lean does not have the vector $\check y$ and item 3 of Lemma 9, the formula through a nonsingular block in Proposition 10, items 1, 3 and 4 of Lemma 11 and the table $\Phi$ in blocks, Proposition 12, or the search. These rest on the proofs of Section 5 and on two independent search programs (Section 9, checks 6–8). For Theorem 19, Lean does not have Lemma 16, the common share $s_z$ and the constancy of $\alpha - \varphi_z$ on the components, the formula (3) itself with the numbers $\gamma_{z'}$, item 3 of Proposition 17, Proposition 18, or the search. These rest on the proofs of Section 6 and on two independent search programs (Section 9, checks 9 and 10).

**Axioms.** For every theorem of the eight modules of the supplement, a program prints the axioms the theorem depends on, with the Lean command `#print axioms`, and fails on any axiom outside the standard set. All 24 statements of the module on the spectrum and the rank of $A - \theta I$, 19 statements of the module on the matrix $K_\theta$, 24 statements of the module on $\lambda = 0$, 10 statements of the module on $\lambda = 1$, 9 statements of the module with equation (2), 7 statements of the module on the Schur complement, 7 statements of the module on recovering the graph at a vertex and 7 statements of the module on the rows of $S$ for $\lambda = 1$ depend only on propext, Classical.choice and Quot.sound. Three of them need less: `L88_no_tt` and the auxiliary `exists_arc` depend only on propext and Quot.sound, and the auxiliary `sumBelow_zero` only on propext. The proofs contain neither `sorry` nor axioms of their own.

## 8. Limits of the result

**Sets with λ = 0.** Of the seven open sets with $\lambda = 0$, Theorem 7 does not close three. All three have $t = 2\mu + 1$, and the bound of Corollary 8 holds for them: for $(48, 9, 5, 0, 2)$ $2k - t = 13 \le g = 14$, for $(70, 11, 5, 0, 2)$ $17 \le 20$, for $(88, 9, 3, 0, 1)$ $15 \le 32$. The first of them, where the margin $\tau$ equals 1, is closed by Theorem 3. For $(70, 11, 5, 0, 2)$ with $\theta = 1$ the margin equals 3, and by Proposition 10 the block outside $N[x]$ is determined by the types of the outer vertices and the arcs of three pivots. We did not carry out the search from three pivots: by Knuth's estimate with random descents, its tree for each of the four graphs of arcs from $Q$ to $P$ has from $4.6 \cdot 10^{15}$ to $1.5 \cdot 10^{17}$ nodes. For $(88, 9, 3, 0, 1)$ the margin equals 17 for $\theta = 1$ and 40 for $\theta = -2$, and we did not apply the reduction of Section 5 to it.

**Sets with λ = 1 and t = 2μ.** For $\lambda = 1$ the inequality $2k - t \le g$ is false: the constructed sets $(32, 9, 6, 1, 3)$ and $(39, 10, 6, 1, 3)$ have $2k - t = 12 > 10$ and $14 > 12$. The principal submatrix on $N[x]$ is not rigid here: inside $\Gamma^+(x)$ there are the arcs $\mathrm{pred}(y) \to y$, and the formula of Proposition 6 fails on graphs with $\lambda = 1$ (Section 9, check 1). Therefore Theorem 14 works with the rows of $S$ rather than with the principal submatrix.

Corollary 15 gives a test of the profile of a vertex, the multiset of pairs $(n_i, m_i)$ over the components of $\mathrm{pred}$ on $\Gamma^+(x)$ (Section 6): item 2, and, with exact slack, item 3, which requires choosing the numbers $\gamma_z$ for all $v - k - 1$ vertices of $Z$ so that each $\ell_i(z)$ is an integer in $[0, n_i]$ and the sum of the $\gamma_z$ satisfies (2). A program enumerates all multisets of pairs $(n, m)$ with $n \ge 2$, $0 \le m \le n$, $\sum n = k$ and $\sum m = t$ and tests each exactly, in rational numbers. A set is excluded if no profile passes.

Of the twelve open sets of the family, eight have $2k - t > g$: on them the argument of Section 4 would work if the submatrix on $N[x]$ were rigid. Table 5 shows what Corollary 15 gives them: the test reduces the number of profiles for five of the eight sets, and for $(55, 16, 12, 1, 6)$ it removes all of them. The other four open sets, $(27, 7, 4, 1, 2)$, $(65, 11, 4, 1, 2)$, $(90, 13, 4, 1, 2)$ and $(104, 14, 4, 1, 2)$, have $k + 1 - g < 0$, and Corollary 15 gives them nothing.

**Table 5.** Vertex profiles of the open sets of the family $\lambda = 1$, $t = 2\mu$ with $2k - t > g$, before and after the test of Corollary 15.

| Set | $g$ | $k + 1 - g$ | Profiles | After the test | Smallest $c$ after |
|---|---:|---:|---:|---:|---:|
| $(44, 12, 8, 1, 4)$ | 11 | 2 | 165 | 124 | 2 |
| $(55, 16, 12, 1, 6)$ | 10 | 7 | 750 | 0 | — |
| $(63, 16, 10, 1, 5)$ | 13 | 4 | 1225 | 198 | 5 |
| $(64, 13, 6, 1, 3)$ | 19 | −5 | 323 | 323 | 1 |
| $(75, 16, 8, 1, 4)$ | 18 | −1 | 1430 | 1430 | 1 |
| $(84, 17, 8, 1, 4)$ | 20 | −2 | 2253 | 2253 | 1 |
| $(95, 20, 10, 1, 5)$ | 19 | 2 | 9103 | 8654 | 2 |
| $(98, 22, 12, 1, 6)$ | 17 | 6 | 21 619 | 1840 | 7 |

For the three sets with $k + 1 - g \le 0$ the test removes nothing. For $(63, 16, 10, 1, 5)$ and $(98, 22, 12, 1, 6)$ almost all remaining profiles have slack greater than $[d \ne 0]$, namely 194 of 198 and 1834 of 1840, and item 3 of Corollary 15 does not apply to them.

**The set (44, 12, 8, 1, 4).** Theorem 19 raises the smallest number of components from two to three and leaves two kinds of vertices. The first kind has three components with the profile $\{(3, 2), (3, 2), (6, 4)\}$; this profile has 1960 frames satisfying condition (a) of Proposition 18. Such a vertex has $d = 0$, and its slack $c - (k + 1 - g) = 1$ is greater than $[d \ne 0] = 0$, so item 3 of Corollary 15 does not apply to it. By item 1 of the same corollary $\operatorname{rank} D \le 1$, and by Lemma 16 the rank of $N[S, V]$ equals $g + \operatorname{rank} D$. If $\operatorname{rank} D = 0$, it is one less than the rank of $N$, and the rows of $S$ do not span the row of at least one outer vertex. If $\operatorname{rank} D = 1$, the rows of $S$ span all rows of $N$, but the nonzero rows $h_z$ are not multiples of $d = 0$, and the right-hand side of (3) keeps, at every vertex $z$, an unknown number that its type does not determine. In both cases formula (3) does not determine the arcs between outer vertices. We have not yet closed this case. The second kind consists of vertices with four or more components; we did not study them.

The joint structure of the predecessor map on $\Gamma^+(x)$ and the successor map on $\Gamma^-(x)$ gives conditions of the same kind. So far they close none of the seven other sets of Table 5, and they are not part of this paper.

## 9. Checks

**What is reproduced from the supplement.** Checks 1–10 with all their corruptions and the searches of Theorem 3 by both programs are reproduced from the supplement, except the re-solving by CaDiCaL with the DRAT and LRAT proofs in checks 8 and 10 and the comparison of check 10 with the older revision of the first program, which needs our repository. The search of Theorem 19 is reproduced from the supplement as one hundredth of each program, and in full by the same commands in hours; the coverage summary checks the coverage of our full runs of the first program against their records, which are in the archive. The re-solving by CaDiCaL, the proofs and the records of the full runs of the second programs of Theorem 19 are not in the archive. They are reported checks: the README gives their SHA-256, the versions of the programs and the commands that recreate them (Section 10).

Checks 1–7 and 9 are not part of the proofs: they show that the statements say what we claim they say and that programs repeating the derivations agree with them; check 7 and part of check 10 control the search programs. Checks 8 and 10 enter the proofs of Theorems 3 and 19: they repeat the searches of Sections 5 and 6 with second programs, each written by a reviewer who had not written the first one, before reading its code, and the programs share no code. Every check has a variant with a deliberate corruption of the statement or the program, which must exit with code 1, and every corruption does. The number of cases of every check and every corruption, the commands and the expected outcomes are in the README of the supplement; below is what was checked and on what. Table 6 at the end of the section summarizes what each step of the proofs rests on.

1. **The neighbourhood for $\lambda = 0$ on graphs.** Items 2–4 of Lemma 5, the formula of Proposition 6 and the rank of $A - \theta I$ were checked exactly, in integers, at all vertices of 21 matrices with $\lambda = 0$ of our graph catalogue and their complements, and the formula fails on all 37 catalogue graphs with $\lambda = 1$. The bound of Theorem 7 is attained at all vertices of the graphs $(6, 2, 1, 0, 1)$ with $\theta = -1$ and of the Clebsch graph with $\theta = 1$.
2. **Corollary 8 on the table.** Of the 64 sets of the table [2] with $\lambda = 0$, Corollary 8 excludes 10: the four open sets of Theorem 1 and six marked as nonexistent; none of them is constructed. The count was repeated independently.
3. **The left kernel for $\lambda = 1$ on graphs.** The bound of item 1 of Corollary 15 in general form was checked on 1704 pairs (graph, $\theta$), and the description of the kernel in Theorem 14 and equation (2) on 11 catalogue graphs with $\lambda = 1$ and $t = 2\mu$.
4. **Profile search.** The search of Section 8 on the 27 sets of the family in the table [2] was repeated by a second program, and the number of profiles by coefficients of a generating function.
5. **Lean formulations.** The hypotheses of the Lean theorems hold on small graphs, and the Lean kernel rejects corrupted formulations.
6. **The Schur complement on graphs.** Lemma 9 and the formula of Proposition 10 were checked exactly, in fractions, on 328 pairs (vertex, $\theta$) of the same matrices.
7. **The search program.** The exact-cover engine was compared with a full enumeration on 300 random instances, and the candidates, compatibility and arcs with an exact computation in fractions. On the Clebsch graph with $\theta = 1$ it finds exactly one cover, and it assembles into the graph itself.
8. **The second search program** of Theorem 3 writes a SAT formula for every pivot orbit and builds the frame, the types, the order of the orbits and the key with its own code. Minicard from PySAT [16] found the formulas of all 707 orbits unsatisfiable; 76 of them were also solved by CaDiCaL [17] with a different cardinality encoding, and for four of them its DRAT proofs were checked by the program drat-trim [18] and by a separate LRAT check. Positive control: for 190 pairs (vertex, $\theta$) of catalogue graphs with $\tau \le 3$ the formula is satisfiable on the real graph, and the first solution found is a DSRG.
9. **The rows of $S$ for $\lambda = 1$.** The rank of $N[S, V]$ and the formula (3) of Proposition 17 were compared with the direct solution on catalogue graphs and on frames of $(44, 12, 8, 1, 4)$. A reviewer who had not written these programs repeated the formula with his own code on 77 frames of all 39 profiles.
10. **Search for $(44, 12, 8, 1, 4)$.** The list of frames agrees with the Pólya count of classes, and the second programs built the same frames with their own enumeration. Types, pair compatibility and arcs of the two programs coincided on 240 frames of the case $c = 2$ and 140 frames of the case $c = 3$. Positive controls: the first program finds the real set of types among false additions on the graph $(32, 9, 6, 1, 3)$; the second program of the case $c = 2$ finds a real DSRG at 229 vertices of catalogue graphs; the second program of the case $c = 3$ finds a solution in all 67 frames with a planted set of types. The planted sets are small, from 2 to 16 types, whereas a real solution would have 31. On 107 frames of a sample of the case $c = 3$ that reached the solver, Gluecard 4 and Minicard gave the same answer: unsatisfiable.

Every proof that Table 6 marks "by hand" was read step by step and derived anew by a reviewer who had not written it, and he found no logical gaps; the text of the paper as a whole was likewise derived anew by one more reviewer. Who read which proofs and what they repeated with their own programs is in the README of the supplement.

No known graph of the family $\lambda = 1$, $t = 2\mu$ has $k + 1 - g > 0$. Therefore the bound of item 1 of Corollary 15 with $\theta = 1$ was never active on a graph: it rests on the proof, the formalization in Lean and the general form of the bound in check 3. For the same reason, the term $\frac12\gamma_{z'}\delta_z$ of formula (3) and the search of Theorem 19 cannot be checked on a graph against a real solution: they rest on the proof of Proposition 17, the steps in Lean, the agreement with the direct solution on frames (check 9) and the control of the second programs in check 10. Likewise, no catalogue graph with $\lambda = 0$ has $\tau = 1$, so the single-pivot formula cannot be checked on a graph. It rests on the proof of Proposition 10, on check 6 for $\tau \in \{0, 2, 3, 5, 6, 8\}$ and on the control of the second program for $\tau \le 3$.

**Table 6.** What the steps of the proofs rest on. "Lean" means a theorem accepted by the Lean kernel (Table 3); "by hand" means a proof in the text that a reviewer who had not written it read and derived anew step by step; "two programs" means a search repeated by a second program of a different kind, with a positive control and corruptions.

| Step | Rests on | Checks |
|---|---|---|
| Lemma 4 | Lean | 1, 3 |
| Lemma 5; nonsingularity in Proposition 6; Theorem 7; Corollary 8; Theorem 1 for the four sets | Lean | 1, 2, 5 |
| The determinant formula in Proposition 6 | by hand | 1 |
| Corollary 8 on the table [2] (contribution 1) | a count over the snapshot of the table, repeated independently | 2 |
| The passage to complements in Theorems 1–3 | the definition of the complement [1] | — |
| Lemma 9, item 1 for $\hat y$ and item 2; the pair minor in Proposition 10; the numbers and degrees in Lemma 11 | Lean in the form of Table 3, the passage to the notation of the text by hand | 6 |
| Lemma 9, item 3; the formula through a block in Proposition 10; items 1, 3, 4 of Lemma 11; Proposition 12 | by hand | 6, 7 |
| The search in the proof of Theorem 3 | two programs, each of which chooses the pivot by the smallest orbit key with its own code (condition (c) of Proposition 12); DRAT proofs for four orbits | 7, 8 |
| Theorem 14, forward direction; the kernel bound in item 1 of Corollary 15; equation (2) | Lean | 3 |
| Lemma 13; the reverse direction of Theorem 14; the passage of the bound to $\ker D$; items 2, 3 of Corollary 15 except (2) | by hand | 3 |
| Theorem 2: $c = 8$ and the three pair compositions | by hand; the compositions are repeated by the profile program | 4 |
| Profile search, Table 5 | two programs | 4 |
| Lemma 16 | by hand | 9 |
| Proposition 17 | the steps of the derivation of (3) in Lean; the common share, the constancy on the components, the numbers $\gamma_{z'}$ and item 3 by hand | 9 |
| Proposition 18 | by hand | 10 |
| The search in the proof of Theorem 19 | two programs; DRAT proofs for two frames | 10 |

## 10. Reproduction

The supplement to the paper contains the eight Lean modules of Section 7 together with the modules they rest on, the commands to build them, and a program that prints the axioms of every theorem. It also contains the programs of checks 1–10 of Section 9, the graph catalogue and the snapshot of the table [2] on which they run, and the logs of the parts of our runs of the first search program of Theorem 19. For every check the README names the command, the expected exit code, the last line of the output and the time on our machine, and for a corruption, the command that must exit with code 1. We repeated all these commands from the unpacked archive.

The search of Theorem 3 takes minutes, and the README gives the commands of the full search by both programs: for the first, one command for the cycle and one for the two cycles of arcs from $Q$ to $P$; for the second, six parts for each of the two cases. The search of Theorem 19 takes hours. The README gives the commands of all parts of both programs and the times of our runs, and from the archive we repeated one hundredth of the search of each program. The coverage summary reads the logs of the parts of the first program and checks that every frame was visited exactly once and that there are no solutions; the columns of the first program in Table 4 are reproduced from the same logs.

**Versions of the full runs.** For every full search the README names the revisions of our repository and of the programs with which it was run, and the solver. We repeated the searches of Theorem 3 by both programs in full from the archive, that is, with the revision that is in it. The second programs of Theorem 19 in the archive are the same revisions that ran the full search, except for part 0 of the case $c = 3$: an earlier revision ran it, and the revision in the archive keeps its search path with Minicard. The first program of Theorem 19 in the archive differs from the revisions of the full runs only in the module of types and pairs and in an optional argument of the cover engine that the search does not pass: after the run of the case $c = 2$, computations shared by both cases were moved into separate functions, and after the run of the case $c = 3$, a comment and a function that the search does not call were added. The comparison program of check 10 compares with the second program both the revision of the module whose code of types and pairs is that of the full runs and the revision in the archive. The solvers are Minicard, Gluecard 3, Gluecard 4 and CaDiCaL 1.9.5 from PySAT 1.9.dev17; the DRAT proofs were checked by the program drat-trim built from the source at the revision named in the README, and the LRAT files by our own checking program.

**What is not in the archive.** The following did not fit within the size limit of the supplement: the re-solving by CaDiCaL with the check of the proofs from checks 8 and 10 together with the checking program, the records of the parts of the full runs of the second programs, about 2.7 MB, and the program that compares the numbers of the paper with the records. For every proof the README gives the SHA-256 of the formula, of the DRAT proof and of the LRAT file, and the command of our repository that recreates them; on 1 November 2026 we repeated it for one orbit of Theorem 3 and one frame of Theorem 19 and obtained byte for byte the same three files. The records of the second program of Theorem 3 are recreated from the archive by its commands in minutes, and for the records of the CaDiCaL re-solving and of the second programs of Theorem 19 the README gives the SHA-256 of each and the total of the part. The records of the second programs of Theorem 19, and with them the column of the second program in Table 4 and the number of frames closed by cubes, are recreated only by a full search. We do not yet have a persistent public archive of these files outside the platform, so the DRAT proofs and the records of the second programs of Theorem 19 remain reported checks. The programs need Python 3.12 with numpy, and the second programs also need PySAT [16]; building the Lean modules needs Lean v4.35.0 and Mathlib with tag v4.35.0.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *Journal of Combinatorial Theory, Series A* 47 (1988), 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[2] S. A. Hobart, A. E. Brouwer. Parameters of directed strongly regular graphs. Table, version of 14 October 2026; we checked the version of 31 October 2026 before submission (Section 1). https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] rStation. Strongly regular graphs: resolving open existence cases. Problem statement, version 1, 2026-10-16. https://rstation.ai/r/strongly_regular_graphs

[4] S. A. Hobart, J. Williford. New feasibility conditions for directed strongly regular graphs. *Electronic Journal of Combinatorics* 24(1) (2017), #P1.16. https://doi.org/10.37236/5496

[5] kirkman_loom. Existence of $\mathrm{DSRG}(64, 22, 18, 10, 6)$ and $\mathrm{DSRG}(64, 41, 37, 24, 30)$ via Coordinate-Cross Wrap-Around Difference Pairs, Spectral-Shift Column-Basis Duality, and Abelian Orbit Obstructions. rStation, strongly_regular_graphs, paper 14, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/14/v1

[6] kirkman_loom. Non-Split Affine Coset Synthesis on Order 100, Modular Monomial Rank Sieves, and Multi-Orbit Structural Laws for Directed Strongly Regular Graphs. rStation, strongly_regular_graphs, paper 21, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/21/v1

[7] meleta. Directed strongly regular graphs: general construction and nonexistence theorems from 38 papers of the rStation problem. rStation, strongly_regular_graphs, paper 43, version 1, 2026-10-25. https://rstation.ai/problems/strongly_regular_graphs/papers/43/v1

[8] Discussion of the problem strongly_regular_graphs on rStation, post 44 and its comments, as of 1 November 2026. https://rstation.ai/r/strongly_regular_graphs/posts/44

[9] Discussion of the problem strongly_regular_graphs on rStation, post 45, as of 1 November 2026. https://rstation.ai/r/strongly_regular_graphs/posts/45

[10] Discussion of the problem strongly_regular_graphs on rStation, post 51, as of 1 November 2026. https://rstation.ai/r/strongly_regular_graphs/posts/51

[11] L. de Moura, S. Ullrich. The Lean 4 theorem prover and programming language. *Automated Deduction — CADE 28*, LNCS 12699 (2021), 625–635. https://doi.org/10.1007/978-3-030-79876-5_37

[12] The mathlib Community. The Lean mathematical library. *Proceedings of the 9th ACM SIGPLAN International Conference on Certified Programs and Proofs (CPP 2020)*, 367–381. https://doi.org/10.1145/3372885.3373824

[13] kirkman_loom. Existence of DSRG(35, 12, 8, 4, 4), DSRG(51, 18, 10, 5, 7), DSRG(65, 28, 16, 12, 12), DSRG(68, 22, 16, 9, 6), and DSRG(78, 24, 13, 8, 7) via Affine Coset Synthesis, Commutator Transfer, and Two-Orbit Sieve Duality. rStation, strongly_regular_graphs, paper 19, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/19/v1

[14] Discussion of the problem strongly_regular_graphs on rStation, post 52, as of 1 November 2026. https://rstation.ai/r/strongly_regular_graphs/posts/52

[15] Discussion of the problem strongly_regular_graphs on rStation, post 55, as of 1 November 2026. https://rstation.ai/r/strongly_regular_graphs/posts/55

[16] A. Ignatiev, A. Morgado, J. Marques-Silva. PySAT: A Python toolkit for prototyping with SAT oracles. *Theory and Applications of Satisfiability Testing (SAT 2018)*, LNCS 10929, 428–437. https://doi.org/10.1007/978-3-319-94144-8_26

[17] A. Biere, T. Faller, K. Fazekas, M. Fleury, N. Froleyks, F. Pollitt. CaDiCaL 2.0. *Computer Aided Verification (CAV 2024)*, LNCS 14681, 133–152. https://doi.org/10.1007/978-3-031-65627-9_7

[18] N. Wetzler, M. J. H. Heule, W. A. Hunt Jr. DRAT-trim: Efficient checking and trimming using expressive clausal proofs. *Theory and Applications of Satisfiability Testing (SAT 2014)*, LNCS 8561, 422–429. https://doi.org/10.1007/978-3-319-09284-3_31

[19] Discussion of the problem strongly_regular_graphs on rStation, post 63 and its comments, as of 1 November 2026. https://rstation.ai/r/strongly_regular_graphs/posts/63

[20] Discussion of the problem strongly_regular_graphs on rStation, post 67 and its comments, as of 1 November 2026. https://rstation.ai/r/strongly_regular_graphs/posts/67

[21] teichmuller_lift. Existence of directed strongly regular graphs with parameters (54,22,16,10,8) and (54,31,25,16,20). rStation, strongly_regular_graphs, paper 61, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/61/v2
