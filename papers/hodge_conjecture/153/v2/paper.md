# Isogeny graphs with dense phases and the projected pseudoeffective cone of Kummer and singular K3 squares

**lelong_ridge**

## 1. Introduction

Let $X$ be a projective K3 surface with transcendental lattice $T = T(X)_{\mathbb Q}$ and $E = \mathrm{End}_{\mathrm{Hdg}}(T)$, a totally real or CM field by Zarhin [6]. In [1] we showed that on $X\times X$ the strongly positive cone can be strictly larger than the pseudoeffective cone when the totally real part $E_0$ of $E$ is not $\mathbb Q$ [1, Thm A], with an instance on the Kummer surface of $\mathbb C/\mathbb Z[i]\times\mathbb C/\mathbb Z[\sqrt{-2}]$ [1, Rem. 5.3]. The obstruction there is Galois-theoretic: a strongly positive class can fail to stay strongly positive after conjugation by some $\tau\in\mathrm{Aut}(\mathbb C)$. This led to the cone $\mathrm{GStrong}^2$ of classes whose conjugates are all strongly positive, and to the question of when $\mathrm{Psef}^2 = \mathrm{GStrong}^2$ [1, Question 6.2]. In [2, Thm C] we answered the question on the slice of classes acting on $T$ by rational scalars, on every projective K3 surface.

This paper treats classes acting on $T$ by arbitrary elements of $E$. A class $\gamma$ on $X\times X$ has coordinates $\pi(\gamma) = (x_1, x_2, u)$: the degrees of the two projections and the element $u\in E\otimes\mathbb R$ by which $\gamma$ acts on $T$. Every class in $\mathrm{GStrong}^2$, and so every pseudoeffective class, has $\pi(\gamma)$ in

$$
K=\{(x_1,x_2,u): x_1\ge0,\ x_2\ge0,\ |s(u)|^2\le x_1x_2\ \text{for every embedding } s:E\to\mathbb C\}
$$

(Proposition 3.1). Theorem E gives a criterion for the converse: if effective surfaces with $|s(u)|^2 = x_1x_2$ have rays dense among the extreme rays of $K$, then the interior of $K$ lies in $\pi(\mathrm{Psef}^2)$, and every rational class $\beta$ with $\pi(\beta)$ in the interior of $K$ has $\beta + yH$ the class of an effective $\mathbb Q$-cycle for $y$ large, where $H = h\boxtimes h$ for an ample $h$.

**Qualifications.** The results concern the projection $\pi$, which forgets the $\mathrm{NS}\otimes\mathrm{NS}$ coordinate; that coordinate is absorbed by $yH$ for $y$ large and is otherwise not controlled. The statements are eventual in $y$. On the boundary of $K$ we prove only that equality rays are attained.

The criterion holds when the dominant rational self-maps of $X$ act on $H^{2,0}$ with phases dense in the unit torus of $E$ (Proposition 4.1). We verify it for $X = \mathrm{Km}(E_1\times E_2)$ with $E_1, E_2$ non-isogenous CM elliptic curves (Proposition 5.1) and, through the Shioda–Inose structure, for every singular K3 surface (Proposition 5.4). On $\mathrm{Km}(\mathbb C/\mathbb Z[i]\times\mathbb C/\mathbb Z[\sqrt{-2}])$ this gives a K3 square on which $\mathrm{Psef}^2\ne\mathrm{Strong}^2$, while $\mathrm{Psef}^2$ and $\mathrm{GStrong}^2$ agree on every family $\beta + yH$ with $y$ large and $\pi(\beta)$ off the boundary of $K$ (Corollary 5.2). This is a positive answer to [1, Question 6.2] in that restricted form.

For totally real $E$ of degree $d\ge3$ the criterion fails for arithmetic reasons. An effective surface attaining the bound at one place has $u^2\in\mathbb Q$, so its sign pattern is a quadratic character of $E$, and at most $2d$ of the $2^d$ sign vertices of $K$ are reached this way (Proposition 6.1, which extends [1, Prop. 6.3] from odd $d$ to all $d\ge3$).

**Bearing on the Hodge conjecture.** None. The hypothesis of Theorem E already implies the Hodge conjecture for $X\times X$ (Theorem E (d)), so the theorem cannot produce new cases. For CM $E$ the conjecture is known by Buskin's theorem [8] (Remark 2.2). For totally real $E$ of degree $d\ge3$ the hypothesis fails (Proposition 6.1). For $d = 2$ it would require an equality cycle with $u\notin\mathbb Q$, which by itself proves the conjecture for $X\times X$ (Question 6.2). The open cases for K3 squares have $E$ totally real, $E\ne\mathbb Q$, outside the known families [12, 13, 14, 15]. Constructing cycles with irrational $u$ there is the missing step, and this paper does not supply it.

The supplement checks the equality property of 378 surfaces on $\mathrm{Km}(\mathbb C/\mathbb Z[i]\times\mathbb C/\mathbb Z[\sqrt{-2}])^2$ exactly and gives exact nonnegative decompositions of three interior targets, including one of mixed sign at the two real places of $E_0$.

## 2. Setup

Let $X$ be a projective K3 surface, $T = T(X)_{\mathbb Q} = \mathrm{NS}(X)_{\mathbb Q}^\perp\subset H^2(X,\mathbb Q)$ and $E = \mathrm{End}_{\mathrm{Hdg}}(T)$. By Zarhin [6], $T$ is an irreducible Hodge structure and $E$ is a totally real field or a CM field. For $e\in E$ the adjoint of $e$ for the intersection form is $\bar e$, where $\bar e = e$ if $E$ is totally real and $\bar e$ is complex conjugation if $E$ is CM [6]. Let $\sigma$ be a nonzero holomorphic 2-form. The line $H^{2,0} = \mathbb C\sigma$ is preserved by $E$, so there is an embedding $s_0\colon E\to\mathbb C$ with $e\sigma = s_0(e)\sigma$. Let $S$ be a set of embeddings $E\to\mathbb C$ containing one from each pair $\{s,\bar s\}$; so $|S| = d = [E:\mathbb Q]$ if $E$ is totally real and $|S| = d_0 = [E_0:\mathbb Q]$ if $E$ is CM with totally real subfield $E_0$. Put $E_{\mathbb R} = E\otimes\mathbb R$ and extend each $s\in S$ $\mathbb R$-linearly to $E_{\mathbb R}$. The map $E_{\mathbb R}\to\prod_{s\in S}\mathbb C$, $u\mapsto(s(u))_s$, identifies $E_{\mathbb R}$ with $\mathbb R^d$ or $\mathbb C^{d_0}$.

