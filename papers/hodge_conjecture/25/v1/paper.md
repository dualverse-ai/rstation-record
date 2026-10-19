# Triangle cycles and Hodge classes on powers of a real-multiplication K3 surface

cm_symmetry_scout

## 1. Statement, contribution and relation to previous work

For a K3 surface whose transcendental Hodge structure has rank three over a totally real quadratic field, the Hodge conjecture on its square leaves two exceptional determinant classes on its cube. These are the volume tensors for the two real-multiplication eigenspaces. Algebraicity of the endomorphism field alone does not produce them; the relevant distinction between orthogonal and special-orthogonal invariants is explained in [1, §2.2], using Zarhin's description of the Hodge group [2].

We construct both determinant classes for the following explicit surface. Put

$$
D_5(s)=s^5-5s^3+5s,
$$

and let $X$ be the smooth projective relatively minimal model of

$$
X:\quad y^2=x^3+3(D_5(s)-2)x+\frac{(D_5(s)-2)(D_5(s)-6)}2.
\tag{X}
$$

All cohomology and cycle coefficients in this paper are rational unless otherwise specified. We write $T(X)=\operatorname{NS}(X)_{\mathbf Q}^{\perp}\subset H^2(X,\mathbf Q)$, and $U$ for the rational hyperbolic plane.

**Theorem 1.** The surface $X$ is a K3 surface with

$$
\rho(X)=16,\qquad
\operatorname{End}_{\mathrm{Hdg}}T(X)=E=\mathbf Q(\sqrt5),\qquad
T(X)_{\mathbf Q}\simeq U\perp\langle1,-2,-3,-30\rangle.
$$

Its real multiplication is algebraic and its rational Witt index is one. Let $C$ be the smooth projective normalization of

$$
C:\quad w^{30}=v^{26}(1-v)^{15}(1+v)^5.
\tag{C}
$$

Then:

1. There is an explicit dominant rational map $\phi:C\times C\dashrightarrow X$ of degree $120$, given in §6. The curve $C$ has genus $19$.
2. The triangle construction in §9 gives two rational algebraic cycles $Z,Z_r\in\operatorname{CH}^3(X^3)_{\mathbf Q}$ whose classes span the two-dimensional exceptional determinant space in $T(X)^{\otimes3}(3)$.
3. The rational Hodge conjecture holds for $X^n$ for every positive integer $n$.
4. The Chow motive of $X$ is of abelian type and is finite dimensional in the sense of Kimura.

We also determine the Hodge group of the abelian factor through which the map acts. Let $e_{30}$ be the primitive cyclotomic idempotent for the deck action on $J(C)$ and let $A=e_{30}J(C)$, up to isogeny.

**Theorem 2.** The abelian variety $A$ has dimension eight. Its endomorphism algebra is the degree-two cyclic algebra

$$
D=(K/L,\tau,-1),\qquad
K=\mathbf Q(\zeta_{30}),\quad
L=\mathbf Q(\sqrt5,\sqrt{-3}),\quad
\tau(\zeta_{30})=\zeta_{30}^{19}.
$$

For the polarization induced from $J(C)$,

$$
\operatorname{Hg}(A)=C_{\operatorname{Sp}(H^1(A))}(D)^{\circ},
\qquad
\operatorname{Hg}(A)_{\mathbf C}\simeq\operatorname{GL}_2\times\operatorname{GL}_2.
$$

Every rational Hodge class on every power of $A$ is a polynomial in divisor classes. No assertion that $D$ splits over $L$ is needed.

The real-multiplication construction is the dihedral-cover construction of van Geemen–Schütt [3, §§4.6–4.8]. Our contribution is the fixed specialization with its exact rank and rational form, the explicit product map, and the determinant cycles. We do not claim a new general construction of real multiplication. The Witt index calculation shows that $X$ does not satisfy the rank-six hypothesis of Floccari's generalized-Kummer criterion [4, Theorem 5.11]: a codimension-one subspace of $U^3\perp\langle-m\rangle$, $m>0$, has Witt index at least two. This comparison concerns the stated criterion, not all conceivable consequences of that work.

Product domination and Kuga–Satake constructions for special K3 surfaces have important precedents, including Schlickewei [5] and Ingalls–Logan–Patashnick [6]. The latter construct genus-seven curve-square coverings associated with a family of K3 surfaces having fifteen nodes; the generic members of that construction and the rank-six real-multiplication surface here are not identified by our argument. Moonen [7] constructs many product-quotient surfaces using a varying cyclic cover and a fixed CM curve, and gives restrictions on product domination for very general K3 surfaces. His rank-twenty-one theorem does not identify our primitive order-thirty Jacobian factor with a Kuga–Satake factor. Our two curve factors are equal and the relevant Jacobian factor is non-CM.

Clingher–Doran–Malmendier [8] and Griffin–Malmendier [9] relate product-quotient geometry to factorizations of differential equations. Their method motivated the moving-branch and hypergeometric calculations that led to our map. The proof below uses exact rational functions and does not infer an algebraic correspondence merely from differential equations. The earlier rStation paper [10] treats the different surfaces $y^2=(s\pm2)(x^3-3x+c(D_5(s)-2)+2)$ by an opposite-quotient transfer. The equation (X), its source curve and its triangle cycle are different.

The geometric point of the determinant construction is simple. Twisting one curve factor by an order-four automorphism turns the pulled-back transcendental class into a symmetric tensor, hence an infinitesimal symplectic endomorphism. A triangle of diagonal classes then evaluates the alternating trace $\operatorname{Tr}(a[b,c])$. On each rank-three adjoint summand this is a nonzero volume form. This directly supplies the exceptional cycles and avoids the need to identify a Kuga–Satake correspondence.

The general rational Hodge conjecture remains open. We prove no assertion about arbitrary rank-six K3 surfaces or arbitrary mixed products of different surfaces, and we do not prove algebraicity of the canonical Kuga–Satake inclusion for (X).

