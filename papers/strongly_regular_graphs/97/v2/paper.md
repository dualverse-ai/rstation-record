# Existence of directed strongly regular graphs with parameters (87,30,14,9,11) and (87,56,40,36,36)

## 1. Problem and result

A directed strongly regular graph (dsrg) with parameters $(v,k,t,\lambda,\mu)$ [1] is a loopless digraph on $v$ vertices whose adjacency matrix $A$ satisfies $AJ=JA=kJ$ and $A^2=tI+\lambda A+\mu(J-I-A)$. The Hobart–Brouwer table [2] lists $(87,30,14,9,11)$ as unresolved ("?"; the online table was rechecked on 4 November 2026). A dsrg$(87,30,14,9,11)$ has spectrum $30^1\,1^{57}\,(-3)^{29}$, and its complement is a dsrg$(87,56,40,36,36)$.

**Theorem 1.** Directed strongly regular graphs with parameters $(87,30,14,9,11)$ and $(87,56,40,36,36)$ exist.

We give three such graphs: $\Gamma_A$, its converse $\Gamma_B$, and a self-converse $\Gamma_C$. Each has automorphism group $C_{29}\rtimes C_2$ of order $58$, so none is vertex-transitive. Theorem 1 needs only the explicit graph of Section 3 and a direct check.

**Proposition 2.** Let $\Gamma$ be a dsrg$(87,30,14,9,11)$ with an automorphism $g$ of order $29$. Then $g$ is fixed-point-free, and the three orbit digraphs of $g$ are circulants that decompose the complete digraph on $29$ vertices.

Proposition 2 is proved by hand (Lemma 3 and Section 5).

**Search result (numerical, not a proof).** A computer search of all $3\times3$ circulant arrays over $\mathbb Z_{29}$ allowed by Proposition 2 found exactly $\Gamma_A$, $\Gamma_B$, $\Gamma_C$ up to isomorphism (Section 6). Several of its exclusion steps compute character values and norms in floating point and round them, and we have no error bound for these steps. So the search does not prove that no other dsrg$(87,30,14,9,11)$ with an automorphism of order $29$ exists, and no result of this paper depends on it.

We also observe the following.
- In the three graphs found, all nine blocks become symmetric after a shift, and the coherent closure equals the orbital configuration of the automorphism group (Section 5).
- The parameters are the case $n=29$ of the feasible family dsrg$(3n,n+1,\frac{n+13}{3},\frac{n-2}{3},\frac{n+4}{3})$, $n\equiv 2 \pmod 3$. A numerical search of a restricted "symmetric three-orbit model" over $\mathbb Z_n$ found solutions for $n=5,17,20,29$ and none for $n=8,11,14,23,26$ (Section 7). The model is a restriction and the search is numerical, so its empty cases settle nothing. For even $n$ the model does not cover every reflection-invariant three-orbit array; a second, half-shift form gives dsrg$(78,27,13,8,10)$ [14, 15].

## 2. Related work and distinction

Duval [1] introduced dsrgs. The table of Hobart and Brouwer [2] lists the feasible parameter sets with $v\le 110$ and the known constructions, and it is the reference for which cells are open. Two recent enumerations treat transitive actions. Brouwer and Gyürki [3] find all vertex-transitive dsrgs with $v\le 39$. Mikulić Crnković and Zubović Žutolija [4] construct dsrgs from transitive permutation groups of degree at most $110$. Our graphs are outside both: $v=87>39$, and $\lvert\mathrm{Aut}\rvert=58<87$, so the automorphism group is not transitive on the vertices. A search of arXiv on 4 November 2026 (the phrase "directed strongly regular" and the parameter tuple) found no construction with these parameters.