We use the conventions of [2, §2]. $P_1 = [\mathrm{pt}\times X]$, $P_2 = [X\times\mathrm{pt}]$, $H = h\boxtimes h$ for an ample class $h$, and a class $\beta\in H^4(X\times X)$ acts by $\beta_* = p_{2*}(\beta\cdot p_1^*(\cdot))$. Write $x_1 = \beta\cdot P_2$ and $x_2 = \beta\cdot P_1$. By the Künneth formula and Zarhin's theorem,

$$
\operatorname{Hdg}^4(X\times X)_{\mathbb Q}=\mathbb Q P_1\oplus\mathbb Q P_2\oplus(\mathrm{NS}\otimes\mathrm{NS})_{\mathbb Q}\oplus(T\otimes T)^{\mathrm{Hdg}},\qquad (T\otimes T)^{\mathrm{Hdg}}\cong E ,
$$

where $[u]\in(T\otimes T)^{\mathrm{Hdg}}$ denotes the class whose correspondence acts by $u$ on $T$ and by $0$ on $\mathrm{NS}\oplus H^0\oplus H^4$. A class $\beta = x_1P_1 + x_2P_2 + N + [u]$ with $u\in E_{\mathbb R}$ acts on $H^{2,0}$ by $t_\beta = s_0(u)$. Let $N^2 = N^2(X\times X)_{\mathbb R}$ be the real span of classes of algebraic cycles. By [2, Lemma 2.1] (see also Lieberman [11]), numerical and homological equivalence agree on $X\times X$. Put

$$
\pi(\beta)=(x_1,x_2,u)\in\mathbb R^2\times E_{\mathbb R},\qquad K=\{(x_1,x_2,u): x_1\ge0,\ x_2\ge0,\ |s(u)|^2\le x_1x_2\ \text{for all } s\in S\}.
$$

Since $H\cdot P_1 = H\cdot P_2 = 0$ and $H\in\mathrm{NS}\otimes\mathrm{NS}$, $\pi(H) = 0$. The map $\pi$ forgets the $\mathrm{NS}\otimes\mathrm{NS}$ coordinate. Rational classes have $\pi$ in $\mathbb Q^2\times E$. Call a point of $K$ with $x_1x_2 > 0$ and $|s(u)|^2 = x_1x_2$ for every $s\in S$ an *equality point*. Let $U = \{u\in E_{\mathbb R} : |s(u)| = 1\text{ for all }s\in S\}$, a torus $(S^1)^{d_0}$ in the CM case and the finite set $\{\pm1\}^d$ in the totally real case. The ray of an equality point $(x_1, x_2, u)$ is determined by its *slope* $x_1/x_2\in\mathbb R_{>0}$ and its *phase* $u/\sqrt{x_1x_2}\in U$, and every pair (slope, phase) occurs.

**Lemma 2.1.** $K$ is a closed convex cone. It is the convex cone generated by $\pi(P_1) = (1, 0, 0)$, $\pi(P_2) = (0, 1, 0)$ and the equality points. Its interior is $\{x_1 > 0,\ x_2 > 0,\ |s(u)|^2 < x_1x_2\text{ for all }s\}$ and is nonempty. Every equality ray is an extreme ray of $K$.

*Proof.* The function $(x_1, x_2)\mapsto\sqrt{x_1x_2}$ is concave on $\mathbb R_{\ge0}^2$, so each condition $|s(u)|\le\sqrt{x_1x_2}$ defines a closed convex cone. Let $(x_1, x_2, u)\in K$. If $x_1x_2 = 0$, then $u = 0$ and the point is $x_1\pi(P_1) + x_2\pi(P_2)$. Otherwise put $r = \sqrt{x_1x_2}$. Then $u/r$ lies in the product $D$ of closed unit discs (or intervals $[-1, 1]$) in the coordinates $s(u)$. A product of compact convex sets is the convex hull of the product of their sets of extreme points, so $D$ is the convex hull of $U$. Writing $u/r = \sum_k\mu_k\zeta_k$ with $\zeta_k\in U$, $\mu_k\ge0$ and $\sum_k\mu_k = 1$ gives $(x_1, x_2, u) = \sum_k\mu_k(x_1, x_2, r\zeta_k)$, a combination of equality points. The description of the interior is immediate, and $(1, 1, 0)$ lies in it. For extremality, let $w = (x_1, x_2, u)$ be an equality point and $w = p + p'$ with $p = (a_1, a_2, v)$, $p' = (a_1', a_2', v')$ in $K$. For each $s$, $\sqrt{x_1x_2} = |s(u)|\le|s(v)| + |s(v')|\le\sqrt{a_1a_2} + \sqrt{a_1'a_2'}\le\sqrt{x_1x_2}$, the last step by the Cauchy–Schwarz inequality. Equality in Cauchy–Schwarz makes $(a_1, a_2)$ and $(a_1', a_2')$ nonnegative multiples of $(x_1, x_2)$, say $\mu(x_1, x_2)$ and $\mu'(x_1, x_2)$. Equality in the other two steps gives $s(v) = \mu\,s(u)$ for every $s$. So $p = \mu w$. ∎

For $\tau\in\mathrm{Aut}(\mathbb C)$, conjugation of cycles induces a real-linear isomorphism $\tau\colon N^2(X\times X)_{\mathbb R}\to N^2(X^\tau\times X^\tau)_{\mathbb R}$ that preserves intersection numbers [1, §6.1]. Following [1, §6.1], let $\mathrm{Strong}_{\mathrm{cur}}^2$ denote the closed cone of classes of closed strongly positive currents of bidimension $(2,2)$, and

$$
\operatorname{GStrong}^2(X\times X)=\{\gamma\in N^2 : \tau(\gamma)\in \operatorname{Strong}^2_{\mathrm{cur}}(X^\tau\times X^\tau)\ \text{for every }\tau\in\operatorname{Aut}(\mathbb C)\}.
$$

Then $\mathrm{Psef}^2\subseteq\mathrm{GStrong}^2\subseteq\mathrm{Strong}_{\mathrm{cur}}^2\cap N^2$ [1, Prop. 6.1].

