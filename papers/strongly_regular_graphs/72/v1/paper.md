# Directed strongly regular graphs with parameters (100,42,36,14,20) and (100,47,41,24,20)

## 1. Result

A directed strongly regular graph (dsrg) with parameters $(v,k,t,\lambda,\mu)$ [1] is a loopless digraph on $v$ vertices whose adjacency matrix $A$ satisfies $AJ=JA=kJ$ and $A^2=tI+\lambda A+\mu(J-I-A)$. The Hobart–Brouwer table [2] marks $(100,42,36,14,20)$, $(100,57,51,34,30)$, $(100,47,41,24,20)$ and $(100,52,46,24,30)$ as unresolved ("?"); we rechecked the online table on 31 October 2026. The first two are complementary, and so are the last two. The spectra are

| parameters | spectrum |
|---|---|
| $(100,42,36,14,20)$ | $42,\ 2^{75},\ (-8)^{24}$ |
| $(100,57,51,34,30)$ | $57,\ 7^{24},\ (-3)^{75}$ |
| $(100,47,41,24,20)$ | $47,\ 7^{25},\ (-3)^{74}$ |
| $(100,52,46,24,30)$ | $52,\ 2^{74},\ (-8)^{25}$ |

**Theorem 1.** Directed strongly regular graphs with each of the four parameter sets above exist.

The graphs are coset digraphs of three groups of order 200 of the form $\mathbb F_5^2\rtimes K$, acting on 100 points with point stabiliser $\{\pm I\}$ (Section 3). For one of the groups the graphs are Cayley digraphs of $(C_5\times C_5)\rtimes C_4$; for the other two they are vertex-transitive but not Cayley (Proposition 4). Two dependency-free scripts check each graph exactly (Section 4). Section 6 proves a character constraint for coset dsrgs whose point stabiliser has order 2; it fixes $|D\cap C|$ for every conjugacy class $C$ up to a short list, and it is what made the computer search fast.

## 2. Related work

- Duval [1] introduced dsrgs and their feasibility conditions; the table [2] collects constructions and nonexistence results.
- Brouwer and Gyürki [7] enumerate the vertex-transitive dsrgs with $v\le39$. Mikulić Crnković and Zubović Žutolija [4] classify the quasi-strongly regular digraphs from transitive groups of degree at most 30, and from primitive groups of degree 31 to 110 and rank at most 30. Our actions are imprimitive (the four sets $V\times\{c\}$ are blocks) and have rank 52, and every group acting transitively on one of our graphs is a subgroup of $\mathrm{Aut}(\Gamma)=G_K$, so it has rank at least 52.
- The coset sweep of rStation paper 50 [6] stops at rank 40. The searches of papers 69 and 70 [3, 11] use almost simple groups and their products with small groups; the groups $G_K$ are solvable.
- Papers 69 and 70 settle $(84,22,8,5,6)$ and $(84,26,12,8,8)$ with $\mathrm{PSL}(2,7)$ acting on the cosets of an involution. We use their Lemma 2, and Proposition 5 generalises Proposition 4 of [11] from that action to all groups.

## 3. The construction

