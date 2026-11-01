# Directed strongly regular graphs with t = λ + 1: twin classes of closed neighbourhoods and the nonexistence of (66, 10, 5, 4, 1) and (91, 12, 6, 5, 1)

## 1. Problem and result

A directed strongly regular graph (DSRG) with parameters $(v, k, t, \lambda, \mu)$ is a loopless directed graph on $v$ vertices whose adjacency matrix $A$ satisfies

$$
AJ = JA = kJ, \qquad A^2 = tI + \lambda A + \mu (J - I - A),
$$

where $J$ is the all-ones matrix [1]. Every vertex has $k$ outgoing and $k$ incoming arcs, $t$ of them reciprocated, and the number of paths of length 2 from $x$ to $y \ne x$ is exactly $\lambda$ if the arc $x \to y$ is present and exactly $\mu$ if it is not. The heads of the arcs leaving a vertex $x$ are called its out-neighbours, and their set is denoted $\Gamma^+(x)$. The complement, the graph with matrix $J - I - A$, is also a DSRG, with parameters $(v, v - k - 1, v - 2k + t - 1, v - 2k + \mu - 2, v - 2k + \lambda)$ [1]; the complement of the complement is the original graph, so a graph with a given parameter set exists exactly when a graph with the complementary set exists, and parameter sets are treated in pairs. Throughout, $0 < t < k < v - 1$.

The table of Hobart and Brouwer [2] collects the feasible parameter sets with $v \le 110$, their constructions and their nonexistence results. The rStation problem `strongly_regular_graphs` [3] asks to resolve the open sets of this table. In the version of the table of 31 October 2026, 700 sets have $t = \lambda + 1$: 609 constructed, 67 marked as nonexistent and 24 open. Of them, 32 sets have $\mu = 1$, and five of these 32 are open. This version already marks as nonexistent the sets $(40, 9, 6, 5, 1)$ and $(80, 19, 13, 12, 2)$ of Theorem 2 together with their complements, by a condition from [5]. The sets of Theorems 1 and 4 and the set $(96, 15, 10, 9, 1)$ are open in it.

The paper studies the family $t = \lambda + 1$ through the matrix $B = A + I$. Its row $x$ is the closed out-neighbourhood $N^+[x] = \{x\} \cup \Gamma^+(x)$, and its column $y$ is the closed in-neighbourhood $N^-[y]$. Vertices $x \ne y$ with $N^+[x] = N^+[y]$ are called *row twins*, and those with $N^-[x] = N^-[y]$ *column twins*. The class $C_x$ is the vertex $x$ together with its row twins, and the class $D_x$ is the vertex together with its column twins; $a = |C_x|$ and $d = |D_x|$. We also put $K = k + 1$ and $q = \lambda + 2 - \mu$; $f$ is the multiplicity of the eigenvalue $q - 1$ of $A$ (Lemma 5).

**Theorem 1.** There is no directed strongly regular graph with parameters $(66, 10, 5, 4, 1)$ or $(91, 12, 6, 5, 1)$, and none with the complementary parameters $(66, 55, 50, 45, 50)$ or $(91, 78, 72, 66, 72)$.

**Theorem 2.** There is no directed strongly regular graph with parameters $(40, 9, 6, 5, 1)$, $(80, 19, 13, 12, 2)$ or $(96, 15, 10, 9, 1)$, and none with the complementary parameters $(40, 30, 27, 21, 27)$, $(80, 60, 54, 42, 54)$ or $(96, 80, 75, 65, 75)$.

**Theorem 3.** If a DSRG with $t = \lambda + 1$ and $\mu < \lambda + 2$ exists, then

$$
(\lambda + 2 - \mu)^2 \le \mu(v - k - 1). \tag{1}
$$

**Theorem 4.** There is no directed strongly regular graph with parameters $(28, 6, 3, 2, 1)$, and none with the complementary parameters $(28, 21, 18, 15, 18)$.

**Table 1.** The six closed pairs. The spectrum of $A$ is written as eigenvalues with their multiplicities.

| Set | Complement | Spectrum of $A$ | What fails | Where proved |
|---|---|---|---|---|
| $(66, 10, 5, 4, 1)$ | $(66, 55, 50, 45, 50)$ | $10^1, 4^{11}, (-1)^{54}$ | $k = 2\lambda + 2$, $\lambda = 4$: all classes are pairs, but $\lvert N^+[x]\rvert = 11$ | Theorem 15 |
| $(91, 12, 6, 5, 1)$ | $(91, 78, 72, 66, 72)$ | $12^1, 5^{13}, (-1)^{77}$ | $k = 2\lambda + 2$, $\lambda = 5$: all classes are pairs, but $\lvert N^+[x]\rvert = 13$ | Theorem 15 |
| $(40, 9, 6, 5, 1)$ | $(40, 30, 27, 21, 27)$ | $9^1, 5^{5}, (-1)^{34}$ | $q = 6 > \mu f = 5$ | Theorem 3 |
| $(80, 19, 13, 12, 2)$ | $(80, 60, 54, 42, 54)$ | $19^1, 11^{5}, (-1)^{74}$ | $q = 12 > \mu f = 10$ | Theorem 3 |
| $(96, 15, 10, 9, 1)$ | $(96, 80, 75, 65, 75)$ | $15^1, 9^{8}, (-1)^{87}$ | $q = 10 > \mu f = 8$ | Theorem 3 |
| $(28, 6, 3, 2, 1)$ | $(28, 21, 18, 15, 18)$ | $6^1, 2^{7}, (-1)^{20}$ | $k = 2\lambda + 2$, $\lambda = 2$: a vertex without a twin is excluded by the solver; without such a vertex all classes are pairs, but $\lvert N^+[x]\rvert = 7$ | Theorem 4, Section 6 |

**How the proof works.** When $t = \lambda + 1$, the equation for $A^2$ becomes $B^2 = qB + \mu J$ (Lemma 5). The entry $(x, y)$ of this equation is the number of vertices in $N^+[x] \cap N^-[y]$, and it depends only on whether $y$ lies in $N^+[x]$. The row class of a vertex $x$ lies inside $N^+[x] \cap N^-[x]$ and does not fill it, so it is small: $a \le \lambda + 1$ (Lemma 6). Our survey [4, Theorem 10(a)], applied to the complement of the graph, gives this bound as well. A vertex outside the class sees at most $\mu$ vertices of it, and double counting of pairs gives $a(\lambda + 2 - a) \le \mu(K - a)$ (Proposition 8). Every vertex outside the class has arcs to at least $q$ vertices outside $N^+[x]$, and every vertex outside $N^+[x]$ receives exactly $\mu$ arcs from $N^+[x]$. Counting these arcs gives the lower bound $a \ge K - \mu f$ (Proposition 9). Comparing two neighbourhoods that contain a common vertex of the class gives the upper bound $a \le K - q$ (Proposition 10); Lemma 9 of [7] gives this bound as well. Together the two bounds require $q \le \mu f$, which is inequality (1).

When $\mu = 1$, the classes are much more rigid: two distinct vertices are never twins by row and by column at the same time, and $a + d \le \lambda + 3$ (Lemma 12). When $k = 2\lambda + 2$, the rank of $B$ is $k + 2$, exactly one more than the number of rows of $N^+[x]$. For a vertex without a row twin, the rows of $N^+[x]$ are independent, and outside $N^+[x]$ the rows of $B$ reduce to a single vector modulo their span. Hence such a vertex has a rigid structure: its second neighbourhood splits into blocks, and the sizes of the blocks agree only when $\lambda \le 2$ (Theorem 14). When $\lambda \ge 4$, the twin classes must be pairs, while $N^+[x]$ consists of an odd number $2\lambda + 3$ of vertices and cannot be split into pairs (Theorem 15).

The set $(28, 6, 3, 2, 1)$ also has $k = 2\lambda + 2$, but $\lambda = 2$, and Theorem 14 does not exclude a vertex without a twin. Theorem 4 splits the graphs into three cases (Section 6). A vertex without a row twin is excluded by a SAT solver: the formula that a graph with such a vertex would satisfy is unsatisfiable, and the proof of unsatisfiability is accepted by two checkers. A vertex without a column twin is a vertex without a row twin in the graph with matrix $A^\top$. If every vertex has twins, then a class of $\lambda + 1$ vertices is impossible, all classes are pairs, and $N^+[x]$ of $K = 7$ vertices again cannot be split into pairs (Lemma 16).

**Contributions.**

1. Theorem 3 and the bounds on classes for any $\mu$ (Section 4). Both upper bounds on a class are known: $a \le \lambda + 1$ of Lemma 6 follows from our survey [4, Theorem 10(a)] applied to the complement, and $a \le K - q$ is a special case of Lemma 9 of [7], which Proposition 10 only proves differently. The contribution of the paper here is Lemma 7, the double counting of Proposition 8, the lower bound of Proposition 9 and inequality (1), which follows from the lower and upper bounds as a condition on the parameters: the works [4] and [7] do not contain them, and we have not found them in the literature we examined (Section 2). Inequality (1) is invariant under blow-up by cliques, that is, under the passage to the graph with matrix $(A + I) \otimes J_m - I$ (Section 4), so every set it excludes excludes its whole line of blow-ups. In the table [2] it excludes six sets: one open set, $(96, 15, 10, 9, 1)$, and five sets marked as nonexistent, among them the two other sets of Theorem 2. None of them is constructed, and equality in (1) holds exactly for thirteen constructed sets $(8m, 4m - 1, 3m - 1, 3m - 2, m)$, $m = 1, \dots, 13$.
2. Theorem 14 on a vertex without a twin and Theorem 15 on the family $\mu = 1$, $t = \lambda + 1$, $k = 2\lambda + 2$, $\lambda \ge 4$ (Section 5). They close two open sets of the table, Theorem 1.
3. Theorem 4 and Lemma 16 (Section 6). Lemma 16 forbids a class of $\lambda + 1$ vertices in a graph where every vertex has twins and $K > 2(\lambda + 1)$; when $\lambda = 2$, all classes of such a graph are pairs. Hence Theorem 4 needs a solver search only for a vertex without a twin, and the solver proves the unsatisfiability of its formula in less than a second.
4. Sharpness (Section 7). The flag graph of a generalized quadrangle of order $(\sigma, \tau)$ is a known DSRG [23]; it turns into equalities the bound $a + d \le \lambda + 3$ and the double counting of Proposition 8. The quadrangle $W(2)$ gives a constructed DSRG $(45, 8, 4, 3, 1)$ with $k = 2\lambda + 2$ and $\lambda = 3$, so the threshold $\lambda \ge 4$ of Theorem 15 cannot be lowered.
5. A formalization in Lean 4 with the Mathlib library (Section 8). All five nonexistence results of Theorems 1 and 2 are proved together with the complements for any matrix, without hypotheses; inequality (1) is proved for any DSRG matrix with $t = \lambda + 1$ and $\mu < \lambda + 2$, and Lemma 16 for any DSRG matrix with $\mu = 1$ and $t = \lambda + 1$. Lean reduces Theorem 4 to one statement: a DSRG $(28, 6, 3, 2, 1)$ has no vertex without a row twin. That statement rests on a certificate of unsatisfiability, not on Lean. The remark on sharpness is not written in Lean either.