**Remark 2.2 (the Hodge conjecture for CM squares).** If $E$ is CM, every Hodge class on $X\times X$ is algebraic. This is Huybrechts [16, Cor. 0.4(ii) and Rem. 3.3], deduced from Buskin's theorem [8], and it is recalled by Varesco [15]. We include the short argument because Section 4 uses the same span property. Indeed, $P_1$, $P_2$ and $\mathrm{NS}\otimes\mathrm{NS}$ are algebraic. For $u\in E$ with $u\bar u = 1$, $u$ is an isometry of $T$, and $u\oplus\mathrm{id}_{\mathrm{NS}}$ is a rational Hodge isometry of $H^2(X,\mathbb Q)$, which is algebraic by Buskin [8]. Its $T\otimes T$ component $[u]$ is then algebraic, because the Künneth projectors onto $\mathrm{NS}$ and $T$ are algebraic [2, §2]. The $\mathbb Q$-span $L$ of the elements of norm one is closed under products, so it is a subfield of $E$. Write $E = E_0(\sqrt{-\delta})$ with $\delta\in E_0$ totally positive. For nonzero $a\in E_0$, $u_a = (a + \sqrt{-\delta})/(a - \sqrt{-\delta})$ has norm one and $u_a\ne-1$, so $L$ contains $(u_a - 1)/(u_a + 1) = \sqrt{-\delta}/a$. With $a = 1$ this gives $\sqrt{-\delta}\in L$. The products $\sqrt{-\delta}\cdot\sqrt{-\delta}/a = -\delta/a$ then run over all of $E_0^*$, so $L\supseteq E_0(\sqrt{-\delta}) = E$. For totally real $E$ the only elements with $u^2 = 1$ are $\pm1$, and Buskin's theorem gives nothing beyond the rational classes. So the open cases of the Hodge conjecture for K3 squares all have $E$ totally real and $E\ne\mathbb Q$. Several such families are known to satisfy it [12, 13, 14, 15].

## 3. The necessary condition and equality surfaces

**Proposition 3.1.** If $\gamma\in\mathrm{GStrong}^2(X\times X)$, then $\pi(\gamma)\in K$. In particular $\pi(\mathrm{Psef}^2)\subseteq\pi(\mathrm{GStrong}^2)\subseteq K$, and for $\beta\in N^2$ with $\pi(\beta)\notin K$, no class $\beta + yH$ lies in $\mathrm{GStrong}^2$ or in $\mathrm{Psef}^2$.

*Proof.* Write $\gamma = x_1P_1 + x_2P_2 + N + [u]$ with $u\in E_{\mathbb R}$. Let $s\colon E\to\mathbb C$ be an embedding. The isomorphism $s\circ s_0^{-1}\colon s_0(E)\to s(E)$ extends to some $\tau\in\mathrm{Aut}(\mathbb C)$. For an algebraic cycle $Z$ on $X\times X$ acting on $T$ by $u_Z\in E$, the conjugate $Z^\tau$ acts on $H^0(X^\tau,\Omega^2)$ by $\tau(s_0(u_Z)) = s(u_Z)$, by the comparison between Betti and algebraic de Rham cohomology [1, Rem. 3.4]. By real-linearity, $\tau(\gamma)$ has intersection numbers $x_1, x_2$ with the fibre classes of $X^\tau\times X^\tau$ and acts on $H^{2,0}(X^\tau)$ by $s(u)$, with $s$ extended $\mathbb R$-linearly to $E_{\mathbb R}$. Let $\sigma'$ be a holomorphic 2-form on $X^\tau$, put $\Sigma_\lambda = p_1^*\sigma' + \lambda\,p_2^*\sigma'$ for $\lambda\in\mathbb C$ and $c' = \int\sigma'\wedge\bar\sigma' > 0$. The form $\Sigma_\lambda\wedge\bar\Sigma_\lambda$ is a semipositive $(2,2)$-form, so it pairs nonnegatively with every closed strongly positive current. As in [2, Lemma 2.2] (after Lehmann and Ottem [5, proof of Thm 3.5]),

$$
\tau(\gamma)\cdot[\Sigma_\lambda\wedge\bar\Sigma_\lambda]=c'\bigl(x_2+2\,\mathrm{Re}(\lambda\,\overline{s(u)})+|\lambda|^2x_1\bigr)\ge0\qquad(\lambda\in\mathbb C).
$$

Taking $\lambda = 0$, $|\lambda|\to\infty$ and $\lambda = -r\,s(u)/|s(u)|$ with $r > 0$ gives $x_2\ge0$, $x_1\ge0$ and $|s(u)|^2\le x_1x_2$. The second statement follows from $\mathrm{Psef}^2\subseteq\mathrm{GStrong}^2$ [1, Prop. 6.1] and $\pi(H) = 0$. ∎

The proof uses only the pairing with the forms $\Sigma_\lambda\wedge\bar\Sigma_\lambda$, on each conjugate. It does not use the comparison with $\mathrm{Strong}^2$ of [1, Prop. 4.2], which is proved there for self-adjoint $u$.

**Lemma 3.2 (equality at one place).** Let $\beta$ be a class with rational coordinates $x_1, x_2\in\mathbb Q$ and $u\in E$. If $|s(u)|^2 = x_1x_2$ for one embedding $s$, then $|s'(u)|^2 = x_1x_2$ for every embedding $s'$. If $E$ is CM, then $u\bar u = x_1x_2$. If $E$ is totally real, then $u^2 = x_1x_2$, so $\mathbb Q(u)$ is $\mathbb Q$ or a real quadratic subfield of $E$.

*Proof.* Complex conjugation on a CM field commutes with every embedding, so $|s(u)|^2 = s(u\bar u)$ in the CM case, and $|s(u)|^2 = s(u^2)$ in the totally real case. Since $s$ is injective, $s(u\bar u - x_1x_2) = 0$ (resp. $s(u^2 - x_1x_2) = 0$) gives $u\bar u = x_1x_2$ (resp. $u^2 = x_1x_2$), and this holds at every $s'$. ∎

So a single cycle that attains the bound of Proposition 3.1 at one place attains it at all places. For self-adjoint $u$, which is every $u$ when $E$ is totally real, equality gives $u^2\in\mathbb Q$, not $u\in\mathbb Q$. For example, on the Kummer surface of [1, Rem. 5.3] the graph of the degree-2 self-map $g$ has $u\in E_0$ with $u^2 = 2$. We call an effective integral cycle $Z$ of dimension 2 on $X\times X$ an *equality cycle* if $\pi([Z])$ is an equality point. Every component of an equality cycle has $\pi$ on the same ray or $\pi = 0$, because each component lies in $K$ (Proposition 3.1) and an equality ray is extreme in $K$ (Lemma 2.1).

## 4. The criterion

**Theorem E.** Let $X$ be a projective K3 surface. Suppose that the rays of the points $\pi([Z])$, for $Z$ an equality cycle on $X\times X$, are dense in the set of equality rays, which is parametrised by slope and phase as $\mathbb R_{>0}\times U$. Then:

(a) The interior of $K$ lies in $\pi(\mathrm{Psef}^2(X\times X))$, and the closures of $\pi(\mathrm{Psef}^2)$ and $\pi(\mathrm{GStrong}^2)$ are both equal to $K$.

(b) Let $\beta\in N^2(X\times X)_{\mathbb R}$ with $\pi(\beta)$ in the interior of $K$. Then $\beta + yH\in\mathrm{Psef}^2$ for all $y$ large. If $\beta$ is a rational class, there is $y_0$ such that $\beta + yH$ is the class of an effective $\mathbb Q$-cycle for every rational $y\ge y_0$.

(c) For $\beta\in N^2(X\times X)_{\mathbb R}$ with $\pi(\beta)\notin\partial K$, either $\beta + yH$ lies in $\mathrm{Psef}^2$ and in $\mathrm{GStrong}^2$ for all $y$ large, or it lies in neither for any $y$.

(d) Every Hodge class on $X\times X$ is algebraic.

*Proof.* Let $C\subseteq\mathbb R^2\times E_{\mathbb R}$ be the convex cone generated by $\pi(P_1)$, $\pi(P_2)$ and the points $\pi([Z])$ for equality cycles $Z$. It is contained in $\pi(\mathrm{Psef}^2)$, which is a convex cone. Let $B = K\cap\{x_1 + x_2 = 1\}$, a compact convex set. The equality points with $x_1 + x_2 = 1$ are $w(t,\zeta) = (t,\ 1 - t,\ \sqrt{t(1 - t)}\,\zeta)$ for $t\in(0, 1)$ and $\zeta\in U$, and $(t,\zeta)\mapsto w(t,\zeta)$ is a homeomorphism onto its image. By hypothesis the normalised points $\pi([Z])/(x_1 + x_2)$ form a dense subset $D$ of this image. By Lemma 2.1, $B$ is the convex hull of $\pi(P_1)$, $\pi(P_2)$ and all $w(t,\zeta)$. Each of these lies in the closure of $D\cup\{\pi(P_1), \pi(P_2)\}$, so $B$ lies in the closure of the convex hull of $D\cup\{\pi(P_1), \pi(P_2)\}$, which is contained in $\mathrm{cl}\,C$. Hence $K\subseteq\mathrm{cl}\,C\subseteq K$.

A convex set in a finite-dimensional real vector space has the same interior as its closure [7, Thm 6.3]. So $\mathrm{int}\,K = \mathrm{int}\,C\subseteq\pi(\mathrm{Psef}^2)$. Since $\pi(\mathrm{Psef}^2)\subseteq\pi(\mathrm{GStrong}^2)\subseteq K$ (Proposition 3.1) and $K$ is closed, both closures equal $K$. This is (a).

For (b), let $w = \pi(\beta)\in\mathrm{int}\,K = \mathrm{int}\,C$. Choose finitely many points of $C$ whose convex hull contains a neighbourhood of $w$, and write each as a finite nonnegative combination of generators of $C$. The finitely many generators $F$ used in this way span a cone with $w$ in its interior. The generators have rational coordinates: $\pi(P_1), \pi(P_2)\in\mathbb Q^2\times\{0\}$, and $\pi([Z])\in\mathbb Z^2\times E$ because $[Z]$ is a rational Hodge class. So $w = \sum_{g\in F}c_g\,g$ with $c_g\ge0$. If $\beta$ is rational, then $w\in\mathbb Q^2\times E$, and the set of $c\in\mathbb R_{\ge0}^F$ with $\sum_g c_g\,g = w$ is a nonempty polyhedron cut out by equations and inequalities with rational coefficients. Its vertices are rational, so we may take every $c_g\in\mathbb Q_{\ge0}$. Let $\gamma$ be the corresponding nonnegative combination of the cycles $Z$ and of $P_1, P_2$ (a $\mathbb Q$-cycle when $\beta$ is rational). Then $\beta - [\gamma]$ lies in $N^2$ and has $\pi = 0$, so $x_1 = x_2 = 0$ and $u = 0$. By the decomposition of Section 2, $\beta - [\gamma] = M\in(\mathrm{NS}\otimes\mathrm{NS})_{\mathbb R}$, rational when $\beta$ is. By the proof of [2, Thm C], $M + yH$ is the class of an effective $\mathbb R$-cycle for $y\ge\varepsilon^{-2}\sum_{i,j}|M_{ij}|$, for a fixed $\varepsilon$ depending only on $h$ and a basis of $\mathrm{NS}$, and of an effective $\mathbb Q$-cycle when $M$ is rational and $y$ is rational. So $\beta + yH = [\gamma] + (M + yH)$ is as claimed.

For (c): if $\pi(\beta)\in\mathrm{int}\,K$, then $\beta + yH\in\mathrm{Psef}^2\subseteq\mathrm{GStrong}^2$ for $y$ large by (b). If $\pi(\beta)\notin K$, then $\pi(\beta + yH) = \pi(\beta)\notin K$, and Proposition 3.1 shows that $\beta + yH$ lies in neither cone, for every $y$.

For (d): the Hodge classes are spanned by $P_1$, $P_2$, $\mathrm{NS}\otimes\mathrm{NS}$ and the classes $[u]$ for $u\in E$. Given $u\in E$, choose a rational $x > \max_s|s(u)|$. Then $\beta = xP_1 + xP_2 + [u]$ is a rational Hodge class with $\pi(\beta)\in\mathrm{int}\,K$. The first part of the proof of (b) applies to it and gives an effective $\mathbb Q$-cycle $\gamma$ with $\pi([\gamma]) = \pi(\beta)$. Then $\beta - [\gamma]$ is a Hodge class with $x_1 = x_2 = 0$ and $u = 0$, so it lies in $(\mathrm{NS}\otimes\mathrm{NS})_{\mathbb Q}$ and is algebraic. So $\beta$ and $[u]$ are algebraic. ∎

Part (d) shows what the hypothesis costs. For CM $E$ it is consistent with Remark 2.2 and adds nothing. For totally real $E\ne\mathbb Q$, the hypothesis can hold only on squares for which the Hodge conjecture holds, and it would need equality cycles at every sign vertex of $K$. Proposition 6.1 shows that this is impossible for $d\ge3$.

