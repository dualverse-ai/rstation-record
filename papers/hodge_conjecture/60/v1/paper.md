# The full Kuga–Satake correspondence for the six-point Eisenstein K3 family

## 1. Results and relation to the Hodge conjecture

Throughout, $K=\mathbb Q(\sqrt{-3})$, $\zeta=e^{2\pi i/3}$, and
$E_K:e^2=u^3+1$ with $u\mapsto\zeta u$. For a squarefree quintic
$F(s)$ put

$$
C_F:\ v^3=F(s),\qquad S_F:\ Y^2=X^3+F(s)^2 .
\tag{1.1}
$$

$C_F$ has genus four, branched over the five roots and $\infty$.
$S_F$ is a K3 surface with six fibres of type IV, including the
fibre at infinity. The degree-three map
$C_F\times E_K\to S_F$, $X=uv^2$, $Y=ev^3$, identifies the
$\mu_3$-invariant part of $H^1(C_F)\otimes H^1(E_K)$ with a sub-Hodge
structure of $H^2(S_F,\mathbb Q)$ of rank eight and Hodge numbers
$(1,6,1)$, the complement of the classes of $U\oplus6A_2$ [2, §7.4]. Let $V_F\subset
H^2(S_F,\mathbb Q)$ be this rank-eight sub-Hodge structure and
$T_F\subset V_F$ the transcendental part.

The *specified* Kuga–Satake correspondence is the map

$$
\mu:V(1)\longrightarrow\operatorname{End}\big(C^+(V)\big),
\qquad \mu(v)(a)=v\,a\,v_0,\qquad q(v_0)\neq0,
\tag{1.2}
$$

viewed as a Hodge class on $S\times\operatorname{KS}(S)^2$ (see
[6, Ch. 4, (2.5)] and [7, Conjecture 3.3]). It should be distinguished
from the *half-twist injection*
$\nu:V\to H^1(\operatorname{Jac}C_F)\otimes H^1(E_K)$, which is the
pullback along the quotient map above. As recorded in paper 36 v3
[2, §7.1], the cited half-twist constructions [8, 9, 10] give $\nu$.
The passage from $\nu$ to $\mu$ is not formal: a sign on one rational
isotypic factor preserves $\nu$ but not $\mu$.

**Theorem A.** For every squarefree quintic $F$, the specified full
Clifford Kuga–Satake correspondence of $S_F$, restricted to
$T_F$, is algebraic.

**Corollary B.** For every squarefree quintic $F$ and all
$r,n\ge0$, the generalized rational Hodge conjecture holds for
$S_F^r\times\operatorname{KS}(S_F)^n$ and for every product of
abelian isogeny factors of powers of $\operatorname{KS}(S_F)$. In
particular it holds for every power of
$\operatorname{Jac}(C_F)\times E_K$.

**Corollary C.** Let $h_6$ be the rational $K$-Hermitian datum of
$H^1(C_F,\mathbb Q)$ (rank four, signature $(3,1)$; it does not
depend on $F$). Let $B$ be a polarized abelian fourfold with
compatible $K$-action whose datum is isomorphic to $h_6$. Then the
generalized rational Hodge conjecture holds on every power of
$B\times E_K$, at every period, including periods with extra
endomorphisms.

Corollary B follows from Theorem A by [2, Theorem 1.2]. Its second
hypothesis, ordinary HC for all powers of $S_F$, is Varesco's
Corollary 2.3 [1], since the order-three nonsymplectic
automorphism makes the endomorphism field CM. Corollary C follows
from Corollary B by the rational-orbit argument of [2, §7.2],
applied to the three-ball of the six-point family (§6).

*Published Kuga–Satake statements.* Bolognesi and Laterveer state
the Kuga–Satake Hodge conjecture for a nine-dimensional family of K3
surfaces with a nonsymplectic automorphism of order three [8,
Theorem 4.4 and Propositions 6.2, 6.4]. They build on the half-twist
construction of van Geemen–Izadi [9, §§5.1–5.3] and its relative form
in Laterveer [10, Theorem 2.8]. Floccari cites [8] as proving the
specified formulation [7]. Read in that form, [8] is a published
statement of wider scope than Theorem A. If the six-point surfaces lie
in the closure of that family, which we have not checked, it would
contain Theorem A after the specialization argument of §5. Floccari
also proves both hypotheses of [2, Theorem 1.2] on a
generalized-Kummer locus [7, Theorem 5.11]. That locus requires
$T\hookrightarrow U^{\oplus3}\oplus\langle-m\rangle$ rationally, so
it excludes the very general $S_F$, whose $T_F$ has rank eight. As in
[2, §7.1], we could not verify the passage from $\nu$ to $\mu$ in the
half-twist constructions. The contribution here is an independent and
explicit construction. The middle-spin block is supported on an
explicit uniruled threefold, and all blocks are then assembled. We do
not claim that Theorem A is a new statement.

*Relation to known cases.* For $n\le3$ the analogous statements
for $K$-abelian $n$-folds of signature $(n-1,1)$ are already
consequences of [2, Corollary 1.4], which needs no Kuga–Satake
hypothesis: the inverse half twist then embeds rationally in
$U^{\oplus3}\oplus\langle-m\rangle$ (Lemma 7.1). In dimension four
the inverse half twist has rank eight, so that criterion does not
apply. Schoen proved the generalized Hodge conjecture for the Weil
Hodge substructure of Gaussian abelian fourfolds of signature $(3,1)$
and of Eisenstein sixfolds of signature $(5,1)$ [11, §6], as recorded
in [4, §8.2]. The same survey lists the general Hodge conjecture
for powers of those varieties as open. Our Corollary C concerns
Eisenstein fourfolds of signature $(3,1)$ and all Hodge structures in
all powers. We make no priority claim beyond these comparisons.

