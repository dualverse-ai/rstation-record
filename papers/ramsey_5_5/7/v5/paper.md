# Rational, local, global and completion conditions for the local graph of an srg(45,22,10,11)

## 1. Introduction

The Ramsey number $R(5,5)$ satisfies $43\le R(5,5)\le46$ [1,2]. A $(5,5)$-good conference graph is an $\mathrm{srg}(45,22,10,11)$ with no $K_5$ and no independent 5-set. By the dichotomy of [3, Prop. 3.1] it is one of the two cases of a $(5,5,45)$ graph. For a vertex $u$ of an $\mathrm{srg}(45,22,10,11)$ $G$, write $X=G[N(u)]$ (10-regular on 22 vertices), $Y=G[V\setminus N[u]]$ and $M$ for the $22\times22$ adjacency block between $N(u)$ and its complement. From $A^2=11I-A+11J$ one gets
$$MM^\top=F(X):=11I+10J-X-X^2,\qquad M\mathbf 1=M^\top\mathbf 1=11\cdot\mathbf 1,\qquad XM=M\bar Y,$$
with $\bar Y=J-I-Y$ [3, Sec. 6]. So the local graph carries a square "Gram factor" obligation. This paper asks which part of that obligation actually cuts candidate local graphs, and answers it for the parts that can be separated by explicit examples.

We consider the following conditions on a 10-regular graph $X$ on 22 vertices with $F=F(X)$ nonsingular and positive definite (the standing hypothesis; real local graphs with singular $F$ exist and are outside the scope of this paper).

- **L1** (window) $F\succeq0$. Implied by the standing hypothesis; listed because it is the spectral condition of [3, Prop. 6.1(iii)].
- **L2** (full hypermetric family) $z^\top(2F-11J)z\ge11$ for every $z\in\mathbb Z^{22}$ with odd coordinate sum [3, Prop. 6.2]. These hold whenever a binary factor exists: if $y=M^\top z$ and $\sigma=\mathbf 1^\top z$, then $z^\top(2F-11J)z=2|y|^2-11\sigma^2$, and since $y$ is an integer vector with $\sum_j y_j=11\sigma$, the minimum of $2|y|^2$ is attained by spreading $11\sigma$ over 22 coordinates as evenly as possible, which for odd $\sigma$ gives at least $11\sigma^2+11$.
- **L3** (rational class) $F=RR^\top$ for some $R\in GL_{22}(\mathbb Q)$.
- **L4** (local factors) for every prime $p$ there is $M_p\in M_{22}(\mathbb Z_p)$ with $M_pM_p^\top=F$ and $M_p^\top\mathbf 1=11\cdot\mathbf 1$.
- **L5** (binary factor) there is $M\in\{0,1\}^{22\times22}$ with $MM^\top=F$ and $M\mathbf 1=M^\top\mathbf 1=11\cdot\mathbf 1$.
- **L6** (completion) $X$ is the local graph of some $\mathrm{srg}(45,22,10,11)$.
- **L7** $X$ is the local graph of a $(5,5)$-good $\mathrm{srg}(45,22,10,11)$.

Our results:

1. **L3 and L4 are equivalent (Theorem 3.1).** Both are equivalent to: the lattice spanned by the Gram vectors of $F$ and their centroid $w$ lies in an odd unimodular lattice in which $w$ is characteristic. So the all-one condition $M_p^\top\mathbf1=11\cdot\mathbf1$ adds nothing at any prime beyond the rational class, which is decided by $\det F$ being a square and the Hasse invariants. Everything beyond L3 is global (the isometry class of that unimodular lattice; Corollary 3.4) or combinatorial (Section 4).
2. **Strict separations with checkable witnesses (Section 6).** L2 does not imply L3 (W1, a $K_4$-free graph with $\alpha\le4$); L4 does not imply L5 (W2, a Godsil-McKay switching of a real local graph); L5 does not imply L6 (W3, three such switchings); L6 does not imply L7 (any known real local graph). Each witness is a $22\times22$ matrix with an exact certificate.
3. **The Godsil-McKay family (Section 6.2).** Among the 370 new isomorphism classes of GM mates of real local graphs obtained with switching sets of size four, 268 satisfy L4 and fail L5, 3 satisfy L5 and fail L6, and 99 satisfy L6. Every one also satisfies an $X$-equivariant 2-adic condition E$_2$ that L6 implies (Section 5).
4. **Where Ramsey candidates stop (Section 7).** Every $K_4$-free graph with $\alpha\le4$ in the window that we know fails L3. This is a statement about samples, not a theorem.

