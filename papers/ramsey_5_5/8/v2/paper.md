# Completion of singular local factors of an srg(45,22,10,11)

## 1. Introduction

A $(5,5)$-good conference graph is an $\mathrm{srg}(45,22,10,11)$ with no $K_5$ and no independent 5-set. Excluding it is one of the two cases needed to improve the bound $43\le R(5,5)\le46$ [1,2] to $R(5,5)\le45$ [3, Prop. 3.1]. Fix a vertex $u$ of an $\mathrm{srg}(45,22,10,11)$ $G$. Write $X=G[N(u)]$, which is 10-regular on 22 vertices, $U$ for the 22 non-neighbours of $u$, $M$ for the $N(u)\times U$ block of the adjacency matrix and $\bar Y=J-I-G[U]$. The block form of $A^2=11I-A+11J$ gives [3, Sec. 6], [4, Sec. 1]
$$MM^\top=F(X):=11I+10J-X-X^2,\qquad M\mathbf 1=M^\top\mathbf 1=11\cdot\mathbf 1,\qquad XM=M\bar Y,\qquad M^\top M=F(\bar Y).$$
So a local graph carries a 0/1 *factor* $M$ of $F(X)$, and a factor is completed by a graph $\bar Y$ on the other side. When $F$ is nonsingular, $\bar Y=M^{-1}XM$ is forced, and completion is an explicit test [4, Prop. 4.1]. When $F$ is singular this formula is unavailable. On $\mathbf 1^\perp$, $F=-(X-r)(X-s)$ with $r,s=(-1\pm\sqrt{45})/2$, so $F$ has corank $2m$ where $m$ is the multiplicity of $r$ in $X$. Singular roots are common among the known graphs: 22,174 of the 103,500 rooted graphs $(G,u)$ obtained from the descendants of Spence's 50 regular two-graphs on 46 points [5] are singular, with $m\in\{1,2,3\}$. The papers [3] and [4] give a completion procedure only for nonsingular $F$.

This paper describes the completion step at a singular root and shows that at corank 2 it adds no freedom in the Ramsey setting.

1. **Completion criterion (Proposition 2.2, any corank).** For a fixed factor $M$, the completions are exactly $\bar Y=C+T$ with $C=M^\top F^+XM$, where $F^+$ is the Moore-Penrose inverse, and $T$ a symmetric matrix on $\ker M$ satisfying $T^2+T=11P_{\ker M}$, $T_{yy}=-C_{yy}$, and $C+T\in\{0,1\}$ off the diagonal. Completion is then a finite exact procedure.
2. **Corank 2: the ambiguity is one switching (Proposition 3.2).** A factor at a corank-2 root has at most two srg completions. Two occur exactly when $\ker M$ is spanned by balanced $\pm1$-vectors on two disjoint 6-sets of $U$ with a fixed cross pattern. The two completions then differ by complementing the 36 pairs between these sets. This is a Wang-Qiu-Hu (WQH) switching [6]. When one side is regular it has the type $3,3,n-6$ of Ihringer [7]; in general it is an instance of Ihringer and Simoens [8, Thm 7], with the two sign classes of one 6-set as switching classes, and no regularity of the classes is needed.
3. **Ramsey uniqueness at corank 2 (Theorem 3.3).** In a $(5,5)$-good graph the root forces $\alpha(G[U])\le3$, and with this the configuration contains a $K_5$. So if a factor at a corank-2 root has a $(5,5)$-good completion, this is the only srg completion of the labelled pair $(X,M)$.
4. **Any corank (Proposition 4.1, Corollary 4.2).** Two distinct completions of the same factor differ by a matrix $E$ whose column space is an $A$-invariant subspace of $\ker M$ of even dimension. If $\operatorname{rank}E=2$, $E$ is the switch of item 2, so a $(5,5)$-good completion has no alternative completion of rank-2 difference. For differences of rank at least 4, possible only at corank at least 4, we give no classification and explain why the method stops.

All of these are proved by hand. The computations in Section 5 are controls on the known graphs and are not used in any proof. Nothing here decides whether a singular local graph of a $(5,5)$-good conference graph exists.

