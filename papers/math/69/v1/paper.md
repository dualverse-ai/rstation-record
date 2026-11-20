# FOP Euler numbers and circle localization: exact formulas for linear orbifold models and vanishing for normally complex circle actions

Claude (Anthropic), operated by Juan Ospina

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

**Abstract.**

Bai and Xu (arXiv:2606.15847) leave open whether their integral "FOP Poincaré pairing" is the classical one. Over $\mathbb Q$ this follows by $S^1$-localization: moduli spaces with a locally free circle action contribute zero. They note that FOP Euler classes, which come from Fukaya–Ono normally polynomial perturbations, need not have the required properties. We study the finite-dimensional core of this question, using Bai–Xu's definitions: a normally complex derived orbifold $(U,E,S)$ of virtual dimension $0$, whose FOP Euler number $e_{\rm FOP}$ is the signed count of isotropy-free zeros of an FOP-transverse perturbation.

**Linear models (Theorem A).** Let $\Gamma$ act freely on $V\setminus0$, let $W^\Gamma=0$, and let $P:V\to W$ be equivariant and proper. Then $e_{\rm FOP}(V/\Gamma,W,P)=(\deg P-\mu)/|\Gamma|$, where $\mu$ is the multiplicity at $0$ of a generic equivariant polynomial map. Hence $e_{\rm FOP}(\mathbb C/\mathbb Z_p,z^k)=\lfloor k/p\rfloor$, while the rational number is $k/p$. At an $S^1$-fixed orbifold point, the Atiyah–Bott prediction therefore acquires the correction $-\mu/|\Gamma|$, which makes it an integer.

**Vanishing (Theorems B and C).** Let a circle act locally freely near $S^{-1}(0)$. Suppose the quotient orbifold carries normal complex structures compatible with the larger stabilizers. Then $e_{\rm FOP}=0$: $U$ bounds the disk bundle $U\times_{S^1}D^2$, which is an NC derived orbifold of virtual dimension $1$. Such structures always exist pointwise. Independently, mapping tori of finite-order NC automorphisms have $e_{\rm FOP}=0$, by a covering argument.

**Verbatim failure (Proposition D).** In an explicit oriented NC model with $e_{\rm FOP}=0$, no $S^1$-invariant section is FOP-transverse.

So the classical equivariant-perturbation argument does not transfer verbatim, but the vanishing survives on these models. We do not decide whether the Floer pairing is classical. `verify.py`: 64 exact checks, FALLOS = 0.


## 1. Introduction

### 1.1 The question

Bai and Xu [BX26] build integral Hamiltonian Floer theory on Fukaya–Ono's normally polynomial perturbations [FO97], in the form developed in [BX22b]; they call these FOP perturbations. Composing the Floer Poincaré pairing with the PSS map gives a nondegenerate pairing on $H(X;\Lambda_\Pi)$, the *FOP Poincaré pairing* [BX26, Definition 1.3]. Right after that definition they write that with the rational virtual techniques of [FO99, LT98, Par16], "such a pairing coincides with the classical Poincaré pairing … because the orbifold Euler classes satisfy properties needed for $S^1$-localization, so there is no contribution from moduli spaces of curves with nonzero energy. However, the FOP Euler characteristic classes arising in our perturbation scheme do not necessarily satisfy these properties and we do not know if the pairing is classical or not."

The classical argument has a finite-dimensional core. A moduli space of nonzero energy is, near its zero locus, a derived orbifold $(U,E,S)$ of virtual dimension $0$, and domain rotation gives a circle action that is locally free. Over $\mathbb Q$, one picks an $S^1$-equivariant multisection. It descends to the quotient, which has virtual dimension $-1$, so it can be chosen without zeros, and the count vanishes. Two features of FOP perturbations break this argument as it stands:

1. FOP perturbations are single-valued sections, normally polynomial along isotropy strata, and transverse in Bai–Xu's "strong" sense [BX22b, Def. 6.1]. An $S^1$-equivariant section with these properties need not exist.
2. The integer count only sees isotropy-free zeros. Zeros in strata with nontrivial isotropy are discarded, and those are exactly the zeros that equivariance tends to force.

This paper settles what happens in explicit finite-dimensional models. It does not decide whether the Floer-theoretic pairing is classical.

### 1.2 Results

Throughout, $(U,E,S)$ is a normally complex (NC) derived orbifold in the sense of [BX26, §4.2], oriented, of virtual dimension $\dim U-\operatorname{rank}E=0$, with $S^{-1}(0)$ compact. Its *FOP Euler number* $e_{\rm FOP}(U,E,S)\in\mathbb Z$ is the signed count of isotropy-free zeros of an FOP-transverse perturbation; it is well defined by [BX22b, Thm. 6.3]. The rational orbifold Euler number is $e_{\mathbb Q}\in\mathbb Q$. Section 2 recalls everything we use.

**Theorem A (linear models; §3).** Let $\Gamma$ be a finite group and $V,W$ complex $\Gamma$-representations with $\dim_{\mathbb C}V=\dim_{\mathbb C}W$. Assume $\Gamma$ acts freely on $V\setminus0$ and $W^\Gamma=0$. Let $P:V\to W$ be a continuous $\Gamma$-equivariant map with $P^{-1}(0)$ compact. Let $\mu=\mu_\Gamma(V,W)\ge1$ be the multiplicity at $0$ of a generic $\Gamma$-equivariant polynomial map $V\to W$ (Definition 3.1). Then
$$e_{\rm FOP}(V/\Gamma,W,P)=\frac{\deg P-\mu}{|\Gamma|},\qquad e_{\mathbb Q}(V/\Gamma,W,P)=\frac{\deg P}{|\Gamma|}.$$
In particular $\deg P\equiv\mu\pmod{|\Gamma|}$. If instead $W^\Gamma\ne0$, then $e_{\rm FOP}=e_{\mathbb Q}=\deg P/|\Gamma|$.

For $\mathbb Z_p$ acting on $\mathbb C$ with weight $a$ and $P=z^k$, this gives $e_{\rm FOP}=\lfloor k/p\rfloor$ and $e_{\mathbb Q}=k/p$ (Corollary 3.4). Now suppose $P$ is equivariant for a circle action whose only fixed point is the orbifold point. Then $e_{\mathbb Q}$ is the Atiyah–Bott fixed-point prediction, and $e_{\rm FOP}$ differs from it by the integer-producing correction $-\mu/|\Gamma|$ (Corollary 3.6). Proposition 3.7 extends the comparison $e_{\mathbb Q}-e_{\rm FOP}=\sum\varepsilon_x\mu_x/|\Gamma_x|$ to compact models whose isotropy groups have prime order and which have no excess strata.

For the circle-action results, we present $U=\tilde V/G$ with $G$ compact, together with a compact group $G^+\supset G$ such that $G^+/G\cong S^1$ acts on $(\tilde V,E,S)$ and preserves orientations and NC data (§4.1). We assume $G^+$ has finite stabilizers near the zero locus. The quotient $B=\tilde V/G^+$ is then an orbifold with the larger local groups $G^+_x\supseteq G_x$. Orbits with $G^+_x\ne G_x$ are called *exceptional*.

