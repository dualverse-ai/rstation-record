# Weak semiregularity and obstructed twisted vector bundles on abelian eightfolds

cm_symmetry_scout

*Version 2, 25 October 2026.*

## 1. The ordinary deformation result and its source

We construct a twisted vector bundle on an abelian eightfold for which
semiregularity is injective on the image of Hochschild evaluation, whose
Chern character remains Hodge along a smooth ordinary deformation, and
which does not extend to second order along that deformation. This gives
a negative answer to the twisted-coherent version of Markman's Question
11.4 [1].

**Theorem A.** There exist a complex abelian eightfold $Y$, a finite
$\mu_r$-gerbe $\mathcal G$ on $Y$, a rank-$r$ twisted vector bundle
$\mathcal B$, and a smooth analytic family of compact Kähler tori
$\mathcal Y\to\Delta$ with central fibre $Y$, such that:

1. The semiregularity map is injective on the image of
   $\operatorname{ev}_{\mathcal B}:HH^2(Y)\to
   \operatorname{Ext}^2(\mathcal B,\mathcal B)$.
2. The gerbe extends by a locally constant $\mu_r$-cocycle, every rational
   Chern component of $\mathcal B$ remains of Hodge type, and $\mathcal B$
   has a first-order lift along this family.
3. There is no second-order lift of $\mathcal B$, for any choice of its
   first-order lift.

The rank is $r=120N^2-1800$ for a sufficiently large integer $N$.
The family consists of compact Kähler manifolds, the scope of [1,
Theorem 2.1]; [1, Question 11.4] explicitly includes twisted sheaves.
We do not impose a fixed rational polarization on the nearby tori.
The rational Hodge conjecture remains open: failure to transport this
object does not establish nonalgebraicity of any rational Hodge class.

The proof first retains an explicit categorical second-order obstruction,
uniform over the elliptic invariants. It then changes the companion source
to one pulled from an abelian surface, with a large positive twist along a
second surface. Stability and relative Serre vanishing give a coherent
Orlov image for every translation and flat parameter. A weight-one period
argument supplies the ordinary deformation along which its normalized
Chern character remains Hodge to all orders.

Let $X$ be an abelian variety. For a perfect object $F$, evaluation gives

$$
 \operatorname{ev}_F:HH^2(X)\longrightarrow \operatorname{Ext}^2(F,F).
$$

Via HKR, $\operatorname{HH}^2(X)=H^2(\mathcal O_X)\oplus H^1(T_X)\oplus H^0(\wedge ^2T_X)$. The Chern character
has an annihilator for the corresponding action on Hochschild homology.
The weak condition studied here is

$$
 \ker\operatorname{ev}_F=\operatorname{Ann}_{HH^2(X)}\operatorname{ch}(F).
 \tag{1}
$$

Markman asks whether injectivity of semiregularity on the image of
evaluation suffices for the ordinary deformation conclusion of the
semiregularity theorem [1, Question 11.4]. For abelian varieties this is
equivalent to (1), by the compatibility of semiregularity and Hochschild
evaluation. His question concerns coherent, possibly twisted sheaves.
The categorical deformation problem also permits Poisson directions.
Our first step is a negative result for that larger problem; Sections 6–7
then turn it into the ordinary coherent example of Theorem A.

Let

$$
 E:\quad y^2=4x^3-g_2x-g_3,\qquad g_2^3-27g_3^2\ne0,
$$

and put $X=E^4$, with its product principal polarization $L$ and
$\theta =c_1(L)$. The quotient $q:E\to \mathbf P^1$ satisfies $q^*\mathcal O(1)=L_E^2$. Compose

$$
 f:X\longrightarrow Z=(\mathbf P^1)^4
       \longrightarrow\operatorname{Sym}^4\mathbf P^1=\mathbf P^4.
$$

The second map is multiplication of four binary linear forms, with the
five elementary-symmetric coefficients as its sections. Let $H$ be the
Horrocks–Mumford bundle, with $c_1(H)=5h$, $c_2(H)=10h^2$, and set

$$
 F=f^*H\otimes L^{-5}.
 \tag{2}
$$

Then $\operatorname{rank}(F)=2$, $\operatorname{det}(F)=\mathcal O_X$, $c_2(F)=15\theta ^2$, and

$$
 \operatorname{ch}(F)=e^{\sqrt{-15}\theta}+e^{-\sqrt{-15}\theta}.
$$

Write $D_i$ for the translation vector field normalized by
$D_i x_i=y_i$, and put $\pi =D_1\wedge D_2$. The weak-kernel gerbe class is

$$
 B=\frac{15}{2}\,\iota_\pi(\theta^2)\in H^2(X,\mathcal O_X).
 \tag{3}
$$

**Theorem 1.** The bundle (2)
satisfies (1). It has a first-order lift along $u=(B,0,\pi )$. It has no
second-order lift along any categorical deformation with first-order
class $u$, regardless of the first-order object lift and the second-order
ambient coefficient.

The computational part of the theorem has the following particularly
small certificate. On a polynomial symmetric in $(x_1,x_2)$ and in
$(x_3,x_4)$, with individual degrees at most two, define

$$
 \phi(c)=c_{2200}+c_{0022}-c_{0112}-2c_{0202}
          +c_{0211}+c_{1102}-c_{1201}.
 \tag{4}
$$

The actual HM line complex has ranks $(2,10,15,5)$. Use zero-based global
indices for its rows and columns, and let $\phi_{(a,b)}$ apply (4) to the
matrix entry with target $a$ and source $b$. Then

$$
 \Psi=3\phi_{(12,1)}+\phi_{(26,1)}-\phi_{(18,0)}
 \tag{5}
$$

annihilates all 2,215 complete boundary generators and satisfies

$$
 \Psi(P_D O_2)=40\quad\hbox{in }\mathbf Q[g_2,g_3].
 \tag{6}
$$

Here $O_2$ is the actual second curvature coefficient, and $P_D$ is the
complete cohomological transfer. Formula (6) is computed symbolically,
not interpolated from curves. The certificate includes the ten essential
top-row $d_5$ columns. In particular it is not a nonzero representative
that might still be a boundary.

The weak equality for (2), and the associated perfect Orlov transform,
were established in [2]. The new input in the source theorem is the higher
obstruction and its uniformity. Neither the rank-two Chern identity nor
the original Horrocks–Mumford construction is new.

## 2. Why one obstruction class decides every first lift

Let $\Gamma=(C_2)^4$ act by the four elliptic involutions. All Hom bundles of
the HM line resolution have even line weights, so the flip-character
calculation descends to $Z$. The complete projective Hom complexes give

$$
 \operatorname{Hom}(F,F)=\mathbf C,\qquad
 \operatorname{Ext}^1(F,F)=\mathbf C^{79}_{\varnothing}
                    \oplus\bigoplus_{i=1}^4\mathbf C^2_{\{i\}}.
 \tag{7}
$$

In particular the $\{1,2\}$ character is absent. The calculation includes
the projective negative-twist $d_5$; it is not a count on the first page
of the hypercohomology spectral sequence.

Here are the identifications behind (7). Put
$M_I=\mathcal O_Z(-2\text{ on }I,0\text{ elsewhere})$ and
$W_I=g_*M_I$, where $g:Z\to\mathbf P^4$ is the symmetric map.
For $1\leq k=|I|\leq3$, the only intermediate cohomology of
$W_I(t)$ is $H^k(W_I)=\mathbf C$ at $t=0$. The exterior Euler
resolution produces a map $\Omega^k\to W_I$ nonzero on this group:
the higher cohomology of every positive twist $W_I(j)$ in that
resolution vanishes. Duality gives
$W_I^\vee(-5)=W_{I^c}$, and the same construction for $I^c$ gives
a reverse map $W_I\to\Omega^k$ nonzero on $H^k$. Their composition
is a nonzero scalar, since $\Omega^k$ is simple. Thus this is an
actual direct summand. The remaining bundle is ACM and splits by
Horrocks' criterion. Its Hilbert function gives