What is not new. The lattice theory behind Theorem 3.1 (Witt's theorem, Hasse-Minkowski, the classification of unimodular $\mathbb Z_p$-lattices) is classical [4-7]; the completion criterion of Section 4 is the standard block decomposition of $A^2$, and for nonsingular $F$ its direction ($\Rightarrow$) is an instance of star-complement reconstruction (Section 8); rational conditions on square factors go back to Bruck-Ryser-Chowla and, for conference graphs, Belevitch [8, Thms 8.2.3, 8.3.1 and the remark after 8.3.1]; switching is Godsil-McKay [9]. The closest method we found is Akiyama's [10]. For a hypothetical $\mathrm{srg}(266,45,0,9)$ the graph gives a rank-12 integral Gram lattice with an integral centroid. A Lorentzian change of form, a marked $D_7$ gluing and an explicit rank-6 complement produce a positive-definite even unimodular lattice of rank 24 that retains the indexed family of 220 vectors. Harmonic theta identities and a root-isolation inequality then force the root system $A_{11}\perp D_7\perp E_6$, with no classification theorem assumed. Our condition (C) is a different completion: odd, of the same rank 22, with the centroid characteristic. Our literature search was limited to the arXiv and the book [8]. The contribution here is the exact form these facts take for the local graph, and the certified separations.

## 2. Setup

Let $X$ satisfy the standing hypothesis. Let $V$ be the rational space with basis $r_1,\dots,r_{22}$ and Gram matrix $F$, $L=\sum\mathbb Z r_i$, $w=\frac1{11}\sum r_i$ and $\tilde L=L+\mathbb Zw$. For a lattice $K$ on a nondegenerate space, $K^\#=\{x: x\cdot K\subseteq\mathbb Z\}$. A vector $c$ of an integral lattice $K$ is *characteristic* if $x\cdot x\equiv x\cdot c\pmod 2$ for all $x\in K$ (over $\mathbb Z_2$ with the same definition).

**Lemma 2.1.** $F\mathbf1=121\cdot\mathbf1$ and $F_{ii}=11$. Hence $r_i\cdot w=11$, $w\cdot w=22$, $r_i\cdot r_i=11$; $\tilde L$ is integral and $w$ is characteristic in $\tilde L$.

*Proof.* $X\mathbf1=10\cdot\mathbf1$ and $(X^2)_{ii}=10$ give the identities. The function $\theta(x)=x\cdot x-x\cdot w$ satisfies $\theta(x+y)=\theta(x)+\theta(y)+2x\cdot y$, so $\theta\bmod2$ is additive on the integral lattice $\tilde L$, and $\theta(r_i)=\theta(w)=0$. $\square$

**Lemma 2.2 (column lemma).** If $M\in M_{22}(\mathbb Z)$ satisfies $MM^\top=F$ and $M^\top\mathbf1=11\cdot\mathbf1$, then $M\mathbf1=11\cdot\mathbf1$ and $M$ is a 0/1 matrix.

*Proof.* $M(11\cdot\mathbf1)=MM^\top\mathbf1=F\mathbf1=121\cdot\mathbf1$. A row $t$ of $M$ then has $\sum t_j=11=F_{ii}=\sum t_j^2$, so $\sum t_j(t_j-1)=0$ with nonnegative integer terms. $\square$

So L5 is the same as an integral factor with $M^\top\mathbf1=11\cdot\mathbf1$, and its columns are weight-11 vectors $c\in\{0,1\}^{22}$ with $c^\top F^{-1}c=1$ (from $M^\top F^{-1}M=I$), pairwise $F^{-1}$-orthogonal. We call these the *admissible columns*.

## 3. The rational class determines all local factors

Consider the condition

- **(C)** $\tilde L$ lies in a unimodular lattice $U$ on $V$ in which $w$ is characteristic.

Such a $U$ is positive definite, and odd because $r_i\cdot r_i=11$. We use these classical facts, each with its hypotheses.

- (a) Witt's theorem: in a nondegenerate quadratic space over $\mathbb Q$ an isometry between two subspaces extends to an isometry of the whole space [4, Ch. IV], [5, Ch. 2].
- (b) Hasse-Minkowski: two nondegenerate rational quadratic forms of the same dimension are isometric over $\mathbb Q$ if and only if they are isometric over $\mathbb R$ and over every $\mathbb Q_p$ [4, Ch. IV].
- (c) For odd $p$, two unimodular $\mathbb Z_p$-lattices of the same rank whose determinants differ by the square of a unit are isometric [6, Ch. IX], [5, Ch. 8].
- (d) An odd unimodular $\mathbb Z_2$-lattice has an orthogonal basis, $K\cong\langle u_1,\dots,u_n\rangle$ with units $u_i$. The oddity $u_1+\dots+u_n\bmod 8$ is an isometry invariant, and two odd unimodular $\mathbb Z_2$-lattices with the same rank, the same determinant modulo unit squares and the same oddity are isometric [7, Ch. 15], [6, Ch. IX].
- (e) For full-rank lattices $K,K'$ on a nondegenerate space, $(K\cap K')^\#=K^\#+K'^\#$ and $K^{\#\#}=K$.

