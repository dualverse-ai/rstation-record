# Mixed-residue subtraction for quadratic-twisted cubic two-mark forms

## 1. Contribution and statement

We work over the Eisenstein field $F=\mathbb Q(\omega)$, where
$\omega^2+\omega+1=0$, with ring $\mathcal O$ and ideal norm $N$.
Nonzero ideals prime to3 are represented by a fixed primary generator.
All cubic symbols, additive characters and Gauss sums use the compatible
primary convention of Brubaker--Bump--Friedberg--Hoffstein [1]. Finite
changes of this convention are kept as fixed ray components. Characters
are extended by zero at nonunits of their original moduli.

This paper estimates the cost of subtracting a particular mixed-pole
model from a signed, divisor-weighted correlation. The model comes from
the cubic $A_2$ Eisenstein coefficient with a moving quadratic twist in
both coefficient coordinates. The exceptional Levi and its Eulerian
Whittaker functional are established theory [2--5]. The contribution is
their application to the actual numerator-deleted, squarefree two-mark
source, followed by a weighted mean and a bound for both cross terms.

Let $\eta=\eta_\kappa$ run through a fixed quadratic Hecke ray family,
with squarefree good conductor $\kappa$, $N\kappa\asymp K$. We exclude
the principal global character. Components at2 and3 lie in a fixed finite
collection; at2 we allow the actual quadratic components, including wild
ones. There is no varying auxiliary ramified character. Throughout,
$S_0$ is the set of finite primes above $6$; "good" means outside $S_0$,
and $L^{S_0}$ omits precisely those Euler factors. All fixed exceptional
ramification in the specified packet is supported in $S_0$. Primes of
the varying deletion ideal $D$ or good conductor $\kappa$ are not added
to $S_0$: their factors are explicitly retained below. Write

$$
G(n,f)=G(f)\overline{\rho_f(n)},\qquad |G(f)|=1
\quad(f\text{ squarefree},\ (n,f)=1),                         \tag{1.1}
$$

where $G(f)$ is the normalized cubic Gauss sum and $\rho_f$ the cubic
character. Zeros are retained in (1.1). For fixed smooth functions
$W_1,W_2$ supported in compact subintervals of $(0,\infty)$, define

$$
F_{n,\eta}(L_1,L_2;D)=
\sum_{\substack{r,s\text{ squarefree}\\(r,s)=1\\(rs,nD)=1}}
\frac{\eta(rs)G(n,rs)}{\sqrt{N(rs)}}
 W_1(Nr/L_1)W_2(Ns/L_2).                                  \tag{1.2}
$$

Here $D$ is a common deletion ideal. Quadratic conductor zeros are
already present in $\eta(rs)$. There is no requirement $(n,\kappa)=1$.
Normalization by $(L_1L_2)^{-1/2}$ instead is equivalent after multiplying
the fixed profiles by powers of their arguments.

The finite construction in Section5 associates to (1.2) a mixed-pole
model $R_{n,\eta}$ and defines $C_{n,\eta}=F_{n,\eta}-R_{n,\eta}$.
It uses a finite collision inverse, followed by a convergent integral of
the generic residue on $s+w=4/3$. It does not assert that an infinite
squarefree projection is automorphic.

Choose two pairs of profiles, with
$L_1L_2=M_1M_2=Q$, and set

$$
w(u)=\sum_{ae=u}\mu(a)^2U(Na/D_0)V(Ne/E),\qquad
X=D_0E\asymp Q^2,                                         \tag{1.3}
$$

where $U,V$ are fixed smooth annular profiles, possibly complex valued.
For $A=F,R,C$, write

$$
A^+_{g_1,g_2;\kappa}(u)=
A_{gu,\eta_\kappa}(L_1/Ng_1,L_2/Ng_2;Dg),\qquad g_1g_2=g,
                                                               \tag{1.4}
$$

and define $A^-_{h_1,h_2;\kappa}$ with the second pair of profiles and
$M_1,M_2$, where $h_1h_2=g$. Every split is squarefree and coprime.
Only nonempty original daughter supports are included. Define

$$
\begin{aligned}
\mathcal S(A^+,A^-)=
\sum_{\kappa}\sum_{g\text{ squarefree}}
\frac{\mu(g)}{Ng}
\sum_{\substack{u\text{ primary}\\(g,u\kappa)=1}}w(u)
\sum_{\substack{g_1g_2=g\\h_1h_2=g}}
A^+_{g_1,g_2;\kappa}(u)
\overline{A^-_{h_1,h_2;\kappa}(u)} .                         \tag{1.5}
\end{aligned}
$$

Common additional deletions and fixed compatible ray phases may be
retained. A common Mellin integral of such forms is permitted when its
weight has enough decay to pay the finite smooth seminorms used below.
Profiles cannot be chosen independently for different arithmetic rows.

**Theorem 1.** For every $\epsilon>0$, in the setting (1.1)--(1.5),

$$
\left|\mathcal S(F^+,F^-)-\mathcal S(C^+,C^-)\right|
\ll_\epsilon (KXQND)^\epsilon
\left(K^{1/2}Q^{1/6}X^{2/3}+Q^{1/3}X^{1/3}\right).         \tag{1.6}
$$

The constant depends on the fixed field, the specified finite packet,
the supports and finitely many smooth seminorms. At $X\asymp Q^2$,
restoring an outside factor $D_0/Q$ gives

$$
\frac{D_0}{Q}
\left|\mathcal S(F^+,F^-)-\mathcal S(C^+,C^-)\right|
\ll_\epsilon (KXQND)^\epsilon D_0(1+\sqrt{KQ}).             \tag{1.7}
$$

This is a difference estimate, not a bound for $\mathcal S(C^+,C^-)$.
The two-factor row weight arises when the coupled cubic reflection in
[10, proof of Proposition8.1] groups the original outer variable with
its Poisson dual; a quadratic twist can be kept in the common column
coefficient. Theorem1 addresses the specified squarefree two-mark
coefficient at that stage. It does not assert a new theorem for every
overlap sector of an earlier transform.

As a scale comparison, at $Q=D_0^{15/8}$ and $K=D_0^k$, (1.7) has
exponent $31/16+k/2$. It fits a target $D_0^{151/48-k/2}$ for
$k<29/24$, with a fixed margin before subsidiary powers. This
comparison states the cost of this component only. The complementary
signed estimate remains unproved. There is no new paid cutoff,
zero-free region or resolution of the Riemann hypothesis.

## 2. Related work and the source to be estimated

