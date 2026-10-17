# Recognition and arithmetic geometry of anchored order-five Diophantine cycles

## 1. The anchored recognition problem

A rational Diophantine tuple consists of distinct nonzero rational numbers whose pairwise products, increased by one, are rational squares. Consider two anchors $a,b$ and five tails $x_0,\ldots,x_4$, indexed cyclically. Requiring the anchor edge, the ten anchor–tail edges, and the five adjacent tail edges gives sixteen of the twenty-one conditions for a septuple. The five tail diagonals remain independent requirements.

The forward construction in [1] produces these sixteen roots from an order-five elliptic correspondence, with explicit matching and anchor lifts. This paper gives an inverse recognition criterion, determines the full matching classes on an inhabited fiber, and determines the anchor group over its universal product-lift field. The last result shows that the simplest moving base supports only degenerate anchors, although an inhabited rational fiber has three independent free group directions. Version 2 of [1] incorporates our split-cover description of the matching surface with attribution; we include its proof to fix the torsor and deck conventions used in the arithmetic below. The uniform nonisogeny theorem and the exclusion of curves of genus at most one defined over $\mathbb Q$ from the fixed-product completion divisor strengthen its geometric restrictions.

Bare circular Diophantine tuples already admit rational parametrizations: Lasić's appendix to [2] recovers them from individually chosen adjacent roots. Our recognition question is more restrictive: when does a rooted five-cycle belong to the anchored order-five source of [1]? The new criterion is a consistent fit by five linear equations, followed by the separate arithmetic lifts. The abelian surface below is also different from the Kummer surface in [3]: its defining quotient is a free translation, whereas a Kummer quotient uses negation.

For clarity, the sufficient completion condition used in [1] is
$$
R_5=(e_1-e_5)^2-4(1+e_2+e_4)=0,                 \tag{1}
$$
where $e_j$ are the elementary symmetric functions of the tails. If
$$
N_i=x_i+x_{i+1}+x_{i+2}-x_{i+3}-x_{i+4}
       +2x_ix_{i+1}x_{i+2}+e_5,
$$
then
$$
N_i^2-R_5=4(1+x_ix_{i+1})(1+x_{i+1}x_{i+2})
                 (1+x_{i+3}x_{i+4})(1+x_ix_{i+2}).
$$
Thus, when the denominator is nonzero, $N_i/(2c_ic_{i+1}c_{i+3})$ supplies the missing root. Equation (1) is sufficient, not asserted necessary for all possible septuples. No nondegenerate rational completion point is obtained here.

## 2. Five linear equations recognize the source

Fix distinct nonzero $x_i\in\mathbb Q$ and individual roots
$c_i^2=1+x_ix_{i+1}$. Define
$$
\mu_i=\frac{c_i+1}{c_i-1},\qquad
G=\frac{\prod_i(c_i+1)}{\prod_i x_i}.
$$
The hypotheses give $c_i\ne\pm1$, and $\prod\mu_i=G^2$. All cyclic solutions of $q_iq_{i+1}=\mu_i$ are
$$
q_0=\varepsilon\frac{G}{\mu_1\mu_3},\qquad
q_{i+1}=\frac{\mu_i}{q_i},\qquad \varepsilon=\pm1.       \tag{2}
$$
The product identity is used only to recover the odd-cycle coordinate. Every $c_i$ is already an individual rational root; nothing here replaces the five edge conditions by one condition on their product.

**Theorem 1 (exact recognition).** For each vector (2), the system
$$
L(q_i^2+1)-2Sq_i+2k=\frac{4q_i}{x_i},\qquad 0\le i<5,  \tag{3}
$$
has at most one solution. A consistent solution with $pL\ne0$, where
$$
p=\frac{S^2-L^2-2kL}{4},\qquad u_i=S-Lq_i,              \tag{4}
$$
recovers exactly a cycle in the finite source
$$
x_i=\frac{4(S-u_i)}{u_i^2-4p},\qquad
L^2(u_i^2-4p)(u_{i+1}^2-4p)
 =4\bigl((S-u_i)(S-u_{i+1})-L^2\bigr)^2.               \tag{5}
$$
Conversely, every cycle in this chart is recovered from its cyclic order and root signs. Consistency is equivalent to two quadratic-interpolation residuals.

**Proof.** If two $q_i$ coincide, consistency in (3) forces the corresponding nonzero tails to coincide. Otherwise any three rows have determinant
$4(q_1-q_0)(q_2-q_0)(q_2-q_1)\ne0$. Interpolate a quadratic through three points $(q_i,4q_i/x_i)$. Its coefficients are $(L,-2S,L+2k)$; the other two evaluations are precisely the residual tests. There is no consistent rank-deficient family.

Writing $D_i=u_i^2-4p$, equations (3)–(4) give
$$
D_i=\frac{4Lq_i}{x_i}\ne0,\qquad
c_i=\frac{q_iq_{i+1}+1}{q_iq_{i+1}-1}.
$$
These identities imply both equations (5). Reversing the calculation proves the converse. For an unordered input one retains its twelve cyclic orders up to rotation and reversal, every individual edge-root sign, and both signs in (2). This is a finite recognition procedure, not a parameter search. $\square$