**Theorem B (NC circle actions; §4.2).** Suppose $B$ and the descended bundle carry NC structures for the groups $G^+_x$ that restrict to the given NC structures of $(U,E)$; call such an action *normally complex*. Then $e_{\rm FOP}(U,E,S)=0$. This holds in particular if there are no exceptional orbits, or if the exceptional orbits are isolated and the NC data are linear in slices near them (Corollary 4.3). Pointwise, the required structures always exist (Lemma 4.2).

The proof avoids equivariant FOP perturbations altogether. $U$ is the boundary of the disk bundle $W=U\times_{S^1}D^2$. Under the hypothesis, $W$ is an NC derived orbifold of virtual dimension $1$, and the FOP cobordism argument applies.

**Theorem C (mapping tori; §4.3).** Let $M$ be an NC orbifold with an NC bundle $F$ of rank $\dim M+1$. Let $\varphi$ be an NC automorphism of $(M,F)$ with $\varphi^q=\mathrm{id}$, and let $s$ be a $\varphi$-equivariant section with compact zero locus. Then the mapping torus $(U_\varphi,E_\varphi,S)$ has $e_{\rm FOP}=0$. No NC condition on the quotient is needed. The proof uses the covering principle (Lemma 4.5): finite unramified coverings multiply $e_{\rm FOP}$ by their degree.

**Proposition D (verbatim failure; §4.4).** There is an explicit oriented NC derived orbifold $(U,E,S)$ of virtual dimension $0$ with the following properties. It carries a locally free circle action. $S$ is $S^1$-invariant with compact zero locus, a $2$-torus inside a $\mathbb Z_2$-stratum with $n_{\mathbb Z_2}=0$. *Every* $S^1$-invariant section vanishes on that torus, so no $S^1$-invariant section is FOP-transverse. Nevertheless $e_{\rm FOP}=0$, as Theorems B and C predict, and an explicit nowhere-vanishing non-invariant section exhibits this directly.

**Which outcome.** In terms of the two outcomes one might hope for: we did **not** find a model of type (A) in which a locally free circle action coexists with $e_{\rm FOP}\ne0$. We obtained results of type (B) for two natural classes, NC circle actions (Theorem B) and mapping tori (Theorem C). We also show that the classical *argument*, which uses equivariant perturbations, cannot be applied verbatim (Proposition D). The integer corrections of Theorem A sit at $S^1$-*fixed* orbifold points. In the Floer pairing those points correspond to zero-energy configurations, which are not where the open question lies; we include these corrections because they make precise the sense in which FOP Euler numbers fail the Atiyah–Bott fixed-point formula. Section 5 says what these finite-dimensional statements imply for [BX26, Def. 1.3], and what they do not.

**Proved / conditional / numerical.** Theorem A, Corollaries 3.4–3.6, Proposition 3.7, Lemma 4.2, Lemma 4.5 and Proposition D are proved here from the definitions of [BX22b, BX26]. Theorem A also uses one standard fact about Whitney stratifications (the frontier condition, §3.2). Theorems B and C additionally use the relative (collared-boundary) versions of the existence and invariance statements of [BX22b], listed as (I1)–(I4) in §2.2. These are part of the toolkit of [BX22b, BX26], but we did not re-derive them. Every number in the examples was computed exactly by `verify.py` (64 checks, FALLOS = 0). No statement depends on floating-point numerics.

## 2. Setting and recollections

### 2.1 NC derived orbifolds

Let $\Gamma$ be finite and $V$ a real $\Gamma$-representation. The *basic decomposition* is $V=V^\Gamma\oplus\check V_\Gamma$, where $\check V_\Gamma$ is the sum of the nontrivial irreducible summands. An NC structure on $V$ is a $\Gamma$-invariant complex structure on $\check V_\Gamma$ [BX26, §4.2.1]. For a $\Gamma$-manifold $U$ and an equivariant bundle $E$, an NC structure consists of $H$-invariant complex structures on $\check E_H\subset E|_{U^H}$, one for each $U$-essential subgroup $H$. These must be compatible under conjugation, and for $K\subseteq H$ they must satisfy $\check E_H\cong\check E_K\oplus(\check E_H\cap E^K|_{U^H})$ with matching restrictions [BX26, Def. 4.6]. On effective orbifolds the structures are imposed chartwise [BX26, Def. 4.7]. An *NC derived orbifold* is a triple $(U,E,S)$ with NC structures on $TU$ and $E$.

We work with global quotients $U=\tilde V/G$, where $G$ is compact and acts with finite stabilizers, as produced from stably complex Kuranishi charts by [BX26, Lemma 4.9]. For $x\in\tilde V$ with stabilizer $G_x$, let $N_x$ be a slice. Write $N_x=N_x^{G_x}\oplus\check N_x$ and $F_x=E_x=F_x^{G_x}\oplus\check F_x$. Since $\dim U=\operatorname{rank}E$, the expected dimension of the zero locus inside the open stratum $U^*_{(G_x)}$ is
$$n_{G_x}=\dim\check F_x-\dim\check N_x$$
[BX22b, (3.2)]. This is the virtual dimension of the restriction $S|:U^{G_x}\to E^{G_x}$. Because $\check N_x$ and $\check F_x$ are complex, **$n_\gamma$ is always even.** We use this repeatedly.

### 2.2 FOP sections, strong transversality and the integer count

Near the fixed locus $U^G$ of a chart group, write the $\check E$-component of a section as $\check s=\operatorname{ev}\circ\operatorname{graph}(\check{\mathfrak s})$. Here $\check{\mathfrak s}:N_\epsilon U^G\to\operatorname{Poly}^G_d(NU^G,\check E^G)$ is a $G$-equivariant smooth map into equivariant complex polynomial maps of degree $\le d$ [BX22b, Defs. 3.25, 3.27]. In words, the section is a polynomial in the normal variable whose coefficients may depend smoothly on the point; the invariant component is unconstrained. For example, on $\mathbb C/\mathbb Z_2$ the map $z\mapsto\bar z$ is excluded [BX22b, Rem. 3.30].

Let $Z^G_d(V,W)=\{(v,P):P(v)=0\}\subset V\times\operatorname{Poly}^G_d(V,W)$, with its canonical Whitney stratification. This is the minimal Whitney stratification refining the isotropy prestratification; it is complex algebraic and $G$-invariant [BX22b, Thm. 4.3]. An FOP section is *strongly transverse at $p$* if the induced map $\tilde S$ is transverse at $p$ to all strata of $\{0\}\oplus Z^G_d$ [BX22b, Def. 6.1]. We use:

* **(I1) Existence and extension.** FOP-transverse perturbations exist $C^0$-close to any section with compact zero locus, and they extend from neighbourhoods of closed subsets [BX22b, Thm. 6.3; BX26, Thm. 8.2(3), Lemma 8.4]. The same holds on orbifolds with collared boundary, where the behaviour at the boundary is prescribed [BX26, footnote 14 and Lemma 8.4].
* **(I2) Locality, products, free part.** FOP transversality is local and agrees with classical transversality on the isotropy-free part. Products of FOP-transverse sections are FOP-transverse [BX26, Thm. 8.2(1),(2),(4)]. It is preserved by NC isomorphisms of charts, since it is defined chartwise.
* **(I3) Strata.** If $S'$ is strongly transverse with compact zero locus, then $S'^{-1}(0)\cap U^*_\gamma$ is a smooth manifold of dimension $n_\gamma$. Its closure meets deeper strata in dimension $\le n_\gamma-2$ [BX22b, Prop. 6.6]. In particular, the closure of the free zero locus is a pseudomanifold of dimension $\dim U-\operatorname{rank}E$ [BX26, Thm. 8.2(6)].
* **(I4) Invariance.** The class of the free zero locus does not depend on the perturbation [BX22b, Thm. 6.3]. Equivalently, it is a cobordism invariant: on an NC derived orbifold $W$ of virtual dimension $1$ with collared boundary $\partial W=U$ and compact zero locus, an FOP-transverse section restricting to an FOP-transverse section on $\partial W$ has a free zero locus that is a compact oriented $1$-manifold with boundary equal to the free zeros on $U$, by (I3). Homotopies whose zero loci stay in a fixed compact set are a special case ($W=[0,1]\times U$).

**Definition 2.1.** $e_{\rm FOP}(U,E,S):=\sum_{x\in S'^{-1}(0)\cap U_{\rm free}}\varepsilon(x)$. Here $S'$ is any FOP-transverse perturbation and $\varepsilon(x)=\pm1$ is the local sign, computed with the orientation of $\det TU\otimes\det E^*$.

The *rational* Euler number $e_{\mathbb Q}$ is the weighted count $\sum_x\deg_x/|\Gamma_x|$ of zeros of any transverse multisection, or of any section with isolated zeros. Here $\deg_x$ is the local degree in a chart. The following is the classical vanishing behind [BX26, after Def. 1.3]; we recall it.

**Fact 2.2 (rational $S^1$-vanishing).** If a circle acts on $(U,E,S)$ preserving orientations and is locally free near $S^{-1}(0)$, then $e_{\mathbb Q}(U,E,S)=0$. Indeed, an equivariant multisection descends to the quotient, which has virtual dimension $-1$, and can be chosen nowhere zero.

## 3. Linear models with an isolated orbifold point

### 3.1 Setting

Let $\Gamma$ be finite and let $V,W$ be complex representations with $\dim_{\mathbb C}V=\dim_{\mathbb C}W=n$. Assume $\Gamma$ acts freely on $V\setminus0$ (so $\Gamma$ acts effectively) and $W^\Gamma=0$. The NC structures are the given complex structures: every nontrivial subgroup $H$ has $\check V_H=V$ and $\check W_H=W$. Take $U=V/\Gamma$ and $E=(V\times W)/\Gamma$. The isotropy strata are $\{0\}$ (group $\Gamma$, $n_\Gamma=\dim W-\dim V=0$) and the free part. A section with compact zero locus is a $\Gamma$-equivariant continuous map $P:V\to W$ with $P^{-1}(0)$ compact. Its degree $\deg P\in\mathbb Z$ is computed on a large sphere. Orientations come from the complex structures.

**Definition 3.1.** Write $\mathcal P=\operatorname{Poly}^\Gamma_d(V,W)$, with $d$ larger than the bound $d_0$ of [BX22b, Lemma 3.2]. For $Q\in\mathcal P$ with isolated zero at $0$, let $m_0(Q)$ be its local multiplicity, i.e. the local degree, which equals $\dim_{\mathbb C}\mathcal O_0/(Q_1,\dots,Q_n)$. Set $\mu_\Gamma(V,W):=m_0(Q)$ for $Q$ in a nonempty Zariski-open subset of $\mathcal P$ (Lemma 3.2).

**Lemma 3.2.** (i) There is a nonempty Zariski-open $\mathcal P^\circ\subset\mathcal P$ such that every $Q\in\mathcal P^\circ$ has finitely many zeros, the free ones simple, and $m_0$ is constant on $\mathcal P^\circ$; call this constant $\mu$. (ii) $\mu=\min m_0(Q)$ over equivariant polynomial maps with isolated zero at $0$, and $\mu\ge1$. (iii) Let $J=\{Q\in\mathcal P:0$ is not isolated or $m_0(Q)>\mu\}$. Then $J$ is a proper algebraic subset, and $(\{0\}\times\mathcal P)\cap\overline{Z^*_{\rm free}}=\{0\}\times J$.

*Proof.* The free stratum of $Z^\Gamma_d$ is a nonsingular complex algebraic set of dimension $\dim\mathcal P+\dim V-\dim W=\dim\mathcal P$ [BX22b, Prop. 3.1; BaiN, Prop. 3.1]. Its projection to $\mathcal P$ is therefore generically finite and unramified, which gives finitely many free zeros, all simple, on a Zariski-open set. Since $W^\Gamma=0$, every $Q$ vanishes at $0$, so $\mu\ge1$. If the zero at $0$ were non-isolated for generic $Q$, the free zero set would have positive dimension, which is a contradiction. Upper semicontinuity of the local multiplicity in algebraic families makes $m_0$ minimal, hence constant, on a Zariski-open set; this gives (i) and (ii). For (iii): if $m_0(Q)>\mu$, then nearby generic $Q'$ have total multiplicity $m_0(Q)$ near $0$, of which only $\mu$ sits at the origin. So free zeros of $Q'$ tend to $0$ as $Q'\to Q$, i.e. $(0,Q)\in\overline{Z^*_{\rm free}}$. Conversely, if $m_0(Q)=\mu$, no zeros of nearby $Q'$ other than $0$ come close to $0$. The same argument applies if the zero is non-isolated. $\square$

### 3.2 The formula

**Lemma 3.3.** Let $S'$ be strongly transverse at $0$, with lift $\check{\mathfrak s}:N_\epsilon\{0\}=B_\epsilon(V)\to\mathcal P$. Then $\check{\mathfrak s}(0)\notin J$, and the local degree of $S'$ at $0$ equals $\mu$.

*Proof.* Let $\Sigma$ be the stratum of $Z^\Gamma_d$ containing $(0,\check{\mathfrak s}(0))$. If $\check{\mathfrak s}(0)\in J$, then by Lemma 3.2(iii) the point lies in the closure of a free stratum $\Sigma'$. Whitney stratifications with connected strata satisfy the frontier condition [Mat70, GWdPL76], so $\Sigma\subset\overline{\Sigma'}\cap(\{0\}\times\mathcal P)=\{0\}\times J$. Hence $\dim_{\mathbb R}\Sigma\le\dim_{\mathbb R}\mathcal P-2$. The map $\tilde S(\nu)=(\nu,\check{\mathfrak s}(\nu))$ has differential of rank $\dim V$, so $\operatorname{im}d\tilde S+T\Sigma$ has dimension at most $\dim V+\dim\mathcal P-2<\dim(V\times\mathcal P)$. Thus transversality fails, contradicting the assumption.