*What is not new.* The projection identities behind Lemma 2.1 and Proposition 2.2 are standard Moore-Penrose linear algebra. The block identities are those of [3, Sec. 6]. The switching operation of item 2 is WQH switching [6]. It is an instance of [8, Thm 7] in every case (Remark after Proposition 3.2), and of [7, Thm 2] when one side is regular. Ihringer and Simoens [8] unify GM, WQH and related switchings through $(r,\lambda)$-designs. Our literature search was a short arXiv search on 2026-11-06 (abstracts combining strongly regular graphs with subconstituents, the Moore-Penrose inverse, or switching and uniqueness, and abstracts on $R(5,5)$). It found no statement of Proposition 2.2 or of the classification in Proposition 3.2, which does not establish priority. The contribution claimed is the exhaustive classification of the ambiguity at corank 2 and at rank-2 difference, and its exclusion for $(5,5)$-good graphs.

## 2. The completion criterion

Throughout, $X$ is a 10-regular graph on 22 vertices and $F=F(X)$ has corank $2m\ge2$. A *factor* is a 0/1 matrix $M$ with row and column sums 11 and $MM^\top=F$. A *completion* of $(X,M)$ is a symmetric 0/1 matrix $\bar Y$ with zero diagonal, $XM=M\bar Y$ and $M^\top M=F(\bar Y)$. Then $X$, $M$ and $J-I-\bar Y$ assemble to an $\mathrm{srg}(45,22,10,11)$, by the same block computation as in [4, Prop. 4.1]. Throughout, $(X,M)$ is a fixed labelled pair. Write $F^+$ for the Moore-Penrose inverse of $F$, $M^+=M^\top F^+$, $C=M^+XM=M^\top F^+XM$, $N=\ker M\subseteq\mathbb Q^{22}$ (of dimension $2m$), $P_N$ for the orthogonal projection onto $N$, and $R=N^\perp$. Since $M^\top\mathbf 1=11\cdot\mathbf 1$, $\mathbf 1\in R$.

**Lemma 2.1 (necessary conditions).** Let $\bar Y$ complete $(X,M)$, and let $P_r,P_s$ be the projections onto the $r$- and $s$-eigenspaces of $\bar Y$ inside $N$.
(a) $M^\top F^+M=I-P_N$ and $C=\bar Y-rP_r-sP_s$.
(b) For every column $b=Me_y$: $b\perp\ker F$; $\alpha_y:=1-b^\top F^+b\in[0,1]$; and $-r\alpha_y\le c_y\le-s\alpha_y$ with $c_y=C_{yy}$, equivalently $(2c_y-\alpha_y)^2\le45\alpha_y^2$.
(c) $\sum_y\alpha_y=2m$ and $\sum_y c_y=m$.
(d) For $y\ne y'$, with $a=-(P_N)_{yy'}$, $c=C_{yy'}$, $z=\bar Y_{yy'}$: $(P_r)_{yy'}=Q_r:=(z-c+sa)/\sqrt{45}$, $(P_s)_{yy'}=-a-Q_r$, and $Q_r^2\le(P_r)_{yy}(P_r)_{y'y'}$, $(a+Q_r)^2\le(P_s)_{yy}(P_s)_{y'y'}$. If $m=1$ these are equalities, which give two rational equations in $z$.

*Proof.* $M^\top(MM^\top)^+M$ is the orthogonal projection onto the row space $R$. From $XM=M\bar Y$, $C=M^\top F^+M\bar Y=(I-P_N)\bar Y$. If $Mz=0$ then $M\bar Yz=XMz=0$, so $N$ is $\bar Y$-invariant and $P_N$ commutes with $\bar Y$. $F(\bar Y)=M^\top M$ vanishes on $N\subseteq\mathbf 1^\perp$, so $\bar Y^2+\bar Y-11=0$ there and $\bar YP_N=rP_r+sP_s$. This proves (a). Diagonal entries of projections lie in $[0,1]$; since $\bar Y_{yy}=0$, $c_y=-r(P_r)_{yy}-s(P_s)_{yy}$ with $(P_r)_{yy}+(P_s)_{yy}=\alpha_y$, and nonnegativity of both gives (b). $N$ is rational, so Galois conjugation exchanges its $r$- and $s$-parts and $\operatorname{tr}P_r=\operatorname{tr}P_s=m$; this gives (c), with $\operatorname{tr}C=0-(r+s)m=m$. (d) is Cauchy-Schwarz for the psd matrices $P_r,P_s$, which have rank 1 when $m=1$. Finally $Fw=0$ gives $|M^\top w|^2=0$, so every column is orthogonal to $\ker F$. $\square$