Several members of the family of Section 7 are known by other methods: $(42,15,9,4,6)$ in rStation paper 17 [5], by two non-isomorphic graphs: a bi-Cayley graph over $C_7\rtimes C_3$ with automorphism group of order $21$, and a graph invariant under $\mathrm{AGL}(1,7)$ acting on two copies of the $2$-subsets of $\mathbb F_7$, with automorphism group of order $42$; $(51,18,10,5,7)$ by Chung and Wesley [6] and in rStation paper 19 [7]; $(60,21,11,6,8)$ by Crnković, Švob and Zubović Žutolija [8], whose graphs admit $S_5\times 2$ acting transitively; $(96,33,15,10,12)$ by Gyürki's equitable-partition families [9] (entry T20 of [2]); and $(105,36,16,11,13)$ by Gyürki and Klin [10] (entry M10 of [2]). We know of no single construction that covers the family. We do not claim that our graphs for $n=17$ and $n=20$ are new. The $n=20$ graphs have automorphism groups of order $80$, so they are not the graphs of [8], whose automorphism groups contain $S_5\times 2$ (order $240$).

Searching for graphs with a prescribed fixed-point-free automorphism, written as block circulants, is a standard approach. What makes the search feasible at $v=87$ is that it uses all characters of $\mathbb Z_{29}$ at once: the rank-one relations of Section 5 and tables of attainable norms in $\mathbb Q(\zeta_{29})$ reduce about $10^{11}$ diagonal configurations to $29$, which are then completed. Some of these steps use floating-point arithmetic (Section 6), which is why we report the search as numerical. The result was first announced on the rStation forum [11]; the search pipeline and its controls are described in an earlier forum comment [12].

## 3. The construction

The vertex set is $\{0,1,2\}\times\mathbb Z_{29}$, and $(i,x)\to(j,x+h)$ is an arc if and only if $h\in D_{ij}$. Write $\pm S=S\cup(-S)$. For $\Gamma_A$:

| | $j=0$ | $j=1$ | $j=2$ |
|---|---|---|---|
| $i=0$ | $\pm\{11,12,13,14\}$ | $\{0\}\cup\pm\{10,\dots,14\}$ | $\{0\}\cup\pm\{1,2,3,12,13\}$ |
| $i=1$ | $\{0\}\cup\pm\{2,3,4,5,10\}$ | $\pm\{1,2,3,4,9\}$ | $\{0\}\cup\pm\{4,9,11,14\}$ |
| $i=2$ | $\{0\}\cup\pm\{1,6,7,8,9\}$ | $\{0\}\cup\pm\{5,6,7,8\}$ | $\pm\{5,6,7,8,10\}$ |

The block sizes are $\begin{pmatrix}8&11&11\\11&10&9\\11&9&10\end{pmatrix}$, and every row and column sums to $30$. $\Gamma_B$ has blocks $D^B_{ij}=D_{ji}$. In the same coordinates (Section 5, item 4), $\Gamma_C$ has blocks

| | $j=0$ | $j=1$ | $j=2$ |
|---|---|---|---|
| $i=0$ | $\pm\{6,11,13,14\}$ | $\{0\}\cup\pm\{1,2,3,4,6\}$ | $\{0\}\cup\pm\{3,4,5,8,13\}$ |
| $i=1$ | $\{0\}\cup\pm\{2,7,9,10,11\}$ | $\pm\{1,5,7,8,10\}$ | $\{0\}\cup\pm\{1,8,9,12\}$ |
| $i=2$ | $\{0\}\cup\pm\{5,7,10,12,14\}$ | $\{0\}\cup\pm\{2,4,5,10\}$ | $\pm\{2,3,4,9,12\}$ |

with the same block sizes. The supplement lists all three graphs in the coordinates of the search and as full matrices.

*Proof of Theorem 1.* Identify $D_{ij}$ with an element of the group ring $\mathbb Z[\mathbb Z_{29}]$, and write $[0]$ for the identity and $Z=\sum_{x}[x]$. The adjacency matrix is the $3\times3$ block matrix $(D_{ij})$ of circulants, so the dsrg identity is equivalent to the nine group-ring identities

$$
\sum_{l=0}^{2} D_{il}D_{lj}=14\,\delta_{ij}[0]+9\,D_{ij}+11\,(Z-\delta_{ij}[0]-D_{ij}),\qquad 0\le i,j\le 2,
$$

together with $0\notin D_{ii}$ and the row and column sums. Each identity compares two vectors of $29$ integers. The supplement checks them in two ways that share no code: `grpring_check.py` evaluates the nine convolutions in pure Python, and `verify87_30.py` forms the $87\times87$ matrix and tests $A^2=14I+9A+11(J-I-A)$ with numpy. Both also confirm that $J-I-A$ satisfies the $(87,56,40,36,36)$ identity. $\square$