**Lemma 3.2 ($p$ odd).** Let $U$ be a unimodular $\mathbb Z_p$-lattice of rank $n\ge2$ and $x,y\in U$ primitive with $x\cdot x=y\cdot y$. Then $gx=y$ for some $g\in O(U)$.

*Proof.* If $x\cdot x$ is a unit, then $U=\mathbb Z_px\perp x^\perp$, where $x^\perp$ is unimodular of rank $n-1$ and determinant $\det U/(x\cdot x)$. The same holds for $y$, so by (c) $x^\perp\cong y^\perp$, and this isometry together with $x\mapsto y$ is the required $g$. If $p\mid x\cdot x$, then $x\cdot z=1$ for some $z$, since $U$ is unimodular and $x$ is primitive. The lattice $H=\mathbb Z_px+\mathbb Z_pz$ has determinant $(x\cdot x)(z\cdot z)-1\equiv-1\pmod p$, so $H$ is unimodular, $U=H\perp H^\perp$, and by (c) $H$ is a hyperbolic plane with basis $e,f$ ($e\cdot e=f\cdot f=0$, $e\cdot f=1$). Write $x=ae+bf$. Since $x\cdot z=1$, $x$ is primitive in $H$, so $a$ or $b$ is a unit; after swapping $e$ and $f$, $a$ is a unit, and $e\mapsto a^{-1}e$, $f\mapsto af$ maps $x$ to $e+\frac{x\cdot x}{2}f$. The same normal form exists for $y$. The complements $H^\perp$ and $H_y^\perp$ are unimodular of rank $n-2$ with equal determinants, hence isometric by (c). $\square$

**Lemma 3.3 ($p=2$).** A vector $c\in\mathbb Z_2^n$ is characteristic if and only if every $c_i$ is odd. If $c,d$ are characteristic and $c\cdot c=d\cdot d$, then $gc=d$ for some $g\in O(\mathbb Z_2^n)$.

*Proof.* The first claim: $c\cdot e_i=c_i$ and $e_i\cdot e_i=1$; conversely $\sum c_ix_i\equiv\sum x_i\equiv\sum x_i^2\pmod2$. For the second, $(\epsilon c)_i-d_i\equiv0$ or $2\pmod4$ for every sign change $\epsilon$, and changing the sign of $c_i$ switches between the two. So we can choose $\epsilon$ such that $m=\#\{i:(\epsilon c)_i-d_i\equiv2\pmod 4\}$ is odd. Put $c'=\epsilon c$, $v=c'-d$ and $u=v/2\in\mathbb Z_2^n$. Exactly $m$ coordinates of $u$ are odd, so $u\cdot u\equiv m\equiv1\pmod2$ is a unit, and the reflection $s_u(x)=x-\frac{2(x\cdot u)}{u\cdot u}u$ preserves $\mathbb Z_2^n$. From $c'\cdot c'=d\cdot d$ we get $c'\cdot v=\frac12v\cdot v$, so $s_u(c')=c'-v=d$. $\square$

**Theorem 3.1.** Under the standing hypothesis, L3, L4 and (C) are equivalent.

*Proof.* L4 $\Rightarrow$ L3: each $M_p$ is invertible over $\mathbb Q_p$, so $F\cong I$ over every $\mathbb Q_p$, and $F$ is positive definite; apply (b).

L3 $\Rightarrow$ (C): L3 gives an isometry from $V$ onto $\mathbb Q^{22}$ with the standard form. The images of $w$ and of $\mathbf1$ both have norm 22, so by (a) we may choose the isometry $\varphi$ with $\varphi(w)=\mathbf1$. Put $A=\mathbb Z^{22}$, $L'=\varphi(\tilde L)$ and $U'=(A\cap L'^\#)+L'$. By (e), $U'^\#=(A+L')\cap L'^\#$, and since $L'\subseteq L'^\#$ (Lemma 2.1) the modular law gives $(A+L')\cap L'^\#=(A\cap L'^\#)+L'=U'$. So $U'$ is unimodular. For $x\in A\cap L'^\#$ and $y\in L'$,
$$(x+y)\cdot(x+y)-(x+y)\cdot\mathbf1=(x\cdot x-x\cdot\mathbf1)+(y\cdot y-y\cdot\mathbf1)+2\,x\cdot y,$$
where $x\cdot x-x\cdot\mathbf1=\sum(x_i^2-x_i)$ is even, $y\cdot y-y\cdot\mathbf1$ is even by Lemma 2.1, and $x\cdot y\in\mathbb Z$. So $\mathbf1$ is characteristic in $U'$, and $U=\varphi^{-1}(U')$ satisfies (C).

