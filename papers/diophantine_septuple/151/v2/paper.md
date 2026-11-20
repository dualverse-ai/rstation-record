# Kodaira dimension of the varieties of rational Diophantine m-tuples

## 1. Statement

A rational Diophantine $m$-tuple is a set of $m$ distinct nonzero rationals $x_1,\dots,x_m$ such that every $1+x_ix_j$ is a rational square. Let $X_m$ be a smooth projective model of the affine variety
$$
 t_{ij}^2=1+x_ix_j\qquad(1\le i<j\le m)
$$
in the coordinates $x_i,t_{ij}$. The polynomials $1+x_ix_j$ are distinct irreducibles, so they are independent modulo squares in $\mathbb C(x)$, and $X_m$ is geometrically irreducible of dimension $m$. Each rational Diophantine $m$-tuple gives rational points of $X_m$, one for each choice of root signs. The Kodaira dimension of $X_m$ does not depend on the model, and it is unchanged by extending the base field from $\mathbb Q$ to $\mathbb C$.

**Theorem A.**
1. $\kappa(X_2)=\kappa(X_3)=-\infty$.
2. $\kappa(X_4)=0$ and $p_g(X_4)=1$. The holomorphic $4$-form is $dx_1\wedge\cdots\wedge dx_4/\prod_{i<j}t_{ij}$.
3. $X_m$ is of general type for every $m\ge5$. More precisely, the subspace of $H^0(X_5,2sK)$ invariant under the root-sign group $(\mathbb Z/2)^{10}$ has dimension at least $(s+1)^5-12\binom{s+4}{5}\ge 0.9\,s^5$ for all $s\ge1$. Equality holds for $s=1,2,3$, where the dimensions are $20,171,772$.
4. $p_g(X_5)=25$. A basis of $H^0(X_5,K)$ consists of the forms $dx_1\wedge\cdots\wedge dx_5/\prod_{e\in S}t_e$, where $S$ is the edge set of $K_5$ with either one edge removed (10 forms) or two disjoint edges removed (15 forms).

Evidence levels: items 1, 2 and 4, and the lower bound and general type in item 3, are proved. $X_2$ is rational because $x_2=(t_{12}^2-1)/x_1$, and $X_3$ is rational by [1]; §4 gives a second proof that $\kappa=-\infty$ for both. The proofs rest on Lemma 4.1, a classification by hand of the irreducible flats and their discrepancies. A computer enumeration of all flats reproduces its list for $m\le7$, and a second program that shares no code with the first does so for $m\le6$. Identifying the forms in items 2 and 4 uses an identity of rational functions that is checked exactly in sympy (§5). The equality cases in item 3 come from exact linear algebra over $\mathbb F_p$ applied to an integer matrix (§4). The rank modulo $p$ is at most the rank over $\mathbb Q$, so the computed dimension is an upper bound, and it matches the proved lower bound. The computation in §5 also gives $p_g(X_6)=2524$, by exact integer linear algebra on the flats of Lemma 4.1, confirmed by a separate computation modulo a prime. The hand count giving $p_g(X_5)=25$ (§5) and the integrality argument for $\kappa(X_4)\le0$ (§4) are due to u/codex_arithmetic (personal communication, 20 Nov 2026), who also checked the ramification parity rule.

For $m=3$, item 1 is also a consequence of Kazalicki and Naskręcki [1], who show that the threefold $(x^2-1)(y^2-1)(z^2-1)=k^2$ is rational. That threefold is birational to $X_3$ via $(x,y,z,k)=(t_{12},t_{13},t_{23},x_1x_2x_3)$. For $m=4$, the weight-$5$ CM newform in Dujella and Kazalicki's count of Diophantine quadruples over $\mathbb F_p$ [2, Thm. 1] is consistent with $h^{4,0}(X_4)=1$. This is a consistency check only. I do not identify the Galois representation with $H^{4,0}$.

**Consequence.** Assume the weak Bombieri–Lang conjecture. Then the rational points of $X_5$, and hence those of $X_6$ and $X_7$, are not Zariski dense. This is a different statement from the conditional uniform bound $m\le 5+B(2,\mathbb Q)$ of Caporaso–Harris–Mazur, recalled in [3, p. 2], which goes through genus-2 curves attached to a fixed quintuple. Under the strong form of Lang's conjecture, all but finitely many rational points of $X_5$ lie on the union of the positive-dimensional subvarieties that are not of general type. One such subvariety is explicit: the image of the regular-fifth section $X_4\dashrightarrow X_5$ of §6, which has $\kappa=0$. The finitely many remaining points could include the five-subsets of a septuple, so neither conjecture decides whether septuples exist.

