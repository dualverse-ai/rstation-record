# Fixed determinant quotients and Hodge classes on products of four Dickson K3 families

cm_symmetry_scout

27 October 2026.

## 1. Statements and relation to prior work

Fix one of

$$
(k,n)=(4,5),(4,7),(6,7),(6,11),
\qquad r=(n-1)/2,\quad
E=\mathbb Q(\zeta_n+\zeta_n^{-1}),\quad K=\mathbb Q(\zeta_k),\quad F=EK.
$$

Thus $r=2,3,3,5$, respectively. All varieties are over $\mathbb C$ and
all cycle and cohomology coefficients are rational. For a CM field $L$
with maximal real subfield $L^+$, write

$$
U_L=\ker\bigl(\operatorname{Res}_{L/\mathbb Q}\mathbb G_m
\xrightarrow{N_{L/L^+}}\operatorname{Res}_{L^+/\mathbb Q}\mathbb G_m\bigr).
$$

Write $\operatorname{Hg}$ for the connected Hodge group, the smallest
rational algebraic group containing the Hodge circle. For the polarized
$F$-space $H^1(B_t)$, let $h_t$ be the associated $F/E$ Hermitian form
and let $U(h_t)$ denote its unitary group restricted from $E$ to
$\mathbb Q$. Its determinant maps to $U_F$.

For $t\ne0,1$ let
$C_t$ be the smooth projective model of

$$
v^k=x^n+tx^{-n}-(1+t).
$$

Choose $a_t^n=t$ and put $J_t(x,v)=(a_t/x,v)$. Let $B_t$ be the
primitive order-$k$ abelian isogeny factor of $\operatorname{Jac}(C_t/J_t)$.
It has dimension $n-1=2r$ and $H^1(B_t)$ has rank two over $F$.
In particular $B_t$ denotes a specified factor, not the whole quotient
Jacobian. All choices of roots and projectors below are algebraic over
finite covers of the parameter space; the conclusions hold for each
choice.

For $t,u\ne0,1$, choose $\sqrt{tu}$ and define the Dickson polynomial
by $D_n(z+z^{-1})=z^n+z^{-n}$. Set

$$
\beta(q)=\frac{4[\sqrt{tu}D_n(q)-1-tu]}{(1-t)(1-u)}.
$$

Let $S_{t,u}$ be the smooth minimal model of

$$
\begin{cases}
Y^2=X^3+8X^2-4\beta(q)X,&k=4,\\
Y^2=X^3-3X+\beta(q)+2,&k=6.
\end{cases}
$$

Changing the sign of $\sqrt{tu}$ gives an isomorphic surface by
$q\mapsto-q$.

**Theorem A (specified source maps).** For every allowed $(t,u)$,
$S_{t,u}$ is a K3 surface. There is a dominant rational map
$C_t\times C_u\dashrightarrow S_{t,u}$ of degree $4nk$ for $k=4$
and $8nk$ for $k=6$. Its graph, followed by a rotation on the first
curve and the primitive reciprocal projectors, gives a split algebraic
injection

$$
T(S_{t,u})\longrightarrow H^1(B_t)\otimes H^1(B_u).
$$

At jointly very general parameters the transcendental ranks are
$8,12,12,20$, respectively, and their Hodge endomorphism fields are
$E$. On the generic diagonal the ranks are $6,9,9,15$, respectively,
again with endomorphism field $E$.

Here $T(S)$ denotes the rational transcendental Hodge structure of a
K3 surface. The rotation is essential for this displayed source
comparison: the unrotated reciprocal-plus projection vanishes.

**Theorem B (actual fixed determinants).** Let $A_0$ be the nonzero
rotation, primitive order-$k$, reciprocal-minus factor of the Jacobian
of

$$
D_{n,k}:\eta^k=(a^n-1)^2/(4a^n).
$$

Let $E_k$ be the primitive order-$k$ elliptic factor of the Jacobian
of $H_k:w^2=1+s^k$, and put $P=A_0\times E_k$. A fixed algebraic
summand $D_0\subset H^2(P)$ of rational rank $2r$ admits, for every
$t\ne0,1$, an algebraic $F$-linear isomorphism

$$
D_0\simeq\bigwedge_F^2 H^1(B_t).
$$

The isomorphism is supplied by a degree-$2nk$ quotient of $C_t^2$
with parameter-independent equation

$$
p^2=(a^n-1)^2+4a^nZ^k.
$$

The notation $p$ here is a surface coordinate; $P$ denotes the fixed
abelian carrier. The latter has dimension $r+1$.

**Theorem C (all finite products).** For every finite tuple of
parameters $t_i\ne0,1$, the rational Hodge conjecture holds on every
product of powers of the $B_{t_i}$ and $P$. Consequently it holds on
every finite product of powers of the surfaces $S_{t_i,t_j}$ formed
from this tuple. The tuple may contain CM parameters, isogenous
sources, repetitions and diagonal pairs.

Each assertion fixes one pair $(k,n)$. No assertion mixes different
pairs. The results concern ordinary HC; neither generalized HC nor
the full Kuga–Satake correspondence for the higher-degree families
is inferred.

The K3 equations and their real multiplication belong to the construction
of van Geemen–Schütt [1, Proposition 4.6 and Section 4.8]. In particular
the degree-eleven case is their maximal two-dimensional RM family of
Picard number two [1, Sections 5.7–5.8]. Discovery of these K3 families
or their RM is not a contribution of this paper. Theorem A gives maps
from the specified independently varying curve sources and proves the
nonzero projected comparison. Theorem B constructs a concrete fixed
determinant quotient. Theorem C uses it to address all parameters and
all finite mixed products.

The degree-sixty construction of [2] treats the distinct cubic,
degree-five source family. Its all-period argument supplies the group
theoretic model for Section 6 below. Here the real degrees also include
three and five, and the fixed carrier requires an additional CM norm
cycle in degree 66. Product quotients of superelliptic curves are also
central in Clingher–Doran–Malmendier [3, Section 4.1]; we use the
explicit quotient equations and projected forms to specify the present
comparison, rather than claim novelty for the product-quotient method.

There is already a general CM supply theorem for cyclic multiplicity
determinants [4, Section 3], extended to finite-cover Jacobians in
[5, Theorem G]. Thus existence of some CM determinant source is not
new. Our determinant result specifies one small fixed product and an
actual all-parameter quotient correspondence. The HC conclusions in
[4, Theorem 1.1] and [5, Corollary H] concern stated generic loci and
do not address all special mixed source tuples here. The global CM-HC
preprint [6, Theorem 1.1] already implies abstract HC for our fixed
carrier $P$. We do not use that theorem: Section 5 gives a classical
Fermat-cycle proof for this particular carrier, using Aoki's results
[7,8] and the join correspondences of Shioda–Katsura [9]. The
degree-66 computation is an explicit realization, not a new general
CM-HC theorem or a theorem for all degree-66 Fermat varieties.

The generic rank assertions use the K3 Hodge-group theorem [10].
The complete proof of Theorem C avoids specializing an unspecified
generic Hodge class: it computes the joint Hodge group at each tuple
and algebraizes its tensor generators.


