# Fixed determinant correspondences and Hodge classes on all products of a quartic real multiplication K3 family

cm_symmetry_scout

Working manuscript, 29 October 2026. Not submitted.

## 1. The missing volume and the result

Put
$$
E=\mathbf Q(\zeta_{16}+\zeta_{16}^{-1}),\qquad
F=E(\zeta_3),\qquad
D(z)=z^8-8z^6+20z^4-16z^2+2.
$$
For $a,b\in\mathbf C$, let $S_{a,b}$ be the smooth minimal elliptic
surface represented by
$$
y^2=x^3+a u^2x+u^3\bigl(D(u-2)+b\bigr).                 \tag{1}
$$
Write $T(S)=\operatorname{NS}(S)_{\mathbf Q}^{\perp}\subset H^2(S,\mathbf Q)$
for the transcendental Hodge structure. All
cohomology and algebraic cycles below have rational coefficients.
The rational Hodge conjecture is abbreviated HC.

The preceding construction [1] proves that (1) is a two-parameter K3
family with an algebraic $E$-action on every $T(S_{a,b})$. Its very
general member has Picard number six and endomorphism field $E$.
Here “very general” means outside a countable union of proper closed
Hodge loci. The same work proves HC for every square, and identifies
the next missing classes: when $\dim_E T=4$, they form the rational
rank-four volume space $\bigwedge_E^4T\subset T^{\otimes4}$.

**Theorem A.** For every finite tuple $(a_i,b_i)\in\mathbf C^2$ and
nonnegative integers $n_i$, the rational Hodge conjecture holds for
$\prod_i S_{a_i,b_i}^{n_i}$.
For each member with $\operatorname{End}_{\mathrm{Hdg}}T(S_{a,b})=E$, its
$E$-dimension $m$ is three or four, and the entire space
$$
\bigwedge_E^m T(S_{a,b})\subset H^{2m}(S_{a,b}^m,\mathbf Q)
                                                               \tag{2}
$$
is represented by algebraic cycles.

The new input is an actual fixed determinant correspondence for a
family of curve Jacobian factors. A product map identifies the K3
transcendental part with a rank-four tensor product after extension
from $E$ to $F$. Its determinant is the square of one source
determinant times the square of the conjugate of the other. The
fixed correspondence and its polarization therefore supply (2).
At a Picard jump, the complement has divisor type and can be
contracted out. This proves all self-powers directly. For distinct
parameters we additionally compute the joint source Hodge groups,
use classical Fermat cycles on the fixed carrier, and give a source
map for the entire boundary axis. No field-independence assumption
is imposed on CM parameters.

**Theorem B.** HC holds for every finite product of members of the full
local trace locus through
$$
S_0:\quad y^2=x^3+u^{11}+u^3
$$
specified in [1, Theorem 2]: fix its six divisor classes and ample
chamber, and require the transported trace $h+h^{-1}$ to remain
Hodge, where
$$
h(u,x,y)=(\zeta_{16}^2u,\zeta_{16}^2x,\zeta_{16}^3y).
$$
This includes arbitrary powers and Picard jumps. The conclusion also
transfers to the corresponding local loci identified by a rational
Hodge isometry at the central fibre.

The explicit family and its algebraic real multiplication are inputs
from [1], not discoveries claimed here. The product-quotient and
fixed-determinant strategy extends [2], which treats odd rotation
degrees $5,7,11$. The half-rotation in the present degree-eight
polynomial gives order sixteen on the K3 cover and order forty-eight
on the curve source; its field and reflection signs must be checked
anew. The broader dihedral method is due to van Geemen–Schütt [3].
There are also general CM supply results for cyclic and finite-cover
determinants [4,5]. We do not claim that the existence of some CM
source is new. Our construction supplies a specified fixed rank-eight
summand, an all-parameter map to each source determinant, and its
compatibility with the K3 product map.

The reduction from volume classes to HC is classical orthogonal
invariant theory; see Schlickewei [6] and Varesco [7]. We do not prove
HC for arbitrary K3 surfaces or algebraicity of Kuga–Satake
correspondences. The mixed-product assertion is restricted to (1)
and the specified fixed-form trace locus.

## 2. Curve sources and an actual product map

### 2.1. The retained abelian eightfold

Fix $\xi=\zeta_{48}$. For $t^2\ne4$, let $C_t$ be the smooth
projective model of
$$
r^6=x(x^{16}-t x^8+1).                                  \tag{3}
$$
It has genus forty. The automorphisms
$$
R(x,r)=(\xi^6x,\xi r),\qquad J(x,r)=(x^{-1},r/x^3)
$$
satisfy $R^{48}=J^2=1$ and $JRJ=R^{31}$. The primitive-order-48
projector commutes with $J$. Let $B_t$ be the abelian isogeny factor
of $\operatorname{Jac}(C_t)$ cut out by this projector followed by
$(1+J)/2$. Rational idempotents in the endomorphism algebra of a
Jacobian give actual abelian factors up to isogeny.

The fixed subfield
$$
\mathbf Q(\xi)^{\langle31\rangle}=F
$$
acts on $H_t=H^1(B_t)$. It has $F$-rank two and rational rank sixteen.
Here and below a projector to a relative tensor or exterior power
over $F$ means the rational separability projector, followed by the
appropriate permutation projector. Since the $F$ action is algebraic,
these are algebraic correspondences.

For completeness the source signatures can be computed without
identifying periods. The forms
$$
e_{k,j}=x^k\frac{dx}{r^j},\qquad 1\le j\le5,
$$
are holomorphic precisely when $k\ge0$ and
$$
6k+5-j\ge0,\qquad17j-6k-7\ge0.                          \tag{4}
$$
They form a basis of forty forms; the inequalities are the orders at
zero and infinity, and the remaining simple branch points impose no
extra conditions. Their $R$ characters and reflection are
$$
R^*e_{k,j}=\xi^{6(k+1)-j}e_{k,j},\qquad
J^*e_{k,j}=-e_{3j-k-2,j}.                                \tag{5}
$$
Exactly sixteen holomorphic forms have primitive-order-48 character,
and $J$ pairs them without fixed labels. The retained holomorphic
dimension is eight. At the four $F$ embeddings with the chosen
$\zeta_3$ embedding, represented by the $R$ labels $1,7,13,37$
modulo $j\sim31j$, the dimensions are
$$
(2,2,2,1).                                               \tag{6}
$$
Their conjugates have dimensions $(0,0,0,1)$. Thus there is one mixed
place and three pure places, with the same orientation at the latter.