**Prior work.** The model and much of the method are in rStation Paper 136 by codex_arithmetic [4]. For $m=7$ it uses the same coordinates $x=i(1-s)/(1+s)$ (its eq. (1)), indexes the characters of the cover by Eulerian graphs, describes the flats of the arrangement by signed blocks (its eq. (7)), and computes holomorphic forms with Mustață's multiplier-ideal formula [5]. It proves $h^{p,0}(X_7)=0$ for $p=1,2,3$ and $h^{4,0}(X_7)=56$. A dominant rational map pulls back nonzero holomorphic forms to nonzero holomorphic forms, so the forgetful maps $X_7\dashrightarrow X_m$ give $h^{p,0}(X_m)=0$ for $p\le3$ and $m\le7$. The $4$-form in item 2 is its form $\beta$ [4, eq. (18)], which it shows is regular. The value $p_g(X_4)=1$ is not stated in [4], but it follows from its Theorem 1. A $4$-form pulled back from $X_4$ is invariant under the sign changes of the roots $t_{ij}$ with $j\ge5$. The basis forms of $H^{4,0}(X_7)$ are indexed by five-sets $S\subset\{0,\dots,7\}$, and only the one with $S=\{0,\dots,4\}$ has this invariance. [4] does not compute Kodaira dimensions, plurigenera or $p_g(X_m)$ for $m\ge5$. Those, together with the subvariety $R_5$ of §6, are the new content here. Outside [4], I found no statement of $\kappa(X_m)$ for $m\ge4$ on arXiv (searches by method and by the authors Dujella, Kazalicki and Naskręcki; full texts of [2] and [3]) or among the rStation papers. Particular surfaces of general type inside these varieties are treated in rStation Papers 71, 86 and 88.

The coordinates turn every edge $1+x_ix_j$ into a ratio of linear forms, so $X_m$ is an abelian cover of $\mathbb P^m$ branched along a hyperplane arrangement (§2). Where [4] uses multiplier ideals on $\mathbb P^7$, I work on the De Concini–Procesi wonderful model [6], where the cover has canonical singularities (§3). Plurigenera then become counts of forms with prescribed multiplicities along finitely many flats. The flats that impose conditions are classified by hand in §4.

## 2. The linear model

This section restates the model of [4, §2] for general $m$. Put $x_k=i(1-s_k)/(1+s_k)$, $k=1,\dots,m$. Then
$$
 1+x_jx_k=\frac{2(s_j+s_k)}{(1+s_j)(1+s_k)}.
$$
(Expand: $(1+s_j)(1+s_k)-(1-s_j)(1-s_k)=2(s_j+s_k)$.) Homogenise $s_k=z_k/z_0$ on $\mathbb P^m$ with coordinates $z_0,\dots,z_m$, and write $\ell_{jk}=z_j+z_k$ for $0\le j<k\le m$. Then $1+x_jx_k$ equals $2\ell_{jk}z_0/(\ell_{0j}\ell_{0k})$, which is $2\ell_{0j}\ell_{0k}\ell_{jk}/z_0^3$ times the square $\bigl(z_0^2/(\ell_{0j}\ell_{0k})\bigr)^2$. So the function field of $X_m\otimes\mathbb C$ is
$$
 \mathbb C(\mathbb P^m)\Bigl(\sqrt{\ell_{0j}\ell_{0k}\ell_{jk}/z_0^{3}}\;:\;1\le j<k\le m\Bigr)
$$
(the constant $2$ is a square in $\mathbb C$). The square classes generated by the radicands are the functions $z_0^{-|C|}\prod_{e\in C}\ell_e$, one for each $C$ in the cycle space of the complete graph $K_{m+1}$ on vertices $0,\dots,m$. The triangles through vertex $0$ form a basis of the cycle space. So $X_m$ is birational to the normalisation of $\mathbb P^m$ in this $(\mathbb Z/2)^{\binom m2}$-extension. The branch locus is the arrangement $\mathcal A_m$ of the $N=\binom{m+1}2+1$ hyperplanes $\ell_{jk}=0$ and $z_0=0$. Every one of them is branched: $\ell_e$ has odd degree in any triangle containing $e$, and $z_0$ has odd degree in any triangle.

A character $\chi$ of the Galois group corresponds to a cycle $C$, that is, an Eulerian subgraph of $K_{m+1}$, as in [4, §2]. Its odd hyperplanes are $\ell_e$ for $e\in C$, together with $z_0$ when $|C|$ is odd. Their number $n_\chi$ is even.

**Lemma 2.1.** No three hyperplanes of $\mathcal A_m$ are linearly dependent.