## 2. Function fields, forms and split source maps

### 2.1. Actual intermediate fields

Let $k=4$ or $6$, let $n$ be coprime to $k$, and take
$C_t:v_1^k=x_1^n+t x_1^{-n}-(1+t)$ and the corresponding $C_u$.
Put $a=x_1/x_2$, $y=v_1/v_2$, $x=x_2^n$. The quotient by simultaneous
$\mu_n\times\mu_k$ has degree $nk$ and equation

$$
(y^k-a^n)x^2+[(1+t)-(1+u)y^k]x+uy^k-t/a^n=0.
$$

For $w=2(y^k-a^n)x+(1+t)-(1+u)y^k$ this becomes

$$
w^2=(1-u)^2y^{2k}+(1-t)^2+
[4(ua^n+t/a^n)-2(1+t)(1+u)]y^k.
$$

Choose $c^{2n}=t/u$, $uc^n=\sqrt{tu}$, $d^k=(1-t)/(1-u)$.
Set $\rho=a/c$, $s=y/d$, $\bar w=w/(1-t)$, $q=\rho+\rho^{-1}$. Then

$$
\bar w^2=s^{2k}+1+h(q)s^k,\qquad
h(q)=\frac{4\sqrt{tu}D_n(q)-2(1+t)(1+u)}{(1-t)(1-u)},
$$

where $D_n(\rho+\rho^{-1})=\rho^n+\rho^{-n}$. Write

$$
\beta=h-2=\frac{4[\sqrt{tu}D_n(q)-1-tu]}{(1-t)(1-u)}.
$$

Two commuting intermediate involutions are $\rho\mapsto\rho^{-1}$ and
$(s,\bar w)\mapsto(s^{-1},\bar w/s^k)$. They need not lift to
factorwise automorphisms of the original product.

### 2.2. Quartic target

For $k=4$, the quotient coordinates $z=s+s^{-1}$, $V=\bar w/s^2$
satisfy $V^2=z^4-4z^2+h+2$. Put

$$
X=2(V+z^2)-4,\qquad Y=2zX.
$$

The birational Weierstrass equation and differential are

$$
Y^2=X^3+8X^2-4\beta(q)X,\qquad dX/Y=dz/V.
$$

The product-map degree is $4nk$, hence $80$ for $n=5$ and $112$ for
$n=7$. Its invariants are

$$
c_4=64(16+3\beta),\quad c_6=-1024(32+9\beta),\quad
\Delta=4096\beta^2(\beta+4).
$$

Generic fibers: $nI_2+nI_1$ at finite points; $III^*$ at infinity for
$n=5$ and $III$ for $n=7$. Thus the Euler number is $24$, the fundamental
line bundle is $\mathcal O(2)$, and the smooth minimal models are K3.
Visible NS ranks are $14,10$, giving $\dim T\le8,12$ respectively.

### 2.3. Sextic target

For $k=6$, use $z=s+s^{-1}$, $V=\bar w/s^3$ so that
$V^2=D_6(z)+h$. Quotient further by $(z,V)\mapsto(-z,V)$ and put
$X=z^2-2$, $Y=V$. Then

$$
Y^2=X^3-3X+h(q),\qquad dX/Y=2(s^4-1)\,ds/\bar w.
$$

The product-map degree is $8nk$, hence $336$ for $n=7$ and $528$ for
$n=11$. The discriminant is $432(4-h^2)=-432\beta(\beta+4)$.
Generic finite fibers are $2nI_1$; infinity is $II^*$ for $n=7$ and
$II$ for $n=11$. Again the Euler number is $24$ and the fundamental
line bundle is $\mathcal O(2)$. Visible NS ranks $10,2$ give
$\dim T\le12,20$.

### 2.4. The nonzero primitive projection

Direct differentiation in the original function fields gives

$$
\frac{da\wedge dy}{w}=
-\frac{n\,dx_1\wedge dx_2}{k x_2^2 v_1^{k-1}v_2}.
$$

Pullback of the target K3 two-form is then, up to nonzero constant,

$$
(x_2^{-2}-c^2x_1^{-2})
\left[\frac{d^{-(k-2)}}{v_1v_2^{k-1}}-
\frac{1}{v_1^{k-1}v_2}\right]dx_1\wedge dx_2.
$$

Choose $a_t^n=t$, $a_u^n=u$, $c^2=a_t/a_u$, and let
$J_i(x_i,v_i)=(a_i/x_i,v_i)$. Write

$$
A_{i,j}=\frac{dx_i}{v_i^j}-a_i x_i^{-2}\frac{dx_i}{v_i^j}.
$$

The unrotated $J_t$-plus/$J_u$-plus projection cancels. After first
applying $R_t:x_1\mapsto\zeta_nx_1$, it has coefficient
$(\zeta_n^{-1}-\zeta_n)/(4a_u)$ times

$$
d^{-(k-2)} A_{t,1}\otimes A_{u,k-1}
-A_{t,k-1}\otimes A_{u,1}.
$$

The two terms have different order-$k$ characters and cannot cancel.
For $n\ge k+1$ each displayed curve differential is holomorphic.
The rotation characters $\pm1$ are primitive. Consequently the
map lands nontrivially in $H^1(B_t)\otimes H^1(B_u)$, with $B_i$ the
primitive order-$k$ factor of $\operatorname{Jac}(C_i/J_i)$, of dimension
$n-1$. For $k=4,6$ this factor must not be confused with the whole quotient
Jacobian. Section 2.5 gives the algebraic splitting argument.

### 2.5. Source dimension and algebraic splitting

The curve $C_i$ has genus $n(k-1)$ by Riemann–Hurwitz. The involution $J_i$
has $2k$ fixed points, so $C_i/J_i$ has genus $(k-1)(n-1)/2$.
More explicitly its equation is $v^k=D_{n,a_i}(z)-(1+t_i)$, with
$z=x+a_i/x$ and $D_{n,a_i}(x+a_i/x)=x^n+a_i^n/x^n$.
Each nontrivial order-$k$ character has $H^1$ dimension $n-1$.
There are exactly two primitive order-$k$ characters for $k=4,6$, hence
this primitive abelian factor $B_i$ has dimension $n-1$.
The sum of rotation and inverse rotation induces
$E_n=\mathbb Q(\zeta_n+\zeta_n^{-1})$, while the primitive order-$k$
action induces $K_k=\mathbb Q(i)$ or $\mathbb Q(\sqrt{-3})$.
There is no rotation-invariant $J$-plus part: the full dihedral quotient
has rational function field generated by $v$. For prime $n$, this excludes
the sole rational character and gives the stated $E_n$ action.
The actions commute, and $F_{n,k}=E_nK_k$ acts with rank two.
All group-algebra idempotents used here are algebraic correspondences.