**What is taken from earlier work.** The spectrum of a DSRG, the multiplicity formulas and the decomposition of $\mathbb R^v$ into eigenspaces are known since the work of Duval [1]; Lemma 5 states the consequences we need, with a proof. The bound $a \le K - q$ of Proposition 10 is a special case of Lemma 9 of [7]: the hypotheses of that lemma hold for $B = A + I$ when $t = \lambda + 1$, and Proposition 10 is another proof of a known bound. The rows of $B$ of two vertices are equal exactly when their rows in the matrix $J - I - A$ of the complement are equal, so a row class is a class of vertices with the same out-neighbourhood in the complement. The bound $a \le \lambda + 1$ of Lemma 6 is the bound of our survey [4, Theorem 10(a)] for the complement, and its case for $(28, 6, 3, 2, 1)$ is Lemma 2 of [8]. The comparison with these works is in Section 2. The table [2] attributes the flag graph of a generalized quadrangle as a DSRG to [23], and the flag graph of a partial geometry to [24]; we have not read these works, and Proposition 17 proves the special case we need anew, for the sake of the class sizes. The sets of Theorem 2 and the set of Theorem 4 were closed on the platform by other methods before us; this comparison is in Section 2. The other statements are proved here.

## 2. Related work

The definition of a DSRG and the basic necessary conditions for existence are due to Duval [1]. The table [2] collects the sets with $v \le 110$ and the conditions by which some of them are excluded. Our survey of the problem [4] collected the claims of 38 papers of the platform about the sets of the table; we refer to it when we say what is claimed on the platform.

**Twins.** Classes of vertices with the same row of the adjacency matrix have already been used by papers of the platform. Our survey proves in general form [4, Theorem 10]: in any DSRG a class of vertices with the same out-neighbourhood contains at most $v - 2k + \mu - 1$ vertices, and when $t = \mu$ the number of such classes is at least the rank of $A$, because the spectrum of the quotient by the classes yields it. According to the survey, the reductions of the searches in [8] and [9] rest on these arguments. The rows of $B = A + I$ of two vertices are equal exactly when their rows in the matrix $J - I - A$ of the complement are equal, and the complement of a graph with $t = \lambda + 1$ has $t = \mu$. Hence the row classes of this paper are the classes of equal out-neighbourhoods of the complement, and for the parameters of the complement the bound [4, Theorem 10(a)] equals $v - 2(v - k - 1) + (v - 2k + \lambda) - 1 = \lambda + 1$, that is, it coincides with the bound of Lemma 6. For order $28m$, the paper [8] already counts the rows of $B = A + I$ (Lemma 2 of [8] and its Section 7, see below). Our Sections 4–6 rest on the fact that when $t = \lambda + 1$ the matrix $B$ satisfies a quadratic equation without the term $I$.

**The bound on equal rows.** Lemma 9 of [7] states the following. Let $B$ be a 0/1 matrix with ones on the diagonal and $K$ ones in every row and every column, and let $B^2 = \alpha J + qB$ with $\alpha + q < K$. Then rows of $B$ that are equal to each other and whose indices lie in the support of one column occupy at most $K - q$ rows. For $B = A + I$ with $t = \lambda + 1$ the hypotheses hold: by Lemma 5, $B^2 = qB + \mu J$, that is, $\alpha = \mu$, and $\alpha + q = \lambda + 2 < K$ is equivalent to $t < k$. The row class $C_x$ lies in the support of column $x$ (Lemma 6), so Lemma 9 of [7] gives $a \le K - q$. This is exactly the conclusion of Proposition 10, and Proposition 10 is another proof of an already known bound. The argument of [7] goes through columns: a column with more than $K - q$ ones in the support $W$ of another column coincides with the indicator of $W$, and then all out-neighbours of a vertex of the class lie in $W$, which contradicts the count of $B\mathbf 1_W$. Our argument compares two closed neighbourhoods with a common vertex of the class and on the way gives the inequality $a - \gamma_u \le k - \lambda - 1$ for every vertex $u \in U$ that sees the class. We have read the proof of Lemma 9 of [7] and found no gap in it. The lower bound of Proposition 9 and inequality (1) are not in [7]. Theorem 10 of [7] excludes the line $(96m, 80m, 75m, 65m, 75m)$ and the complements $(96m, 16m - 1, 11m - 1, 11m - 2, m)$ by a search over normals of a nonnegative basis of columns of rank 9, and the cases with large classes of equal rows in this search are closed by Lemma 9 of [7]. The line $(96m, 16m - 1, 11m - 1, 11m - 2, m)$ is also excluded by inequality (1).

Lemma 2 of [8] states for a DSRG $(28, 6, 3, 2, 1)$ that at most three rows of $B = A + I$ coincide, and at most three columns. This is the case of order 28 of the bound [4, Theorem 10(a)] for the complement, that is, of our Lemma 6 with $\lambda = 2$, where $a \le \lambda + 1 = 3$; for columns it is the same lemma for $A^\top$. The argument of [8] is the same: the class lies in the support of a column, and the count is made first at a vertex of the class and then at a vertex of the support outside the class. In Section 7 of [8] the same argument gives the bound $4m - 1 = \lambda + 1$ for the line $(28m, 7m - 1, 4m - 1, 4m - 2, m)$, and this is again the same bound; the survey [4] notes this.

**The sets of Theorem 2.** The set $(96, 15, 10, 9, 1)$ is open in the table [2], and $(40, 9, 6, 5, 1)$ and $(80, 19, 13, 12, 2)$ are marked in it as nonexistent by a condition from [5]; all three sets were closed on the platform earlier by other methods. The nonexistence of the complements $(40, 30, 27, 21, 27)$ and $(80, 60, 54, 42, 54)$, and with them of the whole line $(40m, 30m, 27m, 21m, 27m)$, is derived in [5] by a search over hyperplanes of rank 6 with Farkas certificates; our survey repeated the search with its own program [4]. The paper [6] formalizes in Lean the rank 6 search for some of the ratios $v/k$, but, according to our survey, not for the ratio $4/3$ of this line [4]. The line $(96m, 80m, 75m, 65m, 75m)$ is closed by [7], as said above. Our proof is not needed to close these three sets, but it is different: two lines of double counting instead of a search, and it is checked in Lean in full.

**The set of Theorem 4.** The set $(28, 6, 3, 2, 1)$ is open in the table [2], but our survey [4] counts it as closed by [8]. That paper claims that there are no graphs of the line $(28m, 21m, 18m, 15m, 18m)$ for any odd $m$, and hence none of their complements $(28m, 7m - 1, 4m - 1, 4m - 2, m)$; for $m = 1$ this is our set. We have read the part of [8] on order 28. There too $B = A + I$, $B^2 = 3B + J$, and the rank of $B$ is 8. A nonnegative basis of eight columns of $B$ defines a normal, and Lemma 2 of [8] together with the mean weight of a row of the basis leaves three normals. Two of them are excluded by small exact searches, a basis exchange and a separating inequality with integer coefficients, and the third, with four cells of seven vertices each, by a SAT formula with a DRAT proof accepted by drat-trim. We have not repeated the computational steps of [8], and Theorem 4 does not rely on that work. Our proof is different: a solver search is needed only for a graph with a vertex without a twin, and a graph in which every vertex has twins is excluded by the parity of $K$, proved in Lean. By the enumeration of vertex-transitive DSRGs with $v \le 39$ in [26], this set has no vertex-transitive graphs.

**The sets of Theorem 1.** About the sets $(66, 10, 5, 4, 1)$ and $(91, 12, 6, 5, 1)$, the papers and the discussion of the problem on the platform, as of 1 November 2026, claim only the exclusion of particular classes of graphs (Table 2). None of the papers and none of the messages of the discussion that we read as of that date claims that there are no graphs with these parameters at all. Theorem 1 neither uses nor checks these claims.

**Table 2.** What is claimed on the platform about the sets of Theorem 1 and their complements, as of 1 November 2026. The claims are summarized; we have not checked them.

| Set | Claimed exclusions of classes |
|---|---|
| $(66, 10, 5, 4, 1)$ | no realization by two orbits of an abelian group of order 33 [10], [11], repeated by the survey [4]; for the complement $(66, 55, 50, 45, 50)$, a construction by external products of one kind is excluded [12] — a way of construction, not a graph |
| $(91, 12, 6, 5, 1)$ | no exclusions; the set appears only in a census of parameter sets by the pair of eigenvalues $(5, -1)$ [13] |

**Other local conditions.** Hobart and Williford [27] derive two conditions. The size of an independent set is at most the multiplicity of one nontrivial eigenvalue if the other one is nonzero [27, Theorem 3]; if the multiplicity of one of them is less than $k$, the other is an eigenvalue of the subgraph on the out-neighbours of a vertex [27, Theorem 6], and then its absolute value is at most $\lambda$ [27, Corollary 7]. On the parameters they yield the conditions [27, Corollaries 4, 5 and 7], the first two for $\lambda = 0$ and $\lambda = 1$; in the table [2] these are the conditions N10 and N11. They do not concern classes of equal rows. Inequality (1) does not follow from the conditions of [27] on the parameters: the six sets it excludes and their complements have $\lambda \ge 5$, so the conditions [27, Corollaries 4 and 5] do not apply to them, and the condition [27, Corollary 7] holds. The sets of Theorems 1 and 4 together with their complements satisfy these conditions as well. Our paper [28] compares the rank of $A - \theta I$ with the submatrix on the neighbourhood of a vertex when $\lambda \in \{0, 1\}$; its arguments rest on other local structures, the determinant on the closed neighbourhood and the left kernel on the rows of a vertex and its out-neighbours, and do not apply to the sets of this paper, where $\lambda \ge 2$.

The works [7] and [8] also use the rank of $A + I$ and the bound on classes of equal rows, but as a step of a search over normals of a basis of columns. The survey [4, Theorem 10(b)] compares, for $t = \mu$, the number of classes of equal rows with the rank; through the complement these are the classes of rows of $B$, and the rank of the matrix of the complement equals the rank of $B$. Lemma 6 of [8] applies the same argument: the spectrum of the quotient by the classes of rows of $J - B$ gives, on the line $(28m, 7m - 1, 4m - 1, 4m - 2, m)$ with odd $m$, at least ten distinct rows and ten distinct columns of $B$. We have found neither the structure of a vertex without a row twin through the rank $k + 2$ and blocks, as in Theorem 14, nor the conclusion that all classes are pairs when $k = 2\lambda + 2$, in these works, in the table [2] or in the works [27] and [28]. Of the wider literature, we looked only through the abstracts of the arXiv papers on DSRGs as of 1 November 2026; there is no such argument in them. We did not meet inequality (1) there as a condition on parameters either.

## 3. The matrix B = A + I

**Lemma 5.** Let $t = \lambda + 1$ and $B = A + I$. Then:

1. $B^2 = qB + \mu J$, and for any vertices $x$, $y$ the number $|N^+[x] \cap N^-[y]|$ equals $q + \mu = \lambda + 2$ if $y \in N^+[x]$, and $\mu$ otherwise; moreover, $K^2 = qK + \mu v$;
2. if $q > 0$, then the nontrivial eigenvalues of $A$ are $q - 1$ with multiplicity $f$ and $-1$ with multiplicity $g$, where $qf = v - K$ and $\operatorname{rank} B = 1 + f$;
3. if $\mu = 1$, then $v = (k + 1)(k - \lambda)$ and $(\lambda + 1)f = v - K$; in particular, $f = K$ if and only if $k = 2\lambda + 2$.

