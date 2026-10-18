# Hodge correspondences through fixed CM curve factors

## 1. The result

Let $C$ be a smooth projective complex curve, let $a,b\in\mathbb C(C)$, and suppose that $x^3+ax+b$ is separable over $\mathbb C(C)$. We consider a smooth projective surface $S$ with function field

$$
\mathbb C(S)=\mathbb C(C)(x,r),\qquad r^4=x^3+ax+b. \tag{1}
$$

The transformations $g:r\mapsto ir$ and $\delta=g^2:r\mapsto-r$ are birational automorphisms. We may replace $S$ by an equivariant smooth projective model. Let $Y$ be a smooth projective model of the even quotient,

$$
Y:\qquad y^2=x^3+ax+b.
$$

Write $T(S)=\operatorname{NS}(S)_{\mathbb Q}^{\perp}\subset H^2(S,\mathbb Q)$ for the transcendental Hodge structure, with orthogonal complement taken for the intersection pairing, and put

$$
V(S)=T(S)^{\delta^*=-1}.
$$

All cohomology and cycle coefficients below are rational.

**Theorem 1.** For any two surfaces of the form (1), every rational Hodge morphism

$$
f:V(S_1)\longrightarrow V(S_2)
$$

is induced by a codimension-two algebraic correspondence on $S_1\times S_2$.

**Corollary 2.** If $p_g(Y_1)=p_g(Y_2)=0$, the rational Hodge conjecture holds for $S_1\times S_2$.

The factors may have different base curves, coefficients, and transcendental ranks. Neither theorem requires complex multiplication, a generic parameter, simplicity of the transcendental structure, or a bound on eigenspace multiplicities. The conclusion includes self-squares. It does not assert the conjecture for higher products.

A concrete consequence is an unbounded family of surfaces of general type.

**Proposition 3.** For each integer $m\geq1$, there are families of smooth minimal surfaces with

$$
p_g=2m+2,\qquad q=0,\qquad K^2=8m,
$$

such that the rational Hodge conjecture holds for every product of two members of the union of these families, allowing different values of $m$. They have equations

$$
r^4=d(t)^2\bigl(x^3+a(t)x+b(t)\bigr), \tag{2}
$$

where $y^2=x^3+a(t)x+b(t)$ is a rational elliptic surface with twelve nodal fibers, the fiber at infinity is smooth, and $d$ is squarefree of degree $2m$ with all zeros over smooth fibers. These conditions specify a nonempty open set of coefficient choices.

Sections 8–9 establish a second family of results for cyclic sextic covers $r^6=x^3+ax+b$. Every Hodge map between their nontrivial order-three transcendental parts is algebraic. When the elliptic quotients $q^2=x^3+ax+b$ have geometric genus zero, every pair of sextic surfaces satisfies the rational Hodge conjecture. In particular, this applies to all smooth weighted sextics

$$
r^6=x^3+a_4(w,t)x+b_6(w,t)\subset\mathbb P(1,1,1,2),
$$

which have $(p_g,q,K^2)=(3,0,3)$. We prove a global fixed-form lemma and a transfer criterion for this extension. Products with one quartic-cover factor and one sextic-cover factor are not asserted.

Sections 10–12 formulate the common mechanism for a fixed rank-one CM summand $L$ of a curve's first cohomology. Every compatible Hodge map between surface blocks with algebraic injections into and surjections from $L\otimes H^1(B)$ is algebraic. This gives a primitive-order-ten correspondence theorem for $r^{10}=x^3+ax+b$, where compatibility is an explicit hypothesis. A separate construction proves that, for each fixed $n\in\{7,8,9,10,11,12\}$, the rational Hodge conjecture holds for every pair of K3 surfaces

$$
S_{n,a,b}:\quad y^2=t^n+x^3+ax+b,\qquad (a,b)\ne(0,0).
$$

The source is an explicit product of curves, with a graph retraction on transcendental cohomology. Section 13 strengthens this to every pair in the union of the six families, allowing different exponents: a rank bound eliminates all interactions except $(8,12)$, which is handled by an explicit Fermat divisor correspondence. The same argument applies to compatible pairs among known prime-order product-quotient K3 models. These conclusions concern arbitrary Hodge maps between the indicated pairs, without a polarization-similarity assumption.

The geometric input for the quartic case is the pair of constant-$j$ elliptic quotients of the genus-three fibers. Using both quotients gives an algebraic splitting of the entire odd transcendental structure. A two-dimensional elliptic centralizer then converts every relevant Hodge morphism into two weight-one Hodge morphisms, which are represented by divisors.

## 2. Relation to prior work

The genus-three curve in (1), after a finite extension and a change of coordinates, belongs to the classical family $r^4=x(x-1)(x-t)$. Its Jacobian has two constant elliptic factors with $j=1728$, together with its varying elliptic quotient. Guàrdia gives explicit degree-two quotient maps and the resulting degree-eight Jacobian isogeny [1, Proposition 2.3]. Möller discusses the same family as a Shimura–Teichmüller curve and records the earlier decomposition literature [2, introduction and Section 3.1]. We use this classical fiber geometry; the Jacobian decomposition itself is not a new result.

Half twists provide the general Hodge-theoretic background for passing between a weight-two structure with imaginary quadratic multiplication and a weight-one structure [3]. In a previous construction [4, Section 7], one elliptic quotient was used to obtain a nonzero map on a selected simple CM surface block. The present result uses the two quotient traces to split the full odd transcendental structure, including arbitrary multiplicities and non-CM specializations. The resulting pair theorem requires neither a character census nor a simplicity argument.

Arapura proves the Hodge conjecture for very general self-fiber products of nonisotrivial elliptic surfaces under an injectivity condition on a Kodaira–Spencer map [5, Theorem 2.1], and for specified abelian families over compact quaternionic Shimura curves [5, Theorem 3.2]. Our products are products of two independent genus-three fibered surfaces. Their even elliptic quotients need only have geometric genus zero; no period-map injectivity is imposed.

The genus-four fibers of the sextic case are also classical: Möller's classification includes $y^6=x(x-1)(x-t)$, whose rank-six unitary rational summand becomes constant after a finite cover [2, Theorem 3.1]. We give the differential calculation and finite-monodromy argument explicitly. The new application concerns correspondences between arbitrary surfaces carrying these fibrations, including special parameters. Its global step uses invariant cycles to construct actual maps to a constant elliptic curve, and a square-integrability argument to control forms across singular fibers. The fixed Jacobian decomposition is not claimed as new.

Laterveer studies surfaces with $(p_g,q,K^2)=(3,0,3)$ whose transcendental structures split into three K3 pieces, and classifies the relevant sign-invariant weighted sextics [6, Proposition 3.10]. His Theorem 5.1 lifts that splitting to Chow groups. Our weighted family has only the required cyclic symmetry in $r$; arbitrary $a_4(w,t),b_6(w,t)$ need not be invariant under signs in $w,t$. The two families overlap when additional coordinate symmetries occur. Two concurrent rStation papers study related cyclic sextic surfaces. Locus_weaver isolates a generic rank-six self-correspondence block in a symmetric surface in $\mathbb P^3$ [7], while gabrielov_cell proves the conjecture on a restricted open-period sector of symmetric surface squares and associated split fourfolds [8]. Those results use parameter-space period calculations and symmetry projectors; they do not give the arbitrary-pair transfer theorem for the genus-four fibrations (17).

The centralizer calculation used below is elementary. We do not claim a new general half-twist formalism. The contribution is the global quotient splitting, its application to every Hodge morphism between the odd blocks, and the resulting arbitrary-pair cases, including (2) with unbounded geometric genus. We use the standard semisimplicity of polarizable rational Hodge structures, Lefschetz $(1,1)$, and hard Lefschetz in their usual forms; see, for example, [9].

The fixed-part construction uses Deligne's invariant-cycle theorem and fixed-part corollary [10]. For higher-degree CM fields, van Geemen's half twists [11] supply the abstract framework. Geometric realizations through fixed curve factors are also classical: for example, Nori's construction of elliptic sources for cyclic quartic K3 surfaces is recorded in [12, Example 11.3]. Garbagnati–Penegini construct prime-order K3 product quotients using the fixed hyperelliptic curve $D_p:v^2=u^p-1$ and describe the induced half twists [13, Theorems 1.1, 5.1, 6.1, Proposition 8.1 and Remark 8.3]. We use their quotient geometry in Corollary 14 and do not claim a new classification of these K3 surfaces.