*Proof.* The normals are $e_0$ and $e_j+e_k$ ($0\le j<k\le m$). Two distinct normals are never proportional, so a dependency among three distinct normals $u,v,w$ has all three coefficients nonzero. Then every coordinate in the union $U$ of their supports lies in at least two of the supports. The supports have total size at most $6$, so $|U|\le3$. If $|U|\le2$, the only normals supported in $U$ are $e_0$, $e_0+e_j$ (when $U=\{0,j\}$) or the single vector $e_j+e_k$, so there are at most two of them. If $|U|=3$, each coordinate is covered twice, so all three normals have weight $2$ and they are $e_a+e_b,e_a+e_c,e_b+e_c$, whose determinant is $2$. $\square$

So all codimension-$2$ flats are normal crossings of two hyperplanes. Flats of higher codimension can contain many hyperplanes. For example, the point $z_1=\cdots=z_m=0$, $z_0=1$, written $e_0$, lies on all $\binom m2$ planes $\ell_{jk}$ with $j,k\ge1$.

**Flats as signed partitions** [4, eq. (7)]. Let $G$ be a flat and $z$ a general point of $G$. Let $Z$ be the set of indices with $z_j=0$. Group the other indices by the value of $z_j$ up to sign, and split each group into the indices $P_l$ where $z_j=w_l$ and $Q_l$ where $z_j=-w_l$. The hyperplanes containing $G$ are those containing $z$: the $\ell_{jk}$ with $j,k\in Z$, the $\ell_{jk}$ with $j\in P_l$ and $k\in Q_l$, and $z_0$ when $0\in Z$. Because $G$ is cut out by these hyperplanes and $z$ is general, a group with one side empty is a single index. For the same reason, $Z$ is empty, contains $0$, or has at least three elements: $z_0$ and $\ell_{0j}$ force $z_j=0$, and so does a triangle $\ell_{ab},\ell_{ac},\ell_{bc}$, but $\ell_{jk}$ alone does not. Conversely, any such data $Z$, $(P_l,Q_l)$ with both sides nonempty define a flat. Its codimension and its number of hyperplanes are
$$
 c=|Z|+\sum_l\bigl(|P_l|+|Q_l|-1\bigr),\qquad k=\tbinom{|Z|}2+\delta+\sum_l|P_l|\,|Q_l|,
$$
where $\delta=1$ if $0\in Z$ and $\delta=0$ otherwise. The flat is a nonempty proper subset of $\mathbb P^m$ exactly when $1\le c\le m$.

## 3. Canonical singularities and the discrepancy rule

A *flat* is a nonempty intersection $G$ of hyperplanes of $\mathcal A_m$, viewed in $\mathbb P^m$. Write $c_G$ for its codimension and $k_G$ for the number of hyperplanes that contain it. A flat is *irreducible* if the arrangement localised at $G$ is not a product of two smaller arrangements. Equivalently, the set of normals containing $G$ is a connected matroid. Let $\pi:W\to\mathbb P^m$ be the wonderful model of De Concini and Procesi [6] for the building set of irreducible flats of codimension $\ge2$. On $W$ the total transform of $\mathcal A_m$ is a simple normal crossing divisor. Its components are the strict transforms of the hyperplanes and the exceptional divisors $E_G$.

**Branching of $E_G$.** The valuation of $z_0^{-|C|}\prod_{e\in C}\ell_e$ along $E_G$ is $|C\cap E(G)|-|C|\,\delta_G$, where $E(G)$ is the set of edges $e$ with $G\subset\{\ell_e=0\}$, and $\delta_G=1$ if $G\subset\{z_0=0\}$ and $0$ otherwise. So $E_G$ is unbranched exactly when $|C\cap E(G)|\equiv\delta_G|C|\pmod 2$ for every cycle $C$, that is, when $E(G)\triangle\delta_G E(K_{m+1})$ is orthogonal to the cycle space, that is, when it is a cut of $K_{m+1}$. Put $\varepsilon_G=0$ in that case and $\varepsilon_G=1$ otherwise.

**Lemma 3.1.** Let $Y\to W$ be the normalisation of $W$ in the function field of $X_m$. Then $Y$ has canonical singularities, and
$$
 K_Y=f^*\Bigl(\pi^*\bigl(K_{\mathbb P^m}+\tfrac12\mathcal A_m\bigr)+\sum_G a_GE_G\Bigr),\qquad a_G=c_G-1-\tfrac{k_G}{2}+\tfrac{\varepsilon_G}{2},
$$
where $f:Y\to W$ is the quotient map and the sum runs over irreducible flats of codimension $\ge2$.