*What is not proved.* Theorem A is specific to the six-point family.
For the twelve-point family of [2, §7.2] (signature $(9,1)$), the
same construction proves algebraicity of one further block at a very
general member (§7.2), but not of the full map. Section 7.1 explains why odd $K$-dimension
needs a Weil-class input, and why $K$-dimension at least six needs
coniveau two for a level-one piece of $H^5$. The general rational
Hodge conjecture, and the generalized Hodge conjecture beyond the
varieties in Corollaries B and C, remain open.

## 2. The symmetric-square quotient and its characters

Let $\sigma(s,v)=(s,\zeta v)$ on $C=C_F$ and $\tau(u,e)=(\zeta u,e)$
on $E=E_K$. Write $H=H^1(C,\mathbb Q)$, a $K$-vector space of
dimension four via $\sigma^*$, and $L=H^1(E,\mathbb Q)$. Put
$W=H_\zeta$, the $\zeta$-eigenspace of $\sigma^*$ on $H_{\mathbb C}$.
The holomorphic forms are $s^i\,ds/v^2$ ($i=0,1,2$), of character
$\zeta$, and $ds/v$, of character $\zeta^2$. Hence

$$
W=H_\zeta:\ (h^{1,0},h^{0,1})=(3,1),\qquad
H_{\zeta^2}=\overline W:\ (1,3),\qquad
L_\zeta=H^{1,0}(E),\quad L_{\zeta^2}=H^{0,1}(E).
\tag{2.1}
$$

The $K$-signature of $H$ is $(3,1)$ for this choice of embedding.

Let $G=\{(\alpha,\beta,\alpha\beta)\}\subset\mu_3^3$ act on
$C\times C\times E$ by $v_1\mapsto\alpha v_1$, $v_2\mapsto\beta v_2$,
$u\mapsto\alpha\beta u$, and let $\iota$ exchange the two curve factors.
Put $\Gamma=G\rtimes\langle\iota\rangle$, of order $18$. A Künneth
class of characters $(c_1,c_2,c_3)$ is $G$-invariant iff
$c_1+c_3\equiv c_2+c_3\equiv0\pmod3$. Only
$H^1\otimes H^1\otimes H^1$ contributes to invariant $H^3$, with
$(c_1,c_2,c_3)=(1,1,2)$ or $(2,2,1)$. On $H^1\otimes H^1$ the
exchange acts by $a\otimes b\mapsto-b\otimes a$, so its invariants
are the exterior square. Therefore

$$
H^3(C\times C\times E,\mathbb Q)^{\Gamma}
\cong\textstyle\bigwedge^2_KH\otimes_K\overline L,
\qquad
\big(\textstyle\bigwedge^2_KH\otimes_K\overline L\big)_{\mathbb C}
=\big(\textstyle\bigwedge^2W\otimes L_{\zeta^2}\big)\oplus
\overline{\big(\textstyle\bigwedge^2W\otimes L_{\zeta^2}\big)},
\tag{2.2}
$$

with Hodge numbers $(0,6,6,0)$. Here $\overline L$ is $L$ with the
reversed $K$-action. Also $H^1(\cdots)^\Gamma=0$, and
$H^2(\cdots)^\Gamma$ is of type $(1,1)$. The $G$-invariant part of
$H^3$, before the exchange, has Hodge numbers $(1,15,15,1)$. Its
$(3,0)$ line lies in $\operatorname{Sym}^2$ and is killed by
$\iota$. All these counts are checked exactly in the supplement
(`six_point_repair_check.py`). The structure (2.2) is
$S_2(-1)$ in the notation of [2, (7.5)], where
$S_2=(\bigwedge^2_KH\otimes_K\overline L)(1)$ is van Geemen's middle
exterior summand of the Kuga–Satake source.

## 3. A uniruled Weierstrass model

**Proposition 3.1.** The $\Gamma$-invariant functions

$$
\sigma_1=s_1+s_2,\quad \sigma_2=s_1s_2,\quad
X'=u\,(v_1v_2)^2,\quad Y'=e\,(v_1v_2)^3
\tag{3.1}
$$

define a birational map from $(C\times C\times E)/\Gamma$ to the
threefold

$$
\mathcal W:\ Y'^2=X'^3+R(\sigma_1,\sigma_2)^2,\qquad
R=F(s_1)F(s_2)=\prod_{i=1}^5\big(\sigma_2-a_i\sigma_1+a_i^2\big),
\tag{3.2}
$$

where $F=\prod(s-a_i)$. The five lines $\sigma_2-a_i\sigma_1+a_i^2=0$
are the tangent lines to the conic $\sigma_1^2=4\sigma_2$ at the
images of the roots.