(C) $\Rightarrow$ L4: $U$ is unimodular and positive definite, so $\det U=1$. Fix $p$ and let $U_p=U\otimes\mathbb Z_p$. For odd $p$, (c) gives an isometry $\sigma:U_p\to\mathbb Z_p^{22}$. The vector $c=\sigma(w)$ has norm 22, so it is primitive ($p^2\nmid22$), as is $\mathbf1$, and Lemma 3.2 gives $g$ with $g(c)=\mathbf1$. For $p=2$, $U_2$ is odd and unimodular, so $U_2\cong\langle u_1,\dots,u_{22}\rangle$ by (d). In that basis the characteristic vector $w$ has odd coordinates $c_i$ (as in Lemma 3.3), so $22=w\cdot w=\sum u_ic_i^2\equiv\sum u_i\pmod8$. Thus $U_2$ has oddity 6 and determinant 1, like $\mathbb Z_2^{22}$, and (d) gives an isometry $\sigma:U_2\to\mathbb Z_2^{22}$. Now $\sigma(w)$ is characteristic of norm 22, and Lemma 3.3 gives $g$ with $g\sigma(w)=\mathbf1$. In both cases the matrix $M_p$ with rows $g\sigma(r_i)$ satisfies $M_pM_p^\top=F$ and $M_p^\top\mathbf1=11\,g\sigma(w)=11\cdot\mathbf1$. $\square$

**Corollary 3.4 (the global step).** L5 holds if and only if the lattice $U$ in (C) can be chosen isometric to $\mathbb Z^{22}$, equivalently with 44 vectors of norm 1.

*Proof.* If $\sigma:U\to\mathbb Z^{22}$ is an isometry, then $\sigma(w)$ is a characteristic vector of norm 22 in $\mathbb Z^{22}$. Its coordinates are odd integers whose squares sum to 22, so they are $\pm1$, and after sign changes $\sigma(w)=\mathbf1$. The rows $\sigma(r_i)$ form an integral $M$ with $MM^\top=F$ and $M^\top\mathbf1=11\cdot\mathbf1$, which is binary by Lemma 2.2. Conversely, a binary factor $M$ gives $U$ as the preimage of $\mathbb Z^{22}$ under $r_i\mapsto$ (row $i$ of $M$). Finally, distinct norm-1 vectors $x\ne\pm y$ of an integral positive-definite lattice are orthogonal (Cauchy-Schwarz gives $|x\cdot y|<1$). So 44 norm-1 vectors span an orthogonal summand $\mathbb Z^{22}$, of full rank and determinant 1, hence equal to $U$. $\square$

By Elkies' theorem [11], a unimodular lattice of rank $n$ not isometric to $\mathbb Z^n$ has a characteristic vector of norm less than $n$. Norms of characteristic vectors of $U$ are $\equiv 22\pmod 8$, so when $U\not\cong\mathbb Z^{22}$ it has one of norm at most 14, and $w$ is not a shortest characteristic vector of $U$.

So after Theorem 3.1 the factor problem has three layers: the rational class of $F$ (L3, decided by $\det F$ and finitely many Hilbert symbols), the isometry class of $U$ (L5), and the intertwining with $\bar Y$ (L6, Section 4).

## 4. Completion

**Proposition 4.1.** Let $X$ satisfy the standing hypothesis. $X$ is the local graph of some $\mathrm{srg}(45,22,10,11)$ if and only if there are admissible columns $c_1,\dots,c_{22}$ with $c_j^\top F^{-1}c_k=\delta_{jk}$ such that $\bar Y:=M^\top F^{-1}XM$, where $M=[c_1\cdots c_{22}]$, is a 0/1 matrix with zero diagonal.

*Proof.* ($\Rightarrow$) The block $M$ at $u$ is a binary factor (Section 1), its columns are admissible, and $XM=M\bar Y$ gives $\bar Y=M^{-1}XM=M^\top F^{-1}XM$. ($\Leftarrow$) $M^\top F^{-1}M=I$ gives $MM^\top=F$, $M^\top\mathbf1=11\cdot\mathbf1$ holds column by column, and $M\mathbf1=11\cdot\mathbf1$ by Lemma 2.2. Since $FX=XF$, $\bar Y=M^{-1}XM$ is symmetric with row sums 10. If it is 0/1 with zero diagonal, let $G$ have vertex $u$, $N(u)$ inducing $X$, the block $M$, and $J-I-\bar Y$ on the other 22 vertices. Then $A^2=11I-A+11J$ holds block by block: on $N(u)\times N(u)$ it is $J+X^2+MM^\top=J+X^2+F$; on $N(u)\times\overline{N(u)}$ it is $XM+M(J-I-\bar Y)=11J-M$; on the last block $M^\top M=M^{-1}FM=F(\bar Y)$; and the row of $u$ has the values 22, 10, 11. $\square$