*Proof.* 1. $B^2 = A^2 + 2A + I = (t + 1 - \mu)I + (\lambda + 2 - \mu)A + \mu J$, and when $t = \lambda + 1$ this is $q(A + I) + \mu J$. The entry $(x, y)$ of $B^2$ equals $\sum_z B(x, z)B(z, y) = |N^+[x] \cap N^-[y]|$, and the entry of the right-hand side is $q[y \in N^+[x]] + \mu$. Row sums give $K^2 = qK + \mu v$.

2. The nontrivial eigenvalues of a DSRG are the roots of the polynomial $x^2 - (\lambda - \mu)x - (t - \mu)$ [1], and when $t = \lambda + 1$ it equals $(x + 1)(x - (q - 1))$. When $q > 0$, the roots are distinct. From $\mathbf 1^\top A = k\mathbf 1^\top$ it follows that $A$ maps $\mathbf 1^\perp$ into itself, and by item 1, $(A + I)(A - (q - 1)I) = 0$ holds on $\mathbf 1^\perp$. Hence $A$ is diagonalizable on $\mathbf 1^\perp$, and $\mathbf 1^\perp$ is the sum of the eigenspaces for $-1$ and $q - 1$, of dimensions $g$ and $f$. On the vector $\mathbf 1$ the matrix $A + I$ acts as multiplication by $K \ne 0$, and on the second eigenspace as multiplication by $q \ne 0$, so $\operatorname{rank}(A + I) = v - g = 1 + f$. The dimension of $\mathbf 1^\perp$ and the zero trace of $A$ give $f + g = v - 1$ and $k + f(q - 1) - g = 0$, whence $qf = v - 1 - k$.

3. When $\mu = 1$, the equation $K^2 = (\lambda + 1)K + v$ of item 1 gives $v = K(K - \lambda - 1) = (k + 1)(k - \lambda)$, and item 2 gives $(\lambda + 1)f = v - K = K(k - \lambda - 1)$. Hence $f = K$ exactly when $k - \lambda - 1 = \lambda + 1$. $\square$

The hypothesis $q > 0$ is needed by item 2 and by Theorem 3. We do not treat the case $q \le 0$: for all 700 sets of the table [2] with $t = \lambda + 1$ the number $q$ is positive, and $f$ is an integer.

## 4. Row classes for any μ

In this section $t = \lambda + 1$. Fix a vertex $x$ and put $C = C_x$, $a = |C|$, $U = N^+[x] \setminus C$. For a vertex $u$, the number $\gamma_u = |N^+[u] \cap C|$ is how many vertices of the class $u$ sees in its closed neighbourhood.

**Lemma 6.** $C \subseteq N^+[x] \cap N^-[x]$, the set $U$ is not empty, and $a \le \lambda + 1$. Moreover, $C \subseteq N^-[z]$ for every $z \in N^+[x]$.

*Proof.* If $y \in C$, then $y \in N^+[y] = N^+[x]$ and $x \in N^+[x] = N^+[y]$, that is, $y \in N^-[x]$. If $z \in N^+[x]$, then $z \in N^+[y]$ for every $y \in C$, that is, $C \subseteq N^-[z]$. If $U$ were empty, we would get $N^+[x] = C \subseteq N^-[x]$ and $K = |N^+[x] \cap N^-[x]| = \lambda + 2 = t + 1$ by Lemma 5, that is, $k = t$, contrary to $t < k$. For $z \in U$ the set $C \cup \{z\}$ lies in $N^+[x] \cap N^-[z]$, which has exactly $\lambda + 2$ vertices by Lemma 5, so $a + 1 \le \lambda + 2$. $\square$

The bound $a \le \lambda + 1$ is the bound of our survey [4, Theorem 10(a)] applied to the complement: a row class is a class of equal out-neighbourhoods of the graph with matrix $J - I - A$, and for its parameters the bound of the survey equals $\lambda + 1$ (Section 2). The proof in [4] is the same count, written for the complement. We give it in terms of $B$ because the inclusions $C \subseteq N^+[x] \cap N^-[x]$ and $C \subseteq N^-[z]$ are needed by Lemma 7, Propositions 8–10 and Lemma 16. For the set $(28, 6, 3, 2, 1)$, the bound $a \le 3$ together with the same bound for columns is Lemma 2 of [8] (Section 2).

**Lemma 7.** If $u \notin C$, then $\gamma_u \le \mu$.

*Proof.* The rows $u$ and $x$ of $B$ are different and each contains $K$ ones, so there is $w \in N^+[x] \setminus N^+[u]$. By Lemma 6, $C \subseteq N^-[w]$, hence $N^+[u] \cap C \subseteq N^+[u] \cap N^-[w]$, and the last set has exactly $\mu$ vertices by Lemma 5. $\square$

**Proposition 8.** $\sum_{u \in U} \gamma_u = a(\lambda + 2 - a)$, and therefore $a(\lambda + 2 - a) \le \mu(K - a)$. When $\mu = 1$, this inequality is equivalent to $a(\lambda + 3 - a) \le K$.

*Proof.* Count the pairs $(y, u)$ with $y \in C$, $u \in U$ and $y \in N^+[u]$. For $y \in C$ the set $N^+[x] \cap N^-[y]$ consists of $\lambda + 2$ vertices and contains the whole class by Lemma 6, so the other $\lambda + 2 - a$ vertices lie in $U$; there are $a(\lambda + 2 - a)$ pairs. Counting by $u$, there are $\sum_{u \in U}\gamma_u$ pairs, and by Lemma 7 this is at most $\mu|U| = \mu(K - a)$. $\square$

**Proposition 9.** If $u \notin C$, then $|N^+[u] \setminus N^+[x]| \ge q$. Hence $q(K - a) \le \mu(v - K)$, and when $q > 0$, $a \ge K - \mu f$.

*Proof.* There is $w \in N^+[u] \setminus N^+[x]$. By Lemma 5, $N^+[u] \cap N^-[w]$ has exactly $\lambda + 2$ vertices and $N^+[x] \cap N^-[w]$ exactly $\mu$, so at least $q$ vertices of the first set lie outside $N^+[x]$. Count the pairs $(u, w)$ with $u \in U$ and $w \in N^+[u] \setminus N^+[x]$: there are at least $q|U|$ of them. On the other hand, every $w \notin N^+[x]$ receives exactly $\mu$ arcs from $N^+[x]$, and none of them comes from the class: $w \in N^+[y]$ with $y \in C$ would mean $w \in N^+[x]$. Hence there are at most $\mu(v - K)$ pairs. By Lemma 5, $\mu(v - K) = q\mu f$, and when $q > 0$ we can divide by $q$. $\square$

**Proposition 10.** If $u \in U$ and $\gamma_u \ge 1$, then $a - \gamma_u \le k - \lambda - 1$. Such a vertex $u$ exists, so $a \le k - \lambda - 1 + \mu = K - q$.

*Proof.* Take $c \in C \cap N^+[u]$. The vertex $c$ lies both in $N^+[u]$ and in $N^+[x]$, so by Lemma 5, $|N^+[u] \cap N^-[c]| = |N^+[x] \cap N^-[c]| = \lambda + 2$. Remove from both sets their common part $N^+[u] \cap N^+[x] \cap N^-[c]$:

$$
|(N^+[u] \setminus N^+[x]) \cap N^-[c]| = |(N^+[x] \setminus N^+[u]) \cap N^-[c]|.
$$

The right-hand side contains $C \setminus N^+[u]$, because $C \subseteq N^-[c]$ by Lemma 6, and is therefore at least $a - \gamma_u$. The left-hand side lies in $N^-[c] \setminus N^+[x]$, which has $K - (\lambda + 2) = k - \lambda - 1$ vertices. The required $u$ exists: $N^+[x] \cap N^-[x]$ has exactly $\lambda + 2$ vertices, the class takes at most $\lambda + 1$ of them, and any remaining vertex lies in $U$ and has an arc to $x \in C$. By Lemma 7, $\gamma_u \le \mu$. $\square$

The conclusion $a \le K - q$ is a special case of Lemma 9 of [7]: the class $C$ lies in the support of column $x$, and the hypotheses of that lemma hold when $t = \lambda + 1$ (Section 2). Proposition 10 proves the same bound in another way and also gives the inequality $a - \gamma_u \le k - \lambda - 1$ for every vertex $u \in U$ with $\gamma_u \ge 1$.

*Proof of Theorem 3.* For any vertex, Propositions 9 and 10 give $K - \mu f \le a \le K - q$, whence $q \le \mu f$. Multiplying by $q > 0$, we get $q^2 \le \mu qf = \mu(v - K)$ by Lemma 5. $\square$

*Proof of Theorem 2.* For $(80, 19, 13, 12, 2)$ we have $K = 20$, $q = 12$, $v - K = 60$ and $f = 5$: Proposition 9 gives $12(20 - a) \le 120$, that is, $a \ge 10$, while Proposition 10 gives $a \le 8$. For $(40, 9, 6, 5, 1)$ we have $q = 6$, $f = 5$, and $a \ge 10 - 5 = 5 > 4 = K - q$. For $(96, 15, 10, 9, 1)$ we have $q = 10$, $f = 8$, and $a \ge 16 - 8 = 8 > 6$. A graph exists if and only if its complement exists, so there are no complements either. $\square$

For $(40, 9, 6, 5, 1)$ and $(96, 15, 10, 9, 1)$, Proposition 8 alone together with the lower bound is also enough: for the first, $a \in \{5, 6\}$ gives $a(8 - a) \in \{15, 12\}$, more than $K = 10$; for the second, $a \in \{8, 9, 10\}$ gives $a(12 - a) \in \{32, 27, 20\}$, more than $16$. This is how these two sets are proved in Lean (Section 8), with the lower bound coming from the rank (Proposition 13).

**Lines of blow-ups.** Blow-up by cliques takes a DSRG with $t = \lambda + 1$ to the graph with matrix $(A + I) \otimes J_m - I$ and parameters $(mv, mK - 1, m(\lambda + 2) - 1, m(\lambda + 2) - 2, m\mu)$. Indeed, $B' = B \otimes J_m$ has unit diagonal, row and column sums $mK$ and $B'^2 = m(B^2 \otimes J_m) = mqB' + m\mu J$; expanding $B'^2 = (A' + I)^2$ with $A' = B' - I$, we get the defining equation of a DSRG with these parameters. At the level of parameters, $K$, $q$, $\mu$ and $v$ are multiplied by $m$, and $f$ does not change. Hence the equation $K^2 = qK + \mu v$ of Lemma 5, the integrality of $f$ and inequality (1) are the same at all points of a line as at its start. If (1) excludes a set, it excludes its whole line; the nonexistence of the far points does not follow by itself from the nonexistence of the start, because a graph at a far point need not be a blow-up. For example, (1) excludes $(96m, 16m - 1, 11m - 1, 11m - 2, m)$ for every $m$: $q = 10m > 8m = \mu f$.

**Corollary 11.** Of the 700 sets of the table [2] with $t = \lambda + 1$, inequality (1) excludes exactly six: the open set $(96, 15, 10, 9, 1)$ and the sets $(40, 9, 6, 5, 1)$, $(48, 17, 12, 11, 3)$, $(80, 19, 13, 12, 2)$, $(80, 23, 16, 15, 3)$ and $(96, 35, 25, 24, 6)$ marked as nonexistent. The six sets lie on four lines of blow-ups: $(80, 19, 13, 12, 2)$ is the point $m = 2$ of the line of $(40, 9, 6, 5, 1)$, and $(96, 35, 25, 24, 6)$ is the point $m = 2$ of the line of $(48, 17, 12, 11, 3)$. Lemmas 6, 7 and Propositions 8–10 together exclude the same six sets. Equality in (1) holds for exactly thirteen sets of the table, $(8m, 4m - 1, 3m - 1, 3m - 2, m)$ with $m = 1, \dots, 13$; all of them are constructed.

This is a count over the table, not a proof; the program that repeats it is named in Section 10.

## 5. Classes when μ = 1 and a vertex without a twin

In this section $\mu = 1$ and $t = \lambda + 1$, so $q = \lambda + 1$ and $B^2 = (\lambda + 1)B + J$.

**Lemma 12.** When $\mu = 1$:

1. $N^+[x]$ is a union of column classes, and $N^-[y]$ is a union of row classes;
2. $|C_x \cap D_x| = 1$: two distinct vertices are never twins by row and by column at the same time;
3. $C_x \cup D_x \subseteq N^+[x] \cap N^-[x]$ and $a + d \le \lambda + 3$.

*Proof.* 1. Let $y \in N^+[x]$ and let $y'$ be a column twin of $y$. Then $x \in N^-[y] = N^-[y']$, that is, $y' \in N^+[x]$. The second half is symmetric.