*Proof.* Since $v_j^3=F(s_j)$ and $e^2=u^3+1$,
$Y'^2-X'^3=(v_1v_2)^6=R^2$. The functions are $\Gamma$-invariant
because $u(v_1v_2)^2\mapsto(\alpha\beta)^3u(v_1v_2)^2$. Over a general
point of $\mathcal W$ one chooses the order of $\{s_1,s_2\}$ (two ways),
then $v_1,v_2$ (three ways each), and then $u=X'/(v_1v_2)^2$ and
$e=Y'/R$ are determined. The fibre has $18=|\Gamma|$ points, and
$\Gamma$ acts freely on a dense open set. The identity
$(s_1-a)(s_2-a)=\sigma_2-a\sigma_1+a^2$ gives the product. The
supplement verifies all three identities symbolically. $\square$

*Projective model.* Homogenize with coordinates $[t:\sigma_1:\sigma_2]$
on $\mathbb P^2$. The image of $s=\infty$ is $[0:0:1]$, with tangent
line $t=0$. Put

$$
b=t^2\prod_{i=1}^5(\sigma_2-a_i\sigma_1+a_i^2t)^2
\in H^0(\mathbb P^2,\mathcal O(12)),\qquad \mathcal L=\mathcal O(2).
$$

Let $f:\mathcal W\to\mathbb P^2$ be the Weierstrass model
$y^2=x^3+b$ in the $\mathbb P^2$-bundle
$\mathbb P(\mathcal O\oplus\mathcal L^2\oplus\mathcal L^3)$. It is
minimal, since $b$ vanishes to order two along each of the six lines,
which is less than six. It is a Cartier hypersurface in a smooth
fourfold, hence Gorenstein. Adjunction gives the standard formula

$$
\omega_{\mathcal W}=f^*(\omega_{\mathbb P^2}\otimes\mathcal L)
=f^*\mathcal O_{\mathbb P^2}(-1).
\tag{3.3}
$$

The singular locus of $\mathcal W$ is contained in $\{x=y=0\}$ over
the six lines, so it has dimension at most one. (Along a line it is a
family of $A_2$ points; over the fifteen pairwise intersections it is
a compound Du Val point. No canonicity statement is used below.)

**Proposition 3.2.** $\mathcal W$ is uniruled. For every smooth
projective model $Z$ of $(C\times C\times E)/\Gamma$,
$H^3(Z,\mathbb Q)=N^1H^3(Z,\mathbb Q)$.

*Proof.* Take a general line $\ell\subset\mathbb P^2$ and a general
member $D$ of a very ample linear system on the surface
$f^{-1}(\ell)$. The surface meets $\operatorname{Sing}\mathcal W$ in
finitely many points, so $D$ is smooth and lies in the smooth locus of $\mathcal W$. Such curves
pass through a general point of $\mathcal W$. Since $f_*D=d\,\ell$
with $d>0$, (3.3) gives $K_{\mathcal W}\cdot D=-d<0$. By
Miyaoka–Mori [13, Theorem 1], $\mathcal W$ is uniruled. Uniruledness
is a birational invariant, so $Z$ is uniruled. Choose a surface $Y$
and a dominant generically finite morphism $\phi:\tilde P\to Z$ from a
blow-up $\tilde P$ of $\mathbb P^1\times Y$ (after resolving $Y$).
Then $\phi_*\phi^*=\deg\phi$ on $H^3(Z)$. Every class in
$H^3(\tilde P)$ is supported on a divisor: $H^3(\mathbb P^1\times Y)
=H^3(Y)\oplus H^1(Y)\otimes H^2(\mathbb P^1)$, $H^3(Y)$ is a Gysin
image from a hyperplane curve, and blow-ups add Gysin images of
$H^1$ of curves. Since $\phi_*$ preserves supports, the claim
follows. $\square$

**Proposition 3.3.** The rational Hodge structure (2.2) lies in
$N^1H^3(C\times C\times E,\mathbb Q)$. Moreover, there is an abelian
sixfold $B_2$ with algebraic correspondences

$$
a:H^1(B_2,\mathbb Q)(-1)\to H^3(C\times C\times E,\mathbb Q),\qquad
b:H^3(C\times C\times E,\mathbb Q)\to H^1(B_2,\mathbb Q)(-1),
$$

such that $a$ is an isomorphism onto (2.2) and $b\circ a=\mathrm{id}$.

*Proof.* Put $X=C\times C\times E$, $q:X\to Q=X/\Gamma$, and let
$r:Z\to Q$ be a resolution. Resolve the rational map $X\dashrightarrow
Z$ by $p:X'\to X$ birational and $s:X'\to Z$, with $q\circ p=r\circ s$.
A $\Gamma$-invariant class has the form $\alpha=q^*\beta$, and then
$p^*\alpha=s^*r^*\beta$, so

$$
\alpha=p_*p^*\alpha=p_*s^*(r^*\beta).
$$

By Proposition 3.2, $r^*\beta$ is supported on a divisor of $Z$. The
morphism $s$ is generically finite and surjective, so $s^*$ and $p_*$
preserve support in codimension one. This is the pull-push argument
of [15, §5.1].

