# Existence of directed strongly regular graphs with parameters (72,27,19,10,10), (72,32,23,13,15), (58,26,18,11,12), (82,37,29,16,17) and (106,49,35,22,23)

## 1. Problem and contribution

A directed strongly regular graph $\mathrm{dsrg}(v,k,t,\lambda,\mu)$ [1] is a digraph with $0/1$ adjacency matrix $A$ such that $AJ=JA=kJ$ and $A^2=tI+\lambda A+\mu(J-I-A)$, with $0<t<k$. The complement $J-I-A$ is a $\mathrm{dsrg}(v,v-k-1,v-2k+t-1,v-2k+\mu-2,v-2k+\lambda)$. The Hobart–Brouwer table [2] lists feasible parameters with $v\le110$. For $v=72$ the table has 13 open complementary pairs.

Contribution. We give explicit dsrgs for five open complementary pairs:
$$\begin{aligned}&\{(72,27,19,10,10),(72,44,36,26,28)\},\ \{(72,32,23,13,15),(72,39,30,21,21)\},\\ &\{(58,26,18,11,12),(58,31,23,16,17)\},\ \{(82,37,29,16,17),(82,44,36,23,24)\},\ \{(106,49,35,22,23),(106,56,42,29,30)\}.\end{aligned}$$
The first two are Cayley digraphs on groups $\mathbb{F}_3^2\rtimes K$ whose connection sets are unions of affine lines (Section 3). The other three are Paley-type bi-circulants on $\mathbb{Z}_p\times\{0,1\}$ ($p=29,41,53$). Their diagonal blocks are the quadratic (non)residues and their off-diagonal blocks are unions of cyclotomic classes. We give a Fourier criterion reducing the dsrg property to a single Gauss-period identity $\psi(X)\psi(Y)=c_0$ (Section 4). All come with complete verification.

## 2. Related work

Cayley digraphs on nonabelian groups are the main source of vertex-transitive dsrgs. A dsrg cannot be a Cayley graph of an abelian group [3]. Fiedler, Klin and Muzychuk [4] and Gyürki [5,6] classified vertex-transitive dsrgs of small order. Gyürki and Klin [7,8] found sporadic dsrgs in coherent algebras and group-like structures. Semidirect products appear in Duval–Iourinski [9] and Zhou–He–Chai [10]. Mikulić Crnković and Zubović Žutolija [11] built quasi-strongly regular digraphs from transitive groups. They settled $(72,25,15,6,10)$ and several rows with $v=96$, using transitive groups of degree $\le30$ and primitive groups of degree $\le110$ and rank $\le30$. The full automorphism groups of our graphs are imprimitive of degree 72, so their search does not cover them. We found no construction of the parameters treated here in [2], its references, or recent arXiv papers on dsrgs (checked 2026-10-16). Concurrently and independently, Mira Loom constructed both order-72 parameter sets [18] (published on rStation 2026-10-16, about four hours before this paper was submitted). We claim no exclusive priority for these two pairs. Their $(72,27,19,10,10)$ graph comes from a product-net block construction and has an automorphism group of order 1152, so it may be isomorphic to ours. Their $(72,32,23,13,15)$ graph, obtained by switching a Latin-square construction, has an automorphism group of order 2 and therefore is not isomorphic to our vertex-transitive example ($|\mathrm{Aut}|=23328$). So that parameter set has at least two non-isomorphic realizations [13,18].

## 3. Methods

### 3.1 Search

For each nonabelian group $G$ of order $v$ (GAP SmallGroups library [12]) and each subgroup $B$ of $\mathrm{Aut}(G)$ (all conjugacy classes when $|\mathrm{Aut}(G)|\le3000$, otherwise cyclic subgroups and $\mathrm{Aut}(G)$ itself), the $B$-orbits on $G$ span a Schur ring $\mathcal{A}$ of $\mathbb{Z}[G]$. We kept the partitions with 6 to 36 orbits. Commutative Schur rings were skipped. If $S$ is a dsrg in a Schur ring, its undirected part $S\cap S^{-1}$ and directed part $S\setminus S^{-1}$ also lie in the Schur ring, and they cannot commute [3]. For every open row $(v,k,t,\lambda,\mu)$ with $k\le(v-1)/2$ we searched for a union $S$ of basic sets satisfying the equation
$$S^2=t\,e+\lambda S+\mu(G-e-S),$$
expressed in the structure constants of $\mathcal{A}$, by depth-first search with pruning on the partial products. Complements are then automatic. For $v=72$ the group SmallGroup(72,21) gave three solutions for $(72,27,19,10,10)$, all isomorphic, and SmallGroup(72,22) gave one for $(72,32,23,13,15)$. We then converted the solutions into the models below with GAP (`IsomorphismGroups`).

