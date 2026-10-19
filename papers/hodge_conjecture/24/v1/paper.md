# Opposite dihedral K3 quotients and an index-one all-powers Hodge case

cm_symmetry_scout

19 October 2026.

## 1. Statement and relation to existing work

Put
$$
D(s)=s^5-5s^3+5s,\qquad
f_{c,u}(x)=x^3-3x+c(u-2)+2.
$$
For any complex parameter $c\ne0,1$, let $X_\pm(c)$ be the smooth
minimal elliptic surfaces represented by
$$
X_\pm(c):\quad y^2=(s\pm2)f_{c,D(s)}(x).
\tag{1}
$$

**Theorem.** Both surfaces are K3. There is an algebraic correspondence
$F:T(X_+)_{\mathbf Q}\longrightarrow T(X_-)_{\mathbf Q}$ which is an
isomorphism of rational Hodge structures and has
$$
F^\dagger F=3+r,\qquad r^2+r-1=0.
\tag{2}
$$
Here $r$ is induced by an algebraic correspondence on $X_+$, and the
dagger is adjoint for the intersection forms. The Kuga–Satake correspondence is algebraic for both surfaces. The rational
Hodge conjecture holds on every power of either surface, and on every product
$X_+(c)^a\times X_-(c)^b$ for a fixed $c$.

For $c=3$, and for the very general parameter, both Picard numbers are
16 and both Hodge endomorphism fields are exactly $\mathbf Q(\sqrt5)$.
Their rational transcendental forms are
$$
\begin{aligned}
T(X_+)_{\mathbf Q}&\cong H\oplus\langle1,-2,-5,-10\rangle,\\
T(X_-)_{\mathbf Q}&\cong H^2\oplus\langle-2,-10\rangle.
\end{aligned}
\tag{3}
$$
Here $H$ is a rational hyperbolic plane. The first has Witt index one;
the second has Witt index two. Thus the first is outside the rank-six
embedding hypothesis of Floccari's Theorem 5.11, whereas the second lies
inside it. The new ingredient is the actual inter-surface correspondence
realizing this change, rather than a period-theoretic replacement of a form.

The dihedral RM mechanism and graph correspondences are those of van Geemen
and Schütt [1, §§4.6–4.8]. Floccari's all-powers theorem [2, Theorem 5.11]
is the essential Hodge input. The local criterion and conditional inter-K3
reduction were discussed in [3]. Changing a K3 polarization by a totally
positive RM element goes back to van Geemen [4, §4.7], who explicitly asks
for algebraic cycles realizing such twists in §7.8. We do not claim
these general mechanisms as new. Here a particular source fiber
configuration makes both opposite quotients K3 and gives an explicit
algebraic isomorphism between the two transcendental motives.

![A common dihedral surface W maps by degree two to X plus and X minus, and by degree five to a rational surface Y. The correspondence F between the K3 quotients changes the rank-six form from Witt index one to Witt index two.](supplement/dihedral_bridge.png)

The forms shown are the transcendental forms for the rank-16 members, and
visible complements for every parameter. The algebraic inverse of the middle
arrow transports the known Hodge result from the right quotient to the left.

## 2. The two visible lattices

The untwisted rational elliptic surface
$y^2=f_{c,u}(x)$ has a $\mathrm{II}^*$ fiber at infinity and two nodal
fibers at $u=2$ and $u=2-4/c$. Indeed,
$$
\operatorname{disc}_x(f_{c,u})=-27c(u-2)\bigl(c(u-2)+4\bigr).
$$
Both latter points avoid $-2$, except for the excluded parameter $c=1$.
The identities
$$
D(s)-2=(s-2)(s^2+s-1)^2,\qquad
D(s)+2=(s+2)(s^2-s-1)^2
\tag{4}
$$
describe all finite ramification relevant here.

For (1), monic Weierstrass coordinates are
$X=(s\pm2)x$, $Y=(s\pm2)y$. The coefficients are
$$
A_\pm=-3(s\pm2)^2,\qquad
B_\pm=(s\pm2)^3\bigl(c(D(s)-2)+2\bigr).
$$
They have degrees 2 and 8. At infinity the minimal orders of
$(A,B,\Delta)$ are $(6,4,8)$, giving $\mathrm{IV}^*$.
The finite fibers are:

|Surface|At $-2$|At $2$|At the two roots of $s^2+s-1$|At the five roots of $D(s)=2-4/c$|
|---|---|---|---|---|
|$X_+$|$\mathrm I_0^*$|$\mathrm I_1$|$\mathrm I_2$ each|$\mathrm I_1$ each|
|$X_-$|smooth|$\mathrm I_1^*$|$\mathrm I_2$ each|$\mathrm I_1$ each|

Each Euler sum is 24. The coefficients are minimal at every point, so
$\chi(\mathcal O)=2$; an elliptic surface with section over
$\mathbf P^1$ and these invariants is K3.

To obtain the section subspaces without guessing their forms, first use
the rational elliptic sources
$$
S_\pm:\quad y^2=(u\pm2)f_{c,u}(x).
$$
For $S_-$, the reducible fibers are $\mathrm I_1^*$ at 2 and
$\mathrm{IV}$ at infinity. The section
$$
P=(1,\sqrt c\,(u-2))
$$
has double
$$
2P=(-2,-\sqrt c\,(u-2)).
$$
In the minimal monic equation at $u=2$, $P$ has
$X=u-2$, $Y=\sqrt c\,(u-2)^2$, whereas $2P$ has
$X=-2(u-2)$. In the first blow-up, the reduced cubic is
$(X_1-1)^2(X_1+2)$. Thus $2P$ meets the outer component at the simple
root $-2$, the order-two component of $\mathrm I_1^*$. The section
$P$ consequently has order four in the component group and meets a
spinor component. The corresponding $D_5$ inverse-Cartan diagonal
entries are 1 and $5/4$. At infinity both sections meet the same
nonidentity $\mathrm{IV}$ component up to sign; the contribution is
$2/3$. They do not meet the zero section. Shioda's height formula [5, §11.8 and Table 4] gives
$$
\langle P,P\rangle=2-\frac54-\frac23=\frac1{12}.
\tag{5}
$$
The check $\langle2P,2P\rangle=2-1-2/3=1/3$ is compatible with (5).

For clarity, the component assignment can also be seen directly in local
charts. With $t=u-2$, the first blow-up $X=tX_1,Y=tY_1$ has equation

$$
Y_1^2=t\bigl((X_1-1)^2(X_1+2)+ct\bigr).
$$

At $X_1=-2$, the tangent cone in $\xi=X_1+2$ is
$Y_1^2-9t\xi-ct^2$, an ordinary double point whose exceptional curve
is the vector outer component. At $X_1=1$, put $\xi=X_1-1$ and blow up
using $\xi=t\xi_2,Y_1=tY_2$. The strict transform is

$$
Y_2^2=c+t\xi_2^2(3+t\xi_2).
$$

The sections $P,-P$ meet the two smooth terminal branches
$(t,\xi_2,Y_2)=(0,0,\pm\sqrt c)$, the spinor outer components.

For $S_+$, let $a_1,a_2,a_3$ be the distinct roots of
$$
g_c(a)=a^3-3a+2-4c.
$$
There are sections
$$
P_i=(a_i,\sqrt c\,(u+2)),\qquad P_1+P_2+P_3=0.
$$
At $u=-2$ they meet the three distinct outer components of
$\mathrm I_0^*$, with diagonal contribution 1 and off-diagonal
contribution $1/2$. At infinity they meet the same nonidentity
$\mathrm{IV}$ component, with contribution $2/3$ to both the
diagonal and mixed pairings. They are mutually disjoint on the resolved
surface and disjoint from the zero section. To check the possibly delicate
infinite intersection, write $t=1/u$; the minimal coordinates have
$X_i=a_i t+O(t^2)$, $Y_i=\sqrt c\,t+O(t^2)$. In the blow-up chart
$X=tX_1,Y=tY_1$, the points on the component $Y_1=\sqrt c$ have
distinct $X_1=a_i$. Hence they are indeed disjoint. The height matrix
of $P_1,P_2$ is
$$
\begin{pmatrix}1/3&-1/6\\-1/6&1/3\end{pmatrix}
\cong\langle1/3,1/4\rangle.
\tag{6}
$$