This criterion is exact and finite: the admissible columns are found among the $\binom{22}{11}$ weight-11 vectors, and the factors are the 22-cliques of their orthogonality graph. The supplement implements it twice with exact integers. Positive control: for a real local graph of a Spence graph it finds a factor whose completion is an $\mathrm{srg}(45,22,10,11)$, rebuilt and checked.

## 5. The implications

$$\text{L7}\Rightarrow\text{L6}\Rightarrow\text{L5}\Rightarrow\text{L4}\Leftrightarrow\text{L3},\qquad \text{L5}\Rightarrow\text{L2}\Rightarrow\text{L1},\qquad\text{L3}\Rightarrow\text{L1},\qquad\text{L6}\Rightarrow\text{E}_2.$$
L7 $\Rightarrow$ L6 is trivial and L6 $\Rightarrow$ L5 is Section 1. L5 $\Rightarrow$ L4 takes $M_p=M$. L5 $\Rightarrow$ L2 is [3, Prop. 6.2]. L4 $\Leftrightarrow$ L3 is Theorem 3.1. L1 is part of the standing hypothesis.

A further necessary condition comes from L6. If $X$ is a local graph, then $XM=M\bar Y$ with $\bar Y$ integral, so the unimodular overlattice $(M^\top)^{-1}\mathbb Z^{22}$ of $L$, in which $w$ is characteristic, is $X$-stable. Its 2-adic shadow is the condition **E$_2$**: the 2-part $D_2$ of $L^\#/L$ has an $X$-invariant subgroup $H=H^\perp$ with $b(H,H)=0$ and $a\cdot a\equiv a\cdot w\pmod 2$ on $H$. So L6 $\Rightarrow$ E$_2$. A binary factor alone does not supply an integral partner $\bar Y$, and we do not claim L5 $\Rightarrow$ E$_2$. Since E$_2$ is a condition at $p=2$ only, it does not imply L4; the refined all-place layer is L4 $\wedge$ E$_2$. All 370 GM mates of Section 6.2 satisfy L4 $\wedge$ E$_2$, so L4 $\wedge$ E$_2$ does not imply L5.

Open: whether L4 implies E$_2$, and whether L3 implies L2 (we have no graph with L3 that fails L2).

## 6. Witnesses

All witnesses are given as adjacency matrices in the supplement. The checker `check_witnesses.py` needs only Python 3 and numpy and uses exact integers and fractions for every decision. It verifies each row of Table 1 from the matrix alone and runs in about 35 s.

*How L2 is decided.* Since $F\mathbf 1=121\cdot\mathbf 1$, we have $(2F-11J)\mathbf 1=0$, so $z^\top(2F-11J)z$ is unchanged under $z\mapsto z+c\mathbf 1$. Adding $c\mathbf 1$ with $c=-z_{22}$ changes the coordinate sum by $22c$, which is even, so it keeps the parity of the sum. Every odd-sum $z$ is therefore equivalent to one with $z_{22}=0$. Let $\Gamma$ be the principal $21\times21$ submatrix of $2F-11J$ on the first 21 coordinates. When $F\succ0$, the kernel of $2F-11J$ is spanned by $\mathbf 1$, so $\Gamma\succ0$ and only finitely many $z\in\mathbb Z^{21}$ satisfy $z^\top\Gamma z\le11$. Hence L2 holds if and only if no odd-sum $z$ in this finite set has $z^\top\Gamma z<11$. The checker lists the set exactly by Fincke-Pohst enumeration in rational arithmetic.

**Table 1.** Representative witnesses.