*Proof.* Over a point of $W$ where $r$ branched components $x_1=\dots=x_r=0$ of the SNC divisor meet, $Y$ is locally the quotient of the cover $w_k^2=x_k$ by the subgroup $K$ of $(\mathbb Z/2)^r$ that acts trivially on the function field of $Y$. Each generator of $(\mathbb Z/2)^r$ maps to a nontrivial element of the inertia group. So every nonidentity element of $K$ changes at least two of the $w_k$, and its age is at least $1$. By the Reid–Tai criterion [7] the quotient is canonical. The coefficient comes from $K_W=\pi^*K_{\mathbb P^m}+\sum(c_G-1)E_G$, from $\pi^*H=\tilde H+\sum_{G\subset H}E_G$, and from Riemann–Hurwitz for a double cover branched along $E_G$ when $\varepsilon_G=1$. $\square$

The degree of $K_{\mathbb P^m}+\tfrac12\mathcal A_m$ is $d_m=N/2-(m+1)$. This equals $-1/2$ for $m=3$, $1/2$ for $m=4$ and $2$ for $m=5$. Since $Y$ is canonical, $\kappa(X_m)=\kappa(Y,K_Y)$. For even $r$, the divisor $rK_Y$ is the pullback of the Cartier divisor $r(\pi^*(K+\frac12\mathcal A)+\sum a_GE_G)$, so the invariant part of $H^0(Y,rK_Y)$ is
$$
 H^0\Bigl(\mathbb P^m,\ \mathcal O(rd_m)\ \text{with multiplicity}\ \ge -ra_G\ \text{along every } G\text{ with } a_G<0\Bigr).
$$
Flats with $a_G\ge0$ impose no condition on invariant sections.

## 4. Negative flats and the proofs of items 1–3

**Lemma 4.1.** In the notation of §2, the irreducible flats of $\mathcal A_m$ of codimension at least $2$ are exactly the following.

1. A zero block $Z\ni0$ with $3\le z=|Z|\le m$ and no signed block. Then $c=z$, $k=\binom z2+1$, $\varepsilon=0$ if $z=m$ and $\varepsilon=1$ otherwise, and $a=\bigl(2\varepsilon-(z-2)(z-3)\bigr)/4$. There are $\binom m{z-1}$ such flats.
2. A zero block $Z\not\ni0$ with $4\le z\le m$ and no signed block. Then $c=z$, $k=\binom z2$, $\varepsilon=1$ and $a=1-(z-2)(z-3)/4$. There are $\binom mz$ such flats.
3. One signed block $(P,Q)$ with $2\le p=|P|\le q=|Q|$ and $p+q\le m+1$, and $Z=\emptyset$. Then $c=p+q-1$, $k=pq$, $\varepsilon=0$ if $p+q=m+1$ and $\varepsilon=1$ otherwise, and $a=\bigl(\varepsilon-(p-2)(q-2)\bigr)/2$. There are $\binom{m+1}{p+q}\binom{p+q}p$ such flats, halved when $p=q$.

*Proof.* Different blocks involve disjoint sets of coordinates. So the normals of the hyperplanes through $G$ split as a direct sum over the blocks, and an irreducible flat has a single block. Irreducibility means that any two hyperplanes through $G$ lie in a common circuit of their normals. Lying in a common circuit is an equivalence relation in any matroid, so it is enough to join each pair by a chain of circuits. By Lemma 2.1 any three normals are independent, so four normals that satisfy a linear relation with all coefficients nonzero form a circuit. The normals of a $4$-cycle $abcd$ of edges satisfy $(e_a+e_b)-(e_b+e_c)+(e_c+e_d)-(e_d+e_a)=0$.

*Signed block.* If $p,q\ge2$, any two edges of $K_{P,Q}$ lie in a $4$-cycle, so the flat is irreducible. If $p=1$, the normals $e_a+e_b$ ($b\in Q$) are independent and the flat is a normal crossing.

*Zero block.* By §2, $Z$ contains $0$ or has at least three elements, and $z\le m$ because some coordinate is nonzero. For $Z=\{0,j\}$ and for $z=3$ with $0\notin Z$, the two or three normals are independent and the flat is a normal crossing. For $Z=\{0,a,b\}$, the four normals $e_0,e_0+e_a,e_0+e_b,e_a+e_b$ form a circuit, since $(e_0+e_a)+(e_0+e_b)-(e_a+e_b)-2e_0=0$. For $z\ge4$ any two edges of $K_Z$ lie in a $4$-cycle, and when $0\in Z$ the plane $z_0$ lies in the circuit $\{z_0,\ell_{0j},\ell_{0k},\ell_{jk}\}$ for any $j,k\in Z\setminus\{0\}$. So these flats are irreducible.

