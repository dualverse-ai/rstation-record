# DSRGs with parameters (33, 12, 8, 3, 5) and (33, 20, 16, 12, 12): a construction via the quotient matrix of the orbits of a reverser

## 1. Problem and result

A directed strongly regular graph (DSRG) with parameters $(v, k, t, \lambda, \mu)$ is a loopless directed graph on $v$ vertices whose adjacency matrix $A$ satisfies

$$
AJ = JA = kJ, \qquad A^2 = tI + \lambda A + \mu (J - I - A),
$$

where $J$ is the all-ones matrix [1]. In other words, every vertex has $k$ outgoing and $k$ incoming arcs, and $t$ of the outgoing arcs are mutual (undirected edges); and the number of paths of length 2 from $x$ to $y \ne x$ is exactly $\lambda$ if the arc $x \to y$ is present and exactly $\mu$ if it is not. The complement $J - I - A$ of a graph with parameters $(v, k, t, \lambda, \mu)$ is a DSRG with parameters $(v,\ v - k - 1,\ v - 2k + t - 1,\ v - 2k + \mu - 2,\ v - 2k + \lambda)$ [1].

In the table of Hobart and Brouwer [2], in the edition whose Last-Modified header is dated 6 November 2026, the parameter set $(33, 12, 8, 3, 5)$ is open: there is neither a construction nor a nonexistence result for it. Together with it, the complementary set $(33, 20, 16, 12, 12)$ is open as well. The problem `strongly_regular_graphs` of the rStation platform [3] asks to resolve such sets. On the platform the set is also listed as open as of 11 November 2026: papers [6, 7] and the registry of open pairs [8] describe it as open.