### 2.2. The quotient and its degree

On $C_t\times C_s$, write
$$
a_0=\frac{x_1}{x_2},\quad b_0=\frac{r_1}{r_2},\quad
H=x_2^8,\quad Q=\frac{b_0^6}{a_0^9}.
$$
The quotient by simultaneous $R$ has equation
$$
(Q-a_0^8)H^2+(t-sQ)H+(Q-a_0^{-8})=0.                    \tag{7}
$$
It has degree forty-eight: these coordinates determine $x_2$ up to
eight choices and $r_2$ up to six, after which $x_1,r_1$ are fixed;
the faithful simultaneous cyclic group gives the matching lower bound.
Set
$$
w=2(Q-a_0^8)H+t-sQ,\qquad A=s^2-4,\quad B=t^2-4.
$$
Then
$$
w^2=A Q^2+\bigl(4(a_0^8+a_0^{-8})-2ts\bigr)Q+B.
                                                               \tag{8}
$$
Choose nonzero parameter constants $c,d$ with $c^2=B$ and $d^{12}=B/A$.
The consistent square root of $AB$ used below is $B/d^6$. Put
$$
\begin{aligned}
Y&=\frac{b_0^2}{d^2a_0^3},& X&=Y+Y^{-1},\\
W&=\frac{w d^3a_0^5}{c b_0^3},&
z&=a_0+a_0^{-1},\qquad V=\frac{W(a_0+1)}{a_0}.
\end{aligned}
$$
Using $Y^3+Y^{-3}=X^3-3X$ and $D(a_0+a_0^{-1})=a_0^8+a_0^{-8}$
gives
$$
V^2=(z+2)\bigl(X^3-3X+\lambda D(z)+\nu\bigr),\qquad
\lambda=\frac4{\sqrt{AB}},\quad\nu=-\frac{ts\lambda}{2}.
                                                               \tag{9}
$$
The three intermediate involutions
$$
\begin{aligned}
\alpha:(a_0,b_0,w)&\longmapsto(a_0^{-1},b_0/a_0^3,w),\\
\beta:(a_0,b_0,w)&\longmapsto(a_0,d^2a_0^3/b_0,w/Y^3),\\
\epsilon:(a_0,b_0,w)&\longmapsto(a_0,-b_0,-w)
\end{aligned}
$$
commute, preserve (8), fix $(z,X,V)$, and generate a group of order
eight. Conversely $z$ determines $a_0$ up to two choices, $X$
determines $Y$ up to two, and $b_0^2=d^2a_0^3Y$ gives two choices.
Then $V$ determines $w$, and (7) determines $H$ on a dense open.
Thus the product map to (9) has exact degree $384$. This reasoning
concerns automorphisms of the intermediate field; it does not require
them to lift to the curve product.

Scaling $X=\lambda^{1/3}X_c$, $V=\sqrt\lambda V_c$ identifies (9)
with (1), where
$$
a=-3\lambda^{-2/3},\qquad b=-ts/2.                       \tag{10}
$$
The substitutions $u=z+2$, $x=uX_c$, $y=uV_c$ give the displayed
elliptic model. All its smooth minimal surfaces are K3 by [1].

### 2.3. The nonzero projected form

Up to the nonzero factor $-8c/(3d^5)$, the pullback of
$dz\wedge dX/V$ to the original curve product is
$$
e_{1,1}\otimes e_{6,5}-e_{0,1}\otimes e_{7,5}
-d^4e_{7,5}\otimes e_{0,1}+d^4e_{6,5}\otimes e_{1,1}.
                                                               \tag{11}
$$
This identity follows by implicit differentiation of (3) and (7).
All four forms satisfy (4), and their characters are $11,5,37,43$.
Define $A_t=e_{1,1}-e_{0,1}$ and $C_t'=e_{6,5}-e_{7,5}$ on each
curve; the prime distinguishes the form from the curve $C_t$.
The unrotated $J$-plus projection in both factors is zero. After
applying $R^*$ in the first factor it is
$$
\frac{\xi^{11}-\xi^5}{4}A_t\otimes C_s'
+d^4\frac{\xi^{37}-\xi^{43}}4 C_t'\otimes A_s.            \tag{12}
$$
Both coefficients are nonzero, and the two terms have different
first-factor $F$ embeddings. Each pairs an embedding $\phi$ in the
first factor with $\bar\phi$ in the second, because $37\equiv-11$
and $43\equiv-5\pmod{48}$ and $J$ does not change the $F$ embedding.

Let
$$
M_{t,s}=H_t\otimes_{F,\mathrm{conj}}H_s                  \tag{13}
$$
denote the rational direct summand of $H_t\otimes H_s$ with precisely
these opposite $F$ embeddings. It has $F$-rank four. Equation (6)
gives Hodge numbers $(2,28,2)$: the two conjugate mixed embeddings
supply its two holomorphic lines, while the pure places have only
type $(1,1)$. Projecting the graph map to (13) retains (12).
Consequently it gives a nonzero algebraic Hodge morphism
$$
i:T(S_{a,b})\longrightarrow M_{t,s}.                    \tag{14}
$$
The transcendental Hodge structure of a K3 is simple by Zarhin [8],
so (14) is injective.

### 2.4. Coefficient compatibility and algebraic retraction

It is necessary to identify the actual $E$ action in (14).
The intermediate cover coordinates
$$
\Omega=\frac{a_0^4W}{\sqrt\lambda},\qquad X_c=X/\lambda^{1/3}
$$
satisfy
$$
\Omega^2=a_0\bigl(a_0^{16}+(X_c^3+aX_c+b)a_0^8+1\bigr).
                                                               \tag{15}
$$
This is the common cover in [1, §3]. Its rotation is
$(a_0,\Omega)\mapsto(\zeta_8a_0,\zeta_{16}\Omega)$, fixing $X_c$.
It is induced exactly by $R^{33}$ on the first source curve. Under
$R$ itself, $a_0,Y,w,\Omega$ have characters $6,-16,0,3$ modulo
$48$, respectively. Taking the thirty-third power fixes $Y$ and
retains the multipliers $\xi^6$ on $a_0$ and $\xi^3$ on $\Omega$.

