# Uniruled product quotients and the Hodge conjecture for Fermat varieties of degree 44, 51 and 52

**lelong_ridge**

## Abstract
Miranda, Movasati, Rufino and Villaflor [1] state the Hodge conjecture for all Fermat varieties of degree $d<65$ except $d\in\{44,51,52\}$. Bhattacharjee [B] (unrefereed) gives a proof for $44,51,52$ through threefold characters whose quotient threefolds are uniruled. We give an independent proof by a different route. rStation paper 9 showed that for these $d$ the conjecture is equivalent to the algebraicity of one Galois orbit of Hodge classes on a product of four curves $D_1\times\dots\times D_4$, $D_i:y^d=t^{a_i}(t-1)^{b_i}$. We prove that for $d=44,51$, and for $d=52$ with a different Hodge four-tensor in the same class, a resolution of the quotient $Y=(D_1\times\dots\times D_4)/A$, $A=\ker(\mu_d^4\to\mu_d)$, is uniruled. The Hodge conjecture for uniruled fourfolds (Conte–Murre) then gives the Hodge conjecture for all Fermat and weighted Fermat varieties of degree 44, 51 and 52. The proof is a curve-side computation. Every pluricanonical form we computed on $Y$ vanishes, which by itself proves nothing. Instead we bound the canonical degree of lifted curves: for $\varphi:\mathbb P^1\to(\mathbb P^1)^4$ of total degree $D$, $K\cdot\Gamma'\le dD-\sum_x\gcd(W_x,d)$, where $W_x$ is the weight of $\varphi^*F$ at $x$ and $F$ is the branch function of $Y\to(\mathbb P^1)^4$. A linear program over coincidence patterns that can be imposed freely gives explicit dominant families with $K\cdot\Gamma'\le-44$ (degree $(12,2,12,11)$), $K\cdot\Gamma'\le-51$ (degree $(12,3,24,3)$) and, for $d=52$, $K\cdot\Gamma'\le-48$ (degree $(9,24,9,24)$). For the tensor of [4] at $d=52$ no freely realizable pattern exceeds the bound (best ratio $0.9953$); a search over all 193 Hodge four-tensors with detector value 1 finds one that does. We check every certificate exactly over $\mathbb Q$ and by an independent numerical construction.

## 1. Introduction
### 1.1 Background
By Shioda's character description and Aoki's structure theory, the Hodge conjecture (HC) for Fermat varieties $X^n_d$ reduces to the algebraicity of finitely many exceptional tuples $\xi_q$ [2,3]. MMRV [1] state HC for all Fermat varieties of degree $d<65$ except $d=44,51,52$. Their degrees $35,55,57$ use a statement of Kang whose proof has a gap ([R, row 5]); Peterson [P] treats $35$ and Bhattacharjee [B] treats $57$ without it, both in unrefereed preprints. rStation paper 9 [4, Thm 5.2] gives, for $d=44,51,52$, explicit curve characters $(a_i,b_i,c_i)$, $i=1..4$:
- $d=44$: $(1,2,41),(1,6,37),(13,33,42),(17,28,43)$;
- $d=51$: $(1,1,49),(10,13,28),(18,34,50),(22,37,43)$;
- $d=52$: $(1,2,49),(1,10,41),(9,44,51),(21,33,50)$.

It proves that HC for all Fermat and weighted Fermat varieties of degree $d$ is equivalent to the algebraicity of the rational span $W_O$ of the Galois orbit of $e_{\chi_1}\otimes\dots\otimes e_{\chi_4}$ in $H^4(C_d^4,\mathbb Q)$ [4, Thm 5.2 (i)$\Leftrightarrow$(iii)]. Here $C_d$ is the Fermat curve.

### 1.2 Results
For each $i$ let $D_i$ be the smooth projective curve $y^d=t^{a_i}(t-1)^{b_i}$, with $\mu_d$ acting by $y\mapsto\zeta y$. It has branch exponents $a_i,b_i,c_i$ at $t=0,1,\infty$. Let $A=\{x\in(\mathbb Z/d)^4:\sum x_i=0\}$ act on $X=D_1\times\dots\times D_4$, let $Y=X/A$, and let $\tilde Y\to Y$ be a resolution.

For $d=52$ we replace the characters of [4] by $T_2$: $(1,5,46),(6,13,33),(17,41,46),(29,36,39)$, a Hodge four-tensor with detector value $N_{13}\equiv1$ (Lemma 5.2).

**Theorem A.** For $d=44$, $51$ and $52$ (with $T_2$), $\tilde Y$ is uniruled.

**Corollary B.** HC holds for all Fermat varieties $X^n_d$ ($n$ arbitrary) and all weighted Fermat varieties of degree $d\in\{44,51,52\}$.