**Comparison with abelian varieties.** Density arguments of this kind go back to Debarre, Ein, Lazarsfeld and Voisin [17, §2, Thm A]. On $B = E'^n$ for an elliptic curve $E'$ with CM, they show $\mathrm{Psef}^k(B) = \mathrm{Strong}^k(B)$. The 1-forms $\sum_i s_i\,dz_i$ with $s_i\in\mathrm{End}(E')$ have dense directions, the pullbacks of a point under the corresponding homomorphisms $B\to E'$ realise the generators $i\,\ell\wedge\bar\ell$ of $\mathrm{Strong}^1$, and products of pseudoeffective classes on an abelian variety are pseudoeffective. On a K3 square there are no such homomorphisms and no product rule. Theorem E replaces them with equality cycles, convexity and absorption by $H$, and as a result it controls only the projection $\pi$ and only for $y$ large.

**Dense phases from self-maps.** Let $g\colon X\dashrightarrow X$ be a dominant rational map. Let $b\colon\tilde X\to X$ resolve the indeterminacy of $g$ and put $\tilde g = g\circ b$. The map $g^* = b_*\tilde g^*$ on $H^2(X,\mathbb Q)$ is the action of the transpose of the closure of the graph [1, Rem. 5.3]. It is a morphism of Hodge structures that preserves $\mathrm{NS}$, and so does its adjoint $g_* = \tilde g_*b^*$. So $g^*$ preserves $T = \mathrm{NS}^\perp$ and acts there by an element $\lambda_g\in E$, the *multiplier* of $g$, with $g^*\sigma = s_0(\lambda_g)\sigma$. Since $\int g^*\sigma\wedge g^*\bar\sigma = \deg g\int\sigma\wedge\bar\sigma$, we have $|s_0(\lambda_g)|^2 = \deg g$.

**Proposition 4.1.** If the set $\{\lambda_g/\sqrt{\deg g}\}$ is dense in $U$, as $g$ runs over the dominant rational self-maps of $X$, then the hypothesis of Theorem E holds.

*Proof.* We use the elliptic family of [2, §3] (after [3, Thm A] and [4, §6.1]): a smooth projective surface $Y$, a generically finite morphism $\varphi\colon Y\to X$ of degree $e$, a resolution $\rho\colon\tilde Y\to Y$ on which the multiplication maps $f_m = [m]\circ\rho$ are morphisms, and the identities $f_m^*\omega_Y = m\,\rho^*\omega_Y$, $f_{m*}\rho^*[\omega_Y] = m[\omega_Y]$ of [2, Lemma 3.1], where $\omega_Y = \varphi^*\sigma$. Fix $g$ and nonzero integers $a, b$. After a further resolution of $\tilde Y$ (which does not change these identities), the map $\psi = (\varphi\circ f_b,\ g\circ\varphi\circ f_a)\colon\tilde Y\to X\times X$ is a morphism. Its first component has degree $b^2e$ and its second has degree $a^2e\deg g$, so $\psi$ is generically finite onto its image and $Z = \psi_*[\tilde Y]$ is a positive multiple of an irreducible surface with $x_2 = b^2e$ and $x_1 = a^2e\deg g$. The correspondence of $Z$ sends $\sigma$ to $(g\circ\varphi\circ f_a)_*(\varphi\circ f_b)^*\sigma = b\cdot ae\cdot g_*\sigma$. Since $b^*b_*$ is the identity on holomorphic 2-forms, $g_*g^*\sigma = \tilde g_*\tilde g^*\sigma = \deg g\cdot\sigma$ and $g_*\sigma = (\deg g/s_0(\lambda_g))\,\sigma = s_0(\bar\lambda_g)\sigma$. On $H^{2,0}$, pushforward along a generically finite morphism is the trace of forms, which may be computed on a dense open set, so $(g\circ\varphi\circ f_a)_* = g_*\varphi_*f_{a*}$ there. So $Z$ acts on $H^{2,0}$ by $abe\,s_0(\bar\lambda_g)$, and as in [2, Lemma 3.2] it acts on $T$ by $u = abe\,\bar\lambda_g$. Then $|s_0(u)|^2 = a^2b^2e^2\deg g = x_1x_2$, so $Z$ is an equality cycle by Lemma 3.2. Its slope is $a^2\deg g/b^2$ and its phase is $\mathrm{sign}(ab)\,\bar\lambda_g/\sqrt{\deg g}$. The phases $\bar\lambda_g/\sqrt{\deg g}$ are dense in $U$ because complex conjugation is a homeomorphism of $U$. For fixed $g$ the slopes $a^2\deg g/b^2$ are dense in $\mathbb R_{>0}$. Hence the rays are dense in $\mathbb R_{>0}\times U$. ∎

## 5. Kummer squares and singular K3 surfaces

### 5.1 Kummer surfaces of products of CM elliptic curves

Let $E_1, E_2$ be elliptic curves with CM by orders $O_1, O_2$ in imaginary quadratic fields $K_1\ne K_2$. Then $E_1$ and $E_2$ are not isogenous. Let $A = E_1\times E_2$, let $p\colon A\dashrightarrow X = \mathrm{Km}(A)$ be the rational quotient map of degree 2, and let $\sigma_A = dz_1\wedge dz_2$ and $\sigma_X$ with $p^*\sigma_X = \sigma_A$. Since $\mathrm{NS}(A)_{\mathbb Q} = \mathbb Qe_1\oplus\mathbb Qe_2$, $T(A) = H^1(E_1)\otimes H^1(E_2)$ has dimension 4, and $p_*$ identifies $T(A)_{\mathbb Q}$ with $T(X)_{\mathbb Q}$ and multiplies the form by 2 [1, Rem. 5.3]. The field $K_1\otimes K_2$ acts on $T(A)$ by Hodge endomorphisms and has degree $4 = \dim T$, so $E = K_1\otimes K_2$, a CM field of degree 4 with $E_0 = \mathbb Q(\sqrt{d_1d_2})$ when $K_j = \mathbb Q(\sqrt{-d_j})$. Its two embeddings up to conjugation are $s_0 = \iota_1\otimes\iota_2$ and $s_1 = \iota_1\otimes\bar\iota_2$, where $\iota_j\colon K_j\to\mathbb C$ is the embedding given by the action on $dz_j$.

For nonzero $\alpha_k\in O_1$ and $\beta_k\in O_2$ ($k = 1, 2$), put $\psi_k = (\alpha_k, \beta_k)\in\mathrm{End}(A)$. The map $\Phi = (p\circ\psi_1, p\circ\psi_2)\colon A\dashrightarrow X\times X$ becomes a morphism after blowing up the finitely many points of $\psi_1^{-1}(A[2])\cup\psi_2^{-1}(A[2])$. Let $Z(\psi_1,\psi_2) = \Phi_*[\tilde A]$ be the pushforward of the fundamental class of the blow-up $\tilde A$.

**Proposition 5.1.** $Z = Z(\psi_1,\psi_2)$ is an equality cycle with

$$
x_2=2|\alpha_1\beta_1|^2,\qquad x_1=2|\alpha_2\beta_2|^2,\qquad u=2\,(\alpha_1\bar\alpha_2)\otimes(\beta_1\bar\beta_2)\in K_1\otimes K_2 .
$$

The rays of these cycles are dense in $\mathbb R_{>0}\times U$. So $X$ satisfies the hypothesis of Theorem E.

*Proof.* The first projection of $Z$ has degree $\deg(p\circ\psi_1) = 2\deg\psi_1 = 2|\alpha_1|^2|\beta_1|^2$, and similarly for the second. So $\Phi$ is generically finite onto its image, $Z$ is a positive multiple of an irreducible surface, and $x_1, x_2$ are as stated. On forms, $\psi_k^*\sigma_A = \iota_1(\alpha_k)\iota_2(\beta_k)\sigma_A$, and $\psi_{k*}\sigma_A = \deg\psi_k\,(\iota_1(\alpha_k)\iota_2(\beta_k))^{-1}\sigma_A = \iota_1(\bar\alpha_k)\iota_2(\bar\beta_k)\sigma_A$. The correspondence of $Z$ sends $\sigma_X$ to $(p\circ\psi_2)_*(p\circ\psi_1)^*\sigma_X = p_*\psi_{2*}\psi_1^*\sigma_A = 2\,\iota_1(\alpha_1\bar\alpha_2)\,\iota_2(\beta_1\bar\beta_2)\,\sigma_X$. As in [2, Lemma 3.2], $Z$ acts on $T(X)$ by the element of $E$ with this image under $s_0$, which is $u$. Then $s_1(u) = 2\,\iota_1(\alpha_1\bar\alpha_2)\,\iota_2(\bar\beta_1\beta_2)$, and $|s_0(u)|^2 = |s_1(u)|^2 = 4|\alpha_1\alpha_2\beta_1\beta_2|^2 = x_1x_2$.

Put $q = \alpha_1/\alpha_2\in K_1^*$ and $r = \beta_1/\beta_2\in K_2^*$. Then $x_1/x_2 = |\iota_1(q)\iota_2(r)|^{-2}$, and the phase of $Z$ is $(e^{i(\theta+\phi)}, e^{i(\theta-\phi)})$ at $(s_0, s_1)$, where $\theta = \arg\iota_1(q)$ and $\phi = \arg\iota_2(r)$. Every pair $(q, r)\in K_1^*\times K_2^*$ occurs, because $q$ and $r$ are ratios of elements of the orders. The map $\mathbb C^*\times\mathbb C^*\to\mathbb R_{>0}\times(S^1)^2$, $(z, w)\mapsto(|zw|^{-2}, zw/|zw|, z\bar w/|z\bar w|)$, is continuous and surjective. Since $\iota_j(K_j^*)$ is dense in $\mathbb C^*$, the image of $K_1^*\times K_2^*$ is dense in $\mathbb R_{>0}\times U$. ∎

The supplement checks the equality $|s(u)|^2 = x_1x_2$ exactly for 378 cycles $Z(\psi_1,\psi_2)$ on $\mathrm{Km}(\mathbb C/\mathbb Z[i]\times\mathbb C/\mathbb Z[\sqrt{-2}])$, and it writes three interior targets exactly as nonnegative rational combinations of such cycles and $P_1, P_2$. One target, $x_1 = x_2 = 1$ and $u = \sqrt2/2\in E_0$, has $s_0(u) > 0 > s_1(u)$. It is a combination of four cycles with coefficient $1/48$ each. By contrast, when $E$ is totally real of odd degree, a cone generated by $P_1, P_2$ and finitely many surfaces contains no vertex of $K$ of mixed sign [1, Prop. 6.3]. Here Proposition 5.1 and Theorem E (a) put every point of $K$, mixed vertices included, in the closure of $\pi(\mathrm{Psef}^2)$.

**Corollary 5.2.** Let $X = \mathrm{Km}(\mathbb C/\mathbb Z[i]\times\mathbb C/\mathbb Z[\sqrt{-2}])$. Then $\mathrm{Psef}^2(X\times X)\ne\mathrm{Strong}^2(X\times X)$, and $\mathrm{GStrong}^2(X\times X)\ne\mathrm{Strong}_{\mathrm{cur}}^2(X\times X)\cap N^2$. For every $\beta\in N^2(X\times X)_{\mathbb R}$ with $\pi(\beta)\notin\partial K$, $\beta + yH$ lies in $\mathrm{Psef}^2$ for all large $y$ if and only if it lies in $\mathrm{GStrong}^2$ for all large $y$. Every Hodge class on $X\times X$ is algebraic.

*Proof.* Let $g$ be the rational self-map of $X$ induced by $[i]\times[\sqrt{-2}]$ and $\beta_g = [1 + g^*]_T + P_1 + P_2$. By [1, Rem. 5.3], $\beta_g + yH$ lies in the interior of $\mathrm{Strong}^2$ for $y$ large and is not pseudoeffective. Here $\pi(\beta_g) = (1, 1, 1 + \lambda_g)$ with $s_0(1 + \lambda_g) = 1 - \sqrt2$ and $s_1(1 + \lambda_g) = 1 + \sqrt2$, so $|s_1|^2 = 3 + 2\sqrt2 > 1$ and $\pi(\beta_g)\notin K$. By Proposition 3.1, $\beta_g + yH\notin\mathrm{GStrong}^2$ for every $y$. The remaining statements are Theorem E (c), (d) and Proposition 5.1. ∎

So on this K3 square the strongly positive cone is too large, while, apart from the boundary of $K$ and for $y$ large, conjugation accounts for the whole difference. This answers [1, Question 6.2] positively in the restricted form of Theorem E (c).

**Remark 5.3 (one CM factor).** If only $E_2$ has CM, by an order in $K_2$, and $E_1$ has none, the same construction with $\alpha_k\in\mathbb Z$ gives the hypothesis of Theorem E for $X = \mathrm{Km}(E_1\times E_2)$. Here $E = K_2$ and $d_0 = 1$. With $w = (\alpha_1/\alpha_2)\,\iota_2(\beta_1/\beta_2)$, the slope is $|w|^{-2}$ and the phase is $w/|w|$, and $w$ runs over the dense subset $\iota_2(K_2^*)$ of $\mathbb C^*$.

### 5.2 Singular K3 surfaces

**Proposition 5.4.** Let $X$ be a singular K3 surface ($\rho(X) = 20$). Then $X$ satisfies the hypothesis of Theorem E.

*Proof.* Here $T$ has dimension 2 and $E = K$ is imaginary quadratic, with $d_0 = 1$ and $U = S^1$. By Shioda and Inose [9, Thm 2], as stated in [10, Thm 7], $X$ has a Nikulin involution $\iota$ such that the minimal resolution of $X/\iota$ is $\mathrm{Km}(A)$, where $A = E_1\times E_2$ with $E_1, E_2$ isogenous elliptic curves with CM by orders in $K$. Let $q\colon X\dashrightarrow\mathrm{Km}(A)$ be the resulting rational map of degree 2. It is a finite étale double cover over the complement $V$ of the eight exceptional curves of the resolution. The involution is symplectic, so $\iota^* - 1$ kills $\sigma_X$, and its kernel on $T(X)_{\mathbb Q}$ is a sub-Hodge structure containing $\sigma_X$, hence all of $T(X)_{\mathbb Q}$ by irreducibility. So $q^*q_* = 1 + \iota^* = 2$ on $T(X)_{\mathbb Q}$.

On $\mathrm{Km}(A)\times\mathrm{Km}(A)$ the cycles $Z(\psi_1,\psi_2)$ of §5.1, with $\alpha_k, \beta_k$ nonzero elements of $\mathrm{End}(E_1)$, $\mathrm{End}(E_2)$, have $x_2 = 2|\alpha_1\beta_1|^2$, $x_1 = 2|\alpha_2\beta_2|^2$ and act on $H^{2,0}$ by $t = s_0(u) = 2\,\alpha_1\beta_1\cdot\overline{\alpha_2\beta_2}$, by the computation of Proposition 5.1 (which did not use $K_1\ne K_2$). Here $\mathrm{End}(E_j)$ is identified with an order in $K\subset\mathbb C$ through the action on $dz_j$. So they are equality cycles, and $\alpha_1\beta_1/(\alpha_2\beta_2)$ runs over a dense subset of $\mathbb C^*$, since it runs over $K^*$. Their rays are dense in $\mathbb R_{>0}\times S^1$.

Let $Z = \sum_k m_kZ_k$ be such a cycle, with $Z_k$ irreducible and $m_k > 0$. In general $Z$ is not reduced. For example, $\psi_1 = \psi_2 = \mathrm{id}$ gives $Z = 2\Delta_{\mathrm{Km}(A)}$. Each $Z_k$ dominates both factors, so it meets $V\times V$. Put $V' = q^{-1}(V)$. The map $q\times q\colon V'\times V'\to V\times V$ is finite étale of degree 4, so the flat pullback $(q\times q)^*(Z_k\cap(V\times V))$ is a reduced cycle on $V'\times V'$. Define $Z' = \sum_k m_kZ_k'$, where $Z_k'$ is the closure in $X\times X$ of $(q\times q)^*(Z_k\cap(V\times V))$, so that the multiplicities $m_k$ are kept. In the example, $Z' = 2(\Delta_X + \Gamma_\iota)$. For a general point $y$ of $\mathrm{Km}(A)$, $Z_k\cap(\{y\}\times\mathrm{Km}(A))$ lies in $\{y\}\times V$, because $Z_k\cap(\mathrm{Km}(A)\times(\mathrm{Km}(A)\setminus V))$ has dimension at most 1. Let $x\in X$ be general and $y = q(x)$. Over $x$, the fibre of $p_1$ on $Z'$ is the pullback under the étale map $\mathrm{id}\times q$ of the fibre of $p_1$ on $Z$ over $y$, which has length $x_2$. So that fibre of $Z'$ has length $2x_2$, counted with multiplicity, and $x_2' = 2x_2$. Similarly $x_1' = 2x_1$. Choose $\sigma_{\mathrm{Km}}$ with $q^*\sigma_{\mathrm{Km}} = \sigma_X$. Then $\int_X\sigma_X\wedge\bar\sigma_X = 2\int\sigma_{\mathrm{Km}}\wedge\bar\sigma_{\mathrm{Km}}$. The integral $\int[Z']\wedge p_1^*\sigma_X\wedge p_2^*\bar\sigma_X$ may be computed on the open part of $Z'$, and on it the forms are pulled back from $\mathrm{Km}(A)\times\mathrm{Km}(A)$. So this integral is $4\int[Z]\wedge p_1^*\sigma_{\mathrm{Km}}\wedge p_2^*\bar\sigma_{\mathrm{Km}}$, and $t' = 4t/2 = 2t$. So $Z'$ is an equality cycle with the same slope and phase as $Z$, and the rays of the $Z'$ are dense. ∎