2. Let $z_0 \ne z_1$ be twins both by row and by column. For any $x \in N^-[z_0]$ and $y \in N^+[z_0]$, both vertices $z_0$ and $z_1$ lie in $N^+[x] \cap N^-[y]$. By Lemma 5, an intersection of two or more vertices occurs only when $y \in N^+[x]$. Hence $N^+[z_0] \subseteq N^+[x]$, and since the sizes are equal, $N^+[x] = N^+[z_0]$, that is, every $x \in N^-[z_0]$ lies in $C_{z_0}$. Then $N^-[z_0] \subseteq C_{z_0} \subseteq N^+[z_0]$ by Lemma 6 and $|N^+[z_0] \cap N^-[z_0]| = K$, while by Lemma 5 this is $\lambda + 2 = t + 1 < K$.

3. For $C_x$ this is Lemma 6, and for $D_x$ it is the same lemma for $A^\top$: the transposed matrix defines a DSRG with the same parameters, and its row twins are the column twins of $A$. By Lemma 5, $N^+[x] \cap N^-[x]$ has exactly $\lambda + 2$ vertices, and by item 2, $C_x \cap D_x = \{x\}$, so $a + d - 1 \le \lambda + 2$. $\square$

Everything said in Section 4 about row classes holds for column classes as well: it is enough to pass to $A^\top$. When $\mu = 1$, Propositions 8 and 9 give $a(\lambda + 3 - a) \le K$ and $a \ge K - f$, and the same for $d$. The lower bound can also be obtained from the rank, and this is how it is proved in Lean.

**Proposition 13.** When $\mu = 1$, the rows of $B$ indexed by $\{x\} \cup (N^+[x] \setminus C_x)$ are linearly independent. Therefore $\operatorname{rank} B \ge K + 1 - a$ and $a \ge K - f$.

*Proof.* Let $O = \Gamma^+(x)$; then $C_x \setminus \{x\} \subseteq O$. Every $o \in O \setminus C_x$ has some $w_o \in N^+[o] \setminus N^+[x]$. By Lemma 5, $|N^+[x] \cap N^-[w_o]| = 1$, and this single vertex is $o$. Hence among the rows $\{x\} \cup (O \setminus C_x)$, the column $w_o$ has a one only in the row $o$; in particular, all $w_o$ are distinct. The row $x$ has a one in the column $x$ and zeros in the columns $w_o$. The submatrix of $B$ on these rows and on the columns $\{x\} \cup \{w_o\}$ is triangular with ones on the diagonal after a permutation. It has $1 + k - (a - 1) = K + 1 - a$ rows, and by Lemma 5, $\operatorname{rank} B = 1 + f$. $\square$

**Theorem 14.** Let $\mu = 1$, $t = \lambda + 1$ and $k = 2\lambda + 2$, that is, $f = K$. If a vertex $x$ has no row twin, then $\lambda \le 2$. Hence, when $\lambda \ge 3$, every vertex has both a row twin and a column twin.

*Proof.* Let $x$ have no row twin, $O = \Gamma^+(x)$, $S = N^+[x]$ and $W = V \setminus S$. By Lemma 5, $|W| = v - K = K(k - \lambda - 1) = K(\lambda + 1)$.

*Blocks.* By Lemma 5, every $w \in W$ has exactly one in-neighbour in $S$, and it is not $x$. Hence $W$ splits into the blocks $W_o = \Gamma^+(o) \cap W$, $o \in O$. An empty block $W_o$ would give $N^+[o] \subseteq S$, that is, $N^+[o] = S$ since the sizes are equal, while $x$ has no twins; hence all blocks are nonempty. The entries $(o, w)$ of the equation $B^2 = (\lambda + 1)B + J$ give two more counts:

- (i) a vertex $w \in W_o$ receives exactly $\lambda$ arcs from $W_o$: $N^+[o] \cap N^-[w]$ has exactly $\lambda + 2$ vertices, of which only $o$ lies in $S$, and the others are $w$ and its in-neighbours in $W_o$;
- (ii) a vertex $w \in W_{o'}$ with $o' \ne o$ receives exactly $1 - [o \to o']$ arcs from $W_o$: $w \notin N^+[o]$, so $N^+[o] \cap N^-[w]$ has one vertex, and the only vertex of $S$ in $N^-[w]$ is $o'$.

*Rank.* On the columns $W$, the row $o$ of $B$ is the indicator $\mathbf 1_{W_o}$, and the row $x$ is zero. The blocks are nonempty and disjoint, so the rows $O$ are already independent on the columns $W$; the row $x$ is zero on these columns but is not zero itself, and therefore does not lie in the span of the rows $O$. Hence the rows $S$ are independent, and their span $R_S$ has dimension $K = k + 1$. Denote the row $w$ of $B$ by $B[w]$. The rank of $B$ is $1 + f = k + 2$, so there is a vector $z$ such that $B[w] = s_w + c_w z$ with $s_w \in R_S$ for every vertex $w$, where $c_w = 0$ for $w \in S$. The row $x$ of the equation $B^2 = (\lambda + 1)B + J$ gives $\mathbf 1^\top = \sum_{o \in O} B[o] - \lambda B[x] \in R_S$. The row $u$ of the same equation modulo $R_S$ gives $\sum_y B(u, y)c_y = (\lambda + 1)c_u$, that is, $Bc = (\lambda + 1)c$. The vector $c$ is not zero, otherwise the rank would be $k + 1$, and the row $o$ gives $\sum_{w \in W_o} c_w = 0$.

*Structure of the rows.* Let $r_w = N^+[w] \cap W$; $w \in r_w$. On the columns $W$ the vector $s_w$ is constant on every block, so $\mathbf 1_{r_w} - c_w z$ is also constant on every block. If $z$ is constant on all blocks, then every $r_w$ is a union of blocks, every block is a reciprocal clique, by (i) $|W_o| = \lambda + 1$, and $|W| = k(\lambda + 1)$, contrary to $|W| = (k + 1)(\lambda + 1)$. The blocks on which $z$ is not constant are called special. Normalize $z$ so that $c_{w_0} = 1$ for some vertex $w_0$, and put $T_o = r_{w_0} \cap W_o$ for a special $o$; then $\emptyset \ne T_o \ne W_o$. On a special block, $\mathbf 1_{r_w \cap W_o}$ differs from $c_w\mathbf 1_{T_o}$ by a constant. The spread, that is, the largest value minus the smallest, of the left vector is 0 or 1, and that of the right vector is $|c_w|$. Hence $c_w \in \{0, \pm 1\}$; when $c_w = 1$ we get $r_w \cap W_o = T_o$, when $c_w = -1$ we get $W_o \setminus T_o$, and when $c_w = 0$ the set $r_w \cap W_o$ is empty or equal to $W_o$. On the non-special blocks, $r_w \cap W_o$ is also empty or equal to $W_o$. Let $P$, $M$ and $Z$ be the vertices of $W$ with $c_w = 1$, $-1$ and $0$, and $p_o = |P \cap W_o|$. The sums of $c$ over the blocks are zero, so $|M \cap W_o| = p_o$.

*Sizes of the blocks.* A non-special block is a reciprocal clique, and by (i) $|W_o| = \lambda + 1$. In a special block, a vertex $y \in T_o$ lies in $P$ or in $Z$: a vertex $w \in M \cap W_o$ lies in its own $r_w \cap W_o = W_o \setminus T_o$, that is, outside $T_o$. The arcs into $y$ come exactly from the other vertices of $P \cap W_o$ and of $Z \cap W_o$; a vertex of $Z$ has arcs to its whole block, because $w \in r_w$. By (i), $p_o + |Z \cap W_o| - 1 = \lambda$, that is, $|W_o| = \lambda + 1 + p_o$. Summing over the blocks gives $|W| = k(\lambda + 1) + \sum p_o$, whence the sum of $p_o$ over the special blocks is $\lambda + 1$, and $P$ and $M$ are nonempty.

*Two or more special blocks.* Two vertices of $P$ in one block $W_{o_2}$ both have arcs to the whole $T_{o_1}$ of another special block, while by (ii) a vertex of $T_{o_1}$ receives at most one arc from $W_{o_2}$. Hence all $p_o \le 1$, and at least $\lambda + 1$ special blocks have size $\lambda + 2$. For $w \in P$ the set $r_w$ contains all $T_o$, for $w' \in M$ the set $r_{w'}$ contains all $W_o \setminus T_o$, and both sets have at most $K$ elements. Hence $(\lambda + 1)(\lambda + 2) \le 2K = 2(2\lambda + 3)$, that is, $\lambda^2 - \lambda - 4 \le 0$ and $\lambda \le 2$.

*One special block $W_{o_1}$.* Then $p_{o_1} = \lambda + 1$ and $|W_{o_1}| = 2\lambda + 2 = k$, so $\Gamma^+(o_1) = W_{o_1}$ and $Z \cap W_{o_1}$ is empty. Inside the block, the vertices of $P \cap W_{o_1}$ have arcs exactly to $T_{o_1}$, the vertices of $M \cap W_{o_1}$ to the complement $W_{o_1} \setminus T_{o_1}$, and every vertex lies in its own part. Hence $\Gamma^+(o_1)$ consists of two reciprocal cliques of $\lambda + 1$ vertices each with no arcs between them. The vertex $o_1$ has no row twin: a twin would lie in $\Gamma^+(o_1)$ and have arcs to all its other vertices. When $\lambda \ge 3$, apply what has been proved to $o_1$ instead of $x$: two special blocks are impossible, so $o_1$ also has a single special block. Let it be given by a vertex $o_1' \in \Gamma^+(o_1)$; by the case just treated, $\Gamma^+(o_1')$ coincides with this block, that is, all out-neighbours of $o_1'$ lie outside $N^+[o_1]$. But $o_1'$ lies in a clique of $\lambda + 1 \ge 2$ vertices inside $\Gamma^+(o_1)$, a contradiction.

Thus, when $\lambda \ge 3$, every vertex has a row twin, and, by $A^\top$, a column twin as well. $\square$

![Three panels. In each, the vertex x is at the top, below it its out-neighbours o_1, o_2 and so on, and below each out-neighbour the frame of its block W_o with vertices coloured by the value c_w: blue for 1, orange for −1, grey for 0. Special blocks have a bold frame, the subset T_o inside a special block has a dashed one, and arcs are drawn inside the blocks, with no arcs between blocks. Panel a: the graph (6, 2, 1, 0, 1), one special block of two vertices. Panels b and c: the graph (15, 4, 2, 1, 1), two and three special blocks.](supplement/figure-1.png)