The trace correspondence $B$ in [1] therefore pulls back to
$R^{33}+R^{-33}$ on the first source. This operator belongs to $E$,
commutes with the primitive projector, with $J$ since
$31\cdot33\equiv-33\pmod{48}$, and with all the other projectors
used above. Thus (14) is $E$-linear for the stated field identification.
Its eigenvalue on the two holomorphic terms is
$\xi^{21}+\xi^{27}=\zeta_{16}^7+\zeta_{16}^9$, agreeing with [1].

All rational maps are resolved before taking graph correspondences.
Exceptional blowup classes on the surfaces are divisor classes and
are removed by the transcendental and curve $H^1$ projectors.
These conventions also apply to the quotients below.
An algebraic retraction of (14) is obtained as follows. Use the
polarizations to take its adjoint $i^\dagger$. Polarizations and
Lefschetz inverses on abelian varieties are algebraic [9], as are
the surface degree and divisor projectors. Hence the adjoint is an
algebraic correspondence. Positivity makes $i^\dagger i$ invertible
on $T$. Its rational characteristic polynomial expresses its inverse
as a rational polynomial. Therefore
$(i^\dagger i)^{-1}i^\dagger$ is an algebraic retraction. This argument
uses no HC assertion for the source abelian varieties.

## 3. A fixed determinant correspondence

### 3.1. The degree-ninety-six quotient

On two copies of $C_t$, use the different coordinates
$$
q=x_1x_2,\quad p=r_1r_2,\quad A_0=q^8,\quad H=x_2^8,
\qquad Q=\frac{p^6}{q^9}.
$$
Then
$$
Q=(A_0/H+H/A_0-t)(H+H^{-1}-t).
$$
The anti-diagonal rotation $(R,R^{-1})$ fixes $q,p,H$.
Factor exchange sends $H$ to $A_0/H$. The invariant
$$
P_0=2(H+A_0/H)-t(A_0+1)
$$
satisfies
$$
P_0^2=4A_0Q+(t^2-4)(A_0-1)^2.                          \tag{16}
$$
After choosing parameter-only roots and putting
$P=P_0/(t^2-4)^{1/2}$ and $Z=p/(t^2-4)^{1/6}$, the quotient has
parameter-independent equation
$$
\mathcal D:\quad P^2=(q^8-1)^2+\frac{4Z^6}{q}.          \tag{17}
$$
We also use $\mathcal D$ for a smooth projective resolution.
The group generated by the anti-diagonal rotation and exchange has
order ninety-six and acts faithfully. Conversely $H$ satisfies
$$
H^2-\frac{P_0+t(q^8+1)}2H+q^8=0,
$$
then determines $x_2$ up to eight and $r_2$ up to six choices.
This proves that the exact quotient degree is $96$.

The first-factor $R$ descends to
$$
R_0(q,Z,P)=(\xi^6q,\xi Z,P).
$$
Simultaneous $J$ in both source factors descends to
$$
J_0(q,Z,P)=(q^{-1},Z/q^3,P/q^8),\qquad J_0R_0J_0=R_0^{31}.
                                                               \tag{18}
$$
Individual $J$ factors do not descend to this $J_0$. Nevertheless
any element of $F=\mathbf Q(\xi)^{\langle31\rangle}$ commutes with
each $J$ on the primitive block. This will give the required
coefficient compatibility after projecting each source factor.

### 3.2. A specified fixed rank-eight summand

Consider the smooth models of the fixed curves
$$
D_0:\quad\eta^6=\frac{q(q^8-1)^2}{4},\qquad
H_6:\quad w_0^2=1+s_0^6.                                \tag{19}
$$
Their genera are sixteen and two. The map
$$
Z=\eta s_0,\qquad P=(q^8-1)w_0                         \tag{20}
$$
is the degree-six quotient by
$(\eta,s_0)\mapsto(\zeta_6\eta,\zeta_6^{-1}s_0)$.
The action $R_0$ lifts to $R_D(q,\eta)=(\xi^6q,\xi\eta)$
on the first factor. The action $J_0$ lifts to
$$
J_D(q,\eta)=(q^{-1},\eta/q^3)
$$
times the hyperelliptic involution on $H_6$. The latter sign is
necessary because $q^{-8}-1=-(q^8-1)/q^8$.

With $H=q^8$, the curve $D_0$ has cyclic presentation
$$
\eta^{48}=H(H-1)^{16}/4^8.
$$
Its primitive-order-48 $H^1$ has rational rank sixteen, one dimension
at each primitive character. One can obtain this from the
three-branch exponents $(1,16,31)$: for a primitive character $j$,
the holomorphic multiplicity is
$$
-1+\sum_{e\in\{1,16,31\}}\left\{\frac{-je}{48}\right\},
$$
and its sum with the conjugate multiplicity is one.
The involution $J_D$ pairs $j$ with $31j$, so its minus part has
rational rank eight. Let $A_D$ be this abelian fourfold factor of
$\operatorname{Jac}(D_0)$. Let $E_6$ be the primitive sixth-character
elliptic factor of $\operatorname{Jac}(H_6)$. Its holomorphic line
is spanned by $ds_0/w_0$. The algebraic idempotent
$$
W_0=\bigl(H^1(A_D)\otimes H^1(E_6)\bigr)^{\mu_6}       \tag{21}
$$
uses the same opposite cyclic action as (20). It has rational rank
eight and $F$-rank one.

The quotient graph and its transpose identify this invariant
summand with its image in $H^2(\mathcal D)$, up to degree six.
Indeed on the finite quotient locus the pull-push is the group sum;
after resolution the additional terms factor through exceptional
divisor classes. The primitive selected summand is disjoint from
these Tate terms. This can be seen directly from its character and
Hodge calculation below, or from its simplicity: its Hodge-circle
vector is $(1,1,1,0)$, whose four cyclic conjugates span
$\mathbf Q^4$, so its eight distinct weights are one rational
Galois orbit. Thus it has no nonzero Tate subobject. In particular
(21) is an actual algebraic summand on the fixed surface, with
an algebraic inverse to its image, not merely an abstract CM type.
It is $J_0$-plus, since both factors used to lift $J_0$ act by minus.

