# Spin(7)-instantons and Chern classes on non-projective quaternionic 4-tori

## 1. Introduction

On a compact Kähler manifold that is not projective, a rational Hodge class need not be a Chern class of a coherent sheaf. Voisin constructed a complex torus of dimension 4 with a nonzero Hodge class in degree 4 on which $c_2(\mathcal F)=0$ for every coherent sheaf $\mathcal F$ [1, Thm. 1]. Her criterion [1, Prop. 1] concerns a compact Kähler manifold $X$ of dimension $n\ge3$ and has three hypotheses:

- (H1) $\mathrm{NS}(X)=0$;
- (H2) $X$ has no proper closed analytic subset of positive dimension;
- (H3) $\mathrm{Hdg}^4(X)$ is orthogonal to $[\omega]^{n-2}$ for some Kähler class $[\omega]$.

Under these hypotheses the proof is a linear argument on $c_2$, by induction on the rank.

This paper studies the same question on a family of 4-tori where (H2) holds and (H1) and (H3) fail. The tori are not projective. The paper makes no claim about the Hodge conjecture, which is known for abelian fourfolds [2, Cor. 1.6.1].

**The tori.** Let $T_u$ be a very general member of the twistor family of a flat hyperkähler 4-torus of quaternionic type. It is built from a quaternion algebra $D$ over $\mathbb Q(\sqrt2)$ whose corestriction to $\mathbb Q$ is $M_2(B)$, with $B$ an indefinite quaternion division algebra over $\mathbb Q$ (Section 2). Then $\mathrm{NS}(T_u)=\mathbb Q w$ with $w$ of signature $(4,4)$, so $T_u$ is not projective, and
$$\mathrm{Hdg}^4(T_u)=\mathbb Q w^2\oplus K_5,$$
where $K_5$ has dimension 5 and is irreducible under $B^\times$. We show that $T_u$ contains no curves, surfaces or threefolds (Lemma 2.3, which rests on Verbitsky's trianalyticity theorem [3, Cor. 2.12]). So (H2) holds. (H1) fails because $w\ne0$. (H3) fails for every Kähler class, because $K_5\otimes\mathbb R$ contains classes represented by nonzero positive $(2,2)$-forms (Section 7).

**Method.** Muñoz [4] showed that if $E$ is a polystable bundle of rank $r$ on a flat Kähler 4-torus, then $\beta(E)=\Delta(E)/2r$, with $\Delta=c_1^2-2r\,\mathrm{ch}_2$, satisfies a quadratic inequality on a 6-dimensional space $A^+$ of real 2-forms (inequality (3.1) below). The inequality comes from rotating the complex structure inside $\mathrm{Spin}(7)$. On $T_u$ every coherent sheaf has $c_1\in\mathbb Q w$, so all slopes vanish at the Kähler metrics on the *wall* $w\cdot\omega^3=0$. Hence every torsion-free sheaf is semistable at every wall metric, and its Jordan–Hölder factors do not depend on the wall metric. Let $M\subset\mathrm{Hdg}^4(T_u)\otimes\mathbb R$ be the set of classes that satisfy (3.1) at every flat Kähler metric on the wall.

**Theorem A.** Let $u$ be very general. Then $\beta(\mathcal F)\in M$ for every coherent sheaf $\mathcal F$ of positive rank on $T_u$.

For bundles whose Jordan–Hölder factors on the wall are locally free, Theorem A follows from Muñoz's inequality and an extension formula. For general sheaves we extend the inequality to stable reflexive sheaves with finite singular set (Proposition 3.7). The inputs are the admissible Hermitian–Einstein metrics of Bando and Siu [5], Price's monotonicity for them as stated in [6], which makes the Chern–Weil currents closed (compare [7, Prop. 2.3.1]), and the finiteness of singular sets, which follows from Lemma 2.3.

**Theorem B.** $M=\mathbb R_{\ge0}\,(-w^2)+\overline{\mathrm{cone}}\{[Z_\ell]:\ell\in\mathbb P^1(\mathbb R)\}$.

Here $[Z_\ell]\in K_5\otimes\mathbb R$ is the class of the linear foliation of $T_u$ by the 4-planes $A\otimes\ker\ell$ of Section 2. These planes are quaternionic, so the leaves are complex for every $u$. In coordinates in which $K_5\otimes\mathbb R$ is the space of real binary quartics, $[Z_\ell]$ is the fourth power $\ell^4$. So $M\cap K_5$ is the cone $\Sigma_4$ of sums of fourth powers of real linear forms, and $M=\{c\,w^2+\kappa:\ c\le0,\ \kappa\in\Sigma_4\}$.

**Consequences** (Section 7).

1. $\Sigma_4$ is strictly smaller than the cone of nonnegative quartics, which is the bound that the curvature of a hyperholomorphic bundle gives. The difference contains a nonempty open set and therefore rational classes $\kappa\in K_5$. For such $\kappa$, no coherent sheaf on $T_u$ has $\beta\in\mathbb R w^2+\mathbb R_{>0}\kappa$.
2. The extreme rays of $\Sigma_4$ are the real points of the conic attached to $B$, which has no rational point. So no rational class spans an extreme ray. The rational boundary points of rank 2 are Galois traces over real quadratic subfields of $B$.
3. Every class of $M$ that lies in $K_5$ lies on the boundary of $M$.
4. For every $z\in B$ of reduced trace $0$ with $z^2<0$, the torus $T_u$ is of Weil type for the field $\mathbb Q(z)$, as Voisin's example is, and its Weil classes form a plane $W_z\subset K_5$. These planes span $K_5$. Every nonzero real Weil class is an indefinite quartic. So for a coherent sheaf $\mathcal F$ of positive rank, the $K_5$-component of $\beta(\mathcal F)$ never lies in $W_z\otimes\mathbb R\setminus0$ (Proposition 7.8).

**What the paper does not do.** It constructs no sheaf, so it does not decide whether $K_5$ contains a Chern class of a coherent sheaf. Theorems A and B give a necessary condition only.

**A correction to [4].** Muñoz states the inequality for abelian varieties and extends it to tori that carry a rational primitive $(1,1)$-class [4, Prop. 20, Rem. 21]. One step of the proof is incomplete: the forms $\gamma\wedge\gamma$, $\gamma\in A^+$, do not detect the 15-dimensional summand $\omega\wedge\Lambda^{1,1}_0$ of the real $(2,2)$-forms. Proposition 3.2 gives a short proof that holds on every flat Kähler 4-torus, which proves the extension Muñoz conjectures after [4, Rem. 21]. The trace of the quadratic form equals $-12$ times $\beta\cdot\omega^2/\omega^4$ (Lemma 3.4), the Bogomolov inequality makes this nonpositive, and a rigorous form of Muñoz's Prop. 18 (Lemma 3.3) makes the form semidefinite.

**Organisation.** Section 2 sets up the tori and proves Lemma 2.3. Section 3 states Muñoz's inequality, gives the repair, and proves Theorem A. Section 4 proves a rank-2 lemma that gives the inclusion $\supseteq$ in Theorem B. Section 5 derives an asymptotic condition from metrics that degenerate along the wall. Section 6 proves Theorem B. Section 7 gives the quartic form and its consequences, and Section 8 discusses what a sheaf with nonzero $K_5$-part would have to look like. The supplement contains the scripts behind the numerical controls.

## 2. The tori

### 2.1 Construction

Let $F=\mathbb Q(\sqrt2)$ and $D=(-11,\,-(19+11\sqrt2))_F$. Both entries are negative at both real places, so $D$ is ramified there. Since $2$ is a square modulo $7$ and modulo $17$, both primes split in $F$. As $N_{F/\mathbb Q}(19+11\sqrt2)=119=7\cdot17$, the element $b=-(19+11\sqrt2)$ has valuation $1$ at one place $\mathfrak p_7$ above $7$ and at one place $\mathfrak p_{17}$ above $17$, and it is a unit at all other finite places. At $\mathfrak p_7$ the Hilbert symbol is the Legendre symbol of $-11\equiv3$ modulo $7$, which is $-1$. At $\mathfrak p_{17}$ it is the Legendre symbol of $-11\equiv6$ modulo $17$, which is also $-1$. At the other odd places both entries are units, or (at the inert prime $11$) $b\equiv3$ lies in $\mathbb F_{11}$ and is a square in the residue field $\mathbb F_{121}$. So $D$ is unramified there, and by parity it is also unramified above $2$. Hence $D$ is ramified exactly at the two real places, $\mathfrak p_7$ and $\mathfrak p_{17}$. The local invariants of $\mathrm{Cor}_{F/\mathbb Q}D$ are the sums of those of $D$ over the places above each prime of $\mathbb Q$. Hence $\mathrm{Cor}_{F/\mathbb Q}D\cong M_2(B)$, where $B$ is the indefinite quaternion division algebra over $\mathbb Q$ ramified at $7$ and $17$.

Let $G=\mathrm{Res}_{F/\mathbb Q}\mathrm{SL}_1(D)$. The norm map $D^\times\to(\mathrm{Cor}\,D)^\times$ gives an action of $G$ on $V_{\mathbb Q}=B^2$, the simple left $M_2(B)$-module, of dimension $8$. Over $\mathbb R$, $G(\mathbb R)=\mathrm{Sp}(1)\times\mathrm{Sp}(1)$ and
$$V_{\mathbb R}=A\otimes U,\qquad A=\mathbb H,\quad (a,b)\cdot q=aq\bar b,\qquad U=\mathbb R^2,$$
where $G(\mathbb R)$ acts trivially on the multiplicity space $U$. The commutant $\mathrm{End}_G(V_{\mathbb Q})$ is $B^{\mathrm{op}}$, and $B\otimes\mathbb R=\mathrm{End}(U)$.

For a unit imaginary quaternion $u$, let $L_u$ be left multiplication by $u$ on $A$. It is the action of $(u,1)\in G(\mathbb R)$, and it is a complex structure on $V_{\mathbb R}$. Fix the lattice $\Lambda=\mathcal O_B^2\subset V_{\mathbb Q}$ for a maximal order $\mathcal O_B$, and put
$$T_u=(V_{\mathbb R}/\Lambda,\ L_u).$$
With a $G(\mathbb R)$-invariant metric on $A$ and any inner product on $U$, the structures $L_i,L_j,L_k$ form a flat hyperkähler structure on $V_{\mathbb R}/\Lambda$, and $\{T_u\}$ is its twistor family. All statements below are invariant under isogeny. Hodge classes pull back, and so does polystability [4, Lemma 17]. So the choice of $\Lambda$ does not matter.

For $\ell\in U^*\setminus0$ let $P_\ell=A\otimes\ker\ell$. It is a real 4-plane, stable under every $L_u$, and $V_{\mathbb R}/P_\ell\cong A\otimes(U/\ker\ell)\cong A$. Let $\pi_\ell\colon V_{\mathbb R}\to A$ be the quotient map, and put
$$[Z_\ell]=\pi_\ell^*\mathrm{vol}_A\in\Lambda^4V_{\mathbb R}^*=H^4(T_u,\mathbb R),$$
where $\mathrm{vol}_A$ is the volume form of $g_A$ for the orientation induced by the complex structures $L_u$. This orientation does not depend on $u$, since $S^2$ is connected.

### 2.2 Hodge classes

The Hodge group $\mathrm{Hg}(T_u)$ is the smallest $\mathbb Q$-subgroup of $\mathrm{GL}(V_{\mathbb Q})$ whose real points contain $U(1)_u=\{\exp(tL_u)\}$. Since $U(1)_u\subset\mathrm{Sp}(1)\times1\subset G(\mathbb R)$, we have $\mathrm{Hg}(T_u)\subseteq G$. A rational class in $H^{2p}(T_u)$ has type $(p,p)$ if and only if it is fixed by $U(1)_u$, if and only if it is fixed by $\mathrm{Hg}(T_u)$.

**Lemma 2.1.** There is a countable union $N\subset S^2$ of nowhere dense closed sets such that $\mathrm{Hg}(T_u)=G$ for $u\notin N$.

*Proof.* Let $H\subsetneq G$ be a $\mathbb Q$-subgroup. The set of $u$ with $U(1)_u\subset H(\mathbb R)$ is closed. Suppose it contains an open set $O$. The circles $U(1)_u$, $u\in O$, generate $\mathrm{Sp}(1)\times1$, so $H(\mathbb R)\supseteq\mathrm{Sp}(1)\times1$, and $H_{\bar{\mathbb Q}}$ contains one of the two factors of $G_{\bar{\mathbb Q}}=\mathrm{SL}_2\times\mathrm{SL}_2$. The Galois group swaps the two factors, because $G$ is a restriction of scalars from the real quadratic field $F$. So $H_{\bar{\mathbb Q}}=G_{\bar{\mathbb Q}}$, a contradiction. There are countably many such $H$. $\square$

"Very general" means $u\notin N$. For the rest of the paper $u$ is very general unless stated otherwise.

**Lemma 2.2.** Let $u$ be very general.

1. $\mathrm{End}^0(T_u)=B^{\mathrm{op}}$, $V_{\mathbb Q}$ is an irreducible $G$-module, and $T_u$ is simple.
2. $\mathrm{NS}(T_u)=\mathbb Q w$, where $w=g_A\otimes\varepsilon_U$, $g_A$ is the invariant inner product on $A$ and $\varepsilon_U$ is an area form on $U$. The hermitian form of $w$ has signature $(2,2)$ over $\mathbb C$ (signature $(4,4)$ as a real form), so $T_u$ is not projective.
3. $\mathrm{Hdg}^4(T_u)=H^4_G:=(\Lambda^4V_{\mathbb Q}^*)^G$ has dimension $6$, and $H^4_G=\mathbb Q w^2\oplus K_5$ with $K_5=H^4_G\cap(w^2)^\perp$ of dimension $5$. Moreover $K_5\otimes\mathbb R=\Lambda^4A^*\otimes S^4U^*$ inside $\Lambda^4(A\otimes U)^*$, and $[Z_\ell]=\mathrm{vol}_A\otimes\ell^4$ lies in it.
4. $B^\times$ acts on $K_5$ absolutely irreducibly.
5. Every class in $H^4_G$ has type $(2,2)$ for every $L_{u'}$, $u'\in S^2$.

*Proof.* (1) The endomorphisms of $T_u$ are the rational endomorphisms of $V_{\mathbb Q}$ that commute with $\mathrm{Hg}(T_u)=G$. The group $G(\mathbb Q)$ spans $\mathrm{Cor}\,D$ (Burnside), so $\mathrm{End}_G(V_{\mathbb Q})=\mathrm{End}_{M_2(B)}(B^2)=B^{\mathrm{op}}$, a division algebra. Since $G$ is reductive, $V_{\mathbb Q}$ is semisimple, and a semisimple module with a division algebra of endomorphisms is irreducible. A subtorus of $T_u$ is given by a rational $L_u$-stable subspace, which is $\mathrm{Hg}$-stable, hence $0$ or $V_{\mathbb Q}$. (For non-projective tori, the fact that $\mathrm{End}^0$ is a division algebra does not by itself imply simplicity. The argument above uses the irreducibility of $V_{\mathbb Q}$.)

(2) $\Lambda^2(A\otimes U)^*=\Lambda^2A^*\otimes S^2U^*\oplus S^2A^*\otimes\Lambda^2U^*$. The first summand has no $G(\mathbb R)$-invariants, because $\Lambda^2A=\mathfrak{sp}(1)_L\oplus\mathfrak{sp}(1)_R$. The invariants of the second are $\mathbb R\,g_A\otimes\varepsilon_U$. For $x=a_1\otimes e_1+a_2\otimes e_2$ one gets $w(x,L_ux)=2g_A(a_1,ua_2)$. This quadratic form pairs $a_1$ with $a_2$ through an invertible matrix, so it has real signature $(4,4)$. A Kähler class would have a definite form, so $T_u$ is not projective.

(3) By Schur–Weyl duality, $\Lambda^4(A\otimes U)=\bigoplus_\lambda S_\lambda A\otimes S_{\lambda'}U$ over partitions $\lambda$ of $4$ with at most two columns: $\lambda=(1^4),(2,1,1),(2,2)$. The $\mathrm{SO}(4)$-invariants are $\Lambda^4A\otimes S^4U$ (dimension $5$), none from $S_{(2,1,1)}A$, and one line in $S_{(2,2)}A\otimes S_{(2,2)}U$ (dimension $1$). So $\dim H^4_G=6$. The exact computation over $\mathbb Q$ (script `invariants.py`) gives the same dimension, and also $\dim\mathrm{NS}(T_u)=1$. The class $w^2$ is $\mathrm{SL}(U)$-invariant, so it lies in the $S_{(2,2)}$ line. The wedge pairing is $\mathrm{GL}(A)\times\mathrm{GL}(U)$-equivariant with values in $\det(A)^{2}\otimes\det(U)^4$, and $S^4U\otimes\det(U)^2$ does not contain $\det(U)^4$. So the $S^4$ part is orthogonal to $w^2$, and $K_5\otimes\mathbb R=\Lambda^4A^*\otimes S^4U^*$. For $[Z_\ell]$: identify $U/\ker\ell$ with $\mathbb R$ through $\ell$. Then $\pi_\ell(a\otimes s)=\ell(s)\,a$, so $\pi_\ell^*\mathrm{vol}_A(a_1\otimes s_1,\dots,a_4\otimes s_4)=\mathrm{vol}_A(a_1,\dots,a_4)\prod_k\ell(s_k)$. This is the image of $\mathrm{vol}_A\otimes\ell^4$ under $\Lambda^4A^*\otimes S^4U^*\subset\Lambda^4(A\otimes U)^*$.

(4) $B^\times$ acts through $B\otimes\mathbb R=\mathrm{End}(U)$ on $S^4U^*$. As a representation of $\mathrm{PGL}_2$ this is $\mathrm{Sym}^2_0$ of the 3-dimensional adjoint representation, which is absolutely irreducible. $B^\times$ is Zariski dense in $\mathrm{GL}_1(B)$.

(5) $L_{u'}$ generates $U(1)_{u'}\subset\mathrm{Sp}(1)\times1\subset G(\mathbb R)$, which fixes $H^4_G$. $\square$

By (4), and because isogenies preserve the span of Chern characters of coherent sheaves, $\mathrm{ch}_2$ of coherent sheaves on $T_u$ spans either $\mathbb Q w^2$ or all of $H^4_G$.

### 2.3 No subvarieties

**Lemma 2.3.** For very general $u$, $T_u$ contains no analytic subvarieties of dimension $1$, $2$ or $3$.

*Proof.* By Lemma 2.2(5), every rational $(p,p)$-class on $T_u$ is $\mathrm{Sp}(1)_L$-invariant, and $\mathrm{Sp}(1)_L$ is the group $\mathrm{SU}(2)$ induced on cohomology by the flat hyperkähler structure $(L_i,L_j,L_k)$. So $T_u$ is of general type with respect to this structure in Verbitsky's sense [3, Def. 2.10]. Hence every closed analytic subvariety $Z\subset T_u$ is trianalytic [3, Cor. 2.12], so its tangent spaces at smooth points are quaternionic and $\dim_{\mathbb R}Z$ is divisible by $4$ [3, Rem. 2.9]. This rules out curves and threefolds.

Let $S$ be an irreducible surface. On a connected component of $S_{\mathrm{reg}}$ the second fundamental form $\mathrm{II}$ is symmetric and complex-linear for $I=L_i$ and $J=L_j$, since the metric is Kähler for both. Hence
$$\mathrm{II}(Iu,Jv)=IJ\,\mathrm{II}(u,v)=K\,\mathrm{II}(u,v),\qquad\mathrm{II}(Iu,Jv)=\mathrm{II}(Jv,Iu)=JI\,\mathrm{II}(v,u)=-K\,\mathrm{II}(u,v),$$
so $\mathrm{II}=0$. In the flat torus that component is therefore an open piece of a leaf $x+P$, where $P$ is a quaternionic, hence $L_u$-complex, real 4-plane. The intersection of $S$ with the leaf $x+P\cong\mathbb C^2$ is analytic and contains an open set, so it is the whole leaf. As $S$ is compact, it contains the closure of the leaf, which is a real subtorus of dimension at least $4$, with equality only if $P$ is rational. So $P$ is a rational $L_u$-stable subspace, and $x+P$ projects to a 2-dimensional subtorus. This contradicts Lemma 2.2(1). $\square$

The input from [3] is Thm. 2.8 there, which is stated for every compact hyperkähler manifold, including tori. An alternative to the first step is [3, Prop. 2.11]: for all but countably many $u$, every integral $(p,p)$-class of $T_u$ is $\mathrm{SU}(2)$-invariant.

**Corollary 2.4.** For very general $u$, the singular set of a reflexive sheaf on $T_u$ is finite. Every torsion sheaf on $T_u$ is supported at finitely many points, so it has $c_1=0$ and $\mathrm{ch}_2=0$. For every torsion-free sheaf $\mathcal F$, $\mathcal F^{**}/\mathcal F$ is supported at points, and $\mathrm{ch}_2(\mathcal F)=\mathrm{ch}_2(\mathcal F^{**})$.

*Proof.* The singular set of a reflexive sheaf has codimension at least $3$, so it has dimension at most $1$. The supports of torsion sheaves and of $\mathcal F^{**}/\mathcal F$ are analytic of dimension at most $3$ and at most $2$, respectively. By Lemma 2.3 all of these are finite. A sheaf supported at points has $\mathrm{ch}$ concentrated in $H^8$. $\square$

**Remark 2.5** (Voisin's hypotheses). On $T_u$, (H2) holds by Lemma 2.3, and (H1) fails because $\mathrm{NS}=\mathbb Q w$. (H3) fails for every Kähler class $\omega$. Indeed $[Z_\ell]\in K_5\otimes\mathbb R$, and $[Z_\ell]\cdot\omega^2>0$ because $[Z_\ell]$ is represented by a nonzero positive $(2,2)$-form (Lemma 7.4). Since $K_5$ is dense in $K_5\otimes\mathbb R$, some rational class in $K_5$ has nonzero pairing with $\omega^2$.

### 2.4 The CM fibre

Let $\iota\in D$ be the generator with $\iota^2=-11$. In each real completion of $D$ it is $\sqrt{11}$ times a unit imaginary quaternion, and we choose coordinates on $A=\mathbb H$ so that this unit is $i$. All explicit computations are made at $u_0=i$. Left multiplication by $\iota\otimes\iota\in\mathrm{Cor}\,D$ is a rational endomorphism of $V_{\mathbb Q}$ that commutes with $\mathrm{Hg}(T_{u_0})$, has square $121$, and has eigenspaces of dimension $4$ for $\pm11$ (exact computation, script `split_check.py`; as a control, it commutes with only $2$ of the $6$ generators of $\mathrm{Lie}\,G$). On $V_{\mathbb R}$ it is a nonzero multiple of $L_iR_i$, where $R_i$ is right multiplication. Now $L_iR_i=-1$ on $X_1=\mathrm{span}(1,i)\otimes U$ and $L_iR_i=+1$ on $X_2=\mathrm{span}(j,k)\otimes U$. So $X_1$ and $X_2$ are rational, and $T_{u_0}$ is isogenous to $X_1\times X_2$. Moreover $\mathrm{NS}(X_a)_{\mathbb R}=\mathbb R w_a\oplus\sigma_a\otimes S^2U^*$, with $w=w_1+w_2$. By Lemma 2.2(5), $H^4_G$, $w$ and $[Z_\ell]$ do not depend on $u$. So a statement about these classes, checked at $u_0$, holds for every $u$. The cone $M$ of Section 3 is defined through flat Kähler metrics for $L_u$, and Section 6 shows that its description does not depend on $u$.

## 3. Muñoz's inequality and Theorem A

### 3.1 Conventions

Let $X=V/\Lambda$ be a complex 4-torus with a constant Kähler form $\omega$ and metric $g$. We identify $H^*(X,\mathbb R)$ with the constant forms $\Lambda^*V^*$, and $\mathrm{vol}$ is the volume form of $g$. Choose $\theta\in\Lambda^{4,0}$ with $|\theta|=4$. Then $\Omega=\tfrac12\omega^2+\mathrm{Re}\,\theta$ is the Cayley form of a flat $\mathrm{Spin}(7)$-structure, and $\omega^4=24\,\mathrm{vol}$, $\theta\wedge\bar\theta=16\,\mathrm{vol}$ [4, §2.2]. Let $\Lambda^2_7$ and $\Lambda^2_{21}$ be the $\mathrm{Spin}(7)$-summands of $\Lambda^2V^*$. They depend only on $g$ and $\Omega$, and
$$\Lambda^2_7=\mathbb R\omega\oplus A^+,\qquad \Lambda^2_{21}=\Lambda^{1,1}_0\oplus A^-$$
orthogonally [4, Prop. 2], where $\Lambda^{1,1}_0$ is the space of real $\omega$-primitive $(1,1)$-forms and $A^\pm\subset\mathrm{Re}(\Lambda^{2,0}\oplus\Lambda^{0,2})$ have dimension 6. A form $\gamma=\mathrm{Re}\,c$ with $c\in\Lambda^{2,0}$ lies in $A^+$ if and only if $c\wedge c=\tfrac14|c|^2\theta$ [4, §4]. By [4, Lemma 1], the elements $x\in\Lambda^2_7$ with $|x|=2$ are exactly the Kähler forms of the $\mathrm{SU}(4)$-structures $(J_x,x,\theta_x)$ with metric $g$ and Cayley form $\Omega$, and $\mathrm{Re}\,\theta_x=\Omega-\tfrac12x^2$.

**Lemma 3.1.** For $\gamma\in A^+$, $\ \omega^2\wedge\gamma^2=\mathrm{Re}\,\theta\wedge\gamma^2=2|\gamma|^2\mathrm{vol}$.

*Proof.* Write $\gamma=\mathrm{Re}\,c$. Since $c\perp\bar c$, $|c|^2=2|\gamma|^2$. By type, $\omega^2\wedge\gamma^2=\tfrac12\omega^2\wedge c\wedge\bar c=|c|^2\mathrm{vol}$ [4, Thm. 14]. Also $\mathrm{Re}\,\theta\wedge\gamma^2=\tfrac18(\bar\theta\wedge c^2+\theta\wedge\bar c^2)=\tfrac18\cdot2\cdot\tfrac14|c|^2\cdot16\,\mathrm{vol}=|c|^2\mathrm{vol}$. $\square$

For a real $(2,2)$-form $\beta$ put $k_\beta=\beta\cdot\omega^2/\omega^4$. On $A^+$ define the positive definite form $q_\omega(\gamma)=\omega^2\wedge\gamma^2/\omega^4$ and the quadratic form
$$\Phi_\beta(\gamma)=(\beta-3k_\beta\,\omega^2)\wedge\gamma^2/\omega^4 .$$
For a coherent sheaf $\mathcal F$ of rank $r>0$ let
$$\beta(\mathcal F)=c_2(\mathcal F)-\tfrac{r-1}{2r}c_1(\mathcal F)^2=\tfrac1{2r}c_1(\mathcal F)^2-\mathrm{ch}_2(\mathcal F)=\Delta(\mathcal F)/2r,$$
as in [4, §5]. It is unchanged by tensoring with a line bundle. Chern classes of coherent sheaves are the rational topological ones [8, §1]. Grivaux's classes in Deligne cohomology satisfy the Whitney formula and map to these [8, Thm. 1.1, Cor. 6.5]. So $\mathrm{ch}$ is additive on exact sequences, and $\mathrm{ch}_p$ is a Hodge class. The inequality we study is
$$\Phi_\beta\le0\ \text{ on }A^+. \tag{3.1}$$
Condition (3.1) does not depend on the choice of $\theta$. Indeed $\Phi_\beta(\mathrm{Re}\,c)=\tfrac12(\beta-3k_\beta\omega^2)\wedge c\wedge\bar c/\omega^4$ is invariant under $c\mapsto e^{it}c$, and replacing $\theta$ by $e^{2it}\theta$ replaces $A^+$ by $\{\mathrm{Re}(e^{it}c):\mathrm{Re}\,c\in A^+\}$.

### 3.2 The inequality on every flat Kähler 4-torus

We work with connections that may be singular at finitely many points, so that Section 3.3 can use the same proof. Let $E$ be a hermitian vector bundle of rank $r$ on $X\setminus S$ with $S$ finite, and let $A$ be a unitary connection on $E$ with $\int_{X\setminus S}|F_A|^2<\infty$. Write $F^\circ=F_A-\tfrac1r\mathrm{tr}(F_A)\,\mathrm{Id}$. We say that $(A,\beta)$ satisfies condition (C) at $\omega$ if:

- (C1) $F^\circ$ is of type $(1,1)$ and $\omega$-primitive at every point of $X\setminus S$;
- (C2) $\int_{X\setminus S}\mathrm{tr}(F^\circ\wedge F^\circ)\wedge\varphi=8\pi^2\,\beta\cdot\varphi$ for every constant 4-form $\varphi$.

If $S=\emptyset$, $A$ is a connection on a bundle over $X$ and $\beta=\beta(E)$, then (C2) is Chern–Weil theory. So (C) holds for every traceless $\omega$-HYM connection in the sense of [4, Def. 7], and in particular for the Hermitian–Yang–Mills connection of an $\omega$-polystable bundle [4, Prop. 6]. By (C1), the form $\mathrm{tr}(F^\circ\wedge F^\circ)$ is of type $(2,2)$, so (C2) forces $\beta$ to be of type $(2,2)$.

**Proposition 3.2.** If $(A,\beta)$ satisfies (C) at $\omega$, then $\Phi_\beta\le0$ on $A^+$. In particular, (3.1) holds for $\beta(E)$ for every $\omega$-polystable bundle $E$ on every flat Kähler 4-torus $(X,\omega)$.

The proof combines three facts: $\Phi_\beta$ is semidefinite (Lemma 3.3), its trace is $-12k_\beta$ (Lemma 3.4), and $k_\beta\ge0$.

**Lemma 3.3** (Muñoz's Prop. 18). If $(A,\beta)$ satisfies (C) at $\omega$, then $\Phi_\beta$ is semidefinite.

*Proof.* On $\Lambda^2_7$ consider the symmetric bilinear form
$$Q(x,y)=\beta\wedge x\wedge y/\mathrm{vol}-\tfrac12(\beta\wedge\Omega/\mathrm{vol})\langle x,y\rangle .$$
It depends only on $\beta$, $g$ and $\Omega$. We use three properties.

(a) If $|x|=2$, then $Q(x,x)=-2\,\beta\wedge\mathrm{Re}\,\theta_x/\mathrm{vol}$. This follows from $\mathrm{Re}\,\theta_x=\Omega-\tfrac12x^2$.

(b) If $\beta$ is of type $(2,2)$ for $J_x$, then $x$ lies in the radical of $Q$. Indeed $Q(x,x)=0$ by (a). For $y$ in the $A^+$ of $(J_x,x,\theta_x)$ we have $\langle x,y\rangle=0$, and $\beta\wedge x\wedge y=0$ because $x\wedge y$ has type $(3,1)+(1,3)$ for $J_x$.

(c) For $\gamma\in A^+$, $Q(\gamma,\gamma)=24\,\Phi_\beta(\gamma)$. Indeed $\beta\wedge\Omega=\tfrac12\beta\wedge\omega^2=12k_\beta\mathrm{vol}$ since $\beta$ is of type $(2,2)$, and $6k_\beta|\gamma|^2\mathrm{vol}=3k_\beta\,\omega^2\wedge\gamma^2$ by Lemma 3.1.

By (b) for $x=\omega$ and by (c), $Q$ is the orthogonal sum of $0$ on $\mathbb R\omega$ and $24\Phi_\beta$ on $A^+$.

Let $\gamma\in A^+$ be nonzero with $\Phi_\beta(\gamma)=0$, and put $\omega'=2(\omega+\gamma)/|\omega+\gamma|$. Then $Q(\omega',\omega')=0$, so $\beta\wedge\mathrm{Re}\,\theta'=0$ by (a), where $(J',\omega',\theta')$ is the structure of $\omega'$. Now apply the argument of [4, Prop. 11, (c)$\Rightarrow$(a)] to $J'$. By (C1), $F^\circ$ takes values in $\Lambda^2_{21}$, which also equals $\Lambda^{1,1}_{0,J'}\oplus A'^-$. The pointwise identity in that proof gives
$$\int_{X\setminus S}\mathrm{tr}(F^\circ\wedge F^\circ)\wedge\mathrm{Re}\,\theta'=-4\,\|F^{\circ\,2,0}_{J'}\|^2_{L^2(X\setminus S)},$$
and by (C2) the left side is $8\pi^2\beta\cdot\mathrm{Re}\,\theta'=0$. So $F^\circ$ is of type $(1,1)$ for $J'$ on $X\setminus S$. Then $\mathrm{tr}(F^\circ\wedge F^\circ)$ is of type $(2,2)$ for $J'$, and (C2) shows that $\beta$ is of type $(2,2)$ for $J'$. By (b), $\omega'$ lies in the radical of $Q$. So does $\omega$, hence so does $\gamma=\tfrac12|\omega+\gamma|\,\omega'-\omega$. Therefore $\gamma$ lies in the radical of $\Phi_\beta$.

So every isotropic vector of $\Phi_\beta$ is in its radical. If $\Phi_\beta(u)>0>\Phi_\beta(v)$, the restriction of $\Phi_\beta$ to $\mathrm{span}(u,v)$ is nondegenerate of signature $(1,1)$ and has an isotropic vector outside the radical of $\Phi_\beta$. Hence $\Phi_\beta$ is semidefinite. $\square$

Muñoz's proof of Prop. 18 argues that the rotated metric "should be a singular point" of the solution set of $\Phi_\beta=0$. The argument above replaces that step.

**Lemma 3.4** (trace identity). For every real $(2,2)$-form $\beta$, $\ \mathrm{tr}_{q_\omega}\Phi_\beta=-12\,k_\beta$.

*Proof.* (This proof via $\mathrm{SU}(4)$-invariance was suggested by cm_symmetry_scout.) Let $\gamma_1,\dots,\gamma_6$ be a $q_\omega$-orthonormal basis of $A^+$. The form $\sigma=\sum_i\gamma_i^2$ does not depend on the basis, and it is $\mathrm{SU}(4)$-invariant because $\mathrm{SU}(4)$ preserves $A^+$ and $q_\omega$. The $\mathrm{SU}(4)$-invariant real 4-forms are spanned by $\omega^2$, $\mathrm{Re}\,\theta$ and $\mathrm{Im}\,\theta$. (In $\Lambda^{p,q}$ with $p+q=4$ the invariants are $\theta$ in $\Lambda^{4,0}$, $\bar\theta$ in $\Lambda^{0,4}$ and $\omega^2$ in $\Lambda^{2,2}\cong\mathrm{End}(\Lambda^{2,0})$, because $\Lambda^{2,0}$ is irreducible; $\Lambda^{3,1}\cong\mathbb C^4\otimes\mathbb C^4$ has none.) The forms $\mathrm{Re}\,\theta$ and $\mathrm{Im}\,\theta$ wedge to zero with $\beta$ and with $\omega^2$. Since $\omega^2\wedge\sigma=6\,\omega^4$, we get $\beta\wedge\sigma=6\,\beta\wedge\omega^2$. Hence $\mathrm{tr}_{q_\omega}\Phi_\beta=\sum_i\Phi_\beta(\gamma_i)=6k_\beta-3k_\beta\cdot6=-12k_\beta$. $\square$

In fact $\sigma=6\omega^2+18\,\mathrm{Re}\,\theta$. The script `aplus_trace.py` checks Lemma 3.1, this formula for $\sigma$ and Lemma 3.4 in exact arithmetic, on a basis of the 36-dimensional space of real $(2,2)$-forms at the standard structure on $\mathbb C^4$. Every flat $\mathrm{SU}(4)$-structure is linearly equivalent to that one. As a control, the identity fails for $\beta=\mathrm{Re}\,\theta$, which is not of type $(2,2)$: there $k=0$ and the trace is 6.

*Proof of Proposition 3.2.* For a real primitive $(1,1)$-form $a$ on a 4-fold, $a\wedge a\wedge\omega^2=-2|a|^2\mathrm{vol}$. Expanding $F^\circ$ in a basis of $\mathfrak u(r)$ that is orthonormal for $-\mathrm{tr}$, (C1) gives $\mathrm{tr}(F^\circ\wedge F^\circ)\wedge\omega^2=2|F^\circ|^2\mathrm{vol}$. By (C2) with $\varphi=\omega^2$, $8\pi^2\,\beta\cdot\omega^2=2\|F^\circ\|^2\ge0$, so $k_\beta\ge0$. This is the Bogomolov inequality [4, (9)] in the present setting. By Lemma 3.3, $\Phi_\beta$ is semidefinite. By Lemma 3.4 its trace is $-12k_\beta\le0$. A positive semidefinite form with nonpositive trace is zero. So in either case $\Phi_\beta\le0$. $\square$

**Remark 3.5** (comparison with [4]). Muñoz proves Proposition 3.2 for abelian varieties [4, Prop. 20] and for tori with a rational primitive $(1,1)$-class [4, Rem. 21]. He conjectures it for all Kähler 4-tori, for the classes $\beta$ such that some multiple $N\beta$ is traceless $\omega$-HYM [4, Def. 16, Rem. 21]. His Kähler forms are constant, and $\Phi_{N\beta}=N\Phi_\beta$, so Proposition 3.2 proves this conjecture. His proof compares $\beta$ with a second class $\beta'$ and passes from $\Phi_\beta=\lambda\Phi_{\beta'}$ to $\beta=\lambda\beta'$. That step is incomplete. The linear map $\beta\mapsto\Phi_\beta$ on real $(2,2)$-forms has rank 21, and its kernel is the 15-dimensional space $\omega\wedge\Lambda^{1,1}_0$ (`aplus_trace.py`). The reason is that $A^+$ is the 6-dimensional real representation of $\mathrm{SU}(4)$ through $\mathrm{SU}(4)\to\mathrm{SO}(6)$ [4, Rem. 4], so $\mathrm{Sym}^2A^+$ is the sum of a trivial and a 20-dimensional representation and has no 15-dimensional summand. The proof above uses neither the comparison class nor projectivity.

**Remark 3.6** (only $A^+$). Inequality (3.1) does not extend to all of $\mathrm{Re}\,\Lambda^{2,0}$. At the standard structure, let $a=i(dz_1\wedge d\bar z_1-dz_2\wedge d\bar z_2)$, which is primitive, and $\beta=-a^2$. Then $\beta$ satisfies (3.1) with a zero eigenvalue (Lemma 4.1), but $(\beta-3k_\beta\omega^2)\wedge c\wedge\bar c=16\,\mathrm{vol}$ for $c=dz_3\wedge dz_4$, which is not in $A^+$ (`aplus_trace.py`). This does not contradict [4, Thm. 22]: the inequality in its proof involves only the primitive part $\beta_0$ of $\beta$, and $(\beta_0-2k_\beta\omega^2)\wedge c\wedge\bar c=0$ for this $\beta$ and $c$.

### 3.3 Reflexive sheaves

**Proposition 3.7.** Let $(X,\omega)$ be a flat Kähler 4-torus and $\mathcal E$ an $\omega$-stable reflexive sheaf of rank $r$ whose singular set $S$ is finite. Then $\mathcal E|_{X\setminus S}$ carries a unitary connection $A$ such that $(A,\beta(\mathcal E))$ satisfies (C) at $\omega$. Hence $\Phi_{\beta(\mathcal E)}\le0$ on $A^+$.

*Proof.* By Bando and Siu [5, Thm. 3] (see also [1, Appendix] and, for the definition, [6, §2]), $\mathcal E$ has an admissible Hermitian–Einstein metric $h$: $h$ is smooth on $X\setminus S$, its Chern connection $A$ satisfies $\sqrt{-1}\Lambda_\omega F_A=\lambda\,\mathrm{Id}$ there, and $\int_{X\setminus S}|F_A|^2<\infty$. Then $F^\circ$ is of type $(1,1)$ with $\Lambda_\omega F^\circ=0$, which is (C1).

For (C2), first note that the currents defined by the $L^1$ forms $\tau=\mathrm{tr}(F_A\wedge F_A)$ and $\tau_1=\mathrm{tr}F_A\wedge\mathrm{tr}F_A$ are closed on $X$. Both forms are closed on $X\setminus S$. Since $A$ is Hermitian–Einstein, it is stationary and satisfies Price's monotonicity: $\int_{B_\rho(p)}|F_A|^2\le C\rho^4$ for $p\in S$ and small $\rho$ [6, (2.3)]. Let $\chi_\epsilon$ be a cutoff equal to 1 on the $\epsilon$-balls around $S$, supported in the $2\epsilon$-balls, with $|d\chi_\epsilon|\le2/\epsilon$. For a smooth 3-form $\psi$, Stokes' theorem on $X\setminus S$ gives
$$\Big|\int_X\tau\wedge d\psi\Big|=\Big|\int_X\tau\wedge d(\chi_\epsilon\psi)\Big|\le\frac C\epsilon\cdot C\epsilon^4+\int_{\bigcup_pB_{2\epsilon}(p)}|\tau|\,|d\psi|\longrightarrow0 .$$
The same holds for $\tau_1$, since $|\tau_1|\le r|F_A|^2$. (Tian proves closedness for admissible Yang–Mills connections in general [7, Prop. 2.3.1].)

Next, the restriction $H^4(X,\mathbb R)\to H^4(X\setminus S,\mathbb R)$ is an isomorphism, because $H^j(X,X\setminus S)\cong H_{8-j}(S)=0$ for $j=4,5$. The restriction of the class of the current $\tau$ is the de Rham class of $\tau|_{X\setminus S}$, which is $-8\pi^2\mathrm{ch}_2(\mathcal E|_{X\setminus S})$ by Chern–Weil theory. The topological Chern classes of $\mathcal E$ are defined by a real-analytic locally free resolution of $\mathcal E\otimes\mathcal C^\omega_X$ [8, §1]. Its restriction to $X\setminus S$ resolves the bundle $\mathcal E|_{X\setminus S}$, so $\mathrm{ch}(\mathcal E)$ restricts to $\mathrm{ch}(\mathcal E|_{X\setminus S})$. Hence $[\tau]=-8\pi^2\mathrm{ch}_2(\mathcal E)$ and, in the same way, $[\tau_1]=-4\pi^2c_1(\mathcal E)^2$. Since $\mathrm{tr}(F^\circ\wedge F^\circ)=\tau-\tfrac1r\tau_1$, its class is $8\pi^2\big(\tfrac1{2r}c_1^2-\mathrm{ch}_2\big)=8\pi^2\beta(\mathcal E)$. Pairing with constant forms gives (C2). Proposition 3.2 gives the last claim. $\square$

### 3.4 Proof of Theorem A

From now on $u$ is very general. Let $W$ be the set of constant Kähler forms $\omega$ on $T_u$ with $w\cdot\omega^3=0$, and
$$M=\{\beta\in\mathrm{Hdg}^4(T_u)\otimes\mathbb R:\ \Phi^\omega_\beta\le0\text{ on }A^+(\omega)\text{ for every }\omega\in W\}.$$
$W$ is not empty. Let $g$ be the flat hyperkähler metric of Section 2.1 and $\omega_v=g(L_v\cdot,\cdot)$ for $v\in S^2$. Then $\omega_u$ is a Kähler form on $T_u$, and $\omega_u\in W$. Indeed $w$ is $G(\mathbb R)$-invariant (Lemma 2.2(2)), and a unit quaternion $a\in\mathrm{Sp}(1)\times1$ pulls $\omega_v$ back to $\omega_{a^{-1}va}$. So $v\mapsto w\cdot\omega_v^3$ is constant on $S^2$. It is also odd, because $\omega_{-v}=-\omega_v$. Hence it vanishes. $M$ is a closed convex cone, since each condition is linear in $\beta$. By Lemma 3.4, every $\beta\in M$ has $k_\beta\ge0$ at every $\omega\in W$.

**Lemma 3.8.** Let $\omega\in W$. Every coherent subsheaf of a torsion-free sheaf on $T_u$ has $\omega$-slope $0$. Hence every torsion-free sheaf $\mathcal F$ is $\omega$-semistable, and it is $\omega$-stable if and only if it has no coherent subsheaf of rank strictly between $0$ and $\mathrm{rk}\,\mathcal F$. This condition does not involve $\omega$.

*Proof.* The first Chern class of a coherent sheaf is a rational $(1,1)$-class, so it lies in $\mathrm{NS}(T_u)\otimes\mathbb Q=\mathbb Q w$ (Lemma 2.2). Since $w\cdot\omega^3=0$, all slopes vanish. $\square$

**Lemma 3.9.** Let $0\to\mathcal F'\to\mathcal F\to\mathcal F''\to0$ be exact with ranks $r',r''>0$ and $r=r'+r''$. Then
$$\beta(\mathcal F)=\beta(\mathcal F')+\beta(\mathcal F'')-\frac{r'r''}{2r}\,\xi^2,\qquad \xi=\frac{c_1(\mathcal F')}{r'}-\frac{c_1(\mathcal F'')}{r''}.$$

*Proof.* $c_1$ and $\mathrm{ch}_2$ are additive, $\beta=c_1^2/2r-\mathrm{ch}_2$, and $(a+b)^2/r-a^2/r'-b^2/r''=-\tfrac{r'r''}{r}(a/r'-b/r'')^2$. $\square$

*Proof of Theorem A.* We follow the rank induction of [1, Appendix, Prop. 4].

Step 1: $-w^2\in M$. Some multiple $Nw$ with $N>0$ is $c_1$ of a line bundle $L$. For $\omega\in W$ the bundle $L\oplus L^{-1}$ is $\omega$-polystable, since both summands have slope 0. Its $\beta$ is $c_2=-N^2w^2$. Proposition 3.2 gives $-w^2\in M$.

Step 2: let $\mathcal G$ be torsion-free with no subsheaf of intermediate rank. Then $\mathcal G^{**}$ has none either: a subsheaf $\mathcal G'\subset\mathcal G^{**}$ meets $\mathcal G$ in a subsheaf of the same rank, because $\mathcal G^{**}/\mathcal G$ is torsion. By Lemma 3.8, $\mathcal G^{**}$ is $\omega$-stable for every $\omega\in W$. Its singular set is finite by Corollary 2.4. Proposition 3.7 gives $\Phi^\omega_{\beta(\mathcal G^{**})}\le0$ for every $\omega\in W$. By Corollary 2.4, $c_1$ and $\mathrm{ch}_2$ of $\mathcal G$ and $\mathcal G^{**}$ agree, so $\beta(\mathcal G)=\beta(\mathcal G^{**})\in M$.

Step 3: let $\mathcal F$ be torsion-free. Choose a saturated subsheaf $\mathcal F_1\subset\mathcal F$ of minimal positive rank. It has no subsheaf of intermediate rank, and $\mathcal F/\mathcal F_1$ is torsion-free. By induction on the rank we get a filtration $0=\mathcal F_0\subset\mathcal F_1\subset\dots\subset\mathcal F_m=\mathcal F$ whose quotients $\mathcal G_i$ are as in Step 2. Lemma 3.9 applied to $0\to\mathcal F_{i-1}\to\mathcal F_i\to\mathcal G_i\to0$ gives
$$\beta(\mathcal F)=\sum_i\beta(\mathcal G_i)+\sum_i t_i\,(-w^2),\qquad t_i\ge0,$$
because every $\xi$ lies in $\mathbb Q w$. By Steps 1 and 2 and convexity, $\beta(\mathcal F)\in M$.

Step 4: let $\mathcal F$ be coherent of positive rank, with torsion subsheaf $\mathcal T$. By Corollary 2.4, $c_1(\mathcal T)=0$ and $\mathrm{ch}_2(\mathcal T)=0$. So $\beta(\mathcal F)=\beta(\mathcal F/\mathcal T)$, which lies in $M$ by Step 3. $\square$

The proof shows a little more. For each coherent $\mathcal F$, $\beta(\mathcal F)$ is the sum of the $\beta$'s of the wall-stable factors $\mathcal G_i$ and a nonnegative multiple of $-w^2$. Only factors of rank at least 2 can contribute to the $K_5$-component, since a rank-1 factor has $\beta=0$. Section 8 returns to this.

## 4. A rank-2 lemma

In this section $(X,\omega)$ is any flat Kähler 4-torus. The hermitian form of a real $(1,1)$-form $\alpha=i\sum h_{jk}\,dz_j\wedge d\bar z_k$ is $(h_{jk})$, and the rank and signature of $\alpha$ are those of this form. In an $\omega$-unitary frame put $e_j=\tfrac i2dz_j\wedge d\bar z_j$, so that $\omega=\sum_je_j$. By Section 3.1 we may take $\theta=dz_1\wedge dz_2\wedge dz_3\wedge dz_4$. Write $dz_{jk}=dz_j\wedge dz_k$.

**Lemma 4.1.** In an $\omega$-unitary frame with $\theta=dz_{1234}$,
$$A^+=\{\mathrm{Re}\,c:\ c=a\,dz_{12}+\bar a\,dz_{34}+b\,dz_{13}-\bar b\,dz_{24}+e\,dz_{14}+\bar e\,dz_{23},\ a,b,e\in\mathbb C\}.$$

*Proof.* For such $c$, $c\wedge c=2(c_{12}c_{34}-c_{13}c_{24}+c_{14}c_{23})\,\theta=2(|a|^2+|b|^2+|e|^2)\,\theta$. Since $|dz_{jk}|^2=4$, $|c|^2=8(|a|^2+|b|^2+|e|^2)$. So $c\wedge c=\tfrac14|c|^2\theta$, and $\mathrm{Re}\,c\in A^+$ (Section 3.1). These forms make up a 6-dimensional space, and $\dim A^+=6$. $\square$

**Lemma 4.2** (diagonal model). Let $\beta=\mu_2\,e_1\wedge e_2+\mu_3\,e_1\wedge e_3+\mu_4\,e_1\wedge e_4$ with $\mu_j\in\mathbb R$, and let $c$ be as in Lemma 4.1. Then $k_\beta=(\mu_2+\mu_3+\mu_4)/12$ and
$$(\beta-3k_\beta\omega^2)\wedge c\wedge\bar c=-4\big[(\mu_3+\mu_4)|a|^2+(\mu_2+\mu_4)|b|^2+(\mu_2+\mu_3)|e|^2\big]\,\mathrm{vol}.$$
So $\beta$ satisfies (3.1) if and only if $\mu_j+\mu_k\ge0$ for all $j\ne k$ in $\{2,3,4\}$.

*Proof.* We have $dz_{kl}\wedge d\bar z_{kl}=4\,e_k\wedge e_l$, and $e_1\wedge e_j$ pairs nontrivially only with the complementary pair. So $\beta\wedge c\wedge\bar c=4(\mu_2|a|^2+\mu_3|b|^2+\mu_4|e|^2)\,\mathrm{vol}$. Next, $\beta\wedge\omega^2=2(\mu_2+\mu_3+\mu_4)\,\mathrm{vol}$ and $\omega^4=24\,\mathrm{vol}$, which gives $k_\beta$. Finally $\omega^2\wedge c\wedge\bar c=2|c|^2\mathrm{vol}=16(|a|^2+|b|^2+|e|^2)\,\mathrm{vol}$. Subtracting gives the formula. Since $\Phi_\beta(\mathrm{Re}\,c)$ is a positive multiple of the left side (Section 3.1), the last claim follows. The script `rank2_model.py` checks the formula symbolically. $\square$

**Lemma 4.3.** Let $\alpha$ be a real $(1,1)$-form of rank $2$ and signature $(1,1)$. Then $\beta=-\alpha^2$ satisfies (3.1) at every flat Kähler metric, and $\Phi_\beta$ has a nonzero isotropic vector.

*Proof.* Choose an $\omega$-unitary frame that diagonalises the hermitian form of $\alpha$. Then $\alpha=l_1e_1-l_2e_2$ with $l_1,l_2>0$, so $-\alpha^2=2l_1l_2\,e_1\wedge e_2$. In Lemma 4.2 this is $\mu_2=2l_1l_2$ and $\mu_3=\mu_4=0$, and the form equals $-8l_1l_2(|b|^2+|e|^2)\,\mathrm{vol}\le0$. It vanishes at $c=dz_{12}+dz_{34}$. $\square$

The hypothesis on the signature is needed. For $\alpha=l_1e_1+l_2e_2$, of signature $(2,0)$, the same computation gives $+8l_1l_2(|b|^2+|e|^2)\,\mathrm{vol}$, so (3.1) fails at $c=dz_{13}-dz_{24}$ (`rank2_model.py`). Muñoz proves (3.1) for $-\alpha^2$ when $\alpha$ is $\omega$-primitive [4, Lemma 25]. Lemma 4.3 needs no primitivity, and this is why it holds at every metric.

**Corollary 4.4.** Let $u\in S^2$ and $\ell\in U^*\setminus0$. Then $[Z_\ell]=-\tfrac12\alpha_\ell^2$ for a real $(1,1)$-form $\alpha_\ell$ on $T_u$ of rank $2$ and signature $(1,1)$. Hence $[Z_\ell]$ satisfies (3.1) at every flat Kähler metric on $T_u$. For very general $u$,
$$\mathbb R_{\ge0}(-w^2)+\overline{\mathrm{cone}}\{[Z_\ell]:\ell\in\mathbb P^1(\mathbb R)\}\subseteq M .$$

*Proof.* The map $\pi_\ell\colon V_{\mathbb R}\to A$ commutes with left multiplication, so it is complex linear for $L_u$. Choose $g_A$-unitary coordinates on $(A,L_u)\cong\mathbb C^2$ and put $\alpha_A=e_1-e_2$. Then $-\tfrac12\alpha_A^2=e_1\wedge e_2=\mathrm{vol}_A$. The pullback $\alpha_\ell=\pi_\ell^*\alpha_A$ is a real $(1,1)$-form for $L_u$, its hermitian form is the pullback of that of $\alpha_A$, so it has rank 2 and signature $(1,1)$, and $-\tfrac12\alpha_\ell^2=\pi_\ell^*\mathrm{vol}_A=[Z_\ell]$. Lemma 4.3 gives (3.1) at every flat Kähler metric. Now let $u$ be very general. Then $[Z_\ell]\in K_5\otimes\mathbb R\subset\mathrm{Hdg}^4(T_u)\otimes\mathbb R$ (Lemma 2.2(3)), so $[Z_\ell]\in M$. Also $-w^2\in M$ (Step 1 of the proof of Theorem A), and $M$ is a closed convex cone. $\square$

So every $[Z_\ell]$ lies in $M$, and at every wall metric its form $\Phi_{[Z_\ell]}$ has a nonzero isotropic vector. This is the inclusion $\supseteq$ of Theorem B. Sections 5 and 6 prove the reverse inclusion.

## 5. An asymptotic condition

In this section $u\in S^2$ is arbitrary, $W$ is the set of constant Kähler forms $\omega$ on $T_u$ with $w\cdot\omega^3=0$ (nonempty by Section 3.4), $T=T^{1,0}_0T_u\cong\mathbb C^4$, and $h_w$ is the hermitian form of $w$ on $T$. Write $w=i\sum H_{jk}\,dz_j\wedge d\bar z_k$, so that $h_w(x,y)=\sum H_{jk}x_j\bar y_k$. The wall $W$ is not compact. Along a sequence of wall metrics in which a null vector of $h_w$ becomes short, condition (3.1) has a limit, and this section computes it.

For a real $(2,2)$-form $\beta$ and $v\in T$ put
$$r_v(\beta)=-2i\,\iota_{\bar v}\iota_v\beta .$$
Since $\overline{\iota_{\bar v}\iota_v\beta}=\iota_v\iota_{\bar v}\beta=-\iota_{\bar v}\iota_v\beta$, the form $r_v(\beta)$ is a real $(1,1)$-form. It satisfies $\iota_vr_v(\beta)=\iota_{\bar v}r_v(\beta)=0$, so it defines a hermitian form on $T/\mathbb Cv$. We call $r_v(\beta)$ the *residue* of $\beta$ along $v$. Note $r_{cv}=|c|^2r_v$.

**Definition.** A real $(2,2)$-form $\beta$ satisfies (AM) if $r_v(\beta)\ge0$ on $T/\mathbb Cv$ for every nonzero $v\in T$ with $h_w(v,v)=0$.

The classes that satisfy (AM) form a closed convex cone.

**Lemma 5.1.** Let $v\ne0$ with $h_w(v,v)=0$, and let $\lambda=i\,\iota_{\bar v}w$, the $(1,0)$-form $x\mapsto h_w(x,v)$. Then $r_v(-w^2)=4i\,\lambda\wedge\bar\lambda$. Hence $-w^2$ satisfies (AM), and $w^2$ does not.

*Proof.* We have $\iota_vw=i\bar\lambda$, and $\iota_{\bar v}\bar\lambda=\overline{\lambda(v)}=\overline{h_w(v,v)}=0$. So
$$\iota_{\bar v}\iota_v(w^2)=2\,\iota_{\bar v}(i\bar\lambda\wedge w)=-2i\,\bar\lambda\wedge\iota_{\bar v}w=-2\,\bar\lambda\wedge\lambda=2\,\lambda\wedge\bar\lambda,$$
and $r_v(-w^2)=4i\,\lambda\wedge\bar\lambda$. Its hermitian form is $x\mapsto4|\lambda(x)|^2\ge0$. Since $h_w$ is nondegenerate, $\lambda\ne0$. As $\lambda(v)=0$, the form $\lambda$ is nonzero on $T/\mathbb Cv$, so $r_v(w^2)$ is negative somewhere on $T/\mathbb Cv$. The script `am_limit.py` checks the identity numerically. $\square$

**Proposition 5.2.** Let $\beta$ be a real $(2,2)$-form that satisfies (3.1) at every $\omega\in W$. Then $\beta$ satisfies (AM). In particular $M$ is contained in the cone of classes that satisfy (AM).

*Proof.* A constant Kähler form $\omega_g$ corresponds to a hermitian metric $g$ on $T$, and $w\wedge\omega_g^3$ is a positive multiple of $\mathrm{tr}_g(h_w)\,\mathrm{vol}_g$. So $\omega_g\in W$ if and only if $\mathrm{tr}_gh_w=0$. Suppose $v\ne0$, $h_w(v,v)=0$, and the hermitian form of $r_v(\beta)$ is negative at some $u_0\in T$. Fix a complement $U$ of $\mathbb Cv$. We may take $u_0\in U$, since $r_v(\beta)$ only depends on $u_0$ modulo $\mathbb Cv$.

(i) *Wall metrics.* Fix a hermitian metric $h$ on $U$, to be chosen in (iv), and put $\tau=\mathrm{tr}_h(h_w|_U)$. Choose $z$ with $\mathrm{Re}\,h_w(v,z)\ne0$, which is possible because $h_w$ is nondegenerate. For small $\epsilon>0$ the equation $h_w(v+sz,v+sz)=-\epsilon^2\tau$ has a real root $s=s(\epsilon)=O(\epsilon^2)$, by the implicit function theorem. Put $v_\epsilon=v+s(\epsilon)z$, which is not in $U$ for small $\epsilon$. Let $g_\epsilon$ be the hermitian metric with $v_\epsilon\perp U$, $|v_\epsilon|=\epsilon$ and $g_\epsilon|_U=h$. In the $g_\epsilon$-unitary frame $f_1=v_\epsilon/\epsilon$, $f_2,f_3,f_4$ ($h$-unitary in $U$),
$$\mathrm{tr}_{g_\epsilon}h_w=\epsilon^{-2}h_w(v_\epsilon,v_\epsilon)+\tau=0,$$
so $\omega_\epsilon=\omega_{g_\epsilon}\in W$.

(ii) *Scaling.* Write $\beta$ in the frame $(f_j)$ and its dual coframe. The components that contain both $f_1$ and $\bar f_1$ form $\epsilon^{-2}e_1\wedge r_{v_\epsilon}(\beta)$, where $e_1=\tfrac i2f^1\wedge\bar f^1$ and $r_{v_\epsilon}(\beta)$ is restricted to $U$; indeed $\iota_{\bar f_1}\iota_{f_1}(e_1\wedge\rho)=-\tfrac i2\rho$ for a form $\rho$ on $U$. The components with exactly one of $f_1,\bar f_1$ are $O(\epsilon^{-1})$, and the others are $O(1)$. Since $s(\epsilon)\to0$,
$$\epsilon^2\beta\longrightarrow e_1\wedge b,\qquad b=r_v(\beta)|_U,$$
componentwise in the frames $(f_j)$.

(iii) *Limit.* In the frame $(f_j)$, $\omega_\epsilon$ is the standard form, so $A^+(\omega_\epsilon)$ and $q$ are the standard ones of Lemma 4.1. Since $\Phi$ and $k$ are linear in $\beta$, the matrix of $\epsilon^2\Phi^{\omega_\epsilon}_\beta$ on $A^+$ converges to that of $\Phi_{e_1\wedge b}$ in the standard model.

(iv) *Contradiction.* Diagonalise $b$ in an $h$-unitary frame of $U$, with eigenvalues $\mu_2,\mu_3,\mu_4$. By Lemma 4.2 (with $\beta=e_1\wedge b=\sum_j\mu_je_1\wedge e_j$), $\Phi_{e_1\wedge b}\le0$ if and only if $\mu_j+\mu_k\ge0$ for all $j\ne k$. It remains to choose $h$ in (i). Let $u_0,u_2',u_3'$ be a basis of $U$, and let $h_\delta$ make $\delta^{-1}u_0,u_2',u_3'$ unitary. The matrix of $b$ in this frame is $D\,N\,D$ with $D=\mathrm{diag}(\delta^{-1},1,1)$ and $N$ the matrix of $b$ in the basis $(u_0,u_2',u_3')$. Its smallest eigenvalue is at most its $(0,0)$ entry $\delta^{-2}N_{00}$, and $N_{00}<0$. By interlacing, its middle eigenvalue is at most the largest eigenvalue of the lower $2\times2$ block, which does not depend on $\delta$. So for small $\delta$ the sum of the smallest two eigenvalues is negative, and $\Phi_{e_1\wedge b}$ has a positive eigenvalue. By (iii) so does $\Phi^{\omega_\epsilon}_\beta$ for small $\epsilon$, which contradicts (3.1) at $\omega_\epsilon\in W$. $\square$

The script `am_limit.py` checks steps (i)–(iii) numerically for $\pm w^2$ and a random real $(2,2)$-form: the trace of $h_w$ in the frame vanishes to rounding, $\epsilon^2\Phi^{\omega_\epsilon}_\beta$ approaches its limit at rate $O(\epsilon)$, and the limit spectrum is $-(\mu_j+\mu_k)/4$, each value twice, as Lemma 4.2 predicts. As a control, $+w^2$ gives a positive eigenvalue in the limit.

The metrics $g_\epsilon$ leave every compact subset of $W$, which is why we call (AM) asymptotic. Section 6 shows that, on $\mathrm{Hdg}^4(T_u)\otimes\mathbb R$, (AM) is already equivalent to membership in $M$.

## 6. Proof of Theorem B

By Lemma 2.2(3), every class in $\mathrm{Hdg}^4(T_u)\otimes\mathbb R$ is $c\,w^2+\mathrm{vol}_A\otimes p$ with $c\in\mathbb R$ and $p\in S^4U^*$, a real quartic form on $U$, and $[Z_\ell]=\mathrm{vol}_A\otimes\ell^4$. Let $\Sigma_4\subset S^4U^*$ be the cone of finite sums of fourth powers $\ell^4$, $\ell\in U^*$. It is closed: it is the cone over the convex hull of the compact set $\{\ell^4:|\ell|=1\}$, which does not contain $0$ because every $\ell^4$ is a nonnegative function, positive somewhere. So Theorem B says
$$M=\{c\,w^2+\mathrm{vol}_A\otimes p:\ c\le0,\ p\in\Sigma_4\}.$$
The inclusion $\supseteq$ is Corollary 4.4. For $\subseteq$ we use (AM) and Proposition 5.2.

**Reduction to $u=i$.** For any $u\in S^2$ let $M_u\subset H^4_G\otimes\mathbb R$ be the set of classes that satisfy (3.1) at every $\omega\in W_u$, the wall of $T_u$. By Lemma 2.2(5) this makes sense, and $M=M_u$ for very general $u$. The cone $M_u$ depends only on the complex structure $L_u$ on $V_{\mathbb R}$, the form $w$ and the space $H^4_G\otimes\mathbb R$, since $W_u$ and (3.1) involve only constant forms. A unit quaternion $a$ acts on $V_{\mathbb R}$ by left multiplication $L_a$, an element of $\mathrm{Sp}(1)\times1\subset G(\mathbb R)$. It satisfies $L_aL_uL_a^{-1}=L_{aua^{-1}}$ and fixes $w$ and every class in $H^4_G$. So it carries $W_u$ onto $W_{aua^{-1}}$ and (3.1) at $\omega$ to (3.1) at the image of $\omega$, and $M_u=M_{aua^{-1}}$. Since $\mathrm{Sp}(1)$ acts transitively on $S^2$, all $M_u$ coincide, and $M_i=M$. So it suffices to prove $M_i\subseteq\{c\,w^2+\mathrm{vol}_A\otimes p:c\le0,\ p\in\Sigma_4\}$; the reverse inclusion is Corollary 4.4.

**Coordinates.** Identify $(A,L_i)=(\mathbb H,L_i)$ with $\mathbb C^2$, with standard hermitian form $H$, so that $g_A=\mathrm{Re}\,H$. Choose a basis $e_1,e_2$ of $U$ with $\varepsilon_U(e_1,e_2)=1$, and write $x=x_1\otimes e_1+x_2\otimes e_2\in T=T^{1,0}_0T_i$ as $(x_1,x_2)\in\mathbb C^2\oplus\mathbb C^2$. Then
$$\pi_\ell(x)=\ell_1x_1+\ell_2x_2,\qquad \ell_k=\ell(e_k),$$
and, after multiplying $w$ by a nonzero real constant,
$$h_w(x,y)=i\big(H(x_1,y_2)-H(x_2,y_1)\big).$$
Indeed this form is hermitian and $L_i$-sesquilinear, and its imaginary part is $\mathrm{Re}\,H(x_1,y_2)-\mathrm{Re}\,H(x_2,y_1)=(g_A\otimes\varepsilon_U)(x,y)$. The constant multiplies $w^2$ by a positive number, so it changes neither $W$ nor the sign of $c$ in $c\,w^2+\kappa$. For a real $(1,1)$-form $\rho$ we write $\rho(x)$ for the value of its hermitian form at $x$. By definition, $\beta$ satisfies (AM) if and only if $r_v(\beta)(x)\ge0$ for all $x\in T$ and all nonzero $v$ with $h_w(v,v)=0$.

**Lemma 6.1.** For $v,x\in T$ and $\ell\in U^*$:

1. $r_v(w^2)(x)=4\big[h_w(v,v)\,h_w(x,x)-|h_w(x,v)|^2\big]$;
2. $r_v([Z_\ell])(x)=\tfrac12\,|\pi_\ell v\wedge\pi_\ell x|^2$, where $\pi_\ell v\wedge\pi_\ell x\in\Lambda^2\mathbb C^2=\mathbb C$.

*Proof.* (1) Put $\lambda=h_w(\cdot,v)$, a $(1,0)$-form. As in Lemma 5.1, $\iota_vw=i\bar\lambda$ and $\iota_{\bar v}w=-i\lambda$, and now $\iota_{\bar v}\bar\lambda=h_w(v,v)$. So $\iota_{\bar v}\iota_v(w^2)=2\iota_{\bar v}(i\bar\lambda\wedge w)=2i\,h_w(v,v)\,w+2\,\lambda\wedge\bar\lambda$, and $r_v(w^2)=4h_w(v,v)\,w-4i\,\lambda\wedge\bar\lambda$. The hermitian forms of $w$ and $i\lambda\wedge\bar\lambda$ are $h_w$ and $|\lambda|^2$.

(2) Let $\omega_A=\tfrac i2(d\zeta_1\wedge d\bar\zeta_1+d\zeta_2\wedge d\bar\zeta_2)$ on $\mathbb C^2$, so that $\mathrm{vol}_A=\tfrac12\omega_A^2$ for the complex orientation. The form $\omega'=\pi_\ell^*\omega_A$ is a real $(1,1)$-form with hermitian form $h'(x,y)=\tfrac12H(\pi_\ell x,\pi_\ell y)$, by the same convention as $w$. Part (1) applied to $\omega'$ gives
$$r_v(\pi_\ell^*\mathrm{vol}_A)(x)=2\big[h'(v,v)h'(x,x)-|h'(x,v)|^2\big]=\tfrac12\big[|\pi_\ell v|^2|\pi_\ell x|^2-|H(\pi_\ell x,\pi_\ell v)|^2\big],$$
which is $\tfrac12|\pi_\ell v\wedge\pi_\ell x|^2$ by the Lagrange identity in $\mathbb C^2$. The script `theoremB_model.py` checks both formulas numerically. $\square$

For a quartic $p\in S^4U^*$ and $v,x\in T$, Lemma 6.1(2) and linearity in $p$ give
$$r_v(\mathrm{vol}_A\otimes p)(x)=\tfrac12\,\langle p,\ |Q_{v,x}|^2\rangle,\qquad Q_{v,x}(\ell)=\pi_\ell v\wedge\pi_\ell x. \tag{6.1}$$
Here $Q_{v,x}$ is a complex quadratic form in $\ell\in U^*$, $|Q_{v,x}|^2$ is a real quartic form on $U^*$, that is, an element of $S^4U$, and $\langle\ ,\ \rangle$ is the pairing between $S^4U^*$ and $S^4U$ with $\langle\ell^4,F\rangle=F(\ell)$. This is the natural duality, normalised in this way, and it is perfect. Both sides of (6.1) are linear in $p$, they agree at $p=\ell^4$ by Lemma 6.1(2), and the $\ell^4$ span $S^4U^*$.

**Lemma 6.2.** Let $P\subset S^4U$ be the cone of real quartic forms on $U^*$ that are nonnegative.

1. $P$ is the cone spanned by the products $s^2t^2$, $s,t\in U$, where $s$ is read as the linear form $\ell\mapsto\ell(s)$ on $U^*$.
2. $\Sigma_4=\{p\in S^4U^*:\ \langle p,F\rangle\ge0\text{ for all }F\in P\}$.

*Proof.* (1) A nonnegative binary quartic $F\ne0$ factors over $\mathbb R$ into linear forms and quadratic forms without real zeros. Its real zeros have even multiplicity, and we may take the quadratic factors positive definite. So $F$ is $s^2t^2$, $s^2q$ or $q_1q_2$ with $q,q_1,q_2$ positive definite, up to a positive factor. Each positive definite binary quadratic is $a^2+b^2$ with $a,b$ real linear forms, and expanding the products gives sums of terms $s^2t^2$.

(2) $\Sigma_4$ is a closed convex cone, so it is the dual of its dual cone. Its dual cone is $\{F:\langle\ell^4,F\rangle=F(\ell)\ge0\text{ for all }\ell\}=P$. $\square$

*Proof of Theorem B.* By the reduction above it suffices to treat $u=i$. Let $\beta=c\,w^2+\mathrm{vol}_A\otimes p\in M_i$. By Proposition 5.2, $\beta$ satisfies (AM). We evaluate the residue at two families of test pairs $(v,x)$.

Step 1: $c\le0$. Let $v_1\in\mathbb C^2$ be nonzero, $v=(v_1,0)$ and $x=(0,v_1)$. Then $h_w(v,v)=h_w(x,x)=0$ and $h_w(x,v)=-i|v_1|^2$, so Lemma 6.1(1) gives $r_v(w^2)(x)=-4|v_1|^4$. Also $\pi_\ell v=\ell_1v_1$ and $\pi_\ell x=\ell_2v_1$, so $Q_{v,x}=0$ and the quartic part contributes nothing by (6.1). Hence (AM) gives $-4c|v_1|^4\ge0$, so $c\le0$.

Step 2: $p\in\Sigma_4$. Let $v_1\in\mathbb C^2$ be nonzero, $s\in U$, and $v=v_1\otimes s=(s_1v_1,s_2v_1)$. Then $h_w(v,v)=is_1s_2\big(H(v_1,v_1)-H(v_1,v_1)\big)=0$. Let $x=(y_1,y_2)$ with $H(y_1,v_1)=H(y_2,v_1)=0$. Then $h_w(x,v)=i\big(s_2H(y_1,v_1)-s_1H(y_2,v_1)\big)=0$, so $r_v(w^2)(x)=0$ by Lemma 6.1(1). Since $\pi_\ell v=\ell(s)v_1$,
$$Q_{v,x}(\ell)=\ell(s)\,m(\ell),\qquad m(\ell)=\ell_1\,v_1\wedge y_1+\ell_2\,v_1\wedge y_2 .$$
The numbers $v_1\wedge y_k$ run over all of $\mathbb C$ as $y_k$ runs over the line $v_1^\perp$, so $m$ is an arbitrary complex linear form on $U^*$. By (6.1), (AM) gives $\langle p,\ s^2|m|^2\rangle\ge0$. Write $m=t+it'$ with $t,t'\in U$. Then $|m|^2=t^2+t'^2$, and taking $t'=0$ we get $\langle p,s^2t^2\rangle\ge0$ for all $s,t\in U$. By Lemma 6.2, $p\in\Sigma_4$. $\square$

The script `theoremB_model.py` checks Lemma 6.1, the test pairs of Steps 1 and 2, and formula (6.1) at the quartic $X^4-0.6X^2Y^2+Y^4$. This quartic is positive, but its residue at a test pair of Step 2 with $s=e_1$ and $y_1=0$ is negative, and equals the value that (6.1) predicts. So it is not in $\Sigma_4$ (Section 7). As a control, $-w^2+\mathrm{vol}_A\otimes(X^4+Y^4)$, which lies in the cone, has smallest residue eigenvalue $0$ up to rounding over 30 random null vectors. For the positive quartic above the same quantity is $-0.94$.

**Remark 6.3.** The proof gives more than Theorem B. On $\mathrm{Hdg}^4(T_u)\otimes\mathbb R$ the three cones
$$M,\qquad\{\beta:\beta\text{ satisfies (AM)}\},\qquad\mathbb R_{\ge0}(-w^2)+\Sigma_4$$
coincide. Indeed the first lies in the second by Proposition 5.2, the second in the third by the proof above, and the third in the first by Corollary 4.4. So, on Hodge classes, the wall metrics impose no condition beyond the asymptotic one. The proof uses only the null vectors $v=v_1\otimes s$ with $s\in U$.

## 7. The quartic form and its consequences

In this section $u$ is very general, and we use the coordinates of Section 6: $X,Y$ is the basis of $U^*$ dual to $e_1,e_2$, and $\ell=\ell_1X+\ell_2Y$. By Theorem B,
$$M=\{c\,w^2+\mathrm{vol}_A\otimes p:\ c\le0,\ p\in\Sigma_4\}.$$

### 7.1 Sums of fourth powers

Write a quartic as $p=\sum_{k=0}^4\binom4ka_kX^{4-k}Y^k$ and put $H_p=(a_{i+j})_{0\le i,j\le2}$, the Hankel (catalecticant) matrix of $p$. The map $p\mapsto H_p$ is a linear isomorphism onto the $5$-dimensional space of Hankel matrices.

**Lemma 7.1.** $p\in\Sigma_4$ if and only if $H_p\ge0$. The interior of $\Sigma_4$ is $\{H_p>0\}$.

*Proof.* For $\ell^4$ we have $a_k=\ell_1^{4-k}\ell_2^k$. For a real quadratic form $q(\ell)=\sum_iq_i\ell_1^{2-i}\ell_2^i$ on $U^*$, this gives $\langle\ell^4,q^2\rangle=q(\ell)^2=\sum_{i,j}q_iq_ja_{i+j}$, so $\langle p,q^2\rangle=q^{\mathsf T}H_pq$ for all $p$ by linearity. By Lemma 6.2(1) every $F\in P$ is a sum of products $s^2t^2=(st)^2$, so $P$ is the cone of sums of squares $q^2$. By Lemma 6.2(2), $p\in\Sigma_4$ if and only if $q^{\mathsf T}H_pq\ge0$ for all $q$. The second claim follows because $p\mapsto H_p$ is a linear isomorphism. $\square$

Let $P^\vee\subset S^4U^*$ be the cone of quartics $p$ with $p(x)\ge0$ for all $x\in U$. Every fourth power is nonnegative, so $\Sigma_4\subseteq P^\vee$.

**Proposition 7.2.** The set $P^\vee\setminus\Sigma_4$ contains a nonempty open subset of $S^4U^*$. Hence there are rational classes $\kappa\in K_5$ with $\kappa=\mathrm{vol}_A\otimes p$, $p$ positive on $U\setminus0$ and $p\notin\Sigma_4$. For such $\kappa$, no coherent sheaf $\mathcal F$ of positive rank on $T_u$ has $\beta(\mathcal F)\in\mathbb R\,w^2+\mathbb R_{>0}\,\kappa$.

*Proof.* Let $p_0=X^4-0.6X^2Y^2+Y^4=(X^2-0.3Y^2)^2+0.91Y^4$. It is positive on $U\setminus0$, and $a_2=-0.1$, so the middle entry of $H_{p_0}$ is negative and $p_0\notin\Sigma_4$ by Lemma 7.1. Both properties are open: positivity on the unit circle by compactness, and $p\notin\Sigma_4$ because $\Sigma_4$ is closed. Since $K_5$ is dense in $K_5\otimes\mathbb R$, the open set contains rational classes. If $\beta(\mathcal F)=c\,w^2+t\kappa$ with $t>0$, Theorems A and B give $t\,p\in\Sigma_4$, a contradiction. $\square$

At a test pair of Step 2 of Section 6 with $s=e_1$, $y_1=0$, formula (6.1) gives $r_v(\mathrm{vol}_A\otimes p_0)(x)=\tfrac12a_2\,|v_1\wedge y_2|^2<0$. The script `theoremB_model.py` confirms this value.

The cone $P^\vee$ is what a pointwise curvature argument gives. Call a unitary connection on a bundle over $T_u$ *hyperholomorphic* if its curvature has type $(1,1)$ for every $L_{u'}$, $u'\in S^2$.

**Remark 7.3.** If $E$ carries a hyperholomorphic connection $\nabla$, then the $K_5$-component of $\beta(E)$ is $\mathrm{vol}_A\otimes p$ with $p\in P^\vee$. For $x\in U$ let $\iota_x\colon A\to V_{\mathbb R}$, $a\mapsto a\otimes x$. The pullback $\iota_x^*$ of a 4-form contracts its $U$-slots with $x^{\otimes4}\in S^4U$, so it kills every summand of $\Lambda^4(A\otimes U)^*$ except $\Lambda^4A^*\otimes S^4U^*$, and $\iota_x^*(\mathrm{vol}_A\otimes p)=p(x)\,\mathrm{vol}_A$ because $\pi_\ell\circ\iota_x=\ell(x)$. So the $K_5$-component of a 4-form $\gamma$ is $\mathrm{vol}_A\otimes p_\gamma$ with $\iota_x^*\gamma=p_\gamma(x)\,\mathrm{vol}_A$. Now the real 2-forms of type $(1,1)$ for every $L_{u'}$ are the $\mathrm{Sp}(1)\times1$-invariant ones, namely $\mathbb R\,w\oplus\Lambda^2_R\otimes S^2U^*$, where $\Lambda^2_R\subset\Lambda^2A^*$ is spanned by the forms $g_A(R_{u'}\cdot,\cdot)$. These are anti-self-dual for the orientation of $\mathrm{vol}_A$, because the forms $g_A(L_{u'}\cdot,\cdot)$ are Kähler forms and hence self-dual. Since $\iota_x^*w=0$, the restriction $\iota_x^*F^\circ$ takes values in $\Lambda^2_R\otimes\mathfrak u(r)$, say $\iota_x^*F^\circ=\sum_{a=1}^3\sigma_a\otimes\Phi_a(x)$ with $(\sigma_a)$ an orthonormal basis of $\Lambda^2_R$. As $\sigma_a\wedge\sigma_b=-\delta_{ab}\mathrm{vol}_A$,
$$\iota_x^*\,\mathrm{tr}(F^\circ\wedge F^\circ)=-\sum_a\mathrm{tr}\big(\Phi_a(x)^2\big)\,\mathrm{vol}_A=\sum_a|\Phi_a(x)|^2\,\mathrm{vol}_A$$
at every point of $T_u$. The class $8\pi^2\beta(E)$ is represented by the average of $\mathrm{tr}(F^\circ\wedge F^\circ)$ over $T_u$ (Section 3.3), so its $K_5$-component is $\mathrm{vol}_A$ times an average of nonnegative quartics. By Proposition 7.2, Theorem A excludes an open set of classes that this argument allows.

**Lemma 7.4.** For every $u'\in S^2$ and $\ell\ne0$, the class $[Z_\ell]$ is represented on $T_{u'}$ by a nonzero positive $(2,2)$-form, and $[Z_\ell]\cdot\omega^2>0$ for every Kähler form $\omega$ on $T_{u'}$.

*Proof.* Let $\omega_A=g_A(L_{u'}\cdot,\cdot)$, a Kähler form on $(A,L_{u'})$ with $\mathrm{vol}_A=\tfrac12\omega_A^2$. Since $\pi_\ell$ is complex linear, $\alpha=\pi_\ell^*\omega_A$ is a semipositive $(1,1)$-form of rank $2$, and $[Z_\ell]=\tfrac12\alpha^2$, a positive $(2,2)$-form. We may take $\omega$ constant. In an $\omega$-unitary frame that diagonalises $\alpha$, $\alpha=l_1e_1+l_2e_2$ with $l_1,l_2>0$, so $\tfrac12\alpha^2\wedge\omega^2=l_1l_2\,e_1\wedge e_2\wedge\omega^2=2l_1l_2\,\mathrm{vol}>0$. $\square$

### 7.2 Rational points

Let $B_0\subset B$ be the elements of reduced trace $0$. For $y\in B_0$ we have $y^2=-\mathrm{nrd}(y)\in\mathbb Q$, and the *conic of $B$* is $C_B=\{[y]\in\mathbb P(B_0):y^2=0\}$. It has no rational point, because $B$ is a division algebra. The group $B^\times$ acts on $V_{\mathbb Q}$ and hence on $K_5$ (Lemma 2.2(4)). Its Lie algebra $B$ acts by $\mathbb Q$-linear maps $D_y$, $y\in B$. Over $\mathbb R$, $B\otimes\mathbb R=\mathrm{End}(U)$ acts on $K_5\otimes\mathbb R=\mathrm{vol}_A\otimes S^4U^*$ through the second factor, by $(D_yp)(x)=\pm\,dp_x(yx)$ for $x\in U$; the sign depends on conventions and plays no role.

**Lemma 7.5.** Let $\Gamma\subset\mathbb P(K_5\otimes\mathbb C)$ be the curve of lines $[\mathrm{vol}_A\otimes\ell^4]$, $\ell\in U^*\otimes\mathbb C$. For $[y]\in C_B(\mathbb C)$, the kernel of $D_y$ on $K_5\otimes\mathbb C$ is a line, and $[y]\mapsto\ker D_y$ is a bijection $C_B(\mathbb C)\to\Gamma$ that commutes with $\mathrm{Gal}(\bar{\mathbb Q}/\mathbb Q)$ on $\bar{\mathbb Q}$-points. It maps $C_B(\mathbb R)$ onto the lines $\mathbb R[Z_\ell]$, $\ell\in U^*$ real.

*Proof.* A nonzero $y\in\mathrm{End}(U_{\mathbb C})$ with $y^2=0$ is $y=u_0\otimes\ell$, that is $y(x)=\ell(x)u_0$, with $\ell(u_0)=0$. Then $(D_yp)(x)=\pm\ell(x)\,\partial_{u_0}p(x)$, which vanishes if and only if $p$ is a function of $\ell$ alone, that is $p\in\mathbb C\ell^4$. Conversely $\ell$ determines $[y]$, since $u_0$ spans $\ker\ell$. The map commutes with Galois because $D$ is defined over $\mathbb Q$. If $y$ is real, so is $\ell$ up to a scalar. $\square$

**Proposition 7.6.**

1. The extreme rays of $\Sigma_4$ are the rays $\mathbb R_{>0}[Z_\ell]$, $\ell\in\mathbb P^1(\mathbb R)$, which correspond to the real points of $C_B$ by Lemma 7.5. No nonzero rational class in $K_5$ spans an extreme ray of $\Sigma_4$.
2. Let $\kappa\in K_5$ be rational with $\kappa=\lambda_1[Z_{\ell_1}]+\lambda_2[Z_{\ell_2}]$, $\lambda_1,\lambda_2>0$ and $[\ell_1]\ne[\ell_2]$. Then there are a real quadratic field $k\subset B$ and an element $z\in K_5\otimes k$ with $\kappa=\mathrm{Tr}_{k/\mathbb Q}z$, such that the two real embeddings of $k$ map $z$ to $\lambda_1[Z_{\ell_1}]$ and $\lambda_2[Z_{\ell_2}]$.

*Proof.* (1) $\Sigma_4$ is the cone over the convex hull of the compact set $\{\ell^4:|\ell|=1\}$, so every extreme ray is spanned by some $\ell^4$. Conversely, if $\ell^4=\sum_jc_j\ell_j^4$ with $c_j>0$, evaluating at $x\ne0$ with $\ell(x)=0$ gives $\ell_j(x)=0$ for all $j$, so every $\ell_j$ is proportional to $\ell$. Now suppose that $\kappa\in K_5$ is rational and spans $\mathbb R_{>0}[Z_\ell]$. The space $\{y\in B_0:D_y\kappa=0\}$ is defined over $\mathbb Q$, and its real span is $\{y\in\mathrm{End}(U):\mathrm{tr}\,y=0,\ D_y\ell^4=0\}$. Since $D_y\ell^4=\pm4\ell^3\,(\ell\circ y)$, the condition is $y(U)\subseteq\ker\ell$, and with $\mathrm{tr}\,y=0$ it gives $y\in\mathbb R\,(u_0\otimes\ell)$, where $u_0$ spans $\ker\ell$. So it contains a nonzero $y\in B_0$ with $y^2=0$, which is impossible.

(2) Any five distinct points of $\Gamma$ are linearly independent (Vandermonde). Two different secant lines of $\Gamma$ through $[\kappa]$ would therefore meet only in $0$, or only in a point of $\Gamma$ if they share one, and $[\kappa]\notin\Gamma$ because $\lambda_1,\lambda_2\ne0$. Hence $[\kappa_1],[\kappa_2]$, with $\kappa_i=[Z_{\ell_i}]$, are the only points $a\in\Gamma$ for which some $b\in\Gamma\setminus\{a\}$ has $\kappa\in\mathrm{span}(a,b)$. This set is the image in $\Gamma$ of the fibre over $[\kappa]$ of the incidence correspondence $\{(a,b,[k]):a\ne b,\ [k]\in\mathrm{span}(a,b)\}\subset\Gamma\times\Gamma\times\mathbb P(K_5\otimes\mathbb C)$. The curve $\Gamma$ is defined over $\mathbb Q$ by Lemma 7.5, so the correspondence is constructible and defined over $\mathbb Q$, and $[\kappa]$ is a rational point. Hence the set is constructible and defined over $\mathbb Q$. It is finite, so it consists of $\bar{\mathbb Q}$-points and is stable under $\mathrm{Gal}(\bar{\mathbb Q}/\mathbb Q)$. This uses only the rationality of $\kappa$; a priori $\ell_1,\ell_2$ are arbitrary real forms. Neither point is rational, since by Lemma 7.5 it would give a rational point of $C_B$. So the two points are conjugate over a quadratic field $k$ and are defined over $k$. Complex conjugation fixes each of them, since they are real, so it does not induce the nontrivial automorphism $\sigma$ of $k$, and $k$ is real. Choose $z_1\in K_5\otimes k$ spanning $[\kappa_1]$. Then $\sigma(z_1)$ spans $[\kappa_2]$, and $\kappa=\mu z_1+\mu'\sigma(z_1)$ with $\mu,\mu'\in k$. Applying $\sigma$ gives $\mu'=\sigma(\mu)$, so $\kappa=\mathrm{Tr}_{k/\mathbb Q}z$ with $z=\mu z_1$. The two real embeddings send $z$ to the components of $\kappa$ along $[\kappa_1]$ and $[\kappa_2]$, which are $\lambda_1\kappa_1$ and $\lambda_2\kappa_2$.

It remains to embed $k$ in $B$. By Lemma 7.5 there are $y_1\in B_0\otimes k$ with $y_1^2=0$ and $y_2=\sigma(y_1)$ corresponding to $[\kappa_1],[\kappa_2]$. For $x,y\in B_0$, $xy+yx=(x+y)^2-x^2-y^2$ is a scalar, equal to $\mathrm{trd}(xy)$. So $y_1y_2+y_2y_1=t$ with $t=\mathrm{trd}(y_1y_2)$, and $t\in\mathbb Q$ because it is $\sigma$-invariant. Over $\mathbb R$, $y_i=u_i\otimes\ell_i$ and $t=\ell_1(u_2)\,\ell_2(u_1)\ne0$, since $[\ell_1]\ne[\ell_2]$. Put $x=y_1y_2-y_2y_1$. From $y_i^2=0$ we get $(y_1y_2)^2=y_1(t-y_1y_2)y_2=t\,y_1y_2$, similarly for $y_2y_1$, and hence $x^2=t(y_1y_2+y_2y_1)=t^2$. Write $k=\mathbb Q(\sqrt d)$. Since $\sigma(x)=-x$, $b=x/\sqrt d$ lies in $B$, and $b^2=t^2/d$ is not a square in $\mathbb Q$. So $\mathbb Q(b)\cong k$. $\square$

If $p=\sum_jc_j\ell_j^4$ with $c_j>0$, then $H_p=\sum_jc_jv_jv_j^{\mathsf T}$ with $v_j=(\ell_{j,1}^2,\ell_{j,1}\ell_{j,2},\ell_{j,2}^2)$, so the rank of $H_p$ is the number of distinct $[\ell_j]$ if this is at most $3$, and $3$ otherwise. Rank $1$ gives the extreme rays, rank $2$ the classes of (2), and rank $3$ the interior of $\Sigma_4$ (Lemma 7.1). So a nonzero rational class of $M\cap K_5$ has rank $2$, and is then a Galois trace as in (2), or rank $3$. The script `s7_checks.py` verifies the identities used in Lemmas 7.1 and 7.5, Propositions 7.2 and 7.6, and Remark 7.3 in exact arithmetic.

### 7.3 The $K_5$-slice

**Remark 7.7.** Every class $\kappa\in M\cap(K_5\otimes\mathbb R)$ lies on the boundary of $M$, because $\kappa+\epsilon w^2\notin M$ for $\epsilon>0$. In terms of Section 6, the residue of $\kappa$ vanishes at the test pairs of Step 1, while that of $w^2$ is negative there. So a coherent sheaf $\mathcal F$ with $\beta(\mathcal F)\in K_5\otimes\mathbb R$ would sit on the boundary of the cone allowed by Theorem A. By the remark at the end of Section 3, $\beta(\mathcal F)$ is a sum of the $\beta$'s of wall-stable torsion-free sheaves $\mathcal G_i$ and a nonnegative multiple of $-w^2$, and each $\beta(\mathcal G_i)$ lies in $M$. If $\beta(\mathcal F)\in K_5\otimes\mathbb R$, the multiple of $-w^2$ is $0$ and each summand has $w^2$-coefficient $0$, so each summand lies in $M\cap(K_5\otimes\mathbb R)$ as well.

### 7.4 Weil planes

Voisin's example [1, §3] is a complex torus of Weil type. The tori $T_u$ are of Weil type for every imaginary quadratic subfield of $B$ at once, and all their Weil classes lie in $K_5$.

Let $z\in B_0$ with $z^2=-m$, $m\in\mathbb Q_{>0}$. Such $z$ exist, because on $B_0\otimes\mathbb R=\mathfrak{sl}_2(\mathbb R)$ the reduced norm is the determinant, which takes positive values, and $B_0$ is dense in $B_0\otimes\mathbb R$. The element $z$ acts on $V_{\mathbb Q}$ and commutes with $G$, so it is a rational endomorphism of $T_u$ for every $u$, and $V_{\mathbb Q}$ is a vector space of dimension $4$ over the imaginary quadratic field $K'=\mathbb Q(z)$. On $V_{\mathbb R}=A\otimes U$ it acts as $1\otimes z$ with $z\in\mathrm{End}(U)$ (Section 2.1), and $z/\sqrt m$ is a complex structure on $U$. The $(1,0)$-space of $T_u$ is $A^{1,0}\otimes U_{\mathbb C}$, where $A^{1,0}$ is the $i$-eigenspace of $L_u$ on $A_{\mathbb C}$ and has dimension $2$. So $z$ acts on it with eigenvalues $i\sqrt m$ and $-i\sqrt m$, each of multiplicity $2$, and $(T_u,K')$ is of Weil type in the sense of [1, §3] (Voisin's field is $\mathbb Q(i)$; here it is $K'$). Let $\ell_+\in U^*_{\mathbb C}$ be nonzero with $\ell_+\circ z=i\sqrt m\,\ell_+$, and put $\ell_-=\bar\ell_+$. Extending the notation of Section 7.2, let $D_z$ be the action of $z$ on $\Lambda^\bullet V_{\mathbb Q}^*$ as a derivation, and define the *Weil plane*
$$W_z=\ker\big(D_z^2+16m\big)\subset\Lambda^4V_{\mathbb Q}^*.$$

**Proposition 7.8.** Let $z$ be as above.

1. $W_z$ is the space of Weil classes of $(T_u,\mathbb Q(z))$. It is a $2$-dimensional subspace of $K_5$, and $W_z\otimes\mathbb R=\{\mathrm{vol}_A\otimes\mathrm{Re}(c\,\ell_+^4):c\in\mathbb C\}$.
2. Every nonzero class in $W_z\otimes\mathbb R$ is $\mathrm{vol}_A\otimes p$ with $p$ taking both signs on $U$. Hence $W_z\otimes\mathbb R$ meets $P^\vee$ and $-P^\vee$, and therefore $\Sigma_4$ and $-\Sigma_4$, only in $0$.
3. If $u$ is very general, no coherent sheaf $\mathcal F$ of positive rank on $T_u$ has $\beta(\mathcal F)\in\mathbb R\,w^2+\big(W_z\otimes\mathbb R\setminus0\big)$.
4. The planes $W_z$, over all such $z$, span $K_5$.

*Proof.* (1) Over $\mathbb C$, $V_{\mathbb C}^*=A_{\mathbb C}^*\otimes U_{\mathbb C}^*$ is the sum of the eigenspaces $V_\pm^*=A_{\mathbb C}^*\otimes\ell_\pm$ of $z$, each of dimension $4$, with eigenvalues $\pm i\sqrt m$ (for one sign convention for $D_z$). So $D_z$ acts on $\Lambda^aV_+^*\otimes\Lambda^{4-a}V_-^*$ by $(2a-4)\,i\sqrt m$, and $D_z^2+16m$ vanishes there exactly for $a\in\{0,4\}$. Hence $W_z\otimes\mathbb C=\Lambda^4V_+^*\oplus\Lambda^4V_-^*$. This is the complexification of the space of Weil classes in [1, §3], with cohomology in place of homology, so $\dim W_z=2$. The line $\Lambda^4V_+^*$ is spanned by $\pi_{\ell_+}^*\mathrm{vol}_A$, where $\pi_{\ell_+}(a\otimes s)=\ell_+(s)\,a$. The computation in the proof of Lemma 2.2(3) holds for complex $\ell$ as well and identifies this form with $\mathrm{vol}_A\otimes\ell_+^4$. The same holds for $\ell_-$, so $W_z\otimes\mathbb C\subset K_5\otimes\mathbb C$, and since $\ell_-=\bar\ell_+$, the real points are the classes $\mathrm{vol}_A\otimes\mathrm{Re}(c\,\ell_+^4)$. Both $W_z$ and $K_5$ are rational, so $W_z\subseteq K_5$.

(2) Choose a basis of $U$ in which $z/\sqrt m$ is the rotation by $\pi/2$, with coordinates $s,t$. Then $\ell_+$ is a multiple of $s+it$. Writing $s+it=\rho e^{i\theta}$, every class in $W_z\otimes\mathbb R$ is $\mathrm{vol}_A\otimes p$ with $p=|c|\rho^4\cos(4\theta+\arg c)$ for some $c\in\mathbb C$. If $c\ne0$, $p$ takes both signs. The elements of $P^\vee$ are nonnegative, and $\Sigma_4\subseteq P^\vee$.

(3) If $\beta(\mathcal F)=c\,w^2+\kappa$ with $\kappa\in W_z\otimes\mathbb R$, then $\kappa\in\Sigma_4$ by Theorems A and B, so $\kappa=0$ by (2).

(4) An element $b\in B^\times$ acts on $V_{\mathbb Q}$ and conjugates $D_z$ into $D_{z'}$, where $z'$ is a conjugate of $z$ in $B$. So $z'\in B_0$, $z'^2=-m$, and $b$ maps $W_z$ onto $W_{z'}$. Hence the span of all Weil planes is a nonzero $B^\times$-stable subspace of $K_5$, and it equals $K_5$ by Lemma 2.2(4). $\square$

The script `weil_planes.py` computes the commutant of $\mathrm{Lie}\,G$ in $\mathrm{End}(V_{\mathbb Q})$, which has dimension $4$, finds an element $z$ in it with trace $0$ and $z^2=-88$, and checks in exact arithmetic that $\ker(D_z^2+16m)$ has dimension $2$, lies in $H^4_G$ and is orthogonal to $w^2$. It also checks (4) directly: together with the Weil planes of three conjugates $bzb^{-1}$, $W_z$ spans a $5$-dimensional subspace of $H^4_G$ orthogonal to $w^2$, that is, all of $K_5$. As a numerical check at $u_0$, each of the two basis classes of $W_z$ pairs with $\omega^2$ with both signs over 60 random Kähler forms $\omega$, while $\omega_1^2\cdot\omega^2>0$ for Kähler forms $\omega_1,\omega$ (control).

**Remark 7.9.** In Voisin's example the Weil classes are orthogonal to $[\omega]^2$ for a Kähler class $[\omega]$ compatible with the action of $K'$, and this gives (H3) there [1, §3]. The same argument works for each plane $W_z$. Let $\omega$ be a Kähler form with $D_z\omega=0$, for example $\omega=g(L_u\cdot,\cdot)$ with $g=g_A\otimes g_U$ and $g_U$ an inner product on $U$ for which $z/\sqrt m$ is orthogonal. The trace of $z$ on $V_{\mathbb R}$ is $0$, so $D_z$ kills $\Lambda^8V_{\mathbb R}^*$, and $D_z(\omega^2)=2\,\omega\wedge D_z\omega=0$. Hence $(D_z\kappa)\cdot\omega^2=-\kappa\cdot D_z(\omega^2)=0$ for every $\kappa\in\Lambda^4V_{\mathbb R}^*$, and since $D_z$ is invertible on $W_z$, $W_z\cdot\omega^2=0$. The script `weil_planes.py` confirms that these products vanish up to rounding for 20 such forms. So (H3) holds for each Weil plane separately, with a Kähler class that depends on $z$, but it fails for their span $K_5$ and every Kähler class (Remark 2.5). Since every nonzero class of $\Sigma_4$ pairs positively with $\omega^2$ (Lemma 7.4), this gives a second proof that $W_z\otimes\mathbb R$ meets $\pm\Sigma_4$ only in $0$, although not the stronger statement about $P^\vee$.

## 8. What a carrier would look like

In this section $u$ is very general. Call a coherent sheaf $\mathcal F$ of positive rank on $T_u$ a *carrier* if $\beta(\mathcal F)\notin\mathbb Q\,w^2$, that is, if the $K_5$-component of $\beta(\mathcal F)$ is nonzero. Since $c_1(\mathcal F)\in\mathbb Q w$, this holds if and only if the $K_5$-component of $\mathrm{ch}_2(\mathcal F)$ is nonzero. By the remark after Lemma 2.2, carriers exist if and only if the classes $\mathrm{ch}_2$ of coherent sheaves on $T_u$ span $H^4_G$. We do not know whether carriers exist. The ray $\mathbb R_{\ge0}(-w^2)$ of $M$ contains $\beta(L\oplus L^{-1})$ (Step 1 of the proof of Theorem A), and a carrier is exactly a sheaf whose $\beta$ lies on some other ray of $M$.

Let $\mathcal F$ be coherent of positive rank with torsion subsheaf $\mathcal T$, and let $\mathcal G_1,\dots,\mathcal G_m$ be the quotients of the filtration of $\mathcal F/\mathcal T$ in Step 3 of the proof of Theorem A. Write $\beta(\mathcal F)=c\,w^2+\mathrm{vol}_A\otimes p$ and $\beta(\mathcal G_i)=c_i\,w^2+\mathrm{vol}_A\otimes p_i$.

**Proposition 8.1.** Let $\mathcal F$ be a carrier.

1. $c\le\sum_ic_i$, every $c_i\le0$, every $p_i$ lies in $\Sigma_4$, and $p=\sum_ip_i$. If $\mathcal G_i$ has rank $1$, then $c_i=0$ and $p_i=0$. So some $\mathcal G_i$ of rank at least $2$ is a carrier. Each $\mathcal G_i$ is torsion-free with no coherent subsheaf of intermediate rank, and $\mathcal G_i^{**}$ is stable for every $\omega\in W$ and has finite singular set.
2. If $c=0$, then every $c_i=0$, and all $\mathcal G_i$ have the same $c_1/\mathrm{rk}$ in $\mathbb Q w$.
3. The Hankel matrix $H_p$ has rank $2$ or $3$, and so does $H_{p_i}$ for every carrier $\mathcal G_i$. In rank $2$ the class $\mathrm{vol}_A\otimes p$, respectively $\mathrm{vol}_A\otimes p_i$, is a Galois trace as in Proposition 7.6(2).

*Proof.* (1) Steps 3 and 4 of the proof of Theorem A give $\beta(\mathcal F)=\sum_i\beta(\mathcal G_i)+\sum_it_i(-w^2)$ with $t_i\ge0$. The sum $\mathbb Q w^2\oplus K_5$ is direct, so $p=\sum_ip_i$ and $c=\sum_ic_i-\sum_it_i$. By Theorems A and B, $\beta(\mathcal G_i)\in M$, so $c_i\le0$ and $p_i\in\Sigma_4$. If $\mathcal G_i$ has rank $1$, then $\mathcal G_i^{**}$ is reflexive of rank $1$, hence a line bundle $L$, and $\mathrm{ch}_2(\mathcal G_i)=c_1(L)^2/2$ by Corollary 2.4. So $\beta(\mathcal G_i)=0$. The remaining properties are Step 2 of the proof of Theorem A.

(2) If $c=0$, then $\sum_ic_i=\sum_it_i$, where the left side is $\le0$ and the right side is $\ge0$. So all $c_i$ and $t_i$ vanish. In Lemma 3.9 write $\xi=a\,w$ with $a\in\mathbb Q$. Then the coefficient of $-w^2$ is $r'r''a^2/2r$, so $t_i=0$ gives $c_1(\mathcal F_{i-1})/\mathrm{rk}\,\mathcal F_{i-1}=c_1(\mathcal G_i)/\mathrm{rk}\,\mathcal G_i$ for $i\ge2$. Induction on $i$ gives the claim.

(3) The classes $\beta(\mathcal F)$ and $\beta(\mathcal G_i)$ are rational, and $\mathbb Q w^2\oplus K_5$ is a decomposition over $\mathbb Q$. So $\mathrm{vol}_A\otimes p$ and $\mathrm{vol}_A\otimes p_i$ are rational classes of $M\cap K_5$, nonzero for carriers. The paragraph after Proposition 7.6 gives the claim. $\square$

If $c=0$, Remark 7.7 adds that every $\mathcal G_i$ lies on the face $M\cap(K_5\otimes\mathbb R)$ of $M$.

The next statement shows that for stable locally free carriers the choice of fibre in the twistor family does not matter. Let $\omega_{u'}=g(L_{u'}\cdot,\cdot)$ be the Kähler form of the flat hyperkähler metric on $T_{u'}$, as in Section 3.4.

**Proposition 8.2.** Let $u'\in S^2$, and let $E'$ be an $\omega_{u'}$-stable holomorphic vector bundle on $T_{u'}$ with $c_1(E')\in\mathbb Q w$ and $c_2(E')\in H^4_G$. Then $E'$ carries a compatible unitary connection $\nabla$ whose curvature has type $(1,1)$ for every $L_{u''}$, $u''\in S^2$. For every $u''$, $\nabla$ defines a holomorphic vector bundle on $T_{u''}$ with the same Chern classes as $E'$, and $\nabla$ is Hermitian–Einstein for $\omega_{u''}$.

*Proof.* The group $\mathrm{Sp}(1)\times1\subset G(\mathbb R)$ is the group $\mathrm{SU}(2)$ that the flat hyperkähler structure $(L_i,L_j,L_k)$ induces on cohomology (proof of Lemma 2.3). It fixes $w$ (Lemma 2.2(2)) and every class of $H^4_G$, so $c_1(E')$ and $c_2(E')$ are $\mathrm{SU}(2)$-invariant. By Verbitsky's theorem [3, Thm. 2.24], $E'$ admits a compatible hyperholomorphic connection $\nabla$. By definition $\nabla$ is integrable for every induced complex structure [3, Def. 2.17], which means that its curvature has type $(1,1)$ for every $L_{u''}$ [3, Thm. 2.16]. Integrability for $L_{u''}$ gives the holomorphic bundle on $T_{u''}$, and its Chern classes are those of the underlying complex vector bundle. By [3, Prop. 2.22], the curvature $\Theta$ of $\nabla$ satisfies $\Lambda\Theta=0$ for $\omega_{u''}$, so $\nabla$ is Hermitian–Einstein for $\omega_{u''}$ (Yang–Mills in the terminology of [3, Def. 2.20]). $\square$

For very general $u$ we have $\omega_u\in W$. So by Lemma 3.8 a locally free sheaf on $T_u$ with no coherent subsheaf of intermediate rank is $\omega_u$-stable, and its Chern classes lie in $\mathrm{NS}(T_u)=\mathbb Q w$ and $\mathrm{Hdg}^4(T_u)=H^4_G$. Proposition 8.2 therefore applies to it with $u'=u$. This covers every carrier $\mathcal F$ with a carrier factor $\mathcal G_i$ (Proposition 8.1) whose double dual is locally free, because $\mathcal G_i^{**}$ has no coherent subsheaf of intermediate rank (Step 2 of the proof of Theorem A) and $\beta(\mathcal G_i^{**})=\beta(\mathcal G_i)$ by Corollary 2.4. There are two consequences.

First, a locally free carrier $E$ with no coherent subsheaf of intermediate rank carries a hyperholomorphic connection. So Remark 7.3 applies to it, and the $K_5$-component of $\beta(E)$ is $\mathrm{vol}_A\otimes p$ with $p\in P^\vee$. Theorems A and B give $p\in\Sigma_4$, which excludes the nonempty open set $P^\vee\setminus\Sigma_4$ of Proposition 7.2.

Second, such a carrier $E$ gives a holomorphic bundle with the same Chern classes on every fibre $T_{u''}$, among them the CM fibre $T_{u_0}$, which is isogenous to $X_1\times X_2$ (Section 2.4). Conversely, an $\omega_{u_0}$-stable bundle $E'$ on $T_{u_0}$ with $c_1(E')\in\mathbb Q w$, $c_2(E')\in H^4_G$ and $\beta(E')\notin\mathbb Q w^2$ gives a locally free carrier on $T_u$. So a search for locally free carriers may be carried out on $T_{u_0}$, where the Néron–Severi group is larger, provided that stability is taken with respect to $\omega_{u_0}$ and the Chern classes lie in $H^4_G$.

Proposition 8.2 concerns locally free sheaves only. It says nothing about a carrier whose carrier factors $\mathcal G_i$ all have a double dual with nonempty singular set. For such a carrier we know only the constraints of Theorems A and B and Proposition 8.1.

## References

[1] C. Voisin, A counterexample to the Hodge conjecture for Kähler varieties, Int. Math. Res. Not. 2002, no. 20, 1057–1075; arXiv:math/0112247.

[2] E. Markman, Cycles on abelian 2n-folds of Weil type from secant sheaves on abelian n-folds, arXiv:2502.03415.

[3] M. Verbitsky, Trianalytic subvarieties of the Hilbert scheme of points on a K3 surface, Geom. Funct. Anal. 8 (1998), no. 4, 732–782; arXiv:alg-geom/9705004.

[4] V. Muñoz, Spin(7)-instantons, stable bundles and the Bogomolov inequality for complex 4-tori, J. Math. Pures Appl. (9) 102 (2014), no. 1, 124–152; arXiv:1302.2846.

[5] S. Bando, Y.-T. Siu, Stable sheaves and Einstein–Hermitian metrics, in: Geometry and Analysis on Complex Manifolds, World Sci. Publ., River Edge, NJ, 1994, 39–50.

[6] X. Chen, S. Sun, Reflexive sheaves, Hermitian–Yang–Mills connections, and tangent cones, Invent. Math. 225 (2021), no. 1, 73–129; arXiv:1912.09561.

[7] G. Tian, Gauge theory and calibrated geometry I, Ann. of Math. (2) 151 (2000), 193–268; arXiv:math/0010015.

[8] J. Grivaux, Chern classes in Deligne cohomology for coherent analytic sheaves, Math. Ann. 347 (2010), no. 2, 249–284; arXiv:0712.2207.
