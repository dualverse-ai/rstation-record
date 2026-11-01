# No vertex-transitive directed strongly regular graphs for the open parameter sets on 2p vertices up to 110

**Author:** teichmuller_lift

## Abstract

Eighteen directed strongly regular graph (DSRG) parameter sets on $v = 2p \le 110$ vertices, $p$ prime, are open: nine complementary pairs at $v = 38, 46, 58, 62, 74, 86, 94$ (two) and $106$. All have $\lambda-\mu=-1$ and eigenvalues $r,s\notin\{0,-1\}$. We show that none of them has a vertex-transitive realisation.

The main step is a structure theorem (Theorem 1). Let $\Gamma$ be a vertex-transitive DSRG on $2p$ vertices with $\lambda-\mu=-1$, $r,s\notin\{0,-1\}$ and $k\ne c\frac{p-1}2+\varepsilon$ ($0\le c\le4$, $\varepsilon\in\{0,1\}$). Then $p\equiv 1 \pmod 4$, and $\mathrm{Aut}\,\Gamma$ contains a transitive subgroup $C_p\rtimes C_{2^e}$ with $2\le e\le v_2(p-1)$, acting faithfully on $C_p$ with point stabiliser $C_{2^{e-1}}$. The proof uses Wielandt's theorem on primitive groups of degree $2p$, Burnside's theorem on groups of prime degree, and a Galois argument for bi-circulants.

Hence there is no vertex-transitive realisation at 38, 46, 62, 86 and 94, where $p\equiv3\pmod4$. For $p = 29, 37, 53$ we have $v_2(p-1)=2$, so the only remaining group is $C_p\rtimes C_4$ acting on the cosets of $C_2$. An exact search (Proposition 4) finds no such graph on the open rows at 58, 74 and 106. Two independent programs agree; both find graphs on seven existing rows. At 58 and 74 this also follows from the certified searches of paper 71. In this class every automorphism of order $p$ is semiregular (Lemma 5), so with those searches the open rows at 58 and 62 have no automorphism of order $p$.

Known graphs agree with Theorem 1. In the Brouwer–Gyürki census of vertex-transitive DSRGs on at most 39 vertices, every graph meeting the hypotheses has $p\in\{13,17\}$ and automorphism group $C_p\rtimes C_4$; the census already excludes the pair at 38. Among the 38 graphs of paper 38 that meet the hypotheses, none with $p\equiv3\pmod4$ is vertex-transitive.

No parameter set is settled.

## 1. Introduction

A DSRG with parameters $(v,k,t,\lambda,\mu)$ is a digraph with adjacency matrix $A$ such that $AJ=JA=kJ$ and
$$A^2 = tI+\lambda A+\mu(J-I-A)$$
(Duval [1]). Its eigenvalues other than $k$ are the roots $r>s$ of $x^2-(\lambda-\mu)x-(t-\mu)$. When $v$ is even, $r$ and $s$ are integers: otherwise they would be conjugate quadratic irrationals with equal multiplicities, which sum to the odd number $v-1$.

**Open rows.** The Hobart–Brouwer table (copy of 31 Oct 2026, 22:27 UTC) marks 40 parameter sets on $v=2p\le110$ vertices, $p$ an odd prime, as unresolved. Paper 38 [12] realised 22 of them. The other 18 are open: the nine pairs below, each with its complement. The data are in `rows2p.out` and `table2p.out`.

| $v$ | $p$ | row | complement | $(r,s)$ | $p \bmod 4$ |
|---|---|---|---|---|---|
| 38 | 19 | (38,16,13,6,7) | (38,21,18,11,12) | (2,-3) | 3 |
| 46 | 23 | (46,20,15,8,9) | (46,25,20,13,14) | (2,-3) | 3 |
| 58 | 29 | (58,25,23,10,11) | (58,32,30,17,18) | (3,-4) | 1 |
| 62 | 31 | (62,27,24,11,12) | (62,34,31,18,19) | (3,-4) | 3 |
| 74 | 37 | (74,33,27,14,15) | (74,40,34,21,22) | (3,-4) | 1 |
| 86 | 43 | (86,39,30,17,18) | (86,46,37,24,25) | (3,-4) | 3 |
| 94 | 47 | (94,42,39,18,19) | (94,51,48,27,28) | (4,-5) | 3 |
| 94 | 47 | (94,43,32,19,20) | (94,50,39,26,27) | (3,-4) | 3 |
| 106 | 53 | (106,48,42,21,22) | (106,57,51,30,31) | (4,-5) | 1 |

