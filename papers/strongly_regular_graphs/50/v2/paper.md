# A triangle family of directed strongly regular graphs on Dih(Z_n^2), and existence of (84,31,27,10,12), (90,31,17,8,12), (90,34,20,14,12), (98,36,21,10,15) and (100,37,33,16,12)

## 1. Results

A directed strongly regular graph (dsrg) with parameters $(v,k,t,\lambda,\mu)$ [1] is a loopless digraph on $v$ vertices whose adjacency matrix $A$ satisfies $AJ=JA=kJ$ and
$$A^2=tI+\lambda A+\mu(J-I-A),\qquad 0<t<k .$$
The complement of a dsrg$(v,k,t,\lambda,\mu)$ is a dsrg$(v,\,v-k-1,\,v-2k+t-1,\,v-2k+\mu-2,\,v-2k+\lambda)$. In the table of Hobart and Brouwer [2] (fetched 2026-10-26), the five parameter sets in the title and their complements are marked "?".

**Theorem 1 (triangle family).** Let $n\ge 3$, $A=\mathbb Z_n^2$, and $G=\mathrm{Dih}(A)=A\rtimes\langle b\rangle$ with $b^2=1$ and $bub=-u$. Put
$$Y=\{(a,c)\in A:\ a,c\in\{1,\dots,n-1\},\ a+c\le n\},\qquad X=Y\setminus\{(a,c):a+c=n\}.$$
Then the Cayley digraph $\mathrm{Cay}(G,\,X\cup Yb)$ (arcs $g\to gs$) is a dsrg with parameters
$$\Big(2n^2,\ (n-1)^2,\ \tbinom n2,\ \tbinom{n-2}2,\ \tbinom{n-1}2\Big).$$

So $X$ is the set of lattice points strictly inside the triangle with vertices $(0,0),(n,0),(0,n)$, and $Y$ is $X$ together with the $n-1$ interior points of the hypotenuse. The members with $v\le 110$ are $(18,4,3,0,1)$, $(32,9,6,1,3)$, $(50,16,10,3,6)$, $(72,25,15,6,10)$ and $(98,36,21,10,15)$. The first four parameter sets are already marked as known in [2]. The case $n=7$ is new. At $n=6$ the triangle graph is not isomorphic to any of the three previously published $(72,25,15,6,10)$ graphs, or to their converses (Section 2).

**Corollary 2.** Directed strongly regular graphs with parameters $(98,36,21,10,15)$ and $(98,61,46,39,36)$ exist.

**Theorem 3.** Directed strongly regular graphs exist with parameters
$(84,31,27,10,12)$, $(90,31,17,8,12)$, $(90,34,20,14,12)$, $(100,37,33,16,12)$,
and with the complementary parameters $(84,52,48,32,32)$, $(90,58,44,38,36)$, $(90,55,41,32,36)$, $(100,62,58,36,42)$.

The graphs in Theorem 3 are unions of orbitals of transitive permutation groups $K$ of degree $v$ with $|K|=4v$. The point stabiliser has order 4 in each case (Table 1). Each one is fixed by two permutations and one out-neighbourhood, printed in Appendix A. Vertex-transitivity is certified directly by these generators.

**Secondary symmetry facts (computational).** These rest on nauty [9] and GAP [8]. They are not needed for Theorems 1 and 3. The supplement scripts `symmetry_check.py` and `group_facts.g` reproduce them, and their outputs are shipped as `symmetry_check.out` and `group_facts.out`.
- The 84- and 90-vertex graphs: nauty gives $|\mathrm{Aut}|=|K|$. Since $K\le\mathrm{Aut}$, this means $\mathrm{Aut}=K$. GAP finds no transitive subgroup of order $v$ among all conjugacy classes of subgroups of $K$. So these graphs are vertex-transitive but not Cayley graphs.
- The 100-vertex graph: $|\mathrm{Aut}|=800=2|K|$. Aut has five conjugacy classes of regular subgroups ($D_{10}\times D_{10}$, $C_{10}\times D_{10}$, and three of type $C_5^2\rtimes C_4$). So it is a Cayley graph.
- The triangle graphs for $3\le n\le10$: $|\mathrm{Aut}|=12n^2$. For $n=7$, $\mathrm{Aut}\cong\mathrm{SmallGroup}(588,35)$, and its regular subgroups have types $\mathrm{Dih}(\mathbb Z_7^2)$ and $C_7\times D_{14}$. So the 98-vertex graph is also a Cayley graph on $C_7\times D_{14}$.
- Converses: the $n=3$ triangle graph is isomorphic to its converse. The triangle graphs for $4\le n\le10$ and the four sporadic graphs are not isomorphic to their converses. We make no converse claim for $n>10$.

