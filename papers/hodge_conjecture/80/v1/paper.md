# Trianalytic and Lagrangian seeds for nonsquare Hodge similarities of K3 type

**lelong_ridge**

## 1. Introduction

### 1.1 The problem

Let $S$, $S'$ be projective K3 surfaces with $\operatorname{End}_{\mathrm{Hdg}} T(S)_{\mathbb Q} = \mathbb Q$. A *Hodge similarity* of multiplier $\lambda \in \mathbb Q_{>0}$ is a Hodge isomorphism $\psi\colon T(S)_{\mathbb Q} \to T(S')_{\mathbb Q}$ with $q'(\psi x) = \lambda\,q(x)$. In [B] the Hodge conjecture for finite products of such surfaces (with $\operatorname{rk} T$ odd or $\ge 10$) was reduced to two statements:

- **(D)**: the determinant class of $T(S)$ is algebraic;
- **($\Psi_{\mathrm{ns}}$)**: every Hodge similarity of nonsquare multiplier is algebraic.

Square multipliers reduce to Hodge isometries, which are algebraic by Buskin [Bu] and Markman [Mar24]. Nonsquare similarities between different K3 surfaces do arise from quotients by symplectic automorphisms of prime order $p$, with multiplier $p$ [Var23, proof of Thm 2.1], but these surfaces have Picard rank at least $9$. At Picard rank one no nonsquare case is known, although partners of every odd prime multiplier $p \nmid d$ exist in degree $2d$ [B].

The known proofs for isometries carry an algebraic cycle, the *seed*, from a special point to the general one. In [A] we described two mechanisms for this: transport of hyperholomorphic objects along twistor lines, and Voisin's deformation of Lagrangian submanifolds. Here we ask what a seed for a nonsquare multiplier must be, and we find a place where one could exist.

### 1.2 Results

**Twistor lines through Picard rank zero (Section 2).** Proposition 2.1: a manifold of $K3^{[m]}$-type, $m \ge 2$, whose twistor line meets a point with $\operatorname{Pic} = 0$ has no trianalytic subvarieties of positive dimension. This follows from Verbitsky [Ver98] and Soldatenkov–Verbitsky [SV15]. Consequences: subvariety seeds between different deformation types are excluded; trianalytic graphs on $S \times S'$ are graphs of isomorphisms; and the graph of the natural norm-$3$ map $F(X) \dashrightarrow Z(X)$ for cubic fourfolds is not trianalytic (Corollary 2.3). In [A, Prop 5.3] the last statement needed a transversality hypothesis.

**Rank-one families (Section 3).** Proposition 2.1 leaves families with $\operatorname{NS} = \mathbb Z u$. Call a surface $W$ in such a family a *$u$-seed* if it is a trianalytic K3 surface whose restriction map is a similarity on $u^\perp$.
- Proposition 3.2: at a $u$-generic point, every surface on which the symplectic form does not vanish is a $u$-seed. The proof is a Wirtinger inequality (Lemma 3.1).
- Proposition 3.4: one $u$-seed proves ($\Psi_{\mathrm{ns}}$) for its multiplier on a $19$-dimensional family of K3 surfaces of Picard rank one.
- Proposition 3.5: a $u$-seed exists iff some positive multiple of an invariant class is effective at one suitable point, and each component is then itself a $u$-seed. Fixed loci of symplectic groups and orbit surfaces of finite groups of automorphisms fail this test; the latter give only square multipliers.

**Necessary conditions (Sections 4–6).**
- $K3^{[2]}$ (Theorem 4.2): $q(u) = -2m'^2$, $\lambda = 10(1+m)$, and the seed has $66m^2 - 54$ double points counted with multiplicity; integrality forces $\lambda \ge 50$. Theorem 6.5: in fact there is no $u$-seed of $K3^{[2]}$-type. At a suitable Hilbert point, the Hodge index theorem bounds $b$ from above (Lemma 6.4), which forces the incidence correspondence to be the union of two graphs, and the transcendental part of the similarity then fails modulo $5$.
- $K3^{[3]}$ (Section 5): $3 \mid \lambda$, with a table of the admissible $(q(u), \operatorname{div} u)$, the wall classes removed. For every entry all the integrality conditions in $H^8$ that we can compute are satisfiable.
- Hilbert points (Section 6): $\lambda \le nb$, where $b$ is the degree of the incidence correspondence over $S$, with equality iff it is Lagrangian. At the points we computed, equality is impossible, so these seeds are not Voisin's mechanism. For genus $4$ we list the numerical invariants a seed must have (Proposition 6.2).
- Numerical test (Proposition 6.3): at a very general Hilbert point, a surface $W \subset S^{[n]}$, $n \le 3$, deforms to a $u$-seed iff three intersection numbers of $W$ with $\langle h, \delta\rangle$ and $\int_W c_2$ are proportional to prescribed values. The transcendental part of the condition is automatic.

**Eisenstein cubics (Section 7).** Proposition 7.1: on the Fano variety $F$ of a cyclic cubic fourfold, a local branch that preserves each fibre of the projection $F \dashrightarrow Y$ to the branch cubic threefold and multiplies $\sigma_F$ by a nonzero constant is a power of the deck transformation. This proves the covector step left open in [A, Appendix A].

### 1.3 Status and what is not new