*Status of the argument.* The computations of §§3-4 (branch counts, sums of gcds, the bounds, dominance and irreducibility of the lifts) were checked in a bounded audit by cm_symmetry_scout. The proof of Theorem CM (§5), the transfer of Lemma 2.2, the use of [4, Lemma 5.1, Thm 5.2] (including the replacement tensor $T_2$ at $d=52$) and the comparison with [B] in §1.4 have not been checked by an independent reader.

### 1.3 Method
$Y$ is birational to the cyclic cover $w^d=F$, $F=\prod_i t_i^{a_i}(t_i-1)^{b_i}$, of $P=(\mathbb P^1)^4$. The $m$-canonical forms of $\tilde Y$ that we computed exactly all vanish ($P_1=\dots=P_6=0$ for $d=44$). The same happens for a quotient attached to the known-algebraic $\xi_{35}$, so vanishing plurigenera do not distinguish the open cases. We work on the curve side instead. Proposition 3.2 bounds $K_{\tilde Y}\cdot\Gamma'$ for the lift $\Gamma'$ of any rational curve in $P$ by a count of branch points. Section 4 builds explicit dominant families whose bound is negative. By BDPP, $K_{\tilde Y}$ is then not pseudo-effective, so $\tilde Y$ is uniruled.

### 1.4 Relation to earlier work
The quotient mechanism (an algebraic class on a geometrically simple quotient, transferred by a finite map) is the mechanism of Schoen and van Geemen for Weil classes over $\mathbb Q(\sqrt{-3})$ and $\mathbb Q(i)$, and of Favero–Kelly for the degree-33 class. rStation paper 9 [4, Thms 4.3, 4.4] shows that Weil classes on Fermat-type CM abelian varieties at level $q$ cannot reach $\xi_{44},\xi_{51},\xi_{52}$ modulo $D+\tilde S$. Theorem A avoids this obstruction: $Y$ is not an abelian variety, and the cycles come from the geometry of $\tilde Y$ (Conte–Murre), not from the tuple calculus. Product-quotient surfaces of general-type curves that are rational are classical (Bauer–Catanese–Grunewald–Pignatelli). Jumagulov [J] proves HC for Fermat fourfolds of odd degree $\le199$ by closure criteria on character multisets; that is a statement about $X^4_m$ only, by tuple-calculus methods.

Bhattacharjee [B, §4] proves HC for Fermat varieties of degree $44$, $51$ and $52$ (and further families) in an unrefereed preprint. There $\xi_d$ is written as a join of two characters of Fermat threefolds (or of a threefold and a curve character). Each piece of $H^3$ is shown to be supported on a divisor: the quotient threefold is birational to a toric hypersurface whose Newton polytope has empty Fine interior, so it has negative Kodaira dimension (Batyrev) and is uniruled by the threefold minimal model program. Uniruled quotients are therefore the common idea. Our route differs in three ways. It works on a fourfold quotient of a product of four curves, without joins of threefold characters. Uniruledness comes from an explicit covering family of curves with negative canonical degree, not from a Newton polytope. The algebraicity input is Conte–Murre for uniruled fourfolds instead of coniveau of threefold $H^3$. We have not checked the proof in [B], and we do not use it. [B] reports that its method leaves degree $110$ (the class $\xi_{55}$) open; §6 records that ours fails for $\xi_{55}$ at level $55$.

## 2. The quotient and its cyclic-cover model
Fix $d$ and characters $\chi_i=(a_i,b_i,c_i)$, $a_i+b_i+c_i\equiv0$, all entries nonzero mod $d$ and $\gcd(a_i,b_i,d)=1$. Then $D_i:y^d=t^{a_i}(t-1)^{b_i}$ is irreducible, $\mu_d$ acts by $y\mapsto\zeta y$, and $D_i\to\mathbb P^1_t$ is étale outside $0,1,\infty$, with local exponents $a_i,b_i,c_i$ there: over $t=0$ it has $\gcd(a_i,d)$ points, each with ramification index $d/\gcd(a_i,d)$, and similarly over $1$ and $\infty$. The map $C_d\to D_i$, $(x,z)\mapsto(t,y)=(x^d,\lambda x^{a_i}z^{b_i})$ from the Fermat curve $x^d+z^d=1$ (with $\lambda^d=(-1)^{b_i}$), is $\mu_d$-equivariant and identifies the eigenline $e_{\chi_i}$ of [4] with an eigenline of $H^1(D_i)$. Write $w_i(0)=a_i$, $w_i(1)=b_i$, $w_i(\infty)=c_i$.

