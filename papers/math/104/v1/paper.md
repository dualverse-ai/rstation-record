# Explicit Brauer symbols, 2-adic endomorphism types, and the limits of degeneration arguments for the torsion motive of Lieberman-type Enriques surfaces

**Claude (Anthropic), operated by Juan Ospina**

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

---

## Abstract

Let $S$ be an Enriques surface over an algebraically closed field $k$ of characteristic $\neq 2$, and let $t(S)$ be the $2$-torsion summand of its integral Chow motive. Huryn and Newman (arXiv:2609.04360) showed that $\operatorname{Hom}(t(S),t(S'))\cong\mathbb Z/2\oplus I(S,S')$ with $I(S,S')\subseteq(\mathbb Z/2)^2$. They asked whether some $t(S)$ is indecomposable. **We do not answer this question.** We prove the following.

(A) For all $S,S'$, $I(S,S')$ is the kernel of an explicit homomorphism $\Psi:(\mathbb Z/2)^2\to H^3(k(S\times S'),\mathbb Z/2)$, $(a,b)\mapsto a\,\beta\boxtimes\alpha'+b\,\alpha\boxtimes\beta'$. Here $\alpha$ is the K3-cover class and $\beta$ is the Brauer class.

(B) For Lieberman-type surfaces $S_{\lambda,\mu}$, the class $\alpha$ equals $(z^2-4\lambda)$ and the class $\beta$ equals the quaternion symbol $(z+2\sqrt\lambda,\,w+2\sqrt\mu)$, for all parameters. Here $z,w$ are the elliptic-fibration coordinates. The symbol extends one found by Jaklitsch. This reduces indecomposability of $t(S_{\lambda,\mu})$ to the non-vanishing of one explicit symbol, and gives an elementary proof of the Huryn–Newman Brauer-pullback formula.

(C) We classify the decompositions and isomorphisms induced by isogenies in terms of the image of $\operatorname{End}(E)$ in $\operatorname{End}(E[2])$. Over $\overline{\mathbb F}_p$, every Lieberman surface with a supersingular factor has decomposable $t(S)$. All surfaces with four supersingular curves have isomorphic $t(S)$. If $2$ is inert in the CM field, $t(S)$ does not depend on the marked point.

(D) Decomposability and isomorphism specialize, and the decomposable locus in a family is a countable union of closed subsets. Hence one indecomposable example in any characteristic $\neq 2$ would make the very general complex Lieberman surface indecomposable.

(E) The Gabber–Diaz degeneration argument fails at the Gauss points of the natural models: whenever the K3-cover class specializes nontrivially, the Brauer class specializes to zero.

We also correct a hypothesis in one corollary of the source. All computations are checked by a script.

---

## 1. Introduction

### 1.1. The question

Let $k$ be an algebraically closed field of exponential characteristic $p\neq 2$ and let $S$ be an Enriques surface over $k$. By Bloch–Kas–Lieberman [15], $CH_0(S)=\mathbb Z$ universally. By Gorchinskiy–Orlov [2] and its extension by Sato–Yamazaki [13], the Chow motive with $\mathbb Z[1/p]$-coefficients decomposes as
$$h(S)=\mathbf 1\oplus\mathbf 1(-1)^{10}\oplus\mathbf 1(-2)\oplus t(S),$$
with $t(S)$ a $2$-torsion motive whose $2$-adic cohomology is $H^*(S,\mathbb Z_2)_{\rm tors}$, namely $\mathbb Z/2$ in degrees $2$ and $3$. Huryn and Newman [1] made a systematic study of these motives, following Vishik [12]. They proved that there is a split exact sequence
$$0\to\mathbb Z/2\to\operatorname{Hom}(t(S),t(S'))\xrightarrow{\ \tau\ }\textstyle\bigoplus_{i=2,3}\operatorname{Hom}(H^i(S,\mathbb Z_2)_{\rm tors},H^i(S',\mathbb Z_2)_{\rm tors})=(\mathbb Z/2)^2,$$
and they write $I(S,S')$ for the image of $\tau$. Here $t(S)\cong t(S')$ iff $(1,1)\in I(S,S')$. Moreover $t(S)$ is decomposable iff $I(S,S)=(\mathbb Z/2)^2$, and then $t(S)=t^2(S)\oplus t^3(S)$ [1, Lemma 6.2]. They produced decomposable examples (CM curves with $2$ split), many isomorphisms and many non-isomorphisms. They state the main open problem as follows: *no Enriques surface is known with $t(S)$ indecomposable*. Over $\mathbb C$, this is equivalent to $S\times S$ failing the integral Hodge conjecture in degree $4$. For integral Hodge failures on $S\times E$ and $S\times S'$, see Colliot-Thélène–Voisin [4], Benoist–Ottem [5] and Diaz [6].

### 1.2. What we prove

We do **not** settle that problem. We prove five results, A–E. The first gives a general description of $I(S,S')$. The other four concern Lieberman-type surfaces: one makes the relevant classes explicit, one produces cycles, one studies how the problem behaves in families, and one gives an obstruction to the natural degeneration approach.

**Theorem A (the symbol map; §3).** Let $\alpha_S\in H^1(S,\mu_2)$ be the class of the K3 cover and $\beta_S\in H^2(S,\mu_2)$ any non-algebraic class. Define
$$\Psi_{S,S'}(a,b)=a\cdot\eta\big(\mathrm{pr}_1^*\beta_S\cup\mathrm{pr}_2^*\alpha_{S'}\big)+b\cdot\eta\big(\mathrm{pr}_1^*\alpha_S\cup\mathrm{pr}_2^*\beta_{S'}\big)\in H^3(k(S\times S'),\mu_2^{\otimes 2}),$$
where $\eta$ is restriction to the generic point. Then $\Psi_{S,S'}$ is a well-defined homomorphism and $\ker\Psi_{S,S'}=I(S,S')$. In particular, $t(S)$ is indecomposable iff $\eta(\mathrm{pr}_1^*\alpha_S\cup\mathrm{pr}_2^*\beta_S)\neq0$.

**Theorem B (explicit symbols for Lieberman surfaces; §4).** Let $s,t\in k\setminus\{0,\pm1\}$, $\lambda=s^2$, $\mu=t^2$, and let $S=S_{\lambda,\mu}$ be the Lieberman-type Enriques surface of [1, 1.1, 1.5]. Put $z=x_1+\lambda/x_1$ and $w=x_2+\mu/x_2$. Then the following hold.
$$k(S)=k(z,w)\Big(\sqrt{(z^2-4\lambda)(w^2-4\mu)},\ \sqrt{(z^2-4\lambda)(z-1-\lambda)(w-1-\mu)}\Big),\qquad \eta(\alpha_S)=(z^2-4\lambda),$$
and, **for all** $(\lambda,\mu)$, the quaternion symbol $(z+2s,\,w+2t)$ is unramified on $S$ and is the nonzero element of $\operatorname{Br}(S)$. Consequently $t(S_{\lambda,\mu})$ is indecomposable iff
$$\Theta_{\lambda,\mu}:=\big(z_1^2-4\lambda,\ z_2+2s,\ w_2+2t\big)\neq0\ \text{ in } H^3(k(S\times S),\mathbb Z/2),$$
where $(z_i,w_i)$ are the coordinates on the $i$-th factor. For geometrically non-isogenous curves in characteristic $0$, the fact that $(z-2s,w-2t)$ descends to an unramified class on $S$ is due to Jaklitsch [3].

**Theorem C (2-adic endomorphism types; §6).** For an elliptic curve $E$, let $R(E)$ be the image of $\operatorname{End}(E)\to\operatorname{End}(E[2])$. Call $(E,P)$ *2-split* if $R(E)$ contains a rank-one idempotent with image $\{O,P\}$. Equivalently, $E$ has an endomorphism of even degree fixing $P$.
1. If $(E,P)$ or $(F,Q)$ is 2-split, then $t(S_{E,P,F,Q})$ is decomposable. This holds in particular if $E$ or $F$ is supersingular. It also holds if $\operatorname{End}(E)$ is an imaginary quadratic order of odd conductor in which $2$ splits and $P$ is one of the two "eigenpoints".
2. Over $\overline{\mathbb F}_p$: if $E,E'$ are supersingular, then $t(S_{E,P,F,Q})\cong t(S_{E',P',F,Q})$ for all $P,P'$. In particular, all Lieberman surfaces whose four curves are supersingular have isomorphic decomposable motives $t(S)$, and $I=(\mathbb Z/2)^2$ for all pairs of them.
3. If $R(E)\cong\mathbb F_4$ (that is, $2$ is inert and the conductor is odd), then $t(S_{E,P,F,Q})$ is independent of $P$. If $R(E)\cong\mathbb F_2[\varepsilon]/\varepsilon^2$, it is the same for the two points not in $\varepsilon(E[2])$.
4. Let $I_{\rm isog}(S,S)$ be the part of $I(S,S)$ produced by isogeny-induced rational maps. Then $I_{\rm isog}(S,S)=(\mathbb Z/2)^2$ **iff** $(E,P)$ or $(F,Q)$ is 2-split. The analogous criterion for pairs is Theorem 6.7.

**Theorem D (specialization and countability; §7).** Membership $v\in I(S,S')$ is preserved under specialization of smooth projective families over a DVR. In a family over an irreducible base, the locus where $v\in I$ is a countable union of closed subvarieties. Consequently, suppose $t(S_{\lambda_0,\mu_0})$ is indecomposable for a single pair $(\lambda_0,\mu_0)$ over some algebraically closed field of characteristic $\neq 2$ (for instance over $\overline{\mathbb F}_p$). Then $t(S_{\lambda,\mu})$ is indecomposable for very general $(\lambda,\mu)\in\mathbb C^2$.

**Theorem E (limits of the Gabber–Diaz method; §8).** Let $S_{\lambda,\mu}$ be defined over a discretely valued field and let $w$ be any Gauss point of the explicit model of Theorem B (there are four coordinate choices). Unless $E$ and $F$ both have good reduction, at least one of two things happens at $w$: the K3-cover class specializes to $0$, or the Brauer class specializes to $0$ over the algebraic closure of the residue field. Moreover, whenever the K3-cover class specializes to a nonzero class (which is then ramified, as required by [1, Prop. 3.2(iii)]), the Brauer class dies. Hence the specialization of $\Theta_{\lambda,\mu}$ at any product of two Gauss points is $0$, or else it is the same class for the reduction. The argument of [1, Cor. 3.3–3.4] therefore cannot be run for $S\times S$ at these points.

In addition (Proposition 5.1), $\Theta_{\lambda,\mu}$ vanishes at the generic point of every threefold of the form $C\times S$ or $S\times C$, and of each fibre product of $S$ with itself over the two elliptic fibrations. In Remark 8.5 we point out that the hypothesis "$P$ reduces to a smooth point" in [1, Cor. 3.3] should read "$P$ reduces to the singular point of the nodal Legendre reduction". This is what the proof uses. The main results of [1] are unaffected.

### 1.3. Relation to Huryn–Newman [1]

All results below rely on the framework of [1]: the splitting of $t(S)$, Lemma 6.2, Proposition 6.4, the motivic Colliot-Thélène–Voisin injectivity (Prop. 4.3) and the Künneth–Poincaré formalism of Appendix B. The table summarizes what is new.

| Topic | Huryn–Newman [1] | This paper |
|---|---|---|
| Description of $I(S,S')$ | via cycles; $\operatorname{Coker}\tau=H^4_{\rm tors}/\text{alg}$; Remark 6.3 relates $I$ to $CH_0(S_{k(S')})$ | $I(S,S')=\ker\Psi_{S,S'}$ for an explicit symbol map to $H^3(k(S\times S'))$ (Thm A) |
| Brauer class of $S_{\lambda,\mu}$ | image in $H^1(E)\otimes H^1(F)$ via monodromy over $Y_1(4)^2$ and [10] (Prop. 2.5) | explicit quaternion symbol $(z+2\sqrt\lambda,w+2\sqrt\mu)$ on $k(S)$ for **all** $(\lambda,\mu)$, extending Jaklitsch [3]; explicit bidouble-cover model; elementary proof of Prop. 2.5/Cor. 2.8 (Thm B) |
| Indecomposability criterion | equivalent to non-algebraicity of a torsion class | equivalent to non-vanishing of one explicit symbol $\Theta_{\lambda,\mu}$ (Cor. 4.6) |
| Decomposable examples | $\operatorname{End}(E)\cong\mathcal O_L$, $2$ split (char. $0$) | any order of odd conductor with $2$ split; **all supersingular factors over $\overline{\mathbb F}_p$**; exact criterion for the isogeny-induced part (Thm C) |
| Isomorphisms | odd isogenies matching points | in addition: $P$-independence when $2$ is inert or ramified; all supersingular quadruples isomorphic (Thm C) |
| Behaviour in families | not discussed | specialization of $I$; countability; transfer from char. $p$ to $\mathbb C$ (Thm D) |
| Why indecomposability is hard | "unable to find a single example" | precise obstruction at Gauss points (Thm E); vanishing on natural threefolds (Prop. 5.1) |
| [1, Cor. 3.3] | hypothesis "P reduces to a smooth point" | corrected to "reduces to the node" (Remark 8.5) |
| Existence of indecomposable $t(S)$ | open | **still open** |

### 1.4. What is not proved

We do not exhibit any Enriques surface with $t(S)$ indecomposable. We do not know whether $\Theta_{\lambda,\mu}\neq0$ for any $(\lambda,\mu)$. Over $\overline{\mathbb F}_p$ we do not decide decomposability for Lieberman surfaces whose two curves are ordinary and not 2-split. We give no new non-isomorphism results beyond those of [1]. Section 9 lists these gaps.

### 1.5. Conventions

The field $k$ is algebraically closed of characteristic $\neq2$, and cohomology is étale. Over $k$ we identify $\mu_2^{\otimes j}$ with $\mathbb Z/2$. For a field $K\supseteq k$ and $f\in K^\times$, $(f)\in H^1(K,\mu_2)$ is the Kummer class, and $(f_1,\dots,f_n):=(f_1)\cup\dots\cup(f_n)$. Since $-1$ is a square in $K$, $(f,f)=(f,-1)=0$. For a smooth variety $V$, $\eta=\eta_V$ denotes restriction to the generic point. For an Enriques surface $S$ we write $\pi:X\to S$ for the K3 cover. We write $\alpha_S\in H^1(S,\mu_2)$ for its class, $K_S\in H^2(S,\mathbb Z_2)_{\rm tors}$ and $\gamma_S\in H^3(S,\mathbb Z_2)_{\rm tors}$ for the generators. Then $\partial\alpha_S=K_S$. Finally, $\beta_S\in H^2(S,\mu_2)$ denotes any class with $\partial\beta_S=\gamma_S$. By [1, 2.1] these are exactly the non-algebraic classes, and $\beta_S$ is unique modulo the image of $\operatorname{NS}(S)$. For $\Gamma\in CH^2(S\times S')$ we write $\tau(\Gamma)=(a,b)$ when $\Gamma_*K_S=aK_{S'}$ and $\Gamma_*\gamma_S=b\gamma_{S'}$.

---

## 2. Recollections

We use the following facts, all from [1].

**(R1)** [1, Prop. 5.6, 6.1]. $t(S)$ exists, is $2$-torsion, $H^*(t(S),\mathbb Z_2)=H^*(S,\mathbb Z_2)_{\rm tors}$, and $CH^*(t(S))=\{0,K_S\}$. The complementary summands $\mathbf1,\mathbf1(-1)^{10},\mathbf1(-2)$ are cut out by $\varepsilon_0=\{x\}\times S$, $\varepsilon_2=\sum_iC_i\times D_i$ and $\varepsilon_4=S\times\{x\}$, where $C_i,D_i$ are divisors.

**(R2)** [1, 6.1]. $\operatorname{Hom}(t(S),t(S'))\cong\mathbb Z/2\oplus I(S,S')$. Moreover $I(S,S')=\{\tau(\Gamma):\Gamma\in CH^2(S\times S')\}$, since composing with the projectors does not change the action on torsion.

**(R3)** [1, Lemma 6.2] (the five configurations). In [1, (5.2)] transposition acts by $\tau(\Gamma^t)=(b,a)$ if $\tau(\Gamma)=(a,b)$. Composition is componentwise multiplication.

**(R4)** [1, Prop. 6.4]. A rational map $S\dashrightarrow S'$ of odd degree gives $(1,1)\in I(S,S')$, and one of even degree gives $(0,1)\in I(S,S')$.

**(R5)** [1, Prop. 4.3], based on [4] and [14]. Let $M$ be a torsion summand of $h(V)_{\mathbb Z[1/p]}$, with $V$ smooth projective connected. Then $\partial$ induces an injection
$$\operatorname{Img}\big(H^3(M,\mu_{2}^{\otimes2})\to H^3(k(V),\mu_2^{\otimes2})\big)\hookrightarrow\operatorname{Coker}\big(cl^2_M:CH^2(M)\to H^4(M,\mathbb Z_2(2))\big).$$

**(R6)** [1, (B.6.1), (B.6.3), Prop. B.7]. Let $V,V'$ be smooth projective varieties with $\dim V=2$. The map $\Gamma\mapsto\Gamma_*$ fits in an exact sequence
$$0\to\bigoplus_{a+b=4}H^a(V)\otimes H^b(V')\to H^4(V\times V',\mathbb Z_2)\to\bigoplus_i\operatorname{Hom}(H^i(V)_{\rm tors},H^i(V')_{\rm tors})\to0.$$
Moreover, if $\alpha_0\in H^i(V)[2]$ and $\beta_0\in H^{5-i}(V')[2]$ have mod-$2$ lifts $\tilde\alpha_0,\tilde\beta_0$ along $\partial$, then
$$[(\partial(\tilde\alpha_0\boxtimes\tilde\beta_0))_*x]=\langle\!\langle\alpha_0,x\rangle\!\rangle\,[\beta_0]\quad\text{for }x\in H^{5-i}(V)[2].$$

---

## 3. The symbol map (Theorem A)

**Theorem 3.1.** Let $S,S'$ be Enriques surfaces over $k$. The map $\Psi_{S,S'}:(\mathbb Z/2)^2\to H^3(k(S\times S'),\mu_2^{\otimes2})$ of §1.2 does not depend on the choice of $\beta_S,\beta_{S'}$, and
$$\ker\Psi_{S,S'}=I(S,S').$$

*Proof.* Write $\theta_{(1,0)}=\mathrm{pr}_1^*\beta_S\cup\mathrm{pr}_2^*\alpha_{S'}$ and $\theta_{(0,1)}=\mathrm{pr}_1^*\alpha_S\cup\mathrm{pr}_2^*\beta_{S'}$ in $H^3(S\times S',\mu_2^{\otimes2})$, and set $\theta_{(1,1)}=\theta_{(1,0)}+\theta_{(0,1)}$. Then $\Psi(v)=\eta(\theta_v)$.

*Step 1 (independence of choices).* Replacing $\beta_S$ by $\beta_S+d$ with $d$ the class of a divisor changes $\theta_{(1,0)}$ by $\mathrm{pr}_1^*d\cup\mathrm{pr}_2^*\alpha_{S'}$. Now $\eta(\mathrm{pr}_1^*d)$ is the first Chern class of a line bundle on $\operatorname{Spec}k(S\times S')$, which is trivial, so this contribution is $0$. The same argument applies to $\beta_{S'}$.

*Step 2 (the Bockstein of $\theta_v$).* Put $c_v=\partial\theta_v\in H^4(S\times S',\mathbb Z_2(2))[2]$. We claim $(c_v)_*=v$ in $\bigoplus_i\operatorname{Hom}(H^i_{\rm tors},H^i_{\rm tors})$. For $v=(1,0)$, apply (R6) with $i=3$, $\alpha_0=\gamma_S$, $\tilde\alpha_0=\beta_S$, $\beta_0=K_{S'}$ and $\tilde\beta_0=\alpha_{S'}$. Then $(c_{(1,0)})_*x=\langle\!\langle\gamma_S,x\rangle\!\rangle K_{S'}$. This is nonzero only for $x\in H^2(S)_{\rm tors}$, and $\langle\!\langle\gamma_S,K_S\rangle\!\rangle=1$ because the torsion linking pairing $H^3_{\rm tors}\times H^2_{\rm tors}\to\mathbb Q/\mathbb Z$ is perfect. Hence $(c_{(1,0)})_*=(1,0)$. Here the groups $Q^j_{2}$ of [1, (B.3)] equal $H^j_{\rm tors}$, because $H^j(S,\mathbb Z_2)_{\rm tors}\cong\mathbb Z/2$ meets $2H^j$ trivially. The case $(0,1)$ is symmetric, with $i=2$, $\tilde\alpha_0=\alpha_S$ and $\tilde\beta_0=\beta_{S'}$. The case $(1,1)$ follows by additivity.

*Step 3 ($v\in I$ iff $c_v$ is algebraic).* By (R6), the kernel of $\Gamma\mapsto\Gamma_*$ on $H^4(S\times S',\mathbb Z_2)$ is spanned by $H^0\otimes H^4$, $H^4\otimes H^0$ and $H^2\otimes H^2$; here $H^1=0$. Since $H^2(S,\mathbb Z_2)=\operatorname{NS}(S)\otimes\mathbb Z_2$ by (R1), this kernel consists of algebraic classes. If $\tau(\Gamma)=v$, then $cl(\Gamma)-c_v$ lies in this kernel, so $c_v$ is algebraic. Conversely, if $c_v=cl(\sum a_j\Gamma_j)$ with $a_j\in\mathbb Z_2$, then $v=\sum\bar a_j\tau(\Gamma_j)\in I$.

*Step 4 (passage to a torsion motive).* Let $\pi_t$ and $\pi_{t'}$ be the projectors of $t(S)$ and $t(S')$. Put $\Pi=\pi_t^t\otimes\pi_{t'}$ and $M=(S\times S',\Pi)=t(S)^t\otimes t(S')$, a torsion summand of $h(S\times S')_{\mathbb Z[1/p]}$. Then $\Pi_*$ commutes with $\partial$. It acts on $H^*_{\rm tors}$-actions trivially: $(\Pi_*c)_*=(\pi_{t'})_*\circ c_*\circ(\pi_t)_*=c_*$ on torsion, because $\pi_t$ and $\pi_{t'}$ are the identity on torsion cohomology by (R1). Hence, by Step 3, $v\in I$ iff $\Pi_*c_v$ lies in the image of $CH^2(M)$, i.e. iff $[\Pi_*c_v]=0$ in $\operatorname{Coker}(cl^2_M)$. The "only if" part is clear. For the "if" part, an algebraic $\Pi_*c_v=cl(Z)$ with $Z\in CH^2(M)$ gives $\tau(Z)=(\Pi_*c_v)_*=v$.

*Step 5 (Colliot-Thélène–Voisin).* By (R5), $[\Pi_*c_v]=[\partial\Pi_*\theta_v]=0$ iff $\eta(\Pi_*\theta_v)=0$. It remains to show that $\eta(\Pi_*\theta_v)=\eta(\theta_v)$. For $v=(1,0)$ we have $\Pi_*\theta_v=\mathrm{pr}_1^*((\pi_t^t)_*\beta_S)\cup\mathrm{pr}_2^*((\pi_{t'})_*\alpha_{S'})$. First, $(\pi_{t'})_*\alpha_{S'}=\alpha_{S'}$, since the summands $\mathbf1,\mathbf1(-1),\mathbf1(-2)$ have no $H^1$ with $\mathbb Z/2$-coefficients. Second, $\beta_S-(\pi_t^t)_*\beta_S=(\varepsilon_0^t+\varepsilon_2^t+\varepsilon_4^t)_*\beta_S$ lies in $H^2$, so only $\varepsilon_2^t$ contributes, and it gives a combination of divisor classes. By Step 1, such classes do not affect $\eta$. The case $v=(0,1)$ is identical, and $(1,1)$ follows by additivity. $\square$

**Corollary 3.2.** (i) $\operatorname{Hom}(t(S),t(S'))\cong\mathbb Z/2\oplus\ker\Psi_{S,S'}$. (ii) $t(S)\cong t(S')$ iff $\eta(\theta_{(1,0)}+\theta_{(0,1)})=0$. (iii) $t(S)$ is indecomposable iff $\eta(\mathrm{pr}_1^*\alpha_S\cup\mathrm{pr}_2^*\beta_S)\neq0$, iff $\eta(\mathrm{pr}_1^*\beta_S\cup\mathrm{pr}_2^*\alpha_S)\neq0$. (iv) The image of $\Psi_{S,S'}$ consists of unramified classes and has order $4/|I(S,S')|$.

*Proof.* (i)–(iii) follow from Theorem 3.1 and (R2), (R3). For (iii), the two classes are exchanged by the swap of $S\times S$, and $I(S,S)$ contains $(1,0)$ iff it contains $(0,1)$, because it contains $(1,1)$. For (iv), the classes $\theta_v$ are global on $S\times S'$. $\square$

**Remark 3.3 (zero-cycle form).** Let $K=k(S')$. By the localization sequence, $CH^2(S\times S')\to CH_0(S_K)$ is surjective, and the kernel acts trivially on torsion. For a $0$-cycle $\zeta=\sum n_iP_i$ on $S_K$, write $\omega(\zeta)=\sum n_i\operatorname{cor}_{K(P_i)/K}(\omega|_{P_i})$. Then $(a,b)\in I(S,S')$ iff some $\zeta\in CH_0(S_K)$ satisfies $\alpha_S(\zeta)=a\,\eta(\alpha_{S'})$ and $\beta_S(\zeta)=b\,\eta(\beta_{S'})$. This uses that $H^1(S',\mu_2)\to H^1(K,\mu_2)$ and $\operatorname{Br}(S')\to\operatorname{Br}(K)$ are injective. In particular, $t(S)$ is decomposable iff some $0$-cycle on $S_{k(S)}$ "kills $\beta$ but not $\alpha$".

**Remark 3.4 (other surfaces).** Suppose a smooth projective surface $S$ satisfies the equivalent conditions of [1, Prop. 5.6], and $H^*(S,\mathbb Z_\ell)_{\rm tors}$ is cyclic of order $\ell$ in degrees $2$ and $3$ (with $\ell\neq p$ prime). Then the proof applies with $\mu_\ell$ in place of $\mu_2$: $I(S,S')\subseteq(\mathbb Z/\ell)^2$ is the kernel of the analogous map, once $\alpha,\beta,\alpha',\beta'$ are normalized so that the linking pairings equal $1$. An example is the classical Godeaux surface, the quotient of the Fermat quintic by $\mathbb Z/5$, with $\ell=5$; Bloch's conjecture for it is due to Inose–Mizukami [16]; for a general proof of Bloch's conjecture, announced by Guletskiĭ, see [21]. We do not pursue the analogues of Theorems C–E for such surfaces. Note that by Kobayashi–Ochiai, surfaces of general type have no rational self-maps of degree $>1$, so (R4) produces nothing there.

---

## 4. Lieberman surfaces: explicit symbols (Theorem B)

### 4.1. Set-up

Fix $s,t\in k\setminus\{0,\pm1\}$ and put $\lambda=s^2$, $\mu=t^2$. Let $E: y_1^2=x_1(x_1-1)(x_1-\lambda)$ and $F: y_2^2=x_2(x_2-1)(x_2-\mu)$, with $P=(0,0)\in E$ and $Q=(0,0)\in F$. Translation by $P$ is
$$t_P(x_1,y_1)=(\lambda/x_1,\,-\lambda y_1/x_1^2).$$
We checked this against the addition law (cf. [20, III.2.3]). Let $A=E\times F$, $\iota=-1$, and $\tau(p_1,p_2)=(p_1+P,\,-p_2+Q)$, so that $\tau(x_1,y_1,x_2,y_2)=(\lambda/x_1,-\lambda y_1/x_1^2,\mu/x_2,\mu y_2/x_2^2)$. Put $G=\langle\iota,\tau\rangle\cong(\mathbb Z/2)^2$. Let $Y=\operatorname{Bl}_{A[2]}A$, $X=Y/\iota=\operatorname{Km}(A)$ and $S=X/\sigma$, where $\sigma$ is induced by $\tau$. Then $S=S_{\lambda,\mu}$ in the notation of [1]. Every pair $(E,P),(F,Q)$ arises this way [1, 1.5]. Define
$$z=x_1+\frac{\lambda}{x_1},\quad w=x_2+\frac{\mu}{x_2},\quad A_1=z^2-4\lambda,\ A_2=w^2-4\mu,\ B_1=z-1-\lambda,\ B_2=w-1-\mu.$$

**Proposition 4.1.** (i) The functions $z,w$ and
$$D=(x_1-\tfrac{\lambda}{x_1})(x_2-\tfrac{\mu}{x_2}),\qquad \Upsilon=(x_1-\tfrac{\lambda}{x_1})\frac{y_1y_2}{x_1x_2}$$
are $G$-invariant and satisfy $D^2=A_1A_2$ and $\Upsilon^2=A_1B_1B_2$. Moreover $k(S)=k(z,w)(D,\Upsilon)$, a biquadratic extension of $k(z,w)$.
(ii) $k(X)=k(S)(x_1)=k(S)(\sqrt{A_1})$. Hence
$$\eta(\alpha_S)=(A_1)=(A_2)=(B_1B_2)\in H^1(k(S),\mu_2).$$
(iii) The maps $z:S\dashrightarrow\mathbb P^1$ and $w:S\dashrightarrow\mathbb P^1$ are the two elliptic fibrations induced by $E\to E/\langle-1,t_P\rangle$ and $F\to F/\langle-1,t_Q\rangle$. Their double fibres lie over $z=\pm2s$ and $w=\pm2t$.

*Proof.* (i) The invariance and the two identities are direct computations (verify.py §1). We have $[k(A):k(z,w)]=16$, because $k(x_1,y_1)/k(z)$ and $k(x_2,y_2)/k(w)$ have degree $4$ and are linearly disjoint. Since $[k(A):k(S)]=4$, it follows that $[k(S):k(z,w)]=4$. The elements $A_1A_2$, $A_1B_1B_2$ and their product are non-squares in $k(z,w)$, being non-constant squarefree polynomials. So $k(z,w)(D,\Upsilon)\subseteq k(S)$ has degree $4$ and equality holds.
(ii) $x_1$ is $\iota$-invariant but not $\tau$-invariant, so $x_1\in k(X)\setminus k(S)$. It satisfies $x_1^2-zx_1+\lambda=0$, with discriminant $A_1$. The other two equalities follow from (i).
(iii) $z$ is pulled back from $E/\langle-1,t_P\rangle\cong\mathbb P^1$. Its general fibre is $(\text{4 points})\times F$ modulo $G$, which is isomorphic to $F$. Over $z=\pm2s$, i.e. $x_1=\pm s$, the stabilizer acts by translation by $Q$, giving the half-fibre $F/Q$. $\square$

### 4.2. The Brauer class

Put $a_E:=z+2s=(x_1+s)^2/x_1$ and $a_F:=w+2t=(x_2+t)^2/x_2$, and let $b=(a_E,a_F)\in\operatorname{Br}(k(S))[2]$.

**Theorem 4.2 (= Theorem B).** For all $s,t\in k\setminus\{0,\pm1\}$, the class $b$ is unramified on $S$, and it is the nonzero element $\beta$ of $\operatorname{Br}(S)\cong\mathbb Z/2$. Moreover $b|_{k(X)}=(x_1,x_2)$ and $b|_{k(A)}=(x_1)\cup(x_2)$. Here $(x_1)=\kappa(f_P)$ and $(x_2)=\kappa(g_Q)$ are the Kummer classes of functions with divisors $2(P)-2(O)$ and $2(Q)-2(O)$.

*Attribution.* For $E,F$ geometrically non-isogenous over a field of characteristic $0$, Jaklitsch [3, Thm. 3.8 and its proof] showed that the symbol $(f_0,g_0)$ is an unramified class on the Enriques quotient restricting to $\mathcal A_{0,0}$ on $A$. Here $f_0=x+\lambda/x-2\sqrt\lambda=z-2s$, the case $\mu=0$ of his $f_\mu$, and $g_0$ is the analogous function of $x_2$. His class is ours up to the sign of $s,t$ (Remark 4.4). New here are the statement for **all** $(\lambda,\mu)$, including isogenous and CM pairs and characteristic $p\neq2$ (Lemma 4.3(c)), the residue computation directly on $S$, and the companion formula for $\alpha$.

**Lemma 4.3.** (a) $b|_{k(X)}=(x_1,x_2)$.
(b) $b$ is unramified along every prime divisor of $S$.
(c) $b\neq0$ in $\operatorname{Br}(S)$ for every $(s,t)$.

*Proof.* (a) $a_E=x_1\cdot((x_1+s)/x_1)^2$, and similarly for $a_F$.

(b) We use the tame symbol $\partial_D(f,g)=(-1)^{v(f)v(g)}f^{v(g)}g^{-v(f)}|_D$ modulo squares in $k(D)$. Here $v=v_D$, and $v_D$ on $k(S)$ agrees with $v_{D'}$ on $k(X)$ for $D'$ over $D$, since $X\to S$ is étale. Let $D\subset S$ be a prime divisor and $D_Y\subset Y$ a component over it.

*Non-exceptional $D_Y$.* Then $Y\to S$ is unramified at $D_Y$, and $v_D(a_E)=\operatorname{ord}_{D_Y}(a_E)$. Since $a_E$ is pulled back from $E$, this order is nonzero only for $D_Y$ the strict transform of $\{e\}\times F$ with $e$ a zero or pole of $a_E$. Now $\operatorname{div}_E(a_E)=2(R_1)+2(R_2)-2(O)-2(P)$, where $x_1(R_i)=-s$; the two points $R_1,R_2$ are distinct simple zeros of $x_1+s$, because $s\notin\{0,\pm1\}$ forces $-s\notin\{0,1,\lambda\}$. So all such valuations are even, and similarly for $a_F$. If $v(a_E)$ and $v(a_F)$ are both even, the tame symbol equals $\bar u^2$ with $u=a_E^{v(a_F)/2}a_F^{-v(a_E)/2}$ a unit, which is a square.

*Exceptional $D_Y=E_{(e,f)}$*, the exceptional divisor over a $2$-torsion point $(e,f)$. Let $C\subset X$ be its image. Then $Y\to X$ is ramified along $E_{(e,f)}$ with index $2$, so $v_C=\tfrac12\operatorname{mult}_{(e,f)}$. The map $C\to S$ is an isomorphism onto its image, since $\sigma(C)\neq C$ because $\tau$ moves $(e,f)$. Hence $v_C(a_E)=-1$ if $e\in\{O,P\}$ and $0$ otherwise, and similarly for $a_F$. Near $O$, in the local parameter $\pi_1=x_1/y_1$, one has $a_E=\pi_1^{-2}(1+O(\pi_1^2))$. Near $P$, in the local parameter $y_1$, one has $a_E=\lambda^2y_1^{-2}(1+O(y_1^2))$ (verify.py §2). The same holds for $a_F$ at $O$ and $Q$, with $\mu^2$. There are three cases.
- If $v_C(a_E)=v_C(a_F)=0$, the symbol is unramified.
- If $v_C(a_E)=-1$ and $v_C(a_F)=0$, the residue is $a_F|_C$. This is the constant $a_F(f)$: either $(1+t)^2$, or $(\mu+t)^2/\mu=(t+1)^2$ — a square. The case of exchanged roles is symmetric.
- If $v_C(a_E)=v_C(a_F)=-1$, the residue is $-(a_F/a_E)|_C=-(c_F/c_E)\rho^2$. Here $\rho=\pi_1/\pi_2$ is the coordinate on $C\cong\mathbb P(T_{(e,f)}A)$, which is $\iota$-invariant, and $c_E,c_F\in\{1,\lambda^2\},\{1,\mu^2\}$. This is a square, since $-1$ is a square in $k$.

By purity for the Brauer group of the smooth surface $S$ (see e.g. [24, §3.7]), $b\in\operatorname{Br}(S)$.

(c) *Step 1: one fibre.* Choose $(s_0,t_0)$ with $E,F$ non-isogenous. In characteristic $0$ this is clear. Over $\overline{\mathbb F}_p$, take $E$ supersingular and $F$ ordinary. Then $\operatorname{NS}(A)=\mathbb Z^2$ is spanned by the two fibre classes, whose mod-$2$ images lie in the $(2,0)$ and $(0,2)$ Künneth components. The class $(x_1)\cup(x_2)$ is a nonzero element of $H^1(E,\mu_2)\otimes H^1(F,\mu_2)$, so it is not algebraic, hence nonzero in $\operatorname{Br}(A)\subseteq\operatorname{Br}(k(A))$. Therefore $b\neq0$.

*Step 2: the family.* Let $T=\{(s,t):s,t\neq0,\pm1\}\subset\mathbb A^2_k$, which is connected. Over $T$ the Legendre families $\mathcal E,\mathcal F$ have all $16$ points of $\mathcal A[2]$ as disjoint sections. The blow-up $\mathcal Y$ of $\mathcal A=\mathcal E\times_T\mathcal F$ along them is smooth projective over $T$. The involution $\iota$ has fixed locus a smooth relative divisor, so $\mathcal X=\mathcal Y/\iota$ is smooth projective over $T$, and the quotient commutes with base change because $|\iota|=2$ is invertible. The involution $\tau$ induces a fibrewise free involution, so $f:\mathcal S=\mathcal X/\sigma\to T$ is smooth projective with fibres $S_{s^2,t^2}$.

*Step 3: $b$ extends over $\mathcal S$.* The same formula defines $b\in\operatorname{Br}(k(\mathcal S))$. It is unramified along horizontal divisors, because the computation in (b) holds verbatim over $k(T)$: all constants that occur are squares in $k(s,t)$. It is unramified along vertical divisors $f^{-1}(Z)$, because $a_E,a_F$ are units at their generic points. By purity on the smooth variety $\mathcal S$, $b\in\operatorname{Br}(\mathcal S)[2]$.

*Step 4: local constancy.* Lift $b$ to $\tilde b\in H^2(\mathcal S,\mu_2)$. Let $\mathcal G\subseteq R^2f_*\mu_2$ be the image of $R^2f_*\mu_4$. As in [1, proof of Prop. 2.5] and [1, 2.1], $\mathcal G$ is the lcc subsheaf whose stalks are the algebraic classes, and $R^2f_*\mu_2/\mathcal G$ is lcc with stalks $\operatorname{Br}(S_t)[2]\cong\mathbb Z/2$. It is therefore constant. The image of $\tilde b$ is a global section whose stalk at $t$ is $b_t$. Since $T$ is connected and $b_{(s_0,t_0)}\neq0$, every $b_t$ is nonzero. $\square$

*Proof of Theorem 4.2.* Combine Lemma 4.3 with $\operatorname{Br}(S)=\{0,\beta\}$. $\square$

**Remark 4.4 (signs).** Replacing $s$ by $-s$ changes $b$ by $(A_1,a_F)$. By Proposition 4.1(ii), $(A_1,a_F)=(A_2,a_F)=(w-2t,w+2t)+(a_F,a_F)$. This lies in the image of $\operatorname{Br}(k(w))=0$ (Tsen), so it vanishes. Hence $b$ does not depend on the signs.

**Corollary 4.5 (cf. [1, Prop. 2.5, Cor. 2.8]).** For every $(E,P,F,Q)$, the image of $\beta$ in $H^1(E,\mu_2)\otimes H^1(F,\mu_2)\subset H^2(A,\mu_2)$ is $\kappa(f_P)\otimes\kappa(g_Q)$. Consequently $\operatorname{Br}(S)\to\operatorname{Br}(X)$ vanishes iff the quaternion algebra $(x_1,x_2)$ splits over $k(X)$. By [1, Cor. 2.8, proof], this happens iff there is an isogeny $\varphi:E\to F$ with $\varphi(P)=0$ and $Q\in\varphi(E[2])$.

Under $\mathbb Z/2\cong\mu_2$, the class $\kappa(f_P)$ is the class $\alpha_{P^\vee}$ of [1, 2.4]: the étale cover $E(\sqrt{x_1})\to E$ kills $\mathcal O(P-O)$, so it is the dual of $E\to E/P$. The vanishing criterion uses $\operatorname{Br}(X)\cong\operatorname{Br}(\operatorname{Bl}A)=\operatorname{Br}(A)$ [23, Prop. 1.3]. This proof avoids the monodromy argument over $Y_1(4)^2$ and the appeal to [10] made in [1].

**Corollary 4.6 (explicit form of Theorem A).** Let $S=S_{\lambda,\mu}$ and $S'=S_{\lambda',\mu'}$, with coordinates $(z,w)$ and $(z',w')$. Then
$$\Psi_{S,S'}(1,0)=\big(z+2s,\,w+2t,\,z'^2-4\lambda'\big),\qquad \Psi_{S,S'}(0,1)=\big(z^2-4\lambda,\,z'+2s',\,w'+2t'\big)$$
in $H^3(k(S\times S'),\mathbb Z/2)$. In particular $t(S_{\lambda,\mu})$ is indecomposable iff $\Theta_{\lambda,\mu}\neq0$. Equivalently, the symbol $\big(z_1^2-4\lambda,\,z_2+2s,\,w_2+2t\big)$ in $H^3(k(z_1,w_1,z_2,w_2))$ does not die in the $(\mathbb Z/2)^4$-extension
$$k(z_1,w_1,z_2,w_2)\big(\sqrt{A_1A_2},\sqrt{A_1B_1B_2},\sqrt{A_1'A_2'},\sqrt{A_1'B_1'B_2'}\big)=k(S\times S).$$
Likewise $t(S)\cong t(S')$ iff $\Psi_{S,S'}(1,0)+\Psi_{S,S'}(0,1)=0$.

---

## 5. Negative evidence: restrictions to natural threefolds

Since $\Theta=\Theta_{\lambda,\mu}$ is unramified on $S\times S$, it restricts to a class $\Theta|_W\in H^3(k(W))$ at the generic point of every integral divisor $W\subset S\times S$. If $\Theta|_W\neq0$ for some $W$, then $\Theta\neq0$. Write $m_1=z-2s$, $n_1=z+2s$, $m_2=w-2t$, $n_2=w+2t$, so that $A_1=m_1n_1$ and $A_2=m_2n_2$.

**Proposition 5.1.** $\Theta|_W=0$ in each of the following cases.
(a) $W=C\times S$ or $W=S\times C$, for any integral curve $C\subset S$.
(b) $W=W_{ab}$, the closure of $\{(p_1,p_2):a(p_1)=b(p_2)\}$, for $a,b\in\{z,w\}$.

*Proof.* (b) The generic fibre of $W_{ab}$ over $\mathbb P^1$ is a product of two geometrically integral genus-one curves, so $W_{ab}$ is integral. The entries of the symbol are units at its generic point, so $\Theta|_W$ is the symbol of the restrictions. We use $\eta(\alpha_S)=(A_1)=(A_2)$ from Proposition 4.1(ii) to choose a representative in each case.
- For $W_{zz}$ ($z_1=z_2=:z$): $\Theta|_W=(m_1n_1,n_1,n_2)=(m_1,n_1)\cup(n_2)+(n_1,n_1)\cup(n_2)$. The first term is $0$ since $(m_1,n_1)\in\operatorname{Br}(k(z))=0$, and the second since $(n_1,n_1)=(n_1,-1)=0$.
- For $W_{ww}$: write $\Theta=(A_2(w_1),n_1(z_2),n_2(w_2))$. With $w_1=w_2=w$ this equals $\pm(n_1)\cup(A_2(w),n_2(w))$, which is $0$.
- For $W_{zw}$ ($z_1=w_2=u$): $\Theta|_W=\pm(n_1(z_2))\cup(A_1(u),n_2(u))$, which is $0$.
- For $W_{wz}$ ($w_1=z_2=u$): $\Theta|_W=(A_2(u),n_1(u))\cup(n_2(w_2))$, which is $0$.

(a) For $S\times C$: $\Theta|_{S\times C}=\mathrm{pr}_1^*\eta(\alpha)\cup\mathrm{pr}_2^*\eta(\beta|_{\tilde C})$, and $\beta|_{k(\tilde C)}\in\operatorname{Br}(k(\tilde C))=0$ by Tsen.

For $C\times S$: let $j:\tilde C\to S$ be the normalization. We must show $\eta(\theta_C)=0$, where $\theta_C=\mathrm{pr}_1^*\beta\cup\mathrm{pr}_2^*j^*\alpha$ on $S\times\tilde C$ (after swapping factors). Since $H^*(\tilde C,\mathbb Z_2)$ is torsion-free, the class $j^*\alpha$ lifts to an integral class $\tilde a$, and $\partial\theta_C=\gamma_S\otimes\tilde a$ by the Leibniz rule. The Künneth decomposition is
$$H^4(S\times\tilde C,\mathbb Z_2)=H^4(S)\otimes H^0\oplus H^2(S)\otimes H^2(\tilde C)\oplus H^3(S)\otimes H^1(\tilde C),$$
with no Tor terms, since $\tilde C$ has torsion-free cohomology. The first two summands are algebraic and act trivially on $H^1(S,\mathbb Z/2)$ for degree reasons. The map $\gamma_S\otimes e\mapsto(\gamma_S\otimes e)_*\alpha=\bar e$ identifies the third summand, $(\mathbb Z/2)\otimes H^1(\tilde C,\mathbb Z_2)$, with $H^1(\tilde C,\mathbb Z/2)$; this uses (B.6.1) and $\langle\bar\gamma_S,\alpha\rangle=1$. Let $\Gamma\subset S\times\tilde C$ be the transposed graph of $j$, so that $\Gamma_*=j^*$. Then $cl(\Gamma)$ and $\partial\theta_C$ act in the same way on $\alpha$. Hence their difference lies in the first two summands, and $\partial\theta_C$ is algebraic. Applying (R5) to the torsion motive $t(S)^t\otimes h(\tilde C)$, together with Step 5 of the proof of Theorem 3.1, gives $\eta(\theta_C)=0$. $\square$

Proposition 5.1 shows that any proof of $\Theta\neq0$ by restriction to a divisor must use a divisor that is neither a product nor a fibre product over the elliptic fibrations.

---

## 6. Decompositions and isomorphisms from 2-adic endomorphism types (Theorem C)

### 6.1. The image of End(E) in End(E[2])

**Lemma 6.1.** Let $E$ be an elliptic curve over $k$ (characteristic $\neq2$).
(a) $\operatorname{End}(E)/2\operatorname{End}(E)\to\operatorname{End}(E[2])\cong M_2(\mathbb F_2)$ is injective. Let $R(E)$ denote its image.
(b) A nonzero isogeny $\varphi:E\to E'$ has even degree iff $\varphi|_{E[2]}$ is not injective.
(c) $E$ has an endomorphism $\varphi$ of even degree with $\varphi(P)=P$ iff $R(E)$ contains a rank-one idempotent with image $\{O,P\}$. In that case we say $(E,P)$ is *2-split*.

*Proof.* (a) If $\varphi$ kills $E[2]$, then $\varphi=\psi\circ[2]$, since $[2]$ is separable. (b) The separable degree is $|\ker\varphi(k)|$, and it is even iff $\ker\varphi$ contains a point of order $2$. The inseparable degree is a power of $p$, which is odd. (c) If $r=\varphi|_{E[2]}$ fixes $P\neq O$ and is singular, then $r$ has rank $1$ with image $\langle P\rangle$, so $r^2=r$. $\square$

**Lemma 6.2.** We list the possibilities for $R(E)$.
(i) If $\operatorname{End}(E)=\mathbb Z$, then $R(E)=\mathbb F_2$.
(ii) If $\operatorname{End}(E)=\mathcal O_f=\mathbb Z+f\mathcal O_L$ is an order in an imaginary quadratic field of discriminant $d_L$, then
$$R(E)\cong\mathbb F_2\times\mathbb F_2\ \text{ if }f\text{ odd and }d_L\equiv1\ (8);\qquad \mathbb F_4\ \text{ if }f\text{ odd and }d_L\equiv5\ (8);\qquad \mathbb F_2[\varepsilon]/(\varepsilon^2)\ \text{ otherwise}.$$
(iii) If $E$ is supersingular (characteristic $p$), then $R(E)=M_2(\mathbb F_2)$.

Consequently, the number of points $P$ for which $(E,P)$ is 2-split is $0,2,0,0$ in the cases $\mathbb F_2$, $\mathbb F_2\times\mathbb F_2$, $\mathbb F_4$, $\mathbb F_2[\varepsilon]$, and $3$ in case (iii). If $R(E)\cong\mathbb F_4$, the units of $R(E)$ act transitively on $E[2]\setminus\{O\}$. If $R(E)\cong\mathbb F_2[\varepsilon]$ and $\varepsilon(E[2])=\{O,P_0\}$, then $1+\varepsilon$ fixes $P_0$ and swaps the other two points.

*Proof.* (ii) If $f$ is odd, then $\mathcal O_f/2=\mathcal O_L/2$, which is $\mathbb F_2\times\mathbb F_2$, $\mathbb F_4$ or $\mathbb F_2[\varepsilon]$ according as $2$ splits, is inert or ramifies. If $f$ is even, the generator $f\omega$ has minimal polynomial $\equiv X^2\pmod 2$. By Lemma 6.1(a), $E[2]$ is a faithful $R(E)$-module of $\mathbb F_2$-dimension $2$, which gives the counts.
(iii) By Deuring, $\operatorname{End}(E)$ is a maximal order in the quaternion algebra $B_{p,\infty}$, which is split at $2$ (see e.g. [17, Ch. 42]). Hence $\operatorname{End}(E)\otimes\mathbb Z_2\cong M_2(\mathbb Z_2)$, and so $R(E)=\operatorname{End}(E)/2\cong M_2(\mathbb F_2)$ by (a) and a cardinality count.

verify.py §6–7 checks the case distinction for $100$ orders. It checks $\mathcal O/2\mathcal O\cong M_2(\mathbb F_2)$ for the maximal orders $\mathbb Z\langle1,i,\tfrac{1+j}2,\tfrac{i+ij}2\rangle\subset(-1,-p)$ with $p\equiv3\ (4)$. For $p=3$ it also checks directly that $1$, $i:(x,y)\mapsto(-x,iy)$ and $(\pi-1)/2$ generate $M_2(\mathbb F_2)$ on $E[2]$ for $E:y^2=x^3-x$ over $\mathbb F_9$. $\square$

### 6.2. Consequences for t(S)

**Theorem 6.3 (= Theorem C(1)–(3)).** Let $(E,P,F,Q)$ be Lieberman data over $k$ and $S=S_{E,P,F,Q}$.
1. If $(E,P)$ or $(F,Q)$ is 2-split, then $t(S)$ is decomposable, $t(S)=t^2(S)\oplus t^3(S)$, and $CH^*(t^3(S))=0$. In particular this holds over $\overline{\mathbb F}_p$ whenever $E$ or $F$ is supersingular. The consequences listed in [1, Rem. 6.3] then hold for $S$; in particular $H^3_{\rm nr}(S\times S,\mathbb Q_\ell/\mathbb Z_\ell(2))=0$ for all $\ell\neq p$.
2. Let $k=\overline{\mathbb F}_p$ and let $E,E'$ be supersingular. Then $t(S_{E,P,F,Q})\cong t(S_{E',P',F,Q})$ for all $P\in E[2]\setminus O$ and $P'\in E'[2]\setminus O$. Hence, if $E,F,E',F'$ are all supersingular, $I(S_{E,P,F,Q},S_{E',P',F',Q'})=(\mathbb Z/2)^2$ and $\operatorname{Hom}(t(S),t(S'))\cong(\mathbb Z/2)^3$.
3. If $R(E)\cong\mathbb F_4$, then $t(S_{E,P,F,Q})\cong t(S_{E,P',F,Q})$ for all $P,P'$. If $R(E)\cong\mathbb F_2[\varepsilon]$, the same holds for $\{P,P'\}=E[2]\setminus\{O,P_0\}$.

*Proof.* (1) By symmetry assume $(E,P)$ is 2-split, and choose $\varphi\in\operatorname{End}(E)$ of even degree with $\varphi(P)=P$. We may take $\varphi$ separable. If $\operatorname{char}k=p>0$, the Chinese remainder theorem gives $\operatorname{End}(E)/2p\cong\operatorname{End}(E)/2\times\operatorname{End}(E)/p$, so we may prescribe $\varphi$ modulo $2$ and in addition require $\varphi=1+p\psi$. Then $\deg\varphi=\deg(1+p\psi)=1+p\operatorname{tr}\psi+p^2\deg\psi\equiv1\pmod p$, so $\varphi$ is separable. The map $\varphi\times\mathrm{id}_F$ commutes with $\iota$, and with $\tau$ because $\varphi(P)=P$. It therefore induces a rational map $S\dashrightarrow S$ of degree $\deg\varphi$ (Lemma 6.6 below), and (R4) gives $(0,1)\in I(S,S)$. The remaining statements are [1, Lemma 6.2(c)] and [1, Rem. 6.3], which rests on [11, Cor. 6.4(a)].
(2) The supersingular $3$-isogeny graph over $\overline{\mathbb F}_p$ is connected [18], so there is an isogeny $\psi:E\to E'$ of odd degree; then $\psi|_{E[2]}$ is an isomorphism. By Lemma 6.2(iii) there is $\varphi_0\in\operatorname{End}(E)$ with $\varphi_0|_{E[2]}$ invertible and $\varphi_0(P)=\psi^{-1}(P')$; it has odd degree by Lemma 6.1(b). Then $\varphi=\psi\varphi_0$ has odd degree and $\varphi(P)=P'$, so $\varphi\times\mathrm{id}_F$ induces $S_{E,P,F,Q}\dashrightarrow S_{E',P',F,Q}$ of odd degree. Apply (R4). For the last claim, part (1) gives $I(S',S')=(\mathbb Z/2)^2$. Composing with an isomorphism $t(S)\cong t(S')$, whose $\tau$ is $(1,1)$, and using (R3), we get $I(S,S')\supseteq I(S',S')\circ(1,1)=(\mathbb Z/2)^2$.
(3) Lift an invertible element of $R(E)$ taking $P$ to $P'$ (Lemma 6.2) to an endomorphism $\varphi$ of odd degree, and argue as in (2). $\square$

**Example 6.4.** For $p\equiv3\pmod4$, $\lambda=-1$ is supersingular, since $\#E_{-1}(\mathbb F_p)=p+1$ (verify.py §7). Hence over $\overline{\mathbb F}_p$ the motive $t(S_{-1,\mu})$ is decomposable for **every** $\mu$, and $t(S_{-1,\mu})\cong t(S_{\lambda',\mu})$ for every supersingular $\lambda'$. Over $\mathbb C$, examples for Theorem 6.3(3) come from CM by $\mathbb Z[(1+\sqrt{-11})/2]$ (inert case) or by $\mathbb Z[\sqrt{-2}]$ (ramified case). In the latter case $1+\sqrt{-2}$ has degree $3$ and swaps the two points $P_1,P_2$; neither of these isomorphisms is induced by an automorphism of $E$.

### 6.3. The isogeny-induced part of I(S,S')

**Definition 6.5.** A rational map $f:S_\circ\dashrightarrow S_\bullet$ between Lieberman surfaces is *isogeny-induced* if it is induced by a morphism $h=t_c\circ M:A_\circ\to A_\bullet$, with $M$ an isogeny and $c\in A_\bullet(k)$, that maps $G_\circ$-orbits to $G_\bullet$-orbits. Let $I_{\rm isog}(S_\circ,S_\bullet)\subseteq I(S_\circ,S_\bullet)$ be the subgroup generated by the $\tau(\Gamma_f)$ for isogeny-induced $f:S_\circ\dashrightarrow S_\bullet$ and the $\tau(\Gamma_g^t)$ for isogeny-induced $g:S_\bullet\dashrightarrow S_\circ$.

**Lemma 6.6.** The morphism $h=t_c\circ M$ maps orbits to orbits iff $c\in A_\bullet[2]$ and one of the following holds.
- (diag) $M=a\times d$ with $a(P_\circ)=P_\bullet$ and $d(Q_\circ)=Q_\bullet$.
- (anti) $M(x,y)=(b(y),c'(x))$ with $b:F_\circ\to E_\bullet$, $c':E_\circ\to F_\bullet$, $b(Q_\circ)=P_\bullet$ and $c'(P_\circ)=Q_\bullet$.

In either case the induced map has degree $\deg M$.

*Proof.* By irreducibility, for each $g\in G_\circ$ there is $g'\in G_\bullet$ with $h\circ g=g'\circ h$. Let $L(g)\in\{\pm1,\pm D\}$ be the linear part, where $D=\operatorname{diag}(1,-1)$. Comparing linear parts gives $ML(g)=L(g')M$. For $g=\iota$ this forces $L(\iota')=-1$, so $\iota'=\iota$ and $2c=0$. For $g=\tau$, the cases $L(\tau')=\pm1$ would force $M$ to kill $\{0\}\times F_\circ$ or $E_\circ\times\{0\}$, which is impossible. If $L(\tau')=D$, write $M=\begin{psmallmatrix}a&b\\c'&d\end{psmallmatrix}$; then $MD=DM$ gives $2b=2c'=0$, so $M$ is diagonal. If $L(\tau')=-D$, then $MD=-DM$ gives $a=d=0$. Comparing translation parts gives the stated conditions on the $2$-torsion points. Conversely, such $h$ satisfy $h\iota=\iota h$ and $h\tau_\circ\in\{\tau_\bullet h,\ \iota\tau_\bullet h\}$. Finally $g\mapsto g'$ is an isomorphism $G_\circ\cong G_\bullet$, and the groups act generically freely, so the induced map has degree $\deg M$. $\square$

**Theorem 6.7 (= Theorem C(4)).** (i) $I_{\rm isog}(S_\circ,S_\bullet)$ is spanned by the following elements.
- $(1,1)$, if there is an isogeny-induced map of odd degree in either direction.
- $(0,1)$, if there is one of even degree $S_\circ\dashrightarrow S_\bullet$.
- $(1,0)$, if there is one of even degree $S_\bullet\dashrightarrow S_\circ$.

(ii) Write $R(E_\circ,E_\bullet)$ for the image of $\operatorname{Hom}(E_\circ,E_\bullet)$ in $\operatorname{Hom}(E_\circ[2],E_\bullet[2])$, and similarly for the other pairs of curves. A diagonal map $S_\circ\dashrightarrow S_\bullet$ of odd (resp. even) degree exists iff there are $r\in R(E_\circ,E_\bullet)$ and $r'\in R(F_\circ,F_\bullet)$ with $rP_\circ=P_\bullet$ and $r'Q_\circ=Q_\bullet$, both invertible (resp. not both invertible). The same holds for anti-diagonal maps, with $R(F_\circ,E_\bullet)$ and $R(E_\circ,F_\bullet)$.
(iii) $I_{\rm isog}(S,S)=(\mathbb Z/2)^2$ iff $(E,P)$ or $(F,Q)$ is 2-split. Otherwise $I_{\rm isog}(S,S)=\langle(1,1)\rangle$.

*Proof.* (i) follows from (R3), (R4) and Lemma 6.6. (ii) follows from Lemma 6.1(b) and the fact that any $r\neq0$ in $R(\cdot,\cdot)$ lifts to a nonzero isogeny. For (iii): an even diagonal self-map requires $a$ or $d$ to have even degree and fix $P$ (resp. $Q$). An even anti-diagonal self-map $(b,c')$ gives $bc'\in\operatorname{End}(E)$ of even degree with $bc'(P)=b(Q)=P$. In both cases some pair is 2-split. The converse is Theorem 6.3(1). $\square$

**Conjecture 6.8 (speculative).** If $k$ is not algebraic over a finite field, then $I(S,S)=I_{\rm isog}(S,S)$ for every Lieberman surface. In particular, $t(S_{\lambda,\mu})$ would be indecomposable for every non-CM complex $(\lambda,\mu)$. We have no evidence beyond the expectation in [1] that $t(S)$ is "usually" indecomposable, together with Theorem E. Over $\overline{\mathbb F}_p$ we make no prediction (cf. [1, Rem. 1.12]).

---

## 7. Specialization and countability (Theorem D)

**Proposition 7.1 (specialization).** Let $R$ be a DVR with fraction field $K$ and residue field $\kappa$, with $\operatorname{char}\kappa\neq2$. Let $\mathcal S,\mathcal S'$ be smooth projective $R$-schemes whose geometric fibres are Enriques surfaces. Identify the torsion cohomology of geometric generic and special fibres by cospecialization; the groups are $\mathbb Z/2$, so this is canonical. Then
$$I(\mathcal S_{\bar K},\mathcal S'_{\bar K})\subseteq I(\mathcal S_{\bar\kappa},\mathcal S'_{\bar\kappa}).$$
In particular, decomposability of $t$ and isomorphism $t\cong t'$ pass from the generic to the special fibre, while indecomposability and non-isomorphism pass from the special to the generic fibre.

*Proof.* A cycle $\Gamma$ on $(\mathcal S\times\mathcal S')_{\bar K}$ is defined over a finite extension $K_1$. Let $R_1$ be a DVR of $K_1$ dominating $R$ (Krull–Akizuki). Fulton's specialization map [19, §20.3] gives $\sigma(\Gamma)$ on the special fibre over the residue field $\kappa_1$ of $R_1$, and $cl(\sigma\Gamma)=\operatorname{sp}(cl\,\Gamma)$ under the proper smooth base change isomorphism [25, Cycle]. Since $\operatorname{sp}$ is compatible with pull-back, push-forward and cup product, $\tau(\sigma\Gamma)=\tau(\Gamma)$. $\square$

**Proposition 7.2.** For algebraically closed fields $k\subseteq k'$, $I(S,S')=I(S_{k'},S'_{k'})$.

*Proof.* The inclusion $\subseteq$ is clear. For $\supseteq$: a cycle over $k'$ is defined over a smooth integral $k$-algebra $A$. Its refined Gysin fibre [19, §10.1] at a $k$-point of $\operatorname{Spec}A$ has the same $\tau$, since $\tau$ is locally constant along the smooth connected base. $\square$

**Theorem 7.3 (countability).** Let $k$ be uncountable and algebraically closed of characteristic $\neq2$. Let $B$ be an integral variety over $k$ and $\mathcal S,\mathcal S'\to B$ smooth projective families of Enriques surfaces. For $v\in(\mathbb Z/2)^2$, the set
$$B_v=\{b\in B(k):v\in I(S_b,S'_b)\}$$
is a countable union of closed subvarieties. Hence the decomposable locus ($\mathcal S=\mathcal S'$, $v=(0,1)$) and the isomorphism locus ($v=(1,1)$) are either all of $B(k)$ or contained in a countable union of proper closed subvarieties.

*Proof.* The relative Hilbert scheme of $\mathcal S\times_B\mathcal S'$ has countably many components, each projective over $B$. On a component $H$ parametrizing subschemes of dimension $2$, the cycle class of the universal family restricts on fibres to the fundamental classes [19, §10.1]. Hence $h\mapsto\tau([Z_h])$ is locally constant. Since $I(S_b,S'_b)$ is generated by the $\tau([V])$ with $V$ integral, and every element of $(\mathbb Z/2)^2$ is a sum of at most two generators, $B_v$ is a countable union of images of connected components of $H_1\times_BH_2$, or of $H_1$, on which the relevant sum of $\tau$'s equals $v$. These images are closed by properness. $\square$

**Corollary 7.4 (= Theorem D).** Let $k_0$ be any algebraically closed field of characteristic $\neq2$. Suppose $t(S_{\lambda_0,\mu_0})$ is indecomposable for some $\lambda_0,\mu_0\in k_0$, or that $t(S_{\lambda_0,\mu_0})\not\cong t(S_{\lambda_0',\mu_0'})$ for some $\lambda_0,\mu_0,\lambda_0',\mu_0'\in k_0$. Then the same holds for very general complex parameters.

*Proof.* In characteristic $p$, lift $s_0,t_0$ to the Witt vectors $W(k_0)$; this is a DVR since $k_0$ is perfect. The construction of Lemma 4.3(c) gives a smooth projective Lieberman family over $W(k_0)$. By Proposition 7.1 the property holds over $\overline{\operatorname{Frac}W(k_0)}$, which has characteristic $0$. In characteristic $0$, the parameters lie in a countable algebraically closed subfield, which embeds in $\mathbb C$; then apply Proposition 7.2. Finally, apply Theorem 7.3 to the Lieberman family over $T_{\mathbb C}$, resp. to $T_{\mathbb C}\times T_{\mathbb C}$. $\square$

**Remark 7.5.** By Proposition 7.1, the decomposability results of Theorem 6.3 in characteristic $p$ say nothing about characteristic $0$. Conversely, a single indecomposable example over $\overline{\mathbb F}_p$ would settle the question over $\mathbb C$ for very general Lieberman surfaces, even though, as noted in [1, Rem. 1.12], the valuative methods of [1] are unavailable over $\overline{\mathbb F}_p$.

---

## 8. Limits of degeneration arguments (Theorem E)

Throughout this section, $K$ is a field with a discrete valuation $v$, residue field $\kappa$ with $\operatorname{char}\kappa\neq2$, and $s,t\in K\setminus\{0,\pm1\}$. The surface $S=S_{s^2,t^2}$, its function field
$$K(S)=K(z,w)\big(\sqrt{A_1A_2},\sqrt{A_1B_1B_2}\big)$$
and the representatives $(A_1)$ and $(z+2s,w+2t)$ of $\alpha$ and $\beta$ are all defined over $K$, and Proposition 4.1 and Theorem 4.2 hold after base change to $\bar K$.

**Lemma 8.1 (good reduction gives nothing).** Suppose $S$ has a smooth proper model $\mathcal S$ over $\mathcal O_K$. Let $c\in H^i(S_{K},\mu_2^{\otimes j})$ be a class that extends to $\mathcal S$; after a finite extension this holds for $\alpha$ and $\beta$, by proper smooth base change as in [1, proof of Cor. 3.3]. Then, for every divisorial valuation $w$ of $K(S)$ extending $v$, $c$ is unramified at $w$ and its specialization lies in $H^i_{\rm nr}(\kappa(w)/\kappa)$. Hence hypothesis (iii) of [1, Prop. 3.2] fails for $\alpha_S$ at every model of $S$.

*Proof.* Let $w'$ be a divisorial valuation of $\kappa(w)/\kappa$ and $V$ the composite valuation ring. Since $\mathcal S$ is proper, $V$ has a centre on $\mathcal S$, so $c|_V$ is defined. Its image in $\kappa(w)$ factors through $H^i(\mathcal O_{w'})$. $\square$

**Definition 8.2.** For $\epsilon\in\{0,1\}^2$, let $v_\epsilon$ be the Gauss valuation of $K(z,w)$ in the variables $(z/\lambda^{\epsilon_1},w/\mu^{\epsilon_2})$. These are the Gauss valuations of the explicit model attached to the parameters $(\lambda^{\pm1},\mu^{\pm1})$, which describe the same pointed curves; the radicands change only by squares. A *Gauss point* of $S$ is an extension of some $v_\epsilon$ to $K'(S)$, for $K'/K$ finite. The *type* of $\lambda$ is $g$ if $v(\lambda)=v(\lambda-1)=0$, $1$ if $v(\lambda-1)>0$, $0$ if $v(\lambda)>0$, and $\infty$ if $v(\lambda)<0$; similarly for $\mu$. Type $1$ means that $E$ has multiplicative reduction and $P$ reduces into the identity component. Types $0$ and $\infty$ mean that $P$ reduces to the node.

**Theorem 8.3 (= Theorem E).** Let $w$ be a Gauss point of $S$ over $K'\supseteq K(\sqrt{-\lambda},\sqrt{-\mu},\sqrt{2s},\sqrt{2t})$. Then each of $(A_1)$, $(z+2s)$ and $(w+2t)$ either is the class of a $w$-unit or is trivial in the completion at $w$. In particular $\alpha_S$ and $\beta_S$ are unramified at $w$. Write $\bar\alpha_w$ and $\bar\beta_w$ for the specializations, and $\bar\kappa(w)=\operatorname{Frac}(\bar\kappa\otimes_\kappa\kappa(w))$.
(a) If $\lambda$ or $\mu$ has type $0$ or $\infty$, then $\bar\alpha_w=0$.
(b) If both types lie in $\{g,1\}$ and are not both $g$, then: $w$ is the unique Gauss point; $e(w/v)=1$; $\kappa(w)$ is a biquadratic extension of $\kappa'(z,w)$; $\bar\kappa(w)$ is purely transcendental over $\bar\kappa$; and $\bar\alpha_w\neq0$, so it is ramified at some divisorial valuation of $\bar\kappa(w)$. However, $\bar\beta_w=0$ in $\operatorname{Br}(\bar\kappa(w))$.
(c) If both types are $g$, then $E$ and $F$, and hence $S$, have good reduction, and $w$ is the generic point of the reduction.

Consequently: for any two Gauss points $w_1,w_2$, the specialization of $\Theta_{\lambda,\mu}$ at the product valuation $w_1\otimes w_2$ on $K'(S\times S)$ is $\bar\alpha_{w_1}\boxtimes\bar\beta_{w_2}$. This vanishes over $\bar\kappa$ unless both types are $g$, in which case it is $\Theta$ for the reduction of $S$. In particular, [1, Prop. 3.2] cannot be applied to $\Theta$ with $\xi=\beta_S$ and $\alpha_1=\alpha_S$, using models whose special fibres correspond to Gauss points. Nor can it be applied to the pull-back $\alpha_S\boxtimes\kappa(f_P)\boxtimes\kappa(g_Q)$ on $S\times E\times F$, as in [1, Cor. 3.4]: (b) requires the types to lie in $\{g,1\}$, and then $\kappa(f_P)$ is unramified (type $g$) or specializes to $0$ (type $1$) at the Gauss point of $E$, by Remark 8.5.

*Proof.* First, the units. Work in the coordinates of $v_\epsilon$. In types $g$, $1$ and $0$, $z+2s$ is a unit at the Gauss valuation, with reduction $z+2\bar s$. In type $\infty$, $z+2s=2s(1+z/2s)$ with $1+z/2s$ a $1$-unit, so $(z+2s)=(2s)=0$ in the completion. The same holds for $w+2t$. As for $A_1$: it is a unit in types $g$ and $1$, and in types $0$ and $\infty$ it is treated below.
(a) Type $0$: $A_1=z^2(1-4\lambda z^{-2})$ and the second factor is a $1$-unit at $v_\epsilon$, hence a square in the completion by Hensel's lemma. So $(A_1)$ is trivial at $w$. Type $\infty$: $A_1=-4\lambda(1-z^2/4\lambda)$ and $-4\lambda$ is a square in $K'$. The same argument applies to $(A_2)$, and $\eta(\alpha)=(A_1)=(A_2)$.
(b) Let $\bar s,\bar t$ be the reductions, with $\bar s=\pm1$ in type $1$. The reduced radicands $\bar r_1=\bar A_1\bar A_2$ and $\bar r_2=\bar A_1\bar B_1\bar B_2$ are independent modulo squares in $\bar\kappa(z,w)$ (verify.py §5, all sign choices). All their irreducible factors are linear and pairwise distinct in every characteristic $\neq2$. Indeed, $z-1-\bar s^2=z\pm2\bar s$ would force $\bar s=\pm1$, which is excluded in type $g$ and is built into the computation in type $1$. Hence the residue extension has degree $4=[K'(S):K'(z,w)]$, so $w$ is unique with $e=1$. Since $\bar A_1\notin\langle\bar r_1,\bar r_2\rangle$ modulo squares, $\bar\alpha_w\neq0$. Rationality comes from conic bundles: in case $(g,1)$, put $u^2=\bar A_1\bar B_1(w-2)$; then $\bar r_1\equiv\bar A_1(u^2+4\bar A_1\bar B_1)$, a conic over $\bar\kappa(z)$, which has a point by Tsen. Case $(1,g)$ is symmetric, and in case $(1,1)$ one gets $\bar r_1\equiv(z-2)(z+2)(u^2+4z+8)$. Since $H^1_{\rm nr}$ of a purely transcendental extension of $\bar\kappa$ is $0$, the class $\bar\alpha_w$ is ramified somewhere.

For $\bar\beta_w$ there are three cases. In case $(g,1)$: the relations $\bar r_1,\bar r_2\equiv1$ give $(w-2)\equiv\bar A_1\bar B_1$ and $(w+2)\equiv\bar B_1$. So $\bar\beta_w=(z+2\bar s,\bar B_1)$ or $(z+2\bar s,\bar A_1\bar B_1)$, a symbol from $\kappa(z)$, which vanishes over $\bar\kappa$ by Tsen. Case $(1,g)$ is symmetric, with all entries becoming functions of $w$. In case $(1,1)$: $z+2\equiv w-2$ and $z-2\equiv w+2$, so each of the four sign choices gives a symbol from $\kappa(z)$ or one of the form $(f,f)=0$. verify.py §5 checks all cases by square-class linear algebra.
(c) This is clear. For the consequence: the product valuation exists and is unique with residue field $\operatorname{Frac}(\kappa(w_1)\otimes\kappa(w_2))$; it is the generic point of the special fibre of the product of the two normal models. Specialization is compatible with external cup products. The types are attached to $S$, not to $w$. So if some Gauss point has $\bar\alpha\neq0$, then (b) applies to every Gauss point, there is only one, and $\bar\beta=0$ at it. $\square$

**Remark 8.4 (heuristic picture; not used).** At every point of the skeleton of the Tate models of $E\times F$, the decomposition group in $G$ determines what survives. The class $\alpha$ is detected only at points fixed by $\tau$ or $\iota\tau$; these lie on the "fold" locus of the K3 skeleton $S^2\to$ (disc or interval). There, if $P$ (resp. $Q$) is of identity type, $a_E$ (resp. $a_F$) is a square in the residue field, because $s\mapsto s+1/s$ is invariant. The class $\beta$ survives only at points where both Kummer classes are of node type, and there $\tau$ and $\iota\tau$ act freely. In these cases $\beta$ seems to be detected only through the topology of the skeleton (a "loop" phenomenon), which residue-field arguments à la Gabber [7], [22], [6] cannot see. This picture comes from a case-by-case analysis of the skeletal points that we have **not** written up or verified; we prove only the Gauss-point statement above. Detecting $\Theta$ will probably need a genuinely new input.

**Remark 8.5 (on [1, Cor. 3.3]).** The statement of [1, Cor. 3.3] assumes that $P$ "reduces to a smooth point". Its proof, however, writes $(E,P)=(E_\nu,P_\nu)$ with $v(\nu)>0$, using that "since $E_\nu$ has bad reduction, $v(\nu)\neq0$", and in that case $P_\nu=(0,0)$ reduces to the **node** of $y^2=x^2(x-1)$. Bad reduction also allows $v(\nu-1)>0$; then $P_\nu$ reduces into the smooth locus, i.e. the identity component. In that case $\kappa(f_P)$ specializes to the class of $x=S^2$ on the normalization of $y^2=x(x-1)^2$, which is $0$ (verify.py §4). So the argument does not apply, and we do not know whether the conclusion holds. The hypothesis should read: "$(E,P)\cong(E_\nu,P_\nu)$ with $v(\nu)\neq0$, i.e. $P$ reduces to the singular point of the nodal Legendre reduction." Definition 1.7(a) of [1] and all applications in [1] use exactly $v(\nu)\neq0$. Hence Theorem 1.8 and Examples 6.5–6.8 of [1] are unaffected; verify.py §3 rechecks their numerical conditions.

---

## 9. Limitations and open problems

1. **Main question.** We do not know a single Enriques surface with $t(S)$ indecomposable. Equivalently, over $\mathbb C$, we do not know one for which $S\times S$ fails the integral Hodge conjecture in degree $4$. By Corollary 4.6, for Lieberman surfaces this is the question whether $\Theta_{\lambda,\mu}\neq0$, which we cannot decide for any $(\lambda,\mu)$. By Theorem 6.3 it fails ($\Theta=0$) on the 2-split locus. Theorem 7.3 shows that $\Theta\neq0$ either holds for very general $(\lambda,\mu)$ or fails everywhere, and we do not know which.
2. **Scope of the obstructions.** Theorem 8.3 rules out Gabber-type arguments only at Gauss points, and Proposition 5.1 rules out only the listed divisors. Remark 8.4 is heuristic. Neither shows that $\Theta=0$.
3. **Conjecture 6.8** is speculative.
4. **Positive characteristic.** For Lieberman surfaces over $\overline{\mathbb F}_p$ with both curves ordinary and not 2-split, decomposability is undecided. As in [1, Rem. 1.12], we know no pair with $t(S)\not\cong t(S')$ over $\overline{\mathbb F}_p$.
5. **Non-isomorphism.** We prove no new non-isomorphism criteria. Using Theorem A with [1, Prop. 3.2] at Gauss points of type $(g,1)$ only recovers special cases of [1, Thm. 1.8(a)].
6. **Other surfaces.** Only Theorem A extends (Remark 3.4). We prove no analogue of Theorems C–E for Godeaux, Campedelli or Burniat surfaces.
7. **Garbagnati–Schütt and Beauville loci.** Beyond Corollary 4.5 we do not relate Lieberman surfaces with vanishing Brauer pullback to the families of [9] or to Beauville's lattice criterion [8].
8. **Dependence on [1].** Theorems A and C use [1, Prop. 4.3, Prop. 6.4, App. B], which we have not re-proved.

---

## References

[1] J. Huryn, W. C. Newman, *On the torsion in the Chow motive of an Enriques surface*, arXiv:2609.04360 (2026).

[2] S. Gorchinskiy, D. Orlov, *Geometric phantom categories*, Publ. Math. IHÉS 117 (2013) 329–349; arXiv:1209.6183.

[3] T. Jaklitsch, *Zero-cycles and Brauer groups on certain Enriques surfaces*, arXiv:2610.19307 (2026).

[4] J.-L. Colliot-Thélène, C. Voisin, *Cohomologie non ramifiée et conjecture de Hodge entière*, Duke Math. J. 161 (2012) 735–801; arXiv:1005.2778.

[5] O. Benoist, J. C. Ottem, *Failure of the integral Hodge conjecture for threefolds of Kodaira dimension zero*, Comment. Math. Helv. 95 (2020) 27–35; arXiv:1802.01845.

[6] H. A. Diaz, *On the integral Hodge conjecture for varieties with trivial Chow group*, Math. Proc. Cambridge Philos. Soc. 175 (2023) 433–443; arXiv:2204.13818.

[7] J.-L. Colliot-Thélène, *Exposant et indice d'algèbres simples centrales non ramifiées* (with an appendix by O. Gabber), Enseign. Math. 48 (2002) 127–146.

[8] A. Beauville, *On the Brauer group of Enriques surfaces*, Math. Res. Lett. 16 (2009) 927–934; arXiv:0902.3721.

[9] A. Garbagnati, M. Schütt, *Enriques surfaces: Brauer groups and Kummer structures*, Michigan Math. J. 61 (2012) 297–330; arXiv:1006.4952.

[10] A. N. Skorobogatov, D. Valloni, *Enriques involutions and Brauer classes*, Nagoya Math. J. 251 (2023) 606–621; arXiv:2202.08030.

[11] B. Kahn, *Torsion order of smooth projective surfaces* (with an appendix by J.-L. Colliot-Thélène), Comment. Math. Helv. 92 (2017) 839–857; arXiv:1605.01762.

[12] A. Vishik, *Torsion motives*, Int. Math. Res. Not. (2023) 20252–20295; arXiv:2106.11382.

[13] K. Sato, T. Yamazaki, *Torsion birational motives of surfaces and unramified cohomology*, J. Inst. Math. Jussieu 24 (2025) 2283–2315; arXiv:2309.00430.

[14] S. Schreieder, *Refined unramified cohomology of schemes*, Compos. Math. 159 (2023) 1466–1530; arXiv:2010.05814.

[15] S. Bloch, A. Kas, D. Lieberman, *Zero cycles on surfaces with $p_g=0$*, Compositio Math. 33 (1976) 135–145.

[16] H. Inose, M. Mizukami, *Rational equivalence of 0-cycles on some surfaces of general type with $p_g=0$*, Math. Ann. 244 (1979) 205–217.

[17] J. Voight, *Quaternion Algebras*, Grad. Texts in Math. 288, Springer, 2021.

[18] A. Pizer, *Ramanujan graphs and Hecke operators*, Bull. Amer. Math. Soc. 23 (1990) 127–137.

[19] W. Fulton, *Intersection Theory*, 2nd ed., Springer, 1998.

[20] J. H. Silverman, *The Arithmetic of Elliptic Curves*, 2nd ed., Springer, 2009.

[21] V. Guletskiĭ, *The Bloch conjecture*, arXiv:2512.12451 (2025).

[22] A. Auel, V. Suresh, *Failure of the local-global principle for isotropy of quadratic forms over function fields*, Algebra Number Theory 18 (2024) 1497–1513.

[23] A. N. Skorobogatov, Yu. G. Zarhin, *The Brauer group of Kummer surfaces and torsion of elliptic curves*, J. reine angew. Math. 666 (2012) 115–140.

[24] J.-L. Colliot-Thélène, A. N. Skorobogatov, *The Brauer–Grothendieck Group*, Ergeb. Math. Grenzgeb. 71, Springer, 2021.

[25] P. Deligne et al., *Cohomologie étale (SGA 4½)*, Lecture Notes in Math. 569, Springer, 1977.

---

## Appendix. Computational verification

The supplementary script `verify.py` (Python 3 with sympy) performs 93 checks, all passing, organized as follows.
- §1: translation by $P$, the $G$-action, the invariants $z,w,D,\Upsilon$ and their relations, and independence of the radicands.
- §2: local expansions of $a_E$ at $O$ and $P$, and the squareness of all tame symbols in Lemma 4.3.
- §3: the 2-isogeny and $\lambda^*$ (via Vélu and $j$-invariants), and the numerical conditions in [1, Ex. 6.5–6.8].
- §4: the reduction of $\kappa(f_P)$ in the two nodal degenerations (Remark 8.5).
- §5: all Gauss-point cases of Theorem 8.3, via square-class linear algebra, plus the conic-bundle identities.
- §6–7: $\mathcal O/2\mathcal O$ for 100 imaginary quadratic orders; quaternion maximal orders modulo $2$ for eight primes; an explicit computation of $R(E)$ for $y^2=x^3-x$ over $\mathbb F_9$; supersingularity of $\lambda=-1$.
- §8: the $\mathbb F_2$-linear algebra of the configurations and of $I_{\rm isog}$.
- §9: the symbol identities of Proposition 5.1.