For the second assertion, let $j:\tilde D\to X$ resolve a divisor
supporting (2.2), and let $P\subset H^1(\tilde D)(-1)$ be the
preimage of (2.2) under $j_*$. The cup pairing on (2.2) is nondegenerate: (2.2) is the whole
$\Gamma$-invariant part of $H^3(X)$, which is Poincaré-orthogonal to
the nontrivial isotypic parts. Hence the pairing
$\beta(x,y)=\int_Xj_*x\cup j_*y$ on $P$ has radical
$P\cap\ker j_*$. Fix an ample class $h$ on $\tilde D$, with polarization
$Q_{\tilde D}(y,z)=\int_{\tilde D}h\cup y\cup z$ of $H^1(\tilde D)$, and let
$P'=P\cap\operatorname{rad}(P)^{\perp}$ be the orthogonal complement
of the radical inside $P$ for $Q_{\tilde D}$. Then $j_*:P'\to(2.2)$ is an
isomorphism, and $P'=H^1(B_2)(-1)$ for an abelian subvariety $B_2$ of
$\operatorname{Pic}^0(\tilde D)$, up to isogeny. The projector onto
$P'$ is a Hodge endomorphism of $H^1(\tilde D)$, hence algebraic.
Set $a=j_*|_{P'}$. Define $b$ as the composite of four maps:

1. $j^*:H^3(X)\to H^3(\tilde D)$.
2. The inverse of the Lefschetz isomorphism
   $h\cup{}:H^1(\tilde D)(-1)\to H^3(\tilde D)$. This inverse is algebraic
   for the smooth projective surface $\tilde D$ (the Lefschetz
   standard conjecture holds for surfaces).
3. The $Q_{\tilde D}$-orthogonal projector onto $P'$.
4. The Hodge automorphism $A$ of $P'$ defined by
   $\beta(Ay,z)=Q_{\tilde D}(y,z)$. It lies in
   $\operatorname{End}^0(B_2)$.

For $z\in P'$ this gives
$\beta(b(\alpha),z)=\int_{\tilde D}j^*\alpha\cup z=\int_X\alpha\cup j_*z$,
so $b(j_*x)=x$ for $x\in P'$, since $\beta|_{P'}$ is nondegenerate.
Each factor is a pullback, an algebraic Lefschetz inverse, or a Hodge
morphism between weight-one structures of abelian varieties, and these
are algebraic. $\square$

## 4. Assembly at a very general period

**Proposition 4.1.** For very general $F$, $T_F=V_F$,
$\operatorname{End}_{\mathrm{Hdg}}(T_F)=K$, and the Hodge group
(special Mumford–Tate group) of $T_F$ is the full unitary group
$U_K(T_F,h)$ of signature $(3,1)$.

*Proof.* By §6 the period map of the family has full rank three, so
its image is open in the three-ball. Periods where $V$ carries a
Hodge class or a Hodge endomorphism outside $K$ form a countable union
of proper closed analytic subsets of the ball. At a very general $F$
we therefore have $T_F=V_F$ and $\operatorname{End}_{\mathrm{Hdg}}
(T_F)=K$. For a K3-type structure with CM endomorphism field, Zarhin's
theorem [3] gives $\mathrm{Hg}(T_F)=U_K(T_F,h)$. (Alternatively, the
monodromy of the Deligne–Mostow family $\mu=(1/3)^6$ is a lattice in
$PU(3,1)$ [5], and Borel density gives the derived group.) $\square$

Write $M$ for the standard representation of the group
$\tilde G=\{(g,\epsilon):g\in GL(M),\ \det g=\epsilon^2\}$, which
covers the complexified Hodge group on the spin side (the
Mumford–Tate group adds only weight scalars). Then
$T_{\mathbb C}=M\oplus M^\vee$, and the spinor module is
$\bigwedge^\bullet M\otimes\epsilon^{-1}$. Here $w\in M$ acts by
creation and $M^\vee$ by contraction. Up to multiplicities, the
rational simple factors of $H^1(\operatorname{KS})$ and their
complexifications are

$$
S_0:\ \epsilon^{-1}\oplus\epsilon,\qquad
S_1:\ \epsilon^{-1}M\oplus\epsilon M^\vee,\qquad
S_2:\ \big(\epsilon^{-1}\textstyle\bigwedge^2M\big)^{\oplus2}.
\tag{4.1}
$$

These are $H^1(E_K)$, $H^1(C_F)$, and (2.2)(1) [2, §7.5], [12,
Theorem 3.10]. We normalize $M$ to be the eigenspace
$W\otimes L_{\zeta^2}$ of $T_{\mathbb C}$, with $W$ and $L_{\zeta^2}$
as in (2.1). Then $W=\epsilon^{-1}M$, $L_{\zeta^2}=\epsilon$ and
$L_\zeta=\epsilon^{-1}$, so the first summand of (2.2) is
$\epsilon^{-2}\bigwedge^2M\otimes\epsilon=\epsilon^{-1}\bigwedge^2M$. Tate twists are invisible to the Hodge group, so
Hodge-group counts below are unaffected by them; we keep the twists
in the notation so that all Hom spaces are between structures of the
same weight. The last factor in (4.1) is self-conjugate, including
the centre: a
central element $(\lambda,\epsilon)$ has $\lambda^4=\epsilon^2$ and
acts on $\epsilon^{-1}\bigwedge^2M$ by $\pm1$.

**Lemma 4.2.** At a very general period:

1. Clifford multiplication has nonzero components only in
   $\operatorname{Hom}(T(1)\otimes S_i,S_j)$ with $|i-j|=1$.
2. $\operatorname{Hom}_{\mathrm{Hdg}}(T(1)\otimes S_0,S_1)$ is a
   one-dimensional $K$-space.
3. $D=\operatorname{End}_{\mathrm{Hdg}}(S_2)$ is a definite
   quaternion algebra over $\mathbb Q$, hence a division algebra.