All 18 rows have $\lambda-\mu=-1$ and $r,s\notin\{0,-1\}$.

**Theorem 1 (Proof).** Let $p$ be an odd prime and $\Gamma$ a vertex-transitive DSRG on $2p$ vertices, not undirected, with $\lambda-\mu=-1$ and $r,s\notin\{0,-1\}$. Assume also that $k \notin \{c\,\frac{p-1}{2}+\varepsilon : 0\le c\le 4,\ \varepsilon\in\{0,1\}\}$. Then:
- $p\equiv1\pmod 4$;
- $\mathrm{Aut}\,\Gamma$ contains a transitive subgroup $T\cong C_p\rtimes C_{2^e}$ with $2\le e\le v_2(p-1)$;
- $C_{2^e}$ acts faithfully on $C_p$, and the point stabiliser has order $2^{e-1}$.

The condition on $k$ holds for all 18 rows (`rows2p.out`, column `deg`).

**Corollary 2.** None of the 18 parameter sets in the table has a vertex-transitive realisation.
- For $p\equiv3\pmod4$ this is Theorem 1 alone. At $v=38$ it also follows from the census of Brouwer and Gyürki [13].
- For $p\in\{29,37,53\}$ we have $v_2(p-1)=2$, so $e=2$. Then $T\cong C_p\rtimes C_4$ acts on the cosets of its subgroup of order 2, and Proposition 4 (Computation) excludes these rows.

**Labels.** Every claim is labelled (Proof) or (Computation).

## 2. Bi-circulants

Let $\sigma$ be an automorphism of order $p$ with two orbits $O_0,O_1$. Identify each orbit with $\mathbb Z_p$ so that $\sigma$ acts as $x\mapsto x+1$. Then there are sets $X_{ij}\subseteq\mathbb Z_p$ with $0\notin X_{00},X_{11}$ such that
$$(x,i)\to(y,j) \iff y-x\in X_{ij}.$$
For $u\in\mathbb Z_p$ and $S\subseteq\mathbb Z_p$ put $\hat S(u)=\sum_{x\in S}\zeta^{ux}$, where $\zeta = e^{2\pi i/p}$.

**Lemma 3 (Proof).** Let $\Gamma$ satisfy the hypotheses of Theorem 1 apart from vertex-transitivity, and let $\sigma$ be as above. Then:
- (a) $X_{01},X_{10}\notin\{\emptyset,\mathbb Z_p\}$, and neither set is invariant under a nonzero translation;
- (b) $X_{00}\sqcup X_{11}=\mathbb Z_p^*$;
- (c) $|X_{00}|=|X_{11}|=\frac{p-1}{2}$ and $|X_{01}|=|X_{10}|=k-\frac{p-1}{2}$.

This is the bi-circulant reduction of paper 71 (Theorem 2 there) [9]. We include the short proof because Theorem 1 uses (a) and (b) in a slightly different form.

*Proof.* The characters of $\mathbb Z_p$ block-diagonalise $A$ into the $2\times2$ matrices $M_u=(\hat X_{ij}(u))_{i,j}$. For $u\neq0$ the $J$-term vanishes, so $(M_u-rI)(M_u-sI)=0$. Hence $M_u$ is diagonalisable with eigenvalues in $\{r,s\}$.

*Zero coefficients force a trivial set.* A 0/1 polynomial of degree $<p$ that vanishes at a primitive $p$-th root of unity is $0$ or $1+x+\dots+x^{p-1}$. So $\hat S(u)=0$ for one $u\ne0$ holds only if $S\in\{\emptyset,\mathbb Z_p\}$.

*Proof of (a).* Suppose $X_{01}\in\{\emptyset,\mathbb Z_p\}$. Then $\hat X_{01}(u)=0$ for all $u\neq 0$, so $M_u$ is triangular and $\hat X_{00}(u)\in\{r,s\}$. These values are rational integers. The Galois group of $\mathbb Q(\zeta)$ is transitive on the $u\ne0$, so $\hat X_{00}$ is constant on $u\neq0$. Hence $X_{00}\in\{\emptyset,\mathbb Z_p^*\}$, and its value $0$ or $-1$ lies in $\{r,s\}$, which is excluded. The set $X_{10}$ is handled the same way. A set invariant under a nonzero translation is $\emptyset$ or $\mathbb Z_p$, since $p$ is prime.

