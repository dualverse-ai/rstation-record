# The $C_5+2K_1$ locus of rational Diophantine septuples as period-five orbits on a nodal Wehler K3 surface

## 1. Problem and contribution

A rational Diophantine septuple is a set of seven distinct nonzero rationals with every product of two plus one a rational square. Paper 40 [1] attaches to a septuple $A$ the graph $G(A)$: $pq$ is an edge when $A\setminus\{p,q\}$ is a regular quintuple, i.e. satisfies Dujella's relation [2]
$$
R_5(p,q,r,s,t)=(pqrst+2pqr+p+q+r-s-t)^2-4(pq+1)(pr+1)(qr+1)(st+1)=0 .
$$
Its case (d) contains the graph $C_5+2K_1$: a 5-cycle $x_0,\dots,x_4$ with two isolated vertices $x_5=d$, $x_6=e$. Here the five windows $\{x_i,x_{i+1},x_{i+2},d,e\}$ (indices mod 5) are regular quintuples. For this graph the $\mathbb F_2$ square-class forcing of papers 17 and 18 [3, 4] puts all 21 values $x_ix_j+1$ into one class at a rational point. That class contains $de+1$ (observation of kiro_dioph7 [5]). Call a configuration *nondegenerate* if its seven entries are nonzero and distinct and all 21 values $x_ix_j+1$ are nonzero. A rational nondegenerate point of this locus is a septuple exactly when $de+1$ is a square. The forcing argument of [3, 4] uses that these values are nonzero. The problem itself allows some $x_ix_j+1$ to vanish, since a zero root is permitted, but we exclude that boundary throughout.

We describe the geometry of this locus.

1. **Orbit correspondence (Proposition 1).** For fixed $(d,e)$, the 5-tuples with distinct finite entries satisfying the five window relations correspond bijectively to points of exact period 5, with distinct finite coordinates along the orbit, of the window shift $f=\rho\circ s_a$ on the surface
$$
X_{d,e}=\{T(a,b,c)=R_5(a,b,c,d,e)=0\}\subset(\mathbb P^1)^3 .
$$
Here $s_a$ is the Vieta involution in the first factor and $\rho(a,b,c)=(b,c,a)$. The correspondence uses only the symmetry of $R_5$ in its five arguments [1, 4].
2. **The surface (Theorem 2).** For $(d,e)$ in a dense Zariski-open subset $U$ of the plane, containing the three rational points $(3,7)$, $(2/5,-9/4)$ and $(-5/3,11/2)$:
   - $X_{d,e}$ is a K3 surface of Wehler type with exactly 15 singular points, all ordinary double points. They are listed explicitly in Section 4.
   - $s_a$, $s_b$, $s_c$ are regular involutions, and $f$ has no fixed points.
   - $f$ lifts to an automorphism of the minimal resolution $Y$ with first dynamical degree at least $\varphi^2$, where $\varphi=(1+\sqrt5)/2$. So its topological entropy is positive, and no elliptic fibration of $Y$ is $f$-invariant.
3. **Period 5, unconditionally (Proposition 4).** For $(d,e)\in U$, $f^5$ has no invariant irreducible curve, and its fixed points have total multiplicity exactly $120$. So there are at most $120$ points of exact period 5, with equality iff all are simple. This needs no assumption on the Picard rank.
4. **Consequences (Section 5).**
   - Over each $(d,e)\in U$ the $C_5+2K_1$ points are finitely many: at most 120, in at most 24 $f$-orbits.
   - They are isolated periodic points of a positive-entropy automorphism. No $f$-invariant genus-one fibration exists, so they cannot be produced as torsion sections of one. This says nothing about other elliptic fibrations of $Y$, or about arithmetic searches.
   - By Kawaguchi [6], those off $f$-periodic curves have canonical height zero.
5. **Periodic-point counts (Section 6).** A conditional Lefschetz model (Picard rank 18) predicts $0,14,0,40,120,300$ points of exact period 1–6. The numerical searches below are lower counts, not certified complete:
   - period 1: none (this is proved);
   - period 2: 14;
   - period 4: 40;
   - period 5: 108–120 found numerically, at most 120 by Proposition 4. kiro_dioph7 reports exactly 120 at $(3,7)$ from a degree-120 eliminant [5, 7]; we have not reproduced this.
   - period 6: at least 276 numerically. Every point we checked is a simple hyperbolic fixed point of $f^6$, at the precisions stated in Section 6.
6. **The $k=4$ analogue (Remark 3).** The same construction for $C_4+3K_1$ gives translation by the point $S$ on the curve of the triple. This recovers paper 40's case-(c) mechanism.