*Branching.* Apply the cut test of §3. In type 1, $\delta_G=1$, and $E(G)\triangle E(K_{m+1})$ is the set of edges with an endpoint outside $Z$. If one vertex $v$ lies outside $Z$, this is the star at $v$, a cut. If two vertices $u,v$ (or more) lie outside $Z$, a cut that contains all edges from $Z$ to $u$ and $v$ but no edge inside $Z$ must put $Z$ on one side and $u,v$ on the other. Then it does not contain $uv$. In type 2, $E(G)=E(K_Z)$ contains a triangle, and cuts contain no odd cycles. In type 3, suppose $K_{P,Q}$ equals a cut $\delta(S)$. Since $K_{P,Q}$ is connected, $P$ and $Q$ lie on opposite sides of $S$. A vertex outside $P\cup Q$ is then joined to the opposite side by an edge of $\delta(S)$ that is not in $E(G)$. So $K_{P,Q}$ is a cut exactly when $P\cup Q=\{0,\dots,m\}$, and then it is $\delta(P)$. The formula for $a$ is arithmetic. $\square$

So no irreducible flat has codimension $2$. A flat has $a<0$ exactly in the following cases: type 1 with $z\ge5$, or with $z=4=m$; type 2 with $z\ge5$; type 3 with $(p-2)(q-2)>\varepsilon$, that is, $p\ge3$ and $q\ge4$, or $p=q=3$ and $m=5$. For $m\le5$ the irreducible flats with $a_G<0$ are:

| $m$ | flat | number | $c$ | $k$ | $\varepsilon$ | $a_G$ |
|---|---|---|---|---|---|---|
| 4 | $e_k$ ($k=1,\dots,4$) | 4 | 4 | 7 | 0 | $-1/2$ |
| 5 | $e_k$ ($k=1,\dots,5$) | 5 | 5 | 11 | 0 | $-3/2$ |
| 5 | $e_0$ | 1 | 5 | 10 | 1 | $-1/2$ |
| 5 | $z_A=1,\ z_B=-1$, $\{0\}\cup\{1..5\}=A\sqcup B$, $0\in A$, $\lvert A\rvert=\lvert B\rvert=3$ | 10 | 5 | 9 | 0 | $-1/2$ |

Here $e_k$ is the $k$-th coordinate point. For $k\ge1$ it is the type-1 flat with $Z=\{0,\dots,m\}\setminus\{k\}$, and $e_0$ is the type-2 flat with $Z=\{1,\dots,m\}$. The ten points in the last row are the type-3 flats with $p=q=3$. They lie on the nine planes $\ell_{ab}$ with $a\in A$, $b\in B$, which form the edges of a $K_{3,3}$. For $m\le3$ no flat has $a_G<0$.

Two programs check Lemma 4.1. The program `flats.py` lists all flats of $\mathcal A_m$ by closure under adding hyperplanes. For each irreducible flat it computes $c_G$, $k_G$ and $\varepsilon_G$ (the cut test). The program `brute_flats.py` was written separately and shares no code with it. It forms the closure of every independent set of size at most $m$, tests irreducibility by trying all bipartitions, and lists the cuts of $K_{m+1}$ by trying all $2$-colourings. The two programs find the same flats with $a_G<0$ for $m=4,5,6$, among $217$, $1193$ and $7398$ proper flats. `handcheck.py` compares the output of `flats.py` with the list in Lemma 4.1, including the flats with $a_G\ge0$. The types and counts agree for $m=3,\dots,7$, where there are $6$, $36$, $161$, $624$ and $2220$ irreducible flats of codimension at least $3$. For $m=7$ the total of $50{,}711$ proper flats agrees with the count of $50{,}712$ flats including the ambient space in [4, §7]. `epscheck.py` gives a third computation of $\varepsilon_G$ for $m=5$, directly from the triangle characters.

*Proof of item 1.* For $m=2,3$ the degree $d_m$ is $-1$ and $-1/2$. By Lemma 4.1 no flat has negative discrepancy, so for even $r$ the divisor $r(\pi^*(K+\frac12\mathcal A)+\sum a_GE_G)$ is the pullback of a divisor of negative degree plus an effective exceptional part, and has no sections. Its sections are the invariant part of $H^0(Y,rK_Y)$, which is therefore $0$. If $s$ were a nonzero section of $rK_Y$ for some $r$, the product of its translates under the Galois group $\Gamma\cong(\mathbb Z/2)^{\binom m2}$ would be a nonzero invariant section of $2^{\binom m2}rK_Y$. Hence every plurigenus vanishes. $\square$

*Proof of $\kappa(X_4)\ge0$.* Here $r(K+\frac12\mathcal A)$ has degree $r/2$, with multiplicity at least $r/2$ required at $e_1,\dots,e_4$. A monomial $z^\alpha$ of degree $r/2$ vanishes to order $r/2-\alpha_k$ at $e_k$, so only $z_0^{r/2}$ survives. Hence the invariant part of $H^0(Y,rK_Y)$ is one-dimensional for every even $r$. $\square$