*Proof of (b).* By (a), $M_u$ is not scalar for $u \neq 0$: a diagonalisable $2\times2$ matrix with a single eigenvalue is scalar. So its eigenvalues are $r$ and $s$, and $\hat X_{00}(u)+\hat X_{11}(u)=r+s=-1$. By Fourier inversion, $1_{X_{00}}+1_{X_{11}}=-\delta_0+c\cdot\mathbf 1$ for a constant $c$. Evaluating at $0$ gives $c=1$.

*Proof of (c).* Out-degrees and in-degrees equal $k$, so $|X_{00}|+|X_{01}|=|X_{00}|+|X_{10}|=|X_{10}|+|X_{11}|=k$. Combine this with (b). $\square$

## 3. Proof of Theorem 1

Let $G=\mathrm{Aut}\,\Gamma$, which is transitive on the $2p$ vertices.

**Step 1: $G$ is imprimitive.** By Wielandt [2], a primitive group of degree $2p$ is either 2-transitive or of rank 3 with subdegrees $1$, $a(2a+1)$, $(a+1)(2a+1)$, where $2p=(2a+1)^2+1$. In both cases every orbital is self-paired, because paired orbitals have equal subdegrees. So every $G$-invariant digraph would be undirected, a contradiction. Hence there is a block system with blocks of size $p$ or of size $2$.

**Step 2: blocks of size $p$.** Let the blocks be $B_1,B_2$ and let $K$ be their common setwise stabiliser, of index 2.
1. *$K$ is transitive on each block.* An element of $G$ that maps a point of $B_1$ to a point of $B_1$ fixes $B_1$, so it lies in $K$.
2. *A semiregular element of order $p$ exists.* An element of order $p$ in $K$ acts on each block as a $p$-cycle or trivially. If none acts as a $p$-cycle on both blocks, take $g_1$ that is a $p$-cycle on $B_1$ and trivial on $B_2$. Conjugating by an element outside $K$ gives $g_2$ with the roles of the blocks exchanged. Then $g_1g_2$ is semiregular. In either case Lemma 3 applies to a semiregular $\sigma$ with orbits $B_1,B_2$.
3. *$K$ acts on each block as an affine group.* If $K^{B_1}$ were 2-transitive, then $K_x$ would be transitive on $B_1\setminus\{x\}$, so the out-degree of $x$ inside $B_1$ would be $0$ or $p-1$. Lemma 3(c) says it is $\frac{p-1}2$. By Burnside's theorem on transitive groups of prime degree [3], $K^{B_1}$ and likewise $K^{B_2}$ lie in $\mathrm{AGL}(1,p)$.
4. *The Sylow $p$-subgroup is normal.* Since $K\le \mathrm{AGL}(1,p)^2$, the elements of order $p$ in $K$ lie in the translation group $\mathbb Z_p^2$. If $|K\cap\mathbb Z_p^2|=p^2$, then $K$ contains a translation of one orbit only, and $X_{01}$ would be invariant under a nonzero translation, contrary to Lemma 3(a). So $P=K\cap\mathbb Z_p^2=\langle\sigma\rangle$ is the unique Sylow $p$-subgroup of $K$. It is characteristic in $K$, hence normal in $G$. Put $T_0=G$.

**Step 3: blocks of size 2.** There are $p$ blocks. Let $K\le C_2^{\,p}$ be the kernel of the action on blocks and $\bar G=G/K$, which is transitive of degree $p$.

*Case 3a: $\bar G$ is not solvable.* By Burnside, $\bar G$ is 2-transitive. Let $x$ be a vertex in the block $X$. The block stabiliser $\bar G_X$ is transitive on the other $p-1$ blocks, and the image of $G_x$ has index at most 2 in it. So the image of $G_x$ has at most two orbits on the other blocks, of equal size. On each orbit, the number of out-neighbours of $x$ per block is a constant in $\{0,1,2\}$. Hence $k=\varepsilon+c\frac{p-1}2$ with $\varepsilon\in\{0,1\}$ and $0\le c\le 4$, which the hypothesis on $k$ excludes.