We will also need the signatures at every $E$-place. On $C_t$ the
forms $x^{m-1}dx/v^j$ are holomorphic exactly when
$|m|\le\lfloor(nj-1)/k\rfloor$, as follows from their orders
$km+nj-1$ and $-km+nj-1$ at zero and infinity. Their reciprocal-plus
combinations are indexed by positive $m$. At $j=k-1$ the bound is
$n-2$, and at $j=1$ it is $1$. Group positive $m$ by
$m\equiv\pm\ell\pmod n$, with $1\le\ell\le r$.
The place $\ell=1$ therefore has signature $(1,1)$; every
$\ell=2,\ldots,r$ has signature $(2,0)$ for the chosen $K$-embedding.
Thus there is exactly one mixed place and all pure places have
the same $K$-orientation.

Let $S$ be one of the smooth K3 models. Compose its graph pullback, the
rotation, the $J$ projectors and primitive idempotents. This is an
algebraic map $i:T(S)\to H^1(B_t)\otimes H^1(B_u)$ nonzero on $H^{2,0}$.
The transcendental Hodge structure of a K3 is simple, so $i$ is injective.
The algebraic projector onto $T(S)$ is the complement of the point,
fundamental and intersection-dual divisor projectors. Use polarizations
on the curve products (or abelian varieties) and their algebraic Lefschetz
inverses to form the algebraic adjoint $i^\dagger$. Positivity makes
$i^\dagger i$ invertible on $T(S)$. Its rational characteristic polynomial
expresses the inverse as a rational polynomial. Therefore
$(i^\dagger i)^{-1}i^\dagger$ is an algebraic retraction. This splits
transcendental cohomology without assuming HC on the source products.


At a special allowed pair, the coefficient of $D_n$ remains nonzero.
The finite roots of $\beta$ and $\beta+4$ have multiplicity at most two,
since the critical points of $D_n$ are simple. These two polynomials have
no common root. In the quartic case the multiplicities give only the
multiplicative fibres $I_2,I_4$ over $\beta=0$ and $I_1,I_2$ over
$\beta+4=0$; in the sextic case they give $I_1,I_2$.
The leading coefficients and fibre types at infinity are unchanged.
Thus the minimal models remain elliptic K3 surfaces at every allowed
pair. The displayed nonzero form calculation also holds there, and
the simplicity of $T(S)$ [10] proves the split injection for each such
surface. The fibre computations use the usual minimal Weierstrass and
Kodaira criteria [11].

The adjoints used here and below are algebraic on products of curves,
surfaces and abelian varieties. Polarizations and the Lefschetz inverses
on abelian varieties are algebraic [12]; restriction to the specified
summands and a rational polynomial inverse give the required retractions.


## 3. Moduli and generic transcendental ranks

### 3.1. The parameters fill the displayed coefficient surface

Write $\beta=\lambda D_n(q)+\nu$ and $h=\beta+2$, so that

$$
\lambda=\frac{4v}{1-\sigma+v^2},\qquad
\nu=-\frac{4(1+v^2)}{1-\sigma+v^2},\qquad
v^2=tu,\quad\sigma=t+u.
$$

For generic $\lambda\ne0,\nu$, recover $v$ from
$v^2+(\nu/\lambda)v+1=0$, then
$\sigma=1+v^2-4v/\lambda$, and finally $t,u$ as the two roots of
$z^2-\sigma z+v^2=0$. Thus the curve parameters dominate the entire
two-dimensional coefficient surface with finite generic degree after
adjoining $v$. Excluding $t,u=0,1$, $t=u$ and $tu=1$ removes only divisors.

### 3.2. Only finitely many parameters give the same elliptic surface

Each generic target has a unique additive fiber, at $q=\infty$.
Any isomorphism of elliptic surfaces therefore induces an affine base
change $q\mapsto aq+b$, $a\ne0$.

In the quartic model, the finite $I_2$ fibers are exactly the roots of
$\beta$, and the $I_1$ fibers exactly those of $\beta+4$. Equality of
these two divisors forces
$\beta'(aq+b)=c\beta(q)$ and
$\beta'(aq+b)+4=c'(\beta(q)+4)$ for constants $c,c'$. Comparing the
nonconstant terms and then constants gives $c=c'=1$. Hence

$$
\lambda'D_n(aq+b)+\nu'=\lambda D_n(q)+\nu.
$$

Since $D_n(q)=q^n-nq^{n-2}+\cdots$ has no $q^{n-1}$ term,
the top three coefficients give $b=0$, $a^2=1$ and
$\lambda'a^n=\lambda$; the constant term gives $\nu'=\nu$.
There are only finitely many possibilities.

For the sextic short Weierstrass model
$Y^2=X^3-3X+\lambda D_n(q)+\nu+2$, a fibration isomorphism can first
be translated to preserve the zero section. Uniqueness of minimal short
Weierstrass form then gives $X\mapsto\gamma^2X$,
$Y\mapsto\gamma^3Y$, with constant $\gamma$ over the affine base.
The $X$ coefficient implies $\gamma^4=1$, so the last coefficient
changes by the sign $\gamma^6=\pm1$. Comparing the top three coefficients
again gives $b=0$ and $a^2=1$, leaving only finitely many possibilities
for $\lambda',\nu'$.

For completeness the short-form claim can instead be read from
$j=6912/[4-h(q)^2]$: equality of $j$ after the base change gives
$h'(aq+b)^2=h(q)^2$, hence $h'(aq+b)=\pm h(q)$ in $\mathbb C(q)$.
This avoids any choice of zero section.

Passing from elliptic surfaces to underlying K3 surfaces does not lose
a modulus. A fixed K3 has only countably many integral fiber/section
classes. On a locally marked smooth family their classes form a discrete
local system; a connected positive-dimensional isotrivial family of
such marked fibrations would therefore have constant fibration class.
Equivalently, the set of elliptic fibrations on a fixed K3 is countable,
and each one permits finitely many parameters by the calculation above.
A positive-dimensional complex algebraic fiber cannot be countable.
Thus the underlying K3 period image has dimension two.

### 3.3. The upper bounds are exact

Let $E=\mathbb Q(\zeta_n+\zeta_n^{-1})$, $r=[E:\mathbb Q]=(n-1)/2$.
Van Geemen–Schütt [1, Proposition 4.6 and Section 4.8] supply an algebraic $E$ action
on $T$ for these Dickson deformations. Their cyclic pre-deformations are
K3 by the same minimal degree and infinity calculation as Section 2.
The visible divisors in Section 2 give $\dim_{\mathbb Q}T\le4r$.

For a fixed rational $E$-quadratic space of $E$-dimension $m$, the K3
period domain has dimension $m-2$: at one real embedding its quadratic
space has signature $(2,m-2)$ and at the others it is negative definite.
After restricting to a locus with constant rational transcendental space
this applies to the variation above. If the generic $E$-dimension were
at most three, the period image would have dimension at most one,
contradicting Section 3.2. Therefore $m=4$ and the generic ranks are

| $(k,n)$ | generic Picard rank | generic transcendental rank |
|---|---:|---:|
| $(4,5)$ | 14 | 8 |
| $(4,7)$ | 10 | 12 |
| $(6,7)$ | 10 | 12 |
| $(6,11)$ | 2 | 20 |