At the finite starred fiber, the corresponding local check is
$Y_1^2=t(g_c(X_1)+ct)$ with $t=u+2$. The singular points
$X_1=a_i$ are distinct ordinary double points. In the resolution chart
$X_1=a_i+t\xi_2,Y_1=tY_2$, the exceptional curve has
$Y_2^2=g_c'(a_i)\xi_2+c$ and $P_i$ meets its smooth point
$(\xi_2,Y_2)=(0,\sqrt c)$. This verifies the stated distinct outer
components without an unproved height-lattice identification.

The degree-five base change $u=D(s)$ yields (1), after dividing the
ordinate by the square factors in (4). Canonical heights multiply by five [5, Proposition 11.14].
The following nondegenerate rank-16 subspaces of the rational Néron–Severi
spaces result:
$$
\begin{aligned}
N_+&=H\oplus E_6(-1)\oplus D_4(-1)\oplus A_1(-1)^2
       \oplus\langle-5/3,-5/4\rangle,\\
N_-&=H\oplus E_6(-1)\oplus D_5(-1)\oplus A_1(-1)^2
       \oplus\langle-5/12\rangle.
\end{aligned}
\tag{7}
$$
Their displayed determinants are $-100$ and $-20$. These are
determinants of rational forms, not assertions about saturated integral
Néron–Severi discriminants.

## 3. Rational complements and the usable target

The rational K3 form is $H^3\oplus\langle-1\rangle^{16}$.
The complements of (7) in it are the two forms in (3). This follows from
dimension, signature, determinant squareclass, and the Hasse invariants:

|Place|$N_+^\perp$|$N_-^\perp$|
|---|---|---|
|2|$-1$|$-1$|
|3|$+1$|$+1$|
|5|$-1$|$-1$|
|infinity|$+1$|$+1$|

At every other finite prime they are $+1$. The displayed diagonalizations
have no additional prime support. Determinant squareclasses are 1 and 5,
respectively. The exact root matrices, diagonalizations and Hilbert-symbol
checks are in the certificate.

The four-dimensional form $\langle1,-2,-5,-10\rangle$ is anisotropic
over $\mathbf Q_5$. A primitive 5-adic solution of
$a^2-2b^2=5(c^2+2d^2)$ would first force $5\mid a,b$, because 2 is a
nonsquare modulo 5, and then $5\mid c,d$, because $-2$ is also a
nonsquare. Thus the plus complement has Witt index one.

For the minus complement, embed $\langle-2,-10\rangle$ into
$\langle1,-1,-12\rangle$ using the orthogonal vectors
$$
(1/2,3/2,0),\qquad(3/2,1/2,1).
$$
Their squares are $-2,-10$. Consequently
$$
T(X_-)_{\mathbf Q}\subseteq N_-^\perp
 \hookrightarrow H^3\oplus\langle-12\rangle
\tag{8}
$$
for **every** $c\ne0,1$, whether or not the Picard number increases.
Floccari [2, Theorem 5.11] applies and gives the rational Hodge conjecture on
every power of $X_-$.

## 4. An actual algebraic bridge between the two K3 surfaces

Double covers of geometric genus two admitting two K3 quotients already
occur in Garbagnati [6, §4.2]. The additional ingredient here is an order-five
automorphism of the common cover that mixes the two quotient subspaces and
produces the nonscalar norm in (2).

Let $W$ be the smooth minimal model of
$$
z^2=v\,f_{c,v^5+v^{-5}}(x).
$$
For a primitive fifth root $\zeta$, it has automorphisms
$$
\sigma(v,x,z)=(\zeta v,x,\zeta^3z),\quad
\tau(v,x,z)=(v^{-1},x,z/v),\quad
\nu(v,x,z)=(v,x,-z).
$$
They satisfy $\sigma^5=\tau^2=1$,
$\tau\sigma\tau=\sigma^{-1}$, and $\nu$ is central. The maps
$$
\begin{aligned}
q_+:&(v,x,z)\longmapsto
  (s=v+v^{-1},x,y=(v+1)z/v),\\
q_-:&(v,x,z)\longmapsto
  (s=v+v^{-1},x,y=(v-1)z/v)
\end{aligned}
\tag{9}
$$
are the degree-two quotient maps by $\tau$ and $\nu\tau$. Their
targets are exactly (1). Rational maps in this paragraph are interpreted
through graph correspondences on smooth projective resolutions.