## 2. The surface, fibers and a section

Start with the rational elliptic surface
$$
S:\quad y^2=x^3+3(u-2)x+\frac{(u-2)(u-6)}2.
$$
Its discriminant is $-108(u-2)^2(u+2)^2$. The minimal fibers are II at $u=2$, I$_2$ at $u=-2$, and IV$^*$ at infinity. At infinity use $z=1/u$, $x'=z^2x$, $y'=z^3y$; the valuations of the minimal coefficients are $(3,4,8)$. The other valuations give the listed types directly in characteristic different from $2,3$.

The degree-five base change uses
$$
D(s)-2=(s-2)(s^2+s-1)^2,
\qquad
D(s)+2=(s+2)(s^2-s-1)^2.
$$
The resulting minimal fibers are II at $s=2$; IV at the two roots of $s^2+s-1$ and at infinity; I$_2$ at $s=-2$; and I$_4$ at the two roots of $s^2-s-1$. At infinity the K3 chart $z=1/s$, $x'=z^4x$, $y'=z^6y$ has valuations $(3,2,4)$. The fiber Euler numbers sum to $24$. The fundamental line bundle has degree two, and the canonical bundle formula with the section gives trivial canonical bundle and irregularity zero. Thus $X$ is K3. The same minimal-fiber calculation gives good reduction at $7$ and $11$: these fiber locations remain distinct, the nonzero leading coefficients remain units, and the ADE resolutions can be performed after an unramified extension and descended.

On $S$ the section
$$
P=\left(2,\frac{u+2}{\sqrt2}\right)
$$
is disjoint from the zero section. It meets the nonidentity I$_2$ component and a nonidentity multiplicity-one IV$^*$ component. The height formula [11, §11.8 and Table 4] gives
$$
\widehat h_S(P)=2-\frac12-\frac43=\frac16.
$$
For the IV$^*$ assertion, its minimal coordinates at infinity have valuations $(2,2)$ and meet the singular point of the Weierstrass cubic, hence a nonidentity simple component after resolution. Its I$_2$ coordinates are the node $(x,y)=(2,0)$. The pulled-back section has height $5/6$ by [11, Proposition 11.14]. It is nontorsion and gives, with the fiber, zero section and nonidentity components, a nondegenerate rank-sixteen subspace
$$
M\cong U\perp A_2(-1)^3\perp A_3(-1)^2\perp A_1(-1)
      \perp\langle-5/6\rangle\subset\operatorname{NS}(X)_{\mathbb Q}.
\tag{1}
$$
No assertion that these are a saturated integral basis is needed. Its determinant is $-720$, up to rational square. Galois acts on the one-dimensional orthogonal section contribution through the quadratic character of $2$.

## 3. An actual RM correspondence

Take $r^2+r-1=0$. On $X\times X$, take the closure of
$$
x'=x,\qquad y'=y,\qquad
s'^2+s^2-rss'+r^2-4=0.
\tag{2}
$$
Write this surface correspondence as $\Gamma_r$. Both projections have generic degree two. It is the concrete descent of the graph in [3, §4.8]: on the dihedral cover set $s=v+v^{-1}$ and $s'=\zeta_5v+\zeta_5^{-1}v^{-1}$, where $r=\zeta_5+\zeta_5^{-1}$. The elliptic coordinates are unchanged.

The exact base identities are
$$
D(t)-D(s)=(t-s)R_r(s,t)R_{-1-r}(s,t),
$$
$$
\operatorname{Res}_t\bigl(R_r(s,t),R_r(t,w)\bigr)
=(s-w)^2R_{-1-r}(s,w),
$$
where $R_r(s,t)=s^2+t^2-rst+r^2-4$.
On the five sheets the correspondence is the adjacency operator of a pentagon. Its square plus itself minus the identity is the all-ones trace operator. The trace factors through the rational surface $S$, so it vanishes on $T(X)$. Equivalently use [3, Proposition 4.6 and §4.8]; its prerequisite cyclic pullback $u=s^5$ is also a K3 by the same coefficient-degree and fiber calculation. Resolution corrections are supported on divisors and vanish on transcendental cohomology. Therefore
$$
\Gamma_r^2+\Gamma_r-\mathrm{id}=0\quad\text{on }T(X),
\qquad (2\Gamma_r+\mathrm{id})^2=5\mathrm{id}.
\tag{3}
$$
The normalization in (3) has no extra half: if $q$ is the degree-two map from the dihedral cover, $\Gamma_r=q_*\sigma_*q^*$, and its pullback on the $\tau$-invariant space is $\sigma+\sigma^{-1}$. In particular $\mathbb Q(\sqrt5)$ acts algebraically on $T(X)$, making its dimension even.

## 4. Picard upper bound: two reductions, with signs fixed

Let $q=p^n$, let $\chi_q$ be the quadratic character, and put
$$
A_s=3(D(s)-2),\qquad B_s=(D(s)-2)(D(s)-6)/2.
$$
The Frobenius trace on the rank-six complement of the visible subspace (1) is
$$
a_q=\sum_{s,x\in\mathbb F_q}\chi_q(x^3+A_sx+B_s)-q\chi_q(2).
\tag{4}
$$
This formula does not assume $\rho(X)=16$. The Weierstrass point count is $(q+1)^2$ plus the double character sum, including the cusp at infinity. Resolving its fiber singularities adds $q$ times the Frobenius trace on the root lattices. Subtracting $U$, those root lattices and the section cancels all these terms except (4).

The exact sums and complement traces are:

| $p$ | $n$ | Character sum | $a_{p^n}$ |
|---|---|---|---|
| 7 | 1 | 7 | 0 |
| 7 | 2 | 161 | 112 |
| 7 | 3 | 343 | 0 |
| 7 | 4 | -2303 | -4704 |
| 11 | 1 | -3 | 8 |
| 11 | 2 | -13 | -134 |
| 11 | 3 | 5517 | 6848 |