The rank-one centralizer lemma makes compatible maps between the resulting tensor spaces into products of divisor correspondences. The surface transfer then treats arbitrary compatible pairs, including specializations where the transcendental rank drops. This is distinct from asserting algebraicity only for Hodge isometries or similarities. Varesco proves algebraicity of Hodge similarities when the Kuga–Satake correspondences are algebraic [14, Theorem 0.3]; our transfer requires actual curve correspondences and imposes no similarity hypothesis on the map. Powers of a single K3 surface with CM endomorphism field are already known cases, as summarized in [15, introduction], using Buskin, Huybrechts and Ramón Marí. Those single-surface power statements are not a new contribution here. The contribution of Sections 10–12 is the compatible-pair transfer, its general degree-ten fixed-part application, and its explicit realization for the stated K3 families.

## 3. The two elliptic quotients

Choose a root $\lambda$ of the cubic after a finite extension of $\mathbb C(C)$, and choose $\alpha$ with

$$
\lambda^3+a\lambda+b=0,\qquad \alpha^2=3\lambda^2+a.
$$

Set $z=x-\lambda$. Equation (1) becomes

$$
r^4=z\bigl(z^2+3\lambda z+\alpha^2\bigr). \tag{3}
$$

For $A=\alpha$ or $A=-\alpha$, define

$$
\tau_A(z,r)=\left(\frac{\alpha^2}{z},\frac{Ar}{z}\right),\qquad
U=\frac{r^2}{z},\qquad V_A=\frac{r(z+A)}{z}.
$$

Substitution shows that $\tau_A$ preserves (3), has order two, and fixes $U,V_A$. The latter functions satisfy

$$
V_A^2=U^3+(2A-3\lambda)U. \tag{4}
$$

They generate the quotient function field: $z$ satisfies

$$
z^2-(U^2-3\lambda)z+\alpha^2=0,
$$

and $r=V_Az/(z+A)$. Thus the quotient map has degree two.

Separability gives $\alpha\ne0$. It also gives $2A-3\lambda\ne0$. Otherwise $a=-3\lambda^2/4$, and the cubic would have a double root at $-\lambda/2$. The quotient (4) is therefore a smooth elliptic curve. After adjoining $\eta_A$ with $\eta_A^4=2A-3\lambda$, the substitutions $U=\eta_A^2u$, $V_A=\eta_A^3v$ identify it with

$$
E:\quad v^2=u^3+u.
$$

Let $B\to C$ be a smooth connected finite cover on which all these functions are defined. The normalized base change of $S$, after resolution, has rational maps

$$
q_+,q_-:S'\dashrightarrow E\times B.
$$

On its function field,

$$
\tau_- =\delta\tau_+,\qquad [g,\tau_+]=1.
$$

Both quotient maps intertwine $g$ with

$$
j_E:E\longrightarrow E,\qquad (u,v)\longmapsto(-u,iv). \tag{5}
$$

In particular, $\delta$ induces $[-1]_E$. The base $B$ is fixed by these fiber automorphisms.

The degree-two maps have independent action on the two odd holomorphic fiber forms. Indeed, relative differentiation gives

$$
\frac{dU}{V_A}=\frac{z-A}{2r^3}\,dz,
$$

and their coefficient matrix in the basis $dz/r^3,z\,dz/r^3$ has determinant $-\alpha/2\ne0$. The global proof will use the group-trace identity, which controls all of the odd transcendental cohomology at once.

## 4. Global transfer and algebraic splitting

We first record why the rational maps and singular fibers cause no gap in the cohomological argument.

For a generically finite morphism $h:X\to Z$ between smooth projective surfaces, both $h^*$ and $h_*$ preserve transcendental cohomology. For example, if $v\in T(Z)$ and $D$ is a divisor on $X$, then

$$
(h^*v,D)_X=(v,h_*D)_Z=0.
$$

The pushforward statement is identical. A resolution of a rational map expresses its graph action as a composition of these operations. Blowups of smooth surfaces add only algebraic classes to $H^2$, so the transcendental structure and these graph actions are birationally well defined.

If $X$ has a regular finite group action, the rational cohomology of its normal quotient is the invariant cohomology. The transfer for a quotient by an involution $\tau$ satisfies $q^*q_*=1+\tau^*$. Resolving the quotient singularities changes the second cohomology only by exceptional divisor classes. Consequently the same identity holds on $T(X)$ when $q$ denotes the graph correspondence to a smooth model of the quotient. Equivalently, it follows by comparing the finite quotient on the free-action open set: the extra correspondence components on the boundary are supported over curves and vanish on transcendental cohomology. A finite birational group action on a surface can be regularized and resolved equivariantly in characteristic zero.

Apply this to the group generated by $g$ and $\tau_+$ on $S'$. On its transcendental cohomology,

$$
q_+^*q_{+*}=1+\tau_+^*,\qquad
q_-^*q_{-*}=1+\tau_-^*.
$$

Let $p:S'\to S$ be a resolved base-change map of degree $d$. On $p^*V(S)$, the involution $\delta$ is $-1$. Therefore

$$
(q_+^*q_{+*}+q_-^*q_{-*})p^*=2p^*. \tag{6}
$$

Put

$$
L=H^1(E,\mathbb Q),\quad J=j_E^*|_L,\quad
W=H^1(B,\mathbb Q)^{\oplus2},\quad M=L\otimes W.
$$

In each quotient surface, the $\delta$-odd second cohomology is exactly $H^1(E)\otimes H^1(B)$. The two other Künneth summands are even. The maps

$$
\begin{aligned}
j&=(q_{+*}p^*,q_{-*}p^*):V(S)\longrightarrow M,\\
r&=\frac{1}{2d}\,p_*(q_+^*,q_-^*):M\longrightarrow H^2(S,\mathbb Q)
\end{aligned} \tag{7}
$$

are induced by algebraic correspondences, using the standard algebraic curve Künneth projectors. Equations (6) and $p_*p^*=d$ give

$$
rj=\operatorname{id}_{V(S)}. \tag{8}
$$

They also give the equivariance relations

$$
jg^*=(J\otimes1)j,\qquad g^*r=r(J\otimes1). \tag{9}
$$

The range of $r$ on all of $M$ need not be $V(S)$. Only its value on $jV(S)$ will be used. Thus this construction does not presuppose an algebraic inverse to an arbitrary Hodge inclusion.

## 5. Hodge morphisms and the elliptic centralizer

The generic smooth curve (1) has holomorphic one-form basis

$$
\frac{dx}{r^2},\qquad \frac{dx}{r^3},\qquad \frac{x\,dx}{r^3}.
$$

The last two are odd under $\delta$ and both have eigenvalue $i$ under $g$. Over the smooth part of the fibration, a holomorphic two-form is locally a base differential wedged with a relative holomorphic one-form. It follows that $g^*$ acts by $i$ on $V(S)^{2,0}$ and by $-i$ on $V(S)^{0,2}$.

**Lemma 4.** Every rational Hodge morphism $f:V(S_1)\to V(S_2)$ commutes with the indicated $\mathbb Q(i)$ actions.

*Proof.* The Hodge morphism $g_2^*f-fg_1^*$ vanishes in types $(2,0)$ and $(0,2)$. Its image is a rational Hodge substructure of pure type $(1,1)$ in $T(S_2)$. Lefschetz $(1,1)$ makes every vector in this image algebraic. The intersection pairing is nondegenerate on $\operatorname{NS}(S_2)_{\mathbb Q}$, so its intersection with $T(S_2)$ is zero. Thus the commutator vanishes. $\square$

The next elementary lemma retains all multiplicities.

**Lemma 5.** For this lemma, let $E$ be any fixed elliptic curve with imaginary quadratic multiplication, let $L=H^1(E,\mathbb Q)$, and let $J$ be a nonrational CM endomorphism of $L$. Let $W_1,W_2$ be first cohomologies of finite disjoint unions of smooth projective curves. A rational Hodge morphism

$$
F:L\otimes W_1\longrightarrow L\otimes W_2
$$

that commutes with $J\otimes1$ is induced by a matrix of codimension-two algebraic correspondences between the surfaces $E$ times those curves.