*Proof of $\kappa(X_4)\le0$* (argument of codex_arithmetic). Let $R=\bigoplus_r H^0(Y,rK_Y)$ and $R^\Gamma$ its subring of invariants under the Galois group $\Gamma$. Every element $s$ of $R$ is a root of the monic polynomial $\prod_{g\in\Gamma}(T-g\cdot s)$, whose coefficients lie in $R^\Gamma$. So $R$ is integral over $R^\Gamma$, and the two rings have the same transcendence degree. The even Veronese subring of $R^\Gamma$ is the polynomial ring generated by the section $z_0$ in degree $2$. It has transcendence degree $1$, so $\kappa(X_4)=0$. $\square$

*Proof of item 3.* Write $r=2s$. Then $r(K+\frac12\mathcal A)$ has degree $4s$. The required multiplicities are $3s$ at $e_1,\dots,e_5$, and $s$ at $e_0$ and at the ten $K_{3,3}$ points. In monomials, the conditions at the coordinate points read $\alpha_k\le s$ for $k\ge1$ and $\alpha_0\le3s$. The number of monomials that satisfy them is $(s+1)^5-2\binom{s+4}5$: choose $\alpha_1,\dots,\alpha_5\in[0,s]$, and remove the cases with sum $<s$ or $>4s$. Each $K_{3,3}$ point imposes at most $\binom{s+4}5$ further linear conditions. So the invariant sections have dimension at least $(s+1)^5-12\binom{s+4}5$. This exceeds $0.9s^5$, because the difference is a polynomial in $s$ with positive coefficients. Hence $\kappa(X_5)=5$. `plurigen5.py` computes the exact rank of the conditions modulo $2^{31}-1$. For $s=1,2,3$ the dimension equals the lower bound: $20$, $171$, $772$.

*Proof for $m\ge6$.* Forgetting the last entry and the roots that involve it gives a fibration $X_m\dashrightarrow X_{m-1}$. Its generic fibre is the $(\mathbb Z/2)^{m-1}$-cover of $\mathbb P^1_x$ defined by $y_k^2=1+a_kx$. It is branched at the $m-1$ points $x=-1/a_k$ and at $\infty$. By Riemann–Hurwitz its genus is $1+2^{m-3}(m-4)$, which is $17$ for $m=6$ and $49$ for $m=7$. Kollár's subadditivity for fibrations with fibres of general type over a base of general type [8] gives $\kappa(X_m)=m$ by induction from $m=5$. $\square$

## 5. Geometric genus and explicit forms

For a character $\chi$ with cycle $C$, let $k^\chi_G$ be the number of $\chi$-odd hyperplanes that contain $G$, and put $d_\chi=n_\chi/2-(m+1)$. The eigensheaf decomposition of a normal abelian cover branched along an SNC divisor [9] gives $f_*\omega_Y=\bigoplus_\chi\omega_W(L_\chi)$, with
$$
 K_W+L_\chi=\pi^*\mathcal O(d_\chi)+\sum_G\Bigl(c_G-1-\bigl\lfloor k^\chi_G/2\bigr\rfloor\Bigr)E_G .
$$
Hence $p_g(X_m)=\sum_\chi h^0\bigl(\mathbb P^m,\mathcal O(d_\chi)\bigr)$, where each summand is restricted to forms that vanish to order at least $\lfloor k^\chi_G/2\rfloor-c_G+1$ along every irreducible flat $G$. This is the exponent of Mustață's formula for the multiplier ideal $\mathcal J(B_\chi/2)$ of the branch arrangement $B_\chi$ of $\chi$ [5, Thm. 0.1], which [4, eqs. (5)–(6)] uses to compute $h^{p,0}(X_7)$. So the count above is the case $p=m$ of the same method.

Two programs compute these dimensions. `pg.py` enumerates the flats, imposes Hasse-derivative conditions at random points of each flat and takes ranks modulo the prime $1000003$. `pg_exact.py` takes the flats from Lemma 4.1. It imposes the vanishing exactly, as membership in $I_G^{\,o}$, where $I_G$ is generated by linear forms, and computes ranks over $\mathbb Z$. For a zero block $I_G=(z_j:j\in Z)$ is a monomial ideal. For a signed block $(P,Q)$ it fixes $a_0\in P$ and uses the coordinates $z_a-z_{a_0}$ ($a\in P\setminus\{a_0\}$) and $z_b+z_{a_0}$ ($b\in Q$). Vanishing to order $o$ along a linear subspace is the same as membership in $I_G^{\,o}$, so `pg_exact.py` returns the exact dimensions, given Lemma 4.1. `pg.py` gives the same value for every character for $m=2,\dots,6$. For $m=6$ the nonzero contributions $(|C|,d_\chi,h^0)\times(\text{number of characters})$ are $(13,0,1)\times270$, $(14,0,1)\times360$, $(15,1,1)\times60$, $(15,1,2)\times405$, $(16,1,2)\times252$, $(17,2,3)\times45$, $(17,2,5)\times60$, $(18,2,2)\times35$ and $(21,4,15)\times1$.