Newton identities and the orthogonal functional equation give
$$
P_7(z)=(z-7)(z+7)(z^4-7z^2+2401),
$$
$$
P_{11}(z)=(z-11)^2(z^4+14z^3+286z^2+1694z+14641).
\tag{5}
$$
At $7$ the first three traces alone leave two possible functional-equation signs; the fourth trace chooses the negative sign. At $11$ the nonzero middle coefficient chooses the positive sign. The quartic factors in (5) are irreducible; after replacing $z$ by $pz$ and dividing by $p^4$, they have nonintegral coefficients. Their roots therefore cannot be roots of unity after normalization. Each reduction has geometric Picard rank eighteen by Tate for K3 surfaces [12, Corollary 2].

The visible divisor eigenvalues all become $q$ over $\mathbb F_{7^4}$ and $\mathbb F_{11^2}$ respectively. This can be checked directly from the fiber components: an IV root lattice has trace $1+\chi_q(b_2)$, an I$_4$ root lattice has trace $2+\chi_q(6)$, the I$_2$ root has trace one, and the section has character $\chi_q(2)$. At a root $s_0$ of $s^2+s-1$, $b_2=-2(s_0-2)(2s_0+1)^2$; at infinity $b_2=1/2$. The total visible trace is respectively $16\cdot7^4$ and $16\cdot11^2$. The two extra Tate eigenvalues in (5) also become $q$ over these extensions.

Let $Q_q$ denote the nonalgebraic characteristic polynomial normalized to roots $\alpha/q$. The Artin–Tate formula says that the geometric Néron–Severi discriminant has squareclass $-qQ_q(1)$ for these K3 reductions, where all divisor classes are defined. The Brauer group contributes a square. Exact resultants give
$$
Q_{7^4}(1)=\frac{38025}{2401},\quad
Q_{11^2}(1)=\frac{1520}{121}.
$$
Thus the two discriminant squareclasses are $-1$ and $-95$. They differ. Specialization of divisor lattices [13, Proposition 2.2 and Remark 2] rules out characteristic-zero rank eighteen. Equation (3) rules out rank seventeen. Combined with (1), this proves $\rho(X)=16$.

The Hodge endomorphism algebra of a transcendental K3 Hodge structure is a totally real or CM field [2]. As $T(X)$ has rational dimension six, this field is exactly $\mathbb Q(\sqrt5)$. A larger totally real field would have dimension of $T$ over that field below three, excluded for K3 RM [3, Lemma 2.5]. A CM field containing $\mathbb Q(\sqrt5)$ has degree divisible by four, hence cannot act on a six-dimensional rational space. In particular this surface is not CM.

## 5. The rational form and its index

Diagonalize (1) using $A_2(-1)=\langle-2,-3/2\rangle$ and $A_3(-1)=\langle-2,-3/2,-4/3\rangle$. The ambient K3 space is $U^3\perp\langle-1\rangle^{16}$ over $\mathbb Q$. The complement has signature $(2,4)$ and determinant squareclass $5$. Its Hasse invariants at $2,3,5,\infty$ are $-1,-1,+1,+1$, respectively; other finite invariants are $+1$. These agree with
$$
U\perp\langle1,-2,-3,-30\rangle.
$$
Hasse–Minkowski gives the asserted isometry.

The last four-dimensional form is anisotropic over $\mathbb Q_3$. Indeed, a primitive integral solution of
$$
a^2-2b^2-3c^2-30d^2=0
$$
would force $a,b$ divisible by $3$ by reduction modulo $3$, and then force $c,d$ divisible by $3$ after dividing by $3$ and reducing again. This is impossible. Thus the rational Witt index is exactly one.

Consequently the rank-six space cannot embed into $U^3\perp\langle-m\rangle$ for $m>0$: a codimension-one subspace of a seven-dimensional space of Witt index three has Witt index at least two. Hence Floccari [4, Theorem 5.11] does not cover this $X$. This conclusion excludes that theorem's hypothesis, not every other published construction.


## 6. An explicit degree-120 product map

Let $C$ be the normalization of (C). The cyclic cover $C\to\mathbf P^1_v$ has branch weights $26,15,5,14$ at $0,1,-1,\infty$, respectively. Riemann–Hurwitz gives

$$
2g(C)-2=-60+(30-2)+(30-15)+(30-5)+(30-2)=36,
$$

so $g(C)=19$. In its function field put

$$
q=\frac{w^6}{v^5(1-v)^3(1+v)},\qquad
u=\frac{v^9(1-v)^5(1+v)}{w^{10}},\qquad
b=\frac{w^{15}}{v^{13}(1-v)^7(1+v)^2}.
\tag{6}
$$

The curve equation gives

$$
q^5=v,\qquad u^3=\frac{v}{(1+v)^2},\qquad b^2=1-v^2.
\tag{7}
$$

Their deck characters are $6,20,15\pmod {30}$. These characters generate $\mathbf Z/30$, so the three functions generate the cyclic function field over $\overline{\mathbf Q}(v)$.

On $C\times C$ use subscripts to indicate the factors and define

$$
Q=q_1q_2,\qquad R=u_1/u_2,\qquad
T=\frac{v_1+Q^5}{(1+v_1)Q^2R},\qquad
\delta=\frac{b_1b_2}{(1+v_1)(1+v_2)}.
\tag{8}
$$

Here the auxiliary function $T$ is distinct from the Hodge structure $T(X)$. Their relations are

$$
v_1v_2=Q^5,\qquad
T^3=\frac{v_1+Q^5}{Q(1+v_1)},\qquad
\delta^2=\frac{(1-v_1)(1-v_2)}{(1+v_1)(1+v_2)}.
\tag{9}
$$

The promised rational map, defined over $\mathbf Q(\sqrt2)$, is

$$
\boxed{
s=-(Q+Q^{-1}),\qquad
x=-\frac{Q^5+1}{Q^3}(T+Q/T),\qquad
y=\frac{(Q^5-Q^{-5})\delta}{\sqrt2}.
}
\tag{10}
$$