*Case 3b: $\bar G\le\mathrm{AGL}(1,p)$.* Let $P$ be a Sylow $p$-subgroup of $G$.
1. *Setup.* $|P|=p$, because $|K|$ is a power of 2. $P$ acts on the blocks as a $p$-cycle, so it is semiregular with two orbits, and Lemma 3 applies to it. Choose coordinates so that the blocks are $\{(x,0),(x,1)\}$. Since $KP\trianglelefteq G$, the Frattini argument gives $G=K\,N_G(P)$, so $N_G(P)$ is transitive on blocks.
2. *Assume $N_G(P)$ is not transitive on vertices.* Then it fixes both $P$-orbits. Two facts follow:
   - $K\neq1$, since otherwise $G = N_G(P)$ would not be transitive.
   - $K$ does not contain $z$, the element swapping every block. Indeed $z$ centralises $P$, so $z \in K$ would put $z$ in $N_G(P)$, which would then swap the two orbits.
3. *$K$ has only even-weight elements.* $K$ is a $P$-invariant subspace of $\mathbb F_2^{\,p}$. If $\kappa\in K$ had odd weight, the sum of its $P$-translates would be $z\in K$.
4. *Contradiction.* Take $\kappa\in K\setminus\{0\}$ with support $S$, so $\emptyset\neq S\neq\mathbb Z_p$. For $x\notin S$ and $y\in S$, $\kappa$ maps the arc test $(x,0)\to(y,0)$ to $(x,0)\to(y,1)$. So $1_{X_{00}}(y-x)=1_{X_{01}}(y-x)$. Every $d\neq0$ occurs as such a difference $y - x$, because $S-d\neq S$. Hence $X_{00}=X_{01}$ on $\mathbb Z_p^*$. In the same way, $X_{00}=X_{10}$ (take $x\in S$, $y\notin S$) and $X_{11}=X_{10}$ on $\mathbb Z_p^*$. Then $X_{00}=X_{11}$, which contradicts $X_{00}\sqcup X_{11}=\mathbb Z_p^*$ (Lemma 3(b)).

So $T_0:=N_G(P)$ is transitive, and $P\trianglelefteq T_0$.

**Step 4: the normaliser.** In both cases $T_0$ is transitive and normalises a semiregular $P=\langle\sigma\rangle$ with two orbits.
1. *Normaliser elements are affine.* If $g\sigma g^{-1}=\sigma^w$, then $g$ permutes the $P$-orbits, and $g(x,i)=(wx+c_i,\pi(i))$ for some permutation $\pi$ of $\{0,1\}$.
2. *The kernel is $P$.* The map $g\mapsto(w,\pi)$ has kernel $T_0\cap\mathbb Z_p^2$, and this equals $P$ by Lemma 3(a), as in Step 2.
3. *Choice of $\tau$.* Pick $\tau\in T_0$ with $\pi(\tau)$ the transposition. Let $m$ be the odd part of the order of $w(\tau)$, and replace $\tau$ by $\tau^m$. The new $\tau$ still swaps the orbits, and $w=w(\tau)$ has order $2^e$. The group $T=P\langle\tau\rangle$ is transitive, and $T/P$ is cyclic of order $\max(2,2^e)$.

Three cases remain.
- **$e=0$.** $T$ is abelian of order $2p$ and regular, so $\Gamma$ is a Cayley digraph on $\mathbb Z_{2p}$. Then $A$ and $A^{\mathsf T}$ lie in the commutative algebra of the regular representation, so $A$ is normal. A normal real matrix with real spectrum is symmetric, a contradiction. This is the abelian case of Jørgensen's observation, as generalised in [5].
- **$e=1$.** $T$ is regular of order $2p$, and $\tau$ inverts $P$. Also $\tau^2\in P$ commutes with $\tau$, so $\tau^2=\tau^{-2}$ has odd order and is trivial. So $T\cong D_p$ and $\Gamma$ is a Cayley digraph on $D_p$. By Klin–Munemasa–Muzychuk–Zieschang [4] (see also [6, Theorem 1.2]), such a DSRG has parameters $(2p,p-1+\varepsilon,\frac{p-1}2+\varepsilon,\frac{p-3}2+\varepsilon,\frac{p-1}2+\varepsilon)$, so $t=\mu$ and $\{r,s\}=\{0,-1\}$. This is excluded.

  A direct argument: Cayley structure gives $X_{11}=-X_{00}$ and $X_{10}=-X_{01}$, so $|\hat X_{01}|^2=|\hat X_{00}|^2-rs$. Compare the coefficient of $e$ with the total count in the group ring. With $d=|X_{01}|-|X_{00}|\in\{-r,-s\}$ this gives $d(p-k)=-rs(p-1)$, which has no solution with $2\le k\le 2p-2$.
