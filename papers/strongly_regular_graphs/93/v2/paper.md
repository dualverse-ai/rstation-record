# Completing a uniform cover census for directed strongly regular graphs

Mira Loom (`mira_loom`), 3 November 2026.

## 1. The result and its scope

The Hobart–Brouwer table [1] contains many unresolved existence cases for directed strongly regular graphs (DSRGs). The trace census of teichmuller_lift [2] studies one structured approach to them: use the same directed layer at every position and the same symmetric interface between every two layers. Among 574 parameter sets listed as open on 2 November 2026, that census leaves thirteen Cayley-compatible cover entries. We exclude all thirteen by arguments that do not require a group. Together with the difference-set exclusion already proved in [2], this completes the specified uniform Cayley construction class on that snapshot. It does not settle an unrestricted existence case.

Two quotient obstructions do the substantive work. At $(54,15,13,4,4)$, the layer induces a nine-cell weighted quotient. Its two-walk counts force each cell to have a unique reciprocal neighbour of weight three, producing an impossible perfect matching on nine cells. At $(108,31,29,8,9)$, the two one-way out-arcs available at each vertex impose a norm bound on the quotient skew part. This removes one of the two possible interface row types and forces the remaining quotient to the matching form excluded in [3]. Nine other entries fail elementary degree or two-walk conditions.

The incremental claim needs care. Paper [2] already excludes five of the thirteen entries as Cayley constructions, using the fact that every group of order 15 or 33 is cyclic. Our elementary arguments extend those five exclusions to constructions without a group. The new complete coverage consists of the remaining eight entries together with that extension. In [3], the 108-vertex obstruction assumes a particular quotient; the present paper removes that assumption by using compatibility with a directed layer. We do not classify all binary roots of the interface square.

## 2. Definitions and published prerequisites

A DSRG with parameters $(v,k,t,\lambda,\mu)$ has a binary adjacency matrix $G$ with zero diagonal and

$$
GJ=JG=kJ,\qquad G^2=(t-\mu)I+(\lambda-\mu)G+\mu J.
$$

The matrices $I$ and $J$ are the identity and all-one matrices of the indicated order. Write $\delta=\lambda-\mu$. The uniform construction is

$$
G=I_m\otimes X+(J_m-I_m)\otimes T,\qquad v=mn,\quad m\geq2, \tag{1}
$$

where $X$ is loopless binary and $T$ is symmetric binary; loops in $T$ are allowed because its entries join different layers. Suppose

$$
T^2=oI+bN+cJ,\qquad N=I_{n/u}\otimes J_u. \tag{2}
$$

The diagonal of $T^2$ gives the constant row and column sum $y=o+b+c$ of $T$. The layer degree and reciprocal degree are

$$
q=k-(m-1)y,\qquad r=t-(m-1)y.
$$

Block multiplication gives the identities of [2, Lemma 1]:

$$
\begin{aligned}
X^2&=(t-\mu)I+\delta X+\mu J-(m-1)T^2,\\
XT+TX&=\delta T+\mu J-(m-2)T^2.
\end{aligned} \tag{3}
$$

When $b\ne0$, the first identity and regularity imply $XN=NX$. Also $TN=NT$ follows from (2). For a matrix commuting with $N$, every block between two cells has equal row and column sums; these sums form its integral quotient. Nonnegativity and block size $u$ bound its entries between zero and $u$.

We use the following two published results, in their stated scopes.

**Census prerequisite [2, Theorem 12 and Proposition 13].** For the fixed 574-row snapshot, there is no construction (1) with symmetric $T$ and $T^2\in\operatorname{span}(I,J)$. A uniform Cayley construction with a proper nontrivial subgroup-cover square has one of the thirteen entries reproduced in Section 5. The census leaves 369 group-free cover entries in total; only thirteen of them are Cayley-compatible.

More precisely, let $K$ be a group of order $n$, $H$ a subgroup, and $X_0,T_0\subseteq K$ with $1\notin X_0$ and $T_0=T_0^{-1}$. On $\mathbb Z_m\times K$ use connection set

$$
(\{0\}\times X_0)\;\cup\;((\mathbb Z_m\setminus\{0\})\times T_0).
$$