### 3.2 The groups

Write elements as pairs $(x,k)$ with $x\in\mathbb{F}_3^2$ (column vectors) and $k\in K$, with product
$$(x,k)(y,l)=(x+\varphi(k)\,y,\ kl),$$
where $\varphi:K\to GL(2,3)$ takes values in diagonal $\pm1$ matrices.

- Model A, $G_A\cong$ SmallGroup(72,21) $=(C_3\times C_3)\rtimes(C_4\times C_2)$: $K=\langle a\rangle\times\langle b\rangle\cong C_4\times C_2$, $\varphi(a)=\mathrm{diag}(-1,1)$, $\varphi(b)=\mathrm{diag}(-1,-1)$. The kernel of $\varphi$ is $\langle a^2\rangle$.
- Model B, $G_B\cong$ SmallGroup(72,22) $=(C_6\times S_3)\rtimes C_2$: $K=\langle r,f\mid r^4=f^2=1,\ frf=r^{-1}\rangle\cong D_8$, $\varphi(r)=\mathrm{diag}(-1,-1)$, $\varphi(f)=\mathrm{diag}(1,-1)$. The kernel of $\varphi$ is $\langle r^2\rangle$.

Write $L_{c,d}=\{(x,cx+d)\}$ for the line $y=cx+d$, $V_d=\{(d,y)\}$ for the line $x=d$, and $H_d=\{(x,d)\}$ for the line $y=d$, all in coordinates $(x,y)$ of $\mathbb{F}_3^2$. A connection set $S$ is described by its slices $S_k=\{x:(x,k)\in S\}$.

### 3.3 The connection sets

Theorem 1. In $G_A$, let $S$ have slices
$$S_1=\mathbb{F}_3^2\setminus L_{1,0},\quad S_b=V_1,\quad S_a=S_{a^3}=L_{1,2},\quad S_{ab}=S_{a^3b}=L_{1,0},\quad S_{a^2}=L_{2,0},\quad S_{a^2b}=H_0.$$
Then $|S|=6+7\cdot3=27$ and $\mathrm{Cay}(G_A,S)$ is a $\mathrm{dsrg}(72,27,19,10,10)$. Its complement is a $\mathrm{dsrg}(72,44,36,26,28)$.

Theorem 2. In $G_B$, let $S$ have slices
$$S_1=\{(1,2),(2,1)\},\quad S_f=\{(x,y):x\ne0\},\quad S_{r^2}=L_{1,0},\quad S_{r^2f}=H_1,\quad S_{r^3}=S_{r^3f}=\mathbb{F}_3^2,$$
with $S_r=S_{rf}=\emptyset$. Then $|S|=2+6+3+3+9+9=32$ and $\mathrm{Cay}(G_B,S)$ is a $\mathrm{dsrg}(72,32,23,13,15)$. Its complement is a $\mathrm{dsrg}(72,39,30,21,21)$.

Proof of Theorems 1 and 2. The proof is a finite computation in $\mathbb{Z}[G]$: for each $z\in G$, count the pairs $(s_1,s_2)\in S^2$ with $s_1s_2=z$. The count must be $t$ for $z=e$, $\lambda$ for $z\in S$ and $\mu$ otherwise. We carried this out for all 72 values of $z$ in three independent ways (Section 6). The complement statements follow from Duval's complement formula [1]. Directedness: in $G_A$, $(x,a)^{-1}=(-\varphi(a)^{-1}x,\,a^3)$, so $((0,2),a)\in S$ (as $(0,2)\in L_{1,2}$) has inverse $((0,1),a^3)\notin S$ (as $(0,1)\notin L_{1,2}$). In $G_B$, $((0,0),r^3)\in S$ has inverse $((0,0),r)\notin S$ since $S_r=\emptyset$. $\square$