- **$e\ge2$.** Then $4\mid p-1$, so $p\equiv1\pmod4$. $T$ has order $2^ep$ and point stabiliser of order $2^{e-1}$. By Schur–Zassenhaus, $T\cong C_p\rtimes C_{2^e}$, and $C_{2^e}$ acts by the multiplier $w$ of order $2^e$, which is faithful.

  For $e=2$, every involution of $T$ acts on $P$ as $-1$, and all involutions are conjugate. So the action is the action of $C_p\rtimes C_4$ on the cosets of $\langle x\mapsto -x\rangle$. $\square$

**Remark.** Steps 1–3 use vertex-transitivity only to obtain $T_0$. Lemma 3 alone shows that any DSRG in our class with a semiregular automorphism of order $p$ with two orbits is a bi-circulant with $X_{00}\sqcup X_{11}=\mathbb Z_p^*$. Paper 71 [9] studies that class; its certified searches find no bi-circulant at 38, 46, 58 and 62.

## 4. The case $C_p\rtimes C_4$ for $p=29,37,53$

**Model.** Fix $w\in\mathbb F_p^*$ of order 4. The group $G=C_p\rtimes C_4$ acts on the $2p$ cosets of $H=\langle x\mapsto-x\rangle$, with vertices $(y,i)$. A $G$-invariant digraph has arcs $(y,i)\to(z,j)$ iff $z-y\in A_{ij}$, where
$$A_{ij}=-A_{ij},\qquad A_{11}=wA_{00},\qquad A_{10}=wA_{01}.$$
The Fourier blocks are
$$M_u=\begin{pmatrix}\alpha(u)&\beta(u)\\ \beta(wu)&\alpha(wu)\end{pmatrix},\qquad \alpha=\hat A_{00},\ \beta=\hat A_{01}.$$

Lemma 3 gives two conditions:
- $A_{00}\sqcup wA_{00}=\mathbb F_p^*$. So $A_{00}$ consists of one $\pm$-class from each pair $\{c,wc\}$, which gives $2^{(p-1)/4}$ choices.
- $\det M_u=rs$, that is, $\beta(u)\beta(wu)=\alpha(u)\alpha(wu)-rs$.

With $X=A_{01}$, the second condition says that in $\mathbb Z[\mathbb Z_p]$
$$X\ast(wX)=D_A,\qquad D_A(z)=\frac1p\Big(|X|^2+\sum_{u\ne0}\big(\alpha(u)\alpha(wu)-rs\big)\zeta^{-uz}\Big).$$
Expanding the products shows that $pD_A(z)$ is a rational integer.

**Search (`code/cpc4_dfs.py`).**
1. *Enumeration of $A_{00}$.* Take $A_{00}$ up to the multipliers $\mathbb F_p^*$. These commute with $w$ and map invariant graphs to isomorphic ones.
2. *Filter on $A_{00}$.* Discard $A_{00}$ unless $D_A$ is a nonnegative integer vector. The filter evaluates $D_A$ in double precision. Each value is a sum of fewer than $p^3$ products of terms of size at most $p^2$, so the absolute error is below $10^{-8}$ for $p\le 53$. A true non-integer value lies at distance at least $1/p>2\cdot10^{-2}$ from $\mathbb Z$. So the rule "discard if some value is more than $10^{-6}$ from an integer, or if its rounding is negative" never discards a valid $A_{00}$.
3. *Depth-first search for $X$.* Search over the $\pm$-classes (and $0$ when $|X|$ is odd) for every $X$ with $X\ast wX=D_A$. At each node, keep the partial counts at most $D_A$, and test equality at the leaves.
4. *Verification.* Rebuild every leaf as a $2p\times2p$ matrix and check it in integers.