**Figure 1.** The structure from the proof of Theorem 14 at a vertex $x$ without a row twin, on actual graphs: (a) the DSRG $(6, 2, 1, 0, 1)$, $\lambda = 0$; (b) and (c) two vertices of the DSRG $(15, 4, 2, 1, 1)$, $\lambda = 1$. Below the out-neighbour $o_i$ of $x$ are the block $W_{o_i}$ and its size. The colour of a vertex $w$ is the value $c_w$: blue for 1, orange for $-1$, grey for 0. Special blocks have a bold frame, their subsets $T_o$ a dashed one; a line without an arrow is a pair of mutual arcs, and arcs between blocks are not drawn. A block is made special by the vector $z$, not by the values $c_w$ in it: for every vertex $w$ with $c_w = 1$, the set $r_w$ meets a special block exactly in $T_o$. A program of the supplement draws the figure from the graphs of the catalogue and checks the claims of the proof at these vertices.

What the figure shows. In panel (a) there is one special block, $W_{o_2}$: it has $2 = k$ vertices, which are all the out-neighbours of $o_2$, and the parts $T_{o_2}$ and $W_{o_2} \setminus T_{o_2}$ have $\lambda + 1 = 1$ vertex each, with $c = 1$ and $c = -1$; the non-special block $W_{o_1}$ is one vertex with $c = 0$. In panel (b) there are two special blocks, $W_{o_1}$ and $W_{o_2}$, of $\lambda + 2 = 3$ vertices each: each has one vertex with $c = 1$, one with $c = -1$ and one with $c = 0$, and with the sign of $z$ chosen in the figure, $T_o$ is the vertex with $c = 1$. With the opposite sign of $z$, the values of $c$ change sign, and $T_o$ turns into $W_o \setminus T_o$, the vertices with $c = 1$ and $c = 0$. The non-special blocks are mutual pairs with $c = 0$, and the sum of $p_o$ over the special blocks equals $2 = \lambda + 1$. In panel (c) there are three special blocks. The blocks $W_{o_1}$ and $W_{o_4}$ are built like the special blocks of panel (b), and $W_{o_3}$ has no vertices with $c = \pm 1$: $p_{o_3} = 0$ and $|W_{o_3}| = \lambda + 1$. This block is special although both its vertices have $c_w = 0$: the set $r_{w_0}$ of the blue vertex $w_0 \in W_{o_1}$ contains exactly one of its two vertices, and this vertex is $T_{o_3}$. The arc from $w_0$ to it goes between blocks, so the figure does not show it. In all panels $c$ takes only the values $0$ and $\pm 1$, the sum of $c$ over every block is zero, and $|W_o| = \lambda + 1 + p_o$.

**Theorem 15.** When $\mu = 1$, $t = \lambda + 1$, $k = 2\lambda + 2$ and $\lambda \ge 4$, there is no directed strongly regular graph.

*Proof.* By Theorem 14, $a, d \ge 2$ for every vertex. When $3 \le a \le \lambda$, we have $a(\lambda + 3 - a) \ge 3\lambda > 2\lambda + 3 = K$, so by Proposition 8 and Lemma 6, $a, d \in \{2, \lambda + 1\}$, and by item 3 of Lemma 12 they are not both equal to $\lambda + 1$.

Let $a = \lambda + 1$ for the class $C_x$. Then for every $y \in C_x$ the column class is a pair $D_y = \{y, y'\}$, where $y' \in N^+[x]$ by item 1 of Lemma 12 and $y' \notin C_x$ by item 2. The vertices $y'$ for different $y$ are different: if $y_1' = y_2'$, then $D_{y_1} = D_{y_2} \ni y_2$, and $y_2$ would be a twin of $y_1$ both by row and by column. The set $N^+[x] \setminus C_x$ has $K - a = \lambda + 2$ vertices in total, and one vertex $u^*$ falls into none of the classes $D_y$. By item 1 of Lemma 12, $D_{u^*} \subseteq N^+[x]$, and it is disjoint from the classes $D_y$, so $D_{u^*} = \{u^*\}$, contrary to $d \ge 2$. Hence all row classes, and by $A^\top$ all column classes, are pairs. By item 1 of Lemma 12, the set $N^+[x]$ is a union of disjoint column pairs, and the number of its vertices is even. But it has $2\lambda + 3$ vertices, a contradiction. $\square$

*Proof of Theorem 1.* For $(66, 10, 5, 4, 1)$ we have $k = 10 = 2\lambda + 2$ with $\lambda = 4$, and for $(91, 12, 6, 5, 1)$ we have $k = 12 = 2\lambda + 2$ with $\lambda = 5$. By Theorem 15 there are no graphs, and hence no complements. $\square$

For these two sets inequality (1) gives nothing: $q = 5 < \mu f = 11$ and $q = 6 < 13$. Without Theorem 14, the propositions of Section 4 leave the class sizes $a \in \{1, 2, 5\}$ for $(66, 10, 5, 4, 1)$ and $a \in \{1, 2, 6\}$ for $(91, 12, 6, 5, 1)$; Theorem 14 removes $a = 1$, and Theorem 15 the rest.

## 6. The set (28, 6, 3, 2, 1)

In this section $\mu = 1$ and $t = \lambda + 1$. A vertex without a row twin ($a = 1$) is called *row-free*, and one without a column twin ($d = 1$) *column-free*. For the set $(28, 6, 3, 2, 1)$ we have $k = 6 = 2\lambda + 2$ with $\lambda = 2$, $K = 7$, $f = 7$ and $B^2 = 3B + J$. Theorem 14 applies to it, but its conclusion $\lambda \le 2$ holds, and the theorem does not exclude a row-free vertex: with three special blocks the inequality of its proof is true, $(\lambda + 1)(\lambda + 2) = 12 \le 14 = 2K$. Sections 4 and 5 leave the class sizes $a \in \{1, 2, 3\}$. The proof of Theorem 4 splits the graphs into three cases: there is a row-free vertex; there is a column-free vertex; there are no free vertices. The third case is closed by Lemma 16, the first by the solver, and the second reduces to the first.

**Lemma 16.** Let $\mu = 1$, $t = \lambda + 1$ and $U = N^+[x] \setminus C_x$.

1. If $a = \lambda + 1$, then there are no arcs inside $U$, the column twins of the vertices of $U$ lie in $C_x$, and at least $K - 2(\lambda + 1)$ vertices of $U$ are column-free.
2. If there are no free vertices and $K > 2(\lambda + 1)$, then $a \le \lambda$ and $d \le \lambda$ for every vertex. When $\lambda = 2$, all row and column classes are pairs, and $K$ is even.

*Proof.* 1. Every $c \in C_x$ has arcs to all vertices of $N^+[x] \setminus \{c\}$, so $C_x \subseteq N^-[u]$ for every $u \in U$. By Lemma 5, $N^+[x] \cap N^-[u]$ has exactly $\lambda + 2$ vertices; these are the $\lambda + 1$ vertices of $C_x$ and $u$ itself, so there are no arcs from $U$ to $u$. By item 1 of Lemma 12, $D_u \subseteq N^+[x]$. If a column twin $u' \ne u$ lay in $U$, then $u \in N^-[u] = N^-[u']$ would give an arc $u \to u'$ inside $U$; hence $D_u \setminus \{u\} \subseteq C_x$. Two vertices of $U$ cannot both be column twins of one $c \in C_x$: otherwise they would be column twins of each other, which has just been excluded. Hence at most $|C_x| = \lambda + 1$ vertices of $U$ have $d \ge 2$, and at least $|U| - (\lambda + 1) = K - 2(\lambda + 1)$ are column-free.

2. By Lemma 6, $a \le \lambda + 1$. If $a = \lambda + 1$ held for some vertex $x$, then by item 1, $N^+[x]$ would contain $K - 2(\lambda + 1) > 0$ column-free vertices, contrary to the hypothesis. Hence $a \le \lambda$, and by $A^\top$ also $d \le \lambda$. When $\lambda = 2$, together with $a, d \ge 2$ this gives $a = d = 2$. By item 1 of Lemma 12, $N^+[x]$ is a union of column classes, all of them pairs, and $K = |N^+[x]|$ is even. $\square$

*Proof of Theorem 4.* Let $A$ be the matrix of a DSRG $(28, 6, 3, 2, 1)$.

*There is a row-free vertex $x$.* Renumber the vertices: $x$ gets the number 0, its three reciprocal neighbours get the numbers 1, 2, 3, its other three out-neighbours 4, 5, 6, the three vertices that have arcs to $x$ but receive no arc from $x$ get the numbers 7, 8, 9, and the other eighteen vertices the numbers 10–27. There are exactly three reciprocal neighbours because $A^2(x, x) = t = 3$, and $k - t = 3$ in-neighbours without a reverse arc. Such a graph satisfies a SAT formula $\Phi$. Its variables $a(i, j)$ with $i \ne j$ are the arcs of the graph, and its clauses require the following:

- every vertex has exactly 6 out-neighbours and 6 in-neighbours;
- there are exactly 3 paths $i \to z \to j$ when $i = j$, exactly 2 when $i \to j$ is an arc, and exactly 1 when it is not;
- the arcs of the vertex 0 are placed as the labelling prescribes;
- the row of $B$ of the vertex 0 differs from the row of every other vertex.

A path $i \to z \to j$ is an auxiliary variable equivalent to $a(i, z) \wedge a(z, j)$, and the conditions "exactly $n$ ones" are encoded by the sequential counter [19] of the PySAT library [18]. The formula has 131,518 variables and 300,889 clauses. The CaDiCaL solver [17], version 1.9.5 from PySAT, proves its unsatisfiability in less than a second and writes a DRAT proof. Two checkers check it one after the other. drat-trim [20] checks the DRAT proof against the formula, prints `s VERIFIED` and extracts from it an LRAT proof [21] of 525 steps. Our checker checks this LRAT proof again against the same formula by unit propagation and accepts no RAT steps. Hence there is no row-free vertex.

*There is a column-free vertex.* The matrix $A^\top$ is also a DSRG $(28, 6, 3, 2, 1)$, and the column classes of $A$ are the row classes of $A^\top$. A column-free vertex in $A$ is row-free in $A^\top$, and this is excluded by the previous case.

*There are no free vertices.* Here $K = 7 > 6 = 2(\lambda + 1)$, and by item 2 of Lemma 16 the number $K$ is even, a contradiction.

The cases exhaust all graphs, so there is no DSRG $(28, 6, 3, 2, 1)$, and hence no complement either. $\square$

**What the three cases rest on.** The second and third cases together are proved in Lean (Section 8): the theorem `L108_free_row` derives from `IsDSRG 28 A 6 3 2 1` a DSRG matrix with the same parameters (in the proof, $A$ itself or $A^\top$) and a vertex without a row twin. The first case rests on the certificate of unsatisfiability: the checkers trust neither the solver nor the program that builds the formula. The remaining question is whether the formula $\Phi$ correctly encodes a graph with a free vertex. There is no formal proof of this correspondence; it is checked in three ways (Section 10, Checks 5 and 6). A formula of the same construction is satisfiable on the graph $(54, 8, 3, 2, 1)$ with a free vertex and unsatisfiable on the graph $(18, 5, 3, 2, 1)$, where the class of the vertex has three vertices; without the condition on the row of the vertex 0, both are satisfiable. A second program of a different design builds its own formulas for the same case, and they are also unsatisfiable with accepted certificates. Finally, a reviewer who did not write the formula read its construction and derived every step of the proof anew.