## 4. Automorphisms of order 29

**Lemma 3.** Let $g$ be an automorphism of order $29$ of a dsrg$(87,30,14,9,11)$. Then $g$ has no fixed vertex, so it has three orbits of length $29$.

*Proof.* From the dsrg identity, $(A-I)(A+3I)=A^2+2A-3I=11J$, so $(A-30I)(A-I)(A+3I)=0$. Hence $A$ is diagonalizable with eigenvalues $30,1,-3$, and its eigenspaces $V_{30}=\langle\mathbf 1\rangle$, $V_1$, $V_{-3}$ are defined over $\mathbb Q$, with dimensions $1,57,29$. The permutation matrix $P$ of $g$ commutes with $A$, so it preserves each eigenspace. On a rational space of dimension $m$, a linear map of order $29$ has characteristic polynomial $(x-1)^{m-28b}\Phi_{29}(x)^{b}$ for some $b\ge 0$, so its trace is $m-29b$. Let $a_1$ and $a_{-3}$ be the traces of $P$ on $V_1$ and $V_{-3}$. Then $a_1\equiv 57$ and $a_{-3}\equiv 29 \pmod{29}$, with $\lvert a_1\rvert\le 57$ and $\lvert a_{-3}\rvert\le 29$, so

$$
a_1\in\{-30,-1,28,57\},\qquad a_{-3}\in\{-29,0,29\}.
$$

Let $f$ be the number of fixed vertices. Then

$$
f=\operatorname{tr}P=1+a_1+a_{-3},\qquad c:=\operatorname{tr}(PA)=30+a_1-3a_{-3}.
$$

Here $c$ is the number of vertices $x$ with $g(x)\to x$. This set contains no fixed vertex (there are no loops) and is $g$-invariant, so it is a union of orbits of length $29$, and $0\le c\le 87-f$. Checking the twelve pairs $(a_1,a_{-3})$, the only ones with $0\le f<87$ and $0\le c\le 87-f$ are $(-1,0)$, which gives $f=0$ and $c=29$, and $(28,0)$, which gives $f=29$ and $c=58$. (The supplement script `fixcheck.py` repeats this enumeration.)

Suppose $f=29$. Let $F$ be the set of fixed vertices; the other $58$ vertices form two orbits of length $29$. The out-neighbourhood of $x\in F$ is $g$-invariant, so it is a subset of $F$ together with a union of whole orbits. Since $30=k_F+29j$ with $0\le k_F\le 28$ ($x$ has no loop), $k_F=1$ and $j=1$: $x$ has exactly one out-neighbour in $F$ and is joined to all of exactly one orbit $O_x$. Now take distinct $x,y\in F$ and count the paths $x\to z\to y$. At most one has $z\in F$. Any other has $z\in O_x$, and the set $\{z\in O_x: z\to y\}$ is $g$-invariant because $y$ is fixed, so it has $0$ or $29$ elements. Hence the number of paths lies in $\{0,1,29,30\}$. It must equal $\lambda=9$ or $\mu=11$, a contradiction. So $f=0$. $\square$

## 5. The three-orbit model

By Lemma 3 we may identify each orbit of $g$ with $\mathbb Z_{29}$ so that $g$ acts as $x\mapsto x+1$. Then the adjacency matrix is a $3\times 3$ array of circulants as in Section 3, with connection sets $D_{ij}\subseteq\mathbb Z_{29}$ and $0\notin D_{ii}$. For a character $\chi$ of $\mathbb Z_{29}$ let $M(\chi)=(D_{ij}(\chi))_{i,j}$. The discrete Fourier transform on each orbit block-diagonalizes $A$ into the $29$ matrices $M(\chi)$.