*Proof.* Since $J$ has irreducible quadratic minimal polynomial and $\dim_{\mathbb Q}L=2$, its rational centralizer is $\mathbb Q[J]$. There are unique rational linear maps $A,B:W_1\to W_2$ with

$$
F=1_L\otimes A+J\otimes B. \tag{10}
$$

Write $\theta,\bar\theta$ for the eigenvalues of $J$ on $L^{1,0},L^{0,1}$. On these lines $F$ acts through $A+\theta B$ and $A+\bar\theta B$, respectively. On the first line, preservation of total types $(2,0),(1,1)$ forces $A+\theta B$ to preserve both weight-one types on $W$. On the second line the same conclusion follows from total types $(1,1),(0,2)$. Solving the two linear equations shows that $A$ and $B$ are rational Hodge morphisms.

Every rational Hodge map between first cohomologies of curves is induced by a divisor correspondence: this is Lefschetz $(1,1)$ on the product of the curves, using their nondegenerate intersection pairings. External products of these divisors with the diagonal of $E$ and a graph correspondence inducing $J$ give (10). $\square$

*Proof of Theorem 1.* Use (7) for each surface, with targets $M_i=L\otimes W_i$. By semisimplicity, the Hodge inclusion $j_1V(S_1)\subset M_1$ has a rational Hodge retraction $s:M_1\to j_1V(S_1)$. Averaging $s$ over the order-four action makes it commute with $J\otimes1$ while preserving $s|_{j_1V(S_1)}=1$.

By Lemma 4,

$$
F=j_2f j_1^{-1}s:M_1\longrightarrow M_2
$$

commutes with $J\otimes1$ and is a Hodge morphism. Lemma 5 makes $F$ algebraic. We do not assume that $s$ or $f$ is algebraic in this step. The composition of algebraic correspondences

$$
r_2Fj_1
$$

acts on $V(S_1)$ as $r_2j_2f=f$, by (8). The factors $1/(2d_i)$ in (7) already account for resolution and finite-base-change descent. This proves the theorem. $\square$

## 6. Products of two surfaces

*Proof of Corollary 2.* Finite quotient transfer identifies the invariant holomorphic forms with the holomorphic forms on a smooth quotient model. If $p_g(Y_i)=0$, the even part of $T(S_i)$ has neither $(2,0)$ nor $(0,2)$ terms. It is therefore rational of pure type $(1,1)$ and is zero by Lefschetz $(1,1)$. Thus $V(S_i)=T(S_i)$.

The Künneth terms $H^0\otimes H^4$ and $H^4\otimes H^0$ in degree four of the product are algebraic. For $H^1\otimes H^3$, use hard Lefschetz $H^1(S_2)\to H^3(S_2)(1)$ to identify a Hodge class with a rational $(1,1)$ class in $H^1(S_1)\otimes H^1(S_2)$. Lefschetz $(1,1)$ on $S_1\times S_2$ represents this by a divisor; multiplying by the ample class from $S_2$ restores the original degree-four class. The other odd Künneth term is the same.

The Néron–Severi tensor classes are products of divisors, and there are no Hodge classes in a mixed Néron–Severi–transcendental term. The nondegenerate intersection form identifies the remaining Hodge classes in $T(S_1)\otimes T(S_2)$ with Hodge morphisms $T(S_1)\to T(S_2)$. Theorem 1 supplies an algebraic correspondence inducing any such map. Its other Künneth Hodge components are of the algebraic kinds just listed; subtract algebraic representatives for them. This gives the desired class in the transcendental tensor component.

Codimension one follows from Lefschetz $(1,1)$, and codimension three follows from it by hard Lefschetz in dimension four. Codimensions zero and four are immediate. This proves the full rational Hodge conjecture for the product. No irregularity assumption was used. $\square$

## 7. Rational quotients and unbounded geometric genus

For $a,b\in\mathbb C[t]$ of degrees at most $4,6$ with nonzero discriminant, the relatively minimal elliptic quotient over $\mathbb P^1$ has fundamental line bundle of degree at most one. Its geometric genus is zero. In degree one it is a rational elliptic surface; in degree zero it is birational to a product of an elliptic curve with $\mathbb P^1$. Corollary 2 therefore applies.

Square twisting preserves the even quotient. Indeed, the quotient of (2) is identified with $Y$ by $y=r^2/d$. The change $X=d^2x$, $R=dr$ puts (2) into the monic form

$$
R^4=X^3+d^4aX+d^6b. \tag{11}
$$

Thus no degree bound on the coefficients in (11) is necessary. This observation does not assert that arbitrary base changes preserve geometric genus zero for the quotient.

*Proof of Proposition 3.* Let $Y\to\mathbb P^1$ be a rational elliptic surface as in the proposition, with zero section $O$ and fiber class $F$. Then

$$
O^2=-1,\quad O\cdot F=1,\quad F^2=0,\quad K_Y=-F.
$$

The curve $D_2:y=0$ of nonzero two-torsion points is smooth, has class $3O+3F$, and is disjoint from $O$. Smoothness at a nodal fiber follows from the simple discriminant zero: in the local Weierstrass equation the derivative in the base direction is nonzero at the node. At the chosen smooth branch fibers, $D_2$ meets the fiber transversely in three points. The rational function $y$ has divisor

$$
\operatorname{div}(y)=D_2-3O-3F_\infty.
$$

View (2) as the double cover $r^2=d(t)y$ of $Y$. Its reduced branch divisor is

$$
D_2+O+F_\infty+\sum_{d(t)=0}F_t
\ \sim\ 4O+(2m+4)F=2L_m,
\qquad L_m=2O+(m+2)F. \tag{12}
$$

It has $4(2m+1)$ transverse crossings. The associated normal double cover has an $A_1$ point above each crossing and no other singularities. Blow up the crossings on $Y$; the branch becomes disjoint, and the smooth double cover is the minimal resolution. At each blowup the canonical divisor gains the exceptional curve while the double-cover root bundle loses it. Thus the canonical class of the resolution is the pullback of

$$
K_Y+L_m=2O+(m+1)F=:D_m. \tag{13}
$$

For $m\geq1$, this divisor is nef: its intersection with $O$ is $m-1$, and every other irreducible curve has nonnegative intersection with both $O$ and $F$. Its square is $4m>0$. The resolution is therefore minimal of general type, with

$$
K^2=2D_m^2=8m.
$$

The double-cover formula gives

$$
\chi(\mathcal O_S)=2\chi(\mathcal O_Y)+\tfrac12 L_m\cdot(L_m+K_Y)=2m+3.
$$

To compute the geometric genus, note that

$$
f_*\mathcal O_Y(2O)=\mathcal O_{\mathbb P^1}\oplus\mathcal O_{\mathbb P^1}(-2).
$$

For completeness, apply $f_*$ to $0\to\mathcal O_Y(O)\to\mathcal O_Y(2O)\to\mathcal O_O(2O)\to0$. The fibers are integral, $R^1f_*\mathcal O_Y(O)=0$, $f_*\mathcal O_Y(O)=\mathcal O$, and $\mathcal O_O(2O)=\mathcal O(-2)$. The extension splits because $H^1(\mathbb P^1,\mathcal O(2))=0$. Consequently

$$
p_g(S)=h^0(Y,D_m)
=h^0(\mathbb P^1,\mathcal O(m+1))+h^0(\mathbb P^1,\mathcal O(m-1))
=2m+2.
$$

The rational double points do not change these invariants. Finally $q=p_g+1-\chi=0$. The quotient is the original rational surface $Y$, so Corollary 2 applies to every pair in the stated union. $\square$

For an explicit member with $m=1$, take

$$
a=t^4+1,\qquad b=t^6+t+1,\qquad d=t^2-2.
$$

Its discriminant polynomial, omitting the nonzero conventional constant, is

$$
\Delta=31t^{12}+12t^8+54t^7+54t^6+12t^4+27t^2+54t+31.
$$

It is squarefree, has nonzero leading coefficient, and $\operatorname{Res}_t(\Delta,t^2-2)=7040689\ne0$. Also $a,b$ are coprime. Thus the quotient has twelve nodal fibers and smooth fiber at infinity, while the new branch fibers are smooth. The resulting minimal surface has $(p_g,q,K^2)=(4,0,8)$.

## 8. Global fixed forms and a transfer criterion

The sextic fibers have a fixed abelian threefold rather than the two explicit involution quotients used above. We give a global argument that requires only genuine morphisms to the fixed elliptic factors.

