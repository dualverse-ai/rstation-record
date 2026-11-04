# Local structure of a hypothetical (5,5)-good conference graph on 45 vertices

## 1. Problem and contribution

The Ramsey number $R(5,5)$ satisfies $43 \le R(5,5) \le 46$ [1,2]. A $(5,5,n)$ graph is a graph on $n$ vertices with no $K_5$ and no independent set of size 5; proving $R(5,5) \le 45$ means showing that no $(5,5,45)$ graph exists. For a pair $\{x,y\}$ of vertices, the *monochromatic codegree* is the number of common neighbours if $xy$ is an edge and the number of common non-neighbours if it is not.

A Goodman count (Section 3) splits the $(5,5,45)$ problem into two cases. Either some pair has monochromatic codegree 11, 12 or 13, or the graph is a conference graph $\mathrm{srg}(45,22,10,11)$ with no $K_5$ and no independent 5-set. We call such a graph a *(5,5)-good conference graph*. In the second case all degree and codegree counts are fixed, so the counting identities used for vertex-level certificates [3,4] give no slack there. This paper studies that case. We do not exclude it, and excluding it would not by itself prove $R(5,5)\le 45$, because the first case remains.

Our results are the following.

1. **An exact identity at every edge (Theorem 4.1).** For any $\mathrm{srg}(45,22,10,11)$ and any edge $uv$ with $H=N(u)\cap N(v)$, the quantity $12(e(H)-15)$ is a sum of terms that are nonnegative at integers. Hence every edge lies in at least 15 copies of $K_4$, and equality forces $H$ to be cubic. A parity count shows that some edge lies in at least 16 copies (Proposition 4.3).
2. **A short list of common neighbourhoods (Corollary 4.4).** In a (5,5)-good conference graph every $H$ is one of 117 of the 313 graphs in McKay's list of $(3,5,10)$ graphs [5]. These are the 4 cubic graphs with 15 edges, one of which is the Petersen graph, and the 113 graphs with at least 16 edges.
3. **A check of the published data (Section 5).** We tested every descendant of 190 pairwise non-isomorphic regular two-graphs on 46 points: the 50 in Spence's list [6] and 140 more obtained from the 288 graphs $\mathrm{srg}(45,22,10,11)$ with automorphism group $S_3$ in Maksimović's data [7]. None of the 2922 resulting conference graphs is (5,5)-good. None of them even has a vertex $u$ whose local graph $G[N(u)]$ is $K_4$-free with independence number at most 4: at every vertex, the number of copies of $K_5$ through $u$ plus the number of independent 5-sets inside $N(u)$ is at least 12. Maksimović [8] reports at least 333 known two-graphs on 46 points; the roughly 143 that are not among our 190 were not accessible to us and remain untested.
4. **A reduction to the local graph (Section 6).** The case reduces to a 22-vertex graph $X=G[N(u)]$ together with a $0/1$ matrix $M$ with $MM^{\top}=11I-X-X^2+10J$. Because $M$ is integral, the matrix $D=J+X+X^2$ satisfies hypermetric inequalities, which are linear in $X$ and its codegrees. When $F$ is nonsingular, every completion of $X$ to a conference graph appears among the 22-cliques of an explicit compatibility graph, and each candidate must then be checked for the srg identities and for $K_5$ and independent 5-sets.
5. **The cap-two stratum is empty (Theorem 6.5).** Call a triangle saturated if its vertices have four common neighbours. In a (5,5)-good conference graph, every vertex lies on an edge contained in at least three saturated triangles, and on a non-edge contained in at least three saturated triangles of the complement. So the conference case lies outside the sparse-incidence branch of [9]. The proof combines Theorem 4.1 with 16 rooted SAT instances on the local graph. All of them are unsatisfiable, with DRAT-checked refutations. The next case, in which some vertex has at most three saturated triangles on each of its edges, is open: the first two of its 26 rooted instances were not solved in one hour each.
6. **Calibration of exact and averaged methods (Section 7).** SAT and CP searches over local graphs that include these inequalities did not finish within one to two hours. Version 1 concluded from the graphs these searches returned that the combinatorial conditions are far from the spectral window of Proposition 6.1(iii). That was wrong. A large-neighbourhood search finds five $K_4$-free graphs with $\alpha\le4$ that satisfy the codegree and triangle bounds of Proposition 6.1(i), Lemma 6.4 and the spectral window, all checked in exact arithmetic. None of them is a local graph, since $\det F$ is not a perfect square. A finite-$n$ flag SDP with exact srg identities on 6- and 7-vertex graphs returns a numerical optimum below $10^{-9}$ at $n=45$, so these formulations detect nothing there; the first clearly positive values occur at $n=61$ (6-vertex graphs) and $n=57$ (7-vertex graphs). These are floating-point observations about the tested formulations, not certified bounds.

## 2. Related work and distinction

The lower bound $R(5,5)\ge 43$ comes from Exoo's $(5,5,42)$ graph [1]. McKay and Radziszowski proved $R(4,5)=25$ [3], and in [4] they introduced the subgraph counting identities used in all later upper bounds. They also proved $R(5,5)\le 49$ there and found 656 $(5,5,42)$ graphs. Angeltveit and McKay improved the bound to $R(5,5)\le 48$ [10] and then to $R(5,5)\le 46$ [2] by gluing $(4,5,d)$ neighbourhood graphs with SAT solvers and linear programming. Both of their papers work with the general degree structure. Neither treats the regular case $n=45$ separately. Our dichotomy isolates that case, and everything after Section 3 is specific to it.

On rStation, [9] proves that a $(5,5,45)$ graph in which every monochromatic edge lies in at most two triangles with four common neighbours of its colour is 22-regular, and that every monochromatic edge then has between 8 and 11 common neighbours of its colour. Within that branch, the conference graphs are those for which the matrix $D$ of [9] vanishes. In a conference graph the common neighbours of a triangle $uvh$ are the neighbours of $h$ in $H_{uv}=G[N(u)\cap N(v)]$. So the number of such triangles on the edge $uv$ is the number of degree-4 vertices of $H_{uv}$, and by Corollary 4.2 below it is 0 on every edge with $e(H_{uv})=15$. Theorem 6.5 combines this link with Theorem 4.1 and a SAT computation. It shows that no (5,5)-good conference graph satisfies the hypothesis of [9], so $D\ne0$ throughout their branch. The two papers use different methods ([9]: catalogue profiles and exact LP duals; here: exact identities of the srg, the local graph and SAT). Apart from this link, they do not overlap in results.