**Table 1.** The sporadic graphs of Theorem 3. Here $K$ is a SmallGroup in the GAP library, $H$ is the point stabiliser, the rank is the number of orbitals of $K$, and $|S|$ is the number of non-diagonal orbitals in the union.

| parameters | $K$ | $H$ | rank | $\lvert S\rvert$ | $\lvert\mathrm{Aut}\rvert$ | Cayley |
|---|---|---|---|---|---|---|
| (84,31,27,10,12) | SG(336,209) $=C_2\times\mathrm{PSL}(3,2)$ | $C_4$ | 24 | 10 | 336 | no |
| (90,31,17,8,12) | SG(360,121) $=A_5\times S_3$ | $C_2^2$ | 26 | 9 | 360 | no |
| (90,34,20,14,12) | SG(360,121), same action | $C_2^2$ | 26 | 10 | 360 | no |
| (100,37,33,16,12) | SG(400,125) $=C_5^2\rtimes((C_4\times C_2)\rtimes C_2)$ | $C_4$ | 27 | 10 | 800 | yes |

## 2. Related work

- **Origins.** Duval [1] introduced dsrgs and the basic feasibility conditions. Many constructions use coherent algebras [3] or Cayley graphs on semidirect products [4].
- **Dihedral and index-2 settings.** For dihedral groups $D_n$ (the case of a cyclic $A$), He, Zhang and Feng [6] and He and Zhang [7] constructed and partly characterised Cayley dsrgs of the form $\mathrm{Cay}(D_n,X\cup Yb)$. Huang, Lu and Park [5] treat a non-abelian group with an abelian subgroup $A$ of index 2. Their Lemma 6 is the general group-ring reduction that we specialise in Section 3. Their Theorem 1(i) gives the character dichotomy behind cases (a) and (b) there. They characterise the cases $|X|=|Y|$, $Y=A\setminus X$ and $Y=X\cup\{e\}$, and the families $(2n,n-\ell,\dots)$ and $(2n,n,\dots)$.
- **Where Theorem 1 sits.** In Theorem 1, $|A|=n^2$, $|Y|=|X|+n-1$ and $k=(n-1)^2$. None of the special cases in [5,6,7] gives these connection sets or these parameters.
- **Other families on $2n^2$ vertices.** Gyürki and Klin [11] construct, from quasigroups of order $n$, dsrgs with parameters $(2n^2,3n-2,2n-1,n-1,3)$ and $(2n^2,4n-2,2n+2,n+2,6)$. Their eigenvalues are $n-2$ and $-2$. Their complements therefore have the same eigenvalues $1,1-n$ as Theorem 1, but degrees $2n^2-3n+1$ and $2n^2-4n+1$ rather than $(n-1)^2$. The layer constructions of rStation paper 4 [12] use products of nets and include a $(72,25,15,6,10)$ graph, through a different construction.
- **Earlier small members.** The parameter sets for $n=4,5,6$ are listed as known in [2]: $(32,9,6,1,3)$ in M9 and M10, $(50,16,10,3,6)$ in M10 (Gyürki and Klin, unions of classes in association schemes), and $(72,25,15,6,10)$ in M17. For $(72,25,15,6,10)$ there are two earlier sources. Paper 4 [12] gives one graph; M17 collects it from there. Mikulić Crnković and Zubović Žutolija [10, Section 4.1.1] give two non-isomorphic graphs, as unions of suborbits of $\mathrm{GO}^+(4,3)$ of degree 72. We compared these three published matrices with the $n=6$ triangle graph using nauty (`symmetry_check.py`). Their automorphism groups have orders $2$ (paper 4) and $2304,2304$ ([10]). The triangle graph has order $432$. None of the three graphs or their converses is isomorphic to the triangle graph. So the triangle graph is a fourth $(72,25,15,6,10)$ graph. We did not compare the $n=4,5$ members.
- **Literature search.** We searched arXiv abstracts for dsrgs on dihedral, generalised dihedral and semidirect-product groups. We found the triangle sets nowhere, and no construction of $(98,36,21,10,15)$.
- **Discovery.** The 98-vertex graph was first found as a union of orbitals of $\mathrm{AGO}^+(2,7)=\mathrm{SG}(588,35)$ acting on 98 cosets of $S_3$, in a sweep over coset actions of small groups (Section 4). Reading off its connection sets in suitable coordinates led to Theorem 1. The sweep graph is shipped as `sweep98_rows.txt`. Using nauty [9], `symmetry_check.py` shows that the graph of Theorem 1 with $n=7$ is isomorphic to the converse of the sweep graph, but not to the sweep graph itself. Both have automorphism groups of order 588.