Proposition 5.4 extends [2, Thm C] on singular K3 squares from rational $u$ to all $u\in K$. Since $E_0 = \mathbb Q$ here, there is no Galois obstruction on these squares, and Theorem E (b) compares $\mathrm{Psef}^2$ only with $\mathrm{GStrong}^2$.

## 6. Totally real fields and open questions

Let $E$ be totally real of degree $d$. Call a point of $K$ with $x_1 = x_2 = 1$ and $s(u) = \varepsilon_s\in\{\pm1\}$ for every $s$ a *vertex*, with sign pattern $\varepsilon = (\varepsilon_s)$. For $D = 1$ or $\mathbb Q(\sqrt D)\subseteq E$, let $\chi_D(s) = s(\sqrt D)/\sqrt D\in\{\pm1\}$.

**Proposition 6.1.** Let $E$ be totally real of degree $d\ge3$, and let $C\subseteq\mathrm{Psef}^2(X\times X)$ be the closed convex cone generated by $P_1$, $P_2$, finitely many irreducible surfaces, and any pseudoeffective classes with zero $T\otimes T$ component. Then $\pi(C)$ contains no vertex whose sign pattern differs from $\pm\chi_D$ for every $D$. Such vertices exist: at most $2d$ of the $2^d$ sign patterns have the form $\pm\chi_D$.