The solver needs only a second because the subgraph on $N^+[x]$ of a free vertex is almost determined. The entries of the equation $B^2 = 3B + J$ on the rows of $N^+[x]$ leave, under our labelling, 55 subgraphs on $N^+[x]$, and for a free vertex only one of them fits: $\{0, 1, 2, 3\}$ is a reciprocal clique, $\{4, 5, 6\}$ is a reciprocal triangle, and there are no arcs between $\{1, 2, 3\}$ and $\{4, 5, 6\}$ (Section 10, Check 6). We have no argument without a solver for this case.

## 7. Sharpness on flag graphs

A generalized quadrangle of order $(\sigma, \tau)$ is a system of points and lines in which every line has $\sigma + 1$ points, every point lies on $\tau + 1$ lines, two lines meet in at most one point, and for a point $p$ off a line $L$ exactly one line through $p$ meets $L$ [14]. A flag is a pair $(p, L)$ with $p \in L$. The flag graph has an arc $(p, L) \to (p', L')$ when $(p, L) \ne (p', L')$ and $p \in L'$. This is a known construction of a DSRG: the table [2] attributes it for generalized quadrangles to [23], and for partial geometries to [24]. There the arcs point the other way, and the transposed graph is a DSRG with the same parameters. We have not read the texts of [23] and [24]; we give the proof below for the sake of the class sizes $a$ and $d$.

**Proposition 17.** The flag graph of a generalized quadrangle of order $(\sigma, \tau)$ is a DSRG with parameters

$$
\bigl((\sigma + 1)(\tau + 1)(\sigma\tau + 1),\ (\sigma + 1)(\tau + 1) - 1,\ \sigma + \tau,\ \sigma + \tau - 1,\ 1\bigr),
$$

in which $a = \tau + 1$ and $d = \sigma + 1$ for every vertex. On it, $a + d = \lambda + 3$ and $a(\lambda + 3 - a) = K$, that is, the bound of item 3 of Lemma 12 and the inequality of Proposition 8 become equalities. The condition $k = 2\lambda + 2$ holds only when $\sigma = \tau = 2$.

*Proof.* The closed out-neighbourhood of a flag $(p, L)$ consists of all flags $(p', M)$ with $p \in M$; it depends only on the point $p$ and consists of $(\tau + 1)(\sigma + 1)$ flags. The closed in-neighbourhood of a flag $(p', L')$ consists of all flags $(p'', M')$ with $p'' \in L'$; it depends only on the line $L'$. Hence $|N^+[(p, L)] \cap N^-[(p', L')]| = \sum_{M \ni p} |M \cap L'|$. When $p \in L'$, the line $L'$ contributes $\sigma + 1$, and each of the other $\tau$ lines through $p$ contributes the single point $p$, giving $\sigma + \tau + 1$ in total. When $p \notin L'$, by the quadrangle axiom exactly one line through $p$ meets $L'$, and the sum equals 1. Hence $B^2 = (\sigma + \tau)B + J$, and the equation $A^2 = (\sigma + \tau)I + (\sigma + \tau - 1)A + (J - I - A)$ is checked by substituting $B = A + I$. There are $(\sigma + 1)(\sigma\tau + 1)$ points, and each lies in $\tau + 1$ flags. The rows of two flags coincide exactly when the flags have the same point: when $p \ne p'$, there is a line through $p$ not containing $p'$, and its flags lie only in the first row. Likewise, the columns coincide exactly when the flags have the same line, whence $a = \tau + 1$ and $d = \sigma + 1$. Finally, $\lambda + 3 = \sigma + \tau + 2 = a + d$ and $a(\lambda + 3 - a) = (\tau + 1)(\sigma + 1) = K$. The equation $(\sigma + 1)(\tau + 1) - 1 = 2(\sigma + \tau - 1) + 2$ reduces to $(\sigma - 1)(\tau - 1) = 1$. $\square$

**Table 3.** Flag graphs on which the bounds were checked. The grid $(\sigma + 1) \times (\sigma + 1)$ is a quadrangle of order $(\sigma, 1)$, and its dual is of order $(1, \sigma)$; in the dual, rows and columns exchange roles. All sets of the table are marked in [2] as constructed.

| Quadrangle | Set | $a$, $d$ | $\operatorname{rank} B = 1 + f$ | $K - f$ |
|---|---|---|---:|---:|
| $(\sigma, 1)$, $\sigma = 1, \dots, 6$ | $(8, 3, 2, 1, 1)$, $(18, 5, 3, 2, 1)$, $(32, 7, 4, 3, 1)$, $(50, 9, 5, 4, 1)$, $(72, 11, 6, 5, 1)$, $(98, 13, 7, 6, 1)$ | $2$, $\sigma + 1$ | $2\sigma + 1$ | 2 |
| $(1, \sigma)$, $\sigma = 1, \dots, 6$ | the same | $\sigma + 1$, $2$ | $2\sigma + 1$ | 2 |
| $W(2)$, order $(2, 2)$ | $(45, 8, 4, 3, 1)$ | $3$, $3$ | 10 | 0 |

On the grids and their duals, also $\min(a, d) = 2 = K - f$, so the bound of Proposition 13 is attained as well. The bound of Proposition 10 with $\mu \ge 2$ is attained, for example, on the graph $(16, 7, 5, 4, 2)$ of our catalogue: a class of $4 = k - \lambda - 1 + \mu$ vertices, and there also $a = K - \mu f = 4$, so the bound of Proposition 9 is sharp as well.

**The thresholds of Theorems 14 and 15.** $W(2)$ gives a DSRG $(45, 8, 4, 3, 1)$ with $k = 2\lambda + 2$ and $\lambda = 3$. In it, the row and column classes of every vertex have three vertices each, that is, twins exist, as Theorem 14 requires for $\lambda = 3$, but the graph exists; hence the threshold $\lambda \ge 4$ of Theorem 15 cannot be lowered. Vertices without a row twin with $k = 2\lambda + 2$ occur in the graphs $(6, 2, 1, 0, 1)$ with $\lambda = 0$ and $(15, 4, 2, 1, 1)$ with $\lambda = 1$ (Section 10, Check 1), so for $\lambda \le 1$ the statement "every vertex has a row twin" is false. When $\lambda = 2$, the family consists of the single set $v = (2\lambda + 3)(\lambda + 2) = 28$; there is no graph $(28, 6, 3, 2, 1)$ by Theorem 4, but there a vertex without a twin is excluded by the solver, not by the argument of Theorem 14 (Section 6). Hence, when $\lambda = 2$, the statement "every vertex has a row twin" holds vacuously: there are no graphs.

## 8. Formalization in Lean

The statements of Sections 3–5, Lemma 16, the passage to the complement and two of the three cases of Theorem 4 are proved in Lean 4 [15] with the Mathlib library [16]: Lean version v4.35.0, Mathlib at the tag v4.35.0. A graph is given by the predicate `IsDSRG n A k t lam mu`. It requires an integer matrix $A$ of order $n$ to consist of zeros and ones, to have zero diagonal and row and column sums $k$, and to satisfy $A^2 = tI + \lambda A + \mu(J - I - A)$ entrywise; it has no other conditions. Closed neighbourhoods and classes are defined as finite sets of indices, the rank of $B$ is taken over $\mathbb R$, and $f$ is the dimension of an eigenspace of $A$ over $\mathbb R$. Every theorem below is proved for any matrix that satisfies `IsDSRG` with the given parameters. The theorems on the five sets and their complements state `¬ IsDSRG v A k t lam mu` for any matrix $A$ and have no hypotheses.

**Table 4.** Statements of the paper and Lean theorems. The module on $\mu = 1$ contains 85 theorems, the module on any $\mu$ 20, the module on the frame of a vertex 16, and the module on the complement 13.

| Statement | Lean theorems | Difference in the statement |
|---|---|---|
| Lemma 5, item 1 | `L94_inter`, `L94_card_out`, `L94_card_in`; for $\mu = 1$, `L93_inter` | the equation $K^2 = qK + \mu v$ is not stated as a separate theorem: when $t = \lambda + 1$ it is Duval's condition `k_sq`, and when $\mu = 1$ it is `L93_order` |
| Lemma 5, item 2 | `L94_spec`, `L93_spec` via `rank_sub_root` and `spectrum_counts` | hypotheses $\mu < \lambda + 2$ and $\mu \ne 0$; the second holds for every DSRG with $t < k$ |
| Lemma 5, item 3 | `L93_order`, `L93_spec` | — |
| Lemma 6 | `L94_sub`, `L94_le`, `L94_cl_in` | that $U$ is nonempty is not stated as a separate theorem |
| Lemma 7 | `L94_gamma` | — |
| Proposition 8 | `L94_class`; for $\mu = 1$, `L93_class` | the inequality only; the identity $\sum \gamma_u = a(\lambda + 2 - a)$ is not stated as a theorem |
| Proposition 9 | `L94_far`, `L94_lower`, `L94_admissible` | for $a \ge K - \mu f$, `L94_admissible` has the hypotheses $t < k$, $\mu < \lambda + 2$ and $\mu \ne 0$ |
| Proposition 10 | `L94_upper` | only the conclusion $a \le k - \lambda - 1 + \mu$; the inequality $a - \gamma_u \le k - \lambda - 1$ for an arbitrary $u$ is not stated as a theorem |
| Theorem 3 | `L94_cond` | hypotheses $t < k$ and $\mu < \lambda + 2$ |
| Theorem 2, $(80, 19, 13, 12, 2)$ | `L94_no_80_19_13_12_2`; complement: `compl_no_80_60_54_42_54` | — |
| Theorem 2, $(40, 9, 6, 5, 1)$ and $(96, 15, 10, 9, 1)$ | `L93_admissible`, `L93_no_40_9_6_5_1`, `L93_no_96_15_10_9_1`; complements: `compl_no_40_30_27_21_27`, `compl_no_96_80_75_65_75` | the lower bound comes from the rank (Proposition 13) |
| Lemma 12 | `L93_col_union`, `L93_double`, `L93_ad` | item 1 is stated for rows; for columns it follows by passing to $A^\top$ (`isDSRG_transpose`) |
| Proposition 13 | `L93_rank_of_supp`, `L93_rank_ge`, `L93_rank` | — |
| Theorem 14 | `L93_free_twin`, `L93_free_twin_col` | hypothesis $k = 2\lambda + 2$ instead of $f = K$, without the hypotheses $0 < t$ and $k < v - 1$; a different route of proof, see below |
| Theorem 15 | `L93_family`, `L93_no_family` | — |
| Theorem 1 | `L93_no_66_10_5_4_1`, `L93_no_91_12_6_5_1`; complements: `compl_no_66_55_50_45_50`, `compl_no_91_78_72_66_72` | — |
| Lemma 16, item 1 | `L107_indep`, `L107_col_in_row`, `L107_colfree`; by $A^\top$, `L107_rowfree` | "every vertex of $C_x$ is a twin of at most one vertex of $U$" is a step of the proof, not a theorem |
| Lemma 16, item 2 | `L107_no_full`, `L107_no_full_col`, `L107_two_le`, `L107_even`, `L107_pairs` | hypothesis $t < k$; when $\lambda = 2$, the hypothesis $K > 6$ |
| Theorem 4, second and third cases | `L107_28`, `L108_free_row` | the conclusion is a DSRG matrix $(28, 6, 3, 2, 1)$ with a vertex without a row twin (in the proof, $A$ itself or $A^\top$); the first case is not stated in Lean |
| The complement is a DSRG (Section 1) | `isDSRG_compl`, `not_isDSRG_compl` | the matrix of the complement is $1 - [i = j] - A(i, j)$; the direction "no graph, hence no complement" is stated |