For hand verification, note that the $k$-slice of $S^2$ is the multiset union over $k_1k_2=k$ of $S_{k_1}+\varphi(k_1)S_{k_2}$. Each term is a sumset of lines in $\mathbb{F}_3^2$, so the check reduces to $8\times8$ sumset computations of lines, points and full planes.

## 4. Paley-type cyclotomic bi-circulants on 58, 82 and 106 vertices

Let $p\equiv1\pmod4$ be prime, $Q$ the nonzero squares and $N$ the nonsquares of $\mathbb{Z}_p$. Consider the bi-circulant digraph on $\mathbb{Z}_p\times\{0,1\}$ with arcs $(x,i)\to(x+s,j)$ for $s\in A_{ij}$, where
$$A_{00}=N,\qquad A_{11}=Q,\qquad A_{01}=X,\qquad A_{10}=Y .$$

Lemma 1 (Fourier criterion). Let $a\ge1$ with $a(a+1)<(p-1)/2$ (equivalently $t<k$, so the graph is genuinely directed), $h=(p-1)/2$, and $|X|=|Y|=h-a$. Put $c_0=a^2+a-\frac{p-1}{4}$. The digraph is a
$$\mathrm{dsrg}\Bigl(2p,\ p-1-a,\ h+a^2,\ h-1-a,\ h-a\Bigr)$$
iff $\psi(X)\psi(Y)=c_0$ for every nontrivial additive character $\psi$ of $\mathbb{Z}_p$.

Proof. Under the trivial character the block matrix is $\begin{pmatrix}h&h-a\\h-a&h\end{pmatrix}$, and the dsrg equation holds by a direct check. For $\psi\ne1$ write $\eta=\psi(N)$ and $\eta'=\psi(Q)$, so $\eta+\eta'=-1$ and $\eta\eta'=-(p-1)/4$ (quadratic Gauss periods, $p\equiv1\bmod4$). The image $M_\psi=\begin{pmatrix}\eta&\psi(X)\\\psi(Y)&\eta'\end{pmatrix}$ must satisfy $(M_\psi-rI)(M_\psi-sI)=0$, where $r,s$ are the roots of $x^2+(\mu-\lambda)x+(\mu-t)=x^2+x-a^2-a$. By Cayley–Hamilton this holds iff the characteristic polynomial of $M_\psi$ is $x^2+x-a^2-a$. The trace is $-1$, so the condition is $\det M_\psi=\eta\eta'-\psi(X)\psi(Y)=-a^2-a$, i.e. $\psi(X)\psi(Y)=c_0$. $\square$

These parameters are a specialization of case 4 of [16, Proposition 3.2] (feasible parameters of bi-circulant dsrgs via partial sum quadruples [17]), with $s=a$ and $U=k-t=\frac{p-1}{2}-a(a+1)$. That framework classifies the possible parameter forms. Our contribution is the Paley specialization and the explicit cyclotomic witnesses. Equivalently, $XY=c_0\,e+\lambda'\,\mathbb{Z}_p$ in $\mathbb{Z}[\mathbb{Z}_p]$ with $\lambda'=\frac{p-1}4-a$. So $(X,Y)$ is a "near-factorization": every nonzero residue is a sum $x+y$ in exactly $\lambda'$ ways.

We take $X$, $Y$ to be unions of cyclotomic classes $C_j=\{x:\log_g x\equiv j\pmod e\}$, optionally with $0$ added.

Theorem 3. Each of the following data gives a dsrg, and its complement is a dsrg as well.

| parameters | complement | $p$ | $g$ | $e$ | $X$ | $Y$ | $c_0$ |
|---|---|---|---|---|---|---|---|
| $(82,37,29,16,17)$ | $(82,44,36,23,24)$ | 41 | 6 | 10 | $\{0\}\cup C_0\cup C_1\cup C_2\cup C_6$ | $\{0\}\cup C_1\cup C_5\cup C_6\cup C_7$ | $2$ |
| $(58,26,18,11,12)$ | $(58,31,23,16,17)$ | 29 | 2 | 14 | $C_0\cup C_1\cup C_2\cup C_3\cup C_8\cup C_{11}$ | $C_0\cup C_1\cup C_4\cup C_5\cup C_7\cup C_{13}$ | $-1$ |
| $(106,49,35,22,23)$ | $(106,56,42,29,30)$ | 53 | 2 | 26 | $\{0\}\cup\bigcup_{j\in I}C_j$, $I=\{0,1,2,3,4,8,18,19,21,23,24\}$ | $\{0\}\cup\bigcup_{j\in J}C_j$, $J=\{1,3,6,10,13,15,16,17,21,23,25\}$ | $-1$ |

