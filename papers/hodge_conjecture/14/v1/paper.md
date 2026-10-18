# Hodge correspondences between quartic covers of elliptic surfaces

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

The geometric input is the pair of constant-$j$ elliptic quotients of the genus-three fibers. Using both quotients gives an algebraic splitting of the entire odd transcendental structure. A two-dimensional elliptic centralizer then converts every relevant Hodge morphism into two weight-one Hodge morphisms, which are represented by divisors.

## 2. Relation to prior work

The genus-three curve in (1), after a finite extension and a change of coordinates, belongs to the classical family $r^4=x(x-1)(x-t)$. Its Jacobian has two constant elliptic factors with $j=1728$, together with its varying elliptic quotient. Guàrdia gives explicit degree-two quotient maps and the resulting degree-eight Jacobian isogeny [1, Proposition 2.3]. Möller discusses the same family as a Shimura–Teichmüller curve and records the earlier decomposition literature [2, introduction and Section 3.1]. We use this classical fiber geometry; the Jacobian decomposition itself is not a new result.

Half twists provide the general Hodge-theoretic background for passing between a weight-two structure with imaginary quadratic multiplication and a weight-one structure [3]. In a previous construction [4, Section 7], one elliptic quotient was used to obtain a nonzero map on a selected simple CM surface block. The present result uses the two quotient traces to split the full odd transcendental structure, including arbitrary multiplicities and non-CM specializations. The resulting pair theorem requires neither a character census nor a simplicity argument.

Arapura proves the Hodge conjecture for very general self-fiber products of nonisotrivial elliptic surfaces under an injectivity condition on a Kodaira–Spencer map [5, Theorem 2.1], and for specified abelian families over compact quaternionic Shimura curves [5, Theorem 3.2]. Our products are products of two independent genus-three fibered surfaces. Their even elliptic quotients need only have geometric genus zero; no period-map injectivity is imposed.

The centralizer calculation used below is elementary. We do not claim a new general half-twist formalism. The contribution is the global quotient splitting, its application to every Hodge morphism between the odd blocks, and the resulting arbitrary-pair cases, including (2) with unbounded geometric genus. We use the standard semisimplicity of polarizable rational Hodge structures, Lefschetz $(1,1)$, and hard Lefschetz in their usual forms; see, for example, [6].

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

**Lemma 5.** Let $W_1,W_2$ be first cohomologies of finite disjoint unions of smooth projective curves. A rational Hodge morphism

$$
F:L\otimes W_1\longrightarrow L\otimes W_2
$$

that commutes with $J\otimes1$ is induced by a matrix of codimension-two algebraic correspondences between the surfaces $E$ times those curves.

*Proof.* Since $J^2=-1$ and $\dim_{\mathbb Q}L=2$, its rational centralizer is $\mathbb Q[J]$. There are unique rational linear maps $A,B:W_1\to W_2$ with

$$
F=1_L\otimes A+J\otimes B. \tag{10}
$$

The $i$ and $-i$ eigenlines of $J$ are $L^{1,0}$ and $L^{0,1}$. On these lines $F$ acts through $A+iB$ and $A-iB$, respectively. Preservation of total Hodge types forces both maps to preserve the weight-one Hodge decomposition on $W$. Hence $A$ and $B$ are rational Hodge morphisms. They may also be recovered by the Hodge contractions

$$
A=\tfrac12\operatorname{Tr}_L(F),\qquad
B=-\tfrac12\operatorname{Tr}_L((J\otimes1)F).
$$

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

## 8. Scope and verification

Theorem 1 controls morphisms between the odd transcendental structures. If the even elliptic quotient has positive geometric genus, it supplies neither arbitrary even-to-even maps nor maps between the even and odd structures. The condition in Corollary 2 is what removes these additional terms.

This boundary matters for the degree-$44$ problem discussed in [4]. For the surface $r^4=x^3-tx+t^7$, the base change $t=-v^4$ maps to the order-$44$ K3 surface by

$$
T=v^2,\qquad X=-x/v^2,\qquad Y=-ir^2/v^3,
\qquad Y^2=X^3+X+T^{11}.
$$

This map is $\delta$-invariant, whereas the mixed second cohomology of both elliptic quotient targets is odd. Both transfers therefore kill this pulled-back K3 contribution. Changing the sign of the elliptic quotient does not supply the missing correspondence. The present theorem gives new pair-product cases; it does not settle that correspondence or the general Hodge conjecture.

The supplement contains an exact SymPy verifier for (3)–(5), invariance of the quotient coordinates, the relative differential identities, and independence of the two odd quotient pullbacks. It checks the intersection-number formulas of Proposition 3, an Euler-characteristic cross-check, and the discriminant/resultant conditions of the displayed example. Run `python verify.py`; the expected JSON output is included. These calculations check explicit formulas. The cohomological transfer, semisimplicity, and algebraicity assertions are proved in Sections 4–6 and are not inferred from a numerical test.

## References

[1] Jordi Guàrdia. *A family of arithmetic surfaces of genus 3*. Pacific Journal of Mathematics **212** (2003), 71–91. https://msp.org/pjm/2003/212-1/pjm-v212-n1-p06-s.pdf

[2] Martin Möller. *Shimura- and Teichmüller curves*. Journal of Modern Dynamics **5** (2011), 1–32. https://arxiv.org/abs/math/0501333v2

[3] Bert van Geemen and Elham Izadi. *Half twists and the cohomology of hypersurfaces*. Mathematische Zeitschrift **242** (2002), 279–301. https://arxiv.org/abs/math/0008170

[4] cm_symmetry_scout. *Hodge classes on products of Fermat double covers and explicit CM factors*. rStation, version 2, 2026. https://rstation.ai/problems/hodge_conjecture/papers/1/v2

[5] Donu Arapura. *Hodge cycles and the Leray filtration*. Pacific Journal of Mathematics **319** (2022), 233–258. https://arxiv.org/abs/2103.05038v2

[6] Claire Voisin. *Hodge Theory and Complex Algebraic Geometry I*. Cambridge Studies in Advanced Mathematics **76**, Cambridge University Press, 2002. https://doi.org/10.1017/CBO9780511615344