So $Q_0:=\check{\mathfrak s}(0)\notin J$. Then $S'(\nu)=\check{\mathfrak s}(\nu)(\nu)$ is homotopic near $0$ to $Q_0(\nu)$ via $\check{\mathfrak s}(t\nu)(\nu)$, $t\in[0,1]$. No zero crosses a small sphere $|\nu|=\delta$ during this homotopy, because $Q_0\notin J$: polynomials near $Q_0$ have no zeros in $0<|\nu|\le\delta$ (Lemma 3.2(iii)). Hence the local degree is $m_0(Q_0)=\mu$, and it is positive because $Q_0$ is complex-analytic. $\square$

**Theorem A.** In the setting of §3.1,
$$e_{\rm FOP}(V/\Gamma,W,P)=\frac{\deg P-\mu_\Gamma(V,W)}{|\Gamma|},\qquad e_{\mathbb Q}=\frac{\deg P}{|\Gamma|},\qquad \deg P\equiv\mu_\Gamma(V,W)\pmod{|\Gamma|}.$$
If $W^\Gamma\ne0$ (and $\Gamma$ still acts freely on $V\setminus0$), then $e_{\rm FOP}=e_{\mathbb Q}=\deg P/|\Gamma|$.

*Proof.* By (I1), choose an FOP-transverse $S'$ that agrees with $P$ outside a compact set. Upstairs on $V$, $S'$ is an equivariant map of degree $\deg P$, with isolated zeros: the origin, of local degree $\mu$ (Lemma 3.3), and free zeros. The free zeros are transverse by (I2) and come in free $\Gamma$-orbits. All points of an orbit carry the same sign, since $\Gamma$ acts complex-linearly and preserves the orientations. Hence $\deg P=\mu+|\Gamma|\,e_{\rm FOP}$. The rational count weights the origin by $1/|\Gamma|$ and each free orbit by $1$, so $e_{\mathbb Q}=\mu/|\Gamma|+e_{\rm FOP}=\deg P/|\Gamma|$. If $W^\Gamma\neq0$, then $n_\Gamma=-\dim W^\Gamma<0$. By (I3) no zero lies at $0$, and the same computation applies with $\mu$ replaced by $0$. $\square$

*Remarks.* (1) The congruence $\deg P\equiv\mu$ is a byproduct. For diagonal cyclic actions it agrees with the classical congruence for equivariant maps between free representation spheres, $\deg\equiv\prod b_j/\prod a_i\pmod p$ [tD87, Ch. II]; `verify.py` checks this. (2) By Theorem A, $e_{\rm FOP}$ is the number of free $\Gamma$-orbits of zeros of a generic equivariant normally polynomial perturbation, counted with sign. The orbifold point is invisible, even though it carries the rational weight $\mu/|\Gamma|$. (3) The formula needs the lift at $0$ to lie off $J$. A non-generic lift such as $z^5+z^3$ on $\mathbb C/\mathbb Z_2$ (multiplicity $3>\mu=1$) would give the wrong count. Lemma 3.3 shows that strong transversality excludes it.

### 3.3 Cyclic examples and the Atiyah–Bott comparison

**Corollary 3.4 (rank one).** Let $\mathbb Z_p$ act on $V=\mathbb C$ with unit weight $a$, on $W=\mathbb C$ with weight $b\equiv ka$, and take $P=z^k$. Let $r\in\{0,\dots,p-1\}$ with $r\equiv k\pmod p$. Then $\mu=r$ when $r\ne0$, and $W$ is trivial when $r=0$. In both cases
$$e_{\rm FOP}(\mathbb C/\mathbb Z_p,z^k)=\Big\lfloor\frac kp\Big\rfloor,\qquad e_{\mathbb Q}-e_{\rm FOP}=\Big\{\frac kp\Big\}.$$
*Proof.* The equivariant monomials are $z^j$ with $j\equiv k\pmod p$, so a generic element is $z^r g(z^p)$ with $g(0)\ne0$. Now apply Theorem A. $\square$

**Corollary 3.5 (scalar cyclic actions).** Let $\mathbb Z_p$ act on $\mathbb C^n$ by a scalar unit weight $a$, and let $W=\bigoplus_j\mathbb C_{b_j}$ with all $b_j\not\equiv0$. Let $r_j\in\{1,\dots,p-1\}$ with $r_j\equiv b_ja^{-1}$. Then $\mu=\prod_jr_j$, and $e_{\rm FOP}=(\deg P-\prod r_j)/p$.

*Proof.* The equivariant monomials of the $j$-th component are exactly those of degree $\equiv r_j\pmod p$. A generic element therefore has lowest-order part a generic $n$-tuple of forms of degrees $r_1,\dots,r_n$. These have only the common zero $0$, so Bézout gives multiplicity $\prod r_j$. $\square$

For non-scalar weights, $\mu$ is not a product of "minimal degrees" in any simple sense. For instance, with $\mathbb Z_5$ weights $(1,2)$ on $V$ and $(1,1)$ on $W$, the generic map is equivalent to $(z_1,z_2^3)$ and $\mu=3$. With target weights $(3,4)$, the generic map has lowest terms $(z_1z_2+z_1^3,\;z_2^2+z_1^2z_2+z_1^4)$ and $\mu=6$. All such values below were computed exactly by resultants after a generic linear change of coordinates (`verify.py`, §3).

**Corollary 3.6 (FOP numbers versus the Atiyah–Bott formula).** In the setting of Theorem A, let a circle act on $V$ and $W$, commuting with $\Gamma$, with nonzero weights $w_i$ on $V$ and $m_j$ on $W$. Let $P$ be $S^1$-equivariant, so that the only $S^1$-fixed point of $V$ is the orbifold point. Then the Atiyah–Bott formula [AB84] gives $\deg P=\prod m_j/\prod w_i$, hence
$$e_{\mathbb Q}=\frac{1}{|\Gamma|}\frac{\prod_jm_j}{\prod_iw_i}\ \ (\text{the localization prediction}),\qquad e_{\rm FOP}=e_{\mathbb Q}-\frac{\mu_\Gamma(V,W)}{|\Gamma|}.$$
In rank one, $e_{\rm FOP}$ is the integer part of the localization prediction.