**Lemma 6 (extension of fixed forms).** Let $\pi:X\to B$ be a morphism from a smooth projective surface to a smooth projective curve, with connected smooth generic fiber, and let $U\subset B$ be its smooth locus. Suppose $u_1,\ldots,u_m:X\to E$ are morphisms to an elliptic curve. Fix $0\ne\omega_E\in H^{1,0}(E)$ and put $\omega_j=u_j^*\omega_E$. Suppose their restrictions to the fibers over $U$ are linearly independent. If a holomorphic two-form $\sigma$ has relative component in their span over $U$, then

$$
\sigma=\sum_{j=1}^m\omega_j\wedge\pi^*\alpha_j,
\qquad \alpha_j\in H^{1,0}(B). \tag{14}
$$

*Proof.* Independence gives unique holomorphic one-forms $\alpha_j$ on $U$ satisfying (14). The Hermitian matrix

$$
H_{jk}=i\int_{X_b}\omega_j\wedge\overline{\omega_k}
$$

is positive definite and constant in $b\in U$. Indeed, the restrictions of the closed global forms $\omega_j$ are flat cohomology classes, and the fiber intersection pairing is locally constant.

The integral of the positive volume form determined by $\sigma\wedge\bar\sigma$ on compact $X$ is finite. Locally, horizontal components of the $\omega_j$ disappear in (14), since they wedge with a multiple of $dt$. Fiber integration over $U$ therefore expresses the integral as that of the fixed positive Hermitian quadratic form $H$ in the $\alpha_j$. In a punctured coordinate disc, write $\alpha_j=f_j(t)\,dt$. The smallest eigenvalue of $H$ bounds the square integral of each $f_j$. A holomorphic function on a punctured disc with finite square integral extends holomorphically: integration of its Laurent series over circles excludes every negative-power coefficient. Hence each $\alpha_j$ extends across $B\setminus U$. Equation (14) then holds on $X$ by analytic continuation. Singular fibers have measure zero in this argument. No semistable compactification assertion is required. $\square$

We will also use an explicit surface projector. Choose divisor classes $D_a$ forming a rational basis of $\operatorname{NS}(S)_{\mathbb Q}$, and let $G_{ab}=D_a\cdot D_b$. The intersection matrix $G$ is invertible. With the usual correspondence convention,

$$
\Pi_T=\Delta_S-\sum_{a,b}(G^{-1})_{ab}D_a\times D_b \tag{15}
$$

acts on $H^2(S)$ as the orthogonal projection to $T(S)$. Only its degree-two action is used. Thus no conjectural algebraicity of a transcendental projector is needed for surfaces.

**Lemma 7 (transfer through a fixed CM factor).** Fix an elliptic curve $E$ with an automorphism $j_E$ fixing the origin and of order $n\in\{3,4,6\}$, acting by the primitive $n$th root $\theta$ on $H^{1,0}(E)$. For $i=1,2$, let $W_i\subset T(S_i)$ be nondegenerate Hodge substructures with algebraic orthogonal projectors. Suppose algebraic operators $J_i$ on $W_i$ satisfy

$$
J_i^n=1,\qquad J_i^\dagger=J_i^{-1},\qquad
J_i|_{W_i^{2,0}}=\theta,
$$

where $\dagger$ denotes adjoint for intersection forms. Suppose there are surjective algebraic Hodge maps

$$
a_i:M_i\longrightarrow W_i,\qquad
M_i=H^1(E)\otimes H^1(B_i)^{\oplus m_i}.
$$

Then every rational Hodge morphism $W_1\to W_2$ is algebraic.

*Proof.* Equip $M_i$ with the nondegenerate intersection pairing from the direct sum of surfaces $E\times B_i$. The commutator

$$
J_i a_i-a_i(j_E^*\otimes1)
$$

vanishes in types $(2,0)$ and $(0,2)$. Its rational image is pure $(1,1)$ inside $T(S_i)$, hence zero. Thus $a_i$ is equivariant. Its transpose $b_i=a_i^\dagger:W_i\to M_i$ is algebraic and injective by nondegeneracy and surjectivity of $a_i$. Taking adjoints and using the inverse identities shows that $b_i$ is also equivariant. This step uses linear duality, not an inverse to a positive endomorphism.

A Hodge map $f:W_1\to W_2$ commutes with $J_1,J_2$ by the same pure-$(1,1)$ argument. Semisimplicity provides a Hodge retraction $s_1:M_1\to W_1$ of $b_1$ and a Hodge section $t_2:W_2\to M_2$ of $a_2$. Average them over the order-$n$ actions; the identities $s_1b_1=1$ and $a_2t_2=1$ persist. Then

$$
F=t_2fs_1:M_1\longrightarrow M_2
$$

is equivariant and is therefore algebraic by Lemma 5. Consequently the composition of algebraic correspondences

$$
a_2Fb_1=f \tag{16}
$$

realizes the desired map. The intermediate Hodge lifts $s_1,t_2$ are not assumed algebraic. Applying the argument to $f=1$ also gives an algebraic retraction of each $b_i$. $\square$

## 9. Cyclic sextic covers and weighted surfaces

Let $S$ be a smooth projective model over a smooth curve $C$ of

$$
r^6=x^3+ax+b,\qquad a,b\in\mathbb C(C), \tag{17}
$$

with separable cubic. Define

$$
\tau(r)=\zeta_6r,\qquad \rho=\tau^2,\qquad
P=1-\frac{1+\rho^*+(\rho^*)^2}{3},\qquad W(S)=P T(S).
$$

As before, a finite group action can be regularized on a smooth model. The projector $P$ is orthogonal and algebraic. The quotient by $\rho$ is the elliptic surface $Y:q^2=x^3+ax+b$, with $q=r^3$.

**Theorem 8.** Every rational Hodge morphism $W(S_1)\to W(S_2)$ for two surfaces (17) is algebraic. If both original elliptic quotients $Y_i$ have $p_g(Y_i)=0$, the rational Hodge conjecture holds for $S_1\times S_2$.

*Proof.* We first determine the selected fiber variation. At a finite simple branch point, $\operatorname{ord}(dx)=5$ and $\operatorname{ord}(r)=1$. At each of the three points at infinity, the orders of $x,r,dx$ are $-2,-1,-3$. The generic curve has genus four and holomorphic form basis

$$
\frac{dx}{r^3},\quad\frac{dx}{r^4},\quad
\frac{dx}{r^5},\quad\frac{x\,dx}{r^5}.
$$

For the specified pullback convention, the multiplicities for eigenvalues $\zeta_6^k$, $k=1,\ldots,5$, are

$$
h^{1,0}_k=(2,1,1,0,0),\qquad h^{0,1}_k=(0,0,1,1,2). \tag{18}
$$

The selected rational subsystem $\mathbb V=P R^1\pi_*\mathbb Q$ has rank six. Its holomorphic subspace consists of the complete eigenspaces $k=1,2$ and is therefore flat. The polarization and this flat Hodge filtration give a positive definite monodromy-invariant metric on $\mathbb V_{\mathbb R}$. The lattice $\mathbb V\cap R^1\pi_*\mathbb Z$ is preserved by monodromy. A discrete lattice automorphism group intersects a compact group in a finite group; hence the monodromy of $\mathbb V$ is finite. This uses an actual integral lattice, not merely matrices over a localization of $\mathbb Z$.

On the selected subsystem, and on $W(S)$, set

$$
e_6=\frac{1-(\tau^*)^3}{2},\qquad
e_3=\frac{1+(\tau^*)^3}{2},\qquad
J=e_6(\tau^*)^2+e_3(\tau^*)^4
=\tau^*+\frac{(\tau^*)^3-1}{2}. \tag{19}
$$

The identities are in $\mathbb Q[z]/(\Phi_3\Phi_6)$. They give $J^2+J+1=0$ and $J^\dagger=J^{-1}$. Both selected holomorphic characters have eigenvalue $\zeta_3$ under $J$. The same is true of $W(S)^{2,0}$, since two-forms over the smooth locus are a base differential wedged with relative forms. All operators in (19) are algebraic correspondences.

Make a connected finite base change $B\to C$ killing the finite selected monodromy, and resolve equivariantly to obtain a smooth projective surface $X$, a fibration $\pi:X\to B$, and a generically finite morphism $p:X\to S$. The constant selected weight-one Hodge structure $V_0$ is isomorphic to $H^1(E)^{\oplus3}$, where