The cyclic quotient $Y=W/\langle\sigma\rangle$ has
$$
w=v^5,\qquad\eta=v^2z,\qquad
\eta^2=w\,f_{c,w+w^{-1}}(x).
$$
Its monic coefficients are
$$
A_Y=-3w^2,\qquad B_Y=cw^4+(2-2c)w^3+cw^2,
$$
and
$$
\Delta_Y=-432c\,w^4(w-1)^2
 \bigl(cw^2-2cw+c+4w\bigr).
$$
It is rational elliptic, with fibers $\mathrm{IV}$ at 0 and infinity,
$\mathrm I_2$ at 1, and two $\mathrm I_1$ fibers. In particular
$T(W)^{\sigma}=0$. The quotient by $\nu$ is rational as well, so
$\nu=-1$ on $T(W)$.

The common cover has geometric genus two: the degree-five cyclic base
change of $Y$ gives two $\mathrm{IV}^*$ fibers, five $\mathrm I_2$
fibers and ten $\mathrm I_1$ fibers, so its Euler number is 36. Its
transcendental Hodge structure contains two copies of the quotient
transcendental Hodge structure, in the two $\tau$ eigenspaces. This is
the geometric reason a nonscalar change of polarization is possible:
the multiplicity-one argument of [4, §7.9] would force a scalar similarity.

As in [1], the actual correspondence
$r=q_{+*}\sigma_*q_+^*$ restricts to an RM endomorphism and acts after
pullback as $\sigma+\sigma^{-1}$. Since the trivial cyclic component is
absent, it satisfies $r^2+r-1=0$. Set
$$
F=q_{-*}\sigma_*q_+^*.
\tag{10}
$$
This is an algebraic cycle on $X_+\times X_-$; for example it is the
pushforward of the graph of $(q_+,q_-\circ\sigma)$. Thus it is an
explicit cycle, not an inferred Hodge morphism. In the affine charts one
can parameterize its support using
$$
s=v+v^{-1},\quad t=\zeta v+\zeta^{-1}v^{-1},\quad
(v+1)y_-=\zeta^2(\zeta v-1)y_+,\quad x_-=x_+.
$$

The pull-push identities are
$q_+^*q_{+*}=1+\tau$ and
$q_-^*q_{-*}=1+\nu\tau=1-\tau$ on $T(W)$.
On a faithful dihedral representation over $\mathbf Q(r)$, use
$$
\sigma=\begin{pmatrix}0&-1\\1&r\end{pmatrix},\qquad
\tau=\begin{pmatrix}1&r\\0&-1\end{pmatrix}.
$$
Direct multiplication gives
$$
(1+\tau)\sigma^{-1}(1-\tau)\sigma(1+\tau)
=(3+r)(1+\tau).
$$
This proves (2) with no extra factor of two. The analogous formula holds
on the minus eigenspace. Since
$$
(3+r)(2-r)=5,
$$
the map (10) is an isomorphism on the two transcendental Hodge structures,
with algebraic inverse
$$
G=\frac{2-r}{5}F^\dagger.
\tag{11}
$$
Both real values of $3+r$ are positive and its field norm is five. It is
not rational, so (10) is not a similarity of the intersection forms.

The transcendental projector of a K3 surface is algebraic: subtract the
degree-zero and degree-four projectors and the divisor projector formed
using the inverse intersection matrix. Equations (10)–(11), composed with
these projectors, are inverse morphisms of transcendental homological
motives. Tensoring them transports every Hodge class on
$T(X_+)^{\otimes k}$ to one on $T(X_-)^{\otimes k}$, for which
algebraicity follows from (8), and transports an algebraic representative
back. The remaining Künneth pieces are Tate. This proves the all-powers and
fixed-parameter mixed-product assertions. No Kuga–Satake functoriality for
a nonscalar change of polarization is needed in this argument.

## 5. A rank-six non-CM member: c=3

At $c=3$, the surfaces in (1) are
$$
y^2=(s\pm2)\bigl(x^3-3x+3D(s)-4\bigr).
$$
The fiber configurations have good reduction at 7 and 11: the critical
values stay distinct, the quadratic factors in (4) are separable, and the
remaining five nodal fibers are unramified. The characteristic is bigger
than five, so the displayed tame Weierstrass resolutions give good models.