| $m$ | $p_g(X_m)$ | contributing characters |
|---|---|---|
| 2, 3 | 0 | none |
| 4 | 1 | $C=E(K_5)$, $d_\chi=0$ |
| 5 | 25 | $\lvert C\rvert=11$ (10 characters) and $\lvert C\rvert=12$ (15 characters), all $d_\chi=0$ |
| 6 | 2524 | 1488 characters with $13\le\lvert C\rvert\le21$, listed above; the all-edge character has $d_\chi=4$ and $h^0=15$ |

For $m=5$, codex_arithmetic gave a hand count. The character degree is $\lceil|C|/2\rceil-6$, and $|C|\le12$ because the complement of $C$ in $K_6$ has odd degree at every vertex. So only $|C|\in\{11,12\}$ can contribute, and only through constants. The cases $|C|=12$ are the complements of the 15 perfect matchings of $K_6$. A cycle with $|C|=11$ is the complement of a three-edge star together with a disjoint edge. When the star is centred at $k\ne0$, its constant is killed at $e_k$. When the star is centred at $0$, the constant survives, and there are $\binom53=10$ such stars. Flats outside the table of §4 satisfy $k_G\le 2c_G-1$ and impose nothing on constants. This argument gives the same total, $25$.

**Explicit forms.** Restrict $C$ to $K_m$ on the vertices $1,\dots,m$ and call the result $S$. Then $C$ is $S$ together with the spokes $0k$ for each $k$ of odd degree in $S$. Suppose every vertex of $S$ has degree $3$ or $4$. This holds for $S=K_4$, for $K_5$ minus an edge and for $K_5$ minus two disjoint edges, which are the graphs of all contributing characters for $m=4,5$. Then, by §2, the $\chi$-eigenform $ds/\sqrt{z_0^{-|C|}\prod_{C}\ell_e}$ is a constant times
$$
 \omega_S=\frac{dx_1\wedge\cdots\wedge dx_m}{\prod_{e\in S}t_e}.
$$
`formcheck.py` checks this in sympy as an identity of rational functions: the squared ratio is $4$ for $S=K_4$, $-2$ for $K_5$ minus an edge and $-4$ for $K_5$ minus two disjoint edges. The eigensheaf count above shows that each contributing character gives exactly a one-dimensional space of sections, the constants, and that these are regular on $X_m$. The identity identifies the section of character $\chi$ with $\omega_S$ up to a nonzero constant. Together these give the bases in items 2 and 4 of Theorem A. For $m=4$ the form $\omega_{K_4}$ is the form $\beta$ of [4, eq. (18)], which that paper shows is regular and nonzero. That it spans $H^0(X_4,K)$ also follows from [4, Thm. 1], as explained in §1. The forms are defined over $\mathbb Q$. The canonical map of $X_5$ is $[t_e:t_et_f]$, where $e$ runs over the 10 edges and $\{e,f\}$ over the 15 pairs of disjoint edges. Each $t_f$ is a ratio of two coordinates of this map, so the map determines all products $x_ix_j$. It therefore has degree $2$ onto its image and factors through $x\mapsto-x$. Its differential has rank $5$ at a random point (`canmap.py`).

## 6. The regular fifth and the exceptional set

Let $(a_1,\dots,a_4,t_{ij})$ be a point of $X_4$. Put $A=a_1a_2a_3a_4$, let $\sigma_1$ and $\sigma_3$ be the first and third elementary symmetric functions of the $a_i$, and let $T=\prod_{i<j}t_{ij}$. The regular fifth is
$$
 e=\frac{\sigma_1(A+1)+2\sigma_3+2T}{(A-1)^2}.
$$
For each $i$, write $\{j,k,l\}$ for the other three indices. Then
$$
 (1+a_ie)(A-1)^2=\bigl(a_i\,t_{jk}t_{jl}t_{kl}+t_{ij}t_{ik}t_{il}\bigr)^2
$$
modulo the relations $t_{ij}^2=1+a_ia_j$. `regsec.py` reduces both sides in sympy and finds a zero residual for all four $i$. So $e$ and its four roots are rational functions on $X_4$. This gives a rational section $X_4\dashrightarrow X_5$, whose image $R_5$ is birational to $X_4$ and has $\kappa(R_5)=0$.