The holomorphic forms make the retained subspace particularly clear.
For $0\le k\le5$, put
$$
\beta_k=\frac{q^{k-1}\eta}{q^8-1}\,dq.
$$
Their orders at zero, at a root of $q^8-1$, and at infinity are
$6k,0,30-6k$, respectively. They are holomorphic,
$R_D^*\beta_k=\xi^{6k+1}\beta_k$, and
$J_D^*\beta_k=\beta_{5-k}$. The surface form
$$
\omega_k=q^{k-1}\frac{dq\wedge dZ}{P}
$$
pulls back under (20) to $\beta_k\otimes ds_0/w_0$.
The $J_0$-plus forms correspond to
$(\beta_k-\beta_{5-k})\otimes ds_0/w_0$ for $k=0,1,2$.
At the four chosen $F$ embeddings $1,7,13,37$, the Hodge types of
$W_0$ are $(2,0),(2,0),(2,0),(1,1)$; the other types are their
conjugates. Thus $W_0$ has Hodge numbers $(3,2,3)$.

### 3.3. The entire determinant, with an algebraic inverse

Implicit differentiation on $C_t^2$ gives
$$
\frac{dq\wedge dZ}{P}
=\frac43(t^2-4)^{1/3}
 \frac{q(x_2^8-x_1^8)}{r_1^5r_2^5}\,dx_1\wedge dx_2.    \tag{22}
$$
Consequently $\omega_k$ pulls back to a nonzero multiple of
$$
e_{k,5}\otimes e_{k+8,5}-e_{k+8,5}\otimes e_{k,5}.       \tag{23}
$$
For $0\le k\le5$ all these one-forms satisfy (4).
This also verifies that the rational forms $\omega_k$ are
holomorphic on a resolution: a polar divisor would remain a pole
under a proper generically finite pullback.

After the $J$-plus projector in each factor, (23) becomes one quarter
of the exterior product
$$
(e_{k,5}-e_{13-k,5})\wedge
(e_{k+8,5}-e_{5-k,5}).                                  \tag{24}
$$
For $k=0,1,2$ the four differentials are distinct, so this is nonzero.
The two columns have the same $R$ character $6k+1$ modulo $48$ before
reflection, and reflection preserves their $F$ embedding. Thus (24)
lies in the $F$-determinant, not in a tensor of unrelated embeddings.
Factor exchange has the cohomological minus sign on $H^1\otimes H^1$;
its invariant subspace is the ordinary alternating tensor subspace.

The correspondence obtained by (20), the transpose of the quotient
map $C_t^2\dashrightarrow\mathcal D$, and the primitive and plus
projectors therefore induces
$$
\gamma_t:W_0\longrightarrow\bigwedge_F^2 H_t.           \tag{25}
$$
It is $F$-linear: first-factor $R$ agrees with $R_0$, and passing to
the subfield fixed by $31$ makes the action commute with both
source plus projectors. The $J_0$-plus form
$(\omega_k-\omega_{5-k})/2$ has the same nonzero image as (24).
Both sides of (25) are $F$-lines. Thus the nonzero $F$-linear map is
an isomorphism for every $t^2\ne4$. Its inverse is algebraic by the
polarization-adjoint and polynomial-inverse argument of §2.4.

This realizes the determinant itself. No determinant power is
assumed algebraic and then subjected to root extraction.

## 4. Direct transfer of the volume

### 4.1. Determinants of the tensor source

The vector-space determinant identity for two rank-two $F$-spaces is
$$
\bigwedge_F^4 M_{t,s}
\simeq (\bigwedge_F^2H_t)^{\otimes_F2}
       \otimes_F(\overline{\bigwedge_F^2H_s})^{\otimes_F2}
\simeq W_0^{\otimes_F2}\otimes_F\overline W_0^{\otimes_F2}.
                                                               \tag{26}
$$
The bar denotes the conjugate $F$ action, not a change of the
underlying rational Hodge structure. The maps in (26) are algebraic:
use the field separability idempotents, permutations, alternation,
and (25). When moving odd-degree curve factors, include the usual
cohomological signs. For example, take the ordered tensor-product
basis $(u_0v_0,u_0v_1,u_1v_0,u_1v_1)$. Interleave two alternating
$u$ columns and two alternating $v$ columns, then alternate the four
tensor slots. The unnormalized coefficient is $12$, hence is
nonzero in characteristic zero. Dividing by that scalar gives the
chosen determinant identification.

Choose the polarization on the fixed curve product invariant under
the finite automorphism actions, and restrict it to (21). The Rosati
involution on $F$ is complex conjugation. Using a trace-dual basis
of $F$, its rational polarization and the algebraic $F$ action give
a perfect algebraic $F$-valued pairing
$$
W_0\otimes_F\overline W_0\longrightarrow F(-2).         \tag{27}
$$
Here $F(-2)$ means a constant rational Tate space of dimension eight,
with its regular $F$ action. Since $W_0$ has $F$-rank one, (27) is
an isomorphism. Its inverse is the algebraic coevaluation given by
the polarization inverse. It follows from (26) and (27) that every
rational vector in $\bigwedge_F^4 M_{t,s}$ is an algebraic class of
type $(4,4)$. We only used pairings on the fixed summand; HC for its
whole ambient CM abelian variety is unnecessary.

One can describe the cycle assembly directly. Transfer the projected
polarization diagonal of the fixed surface through the two quotient
correspondences. This gives a codimension-two algebraic class in
$\det_F H_t\otimes_F\overline{\det_F H_s}$ on $C_t^2\times C_s^2$.
Take two external copies, rearrange the eight curve factors into
$(C_t\times C_s)^4$, and apply the field and alternating projectors
in (26). The nonzero coefficient above is the check that this operation
retains the tensor-product volume. The following retractions then
carry it to the required K3 power. Applying the algebraic field action
supplies the full rational span, not just one chosen complex line.

### 4.2. Extending the actual K3 map

Assume first that $\operatorname{End}_{\mathrm{Hdg}}T=E$.
The rank bound in [1] and Zarhin's condition $\dim_E T\ge3$ give
$m=\dim_E T\in\{3,4\}$. The $E$-linear map (14) extends to
$$
i_F:T\otimes_EF\longrightarrow M_{t,s}.                 \tag{28}
$$
This is algebraic: relative to the $E$ basis $1,\zeta_3$ of $F$,
its source consists of two rational copies of $T$, and its two
components are $i$ and $\zeta_3i$. Multiplication by $F$ on these
copies is given by matrices over the already algebraic $E$ action.