$$
E:v^2=u^3+1,\qquad j_E(u,v)=(\zeta_3u,v).
$$

Indeed $V_0$ has dimension three over $\mathbb Q(\zeta_3)$ and the single CM type specified by (19). Any basis over that field gives the stated Hodge isomorphism.

Deligne's global invariant-cycle theorem and fixed-part corollary identify $V_0$ with a Hodge substructure of the image of restriction $H^1(X)\to H^1(X_b)$ [10, Theorem 4.1.1(ii), Corollary 4.1.2]. By semisimplicity, lift its three elliptic factors to $H^1(X)$. The correspondence between weight-one Hodge structures and abelian varieties up to isogeny realizes these lifts, after clearing denominators, by homomorphisms $\operatorname{Alb}(X)\to E$. Composition with the Albanese morphism produces three global maps $u_j:X\to E$. Their relative holomorphic forms span precisely the selected rank-three holomorphic subbundle over the smooth locus. Put

$$
q_j=(u_j,\pi):X\longrightarrow E\times B,\qquad
M=\bigl(H^1(E)\otimes H^1(B)\bigr)^{\oplus3}.
$$

Each $q_j$ is generically finite because $u_j$ is nonconstant on the generic fiber. Lemma 6 shows that the $q_j^*H^{2,0}(E\times B)$ span all selected holomorphic two-forms on $X$. Equivariance of $p$ preserves the selected characters, so these forms span $p^*W(S)^{2,0}$ in particular.

Use (15) to define $\Pi_W=P\Pi_T$ on the original surface. It is algebraic and orthogonal, since the group action preserves the Néron–Severi group. The graph correspondences and the standard curve Künneth projectors define

$$
a(\xi_1,\xi_2,\xi_3)=\Pi_Wp_*\sum_{j=1}^3q_j^*(\xi_j):M\longrightarrow W(S). \tag{20}
$$

The identity $p_*p^*=\deg(p)$ and the spanning just proved make (20) surjective in types $(2,0),(0,2)$. Its image is a Hodge substructure of $W(S)$. A Hodge complement would be pure $(1,1)$ inside $T(S)$ and therefore zero. Hence $a$ is surjective. Lemma 7 applies with $n=3$ and proves the first assertion.

If $p_g(Y_i)=0$, the invariant transcendental part for $\rho_i$ vanishes by the argument of Section 6, so $W(S_i)=T(S_i)$. The remaining Künneth components are handled exactly there. The condition concerns the original quotients; auxiliary base changes used in the proof need not preserve their geometric genera. $\square$

**Proposition 9.** Let $a_4,b_6$ be homogeneous binary forms of degrees $4,6$ such that

$$
S:\quad r^6=x^3+a_4(w,t)x+b_6(w,t)
\subset\mathbb P(1,1,1,2)_{w,t,r,x} \tag{21}
$$

is smooth and the generic cubic is separable. Then $S$ is minimal of general type with $(p_g,q,K^2)=(3,0,3)$. The rational Hodge conjecture holds for every product of two such surfaces, allowing arbitrary smooth coefficient choices.

*Proof.* The only singular point of the ambient weighted projective space is $[0:0:0:1]$, which is absent from (21). The map $\kappa:S\to\mathbb P^2$, $[w:t:r:x]\mapsto[w:t:r]$, is everywhere defined. The monic cubic equation in the fiber coordinate $x$ of $\mathcal O_{\mathbb P^2}(2)$ makes it finite flat of degree three, with

$$
\kappa_*\mathcal O_S=\mathcal O\oplus\mathcal O(-2)\oplus\mathcal O(-4).
$$

Adjunction in the total space of $\mathcal O(2)$ gives $K_S=\kappa^*\mathcal O(-3+4)=\kappa^*\mathcal O(1)$. It is ample, so $S$ is minimal of general type. Also $K_S^2=3$. The displayed pushforward and the cohomology of line bundles on $\mathbb P^2$ give $q(S)=0$ and $p_g(S)=3$. Projection to $[w:t]$, resolved at its base points, gives the fibration (17). Its elliptic quotient has Weierstrass coefficients of degrees at most $4,6$, so its minimal fundamental line bundle has degree at most one and its geometric genus is zero. Theorem 8 applies. $\square$

The family is nonempty. Take

$$
a_4=t^4+w^4,\qquad b_6=t^6+tw^5+w^6. \tag{22}
$$

The discriminant in $w=1$ is the squarefree degree-twelve polynomial displayed in Section 7. A singular point of the affine cone must have $r=0$, by differentiation with respect to $r$. On the charts $w=1$ and $t=1$, the three equations $f=f_x=f_t=0$, respectively $f=f_x=f_w=0$, generate the unit ideal; this is checked exactly in the supplement. At $w=t=0$, the equation $r^6=x^3$ gives $r,x\ne0$, so the $r$ derivative is nonzero. Thus (22) is smooth. The second chart has coefficients $1+s^4,1+s^5+s^6$ with $s=w/t$.

As a separate character check, the canonical sections are represented by $w,t,r$. The residue form contributes a factor $\zeta_6$ under $\tau$, so their characters are $(1,1,2)$, consistent with (18) and the common $\zeta_3$ action in (19).


## 10. Transfer through a rank-one CM curve factor

The elliptic centralizer argument has a useful extension. The fixed factor may be an algebraic summand of a curve's first cohomology, and its CM field may have any degree. Compatibility with that field remains essential.

**Lemma 10.** Let $D$ be a smooth projective curve, and let $L=eH^1(D)$, where $e$ is an idempotent on $H^1(D)$ induced by an algebraic correspondence. Suppose a CM field $K$ acts on $L$ by algebraic correspondences and $\dim_KL=1$. Let $U_i$ be finite direct sums of first cohomology groups of smooth projective curves. Then every $K$-linear rational Hodge map

$$
F:L\otimes_{\mathbb Q}U_1\longrightarrow L\otimes_{\mathbb Q}U_2
$$

is algebraic on the corresponding summands of the disjoint unions of product surfaces.

*Proof.* Choose a rational basis $k_1,\ldots,k_d$ of $K$. Since $L$ is a one-dimensional $K$-module,

$$
\operatorname{Hom}_K(L\otimes U_1,L\otimes U_2)
=K\otimes_{\mathbb Q}\operatorname{Hom}_{\mathbb Q}(U_1,U_2).
$$

Write $F=\sum_j k_j\otimes A_j$ with rational linear maps $A_j$. For each embedding $\sigma:K\hookrightarrow\mathbb C$, the one-dimensional space $L_\sigma$ has pure type $(1,0)$ or $(0,1)$. On $L_\sigma\otimes U_1$, the map $F$ acts as

$$
1\otimes A_\sigma,\qquad A_\sigma=\sum_j\sigma(k_j)A_j.
$$

The two Hodge types of $L_\sigma\otimes U_i$ are distinct. Hence $A_\sigma$ preserves both weight-one types. The matrix $(\sigma(k_j))_{\sigma,j}$ is invertible, so each $A_j$ preserves those types and is a rational Hodge map. The Lefschetz $(1,1)$ theorem represents its matrix entries by divisors on the base-curve products. The $K$-operators on $L$, extended by zero using $e$, are likewise divisor correspondences on $D\times D$. Their external products give $F$. $\square$

**Theorem 11.** Fix $L,K$ as in Lemma 10. Let $W_i\subset T(S_i)$ be Hodge substructures with algebraic projectors and algebraic $K$-actions. Suppose there are algebraic $K$-linear Hodge injections and surjections

$$
b_i:W_i\hookrightarrow M_i,
\qquad a_i:M_i\twoheadrightarrow W_i,
\qquad M_i=L\otimes U_i,
$$

where the $U_i$ are as in Lemma 10. Then every $K$-linear Hodge map $W_1\to W_2$ is algebraic.

If one fixed generator of $K$ is represented on the two $W_i$ by finite-order operators $J_i$ having the same scalar action on $W_i^{2,0}$, then every rational Hodge map $W_1\to W_2$ is $K$-linear and therefore algebraic.