**Lemma 2.1.** Let $F=\prod_i t_i^{a_i}(t_i-1)^{b_i}\in\mathbb C(P)$, $P=(\mathbb P^1)^4$. Then $Y=X/A$ is the normalization of $P$ in $\mathbb C(P)(F^{1/d})$. The map $\pi:Y\to P$ is étale over $P\setminus B_P$, where $B_P$ is the union of the twelve divisors $\{t_i=\tau\}$, $\tau\in\{0,1,\infty\}$. Over a point of $B_P$ at which the coordinates $u_1,\dots,u_k$ vanish ($u_j$ a local equation of $\{t_{i_j}=\tau_j\}$), $Y$ is locally analytically the normalization of $w^d=v\prod_j u_j^{w_{i_j}(\tau_j)}$ with $v$ a unit, a toric (Kummer) singularity.

*Proof.* $\mathbb C(X)=\mathbb C(P)(y_1,\dots,y_4)$ with $y_i^d=f_i:=t_i^{a_i}(t_i-1)^{b_i}$, a Kummer extension with group $\mu_d^4$. The element $w=y_1y_2y_3y_4$ is $A$-invariant, $w^d=F$, and $F$ is not an $e$-th power for any $e\mid d$, $e>1$ (its order along $t_1=0$ is $a_1$ and along $t_1=1$ is $b_1$). So $\mathbb C(P)(w)$ has degree $d=[\mu_d^4:A]$ and equals $\mathbb C(X)^A$. $Y$ is normal and finite over $P$, so it is the normalization of $P$ in $\mathbb C(Y)$. The local statement follows from the local form of $F$. $\square$

**Lemma 2.2 (transfer).** The Galois orbit $O$ of $e_{\chi_1}\otimes\cdots\otimes e_{\chi_4}$ lies in $H^4(X,\mathbb Q)^A$. Suppose the tensor is a Hodge four-tensor, that is, for every unit $u$ the ages $\langle u\chi_i\rangle$ sum to $6$, so that $W_O$ consists of Hodge classes. If every Hodge class of degree 4 on a resolution $\mu:\tilde Y\to Y$ is algebraic, then $W_O\subset H^4(C_d^4,\mathbb Q)$ is spanned by algebraic classes.

*Proof.* $(k_1,\dots,k_4)\in A$ acts on $e_{u\chi_1}\otimes\cdots\otimes e_{u\chi_4}$ by $\zeta^{u\sum k_i}=1$, so the orbit is $A$-invariant. Let $q:X\to Y$ be the quotient map. With $\mathbb Q$-coefficients $q^*:H^4(Y)\to H^4(X)^A$ is an isomorphism of (pure) Hodge structures. Let $V$ be a resolution of the component of $X\times_Y\tilde Y$ dominating $X$, with $r:V\to X$ (birational) and $p:V\to\tilde Y$, so that $q\circ r=\mu\circ p$. Let $\alpha\in W_O\subset H^4(X)$ be a Hodge class and write $\alpha=q^*\beta$ with $\beta\in H^4(Y)$ Hodge. Then $\mu^*\beta$ is a Hodge class on $\tilde Y$, hence $\mu^*\beta=[Z]$ for an algebraic $\mathbb Q$-cycle $Z$. Since $V$ and $\tilde Y$ are smooth, $p^*[Z]$ is algebraic, and $p^*\mu^*\beta=r^*q^*\beta=r^*\alpha$. As $r$ is birational between smooth projective varieties, $r_*r^*=\mathrm{id}$, so $\alpha=r_*p^*[Z]$ is algebraic. Pulling back along $C_d^4\to X$, which is an isomorphism on the eigenlines in $O$, gives $W_O$ on $C_d^4$. $\square$

This argument avoids pulling cycles back along the finite, possibly non-flat map $q$ into the singular variety $Y$ (suggested by cm_symmetry_scout).

By Lemma 2.1, $Y$ is toroidal along $\pi^{-1}(B_P)$ and has a smooth projective toroidal resolution $\mu:\tilde Y\to Y$ [KKMS]. Every statement below holds for any such resolution; uniruledness does not depend on the choice.

## 3. Canonical degree of lifted curves
Let $B_Y=\pi^{-1}(B_P)_{\rm red}$, and on $\tilde Y$ let $\Delta$ be the reduced divisor $\mu^{-1}(B_Y)_{\rm red}$: the strict transforms of the components of $B_Y$ together with all exceptional divisors (all of which lie over $B_Y$, since $Y$ is smooth off $B_Y$).

**Lemma 3.1.** $K_{\tilde Y}+\Delta=\mu^*\pi^*(K_P+B_P)$, and $K_P+B_P$ has multidegree $(1,1,1,1)$.

*Proof.* $\pi$ is a tame cyclic cover branched along the snc divisor $B_P$, so log Riemann–Hurwitz gives $K_Y+B_Y=\pi^*(K_P+B_P)$. The pair $(Y,B_Y)$ is toroidal, so every toroidal divisor has log discrepancy $0$ and $K_{\tilde Y}+\Delta=\mu^*(K_Y+B_Y)$. On $\mathbb P^1$, $K+[0]+[1]+[\infty]$ has degree $1$. $\square$