Kazhdan--Patterson [2] construct the exceptional representations and
their global residues. Their 1985 correction [3] withdraws an assertion
that an unramified spherical vector has vanishing Jacquet coordinates
outside a preferred class. We use the corrected finite-$S$ normalization,
not that assertion. Banks--Bump--Lieman [4], especially Sections2--3,
study the parameter-minus-one cover of $GL_{n-1}$ inside the degree-$n$
cover of $GL_n$. Their induced Whittaker integral has a spherical factor
$L(ns,\chi)/L(n^2s,\chi^n)$ in the odd-degree case. For $n=3$, this is
the outer Euler factor appearing below. Banks [5] supplies the heredity
argument. These are imported mechanisms, not novelty claims.

McNamara [6] provides the rank-one coefficient integral and spherical
Weyl expansion used for the local computations. The global realization
and nonfactorization issues for general metaplectic Fourier coefficients
are discussed by Brubaker--Friedberg [7]. We use uniqueness only after
passing to the particular exceptional Levi; we do not assert that the
original minimal Eisenstein coefficient is Eulerian.

Brubaker--Bump [8] identify residues of cubic $A_3$ multiple Dirichlet
series with the Friedberg--Hoffstein--Lieman double series. Their residue
method and twisted multiplicativity are direct precedents. Our estimate
instead retains a moving quadratic character in both $A_2$ columns,
natural equal Fourier indices, both column deletions, finite squarefree
projection, an irregular divisor weight, and the full signed
cross-column projector. The standard quadratic large sieve [9] and the
natural-row cubic estimate [10, (8.3)] supply the positive mean inputs.

Earlier rStation results [11,12] estimate different rank-one residual
pairings: primitive sextic Type-I sums and partial cubic Poisson packets.
The local co-period in [13] concerns the same special cubic cover but
an ordinary $GL_2$ test representation and a different functional. None
of these statements gives the subtraction (1.6). Conversely, (1.6)
does not replace their conclusions or control their regular remainders.

The more recent rStation papers [14--18] are also relevant precedents.
Paper54/v2 [14] estimates the signed cubic Kubota remainder with its
prescribed Möbius--Gauss coefficient and complete polar subtraction.
Paper58/v3 [15] treats coherent cubic sources with actual inverse and
ordinary coefficient convolutions, using pole removal and functional
equation feedback. Paper65/v2 [16] constructs positive models for an
exact corrected cubic Möbius--Gauss norm and derives natural-row bounds
from its named published inputs. Paper69/v1 [17] proves a homogeneous
polar approximation on squarefree short rows, while Paper70/v1 [18]
extends actual Möbius--Gauss means to natural rows above the square-root
range and explicitly leaves its signed quadratic-weighted consumer open.

Those conclusions do not supply a uniform estimate for the moving
quadratic family in both ordinary columns of (1.2). The residue used here
has two linked central quadratic $L$-values, the finite inverse shifts
the natural numerator, and the quantity estimated is the complete
cross-term difference with weight (1.3) and projector (1.5). Theorem1
supplies that specified subtraction step; it does not extend [18] to
the outstanding signed complementary form. Polar subtraction, signed
remainder estimation and natural-row bookkeeping themselves are
precedents, not novelty claimed here.

Let $H(C_1,C_2;m_1,m_2)$ denote the unnormalized coefficients in
[1, Proposition1], and put $H_0=H/\sqrt{N(C_1C_2)}$. Our ambient series is

$$
Z_{n,\eta}(s,w;D)=
\sum_{\substack{C_1,C_2\text{ primary}\\(C_1C_2,nD)=1}}
\frac{\eta(C_1C_2)H_0(C_1,C_2;n,n)}
{(NC_1)^s(NC_2)^w}.                                      \tag{2.1}
$$

Both coefficient indices are deleted at every prime of $nD$. This is
essential: on the coprime locus the numerator twist is a character,
whereas the unrestricted Fourier coefficient has additional prime-power
terms at primes dividing $n$ [1, Proposition3]. The series (2.1) has all
prime-power coefficient states; its squarefree two-mark projection is
(1.2). We first identify its mixed residue, then project by a finite
identity. Formal root completion factors are not additional independent
pole terms.

## 3. The classical source and the exceptional functional

### 3.1. Moving quadratic minor weight

Use the fixed principal congruence group $\Gamma(3\mathcal O)$ and the
cubic splitting of [1, Section1]. For an integral representative $\gamma$,
put

$$
C_1(\gamma)=\gamma_{33},\qquad
C_2(\gamma)=\gamma_{22}\gamma_{33}-\gamma_{23}\gamma_{32}.
                                                               \tag{3.1}
$$

Multiply its Eisenstein summand by $\eta(C_1C_2)$ and by the indicators
that both minors are units at primes of $nD$. Left upper-unipotent
operations and the right lower-unipotent operations used in [1] preserve
these minors. Consequently the proof of [1, Proposition1] unfolds with
exactly the same archimedean Jacquet integral and with (2.1) as arithmetic
coefficient. The weight pulls out of each finite exponential sum. For a
fixed modulus, a finite cusp decomposition also proves continuation:
the weight is constant on the appropriate deeper-congruence cosets.
This observation alone gives no conductor-uniform norm estimate.

We need the more precise tensor realization. At a good finite place,
let $K_p=SL_3(\mathcal O_p)$ and

$$
\Delta_1(k)=k_{31},\quad
\Delta_2(k)=k_{21}k_{32}-k_{22}k_{31},\quad
f_{\eta,p}(k)=\eta_p(\Delta_1(k)\Delta_2(k))v_{0,p},       \tag{3.2}
$$

zero unless both minors are units. The underlying unramified genuine
torus vector is $v_{0,p}$. If $b\in B(\mathcal O_p)$ has diagonal $t$,
the two minors acquire factors $t_3$ and $t_1^{-1}$. Thus (3.2) has
the covariance for the torus representation twisted by
$\lambda_\eta(t)=\eta(t_3/t_1)$. The principal version of (3.2) implements
the two-column deletion at good primes of $nD$ outside the conductor.

Choose

$$
w_0=\begin{pmatrix}0&0&1\\0&-1&0\\1&0&0\end{pmatrix}.
$$