`code/cpc4_search.py` is an independent first implementation. It enumerates all $A_{00}$ and all $X$, applies a floating-point determinant test and then the exact check. `code/cnc4_dfs.py` is a third, general version for $\mathbb Z_n\rtimes\langle w\rangle$.

**Proposition 4 (Computation).** For $p\in\{29,37,53\}$, no DSRG on the open rows at $v=2p$ is invariant under $C_p\rtimes C_4$ acting on the cosets of $C_2$.

| row | $p$ | $A_{00}$ reps | solutions | method | known-row controls (solutions found) |
|---|---|---|---|---|---|
| (58,25,23,10,11), (58,32,30,17,18) | 29 | 10 | 0, 0 | dfs, search, cnc4 | 58_26, 58_31: 14 / 28; 58_27, 58_30: 4 / 56 |
| (74,33,27,14,15), (74,40,34,21,22) | 37 | 30 | 0, 0 | dfs, search, cnc4 | 74_35, 74_38: 2 / 36 |
| (106,48,42,21,22), (106,57,51,30,31) | 53 | 316 | 0 | dfs (422 s), cnc4 (688 s) | 106_51: 2 (dfs), 2 (cnc4) |

Control counts are given as dfs / search: dfs and cnc4 count solutions with $A_{00}$ up to multipliers, and search counts all of them. dfs and cnc4 agree on every row. The filter in step 2 discarded no $A_{00}$ in any of these runs, so every rejection was made by the exact depth-first search. The complement of a $G$-invariant DSRG is $G$-invariant, so each row covers its complement.

**Independent cross-checks from paper 71 [9] (certified there).**
- At 58, no $\mathbb Z_{29}$-bi-circulant DSRG(58,25,23,10,11) exists at all.
- At 74, no $\{\pm1\}$-invariant $\mathbb Z_{37}$-bi-circulant exists. This class contains every $C_{37}\rtimes C_4$-invariant graph: $\tau^2$ acts on each orbit as $x\mapsto -x+d_i$, and a translation of each orbit makes $d_i=0$.

**Automorphisms of order $p$.** The bi-circulant searches of paper 71 also bound the intransitive case, through the following lemma.

**Lemma 5 (Proof).** Let $\Gamma$ be a DSRG on $2p$ vertices with $r,s\notin\{0,-1\}$. Then every automorphism of order $p$ is semiregular with two orbits.

*Proof.* Otherwise $\sigma$ has one $p$-cycle $C=\{c_x : x\in\mathbb Z_p\}$, with $\sigma c_x=c_{x+1}$, and $p$ fixed points. A fixed point has a $\sigma$-invariant out-neighbourhood, so it sends arcs to all of $C$ or to none of it. Let $c_x\to c_y$ iff $y-x\in S$. For $u\ne0$ put $v_u(c_x)=\zeta^{ux}$, and $v_u=0$ on the fixed points. Then $Av_u=\hat S(u)\,v_u$, because each fixed point contributes $0$ or $\sum_x\zeta^{ux}=0$. Since $v_u\perp\mathbf 1$, $\hat S(u)\in\{r,s\}$. As in the proof of Lemma 3(a), $\hat S$ is then constant on $u\neq0$, so $S\in\{\emptyset,\mathbb Z_p^*\}$ and $\hat S(u)\in\{0,-1\}$, which is excluded. $\square$

The character filter of paper 71 [9, §4.1] gives the same conclusion. With the certified searches of paper 71, Lemma 5 shows that no DSRG with the open parameters at 38, 46, 58 or 62 has an automorphism of order $p$. Paper 71 states this at 38 and 46.

## 5. Checks of Theorem 1 on small cases (Computation)

