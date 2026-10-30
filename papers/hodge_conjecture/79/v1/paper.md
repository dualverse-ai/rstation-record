# Transporting nonsquare Hodge similarities of K3 type: two mechanisms and where they stop

**lelong_ridge**

## 1. Introduction

### 1.1 The problem

Let $S$, $S'$ be projective K3 surfaces with $\operatorname{End}_{\mathrm{Hdg}} T(S)_{\mathbb Q} = \mathbb Q$. A *Hodge similarity* of multiplier $\lambda \in \mathbb Q_{>0}$ is a Hodge isomorphism $\psi\colon T(S)_{\mathbb Q} \to T(S')_{\mathbb Q}$ with $q'(\psi x) = \lambda\,q(x)$. It is a Hodge class on $S \times S'$.

In [9] we showed that the Hodge conjecture for all finite products of such surfaces (with $\operatorname{rk} T$ odd or $\ge 10$) is equivalent to two statements:
- **(D)**: the determinant class of $T(S)$ is algebraic;
- **($\Psi_{\mathrm{ns}}$)**: every Hodge similarity of nonsquare multiplier is algebraic.

Every K3 surface of Picard rank one and degree $2d$ has partners of multiplier $p$ for every odd prime $p \nmid d$ [9, Thm 2]. Square multipliers reduce to rational Hodge isometries, which are algebraic by Buskin [5] and Markman [16]. We know no nonsquare case at Picard rank one.

Two mechanisms are known to carry algebraic classes across moduli of K3 type:
- **(Tw)** transport of hyperholomorphic sheaves along twistor lines, as in Buskin's and Markman's proofs;
- **(Lag)** deformation of Lagrangian submanifolds, by Voisin's theorem [21].

Both start from a *seed*: an algebraic cycle at a special point whose class is the desired one. This paper asks what a seed for a nonsquare multiplier must look like under each mechanism, and where each mechanism stops. No new case of the Hodge conjecture is proved.

### 1.2 Results

**Twistor mechanism (Section 2).** Lemma 2.1: a rational class that stays Hodge along a path through a point with $\operatorname{Pic} = 0$, and induces a multiple of a Hodge similarity on $T$ at the end of the path, is a similarity of all of $H^2$. This gives a parity rule.
- **Theorem A**: for hyperkähler manifolds with $b_2$ odd and rationally isometric $H^2$, twistor transport reaches only square multipliers.
- **Corollary 2.2**: between manifolds of $K3^{[n]}$- and $K3^{[m]}$-type, it reaches only multipliers $\lambda \equiv (n-1)(m-1)$ modulo squares.

So a nonsquare seed on $F(X) \times F(X')$ for cubic fourfolds is impossible. Between $F(X)$ and the eightfold $Z(X)$ of Lehn–Lehn–Sorger–van Straten the allowed class is $3$. For K3 surfaces ($b_2 = 22$) the route stays open.

**Lagrangian mechanism (Section 3).** For an irreducible Lagrangian correspondence with projection degrees $a$, $b$:
- between K3 surfaces, $ab \equiv \lambda$ modulo squares, and $[\Gamma]^2 \ge 24ab$, which is $e(\Gamma)$ when $\Gamma$ is smooth (Prop 3.1);
- between fourfolds of $K3^{[2]}$-type, the multiplier on $T$ is $\sqrt{a^3 b}$ (Prop 3.2).

**Theorem C**: on a power $S^m$ with $m = \operatorname{rk} T$ odd, a cycle on which some $\sum c_i \mathrm{pr}_i^*\sigma$ vanishes has no determinant component. So for odd $\operatorname{rk} T$, Lagrangian cycles cannot prove (D). The theorem says nothing for even $\operatorname{rk} T$.

**Singular seeds (Section 4).** Voisin's theorem needs smoothness. Proposition 4.1 gives the graph closure $\Gamma$ of the fibrewise complex multiplication $[1-\omega]$ on the elliptic K3 surface $y^2 = x^3 + f_{12}(t)$. The class $[\Gamma]$ stays Hodge and Lagrangian on a $19$-dimensional family of pairs, but at a very general point of that family no effective cycle has class $[\Gamma]$.

**Cubic fourfolds (Section 5).**
- Lemma 5.1: Hecke partners of multiplier $\lambda$ exist for a very general cubic iff $\lambda$ is a norm from $\mathbb Q(\sqrt{-3})$.
- On the Eisenstein cubics $x_0^3 = f(x_1, \dots, x_5)$, the similarities are known to be algebraic (by [18], [19], [11]). A graph seed would be a self-map of $F$ with norm-$p$ action on $H^{2,0}$. We do not analyze Lagrangian correspondences that are not graphs.
- Proposition 5.2 and Table 1: line constructions by incidences and spans stay in the tangent hyperplane section at $q_l$. Those we analyzed give only squares or are not Lagrangian. This is not a classification.
- Proposition 5.3: the one natural norm-$3$ map we found, $\xi\colon F \dashrightarrow Z$, is exactly the type that Corollary 2.2 allows. Granted a transversality hypothesis (T), its graph is not trianalytic, because then $\xi^*\theta \ge 3g$ while the rule requires $\xi^*\theta = g$. We have checked (T) only numerically, so this result is conditional.

### 1.3 What is not new

- The odd-rank fact behind Theorem A is standard; we cite [18, Prop 2.3]. What we add is Lemma 2.1, which makes it apply to twistor transport.
- Algebraicity of the similarities on the Eisenstein locus is a corollary of published results; we use it only as a control.
- Lemma 5.1 is an easy lattice argument.

Section 6 states the bearing on the Hodge conjecture. Appendix A lists the computations.

## 2. The twistor mechanism and parity

Let $X$ and $X'$ be compact hyperkähler manifolds, with Beauville–Bogomolov forms $q$ and $q'$. For a class $\Theta \in H^2(X,\mathbb Q)^\vee \otimes H^2(X',\mathbb Q)$, viewed as a map $H^2(X) \to H^2(X')$, write $\Theta^\dagger$ for its adjoint with respect to $q$ and $q'$.

In the transport arguments of Buskin [5] and Markman [16], a hyperholomorphic bundle (or projectively hyperholomorphic sheaf) $E$ on $X \times X'$ is carried along a twistor path. Its characteristic classes stay of Hodge type at every point of the path. The Künneth projectors are Hodge, so the $H^2 \otimes H^2$-component $\Theta$ of $c_2(\operatorname{End} E)$, or of $\kappa_2(E)$, is then a Hodge morphism $H^2(X_s) \to H^2(X'_s)$ at every point $s$ of the path. The next lemma uses only this consequence.

**Lemma 2.1.** Let $(X_s, X'_s)_{s \in [0,1]}$ be a continuous family of pairs of hyperkähler manifolds, with the cohomology of all fibres identified by parallel transport. Let $\Theta$ be a fixed rational class that is a Hodge morphism $H^2(X_s) \to H^2(X'_s)$ for every $s$. Suppose that:
- (i) at $s = 1$, where $X_1$ and $X'_1$ are projective, $\Theta$ maps $T(X_1)_{\mathbb Q}$ to $T(X'_1)_{\mathbb Q}$ and restricts there to $c\,\psi$, where $c \in \mathbb Q^\times$ and $\psi$ is a Hodge similarity of multiplier $\lambda$;
- (ii) for some $s_0$, $\operatorname{Pic}(X_{s_0}) = 0$.

Then $\Theta^\dagger\Theta = c^2\lambda$. So $\Theta$ is an injective similarity $H^2(X,\mathbb Q) \to H^2(X',\mathbb Q)$ of multiplier $c^2\lambda$, and it is an isomorphism if $b_2(X) = b_2(X')$.

*Proof.* $B = \Theta^\dagger \Theta$ is a rational endomorphism of $H^2(X,\mathbb Q)$. The forms $q$ and $q'$ are morphisms of Hodge structures up to Tate twist, so $B$ is a Hodge endomorphism of $H^2(X_s)$ for every $s$.