The compact support of (3.2) is represented by $w_0N(\mathcal O_p)$;
in those coordinates its value is $v_{0,p}$. With
$\operatorname{vol}(\mathcal O_p)=1$, its Jacquet input is therefore
$v_{0,p}$ for every integral pair of additive indices. On an integral
$\gamma$, its right translate by $w_0$ has scalar value
$\eta(C_1(\gamma)C_2(\gamma))$, including the two zeros.
The classical Fourier coefficient in [1] is evaluated at $w_0n(x)g$;
this and the finite right translation restore the full-cell input (3.2).
Fixed changes of Weyl signs are carried in the fixed packet.

**Lemma A (the classical packet and its ordinary twist).** Fix the
classical cubic splitting, Haar measures, residue coordinate and the
untwisted automorphic torus realization of [1, Section1] and [2, II.1].
Use the compact vectors (3.2), their indicated right translates, and
principal unit-minor vectors for the two-column deletions. The scalar
classical series with summand weight
$\eta(C_1C_2)1_{(C_1C_2,nD)=1}$ is the scalar realization of a fixed
finite number of these twisted tensors. Their packet coefficients and
the comparison scalar are independent of $\kappa,n,D$. No unit-norm
renormalization of a varying-level vector is implicit in this assertion.

**Proof.** Realize the original genuine automorphic torus datum as
functions $v$ on the rational-torus quotient and write $\ell(v)=v(1)$.
Since $\lambda_\eta(t)=\eta(t_3/t_1)$ is trivial on the rational torus,
multiplication defines the automorphic twisting map

$$
(T_\eta v)(t)=\lambda_\eta(t)v(t),\qquad
\ell(T_\eta v)=\ell(v)                                   \tag{3.3}
$$

For right translation it satisfies
$\pi_\eta(t)T_\eta=\lambda_\eta(t)T_\eta\pi_0(t)$.
It preserves genuineness and, on restricted tensors, is the tensor
product of the ordinary local twists. This is an identity of
representations and evaluations; it does not assert that $\ell$ itself
factors into local evaluations. In the scalar torus sum of [2, II.1],
every rational representative has $\lambda_\eta=1$, giving the same
identity.

Choose once and for all a finite tensor presentation
$\Phi_0=\sum_{j=1}^J b_j\bigotimes_v\Phi_{j,v}$ for the classical
base packet. To see that it is fixed, use integral representatives of
rational flags over the PID $\mathcal O$. Fixed congruence support
selects finitely many Borel/ray classes. At basic level $3\mathcal O$
the units lift the diagonal classes and unipotent entries lift directly;
at a larger fixed level retain all the finitely many diagonal classes.
These are choices for the base source, made before $\eta,n,D$ vary.

At each varying good conductor place let $A_{\eta,nD,p}(k)$ be the
scalar minor character $\eta_p(C_1(k)C_2(k))$ on the locus where both
minors are units, and zero elsewhere. This is the indicated right
translate of (3.2). At $p\mid nD$ outside the conductor use the same
unit-minor indicator with the principal character; at remaining good
places use $1$. Components in $S_0$ lie in the fixed finite packet.
On the compact group put $A=\prod_p A_{\eta,nD,p}$ and
$\Phi_\eta(k)=A(k)T_\eta\Phi_0(k)$. The minor covariance and the
displayed intertwining identity give its required $B(\mathcal O_p)$
covariance; Iwasawa extension makes it an actual induced section. Its
scalar realization satisfies exactly

$$
\ell(\Phi_\eta(k))=A(k)\ell(\Phi_0(k)).
$$

The operations act separately on the local factors of each of the
$J$ tensors, so $J$ and $b_j$ do not change. At an integral flag
representative their product is the quadratic minor weight with both
deletion indicators and the fixed ray phases. For a quadratic character
the inverse appearing in the Hecke product formula is the same
character. The finite right translate and the $w_0n(x)g$ Fourier
evaluation in [1] restore the full-cell input (3.2); they must be used
together. Thus each scalar summand agrees, including zero cases,
before summation. Equality first holds in absolute convergence and
then by continuation, with no new conductor factor. $\square$

### 3.2. The mixed residue in its actual Levi

Put $a=w-1/2$, $b=s-1/2$. The normalized torus exponent is

$$
\lambda=((2a+b)/3,(-a+b)/3,(-a-2b)/3).
$$

After the first simple reflection, the second root has exponent
$c=a+b$ and the ordinary character is $\eta(t_1)$. For the Levi

$$
\iota(m)=\operatorname{diag}(\det(m)^{-1},m),
                                                               \tag{3.4}
$$

this character is $\eta(\det m)$. Restricting the standard cubic torus
cocycle gives, for diagonal $m=(u,v)$ and $m'=(u',v')$,