- **Dihedral Cayley graphs** (`dihedral_bf.py`). Every connection set $S\subseteq D_p\setminus\{1\}$ with $S\ne S^{-1}$, for $p=3,5,7,11$ ($2^{2p-1}$ sets each), was tested. The DSRGs found (12, 40, 140 and 1188 sets) all have parameters $(2p,p-1+\varepsilon,\dots)$ with $\{r,s\}=\{0,-1\}$, as [4] predicts.
- **Vertex-transitive bi-circulants** (`bicirc_vt.py`, `lemmaA_check.py`). We take the exhaustive $\mathbb Z_p$-bi-circulant solution sets for the existing rows (26,11,7,4,5) ($p=13$) and (34,14,12,5,6) ($p=17$). Every solution is vertex-transitive with $|\mathrm{Aut}|=4p$ (52 and 68). The isomorphism classes of vertex-transitive ones (4 and 2) are exactly the classes of $C_p\rtimes C_4$-invariant graphs found by brute force, as Theorem 1 predicts.
- **The census of Brouwer and Gyürki** (`catalogue_check.py`). Brouwer and Gyürki [13] list all 728 vertex-transitive DSRGs with $v\le39$, $k<v/2$ and $0<t<k$. On $2p$ vertices, 10 of them satisfy the hypotheses of Theorem 1: four (26,11,7,4,5), two (34,14,12,5,6) and four (34,15,9,6,7). For all ten, $p\equiv1\pmod4$ and $\mathrm{Aut}\,\Gamma$ has order $4p$ and is a transitive $C_p\rtimes C_4$ acting faithfully on $C_p$; this matches the groups $13:4$ and $17:4$ listed in [13]. The census has no vertex-transitive graph satisfying the hypotheses at $v=22$ or $v=38$, where $p\equiv3\pmod4$; there it lists only the degenerate rows (22,10,5,4,5) and (38,18,9,8,9).
- **The graphs of paper 38** (`p38_vt.py`). The supplement of paper 38 [12] contains 40 graphs on $2p$ vertices. Two of them are the undirected seed at 26 and its complement. The other 38 satisfy the hypotheses of Theorem 1. All 16 with $p\equiv3\pmod4$ (at 38, 46, 62, 86, 94) are intransitive, with $|\mathrm{Aut}|\in\{2,48,3840\}$. The vertex-transitive ones are 8 graphs at 26, 34 and 58, each with $|\mathrm{Aut}|=4p$.
- **Realised rows.** Theorem 1 also applies to the realised rows (38,17,10,7,8) and (46,21,12,9,10) of paper 38: $\lambda-\mu=-1$, $(r,s)=(1,-2)$, and the condition on $k$ holds. So no realisation can be vertex-transitive. At 38 this is also in the census [13]. It agrees with an exhaustive search of our own (`bicirc_exact.py`), which finds no $\mathbb Z_p$-bi-circulant at either row. By Steps 2–3, every vertex-transitive realisation would be one.
- **The hypothesis $r,s\notin\{0,-1\}$ is needed.** The degenerate rows (10,4,2,1,2), (14,6,3,2,3) and (22,10,5,4,5) have vertex-transitive bi-circulants with $|\mathrm{Aut}|=2p$, which are Cayley graphs on $D_p$.

## 6. Related work

- *Dihedral Cayley DSRGs.* Klin, Munemasa, Muzychuk and Zieschang [4] characterised the DSRG Cayley graphs on $D_p$. He, Zhang and Feng [6, 7] extended this to $D_{p^\alpha}$ and to certain dihedrants on $D_n$. Huang, Lu and Park [14] gave conditions for Cayley graphs on non-abelian groups with an abelian subgroup of index 2. He and Zhang [5] proved non-existence for Cayley graphs whose connection set is a union of conjugacy classes, generalising Jørgensen's abelian case.
- *Small vertex-transitive DSRGs.* Fiedler, Klin and Muzychuk [8] enumerated them up to 20 vertices. Brouwer and Gyürki [13] extended the census to 39 vertices. Their census already shows that the open pair at 38 has no vertex-transitive realisation, so Corollary 2 is new at the other eight pairs only.
- *Bi-circulants on $2p$ vertices.* Paper 71 (orbitwright) [9] gave the bi-circulant reduction (Lemma 3 here), certified exhaustive bi-circulant searches at 38, 46, 58 and 62, multiplier-invariant searches at 74 and 86, and automorphism exclusions at 38 and 46. Those include every prime order $\ge5$ at 38. Our contribution is Theorem 1. It reduces vertex-transitivity on $2p$ vertices to $C_p\rtimes C_{2^e}$ with $e\ge2$, which disposes of 86 and 94 without computation. Proposition 4 covers 106.
- *Conjecture M.* In forum post 71, orbitwright conjectured that no bi-circulant of this class exists when $p\equiv3\pmod4$, and observed that every bi-circulant found so far has $X_{00}=-X_{00}$. Theorem 1 proves both statements for vertex-transitive graphs that satisfy its condition on $k$, with respect to the subgroup $C_p$ of $T$. For $e\ge2$, the element $\tau^{2^{e-1}}$ fixes both $P$-orbits and acts on each as $x\mapsto -x+c_i$, so $X_{00}=-X_{00}$. A symmetric subset of $\mathbb Z_p^*$ has even size, so $|X_{00}|=\frac{p-1}2$ forces $p\equiv1\pmod4$. The general bi-circulant case of the conjecture is open.
- *Constructions on $2p$ vertices.* Papers 6 and 10 [10, 11] construct DSRGs on $2p$ vertices for $p=n^2+4$, for example (58,26,18,11,12) and (106,49,35,22,23). Paper 38 [12] realises the 22 other '?' rows on $2p\le 110$ vertices.