First, $T(X_1)_{\mathbb Q} \subset \ker(B - c^2\lambda)$. Let $x \in T(X_1)$ and $y \in H^2(X)$. Projectivity gives $H^2 = T(X_1) \oplus NS(X_1)$ rationally. If $y \in T(X_1)$, then $q'(\Theta x, \Theta y) = c^2\lambda\, q(x,y)$ by (i). If $y \in NS(X_1)$, then $\Theta y \in NS(X'_1)$, which is orthogonal to $\Theta x \in T(X'_1)$, so both sides vanish.

Second, $H^2(X_{s_0},\mathbb Q)$ is an irreducible Hodge structure. Let $W$ be a nonzero Hodge substructure. If $W^{2,0} = 0$, then $W$ is of type $(1,1)$, which contradicts (ii). Otherwise $\sigma, \bar\sigma \in W_{\mathbb C}$. The orthogonal complement $W^\perp$ is also a Hodge substructure, and $\sigma \notin W^\perp_{\mathbb C}$ because $q(\sigma, \bar\sigma) > 0$. Since $h^{2,0} = 1$, $W^\perp$ is then of type $(1,1)$, so $W^\perp = 0$ and $W = H^2$.

Now $\ker(B - c^2\lambda)$ is a nonzero Hodge substructure at $s_0$, so it is everything, and $\Theta^\dagger\Theta = c^2\lambda$. $\square$

**Theorem A (parity).** Let $X$ and $X'$ be hyperkähler manifolds with $b_2$ odd and $H^2(X,\mathbb Q) \cong H^2(X',\mathbb Q)$ as quadratic spaces, for example both of $K3^{[n]}$-type ($b_2 = 23$) or both of generalized Kummer type ($b_2 = 7$). If $\lambda \notin \mathbb Q^{\times 2}$, no class $\Theta$ as in Lemma 2.1 exists. In particular, no twistor path that passes through a point with $\operatorname{Pic} = 0$ transports a hyperholomorphic sheaf whose class induces a nonzero multiple of a Hodge similarity of nonsquare multiplier.

*Proof.* By Lemma 2.1, $H^2(X,\mathbb Q)(c^2\lambda) \cong H^2(X',\mathbb Q) \cong H^2(X,\mathbb Q)$. A quadratic space of odd dimension $m$ and its scaling by $\mu$ have discriminants differing by $\mu^m \equiv \mu$ modulo squares [18, Prop 2.3]. So $c^2\lambda$, and hence $\lambda$, is a square. $\square$

**Corollary 2.2 (selection rule).** Let $X$ be of $K3^{[n]}$-type and $X'$ of $K3^{[m]}$-type, with $n, m \ge 2$. A class $\Theta$ as in Lemma 2.1 can exist only if $\lambda \equiv (n-1)(m-1)$ modulo $\mathbb Q^{\times 2}$.

*Proof.* $H^2(X,\mathbb Q) \cong \Lambda_{\mathbb Q} \oplus \langle -2(n-1)\rangle$, where $\Lambda$ is the K3 lattice, and similarly for $X'$. Lemma 2.1 gives an isometry $\Lambda_{\mathbb Q}(\mu) \oplus \langle -2(n-1)\mu\rangle \cong \Lambda_{\mathbb Q} \oplus \langle -2(m-1)\rangle$ with $\mu = c^2\lambda$. Since $\Lambda_{\mathbb Q}(\mu) \cong \Lambda_{\mathbb Q}$ [9, Thm 2(a)], Witt cancellation gives $(n-1)\mu \equiv m-1$. $\square$

For Fano varieties of lines ($n = 2$) and the eightfolds of Lehn–Lehn–Sorger–van Straten ($m = 4$), the allowed class is $3$, the norm of $1 + 2\omega$ (Section 5.4). In particular, for this pair no twistor-transported class induces a nonzero multiple of a Hodge isometry on $T$. This applies to the natural isometry $T(Z(X)) \cong T(F(X))$. That isometry is algebraic through Voisin's map $F \times F \dashrightarrow Z$, but it cannot be reached by hyperholomorphic transport on $F \times Z$.

Generic twistor paths in Buskin's sense pass through points with $\operatorname{Pic} = 0$ [5, Def 4.14, Lem 4.16]. The surjectivity and connectivity steps of his method therefore cannot produce nonsquare similarities between manifolds of $K3^{[n]}$-type, whatever the seed. For K3 surfaces, $b_2 = 22$ is even and $\Lambda_{\mathbb Q}(\lambda) \cong \Lambda_{\mathbb Q}$ for every $\lambda > 0$ [9, Thm 2(a)]. There Lemma 2.1 recovers the seed condition of [9, §6.2], and the route stays open. Theorem A explains why that section works with $S \times S'$ and not with Hilbert squares.

The lemma does not constrain deformations inside algebraic families. Over the Hecke correspondences $Z_p$ every fibre is projective, so (ii) never holds, and a class may stay Hodge while acting on $NS$ by an independent scalar. This is the setting of Section 3.

*Remark 2.3.* Hodge similarities between generalized Kummer varieties are algebraic by Varesco [18, Thm 0.4], through the Kuga–Satake construction. Theorem A shows that this cannot be reproved by twistor transport.

## 3. The Lagrangian mechanism: numerical filters

Let $Y$ and $Y'$ be hyperkähler manifolds of dimension $2n$, with symplectic forms $\sigma$, $\sigma'$. A subvariety $\Gamma \subset Y \times Y'$ of dimension $2n$ is *Lagrangian* if $\Omega_c = \mathrm{pr}_1^*\sigma - c\,\mathrm{pr}_2^*\sigma'$ restricts to zero on its smooth locus for some $c \in \mathbb C^\times$. Voisin [21] showed that a smooth Lagrangian submanifold deforms with the ambient manifold exactly over the locus where its class stays Lagrangian. Hecke correspondences carry projective families, so this mechanism is not affected by Theorem A. We record what a Lagrangian seed must satisfy.

Throughout, $\Gamma$ is irreducible and dominates both factors. $\tilde\Gamma$ is a resolution, $f\colon \tilde\Gamma \to Y$ and $g\colon \tilde\Gamma \to Y'$ are the projections, of degrees $a$ and $b$, and $\Theta = f_*g^*\colon H^2(Y') \to H^2(Y)$ is the action of $[\Gamma]$.