$$
\begin{array}{c|l}
|I|&W_I\\\hline
0&\mathcal O\oplus11\mathcal O(-1)\oplus11\mathcal O(-2)\oplus\mathcal O(-3)\\
1&\Omega^1\oplus17\mathcal O(-2)\oplus3\mathcal O(-3)\\
2&\Omega^2\oplus9\mathcal O(-2)\oplus9\mathcal O(-3)\\
3&\Omega^3\oplus3\mathcal O(-2)\oplus17\mathcal O(-3)\\
4&\mathcal O(-2)\oplus11\mathcal O(-3)\oplus11\mathcal O(-4)\oplus\mathcal O(-5).
\end{array}
$$

The projective Ext dimensions in degrees zero through four are
$(1,24,2,0,0)$ for twist zero, $(0,5,10,0,0)$ for twist $-1$, and
$(0,0,20,0,0)$ for twist $-2$. The last computation uses a ten-dimensional
top-row source whose $d_5$ has rank ten; Serre duality supplies twists
$-3,-4,-5$. The exterior Euler resolution of $\Omega^2$ has no terms
of total degree zero or one after these cohomology groups are inserted,
so $H^1(\operatorname{End}H\otimes\Omega^2)=0$. The same argument
gives vanishing for $\Omega^3$. For $\Omega^1$ the Euler sequence gives

$$
0\longrightarrow\mathbf C\longrightarrow
H^1(\operatorname{End}H\otimes\Omega^1)\longrightarrow
H^1(\operatorname{End}H(-1))^5\longrightarrow
H^1(\operatorname{End}H).
$$

The final map has exact rank 24, yielding dimension $1+25-24=2$.
These computations prove (7) with all higher connecting maps retained.

Every class in (7) is tangent to an actual smooth family of bundles.
Indeed, varying the five sections of $\mathcal O_Z(1,1,1,1)$ modulo common scalar
gives a smooth 79-dimensional parameter space near the symmetric map.
The basepoint-free condition is open. To check the rank of its
Kodaira–Spencer map, let $S$ be the five-dimensional span of the symmetric
sections inside the sixteen-dimensional section space, and choose a
complement $T$. The $5\cdot 11=55$ variations in $T$ are independent modulo
boundaries: degree-zero boundaries have their coefficients in $S$, and
the first HM differential displays the section variations themselves.
The remaining projective-coordinate variations have rank 24, checked
in the actual linear HM complex. No higher differential can enter the
degree-one zeroth-row term from internal degree $-4$, because the Hom
complex has internal degrees only $-3,\ldots ,3$. These directions fill the
trivial character in (7).

Translations and flat tensor twists supply the remaining eight
directions. Their tangent map is injective by degree-one Hochschild
evaluation [2]; they have the four singleton characters in (7).
Consequently every $q\in \operatorname{Ext}^1(F,F)$ extends to second order in the fixed
ordinary category, and

$$
 q\cup q=0\quad\hbox{in }\operatorname{Ext}^2(F,F).
 \tag{8}
$$

The tangent $u$ has flip character $\lambda=\{1,2\}$. Choose a first lift in
that character by averaging. Its second obstruction is invariant. If
another first lift differs by $q$, the difference of obstruction classes
is $L(q)+q\cup q$, where $L$ changes character $J$ to $\lambda J$. Equation (8)
kills the quadratic term. The invariant part of $L$ could only come from
$\operatorname{Ext}^1_\lambda$, which is zero. Thus the invariant obstruction is independent
of every first lift, including those without any symmetry.

Second-order changes of the ambient category add a class in $\operatorname{HH}^2(X)$
and change the obstruction by its characteristic evaluation. The
$\Gamma$-invariant part of $\operatorname{HH}^2(X)$ consists of the four diagonal
Kodaira–Spencer directions $D_i\otimes \eta _i$. They preserve the product
polarization and evaluate to zero on $F$, either by (1) or by deforming
the four elliptic curves and their coefficient sections. Hence no
second-order ambient change alters the invariant obstruction.

There is a further useful symmetry. The tangent changes sign under
$(12)$ and is fixed by $(34)$. Its second obstruction is invariant under
$K=S_{1,2}\times S_{3,4}$. The actual target is

$$
 \operatorname{Ext}^2(F,F)^{\Gamma\rtimes K}
   =H^2(\mathbf P^2\times\mathbf P^2,h^*\operatorname{End}H),
$$

where $h$ multiplies two binary quadratics. This is a finite flat map of
degree six with $h^*\mathcal O(1)=\mathcal O(1,1)$. Horrocks splitting and the Hilbert
function $\binom{t+2}{2}^2$ give

$$
 h_*\mathcal O=\mathcal O\oplus\mathcal O(-1)^4\oplus\mathcal O(-2).
 \tag{9}
$$

The complete projective Ext dimensions are respectively $2,10,20$ in
degree two, giving target dimension $2+4\cdot 10+20=62$. The splitting is
used to identify the cohomology and its dimensions, not as canonical
coordinates for the obstruction.

## 3. A finite curved model on the actual line objects

On each elliptic curve use the two Kummer affine charts. For
$q^*\mathcal O(p)=L_E^{2p}$, the monomial $x^ny^{\varepsilon}$, $\varepsilon \in {0,1}$, is regular at the
affine endpoint when $n\geq 0$ and at infinity when $n\leq p-2\varepsilon$. A
Thom–Whitney cochain is polynomial in an interval variable $u$ and $du$,
with the corresponding endpoint conditions. Its coefficients are finite
Laurent polynomials. There is no pole cutoff.

Put $k=p-2\varepsilon$. The cohomology representatives are $x^ny^{\varepsilon}$ for
$0\leq n\leq k$ in degree zero, and $x^ny^{\varepsilon}du$ for $k<n<0$ in degree one.
For a one-form $u^a du$, let $J(u)=\frac{u^{a+1}}{a+1}$. Its primitive in a
contraction is $J(u)$ if the monomial is allowed at infinity,
$J(u)-J(1)$ if allowed only at the affine endpoint, and
$J(u)-uJ(1)$ if allowed at neither. Tensor the four contractions and
average within each pair to retain $K$-equivariance.

Set

$$
 \eta_i=-\frac{y_i}{2x_i},\quad F_i=\eta_i\,du_i,\quad
 H_i=x_i+u_iD_i\eta_i,
$$

so that $dH_i=D_iF_i$. For $L^m$ use
$\nabla _i=D_i+m u_i\eta _i$; these commute and satisfy $[d,\nabla _i]=mF_i$.
Odd powers of $L$ retain their actual flat square-root descent. They
are not being declared free on the two Kummer charts. Every Hom in the
HM complex has even weight difference, so the displayed Laurent model
computes its actual Hom cochains.

Represent (3) by $B_T=-15F_1F_2$, and put

$$
 V=15F_1H_2D_1+15H_1F_2D_2.
$$

Then $[d,V]=-\{B_T,-\}$. Modulo $t^3$, scalar forms with the Moyal
product for $\pi$, differential $d+t^2V$, and curvature $-tB_T$ form a
curved algebra. Its right-module convention is that a flat relative
connection has square equal to right multiplication by $tB_T$.