## 3. Proof of Theorem 1

The reduction (I), (II) below is the case $f(u)=-u$, $\alpha=e$ of [5, Lemma 6]. We include its two-line derivation to keep the proof self-contained. Write $\mathbb Z[A]$ for the group ring, $T^{(-1)}=\sum_{u\in T}(-u)$, and identify a subset of $A$ with the sum of its elements. In $G$ we have $b\,u=(-u)\,b$. So for $S=X+Yb$:
$$S^2=X^2+XYb+YbX+YbYb=\big(X^2+YY^{(-1)}\big)+\big(XY+YX^{(-1)}\big)b .$$
Write $G=A+Ab$. The dsrg identity $S^2=te+\lambda S+\mu(G-e-S)=(t-\mu)e+(\lambda-\mu)S+\mu G$ splits into two identities in $\mathbb Z[A]$. Here $t-\mu=n-1$, $\lambda-\mu=-(n-2)$ and $\mu=\binom{n-1}2$:
$$\text{(I)}\quad X^2+YY^{(-1)}=(n-1)e-(n-2)X+\mu A,\qquad \text{(II)}\quad XY+YX^{(-1)}=-(n-2)Y+\mu A .$$
Moreover $|X|=\binom{n-1}2=\mu$, $|Y|=\binom n2=t$, $|X|+|Y|=(n-1)^2=k$, and $e\notin S$. Also $S^{(-1)}\ne S$: the set $-X$ consists of the points $(n-a,n-c)$ with $(n-a)+(n-c)>n$, so $X\cap(-X)=\emptyset$ and $X\neq\emptyset$ for $n\ge3$. Since $0<t<k$ exactly when $n\ge3$, it remains to prove (I) and (II). Both sides are elements of $\mathbb Z[A]$, so it is enough to compare their values under every character $\psi$ of $A$.

**Trivial character.** Here $\psi(A)=n^2$. (II) reads $2\mu t=-(n-2)t+\mu n^2$, that is $t(2\mu+n-2)=\mu n^2$. This holds because $2\mu+n-2=n(n-2)$ and $t\,n(n-2)=\tfrac{n^2(n-1)(n-2)}2=\mu n^2$. (I) reads $\mu^2+t^2=(n-1)-(n-2)\mu+\mu n^2$. With $t=\mu+n-1$ this becomes $2\mu^2+2\mu(n-1)+(n-1)^2=(n-1)+\mu(n^2-n+2)$. Substituting $2\mu=(n-1)(n-2)$ and dividing by $n-1$ turns both sides into $\tfrac{(n-1)(n-2)^2}2+(n-1)(n-2)+(n-1)$, which are equal.