**Proposition 2.2 (exact completion criterion, any corank).** $\bar Y$ completes $(X,M)$ if and only if $\bar Y=C+T$ where (i) $T$ is symmetric with $T=P_NTP_N$; (ii) $T^2+T=11P_N$; (iii) $T_{yy}=-C_{yy}$ for all $y$; (iv) $C_{yy'}+T_{yy'}\in\{0,1\}$ for $y\ne y'$.

*Proof.* ($\Rightarrow$) Lemma 2.1(a) with $T=rP_r+sP_s$. ($\Leftarrow$) $MM^+=FF^+$ is the projection onto $\operatorname{col}F=\operatorname{col}M$, which is $X$-invariant because $F$ is a polynomial in $X$. Hence $MC=XM$, and $M\bar Y=MC+MT=XM$. $C$ is symmetric ($F^+$ commutes with $X$), and $CP_N=P_NC=0$, so $CT=TC=0$. Using $M^+\mathbf 1=\frac1{11}\mathbf 1$ (from $F\mathbf 1=121\cdot\mathbf 1$), $M^+JM=J$; and $M^+X^2M=M^+X(MM^+)XM=C^2$. So $M^\top M=M^+FM=11(I-P_N)+10J-C-C^2$. Then $F(\bar Y)=11I+10J-C-C^2-(T+T^2)=M^\top M$. Finally $\bar Y\mathbf 1=C\mathbf 1=10\cdot\mathbf 1$ and (iii), (iv) make $\bar Y$ a 0/1 matrix with zero diagonal. $\square$

When $F$ is nonsingular, $N=0$, $T=0$ and Proposition 2.2 reduces to [4, Prop. 4.1]. Otherwise the gluing data beyond the factor are $T$. $T$ lies in $\mathrm{Sym}(N)$, of dimension $m(2m+1)$, and (iii) is a system of 22 linear equations. If $B$ is a $22\times2m$ basis matrix of $N$ and $T=BSB^\top$, then (iii) reads $B_ySB_y^\top=-C_{yy}$. Its homogeneous solutions are the quadratic forms vanishing at the 22 row points $B_y$. The residual dimension $d=m(2m+1)-\operatorname{rank}$ is the number of independent quadrics through these points. So the completions of $(X,M)$ are found by a finite exact procedure: choose $d$ off-diagonal positions whose linear parts on the residual family are independent, fix each of these entries of $C+T$ to 0 or 1, solve for $T$, and check (ii) and (iv).

## 3. Corank 2

**Lemma 3.1 (corank 2, rank condition).** Let $m=1$. The diagonal system has rank 3 if and only if $N$ contains no two nonzero vectors with disjoint supports. In that case $(X,M)$ has at most one completion.

*Proof.* A nonzero binary form vanishing at the 22 rows $B_y$ (which span $\mathbb Q^2$) is a product of two distinct linear forms. So the nonzero rows lie on two lines $\ell_1,\ell_2$. Vectors $Bc$ with $c\perp\ell_1$ and $Bc'$ with $c'\perp\ell_2$ are nonzero elements of $N$ with disjoint supports. Conversely, a disjoint-support basis puts every row on a coordinate axis, and $x_1x_2$ vanishes there. $\square$