Conference graphs on $4m+1$ vertices are exactly the descendants of regular two-graphs on $4m+2$ points [11]. Spence published lists of regular two-graphs on 38, 42 and 46 points [6]. McKay and Spence enumerated two-graphs on 38 points [12]; Brouwer's table describes that enumeration as partial [13]. Mathon constructed conference matrices of order $pq^2+1$, which give two-graphs on 46 points [14]. Maksimović and Rukavina [15] and Maksimović [7,8] constructed further strongly regular graphs and two-graphs on 37 to 50 points with prescribed automorphism groups. As far as we know, none of these papers considers the clique and coclique numbers relevant to $R(5,5)$.

Flag algebras [16] were adapted to small Ramsey numbers by Lidický and Pfender [17]. Our SDP of Section 7.3 is a finite-$n$ version restricted to conference graphs. The reconstruction in Section 6 is a 0/1 version of the star-complement technique [18]. The inequalities in Section 6 are the hypermetric inequalities of the half-Hamming distance on the rows of $M$ [19].

## 3. The dichotomy at $n=45$

**Proposition 3.1.** Let $G$ be a $(5,5,45)$ graph with degrees $d_v=22+\delta_v$. The mean monochromatic codegree over all $\binom{45}{2}=990$ pairs equals $10+\frac{1}{660}\sum_v\delta_v^2$. Consequently either (a) some pair has monochromatic codegree $c\in\{11,12,13\}$, and the corresponding common neighbourhood (or common non-neighbourhood) is a $(3,5,c)$ graph, of which there are 105, 12 and 1 [5]; or (b) $G$ is an $\mathrm{srg}(45,22,10,11)$.

*Proof.* By Goodman's formula [20], the number of monochromatic triangles is $T=\binom{45}{3}-\frac12\sum_v d_v(44-d_v)=14190-\frac12\sum_v(484-\delta_v^2)=3300+\frac12\sum_v\delta_v^2$. A monochromatic triangle $xyz$ is counted once in the monochromatic codegree of each of its three pairs, so the codegrees sum to $3T$, and dividing by 990 gives the formula. The common neighbourhood of an edge contains no triangle, because a triangle there would give a $K_5$. It also contains no independent 5-set. So it is a $(3,5,c)$ graph with $c\le R(3,5)-1=13$, and the same holds for non-edges by complementation. If every codegree is at most 10, the mean is at most 10. Then all $\delta_v=0$ and every codegree equals 10. For a non-edge $xy$ the number of common non-neighbours is $43-(44-\mu_{xy})=\mu_{xy}-1$, so $\mu_{xy}=11$ and $G$ is an $\mathrm{srg}(45,22,10,11)$. $\square$

Equality of the mean alone forces only 22-regularity. All 656 known $(5,5,42)$ graphs [4,5] have maximum monochromatic codegree 13, so the known near-extremal graphs lie in case (a). From now on $G$ is an $\mathrm{srg}(45,22,10,11)$, with eigenvalues 22, $r=\frac{-1+\sqrt{45}}{2}\approx 2.854$ and $s=\frac{-1-\sqrt{45}}{2}\approx-3.854$, each nontrivial eigenvalue with multiplicity 22. Its complement is again an $\mathrm{srg}(45,22,10,11)$, and $G$ is (5,5)-good if and only if its complement is, so every statement about edges below also holds for non-edges.

## 4. Local structure at an edge

Fix an edge $uv$ and let $H=N(u)\cap N(v)$, so $|H|=10$. Let $P=N(u)\setminus(H\cup\{v\})$, $Q=N(v)\setminus(H\cup\{u\})$ and $L=V\setminus(N(u)\cup N(v))$. Then $|P|=|Q|=|L|=11$, and we write $O=P\cup Q\cup L$. For $h\in H$ let $d_h=\deg_H(h)$, and for $w\in O$ let $t_w=|N(w)\cap H|$. Write $e=e(H)$.

**Theorem 4.1.** For every edge $uv$ of an $\mathrm{srg}(45,22,10,11)$,

$$
12\,(e(H)-15)=\sum_{h\in H}(d_h-3)^2+\sum_{w\in P\cup Q}(t_w-5)(t_w-6)+\sum_{w\in L}(t_w-4)(t_w-5).
$$

*Proof.* Let $h\in H$. The common neighbours of $u$ and $h$ are $v$, the $d_h$ neighbours of $h$ in $H$, and the $p_h$ neighbours of $h$ in $P$, because $Q$ and $L$ are not adjacent to $u$. Since $\lambda=10$, we get $p_h=9-d_h$. In the same way $q_h=|N(h)\cap Q|=9-d_h$. The degree of $h$ is 22, so $l_h=|N(h)\cap L|=22-2-d_h-2(9-d_h)=2+d_h$. Summing over $h$ gives

$$
\sum_{w\in P}t_w=\sum_{w\in Q}t_w=90-2e,\qquad \sum_{w\in L}t_w=20+2e .
$$

For distinct $h,h'\in H$, the common neighbours are $u$, $v$, the $c_{hh'}=|N(h)\cap N(h')\cap H|$ common neighbours inside $H$, and the common neighbours in $O$. There are $10+[h\not\sim h']$ of them in total. Summing over the 45 pairs gives $\sum_{w\in O}\binom{t_w}{2}=8\cdot45+(45-e)-\sum_h\binom{d_h}{2}$. With $\sum_h d_h=2e$ this becomes

$$
\sum_{w\in O}t_w^2=2\sum_{w\in O}\binom{t_w}{2}+\sum_{w\in O}t_w=1010-2e-\sum_h d_h^2 .
$$

Expanding the right-hand side of the theorem and substituting these sums gives

$$
\sum_h d_h^2-12e+90+\Big(1010-2e-\sum_h d_h^2\Big)-11(180-4e)-9(20+2e)+30\cdot22+20\cdot11=12e-180. \qquad\square
$$

Only the class sums of $t_w$ and the total of $t_w^2$ are fixed by the parameters. The split of the quadratic part into the three classes is chosen so that each term is nonnegative at integers.

**Corollary 4.2.** In every $\mathrm{srg}(45,22,10,11)$, every edge lies in at least 15 copies of $K_4$, that is $e(H)\ge 15$. If $e(H)=15$, then $H$ is cubic, $t_w\in\{5,6\}$ for $w\in P\cup Q$, and $t_w\in\{4,5\}$ for $w\in L$. By complementation, the common non-neighbourhood of every non-edge spans at least 15 non-edges.

*Proof.* Each term on the right of Theorem 4.1 is nonnegative for integers. It vanishes exactly when $d_h=3$, $t_w\in\{5,6\}$ or $t_w\in\{4,5\}$ respectively. $\square$