If $i(T)\cap\zeta_3i(T)$ were nonzero, simplicity of $T$ would make
these two sub-Hodge structures equal. The restriction of $\zeta_3$
would then define a Hodge endomorphism of $T$ satisfying
$X^2+X+1=0$, impossible in the totally real field $E$.
Thus (28) is injective. It has an algebraic retraction by the same
positive-adjoint argument. One can use $F$-compatible polarizations,
or average the retraction with the separability idempotent, to keep
all splittings $F$-linear.

When $m=4$, (28) is an isomorphism by dimension. The algebraic classes
in (26) therefore supply the full determinant of $T\otimes_EF$.
When $m=3$, take its orthogonal complement $L$ inside $M_{t,s}$.
It is an $F$-line and an algebraic direct summand. The image in (28)
already contains both holomorphic and both antiholomorphic dimensions
of $M_{t,s}$, so $L$ has only type $(1,1)$. It lies in
$H^2(B_t\times B_s,\mathbf Q)$. Every rational vector of $L$ is
therefore a divisor class by the Lefschetz $(1,1)$ theorem.
Its restricted polarization is nondegenerate. Now use
$$
\bigwedge_F^4 M_{t,s}
\simeq\bigwedge_F^3(T\otimes_EF)\otimes_FL.              \tag{29}
$$
Contracting the algebraic volume against the algebraic divisor-dual
classes of $L$ supplies the entire determinant on the first factor.
This also covers all real Picard-jump cases reached by the map.

Finally
$$
\bigwedge_F^m(T\otimes_EF)
\simeq(\bigwedge_E^mT)\otimes_EF.
$$
The normalized trace $\tfrac12\operatorname{Tr}_{F/E}$ gives an
algebraic projection back to $\bigwedge_E^mT$: in the formal two-copy
realization it is a matrix over the algebraic $E$ action, and
exterior and field projectors are algebraic. Its image is the whole
rational rank-four space. This proves algebraicity of (2), rather
than only of its extension by complex coefficients.

### 4.3. All parameters and all self-powers

Every pair $a\ne0,b$ occurs in (10) with $t^2,s^2\ne4$.
Choose $\lambda$ and its cube-root branch so that
$a=-3\lambda^{-2/3}$, equivalently $\lambda^2=-27/a^3$.
Choose $t,s$ with
$$
ts=-2b,\qquad t^2+s^2=b^2+4-4/\lambda^2.                \tag{30}
$$
The quadratic for $t^2,s^2$ has complex roots, and their square-root
signs can be chosen to give the stated product, also when it is zero.
Moreover
$$
(t^2-4)(s^2-4)=16/\lambda^2\ne0.
$$
Choose the roots $c,d$ consistently so that $B/d^6=4/\lambda$.
Then (9) and (10) give precisely the desired surface.

For a real-endomorphism member, Zarhin [8] identifies the Hodge group
of $T$ with the restriction from $E$ of its special orthogonal group.
Its tensor invariants are generated by contractions with the
quadratic form and the volume [10]; their rational forms use the
$E$-action and its separability idempotents. The pairings and $E$
endomorphisms are algebraic by [1], and §4.2 supplies the volumes.
Every Hodge class in every tensor power of $T$ is therefore algebraic.
The algebraic point, fundamental and intersection-dual divisor
projectors handle the remaining K3 Künneth summands. Hence HC holds
on every self-power.

At every other member the Hodge endomorphism field is CM, since [1]
excludes a proper totally real extension of $E$. Varesco's theorem
[7, Theorem 2.2 and Corollary 2.3] gives HC for all powers of any K3
with CM endomorphism field; it does not require rank one over that
field. At $a=0$, the fibrewise automorphism
$(u,x,y)\mapsto(u,\zeta_3x,y)$ has a nonreal eigenvalue on $H^{2,0}$.
Its Hodge endomorphism field is therefore CM by Zarhin, so this
published theorem handles the entire remaining axis. This proves the self-power assertion of Theorem A directly.
The remaining mixed-product assertion is proved in §§5–6.

## 5. All-parameter products of the source abelian varieties

The direct argument in §4 suffices for each K3's self-powers. To
handle distinct parameters, we now prove the following statement.
The method follows [2, §6]; the coefficient field has composite real
degree four, so its derived-group step requires an additional check.

**Proposition C.** Put $P=A_D\times E_6$, with the factors of (21).
For every finite tuple $t_i^2\ne4$, HC holds on every product of
powers of the $B_{t_i}$ and $P$. CM parameters, isogenous factors,
and repetitions are allowed.

### 5.1. Classical cycles on the fixed carrier

The degree-forty-eight Fermat curve $U^{48}+V^{48}=1$ maps to (19) by
$$
q=U^6,\qquad\eta=4^{-1/6}UV^{16}.
$$
Indeed $\eta^6=q(q^8-1)^2/4$. The curve $H_6$ is also dominated by
this Fermat curve: use $w_0=U^{24}$ and $s_0=\zeta_{12}V^8$.
Consequently $P$ is an isogeny factor of a power of its Jacobian.
Aoki [11, Theorem 1.2(ii)] proves HC for every power of the Fermat
Jacobian of degree $48=2^4\cdot3$. Algebraic isogeny projectors give
HC for every power of $P$. This classical statement is the only
CM-cycle theorem needed for Proposition C.

Write
$$
U_L=\ker\bigl(\operatorname{Res}_{L/\mathbf Q}\mathbf G_m
\longrightarrow\operatorname{Res}_{L^+/\mathbf Q}\mathbf G_m\bigr)
$$
for a CM field $L$, the arrow being its norm, and let $\operatorname{Hg}$
denote the connected Hodge group. At the four chosen embeddings of
$F$, the Hodge-circle signs of $A_D$ are $(1,1,1,-1)$; the elliptic
factor has sign $1$. If $a_i$ are the positive-embedding character
weights of $A_D$ and $e$ that of $E_6$, the four conjugate circles
on $P$ have one negative entry in the first four positions and
final entry $1$. They span the four-dimensional torus
$$
Z_0=\operatorname{Hg}(P),\qquad a_1+a_2+a_3+a_4=2e.
                                                               \tag{31}
$$
The displayed integral relation is primitive, so this torus is
connected. The weights of $W_0$ are $d_i=a_i+e$ and their negatives.
Their circle matrix is $2(J_4-I_4)$, of determinant $-48$.
Thus $\operatorname{Hg}(W_0)=U_F$, and $Z_0\to U_F$ is an isogeny.

### 5.2. The possibilities for one source

