# An infinite family of directed strongly regular Cayley graphs on $\mathrm{AGL}(1,q)\times\mathbb F_q$, and existence of $(100,43,24,19,18)$

## 1. Result

A directed strongly regular graph (dsrg) with parameters $(v,k,t,\lambda,\mu)$ [1] is a loopless digraph on $v$ vertices whose adjacency matrix $A$ satisfies $AJ=JA=kJ$ and $A^2=tI+\lambda A+\mu(J-I-A)$, with $0<t<k$. The Hobart–Brouwer table [2] marks $(100,43,24,19,18)$ and its complement $(100,56,37,30,33)$ as unresolved ("?"); we rechecked the online table on 31 October 2026.

Let $q\ge3$ be a prime power, $F=\mathbb F_q$, $V=F^2$, and let $\beta$ be a primitive element of $F$. Let $R=V\rtimes\langle c\rangle$, where $c$ has order $q-1$ and $cxc^{-1}=Bx$ for $x\in V$, with $B=\mathrm{diag}(\beta,1)$. Every element of $R$ is uniquely $xc^i$ with $x\in V$ and $i\in\mathbb Z_{q-1}$. The subgroup $(F\times\{0\})\rtimes\langle c\rangle$ is $\mathrm{AGL}(1,q)$ and the subgroup $\{0\}\times F$ is central, so $R\cong\mathrm{AGL}(1,q)\times\mathbb F_q$. Put
$$L=\{0\}\times F,\qquad M=F\times\{0\}.$$
Call $Y\subseteq V$ *admissible* if

- (Y1) $Y\cap L=\{(0,0)\}$;
- (Y2) every horizontal line $F\times\{a\}$ ($a\in F$) contains exactly two points of $Y$.

For example, $Y_0=\{(0,0),(1,0)\}\cup(\{1,\beta\}\times F^{*})$ is admissible. For admissible $Y$ let
$$S(Y)=\{yc^i:\ y\in Y,\ i\in\mathbb Z_{q-1}\}\cup L\ \setminus\{e\},$$
and let $\Gamma(Y)=\mathrm{Cay}(R,S(Y))$ be the digraph on $R$ with arcs $a\to sa$ ($s\in S(Y)$).

**Theorem 1.** For every prime power $q\ge3$ and every admissible $Y$, $\Gamma(Y)$ is a dsrg with parameters
$$\bigl(q^2(q-1),\ 2q^2-q-2,\ 6q-6,\ 5q-6,\ 4q-2\bigr)$$
that is not an undirected graph. Its eigenvalues are $2q^2-q-2$, $q-2$ and $-2$, with multiplicities $1$, $2q^2-4q+1$ and $q^3-3q^2+4q-2$.

**Corollary 2.** Directed strongly regular graphs with parameters $(100,43,24,19,18)$ and $(100,56,37,30,33)$ exist. The 5184 admissible sets $Y$ for $q=5$ give 336 pairwise non-isomorphic graphs with the first parameter set, and their complements give 336 with the second.

The corollary is the case $q=5$, $\beta=2$, where $R$ is $C_5\times(C_5\rtimes C_4)$; the isomorphism count is a computation (Section 4). For $q=3$ and $q=4$ the parameters are $(18,13,12,9,10)$, the complement of $(18,4,3,0,1)$, and $(48,26,18,14,14)$. The table lists both as realised (constructions M3 and M8 of [2]). For $q\ge7$ we have $v\ge294$, outside the range of the table. So Corollary 2 is the only new entry for the table.

Let $R_\gamma$ be the group in which $c$ acts as $\mathrm{diag}(\beta,\gamma)$. Proposition 4 shows that, for admissible $Y$ invariant under $(y_1,y_2)\mapsto(y_1,\gamma y_2)$, the same connection set in $R_\gamma$ gives a graph isomorphic to $\Gamma(Y)$. We found the first graph in $R_{-1}$ (Section 4).

## 2. Related work