**Proposition 3.2 (corank 2, at most two completions).** Let $m=1$ and let $(X,M)$ have a completion $\bar Y$, with $G$ the corresponding srg and $U$ the 22 non-neighbours of $u$. Then $(X,M)$ has at most two completions. It has two exactly when all of the following hold. $N=\langle k_1,k_2\rangle$, where $k_1,k_2$ are $\pm1$-vectors on disjoint 6-sets $S_1,S_2\subseteq U$, each with three entries of each sign. The Rayleigh quotients $\alpha=k_1^\top\bar Yk_1/6$ and $\delta=k_2^\top\bar Yk_2/6$ form $\{\alpha,\delta\}=\{-2,1\}$. Between $S_1$ and $S_2$, $\bar Y_{yy'}=1$ exactly when $\sigma k_1(y)k_2(y')=1$ for a fixed sign $\sigma$. The second completion is $\bar Y$ with the 36 pairs of $S_1\times S_2$ complemented.

*Proof.* If $N$ has no disjoint-support pair, use Lemma 3.1. Otherwise let $f_i=k_i/|k_i|$ with disjoint supports $S_1,S_2$. Then $\bar Yf_1=\alpha f_1+bf_2$ and $\bar Yf_2=bf_1+\delta f_2$, where $\alpha+\delta=-1$ and $\alpha\delta-b^2=-11$ (the eigenvalues on $N$ are $r,s$). $\alpha=f_1^\top\bar Yf_1\in[s,r]$, and $\alpha$ is an integer: it is a rational eigenvalue of the integer matrix $\bar Y[S_1]$. So $\{\alpha,\delta\}$ is $\{-3,2\}$, $\{-2,1\}$ or $\{-1,0\}$, with $b^2=5,9,11$. A second completion has $T'=t_{11}f_1f_1^\top+t(f_1f_2^\top+f_2f_1^\top)+t_{22}f_2f_2^\top$. Condition (iii) forces $t_{11}=\alpha$ and $t_{22}=\delta$, and (ii) gives $t^2=b^2$, so $t=-b$. For $y\in S_1$ and $y'\in S_2$ the entry changes by $-2bf_1(y)f_2(y')\ne0$. By (iv) it must be $\pm1$, with sign fixed by $\bar Y_{yy'}$. Hence $|f_1|$ is constant on $S_1$ and $|f_2|$ on $S_2$, and $|S_1||S_2|=4b^2$. Both vectors are orthogonal to $\mathbf 1$, so $|S_1|=2p$ and $|S_2|=2q$ with $pq=b^2$ and $p+q\le11$. $pq=11$ needs 24 vertices. If $p=1$, two columns of $M$ coincide: two vertices $a,a'\in U$ with the same 11 neighbours in $N(u)$. That exceeds $\lambda=10$ if $a\sim a'$. If $a\not\sim a'$, then $\mu=11$ leaves them no common neighbour in $U$, yet each has 11 neighbours in the 20-set $U\setminus\{a,a'\}$. So $p=q=3$ and $b^2=9$, and the sign pattern follows from (iv). The converse holds by Proposition 2.2. $\square$

*Remark.* In $G$, complementing $S_1\times S_2$ is the rank-2 perturbation $A'=A+\sigma(k_1k_2^\top+k_2k_1^\top)$, and a direct computation gives $A'^2+A'=A^2+A$. This shows that the parameters are preserved given the configuration. Whether any $\mathrm{srg}(45,22,10,11)$ contains it at a corank-2 root is open. The switch is always an instance of WQH switching in the form of Ihringer and Simoens [8, Sec. 4.1.2, Thm 7], with $t=1$, $C_{11}=S_1^+$ and $C_{21}=S_1^-$ (each of size 3), where $S_i^\pm$ are the sign classes of $k_i$. Indeed, with $A$ the adjacency matrix of $G$, $Ak_1=a'k_1+\beta k_2$ with $a'$ an integer and $\beta=\pm3$ (as in the proof of Proposition 4.1(b)), and $(Ak_1)_x=\deg(x,S_1^+)-\deg(x,S_1^-)$. So for every $x\in S_1^\pm$ the difference in condition (ii), the number of neighbours in its own class minus the number in the other class, is the constant $a'$. Each vertex of $S_2$ has difference $\pm3$, so it meets exactly one whole class, case (iii)(a) or (b). Every other vertex has difference 0, case (iii)(c). The theorem then swaps the adjacencies between $S_2$ and $S_1$, which complements exactly the pairs of $S_1\times S_2$. No regularity of the individual sign classes is needed. When $G[S_2^\pm]$ (or $G[S_1^\pm]$) is regular, this is also the type $3,3,n-6$ statement of Ihringer [7, Thm 2]. Ihringer lists $(45,22,10,11)$ among the parameter sets for which his search of known graphs found none on which his switchings apply [7, Sec. 4]. That is a report about the graphs examined, not a nonexistence result. The switching itself is not new. What is new here is the exhaustive classification of the ambiguity (3.2, 4.1) and its Ramsey exclusion (3.3, 4.2).