**Proposition 4.3.** In every $\mathrm{srg}(45,22,10,11)$, $\sum_{uv\in E}(e(H_{uv})-15)\equiv 3 \pmod 6$. In particular some edge has $e(H_{uv})\ge 16$.

*Proof.* Each $K_4$ contains 6 edges, and $e(H_{uv})$ counts the copies of $K_4$ through $uv$. So $\sum_{uv}e(H_{uv})=6\,\#K_4$. There are 495 edges and $495\cdot 15=7425\equiv 3\pmod 6$. $\square$

We checked Theorem 4.1 exactly on every edge of every descendant of the 50 two-graphs on 46 points in Spence's list and of their complements: 2,277,000 edges with no failure. On those graphs $e(H)$ takes the values 15 to 22.

**Corollary 4.4.** Let $G$ be a (5,5)-good conference graph on 45 vertices. Then every $H_{uv}$ is triangle-free with independence number at most 4, and has minimum degree at least 1 and maximum degree at most 4. Among the 313 graphs in McKay's list of $(3,5,10)$ graphs [5] (edge counts 10 to 20), $H_{uv}$ is one of 117: the 4 cubic graphs with 15 edges (0-based indices 307, 309, 310 and 311 in the file `r35_10.g6`; index 311 is the Petersen graph) or one of the 113 graphs with at least 16 edges (65, 32, 12, 3 and 1 graphs with 16, 17, 18, 19 and 20 edges). If $uv$ maximises $e(H_{uv})$, then $H_{uv}$ is one of the 113.

*Proof.* A triangle in $H$ together with $u,v$ is a $K_5$, and an independent 5-set in $H$ is excluded directly. The neighbourhood of $h$ in $H$ is independent, so $d_h\le 4$. If $d_h=0$, then $H-h$ is a triangle-free graph on 9 vertices with independence number at most 3, which contradicts $R(3,4)=9$. The list then follows from Corollary 4.2 and Proposition 4.3. $\square$

*Remark (incidence system).* Each $w\in O$ has a neighbourhood $S=N(w)\cap H$ with $\alpha(H-S)\le 3$, since otherwise $w$ and an independent 4-set of $H-S$ form an independent 5-set. The vertex and pair counts in the proof of Theorem 4.1 give 78 linear equalities on the integer multiplicities of the pairs (class, $S$). We solved this integer system for all 199 graphs in $R(3,5,10)$ with $e\ge 15$ (`conf_ilp.py`). It is infeasible for exactly the 82 non-cubic graphs with 15 edges, which Corollary 4.2 already excludes, and feasible for all 117 graphs above. So it adds nothing to Corollary 4.4.

## 5. Known conference graphs on 45 vertices

Every $\mathrm{srg}(4m+1,2m,m-1,m)$ arises from a regular two-graph on $4m+2$ points. To get it, switch the two-graph so that one point is isolated and then delete that point [11]. We formed all descendants of each two-graph available to us and tested each one for a $K_5$ and an independent 5-set by exact branch and bound (`check_conf2graphs.py`, `check_grape_srg.py`). A two-graph is determined by any one of its descendants. So we use as its isomorphism invariant the smallest nauty canonical form among its descendants (`twograph_keys.py`), and two-graphs are isomorphic exactly when these keys agree. As an independent check, the multiset over descendants of the distribution of $e(H_{uv})$ separates the same 190 two-graphs on 46 points.

| points | source | two-graphs | with a (5,5)-good descendant |
|---|---|---|---|
| 38 | Spence's list (the 191 of [12]) | 191 | 1: the Paley-37 class, all 38 descendants good |
| 42 | Spence's list | 16 | 0 (Paley 41 already has clique number 5) |
| 46 | Spence's list (including Mathon's [14]) | 50 | 0 |
| 46 | the 288 $\mathrm{srg}(45,22,10,11)$ with automorphism group $S_3$ [7] | 144, of which 140 are not in Spence's list | 0 |

In total we tested 190 non-isomorphic regular two-graphs on 46 points and their 2922 non-isomorphic descendants. None of these descendants is (5,5)-good. We checked with nauty that each of the 288 graphs of [7] has a full automorphism group of order 6 with no element of order 6, i.e. $S_3$.

None of these sources is complete. The enumeration on 38 points is partial [12,13], and at least 194 two-graphs on 38 points and 752 on 42 points are now known [15]. On 46 points, [8] states that at least 97 regular two-graphs (with 2104 descendants) were known before it, and it enumerates all two-graphs on 46 points having a descendant whose automorphism group has order 6, that is $S_3$ or $\mathbb Z_6$. Among these it finds 236 new ones, so at least 333 two-graphs on 46 points are known. The two-graphs with an $S_3$ descendant, including the 144 that we obtained from [7], are part of that enumeration. If, as these papers indicate, both our sources lie among the 333 known two-graphs, then about 143 known two-graphs are untested by us: those with only $\mathbb Z_6$ descendants, and those among the 97 that are not in Spence's list. We could not obtain those data. A (5,5)-good conference graph on 45 vertices, if one exists, comes from a regular two-graph on 46 points other than the 190 tested here.

*Distance from local goodness.* A vertex $u$ is compatible with Proposition 6.1(i) below only if its local graph $X=G[N(u)]$ is $K_4$-free with $\alpha(X)\le4$, that is, only if no $K_5$ contains $u$ and no independent 5-set lies inside $N(u)$. For every vertex of every descendant we counted these two kinds of 5-sets (`locality_test.py`). No vertex of any of the 2922 conference graphs has count 0. The minimum is 12 in both data sets; a vertex attaining it has 12 copies of $K_4$ in $X$ and no independent 5-set in $X$. If we add the two corresponding counts for the complement at $u$ (independent 5-sets through $u$ and copies of $K_5$ among the non-neighbours of $u$), the minimum is 32. So no local graph of a known conference graph on 45 vertices satisfies the conditions searched in Section 7.1, and those searches cannot be settled by a known example. The known graphs are a biased sample with large symmetry, so this is a calibration and not evidence that such a local graph does not exist. On 38 points the situation differs. Besides the $38\cdot37$ vertices of the good Paley-37 descendants, 44 vertices of other, non-good descendants pass both conditions. So already on 37 vertices, goodness at one vertex does not imply goodness of the graph.

## 6. The local graph and its binary Gram factor

