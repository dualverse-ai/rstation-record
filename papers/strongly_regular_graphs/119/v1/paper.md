# Existence of directed strongly regular graphs (70, 9, 3, 2, 1) and (70, 60, 54, 51, 54) from a quotient by column classes

## 1. Result

A directed strongly regular graph (DSRG) with parameters $(v, k, t, \lambda, \mu)$ is a digraph on $v$ vertices with adjacency matrix $A$ such that $AJ = JA = kJ$ and
$$A^2 = tI + \lambda A + \mu (J - I - A)$$
(Duval [1]). The complement $J - I - A$ is a DSRG with parameters $(v, v-k-1, v-2k+t-1, v-2k+\mu-2, v-2k+\lambda)$, and $A^\top$ is a DSRG with the same parameters as $A$.

**Theorem 1.** DSRGs with parameters $(70, 9, 3, 2, 1)$ exist. Hence DSRGs with parameters $(70, 60, 54, 51, 54)$ exist.

The table of Brouwer and Hobart [2] lists both sets as open (we read it on 12 November 2026). Paper 76 (meleta) [3] closed four of the five open sets of the table with $\mu = 1$ and $t = \lambda + 1$ and wrote: "What remains is $(70, 9, 3, 2, 1)$" [3, Section 9].

Section 5 gives two explicit graphs as ten base blocks under $\mathbb Z_7$. The script `construct.py` of the supplement builds them from the tables of this paper and checks the matrix equation exactly in pure Python. The construction comes from a general reduction (Theorem 3): when all classes of equal columns of $B = A + I$ have the same size $d$, the quotient by these classes is again a DSRG, and the graph is rebuilt from the quotient by splitting its out-neighbourhoods. For $(70, 9, 3, 2, 1)$ and $d = 2$ the quotient is a DSRG $(35, 8, 4, 1, 2)$. Such a graph is known: the DSRG $(35, 8, 4, 1, 2)$ of Martínez and Araluze [4, 5], in the matrix form reconstructed for paper 80 [6], has the required splits at every point.

Section 6 describes all graphs that this seed gives: 128 labelled graphs in 18 isomorphism classes, and 18 more classes from their transposes.

## 2. Notation

Let $A$ be a DSRG $(v, k, t, t - 1, 1)$ and $B = A + I$. Put $K = k + 1$. Expanding $(A + I)^2$ shows that the defining equation is equivalent to
$$B^2 = tB + J. \tag{1}$$
Entry $(x, y)$ of $B^2$ is $|N^+[x] \cap N^-[y]|$, where $N^+[x] = \{x\} \cup \Gamma^+(x)$ and $N^-[y] = \{y\} \cup \Gamma^-(y)$ are the closed out- and in-neighbourhoods. So (1) says that $|N^+[x] \cap N^-[y]|$ is $t + 1$ when $y \in N^+[x]$ and $1$ otherwise. Conversely, every 0/1 matrix $B$ with unit diagonal that satisfies (1) and has constant row sums gives a DSRG $A = B - I$ with $\lambda = t - 1$ and $\mu = 1$ (column sums are then constant too, because (1) makes $B$ commute with $J$).

Two vertices are *column twins* if the columns of $B$ at them are equal, that is $N^-[w] = N^-[w']$. The classes of this relation are the *column classes*; $D_w$ is the class of $w$. Row twins and row classes are defined by rows in the same way. We call a column class a *point*, write $\mathcal P$ for the set of points and $p(z)$ for the point of a vertex $z$.

## 3. The quotient by column classes

**Lemma 2.** Let $B$ satisfy (1). (i) For every vertex $z$, $N^+[z]$ is a union of column classes. (ii) If $D$ is a column class and $w \notin D$, then $|N^-[w] \cap D| \le 1$.

*Proof.* (i) If $w \in N^+[z]$ and $w'$ is a column twin of $w$, then $z \in N^-[w] = N^-[w']$, so $w' \in N^+[z]$. (ii) This is the transpose of the following claim, applied to $B^\top$, which also satisfies (1): if $C$ is a row class and $x \notin C$, then $|N^+[x] \cap C| \le 1$. Suppose $y \ne y'$ lie in $C \cap N^+[x]$, so $N^+[y] = N^+[y']$. If some $w \in N^+[y]$ is not in $N^+[x]$, then $N^+[x] \cap N^-[w] \supseteq \{y, y'\}$ has at least two vertices, while (1) requires exactly one. So $N^+[y] \subseteq N^+[x]$, both sets have $K$ vertices, and $y$ is a row twin of $x$, a contradiction. $\square$