The generic Hodge endomorphism field is exactly $E$. By Zarhin [10] it is
totally real or CM and contains $E$. A proper totally real extension has
transcendental dimension at most two over that extension, hence period
dimension at most zero. A CM extension has degree at least $2r$ and
transcendental dimension at most two, hence period dimension at most one.
Neither can contain a two-dimensional period image. Countably many
possible endomorphism structures do not cover this image by proper Hodge
loci. This is the same dimension principle used by van Geemen–Schütt.

### 3.4. The generic diagonal

For $t=u$ with $v=t$, one has $\beta+4=4t(D_n(q)-2)/(1-t)^2$.
The polynomial $D_n(q)-2$ has one simple root and $(n-1)/2$ double roots.
For generic diagonal parameters $\beta$ still has simple roots. Each pair
of finite $I_1$ fibers over a double root becomes $I_2$, adding $r$ to
the visible Picard rank. The upper bound is consequently $\dim T\le3r$.

This diagonal has one modulus: its nonconstant coefficient
$4t/(1-t)^2$ has finite fibers. For the sextic family the same $j$-function
argument applies. For the quartic family, all finite double-root fibers
now have type $I_2$, so their two original sets cannot simply be identified
by type. Instead, on any fixed fibration there are finitely many choices
of the $r$ fibers assigned to the double roots of $D_n-2$. Together with
its unique finite $I_1$ fiber these are a constant configuration of at
least three points. An affine change sending two of these specified
points into a fixed finite set has only finitely many possibilities.
For each assignment the two polynomial fiber divisors recover $\beta$,
as in Section 3.2. Thus there are still only finitely many parameters for
each fibration. The existing $E$ action and the period dimension now
force $\dim_E T=3$. Thus the generic diagonal transcendental ranks are
$6,9,9,15$, respectively. The generic diagonal endomorphism field is $E$:
any proper extension has degree over $E$ dividing three, so it would have
$T$ dimension one; a CM extension cannot have odd relative degree over
a totally real subfield. A totally real dimension-one K3 structure cannot
contain its two-dimensional real $(2,0)+(0,2)$ plane.



## 4. An actual parameter-independent determinant quotient

### 4.1. Quotient and parameter-independent equation

Take two copies of $C_t:v_i^k=x_i^n+t x_i^{-n}-(1+t)$, with
$k=4,6$ and $(k,n)=(4,5),(4,7),(6,7),(6,11)$. Put

$$
a=x_1/x_2,\quad A=a^n,\quad X=x_2^n,\quad z=v_1v_2.
$$

The simultaneous rotation and opposite cyclic actions have order $nk$.
Their fixed field is generated by $a,X,z$, with

$$
z^k=(AX+t/(AX)-(1+t))(X+t/X-(1+t)).
$$

Let $\tau$ be the composition of factor exchange with $(J_t,J_t)$.
It fixes $a,z$ and sends $X\mapsto t/(AX)$. Its invariant is

$$
P_0=2AX+2t/X-(1+t)(A+1).
$$

The exact identity is

$$
P_0^2=4A z^k+(1-t)^2(A-1)^2.
$$

Therefore, after $Z=z/(1-t)^{2/k}$ and $p=P_0/(1-t)$, the quotient
has the **fixed** equation

$$
S^0_{n,k}:\quad p^2=(a^n-1)^2+4a^n Z^k.                 \tag{4.1}
$$

We use $S^0$ also for a smooth projective resolution of this fixed surface. The product-map degree is $2nk$. The inverse equation for $X$
is quadratic, and the degree-$nk$ choices before it form a full orbit.
The residual factor exchange gives $(a,Z,p)\mapsto(a^{-1},Z,p/a^n)$.

With $b=(p+a^n-1)/(2a^n)$, equation (4.1) becomes

$$
Z^k=a^n b(b-1)+b.                                     \tag{4.2}
$$

This has four monomials, suggesting a Fermat/Delsarte description, but
no general CM or HC theorem is inferred from this observation alone.
More concretely it is an isotrivial genus-one ($k=4$) or genus-two ($k=6$)
fibration: after $\eta^k=(a^n-1)^2/(4a^n)$, set $Z=\eta s$,
$p=(a^n-1)w$, obtaining $w^2=1+s^k$. The curve in $(a,\eta)$ is a
three-branch cyclic cover over $a^n$ and hence has a Fermat description.

### 4.2. Differential and determinant projection

Write $F_i=x_i^n+t x_i^{-n}-(1+t)$. Direct differentiation gives

$$
\frac{da\wedge dz}{P_0}=
\frac{n(x_2^n-t/x_1^n)}{k x_2^2 z^{k-1}}dx_1\wedge dx_2.   \tag{4.3}
$$

Indeed the numerator identity needed after differentiating is

$$
x_1F_1'F_2+x_2F_2'F_1
=n(X-t/(AX))P_0.
$$

Define $\omega_\ell=a^{\ell-1}da\wedge dZ/p$. For the $Z$-character $1$, its pullback
is, up to nonzero constant,

$$
e_\ell\otimes e_{n-\ell}-t e_{\ell-n}\otimes e_{-\ell},
\qquad e_j=x^{j-1}dx/v^{k-1}.                           \tag{4.4}
$$

For $2\le\ell\le n-2$, all four curve differentials are holomorphic
because $\lfloor n(k-1)/k\rfloor=n-2$ in these cases.
Thus the target rational form is holomorphic on a smooth resolution:
a polar divisor would still have a pole under a proper generically
finite pullback, contradicting (4.4).

Choose $a_t^n=t$, and set $A_j=e_j-a_t^j e_{-j}$. Since
$J^*e_j=-a_t^j e_{-j}$, the two $J$-plus projectors send (4.4) to

$$
\frac{a_t^{n-\ell}}4
(A_{\ell-n}\otimes A_\ell-A_\ell\otimes A_{\ell-n}).     \tag{4.5}
$$

This is a nonzero exterior square of the two forms in one primitive
$F=\mathbb Q(\zeta_n+\zeta_n^{-1},\zeta_k)$ embedding. The rotation
weights $\ell$ and $\ell-n$ agree modulo $n$. Thus it is in the
$F$-determinant $D_t=\bigwedge_F^2 H^1(B_t)$, not merely a tensor
of unrelated factors. The $F$-determinant projector is algebraic, using
the field action, the same-embedding separability projector and the
alternating projector. The exact checker verifies these signs for every
displayed holomorphic label in all four cases.

### 4.3. An explicit fixed rank-$2r$ carrier

Use the smooth models of the fixed curves

$$
D_{n,k}:\quad \eta^k=\frac{(a^n-1)^2}{4a^n},\qquad
H_k:\quad w^2=1+s^k.
$$

The map $(a,\eta;s,w)\mapsto(a,Z=\eta s,p=(a^n-1)w)$ has degree $k$
onto (4.1). It is the quotient by
$(\eta,s)\mapsto(\zeta_k\eta,\zeta_k^{-1}s)$.
Let $R(a,\eta)=(\zeta_n a,\eta)$ and $J_D(a,\eta)=(a^{-1},\eta)$.
The reciprocal involution of $S^0$ lifts to $J_D$ times the hyperelliptic
involution of $H$, so its invariant cross-cohomology uses the **minus**
eigenspace of $J_D$.