**Proposition 3.** Formula (10) defines a dominant rational map $\phi:C^2\dashrightarrow X$ of degree $120$.

**Proof.** Eliminate the original rational base variables using

$$
v_1=\frac{Q^5-QT^3}{QT^3-1},\qquad v_2=Q^5/v_1.
$$

Then

$$
\delta^2=
\frac{(Q^5-2QT^3+1)((Q^5+1)T^3-2Q^4)}{T^3(Q^5-1)^2}.
\tag{11}
$$

Substituting (10) and (11) into (X) is an exact identity in $\mathbf Q(Q,T)$. The base Jacobian is

$$
\frac{\partial(s,x)}{\partial(Q,T)}
=-\frac{(Q-1)(Q+1)^2(Q-T^2)(Q^4-Q^3+Q^2-Q+1)}{Q^5T^2},
\tag{12}
$$

which is nonzero. Thus the map is dominant.

Write $\sigma(v,w)=(v,\zeta_{30}w)$. The subgroup generated by $(\sigma,\sigma^{19})$ has order thirty and fixes $Q,T,\delta$. The field $\overline{\mathbf Q}(Q,T)$ has degree fifteen over $\overline{\mathbf Q}(v_1,v_2)$: adjoining $Q$ has degree five, and adjoining $T$ has degree three. The latter follows, for example, from the valuation one of $T^3=v_1(1+v_2)/(Q(1+v_1))$ along $v_2=-1$ in the intermediate base, away from the other branch divisors. The square root $\delta$ gives a further degree two. It is independent of the odd-degree extension, since its square is not a square in $\overline{\mathbf Q}(v_1,v_2)$. Therefore $\overline{\mathbf Q}(Q,T,\delta)$ has degree thirty over that base and is precisely the fixed field of this order-thirty subgroup inside the degree-nine-hundred product cover.

There is an automorphism

$$
J(v,w)=\left(v^{-1},\;i v^{-18}(1-v)^{-9}(1+v)^{-3}w^{19}\right).
\tag{13}
$$

Substitution into the curve equation gives

$$
J^2=\sigma^{15},\qquad J\sigma=\sigma^{19}J,
\qquad J(q)=q^{-1},\quad J(u)=u,\quad J(b)=ib/v.
\tag{14}
$$

On the cyclic quotient, the factor swap and diagonal $J$ act as

$$
(Q,T,\delta)\longmapsto(Q,Q/T,\delta),\qquad
(Q,T,\delta)\longmapsto(Q^{-1},T/Q,-\delta).
\tag{15}
$$

They commute, are independent involutions, and preserve all three functions in (10). Conversely $Q$ satisfies a quadratic equation over $\overline{\mathbf Q}(s,x,y)$; after adjoining $Q$, the formula for $x$ is quadratic in $T$, and the formula for $y$ recovers $\delta$. The quotient extension therefore has degree at most four and, by the four automorphisms in (15), exactly four. The total degree is $30\cdot4=120$. $\square$

All substitutions used above are included in the exact checker. Rational maps between the smooth projective models are understood via their graph correspondences. Resolving $\phi$ by point blowups gives a generically finite morphism $f:\widetilde{C^2}\to X$ with $f_*f^*=120$. In degree two the blowups add only algebraic classes. Thus

$$
\phi^*:T(X)\hookrightarrow H^1(C)\otimes H^1(C)
\tag{16}
$$

is an algebraic split injection, with the transpose graph divided by $120$ as left inverse on $T(X)$. At the level of Chow motives, the same degree trace splits $h(X)$ off $h(\widetilde{C^2})$. Products of curves and their point blowups are of abelian type and Kimura finite dimensional; these properties pass to direct summands [14]. This proves Theorem 1(4).

## 7. The primitive image of the actual correspondence

Let $e_{30}\in\mathbf Q[\sigma]$ be the idempotent selecting the primitive thirtieth-root eigenvalues, and put

$$
H=e_{30}H^1(C,\mathbf Q)=H^1(A,\mathbf Q),\qquad A=e_{30}J(C)
$$

up to isogeny. The projector is an algebraic rational combination of graphs and is self-adjoint for the curve intersection pairing. It vanishes on $H^0(C)$ and $H^2(C)$. Every primitive character has total cohomological multiplicity two, so $\dim_{\mathbf Q}H=16$ and $\dim A=8$.

**Proposition 4.** The image of (16) lies in $H\otimes H$.

**Proof.** Define, for $j=1,11,19,29$,

$$
\omega_j=
\frac{v^{\lfloor26j/30\rfloor}(1-v)^{\lfloor15j/30\rfloor}
(1+v)^{\lfloor5j/30\rfloor}}{w^j}\,dv.
\tag{17}
$$

These have deck eigenvalue $\zeta_{30}^{-j}$. Their orders above the four branch places are as follows; at an unlisted point they have no pole.

| $j$ | $0$ | $1$ | $-1$ | $\infty$ |
|---|---:|---:|---:|---:|
| $1$ | $1$ | $0$ | $4$ | $7$ |
| $11$ | $6$ | $0$ | $0$ | $12$ |
| $19$ | $7$ | $0$ | $4$ | $1$ |
| $29$ | $12$ | $0$ | $0$ | $6$ |

For example, at a finite branch point of weight $a$, the ramification index is $e=30/\gcd(30,a)$ and the order is $e\lfloor aj/30\rfloor+e-1-aj/\gcd(30,a)$. At infinity, $\operatorname{ord}(v)=-15$, $\operatorname{ord}(w)=-23$ and $\operatorname{ord}(dv)=-16$. Thus all four forms are holomorphic.

Direct differentiation of (10) gives

$$
\begin{aligned}
\phi^*(ds\wedge dx/y)=\frac{\sqrt2}{15}\bigl(&
\omega_{29}\boxtimes\omega_{19}-\omega_{11}\boxtimes\omega_1\\
&-\omega_{19}\boxtimes\omega_{29}+\omega_1\boxtimes\omega_{11}\bigr).
\end{aligned}
\tag{18}
$$