**Non-trivial characters.** Let $\zeta=e^{2\pi i/n}$ and $\psi(a,c)=u^a w^c$ with $u=\zeta^j$, $w=\zeta^l$, $(j,l)\ne(0,0)$. Put $x=\psi(X)$, $y=\psi(Y)$. Since $\psi(T^{(-1)})=\overline{\psi(T)}$, (I) and (II) become
$$\text{(I}'\text{)}\ x^2+|y|^2=(n-1)-(n-2)x,\qquad \text{(II}'\text{)}\ y\,(x+\bar x+n-2)=0 .$$
So it is enough to show that one of the following holds for every non-trivial $\psi$:
- (a) $y=0$ and $x\in\{1,-(n-1)\}$. These are the roots of $x^2+(n-2)x-(n-1)=(x-1)(x+n-1)$.
- (b) $\operatorname{Re}x=-\tfrac{n-2}2$ and $|y|=|x-1|$.

Case (b) suffices: put $x=-\tfrac{n-2}2+i\beta$. Then $x^2+(n-2)x-(n-1)=-\tfrac{(n-2)^2}4-\beta^2-(n-1)=-|x-1|^2$, so (I$'$) holds exactly when $|y|^2=|x-1|^2$.

We use two elementary facts. For $w^n=1\ne w$:
$$\sum_{c=1}^{n-1}w^c=-1,\qquad \sum_{c=1}^{n-1}c\,w^c=\frac{n}{w-1}. \tag{$*$}$$
The second follows from $(w-1)\sum_{c=0}^{n-1}c\,w^c=(n-1)w^n-\sum_{c=1}^{n-1}w^c=n$. Also, $|w|=1$ gives $\operatorname{Re}\frac1{w-1}=-\frac12$ and $\operatorname{Re}\frac w{w-1}=\frac12$. Let $L=\{(a,n-a):1\le a\le n-1\}$, so $X=Y-L$ and $\psi(L)=\sum_{a=1}^{n-1}(u w^{-1})^a$.

- **$u=w\ne1$ (that is, $j=l\ne0$).** Then $\psi(L)=n-1$. The number of points of $Y$ with $a+c=s$ is $s-1$ for $2\le s\le n$. By $(*)$, $y=\sum_{s=2}^n(s-1)w^s=w\sum_{c=1}^{n-1}c\,w^c=\frac{nw}{w-1}$. Hence $x=y-(n-1)=1+\frac n{w-1}$, so $\operatorname{Re}x=1-\frac n2=-\frac{n-2}2$ and $|x-1|=\frac n{|w-1|}=|y|$. This is case (b).
- **$u=1\ne w$ (and, by the symmetry $(a,c)\mapsto(c,a)$, $w=1\ne u$).** Then $\psi(L)=\sum_{a=1}^{n-1}w^{-a}=-1$. The fibre of $Y$ over $c$ has $n-c$ points, so by $(*)$ $y=\sum_{c=1}^{n-1}(n-c)w^c=-n-\frac n{w-1}=-\frac{nw}{w-1}$. Hence $x=y+1$ with $\operatorname{Re}x=1-\frac n2$ and $|x-1|=|y|$. This is case (b).
- **$u\ne w$ and $u,w\ne1$.** Then $\psi(L)=-1$. For fixed $a$, $\sum_{c=1}^{n-a}w^c=\frac{w^{n-a+1}-w}{w-1}=\frac{w\,(w^{-a}-1)}{w-1}$. Hence
$$y=\frac w{w-1}\sum_{a=1}^{n-1}\big((u/w)^a-u^a\big)=\frac w{w-1}\,(-1+1)=0,$$
because $u/w\ne1$ and $u\ne1$ are $n$-th roots of unity. So $x=y-\psi(L)=1$. This is case (a).

The three cases cover every $(j,l)\ne(0,0)$, which proves (I) and (II), and with them Theorem 1. $\square$

*Remarks.* (i) Replacing $Y$ by a translate $z+Y$ ($z\in A$) multiplies both sides of (II) by $z$ and leaves (I) unchanged, so it again gives a dsrg. For $n$ odd it is conjugate to the original: conjugation by $w\in A$ maps $Yb$ to $(Y-2w)b$. Replacing $(X,Y)$ by $(X,-Y)$ also preserves (I) and (II), since $\psi(-Y)=\overline{\psi(Y)}$ has the same modulus and vanishes on the same characters. (ii) The non-principal eigenvalues are the roots $r=1$, $s=-(n-1)$ of $z^2-(\lambda-\mu)z-(t-\mu)$.

## 4. The sporadic graphs (Theorem 3) and how they were found

**Search.** For every group $K$ of order $v\cdot s$ in the SmallGroups library ($s\in\{2,3,4,6\}$, orders with fewer than 700 groups) and every core-free subgroup $H$ of order $s$, we formed the orbital configuration of $K$ on $K/H$, keeping those of rank at most 40. We skipped commutative configurations. A dsrg adjacency matrix lying in a commutative coherent algebra is normal with real spectrum, hence symmetric. In the remaining configurations, $A=\sum_{i\in S}A_i$ is a dsrg if and only if a linear identity holds in the basis of orbital matrices. That identity has coefficients $p_{ij}^k$. We searched for $S$ by depth-first search with degree and $p_{ij}^k$ pruning. Configurations where the node limit was hit were passed to an exact CP-SAT model of the same identity. As controls, the search rediscovered known graphs, including $(57,22,14,9,8)$, $(58,26,18,11,12)$, $(58,27,15,12,13)$, $(81,38,34,15,20)$ and $(102,47,34,21,22)$. In the part of the sweep completed so far, the rows in Theorem 3 and Corollary 2 are the only hits on rows marked "?" in [2] that no earlier source covered.

**Description.** In each case some normal subgroup $N$ of index 2 in $K$ is already transitive, with point stabiliser $H\cap N$ of order 2:
- $N=\mathrm{PSL}(3,2)$ for $v=84$, so the vertices are the 84 cosets of an involution in $\mathrm{PSL}(3,2)$, and $H\cong C_4$ is a diagonal subgroup of $C_2\times\mathrm{PSL}(3,2)$;
- $N=A_5\times C_3\cong\mathrm{GL}(2,4)$ for $v=90$, with vertices the cosets of an involution of $A_5$;
- $N=C_2\times D_{10}\times D_{10}$ for $v=100$.

We have no closed description comparable to Theorem 1 for these graphs.

**Verification.** Each graph was checked by two independent programs, and the same programs checked every complement:
1. The search code tests $A^2=tI+\lambda A+\mu(J-I-A)$ with integer matrices.
2. A separate script (supplement, `verify_all.py`, plain Python with no libraries) rebuilds the arc set as the $K$-orbit of $\{(1,j):j\in N(1)\}$ from the printed generators. It then counts, for every ordered pair of vertices, the directed 2-walks between them.

For Theorem 1 the same script builds $\mathrm{Cay}(\mathrm{Dih}(\mathbb Z_n^2),X\cup Yb)$ directly. It confirms $n=3,\dots,12$ and their complements, and a separate numpy check confirms $n\le 16$. A perturbed connection set is rejected in both cases (negative control). These checks, together with the proof in Section 3, are the complete evidence for the existence claims.

The symmetry statements in Section 1 are separate computations. `symmetry_check.py` (numpy and pynauty) computes $|\mathrm{Aut}|$ and converse isomorphism. It also compares the $n=7$ graph with the sweep graph and, if given the external files, the $n=6$ graph with the published $(72,25,15,6,10)$ matrices. It writes the nauty automorphism generators to `aut_gens.g`. `group_facts.g` (GAP 4.13.1) then checks that $K\le\mathrm{Aut}$, identifies the groups, and lists the regular subgroups. The outputs are in `symmetry_check.out` and `group_facts.out`.

## 5. Questions

1. Theorem 1 uses only the triangle and its hypotenuse. Do other lattice polygons in $\mathbb Z_n^2$, or simplices in $\mathbb Z_n^d$ with $\mathrm{Dih}(\mathbb Z_n^d)$, give further families?
2. At $n=6$ the triangle graph differs from all three previously published graphs (Section 2). Are the known graphs for $n=4,5$ (M9, M10 in [2]) isomorphic to the triangle graphs?
3. Do the 84- and 90-vertex graphs belong to families on $C_2\times\mathrm{PSL}(3,q)$ or $A_5\times S_3$-type groups?

## References

[1] A. M. Duval, A directed graph version of strongly regular graphs, J. Combin. Theory Ser. A 47 (1988) 71–100.
[2] S. A. Hobart, A. E. Brouwer, Directed strongly regular graphs, online table, https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html (fetched 2026-10-26).
[3] M. Klin, A. Munemasa, M. Muzychuk, P.-H. Zieschang, Directed strongly regular graphs obtained from coherent algebras, Linear Algebra Appl. 377 (2004) 83–109.
[4] A. M. Duval, D. Iourinski, Semidirect product constructions of directed strongly regular graphs, J. Combin. Theory Ser. A 104 (2003) 157–167.
[5] X. Huang, L. Lu, J. Park, On directed strongly regular Cayley graphs over non-abelian groups with an abelian subgroup of index 2, arXiv:2209.10352 (2022).
[6] Y. He, B. Zhang, R. Feng, Directed strongly regular Cayley graphs on dihedral groups, arXiv:1801.04748 (2018).
[7] Y. He, B. Zhang, The application of representation theory in directed strongly regular graphs, arXiv:1707.07789 (2017).
[8] The GAP Group, GAP – Groups, Algorithms, and Programming, Version 4.13.1.
[9] B. D. McKay, A. Piperno, Practical graph isomorphism II, J. Symbolic Comput. 60 (2014) 94–112 (nauty; used through pynauty).
[10] V. Mikulić Crnković, M. Zubović Žutolija, Quasi-strongly regular digraphs constructed from transitive groups of degree $n\le110$, arXiv:2609.10075v1 (2026). Matrices: https://www.math.uniri.hr/~matea.zubovic/dsrg/new_DSRGs.html
[11] Š. Gyürki, M. Klin, Directed strongly regular graphs from groups, loops and quasigroups, arXiv:2608.16202 (2026).
[12] rStation paper 4, Existence of DSRGs (45,18,8,6,8) and 21 further complement classes via nets and equitable partitions, v1 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/4/v1 . Its $(72,25,15,6,10)$ matrix is also in S. Chung's collection, https://github.com/dualverse-ai/strong_regular_graph/tree/main/finite_constructions (source of M17 in [2]).

## Appendix A. Data for Theorem 3

Vertices are $1,\dots,v$. $K=\langle g_1,g_2\rangle$, where $g_i$ is given as the image list $(g_i(1),\dots,g_i(v))$. The arc set is the $K$-orbit of $\{(1,j):j\in N(1)\}$. The same data are in the supplement as `sporadic.json`.

**(84, 31, 27, 10, 12)** (from SG(336,209))

- $g_1$ = `64 63 66 65 68 67 62 61 69 70 71 72 30 29 28 27 26 25 32 31 36 35 34 33 78 77 76 75 74 73 80 79 84 83 82 81 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 56 55 50 49 52 51 54 53 57 58 59 60 37 38 39 40 41 42 43 44 45 46 47 48`
- $g_2$ = `12 11 5 6 10 9 1 2 3 4 7 8 73 74 84 83 77 78 82 81 76 75 80 79 14 13 23 24 18 17 21 22 15 16 19 20 49 50 58 57 53 54 60 59 56 55 52 51 71 72 62 61 69 70 66 65 68 67 64 63 48 47 44 43 46 45 40 39 42 41 38 37 25 26 31 32 29 30 27 28 35 36 33 34`
- $N(1)$ = `2 3 5 6 7 10 12 13 14 18 21 25 29 30 31 41 46 47 48 50 57 59 60 61 67 69 72 74 75 80 81`

**(90, 31, 17, 8, 12)** (from SG(360,121))

- $g_1$ = `2 18 27 13 24 4 11 12 10 8 21 20 14 29 7 3 30 6 5 17 16 1 22 15 26 9 19 25 23 28 64 65 66 76 72 77 80 90 63 89 67 74 82 81 83 73 75 88 87 79 85 84 69 61 62 71 86 70 68 78 34 54 43 51 50 38 42 40 41 32 57 48 52 46 31 36 49 39 37 45 56 35 58 53 59 33 55 60 47 44`
- $g_2$ = `75 70 86 61 82 76 79 66 78 68 69 67 63 90 80 74 89 72 77 65 64 73 84 62 87 81 71 83 85 88 16 17 12 4 6 5 7 29 14 30 20 3 24 9 25 1 2 28 26 11 23 22 21 13 15 19 27 18 8 10 34 43 54 53 41 59 33 60 50 47 57 58 52 31 46 35 56 44 37 55 49 36 48 51 38 42 45 40 32 39`
- $N(1)$ = `2 3 6 8 10 13 16 22 25 28 29 32 33 37 38 44 45 46 54 57 58 61 62 64 69 73 74 77 78 82 89`

**(90, 34, 20, 14, 12)** (from SG(360,121))

- $g_1$ = `2 18 27 13 24 4 11 12 10 8 21 20 14 29 7 3 30 6 5 17 16 1 22 15 26 9 19 25 23 28 64 65 66 76 72 77 80 90 63 89 67 74 82 81 83 73 75 88 87 79 85 84 69 61 62 71 86 70 68 78 34 54 43 51 50 38 42 40 41 32 57 48 52 46 31 36 49 39 37 45 56 35 58 53 59 33 55 60 47 44`
- $g_2$ = `75 70 86 61 82 76 79 66 78 68 69 67 63 90 80 74 89 72 77 65 64 73 84 62 87 81 71 83 85 88 16 17 12 4 6 5 7 29 14 30 20 3 24 9 25 1 2 28 26 11 23 22 21 13 15 19 27 18 8 10 34 43 54 53 41 59 33 60 50 47 57 58 52 31 46 35 56 44 37 55 49 36 48 51 38 42 45 40 32 39`
- $N(1)$ = `4 8 12 14 15 18 23 24 28 30 32 33 37 38 44 45 46 50 54 56 57 58 61 62 64 66 69 73 74 77 78 82 83 89`

**(100, 37, 33, 16, 12)** (from SG(400,125))

- $g_1$ = `2 3 6 29 32 1 33 36 42 45 7 81 8 22 25 9 84 10 14 89 15 46 49 47 50 4 74 5 51 54 52 55 60 63 61 64 16 91 17 92 18 37 40 38 41 19 93 20 94 21 26 96 27 97 28 67 65 68 66 11 86 12 87 13 71 69 72 70 78 76 79 77 30 98 31 58 56 59 57 34 99 35 43 100 44 82 80 23 95 24 85 83 90 88 48 75 73 53 62 39`
- $g_2$ = `23 43 34 5 58 30 15 78 10 71 38 25 11 8 67 61 45 26 52 36 19 12 74 1 39 47 32 16 27 89 6 62 20 84 3 53 56 40 22 13 75 17 81 2 48 76 63 42 28 90 69 54 33 21 85 86 4 57 41 65 49 29 18 82 96 14 77 64 93 9 70 55 37 24 87 91 7 66 50 60 44 97 51 35 94 73 59 46 31 92 88 79 83 72 95 80 68 100 99 98`
- $N(1)$ = `3 7 8 12 17 23 24 26 27 28 34 35 39 42 45 46 48 50 56 57 58 59 66 67 74 76 77 78 79 81 86 87 93 94 95 98 100`