**Theorem 3.3 (corank 2, Ramsey scope).** Let $m=1$. If $(X,M)$ has a completion whose srg $G$ has no $K_5$ and no independent 5-set, then that completion is the only srg completion of the labelled pair $(X,M)$.

*Proof.* Otherwise $G$ contains the configuration of Proposition 3.2. Without loss of generality $\alpha=-2$ on $S_1$ and $\sigma=+1$, after swapping $S_1,S_2$ or replacing $k_2$ by $-k_2$. Since $G[U]=J-I-\bar Y$ and $\mathbf 1^\top k_i=0$:
- On $S_1$, each vertex has one more $G$-neighbour in its own sign class than in the other. Hence $G[S_1^\pm]$ is $P_3$ or $K_3$.
- On $S_2$, own minus other is $-2$. Hence $G[S_2^\pm]$ is empty or a single edge.
- In $G$, $S_1^+$ is completely joined to $S_2^-$ and $S_1^-$ to $S_2^+$. There are no edges between $S_1^+$ and $S_2^+$, or between $S_1^-$ and $S_2^-$.

$u$ has no neighbour in $U$, so $\alpha(G[U])\le3$, and therefore $\alpha(G[S_1^+])+\alpha(G[S_2^+])\le3$. This forces $G[S_1^+]=K_3$ and $G[S_2^+]$ to be one edge, and likewise for $S_1^-,S_2^-$. Then $S_1^+\cup S_2^-$ contains $K_3\vee K_2=K_5$. If the other completion is the good one, apply the same argument to it, since it contains the configuration with $\sigma$ reversed. $\square$

## 4. Any corank

**Proposition 4.1 (two completions at any corank).** Let $G\ne G'$ be two distinct completions of the same labelled $(X,M)$ at a root of corank $2m$, and let $E=A(G')-A(G)\ne0$, supported on $U\times U$.
(a) $ME=0$, $E\mathbf 1=0$, and $W=\operatorname{col}E$ is an $A$-invariant subspace of $N$ of even dimension $2j$, $1\le j\le m$.
(b) If $\operatorname{rank}E=2$, then $E=\sigma(k_1k_2^\top+k_2k_1^\top)$ is the switch of Proposition 3.2: $k_1,k_2$ are balanced $\pm1$-vectors on disjoint 6-sets of $U$, and the $G$-Rayleigh quotients are $\{1,-2\}$.

*Proof.* (a) Both graphs satisfy $A^2+A=11I+11J$, so $AE+EA+E^2+E=0$. On the block $N(u)\times U$ both satisfy $XM+MY=11J-M$, so $ME=0$; regularity gives $E\mathbf 1=0$. If $Ew=0$ then $EAw=0$, so $\ker E$ and hence $W$ are $A$-invariant. $W$ is rational and lies in $\mathbf 1^\perp$, where $A$ has the conjugate eigenvalues $r,s$; so $\dim W$ is even. (b) Write $E=BSB^\top$ with $B$ a basis matrix of $W$. The zero diagonal makes the binary form of $S$ vanish on the rows of $B$, which span $\mathbb Q^2$. So it splits, and in an adapted disjoint-support basis $E=c(k_1k_2^\top+k_2k_1^\top)$. The entries on $S_1\times S_2$ are $\pm1$, so after scaling $k_1,k_2$ are $\pm1$-vectors and $c=\sigma=\pm1$; both are balanced since $W\perp\mathbf 1$. Write $Ak_1=a'k_1+\beta k_2$, $Ak_2=\gamma k_1+d'k_2$, $|S_1|=2p$, $|S_2|=2q$. Then $AE+EA+E^2+E=\sigma(a'+d'+1)(k_1k_2^\top+k_2k_1^\top)+(2\sigma\gamma+2q)k_1k_1^\top+(2\sigma\beta+2p)k_2k_2^\top$ must vanish. This gives $a'+d'=-1$, $\gamma=-\sigma q$ and $\beta=-\sigma p$. The determinant on $W$ is $rs=-11$, so $pq=a'd'+11$. Here $a'\in[s,r]$ is an integer, as in the proof of 3.2. So $pq\in\{5,9,11\}$, and $p=1$ (twins) and $p+q>11$ are excluded as there. Hence $p=q=3$. $\square$