Define the signed transport
$$
B_i=\frac{4L}{c_i-1},\qquad B_i^2=D_iD_{i+1},\qquad
\prod_i\frac{B_i}{D_i}=\varepsilon.                    \tag{6}
$$
Positive closure means $\varepsilon=1$. Arithmetic recognition additionally requires the three separate lifts
$$
r^2=p+1,\qquad d_a^2=S^2-4p,\qquad \delta_0^2=D_0.    \tag{7}
$$
Set $a,b=(S\pm d_a)/2$ and propagate $\delta_{i+1}=B_i/\delta_i$. The sixteen individual roots are
$$
r,\qquad \frac{u_i-2a}{\delta_i},\qquad
\frac{u_i-2b}{\delta_i},\qquad c_i.                     \tag{8}
$$
Indeed $1+ax_i=(u_i-2a)^2/D_i$, and similarly for $b$. The common squareclass of the $D_i$ need not be trivial; the last lift in (7) cannot be replaced by a product-square condition. For distinct anchors it is necessary whenever both anchor edges are squares.

Zero roots $c_i=0$ cause no failure in (2)–(8). They only require another chart for completion formulas dividing by them. Likewise a moving coordinate at infinity below can represent a finite nonzero tail. Zero entries, collisions, and actual poles of physical recovery remain separate exclusions. The certificate `order5_tail_inverse_review.py` verifies these identities and the independent recovery of the saved controls.

## 3. Positive closure forces the order-five normalization

**Theorem 2.** A rational cycle satisfying Theorem 1 with $pL\ne0$ and positive closure satisfies
$$
4kp=(k-1)(k+1)^2.                                      \tag{9}
$$
There is no singular rational exception with five distinct tail coordinates.

**Proof.** Let $B_L(u,v)$ be the difference of the two sides of (5). This symmetric curve has bidegree $(2,2)$ and no vertical or horizontal component. For a finite fiber, put $D=u^2-4p$, $h=S-u$, and $j=Sh-L^2$. Its coefficients in $v$ are
$$
L^2D-4h^2,\quad 8hj,\quad -4pL^2D-4j^2.
$$
Their simultaneous vanishing contradicts $pL\ne0$, whether $D=0$ or not. At infinity the fiber polynomial is
$(L^2-4)v^2+8Sv-4pL^2-4S^2$, with the same conclusion.

There are therefore at most two geometric components. At each cycle state the neighboring coordinates give two distinct fiber roots, so that state is smooth and the root-exchange successor is defined. If the curve were singular or reducible, its component would normalize to a genus-zero curve. A smooth rational point makes that component rationally defined, and an odd five-cycle prevents the successor from exchanging two components. Its normalization is $\mathbb P^1$, carrying a rational Möbius transformation with a five-cycle. Such a transformation has projective order five; its rational invariant $\tau=\operatorname{tr}(M)^2/\det(M)$ would satisfy $\tau^2-3\tau+1=0$, impossible over $\mathbb Q$.

Consequently the correspondence is smooth. Put $t=S-L$ and
$$
U=\frac{tu-4p}{t-u}.
$$
The exceptional possibility $t=k$ would give $p=k^2/4$ and a singular point $(u,v)=(k,k)$. Thus the projective change has nonzero determinant $t^2-4p=-2L(t-k)$. It transforms (5) into
$$
(U^2-4p)(U'^2-4p)=4(U+U'+2k)^2.                        \tag{10}
$$
Choose $\zeta_i^2=U_i^2-4p$, with $\zeta_i\zeta_{i+1}=2(U_i+U_{i+1}+2k)$. The exact identity
$$
\frac{2(U_i+U_{i+1}+2k)}{U_i^2-4p}
=\frac{B_i}{D_i}\frac{t+U_{i+1}}{t+U_i}
$$
identifies its transport multiplier with (6). Positive closure gives a closed five-cycle on the lifted genus-one curve.

For $z=(U+\zeta)/2$, its equation is
$$
y^2=(p+1)z^4+4kz^3+(4k^2-2p(p+1))z^2
                   +4kpz+p^2(p+1).                    \tag{11}
$$
More explicitly, the signed correspondence becomes
$$
(z^2-p)(z'^2-p)-2(z+z')(zz'+p)-4kzz'=0.
$$
Putting $A_z=z^2-2z-p$, $N_z=z^2+2kz+p$, and $y=A_zz'-N_z$ gives (11). For a quartic $y^2=az^4+bz^3+cz^2+ez+\eta^2$, the coordinates
$$
X=\frac{2\eta(y+\eta)+ez}{z^2},\qquad
Y=\frac{(X^2-4\eta^2a)z-eX-2\eta^2b}{2\eta}
$$
give the required cubic model. Applying them with $\eta=pr$ and then shifting $x=X+2p(p+1)$ gives (12).

The two root-exchange involutions are reflections; their composition is translation. Taking $(0,pr)$ as origin, where $r^2=p+1$ over algebraic constants, the translation point becomes
$$
Q_5=(4p(p+1-k),8kp(p+1-k))
$$
on
$$
E_C':y^2=x\bigl(x^2+(4k^2-8p(p+1))x
                    +16p^2((p+1)^2-k^2)\bigr).         \tag{12}
$$
The successor of the chosen origin has $z=-1-r$ and $y=N_z(-1-r)$. Substituting it into this map identifies the translation, not just a point on the cubic. These identities are certified in `order5_normalization_implication.py`. In the exceptional chart $p=-1$, (11) is $y^2=4kz(z^2+kz-1)$; the map $(x,y_c)=(4kz,4ky)$, followed by changing origin from $(0,0)$, gives translation by $-Q_5$.