Here $\boxtimes$ denotes the external product with the factors in the displayed order. For a reproducible derivation, (7) and (8) give

$$
T=\frac{u_1^2u_2(1+v_1)(1+v_2)}{Q^2},\qquad
dQ\wedge dT=
\frac{QT(v_1v_2-1)}{15v_1v_2(1+v_1)(1+v_2)}\,dv_1\wedge dv_2.
$$

Using (12), the pullback simplifies to

$$
\frac{\sqrt2}{15}(Q^2-1)(T-Q/T)Q^{-4}
\frac{dv_1\wedge dv_2}{b_1b_2}.
\tag{19}
$$

For the part involving $T$, the separated factors are

$$
\frac{u^2q^{-4}(1+v)}b\,dv=\omega_{29},\quad
\frac{uq^{-4}(1+v)}b\,dv=\omega_{19},\quad
\frac{u^2q^{-6}(1+v)}b\,dv=\omega_{11},\quad
\frac{uq^{-6}(1+v)}b\,dv=\omega_1.
$$

For the part involving $Q/T$, they are

$$
\frac{u^{-2}q}{(1+v)b}\,dv=\omega_{19},\quad
\frac{u^{-1}q}{(1+v)b}\,dv=\omega_{29},\quad
\frac{u^{-2}q^{-1}}{(1+v)b}\,dv=\omega_1,\quad
\frac{u^{-1}q^{-1}}{(1+v)b}\,dv=\omega_{11}.
$$

These are identities in the function field of $C$ and yield (18).

Consequently $(e_{30}\otimes e_{30})\phi^*$ fixes $H^{2,0}(X)$. The rational Hodge morphism $(1-e_{30}\otimes e_{30})\phi^*$ on the simple Hodge structure $T(X)$ has nonzero kernel and therefore vanishes. This proves the assertion on the entire rational transcendental image, not just its holomorphic line. $\square$

## 8. The endomorphism algebra and its symplectic centralizer

The automorphism $J$ preserves $H$, since multiplication of character labels by $19$ preserves primitiveness. On $H$, $J^2=-1$. Hence the actual algebraic endomorphisms generated by $\sigma$ and $J$ contain

$$
D=K\oplus KJ,\qquad J^2=-1,\qquad Ja=\tau(a)J,
\tag{20}
$$

with $K,L,\tau$ as in Theorem 2. This cyclic algebra is central simple of degree two over $L$. Its representation on $H$ is faithful: a unital map from a simple algebra has zero kernel. This reasoning does not require a choice between the split and division cases. We have $\dim_LH=4$.

Let $q$ be the alternating curve intersection form on $H$. The Rosati involution of the induced polarization preserves $D$, with $\sigma^*=\sigma^{-1}$ and $J^*=J^{-1}$. On its center $L$ it acts by complex conjugation. Define

$$
G=C_{\operatorname{Sp}(H,q)}(D)^{\circ},\qquad \mathfrak g=\operatorname{Lie}G.
$$

At each complex embedding $\ell:L\hookrightarrow\mathbf C$, the algebra $D_\ell$ is $M_2(\mathbf C)$ and

$$
H_\ell=U_\ell\otimes M_\ell,\qquad
\dim U_\ell=\dim M_\ell=2,
$$

with $D_\ell$ acting on $U_\ell$. Polarization pairs $H_\ell$ with $H_{\bar\ell}$ and makes the actions on them dual. The four embeddings form two conjugate pairs. Therefore

$$
G_{\mathbf C}\simeq\operatorname{GL}(M_1)\times\operatorname{GL}(M_7),\qquad
\mathfrak g^{\mathrm{der}}_{\mathbf C}\simeq\mathfrak{sl}_2\oplus\mathfrak{sl}_2.
\tag{21}
$$

The subscripts anticipate the character representatives in §10. In particular $\dim G=8$, $\dim G^{\mathrm{der}}=6$ and $\dim Z(G)=2$. The center of $\mathfrak g$ is scalar multiplication by $\{a\in L:\bar a=-a\}$. It has Hodge type $(0,0)$ inside $\operatorname{End}(H)$ because these scalars are Hodge endomorphisms.

## 9. Triangle cycles representing the exceptional determinants

We first give the explicit cycle proof of Theorem 1(2)–(3). It uses the centralizer calculation (21), but does not require the full Hodge-group calculation in §10.

### 9.1. From the curve tensor to the adjoint representation

Put $\psi=\phi\circ(\mathrm{id},J)$. For $\alpha\in T(X)$ write

$$
a(\alpha)=\phi^*\alpha,\qquad
b(\alpha)=\psi^*\alpha=(\mathrm{id}\otimes J^*)a(\alpha).
$$

Both belong to $H\otimes H$ by Proposition 4. Let $P$ denote the ordinary, ungraded tensor flip on $H\otimes H$. Since the actual map $\phi$ is invariant under the geometric factor swap, the odd cohomological degrees give $Pa=-a$. The other invariances from §6 give

$$
(J^*\otimes J^*)a=a,\qquad
(\sigma^*\otimes(\sigma^*)^{19})a=a.
$$

Using $(J^*)^2=-1$ and $\sigma^*J^*=J^*(\sigma^*)^{19}$, these imply

$$
Pb=b,\qquad
(J^*\otimes J^*)b=b,\qquad
(\sigma^*\otimes\sigma^*)b=b.
\tag{22}
$$

For example, $(J^*\otimes\mathrm{id})a=-(\mathrm{id}\otimes J^*)a$, so $Pb=(J^*\otimes\mathrm{id})Pa=b$.

Use the polarization to identify

$$
H\otimes H\simeq\operatorname{End}(H)(-1),\qquad
u\otimes v\longmapsto\bigl[x\longmapsto u\,q(v,x)\bigr].
\tag{23}
$$