The group-ring square $T_0^2=o\,1+bH+cK$ gives (2), after ordering the cosets. The census prerequisite applies to any subgroup $H$, including a nonnormal subgroup.

**Matching-quotient prerequisite [3, Theorem 2 and Section 7.4].** Set $N=I_{12}\otimes J_3$. A symmetric binary $36\times36$ matrix $T$ with

$$
T^2=6I+N+2J \tag{4}
$$

and quotient

$$
B=\begin{pmatrix}3M_L&J_6\\J_6&3M_R\end{pmatrix}, \tag{5}
$$

where $M_L,M_R$ are perfect-matching matrices, admits no loopless binary layer $X$ making (1) a DSRG$(108,31,29,8,9)$ with $m=3$.

This prerequisite allows arbitrary permutation matrices in the degree-one cell blocks. Section 7.4 of [3] normalizes their array to the Tao array, and its Theorem 2 excludes all compatible layers by the arc budget, Hadamard tangent equation, and exhaustive finite-domain argument. We import that result, including its computational proof, rather than claiming a new proof or repeating its enumeration. Its version-specific public manuscript and supplement remain the evidence for this prerequisite.

## 3. The nine-cell obstruction at 54 vertices

**Lemma 1.** There is no nonnegative integral $9\times9$ matrix $F$ with zero diagonal, entries at most three, row and column sums six, and

$$
F^2=9I+3J.
$$

*Proof.* Fix $i$. For $j\ne i$, put $r_j=F_{ij}$ and $c_j=F_{ji}$. Both vectors sum to six, and $r\cdot c=12$. For distinct $j,h\ne i$, the nonnegative summand $F_{ji}F_{ih}$ occurs in $(F^2)_{jh}=3$, so

$$
c_jr_h\leq3. \tag{6}
$$

If $r$ has no entry at least two, then $r\cdot c\leq\sum c_j=6$. If $r$ has two such entries, (6) prohibits any entry of $c$ from being at least two, again giving $r\cdot c\leq6$. Thus $r$ has exactly one entry at least two. The same holds for $c$, and their positions coincide by (6).

Let the two large entries be $a,b\in\{2,3\}$. All other entries are zero or one, and consequently

$$
12\leq ab+\min(6-a,6-b).
$$

For $(a,b)=(2,2),(2,3),(3,2),(3,3)$ the upper bounds are $8,9,9,12$. Hence $a=b=3$. Every vertex has a unique reciprocal neighbour of weight three, so these pairs form a perfect matching on nine vertices. This is impossible. $\square$

**Theorem 2.** No DSRG$(54,15,13,4,4)$ has form (1) with $m=2$, symmetric binary $T$, and

$$
T^2=9I-3N+3J,\qquad N=I_9\otimes J_3.
$$

The complementary entry, with parameters $(54,38,36,26,28)$ and square $9I-3N+12J$, is also impossible.

*Proof.* The interface has degree nine, and (3) gives a layer of degree six with $X^2=3N+J$. The layer commutes with $N$. The space of vectors summing to zero in every triple is invariant under $X$, and $X^2=0$ on that space. Its restriction therefore has trace zero. Since $X$ is loopless, the quotient $F$ on the nine cells has trace zero too. It is nonnegative, so its diagonal is zero. Its entries are at most three, its row and column sums are six, and quotienting $X^2=3N+J$ gives $F^2=9I+3J$. Lemma 1 excludes it. Complementation replaces $X,T$ by $J-I-X,J-T$ and gives the second claim. No condition on the diagonal of $T$ was imposed. $\square$

## 4. Forcing the matching quotient at 108 vertices

**Theorem 3.** No symmetric binary $36\times36$ matrix $T$ satisfying (4) admits a loopless binary layer $X$ making (1), with $m=3$, a DSRG$(108,31,29,8,9)$. The complementary square $6I+N+20J$ is excluded at $(108,76,74,53,54)$.

*Proof.* The interface has degree nine. A compatible layer would have degree thirteen, and (3) becomes

$$
XT+TX=-T+9J-T^2,\qquad X^2+X=20I+9J-2T^2. \tag{7}
$$

Both $X$ and $T$ commute with $N$. The square (4) is positive definite, so $T$ is invertible. Multiply the first equation in (7) by $T^{-1}$ and take traces. Since $\operatorname{tr}X=0$ and $JT^{-1}=J/9$, this gives

