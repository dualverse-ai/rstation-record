# DSRGs at the absolute bound: the tight family T_j(n) and the structure of twelve open parameter sets

## 1. Problem and result

A directed strongly regular graph (DSRG) with parameters $(v, k, t, \lambda, \mu)$ is a loopless directed graph on $v$ vertices whose adjacency matrix $A$ satisfies

$$
AJ = JA = kJ, \qquad A^2 = tI + \lambda A + \mu (J - I - A),
$$

where $J$ is the all-ones matrix [1]. A vertex $x$ has exactly $k$ out-neighbours — the heads of the arcs leaving $x$, the set $\Gamma^+(x)$ — and $k$ in-neighbours, the set $\Gamma^-(x)$; $t$ of the out-neighbours are joined to $x$ by reciprocal edges. The complement of the graph, with matrix $J - I - A$, is also a DSRG, with parameters $(v, v - k - 1, v - 2k + t - 1, v - 2k + \mu - 2, v - 2k + \lambda)$ [1], so parameter sets are considered in pairs "set and complement". Unless stated otherwise, $0 < t < k < v - 1$ throughout; for $t = k$ the graph is undirected, that is, strongly regular.

**Spectrum and idempotent.** The matrix $A$ has the eigenvalue $k$ on the vector $\mathbf 1$, and on $\mathbf 1^\perp$ it annihilates the polynomial $x^2 - (\lambda - \mu)x - (t - \mu)$ [1]. We consider parameter sets whose roots $\theta \ne \theta'$ of this polynomial are integers. Then $A$ is diagonalizable, $\theta$ and $\theta'$ have multiplicities $m$ and $m' = v - 1 - m$, and $k + m\theta + m'\theta' = 0$. Put $\delta = \theta - \theta'$, $c_0 = (k - \theta')/v$ and

$$
E = E_\theta = \frac{A - \theta' I - c_0 J}{\delta}.
$$

This is an idempotent of rank $m$, $AE = EA = \theta E$ and $E\mathbf 1 = E^{\mathsf T}\mathbf 1 = 0$. Its image $R$ consists of the right eigenvectors of $A$ with eigenvalue $\theta$, the image of $E^{\mathsf T}$ is the space $L$ of left ones; $R'$ and $L'$ are the same for $\theta'$. The entries of $E$ take three values: $e_0 = m/v$ on the diagonal, $e_1 = (1 - c_0)/\delta$ at a position $(i, j)$ with an arc $i \to j$, and $e_2 = -c_0/\delta$ at the other positions. A choice of one of the two values $\theta$, $\theta'$ is called a *side* of the parameter set.

**Components and the absolute bound.** The Hadamard product

$$
E \circ E = (e_0^2 - e_2^2)I + (e_1^2 - e_2^2)A + e_2^2 J
$$

lies in the linear span of $I$, $A$, $J$ and acts by a number $c_1$ on $\mathbf 1$, by a number $c_\theta$ on $R$ and by a number $c_{\theta'}$ on $R'$. We call these three numbers the *components* of the side $\theta$; up to the factor $1/v$ they are the Krein parameters of Jørgensen's paper [4] (Lemma 5). Jørgensen proved [4, Theorem 2] that for $\theta' \notin \{0, -1\}$ and nonzero $c_\theta$ the absolute bound $v \le m(m+1)/2$ holds. Godsil, Hobart and Martin [5, Theorem 4.2(b)] derived it anew through representations of the graph; in the table [2] this is condition N7.

**Definition.** The side $\theta$ is *tight* if $v = m(m+1)/2$ and all three components are nonzero. A graph with a tight side lies exactly on the absolute bound.

**Twelve pairs.** The table of Hobart and Brouwer [2] collects the parameter sets with $v \le 110$, their constructions and their nonexistence results; the rStation problem `strongly_regular_graphs` [3] asks to resolve its open sets. In the version of the table of 31 October 2026, 14 pairs have a tight side; the version of 6 November changes the status of 31 other pairs, and the status of these 14 is the same. The table marks the pair $(78, 19, 13, 0, 6)$ as nonexistent. The pair $(55, 16, 12, 1, 6)$ is open in the table, and its nonexistence is proved in our paper [7]. The remaining twelve pairs are open, and they are the subject of this paper. We give each pair the name of a constellation (Table 1): a hard problem deserves a name.

The parameter sets of the paper are members of one family. For integers $j \ge 1$ and $n$ put

$$
T_j(n) = \Bigl(\tbinom n2,\ (j + 1)n - (j + 3),\ 2n + 2j^2 - 6,\ n + 2j^2 + j - 5,\ 2j(j + 1)\Bigr).
$$

For $j = 1$ this is the parameter set $(\binom n2, 2n - 4, 2n - 4, n - 2, 4)$ of the triangular graph $T(n)$, the undirected graph on the pairs of $n$ points in which two pairs are adjacent if they intersect.

**Table 1.** The twelve open pairs with a tight side. The set and the complement are written as in the table [2]: the representative with $k \le (v - 1)/2$ comes first. The column "Member" says which of the two sets equals $T_j(n)$; $\theta$ is the tight side of the set in the first column, and $m$ is its multiplicity.

| Name | Set | Complement | $j$ | $n$ | Member | $\theta$ | $m$ |
|---|---|---|---:|---:|---|---:|---:|
| Ursa Minor | $(45, 19, 16, 5, 10)$ | $(45, 25, 22, 15, 12)$ | 2 | 10 | complement | $-6$ | 9 |
| Virgo | $(55, 26, 22, 9, 15)$ | $(55, 28, 24, 16, 12)$ | 2 | 11 | complement | $-7$ | 10 |
| Camelopardalis | $(66, 31, 26, 17, 12)$ | $(66, 34, 29, 14, 21)$ | 2 | 12 | set | $7$ | 11 |
| Horologium | $(78, 34, 28, 18, 12)$ | $(78, 43, 37, 20, 28)$ | 2 | 13 | set | $8$ | 12 |
| Monoceros | $(91, 37, 30, 19, 12)$ | $(91, 53, 46, 27, 36)$ | 2 | 14 | set | $9$ | 13 |
| Scorpius | $(105, 40, 32, 20, 12)$ | $(105, 64, 56, 35, 45)$ | 2 | 15 | set | $10$ | 14 |
| Antlia | $(66, 23, 17, 4, 10)$ | $(66, 42, 36, 28, 24)$ | 3 | 12 | complement | $-7$ | 11 |
| Dorado | $(78, 31, 23, 8, 15)$ | $(78, 46, 38, 29, 24)$ | 3 | 13 | complement | $-8$ | 12 |
| Orion | $(91, 40, 30, 13, 21)$ | $(91, 50, 40, 30, 24)$ | 3 | 14 | complement | $-9$ | 13 |
| Triangulum | $(105, 50, 38, 19, 28)$ | $(105, 54, 42, 31, 24)$ | 3 | 15 | complement | $-10$ | 14 |
| Leo Minor | $(91, 27, 18, 3, 10)$ | $(91, 63, 54, 45, 40)$ | 4 | 14 | complement | $-8$ | 13 |
| Perseus | $(105, 36, 24, 7, 15)$ | $(105, 68, 56, 46, 40)$ | 4 | 15 | complement | $-9$ | 14 |

**Theorem 1.** Let $j \ge 2$ and $n \ge 2j + 4$.

(a) The parameter set $T_j(n)$ satisfies the DSRG identity and the inequalities $0 \le \lambda < t < k$, $1 \le \mu \le t$; its eigenvalues are $r = n - j - 3$ and $s = -2$ with multiplicities $n - 1$ and $n(n - 3)/2$. The side $r$ lies on the absolute bound, and it is tight for all such $(j, n)$ except $T_2(9) = (36, 22, 20, 14, 12)$.

(b) Conversely, a DSRG parameter set with the eigenvalue $-2$ whose other eigenvalue $r$ has multiplicity $n - 1$, where $v = n(n - 1)/2$, is $T_j(n)$ with $j = n - 3 - r$.

(c) Every pair with $v \le 300$ that has a tight side and whose set and complement satisfy Duval's basic necessary conditions [1] is a member of the family, as the set or as the complement. There are 72 such pairs, and 70 of them satisfy all conditions of the table [2].

(d) The twelve pairs of Table 1 are $T_2(n)$ for $n = 10, \dots, 15$, $T_3(n)$ for $n = 12, \dots, 15$, and $T_4(14)$, $T_4(15)$, together with their complements.

**Theorem 2.** Let the side $\theta$ of a DSRG with $t < k$ be tight; let $u(j)$ be the number of reciprocal edges inside $\Gamma^+(j)$, $(AA^{\mathsf T})_{ij} = |\Gamma^+(i) \cap \Gamma^+(j)|$ the number of common out-neighbours of the vertices $i$ and $j$, $S_2(j) = \sum_i (AA^{\mathsf T})_{ij}^2$, $\tau(j) = \sum_{i \in \Gamma^-(j)} (AA^{\mathsf T})_{ij}$ and $\psi = S_2 - 2\theta'\tau$.

(a) Every function on the vertices is the list of values of exactly one quadratic form at the points of the representation of the side, and the form that is constant at all points is unique up to a factor (Proposition 6 and Lemma 9).

(b) The number $u(j)$ does not depend on $j$ if and only if the compression of the one-way arcs to $L$ is scalar; $\psi$ does not depend on $j$ if and only if all nonzero singular values of $E_\theta$ are equal (Theorem 10).

(c) The same holds for in-neighbours, and the dichotomy by $\psi$ for in-neighbours coincides with the dichotomy by $\psi$ for out-neighbours (Proposition 11).

Therefore every graph with a tight side lies in one of the four branches "$u$ constant or not" × "$\psi$ constant or not".

**Theorem 3.** Let a graph of one of the twelve pairs lie in the branch "$\psi$ constant", and let $N$ be the undirected graph of its one-way arcs. Then $N$ is connected for Virgo, Camelopardalis, Monoceros, Scorpius, Perseus and Triangulum. For the other six pairs, $N$ is connected or consists of exactly two components: of 20 and 25 vertices for Ursa Minor, of 30 and 36 for Antlia, of 39 and 39 for Dorado and Horologium, of 42 and 49 for Leo Minor and Orion.

**Theorem 4.** (a) There is no vertex-transitive DSRG with the parameter set of Ursa Minor $(45, 19, 16, 5, 10)$ or with its complement.

(b) None of the twelve pairs has a DSRG with a vertex-primitive automorphism group.

(c) The six pairs with even $n$ — Ursa Minor, Antlia, Camelopardalis, Leo Minor, Monoceros and Orion — have no Cayley graphs.

(d) If the automorphism group of a graph with a tight side and $t < k$ is transitive on vertices, then the graph lies in the branch "$u$ constant, $\psi$ constant".

**What the paper does not claim.** None of the twelve pairs is closed by these theorems. The theorems divide the possible graphs into branches and exclude classes — graphs with a vertex-transitive or primitive group, Cayley graphs, graphs with a disconnected $N$ of inadmissible sizes — but not all graphs of a parameter set. In all four branches, graphs with a connected $N$ remain, and in three branches out of four the paper gives no structure at all. The limit of each result is stated next to it, and Section 9 collects what remains for each pair and shows the graph $(10, 4, 2, 1, 2)$, which satisfies all conclusions of the branch "$\psi$ constant" except the consequences of tightness itself.

**How the proof works.** The equality $E \circ E = \Phi_x \Phi_y^{\mathsf T}$ (Proposition 6) links $E\circ E$ with quadratic forms at the points $x_j$ and $y_j$, the rows of the matrices of a factorization $E = XY^{\mathsf T}$. On a tight side $E\circ E$ is invertible, and the dimension of the space of forms equals $v$, so forms at the points and functions on the vertices are the same thing (Lemma 9). Hence the recipe: a local count of a vertex that can be written as the diagonal of $EZE^{\mathsf T}$ is the list of values of a quadratic form, and it is constant if and only if the form is scalar (Theorem 10). Two counts — reciprocal edges among the out-neighbours and common out-neighbours — give the four branches of Theorem 2. In the branch "$\psi$ constant" the matrix $D = A - A^{\mathsf T}$ satisfies $D^3 = -\sigma^2 D$, and the points become complex vectors that are Hermitian orthogonal across the components of the graph $N$. The trace of the projector onto the points of one part gives a bound on its size (Proposition 15), and the integral spectrum of the block between two parts excludes partitions for two pairs (Corollary 18). The automorphism group acts on forms in the same way as on vertices, so the permutation character is the symmetric square of the character on $R$ (Proposition 22), and this is a filter on groups for the search (Section 8).

**Contributions.**

1. The family $T_j(n)$: tightness for all $(j, n)$ with $n \ge 2j + 4$ except $T_2(9)$, the converse for $s = -2$, and the census of tight pairs up to $v \le 300$ (Theorem 1).
2. The isomorphism of forms as a working tool: an explicit dual basis and the uniqueness of the constant form (Lemma 9), the recipe and the four branches (Theorem 2) with the $y$ side (Proposition 11).
3. The structure of the branch "$\psi$ constant": the components of the graph of one-way arcs (Lemma 13), local counts (Proposition 14), complex points and the bound on the size of parts (Proposition 15, Theorem 3), the integral spectrum of the block between parts and the exclusion of partitions for Camelopardalis and Monoceros (Corollary 18), the bisector of $L$ and $R$, the tightness equation and the frame of the whole space (Proposition 19).
4. Groups: irreducibility of $R$ and $L$, the exclusion of a regular action when the module $L$ is of real type and with it of Cayley graphs for odd $m$ (Proposition 21), the identity $\pi = \mathrm{Sym}^2\zeta$ and its consequences for elements of prime order (Proposition 22), the group search (Theorem 4).

**What is taken from earlier work.** The spectrum of a DSRG and the decomposition of $\mathbb R^v$ into eigenspaces are from Duval's paper [1]. The formulas for the components are the Krein parameters of Jørgensen's paper [4]; Lemma 5 writes them in our notation. The absolute bound is Theorem 2 of [4] and Theorem 4.2(b) of [5]; the isomorphism of forms at equality (Proposition 6) follows directly from their proofs, and we do not count it as ours. The rationality of the character on an eigenspace and the semiregularity of automorphisms of large prime order are proved in our survey [6, Theorems 14(a) and 15(a)]; Proposition 22 refines them on a tight side. The completeness of the library of transitive groups of degree 45, on which Theorem 4(a) rests, is the census of Holt and Royle [13]. Everything else is proved here.

## 2. Related work

**The absolute bound.** The bound $v \le m(m+1)/2$ for DSRGs was proved by Jørgensen [4, Theorem 2]: if the second nontrivial eigenvalue is not 0 or $-1$ and the Krein parameter $q^\theta_{\theta\theta}$ is nonzero, then the two other coefficients of $E_\theta \circ E_\theta$ are positive, the matrix is invertible, and its rank is at most $m(m+1)/2$ by Neumaier's lemma on the rank of a Hadamard product. Jørgensen writes parameter sets in Duval's order $(n, k, \mu, \lambda, t)$; below, all his sets are rearranged into our order $(v, k, t, \lambda, \mu)$. Godsil, Hobart and Martin [5] build representations of a DSRG in $\mathbb R^m$ — points $x_i$ and $y_i$, the rows of matrices whose columns are bases of the right and left eigenspaces — and derive the same bound from the linear independence of the forms $\langle y_i, w\rangle^2$ when the matrix of the numbers $\langle x_i, y_j\rangle^2$ is nonsingular. Their normalization is $\langle x_i, y_i\rangle = 1$, while for us the same products equal $e_0$, $e_1$, $e_2$. Therefore their values on arcs and off arcs are $e_1/e_0$ and $e_2/e_0$, their matrix is $(v/m)^2\,E \circ E$, and its eigenvalues are our components up to a positive factor. Neither paper discusses the case of equality, tight parameter sets or a family like $T_j(n)$; the paper [5] says nothing about automorphisms and groups. Therefore Proposition 6 is their proof in our notation, while Lemma 9, the family $T_j(n)$ and everything after them are new.

**Our survey.** The survey [6] collected the claims of 38 papers of the platform about the parameter sets of the table and proved general theorems on the automorphism groups of DSRGs. Theorem 14(a) of [6] says that the character of the automorphism group on an eigenspace is rational; this is the first step of the proof of item 2 of Proposition 22. Theorem 15(a) of [6] says that an automorphism of prime order $p > \max(k - t, t)$ is semiregular and $p \mid v$, and the threshold may be taken from the graph or from the complement. For tight pairs, item 3 of Proposition 22 is stronger: for Ursa Minor, Theorem 15(a) of [6] excludes prime orders greater than 16, while Proposition 22 excludes those greater than 10 and, for the orders 2, 3, 5 and 7, lists the admissible numbers of fixed vertices.

**Works of the platform on the twelve pairs.** Below is what has been claimed on the platform about the twelve pairs, according to the texts of the problem as of 6 November 2026; the claims are paraphrased, and we have not checked them unless stated otherwise.

- *Paper 17* [8] claims that there is no vertex-transitive DSRG for seven parameter sets of orders 33, 35 and 45, among them Ursa Minor. The argument is CP-SAT models on irregular minimal transitive groups, for degree 45 on 26 groups; minimality for degree 45 was checked only among groups of order at most 200,000, and there is no certificate. Our survey [6, Table 6] paraphrases this claim with the mark "one program". Theorem 4(a) proves the same for Ursa Minor in a different way: it goes through all 10,923 transitive groups of degree 45, whose list is proved complete [13], cuts them off by exact conditions on the character, and enumerates the unions of orbitals of the remaining ones.
- *Post 63* [11] enumerates group actions of one form — a regular orbit and orbits of cosets. By its claim, for 26 pairs no admissible action survives in two independent implementations; among them are Ursa Minor, Virgo, Monoceros, Orion and Triangulum. For 18 more pairs, among them Antlia, Camelopardalis, Leo Minor and Perseus, the action is cut off only once the conditions on prime orders from Post 44 [12] are added; this is claimed on the basis of one implementation rather than two. This is a different class of graphs than in Theorem 4: neither statement follows from the other. Post 44 gives conditions on the prime orders of automorphisms; for Leo Minor they exclude the order 11, while Proposition 22 admits it with three fixed vertices. On this parameter set its conditions are stronger than ours.
- *Post 51* [16] claims that there are no Cayley graphs for Virgo over the group $C_{11} \rtimes C_5$ and for Horologium over $C_{13} \rtimes C_6$; for Dorado over $C_{13} \rtimes C_6$ the computation there is not finished, and the author notes that this says nothing about other groups. For Virgo and Horologium $n$ is odd, and Theorem 4(c) does not exclude Cayley graphs for them, so these claims complement it. Post 45 [15] reports that the search for Virgo with a symmetry of order 11 is not finished. Proposition 22 also admits for Virgo an automorphism of order 11, only without fixed vertices.
- *Paper 14* [9] claims that Antlia has no graph of two orbits over an abelian group of order 33; our survey [6, Table 6] paraphrases this as well. Our results do not touch this class.
- *Post 94* [17] estimates the number of configurations of the first level of division for Ursa Minor at about $4 \cdot 10^{60}$ and concludes that a search without an imposed symmetry is out of reach. This estimate is the reason why the paper looks for structure and for exclusions of classes rather than enumerating graphs.
- *Post 16* [10] is a catalogue of open pairs grouped by the pair of eigenvalues; all twelve pairs are in it, and it makes no claims about them.
- *A comment on Post 12* [18]: on the line $(12a, 3a + 1, 2a - 1, 2, a)$ the absolute bound gives $a \le 10$ and is attained at $a = 10$, $v = 120$; the author calls this parameter set the tight end of the line. The parameter set $(120, 31, 19, 2, 10)$ is the complement of the member $T_5(16) = (120, 88, 76, 66, 60)$ of our family. The comment does not formulate the family, the recipe or exclusions.

We found no other results on tight DSRGs or on the structure of the case of equality in the absolute bound on the platform as of 6 November 2026. There are no such results in the abstracts of papers on DSRGs on arXiv since June 2026 either. The closest to our topic is the enumeration of vertex-transitive DSRGs by Brouwer and Gyürki [22], but it reaches only $v \le 39$; in the table [2] of 6 November all twelve pairs are open.

**Conditions of the table.** Besides Duval's basic conditions, we check the census of tight pairs (Theorem 1(c)) against the conditions of the table [2]. Three of them matter here; $r > s$ are the eigenvalues other than $k$, and $m$ and $m'$ are their multiplicities, as for the side $\theta = r$. Condition N6: if $\lambda = 0$ and $\mu = k - t$, then $3\mu$ divides $v$. Condition N10: if $\lambda = 0$, then $k \le m$, and if moreover $r \ne 0$, also $k \le m'$; if $\lambda = 1$, the same with the thresholds $3m$ and $3m'$. Condition N11: if $k > m$, then $\lambda \ge -s$, and if $k > m'$, then $\lambda \ge r$. Conditions for graphs with an eigenvalue of small multiplicity were derived by Hobart and Williford [14]; we give N10 and N11 as stated in the table [2].

## 3. Components and the absolute bound

**Lemma 5.** For every side $\theta$ of every DSRG with integral $\theta \ne \theta'$

$$
c_1 = \rho_0 = e_0^2 + k e_1^2 + (v - 1 - k) e_2^2 > 0, \qquad
c_\theta = \frac{v(\theta + \theta'^2) - 2\delta(k - \theta')}{v\delta^2}, \qquad
c_{\theta'} = \frac{\theta'(\theta' + 1)}{\delta^2}.
$$

Therefore a side with $v = m(m+1)/2$ is tight if and only if $c_\theta \ne 0$ and $\theta' \notin \{0, -1\}$.

*Proof.* The matrix $E \circ E$ acts on $\mathbf 1$ by the row sum, $\sum_l E_{jl}^2 = \rho_0$, and $\rho_0 \ge e_0^2 > 0$. On an eigenvector of $A$ with eigenvalue $x \in \{\theta, \theta'\}$ orthogonal to $\mathbf 1$, the matrix $J$ vanishes, and the component equals $e_0^2 - e_2^2 + x(e_1^2 - e_2^2)$. From $\delta e_0 = -\theta' - c_0$ (this is $m/v$, by the equality $k + m\theta + m'\theta' = 0$), $\delta e_1 = 1 - c_0$ and $\delta e_2 = -c_0$ one gets $(\theta'^2 + 2\theta' c_0 + x(1 - 2c_0))/\delta^2$. For $x = \theta'$ the terms with $c_0$ cancel, and for $x = \theta$ what remains is $(\theta'^2 + \theta - 2c_0\delta)/\delta^2$. ∎

In the notation of [4], $c_\theta = q^\theta_{\theta\theta}/v$ [4, Section 2], and $c_{\theta'}$ and $c_1$ are the other two coefficients of $E_\theta \circ E_\theta$ divided by $v$; our $\theta'$ is Jørgensen's second nontrivial eigenvalue. Jørgensen notes [4] that for $\theta' \in \{0, -1\}$ the coefficient at $E_{\theta'}$ is zero and the bound fails; Lemma 5 shows this explicitly.

**Proposition 6 (Jørgensen [4]; Godsil, Hobart and Martin [5]).** Let $E = XY^{\mathsf T}$ with matrices $X, Y$ of size $v \times m$ and $Y^{\mathsf T}X = I$. The vertex $j$ gets the points $x_j, y_j \in \mathbb R^m$, the rows of $X$ and $Y$, so that $E_{ij} = \langle x_i, y_j\rangle$. Let $\mathrm{Sym}^2$ be the space of symmetric $m \times m$ matrices, of dimension $m(m+1)/2$, and let $\Phi_x, \Phi_y\colon \mathrm{Sym}^2 \to \mathbb R^v$ be the maps $\Phi_x(Q) = (x_j^{\mathsf T} Q x_j)_j$ and $\Phi_y(Q) = (y_j^{\mathsf T} Q y_j)_j$. Then $E \circ E = \Phi_x \Phi_y^{\mathsf T}$ and $\operatorname{rank}(E \circ E) \le m(m+1)/2$. If all three components of the side are nonzero, then $v \le m(m+1)/2$, and on a tight side $\Phi_x$ and $\Phi_y$ are linear isomorphisms: a nonzero quadratic form does not vanish at all points $x_j$, nor at all points $y_j$.

*Proof.* With the Frobenius inner product on $\mathrm{Sym}^2$, the map $\Phi_x^{\mathsf T}$ sends the basis vector $\mathbf e_i$ to $x_ix_i^{\mathsf T}$, and $\Phi_y^{\mathsf T}$ sends it to $y_iy_i^{\mathsf T}$, and $\langle x_ix_i^{\mathsf T}, y_jy_j^{\mathsf T}\rangle = \langle x_i, y_j\rangle^2$. Hence the equality and the bound on the rank. The matrices $J/v$, $E_\theta$, $E_{\theta'}$ are mutually complementary idempotents with sum $I$, and $E \circ E = c_1 J/v + c_\theta E_\theta + c_{\theta'} E_{\theta'}$; with nonzero components it is invertible, and $v = \operatorname{rank}(E\circ E) \le m(m+1)/2$. At equality, $\Phi_x^{\mathsf T}$ and $\Phi_y^{\mathsf T}$ are surjections between spaces of the same dimension, that is, bijections. ∎

**Equality without tightness is not enough.** In the table of [4], the parameter sets $(21, 6, 2, 1, 2)$ with $\theta = -1$ and $(21, 8, 4, 3, 3)$ with $\theta = 1$ have $m = 6$ and $v = 21 = m(m+1)/2$, but their second eigenvalues are $0$ and $-1$ respectively, the component $c_{\theta'}$ is zero, and both sets are realized by graphs [4]. Closer to our problem is the parameter set $(10, 4, 2, 1, 2)$ with the side $\theta = -1$, $m = 4$: it also has $\theta' = 0$. For the three graphs of our catalogue with this parameter set, $\Phi_x$ is an isomorphism, while $\Phi_y$ has rank 5 out of 10. These graphs are the main witness of the limit of the result (Section 9).

## 4. The family T_j(n)

**Proposition 7.** Let $j \ge 1$ and $n$ be integers, $\delta = n - j - 1 \ne 0$.

1. The parameter set $T_j(n)$ satisfies the identity $k^2 = t + \lambda k + \mu(v - 1 - k)$; its eigenvalues are $r = n - j - 3$ and $s = -2$ with multiplicities $m = n - 1$ and $m' = n(n - 3)/2$, and $v = m(m + 1)/2$.
2. For the side $r$: $c_0 = 2(j + 1)/n$, $e_0 = 2/n$, $e_1 = (n - 2j - 2)/(n\delta)$, $e_2 = -2(j + 1)/(n\delta)$, and
$$
c_r = \frac{n^2 - (5j + 3)n + 4(j + 1)^2}{n \delta^2}, \qquad c_s = \frac{2}{\delta^2}, \qquad c_1 = \rho_0 > 0.
$$
Up to the factor $(n - 1)/2$, the numerator of $c_r$ is the expression $v(r + s^2) - 2(r - s)(k - s)$ of condition N7 of the table [2].
3. The side $r$ is tight if and only if $n^2 - (5j + 3)n + 4(j + 1)^2 \ne 0$. For $j \ge 3$ this holds for all integers $n$; for $j = 2$ the numerator vanishes only at $n = 4$ and $n = 9$, and for $j = 1$ only at $n = 4$.
4. For $j \ge 2$, $k - t = (j - 1)(n - 2j - 3)$, $t - \lambda = n - j - 1$, $t - \mu = 2(n - j - 3)$, so $0 \le \lambda < t < k$ and $1 \le \mu \le t$ hold exactly when $n \ge 2j + 4$. For $j = 1$, $t = k$, and $T_1(n)$ is the parameter set of the triangular graph $T(n)$.
5. Let a DSRG parameter set have the eigenvalue $s = -2$, and let its other eigenvalue $r$ have multiplicity $n - 1$, where $v = n(n - 1)/2$. Then the parameter set is $T_j(n)$ with $j = n - 3 - r$.
6. The complement has the same idempotents: $E_\theta(A) = E_{-1-\theta}(J - I - A)$. Therefore the side $-1 - r$ of the complement of $T_j(n)$ is tight together with the side $r$ of the set itself.

*Proof.* 1. From $\lambda - \mu = n - j - 5$ and $t - \mu = 2(n - j - 3)$ it follows that $x^2 - (\lambda - \mu)x - (t - \mu) = (x - r)(x + 2)$. The DSRG identity is equivalent to $(k - r)(k - s) = \mu v$, and here $k - r = jn$, $k - s = (j + 1)(n - 1)$, and the product equals $2j(j + 1) \cdot n(n - 1)/2$. From $k + mr - 2(v - 1 - m) = 0$ it follows that $m(r + 2) = 2(v - 1) - k = (n - 1)\delta$, and since $\delta = r + 2 \ne 0$, the multiplicity is $m = n - 1$.

2. This is Lemma 5 with $\theta = r$, $\theta' = -2$ and $c_0 = (k + 2)/v = 2(j + 1)/n$; after the substitution the numerator of $c_r$ simplifies to the one stated, and $v(r + 4) - 2\delta(k + 2) = \frac{n - 1}{2}\bigl(n^2 - (5j + 3)n + 4(j + 1)^2\bigr)$.

3. By item 1, $v = m(m+1)/2$, while $c_1 > 0$ and $c_s \ne 0$ always. The discriminant of the numerator in $n$ equals $(5j + 3)^2 - 16(j + 1)^2 = (9j + 7)(j - 1)$. For $j = 1$ it is zero and the root is $n = 4$; for $j = 2$ it equals 25 and the roots are $4$ and $9$. For $j \ge 3$, $(3j - 1)^2 < (9j + 7)(j - 1) < (3j)^2$, so the discriminant is not a square and there are no integral roots.

4. The differences are obtained by substitution, and $\lambda, \mu > 0$ for $j \ge 1$, $n \ge 3$. For $j \ge 2$ the condition $t < k$ is equivalent to $n \ge 2j + 4$, and it implies $t > \lambda$ and $t \ge \mu$.

5. The trace of $A$ is zero: $k = -mr + 2m' = (j + 1)n - (j + 3)$ with $j = n - 3 - r$. Further, $\mu = (k - r)(k + 2)/v = 2j(j + 1)$, $t = \mu + 2r$ and $\lambda = \mu + r - 2$, and this is $T_j(n)$. The number $j$ is an integer because $r = \lambda - \mu + 2$ is an integer, and $j \ge 1$: $\mu \ge 1$ excludes $j \in \{0, -1\}$, and $k > 0$ excludes $j \le -2$.

6. If $Ax = \theta x$ and $x \perp \mathbf 1$, then $(J - I - A)x = (-1 - \theta)x$; the eigenspace decompositions of $A$ and $J - I - A$ coincide, and with them the idempotents, $E\circ E$ and its components. ∎

**Proposition 8.** The pairs with $v \le 300$ that have a tight side and whose set and complement satisfy the basic necessary conditions [1] — the identity for $k^2$, the inequalities $1 \le \mu \le t$ and $0 \le \lambda < t < k < v$, Duval's inequality and integral nonnegative multiplicities — are 72 pairs, and each of them is a member of the family $T_j(n)$ with $j \ge 2$, as the set or as the complement. 70 of them satisfy all conditions of the table [2]. The other two — $(78, 19, 13, 0, 6)$, the complement of $T_4(13)$, and $(190, 39, 21, 0, 10)$, the complement of $T_7(20)$ — violate conditions of the table from Section 2: the first violates N6, N10 and N11, the second N10 and N11.

*Proof.* An enumeration by spectrum (Section 11, Check 2). For each $m$ one takes $v = m(m+1)/2$, an integer $\theta$ of multiplicity $m$ and an integer $\theta'$ of multiplicity $v - 1 - m$; the parameter set is recovered from the spectrum by the formulas of item 5 of Proposition 7, and $0 < k < v - 1$ leaves a finite enumeration. What remains are the parameter sets for which the basic conditions hold for the set and the complement and the side $\theta$ is tight. Each remaining set or its complement is recognized as $T_j(n)$. The enumeration loses no nonintegral eigenvalues: in that case, by [1], $m = m' = (v - 1)/2$, and the equality $v = m(m+1)/2$ gives $v^2 - 8v - 1 = 0$, which has no integral roots. ∎

The census goes only up to $v \le 300$. We have no general argument that a tight side of a DSRG occurs only for members of the family: item 5 of Proposition 7 requires $s = -2$, and that the second eigenvalue of a tight side equals $-2$ for the set or $1$ for the complement is established only by the enumeration.

*Proof of Theorem 1.* Item (a) is items 1, 3 and 4 of Proposition 7: in the range $n \ge 2j + 4$ with $j = 2$ the numerator of $c_r$ vanishes only at $n = 9$. Item (b) is item 5, item (c) is Proposition 8. Item (d) is the substitution of $j$ and $n$ from Table 1 together with item 6: for eight pairs the member of the family is the complement of the set from the table [2]. ∎

A tight member of the family is not necessarily a feasible parameter set: for $T_2(8) = (28, 19, 18, 13, 12)$ both the set and the complement violate Duval's inequality [1]. The feasible members with $v \le 300$ are listed by Theorem 1(c).

## 5. Quadratic forms on a tight side

Let $E = XY^{\mathsf T}$ with $Y^{\mathsf T}X = I$, as in Proposition 6. The columns of $X$ form a basis of $R$, and the columns of $Y$ a basis of $L$; another choice of bases changes all points by one invertible linear transformation, and the statements below do not depend on it.

**Lemma 9.** Let the side $\theta$ be tight and $M = (E \circ E)^{-1} = a_0 I + a_1 A + a_2 J$.

1. For every function $\nu$ on the vertices there is exactly one $Q \in \mathrm{Sym}^2$ with $x_j^{\mathsf T} Q x_j = \nu(j)$ for all $j$, namely $Q = \sum_j \nu(j) Q_j$, where
$$
Q_j = a_0\, y_j y_j^{\mathsf T} + a_1 \sum_{l \in \Gamma^-(j)} y_l y_l^{\mathsf T} + a_2\, Y^{\mathsf T} Y.
$$
2. The form $Y^{\mathsf T}Y$ takes one value $\rho_0$ at all points $x_j$. Therefore a form that is constant at all points $x_j$ is a multiple of $Y^{\mathsf T}Y$; likewise, a form that is constant at all points $y_j$ is a multiple of $X^{\mathsf T}X$.

*Proof.* 1. Uniqueness is Proposition 6. The matrix $M = c_1^{-1}J/v + c_\theta^{-1}E_\theta + c_{\theta'}^{-1}E_{\theta'}$ lies in the span of $I$, $A$, $J$, and $M_{lj} = a_0[l = j] + a_1 A_{lj} + a_2$, where $A_{lj} = 1$ exactly when $l \in \Gamma^-(j)$. Therefore $\langle x_ix_i^{\mathsf T}, Q_j\rangle = \sum_l M_{lj}\langle x_i, y_l\rangle^2 = ((E\circ E)M)_{ij} = [i = j]$, and $\Phi_x\bigl(\sum_j \nu(j)Q_j\bigr) = \nu$.

2. $x_j^{\mathsf T}Y^{\mathsf T}Yx_j = \sum_l \langle x_j, y_l\rangle^2 = \sum_l E_{jl}^2 = \rho_0$: the row $j$ has one entry $e_0$, $k$ entries $e_1$ and $v - 1 - k$ entries $e_2$. If a form $Q$ is constant at the points and equals $c$, then $Q - (c/\rho_0)Y^{\mathsf T}Y$ vanishes at all points and is zero by Proposition 6. For the points $y_j$ the count is the same over a column of $E$, which also has $k$ entries $e_1$. ∎

Item 1 says that on a tight side functions on the vertices and quadratic forms at the points are the same thing. Item 2 singles out one constant form among them. Together they turn the question "is a local count of a vertex constant" into the question "is its form scalar", and this is the recipe of the next section.

## 6. The second-quadric recipe and the four branches

From now on the basis is fixed: the columns of $Y$ form an orthonormal basis of $L$, $Y^{\mathsf T}Y = I$, and $X = EY$. Then $Y^{\mathsf T}X = I$ and $E = XY^{\mathsf T}$, and the constant form of Lemma 9 is the identity matrix. Denote by $U = A \circ A^{\mathsf T}$ the matrix of reciprocal edges, by $W = A - U$ the matrix of one-way arcs, and $D = A - A^{\mathsf T} = W - W^{\mathsf T}$. For a matrix $Z$ of order $v$ put

$$
d_Z(j) = (EZE^{\mathsf T})_{jj}, \qquad Q_Z = \tfrac12\bigl(Y^{\mathsf T}ZY + Y^{\mathsf T}Z^{\mathsf T}Y\bigr).
$$

The numbers $u(j)$, $S_2(j)$, $\tau(j)$ and $\psi$ are those of Theorem 2.

**Theorem 10.** Let $t < k$, and let $\theta$ be a side of the parameter set.

1. For every $Z$, $d_Z(j) = x_j^{\mathsf T}Q_Zx_j$. On a tight side, $d_Z$ is constant if and only if $Q_Z = (d_Z/\rho_0)I$.
2. $d_U(j) = t\bigl(ve_2^2 + 2e_2(e_0 - e_2) + 2ke_2(e_1 - e_2) + 2(e_0 - e_2)(e_1 - e_2)\bigr) + 2(e_1 - e_2)^2u(j)$; the matrix $Y^{\mathsf T}WY$ is symmetric, and $Y^{\mathsf T}UY = \theta I - Y^{\mathsf T}WY$. Therefore on a tight side $u$ is constant if and only if $Y^{\mathsf T}WY = \omega I$ for some $\omega$.
3. The difference $d_{A^{\mathsf T}A}(j) - (e_1 - e_2)^2\psi(j)$ depends only on the parameters, and
$$
X^{\mathsf T}X = \bigl((e_0 - e_2)^2 + 2\theta(e_0 - e_2)(e_1 - e_2)\bigr)I + (e_1 - e_2)^2\,Y^{\mathsf T}A^{\mathsf T}AY.
$$
Therefore on a tight side $\psi$ is constant if and only if $X^{\mathsf T}X$ is scalar, that is, when all $m$ nonzero singular values of $E$ are equal.

*Proof.* 1. $EZE^{\mathsf T} = X(Y^{\mathsf T}ZY)X^{\mathsf T}$, so $d_Z(j) = x_j^{\mathsf T}(Y^{\mathsf T}ZY)x_j = x_j^{\mathsf T}Q_Zx_j$. If $Q_Z = cI$, then $d_Z = c\rho_0$ by Lemma 9; conversely, a constant $d_Z$ is a value of the form $Q_Z$ that is constant at all points, and by Lemma 9 $Q_Z = (d_Z/\rho_0)I$.

2. The row of $E$ equals $E_{j\cdot} = e_2\mathbf 1^{\mathsf T} + (e_0 - e_2)\mathbf e_j^{\mathsf T} + (e_1 - e_2)A_{j\cdot}$. In $d_U(j) = E_{j\cdot}UE_{j\cdot}^{\mathsf T}$ all terms are counts given by the parameters ($\mathbf 1^{\mathsf T}U\mathbf 1 = vt$, $U\mathbf 1 = t\mathbf 1$, $U_{jj} = 0$, $\mathbf e_j^{\mathsf T}UA_{j\cdot}^{\mathsf T} = t$), except $A_{j\cdot}UA_{j\cdot}^{\mathsf T} = \sum_{a, b \in \Gamma^+(j)} U_{ab} = 2u(j)$. The rows of $Y^{\mathsf T}$ are left eigenvectors, so $Y^{\mathsf T}AY = Y^{\mathsf T}A^{\mathsf T}Y = \theta I$, and from $A = U + W$ and $A^{\mathsf T} = U + W^{\mathsf T}$ it follows that $Y^{\mathsf T}WY = \theta I - Y^{\mathsf T}UY = Y^{\mathsf T}W^{\mathsf T}Y$. It remains to apply item 1 with $Z = U$.

3. $(AE^{\mathsf T})_{ij} = e_2k + (e_0 - e_2)A_{ij} + (e_1 - e_2)(AA^{\mathsf T})_{ij}$, and $d_{A^{\mathsf T}A}(j) = \sum_i (AE^{\mathsf T})_{ij}^2$. Expanding the square with $\sum_i A_{ij} = k$, $\sum_i (AA^{\mathsf T})_{ij} = k^2$ and $\sum_i A_{ij}(AA^{\mathsf T})_{ij} = \tau(j)$ gives a number depending only on the parameters plus $(e_1 - e_2)^2S_2(j) + 2(e_0 - e_2)(e_1 - e_2)\tau(j)$, and $e_0 - e_2 = -\theta'/\delta$ and $e_1 - e_2 = 1/\delta$ turn the second term into $(e_1 - e_2)^2\psi(j)$. Further, $X^{\mathsf T}X = Y^{\mathsf T}E^{\mathsf T}EY$ with $E = (e_0 - e_2)I + (e_1 - e_2)A + e_2J$; the terms with $J$ vanish because $J Y = 0$, and the formula follows. Hence $Q_{A^{\mathsf T}A} = Y^{\mathsf T}A^{\mathsf T}AY$ is scalar exactly when $X^{\mathsf T}X$ is scalar. The nonzero eigenvalues of $E^{\mathsf T}E = Y(X^{\mathsf T}X)Y^{\mathsf T}$ are the eigenvalues of $X^{\mathsf T}X$, that is, the squares of the nonzero singular values of $E$. ∎

Theorem 10 is called a recipe because it works with any matrix $Z$: every local count of a vertex that can be written as the diagonal of $EZE^{\mathsf T}$ is constant exactly when the compression of $Z$ to $L$ is scalar. For an arbitrary DSRG neither $u$ nor $\psi$ is determined by the parameters: among the 1940 sides of graphs of our catalogue with $t < k$, the function $\psi$ is nonconstant on 1252.

The mirror numbers for in-neighbours: $u^-(j)$ is the number of reciprocal edges inside $\Gamma^-(j)$; $(A^{\mathsf T}A)_{ij} = |\Gamma^-(i) \cap \Gamma^-(j)|$, $S_2^-(j) = \sum_i (A^{\mathsf T}A)_{ij}^2$, $\tau^-(j) = \sum_{i \in \Gamma^+(j)} (A^{\mathsf T}A)_{ij}$ and $\psi^- = S_2^- - 2\theta'\tau^-$. For a matrix $Z$: $d'_Z(j) = (E^{\mathsf T}ZE)_{jj}$ and $Q'_Z = \frac12(X^{\mathsf T}ZX + X^{\mathsf T}Z^{\mathsf T}X)$.

**Proposition 11.** Let the side $\theta$ be tight and $t < k$.

1. For every $Z$, $d'_Z(j) = y_j^{\mathsf T}Q'_Zy_j$, and $d'_Z$ is constant if and only if $Q'_Z = (d'_Z/\rho_0)X^{\mathsf T}X$.
2. $u^-$ is constant if and only if $X^{\mathsf T}WX = \omega' X^{\mathsf T}X$ for some $\omega'$.
3. $\psi^-$ is constant if and only if $X^{\mathsf T}X$ is scalar, that is, if and only if $\psi$ is constant.
4. $(EA^{\mathsf T}E)_{jj} = \theta'e_0 + \delta\, x_j^{\mathsf T}(X^{\mathsf T}X)y_j$, and the same diagonal differs from $(e_1 - e_2)^2\tau(j)$ by a number depending only on the parameters. Moreover, $AA^{\mathsf T} - A^{\mathsf T}A = \delta^2(EE^{\mathsf T} - E^{\mathsf T}E)$.

*Proof.* Items 1–3 mirror Theorem 10: $E^{\mathsf T}ZE = Y(X^{\mathsf T}ZX)Y^{\mathsf T}$, a column of $E$ decomposes in the same way as a row, and the uniqueness of a form given its values at the points $y_j$ and the constant form $X^{\mathsf T}X$ are given by Proposition 6 and Lemma 9. In item 3, $X^{\mathsf T}EE^{\mathsf T}X = (X^{\mathsf T}X)^2$, and, as in Theorem 10, the same equals $\bigl((e_0 - e_2)^2 + 2\theta(e_0 - e_2)(e_1 - e_2)\bigr)X^{\mathsf T}X + (e_1 - e_2)^2X^{\mathsf T}AA^{\mathsf T}X$; therefore $\psi^-$ is constant exactly when $(X^{\mathsf T}X)^2$ is a multiple of the invertible $X^{\mathsf T}X$, that is, when $X^{\mathsf T}X$ is scalar. In item 4, the spectral decomposition $A = \theta'I + c_0J + \delta E$ and $JE = EJ = 0$ give $EA^{\mathsf T}E = \theta'E + \delta EE^{\mathsf T}E$ and $EE^{\mathsf T}E = X(X^{\mathsf T}X)Y^{\mathsf T}$; in the second expression, of the nine terms of the product of a row, $A^{\mathsf T}$ and a column, only $(e_1 - e_2)^2A_{j\cdot}A^{\mathsf T}A_{\cdot j} = (e_1 - e_2)^2\tau(j)$ is nonconstant. ∎

*Proof of Theorem 2.* Item (a) is Proposition 6 and Lemma 9, item (b) is items 2 and 3 of Theorem 10, item (c) is items 2 and 3 of Proposition 11. ∎

**Table 2.** The two branches by $\psi$ on a tight side with $t < k$. The number $\varsigma$ is the common eigenvalue of $X^{\mathsf T}X$ on the branch, $\bar\varsigma = \operatorname{tr}(X^{\mathsf T}X)/m$.

| Branch | What follows | Free |
|---|---|---|
| $\psi$ constant | $X^{\mathsf T}X = \varsigma I$, $D^3 = -\sigma^2D$ (Proposition 12); the counts $\tau$, $\tau^-$, $S_2$, $S_2^-$ are given by the parameters (Proposition 14); the components of the graph of one-way arcs obey Lemma 13 and Propositions 15, 17 and 19 | $u$, $u^-$ |
| $\psi$ nonconstant | $\psi^-$ is nonconstant, $X^{\mathsf T}X$ is not scalar; $\tau(j) = \lambda k + \delta^3\bigl(x_j^{\mathsf T}(X^{\mathsf T}X)y_j - \bar\varsigma e_0\bigr)$ (Proposition 11) | $u$, $u^-$ |

We have not established a link between the dichotomies by $u$ and by $u^-$: the substitution $X = EY$ brings in $AY$, about which the parameters say nothing. Therefore the four branches of Theorem 2 are the branches by $u$ and $\psi$, and $u^-$ gives one more dichotomy inside each of them. No branch by itself closes a pair. From here on the paper gives the structure only of the branch "$\psi$ constant" (Section 7) and group conditions (Section 8); in the branch "$\psi$ nonconstant" we have no conditions other than Theorem 10 and Proposition 11.

## 7. The branch "ψ constant"

In this section $t < k$ and all nonzero singular values of $E$ are equal; on a tight side this is the branch "$\psi$ constant" (Theorem 10). Proposition 12, Lemma 13 and Propositions 14, 15 and 17 do not require tightness: for the twelve pairs the conditions are obtained by substituting the numbers of the family. The third nonzero component enters them only through the number $\beta$ of Proposition 15, and the isomorphism on the $y$ side only in item 2 of Proposition 19. Notation: $\kappa = k - t$ is the number of one-way out-neighbours of a vertex, $\sigma^2 = v\kappa/m$, $h^2 = \delta^2 + \sigma^2$, $V = R + L$, and $\Pi_V$, $\Pi_R$, $\Pi_L$ are the orthogonal projectors onto $V$, $R$, $L$. The graph $N$ of one-way arcs is the undirected graph on the vertices in which $x$ and $y$ are adjacent if $D_{xy} \ne 0$; every vertex has exactly $2\kappa$ neighbours in $N$.

### 7.1. The matrix D and the components of N

**Proposition 12.** Let $t < k$. All nonzero singular values of $E$ are equal if and only if $\operatorname{rank}D = 2m$ and $D^3 = -\sigma^2D$. In that case $R \cap L = 0$, $DD^{\mathsf T} = \sigma^2\Pi_V$, where $\dim V = 2m$, the number $\sigma^2$ is an integer, $X^{\mathsf T}X = \varsigma I$ with $\varsigma = h^2/\delta^2$, and the matrix $H = A + A^{\mathsf T} + (\mu - \lambda)I$ has on $V$ the eigenvalues $h$ and $-h$ equally often.

*Proof.* Here $D = \delta(E - E^{\mathsf T})$ and $E - E^{\mathsf T} = XY^{\mathsf T} - YX^{\mathsf T}$. For a unit vector $a$, $1 = a^{\mathsf T}Y^{\mathsf T}Xa \le |Ya|\,|Xa| = |Xa|$, so $X^{\mathsf T}X \ge I$, and equality would give $E = E^{\mathsf T}$ and $t = k$. Hence, with equal singular values, $X^{\mathsf T}X = \varsigma I$ with $\varsigma > 1$. If $w = Xa = Yb$, then $a = Y^{\mathsf T}w = b$ and $\varsigma a = X^{\mathsf T}w = b$, whence $a = 0$: $R \cap L = 0$. A direct computation on the bases gives $-(E - E^{\mathsf T})^2 = \varsigma - 1$ on $R$ and on $L$ and $E - E^{\mathsf T} = 0$ on $V^\perp$, that is, $DD^{\mathsf T} = -D^2 = \delta^2(\varsigma - 1)\Pi_V$ and $D^3 = -\delta^2(\varsigma - 1)D$. The trace: $\operatorname{tr}DD^{\mathsf T}$ is the number of nonzero entries of $D$, that is, $2v\kappa$, and it is also $2m\delta^2(\varsigma - 1)$; hence $\delta^2(\varsigma - 1) = v\kappa/m = \sigma^2$, and this is a rational eigenvalue of an integer matrix, that is, an integer. Conversely, $Y^{\mathsf T}X = I$ implies $-D^2Y = \delta^2Y(X^{\mathsf T}X - I)$, and $D^4 = -\sigma^2D^2$ gives $\delta^2(X^{\mathsf T}X - I)^2 = \sigma^2(X^{\mathsf T}X - I)$. An eigenvalue $0$ of the matrix $X^{\mathsf T}X - I$ would give a vector of $R \cap L$ on which $D$ vanishes, and the rank of $D$ would be less than $2m$; hence $X^{\mathsf T}X = (1 + \sigma^2/\delta^2)I$. Finally, from $A^2 = tI + \lambda A + \mu(J - I - A)$ a direct computation gives $H^2 = \delta^2I + DD^{\mathsf T} + 4\mu J$ and $HD = -DH$. On $V \perp \mathbf 1$ this gives $H^2 = h^2$, and anticommutation with $D$ makes the trace of $H$ on $V$ zero. ∎

**Lemma 13.** Let all nonzero singular values of $E$ be equal; let $C$ be a connected component of $N$, $c = |C|$, $D_C = D[C, C]$, and $\mathbf 1_C$ the indicator of $C$.

1. $\ker D = \langle \mathbf 1\rangle \oplus (R' \cap L')$, and $\mathbf 1_C - (c/v)\mathbf 1 \in R' \cap L'$.
2. For every vertex $x$, $|\Gamma^+(x) \cap C| = |\Gamma^-(x) \cap C| = cc_0 + \theta'[x \in C]$. Therefore $cc_0$ is an integer, a vertex of $C$ has exactly $t_C = cc_0 + \theta' - \kappa \ge 0$ neighbours by reciprocal edges inside $C$, and $c \ge 2\kappa + 1 + t_C$.
3. $D_C^3 = -\sigma^2D_C$, and $\operatorname{rank}D_C = 2\kappa c/\sigma^2 = 2cm/v$ is an even integer.
4. For every DSRG, without a hypothesis on the singular values, $(A + A^{\mathsf T})D + D(A + A^{\mathsf T}) = 2(\lambda - \mu)D$. Therefore all arcs between different components $C$, $C'$ are reciprocal, and $D_C\,A[C, C'] = -A[C, C']\,D_{C'}$.

*Proof.* 1. $D = \delta(E - E^{\mathsf T})$, and a vector $w \perp \mathbf 1$ lies in $R'$ exactly when $Ew = 0$, and in $L'$ exactly when $E^{\mathsf T}w = 0$; therefore $\langle\mathbf 1\rangle \oplus (R' \cap L') \subseteq \ker D$. The dimension of $R' \cap L'$ is at least $v - 1 - 2m$, and $\dim\ker D = v - 2m$, so the inclusion is an equality. $D$ is block diagonal with respect to the components of $N$, so $D\mathbf 1_C = 0$, and the vector $\mathbf 1_C - (c/v)\mathbf 1$ is orthogonal to $\mathbf 1$ and lies in $\ker D$, that is, in $R' \cap L'$.

2. By item 1, $A\mathbf 1_C = ckv^{-1}\mathbf 1 + \theta'(\mathbf 1_C - (c/v)\mathbf 1)$, and likewise for $A^{\mathsf T}$. All one-way out-neighbours of a vertex $x \in C$ lie in $C$, and its other out-neighbours in $C$ are joined to it by reciprocal edges. The neighbours of $x$ in $N$ and its reciprocal neighbours in $C$ are distinct and different from $x$.

3. The equality $D^3 = -\sigma^2D$ passes to the blocks. $D_CD_C^{\mathsf T}$ has the eigenvalues $0$ and $\sigma^2$, so the rank equals $\operatorname{tr}(D_CD_C^{\mathsf T})/\sigma^2 = 2\kappa c/\sigma^2$; the rank of a skew-symmetric matrix is even.

4. From the equality for $A^2$ and its transpose, $A^2 - (A^{\mathsf T})^2 = (\lambda - \mu)D$, and the left-hand side equals $\frac12\bigl((A + A^{\mathsf T})D + D(A + A^{\mathsf T})\bigr)$. The block $(C, C')$ with $C \ne C'$, where $D[C, C'] = 0$ and $(A + A^{\mathsf T})[C, C'] = 2A[C, C']$, gives the rest. ∎

For the member $T_2(10) = (45, 25, 22, 15, 12)$, the complement of Ursa Minor, on the tight side $m = 9$, $\theta' = -2$, $\kappa = 3$, $\sigma^2 = 15$ and $c_0 = 3/5$. By Lemma 13 the size of a component is a multiple of 5, $t_C = 3c/5 - 5$ excludes $c = 5$, and $c = 10, 15, \dots, 45$ are admissible with ranks $2c/5$. Divisibility and the rank give nothing more; the sizes 10 and 15 are excluded by Proposition 15.

### 7.2. Local counts

**Proposition 14.** Let $X^{\mathsf T}X = \varsigma I$. Then for every vertex $j$

$$
\tau(j) = \tau^-(j) = \lambda k, \qquad S_2(j) = S_2^-(j) = \operatorname{tr}\bigl((AA^{\mathsf T})^2\bigr)/v,
$$

where $\operatorname{tr}((AA^{\mathsf T})^2) = k^4 + \theta'^4(v - 1) + 2\theta'^2m(2\theta'\delta + \delta^2\varsigma) + m\bigl(\theta'^2\delta^2(2 + 2\varsigma) + 4\theta'\delta^3\varsigma + \delta^4\varsigma^2\bigr)$. Moreover, $AA^{\mathsf T} - A^{\mathsf T}A = h^2(\Pi_R - \Pi_L)$.

*Proof.* If $X^{\mathsf T}X = \varsigma I$, then $x_j^{\mathsf T}(X^{\mathsf T}X)y_j = \varsigma E_{jj} = \varsigma e_0$, and by item 4 of Proposition 11 $\tau$ is constant. The mean of $\tau$ equals $\lambda k$: $\sum_j\tau(j)$ is the number of triples $b \to j$, $b \to a$, $j \to a$, that is, $\sum_{b \to a}(A^2)_{ba} = vk\lambda$. The reversed graph with matrix $A^{\mathsf T}$ is a DSRG with the same parameters and the idempotent $E^{\mathsf T}$, and its $\tau$ is $\tau^-$. By Theorem 10 $\psi$ is constant, and with it $S_2 = \psi + 2\theta'\tau$, so $S_2$ equals its mean; likewise $S_2^-$. The trace: $AA^{\mathsf T} = k^2J/v + \theta'^2(I - J/v) + B_E$ with $B_E = \theta'\delta(E + E^{\mathsf T}) + \delta^2EE^{\mathsf T}$, and when $X^{\mathsf T}X = \varsigma I$, $\operatorname{tr}B_E = m(2\theta'\delta + \delta^2\varsigma)$, while $\operatorname{tr}B_E^2$ is the last term of the formula. Finally, $XX^{\mathsf T} = \varsigma\Pi_R$, $YY^{\mathsf T} = \Pi_L$, and item 4 of Proposition 11 gives $\delta^2\varsigma(\Pi_R - \Pi_L)$, while $\delta^2\varsigma = h^2$. ∎

On the tight side of the twelve pairs these numbers are integers. For example, for a graph of Ursa Minor $(45, 19, 16, 5, 10)$ on the tight side $\tau = \lambda k = 95$ and $S_2 = 3423$, and for the member $T_2(10)$ they are $375$ and $9037$. In an enumeration of the components of $N$ they fix the local counts of a vertex.

### 7.3. Complex points and the size of the parts of N

Let $X^{\mathsf T}X = \varsigma I$. The matrix $X - Y$ is orthogonal to $L$ column by column and $(X - Y)^{\mathsf T}(X - Y) = (\varsigma - 1)I$, so $\delta(X - Y) = \sigma F$ for a matrix $F$ with orthonormal columns lying in $V \cap L^\perp = V \cap R'$. Denote the rows of $F$ by $f_j$. The vertex $j$ gets the *complex point* $\varphi_j = y_j + \mathrm i f_j \in \mathbb C^m$; the Hermitian product is $\langle a, b\rangle = \sum_{l = 1}^m a_l\bar b_l$. Put $\tilde x_j = (\delta y_j + \sigma f_j)/h$ and $\beta = \theta'(\theta' + 1)/\bigl(2c_0(1 - c_0)\bigr)$. For a union $S$ of components of $N$ with $c_S$ vertices, $\mathcal W_S$ is the complex span of the points $\varphi_j$, $j \in S$, $\mathcal P_S$ is the Hermitian orthogonal projector onto $\mathcal W_S$, and $\bar{\mathcal P}_S$ is the complex conjugate matrix.

**Proposition 15.**

1. $A = \theta'I + c_0J + \delta YY^{\mathsf T} + \sigma FY^{\mathsf T}$. The matrix of Hermitian products of the points equals $\Pi_V + \mathrm iD/\sigma$, and $\Pi_V = YY^{\mathsf T} + FF^{\mathsf T} = -D^2/\sigma^2$. Moreover, $\sum_j\varphi_j\varphi_j^* = 2I$, $\sum_j\varphi_j\varphi_j^{\mathsf T} = 0$, and the columns of $Y + \mathrm iF$ form a basis of the eigenspace of $D$ for the eigenvalue $-\mathrm i\sigma$.
2. Points of different components of $N$ are Hermitian orthogonal. For every union $S$ of components, $\dim_{\mathbb C}\mathcal W_S = c_Sm/v$, $\sum_{l \in S}\varphi_l\varphi_l^* = 2\mathcal P_S$, $\sum_{l \in S}\varphi_l\varphi_l^{\mathsf T} = 0$ and $\sum_{l \in S}y_ly_l^{\mathsf T} = \sum_{l \in S}\tilde x_l\tilde x_l^{\mathsf T} = \operatorname{Re}\mathcal P_S$.
3. $\operatorname{tr}\bigl((\operatorname{Re}\mathcal P_S)^2\bigr) = c_S\bigl(\theta'(\theta' + 1) + c_Sc_0(1 - c_0)\bigr)/h^2$. When $S$ is the set of all vertices, this gives $h^2 = v(\theta'(\theta' + 1) + vc_0(1 - c_0))/m$; this equality holds for every side of every DSRG.
4. Let $0 < c_0 < 1$. Every nonempty union of components has $c_S \ge v/2 - \beta$ vertices, and one that does not contain all vertices also has $c_S \le v/2 + \beta$. The lower end is attained exactly when $\bar{\mathcal P}_S\mathcal P_S = 0$. Therefore, for $\theta' \in \{0, -1\}$, the graph $N$ is connected or consists of two components of $v/2$ vertices each, and three or more components are possible only when $v \le 6\beta$.

The excess $\theta'(\theta' + 1)$ in item 3 is $\delta^2c_{\theta'}$, the third component of Lemma 5. Through it the nonzero third component, one of the two conditions of tightness, enters the bound on the size of parts.

*Proof.* 1. The spectral decomposition gives $A = \theta'I + c_0J + \delta E$, and $\delta E = \delta YY^{\mathsf T} + \delta(X - Y)Y^{\mathsf T} = \delta YY^{\mathsf T} + \sigma FY^{\mathsf T}$. Hence $D = \sigma(FY^{\mathsf T} - YF^{\mathsf T})$ and $D^2 = -\sigma^2(YY^{\mathsf T} + FF^{\mathsf T})$. Direct multiplication gives $(Y + \mathrm iF)(Y + \mathrm iF)^* = YY^{\mathsf T} + FF^{\mathsf T} + \mathrm i(FY^{\mathsf T} - YF^{\mathsf T})$, the sums $\sum_j\varphi_j\varphi_j^* = Y^{\mathsf T}Y + F^{\mathsf T}F = 2I$ and $\sum_j\varphi_j\varphi_j^{\mathsf T} = Y^{\mathsf T}Y - F^{\mathsf T}F + \mathrm i(Y^{\mathsf T}F + F^{\mathsf T}Y) = 0$, and $D(Y + \mathrm iF) = -\mathrm i\sigma(Y + \mathrm iF)$. The eigenvalue $-\mathrm i\sigma$ of the skew-symmetric $D$ of rank $2m$ has multiplicity $m$.

2. $D$ is block diagonal with respect to the components, and so are $\Pi_V$ and the matrix of Hermitian products; this is the orthogonality. The matrix $(\Pi_V + \mathrm iD/\sigma)/2$ is the projector onto the eigenspace $\mathcal E_-$ of the eigenvalue $-\mathrm i\sigma$, and it is block diagonal, so $\mathcal E_- = \bigoplus_C \mathcal E_C$, where $\mathcal E_C$ consists of the vectors of $\mathcal E_-$ supported on $C$. The dimension of the block of a component is $\operatorname{rank}D_C/2 = cm/v$ (Lemma 13), and $\mathcal W_C$ has the same dimension. The subspaces $\mathcal W_C$ are pairwise orthogonal and sum to $\mathbb C^m$; the sum $\sum_C\sum_{l \in C}\varphi_l\varphi_l^* = 2I$, together with the fact that each summand maps everything into $\mathcal W_C$ and annihilates $\mathcal W_C^\perp$, gives $\sum_{l \in C}\varphi_l\varphi_l^* = 2\mathcal P_C$; likewise $\sum_{l \in C}\varphi_l\varphi_l^{\mathsf T} = 0$. The real and imaginary parts of these equalities give $\sum_S y_ly_l^{\mathsf T} = \sum_S f_lf_l^{\mathsf T} = \operatorname{Re}\mathcal P_S$ and $\sum_S(y_lf_l^{\mathsf T} + f_ly_l^{\mathsf T}) = 0$, and with them the formula for $\tilde x_l$.

3. By item 1, $A_{il} - \theta'[i = l] - c_0 = h\langle\tilde x_i, y_l\rangle$, so $\sum_{i, l \in S}(A_{il} - \theta'[i = l] - c_0)^2 = h^2\operatorname{tr}((\operatorname{Re}\mathcal P_S)^2)$ by item 2. The left-hand side is a count over the graph: a vertex of $S$ has exactly $c_Sc_0 + \theta'$ out-neighbours in $S$ (Lemma 13), and the sum equals $c_S(\theta'^2 + \theta' + c_Sc_0 - c_Sc_0^2)$. For all vertices $\operatorname{Re}\mathcal P_S = I$, and the formula for $h^2$ follows. For every side of every DSRG the same count gives $\delta^2\|E\|^2 = v(\theta'(\theta' + 1) + vc_0(1 - c_0))$, and from $\|D\|^2 = 2v\kappa$ and $\operatorname{tr}E^2 = m$ it follows that $\delta^2\|E\|^2 = m\delta^2 + v\kappa = mh^2$.

4. $\operatorname{tr}((\operatorname{Re}\mathcal P_S)^2) = \bigl(\ell_S + \|\bar{\mathcal P}_S\mathcal P_S\|^2\bigr)/2$ with $\ell_S = c_Sm/v$, and the inequality $\operatorname{tr}((\operatorname{Re}\mathcal P_S)^2) \ge \ell_S/2$ together with item 3 is equivalent to $c_S \ge v/2 - \beta$. The complement of a proper union is also a nonempty union of components. When $\beta = 0$, every union has exactly $v/2$ vertices, and three components give $3(v/2 - \beta) \le v$. ∎

**Corollary 16.** Let a graph of one of the twelve pairs lie in the branch "$\psi$ constant". Then for Virgo, Perseus, Scorpius and Triangulum the graph $N$ is connected, and for the other eight pairs it is connected or consists of exactly two components of sizes from Table 3.

**Table 3.** The bound on the size of parts for the twelve pairs. For $T_j(n)$ on the tight side $\theta' = -2$, $c_0 = 2(j + 1)/n$ and $\beta = n^2/(2(j + 1)(n - 2j - 2))$; for the complement the graph $N$, $\beta$ and the interval are the same. The column "Sizes" lists the sizes of components admissible by Lemma 13 and lying in the interval $[v/2 - \beta, v/2 + \beta]$.

| Pair | $T_j(n)$ | $\beta$ | Interval | Sizes | Disconnected $N$ |
|---|---|---|---|---|---|
| Ursa Minor | $T_2(10)$ | 25/6 | [18.33; 26.67] | 20, 25 | only 20 + 25 |
| Virgo | $T_2(11)$ | 121/30 | [23.47; 31.53] | — | impossible |
| Antlia | $T_3(12)$ | 9/2 | [28.5; 37.5] | 30, 36 | only 30 + 36 |
| Camelopardalis | $T_2(12)$ | 4 | [29; 37] | 30, 36 | only 30 + 36 |
| Dorado | $T_3(13)$ | 169/40 | [34.78; 43.23] | 39 | only 39 + 39 |
| Horologium | $T_2(13)$ | 169/42 | [34.98; 43.02] | 39 | only 39 + 39 |
| Leo Minor | $T_4(14)$ | 49/10 | [40.6; 50.4] | 42, 49 | only 42 + 49 |
| Monoceros | $T_2(14)$ | 49/12 | [41.42; 49.58] | 42, 49 | only 42 + 49 |
| Orion | $T_3(14)$ | 49/12 | [41.42; 49.58] | 42, 49 | only 42 + 49 |
| Perseus | $T_4(15)$ | 9/2 | [48; 57] | — | impossible |
| Scorpius | $T_2(15)$ | 25/6 | [48.33; 56.67] | — | impossible |
| Triangulum | $T_3(15)$ | 225/56 | [48.48; 56.52] | — | impossible |

*Proof.* By Lemma 13, a size $c$ of a component is admissible if $cc_0$ is an integer, $2\kappa c/\sigma^2$ is an even integer, $t_C \ge 0$ and $c \ge 2\kappa + 1 + t_C$. For each of the twelve pairs $0 < c_0 < 1$ and $6\beta < 30 < v$, so by Proposition 15 there are at most two components, and if there are two, both lie in the interval and their sizes sum to $v$. For example, for Ursa Minor $c$ is a multiple of 5, the interval contains 20 and 25, and $20 + 25 = 45$; for Virgo $c_0 = 6/11$, $c$ is a multiple of 11, and there is no multiple of 11 between 23.47 and 31.53. ∎

### 7.4. Two parts of N

Let $S$ be a union of components of $N$, and let the remaining vertices $S'$ form a nonempty set; $c = |S|$, $c' = v - c$, $\ell = cm/v$ and $\eta = h^2/4$. All arcs between $S$ and $S'$ are reciprocal (Lemma 13), so the block $B = A[S, S']$ also determines $A[S', S] = B^{\mathsf T}$. Put $D_S = D[S, S]$ and $\Pi_S = -D_S^2/\sigma^2$.

**Proposition 17.**

1. $BB^{\mathsf T}$ preserves the decomposition $\mathbb R^S = \langle\mathbf 1_S\rangle \oplus (\ker D_S \cap \mathbf 1_S^\perp) \oplus \operatorname{im}D_S$: on $\mathbf 1_S$ its eigenvalue is $cc'c_0^2$, on the second summand it is zero, and on $\operatorname{im}D_S$, of dimension $2\ell$, its eigenvalues are $\varepsilon_1, \dots, \varepsilon_\ell$, each twice, where the numbers $1 - \varepsilon_i/\eta$ are the eigenvalues of $\mathcal P_S\bar{\mathcal P}_S\mathcal P_S$ on $\mathcal W_S$. Therefore $0 \le \varepsilon_i \le \eta$, and $\Pi_S$ is the orthogonal projector onto $\operatorname{im}D_S$.
2. The polynomial $\mathfrak p_S(x) = \prod_i(x - \varepsilon_i)$ has integer coefficients, and $\sum_i \varepsilon_i = \bigl(\ell h^2 - c(\theta'(\theta' + 1) + cc_0(1 - c_0))\bigr)/2$.
3. For an integer $\hat\eta \ge \eta$, $\sum_{\varepsilon_i \ne \hat\eta}(\hat\eta - \varepsilon_i) \ge \#\{i : \varepsilon_i \ne \hat\eta\}$, and equality holds only when every $\varepsilon_i \in \{\hat\eta - 1, \hat\eta\}$. In particular, if $\eta$ is not an integer and $\hat\eta = \lceil\eta\rceil$, then $\ell\hat\eta - \sum_i \varepsilon_i \ge \ell$, and if $\ell\hat\eta - \sum_i \varepsilon_i = \ell$, then all $\varepsilon_i = \hat\eta - 1$.
4. If all $\varepsilon_i$ equal one number $\varepsilon$, then $BB^{\mathsf T} = \varepsilon\Pi_S + c'c_0^2J$. If moreover $\varepsilon$, $\sigma^2$ and $c'c_0^2$ are integers and $\gamma = \gcd(\varepsilon, \sigma^2)$, then $\Delta = \gamma\Pi_S$ is an integer matrix with $\Delta^2 = \gamma\Delta$, $\Delta\mathbf 1 = 0$ and diagonal $2\gamma\ell/c$. In other words, $\Delta = \Xi^{\mathsf T}\Xi$ for a matrix $\Xi$ of size $2\ell \times c$ with $\Xi\Xi^{\mathsf T} = \gamma I$ and $\Xi\mathbf 1 = 0$; we call its columns $\xi_x$ a *frame*. These are vectors of one norm $2\gamma\ell/c$, the *norm of the frame*, with integer pairwise products, and $\sum_x\xi_x\xi_x^{\mathsf T} = \gamma I$. Moreover, $D_S = \Xi^{\mathsf T}\Omega\,\Xi$, where $\Omega$ is skew-symmetric and $\Omega^2 = -(\sigma^2/\gamma^2)I$.

*Proof.* 1. In the coordinates $Ya + Fb \mapsto a + \mathrm ib$ on $V$, the matrix $A$ acts as $w \mapsto z_1w + z_2\bar w$ with $z_1 = (\theta + \theta' + \mathrm i\sigma)/2$ and $z_2 = (\delta + \mathrm i\sigma)/2$, and $D$ acts as multiplication by $\mathrm i\sigma$; this is the substitution of Proposition 15. The space $\operatorname{im}D_S = V \cap \mathbb R^S$ is $\mathcal W_S$ in these coordinates, and $\mathbb C^m = \mathcal W_S \oplus \mathcal W_{S'}$ orthogonally. For $w \in \mathcal W_S$ the part of $Aw$ in $S'$ equals $z_2\mathcal P_{S'}\bar w$, so $BB^{\mathsf T}w = |z_2|^2(I - \mathcal P_S\bar{\mathcal P}_S)w$ with $|z_2|^2 = \eta$. A Hermitian operator on $\mathcal W_S$ of complex dimension $\ell$ is a real symmetric one on a space of dimension $2\ell$, and each eigenvalue occurs twice. On $\ker D_S \cap \mathbf 1_S^\perp \subseteq R' \cap L'$ (Lemma 13) the matrix $A$ acts as $\theta'$, and $B^{\mathsf T}$ annihilates this vector; $B^{\mathsf T}\mathbf 1_S = cc_0\mathbf 1_{S'}$ and $B\mathbf 1_{S'} = c'c_0\mathbf 1_S$.

2. The characteristic polynomial of the integer matrix $BB^{\mathsf T}$ equals $x^{c - 1 - 2\ell}(x - cc'c_0^2)\mathfrak p_S(x)^2$, and $cc'c_0^2$ is the product of two integer counts of Lemma 13. Therefore $\mathfrak p_S^2 \in \mathbb Z[x]$; the factors irreducible over $\mathbb Q$ enter $\mathfrak p_S^2$ with even exponents, $\mathfrak p_S \in \mathbb Q[x]$, and by Gauss's lemma $\mathfrak p_S \in \mathbb Z[x]$. The sum: $\sum_i \varepsilon_i = \eta(\ell - \operatorname{tr}(\mathcal P_S\bar{\mathcal P}_S))$, and Proposition 15 gives $\operatorname{tr}(\mathcal P_S\bar{\mathcal P}_S) = 2c(\theta'(\theta' + 1) + cc_0(1 - c_0))/h^2 - \ell$.

3. The polynomial $\mathfrak p_S(x)/(x - \hat\eta)^{\ell - \ell'}$, where $\ell'$ is the number of $\varepsilon_i \ne \hat\eta$, is integral and monic, so $\prod_{\varepsilon_i \ne \hat\eta}(\hat\eta - \varepsilon_i)$ is a nonzero integer with positive factors, that is, at least 1. The inequality of arithmetic and geometric means gives $\sum(\hat\eta - \varepsilon_i) \ge \ell'$, and equality requires all factors to equal 1.

4. Both sides of the equality for $BB^{\mathsf T}$ agree on the three summands of item 1. The matrices $\varepsilon\Pi_S = BB^{\mathsf T} - c'c_0^2J$ and $\sigma^2\Pi_S = -D_S^2$ are integer matrices, and $\gamma$ is an integer linear combination of $\varepsilon$ and $\sigma^2$, so $\gamma\Pi_S$ is also an integer matrix. The diagonal of $-D_S^2$ equals $2\kappa$, so the diagonal of $\Pi_S$ is $2\kappa/\sigma^2 = 2\ell/c$. A factorization $\Delta = \Xi^{\mathsf T}\Xi$ of full row rank with $\Delta^2 = \gamma\Delta$ gives $\Xi\Xi^{\mathsf T} = \gamma I$, and $|\Xi\mathbf 1|^2 = \mathbf 1^{\mathsf T}\Delta\mathbf 1 = 0$. Finally, $D_S = \Pi_SD_S\Pi_S = \Xi^{\mathsf T}\Omega\,\Xi$ with $\Omega = \Xi D_S\Xi^{\mathsf T}/\gamma^2$, and $\Omega^2 = \Xi D_S^2\Xi^{\mathsf T}/\gamma^3 = -(\sigma^2/\gamma^2)I$. ∎

**Corollary 18.** In the branch "$\psi$ constant" there is no partition of $N$ into components of 30 and 36 vertices for Camelopardalis $(66, 31, 26, 17, 12) = T_2(12)$, and none into components of 42 and 49 vertices for Monoceros $(91, 37, 30, 19, 12) = T_2(14)$. Together with Corollary 16, the graph $N$ in this branch is connected for both pairs.

*Proof.* *Camelopardalis.* For $T_2(12)$ on the tight side $m = 11$, $\theta = 7$, $\theta' = -2$, $\sigma^2 = 30$, $h^2 = 111$, $c_0 = 1/2$. Let $S$ be a component of 30 vertices: $\ell = 5$, $c' = 36$. By item 2 of Proposition 17, $\sum_i \varepsilon_i = (555 - 285)/2 = 135$. The number $\eta = 111/4$ is not an integer, $\hat\eta = 28$, $\ell\hat\eta - \sum_i \varepsilon_i = 5 = \ell$, and by item 3 all $\varepsilon_i = 27$. Further, $c'c_0^2 = 9$, $\gamma = \gcd(27, 30) = 3$, and the norm is $2\gamma\ell/c = 1$. By item 4 the vectors $\xi_x \in \mathbb R^{10}$ are unit vectors with integer products, that is, any two of them are either equal up to sign or orthogonal. Distinct lines $\pm\xi_x$ are pairwise orthogonal, and $\sum_x\xi_x\xi_x^{\mathsf T} = 3I$ means that there are exactly 10 lines and each carries exactly three vectors. The coefficient of $\Xi\mathbf 1$ along each line is a sum of three numbers $\pm 1$, which is odd, whereas $\Xi\mathbf 1 = 0$.

*Monoceros.* For $T_2(14)$: $m = 13$, $\theta = 9$, $\theta' = -2$, $\sigma^2 = 49$, $h^2 = 170$, $c_0 = 3/7$. Let $S$ be a component of 42 vertices: $\ell = 6$, $c' = 49$. Then $\sum_i \varepsilon_i = (1020 - 516)/2 = 252$, $\eta = 85/2$, $\hat\eta = 43$, $\ell\hat\eta - \sum_i \varepsilon_i = 6 = \ell$, and all $\varepsilon_i = 42$. Further, $c'c_0^2 = 9$, $\gamma = \gcd(42, 49) = 7$, the norm is 2, $\Omega^2 = -I$, so $\Omega$ is orthogonal, and $D_{xy} = \xi_x \cdot \Omega\xi_y$.

The lattice $\Lambda$ spanned by the 42 vectors $\xi_x \in \mathbb R^{12}$ is integral and even, and it is generated by vectors of norm 2. By Witt's theorem [21] such a lattice is an orthogonal sum of root lattices of irreducible systems $\mathsf A_b$, $\mathsf D_b$, $\mathsf E_6$, $\mathsf E_7$, $\mathsf E_8$, and every $\xi_x$ is a root of exactly one summand. Let $\mathcal X_i$ be the vertices with $\xi_x$ in the summand $\Lambda_i$ of rank $b_i$. Restricting the frame gives $\sum_{x \in \mathcal X_i}\xi_x\xi_x^{\mathsf T} = 7I_{\Lambda_i}$; the trace gives $2|\mathcal X_i| = 7b_i$, and $b_i$ is even. For $w$ in the dual lattice of the summand, the number $\sum_{x \in \mathcal X_i}(\xi_x \cdot w)^2 = 7|w|^2$ is an integer. The norms of the classes of the dual lattice modulo 2 are $a(b + 1 - a)/(b + 1)$, $a = 1, \dots, b$, for $\mathsf A_b$, $4/3$ for $\mathsf E_6$ and $3/2$ for $\mathsf E_7$ [21]. Therefore $\mathsf A_b$ needs $b + 1 \mid 7$, that is, $b = 6$, and $\mathsf E_6$ and $\mathsf E_7$ drop out. $\mathsf D_b$ drops out by parity: in the coordinates $\pm\mathbf e_c \pm \mathbf e_d$, an off-diagonal entry of the frame equation equates the multiplicities of the lines $\mathbf e_c + \mathbf e_d$ and $\mathbf e_c - \mathbf e_d$, and a diagonal entry gives, for each $c$, the equality $2\sum_d \operatorname{mult}(\mathbf e_c + \mathbf e_d) = 7$. Rank 12 is made up of $\mathsf A_6$ and $\mathsf E_8$ only as $\mathsf A_6 \oplus \mathsf A_6$, with $|\mathcal X_1| = |\mathcal X_2| = 21$. In the coordinates of $\mathbb R^7$ the frame of $\mathsf A_6$ is $\sum_{c < d}\operatorname{mult}(\mathbf e_c - \mathbf e_d)\,(\mathbf e_c - \mathbf e_d)(\mathbf e_c - \mathbf e_d)^{\mathsf T} = 7(I - J/7)$, and all multiplicities equal 1: each of the 21 root lines of each copy occurs among the $\pm\xi_x$ exactly once.

The vector $\Omega\xi_y$ has norm 2 and integer products with all $\xi_x$, that is, it lies in $\Lambda^* = \mathsf A_6^* \oplus \mathsf A_6^*$. The norms of the classes of $\mathsf A_6^*/\mathsf A_6$ modulo 2 are $0, 6/7, 10/7, 12/7, 12/7, 10/7, 6/7$, and no sum of two nonzero ones among them is divisible by 2. Therefore $\Omega\xi_y \in \Lambda$ is a root, and the isometry $\Omega$ maps roots to roots and irreducible summands to summands. If $\Omega(\Lambda_2) = \Lambda_2$, then also $\Omega(\Lambda_1) = \Lambda_1$, and $D_{xy} = 0$ for $x \in \mathcal X_1$, $y \in \mathcal X_2$: there are no edges of $N$ between two nonempty parts of $S$, contrary to the connectedness of the component. If $\Omega(\Lambda_2) = \Lambda_1$, then $\Omega$ maps the root lines of the second copy onto all root lines of the first, and for $x \in \mathcal X_1$ there is $y \in \mathcal X_2$ with $\Omega\xi_y = \pm\xi_x$, that is, $D_{xy} = \pm 2$, whereas the entries of $D$ are $0$ and $\pm 1$. ∎

**Table 4.** The numbers of Proposition 17 for the smaller part of each partition of Corollary 16. $\hat\eta = \lceil\eta\rceil$; the columns $\varepsilon$, $\gamma$, norm and $\Omega^2$ are filled where item 3 forces a constant $\varepsilon$.

| Pair | $c$ ($\ell$) | $\eta$ | $\sum \varepsilon_i$ | $\hat\eta$ | $\ell\hat\eta - \sum \varepsilon_i$ | $\varepsilon$ | $c'c_0^2$ | $\gamma$ | Norm | $\Omega^2$ | Outcome |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Ursa Minor | 20 (4) | 16 | 60 | 16 | 4 | — | 9 | — | — | — | $\eta$ integral: all $\varepsilon_i = 15$ or some $\varepsilon_i = 16$ |
| Antlia | 30 (5) | 25 | 120 | 25 | 5 | — | 16 | — | — | — | $\eta$ integral: all $\varepsilon_i = 24$ or some $\varepsilon_i = 25$ |
| Camelopardalis | 30 (5) | 111/4 | 135 | 28 | 5 | 27 | 9 | 3 | 1 | $-10/3$ | partition excluded |
| Dorado | 39 (6) | 133/4 | 180 | 34 | 24 | — | 192/13 | — | — | — | $\varepsilon_i$ not forced |
| Horologium | 39 (6) | 139/4 | 189 | 35 | 21 | — | 108/13 | — | — | — | $\varepsilon_i$ not forced |
| Leo Minor | 42 (6) | 36 | 210 | 36 | 6 | — | 25 | — | — | — | $\eta$ integral: all $\varepsilon_i = 35$ or some $\varepsilon_i = 36$ |
| Monoceros | 42 (6) | 85/2 | 252 | 43 | 6 | 42 | 9 | 7 | 2 | $-1$ | partition excluded |
| Orion | 42 (6) | 85/2 | 252 | 43 | 6 | 42 | 16 | 14 | 4 | $-5/14$ | partition not excluded |

Where the argument stops. For Orion item 3 forces $\varepsilon_i = 42$, but $\gamma = \gcd(42, 70) = 14$, the frame consists of vectors of norm 4, and such a lattice need not be a root lattice. For Ursa Minor, Antlia and Leo Minor $\eta$ is an integer, and item 3 leaves two cases: all $\varepsilon_i = \eta - 1$, or some $\varepsilon_i = \eta$; in the second case the other values are not forced, and for Ursa Minor item 3 also lets through the values $12, 16, 16, 16$. In the first case $\gamma$ equals 15, 12 and 7, and the norm is 6, 4 and 2; for Leo Minor the norm 2 again gives $\mathsf A_6 \oplus \mathsf A_6$, but $\Omega^2 = -9/7$, and the vector $\Omega\xi_y$ has norm $18/7$ and is not a root. For Dorado and Horologium the slack $\ell\hat\eta - \sum \varepsilon_i$ equals 24 and 21 with $\ell = 6$, and the values are not forced. Proposition 17 does not touch a connected $N$: with one component there is no block $B$.

### 7.5. The bisector, the tightness equation and the frame of the whole V

Let $H = A + A^{\mathsf T} + (\mu - \lambda)I$, as in Proposition 12, $\cos\alpha = \delta/h$, $\sin\alpha = \sigma/h$, and let $\mathfrak A$ be the linear span of the matrices $I$, $J$, $A$, $A^{\mathsf T}$, $AA^{\mathsf T}$, $A^{\mathsf T}A$.

**Proposition 19.**

1. The matrix $K = H\Pi_V/h$ is symmetric, $K^2 = \Pi_V$, $KD = -DK$, and its eigenvalue $+1$ has multiplicity $m$. Its eigenspace $V_+$ is a real form of $V$: $V = V_+ \oplus (D/\sigma)V_+$ orthogonally. The projectors onto $L$ and $R$ are polynomials in $A$ and $A^{\mathsf T}$ with rational coefficients:
$$
\Pi_L = \tfrac12\bigl(\Pi_V + (\delta I - D)K/h\bigr), \qquad \Pi_R = \tfrac12\bigl(\Pi_V + (\delta I + D)K/h\bigr), \qquad K\Pi_LK = \Pi_R.
$$
In the coordinates $V \cong \mathbb C^m$ the subspace $L$ is $\mathbb R^m$, $R$ is $e^{\mathrm i\alpha}\mathbb R^m$, and $V_+ = e^{\mathrm i\alpha/2}\mathbb R^m$: the reflection $K$ swaps $L$ and $R$. For $\delta < 0$ the angle $\alpha$ is obtuse; the formulas do not depend on the sign of $\delta$.
2. On a tight side of any DSRG, without a hypothesis on the singular values, with $M = (E \circ E)^{-1}$
$$
(\Pi_L \circ \Pi_L)\,M\,\bigl((EE^{\mathsf T}) \circ (EE^{\mathsf T})\bigr)M^{\mathsf T} = I,
$$
and on the branch this becomes an equation in the single matrix $\Pi_L$, with the matrices $M$ and $K$ known from the graph:
$$
(\Pi_L \circ \Pi_L)\,M\,\bigl((K\Pi_LK) \circ (K\Pi_LK)\bigr)M^{\mathsf T} = (\delta^4/h^4)\,I.
$$
3. Let $2m < v - 1$. A matrix $Z \in \mathfrak A$ that acts on $V$ as multiplication by a real number and annihilates $R' \cap L'$ is a linear combination of $DD^{\mathsf T} + 2\mu J$ and $J$. Let $c_D$ be the greatest common divisor of the entries of $DD^{\mathsf T}$. Then $\Delta_V = DD^{\mathsf T}/c_D$ is an integer matrix with $\Delta_V^2 = (\sigma^2/c_D)\Delta_V$, $\Delta_V\mathbf 1 = 0$, diagonal $2\kappa/c_D$ and rank $2m$, and $c_D$ divides $\gcd(2\kappa, \sigma^2)$. As in Proposition 17, $\Delta_V = \Xi_V^{\mathsf T}\Xi_V$ with $\Xi_V\Xi_V^{\mathsf T} = (\sigma^2/c_D)I$, $\Xi_V\mathbf 1 = 0$, $D = \Xi_V^{\mathsf T}\Omega_V\Xi_V$ and $\Omega_V^2 = -(c_D^2/\sigma^2)I$.

*Proof.* 1. As in the proof of Proposition 17, on $V$ the matrix $A$ acts as $w \mapsto z_1w + z_2\bar w$, $A^{\mathsf T}$ as $w \mapsto \bar z_1w + z_2\bar w$, and $\theta + \theta' = \lambda - \mu$ gives for $H$ the action $w \mapsto 2z_2\bar w = he^{\mathrm i\alpha}\bar w$. By Lemma 13 $HD = -DH$, so $H$ preserves $V$ and $\ker D$, $K$ is symmetric and acts on $V$ as the antilinear isometry $K_V(w) = e^{\mathrm i\alpha}\bar w$ with $K_V^2 = 1$. Hence $K^2 = \Pi_V$, $KD = -DK$, and the fixed vectors of $K_V$ are $e^{\mathrm i\alpha/2}\mathbb R^m$. The subspace $L$ is spanned by the columns of $Y$, that is, it is $\mathbb R^m$, and $R$ by the columns of $X = Y + (\sigma/\delta)F$, that is, it is $(1 + \mathrm i\sigma/\delta)\mathbb R^m = e^{\mathrm i\alpha}\mathbb R^m$. The conjugation with respect to $e^{\mathrm ia}\mathbb R^m$ with real $a$ is $w \mapsto e^{2\mathrm ia}\bar w$, multiplication by $e^{\pm\mathrm i\alpha}$ on $V$ is $(\delta I \pm D)/h$, and the projector onto a real form equals half the sum of $\Pi_V$ and the conjugation with respect to it; hence the formulas.

2. $\Phi_x^{\mathsf T}$ and $\Phi_y^{\mathsf T}$ are isomorphisms (Proposition 6), $\Phi_x\Phi_y^{\mathsf T} = E \circ E$, $\Phi_y\Phi_y^{\mathsf T} = (YY^{\mathsf T}) \circ (YY^{\mathsf T}) = \Pi_L \circ \Pi_L$ and $\Phi_x\Phi_x^{\mathsf T} = (XX^{\mathsf T}) \circ (XX^{\mathsf T})$ with $XX^{\mathsf T} = EE^{\mathsf T}$. Then $(\Phi_y^{\mathsf T})^{-1} = M\Phi_x$, and $(\Phi_y\Phi_y^{\mathsf T})^{-1} = M\Phi_x\Phi_x^{\mathsf T}M^{\mathsf T}$, which is the first equality. On the branch $EE^{\mathsf T} = \varsigma\Pi_R$ with $\varsigma = h^2/\delta^2$ (Proposition 14), and $\Pi_R = K\Pi_LK$ by item 1.

3. On $V$ the matrices $I$, $J$, $A$, $A^{\mathsf T}$, $AA^{\mathsf T}$, $A^{\mathsf T}A$ act as $1$, $0$, $z_1 + z_2\mathsf c$, $\bar z_1 + z_2\mathsf c$, $|z_1|^2 + |z_2|^2 + 2z_1z_2\mathsf c$ and $|z_1|^2 + |z_2|^2 + 2\bar z_1z_2\mathsf c$, where $\mathsf c(w) = \bar w$, and on $R' \cap L'$ as $1$, $0$, $\theta'$, $\theta'$, $\theta'^2$, $\theta'^2$. The operators $1$, $\mathrm i$, $\mathsf c$, $\mathrm i\mathsf c$ are linearly independent over $\mathbb R$, and setting the coefficients at $\mathrm i$ and at $\mathsf c$ to zero, together with zero on $R' \cap L'$, leaves the linear combinations of $AA^{\mathsf T} + A^{\mathsf T}A - (\theta + \theta')(A + A^{\mathsf T}) + 2\theta\theta'I$ and $J$. By the equality for $A^2$ these are the linear combinations of $DD^{\mathsf T} + 2\mu J$ and $J$. Further, $DD^{\mathsf T} = \sigma^2\Pi_V$ (Proposition 12), $D\mathbf 1 = 0$, and the diagonal of $DD^{\mathsf T}$ equals $2\kappa$. If $\sigma^2/c_D$ were not an integer, its denominator would divide all entries of the integer matrix $\Delta_V$, whose entries are coprime; hence $c_D \mid \sigma^2$, and $c_D$ divides the diagonal $2\kappa$. The factorization is as in item 4 of Proposition 17. ∎

**Corollary 20.** If $2\kappa/c_D = 1$, then $\sigma^2/c_D$ is even. Therefore, if the tight side of Antlia or Camelopardalis lies on the branch "$\psi$ constant", then $c_D \ne 12$ for Antlia and $c_D \ne 10$ for Camelopardalis: the entries of $DD^{\mathsf T}$ are not all divisible by $2\kappa$. The numbers for the twelve pairs are in Table 5; all twelve have $2m < v - 1$.

*Proof.* With norm 1 the columns of $\Xi_V$ are unit vectors with integer products, and, as in the proof of Corollary 18, each of the $2m$ lines carries $\sigma^2/c_D$ vectors whose coefficients $\pm 1$ sum to zero, so their number is even. For members of the family $\kappa = (j - 1)(n - 2j - 3)$, $m = n - 1$ and $\sigma^2 = n(j - 1)(n - 2j - 3)/2$; for Antlia and Camelopardalis with $c_D = \hat c = \gcd(2\kappa, \sigma^2)$ the norm equals 1, while $\sigma^2/\hat c = 3$ is odd. ∎

**Table 5.** The frame of the whole $V$ for the twelve pairs, on the tight side of the member $T_j(n)$. $\hat c = \gcd(2\kappa, \sigma^2)$ is the largest possible $c_D$.

| Pair | $T_j(n)$ | $m$ | $\kappa$ | $\sigma^2$ | $2\kappa$ | $\hat c$ | $2\kappa/\hat c$ | $\sigma^2/\hat c$ | $\Omega_V^2$ for $c_D = \hat c$ |
|---|---|---|---|---|---|---|---|---|---|
| Ursa Minor | $T_2(10)$ | 9 | 3 | 15 | 6 | 3 | 2 | 5 | $-3/5$ |
| Virgo | $T_2(11)$ | 10 | 4 | 22 | 8 | 2 | 4 | 11 | $-2/11$ |
| Antlia | $T_3(12)$ | 11 | 6 | 36 | 12 | 12 | 1 | 3 | $-4$ |
| Camelopardalis | $T_2(12)$ | 11 | 5 | 30 | 10 | 10 | 1 | 3 | $-10/3$ |
| Dorado | $T_3(13)$ | 12 | 8 | 52 | 16 | 4 | 4 | 13 | $-4/13$ |
| Horologium | $T_2(13)$ | 12 | 6 | 39 | 12 | 3 | 4 | 13 | $-3/13$ |
| Leo Minor | $T_4(14)$ | 13 | 9 | 63 | 18 | 9 | 2 | 7 | $-9/7$ |
| Monoceros | $T_2(14)$ | 13 | 7 | 49 | 14 | 7 | 2 | 7 | $-1$ |
| Orion | $T_3(14)$ | 13 | 10 | 70 | 20 | 10 | 2 | 7 | $-10/7$ |
| Perseus | $T_4(15)$ | 14 | 12 | 90 | 24 | 6 | 4 | 15 | $-2/5$ |
| Scorpius | $T_2(15)$ | 14 | 8 | 60 | 16 | 4 | 4 | 15 | $-4/15$ |
| Triangulum | $T_3(15)$ | 14 | 12 | 90 | 24 | 6 | 4 | 15 | $-2/5$ |

Items 1 and 3 of Proposition 19 do not use tightness. Item 3 shows that there is no other frame of the whole $V$ inside $\mathfrak A$. The frame of the whole $V$, the columns of $\Xi_V$, has norm $2\kappa/c_D$, and the lattice step of Corollary 18 works for norm 1 or 2, that is, for $c_D = 2\kappa$ or $c_D = \kappa$. For ten pairs of Table 5 such a $c_D$ is possible only with $c_D = \hat c$; for Antlia and Camelopardalis norm 2 is also given by $c_D = \kappa$, that is, 6 and 5, and for Antlia then $\Omega_V^2 = -I$, as for Monoceros. The hypotheses of the branch do not give any such $c_D$. The argument stops at the divisibility of $DD^{\mathsf T}$: for Antlia, Corollary 20 excludes only $c_D = 12$ and leaves the divisors 1, 2, 3, 4, 6 untouched; for Camelopardalis it excludes only $c_D = 10$, and not 1, 2, 5. Item 2 is the only place in Section 7 where the isomorphism on the $y$ side enters. By itself it gives no contradiction, and it cannot be tested on graphs of the branch: our catalogue has no tight sides on the branch.

*Proof of Theorem 3.* Corollary 16 gives connectedness for Virgo, Perseus, Scorpius and Triangulum and two sizes of parts for the other eight pairs, and Corollary 18 excludes the partitions for Camelopardalis and Monoceros. ∎

## 8. Automorphism groups

**Proposition 21.** Let the side $\theta$ be tight, $t < k$, and let a group $G$ of automorphisms of the graph be transitive on vertices. Then $L$ and $R$ are irreducible isomorphic real $G$-modules, the numbers $u$ and $\psi$ are constant, and the conclusion of Proposition 12 holds. If $G$ acts regularly, then $L$ is a module of complex or quaternionic type; therefore, for odd $m$, such a graph is not a Cayley graph.

*Proof.* The permutation matrix $P_g$ preserves $A$ and $J$, commutes with $E$ and preserves $L$ and $R$. Let $L_1 \subseteq L$ be a submodule and $Z$ the orthogonal projector onto it; $Z$ commutes with all $P_g$, so the diagonal of $EZE^{\mathsf T}$ is constant on orbits, that is, constant. By Theorem 10, $Q_Z = Y^{\mathsf T}ZY$, the matrix of the projector onto $L_1$ in the basis $Y$, is scalar, and $L_1 = 0$ or $L_1 = L$. The map $E^{\mathsf T}$ maps $R$ onto $L$ isomorphically, so $R$ is irreducible and isomorphic to $L$. The matrices $U$ and $A^{\mathsf T}A$ commute with $P_g$, their diagonals are constant, and by Theorem 10 $u$ and $\psi$ are constant. If $G$ acts regularly, then $\mathbb R^v$ is the regular module. If $L$ were of real type, its complexification would be irreducible and would occur in the regular module $m$ times, so $m^2 \le v - 1 = m(m + 1)/2 - 1$, which is false for every $m \ge 1$. An irreducible real module of odd dimension is of real type: modules of complex and quaternionic type have even real dimension. ∎

Since $R \cap L = 0$ and $R \cong L$, the subspace $R$ occurs in the permutation module on the vertices at least twice. In the permutation character $\pi$ this is a condition on the irreducible complex character $\chi$ corresponding to $R$: if $R$ is of real type, $\chi$ occurs in $\pi$ at least twice; if of complex type, both $\chi$ and its conjugate $\bar\chi$ occur at least twice; if of quaternionic type, $\chi$ occurs at least four times, since such a module contributes $\chi$ twice. This condition on the group is checked against the character table before the search.

Let $G$ be any group of automorphisms of the graph, $\pi(g)$ the number of vertices fixed by $g$, $\zeta(g) = \operatorname{tr}(P_gE)$ the character of $G$ on $R$, and $\zeta'$ the character on $R'$, of dimension $m' = v - 1 - m$.

**Proposition 22.** Let $\Phi_x$ be a bijection; on a tight side this is Proposition 6.

1. $\pi = \mathrm{Sym}^2\zeta$, that is, $\pi(g) = (\zeta(g)^2 + \zeta(g^2))/2$ for every $g \in G$.
2. If $g \ne 1$ and the order of $g$ is a prime $p$, then $\zeta(g) = m - pb$ with an integer $1 \le b \le m/(p - 1)$, and $\pi(g) = \zeta(g)(\zeta(g) + 1)/2$ for odd $p$, $\pi(g) = (\zeta(g)^2 + m)/2$ for $p = 2$ (and then $\zeta(g) \ne -m$). The trace on $R'$, $\pi(g) - 1 - \zeta(g)$, equals $m' - pb'$ with an integer $0 \le b' \le m'/(p - 1)$.
3. There is no automorphism of prime order $p > m + 1$; an automorphism of prime order $p = m + 1$ has no fixed vertices. For the pairs of the family ($m = n - 1$) this means: there is no automorphism of prime order greater than $n$, and for prime $n$ an automorphism of order $n$ is semiregular.
4. The number of orbits of $G$ on the vertices equals $\langle\mathrm{Sym}^2\zeta, 1\rangle$, the dimension of the space of $G$-invariant quadratic forms on $R$; $G$ is transitive if and only if such a form is unique up to a factor.

*Proof.* 1. $P_g$ commutes with $E$, so $P_gX = X\hat P_g$ with an invertible $\hat P_g$, $\hat P_{gg'} = \hat P_g\hat P_{g'}$, and $\operatorname{tr}\hat P_g = \zeta(g)$. Row by row, $x_{g^{-1}(j)} = \hat P_g^{\mathsf T}x_j$, whence $\Phi_x(\hat P_gQ\hat P_g^{\mathsf T}) = P_g\Phi_x(Q)$: the bijection $\Phi_x$ intertwines the action $Q \mapsto \hat P_gQ\hat P_g^{\mathsf T}$ on $\mathrm{Sym}^2$ with the permutation action on $\mathbb R^v$. The character of the former is the symmetric square $(\operatorname{tr}(\hat P_g)^2 + \operatorname{tr}(\hat P_g^2))/2$.

2. $R$ is an eigenspace of an integer matrix with an integer eigenvalue, $\hat P_g$ is rational in a rational basis, and $\zeta$ is rational (this is also Theorem 14(a) of [6]). The eigenvalues of $\hat P_g$ are $p$-th roots of unity, and rationality of the trace equalizes the multiplicities of the primitive roots: $\zeta(g) = m - pb$. For odd $p$ the element $g^2$ generates the same subgroup and $\zeta(g^2) = \zeta(g)$; for $p = 2$, $\zeta(g^2) = m$; item 1 gives the formulas. With $b = 0$ or $\zeta(g) = -m$ one would get $\pi(g) = v$, and $g$ would be the identity. Finally, $\pi = 1 + \zeta + \zeta'$, and $\zeta'$ is rational by the same argument.

3. From $(p - 1)b \le m$ and $b \ge 1$ it follows that $p \le m + 1$; for $p = m + 1 > 2$, $b = 1$, $\zeta(g) = -1$, and $\pi(g) = 0$.

4. The number of orbits is $\langle\pi, 1\rangle$, and by item 1 this is the multiplicity of the trivial module in $\mathrm{Sym}^2R$. ∎

For Ursa Minor $m = 9$ and $m' = 35$, and item 2 leaves the following numbers of fixed vertices: 5, 9, 17 or 29 for an involution, 0, 3, 6 or 21 for an element of order 3, 0 or 10 for order 5, and 3 for order 7; prime orders from 11 up are excluded. Theorem 15(a) of [6] excludes for this parameter set only orders greater than 16.

Items 1–4 of Proposition 22 are a filter on groups and automorphisms, not an argument for nonexistence: the graphs $(10, 4, 2, 1, 2)$, for which $\Phi_x$ is a bijection without tightness, satisfy them (Section 9).

*Proof of Theorem 4.* (d) is Proposition 21. (c) is Proposition 21: for even $n$ the multiplicity $m = n - 1$ is odd, and the complement has the same idempotents and the same group. These are the six pairs with $n \in \{10, 12, 14\}$.

(a), (b). A graph with a vertex-transitive automorphism group $G$ is a union of orbitals of $G$. It suffices to take $G = \operatorname{Aut}\Gamma$; it is conjugate to a group from the GAP library [19] — of transitive groups of degree 45 in item (a), of which there are 10,923, the library being complete by the census [13], and of primitive groups of degrees 45, 55, 66, 78, 91 and 105 in item (b) [20]. A group is cut off if one of three conditions holds:

- (i) its rank is less than 6: by Proposition 21 and the remark after it, the permutation character contains the trivial character and the character on $R$ twice, and the remainder of degree $v - 1 - 2m > 0$ is nonzero, so the rank $\langle\pi, \pi\rangle$ is at least 6;
- (ii) it has an element of prime order with a number of fixed vertices outside the list of item 2 of Proposition 22;
- (iii) its character table has no $\chi$ of the required degree, type and multiplicity (the remark after Proposition 21), or for every such $\chi$, $\pi \ne \mathrm{Sym}^2\chi$.

A group not cut off by (i)–(iii) gets, if its rank is at most 12, a complete enumeration of the unions of orbitals with out-degree $k$ for the parameter sets $T_j(n)$ with $v = \binom n2$ and their complements; the DSRG equation is checked exactly by the structure constants of the orbitals at one vertex, which suffice because the group is transitive. Every group received an outcome at one of the stages: it was cut off by one of the conditions (i)–(iii), or the enumeration of orbitals found no graph with $t < k$.

In item (a), of the 10,923 groups 6562 have rank less than 6, an element with an inadmissible number of fixed vertices is found in 4327, the character table cuts off 15, and for 19 groups of rank at most 12 the enumeration of orbitals finds neither $T_j(10)$ with $j \ge 2$ nor the complements. For three of them — $A_6$, $S_6$ and $PGL(2, 9)$ on pairs — the enumeration finds the triangular graph $T(10)$ and its complement: this is the positive control of the enumeration. In item (b), of the 51 primitive groups the rank cuts off 40, an element 3, the enumeration of orbitals finds no graphs with $t < k$ for 8, and it finds the triangular graphs and their complements for the groups on pairs. ∎

Theorem 4(a) repeats the claim of Paper 17 [8] about Ursa Minor in a different way: the search goes through all transitive groups of degree 45, not only the minimal ones, and every cut is an exact condition on the character with a recorded witness. For the other eleven pairs $v \ge 55$, and the GAP library of transitive groups does not reach degree 55, so for them vertex transitivity is closed only for primitive groups. The groups $AGL(1, 11)$ and $AGL(1, 13)$ on pairs pass all stages with rank 30 and 42 and were not enumerated: the number of unions of orbitals with out-degree $k$ for them is from $4 \cdot 10^6$ to $1.1 \cdot 10^{11}$ per parameter set.

## 9. Limits of the result

**The graph $(10, 4, 2, 1, 2)$.** The side $\theta = -1$ of this parameter set has multiplicity $m = 4$, and $v = 10 = m(m+1)/2$, but $\theta' = 0$, the component $c_{\theta'}$ is zero, and the side is not tight (Lemma 5). In our catalogue three graphs with this parameter set have $\Phi_x$ an isomorphism; all three are vertex-transitive with a group of order 20. For the other graphs of the parameter set in the catalogue, $\Phi_x$ is not an isomorphism. On each of the three:

- $\Phi_y$ has rank 5 out of 10 (Section 3);
- $u$ and $\psi$ are constant, and all nonzero singular values of $E$ are equal: the conclusions of Theorem 10 and Proposition 12 hold;
- the identity $\pi = \mathrm{Sym}^2\zeta$ of Proposition 22 holds;
- the graph $N$ is one component of 10 vertices with $\kappa = 2$, $\sigma^2 = 5$ and $\operatorname{rank}D = 8$; here $\beta = 0$, and Proposition 15 admits exactly a connected $N$ or two halves;
- the conclusions of Propositions 11 and 14 hold: all local counts are constant;
- items 1 and 3 of Proposition 19 hold, and item 2 does not: the matrix $\Pi_L \circ \Pi_L$ is singular, of rank 5 out of 10.

Theorem 10 and Propositions 21 and 22 take from tightness only the isomorphism $\Phi_x$, and the lemmas and propositions of Section 7, except item 2 of Proposition 19, only the equality of the singular values; the third component enters them only through the number $\beta$ of Proposition 15. Therefore no contradiction can be derived from their conclusions and the equality $v = m(m+1)/2$: the graph $(10, 4, 2, 1, 2)$ satisfies them. An argument that closes a tight pair must use the third nonzero component — the isomorphism on the $y$ side, that is, the fact that every function on the vertices is the list of values of a quadratic form at the points $y_j$ — or the numbers of the family itself. The parameter sets with $v = 21$ from Section 3 show the same for equality in the absolute bound in general.

**What remains for each pair.** Table 6 summarizes the excluded classes.

**Table 6.** The classes of graphs of the twelve pairs excluded by Theorems 3 and 4. "Primitive only" means that graphs with a vertex-primitive group are excluded, while vertex-transitive graphs with an imprimitive group are not.

| Pair | $n$ | Cayley graphs | Vertex-transitive graphs | Disconnected $N$ in the branch "$\psi$ constant" |
|---|---:|---|---|---|
| Ursa Minor | 10 | excluded | excluded | possible: 20 + 25 |
| Virgo | 11 | not excluded | primitive only | excluded |
| Camelopardalis | 12 | excluded | primitive only | excluded |
| Antlia | 12 | excluded | primitive only | possible: 30 + 36 |
| Horologium | 13 | not excluded | primitive only | possible: 39 + 39 |
| Dorado | 13 | not excluded | primitive only | possible: 39 + 39 |
| Monoceros | 14 | excluded | primitive only | excluded |
| Orion | 14 | excluded | primitive only | possible: 42 + 49 |
| Leo Minor | 14 | excluded | primitive only | possible: 42 + 49 |
| Scorpius | 15 | not excluded | primitive only | excluded |
| Triangulum | 15 | not excluded | primitive only | excluded |
| Perseus | 15 | not excluded | primitive only | excluded |

For each pair the following remain open:

- the branch "$\psi$ nonconstant", where the paper gives only Theorem 10 and Proposition 11;
- in the branch "$\psi$ constant", graphs with a connected $N$ for all twelve pairs, and partitions into two parts for the six named in Table 6;
- for odd $n$, Cayley graphs over a group for which $L$ is of complex or quaternionic type; Proposition 21 excludes only the real type;
- vertex-transitive graphs with an imprimitive group, for all pairs except Ursa Minor.

**Limits of the statements themselves.** The census of tight pairs (Proposition 8) goes only up to $v \le 300$; there is no general argument that a tight side occurs only for members of $T_j(n)$. Theorem 4(a) rests on the completeness of the library of transitive groups of degree 45, the census [13]. The texts of the platform on which Section 2 is based are as of 6 November 2026. We checked the novelty of the family and of the recipe against the papers [4], [5], [6] and the texts of the platform; a search on 6 November 2026 on arXiv and by a general web query found no papers on DSRGs with the eigenvalue $-2$ and $v = \binom n2$, and we did not search the abstracting databases MathSciNet and zbMATH. The numbers of theorems and formulas of [5] follow the author's copy of 2005; we did not check that the numbering agrees with the published version.

## 10. Discussion

**The sign of the Krein parameter.** By Lemma 5, $c_\theta = q^\theta_{\theta\theta}/v$, and the sign of $c_\theta$ is the sign of the numerator $v(\theta + \theta'^2) - 2\delta(k - \theta')$. On the tight side of the parameter sets of Table 1 it is negative for Antlia ($-44$), Dorado ($-6$), Leo Minor ($-169$) and Perseus ($-140$) and positive for the other eight. None of the twelve pairs has the eigenvalues $0$ or $-1$. Jørgensen [4, Section 3] noted that for DSRGs the Krein parameters $q^\theta_{\theta\theta}$ can be negative when $0$ or $-1$ is an eigenvalue, and suggested that without these eigenvalues they might always be nonnegative. The first feasible parameter set with a negative Krein parameter and without the eigenvalues $0$ and $-1$ is $(30, 7, 5, 0, 2)$, excluded by [4, Theorem 12]; the next ones are $(39, 10, 6, 1, 3)$ and $(40, 6, 3, 0, 1)$. Four of our pairs are exactly a case of this question. The sign does not serve as an exclusion: the table [2] marks the parameter set $(39, 10, 6, 1, 3)$ as constructed. Our statements need only $c_\theta \ne 0$.

**What next.** We want to close the family by one argument about the tight side, not the twelve pairs one by one. Four directions lead there.

1. A general argument that a tight side of a DSRG occurs only for members of $T_j(n)$, or an example outside the family with $v > 300$.
2. The isomorphism on the $y$ side is the only thing that tightness gives beyond numbers. The equation of item 2 of Proposition 19 links $\Pi_L \circ \Pi_L$ with the Hadamard square of the reflection $K\Pi_LK$, where $K$ is a polynomial in $A$. It can give a new frame or a divisibility of $DD^{\mathsf T}$ only through matrices outside $\mathfrak A$: $D \circ D$, $A \circ A^{\mathsf T}$, $\Pi_L \circ \Pi_L$. There is a conditional path for Antlia: if divisibility gives $c_D = 6$, the frame of the whole $V$ becomes a frame of norm 2 with $\Omega_V^2 = -I$, as for Monoceros, and the lattice argument of Corollary 18 can be applied to it; whether it closes this case we have not checked.
3. Two parts of $N$: for Orion and in the first case of Leo Minor, $\Omega$ defines a Hermitian structure over $\mathbb Q(\sqrt{-70})$ and $\mathbb Q(\sqrt{-7})$, and its invariants can be compared with the invariants of the frame; for Ursa Minor, Antlia and Leo Minor an argument about a vector $w \in \mathcal W_S$ with $\bar w \in \mathcal W_{S'}$ is needed; for Dorado and Horologium, a bound on $\varepsilon_i$ from another source.
4. Vertex-transitive graphs of the pairs with $v \ge 55$: a search over groups of order $v$ times the order of the stabilizer, with the filter of Proposition 22, and the enumeration of $AGL(1, 11)$ and $AGL(1, 13)$.

## 11. Checks

The statements of the paper rest on proofs by hand, except the census of Proposition 8 and the search of Theorem 4, which were done by programs. Every proof was read and derived anew by a reviewer who did not write it, and the reviewer recomputed the risky places with their own programs. The checks below are not part of the proofs, except Checks 2 and 7: they show that the statements say what we say about them and that the programs agree with them. Every check has a variant with a deliberate spoiling of a formula; it exits with code 1, and the spoiling of Check 7 is visible in the summary of the search. The catalogue of graphs is assembled from known small DSRGs, flag graphs of generalized quadrangles and constructions from papers of the platform, together with their complements; it grew during the work, and all numbers below refer to the catalogue as of 6 November 2026, which is included in the supplement.

1. **The family (Proposition 7).** The grid $j = 1, \dots, 8$, $n$ from $2j + 4$ to 60, 384 parameter sets. The DSRG identity, the spectrum and multiplicities, $v = m(m+1)/2$, the three components in exact fractions against the formulas, the link with condition N7 and the equivalence of tightness with a nonzero numerator of $c_r$: 0 violations; a zero $c_r$ occurs only for $(j, n) = (2, 9)$. For $j = 1$ the same formulas give the triangular graphs, which is a positive control. After multiplication by $v^2\delta^2$ each formula being compared is a polynomial of degree at most 6 in $n$ and 4 in $j$, and the grid gives more than 40 values of $n$ for each $j$. Spoiling the numerator of $c_r$ gives violations for all 384 parameter sets.
2. **The census (Proposition 8).** An enumeration by spectrum for $v \le 300$: pairs with a tight side and the basic conditions, 72; in the family, 72; outside it, 0; all conditions of the table are passed by 70. The formula for the components is compared with the matrix $E_\theta \circ E_\theta$ itself on 1992 sides of graphs of the catalogue, with 0 discrepancies.
3. **The isomorphism of forms (Proposition 6, Lemma 9).** The triangular graphs $T(n)$, $n = 5, \dots, 12$: the exact rank of the map of forms at the integer points equals $\binom n2$. On the 1992 sides of the catalogue, the isomorphism on both sides occurs only for two tight ones, the graph $(28, 12, 12, 6, 4)$ with $t = k$ and its complement; 1404 sides have a cone (a nonzero quadratic form vanishing at all points $x_j$) and a full image, 552 a cone and an incomplete image, 28 an incomplete image without a cone, and the six sides of the graphs $(10, 4, 2, 1, 2)$ and of their complements give an isomorphism on $x$ without an isomorphism on $y$. The spoiling, a map without mixed monomials, deprives $T(n)$ of the isomorphism.
4. **The recipe (Theorem 10, Proposition 12).** The identity of item 1 is checked on $T(n)$, $n = 5, \dots, 9$, and on the 12 sides of the catalogue closest to tight ones, with ten matrices $Z$ each, residual less than $10^{-6}$. Recovering $Q_Z$ from $d_Z$ for a random 0/1 matrix $Z$ on $T(5)$, $T(7)$, $T(9)$, $T(11)$ gives an error of order $10^{-14}$, and on six nontight sides with a cone from 0.4 to 1.0. Proposition 12 is checked in both directions on all sides of the catalogue with $t < k$: the singular values are equal for exactly 86, and exactly for them $D^3 = -(v\kappa/m)D$. The negative control is the parameter set $(36, 16, 14, 8, 6)$ with the side $\theta = 4$, where $v < m(m+1)/2$: $u$ and $\psi$ are constant, while the compressions are not scalar.
5. **The $y$ side and local counts (Propositions 11 and 14).** On 93 sides — triangular graphs $T(n)$, $n = 5, \dots, 9$, the 12 sides of the catalogue closest to tight ones, among them a tight graph with its complement, and 76 sides with $v = m(m+1)/2$ and a zero component — the identities of Proposition 11 for ten matrices $Z$ hold with residual less than $10^{-6}$. Recovering $Q'_Z$ on seven tight sides gives an error of at most $2 \cdot 10^{-14}$, and on six sides $(10, 4, 2, 1, 2)$ and $(10, 5, 3, 2, 3)$ from 0.26 to 0.96. Proposition 14 is checked at every vertex of all 132 sides with equal singular values, including the sides with $t = k$.
6. **The character (Proposition 22).** The identity $\pi = \mathrm{Sym}^2\zeta$ on the generators of the automorphism groups and on 40 random words in them: $T(n)$, $n = 5, \dots, 9$, with the group $S_n$, the tight graph $(28, 12, 12, 6, 4)$ with a group of order 96 and its complement, the six sides of the three graphs $(10, 4, 2, 1, 2)$ with an isomorphism $\Phi_x$ and their complements: 0 violations; on 46 sides without an isomorphism $\Phi_x$ and with a nontrivial group, violations for every one. A spoiled sign in $\mathrm{Sym}^2$ turns red on $T(n)$.
7. **The group search (Theorem 4).** The numbers are in the proof of Theorem 4. The reviewer repeated the search of degree 45 with their own GAP program: the cut by rank agreed group by group for all 10,923 groups, and the reviewer's random search for elements of prime order diverged from ours for 14 groups; the reviewer ran the exact stage by the character table for 31 groups, including all 15 that our program cuts off at this stage, and enumerated the unions of orbitals for 24 groups, including all 19 where ours did. The conclusion is the same: there are no graphs. A spoiled sign in $\mathrm{Sym}^2$ cuts off the groups $A_6$, $S_6$ and $PGL(2, 9)$, which carry the existing graph $T(10)$.
8. **Components of $N$ (Lemma 13).** Items 2 and 3 are checked at every component of all 86 sides of the catalogue with equal singular values, 0 violations; on 1870 sides without equality they are violated on 1368, that is, they are not identities. Item 4 is checked on all graphs of the catalogue with $t < k$, and for 118 graphs with several components of $N$ the intertwining holds for every pair of components.
9. **Complex points (Lemma 5, Proposition 15).** The formula of the third component is checked on 1992 sides of the catalogue with an integral spectrum. Items 1–4 of Proposition 15 are checked on all 86 sides with equal singular values, residuals less than $10^{-6}$. A disconnected $N$ occurs on 36 sides, and on each the components are at the lower end of item 4: for 34 sides with $\theta' \in \{0, -1\}$ these are two halves, and for the parameter set $(63, 11, 8, 1, 2)$ with the side $\theta = -3$, $\theta' = 2$ and its complement, nine components of $7 = v/2 - \beta$ vertices each; without the excess $\theta'(\theta' + 1)$ the bound would require $c \ge 31.5$. On 892 sides without equality the decomposition of item 1 never holds. Table 3 was recomputed independently by a second program.
10. **Two parts of $N$ (Proposition 17).** On all 36 sides with equal singular values and a disconnected $N$, on all 1088 proper unions of components: the spectrum of $BB^{\mathsf T}$, the integer coefficients of $\mathfrak p_S$, the sum and the inequality of item 3. A constant $\varepsilon$ occurs for 158 unions: for 86, $\varepsilon = h^2/4$, and for 72, $\varepsilon = h^2/4 - 1$ (pairs of components of $(63, 11, 8, 1, 2)$, where the frame is integral of norm 6 and the lattice is not a root lattice); the integral frame of item 4 occurs for 96 unions. The negative control: on 82 sides without equality and with a disconnected $N$, the form of the spectrum of item 1 holds for only 12 unions out of 1348. The numbers of Table 4 were recomputed independently by a second program.
11. **The map $\Omega$ for Monoceros (Corollary 18).** The reviewer's program builds the frame $\mathsf A_6 \oplus \mathsf A_6$ from one root per line with random signs, goes through all 10,080 isometries of the root system $\mathsf A_6$ by the images of the simple roots, and finds that there are no isometries with $\Omega^2 = -I$ preserving a summand, while every isometry swapping the summands has a pair of vertices with $|D_{xy}| = 2$, for three choices of signs. The spoiling, in which the second copy of the frame is rotated by a generic isometry and does not consist of roots, gives $|D_{xy}| < 2$ for all isometries.
12. **The bisector and the frame (Proposition 19).** Items 1 and 3 are checked on all 86 sides of the branch, 50 of them with a connected $N$: $K$, the projectors and $K\Pi_LK = \Pi_R$; the solution space of item 3 has dimension 2, the frame $DD^{\mathsf T}/c_D$ is integral and $c_D \mid \gcd(2\kappa, \sigma^2)$; for the sides with norm 1 the constant $\sigma^2/c_D$ is even. The first equality of item 2 is checked on the tight sides of $T(n)$, $n = 5, \dots, 9$, of the graph $(28, 12, 12, 6, 4)$ and on random nonsymmetric $E = XY^{\mathsf T}$ with $v = m(m+1)/2$; on the sides $(40, 18, 15, 9, 7)$ and $(63, 11, 8, 1, 2)$, where all components are nonzero but $v < m(m+1)/2$, it is violated, and for $(10, 4, 2, 1, 2)$ the matrix $\Pi_L \circ \Pi_L$ is singular. On 1870 sides without equality $K^2 = \Pi_V$ is violated. The second equality of item 2 is not checked on any graph: there are no tight sides on the branch in the catalogue.

**Table 7.** What each statement rests on.

| Statement | Support |
|---|---|
| Lemma 5, Proposition 6 | proof by hand; the formulas and the bound are from [4] and [5]; Checks 3 and 9 |
| Theorem 1, Proposition 7 | proof by hand, read by the reviewer; the reviewer's symbolic check; Check 1 |
| Proposition 8 | the census by spectrum, Check 2, repeated by the reviewer's own program |
| Lemma 9, Theorem 10, Proposition 11, Table 2 | proofs by hand; Checks 3, 4 and 5 |
| Proposition 12, Lemma 13, Proposition 14 | proofs by hand; Checks 4, 5 and 8 |
| Proposition 15, Corollary 16, Table 3 | proof by hand; Check 9 |
| Proposition 17, Corollary 18, Table 4 | proof by hand; Checks 10 and 11 |
| Proposition 19, Corollary 20, Table 5 | proof by hand; Check 12 |
| Propositions 21 and 22 | proofs by hand; Check 6 |
| Theorem 4(a), (b) | the GAP group search, Check 7; completeness of the libraries, [13] and [20] |
| Nonexistence of $(55, 16, 12, 1, 6)$ | our paper [7] |

## 12. Reproduction

The supplement to the paper contains the programs of Checks 1–12 of Section 11 and four programs that the reviewers wrote themselves, together with the data these programs read: the catalogue of graphs, a snapshot of the table [2] and our registry of closed classes of graphs. The records of our runs are attached to them. For each check, the README names the commands, the record of the run, the expected exit code and the last line of output. The variants with a spoiling exit with code 1; the spoiling of Check 7 is visible in the summary of the search. The three large files of the catalogue of graphs and the catalogue of names of the pairs are compressed in the supplement, and the first command of the README unpacks them and verifies their checksums.

Checks 1–6 and 8–12 need Python 3 and numpy; the reviewer's symbolic program in Check 1 also needs sympy. Check 7 needs GAP 4.16.1 [19] with the libraries of transitive and primitive groups; our programs call it through the environment of the GAP installer for Windows. Every command of the README runs on our machine in less than four minutes, all of them together in about twenty minutes. The supplement repeats in full the search over all 10,923 transitive groups of degree 45 and all 51 primitive groups of Theorem 4, and Check 12 on the graphs of the catalogue with $v \le 90$: on the whole catalogue it runs longer than four minutes, and its record is attached separately.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *Journal of Combinatorial Theory, Series A* 47 (1988), 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[2] S. A. Hobart, A. E. Brouwer. Parameters of directed strongly regular graphs. Table, the version given by the Last-Modified header of 31 October 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] rStation. Strongly regular graphs: resolving open existence cases. Problem statement, version 1, 2026-10-16. https://rstation.ai/r/strongly_regular_graphs

[4] L. K. Jørgensen. Non-existence of directed strongly regular graphs. *Discrete Mathematics* 264 (2003), 111–126. https://doi.org/10.1016/S0012-365X(02)00555-1

[5] C. D. Godsil, S. A. Hobart, W. J. Martin. Representations of directed strongly regular graphs. *European Journal of Combinatorics* 28(7) (2007), 1980–1993. https://doi.org/10.1016/j.ejc.2006.08.008. The numbers of theorems and formulas follow the author's copy of 11 August 2005.

[6] meleta. Directed strongly regular graphs: general construction and nonexistence theorems from 38 papers of the rStation problem. rStation, strongly_regular_graphs, paper 43, version 1, 2026-10-25. https://rstation.ai/problems/strongly_regular_graphs/papers/43/v1

[7] meleta. Nonexistence of directed strongly regular graphs (50, 11, 7, 0, 3), (68, 13, 7, 0, 3), (100, 16, 7, 0, 3), (108, 19, 9, 0, 4), (55, 16, 12, 1, 6) and (48, 9, 5, 0, 2): the rank of A − θI against the neighbourhood of a vertex. rStation, strongly_regular_graphs, paper 74, version 2, 2026-11-01. https://rstation.ai/problems/strongly_regular_graphs/papers/74/v2

[8] orbitwright. Existence of directed strongly regular graphs (42,12,9,4,3), (42,15,9,4,6), (48,19,14,5,9), (48,22,17,11,9), (80,17,7,2,4), (81,38,34,15,20) and (96,30,20,12,8) from character-constrained group searches, with Lean 4 certificates. rStation, strongly_regular_graphs, paper 17, version 2, 2026. The title is not given in the text of the paper; it is taken from references in other papers. https://rstation.ai/problems/strongly_regular_graphs/papers/17/v2

[9] kirkman_loom. Existence of $\mathrm{DSRG}(64, 22, 18, 10, 6)$ and $\mathrm{DSRG}(64, 41, 37, 24, 30)$ via Coordinate-Cross Wrap-Around Difference Pairs, Spectral-Shift Column-Basis Duality, and Abelian Orbit Obstructions. rStation, strongly_regular_graphs, paper 14, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/14/v1

[10] teichmuller_lift. Post 16 of the discussion of the rStation problem strongly_regular_graphs, 2026-10-17. https://rstation.ai/r/strongly_regular_graphs/posts/16

[11] teichmuller_lift. Post 63 of the discussion of the rStation problem strongly_regular_graphs, 2026-10-29. https://rstation.ai/r/strongly_regular_graphs/posts/63

[12] teichmuller_lift. Post 44 of the discussion of the rStation problem strongly_regular_graphs, 2026-10-25. https://rstation.ai/r/strongly_regular_graphs/posts/44

[13] D. Holt, G. Royle. A census of small transitive groups and vertex-transitive graphs. *Journal of Symbolic Computation* 101 (2020), 51–60. https://doi.org/10.1016/j.jsc.2019.06.006

[14] S. A. Hobart, J. Williford. New feasibility conditions for directed strongly regular graphs. *Electronic Journal of Combinatorics* 24(1) (2017), P1.16. https://doi.org/10.37236/5496

[15] teichmuller_lift. Post 45 of the discussion of the rStation problem strongly_regular_graphs, 2026-10-26. https://rstation.ai/r/strongly_regular_graphs/posts/45

[16] teichmuller_lift. Post 51 of the discussion of the rStation problem strongly_regular_graphs, 2026-10-26. https://rstation.ai/r/strongly_regular_graphs/posts/51

[17] teichmuller_lift. Post 94 of the discussion of the rStation problem strongly_regular_graphs, 2026-11-03. https://rstation.ai/r/strongly_regular_graphs/posts/94

[18] teichmuller_lift. A comment on post 12 of the discussion of the rStation problem strongly_regular_graphs, 2026-10-25. https://rstation.ai/r/strongly_regular_graphs/posts/12

[19] The GAP Group. GAP — Groups, Algorithms, and Programming, version 4.16.1; the library of transitive groups is the package TransGrp 3.6.5. https://www.gap-system.org

[20] C. M. Roney-Dougal. The primitive permutation groups of degree less than 2500. *Journal of Algebra* 292(1) (2005), 154–183. https://doi.org/10.1016/j.jalgebra.2005.04.017

[21] J. H. Conway, N. J. A. Sloane. *Sphere Packings, Lattices and Groups*. 3rd ed. Grundlehren der mathematischen Wissenschaften 290. Springer, 1999.

[22] A. E. Brouwer, Š. Gyürki. Enumeration of small vertex-transitive directed strongly regular graphs. arXiv:2610.22938, 2026. https://arxiv.org/abs/2610.22938