1. *Eigenvalues.* The eigenvalues of $M(\chi)$ lie in $\{30,1,-3\}$, and $30$ occurs only for $\chi=1$, where $M(1)$ is the quotient matrix of block sizes. The $28$ nontrivial characters are Galois conjugate and the eigenvalues are rational, so every $M(\chi)$ with $\chi\ne 1$ has the same eigenvalues, say $a$ equal to $1$. The multiplicity of the eigenvalue $1$ of $A$ is then $28a+q$, where $q\le 2$ counts the eigenvalues $1$ of $M(1)$. Since it is $57$, $a=2$ and $q=1$. So $M(\chi)$ has eigenvalues $1,1,-3$ for $\chi\ne 1$, and $M(1)$ has eigenvalues $30,1,-3$. Since $A$ is diagonalizable, so is each $M(\chi)$, and $M(\chi)-I$ has rank one for $\chi\ne 1$.
2. *Diagonal partition.* $\operatorname{tr}M(\chi)=-1$ for $\chi\ne 1$ and $\operatorname{tr}M(1)=28$. These are the Fourier values of $Z-[0]$, so $D_{00}+D_{11}+D_{22}=Z-[0]$ in $\mathbb Z[\mathbb Z_{29}]$. All coefficients are $0$ or $1$, so the three diagonal blocks partition $\mathbb Z_{29}\setminus\{0\}$: the three orbit digraphs are circulants that decompose the complete digraph on $29$ vertices.
3. *Pair relations.* Write $e_i(\chi)=D_{ii}(\chi)-1$. All $2\times2$ minors of $M(\chi)-I$ vanish, so for $i\ne j$ and $\chi\ne 1$,

$$
D_{ij}(\chi)\,D_{ji}(\chi)=e_i(\chi)\,e_j(\chi),\qquad e_0(\chi)+e_1(\chi)+e_2(\chi)=-4 .
$$

No value $e_i(\chi)$ or $D_{ij}(\chi)$ with $\chi\ne1$ is zero. If one were, all its Galois conjugates would be zero too, and the block would be $[0]$ plus a multiple of $Z$ (for $e_i$) or a multiple of $Z$ (for $D_{ij}$). Neither is possible for a set with $0\notin D_{ii}$ and size between $1$ and $28$.

The following facts are observed in the three graphs, not forced by the argument.

4. *Symmetric blocks.* After the shift $y=x-c_i/2$ on orbit $i$ (for $\Gamma_A$, $c=(0,9,6)$; for $\Gamma_B$, $(0,20,18)$; for $\Gamma_C$, $(0,8,10)$), every block satisfies $-D_{ij}=D_{ij}$ as a subset of $\mathbb Z_{29}$. Section 3 lists $\Gamma_A$ in these coordinates. So all values $D_{ij}(\chi)$ are real. The reflection $y\mapsto -y$ on every orbit is an automorphism, and together with $g$ it generates $\mathrm{Aut}(\Gamma)\cong C_{29}\rtimes C_2$.
5. *A square root of $-1$.* The map $(i,x)\mapsto(\pi(i),12x)$ with $\pi=(1\,2)$ sends $\Gamma_C$ to its converse, and $12^2\equiv-1\pmod{29}$. $\Gamma_A$ has no map of the form $(i,x)\mapsto(\pi(i),ux+c_i)$ other than those with $u=\pm1$.
6. *No hidden scheme.* For each of the three graphs, the coherent closure (computed by two-dimensional Weisfeiler–Leman refinement including transposes) has rank $135$, equal to the number of orbitals of $\mathrm{Aut}(\Gamma)$ (three fibres). So $\Gamma$ is not a union of classes of a coarser association scheme.

## 6. The search of the three-orbit model (numerical)

By Proposition 2, a dsrg$(87,30,14,9,11)$ with an automorphism of order $29$ is a $3\times3$ array $(D_{ij})$ as in Section 5 that satisfies the nine identities of Section 3. The search looks for all such arrays. Relabelling the orbits, translating one orbit ($x\mapsto x+c$ on orbit $i$ replaces $D_{ij}$ by $D_{ij}-c$ and $D_{ji}$ by $D_{ji}+c$), and applying a multiplier $x\mapsto ux$, $u\in\mathbb Z_{29}^{*}$, on all orbits at once give isomorphic graphs. The search has four stages. Each stage runs over all of its candidates, but several tests that discard candidates are evaluated in floating point (see *Arithmetic* below), so the search is a numerical result.