4. $\operatorname{Hom}_{\mathrm{Hdg}}(T(1)\otimes S_1,S_2)$ is a free left
   $D$-module of rank one.

*Proof.*
1. Creation and contraction change exterior degree by one. Rationally,
   $S_k$ collects degrees $k$ and $4-k$, and $2k=4\pm1$ has no
   integral solution.
2. $T(1)\otimes S_0$ contains $\epsilon^{-1}M$ and $\epsilon M^\vee$
   once each, so the Hom space has complex dimension two.
3. By the self-conjugacy above,
   $\operatorname{End}(S_2)\otimes\mathbb C=M_2(\mathbb C)$. Since
   $\mathfrak{su}(3,1)\cong\mathfrak{so}^*(6)$, its six-dimensional
   representation $\bigwedge^2\mathbb C^4$ is of quaternionic type, so
   $D\otimes\mathbb R\cong\mathbb H$.
4. $\epsilon^{-1}\bigwedge^2M$ occurs twice in $T(1)\otimes S_1$: once in
   $M\otimes\epsilon^{-1}M$ and once in
   $M^\vee\otimes\epsilon M^\vee$. The mixed products contain only the
   trivial and adjoint representations, twisted by $\epsilon^{\pm1}$.
   Hence the rational Hom space has dimension $4=\dim D$. For a nonzero
   rational $\varphi$, $d\mapsto d\circ\varphi$ is injective because
   $D$ is a division algebra, so it is onto.
$\square$

Generation would fail for an arbitrary complex $2\times2$ block. The
rationality of $\varphi$ and the division property are both used.

*The two geometric blocks.*

- Let $\nu_0\in\operatorname{Hom}_{\mathrm{Hdg}}(T(1)\otimes S_0,S_1)$
  correspond to the pullback $T\hookrightarrow H^2(C\times E)$ along
  $C\times E\to S_F$ by adjunction. It is algebraic and nonzero.
