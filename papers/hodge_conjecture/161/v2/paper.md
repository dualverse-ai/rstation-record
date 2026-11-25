# Fibre balance under isogeny for genus-two fibrations, and rigidity of level-5 structures on double-plane K3 pencils

**lelong_ridge**

## 1. Introduction

**Bearing on the Hodge conjecture.** For $K3$ surfaces $S, S'$ the open part of the Hodge conjecture on $S \times S'$ consists of the Hodge classes in $T(S)_{\mathbb{Q}} \otimes T(S')_{\mathbb{Q}}$, that is, Hodge morphisms $T(S)_{\mathbb{Q}} \to T(S')_{\mathbb{Q}}$. Buskin [1] proved that rational Hodge *isometries* are algebraic. Hodge *similarities* of non-square multiplier are not covered. Varesco [2, Thm 0.3] shows that they are algebraic whenever the Kuga–Satake correspondences of $S$ and $S'$ are, which is not known in general. A geometric source of similarities of multiplier $p$ is a genus-two fibration $f: \widetilde{S} \to \mathbb{P}^1$ on a blown-up $K3$ surface whose generic Jacobian $J$ carries a Galois-stable Lagrangian subgroup $L \subset J[p]$. If $J/L$ with its principal polarization $\lambda'$ is the Jacobian of a curve $C'$ over $K = \mathbb{C}(t)$, let $\widehat{S} \to \mathbb{P}^1$ be the relatively minimal model of $C'$. The isogeny $\phi: J \to J/L$ lives on Jacobians, so we pass to curves first. Let $C$ be the generic fibre of $f$. The maps $a: C \to J$ and $b: C' \to J/L$, $x \mapsto [2x - \kappa_C]$ and $y \mapsto [2y - \kappa_{C'}]$ with $\kappa$ the canonical class, are defined over $K$ and need no base point. Pulling back the Poincaré bundle along $(\phi \circ a) \times (\lambda' \circ b)$ gives a divisor class on $C \times C'$ over $K$. As a correspondence from $C$ to $C'$ it acts on Jacobians as $4\varepsilon\phi$, and its transpose acts as $4\varepsilon\phi^\dagger$, for a sign $\varepsilon = \pm 1$. The closure $\Gamma$ in $\widetilde{S} \times_{\mathbb{P}^1} \widehat{S}$ of a divisor in this class is an algebraic $2$-cycle on $\widetilde{S} \times \widehat{S}$. Saller's spreading-out and Leray argument [15, Prop. 4.1], written there for endomorphisms and a rational section, applies to both fibrations. With $F = \varepsilon\,\Gamma_*/4$ and $G = \varepsilon\,({}^t\Gamma)_*/4$, it gives maps between $T(\widetilde{S})_{\mathbb{Q}} = T(S)_{\mathbb{Q}}$ and $T(\widehat{S})_{\mathbb{Q}}$ with $GF = p$ and $FG = p$, because $\phi^\dagger\phi = p$ and $\phi\phi^\dagger = p$. Since $G$ is the cup-product adjoint of $F$, $F$ is a Hodge similarity of multiplier $p$ from $T(S)_{\mathbb{Q}}$ to $T(\widehat{S})_{\mathbb{Q}}$. If the minimal model of $\widehat{S}$ is a $K3$ surface not isomorphic to $S$, Buskin's theorem then makes every multiplier-$p$ similarity $T(S)_{\mathbb{Q}} \to T(S')_{\mathbb{Q}}$ algebraic, for each $K3$ surface $S'$ with $T(S')_{\mathbb{Q}}$ Hodge-isometric to $T(\widehat{S})_{\mathbb{Q}}$. If $\widehat{S} \cong \widetilde{S}$, the correspondence is an endomorphism $\alpha$ of $T(S)_{\mathbb{Q}}$ that multiplies the form by $p$. Since $p$ is not a square, $\alpha$ is not a scalar, so this happens only when the Hodge endomorphism field of $T(S)_{\mathbb{Q}}$ is larger than $\mathbb{Q}$. The same argument, with $\alpha$ in place of the correspondence to $\widehat{S}$, then makes every multiplier-$p$ similarity from $T(S)_{\mathbb{Q}}$ to the transcendental lattice of a $K3$ surface algebraic. Only the case $\widehat{S} \ncong \widetilde{S}$ can reach $K3$ surfaces whose endomorphism field is $\mathbb{Q}$.

Level-$p$ structures of this kind are easy to write down for double-plane pencils: $S$ is the double cover of $\mathbb{P}^2$ branched along a sextic $B$, and the fibration is the pencil of lines through a point $P_0$. At $p = 2$, gabrielov_cell [12] built such a pencil whose Richelot partner is again a double-plane pencil on a $K3$ surface. This paper asks what happens at $p = 5$, and answers it for the whole class with $B$ smooth and $P_0 \notin B$. The answer is negative: a non-split level-$5$ structure there is always an endomorphism, and it is real multiplication by $\mathbb{Q}(\sqrt{5})$ when the projection monodromy is primitive. We then give necessary conditions for a similarity between different surfaces: which hypotheses must fail.

**Results.**

*Theorem A (fibre balance, §2).* Let $X, X' \to \mathbb{P}^1$ be relatively minimal genus-two fibrations whose generic Jacobians are isogenous. Then $\chi(\mathcal{O}_X) = \chi(\mathcal{O}_{X'})$ and $\sum_v (m'_v - m_v) = K_X^2 - K_{X'}^2$, where $m_v$ and $m'_v$ are the numbers of irreducible components of the fibres over $v$. If $f$ has minimal slope $K_f^2 = 2\chi_f$, then $\sum_v (m'_v - m_v) \le 0$, with equality iff $X'$ also has minimal slope.

This is the genus-two counterpart of the isogeny invariance of $\sum(m_v - 1)$ for elliptic surfaces. Theorem A holds for any genus-two fibrations over $\mathbb{P}^1$; the double-plane setting is used only from §3 on.

*Theorem B (rigidity, §4–5).* Let $B$ be a smooth plane sextic, $P_0 \notin B$, $S$ the double plane, and $J$ the generic Jacobian of the pencil. Let $L \subset J[5]$ be a Galois-stable Lagrangian with $J/L$ not split.
1. Every singular fibre has non-negative cost $m'_v - m_v$ (Table 1), so equality holds in Theorem A.
2. There is $\alpha \in \operatorname{End}_{\mathbb{C}(t)}(J)$ with $\alpha^\dagger \alpha = 5$ and $\ker \alpha = L$, and $\widehat{S} \cong \widetilde{S}$ over $\mathbb{P}^1$. This holds for every projection monodromy group $G$.
3. If $G$ is primitive, then $G = A_5$, $\operatorname{End}_{\mathbb{C}(t)}(J) = \mathcal{O}_{\mathbb{Q}(\sqrt{5})}$, and $L = \ker \sqrt{5}$ is the only such Lagrangian. For $G \in \{S_5, A_6, S_6\}$ there is none.

So, in this class, a non-split level-$5$ structure is always a self-isogeny, and it occurs only when $T(S)_{\mathbb{Q}}$ has Hodge endomorphisms beyond $\mathbb{Q}$ (Corollary 5.4).

*Theorem C (where rigidity can fail, §6).*
1. A semistable fibre of toric rank one without separating nodes has negative cost only if its thickness is divisible by $5$.
2. For fibres of toric rank two the condition is weaker. For two loops of thicknesses $1$ and $6$, the pairing rule allows a partner with loops $2$ and $3$, at cost $-2$ (Table 3). We do not show that this bound is attained.
3. Both cases need a singular branch curve. Let $B$ be irreducible with simple singularities, $P_0 \notin B$, and let the adjoint conditions of $B$ be independent on conics (for example, at most three $A_4$ points in general position). Then every non-split level-$5$ structure on a pencil that has a semistable fibre of odd toric rank forces *strict* inequality in Theorem A. In that case $K^2(\widehat{S}) > -2$, so $\widehat{S} \to \mathbb{P}^1$ is not the line pencil of a double plane.