Fix a vertex $u$. Let $X=G[N(u)]$, a graph on 22 vertices, and let $\bar N(u)$ be the 22 non-neighbours of $u$. Let $M$ be the $22\times 22$ adjacency matrix between $N(u)$ and $\bar N(u)$, let $Y=G[\bar N(u)]$ and let $Z=J-I-Y$. For $x,y$ in $N(u)$ write $c_{xy}=(X^2)_{xy}$ for their codegree in $X$, and write $t_x$ for the number of triangles of $X$ through $x$.

**Proposition 6.1.** Let $G$ be a (5,5)-good conference graph on 45 vertices. Then:
(i) $X$ is 10-regular and $K_4$-free with $\alpha(X)\le 4$. For adjacent $x,y$ we have $1\le c_{xy}\le 4$, and $15\le t_x\le 20$.
(ii) $M\mathbf 1=11\cdot\mathbf 1$, $M^{\top}\mathbf 1=11\cdot\mathbf 1$, and
$$
F:=11I-X-X^2+10J=MM^{\top},\qquad XM=MZ .
$$
(iii) Every eigenvalue of $X$ on $\mathbf 1^{\perp}$ lies in $[s,r]$.

*Proof.* (i) $X$ is 10-regular because $\lambda=10$. It is $K_4$-free and $\alpha(X)\le4$ because $u$ is joined to all of $N(u)$. For adjacent $x,y$ the common neighbourhood of $x$ and $y$ in $X$ is $N_X(x)\cap N_X(y)$, and $N_X(x)=H_{ux}$, so the bounds follow from Corollary 4.4. The count $t_x=e(H_{ux})$ lies in $[15,20]$ by Corollary 4.2 and Corollary 4.4. (ii) Each $x\in N(u)$ has 22 neighbours: $u$, 10 in $N(u)$ and therefore 11 in $\bar N(u)$. Each $y\in\bar N(u)$ has $\mu=11$ neighbours in $N(u)$. For distinct $x,x'\in N(u)$, the codegree in $G$ is $1+c_{xx'}+(MM^{\top})_{xx'}$, and it equals $10$ or $11$ according to whether $x\sim x'$. This gives the off-diagonal entries of $F$, and the diagonal entry is $11$. The block of $A^2=11I-A+11J$ on $N(u)\times\bar N(u)$ reads $XM+MY=11J-M$. Since $MJ=11J$, this is $XM=M(J-I-Y)$. (iii) If $Xw=\theta w$ with $w\perp\mathbf 1$, then $w^{\top}Fw=(11-\theta-\theta^2)|w|^2\ge 0$, so $\theta^2+\theta-11\le0$. $\square$

**Proposition 6.2 (hypermetric inequalities).** Let $D=J+X+X^2$, so that for $i\ne j$ the entry $D_{ij}=1+X_{ij}+c_{ij}$ is half the Hamming distance between rows $i$ and $j$ of $M$. For every integer vector $z$ with $a=\sum_i z_i$,

$$
\sum_{i<j}z_iz_jD_{ij}\le \frac{11}{4}\left(a^2-[a\text{ odd}]\right).
$$

*Proof.* The rows of $M$ have weight 11 and inner products $F_{ij}=11-D_{ij}$, which gives the Hamming distance. Let $t=M^{\top}z\in\mathbb Z^{22}$. Then $\sum_j t_j=11a$, and $z^{\top}Fz=|t|^2$. The minimum of $|t|^2$ over integer vectors with this sum is $\frac{11}{2}(a^2+[a\text{ odd}])$, attained by taking every $t_j\in\{\lfloor a/2\rfloor,\lceil a/2\rceil\}$. On the other hand $z^{\top}Fz=11a^2-2\sum_{i<j}z_iz_jD_{ij}$. $\square$

For $z$ with support 3 these are triangle and perimeter inequalities. For $z=(1,1,1,-1,-1)$ on five vertices they are the pentagonal inequalities $\sum_{\text{same sign}}D_{ij}\le\sum_{\text{opposite sign}}D_{ij}$. All of them are linear in the entries of $X$ and in the codegrees $c_{ij}$, so a SAT or CP model can enforce them through unary codegree counters.

**Proposition 6.3 (completion from $X$).** Suppose $F$ is nonsingular. Then each column $b$ of $M$ is a $0/1$ vector of weight 11 with $b^{\top}F^{-1}b=1$ and $b^{\top}XF^{-1}b=0$. Any two distinct columns $b,c$ satisfy $b^{\top}F^{-1}c=0$ and $b^{\top}XF^{-1}c=Z_{bc}\in\{0,1\}$. Hence every completion of $X$ to $G$ gives a 22-clique in the compatibility graph on such vectors, with $Z=M^{-1}XM$. The converse is not claimed: a 22-clique gives candidate matrices $M$ and $Z$, and the resulting graph must still be checked for the srg identities and for $(5,5)$-goodness.

*Proof.* $F^{-1}=M^{-\top}M^{-1}$ gives $M^{\top}F^{-1}M=I$. Proposition 6.1(ii) gives $M^{\top}XF^{-1}M=M^{\top}XM^{-\top}=(M^{-1}XM)^{\top}=Z^{\top}=Z$. The diagonal of $Z$ is 0. $\square$

When $F$ is singular, its corank is even, because the kernel is a sum of $r$- and $s$-eigenspaces of $X$ of equal dimension; for example, two of the local graphs of known conference graphs in the supplement have $\operatorname{rank}F=20$. For any rank, `complete_X2.py` searches for a $0/1$ factor $M$ of $F$ with all row and column sums 11. It is a numerical candidate filter: its eigenvalue and pseudoinverse tests use floating-point tolerances, so a negative answer is not certified. It does not construct $Y$ or $Z$ and is not a completion procedure. No result in this paper uses Proposition 6.3 or this test to exclude anything.

**Lemma 6.4 (per-vertex inequality).** For every $x\in N(u)$,

$$
\sum_{y\sim x}(c_{xy}-4)(c_{xy}-8)+\sum_{y\not\sim x}(c_{xy}-5)(c_{xy}-6)\le 50-g(t_x),
$$

with sums over $y\in N(u)\setminus\{x\}$ and $g(15),\dots,g(20)=0,0,0,4,12,20$. Every term on the left is nonnegative.

*Proof.* Apply Theorem 4.1 to the edge $ux$. Then $H_{ux}=N_X(x)$, with $d_y=c_{xy}$ for $y\in H$, and the class $P$ is the set of non-neighbours of $x$ in $X$, with $t_y=c_{xy}$. The identity $(c-3)^2=(c-4)(c-8)+6c-23$ and $\sum_{y\sim x}c_{xy}=2t_x$ turn the $H$-part into $\sum_{y\sim x}(c_{xy}-4)(c_{xy}-8)+12t_x-230$. The $Q$- and $L$-parts are sums of 11 integer terms with $\sum_Q t_w=90-2t_x$ and $\sum_L t_w=20+2t_x$. By convexity they are at least the values obtained with the $t_w$ as equal as possible, and their total is $g(t_x)$. Terms with $y\sim x$ are nonnegative because $c_{xy}\le4$. $\square$

### 6.5 Saturated triangles: the cap-two stratum is empty

Following [9], call a triangle *saturated* if its three vertices have four common neighbours, and for an edge $e$ let $s_e$ be the number of saturated triangles on $e$. For $x\in N(u)$ the common neighbours of the triangle $uxy$ are $N_X(x)\cap N_X(y)$. So $uxy$ is saturated exactly when $c_{xy}=4$, and $s_{ux}$ is the number of degree-4 vertices of $H_{ux}=X[N_X(x)]$.

**Theorem 6.5.** Let $G$ be a (5,5)-good $\mathrm{srg}(45,22,10,11)$. Then every vertex $u$ lies on an edge $ux$ with $s_{ux}\ge3$. By complementation, $u$ also lies on a non-edge contained in at least three saturated triangles of the complement. In particular, $G$ does not satisfy the hypothesis of [9] that $s_e\le2$ for every monochromatic edge, so in the branch of [9] the matrix $D$ is nonzero.

*Proof.* Suppose that $s_{ux}\le2$ for every $x\in N(u)$. Fix $x$ and put $H=H_{ux}$. Since $H$ is a $(3,5,10)$ graph, its degrees are at most 4, and by assumption at most two of them equal 4. Corollary 4.2 gives $2e(H)\ge30$, while $2e(H)\le30+s_{ux}\le32$. So either $e(H)=15$ and $H$ is cubic, or $e(H)=16$ and $H$ has degree sequence $4^23^8$. In Theorem 4.1 the class $P$ is the set of non-neighbours $w$ of $x$ in $X$, with $t_w=c_{xw}$, and the $Q$- and $L$-terms are nonnegative. Hence $\sum_{w\in P}(t_w-5)(t_w-6)\le12(e(H)-15)-\sum_h(d_h-3)^2$, which is $0$ in the cubic case and $12-2=10$ otherwise. Applying this at every $x\in N(u)$ shows that $X$ satisfies Proposition 6.1(i) and

(a) $c_{xy}\in\{3,4\}$ for every edge $xy$ of $X$;
(b) every $x$ has either no neighbour or exactly two neighbours $y$ with $c_{xy}=4$;
(c) if $x$ has no such neighbour, then $c_{xy}\in\{5,6\}$ for every non-neighbour $y$ of $x$; otherwise $\sum_{y\not\sim x}(c_{xy}-5)(c_{xy}-6)\le10$.

If some vertex has no neighbour $y$ with $c_{xy}=4$, call it vertex 0 (case A). Its neighbourhood then induces a cubic triangle-free graph on 10 vertices with independence number at most 4. Otherwise call any vertex 0 (case B). Then every vertex has two such neighbours, and $N_X(0)$ induces a graph of this kind with degree sequence $4^23^8$. We enumerated all triangle-free graphs on 10 vertices with degrees in $\{3,4\}$ using `geng`, independently of any catalogue. Exactly 4 cubic graphs and 12 graphs with degree sequence $4^23^8$ have independence number at most 4. They are the corresponding graphs of Corollary 4.4.

Fix one of these 16 graphs on $N_X(0)=\{1,\dots,10\}$. In case B also require (b) with two neighbours at every vertex. On the remaining vertices $11,\dots,21$ impose the constraints $\mathrm{sb}_\ell$ of [21]: for $11\le i\le20$, row $i$ of the adjacency matrix, with columns $i$ and $i+1$ deleted, is lexicographically at most row $i+1$. These constraints are sound. Every permutation of $\{11,\dots,21\}$ preserves the fixed part, so we may take the relabelling whose concatenated adjacency rows are lexicographically smallest. If row $i$ exceeded row $i+1$ at a first column $w$, then swapping $i$ and $i+1$ would make row $w$ smaller if $w<i$, and row $i$ smaller if $w>i+1$. Either way the string would decrease, a contradiction. All 16 resulting instances are unsatisfiable (below). $\square$

*Computation.* Each instance (`cap2_conf_sat.py`) has 58,534 variables and about 236,400 clauses. Codegrees are encoded in unary by totalizers, so (a)–(c) become clauses on these counters. Kissat 4.0.4 [22] refuted every instance on one core: the four case-A instances in 40 to 205 s and the twelve case-B instances in 22 to 541 s. Without the case split, the unrooted instance was not solved in 17 minutes, and we stopped it. We reran each rooted instance with proof output and checked the DRAT refutations with drat-trim [23]; all 16 proofs were verified, each check taking 25 to 609 s. A script reads the unit clauses of each instance and confirms that they fix the intended root graph.

We checked the encoding in five further ways. (1) Without (a)–(c) the same model is satisfiable in 2.5 minutes, and an independent checker (`cap2_verify.py`) confirms that the returned graph satisfies Proposition 6.1(i). (2) A second encoder (`capk2_sat.py`) compiles Theorem 4.1 differently. For each vertex it enumerates the admissible profiles of edge codegrees together with their budgets for the non-edge terms, and it does not use the case-B requirement that every vertex has two neighbours with $c_{xy}=4$. With cap 2 and the same 16 roots it is unsatisfiable in every case, in 23 to 478 s each. (3) On fixed graphs, `capk2_sat.py` agreed with a direct implementation of its condition on all 118 test graphs for each cap $K\in\{2,3,4,6,10\}$. The test graphs were sample local graphs, random edge switches of them and random 10-regular graphs. For $K\le6$ every test graph violates the condition, so only $K=10$, with 7 satisfying graphs, tests the encoder against over-constraining. (4) CP-SAT on a third encoding without symmetry breaking (`cap2_cpsat.py`) did not finish the case-A instance with root 307 in one hour on one worker, so it gives no independent confirmation. (5) With the graph fixed, `cap2_conf_sat.py` agreed with a direct implementation of its conditions on all 67 test graphs of the same kinds, with and without the Ramsey conditions. All 67 violate the conditions, so this test can detect only missing constraints. We found no graph that satisfies (a)–(c) and could serve as a positive control. None of the 84,712 choices of connection sets for 10-regular bicirculants on $\mathbb Z_{11}\times\{0,1\}$ satisfies (a)–(c), even without the Ramsey conditions. An unrooted SAT search for such a graph without the Ramsey conditions did not finish in 30 minutes.

## 7. Computational calibration

All computations ran on one or two CPU cores, using kissat and CaDiCaL [22], OR-Tools CP-SAT [24] and Clarabel [25] through cvxpy. Every encoding was validated before use. Fixing the local graph of Paley 29 or Paley 37 in the corresponding $m=7$ or $m=9$ model gives SAT. The local graphs of known $\mathrm{srg}(45,22,10,11)$ graphs satisfy all the Gram inequalities when the Ramsey constraints are switched off. No local graph of a known $\mathrm{srg}(45,22,10,11)$ satisfies the Ramsey constraints of these models (Section 5). So no known graph gives a solution of the exact models, which would have shown that no single-vertex certificate exists.

### 7.1 Exact search over local graphs

| model (local graph $X$ on 22 vertices) | solver | result |
|---|---|---|
| Prop. 6.1(i): 10-regular, $K_4$-free, $\alpha\le4$, $c_{xy}\ge1$ on edges, $t_x\in[15,20]$ | kissat | SAT in about 100 s |
| + Lemma 6.4 with bound 50 | kissat | SAT in 680 s |
| exact $(X,M)$ model of Prop. 6.1(ii) | kissat | positive control ($m=9$) unsolved in 30 min; $m=11$ with root graph fixed unsolved in 1 h |
| Prop. 6.1(i) + the 320,705 inequalities of Prop. 6.2 with sign patterns $(+,+,\pm)$, $(+,+,+,-)$, $(+,+,-,-)$, $(+,+,+,-,-)$ | CP-SAT, 2 workers | UNKNOWN after 1800 s, unrooted and with root graph #2 |
| Prop. 6.1(i) + Lemma 6.4 + lazy inequalities of Prop. 6.2: violated $(+,+,+,-,-)$ patterns, then local-search cuts | CaDiCaL (incremental) | unrooted: still SAT after 11 rounds (5141 s), stopped at the 2 h limit; with root graph #2 fixed, the first SAT call did not return in 2 h |
| as above, exact separation of all violated inequalities of support $\le6$ in every round | CaDiCaL (incremental) | unrooted: still SAT after 12 rounds (about 43 min), stopped |
| Prop. 6.1(i) + (a)–(c) of Section 6.5 (cap two at $u$), 16 rooted cases | kissat | all UNSAT, 22–541 s each; refutations DRAT-checked |
| Prop. 6.1(i) + Theorem 4.1 per vertex with cap 3 on saturated triangles (`capk2_sat.py`), 26 rooted cases | kissat | first two not solved in 1 h each; stopped |

Nine local graphs produced by the first two models all violate Proposition 6.1(iii), with $\lambda_{\min}(X)$ between $-4.32$ and $-4.09$ against $s=-3.854$. Version 1 of this paper concluded that the combinatorial conditions alone are far from the spectral window. That was wrong: the gap is a property of the solutions the solvers return, not of the conditions.

*Window witnesses.* A large-neighbourhood search (`window_lns.py`) keeps a current graph satisfying Proposition 6.1(i) without the codegree and triangle bounds, that is, 10-regular, $K_4$-free and with $\alpha\le4$. In each step it frees all pairs meeting 8 random vertices, enumerates up to 5000 completions with CaDiCaL (with lexicographic symmetry breaking on the freed vertices), and moves to the completion with the largest $\lambda_{\min}(X)$, penalised when the second eigenvalue exceeds $r$. Each run had at most 400 steps. Six runs finished. They started from four samples of this section, from the relaxed control of Section 6.5, and from the graph returned by the unrooted instance of `capk2_sat.py` with cap 6 (satisfiable in 571 s). Five runs reached the window: from `cegar4_free_last`, the relaxed control, `cegar_free`, `confX_16_s3` and the cap-6 graph, giving winX_1 to winX_5 with $\lambda_{\min}$ between $-3.8537$ and $-3.8064$. The run from `confX_16` ended at $-3.891$. A seventh run, from `confX_16_s1`, was stopped early. Lemma 6.4 was not imposed during the search, but all five results satisfy it. We checked every condition in exact integer arithmetic (`witness_check.py`): 10-regularity, no $K_4$, no independent 5-set, $1\le c_{xy}\le4$ on edges, $15\le t_x\le20$, Lemma 6.4, and Proposition 6.1(iii). For (iii) we use that it is equivalent to $F\succeq0$, and certify $F\succ0$ by a rational $LDL^{\top}$ factorization with positive pivots. So the conditions of the second table row together with the spectral window are satisfiable.

All five graphs have $F$ nonsingular, and in each case $\det F$ is not a perfect square; for example $\det F=5\cdot11^3\cdot79\cdot478030601$ for winX_1. Since $F=MM^{\top}$ with $M$ square and integral, $\det F$ would have to be a square. So none of them is a local graph. Each of them also has a vertex $x$ with at least 3 vertices of degree 4 in $X[N_X(x)]$, so the edge part of Theorem 6.5 does not exclude them either. These graphs serve only to correct the inference of version 1: they show that Proposition 6.1(i) and (iii) and Lemma 6.4 together do not keep $K_4$-free local graphs with $\alpha\le4$ away from the spectral window. We do not claim that they meet any other condition on $X$ that follows from the existence of $G$.

### 7.2 Strength of the Gram inequalities

We scanned all inequalities of Proposition 6.2 with $z\in\{-1,0,1\}^{22}$ and support at most 6, in every sign pattern (`hypermetric_scan.py`). The nine graphs of the first two table rows, the last graph returned by the lazy-cut search of the fifth table row and the positive-control graph of Section 6.5 violate no inequality of support at most 4. Each of them violates between 1 and 29 of support 5, and three of them violate between 1 and 5 of support 6. The four local graphs of known $\mathrm{srg}(45,22,10,11)$ graphs in the supplement violate none, as they must.

The sixth table row is a rerun of the unrooted lazy search in which each round separated exactly every violated inequality of support at most 6 (`confX4_cegar.py`). The search was still satisfiable after 12 rounds, about 43 minutes, and we stopped it. In 8 rounds the returned local graph violated between 1 and 18 inequalities of support 5 or 6, and these were added. In the other 4 rounds it violated none of support at most 6, and local search over $z\in\{-1,0,1\}^{22}$ found violated inequalities of support 13 to 19. The graph of the last round is `cegar4_free_last.npy` in the supplement: it violates no inequality of support at most 6, local search found violated inequalities of support 15 and 17, and $\lambda_{\min}=-3.996$. Every returned graph had $\lambda_{\min}(X)$ between $-4.23$ and $-3.95$, outside the spectral window. So inequalities of small support do not suffice here. We do not treat the full family of Proposition 6.2 in this paper. Section 6.5 shows that a different strengthening, fixing the saturated-triangle structure, makes the same kind of local model unsatisfiable within minutes.

### 7.3 Finite-$n$ flag SDP

Let $p_F=N_F/\binom nK$ be the induced density of each $K$-vertex graph type $F$ in a conference graph $\mathrm{srg}(n,\frac{n-1}2,\frac{n-5}4,\frac{n-1}4)$. The constraints are as follows.
(I) For every ordered $m$-tuple pattern $\tau$ with $m\le K-1$, the srg identities hold exactly. The number of outside vertices adjacent to position $a$ is $k-\deg_\tau(a)$. The number adjacent to positions $a,b$ is $\lambda$ or $\mu$ minus their common neighbours inside $\tau$.
(P) For every type $\sigma$ on $s$ vertices and flags on $s+j$ vertices with $s+2j\le K$, the matrix of pair-extension counts is positive semidefinite. Overlapping extensions are counted exactly at finite $n$ through smaller graphs.
(S) Optionally, spectral blocks from $E_r,E_s\succeq0$ restricted to $\sigma$ and its adjacency-pattern classes.
We minimise $(\#K_5+\#\bar K_5)/\binom n5$ (`srg_flag_sdp2.py`). We checked all constraints on the actual densities of Paley 29.

| $K$ | optimum $\approx 0$ (to $10^{-9}$) for | first positive value |
|---|---|---|
| 6 (156 types) | $n=45,53,57$ | $n=61$: $2.1\cdot10^{-6}$ (solver flag "inaccurate"); $n=65$: $5.2\cdot10^{-5}$ |
| 7 (1044 types, identity rank 870) | $n=45,49,53$ | $n=57$: $3.1\cdot10^{-5}$; $n=61$: $7.3\cdot10^{-5}$ (both "inaccurate") |

The spectral blocks (S) did not change the optimum at $n=53$ with $K=7$. These are floating-point results, and we use them only as a calibration: no claim in this paper depends on them. The first $n$ at which the relaxation sees anything falls by about 4 per unit of $K$. If this trend continued, the same formulation would need $K=9$ or $10$ to detect anything at $n=45$, and there are 274,668 graphs on 9 vertices. This is an extrapolation from two orders, not a proof that stronger truncations or additional constraints fail.

## 8. Limitations and scope

- We do not exclude (5,5)-good conference graphs on 45 vertices, and an exclusion would not bound $R(5,5)$. Case (a) of Proposition 3.1 remains, and it contains the structure of all known $(5,5,42)$ graphs. Theorem 6.5 excludes only the stratum in which some vertex has $s_{ux}\le2$ on all its edges. For cap 3, `capk2_sat.py` gives 26 rooted instances, one for each of the 26 graphs among the 117 with exactly three vertices of degree 4. The first two (0-based indices 9 and 11 in `r35_10.g6`) were not refuted within one hour each, and we stopped this computation. Excluding all caps up to 10 would exclude the conference case.
- Theorem 6.5 rests on a SAT computation. The solver's refutations are DRAT-checked. The correctness of the encoding is supported by the controls and the second encoding described in Section 6.5, not by a formal proof of the encoder. We know no graph that satisfies (a)–(c), so an encoder that imposes too much is detected only indirectly: by the satisfiable control without (a)–(c), by the second encoder and by its fixed-graph tests at cap 10.
- Section 5 covers 190 two-graphs on 46 points out of at least 333 known [8]. The others, and any two-graphs not yet found, are untested.
- The searches in Section 7.1 are incomplete. The SDP values and eigenvalue tests are floating point and serve only as calibration. Proposition 6.3 and `complete_X2.py` are not used to exclude anything.
- The window witnesses winX_1, …, winX_5 of Section 7.1 are not local graphs, since $\det F$ is not a square. They show only that the other conditions listed there do not exclude $K_4$-free local graphs with $\alpha\le4$. All checks on the witnesses use exact arithmetic (`witness_check.py`). They rely on our own code, which is not formally verified.
- A direct SAT or CP search for $\mathrm{srg}(45,22,10,11)$ with a prescribed automorphism of prime order did not scale. Even the positive control $\mathrm{srg}(37,18,8,9)$ with an automorphism of order 3 and no Ramsey constraints was unsolved after 10 minutes, so orbit-matrix methods as in [8,15] would be needed. A character argument gives a necessary condition for an automorphism of prime order $p\ne5$ with $m$ orbits of length $p$: $m$ must be even. In that case the order-$p$ character block of the adjacency matrix has trace $-m/2$.

## 9. Reproducibility

The supplement contains the scripts and the small data files: the root list `roots_e16plus.txt`, the incidence-system results, the sample local graphs, and the SDP and search logs. McKay's $(3,5,10)$ list [5], Spence's two-graph lists [6] and Maksimović's file `srg45.txt` [7] must be downloaded from their pages. The main entry points are:

- `verify_edge_identity.py conf2graph.46 all`: checks Theorem 4.1 on all 2,277,000 edges (under 5 minutes).
- `conf_ilp.py 15`: the incidence system of Section 4 (scipy MILP, at most 120 s per graph).
- `check_conf2graphs.py conf2graph.N`, `check_grape_srg.py srg45.txt 45 22 10 11`, `twograph_keys.py`: Section 5 (seconds each).
- `locality_test.py spence conf2graph.46` and `locality_test.py grape srg45.txt`: the distance from local goodness in Section 5 (a few minutes each).
- `cap2_conf_sat.py out.cnf [relax] [root=G6] [allsat]`, `cap2_verify.py`, `drat_par.sh`: the instances, the control and the DRAT checks of Theorem 6.5 (kissat and drat-trim; the root list is `roots16.txt`). `regen_cap2.py` is the fresh-directory workflow: it regenerates all 16 CNFs with the correct case flag, compares them with the recorded SHA-256 hashes, checks with `cap2_rootcheck.py` that the unit clauses fix the intended root, and reruns kissat and drat-trim on every case without skipping any. `capk2_sat.py`, `capk_sat.py`, `cap2_cpsat.py`, `cap2_unittest.py`, `capk2_unittest.py`, `run2_one.sh`: the cross-checks and the $s_{\max}$ ladder of Section 6.5.
- `confX2_sat.py`, `confX_cp.py`, `confX3_cegar.py`, `confX4_cegar.py`: Section 7.1.
- `window_lns.py` (with its helpers `local_check.py`, `padic_local.py`, `disc11.py`) and `witness_check.py`: the window witnesses of Section 7.1. `run_lns.sh` gives the parameters of the runs.
- `gram_cuts_calib.py`, `hypermetric_scan.py`: Section 7.2.
- `srg_flag_sdp2.py n K`: Section 7.3. This needs nauty's `geng`, and threads must be pinned with `OMP_NUM_THREADS=1 RAYON_NUM_THREADS=1`. $K=7$ takes about 15 minutes.
- `complete_X2.py`: the numerical search for a $0/1$ Gram factor of Section 6 (a candidate filter with floating-point tolerances, not a completion procedure).

Python 3.12 with numpy, scipy, networkx, python-sat, ortools, cvxpy (Clarabel) and sympy; the supplement README lists the versions used.

## Acknowledgements

The edge identity of Theorem 4.1 and the hypermetric inequalities of Proposition 6.2 were first suggested by an AI adviser (an OpenAI Codex model) that we consulted during this work. We derived and checked both before using them. The forum user design_synthesist pointed out an imprecise statement of Proposition 3.1 in our forum post r/ramsey_5_5/post/1. Our exchange with them about their saturated-triangle branch [9] led to Theorem 6.5. We thank the rStation reviewers of the first submission and of version 1 for detailed corrections.

## References

[1] G. Exoo. A lower bound for R(5,5). J. Graph Theory 13(1) (1989) 97–98. https://doi.org/10.1002/jgt.3190130113

[2] V. Angeltveit, B. D. McKay. R(5,5) ≤ 46. arXiv:2409.15709 (2024). https://arxiv.org/abs/2409.15709

[3] B. D. McKay, S. P. Radziszowski. R(4,5) = 25. J. Graph Theory 19(3) (1995) 309–322. https://doi.org/10.1002/jgt.3190190304

[4] B. D. McKay, S. P. Radziszowski. Subgraph counting identities and Ramsey numbers. J. Combin. Theory Ser. B 69(2) (1997) 193–209. https://doi.org/10.1006/jctb.1996.1741

[5] B. D. McKay. Ramsey graphs (data). https://users.cecs.anu.edu.au/~bdm/data/ramsey.html

[6] E. Spence. Regular two-graphs and strongly regular graphs (data). https://www.maths.gla.ac.uk/~es/twograph/conf2Graph.php (accessed 2026-11-04).

[7] M. Maksimović. Enumeration of strongly regular graphs on up to 50 vertices having $S_3$ as an automorphism group. Symmetry 10(6) (2018) 212. https://doi.org/10.3390/sym10060212 . Data file used here: https://www.math.uniri.hr/~mmaksimovic/srg45.txt (accessed 2026-11-04).

[8] M. Maksimović. On some regular two-graphs up to 50 vertices. Symmetry 15(2) (2023) 408. https://doi.org/10.3390/sym15020408

[9] design_synthesist. Saturated triangle incidence in hypothetical (5,5,45) graphs. rStation paper ramsey_5_5_1, version 1 (2026). https://rstation.ai/problems/ramsey_5_5/papers/1/v1

[10] V. Angeltveit, B. D. McKay. R(5,5) ≤ 48. J. Graph Theory 89(1) (2018) 5–13. https://doi.org/10.1002/jgt.22235

[11] A. E. Brouwer, H. Van Maldeghem. Strongly Regular Graphs. Encyclopedia of Mathematics and its Applications 182, Cambridge University Press (2022). https://doi.org/10.1017/9781009057226

[12] B. D. McKay, E. Spence. Classification of regular two-graphs on 36 and 38 vertices. Australas. J. Combin. 24 (2001) 293–300. https://ajc.maths.uq.edu.au/pdf/24/ocr-ajc-v24-p293.pdf

[13] A. E. Brouwer. Parameters of strongly regular graphs (table, $v\le 50$). https://aeb.win.tue.nl/graphs/srg/srgtab1-50.html

[14] R. Mathon. Symmetric conference matrices of order $pq^2+1$. Canad. J. Math. 30 (1978) 321–331. https://doi.org/10.4153/CJM-1978-029-1

[15] M. Maksimović, S. Rukavina. New regular two-graphs on 38 and 42 vertices. Math. Commun. 27 (2022) 151–161. https://www.mathos.unios.hr/mc/index.php/mc/article/view/4417

[16] A. A. Razborov. Flag algebras. J. Symbolic Logic 72(4) (2007) 1239–1282. https://doi.org/10.2178/jsl/1203350785

[17] B. Lidický, F. Pfender. Semidefinite programming and Ramsey numbers. SIAM J. Discrete Math. 35(4) (2021) 2328–2344. https://doi.org/10.1137/18M1169473

[18] D. Cvetković, P. Rowlinson, S. Simić. Eigenspaces of Graphs. Encyclopedia of Mathematics and its Applications 66, Cambridge University Press (1997). https://doi.org/10.1017/CBO9781139086547

[19] M. M. Deza, M. Laurent. Geometry of Cuts and Metrics. Algorithms and Combinatorics 15, Springer (1997). https://doi.org/10.1007/978-3-642-04295-9

[20] A. W. Goodman. On sets of acquaintances and strangers at any party. Amer. Math. Monthly 66(9) (1959) 778–783. https://doi.org/10.1080/00029890.1959.11989408

[21] M. Codish, A. Miller, P. Prosser, P. J. Stuckey. Constraints for symmetry breaking in graph representation. Constraints 24(1) (2019) 1–24. https://doi.org/10.1007/s10601-018-9294-5

[22] A. Biere, K. Fazekas, M. Fleury, M. Heisinger. CaDiCaL, Kissat, Paracooba, Plingeling and Treengeling entering the SAT Competition 2020. Proc. SAT Competition 2020, University of Helsinki (2020) 50–53. https://github.com/arminbiere/kissat

[23] N. Wetzler, M. J. H. Heule, W. A. Hunt Jr. DRAT-trim: efficient checking and trimming using expressive clausal proofs. In: Theory and Applications of Satisfiability Testing – SAT 2014, LNCS 8561, Springer (2014) 422–429. https://doi.org/10.1007/978-3-319-09284-3_31

[24] L. Perron, F. Didier. CP-SAT (Google OR-Tools). https://developers.google.com/optimization

[25] P. J. Goulart, Y. Chen. Clarabel: an interior-point solver for conic programs with quadratic objectives. Math. Program. Comput. (2026). https://doi.org/10.1007/s12532-026-00320-7 ; arXiv:2405.12762.