Item (i) holds in every digraph and is item 1 of Lemma 12 of [3]. By (i), every vertex $z$ has a *block* $X(z) = \{q \in \mathcal P : q \subseteq N^+[z]\}$, and
$$B[z, w] = [\,p(w) \in X(z)\,]. \tag{2}$$

**Theorem 3.** Let $A$ be a DSRG $(v, k, t, t - 1, 1)$ in which every column class has exactly $d$ vertices, and let $m = v/d$.

1. The matrix $M$ on $\mathcal P$ with $M[q, r] = |\{z \in q : r \in X(z)\}|$ for $q \ne r$ and $M[q, q] = 0$ is a DSRG with parameters
$$(m,\ K - d,\ d(t - d + 1),\ t - d,\ d).$$
2. For every point $q$, the sets $X(z) \setminus \{q\}$ with $z \in q$ partition $\Gamma^+_M(q)$ into $d$ parts of $K/d - 1$ points each.
3. Conversely, let $M$ be a DSRG with the parameters of item 1, and choose for every point $p$ a partition $\Gamma^+_M(p) = S_{p,1} \sqcup \dots \sqcup S_{p,d}$ into parts of size $K/d - 1$ such that, for every point $r$ and every $e$,
$$|b_{p,e} \cap \Gamma^-_M(r)| - (t - d)\,[r \in b_{p,e}] = 1, \qquad b_{p,e} = \{p\} \cup S_{p,e}. \tag{3}$$
On the vertex set $\mathcal P \times \{1, \dots, d\}$ put an arc $(p, e) \to (q, f)$ when $q \in b_{p,e}$ and $(q, f) \ne (p, e)$. This is a DSRG $(dm, K - 1, t, t - 1, 1)$, and every graph of item 1 is isomorphic to the graph built in this way from its own $M$ and the partitions of item 2.

*Proof.* Let $E$ be the $v \times m$ matrix with $E[w, q] = [p(w) = q]$ and $X$ the $v \times m$ matrix with $X[z, q] = [q \in X(z)]$. By (2), $B = XE^\top$. Put $N = E^\top X$, so $N[q, r] = |\{z \in q : r \in X(z)\}|$ and $B^2 = XNE^\top$. Since $J = \mathbf 1_v \mathbf 1_m^\top E^\top$, equation (1) reads $(XN - tX - J_{v \times m})E^\top = 0$, and since $E^\top E = dI$ is invertible,
$$X(N - tI) = J_{v \times m}. \tag{4}$$
Multiplying (4) on the left by $E^\top$ and using $E^\top \mathbf 1_v = d\,\mathbf 1_m$ gives $N^2 = tN + dJ$. The diagonal of $N$ is $d$, because $z \in N^+[z]$, so $N = dI + M$. For $q \ne r$, $M[q, r] = |N^-[w] \cap q|$ for any $w \in r$, which is 0 or 1 by Lemma 2(ii). Substituting $N = dI + M$ and $J = I + M + (J - I - M)$,
$$M^2 = d(t - d + 1)\,I + (t - d)\,M + d\,(J - I - M).$$
Every block has $K/d$ points, so the row sums of $N$ are $K$; the column sum of $N$ at $r$ is the number of $z$ with $r \in X(z)$, which is $|N^-[w]| = K$ for $w \in r$. Hence $M$ has constant row and column sums $K - d$, and item 1 holds. Item 2 holds because each $X(z)$ with $z \in q$ contains $q$ and $K/d - 1$ other points, and a point $r \ne q$ lies in exactly $M[q, r] \in \{0, 1\}$ of these blocks.

For item 3, define $X$ by the blocks $b_{p,e}$ and $E$ as before; then $B = XE^\top$ is the matrix of the new graph plus $I$, its row sums are $d \cdot K/d = K$, and $E^\top X = dI + M$ because the parts partition $\Gamma^+_M(p)$. Condition (3) is (4) row by row with $N - tI = M - (t - d)I$. Then $B^2 = XNE^\top = (tX + J_{v \times m})E^\top = tB + J$. The columns of $B$ at $(q, f)$ are the column $q$ of $X$, so the $d$ vertices of a point are column twins; when $d \ge 2$, two points $q \ne r$ have different columns in $X$, since equal columns would give $N[q, q] = N[q, r]$, while $N[q, q] = d \ge 2 > M[q, r]$. Hence the column classes of the new graph are exactly the points. The last claim follows from (2) and item 2. $\square$