*Proof.* Fix a vertex with sign pattern $\varepsilon$ not of the form $\pm\chi_D$, and put $\varphi(\gamma) = \sum_s\varepsilon_s\,s(u) - c(x_1 + x_2)$ with $c$ chosen below. On $P_1$, $P_2$ and generators with zero $T\otimes T$ component, $\varphi = -c(x_1 + x_2)\le0$. Let $Z$ be one of the finitely many irreducible surfaces. If $x_1x_2 = 0$ then $u = 0$ by Proposition 3.1 and $\varphi\le0$. If $|s(u)|^2 = x_1x_2 > 0$ at some place, then by Lemma 3.2 $u^2 = x_1x_2$, so $u = r\sqrt D$ with $r\in\mathbb Q^*$ and $\mathbb Q(\sqrt D)\subseteq E$ or $D = 1$, and $s(u) = r\sqrt D\,\chi_D(s)$. Since $\varepsilon\ne\pm\chi_D$, the vectors $\varepsilon$ and $\chi_D$ differ in at least one and agree in at least one coordinate, so $|\sum_s\varepsilon_s\chi_D(s)|\le d - 2$. With $|r|\sqrt D = \sqrt{x_1x_2}\le(x_1 + x_2)/2$ this gives $\varphi\le((d - 2)/2 - c)(x_1 + x_2)$. Otherwise $|s(u)|\le\rho_Z\sqrt{x_1x_2}$ for some $\rho_Z < 1$ and all $s$, and $\varphi\le(d\rho_Z/2 - c)(x_1 + x_2)$. Let $\rho$ be the largest $\rho_Z$ (or $0$) and $c = \max((d - 2)/2,\ d\rho/2) < d/2$. Then $\varphi\le0$ on $C$, while $\varphi = d - 2c > 0$ at the vertex.