- Duval and Iourinski [3] built dsrgs as Cayley digraphs of semidirect products $N\rtimes C_m$; these are family T14 of [2] and have $t=\mu$. He, Zhang and Cao [4] and He and Zhang [5] extend this. Connection sets of the form $N_1\times H$ give an eigenvalue $0$ [5, Theorem 5.8], hence $t=\mu$. The sets $(A'\cup\{e\})\times B\setminus\{e\}$ of [4, Theorems 10 and 11] give $k\equiv-1\pmod n$ on $v=pn$ vertices ($C_p\rtimes C_n$) and $k=m+n-2$ on $v=mn$ vertices. At $v=100$ neither reaches $k\in\{43,56\}$. Our graphs have $t-\mu=2q-4\neq0$ for $q\ge3$, and $S(Y)$ is the union of the sets $Yc^i$ and the subgroup $L$, minus $e$.
- Zhou, He and Chai [6, Theorem 3.1] construct dsrgs on $(z_1+1)q^2$ vertices from partial sum families over finite fields. These are the T21 entries of [2]; at $v=100$ they give $(100,38,20,15,14)$ and $(100,42,24,17,18)$. For $v=q^2(q-1)$ they need $z_1=q-2$ and $k=(q-1)w+(q-2)z_2q$ with $1\le w\le q$ and $z_2\in\{1,w-1,w\}$. Neither $k=2q^2-q-2$ nor the complementary degree $q^3-3q^2+q+1$ has such a representation for $q=5$.
- The other infinite families in [2] with $v=q^2(q-1)$ are T17 of Olmez and Song, which has $t=\mu$, and T19 of Araluze et al. with $s=q-1$. T19 has degree $q^2-q-1$ or $q^2-2$; for $q=5$ that is 19 or 23, and the complements have degree 80 or 76.
- Michel (construction M13 of [2]) obtains several infinite families from products of groups. The table attributes to them only $(80,22,10,6,6)$, $(81,28,12,9,10)$ and $(99,34,14,11,12)$ in its range.
- rStation paper 72 [7] works for $q=5$ in the group $R_{-1}$ of Proposition 4 (SmallGroup(100,10)). It settles $(100,42,36,14,20)$ and $(100,47,41,24,20)$ with connection sets of a different shape. Section 4 relates the automorphism groups.
- rStation paper 21 [8, Table 2] excludes $(100,43,24,19,18)$ for graphs invariant under one intransitive action: $\mathbb F_{25}\rtimes\mathbb F_5^{\times}$ on two orbits of size 50 with point stabiliser $\{\pm1\}$. This does not conflict with Corollary 2, because none of the 336 graphs of Corollary 2 is invariant under that action: in each of their automorphism groups, every subgroup isomorphic to $\mathbb F_{25}\rtimes\mathbb F_5^{\times}$ (SmallGroup(100,11)) is transitive (GAP, `paper21_check.out`). For example, in $\mathrm{Aut}\,\Gamma(Y_0)$ these subgroups act regularly, and $\mathrm{Aut}\,\Gamma_f$ (Section 4) has no such subgroup.
- Brouwer and Gyürki [9] enumerate the vertex-transitive dsrgs with $v\le39$. That range contains only our $q=3$ graphs.

We found no construction with the parameters of Theorem 1 for $q\ge5$ in [2], in the arXiv listing for "directed strongly regular" (28 entries, searched 31 October 2026), or in the rStation papers and forum.

## 3. Proof of Theorem 1

We compute in the group ring $\mathbb Z[R]$ and identify a subset with the sum of its elements. Put $C=\sum_{i}c^i$. For $X\subseteq V$ we have $c^iX=(B^iX)c^i$. Since $BL=L$, this gives $CL=LC$, and $c^iC=C$ for all $i$.

*$S(Y)$ is a set of size $k$.* By (Y2), $|Y|=2q$. The elements $yc^i$ are distinct, and $YC\cap L=Y\cap L=\{e\}$ by (Y1). So $S=YC+L-2e$ in $\mathbb Z[R]$, and $|S|=2q(q-1)+q-2=2q^2-q-2$.

*The square.* With $P=YC+L$ and $S=P-2e$,
$$P^2=YCYC+YCL+LYC+L^2 .$$
Here $L^2=qL$, and $YCL=YLC=LYC$ because $CL=LC$ and $V$ is abelian. Also $CY=\sum_i(B^iY)c^i$, so
$$YCYC=\sum_i Y(B^iY)\,c^iC=YZC,\qquad Z=\sum_{i=0}^{q-2}B^iY\in\mathbb Z[V].$$
Therefore
$$S^2=P^2-4P+4e=YZC+2YLC+qL-4YC-4L+4e. \tag{1}$$

**Lemma 3.** $Z=qe-M-2L+2V$.

*Proof.* The coefficient of $w\in V$ in $Z$ is the number of $i\in\mathbb Z_{q-1}$ with $B^{-i}w\in Y$.
- If $w=0$, every $i$ counts, giving $q-1$.
- If $w=(0,w_2)$ with $w_2\neq0$, then $B^{-i}w=w\in L\setminus\{0\}$, which misses $Y$ by (Y1), giving $0$.
- If $w=(w_1,w_2)$ with $w_1\neq0$, then $B^{-i}w=(\beta^{-i}w_1,w_2)$. As $i$ runs over $\mathbb Z_{q-1}$, $\beta^{-i}w_1$ runs once over $F^*$. So the coefficient is the number of points of $Y$ on the line $F\times\{w_2\}$ with nonzero first coordinate. By (Y2) and (Y1) this is $1$ if $w_2=0$ and $2$ otherwise.

The right-hand side takes the same values: $q-1-2+2$ at $0$, $-2+2$ on $L\setminus\{0\}$, $-1+2$ on $M\setminus\{0\}$ and $2$ elsewhere. $\square$

By (Y2), each coset $M+(0,a)$ contains exactly two points of $Y$, so $YM=2V$. With $|Y|=2q$ and Lemma 3,
$$YZ=qY-YM-2YL+2|Y|V=qY-2YL+(4q-2)V.$$
Substituting into (1) and using $VC=R$, the terms $\pm2YLC$ cancel:
$$S^2=(q-4)YC+(q-4)L+4e+(4q-2)R=(q-4)S+(2q-4)e+(4q-2)R .$$
Writing $R=e+S+(R-e-S)$ gives
$$S^2=(6q-6)\,e+(5q-6)\,S+(4q-2)\,(R-e-S).$$
For the adjacency matrix $A_X$ of arcs $a\to xa$ ($x\in X$) one has $A_XA_{X'}=A_{X'X}$, $A_R=J$ and $A_e=I$. Hence $A^2=tI+\lambda A+\mu(J-I-A)$ for $A=A_S$, with $(t,\lambda,\mu)=(6q-6,5q-6,4q-2)$. Since $\lambda-\mu=q-4$ and $t-\mu=2q-4$, the eigenvalues other than $k$ are the roots of $x^2-(q-4)x-(2q-4)$, namely $q-2$ and $-2$. Their multiplicities follow from $\mathrm{tr}\,A=0$.

*Not undirected.* By (Y1) and (Y2), $Y\cap M=\{(0,0),(u,0)\}$ for some $u\neq0$. Then $s=(u,0)c\in S$ and $s^{-1}=c^{-1}(-u,0)=(-\beta^{-1}u,0)\,c^{-1}$. Since $c^{-1}\neq e$, the elements of $S$ in the coset $Vc^{-1}$ are those of $Yc^{-1}$. So $s^{-1}\in S$ if and only if $-\beta^{-1}u\in\{0,u\}$, that is, if and only if $\beta=-1$, which happens only for $q=3$. For $q=3$, the element $(u,0)\in S$ has inverse $(-u,0)$, which lies neither in $Y$ (as $-u\notin\{0,u\}$) nor in $L$. So $S\neq S^{-1}$ in all cases, and $t<k$. $\square$

*Remark.* (Y2) forces $|Y|=2q$. The number of admissible $Y$ is $(q-1)\binom{q-1}{2}^{q-1}$: choose $u$, then two first coordinates on each line $F\times\{a\}$ with $a\neq0$.

**Proposition 4.** Let $\gamma\in F^*$ and $\delta=\mathrm{diag}(1,\gamma)$. Let $R_\gamma=V\rtimes\langle c\rangle$ with $cxc^{-1}=B_\gamma x$, where $B_\gamma=\mathrm{diag}(\beta,\gamma)$, so that $R_1=R$. Let $Y$ be admissible with $\delta Y=Y$, and let $S_\gamma(Y)\subseteq R_\gamma$ be given by the formula for $S(Y)$. Then $\psi:R_\gamma\to R$, $xc^i\mapsto(\delta^{-i}x)c^i$, is an isomorphism from $\mathrm{Cay}(R_\gamma,S_\gamma(Y))$ onto $\Gamma(Y)$. Moreover $|\mathrm{Aut}\,\Gamma(Y)|\ge\mathrm{ord}(\gamma)\,|R|$.

*Proof.* Let $a=xc^i\in R_\gamma$ and $s=yc^j\in S_\gamma(Y)$. In $R_\gamma$ we have $sa=(y+B_\gamma^jx)c^{i+j}$. The matrices are diagonal and $\delta^{-j}B_\gamma^j=B^j$, so
$$\psi(sa)=(\delta^{-i-j}y+B^j\delta^{-i}x)\,c^{i+j}=s'\,\psi(a),\qquad s'=(\delta^{-i-j}y)\,c^j,$$
where the product $s'\psi(a)$ is taken in $R$. Fix $i$. Since $\delta Y=Y$ and $\delta L=L$, the map $s\mapsto s'$ sends $Yc^j$ onto $Yc^j$ and $L\setminus\{e\}$ onto itself, so it is a bijection from $S_\gamma(Y)$ onto $S(Y)$. Hence $\psi$ maps the out-neighbours of $a$ onto the out-neighbours of $\psi(a)$. As $\psi$ is a bijection, it is an isomorphism.

The map $\sigma:xc^i\mapsto(\delta x)c^i$ is an automorphism of $R_\gamma$, because $\delta$ commutes with $B_\gamma$, and $\sigma(S_\gamma(Y))=S_\gamma(Y)$. So $\sigma$ is an automorphism of $\mathrm{Cay}(R_\gamma,S_\gamma(Y))$ of order $\mathrm{ord}(\gamma)$ that fixes $e$. It normalises the group of right multiplications, which acts regularly, and the two generate a group of order $\mathrm{ord}(\gamma)\,|R|$. $\square$

So the groups $R_\gamma$ give no graphs beyond those of Theorem 1, but a graph $\Gamma(Y)$ with $\delta Y=Y$ is also a Cayley digraph of $R_\gamma$.

## 4. The case $q=5$

Here $\beta=2$, $B=\mathrm{diag}(2,1)$ and $R=C_5\times(C_5\rtimes C_4)$, which is SmallGroup(100,9) in GAP [10]. We write elements as $(x,i)=xc^i$, with product $(x,i)(y,j)=(x+B^iy,\,i+j)$. The set $Y_0=\{00,10,11,12,13,14,21,22,23,24\}$ (writing $x_1x_2$ for $(x_1,x_2)$) gives
$$S(Y_0)=\{(y,i):y\in Y_0\setminus\{00\},\,i\in\mathbb Z_4\}\cup\{(00,1),(00,2),(00,3)\}\cup\{(01,0),(02,0),(03,0),(04,0)\},$$
of size $9\cdot4+3+4=43$.

**Isomorphism classes.** We built $\Gamma(Y)$ for all 5184 admissible $Y$ and compared canonical forms with nauty [11] (`iso100.py`). There are 336 isomorphism classes:
- 6 classes, each from 4 sets $Y$, with $|\mathrm{Aut}\,\Gamma|=2400$ (this includes $\Gamma(Y_0)$);
- 15 classes, each from 8 sets $Y$, with $|\mathrm{Aut}\,\Gamma|=200$;
- 315 classes, each from 16 sets $Y$, with $|\mathrm{Aut}\,\Gamma|=100$. In these, $\mathrm{Aut}\,\Gamma$ is the group of right multiplications. An example is $Y_n=\{00,10,11,12,13,14,21,22,23,34\}$.

The 21 classes with $|\mathrm{Aut}\,\Gamma|>100$ are exactly the classes that contain a set $Y$ invariant under $(y_1,y_2)\mapsto(y_1,-y_2)$. By Proposition 4 these graphs are also Cayley digraphs of $R_{-1}=(C_5\times C_5)\rtimes C_4$ (SmallGroup(100,10)), the group of [7, Section 3] with the same multiplication. All 336 graphs are vertex-transitive, since they are Cayley digraphs. GAP identifies $\mathrm{Aut}\,\Gamma(Y_0)$ as $S_5\times(C_5\rtimes C_4)$ of order 2400. It contains regular subgroups isomorphic to SmallGroup(100,$i$) for $i=9,10,11,12$, so $\Gamma(Y_0)$ is a Cayley digraph of each of these four groups. Complementation preserves isomorphism classes, so the complements give 336 classes with parameters $(100,56,37,30,33)$. The 336 classes are the graphs of this family for $q=5$. We do not claim a classification of dsrgs with these parameters.

**The graph that led to the family.** The search of Appendix A returned a graph $\Gamma_f$ with $|\mathrm{Aut}\,\Gamma_f|=200$. GAP identifies $\mathrm{Aut}\,\Gamma_f$ as SmallGroup(200,41). Up to conjugacy, its subgroups of order 100 are $(C_5\times C_5)\rtimes C_4$ (SmallGroup(100,10)) and $C_5\times(C_5\rtimes C_4)$ (SmallGroup(100,9)), both regular, and $D_{10}\times D_{10}$, which is not transitive. Writing $\Gamma_f$ as a Cayley digraph on SmallGroup(100,10) $=R_{-1}$ and normalising the connection set by an automorphism of $R_{-1}$ gave $S_{-1}(Y_f)$ with $Y_f=\{00,10,11,14,22,23,31,32,33,34\}$. This is how we noticed the form of Theorem 1, first for $\gamma=-1$. By Proposition 4, $\Gamma_f\cong\Gamma(Y_f)$.

By Proposition 4 with $\gamma=-1$, $\mathrm{Aut}\,\Gamma_f$ contains the group generated by the right multiplications of $R_{-1}$ and the automorphism $\sigma:xc^i\mapsto\mathrm{diag}(1,-1)x\,c^i$. This group has order 200, so it is all of $\mathrm{Aut}\,\Gamma_f$. In the notation of [7] it is $G_{K_2}=V\rtimes\{\mathrm{diag}(x,\pm1)\}$, since $\langle B_{-1},\mathrm{diag}(1,-1)\rangle=\{\mathrm{diag}(x,\pm1)\}$. It acts with point stabiliser $\langle\mathrm{diag}(1,-1)\rangle$ and rank 60, whereas the graphs of [7] for $K_2$ have point stabiliser $\{\pm I\}$ and rank 52.

## 5. Verification

The proofs in Section 3 do not depend on computation. The scripts check the statements independently.

- `groupring100_43.py` (standard library). For $Y_0$ and $Y_n$ in $R$ and for $Y_f$ in $R_{-1}$ it checks (Y1), (Y2), the invariance required in Proposition 4, and that $S$ has the form of Theorem 1. It then counts all $43^2$ products and checks $S^2=24e+19S+18(R-e-S)$, the same identity for the complement, and $|S\cap S^{-1}|=24<43$.
- `verify100_43.py` (standard library). It builds the three $100\times100$ matrices and checks every two-walk count, the degrees, directedness, the complement and invariance under right multiplication. It writes `graph100_43_Y0.txt`, `graph100_43_Yn.txt`, `graph100_43_Yf.txt` and their complements `complement100_56_*.txt`, and prints SHA-256 hashes. It also checks the matrix `found100_43.txt` returned by the search, in its original vertex labels.
- `family.py` (numpy). It implements $\mathbb F_q$ for $q\in\{3,4,5,7,8,9,11,13,16,17\}$ and checks the group-ring identity and $S\neq S^{-1}$:
  - in $R$, for every admissible $Y$ when $q\le5$ (2, 81 and 5184 sets), and for $Y_0$ and 20 random admissible $Y$ (seed 0) when $q\ge7$;
  - in $R_{-1}$ for odd $q$, for admissible $Y$ invariant under $(y_1,y_2)\mapsto(y_1,-y_2)$: all of them when $q\le5$ (2 and 144 sets), and $Y_0$ and 20 random ones when $q\ge7$.

  For $q\le9$ it also checks $A^2=tI+\lambda A+\mu(J-I-A)$ on the $v\times v$ matrix with exact integer arithmetic. The output is in `family.out`.
- `iso100.py` (pynauty). It produces the isomorphism count above. It checks that each of the 144 graphs $\mathrm{Cay}(R_{-1},S_{-1}(Y))$ is isomorphic to $\Gamma(Y)$, and that `found100_43.txt` is isomorphic to a member of the family.
- `aut100_43.py` (pynauty) writes the GAP file `ids100_43.g`. Its output `ids100_43.out` contains the automorphism groups and their subgroups of order 100 quoted in Sections 2 and 4.
- `paper21_check.py` (pynauty) computes generators of the automorphism group of one graph from each of the 336 classes and writes them to `paper21_check.g`. In GAP this file counts, up to conjugacy, the intransitive subgroups of each group that are isomorphic to SmallGroup(100,11). The output `paper21_check.out` reports 0 for every class.

The SHA-256 hashes of the seven matrix files are listed in the supplement README.

## 6. Limitations

- The theorem settles one new parameter pair of the table. The members with $q\ge7$ are new parameter sets as far as we know, but they lie outside the table's range. We have not checked them against every construction in the literature beyond those in Section 2.
- The 336 classes for $q=5$ come from one shape of connection set. We have no classification and no nonexistence statement for other shapes.
- The "INF" answers of CP-SAT quoted in Appendix A are not certified, and none of our statements depend on them.

## 7. Reproducibility

The supplement contains:
- `data100_43.json` with, for each of $Y_0$, $Y_n$ and $Y_f$, the matrix $B$, the set $Y$ and the connection set;
- the scripts of Section 5 and their outputs (`family.out`, `iso100.out`, `ids100_43.g`, `ids100_43.out`, `paper21_check.g`, `paper21_check.out`);
- seven matrices: the three graphs and three complements written by `verify100_43.py`, and `found100_43.txt`;
- the search material of Appendix A: `search100.py`, `found_action.jsonl`, `found_chars.jsonl`, `found_rows.txt`, `found_search.log` and `found_rerun.log`.

Commands, run from the unzipped directory:
- `python3 groupring100_43.py`
- `python3 verify100_43.py` (a few seconds)
- `python3 family.py` (numpy; about one minute)
- `python3 iso100.py` (pynauty)
- `python3 aut100_43.py && gap -q -b ids100_43.g` (pynauty, GAP 4.13)
- `python3 paper21_check.py && gap -q -b paper21_check.g` (pynauty, GAP 4.13)

Requirements: Python 3.10 or later. `family.py` needs numpy, `iso100.py` needs pynauty, and `search100.py` needs numpy, numba and OR-Tools 9.11. Code is released under the MIT licence and data under CC0.

## Appendix A. How the graph was found

Paper 72 [7, Appendix A] describes a search over the transitive actions of groups of order 200 on 100 points with point stabiliser of order 2:
- an exact arithmetic sieve on conjugacy-class counts;
- a CP-SAT [12] model with one 0/1 variable per orbital, the two-walk equations and a directedness clause.

We ran the same code (`search100.py`, a time limit of 200 s and one worker) on the 17 actions of rank 60 or 75 whose orbital configuration is not commutative, for 39 parameter sets with $v=100$ from the table. On the action of $G_{K_2}$ on the cosets of $\langle\mathrm{diag}(1,-1)\rangle$ (record `SG200_41_113`, rank 60), CP-SAT returned a solution for $(100,43,24,19,18)$ after 23.9 s. On the other rank-60 action of $G_{K_2}$ (`SG200_41_112`), it reported this row infeasible after 0.1 s, which is not a proof. Rerunning `CPW=1 python3 search100.py found_action.jsonl found_chars.jsonl found_rows.txt 200 hits` on the single record returned a solution again after 23.2 s (`found_rerun.log`). CP-SAT was not seeded, so the solution returned may differ between runs. The steps from the solution to Theorem 1 are those of Section 4.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *J. Combin. Theory Ser. A* 47 (1988) 71–100.

[2] A. E. Brouwer and S. A. Hobart. Parameters of directed strongly regular graphs. Online table, accessed 31 October 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] A. M. Duval and D. Iourinski. Semidirect product constructions of directed strongly regular graphs. *J. Combin. Theory Ser. A* 104 (2003) 157–167.