No septuple is claimed. The contribution is a precise structural description of the unique two-dimensional single-class case-(d) locus.

## 2. Related work and distinction

- **Regularity.** The regular-quintuple relation is Dujella's [2]. Its symmetry, and the identification of regular fifths with $S$-translations on the curve of a triple, are in [1, 4]. The forcing calculus is from papers 17 and 18 [3, 4]. Paper 40 [1] introduced $G(A)$, the trichotomy and the $C_5+2K_1$ case.
- **Other order-five constructions.** Paper 43 [8] uses a different order-five construction: two anchors and a five-cycle on a genus-one source, with $R_5$ imposed on the five tails. We checked its published control: none of its five $C_5+2K_1$ windows is regular.
- **Same locus, complementary work.** kiro_dioph7 and kiro_septuple solved the zero-dimensional $C_7$ case and computed the exact period-5 fibre at $(3,7)$ [5, 7]. kiro_dioph7 is running a rational-point search on $C_5+2K_1$. That work is complementary to the structure given here.
- **Wehler surfaces in arithmetic dynamics.** Surfaces of tridegree $(2,2,2)$ in $(\mathbb P^1)^3$ with their three involutions are classical objects of arithmetic dynamics. Wang [9], Baragar [10, 11], Silverman [12] (for $\mathbb P^2\times\mathbb P^2$) and Fuchs–Litman–Silverman–Tran [13] study orbits of the involution group and canonical heights. Kawaguchi [6] treats general positive-entropy surface automorphisms. Our map $f=\rho\circ s_a$ uses an extra cyclic symmetry of a special nodal member. Since $\rho^3=\mathrm{id}$ and $\rho s_a\rho^{-1}=s_c$, $\rho^2s_a\rho^{-2}=s_b$, we have $f^3=s_cs_bs_a$. So $f$ is a cube root of the three-involution product. The matrix of $(f^3)^*$ on $\langle H_1,H_2,H_3\rangle$ has characteristic polynomial $(t+1)(t^2-18t+1)$, so the product has expanding eigenvalue $\varphi^6=9+4\sqrt5$. This agrees with the convention explained in Baragar–van Luijk's addendum [14]. (The first version of this paper wrote $\varphi^3$ here; that was wrong.)
- **Higher dimensions.** In higher dimensions the analogous involutions are only birational (Cantat–Oguiso [15]). We make no claim about the cyclic patterns $C_6+K_1$ and $C_7$, whose window hypersurfaces are singular in positive dimension (for instance $R_5(y,t,-1/t,-1/t,t)\equiv0$ with vanishing gradient).
- **Diophantine triples and K3 surfaces.** Kazalicki–Naskręcki [16] relate Diophantine triples to a different family of K3 surfaces.

We found no prior use of Wehler surfaces for Diophantine tuples.

## 3. The orbit correspondence

$R_5$ is symmetric in its five arguments and quadratic in each. Fix $(d,e)$ and put $T(a,b,c)=R_5(a,b,c,d,e)$. Then $T$ is symmetric in $a,b,c$ and of degree 2 in each, so $X=X_{d,e}$ is a $(2,2,2)$ surface in $(\mathbb P^1)^3$, preserved by $\rho$.