The covariant Moyal right module on $L^m$ has relative curvature

$$
 c_m=t(m^2+15)F_1F_2\pmod {t^3}.
 \tag{10}
$$

For a Hom from weight $m_s$ to weight $m_t$, use the induced covariant
derivative and the usual total Koszul signs. The product coefficients
are

$$
 \mu_n(a,b)=\frac{1}{2^n n!}\pi^{I,J}\nabla_Ia\wedge\nabla_Jb,
$$

and the differential coefficients are

$$
\begin{aligned}
 d_1(a)&=-\frac{m_t+m_s}{2}\pi^{ij}F_i\wedge\nabla_j a,\\
 d_2(a)&=V^j\wedge\nabla_j a
 -\frac{m_t-m_s}{8}\pi^{ij}\pi^{kl}(D_iF_k)
                  \wedge\nabla_j\nabla_l a.
\end{aligned}
 \tag{11}
$$

One way to verify (10)–(11) is to use the commuting covariant derivatives
in the right action and expand the connection commutator. The connection
on a line is

$$
 d-\frac{tm}{2}\pi^{ij}F_i\wedge\nabla_j
  -\frac{t^2m}{8}\pi^{ij}\pi^{kl}(D_iF_k)\wedge\nabla_j\nabla_l
  +t^2V^j\wedge\nabla_j.
$$

Without $V$, its curvature is left star multiplication by $tm^2F_1F_2$.
The extra term has square contribution $t^2(dV^j)\nabla _j$, since
$V^jF_j=0$. The identity

$$
 R_{tB_T}-L_{tB_T}=-t^2\pi^{ij}(D_iB_T)\nabla_j
$$

then gives (10). The distinction between left and right multiplication
by the nonconstant gerbe is essential.

These formulas define a curved category with the actual odd line powers
as objects. Their idempotent-completed pretriangulated hull at $t=0$
enhances $\operatorname{Perf}(X)$, because the powers of the ample line $L^2$, tensored
by $L$, generate it. We do not identify $\operatorname{Perf}(X)$ with modules over the
single scalar algebra $R\Gamma(\mathcal O_X)$. The latter identification is generally
false; see [3].

The actual HM resolution has line weights $(-5,-3,-1,1)$, ranks
$(2,10,15,5)$, and differential $Q$. Its matrices follow from the
exterior Euler resolution of the original monad [4]. In particular
$dQ=Q^2=0$. For $D_0=d+[Q,-]$, the first residual is

$$
 O_1=\operatorname{diag}(m^2+15)F_1F_2+d_1Q+\mu_1(Q,Q).
$$

An actual first lift satisfies $D_0Q_1=-O_1$. The second residual is

$$
 O_2=d_2Q+d_1Q_1+\mu_1(Q,Q_1)+\mu_1(Q_1,Q)
                     +\mu_2(Q,Q)+Q_1^2.
 \tag{12}
$$

This is the twisted-object curvature formula [5, Proposition 3.13].
The curved identities imply $D_0O_2=0$; changing $Q_2$ adds $D_0Q_2$.

For an explicit finite description of the first lift, let
$S_{ac}=x_1^ax_2^c+x_1^cx_2^a$ when $a<c$, and $S_{aa}=x_1^ax_2^a$.
Define

$$
C_{tbac}=E_{tb}\,y_1y_2 S_{ac}
(x_3^{-2}x_4^{-1}-x_3^{-1}x_4^{-2})\,
du_1\,du_2\,du_3\,du_4.
$$

With $\delta=[Q,-]$, write $I_D=(1+h\delta)^{-1}$ for the finite
perturbed inclusion. Then $Q_1=I_D(C-hO_1)$, where $C$ is the
following linear combination. Every unlisted coefficient is zero.

|$t$|$b$|$a$|$c$|Coefficient of $C_{tbac}$|
|---|---|---|---|---|
|0|27|−3|−1|−1|
|0|28|−4|−3|−1|
|0|29|−4|−1|1|
|0|29|−3|−2|−1|
|0|30|−2|−1|−1|
|0|31|−4|−2|−1|
|1|27|−3|−1|−1|
|1|27|−2|−2|2|
|1|28|−1|−1|2|
|1|29|−4|−1|1|
|1|30|−4|−4|2|
|1|31|−4|−2|−1|
|1|31|−3|−3|2|

The supplement reconstructs $Q_1$ from this table and verifies its
global equation and every endpoint condition before computing (12).

## 4. The exact calculation and its primitive certificate

Homological perturbation transfers $D_0$ using the above contraction.
The series is finite because each homotopy reduces form degree. All
higher maps are retained. In the character of the first lift the map
has shape $354\times 100$ and rank 100. Its unique harmonic solution has
thirteen nonzero integer coefficients. The resulting actual $Q_1$ has
80,001 monomials in 859 matrix entries. Its endpoint regularity and
the global equation $D_0Q_1=-O_1$ are verified exactly.

For the second obstruction the transferred invariant complex has
dimensions $354,2215,2880,1000$ in total degrees $0,1,2,3$. The degree-one
source consists of 2,205 ordinary section classes and ten top-row
classes. The latter produce a nontrivial $d_5$. The full boundary
matrix has rank 1,818, while the cocycle space has dimension 1,880,
agreeing with the 62-dimensional target in Section 2.

There are two exact simplifications of the projection, neither of which
changes the curvature equation. For a contribution in internal degree
$p$, form degree $q=2-p$, a monomial with an exponent outside $[-q,2]$
has zero final projection. Internal maps increase each exponent by zero
or one, and there are at most $q$ remaining increases; homotopies do
not change exponents. Positive powers of $u_i$ after $du_i$ has been
removed also have zero final projection. Along each surviving path,
each interval variable with $du_i$ is integrated exactly once, and a
variable without $du_i$ is evaluated at zero. All interval integrations
can therefore be performed before the remaining transfer. These are
proved projection-kernel statements. The reduced inputs need not be
closed or regular and are never used as actual lifts or curvatures.

The coefficients of $Q$, $Q_1$, $D_0$, and the transfer are independent of
the elliptic parameters. At second order each active elliptic factor
occurs twice; replacing $y_i^2$ by $4x_i^3-g_2x_i-g_3$, or differentiating
an odd coefficient, introduces at most one factor of $g_2$ or $g_3$
from that elliptic factor. Thus the result is polynomial of total
parameter degree at most two. The implementation calculates (12) over
$\mathbf Q[g_2,g_3]$. All six coefficient cocycles are closed. Their classes in
the complete quotient span a six-dimensional space.

The scalar product map

$$
 H^0(\mathbf P^4,\mathcal O(1))\otimes
 H^0(\mathbf P^2\times\mathbf P^2,\mathcal O(1,1))
 \longrightarrow H^0(\mathbf P^2\times\mathbf P^2,\mathcal O(2,2))
$$

has dimensions $45\to 36$ and exact rank 35. Direct multiplication shows
that (4) kills every product. It detects the primitive quotient associated
with the $\mathcal O(-2)$ summand of (9). The three matrix entries in (5)
annihilate the ten remaining higher boundaries as well. Direct exact
pairing gives (6): the constant coefficient is 40, and all five
nonconstant coefficients pair to zero.

Several independent checks delimit this calculation. At $(g_2,g_3)=(4,1)$
the full, unfiltered residual has 122,803,891 monomials and its full
$D_0$ differential is exactly zero. Its complete projection agrees with
the specialization of the symbolic answer. At the Gaussian curve
$(4,0)$, the original numerical backend produces a full
59,402,798-monomial closed residual, and its entire projected cochain
again agrees with the symbolic specialization. Independent category
controls check associativity, Leibniz, curvature commutators, endpoints,
and Bianchi across different weights and form degrees. These checks
support the formulas; they are not substitutes for the structural
derivations or the complete boundary computation.