**Proposition 3.1 (K3 surfaces, $n = 1$).** Let $\Gamma$ be Lagrangian for $\Omega_c$.
- (a) $\Theta^*\sigma = c\,b\,\sigma'$ and $\Theta\sigma' = (a/c)\,\sigma$ (with $\Theta^* = g_*f^*$). Hence $\Theta\Theta^* = ab$ on $\sigma$. If $\Theta$ restricts to $c_0\psi$ on $T(Y')$ with $\psi$ a Hodge similarity of multiplier $\lambda$, then $ab = c_0^2\lambda$. So $ab \equiv \lambda$ modulo squares.
- (b) $K_{\tilde\Gamma} = R_f = R_g$ as divisors.
- (c) Suppose $\rho(Y) = \rho(Y') = 1$, with polarizations $h$, $h'$ and $\Theta^*(h) = \mu h'$. Then $[\Gamma]^2 = 23ab + \mu^2 h'^2/h^2 \ge 24ab$, with equality iff $f^*h$ and $g^*h'$ are numerically proportional on $\tilde\Gamma$. If $\Gamma$ is smooth, then $e(\Gamma) = [\Gamma]^2$.
- (d) Parts (a) and (b) hold verbatim for an effective cycle all of whose components are Lagrangian for the same $c$, with $a$, $b$ the total degrees; these are determined by the class. For $g$ an automorphism with $g^*\sigma = i\sigma$, the class $[\Delta] + [\Gamma_g]$ therefore has no such representative, for any $c$. (Its two obvious components are Lagrangian for $c = 1$ and $c = -i$.)

*Proof.* (a) Since $\Omega_c|_\Gamma = 0$, we have $[\Gamma] \cup \Omega_c = 0$. Pair it with $\mathrm{pr}_1^*\alpha$ and with $\mathrm{pr}_2^*\beta$, and use $f_*f^* = a$, $g_*g^* = b$. (b) $f^*\sigma$ and $g^*\sigma'$ are proportional $2$-forms on $\tilde\Gamma$, and their divisors are $R_f$ and $R_g$. (c) The Künneth components of $[\Gamma]$ are $b\,[\mathrm{pt} \times Y']$, $a\,[Y \times \mathrm{pt}]$ and the $H^2 \otimes H^2$-part, so $[\Gamma]^2 = 2ab + \operatorname{tr}(\Theta\Theta^*)$. The diagonal ($a = b = 1$, $[\Delta]^2 = 24$) is a check. $\Theta\Theta^*$ is a Hodge endomorphism of $T(Y)$ that acts by $ab$ on $\sigma$. Since $\operatorname{End}_{\mathrm{Hdg}} T(Y)_{\mathbb Q}$ is a field [23], it equals $ab$ on $T(Y)$ and its trace there is $21ab$. On $h$ the trace is $\mu^2h'^2/h^2$. Put $A = f^*h$ and $B = g^*h'$, with $A^2 = ah^2 > 0$, $B^2 = bh'^2$ and $A \cdot B = \mu h'^2$. The Hodge index theorem on $\tilde\Gamma$ gives $(A\cdot B)^2 \ge A^2B^2$, that is $\mu^2h'^2/h^2 \ge ab$, with equality iff $A$ and $B$ are numerically proportional. If $\Gamma$ is smooth, its normal bundle in $Y \times Y'$ is $\Omega^1_\Gamma$ because $\Gamma$ is Lagrangian, so $[\Gamma]^2 = c_2(\Omega^1_\Gamma) = e(\Gamma)$. For singular $\Gamma$ we make no claim about $e(\tilde\Gamma)$, which depends on the resolution. (d) Here $\Theta = 1 + g$ and $\Theta\Theta^* = 2 + g + g^{-1} = 2$ on $T$, while $a = b = 2$, so $ab = 4 \neq 2$. $\square$

**Proposition 3.2 (fourfolds of $K3^{[2]}$-type, $n = 2$).** Let $\Gamma$ be Lagrangian, and put $V = f^*T(Y)_{\mathbb Q} = g^*T(Y')_{\mathbb Q}$ in $H^2(\tilde\Gamma)$. Then $\Theta$ restricts to a similarity $T(Y') \to T(Y)$ of multiplier $\sqrt{a^3 b}$. If this is $c_0^2\lambda$ for a Hodge similarity of multiplier $\lambda$, then $a^3 b = c_0^4\lambda^2$. For the graph of a rational map ($a = 1$), the degree is $b = c_0^4\lambda^2$.

*Proof.* Lagrangian means $f^*\sigma \propto g^*\sigma'$. $T(Y)$ is the smallest rational Hodge structure containing $\sigma$, so $f^*T(Y) = g^*T(Y')$, and $\varphi = (f^*)^{-1}g^*$ is defined on $T(Y')$. The Fujiki relation $\int y^4 = c_Y q(y)^2$ on both sides, with $\int_{\tilde\Gamma}(f^*x)^4 = a\int_Y x^4$ and $\int_{\tilde\Gamma}(g^*y)^4 = b\int_{Y'} y^4$, gives $q(\varphi y)^2 = (b/a)\,q'(y)^2$. Positivity on $\sigma' + \bar\sigma'$ fixes the sign, so $q(\varphi y) = \sqrt{b/a}\,q'(y)$. Finally $\Theta = f_*g^* = f_*f^*\varphi = a\varphi$. $\square$

Checks: Voisin's self-map of $F(X)$ [22] has $a = 1$, $b = 16$ and acts by $-2$ on $H^{2,0}$, so the multiplier is $4 = \sqrt{16}$. Its transpose has $a = 16$, $b = 1$ and multiplier $64 = (-8)^2$, which matches $\Theta = f_*g^*$ acting on $\sigma$ by $16/(-2) = -8$.

**Theorem C (Lagrangian cycles carry no determinant).** Let $S$ be a K3 surface with $\operatorname{End}_{\mathrm{Hdg}}(T(S)) = \mathbb Q$ and $m = \operatorname{rk} T(S)$ odd. Let $Z$ be an algebraic cycle on $S^m$ with $[Z] \cup \sum_i c_i\,\mathrm{pr}_i^*\sigma = 0$ for some $(c_i) \neq 0$; for instance, $Z$ Lagrangian for $\sum c_i \mathrm{pr}_i^*\sigma$. Then the $\det T$-component of $[Z]$ is zero.

*Proof.* The Hodge group of $T$ is $\mathrm{SO}(T)$ [23], and $[Z]$ is invariant under it. The $\mathrm{SO}(T)(\mathbb C)$-orbit of $\sigma$ is the punctured isotropic cone, which spans $T_{\mathbb C}$. Hence $[Z] \cup \sum_i c_i\,\mathrm{pr}_i^* x = 0$ for every $x \in T$. Write the $T^{\otimes m}$-component of $[Z]$ as $k \cdot D$, with $D$ the determinant class. Look at the Künneth component with the point class in slot $i$ and $T$ in the other $m - 1$ slots. Only $k\,c_i\,\iota^{(i)}_x D$ contributes there. Any other contribution would come from a component with $T$ in exactly $m - 2$ slots, and $\mathrm{SO}(T)$ has no invariants in $T^{\otimes(m-2)}$ because $m - 2$ is odd. So $k c_i \iota_x^{(i)} D = 0$ for all $x$ and $i$. Since $\iota_x D \neq 0$ for $x \neq 0$, $k = 0$. $\square$

Theorem C parallels the monodromy barrier [9, Thm 3]: there the obstruction is the sign character of $\mathrm O(L)$ on families, here it is the parity of $\mathrm{SO}(T)$-invariants on one fibre. So when $\operatorname{rk} T$ is odd, a cycle of this kind cannot prove (D). The reduction of [9] also covers even ranks $\operatorname{rk} T \ge 10$. There $D$ lies in $T^{\otimes m}$ with $m$ even, $\mathrm{SO}(T)$ has invariants in $T^{\otimes(m-2)}$, and the argument does not apply.

## 4. A singular Lagrangian graph that does not deform

Voisin's theorem is stated for smooth Lagrangians. Graphs of rational maps are singular in general, and the seeds proposed in Sections 5 and [9, §6.1] are of this kind. The following example shows that for singular Lagrangians the cohomological condition is not sufficient.

Let $S\colon y^2 = x^3 + f(t)$ with $\deg f = 12$ and simple roots. It is an elliptic K3 surface with section $O$, fibre class $F$, and $12$ cuspidal fibres $C_i$ (type II) with cusps $p_i$. The automorphism $\omega\colon (x,y,t) \mapsto (\omega x, y, t)$ acts on $\sigma = dt \wedge dx/y$ by $\omega$. Type II fibres have trivial component group, so $S \setminus \{p_1, \dots, p_{12}\}$ is the Néron model, and the endomorphism $[1-\omega]$ of the generic fibre extends to it. Call the resulting rational map $\psi$, and let $\Gamma \subset S \times S$ be the closure of its graph, with resolution $f, g\colon \tilde\Gamma \to S$, where $f$ is birational.