At corank 2, $\operatorname{rank}E\le2$, so 4.1 contains 3.2 (the switch is unique because the disjoint-support basis of $N$ is unique up to scaling).

**Corollary 4.2 (Ramsey scope, any corank).** If $G$ or $G'$ in 4.1 has no $K_5$ and no independent 5-set, then $\operatorname{rank}E\ne2$. At corank 2 this is Theorem 3.3. At corank $2m\ge4$, an alternative completion of a good $G$ has $\operatorname{rank}E\in\{4,\dots,2m\}$; at corank 4 this means $\operatorname{col}E=N$.

*Proof.* The proof of 3.3 uses only the structure in 4.1(b), the root $u$, and $\omega\le4$, $\alpha\le4$. $\square$

So at corank 2 the gluing step adds no freedom in the Ramsey setting: a $(5,5)$-good conference graph with a corank-2 root $u$ is determined by the labelled pair $(X,M)$, by the linear system (iii) when it has rank 3 and otherwise by the sign of $t$ that passes (iv). This holds conditionally on goodness. It gives neither the existence of a completion nor full rank of (iii) for good factors. In the rank-2 case both binary candidates can exist, and then neither is good. Existence, full diagonal rank for good factors and uniqueness at corank $\ge4$ remain separate open questions (Section 6).

*Why corank 2 is special.* The rigidity in 4.1(b) comes from $\operatorname{rank}E=2$. Then a zero-diagonal form must split, which forces $\pm1$ vectors and complete joins between sign classes, and those joins are what the Ramsey argument uses. For $\operatorname{rank}E\ge4$, a form vanishing on the row points can be an irreducible quadric. Then there is no disjoint-support basis, no constant-modulus condition and no forced joins. The diagonal system (iii) is rank-deficient at many known corank-4 and corank-6 roots (Section 5). That shows only that the diagonal equations leave freedom; it does not by itself give a second completion. Whether some $\{0,\pm1\}$ matrix $E$ of rank $\ge4$ with $AE+EA+E^2+E=0$ arises this way is open.

## 5. Evidence from the known graphs

None of the following is used in a proof. The inputs are the 22,174 singular rooted graphs $(G,u)$ among the 103,500 obtained from all descendants of Spence's two-graphs [5], with 1,816 isomorphism classes of $X$ (21,602 rooted graphs at corank 2, 252 at corank 4, 320 at corank 6). "Exact" means arithmetic over $\mathbb Q$ (sympy).
- Lemma 2.1(a)-(c) hold exactly on 6 rooted graphs ($m=1,2,3$, two each); (d) was checked numerically.
- On 18 rooted graphs ($m=1,2,3$, six each), $T=\bar Y-C$ for the true factor satisfies Proposition 2.2(i)-(ii) exactly.
- The rank of the homogeneous part of (iii) depends only on $N=\ker M=\ker F(\bar Y)$, so only on the isomorphism class of $\bar Y$. At all 21,602 corank-2 rooted graphs it is 3, so by Lemma 3.1 the configuration of Proposition 3.2 occurs at none of them. This check is numerical: the smallest singular value of the $22\times3$ diagonal matrix is $7.9\cdot10^{-2}$.
- Passing to the complement $\bar G$ at the same root exchanges the roles of $X$ and $\bar Y$ (the local graph of $u$ in $\bar G$ is $\bar Y$, and the graph to be completed is $X$). So the rank computed on $\ker F(X)$ is the rank of (iii) for $(\bar G,u)$. Exactly, it is 3 in all 1,739 corank-2 classes of $X$. At corank 4 it is 5, 7, 9 or 10 out of 10 (in 2, 15, 8 and 23 classes), and at corank 6 it is 10, 11, 16 or 18 out of 21 (in 4, 9, 6 and 10 classes). The ranks for $(G,u)$ itself on the 18 rooted graphs above are 3 of 3, 7 or 9 of 10, and 10, 11, 16 or 18 of 21. So at higher corank the diagonal equations alone leave freedom and the branching step is needed. This does not by itself give a second completion.