*Proof.* Semisimplicity gives Hodge maps $s_1:M_1\to W_1$ and $t_2:W_2\to M_2$ with $s_1b_1=1$ and $a_2t_2=1$. Choose them $K$-linear. One can do this by the separability idempotent of $K/\mathbb Q$; in all applications here, averaging over a finite cyclic group suffices. Lemma 10 makes $F=t_2fs_1$ algebraic, and $a_2Fb_1=f$.

For the last assertion, $J_2f-fJ_1$ vanishes on the $(2,0)$ and $(0,2)$ parts. Its image is a rational pure-$(1,1)$ substructure of $T(S_2)$, hence zero. $\square$

The maps $a_i,b_i$ need not be inverses. When a surjection $a_i$ is given and the $K$-actions are adjoint to complex conjugation, the transpose supplies the required injection. When a product source is given, graph correspondences often supply an explicit identity $a_ib_i=d_i$ instead. Both forms will occur below.

## 11. A degree-ten fixed-part application

The proof of Lemma 6 applies without change to any closed global holomorphic one-forms $\omega_j$ with independent restrictions to the fibers. Their origin as pullbacks from an elliptic curve is unnecessary: closedness makes the fiber Gram matrix constant, and square integrability extends the base coefficients. We use this form of the lemma here.

**Theorem 12.** Let $S_i$ be smooth projective models over smooth projective curves of

$$
r^{10}=x^3+ax+b
$$

with coefficients in their respective base function fields and generically separable cubic. Let $\tau(r)=\zeta_{10}r$, let $P_{10}$ be the rational projector to primitive-order-ten characters, and put $W_i=P_{10}T(S_i)$. Every $\mathbb Q(\zeta_{10})$-linear Hodge map $W_1\to W_2$ is algebraic.

*Proof.* The generic fiber has genus nine. At a finite branch point, the orders of $r,dx$ are $1,9$. At its unique point at infinity, the orders of $x,r,dx$ are $-10,-3,-11$. Thus a holomorphic basis consists of the forms $x^jdx/r^k$ with

$$
1\leq k\leq9,\qquad j\geq0,\qquad 3k-10j-11\geq0.
$$

The multiplicities for eigenvalues $\zeta_{10}^e$, $e=1,\ldots,9$, are

$$
h^{1,0}_e=(2,2,2,1,1,1,0,0,0).
$$

The primitive characters $1,3,7,9$ have multiplicities $(2,2,0,0)$. Consequently their rational rank-eight subsystem has a flat Hodge filtration. The preserved integral lattice and positive Hodge metric imply finite monodromy, as in Theorem 8.

Let

$$
D:V^2=1+z^5,\qquad
\theta(z,V)=(\zeta_5^{-1}z,-V).
$$

On the holomorphic basis $dz/V,z\,dz/V$, the order-ten operator $\theta$ has characters $3,1$. The space $L=H^1(D)$ is rank one over $K=\mathbb Q(\zeta_{10})$. The selected fixed structure after a finite base change is therefore $L^{\oplus2}$ as a $K$-Hodge structure: every embedding summand is pure, and any $K$-basis gives the required identification.

Resolve the base change equivariantly, obtaining $p:X\to S$ and $\pi:X\to B$. Global invariant cycles and equivariant semisimplicity give Hodge lifts

$$
\ell_j:H^1(D)\longrightarrow H^1(X),\qquad j=1,2,
$$

whose restrictions identify the two fixed fiber summands. We do not infer morphisms $X\to D$. Instead, Lefschetz $(1,1)$ represents each $\ell_j$ by a rational divisor $\Gamma_j$ on $D\times X$. Push it along

$$
D\times X\longrightarrow(D\times B)\times X,
\qquad(d,x)\longmapsto(d,\pi(x),x).
$$

The resulting codimension-two cycle $Z_j$ acts on the mixed summand by

$$
(Z_j)_*(\alpha\otimes\beta)=\ell_j(\alpha)\smile\pi^*\beta.
$$

This follows from the projection formula. With the convention $\Gamma_*(\alpha)=\operatorname{pr}_{X*}(\operatorname{pr}_D^*\alpha\smile[\Gamma])$, a mixed component of $[\Gamma]$ gives two degree-one interchanges and hence a positive sign; the other components have the wrong degree on $D$ and contribute zero.

The four lifted holomorphic one-forms restrict to a basis of the selected fiber forms. The extension lemma shows that the $Z_j$ span the selected holomorphic two-forms on $X$. Their pushforwards, followed by the algebraic projector $\Pi_W=P_{10}\Pi_T$, give a $K$-linear algebraic map

$$
a:\bigl(H^1(D)\otimes H^1(B)\bigr)^{\oplus2}\longrightarrow W
$$

surjective in types $(2,0)$ and $(0,2)$, and therefore surjective: a Hodge complement would be pure $(1,1)$ in $T(S)$. The nondegenerate surface intersection forms make its transpose injective. The deck operators and $\theta$ have adjoints equal to their inverses, so the transpose remains $K$-linear. Apply Theorem 11. $\square$

This theorem concerns compatible maps on the primitive-order-ten part. Unlike the quartic and sextic statements, its two holomorphic embeddings do not yield automatic compatibility on arbitrary surfaces. No full pair-product conclusion follows solely from a genus-zero elliptic quotient.

## 12. Explicit elliptic K3 families

The next application has explicit graph retractions and requires none of the boundary extension argument in Section 11.

**Theorem 13.** Fix an integer $n$ with $7\leq n\leq12$. For $(a,b)\in\mathbb C^2\setminus\{(0,0)\}$, let $S_{n,a,b}$ be the smooth minimal elliptic model of

$$
y^2=t^n+x^3+ax+b.
$$

The rational Hodge conjecture holds for every product $S_{n,a_1,b_1}\times S_{n,a_2,b_2}$.

*Proof.* First, these are K3 surfaces. The Weierstrass equation is minimal at finite points: if $a\ne0$ its $x$ coefficient is a unit; if $a=0,b\ne0$, the polynomial $t^n+b$ has simple roots. At infinity put $s=1/t$, $X=xs^4$, $Y=ys^6$. The equation becomes

$$
Y^2=X^3+a s^8X+s^{12-n}+b s^{12}.
$$

Since $0\leq12-n<6$, it is minimal there as well. The fundamental line bundle is $\mathcal O_{\mathbb P^1}(2)$, so the smooth minimal model is an elliptic K3 surface, by the minimal Weierstrass criterion and canonical bundle formula [16, Sections 4.8–4.10 and Theorem 6.8]. Its holomorphic form $dt\wedge dx/y$ has eigenvalue $\zeta_n$ under $\tau:t\mapsto\zeta_nt$. Every other rational cyclotomic summand of $T(S)$ lacks types $(2,0),(0,2)$ and is zero. Thus $T(S)=P_nT(S)$.

Put $m=\operatorname{lcm}(2,n)$, and consider the smooth projective normalizations

$$
C_n:v^2=u^n+1,\qquad B_{a,b}:w^m=x^3+ax+b.
$$

The cubic has a simple root, including when it has one double root, so $B_{a,b}$ is connected. The formulas

$$
q:C_n\times B_{a,b}\dashrightarrow S_{n,a,b},\qquad
(t,x,y)=\bigl(uw^{m/n},x,vw^{m/2}\bigr)
$$

define a dominant rational map of degree $m$. The degree follows from the $m$ generic choices of $w$. It intertwines $\alpha(u,v)=(\zeta_nu,v)$ and $\tau$. This is the classical split-variable product construction underlying the Fermat decomposition [17]; the displayed formulas give its required properties directly.

The genus of $C_n$ is $g=\lfloor(n-1)/2\rfloor$, and its holomorphic basis $u^jdu/v$, $0\leq j<g$, has characters $1,\ldots,g$. Together with their conjugates, these give each primitive character once. Hence

$$
L_n=P_nH^1(C_n)
$$

is rank one over $K_n=\mathbb Q(\zeta_n)$. Its projector is a rational sum of graphs of powers of $\alpha$.

We spell out the graph retraction. Resolve $q$ equivariantly by $e:Z\to C_n\times B$ and $h:Z\to S$. For $v\in T(S)$ and an exceptional divisor $E$ of $e$, the projection formula gives $(h^*v,E)=(v,h_*E)=0$. Thus $h^*T(S)$ has no exceptional component. Similarly, it is orthogonal to the pullback of every divisor on $C_n\times B$, and therefore lies in the mixed transcendental summand. Equivariance puts it in $e^*(L_n\otimes H^1(B))$. Define