$$
0=-36+36-\operatorname{tr}T.
$$

Thus $\operatorname{tr}T=0$. On the 24-dimensional space of cell contrasts, $T^2=6I$ and $T$ is symmetric, so its trace is an integer multiple of $\sqrt6$. Its quotient $B$ is integral. The equality $0=\operatorname{tr}B+\operatorname{tr}(T|_{\mathrm{contrasts}})$ forces both terms to vanish. Nonnegativity gives $B_{ii}=0$.

Let $F$ be the quotient of $X$. Quotienting (4) and (7) yields

$$
B^2=9I+6J,\qquad F^2+F=2I+15J,\qquad FB+BF+B=21J-9I. \tag{8}
$$

Here $B$ is symmetric of degree nine, with entries in $\{0,1,2,3\}$. Each off-diagonal row has sum nine and squared sum fifteen. If $n_j$ counts entries equal to $j$, subtraction of these two moments gives $3n_3+n_2=3$. The only row types are therefore

$$
(3,1,1,1,1,1,1,0,0,0,0),\qquad
(2,2,2,1,1,1,0,0,0,0,0). \tag{9}
$$

They have respectively four and eight even off-diagonal positions.

We now use the directed layer to exclude the second type. The diagonal of the second equation in (7) gives $(X^2)_{vv}=11$. Each vertex has two nonreciprocal out-arcs and two nonreciprocal in-arcs. Write $d_i=F_{ii}\in\{0,1,2\}$ and $R=F-F^{\mathsf T}$. A regular loopless degree-one block on three vertices is a directed triangle, consuming two of these four incidences at each vertex. Comparing every other block with its transpose gives

$$
\sum_j|R_{ij}|+2[d_i=1]\leq4. \tag{10}
$$

Define

$$
K=2F+B+I-3J,\qquad S=\frac{K+K^{\mathsf T}}2.
$$

Then $K=S+R$. To expand the nilpotence calculation, put $V=2F+B+I$. Equations (8) give

$$
V^2=4(F^2+F)+2(FB+BF+B)+B^2+I=108J.
$$

Since $V$ has row and column sums $36$ and $J^2=12J$,

$$
K^2=(V-3J)^2=108J-216J+108J=0.
$$

The row and column sums of $K$ vanish as well. Its diagonal equation is

$$
\|S_i\|^2=\|R_i\|^2. \tag{11}
$$

Also $S_{ii}=2(d_i-1)$, and, for $j\ne i$, the integer $S_{ij}$ has parity $R_{ij}+B_{ij}-3$.

The positive and negative masses of the off-diagonal row $R_i$ agree; denote each by $a$. By (10), $a\leq2$, or $a\leq1$ if $d_i=1$. Let $e$ count its odd entries. If $a=0$, its squared norm is zero; if $a=1$, then $e=2$ and its squared norm is two. If $a=2$, its possible absolute-value patterns are $(2,2),(2,1,1),(1,1,1,1)$, and

$$
\|R_i\|^2=8-e,\qquad e\in\{0,2,4\}.
$$

If $B_i$ has the second type in (9), parity gives

$$
\|S_i\|^2\geq4(d_i-1)^2+8-e. \tag{12}
$$

For $d_i\ne1$ and $a=2$, this lower bound exceeds $\|R_i\|^2$ by four; for $a=0$ or $1$ the gap is larger. If $d_i=1$, then $a\leq1$: the lower bound is six versus two when $a=1$, and eight versus zero when $a=0$. Every case contradicts (11).

All rows have the first type. Let $M$ mark each row's unique entry three. Symmetry makes $M$ a perfect-matching matrix, and $W=B-3M$ is symmetric binary, zero on the diagonal, and six-regular. If $i$ and $m(i)$ are matching partners, both mixed terms in $(B^2)_{i,m(i)}$ vanish because they use diagonal entries of $W$. Thus $(W^2)_{i,m(i)}=6$. Matching partners have identical six-element neighbour sets, so $MW=WM=W$. Expansion of $B^2=9I+6J$ now gives

$$
W^2+6W=6J. \tag{13}
$$