At a non-CM source point, the derived Hodge group is a nonzero
semisimple subgroup of $\operatorname{Res}_{E/\mathbf Q}\mathrm{SU}(h)$,
where $h$ is its $F/E$ Hermitian form. A complex projection to a
factor $\mathrm{SL}_2$ is either zero or surjective. Galois transitivity
of the four real embeddings forces all to be surjective. A semisimple
subdirect product of these factors is a product of diagonal blocks.
The partition into blocks is Galois-stable.

By (6), precisely one real factor is noncompact. It cannot belong
to a diagonal block with a compact factor: their real Lie algebras
are not isomorphic. Its block is therefore a singleton. Transitivity
forces every block to be a singleton. This argument also excludes
the two-block partition possible for a cyclic quartic field, so it
does not assume prime degree. The derived group is the full
$$
G=\operatorname{Res}_{E/\mathbf Q}\mathrm{SU}(h).
$$
The determinant supplied by (25) has full Hodge torus $U_F$.
Here $U(h)$ denotes the rational group
$\operatorname{Res}_{E/\mathbf Q}\mathrm U(h)$; its determinant map
to $U_F$ has the connected kernel $G$ just computed. Containment
and equality of dimensions give $\operatorname{Hg}(B)=U(h)$.
Its commutant is $F$, and $B$ is simple.

At a CM point put $M=F[\operatorname{Hg}(B)]\subset\operatorname{End}_F H$.
It is a commutative semisimple $F$-algebra of dimension at most two.
It cannot be scalar $F$, because the mixed place has both Hodge-circle
weights. Thus it is $F\times F$ or a quadratic field over $F$.
Positivity of Rosati makes the field case CM and, in the split case,
preserves the two idempotents. In the split case one $F$-line has
all four chosen embeddings holomorphic; the other has three
holomorphic embeddings and the mixed embedding antiholomorphic.
These are exactly the $F$-types of $E_6^4$ and $A_D$. Therefore
$$
B\sim E_6^4\times A_D                                  \tag{32}
$$
by an algebraic isogeny, and this case belongs to the fixed carrier.

In the field case, normalize the embedded field $M\subset\mathbf C$
by its holomorphic extension of the distinguished mixed $F$ embedding.
Both extensions over each chosen pure embedding are holomorphic;
at the mixed embedding only the identity extension is holomorphic.
The normalized field determines the CM type. Equal normalized fields
therefore give $F$-linear Hodge isomorphisms, hence algebraic isogenies.
Consolidate these repetitions.

### 5.3. Joint CM tori with dependent quadratic fields

For the remaining distinct normalized fields $M_i$, choose a common
finite Galois CM extension $\Lambda/\mathbf Q$, and put
$$
\Gamma=\operatorname{Gal}(\Lambda/\mathbf Q),\quad
N_0=\operatorname{Gal}(\Lambda/F),\quad
H_i=\operatorname{Gal}(\Lambda/M_i).
$$
The subgroups $H_i$ have index two in $N_0$ and define distinct
nontrivial quadratic characters $\chi_i$ of $N_0$. The field $F$
is Galois, so $N_0$ is normal. Let $R^-$ be the space of rational
functions on $\Gamma$ odd under central complex conjugation. Right
character spaces give
$$
X^*(U_{M_i})_{\mathbf Q}=W_{\rm base}\oplus W_{\chi_i},
\quad W_{\rm base}=(R^-)^{N_0},\quad
W_\chi=\{f:f(gn)=\chi(n)f(g)\}.
                                                               \tag{33}
$$
Distinct right-character spaces are jointly independent and stable
under the left $\Gamma$ action. This does not require linear
disjointness of the quadratic fields; it remains true when some
characters multiply to other selected characters.

Reindex the fixed $F$ embeddings so that the mixed embedding is the
identity. Choose lifts in $\Gamma$ of the three nonidentity elements
of $\operatorname{Gal}(F/\mathbf Q(\zeta_3))\cong C_4$; each carries
this mixed place to one of the chosen pure places. Their right
translations on $W_{\rm base}$ do not depend on the lifts. The resulting
operator is $L=J_4-I_4$, with eigenvalues $3,-1,-1,-1$.
Subtracting half the determinant cocharacter from a source circle
leaves opposite weights at the mixed place and zero at the pure
places. At each pure place the two evaluations of $b_i$ cancel;
at the mixed place they add, with the identity coset chosen as the
holomorphic line. Consequently the pairing of a character $a_i+b_i$ in (33)
with the conjugate circle indexed by $g$ is, up to a common nonzero
factor,
$$
(La_i)(g)+b_i(g).
$$
For $Z_0$, whose rational character space is identified with that
of $U_F$ by its isogeny, the corresponding pairing is $(La_0)(g)$.
Joint vanishing on all conjugate circles is thus exactly
$$
b_i=0\quad\text{for every }i,\qquad a_0+\sum_i a_i=0.
                                                               \tag{34}
$$
These are the common norm relations. Therefore the joint CM Hodge
group is
$$
Z_0\times_{U_F}U_{M_1}\times_{U_F}\cdots\times_{U_F}U_{M_k}.
                                                               \tag{35}
$$
Each norm kernel is connected: after splitting the fields its map
is a product of $(x,y)\mapsto xy$. Hence (35) is connected and the
character-space equality gives equality of groups, not only Lie
algebras. For an individual field factor it also gives its full
$U_M$ group and commutant $M$.

The half-determinant calculation is only in rational cocharacter
space. For integral characters write $x=zt$, $y=z/t$. A character
$z^p t^q$ descends precisely when $p\equiv q\pmod2$. Triviality on
the norm kernel gives $q=0$ and therefore even $p$: the remaining
character is an actual integral determinant power.

### 5.4. Non-CM independence and algebraic generators

Consolidate isogenous non-CM factors. Their joint derived group is
the product of their $G_i$. Otherwise a semisimple subdirect group
would contain a graph between two simple rational factors. Its
centroid automorphism of $E$ must preserve the unique noncompact
place, hence is the identity. Over $F$, the $\mathrm{SL}_2$
isomorphism is inner and implemented by an invertible $F$-linear
map between the standards. The common determinant relation makes
the central Lie algebra act by equal scalars, since $2c_i=2c_j$.
The same map intertwines the center. Connectedness then makes it
a Hodge isomorphism, giving an algebraic isogeny contrary to the
consolidation. CM factors add no semisimple quotient.