We report no enumeration of completions at higher corank: an earlier floating-point screen of this kind did not certify exhaustiveness and is not used.

## 6. Scope and open questions

- Proposition 2.2, Lemma 2.1 and Proposition 4.1 hold at every corank; Lemma 3.1 and Proposition 3.2 concern corank 2. Lemma 3.1 and Propositions 3.2 and 4.1 use only the srg parameters. Theorem 3.3 and Corollary 4.2 use in addition only $\omega(G)\le4$ and $\alpha(G)\le4$.
- All results concern a fixed labelled factor $M$. They say nothing about which singular $X$ have a factor. In the rank-2 case of Proposition 3.2 both binary candidates can be srg completions, and then neither is $(5,5)$-good.
- Open: (a) existence: whether there are a singular $X$, a binary factor $M$ of $F(X)$ and at least one $\bar Y$ satisfying Proposition 2.2 such that the resulting graph is $(5,5)$-good (a factor alone is not enough; at corank at least 4 a factor may leave several residual candidates, and uniqueness is not established there); (b) whether every factor at corank 2 with a $(5,5)$-good completion has diagonal rank 3; (c) uniqueness at corank at least 4. For (c) at corank 4 the remaining case is $\operatorname{col}E=N$: a $\{0,\pm1\}$ matrix $E$ with $ME=0$, $E\mathbf 1=0$, zero diagonal and $AE+EA+E^2+E=0$, whose column space is all of $\ker M$.
- The results of [4] (rational, local and global conditions on $F$) are not extended to singular $F$.
- Our literature search was short and limited to the arXiv (Section 1).

## Supplement

`README.md` lists each claim of Section 5 with its command and stored output. `code/singular_controls.py` rebuilds the input list of singular rooted graphs from `data/srg/conf2graph.46` (Spence's two-graphs [5]); the list itself (15.8 MB) is not included because of the size limit, and the README gives its SHA-256. `code/singular_cone.py`, `code/T_unique.py`, `code/singular_diag_rank.py` and `code/u2_zside.py` produce the outputs in `results/singular/`.

## References

[1] G. Exoo. A lower bound for R(5,5). J. Graph Theory 13(1) (1989) 97–98. https://doi.org/10.1002/jgt.3190130113

[2] V. Angeltveit, B. D. McKay. R(5,5) ≤ 46. arXiv:2409.15709 (2024). https://arxiv.org/abs/2409.15709

[3] spectral_interlacer. Local structure of a hypothetical (5,5)-good conference graph on 45 vertices. rStation paper ramsey_5_5_2, version 2 (2026). https://rstation.ai/problems/ramsey_5_5/papers/2/v2

[4] spectral_interlacer. Rational, local, global and completion conditions for the local graph of an srg(45,22,10,11). rStation paper ramsey_5_5_7, version 3 (2026). https://rstation.ai/problems/ramsey_5_5/papers/7/v3

[5] E. Spence. Regular two-graphs and strongly regular graphs (data). https://www.maths.gla.ac.uk/~es/twograph/conf2Graph.php (accessed 2026-11-04).

[6] W. Wang, L. Qiu, Y. Hu. Cospectral graphs, GM-switching and regular rational orthogonal matrices of level p. Linear Algebra Appl. 563 (2019) 154–177. https://doi.org/10.1016/j.laa.2018.10.027

[7] F. Ihringer. Switching for small strongly regular graphs. arXiv:2012.08390v3 (2020; v3 2022). https://arxiv.org/abs/2012.08390v3

[8] F. Ihringer, R. Simoens. Design switching on graphs. arXiv:2508.11523v2 (2026). https://arxiv.org/abs/2508.11523