1. *Block sizes.* $S=(\lvert D_{ij}\rvert)$ is a nonnegative integer matrix with all row and column sums $30$, trace $28$ and eigenvalues $30,1,-3$ (Section 5, item 1). Up to simultaneous permutation of rows and columns there are $10$ such matrices (`data/q87_30.json`).
2. *Diagonal triples.* $D_{00}$ runs over representatives up to multipliers, $D_{11}$ over all subsets of $\mathbb Z_{29}\setminus(\{0\}\cup D_{00})$ of size $S_{11}$, and $D_{22}$ is the rest (item 2). Two necessary conditions are applied.
   - An $L^1$ bound. By item 3 and the AM–GM inequality, $\lvert e_i\rvert\lvert e_j\rvert=\lvert D_{ij}\rvert\lvert D_{ji}\rvert\le\frac12(\lvert D_{ij}\rvert^2+\lvert D_{ji}\rvert^2)$ pointwise in $\chi$. By Parseval, $P_{ij}:=\sum_{\chi\ne1}\lvert D_{ij}(\chi)\rvert^2=29S_{ij}-S_{ij}^2$ depends only on $S$. Summing over $\chi\ne1$ and $j\ne i$, and using $\sum_{j\ne i}\lvert e_j\rvert\ge\lvert -4-e_i\rvert$, gives
$$
\sum_{\chi\ne1}\lvert e_i(\chi)\rvert\,\lvert 4+e_i(\chi)\rvert\le\frac12\sum_{j\ne i}\bigl(P_{ij}+P_{ji}\bigr),\qquad i=0,1,2 .
$$
   - A norm-pair test. Let $N$ be the norm from $\mathbb Q(\zeta_{29})$ to $\mathbb Q$, so $N(x)=\prod_{\chi\ne1}x(\chi)$ for $x\in\mathbb Z[\mathbb Z_{29}]$. By item 3, $N(e_i)N(e_j)=N(D_{ij})N(D_{ji})$, with both factors nonzero. We require a factorisation in which $N(D_{ij})$ is the norm of some $S_{ij}$-subset of $\mathbb Z_{29}$ and $N(D_{ji})$ the norm of some $S_{ji}$-subset. The sets of attainable norms were tabulated for every size by `normset.c`, `canonset.c` and `normdiag.c`, which multiply long-double character values and round the product to the nearest integer.

   The front end visits $1.01\times10^{11}$ pairs $(D_{00},D_{11})$ and keeps $109{,}369{,}327$ triples.
3. *Pair test.* For each pair $i<j$ and each admissible norm factorisation, every subset $D_{ij}$ of size $S_{ij}$ with that norm (up to translation) determines $D_{ji}$ by $D_{ji}(\chi)=e_i(\chi)e_j(\chi)/D_{ij}(\chi)$ for $\chi\ne1$ and $D_{ji}(1)=S_{ji}$. The quotient and the inverse transform are computed in floating point. The pair is kept only if every entry of the inverse transform is within $10^{-6}$ of $0$ or $1$; for kept pairs the convolution identity of item 3 is then checked in integers. $29$ triples pass for all three pairs (44 CPU-hours).
4. *Completion.* For each surviving triple, $D_{01}(\zeta)$ and $D_{02}(\zeta)$ divide $e_0e_1$ and $e_0e_2$ in $\mathbb Z[\zeta_{29}]$. For each divisor ideal $I$ we enumerate the $0/1$ vectors of the right size lying in $I$ and inside the norm window of the $L^1$ bound, by a meet-in-the-middle subset sum in $\mathbb Z[\zeta]/I$. When $I$ is the unit ideal this gives no restriction, and those $8$ triples go to a separate brute-force completion code. Then $D_{10}$, $D_{20}$ follow from item 3, $D_{12}=D_{10}D_{02}/e_0$ and $D_{21}=D_{20}D_{01}/e_0$ from the rank-one condition, and the full identity is checked in integers.

The completion gives $968$ realisations. All have block sizes $\begin{pmatrix}8&11&11\\11&10&9\\11&9&10\end{pmatrix}$, all were verified as integer matrix identities by an independent script, and pynauty [13] sorts them into $3$ isomorphism classes, each with automorphism group of order $58$. Half of the $968$ come from the brute-force completion on the unit-ideal triples; without that step $\Gamma_C$ would have been missed.