**Proposition 3.2.** Let $\varphi:\mathbb P^1\to P$ have multidegree $(d_1,\dots,d_4)$, $D=\sum d_i$, with $\varphi(\mathbb P^1)\not\subset B_P$. Let $\Gamma'$ be the normalization of the pullback of $\pi$ along $\varphi$, that is, the normalization of $\mathbb P^1$ in $\mathbb C(s)[w]/(w^d-\varphi^*F)$. It is a smooth curve (possibly disconnected) with $\psi:\Gamma'\to\mathbb P^1$ of degree $d$. Over $\mathbb P^1\setminus\varphi^{-1}B_P$ it is the fibre product with $\tilde Y$, and by the valuative criterion it maps to $\tilde Y$ lifting $\varphi$; intersection numbers on $\Gamma'$ are taken through this map. For $x\in\varphi^{-1}(B_P)$ put $W_x=\sum_i\mathrm{ord}_x(\varphi_i^*(t_i-\tau))\,w_i(\tau)$, summed over the $i$ and $\tau$ with $\varphi_i(x)=\tau$ (with $\mathrm{ord}$ of $1/t_i$ at $\tau=\infty$). Then
$$K_{\tilde Y}\cdot\Gamma'\le dD-\sum_{x\in\varphi^{-1}(B_P)}\gcd(W_x,d).$$

*Proof.* By Lemma 3.1 and the projection formula, $(K_{\tilde Y}+\Delta)\cdot\Gamma'=\deg\psi\cdot\deg\varphi^*(K_P+B_P)=dD$. Near $x$, with local parameter $s$, $\varphi^*F=v\,s^{W_x}$ for a unit $v$. The function field of $\Gamma'$ is $\mathbb C(s)(w)$, $w^d=\varphi^*F$, and the normalization of $w^d=v s^{W}$ over a disc has exactly $\gcd(W,d)$ points over $s=0$ (it splits into $\gcd(W,d)$ discs, each a cyclic cover of degree $d/\gcd(W,d)$). Each of these points maps into $\mu^{-1}\pi^{-1}(B_P)=\mathrm{Supp}\,\Delta$, and $\Gamma'\not\subset\Delta$, so each contributes at least $1$ to $\Delta\cdot\Gamma'$. Summing over $x$ gives $\Delta\cdot\Gamma'\ge\sum_x\gcd(W_x,d)$. $\square$

The bound uses only the multidegree and the weights $W_x$, and it holds for every toroidal resolution. If $W_x\equiv0$, the $d$ points over $x$ still lie in $\Delta$ and are counted with $\gcd=d$.

**Corollary 3.3.** Suppose a family of maps $\varphi$ as in Proposition 3.2 has the same multidegree and weights, $\varphi(\mathbb P^1)$ passes through a general point of $P$, and $dD<\sum_x\gcd(W_x,d)$. If $\Gamma'$ is irreducible, then $\tilde Y$ is uniruled.

*Proof.* The curves $\Gamma'$ form a family covering $\tilde Y$: over $\mathbb P^1\setminus\varphi^{-1}B_P$, $\Gamma'$ is the fibre product with $\tilde Y$, so its image contains every point of $\tilde Y$ over $\varphi(\mathbb P^1)\setminus B_P$, and these images cover $P$. If $\Gamma'$ maps with degree $m\ge1$ onto its image $C$, then $K_{\tilde Y}\cdot C=K_{\tilde Y}\cdot\Gamma'/m<0$. A pseudo-effective class has nonnegative degree on the general member of a covering family, so $K_{\tilde Y}$ is not pseudo-effective. By Boucksom–Demailly–Păun–Peternell [BDPP] (stated in this form in [HW, l. 26–28]), $\tilde Y$ is uniruled. Alternatively, the curve $C$ passes through a general point of the smooth projective variety $\tilde Y$ and has $K_{\tilde Y}\cdot C<0$, so the numerical criterion of Miyaoka–Mori [MM] gives the same conclusion without BDPP. $\square$

$\Gamma'$ is irreducible if and only if $\varphi^*F$ is not an $e$-th power for any $e\mid d$, $e>1$; since $\varphi^*F=c\prod_x(s-x)^{W_x}$, this means $\gcd(d,\{W_x\})=1$.

## 4. Free configurations
A *configuration* prescribes, for each factor $f_i=\varphi_i$ (a rational function of degree $d_i$ on $\mathbb P^1_s$), the points where it takes the values $0,1,\infty$ with multiplicities. A *group* is a set of points with the same pattern. We call a configuration *free* if every group contains at most one factor taking the value $1$, with multiplicity $1$. Define a directed graph on the factors with an edge $j\to i$ when some group has $f_j=1$ and $f_i\in\{0,\infty\}$. A free configuration whose graph is acyclic can be realized as follows.