| $\Gamma$, weights on $V$ | reference $P$ | weights on $W$ | $\deg P$ | $\mu$ | $e_{\mathbb Q}$ (= AB) | $e_{\rm FOP}$ |
|---|---|---|---|---|---|---|
| $\mathbb Z_2$, $(1)$ | $z^3$ | $(1)$ | 3 | 1 | 3/2 | 1 |
| $\mathbb Z_3$, $(1)$ | $z^5$ | $(2)$ | 5 | 2 | 5/3 | 1 |
| $\mathbb Z_5$, $(1)$ | $z^{10}$ | $(0)$ | 10 | 0 | 2 | 2 |
| $\mathbb Z_2$, $(1,1)$ | $(z_1^3,z_2^3)$ | $(1,1)$ | 9 | 1 | 9/2 | 4 |
| $\mathbb Z_3$, $(1,1)$ | $(z_1^2,z_2^2)$ | $(2,2)$ | 4 | 4 | 4/3 | 0 |
| $\mathbb Z_3$, $(1,1)$ | $(z_1^2,z_2^4)$ | $(2,1)$ | 8 | 2 | 8/3 | 2 |
| $\mathbb Z_5$, $(1,2)$ | $(z_1^3,z_2^2)$ | $(3,4)$ | 6 | 6 | 6/5 | 0 |
| $\mathbb Z_5$, $(1,2)$ | $(z_1,z_2^3)$ | $(1,1)$ | 3 | 3 | 3/5 | 0 |
| $\mathbb Z_5$, $(2,3)$ | $(z_1^4,z_2^3)$ | $(3,4)$ | 12 | 2 | 12/5 | 2 |
| $\mathbb Z_7$, $(1,3)$ | $(z_1^2,z_2^2)$ | $(2,6)$ | 4 | 4 | 4/7 | 0 |

In each row, the perturbation used is $P$ plus Newton-subdominant equivariant terms. This keeps the behaviour at infinity, and `verify.py` checks that it has the generic multiplicity at $0$, i.e. that it is FOP-transverse there.

### 3.4 Prime-order isotropy: comparing the two counts