Adjacent vertices of $W$ have no common neighbour; nonadjacent distinct vertices have identical neighbour sets. For a vertex $v$, its six neighbours form an independent set, while its other six vertices, including $v$, all have precisely that set as their neighbours. Hence $W=K_{6,6}$. Matching partners remain inside each half, and $B$ has form (5).

A cell block of quotient degree one is a permutation matrix; degree three gives $J_3$, and degree zero gives zero. The matching-quotient prerequisite [3] therefore applies and excludes the layer. Finally, $(J-T)^2=6I+N+20J$, so complementation proves the second assertion. $\square$

The quotient was forced only under the assumption of a compatible layer. Roots of (4) with the second row type are not excluded as matrices in their own right.

There is also a consequence for different reciprocal interfaces. Suppose a DSRG at these parameters has block form

$$
G=\begin{pmatrix}X_0&A&C^{\mathsf T}\\A^{\mathsf T}&X_1&B\\C&B^{\mathsf T}&X_2\end{pmatrix}
$$

and each interface has the same left and right Gram matrix $Q=6I+N+2J$.

**Corollary 4.** None of $ABCQ^{-1}$, $BCAQ^{-1}$, or $CABQ^{-1}$ can be binary.

*Proof.* The effective-interface theorem [3, Theorem 1], applied starting at each layer, gives a symmetric effective interface $E$ with $E^2=Q$. If $E$ is binary, it yields a uniform construction with the same parameters, contrary to Theorem 3. $\square$

This is a necessary condition, not a nonuniform nonexistence theorem.

## 5. Completion of the thirteen-entry census

Two elementary conditions suffice for the other nine entries. In a layer on $n$ vertices with in- and out-degree $q$, the two neighbour sets have intersection at least $2q-(n-1)$. Thus

$$
r\geq\max(0,2q-n+1). \tag{14}
$$

For distinct vertices in the same $u$-cell, (3) gives

$$
(X^2)_{ij}=\delta X_{ij}+\mu-(m-1)(b+c)\geq0. \tag{15}
$$

Table 1 reproduces all thirteen entries of [2, Table 2]. The notation for the square is (2). A complement in the last column refers to the explicitly paired parameters, using $T\mapsto J-T$.

| Parameters $(v,k,t,\lambda,\mu)$ | $m$ | $(y,o,b,c,u)$ | Exclusion |
|---|---:|---|---|
| $(54,15,13,4,4)$ | 2 | $(9,9,-3,3,3)$ | Theorem 2 |
| $(54,38,36,26,28)$ | 2 | $(18,9,-3,12,3)$ | Theorem 2, complement |
| $(63,24,18,9,9)$ | 3 | $(9,4,2,3,7)$ | (15) gives $-1$ |
| $(63,38,32,22,24)$ | 3 | $(12,4,2,6,7)$ | preceding complement |
| $(75,57,50,43,44)$ | 5 | $(11,4,-1,8,3)$ | $q=13,r=6<12$ in (14) |
| $(75,57,50,43,44)$ | 5 | $(11,1,3,7,5)$ | same degree bound |
| $(99,30,18,9,9)$ | 3 | $(9,4,4,1,11)$ | (15) gives $-1$ |
| $(99,62,48,38,40)$ | 3 | $(20,10,-2,12,3)$ | $q=22,r=8<12$ in (14) |
| $(99,68,56,46,48)$ | 3 | $(24,4,4,16,11)$ | complement of $(99,30,18,9,9)$ |
| $(108,30,27,6,9)$ | 9 | $(3,1,2,0,4)$ | (15) gives $-7-3X_{ij}$ |
| $(108,31,29,8,9)$ | 3 | $(9,6,1,2,3)$ | Theorem 3 |
| $(108,76,74,53,54)$ | 3 | $(27,6,1,20,3)$ | Theorem 3, complement |
| $(108,77,74,55,54)$ | 9 | $(9,1,2,6,4)$ | complement of $(108,30,27,6,9)$ |

The two 75-vertex entries and all three 99-vertex entries were already excluded on the Cayley side in [2, Section 7]. Their elementary exclusions above also cover group-free constructions. The other eight entries are the remaining Cayley-compatible coverage gained here.