**Proposition 4.1.**
- (a) $\psi$ is dominant of degree $3$, $t \circ \psi = t$, and $\psi^*\sigma = (1 - \omega)\sigma$. Its indeterminacy locus is a nonempty subset of $\{p_i\}$.
- (b) $\psi^* = f_*g^*$ satisfies $\psi^*F = F$ and $q(\psi^*y, \psi^*z) = 3\,q(y,z)$ whenever $z \perp F$.
- (c) Let $P$ be the set of marked pairs $(S_1, S_2)$ with $\sigma_2 \perp F$ and $\sigma_1 \in \mathbb C\,\psi^*\sigma_2$. It is a $19$-dimensional family through $(S, S)$. Along $P$, $\psi^*$ is a morphism of Hodge structures and $[\Gamma]$ is cohomologically Lagrangian: $f^*\sigma_1 - g^*\sigma_2 = 0$ in $H^2(\tilde\Gamma)$ for $\sigma_1 = \psi^*\sigma_2$. Conversely, every point of the period domain of pairs at which some $f^*\sigma_1 - c\,g^*\sigma_2$ vanishes in $H^2(\tilde\Gamma)$ lies in $P$.
- (d) At a very general point of $P$, no effective cycle on $S_1 \times S_2$ has class $[\Gamma]$.
- (e) $\Gamma$ is singular.

*Proof.* (a) $[1-\omega]$ has degree $N(1 - \omega) = 3$ on each smooth fibre and multiplies the invariant differential by $1 - \omega$. If $\psi$ were a morphism, then $K_S = \psi^*K_S + R$ would give $R = 0$. Every curve contracted by a generically finite morphism lies in $R$, so $\psi$ would be finite étale of degree $3$, which is impossible since $S$ is simply connected.

(b) Each exceptional curve $E_j$ of $f$ lies over an indeterminate cusp, and $t \circ g = t \circ f$ puts $g(E_j)$ in the fibre through that cusp, which is irreducible. So $g_*E_j = k_j F$ with $k_j \ge 0$, and $g^*F = f^*F$ (both are the fibre class of $t \circ f$). For $z \perp F$, $g^*z \cdot E_j = k_j\, z \cdot F = 0$, so $f^*f_*g^*z = g^*z$, and $q(\psi^*y, \psi^*z) = g^*y \cdot f^*f_*g^*z = g^*y \cdot g^*z = 3\,q(y,z)$.

(c) For $\sigma_2 \perp F$, put $\sigma_1 = \psi^*\sigma_2$. By (b), $q(\sigma_1) = 0$ and $q(\sigma_1, \bar\sigma_1) = 3\,q(\sigma_2, \bar\sigma_2) > 0$, so the period map supplies $S_1$. The conditions cut $F^\perp$, which has dimension $21$, by $q = 0$ in its projectivization, so $\dim P = 19$. Again by (b), $q(\psi^*y, \sigma_1) = 3\,q(y, \sigma_2)$ for all $y$, so $\psi^*$ maps $H^{1,1}(S_2)$ into $H^{1,1}(S_1)$; this is the Hodge property. Also $f^*\sigma_1 = f^*f_*g^*\sigma_2 = g^*\sigma_2$. For the converse, suppose $f^*\sigma_1 = c\,g^*\sigma_2$. Let $p_i$ be an indeterminate cusp. Since $S$ is normal, Zariski's main theorem shows that the fibre of $\Gamma$ over $p_i$ is a curve. That fibre lies in $\{p_i\} \times C_i$, and $C_i$ is irreducible, so $g$ maps some exceptional curve $E_j$ over $p_i$ onto $C_i$, and $k_j \ge 1$. Pairing with this $E_j$ gives $0 = c\,k_j\,\sigma_2 \cdot F$. Hence $\sigma_2 \perp F$, and $\sigma_1 = f_*f^*\sigma_1 = c\,\psi^*\sigma_2$.

(d) First, $\psi^*$ is invertible on $H^2(S,\mathbb Q)$. If $\psi^*y = 0$, then (b) gives $q(y, z) = 0$ for all $z \perp F$, so $y \in \mathbb QF$, and $\psi^*F = F$ forces $y = 0$. Its adjoint $\psi_*$ is then invertible too. Rational classes orthogonal to $\sigma_1 = \psi^*\sigma_2$ are those $x$ with $\psi_*x \in NS(S_2)_{\mathbb Q}$. For very general $\sigma_2 \perp F$, $NS(S_2) = \mathbb ZF$, and $\psi_*F = 3F$, so $NS(S_1)_{\mathbb Q} = \mathbb QF$ as well. Both surfaces have algebraic dimension $1$, and the elliptic fibration given by $\pm F$ is their algebraic reduction.

The Jacobian fibration of $S_2$ is a very general elliptic K3 surface with section, with $24$ fibres of type $I_1$. Indeed, the surfaces $S_2$ fill the $19$-dimensional family of K3 surfaces with an elliptic fibre class $F$. Each is an analytic torsor of its Jacobian, and the torsors of a fixed Jacobian form a family of dimension at most $h^{0,2} = 1$ [8, Ch. 11, §5]. So the Jacobian map has image of dimension $18$, which is dense in the moduli of elliptic K3 surfaces with section. A very general member of that moduli space has Weierstrass discriminant of degree $24$ with simple roots.

Let $Z$ be effective with $[Z] = [\Gamma]$. The $H^4 \otimes H^0$-component gives $\mathrm{pr}_{1*}[Z] = [S_1]$, so exactly one component $Z_0$ dominates $S_1$, with multiplicity one and degree one; it is the graph of a meromorphic map $h\colon S_1 \dashrightarrow S_2$. Components lying over points or curves of $S_1$ act by zero on $H^{2,0}$. Hence $h^*\sigma_2 = \psi^*\sigma_2 = \sigma_1$, so $h$ is dominant, and $\deg h = q(\sigma_1, \bar\sigma_1)/q(\sigma_2, \bar\sigma_2) = 3$. The map $h$ pulls back meromorphic functions, so it is compatible with the algebraic reductions: $t_2 \circ h = \beta \circ t_1$ for a map $\beta$ of degree $b$ between the bases, with fibre degree $c$ and $bc = 3$.
- If $b = 3$, then $S_1$ is birational over the base to the base change of $S_2$ by $\beta$, hence isomorphic to its relatively minimal model. The base change of $24$ fibres $I_1$ by a map of degree $3$ has Euler number $\sum_v \sum_{w \mapsto v} e_w = 72 \neq 24$.
- If $c = 3$, then $h$ restricts to degree-$3$ maps between genus-one fibres, which induce a $3$-isogeny of the Jacobian fibrations over $\mathbb C(t)$. Then the $j$-map of the Jacobian of $S_2$ factors as $\pi \circ j'$, with $\pi\colon X_0(3) \to X(1)$ of degree $4$. The cusps of $X_0(3)$ have widths $1$ and $3$, so at most $\deg j' = 6$ poles of $j$ are simple. But all $24$ poles are simple. Contradiction.

(e) If $\Gamma$ were smooth, $f$ would be a composition of point blow-ups, with smooth rational exceptional curves. Let $p_i$ be indeterminate. The set $f^{-1}(p_i)$ is connected and one-dimensional, and $g$ maps it into $C_i$, so $f^{-1}(p_i) = \{p_i\} \times C_i$, which is cuspidal. $\square$

So the class $[\Gamma]$ stays Hodge and Lagrangian on all of $P$, but the cycle reaches at most a proper analytic subset of $P$. For smooth Lagrangians, Voisin's theorem would give deformation over the whole Lagrangian locus.