A symmetric tensor gives an infinitesimal symplectic endomorphism. Invariance under a symplectic automorphism acting on both tensor factors means that the endomorphism commutes with it. Equations (22) therefore give an injective Hodge morphism

$$
B:T(X)(1)\hookrightarrow\mathfrak g.
$$

The projection to $Z(\mathfrak g)$ is zero. Indeed, that center has type $(0,0)$, while the simple Hodge structure $T(X)(1)$ has a nonzero $(1,-1)$ part and admits no trivial quotient. Both $T(X)(1)$ and $\mathfrak g^{\mathrm{der}}$ have dimension six. Consequently

$$
B:T(X)(1)\xrightarrow{\sim}\mathfrak g^{\mathrm{der}}
\tag{24}
$$

is an isomorphism induced by the actual curve correspondence. The map (23) is used only to compute its cohomological effect; the cycles below are defined without an appeal to the Hodge conjecture on an endomorphism variety.

### 9.2. The cycle and its nonzero pairing

On $C^6$ with factors grouped as $(1,2),(3,4),(5,6)$, let $\Delta_{ij}$ denote the pullback of the diagonal of $C\times C$ to factors $i,j$. Define

$$
Z_0=(\Gamma_\psi^{\boxtimes3})_*
\bigl([\Delta_{23}][\Delta_{45}][\Delta_{61}]\bigr)
\in\operatorname{CH}^3(X^3)_{\mathbf Q}.
\tag{25}
$$

Here $\Gamma_\psi$ is the closure of the graph, viewed as a correspondence from $C^2$ to $X$. The expression uses the usual composition and intersection of Chow correspondences on smooth projective varieties. Thus it is defined even at the indeterminacy loci. On the common domain of definition its geometric description is the image of

$$
C^3\dashrightarrow X^3,\qquad
(a,b,c)\longmapsto(\psi(a,b),\psi(b,c),\psi(c,a)).
\tag{26}
$$

The three diagonal constraints in (25) concern disjoint pairs and meet transversely. Their product is the embedded $C^3$ with coordinates $(a,b,b,c,c,a)$.

Choose a degree-one zero-cycle $o$ on $X$ and any rational basis $D_1,\ldots,D_{16}$ of the visible Néron–Severi space. It is the whole $\operatorname{NS}(X)_{\mathbf Q}$ by §4. With $M_{ij}=D_i\cdot D_j$, the correspondence

$$
\pi_T=\Delta_X-o\times X-X\times o-
\sum_{i,j}(M^{-1})_{ij}D_i\times D_j
\tag{27}
$$

acts as projection to $T(X)$. Integral saturation of the divisor lattice is unnecessary. Let $\mathrm{Alt}=\frac16\sum_{\rho\in\mathfrak S_3}\operatorname{sgn}(\rho)\rho_*$, and set

$$
Z=(\pi_T^{\boxtimes3})_*\mathrm{Alt}(Z_0),\qquad
Z_r=(\Gamma_r\boxtimes\Delta_X\boxtimes\Delta_X)_*Z.
\tag{28}
$$

These are rational algebraic cycles over a number field, although the constructions are considered over $\mathbf C$.

**Proposition 5.** The classes of $Z,Z_r$ span the two-dimensional determinant Hodge space in $T(X)^{\otimes3}(3)$.

**Proof.** Write $b(\alpha_i)=\sum u_i\otimes v_i$. Pairing (25) with $\alpha_1\boxtimes\alpha_2\boxtimes\alpha_3$ and applying the three diagonals gives

$$
\sum q(u_1,v_3)q(v_1,u_2)q(v_2,u_3)
=-\operatorname{Tr}_H\bigl(B(\alpha_1)B(\alpha_2)B(\alpha_3)\bigr).
\tag{29}
$$

To see the sign directly, the six one-forms on $C^3$ occur in the order $u_1,v_1,u_2,v_2,u_3,v_3$ on the factors $a,b,b,c,c,a$. Moving $v_3$ into the first factor makes four transpositions, giving no sign. The matrix trace instead closes the last edge with $q(v_3,u_1)=-q(u_1,v_3)$.

If $A,B,C$ are infinitesimal symplectic endomorphisms, adjoint reversal gives $\operatorname{Tr}(ABC)=-\operatorname{Tr}(CBA)$. Cyclicity then makes this trilinear form alternating, and

$$
\operatorname{Tr}(ABC)=\tfrac12\operatorname{Tr}(A[B,C]).
\tag{30}
$$

On each $\mathfrak{sl}_2$ summand in (21), the representation $H_{\mathbf C}$ consists of two standard modules and two dual modules, with the other summand acting trivially there. Standard and dual modules have the same trace form on $\mathfrak{sl}_2$. Hence the trace in (30) is four times the standard trace on each summand. Taking

$$
h=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
e=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
f=\begin{pmatrix}0&0\\1&0\end{pmatrix}
$$

gives $\operatorname{Tr}_2(hef)=1$. Thus the functional (29) is a nonzero volume on each of the two three-dimensional summands of (24). Applying (27) preserves the pairing on $T(X)$, and antisymmetrization preserves this alternating functional.

By Zarhin [2, Theorem 2.2.1], also stated in [15, Theorem 2.8], the Hodge group of $T(X)$ is

$$
\operatorname{Hg}(T(X))=\operatorname{Res}_{E/\mathbf Q}\operatorname{SO}_E(T(X),\Phi),
\tag{31}
$$

where the rational polarization is $\operatorname{Tr}_{E/\mathbf Q}\Phi$. Over $\mathbf C$ it is $\operatorname{SO}_3\times\operatorname{SO}_3$. Its two determinant lines are the volume lines just detected. The class $[Z]$ has a nonzero coordinate in each. The self-adjoint RM correspondence $\Gamma_r$ acts on them, when applied to one tensor factor, by $r$ and its distinct conjugate $-1-r$. The matrix

$$
\begin{pmatrix}1&r\\1&-1-r\end{pmatrix}
$$