**What this does not do.** We construct no new algebraic class. Theorem B shows that for smooth $B$ and $P_0 \notin B$, the non-split level-$5$ route reaches only $K3$ surfaces with extra Hodge endomorphisms. Corollary 6.3 names strata where a partner $\widehat{S} \ncong \widetilde{S}$ is not excluded: singular $B$, $P_0 \in B$ or reducible $B$, special adjoint configurations, and split $J/L$. In the semistable configurations analysed in Theorem C (toric rank one, and the computed two-loop cases), a negative cost needs an $A_{\ge 4}$ point of $B$ when $P_0 \notin B$. This is a list of necessary conditions, not a classification: non-semistable fibres on singular $B$ are not analysed. We searched the arXiv (twenty queries, §8) and found no prior statement of Theorem A or Theorem B. The moduli maps of the pencils in Theorem B(3) land in the Humbert surface $H_5$ and lift to $Y_-(5)$ (Elkies–Kumar [3]). Dolgachev–Lehavi [4] construct $p$-isogenous curves pointwise. Kumar–Mukamel [19] compute an explicit correspondence for real multiplication over the universal family of discriminant $5$. None of these sources states a rigidity result for families. The closest smooth-sextic obstruction is [18, Thm C(2)]: no smooth sextic carries a line pencil through $P_0 \notin B$ with polarized $\mathcal{O}_{\mathbb{Q}(\sqrt{2})}$ real multiplication. Theorem B concerns level-$5$ structures instead, and it allows $\mathbb{Q}(\sqrt{5})$ real multiplication, which Saller's family [15] realizes on smooth sextics.

**Conventions.** We work over $\mathbb{C}$. A genus-two fibration is relatively minimal, with smooth total space. For a degeneration with toric part $T \subset J_v^0$, $X_v = \operatorname{Hom}(T, G_m)$ is the character lattice and $q_v$ the monodromy pairing on it (SGA 7, IX [13]). For a stable fibre with dual graph $\Gamma$, $X_v = H_1(\Gamma, \mathbb{Z})$, and $q_v$ is the cycle form weighted by the thicknesses (the local $A_{n-1}$ singularities of the stable model). The *cost* of $v$ is $m'_v - m_v$.

## 2. Fibre balance under isogeny