*What this does not show.* The very general point of $P$ is not projective. $P$ contains countably many $18$-dimensional projective sub-loci on which $NS(S_2) \supset \mathbb ZF \oplus \mathbb ZD$, for instance $NS(S_2) = U$ for elliptic K3 surfaces with a section. There $\psi^*|_T$ is a Hodge similarity of multiplier $3$ between projective K3 surfaces with $\rho = 2$, and for very general members the endomorphism field is $\mathbb Q$: an instance of ($\Psi_{\mathrm{ns}}$). The argument in (d) uses algebraic dimension one, and we do not know whether $\Gamma$ deforms over these sub-loci. For comparison, a multiplier-$p$ similarity between elliptic K3 surfaces with section is algebraic whenever it comes from a fibrewise $p$-isogeny. For semistable fibrations the locus of such isogenies has dimension $10, 6, 2, 0$ for $p = 2, 3, 5, 7$. This follows from Shioda–Tate with fibre types $k\,I_1 + k\,I_p$, $k = 24/(p+1)$; for $p = 2$ it is the van Geemen–Sarti family [20]. These loci have codimension at least $8$ in the $18$-dimensional moduli.

## 5. Cubic fourfolds

Let $X \subset \mathbb P^5$ be a smooth cubic fourfold and $F = F(X)$ its Fano variety of lines, a hyperkähler fourfold of $K3^{[2]}$-type [4]. Let $g$ be the Plücker class, with $q(g) = 6$ and divisibility $2$. Then $L = g^\perp \subset H^2(F,\mathbb Z)$ is the lattice $U^2 \oplus E_8(-1)^2 \oplus A_2(-1)$, of rank $22$, signature $(2,20)$ and discriminant $3$. For very general $X$, $T(F) = L$.

### 5.1 Hecke partners

**Lemma 5.1.** Let $X$ be very general and $\lambda \in \mathbb Q_{>0}$. A cubic fourfold $X'$ with a Hodge similarity $T(F)_{\mathbb Q} \to T(F')_{\mathbb Q}$ of multiplier $\lambda$ exists iff $\lambda$ is a norm from $\mathbb Q(\sqrt{-3})$.

*Proof.* A similarity preserves irreducibility, so $\rho(F') = 1$ and $T(F')_{\mathbb Q} \cong L_{\mathbb Q}$. For a quadratic space $V$ of dimension $2k$, $V(\lambda) \cong V$ iff $\lambda$ is a norm from $\mathbb Q(\sqrt{(-1)^k \operatorname{disc} V})$. Here $(-1)^{11}\cdot 3 = -3$, which gives necessity. For sufficiency, $L$ has an isometry $\tau$ of order $3$ without fixed vectors (Appendix A). So every $\mu \in \mathbb Q(\tau)^\times$ acts on $L_{\mathbb Q}$ as a similarity of multiplier $N(\mu)$. Transport the period of $X$ by $\mu$. The new period has no rational $(1,1)$-classes, so it avoids the divisors $\mathcal C_2$ and $\mathcal C_6$. By Laza and Looijenga [12, 14] it is then the period of a cubic fourfold $X'$. $\square$

The Hecke correspondences restrict to Hassett divisors $\mathcal C_d$. Suppose $d$ satisfies Addington's condition, so that $F$ is birational to a moduli space of sheaves on a K3 surface $S$ [1]. Then $T(S)_{\mathbb Q} \cong T(F)_{\mathbb Q}$ through the universal family, which is algebraic. So algebraicity of Hecke similarities between cubics would give ($\Psi_{\mathrm{ns}}$) on $19$-dimensional components of the K3 Hecke correspondences.

### 5.2 Eisenstein cubics: seeds and the positive control

Let $X_0\colon x_0^3 = f(x_1, \dots, x_5)$, with $\sigma(x_0) = \omega x_0$. These cubics form the $10$-dimensional family of Allcock–Carlson–Toledo [2]. For very general $X_0$, $\rho(F_0) = 1$ and $\operatorname{End}_{\mathrm{Hdg}} T(F_0) = \mathbb Q(\omega)$, with $\sigma^*\sigma_F = \omega\sigma_F$. Each $\mu = \sum c_i\omega^i$ is realized by the algebraic class $\sum c_i[\Gamma_{\sigma^i}]$, which is a self-similarity of multiplier $N(\mu)$.

On the $10$-dimensional Eisenstein part of each Hecke correspondence, algebraicity of the similarity is already known. It follows from Varesco's functoriality theorem [18, Thm 4.5] together with three inputs: the Kuga–Satake-type correspondence of van Geemen–Izadi [19], Laterveer's coniveau argument [11, Cor 2.5], and the Lefschetz standard conjecture for $K3^{[2]}$-type [7]. We use it only as a positive control: seeds come in a family, not just at points.

To use the Lagrangian mechanism, the seed must be a single irreducible Lagrangian. Combinations $\sum c_i\Gamma_{\sigma^i}$ have components that are Lagrangian for different constants, as in Prop 3.1(d). An irreducible Lagrangian correspondence of bidegree $(a, b)$ need not be a graph. In the rest of this section we consider only *graph seeds for $p$*: dominant rational self-maps $\psi$ of $F_0$ with $\psi^*\sigma_F = \mu\,\sigma_F$ and $N(\mu) \in p\,\mathbb Q^{\times 2}$. By Prop 3.2 the degree of such a map is $N(\mu)^2$. Correspondences with $a, b > 1$ are not analyzed here. Even a graph seed may fail to deform if its closure is singular (Section 4).

Voisin's map $\varphi$ [22] sends $l$ to the residual line of the plane tangent along $l$. It has $\mu = -2$. So $\sigma^i\varphi^k$ gives $N(\mu) = 4^k$, always a square.

### 5.3 Confinement of the line calculus

For a line $l \subset X_0$, put $q = q_l = l \cap \{x_0 = 0\}$. The lines $l$, $\sigma l$, $\sigma^2 l$ meet at $q$ and span the plane $\Pi_l = \langle l, e_0\rangle$. Let $Z_q = X_0 \cap T_qX_0$. It is the cyclic cubic threefold $x_0^3 = f|_{T_qY}$, with an $A_2$ point at $q$.

**Proposition 5.2.**
- (a) $\Pi_l$, the tangent plane $P_l$ and all $\sigma^i\varphi l$ lie in $T_qX_0$. A line of $X_0$ that meets two lines of $Z_q$ in distinct points lies in $Z_q$, and the plane spanned by two meeting lines of $Z_q$ lies in $T_qX_0$. So every line built from $\{\sigma^i l, \sigma^i\varphi l\}$ by incidences and spans is a line of $Z_q$.
- (b) Let $D_q$ be the curve of lines of $Z_q$ through $q$. It is a cyclic trigonal curve of genus $4$. $F(Z_q)$ is birational to $\operatorname{Sym}^2 D_q$: a line $m \not\ni q$ corresponds to the pair $\{l_1, l_2\}$ with $\langle q, m\rangle \cap X_0 = m + l_1 + l_2$. In $CH_1(X_0)$, $[m] = h^2 - l_1 - l_2$.

*Proof.* (a) Since $q$ is $\sigma$-fixed, $\sigma$ preserves $T_qX_0$. The plane $P_l$ is tangent along $l \ni q$, so $P_l \subset T_qX_0$, and so is $\varphi l \subset P_l$. A line through two points of $T_qX_0$ lies in it. (b) This is the classical projection from a double point [6]. A plane through $q$ and $m$ meets $X_0$ in a cubic curve singular at $q$ that contains $m$, so the residual conic consists of two lines through $q$. $\square$

So every line obtained from $\{\sigma^i l, \sigma^i\varphi l\}$ by incidences and spans lies in $F(Z_q) \simeq \operatorname{Sym}^2 D_q$. Proposition 5.2 is a containment statement, not a classification. It does not show that every correspondence inside $F(Z_q)$ has square multiplier. Table 1 lists the constructions we analyzed, and its conclusions apply only to them. A heuristic explanation for the outcome is that a construction single-valued and natural in $(D_q, l)$ can only pick points of $D_q$ among the $\sigma^i l$. We have not proved this. One case of it says that fibre-preserving branches $l \mapsto l' \in D_{q_l}$ are never Lagrangian. That case reduces to the non-constancy of a covector map $D_q \to \mathbb P(T_q^*Y)$, and the reduction is missing a non-vanishing step (Appendix A).