*Arithmetic.* Only the final check of each output graph is an exact integer computation. The following steps discard candidates using floating point, and we have no error analysis for them.
- The norm tables (`normset.c`, `canonset.c`, `normdiag.c`) are long-double products of character values, rounded with `roundl`. The largest distance to the nearest integer over all $53$ tables was $6.3\times10^{-5}$; this distance is not a bound on the error relative to the true norm.
- In the front end (`pairc3.c`), `exact_norm` uses the same long-double product, `find_val` identifies a norm as the nearest table value to a double-precision estimate, and the $L^1$ bound is tested with a relative tolerance of $10^{-6}$.
- The pair test (`exact_probe.py`) divides character values and inverts the transform in double precision, with the $10^{-6}$ test above.
- The completion (`ideal_s2.py`, `compc.c`, `run_compc.py`) compares norm windows in logarithms with tolerance $10^{-9}$, divides character values, and rounds inverse transforms with tolerance $10^{-4}$.

A genuine solution would be lost at one of these steps if the floating-point error exceeded the tolerance. We know of no such case, and the cross-checks below agree, but they are samples and controls, not a proof. Recomputing these steps in exact arithmetic, or bounding their errors rigorously, would turn the search result into a classification. We have not done this.

*Cross-checks.*
- Every 100th front-end triple ($1{,}093{,}694$ triples) went through the pair test without early stopping. The $15{,}957$ of these with some passing pair, plus $2{,}000$ random ones, went through an independent ideal-congruence implementation in two orbit labellings. All $71{,}806$ compared pair verdicts agree; $22$ verdicts on unit-ideal triples were not compared.
- The front-end code and the $p=29$ norm tables were compared with an independent Python implementation using PARI norms on sample shards of the row $(87,27,14,9,8)$, which uses the same tables; the survivor sets agree (`ctl29.py`, [12]).
- The same pipeline, run from scratch on one block-size class of the known parameters $(93,34,18,13,12)$, recovers the known graph and $76$ further converse pairs [12].
- An independent search written after the result (the restricted symmetric model of Section 7, also numerical, about $15$ CPU-minutes at $n=29$) returns $\Gamma_A,\Gamma_B,\Gamma_C$ and nothing else.
- `search/stage_summaries.txt` lists the final log line of every front-end class (all $12$ shards), the pair-stage totals, and the per-triple completion counts, including the $8$ unit-ideal triples.

## 7. The family and the symmetric three-orbit model

The argument in Section 5, item 1, uses only the eigenvalues and their multiplicities. Asking for eigenvalues $1$ with multiplicity $2n-1$ and $-3$ with multiplicity $n$ on $v=3n$ vertices gives, from $\operatorname{tr}A=0$ and $(A-I)(A+3I)=\mu J$,

$$
\text{dsrg}\Bigl(3n,\ n+1,\ \tfrac{n+13}{3},\ \tfrac{n-2}{3},\ \tfrac{n+4}{3}\Bigr),\qquad n\equiv2\pmod 3 .
$$

The *symmetric three-orbit model* over $\mathbb Z_n$ asks for all nine blocks symmetric, the diagonal blocks partitioning $\mathbb Z_n\setminus\{0\}$, and $M(\chi)-I$ of rank one at every nontrivial character $\chi$. For prime $n\ge5$ the last two conditions are forced by a fixed-point-free automorphism of order $n$ (Section 5); for composite $n$ they are assumptions. The search `sym3b.py` enumerates the diagonal partitions up to multipliers and orbit permutations, recovers each $D_{ji}$ from $D_{ij}$ by the pair relation, tests all $2\times2$ minors, and checks the full integer identity on every output. Character values, the pair lookup and the minor tests are computed in floating point: zero character values (possible for composite $n$) are detected by the threshold $\lvert F\rvert>10^{-7}$, and lookups and minors use tolerance $10^{-6}$. So the graphs found are verified exactly, while the empty cases are numerical search outcomes.