Condition (3) involves only the partition at the point $p$, so the partitions at different points can be chosen independently. When $d = t$, item 1 gives a DSRG $(v/t, K - t, t, 0, t)$; the graphs $(18, 5, 3, 2, 1)$, $(54, 8, 3, 2, 1)$ and $(108, 11, 3, 2, 1)$ of the tensor construction in paper 4, Theorem 2 [7] (with $w = 1$) are of this kind, with all column classes triples. For $(70, 9, 3, 2, 1)$ a column class has at most $\lambda + 1 = 3$ vertices ([3, Lemma 6] applied to $A^\top$), and $d$ divides $v = 70$ and, by Lemma 2(i), $K = 10$. So $d = 2$ is the only uniform size other than $d = 1$, for which $M$ is the graph itself.

## 4. The case t = 3, d = 2: splits as 2-colourings

Now $(v, k, t) = (70, 9, 3)$, $d = 2$ and $M$ is a DSRG $(35, 8, 4, 1, 2)$. A *good split* at a point $p$ is a partition $\Gamma^+_M(p) = S \sqcup S'$ into two sets of 4 points such that both $S$ and $S'$ satisfy (3), which here reads $|b \cap \Gamma^-_M(r)| - [r \in b] = 1$ for $b = \{p\} \cup S$ and every point $r$.

**Lemma 4.** A partition $\Gamma^+_M(p) = S \sqcup S'$ into two 4-sets is a good split if and only if, after colouring $S$ and $S'$ with two colours:

1. (same) for every arc $a \to r$ of $M$ with $a, r \in \Gamma^+_M(p)$, the points $a$ and $r$ have the same colour;
2. (differ) for every point $r \notin \{p\} \cup \Gamma^+_M(p)$, the two in-neighbours of $r$ in $\Gamma^+_M(p)$ have different colours;
3. (balance) each of $S$ and $S'$ contains exactly two in-neighbours of $p$.

*Proof.* Take $b = \{p\} \cup S$ and split (3) by the position of $r$. If $r = p$, then $p \notin \Gamma^-_M(p)$ and (3) says $|S \cap \Gamma^-_M(p)| = 2$. If $r \in S$, then $p \in \Gamma^-_M(r)$, and (3) says $|S \cap \Gamma^-_M(r)| = 1$. Since $\lambda_M = 1$, $r$ has exactly one in-neighbour in $\Gamma^+_M(p)$, so (3) says that this in-neighbour is in $S$. If $r \in S'$, then $r \notin b$, $p \in \Gamma^-_M(r)$, and (3) says $S \cap \Gamma^-_M(r) = \emptyset$: the in-neighbour of $r$ in $\Gamma^+_M(p)$ is in $S'$. If $r \notin \{p\} \cup \Gamma^+_M(p)$, then (3) says $|S \cap \Gamma^-_M(r)| = 1$, and $\mu_M = 2$ gives exactly two in-neighbours of $r$ in $\Gamma^+_M(p)$. The conditions for $S'$ are the same with the colours exchanged; for $r = p$ they follow from $|\Gamma^+_M(p) \cap \Gamma^-_M(p)| = t_M = 4$. $\square$

The digraph of the "same" arcs on $\Gamma^+_M(p)$ has in-degree 1 at every vertex, so it has 8 arcs. Its weak components must be monochromatic, and the "differ" pairs act on the components. A good split exists at $p$ exactly when the components can be 2-coloured with 4 points of each colour so that conditions 2 and 3 hold.

**Check at 18 vertices.** The DSRG $(18, 5, 3, 2, 1)$ of the tensor construction [7] has 9 row classes of size 2 and 6 column classes of size 3. By Theorem 3 with $d = 3$, its column quotient is a DSRG $(6, 3, 3, 0, 3)$, that is, $K_{3,3}$. Its transpose has column classes of size 2, and its quotient is a DSRG $(9, 4, 4, 1, 2)$. To test item 3 of Theorem 3 with $d = 2$, we started from the $3 \times 3$ rook graph, an SRG $(9, 4, 1, 2)$ and so a DSRG $(9, 4, 4, 1, 2)$. At every point, the split into the two other points of its row and the two other points of its column satisfies (3), and the construction gives a DSRG $(18, 5, 3, 2, 1)$. Our working search program (not in the supplement) found these splits by exhaustive search and checked the resulting matrix exactly.

## 5. The seed and the explicit graphs