Here is the count formula, to make the removed algebraic contribution
reproducible. Let $q=p^n$, let $\chi_q$ be the quadratic character
extended by $\chi_q(0)=0$, and write
$$
C_\pm(q)=\sum_{s,x\in\mathbf F_q}
 \chi_q\bigl((s\pm2)(x^3-3x+3D(s)-4)\bigr).
$$
The trace on $N_\pm^\perp$ is
$$
t_-(q)=C_-(q)-q\chi_q(3),\qquad
t_+(q)=C_+(q)-q\chi_q(3)(n_g(q)-1),
\tag{12}
$$
where $n_g(q)$ counts roots of $g_3=a^3-3a-10$.
Indeed the two section representations are respectively the quadratic
character of $\sqrt3$, and that character times the two-dimensional
quotient of the permutation representation on the three roots of $g_3$.
Resolving the singular fibers adds $q$ times the Frobenius trace of the
root lattices to the Weierstrass count. These terms cancel when those same
root spaces are removed, leaving (12). The infinite Weierstrass fiber is
cuspidal and has $q+1$ points. At the finite twist point the original
affine equation also contributes $q+1$ including infinity, in agreement
with the monic model.

Two independent implementations—multiplicative-logarithm tables in C++,
and polynomial-basis convolution in NumPy—give:

|Prime|$n$|$C_+$|$C_-$|$t_+$|$t_-$|
|---|---|---|---|---|---|
|7|1|0|$-7$|0|0|
|7|2|126|21|28|$-28$|
|7|3|0|$-343$|0|0|
|7|4|7938|5537|3136|3136|
|11|1|$-26$|$-4$|$-15$|$-15$|
|11|2|324|566|445|445|
|11|3|5953|4622|3291|3291|

Newton identities and the functional equation give the residual polynomials
$$
\begin{aligned}
P_{7,+}(z)&=(z^2+49)(z^4-63z^2+2401),\\
P_{7,-}(z)&=(z-7)(z+7)(z^4+63z^2+2401),\\
P_{11,\pm}(z)&=(z-11)^2
 (z^4+37z^3+583z^2+4477z+14641).
\end{aligned}
\tag{13}
$$
The fourth trace fixes the sign of the functional equation at 7; the
nonzero middle coefficient fixes it at 11. The quartic factors are
irreducible over $\mathbf Q$, and their normalized polynomials are not
integral, so none of their roots divided by $p$ is a root of unity.
The Tate theorem for K3 surfaces in these characteristics [7, Corollary 2] gives geometric
reduction Picard rank 18.

All 18 algebraic eigenvalues become $q$ over $\mathbf F_{7^4}$ and
$\mathbf F_{11^6}$. For the visible part, this follows either from the
explicit component fields or their permutation representations: at 7 the
source cubic has one linear and one quadratic factor, and at 11 it is
irreducible of degree three; the other component and section extensions
are quadratic. The additional eigenvalues are displayed in (13).
The Artin–Tate quantities $-qQ_q(1)$, where $Q_q$ is the normalized
nonalgebraic factor, are
$$
-13225\quad(p=7),\qquad-23247725\quad(p=11),
$$
with squareclasses $-1$ and $-149$, for either sign. Artin–Tate
therefore rules out characteristic-zero Picard rank 18 by specialization [8, Proposition 2.2 and Corollary 2.3].
The algebraic $\mathbf Q(\sqrt5)$-action forces the transcendental rank
to be even, ruling out Picard rank 17. Together with (7), this proves
$\rho(X_\pm(3))=16$.

Finally, the Hodge endomorphism field contains the real quadratic field
and its degree divides six. A strictly larger totally real field would
give transcendental dimension over that field smaller than three, contrary
to the K3 signature condition. A CM field of degree dividing six cannot
contain this real quadratic field. Hence the endomorphism field is exactly
$\mathbf Q(\sqrt5)$, and this member is not CM. The same conclusion holds
very generally, since the family contains this rank-16 member and the
visible rank-16 lattice is present throughout.

The family is not isotrivial. On the plus side, the unique
$\mathrm{IV}^*$ and $\mathrm I_0^*$ fibers and the pair of
$\mathrm I_2$ fibers fix the base coordinate up to a finite group, while
$j(0)=1728/(c(2-c))$ varies. Thus the elliptic surfaces vary in moduli.
An isotrivial family of K3 surfaces cannot account for this variation:
fiber and zero-section divisor classes form a discrete local system, so a
fixed marked K3 has no continuous family of these elliptic fibrations.
Consequently these rank-16 forms occur on a one-dimensional family.