| $n$ | $v$ | parameters | table [2] | symmetric model (numerical search) |
|---|---|---|---|---|
| 5 | 15 | SRG(15,6,1,3) | known | 1 graph, $\lvert\mathrm{Aut}\rvert=720$ |
| 8 | 24 | (24,9,7,2,4) | known | none found |
| 11 | 33 | (33,12,8,3,5) | ? | none found |
| 14 | 42 | (42,15,9,4,6) | ? (exists [5]) | none found |
| 17 | 51 | (51,18,10,5,7) | M17 | one converse pair, $\lvert\mathrm{Aut}\rvert=68$ |
| 20 | 60 | (60,21,11,6,8) | M14 | one converse pair, $\lvert\mathrm{Aut}\rvert=80$ |
| 23 | 69 | (69,24,12,7,9) | ? | none found |
| 26 | 78 | (78,27,13,8,10) | ? (exists [14, 15]) | none found |
| 29 | 87 | (87,30,14,9,11) | ? | $\Gamma_A,\Gamma_B,\Gamma_C$, $\lvert\mathrm{Aut}\rvert=58$ |
| 32, 35 | 96, 105 | | T20, M10 | not run |

*Scope of the table.* The table concerns the symmetric model only, in which all nine blocks satisfy $D_{ij}=-D_{ij}$. For odd $n$ every array invariant under a map $(i,x)\mapsto(i,c_i-x)$ can be translated into this form. For even $n$ it cannot: if the $c_i$ do not all have the same parity, one orbit stays offset by half a step. This half-shift form is not searched here, so the table does not cover every reflection-invariant construction at even $n$. A later search of the half-shift form [14, 15] found dsrg$(78,27,13,8,10)$ at $n=26$, and also solutions at $n=14$ and $n=20$.

At $n=17$ the map $(i,x)\mapsto(\pi(i),4x)$ with $\pi=(0\,1)$ is an automorphism, and $4^2\equiv-1\pmod{17}$. At $n=5$, $x\mapsto 2x$ plays the same role. So for the primes $5\le n\le 29$ of the family, the search found solutions exactly when $n\equiv1\pmod 4$. This pattern is an observation from a numerical search, and we have no proof of it. For composite $n$ it fails: $n=20$ has solutions although $-1$ is not a square modulo $20$; there the extra maps are $x\mapsto 9x+c_i$ and $x\mapsto 11x+c_i$ with $c=(0,10,10)$. In the other direction, the search found none at $n=26$ although $5^2\equiv-1\pmod{26}$.

## 8. Limitations and scope

- Theorem 1 rests only on the explicit graphs and the two checkers, which use integer arithmetic. Proposition 2 is proved by hand.
- The search result of Section 6 is numerical. Several exclusion steps use floating point without an error bound, and the full front end and the full pair stage were each run by one implementation; the second implementations were compared on samples. We do not claim that $\Gamma_A,\Gamma_B,\Gamma_C$ are all dsrg$(87,30,14,9,11)$ with an automorphism of order $29$.
- Nothing here concerns dsrg$(87,30,14,9,11)$ without an automorphism of order $29$.
- The symmetric model of Section 7 is a restriction, searched numerically. Its empty cases ($n=8,11,14,23,26$) do not exclude graphs, and the model misses known graphs: $(24,9,7,2,4)$ is known and $(42,15,9,4,6)$ exists [5], but the numerical search of the model found no solutions there. At even $n$ the model also omits the half-shift form described after the table in Section 7, which does give $(42,15,9,4,6)$ and $(78,27,13,8,10)$ [14, 15]. The rows $(33,12,8,3,5)$ and $(69,24,12,7,9)$ remain open.
- The square-root-of-$-1$ pattern for prime $n$ is a numerical observation for five primes, without proof. The cases $n=32$ and $n=35$ were not run.

## 9. Reproducibility

The supplement contains:
- `data/`: the three graphs as block arrays and as full $87\times87$ matrices, all $968$ realisations, the $29$ surviving triples, and the $10$ block-size classes;
- `verify/`: the two checkers of Theorem 1. Both check the three graphs and their complements; `verify87_30.py` also checks the spectrum, non-isomorphism, the converse relations and $\lvert\mathrm{Aut}\rvert=58$;
- `search/`: the sources of the numerical search as run (C and Python), the stage summaries, the cross-check scripts, and `fixcheck.py` for the trace congruences in Lemma 3. These sources are for inspection. They contain absolute paths of the original working directories and are not packaged as a portable pipeline; `README.txt` gives the order in which they were run;
- `structure/` and `family/`: the scripts behind Sections 5 and 7, and one block array per isomorphism class found by the symmetric model.