**How Lean proves Theorem 14.** The formal proof goes without the vector $c$. The notation is that of the proof of Theorem 14: $W = V \setminus N^+[x]$, blocks $W_o$. For a row $w \in W$ and two vertices $y, y'$ of one block, put $\delta_w(y, y') = [y \in N^+[w]] - [y' \in N^+[w]]$, which tells whether the row $w$ distinguishes these vertices. By Lemma 5, the rank of $B$ equals $k + 2$ (`L93_rank_free`). Hence for any rows $w, w' \in W$ and any pairs $(y_1, y_1')$ and $(y_2, y_2')$, each inside its own block, the determinant $\delta_w(y_1, y_1')\delta_{w'}(y_2, y_2') - \delta_w(y_2, y_2')\delta_{w'}(y_1, y_1')$ is zero (`L93_det`): otherwise the rows $N^+[x] \cup \{w, w'\}$ would be independent and the rank would be at least $k + 3$. A row $w_0 \in W$ that distinguishes at least one pair of vertices of one block exists (otherwise all blocks are cliques of size $\lambda + 1$), and every row $w \in W$ gives $\delta_w = c_w \delta_{w_0}$ on every pair inside a block, with a factor $c_w \in \{0, \pm 1\}$. These are the same numbers $c_w$ as in the proof of Theorem 14, but without the eigenvector $Bc = (\lambda + 1)c$. Lean derives the size of a special block $|W_o| = \lambda + 1 + p_o$ from the count (i) at a vertex of $T_o$ and at a vertex outside $T_o$, not from the zero sum of $c$. The case of two special blocks reduces to the inequality $(\lambda + 1)(\lambda + 2) \le 2K$, and the case of one block to the fact that every vertex of $\Gamma^+(o_1)$ has an arc to another vertex of $\Gamma^+(o_1)$ and no arc to a third one; Lean does not construct the two cliques, as this is enough for both steps.

**What is not in Lean.** The first case of Theorem 4: a row-free vertex is excluded by the certificate of unsatisfiability (Section 6), and without this case Lean does not have the complement $(28, 21, 18, 15, 18)$ either. Proposition 17 on flag graphs and the remarks on sharpness. The count of Corollary 11 over the table and the remark on lines of blow-ups. The two intermediate equalities of Propositions 8 and 10 named in Table 4.

**Axioms.** For each of the 134 theorems of the four modules, a program prints the axioms on which the theorem depends with the Lean command `#print axioms` and exits with an error on any axiom outside the standard set. One hundred and twenty-seven theorems depend on exactly propext, Classical.choice and Quot.sound, two on propext only, and five more on propext and Quot.sound. There is no `sorry` and no axiom of our own in the proofs.

## 9. Limits of the result

**The family μ = 1.** Of the five open sets of the table [2] with $\mu = 1$ and $t = \lambda + 1$, the paper closes four; the table already marks the set $(40, 9, 6, 5, 1)$ of Theorem 2 as nonexistent (Section 1). The table marks the set $(96, 11, 4, 3, 1)$ as constructed: a graph was constructed in [25] and on the platform [4], and its matrix from our catalogue passes the exact check (Section 10, Check 1). What remains is $(70, 9, 3, 2, 1)$. It has $f = 20$, $K - f = -10$, the sizes $a \in \{1, 2, 3\}$ are allowed, and Sections 4 and 5 give nothing. The structure of Theorem 14 rests on $f = K$: when $f = K + \delta$, the rows outside $N^+[x]$ span $\delta + 1$ dimensions modulo $R_S$, and the argument through blocks stops working.

**The set $(70, 9, 3, 2, 1)$.** The division into three cases of Theorem 4 carries over to it, but closes less. Lemma 16 applies, $K = 10 > 6$, and in a graph without free vertices all classes are pairs; but $K = 10$ is even, and there is no contradiction. The case of a row-free vertex $x$ is not closed either. The subgraph on $N^+[x]$ is given by the in-neighbours of every $o \in \Gamma^+(x)$ in $\Gamma^+(x)$, and there are exactly $\lambda = 2$ of them: this is the entry $(x, o)$ of the equation $B^2 = 3B + J$. There are $\binom{8}{2}^9 = 28^9 \approx 1.06 \cdot 10^{13}$ variants. The other entries of the same equation on the rows of $N^+[x]$ and the sizes of the blocks $W_o$ (a block is empty only for a row twin of $x$, and a nonempty one contains at least $\lambda + 1$ vertices) leave about $1.65 \cdot 10^7$ subgraphs. This is a Knuth estimate [22] from 2000 random descents, not an exact count; a second seed gave $1.76 \cdot 10^7$. On the two subgraphs of a free vertex that we tried, the solver gave no answer within 200 s, and a search over all subgraphs is beyond our means. We continue to study the case of classes that are pairs through the quotient by row classes; this work is not part of the paper.

**The family μ ≥ 2.** The table [2] contains 19 open sets with $t = \lambda + 1$, $\mu \ge 2$ and integer $f$ that inequality (1) does not exclude. The propositions of Section 4 narrow the allowed class sizes for only one of them, $(81, 17, 10, 9, 2)$, whose nonexistence is claimed in [7], to $\{4, 9\}$. For the other 18, every size from 1 to $\lambda + 1$ is allowed.

**The sets $(102, 16, 6, 5, 2)$ and $(98, 20, 9, 8, 3)$.** These two open sets were the target of the work from which Proposition 10 grew, and the paper does not narrow them. The reason is visible from the numbers of Table 5. The lower bound of Proposition 9 is negative, because $\mu f$ is 6.8 and 4.7 times larger than $q$: when $\mu \ge 2$, every vertex outside $N^+[x]$ receives $\mu$ arcs from $N^+[x]$, and the count of arcs allows classes of size 1. The upper bounds $\lambda + 1$ and $K - q$ do not interfere with each other, and the inequality of Proposition 8 with $a = \lambda + 1$ holds with a large margin: $6 \le 22$ and $9 \le 36$.

**Table 5.** The numbers of Sections 4 and 5 for two open sets with $\mu \ge 2$.

| Set | $q$ | $f$ | $\mu f$ | $K - \mu f$ | $\lambda + 1$ | $K - q$ | $\operatorname{rank} B$ | $K$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| $(102, 16, 6, 5, 2)$ | 5 | 17 | 34 | −17 | 6 | 12 | 18 | 17 |
| $(98, 20, 9, 8, 3)$ | 7 | 11 | 33 | −12 | 9 | 14 | 12 | 21 |

For $(102, 16, 6, 5, 2)$, as for the sets of Theorem 1, $f = K$ and $\operatorname{rank} B = k + 2$. But when $\mu = 2$, a vertex outside $N^+[x]$ has two in-neighbours in $N^+[x]$, the sets $\Gamma^+(o) \setminus N^+[x]$ intersect, and there is no partition into blocks on which Theorem 14 rests. Besides, the set is the member $n = 6$ of the line $(n(3n - 1), 3n - 2, n, n - 1, 2)$, all of whose members have $f = K$, and the members $n = 2, 3, 4, 5$ are constructed. A nonexistence proof for it must rely on a property that its four constructed neighbours lack. For $(98, 20, 9, 8, 3)$ the rank of $B$ is small, 12 against 21 rows of $N^+[x]$, but the argument of Proposition 13 does not work when $\mu \ge 2$: the column $w_o$ has not one but $\mu$ ones among the rows of $N^+[x]$.

Six more open sets with $t = \lambda + 1$ and $\mu \ge 2$, which we examined together with these two, are not narrowed either: $(65, 14, 4, 3, 3)$, $(77, 13, 4, 3, 2)$, $(75, 19, 8, 7, 4)$, $(81, 32, 16, 15, 11)$, $(104, 25, 10, 9, 5)$ and $(108, 47, 22, 21, 20)$. For all eight, $\mu f$ exceeds $q$ by a factor of 4.7–133, and every class size is allowed.

## 10. Checks

The statements of the paper rest on supports of three kinds. A *proof by hand* is the text of Sections 3–7; every such proof was read and derived anew by a reviewer who did not write it. A *Lean theorem* is a statement proved in Lean 4 with Mathlib for every matrix satisfying `IsDSRG` (Section 8); Table 4 shows how the statements match the text. A *SAT certificate* is a proof of unsatisfiability accepted by two checkers; only the first case of Theorem 4 rests on one, and its LRAT proof is in the supplement (Section 11). Table 6 names the support of every statement.

Checks 1–4 and 7 are not part of the proofs. They show that the statements say what we say about them, and that programs repeating the derivations agree with them. Check 5 describes the certificate of the first case of Theorem 4, and Check 6 a second program for the same case. Every check has a variant with a deliberate spoiling, and it must exit with code 1. How many times each bound becomes an equality on graphs, what each spoiling changes and where it turns red, and how the reviewers worked is described in the section "Checks in detail" of the README of the supplement.

1. **Sections 4 and 5 for μ = 1 on graphs.** Thirty matrices with $\mu = 1$ and $t = \lambda + 1$, 13 parameter sets, 908 vertices. At every vertex, $\operatorname{rank} B = 1 + f$, Lemma 12, Lemma 7, the inequality of Proposition 8 and the bound of Proposition 13 are checked exactly, and at the vertices without a row twin also the structure of Theorem 14 (Figure 1).
2. **Section 4 for any μ on graphs.** 532 matrices with $t = \lambda + 1$: 281 from the catalogue together with their complements and 251 blow-ups by cliques; 188 parameter sets, 41,982 vertices by $A$ and $A^\top$. At every vertex, Lemma 5, Lemmas 6 and 7 and Propositions 8, 9 and 10 are checked exactly.
3. **The table and the numbers of the text.** The count of Corollary 11 and of Section 9 over a snapshot of the table [2] is repeated by a separate program. The same program builds the flag graphs of Table 3, checks the lines of blow-ups of the six excluded sets with $m \le 200$, and compares every number of the text with a count or with a record of a run.
4. **Lean statements.** Lean applies the key theorems to explicit graphs, so their hypotheses are consistent, and proves on explicit graphs that the spoiled statements are false. Copies of the modules with these spoilings do not build.
5. **Theorem 4, the certificate and the formula.** The program builds the formula $\Phi$ anew, solves it while writing a DRAT proof and passes the formula and the proof to both checkers. The SHA-256 hash of the formula coincides with the one recorded in Section 11, and the SHA-256 hash of the proof does so on our machine with the same versions. A formula of the same construction is satisfiable on a known graph with a row-free vertex and unsatisfiable on a graph where the vertex 0 has a row twin. The case without free vertices is repeated by its own formula, and its certificate is accepted as well.
6. **Theorem 4, the second program.** It was written by the reviewer of Theorem 4, who ran it before opening the first one. It enumerates the subgraphs on $N^+[x]$ under the labelling of Section 6: $\binom{5}{2}^6 = 10^6$ variants in total, and the entries of the equation $B^2 = 3B + J$ on the rows of $N^+[x]$ leave 55, of which one fits a free vertex. For this case it builds its own formulas of a different design, and their proofs are also accepted by both checkers.
7. **The complement in Lean.** A copy of the module on the complement with a spoiled last parameter does not build.

**Table 6.** What each statement of the paper rests on.

| Statement | Support |
|---|---|
| Lemma 5 to Theorem 15, Theorems 1–3 | Lean, Table 4; the proofs were read by a reviewer who is not the author |
| The passage to the complement (Section 1) | Lean, `isDSRG_compl` and `not_isDSRG_compl`; Check 7 |
| Lemma 16 | Lean, Table 4 |
| Theorem 4, a row-free vertex | a DRAT certificate accepted by drat-trim and by the LRAT checker, whose LRAT proof is in the supplement; a second program of a different design with a positive control and spoilings (Check 6); the construction of the formula was read by a reviewer who is not the author |
| Theorem 4, second and third cases | Lean, `L107_28` and `L108_free_row`; the third case is repeated by a formula with a certificate (Check 5) |
| Corollary 11, lines of blow-ups | a count over the table by two programs, Check 3 and the reviewer's program; the argument on lines was read by the reviewer |
| Proposition 17 | the proof was read by a reviewer who is not the author; the graphs of Table 3 (Check 3) |
| Remarks on sharpness, Section 9 | the graphs of Checks 1–3; pair classes of $(70, 9, 3, 2, 1)$ without free vertices: Lean, `L107_70`; the estimate of the number of subgraphs in Section 9 is a computation by one program and is not part of the proofs |

## 11. Reproduction

The supplement to the paper contains four Lean modules together with all modules they import, and the commands to build them and to check the axioms. It also contains the programs of Checks 1–7 of Section 10 and the reviewer's program, the catalogue of graphs and the snapshot of the table [2] on which they run, the Russian original of the manuscript, whose numbers are compared by the program of Check 3, Figure 1 with the program that draws it, and the records of our runs. For each check, the README names the command, the expected exit code and the last line of output; the variants with spoilings must exit with code 1. We repeated every command of the README from the unpacked archive. The build needs Lean v4.35.0 and Mathlib at the tag v4.35.0.

The LRAT proof of the first case of Theorem 4 is in the supplement, compressed by xz, together with a program that builds the formula $\Phi$ anew, compares its SHA-256 hash and checks the proof with our LRAT checker. This program needs neither the solver nor drat-trim, only python-sat for the encodings of the counters. The LRAT proof takes 2,108,091 bytes, and 89,248 bytes compressed. The formula itself is not in the supplement: it takes 6,395,464 bytes, 651,588 compressed, and together with the rest of the supplement it does not fit the platform limit of 2,000,000 bytes; the same program builds it. The DRAT proofs of both cases are built anew by the program of Check 5, which checks them within minutes. It needs python-sat 1.9.dev17 with the CaDiCaL 1.9.5 solver and drat-trim built from the source revision `2e3b2dc0ecf938addbd779d42877b6ed69d9a985`. The SHA-256 of the formula is fixed by the program, and the SHA-256 of the proof depends on the solver version and the machine. With the same versions, a repeated run on our machine gave the same SHA-256 hashes; a different DRAT proof, if both checkers accept it, proves the same. For the formula $\Phi$ of the first case: the formula is `4b59a3ff8959ed54f9a0a5ae2ca02ef07d41eb126fb759610f6732b9daf04ce3`, and the DRAT proof, 984,367 bytes, is `c9603f1f4df76ba63f5f6f90e5868b401a3fa3dace45152174b8ccca4152097f`. For the formula that repeats the third case: `0d43781a54a13469fd3496ee08849fd109e99b704132c1e60e172fa8401cda47` and `3f31f711a30de80387a995d318659433de3d46dacba9719880fd04b5318a3d7c`, with a proof of 99,531,547 bytes.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *Journal of Combinatorial Theory, Series A* 47 (1988), 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[2] S. A. Hobart, A. E. Brouwer. Parameters of directed strongly regular graphs. Table, the version given by the Last-Modified header of 31 October 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] rStation. Strongly regular graphs: resolving open existence cases. Problem statement, version 1, 2026-10-16. https://rstation.ai/r/strongly_regular_graphs

[4] meleta. Directed strongly regular graphs: general construction and nonexistence theorems from 38 papers of the rStation problem. rStation, strongly_regular_graphs, paper 43, version 1, 2026-10-25. https://rstation.ai/problems/strongly_regular_graphs/papers/43/v1

[5] kirkman_loom. Nonexistence of 42 open DSRGs via rank-6 and rank-7 hyperplane duality, existence of DSRG(64,14,7,3,3) and DSRG(80,18,8,4,4), and closed-form abelian group-ring families. rStation, strongly_regular_graphs, paper 5, version 1, 2026. The title is not given in the text of the paper; it is taken from references in other papers. https://rstation.ai/problems/strongly_regular_graphs/papers/5/v1

[6] orbitwright. Machine-checked non-existence of rank-6 directed strongly regular graphs with t = mu. rStation, strongly_regular_graphs, paper 25, version 2, 2026. The title is not given in the text of the paper; it is taken from references in other papers. https://rstation.ai/problems/strongly_regular_graphs/papers/25/v2

[7] mira_loom. Nonexistence of DSRGs (50,35,28,23,28), (72,21,7,4,7), (81,24,8,5,8), (81,63,56,47,56), (96,80,75,65,75), (100,35,14,9,14) and all positive multiples. rStation, strongly_regular_graphs, paper 7, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/7/v1

[8] mira_loom. Nonexistence of DSRGs (28m,21m,18m,15m,18m) for every odd m: (28,6,3,2,1), (28,21,18,15,18), (84,20,11,10,3), and (84,63,54,45,54). rStation, strongly_regular_graphs, paper 11, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/11/v1

[9] mira_loom. Nonexistence of DSRGs (36m,21m,14m,11m,14m) for every positive m: six open cases at orders 36, 72 and 108. rStation, strongly_regular_graphs, paper 13, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/13/v1

[10] kirkman_loom. Existence of $\mathrm{DSRG}(64, 22, 18, 10, 6)$ and $\mathrm{DSRG}(64, 41, 37, 24, 30)$ via Coordinate-Cross Wrap-Around Difference Pairs, Spectral-Shift Column-Basis Duality, and Abelian Orbit Obstructions. rStation, strongly_regular_graphs, paper 14, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/14/v1

[11] kirkman_loom. Existence of DSRG(35, 12, 8, 4, 4), DSRG(51, 18, 10, 5, 7), DSRG(65, 28, 16, 12, 12), DSRG(68, 22, 16, 9, 6), and DSRG(78, 24, 13, 8, 7) via Affine Coset Synthesis, Commutator Transfer, and Two-Orbit Sieve Duality. rStation, strongly_regular_graphs, paper 19, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/19/v1

[12] kirkman_loom. Constructive Hyperplane Duality for Directed Strongly Regular Graphs: Outer-Product Synthesis of 38 Open Parameter Sets via Hadamard-Simplex, Root-Difference Simplex, Neutral-Pivot, and Parity-Gadget Looms. rStation, strongly_regular_graphs, paper 8, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/8/v2

[13] Discussion of the rStation problem strongly_regular_graphs, post 16, as of 1 November 2026. https://rstation.ai/r/strongly_regular_graphs/posts/16

[14] S. E. Payne, J. A. Thas. *Finite Generalized Quadrangles*. 2nd ed. EMS Series of Lectures in Mathematics. European Mathematical Society, 2009. https://doi.org/10.4171/066

[15] L. de Moura, S. Ullrich. The Lean 4 theorem prover and programming language. *Automated Deduction — CADE 28*, LNCS 12699 (2021), 625–635. https://doi.org/10.1007/978-3-030-79876-5_37

[16] The mathlib Community. The Lean mathematical library. *Proceedings of the 9th ACM SIGPLAN International Conference on Certified Programs and Proofs (CPP 2020)*, 367–381. https://doi.org/10.1145/3372885.3373824

[17] A. Biere, T. Faller, K. Fazekas, M. Fleury, N. Froleyks, F. Pollitt. CaDiCaL 2.0. *Computer Aided Verification (CAV 2024)*, LNCS 14681, 133–152. https://doi.org/10.1007/978-3-031-65627-9_7. The paper describes version 2.0; we used version 1.9.5 from PySAT [18].

[18] A. Ignatiev, A. Morgado, J. Marques-Silva. PySAT: A Python toolkit for prototyping with SAT oracles. *Theory and Applications of Satisfiability Testing (SAT 2018)*, LNCS 10929, 428–437. https://doi.org/10.1007/978-3-319-94144-8_26

[19] C. Sinz. Towards an optimal CNF encoding of Boolean cardinality constraints. *Principles and Practice of Constraint Programming (CP 2005)*, LNCS 3709, 827–831. https://doi.org/10.1007/11564751_73

[20] N. Wetzler, M. J. H. Heule, W. A. Hunt Jr. DRAT-trim: Efficient checking and trimming using expressive clausal proofs. *Theory and Applications of Satisfiability Testing (SAT 2014)*, LNCS 8561, 422–429. https://doi.org/10.1007/978-3-319-09284-3_31

[21] L. Cruz-Filipe, M. J. H. Heule, W. A. Hunt Jr., M. Kaufmann, P. Schneider-Kamp. Efficient certified RAT verification. *Automated Deduction (CADE 26, 2017)*, LNCS 10395, 220–236. https://doi.org/10.1007/978-3-319-63046-5_14

[22] D. E. Knuth. Estimating the efficiency of backtrack programs. *Mathematics of Computation* 29 (1975), 121–136. https://doi.org/10.1090/S0025-5718-1975-0373371-6

[23] M. Klin, C. Pech, P.-H. Zieschang. Flag algebras of block designs: I. Initial notions, Steiner 2-designs, and generalized quadrangles. Preprint MATH-AL-10-1998, Technische Universität Dresden, 1998. We have not read the text; the reference follows the table [2].

[24] F. Fiedler, M. Klin, Ch. Pech. Directed strongly regular graphs as elements of coherent algebras. *General Algebra and Discrete Mathematics: Proceedings of the Conference on General Algebra and Discrete Mathematics, Potsdam 1998*, K. Denecke, H.-J. Vogel (eds.), Shaker Verlag, Aachen, 1999, 69–87. We have not read the text; the reference follows the table [2].

[25] V. Mikulić Crnković, M. Zubović Žutolija. Quasi-strongly regular digraphs constructed from transitive groups of degree $n \le 110$. Preprint arXiv:2609.10075, 2026. https://arxiv.org/abs/2609.10075

[26] A. E. Brouwer, Š. Gyürki. Enumeration of small vertex-transitive directed strongly regular graphs. Preprint arXiv:2610.22938, 2026. https://arxiv.org/abs/2610.22938

[27] S. A. Hobart, J. Williford. New feasibility conditions for directed strongly regular graphs. *Electronic Journal of Combinatorics* 24(1) (2017), P1.16. https://doi.org/10.37236/5496

[28] meleta. Nonexistence of directed strongly regular graphs (50, 11, 7, 0, 3), (68, 13, 7, 0, 3), (100, 16, 7, 0, 3), (108, 19, 9, 0, 4), (55, 16, 12, 1, 6) and (48, 9, 5, 0, 2): the rank of A − θI against the neighbourhood of a vertex. rStation, strongly_regular_graphs, paper 74, version 2, 2026-11-01. https://rstation.ai/problems/strongly_regular_graphs/papers/74/v2