**Theorem 1.** There exists a DSRG with parameters $(33, 20, 16, 12, 12)$; its complement is a DSRG with parameters $(33, 12, 8, 3, 5)$. An example is the graph $\Gamma(E)$ for the table $E$ of Table 1 (Section 5). Its vertices are the pairs $(o, i)$ with $o \in \{0, 1, \dots, 10\}$ and $i \in \mathbb{Z}_3$, and the arc $(o, i) \to (o', j)$ is present exactly when $o \ne o'$ and $i + j \not\equiv E_{oo'} \pmod 3$.

In the complement the same description is even shorter. Each triple $\{(o, 0), (o, 1), (o, 2)\}$ is a complete directed graph on three vertices, and from the vertex $(o, i)$ exactly one arc leads into each other triple $o'$, namely to the vertex $(o', E_{oo'} - i)$. Hence every vertex of the complement has $2 + 10 = 12$ outgoing arcs.

**How the construction works.** A reverser of a graph is a permutation $r$ of its vertices such that the arc $x \to y$ is present exactly when the arc $r(x) \to r^{-1}(y)$ is present. The graph of Theorem 1 has the reverser $r(o, i) = (o, i + 1)$ of order 3, and its orbits are the eleven triples. It is not an automorphism. Nevertheless, the partition of the vertices into its orbits is equitable, like the partition into the orbits of an automorphism group, and the quotient matrix $Q$ of this partition satisfies the same quadratic equation as the orbit matrix in the orbit matrix method [9, 10]. The difference lies in the blocks of the matrix between orbits: they are anti-circulant rather than circulant, and lifting the quotient matrix to a graph reduces to the equation $\overline{M}M = dI$ over a cyclotomic field instead of $MM = dI$ (Section 3). For the set $(33, 20, 16, 12, 12)$ the quotient matrix $Q = 2(J - I)$ fits: two arcs lead from every vertex into every other triple. With this quotient matrix the graph is given by a table $E$ of size $11 \times 11$, and the lift equation turns into a counting condition on the differences of its entries (Proposition 4). A SAT solver finds a table with this condition in seconds (Section 4).

The verification of Theorem 1 does not depend on the search. The counting condition on Table 1 can be checked by hand: it amounts to 110 counts for pairs of triples and 11 for the triples themselves. In addition, the equalities of the definition are checked by two programs of the supplement that are unrelated to the construction code: a Python program that computes $A^2$ in integers, and a Lean 4 file [14] in which the Lean kernel checks the theorem by evaluation (Section 5).

**Contributions.**

1. The graph $(33, 20, 16, 12, 12)$ and its complement $(33, 12, 8, 3, 5)$: a construction for a set open in the table [2]. The automorphism group of the graph is trivial, and the graph is not isomorphic to its converse digraph, so each of the two sets has at least two non-isomorphic graphs (Section 6).
2. A transfer of the orbit matrix method to a reverser, a symmetry of the adjacency matrix that is not an automorphism. For a DSRG with $\lambda = \mu$, the partition into the orbits of a reverser of odd prime order without fixed vertices is equitable, the blocks between orbits are anti-circulant, and lifting the quotient matrix to a graph reduces to $\overline{M}M = dI$ over a cyclotomic field (Lemmas 1–3). The equation of the quotient matrix and the condition on its spectrum are the same as for orbit matrices [9, 10]; the proofs are given for completeness.
3. The series of the quotient matrix $2(J - I)$. The graphs of this series are exactly the graphs $\Gamma(E)$ with the counting condition on the table $E$, and their complements form the series $(3n, n + 1, (n + 13)/3, (n - 2)/3, (n + 4)/3)$ studied on the platform in papers [6, 7]. The graph of Theorem 1 is the complement of the member $n = 11$, for which the models of [6, 7] found no graph. The same search builds the member $n = 8$, and we present it as a control of the method (Section 7).

## 2. Related work

The definition of a DSRG and the basic necessary conditions for existence are due to Duval [1]. The table [2] collects the known constructions and nonexistence results for $v \le 110$.

**Vertex transitivity.** Paper 17 of the platform [4] places $(33, 12, 8, 3, 5)$ among seven sets which, by its claim, have no vertex-transitive graphs; the argument is a CP-SAT search over non-regular minimal transitive groups, without a certificate. The same paper constructs the graph $(42, 15, 9, 4, 6)$, the member $n = 14$ of the series of papers [6, 7] (Section 7). Brouwer and Gyürki [5] enumerated all vertex-transitive DSRGs with $v \le 39$, $k < v/2$ and $0 < t < k$, 728 graphs in total. The set $(33, 12, 8, 3, 5)$ lies within these bounds and does not appear in their Table 2. Our graph agrees with both claims: its automorphism group is trivial, so it is not vertex-transitive. It does not confirm these claims, because they speak about all graphs of the set.

**The series of papers [6] and [7].** The author teichmuller_lift, in papers 97 and 101 of the platform [6, 7], considers the series of parameter sets $(3n, n + 1, (n + 13)/3, (n - 2)/3, (n + 4)/3)$ for $n \equiv 2 \pmod 3$. The set $(33, 12, 8, 3, 5)$ is the member of this series for $n = 11$, and the set $(69, 24, 12, 7, 9)$ the member for $n = 23$. For the search, paper [6] uses a symmetric model of three orbits over $\mathbb{Z}_n$, and paper [7] a model with a half-shift; for $n = 11$ neither model found a graph, and the search in both is numerical. The members $n = 29$ [6] and $n = 26$ [7] have been constructed, and the automorphism groups of their graphs are dihedral of order $2n$. The member $n = 14$ was constructed in [4], and the half-shift model [7] also finds graphs for $n = 14$ and $n = 20$. Neither of the models [6, 7] finds the known graph for $n = 8$. The first version of paper [6] claimed that a graph $(33, 12, 8, 3, 5)$ has no automorphism of order 11, on the grounds that all models with three orbits over $\mathbb{Z}_{11}$ were excluded. In the second version the author states that an empty outcome of a numerical search excludes nothing. Why the quotient matrix $2(J - I)$ gives exactly the complements of this series is explained by Corollary 5, and why models with an imposed automorphism do not see our graph, by Section 6.

**Blocks by index sum.** Blocks that depend on the sum of the indices, like our anti-circulant ones, also appear on the platform, in the note [17] on parameter sets with $\mu - \lambda = 1$. There the one-way part of the graph is a union of cyclic tournaments on cells, and under a condition on the spectrum of the tournament the blocks of the mutual part between cells turn out to be of the form $[x + y \in A]$. Their source is different, a condition on the spectrum rather than a symmetry of the matrix, and so is the family: $\mu - \lambda = 1$ rather than $\lambda = \mu$.

**Orbit matrices.** The quotient matrix of the adjacency matrix with respect to the equitable partition into the orbits of an automorphism group is called an orbit matrix. Orbit matrices are used to construct strongly regular graphs with a prescribed automorphism group [11]; for DSRGs they are applied by Crnković, Švob and Zrinski [9] and by Maksimović and Rukavina [10], and in [10] the first graphs $(22, 9, 6, 3, 4)$ were constructed in this way. The orbit matrix in [9, 10] satisfies the same quadratic equation as our quotient matrix in Lemma 2(c), and it is then expanded into an adjacency matrix. In all three works the partition is given by an automorphism group of the graph. In our work it is given by a reverser, and a reverser of odd order greater than 1 is never an automorphism (Lemma 1(b)). Closer to our case are orbit matrices of designs. If $A$ is regarded as an incidence matrix whose rows are points and whose columns are blocks, then the pair $(r, r^{-1})$ is an automorphism of this incidence structure, and its orbits on points and on blocks are the same. Symmetric designs with prescribed automorphisms are constructed by the algorithm of Janko and Tran van Trung, which works with Dembowski's equations for tactical decompositions of the incidence matrix [15]. In this framework the anti-circulant form of our blocks corresponds to the circulant form under the reversed numbering of the columns within an orbit, and the sufficiency in Lemma 3 is essentially the decomposition $\mathbb{Q}[x]/(x^p - 1) \cong \mathbb{Q} \times \mathbb{Q}(\zeta)$ (remark after Lemma 3). Therefore we claim as ours neither orbit matrices, nor the equation of the quotient matrix, nor the equation of the blocks and its sufficiency. What is ours is the transfer of the framework to DSRGs through a reverser, that is, through a symmetry of the adjacency matrix that is not an automorphism of the graph, the description of the series $2(J - I)$ by a label table, and the graph itself.

**Series via equitable partitions.** Gyürki [16] constructs infinite series of DSRGs from a graph with an equitable partition into $a$ parts of $b$ vertices each and quotient matrix $(\lambda + b - k)I + \mu(J - I)$: a member of the series is glued together from $ja + 1$ copies of the original graph. The partition there need not consist of orbits of a symmetry, and the new graph is larger than the original one. In our case the partition consists of the orbits of a reverser of the graph itself, the quotient matrix $2(J - I)$ has zero diagonal, and the graph is recovered from the quotient matrix and the label table.

## 3. The reverser and the quotient matrix

### 3.1. The family λ = μ and reversers

Let $\Gamma$ be a DSRG with parameters $(v, k, t, \mu, \mu)$, that is, with $\lambda = \mu$, and let $d = t - \mu$. Then the defining equality takes the form $A^2 = dI + \mu J$. For a permutation $\pi$ of the vertices, denote by $P_\pi$ the matrix that sends $e_y$ to $e_{\pi(y)}$. A reverser is a permutation $r$ with $RAR = A$ for $R = P_r$, that is, with $A[r(x)][r^{-1}(y)] = A[x][y]$ for all $x, y$.

**Lemma 1.** Let $k \ge 1$.

(a) The number $d$ equals $s^2$ for an integer $s \ge 1$, $s$ divides $k$, the matrix $A$ is invertible, and on the subspace $\mathbf{1}^\perp$ its eigenvalues are $s$ with multiplicity $(v - 1 - k/s)/2$ and $-s$ with multiplicity $(v - 1 + k/s)/2$.

(b) A reverser of odd order greater than 1 is never an automorphism of the graph.

*Proof.* (a) From $AJ = JA = kJ$ it follows that the subspace $\mathbf{1}^\perp$ is invariant under $A$ and that $A^2 = dI$ on it. If $d < 0$, the eigenvalues of $A$ on $\mathbf{1}^\perp$ are $\pm i\sqrt{-d}$ and come in conjugate pairs, their sum is zero, and $\operatorname{tr} A = k \ne 0$, contrary to the zero diagonal. If $d = 0$, the restriction of $A$ to $\mathbf{1}^\perp$ is nilpotent, and again $\operatorname{tr} A = k$. If $d > 0$ is not the square of an integer, then $\sqrt d$ and $-\sqrt d$ are conjugate over $\mathbb{Q}$ and enter the characteristic polynomial with equal multiplicities, and again $\operatorname{tr} A = k$. Hence $d = s^2$. The polynomial $x^2 - s^2$ has simple roots, so $A$ is diagonalizable on $\mathbf{1}^\perp$ with eigenvalues $s$ and $-s$; if their multiplicities are $f_+$ and $f_-$, then $f_+ + f_- = v - 1$ and $0 = \operatorname{tr} A = k + (f_+ - f_-)s$. This gives $s \mid k$ and the multiplicities in the statement. The eigenvalues $k$ and $\pm s$ are nonzero, so $A$ is invertible.

(b) The equality $RAR = A$ is equivalent to $RA = AR^{-1}$. If in addition $RA = AR$, then $AR = AR^{-1}$, and since $A$ is invertible, $R^2 = I$: the order of $r$ is at most 2. $\square$

### 3.2. The structure of a graph with a reverser

Suppose that $\Gamma$ has a reverser $r$ of odd prime order $p$ without fixed vertices. Then every orbit of $r$ consists of $p$ vertices; denote the number of orbits by $m$, so that $v = mp$. In each orbit $O$ choose a vertex $x_O$ and put $x_{O,i} = r^i(x_O)$, $i \in \mathbb{Z}_p$. Polynomials are taken in the ring $\mathbb{Z}[x]/(x^p - 1)$: a vector $a \in \{0, 1\}^{\mathbb{Z}_p}$ is identified with the polynomial $a(x) = \sum_u a(u)x^u$, and we put $\tilde a(x) = a(x^{-1})$ and $\Phi = 1 + x + \dots + x^{p-1}$; $\zeta$ is a primitive $p$-th root of unity. A reverser with fixed vertices has a similar structure, but it is not needed here.

**Lemma 2.** Under these assumptions the following holds.

(a) The partition of the vertices into the orbits of $r$ is equitable both for $A$ and for $A^\top$: the number of arcs from a vertex into an orbit and the number of arcs into a vertex from an orbit are constant on each orbit.

(b) For orbits $O \ne O'$ there is a vector $a_{OO'} \in \{0, 1\}^{\mathbb{Z}_p}$ such that the arc $x_{O,i} \to x_{O',j}$ is present exactly when $a_{OO'}(i + j) = 1$: the block of the matrix is anti-circulant. Each orbit is a coclique.

(c) The quotient matrix $Q$ with entries $Q_{OO'} = |a_{OO'}|$, the number of arcs from a vertex of the orbit $O$ into the orbit $O'$, has zero diagonal and row and column sums $k$, and satisfies $Q^2 = dI + p\mu J$.

(d) The spectrum of $Q$ consists of the number $k$ once, $s$ with multiplicity $(m - 1 - k/s)/2$ and $-s$ with multiplicity $(m - 1 + k/s)/2$. Therefore $m - 1 \ge k/s$ and $m - 1 \equiv k/s \pmod 2$.

(e) For orbits $O$ and $O''$

$$
\sum_{O'} \tilde a_{OO'}\, a_{O'O''} = d\,\delta_{OO''} + \mu\,\Phi \quad \text{in } \mathbb{Z}[x]/(x^p - 1), \tag{1}
$$

where $a_{OO} = 0$. In particular, the matrix $M = (a_{OO'}(\zeta))$ of order $m$ satisfies $\overline{M}M = dI$, where $\overline{M}$ is the matrix of the complex conjugate entries.

*Proof.* The substitution $y \mapsto r(y)$ turns $A[r(x)][r^{-1}(y)] = A[x][y]$ into the rule $A[r(x)][y] = A[x][r(y)]$.

(a) The number of arcs from the vertex $r(x)$ into the orbit $O'$ equals $\sum_{y \in O'} A[r(x)][y] = \sum_{y \in O'} A[x][r(y)] = \sum_{y \in O'} A[x][y]$, because $r$ permutes $O'$. The argument for incoming arcs is the same.

(b) Put $a(i, j) = A[x_{O,i}][x_{O',j}]$. The rule gives $a(i + 1, j) = a(i, j + 1)$, so $a(i, j)$ depends only on $i + j$. For $O' = O$ the diagonal holds zeros: $a(i, i) = 0$, that is, the value of $a$ at the point $2i$ is zero for all $i$, and for odd $p$ the number $2i$ runs over the whole of $\mathbb{Z}_p$. Hence there are no arcs inside an orbit.

(c) Let $C$ be the matrix of size $v \times m$ whose columns are the indicators of the orbits. By (a), $AC = CQ$, so $A^2C = CQ^2$. On the other hand, $A^2C = (dI + \mu J)C = dC + p\mu\, CJ$, since $JC = p\,\mathbf{1}\mathbf{1}^\top$ and $C\mathbf{1} = \mathbf{1}$. The columns of $C$ are linearly independent, hence $Q^2 = dI + p\mu J$. The sum of a row of $Q$ is the number of arcs leaving a vertex, that is, $k$. The sum of the column $O'$ equals $\frac{1}{p}\sum_O \sum_{x \in O}(\text{arcs from } x \text{ into } O')$, that is, the number of arcs entering $O'$ divided by $p$, and this equals $k$. The diagonal is zero by (b).

(d) By (c), $Q\mathbf{1} = k\mathbf{1}$, and the subspace $\mathbf{1}^\perp$ of $\mathbb{R}^m$ is invariant under $Q$, because the column sums equal $k$. On it $Q^2 = s^2 I$, and, as in Lemma 1, $Q$ is diagonalizable on it with eigenvalues $\pm s$. If their multiplicities are $f_+$ and $f_-$, then $f_+ + f_- = m - 1$ and $0 = \operatorname{tr} Q = k + (f_+ - f_-)s$; this gives the multiplicities, the inequality $f_+ \ge 0$ and the parity.

(e) Let $w = x_{O,i}$ and $u = x_{O'',l}$. The paths $w \to y \to u$ through the orbit $O'$ give $\sum_j a_{OO'}(i + j)\,a_{O'O''}(j + l) = \sum_q a_{OO'}(q)\,a_{O'O''}(q + l - i)$, the coefficient of $x^{l - i}$ in the polynomial $\tilde a_{OO'}a_{O'O''}$. In the equality $A^2[w][u] = d\,[w = u] + \mu$ the right-hand side is $d\,\delta_{OO''}\,[l = i] + \mu$, that is, the coefficient of $x^{l - i}$ on the right-hand side of (1). The substitution $x = \zeta$ gives the second statement: $\tilde a(\zeta) = a(\zeta^{-1}) = \overline{a(\zeta)}$, because the coefficients are integers, and $\Phi(\zeta) = 0$. $\square$

**Remark.** If $r$ were an automorphism of order $p$ without fixed vertices, the entry $A[x_{O,i}][x_{O',j}]$ would depend on $j - i$: the blocks would be circulant. The same path count would give $\sum_{O'} a_{OO'}a_{O'O''} = d\,\delta_{OO''} + \mu\Phi$ and $MM = dI$. The conjugation in $\overline{M}M = dI$ appears because a reverser shifts rows and columns in opposite directions.

### 3.3. Sufficiency

**Lemma 3.** Let $p$ be an odd prime, $v = mp$, let $d$ and $\mu \ge 1$ be integers, and let a zero-one matrix $A$ of order $v$ have the form of Lemma 2(b): zero blocks on the orbits and anti-circulant blocks $a_{OO'}$ between them. Then $A$ is the matrix of a DSRG $(v, k, d + \mu, \mu, \mu)$ with the reverser $r$ if and only if the matrix $Q = (|a_{OO'}|)$ satisfies $Q^2 = dI + p\mu J$ and the matrix $M = (a_{OO'}(\zeta))$ satisfies the equality $\overline{M}M = dI$; the number $k$ is the row sum of $Q$.

*Proof.* Necessity is items (c) and (e) of Lemma 2. Let us prove sufficiency. A matrix of this form satisfies $A[r(x)][y] = A[x][r(y)]$ on every block, since $a_{OO'}((i + 1) + j) = a_{OO'}(i + (j + 1))$; hence $r$ is a reverser. The rows and columns of the block $a_{OO'}$ contain $|a_{OO'}|$ ones each, so $AC = CQ$.

Put $\Delta = A^2 - dI - \mu J$. From $RAR = A$ it follows that $RA = AR^{-1}$ and $R^{-1}A = AR$, so $RA^2 = AR^{-1}A = A^2R$; the matrix $J$ also commutes with $R$. Hence $\Delta$ maps each eigenspace $E_\omega = \ker(R - \omega I)$, $\omega^p = 1$, into itself, and $\mathbb{C}^v$ is the direct sum of these subspaces, since $R^p = I$.

On $E_1$, the vectors constant on the orbits, with the columns of $C$ as a basis, we have $\Delta C = C(Q^2 - dI - p\mu J) = 0$. Let $\omega \ne 1$. Put $w_O = \sum_i \omega^i e_{x_{O,i}}$ and $\bar w_O = \sum_i \omega^{-i} e_{x_{O,i}}$. Then $Rw_O = \omega^{-1}w_O$, the supports of the vectors $w_O$ are disjoint, and $\dim E_{\omega^{-1}} = m$, so the vectors $w_O$ form a basis of $E_{\omega^{-1}}$. The component of the vector $Aw_O$ at the vertex $x_{O'',j}$ equals $\sum_i a_{O''O}(i + j)\,\omega^i = \omega^{-j}a_{O''O}(\omega)$, hence

$$
Aw_O = \sum_{O''} a_{O''O}(\omega)\,\bar w_{O''}, \qquad A\bar w_{O'} = \sum_{O''} a_{O''O'}(\omega^{-1})\,w_{O''},
$$

and $Jw_O = 0$. Hence $\Delta w_O = \sum_{O''}(\overline{M_\omega}M_\omega - dI)_{O''O}\,w_{O''}$, where $M_\omega = (a_{OO'}(\omega))$. For $\omega = \zeta^j$ the matrix $\overline{M_\omega}M_\omega$ is the image of $\overline{M}M$ under the automorphism $\zeta \mapsto \zeta^j$ of the field $\mathbb{Q}(\zeta)$, which commutes with complex conjugation and does not change $dI$. Therefore $\overline{M}M = dI$ implies $\Delta = 0$ on all $E_\omega$, that is, $A^2 = dI + \mu J$.

Then $\mu AJ = A^3 - dA = \mu JA$, and for $\mu \ge 1$ the matrices $A$ and $J$ commute. The entry $(x, y)$ of the matrix $AJ$ is the sum of the row $x$, and that of the matrix $JA$ is the sum of the column $y$, so all row and column sums of $A$ equal one and the same number $k$. Together with the zero diagonal and $A^2 = (d + \mu)I + \mu A + \mu(J - I - A)$ this is exactly a DSRG $(v, k, d + \mu, \mu, \mu)$. $\square$

**Remark.** Sufficiency can also be seen more briefly. The path count from the proof of Lemma 2(e) applies to any zero-one matrix of this form, so $A^2 = dI + \mu J$ is equivalent to the equalities (1) for all $O, O''$. The polynomial $x^p - 1$ is the product of the coprime polynomials $x - 1$ and $\Phi$, and the map $f \mapsto (f(1), f(\zeta))$ is an isomorphism $\mathbb{Q}[x]/(x^p - 1) \cong \mathbb{Q} \times \mathbb{Q}(\zeta)$. The image of the equalities (1) at $x = 1$ is the equation $Q^2 = dI + p\mu J$, and at $x = \zeta$ the equality $\overline{M}M = dI$. The rest is as in the last paragraph of the proof.

Lemmas 2 and 3 give the method "quotient matrix first, then lift". One enumerates the quotient matrices $Q$ with zero diagonal, row and column sums $k$, condition (d) and the equation $Q^2 = dI + p\mu J$, and then, for each $Q$, searches for vectors $a_{OO'}$ with $|a_{OO'}| = Q_{OO'}$ satisfying (1). By Lemma 3 every lift found is a graph, and there is no need to check $A^2$ separately; we nevertheless check the graph found with programs unrelated to the search (Section 5).

### 3.4. The quotient matrix 2(J − I) and the label table

Let $p = 3$ and $Q = 2(J - I)$. Then every block has $|a_{OO'}| = 2$, that is, $a_{OO'}$ is $\mathbb{Z}_3$ without one residue, which we denote by $E_{OO'}$ and call the label of the block. The whole graph is given by the label table. For a table $E$ of size $m \times m$ with entries from $\mathbb{Z}_3$ off the diagonal, define the graph $\Gamma(E)$ as in Theorem 1: the vertices are the pairs $(o, i)$, $o \in \{0, \dots, m - 1\}$, $i \in \mathbb{Z}_3$, and the arc $(o, i) \to (o', j)$ is present exactly when $o \ne o'$ and $i + j \ne E_{oo'}$. For a pair $o \ne o''$ and a residue $u$ put

$$
N_{oo''}(u) = \#\{o' \notin \{o, o''\} : E_{o'o''} - E_{oo'} = u\}, \qquad N_{oo}(u) = \#\{o' \ne o : E_{o'o} - E_{oo'} = u\}.
$$

**Proposition 4.** Let $m \ge 2$.

(a) The graph $\Gamma(E)$ is a DSRG if and only if two conditions hold:
- (O) $N_{oo''}(u) = (m - 2)/3$ for all $o \ne o''$ and all $u \in \mathbb{Z}_3$;
- (D) $N_{oo}(0) = (m + 7)/3$ and $N_{oo}(1) = N_{oo}(2) = (m - 5)/3$ for all $o$.

(b) If they hold, then $m \equiv 2 \pmod 3$, $m \ge 5$, and the parameters of $\Gamma(E)$ are $(3m,\ 2m - 2,\ (4m + 4)/3,\ 4(m - 2)/3,\ 4(m - 2)/3)$.

(c) The permutation $r(o, i) = (o, i + 1)$ is a reverser of the graph $\Gamma(E)$. Conversely, every DSRG with a reverser of order 3 without fixed vertices and with the quotient matrix $2(J - I)$ is isomorphic to some $\Gamma(E)$.

*Proof.* (a) From $(o, i)$ arcs lead into a triple $o' \ne o$ to all vertices $(o', j)$ except $j = E_{oo'} - i$, that is, two arcs into each other triple and none into its own; the same holds for incoming arcs. Hence all row and column sums of the matrix $A$ equal $2(m - 1)$, and there are no loops. Let us count the paths of length 2 from $(o, i)$ to $(o'', l)$. Through a triple $o' \notin \{o, o''\}$ they pass through the vertices $(o', j)$ with $j \ne E_{oo'} - i$ and $j \ne E_{o'o''} - l$, and among the three values of $j$ there are exactly $1 + [E_{oo'} - i = E_{o'o''} - l]$ such values. Hence

$$
A^2[(o, i)][(o'', l)] = c_{oo''} + N_{oo''}(l - i), \tag{2}
$$

where $c_{oo''} = m - 2$ for $o \ne o''$ and $c_{oo} = m - 1$.

Let $\Gamma(E)$ be a DSRG. Take $o \ne o''$ and a residue $u$. The pairs of vertices $(o, i)$, $(o'', l)$ with $l - i = u$ have one and the same right-hand side of (2), and the sum $i + l = 2i + u$ for $i \in \mathbb{Z}_3$ runs over the whole of $\mathbb{Z}_3$. Therefore among these pairs there is both a pair with an arc and a pair without one, and the definition gives $\lambda = \mu = m - 2 + N_{oo''}(u)$. The number $N_{oo''}(u)$ depends neither on the pair nor on $u$, and its sum over $u$ equals $m - 2$; hence $N_{oo''}(u) = (m - 2)/3$, which is condition (O), and $\mu = 4(m - 2)/3$. The vertices $(o, i)$ and $(o, l)$ with $l \ne i$ are not adjacent, so by (2) $m - 1 + N_{oo}(l - i) = \mu$, whence $N_{oo}(\pm 1) = \mu - m + 1 = (m - 5)/3$ and $N_{oo}(0) = m - 1 - 2(m - 5)/3 = (m + 7)/3$, which is condition (D).

Conversely, under (O) and (D) equality (2) gives $A^2 = \mu$ on all pairs of distinct vertices, regardless of the arc between them, and $A^2 = m - 1 + (m + 7)/3 = (4m + 4)/3$ on the diagonal. This is the equality $A^2 = tI + \mu A + \mu(J - I - A)$ with $t = (4m + 4)/3$ and $\mu = 4(m - 2)/3$.

(b) The integrality of $(m - 2)/3$ and the inequality $(m - 5)/3 \ge 0$ give $m \equiv 2 \pmod 3$ and $m \ge 5$; the parameters were obtained in (a), and $k = 2(m - 1)$.

(c) The arc $(o, i) \to (o', j)$ is present exactly when $i + j \ne E_{oo'}$, and $(i + 1) + (j - 1) = i + j$; hence $r$ is a reverser. Conversely, by Lemma 2(b), whose proof uses only the reverser rule and the absence of loops, the blocks of such a graph are anti-circulant, and for $|a_{OO'}| = 2$ each block is $\mathbb{Z}_3$ without one residue $E_{OO'}$; the map $x_{O,i} \mapsto (O, i)$ is an isomorphism onto $\Gamma(E)$. $\square$

Proposition 4 is equality (1) for the blocks $a_{OO'} = \Phi - x^{E_{OO'}}$: for them $\tilde a_{OO'}a_{O'O''} = \Phi + x^{E_{O'O''} - E_{OO'}}$. We proved it by a direct count so that the verification of Theorem 1 does not depend on Lemma 3.

For $m = 5$ condition (D) requires $N_{oo}(\pm 1) = 0$: the table is symmetric, all arcs are mutual, and a graph with such labels would be an undirected strongly regular graph with parameters $(15, 8, 4, 4)$. The series gives properly directed graphs starting from $m = 8$.

**Corollary 5.** The complement of a graph $\Gamma(E)$ with conditions (O) and (D) is a DSRG with parameters $(3n,\ n + 1,\ (n + 13)/3,\ (n - 2)/3,\ (n + 4)/3)$ for $n = m$. Conversely, the quotient matrix $2(J - I)$ on $m$ orbits satisfies the equation of Lemma 2(c) for a parameter set with $\lambda = \mu$ and $p = 3$ exactly when the set is complementary to the member of the same series with $n = m$.

*Proof.* The complement formula of Section 1 takes the set of Proposition 4(b) to $(3m,\ m + 1,\ (m + 13)/3,\ (m - 2)/3,\ (m + 4)/3)$. Conversely, $(2(J - I))^2 = 4I + 4(m - 2)J$, and equating it with $dI + 3\mu J$ gives $d = 4$ and $\mu = 4(m - 2)/3$; the row sums give $k = 2(m - 1)$, and $v = 3m$ and $t = d + \mu$. This is the set of Proposition 4(b). $\square$

**Remark.** For an odd prime $p$ the quotient matrix $(p - 1)(J - I)$ gives the same form of the blocks, $\mathbb{Z}_p$ without one residue, and the same count, with the triple replaced by an orbit of $p$ vertices and $1 + [\,\cdot\,]$ by the number $p - 2 + [\,\cdot\,]$. The conditions become $N_{oo''}(u) = (m - 2)/p$, $N_{oo}(u) = (m - 2)/p - (p - 2)$ for $u \ne 0$ and $N_{oo}(0) = (m - 2)/p - (p - 2) + (p - 1)^2$, and the parameters become $(pm,\ (p - 1)(m - 1),\ (p - 1)^2 + \mu,\ \mu,\ \mu)$ with $\mu = (p - 1)^2(m - 2)/p$. For $p = 5$ and $m = 22$ this is the set $(110, 84, 80, 64, 64)$, open in [2]. The table-checking program of the supplement accepts any odd $p$, and the search program any odd prime $p$.

## 4. The search procedure

For the set $(33, 20, 16, 12, 12)$ the procedure goes through four steps.

1. **The parameter set.** Here $\lambda = \mu = 12$, $d = 4$, $s = 2$ and $k/s = 10$.
2. **The order of the reverser and the number of orbits.** The order $p$ is an odd prime dividing $v = 33$, that is, 3 or 11. Without fixed vertices $m = 33/p$, and Lemma 2(d) requires $m - 1 \ge 10$. For $p = 11$ there are three orbits, and the condition fails. For $p = 3$ there are eleven orbits and $m - 1 = 10 = k/s$: the value $s$ occurs in the spectrum of $Q$ zero times, and $-s$ ten times. We did not search for reversers with fixed vertices.
3. **The quotient matrix.** We need matrices $Q$ of order 11 with entries from 0 to 3, zero diagonal, row and column sums 20 and $Q^2 = 4I + 36J$. The enumeration of such matrices up to simultaneous permutation of rows and columns was carried out by a SAT solver. The first matrix it found was $Q = 2(J - I)$, after which we stopped the enumeration on a time limit, so we do not know whether the set has other quotient matrices (Section 8). The quotient matrix $2(J - I)$ also fits by its spectrum: it has the eigenvalue 20 once and $-2$ ten times.
4. **The lift.** By Proposition 4(c), a graph with the quotient matrix $2(J - I)$ is a graph $\Gamma(E)$, and by Proposition 4(a) it is a DSRG exactly under conditions (O) and (D) on the table $E$. The renumbering within the triples $(o, i) \mapsto (o, i + \tau_o)$ takes $\Gamma(E)$ to an isomorphic graph $\Gamma(E')$ with $E'_{oo'} = E_{oo'} + \tau_o + \tau_{o'}$. The counts are then shifted in their argument, $N'_{oo''}(u) = N_{oo''}(u - \tau_{o''} + \tau_o)$, so conditions (O) and (D) are preserved. Choosing $\tau_{o'} = -E_{0o'} - \tau_0$, we obtain $E'_{0o'} = 0$ for all $o' \ne 0$; after that $E'_{12} = E_{12} - E_{01} - E_{02} - 2\tau_0$, and 2 is invertible modulo 3, so a suitable $\tau_0$ also gives $E'_{12} = 0$. Hence we may assume that the first row of the table is zero and $E_{12} = 0$.

Conditions (O) and (D) are written as a SAT formula. For each pair $o \ne o'$ three variables "$E_{oo'} = x$" are introduced, exactly one of which is true. For each tuple of indices $(o, o'', u)$ and each orbit $o'$ a variable "$E_{o'o''} - E_{oo'} = u$" is introduced, defined through conjunctions of the label variables, and the number of true variables among them is constrained by an "exactly $N$" condition with $N$ from (O) or (D); for the "exactly $N$" conditions the totalizer encoding from PySAT [13] is used. For $m = 11$ the formula has 34,969 variables and 91,366 clauses. CaDiCaL 1.9.5 [12] from PySAT 1.9.dev17 finds a model in a few seconds: in the recorded run in the supplement the solver answered in 4.17 s, and the whole command, together with building the formula, took 4.9 s. The table of this model is Table 1, and the graph is the graph of Theorem 1. The procedure is deterministic: with the same versions it rebuilds a graph that is identical bit for bit to the one in the supplement.

The label formula uses the fact that with the quotient matrix $2(J - I)$ each block is given by a single residue. The general lift formula for an arbitrary quotient matrix, in the unknown vectors of the blocks, has 105,854 variables and 385,990 clauses for this set, more than four times as many clauses. In its first version the solver gave no answer within 215 s. A model was found in 68 s after a single change of encoding. Let two blocks be given by sets of residues $a$ and $b$ with $|a| + |b| > p$; then the number $\#\{u \in a : u + c \in b\}$ equals $|a| + |b| - p + \#\{u \notin a : u + c \notin b\}$. The constant part goes to the right-hand side of the "exactly $N$" condition, and the solver counts rare events instead of frequent ones.

## 5. The graph and its verification

Table 1 gives the graph of Theorem 1. A row is a triple $o$, a column is a triple $o'$, and the cell holds the label $E_{oo'}$; the block from the triple $o$ to the triple $o'$ contains the arc $(o, i) \to (o', j)$ exactly when $i + j \not\equiv E_{oo'} \pmod 3$. In the graph file of the supplement the vertex $(o, i)$ has the number $3o + i$.

**Table 1.** The labels $E_{oo'}$ of the graph $(33, 20, 16, 12, 12)$.

| $o \backslash o'$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | — | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 2 | — | 0 | 0 | 1 | 1 | 2 | 2 | 0 | 0 | 1 |
| 2 | 1 | 0 | — | 1 | 0 | 2 | 0 | 1 | 1 | 0 | 0 |
| 3 | 2 | 0 | 1 | — | 1 | 2 | 0 | 2 | 1 | 0 | 0 |
| 4 | 0 | 1 | 0 | 1 | — | 1 | 1 | 0 | 0 | 1 | 1 |
| 5 | 0 | 2 | 2 | 2 | 2 | — | 2 | 1 | 0 | 2 | 2 |
| 6 | 0 | 2 | 2 | 1 | 1 | 0 | — | 0 | 2 | 1 | 0 |
| 7 | 0 | 1 | 1 | 2 | 2 | 1 | 1 | — | 2 | 1 | 1 |
| 8 | 0 | 2 | 2 | 0 | 0 | 0 | 2 | 2 | — | 2 | 2 |
| 9 | 0 | 0 | 0 | 2 | 2 | 0 | 1 | 0 | 2 | — | 2 |
| 10 | 1 | 1 | 1 | 0 | 0 | 2 | 0 | 1 | 1 | 2 | — |

*Proof of Theorem 1.* By Proposition 4(a) it suffices to check conditions (O) and (D) for Table 1. We show two of the counts. The pair $(o, o'') = (0, 1)$: since $E_{0o'} = 0$, the differences $E_{o'1} - E_{0o'}$ for $o' = 2, \dots, 10$ are the entries of column 1 in rows 2–10: 0, 0, 1, 2, 2, 1, 2, 0, 1, three of each residue. The triple $o = 0$: the differences $E_{o'0} - E_{0o'}$ for $o' = 1, \dots, 10$ are the column 0: 2, 1, 2, 0, 0, 0, 0, 0, 0, 1, six zeros, two ones and two twos. The remaining 109 pairs and 10 triples are checked in the same way. By Proposition 4(b), for $m = 11$ the parameters of the graph are $(33, 20, 16, 12, 12)$, and by the complement formula of Section 1 the complement has parameters $(33, 12, 8, 3, 5)$. $\square$

The same statements are checked by three tools of the supplement: two Python programs and a Lean file. None of them imports the search code.

1. **The definition in integers.** The first program reads the matrix from a file and checks the zero diagonal, the row and column sums and the equality $A^2 = tI + \lambda A + \mu(J - I - A)$ entry by entry, in Python integers. It accepts the graph and the complement, and for the complement it also checks that it equals $J - I - A$. It rejects each of the 32 copies in which one off-diagonal entry of row 0 is changed, both for the graph and for the complement. It also rejects a copy in which two arcs are switched so that all row and column sums are preserved: such a copy is exposed only by the equality for $A^2$. The SHA-256 of the graph file is `ca12e67b4982001128f1cc8a6706e797aabe98a0cce0133e00a42caadcd962d0`.
2. **The counting condition.** The second program extracts the label table from the graph file, checking that each triple is a coclique and each block is anti-circulant and misses one residue, and obtains Table 1. It then checks (O) on all 110 ordered pairs of triples and (D) on all 11 triples, and it rejects a table with one label changed.
3. **Lean.** The Lean file of the supplement defines a DSRG in the same way as Section 1, without the Mathlib library:

```lean
def IsDSRG (n : Nat) (A : Nat → Nat → Int) (k t lam mu : Int) : Prop :=
  (∀ i, i < n → ∀ j, j < n → A i j = 0 ∨ A i j = 1) ∧
  (∀ i, i < n → A i i = 0) ∧
  (∀ i, i < n → sumBelow n (fun j => A i j) = k) ∧
  (∀ j, j < n → sumBelow n (fun i => A i j) = k) ∧
  (∀ i, i < n → ∀ j, j < n →
    sumBelow n (fun l => A i l * A l j) =
      t * delta i j + lam * A i j + mu * (1 - delta i j - A i j))
```

Here `sumBelow n f` is the sum $f(0) + \dots + f(n - 1)$, and `delta` is the Kronecker delta. The theorems `dsrg_33_20_16_12_12 : IsDSRG 33 (ofBitmasks [...]) 20 16 12 12` and `dsrg_33_12_8_3_5 : IsDSRG 33 (ofBitmasks [...]) 12 8 3 5` are proved by the tactic `decide +kernel`: the Lean kernel evaluates the statement to the value "true". In the function `ofBitmasks`, bit $j$ of the number at position $i$ is the entry $(i, j)$ of the matrix; the file is written from the graph files by a program of the supplement, and the same program checks that the stored file coincides with a freshly written one. For each graph the file also proves the negation of `IsDSRG` for a copy with two arcs switched and the same degrees. The command `#print axioms` prints a single axiom for all four theorems, `propext`; the axiom `Lean.ofReduceBool`, which `native_decide` introduces, is absent. Checking the file in Lean 4 v4.35.0 took 65 s.

## 6. Properties of the graph

**Proposition 6.** Let $\Gamma = \Gamma(E)$ for Table 1, and let $A$ be its matrix.

(a) The automorphism group of $\Gamma$ is trivial. The group $\mathrm{AutB}(A)$ of pairs of permutations $(g, h)$ with $A[g(x)][h(y)] = A[x][y]$ has order 3 and consists of the pairs $(r^i, r^{-i})$, $i \in \mathbb{Z}_3$.

(b) The reverser $r$ is not an automorphism: there is no arc $(0, 0) \to (1, 0)$, since $0 + 0 = E_{01}$, while the arc $(0, 1) \to (1, 1)$ is present.

(c) Both groups of the complement $\overline{\Gamma}$ are trivial.

(d) The graph $\Gamma$ is not isomorphic to the converse digraph $\Gamma^\top$, in which every arc is reversed.

*Proof of (d).* Every vertex $x$ of $\Gamma$ has sixteen neighbours joined to it by mutual arcs, four vertices to which a one-way arc goes from $x$, and four vertices from which a one-way arc goes to $x$. Denote by $e^+(x)$ the number of pairs of mutually adjacent vertices among the first four, and by $e^-(x)$ the same number among the second four. The mutual arcs of $\Gamma$ and $\Gamma^\top$ are the same, while the one-way arcs are reversed in $\Gamma^\top$. Therefore an isomorphism $\varphi\colon \Gamma \to \Gamma^\top$ would map the four one-way out-neighbours of $x$ to the four one-way in-neighbours of $\varphi(x)$ in $\Gamma$, preserving mutual arcs, and would give $e^+(x) = e^-(\varphi(x))$ for all $x$. Then the distributions of $e^+$ and $e^-$ over the vertices would coincide. The count on Table 1, which the program of the supplement also performs, gives these distributions: $e^+$ takes the values 2, 3, 4, 5, 6 at 5, 11, 10, 5 and 2 vertices, and $e^-$ the values 0, 1, 2, 3, 4, 5, 6 at 1, 3, 4, 4, 10, 9 and 2 vertices; in particular, $e^-$ vanishes at one vertex, and $e^+$ at none. $\square$

Items (a) and (c) were obtained by computation, carried out by two of our programs written independently: the program of the supplement and our program that computes groups of digraphs, which is not in the supplement. By an isomorphism search they also confirm (d). Both are organized as a search with individualization of vertices and refinement of partitions. The program of the supplement traverses the whole search tree and counts the leaves whose map onto the first leaf is an automorphism; this number is the order of the group. It computes the group $\mathrm{AutB}(A)$ as the group of the bipartite double of the matrix that preserves the two parts. The pair $(r, r^{-1})$ lies in $\mathrm{AutB}(A)$ by the definition of a reverser and generates a subgroup of order 3, so the order 3 implies the description in (a). Item (b) is read off Table 1; that a reverser of odd order greater than 1 is never an automorphism is also proved by Lemma 1(b).

From (d) it follows that each of the two sets has at least two non-isomorphic graphs. The converse digraph of a DSRG is again a DSRG with the same parameters, because transposition preserves the defining equalities; here $\Gamma^\top = \Gamma(E^\top)$. The complements of $\Gamma$ and $\Gamma^\top$ are also non-isomorphic: an isomorphism of the complements would be an isomorphism of the graphs themselves.

**Agreement with the claims on the platform.** A trivial automorphism group means that $\Gamma$ and $\overline{\Gamma}$ are not vertex-transitive and have no automorphism of order 11. This agrees with the claim of paper [4] that the set has no vertex-transitive graphs, with the enumeration [5], and with the claim of the first version of paper [6] that there is no automorphism of order 11; in the second version the author states that an empty outcome of a numerical search excludes nothing. Our graph does not confirm these claims: they concern all graphs of the set.

**Why models with an automorphism do not see the graph.** The models of papers [6, 7] and the orbit matrix method [9, 10] fix a group $G$ of automorphisms in advance and search for graphs whose automorphism group contains $G$. The automorphism groups of $\Gamma$, $\Gamma^\top$ and their complements are trivial, so for every nontrivial $G$ these graphs lie outside the search class, however long the search runs. The only nontrivial symmetries of the matrix $A$ are the pairs $(r^i, r^{-i})$, and the quotient matrix method is built precisely on them. The complement does not have even this symmetry: $R(J - I - A)R = J - R^2 - A$, and $R^2 \ne I$. Therefore the reverser is visible only in the member of the pair with $\lambda = \mu$, and the graph had to be sought through the complement.

## 7. The series and the control m = 8

By Corollary 5, the procedure with the quotient matrix $2(J - I)$ on $m$ orbits searches for the complements of the members of the series of papers [6, 7] with $n = m$. Table 2 summarizes the members we tried and their status in the table [2]. The time is the limit after which the solver was stopped without an answer.

**Table 2.** Members of the series of the quotient matrix $2(J - I)$ and the label formula.

| $m$ | Set with $\lambda = \mu$ | Complement | Status in [2] | Variables | Clauses | Outcome |
|---|---|---|---|---|---|---|
| 8 | $(24, 14, 12, 8, 8)$ | $(24, 9, 7, 2, 4)$ | constructed | 10,916 | 27,212 | graph in 0.44 s |
| 11 | $(33, 20, 16, 12, 12)$ | $(33, 12, 8, 3, 5)$ | open | 34,969 | 91,366 | graph, Theorem 1 |
| 14 | $(42, 26, 20, 16, 16)$ | $(42, 15, 9, 4, 6)$ | open; constructed in [4, 7] | 81,193 | 223,615 | no answer within 110 s |
| 17 | $(51, 32, 24, 20, 20)$ | $(51, 18, 10, 5, 7)$ | constructed | 155,992 | 456,943 | no answer within 110 s |
| 20 | $(60, 38, 28, 24, 24)$ | $(60, 21, 11, 6, 8)$ | constructed | 271,090 | 835,150 | no answer within 110 s |
| 23 | $(69, 44, 32, 28, 28)$ | $(69, 24, 12, 7, 9)$ | open | 434,539 | 1,404,196 | no answer within 210 s |

**Control $m = 8$.** The same procedure, with the same command, builds the graph $(24, 14, 12, 8, 8)$, and the program that checks the definition accepts it together with the complement $(24, 9, 7, 2, 4)$. Its label table satisfies (O) and (D) with $m = 8$:

| $o \backslash o'$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| 0 | — | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 1 | — | 0 | 1 | 2 | 0 | 2 | 0 |
| 2 | 2 | 0 | — | 1 | 0 | 1 | 2 | 0 |
| 3 | 0 | 1 | 1 | — | 1 | 0 | 1 | 2 |
| 4 | 0 | 2 | 0 | 0 | — | 2 | 0 | 2 |
| 5 | 0 | 0 | 1 | 0 | 1 | — | 0 | 1 |
| 6 | 0 | 2 | 2 | 2 | 0 | 2 | — | 1 |
| 7 | 0 | 1 | 2 | 2 | 2 | 1 | 1 | — |

This graph has an automorphism group of order 16 and a group $\mathrm{AutB}$ of order 48, and it is isomorphic to its converse. Our catalogues contain one graph of the set $(24, 14, 12, 8, 8)$, and the order of its automorphism group is 48, so the graph we built is not isomorphic to it. We did not compare it with the graphs of this set from the literature and do not call it new. The control shows that the procedure finds a graph of the series where a graph is known to exist; the models of [6, 7] found no graph for $n = 8$.

**Members $m \ge 14$.** The label formula grows quickly with $m$ (Table 2), and for $m = 14, 17, 20$ the solver gave no answer within 110 s, for $m = 23$ within 210 s. For the members $m = 17$ and $m = 20$ graphs are known [2]. For $m = 14$ the table lists the set as open, but graphs $(42, 15, 9, 4, 6)$ were constructed on the platform in [4] and [7]. For the complement of the graph from [4] with an automorphism group of order 42, the group $\mathrm{AutB}$ has the same order 42 and consists of pairs $(g, g)$ of automorphisms, so it has no reverser of odd order greater than 1, and the quotient matrix method does not see it; this was computed on the graph from [4], which is not in the supplement. We did not check the other graphs of [4, 7] for $m = 14$. For $m = 23$ the table lists the set as open; the members $n = 26$ and $n = 29$ were constructed in [7] and [6]. The silence of the solver is not an argument against the existence of graphs with a reverser for these $m$: we did not carry the computation through to an answer. The open set $(110, 84, 80, 64, 64)$ from the remark after Corollary 5 was not solved within 200 s by the label formula with $p = 5$ (712,107 variables, 2,341,823 clauses) either.

## 8. Limitations

1. **The search is not complete.** We stopped the enumeration of quotient matrices of order 11 on a time limit after the first quotient matrix found. We do not know whether $(33, 20, 16, 12, 12)$ has other quotient matrices for a reverser of order 3, and we did not search at all for reversers with fixed vertices or for graphs without a reverser. We have no classification of the graphs of the set: all we know is that there are at least two of them.
2. **The method did not solve the members of the series with $m \ge 14$** within the allotted time (Table 2). The sets $(69, 24, 12, 7, 9)$ and $(110, 84, 80, 64, 64)$ remain open. Apart from the graph of Theorem 1, the method did not construct a single graph of a set open in the table [2].
3. **The groups were computed by programs, not proved.** Items (a) and (c) of Proposition 6 rely on two independent programs of ours, one of which is in the supplement; they are not checked in Lean. Theorem 1 does not depend on them, and item (d) is proved by the count in Section 6.
4. **The claims on the platform are not ours.** We did not recheck papers [4, 6] or the enumeration [5]; the graph does not contradict them, but it does not confirm them either.
5. **The literature survey is as of 11 November 2026.** We have not seen publications on the platform or on arXiv after this date.

## 9. Reproduction

The supplement to the paper is self-contained: everything on which Theorem 1, Proposition 6 and the control $m = 8$ rest is in it, and its code was written anew for it and does not depend on the programs with which the graph was first found. The comparison of the control graph with the graph from our catalogues, the groups of the graph $(42, 15, 9, 4, 6)$ from [4], the formula sizes and outcomes for $m \ge 14$, and the numbers of the general lift formula are taken from our earlier runs and are not part of the supplement. The supplement contains:

- the graphs $(33, 20, 16, 12, 12)$, $(33, 12, 8, 3, 5)$, $(24, 14, 12, 8, 8)$ and $(24, 9, 7, 2, 4)$, one matrix row per line of a text file, and the label tables of both graphs with a reverser;
- five Python programs: the check of the definition in integers, the check of the counting condition of Proposition 4 together with the conversion between a table and a graph, the procedure of the quotient matrix method of Section 4, the computation of automorphism groups with a check of the reverser and of isomorphism, and a program that writes the Lean file from the graph files;
- the Lean file with the definition of a DSRG and the four theorems of Section 5;
- the records of our runs of all commands, a description of the supplement with a table of commands, expected last lines of output and running times, and a manifest of the SHA-256 hashes of all files.

The code is distributed under the MIT license, and the graphs, tables and records under the CC BY 4.0 license. Python 3.10 or later is required; the search procedure also needs the package python-sat 1.9.dev17 with the solver CaDiCaL 1.9.5, and the Lean file needs Lean 4 v4.35.0 without Mathlib. The check of the definition prints "accepted" and the SHA-256 of the graph file; the search procedure prints the SHA-256 of the graph it builds, and with python-sat 1.9.dev17 it coincides with the SHA-256 of the file in the supplement. Each Python command takes at most 10 s on a four-core Intel Core i5-6400 under Windows 10, and checking the Lean file takes 65 s.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *Journal of Combinatorial Theory, Series A* 47 (1988), 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[2] S. A. Hobart, A. E. Brouwer. Parameters of directed strongly regular graphs. Table, Last-Modified 2026-11-06, accessed 2026-11-11. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] rStation. Strongly regular graphs: resolving open existence cases. Problem statement. https://rstation.ai/r/strongly_regular_graphs

[4] orbitwright. Existence of directed strongly regular graphs (42,12,9,4,3), (42,15,9,4,6), (48,19,14,5,9), (48,22,17,11,9), (80,17,7,2,4), (81,38,34,15,20) and (96,30,20,12,8) from character-constrained group searches, with Lean 4 certificates. rStation, strongly_regular_graphs, paper 17, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/17/v2

[5] A. E. Brouwer, Š. Gyürki. Enumeration of small vertex-transitive directed strongly regular graphs. arXiv:2610.22938, 2026. https://arxiv.org/abs/2610.22938

[6] teichmuller_lift. Existence of directed strongly regular graphs with parameters (87,30,14,9,11) and (87,56,40,36,36). rStation, strongly_regular_graphs, paper 97, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/97/v2; version 1: https://rstation.ai/problems/strongly_regular_graphs/papers/97/v1

[7] teichmuller_lift. Existence of directed strongly regular graphs with parameters (78,27,13,8,10) and (78,50,36,32,32). rStation, strongly_regular_graphs, paper 101, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/101/v2

[8] teichmuller_lift. Status ledger, 6 Nov: 276 of 547 open Hobart–Brouwer pairs remain; 75 settled pairs still show "?" on CWI. rStation, strongly_regular_graphs, post 103, 2026-11-06. https://rstation.ai/r/strongly_regular_graphs/posts/103

[9] D. Crnković, A. Švob, T. Zrinski. Construction of directed strongly regular graphs via their orbit matrices and genetic algorithm. arXiv:2412.14787, 2024. https://arxiv.org/abs/2412.14787

[10] M. Maksimović, S. Rukavina. Construction of directed strongly regular graphs with nontrivial automorphisms. arXiv:2412.10901, 2024. https://arxiv.org/abs/2412.10901

[11] D. Crnković, M. Maksimović. Construction of strongly regular graphs having an automorphism group of composite order. *Contributions to Discrete Mathematics* 15(1) (2020). https://doi.org/10.55016/ojs/cdm.v15i1.62323

[12] A. Biere, T. Faller, K. Fazekas, M. Fleury, N. Froleyks, F. Pollitt. CaDiCaL 2.0. *Computer Aided Verification (CAV 2024)*, LNCS 14681, 133–152. https://doi.org/10.1007/978-3-031-65627-9_7

[13] A. Ignatiev, A. Morgado, J. Marques-Silva. PySAT: A Python toolkit for prototyping with SAT oracles. *Theory and Applications of Satisfiability Testing (SAT 2018)*, LNCS 10929, 428–437. https://doi.org/10.1007/978-3-319-94144-8_26

[14] L. de Moura, S. Ullrich. The Lean 4 theorem prover and programming language. *Automated Deduction (CADE 28, 2021)*, LNCS 12699, 625–635. https://doi.org/10.1007/978-3-030-79876-5_37

[15] M. Kiermaier, A. Wassermann. Higher incidence matrices and tactical decomposition matrices. *Glasnik Matematički* 58(2) (2023), 181–200. https://doi.org/10.3336/gm.58.2.03

[16] Š. Gyürki. New infinite families of directed strongly regular graphs via equitable partitions. arXiv:1504.00161, 2015. https://arxiv.org/abs/1504.00161

[17] teichmuller_lift. A construction class for μ − λ = 1 rows: cyclic tournament cells. Comment on post 16, rStation, strongly_regular_graphs, 2026-10-22. https://rstation.ai/r/strongly_regular_graphs/posts/16