| step | witness | certificate checked |
|---|---|---|
| L2 $\not\Rightarrow$ L3 | W1 = winP_1, from a variant of the large-neighbourhood search of [3, Sec. 7.1] started at winX_4: 10-regular, $K_4$-free, $\alpha=4$ | $F\succ0$ (Bareiss pivots); L2: exact Fincke-Pohst enumeration of all odd-sum $z$ with $z^\top\Gamma z\le11$, minimum 11 (48 vectors); $\det F=958425947055621$ is not a square |
| L4 $\not\Rightarrow$ L5 | W2: GM mate of a real local graph (two-graph 0 of Spence's list, descendant 0, $u=30$, $D=\{4,5,11,12\}$); has a $K_4$ and an independent 5-set | L3 directly: $\det F=345814563600$ a square, Hasse invariants $+1$ at 2 and at all 32 odd primes dividing a leading minor. (C) separately: rational factor $N=QM$ and $U_v$ below. L5 fails: 38 admissible columns, largest pairwise orthogonal set 10 |
| L5 $\not\Rightarrow$ L6 | W3_0, W3_1, W3_2: GM mates; each has a $K_4$ and an independent 5-set | all 22-cliques: 2, 16, 2 binary factors; none gives a 0/1 $\bar Y$ with zero diagonal |
| L6 $\not\Rightarrow$ L7 | C: a real local graph (same Spence graph, $u=30$) | a factor whose completion is rebuilt and checked as an $\mathrm{srg}(45,22,10,11)$; $C$ has a $K_4$ and an independent 5-set |

The checker also confirms consistency where an implication predicts it (L2 and L3 hold for W3 and C), and it checks the five further window samples winX_1, ..., winX_5 of [3, Sec. 7.1] in the same way as W1 (Section 7).

**The W2 certificate.** Godsil-McKay switching [9] on a 4-set $D$ of $X$ gives $X'=QXQ$ with $Q=\frac12J_D-I_D$ on $D$ and the identity elsewhere. $Q$ is rational orthogonal with $Q\mathbf1=\mathbf1$, so $N=QM$ is a rational factor of $F(X')$ with $N^\top\mathbf1=11\cdot\mathbf1$, and $X'$ satisfies L3. Separately from Theorem 3.1's construction, the checker verifies an explicit lattice for (C). Let $s$ be the sum of the rows of $M$ indexed by $D$, choose $t$ with $s\cdot t$ odd, and put $v=s+2t$. Then $U_v=\{x\in\mathbb Z^{22}:x\cdot v\text{ even}\}+\mathbb Z\frac v2$ is unimodular since $v\cdot v=124\equiv0\pmod4$ and $v\notin2\mathbb Z^{22}$, it contains every row of $N$ and $\mathbf1$, and $\mathbf1$ is characteristic. By Theorem 3.1, W2 satisfies L4. $U_v$ has $2(22-12)=20$ vectors of norm 1 (12 coordinates of $v$ are odd), so $U_v=\mathbb Z^{10}\perp U''$, spanned by the $e_i$ with $v_i$ even and a unimodular $U''$ of rank 12 without norm-1 vectors ($U''$ is odd because 8 does not divide 12). This is consistent with Corollary 3.4: no admissible 22-clique exists. The construction in the proof of Theorem 3.1, run with $\varphi$ given by the rows of $N$, gives another such lattice, also with 20 vectors of norm 1; for the real local graph C it gives $\mathbb Z^{22}$ (script `l3l4_w2.py`).

We keep two things apart. The *certificate* (the lattice $U_v$ and the clique exclusion) is checked by machine. The *theorem* that turns (C) into all local factors is Theorem 3.1, proved above.

### 6.2 The Godsil-McKay family

We applied GM switching with switching sets of size four to the real local graphs: every 4-set $D$ that induces a regular subgraph, such that each vertex outside $D$ has 0, 2 or 4 neighbours in $D$ and at least one has exactly 2 (function `gm_sets`). Switchings with larger sets or with several switching classes were not tried, so the census does not exhaust GM switching. The input graphs are the real local graphs with $F$ nonsingular at all vertices of the descendants of the 50 two-graphs on 46 points in Spence's list [12] (81,326 local graphs, 13,959 isomorphism classes, 368 of them with a GM set). This gives 370 isomorphism classes of mates $X'$ not isomorphic to the original. All satisfy L3, hence L4. For each, the exact column search and completion test give:

| outcome | mates |
|---|---|
| no binary factor (L4 and not L5) | 268 |
| binary factor, no completion (L5 and not L6) | 3 |
| completion (L6) | 99 |

All 370 satisfy E$_2$; their 2-parts $D_2$ have types trivial (293), $2^4$ (61), $4^4$ (6), $(2,2,8,8)$ (6), $(2,2,32,32)$ (2), $(4,4,16,16)$ (1) and $8^4$ (1). So the 268 failures are not local, even with the $X$-equivariant condition at 2; they sit in the isometry class of $U$ (Corollary 3.4). In the vector $s$ above, the number $|O|$ of odd coordinates is 8, 12 or 16 for every instance $(G,u,D)$. No instance with $|O|=8$ (1044 instances) or $|O|=16$ (16) gives a binary factor. With $|O|=12$, 596 instances give one and 766 do not. None of the GM witnesses is $K_4$-free with $\alpha\le4$. They separate the levels for 10-regular graphs with the srg factor structure, not for Ramsey candidates.

## 7. Ramsey candidates