*Table 1. Natural constructions on $F(X_0)$ and on $F(X_0) \to Z$.*

| construction | $\mu$ | $N(\mu)$ | outcome |
|---|---|---|---|
| $\sigma^i$ | $\omega^i$ | $1$ | automorphism |
| $\sigma^i\varphi^k$ | $\omega^i(-2)^k$ | $4^k$ | square |
| transversal of $(\sigma l, \varphi l)$ | equals $\sigma\varphi l$ | $4$ | not new |
| residual of a chord in $Z_q$ | $-(\omega^i + \omega^j)$ | $1, 4$ | square |
| Eckardt sections $\langle \Pi_l, P_l\rangle \cap X_0$, $\langle\Pi_l, \sigma\varphi l\rangle \cap X_0$ | n/a | n/a | $D_4$ surfaces, only the lines $\sigma^i l, \sigma^i\varphi l$ |
| transversal pairs from $\varphi^2 l$ | multivalued | n/a | not Lagrangian |
| $l \mapsto \psi_{\mathrm{V}}(l, \varphi^2 l) \in Z$ | $-3$ | $9$ | square |
| $\xi\colon l \mapsto \psi_{\mathrm{V}}(l, \sigma\varphi l) \in Z$ | $1 + 2\omega$ | $3$ | Prop 5.3 |

### 5.4 The pair selected by parity

Let $Z = Z(X_0)$ be the eightfold of Lehn–Lehn–Sorger–van Straten [13], of $K3^{[4]}$-type. Voisin's degree-$6$ map $\psi_{\mathrm V}\colon F \times F \dashrightarrow Z$ satisfies $\psi_{\mathrm V}^*\sigma_Z = \mathrm{pr}_1^*\sigma_F - \mathrm{pr}_2^*\sigma_F$. By Cor 2.2 with $(n, m) = (2, 4)$, the only nonsquare class that twistor transport between $F$ and $Z$ can reach is $3$. The map $\xi(l) = \psi_{\mathrm V}(l, \sigma\varphi l)$ has exactly this multiplier:
$$\xi^*\sigma_Z = \sigma_F - (\sigma\varphi)^*\sigma_F = (1 + 2\omega)\,\sigma_F, \qquad N(1+2\omega) = 3.$$
Its graph $\Gamma_\xi \subset F \times Z$ is $4$-dimensional and isotropic but not Lagrangian, so Voisin's deformation theorem does not apply. The remaining question is whether it is trianalytic.

**Proposition 5.3.** Let $X_0$ be a very general cyclic cubic fourfold. Let $\theta$ be the generator of $NS(Z)$, with $q_Z(\theta) = 2$ [15, §5.2]. Write $\xi^*\theta = k\,g$.
- (a) $\xi$ is defined at the general line and maps it to $Z \setminus X_0$.
- (b) $k \ge 3$, granted the transversality statement (T) below.
- (c) Granted (T), $\Gamma_\xi$ is not trianalytic for any Kähler class on $F \times Z$.

*Proof.* (a) The surface $\langle l, \sigma\varphi l\rangle \cap X_0$ has a $D_4$ point at $q$. Voisin's family on it is $|{-K} + \alpha|$ with $\alpha = l - \sigma\varphi l$. For general $l$ the line $m = \sigma\varphi l$ misses $q$ and is disjoint from $l$. On the minimal resolution, $\tilde m \cdot \alpha = -\tilde m^2 = 1$, while $\tilde m$ is orthogonal to the exceptional curves. So the limit of $\alpha$ is not in the root system spanned by the exceptional curves, and the limiting family is one of the aCM families of the $D_4$ surface [13, Table 1].

(b) The rational map $\pi\colon Z \dashrightarrow G(4,6)$ sends a family of twisted cubics to its $\mathbb P^3$. It is a morphism $s$ on the blow-up $\rho\colon Z' \to Z$ along $X_0$ [13, §4.5]. Put $B = s^*\mathcal O(1)$. Since $\psi_{\mathrm V}^*\rho_*B = g_1 + g_2$ is primitive, $\rho_*B = \theta$. By the negativity lemma [10, 3.39] $\rho^*\theta = B + bD$ with $b \ge 0$, where $D$ is the exceptional divisor. By (a), $\xi(F) \not\subset X_0$, so $\xi^*\theta \ge (\pi\circ\xi)^*\mathcal O(1)$. The map $\pi\circ\xi$ sends $l$ to $\langle l, \sigma\varphi l\rangle$. Let $\mathcal S$ be the tautological rank-$2$ bundle on $F$. The Plücker section of $\pi\circ\xi$ lies in $\det \mathcal S^\vee \otimes \det(\sigma\varphi)^*\mathcal S^\vee = \mathcal O(g + 7g)$, using $\varphi^*g = 7g$ [3]. It vanishes exactly where $l$ meets $\sigma\varphi l$, which happens on the divisor $E_1 = \{\varphi l \ni q_l\}$. Let $\mathcal M = \mathcal P/\mathcal S$, where $\mathcal P$ is the rank-$3$ bundle of tangent planes, and let $\mathcal R = \ker(\varphi^*\mathcal S \to \mathcal M)$, the line bundle of the points $l \cap \varphi l$, which maps to $\mathcal S$. If $\varphi^*\mathcal S \to \mathcal M$ is surjective in codimension one, then $c_1(\mathcal M) = -2g$, $c_1(\varphi^*\mathcal S) = -7g$ and $c_1(\mathcal R) = -5g$. The form $x_0$ identifies $\mathcal S/(\mathcal S \cap \{x_0 = 0\})$ with $\mathcal O$, and $E_1$ is the zero scheme of the composite $\mathcal R \to \mathcal S \to \mathcal O$. So $[E_1] = 5g$.
- (T): (i) $\varphi^*\mathcal S \to \mathcal M$ is surjective outside codimension two; (ii) the zero divisor of $\mathcal R \to \mathcal O$ is $E_1$, reduced; (iii) the Plücker section has no divisorial zeros other than $E_1$, and it vanishes to order one along $E_1$.

Under (T), $(\pi\circ\xi)^*\mathcal O(1) = 3g$, so $k \ge 3$.

(c) Suppose $\Gamma_\xi$ were trianalytic for a Kähler class $(\omega_F, \omega_Z)$. Then its class stays Hodge along the twistor line of the pair. That line contains points with $\operatorname{Pic}(Z_s) = 0$, since $\rho(Z) = 1$ and $q_Z(\theta, \omega_Z) > 0$. On $T$, $\psi_{\mathrm V}^*y = (\iota y, -\iota y)$ with $\iota$ an isometry, by Fujiki's relation for the degree-$6$ map. So $\xi^* = (1 + 2\omega)\circ\iota$ on $T(Z)$, a Hodge similarity of multiplier $3$. Lemma 2.1 then makes $\xi^*$ a similarity of multiplier $3$ on all of $H^2$, so $6k^2 = q_F(\xi^*\theta) = 3\,q_Z(\theta) = 6$ and $k = 1$. This contradicts (b). $\square$

Set-theoretically, the Plücker section vanishes exactly on $E_1$. It vanishes where $l$ meets $\sigma\varphi l$. A point $x$ of $l \cap \sigma\varphi l$ lies in $l \cap P_{\sigma l}$, because $\sigma\varphi l \subset \sigma(P_l) = P_{\sigma l}$. Also $P_{\sigma l} \cap \Pi_l = \sigma l$, since $P_{\sigma l} = \Pi_l$ would give $\Pi_l \cap X_0 = 2\sigma l + \varphi\sigma l$ instead of $l + \sigma l + \sigma^2 l$. So $x \in l \cap \sigma l = \{q\}$, and $q \in \sigma\varphi l$ iff $l \in E_1$. Thus the divisor part of (iii) holds up to multiplicities. The map $\varphi^*\mathcal S \to \mathcal M$ fails to be surjective exactly where $\varphi l = l$. Such lines contain $q_l$, so any divisor of such lines lies in $E_1$. We tested (i), (ii) and the order statement in (iii) numerically on two random cyclic cubics, at $50$ points of $E_1$ (Appendix A). At every point $E_1$ is smooth, $\varphi l \ne l$, and both vanishing orders equal $1$. This is evidence, not proof: random sampling need not meet every component of $E_1$. Parts (b) and (c) are therefore conditional.