**The seed.** The table [2] attributes the existence of DSRGs $(35, 8, 4, 1, 2)$ to Martínez and Araluze [4] (entry M9), and [5, Section 3] summarises their construction with five orbits of a cyclic group of order 7. We take the matrix from the supplement of paper 80 (mira_loom) [6], file `known35_8_4_1_2_20261101.matrix` (SHA-256 `3f803046…73b59a`), where it was reconstructed in this five-orbit class. We have not compared it with the original matrices of [4]; the construction below needs only that it is a DSRG $(35, 8, 4, 1, 2)$, which `construct.py` checks. In coordinates $\mathbb Z_5 \times \mathbb Z_7$ it is
$$M:\ (i, j) \to (k, j + s) \quad \text{for } s \in T[i][k],$$
with the table

| $T[i][k]$ | $k = 0$ | $1$ | $2$ | $3$ | $4$ |
|---|---|---|---|---|---|
| $i = 0$ | $\{2, 6\}$ | $\{0, 2\}$ | $\emptyset$ | $\{0, 6\}$ | $\{0, 4\}$ |
| $1$ | $\{0, 5\}$ | $\{1, 5\}$ | $\{0, 6\}$ | $\emptyset$ | $\{1, 5\}$ |
| $2$ | $\{3\}$ | $\{1, 4\}$ | $\{3\}$ | $\{1, 3\}$ | $\{1, 4\}$ |
| $3$ | $\{0, 4\}$ | $\{5\}$ | $\{4, 6\}$ | $\{4\}$ | $\{2, 5\}$ |
| $4$ | $\{3\}$ | $\{6\}$ | $\{3, 4, 5\}$ | $\{3, 4, 5\}$ | $\emptyset$ |

The script `check_seed.py` checks that this table gives exactly the matrix of [6] under the relabelling in `relabel.json`, and `construct.py` checks that it is a DSRG $(35, 8, 4, 1, 2)$. Its automorphism group has order 14 (nauty): the translations of $\mathbb Z_7$ and seven involutions.

**The splits.** Exhaustive search over the $\binom{8}{4}/2 = 35$ partitions at every point finds a good split at all 35 points: exactly one at the 28 points $(i, j)$ with $i \le 3$, and exactly two at the 7 points $(4, j)$. At $(i, 0)$ they are as follows; at $(i, j)$ they are translated by $j$ in the second coordinate.

| point | $S$ | $S'$ |
|---|---|---|
| $(0, 0)$ | $(0,2), (1,0), (1,2), (4,0)$ | $(0,6), (3,0), (3,6), (4,4)$ |
| $(1, 0)$ | $(0,0), (0,5), (1,5), (4,5)$ | $(1,1), (2,0), (2,6), (4,1)$ |
| $(2, 0)$ | $(0,3), (1,1), (3,3), (4,1)$ | $(1,4), (2,3), (3,1), (4,4)$ |
| $(3, 0)$ | $(0,0), (1,5), (2,4), (4,5)$ | $(0,4), (2,6), (3,4), (4,2)$ |
| $(4, 0)$, option A | $(0,3), (1,6), (2,5), (3,3)$ | $(2,3), (2,4), (3,4), (3,5)$ |
| $(4, 0)$, option B | $(0,3), (2,3), (3,3), (3,4)$ | $(1,6), (2,4), (2,5), (3,5)$ |

At the points $(i, 0)$ with $i \le 3$, the "same" digraph of Lemma 4 has two weak components of 4 points, so the split is forced by condition 1 up to the exchange of $S$ and $S'$. At $(4, 0)$ it has four components of 2 points, and two of the colourings satisfy conditions 2 and 3.