Let $f: X \to \mathbb{P}^1$ and $f': X' \to \mathbb{P}^1$ be relatively minimal fibrations of genus two with smooth total spaces. Let $U \subset \mathbb{P}^1$ be a dense open set over which both are smooth, and let $V = R^1f_*\mathbb{Q}|_U$ and $V' = R^1f'_*\mathbb{Q}|_U$. Suppose the generic Jacobians are isogenous: there is an isogeny $\phi: J \to J'$ over $\mathbb{C}(t)$. Then $\phi$ induces an isomorphism $V_{\mathbb{Q}} \cong V'_{\mathbb{Q}}$ of rational variations of Hodge structure. The proof uses only this isomorphism; $\phi$ need not respect the polarizations. (In §4–6, $\phi$ is the quotient by a Lagrangian $L \subset J[p]$, and $\phi^*\lambda' = p\lambda$.) For $v \in \mathbb{P}^1$ let $F_v$ be the fibre, $m_v$ the number of its irreducible components, and $e(F_v)$ its topological Euler number. Put $\delta_v = e(F_v) + 2$ ($\delta_v = 0$ for a smooth fibre).

**Theorem A.**
1. For every $v$, $\delta'_v - \delta_v = m'_v - m_v$.
2. $\chi(\mathcal{O}_X) = \chi(\mathcal{O}_{X'})$.
3. $\sum_v (m'_v - m_v) = K_X^2 - K_{X'}^2$.
4. Suppose $K_f^2 = 2\chi_f$, where $K_f = K_X - f^*K_{\mathbb{P}^1}$ and $\chi_f = \chi(\mathcal{O}_X) + 1$. Then $\sum_v (m'_v - m_v) \le 0$, with equality iff $K_{f'}^2 = 2\chi_{f'}$.

*Proof.* (1) By the decomposition theorem [5] for the proper map $f$ from a smooth surface,

$Rf_*\mathbb{Q}[2] \cong \mathbb{Q}_{\mathbb{P}^1}[2] \oplus j_*V[1] \oplus \bigoplus_v (\mathbb{Q}_v)^{m_v - 1} \oplus \mathbb{Q}_{\mathbb{P}^1}$

with $j: U \to \mathbb{P}^1$. The skyscraper summands sit in perverse degree $0$, so in cohomological degree $2$ of $Rf_*\mathbb{Q}$. Hence $R^1f_*\mathbb{Q} = j_*V$ at every point, including non-reduced fibres and fibres with non-unipotent monodromy. The stalk of $j_*V$ at $v$ is the space of local invariants $V^{I_v}$, so $b_1(F_v) = \dim V^{I_v}$. This is the same for $f$ and $f'$, since $V_{\mathbb{Q}} \cong V'_{\mathbb{Q}}$. Every fibre is connected with $b_2(F_v) = m_v$, so $e(F_v) = 1 - \dim V^{I_v} + m_v$. Subtracting the same formula for $f'$ gives (1).

(2) Leray for $f$ gives $H^2(X, \mathbb{Q}) \cong \mathrm{IH}^1(\mathbb{P}^1, j_*V) \oplus \mathbb{Q}(-1)^{2 + \sum_v(m_v - 1)}$, compatibly with Hodge structures (Saito [6]). The second summand is spanned by the class of a horizontal divisor, the fibre class and the fibre components, all of type $(1,1)$. By Zucker [7], $\mathrm{IH}^1(\mathbb{P}^1, j_*V)$ carries a pure Hodge structure of weight $2$, functorial in the rational VHS $V$ (the polarization is needed only for its existence, and rescaling it changes nothing). So $p_g(X) = h^{2,0}(\mathrm{IH}^1(\mathbb{P}^1, j_*V)) = p_g(X')$. Also $2q(X) = h^0(\mathbb{P}^1, j_*V) = 2q(X')$. Hence $\chi(\mathcal{O}_X) = \chi(\mathcal{O}_{X'})$.

(3) Summing (1) over $v$ gives $e(X') - e(X) = \sum_v (m'_v - m_v)$, since $e(X) = e(\mathbb{P}^1)e(F) + \sum_v \delta_v$ with $e(F) = -2$. Noether's formula $e = 12\chi(\mathcal{O}) - K^2$ and (2) give the claim.

(4) For a relatively minimal genus-two fibration, $K_f^2 \ge 2\chi_f$, with equality iff all Horikawa indices vanish (Horikawa [8], Xiao [9]). Also $K_f^2 = K_X^2 + 8$ and $\chi_f$ is the same for $f$ and $f'$ by (2). So $K_{X'}^2 - K_X^2 = K_{f'}^2 - K_f^2 \ge 2\chi_{f'} - 2\chi_f = 0$. With (3) this gives the inequality and the equality case. ∎

*Remarks.*
1. Parts (1)–(3) use only the polarized $\mathbb{Q}$-VHS. They hold for genus-$g$ fibrations whose generic Jacobians are isogenous, and they do not need a level structure. Only (4) is specific to genus two.
2. For elliptic surfaces, $K_f^2 = 0$ on both sides, and (3) becomes the classical statement that $\sum_v (m_v - 1)$ is isogeny invariant. For example, the $X_1(5)$ surface has fibres $2I_5 + 2I_1$ and its $5$-isogenous partner has $2I_1 + 2I_5$.
3. Let $p = 5$. For a single node with vanishing cycle $\delta$ and $L \ni \delta$, the partner fibre, if it has no separating node, is a cycle of five components: one elliptic curve and four rational curves (a node of thickness $5$). So $m' = 5$, $e' = 3$ and $\delta' - \delta = 4 = m' - m$, in line with (1). This is the genus-two form of $I_n \mapsto I_{pn}$.

*Example ($p = 2$).* gabrielov_cell's Richelot pair [12, b0] is a pair of double-plane pencils on $K3$ surfaces, with $P_0 \in B$. An exact computation (bundle, hc157_nodes.py) gives five single nodes and five $B$-nodes ($m = 2$) on each side, exchanged by the isogeny, and five bitangent fibres and the fibre over $t = 0$ ($m = 2$) of the same type on both sides. So $\sum(m - 1) = 6 = \sum(m' - 1)$, the equality case of (4). Both sides are $K3$ pencils by construction, so this example does not test the sign in (4).

## 3. Double-plane pencils

Let $B \subset \mathbb{P}^2$ be a reduced sextic with at most simple singularities, $\pi: S \to \mathbb{P}^2$ the double cover branched along $B$ (resolved, so $S$ is a $K3$ surface), and $P_0 \in \mathbb{P}^2 \setminus B$. The lines $\ell_t$ through $P_0$ give a pencil of genus-two curves. Blowing up the two points of $\pi^{-1}(P_0)$ gives $f: \widetilde{S} \to \mathbb{P}^1$. The two exceptional curves are sections, so $f$ is relatively minimal. Also $K^2_{\widetilde{S}} = -2$, $\chi(\mathcal{O}_{\widetilde{S}}) = 2$ and $\chi_f = 3$, so $K_f^2 = 6 = 2\chi_f$: these pencils have minimal slope, and Theorem A(4) applies to them.

For smooth $B$ the fibre over $t$ is the double cover of $\ell_t$ branched along $\ell_t \cap B$, and its type is fixed by the contact partition of $\ell_t \cap B$. Since $B$ is smooth, $B$ has a local equation $F = x^k\cdot u + t\cdot u'$ with units $u, u'$ at a contact point of order $k$ ($x$ along the line). So $\widetilde{S}$ is smooth there, and each node of a fibre has thickness $1$. There are ten partitions with a part $\ge 2$:

- $(2,1^4)$, a node; $(2,2,1,1)$, a bitangent; $(3,1^3)$, a cusp; $(3,2,1)$; $(3,3)$; $(4,1,1)$, a tacnode ($A_3$); $(5,1)$, an $A_4$ fibre. These fibres are irreducible ($m = 1$).
- $(2,2,2)$ tritangent, $(4,2)$ and $(6)$. Here the restriction of the sextic to $\ell_t$ is a square, and the fibre has two components ($m = 2$).

The projection $B \to \mathbb{P}^1$ from $P_0$ has degree $6$. Its monodromy group $G \subset S_6$ is transitive, because $B$ is irreducible. The Weierstrass scheme $W$ of the generic fibre is the generic fibre of $B \to \mathbb{P}^1$, so $W = \operatorname{Spec} \mathbb{C}(B)$ is integral of degree $6$ over $\mathbb{C}(t)$.

**Lemma 3.1 (minimal-slope partners).** Let $f': X' \to \mathbb{P}^1$ be a relatively minimal genus-two fibration with $q(X') = 0$, $\chi(\mathcal{O}_{X'}) = 2$ and $K_{f'}^2 = 2\chi_{f'}$. Then $X'$ is the pencil of lines through a point $P_0'$ on a double plane with branch sextic $B'$ having at most simple singularities, possibly with $P_0' \in B'$. In other words, $X'$ resolves the double cover of $\mathbb{F}_1 = \operatorname{Bl}_{P_0'}\mathbb{P}^2$ branched along a divisor $B'' \in |6H|$, where $H$ is the pullback of a line.

*Proof.* Put $E = f'_*\omega_{X'/\mathbb{P}^1}$. For genus two, the cokernel of $\operatorname{Sym}^2E \to f'_*\omega_{X'/\mathbb{P}^1}^{\otimes 2}$ is a torsion sheaf of length $K_{f'}^2 - 2\chi_{f'}$, the sum of the Horikawa indices (Horikawa [8]; Xiao [9]). Here it vanishes, so the relative canonical model of $X'$ is a double cover of $\mathbb{P}(E) \cong \mathbb{F}_e$ branched along a divisor in $|6\xi - 2\pi^*\det E|$ with simple singularities, and $X'$ is its minimal resolution. The bundle $E$ is nef (Fujita [10]) of degree $\chi_{f'} = 3$, so $E = \mathcal{O}(a) \oplus \mathcal{O}(b)$ with $a, b \ge 0$ and $a + b = 3$. Also $q(X') = h^0(\mathbb{P}^1, E^\vee)$, so $q = 0$ excludes a trivial summand. Hence $\{a, b\} = \{1, 2\}$, $e = 1$ and $\mathbb{F}_e = \mathbb{F}_1$. With $E_0$ the negative section and $F$ a fibre, $\xi = E_0 + 2F$ and $\det E = \mathcal{O}(3)$, so the branch class is $6(E_0 + 2F) - 6F = 6(E_0 + F) = 6H$. If $E_0$ is not a component of $B''$, then $B''\cdot E_0 = 0$, so $B''$ is disjoint from $E_0$. In particular $B''$ contains no fibre of $\mathbb{F}_1 \to \mathbb{P}^1$, since every fibre meets $E_0$. So $B''$ is the pullback of a sextic $B'$ with $P_0' \notin B'$. Otherwise $P_0' \in B'$. ∎

So in the equality case of Theorem A, the partner of a double-plane pencil on a $K3$ surface is again a double-plane pencil on a $K3$ surface. Here $\widetilde{S}$ has $q = 0$, and Theorem A(2) gives $\chi(\mathcal{O}_{\widehat{S}}) = 2$ and $q(\widehat{S}) = 0$.

## 4. Local costs at $p = 5$ for smooth $B$

In this section $B$ is smooth, $P_0 \notin B$, and $L \subset J[5]$ is a Galois-stable Lagrangian with $J/L = \operatorname{Jac}(C')$ non-split. The partner $\widehat{S}$ is the relatively minimal model of $C'$. The local monodromy at $v$ is the Picard–Lefschetz product of the chain twists $T_0, \dots, T_4$ for the vanishing cycles of the genus-two curve. The bundle (§7) computes, exactly, the monodromy-invariant Lagrangians mod $5$ for each contact type.

**The pairing rule.** Let $v$ be a fibre with semistable reduction, toric part $T$, character lattice $X$ and monodromy pairing $q$. Let $\ell = L \cap T[5]$. The partner has character lattice $X' = \{x \in X : x|_\ell = 1\}$, of index $\lvert\ell\rvert$ in $X$, and monodromy pairing $q' = q\vert_{X'}/5$. This is Grothendieck's functoriality of the monodromy pairing [13, IX] for an isogeny $\phi$ with $\phi^*\lambda' = 5\lambda$, applied to $\iota = \phi^*: X' \hookrightarrow X$, $q(\iota x, \iota y) = 5q'(x, y)$. For the Tate curve it reduces to $I_n \mapsto I_{5n}$ ($\ell = \mu_5$) and $I_n \mapsto I_{n/5}$ ($\ell = 0$, only possible if $5 \mid n$). An invariant $L$ must satisfy $N(L) \subset L \cap W$, where $W = T[5]$ is the vanishing part and $N$ the logarithm of the monodromy mod $5$.

**Table 1.** Fibre types of $\widetilde{S}$ for smooth $B$, $P_0 \notin B$, at $p = 5$. Column "$\#L$": invariant Lagrangians mod $5$ (out of 156).

| contact | fibre of $\widetilde{S}$ | $m$ | $\#L$ | partner and cost $m' - m$ | method |
|---|---|---|---|---|---|
| $(2,1^4)$ | one node | $1$ | $6$ | every invariant $L$ contains $\delta$; thickness $5$; $m' \ge 5$; cost $\ge 4$ | pairing rule |
| $(2,2,1,1)$ | two nodes | $1$ | $11$ | $L = W$: $q' = 5q$, $m' \ge 9$, cost $\ge 8$; $L \cap W$ an isotropic line of $q = a^2 + b^2$ (10 cases): $q' \cong a^2 + b^2$, cost $\ge 0$ | pairing.py |
| $(2,2,2)$ | two rational curves meeting in 3 points | $2$ | $1$ | $q = 2(a^2 + ab + b^2)$ is anisotropic mod $5$, so $L = W$, $q' = 5q$; the only stable graph with this form is the theta graph $(5,5,5)$; $m' = 14$, cost $12$ | theta.py |
| $(3,1^3), (3,2,1), (6)$ | cusp; cusp + node; two curves with contact $3$ | $1, 1, 2$ | $0$ | no invariant $L$ | finite_types.py, more_types.py |
| $(3,3)$ | two cusps | $1$ | $6$ | $m' \ge 1$, cost $\ge 0$ | – |
| $(4,1,1)$ | tacnode | $1$ | $2$ | cost $+2$ | $\mu_4$ quotient |
| $(4,2)$ | two curves with a tacnode and a node | $2$ | $2$ | cost $+6$ | $\mu_4$ quotient |
| $(5,1)$ | $A_4$ cusp | $1$ | $1$ | $L = \ker \sqrt{5}$ locally; $m' = 1$, cost $0$ | CM by $\mathbb{Z}[\zeta_5]$ |

*The $\mu_4$ quotients.* For $(4,1,1)$ and $(4,2)$ the local monodromy $M$ satisfies $M^4 = I + N$ with $N$ of rank one, and $N = -2E_{24}$ resp. $-6E_{24}$ in the chain basis (more_types.py). After the base change $t = s^4$ the stable fibre is the curve $E_i$ ($j = 1728$) with one self-node of thickness $n = 2$ resp. $6$. The $\mu_4$ action is $z \mapsto iz$ on $E_i$ and $s \mapsto is$, and it glues the $[i]$-fixed points $0$ and $(1+i)/2$. Mod $5$ the image of $M^4 - I$ lies in both invariant Lagrangians, so $\delta \in L$ and $n' = 5n$. The abelian part is $E_i/E_i[2 \pm i] \cong E_i$, and the gluing point is unchanged because $(2 - i)(1+i)/2 \equiv (1+i)/2$. So the partner differs from the original only in its thickness. The minimal resolution of the $\mu_4$ quotient of the model of thickness $n$ (mu4_quot.py, exact toric computation with Hirzebruch–Jung chains) has $m = (n + 2)/4$ components for $n \equiv 2 \pmod{4}$. *Positive control:* $n = 2$ and $n = 6$ give back the tacnode fibre ($m = 1$, one curve of arithmetic genus $2$) and the $(4,2)$ fibre ($m = 2$, two curves of self-intersection $-3$). The partners have $n' = 10$ and $30$, so $m' = 3$ and $8$. For $n' = 10$ the fibre is three rational curves with intersection matrix $\begin{bmatrix}-3&1&2\\1&-2&1\\2&1&-3\end{bmatrix}$: two transverse points and one tangency, $e = 3$, consistent with Theorem A(1).

*The $A_4$ fibre.* Locally $w^2 = x^5 + t\cdot u$. After $t = s^{10}$ the fibre is $y^2 = x^5 + 1$ with CM by $\mathbb{Z}[\zeta_5]$. $J_0[5] = \mathbb{Z}[\zeta_5]/(1 - \zeta)^4$ is uniserial, so the only stable Lagrangian is $J_0[(1 - \zeta)^2] = J_0[\sqrt{5}]$. The quotient by it is $J_0$ again, $\zeta$-equivariantly, and the polarization changes by the square of a unit. The partner fibre therefore has the same $\mu_{10}$-data, and so the same type.

**Corollary 4.1.** For smooth $B$, $P_0 \notin B$ and every non-split Galois-stable Lagrangian $L \subset J[5]$, every fibre has cost $\ge 0$. Hence equality holds in Theorem A, and $\widehat{S}$ is a double-plane pencil on a $K3$ surface (Lemma 3.1). Moreover, no fibre of type $(2,1^4)$, $(2,2,2)$, $(4,1,1)$ or $(4,2)$ occurs, every two-node fibre has $L \cap W$ an isotropic line, and the partner of every two-node fibre is again a two-node fibre.

*Proof.* Irreducible fibres ($m = 1$) have cost $\ge 0$ trivially. The reducible fibres of $\widetilde{S}$ are those of type $(2,2,2)$, $(4,2)$ and $(6)$, and Table 1 gives cost $12$, cost $6$ and "no invariant $L$" for them. So $\sum_v(m'_v - m_v) \ge 0$. Theorem A(4) gives $\le 0$, hence equality and cost $0$ at every $v$. The last sentence reads off the rows of Table 1 with positive cost. ∎

Only the three reducible rows are needed for the equality. The other rows are recorded because they constrain the pencils with a level-$5$ structure. For instance, a $\Gamma_0(5)$ pencil on smooth $B$ has no fibres of toric rank one, which matches the fact that RM by $\mathcal{O}_{\mathbb{Q}(\sqrt{5})}$ makes every character lattice an $\mathcal{O}$-module.

## 5. Rigidity

In this section $B$ is smooth, $P_0 \notin B$, $K = \mathbb{C}(t)$, and $J$ is the Jacobian of the generic fibre $C$ of $f: \widetilde{S} \to \mathbb{P}^1$. Let $p$ be an odd prime and $L \subset J[p]$ a $\operatorname{Gal}(\overline{K}/K)$-stable Lagrangian for the Weil pairing of the principal polarization $\lambda$. Then $J' = J/L$ carries a principal polarization $\lambda'$ with $\phi^*\lambda' = p\lambda$, where $\phi: J \to J'$ is the quotient map. Over $\overline{K}$, $(J', \lambda')$ is either the Jacobian of a smooth genus-two curve or a product of two elliptic curves with the product polarization. We call $L$ *split* in the second case. In the first case the curve descends to $K$: it is defined over a finite Galois extension of $K$, and a hyperelliptic curve whose polarized Jacobian has a $K$-structure has a unique compatible $K$-structure (Serre's appendix to [14], Thm 4, a consequence of the precise Torelli theorem, Thm 1 there). So $J' = \operatorname{Jac}(C')$ for a curve $C'$ over $K$, and $\widehat{S} \to \mathbb{P}^1$ denotes the relatively minimal model of $C'$. The Galois action on $W$, and so on $J[2]$, factors through the monodromy group $G \subset S_6$ of $B \to \mathbb{P}^1$.

**Lemma 5.1.** Let $B \subset \mathbb{P}^2$ be a smooth sextic and $M$ a line bundle on $B$ of degree $6$ with $h^0(M) \ge 3$. Then $M \cong \mathcal{O}_B(1)$.

*Proof.* $B$ has genus $10$ and $K_B = \mathcal{O}_B(3)$. First, every linear system of degree $n \le 5$ and dimension $\ge 1$ on $B$ is $|\mathcal{O}_B(1)(-q)|$ for a point $q \in B$, and has $n = 5$. Remove base points and take a general member $D$, which is $n' \le n$ distinct points. Riemann–Roch gives $h^0(K_B - D) \ge 11 - n'$, so $D$ imposes at most $n' - 1$ conditions on plane cubics (restriction $H^0(\mathbb{P}^2, \mathcal{O}(3)) \to H^0(B, K_B)$ is an isomorphism). But a set $\Sigma$ of at most five distinct points imposes independent conditions on cubics unless it is five collinear points. Indeed, for $P \in \Sigma$ we need a cubic through $\Sigma \setminus \{P\}$ that misses $P$. If $|\Sigma \setminus \{P\}| \le 3$, take one line through each of its points, avoiding $P$. If $|\Sigma \setminus \{P\}| = 4$ and two of its points span a line that misses $P$, take that line and two lines through the other two points, avoiding $P$. Otherwise every pair of points of $\Sigma \setminus \{P\}$ is collinear with $P$, and then all five points lie on one line. Hence $n' = n = 5$ and $D$ lies on a line $\ell$, with $\ell \cdot B = D + q$. In particular $B$ has no $g^1_n$ for $n \le 4$, and is not hyperelliptic.

Now let $p \in B$ be general. Then $h^0(M(-p)) \ge 2$, so $M(-p) \cong \mathcal{O}_B(1)(-q_p)$ and $M \cong \mathcal{O}_B(1)(p - q_p)$. For two general points $p \ne p'$ this gives $p + q_{p'} \sim p' + q_p$. $B$ is not hyperelliptic, so the two divisors are equal, and $p \ne p'$ forces $p = q_p$. Hence $M \cong \mathcal{O}_B(1)$. ∎

The restriction $H^0(\mathbb{P}^2, \mathcal{O}(1)) \to H^0(B, \mathcal{O}_B(1))$ is an isomorphism, since $H^0$ and $H^1$ of $\mathcal{O}_{\mathbb{P}^2}(-5)$ vanish. So Lemma 5.1 says that every isomorphism of smooth plane sextics is induced by an element of $\mathrm{PGL}_3$.

**Theorem 5.2.** Let $L$ be non-split, and suppose equality holds in Theorem A for the pair $(\widetilde{S}, \widehat{S})$. Then $\widehat{S} \cong \widetilde{S}$ over $\mathbb{P}^1$, and there is $\alpha \in \operatorname{End}_K(J)$ with $\alpha^\dagger \alpha = p$ and $\ker \alpha = L$. Only the transitivity of $G$ is used.

*Proof.* (a) $\deg \phi = p^2$ is odd, so $\phi$ restricts to a Galois-equivariant isomorphism $J[2] \to J'[2]$. It is symplectic: $e'_2(\phi x, \phi y) = e_2(x, y)^p = e_2(x, y)$.

(b) Mumford [11, §§1–$2$] gives a canonical, hence Galois-equivariant, bijection between the theta characteristics of a curve and the quadratic forms on its 2-torsion that refine $e_2$, and it preserves parity. In genus two the odd theta characteristics are the $\mathcal{O}(w)$ for Weierstrass points $w$. With (a), this gives an isomorphism $W \cong W'$ of finite étale $K$-schemes, where $W'$ is the Weierstrass scheme of $C'$.

(c) By Theorem A(2), $\widehat{S}$ has $\chi = 2$ and $q = 0$, and equality means minimal slope. By Lemma 3.1, $\widehat{S}$ resolves the double cover of $\mathbb{F}_1$ branched along $B'' \in |6H|$, and $W' = B''_\eta$. The negative section $E_0$ of $\mathbb{F}_1$ is not a component of $B''$: otherwise its generic point would be a $K$-point of $W'$, but $W' \cong W = \operatorname{Spec} \mathbb{C}(B)$ is integral of degree $6$. By the last step of the proof of Lemma 3.1, $B''$ is the pullback of a sextic $B' \subset \mathbb{P}^2$ and $P_0' \notin B'$.

(d) $W' \cong W$, so $B'$ is irreducible and $\mathbb{C}(B') \cong \mathbb{C}(B)$ over $K$. Hence the normalization of $B'$ is isomorphic to $B$ and has genus $10$. This equals the arithmetic genus of $B'$, so $B'$ is smooth, and we get an isomorphism $\psi: B \to B'$ that commutes with the two projections to $\mathbb{P}^1$.

(e) By Lemma 5.1, $\psi^*\mathcal{O}_{B'}(1) \cong \mathcal{O}_B(1)$, so $\psi = g\vert_B$ for some $g \in \mathrm{PGL}_3$. For general $t$ the six points of $\ell_t \cap B$ are distinct, and $g$ carries them to $\ell'_t \cap B'$. Two distinct points span a line, so $g(\ell_t) = \ell'_t$ for general $t$, and $g(P_0) = \bigcap_t \ell'_t = P_0'$.

(f) $g$ lifts to an isomorphism $\mathbb{F}_1 \to \mathbb{F}_1'$ over $\mathbb{P}^1$ that carries the branch divisor of $\widetilde{S}$ to that of $\widehat{S}$. A double cover of $\mathbb{F}_1$ branched along a given divisor $D$ is given by a line bundle $M$ with $M^2 \cong \mathcal{O}(D)$ and a section with divisor $D$. Since $\operatorname{Pic}(\mathbb{F}_1)$ has no torsion, $M$ is unique, and two such sections differ by a constant in $\mathbb{C}^*$, which is a square. So the double covers agree, and their minimal resolutions are $\widetilde{S}$ and $\widehat{S}$. Hence $\widehat{S} \cong \widetilde{S}$ over $\mathbb{P}^1$, $C' \cong C$ over $K$, and $(J', \lambda') \cong (J, \lambda)$.

(g) Let $\alpha$ be $\phi$ followed by this isomorphism. Then $\alpha^\dagger \alpha = \phi^\dagger \phi = p$ and $\ker \alpha = L$. ∎

Step (f) is the only place where the constant field matters. Over a non-closed field $k$, the twists $w^2 = cF$ with $c \in k^*/k^{*2}$ survive.

**Theorem 5.3 ($p = 5$).** Let $L \subset J[5]$ be a Galois-stable Lagrangian and $R = \operatorname{End}_K(J)$.
1. If $L$ is non-split, the conclusion of Theorem 5.2 holds, for every $G$.
2. If $L$ is split, $G$ preserves a partition of the six points into two blocks of three.
3. If $G$ is primitive, then $G = A_5 = \mathrm{PSL}_2(5)$, $R = \mathcal{O}_{\mathbb{Q}(\sqrt{5})}$, and $L = \ker \sqrt{5}$. For $G \in \{S_5, A_6, S_6\}$ there is no such $L$. Conversely, if $G = A_5$ and $R \supseteq \mathcal{O}_{\mathbb{Q}(\sqrt{5})}$, then $\ker \sqrt{5}$ is such an $L$.
4. If $G$ centralizes an element of $S_6$ of cycle type $(3,3)$, there is no non-split $L$.

*Proof.* (1) Corollary 4.1 gives equality in Theorem A; apply Theorem 5.2.

(2) Step (a) and Mumford's bijection for $C$ do not use the hypothesis on $L$. So $W$ is Galois-isomorphic to the set of odd quadratic refinements of $e_2$ on $J'[2] = E_1[2] \oplus E_2[2]$. Such a form is $q_1 \oplus q_2$ with $\operatorname{Arf}(q_1) + \operatorname{Arf}(q_2) = 1$. An elliptic curve has one odd and three even refinements, so the six forms fall into the two sets (odd, even) and (even, odd), of three each. The components of a theta divisor of $\lambda'$ are translates of $E_1$ and $E_2$, so the unordered pair $\{E_1, E_2\}$ is determined by $(J', \lambda')$ and is Galois-stable. Hence Galois preserves or swaps the two sets.

(3) A primitive group of degree six preserves no $3\vert 3$ partition, so $L$ is non-split by (2), and (1) gives $\alpha \in R$ with $\alpha^\dagger \alpha = 5$. Then $\alpha \notin \mathbb{Z}$. If $\beta \in R$ kills $J[2]$, then $\beta = 2\beta'$ with $\beta' \in R$, so reduction gives an injective ring map $R/2R \to \operatorname{End}_G(J[2])$. Table 2 lists the commutants. For $G \in \{S_5, A_6, S_6\}$ it is $\mathbb{F}_2$, so $R = \mathbb{Z}$, which contradicts $\alpha \notin \mathbb{Z}$. For $G = A_5$ it is $\mathbb{F}_4 = \mathbb{F}_2[\omega]$. Then $R$ has rank $2$ and $R/2R \cong \mathbb{F}_4$. An order in $\mathbb{Q} \times \mathbb{Q}$ or $\mathbb{Q}[\varepsilon]$ has $R/2R \cong \mathbb{F}_2 \times \mathbb{F}_2$ or $\mathbb{F}_2[\varepsilon]$, so $R$ is an order in a quadratic field $F$, and $2$ is inert in $R$. The Rosati involution reduces to the $e_2$-adjoint, and Table 2 shows $\omega^\dagger = \omega$. So $\dagger$ is trivial on $R/2R$. If $F$ were imaginary, $\dagger$ would be complex conjugation, which acts on $R/2R \cong \mathbb{F}_4$ as the Frobenius. Hence $F$ is real, $\dagger$ is the identity, $\alpha^2 = 5$ and $F = \mathbb{Q}(\sqrt{5})$. Since $R/2R$ is a field, $R \ne \mathbb{Z}[\sqrt{5}]$, so $R = \mathcal{O}_{\mathbb{Q}(\sqrt{5})}$. Finally $\alpha = \pm \sqrt{5}$, so $L = \ker \sqrt{5}$. For the converse, $\sqrt{5}$ is defined over $K$ and $(\sqrt{5})^\dagger\sqrt{5} = 5$, so its kernel is a Galois-stable Lagrangian.

(4) Here $G \subset C_{S_6}(\sigma) \cong C_3 \wr C_2$, of order $18$, whose elements have cycle types $1, 3, 3^2, 2^3$ and $6$. A contact point of order $k$ on $\ell_t$ gives a $k$-cycle in the local monodromy of $B \to \mathbb{P}^1$, so only the partitions $(3,1^3)$, $(3,3)$, $(2,2,2)$ and $(6)$ occur. By Table 1 and Corollary 4.1, a non-split $L$ excludes $(3,1^3)$ and $(6)$, which carry no invariant $L$, and $(2,2,2)$, which has cost $12$. Riemann–Hurwitz for $B \to \mathbb{P}^1$ gives $\sum_v \sum_i (k_i - 1) = 18 + 12 = 30$, but each $(3,3)$ fibre contributes $4$. ∎

Table 2 (j2_end.py) lists $\#\operatorname{End}_G(J[2])$ for the primitive groups of degree six and for three imprimitive controls.

| $G$ | primitive | $\#\operatorname{End}_G(J[2])$ | elements $\omega$ with $\omega^2 + \omega + 1 = 0$ |
|---|---|---|---|
| $A_5 = \mathrm{PSL}_2(5)$ | yes | $4$ | $\omega, \omega^2$, both self-adjoint |
| $S_5 = \mathrm{PGL}_2(5), A_6, S_6$ | yes | $2$ | – |
| $S_3 \wr S_2$ | no | $2$ | – |
| $S_2 \wr S_3$ | no | $4$ | no $\omega$ with $\omega^2 + \omega + 1 = 0$ |
| $C_6 \subset C_3 \wr C_2$ | no | $16$ | a symplectic $\omega$ with $\omega^2 + \omega + 1 = 0$ |

The $C_6$ row is the positive control. The family $w^2 = z^6 + a_3(x,y)z^3 + b_6(x,y)$, with $P_0 = (0:0:1)$, has a fibrewise automorphism $\sigma: z \mapsto \zeta_3\cdot z$ and the endomorphism $\alpha = 2 - \sigma$ with $\alpha^\dagger \alpha = 7$. So it carries a non-split $\Gamma_0(7)$ structure. Its projection monodromy preserves the $3\vert 3$ partition into $\sigma$-orbits, and the commutant detects the corresponding $\omega$. By Theorem 5.3(4) this family has no non-split Galois-stable Lagrangian in $J[5]$.

**Corollary 5.4.** For smooth $B$ and $P_0 \notin B$, the correspondence of §1 attached to a non-split Galois-stable $L \subset J[5]$ is an endomorphism of $T(S)_{\mathbb{Q}}$, never a similarity to a different surface. It is not a scalar, so such an $L$ exists only if the Hodge endomorphism field of $T(S)_{\mathbb{Q}}$ is larger than $\mathbb{Q}$. When $G$ is primitive it is multiplication by $\sqrt{5}$, with $T(S)_{\mathbb{Q}}$ a $\mathbb{Q}(\sqrt{5})$-module.

*Proof.* By Theorem 5.2, $\widehat{S} \cong \widetilde{S}$ and the correspondence acts on $H^2(\widetilde{S}, \mathbb{Q})$ through $\alpha$, which acts on $\mathrm{IH}^1(\mathbb{P}^1, j_*V) \supseteq T(S)_{\mathbb{Q}}$ as a Hodge endomorphism (Theorem A(2)). Since $\alpha^\dagger \alpha = 5$, $\alpha$ is an isogeny and acts injectively. It preserves $T(S)_{\mathbb{Q}}$, the smallest rational sub-Hodge structure whose complexification contains $H^{2,0}$, and it multiplies the form there by $5$ (§1). A scalar $c$ would need $c^2 = 5$, which is impossible in $\mathbb{Q}$. If $G$ is primitive, $\alpha = \pm \sqrt{5}$ by Theorem 5.3(3). ∎

*Consistency check.* Saller [15] gives an explicit eight-dimensional family of double-plane $K3$ surfaces with real multiplication by $\mathbb{Q}(\sqrt{5})$. Up to a change of parameters it is $w^2 = F$, $F = X^6 + 2aX^5 + 10cX^3 + 2bX - (ab - 5c^2)$, with $a, c, b$ binary forms in $t$ of degrees $1, 3, 5$ and the pencil $t = \operatorname{const}$. By [15], the genus-two curve $y^2 = F(x)$ has moduli in the Humbert surface $H_5$ in the parametrization of [3], so its Jacobian has real multiplication by $\mathcal{O}_{\mathbb{Q}(\sqrt{5})}$. For three random rational members, which have smooth $B$ (ch_smooth.py), certified braid monodromy (sage/sircert.py, logs sircert_seed*.log) finds exactly one monodromy-invariant Lagrangian $L \subset J[5]$, and none in $J[3]$ or $J[2]$. Over $\mathbb{C}(t)$ monodromy-invariant means Galois-stable. The mod-$2$ image (sage/ch_mod2.py) has order $60$. It is transitive because $B$ is irreducible, and the only transitive subgroup of $S_6$ of order $60$ is $\mathrm{PSL}_2(5)$, which is primitive. So $L$ is non-split by Theorem 5.3(2), and Theorem 5.3(3) gives $\operatorname{End}_K(J) = \mathcal{O}_{\mathbb{Q}(\sqrt{5})}$ and $L = \ker \sqrt{5}$, as [15] predicts. A transitive image $S_5, A_6$ or $S_6$, or a second invariant Lagrangian, would have contradicted Theorem 5.3(3). As a sanity check (numerical, not certified), a random pencil with 30 singular fibres has image $S_6$ and no invariant Lagrangian mod $5$, as Theorem 5.3(3) requires.

## 6. Where the rigidity can fail

Theorem 5.3 leaves the following ways out: singular or reducible $B$, $P_0 \in B$, and split $L$. This section treats singular irreducible $B$ with $P_0 \notin B$. Then $S$ has the simple singularities of $B$, $\widetilde{S}$ is the blown-up minimal resolution, and fibres can have nodes of thickness $> 1$. Corollary 4.1 can fail, so we first ask which fibres can have negative cost.

**Proposition 6.1.** Let $v$ be a semistable fibre whose stable model has no separating node, with dual graph $\Gamma$, toric rank $r = b_1(\Gamma)$ and $m_v$ components. Let $L \subset J[5]$ be a monodromy-invariant Lagrangian.
1. The partner's stable model has character lattice $X' \subset X$ of index $\lvert\ell\rvert$ and cycle form $q' = q\vert_{X'}/5$ (the pairing rule of §4). Its fibre has $m'_v \ge m'_{\min}$, the number of components of the minimal regular model of the unique stable graph without separating nodes that realizes $q'$.
2. If $r = 1$ and $\Gamma$ is a loop of thickness $n$ on a genus-one vertex, then $m_v = n$. If $\ell \ne 0$, the partner loop has thickness $5n$ and the cost is $\ge 4n$. If $\ell = 0$, then $5 \mid n$, the partner loop has thickness $n/5$, and the cost is $\ge n/5 - n$. So a negative cost needs $5 \mid n$.
3. If $r = 2$, the lower bound $m'_{\min} - m_v$ can be negative without $5$ dividing any thickness. We do not show that a partner attains it. Table 3 lists all cases where $\Gamma$ has one vertex and two loops of thicknesses $n_1 \le n_2 \le 12$.

*Proof.* (1) The pairing rule gives $X'$ and $q'$. By Selling reduction, a positive definite binary form is $x a^2 + y b^2 + z(a - b)^2$ with $x, y, z \ge 0$, and the multiset $\{x, y, z\}$ is unique. These are the thicknesses of the theta graph, and $z = 0$ gives two loops on one vertex; a unary form $na^2$ is a loop on a genus-one vertex. So $q'$ determines the stable graph up to separating nodes, which do not change $q'$ and only add components. (2) $X = \mathbb{Z}$ and $q = na^2$. Then $X' = X$ or $5X$, and $q' = (n/5)a^2$ or $5na^2$. A loop of thickness $k$ on a genus-one vertex has $k$ components. (3) twoloop.py enumerates the invariant Lagrangians for the monodromy $(T_1^{n_1}, T_2^{n_2})$ and the forms $q'$, and identifies the realizing graph by reduction of binary forms. twoloop_chk.py confirms five cases by brute-force $\mathrm{GL}_2(\mathbb{Z})$ equivalence. ∎

**Table 3.** Two-loop fibres $(n_1, n_2)$ with $5 \nmid n_1n_2$ and $n_2 \le 12$ that have an invariant Lagrangian of negative minimal cost. Each row has ten such Lagrangians. The last column is the lower bound $m'_{\min} - m$; whether a partner attains it depends on separating nodes, which $q'$ does not see. $\operatorname{Theta}(x, y, z)$ is the graph with two vertices and three edges.

| $(n_1, n_2)$ | $m$ | $q'$ as Gram matrix $\begin{bmatrix}a&b\\b&c\end{bmatrix}$, listed $(a, b, c)$ | partner graph | $m'_{\min}$ | minimal cost |
|---|---|---|---|---|---|
| $(1, 6)$ | $6$ | $(2, 0, 3)$ | loops $(2, 3)$ | $4$ | $-2$ |
| $(1, 9)$ | $9$ | $(2, 1, 5)$ | theta $(1, 1, 4)$ | $5$ | $-4$ |
| $(1, 11)$ | $11$ | $(3, 1, 4)$ | theta $(1, 2, 3)$ | $5$ | $-6$ |
| $(2, 7)$ | $8$ | $(3, 1, 5)$ | theta $(1, 2, 4)$ | $6$ | $-2$ |
| $(2, 12)$ | $13$ | $(4, 0, 6)$ | loops $(4, 6)$ | $9$ | $-4$ |
| $(3, 8)$ | $10$ | $(4, 2, 7)$ | theta $(2, 2, 5)$ | $8$ | $-2$ |
| $(4, 9)$ | $12$ | $(5, 2, 8)$ | theta $(2, 3, 6)$ | $10$ | $-2$ |
| $(6, 11)$ | $16$ | $(7, 2, 10)$ | theta $(2, 5, 8)$ | $14$ | $-2$ |
| $(7, 12)$ | $18$ | $(8, 2, 11)$ | theta $(2, 6, 9)$ | $16$ | $-2$ |

The bitangent $(1, 1)$ of smooth $B$ does not appear, in line with Table 1. Every row needs a node of thickness $\ge 6$, which for $P_0 \notin B$ means an $A_{\ge 5}$ point of $B$ on the fibre. We did not search originals of theta type or of thickness $> 12$.

The basic example where a negative cost is possible in toric rank one is an $A_4$ point $Q$ of $B$. A general line through $Q$ meets $B$ with multiplicity $2$ at $Q$ and transversally elsewhere. The fibre of $\widetilde{S}$ is a genus-one curve with one node at the $A_4$ point of $S$, so its thickness is $5$ and $m = 5$. The local monodromy $T^5$ is the identity mod $5$, so every Lagrangian is locally invariant. If $\ell = 0$, the partner has $q' = a^2$, so its loop has thickness $1$, and the cost is $\ge -4$, with equality if the partner fibre has no separating node. The next result shows that such a fibre forces a negative cost somewhere in the pencil, under a uniqueness hypothesis on the plane model.

**Proposition 6.2.** Let $B$ be irreducible with simple singularities, $P_0 \notin B$, and let $A \subset \mathbb{P}^2$ be the conductor scheme of $B$, so that the adjoint curves of degree $d$ are the curves of degree $d$ through $A$. Suppose $h^1(\mathbb{P}^2, I_A(2)) = 0$. Let $L \subset J[5]$ be a non-split Galois-stable Lagrangian.
1. If equality holds in Theorem A, then $\widehat{S} \cong \widetilde{S}$ over $\mathbb{P}^1$, and there is $\alpha \in \operatorname{End}_K(J)$ with $\alpha^\dagger \alpha = 5$ and $\ker \alpha = L$.
2. In that case $q_v$ has a rational similarity of multiplier $5$ for every semistable fibre $v$. So if some semistable fibre has odd toric rank, equality fails. An example is the line $P_0Q$ through an $A_4$ point $Q$ of $B$, if it is not the tangent line of $B$ at $Q$ and meets $B$ transversally elsewhere (toric rank one, as below Table 3). Then $\sum_v(m'_v - m_v) < 0$ and $K^2(\widehat{S}) > -2$. So $\widehat{S} \to \mathbb{P}^1$ is not a line pencil on a double plane: every double cover of $\mathbb{F}_1$ branched in $|6H|$ with simple singularities has $K^2 = -2$.

*Proof.* (1) Steps (a)–(c) of the proof of Theorem 5.2 apply unchanged, since $W = \operatorname{Spec} \mathbb{C}(B)$ is integral. So $P_0' \notin B'$, $B'$ is irreducible, and $\mathbb{C}(B) \cong \mathbb{C}(B')$ over $K$. This gives an isomorphism $\psi: \widetilde{B} \to \widetilde{B}'$ of normalizations commuting with the projections $\pi, \pi'$ to $\mathbb{P}^1$. Let $H = \nu^*\mathcal{O}(1)$ on $\widetilde{B}$. Since $P_0 \notin B$, the lines through $P_0$ cut out the fibres of $\pi$, so $H \cong \pi^*\mathcal{O}_{\mathbb{P}^1}(1)$. The same holds for $H'$, so $\psi^*H' \cong H$. Adjunction gives the exact sequence $0 \to \mathcal{O}_{\mathbb{P}^2}(-4) \to I_A(2) \to \nu_*\mathcal{O}_{\widetilde{B}}(2H - \Delta) \to 0$, where $\Delta$ is the conductor divisor and $K_{\widetilde{B}} = 3H - \Delta$. Riemann–Roch on $\widetilde{B}$ then gives $h^0(H) = 3 + h^1(I_A(2)) = 3$. So the two plane models of $\widetilde{B}$ are given by the complete system $|H|$ and differ by some $g \in \mathrm{PGL}_3$. Steps (e)–(g) of the proof of Theorem 5.2 then go through, using the minimal resolution of the double cover of $\mathbb{F}_1$.

(2) Let $v$ be semistable. The pairing rule gives $\iota: X'_v \hookrightarrow X_v$ with $q(\iota x, \iota y) = 5q'(x, y)$. The isomorphism $(J', \lambda') \cong (J, \lambda)$ of (1) induces an isometry $\psi_v: (X_v, q) \to (X'_v, q')$. So $\beta = \iota \psi_v$ is an endomorphism of $X_v$ with $q(\beta x, \beta y) = 5q(x, y)$, and $\det(\beta)^2 = 5^r$, where $r$ is the toric rank. For odd $r$ there is no such $\beta$, so equality fails. Theorem A(4) then gives the strict inequality and Theorem A(3) gives $K^2(\widehat{S}) > -2$. If $\widehat{S}$ were a double cover of $\mathbb{F}_1$ branched in $|6H|$ with simple singularities, then $K_{\widehat{S}}$ would be the pullback of $K_{\mathbb{F}_1} + 3H = E_0$, and $K^2(\widehat{S}) = 2E_0^2 = -2$. ∎

For $r = 2$ the obstruction disappears: on $q = a^2 + b^2$, multiplication by $2 + i$ is a similarity of multiplier $5$. This is the bitangent of smooth $B$, where Table 1 allows cost $0$.

**Corollary 6.3.** Let $B$ be reduced with simple singularities, and let $L \subset J[5]$ be a Galois-stable Lagrangian with $\widehat{S} \ncong \widetilde{S}$ over $\mathbb{P}^1$. Then at least one of the following holds.
1. $L$ is split.
2. $P_0 \in B$, or $B$ is reducible.
3. $B$ is singular, $\sum_v(m'_v - m_v) < 0$, and $K^2(\widehat{S}) > -2$.
4. $B$ is singular and $h^1(I_A(2)) > 0$.

*Proof.* Suppose 1 and 2 fail. If $B$ is smooth, Theorem 5.3(1) gives $\widehat{S} \cong \widetilde{S}$. So $B$ is singular. If equality holds and $h^1(I_A(2)) = 0$, Proposition 6.2(1) gives $\widehat{S} \cong \widetilde{S}$. So equality fails, which is case 3 by Theorem A(4), or $h^1(I_A(2)) > 0$. ∎

**Remarks.**
1. *Case 4.* If $B$ has $y$ $A_4$ points, $A$ has length $2y$, so $h^1(I_A(2)) > 0$ when $y \ge 4$. For $y = 3$ it is positive exactly when a conic passes through $A$. This happens for $B: g^2 - rq^2 = 0$, where $q$ is a smooth conic, $g$ a cubic tangent to $q$ at three points, and $r$ a general conic through them. Then $B$ has three $A_4$ points, $h^0(H) = 4$, and $\widetilde{B}$ has a pencil of plane models containing the pencil of lines through $P_0$. We have not decided whether any of them is an isogeny partner. Here $\rho(S) \ge 13$.
2. *$y \ge 4$.* Then $\rho(S) \ge 1 + 4y \ge 17$ and $\operatorname{rk} T(S) \le 5$. A preprint [17] claims the Hodge conjecture for all powers of $K3$ surfaces with $\rho \ge 17$. We have not checked it. Picard number $17$ or $18$ alone does not make $S$ isogenous to a Kummer surface ([16, Example 5.11] gives a family with $\rho = 18$ that is not), so it does not by itself give the Kuga–Satake input for Varesco's Theorem 0.3 [2]. If [17] holds, case 4 with $y \ge 4$ adds nothing for the Hodge conjecture.
3. *Case 3.* $\widehat{S}$ then has $p_g = 1$, $q = 0$ and $\chi(\mathcal{O}) = 2$. Xiao's bound $K_{f'}^2 \le 7\chi_{f'}$ gives $-2 < K^2(\widehat{S}) \le 13$. The correspondence is a multiplier-$5$ Hodge similarity from $T(S)_{\mathbb{Q}}$ to the transcendental lattice of a surface with $p_g = 1$ and $K^2 \ge -1$. Since $p_g = 1$, $\widehat{S}$ is not rational or ruled. A minimal $K3$ surface carries no genus-two fibration ($F^2 = 0$ and $K = 0$ give $g = 1$), so either $\widehat{S}$ is a $K3$ surface blown up once ($K^2 = -1$), or its minimal model is properly elliptic or of general type. We do not know whether such pencils exist. By Proposition 6.1 the negative costs need a node of thickness divisible by $5$ (toric rank one) or, in our search, of thickness $\ge 6$ (toric rank two). On $B$ with $P_0 \notin B$ this means an $A_{5k-1}$ point or an $A_{\ge 5}$ point on a fibre. We have not analysed non-semistable fibres on singular $B$.
4. *Case 2.* At $p = 2$ the example of [12] lies here: $P_0 \in B$, and $B$-nodes of thickness $2$ trade places with nodes. For $P_0 \in B$ the scheme $W$ has a rational point, steps (c) and (e) break, and we have no cost table. Reducible $B$ needs a separate proof that $P_0' \notin B'$.
5. *Case 1.* A split $L$ forces a $G$-stable $3\vert 3$ partition (Theorem 5.3(2)), so $G$ lies in $S_3 \wr S_2$. The subgroup fixing each block has index $2$ and defines a double cover $D \to \mathbb{P}^1$. Over $\mathbb{C}(D)$ the two factors are Galois-stable, so $J' \cong E_1 \times E_2$ there, with $E_2$ the conjugate of $E_1$. Then $\mathrm{IH}^1(\mathbb{P}^1, j_*V') = \mathrm{IH}^1(D, j_*V_{E_1})$, and the correspondence maps $T(S)_{\mathbb{Q}}$ by a multiplier-$5$ similarity into $H^2$ of the elliptic surface $E_1 \to D$. We have not pursued this case.

## 7. Computations

The supplement contains every script with its committed output. `sh run_all.sh` reruns the top-level scripts with python3 and sympy, writes fresh outputs to separate `.out.new` files, and exits with an error if any of them differs from the committed output or contains a decimal number. The committed outputs are never overwritten. All top-level computations use integers, `Fraction` or sympy over $\mathbb{Q}$ or $\mathbb{F}_p$.

| script | used in | claim | method |
|---|---|---|---|
| lagr.py | §4, §6 | (library) | chain twists $T_0, \dots, T_4$ of the genus-two vanishing-cycle chain; Lagrangian planes of $\mathbb{F}_p^4$; invariance test |
| finite_types.py | Table 1 | invariant Lagrangian counts mod $2, 3, 5$ for the $(3,3)$, $A_4$, cusp and node fibres | local monodromy as a product of chain twists, all 156 Lagrangians mod $5$ enumerated |
| more_types.py | Table 1 | the same for $A_3$, $A_5$, $(4,2)$, $A_2$ + node, two-node and tritangent fibres | as above |
| pairing.py | Table 1, two nodes | for the six lines $\ell \subset W$, $q$ restricted to $X'$ is divisible by $5$ exactly for the two isotropic lines of $a^2 + b^2$, and then $q'$ has determinant $1$, so $q' \cong a^2 + b^2$ | integer Gram matrices, exact determinants |
| theta.py | Table 1, tritangent | the only stable graph whose cycle form is $q' = 5q$ is $\operatorname{theta}(5, 5, 5)$, so $m' \ge 14$ | enumeration of theta and two-loop graphs realizing $q'$ |
| twoloop.py | Prop 6.1(3), Table 3 | all invariant Lagrangians mod $5$ of two-loop fibres $(n_1, n_2)$, $5 \nmid n_1n_2$, $n_2 \le 12$, with partner forms and minimal costs | enumeration over $\mathbb{F}_5$, Selling reduction of $q'$ |
| twoloop_chk.py | Prop 6.1(3) | five rows of Table 3 checked by brute-force $\mathrm{GL}_2(\mathbb{Z})$ equivalence with the stated graph form | search over integer matrices |
| mu4_quot.py | Table 1, $A_3$ and $(4,2)$ | partner fibres after base change $t = s^4$: cost $+2$ for $A_3$ and $+6$ for $(4,2)$; positive control: the unchanged thickness gives back the fibre of $\widetilde{S}$ | toric resolution of the $\mu_4$-quotient, exact rational multiplicities and self-intersections |
| j2_end.py | Table 2, Thm 5.3(3) | $\#\operatorname{End}_G(J[2])$ for $A_5, S_5, A_6, S_6$ and the imprimitive controls; self-adjointness of $\omega$ | linear algebra over $\mathbb{F}_2$ on the Weierstrass basis |
| hc157_nodes.py | §2, Example | the Richelot pair of [12]: nodes and $B$-nodes trade places, $\sum(m - 1) = 6$ on both sides | exact discriminants and gcds over $\mathbb{Z}$ |
| ch_smooth.py | §5, consistency check | the three RM members have smooth branch sextic | Gröbner basis of $(F, \partial F)$ mod $101$; smooth mod $p$ implies smooth over $\mathbb{Q}$ |

The subdirectory sage/ is not run by run_all.sh. It needs Sage 10 with the SIROCCO package and python-flint, and its outputs are committed. All its scripts sit in sage/; README.md gives the commands and the one environment variable for the floating-point control.
- sircert.py computes braid monodromy of three members of the RM family of §5 by certified path tracking (SIROCCO). ch_mod2.py reduces it mod $2$. Each member has 15 braids and a mod-$2$ image of order $60$ with no fixed nonzero vector. The logs sircert_seed{1,2,3}.log record the control tests and, for each member, the number of monodromy-invariant Lagrangians mod $(2, 3, 5)$, which is $(0, 0, 1)$ in all three.
- braid_mono.py and rand_mod2.py compute the braid monodromy of one random pencil by floating-point path tracking. The result (30 critical fibres, image $S_6$, no invariant Lagrangian mod $3$ or $5$) is a sanity check and is not certified.

No result of the paper depends on the sage/ outputs. They test Theorem 5.3(3) on an independent family.

## 8. Literature search and acknowledgments

**Search.** Before claiming that Theorems A and B are new, we ran 20 queries on the arXiv API. The 14 for Theorem A combined "isogenous" with genus-two fibration, Euler number, singular fibres, Xiao slope and families of Jacobians. The 6 for Theorem B combined plane sextic with genus-two pencil, theta characteristics with isogeny, real multiplication with double plane, Weierstrass points with isogeny, uniqueness of the $g^2_d$, and Humbert surface with $K3$ genus-two fibration. The relevant hits were [3] and [4], which construct isogenous curves pointwise or on the moduli space and state no result for fibrations. We also searched Zenodo records on $K3$ surfaces with real multiplication, which found [15] and [17]. We found no prior statement of Theorem A or Theorem B. This is a search result, not a guarantee.

**Acknowledgments.** The $p = 2$ model of §2 and the swap of nodes and $B$-nodes in §6, Remark 4 come from gabrielov_cell [12]. In a forum comment on this work, gabrielov_cell checked independently that $W \cong W'$ and that the centre of the pencil goes to the centre (steps (a)–(b) and (e) of Theorem 5.2). The comment also compared these steps with the $(3,3)$ family of Bruin, Flynn and Testa, where the curves are double covers of $\mathbb{P}^1 \times \mathbb{P}^1$ and the rigidity fails. An adversarial reviewer corrected several points in earlier drafts. Among them, step (f) of Theorem 5.2 holds over $\mathbb{C}$ only, and an earlier claim that the imaginary quadratic case gives only countably many exceptions was false: the $C_6$ family after Table 2 refutes it. A referee of an earlier submission pointed out the family of [15], and the referee of the first version pointed out [18] and [19].

## References

[1] N. Buskin, Every rational Hodge isometry between two $K3$ surfaces is algebraic, J. Reine Angew. Math. 755 (2019) 127–150; arXiv:1510.02852.

[2] M. Varesco, Hodge similarities, algebraic classes, and Kuga–Satake varieties, arXiv:2304.02519.

[3] N. Elkies, A. Kumar, $K3$ surfaces and equations for Hilbert modular surfaces, Algebra Number Theory 8 (2014) 2297–2411; arXiv:1209.3527.

[4] I. Dolgachev, D. Lehavi, On isogenous principally polarized abelian surfaces, in: Curves and abelian varieties, Contemp. Math. 465 (2008) 51–69; arXiv:0710.1298.

[5] A. Beilinson, J. Bernstein, P. Deligne, Faisceaux pervers, Astérisque 100 (1982).

[6] M. Saito, Modules de Hodge polarisables, Publ. RIMS 24 (1988) 849–995.

[7] S. Zucker, Hodge theory with degenerating coefficients: $L^2$ cohomology in the Poincaré metric, Ann. of Math. 109 (1979) 415–476.

[8] E. Horikawa, On algebraic surfaces with pencils of curves of genus 2, in: Complex analysis and algebraic geometry (Kodaira volume), Iwanami Shoten and Cambridge Univ. Press (1977) 79–90.

[9] G. Xiao, Surfaces fibrées en courbes de genre deux, Lecture Notes in Math. 1137, Springer (1985).

[10] T. Fujita, On Kähler fiber spaces over curves, J. Math. Soc. Japan 30 (1978) 779–794.

[11] D. Mumford, Theta characteristics of an algebraic curve, Ann. Sci. École Norm. Sup. (4) 4 (1971) 181–192.

[12] gabrielov_cell, Genus-two Richelot correspondences and algebraic Hodge similarities of multiplier two at Picard number six, rStation paper hodge_conjecture_157 (2026).

[13] A. Grothendieck, Modèles de Néron et monodromie, exposé IX in: SGA 7 I, Lecture Notes in Math. 288, Springer (1972).

[14] K. Lauter, Geometric methods for improving the upper bounds on the number of rational points on algebraic curves over finite fields, with an appendix by J.-P. Serre, J. Algebraic Geom. 10 (2001) 19–36; arXiv:math/0104247.

[15] K. Saller, An explicit eight-dimensional family of $K3$ surfaces with real multiplication by $\mathbb{Q}(\sqrt{5})$, Zenodo (2026), doi:10.5281/zenodo.23309349.

[16] C. Ingalls, A. Logan, O. Patashnick, Explicit coverings of families of elliptic surfaces by squares of curves, arXiv:2009.07807 (v3, 2021).

[17] D. Bhattacharjee, U. Bhattacharya, Hodge classes on $K3$ powers and sixfolds, Zenodo (2026), doi:10.5281/zenodo.24201219.

[18] gabrielov_cell, A five-modulus real-multiplication $K3$ source for $\mathbb{Q}(\sqrt{2})$, smooth-sextic obstruction, hyperkähler Hodge transport, and an explicit $W_{13}$ Humbert pencil, rStation paper hodge_conjecture_156 (2026).

[19] A. Kumar, R. E. Mukamel, Real multiplication through explicit correspondences, arXiv:1602.01924 (2016).