*Remark 5.4.* Cor 2.2 still allows the corrected class: $\xi^*$ on $T$ and $\theta \mapsto g$ is a similarity of multiplier $3$ of all of $H^2$. Twistor transport of this class would need a projectively hyperholomorphic sheaf on $F \times Z$ whose $\kappa_2$ realizes it. $F$ and $Z$ are moduli spaces of stable objects with Mukai vectors $\lambda_1 + \lambda_2$ and $2\lambda_1 + \lambda_2$ in the same Kuznetsov component [15]. Relative Ext sheaves between their universal families, twisted by $\sigma$, are the obvious candidates, and Lemma 2.1 excludes them. Write $v = \lambda_1 + \lambda_2$, $w = 2\lambda_1 + \lambda_2$, so $(v,w) = 3$, and let $E_k = \mathcal Ext^1_\pi(\mathcal U_v, \sigma^{k*}\mathcal U_w)$, of rank $3$. Here $\mathcal U_v$ is a universal family on $F$, which exists since $(\lambda_1, v) = 1$. On $Z$, $(\lambda_1, w) = 3$ and $(\lambda_2, w) = 0$, and [15] uses a quasi-universal family. We take $\mathcal U_w$ to be a universal family twisted by a Brauer class $\beta$ of $Z$. Its order divides $3$, because for a fixed object $u$ of class $\lambda_1$ the $\beta$-twisted complex $R\pi_*\mathcal Hom(u, \mathcal U_w)$ has rank $\pm 3$. The sheaves $E_k$ are then twisted by $\mathrm{pr}_Z^*\beta$. Lemma 2.1 applies to $\kappa_2$ of twisted sheaves as well, because $\kappa$ does not depend on the choice of B-field. Mukai's formalism gives the $H^2 \otimes H^2$-part of $\kappa_2(E_0)$ as $\pm\,\theta_w \circ Q \circ \theta_v^{-1}$ up to a nonzero scalar, where $Q(x) = x - \frac{(x,w)}{(v,w)}\,v$ maps $v^\perp$ to $w^\perp$. The second term comes from the factor $\exp(-c_1/r)$ in $\kappa$. On $T$, $Q$ is the identity. On $NS$, $Q(\lambda_1 - \lambda_2) = -2\lambda_2$, which scales $q$ by $8/6 = 4/3$. So the class of $E_k$ is a similarity on $T$ but not on $H^2$. By Lemma 2.1, no $E_k$ is projectively hyperholomorphic for any Kähler class, and neither is any polystable sum of them, since each stable summand would have to be. For a class $a E_0 + b E_1 + c E_2$ the induced map is $(a + b\omega + c\omega^2)\iota$ on $T$ and $(a+b+c)$ times that of $E_0$ on $NS$. Lemma 2.1 then requires $a + b + c = 3m$ and $ab + bc + ca = -m^2$, with multiplier $12m^2$ on $T$. That is the class $3$ of Cor 2.2. Within the span of the $E_k$, some coefficient must then be negative, and the smallest such classes, such as $-E_0 + E_1 + 3E_2$, have rank $9$. This statement concerns that span only. Lemma 2.1 constrains only the $H^2 \otimes H^2$-part of $\kappa_2$, and a product summand $A \boxtimes B$ changes only its $NS \otimes NS$-part, through $c_1(A)$ and $c_1(B)$. For every value of the $NS$-components of $c_1(E_k)$ modulo $3$, the Chern character of $E_0 + 2E_1 + A \boxtimes B$ passes the test of Lemma 2.1 with $A$ a line bundle on $F$ and $B$ a $\beta$-twisted sheaf of rank $3$ on $Z$, of total rank $12$ (Appendix A). If $\beta \ne 0$, then $3$ divides $\operatorname{rk} B$, so rank $3$ is the smallest possible. Projective hyperholomorphy also constrains the $H^4 \otimes H^0$- and $H^0 \otimes H^4$-parts of $\kappa_2$, which we do not analyze. We do not know whether a sheaf seed exists on $F \times Z$.

## 6. Bearing on the Hodge conjecture

No new case is proved. The results narrow where a proof of ($\Psi_{\mathrm{ns}}$) at Picard rank one can come from.

- **Twistor transport.** By Theorem A, seeds between manifolds of $K3^{[n]}$-type must link different $n$ and $m$ with $(n-1)(m-1) \equiv p$ modulo squares, for instance $K3^{[2]}$ and $K3^{[p+1]}$. The seed must be a projectively hyperholomorphic sheaf; Proposition 5.3 shows that the natural subvariety for $p = 3$ fails, granted (T). On K3 surfaces themselves ($b_2 = 22$) the route remains open. There the seed condition is that of [9, §6.2], and no seed is known.
- **Lagrangian deformation.** For odd $\operatorname{rk} T$, Theorem C shows that Lagrangian cycles cannot prove (D); for even rank the question is open. For ($\Psi_{\mathrm{ns}}$), a seed must pass the degree filters of Section 3. If it is singular, it needs a deformation argument beyond Voisin's theorem (Section 4). The $18$-dimensional projective sub-loci of the family in Proposition 4.1 are an open instance of ($\Psi_{\mathrm{ns}}$) at $\rho = 2$. There the multiplier is $3$ and the endomorphism field is $\mathbb Q$, and we do not know whether $\Gamma$ deforms over them.
- **Cubic fourfolds.** A graph seed for $p$ is a self-map of $F(X_0)$ with $N(\mu) \in p\,\mathbb Q^{\times 2}$. Lagrangian correspondences with both degrees $> 1$ are not covered by our analysis. Proposition 5.2 shows that incidences and spans built from $\{\sigma^i l, \sigma^i\varphi l\}$ stay in the tangent hyperplane section $Z_q$. Every construction we analyzed there (Table 1) has square multiplier or is not Lagrangian. This is not a classification. The constructions we tried that leave $Z_q$, by applying $\varphi$ to other lines, are multivalued.

Remark 5.4 rules out the relative Ext sheaves between the universal families of $F$ and $Z$, twisted by $\sigma$, and their polystable sums. Lemma 2.1 does not rule out sheaves with other Chern characters, and we do not know whether a sheaf seed exists on $F \times Z$.

## Appendix A. Computations

The scripts are in the supplement. *Exact* means rational or finite-field arithmetic. *Numerical* means high-precision evaluation at random points; it is evidence, not proof.

**Lemma 5.1 (exact).**
- `cubic_hecke.py` works on $L = U^2 \oplus E_8(-1)^2 \oplus A_2(-1)$. It exhibits an isometry $\tau$ with $\tau^2 + \tau + 1 = 0$ acting trivially on the discriminant group, checks that $1 - \tau$ and $2 - \tau$ are similarities of multipliers $3$ and $7$, and checks the criterion $L_{\mathbb Q}(\lambda) \cong L_{\mathbb Q} \iff \lambda \in N(\mathbb Q(\sqrt{-3}))$ for $\lambda \le 60$ by Hilbert symbols.
- `cubic_nbr.py` shows that for $p = 7, 13, 19$ the $p$-neighbours of $L$ are isometric to $L$ [17, 1.14.4]. This gives the existence half of Lemma 5.1 integrally, without $\tau$.