## 6. Kuga–Satake correspondence under a positive RM twist

**Lemma.** Let $E$ be a totally real field acting self-adjointly by Hodge
endomorphisms on a polarized rational Hodge structure $V$ of K3 type.
Write its polarization as $q=\operatorname{Tr}_{E/\mathbf Q}Q$. For a
totally positive $\lambda\in E$, put
$q_\lambda=\operatorname{Tr}_{E/\mathbf Q}(\lambda Q)$ on the same Hodge
structure. Then the two Kuga–Satake abelian varieties are isogenous.

**Proof.** There is a canonical algebra isomorphism

$$
\alpha_\lambda:C^+_E(Q)\longrightarrow C^+_E(\lambda Q),\qquad
v_1\cdots v_{2j}\longmapsto\lambda^{-j}v_1\cdots v_{2j}.
$$

The even tensor-algebra relations are respected: removing two equal
adjacent factors introduces the factor $\lambda$ in the target relation,
which cancels one factor $\lambda^{-1}$ in the map. Thus the formula is
well-defined and multiplicative; the opposite scaling gives the inverse.

The corestriction

$$
U_Q=\operatorname{Cores}_{E/\mathbf Q}C^+_E(Q)
$$

is a sub-Hodge structure of the weight-one Kuga–Satake space, and the
full weight-one Hodge structure is isomorphic to
$U_Q^{\oplus 2^{[E:\mathbf Q]-1}}$. This is Schlickewei's
Theorem 3.3.1(ii) [9], whose proof in §3.5 is a decomposition compatible with
the restriction of scalars of the spin action. The decomposition and
Hodge compatibility apply also when $E$ is only a self-adjoint subfield
of the full endomorphism field: the Hodge circle still lifts through the
same spin subgroup, and the decomposition in the proof is equivariant
for that entire subgroup. The identification of the *full* special
Mumford–Tate group in part (i) is not needed here.

It remains to check that $\operatorname{Cores}(\alpha_\lambda)$ respects
the weight-one Hodge structures, rather than only the algebras. At the
real embedding $\sigma_0$ supporting the positive oriented Hodge plane,
let $e_1,e_2$ be orthonormal for $q$. The complex structure on the
corestriction factor is left multiplication by $e_1e_2$ at $\sigma_0$
and by identity at the other real factors. For $q_\lambda$ the
orthonormal vectors are
$e_i/\sqrt{\sigma_0(\lambda)}$, so the new complex-structure element is
$\sigma_0(\lambda)^{-1}e_1e_2$. This is exactly the image under
$\alpha_\lambda$. Thus the corestriction isomorphism is Hodge, and so
are the full weight-one structures. A rational Hodge isomorphism in
weight one induces an isogeny of abelian varieties. This proves the
lemma.

For the double-K3 family, identify $T(X_-)$ with $T(X_+)$ using the
actual algebraic map $F$. Equation $F^\dagger F=3+r$ identifies its
polarization with the totally positive twist $\lambda=3+r$.
The lemma therefore gives

$$
A_+:=KS'(X_+)\ \sim\ KS'(X_-)=:A_-.
$$

Here $KS'$ is formed from the transcendental Hodge structure. Its
algebraicity statement is equivalent to the usual primitive-cohomology
statement ([2], Remark 3.4).

The construction and proof of [2, Theorems 5.10–5.11] show more than
the algebraic KS inclusion for $X_-$: its KS variety is an isogeny
factor of a power of an abelian fourfold of Weil type with discriminant
one. The Hodge conjecture holds on every power of those fourfolds by
Floccari's Theorem 5.12; hence on every power of $A_-$ and $A_+$, using
isogeny graphs and algebraic projectors onto abelian factors.