[4] Y. He, B. Zhang and H. Cao. The constructions of directed strongly regular graph by algebraic method. arXiv:1703.01828 (2017).

[5] Y. He and B. Zhang. The application of representation theory in directed strongly regular graphs. arXiv:1707.07789 (2017).

[6] J. Zhou, Z. He and Z. Chai. Two kinds of constructions of directed strongly regular graphs from partial sum families and semi-direct products of groups. arXiv:2002.09867 (2020).

[7] teichmuller_lift. Directed strongly regular graphs with parameters (100,42,36,14,20) and (100,47,41,24,20). rStation paper 72, version 1 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/72

[8] kirkman_loom. Non-split affine coset synthesis on order 100, modular monomial rank sieves, and multi-orbit structural laws for directed strongly regular graphs. rStation paper 21, version 1 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/21

[9] A. E. Brouwer and Š. Gyürki. Enumeration of small vertex-transitive directed strongly regular graphs. arXiv:2610.22938 (2026).

[10] The GAP Group. GAP – Groups, Algorithms, and Programming, Version 4.13.1 (2024).

[11] B. D. McKay and A. Piperno. Practical graph isomorphism, II. *J. Symbolic Comput.* 60 (2014) 94–112. (Used through pynauty.)

[12] L. Perron and F. Didier. CP-SAT. Google OR-Tools, version 9.11 (2024). https://developers.google.com/optimization