**Proposition 3.7.** Let $(U,E,S)$ be a compact-zero-locus NC derived orbifold of virtual dimension $0$ such that every nontrivial isotropy group $\Gamma_x$ acts freely on $\check N_x\setminus0$ (e.g. all isotropy groups have prime order). Assume no excess strata: $n_\gamma\le0$ for all $\gamma\ne1$. Then for every FOP-transverse $S'$,
$$e_{\mathbb Q}(U,E,S)=e_{\rm FOP}(U,E,S)+\sum_{x\in S'^{-1}(0)\setminus U_{\rm free}}\frac{\varepsilon_x\,\mu_{\Gamma_x}(\check N_x,\check F_x)}{|\Gamma_x|},$$
where the sum runs over the finitely many zeros in strata with $n_\gamma=0$, and $\varepsilon_x$ is the sign of the transverse zero of $S'|:U^{\Gamma_x}\to E^{\Gamma_x}$.

*Proof.* Zeros in strata with $n_\gamma<0$ do not exist, by (I3). Near a zero $x$ in a stratum with $n_\gamma=0$, write $S'(y,\nu)=(s^\gamma(y,\nu),\check{\mathfrak s}(y,\nu)(\nu))$, with $y\in N_x^{\Gamma_x}$ and $\nu\in\check N_x$. Strong transversality at $x$ forces $d_ys^\gamma(x)$ to be an isomorphism and $\check{\mathfrak s}(x,0)\notin J$; the second condition follows from the argument of Lemma 3.3 applied to the stratum through $(x,\check{\mathfrak s}(x,0))$, where the $y$-directions are already used up by $s^\gamma$. The invariant component has no linear terms in $\nu$, because $\check N_x$ has no trivial summand. A homotopy as in Lemma 3.3 then shows that the local degree upstairs is $\varepsilon_x\mu_x$. Summing the rational contributions $\deg_x/|\Gamma_x|$ gives the claim. $\square$

*Example (`verify.py` §5).* Take $\mathbb Z_2$ acting on $\mathbb C^2$ by $(z_1,z_2)\mapsto(z_1,-z_2)$, with $W=\mathbb C_+\oplus\mathbb C_-$ and $n_{\mathbb Z_2}=0$. Perturb $P=(z_1^2,z_2^3)$ to $Q=(z_1^2+2z_1-3+5z_2^2,\;z_2^3+z_2(2+z_1))$. The zeros are two stratum zeros $(1,0),(-3,0)$ with $\mu=1$ and four free zeros, i.e. two orbits. So $e_{\mathbb Q}=6/2=3$ and $e_{\rm FOP}=2$, with difference $2\cdot\tfrac12$.

## 4. Circle actions

### 4.1 Setting

Let $U=\tilde V/G$ as in §2.1, and let $G^+$ be a compact Lie group containing $G$ as a normal subgroup with $G^+/G\cong S^1$. Suppose $G^+$ acts on $\tilde V$ and on $E$, extending the $G$-action, preserving $S$, the orientations and the NC data. Assume $G^+$ has finite stabilizers on a $G^+$-invariant neighbourhood of $\tilde S^{-1}(0)$; we restrict to that neighbourhood. This models domain rotation acting on a global Kuranishi chart. The circle $S^1=G^+/G$ then acts on $U$ locally freely. For $x\in\tilde V$, let $\rho_x:G^+_x\to S^1$ be the induced homomorphism. Its kernel is $G_x$ and its image is a cyclic group $K_x$. The orbit of $x$ is *exceptional* if $K_x\ne1$, and the action is *orbifold-free* if no orbit is exceptional. Exceptional orbits arise from multiply covered configurations, among others; they may also have $G_x\ne1$. Let $B=\tilde V/G^+$, an orbifold with local groups $G^+_x$, and let $\bar E\to B$ be the descended bundle, with section $\bar s$. Near an orbit,
$$U\cong(S^1\times N_x)/G^+_x,$$
where $G^+_x$ acts on $S^1$ through $\rho_x$, and $N_x$ is a $G^+$-slice, which is also the chart of $B$ at $[x]$.

**Definition 4.1.** The action is *normally complex* if $(B,\bar E)$ carries an NC structure, in the sense of [BX26, Defs. 4.6–4.7] with respect to the groups $G^+_x$, whose restriction to subgroups of $G_x$ is the given NC structure of $(U,E)$. (The $S^1$-orbit direction is $G_x$-trivial, so this restriction makes sense.)

If the action is orbifold-free, $B$ has the same local groups as $U$, and the NC structure descends. So orbifold-free actions are normally complex.

**Lemma 4.2 (pointwise extension).** For every $x$, the slice representations $N_x$ and $F_x$ admit $G^+_x$-NC structures that restrict to the given $G_x$-NC structures.

*Proof.* Since $G_x\trianglelefteq G^+_x$, the decomposition $\check N^+=\check N_{G_x}\oplus(N^{G_x}\cap\check N^+)$ into the $G^+_x$-nontrivial part is $G^+_x$-invariant. The given complex structure $J_0$ on $\check N_{G_x}$ is $G^+_x$-invariant, because $G^+$ preserves NC data. The group $G^+_x$ acts on $N^{G_x}$ through the cyclic group $K_x$. The nontrivial part of a real $K_x$-representation is a sum of rotation planes, which have invariant complex structures, and copies of the sign representation $\mathbb R_-$ (when $|K_x|$ is even). Let $\tilde h\in G^+_x$ lift a generator of $K_x$. It preserves the orientation of the slice, because $U$ is oriented and the circle action preserves orientation. Since $\tilde h$ acts complex-linearly on $\check N_{G_x}$, we get $\det(\tilde h|_{N})=\det(\tilde h|_{N^{G_x}})=(-1)^{\#\mathbb R_-}$, so $\#\mathbb R_-$ is even. Pair the sign summands to obtain an invariant complex structure $J'$, and set $J=J_0\oplus J'$. For a subgroup $H'\subseteq G^+_x$, put $J_{H'}:=J|_{\check N_{H'}}$; this is well defined because $J$ commutes with $H'$ and $\check N_{H'}\subseteq\check N^+$. These structures satisfy [BX26, Def. 4.6(1),(2)] and restrict to $J_0$ on subgroups of $G_x$. The same argument applies to $F_x$, using that $E$ is oriented relative to $U$. $\square$

So the obstruction to Definition 4.1 is global. It amounts to choosing complex structures, compatibly, on the $\mathbb R_-$-isotypic subbundles of the normal and obstruction bundles along the exceptional strata of $B$, and on their rotation-plane parts.

### 4.2 Theorem B: normally complex circle actions

**Theorem B.** If the circle action is normally complex, then $e_{\rm FOP}(U,E,S)=0$.

*Proof.* Let $G^+$ act on the closed unit disk $D^2\subset\mathbb C$ by rotations through $G^+\to G^+/G=S^1$. Set
$$W:=(\tilde V\times D^2)/G^+,\qquad E_W:=(\tilde E\times D^2)/G^+,\qquad S_W([x,w])=S(x).$$
(1) *Structure.* At $w\ne0$ the stabilizer of $(x,w)$ is $G_x$ and $W\cong U\times(0,1]$ locally. At $w=0$ the stabilizer is $G^+_x$ and the chart is $N_x\oplus\mathbb C_{\rho_x}$. Effectiveness holds because $G_x$ acts effectively on $N_x$. The boundary is $\partial W=(\tilde V\times S^1)/G^+=\tilde V/G=U$, and it has a collar. The rank of $E_W$ is $\dim W-1$, so $W$ has virtual dimension $1$. The zero locus $\tilde S^{-1}(0)\times_{G^+}D^2$ is compact.

(2) *NC structure.* At $w=0$, use the NC structure of $B$ on $N_x$, together with the standard complex structure on $\mathbb C_{\rho_x}$, which is complex. Compatibility [BX26, Def. 4.6(2)] holds because the $\mathbb C_\rho$-summand is complex and is trivial exactly for the subgroups in $\ker\rho_x=G_x$. At $w\ne0$, use the product structure. The two descriptions agree on overlaps by Definition 4.1. The bundle $E_W$ is handled in the same way.

(3) *Cobordism.* By (I1), choose an FOP-transverse $S'_U$ on $U$ and extend it, with a collar, to an FOP-transverse $S'_W$ on $W$ that is $C^0$-close to $S_W$. Its zero locus is then compact. By (I3), the free zero locus of $S'_W$ is a $1$-manifold. Its closure adds only points in strata of dimension $\le1-2<0$, that is, none. So it is a compact oriented $1$-manifold whose boundary is $S_U'^{-1}(0)\cap U_{\rm free}$; here we use $W_{\rm free}\cap\partial W=U_{\rm free}$, since stabilizers agree for $w\ne0$. The signed count of its boundary points is $0$. $\square$

**Corollary 4.3.** $e_{\rm FOP}=0$ in each of the following cases. (a) The action is orbifold-free. (b) $U$ is a linear tube $(S^1\times N)/H$ with linear NC data, where $H$ is finite, $\rho:H\to S^1$, and $N$ is an $H$-representation. (c) More generally, near each exceptional orbit the NC data are linear in a slice, and the exceptional orbits are isolated.

*Proof.* (a) was noted after Definition 4.1. In (b) and (c), Lemma 4.2 gives constant NC structures on the linear slices of $B$. Away from the exceptional points, the structure descended from $U$ is used. The two agree on overlaps because both are the constant linear structure restricted to the subgroups of $G_x$. $\square$

*Remark 4.4.* The proof of Theorem B is the integral counterpart of the rational argument. The rational argument uses that $E$ is pulled back from the quotient. Here we use instead that $(U,E,S)$ bounds the NC disk bundle, and the hypothesis is exactly what makes this disk bundle an object of $\mathrm{dOrb}^{\rm NC}$. Note that $W$ has the larger stabilizers $G^+_x$ along its core $B$. Core points with $G^+_x=1$ are free points of $W$ and are handled by the same $1$-manifold argument. Core points with $G^+_x\ne1$ are never counted.

### 4.3 Theorem C: mapping tori and finite coverings

**Lemma 4.5 (covering principle).** Let $\pi:\hat U\to U$ be a finite unramified covering of NC orbifolds of degree $q$, i.e. a local NC isomorphism with fibres of cardinality $q$. Then $e_{\rm FOP}(\hat U,\pi^*E,\pi^*S)=q\,e_{\rm FOP}(U,E,S)$.

*Proof.* If $S'$ is FOP-transverse on $U$, then $\pi^*S'$ is FOP-transverse, by locality and invariance under NC isomorphisms (I2). Free points lie over free points, $q$ to $1$, with the same signs. Then apply (I4). $\square$

**Theorem C.** Let $M=\tilde M/\Gamma$ be an NC orbifold and $F\to M$ an NC bundle of rank $\dim M+1$. Let $\varphi$ be an NC automorphism of $(M,F)$, lifted to $\tilde\varphi$ normalizing $\Gamma$, with $\tilde\varphi^q\in\Gamma$. Let $s$ be a $\varphi$-equivariant section with compact zero locus. Form the mapping torus
$$U_\varphi=(\mathbb R\times\tilde M)/\langle\Gamma,T\rangle,\qquad T(\theta,m)=(\theta+1,\tilde\varphi m),$$
with $E_\varphi$ and $S=s$ defined in the same way, and with $S^1=\mathbb R/q\mathbb Z$ acting by translation. Then $e_{\rm FOP}(U_\varphi,E_\varphi,S)=0$.

*Proof.* The group $\langle\Gamma,T^q\rangle$ is also generated by $\Gamma$ and the translation by $q$, because $T^q\circ(\tilde\varphi^q)^{-1}$ is that translation. Hence $\hat U:=(\mathbb R\times\tilde M)/\langle\Gamma,T^q\rangle\cong(\mathbb R/q\mathbb Z)\times M$. The map $\hat U\to U_\varphi$ is an unramified $q$-fold covering, the quotient by the free $\mathbb Z_q$-action induced by $T$ (free on the $\theta$-coordinate). The pulled-back section is $\mathrm{pr}^*s$. Choose an FOP-transverse $s'$ on $M$ rel infinity; its free zero set is empty, since the virtual dimension is $-1$. The product of the zero section of the rank-$0$ bundle on $\mathbb R/q\mathbb Z$ with $s'$ is FOP-transverse (I2), and its free zeros are $(\mathbb R/q\mathbb Z)\times\emptyset=\emptyset$. Thus $e_{\rm FOP}(\hat U)=0$, and Lemma 4.5 gives $q\,e_{\rm FOP}(U_\varphi)=0$. $\square$

Theorem C needs no NC structure on the quotient. It applies, for instance, when the sign-type parts along exceptional strata carry no complex structure, provided the circle bundle admits a global slice. Theorem B needs no slice. Neither theorem covers circle actions that are both non-NC and without a global slice (or a suitable finite cover); see §7.

### 4.4 Proposition D: equivariant FOP perturbations need not exist

Let $\tilde M=S^1_t\times\mathbb R^2_y\times\mathbb C_z$ and $\Gamma=\{1,g\}$ with $g(t,y,z)=(t,y,-z)$. Let $\tilde\varphi(t,y,z)=(t,-y,z)$. It commutes with $g$, satisfies $\tilde\varphi^2=1$, and preserves orientation. Let $F=\mathbb R^4\oplus\mathbb C$, with $g$ acting by $(1,-1)$ and $\tilde\varphi$ by $(-1,+1)$. This action is orientation-preserving, and $\tilde\varphi$ preserves the NC structure, namely the complex structures on $\check N_g=\mathbb C_z$ and $\check F_g=\mathbb C$. Let $(U,E)$ be the mapping torus with $S^1=\mathbb R/2\mathbb Z$, as in Theorem C with $q=2$. Then $\dim U=6=\operatorname{rank}E$. The stratum $U_g=\{z=0\}$ has $n_g=\dim\check F_g-\dim\check N_g=0$. The circle action is locally free, with exceptional set $\{y=0\}$ (stabilizer generated by the half-turn).

**Proposition D.** (i) $S(\theta,t,y,z)=(y_1,y_2,0,0,z)$ is an $S^1$-invariant FOP section with compact zero locus $T_0=\{y=0,z=0\}$, a $2$-torus contained in the $\mathbb Z_2$-stratum $U_g$. (ii) Every $S^1$-invariant section of $E$ vanishes on $T_0$, so no $S^1$-invariant section is FOP-transverse. (iii) The section
$$s_\theta(t,y,z)=\big(y_1,\;y_2,\;\epsilon\cos\pi\theta,\;\epsilon\sin\pi\theta,\;z\big),\qquad\epsilon>0,$$
is a well-defined, nowhere-vanishing FOP section of $E\to U$ that is homotopic to $S$ through sections whose zeros lie in $T_0$. Hence $e_{\rm FOP}(U,E,S)=0$.

*Proof.* (ii) An $S^1$-invariant section is a $\Gamma$-equivariant, $\tilde\varphi$-equivariant map $(a,b):\tilde M\to\mathbb R^4\oplus\mathbb C$. Then $\tilde\varphi$-equivariance gives $a(t,-y,z)=-a(t,y,z)$, so $a=0$ on $\{y=0\}$, and $g$-equivariance gives $b(t,y,-z)=-b(t,y,z)$, so $b=0$ on $\{z=0\}$. Hence $(a,b)=0$ on $T_0\subset U_g^*$. But by (I3), an FOP-transverse section meets $U_g^*$ in a manifold of dimension $n_g=0$. (iii) The gluing condition $s_{\theta+1}(m)=\tilde\varphi_F\,s_\theta(\tilde\varphi^{-1}m)$ holds because $\cos\pi(\theta+1)=-\cos\pi\theta$ and $\sin\pi(\theta+1)=-\sin\pi\theta$, while $\tilde\varphi_F=-1$ on $\mathbb R^4$ and $y\mapsto-y$. The section is $g$-equivariant, and its $\check F$-component $z$ is a polynomial in the normal variable. Since $|s_\theta|^2\ge\epsilon^2$, it has no zeros, so it is FOP-transverse vacuously. The homotopy $(y_1,y_2,\tau\epsilon\cos\pi\theta,\tau\epsilon\sin\pi\theta,z)$, $\tau\in[0,1]$, has all its zeros in $T_0$, so (I4) applies. $\square$

`verify.py` §6 checks (ii) by brute force on the space of all equivariant polynomial components of degree $\le4$. It also checks the gluing identity, the equivariance and the lower bound in (iii). The variant with $\tilde\varphi$ acting by $-1$ on $\check F$ is ill-posed: every invariant section then vanishes on the non-compact set $\{y=0\}$ (control in `verify.py`).

## 5. What this implies for [BX26, Definition 1.3]

The rational argument that the Poincaré pairing is classical has two steps. First, the zero-energy configurations reproduce the classical pairing. Second, the moduli spaces of nonzero energy contribute nothing, because of the domain-rotation circle action. Our results bear on the second step only, and only in finite-dimensional form:

* **What fails.** The verbatim argument needs an $S^1$-equivariant FOP-transverse perturbation, and such perturbations need not exist even in very simple oriented NC models (Proposition D). Equivariance forces zeros in isotropy strata of the wrong dimension. Moreover, FOP Euler numbers do not obey the Atiyah–Bott fixed-point formula at $S^1$-fixed orbifold points: the correction is $-\mu/|\Gamma|$ (Theorem A, Corollary 3.6). So the phrase "FOP Euler classes do not necessarily satisfy these properties" is accurate in a precise sense.
* **What survives.** If the circle action on a chart is normally complex in the sense of Definition 4.1 (Theorem B), or the chart is a mapping torus (Theorem C), or it has a finite unramified cover on which the lifted action is orbifold-free (Lemma 4.5 with Corollary 4.3(a)), then the integer count of a single compact, zero-dimensional chart vanishes. So the obstruction vanishes on all these local models. Lemma 4.2 shows that the condition of Theorem B holds pointwise automatically; what remains is a global, bundle-theoretic choice.
* **What we have not done.** We have not shown that Bai–Xu's AMS-type charts for the PSS-composition moduli spaces carry $G^+$-actions that are normally complex in our sense. Nor have we shown that the inductive, collared and rigidified FOP perturbations of [BX26, Thm. N], which must also be compatible with all boundary strata of the flow categories and multimodules, can be chosen together with the disk-bundle cobordisms used in Theorem B. The stable complex structures on such charts come from the complex-linear part of the linearized Cauchy–Riemann operator, which is rotation-invariant. That makes the NC hypothesis plausible, but it is not a proof. Consequently **we do not claim that the FOP Poincaré pairing is classical**. What we can say is that the finite-dimensional obstruction suggested by [BX26] vanishes on the models studied here, and that it is not detected by any single compact chart of the kinds above.

## 6. Relation to published work

*Recalled (not new).* The following are taken from the literature: NC structures, FOP sections, strong transversality, the free-part Euler class and its properties (I1)–(I4) [BX22b, BX26]; the Fukaya–Ono idea of normally polynomial single-valued perturbations [FO97]; and the rational vanishing for locally free circle actions (Fact 2.2; e.g. [FO99, Par16]). The congruence for equivariant maps between free representation spheres [tD87], the Atiyah–Bott localization formula [AB84], and the frontier condition for Whitney stratifications [Mat70, GWdPL76] are classical. Parker [Par13] developed Fukaya–Ono's integer counts in the exploded setting. He computed integer contributions of multiple covers through a Möbius-inversion formula; his Lemma 1.3 expresses a curve's integer contribution as $\frac1{|G|}\langle\sigma_f,\{1\}\rangle$. Our Proposition 3.7 is an elementary relative of that bookkeeping in Bai–Xu's framework. Ionel–Parker [IP18] use related integrality mechanisms for the Gopakumar–Vafa formula. Rezchikov [Rez22] proves the integral Arnold conjecture with a different method, and [BX22a] with FOP perturbations. Quantum K-theory [Lee04] and complex-oriented Gromov–Witten theory [AMS23] are the settings named in [BX26] where the Poincaré pairing receives quantum corrections; we do not use them.

*New, to our knowledge.* The following appear to be new: the exact formula of Theorem A for FOP Euler numbers of linear models and its corollaries, including the Atiyah–Bott defect $-\mu/|\Gamma|$; Proposition 3.7 as stated; Definition 4.1, Lemma 4.2 and Theorem B (vanishing for NC circle actions via the disk-bundle cobordism); Lemma 4.5 and Theorem C; and the explicit model of Proposition D. A web search of arXiv listings for FOP perturbations, integral Euler classes and $S^1$-localization found no treatment of these questions. Bai's lecture notes on FOP perturbations [BaiN] contain no worked local examples of this kind. Several of the arguments are short, and experts may regard them as folklore; we make no stronger priority claim.

## 7. Limitations and open problems

1. **Scope.** Everything is finite-dimensional: single compact NC derived orbifolds of virtual dimension $0$, presented as global quotients. Nothing here addresses moduli spaces, flow categories or the compatibility system of [BX26, Thm. N].
2. **Inputs.** Theorems B and C use the collared-boundary existence and cobordism-invariance statements (I1), (I4) of [BX22b, BX26], and the general structure result (I3) for the free zero locus. We have not re-proved them. Lemma 3.3 uses the frontier condition for the canonical Whitney stratification of $Z^G_d$.
3. **Theorem A** assumes that $\Gamma$ acts freely on $V\setminus0$. **Proposition 3.7** assumes prime-order (more generally, normally free) isotropy and no excess strata. Excess strata ($n_\gamma>0$) require an excess-intersection term, which we do not compute in general.
4. **The gap.** We cannot decide whether $e_{\rm FOP}=0$ for every locally free, orientation- and NC-preserving circle action. The remaining case combines positive-dimensional exceptional strata, along which the sign-type normal or obstruction bundles admit no compatible complex structure, with a circle bundle having no global slice and no finite cover of the kind in Theorem C. We have found no counterexample.
5. **Dependence on NC data.** We have not studied how $e_{\rm FOP}$ depends on the choice of NC structure within its homotopy class. Theorem B needs the NC structure on the quotient to restrict to the given one.
6. **Verification.** `verify.py` checks the algebra and all examples exactly. The topological arguments (cobordism, coverings) are proved in the text and are not machine-checked. `verify.mpl` is a Maple mirror of the exact parts; it has been executed in Maple: 35 checks, FALLOS = 0 (output in `verify_mpl_output.txt`).

## 8. Verification

`verify.py` (SymPy 1.14) has 64 checks, ending with `FALLOS = 0`. It covers:
- dimension and parity bookkeeping;
- 306 rank-one cases $(p,a,k)$ for Corollary 3.4, with free zeros checked to be simple by discriminants;
- twelve two-dimensional diagonal $\mathbb Z_p$ models (exact resultants after a generic linear change of coordinates, multiplicity at $0$, simplicity of free zeros, divisibility by $p$, the congruence, $\mu=\prod r_j$ for scalar actions, agreement with fully generic equivariant maps);
- three fixed examples mirrored in `verify.mpl`;
- the Atiyah–Bott comparison;
- the example of Proposition 3.7;
- Proposition D (equivariance constraints on all degree-$\le4$ equivariant components, gluing, non-vanishing, non-invariance);
- Lemma 4.2 scans;
- control cases (non-equivariant or non-polynomial candidates, a multiplicity-jump lift, the naive orbit count, and the ill-posed variant of Proposition D).

The output is in `verify_output.txt`.

## References

- [AB84] M. F. Atiyah, R. Bott, The moment map and equivariant cohomology, Topology 23 (1984), 1–28.
- [AMS23] M. Abouzaid, M. McLean, I. Smith, Gromov–Witten invariants in complex-oriented generalised cohomology theories, arXiv:2307.01883.
- [BaiN] S. Bai, Lecture notes on FOP perturbations (MIT 18.937), https://math.mit.edu/~shaoyunb/18.937/FOP.pdf.
- [BX22a] S. Bai, G. Xu, Arnold conjecture over integers, arXiv:2209.08599.
- [BX22b] S. Bai, G. Xu, An integral Euler cycle in normally complex orbifolds and $\mathbb Z$-valued Gromov–Witten type invariants, arXiv:2201.02688.
- [BX26] S. Bai, G. Xu, Integral Hamiltonian Floer theory: foundations, arXiv:2606.15847.
- [FO97] K. Fukaya, K. Ono, Floer homology and Gromov–Witten invariant over integer of general symplectic manifolds – summary, Proc. Last Taniguchi Conference, 1997.
- [FO99] K. Fukaya, K. Ono, Arnold conjecture and Gromov–Witten invariant, Topology 38 (1999), 933–1048.
- [GWdPL76] C. G. Gibson, K. Wirthmüller, A. A. du Plessis, E. J. N. Looijenga, Topological Stability of Smooth Mappings, LNM 552, Springer, 1976.
- [IP18] E.-N. Ionel, T. H. Parker, The Gopakumar–Vafa formula for symplectic manifolds, Ann. of Math. 187 (2018), 1–64.
- [Lee04] Y.-P. Lee, Quantum K-theory I: foundations, Duke Math. J. 121 (2004), 389–424.
- [LT98] J. Li, G. Tian, Virtual moduli cycles and Gromov–Witten invariants of general symplectic manifolds, in: Topics in Symplectic 4-Manifolds, 1998.
- [Mat70] J. Mather, Notes on topological stability, Harvard lecture notes, 1970 (reprinted Bull. AMS 49 (2012), 475–506).
- [Par13] B. Parker, Integral counts of pseudo-holomorphic curves, arXiv:1309.0585.
- [Par16] J. Pardon, An algebraic approach to virtual fundamental cycles on moduli spaces of pseudo-holomorphic curves, Geom. Topol. 20 (2016), 779–1034.
- [Rez22] S. Rezchikov, Integral Arnol'd conjecture, arXiv:2209.11165.
- [tD87] T. tom Dieck, Transformation Groups, de Gruyter, 1987.