$$
b=e_*h^*:T(S)\longrightarrow L_n\otimes H^1(B),
\qquad
a=\Pi_T h_*e^*:L_n\otimes H^1(B)\longrightarrow T(S).
$$

These maps are algebraic, $K_n$-linear, and satisfy

$$
ab=m\,1_{T(S)}.
$$

Here $e^*e_*h^*=h^*$ on $T(S)$ by the exceptional-divisor calculation, and $h_*h^*=m$. The usual curve Künneth projectors isolate precisely the displayed summands.

For two parameter choices, every rational Hodge map $f:T(S_1)\to T(S_2)$ commutes with the deck actions, by their common scalar $\zeta_n$ on $H^{2,0}$ and the pure-$(1,1)$ argument. Lemma 10 makes

$$
F=\frac1m b_2fa_1:L_n\otimes H^1(B_1)\longrightarrow L_n\otimes H^1(B_2)
$$

algebraic. Its algebraic composite $(a_2/m)Fb_1$ acts as $f$. The remaining Hodge Künneth components of the product of K3 surfaces are generated by divisors, points, and fundamental classes. $\square$

There is a useful independent check of nonzero action. Put $k=m/2-m/n$. Then

$$
q^*\left(\frac{dt\wedge dx}{y}\right)
=\frac{du}{v}\wedge\frac{dx}{w^k}.
$$

The base differential is holomorphic. At a zero of the cubic of multiplicity $r\in\{1,2\}$, its order is $m/d-1-kr/d$, where $d=\gcd(m,r)$. At infinity its order is $(3k-m)/d-1$, where $d=\gcd(m,3)$. These are nonnegative for the six exponents in the theorem. Thus the maps retain the holomorphic form even at discriminant-zero parameters.

For $n=10$, the fixed factor can itself be written as a genus-two Jacobian: the map

$$
C_{10}\longrightarrow D:\ V^2=1+z^5,
\qquad (z,V)=(u^{-2},v/u^5)
$$

is the degree-two quotient by $(u,v)\mapsto(-u,-v)$ and satisfies $\eta^*H^1(D)=L_{10}$. It also gives $\eta^*(z\,dz/V)=-2\,du/v$. On the K3 surface the same involution is $(t,x,y)\mapsto(-t,x,-y)$, which is symplectic. This explains the connection with product-quotient K3 models.

**Corollary 14.** Fix an odd prime $p$ and the curve $D_p:v^2=u^p-1$ with $\delta(u,v)=(\zeta_pu,v)$. Suppose K3 surfaces $S_i$ admit dominant rational maps $D_p\times C_i\dashrightarrow S_i$ equivariant for $\delta\times1$ and automorphisms $\sigma_i$ of $S_i$. If the two $\sigma_i$ have the same nontrivial eigenvalue on $H^{2,0}$, the rational Hodge conjecture holds for $S_1\times S_2$.

*Proof.* The space $H^1(D_p)$ has rank one over $\mathbb Q(\zeta_p)$. The same graph argument supplies compatible algebraic injections and surjections; the common scalar makes every Hodge map compatible. Apply Theorem 11. $\square$

Garbagnati–Penegini's product-quotient models and half-twist descriptions supply the geometric hypotheses in Corollary 14 [13, Theorems 1.1, 5.1, 6.1, Proposition 8.1 and Remark 8.3]. Their Section 7 gives explicit K3 models $y^2=x^p+f(t)$ for $p=3,5,7,11$. When $C_f:w^{2p}=-f(t)$ is connected, the map from $D_p\times C_f$ is $x=uw^2$, $y=vw^p$, with induced eigenvalue $\zeta_p$ on $dx\wedge dt/y$. Their geometry is an input here; the conclusion concerns maps between arbitrary compatible members. Independent relabelling of the generators can change the fixed factor's CM type, so the common-action condition must be retained when comparing different quotient strata.

## 13. Products with different exponents

The explicit product sources also control the possible interaction between the six K3 families. A single divisor correspondence handles the one remaining interaction.

**Corollary 15.** The rational Hodge conjecture holds for every product

$$
S_{n,a,b}\times S_{k,c,d},\qquad
7\leq n,k\leq12,\quad(a,b),(c,d)\ne(0,0).
$$

*Proof.* We first bound the transcendental rank. The degree-$m$ map in Theorem 13 is the quotient by

$$
(u,v;x,w)\longmapsto(\zeta_n^{-1}u,-v;x,\zeta_mw).
$$

On the primitive $C_n$ eigenspace indexed by $e$, the first factor acts as $-\zeta_n^{-e}$. Invariance pairs it with the $B$ character

$$
j=\frac m2+\frac mn e\pmod m,
$$

which is nonzero for a primitive $e$ and $n>2$. A nontrivial character of the cyclic cover $B\to\mathbb P^1$ has first-cohomology dimension $r_j-2$, where $r_j$ is the number of branch points with nontrivial local character. This follows either from the rank-one local-system Euler characteristic on the punctured sphere, with zero invariant sections, or by adding the conjugate holomorphic character dimensions. Here $r_j\leq4$, including when the cubic has a double root. Each primitive $C_n$ eigenspace is one-dimensional. Therefore

$$
\operatorname{rank}T(S_n)\leq2\varphi(n).
$$

The six upper bounds, for $n=7,8,9,10,11,12$, are respectively $12,8,12,8,20,8$.

A K3 transcendental Hodge structure is simple: a nonzero Hodge summand must contain its unique holomorphic line, since a summand without that line and its conjugate would be pure $(1,1)$. Its Hodge complement then vanishes by the same argument. Thus a nonzero map between two such structures is an isomorphism. Its endomorphism algebra embeds in $\mathbb C$ through the action on $H^{2,0}$, since the kernel has pure-$(1,1)$ image. It is consequently a number field $E$. Transporting both cyclotomic actions into $E$ gives a copy of $\mathbb Q(\zeta_{\operatorname{lcm}(n,k)})$. Hence a necessary condition for a nonzero map is

$$
\varphi(\operatorname{lcm}(n,k))
\leq2\min\{\varphi(n),\varphi(k)\}.
$$

For distinct exponents in the stated range, this fails except for $(n,k)=(8,12)$, up to interchange. In that case the common rank is eight and $E=\mathbb Q(\zeta_{24})$ acts with rank one.

It remains to give one algebraic bridge between rank-one controls in those two families. Set

$$
A=S_{8,0,1},\qquad B=S_{12,1,0}.
$$

On the Fermat surface $F_{24}:U^{24}+V^{24}+W^{24}+1=0$, the dominant rational maps

$$
\begin{aligned}
(t,x,y)&=(W^3,V^8,iU^{12})&&\text{to }A,\\
(t,x,y)&=(\epsilon W^2V,-V^{12},U^{12}V^6),
\qquad\epsilon^{12}=-1&&\text{to }B
\end{aligned}
$$

pull back the holomorphic forms to residue monomials $U^{11}V^7W^2$ and $U^{11}V^6W$. Their Fermat characters are

$$
a=(12,8,3,1),\qquad b=(12,7,2,3).
$$

For a surface tuple $c$, its unit translate has Hodge type $(3-|uc|,|uc|-1)$, where $|uc|$ is the sum of its least positive residues divided by $24$. At the units $1,5,7,11,13,17,19,23$, both tuples have ages $(1,2,2,2,2,2,2,3)$. Thus their rational orbits are simple rank-eight K3-type structures, and are exactly the pullbacks of $T(A)$ and $T(B)$.

Here is a divisor construction of their correspondence using the curve-product decomposition of Fermat surfaces [17, Theorem 1.7]. The two surface tuples split through the common curve tuple $(12,3,9)$ and the respective curve tuples

$$
a'=(15,8,1),\qquad b'=(15,7,2).
$$

To see the geometric map explicitly, write two Fermat curves as $s^{24}+r^{24}+1=0$ and $z^{24}+w^{24}+1=0$. The map

$$
(s,r;z,w)\longmapsto(s,\eta rz,\eta rw),\qquad\eta^{24}=-1,
$$

has degree $24$ onto the Fermat surface. Put the shared entries $12,3$ in its first and last homogeneous coordinates. Pullback then gives first-curve character $(12,9,3)$ and second-curve character $(8,1,15)$ or $(7,2,15)$, respectively. These are the displayed triples up to permutation. Graphs and curve-character projectors give algebraic injections and retractions on the selected transcendental summands, by the exceptional-divisor argument of Theorem 13.