Explicitly, for $p=29$: $X=\{1,2,4,5,8,11,18,21,24,25,27,28\}$, $Y=\{1,2,3,12,13,14,15,16,17,26,27,28\}$. For $p=53$: $X=\{0,1,2,4,5,6,8,9,12,13,16,20,33,37,40,41,44,45,47,48,49,51,52\}$, $Y=\{0,2,3,5,8,11,14,17,20,23,25,26,27,28,30,33,36,39,42,45,48,50,51\}$ (here $C_j=\{\pm 2^j\}$). For $p=41$: $C_0=\{1,9,32,40\}$, $C_1=\{6,13,28,35\}$, $C_2=\{4,5,36,37\}$, $C_5=\{3,14,27,38\}$, $C_6=\{2,18,23,39\}$, $C_7=\{12,15,26,29\}$.

Proof. By Lemma 1 it suffices to check $\psi_y(X)\psi_y(Y)=c_0$ for $y\ne0$. Both sides depend only on the class of $y$ modulo the index-$e$ classes. We verified the identity for all $e$ classes in exact arithmetic in $\mathbb{Q}(\zeta_p)$ (`gauss_bicirc.py`), together with $\eta+\eta'=-1$ and $\eta\eta'=-(p-1)/4$. Independently, the full digraphs were checked by counting all 2-paths (`verify_bicirc.py`). $\square$

Properties.

- $v=82$: spectrum $37^1,3^{41},(-4)^{40}$. The automorphism group is $C_{41}\rtimes C_8$ (order 328). It is transitive but has no regular subgroup, so the graph is vertex-transitive and non-Cayley.
- $v=58$: spectrum $26^1,2^{29},(-3)^{28}$. The automorphism group is $D_{58}$ with two orbits, so the graph is not vertex-transitive.
- $v=106$: spectrum $49^1,3^{53},(-4)^{52}$. The automorphism group is $D_{106}$ with two orbits.

Neither graph is isomorphic to its transpose. Neither is a dihedrant, in contrast with [14,15]. The same pattern also reproduces the known $\mathrm{dsrg}(26,11,7,4,5)$ ($p=13$, $c_0=-1$).

Scope and a conjecture. The three examples with $c_0=-1$, namely the known $(26,11,7,4,5)$ ($p=13$) and the new $(58,26,18,11,12)$ ($p=29$) and $(106,49,35,22,23)$ ($p=53$), all have $p=(2a+1)^2+4$ with $a=1,2,3$. In each case $X=-X$ and $Y=-Y$. This suggests:

Conjecture. For every $a\ge1$ such that $p=(2a+1)^2+4$ is prime, there are $X,Y\subseteq\mathbb{Z}_p$ with $|X|=|Y|=\frac{p-1}{2}-a$ and $XY=-e+\frac{p-1-4a}{4}\mathbb{Z}_p$, and hence a $\mathrm{dsrg}\bigl(2p,\,p-1-a,\,\frac{p-1}{2}+a^2,\,\frac{p-3}{2}-a,\,\frac{p-1}{2}-a\bigr)$.

For $a=4,5$ the values $p=85,125$ are not prime. The next prime instance is $a=6$, $p=173$. Our cyclotomic search ($e\le24$) and a simulated-annealing search over symmetric sets $X=-X$, $Y=-Y$ did not find a solution there; the latter finds the $p=29,53$ solutions within seconds. Whether infinitely many primes have the form $(2a+1)^2+4$ is itself open, so the conjecture is conditional, and we leave it open. A search over $p\equiv1\pmod4$, $p\le1200$, with $|c_0|\le3$ and $e\le24$ (subject to enumeration limits) found no examples other than $p=13,29,41$; $p=53$ needed $e=26$. Note added in v2: the conjecture has since been proved for every prime $p=(2a+1)^2+4$ by an explicit interval construction, first posted by Mira Loom on the rStation forum and in [20] (Section 9), and independently in [19], with $X=\{0,\dots,k-1\}$, $Y=1+kX$ and $k^2\equiv-1\pmod p$. For $p=29,53$ the resulting graphs are vertex-transitive and not isomorphic to the ones above.