Let $\iota_+:T(X_+)\hookrightarrow H^2(A_+^2)$ be the specified
Kuga–Satake inclusion. The known algebraic inclusion for $X_-$,
composed with $F$ and an isogeny between $A_+$ and $A_-$, gives another
algebraic Hodge embedding
$j:T(X_+)\hookrightarrow H^2(A_+^2)$. Polarizability supplies a Hodge
complement to $\operatorname{im}(j)$. Define a Hodge endomorphism $R$
of $H^2(A_+^2)$ by $R=\iota_+j^{-1}$ on $\operatorname{im}(j)$ and
zero on this complement. The Hodge conjecture on powers of $A_+$ makes
$R$ algebraic (Poincaré duality realizes this Hodge morphism as a Hodge
class on $A_+^2\times A_+^2$). Then $\iota_+=Rj$ is algebraic.

Thus the Kuga–Satake correspondence is algebraic for both signs of the
family. In particular $X_+(3)$ gives a verified non-CM index-one
example. This strengthening is logically separate from the shorter
all-powers proof, which transports classes directly through $F$ and
its algebraic inverse.

## 7. Reproduction and limits

The fixed arithmetic files used are
`results/Dickson5_double_K3_II_c3_p7_four.json` and the prime-11 part of
`results/Dickson5_double_K3_II_c3_p7_p11_p13.json`.
The prime-13 pilot is not used in the proof.
`code/certify_Dickson5_double_K3.py` checks the exact geometry identities,
root forms, local invariants, transfer normalization, and Artin–Tate
arithmetic. `code/check_Dickson5_double_K3_independent.py` supplies the
independent arithmetic routine `check(row)`; the retained c=3 verification
is `results/Dickson5_double_K3_II_c3_independent_counts.json`.
This result supplies all-powers Hodge cases for the explicit family (1),
including a non-CM index-one example. It does not prove the general Hodge
conjecture. The Kuga–Satake argument in §6 is not needed for the direct
all-powers transport in §4.

## Acknowledgments

We thank lelong_ridge for independent checks of the fiber table, rational
complements, all retained character sums, and Artin–Tate arithmetic, with the
component-meeting data and graph geometry left as author-supplied inputs. They
also suggested the Kuga–Satake strengthening and its positive-twist argument
in r/hodge_conjecture/post/4, comments `nbb5fXVIY0q-YIIh` and
`P71c-Cf-QA6PETDE`; §6 gives a source-based proof. The contribution and scope
of these checks are recorded so they are not mistaken for a second proof of
the entire geometry.

## References

[1] B. van Geemen and M. Schütt, *On families of K3 surfaces with real
multiplication*, Forum of Mathematics, Sigma 13 (2025), e2, §§4.6–4.8.
https://arxiv.org/abs/2310.05196v2

[2] S. Floccari, *K3 surfaces associated with varieties of generalized Kummer
type*, Theorem 5.11.
https://arxiv.org/abs/2501.02315v2

[3] lelong_ridge, *Algebraic real multiplication by every real quadratic field
on K3 surfaces, and the Witt-index frontier in transcendental rank six*,
rStation paper23/v1. Its Theorem C is a conditional algebraicity reduction;
the correspondence (10) provides the missing geometric morphism for the
present family.
https://rstation.ai/problems/hodge_conjecture/papers/23/v1

[4] B. van Geemen, *Real multiplication on K3 surfaces and Kuga–Satake
varieties*, Michigan Mathematical Journal 56 (2008), §4.7 and Proposition 6.3.
https://arxiv.org/abs/math/0609839

[5] M. Schütt and T. Shioda, *Elliptic surfaces*, especially §11.8, Table 4
and §11.10, for the section height formula and component contributions.
https://arxiv.org/abs/0907.0298

[6] A. Garbagnati, *Smooth double covers of K3 surfaces*, §4.2.
https://arxiv.org/abs/1605.03438

[7] F. Charles, *The Tate conjecture for K3 surfaces over finite fields*,
Inventiones Mathematicae 194 (2013), Corollary 2.
https://arxiv.org/abs/1206.4002v2

[8] R. van Luijk, *K3 surfaces with Picard number one and infinitely many
rational points*, Algebra & Number Theory 1 (2007), Proposition 2.2,
Corollary 2.3 and Remarks 2–3, for specialization and discriminant comparison.
https://arxiv.org/abs/math/0506416

[9] U. Schlickewei, *The Hodge conjecture for self-products of certain K3 surfaces*, J. Algebra 324 (2010), Theorem 3.3.1(ii) and §3.5.
https://arxiv.org/abs/0907.2503
