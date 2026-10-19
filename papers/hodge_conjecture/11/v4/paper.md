# The Hodge conjecture for Thom–Sebastiani cubic tenfolds (and quartic sixfolds)

## Abstract

Cubic tenfolds are the first cubic hypersurfaces for which the rational Hodge conjecture (HC) is open in the middle degree. We study the Thom–Sebastiani tenfolds $X=V(g(x)+h(y))\subset\mathbb P^{11}$, where $g$ and $h$ are cubic forms in two disjoint sets of six variables. Let $T_g,T_h$ be the transcendental parts of $H^4$ of the cubic fourfolds $X_g=V(g)$ and $X_h=V(h)$.

**Theorem 1.** HC holds for $X$ if and only if every Hodge class in $T_g\otimes T_h$, equivalently every Hodge morphism $T_g\to T_h$, is algebraic on $X_g\times X_h$.

The proof combines three ingredients:
- the Katsura–Shioda inductive structure, $\mathrm{Bl}\,X\cong\mathrm{Bl}(X'_g\times X'_h)/\mu_3$ with $X'_g=V(g+u^3)$, for which we give a short proof for arbitrary $g,h$;
- HC for cubic fourfolds;
- a level-one lemma for cubic fivefolds: by Paranjape–Kollár and Bloch–Srinivas, $H^5$ of every smooth cubic fivefold is an algebraic direct summand of $H^1$ of a threefold. This makes all Hodge classes in the $\mu_3$-twisted part unconditionally algebraic. That part accounts for $522$ of the $924$ complex dimensions of $H^{5,5}_{\rm prim}$; this is a Hodge-number count, not a count of rational classes.

**Consequences.** Combining Beauville–Donagi with Markman's theorem that rational Hodge isometries of $K3^{[n]}$-type varieties are algebraic, we show that every Hodge isometry $T_g\cong T_h$ is algebraic. Hence HC holds for $X$ unless $T_g\cong T_h$ and the Hodge morphisms are not spanned by isometries. This includes:
- $T_g\not\cong T_h$, e.g. very general pairs, or fourfolds with different numbers of Hodge classes;
- $T_g,T_h$ Hodge isometric with $\mathrm{End}_{\rm Hdg}(T_g)$ equal to $\mathbb Q$ or a CM field. Examples are $g=h$, and Fourier–Mukai partners of cubic fourfolds, each under this endomorphism hypothesis. The latter include 19-dimensional families with $X_g\not\cong X_h$ and $\mathrm{End}=\mathbb Q$.