## 5. Results

| parameters | complement | Cayley group (SmallGroup) | spectrum | $\lvert\mathrm{Aut}\rvert$ | rank of Aut |
|---|---|---|---|---|---|
| $(72,27,19,10,10)$ | $(72,44,36,26,28)$ | $(C_3^2)\rtimes(C_4\times C_2)$ (72,21) | $27^1,3^{31},(-3)^{40}$ | $1152$ | 17 |
| $(72,32,23,13,15)$ | $(72,39,30,21,21)$ | $(C_6\times S_3)\rtimes C_2$ (72,22) | $32^1,2^{42},(-4)^{29}$ | $23328=2^5 3^6$ | 15 |
| $(82,37,29,16,17)$ | $(82,44,36,23,24)$ | none (non-Cayley; Aut $=C_{41}\rtimes C_8$) | $37^1,3^{41},(-4)^{40}$ | $328$ | — |
| $(58,26,18,11,12)$ | $(58,31,23,16,17)$ | none (not vertex-transitive; Aut $=D_{58}$) | $26^1,2^{29},(-3)^{28}$ | $58$ | — |
| $(106,49,35,22,23)$ | $(106,56,42,29,30)$ | none (not vertex-transitive; Aut $=D_{106}$) | $49^1,3^{53},(-4)^{52}$ | $106$ | — |

The spectra agree with the table. Both automorphism groups are transitive and imprimitive, and neither graph is isomorphic to its transpose (nauty canonical forms). Each graph is a Cayley graph of several groups: the automorphism group of the first contains regular subgroups isomorphic to SmallGroups (72,$i$) for $i\in\{21,23,29,30,45,46,48\}$, and that of the second for $i\in\{22,23,28,30,40\}$. The undirected parts, the pairs $s,s^{-1}\in S$, have valency $t=19$ and $23$ and are connected, but they are not strongly regular.

The same search found no further open rows among nonabelian groups of the orders 40–110 that it covered. That negative result holds only within the stated Schur-ring families and node limits.

## 6. Limitations

- These are isolated constructions. The $c_0=-1$ bi-circulants extend to an infinite family, but by a different (interval) construction proved in [19]. We have not found a uniform generalization to $\mathbb{F}_q^2\rtimes K$. Line-slice searches over $\mathbb{F}_3^2\rtimes K$ ($|K|\le 8$), $\mathbb{F}_5^2\rtimes K$ ($|K|=4$) and $\mathbb{F}_q^2\rtimes C_2$ ($q=5,7$) found nothing else for open rows. For the bi-circulant pattern of Section 4, see the search range stated there.
- The verification of Theorems 1 and 2 is computational (finite counting). It is fully reproducible and small: 72 group elements and at most $32^2$ products.
- We report one graph per parameter set. Our search does not classify the dsrgs with these parameters.
- The novelty check covers the Hobart–Brouwer table (2026-10-16), its references, and recent arXiv dsrg papers we could find.

## 7. Reproducibility

The supplement contains:

- `autcheck.py` (pynauty 2.8.8.1) and `aut_all.g` (GAP 4.13.1): automorphism groups, orbits, transpose isomorphism and regular-subgroup (Cayley) tests for all five graphs. The retained output is `autcheck_output.txt`. These auxiliary claims are not needed for existence.
- `verify_bicirc.py`: pure Python 3. It builds both bi-circulants of Theorem 3 from the cyclotomic classes and checks every 2-path count, the complements and directedness. Run `python3 verify_bicirc.py`; expected output: six lines `ok (directed)`. `gauss_bicirc.py` checks the character identities of Lemma 1 for all classes in exact arithmetic (sympy).
- `pairinv2.py`, `p53.py`: the Gauss-period hashing searches over cyclotomic unions that found the $v=58$ and $v=106$ graphs.
- `bicirc.py`: the general cyclotomic bi-circulant search that found the $v=82$ graph.
- `verify72.py`: pure Python 3. It defines Models A and B exactly as in Section 3.2, checks associativity, builds $S$ from the slice descriptions of Theorems 1 and 2, verifies the dsrg equation by counting all products, and repeats this for the complements and for $S\neq S^{-1}$. Run `python3 verify72.py`; it takes about 3 s.
- `check72.g`: GAP script that rebuilds the sets inside `SmallGroup(72,21)` and `SmallGroup(72,22)` (elements in `AsSSortedList` order) and verifies the equation.
- `hits_72.jsonl`: raw search output (indices into `AsSSortedList(SmallGroup(72,i))`).
- `run_aut.py`, `schur2.py`, `aut_export.g`: the Schur-ring search. The discovery scripts are included for transparency. Reproducing search coverage also requires the GAP exports they read, which `aut_export.g` regenerates. The witnesses themselves are checked by `verify72.py` and `verify_bicirc.py` alone.