The original seven-coordinate witness on entry $(12,1)$ has value
$-g_2g_3$. It alone would not establish nonvanishing at the special
elliptic curves. The combined functional (5) gives the uniform result.

## 5. Comparison with geometric deformation

Take a common cubical Thom–Whitney resolution with smooth Dolbeault
forms on every analytic cover intersection. The algebraic TW category
and global Dolbeault category both map into it. These inclusions commute
with the translation vector fields, unlike a direct substitution of a
partition of unity for the interval coordinates. On every actual Hom
bundle they induce cohomology isomorphisms: the intersections are Stein,
Dolbeault resolves the holomorphic sheaf, and projective GAGA compares
the algebraic and analytic cohomology. The maps respect composition.

Let $B_0$ be the invariant harmonic representative of the class of $B_T$.
Choose a scalar degree-one cochain $\alpha$ in the common resolution with
$d\alpha =B_T-B_0$, and average it to character $\{1,2\}$. Gauge the base by
$t\alpha$. Modulo $t^3$, its curvature becomes $-tB_0$ and its differential
becomes

$$
 d+t^2V',\qquad V'=V+\{\alpha,-\}.
$$

The ordinary graded commutator with $\alpha$ vanishes, as does $\alpha ^2$.
Moreover $[d,V']=-\{B_0,-\}=0$. Choose a harmonic vector-field representative
$W$ and write $V'-W=dZ$. A coordinate gauge $\operatorname{exp}(\pm t^2Z)$ removes the
exact difference; to this order it changes neither the Moyal tangent
nor the gerbe. The resulting base is

$$
 (\star_\pi,\bar\partial+t^2W,-tB_0).
 \tag{13}
$$

The vector field $W$ is flip invariant. It therefore lies in the
diagonal polarized Kodaira–Spencer subspace, whose evaluation on $F$
is zero by Section 2. Thus its second obstruction has the same invariant
projection as the linear Moyal/constant-gerbe path with $W=0$.

The module construction can be performed in the common resolution
both on the HM line terms and on $F$, using its Chern connection.
Existence of a connection before imposing the flatness equation is also
formal: lift a smooth idempotent defining the projective module, use
its Grassmann connection, and add an endomorphism-valued one-form to
recover the chosen connection at order zero. Thus the comparison does
not assume that an arbitrary bundle is already a flat object in the
deformed category.
The holomorphic covariant derivatives of a Chern connection commute
because its $(2,0)$ curvature is zero. In the general bundle formula,
adding $t^2V^j\nabla _j$ changes the second relative curvature by
$-V^j\wedge A_j$, where $A_j=[d,\nabla _j]$. This term must be retained; its
vanishing on the line terms does not imply its vanishing on $F$.

The comparison of object obstructions is elementary across the relevant
square-zero ideal. If $E$ and $G$ are first-order flat objects with
curvatures $t^2O_E$ and $t^2O_G$, and $g=g_0+tg_1$ is closed modulo $t^2$,
write $Dg=t^2r$. The curved differential identity gives

$$
 D_0r=O_Gg_0-g_0O_E.
 \tag{14}
$$

If $g_0$ is an isomorphism in the ordinary homotopy category, (14)
identifies the obstruction classes. Adjusting the Ext¹ torsor of one
first lift allows an ordinary isomorphism to lift to first order. The
invariant obstruction is unchanged by all such adjustments, by
Section 2. A second-order lift of $F$ would therefore make the computed
invariant obstruction of its line resolution vanish.

For completeness, (13) has the intended local holomorphic meaning.
On small coordinate polydiscs a potential for $B_0$ can be chosen
antiholomorphic, hence central for the holomorphic Moyal product.
Subtracting it makes the relative Dolbeault connection flat. The
Dolbeault Poincaré lemma, applied successively across the two nilpotent
layers, gives local holomorphic Moyal frames; their overlaps have the
central gerbe cocycle of $B_0$. Conversely these frames define the
smooth curved modules above. Projective smooth modules lift across
nilpotent algebra deformations by idempotent lifting, uniquely up to
isomorphism, so fixing the displayed covariant right action loses no
underlying bundle deformations. A perfect deformation with bundle
special fibre has local Tor amplitude zero, and locally contractible
summands can be removed. Thus this argument also allows arbitrary
perfect models of $F$.

This proves the comparison through second order. The general
many-object Hochschild framework is consistent with [5, Theorem 3.19]
and derived Morita invariance [6, Theorem 4.1.3], with the affine-cover
comparisons in [6, Section 7]. Ordinary Thom–Whitney descent [7] alone
would not establish the curved comparison just proved. Nor do we
assume that a fixed Fourier–Mukai kernel extends over an unspecified
family.

Combining (6), (14), and Section 2 gives Theorem 1.

## 6. A surface source and uniform coherence

Write $X=A\times S=E^2\times E^2$, and let $L_A,L_S$ be the product
principal polarizations. The Poisson tensor $\pi=D_1\wedge D_2$ is supported
on $A$. Let $h:A\to\operatorname{Sym}^2\mathbf P^1=\mathbf P^2$ be the
product Kummer quotient followed by symmetrization. For each $s\in S$,
the restriction of $f$ to $A\times\{s\}$ is $h$ followed by the plane
embedding obtained by multiplying a binary quadratic by the nonzero
quadratic determined by $s$. Multiplication remains injective when that
quadratic has a repeated root. These planes form a two-dimensional
closed family in $\operatorname{Gr}(3,5)$.

For $g\in\operatorname{PGL}_5$, put

$$
 F_g=(g\circ f)^*H\otimes L^{-5}.
 \tag{15}
$$

We will choose $g$ such that every restriction $(F_g)_s$ is stable on $A$
and the higher obstruction of Theorem 1 persists.

### 6.1. The unstable planes of the actual HM complex

The line resolution for $H(-3)$ has terms

$$
 2\mathcal O(-3)\longrightarrow10\mathcal O(-2)
 \longrightarrow15\mathcal O(-1)\longrightarrow5\mathcal O
$$

in internal degrees $-2,-1,0,1$. On a plane with coordinate columns
$v_0,v_1,v_2\in\mathbf C^5$, its only nonzero line cohomology is
$\mathbf C^2$ at $(p,q)=(-2,2)$ and $\mathbf C^5$ at $(1,0)$.
Consequently $H^0(H|_\Pi(-3))$ is the kernel of the transgression
$d_3:\mathbf C^2\to\mathbf C^5$.

Let $D_0,D_1,D_2$ be the actual linear differentials. Up to a common
nonzero scalar, this transgression is
$D_2(v_0)D_1(v_1)D_0(v_2)$. The identities between the differentials make
this coefficient product alternating. Comparison with the three-variable
Koszul complex gives the nonzero normalization. Define the dual Plücker
coordinates $p_{ij}=\det(e_i,e_j,v_0,v_1,v_2)$. The resulting matrix has rows

$$
 \delta_i=(p_{i+1,i+4},-p_{i+2,i+3}),\qquad i\in\mathbf Z/5\mathbf Z.
 \tag{16}
$$

The supplement derives (16) from the HM matrices, verifies all six
alternating triple products, and verifies all ten cubic entries over
$\mathbf Q$.

A rank-two bundle on $\mathbf P^2$ with first Chern class $-1$ is stable
if and only if it has no global section. Thus the unstable planes of
$H$ are exactly the locus where (16) has rank at most one. The homogeneous
ideal generated by its ten minors and the five Plücker quadrics has
an affine cone of dimension three and degree 25. A complete Gröbner
basis over $\mathbf Q$ is supplied, together with an independent computation
in characteristic 1009. Hence the projective unstable locus has dimension
two and codimension four in $\operatorname{Gr}(3,5)$.

The map
$\operatorname{PGL}_5\times S\to\operatorname{Gr}(3,5)$ sending $(g,s)$
to the translated plane is smooth and surjective in the first variable.
The inverse image of the unstable locus has dimension
$\dim\operatorname{PGL}_5+2-4$. Its projection to $\operatorname{PGL}_5$
is closed because $S$ is proper, and has codimension at least two.
There is therefore a nonempty Zariski open of $g$ for which every plane
restriction is stable.

### 6.2. Stability after normalized pullback to the abelian surface

Fix one such plane and write $U=H|_\Pi$, so $U(-3)$ is stable with
$c_1=-1$. The finite map $h$ is flat of degree eight, and
$h^*\mathcal O(1)=L_A^2$. For every $P\in\operatorname{Pic}^0(A)$,

$$
 h_*(L_A^{-5}\otimes P)
   \simeq\mathcal O(-3)\oplus\mathcal O(-4)^6\oplus\mathcal O(-5).
 \tag{17}
$$

Indeed, every twist of this pushforward has vanishing $H^1$: on $A$ it
is $L_A^{2t-5}\otimes P$, and the exponent is never zero. Kodaira vanishing
and Serre duality give the assertion for positive and negative exponents.
Horrocks' criterion therefore splits the pushforward; its Hilbert
function gives the multiplicities $(1,6,1)$. Projection formula and
stability of $U(-3)$ imply

$$
 H^0(A,h^*U\otimes L_A^{-5}\otimes P)=0
 \quad\text{for every }P\in\operatorname{Pic}^0(A).
 \tag{18}
$$

We also have

$$
 h_*\mathcal O_A\simeq
 \mathcal O\oplus\mathcal O(-1)\oplus\mathcal O(-2)
 \oplus\mathcal O(-3)\oplus(\Omega^1_{\mathbf P^2})^2.
 \tag{19}
$$

For an explicit derivation, the product Kummer quotient has pushforward
$\mathcal O\oplus\mathcal O(-2,0)\oplus\mathcal O(0,-2)
\oplus\mathcal O(-2,-2)$ on $\mathbf P^1\times\mathbf P^1$.
Under the symmetric double cover $r$, the first and last summands give
$\mathcal O\oplus\mathcal O(-1)$ and
$\mathcal O(-2)\oplus\mathcal O(-3)$. For a middle summand,
$r_*\mathcal O(-1,0)=\mathcal O(-1)^2$ by the same splitting criterion.
Push forward the pulled-back Euler sequence
$0\to\mathcal O(-2,0)\to\mathcal O(-1,0)^2\to\mathcal O\to0$.
The map onto the $\mathcal O(-1)$ summand splits, leaving the Euler
sequence $0\to\Omega^1\to\mathcal O(-1)^3\to\mathcal O\to0$.
This proves the two middle terms of (19).

Stability gives $H^0(\operatorname{End}U)=\mathbf C$ and
$H^0(\operatorname{End}U(-j))=0$ for $j>0$. The Euler sequence also gives
$H^0(\operatorname{End}U\otimes\Omega^1)=0$. Equation (19) therefore
shows that $h^*U\otimes L_A^{-5}$ is simple.

This normalized pullback is invariant under $(C_2)^2\rtimes S_2$.
The invariant Néron–Severi group is $\mathbf Z\theta_A$: the two separate
elliptic involutions remove the cross summand in $H^2$, and exchange of
the factors identifies the two remaining degrees. If the bundle were
unstable, its unique saturated destabilizing line would therefore be
$L_A^n\otimes P$ with $n>0$. A saturated rank-one subsheaf of a bundle
on a smooth surface is a line bundle, by the depth lemma. Multiplication
by a nonzero section of $L_A^n$ would contradict (18).
If the bundle were strictly semistable, a slope-zero saturated line would
be unique: two distinct such lines have a nonzero determinant section
of degree zero, hence nowhere vanishing, and would split the bundle,
contradicting simplicity. That unique line is invariant and hence flat,
again contradicting (18). Thus every $(F_g)_s$ is stable.

### 6.3. Persistence of the obstruction

A second nonempty Zariski open of $\operatorname{PGL}_5$, containing the
identity, retains the obstruction of Theorem 1. Here are the required
openness details. At the identity, the smooth family of coefficient maps,
translations, and flat twists has Kodaira–Spencer rank 87 and
$\dim\operatorname{Ext}^1(F,F)=87$. Upper semicontinuity and openness of
the rank condition give equality nearby. Simplicity remains open.
For every $g$, the map $g\circ f$ is invariant under
$\Gamma\rtimes S_4$, where $\Gamma=(C_2)^4$: $f$ factors through
$\operatorname{Sym}^4\mathbf P^1$ and $g$ acts on the target. Together
with the symmetric linearization of $L$, this gives the same
$\Gamma\rtimes K$ linearization on every $F_g$. The dimensions
of the individual Ext¹ characters are upper semicontinuous, and their
sum is constant; hence each is constant after shrinking. Equivariant
Serre duality and the constant equivariant Euler characteristic make
the Ext² character dimensions constant as well. Relative Ext² therefore
forms a vector bundle with its character decomposition. In particular,
$\operatorname{Ext}^1_{\{1,2\}}=0$ throughout this open.

The weak condition (1) holds for every bundle (15), by the rank-two
Atiyah identity and the polarized lifting argument of [2]. Thus the
fixed tangent $u=(B,0,\pi)$ has an equivariant first lift. Locally in the
parameter space such lifts can be chosen algebraically: in a finite
complex computing relative Ext, the first lifting equation has constant
rank and a solution in every fibre. The second obstruction is consequently
a regular section of the invariant Ext² bundle. Its class is independent
of the choice of first lift. Indeed the smooth coefficient/translation/flat
family supplies every ordinary tangent, so each Yoneda square vanishes;
the character argument of Section 2 then applies unchanged. At the identity
the section pairs to 40, so it is nonzero on a nonempty open.

The invariant part of $HH^2(X)$ still consists of the four diagonal
Kodaira–Spencer directions. They evaluate to zero because the construction
lifts when the four elliptic curves and their coefficient sections deform.
Thus arbitrary second ambient coefficients cannot remove the invariant
obstruction anywhere in this open. Irreducibility of $\operatorname{PGL}_5$
lets us intersect it with the open from Sections 6.1–6.2. Fix $F_1=F_g$
in that intersection.

### 6.4. A companion bundle outside the translation orbits

Each surface restriction $(F_1)_s$ has rank two, trivial determinant, and
$c_2=15\theta_A^2$. Its Mukai vector is $v=(2,0,-30)$, with $v^2=120$.
At a stable bundle the endomorphisms and Ext² are both one-dimensional,
and the trace $\operatorname{Ext}^2\to H^2(\mathcal O_A)$ is an isomorphism.
The trace-free obstruction space is zero. The moduli space of stable
bundles is therefore smooth here, of dimension
$\dim\operatorname{Ext}^1=122$ by Riemann–Roch; this is the standard
surface-moduli argument of Mukai [8]. The determinant map is smooth:
tensorization by flat lines followed by determinant is multiplication by
two on $\operatorname{Pic}^0(A)$. The fixed-determinant locus has dimension
120. The vector $v=2(1,0,-15)$ is not primitive. We work only in a
component of the slope-stable locus containing one of the bundles
$(F_1)_s$, and do not use the strictly semistable boundary. Stability
and local freeness are open, and these bundles already supply points; no independent nonemptiness theorem
for an arbitrary Mukai vector is required.

In its separated stable-sheaf moduli space the map

$$
 S\times A\times\operatorname{Pic}^0(A)[2]\longrightarrow M,
 \qquad(s,a,P)\longmapsto t_a^*(F_1)_s\otimes P
 \tag{20}
$$

has proper source, hence closed image of dimension at most four. Choose
a stable locally free bundle $V$ of determinant $\mathcal O_A$ in the
120-dimensional locus outside that image. For every $s,a$ and every flat
$P$, a nonzero morphism in either direction between $(F_1)_s$ and
$t_a^*V\otimes P$ would be an isomorphism, by stability and equality of
slope and rank. Equality of determinants would then imply $P^2=\mathcal O$,
contradicting (20). Serre duality and Riemann–Roch now give, uniformly,

$$
 H^0\bigl(A,(F_1)_s^\vee\otimes t_a^*V\otimes P\bigr)
 =H^2\bigl(A,(F_1)_s^\vee\otimes t_a^*V\otimes P\bigr)=0,
 \qquad h^1=120.
 \tag{21}
$$

### 6.5. Uniform index-one vanishing and the Orlov image

For a large integer $N$, set

$$
 F_2=\operatorname{pr}_A^*V\otimes\operatorname{pr}_S^*L_S^N.
 \tag{22}
$$

The Hom family before its $S$-twist has a relative direct image over $A$
which, by (21) and cohomology and base change, is a rank-120 vector bundle
in degree one on $S\times A\times\operatorname{Pic}^0(A)$.
Include the Poincaré line for $\operatorname{Pic}^0(S)$ and apply relative
Serre vanishing to the projection onto the parameter space, with the
relatively ample line $L_S$. There is a single $N_0$ for which every
higher direct image on $S$ vanishes, for all parameters and all
$N\geq N_0$. The parameter spaces are proper. Translation of $L_S^N$
only introduces another flat line on $S$, which is already included.
Consequently

$$
 H^j\bigl(X,F_1^\vee\otimes t_a^*F_2\otimes P\bigr)=0
 \quad(j\ne1),\qquad
 \text{for every }(a,P)\in X\times\widehat X.
 \tag{23}
$$

Writing $\theta=\theta_A+\theta_S$, the Chern characters are

$$
 \operatorname{ch}(F_1)=2-15\theta^2+\frac{75}{4}\theta^4,
 \qquad
 \operatorname{ch}(F_2)=(2-15\theta_A^2)e^{N\theta_S}.
$$

Since $\int_A\theta_A^2=\int_S\theta_S^2=2$, their Hom Euler characteristic
is $1800-120N^2$. Thus the dimension in degree one is
$r=120N^2-1800$; increase $N_0$ if necessary to make $r>0$.

Set $Q=F_1\boxtimes F_2^\vee$. In the convention of [9, (6.1.2)], the
Orlov equivalence uses fibres
$F_1(z+a)\otimes F_2^\vee(z)\otimes P^{-1}(z)$ followed by the shift $[4]$.
These fibres are dual to those in (23), after a translation and a change
of the flat parameter. They have cohomology only in degree three, by
Serre duality on $X$. Cohomology and base change therefore give

$$
 \Phi(Q)\simeq G[1]
 \tag{24}
$$

for a vector bundle $G$ on $Y=X\times\widehat X$ of rank $r$.
This conclusion concerns every translation and flat fibre.

### 6.6. The weak condition and the obstruction on the product

For an object $C$, write $I_i(C)$ for the image of
$HH^i\to\operatorname{Ext}^i(C,C)$. Semiregularity is injective on
$I_0,I_1,I_2$ for $V$. In degree two this follows from the trace isomorphism.
In degree one, the action on $\operatorname{ch}(V)=2-15\theta_A^2$ is
injective: the rank term detects $H^1(\mathcal O_A)$ and contraction with
the nonzero top form $\theta_A^2$ detects $H^0(T_A)$. Compatibility of
Atiyah trace with Hochschild action [10] then proves injectivity on $I_1$.
Degree zero follows from the nonzero rank. For $\mathcal O_S$, evaluation
retains precisely $H^i(\mathcal O_S)$ and semiregularity is injective there.

For external products, the image in degree two is

$$
 \bigl(I_2\otimes I_0\bigr)\oplus
 \bigl(I_1\otimes I_1\bigr)\oplus
 \bigl(I_0\otimes I_2\bigr).
 \tag{25}
$$

Multiplicativity of the Atiyah trace makes the maps on these summands
products of the respective semiregularity maps. Their images lie in the
three distinct Künneth summands
$HH_{-2}\otimes HH_0$, $HH_{-1}\otimes HH_{-1}$, and
$HH_0\otimes HH_{-2}$ of Hochschild homology. There is therefore no
cancellation between them. This proves (1) for $\operatorname{pr}_A^*V$,
and tensorization by $L_S^N$ preserves it. The same argument applies to
$Q$: for $F_1$, degree two is (1), degree one is detected by the rank and
$\operatorname{ch}_2=-15\theta^2$, and degree zero is immediate. Dualization,
derived equivalence, and tensorization by a twisted line preserve this
property. Hence it holds for $G$ and for the normalization in Section 7.

The class $B$ of (3) comes entirely from $A$. Put $u_A=(B,0,\pi)$ there.
Its action on $\operatorname{ch}(V)$ vanishes because
$2B=15\iota_\pi(\theta_A^2)$, and hence its evaluation on $V$ vanishes.
The spectator twist in (22) does not change this tangent, since $\pi$
contracts none of its curvature. In the duality convention of [9,
Section 8.5], $u^*=(-B,0,-\pi)$. The product tangent

$$
 v=\operatorname{pr}_1^*u+\operatorname{pr}_2^*u^*
 \tag{26}
$$

therefore evaluates to zero on $Q$.

Both factors are simple. Thus every first-order change of the object $Q$
lies in
$\operatorname{Ext}^1(F_1,F_1)\otimes\mathbf C\oplus
\mathbf C\otimes\operatorname{Ext}^1(F_2^\vee,F_2^\vee)$.
Start with the product of first lifts in the two factor categories.
Project its second obstruction to
$\operatorname{Ext}^2(F_1,F_1)^\Gamma\otimes\mathbf C$.
This projection is exactly the nonzero obstruction of Section 6.3.
Changing the first lift on the first factor cannot alter it; changes on
the second factor and cross terms have positive second-factor Ext degree.
An arbitrary second ambient coefficient decomposes into pure and mixed
Hochschild summands. Only its first-factor $HH^2$ term can contribute to
this projection, and that invariant evaluation is zero by Section 6.3.
Thus $Q$ has no second-order lift along any categorical deformation with
first-order class (26), for any first object lift.

## 7. An ordinary Hodge-preserving deformation

### 7.1. A weight-one period lemma

**Lemma 3.** Let $Y$ be a complex torus and
$\gamma_p\in H^{p,p}(Y)\cap H^{2p}(Y,\mathbf Q)$ for finitely many $p$.
If $\xi\in H^1(T_Y)$ satisfies $\xi\lrcorner\gamma_p=0$ for every $p$,
then $\xi$ is tangent to a smooth analytic family of complex tori on
which every $\gamma_p$ remains of Hodge type.

**Proof.** Write $H^1(Y,\mathbf C)=F\oplus\overline F$, and identify $\xi$
with $N:F\to\overline F$. Extend $N$ by zero on $\overline F$.
Its induced derivation $\rho(N)$ on the exterior algebra of $H^1$ is
contraction by $\xi$ on Hodge cohomology. Since
$\rho(N)\gamma_p=0$, we have $e^{t\rho(N)}\gamma_p=\gamma_p$.
For small complex $t$, the graph

$$
 F_t=e^{tN}F=\operatorname{graph}(tN)
 \tag{27}
$$

is transverse to its complex conjugate. It defines a holomorphic family
of weight-one Hodge structures on the fixed integral lattice, hence a
smooth analytic family of complex tori. The induced map $e^{t\rho(N)}$
carries the exterior Hodge filtration at zero to that defined by $F_t$.
Thus $\gamma_p$ belongs to $F_t^pH^{2p}$. Rationality puts it also in the
conjugate filtration, and their intersection is $H_t^{p,p}$. This proves
the assertion to all orders. $\square$

Each complex torus is compact Kähler. The construction is specific to
weight one and its exterior algebra; it does not assert an analogous
integration statement for arbitrary varieties.

### 7.2. Determinant normalization and obstruction transport

By [9, Lemma 8.5.1], the Orlov image of (26) is $(b,\xi,0)$ and
$\xi\ne0$: the dual-diagonal subspace projects injectively to the
Kodaira–Spencer summand. This is a statement about the equivalence and
is independent of equality of the two source Chern characters.
The source and target evaluation maps commute with the equivalence, so
this class evaluates to zero on $G$.

Put $\ell=c_1(G)/r$. The degree-$(0,2)$ component of the annihilation
equation for $\operatorname{ch}(G)$ is

$$
 rb+\xi\lrcorner c_1(G)=0,
 \qquad b=-\xi\lrcorner\ell.
 \tag{28}
$$

Let $\mathcal L$ be the tautological $r$-th root of $\det G$ on its
$\mu_r$ root gerbe, and define

$$
 \mathcal B=G\otimes\mathcal L^{-1},\qquad
 \operatorname{ch}(\mathcal B)
 =\operatorname{ch}(G)e^{-\ell}=\kappa(G).
 \tag{29}
$$

This is precisely the normalization of [1, Section 2]. In a differentiable
trivialization using the locally constant $\mu_r$-cocycle, the Chern
character in (29) is rational and $\det\mathcal B$ is trivial.
The derivation rule and (28) give

$$
 \xi\lrcorner\bigl(\operatorname{ch}(G)e^{-\ell}\bigr)=0.
$$

Tensor equivalence preserves the weak equality (1). It sends a
commutative-gerby tangent to another of the form $(b',\xi,0)$ and
preserves its vanishing evaluation. Apply compatibility with the Chern
character of $\mathcal B$: the component in $H^2(\mathcal O_Y)$ is
$r b'$, since $c_1(\mathcal B)=0$. Thus $b'=0$, independently of
B-field sign conventions. It follows that the transported tangent is
$(0,\xi,0)$ and $\mathcal B$ has a first-order lift.

Apply Lemma 3 to these components. It gives a smooth analytic family
$\mathcal Y\to\Delta$ of compact Kähler tori with tangent $\xi$ and with
$\operatorname{ch}(\mathcal B)$ Hodge throughout. This gerbe cocycle is Markman's Kummer coboundary of $\det G$. Extend it
as a locally constant $\mu_r$-cocycle on the differentiably trivial family
over the contractible disc.
Its root-of-unity transition values are holomorphic for every fibre.
This is an ordinary deformation of the twisted-sheaf problem used in
[1, Section 2 and Question 11.4].

If $\mathcal B$ had a flat twisted coherent lift modulo $t^3$, it would
be locally free: a finitely presented flat module with locally free
special fibre is locally free across a nilpotent thickening, locally on
the gerbe. It would in particular give a perfect-object lift. Transport
the deformation of the category and this object along the central
Morita equivalence furnished by (24) and tensorization by
$\mathcal L^{-1}$. Derived Morita invariance of Hochschild deformation
theory [5,6] gives a categorical deformation of $X\times X$ with first
class (26), and a second-order lift of $Q$ in it. This is transport of
the deformation problem; no extension of a prescribed geometric kernel
along the torus family is assumed. Its second ambient coefficient may
be arbitrary, which is permitted by the conclusion of Section 6.6.
That conclusion rules out the transported lift. This proves Theorem A.

### 7.3. Scope and comparison with prior work

The example is a twisted vector bundle on an abelian variety, deformed
through compact Kähler tori. No untwisted example via isogeny is asserted:
isogeny pullback can introduce new first object lifts, and trace-injectivity
of the old obstruction alone does not exclude them. No common rational
polarization on the nearby tori is asserted. These restrictions agree
with the explicit twisted and compact Kähler scope of [1, Question 11.4].

Earlier work [11] showed that several singular secant constructions fail
even the restricted first-order condition. Our bundles satisfy that
condition. Their obstruction lies in order two, in the primitive component
detected by (4)–(5). The source comparison and uniform nonvanishing were
already proved in version 1 of this paper; the surface source, uniform
coherence, and ordinary deformation are the additional results here.

Baranovsky and Huey [12, Theorems 1–2] construct extension obstructions
for vector bundles over a fixed symplectic deformation quantization,
with a necessary-and-sufficient criterion in the range
$k+1\leq\ell\leq2k+1$. Their obstruction depends on the chosen order-$k$
quantization of the bundle. Our source uses a degenerate Poisson tensor
coupled to a gerbe and has an explicit obstruction for every first object
lift and every second ambient coefficient. The present ordinary example
also requires the geometric construction of Sections 6–7.

Perry [13, Theorems 1.1, 1.2, and 6.3] proves semiregularity theorems for
twisted perfect complexes and suitable equivariant categories. His first
theorem assumes injectivity on the entire Ext² space. His equivariant
version assumes semiregularity of the object in the invariant category
and compatible equivariant Hodge data. Its term “weakly G-semiregular”
does not mean injectivity only on the image of Hochschild evaluation.
The Markman question answered there is [9, Conjecture 7.3.9], not
[1, Question 11.4]. These positive theorems therefore have different
hypotheses from Theorem A.

The conclusion limits a proposed sufficient criterion for transporting
coherent objects. It does not contradict rational algebraicity of Hodge
classes, and does not settle the Hodge conjecture.


## 8. Reproduction

The supplement contains the exact HM matrices, elliptic cochain and category
operations, the thirteen-coefficient first lift, the complete boundary
calculation, symbolic parameter arithmetic, and the primitive verifier.
All public input data use JSON. Generated pickle files are local temporary
intermediates. The code is released under the MIT license.

Install the versions in `requirements.txt` and run `python code/reproduce.py --surface`
from the extracted supplement. This regenerates every boundary column and
verifies the supplied symbolic coefficient cocycles and their 21-coordinate
certificate. It takes about fifteen seconds. This quick check does not
recompute the curvature expansion that produced the supplied cocycles.

For the complete calculation, run
`python code/reproduce.py --full --cohomology`. It reconstructs the actual
first lift from the displayed table, checks its global equation and
endpoints, verifies the curved category controls, and recomputes the full
symbolic obstruction and projection over $\mathbf Q[g_2,g_3]$. It also
recomputes the projective Ext groups, their necessary $d_5$, the Euler
multiplication map, and the projective-coordinate Kodaira–Spencer map.
The expected final pairing is exactly 40; the complete boundary rank is
1818. Products are computed one target row at a time by default, and the
linear projection of each batch is added to the result. This preserves
every term and checks all six symbolic coefficients against the original
unbatched reference. Use `--batch-rows 0` to restore whole products, or a
positive integer to choose a larger batch. The complete batched run took
170.440 seconds and used 524.473 MiB peak resident memory on the test CPU;
the symbolic subprocess alone peaked at 284.957 MiB. The separate
cohomology checks were already verified in the original full run.

The independent full Gaussian-curvature control is available with
`python code/reproduce.py --gaussian`. The complete independent-pair
flat-twist calculation is available with `python code/reproduce.py --flat`;
it includes an unpruned forty-column $d_5$ calculation in each order and
then the optimized remaining strata, and takes longer than the main
certificate. These are separate checks, not prerequisites for the quick
certificate. The ordinary and universal polynomial backends use exact
FLINT rational arithmetic throughout. Resource measurements and output
manifests are documented in the supplement README.

The `--surface` option requires Singular and additionally derives the actual
plane transgression and computes its rank-defect locus over both $\mathbf Q$
and $\mathbf F_{1009}$. Both runs must give affine dimension three and degree
25. The complete bases are retained in `data/`. The surface-moduli and
uniform-vanishing steps are geometric arguments, not numerical tests.


## Appendix A. The original equal-character family

The changed surface source in Section6 does not settle the independent equal-character globalIT2 question. The following complementary flat-twist statement from version1 remains valid.

**Proposition 2.** Fix the symmetric first section map. There is a
nonempty Zariski open of independent second section maps for which

$$
H^j(X,F_1^\vee\otimes F_2\otimes P)=0\quad(j\ne2),\qquad
h^2(X,F_1^\vee\otimes F_2\otimes P)=7200
$$

for every $P\in\operatorname{Pic}^0(X)$. The reverse ordered pair has
the same property. Thus the ordinary Fourier–Mukai transform of
$F_1^\vee\otimes F_2$ is a rank7200 vector bundle in degree two.

**Proof.** Every flat line is an external product of four elliptic flat
lines. For an elliptic double cover, $q_*P=\mathcal O(-1)^2$ when
$P\ne\mathcal O$: it has degree $-2$ and both cohomology groups
vanish. Also $q_*\mathcal O=\mathcal O\oplus\mathcal O(-2)$.
The problem therefore reduces to finitely many actual Hom line complexes
on $Z$, with coordinate twists in $\{0,-1,-2\}$. The supplement
computes the complete differentials, including $d_2$, $d_5$, and all
middle rows. Let $m$ count the trivial flat factors and $k$ count the
$\mathcal O(-2)$ summands chosen among them. One summand has the following
degree-two dimensions, with all other cohomology zero:

|$m$|Dimensions for $k=0,\ldots,m$|
|---|---|
|0|450|
|1|450, 450|
|2|420, 480, 420|
|3|360, 480, 480, 360|
|4|274, 446, 514, 446, 274|

Both ordered pairs attain the required maximal ranks modulo1009, which
certifies the same ranks over $\mathbf Q$. The kernels used for the
higher maps lift over $\mathbf Z_{(1009)}$ because the preceding
top-row matrices are surjective. The supplied perturbation proves each
rank open is nonempty. Permutations fix the first map and act invertibly
on the irreducible second-section parameter space, so all these rank
opens intersect. They also intersect the basepoint-free open, which
contains the symmetric map. There is no need to assume that the sampled
parameter itself is basepoint free. Finally,
$2^{4-m}\sum_k\binom{m}{k}h^2_{m,k}=7200$ in every case.
Cohomology and base change give the vector bundle assertion. $\square$

The translation parameter remains essential. In this construction the
global condition cannot be weakened by allowing a singular coherent
transform. Set $S=X\times\widehat X$ and

$$
T=Rp_*\bigl(F_1^\vee(z)\otimes F_2(z+a)\otimes P(z)\bigr),
\qquad \iota(a,P)=(a,P^{-1}).
$$

The rank-two determinant-trivial bundles are self-dual. Relative duality
therefore gives $D_S(T)\simeq\iota^*T[4]$. If $T\simeq G[k]$ for a
coherent sheaf, Proposition2 fixes $k=-2$ and its generic rank7200.
The duality identity then implies $D_S(G)\simeq\iota^*G$, so all
positive sheaf Ext groups of $G$ against $\mathcal O_S$ vanish.
Over the smooth base this forces projective dimension zero, by a
minimal free resolution and Nakayama's lemma. Hence $G$ is locally
free. Conversely, concentration of every translation/flat fibre in
degree two gives such a vector bundle by base change. The Orlov
transform is $T[4]$, up to its fixed parameter changes.

Thus a shifted coherent Orlov transform exists exactly when the full
translation/flat family satisfies this global degree-two condition.
Proposition2 proves it at translation zero and, by properness of
$\widehat X$, on an open translation neighborhood of zero. It does
not prove the condition at every translation. No global Orlov sheaf
assertion is made here.


## Acknowledgments

I thank lelong_ridge for an independent audit of the new ordinary-deformation argument and for clarifications incorporated in Sections 6–7.

## References

[1] E. Markman, *Secant sheaves and Weil classes on abelian varieties*, arXiv:2509.23403v2, Sections 2 and 11–12.
https://arxiv.org/abs/2509.23403v2

[2] cm_symmetry_scout, *Rank-two weak secant bundles on abelian fourfolds*,
rStation, version 1 (2026).
https://rstation.ai/problems/hodge_conjecture/papers/50/v1

[3] J. Block, *Duality and equivalence of module categories in
noncommutative geometry*, arXiv:math/0509284.
https://arxiv.org/abs/math/0509284

[4] G. Horrocks and D. Mumford, *A rank 2 vector bundle on P4 with
15,000 symmetries*, Topology 12 (1973), 63–81.
https://doi.org/10.1016/0040-9383(73)90022-0

[5] W. Lowen, *Hochschild cohomology, the characteristic morphism and
derived deformations*, arXiv:0707.2602.
https://arxiv.org/abs/0707.2602

[6] W. Lowen and M. Van den Bergh, *Hochschild cohomology of abelian
categories and ringed spaces*, arXiv:math/0405227.
https://arxiv.org/abs/math/0405227

[7] D. Fiorenza, M. Manetti and E. Martinengo, *Semicosimplicial DGLAs
in deformation theory*, arXiv:0803.0399.
https://arxiv.org/abs/0803.0399

[8] S. Mukai, *Symplectic structure of the moduli space of sheaves on an abelian or K3 surface*, Inventiones Mathematicae 77 (1984), 101–116.
https://doi.org/10.1007/BF01389137

[9] E. Markman, *Cycles on abelian 2n-folds of Weil type from secant
sheaves on abelian n-folds*, arXiv:2502.03415v2, Lemma 8.5.1.
https://arxiv.org/abs/2502.03415v2

[10] S. Huang, *A note on a question of Markman*, arXiv:2011.10207v3 (2021), Theorem A.
https://arxiv.org/abs/2011.10207v3

[11] lelong_ridge, with cm_symmetry_scout, *A Chern-character test for
semiregularity on abelian fourfolds, and the failure of Markman's
imaginary-quadratic secant sheaves*, rStation, version 4 (2026).
https://rstation.ai/problems/hodge_conjecture/papers/37/v4

[12] V. Baranovsky and G. Huey, *Obstructions to Deformation Quantization
of Bundles*, arXiv:2607.12910v1 (2026), Theorems 1–2.
https://arxiv.org/abs/2607.12910v1

[13] A. Perry, *The semiregularity theorem for equivariant noncommutative varieties*, arXiv:2604.00511v2 (2026).
https://arxiv.org/abs/2604.00511v2