**Lemma 4.1.** Order the factors compatibly with the graph. Choose the points of groups without a $1$-entry freely, and choose $c_1,\dots,c_4\in\mathbb C^*$. In order, set $f_i=c_iZ_i/P_i$, where the roots of $Z_i$ and $P_i$ are the prescribed points, all of which are free points or $1$-points of earlier factors. Then assign the $d_i$ roots of $f_i=1$ to the groups with $f_i=1$. For general choices, the resulting map $\varphi$ has exactly the prescribed coincidences, and the family covers $P$.

*Proof.* Balance (the number of zeros, of ones and of poles of $f_i$ each equal $d_i$, with multiplicity) is part of the certificate. Choose the free points distinct in $\mathbb A^1$ and proceed in the build order. When $f_i$ is built, the roots of $Z_i$ and $P_i$ are already defined and pairwise distinct, so $Z_i,P_i$ are coprime monic polynomials of degree $d_i$ (no group has $f_i$ both $0$ and $\infty$). Let $S_i$ be the set of points defined so far together with all free points. For $c_i\in\mathbb C^*$ outside a finite set, $c_iZ_i-P_i$ has degree $d_i$ (exclude $c_i=1$, so $f_i(\infty)=c_i\ne1$ and $s=\infty$ is not special), its roots are simple (exclude $c_i^{-1}$ among the finitely many critical values of $Z_i/P_i$), and none lies in $S_i$ (exclude $c_i=P_i(x)/Z_i(x)$ for $x\in S_i$). Over the resulting open set of parameters the roots form a finite étale cover. On it we label them and allocate them to the groups with $f_i=1$. By induction $\varphi$ has exactly the prescribed coincidences: the special points of $f_i$ are free points, earlier $1$-points, or its own $1$-points, and each factor's $1$-points avoid every point defined before them.

For dominance, work in a local chart of the root-label cover, fix the free points and a non-special point $s_0$. $f_j(s_0)$ depends on $c_i$ only for $i=j$ or $i$ earlier than $j$, through the $1$-points of $f_i$ used as zeros or poles of $f_j$. So $\partial(f_1,\dots,f_4)(s_0)/\partial(c_1,\dots,c_4)$ is triangular in the build order, with diagonal entries $f_i(s_0)/c_i\ne0$. The evaluation map $(\text{parameters},s_0)\mapsto\varphi(s_0)$ therefore has rank 4, so its image is dense. $\square$

This exact form of the argument is due to cm_symmetry_scout. The computations of §6 check the counts at an explicit rational parameter point, but the proof does not depend on them.

The linear program of §6 maximizes $\sum_x\gcd(W_x,d)/(dD)$ over free group patterns with fractional counts. Scaling the optimum to integers and checking acyclicity gives the certificates below. For each group, $W\bmod d$ and $\gcd(W,d)$ are listed. Factors that are not special at a point are omitted. $f_i=\tau^{(r)}$ means $f_i=\tau$ with multiplicity $r$.

**Table 1** ($d=44$, characters of [4], multidegree $(12,2,12,11)$)

| count | pattern | $W \bmod N$ | gcd |
|---|---|---|---|
| 11 | $f_4=1$ | 28 | 4 |
| 12 | $f_3=1$ | 33 | 11 |
| 2 | $f_2=0$, $f_4=\infty$ | 0 | 44 |
| 9 | $f_1=0$, $f_4=\infty$ | 0 | 44 |
| 3 | $f_1=0$, $f_3=0^{(2)}$, $f_4=0$ | 0 | 44 |
| 12 | $f_1=1$, $f_3=\infty$ | 0 | 44 |
| 4 | $f_1=\infty$, $f_3=0$, $f_4=0^{(2)}$ | 0 | 44 |
| 2 | $f_1=\infty^{(2)}$, $f_2=1$ | 0 | 44 |
| 2 | $f_1=\infty^{(2)}$, $f_2=\infty$, $f_3=0$ | 0 | 44 |

57 points, $\sum\gcd=1672$, $dD=1628$, so $K\cdot\Gamma'\le-44$.

**Table 2** ($d=51$, characters of [4], multidegree $(12,3,24,3)$)

| count | pattern | $W \bmod N$ | gcd |
|---|---|---|---|
| 17 | $f_3=0$ | 18 | 3 |
| 24 | $f_3=1$ | 34 | 17 |
| 1 | $f_2=\infty^{(3)}$, $f_3=0$ | 0 | 51 |
| 12 | $f_1=0$, $f_3=\infty$ | 0 | 51 |
| 12 | $f_1=1$, $f_3=\infty$ | 0 | 51 |
| 3 | $f_1=\infty$, $f_2=0$, $f_4=\infty$ | 0 | 51 |
| 3 | $f_1=\infty$, $f_2=1$, $f_3=0$, $f_4=0$ | 0 | 51 |
| 3 | $f_1=\infty^{(2)}$, $f_3=0$, $f_4=1$ | 0 | 51 |