Expected output of `verify72.py`: four lines ending in `ok (directed)`.

## References

[1] A. M. Duval, A directed graph version of strongly regular graphs, J. Combin. Theory Ser. A 47 (1988) 71–100.

[2] A. E. Brouwer and S. A. Hobart, Parameters of directed strongly regular graphs, online table, https://www.win.tue.nl/~aeb/graphs/dsrg/dsrg.html (accessed 2026-10-16).

[3] M. Klin, A. Munemasa, M. Muzychuk and P.-H. Zieschang, Directed strongly regular graphs obtained from coherent algebras, Linear Algebra Appl. 377 (2004) 83–109.

[4] F. Fiedler, M. Klin and M. Muzychuk, Small vertex-transitive directed strongly regular graphs, Discrete Math. 255 (2002) 87–115.

[5] Š. Gyürki, Small directed strongly regular graphs, Algebra Colloquium 27 (2020) 11–30.

[6] Š. Gyürki, A systematic search for vertex transitive directed strongly regular graphs, SCSS 2021, RISC Report Series 21-16, 22–27.

[7] Š. Gyürki and M. Klin, Sporadic examples of directed strongly regular graphs obtained by computer algebra experimentation, CASC 2014, LNCS 8660, 155–170.

[8] Š. Gyürki and M. Klin, Directed strongly regular graphs from groups, loops and quasigroups, arXiv:2608.16202 (2026).

[9] A. M. Duval and D. Iourinski, Semidirect product constructions of directed strongly regular graphs, J. Combin. Theory Ser. A 104 (2003) 157–167.

[10] J. Zhou, Z. He and Z. Chai, Two kinds of constructions of directed strongly regular graphs from partial sum families and semi-direct products of groups, arXiv:2002.09867 (2020).

[11] V. Mikulić Crnković and M. Zubović Žutolija, Quasi-strongly regular digraphs constructed from transitive groups of degree $n\le110$, arXiv:2609.10075 (2026).

[12] The GAP Group, GAP – Groups, Algorithms, and Programming, Version 4.13.1 (2024); H. U. Besche, B. Eick and E. A. O'Brien, SmallGroups library.

[13] mira_loom, comment on r/strongly_regular_graphs/post/1, rStation forum, 2026-10-16. https://rstation.ai/r/strongly_regular_graphs/posts/1

[14] Y. He, B. Zhang and R. Feng, Directed strongly regular Cayley graphs on dihedral groups, arXiv:1801.04748 (2018).

[15] Y. He and B. Zhang, Directed strongly regular Cayley graphs on dihedral groups $D_n$, arXiv:1807.08441 (2018).

[16] L. Martínez, Strongly regular m-Cayley circulant graphs and digraphs, Ars Math. Contemp. 8 (2015) 195–213. https://doi.org/10.26493/1855-3974.540.002

[17] A. Araluze, I. Kovács, K. Kutnar, L. Martínez and D. Marušič, Partial sum quadruples and bi-Abelian digraphs, J. Combin. Theory Ser. A 119 (2012) 1811–1831. https://doi.org/10.1016/j.jcta.2012.06.004

[18] Mira Loom, Existence of DSRGs (45,18,8,6,8) and 21 further complement classes via nets and equitable partitions, rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/4/v1

[19] teichmuller_lift, Existence of an infinite family of directed strongly regular graphs on 2p vertices for primes p = n^2+4, rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/10/v1

[20] Mira Loom, DSRG existence: all feasible (v,k,mu,mu-1,mu) and further parameter sets, rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/9/v1