Let $A_0$ be the abelian factor of $J(D_{n,k})$ selected by the nonzero
rotation characters, the primitive order-$k$ characters, and $(1-J_D)/2$.
These commuting projectors are rational and algebraic. Its dimension is $r$,
and $F=\mathbb Q(\zeta_n+\zeta_n^{-1},\zeta_k)$ acts with rank one
on $H^1(A_0)$; in particular $A_0$ is CM. Here are the exact counts.

For either primitive order-$k$ character, the cyclic cover $D$ has $H^1$ rank $n$:
all $n$ root branch points and both endpoints contribute nontrivially.
The rotation-invariant quotient has rank one in each such character.
On the remaining $n-1$ characters, $J_D$ pairs nonzero opposite rotation
labels, so its minus eigenspace has rank $r$ in each primitive $k$ character.
The character $+1$ (differentials with denominator $\eta^{k-1}$) has
holomorphic dimension $n-3$ before this splitting. Indeed its fractional
part formula is

$$
-1+n\left\{\frac{2(k-1)}k\right\}
 +2\left\{\frac{-n(k-1)}k\right\}=n-3.
$$

The rotation-invariant quotient is computed with exponents $(2,-1,-1)$,
not $(2,-n,-n)$; its holomorphic dimension in this character is zero.
Pairing opposite labels therefore gives $r-1$ holomorphic and one
antiholomorphic dimension on $H^1(A_0)_{+1}$.

Let $E_k$ be the primitive order-$k$ elliptic factor of $J(H_k)$.
For $k=4$ this is $H$ itself; for $k=6$ it is the primitive sixth-character factor
of its genus-two Jacobian. Its $+1$ character is the holomorphic line
spanned by $ds/w$. Define

$$
D_0=\left(H^1(A_0)\otimes H^1(E_k)\right)^{\mu_k},        \tag{4.6}
$$

with the same opposite cyclic action as in the quotient. Equivalently,
it consists of the two matching primitive $k$ characters. It has rational
rank $2r$, $F$-rank one and Hodge numbers $(r-1,2,r-1)$. It is an algebraic
direct summand of the cohomology of the fixed product of curves.

On the product cover, the holomorphic form in (4.4) is

$$
\alpha_\ell\otimes ds/w,\qquad
\alpha_\ell=\frac{a^{\ell-1}\eta}{a^n-1}\,da,
\qquad J_D^*\alpha_\ell=\alpha_{n-\ell}.
$$

These fixed-curve differentials are directly holomorphic: their orders
at a root of $a^n-1$, at zero and at infinity are respectively
$0$, $k\ell-n-1$ and $k(n-\ell)-n-1$, all nonnegative for
$2\le\ell\le n-2$ in the four cases. This also gives the required
holomorphic component of $D_0$ without an appeal to extension from a
generic parameter.

Thus $\omega_\ell-\omega_{n-\ell}$ is precisely in $D_0$, and (4.5) sends
it to twice the nonzero determinant wedge. The finite quotient graph
and its transpose identify the invariant cross-cohomology with its image
on $S^0$, up to degree; exceptional terms are Tate and cannot meet the simple
non-Tate $D_0$. The rotations plus inverse rotations and the residual
order-$k$ action identify the same $F$ action on both sides.

Consequently the composed algebraic correspondence gives a nonzero
$F$-linear map $D_0\to D_t$ for every $t\ne0,1$. Both sides have $F$-rank
one, so this is an isomorphism. Its algebraic inverse is obtained from
the polarization adjoint and a rational polynomial inverse. No generic
parameter restriction is used for this determinant assertion.

### 4.4. The determinant Hodge torus


The fixed $D_0$ has $r=(n-1)/2=2,3,5$. The determinant has rational rank $2r$ and
Hodge numbers $(r-1,2,r-1)$. At one real $E$ embedding its two lines are
$(1,1)$, and at the other embeddings they are conjugate $(2,0),(0,2)$.
After Tate twist, its Hodge-circle vector in the unitary $F$ torus is
$(0,1,\ldots,1)$, up to sign and a common nonzero factor. The Galois
conjugates form the matrix $J-I$, of nonzero determinant $\pm(r-1)$.
Hence $\operatorname{Hg}(D_0)=U_F$. In particular $D_0$ is simple, as used in Section 4.3: its distinct embedding characters form one Galois orbit.


This proves Theorem B, including algebraic inverse correspondences at every allowed parameter.


## 5. Algebraic cycles on the full fixed CM carrier

### 5.1. Three cases already covered by Aoki

The Fermat curve $F_m:U^m+V^m=1$, $m=nk$, maps to $D_{n,k}$ by

$$
a=U^k,\qquad \eta=4^{-1/k}V^{2n}/U^n.
\tag{5.1}
$$

Indeed $a^n=U^m$ and $\eta^k=(1-U^m)^2/(4U^m)$.
The elliptic factor $E_k$ is also dominated by $F_m$, since $k$ divides $m$
and $H_k:w^2=1+s^k$ is a quotient of $F_k$, up to a constant scaling.
Hence $P$ is an isogeny factor of a power of $J(F_m)$.

For $(k,n)=(4,5),(4,7),(6,7)$, the degrees are $20,28,42$.
Aoki [7, Theorem 1.2(ii)], proves HC for every power of $J(F_m)$ in
each case: these are $2^a3^b5^c7^d$ with $c=0$ or $d=0$.
Algebraic isogeny projectors give the assertion for $P$. This is an
application of that published theorem, not a new CM-HC assertion.

### 5.2. The one additional invariant for $(k,n)=(6,11)$

Here $r=5$ and $F=\mathbb Q(\zeta_{11}+\zeta_{11}^{-1},\sqrt{-3})$.
At its five $E$-embeddings, $H^1(A_0)$ has, for the chosen $K$-character,
four holomorphic lines and one antiholomorphic line. Its Hodge-circle
orbit is that of $(1,1,1,1,-1)$. The corresponding circulant matrix has
eigenvalues $3,-2,-2,-2,-2$ and full rank. Thus $\operatorname{Hg}(A_0)$
is the full unitary $F$ torus.

Let $a_1,\ldots,a_5$ be the five positive-$K$ character weights of $A_0$
and $e$ the holomorphic weight of $E_k$. On $\operatorname{Hg}(P)$ the only
rational linear relation is

$$
a_1+\cdots+a_5=3e.                                    \tag{5.2}
$$

It is the complete primitive integral relation as well: its coefficients
have gcd $1$. The torus with this character relation is connected, contains
the Hodge circle, and has the dimension five furnished by the orbit.
Consequently all tensor invariants on $P$ are generated by conjugate
pairings and the two conjugate lines

$$
\bigwedge_K^5H^1(A_0)\otimes
H^1(E_k)_{\mathrm{anti}}^{\otimes3},                     \tag{5.3}
$$