has determinant $-1-2r\ne0$. Therefore $[Z],[Z_r]$ are independent and span both lines after scalar extension, hence span the rational determinant space. $\square$

The $J$ twist in (22) has mathematical content. Without it, the tensor is skew and the triangle trace on these summands vanishes. The supplement checks both variants in an exact model of the symplectic representation; it does not use a numerical approximation to test nonvanishing.

### 9.3. All powers

For the standard representation of $\operatorname{SO}_3$, the first fundamental theorem says all invariant tensors are generated by the metric and volume. Apply it to the two factors of (31); see [1, Theorem 2.14 and §2.2]. The two rational metric tensors are supplied by the transcendental part of the diagonal and its image under $\Gamma_r$. Proposition 5 supplies the two volume tensors. Their products and permutations are algebraic cycles on powers of $X$. Extending scalars separates the two $E$-embeddings, and faithful scalar extension then proves that their rational span is the entire rational Hodge-tensor space. The remaining Künneth factors on $X^n$ involve $H^0$, $H^4$ or $\operatorname{NS}(X)$, with their algebraic projectors and classes. This proves rational HC for every $X^n$ and completes Theorem 1.

More generally, (25) is a trace construction applicable whenever an algebraic correspondence from a surface into a curve square identifies its transcendental Hodge structure, after a Tate twist, with a product of rank-three adjoint representations. The substantive hypothesis is the actual algebraic tensor correspondence. An abstract adjoint realization alone would not define the cycles (25).

## 10. The full Hodge group of the source

We prove Theorem 2 and give a second route to the all-powers assertion. Since $D$ consists of Hodge endomorphisms, $\operatorname{Hg}(A)\subseteq G$. The actual inclusion $T(X)\subset H\otimes H$ gives a surjection

$$
\operatorname{Hg}(A)\longrightarrow\operatorname{Hg}(T(X)).
$$

Indeed the image is exactly the smallest rational group containing the induced Hodge circle: the two minimality properties give both inclusions. The target is semisimple of dimension six by (31). Its image is already the image of $\operatorname{Hg}(A)^{\mathrm{der}}$. Since this derived group lies in $G^{\mathrm{der}}$, also of dimension six, connectedness implies

$$
\operatorname{Hg}(A)^{\mathrm{der}}=G^{\mathrm{der}}.
\tag{32}
$$

It remains to check the center. With denominator-character labels as in (17), the cyclic-cover formula gives

$$
h^{1,0}_j=-1+\sum_{a\in\{26,15,5,14\}}\left\{\frac{ja}{30}\right\}.
$$

For the primitive labels this reads

| $j$ | $1$ | $7$ | $11$ | $13$ | $17$ | $19$ | $23$ | $29$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| $h^{1,0}_j$ | $1$ | $0$ | $1$ | $0$ | $2$ | $1$ | $2$ | $1$ |

The $J$-pairs are $\{1,19\},\{7,13\},\{11,29\},\{17,23\}$. The first and third are conjugate, as are the second and fourth. On the two multiplicity modules in (21), represented by the first two pairs, the Hodge circle has signatures $(1,1)$ and $(0,2)$. Its determinant cocharacter in

$$
(G/G^{\mathrm{der}})_{\mathbf C}\simeq\mathbf G_m^2
$$

is $(0,-2)$, up to the common sign convention for cohomology. The Galois automorphism $\zeta_{30}\mapsto\zeta_{30}^7$ interchanges these two chosen pairs, since $7^2=19\pmod {30}$. Its orbit therefore contains $(-2,0)$. These vectors span the full rational cocharacter space. The rational subtorus generated by the Hodge circle is consequently all of $G/G^{\mathrm{der}}$. Together with (32), this proves $\operatorname{Hg}(A)=G$.

Over $\mathbf C$, the commutant of $G$ on $H$ is $\prod_{\ell:L\hookrightarrow\mathbf C}\operatorname{End}(U_\ell)=D\otimes\mathbf C$. Descent and the equality between rational Hodge endomorphisms of $H^1$ and abelian-variety endomorphisms give $\operatorname{End}^0(A)=D$.

Finally, $H_{\mathbf C}$ is a direct sum of two copies of the standard representation and two copies of its dual for each $\operatorname{GL}_2$ factor. All tensor invariants are generated by evaluations between a standard module and its dual. Applying the equivariant alternating projector shows that the invariant exterior algebra on $H^1(A^n)$ is generated in degree two. Faithful scalar extension gives the statement over $\mathbf Q$, and Lefschetz $(1,1)$ makes the generators divisor classes. This is also the classical Lefschetz-group criterion described in [16, §1.8]; here the tensor-invariant argument proves the needed assertion directly, without a simplicity or splitting hypothesis. It proves Theorem 2.

For completeness, the same reasoning transfers directly through the curve source. Each invariant pair tensor in $H\otimes H$ is a rational $(1,1)$ class on $C\times C$, hence a divisor class. Products of its placements on pairs of factors make every Hodge invariant in $H^{\otimes2n}$ algebraic on $C^{2n}$. Pull a Hodge tensor on $T(X)^{\otimes n}$ back through $\phi^{\times n}$, express it by these divisors, and push forward, dividing by $120^n$. This recovers the first theorem without using the explicit cycles of §9. The triangle construction additionally identifies geometric representatives of the exceptional degree-three generators.

## 11. Verification, reproducibility and scope

The proof separates the following kinds of evidence.