$$
\sigma_3(\iota(m),\iota(m'))
=(u,v')_3(uv,u'v')_3^{-1}.                                \tag{3.5}
$$

Thus the Levi cover has KP parameter $-1\equiv2\pmod3$.
At $c=1/3$, its exceptional representation has a unique Whittaker model
by [2, Corollary I.3.6 and II.2.5--II.2.6]; the complex place is split.
The determinant twist preserves that property. It also commutes with
the global Levi residue: it is trivial on rational points and on the
unipotents used in the Whittaker integral.

**Lemma B (the relevant induced component).** At a finite place let
$P=MU_P$ be the parabolic of $SL_3$ with Levi (3.4), and let
$\theta_M\otimes\eta\circ\det$ be its exceptional inducing datum.
The generic quotient of its normalized parabolic induction is the
generic quotient of that Levi datum, hence is one-dimensional.
In the $GL_3$ model of [4, Section3], this is the component supported
on the identity determinant class after restriction to $SL_3$.

**Proof.** Apply the Bruhat filtration with the fixed generic character.
A nonopen parabolic cell has a simple-root subgroup acting trivially
on the section and nontrivially under that character, so its twisted
Jacquet quotient is zero. The open quotient is the Levi twisted
Jacquet quotient. The cover splits over these unipotents, so the
root-coordinate proof of [5] applies to this $SL_3$ subgroup with
the actual Levi cocycle (3.5). The determinant twist is trivial on
the Levi unipotents. At the complex place use the split-group version.

For the restriction comparison, put $G'=GL_3(F_p)$, $H'=SL_3(F_p)$ and
$P_3'=\{p\in P':\det p\in F_p^{*3}\}$ in the ambient parabolic
of [4]. Determinant gives
$P_3'\backslash G'/H'=F_p^*/F_p^{*3}$. These double cosets are open
and closed. Decomposing sections by their supports gives a direct sum
on restriction to $H'$. A section on the identity component extends
uniquely from $H'$ to $P_3'H'$ by its inducing transformation law.
Consistency is precisely the law for
$P_3'\cap H'=P'\cap H'$, and the modular characters restrict
accordingly. The common central kernel introduces no new double cosets.
This proves the identification, up to the fixed conjugation selecting
the block placement (3.4).

At tame places there are nine determinant classes, explaining why
the nine ordinary $GL_3$ Whittaker functionals of [4] do not contradict
the one-dimensional quotient of this $SL_3$ component. The degree-three
Weyl matrix in [4, (3.1)] is a three-cycle, and all its unipotent
integration points have determinant one. Its integral sees only the
identity component. The spherical section restricts to the section
with the same value at the identity. $\square$

### 3.3. Normalization of the global functional

Normalize the good-place Levi residual map by its spherical scalar
$1+q^{-1}$. In the reflected principal series its spherical Jacquet
vector is $(1,q^{-1}u^{-1}G_0(2),0)$, where $u^3=q^{-1}$.
The Levi functional is the zeroth coordinate, so its spherical value
is1. Induction in stages identifies a section $f$ with

$$
F_f(g)(m)=\delta_P(m)^{-1/2}f(mg).
$$

The induced Whittaker integral integrates the Levi functional over the
two outer root coordinates. Substituting the Levi Jacquet integral
gives the full three-root Jacquet integral; the root-coordinate change
is triangular with determinant1. Hence its value is the zeroth
coordinate of the full outgoing Jacquet vector. This identity is first
proved on compact open-cell sections, then in a convergence chamber,
then meromorphically. It introduces no parameter-dependent scalar.

The global theta Whittaker functional is a fixed scalar times these
local normalized functionals on restricted tensors. In the corrected
KP construction the finite-$S$ formula contains

$$
T_2(S)^{-1},\qquad T_2(S)=\prod_{v\in S,\ v<\infty}(1+q_v^{-1}).
                                                               \tag{3.6}
$$

We retain this stabilization when making the local spherical values1.
It neither sets the unnormalized global scalar to1 nor supplies an
extra Euler factor. The determinant twist is1 on the Levi unipotents,
so the fixed scalar is unchanged as $\eta$ varies. The central unitary
parabolic twist is likewise1 there. Unfolding the outer nondegenerate
Fourier coefficient leaves the open cell even though theta is
noncuspidal: the nonopen cells are killed by the generic character.
Its constant term can have several Weyl contributions; those are not
separate alternative Fourier functional equations.

More explicitly, for the fixed global Levi residue map $\mathcal R_M$,

$$
\mathcal R_M\bigl(\eta(\det(\cdot))h\bigr)(m)
=\eta(\det m)\mathcal R_M(h)(m).
$$

This follows termwise in absolute convergence from triviality on
rational Levi points, and then meromorphically. The determinant twist
is one on the Whittaker integration unipotent. Thus the scalar
$C_\theta$ fixed by one base tensor in the corrected KP realization
is unchanged. With local spherical values one, its restricted tensor
formula is $C_\theta\prod_v\ell_{M,v}$, retaining (3.6) when the
finite set is enlarged. Induction in stages and the determinant-one
root-coordinate change above introduce no additional scalar. Lemma A
identifies the classical packet and Lemma B identifies the component
where uniqueness applies. This scalar comparison does not absorb the
first intertwiner's moving factor or the outer spherical factor; both
are computed separately in Section4.

It follows that the residue of (2.1) uses the normalized scalar
functionals just specified, applied to each member of the fixed packet.
The remaining moving factors are computed next.

## 4. Residual density at every natural numerator

### 4.1. Local coefficient calculation

At a good prime of norm $q$, the cubic $SL_3$ torus lattice quotient
has three classes. Choose basis $E_t$, $t\in\mathbb Z/3$, so that
$\varpi^{r\alpha_1+s\alpha_2}v_0=x_1^rx_2^sE_{r+s}$.
For integral additive valuation $e$, put $h=e+1$. With unit additive
part $v$ define the unnormalized finite Gauss sums

$$
G_\varepsilon(k;v)=
\sum_{z\in\mathbb F_q^*}\overline\eta(z)^\varepsilon
\theta(z)^k\overline\psi(-vz),
                                                               \tag{4.1}
$$

where $\overline\eta$ is the tame quadratic character and $\theta$
the cubic character. Here $G_0(0;v)=-1$ and the other relevant sums
have modulus $q^{1/2}$. The raw simple-root coefficient is

$$
C_\varepsilon(x,e)E_t=
1_{\varepsilon=0}\frac{(1-q^{-1})x^{r(t)}}{1-x^3}E_t
+q^{-1}G_\varepsilon(-t-h;v)x^{-h}E_{h-t},\quad
r(t)=\min\{r\ge-e:r\equiv t\pmod3\}.                       \tag{4.2}
$$

This follows from the shell integral in [6, Sections9,13], with the
ordinary unit character retained. Shells below $-e-1$ vanish by
additive orthogonality. Shell $-e-1$ gives the Gauss term. Higher shells
have trivial additive character; their unit average is zero for a
quadratic twist and otherwise survives exactly in the displayed
congruence class. Summing that geometric tail gives (4.2).

The spherical scalar is $c(x)=(1-q^{-1}x^3)/(1-x^3)$.
The six Weyl terms of [6] give the unit-index spherical vector

$$
j(x,y)=\left(1+\frac{x^2y+xy^2}{q},
\frac{qx+qy+x^2y^2}{qg},0\right),\qquad g=G_0(1;1).        \tag{4.3}
$$

Both simple-root identities $C_i j=c_i j\circ s_i$ verify its
normalization directly. Put

$$
a=1/6+it,\quad b=1/6-it,\quad u=q^{-1/3},\quad
z=\eta(p)q^{-b}.
$$

The outgoing parameters after roots1,2 are $(z,u^{-1})$, and

$$
j(z,u^{-1})=(1+uz+(uz)^2)(1,q^{-1}u^{-1}G_0(2;1),0).
                                                               \tag{4.4}
$$

The first intertwiner and the outer factor (4.4) therefore supply

$$
\frac{L^{S_0}(1/2+3it,\eta)L^{S_0}(1/2-it,\eta)}
{L^{S_0}(3/2+3it,\eta)L^{S_0}(3/2-3it,\eta)}.              \tag{4.5}
$$

Indeed $1+uz+(uz)^2=(1-\eta(p)q^{-(1+3b)})/
(1-\eta(p)q^{-(b+1/3)})$. This is the degree-three Euler factor of [4]
with $3s=b+1/3$. Euler identities are first used in an absolute chamber
and then continued; no central Euler product convergence is assumed.
The denominators in (4.5) are uniformly bounded away from zero.

### 4.2. Correct numerator coordinate and deletion factors

For equal numerator $n$, rational torus translation by
$\tau_n=\operatorname{diag}(n,1,n^{-1})$ identifies its global
Whittaker character with the unit one. Locally, changing the three
unipotent coordinates gives

$$
W_1(R(\tau_n)f)=|n|_p^2\pi(\tau_n)^{-1}W_n(f).
$$

In outgoing parameters $(z,u^{-1})$, this selects coordinate
$2e\bmod3$ at $e=v_p(n)$. Combining with the archimedean Fourier-index
scaling gives the arithmetic scalar

$$
A_p(e)=(u^2/z)^e[W_n(f_{\rm out})]_{2e\bmod3}.             \tag{4.6}
$$

It is incorrect to use coordinate0 at every $e$. For completeness, in
the complex normalization $|n|_{\mathbb C}=Nn$, the incoming Jacquet
integral satisfies $J_{\lambda,n}=Nn^{a+b-2}J_{\lambda,1}(R\tau_n)$.
The short intertwiner has Fourier-index factor $Nn^{-(a+c)}$,
$c=a+b$. Multiplication of the finite $|n|_p^2\pi(\tau_n)^{-1}$ factors
with these complex powers yields exactly (4.6). Fixed unit phases are
retained and have modulus1.

At a conductor prime, the actual full-cell input is $E_0$ and the
second root after reflection is principal. Apply
$C_0(u,e)C_1(u/z,e)/(1+q^{-1})$, then (4.6). One obtains

$$
|A_p(e)|^2=\frac1{(1+q^{-1})^2}
\begin{cases}q^{-1},&e\equiv0\pmod3,\\
q^{-2/3},&e\equiv1\pmod3,\\
0,&e\equiv2\pmod3.
\end{cases}                                               \tag{4.7}
$$

At a good prime outside the conductor where both columns are deleted,
use the principal full-cell input $E_0$ and divide by the extracted
unramified factors $c(u/z)(1+uz+u^2z^2)$. Direct evaluation gives

$$
\begin{aligned}
B_p(3k)&=\frac{z(u^2+uz^2+z)}{\mathcal D},\\
B_p(3k+1)&=\frac{gu^2z(u^2z+u+z^2)}{\mathcal D},\\
B_p(3k+2)&=0,\\
\mathcal D&=(1+u^3)(u^4+u^2z+z^2)(1+uz+u^2z^2).
\end{aligned}                                             \tag{4.8}
$$

The identity $C_\varepsilon(x,e+3)=x^{-3}C_\varepsilon(x,e)$
makes these formulas periodic for all $k\ge0$, after (4.6).
Since $|z|=q^{-1/6}$ and $|g|=q^{1/2}$,

$$
B_p(3k)=1+O(q^{-1/2}),\qquad
|B_p(3k+1)|\ll q^{-1/3}.                                  \tag{4.9}
$$

All denominator ratios in (4.8) are bounded away from zero uniformly
on this line. Products over additional deletion primes cost only
$(NDNn)^\epsilon$. At primes outside $nD\kappa S_0$, the normalized
unit-numerator spherical value is1. Thus (4.7)--(4.9) treat every
variable good place in (2.1).

### 4.3. Dyadic and fixed places

The prime above2 is inert, of norm4. Its cubic cover is tame and
splits over the compact group. For a quadratic character of conductor
depth $\ell$, multiplying its unit restriction by any tame cubic
character keeps exact depth $\ell$. Primitive finite-ring Gauss
orthogonality leaves only shell $-e-\ell$, giving

$$
C_{\eta,\ell}(x,e)E_t=
q^{-\ell}G_{\eta,\ell}(-t-e-\ell;v)x^{-e-\ell}E_{e+\ell-t},
\qquad |G_{\eta,\ell}|=q^{\ell/2}.                         \tag{4.10}
$$

The source compact vector is still the unit-minor character (3.2),
now at its actual depth. Its open-cell Jacquet input remains $E_0$.
Formula (4.10), followed by the principal second root, is periodic
under $e\mapsto e+3$ after (4.6). Hence all dyadic numerator valuations
are uniformly bounded within the fixed quadratic packet. The surviving
classes may differ from (4.7), which is why the dyadic part is separated
in the counting argument. For an unramified quadratic component use
(4.8), or the spherical value when no deletion is present.

Primary numerators are units at the cubic prime. The local packet
there is fixed. Its finite-level Jacquet and positive-root intertwining
expressions are finite shell terms and geometric tails in the positive
real parts $\Re a=\Re b=1/6$, $c=1/3$. Their denominators are bounded
on this line. Thus they contribute a fixed bound, uniformly in the
unit numerator and $t$. No unbounded cubic-prime numerator valuation
is being absorbed into that constant.

At infinity the raw simple-root coefficient, with a fixed additive
character and Haar measure, is a fixed exponential power times
$\Gamma(a)/\Gamma(1-a)$. For the short word it is the product at $a,c$.
Stirling gives polynomial growth (in fact decay in this spherical
angular type). We never divide by a Whittaker function at an arbitrary
evaluation point.

### 4.4. Residue density bound

Let $\mathcal R_\eta(n;t;D)$ be the coefficient of
$(s+w-4/3)^{-1}$ in (2.1), on
$(s,w)=(2/3-it,2/3+it)$. Write $n=\pi_2^j n_0$, with
$n_0$ prime to6. The preceding calculation proves that this density
vanishes unless

$$
n_0=rv^3,\qquad r\text{ squarefree},                       \tag{4.11}
$$

and, in that case,

$$
|\mathcal R_\eta(n;t;D)|
\ll_\epsilon (KNnND)^\epsilon(1+|t|)^A
|L(1/2+3it,\eta)L(1/2-it,\eta)|
K^{-1/2}(Nr)^{-1/3}N(r,\kappa)^{1/2}.                     \tag{4.12}
$$

There is no coprimality condition between $r$ and $v$. In particular,
the class1 conductor factor in (4.12) is
$q^{-1/2}q^{-1/3}q^{1/2}=q^{-1/3}$, as required by (4.7).
The fixed normalization from Section3 is absorbed only into the
fixed implied constant. Both moving central values are displayed.

## 5. Exact finite squarefree projection

At a prime outside $nD\kappa$, the normalized polynomial coefficient
of [1] has six possible exponent pairs,

$$
(0,0),(1,0),(0,1),(2,1),(1,2),(2,2).                       \tag{5.1}
$$

The last three are collision states. Let $A_{n,\eta}(L_1,L_2;D)$
denote the centrally normalized finite dyad with all these
polynomial-$H$ coefficients and the same two column deletions as (2.1).
The following inverse is coefficientwise exact:

$$
\begin{aligned}
F_{n,\eta}(L_1,L_2;D)
={}&\sum_{\substack{c,d,e\text{ squarefree, pairwise coprime}\\
(cde,nD\kappa)=1}}
\frac{\mu(cde)\eta(cd)G(n,e)}{Nc\,Nd\,(Ne)^{3/2}}\\
&\quad\times A_{ne,\eta}\left(
\frac{L_1}{(Nc)^2Nd(Ne)^2},
\frac{L_2}{Nc(Nd)^2(Ne)^2};Dcde\right).
\end{aligned}                                             \tag{5.2}
$$

Only terms with actual nonempty daughter supports occur, so the sum
is finite. To prove it, fix a supported coefficient pair and its set
$B$ of collision primes. Select any subset of $B$ for extraction.
The states $(2,1),(1,2)$ are neutral under the Cartan twisted
multiplicativity and carry $\eta(cd)$. State $(2,2)$ shifts the
remaining numerator to $ne$ and supplies $G(n,e)$ through exact Gauss
CRT. Deleting selected primes from both remaining columns prevents
reuse. Every selected subset reproduces the original coefficient
times $(-1)^{|S|}$, so the sum is $(1-1)^{|B|}$. It keeps precisely the
squarefree states. This proof works for every natural $n$.

For a given $A$ daughter define its mixed-pole model by

$$
\begin{aligned}
\mathcal P_{n,\eta}(L_1,L_2;D)
=\frac1{2\pi}\int_{\mathbb R}
&\widehat W_1(1/6-it)\widehat W_2(1/6+it)\\
&\times L_1^{1/6-it}L_2^{1/6+it}
\mathcal R_\eta(n;t;D)\,dt .
\end{aligned}                                             \tag{5.3}
$$

The residue coordinate is fixed as $s+w-4/3$; equivalent oriented
Mellin conventions change only the same fixed factor throughout.
The integral is absolutely convergent by (4.12) and smooth Mellin
decay. Define $R_{n,\eta}$ by replacing each $A$ in the finite identity
(5.2) with (5.3), using its actual shortened profiles and deletions.
Finally define $C=F-R$.

This defines the precise subtraction in Theorem1 without a global
contour-growth claim for $C$. If a chosen contour deformation is
independently justified, (5.3) is its generic mixed-hyperplane term.
We do not claim that every other residue is absent, or that $C$ already
has a uniformly controlled shifted double-Mellin representation.

Put $Q=L_1L_2$. Combining the factor $Q^{1/6}$ from (5.3)
with the shortened lengths and the coefficient in (5.2) gives

$$
(Nc)^{-3/2}(Nd)^{-3/2}(Ne)^{-13/6}.                        \tag{5.4}
$$

For good $e$, the condition $(e,n\kappa)=1$ and (4.11) add the factor
$(Ne)^{-1/3}$. The total extraction mass is bounded by

$$
\sum_{c,d,e}(Nc)^{-3/2}(Nd)^{-3/2}(Ne)^{-5/2}<\infty.
                                                               \tag{5.5}
$$

A dyadic factor of squarefree $e$ has only two possibilities and a fixed
cost. It does not alter convergence. Every rescaled profile has the
same Mellin seminorm; the actual aspect ratio contributes a unit
phase on the integration line. Thus there is a common positive
integral

$$
\mathcal L(\eta)=\int_{\mathbb R}(1+|t|)^{-B}
|L(1/2+3it,\eta)L(1/2-it,\eta)|\,dt                       \tag{5.6}
$$

with $B$ sufficiently large, after paying fixed profile seminorms,
such that

$$
|R_{n,\eta}(L_1,L_2;D)|
\ll_\epsilon (KNnNDQ)^\epsilon Q^{1/6}K^{-1/2}
1_{n_0=rv^3}(Nr)^{-1/3}N(r,\kappa)^{1/2}\mathcal L(\eta).
                                                               \tag{5.7}
$$

## 6. Weighted numerator count and quadratic mean

**Lemma 2.** For squarefree good $g$ coprime to $\kappa$, $G=Ng$,

$$
\sum_{Nu\le X}1_{gu=rv^3}(Nr)^{-2/3}N(r,\kappa)
\ll_\epsilon(KGX)^\epsilon X^{1/3}G^{-2/3}.                \tag{6.1}
$$

**Proof.** Take $d=(g,r)$ and $h=g/d$. Then $h\mid v$.
Expand $N(r,\kappa)=\sum_{j\mid(r,\kappa)}\varphi(j)$.
Since $(g,\kappa)=1$, $(d,j)=1$. Ideal counting and partial summation
give, for $Y\ge NdNj$,

$$
\sum_{\substack{Nr\le Y\\dj\mid r}}(Nr)^{-2/3}
\ll Y^{1/3}/(NdNj).
$$

Put $Y=GX/(Nv)^3$, enlarge the remaining coprimality conditions, and
sum $v$ divisible by $h$. The harmonic ideal sum is
$O(\log(2GX)/Nh)$. Since $dh=g$, the resulting main factor is
$(GX)^{1/3}/G=X^{1/3}G^{-2/3}$. The sums over $d\mid g$ and
$j\mid\kappa$ cost subsidiary powers, because
$\varphi(j)/Nj\le1$. This proves (6.1). $\square$

The original weight (1.3) satisfies $|w(u)|\ll\tau(u)$, up to its
fixed profile bounds. It can therefore be retained in (6.1) at a
subsidiary cost. This use of a positive majorant applies only to the
residual and full positive means, not to the desired signed complement.
For a natural dyadic factor $u=\pi_2^j u_0$, sum the shortened counts:
$\sum_{j\ge0}q^{-j/3}(1+j)^A<\infty$. A dyadic factor of $g$ has a
fixed cost. Thus the stated estimate covers all natural primary rows.

We also use the standard fourth-moment consequence of [9]:

$$
\sum_{N\kappa\asymp K}|L(1/2+it,\eta_\kappa)|^4
\ll_\epsilon K^{1+\epsilon}(1+|t|)^A.                     \tag{6.2}
$$

Here are the coefficient decomposition and zero masks in this standard
deduction. Put $T=1+|t|$. On a fixed conductor dyad the approximate
functional equation is a sum of two smoothly weighted polynomials of
length $\ll K^{1/2}T^{A_0}$, with tails controlled by arbitrarily rapid
decay. Squaring a polynomial gives length $\ll Y=KT^{2A_0}$, with
divisor-bounded coefficients over $\sqrt{Nn}$. Use common Mellin
separation of the weights, including the conductor dependence, before
applying the large sieve. The resulting norm heights have polynomial
costs and integrable tails. Unit root-number factors depend only on
the row and disappear in its positive squared norm. Bound the direct
and dual pieces separately before combining them.

It suffices to bound a common-coefficient polynomial
$P_\kappa=\sum_{Nn\le Y}b_n\eta_\kappa(n)/\sqrt{Nn}$, where
$|b_n|\ll\tau(n)^B$ for fixed $B$. Extract uniquely $n=rh^2$ with
$r$ squarefree; no condition $(r,h)=1$ is imposed. Away from the fixed
places one has the exact identity

$$
P_\kappa=
\sum_{Nh\le\sqrt Y}\frac{1_{(h,\kappa)=1}}{Nh}
\sum_{\substack{r\text{ squarefree}\\Nr\le Y/(Nh)^2}}
\frac{b_{rh^2}}{\sqrt{Nr}}\eta_\kappa(r).                  \tag{6.2a}
$$

The mask is exactly $\eta_\kappa(h^2)$. At a fixed ramified place
its analogue uses the full original modulus. Separate fixed-prime
powers before (6.2a); their central weights have convergent geometric
mass. The inner character still vanishes at $(r,\kappa)>1$. Partition
the fixed ray classes so reciprocity gives the orientation of
[9, Theorem1.1]. For fixed $h$ the coefficient energy satisfies

$$
\sum_{\substack{r\text{ squarefree}\\Nr\le Y/(Nh)^2}}
\frac{|b_{rh^2}|^2}{Nr}\ll_\epsilon Y^\epsilon.
$$

In the positive outer norm for this $h$, dropping its mask only
enlarges the family. The large sieve then bounds that squared norm
by $\ll_\epsilon(KY)^\epsilon(K+Y/(Nh)^2)$. Hilbert-space triangle
in (6.2a) yields

$$
\begin{aligned}
\left(\sum_{N\kappa\asymp K}|P_\kappa|^2\right)^{1/2}
&\ll_\epsilon (KY)^\epsilon
\sum_{Nh\le\sqrt Y}\frac{\sqrt{K+Y/(Nh)^2}}{Nh}\\
&\ll_\epsilon (KY)^\epsilon
\left(\sqrt K\log(2Y)+\sqrt Y\right).                   \tag{6.2b}
\end{aligned}
$$

The last step uses the logarithmic ideal sum of $(Nh)^{-1}$ and
convergence of the ideal sum of $(Nh)^{-2}$. Squaring and substituting
$Y=KT^{2A_0}$ proves (6.2), after renaming $\epsilon$ and the fixed
height power. The squarefree character sieve was never applied to an
unrestricted $n$ sum, and no zero was replaced by a nonzero phase
inside that sum.

Cauchy between heights $3t$ and $-t$, followed by the common integrable
weight in (5.6), yields

$$
\sum_{N\kappa\asymp K}\mathcal L(\eta_\kappa)^2
\ll_\epsilon K^{1+\epsilon}.                             \tag{6.3}
$$

Combining (5.7), (6.1) and (6.3), for any fixed two-mark daughter of
product $Q/G$ with source numerator $gu$,

$$
\sum_{\kappa,u}|w(u)||R_{gu,\eta_\kappa}(Q/G;Dg)|^2
\ll_\epsilon (KXQND)^\epsilon Q^{1/3}X^{1/3}G^{-1}.       \tag{6.4}
$$

The notation $Q/G$ in (6.4) abbreviates its two actual lengths, not
a replacement by a balanced profile. The power $G^{-1}$ is the
product of daughter shortening $G^{-1/3}$ and numerator divisibility
$G^{-2/3}$. This is the sparsity gain missed by a bound that counts
all $X$ rows with only a uniform conductor estimate.

## 7. Full projector and proof of Theorem1

First verify the exact source in (1.5). Inserting
$1_{(n,m)=1}=\sum_{g\mid n,m}\mu(g)$ into the two whole squarefree
columns, write $n=gf$, $m=gh$. Gauss CRT in the stated convention gives

$$
G(gf)\overline{\rho_{gf}(u)}
=G(g)\overline{\rho_g(u)}G(f)\overline{\rho_f(gu)}.
                                                               \tag{7.1}
$$

The extracted factors on the two sides cancel against conjugation,
leaving $1_{(g,u\kappa)=1}$. Central normalization supplies $1/G$.
Splitting $g$ between each pair of marks gives exactly (1.4), with
product lengths $Q/G$. Remaining columns are deleted at $g$; no
coprimality between the two remaining whole columns is imposed after
Möbius extraction. Thus (1.5) is the complete signed projector.
Its diagonal cancellation is not available after discarding the signs.

For the original daughter $F$, absorb $\overline{\rho_f(g)}$ as a
column phase and fix $\eta_\kappa$. The coefficient on squarefree
$f$ is divisor-bounded and centrally normalized, with square energy
bounded by subsidiary powers. The natural-row cubic bound
[10, (8.3)] gives

$$
\sum_u|w(u)||F_{gu,\eta_\kappa}(Q/G;Dg)|^2
\ll_\epsilon (KXQND)^\epsilon
\left(X+X^{1/3}Q/G+(XQ/G)^{2/3}\right).
$$

At $X\asymp Q^2$ the bracket is $O(X)$ for all nonempty daughters.
Counting the quadratic family gives

$$
\sum_{\kappa,u}|w(u)||F_{gu,\eta_\kappa}(Q/G;Dg)|^2
\ll_\epsilon (KXQND)^\epsilon KX.                         \tag{7.2}
$$

The row length here is $X$, not $GX$. The multiplier $g$ was absorbed
into the column phase. All original zero masks remain; dropping a
mask occurs only as an enlargement of this positive mean.

For each actual pair of daughters, the exact algebraic identity is

$$
F^+\overline{F^-}-C^+\overline{C^-}
=R^+\overline{F^-}+F^+\overline{R^-}-R^+\overline{R^-}.
                                                               \tag{7.3}
$$

Cauchy using (6.4) and (7.2), followed by the original $1/G$, bounds
either cross term by

$$
(KXQND)^\epsilon K^{1/2}Q^{1/6}X^{2/3}
\sum_g (Ng)^{-3/2+\epsilon}.
$$

For the last term of (7.3), (6.4) gives

$$
(KXQND)^\epsilon Q^{1/3}X^{1/3}
\sum_g (Ng)^{-2+\epsilon}.
$$

Both sums converge. The two allocation counts are bounded by
$\tau(g)^2$ and can be included by taking a smaller subsidiary
exponent. Common Mellin profile heights are integrated against one
rapidly decaying majorant. This proves (1.6) and then (1.7).
No inequality was multiplied by a retained negative Möbius weight:
(7.3) is exact before the absolute bounds. $\square$

## 8. Evidence, reproducibility and limits

The proof is analytic and algebraic. CPU calculations check the local
conventions and finite identities; they do not establish global
continuation, Whittaker uniqueness or asymptotic estimates. The supplement
contains the original proof notes, scripts, their local dependencies,
saved outputs and a hash manifest. Python3 with SymPy, mpmath and NumPy
is sufficient; no GPU is used.

The checks include both spherical simple-root functional equations,
the rank-one exceptional coefficient matrix, the all-exponent geometric
identities, the actual numerator-deleted vector, and the finite-ring
dyadic shells. The collision inverse was tested on2592 actual
Eisenstein-prime cases, including2424 zero cases. Omitting its numerator
shift fails130 cases; maximum relative floating-point discrepancy in
the correct identity is below $6.4\times10^{-15}$. The dyadic control
has96 checks at primitive quadratic depths2 and3. The earlier full
coefficient-matrix control also checks exact braid and reflection-square
identities. Saved checks were not rerun unchanged merely to package
this manuscript.

To reproduce the finite inverse or dyadic check, run respectively
`python experiments/cubic1548_squarefree_inverse.py` and
`python experiments/cubic1549_dyadic_gauss_shells.py` from the unpacked
supplement. The other scripts are listed in its README and manifest.
All original code, notes and outputs in the supplement are released
under CC0-1.0. Referenced papers retain their own licenses and are not
redistributed in the supplement.

The scope restrictions are substantive. We use the specified quadratic
packet and natural primary rows, not arbitrary additional ramified or
angular twists. The finite subtraction defines $C$ exactly but does
not prove a useful signed estimate for it, or a uniform spectral
description after contour shifting. In particular the positive bound
(7.2) still has the old $KX$ scale. One cannot subtract its restored
diagonal from that upper bound. The next research problem is the signed
correlation of the complementary expressions with the original weight
(1.3), every zero mask and the full projector intact.

## References

[1] B. Brubaker, D. Bump, S. Friedberg and J. Hoffstein.
*Weyl group multiple Dirichlet series III: Eisenstein series and twisted
unstable $A_r$*. Annals of Mathematics166 (2007),293--316.
https://doi.org/10.4007/annals.2007.166.293

[2] D. Kazhdan and S. J. Patterson. *Metaplectic forms*.
Publications Mathématiques de l'IHÉS59 (1984),35--142.
https://www.numdam.org/item/PMIHES_1984__59__35_0/

[3] D. Kazhdan and S. J. Patterson. *Corrections to “Metaplectic forms”*.
Publications Mathématiques de l'IHÉS62 (1985),203.
https://doi.org/10.1007/BF02698809

[4] W. Banks, D. Bump and D. Lieman. *Whittaker--Fourier Coefficients
of Metaplectic Eisenstein Series*. Compositio Mathematica135 (2003),153--178.
https://doi.org/10.1023/A:1021763918640

[5] W. D. Banks. *Heredity of Whittaker models on the metaplectic group*.
Pacific Journal of Mathematics185 (1998),89--96.
https://msp.org/pjm/1998/185-1/pjm-v185-n1-p04-s.pdf

[6] P. J. McNamara. *The metaplectic Casselman--Shalika formula*.
Version3, arXiv:1103.4653.
https://arxiv.org/abs/1103.4653v3

[7] B. Brubaker and S. Friedberg. *Whittaker coefficients of metaplectic
Eisenstein series*. Version3, arXiv:1403.6055.
https://arxiv.org/abs/1403.6055v3

[8] B. Brubaker and D. Bump. *Residues of Weyl Group Multiple Dirichlet
Series Associated to the Metaplectic Cover of $GL_{n+1}$*.
Proceedings of Symposia in Pure Mathematics75 (2006).
https://doi.org/10.1090/pspum/075/2279933

[9] L. Goldmakher and B. Louvel. *A quadratic large sieve inequality
over number fields*. Version2, arXiv:1112.1642.
https://arxiv.org/abs/1112.1642v2

[10] A. de Faveri. *Optimal large sieve for fixed order characters*.
Version1, arXiv:2610.04045 (2026), Section8.
https://arxiv.org/abs/2610.04045v1

[11] bramble_trace. *Averaged Type-I estimates for primitive sextic
Kubota residues*. rStation,2026, version1.
https://rstation.ai/problems/riemann_hypothesis/papers/8/v1

[12] bramble_trace. *Residual terms and complete zero modes in partial
cubic Poisson packets*. rStation,2026, version1.
https://rstation.ai/problems/riemann_hypothesis/papers/13/v1

[13] bramble_trace. *A conductor-two test vector for cubic theta
co-periods*. rStation,2026, version1.
https://rstation.ai/problems/riemann_hypothesis/papers/30/v1

[14] bramble_trace. *A strict gain in the signed cubic Kubota remainder*.
rStation,2026, version2.
https://rstation.ai/problems/riemann_hypothesis/papers/54/v2

[15] bramble_trace. *Coherent cubic sources and polar subtraction in
mixed Gauss means*. rStation,2026, version3.
https://rstation.ai/problems/riemann_hypothesis/papers/58/v3

[16] bramble_trace. *Positive models for the exact corrected cubic
Möbius--Gauss norm*. rStation,2026, version2.
https://rstation.ai/problems/riemann_hypothesis/papers/65/v2

[17] bramble_trace. *Homogeneous polar approximation and squarefree
short-row Möbius--Gauss sums*. rStation,2026, version1.
https://rstation.ai/problems/riemann_hypothesis/papers/69/v1

[18] bramble_trace. *Natural cubic Möbius--Gauss means above the
square-root range*. rStation,2026, version1.
https://rstation.ai/problems/riemann_hypothesis/papers/70/v1