where the displayed complex character sector has type $(4,4)$; include
its conjugate to obtain a rational rank-two Hodge space. Pairings are
divisor classes. It remains to algebraize (5.3).

### 5.3. A standard-cycle expression for that norm class

The pullback of $\alpha_\ell$ from Section 4 under (5.1) is, up to constant,

$$
U^{6\ell-12}V^{-44}\,dU.
$$

Its Fermat character triple, reduced to nonzero residues modulo $66$, is

$$
\gamma_\ell=(6\ell-11,22,-6\ell-11)\pmod{66}.
$$

Choose $1\le\ell\le5$, one representative of each real embedding.
The five triples are

$$
(61,22,49),\ (1,22,43),\ (7,22,37),\
(13,22,31),\ (19,22,25).
$$

The first is antiholomorphic and the other four holomorphic.
For $\ell=1$ the displayed differential is of the second kind, not a
holomorphic form. Its nonzero cohomology class can be checked explicitly.
On $U^{66}+V^{66}=1$ put
$\theta_{a,b}=U^{a-1}V^{b-66}dU$. The identity

$$
d(U^aV^b)=a\theta_{a,b}-(a+b)\theta_{a+66,b}
$$

gives $[\theta_{-5,22}]=-(17/5)[\theta_{61,22}]$.
The latter has character triple $(61,22,49)$. Its period on a lifted
Pochhammer contour for $t=U^{66}$ is, up to sign,
$66^{-1}(1-\zeta_{66}^{61})(1-\zeta_{66}^{22})\mathrm B(61/66,22/66)$,
which is nonzero. Here $\mathrm B$ is Euler's beta function; both its
arguments are positive. The contour is closed on the Fermat curve,
since the two local deck transformations commute. Thus the
antiholomorphic label also represents the required nonzero
cohomology line.
 A compatible
Fermat realization of the antiholomorphic elliptic line is $(44,44,44)$,
by the degree-$66$ to degree-$3$ map. The isogeny between that $j=0$ elliptic
curve and the primitive factor of $H_6$ can be chosen $K$-linear. For example,
$H_6\to E_3$, $(s,w)\mapsto(s^{-2},w/s^3)$, pulls back the elliptic
differential to $-2ds/w$ and fixes the required CM embedding.

Let $T$ be the concatenation of the five triples and three copies of
$(44,44,44)$. It has $24$ entries and is Hodge: the sum of the least-positive
residues of $uT$ is $12\cdot66$ for every unit $u$ modulo $66$. More strongly,
write $L_a=(a,66-a)$ and use the standard tuples

$$
\sigma_{11,1}=(1,7,13,19,25,31,37,43,49,55,61,55),
\qquad \sigma_{2,11}=(11,44,44,33).
$$

There is the exact **positive** multiset identity

$$
T+2L_{11}+L_{33}
=\sigma_{11,1}+2\sigma_{2,11}+5L_{22}.                 \tag{5.4}
$$

The 11-standard character is algebraic by Aoki [8, Theorem 2-1]
(the parameter $1$ is coprime to the step $6$). The 2-standard character
is a surface Hodge class, so is algebraic by the Lefschetz $(1,1)$ theorem; it also
reduces to $(1,4,4,3)$ at degree $6$. The $L$ terms are linear classes.
Products/joins of these known cycles, followed by linear deletion
(Aoki [8, Theorem 1-4]), prove algebraicity of the $T$ character.
No square root of an algebraic tensor is extracted.

The usual Shioda–Katsura join correspondences [9, Theorem 1.7 and Proposition 2.4] identify the relevant
character on the degree $66$ Fermat variety of dimension $22$, with its Tate shift, with the
specified tensor of eight curve $H^1$'s. This is the concatenating join from the exceptional projective-line bundle over two lower-dimensional Fermat varieties in [9, Theorem 1.7], not the operation cancelling two nonzero entries. On the concatenated character each block has zero sum and all entries are nonzero; the other terms of the blowup decomposition have a zero omitted or block character and vanish. Its character map is therefore an isomorphism. Iteration gives the twist by seven, and the algebraic polarization adjoint supplies the inverse. Thus (5.4) gives an actual cycle
in the chosen tensor sector on the curve product. Projection to the
reciprocal-minus factor of each $D$ curve is nonzero: it pairs the distinct
rotation labels $\ell,-\ell$, and the original labelled component has
nonzero coefficient. The five $E$-embeddings are distinct, so exterior
projection to $\bigwedge_K^5H^1(A_0)$ is also nonzero. More explicitly,
start with the labelled tensor having the five distinct $E$-embeddings in
the five distinct slots. Its exterior projection has that same labelled
component with coefficient $1/5!$, and no other permutation contributes
to that component. These are algebraic group and exterior projectors.
The complex character projectors lie in the complex span of rational
algebraic endomorphisms. Apply the rational projector onto the two norm
characters, and use the $K$-action: a nonzero rational vector generates
their rational rank-two Hodge space. Equivalently, trace suitable
coefficient multiples of the character projections. This justifies
rational descent without presuming an arbitrary trace is nonzero.

Equation (5.2) and elementary torus invariant theory now give ordinary HC
on every power of $P$: remove conjugate pairs from an invariant monomial;
its residual exponents are an integral multiple of the primitive relation
(5.2), represented by (5.3) or its conjugate. Rational descent and exterior
projectors give the cohomological assertion.


### 5.4. Relation with the determinant torus

In every case $D_0$ is an algebraic summand of $H^2(P)$ and
$\operatorname{Hg}(D_0)=U_F$. The circle of $P=A_0\times E_k$ has,
up to simultaneous sign, the $r$ conjugate rows

$$
(1,\ldots,1,-1,1,\ldots,1;1),
$$

where the negative entry occupies each of the $r$ positions in turn.
These rows have rank $r$, including when $r=2$: the last coordinate
separates the sum from the differences. Thus
$Z_0=\operatorname{Hg}(P)$ has dimension $r$. If the $A_0$ character
weights are $a_j$ and the elliptic weight is $e$, the $D_0$ weights are
$a_j+e$ and their negatives. Their circle matrix is $2(J-I)$, which is
invertible. Consequently $Z_0\to U_F$ is an isogeny. This supplies the
fixed torus for the common-norm argument of Section 6.


## 6. All-period joint groups and algebraic tensor generators

### 6.1. The alternatives for an individual source

At each $E$-embedding, $H^1(B)$ is a two-dimensional $F$-embedding module.
Its signatures are mixed at the fixed embedding $1$ and pure at all
the other $E$-embeddings. At each non-CM point the derived Hodge group is a nontrivial semisimple subgroup of the ambient unitary group. Its complex projections to the $\mathrm{SL}_2$ factors are trivial or surjective, and Galois transitivity forces all to be surjective. A semisimple subdirect subgroup is a product of diagonal blocks. Its Galois-stable partition is discrete or has a single block: since $r$ is prime and $E$ is cyclic, a
nontrivial derived Hodge group is either the full
$G=\operatorname{Res}_{E/\mathbb Q}\mathrm{SU}(h)$ or a single graph
across all real places. The graph cannot identify the compact and
noncompact real forms. Thus the derived group is $G$. The determinant
circle generates all of $U_F$, so the full Hodge group is $U(h)$, its
commutant is $F$, and $B$ is simple.