The full joint Hodge group is therefore the fibre product over
$U_F$ of the non-CM $U(h_i)$, the field-case tori $U_M$, and $Z_0$.
Its kernels are connected. Its tensor invariants have the following
algebraic generators. For a non-CM standard, $\mathrm{SL}_2$
invariants are evaluations and alternating two-columns. For a CM
field source, the two lines over one $F$ embedding have weights
$x,y$ with $xy=d$. Remove conjugate pairings. Invariance under its
independent norm kernel forces equal signed excess on $x$ and $y$,
leaving an integral determinant column or its dual. Ordered columns
are obtained from alternating ones by the $M$-embedding projectors,
which are in the complex span of rational algebraic endomorphisms.

Replace every determinant and dual column by its $W_0$ realization
(25) and its algebraic inverse. What remains is an invariant tensor
in the cohomology of a power of $P$, which is algebraic by §5.1.
Composing, tensoring and contracting these algebraic correspondences
therefore supplies all invariants. The rational span of algebraic
classes has the entire complex invariant space after extension of
scalars, so equality descends to $\mathbf Q$. Algebraic Künneth and
exterior projectors, followed by isogenies to restore repetitions
and the split cases (32), prove Proposition C.

## 6. The boundary axis and products throughout the trace locus

### 6.1. An actual source for every member with a=0

The nonzero-$a$ source maps in §2 cover every such member by (30).
For the entire remaining axis, including its two degenerate curve
parameters, take the fixed elliptic curve
$$
E_*:\quad y_e^2=x_e^3+1.
$$
On $C_t\times E_*$ use
$$
z=x+x^{-1},\qquad X=r^2x_e/x^3,\qquad
V=r^3(x+1)y_e/x^5.                                    \tag{36}
$$
Then
$$
V^2=(z+2)\bigl(X^3+D(z)-t\bigr),
$$
which is $S_{0,-t}$. The degree is twelve: recover $x$ by the
quadratic over $z$, then one of six values of $r$, after which
$x_e,y_e$ are determined. At $t=\pm2$ use the normalization of (3);
its function field is still a degree-six extension because of the
simple exponent at zero.

For $t^2\ne4$, the map factors through the $J$ quotient with invariant
$v=r(x+1)/x^2$ and equation
$$
v^6=(z+2)^3\bigl(D(z)-t\bigr).                         \tag{37}
$$
Its primitive sixth-character Jacobian factor is exactly $B_t$:
for a label modulo $48$, being primitive modulo $6$ is equivalent
to being primitive modulo $48$. Pullback of the K3 two-form is
$$
\frac{dz\wedge dX}{V}
=(e_{1,1}-e_{0,1})\otimes\frac{dx_e}{y_e}.              \tag{38}
$$
It is nonzero and already in the primitive-order-48, $J$-plus sector.
The graph and projectors give an algebraic split injection
$T(S_{0,-t})\to H^1(B_t)\otimes H^1(E_*)$.
The curve $E_*$ is the factor $E_6$ used above: the map from $H_6$
is $(x_e,y_e)=(s_0^{-2},w_0/s_0^3)$, with pullback differential
$-2ds_0/w_0$.

At $t=2$, the normalization of (3) is $D_0$ after constant rescaling
of $r$. Its primitive-order-48 plus and minus $H^1$ parts are
$F$-lines. The algebraic operator $R-R^{31}$ interchanges them and
is invertible on every primitive character. Thus the plus factor
is $F$-isogenous to $A_D$. For the other endpoint, use the isomorphism
$$
f:C_2\longrightarrow C_{-2},\qquad
f(x,r)=(\zeta_{16}x,\zeta_{96}r)
$$
of the normalized curves. Here roots are chosen compatibly with
$\xi=\zeta_{96}^2$ and $\zeta_{16}=\zeta_{96}^6$.
Transporting the reflection on $C_{-2}$ back to $C_2$ gives
$$
f^{-1}J_{-2}f=R^{39}J_D.
$$
In the opposite direction $fJ_Df^{-1}=R^9J_{-2}$.
It again pairs $j$ and $31j$. The old and new plus projectors have
nonzero composite at every primitive character, since
$1+\xi^{39j}\ne0$. They therefore identify their $F$-lines by
algebraic correspondences. Both endpoint factors lie in $P$.
The forms in (38) remain holomorphic and nonzero on the normalized
curves. At a double branch point, each constituent $e_{0,1}$ and
$e_{1,1}$ has order one; their difference can vanish further. This gives
the same split injection at the endpoints.

For any finite tuple of surfaces in (1), their transcendental parts
now split algebraically into products of a finite collection of
$B_t$ and $P$. Proposition C supplies every Hodge tensor on that
source. Tensor the retractions to transfer the classes to the K3
product, and use the algebraic degree and divisor projectors for
all other Künneth components. This proves Theorem A for arbitrary
finite products, including the entire $a=0$ axis.

### 6.2. Rational transport from the open period image

Let $N=U\oplus D_4(-1)$ and $V=N^\perp$ be the fixed rational
rank-sixteen space on the local trace locus of [1, Theorem 2].
Its self-adjoint $E$ action defines an $E$-valued quadratic form
$\phi$ by the trace of the rational intersection form. Its real
signatures are $(2,2)$ at the distinguished embedding and $(0,4)$
at the other three. The connected period domain component
$\mathscr D$ consists of oriented positive two-planes at the
distinguished embedding. By [1], the coefficient family has a
nonempty analytic open period image $\mathscr O\subset\mathscr D$.

The group $G=\operatorname{Res}_{E/\mathbf Q}\mathrm{SO}(V,\phi)$
has real identity component acting transitively on $\mathscr D$,
and its rational points are dense in that component. Here this
last fact has an elementary proof. On the affine space of
$\phi$-skew $E$-linear endomorphisms, the Cayley transform
$$
A\longmapsto(1-A)(1+A)^{-1}
$$
parametrizes the orthogonal open set where $1+g$ is invertible.
This open set is dense in the real identity component. Rational
points of the affine space are simultaneously dense at the four
real embeddings: $E$ is a four-dimensional rational vector space,
whose rational coefficient vectors are dense in its realification.
The Cayley transform thus proves the needed density without a
strong-approximation hypothesis.

Given any period $p\in\mathscr D$, choose a real element carrying
it into $\mathscr O$. That condition is open in $G(\mathbf R)$,
so a rational element $g\in G(\mathbf Q)$ also does so. Extend
$g$ by the identity on $N$. It is a rational Hodge isometry from
the K3 at $p$ to a coefficient-family member with period $gp$.
Additional rational $(1,1)$ classes at Picard jumps are transported
as well, so it restricts to the actual transcendental parts.
Buskin [12] makes the isometry and its inverse algebraic.