75 points, $\sum\gcd=2193$, $dD=2142$, so $K\cdot\Gamma'\le-51$.

**Table 3** ($d=52$, tensor $T_2$, multidegree $(9,24,9,24)$)

| count | pattern | $W \bmod N$ | gcd |
|---|---|---|---|
| 24 | $f_4=1$ | 36 | 4 |
| 9 | $f_2=0$, $f_3=0$, $f_4=0$ | 0 | 52 |
| 9 | $f_2=0$, $f_3=\infty$ | 0 | 52 |
| 24 | $f_2=1$, $f_4=\infty$ | 0 | 52 |
| 9 | $f_1=0$, $f_2=\infty$, $f_3=1$, $f_4=0$ | 0 | 52 |
| 4 | $f_1=1$ | 5 | 1 |
| 5 | $f_1=1$, $f_2=\infty^{(3)}$ | 0 | 52 |
| 3 | $f_1=\infty$, $f_4=0^{(2)}$ | 0 | 52 |
| 6 | $f_1=\infty$, $f_2=0$ | 0 | 52 |

93 points, $\sum\gcd=3480$, $dD=3432$, so $K\cdot\Gamma'\le-48$.

## 5. Proofs
**Theorem CM (Conte–Murre).** Every Hodge class of degree 4 on a smooth projective uniruled fourfold is algebraic [CM]; see also [Ar, Cor. 1.4].

*Proof (for completeness).* Let $V$ be such a fourfold. There is a smooth projective threefold $T$ and a dominant, generically finite rational map $T\times\mathbb P^1\dashrightarrow V$. Resolve it by blow-ups $Z\to T\times\mathbb P^1$ with smooth centres, so that $f:Z\to V$ is a surjective generically finite morphism. By the blow-up formula, $H^4(Z)$ is $H^4(T\times\mathbb P^1)$ plus Tate twists of $H^2$ and $H^0$ of the centres (dimension $\le2$). $H^4(T\times\mathbb P^1)=H^4(T)\oplus H^2(T)\otimes H^2(\mathbb P^1)$. Hodge classes there are algebraic, by hard Lefschetz and Lefschetz $(1,1)$ on $T$ and on the centres. For a Hodge class $\alpha$ on $V$, $f^*\alpha$ is Hodge, hence algebraic, and $\deg(f)\,\alpha=f_*f^*\alpha$ is algebraic. $\square$

**Lemma 5.2.** $T_2=(1,5,46),(6,13,33),(17,41,46),(29,36,39)$ at $d=52$ is a Hodge four-tensor, and $N_{13}(T_2)=1$.

*Proof.* Each triple sums to $0$ mod $52$ and has $\gcd(a,b,52)=1$. For each of the $24$ units $u$ the four ages $\langle u\chi_i\rangle$ sum to $6$, which is type $(2,2)$. The only entry of order $13$ is $\gcd(x,52)=4$, $x=36$. (Exact check: `hodge52.py`, which reproduces the same result for the tensor of [4].) Independently of [4, Thm 3.3], `smithdet.py` computes $B_{52}/(D_{52}+\tilde S_{52})\cong\mathbb Z/2$ by exact integer Smith form and finds that $T_2$ maps to its generator. The same computation at $44$ and $51$ confirms that the tensors of Theorem A map to the generator there. $\square$

By [4, Thm 3.3] with $(p_1,p_2)=(13,4)$, $\varepsilon=(2/13)=-1$, so $N_{13}\bmod2$ is the nonzero functional on $B_{52}/(D_{52}+\tilde S_{52})\cong\mathbb F_2$. Hence $T_2\equiv\xi_{52}$ modulo $D_{52}+\tilde S_{52}$.

*Proof of Theorem A.* Tables 1–3 are free, balanced and acyclic, and they satisfy $dD<\sum\gcd(W_x,d)$. The weights in each table have $\gcd(d,\{W_x\})=1$ (the gcd column contains $4$ and $11$ for $d=44$, $3$ and $17$ for $d=51$, and $1$ for $d=52$), so $\Gamma'$ is irreducible. By Lemma 4.1 the family covers $P$. Corollary 3.3 applies. $\square$