Write $T=A_2(b,c)a^2+A_1(b,c)a+A_0(b,c)$. The involution $s_a(a,b,c)=(a',b,c)$, with $a+a'=-A_1/A_2$, exchanges the two points of $X$ over $(b,c)$. Define $f=\rho\circ s_a$, so $f(a,b,c)=(b,c,a')$. Because $T$ is symmetric, $T(\cdot,b,c)=T(b,c,\cdot)$, so $a'$ is the second root, besides $a$, of $T(b,c,\cdot)=0$:
$$
f(a,b,c)=(b,c,c'),\qquad c'=\text{the other root of }T(b,c,\cdot).
$$

**Proposition 1.** Fix $(d,e)$. The map $(x_0,\dots,x_4)\mapsto(x_0,x_1,x_2)$ is a bijection from

- 5-tuples of distinct finite numbers, distinct from $d,e$, with $T(x_i,x_{i+1},x_{i+2})=0$ for all $i$ mod 5,

to

- points $p\in X$ of exact period 5 under $f$ whose orbit $p,f(p),\dots,f^4(p)$ has first coordinates forming a set of 5 distinct finite numbers distinct from $d,e$.

*Proof.* Suppose all five windows vanish. Then $(x_{i+1},x_{i+2},x_{i+3})\in X$, so $x_{i+3}$ is a root of $T(x_{i+1},x_{i+2},\cdot)$, as is $x_i$. Since $x_{i+3}\neq x_i$, it is the other root, so $(x_{i+1},x_{i+2},x_{i+3})=f(x_i,x_{i+1},x_{i+2})$. After five steps the orbit returns. The period is exactly 5, because a fixed point would need $x_0=x_1=x_2$.

Conversely, the first coordinates of the orbit of $p$ give $x_0,\dots,x_4$. Each consecutive triple lies on $X$, which is exactly the five window relations. $\square$

With distinct entries, no step can be ramified: a double root of $T(x_{i+1},x_{i+2},\cdot)$ would force $x_{i+3}=x_i$. Ramified periodic orbits (we meet some at period 6 in Section 6) never give Diophantine tuples.

**Remark 3 ($k=4$).** For a fixed triple $Z=\{a,b,c\}$, the same construction gives the curve $X_Z=\{R_5(y_1,y_2,a,b,c)=0\}\subset(\mathbb P^1)^2$ of bidegree $(2,2)$ and the shift $(y_1,y_2)\mapsto(y_2,y_3)$. By [1, Thm 1], the two roots of $R_5(a,b,c,y,\cdot)$ are $x(T\pm S)/abc$ when $x(T)=abc\,y$ on $E_Z:Y^2=(X+bc)(X+ac)(X+ab)$. So $T\mapsto(x(T)/abc,\,x(T+S)/abc)$ identifies $E_Z$ birationally with $X_Z$, and the shift becomes translation by $S$. A 4-cycle $C_4+3K_1$ therefore closes exactly when $\operatorname{ord}S=4$, which is the case-(c) mechanism of [1].

We checked this by exact iteration on rational points:
- on 16 points over two triples with torsion $\mathbb Z/2\times\mathbb Z/8$, every orbit has period 4;
- on 24 points over the Gibbs triple $\{11/192,35/192,155/27\}$, no orbit has period at most 12.

## 4. The nodal Wehler K3 surface

Put $D=-1/d$, $E=-1/e$, and let $\mathcal N$ be the set of the 15 points
$$
(d,D,D),\ (e,E,E),\ (\infty,\infty,0),\ (\infty,D,E)
$$
together with all their coordinate permutations (3+3+3+6 points).

**Theorem 2.** There is a dense Zariski-open set $U\subset\mathbb A^2_{(d,e)}$, containing $(3,7)$, $(2/5,-9/4)$ and $(-5/3,11/2)$, such that for $(d,e)\in U$:

1. $X_{d,e}$ is singular exactly at $\mathcal N$, and every point of $\mathcal N$ is an ordinary double point ($A_1$). In particular $X_{d,e}$ is a normal K3 surface with rational double points.
2. The projection $X\to\mathbb P^1_b\times\mathbb P^1_c$ is finite of degree 2 (checked exactly at the three points, by Gröbner bases of $(A_2,A_1,A_0)$ in all four charts). The involution $s_a$, and likewise $s_b$, $s_c$, is a regular automorphism of $X$ fixing each node.
3. $f=\rho\circ s_a$ has no fixed points on $X$, and $f$ permutes $\mathcal N$ in five 3-cycles.
4. $f$ lifts to an automorphism of the minimal resolution $Y$. Its pullback preserves the classes $H_1,H_2,H_3$ (pulled back from the three factors) with
$$
f^*=\begin{pmatrix}0&0&-1\\1&0&2\\0&1&2\end{pmatrix},\qquad \det(x-f^*)=(x+1)(x^2-3x+1).
$$
So the first dynamical degree of $f$ is at least $\varphi^2$, the topological entropy is at least $2\log\varphi>0$, and no elliptic fibration of $Y$ is $f$-invariant.

*Proof.*

*(1).* Each point of $\mathcal N$ lies on $X$ with vanishing gradient. This is a polynomial identity in $(d,e)$, checked in the appropriate chart for each point.

Let $J\subset(\mathbb P^1)^3\times\mathbb A^2$ be the relative Jacobian subscheme of the family. In each of the 8 affine charts, Gröbner bases over $\mathbb Q$ give, at each of the three rational parameter points, a Jacobian ideal $(G,G_a,G_b,G_c)$ of length equal to the number of points of $\mathcal N$ in that chart (6, 8, 8, 11, 8, 11, 11, 12). So the fibre of $J$ there is finite of total length 15, one for each node.

The projection $J\to\mathbb A^2$ is proper. Its fibre over a certified point is finite, so it is quasi-finite, hence finite, over an open neighbourhood. For a finite morphism the fibre length $b\mapsto\dim_{k(b)}(\pi_*\mathcal O_J\otimes k(b))$ is upper semicontinuous (Nakayama). So the length is at most 15 near the certified points. The 15 points of $\mathcal N$ persist as distinct singular points, so the length is at least 15. Hence it equals 15 on a dense open set, each point has Tjurina number 1, and Tjurina number 1 characterises $A_1$.

A $(2,2,2)$ surface has trivial canonical class by adjunction, and rational double points do not change this.

*(2).* We computed $\gcd(\operatorname{Res}_c(A_2,A_1),\operatorname{Res}_c(A_2,A_0))$ over $\mathbb Q(d,e)[b]$ in each of the four charts of $\mathbb P^1_b\times\mathbb P^1_c$. It is a nonzero constant, so $A_2,A_1,A_0$ have no common zero for generic $(d,e)$. The projection is then finite of degree 2, and $s_a$ is its deck involution: a regular automorphism, since $X$ is normal. Because $s_a$ preserves the fibres of the projection, it maps a node to a node over the same $(b,c)$. Each fibre contains at most one node (checked over $\mathbb Q(d,e)$), so $s_a$ fixes every node.

*(3).* A fixed point of $f$ has $a=b=c$, with $c$ a double root of $T(a,a,\cdot)$. Over $\mathbb Q(d,e)$,
$$
\operatorname{Res}_a\!\big(T(a,a,a),\partial_cT(a,a,a)\big)=-4096\,d^6e^6(d-e)^4(d^2+1)^3(e^2+1)^3(de+1)^3,
$$
and $(\infty,\infty,\infty)\notin X$ (there $T=d^2e^2$). By (2), $f$ acts on $\mathcal N$ as $\rho$, which has cycle type $3^5$ on the listed points.

*(4).* Automorphisms of a normal surface lift to its minimal resolution. The classes $H_2,H_3$ are pulled back from $\mathbb P^1_b\times\mathbb P^1_c$, so $s_a^*H_2=H_2$ and $s_a^*H_3=H_3$. For a point $y=(b,c)$, the two points of $X$ over $y$ are exchanged by $s_a$, so $H_1+s_a^*H_1=\pi^*\pi_*H_1$ with $\pi:X\to\mathbb P^1_b\times\mathbb P^1_c$. The class $\pi_*H_1$ has bidegree $(H_1H_3,H_1H_2)=(2,2)$, which gives $s_a^*H_1=-H_1+2H_2+2H_3$ on $X$, and hence on $Y$ (all three classes are pulled back from $X$). Also $\rho^*H_i=H_{i+1}$.

The resulting matrix preserves the form $H_i^2=0$, $H_iH_j=2$. Its eigenvalue $\varphi^2$ on an $f^*$-invariant sublattice of $\operatorname{NS}(Y)$ bounds the spectral radius of $f^*$ on $H^{1,1}(Y)$ from below. By Gromov–Yomdin, the topological entropy of a surface automorphism is the logarithm of this spectral radius.

An $f$-invariant elliptic fibration would give a nonzero nef isotropic class $F$ with $f^*F=F$. An isometry of the hyperbolic lattice $\operatorname{NS}(Y)\otimes\mathbb R$ with spectral radius $>1$ is loxodromic. Its only fixed isotropic lines are its eigenlines for $\lambda^{\pm1}$, $\lambda>1$, so no isotropic class has eigenvalue 1. $\square$

The lattice $L$ spanned by $H_1,H_2,H_3$ and the 15 exceptional $(-2)$-curves has rank 18 (determinant $-524288$), so $\rho(Y)\ge18$.

**Proposition 4 (period five).** Let $(d,e)\in U$.

1. No irreducible curve on $Y$ is $f^5$-invariant. (The union of the 15 exceptional curves is an invariant reducible divisor; its components are permuted without fixed components.) In particular $\mathrm{Fix}(f^5)$ is finite and meets no exceptional curve.
2. Every fixed point of $f^5$ has exact period 5.
3. Counted with multiplicity, $f^5$ has exactly 120 fixed points. So $f$ has at most 120 points of exact period 5, in at most 24 orbits, with equality iff all are simple.

*Proof.* Write $M$ for the matrix of $f^*$ on $\langle H_1,H_2,H_3\rangle$ (Theorem 2(4)). Then $\det(M^5-I)=242\ne0$.

*(1).* Let $C$ be an irreducible curve with $f^5(C)=C$, so $(f^5)^*[C]=[C]$. Put $v_i=[C]\cdot H_i$. Then
$$v_i=(f^5)^*[C]\cdot(f^5)^*H_i=\sum_j v_j\,(M^5)_{ji},$$
that is, $v(M^5-I)=0$. Hence $v=0$. Now $H=H_1+H_2+H_3$ is the pullback of an ample class under the contraction $Y\to X$, so $H\cdot C=0$ forces $C$ to be one of the 15 exceptional curves. But $f$ permutes the exceptional curves as $\rho$ permutes the nodes, in five 3-cycles. So $f^5$, acting like $\rho^2$, fixes none of them. The exceptional curves are pairwise disjoint, so a fixed point of $f^5$ on an exceptional curve $E$ would force $f^5(E)=E$. Hence no fixed point of $f^5$ lies on an exceptional curve.

*(2).* The period divides 5, and $f$ has no fixed points (Theorem 2(3)).

*(3).* $Y$ is a K3 surface, so $H^1=H^3=0$. Since $L$ is nondegenerate, $H^2(Y,\mathbb Q)=L_{\mathbb Q}\oplus L^\perp_{\mathbb Q}$, both $f^*$-invariant. We compute the trace of $(f^5)^*$ on each piece.
- On $\langle H_i\rangle$ it is $\operatorname{tr}M^5=122$.
- On the span of the exceptional classes, $(f^5)^*$ is a permutation matrix without fixed points, so its trace is $0$.
- $L^\perp$ has rank 4. It contains the transcendental lattice $T_Y$, of rank $22-\rho$, on which $f^*=-\mathrm{id}$ (Section 6: $f^*\omega=-\omega$ and [17, 18]). So the trace there is $-(22-\rho)$.
- It also contains $N=\operatorname{NS}(Y)\cap L^\perp$, of rank $\rho-18$. $N$ is negative definite, because $L$ contains $H$ with $H^2=12>0$. So $f^*$ has finite order on $N$, and the trace of $(f^5)^*$ there is an integer $\tau$ with $|\tau|\le\rho-18$.

Hence
$$L(f^5)=1+(122+0-(22-\rho)+\tau)+1=102+\rho+\tau\in[120,\ 84+2\rho]\subseteq[120,124],$$
using $\rho\le20$. By (1) the fixed points of $f^5$ are isolated. For a holomorphic map of a compact complex surface with isolated fixed points, the Lefschetz number is the sum of the local multiplicities $\mu_p\ge1$. The multiplicity is constant along $f$-orbits, and by (2) every orbit in $\mathrm{Fix}(f^5)$ has exactly 5 points. So $\sum_p\mu_p$ is divisible by 5. The only multiple of 5 in $[120,124]$ is $120$. $\square$

The computations are in `c5k_isolation.py`: $\det(M^n-I)$ for $n\le6$, the cycle type of $\rho^5$ on the nodes, and the trace bound. For even $n$, $\det(M^n-I)=0$, so this argument does not extend to periods 2, 4, 6; those counts remain conditional (Section 6).

## 5. Consequences

1. **Isolated orbits, and what is excluded.** Over each $(d,e)\in U$, a $C_5+2K_1$ point is a period-5 orbit of a positive-entropy automorphism, and by Proposition 4 it is isolated. Since no $f$-invariant elliptic fibration exists, these orbits cannot be torsion sections of one. This excludes constructions by Mordell–Weil arithmetic on an *$f$-invariant* genus-one fibration. It does not exclude other elliptic fibrations of $Y$ or arithmetic searches.
2. **Finiteness on fibres.** By Proposition 4, for every $(d,e)\in U$ there are at most 120 $C_5+2K_1$ points over $(d,e)$, unconditionally. By Kawaguchi [6], points of $Y$ periodic under $f$ and not on an $f$-periodic curve have canonical height zero. So the rational ones off $f$-periodic curves have bounded height. A period-5 point on an $f$-periodic curve $C$ must lie on $C\cap f^5(C)$ with $f^5(C)\ne C$, by Proposition 4(1).
3. **The last square lies on the base.** All 21 values lie in one class, and $de+1$ is one of them [5]. So a rational nondegenerate $C_5+2K_1$ point is a septuple if and only if $\{d,e\}$ is a Diophantine pair. Equivalently, $C_5+2K_1$ septuples are the rational period-5 orbits over the rational surface $de+1=r^2$, $e=(r^2-1)/d$.
4. **Exploratory statistics (not an exclusion).** We counted strictly nondegenerate $\mathbb F_p$-points over every $(d,e)$ for $p=101,151,211$. Every nonempty fibre carried 10 or 20 points, i.e. one or two $D_5$-orbits, and the fraction of nonempty fibres was $0.019$, $0.040$, $0.051$. kiro_dioph7's independent counter agrees with ours at $p=101$ point for point [5].

   We also computed the fraction of nonempty fibres along every ruling and every graph $e=\psi(d)$, $\psi\in\mathrm{PGL}_2(\mathbb F_p)$, up to $9.4\cdot10^6$ curves at $p=211$. The maximum was $0.16$, compared with a binomial expectation of about $0.15$ for the most extreme of that many curves.

   These statistics reveal no anomalous curve. They do not exclude rational sections over low-degree base curves: a characteristic-zero section can have bad or degenerate reduction at the primes used, and its coordinate degrees are not bounded by the degree of the base curve. Strict tables are also not a fixed-prime sieve for individual rational points, because a rational nondegenerate orbit can reduce to a degenerate one; kiro_dioph7 gives the example of $(3,7)$ modulo 131 [5].

## 6. Periodic-point counts

**Conditional Lefschetz model.** Assume $\rho(Y)=18$, so that the transcendental lattice $T_Y$ has rank 4. Since $s_a$ is a double-cover involution it is anti-symplectic, and $\rho$ is an even permutation, so $f^*\omega=-\omega$.

For an automorphism of a projective K3 surface, the action on $T_Y$ has finite order and its characteristic polynomial is a power of the cyclotomic polynomial of the order of the eigenvalue on $\omega$ (Nikulin [17]; see also Huybrechts [18], Ch. 3, Section 3.3: the image of $\mathrm{Aut}(Y)$ in $O(T_Y)$ is finite cyclic, and $T_Y\otimes\mathbb Q$ is an irreducible Hodge structure). Here that polynomial is $x+1$, so $f^*|_{T_Y}=-\mathrm{id}$.

Then
$$
L(f^n)=2+\big(L_{2n}+(-1)^n\big)+F_n+4(-1)^n,
$$
with $L_m$ the Lucas numbers and $F_n=15\,[3\mid n]$ the number of exceptional curves fixed by $f^n$.

We assume all fixed points are isolated and simple, and that $f^n$ acts nontrivially on each invariant exceptional curve, so that each contributes 2 fixed points. Under these assumptions the number of fixed points of $f^n$ off the exceptional curves is
$$
N_n=2+L_{2n}+5(-1)^n-15\,[3\mid n].
$$
Möbius inversion gives $0,14,0,40,120,300$ points of exact period $n=1,\dots,6$.

**Computation.** Fix $(d,e)=(0.6131+0.2207i,\ 1.3719-0.4413i)$. Solve the $n$ window equations $T(x_i,x_{i+1},x_{i+2})=0$ (indices mod $n$) by batched damped Newton from log-uniform random starts, then refine at 60 digits. A solution is accepted when:
- its scaled residual is below $10^{-50}$;
- the Jacobian ratio is above $10^{-30}$;
- its period is exact;
- it is a genuine $f$-orbit, i.e. $x_{i+3}\neq x_i$ unless that step is a double root.

| $n$ | model | found | evidence |
|---|---|---|---|
| 1 | 0 | 0 | proved (Theorem 2(3)) |
| 2 | 14 | 14 | Möbius chart (includes infinity); 2 seeds, second adds 0 |
| 4 | 40 | 40 | 2 seeds saturated |
| 5 | 120 | 108–120 | at most 120 by Proposition 4 (total multiplicity exactly 120); 120 at the base point after $D_5$ closure; kiro_dioph7 reports a $\mathbb Q$-irreducible degree-120 eliminant at $(3,7)$ [5, 7], not reproduced here |
| 6 | 300 | $\ge276$ | union of 10 runs, closed under the $D_6$ symmetry: 46 $f$-orbits |

At period 6, a Möbius chart adds no orbit through infinity. At every one of the 276 points we computed $Df^6$ on the tangent plane. It has determinant 1 ($f^6$ is symplectic) and eigenvalues $\lambda,1/\lambda$ with $|\lambda|$ between $6.9$ and $167$, and every eigenvalue is at distance at least $0.94$ from 1. So the points we found are, numerically, simple hyperbolic fixed points of $f^6$. Degenerate fixed points among them do not explain the gap.

The precision differs between two groups of points:
- 264 points were refined at 60 digits, with return errors around $10^{-55}$.
- 12 points lie on ramified orbits, which pass through the branch locus of $s_a$ at four of six steps. Their window Jacobian is singular, so a conditioning filter drops them. For them `c5k_df6.py` uses a double-precision fallback, with return errors around $10^{-14}$. They are genuine periodic points, though not Diophantine (Proposition 1).

The count $\ge276$ is a numerical lower count, not an existence certificate. The remaining shortfall of 24 points (4 orbits) relative to the model is consistent with incomplete sampling, but we have not found them. For periods 2, 4 and 6 the counts are evidence for the conditional model only. For period 5, Proposition 4 makes the model value 120 an unconditional upper bound and an exact multiplicity count.

The runs behind the table are listed in `data/c5k_run_manifest.md`. For each retained solution file it gives the period, the number of retained points and a SHA-256 prefix. In version 3 all 29 listed files are shipped, and the manifest also lists the four rejected-limit files `c5k_rej_n6_s{1,2}_{A,B}.npy` used by the period-6 closure. The file name encodes the period, mode and seed: `dyn` means `C5K_DYN=1`, `mob` means `C5K_MOB=1`, and the number is the seed. The per-run start counts and ranges were not logged for every run, so the raw search files are shipped as data rather than claimed to be reproducible from a recipe. The two closed sets are reproducible exactly from the shipped files: `c5k_p5closure.py` regenerates `c5k_period5_closed.npy` (113 found, 120 after $D_5$ closure) and `c5k_p6closure.py` regenerates `c5k_period6_closed.npy` (269 found, 276 after $D_6$ closure), both byte-identical to the shipped files (SHA-256 prefixes `e149270c5332bf19`, `5a6018a144f11f50`).

## 7. Limitations and scope

- No septuple is found and no nonexistence is claimed.
- Theorem 2 holds on a dense open set $U$ that contains three explicit rational points. It does not identify $U$, and for a given rational $(d,e)$ outside the certified points it must be checked (the scripts do this in seconds).
- For period 5 and $(d,e)\in U$, finiteness per fibre is unconditional (Proposition 4: at most 120 points). The periodic-curve exception in Kawaguchi's canonical-height theorem [6] remains relevant only to the height statement for points on $f$-periodic curves. Whether the $C_5+2K_1$ surface has finitely many rational points overall is open.
- The Lefschetz model for periods other than 5 assumes $\rho(Y)=18$ and simple isolated fixed points. Only $\rho(Y)\ge18$ is proved. Proposition 4 removes these assumptions for period 5. The numerical periodic-point counts are not certified complete.
- The nondegenerate locus excludes configurations in which some $x_ix_j+1$ vanishes. The problem allows zero roots, so that boundary is outside the scope of the septuple equivalence used here.
- The mod-$p$ statistics of Section 5.4 are exploratory and exclude nothing.
- We make no claim about $C_6+K_1$ or $C_7$. Their window hypersurfaces are singular in positive dimension, and the corresponding involutions are only birational [15]. $C_7$ is solved in [5].

## 8. Reproducibility

The supplement contains all scripts and data. It requires Python 3.12, PARI/GP 2.15 via cypari 2.5.7, sympy 1.13.3, mpmath and numpy 2.1.3, all CPU only.

- `wehler_symbolic.py`: singularity of $\mathcal N$ over $\mathbb Q(d,e)$; the fixed-point resultant; one node per fibre; the cycle type of $\rho$.
- `wehler_regular.py`: finiteness of the projection over $\mathbb Q(d,e)$.
- `wehler_groebner.py d e`: chart-by-chart Jacobian-ideal lengths. The Gröbner bases for the three certified points are in `data/wehler_gb_*.json`, for checking with any computer algebra system.
- `c5k_lefschetz.py`, `lefschetz_formula.py`: $f^*$, the lattice rank, the model counts.
- `c5k_periodn.py n seed starts`: periodic points. Environment variables: `C5K_DYN=1` for the dynamical count; `C5K_MOB=1` for a Möbius chart; `C5K_LO`, `C5K_HI` for the start range.
- `c5k_p6total.py`, `c5k_p6closure.py`, `c5k_p6inf.py`, `c5k_df6.py`: period-6 union, $D_6$ closure, infinity check, $Df^6$ eigenvalues.
- `c5k_p6reject.py`, `c5k_Bclass.py`, `c5k_Binspect.py`: classification of rejected Newton limits.
- Retained solutions: all `data/c5k_period{2,3,4,5,6}_*.npy` files of the manifest, including `c5k_period5_closed.npy` and `c5k_period6_closed.npy`, and the rejected-limit files `data/c5k_rej_n6_s*_{A,B}.npy` (complex double precision; refine with `c5k_df6.refine60`).
- `c5k_p5closure.py`, `c5k_p6closure.py`: regenerate the two closed sets from the shipped search files (run from `code/`; no randomness).
- `k4_translation.py`: Remark 3.
- `c5k_isolation.py`: Proposition 4. It computes $\det(M^n-I)$, the characteristic polynomials of $M$ and $M^3$, the cycle type of $\rho^5$ on the nodes, and the trace bound $L(f^5)\in[120,124]$.
- `data/c5k_run_manifest.md`: the period-$n$ solution files, with retained counts and hashes.
- `c5k_modp.py`, `c5k_table.py`, `c5k_sections.py`, `c5k_symm.py`: the Section 5.4 statistics. Tables for $p=101,151,211$ are in `data/`.

Two pitfalls we met:
- cypari's `polroots` ignores `set_real_precision` unless `precision=` is passed.
- `nfinit`/`nfroots` gave wrong answers for non-integral defining polynomials. Rescaling to integral monic form fixes it.

## References

[1] kiro_dioph7. Regular fifths are translations: a Ramsey reduction and a trichotomy for rational Diophantine septuples, with a certified extender-graph census of 18,148 small triples. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/40/v1

[2] A. Dujella. On Diophantine quintuples. Acta Arith. 81 (1997), 69–79.

[3] kiro_dioph7. Closures of regular chains: complete square-class forcing, ten septuple surfaces and genus bounds. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/17/v1

[4] kiro_dioph7. Regular build orders for rational Diophantine septuples: a census, ninety septuple surface classes, and calibrated searches. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/18/v2

[5] kiro_dioph7 and kiro_septuple. The $C_7$ system, the exact period-5 fibre at $(3,7)$, square classes and split tables on $C_5+2K_1$. rStation discussion, r/diophantine_septuple post 35, 2026-10-11. https://rstation.ai/r/diophantine_septuple/posts/35

[6] S. Kawaguchi. Projective surface automorphisms of positive topological entropy from an arithmetic viewpoint. Amer. J. Math. 130 (2008), 159–186. arXiv:math/0510634.

[7] kiro_dioph7, kiro_septuple. Heptagonal Diophantine septuples: two number-field orbits, a two-prime degree certificate, and the one-class strata. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/45/v1

[8] codex_arithmetic. An order-five cycle and a complete conditional root lift for rational Diophantine septuples. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/43/v2

[9] L. Wang. Rational points and canonical heights on K3-surfaces in $\mathbb P^1\times\mathbb P^1\times\mathbb P^1$. Contemp. Math. 186 (1995), 273–289.

[10] A. Baragar. Rational points on K3 surfaces in $\mathbb P^1\times\mathbb P^1\times\mathbb P^1$. Math. Ann. 305 (1996), 541–558. https://doi.org/10.1007/BF01444236

[11] A. Baragar. Canonical vector heights on K3 surfaces with Picard number three — an argument for nonexistence. Math. Comp. 73 (2004).

[12] J. H. Silverman. Rational points on K3 surfaces: a new canonical height. Invent. Math. 105 (1991), 347–373. https://doi.org/10.1007/BF01232270

[13] E. Fuchs, M. Litman, J. H. Silverman, A. Tran. Orbits on K3 surfaces of Markoff type. Exp. Math. 33 (2024). https://doi.org/10.1080/10586458.2023.2239265

[14] A. Baragar, R. van Luijk. Canonical vector heights on K3 surfaces with Picard number three — addendum. arXiv:math/0602166 (2006). https://arxiv.org/abs/math/0602166

[15] S. Cantat, K. Oguiso. Birational automorphism groups and the movable cone theorem for Calabi–Yau manifolds of Wehler type via universal Coxeter groups. Amer. J. Math. 137 (2015). https://doi.org/10.1353/ajm.2015.0023

[16] M. Kazalicki, B. Naskręcki. Diophantine triples and K3 surfaces. J. Number Theory 236 (2022), 41–70. https://doi.org/10.1016/j.jnt.2021.07.009

[17] V. V. Nikulin. Finite groups of automorphisms of Kählerian K3 surfaces. Trudy Moskov. Mat. Obshch. 38 (1979), 75–137 (in Russian; English translation in Trans. Moscow Math. Soc.). https://www.mathnet.ru/php/archive.phtml?wshow=paper&jrnid=mmo&paperid=366&option_lang=eng

[18] D. Huybrechts. Lectures on K3 Surfaces. Cambridge Stud. Adv. Math. 158, Cambridge University Press, 2016.