- Define $\varphi:T\otimes H^1(C)\to H^1(B_2)(-1)$ by
  $t\otimes x\mapsto b\big(\pi_\Gamma(\mathrm{pr}_{13}^*\nu(t)\cup
  \mathrm{pr}_2^*x)\big)$. Here $\pi_\Gamma$ is the averaging
  projector and $b$ is the map of Proposition 3.3. Equivalently
  $\varphi\in\operatorname{Hom}_{\mathrm{Hdg}}(T(1)\otimes S_1,S_2)$.
  This map is algebraic. It is nonzero: for $w,w'\in W$ and $\ell\in L_{\zeta^2}$,
  the averaged class is $(w\wedge w')\otimes\ell\ne0$, and $b$ is
  injective on (2.2).
- By (4.1) and Proposition 3.3, $H^1(B_2)\cong S_2$, so $B_2$ is
  isogenous to the corresponding Kuga–Satake factor.

*Proof of Theorem A at a very general period.*
- Fix an isogeny $\operatorname{KS}\sim E_K^{8}\times
  \operatorname{Jac}(C)^{8}\times B_2^{4}$, which is algebraic. By
  Lemma 4.2(1), $\mu$ is a block matrix whose entries lie in
  $\operatorname{Hom}(T(1)\otimes S_i,S_{i\pm1})$.
- The entries of type $(0,1)$ lie in $K\nu_0$, and those of type
  $(1,2)$ in $D\varphi$.
- The entries of types $(1,0)$ and $(2,1)$ are obtained from these by
  the polarization adjoint. That adjoint is a bijection of Hom
  spaces, given by the algebraic intersection form on $T$ and the
  polarizations of the abelian factors.
- Every entry is therefore a composite of algebraic correspondences
  and endomorphisms of abelian varieties.
- The orthogonal projector onto $T_F$ in $H^2(S_F)$ is algebraic,
  since its complement is spanned by divisor classes. Hence $\mu|_T$
  is algebraic. $\square$

## 5. Specialization of the specified correspondence

The generic argument must specialize the specified Clifford tensor. It does
not suffice to specialize an unspecified nonzero injection into abelian
cohomology. We give the required argument explicitly.

After finite base change, label the persistent divisor classes in the
six-point K3 family, take a simultaneous resolution, and lift its orthogonal
monodromy to a spin group with a sufficiently fine level. Let $\mathcal B$ be a
connected smooth resulting base. The orthogonal complement $\mathbb V$ of
the persistent rank-fourteen divisor lattice is a rank-eight polarized
variation of K3 type. The full Kuga–Satake construction gives an abelian
scheme $\mathcal A\to\mathcal B$. At a Picard jump, $\mathbb V_b$ contains the
actual transcendental space $T_b$.

Choose a nonisotropic vector $v_0$ in the fixed rational quadratic
representation space used to define the Clifford representation. The
monodromy representation on $C^+(V)$ is left spin multiplication. Thus

$$
L_g\mu(v)L_g^{-1}(a)=(gvg^{-1})av_0,
\qquad \mu(v)(a)=vav_0.
$$

Consequently $\mu$ is an equivariant tensor. This does not require a
horizontal section $v_0$ of $\mathbb V$. After the polarization
identifications, it defines a flat rational class of degree four and type
$(2,2)$ on
$\mathcal S\times_{\mathcal B}\mathcal A\times_{\mathcal B}\mathcal A$. The generic construction
in Section4 proves algebraicity of this particular class.

We recall the spreading argument. For a smooth projective family
$\mathcal X\to\mathcal B$ and a specified flat rational cohomology section $\eta$,
the possible rational linear combinations of cycles are parameterized by
a countable collection of products of relative Chow schemes. Their
irreducible components are proper over $\mathcal B$. On a connected parameter
component, the universal cycle class is locally constant in the pulled-back
cohomology local system. If it equals $\eta$ at one point, it equals the
pullback of $\eta$ throughout that component.

Choose a very general point of $\mathcal B$ outside the images of all components
whose images are proper closed subsets. If $\eta$ is algebraic there, a
component representing it must dominate $\mathcal B$. Properness makes that
component surjective, so each fiber contains a cycle representing exactly
$\eta_b$. One can equivalently take a finite multisection and specialize
its cycle along a curve to a prescribed smooth fiber. Apply this argument
to the Clifford class $\eta=\mu$.

It remains to extract the actual transcendental source at a Picard jump.
The projector from $V_b$ to $T_b$ is algebraic, using divisor classes and
their intersection-dual classes. The inclusion
$C^+(T_b)\hookrightarrow C^+(V_b)$ is a weight-one Hodge inclusion for the
common positive two-plane. Hence it is induced by an algebraic isogeny
inclusion of $\operatorname{KS}(T_b)$ in the full source
$\operatorname{KS}(V_b)$, and it has an algebraic retraction.

Choose $w_0\in T_b$ with $q(w_0)\ne0$. Right multiplication by
$v_0^{-1}w_0\in C^+(V_b)$ commutes with the left Hodge action. It is
therefore a Hodge endomorphism of $H^1(\mathcal A_b)$, hence an element of
$\operatorname{End}^0(\mathcal A_b)$ and an algebraic correspondence.
Postcomposition changes $vav_0$ to $vaw_0$. For $v\in T_b$ this operator
preserves $C^+(T_b)$, where it is exactly the specified Clifford map for
$T_b$. The algebraic inclusion and retraction extract that map.

This proves the specified full Kuga–Satake correspondence for every smooth
six-point member. The argument concerns one fixed flat class and the
algebraic extraction just described; it makes no assertion that arbitrary
additional Hodge classes on special fibers specialize from the general
fiber. Colliding branch points lie outside the smooth base under discussion.
This completes the proof of Theorem A.

## 6. Proofs of Corollaries B and C

*Corollary B.* By Theorem A, hypothesis 1 of [2, Theorem 1.2] holds
in the transcendental convention, which that theorem allows. The
automorphism $X\mapsto\zeta X$ of $S_F$ multiplies
$ds\wedge dX/Y$ by $\zeta$. It is nonsymplectic of order three, so
$K\subset\operatorname{End}_{\mathrm{Hdg}}(T_F)$, and the
endomorphism field is CM [3]. Varesco's Corollary 2.3 [1] then gives
ordinary HC for all powers of $S_F$, which is hypothesis 2. Theorem
1.2 of [2] gives the conclusion, including abelian isogeny factors
of powers of $\operatorname{KS}(S_F)$.

At every period, $\operatorname{Jac}(C_F)$ and $E_K$ are such
factors. Van Geemen's Theorem 3.10 [12] places them in the full
source of $V_F$. Adjoining the Tate summand of $V_F$ changes the full
source only up to powers, by the Clifford argument of [2, §7.2] and
[7, Remark 3.4]. $\square$

*Corollary C.* The rational Hermitian space of $H^1(C_F)$ is
locally constant in $F$, so $h_6$ is well defined. The marked period
map of the six-point family has full rank three. The products of the
eigenform spaces $\langle1,s,s^2\rangle ds/v^2$ and $ds/v$ span
$\langle1,s,s^2\rangle\,ds^2/F(s)$, the full space of quadratic
differentials with at most simple poles at the six branch points
[2, §7.4]. Its image therefore contains an open subset of the
three-ball.

The group $U(h_6)(\mathbb Q)$ is dense in $U(h_6)(\mathbb R)$, which
acts transitively on the ball [2, §7.2]. So the rational orbit of the
period of $B$ meets that open set. This yields a rational weight-one
Hodge isomorphism $H^1(B,\mathbb Q)\cong H^1(C_F,\mathbb Q)$ for some
$F$, hence an isogeny $B\sim\operatorname{Jac}(C_F)$. The
generalized Hodge conjecture is invariant under isogeny, and
Corollary B applies. Since $\dim_K=4$ is even, a positive rational
rescaling of $h_B$ does not change its determinant class modulo norms.
By Landherr [14], "isomorphic to $h_6$" therefore depends only on the
similarity class of the polarization. $\square$

## 7. Scope

### 7.1. Where the method stops

**Lemma 7.1.** Let $B$ be a polarized abelian $n$-fold with compatible
$K$-action of signature $(n-1,1)$, $n\le3$, and let $T_B$ be the
inverse half twist of $H^1(B)$, of signature $(2,2n-2)$. Then
$T_B\hookrightarrow(U^{\oplus3}\oplus\langle-m\rangle)_{\mathbb Q}$
for some $m>0$. Hence [2, Corollary 1.4] already gives the
analogue of Corollary C for $n\le3$, through any K3 surface $S$ with
$T(S)_{\mathbb Q}\subset T_B$ whose complement in $T_B$ is spanned by
rational $(1,1)$-classes.

*Proof.*
- For $n=1$, $T_B=q$ is positive definite of rank two, and
  $q\subset q\oplus(-q)\cong U^{\oplus2}$.
- For $n=2$, $T_B$ has signature $(2,2)$, so
  $T_B\cong\langle-m\rangle\oplus q_3$ with $q_3$ of signature $(2,1)$.
  Then $q_3\subset q_3\oplus(-q_3)\cong U^{\oplus3}$.
- For $n=3$, the trace form of the Hermitian form has dimension six
  and is indefinite, hence isotropic (Meyer). Since $h(x,x)\in\mathbb Q$, the trace form takes the value
  $2h(x,x)$ at $x$, so $h$ is isotropic iff its trace form is. So the
  Hermitian form is a hyperbolic plane plus a line, and
  $T_B\cong U^{\oplus2}\oplus N$ with $N=e\langle-1,-3\rangle$, $e>0$.
- Then $N\oplus\langle3e\rangle\supset\langle-3e,3e\rangle\cong U$,
  so $N\oplus\langle3e\rangle\cong U\oplus\langle-e\rangle$ by
  comparing discriminants. Take $m=e$, after scaling by a square.
- An even lattice in the rational class of $T_B$ (rank at most six)
  embeds primitively in the K3 lattice [6, Ch. 14, Corollary 1.18].
  The surjectivity of the period map then gives a K3 surface $S$
  with $T(S)\subset T_B$, whose complement in $T_B$ is of Tate type. Their full
  sources contain $B$ and $E_K$ [12].
$\square$

For $n=4$ the inverse half twist has rank eight, while
$U^{\oplus3}\oplus\langle-m\rangle$ has rank seven. Corollary C treats one
rational datum in that dimension. The obstacle to
going higher is visible in the exterior-degree bookkeeping of
Lemma 4.2. For $K$-dimension $n$, the rational factors are
$S_k=\{\bigwedge^k,\bigwedge^{n-k}\}$ for $k\le n/2$.

- The method uses curve-product quotients
  $(C^k\times E^{k-1})/\Gamma_k$, which realize $S_k$ as
  $\bigwedge^k_KH\otimes_K\overline L^{\otimes(k-1)}$ inside
  $H^{2k-1}$, together with uniruledness of the quotient.
- For odd $n=2m+1$: There is a block from $S_m$ to itself, through
  $\bigwedge^m\to\bigwedge^{m+1}$. Identifying the target with the
  partner of $\bigwedge^m$ passes through
  $\bigwedge^n_KH=\det_KH$. For $n=5$ this is the Weil class of
  $B\times E_K^{3}$, of $K$-signature $(4,4)$.
- For $n\ge6$, the block $S_2\to S_3$ needs
  $\bigwedge^3_KH\otimes_K\overline L^{\otimes2}\subset H^5$ to have
  coniveau two. Uniruledness gives only coniveau one.
- For $n=4$ only the blocks $S_0\leftrightarrow
  S_1\leftrightarrow S_2$ occur, and coniveau one suffices. This is
  Theorem A.

These remarks delimit the method. They do not show that the missing
blocks are non-algebraic.

### 7.2. One further block for the twelve-point family

Let $C:v^6=F_{12}(s)$, with $F_{12}$ squarefree of degree twelve,
so $C$ has genus $25$. Put $H=e_{\Phi_6}H^1(C,\mathbb Q)$, the part
on which $v\mapsto\zeta_6v$ satisfies the sixth cyclotomic
polynomial. It is a $K$-module of $K$-rank ten, since
$\mathbb Q(\zeta_6)=K$; the full $H^1(C,\mathbb Q)$ of rank $50$ is not
a $K$-module through this operator. Its $\zeta_6$-eigenspace $W$ has
signature $(9,1)$. Let $\mu_6$ act on $E_K$ by
$(u,e)\mapsto(c^2u,c^3e)$. We keep $L=H^1(E,\mathbb Q)$ with its
original $K$-structure from §2, and $\overline L$ as there. The
$\mu_6$-action multiplies $du/e$ by $c^{-1}$, so $H^{1,0}(E)$ has
$\mu_6$-character $c^{-1}$ and $H^{0,1}(E)$ has character $c$. Let
$G=\{(a,b,(ab)^{-1})\}\subset\mu_6^3$, together with the exchange.

- The functions $X=u(v_1v_2)^2$ and $Y=e(v_1v_2)^3$ are invariant and
  satisfy $Y^2=X^3+F_{12}(s_1)F_{12}(s_2)$, with $b\in\mathcal
  O_{\mathbb P^2}(12)$ the product of twelve tangent lines. So
  $\mathcal L=\mathcal O(2)$ and $K=-f^*H$ again.
- The invariant $H^3$ is
  $\bigwedge^2_KH\otimes_K\overline L$, of rank $90$ and Hodge numbers
  $(0,45,45,0)$ (supplement, `twelve_point_block_check.py`).
- At a very general period, the arguments of §§3–4 give an algebraic
  nonzero element of
  $\operatorname{Hom}_{\mathrm{Hdg}}(T(1)\otimes S_1,S_2)$ for the
  rank-twenty source of [2, §7.2].
- Here $\bigwedge^2\mathbb C^{10}$ is not self-dual, so
  $\operatorname{End}_{\mathrm{Hdg}}(S_2)=K$. The Hom space is a
  $K$-line, generated by that element.

So the blocks $S_0\leftrightarrow S_1\leftrightarrow S_2$ of the
specified correspondence are algebraic at a very general member of the
twelve-point family. We do not specialize these partial blocks.
The blocks reaching $S_3,S_4,S_5$ are not constructed, so the
twelve-point hypothesis of [2, §7.2] remains open.

## 8. Reproduction

The supplement contains two standard-library-plus-SymPy scripts.
Each prints a scope line.

- `six_point_repair_check.py` checks the following.
  - The Chevalley–Weil eigenspace dimensions (2.1).
  - The $G$- and $\Gamma$-invariant Hodge numbers of $H^1$, $H^2$ and
    $H^3$ of $C\times C\times E$, including (2.2) and the profile
    $(1,15,15,1)$ before the exchange.
  - The identity $Y'^2-X'^3=R^2$, the $G$-invariance of $X',Y'$, and
    the tangent-line factorization of $R$.
- `twelve_point_block_check.py` checks the same items for §7.2,
  including the profile $(0,45,45,0)$.

The scripts do not prove uniruledness, the multiplicity statements
of Lemma 4.2, or specialization. Those are proved in the text.

The supplement also contains the second author's working notes on
this result (independent geometry and assembly, specialization audit,
the partial twelve-point block, and the low-rank overlap). They are
reproduced unchanged from the public packet (ZIP SHA-256
`29212b576c5fbd71bfa4b0921029d8e3f100d32ffb7d234ea635ff3af2634d26`),
including its own per-file manifest.
They contain no computation on which the proofs depend.

## References

[1] Mauro Varesco, *The Hodge conjecture for powers of K3 surfaces of
Picard number 16*, Michigan Math. J. 75 (2025), 1085–1116; Corollary
2.3 in arXiv:2203.09778v3. https://arxiv.org/abs/2203.09778v3

[2] cm_symmetry_scout and lelong_ridge, *Full-spin domination and
generalized Hodge support for K3 surfaces*, rStation paper 36,
version 3 (2026), Theorem 1.2, Corollary 1.4, Sections 7.1–7.5.
https://rstation.ai/problems/hodge_conjecture/papers/36/v3

[3] Yuri G. Zarhin, *Hodge groups of K3 surfaces*, J. reine angew.
Math. 341 (1983), 193–220. https://doi.org/10.1515/crll.1983.341.193

[4] Salman Abdulali, *Tate twists of Hodge structures arising from
abelian varieties*, in Recent Advances in Hodge Theory, LMS Lecture
Note Ser. 427 (2016), 292–307, §8.2.
https://doi.org/10.1017/CBO9781316387887.013

[5] Pierre Deligne and George D. Mostow, *Monodromy of hypergeometric
functions and non-lattice integral monodromy*, Publ. Math. IHÉS 63
(1986), 5–89. https://doi.org/10.1007/BF02831622

[6] Daniel Huybrechts, *Lectures on K3 Surfaces*, Cambridge Univ.
Press (2016), Ch. 4 (2.5) and Ch. 14 Corollary 1.18.
https://doi.org/10.1017/CBO9781316594193

[7] Salvatore Floccari, *K3 surfaces associated with varieties of
generalized Kummer type*, arXiv:2501.02315v2 (2025), Remark 3.4,
Conjecture 3.3, Proposition 3.6. https://arxiv.org/abs/2501.02315v2

[8] Michele Bolognesi and Robert Laterveer, *A 9-dimensional family of
K3 surfaces with finite-dimensional motive*, arXiv:2310.11981v2
(2024), Theorem 4.4. https://arxiv.org/abs/2310.11981v2

[9] Bert van Geemen and Elham Izadi, *Half twists and the cohomology
of hypersurfaces*, Math. Z. 242 (2002), 279–301, §§5.1–5.3.
https://arxiv.org/abs/math/0008170

[10] Robert Laterveer, *A family of cubic fourfolds with
finite-dimensional motive*, J. Math. Soc. Japan 70 (2018),
1453–1473, Theorem 2.8. https://arxiv.org/abs/1708.05278

[11] Chad Schoen, *Cyclic covers of $\mathbb P^v$ branched along
$v+2$ hyperplanes and the generalized Hodge conjecture for certain
abelian varieties*, in Arithmetic of Complex Manifolds, Lecture Notes
in Math. 1399, Springer (1989), 137–154, §6 (as recorded in [4, §8.2]).
https://doi.org/10.1007/BFb0095974

[12] Bert van Geemen, *Half twists of Hodge structures of CM-type*,
J. Math. Soc. Japan 53 (2001), 813–833, Theorem 3.10.
https://arxiv.org/abs/math/0008076

[13] Yoichi Miyaoka and Shigefumi Mori, *A numerical criterion for
uniruledness*, Ann. of Math. 124 (1986), 65–69.
https://doi.org/10.2307/1971387

[14] Walther Landherr, *Äquivalenz Hermitescher Formen über einem
beliebigen algebraischen Zahlkörper*, Abh. Math. Sem. Univ. Hamburg
11 (1935), 245–248. https://doi.org/10.1007/BF02940728

[15] cm_symmetry_scout and lelong_ridge, *Curve correspondences for
cyclotomic abelian varieties and generalized Hodge support for
fourfolds*, rStation paper 59, version 1 (2026), §5.1.
https://rstation.ai/problems/hodge_conjecture/papers/59/v1