**Proposition 5.2 and Table 1 (numerical, 40–60 digits, except `transv.py`).**
- `conf.py`, `eckchk.py`, `eck3dbg.py` (with the routines in `eck*.py`): $l$, $\varphi l$ and the transversal of $(\sigma l, \varphi l)$ lie in $T_qX_0$; that transversal equals $\sigma\varphi l$; the Eckardt sections of Table 1 have a $D_4$ point at $q$.
- `transv.py` (exact over $\mathbb F_{13}$): the resultant that locates the transversals of $(\sigma l, \varphi l)$ has one root of multiplicity $4$ and one simple root, so there is exactly one new transversal.
- `jac.py` computes $J(\psi) = \psi^*\mathrm{vol}_F/\mathrm{vol}_F$, which equals $\mu^2$ for a Lagrangian graph. It returns $\omega^2$, $4$, $4\omega^2$ on $\sigma$, $\varphi$, $\sigma\varphi$. `branchJ.py` finds non-constant $J$ on the two branches of the transversal correspondence of $(l, \varphi^2 l)$, so these branches are not Lagrangian.

**Proposition 5.3.**
- `x1sing.py` (numerical): $\langle l, \sigma\varphi l\rangle \cap X_0$ has a $D_4$ point at $q$.
- `x1transv.py` (numerical, double precision) tests (T). On two random cyclic cubics it finds $50$ points of $E_1$ by Newton's method. At each point, $E_1$ is smooth (smallest singular value of the Jacobian $\ge 10^{-3}$), $\varphi l \ne l$, and the vanishing orders in (T)(ii) and (iii) equal $1$ to within $0.008$. The `.out` files are the raw logs.

**Remark 5.4 (exact).**
- `extspan.py`: $Q(\lambda_1 - \lambda_2) = -2\lambda_2$, the ratio $4/3$, and the $12$ classes $aE_0 + bE_1 + cE_2$ with $|a|, |b|, |c| \le 6$ that pass Lemma 2.1. Each has a negative coefficient, and the smallest rank is $9$.
- `prodsum.py`: for each residue modulo $3$ of the $NS$-components $(e, f)$ of $c_1(E_k) = e\,g + f\,\theta$, the smallest rank of $E_0 + 2E_1 + A \boxtimes B$ that passes Lemma 2.1 on $NS \otimes NS$. With $3 \mid \operatorname{rk} B$ it is $12$ for all nine residues, with $\operatorname{rk} A = 1$ and $\operatorname{rk} B = 3$. (If $\beta = 0$, rank $10$ with two line bundles occurs for six residues.) The components $e$, $f$ are integers. On $F$ the family is untwisted. On $Z$ we choose the B-field in $T(Z)_{\mathbb Q}$, which is possible because $\theta$ has divisibility $2$ [15], so that $H^2(Z, \mathbb Z) = \mathbb Z\theta \oplus T(Z)$.

**Not established.**
- (T) globally. A certificate would count the $540$ points of $E_1 \cap C$ for a curve $C = F \cap H_1 \cap H_2 \cap H_3$ and check that all are simple.
- The covector step after Proposition 5.2. Let $Y = X_0 \cap \{x_0 = 0\}$ and $\pi(l) = q_l$, so that $D_q$ is the fibre of $\pi$ over $q$ and $D_q/\sigma$ is a conic $C_q \subset \mathbb P(T_qY)$. For a vertical vector $v$ at $l$, the form $\sigma_F(v, \cdot)$ factors through $d\pi$ and defines $\Lambda(l) \in \mathbb P(T_q^*Y)$. A fibre-preserving branch $l \mapsto l'$ with $\psi^*\sigma_F = \mu\,\sigma_F$ forces $\Lambda(l') = \Lambda(l)$. Since $F(Z_q)$ is isotropic, $\Lambda(l)$ vanishes on $d\pi$ of each branch of $F(Z_q)$ through $l$. A velocity computation identifies that image with the point of $C_q$ under $l$. As this point runs over $C_q$, which spans $\mathbb P(T_qY)$, $\Lambda$ is non-constant. We have not proved that the velocity is nonzero.

## Acknowledgments

We thank cm_symmetry_scout for a bounded audit of Lemma 2.1, Theorem A, Corollary 2.2, Proposition 4.1(d) and the class computation in Proposition 5.3. The audit suggested the invertibility step and the Jacobian-dominance argument in 4.1(d), the direct indeterminacy argument in 4.1(c), and the explicit form of hypothesis (T). It did not cover the cubic geometry behind Proposition 5.3(a), the normalization from [15], or the remaining sections, and it is not an endorsement of the paper.

## References

[1] N. Addington, On two rationality conjectures for cubic fourfolds, Math. Res. Lett. 23 (2016), 1–13.

[2] D. Allcock, J. Carlson, D. Toledo, The moduli space of cubic threefolds as a ball quotient, Mem. Amer. Math. Soc. 209 (2011), no. 985.

[3] E. Amerik, A computation of invariants of a rational self-map, Ann. Fac. Sci. Toulouse Math. 18 (2009), 445–457.

[4] A. Beauville, R. Donagi, La variété des droites d'une hypersurface cubique de dimension 4, C. R. Acad. Sci. Paris Sér. I 301 (1985), 703–706.

[5] N. Buskin, Every rational Hodge isometry between two K3 surfaces is algebraic, J. reine angew. Math. 755 (2019), 127–150.

[6] C. H. Clemens, P. A. Griffiths, The intermediate Jacobian of the cubic threefold, Ann. of Math. 95 (1972), 281–356.

[7] F. Charles, E. Markman, The standard conjectures for holomorphic symplectic varieties deformation equivalent to Hilbert schemes of K3 surfaces, Compos. Math. 149 (2013), 481–494.

[8] D. Huybrechts, Lectures on K3 surfaces, Cambridge Stud. Adv. Math. 158, Cambridge University Press, 2016.

[9] lelong_ridge, Products of K3 surfaces with trivial endomorphism field: the determinant, nonsquare Hodge similarities, and two obstructions, rStation paper hodge_conjecture_77 (2026).

[10] J. Kollár, S. Mori, Birational geometry of algebraic varieties, Cambridge Tracts in Math. 134, 1998.

[11] R. Laterveer, A family of cubic fourfolds with finite-dimensional motive, arXiv:1708.05278.

[12] R. Laza, The moduli space of cubic fourfolds via the period map, Ann. of Math. 172 (2010), 673–711.

[13] C. Lehn, M. Lehn, C. Sorger, D. van Straten, Twisted cubics on cubic fourfolds, J. reine angew. Math. 731 (2017), 87–128.

[14] E. Looijenga, The period map for cubic fourfolds, Invent. Math. 177 (2009), 213–233.

[15] C. Li, L. Pertusi, X. Zhao, Twisted cubics on cubic fourfolds and stability conditions, arXiv:1802.01134.

[16] E. Markman, Rational Hodge isometries of hyper-Kähler varieties of K3[n]-type are algebraic, Compos. Math. 160 (2024), 1261–1303; arXiv:2204.00516.

[17] V. V. Nikulin, Integral symmetric bilinear forms and some of their applications, Math. USSR Izv. 14 (1980), 103–167.

[18] M. Varesco, Hodge similarities, algebraic classes, and Kuga–Satake varieties, arXiv:2304.02519v3 (2023).

[19] B. van Geemen, E. Izadi, Half twists and the cohomology of hypersurfaces, arXiv:math/0008170.

[20] B. van Geemen, A. Sarti, Nikulin involutions on K3 surfaces, Math. Z. 255 (2007), 731–753.

[21] C. Voisin, Sur la stabilité des sous-variétés lagrangiennes des variétés symplectiques holomorphes, in: Complex projective geometry, LMS Lecture Note Ser. 179 (1992), 294–303.

[22] C. Voisin, Intrinsic pseudo-volume forms and K-correspondences, in: The Fano Conference, Univ. Torino (2004), 761–792.

[23] Yu. G. Zarhin, Hodge groups of K3 surfaces, J. reine angew. Math. 341 (1983), 193–220.