Direct division-polynomial evaluation on (12) gives
$$
\psi_5(Q_5)=-2^{30}k^6p^9(p+1-k)^6
                 \bigl(4kp-(k-1)(k+1)^2\bigr).        \tag{13}
$$
Smoothness excludes all prefactor zeros: the cubic discriminant is
$2^{16}k^2p^4(k^2-4p)((p+1)^2-k^2)^2$. A closed lifted cycle forces $5Q_5=O$, so (13) gives (9). Conversely (9) gives exact order five on the smooth lifted source. Distinct physical tails still require their own check. $\square$

Changing $(q,L,k)$ to $(-q,-L,-k)$ preserves $u,p,S$ but reverses (6). Negative closure therefore gives $p=p_5(-k)$, where
$$
p_5(k)=\frac{(k-1)(k+1)^2}{4k}.
$$
Squared closure alone does not distinguish these normalizations.

## 4. The matching normalization and its global deck

Henceforth take $p=p_5(k)$, $r^2=p+1$, and rational $k\ne0,\pm1$. Write
$$
q=4p,\quad \Delta=k^2-q,\quad
A(z)=z^2-q,\quad B(U)=(p+1)U^2+4kU+4k^2-q(p+1),
\quad C(t)=(t-2k)^2-q.
$$
The source and anchor bases are
$$
E_C:V^2=A(U)B(U),\qquad E_A:\bar d^2=A(t)C(t),          \tag{14}
$$
with split covers
$$
E_C':z_C^2=A(U),\ w_C^2=B(U),\qquad
E_A':z_A^2=A(t),\ w_A^2=C(t).                           \tag{15}
$$
All denote smooth projective curves. Their branch sets are disjoint, since
$\operatorname{Res}(A,B)=\operatorname{Res}(A,C)=16k^2\Delta$.
After normalization, further discriminant factors are $k^2-k-1$ and $k^2+4k-1$, neither with rational roots. Thus the stated rational range is smooth.

**Theorem 3 (matching surface).** The normalization of $E_C\times E_A$ obtained by adjoining $\gamma^2=A(U)A(t)$ is the abelian surface
$$
\mathcal S=(E_C'\times E_A')/
       \langle(\tau_C,\tau_A)\rangle,                  \tag{16}
$$
where each $\tau$ simultaneously changes its two root signs. Both arrows
$E_C'\times E_A'\to\mathcal S\to E_C\times E_A$ are degree-two isogenies.

**Proof.** Each curve in (15) is a connected degree-four cover of $\mathbb P^1$ with four simple branch values; Riemann–Hurwitz gives genus one. The simultaneous sign involution is fixed-point-free, including at infinity. Choose origins
$[1:-1:r:0]$ and $[1:-1:1:0]$, in coordinates $[U:z_C:w_C:W]$ and $[t:z_A:w_A:W]$. Their images are the negative infinity branches of (14). A fixed-point-free elliptic involution is translation by nonzero two-torsion. Quotienting their product by the diagonal translation proves the isogeny statement.

The invariant field is generated by
$U,t,V=z_Cw_C,\bar d=z_Aw_A,\gamma=z_Cz_A$. The three corresponding exponent vectors $1100,0011,1010$ generate all even-parity monomials, proving (16). The naive affine equations can be nonnormal at their boundaries; it is their normalization over the product that is abelian. $\square$

On the open with nonzero radicands, every rational matching point has one common squareclass
$$
\lambda=[A(U)]=[B(U)]=[A(t)]=[C(t)].                    \tag{17}
$$
It lifts to the shared covers $\lambda z_C^2=A(U)$, $\lambda w_C^2=B(U)$, $\lambda z_A^2=A(t)$, $\lambda w_A^2=C(t)$, with invariants multiplied by $\lambda$. Conversely these formulas recover every rational point of that class. These are torsors twisted by deck translations, so their Jacobians remain the original covers. They are not ordinary Weierstrass quadratic twists. Restricting to the untwisted product alone would lose rational matching points.

The matching equation alone is a rational conic over a fixed source coordinate. For $qA(U)\ne0$, put
$$
m=(s+q/s)/2,\quad n=(s-q/s)/2,\quad
t=\frac{mU+q}{m+U},\quad \gamma=\frac{nA(U)}{m+U}.
$$
Its signed inverse is $s=(q-tU-\gamma)/(t-U)$. Homogenizing in $s$ retains both diagonal points $t=U$, with $\gamma=\pm A(U)$, and the infinity charts. These maps are checked in `order5_full_matching_conic.py`, including the separate degenerate fibers when $A(U)=0$. Rationalizing this conic leaves the source equation and anchor equation in (14) to be satisfied. It therefore does not parametrize the full surface by rational functions or remove the arithmetic content of (17).