No seed is constructed and no new case of the Hodge conjecture is proved (Section 8). Propositions 2.1, 3.2, 3.4, 3.5, Theorem 4.2, Propositions 6.1, 6.3, Lemma 6.4, Theorem 6.5 and Proposition 7.1 are proved. Propositions 5.2 and 6.2(b)–(c), and the numbers for genus $7$ and genus $2$ in Section 6.4, rest on computations whose inputs are listed with them. These computations (the $\operatorname{Sym}^2$-projection of $[\Delta_x]$, the $H'$-term, and the elimination of $\nu$) have not been checked independently. Remark 5.3 is heuristic.

Trianalyticity and its rigidity are due to Verbitsky [Ver95, Ver96, Ver98] and Soldatenkov–Verbitsky [SV15]; the twistor-path argument is Buskin's [Bu]; the integral cohomology inputs are Markman's [Mar07], Kapfer's [Kap16] and Lehn's [Leh99]; nef cones of Hilbert schemes are from Bayer–Macrì [BM14, BM14b]. What we add are the statements about $u$-seeds and the computations built on them.

## 2. Twistor lines through Picard rank zero

Twistor transport moves an object along twistor lines and keeps it holomorphic at every point. The objects it can carry are trianalytic subvarieties and projectively hyperholomorphic sheaves. In [A, Lemma 2.1] we showed that a Hodge class that stays Hodge along a path through a point with $\operatorname{Pic} = 0$ is a similarity of all of $H^2$, and deduced parity rules for the multiplier. For subvarieties a stronger statement holds: on manifolds of $K3^{[m]}$-type, a twistor line through $\operatorname{Pic} = 0$ carries no trianalytic subvariety at all.

**Proposition 2.1.** Let $Y$ be of $K3^{[m]}$-type with $m \ge 2$, with a hyperkähler metric whose twistor line contains a point $Y_{s_0}$ with $\operatorname{Pic}(Y_{s_0}) = 0$.
- (a) Every subvariety of $Y$ that is trianalytic for this metric is a point or $Y$.
- (b) Let $X$ be a compact hyperkähler manifold with $\dim X < \dim Y$, and let $\Gamma \subset X \times Y$ be irreducible and trianalytic for a product metric whose second factor is as above. Then $\Gamma = W \times Y$ or $\Gamma = W \times \{y\}$, so $[\Gamma]$ induces the zero map between $H^2(X)$ and $H^2(Y)$.

The hypothesis holds if and only if no nonzero rational class is orthogonal to the positive three-plane $P = \langle \omega, \operatorname{Re}\sigma, \operatorname{Im}\sigma\rangle$ of the metric. Indeed, the points of the twistor line correspond to the isotropic lines in $P_{\mathbb C}$, and for an integral class $y \notin P^\perp$ only two of them lie in $y^\perp$.

*Proof.* (a) Put $V = H^2(Y_{s_0}, \mathbb Q)$. It has no nonzero rational $(1,1)$-class. Let $V_1 \subset V$ be a sub-Hodge structure. If $\sigma \notin V_{1,\mathbb C}$, then $V_1$ is of type $(1,1)$, so $V_1 = 0$. Otherwise the $q$-orthogonal complement of $V_1$ is a sub-Hodge structure orthogonal to $\sigma$ and $\bar\sigma$, hence of type $(1,1)$ and zero, so $V_1 = V$. So $V$ is irreducible, and $E = \operatorname{End}_{\mathrm{Hdg}} V$ is a division algebra. It embeds into $\mathbb C$ through its action on $H^{2,0}$, so it is a number field, and $[E:\mathbb Q]$ divides $\dim V = 23$. Suppose $[E:\mathbb Q] = 23$, and let $\tau_0\colon E \to \mathbb C$ be the character by which $E$ acts on $\sigma$. Adjunction with respect to $q$ is an involution of $E$ with $\tau_0(\varphi^\dagger) = \overline{\tau_0(\varphi)}$. If $\tau_0(E) \not\subset \mathbb R$, this involution is nontrivial, so $[E:\mathbb Q]$ is even, which is impossible. If $\tau_0(E) \subset \mathbb R$, then $\operatorname{Re}\sigma$ and $\operatorname{Im}\sigma$ lie in $V \otimes_{E,\tau_0} \mathbb R$, which has real dimension $1$, which is also impossible. So $E = \mathbb Q$. The Hodge group of $V$ acts faithfully and irreducibly, so it is reductive, and it contains the rotations of the plane $\langle \operatorname{Re}\sigma, \operatorname{Im}\sigma\rangle$. Zarhin's argument [Zar] then shows that it is $\mathrm{SO}(V)$.

The Mumford–Tate group of $Y_{s_0}$, the smallest $\mathbb Q$-subgroup of $\mathrm{GL}(H^*(Y,\mathbb Q))$ containing the one-parameter group of the Weil operator, lies in the maximal Mumford–Tate group $G$. For manifolds of maximal holonomy, $G \cong \mathrm{Spin}(H^2(Y), q)$ [SV15, Def 1.6 and the paragraph after it]. Its image in $\mathrm{GL}(H^2)$ is $\mathrm{SO}(H^2)$, with finite central kernel, and the image of the Mumford–Tate group contains the Hodge group of $H^2$. A connected subgroup of $G$ of full dimension is $G$, so $Y_{s_0}$ is Mumford–Tate generic.

A trianalytic $W \subset Y$ is a complex subvariety of $Y_{s_0}$, so it is absolutely trianalytic, that is, trianalytic for every hyperkähler metric compatible with $Y_{s_0}$ [SV15, Claim 1.8]. By [SV15, Thm 1.9], a diffeomorphism carries $W$ to an absolutely trianalytic subvariety of the same dimension at any other point of the same connected component of the Teichmüller space. A family connecting $Y$ with a Hilbert scheme induces a diffeomorphism that puts both complex structures in one component. The period map is surjective on each component [Huy99, Thm 8.1], so the component contains $S^{[m]}$, where $S$ is a K3 surface with $\operatorname{Pic}(S) = 0$ and $\operatorname{End}_{\mathrm{Hdg}} H^2(S) = \mathbb Q$. Its Hodge group is $\mathrm{SO}(H^2(S))$ [Zar], so every Hodge class on every power $S^k$ is invariant under the $\mathrm{SU}(2)$ of any hyperkähler metric, and $S$ has no nontrivial automorphisms. By Verbitsky [Ver98, Thm 9.12], $S^{[m]}$ then has no trianalytic subvariety other than points and $S^{[m]}$, for any compatible metric. So $W$ is a point or $Y$.

(b) The projections are holomorphic for every induced complex structure of the product metric. By Remmert's proper mapping theorem, $\mathrm{pr}_Y(\Gamma)$ is trianalytic, and so is $\mathrm{pr}_Y(\Gamma \cap (\{x\} \times Y))$ for every $x \in X$. By (a) each irreducible component of these sets is a point or $Y$. If $\mathrm{pr}_Y(\Gamma)$ is a point, then $\Gamma = W \times \{y\}$. Otherwise $\dim \Gamma \ge \dim Y > \dim X$, so the fibres of $\Gamma \to \mathrm{pr}_X(\Gamma)$ are positive-dimensional, hence equal to $Y$, and $\Gamma = \mathrm{pr}_X(\Gamma) \times Y$. The classes $[W] \otimes 1$ and $[W] \otimes [\mathrm{pt}]$ have no Künneth component involving $H^2(Y)$ or $H^{\dim_{\mathbb R} Y - 2}(Y)$. $\square$

**Remark 2.2 (products of K3 surfaces).** Let $\Gamma \subset S \times S'$ be a surface that is trianalytic for a product metric and dominates both factors. Then $\Gamma$ is the graph of an isomorphism. Its normalization $\tilde\Gamma$ is smooth and hyperkähler [SV15, Thm 1.2]. The map $\tilde\Gamma \to S$ is holomorphic for every induced complex structure, so its fibres are trianalytic, and a curve never is. Hence the map is finite. Both canonical bundles are trivial, so it is étale, and since $S$ is simply connected it is an isomorphism. The same holds for $\tilde\Gamma \to S'$, and $[\Gamma]$ induces an integral Hodge isometry. No Picard condition is needed here. So on $S \times S'$, twistor transport can produce a nonsquare similarity only from a sheaf seed [B, §6.2].

**Corollary 2.3.** Let $X_0$ be a cubic fourfold with $\operatorname{NS}(Z(X_0)) = \mathbb Z\theta$, where $Z(X_0)$ is the eightfold of Lehn–Lehn–Sorger–van Straten [LLSvS]. Then for every nonconstant rational map $\xi\colon F(X_0) \dashrightarrow Z(X_0)$ and every Kähler class on $F \times Z$, the graph $\Gamma_\xi$ is not trianalytic. In particular this holds for the norm-$3$ map $\xi$ of [A, Prop 5.3], without the transversality hypothesis (T) used there.

*Proof.* $F \times Z$ is simply connected, so a Kähler class is $(\omega, \omega')$ and its Ricci-flat metric is the product metric. Since $Z$ is projective, we may take $\theta$ ample. A rational class orthogonal to $\operatorname{Re}\sigma_Z$ and $\operatorname{Im}\sigma_Z$ lies in $\operatorname{NS}(Z) = \mathbb Z\theta$, and $q(\theta, \omega') > 0$ because $\theta$ and $\omega'$ lie in the same component of the positive cone. So no nonzero rational class is orthogonal to $\langle \omega', \operatorname{Re}\sigma_Z, \operatorname{Im}\sigma_Z\rangle$, and the twistor line of $(Z, \omega')$ meets $\operatorname{Pic} = 0$. $Z$ is of $K3^{[4]}$-type and $\dim F = 4 < 8$. By Proposition 2.1(b), an irreducible trianalytic $\Gamma \subset F \times Z$ is $W \times Z$ or $W \times \{z\}$. The graph $\Gamma_\xi$ has dimension $4$ and is not of the first kind, and it is of the second kind only if $\xi$ is constant. $\square$

So twistor transport between deformation types can use only sheaf seeds, as long as the twistor lines involved meet $\operatorname{Pic} = 0$. A subvariety seed must live in a family where some class stays algebraic along every twistor line. The simplest such families are those in which a single class $u$ stays algebraic. Section 3 studies them.

## 3. Trianalytic K3 surfaces in rank-one families

Proposition 2.1 leaves one geometric possibility for twistor transport: a trianalytic subvariety in a family whose twistor lines never reach $\operatorname{Pic} = 0$. The simplest case is a family in which one class stays algebraic.

### 3.1 Setup

Let $Y$ be of $K3^{[n]}$-type, $n \ge 2$, with Beauville–Bogomolov form $q$, and let $u \in H^2(Y, \mathbb Z)$ be primitive with $q(u) < 0$. We call $Y$ *$u$-generic* if $\operatorname{NS}(Y) = \mathbb Z u$ and $\operatorname{End}_{\mathrm{Hdg}}(u^\perp_{\mathbb Q}) = \mathbb Q$. Then the Hodge group of $u^\perp_{\mathbb Q}$ is $\mathrm{SO}(u^\perp)$ [Zar]. We always assume that $u^\perp$ contains a Kähler class; at a $u$-generic point this means that $u$ is not a wall (MBM) class [AV]. For an irreducible surface $W \subset Y$ we write $j\colon W' \to Y$ for a resolution of its normalization.

**Lemma 3.1 (Wirtinger test).** Let $\omega$ be a Kähler class on $Y$ and $\sigma$ the symplectic form. For every irreducible surface $W \subset Y$,
$$\frac{q_{W'}(j^*\sigma, j^*\bar\sigma)}{q(\sigma, \bar\sigma)} \le \frac{q_{W'}(j^*\omega)}{q(\omega)},$$
where $q_{W'}$ is the intersection form of $W'$. Equality holds iff $W$ is trianalytic for the hyperkähler metric with Kähler class $\omega$.

*Proof.* Let $\omega_I = \omega, \omega_J, \omega_K$ be the Kähler forms of the metric, normalized so that $\sigma = \omega_J + i\omega_K$. They are $q$-orthogonal of equal square, so $q(\sigma, \bar\sigma) = 2q(\omega)$. At a smooth point of $W$ with tangent space $V$, $\sigma|_V \wedge \bar\sigma|_V \le 2\,\omega|_V^2$ as top forms on $V$, with equality iff $V$ is $J$-invariant, that is, quaternionic. Integrate over $W$. A complex subvariety whose smooth locus is quaternionic is trianalytic [Ver98]. $\square$

The test is sharp on a known example. Let $S = \{w^4 = f_4(x, y, z)\}$ with $g(w) = iw$, and let $W_g = \{\xi \in S^{[2]} : \xi = x + gx\}$. Then $W_g$ is a K3 surface, $j^*\sigma = (1+i)\sigma_{W}$, and for $\omega = \tilde h - \delta$ both sides equal $2$. So $W_g$ is trianalytic. It is the K3 component of the fixed locus of the symplectic involution $g^{2[2]} \circ \beta$, with $\beta$ Beauville's involution.

**Proposition 3.2 (automatic trianalyticity).** Let $Y$ be $u$-generic and let $W \subset Y$ be an irreducible surface with $j^*\sigma \ne 0$. Then:
- (a) there is $\lambda \in \mathbb Q_{>0}$ with $q_{W'}(j^*x, j^*y) = \lambda\,q(x, y)$ for $x, y \in u^\perp$;
- (b) $W$ is trianalytic for every Kähler class $\omega \perp u$, its normalization is a K3 surface $\tilde W$, $j^*u = 0$, and $j^*\colon u^\perp_{\mathbb Q} \to H^2(\tilde W, \mathbb Q)$ is a bijective similarity of multiplier $\lambda$;
- (c) $\tilde W$ has no nonzero rational $(1,1)$-class, and $u^\perp_{\mathbb Q}(\lambda) \cong H^2(\tilde W, \mathbb Q)$ as quadratic spaces.

*Proof.* (a) The form $(x, y) \mapsto q_{W'}(j^*x, j^*y)$ on $u^\perp_{\mathbb Q} = T(Y)_{\mathbb Q}$ is a Hodge class, hence invariant under $\mathrm{SO}(u^\perp)$, hence a multiple $\lambda q$. Evaluating at $(\sigma, \bar\sigma)$ gives $\lambda > 0$, because $q_{W'}(j^*\sigma, j^*\bar\sigma) = \int_{W'} j^*\sigma \wedge j^*\bar\sigma > 0$ when $j^*\sigma \ne 0$. (b) Since $\sigma \in u^\perp_{\mathbb C}$ and $\omega \in u^\perp_{\mathbb R}$, both sides of Lemma 3.1 equal $\lambda$. So $W$ is trianalytic, and its normalization is a smooth hyperkähler surface [SV15, Thm 1.2], hence a K3 surface or a complex torus, and equal to $W'$. By (a), $j^*$ is injective on $u^\perp_{\mathbb Q}$, which has dimension $22$. A torus has $b_2 = 6$, so $\tilde W$ is a K3 surface and $j^*\colon u^\perp_{\mathbb Q} \to H^2(\tilde W, \mathbb Q)$ is bijective. The map $x \mapsto q_{\tilde W}(j^*u, j^*x)$ is a morphism of Hodge structures $u^\perp_{\mathbb Q} \to \mathbb Q(-1)$, hence zero, because $u^\perp_{\mathbb Q} = T(Y)_{\mathbb Q}$ has no nonzero rational $(1,1)$-class. So $j^*u$ is orthogonal to all of $H^2(\tilde W, \mathbb Q)$, and $j^*u = 0$. (c) follows from (b). $\square$

So at a $u$-generic point, every surface on which $\sigma$ does not vanish identically is a trianalytic K3 surface. We call such a surface a *$u$-seed* of multiplier $\lambda$.

**Lemma 3.3.**
- (a) If $Y$ is $u$-generic, the Hodge classes in $H^*(Y, \mathbb Q)$ are exactly the $\mathrm{Spin}(u^\perp)$-invariant classes.
- (b) Let $Y_1$ be a point of the $u$-family with $\operatorname{End}_{\mathrm{Hdg}} T(Y_1)_{\mathbb Q} = \mathbb Q$, and let $\omega \perp u$ be a Kähler class with $\operatorname{NS}(Y_1) \cap \omega^\perp = \mathbb Z u$. Then all but countably many points of the twistor line of $(Y_1, \omega)$ are $u$-generic. This applies in particular when $Y_1$ is $u$-generic.

*Proof.* (a) The Hodge group of $H^*(Y, \mathbb Q)$ is the image of a connected subgroup $H$ of $\mathrm{Spin}(H^2(Y, \mathbb Q), q)$, which acts on $H^*$ through the Looijenga–Lunts–Verbitsky representation [LL97, Ver96], and $H$ maps onto the Hodge group of $H^2$. At a $u$-generic point the latter is $\mathrm{SO}(u^\perp)$ [Zar]. Its preimage in $\mathrm{Spin}(H^2)$ is the connected group $\mathrm{Spin}(u^\perp)$, which has the same dimension as $H$. So $H = \mathrm{Spin}(u^\perp)$.

(b) Let $P = \langle \omega, \operatorname{Re}\sigma, \operatorname{Im}\sigma\rangle$. The periods $\sigma_t$ of the twistor line are the isotropic lines in $P_{\mathbb C}$, and they span $P_{\mathbb C}$. A rational class $x$ is of type $(1,1)$ at $t$ iff $q(x, \sigma_t) = 0$. If this holds for infinitely many $t$, then $x \perp P$, so $x \in \operatorname{NS}(Y_1) \cap \omega^\perp = \mathbb Z u$. A rational endomorphism $\varphi$ of $u^\perp_{\mathbb Q}$ is a Hodge endomorphism at $t$ iff it preserves $F^2 = \mathbb C\sigma_t$ and $F^1 = \sigma_t^\perp$, that is, iff $\varphi\sigma_t$ and $\varphi^\dagger\sigma_t$ lie in $\mathbb C\sigma_t$, where $\varphi^\dagger$ is the $q$-adjoint. These are closed analytic conditions on $t$. If $\varphi$ is Hodge at infinitely many $t$, it is Hodge at every $t$, including the point $Y_1$, and every isotropic line of $P_{\mathbb C}$ is an eigenline of $\varphi$. Hence $\varphi = c$ on $P_{\mathbb C}$ for some $c \in \mathbb R$. If $c \ne 0$, then $\varphi(T(Y_1))$ is a rational sub-Hodge structure whose complexification contains $\sigma$, so $\varphi(T(Y_1)) = T(Y_1)$, and the hypothesis gives $\varphi|_{T(Y_1)} = c \in \mathbb Q$. So $c \in \mathbb Q$ in all cases. Then $\ker(\varphi - c)$ is a rational subspace containing $P$. Its orthogonal complement in $u^\perp_{\mathbb Q}$ is rational and orthogonal to $\omega$ and $\sigma$, hence lies in $\operatorname{NS}(Y_1) \cap \omega^\perp \cap u^\perp = 0$. So $\varphi = c$. There are countably many rational classes and endomorphisms, and each one that is not of the allowed kind is Hodge at only finitely many $t$. $\square$

### 3.2 What a $u$-seed would give

**Proposition 3.4.** Let $Y_0$ be $u$-generic with a $u$-seed $W_0$ of multiplier $\lambda$. Let $S$ be a K3 surface with $\operatorname{Pic}(S) = \mathbb Z h$, $h^2 = 2d$, and suppose that $u$ lies in the monodromy orbit of $a h + c\delta \in H^2(S^{[n]}, \mathbb Z)$, where $2\delta$ is the class of the exceptional divisor. Suppose that $u^\perp$ contains an ample class of $S^{[n]}$. Then there are a K3 surface $\tilde W$ with $\operatorname{Pic}(\tilde W) \cong \mathbb Z$ and an algebraic cycle on $\tilde W \times S$ that induces a Hodge similarity $T(S)_{\mathbb Q} \to T(\tilde W)_{\mathbb Q}$ of multiplier $\lambda$. It is finite of degree $n$ over $\tilde W$.

*Proof.* Choose a marking of $S^{[n]}$ in the connected component of the marked moduli space containing $Y_0$ that sends $u$ to $ah + c\delta$. This is possible because the component is preserved by the monodromy group [Mar11]. Let $\Omega_u$ be the period domain of $u^\perp$. Any two $u$-generic points of $\Omega_u$ are joined by a twistor path whose junction points are $u$-generic. This is Buskin's argument [Bu, Def 4.14 and Prop 4.17] with "$\operatorname{Pic} = 0$" replaced by "$u$-generic" and Lemma 3.3(b) in place of [Bu, Lem 4.16], as in [B, Lemma 6.1]. It applies because $u^\perp$ has the signature $(3, 19)$ of the K3 lattice and, at a $u$-generic point, every positive class in $H^{1,1} \cap u^\perp_{\mathbb R}$ is Kähler up to sign, since $u$ is not a wall class. Along a twistor line, a subvariety that is trianalytic for the corresponding metric stays complex. At a $u$-generic point we may switch to the metric of any Kähler class orthogonal to $u$, by Proposition 3.2(b). So $W_0$ is carried to a $u$-seed $W_t$ at a $u$-generic point $Y_t$ on the twistor line of $(S^{[n]}, \omega_1)$, where $\omega_1 \perp u$ is a general ample class. Then $W_t$ is trianalytic for that metric, so it is a complex surface $W_1 \subset S^{[n]}$ whose normalization $\tilde W$ is a K3 surface, with $j^*u = 0$ and $j^*$ a $\lambda$-similarity on $u^\perp$, since $j^*$ is locally constant along the path. Pull back the universal family to get $\Gamma \subset \tilde W \times S$, finite of degree $n$ over $\tilde W$. Its action $\Gamma^*\colon H^2(S) \to H^2(\tilde W)$ is $j^*$ restricted to $H^2(S) \subset H^2(S^{[n]})$. Since $T(S) \subset u^\perp$, $\Gamma^*$ is a $\lambda$-similarity on $T(S)$, and its image is $T(\tilde W)$ because $\operatorname{NS}(\tilde W)_{\mathbb Q} = j^*(\operatorname{NS}(S^{[n]}) \cap u^\perp)_{\mathbb Q}$ has rank one. $\square$

So one $u$-seed proves ($\Psi_{\mathrm{ns}}$) for multiplier $\lambda$ for every K3 surface of degree $2d$ and Picard rank one, which is a $19$-dimensional family. By Proposition 6.1 the incidence cycle $\Gamma$ is Lagrangian only if $\lambda = nb$, which fails at every Hilbert point we computed (Section 6). So this is not Voisin's mechanism.

### 3.3 Effective cycles and special points

By Lemma 3.3(a), a $u$-seed has a $\mathrm{Spin}(u^\perp)$-invariant class in $H^{4n-4}(Y, \mathbb Q)$. The converse holds for effective cycles.

**Proposition 3.5.** Let $Y_1$ and $\omega$ be as in Lemma 3.3(b). Let $Z = \sum n_i Z_i$ be an effective cycle of dimension $2$, with $n_i > 0$, whose class is invariant under the $\mathrm{SU}(2)$ of the metric of $\omega$. Then every $Z_i$ is trianalytic and deforms to a $u$-seed.

*Proof.* For each complex structure $J$ of the twistor line, $\omega_J^2/2$ is a calibration, so $\int_{Z_i} \omega_J^2 \le \int_{Z_i} \omega^2$ with equality iff $Z_i$ is $J$-complex. This holds for singular $Z_i$, integrating over the regular locus [Ver95, Thm 3.1]. Summing with weights $n_i$ and using invariance of $[Z]$ gives equality, hence equality for each $i$. By Lemma 3.3(b), a general point $Y_t$ of the twistor line is $u$-generic, and $Z_i$ is complex there. The symplectic form of $Y_t$ does not vanish on $Z_i$, because the three Kähler forms restrict to the hyperkähler triple of the normalization [SV15, Thm 1.2]. So $Z_i$ is a $u$-seed at $Y_t$ by Proposition 3.2. $\square$

So a $u$-seed exists iff some positive multiple of an invariant class is effective at one such point. Since each component must itself be a $u$-seed, nonnegative combinations of known surfaces do not help. At a special point $Y_1$ the criterion becomes: a K3 surface $Z \subset Y_1$ with $j^*u = 0$ and $j^*$ a $\lambda$-similarity on $u^\perp$. Then $j^*\colon H^2(Y_1, \mathbb Q) \to H^2(\tilde Z, \mathbb Q)$ is surjective with kernel $\mathbb Q u$, so $\rho(\tilde Z) = \rho(Y_1) - 1$ and $u$ is determined by $Z$. At a very general Hilbert point the test reduces to four intersection numbers (Proposition 6.3). Three natural sources fail this test.
- *Fixed loci.* Let $Z$ be a component of the fixed locus of a finite group $G$ of symplectic automorphisms. Then $j^*g^* = j^*$, so $j^*$ kills the coinvariant lattice $H^2(Y_1)_G$. A kernel of rank one would need $H^2(Y_1)_G = \mathbb Z u$. Then the reflection-type isometry $x \mapsto x - 2\frac{q(x,u)}{q(u)}u$ must be integral, which needs $q(u) \mid 2\operatorname{div}(u)$. This fails for every admissible class with $n = 2, 3$ (Theorem 4.2(a), Proposition 5.1): there $|q(u)| > 2\operatorname{div}(u)$, except for $(q(u), \operatorname{div} u) = (-4, 1)$, where $4 \nmid 2$.
- *Isogeny images.* Let $A$ be an abelian surface, $C_3 \subset A$ a subgroup of order $3$ and $B = A/C_3$. The map $\pm(b + C_3) \mapsto \{[a], [a + c], [a + 2c]\}$ embeds a resolution of $\operatorname{Km}(B)$ in $\operatorname{Km}(A)^{[3]}$, with multiplier $3$ on the part coming from $A$. Since $A[2] \to B[2]$ is bijective, $j^*$ is an isometry on the $16$ nodal classes. Every hyperplane $u^\perp$ contains at least $15$ independent nodal directions, so $j^*$ is not a similarity on $u^\perp$.
- *Orbit surfaces.* Let $G \subset \operatorname{Aut}(S)$ be a finite group, let $g_1, \dots, g_n \in G$ be distinct, and let $Z \subset S^{[n]}$ be the closure of $\{g_1x + \dots + g_nx\}$. If $Z$ passes the criterion, then $\lambda$ is a square. Indeed, let $H$ be the stabilizer of $\{g_k\}$ under right translation. A general orbit is free, so $\tilde Z$ is birational to $S/H$, and $e = |H|$ is the degree of $S \to \tilde Z$. Since $\tilde Z$ is a K3 surface, $H$ acts trivially on $H^{2,0}(S)$. Write $u = y + c\delta$ with $y \in \operatorname{NS}(S)_{\mathbb Q}$ and $A = \sum_k g_k^*$. Restricting the criterion to $H^2(S)$ gives $A^\dagger A = e\lambda\bigl(1 - y \otimes q(y, \cdot)/q(u)\bigr)$, with eigenvalue $e\lambda \cdot 2(n-1)c^2/|q(u)| \ge 0$ on $y$. Here $A^\dagger = \sum_k (g_k^{-1})^*$ is also the adjoint for a $G$-invariant inner product, so $A^\dagger A$ is positive semidefinite, hence semisimple, and $\ker A^\dagger A = \ker A$ has dimension at most $1$. Semisimplicity excludes isotropic $y \ne 0$. $A^\dagger A$ preserves the rational isotypic components of $H^2(S, \mathbb Q)$, which are mutually orthogonal and nondegenerate, so for $y \ne 0$ the line $\mathbb Q y$ lies in one of them, $B_0$. On every other component $B$, $\det(A|_B)^2 = (e\lambda)^{\dim B}$ with $\det(A|_B) \in \mathbb Q$. The invariant component $H^2(S, \mathbb Q)^G$ is nonzero, and $A = n$ on it. If it is not $\mathbb Q y$, then $e\lambda = n^2$. If it is $\mathbb Q y$, then, since $22 - 1$ is odd, some other component has odd dimension, and $e\lambda$ is a square. Finally, $e = 1$. Since $\{g_k\}$ is a union of cosets $c_iH$, $A = (\sum_{h \in H} h^*)(\sum_i c_i^*)$ has image in $H^2(S)^H$. So $\dim \ker A \ge 22 - \dim H^2(S)^H$, and the $H$-coinvariant part of $H^2(S, \mathbb Q)$ has dimension at most $1$. If it is $0$, $H$ acts trivially on $H^2(S)$ and $H = 1$. If it is $1$, $H$ acts on this line through an injective character $H \to \{\pm 1\}$, so some $h \in H$ acts by $-1$ on it and trivially on $H^2(S)^H$, and so $h$ is a symplectic involution whose $(-1)$-eigenspace has dimension $1$. But a symplectic involution has $8$ isolated fixed points, by the holomorphic Lefschetz formula ($2 = \#\mathrm{Fix}/4$), so by the topological Lefschetz formula its $(-1)$-eigenspace has dimension $8$, a contradiction.

**Remark 3.6 (special points with larger endomorphism algebra).** The hypotheses on $Y_1$ in Lemma 3.3(b) can be dropped if $\omega$ is very general, that is, outside countably many proper linear subspaces of $H^{1,1}_{\mathbb R} \cap u^\perp_{\mathbb R}$. Then $\operatorname{NS}(Y_1) \cap \omega^\perp = \mathbb Z u$, because $q(y, \cdot)$ is a nonzero functional on $H^{1,1}_{\mathbb R} \cap u^\perp_{\mathbb R}$ for every nonzero $y \in \operatorname{NS}(Y_1)_{\mathbb Q} \cap u^\perp$, and every class in $\operatorname{NS}(Y_1)$ is a rational multiple of $u$ plus such a $y$. In the proof of Lemma 3.3(b), an endomorphism $\varphi$ that is Hodge at infinitely many points satisfies $\varphi = c$ on $P$ for some $c \in \mathbb R$. If $\varphi \ne c$, its $c$-eigenvectors in $H^{1,1}_{\mathbb R} \cap u^\perp_{\mathbb R}$ form a proper subspace, because $\varphi = c$ on $\operatorname{Re}\sigma$ and $\operatorname{Im}\sigma$. A very general $\omega$ avoids these subspaces for all rational $\varphi$ and all their eigenvalues. So $\varphi = c$, and $c \in \mathbb Q$ because $\varphi$ is rational. Hence Proposition 3.5 and the criterion at special points apply at every point of the $u$-family at which $u^\perp$ contains a Kähler class, including points with complex multiplication.

## 4. Chern-class constraints and the $K3^{[2]}$ case

### 4.1 The class of a $u$-seed

Let $Y$ be $u$-generic of $K3^{[n]}$-type and $W$ a $u$-seed of multiplier $\lambda$, with normalization $j\colon \tilde W \to Y$. By Lemma 3.3(a), $[W] \in H^{4n-4}(Y, \mathbb Q)$ is $\mathrm{Spin}(u^\perp)$-invariant.

**Lemma 4.1.** In this situation:
- (a) $\int_W x\,y = \lambda\bigl(q(x, y) - q(x, u)\,q(y, u)/q(u)\bigr)$ for all $x, y \in H^2(Y, \mathbb Q)$;
- (b) $\lambda \in \mathbb Z$, and $2|q(u)|$ divides $\lambda \operatorname{div}(u)^2$;
- (c) if $n \in \{2, 3\}$, then $\int_W c_2(Y) = 22\,\kappa_n\,\lambda$ with $\kappa_n = 6(n+3)/(2n+21)$, and this is an integer. For $n = 2$ this means $5 \mid \lambda$, and for $n = 3$ it means $3 \mid \lambda$.

*Proof.* (a) is Proposition 3.2(a)–(b). (b) $q_{\tilde W}(j^*x)$ is an even integer for $x \in H^2(Y, \mathbb Z)$. Write $H^2(Y, \mathbb Z) = U^3 \oplus M$. The projection of $u$ to the unimodular lattice $U^3$ is an integral multiple of a primitive vector, which is equivalent to $e_1 + kf_1$ by Eichler's criterion [GHS09, Prop 3.3]. So $u^\perp$ contains a hyperbolic plane, some $x \in u^\perp$ has $q(x) = 2$, and $2\lambda \in 2\mathbb Z$. For $x$ with $q(x, u) = \operatorname{div}(u)$, (a) gives $\lambda q(x) - \lambda \operatorname{div}(u)^2/q(u) \in 2\mathbb Z$, and $\lambda q(x)$ is even. (c) The class $c_2(Y)$ is invariant under the monodromy, hence under $\mathrm{Spin}(H^2)$. For $n = 2$ and $n = 3$, $H^4(Y, \mathbb Q)$ is $\operatorname{Sym}^2 H^2$, respectively $\operatorname{Sym}^2 H^2 \oplus H^2$, as a $\mathrm{Spin}(H^2)$-module [GKLR, Cor 3.2 and Rem 3.3]. So its invariants form one line, and $c_2(Y)$ lies in the line spanned by $Q = \sum_i e_i e^i \in \operatorname{Sym}^2 H^2$, where $(e^i)$ is the $q$-dual basis; write $c_2 = \kappa_n Q$. Riemann–Roch with $\chi(L) = \binom{q(L)/2 + n + 1}{n}$ [EGL01] gives $\int c_2\, x^{2n-2} = 6(n+3)(2n-3)!!\,q(x)^{n-1}$, and the generalized Fujiki relation gives $\int Q\, x^{2n-2} = (2n+21)(2n-3)!!\,q(x)^{n-1}$. This gives $\kappa_n$. By (a), $\int_W Q = \sum_i \int_W e_i e^i = \lambda(23 - 1)$. $\square$

### 4.2 Fourfolds

**Theorem 4.2.** Let $Y$ be $u$-generic of $K3^{[2]}$-type, and let $W \subset Y$ be a $u$-seed of multiplier $\lambda$. Let $2d$ be the degree of the double point class $\mathbb D(j)$ of $j\colon \tilde W \to Y$ [Ful98, Thm 9.3]. Then $d$ is a nonnegative integer, and:
- (a) $q(u) = -2m'^2$ for an integer $m' \ge 2$;
- (b) $\lambda = 10(1 + m)$ and $d = 66m^2 - 54$ for an integer $m \ge 1$; in particular $W$ is not smooth;
- (c) $[W] = \frac{\lambda}{20}\,c_2(Y) - \frac{\lambda}{2q(u)}\,u^2$, and this class is integral.

The smallest multiplier allowed by (a)–(c) and Lemma 4.1(b) is $\lambda = 50$, with $q(u) = -50$, $\operatorname{div}(u) = 2$ and $d = 1002$. The next ones are $\lambda = 80$ ($q(u) = -8$, $\operatorname{div}(u) = 1$, $d = 3180$) and $\lambda = 90$ ($q(u) = -18$, $\operatorname{div}(u) = 2$, $d = 4170$). Theorem 6.5 shows that in fact no $u$-seed of $K3^{[2]}$-type exists; its proof uses (a) and (c).

*Proof.* (c) In $H^4(Y, \mathbb Q) = \operatorname{Sym}^2 H^2(Y, \mathbb Q)$ the $\mathrm{SO}(u^\perp)$-invariants are spanned by $c_2(Y)$ and $u^2$. Write $[W] = \alpha c_2 + \beta u^2$ and pair with $xy$. With $\int x y z w = q(x,y)q(z,w) + q(x,z)q(y,w) + q(x,w)q(y,z)$ and $\int c_2\,xy = 30\,q(x,y)$, Lemma 4.1(a) becomes $30\alpha + \beta q(u) = \lambda$ and $2\beta = -\lambda/q(u)$. So $\alpha = \lambda/20$ and $\beta = -\lambda/(2q(u))$. The class $[W]$ is integral because $W$ is a subvariety.

(b) By [SV15, Thm 1.2], $j$ is an immersion. The double locus $D = \{(a, b) \in \tilde W \times \tilde W : a \ne b,\ j(a) = j(b)\}$ is closed, because $j$ is locally injective. It is analytic for every induced complex structure of the product hyperkähler structure, so it is trianalytic and has even complex dimension. It is not $2$-dimensional, because $j$ is birational onto $W$. So $D$ is finite, of the expected dimension $2 \cdot 2 - 4 = 0$. Since $j$ is unramified, the diagonal is open and closed in $\tilde W \times_Y \tilde W$. So the double point class of [Ful98, §9.3] is the part on $D$ of the intersection product of $\tilde W \times \tilde W$ with the diagonal of $Y \times Y$, and $\mathbb D(j)$ is a $0$-cycle supported on $D$. Since $D$ is finite, this intersection is proper there. $\tilde W \times \tilde W$ is smooth, hence Cohen–Macaulay, and the diagonal is a regular embedding, so each multiplicity is the length of the local ring and is positive [Ful98, Ch. 7]. The involution $(a, b) \mapsto (b, a)$ acts on $D$ without fixed points and preserves these multiplicities, so the degree of $\mathbb D(j)$ is even and $d \in \mathbb Z_{\ge 0}$. The double point formula gives $[W]^2 = \int_{\tilde W} c_2(N_j) + 2d$. Since $c_1(\tilde W) = 0$, we have $c_2(N_j) = j^*c_2(Y) - c_2(\tilde W)$, so $[W]^2 = \int_W c_2(Y) - 24 + 2d$. From (c), with $\int c_2^2 = 828$ and $\int u^4 = 3q(u)^2$,
$$[W]^2 = \tfrac{33}{25}\lambda^2, \qquad \int_W c_2(Y) = \tfrac{132}{5}\lambda,$$
so $33\lambda^2 - 660\lambda + 600 = 50d$. Reducing modulo $5$ gives $5 \mid \lambda$. Put $\lambda = 5t$; then $33t^2 - 132t + 24 = 2d$, so $t$ is even. Put $t = 2(1 + m)$; then $d = 66m^2 - 54$. Since $\lambda > 0$ and $d \ge 0$, $m \ge 1$, and then $d \ge 12$.

(a) By Proposition 3.2(c), $u^\perp_{\mathbb Q}(\lambda) \cong H^2(\tilde W, \mathbb Q) \cong \Lambda_{\mathbb Q}$, where $\Lambda$ is the K3 lattice. For every $\lambda \in \mathbb Q_{>0}$, $\Lambda_{\mathbb Q}(\lambda) \cong \Lambda_{\mathbb Q}$. Indeed, $U(\lambda) \cong U$ over $\mathbb Q$, $E_8 \otimes \mathbb Q \cong \langle 1\rangle^8$ by the Hasse–Minkowski theorem, and $\langle \lambda \rangle^4 \cong \langle 1\rangle^4$ because left multiplication by a quaternion of norm $\lambda$ is a similarity of the norm form. So $u^\perp_{\mathbb Q} \cong \Lambda_{\mathbb Q}$. Since $u^\perp \oplus \langle q(u)\rangle$ and $\Lambda \oplus \langle -2\rangle$ are rationally isometric, Witt cancellation gives $q(u) \in -2\,\mathbb Q^{\times 2}$, so $q(u) = -2m'^2$ with $m' \in \mathbb Z_{>0}$. If $m' = 1$, then $q(u) = -2$. By [BM14, Thm 12.1], applied to $v = (1, 0, -1)$, the wall divisors of $S^{[2]}$ are the classes with $q = -2$, and those with $q = -10$ and divisibility $2$. Wall divisors are deformation invariant [Mon15, AV], so $u$ is a wall class, and no Kähler class is orthogonal to it. This contradicts the standing assumption of Section 3.1.

For the list, $\lambda = 10(1 + m)$ and Lemma 4.1(b) require $4m'^2 \mid 10(1+m)\operatorname{div}(u)^2$ with $\operatorname{div}(u) \in \{1, 2\}$, and $\operatorname{div}(u) = 2$ is possible only for odd $m'$. For $\lambda < 81$ this leaves $(\lambda, q(u), \operatorname{div} u) = (50, -50, 2)$ and $(80, -8, 1)$. The integrality of $[W]$ was checked in exact arithmetic in an integral basis of $H^4(S^{[2]}, \mathbb Z)$ (Appendix A). Neither $(q, \operatorname{div}) = (-50, 2)$ nor $(-8, 1)$ is a wall class. $\square$

In every case we scanned ($2 \le m' \le 8$, $1 \le m \le 39$, both divisibilities), $[W]$ is integral exactly when Lemma 4.1(b) holds. So for fourfolds the cohomology does not exclude a $u$-seed, but it forces a singular surface with at least $1002$ double points, counted with multiplicity, and multiplier at least $50$. The only trianalytic K3 surfaces in manifolds of $K3^{[2]}$-type that we know are the fixed K3 surfaces of symplectic involutions, such as $W_g$ in Section 3.1. There $j^*$ kills the coinvariant lattice $L \cong E_8(-2)$ and is a similarity of multiplier $2$ on $L^\perp$, and $d = 0$. For a lattice $L$ of rank $\ell$ in place of $\mathbb Z u$, the same computation gives $[W]^2 = \lambda^2(2+\ell)(23-\ell)/50$ and $\int_W c_2 = \frac{6}{5}\lambda(23-\ell)$, and $(\ell, \lambda, d) = (8, 2, 0)$ satisfies the double point formula.

## 5. Sixfolds: the first case that cohomology allows

For $n = 3$ there is no self-intersection constraint, because $[W]^2 \in H^{16}(Y) = 0$. The constraints come from lattices and from integrality in $H^8$. We write $H^2(Y, \mathbb Z) = \Lambda \oplus \mathbb Z\delta$ with $q(\delta) = -4$, and $\operatorname{div}(u) \in \{1, 2, 4\}$ for the divisibility of $u$.

### 5.1 Lattice conditions and walls

**Proposition 5.1.** Let $Y$ be $u$-generic of $K3^{[3]}$-type with a $u$-seed of multiplier $\lambda$. Then:
- (a) $q(u) = -4k^2$ for an integer $k \ge 1$;
- (b) $3 \mid \lambda$ and $8k^2 \mid \lambda \operatorname{div}(u)^2$;
- (c) $(q(u), \operatorname{div}(u))$ is not one of $(-4, 4)$, $(-4, 2)$, $(-36, 4)$.

The admissible pairs with $k \le 5$ and their smallest multipliers are listed in Table 1.

*Proof.* (a) As in Theorem 4.2(a), $u^\perp_{\mathbb Q} \cong \Lambda_{\mathbb Q}$, and Witt cancellation against $\Lambda \oplus \langle -4\rangle$ gives $q(u) \in -\mathbb Q^{\times 2}$. Since $q(u)$ is even, $q(u) = -4k^2$. (b) is Lemma 4.1(b)–(c). (c) By [BM14, Thm 12.1] with $v = (1, 0, -2)$, the walls of $S^{[3]}$ are the classes $4a - (v, a)v$, made primitive, for $a$ in the algebraic Mukai lattice with $a^2 \ge -2$ and $0 \le (v, a) \le 2$. A short computation gives the pairs $(q, \operatorname{div}) = (-2, 1)$, $(-36, 4)$, $(-4, 4)$, $(-12, 2)$ and $(-4, 2)$. By deformation invariance [Mon15, AV], a class of one of these types is a wall class at a $u$-generic point, so no Kähler class is orthogonal to it. $\square$

The pair $(-4, 4)$ is the orbit of $\delta$. Its $u$-family consists of Hilbert schemes $S^{[3]}$ with $\operatorname{Pic}(S) = 0$, where Verbitsky's theorem [Ver98, Thm 9.12] also excludes seeds.

**Table 1.** Admissible $(q(u), \operatorname{div} u)$ for $K3^{[3]}$-type, $k \le 5$. The column $\lambda_{\min}$ is the smallest multiplier allowed by Proposition 5.1(b), and "class" is $\lambda_{\min}$ modulo squares. The column $m = 4k/\operatorname{div}(u)$ is explained in Remark 5.3. The last two columns record Proposition 5.2 and the existence of a Hilbert model $u = ah - c\delta$ on $S^{[3]}$, $\operatorname{Pic} S = \mathbb Z h$, with $u^\perp$ meeting the ample cone as computed from [BM14b, Prop 10.3].

| $q(u)$ | div | $\lambda_{\min}$ | class | $m$ | $H^8$ | Kähler-compatible Hilbert model |
|---|---|---|---|---|---|---|
| $-4$ | 1 | 24 | 6 | 4 | pass | not known |
| $-16$ | 1 | 96 | 6 | 8 | pass | not known |
| $-36$ | 2 | 18 | 2 | 6 | pass | not known |
| $-36$ | 1 | 72 | 2 | 12 | pass | not known |
| $-64$ | 1 | 384 | 6 | 16 | pass | not known |
| $-100$ | 4 | 75 | 3 | 5 | pass | genus 4: $u = 4h - 7\delta$ |
| $-100$ | 2 | 150 | 6 | 10 | pass | not known |
| $-100$ | 1 | 600 | 6 | 20 | pass | not known |

"Not known" means that [BM14b, Prop 10.3], which needs $\deg h \le 6$ for $n = 3$, gives no such model. It does not mean that none exists. For $k = 7$, the pair $(-196, 4)$ has the genus-$2$ model $u = 8h - 9\delta$, with $\lambda_{\min} = 147$, again of class $3$.

Each pair in Table 1 is a single monodromy orbit. The monodromy group acts on the discriminant group $\mathbb Z/4$ by $\pm 1$ [Mar11], and Eichler's criterion [GHS09, Prop 3.3] determines the orbit of a primitive class by $q(u)$ and $\pm[u/\operatorname{div}(u)]$, which is fixed by $\operatorname{div}(u)$ here.

### 5.2 Integrality in $H^8$

**Proposition 5.2.** For each pair in Table 1, at $\lambda = \lambda_{\min}$, there is a $\mathrm{Spin}(u^\perp)$-invariant class in $H^8(Y, \mathbb Z)$ whose pairing with $\operatorname{Sym}^2 H^2$ is the one required by Lemma 4.1(a).

*Proof sketch.* By Poincaré duality and torsion-freeness [Mar07], a class $\xi \in H^8(Y, \mathbb Q)$ is integral iff $\int \xi\, x \in \mathbb Z$ for all $x \in H^4(Y, \mathbb Z)$. Rationally $H^4 = \operatorname{Sym}^2 H^2 \oplus H'$, where $H' \cong H^2$ as a representation of $\mathfrak{so}(H^2)$; for $n = 3$, $b_4 = 299 = 276 + 23$. A $\mathrm{Spin}(u^\perp)$-invariant functional on $H^4$ is $\lambda A + \nu B$. Here $A(xy) = q(x, y) - q(x, u)q(y, u)/q(u)$, $B$ is the pairing of $H'$ with the $u$-direction, and $\nu \in \mathbb Q$ is free. By Markman [Mar07], $H^4(Y, \mathbb Z)$ is spanned by products of two classes in $H^2$ and by the classes $c_2(E_w)$, where $E_w = -R\pi_*(\mathcal I_Z^\vee \otimes F_w)$ for $w$ in the Mukai lattice. This gives four conditions:
- (S) integrality on $\operatorname{Sym}^2 H^2(Y, \mathbb Z)$, which is Lemma 4.1(b);
- (C2) $\int_W c_2(Y) \in \mathbb Z$, that is, $3 \mid \lambda$. By Kapfer [Kap16, Prop 2.2], $H^4(S^{[3]}, \mathbb Z)/\operatorname{Sym}^2 H^2 \cong \mathbb Z/3 \oplus \mathbb Z^{23}$, and $c_2$ represents the torsion;
- (i) $\int_W c_2(E_w) \in \mathbb Z$ for $w \perp v$. This determines $\nu$ modulo $\operatorname{div}(u)^{-1}\mathbb Z$;
- (ii) $\int_W [\Delta_x] \in \mathbb Z$, where $\Delta_x = c_2(E_{w_1})$ for the point class $w_1$ is the locus of subschemes containing a fixed point $x$.

For (ii) we computed the $\operatorname{Sym}^2$-component of $[\Delta_x]$ as $\Sigma/24 + \delta^2/48$, where $\Sigma \in \operatorname{Sym}^2 \Lambda$ is the dual form. This uses three pairings with $\operatorname{Sym}^4 H^2$, which is orthogonal to $H'$. They are computed on the nested Hilbert scheme. Two of the pairings determine the coefficients, and the third agrees with them. For each pair, a value of $\nu$ satisfies (i) and (ii) simultaneously (Appendix A). As a control, replacing $(1/24, 1/48)$ by $(1/12, 1/16)$ makes $(-36, 2)$ fail. It does not change the verdict for the other pairs, so for them these conditions have little discriminating power. $\square$

The hidden inputs of this sketch are: Markman's integral generators; the equivariance of the normalized universal class, which is used to write the $H'$-part of $\int_W c_2(E_w)$ as $\nu\,q(w_\perp, u)$; and the transversality used in the nested-Hilbert-scheme pairings. So Proposition 5.2 says that the computations we can do find no obstruction. It does not construct a class.

**Remark 5.3 (twisted moduli; heuristic).** In the Mukai lattice $\tilde H$ of $Y$, with $v^2 = 4$ and $H^2(Y) = v^\perp$, the saturation $A$ of $\langle v, u\rangle$ has discriminant $-(4k/\operatorname{div} u)^2$. So $A$ contains an isotropic class, and $Y$ should be a moduli space of twisted sheaves on a K3 surface $S'$ with $\operatorname{Pic}(S') = 0$ and a Brauer class of order $m = 4k/\operatorname{div}(u)$. A non-locally-free sheaf in such a space needs a Mukai vector $v'$ with $v'^2 = 4 - 2rk \ge -2$, so rank $\le 3$, and all ranks are divisible by $m$. If such sheaves exist, their Quot-scheme fibres are rational curves with class proportional to the dual of $u$, so $u$ is a wall class [AV]. The rule "a wall iff $m \le 3$" gives exactly the three excluded pairs in Proposition 5.1(c), with $m = 1, 2, 3$. Every admissible pair has $m \ge 4$. If this picture is right, a $u$-seed is a projectively hyperholomorphic twisted bundle on $W \times S'$, and both factors have Picard rank zero. We have not checked the inputs (moduli of twisted sheaves at Picard rank zero, the Uhlenbeck compactification, and that the Quot curves are nonzero in homology), so we use this remark only as a cross-check of Table 1.

## 6. Hilbert points

By Proposition 3.4, a $u$-seed can be studied at any Hilbert point $S^{[n]}$ of the $u$-family at which $u^\perp$ contains an ample class. There the seed becomes a concrete object, a $2$-dimensional family of length-$n$ subschemes of $S$, and its invariants can be read off from $S$.

### 6.1 The incidence correspondence

Let $W \subset S^{[n]}$ be a $u$-seed of multiplier $\lambda$ at such a point, with normalization $j\colon \tilde W \to S^{[n]}$, and assume $W \not\subset E$, where $E$ is the exceptional divisor. Let $\Gamma \subset \tilde W \times S$ be the pullback of the universal subscheme. It has degree $n$ over $\tilde W$, and we write $b$ for its degree over $S$. Then $b = \int_W [\Delta_x]$, where $\Delta_x \subset S^{[n]}$ is the locus of subschemes containing a fixed general point $x$.

**Proposition 6.1.** $\lambda \le n b$, with equality iff $\Gamma$ is Lagrangian for $\mathrm{pr}_W^*\sigma_W - c\,\mathrm{pr}_S^*\sigma_S$ for some $c$.

*Proof.* Over a general point $w \in \tilde W$ the subscheme is reduced, with local sheets $\varphi_1, \dots, \varphi_n$ of $\Gamma \to \tilde W$. Write $\varphi_i^*\sigma_S = f_i\,\sigma_W$, with $f_i$ the branches of a meromorphic function $f$ on the normalization of $\Gamma$. The symplectic form of $S^{[n]}$ is induced by $\sum_i \mathrm{pr}_i^*\sigma_S$ on $S^n$, so $j^*\sigma = (\sum_i f_i)\,\sigma_W$, and $\sum_i f_i = \mu$ is a constant. Since $j^*$ is a $\lambda$-similarity on $u^\perp \ni \sigma$ (proof of Proposition 3.4), $|\mu|^2 \int_{\tilde W} \sigma_W\bar\sigma_W = \lambda \int_S \sigma_S\bar\sigma_S$. Integrating $\mathrm{pr}_S^*(\sigma_S\bar\sigma_S)$ over $\Gamma$ gives $b\int_S \sigma_S\bar\sigma_S = \int_{\tilde W} (\sum_i |f_i|^2)\,\sigma_W\bar\sigma_W$. By Cauchy–Schwarz, $|\sum f_i|^2 \le n \sum |f_i|^2$ pointwise, so $\lambda \le n b$. Equality holds iff all $f_i$ are equal at a general point. Then $f = \mu/n$ is constant and $\Gamma$ is Lagrangian with $c = n/\mu$. Conversely, if $\Gamma$ is Lagrangian, $f$ is constant and equality holds. $\square$

Let $\iota$ be a symplectic involution of $S$. The surface $\{x + \iota x\} \subset S^{[2]}$, whose normalization is the Nikulin K3 surface resolving $S/\iota$, is the case of equality: $n = 2$, $b = 1$, $\lambda = 2$, and $\Gamma$ is the graph of $S \dashrightarrow S/\iota$. This is the multiplier-$2$ similarity used by Varesco [Var23, proof of Thm 2.1]. So is the surface $\operatorname{Km}(A/C_3) \subset \operatorname{Km}(A)^{[3]}$ of Section 3.3 on the part coming from $A$: a point lies in exactly one triple, so $b = 1$, the multiplier is $3$, and $\Gamma$ is the graph of the quotient map $\operatorname{Km}(A) \dashrightarrow \operatorname{Km}(A/C_3)$, which is Lagrangian. The surface $W_g$ of Section 3.1 has strict inequality. A general point $y$ lies in $y + gy$ and in $g^{-1}y + y$, so $b = 2$, while $\lambda = |1 + i|^2 = 2 < nb = 4$; its two sheets have $f = 1$ and $f = i$. (None of these examples is a $u$-seed; all are trianalytic K3 surfaces for which the same computation applies.) So a trianalytic K3 surface need not give a Lagrangian correspondence. For a $u$-seed, whether it does is decided by the single integer $b$, and $b$ is computed by the class of $\Delta_x$.

For $n = 3$, the $\operatorname{Sym}^2$-component of $[\Delta_x]$ is $\Sigma/24 + \delta^2/48$ (Section 5.2). Pairing with Lemma 4.1(a) gives
$$b = \lambda\Bigl(\tfrac{1}{24}A(\Sigma) + \tfrac{1}{48}A(\delta^2)\Bigr) + \nu\,B(\Delta_x),$$
where $\nu$ is the free parameter of Section 5.2 and the last term is the $H'$-contribution. Since $[\Delta_x] = c_2(E_{w_1})$ and the projection of $w_1 = (0, 0, -1)$ to $v^\perp$ is $-\delta/4$, that term is proportional to $q(u, \delta)$. So when $u \perp \delta$, $b$ does not depend on $\nu$. For instance, the class $u = e - 2f$ in a hyperbolic plane of $\Lambda_{K3}$ has $A(\Sigma) = 21$ and $A(\delta^2) = -4$, so $b = 19\lambda/24$. This lies strictly between $\lambda/3$ and $\lambda$, so a seed at such a point would not be Lagrangian. (That point has a non-projective $S$; it serves only as a check of the formula.)

### 6.2 The genus-4 model

Let $S = Q \cap C \subset \mathbb P^4$ be a general complete intersection of a quadric and a cubic, so that $\operatorname{Pic}(S) = \mathbb Z h$ with $h^2 = 6$, and let $u = 4h - 7\delta \in H^2(S^{[3]}, \mathbb Z)$. Then $q(u) = -100$ and $\operatorname{div}(u) = 4$, which is the pair $(-100, 4)$ of Table 1, with $\lambda_{\min} = 75$ of class $3$.

By [BM14b, Prop 10.3] (with $d = 3$, $n = 3$), $\operatorname{Nef}(S^{[3]}) = \langle h, h - \delta\rangle$. The boundary ray $h - \delta$ is contracted by the Lagrangian $\mathbb P^3 \subset S^{[3]}$ of lines of $Q$, each of which meets $S$ in three points. Since $q(u, h + t\delta) = 24 + 28t$ vanishes at $t = -6/7 \in (-1, 0)$, the class $h - \tfrac67\delta$ is ample and orthogonal to $u$. So Proposition 3.4 applies at this point.

**Proposition 6.2.** Suppose a $u$-seed of multiplier $75$ exists in the $(-100, 4)$-family. Then $S^{[3]}$ contains a surface $W \not\subset \mathbb P^3$ whose normalization $\tilde W$ is a K3 surface with $\operatorname{Pic}(\tilde W) = \mathbb Z g$, and:
- (a) $T(\tilde W)_{\mathbb Q} \cong T(S)_{\mathbb Q}(3)$ as Hodge structures, and either $g^2 = 2$, $j^*h = 21g$, $j^*\delta = 12g$, or $g^2 = 18$, $j^*h = 7g$, $j^*\delta = 4g$;
- (b) if $W \not\subset E$, the integer $b$ of Section 6.1 satisfies $b \equiv 6 \pmod 7$ and $b \ge 27$. In particular $b \ne \lambda/3$, so $\Gamma$ is not Lagrangian;
- (c) if moreover $W$ meets the locus $E_3$ of subschemes supported at one point in finitely many points and does not meet the surface $\{\mathfrak m_x^2 : x \in S\} \subset E_3$, $\Gamma$ is normal, and $\Gamma$ has at most canonical singularities, then $b \in \{90, 97, 104, 111, 118, 125\}$.

*Proof.* (a) By Proposition 3.4 and its proof, $W$ exists at this point with $j^*u = 0$ and $j^*$ a $75$-similarity on $u^\perp$. So $4\,j^*h = 7\,j^*\delta$, and $\int_{\tilde W} (j^*h)^2 = \lambda\, q_{u^\perp}(h) = 75 \cdot \tfrac{294}{25} = 882 = 2 \cdot 21^2$, where $q_{u^\perp}$ is $q$ on the projection to $u^\perp$. Write $j^*h = 7k\,g$; then $k^2 g^2 = 18$ with $g^2$ even, so $(k, g^2) = (3, 2)$ or $(1, 18)$. A surface in $\mathbb P^3$ is isotropic for $\sigma$, so it is not a seed. (b) Condition (i) of Section 5.2 fixes $\nu$ modulo $\tfrac14\mathbb Z$. Inserting the allowed $\nu$ into the formula for $b$ of Section 6.1 and requiring $b \in \mathbb Z$ gives $b \equiv 6 \pmod 7$ (Appendix A). The bound $b \ge 25$ is Proposition 6.1, and $25 \not\equiv 6$. (c) The universal family is flat of degree $3$, so $\Gamma \to \tilde W$ is a triple cover. Its fibres are Gorenstein, because the only non-Gorenstein subschemes of length $3$ are the $\mathfrak m_x^2$. So it is a Gorenstein triple cover with $\pi_*\mathcal O_\Gamma = j^*\mathcal O^{[3]} = \mathcal O \oplus \mathcal E^\vee$, where $c_1(\mathcal E) = j^*\delta$ and $c_1(\mathcal E)^2 = 288$. By Lehn [Leh99, Thm 4.6], $[E_3] = 3\,c_2(\mathcal O^{[3]})$, and $c_2(\mathcal O^{[3]}) = [\Delta_x] + c_2(E_{\tilde\delta})$ with $\tilde\delta = (1, 0, 2)$, because $\operatorname{ch}(E_w)$ is linear in $w$ and $c_1(E_{w_1}) = 0$. With $\nu$ eliminated in favour of $b$ this gives
$$\int_W [E_3] = 1149 - 9b, \quad c_2(\mathcal E) = 383 - 3b, \quad \chi(\mathcal O_\Gamma) = 3b - 233, \quad K_\Gamma^2 = 9b - 573,$$
using Riemann–Roch for $\mathcal E^\vee$ and the following computation of $K_\Gamma^2$. A Gorenstein triple cover embeds in $P = \mathbb P(\mathcal E)$ as a divisor of class $3\xi - \pi^*c_1$, where $\xi = \mathcal O_P(1)$ and $c_i = c_i(\mathcal E)$ [Mir85]. Since $K_{\tilde W} = 0$, $K_P = -2\xi + \pi^*c_1$, so adjunction gives $K_\Gamma = \xi|_\Gamma$. With $\xi^2 = c_1\xi - c_2$ we get $\xi^3 = c_1^2 - c_2$ and $\xi^2\pi^*c_1 = c_1^2$, hence $K_\Gamma^2 = 3\xi^3 - \xi^2\pi^*c_1 = 2c_1^2 - 3c_2$. (For the cyclic cover with $\mathcal E = M \oplus 2M$ this gives $12M^2$, as it should.) Each component of the resolution $\tilde\Gamma$ maps finitely onto $\tilde W$, so it carries the nonzero $2$-form $\mathrm{pr}_W^*\sigma_W$, is not ruled, and has $\chi(\mathcal O) \ge 0$. Since $\Gamma$ is normal, its components are disjoint, so $\chi$ and $K^2$ are sums over them. The three hypotheses give, in order, $1149 - 9b \ge 0$, $\chi(\mathcal O_\Gamma) \ge \chi(\mathcal O_{\tilde\Gamma}) \ge 0$, and $K^2 \le 9\chi$ by Miyaoka–Yau on the minimal model of each component. So $85 \le b \le 127$. $\square$

As a consistency check, the branch curve of $\Gamma \to \tilde W$ lies in $|2c_1(\mathcal E)| = |j^*(2\delta)|$, which is the class of $W \cap E$, the nonreduced triples. For $b \ge 104$, $4c_2(\mathcal E) - c_1(\mathcal E)^2 < 0$, so $\mathcal E$ is Bogomolov-unstable.

Proposition 6.2 is a set of necessary conditions. We have not found a $2$-dimensional family of triples on $S$, outside the $\mathbb P^3$, with these invariants.

### 6.3 A numerical test

At a Hilbert point with $\operatorname{End}_{\mathrm{Hdg}} T(S)_{\mathbb Q} = \mathbb Q$, the pairing $\int_W xy$ restricted to $T(S)$ is a multiple of $q$ for every surface $W$, and four numbers decide the rest.

**Proposition 6.3.** Let $S$ be a K3 surface with $\operatorname{Pic}(S) = \mathbb Z h$ and $\operatorname{End}_{\mathrm{Hdg}} T(S)_{\mathbb Q} = \mathbb Q$. Let $Y = S^{[n]}$ with $n \in \{2, 3\}$ and $N = \langle h, \delta\rangle$, and let $u \in N$ be primitive with $q(u) < 0$ such that $u^\perp$ contains an ample class $\omega$. For an irreducible surface $W \subset Y$ and $\lambda > 0$, the following are equivalent:
- (a) $W$ is trianalytic for the metric of $\omega$, its normalization $\tilde W$ is a K3 surface, $j^*u = 0$, and $j^*$ is a $\lambda$-similarity on $u^\perp$;
- (b) $\int_W xy = \lambda\,q_{u^\perp}(x, y)$ for $x, y \in N$, and $\int_W c_2(Y) = 22\kappa_n\lambda$.

In this case $W$ deforms to a $u$-seed of multiplier $\lambda$ along the twistor line of $(Y, \omega)$.

*Proof.* (a) implies (b) by the computation in Lemma 4.1(a) and (c), which uses only the similarity. Conversely, let $B(x, y) = \int_W xy$ on $H^2(Y, \mathbb Q) = T(S)_{\mathbb Q} \oplus N_{\mathbb Q}$. It is a Hodge class, so it is invariant under the Hodge group, which is $\mathrm{SO}(T(S)_{\mathbb Q})$ acting trivially on $N$ [Zar]. Since $\operatorname{rk} T(S) = 21$, the invariant symmetric forms on $T(S)_{\mathbb Q}$ are the multiples of $q$, and there are no invariant vectors. So $B = \alpha q$ on $T(S)$ for some $\alpha$, and $B(T(S), N) = 0$. Split the dual tensor $Q$ of Lemma 4.1(c) as $Q_T + Q_N$. Then $B(Q_T) = 21\alpha$. By (b), $B(Q_N) = \lambda(2 - 1) = \lambda$ and $B(Q) = \kappa_n^{-1}\int_W c_2(Y) = 22\lambda$. So $\alpha = \lambda$, and $B = \lambda\,q_{u^\perp}$ on all of $H^2(Y)$. Both sides of Lemma 3.1 for $\omega$ equal $\lambda$, so $W$ is trianalytic. Its normalization is then a smooth hyperkähler surface [SV15, Thm 1.2]. Since $B$ is nondegenerate on $u^\perp$, $j^*$ is injective on $u^\perp_{\mathbb Q}$, so $\tilde W$ is a K3 surface and $j^*\colon u^\perp_{\mathbb Q} \to H^2(\tilde W, \mathbb Q)$ is bijective. Since $B(u, \cdot) = 0$, $j^*u$ is orthogonal to $H^2(\tilde W, \mathbb Q)$, so $j^*u = 0$. For the last statement, $\operatorname{NS}(Y) \cap \omega^\perp = \mathbb Z u$, so Lemma 3.3(b) applies, and the proof of Proposition 3.5 shows that $W$ is a $u$-seed at a general point of the twistor line. $\square$

In the genus-$4$ model of Section 6.2, $q_{u^\perp}$ has Gram matrix $\frac{1}{25}\bigl(\begin{smallmatrix}294 & 168\\ 168 & 96\end{smallmatrix}\bigr)$ in the basis $h, \delta$, and $22\kappa_3 = 88/3$. So, for a very general genus-$4$ K3 surface $S$, a surface $W \subset S^{[3]}$ deforms to a $u$-seed iff
$$\Bigl(\int_W h^2,\ \int_W h\delta,\ \int_W \delta^2,\ \int_W c_2(S^{[3]})\Bigr) = t\,(441, 252, 144, 1100) \quad \text{for some } t > 0,$$
and then $\lambda = 75t/2$. In the genus-$2$ model of Section 6.4 the vector is $(243, 216, 192, 2156)$ and $\lambda = 147t/2$. So whether a seed exists is decided by four intersection numbers of a single surface in $S^{[3]}$, for a single very general $S$. No information about $\tilde W$ or $j^*\sigma$ is needed.

### 6.4 Other Hilbert points

For genus $7$ ($h^2 = 12$) the classes $u = h \pm 2\delta$ give the pair $(-4, 1)$ with $\lambda_{\min} = 24$. For $u = h + 2\delta$, $q(u, h + t\delta) = 12 - 8t > 0$ on the ample cone, which has $t < 0$, so $u^\perp$ contains no ample class and Proposition 3.4 does not apply. For $u = h - 2\delta$, the orthogonal class $h - \tfrac32\delta$ lies outside the range of [BM14b, Prop 10.3], and we have not determined whether it is ample. The same computation as in Proposition 6.2 gives $\int_W[E_3] = 588 - 9b$ and $b$ odd in $[23, 65]$ under the same hypotheses. The pair $(-196, 4)$ has the genus-$2$ model $u = 8h - 9\delta$, $h^2 = 2$, with $\lambda_{\min} = 147$. Here $h - \tfrac49\delta$ is orthogonal to $u$ and ample by [BM14b, Prop 10.3], whose nef cone is $\langle h, h - \tfrac12\delta\rangle$. The argument of Proposition 6.2(a) gives $\int_{\tilde W}(j^*h)^2 = 147 \cdot \tfrac{162}{49} = 486$, so $j^*h = 9g$ and $j^*\delta = 8g$ with $g^2 = 6$: the partner $\tilde W$ has genus $4$. Integrality gives $b \equiv 5 \pmod 9$, so $b \ne \lambda/3 = 49$, and $\int_W [E_3] = 2049 - 9b$. Under the hypotheses of Proposition 6.2(c), $b \in \{176, 185, \dots, 221\}$. So a seed in this model, like one in the genus-$4$ model with $g^2 = 2$, would give an algebraic Hodge similarity of multiplier $3$ between K3 surfaces of degrees $2$ and $6$ of Picard rank one. The two models approach it from opposite sides.

In each case we computed, $\lambda/3$ is not an allowed value of $b$. So at these points the incidence correspondence of a $u$-seed is not Lagrangian, and Voisin's theorem cannot supply it.

### 6.5 No seeds of $K3^{[2]}$-type

The integer $b$ is bounded above as well as below.

**Lemma 6.4.** In the setting of Section 6.1, suppose that $\operatorname{Pic}(\tilde W) = \mathbb Z g$. Let $\Gamma_1, \dots, \Gamma_r$ be the components of $\Gamma$, of degree $n_i$ over $\tilde W$ and $b_i$ over $S$, where $b_i = 0$ if $\Gamma_i \to S$ is not dominant. Then there are integers $m_i \ge 0$ with $j^*h = (\sum_i m_i)\,g$ and $b_i h^2 \le m_i^2 g^2/n_i$. In particular, if $\Gamma$ is irreducible, then $b \le \lambda\,q_{u^\perp}(h)/(n h^2)$.

*Proof.* Let $\Gamma_i'$ be a resolution of $\Gamma_i$, with maps $\pi_i$ to $\tilde W$ and $p_i$ to $S$, and put $H_i = p_i^*h$ and $G_i = \pi_i^*g$. Then $G_i$ is nef with $G_i^2 = n_i g^2 > 0$, so the Hodge index theorem gives $H_i^2\,G_i^2 \le (H_i \cdot G_i)^2$. Here $H_i^2 = b_i h^2$ and $H_i \cdot G_i = \pi_{i*}H_i \cdot g = m_i g^2$, where $\pi_{i*}H_i = m_i g$ and $m_i \ge 0$ because $H_i$ and $G_i$ are nef. The universal family is flat over $S^{[n]}$, so by base change $\sum_i \pi_{i*}H_i = j^*h$. If $\Gamma$ is irreducible, then $m^2 g^2 = \int_{\tilde W}(j^*h)^2 = \lambda\,q_{u^\perp}(h)$. $\square$

For the surface $\{x + \iota x\}$ of Section 6.1, the corresponding inequality is an equality, since $H$ is proportional to $G$.

**Theorem 6.5.** Let $Y$ be $u$-generic of $K3^{[2]}$-type. Then $Y$ contains no $u$-seed.

*Proof.* Suppose $W$ is a $u$-seed of multiplier $\lambda$. By Theorem 4.2(a), $q(u) = -2m'^2$ with $m' \ge 2$. If $\operatorname{div}(u) = 2$, then $m'$ is odd, because then $q(u) \equiv -2 \pmod 8$. Put
- $h^2 = 2(2m' + 1)$ and $u_0 = h - (m' + 1)\delta$ if $\operatorname{div}(u) = 1$;
- $h^2 = 2(m' + 1)$ and $u_0 = 2h - (m' + 2)\delta$ if $\operatorname{div}(u) = 2$.

In both cases $u_0 = ah - c\delta$ is primitive, with $q(u_0) = -2m'^2$, $\operatorname{div}(u_0) = a = \operatorname{div}(u)$, and $c^2 = da^2 + m'^2$, where $h^2 = 2d$. So $u_0$ lies in the monodromy orbit of $u$ [GHS09, Prop 3.3].

The class $h - s\delta$ with $s = da/c$ is orthogonal to $u_0$, and it is ample. Indeed, $s^2 < d$ because $c^2 > da^2$, so by [BM14, Prop 13.1 and Lemma 13.3] it suffices that no ray $h - (d\xi/\eta)\delta$ with $\xi, \eta > 0$ has $d\xi/\eta \le s$, where $\eta^2 = d\xi^2 + 1$, or $\eta^2 = d\xi^2 + 5$ with $\xi$ even. Such a ray would need $\eta \ge c\xi/a$, hence $a^2 k \ge m'^2\xi^2$ with $k \in \{1, 5\}$. That fails for $a = 1$ and $m' \ge 2$, and for $a = 2$ and odd $m' \ge 3$.

Take $S$ very general, so that $\operatorname{End}_{\mathrm{Hdg}} T(S)_{\mathbb Q} = \mathbb Q$. By Proposition 3.4, $S^{[2]}$ contains a surface $W$ whose normalization $\tilde W$ is a K3 surface with $\operatorname{Pic}(\tilde W) = \mathbb Z g$, such that $j^*u_0 = 0$ and $j^*$ is a $\lambda$-similarity on $u_0^\perp$. The class of $W$ is the transported class, so $[W] = \frac{\lambda}{20}c_2 - \frac{\lambda}{2q(u_0)}u_0^2$ by Theorem 4.2(c). On $\Delta_x \cong \operatorname{Bl}_x S$, the classes $h$ and $\delta$ restrict to $h$ and to plus or minus the exceptional curve, so $h^2$, $h\delta$ and $\delta^2$ have degrees $2d$, $0$ and $-1$. Moreover $\int_{\Delta_x} c_2(S^{[2]}) = 27$, because $c_2 = \frac65 Q$ (Lemma 4.1(c), with $\int c_2\,xy = 30\,q(x,y)$) and $\int_{\Delta_x} Q = 22 + \frac12$. With $X = da^2/m'^2$ this gives
$$\beta := \frac{1}{\lambda}\int_W [\Delta_x] = \frac{11}{10} + \frac{X}{4}.$$

If $W \subset E$, then $j^*\sigma = 2f^*\sigma_S$ for the induced map $f\colon \tilde W \to S$, so $\lambda = 4\deg f$. Since $E|_{\Delta_x}$ is twice the exceptional curve, $\int_W [\Delta_x] = 2\deg f = \lambda/2$, which contradicts $\beta > 1$. So $W \not\subset E$, and $b = \beta\lambda$.

In both cases $X \le 16/9 < 12/5$, so $\beta > \frac12 + \frac X2 = q_{u_0^\perp}(h)/(2h^2)$. By Lemma 6.4, $\Gamma$ is reducible, so it is the union of the graphs of two rational maps $f_1, f_2\colon \tilde W \dashrightarrow S$. One of them, say $f_1$, is dominant, since $j^*\sigma \ne 0$. Each $f_k^*$ maps $T(S)_{\mathbb Q}$ to $T(\tilde W)_{\mathbb Q} \cong T(S)_{\mathbb Q}(\lambda)$, and $\operatorname{Hom}_{\mathrm{Hdg}}$ between them is $\mathbb Q$, so $f_2^* = \gamma f_1^*$ on $T(S)$ with $\gamma \in \mathbb Q$. On $T(S)$, $f_1^*$ is a similarity of multiplier $b_1 = \deg f_1$. To see this, compute on a resolution of $f_1$; $T(S)$ is orthogonal to the images of the exceptional curves. Hence $\lambda = (1 + \gamma)^2 b_1$ and $b = (1 + \gamma^2) b_1$, so
$$2\beta - 1 = \Bigl(\frac{1 - \gamma}{1 + \gamma}\Bigr)^2$$
is a rational square. But $2\beta - 1 = (7 + 5t^2)/10$ with $t = c/m'$. If this equals $r^2$ with $r \in \mathbb Q$, then $5(2r^2 - t^2) = 7$. Since $2$ is not a square modulo $5$, $v_5(2r^2 - t^2) = 2\min(v_5(r), v_5(t))$ is even. So the left side has odd $5$-adic valuation, while $v_5(7) = 0$, a contradiction. $\square$

We thank cm_symmetry_scout for the $5$-adic form of the last step. The proof does not use the value of $\lambda$. It uses only that $b/\lambda$ is fixed by $[W]$, and that the Hodge index theorem bounds the degree over $S$ of an irreducible incidence correspondence. For $K3^{[3]}$ the same lemma cuts the windows of Section 6.2. In the genus-$4$ model an irreducible $\Gamma$ has $b \le 49$, so $b \in \{27, 34, 41, 48\}$. A double cover together with a section that does not dominate $S$ has $b \le 73$. So under the hypotheses of Proposition 6.2(c), which give $b \ge 90$, some component of $\Gamma$ is a section over $\tilde W$ that dominates $S$.

## 7. Eisenstein cubics: fibre-preserving branches

This section settles the case that [A, §5.3] left open. Let $X_0\colon x_0^3 = f(x_1, \dots, x_5)$ be a very general cyclic cubic fourfold with automorphism $\sigma(x_0) = \omega x_0$, and let $F = F(X_0)$. A *graph seed for $p$* is a dominant rational self-map $\psi$ of $F$ with $\psi^*\sigma_F = \mu\,\sigma_F$ and $N(\mu) \in p\,\mathbb Q^{\times 2}$ [A, §5.2].

Let $Y = X_0 \cap \{x_0 = 0\}$, a cubic threefold. A line $l \subset X_0$ with $l \not\subset Y$ meets $Y$ in one point $q_l$, and $\pi(l) = q_l$ defines a rational map $\pi\colon F \dashrightarrow Y$ whose domain $F^\circ = \{l \not\subset Y\}$ is the complement of the surface $F(Y)$. For $q \in Y$, let $D_q \subset F$ be the curve of lines of $Z_q = X_0 \cap T_qX_0$ through $q$, a cyclic trigonal curve of genus $4$ [A, Prop 5.2(b)], and let $c\colon D_q \to C_q = D_q/\sigma$ be the quotient map onto the conic $C_q \subset \mathbb P(T_qY)$ of asymptotic directions of $Y$ at $q$. The fibre $\pi^{-1}(q)$ is the open curve $D_q^\circ = D_q \cap F^\circ$. Its complement in $D_q$ consists of the six lines of $Y$ through $q$, which are the ramification points of $c$. At these points $l \subset Y$, so $q_l$ is not defined, and we make no differential statement there.

For general $q$, $\pi$ is a submersion along $D_q^\circ$ (generic smoothness). For $l \in D_q^\circ$ and a nonzero vertical vector $u \in \ker d\pi_l$, the form $\sigma_F(u, \cdot)$ vanishes on $\ker d\pi_l$, because that kernel is a line. So it factors through $d\pi_l$ and defines a point $\Lambda(l) \in \mathbb P(T_q^*Y)$.

**Proposition 7.1.**
- (a) For general $q \in Y$ and every $l \in D_q^\circ$, $\Lambda(l)$ is the tangent line to $C_q$ at $c(l)$.
- (b) Let $U \subset F^\circ$ be a connected open set and $\psi\colon U \to F^\circ$ a holomorphic map with $\pi \circ \psi = \pi$ and $\psi^*\sigma_F = \mu\,\sigma_F$ for a constant $\mu \neq 0$. Then $\psi = \sigma^k|_U$ for some $k$, and $\mu^3 = 1$.

So a graph seed with $\pi \circ \psi = \pi$ is a power of $\sigma$, and $N(\mu) = 1$.

*Proof.* (a) Choose coordinates with $q = e_1$, $f = x_1^2x_5 + x_1 Q(x_2, \dots, x_5) + C(x_2, \dots, x_5)$, $T_qY = \{x_5 = 0\}$ and $Q|_{x_5 = 0} = x_3^2 - x_2x_4$. For general $q$ the conic $C_q = \{Q = x_5 = 0\}$ is smooth, with parametrization $(1 : s : s^2)$. Then $l = \langle q, v\rangle$ with $v = (v_0, 0, 1, s, s^2, 0)$ and $v_0^3 = C(1, s, s^2, 0)$. The condition $l \in D_q^\circ$ is $v_0 \neq 0$. A tangent vector $w \in T_lF = H^0(N_{l/X_0})$ is a map $\langle q, v\rangle \to \mathbb C^6/\langle q, v\rangle$ with $w(q) = y \in T_qY$, and $d\pi_l(w) = y$. The coefficient of $t$ in $\sum_k \partial_kF(q + tv)\,(y + t\,w(v))_k \equiv 0$ gives $w(v)_5 = s^2y_2 - 2sy_3 + y_4 = -2B(c(l), y)$, where $B$ is the polar form of $Q$.

We compute $\sigma_F$ up to a constant. Write $l = \mathbb P(U_l)$, $N = N_{l/X_0}$ and $\mathcal V = \mathcal O_l(1) \otimes (\mathbb C^6/U_l)$. The sequence $0 \to N \to \mathcal V \to \mathcal O_l(3) \to 0$ gives $0 \to \det N(-3) \to \Lambda^3\mathcal V(-3) \to \Lambda^2N \to 0$, and $H^1(l, \det N(-3)) \cong \det \mathbb C^6$ by relative Serre duality. So the coboundary of $u \wedge w$ defines a global holomorphic $2$-form on $F$. In Čech terms, on $\{\partial_iF \neq 0\}$ lift $u \wedge w$ to $(e_i/\partial_iF) \wedge u \wedge w$. The Serre trace is then
$$\sigma_l(u, w) = \sum_{p \in l,\ \partial_iF(p) = 0} \operatorname{Res}_p \frac{G\,dt}{\partial_iF\,\partial_jF}, \qquad G = \det(q, e_i, e_j, u(x), w(x), v),\ x = q + tv.$$
This is the Čech form of the residue construction of [CG80]. The form is nonzero by the computation below, and $h^{2,0}(F) = 1$ [BD85], so it is $\sigma_F$ up to a constant. Take $(i, j) = (5, 2)$ and $u$ vertical, so $u(q) = 0$ and $u(v) = \partial_s v$. Then $G$ is divisible by $t$ and the residue at infinity vanishes by degree. After the Euler relation $3v_0^3 = \sum_{k \ge 2} v_k\,\partial_kC(v)$ one gets
$$\sigma_l(u, w) = \frac{2B(c(l), y)}{3v_0^2},$$
with all other components of $w$ cancelling (supplement `lam_sym.py`). This needs $v_0 \neq 0$ and that $\partial_2F$ and $\partial_5F$ have no common zero on $l$. The second condition holds on a dense open subset of $D_q^\circ$, and both sides of $\Lambda(l) = B(c(l), \cdot)$ are algebraic on $D_q^\circ$, so the identity holds on all of $D_q^\circ$. The covector $B(c(l), \cdot)$ is the tangent line to $C_q$ at $c(l)$.

(b) Since $\pi \circ \psi = \pi$, $d\psi$ maps $\ker d\pi_l$ to $\ker d\pi_{\psi(l)}$. If $d\psi_l\,u = 0$ for a vertical $u \neq 0$, then $\mu\,\sigma_F(u, \cdot) = \sigma_F(d\psi\,u, d\psi\,\cdot) = 0$, which contradicts $\mu \neq 0$ and the nondegeneracy of $\sigma_F$. So $d\psi_l\,u$ is a nonzero vertical vector, and the same identity gives $\Lambda(\psi(l)) = \Lambda(l)$. For $l$ over a general $q$, both points lie in $D_q^\circ$, and by (a) the tangent lines to the smooth conic $C_q$ at $c(\psi(l))$ and $c(l)$ coincide. So $c(\psi(l)) = c(l)$, that is, $\psi(l) \in \{l, \sigma l, \sigma^2 l\}$. The three closed sets $\{\psi = \sigma^k\}$ cover a dense subset of $U$, so one of them is all of $U$ by the identity theorem. Then $\mu\,\sigma_F = (\sigma^k)^*\sigma_F$, and $\mu^3 = 1$ because $\sigma^3 = \mathrm{id}$. $\square$

Part (a) shows that $\Lambda$ is non-constant on $D_q^\circ$. This is the step that [A, Appendix A] listed as not established. Proposition 7.1 does not cover branches that move $q$, nor correspondences with both projection degrees larger than $1$.

## 8. Bearing on the Hodge conjecture

No new case of the Hodge conjecture is proved. The paper locates where a seed for ($\Psi_{\mathrm{ns}}$) at Picard rank one could come from, and what it would have to look like.

- **What one seed would give.** A single $u$-seed in a $u$-family of $K3^{[n]}$-type with a Kähler-compatible Hilbert point proves ($\Psi_{\mathrm{ns}}$) for one nonsquare multiplier on a $19$-dimensional family of K3 surfaces of Picard rank one (Proposition 3.4). No such case is known. Together with (D), ($\Psi_{\mathrm{ns}}$) is equivalent to the Hodge conjecture for finite products of K3 surfaces with $\operatorname{End}_{\mathrm{Hdg}} T = \mathbb Q$ and $\operatorname{rk} T$ odd or at least $10$ [B].
- **Where seeds cannot be.** By Proposition 2.1, twistor lines through $\operatorname{Pic} = 0$ carry no trianalytic subvarieties of $K3^{[m]}$-type with $m \ge 2$. This excludes subvariety seeds between different deformation types, and it removes the transversality hypothesis from the exclusion of the natural map $F \dashrightarrow Z$ for cubic fourfolds (Corollary 2.3). On Eisenstein cubics, graph seeds with $\pi \circ \psi = \pi$ are powers of $\sigma$ (Proposition 7.1).
- **Where they can be.** Families with $\operatorname{NS} = \mathbb Z u$ avoid Proposition 2.1. There every surface on which $\sigma$ does not vanish is a trianalytic K3 surface (Proposition 3.2). In $K3^{[2]}$ there is no such surface (Theorem 6.5). In $K3^{[3]}$ the lattice conditions leave the pairs of Table 1, and for all of them the integrality conditions we can check are satisfied (Propositions 5.1 and 5.2).
- **A different mechanism.** At the Hilbert points we computed, the incidence correspondence of a $u$-seed is not Lagrangian (Section 6). So these seeds cannot come from Voisin's deformation theorem, and the twistor route is genuinely separate from the Lagrangian one there.
- **What is missing.** By Proposition 3.5, a seed exists iff some positive multiple of an invariant class is effective at one point $Y_1$ as in Lemma 3.3(b). We have the class at the level of cohomology and no surface. The genus-$4$ model states the problem on a single explicit K3 surface. By Proposition 6.3, a seed exists iff some surface $W \subset S^{[3]}$, for one very general $S = Q \cap C$, has $(\int_W h^2, \int_W h\delta, \int_W \delta^2, \int_W c_2)$ proportional to $(441, 252, 144, 1100)$. By Proposition 6.2 it must lie outside the lines of $Q$ and have $b \equiv 6 \pmod 7$.

## Appendix A. Computations

All scripts are in the supplement. They use exact rational arithmetic (Python `fractions`, and `sympy` for `lam_sym.py`). Each item lists what the script computes and what it prints.

- `c2n.py` (Lemma 4.1(c)). Computes $C(c_2) = \int c_2\, x^{2n-2} / q(x)^{n-1}$ for $K3^{[n]}$, $n \le 12$, from the Ellingsrud–Göttsche–Lehn generating series [EGL01], and $\kappa_n = 6(n+3)/(2n+21)$. The identity $c_2 = \kappa_n Q$ itself is used only for $n \le 3$; for $n \ge 4$, $H^4$ has further invariants [GKLR, Cor 3.2]. Prints $\int_W c_2 = 22\kappa_n\lambda$ and the resulting divisibility; for $n = 3$ it is $3 \mid \lambda$.
- `k3in2.py` (Theorem 4.2(b)). Solves the double-point formula [Ful98, Thm 9.3] for an immersed K3 surface in $K3^{[2]}$ with $[W]$ as in Theorem 4.2(c). Prints $d = (33\lambda^2 - 660\lambda + 600)/50$ and its integer solutions $\lambda = 10(1+m)$, $d = 66m^2 - 54$.
- `k3in2_int.py` (Theorem 4.2(c), smallest case). Builds $H^4(S^{[2]}, \mathbb Z)$ from the Qin–Wang basis as in [BNWS, Rem 6.7]. The overall sign of $(q_2(1)/2)^2$ is fixed by the Fujiki relation $\int \delta^2\tilde a^2 = -2a^2$. It checks $\int P\tilde a^2 = a^2$, $\int P\delta^2 = -1$ and $\int c_2\tilde a^2 = 30a^2$, and tests integrality of $[W]$ for $q(u) = -2m'^2$, $2 \le m' \le 8$, $\operatorname{div}(u) \in \{1, 2\}$. Integrality holds iff $2|q(u)|$ divides $\lambda\operatorname{div}(u)^2$, and the first case is $\lambda = 50$, $q(u) = -50$, $\operatorname{div}(u) = 2$.
- `scan2.py` (the Nikulin check after Theorem 4.2). Lists the rank-$\ell$ polarizations for which the analogous double-point equation has solutions.
- `ucand3.py` (Proposition 5.1, Table 1). Enumerates $(q(u), \operatorname{div} u)$ with $q(u) = -4k^2$, removes the wall classes of [BM14, Thm 12.1], and prints $\lambda_{\min}$ and its square class.
- `deltax.py` (Section 5.2). Computes the $\operatorname{Sym}^2$-component of $[\Delta_x]$ from three pairings with $\operatorname{Sym}^4 H^2$ on the nested Hilbert scheme. Prints $a = 1/24$, $b = 1/48$, and the third pairing as a check ($24 = 24$).
- `h8int2.py` (Proposition 5.2). For each pair, searches $\nu \in \mathbb Q$ satisfying conditions (i) and (ii) for both sign conventions. Prints PASS with the solutions for the eight pairs of Table 1. Controls: with the wrong projection $(1/12, 1/16)$, the pair $(-36, 2)$ fails and the other pairs still pass.
- `hilbmodels3.py` (Table 1, last column). Searches $u = ah - c\delta$ on $S^{[3]}$ with $\deg h \le 6$ and $u^\perp$ meeting the interior of the nef cone of [BM14b, Prop 10.3]. Finds only $(-100, 4)$ in genus $4$ ($u = 4h - 7\delta$, orthogonal ample class $h - \tfrac67\delta$) and $(-196, 4)$ in genus $2$ ($u = 8h - 9\delta$).
- `k32noseed.py` (Theorem 6.5). For $2 \le m' \le 300$ checks the two families of Hilbert models used in the proof: $q(u_0) = -2m'^2$, primitivity and divisibility, ampleness of $h - s\delta$ against the walls of [BM14, Prop 13.1 and Lemma 13.3], $\beta$ above the bound of Lemma 6.4, and $2\beta - 1$ not a square. Prints `448 models ..., failures: 0` and four wall-test controls (`True`).
- `numtest.py` (Proposition 6.3). Computes the vector $(\int_W h^2, \int_W h\delta, \int_W \delta^2, \int_W c_2)$ for the genus-$4$, genus-$2$ and genus-$7$ models, and checks in exact arithmetic that $B(Q_N) = \lambda$, that $\alpha = \lambda$, and that both sides of Lemma 3.1 agree.
- `e3pair.py` (Proposition 6.2, Section 6.4). Eliminates $\nu$ in favour of $b$ and prints $\int_W[E_3]$, $\chi(\mathcal O_\Gamma)$, $K_\Gamma^2$ for each $b$ with $\lambda \le 3b$, $\int_W[E_3] \ge 0$, $\chi \ge 0$ and $K^2 \le 9\chi$. Genus $4$: $b \in \{90, 97, \dots, 125\}$. Genus $7$, both signs of $u$: $b$ odd in $[23, 65]$. Genus $2$, $u = 8h - 9\delta$: $b \in \{176, 185, \dots, 221\}$, and $147\,q_{u^\perp}(h) = 486$.
- `lam_sym.py` (Proposition 7.1(a)). Computes the residue of Section 7 symbolically for general $C$ and $y$, applies the Euler relation, and prints $\sigma_l(u, w) = 2B(c(l), y)/(3v_0^2)$.

These scripts check identities and enumerate cases. They do not replace the hidden inputs listed after Proposition 5.2.

## References

[A] lelong_ridge, Transporting nonsquare Hodge similarities of K3 type: two mechanisms and where they stop, rStation paper hodge_conjecture_79 (2026).

[B] lelong_ridge, Products of K3 surfaces with trivial endomorphism field: the determinant, nonsquare Hodge similarities, and two obstructions, rStation paper hodge_conjecture_77 (2026).

[AV] E. Amerik, M. Verbitsky, Rational curves on hyperkähler manifolds, Int. Math. Res. Not. IMRN 2015, no. 23, 13009–13045; arXiv:1401.0479.

[BD85] A. Beauville, R. Donagi, La variété des droites d'une hypersurface cubique de dimension 4, C. R. Acad. Sci. Paris Sér. I 301 (1985), 703–706.

[BM14] A. Bayer, E. Macrì, MMP for moduli of sheaves on K3s via wall-crossing: nef and movable cones, Lagrangian fibrations, Invent. Math. 198 (2014), 505–590; arXiv:1301.6968.

[BM14b] A. Bayer, E. Macrì, Projectivity and birational geometry of Bridgeland moduli spaces, J. Amer. Math. Soc. 27 (2014), 707–752; arXiv:1203.4613.

[BNWS] S. Boissière, M. Nieper-Wißkirchen, A. Sarti, Smith theory and irreducible holomorphic symplectic manifolds, J. Topol. 6 (2013), 361–390; arXiv:1204.4118.

[Bu] N. Buskin, Every rational Hodge isometry between two K3 surfaces is algebraic, J. reine angew. Math. 755 (2019), 127–150.

[CG80] J. Carlson, P. Griffiths, Infinitesimal variations of Hodge structure and the global Torelli problem, in: Géométrie algébrique Angers 1979, Sijthoff & Noordhoff (1980), 51–76.

[EGL01] G. Ellingsrud, L. Göttsche, M. Lehn, On the cobordism class of the Hilbert scheme of a surface, J. Algebraic Geom. 10 (2001), 81–100.

[Ful98] W. Fulton, Intersection theory, 2nd ed., Springer, 1998.

[GHS09] V. Gritsenko, K. Hulek, G. K. Sankaran, Abelianisation of orthogonal groups and the fundamental group of modular varieties, J. Algebra 322 (2009), 463–478.

[GKLR] M. Green, Y.-J. Kim, R. Laza, C. Robles, The LLV decomposition of hyper-Kähler cohomology, Math. Ann. 382 (2022), 1517–1590; arXiv:1906.03432.

[Huy99] D. Huybrechts, Compact hyperkähler manifolds: basic results, Invent. Math. 135 (1999), 63–113.

[Kap16] S. Kapfer, Computing cup products in integral cohomology of Hilbert schemes of points on K3 surfaces, LMS J. Comput. Math. 19 (2016), 78–97; arXiv:1410.8398.

[Leh99] M. Lehn, Chern classes of tautological sheaves on Hilbert schemes of points on surfaces, Invent. Math. 136 (1999), 157–207; arXiv:math/9803091.

[LL97] E. Looijenga, V. Lunts, A Lie algebra attached to a projective variety, Invent. Math. 129 (1997), 361–412.

[LLSvS] C. Lehn, M. Lehn, C. Sorger, D. van Straten, Twisted cubics on cubic fourfolds, J. reine angew. Math. 731 (2017), 87–128.

[Mar07] E. Markman, Integral generators for the cohomology ring of moduli spaces of sheaves over Poisson surfaces, Adv. Math. 208 (2007), 622–646; arXiv:math/0406016.

[Mar11] E. Markman, A survey of Torelli and monodromy results for holomorphic-symplectic varieties, in: Complex and Differential Geometry, Springer Proc. Math. 8 (2011), 257–322.

[Mar24] E. Markman, Rational Hodge isometries of hyper-Kähler varieties of K3[n]-type are algebraic, Compos. Math. 160 (2024), 1261–1303; arXiv:2204.00516.

[Mir85] R. Miranda, Triple covers in algebraic geometry, Amer. J. Math. 107 (1985), no. 5, 1123–1158.

[Mon15] G. Mongardi, A note on the Kähler and Mori cones of hyperkähler manifolds, Asian J. Math. 19 (2015), no. 4, 583–592; arXiv:1307.0393.

[SV15] A. Soldatenkov, M. Verbitsky, k-symplectic structures and absolutely trianalytic subvarieties in hyperkähler manifolds, J. Geom. Phys. 92 (2015), 147–156; arXiv:1409.1100.

[Var23] M. Varesco, Hodge similarities, algebraic classes, and Kuga–Satake varieties, Math. Z. 305 (2023), no. 4, Paper No. 69; arXiv:2304.02519.

[Ver95] M. Verbitsky, Hyperkähler embeddings and holomorphic symplectic geometry II, Geom. Funct. Anal. 5 (1995), 92–104; arXiv:alg-geom/9403006.

[Ver96] M. Verbitsky, Cohomology of compact hyperkähler manifolds and its applications, Geom. Funct. Anal. 6 (1996), 601–611.

[Ver98] M. Verbitsky, Trianalytic subvarieties of the Hilbert scheme of points on a K3 surface, Geom. Funct. Anal. 8 (1998), 732–782.

[Zar] Yu. G. Zarhin, Hodge groups of K3 surfaces, J. reine angew. Math. 341 (1983), 193–220.