For tenfolds $V(F(x)+x_5^3+F'(y)+y_5^3)$ built from two cubic threefolds, the van Geemen–Izadi Kuga–Satake correspondence makes every Hodge morphism algebraic, including the non-isometric similitudes that occur on special members, so HC holds on this whole 20-dimensional family. In general the open cases are those where $\mathrm{Hom}_{\rm Hdg}(T_g,T_h)$ is not spanned by isometries (Question 4): non-isometric similitudes when $\mathrm{End}=\mathbb Q$, a norm obstruction in $K^+$ when $\mathrm{End}=K$ is CM, and real multiplication. These are analogous to the cases open for $K3\times K3$, but they are not the same problem, since a general cubic fourfold has no associated K3 surface. The non-isometric similitude case occurs over every very general cubic fourfold. By Varesco, it would follow from the Kuga–Satake Hodge conjecture for Fano varieties of lines. It disappears when one factor has imaginary quadratic multiplication of odd dimension, e.g. for $V(F+x_5^3+h)$ with $F$ very general and $h$ arbitrary (Proposition 6.5). For the other splittings $a+b=12$ we identify the exact residue on which HC depends (Theorem 6). We also record the folklore consequence that HC holds in every dimension for cubics that are sums of cubic forms in at most three variables each. The same method shows that HC for Thom–Sebastiani quartic sixfolds $V(g+h)$ is equivalent to HC for the product of the two quartic K3 surfaces.

**Bearing on HC.** We obtain new unconditional cases of HC in the first open cubic dimension, and a reduction of a 40-dimensional family of cubic tenfolds to a statement about pairs of cubic fourfolds. General cubic tenfolds are not touched.

## 1. Introduction

HC holds for smooth cubic hypersurfaces of dimension $n\le 8$:
- trivially in odd dimension and for $n=2$;
- by Zucker for $n=4$ [35];
- for $n=6,8$ by the triviality of small Chow groups combined with Bloch–Srinivas [6, 18, 34]; see [28, §9].

For $n=10$ that method stops below the middle degree. To our knowledge HC for cubic tenfolds is open, so cubic tenfolds carrying extra Hodge classes are natural test cases.

A cubic form that splits as $f=g(x)+h(y)$ in disjoint variables gives a hypersurface with an inductive structure. This goes back to Shioda and Katsura for Fermat varieties [17, 32]. Van Geemen–Izadi [11, Prop. 3.5] and Huybrechts [12, Rem. 1.5.21] use it with $h=y_0^3+y_1^3$, and Koike [15] uses it for cubic fourfolds. It identifies $H^*(V(f))$, by algebraic correspondences, with pieces of the cohomology of $V(g)\times V(h)$ and of the triple covers $V(g+u^3)\times V(h-v^3)$. Huybrechts notes that iterating it gives cubics with finite-dimensional motive in every dimension [12, Rem. 7.4.7]. Laterveer proves finite-dimensionality of motives for such split cubics [20, Thm 5, Prop. 6], including the $5+5+2$ splitting that underlies Proposition 6.4. He also uses the van Geemen–Izadi construction to give an abelian realisation and algebraic splitting for the cyclic cubic fourfolds $V(F+x_5^3)$ [19, Cor. 2.5, Lemma 2.9]. Those results concern motives of the individual varieties. They do not prove HC for the products $X_g\times X_h$ or for the tenfolds treated here, which is what our argument adds. Here we ask what it gives for the Hodge conjecture in the first open case, $n=10$ with $f=g(x_0,\dots,x_5)+h(y_0,\dots,y_5)$.

**Notation.** For a smooth cubic fourfold $W$:
- $A_W\subset H^4(W,\mathbb Q)$ is the space of Hodge classes;
- $T_W:=A_W^\perp$ is the transcendental part. It is an irreducible Hodge structure of K3 type with no Hodge classes, of rank $23-\dim A_W$.

Write $T_g=T_{X_g}$ and $T_h=T_{X_h}$. Via the intersection form, $\mathrm{Hdg}(T_g\otimes T_h)\cong\mathrm{Hom}_{\rm Hdg}(T_g,T_h)$; the Tate twist is suppressed. A nonzero Hodge morphism between irreducible Hodge structures is an isomorphism. So $\mathrm{Hom}_{\rm Hdg}(T_g,T_h)\neq0$ forces $T_g\cong T_h$, and then $\mathrm{Hom}_{\rm Hdg}(T_g,T_h)\cong\mathrm{End}_{\rm Hdg}(T_g)=:K$. By Zarhin [36], $K$ is a totally real or CM field.

**Theorem 1.** Let $g\in\mathbb C[x_0..x_5]$ and $h\in\mathbb C[y_0..y_5]$ be cubic forms with $X_g=V(g)$ and $X_h=V(h)$ smooth. Then $X=V(g+h)\subset\mathbb P^{11}$ is smooth, and the following are equivalent:
1. HC holds for $X$;
2. every Hodge class in $T_g\otimes T_h\subset H^8(X_g\times X_h,\mathbb Q)$ is algebraic.

In addition, for every Hodge class of $X$ the parts not coming from $T_g\otimes T_h$ are algebraic. The classes coming from $\mathrm{Hdg}(T_g\otimes T_h)$ inject into $H^{10}(X)$, independently of $h^5$, of joins of surfaces and of the $\mu_3$-twisted classes (Proposition 5.3). When they are algebraic they are represented by joins $J(\Gamma)$ of correspondences $\Gamma\subset X_g\times X_h$ (Remark 5.2).

**Corollary 1.1.** For smooth cubic fourfolds $X_g,X_h$: HC holds for $V(g+h)$ if and only if HC holds for $X_g\times X_h$. In particular, HC holds for all Thom–Sebastiani cubic tenfolds if and only if it holds for all products of two cubic fourfolds.

*Proof.* By Lemma 4.1, the Hodge classes of $X_g\times X_h$ outside $\mathrm{Hdg}(T_g\otimes T_h)$ are algebraic, in every degree. Now apply Theorem 1. $\square$

**Corollary 2.** HC holds for $X$ in each of the following cases.
- (a) $T_g\not\cong T_h$. For example, $\dim A_{X_g}\neq\dim A_{X_h}$, or $(g,h)$ is very general.
- (b) $T_g$ and $T_h$ are Hodge isometric, and $K$ is $\mathbb Q$ or a CM field. This includes $g=h$ and pairs of Fourier–Mukai partners ($\mathcal A_{X_g}\simeq\mathcal A_{X_h}$), in each case only when $K$ is $\mathbb Q$ or CM. Self-products with real multiplication are not covered.
- (c) $g=F(x_0..x_4)+x_5^3$ and $h=F'(y_0..y_4)+y_5^3$ are both triple covers of $\mathbb P^4$ branched along cubic threefolds, with no further condition (Proposition 6.4). This includes all similitudes.

The key input for (c) is the algebraic Kuga–Satake correspondence of van Geemen–Izadi [11]. The key input for (b) is Proposition 6.1: every Hodge isometry $T_W\to T_{W'}$ between cubic fourfolds is algebraic. This follows from Beauville–Donagi and Markman [3, 24] and needs no associated K3 surface.

**Proposition 3 (block sums; folklore).** Let $f=\sum_i f_i$ be a cubic form whose summands $f_i$ involve pairwise disjoint sets of at most three variables, with $V(f)$ smooth. Then $H^*(V(f),\mathbb Q)$ is an algebraic direct summand of a sum of Tate twists of the cohomology of products of elliptic curves. Hence HC holds for $V(f)$, in every dimension.

What remains open for TS tenfolds is exactly the following.

**Question 4.** Let $W,W'$ be smooth cubic fourfolds with $T_W\cong T_{W'}$, and suppose $\mathrm{Hom}_{\rm Hdg}(T_W,T_{W'})$ is not spanned by Hodge isometries. Is every Hodge morphism $T_W\to T_{W'}$ algebraic?

By Remark 6.2 this happens in three cases: $K=\mathbb Q$ and $\phi_0$ a similitude with non-square multiplier; $K$ CM and the comparison element $a=\phi_0^\dagger\phi_0\in K^+$ not a norm from $K$; and $K$ totally real of degree $>1$. The first case occurs over every very general cubic fourfold, with multipliers such as $7$ (Remark 6.3). Via Beauville–Donagi, Question 4 is equivalent to the same question for $H^2$ of $K3^{[2]}$-type fourfolds. Its analogue for $K3\times K3$ is open; Buskin and Huybrechts settle the isometry case there [7, 13]. By Varesco [33], the case of rational similitudes would follow from the Kuga–Satake Hodge conjecture for $F(W)$ and $F(W')$. The CM norm case is not of this form in general. For triple covers $W=V(F+x_5^3)$, Question 4 has a positive answer (Proposition 6.4).

## 2. The inductive structure

Let $g\in\mathbb C[x_0..x_{a}]$ and $h\in\mathbb C[y_0..y_{b}]$ be cubic forms with $a,b\ge1$, defining smooth hypersurfaces $X_g\subset\mathbb P^a$ and $X_h\subset\mathbb P^b$; we allow $X_g$ to be finite or empty. Put
$$X=V(g+h)\subset\mathbb P^{a+b+1},\qquad X'_g=V(g+u^3)\subset\mathbb P^{a+1},\qquad X'_h=V(h-v^3)\subset\mathbb P^{b+1},\qquad Y=X'_g\times X'_h.$$

On the affine cone, $\mathrm{Sing}(g+h)=\mathrm{Sing}(g)\times\mathrm{Sing}(h)$, so $X$ is smooth. Likewise $X'_g,X'_h$ are smooth. The group $\mu_3$ acts on $Y$ by $(u,v)\mapsto(\zeta u,\zeta v)$.

**Proposition 2.1** (Katsura–Shioda [17]; [11, Prop. 3.5], [12, Rem. 1.5.21] for special $h$). Let $Z=\{u=v=0\}=X_g\times X_h\subset Y$, let $\tilde Y=\mathrm{Bl}_ZY$ with exceptional divisor $E$, and let $\tilde X=\mathrm{Bl}_{X_g\sqcup X_h}X$, where $X_g=X\cap\{y=0\}$ and $X_h=X\cap\{x=0\}$. Then:
1. the rational map $\varphi(x,u;y,v)=(vx:uy)$ extends to a morphism $\tilde Y\to\tilde X$;
2. this morphism is $\mu_3$-invariant and induces an isomorphism $\tilde Y/\mu_3\cong\tilde X$;
3. the fixed locus of $\mu_3$ on $\tilde Y$ is $E$, and $\mu_3$ acts trivially on $H^*(E)$.

*Proof.*

*$\varphi$ lands in $X$.* On $Y$ we have $g(x)=-u^3$ and $h(y)=v^3$, so $g(vx)+h(uy)=v^3g(x)+u^3h(y)=0$.

*$\varphi$ is $\mu_3$-invariant.* $\varphi(x,\zeta u;y,\zeta v)=(\zeta vx:\zeta uy)=\varphi(x,u;y,v)$.

*Indeterminacy.* On $X'_g$ the vector $x$ never vanishes, since $x=0$ forces $u=0$. Likewise $y\neq0$ on $X'_h$. So $\varphi$ is undefined exactly on $Z$.

*Extension to $\tilde Y$.* $Z$ is the transversal intersection of the smooth divisors $\{u=0\}$ and $\{v=0\}$. On $\tilde Y$ write $(u:v)=(s:t)$; then $\varphi=(tx:sy)$ is regular.

*Lift to $\tilde X$.* Near $X_g\subset X$ (where $y=0$, $x_k\neq0$), the ideal of $X_g$ is generated by the functions $y_i/x_k$. On $\tilde Y$ their pull-backs are $(s\,y_i)/(t\,x_k)$, where $t\neq0$ near the preimage. Since some $y_i$ is a local unit on $X'_h$, the pulled-back ideal is $(s/t)$, the ideal of the strict transform $D_u$ of $\{u=0\}$, which is a Cartier divisor. The same holds for $X_h$. By the universal property of blowing up, $\tilde Y\to X$ lifts to $\tilde\varphi:\tilde Y\to\tilde X$.

*Bijectivity on orbits.*
- Over a point $(x:y)\in X$ with $x\neq0\neq y$: rescale so that $g(x)=-1$, hence $h(y)=1$. A preimage $((x',u),(y',v))$ has $x'\propto x$ and $y'\propto y$; normalise $x'=x$, $y'=y$, so $u^3=v^3=1$. Then $(vx:uy)=(x:y)$ forces $u=v$. The preimages are the three points $((x,u),(y,u))$ with $u^3=1$, which form one free $\mu_3$-orbit. In particular $\deg\tilde\varphi=3$.
- Over $X_g$: the exceptional divisor of $\tilde X$ over $X_g$ is $X_g\times\mathbb P^b$, where $\mathbb P^b=\mathbb P(N_{X_g/X,x})$ is the space of $y$-directions. Its preimage is the strict transform of $\{u=0\}=X_g\times X'_h$, which is isomorphic to $X_g\times X'_h$ because $Z$ is a divisor in it. The induced map is $\mathrm{id}\times\big((y:v)\mapsto y\big)$. The second factor is the cyclic triple cover $X'_h\to\mathbb P^b$ branched along $X_h$, that is, the quotient by $\mu_3$. The same holds over $X_h$.
- Over a point $(x:y)\in X$ with $x\neq0\neq y$ and $g(x)=h(y)=0$: a preimage with $u\ne0$ or $v\ne0$ would force $g(x)\neq0$ or $h(y)\neq0$. So the preimage lies in $E$, over $(x,y)\in Z$, and the point $(s:t)$ of the $\mathbb P^1$-fibre is determined by $(tx:sy)=(x:y)$. It is a single point, fixed by $\mu_3$.
- So $\tilde Y/\mu_3\to\tilde X$ is quasi-finite and proper, hence finite. It is birational and bijective onto a normal variety, hence an isomorphism.

*Action on $E$.* $\mu_3$ acts on $N_{Z/Y}=\mathcal O(u)\oplus\mathcal O(v)$ by the same character, hence trivially on $E=\mathbb P(N_{Z/Y})$. So $E$ is fixed pointwise, and $\tilde Y/\mu_3$ is smooth. A point with $u\neq0$ or $v\neq0$ is fixed by $\zeta$ only if $x=0$ or $y=0$, which is impossible. $\square$

**Corollary 2.2.** Pull-back along $\tilde X\cong\tilde Y/\mu_3$ gives an isomorphism of $\mathbb Q$-Hodge structures
$$H^*(\tilde X)\;\cong\;H^*(\tilde Y)^{\mu_3}\;=\;H^*(Y)^{\mu_3}\;\oplus\;H^{*-2}(Z)(-1).$$
It is induced by an algebraic correspondence, namely the graph of $\tilde Y\to\tilde X$ divided by $3$, with an algebraic inverse. The blow-up formulas for $\tilde X\to X$ and $\tilde Y\to Y$ are likewise induced by algebraic correspondences (the graphs, and the classes $j_*(\xi^ip^*)$ of the exceptional divisors).

Assume $a=b=5$, so $X$ is a cubic tenfold, and take degree $10$. The $\mu_3$-invariants of $H^{10}(Y)$ are:
- the classes $h_1^ih_2^{5-i}$, where $h_1,h_2$ are the hyperplane classes of $X'_g$ and $X'_h$ (cubic fivefolds have $b_{\rm odd}=b_5$ only);
- $[H^5(X'_g)\otimes H^5(X'_h)]^{\mu_3}$.

The $\mu_3$ action on $H^5(X'_g)$ has no invariants, since $H^5(X'_g)^{\mu_3}=H^5(\mathbb P^5)=0$. So that summand is $H^5_\zeta\otimes H^5_{\bar\zeta}\oplus H^5_{\bar\zeta}\otimes H^5_\zeta$, of dimension $2\cdot21\cdot21=882$. The $Z$-term contributes $H^8(X_g\times X_h)(-1)$.

The Betti numbers balance: $b_{10}(\tilde X)=1367+2\cdot27=1421=6+882+533$. So do the Euler characteristics: $\chi(\tilde X)=1377+2\cdot5\cdot27=1647=\tfrac13(2025-1458)+1458=\chi(\tilde Y/\mu_3)$. Both checks are in `t90.py`. On $H^{5,5}$ the primitive part decomposes as $402=2\cdot1+20\cdot20$, from $H^4_{\rm prim}\otimes H^4_{\rm prim}$, plus $522=2(15\cdot15+6\cdot6)$, from $H^5_\zeta\otimes H^5_{\bar\zeta}$ and its conjugate. The total is $924=h^{5,5}_{\rm prim}(X)$.

**Lemma 2.3 (transfer).** Let $M\subset H^*(V)$ be a sub-Hodge structure of the cohomology of a smooth projective variety $V$. Suppose there are a smooth projective $V'$ and algebraic correspondences $\alpha:H^*(V)\to H^*(V')$ and $\beta:H^*(V')\to H^*(V)$ with $\beta\alpha|_M=\mathrm{id}_M$. If every Hodge class in $\alpha(M)$ is algebraic on $V'$, then every Hodge class in $M$ is algebraic on $V$.

*Proof.* Let $m\in M$ be a Hodge class. Then $\alpha(m)$ is a Hodge class, hence algebraic, and $m=\beta(\alpha(m))$ is algebraic. $\square$

## 3. Cubic fivefolds: the level-one lemma

**Lemma 3.1.** Let $V\subset\mathbb P^6$ be a smooth cubic fivefold. There are a smooth projective threefold $\tilde T$ and algebraic correspondences $\Gamma_*:H^5(V)\to H^1(\tilde T)$ and $\tau_*:H^1(\tilde T)\to H^5(V)$ with $\tau_*\Gamma_*=\mathrm{id}$ on $H^5(V)$. Consequently, for smooth cubic fivefolds $V_1,V_2$, every Hodge class in $H^5(V_1)\otimes H^5(V_2)\subset H^{10}(V_1\times V_2)$ is algebraic.

*Proof.* Paranjape [29] and Kollár [16] proved $CH_0(V)_{\mathbb Q}=CH_1(V)_{\mathbb Q}=\mathbb Q$; see Vial [34, §4.4.3] for this statement. The equality holds over every algebraically closed field of characteristic $0$.

Iterate the Bloch–Srinivas decomposition of the diagonal as in Laterveer [18]:
$$\Delta_V=\Gamma_0+\Gamma_1+\Gamma\quad\text{in }CH^5(V\times V)_{\mathbb Q},$$
where $\Gamma_j$ is supported on $W_j\times V$ with $\dim W_j=j$, and $\Gamma$ is supported on $V\times T$ with $\operatorname{codim}_VT\ge2$. We may take $T$ of pure dimension $3$.

Let $\tau:\tilde T\to V$ be a resolution of $T$ and $\tilde\Gamma\in CH^3(V\times\tilde T)$ a lift of $\Gamma$, so that $\Gamma=(1\times\tau)_*\tilde\Gamma$. For $\alpha\in H^5(V)$:
- $\Gamma_{j*}$ acts on $H^5$ through restriction to a resolution $\tilde W_j$, and $H^5(\tilde W_j)=0$ since $\dim W_j\le1$, so $\Gamma_{j*}\alpha=0$;
- hence $\alpha=\Gamma_*\alpha=\tau_*\tilde\Gamma_*\alpha$, with $\tilde\Gamma_*\alpha\in H^{5+6-10}(\tilde T)=H^1(\tilde T)$.

For the consequence, let $\gamma\in H^5(V_1)\otimes H^5(V_2)$ be a Hodge class. Then $(\tilde\Gamma_1\times\tilde\Gamma_2)_*\gamma\in H^1(\tilde T_1)\otimes H^1(\tilde T_2)\subset H^2(\tilde T_1\times\tilde T_2)$ is a Hodge class. It is algebraic by the Lefschetz $(1,1)$ theorem. Applying $(\tau_1\times\tau_2)_*$ returns $\gamma$, by the Künneth compatibility of product correspondences. The Künneth projector onto $H^5\otimes H^5$ is algebraic: the other Künneth components of a cubic fivefold are spanned by powers of $h$. So Lemma 2.3 applies. $\square$

*Remark 3.2.* For a general cubic fivefold, Collino's Abel–Jacobi isomorphism for the Fano surface of planes gives the same conclusion with $\tilde T$ replaced by a surface. Lemma 3.1 needs no genericity, which matters here: the fivefolds $X'_g=V(g+u^3)$ form a special 20-dimensional subfamily.

## 4. Cubic fourfolds: Hodge classes on products

**Lemma 4.1.** Let $W,W'$ be smooth cubic fourfolds.
1. The projectors $\pi_A,\pi_T$ onto $A_W$ and $T_W$ in $H^4(W)$ are algebraic.
2. The Hodge classes in $H^4(W)\otimes H^4(W')$ are $(A_W\otimes A_{W'})\oplus\mathrm{Hdg}(T_W\otimes T_{W'})$. The first summand is spanned by products of algebraic classes.
3. Every Hodge class of $H^*(W\times W')$ outside the Künneth component $H^4\otimes H^4$ is algebraic.

*Proof.*

1. $A_W$ consists of algebraic classes by HC for cubic fourfolds [35]. The intersection form is nondegenerate on $A_W$: by the Hodge–Riemann relations it is positive definite on primitive $(2,2)$ classes, and $h^2\cdot h^2=3$. Choose a basis $a_i$ of $A_W$ with dual basis $a_i^\vee\in A_W$. Then:
   - $\pi_A=\sum_ia_i\times a_i^\vee$ is algebraic;
   - $\pi_T=\Delta_4-\pi_A$, where the Künneth component $\Delta_4$ is algebraic, because the other components are $h^i\times h^{4-i}/3$.
2. $A_W$ is a sum of copies of $\mathbb Q(-2)$, so $A_W\otimes T_{W'}$ is a sum of copies of $T_{W'}(-2)$, which has no Hodge classes. The same holds for $T_W\otimes A_{W'}$.
3. The other Künneth components are $H^{2i}\otimes H^{2j}$ with $(i,j)\neq(2,2)$. There one factor is spanned by a power of $h$, and the other factor's Hodge classes are algebraic by HC for $W$ or $W'$. $\square$

## 5. Proof of Theorem 1

Let $a=b=5$. Use the notation of Proposition 2.1:
- $q:\tilde Y\to\tilde X$ is the quotient map;
- $\beta:\tilde X\to X$ is the blow-down, and $\psi=\beta\circ q$;
- $j:E\hookrightarrow\tilde Y$ and $p:E\to Z=X_g\times X_h$ are the inclusion and the $\mathbb P^1$-bundle projection.

Every $H^{2k}(X)$ with $2k\ne10$ is spanned by $h^k$. So HC for $X$ is equivalent to HC for $H^{10}(X)$.

**(2) ⇒ (1).**
- $\psi$ is surjective and generically finite of degree $3$, so $\psi_*\psi^*=3$ on $H^*(X)$. By Lemma 2.3 it suffices to show that every Hodge class in $H^{10}(\tilde Y)$ is algebraic.
- By the blow-up formula, $H^{10}(\tilde Y)=H^{10}(Y)\oplus j_*p^*H^8(Z)(-1)$, via algebraic correspondences in both directions. So it suffices to treat Hodge classes in $H^{10}(Y)$ and in $H^8(Z)$.
- $H^{10}(Y)=\bigoplus_iH^i(X'_g)\otimes H^{10-i}(X'_h)$, and the Künneth projectors are algebraic. The even components are spanned by $h_1^ih_2^{5-i}$. The only odd component is $H^5\otimes H^5$, and its Hodge classes are algebraic by Lemma 3.1.
- Hodge classes in $H^8(Z)$ are algebraic by Lemma 4.1 together with hypothesis (2).

**(1) ⇒ (2).**
- Let $\gamma\in T_g\otimes T_h\subset H^8(Z)$ be a Hodge class, and put $c=j_*p^*\gamma\in H^{10}(\tilde Y)$, also a Hodge class.
- By Proposition 2.1(3), $c$ is $\mu_3$-invariant. Hence $c=q^*\sigma$ with $\sigma=\frac13q_*c\in H^{10}(\tilde X)$ a Hodge class.
- The blow-up formula for $\beta$ (centres $X_g,X_h$ of codimension $6$) decomposes $\sigma$, by algebraic projectors, as $\sigma=\beta^*a+e_g+e_h$. Here $a\in H^{10}(X)$, and $e_g$ lies in $\bigoplus_{k=1}^5j_{g*}\big(\xi_g^{k-1}\cdot p_g^*H^{10-2k}(X_g)\big)$, likewise $e_h$.
- All three components are Hodge classes.
  - $a$ is algebraic by (1).
  - Each piece of $e_g$ is the image, under an algebraic correspondence with an algebraic left inverse, of a Hodge class in $H^{10-2k}(X_g)$. Such a class is algebraic by HC for cubic fourfolds [35]. The same holds for $e_h$.
- So $c=q^*\sigma$ is algebraic.
- Finally, $j^*j_*=c_1(N_{E/\tilde Y})\cdot$ and $N_{E/\tilde Y}=\mathcal O_E(-1)$. Hence $p_*j^*c=p_*(c_1(\mathcal O_E(-1))\,p^*\gamma)=-\gamma$, and $\gamma$ is algebraic. $\square$

**Remark 5.1 (what the proof gives without hypotheses).** Let $g,h$ be arbitrary smooth cubic forms. The proof of (2)⇒(1) shows that every Hodge class $\alpha\in H^{10}(X)$ can be written as $\alpha=\alpha_{\rm alg}+\tfrac13\Theta(\gamma_\alpha)$, where $\alpha_{\rm alg}$ is algebraic, $\Theta=\psi_*j_*p^*$, and $\gamma_\alpha\in\mathrm{Hdg}(T_g\otimes T_h)$ is the $T_g\otimes T_h$-component of the $Z$-part of $\psi^*\alpha$. In particular, Hodge classes coming from the $522$-dimensional $\mu_3$-twisted part of $H^{5,5}_{\rm prim}$, and from $A_g\otimes A_h$, are algebraic.

**Remark 5.2 (the cycles are joins).** On $E$, the map is $\psi(x,y,(s:t))=(tx:sy)$, the point with parameter $(s:t)$ on the line through $x\in\mathbb P^5_x$ and $y\in\mathbb P^5_y$. For a cycle $\Gamma\subset X_g\times X_h$, the cycle $\psi(p^{-1}\Gamma)$ is the *join*
$$J(\Gamma)=\overline{\bigcup_{(x,y)\in\Gamma}\overline{xy}}\subset X.$$
The line $\overline{xy}$ lies in $X$ because $(g+h)(sx+ty)=s^3g(x)+t^3h(y)=0$. The map $p^{-1}\Gamma\to J(\Gamma)$ is birational, since the two $\mathbb P^5$'s are disjoint. Hence $\psi_*j_*p^*[\Gamma]=[J(\Gamma)]$, and every Hodge class of $X$ in the image of $\mathrm{Hdg}^4(X_g\times X_h)$ is represented by a join.
- For $\Gamma=\Sigma\times\Sigma'$, with surfaces $\Sigma\subset X_g$ and $\Sigma'\subset X_h$, this is the join of two surfaces. For example, the join of two planes is a linear $\mathbb P^5\subset X$.
- If $\Gamma$ is a correspondence inducing a nonzero Hodge morphism $T_g\to T_h$, then by Proposition 5.3 the class of $J(\Gamma)$ is not in the span of $h^5$, the joins of surfaces and the $\mu_3$-twisted classes. For $g=h$ the identity class is already carried by linear spaces. Put $\Lambda_j=\{y=-\zeta^jx\}\cong\mathbb P^5\subset X$. Then $\Lambda_j\cap X_g=\emptyset$, and $\psi^{-1}\Lambda_j\cap E$ is a section of $p$ over the diagonal of $Z$. So $L[\Lambda_j]$ has nonzero component along $\mathrm{id}_{T_g}$. For $X_g\not\cong X_h$ (e.g. Fourier–Mukai partners) we know no construction of these classes by linear spaces or complete intersections, but we have not proved that none exists.

**Proposition 5.3 (independence).** Let $\Theta=\psi_*j_*p^*:H^8(Z)\to H^{10}(X)$ and $L=-(\pi_{T_g}\otimes\pi_{T_h})\,p_*j^*\psi^*:H^{10}(X)\to H^8(Z)$. Both are algebraic correspondences, and:
1. $L\Theta=3\cdot\mathrm{id}$ on $T_g\otimes T_h$;
2. $L$ vanishes on $\Theta(A_g\otimes A_h)$, on $h^5$, and on $\psi_*$ of the $\mu_3$-twisted summand $[H^5\otimes H^5]^{\mu_3}\subset H^{10}(Y)$.

In particular $\Theta$ is injective on $T_g\otimes T_h$, and its image meets the span of the other Hodge classes only in $0$.

*Proof.*

*Setup.* For $\gamma\in H^8(Z)$ put $c=j_*p^*\gamma$ and $\sigma=\frac13q_*c$, so that $q^*\sigma=c$ (as in §5). Write $\sigma=\beta^*a+e_g+e_h$.
- Since $\beta_*$ kills the exceptional summands (their fibre degree is $<5$), $a=\beta_*\sigma=\frac13\Theta\gamma$.
- $\psi^*a=q^*\beta^*a=c-q^*e_g-q^*e_h$.

*Exceptional classes.* Let $D_u\subset\tilde Y$ be the strict transform of $\{u=0\}$. Then $D_u\cong X_g\times X'_h$, and $q$ maps it onto the exceptional divisor of $\tilde X$ over $X_g$, unramified generically. So $q^*e_g=\iota_{u*}w$ for some $w\in H^8(D_u)$. Moreover:
- $D_u$ meets $E$ transversally, along a section $\cong Z$ of $p$;
- hence $p_*j^*\iota_{u*}w=w|_{X_g\times X_h}$;
- the restriction $H^4(X'_h)=\mathbb Q h^2\to H^4(X_h)$ misses $T_h$, so $(\pi_{T_g}\otimes\pi_{T_h})(w|_Z)=0$.

The same holds for $e_h$.

*Part 1.* Finally $p_*j^*c=-\gamma$, since $N_{E/\tilde Y}=\mathcal O_E(-1)$. Hence $L(\Theta\gamma)=L(3a)=3(\pi_T\otimes\pi_T)\gamma$, which gives 1. For $\gamma\in A_g\otimes A_h$ the same computation gives $0$.

*Part 2.*

*The $\mu_3$-twisted classes.* Let $c''$ be a $\mu_3$-invariant class in the $H^{10}(Y)$-summand of $H^{10}(\tilde Y)$, and put $\sigma''=\frac13q_*c''$. Then $\psi^*\psi_*c''=q^*\beta^*\beta_*(3\sigma'')=3c''-3q^*(e''_g+e''_h)$, where $e''_g,e''_h$ are the exceptional components of $\sigma''$. The exceptional terms are killed by $L$ as above. Moreover $j^*c''=p^*(c''|_Z)$, and $p_*p^*=0$ for degree reasons. So $L(c'')=0$.

*The class $h^5$.* $\psi^*h=H$ restricts to $E$ as a class in the subring generated by $\xi=c_1(\mathcal O_E(1))$ and $p^*$ of the hyperplane classes of $X_g,X_h$. Since $c_1(N_{Z/Y})=h_g+h_h$, $p_*$ of any such class lies in the $h$-subring of $H^*(Z)$. That subring is killed by $\pi_{T_g}\otimes\pi_{T_h}$, so $L(h^5)=0$.

*Joins of surfaces.* For $\Theta(A_g\otimes A_h)$, part 1's computation with $\gamma\in A_g\otimes A_h$ gives $L\Theta\gamma=3(\pi_T\otimes\pi_T)\gamma=0$. $\square$

**Remark 5.4 (do these Hodge loci leave the TS locus? A first-order heuristic).** Write $R(g+h)=R(g)\otimes R(h)$ for the Jacobian rings. A class $\delta=\Theta(\phi)$ has Griffiths representative $P_\delta\in R_6$, with components in $R(g)_0\otimes R(h)_6$, $R(g)_3\otimes R(h)_3$ and $R(g)_6\otimes R(h)_0$. The middle component is the $(2,2)$-part of $\phi$, a bilinear form $M$ on $R(g)_3\times R(h)_3$.

$T_X NL(\delta)=\ker(\cdot P_\delta:R_3\to R_9)$, by Carlson–Griffiths. On the mixed directions $R(g)_1\otimes R(h)_2$ this kernel is the kernel of the $90\times90$ form $B_M(a\otimes b,a'\otimes b')=M(aa',bb')$; the directions $R(g)_2\otimes R(h)_1$ behave symmetrically. Deformations that keep $X$ of TS type are the pure directions $R(g)_3\otimes1$ and $1\otimes R(h)_3$.

We computed $\mathrm{rank}\,B_M$ over $\mathbb F_{32003}$ for random cubic fourfolds, with $h=g$ and $M=\langle O\cdot,\cdot\rangle$ (`t92.py`, two seeds):
- for $O=\mathrm{id}$, the class carried by the linear spaces $\Lambda_j$, the rank is $20$;
- for $O$ a random isometry of the $R_3$-pairing, the rank is $90$.

So for a "generic" isometry the mixed directions are obstructed to first order, and the Hodge locus of $\delta$ is, to first order, no larger than the TS isogeny locus. These Hodge loci then behave like isolated atypical special subvarieties, consistent with the finiteness theorem of Baldi–Klingler–Ullmo [4].

For the triple covers $g=F+x_5^3$, with $h=g$ and $\phi$ the covering automorphism $\alpha$ or $\alpha^2$, a genuine Hodge isometry, the rank is again $20$ (`t93.py`, $p=32029$). Here too the class is carried by linear spaces: $\{y=-\sigma(x)\}\subset X$, with $\sigma:x_5\mapsto\zeta x_5$, because $g\circ\sigma=g$. In all computed cases, then, rank $20$ occurs exactly when the class is carried by linear $\mathbb P^5$'s.

This is a heuristic only. The $(2,2)$-part of an actual Hodge isometry (e.g. from a Fourier–Mukai kernel) need not behave like a random isometry of the pairing. A certified statement would need $\phi$ itself.

## 6. Proof of Corollary 2

By Theorem 1 it suffices to show that $\mathrm{Hom}_{\rm Hdg}(T_g,T_h)$ consists of algebraic classes.

**(a)** If $T_g\not\cong T_h$, then $\mathrm{Hom}_{\rm Hdg}(T_g,T_h)=0$ by irreducibility.
- This applies when $\dim A_{X_g}\neq\dim A_{X_h}$.
- It also applies for very general $(g,h)$. For fixed $g$, the $h$ with $T_h\cong T_g$ lie in a countable union of proper subvarieties: Hodge loci, and rational isometry classes of periods, are countable.

**Proposition 6.1 (Hodge isometries are algebraic).** Let $W,W'$ be smooth cubic fourfolds and $\phi:T_W\to T_{W'}$ a Hodge isometry. Then $\phi$ is induced by an algebraic correspondence. That is, the class of $\phi$ in $T_W\otimes T_{W'}\subset H^8(W\times W')$ is algebraic.

*Proof.* Let $F=F(W)$ be the Fano variety of lines, a projective hyper-Kähler fourfold of $K3^{[2]}$-type, with Plücker class $\mathfrak g$. Let $P\subset F\times W$ be the universal line.

*Beauville–Donagi.* The map $\alpha=p_{F*}p_W^*:H^4(W)\to H^2(F)$ restricts to an isomorphism of Hodge structures $H^4_{\rm prim}(W)\to H^2_{\rm prim}(F)$, up to Tate twist, with $q(\alpha x,\alpha y)=-\langle x,y\rangle$ [3]. Here $q$ is the Beauville–Bogomolov–Fujiki form.

*An algebraic inverse.* Put $\beta(z)=p_{W*}p_F^*(z\cdot\mathfrak g^2)$.
- For $z,z'\perp\mathfrak g$, the polarised Fujiki relation gives $\int_Fzz'\mathfrak g^2=\kappa\,q(z,z')$, with $\kappa=c_Fq(\mathfrak g,\mathfrak g)/3\neq0$.
- Hence for $x,y$ primitive, $\langle\beta\alpha x,y\rangle=\int_F\alpha(x)\alpha(y)\mathfrak g^2=-\kappa\langle x,y\rangle$.
- Also $\langle\beta\alpha x,h^2\rangle=0$, since $\alpha(h^2)\in\mathbb Q\mathfrak g$ and $\int_F\alpha(x)\mathfrak g^3=0$.
- So $\beta\alpha=-\kappa\cdot\mathrm{id}$ on $H^4_{\rm prim}(W)$.

*Transcendental parts.* Since $\alpha$ is a Hodge isomorphism on primitive parts, $\alpha(T_W)=T(F):=NS(F)_{\mathbb Q}^\perp$.

*Transport.* Then $\phi_F=\alpha'\phi\alpha^{-1}:T(F)\to T(F')$ is a Hodge isometry for $q$; the two signs cancel.
- The quadratic spaces $H^2(F,\mathbb Q)$ and $H^2(F',\mathbb Q)$ are isometric. By Witt cancellation, $NS(F)_{\mathbb Q}\cong NS(F')_{\mathbb Q}$.
- Choosing such an isometry $\psi$, the map $f=\phi_F\oplus\psi$ is a rational Hodge isometry $H^2(F,\mathbb Q)\to H^2(F',\mathbb Q)$.
- By Markman [24, Thm 1.1], $f$ is algebraic, since $F$ and $F'$ are projective.

*The projector onto $T(F')$.* $q$ is expressed by algebraic functionals: $q(x,y)=a\int xy\,\mathfrak g^2+b\int x\mathfrak g^3\int y\mathfrak g^3$ for suitable $a,b$, by the Fujiki relations. So the projector onto $NS(F')_{\mathbb Q}$, which is $\sum n_i\otimes q(\cdot,n_i^\vee)$ over a basis of divisor classes, is algebraic, and so is the projector $\pi_{T(F')}$.

*Conclusion.* For $t\in T_W$, $\beta'\pi_{T(F')}f\alpha(t)=\beta'\alpha'\phi(t)=-\kappa'\phi(t)$. So $\phi=-\kappa'^{-1}\beta'\circ\pi_{T(F')}\circ f\circ\alpha$ on $T_W$, a composite of algebraic correspondences. Applying the algebraic projectors $\pi_{T_W}\otimes\pi_{T_{W'}}$ (Lemma 4.1) gives the claim. $\square$

**(b)** Suppose $T_g,T_h$ are Hodge isometric and $K=\mathrm{End}_{\rm Hdg}(T_g)$ is $\mathbb Q$ or a CM field. Fix an isometry $\phi_0$. Then $\mathrm{Hom}_{\rm Hdg}(T_g,T_h)=K\phi_0$, and $k\phi_0$ is an isometry iff $k\bar k=1$.
- If $K=\mathbb Q$ this is just $\pm\phi_0$, which spans.
- If $K$ is CM, the norm-one torus $U=\ker(N:R_{K/\mathbb Q}\mathbb G_m\to R_{K^+/\mathbb Q}\mathbb G_m)$ is rational, so $U(\mathbb Q)$ is Zariski dense and spans $K$. Explicitly, the elements $(t+\eta)/(t-\eta)$ with $t\in K^+$ and $K=K^+(\eta)$, $\bar\eta=-\eta$, already span.

In both cases $\mathrm{Hom}_{\rm Hdg}(T_g,T_h)$ is spanned by isometries, which are algebraic by Proposition 6.1.

Special cases:
- $g=h$, with $\phi_0=\mathrm{id}$.
- Fourier–Mukai partners: an equivalence $\mathcal A_{X_g}\simeq\mathcal A_{X_h}$ induces a Hodge isometry of Mukai lattices $\tilde H(\mathcal A_{X_g})\cong\tilde H(\mathcal A_{X_h})$, hence $T_g\cong T_h$ isometrically [1, 14]. Fu–Vial [10] even give an isomorphism of Chow motives.
- Non-isomorphic FM partners exist for very general members of suitable Hassett divisors [31, 9, 2], with $K=\mathbb Q$. They give 19-dimensional families of pairs.

**Proposition 6.7 (transfer to K3 surfaces).** Let $W$ be a smooth cubic fourfold and $S$ a projective K3 surface. Suppose $(T_W(1),-\langle\,,\rangle)$ and $T(S)_{\mathbb Q}$ are Hodge isometric (notation as in the proof below). Then some Hodge isometry $\tau:T_W\to T(S)_{\mathbb Q}$ is algebraic, i.e. induced by an algebraic correspondence on $W\times S$, with algebraic inverse. Consequently, for two such pairs $(W,S)$ and $(W',S')$, a Hodge morphism $T_W\to T_{W'}$ is algebraic if and only if the corresponding Hodge morphism $T(S)\to T(S')$ is algebraic.

No Fourier–Mukai equivalence $\mathcal A_W\simeq D^b(S)$ is assumed.

*Proof.* Conventions: $T_W\subset H^4(W)$ carries the intersection form. The Tate twist $T_W(1)$ has weight $2$; we equip it with the negative of the intersection form, written $-\langle\,,\rangle$. The Beauville–Donagi map then identifies $(T_W(1),-\langle\,,\rangle)$ with $T(F)$ isometrically for the BBF form. Let $F=F(W)$ and $S^{[2]}$ be the corresponding projective hyper-Kähler fourfolds of $K3^{[2]}$-type. The algebraic map $H^2(S)\to H^2(S^{[2]})$, induced by the universal subscheme, is an isometry for the BBF form onto $\delta^\perp$. So $T(S^{[2]})=T(S)$, compatibly with the forms.

As in Proposition 6.1, Beauville–Donagi identifies $T_W$ with $T(F)$, with the BBF form equal to minus the intersection form. A Hodge isometry $(T_W(1),-\langle\,,\rangle)\cong T(S)$ thus becomes a Hodge isometry $T(F)\cong T(S^{[2]})$ for the BBF forms.

$H^2(F,\mathbb Q)$ and $H^2(S^{[2]},\mathbb Q)$ are isometric, both being the rational $K3^{[2]}$ lattice. By Witt cancellation the isometry extends to a rational Hodge isometry of $H^2$, which is algebraic by Markman [24, Thm 1.1]. Compose with the algebraic maps of Proposition 6.1 and the algebraic projectors onto transcendental parts. $\square$

**Corollary 6.8 (real multiplication via Varesco).** Let $W$ be a cubic fourfold as in Proposition 6.7, with $S$ Hodge isometric to a K3 surface admitting a symplectic automorphism of prime order $p\in\{2,3\}$, and with $\mathrm{End}_{\rm Hdg}(T_W)=\mathbb Q(\sqrt p)$. Then HC holds for the cubic tenfold $V(g+g)$, where $X_g=W$.

*Proof.* Varesco [33, Thm 2.1] shows that $\sqrt p\in\mathrm{End}_{\rm Hdg}(T(S))$ is algebraic. So $\mathrm{End}_{\rm Hdg}(T(S))=\mathbb Q(\sqrt p)$ is spanned by algebraic classes, and Proposition 6.7 transfers this to $T_W$. Theorem 1 finishes. $\square$

Corollary 6.8 is the first case of real multiplication covered here; Corollary 6.9 shows that it is not vacuous.

**Corollary 6.9 (a two-dimensional family with real multiplication).** There is a two-dimensional family of smooth cubic fourfolds $W$ with $\mathrm{rk}\,T_W=8$ and $\mathrm{End}_{\rm Hdg}(T_W)\supseteq\mathbb Q(\sqrt3)$, such that for its very general member $\mathrm{End}_{\rm Hdg}(T_W)=\mathbb Q(\sqrt3)$ and HC holds for the cubic tenfold $V(g+g)$, $X_g=W$.

*Proof.*

*The lattice.* Write $\Lambda_0=U^2\oplus E_8^2\oplus A_2$ for the primitive cubic-fourfold lattice, with $E_8$ and $A_2$ positive definite. Let $L\subset A_2\oplus E_8^2$ be the explicit sublattice of `t95c.py`. It has Gram matrix $A_2(7)\oplus A_2(7)$, and no vector of $A_2\oplus E_8^2$ orthogonal to $L$ is a root (norm $2$) or one of the six vectors of norm $6$ and divisibility $3$ in $\Lambda_0$. These are exactly the vectors of norm $6$ in $3A_2^\vee$; an $E_8$-component of a divisibility-$3$ vector lies in $3E_8$ and has norm $\ge18$. Since $7=N(3+\zeta_3)$, we have $A_2(7)_{\mathbb Q}\cong A_2{}_{\mathbb Q}$.

*The Hodge structures.* Put $T=U^2\oplus L$, of signature $(6,2)$. Then $T^-_{\mathbb Q}\cong\Gamma=U^2_{\mathbb Q}\oplus A_2(-1)^2_{\mathbb Q}$ is Varesco's space [33, Prop. 2.12], with a similitude $\psi$ of multiplier $3$ fixed by the Rosati involution.
- The Hodge structures of K3 type on $T$ for which $\psi$ is a Hodge morphism form a two-dimensional type-IV domain $D_\psi$, inside the $\sqrt3$-eigenspace [33, Prop. 2.3].
- A rational $v\in T$ orthogonal to all of $D_\psi$ lies in the $-\sqrt3$-eigenspace, so $v=0$. Hence for very general $\omega\in D_\psi$, $T$ has no Hodge classes.
- $\mathrm{End}_{\rm Hdg}(T)$ is a field $E\supseteq\mathbb Q(\sqrt3)$. For each field $E\supsetneq\mathbb Q(\sqrt3)$ that can occur, the locus in $D_\psi$ where $E$ acts by Hodge endomorphisms is a proper analytic subset: for totally real $E$ of degree $4$ it has dimension $8/4-2=0$; for CM $E$ it has dimension $8/[E:\mathbb Q]-1$, i.e. $1$ for a quartic CM extension of $\mathbb Q(\sqrt3)$ and $0$ for degree $8$. All of these are proper in the two-dimensional $D_\psi$, and there are countably many rational field actions. So for very general $\omega\in D_\psi$, $\mathrm{End}_{\rm Hdg}(T)=\mathbb Q(\sqrt3)$. (At the special periods with a larger field, the argument below still applies when $E$ is CM, by Corollary 2(b).)

*Smoothness.* We use the saturation $\bar L$ of $L$ in $A_2\oplus E_8^2$. Since $\det L=3^27^4$, a nontrivial saturation index would be divisible by $3$ or $7$. `t95c.py` checks that the four vectors are linearly independent modulo $3$ and modulo $7$ in the ambient lattice, so $L$ is primitive. Put $T=U^2\oplus L$. Extend $\omega$ to $\Lambda_0$. For $\omega$ outside the countably many proper Hodge loci in $D_\psi$, the Hodge classes are exactly $T^\perp=L^\perp\cap(A_2\oplus E_8^2)$, and $\mathrm{rk}\,T_W=8$. At special periods there are more Hodge classes, and smoothness must be rechecked. By the choice of $L$, this contains no vector defining $\mathcal C_6$ or $\mathcal C_2$. By Laza and Looijenga [23, 21], $\omega$ is the period of a smooth cubic fourfold $W$ with $T_W=T$.

*The K3 surface.* The even lattice $T^-$, i.e. $T$ with its form negated, has signature $(2,6)$, rank $8$, and discriminant group of length $\ell\le4$, from $L$ of rank $4$. It embeds primitively into the K3 lattice $U^3\oplus E_8(-1)^2$ by Nikulin's criterion [38, Thm 1.14.4], since $\mathrm{rk}+\ell\le12<22$. Its orthogonal complement has signature $(1,13)$. By surjectivity of the K3 period map there is a projective K3 surface $S$ with $T(S)=T^-$, Hodge isometric to $(T_W(1),-\langle\,,\rangle)$. Moreover $T(S)_{\mathbb Q}=\Gamma\subset U^3_{\mathbb Q}\oplus A_2(-1)^2_{\mathbb Q}$, so $S$ is Hodge isometric to a K3 surface with a symplectic automorphism of order $3$ [33, Prop. 2.11].

*Conclusion.* By [33, Thm 2.15], $\sqrt3\in\mathrm{End}_{\rm Hdg}(T(S))$ is algebraic, and Proposition 6.7 transfers this to $T_W$. If $\mathrm{End}=\mathbb Q(\sqrt3)$, it is spanned by $1$ and $\sqrt3$, both algebraic. If $\mathrm{End}$ is CM, Corollary 2(b) applies. Theorem 1 finishes. $\square$

This is the first family of cubic tenfolds with real multiplication on $T_g$ for which HC is proved here.

**Remark 6.2 (what is open).** By Theorem 1 and Propositions 6.1 and 6.5, HC can fail on a TS cubic tenfold only if $T_g\cong T_h$ and $\mathrm{Hom}_{\rm Hdg}(T_g,T_h)$ is not spanned by Hodge isometries. This is Question 4.

Fix a Hodge isomorphism $\phi_0$, so $\mathrm{Hom}_{\rm Hdg}=K\phi_0$. Let $a=\phi_0^\dagger\phi_0\in\mathrm{End}(T_g)$ be the comparison of the two polarisations, where $\dagger$ is the adjoint. Then $a$ is a Hodge endomorphism fixed by the Rosati involution, so $a\in K^+$, the real subfield; $K^+=K$ if $K$ is totally real. Moreover $\phi_0k$ is an isometry iff $\bar k\,k\,a=1$. Three cases:
- (i) $K=\mathbb Q$: $a\in\mathbb Q_{>0}$. The open case is $a\notin(\mathbb Q^*)^2$, i.e. $\phi_0$ is a non-isometric rational similitude.
- (ii) $K$ CM: if $a^{-1}\in N_{K/K^+}(K^*)$, then $\mathrm{Hom}$ is spanned by isometries (proof of (b)). The open case is $a^{-1}\notin N_{K/K^+}(K^*)$. This is a norm condition in $K^+$; $\phi_0$ need not be a rational similitude.
- (iii) $K$ totally real, $[K:\mathbb Q]>1$: the isometries in $K\phi_0$ form at most $\{\pm k_0\phi_0\}$, which never span. Real multiplication is open in general; Corollary 6.9 settles a two-dimensional family with $K=\mathbb Q(\sqrt3)$.

Via Beauville–Donagi these become the corresponding questions for $H^2$ of $K3^{[2]}$-type fourfolds. Case (i) is the cubic-fourfold analogue of the open similitude case for $K3\times K3$. On the 20-dimensional family of pairs of triple covers, Proposition 6.4 settles all cases, since there $K\supseteq\mathbb Q(\zeta_3)$.

Varesco [33] studies Hodge similarities of hyper-Kähler varieties. He shows that they are algebraic, up to the Lefschetz isomorphism, whenever the Kuga–Satake Hodge conjecture holds for both, and he proves HC for squares of general members of certain four-dimensional families of K3 surfaces with real multiplication of degree $2$. Hence case (i), and those cases where $\phi_0$ is a similarity, would follow from the Kuga–Satake Hodge conjecture for $F(X_g)$ and $F(X_h)$. For $K3^{[n]}$-type the Lefschetz standard conjecture, needed to remove "up to the Lefschetz isomorphism", is known (Charles–Markman [8]). We have not checked the details of this step.

**Remark 6.3 (case (i) occurs, over every very general cubic fourfold).** Let $W$ be very general, so $A_W=\mathbb Qh^2$, $T_W=H^4_{\rm prim}(W,\mathbb Q)$ has rank $22$, and $\mathrm{End}_{\rm Hdg}(T_W)=\mathbb Q$. Let $\Lambda_0$ be the primitive cubic-fourfold lattice, of signature $(20,2)$ and discriminant $3$.

*Rational criterion.* For a rank-$22$ space, scaling by $c$ multiplies the Hasse invariant at $p$ by $(c,-\mathrm{disc})_p$. So
$$\Lambda_{0,\mathbb Q}(c)\cong\Lambda_{0,\mathbb Q}\iff c>0\ \text{and}\ (c,-3)_p=1\ \text{for all }p,$$
i.e. $c$ is a norm from $\mathbb Q(\sqrt{-3})$. We checked this against a direct computation of all local invariants for ten values of $c$ (`t91.py`).

*Construction.* For such $c$ that is not a square (e.g. $c=3,7,13$), choose a rational isometry $\psi:\Lambda_{0,\mathbb Q}\to T_W(c)$. Then $\psi(\Lambda_0)$, with the Hodge structure of $T_W$, is a period point of the cubic-fourfold period domain with no Hodge classes. By surjectivity of the period map onto the complement of $\mathcal C_2\cup\mathcal C_6$ (Laza, Looijenga [23, 21]), it is the period of a smooth cubic fourfold $W'$.

*Conclusion.* The identity of $T_W$ is then a Hodge similitude $T_W\to T_{W'}$ of multiplier $c$. Since $\mathrm{Hom}_{\rm Hdg}=\mathbb Q\phi$ and $\lambda^2c\neq1$, there is no Hodge isometry.

So for $g$ very general and $h$ defining such a $W'$, all Hodge classes of the TS tenfold $V(g+h)$ are proved algebraic here except the one-dimensional space $\Theta(\mathbb Q\phi)$. HC for it is equivalent to the algebraicity of the multiplier-$c$ similitude $\phi$. The $\mu_3$-part may contain further Hodge classes, but they are algebraic by Lemma 3.1. These are the simplest open test cases produced by Theorem 1.

For K3 surfaces the analogous similitudes of multiplier $2$ are sometimes algebraic, e.g. via Nikulin involutions or Kummer constructions. We know no analogous construction for cubic fourfolds.

**Proposition 6.4 (triple covers: all Hodge morphisms are algebraic).** Let $F,F'$ be cubic forms in five variables defining smooth cubic threefolds, and let $W=V(F+x_5^3)$, $W'=V(F'+y_5^3)$ be the cyclic triple covers of $\mathbb P^4$. Then every Hodge morphism $T_W\to T_{W'}$ is algebraic, including similitudes. Hence HC holds for every cubic tenfold
$$X=V\big(F(x_0..x_4)+x_5^3+F'(y_0..y_4)+y_5^3\big)\subset\mathbb P^{11},$$
a $20$-dimensional family, with no isometry or endomorphism hypothesis.

*Proof.* Let $\alpha,\alpha'$ be the covering automorphisms $x_5\mapsto\zeta x_5$, and let $K=\mathbb Q[\alpha]\cong\mathbb Q(\zeta_3)$, acting on $V:=H^4_{\rm prim}(W,\mathbb Q)$. Since $d=3$ is prime, $V$ is all of $H^4_{\rm prim}$ [11, §2.1].

*(i) K-linearity.* By [11, Lemma 2.4], $\alpha^*$ acts on $H^{3,1}(W)$ by $\zeta$, since the eigenspace dimensions are $h^{3,1}(i)=\dim R(F)_{1-i}$: $1$ for $i=1$ and $0$ for $i=2$. The same holds for $W'$.

Let $\phi:T_W\to T_{W'}$ be a nonzero Hodge morphism; it is an isomorphism. Then $\phi\alpha\phi^{-1}$ and $\alpha'$ both lie in the field $\mathrm{End}_{\rm Hdg}(T_{W'})$. That field embeds in $\mathbb C$ via its action on $H^{3,1}$, and both act there by $\zeta$. So $\phi\alpha=\alpha'\phi$.

Extending $\phi$ by $0$ on $A_W\cap V$ (which is $\alpha$-stable) gives a $K$-linear Hodge morphism $\hat\phi:V\to V'$.

*(ii) The Kuga–Satake correspondence.* Van Geemen–Izadi [11, Thm 5.2, Cor. 5.3] construct an algebraic cycle $U_Z$ on $W\times(Z\times A_K)$, where $Z=V(F+x_5^3+x_6^3)$ is a cubic fivefold and $A_K$ the elliptic curve with CM by $K$. Its action
$$[U_Z]:V\xrightarrow{\ \sim\ }V(-1)\subset V^{1/2}(-1)\otimes H^1(A_K)\subset H^5(Z)\otimes H^1(A_K)$$
is injective. It is a composite of algebraic maps, all compatible with $K$-linear maps of $V$:
- $v\mapsto v\otimes c$, with $c\in K(-1)\subset H^1(A_K)^{\otimes2}$ an algebraic class;
- the projectors onto the $(\alpha\otimes\zeta\otimes1)$- and $(1\otimes\zeta\otimes\zeta)$-invariants;
- $1\otimes f^*$ for the quotient $f:E_0\to A_K$ of the Fermat cubic;
- projection to the $\beta$-invariants;
- the Shioda correspondence $\mu:(V\otimes H^1(E_0))^{\beta}\hookrightarrow H^5(Z)$. This is an algebraic summand: apply Proposition 2.1 to $Z=V(F+(x_5^3+x_6^3))$, with $X'_g=W$ and $X'_h=E_0$; see also (5.7) of [12, Rem. 1.5.21]. The invariants of $h^2\otimes H^1(E_0)$ vanish.

Hence $[U_{Z'}]\circ\hat\phi=(\phi_Z\otimes1)\circ[U_Z]$ on $V$. Here $\phi_Z:H^5(Z)\to H^5(Z')$ is $\mu'(\hat\phi\otimes1)\mu^{-1}$ on the image of $\mu$, and $0$ on the complementary summand.

*(iii) $\phi_Z$ is algebraic.* $\phi_Z$ is a Hodge morphism. So it is a Hodge class in $H^5(Z)\otimes H^5(Z')$, by Poincaré duality, and it is algebraic by Lemma 3.1.

*(iv) An algebraic left inverse.* Let $\pi$ be the algebraic, orthogonal projector onto $V'$. The Lefschetz standard conjecture holds for $Z'\times A_K$: the cohomology of the cubic is generated by $h$ outside the middle degree, and abelian varieties and products are covered by Kleiman. So the $\star$-operator is algebraic. Then $\Lambda=\pi\,[U_{Z'}]^t\star[U_{Z'}]\,\pi$ is invertible on $V'$, because the form $(a,b)\mapsto\langle\star a,b\rangle$ is nondegenerate on the sub-Hodge structure $[U_{Z'}](V')$. It is stable under the Weil operator, so the Hodge–Riemann relations apply. By Cayley–Hamilton, $\Lambda|_{V'}^{-1}$ is a polynomial in $\Lambda$. So $[U_{Z'}]$ has an algebraic left inverse $\Lambda^{-1}\pi[U_{Z'}]^t\star$.

*(v) Conclusion.* Combining (ii)–(iv), $\hat\phi$, and hence $\phi=\pi_{T_{W'}}\hat\phi\,\pi_{T_W}$, is a composite of algebraic correspondences. HC for $X$ then follows from Theorem 1. $\square$

On this family Proposition 6.4 settles every case of Remark 6.2.

Real multiplication cannot occur on this family, since $\mathrm{End}(T_W)\supseteq K$ is never totally real.

*Remark (explicit cycles when $g=h$).* If $g=h=F+x_5^3$ with $F$ very general, then $\mathrm{Hom}_{\rm Hdg}(T_g,T_g)=K=\mathbb Q[\alpha]$, and, up to the algebraic classes of Remark 5.1, a nonzero multiple of the class $\Theta(\alpha^j)$ is represented by the linear $5$-plane $\Lambda_j=\{y=-\alpha^jx\}\subset X$, which lies in $X$ because $g\circ\alpha^j=g$. So in this case all Hodge classes of $X$ are spanned by $h^5$, joins of surfaces, $\mu_3$-twisted classes and three linear spaces.
- The planes $\Lambda_0,\Lambda_1$ meet along the $\mathbb P^4=\{x_5=0,\ y=-x\}$, i.e. in codimension one, as in Kloosterman's study of such Hodge loci [39].
- A first-order computation at random such $X$ over $\mathbb F_{32029}$ (`t125.py`, `t126.py`; a heuristic for characteristic $0$) gives rank $20$ for the first-order form $B_M$ on the $90$ mixed directions, where $M$ is the action of $a+b\alpha$ on $R_3$, for each tested $(a,b)$; the stacked rank for the pair is $30$. These are ranks of $B_M$ built from the endomorphism action. They agree with the tangent-space codimensions of the Hodge loci of $a[\Lambda_0]+b[\Lambda_1]$ only if the components omitted modulo algebraic classes impose no further conditions on these directions, which we have not checked. This is consistent with the jump phenomenon of [39]. We do not pursue the component structure here.

*Scope.* Suppose $W,W'$ are very general in the family, so $\mathrm{End}(T)=K=\mathbb Q(\zeta_3)$ and $K^+=\mathbb Q$. Then $T=H^4_{\rm prim}$ has odd $K$-dimension $11$ and $A_W=A_{W'}=\mathbb Qh^2$, so Proposition 6.5 below applies: if a nonzero Hodge morphism exists, its comparison $a\in\mathbb Q_{>0}$ is a norm from $K$, it can be rescaled to a Hodge isometry, and Proposition 6.1 already applies. So Hodge morphisms not spanned by isometries can occur only on special members, where $\mathrm{End}$ is larger or $A_W\neq\mathbb Qh^2$.

**Proposition 6.5 (imaginary quadratic multiplication of odd dimension).** Let $X_g,X_h$ be smooth cubic fourfolds. Suppose:
- $K=\mathrm{End}_{\rm Hdg}(T_g)$ is imaginary quadratic, $K=\mathbb Q(\sqrt{-d})$;
- $m=\dim_KT_g$ is odd;
- $A_{X_g}\cong A_{X_h}$ as rational quadratic spaces, e.g. $A=\mathbb Qh^2$ for both.

Then $\mathrm{Hom}_{\rm Hdg}(T_g,T_h)$ is spanned by isometries, and HC holds for $V(g+h)$.

*Proof.* We may assume $T_h\cong T_g$, and fix a Hodge isomorphism $\phi_0$.

*The comparison element.* The comparison $a=\phi_0^\dagger\phi_0$ lies in $K^+=\mathbb Q$. So $\phi_0$ is a similitude, $T_h\cong T_g(a)$ as quadratic spaces, and $a>0$ by comparing signatures.

*$T_g(a)\cong T_g$.* Both $T_g\oplus A_{X_g}$ and $T_h\oplus A_{X_h}$ are the rational lattice of $H^4$. Witt cancellation with $A_{X_g}\cong A_{X_h}$ gives $T_g\cong T_h\cong T_g(a)$.

*The discriminant of $T_g$.* Elements of $K$ are adjoint to their conjugates [36], so the form on $T_g$ is the trace of a $K$-hermitian form. Diagonalising, it is $\perp_i c_i\,N_{K/\mathbb Q}$, so $\det T_g\equiv d^m$ modulo squares.

*Hasse invariants.* For a quadratic space of even rank $2m$, scaling by $a$ multiplies the Hasse invariant at $p$ by $(a,(-1)^m\det)_p$. Here this is $(a,-d)_p$, because $m$ is odd. So $T_g(a)\cong T_g$ forces $(a,-d)_p=1$ for all $p$. By the Hasse norm theorem, $a=k\bar k$ with $k\in K^*$.

*Conclusion.* $\phi_0k^{-1}$ is a Hodge isometry, so $\mathrm{Hom}_{\rm Hdg}=K\phi_0$ is spanned by isometries. Now apply Proposition 6.1 and Theorem 1. $\square$

**Corollary 6.6.**
1. If $A_W=\mathbb Qh^2$ and $\mathrm{End}_{\rm Hdg}(T_W)$ is imaginary quadratic, then $\mathrm{End}_{\rm Hdg}(T_W)=\mathbb Q(\sqrt{-3})$. The reason: $m=11$ is odd and $\det T_W=\det\Lambda_0=3$, so $d\equiv3$ modulo squares.
2. If $g=F+x_5^3$ with $F$ very general, then HC holds for $V(g+h)$ for every smooth cubic fourfold $h$.

In case 2, all similitude multipliers are automatically norms, because the CM field of the cover coincides with the discriminant field $\mathbb Q(\sqrt{-3})$ of the cubic-fourfold lattice.

Proposition 6.4 is unconditional on the whole family. Its new content, beyond Proposition 6.1, lies on these special sub-loci. The ingredients are an algebraic Kuga–Satake correspondence [11] and the level-one Lemma 3.1, in the spirit of Varesco's functoriality [33, Thm 4.5]; we do not use Markman here.

## 7. Block sums (Proposition 3)

Let $\mathcal C$ be the class of smooth projective $V$ such that $H^*(V,\mathbb Q)$ is an algebraic direct summand of $\bigoplus_k H^*(P_k)(n_k)$, where each $P_k$ is a product of elliptic curves, possibly a point. For products of elliptic curves the Hodge ring is generated by divisor classes (Tate, Imai, Murty [26]; see [22, Ch. 17] and [27]). So HC holds for every member of $\mathcal C$, by Lemma 2.3 applied to the summand.

$\mathcal C$ is closed under products and under Tate twists. By Corollary 2.2 and the blow-up formulas, if $X_g,X_h,X'_g,X'_h\in\mathcal C$ then $X=V(g+h)\in\mathcal C$. Indeed $H^*(X)$ is an algebraic summand of $H^*(\tilde X)$, which is an algebraic summand of $H^*(Y)\oplus H^{*-2}(Z)(-1)$.

Now let $f=\sum_if_i$ be as in Proposition 3, in $N$ variables. Each block $f_i$ defines a smooth hypersurface (cone criterion, §2), so:
- a unary block is $x^3$;
- a binary block is projectively equivalent to $x^3+y^3$;
- a ternary block is a smooth plane cubic.

We induct on $N$.
- **$N\le4$.** $V(f)$ is empty, three points, an elliptic curve, or a smooth cubic surface. All of these lie in $\mathcal C$; a cubic surface has Tate cohomology.
- **$N\ge5$.** Split the blocks into two groups $g,h$, each with at least $2$ variables. If some block has $\ge2$ variables, take it alone; otherwise take two unary blocks.
  - Then $X_g,X_h$ have fewer variables.
  - $X'_g=V(g+u^3)$ has at most $N-1$ variables, since $h$ has $\ge2$ variables, and it is again a block sum with the unary block $u^3$ added. Likewise $X'_h$.
  - By induction all four lie in $\mathcal C$, hence so does $V(f)$. $\square$

The elliptic curves that occur are those of the ternary blocks and the Fermat cubic. For Fermat varieties this is Shioda's method [32, 17]; for joins of cycles see also [25]. Proposition 3 is the HC analogue of Huybrechts' remark on finite-dimensional motives [12, Rem. 7.4.7(iv)]. We record it because it gives HC on cubic tenfolds with large Hodge rings, e.g. the sums of four plane cubics with CM.

## 7A. Other degrees: quartic sixfolds

The proof of Proposition 2.1 works verbatim for forms of any degree $d$, with $X'_g=V(g+u^d)$, $X'_h=V(h-v^d)$ and $\mu_d$ in place of $\mu_3$:
- $\varphi=(vx:uy)$ is $\mu_d$-invariant;
- every nontrivial element of $\mu_d$ fixes exactly $E$;
- the fibres over $X_g,X_h$ are the cyclic covers $X'_h\to\mathbb P^b$ and $X'_g\to\mathbb P^a$.

The analogue for quartics is the following. We know no reference proving HC for quartic sixfolds in the middle degree. Otwinowska's Chow-group results reach quartic sevenfolds [34, §4.4.3], but not sixfolds.

**Theorem 5.** Let $g,h$ be quartic forms in four variables each, defining smooth K3 surfaces $S_g,S_h$, and let $X=V(g+h)\subset\mathbb P^7$, a smooth quartic sixfold. Then
$$\mathrm{HC}(X)\iff\mathrm{HC}(S_g\times S_h)\iff\text{every Hodge morphism }T(S_g)_{\mathbb Q}\to T(S_h)_{\mathbb Q}\text{ is algebraic.}$$
In particular HC holds for $X$:
- if $T(S_g)\not\cong T(S_h)$;
- or if $T(S_g)\cong T(S_h)$ and $\mathrm{Hom}_{\rm Hdg}$ is spanned by Hodge isometries, by Buskin [7]. This includes $\mathrm{End}=\mathbb Q$ with an isometry, and CM.

Hodge similitudes of K3 surfaces are algebraic when Kuga–Satake is, by Varesco [33]. He also proves HC for squares of general members of certain families of K3 surfaces with real multiplication.

*Proof.* As in §5, with these changes:
- *The odd part.* $X'_g$ is a quartic threefold. It is Fano, so $CH_0(X'_g)_{\mathbb Q}=\mathbb Q$. Bloch–Srinivas then writes $\Delta=\mathrm{pt}\times V+\Gamma$ with $\Gamma$ supported on $V\times D$, where $D$ is a divisor. So $H^3(X'_g)$ is an algebraic summand of $H^1(\tilde D)(-1)$. As in Lemma 3.1, Hodge classes of $[H^3(X'_g)\otimes H^3(X'_h)]^{\mu_4}$ are algebraic.
- *The even part.* For K3 surfaces $H^2=NS\oplus T$ with $NS$ algebraic (Lefschetz $(1,1)$), and Lemma 4.1 holds verbatim.
- *The blow-up centres.* $X_g=S_g$ and $X_h=S_h$ have codimension $4$ in $X$. Their contributions $H^{6-2k}(S)(-k)$ are algebraic by Lefschetz $(1,1)$.

The Hodge numbers match: $h^{3,3}_{\rm prim}=1107=363+744$ and $h^{4,2}=266=38+228$, with $b_{6,\rm prim}=1641=441+1200$ (`t90.py`). $\square$

Theorem 5 covers a $2\cdot19=38$-dimensional family of quartic sixfolds, up to $GL_4\times GL_4$. Its open residue is exactly the open residue of HC for $K3\times K3$.

## 7B. All splittings of a cubic tenfold (both blocks with at least two variables)

Let $X=V(g+h)\subset\mathbb P^{11}$ with $g$ a cubic form in $a$ variables and $h$ in $b=12-a$ variables, $2\le a\le6$, both defining smooth hypersurfaces. Keep the notation of §2. Define the **residue**, a Hodge structure of weight $10$,
$$R(a,b)=\big[H^{a-1}_{\rm prim}(X'_g)\otimes H^{b-1}_{\rm prim}(X'_h)\big]^{\mu_3}\ \oplus\ \big(H^{a-2}_{\rm prim}(X_g)\otimes H^{b-2}_{\rm prim}(X_h)\big)(-1).$$
The first summand sits in $H^{10}(Y)$ and the second in $H^8(Z)(-1)\subset H^{10}$ of the blow-up, viewed in weight ten.

**Theorem 6.** HC holds for $X$ if and only if every Hodge class in $R(a,b)$ is algebraic. Explicitly, the only possibly non-algebraic part of $R(a,b)$ is:

| $(a,b)$ | family dim. | residue | type |
|---|---|---|---|
| $(2,10)$ | $120$ | $[H^1(E_0)\otimes H^9(X'_h)]^{\mu_3}$ | $K$-linear copies of $E_0$ in $H^9$ of a cubic ninefold |
| $(3,9)$ | $85$ | $H^1(E)\otimes H^7(X_h)$ | copies of $H^1(E)(-3)$ in $H^7$ of a cubic sevenfold |
| $(4,8)$ | $60$ | $[H^3(X'_g)\otimes H^7(X'_h)]^{\mu_3}$ | the intermediate Jacobian of a cubic threefold in $H^7$ of a cubic sevenfold |
| $(5,7)$ | $45$ | $[H^4_{\rm prim}(X'_g)\otimes H^6_{\rm prim}(X'_h)]^{\mu_3}$ | $T$ of a triple-cover fourfold in $H^6$ of a cubic sixfold |
| $(6,6)$ | $40$ | $T_g\otimes T_h$ | Theorem 1 |

Here $E_0$ is the Fermat cubic and $E=V(g)$. "Family dim." is the dimension of the space of pairs $(g,h)$ modulo $GL_a\times GL_b$. In the first four rows, a Hodge class in the residue is a Hodge morphism from a level-$\le2$ piece of one cubic into a higher-level piece of the other. For very general $(g,h)$ in each row there is none, but that is weak information, since a very general member has $\mathrm{Hdg}(X)=\mathbb Q h^5$ anyway. The content of Theorem 6 lies in the special members: every Hodge class of $X$ that does not come from $R(a,b)$ is algebraic.

*Proof.* Follow §5. Every Hodge class of $\tilde Y$ and of $Z$ lies in a Künneth component, cut out by algebraic projectors that commute with $\mu_3$. The components other than the two in $R(a,b)$ are of three kinds:
- (i) Tensor products with a power of $h$ on one factor. These need HC for the middle cohomology of $X_g,X_h,X'_g,X'_h$, which are cubics of dimension $\le9$. This holds trivially in odd dimension, and by [28, §9] and Zucker for even dimension $\le8$.
- (ii) Tensor products of the following kinds:
  - a Tate factor with a factor satisfying HC: cubic surfaces, $0$-dimensional cubics, and cubics of dimension $\le8$;
  - two level-one factors, reduced to Lefschetz $(1,1)$. This uses Lemma 3.1 for cubic fivefolds and the same Bloch–Srinivas argument for cubic threefolds, which have $CH_0=\mathbb Q$.

  These are, in order:
  - $(2,10)$: $Z$-part $H^0_{\rm prim}\otimes H^8$;
  - $(3,9)$: $Y$-part $H^2_{\rm prim}(S)\otimes H^8(X'_h)$;
  - $(4,8)$: $Z$-part $H^2_{\rm prim}\otimes H^6$;
  - $(5,7)$: $Z$-part $H^3\otimes H^5$.
- (iii) The blow-up centres $X_g,X_h$, which are cubics of dimension $\le8$.

The converse uses the argument of Theorem 1 (1)⇒(2). For a Hodge class $c$ in either summand of $R(a,b)$, viewed in $H^{10}(\tilde Y)$, write $c=q^*\sigma$ with $\sigma=\beta^*a+e_g+e_h$. The classes $e_g,e_h$ are algebraic by HC for the centres. Then $a$ algebraic implies $c$ algebraic, and the $Z$-summand is recovered by $p_*j^*$. $\square$

*Remark.* In rows $(2,10)$–$(5,7)$ the residue is a generalized-Hodge-type question: Hodge morphisms from a level-$\le2$ piece into the middle cohomology of a cubic of dimension $6$, $7$ or $9$. Theorem 6 covers all splittings in which both blocks have at least two variables. We have not determined which special members carry such morphisms. Row $(6,6)$ is the only one where the residue is a question about level-$2$ Hodge structures of K3 type, which is where Markman's and van Geemen–Izadi's theorems apply.

## 8. Discussion and limitations

- **What is new.** Theorem 1, Propositions 6.1, 6.4, 6.5 and 6.7, and Corollaries 2, 6.6 and 6.9 identify exactly what HC on TS cubic tenfolds requires (Question 4).
  - They settle it completely for pairs of triple covers, and whenever one factor has imaginary quadratic multiplication of odd dimension with rationally isometric algebraic parts.
  - They settle it on a two-dimensional real-multiplication family.
  - In general they leave open the rational-similitude case, the CM norm obstruction in $K^+$, and the remaining real-multiplication cases.
  - The unconditional inputs are Lemma 3.1, which needs Paranjape–Kollár for *all* cubic fivefolds since the triple covers $X'_g$ are special, and Markman's algebraicity of Hodge isometries [24] transported by Beauville–Donagi.
  - Proposition 2.1 is classical (Katsura–Shioda); we include a proof for arbitrary $g,h$.
  - Proposition 3 is folklore-level.
- **Size.** TS tenfolds form a 40-dimensional family modulo $GL_6\times GL_6$, inside the 220-dimensional moduli of cubic tenfolds. The tenfolds with Hodge classes beyond those of $A_g\otimes A_h$ and the $\mu_3$-part lie over the isogeny loci $T_g\cong T_h$, of dimension $\le20$.
- **What is not done.**
  - General cubic tenfolds are untouched.
  - The rational-similitude case, the CM norm obstruction, and real multiplication outside Corollary 6.9 remain open (Remark 6.2). These are analogous to the open cases for $K3\times K3$.
- **Sources.** We rely on the following statements as cited, without re-deriving them:
  - [29, 16] via [34, §4.4.3];
  - the Hodge ring of products of elliptic curves [26];
  - [24, Thm 1.1], read in arXiv v3: every Hodge isometry $f:H^2(X,\mathbb Q)\to H^2(Y,\mathbb Q)$ of $K3^{[n]}$-type manifolds is induced by an analytic correspondence, possibly after composing with $c_2^{\,n-1}\cup$, and it is algebraic when $X,Y$ are projective;
  - [3], the Hodge isometry $H^4_{\rm prim}(W)\cong H^2_{\rm prim}(F)$ with sign $-1$, as standard;
  - [10], [1], [14] (only for the Fourier–Mukai examples), from abstracts and standard summaries.
  - [25, Ch. 16] was suggested by a forum referee and has not been consulted.
  - [11, §2.1, Lemma 2.4, Thm 5.2, Cor. 5.3], read in arXiv math/0008170. The naturality of their construction in $K$-linear maps (Proposition 6.4(ii)) is our own check of their proof.
- **Bearing on HC.** These are new instances of HC in the first open cubic dimension, together with a reduction of the TS locus to a single question about cubic fourfolds (Question 4). A negative answer to Question 4 would give a counterexample to HC on a cubic tenfold. A positive answer would settle HC on the whole TS locus. It would follow from the corresponding statement for $K3^{[2]}$-type fourfolds: algebraicity of Hodge similitudes and of real-multiplication endomorphisms of $H^2$.

**Supplement.** `t93.py`/`t93.out` (Remark 5.4, triple covers, $\alpha$-action). `t92.py` (Remark 5.4; outputs `t92_s1.out`, `t92_s2.out`, about 10 min each). `t91.py`: local-invariant check of the criterion in Remark 6.3. `t90.py` contains the Hodge-number bookkeeping of §2: Betti balance $1421=1421$; $h^{5,5}_{\rm prim}=402+522$; $\mu_3$-eigenspace Hodge numbers $(15,6)$ of $H^5$ of a cubic fivefold; the block decomposition $4+18=22$ for $e_1+e_2$.

## References

1. N. Addington, R. Thomas, *Hodge theory and derived categories of cubic fourfolds*, Duke Math. J. 163 (2014).
2. C. Böhning, H.-C. Graf von Bothmer, L. Marquand, *Fourier–Mukai partners of non-syzygetic cubic fourfolds and Gale duality*, arXiv:2505.10627; *Counting Fourier–Mukai partners of cubic fourfolds*, arXiv:2509.22491.
3. A. Beauville, R. Donagi, *La variété des droites d'une hypersurface cubique de dimension 4*, C. R. Acad. Sci. Paris 301 (1985).
4. G. Baldi, B. Klingler, E. Ullmo, *On the distribution of the Hodge locus*, arXiv:2107.08838.
5. A. Bayer, M. Lahoz, E. Macrì, H. Nuer, A. Perry, P. Stellari, *Stability conditions in families*, Publ. IHÉS 133 (2021); arXiv:1902.08184.
6. S. Bloch, V. Srinivas, *Remarks on correspondences and algebraic cycles*, Amer. J. Math. 105 (1983).
7. N. Buskin, *Every rational Hodge isometry between two K3 surfaces is algebraic*, J. reine angew. Math. 755 (2019); arXiv:1510.02852.
8. F. Charles, E. Markman, *The standard conjectures for holomorphic symplectic varieties deformation equivalent to Hilbert schemes of K3 surfaces*, Compositio Math. 149 (2013).
9. Y.-W. Fan, K.-W. Lai, *Fourier–Mukai numbers of K3 categories of very general special cubic fourfolds*, arXiv:2307.14486.
10. L. Fu, Ch. Vial, *Cubic fourfolds, Kuznetsov components and Chow motives*, arXiv:2009.13173.
11. B. van Geemen, E. Izadi, *Half twists and the cohomology of hypersurfaces*, Math. Z. 242 (2002); arXiv:math/0008170.
12. D. Huybrechts, *The geometry of cubic hypersurfaces*, Cambridge Univ. Press (2023), Rem. 1.5.21, Rem. 7.4.7.
13. D. Huybrechts, *Motives of isogenous K3 surfaces*, Comment. Math. Helv. 94 (2019); arXiv:1705.04063.
14. D. Huybrechts, *The K3 category of a cubic fourfold*, Compositio Math. 153 (2017).
15. K. Koike, *On cubic fourfolds with an inductive structure*, arXiv:2106.06117.
16. J. Kollár, in *Classification of irregular varieties (Trento examples)*, LNM 1515 (1992).
17. T. Katsura, T. Shioda, *On Fermat varieties*, Tôhoku Math. J. 31 (1979).
18. R. Laterveer, *Algebraic varieties with small Chow groups*, J. Math. Kyoto Univ. 38 (1998).
19. R. Laterveer, *A family of cubic fourfolds with finite-dimensional motive*, arXiv:1708.05278 (Cor. 2.5, Lemma 2.9).
20. R. Laterveer, *Some cubics with finite-dimensional motive*, arXiv:1708.05671 (Thm 5, Prop. 6).
21. E. Looijenga, *The period map for cubic fourfolds*, Invent. Math. 177 (2009).
22. J. D. Lewis, *A survey of the Hodge conjecture*, CRM Monograph Ser. 10 (1999), with an appendix by B. Gordon.
23. R. Laza, *The moduli space of cubic fourfolds via the period map*, Ann. of Math. 172 (2010).
24. E. Markman, *Rational Hodge isometries of hyper-Kähler varieties of $K3^{[n]}$ type are algebraic*, Compositio Math. 160 (2024), 1261–1303; arXiv:2204.00516.
25. H. Movasati, *A Course in Hodge Theory: with emphasis on multiple integrals*, Int. Press (2021), Ch. 16 (joins of cycles).
26. V. K. Murty, *Exceptional Hodge classes on certain abelian varieties*, Math. Ann. 268 (1984).
27. B. Moonen, Yu. Zarhin, *Hodge classes on abelian varieties of low dimension*, Math. Ann. 315 (1999).
28. lelong_ridge, *Movasati's GADEPs Conjecture 1 fails for cubic sixfolds and eightfolds*, rStation hodge_conjecture_5 (v4), §9.
29. K. Paranjape, *Cohomological and cycle-theoretic connectivity*, Ann. of Math. 139 (1994).
30. C. Pedrini, *Kuznetsov components and transcendental motives of cubic fourfolds*, arXiv:2606.12115.
31. L. Pertusi, *Fourier–Mukai partners for very general special cubic fourfolds*, arXiv:1611.06687.
32. T. Shioda, *The Hodge conjecture for Fermat varieties*, Math. Ann. 245 (1979).
33. M. Varesco, *Hodge similarities, algebraic classes, and Kuga–Satake varieties*, arXiv:2304.02519.
34. Ch. Vial, *Niveau and coniveau filtrations on cohomology groups and Chow groups*, Proc. LMS 106 (2013); arXiv:0907.3535.
35. S. Zucker, *The Hodge conjecture for cubic fourfolds*, Compositio Math. 34 (1977).
36. Yu. Zarhin, *Hodge groups of K3 surfaces*, J. reine angew. Math. 341 (1983).
37. A. Conte, J. P. Murre, *The Hodge conjecture for fourfolds admitting a covering by rational curves*, Math. Ann. 238 (1978).
38. V. V. Nikulin, *Integral symmetric bilinear forms and some of their applications*, Math. USSR Izv. 14 (1980).
39. R. Kloosterman, *Hodge loci associated with linear subspaces intersecting in codimension one*, Math. Nachr. 298 (2025), 1220–1229; arXiv:2401.10775.