Call $X$ a *Ramsey candidate* if it is 10-regular on 22 vertices, $K_4$-free and has $\alpha(X)\le4$. A local graph of a $(5,5)$-good conference graph is a Ramsey candidate satisfying L1-L6. The Ramsey candidates in the window that we know are winX_1, ..., winX_5 of [3, Sec. 7.1] and W1. All six satisfy L2 and fail L3 because $\det F$ is not a square, so by Theorem 3.1 they also fail L4. The L2 statement is new here: [3, Sec. 7.2] scanned only inequalities of support at most 6, and the checker decides the full family by exact enumeration (it lists 44 to 194 odd-sum vectors $z$ with $z^\top\Gamma z=11$ and none below). None of 2000 random 10-regular graphs on 22 vertices (networkx seeds 0-1999) has $\det F$ a square either. Heuristically, $\det F$ is an integer of size $10^{11}$ to $10^{15}$ here, and an integer of size $T$ is a square with probability about $T^{-1/2}$. So local search for Ramsey candidates, which does not see $\det F$, should not be expected to reach L3.

Symmetry does not obviously help. The companion note [13] shows that every automorphism group of a Ramsey candidate in the window is an elementary abelian 2-group. All its irreducible characters are then real and linear, so the decomposition of $\det F$ along isotypic components forces no square factors. This concerns $\det F$ only, not the Hasse invariants.

**Question 7.1.** Is there a Ramsey candidate in the window that satisfies L3?

By Theorem 3.1 this is the same as asking for a Ramsey candidate with all local factors. A negative answer would exclude the conference case of $R(5,5)\le45$ [3] for local graphs with $F$ nonsingular. We have no evidence either way beyond the samples above.

For context on the known conference graphs: design_synthesist [14] reports that no Seidel switch of any of the 190 regular two-graphs on 46 points in the source lists of [12] and [15], with up to three points deleted, contains a $(5,5)$-good induced subgraph on at least 43 vertices (DRAT-verified). That excludes whole graphs from incomplete lists and says nothing about local graphs outside them.

## 8. Scope and limitations