For the count, the quadratic subfields of $E$ lie in its largest multiquadratic subfield, of degree $2^k$ dividing $d$, which has $2^k - 1$ quadratic subfields. So there are at most $2\cdot2^k\le2d$ patterns $\pm\chi_D$, and $2d < 2^d$ for $d\ge3$. ∎

For $d$ odd, $E$ has no quadratic subfield, and Proposition 6.1 is [1, Prop. 6.3]. The argument of [1, §6.2] applies unchanged: a vertex as in Proposition 6.1 that lies in the closure of $\pi(\mathrm{Psef}^2)$ can only be approached by combinations of surfaces of unbounded degree, since surfaces of bounded degree have finitely many classes. In particular the phases of equality cycles lie in the finite set $\{\pm\chi_D\}\subsetneq U = \{\pm1\}^d$, so the hypothesis of Theorem E fails for every totally real $E$ of degree $d\ge3$. Whether such vertices lie in $\pi(\mathrm{Psef}^2)$ at all is open.

**Question 6.2 ($d = 2$).** Let $E = \mathbb Q(\sqrt D)$ be real quadratic. All four sign patterns have the form $\pm\chi_1$ or $\pm\chi_D$. The hypothesis of Theorem E asks for equality cycles with $u\in\mathbb Q^*\sqrt D$ and a dense set of slopes. A single equality cycle with $u\in\mathbb Q^*\sqrt D$ would already make $[\sqrt D]$ algebraic and so prove the Hodge conjecture for $X\times X$. Is there such a cycle on the real-multiplication families of Varesco [15], where the conjecture is known for the general member? On $\mathrm{Km}(\mathbb C/\mathbb Z[i]\times\mathbb C/\mathbb Z[\sqrt{-2}])$, where $E$ is CM, the graph of $g$ is an equality cycle with self-adjoint $u$ and $u^2 = 2$ [1, §6.2]. The question asks for the analogue with $E$ totally real.

**Question 6.3 (boundary).** For $X$ as in Corollary 5.2, is every point of $\partial K$ with $x_1x_2 > 0$ in $\pi(\mathrm{Psef}^2)$? Theorem E gives the dense set of equality rays realised by cycles, but not the irrational slopes or phases.

**Question 6.4 (other CM K3 surfaces).** Let $X$ have CM by $E$ with $E_0\ne\mathbb Q$ and no dominant rational map to a Kummer surface. Do the multipliers $\lambda_g/\sqrt{\deg g}$ of dominant rational self-maps have dense phases in $U$? Arithmetic does not forbid it: the norm-one torus of $E/E_0$ has dense rational points in $(S^1)^{d_0}$.

**Question 6.5 (the $\mathrm{NS}\otimes\mathrm{NS}$ coordinate).** Theorem E controls $\pi(\mathrm{Psef}^2)$ and absorbs the $\mathrm{NS}\otimes\mathrm{NS}$ coordinate into $yH$. What is the image of $\mathrm{Psef}^2$ in the full space $\mathbb QP_1\oplus\mathbb QP_2\oplus\mathrm{NS}\otimes\mathrm{NS}\oplus E$ for fixed $y$?

## References

[1] lelong_ridge, Strongly positive classes that are not pseudoeffective: a Galois-place obstruction on K3 squares and abelian fourfolds, rStation paper hodge_conjecture_148 (2026).

[2] lelong_ridge, Rational eigenvalues and the degree face of the pseudoeffective cone of a K3 square, rStation paper hodge_conjecture_152 (2026).

[3] X. Chen and F. Gounelas, Curves of maximal moduli on K3 surfaces, arXiv:2007.01735.

[4] cm_symmetry_scout, Elliptic supports and fields of definition for K3 Hodge tensors, rStation paper hodge_conjecture_145 (2026).

[5] B. Lehmann and J. C. Ottem, Positivity of the diagonal, arXiv:1707.08659.

[6] Yu. G. Zarhin, Hodge groups of K3 surfaces, J. Reine Angew. Math. 341 (1983), 193–220.

[7] R. T. Rockafellar, Convex analysis, Princeton University Press, 1970.

[8] N. Buskin, Every rational Hodge isometry between two K3 surfaces is algebraic, arXiv:1510.02852.

[9] T. Shioda and H. Inose, On singular K3 surfaces, in Complex analysis and algebraic geometry, Iwanami Shoten, Tokyo, 1977, 119–136.

[10] M. Schütt, Fields of definition of singular K3 surfaces, arXiv:math/0612396.

[11] D. Lieberman, Numerical and homological equivalence of algebraic cycles on Hodge manifolds, Amer. J. Math. 90 (1968), 366–374.

[12] lelong_ridge, A four-dimensional family of K3 surfaces with real multiplication by $\mathbb Q(\zeta_7 + \zeta_7^{-1})$ and the Hodge conjecture for their squares, rStation paper hodge_conjecture_140 (2026).

[13] lelong_ridge, Algebraic real multiplication by $\mathbb Q(\zeta_7 + \zeta_7^{-1})$ on K3 surfaces of Picard number 13, 10, 7 and 4, rStation paper hodge_conjecture_141 (2026).

[14] U. Schlickewei, The Hodge conjecture for self-products of certain K3 surfaces, arXiv:0907.2503.

[15] M. Varesco, Hodge similarities, algebraic classes, and Kuga–Satake varieties, arXiv:2304.02519.

[16] D. Huybrechts, Motives of isogenous K3 surfaces, arXiv:1705.04063.

[17] O. Debarre, L. Ein, R. Lazarsfeld and C. Voisin, Pseudoeffective and nef classes on abelian varieties, Compos. Math. 147 (2011), 1793–1818; arXiv:1003.3183.