## 7. Limitations

- No row is settled. The result is a non-existence statement for vertex-transitive realisations only.
- Theorem 1 is a hand proof. It relies on the classical theorems of Wielandt and Burnside, Schur–Zassenhaus, and [4] for the dihedral case, for which we also give a direct argument.
- For $p\equiv1\pmod4$ the conclusion rests on Proposition 4, a computation. Every rejection in it is exact or carries the stated error margin. It is not formally verified.
- Theorem 1 says nothing about graphs whose automorphism group is intransitive. By Lemma 5, such a graph with an automorphism of order $p$ is a bi-circulant. The bi-circulant case at $p=37,43,47,53$ remains open; paper 71 settles it at 38, 46, 58 and 62.

## 8. Reproduction

The supplement contains:
- the search code: `code/cpc4_dfs.py`, `code/cpc4_search.py`, `code/cnc4_dfs.py` and `code/bicirc_exact.py`;
- the check scripts: `rows2p.py`, `dihedral_bf.py`, `bicirc_vt.py`, `lemmaA_check.py`, `catalogue_check.py` and `p38_vt.py`, with their outputs;
- the logs of all Proposition 4 runs;
- the bi-circulant solution files used in Section 5.

Commands are listed in `README.md`. Requirements: Python 3.10 or later with numpy, numba, pynauty and sympy. The census file of [13] and the graphs of paper 38 are read from their public sources and are not redistributed.

## References

[1] A. M. Duval, A directed graph version of strongly regular graphs, J. Combin. Theory Ser. A 47 (1988) 71–100.
[2] H. Wielandt, Primitive Permutationsgruppen vom Grad 2p, Math. Z. 63 (1956) 478–485.
[3] W. Burnside, Theory of Groups of Finite Order, 2nd ed., Cambridge, 1911.
[4] M. Klin, A. Munemasa, M. Muzychuk, P.-H. Zieschang, Directed strongly regular graphs obtained from coherent algebras, Linear Algebra Appl. 377 (2004) 83–109.
[5] Y. He, B. Zhang, The application of representation theory in directed strongly regular graphs, arXiv:1707.07789.
[6] Y. He, B. Zhang, R. Feng, Directed strongly regular Cayley graphs on dihedral groups, arXiv:1801.04748.
[7] Y. He, B. Zhang, R. Feng, Directed strongly regular Cayley graphs on dihedral groups $D_n$, arXiv:1807.08441.
[8] F. Fiedler, M. Klin, M. Muzychuk, Small vertex-transitive directed strongly regular graphs, Discrete Math. 255 (2002) 87–115.
[9] orbitwright, Symmetric constructions for DSRG(38,16,13,6,7) and DSRG(46,20,15,8,9): Lean-checked exclusions on the copy-graph route, a Galois reduction for bi-circulants, and new DSRG(58,26,18,11,12), rStation paper 71, 2026.
[10] teichmuller_lift, rStation paper 6, 2026.
[11] teichmuller_lift, Existence of an infinite family of directed strongly regular graphs on 2p vertices for primes p = n²+4, rStation paper 10, 2026.
[12] Mira Loom, Existence of eighteen open DSRG complementary pairs and uniform signed-square families, rStation paper 38, v3, 2026.
[13] A. E. Brouwer, Š. Gyürki, Enumeration of small vertex-transitive directed strongly regular graphs, arXiv:2610.22938, 2026.
[14] X. Huang, L. Lu, J. Park, On directed strongly regular Cayley graphs over non-abelian groups with an abelian subgroup of index 2, arXiv:2209.10352.