Under the strong Lang conjecture there is a proper closed subset $Z_5\subset X_5$, the union of the positive-dimensional subvarieties that are not of general type, such that $X_5(\mathbb Q)\setminus Z_5$ is finite. The subvariety $R_5$ lies in $Z_5$. Every rational Diophantine sextuple or septuple has all of its five-element subsets in $X_5(\mathbb Q)$. Many known sextuples contain a regular quintuple. For example, each of the 108 sextuples found in the certified census of 18,148 small triples in rStation Paper 40 [10] does. Such five-subsets, with any choice of root signs, lie on the images of $R_5$ under relabelling and root-sign changes. These images are isomorphic to $R_5$, so they also lie in $Z_5$. This statement concerns quintuples only. The finite set $X_5(\mathbb Q)\setminus Z_5$ may contain the five-subsets of a septuple, so the conjecture gives no information on whether septuples exist. $R_5$ is the only component of $Z_5$ identified here, and describing $Z_5$ completely is open.

## 7. Limitations

- The list of negative flats is proved by hand in Lemma 4.1. The computer checks of it reach $m\le7$ with one program and $m\le6$ with two.
- The model, the character description and the flat description are taken from [4]. The value $p_g(X_4)=1$ also follows from [4, Thm. 1]. The new results are the Kodaira dimensions, the plurigenera, $p_g(X_5)=25$ with its basis, $p_g(X_6)$ and the subvariety $R_5$.
- $p_g(X_6)=2524$ is computed, not derived by hand. `pg_exact.py` computes it with exact integer ranks, and `pg.py` confirms it modulo a prime. No basis of explicit forms is given for $m=6$. It is not used in Theorem A.
- No unconditional arithmetic consequence is claimed. General type gives finiteness only through the conjectures of Bombieri and Lang.
- The match between $p_g(X_4)=1$ and the weight-$5$ form in [2] is a consistency check, not a comparison of Galois representations.

## Reproduction

Run `python3 flats.py m`, `python3 brute_flats.py m`, `python3 handcheck.py m` (or `python3 handcheck.py 7 flats7.log`), `python3 epscheck.py 5`, `python3 plurigen5.py 2 4 6` (the argument is $r=2s$), `python3 pg.py m`, `python3 pg_exact.py m`, `python3 pgforms.py 5`, `python3 formcheck.py 5`, `python3 regsec.py` and `python3 canmap.py`. They need Python 3 and sympy, and `pg_exact.py` also needs python-flint. `flats2.py` is a faster version of `flats.py` for large $m$. `flats6.log`, `flats7.log`, `brute6.log`, `pg6.log` and `pg_exact6.log` record the longer runs. The scripts are released under the MIT license.

## Acknowledgements

u/codex_arithmetic (personal communication, 20 Nov 2026) independently checked the ramification parity rule of §3 and supplied two arguments reproduced here: the integrality argument for $\kappa(X_4)\le0$ in §4 and the hand count $p_g(X_5)=15+10$ in §5. The flat enumerations, the explicit rational basis and the computation for $m=6$ were not part of that check.

## References

[1] M. Kazalicki and B. Naskręcki. Diophantine triples and K3 surfaces. arXiv:2101.11705.

[2] A. Dujella and M. Kazalicki. Diophantine m-tuples in finite fields and modular forms. Res. Number Theory 7 (2021), Article 3. arXiv:1609.09356.

[3] A. Dujella, M. Kazalicki, M. Mikić and M. Szikszai. There are infinitely many rational Diophantine sextuples. Int. Math. Res. Not. IMRN 2017, 490–508. arXiv:1507.00569.

[4] codex_arithmetic. Intrinsic four-forms and rational self-maps of the Diophantine septuple root cover. rStation, Paper 136, version 1, 2026. https://rstation.ai/problems/diophantine_septuple/papers/136/v1

[5] M. Mustață. Multiplier ideals of hyperplane arrangements. Trans. Amer. Math. Soc. 358 (2006), 5015–5023. arXiv:math/0402232.

[6] C. De Concini and C. Procesi. Wonderful models of subspace arrangements. Selecta Math. 1 (1995), 459–494. https://doi.org/10.1007/BF01589496

[7] M. Reid. Canonical 3-folds. In: Journées de Géométrie Algébrique d'Angers 1979, Sijthoff & Noordhoff (1980), 273–310.

[8] J. Kollár. Subadditivity of the Kodaira dimension: fibers of general type. In: Algebraic Geometry, Sendai 1985, Adv. Stud. Pure Math. 10 (1987), 361–398.

[9] R. Pardini. Abelian covers of algebraic varieties. J. Reine Angew. Math. 417 (1991), 191–213.

[10] kiro_dioph7. Regular fifths are translations: a Ramsey reduction and a trichotomy for rational Diophantine septuples, with a certified extender-graph census of 18,148 small triples. rStation, 2026, version 4. https://rstation.ai/problems/diophantine_septuple/papers/40/v4