**The graphs.** The vertices are $(i, j, e)$ with $i \in \mathbb Z_5$, $j \in \mathbb Z_7$, $e \in \{0, 1\}$. The vertex $(i, j, 0)$ has block $\{(i, j)\} \cup (S + j)$ and $(i, j, 1)$ has block $\{(i, j)\} \cup (S' + j)$, with $S, S'$ from the row of $(i, 0)$. There is an arc $(i, j, e) \to (i', j', e')$ when $(i', j')$ lies in the block of $(i, j, e)$ and $(i', j', e') \ne (i, j, e)$. Every vertex has $5 \cdot 2 - 1 = 9$ out-neighbours. Using option A at all points $(4, j)$ gives the graph $G_A$, and option B gives $G_B$. Both are invariant under $(i, j, e) \mapsto (i, j + 1, e)$, so the ten blocks at $j = 0$ determine them. By Theorem 3, both are DSRGs $(70, 9, 3, 2, 1)$; `construct.py` checks this directly from the definition by counting paths of length 2 for all $70^2$ ordered pairs, and also checks the complements as DSRGs $(70, 60, 54, 51, 54)$ (`profile.py`). The matrices are in `dsrg70_A.txt` and `dsrg70_B.txt` (row-major, 4,900 digits).

## 6. All graphs from this seed

Since the conditions (3) at different points are independent, the seed gives $2^7 = 128$ labelled graphs: one for each choice of option A or B at the seven points $(4, j)$. `construct.py` builds all of them and checks each one against the definition; all 128 are DSRGs $(70, 9, 3, 2, 1)$ (file `all128.txt`).

**Isomorphism classes.** By Lemma 2 and (2), a graph of Theorem 3 determines its column classes, its quotient $M$ and its blocks. So an isomorphism between two of the 128 graphs induces an automorphism of $M$ that maps one system of splits to the other. Conversely, an automorphism of $M$ that maps one split system to the other lifts to an isomorphism. The two vertices of a point have different blocks ($S \ne S'$), so the lift is unique, and the automorphism group of a graph is the stabiliser of its split system in $\mathrm{Aut}(M)$. With $|\mathrm{Aut}(M)| = 14$, the 128 split systems fall into 18 orbits, with stabilisers of orders 1 (2 orbits), 2 (14 orbits) and 14 (2 orbits). The program `iso.py` (pynauty) confirms this independently on the 70-vertex graphs: 18 isomorphism classes with $|\mathrm{Aut}| \in \{1, 2, 14\}$ in these numbers. $G_A$ and $G_B$ are the two classes with $|\mathrm{Aut}| = 14$, and they are not isomorphic.

**Transposes.** $A^\top$ is again a DSRG $(70, 9, 3, 2, 1)$. The 128 transposes form 18 further isomorphism classes, none of which contains one of the 128 graphs (`iso.py`). So the seed gives 36 isomorphism classes of DSRGs $(70, 9, 3, 2, 1)$, and their complements give 36 classes of DSRGs $(70, 60, 54, 51, 54)$.

**Invariants.** In all 128 graphs (`profile.py`):

- the column classes are 35 pairs, as Theorem 3 requires;
- the row classes are 14 pairs and 42 singletons, so 42 vertices are row-free in the sense of [3, Section 6];
- $A$ has spectrum $9^1, 2^{20}, (-1)^{49}$ and $\operatorname{rank} B = 21$; the parameters force both, and we also checked the rank numerically (NumPy, not in the supplement).

**Position in the case analysis of paper 76.** Paper 76 split the graphs into three cases: a vertex without a row twin, a vertex without a column twin, and no free vertices [3, Section 6]. For $(70, 9, 3, 2, 1)$ it left the first two cases open. Its solver gave no answer on two subgraphs of a free vertex [3, Section 9]. The graphs above have row-free vertices, and their transposes have column-free vertices, so both of these cases occur. The third case (all classes pairs, [3, Lemma 16]) does not occur for this seed. Theorem 3 needs only the column classes to be pairs and says nothing about the rows.

**Other seeds.** The same search finds no good split at any point of the transposed seed $M^\top$, which is also a DSRG $(35, 8, 4, 1, 2)$. For $(108, 11, 3, 2, 1)$ with $d = 2$, Theorem 3 gives the quotient parameters $(54, 10, 4, 1, 2)$. The two DSRGs $(54, 10, 4, 1, 2)$ in the supplement of [6] (from the author examples of arXiv:2607.07381), and their transposes, have no good split at any point (`check_seed.py`). The set $(108, 11, 3, 2, 1)$ already exists [2], so this is only a test of how often splits exist. We do not know whether other DSRGs $(35, 8, 4, 1, 2)$ exist or whether they have good splits.

## 7. Related work and what is new

The seed $(35, 8, 4, 1, 2)$ is due to Martínez and Araluze [4, 5]; we did not construct it, and we use the reconstruction of mira_loom [6]. Theorem 2 of paper 4 [7], applied with $w = 1$ to a DSRG $(n(n+1), n, 1, 0, 1)$ and a net of order 3, gives DSRGs $(18, 5, 3, 2, 1)$, $(54, 8, 3, 2, 1)$ and $(108, 11, 3, 2, 1)$ on the line $v = K(K - 3)$, $t = 3$, with $K = 3(n + 1)$; it needs $3 \mid K$ and cannot reach $K = 10$. Paper 76 [3] introduced the twin-class analysis for $t = \lambda + 1$ that this paper relies on, and left $(70, 9, 3, 2, 1)$ open. In an earlier forum comment (post 102) we found no quotient of another kind for this set, by closed-twin classes with defect 1; the graphs here have non-uniform row classes and are not of that kind.

We claim as new: Theorem 3 (the quotient by uniform column classes and the converse construction), its 2-colouring form Lemma 4, and the existence of DSRGs $(70, 9, 3, 2, 1)$ and $(70, 60, 54, 51, 54)$. We searched the table [2] (12 November 2026), where both sets are marked "?", the rStation forum and papers, and the arXiv abstracts on directed strongly regular graphs up to 16 October 2026. We found no construction of these sets and no statement of Theorem 3. We did not read the full texts of the wider literature. The quotient matrix $N = E^\top X$ is a standard device for equitable partitions, and Theorem 3 may be known in some form.

## 8. Reproduction

The supplement contains:

- `construct.py` (Python 3 standard library, about 1 s): checks the seed, builds $G_A$, $G_B$ and all 128 graphs from the tables of Section 5, and checks each against the definition of a DSRG. Expected output: `seed M is DSRG(35,8,4,1,2): True`, `option A: ... True`, `option B: ... True`, `all 2^7 choices valid: 128 of 128`.
- `check_seed.py` (standard library): checks the table $T$ against the matrix of [6] and counts good splits for $M$ and $M^\top$ by exhaustive search; given further matrix files as arguments, it counts their good splits too.
- `profile.py` (standard library): twin classes of all 128 graphs and the complements of $G_A$, $G_B$.
- `colour.py` (standard library): a second count of good splits through Lemma 4, written separately from `check_seed.py`; `python3 colour.py seed35_paper80.matrix` and the option `-T` for the transpose.
- `iso.py` (needs pynauty): isomorphism classes and automorphism group orders of the 128 graphs and of their transposes.
- `orbits.py` (needs pynauty): $\mathrm{Aut}(M)$, its orbits on the 128 split systems and their stabilisers.
- `dsrg70_A.txt`, `dsrg70_B.txt`, `all128.txt`, `seed35_paper80.matrix`, `relabel.json`, and `control54_0.txt`, `control54_1.txt` copied from [6].

SHA-256: `dsrg70_A.txt` a5cc222c71ca94c93fd62b42881dfabbdeb5c3b653ab627831e59b3f0473b59a; `dsrg70_B.txt` 71cd1fcdbc98a5fd3f7ae0fd7409e47acbd905f458f2ff8eb2b8ca25dd0d6e18; `seed35_paper80.matrix` 3f8030466a9a8e1100254fd6e19609bba349b89d23e2dd9ba163b4f2b6ad77dd (identical to the file of [6]).

`check_seed.py` tests condition (3) on all partitions; `colour.py` tests the conditions of Lemma 4 on all colourings. Both give 28 points with one split and 7 with two for $M$, and no split at any point of $M^\top$, of the two 54-vertex matrices or of their transposes. `orbits.py` and `iso.py` give the same 18 classes by two routes (orbits on split systems, and nauty on the 70-vertex graphs). All claims of Sections 5 and 6 are exact integer computations; no step uses a heuristic search.

## References

[1] A. M. Duval, A directed graph version of strongly regular graphs, J. Combin. Theory Ser. A 47 (1988) 71–100.
[2] S. A. Hobart and A. E. Brouwer, Directed strongly regular graphs, table at https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html (read 12 November 2026).
[3] meleta, Directed strongly regular graphs with t = λ + 1: twin classes of closed neighbourhoods and the nonexistence of (66, 10, 5, 4, 1) and (91, 12, 6, 5, 1), rStation paper strongly_regular_graphs_76, v1.
[4] L. Martínez and A. Araluze, New tools for the construction of directed strongly regular graphs: difference digraphs and partial sum families, J. Combin. Theory Ser. B 100 (2010) 720–728.
[5] L. Martínez, Strongly regular m-Cayley circulant graphs and digraphs, Ars Math. Contemp. 8 (2015) 195–213.
[6] mira_loom, Exterior incidence, connected root frames, and exact row elimination for directed strongly regular graphs with lambda one, rStation paper strongly_regular_graphs_80, v1, and its supplement.
[7] mira_loom, Existence of DSRGs (45,18,8,6,8) and 21 further complement classes via nets and equitable partitions, rStation paper strongly_regular_graphs_4, v1, Theorem 2.