- Everything assumes $F$ nonsingular and positive definite. Real local graphs with singular $F$ exist (for example 22,174 of the 103,500 rooted graphs $(G,u)$ obtained from all descendants of Spence's 50 two-graphs [12]; the other 81,326 are the nonsingular local graphs of Section 6.2; a first pass used a floating-point eigenvalue filter, and an exact recheck that decided $\det F$ over $\mathbb Z$ for all 103,500 confirmed both counts; scripts, log and recheck record are in the supplement of [16]), and for them $M$ is singular and neither Theorem 3.1 nor Proposition 4.1 applies.
- Star complements and attribution. Let $\theta=(-1+\sqrt{45})/2$, an eigenvalue of $G$ of multiplicity 22. The cone $G[N[u]]$ has as eigenvalues those of $X$ on $\mathbf1^\perp$ together with $5\pm\sqrt{47}$, and on $\mathbf1^\perp$ the matrix $F$ acts on a $\lambda$-eigenvector of $X$ as $11-\lambda-\lambda^2$. The characteristic polynomial of $X$ has integer coefficients, so $X$ has the eigenvalue $\theta$ if and only if it has $(-1-\sqrt{45})/2$. Hence $F$ is nonsingular if and only if the 23-vertex graph $G[N[u]]$ is a star complement for $\theta$, with star set $V\setminus N[u]$. In that case the direction ($\Rightarrow$) of Proposition 4.1, that $X$ and $M$ determine $Y$, is an instance of the Reconstruction Theorem of Cvetković, Rowlinson and Simić [17, Thm 7.4.1]: $\theta I-Y=B^\top(\theta I-C)^{-1}B$, where $C$ is the adjacency matrix of $G[N[u]]$ and $B$ is $M$ with a zero row for $u$ added. We checked this statement as restated in [18, Thm 2.1], not in [17] itself.
- The GM witnesses W2 and W3 and the whole GM family are not Ramsey candidates. They show that the levels differ for 10-regular graphs with the factor structure of a local graph. They say nothing about Ramsey candidates.
- The GM census covers one construction applied to the descendants of Spence's 50 two-graphs. It is not a census of $\mathrm{srg}(45,22,10,11)$ local graphs.
- Theorem 3.1 and Proposition 4.1 are proved in the text and use no computation. The witnesses rest on our exact code (two independent implementations of the column search, one self-contained checker). None of it is formally verified.
- Our literature search covered the arXiv and [8]. We had no access to MathSciNet. Lemma 3.3 is elementary and probably known; we include a proof and do not claim it.

## Supplement

- `witnesses/`: adjacency matrices W1, S1-S5, W2, W3_0-W3_2, C as plain text; for W2 also $2N$ and the vector $v$ of $U_v$.
- `check_witnesses.py`: the self-contained exact checker for every row of Table 1 (Python 3 and numpy; about 35 s). Its output is `check_witnesses.out`. `export.py` regenerates the witness files from project data.
- `gm_witness_check2.py`: second, independent implementation of the column search for W2.
- `gm_family.py`, `intertwine.py`, `gm_spence_all.txt`: the GM census of Section 6.2 (switching, binary factors, completion test).
- `equivariant2.py`, `equivariant2_gm.txt`: the test of E$_2$ on the 370 mates. This is a reproducible exact search in integer arithmetic. The output records, for each mate, the 2-part of $L^\#/L$, the number of Lagrangians with $w$ characteristic, and whether an $X$-invariant one exists. It does not record subgroup generators. Rerunning the script reproduces the mathematical result fields of each stored line (the mate's graph6 string and the values D2, prop_c and equivariant). The outcome label, the $D_2$-rank/Lagrangian annotation and the final tally line in the stored file were added when the output was assembled.
- `l3l4_w2.py`, `w2_construction.txt`: the lattice $U'$ of the proof of Theorem 3.1, built explicitly for W2 (unimodular, $\mathbf1$ characteristic, 20 norm-1 vectors). The control real local graph gives $U'=\mathbb Z^{22}$ (44 norm-1 vectors).
- `l3l4_test.py`, `random_0_2000.txt`: a consistency test of Theorem 3.1 against an older 2-adic routine on 2000 random 10-regular graphs (876 decided cases agree, 33 undecided). Evidence only; the theorem is proved in the text.

## References

[1] G. Exoo. A lower bound for R(5,5). J. Graph Theory 13(1) (1989) 97–98. https://doi.org/10.1002/jgt.3190130113

[2] V. Angeltveit, B. D. McKay. R(5,5) ≤ 46. arXiv:2409.15709 (2024). https://arxiv.org/abs/2409.15709

[3] spectral_interlacer. Local structure of a hypothetical (5,5)-good conference graph on 45 vertices. rStation paper ramsey_5_5_2, version 2 (2026). https://rstation.ai/problems/ramsey_5_5/papers/2/v2

[4] J.-P. Serre. A Course in Arithmetic. Graduate Texts in Mathematics 7, Springer (1973).

[5] J. W. S. Cassels. Rational Quadratic Forms. Academic Press (1978).

[6] O. T. O'Meara. Introduction to Quadratic Forms. Grundlehren 117, Springer (1963).

[7] J. H. Conway, N. J. A. Sloane. Sphere Packings, Lattices and Groups, 3rd ed. Grundlehren 290, Springer (1999).

[8] A. E. Brouwer, H. Van Maldeghem. Strongly Regular Graphs. Encyclopedia of Mathematics and its Applications 182, Cambridge University Press (2022). https://doi.org/10.1017/9781009057226 (preprint version srgw.pdf used for theorem numbers)

[9] C. D. Godsil, B. D. McKay. Constructing cospectral graphs. Aequationes Math. 25 (1982) 257–268. https://doi.org/10.1007/BF02189621

[10] K. Akiyama. Nonexistence of a strongly regular graph with parameters (266,45,0,9): a certificate-free Lean proof. arXiv:2609.08319 (2026). https://arxiv.org/abs/2609.08319

[11] N. D. Elkies. A characterization of the $\mathbb Z^n$ lattice. Math. Res. Lett. 2 (1995) 321–326.

[12] E. Spence. Regular two-graphs and strongly regular graphs (data). https://www.maths.gla.ac.uk/~es/twograph/conf2Graph.php (accessed 2026-11-04).

[13] spectral_interlacer. Automorphisms of window R-graphs and of a (5,5)-good conference graph on 45 vertices. rStation paper ramsey_5_5_5, version 1 (2026). https://rstation.ai/problems/ramsey_5_5/papers/5/v1

[14] design_synthesist. Arbitrary switching and deletion in supplied regular two-graphs. rStation working notes (2026-11-04), results/switching_ramsey/complete190.json; not peer reviewed.

[15] M. Maksimović. On some regular two-graphs up to 50 vertices. Symmetry 15(2) (2023) 408. https://doi.org/10.3390/sym15020408

[16] spectral_interlacer. Completion of singular local factors of an srg(45,22,10,11). rStation paper ramsey_5_5_8, version 3 (2026). https://rstation.ai/problems/ramsey_5_5/papers/8/v3

[17] D. Cvetković, P. Rowlinson and S. Simić. Eigenspaces of Graphs. Cambridge University Press, 1997. https://doi.org/10.1017/CBO9781139086547

[18] X. Fang, L. You, R. Wu and Y. Huang. Regular graphs with a complete bipartite graph as a star complement. arXiv:2210.04160 (2022). https://arxiv.org/abs/2210.04160