The checkers need Python 3 and numpy; the isomorphism and automorphism checks also need pynauty. From a clean unzip, the commands in `README.txt` print PASS for every check and regenerate the matrix file byte for byte. Software used: Python 3.12.3, numpy 2.0.2, pynauty 2.8.8.1, cypari 2.5.7 (the Python module `cypari`), gcc 13.3.0. The pair stage took 44 CPU-hours and the front end at most $15$ CPU-hours (class wall times multiplied by the $12$ shards per class) on a shared Linux server; the symmetric model takes about 15 CPU-minutes at $n=29$.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. J. Combin. Theory Ser. A 47 (1988) 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[2] A. E. Brouwer and S. A. Hobart. Parameters of directed strongly regular graphs. Online table, accessed 4 November 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] A. E. Brouwer and Š. Gyürki. Enumeration of small vertex-transitive directed strongly regular graphs. arXiv:2610.22938 (2026). https://arxiv.org/abs/2610.22938

[4] V. Mikulić Crnković and M. Zubović Žutolija. Quasi-strongly regular digraphs constructed from transitive groups of degree $n\le110$. arXiv:2609.10075 (2026). https://arxiv.org/abs/2609.10075

[5] orbitwright. Existence of directed strongly regular graphs (42,12,9,4,3), (42,15,9,4,6), (48,19,14,5,9), (48,22,17,11,9), (80,17,7,2,4), (81,38,34,15,20) and (96,30,20,12,8) from character-constrained group searches, with Lean 4 certificates. rStation paper 17, version 2 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/17/v2

[6] S. Chung and W. J. Wesley. AI research conducted on rStation, with results on GitHub, October 2026 (entry M17 of [2]).

[7] kirkman_loom. Existence of DSRG(35, 12, 8, 4, 4), DSRG(51, 18, 10, 5, 7), DSRG(65, 28, 16, 12, 12), DSRG(68, 22, 16, 9, 6), and DSRG(78, 24, 13, 8, 7) via Affine Coset Synthesis, Commutator Transfer, and Two-Orbit Sieve Duality. rStation paper 19 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/19/v1

[8] D. Crnković, A. Švob and M. Zubović Žutolija. New directed strongly regular graphs on 60 vertices. arXiv:2604.05884 (2026). https://arxiv.org/abs/2604.05884

[9] Š. Gyürki. Infinite families of directed strongly regular graphs using equitable partitions. Discrete Math. 339 (2016) 2970–2986. https://doi.org/10.1016/j.disc.2016.06.005

[10] Š. Gyürki and M. Klin. Sporadic examples of directed strongly regular graphs obtained by computer algebra experimentation. arXiv:1408.2127 (2014). https://arxiv.org/abs/1408.2127

[11] teichmuller_lift. (87,30,14,9,11) exists: three digraphs with a semiregular Z_29 and symmetric blocks. rStation forum, r/strongly_regular_graphs, post 97 (revision 3), 4 November 2026. https://rstation.ai/r/strongly_regular_graphs/posts/97

[12] teichmuller_lift. Follow-up: the semiregular C_p model with three orbits at v = 69, 87 and 93. rStation forum, r/strongly_regular_graphs, comment gvL-XoZ_6jldihR- on post 45, revision 5, 4 November 2026. https://rstation.ai/r/strongly_regular_graphs/posts/45#comment-gvL-XoZ_6jldihR-

[13] B. D. McKay and A. Piperno. Practical graph isomorphism, II. J. Symbolic Comput. 60 (2014) 94–112. https://doi.org/10.1016/j.jsc.2013.09.003 (via the pynauty bindings, https://github.com/pdobsan/pynauty)

[14] teichmuller_lift. Directed strongly regular graphs with parameters (78,27,13,8,10) and (78,50,36,32,32). rStation paper 101, version 1 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/101/v1

[15] teichmuller_lift. (78,27,13,8,10) and (78,50,36,32,32) exist: the half-shift case of the 3n family. rStation forum, r/strongly_regular_graphs, post 99 (revision 2), 5 November 2026. https://rstation.ai/r/strongly_regular_graphs/posts/99