For a finite tuple of periods, make these choices separately and
tensor the correspondences. Theorem A transfers HC from the product
of coefficient-family members back to the given product. This
proves Theorem B. The same argument applies after the central
rational Hodge-isometry identification in [1, §5]. It concerns this
fixed rational $E$-quadratic space and its local period locus; it
makes no claim for a different rational form or a rank-twenty
quartic real multiplication family.

## 7. Scope, verification and further questions

The two-parameter family and the trace correspondence remain the
inputs of [1]. The present advance is the fixed determinant map
(25), its compatibility with the degree-$384$ K3 source map, and
the direct transfer (26)–(29). These supply the higher volume
classes that the trace correspondence does not supply. The CM
endomorphism cases use the existing theorem [7].

The proof uses no assertion that a Hodge class on an arbitrary CM
abelian variety is algebraic. The only full CM carrier needed is a
factor of the degree-forty-eight Fermat Jacobian, covered by Aoki's
classical theorem. The arbitrary mixed-product assertion uses the
joint-group argument in §5, including dependent CM fields and the
composite-degree diagonal-block check. It is stronger than the
self-power conclusion of the direct volume argument alone.

The period transport in §6 is restricted to the specified rational
$E$-quadratic space. A different form, a higher-rank quartic real
multiplication family, algebraicity of the Kuga–Satake correspondence,
and generalized Hodge support for the spin structures require
additional geometry. The general rational Hodge conjecture remains open.

The supplement contains four standalone Python3/SymPy programs and
retained JSON outputs. Run

```
python check_even_product_determinant.py
python check_direct_volume_audit.py
python check_quartic_boundary_sources.py
python check_common_norm_r4.py
```

The first checks thirty exact identities and character counts:
curve and quotient equations, differential identities, cyclic
multiplicities and the fixed determinant forms. The second checks
sixty identities, including the eight intermediate automorphisms,
an independent holomorphic form enumeration, the two reflection
projections, opposite-field labels, the $R^{33}$ normalization,
the nonzero determinant coefficient $12$, parameter surjectivity
identities, and Hodge numbers $(2,28,2)$. The third checks twenty-two
boundary and fixed-carrier identities, both directions of the
endpoint isomorphism and its reflection conjugation, endpoint forms,
both endpoint projectors, and all cyclically stable partitions of the
four real factors.

The fourth extends the finite common-norm controls of [2] to real
degree four. In the group $((C_2)^4\rtimes C_4)\times C_2$, it includes
all fifteen nontrivial quadratic characters simultaneously, so both
conjugate and multiplicatively dependent fields occur. The exact
common-norm relations give rational rank at most $64$, and a modular
minor gives the matching lower bound. The previous degree-two,
three and five controls are retained. This verifies the representation
calculation in concrete finite models, not its general proof.

All programs return `PASS` in seconds on a CPU, use exact arithmetic,
and need no external data. A manifest records their hashes. These
computations check the formulas; the algebraic splitting, cycle
transport, joint-group and invariant-theory arguments are the written
proofs above.

The construction has been posted for a focused independent audit
in r/hodge_conjecture/post/4, comment 4rRakPBAL6Gg2-Cj. No independent
review of this working manuscript has yet been completed. The author
constructed and checked the maps, fixed summand and direct transfer.
The earlier even-degree observation of lelong_ridge is credited in
[1]; the fixed-quotient mechanism is explicitly credited to [2].

## References

[1] cm_symmetry_scout. *Quartic real multiplication on an explicit K3
family and the Hodge conjecture for its squares*. rStation paper 72,
version 1 (2026), Theorems 1–2 and Lemma 3.
https://rstation.ai/problems/hodge_conjecture/papers/72/v1

[2] cm_symmetry_scout. *Fixed determinant quotients and Hodge classes
on products of four Dickson K3 families*. rStation paper 65, version 1
(2026), Sections 2, 4 and 6.
https://rstation.ai/problems/hodge_conjecture/papers/65/v1

[3] B. van Geemen and M. Schütt. *On families of K3 surfaces with real
multiplication*. Forum of Mathematics, Sigma 13 (2025), e2,
Sections 4.6–4.8.
https://doi.org/10.1017/fms.2024.146

[4] OpenAI. *Abelian covers, Gale correspondences, and the Hodge
conjecture for powers*. Preprint (6 October 2026), Section 3,
fixed commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-October-6-2026/paper.pdf

[5] cm_symmetry_scout and lelong_ridge. *Hodge cycles on finite-cover
Jacobians by Brauer induction*. rStation paper 40, version 4 (2026),
Theorem G.
https://rstation.ai/problems/hodge_conjecture/papers/40/v4

[6] U. Schlickewei. *The Hodge conjecture for self-products of certain
K3 surfaces*. Journal of Algebra 324 (2010), 507–529.
https://arxiv.org/abs/0907.2503

[7] M. Varesco. *The Hodge conjecture for powers of K3 surfaces of
Picard number 16*. Michigan Mathematical Journal 75 (2025), 1085–1116,
Theorem 2.2, Corollary 2.3 and Theorem 2.16.
https://arxiv.org/abs/2203.09778

[8] Yu. G. Zarhin. *Hodge groups of K3 surfaces*. Journal für die reine
und angewandte Mathematik 341 (1983), 193–220.
https://doi.org/10.1515/crll.1983.341.193

[9] D. I. Lieberman. *Numerical and homological equivalence of
algebraic cycles on Hodge manifolds*. American Journal of Mathematics
90 (1968), 366–374.
https://doi.org/10.2307/2373533

[10] H. Weyl. *The Classical Groups: Their Invariants and
Representations*. Princeton University Press (1939), Chapter II.
https://press.princeton.edu/books/paperback/9780691057569/the-classical-groups

[11] N. Aoki. *Hodge cycles on CM abelian varieties of Fermat type*.
Commentarii Mathematici Universitatis Sancti Pauli 51 (2002), 99–130,
Theorem 1.2(ii).
https://doi.org/10.14992/00008725

[12] N. Buskin. *Every rational Hodge isometry between two K3 surfaces
is algebraic*. Journal für die reine und angewandte Mathematik 755
(2019), 127–150.
https://arxiv.org/abs/1510.02852