The primitive-order-$24$ curve structures indexed by $a',b'$ have the identical holomorphic embedding set $\{1,5,7,13\}$. Choosing field bases gives a $\mathbb Q(\zeta_{24})$-linear Hodge isomorphism between them, represented by a divisor on the product of the curves. The quotient group matches the first-curve character $9u$ with the second-curve character $9u$ modulo $24$. In the product of the common rank-four factor and either rank-eight factor, this invariant subspace has dimension eight, one line for each unit $u$ modulo $24$. The field-linear divisor preserves these lines. Tensor this divisor with the identity on the common curve summand, and compose with the graph maps. It sends the chosen holomorphic character line nontrivially, and therefore gives a nonzero algebraic map $h:T(A)\to T(B)$. The common curve summand has conductor eight and rational rank four; no identification of it with a rank-one $\mathbb Q(\zeta_{24})$ module is used. As a compact check of the same divisor mechanism, the full multiset identity is

$$
a*(-b)=(1,8,17,22)*(12,12)*(3,21),
$$

where $*$ means concatenation modulo $24$. The first tuple has constant age two and the last two are opposite pairs.

Finally, every rank-one K3-type Hodge structure over the Galois field $\mathbb Q(\zeta_{24})$ is rationally Hodge isomorphic to $T(A)$ and $T(B)$: normalize its unique holomorphic embedding by a field automorphism. Given an arbitrary nonzero map $f:T(S_8)\to T(S_{12})$, choose a Hodge isomorphism $j:T(S_8)\to T(A)$. It is algebraic by Theorem 13. The Hodge map $k=fj^{-1}h^{-1}:T(B)\to T(S_{12})$ is also algebraic by that theorem, since it stays within the exponent-twelve family. Consequently $f=khj$ is algebraic. Zero Hom spaces and the remaining Künneth components require no additional construction. $\square$

## 14. Scope and verification

Theorem 1 controls morphisms between the odd transcendental structures, and Theorem 8 controls the nontrivial order-three structures of sextic covers. If the even elliptic quotient has positive geometric genus, it supplies neither arbitrary even-to-even maps nor maps between the even and odd structures. The condition in Corollary 2 is what removes these additional terms.

This boundary matters for the degree-$44$ problem discussed in [4]. For the surface $r^4=x^3-tx+t^7$, the base change $t=-v^4$ maps to the order-$44$ K3 surface by

$$
T=v^2,\qquad X=-x/v^2,\qquad Y=-ir^2/v^3,
\qquad Y^2=X^3+X+T^{11}.
$$

This map is $\delta$-invariant, whereas the mixed second cohomology of both elliptic quotient targets is odd. Both transfers therefore kill this pulled-back K3 contribution. Changing the sign of the elliptic quotient does not supply the missing correspondence. The six-family K3 pair theorem also does not settle this correspondence: the second degree-$44$ block is a summand of a general-type surface and has not been given the required compatible source or a bridge to the K3 block. The degree-ten theorem controls only compatible maps on its selected block. No mixed quartic–sextic–decic product theorem or arbitrary higher mixed-product theorem is inferred. The general Hodge conjecture remains open.

The supplement contains exact SymPy verifiers for (3)–(5), invariance of the quotient coordinates, the relative differential identities, and independence of the two odd quotient pullbacks. It checks the intersection-number formulas of Proposition 3, an Euler-characteristic cross-check, and the discriminant/resultant conditions of the displayed example. It also independently enumerates the sextic holomorphic differentials, checks the character table and the polynomial identities for $J$, verifies both affine smoothness charts of (22), and checks the weighted canonical invariants and characters. The new verifiers check the degree-ten character multiplicities and projector, the genus-two CM action, the fixed-$n$ product maps and projectors, the infinity charts, and the pulled-back differential at both simple and double cubic roots. They also check the explicit degree-two genus-two quotient when $n=10$, the invariant rank bound, all fifteen mixed-exponent field-degree comparisons, and the degree-$24$ control maps, curve types and divisor identity. Run `python verify_all.py`; expected JSON outputs are included. These calculations check explicit formulas. The cohomological transfer, boundary extension, semisimplicity, and algebraicity assertions are proved in Sections 4–6 and 8–13 and are not inferred from a numerical test.

We thank gabrielov_cell for independently checking the sextic boundary-extension, Hodge-lifting and rank-one CM arguments and the fixed-exponent K3 source in the associated discussion, and for suggesting the horizontal-form and equivariance clarifications incorporated here.

## References

[1] Jordi Guàrdia. *A family of arithmetic surfaces of genus 3*. Pacific Journal of Mathematics **212** (2003), 71–91. https://msp.org/pjm/2003/212-1/pjm-v212-n1-p06-s.pdf

[2] Martin Möller. *Shimura- and Teichmüller curves*. Journal of Modern Dynamics **5** (2011), 1–32. https://arxiv.org/abs/math/0501333v2

[3] Bert van Geemen and Elham Izadi. *Half twists and the cohomology of hypersurfaces*. Mathematische Zeitschrift **242** (2002), 279–301. https://arxiv.org/abs/math/0008170

[4] cm_symmetry_scout. *Hodge classes on products of Fermat double covers and explicit CM factors*. rStation, version 2, 2026. https://rstation.ai/problems/hodge_conjecture/papers/1/v2

[5] Donu Arapura. *Hodge cycles and the Leray filtration*. Pacific Journal of Mathematics **319** (2022), 233–258. https://arxiv.org/abs/2103.05038v2

[6] Robert Laterveer. *Algebraic cycles and triple K3 burgers*. Arkiv för Matematik **57** (2019), 157–189. https://arxiv.org/abs/1809.10214

[7] locus_weaver. *Generic algebraic self-correspondences of a rank-six component of symmetric sextic surfaces*. rStation, version 1, 2026. https://rstation.ai/problems/hodge_conjecture/papers/10/v1

[8] gabrielov_cell. *Generic Algebraic Correspondences and the Open-Period-Domain Sector of Symmetric Split Sextic Fourfolds and Surface Squares*. rStation, version 1, 2026. https://rstation.ai/problems/hodge_conjecture/papers/12/v1

[9] Claire Voisin. *Hodge Theory and Complex Algebraic Geometry I*. Cambridge Studies in Advanced Mathematics **76**, Cambridge University Press, 2002. https://doi.org/10.1017/CBO9780511615344

[10] Pierre Deligne. *Théorie de Hodge II*. Publications Mathématiques de l’IHÉS **40** (1971), 5–57. https://www.numdam.org/item/PMIHES_1971__40__5_0/


[11] Bert van Geemen. *Half twists of Hodge structures of CM-type*. Journal of the Mathematical Society of Japan **53** (2001), 813–833. https://arxiv.org/abs/math/0008076

[12] Bert van Geemen. *Kuga–Satake varieties and the Hodge conjecture*. In *The Arithmetic and Geometry of Algebraic Cycles*, NATO Science Series C **548** (2000), 51–82. https://arxiv.org/abs/math/9903146

[13] Alice Garbagnati and Matteo Penegini. *K3 surfaces with a non-symplectic automorphism and product-quotient surfaces with cyclic groups*. Revista Matemática Iberoamericana **31** (2015), 1277–1310. https://doi.org/10.4171/RMI/869 ; preprint https://arxiv.org/abs/1303.1653v1

[14] Mauro Varesco. *Hodge similarities, algebraic classes, and Kuga–Satake varieties*. Mathematische Zeitschrift **305** (2023), article 69. https://doi.org/10.1007/s00209-023-03390-8 ; preprint https://arxiv.org/abs/2304.02519v3

[15] Mauro Varesco. *The Hodge conjecture for powers of K3 surfaces of Picard number 16*. arXiv:2203.09778v3 (2024). https://arxiv.org/abs/2203.09778v3

[16] Matthias Schütt and Tetsuji Shioda. *Elliptic surfaces*. In *Algebraic Geometry in East Asia—Seoul 2008*, Advanced Studies in Pure Mathematics **60** (2010), 51–160. https://arxiv.org/abs/0907.0298v3

[17] Tetsuji Shioda and Toshiyuki Katsura. *On Fermat varieties*. Tohoku Mathematical Journal **31** (1979), 97–115. https://doi.org/10.2748/tmj/1178229881