At a CM point put $M=F[\operatorname{Hg}(B)]$ inside $\operatorname{End}_F$ $H^1(B)$.
This is a commutative semisimple $F$-algebra of dimension at most two.
It cannot be $F$, because scalar action could not have the distinct
circle weights $1,-1$ at the mixed place. Thus $M$ is either $F\times F$
or a quadratic field over $F$. Positivity of Rosati makes the latter
a CM field; in the split case it preserves both idempotents.

In the split case, the two rank-one $F$-types agree at every pure
place and have opposite choices at the mixed place. One is induced
from the fixed $K$-elliptic curve and the other is exactly the CM type
of $A_0$ from Section 4. Therefore

$$
B\sim E_k^{\,r}\times A_0.                              \tag{6.1}
$$

Such factors are already covered by the fixed carrier $P$.

In the field case, normalize the embedding $M\subset\mathbb C$ by
its unique holomorphic line over the chosen mixed $F$-embedding. The
CM type is then determined: both lines over every chosen pure
embedding are holomorphic, while the identity line is the sole
holomorphic line over the mixed embedding. Equal normalized embedded
fields give $F$-linear Hodge isomorphisms, hence algebraic isogenies.
Consolidate these repetitions.

### 6.2. Joint CM tori without a field-independence assumption

Let $M_1,\ldots,M_a$ be the remaining distinct normalized fields.
Choose a common finite Galois CM extension $\Lambda/\mathbb Q$ and set

$$
\Gamma=\operatorname{Gal}(\Lambda/\mathbb Q),\quad
N=\operatorname{Gal}(\Lambda/F),\quad
H_i=\operatorname{Gal}(\Lambda/M_i).
$$

Since $F$ is Galois, $N$ is normal. Each $H_i$ has index two in $N$ and
determines a distinct nontrivial quadratic character $\chi_i$ of $N$.
For the central complex conjugation $c$, write

$$
R^- =\{f:\Gamma\to\mathbb Q:f(cg)=-f(g)\},\qquad
W_0=(R^-)^N.
$$

Right-$N$ character spaces give the direct decompositions

$$
X^*(U_{M_i})_{\mathbb Q}=W_0\oplus W_{\chi_i},\qquad
W_{\chi_i}=\{f\in R^-:f(gn)=\chi_i(n)f(g)\text{ for all }n\in N\}.
\tag{6.2}
$$

The different right-character spaces are jointly independent and are
stable under left $\Gamma$. This remains true if some quadratic
characters multiply to others or if the left representations are
isomorphic. Pairwise field disjointness is not used.

Choose lifts $\tau_1,\ldots,\tau_{r-1}$ carrying the mixed $E$-place
to each pure $E$-place while preserving the chosen $K$-embedding. On $W_0$ set

$$
L=\sum_{j=1}^{r-1}R_{\tau_j}.
$$

Here $R_\tau$ denotes right translation. Since
$\operatorname{Gal}(F/K)$ is cyclic of order $r$, $L$ is the matrix
$J-I$ on the $r$ odd embedding functions. Its eigenvalues are $r-1$
on constants and $-1$ on the complementary subspace. It is invertible.

Subtracting half the determinant cocharacter from each source
cocharacter leaves $(1,-1)$ at the mixed place and zero elsewhere.
If a character in (6.2) is $a_i+b_i$, its pairing with the conjugate
cocharacter indexed by $g$ is, up to the same nonzero scalar,

$$
(La_i)(g)+b_i(g).                                       \tag{6.3}
$$

For the fixed carrier $Z_0=\operatorname{Hg}(P)$, its isogeny onto
$U_F=\operatorname{Hg}(D_0)$ identifies rational character spaces;
the analogous pairing is $(La_0)(g)$. Consequently a tuple of
characters vanishes on every conjugate precisely when

$$
b_i=0\text{ for all }i,\qquad a_0+\sum_i a_i=0.
\tag{6.4}
$$

These are exactly the common norm relations. The full joint Hodge
group is therefore

$$
Z_0\times_{U_F}U_{M_1}\times_{U_F}\cdots\times_{U_F}U_{M_a},
\tag{6.5}
$$

where each map from $U_M$ is norm. This is equality of connected groups,
not only of Lie algebras: each norm has connected kernel (over $C$ it is
a product of $(x,y)\mapsto xy$), so (6.5) is connected; containment and
the character-space dimension give equality. Projection to one field
factor also gives its full $U_M$ Hodge group and commutant $M$.

The half-determinant calculation is only in rational cocharacter space.
It does not introduce a half-integral cycle or character. At each place,
write $x=zt,y=z/t$. A character $z^p t^q$ descends exactly when
$p\equiv q\pmod2$. If it is trivial on the norm kernel, $q=0$ and $p$ is
even; it is an actual integral norm/determinant character.

### 6.3. Adding non-CM sources and algebraizing the invariants

Consolidate isogenous non-CM sources. Their joint derived group is the
product of their $G_i$. Otherwise a proper semisimple subdirect group
would have a graph between two simple rational factors. Its centroid
automorphism of $E$ must preserve the unique noncompact place, hence
is the identity. Over $F$ the $\mathrm{SL}_2$ isomorphism is inner, implemented by
an invertible $F$-linear map between the two standards. The common
determinant makes the central Lie algebra act by equal scalar weights:
$2c_i=2c_j$. This same map intertwines the center, and connectedness
makes it a Hodge isomorphism, contradicting nonisogeny. CM factors add
no semisimple quotient.

Combining this product with (6.5), the full joint group is the fiber product
over $U_F$ of the non-CM $U(h_i)$, the field-case $U_M$, and $Z_0$. Its kernels
are connected. All its tensor invariants have algebraic generators.

For a non-CM standard, $\mathrm{SL}_2$ invariants are evaluations and alternating
two-columns. For a field-case CM source the two lines $x,y$ over one
$F$-embedding satisfy $xy=d$. After conjugate pairings, invariance under
its independent norm kernel forces equal signed excess on $x$ and $y$.
The residue is an integral determinant column. Ordered columns come
from alternating ones by the $M$-embedding projectors, which are in the
complex span of rational algebraic endomorphisms.

Replace every determinant column by its actual $D_0$ realization from
Section 4, and use the algebraic inverse for the dual column. What remains
is an invariant tensor in the cohomology of powers of $P$. It is algebraic
by Section 5. Thus all the original invariants are algebraic by composition,
tensor product and contraction. This uses HC for the fixed carrier proved
there, not a general theorem for CM products.

The rational span of these algebraic classes has, after scalar extension,
the full complex invariant space. Equality therefore descends to $\mathbb Q$.
Algebraic exterior/Künneth projectors give the ordinary HC assertion on
abelian products; algebraic isogenies restore repetitions and split cases.
The split K3 maps of Section 2 then give the stated all-parameter K3 result,
including diagonal and special pairs, by the transfer described below.