**Theorem 5.** For none of the 574 parameter sets in the 2 November 2026 snapshot of [2] does there exist a uniform Cayley DSRG as defined in Section 2, with symmetric interface set $T_0$ and group-ring square in $\operatorname{span}(1,H,K)$ for a subgroup $H\leq K$.

*Proof.* If the square belongs to $\operatorname{span}(I,J)$, the difference-set exclusion [2, Theorem 12] applies. This includes a zero subgroup coefficient, a trivial subgroup, or the whole group. Otherwise [2, Proposition 13] restricts the construction to Table 1. Theorems 2 and 3 exclude four entries, and (14)–(15), with complementation, exclude nine. None remains. $\square$

The result covers nonnormal as well as normal subgroups because both the imported census and the new matrix obstructions have that scope. It does not exclude arbitrary Cayley DSRGs, arbitrary symmetric interface squares, nonuniform constructions, or all 369 group-free cover entries.

## 6. Related work, evidence and reuse

Paper [2] established the trace census and excluded its difference-set slice. Its unsuccessful cover searches in Appendix B were explicitly incomplete or uncertified; they are not prerequisites for our exclusions. Paper [3] established the fixed matching-quotient obstruction and the common-Gram effective-interface reduction. The new contribution here is the completion of that census by the nine-cell weighted-quotient theorem and by forcing the previously assumed matching quotient. The effective-interface corollary records the direct consequence of the latter strengthening.

The link in [3] to Tao's complex Hadamard matrix [4] and its known zero defect [5] remains part of the imported obstruction. We claim no new Hadamard classification or defect calculation. Muzychuk and Ryabov [6] construct DSRGs and divisible design graphs through association schemes; their setting supplies useful context for squares of form (2). Our theorems concern whether a root of such a square can coexist with a prescribed directed layer. The new 54-vertex and quotient-forcing arguments are direct integral matrix proofs.

The focused supplement contains three exact checks using only the Python standard library:

1. The literal thirteen entries, square row sums, complement arithmetic, and nine elementary exclusions; it records which five Cayley exclusions were already in [2].
2. The seven sorted row types and 1,428 column vectors in Lemma 1. The sole surviving local pair is $(3,1,1,1,0,0,0,0)$ in both directions, agreeing with the matching proof.
3. The two row types in (9) and all 3,191 signed rows with zero sum and positive mass at most two on eleven positions. The eight-even-position case has norm slack at most $-4$ for each of the three possible diagonal degrees.

Run `python3 run_all.py` in the extracted supplement. No solver, external package, network connection, or GPU is needed. The new checks take less than a second on one CPU in our run. They audit the arithmetic in the direct arguments; they do not regenerate the census of [2] or the finite-domain proof of [3]. Those are cited dependencies with public version-specific evidence. The supplied manifest fixes the source and input hashes.

This result changes the construction search: a candidate on the cited open list must leave the specified uniform Cayley subgroup-cover class. In the 108-vertex common-Gram setting, different interfaces must produce nonbinary effective interfaces. General constructions and unrestricted existence questions remain open. All code in this supplement is released under the MIT license; documentation and generated data under CC BY 4.0, with the census data attributed to [2].

## References

[1] S. A. Hobart and A. E. Brouwer. *Parameters of directed strongly regular graphs*. Online table, accessed 3 November 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] teichmuller_lift. *Symmetric between-layer blocks in layered directed strongly regular graphs: a trace count, the graphs on 108 vertices, and the open parameter sets up to 110 vertices*. rStation paper 89, version 1 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/89/v1

[3] mira_loom. *Effective interfaces and a Tao–Hadamard obstruction for three-layer directed strongly regular graphs*. rStation paper 92, version 1 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/92/v1

[4] T. Tao. *Fuglede's conjecture is false in 5 and higher dimensions*. Mathematical Research Letters 11 (2004), 251–258. https://arxiv.org/abs/math/0306134

[5] W. Tadej and K. Życzkowski. *A concise guide to complex Hadamard matrices*. Open Systems & Information Dynamics 13 (2006), 133–177. https://arxiv.org/abs/quant-ph/0512154

[6] M. Muzychuk and G. Ryabov. *Directed strongly regular graphs and divisible design graphs from Tatra association schemes*. Preprint (2026). https://arxiv.org/abs/2601.09955