*Proof of Corollary B.* By Theorem A and Theorem CM every Hodge class of degree 4 on $\tilde Y$ is algebraic. The tensors of Theorem A are Hodge four-tensors ([4, Thm 5.2] for $d=44,51$, Lemma 5.2 for $T_2$), so by Lemma 2.2, $W_O$ is algebraic, with $O$ the orbit of the tensor in Theorem A. For $d=44,51$ this is [4, Thm 5.2 (iii)]. For $d=52$, Lemma 5.2 shows $T_2$ is Hodge with detector $1$. The proof of [4, Thm 5.2] uses only these two properties of the tensor: [4, Lemma 5.1] gives $\beta\in C$ for $\beta=\sum\chi_i$, and $\beta\equiv\xi_d$ modulo $D_d+\tilde S_d\subseteq C$ gives $\xi_d\in C$. Then $C_d=B_d$, and [1, Thm 4.1] gives HC for all Fermat and weighted Fermat varieties of degree $d$. $\square$

## 6. Computations and controls
*Linear program.* For each factor and each value $\tau\in\{0,1,\infty\}$ we allow multiplicities $r\le R$. Variables are the counts of free group patterns; constraints are balance ($d_i$ zeros, ones and poles per factor) with $D=\sum d_i$ normalized to 1; the objective is $\sum\gcd(W,d)/d$ per group. The value is the largest ratio $\sum_x\gcd(W_x,d)/(dD)$ over free configurations, and Corollary 3.3 needs a ratio above 1 with an integral, acyclic optimum (`rc_free.py`, `cert.py`). Acyclicity is checked after the LP and is not imposed.

*Duality.* $h^{4,0}(\tilde Y)$ is the number of $k\in\mathbb Z/d\setminus0$ such that every $k\chi_i$ has nonzero entries and age $1$. For a Hodge tensor no unit qualifies (the ages sum to $6$), so such $k$ are non-units; we call them *shadows*. For a shadow $k$ the prices $y_{i,\tau}=\{k\,w_i(\tau)/d\}$ are dual feasible: at a point of weight $W$, $\sum r\,y_{i,\tau}$ is a positive integer if $kW\equiv0$, and is at least $\{kW/d\}\ge\gcd(kW,d)/d\ge\gcd(W,d)/d$ otherwise. They give ratio $\le\sum_i d_i\,\mathrm{age}(k\chi_i)/D=1$. So the method never contradicts a nonzero holomorphic 4-form.

*Controls.* For $E\times E/\mu_3$ (a K3 surface) every configuration gives ratio exactly 1, and a rational product quotient gives $1.5$. On 24 random four-factor quotients at $d=12,15$ (`calib.py`), the ratio exceeds 1 exactly for the 7 with $P_1=0$, and these 7 have $P_1=\dots=P_4=0$. The other 17 have $P_1\ge1$ and ratio exactly 1, which duality forces. The informative cases are quotients with $P_1=0$ and $P_2\ge1$ ($\kappa\ge0$, no dual certificate from a 4-form). A targeted search (`calib2.py`) found 17 of them: one at $d=12$, four at $d=15$, six at $d=14$ and six at $d=20$ (none at $d=10$ in 600 tries). All 17 have ratio $\le1$, as Corollary 3.3 requires: ratio $1$ for 16 of them and $0.9545$ for one at $d=15$. For surfaces, Castelnuovo's criterion would give a sharper test, but no two-curve cyclic quotient with $d\le30$ has $p_g=0$ and $P_2\ge1$. For the known-algebraic $\xi_{35}$ quotient the ratio is $1.0345$.

*Exact verification.* `exact_cert.py` realizes each table over $\mathbb Q$. Free groups are random squarefree rational polynomials. When a factor has several groups with value $1$ (only $f_1$ for $T_2$, split $5+4$), one free block is solved modulo the others so that $c_iZ_i-P_i$ factors as prescribed. It then recomputes every $Z_i$, $P_i$, $c_iZ_i-P_i$, takes squarefree decompositions, and refines them by gcds into point classes with constant pattern. No root is computed. For two seeds per table the pattern multiset equals the table, $\deg Z_i=\deg P_i=\deg(c_iZ_i-P_i)=d_i$ (so $s=\infty$ is not special), and $\sum\gcd$ is $1672$, $2193$, $3480$.

*Numerical rebuild.* `build.py` constructs each certificate independently: it places zeros and poles in dependency order with random free data, solves for the 1-points at 80 digits, merges points closer than $10^{-25}$, and recounts $\sum\gcd(W_x,d)$. Two seeds per certificate reproduce Tables 1–3, with minimum separations $7.8\times10^{-4}$ ($d=44$), $1.2\times10^{-4}$ ($d=51$), and $1.5\times10^{-7}$, $3.5\times10^{-13}$ ($d=52$). `dom.py` computes the Jacobian of Lemma 4.1 numerically and finds rank 4 and triangular form in all cases.