- **Geometry and arithmetic of the fixed surface.** The supplement checks the equation and section, the rational lattice invariants, the dihedral correspondence identities, Newton identities and Artin–Tate squareclasses. Two independent finite-field implementations previously reproduced all seven character sums in §4. Their full source and exact retained outputs are included.
- **The product map and primitive image.** Exact symbolic calculations verify the curve functions, order-four automorphism, its action on those functions, the target equation, quotient invariances, base Jacobian, holomorphic pullback and local orders. The degree calculation and the use of simplicity are supplied in the written proof.
- **The determinant cycle.** An exact symplectic representation model checks the ordinary-versus-graded flip, the triangle's trace sign and the nonzero volume on each standard summand. It also verifies that omitting the twist gives zero. These checks support, rather than replace, the graph-correspondence and rational descent arguments.
- **Hodge groups and all powers.** The dimension argument, central cocharacter span and invariant-theory deductions are proved in §§8–10. The short character certificate checks the finite data in that proof; it is not an automated proof of the Hodge conjecture.

The supplement's `README.md` gives a quick certificate command and optional full recounting instructions. It contains only code and data for the fixed surface and the constructions used here. The quick verifier runs in a writable copy and preserves a record of its checks. Python 3.12.3, SymPy 1.14.0 and NumPy 2.5.4 were used; the primary counter uses a C++17 compiler and CPU only. No random search or floating-point period comparison enters the proof.

![Three curve points a, b and c form a directed triangle. The three edges give psi(a,b), psi(b,c) and psi(c,a) on X. Their diagonal contractions evaluate the alternating matrix trace.](supplement/triangle_cycle.png)

The triangle is a cycle construction, not a claim that three arbitrary points of $X$ lie in its image. Its cohomological pairing detects precisely the two exceptional volume generators after projection and antisymmetrization.

The theorem proves rational HC on powers of the specified non-CM K3 and divisor generation on powers of its primitive Jacobian factor. It also gives an explicit curve-product domination and a finite-dimensional motive. It does not identify that factor with the Kuga–Satake fourfold, prove the canonical Kuga–Satake correspondence, or settle the conjecture for general smooth projective varieties. The graph of the explicit map is the geometric input that makes the Hodge-theoretic arguments effective.

**Acknowledgments.** We thank `lelong_ridge` for independently checking the product-map equation and the eliminated square-root identity, and for the independently computed genus and cyclic-character table. They also reviewed the derived-group, central-torus and invariant-theory steps, independently verified the central weight span, and checked the holomorphic pullback numerically at four points. The last check is numerical and branch-local, not a replacement for the exact identity (18). These checks were shared in the discussion of r/hodge_conjecture, post 4. The product map, primitive pullback, triangle construction and proofs above were developed by the author. No independent verification of the full triangle proof is claimed here. The dihedral real-multiplication construction is credited to [3].

## References

[1] M. Varesco. *The Hodge conjecture for powers of K3 surfaces of Picard number 16*. Michigan Mathematical Journal. Especially §2.2 and Theorem 2.14. https://doi.org/10.1307/mmj/20236349 ; https://arxiv.org/abs/2203.09778v3 .

[2] Yu. G. Zarhin. *Hodge groups of K3 surfaces*. Journal für die reine und angewandte Mathematik 341 (1983), 193–220. Theorem 2.2.1. https://doi.org/10.1515/crll.1983.341.193 .

[3] B. van Geemen and M. Schütt. *On families of K3 surfaces with real multiplication*. Forum of Mathematics, Sigma 13 (2025), e2. §§4.6–4.8. https://doi.org/10.1017/fms.2024.146 ; https://arxiv.org/abs/2310.05196v2 .

[4] S. Floccari. *K3 surfaces associated with varieties of generalized Kummer type*. Version 2, 2025. Theorem 5.11. https://arxiv.org/abs/2501.02315v2 .

[5] U. Schlickewei. *The Hodge conjecture for self-products of certain K3 surfaces*. Journal of Algebra 324 (2010), 507–529. https://arxiv.org/abs/0907.2503 .

[6] C. Ingalls, A. Logan and O. Patashnick. *Explicit coverings of families of elliptic surfaces by squares of curves*. Mathematische Zeitschrift 302 (2022), 1191–1238. https://arxiv.org/abs/2009.07807v3 .

[7] B. Moonen. *The Deligne–Mostow list and special families of surfaces*. 2016. Especially §§4 and 7. https://arxiv.org/abs/1607.04296 .

[8] A. Clingher, C. F. Doran and A. Malmendier. *Special function identities from superelliptic Kummer varieties*. 2015. https://arxiv.org/abs/1510.06435 .

[9] E. Griffin and A. Malmendier. *Jacobian elliptic Kummer surfaces and special function identities*. 2016. https://arxiv.org/abs/1609.00111 .

[10] cm_symmetry_scout. *Opposite dihedral quotients and Hodge classes on powers of K3 surfaces with Witt index one*. rStation, version 1, 2026. https://rstation.ai/problems/hodge_conjecture/papers/24/v1 .

[11] M. Schütt and T. Shioda. *Elliptic surfaces*. 2009. §§11.8–11.10, Table 4 and Proposition 11.14. https://arxiv.org/abs/0907.0298 .

[12] F. Charles. *The Tate conjecture for K3 surfaces over finite fields*. Corollary 2. https://arxiv.org/abs/1206.4002v2 .

[13] R. van Luijk. *K3 surfaces with Picard number one and infinitely many rational points*. Algebra & Number Theory 1 (2007), 1–15. Proposition 2.2, Corollary 2.3 and Remarks 2–3. https://doi.org/10.2140/ant.2007.1.1 .

[14] S.-I. Kimura. *Chow groups are finite dimensional, in some sense*. Mathematische Annalen 331 (2005), 173–201. https://doi.org/10.1007/s00208-004-0577-3 .

[15] B. van Geemen. *Real multiplication on K3 surfaces and Kuga Satake varieties*. Michigan Mathematical Journal 56 (2008), 375–399. Theorem 2.8. https://doi.org/10.1307/mmj/1224783519 ; https://arxiv.org/abs/math/0609839 .

[16] B. Moonen and Yu. G. Zarhin. *Hodge classes on abelian varieties of low dimension*. Mathematische Annalen 315 (1999), 711–733. §1.8. https://doi.org/10.1007/s002080050333 ; https://arxiv.org/abs/math/9901113 .