Recover physical data by
$$
S=\frac{t^2-2kt+q}{2(t-k)},\quad
a,b=\frac{S\pm\bar d/(2(t-k))}{2},\quad
x(U,t)=\frac{2((t-k)^2-(U+k)^2)}{(t-k)A(U)}.           \tag{18}
$$
The source recurrence of [1] is
$$
U'=\frac{4(U+2k)-2V}{U^2-4(p+1)},\qquad
V'=\frac{U(U'^2-4(p+1))}{2}-2(U'+2k).
$$
With $\beta=2(U+U'+2k)$, propagate $\gamma'=\gamma\beta/A(U)$. The order-five identity and positive radical closure generate the five tails. The finite coordinates $u=(tU+q)/(t+U)$, $\delta=\gamma/(t+U)$ recover (8). These formulas describe dense charts of the projective maps; their poles alone do not discard a rational physical point.

**Theorem 4 (signed physical deck).** The entry-preserving symmetry extends to translation by a rational point of exact order four on $\mathcal S$. On its affine chart it is
$$
\begin{aligned}
U^*&=-\frac{kU+q}{U+k},&V^*&=-\frac{\Delta V}{(U+k)^2},\\
t^*&=k-\frac{\Delta}{t-k},&\bar d^*&=\frac{\Delta\bar d}{(t-k)^2},\\
\gamma^*&=\frac{\Delta\gamma\bar d}{A(t)(U+k)(t-k)}.
\end{aligned}                                         \tag{19}
$$
It multiplies (17) by $[\Delta]$, swaps the anchors, and preserves the ordered tail cycle.

**Proof.** Substitution gives
$$
A(U^*)=\frac{\Delta A(U)}{(U+k)^2},\quad
B(U^*)=\frac{\Delta B(U)}{(U+k)^2},\quad
A(t^*)=\frac{\Delta C(t)}{(t-k)^2},\quad
C(t^*)=\frac{\Delta A(t)}{(t-k)^2}.
$$
Equations (18) show the stated entry action. The recurrence commutes with the source transformation; its edge transport transforms by
$\beta_i^*=\Delta\beta_i/((U_i+k)(U_{i+1}+k))$.

The global extension is explicit. In coordinate order $[U:W:z:w]$, the map from class $\lambda$ to class $\lambda\Delta$ is
$$
[U:W:z:w]\mapsto[-kU-qW:U+kW:z:-w],
$$
and on the anchor cover it is
$$
[t:W:z:w]\mapsto[kt+(q-2k^2)W:t-kW:w:z].
$$
Their base-coordinate matrices square to $\Delta I$ and $-\Delta I$; they are invertible and induce (19) on the quotient. Thus $U=-k\leftrightarrow\infty$, $t=k\leftrightarrow\infty$, and $A(t)=0$ are retained. In particular $x(-k,t)=2(t-k)/\Delta$ equals the transformed infinity-source value $-2/(t^*-k)$.

The two base involutions are fixed-point-free translations: a source fixed point would have $(U+k)^2=\Delta,V=0$, but
$$
\operatorname{Res}_U\bigl((U+k)^2-\Delta,A(U)B(U)\bigr)
=256p^2\Delta^2((p+1)^2-k^2)\ne0.
$$
An anchor fixed point would have $(t-k)^2=-\Delta,\bar d=0$, whereas $A(t)C(t)=4k^2\Delta\ne0$. Subtracting the image of the surface origin from (19) therefore induces the identity on the product base, and its difference from the identity maps into a finite kernel. It is constant, hence zero. The translation point is
$$
R=(-k,r\Delta,k,-\Delta,-\Delta).
$$
This point lies on the $t=k$ recovery boundary; its role is as a group translation. The second iterate fixes $U,V,t,\bar d$ and negates $\gamma$, proving exact order four. The symbolic and projective identities are recorded in `order5_full_source_abelian_surface.py`. $\square$

## 5. Complete arithmetic at an inhabited fiber

At
$$
k=25/31,\quad p=-4704/24025,\quad r=139/155,
\quad \Delta=34441/155^2,
$$
certified descent gives
$$
\operatorname{rank}E_C'=1,\quad E_C'(\mathbb Q)_{\rm tors}=C_{10},
\qquad
\operatorname{rank}E_A'=2,\quad E_A'(\mathbb Q)_{\rm tors}=C_4.       \tag{20}
$$
Here the anchor cover is
$$
E_A':y^2=x(x^2+(4k^2-8p)x+16p^2).                     \tag{21}
$$
The exact models, points, rank intervals, and torsion outputs are in `order5_full_source_group_arithmetic.json`. Both nontrivial descent fields have discriminant $34441$, class number two, and certified class/unit data (`bnfcertify=1`).

For $E:y^2=x(x^2+ax+b)$, let $\bar E$ be its standard two-isogenous quotient and put $\alpha(P)=[x(P)]$, with $\alpha(O)=1$, $\alpha((0,0))=[b]$. The identity [4]
$$
|\alpha(E)|\,|\alpha(\bar E)|=2^{\operatorname{rank}E+2}           \tag{22}
$$
proves completeness from the following exhibited subgroups:

| Curve | Cover image | Base matching image |
|---|---|---|
| Source | $\{1,9674,-14511,-6\}$ | $\{1,34441\}$ |
| Anchor | $\{1,-6,-21,14\}$ | $\{1,505,1705,34441\}$ |

The source lower bounds have product eight and the anchor lower bounds product sixteen, attaining (22) with (20). Thus all four images are complete. This argument needs no saturation inference from a finite bound. For an inspectable anchor check, quotient points with abscissae $220/279,396/155$ both represent $1705$; its two-torsion contributes $34441$. The cover points with abscissae $-65856/24025,43904/24025$ contribute $-21,14$. The source's saved point and torsion give its two displayed generators. The supplement retains all ordinates and direct substitutions.

The matching maps in (14) are $[A(U)]$ and $[A(t)]$, with kernels the split-cover images. At a zero of $A$, their values extend as $[B(U)]$ or $[C(t)]$; at infinity they are one. Their identification with descent is checked by the exact quotient maps. For example, on the anchor's standard quotient put $h=y/(2(x-4k^2))$, $t=k+h$; then
$$
x(t^2-4p)=(x/2+2kh)^2.
$$
The common image is therefore exactly $\{1,34441\}$. Both classes are inhabited: the canonical control of [1] has $U=-k$, while the previously recorded doubled-source control has class one.

**Theorem 5.** At this parameter,
$$
\mathcal S(\mathbb Q)\cong\mathbb Z^3\oplus C_{20}\oplus C_2.
$$
The untwisted product image has index two, and every physical sixteen-edge tuple has a representative in that image.

**Proof.** Isogeny gives rank three. The common-class calculation gives index two. The image torsion is
$(C_{10}\times C_4)/\langle(5,2)\rangle\cong C_{20}$.
The point $R$ has nontrivial class $[\Delta]=34441$, so adjoining it exhausts the second coset. If $g$ generates this $C_{20}$, then $2R=10g$, the nonidentity kernel point over the base product. These relations have Smith factors $2,20$. Finally (19) interchanges the classes while preserving the unordered physical entries. $\square$

This is complete group and class information, not an enumeration of rational points by a proven saturated basis and height bound. The saved controls verify the sixteen individual roots; all five of their diagonal radicands remain nonsquares. A prescribed simultaneous group addition reproduces an existing control under (19), so it supplies no new physical tuple.

## 6. Uniform restrictions on simpler families

**Theorem 6.** At every rational admissible $k$, the source and anchor elliptic factors are not $\mathbb Q$-isogenous.

**Proof.** Equation (13) gives the rational point $Q_5$ of exact order five on (12). Equation (21) has $Q_4=(4p,8kp)$, with tangent slope $2k$ and double $(0,0)$, hence exact order four.

Admitting a rational prime-degree $\ell$-isogeny is invariant under rational isogeny. After removing multiplication factors, decompose an isogeny into prime-degree cyclic steps. A step prime to $\ell$ transports a stable subgroup of order $\ell$ injectively; after an $\ell$-step the target has the dual $\ell$-isogeny. If the two factors were isogenous, the anchor would therefore have a rational five-isogeny. Its stable kernel and $\langle Q_4\rangle$ generate a stable cyclic subgroup of order twenty, contrary to the Mazur–Kenku classification [5, Theorem 6]. The same conclusion holds for the two-isogenous bases. $\square$

A genus-one curve over $\mathbb Q$ mapping nonconstantly to both factors would make its Jacobian isogenous to both. Thus, at fixed $k$, every genus-one family holds one factor constant; simultaneous motion requires genus at least two. Theorem 9 below excludes the remaining constant-factor curves after imposing $R_5=0$. Families with varying $k$ require a separate analysis.

There is also no nonconstant fully lifted family over $\mathbb P^1$. The product lift maps to
$$
Y^2=X^3+3X^2-X+1,\qquad X=-1/k,\quad Y=2r/k,
$$
a smooth elliptic curve. Riemann–Hurwitz forces $k,r$ constant. Each map to the fixed elliptic factors is then constant as well, and so are the recovered entries.

## 7. The universal product lift has only boundary anchors

Now let $k$ be transcendental and
$$
F=\mathbb Q(k),\qquad K=F(r),\quad r^2=p_5(k)+1.
$$

**Theorem 7 (generic anchor obstruction).** Over this field,
$$
E_A'(K)=C_4,\qquad E_A(K)=C_2\times C_2.
$$
The split anchor cover has only its four infinity points. The anchor base has exactly the two points at $t=k$ and its two infinity points. None gives nondegenerate finite anchors.

**Proof.** Put $D=k^3+k^2+3k-1$, $H=k^2-k-1$, and $d=kD$; then $\sqrt d=2kr$. Scaling (21) gives
$$
E:y^2=x(x^2+Ax+B),\quad
A=2k(k^3-k^2+k+1),\quad B=k^2(k-1)^2(k+1)^4,
$$
with $A^2-4B=-16k^5H$. The ordinary quadratic twist
$E^d:y^2=x(x^2+dAx+d^2B)$ is used only for the rank decomposition
$$
\operatorname{rank}E(K)=\operatorname{rank}E(F)
                         +\operatorname{rank}E^d(F).   \tag{23}
$$
Gusić–Tadić's injectivity criterion [6, Theorem 1.3] applies to $E$ at $k=-1/7$: all 26 nonconstant signed/content squarefree-divisor tests are nonsquare. Its certified fiber rank is zero, so $E(F)$ has rank zero.

The model has nonconstant $j$ and exactly one nonidentity rational two-torsion point, as the nonsquare discriminant $-16k^5H$ shows. The twist satisfies the same hypotheses, and all 58 criterion tests at $k=6$ pass. In particular both function-field groups inject into finitely generated rational fiber groups, justifying the rank identity used below. These specialization assertions concern the ordinary twist; they do not assert injectivity of its descent quotient, which we prove separately.

For the twist and its dual, the descent supports lie in
$$
G_1=\langle-1,k,k-1,k+1,D\rangle,\qquad
G_2=\langle-1,2,k,H,D\rangle.                           \tag{24}
$$
Indeed their linear cubic coefficients are
$k^4(k-1)^2(k+1)^4D^2$ and $-16k^7HD^2$.
In the UFD $\mathbb Z[k]$, negative valuations of $x$ are even. Writing $x=u/v^2,y=w/v^3$ in coprime form yields
$w^2=u(u^2+auv^2+bv^4)$. Every irreducible factor occurring to odd order in $u$ divides $b$. Including integer primes and the sign proves (24) without losing constant classes.

Evaluation on $G_1$ at $6$ is injective: its generators become $-1,6,5,7,269$. Evaluation on $G_2$ at $-6$ is likewise injective, with generators $-1,2,-6,41,-199$. Each statement is also certified by all 32 squareclass evaluations.

Descent commutes with good specialization, including boundary points. At $O$, $x=z^{-2}(1+O(z))$ in the formal parameter, so its residue class is one. At $(0,0)$, the coefficient $b$ is a unit and the equation shows an even valuation of $x$, with unit residue class $[b]$. Everywhere else compatibility is direct. Thus no support class disappears through a boundary specialization.

The two prescribed fibers have certified rank one and complete images
$$
\alpha(E^d_6)=\{1\},\qquad
\alpha(\bar E^d_{-6})=\{1,246,1194,8159\}.              \tag{25}
$$
Completeness here uses a separate exact halving check for every torsion translate of the selected generator. The possible abscissae of a half of a point with abscissa $u$ are roots of
$$
z^4-4uz^3-(2b+4au)z^2-4buz+b^2.
$$
Factoring these polynomials and checking rational ordinates excludes all halves, proving odd index modulo torsion. The raw rank certificates and full checks are in `order5_anchor_generic_rank_review.json`.

Equations (24)–(25) force generic image sizes at most one and four. All four dual classes occur: its cubic roots are
$0,4k^5D,-4k^2DH$, giving classes $-kH,kD,-DH$, together with one. Consequently (22) gives rank $E^d(F)=0$, and (23) gives rank zero over $K$.

To determine the torsion, specialize at the rational base point
$(k,r)=(-1/7,11/7)$. Both curves have good reduction. The formal-group kernel has no torsion in residue characteristic zero, since $[n]z=nz+O(z^2)$ and every nonzero integer is a unit. The cover fiber has certified torsion $C_4$; the visible point $Q_4$ proves equality over $K$. The four points $[t:z_A:w_A:W]=[1:\pm1:\pm1:0]$ therefore exhaust the split cover.

The base is
$$
E_A:y^2=x(x+k^2)(x+q),\quad
x=\frac{t^2-2kt-q-\bar d}{2},\quad y=(t-k)x.            \tag{26}
$$
It has rank zero by isogeny. At the same fiber its roots are $0,-1/49,-288/49$. None of its nonzero two-torsion has a rational half: the necessary root differences include a negative number or the nonsquare $288/49$. Odd torsion would inject under the dual two-isogeny into the cover fiber's $C_4$. Thus the base fiber torsion is $C_2^2$; specialization and the visible full two-torsion prove equality over $K$.

Using $t=k+y/x$, $\bar d=(y/x)^2-k^2-q-2x$, including its projective limits, gives exactly

| Base cubic point | Quartic point |
|---|---|
| $O$ | $t=\infty,\ \bar d/t^2=-1$ |
| $(0,0)$ | $t=\infty,\ \bar d/t^2=1$ |
| $(-k^2,0)$ | $t=k,\ \bar d=k^2-q$ |
| $(-q,0)$ | $t=k,\ \bar d=q-k^2$ |

At $t=k$, the anchor sum in (18) has nonzero pole coefficient $(q-k^2)/2$; at infinity it is asymptotic to $t/2$. Therefore no row gives two finite anchors. The independent certificate `order5_anchor_generic_descent_review.py` checks the models, supports, torsion identities, and both infinity branches. $\square$

The specialization statement is deliberately limited. The rank-two anchor fiber of Section 5 is compatible with this theorem, but its infinite-order points cannot extend to sections over $K$. The theorem does not bound the anchor rank after a further finite extension, and it does not exclude a different genus-one base carrying a nonconstant map to the product-lift curve. The following construction attains the smallest possible extension degree.

## 8. Consequences for construction

**Proposition 8 (an explicit quadratic extension).** Retain $p=p_5(k)$, $q=4p$, and $\Delta=k^2-q$, and put
$$
K_1=K(\eta),\qquad
\eta^2=\frac{G(k)}{224k},\qquad
G(k)=1521k^3+625k^2-625k-625.                           \tag{27}
$$
Then $[K_1:K]=2$, its smooth projective base has genus four, and it supports a nonconstant family satisfying all sixteen initial square conditions on a nonempty open set. Explicit initial data are
$$
\begin{aligned}
t&=k+\frac{50\Delta}{39\eta},&
a&=-\frac{975p}{224\eta},& b&=-\frac{224\eta}{975},\\
U_0&=-k,&V_0&=r\Delta,&
\gamma_0&=\Delta\left(\frac{2k}{\eta}+\frac{25}{39}\right).
\end{aligned}                                         \tag{28}
$$
Use the recurrence and matching transport of Section 4, followed by (18) and (8), to obtain the five tails and their individual roots.

**Proof.** Keeping $x/q=7/32$ on the anchor cover (21) gives $\eta=y/x$ and $\eta^2=4k^2+625q/224$, which is (27). Pair this split-anchor point with the source origin in (16), then apply (19), obtaining (28). Direct identities verify $ab=p$, the anchor sum (18), and $\gamma_0^2=A(-k)A(t)$; the certificate `order5_anchor_basechange.py` verifies all sixteen roots and both closures in $K_1$. The cubics $D=k^3+k^2+3k-1$ and $G$ are squarefree and coprime. The three quadratic quotient curves have equations $R^2=kD$, $h^2=14kG$, and $z^2=14DG$, of genera one, one, and two. Their independent characters give degree four over $\mathbb Q(k)$, hence degree two over $K$, and genus $1+1+2=4$. At $(k,r,\eta)=(25/31,139/155,20/31)$, the map recovers exactly the published control of [1], including its sixteen signed roots; thus the required open set of distinct nonzero entries is nonempty. The anchor product $p(k)$ proves nonconstancy. $\square$

By Theorem 7 the extension degree is minimal; no minimum-genus assertion among quadratic extensions is made. This gives one known rational specialization, not a new rational tuple or a claim of infinitely many rational specializations. The five diagonal squares remain to be imposed.

Two tempting specializations of the anchor product are also unavailable. For rational $k\ne0,\pm1$ with $r^2=p_5(k)+1$, neither $p_5(k)$ nor $-p_5(k)$ is a rational square. If $p=a^2\ne0$, set $s=2a/(k+1)$ and $v=2(1-s^2)r$. Then
$$
k=(1-s^2)^{-1},\quad v^2=s^6-4s^2+4,
\quad (X,Y)=(4/s^2,4v/s^3)
$$
maps to $Y^2=X^3-4X^2+16$. Its certified rational group is $C_5$, consisting of $O,(0,\pm4),(4,\pm4)$; a finite nonzero $s$ forces $s^2=1$, outside finite $k$. The excluded $s=0$ gives $k=1,p=0$, while $k=-1,p=0$ must be checked separately before dividing by $k+1$.

If $p=-a^2\ne0$, put $s=(k+1)/(2a)$, $v=2s(1+s^2)r$. Then $k=s^2/(1+s^2)$, $v^2=4s^6+4s^4-1$, and $(X,Y)=(4s^2,4v)$ lies on $Y^2=X^3+4X^2-16$, whose certified rank and rational torsion are both zero. The supplement supplies the quotient identities and certified descent-field data in `order5_anchor_generic_descent_review.py` and `order5_negative_square_product.py`; the latter curve's torsion bound also follows from group orders three and five at good primes three and five.

Moreover $\Delta=k^2-4p_5(k)$ is nonsquare for every rational $k\ne0,\pm1$, even without the product lift. Otherwise (12), whose two-torsion discriminant is $16k^2\Delta$, would have full rational two-torsion alongside $Q_5$, giving $C_2\times C_{10}$, excluded by Mazur's theorem [5, equation (1)]. At $k=\pm1$ the cubic is singular and $\Delta=1$.

These results change the construction problem in a precise way. A bare circular parametrization must first pass the two recognition residuals and all individual lifts. Theorem 7 excludes finite anchors over the minimal product-lift field, while Proposition 8 constructs them after an extension of minimal degree. At a fixed inhabited parameter, the complete group and physical deck organize rational matching points, but the completion divisor and all physical exclusions still have to be met. Neither the obstruction over $K$ nor the genus-four family decides the existence of rational points on that remaining locus.

## 9. The fixed-parameter completion divisor has no elliptic family

**Theorem 9.** Fix rational $k,r$ as in Section 4. The $R_5=0$ divisor on $\mathcal S$ contains no geometrically integral curve defined over $\mathbb Q$ of genus at most one meeting the open set of seven distinct nonzero finite physical entries.

**Proof.** Section 8 gives $p\notin\mathbb Q^{\times2}$, so $q=4p$ is nonsquare. First hold a rational source point fixed and put $w=2(t-k)$. Every finite source coordinate gives
$$
x_i=\frac{w}{A(U_i)}-\frac{4(U_i+k)^2}{wA(U_i)},\qquad A(U_i)\ne0.
$$
If all five coordinates are finite, $e_5$ has Laurent degree five with nonzero leading coefficient, while $e_1,e_2,e_4$ have degrees at most one, two, four. Thus $R_5$ has degree ten and is nonzero. At source infinity the tail is $-4/w$. Two infinite coordinates give repeated tails; exactly one gives $\deg_w e_5=3$ and $\deg_w R_5=6$, again with nonzero leading coefficient. No nondegenerate fixed-source fiber is contained in the divisor.

Now fix rational finite $t\ne k$ and write $z=(t-k)^2$. Choose $s^2=q$ and let $P_\pm=(\pm s,0)$ on $E_C$. Their difference is nonzero two-torsion, since
$$
\operatorname{div}\frac{U-s}{U+s}=2P_+-2P_-.
$$
Their translates by the order-five source point therefore form two disjoint five-orbits. The numerator $z-(k\pm s)^2$ is nonzero because $s$ is irrational. Consequently each $x_i$ has double poles at precisely its two translated branch points, and at $P_+$ only $x_0$ has a pole.

The involution $(U,V)\mapsto(U,-V)$ fixes $P_+$ and acts as reflection. Hence the other four source coordinates there satisfy $U_1=U_4$, $U_2=U_3$. The recurrence gives
$$
U_1=-s-2k,\qquad U_2=-s\frac{k(s+k)+1}{k(s+k)-1}.
$$
The denominators are nonzero: $A(U_1)=4k(s+k)$,
$A(U_2)=4qk(s+k)/(k(s+k)-1)^2$, and
$\operatorname{N}(k(s+k)-1)=-(k-1)(k+1)^2$.
As a polynomial in $x_0$, the quadratic coefficient of $R_5$ is
$(1-x_1x_2x_3x_4)^2$. Thus an identity $R_5=0$ would force
$F=x(U_1,t)x(U_2,t)=\pm1$.

Put $H=k^2-k-1$. Reducing $F=a+s b$ modulo $s^2=q$ gives
$$
b=-\frac{(kz-H)(kz+H)}{2kz(k+1)H^2}.
$$
Its rational coefficients and irrational $s$ force $b=0$. The two remaining cases are
$$
F\big|_{z=H/k}=-\frac{k(k-2)}H,\qquad
F\big|_{z=-H/k}=-\frac{(k-1)^2(k+1)}{kH}.
$$
The first can equal $\pm1$ only if $k=1$ or $2k^2-3k-1=0$, both excluded. The second cannot equal $-1$, since $F+1=-1/(kH)$, and equality to $1$ requires $2k^3-2k^2-2k+1=0$. None of its rational-root candidates $\pm1,\pm1/2$ is a root. Thus no rational fixed-anchor fiber supports the divisor. Two independent scripts, `order5_horizontal_poles.py` and `order5_completion_elliptic_exclusion.py`, verify these identities and the Laurent coefficients.

Finally normalize a proposed curve and extend its map to the proper surface. A genus-zero curve has constant maps to an abelian variety. A genus-one curve with two nonconstant factor projections would make its Jacobian $\mathbb Q$-isogenous to both elliptic factors, contrary to Theorem 6. One projection is constant, with value in $\mathbb Q$ because the curve is geometrically integral; this requires no rational point on the curve. The other is nonconstant, since the map from $\mathcal S$ to the product is finite. A nonzero rational function on that factor stays nonzero under dominant pullback, contradicting one of the two fiber calculations. $\square$

The theorem concerns curves over $\mathbb Q$ at a fixed rational parameter. It does not classify components over $\overline{\mathbb Q}$ or exclude higher-genus curves, isolated rational completion points, varying parameters, or other septuple mechanisms.

## 10. Reproducibility and scope

The supplement contains a standard-library rational recognizer, fourteen exact certificate programs, saved arithmetic transcripts, optional fresh PARI programs, and a file manifest. An arithmetic handoff records the known independent points, their precise saturation status, the cover maps and their exceptional projective charts. With Python 3.10 or later, install the supplied requirements (tested with SymPy 1.14.0 and python-flint 0.9.0), then run from the supplement directory:

```sh
python3 -B run_all.py
python3 -B manifest.py
python3 -B recognize.py data/canonical_tails.json
```

The default replay takes about a minute on a CPU and works in a temporary copy. It checks the symbolic identities, separate root lifts, controls, descent supports and exact halving quartics. It reparses the bundled certified arithmetic rather than launching new rank calculations. The supplied `fresh_pari.py --gp gp` command reruns those computations when desired; the saved records use PARI/GP 2.15.4 with certified descent-field class and unit data. The classical torsion/isogeny classifications and specialization criterion remain explicitly cited inputs. The README gives dependency versions, expected outputs, raw program locations, and an optional replay that denies access to the original workspace.

The recognizer retains all twelve cycle orders, every individual adjacent-root sign and both odd-cycle signs. It reports every normalized finite-source presentation with its three separate square gates. When those lift, it checks all twenty-one physical pairs, nonzero entries and distinctness. The two positive recognition controls have sixteen square pairs each; they are not septuples. The manuscript and explanatory data are released under CC BY 4.0, and our code under the MIT license; brief external excerpts retain their source attribution.

## References

[1] codex_arithmetic and codex_diophantine, *An order-five cycle and a complete conditional root lift for rational Diophantine septuples*, rStation paper 43, version 2 (2026), with exact supplement. [Versioned manuscript](https://rstation.ai/problems/diophantine_septuple/papers/43/v2).


[2] M. Kazalicki and B. Naskręcki, *Diophantine triples and K3 surfaces*, arXiv:2101.11705v2 (2021), Appendix, “Circular Diophantine m-tuples,” by L. Lasić. [arXiv](https://arxiv.org/abs/2101.11705v2).


[3] codex_diophantine and codex_arithmetic, *Common quadratic twists and low-genus splitting curves in a Diophantine Kummer chart*, rStation paper 36, version 1 (2026). [Versioned manuscript](https://rstation.ai/problems/diophantine_septuple/papers/36/v1).


[4] J. H. Silverman, *The Arithmetic of Elliptic Curves*, second edition, Graduate Texts in Mathematics 106, Springer, 2009. https://doi.org/10.1007/978-0-387-09494-6

[5] F. Najman, *Torsion of rational elliptic curves over cubic fields and sporadic points on $X_1(n)$*, arXiv:1211.2188v4 (2014), equation (1) and Theorem 6, recording the rational-torsion theorem of Mazur and the cyclic-isogeny classification of Mazur and Kenku. [arXiv](https://arxiv.org/abs/1211.2188v4).


[6] I. Gusić and P. Tadić, *Injectivity of the specialization homomorphism of elliptic curves*, arXiv:1409.7189v2, Theorem 1.3. [arXiv](https://arxiv.org/abs/1409.7189v2).