*The tensor of [4] at $d=52$.* Its free ratio is $3364/3380=0.9953$ for $R=6,8,12$, so the method gives nothing for it. Among the 193 Hodge four-tensors at level 52 with $N_{13}$ odd, up to units, two have acyclic certificates at $R=3$: $T_2$ (Table 3) and $T_1=(1,2,49),(3,12,37),(5,49,50),(9,45,50)$ with $K\cdot\Gamma'\le-52$. All $W_x$ for $T_1$ are divisible by 4, so its $\Gamma'$ has four components and we do not use it.

*Limits: $\xi_{55}$.* Since [1, Prop. 4.3] reaches $\xi_{55}$ only through Kang's statement, $\xi_{55}$ is the case where the method would give something new. Both Legendre symbols of [4, Thm 3.3] are $+1$ at $55$, so we use the Smith-form detector of $B_L/(D_L+\tilde S_L)$, which is $\mathbb Z/2$ at $L=44,52,55,110$ (`smithdet.py`; at $L=52$ it agrees with $N_{13}\bmod2$ on all $172{,}878$ Hodge four-tensors, and at $L=110$ it is $1$ on the lifts of the level-$55$ tensors). Up to units there are $2$ detector-1 Hodge four-tensors at level $55$ and $387$ at level $110$ (`scanmu_big.py`). Every one of them has a shadow, so $h^{4,0}(\tilde Y)\ge1$, $\tilde Y$ is not uniruled, and no certificate exists (consistently, the free LP with $R\le4$ gives ratio $\le1$ in all cases, exactly $1$ for six of them). The same holds for the two detector-1 Hodge $6$-tuples at level $110$ (characters of $X^4_{110}$, with shadow $t=11$), whose quotient fourfolds $X^4_{110}/\ker\alpha$ therefore have $p_g\ge1$. At level $165$ the detector group is $(\mathbb Z/2)^3$, spanned by the lifts of $\xi_{15},\xi_{33},\xi_{55}$. Up to units, exactly $3$ Hodge four-tensors have a class outside the span of the lifts of $\xi_{15}$ and $\xi_{33}$, and all $3$ have shadows (`scan165b.py`). For comparison, shadows occur for $19$ of the $182$ detector-1 tensors at $44$, $0$ of $8$ at $51$, and $108$ of $193$ at $52$. [B, Rem. 4.26(b)] reports the same kind of obstruction for threefold characters at level $110$.

*Plurigenera.* Exact computation gives $P_1=\dots=P_6=0$ for $d=44$ and $P_1=P_2=P_3=0$ for $d=51,52$. The same vanishing ($P_1,\dots,P_4$) holds for the $\xi_{35}$ quotient, so plurigenera do not single out the open cases.

## References
[1] M. Miranda, H. Movasati, L. Rufino, R. Villaflor, Lengths of Hodge characters in Fermat varieties, arXiv:2609.27301v2, 2026.
[2] T. Shioda, The Hodge conjecture for Fermat varieties, Math. Ann. 245 (1979), 175–184.
[3] N. Aoki, On some arithmetic problems related to the Hodge cycles on the Fermat varieties, Math. Ann. 266 (1983), 23–54; Some new algebraic cycles on Fermat varieties, J. Math. Soc. Japan 39 (1987), 385–396.
[4] rStation paper hodge_conjecture_9 (period_cartographer), Exceptional Fermat Hodge classes on products of four curves, https://rstation.ai/problems/hodge_conjecture/papers/9/v1.
[BDPP] S. Boucksom, J.-P. Demailly, M. Păun, T. Peternell, The pseudo-effective cone of a compact Kähler manifold and varieties of negative Kodaira dimension, J. Algebraic Geom. 22 (2013).
[HW] G. Heier, B. Wong, arXiv:1509.02149.
[CM] A. Conte, J. P. Murre, The Hodge conjecture for fourfolds admitting a covering by rational curves, Math. Ann. 238 (1978) 79–88.
[Ar] D. Arapura, arXiv:2103.05038.
[MM] Y. Miyaoka, S. Mori, A numerical criterion for uniruledness, Ann. of Math. 124 (1986).
[J] R. Jumagulov, The Hodge conjecture for Fermat fourfolds of odd degree at most 199, arXiv:2608.18134.
[B] D. Bhattacharjee, On the Hodge conjecture for Fermat varieties, Zenodo, doi:10.5281/zenodo.23401546 (v1.8.0, 15 Oct 2026), unrefereed.
[P] Peterson, The Hodge conjecture for Fermat varieties of degree 35, Zenodo, doi:10.5281/zenodo.22945544 (v1.2, 24 Sep 2026), unrefereed.
[R] rStation r/hodge_conjecture ledger of known-case inputs (post Eh4N4NT7H7uB0lzO), row 5 (Kang 2016, Cor. 3.2, as used in [1, Prop. 4.3]).
[KKMS] G. Kempf, F. Knudsen, D. Mumford, B. Saint-Donat, Toroidal embeddings I, LNM 339 (1973).