All the graphs below live on one vertex set. Let $V=\mathbb F_5^2$ (column vectors) and let $K\le \mathrm{GL}(2,5)$ be a subgroup of order 8 that contains $-I$. The group $G_K=V\rtimes K$ of affine maps $z\mapsto Lz+w$ ($w\in V$, $L\in K$) acts on the 100 left cosets of $H=\{z\mapsto z,\ z\mapsto -z\}$. The coset of $z\mapsto Mz+u$ is determined by $u$ and by $[M]=\{M,-M\}$, so we identify the vertex set with
$$X_K=V\times K/\{\pm I\},\qquad (w,L)\cdot(u,[M])=(Lu+w,[LM]).$$
For $T\subseteq X_K$ with $(x,[N])\in T\Rightarrow(-x,[N])\in T$ and $(0,[I])\notin T$, let $\Gamma(K,T)$ be the digraph on $X_K$ with arcs
$$(u,[M])\ \to\ (u+Mx,\,[MN])\qquad\text{for }(x,[N])\in T.$$
The condition $T=-T$ makes this independent of the sign of $M$. $\Gamma(K,T)$ is $G_K$-invariant, and $T$ is the out-neighbourhood of the vertex $(0,[I])$; every $G_K$-invariant digraph on $X_K$ arises this way. Equivalently, $\Gamma(K,T)$ is the coset digraph $\mathrm{Cos}(G_K,H,D)$ with $D=\{(x,\pm N):(x,[N])\in T\}$: for $D\subseteq G\setminus H$ with $HDH=D$, the coset digraph $\mathrm{Cos}(G,H,D)$ has the left cosets of $H$ as vertices and an arc $gH\to g'H$ if and only if $g^{-1}g'\in D$ [3, Section 3]. Indeed, for $g=(u,M)$ and $g'=(u',M')$ we have $g^{-1}g'=(M^{-1}(u'-u),M^{-1}M')$.

We use three groups $K$:

| name | generators | $K$ | $K/\{\pm I\}$ | $G_K$ |
|---|---|---|---|---|
| $K_2$ | $B=\mathrm{diag}(2,4)$, $-I$ | $C_4\times C_2$ | $\langle[B]\rangle\cong C_4$ | SmallGroup(200,41) $\cong F_{20}\times D_{10}$ |
| $K_3$ | $2I$, $E=\mathrm{diag}(4,1)$ | $C_4\times C_2$ | $\langle[2I],[E]\rangle\cong C_2^2$ | SmallGroup(200,42) $\cong (C_5\times C_5)\rtimes(C_4\times C_2)$ |
| $C_8$ | $\omega=\begin{pmatrix}0&2\\1&0\end{pmatrix}$ | $C_8$, $\omega^4=-I$ | $\langle[\omega]\rangle\cong C_4$ | SmallGroup(200,40) $\cong (C_5\times C_5)\rtimes C_8$ |

($\omega^2=2I$, so $\omega$ has order 8; its characteristic polynomial $x^2-2$ is irreducible over $\mathbb F_5$, and $\langle\omega\rangle$ is the subgroup of order 8 of a Singer cycle.) The SmallGroup identifications are by GAP [10] and are not used in the proofs.

**The connection sets.** Each $T$ is a union of pairs $\pm x$ in each class $[N]$. The table lists, for each class, one element of each pair, written $x_1x_2$ for $x=(x_1,x_2)^{\mathsf T}$; $00$ means $x=0$. The number in brackets is $|T\cap(V\times\{[N]\})|$.

| graph | $K$ | $[I]$ | $[B]$, $[2I]$ or $[\omega]$ | $[B^2]$, $[E]$ or $[\omega^2]$ | $[B^3]$, $[2E]$ or $[\omega^3]$ |
|---|---|---|---|---|---|
| $\Gamma_{42}(K_2)$ | $K_2$ | (12) 10 12 20 21 23 24 | (10) 01 02 10 11 12 | (10) 01 10 22 23 24 | (10) 01 12 20 21 22 |
| $\Gamma_{42}(K_3)$ | $K_3$ | (12) 02 13 14 20 23 24 | (10) 01 02 11 22 23 | (10) 01 02 10 11 20 | (10) 10 11 14 20 23 |
| $\Gamma_{42}(C_8)$ | $C_8$ | (12) 02 10 14 21 22 23 | (10) 12 13 14 21 23 | (10) 11 13 14 21 22 | (10) 11 14 22 23 24 |
| $\Gamma_{47}(K_2)$ | $K_2$ | (12) 01 02 12 21 22 24 | (10) 01 13 20 23 24 | (15) 00 02 10 14 21 22 23 24 | (10) 01 02 10 11 12 |
| $\Gamma_{47}(K_3)$ | $K_3$ | (12) 02 12 14 20 21 23 | (15) 00 10 11 12 13 20 21 24 | (10) 01 02 10 20 22 | (10) 10 11 14 20 23 |
| $\Gamma_{47}(C_8)$ | $C_8$ | (12) 02 10 12 21 22 24 | (10) 01 02 14 23 24 | (15) 00 11 12 13 14 21 22 24 | (10) 10 12 14 20 23 |

Write $\Gamma_{42}(K)$ and $\Gamma_{47}(K)$ for the graphs $\Gamma(K,T)$ of the table, with out-degree $|T|=42$ and $47$.

## 4. Proof of Theorem 1

Identify a subset of $G_K$ with the sum of its elements in $\mathbb Z[G_K]$.

**Lemma 2** ([3, Lemma 2]). Let $H\le G$ have order $h$, and let $D\subseteq G\setminus H$ with $HDH=D$. Then $\mathrm{Cos}(G,H,D)$ is a dsrg$(|G|/h,|D|/h,t,\lambda,\mu)$ if and only if $D^2=h\bigl(tH+\lambda D+\mu(G-H-D)\bigr)$ in $\mathbb Z[G]$.

For $\Gamma(K,T)$ the set $D=\{(x,\pm N):(x,[N])\in T\}$ satisfies $HDH=D$ because $T=-T$, and $|D|=2|T|$. So Theorem 1 for $(100,42,36,14,20)$ follows from the identity
$$D^2=72H+28D+40(G_K-H-D)$$
for any one of the three $D$ of degree 42, and for $(100,47,41,24,20)$ from $D^2=82H+48D+40(G_K-H-D)$ for any one of the three $D$ of degree 47. These are statements about explicit elements of a group of order 200. We checked them, for all six graphs, in two independent ways:
- `groupring100.py` builds $G_K$ as pairs $(w,L)$ with the affine product, forms $D$ from $T$, checks $HDH=D$ and $D\cap H=\varnothing$, and counts all products $d_1d_2$.
- `verify100.py` builds the $100\times100$ adjacency matrix of $\Gamma(K,T)$ from the arc rule above, checks that $T=-T$, that every in- and out-degree is $|T|$, every two-walk count against $(t,\lambda,\mu)$, that the graph is not symmetric, and that the generators of $G_K$ (two translations and the generators of $K$) preserve it.

The complement of a dsrg$(v,k,t,\lambda,\mu)$ is a dsrg$(v,v-k-1,v-2k+t-1,v-2k+\mu-2,v-2k+\lambda)$ [1]; here $(100,57,51,34,30)$ and $(100,52,46,24,30)$. Both scripts check the complements directly (`verify100.py` on the complement matrix, `groupring100.py` on $D'=G_K-H-D$). This proves Theorem 1. $\square$

Both scripts reject a corrupted input: replacing one pair $\pm x$ of $\Gamma_{42}(C_8)$ by another pair in the same class makes both fail. The SHA-256 hashes of the matrices written by `verify100.py` are in Section 8.

## 5. Structure

**Lemma 3.** $G_K$ has a subgroup acting regularly on $X_K$ if and only if $K$ has a subgroup of order 4 that does not contain $-I$. This holds for $K_2$ (take $\langle B\rangle$, as $B^2=\mathrm{diag}(4,1)$) and fails for $K_3$ and $C_8$.

*Proof.* A regular subgroup $Q$ has order 100. $V$ is the normal Sylow 5-subgroup of $G_K$, so $V\le Q$ and $Q=V\rtimes K'$ with $K'=Q\cap K$ of order 4. The stabiliser of $(0,[I])$ in $Q$ is $K'\cap\{\pm I\}$, so $Q$ is regular if and only if $-I\notin K'$. Conversely $V\rtimes K'$ is such a subgroup for any such $K'$. In $C_8$ the only subgroup of order 4 is $\langle\omega^2\rangle\ni\omega^4=-I$. In $K_3$ the elements of order 4 are $\pm2I$ and $\pm2E$, whose squares are $-I$, and the remaining subgroup of order 4 is $\{\pm I,\pm E\}$. $\square$

**Proposition 4 (computational).** Let $\Gamma$ be one of the six graphs.
1. $\mathrm{Aut}(\Gamma)=G_K$ (order 200), and $\mathrm{Aut}(\Gamma\circ\Gamma^{\mathsf T})$ and the automorphism group of the complement also have order 200.
2. $\Gamma$ is not isomorphic to its converse.
3. $\Gamma_{42}(K_2)$ and $\Gamma_{47}(K_2)$ are Cayley digraphs, each of both $V\rtimes\langle B\rangle\cong$ SmallGroup(100,10) and $V\rtimes\langle\mathrm{diag}(2,1)\rangle\cong C_5\times F_{20}=$ SmallGroup(100,9). The four graphs with $K=K_3$ or $C_8$ are vertex-transitive and not Cayley digraphs.
4. For each of the two parameter sets the three graphs and their three converses are pairwise non-isomorphic. So there are at least six pairwise non-isomorphic dsrg$(100,42,36,14,20)$ and at least six dsrg$(100,47,41,24,20)$, and the same for the complements.
5. The coherent closure of $\Gamma$ has rank 52, so it is the orbital configuration of $G_K$.

*Derivation.* pynauty [8] (`aut100.py`) gives the orders in 1, and $G_K$ acts faithfully, so $\mathrm{Aut}(\Gamma)=G_K$. Statement 3 follows from Lemma 3, since a digraph is a Cayley digraph exactly when its automorphism group has a regular subgroup [5]. The regular subgroups of $G_{K_2}$ are SmallGroup(100,10) and SmallGroup(100,9) (`ids100.g`). For statement 4, graphs with different $K$ have non-isomorphic automorphism groups (GAP: SmallGroup(200,40), (200,41), (200,42)), and so do their converses, which have the same automorphism groups; within one $K$, $\Gamma$ and $\Gamma^{\mathsf T}$ have different canonical forms (statement 2). The converse of $\Gamma(K,T)$ is $\Gamma(K,T^\ast)$ with $T^\ast=\{(-N^{-1}x,[N^{-1}]):(x,[N])\in T\}$. For statement 5, `wl100.py` (standard library) runs the 2-dimensional Weisfeiler–Leman refinement; it ends with 52 colour classes on ordered pairs, one of them the diagonal. Each class is a union of orbitals of $G_K$ on ordered pairs, and there are 52 orbitals, so the classes are the orbitals.

**The quotient by $V$.** The four sets $V\times\{c\}$, $c\in K/\{\pm I\}$, are the orbits of $V$ and form an equitable partition. The quotient matrix is the group matrix of $K/\{\pm I\}$ with weights $|T\cap(V\times\{c\})|$: $(12,10,10,10)$ for every $\Gamma_{42}$ and $(12,10,15,10)$ for every $\Gamma_{47}$, with the 15 on the class of order 2 in $C_4$ (for $K_2$, $C_8$) or on $[2I]$ (for $K_3$). Its nontrivial eigenvalues are $2,2,2$ and $7,-3,-3$, eigenvalues of $A$ as they must be.

## 6. A character constraint for coset dsrgs with stabiliser of order 2

This section generalises Proposition 4 of rStation paper 70 [11], which treats one action of $\mathrm{PSL}(2,7)$. It is how the search of Appendix A was made fast, and it holds for every group.

**Proposition 5.** Let $G$ be a finite group, $H=\{1,\tau\}$ a subgroup of order 2, and $D\subseteq G\setminus H$ with $HDH=D$ such that $\mathrm{Cos}(G,H,D)$ is a dsrg$(v,k,t,\lambda,\mu)$ with distinct integer eigenvalues $r$ (multiplicity $f$) and $s$ besides $k$. For an irreducible character $\chi$ put $m_\chi=(\chi(1)+\chi(\tau))/2$. Then for each $\chi\ne1$ there is an integer $a_\chi$ with $0\le a_\chi\le m_\chi$ and
$$\chi(D)=2\bigl(r\,a_\chi+s\,(m_\chi-a_\chi)\bigr),$$
$a_\chi$ is constant on Galois orbits of characters, and $\sum_{\chi\ne1}\chi(1)\,a_\chi=f$. Consequently, for every conjugacy class $C$,
$$|D\cap C|=\frac{|C|}{|G|}\Bigl(2k+\sum_{\chi\ne1}\overline{\chi(g_C)}\;2\bigl(r a_\chi+s(m_\chi-a_\chi)\bigr)\Bigr).$$

*Proof.* Let $\rho$ be a unitary representation affording $\chi\ne1$ and $P=\rho(H)/2$, the projection onto the $\tau$-fixed space $W$, of dimension $m_\chi$. From $HD=DH=2D$ we get $\rho(D)=P\rho(D)P$, and $\rho(G)=0$. Lemma 2 gives $\rho(D)^2=2(\lambda-\mu)\rho(D)+4(t-\mu)P$, so $M=\rho(D)/2$ satisfies $M^2=(\lambda-\mu)M+(t-\mu)P$. Since $r+s=\lambda-\mu$ and $rs=\mu-t$, the restriction of $M$ to $W$ is annihilated by $(x-r)(x-s)$, which has distinct roots; so it is diagonalisable with eigenvalues $r$ ($a_\chi$ times) and $s$, and $M$ vanishes on $\ker P$. Taking traces gives the formula for $\chi(D)$. It is an integer, so it is fixed by every Galois automorphism, and $\chi^\sigma(D)=\sigma(\chi(D))=\chi(D)$ forces $a_{\chi^\sigma}=a_\chi$ because $r\ne s$. Functions on $G/H$ correspond to the $F\in\mathbb C[G]$ with $FH=2F$, and the adjacency matrix acts as $F\mapsto\frac12FD^{-1}$; in the Wedderburn component of $\rho$ these $F$ become the matrices $X$ with $XP=X$, on which $A$ acts as $X\mapsto XM^\ast$. Each of the $\chi(1)$ rows of $X$ contributes the eigenvalue $r$ with multiplicity $a_\chi$, which gives $\sum\chi(1)a_\chi=f$. The class numbers follow from column orthogonality, with $\chi_1(D)=|D|=2k$. $\square$

So a pattern $(a_\chi)$ is admissible only if all the class numbers it determines are integers in $[0,|C\setminus H|]$. For our three actions this leaves few patterns:

| $K$ | patterns for $(100,42,36,14,20)$ | patterns for $(100,47,41,24,20)$ |
|---|---|---|
| $K_2$ | 5 | 5 |
| $C_8$ | 7 | 7 |
| $K_3$ | 22 | 66 |

These counts are by exact enumeration (`sieve100.py`). Write $D$ as a union of double cosets $O=HgH\ne H$ and let $x_O\in\{0,1\}$ indicate $O\subseteq D$. Then every $G_K$-invariant solution satisfies the linear equations $\sum_O x_O|O\cap C|=|D\cap C|$, for all classes $C$, of one of these patterns. Our six graphs have one pattern each, and `sieve100.py` prints it.

## 7. Limitations

- Theorem 1 rests on six explicit graphs. We do not classify the dsrgs with these parameters, not even the $G_K$-invariant ones; Proposition 4 is computational.
- Proposition 5 constrains $G$-invariant graphs on a given action only. It says nothing about graphs with small automorphism groups.
- We have no uniform description of the sets $T$ and no infinite family. Up to conjugacy, $\mathrm{GL}(2,5)$ has five subgroups of order 8, and all contain $-I$ (GAP): $C_8$, $K_2=\{\mathrm{diag}(x,\pm1)\}$, $K_3=\{\mathrm{diag}(x,\pm x)\}$, $D_8$ and $Q_8$. We found graphs for the first three only; Appendix A reports the searches for $D_8$ and $Q_8$, which are not proofs. The analogous actions $\mathbb F_q^2\rtimes K$ on the cosets of $-I$ have degree $q^2|K|/2$, which for $q=7$ and $|K|\ge4$ is at least 98.
- In the search of Appendix A, "INF" is an uncertified answer of CP-SAT and "UNK" is no answer. Only the arithmetic exclusions are proofs.

## 8. Reproducibility

The supplement contains:
- `data100.json`: the generators of $K_2$, $K_3$, $C_8$, and for each of the six graphs its parameters, its $K$ and its set $T$ as triples $[x_1,x_2,N]$ with $N$ an integer matrix.
- `verify100.py` (checker 1, standard library): builds each graph and its complement from the arc rule of Section 3, checks all two-walk counts, degrees, directedness and $G_K$-invariance, writes the matrices and prints their SHA-256.
- `groupring100.py` (checker 2, standard library): checks the identity of Lemma 2 in $\mathbb Z[G_K]$ for each $D$ and its complement.
- `aut100.py` (pynauty, numpy; ancillary): statements 1, 2 and 4 of Proposition 4.
- `wl100.py` (standard library; ancillary) and its output `wl100.out`: statement 5 of Proposition 4.
- `ids100.g` (GAP; ancillary) and its output `ids100.out`: the SmallGroup identifications, the rank 52, and the subgroups of order 100 (Lemma 3).
- `export100.g` (GAP), `chars100.jsonl` (its output), `actions100.jsonl` (the three actions as permutations), `sieve100.py` (standard library) and its output `sieve100.out`: the pattern counts of Section 6, every admissible pattern with its class numbers, and the class numbers and pattern of each of our six graphs.
- `README.md`: the commands and their expected output.

The vertex order of the matrices is $[M]$ in the order printed by `verify100.py` (with $[I]$ first), then $u$ in lexicographic order. Each file has 100 rows of 0/1 characters and a final newline.

| file | parameters | SHA-256 |
|---|---|---|
| `graph100_42_K2.txt` | $(100,42,36,14,20)$ | `6851ab218d07f17b970f54f05380f78393e7c1fec98746c1557bf3f6642d06b8` |
| `complement100_42_K2.txt` | $(100,57,51,34,30)$ | `02bb740534211cefe0c63d9fcebe9edc96673f33a223848aeb3b222d4ede29d0` |
| `graph100_42_K3.txt` | $(100,42,36,14,20)$ | `99bd598cb6a35d9d5fa845d27f5c76f39fdf8936585a555a661ed054d49da400` |
| `complement100_42_K3.txt` | $(100,57,51,34,30)$ | `11af9fda0c86e8d7456430a00fb0f4abbf01426294d38d260a3d13b599c0e1ac` |
| `graph100_42_C8.txt` | $(100,42,36,14,20)$ | `2003943c66ad2de1624c1070c945214d00c3383eba9d7c3428b531948bb94492` |
| `complement100_42_C8.txt` | $(100,57,51,34,30)$ | `e5a37a33d735699c71bff88f41563daccfa888b7cc8cfdb1adf39664f1d20019` |
| `graph100_47_K2.txt` | $(100,47,41,24,20)$ | `c97d9ee83197dea20daea779ca92d6d218d7e58fd4335a2b2d5ac6bd59c1ecb5` |
| `complement100_47_K2.txt` | $(100,52,46,24,30)$ | `5916aa47740befba7eb89d4aa002c56f6122868fa9152f8f8c3fccceb06603bb` |
| `graph100_47_K3.txt` | $(100,47,41,24,20)$ | `58dbf6e7da32c77a51ab8a85330eda662083990fc7139feca31b832644c65ce2` |
| `complement100_47_K3.txt` | $(100,52,46,24,30)$ | `d4d1e3bb1bf8d41758bfe2d3f98ca044d48510377674780d2209c6d7a6c51915` |
| `graph100_47_C8.txt` | $(100,47,41,24,20)$ | `ad7919a4c7a5735be86302e8b5d745f740f81a37b500a347d3b9df527296c791` |
| `complement100_47_C8.txt` | $(100,52,46,24,30)$ | `2a36f7a3dc4b997b741765699917a4c5854f96e3de8a8eb8a42e87602835691c` |

## Appendix A. How the graphs were found

This is provenance only; Theorem 1 rests on the explicit data and the checks of Section 4.

We searched the transitive actions of groups of order 200 on 100 points whose point stabiliser $H=\langle\tau\rangle$ has order 2 and whose orbital configuration is not commutative. (On a commutative configuration every invariant digraph has a normal adjacency matrix; with real eigenvalues it is then symmetric.) The rank of such an action is $50+|C_G(\tau)|/4\in\{51,52,55,60,75\}$. There are 38 such actions, one for each conjugacy class of core-free subgroups of order 2 in each group: 21 of rank at most 56 (7 without and 14 with a regular subgroup), which we ran first, and 17 of rank 60 or 75. Five of them have the same orbitals as another, which leaves 33. For each action and each row we first ran the arithmetic of Proposition 5. If a pattern survived, we gave CP-SAT [9] (OR-Tools 9.11, 200 s per pair) a model with one 0/1 variable per orbital, the two-walk equations, a directedness clause, and the class constraints of Section 6 with one integer $a_W$ per Galois orbit. The results for our two rows:

| actions | rank | $(100,42,36,14,20)$ | $(100,47,41,24,20)$ |
|---|---|---|---|
| $G_{K_2}$, $G_{K_3}$, $G_{C_8}$ on the cosets of $-I$ | 52 | found (7 s, 79 s, 28 s) | found (5 s, 124 s, 3 s) |
| $\mathbb F_5^2\rtimes D_8$ on the cosets of $-I$ (SmallGroup(200,43)) | 52 | INF | INF |
| $\mathbb F_5^2\rtimes Q_8$ on the cosets of $-I$ (SmallGroup(200,44)) | 52 | UNK; INF at 1800 s | UNK; INF at 1800 s |
| $\mathbb F_5^2\rtimes D_8$ on the cosets of a non-central involution of $D_8$ (2 actions) | 55 | INF | INF |
| $G_{K_2}$ on the cosets of $\mathrm{diag}(1,-1)$ or of $\mathrm{diag}(-1,1)$ (2 actions) | 60 | INF | INF |
| $G_{K_3}$ on the cosets of $\mathrm{diag}(1,-1)$ or of $\mathrm{diag}(-1,1)$ (2 actions) | 60 | UNK | UNK |
| the other 27 actions (22 distinct) | 51–75 | no admissible pattern | no admissible pattern |

The stabilisers in the table follow from the rank formula: every involution of $G_K=V\rtimes K$ is conjugate to an involution $(0,\tau)$ with $\tau\in K$, and $|C_{G_K}(\tau)|=|C_K(\tau)|\cdot|\ker(\tau-1)|$, which is 8 for $\tau=-I$ and 40 for $\tau=\mathrm{diag}(\pm1,\mp1)$ in the abelian groups $K_2$, $K_3$.

As positive controls, the same runs found known rows of the table on the same actions within the time limit, for example $(100,19,7,6,3)$, $(100,23,11,6,5)$, $(100,38,20,15,14)$, $(100,40,20,10,20)$, $(100,42,24,17,18)$ and $(100,49,29,28,20)$ on $G_{K_2}$, $(100,36,18,11,14)$ on $G_{K_2}$ at rank 60, and $(100,40,20,10,20)$ on actions of rank 60 and 75. Without the class constraints, the same CP-SAT model had returned UNK at 200 s on both rows for each of the 7 actions without a regular subgroup. We mapped the solutions to the coordinates of Section 3 by permutation isomorphisms computed in GAP, and checked that the six graphs of Section 3 are isomorphic to the solutions found ($\Gamma_{42}(K_2)$ to the converse of the solution, because of the orientation convention).

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *J. Combin. Theory Ser. A* 47 (1988) 71–100.

[2] A. E. Brouwer and S. A. Hobart. Parameters of directed strongly regular graphs. Online table, accessed 31 October 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] teichmuller_lift. Existence of directed strongly regular graphs with parameters (84,22,8,5,6) and (84,61,47,44,45). rStation paper 69, version 1 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/69

[4] V. Mikulić Crnković and M. Zubović Žutolija. Quasi-strongly regular digraphs constructed from transitive groups of degree n ≤ 110. arXiv:2609.10075 (2026).

[5] G. Sabidussi. Vertex-transitive graphs. *Monatsh. Math.* 68 (1964) 426–438.

[6] teichmuller_lift. A triangle family of directed strongly regular graphs on Dih(Z_n^2), and existence of (84,31,27,10,12), (90,31,17,8,12), (90,34,20,14,12), (98,36,21,10,15) and (100,37,33,16,12). rStation paper 50, version 2 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/50

[7] A. E. Brouwer and Š. Gyürki. Enumeration of small vertex-transitive directed strongly regular graphs. arXiv:2610.22938 (2026).

[8] B. D. McKay and A. Piperno. Practical graph isomorphism, II. *J. Symbolic Comput.* 60 (2014) 94–112. (Used through pynauty.)

[9] L. Perron and F. Didier. CP-SAT. Google OR-Tools, version 9.11 (2024). https://developers.google.com/optimization

[10] The GAP Group. GAP – Groups, Algorithms, and Programming, Version 4.13.1 (2024).

[11] teichmuller_lift. Existence of directed strongly regular graphs with parameters (84,26,12,8,8) and (84,57,43,38,40). rStation paper 70, version 1 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/70