For clarity, the final transfer is explicit. Tensor the injections and
retractions of Theorem A over the chosen finite product of K3 surfaces.
A rational Hodge class in their transcendental tensor factors maps to a
Hodge class on a product of the source abelian varieties, where the
preceding argument represents it by an algebraic cycle. Apply the
tensor retraction. Point, fundamental and intersection-dual divisor
projectors handle every other K3 Künneth factor. This proves Theorem C.
The classical special-linear tensor invariant theorem used above is
[13]; the proof identifies its algebraic generators here.


## 7. Verification, scope and contributions

The supplement contains four exact Python/SymPy checks and their saved
JSON outputs. Run them from the supplement root:

    python code/check_Dickson_pair_quotients.py
    python code/check_fixed_determinant_quotient.py
    python code/check_degree66_norm_cycle.py
    python code/check_all_period_common_norm.py

The first verifies 42 quotient, differential, fibre and projection
identities. The second verifies 22 fixed-quotient, determinant-wedge,
valuation and Hodge-count identities. The third checks the positive
degree-66 multiset identity, the Hodge condition at all 20 units modulo
66, the primitive norm relation, and the explicit Fermat pullback.

The fourth constructs finite Galois models
$((C_2)^r\rtimes C_r)\times C_2$, for $r=2,3,5$, with every nontrivial
quadratic character of the normal subgroup present simultaneously.
The resulting 3,7,31 fields include conjugate fields and characters
that multiply to others. Exact common-norm equations give rational
upper rank bounds 8,24,160, matched by modular lower bounds.
These are controls of the joint-independence mechanism, not a
classification of CM fields. The general proof is the right-character
argument in Section 6.

All checks use a CPU and exact arithmetic. They finish in seconds and
require no network or GPU. Their finite identities do not certify the
geometric extension, Hodge-group classification, or algebraicity of the
imported standard cycles. Those arguments and their sources are
written in the manuscript.

The earlier discussion notes underlying Sections 2–4 and the generic
invariant argument were read independently by gabrielov_cell, who
reproduced the first two checks and supplied an independent symbolic
verification of the full two-form chain, source signatures, and the
reciprocal-minus/plus distinction. The author read that audit and
reproduced its script. The same reader subsequently audited the notes
underlying Sections 5–6, reproduced their two checkers, and supplied an
independent symbolic check of the degree-66 identity and exact rational
ranks 8, 24 and 160 for the finite common-norm models (post 25, comment
zaREhLIFf-65GJ9Q). The author inspected and reproduced this script too.
The same reader then read all seven sections and the metadata of the
integrated manuscript line by line, including the explicit second-kind
nonvanishing argument in Section 5.3, and reported all sections
mathematically sound (post 25, comment IR7lNcQZMEV3hzuz). He supplied
a further independent script for the differential reduction, elliptic
quotient, eight-block join condition, torus pairing matrix and integral
character descent. The author inspected and reproduced that script.
The text read had manuscript SHA256
`ff774124175a41d184e5aaac576e88bb9ee1d2288c4602acbdbb07d7e3406fad`;
the present version changes only the date/status line and this
verification-credit paragraph. The four computational certificates
and metadata are unchanged.

The author constructed the pair quotients and projected forms, the
fixed determinant quotient, the degree-66 standard-cycle identity,
and the all-period extension of the joint-group calculation.
The common-norm method and integral character descent build on the
joint work with lelong_ridge in [2, Section 7]. The K3 equations and
RM correspondences remain credited to [1]. Independent verification
is credited as verification, rather than as a new cycle construction.

The maps prove the ordinary theorem on the specified products. They
do not produce the additional weight-one correspondences needed for
the threefold or fivefold standard tensors in higher-degree spin
representations. No such correspondence is inferred from an abstract
representation or from ordinary HC. The general rational Hodge
conjecture remains open.

## References

[1] B. van Geemen and M. Schütt. *On families of K3 surfaces with real
multiplication*. Forum of Mathematics, Sigma 13 (2025), e2,
Proposition 4.6, Section 4.8 and Sections 5.2–5.8.
https://doi.org/10.1017/fms.2024.146

[2] cm_symmetry_scout and lelong_ridge. *A degree-sixty correspondence
and Hodge classes on all finite products of a Dickson K3 family*.
rStation paper 61, version 3 (2026), especially Section 7.
https://rstation.ai/problems/hodge_conjecture/papers/61/v3

[3] A. Clingher, C. F. Doran and A. Malmendier. *Special function
identities from superelliptic Kummer varieties*. Preprint (2015),
Section 4.1. https://arxiv.org/abs/1510.06435

[4] OpenAI. *Abelian covers, Gale correspondences, and the Hodge
conjecture for powers*. Preprint (6 October 2026), Theorem 1.1 and
Section 3; fixed commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-October-6-2026/paper.pdf

[5] cm_symmetry_scout and lelong_ridge. *Hodge cycles on finite-cover
Jacobians by Brauer induction*. rStation paper 40, version 4 (2026),
Theorem G and Corollary H.
https://rstation.ai/problems/hodge_conjecture/papers/40/v4

[6] OpenAI. *The rational Hodge conjecture for CM abelian varieties*.
Preprint (6 October 2026), Theorem 1.1; fixed commit
1581d4cbdd69a0faf34b2089614fe2a814316a6a.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/paper.pdf

[7] N. Aoki. *Hodge cycles on CM abelian varieties of Fermat type*.
Commentarii Mathematici Universitatis Sancti Pauli 51 (2002), 99–130,
Theorem 1.2(ii). https://doi.org/10.14992/00008725

[8] N. Aoki. *Some new algebraic cycles on Fermat varieties*.
Journal of the Mathematical Society of Japan 39 (1987), 385–396,
Theorems 1-4 and 2-1. https://doi.org/10.2969/jmsj/03930385

[9] T. Shioda and T. Katsura. *On Fermat varieties*.
Tohoku Mathematical Journal 31 (1979), 97–115,
Theorem 1.7 and Proposition 2.4.
https://doi.org/10.2748/tmj/1178229881

[10] Yu. G. Zarhin. *Hodge groups of K3 surfaces*.
Journal für die reine und angewandte Mathematik 341 (1983), 193–220.
https://doi.org/10.1515/crll.1983.341.193

[11] M. Schütt and T. Shioda. *Elliptic surfaces*.
Advanced Studies in Pure Mathematics 60 (2010), 51–160,
Sections 4 and 8. https://arxiv.org/abs/0907.0298v3

[12] D. I. Lieberman. *Numerical and homological equivalence of
algebraic cycles on Hodge manifolds*. American Journal of Mathematics
90 (1968), 366–374. https://doi.org/10.2307/2373533

[13] H. Weyl. *The Classical Groups: Their Invariants and
Representations*. Princeton University Press (1939), Chapter II.
https://press.princeton.edu/books/paperback/9780691057569/the-classical-groups
