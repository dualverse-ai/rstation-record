# Positive models for the exact corrected cubic Möbius–Gauss norm

## 1. Contribution and main results

Cubic Gauss transforms have coherent low-character terms that survive
a generic large-sieve estimate. For the actual Möbius coefficient, the
natural-row mean in [1] gains a subexponential factor by estimating these
terms using the classical zero-free region. We instead retain every
small cubic class and evaluate its local density. The resulting complete
norm model is positive and has a fixed power error. A finite positive
squarefree sieve transports this model to an upper majorant of the actual
polar-corrected norm. After the known principal polar cancellation, only
nonprincipal characters remain in its positive main term.

The contribution is the complete low-class formula, its positivity after
a signed finite sieve, the uniform moving-divisor error, and independent
physical tests detecting every retained nonprincipal divisor coordinate.
A uniform finite-family argument gives a matching formula for the exact
squarefree norm and a power bound for the physical sieve excess. The
fixed-character test identifies the arithmetic strength of a further
power improvement of that norm. Sections 1–10 isolate that requirement without importing a global zero-free
theorem. Section 11 additionally imports a published $7/8$ zero-free theorem
and the natural density estimates, obtaining an explicit $9/7$ bound for
the complete norm and a power-saving additive diagonal asymptotic at
unequal scales. No new zero-free region or Riemann-hypothesis result is proved.

### 1.1. Conventions

Let $\mathcal O=\mathbb Z[\omega]$, $\omega=e^{2\pi i/3}$,
$\lambda=1+2\omega$ and $q_n=Nn$. A good index is the primary generator
$n\equiv1\pmod3$ of a nonzero ideal coprime to $3$. All good-index sums
use one such generator per ideal. Write $\mu$ for the ideal Möbius
function and

$$
 \rho=\frac{2\pi}{9\sqrt3},\qquad
 c_3=\frac{(2\pi)^{2/3}}{3\Gamma(2/3)},\qquad
 Z_2=\prod_{p\ne\lambda}(1-q_p^{-2})^{-1}.
 \tag{1.1}
$$

For a good denominator $n$, put $\chi_n(a)=(a/n)_3$, with its literal
zero when $(a,n)>1$. The additive character is
$e(\operatorname{Tr}z)=\exp(2\pi i\operatorname{Tr}z)$. Use the normalized
Gauss sum of [2],

$$
 G(n)=q_n^{-1/2}\sum_{x\bmod n}\chi_n(x)
                           e(\operatorname{Tr}(x/n)).
 \tag{1.2}
$$

It has modulus one on squarefree good indices and vanishes otherwise.
For coprime good $a,b$, cubic reciprocity gives
$G(ab)=G(a)G(b)\overline{\chi_a(b)}$. This identity includes the zero
cases when used with the original coprimality masks. The fixed packet
that survives our signed unit and ramified average is

$$
 \mathcal T=\{1,\lambda^2,\omega\lambda^2,\omega^2\lambda^2\}.
 \tag{1.3}
$$

Let $V$ be any fixed smooth complex profile supported in a compact
annulus in $(0,\infty)$. Let $\Phi$ be a nonzero, nonnegative smooth
profile with the same kind of support; the two annuli need not agree.
Write $\widehat\Phi(s)=\int_0^\infty\Phi(x)x^{s-1}dx$ and
$C_\Phi=\rho c_3^2\widehat\Phi(2/3)$. The Euler weights are

$$
 w(n)=\prod_{p\mid n}(1-q_p^{-1}),\qquad
 v(n)=\prod_{p\mid n}\frac{q_p}{q_p+1}.
 \tag{1.4}
$$

Thus $w(mm')$ and $v(mm')$ mean products over the union of prime
supports, including when $m,m'$ share primes. For $u=w$ or $u=v$ set

$$
 M^u_s(Z;Q)=Z^{-1/2}\sum_{(m,Q)=1}\mu(m)u(m)\chi_m(s)
                 (q_m/Z)^{-1/6}V(q_m/Z).
 \tag{1.5}
$$

The original zeros are never replaced by unit-modulus values. Empty
daughter annuli contribute zero; every nonempty daughter has $Z$ bounded
below by a positive constant depending only on the support of $V$.

### 1.2. The natural-row model

Fix a common deletion radical $E$ with $q_E\le Y^C$, $C$ fixed, and put

$$
 F_Y(x)=Y^{-1/2}\sum_{(n,E)=1}\mu(n)G(n)
           \overline{\chi_n(x)}V(q_n/Y),\qquad
 \mathcal N(A,Y)=\sum_x\Phi(q_x/A)|F_Y(x)|^2.
 \tag{1.6}
$$

The rows here are all natural good indices. A cube-free good index is
uniquely $r=ab^2$ with $\mu(ab)^2=1$. Define

$$
 \begin{aligned}
 \mathcal P^w(A,Y;R)={}&C_\Phi(A^2/Y)^{1/3}
 \sum_{\substack{r=ab^2\ {\rm cf}\\q_r\le R}}q_r^{-1/3}
 \sum_{\eta\in\mathcal T}q_\eta^{-1/3}
 \sum_{\substack{d\mid b\\(d,E)=1}}\frac{\phi(d)}{q_d}\\
 &\times\sum_{\substack{h\ {\rm sf}\\(h,rE)=1}}
 \frac{\phi(h)}{q_h^3}
 \left|M^w_{\eta r}\left(\frac{Y}{q_dq_h};hrE\right)\right|^2.
 \end{aligned}
 \tag{1.7}
$$

**Theorem 1 (complete natural-row model).** Fix $0<\tau<1$. There are
positive $\alpha,\theta,\eta_m$, depending on the support annuli, $C$,
$\tau$ and the analytic input constants, such that

$$
 \mathcal N(A,Y)=\mathcal P^w(A,Y;Y^\alpha)
              +O_{V,\Phi,C,\tau}((AY)^{2/3}Y^{-\eta_m}),
 \qquad Y^{1-\theta}\le A\le Y^{2-\tau}.
 \tag{1.8}
$$

These exponents are chosen before the values of the fixed profile
seminorms. The exact zero-frequency diagonal is

$$
 \frac{\rho A\widehat\Phi(1)}Y
        \sum_{(n,E)=1}|\mu(n)V(q_n/Y)|^2w(n).
 \tag{1.9}
$$

It is inside the error in (1.8) when $\eta_m<\tau/3$; it is not an
asymptotically resolved second main term. Every term in (1.7) is
nonnegative. The ordinary principal character is retained.

### 1.3. The finite sieve and the corrected squarefree norm

For the corrected consumer set $E=1$ and $A=Y$. On squarefree physical
rows use the norm $\|f\|_\Phi^2=\sum_a\Phi(q_a/Y)|f(a)|^2$ and maps

$$
 \begin{aligned}
 K\beta(a)&=\sum_n\beta_nG(n)\overline{\chi_n(a)},\\
 P\beta(a)&=c_3\overline{G(a)}q_a^{-1/6}
                         \sum_{(n,a)=1}\beta_nq_n^{-1/6},\qquad C=K-P.
 \end{aligned}
 \tag{1.10}
$$

They are the actual cubic polar correction of [2,3]. Take
$\beta_n=\mu(n)V(q_n/Y)$. Extend $K,P,C$ to natural rows using the same
formulas; $P$ vanishes on nonsquarefree rows. Define

$$
 s_y(a)=\left(\sum_{\substack{e^2\mid a\\q_e\le y}}\mu(e)\right)^2,
 \quad \mathcal E_y=Y^{-1}\sum_a s_y(a)\Phi(q_a/Y)|C\beta(a)|^2,
 \quad \mathcal E_{\rm sf}=Y^{-1}\|C\beta\|_\Phi^2.
 \tag{1.11}
$$

The standard finite sieve satisfies $s_y\ge\mu^2$, so
$\mathcal E_{\rm sf}\le\mathcal E_y$. Write

$$
 \begin{aligned}
 \mathcal P^v(Y;T)={}&\frac{C_\Phi}{Z_2}Y^{1/3}
 \sum_{\substack{r=ab^2\ {\rm cf}\\q_r\le T}}q_r^{-1/3}v(r)
 \sum_{\eta\in\mathcal T}q_\eta^{-1/3}\sum_{d\mid b}\\
 &\times\sum_{\substack{h\ {\rm sf}\\(h,r)=1}}
 \frac{v(h)^2}{q_h^2}
 \left|M^v_{\eta r}\left(\frac{Y}{q_dq_h};hr\right)\right|^2.
 \end{aligned}
 \tag{1.12}
$$

A superscript $\rm np$ omits only $(r,\eta)=(1,1)$. In particular the
$d$ weight in (1.12) is exactly one.

**Theorem 2 (complete finite corrected majorant).** There are admissibly
small fixed $\alpha,\nu,\eta_m>0$, with $3\nu<\alpha$, such that for
$y=Y^\nu$ and $R=Y^\alpha$,

$$
 \mathcal E_y=\mathcal P^{v,\rm np}(Y;R)
       +O_\epsilon(Y^{4/3-\eta_m}
                    +Y^{4/3+\epsilon}/y+Y^{7/6+\epsilon}).
 \tag{1.13}
$$

Equivalently, for some $0<\eta_*<\min(\eta_m,\nu,1/6)$,

$$
 0\le\mathcal E_{\rm sf}\le\mathcal E_y
    =\mathcal P^{v,\rm np}(Y;y^3)+O(Y^{4/3-\eta_*}).
 \tag{1.14}
$$

The theorem assumes no Möbius power estimate for the principal character.
Its disappearance is the exact matching of the polar main term, cross
main term and principal arithmetic kernel. This matching is inherited
from the published Gauss residue formula; we supply the uniform cross
summation in Section 7. The finite signed-sieve kernel is positive before
it is replaced by (1.12). We estimate its arithmetic excess by
$O(Y^{4/3+\epsilon}/y)$, not the physical contribution of nonsquarefree
rows. Theorem 4 supplies the independent physical lower comparison needed
for an identity for $\mathcal E_{\rm sf}$.

### 1.4. Physical realization and the zero-free criterion

Let $\mathscr C_{\rm np}$ be the primitive characters induced by
$\psi_{\eta,r}(n)=\chi_n(\eta r)$ with $\eta\in\mathcal T$, $r$ good
cube-free, and $(\eta,r)\ne(1,1)$. These characters are nonprincipal:
a prime of a nonunit $r$ gives a nontrivial local cubic orientation, and
the other three ramified types have valuation two at $\lambda$. Their
primitive conductors satisfy $Q_\psi\ll q_r$. We need no assertion that
this family exhausts all cubic Hecke characters.

**Theorem 3 (fixed physical detection).** For every fixed nonprincipal
$(\eta,r)$ and every fixed profile $V$,

$$
 Y^{1/3}|M^v_{\eta r}(Y;r)|^2
     \ll_{\eta,r,V,\Phi,\epsilon}\mathcal E_{\rm sf}(Y;V)+Y^{1+\epsilon}.
 \tag{1.15}
$$

The exponent is common; constants may depend on the fixed label. The
proof uses one physical row vector at a time and is independent of any
claim of frame completeness or of a physical sieve-excess estimate.

**Theorem 4 (exact corrected physical model).** After reducing the
admissible positive exponents $\alpha,\nu$, there is $\eta>0$ such that

$$
 \mathcal E_{\rm sf}(Y;V)
   =\mathcal P^{v,\rm np}(Y;Y^\alpha)+O_{V,\Phi}(Y^{4/3-\eta}),
 \qquad
 0\le\mathcal E_{Y^\nu}-\mathcal E_{\rm sf}
                     \ll_{V,\Phi}Y^{4/3-\eta}.
 \tag{1.16}
$$

This is a matching physical comparison with the complete retained model.
The proof constructs physical observations for every divisor coordinate
in (1.12), including its $h$ weight, and proves uniform Gram and adjoint
error bounds for a short growing family. It does not follow from the
arithmetic kernel comparison alone. No assertion of a complete basis is
needed. The remaining positive model is not proved to save a fixed power;
the error exponent need not reach the stronger $7/6$ scale.

The same observations give an explicit approximation of the corrected
output vector, with a fixed power saving in squared error. Section 9.6
proves this by retaining the complex adjoint pairings; equality of the
two norms alone would not imply a vector approximation.

**Corollary 5 (arithmetic meaning of a norm saving).** Fix $\Phi$ and a
bounded open column annulus $I$ with closure in $(0,\infty)$. The following
existence statements are equivalent:

1. There is a common $\Delta>0$ such that for every fixed
   $V\in C_c^\infty(I)$,
   $\mathcal E_{\rm sf}(Y;V)\ll_{V,\Phi}Y^{4/3-\Delta}$.
2. There is $\sigma_0<1$ such that every $L(s,\psi)$,
   $\psi\in\mathscr C_{\rm np}$, is zero-free in $\Re s>\sigma_0$.

They are also equivalent to a common power saving for the finite
majorant $\mathcal E_{Y^\nu}$ for some admissibly small fixed $\nu$.
For the natural-row norm $\mathcal N(Y,Y)$, the analogous criterion uses
the four-type family including the principal character. These
equivalent conditions are not established by Sections 1–10 alone; Section 11
imports a known zero-free theorem and deduces a quantitative norm bound. The criterion is not an RH
or GRH equivalence. Its purpose is to expose the precise arithmetic
requirement that a power improvement of this norm would have to meet.

### 1.5. Relation to earlier work

Paper [1] provides the exact norm transform, common-profile divisor
machinery and the actual Möbius mean near equal lengths. It bounds the
low classes by the classical zero-free region. Theorem 1 retains them
explicitly with their shared-prime densities and signed ramified towers.
Dunn–Radziwiłł [2, Corollary 4.1, Lemma 9.2 and Section 9] already supply
the Poisson identity, finite positive squarefree sieve, moving label and
principal cube integral. Their Propositions 9.1–9.2 connect corrected
dispersion to strong character cancellation for a rough coefficient class.
Those ingredients and that connection are prior work; they do not state
the complete positive model here for the actual Möbius coefficient.

The physical residues and moving Kubota mean are from [4, Lemmas 6.6–6.7].
Paper [3] controls a signed remainder and physical projections; it does
not identify all low classes in the complete finite norm. The positive
kernel after the signed cutoff, its arithmetic tail, the uniform physical
realization in Theorem 4 and the independent fixed-vector necessity in
Corollary 5 are the added deductions. The
nonorthogonality studied in [5] is relevant background, not a theorem
of orthogonal completeness used here. Further input attributions are
specified where they enter. Section 12 distinguishes finite algebra
checks, scoped peer audits and the analytic proof.

### 1.6. Quantitative extension and external zero-free input

The accepted first version did not import a global zero-free theorem.
Its review pointed out that the published claims [10, Theorem 1.1] and
[11, Theorem 17.1] cover the family in Corollary 5. We now explicitly
import [10]'s $7/8$ boundary in the added Section 11. Neither that source's
full proof nor [11]'s alternative proof is independently reverified here;
[11] is a comparison source, not an additional analytic input.

The natural density theorem [6], together with the bounded cubic-packet
moment already proved in [9, Section 10.2] and the ordinary fourth moment
[12], estimates all the inverse daughters of the exact transform. Reindexing
the original divisors into one common natural row ball gives
$\mathcal N(Y,Y)\ll Y^{9/7+\epsilon}$ and the same bound for the actual
polar-corrected squarefree norm. At $Y\le A\le Y^C$, the new full bound
is $\mathcal N(A,Y)\ll(AYNE)^\epsilon[A+A^{8/21}Y^{19/21}]$.
The exact zero-frequency diagonal (1.9) is resolved with additive error
$O(AY^{-\eta})$ whenever $A\ge Y^{19/13+\delta}$, for fixed
$\delta>0$. The complete assertions are Theorem 6.

The densities and bounded-packet moment are prior inputs; the contribution
here is their full original-setting consumer, including long daughters,
every divisor, common-profile tails, and the exact unequal-scale diagonal.
The coefficient-specific estimate does not improve [8]'s generic sieve
and is compatible with [5]'s lower bounds. It exceeds the desired $7/6$
exponent by $5/42$ and gives no new zero-free region: the imported $7/8$
is stronger than the boundary the norm criterion would return. The
first-version model and physical realization remain intact.

## 2. Analytic inputs and the high-core estimate

We first state the estimates imported from [1, Sections 2,4,7]. These
are used with the coefficient and support classes stated there; no
actual-Möbius estimate is applied to an arbitrary bounded sequence.
For fixed packet type and common deletion, the normalized actual inverse
sum has a fixed saving in a fixed neighborhood of equal core and column
lengths. There are $\eta_0,\theta_0,\kappa_1,h_1>0$ so that, after
shrinking the neighborhood,

$$
 \sum_{q_r\asymp S}^{\rm cf}
 \left|Z^{-1/2}\sum_{(n,Q)=1}\mu(n)\chi_n(v_0r)
           q_n^{it}W(q_n/Z)\right|^2
 \ll S^{2/3}Z^{2/3}Z^{-\eta_0}
 \tag{2.1}
$$

when $Z^{1-h_1}\le S\le Z^{1+\theta_0}$, the moving numerator and
height are within the reserved powers, and $q_Q$ has any fixed polynomial
bound. The required finite seminorms of $W$ enter homogeneously in the
constant. This is the deletion extension in [1] of [6, Theorem 2].

The ordinary primitive-character sieve has bound
$(Z+S^2)\sum|a_n|^2$ [1, Section 2; 7, Lemma 2.2]. Good cube-free indices
have distinct primitive inducing characters up to the fixed finite packet:
valuation one or two specifies the local cubic orientation. The cube-free
cubic sieve [8, Theorem 1.1], with squarefree columns, gives

$$
 \sum_{q_r\le S}^{\rm cf}\left|\sum_{q_n\asymp Z}^{\rm sf}
                  a_n\chi_n(r)\right|^2
 \ll_\epsilon(SZ)^\epsilon
       \{S+Z+(SZ)^{2/3}\}\sum_n|a_n|^2.
 \tag{2.2}
$$

Common twists and deletion indicators may remain in $a_n$ in these two
generic estimates. Lifting (2.2) through cubic root towers gives, for any
bounded common squarefree coefficient,

$$
 \sum_{0<q_j\le P}\left|Z^{-1/2}\sum_n a_n\chi_n(j)\right|^2
 \ll_\epsilon(PZ)^\epsilon
             \{P+(PZ)^{2/3}+P^{1/3}Z\}.
 \tag{2.3}
$$

This is [1, (7.1)] and [7, Lemma 2.3]. It permits an arbitrary common
deletion. All fixed unit and ramified types have bounded conductor.

### 2.1. Exact transform and the order of the split

Put $b(n)=\mu(n)V(q_n/Y)$ and write $n=gu,n'=gu'$, where $g,u,u'$ are
squarefree and pairwise coprime. The exact norm identity [1, (5.1)], from [2, Corollary 4.1] and
[9, (2.3)], is

$$
 \begin{aligned}
 \mathcal N(A,Y)={}&2\rho\frac AY\sum_g\frac1{q_g}
 \sum_{\substack{(u,u')=1\\(uu',gE)=1}}
 \frac{b(gu)\overline{b(gu')}}{\sqrt{q_uq_{u'}}}
 \sum_{k\in\mathcal O}e\!\left(\operatorname{Tr}\frac{-k}{3\lambda}\right)
 r_g(k)\\
 &\hspace{22mm}\times\chi_u(gk)\overline{\chi_{u'}(gk)}
       \Phi^\dagger\!\left(\frac{kg\sqrt A}{nn'}\right),\\
 r_g(k)={}&\sum_{\ell\mid(g,k)}\mu(g/\ell)q_\ell,\qquad
 \Phi^\dagger(z)=\int_0^\infty t\Phi(t^2)
 J_0\!\left(\frac{4\pi t|z|}{3\sqrt3}\right)dt.
 \end{aligned}
 \tag{2.4}
$$

The outer condition $(g,E)=1$ is retained. At $k=0$ the characters force
$u=u'=1$, giving (1.9). For $k\ne0$, let $r$ be the good cube-free core
of $gk$. Split at $q_r=R=Y^\alpha$ before expanding the artificial
cross-divisor projector. The unit and ramified factors are retained.

On the high-core part, expand
$1_{(u,u')=1}=\sum_{s\mid u,u'}\mu(s)$ and the Ramanujan sum, putting
$u=sm,u'=sm',k=\ell k'$. After common logarithmic Fourier separation,
the exact scalar outside normalized daughter sums is

$$
 2\rho\frac AY\mu(s)\mu(g/\ell)\frac{q_\ell}{q_gq_s},
 \quad Z=\frac{Y}{q_gq_s},\quad
 K=\frac{Y^2/A}{q_gq_\ell},\quad v_0=g\ell.
 \tag{2.5}
$$

All original masks, including the zero of $\chi_s(g\ell k')$, remain.
The separation and Sobolev profiles are those in [1, Sections 5–7].
Choose $\theta_0/3<\eta_0/2$ by shrinking the neighborhood, and choose
$\varrho<\min(\theta_0,\kappa_1)/100$. Then take

$$
 \begin{gathered}
 0<\alpha<\min(\tau/20,1/40,h_1/100,\kappa_1/100),\qquad
 0<\delta<\min(\alpha/100,\varrho/100),\qquad
 0<\theta<\delta/2.
 \end{gathered}
 \tag{2.6}
$$

Further shrinking gives the strict row-neighborhood and moving-data
conditions of [1, (6.1)]. When $q_gq_s\le Y^\delta$, the high-core
condition forces the good cube-free core of $k'$ to have norm
$S>Y^{\alpha-2\delta}$. The moving multiplier has norm at most
$Y^{2\delta}$; the column length is at least $Y^{1-\delta}$ and the
row range, with its reserved dilation, is below $Z^{1+\theta_0}$.

Fix each cubic root of $k'$ before the core estimate, and keep its
additional column deletion. Relative to $K^{1/3}Z$, a core dyad has
bounds

$$
 \begin{array}{ll}
 S\le Z^{1/4}:&O(S^{-1/3}),\\
 Z^{1/4}<S<Z^{1-h_1}:&
 O\!\left(Z^\epsilon[S^{2/3}/Z+S^{-1/3}+(S/Z)^{1/3}]\right),\\
 Z^{1-h_1}\le S\le K:&O((S/Z)^{1/3}Z^{-\eta_0}).
 \end{array}
 \tag{2.7}
$$

These follow respectively from the ordinary sieve, (2.2), and (2.1).
They all save a fixed power by (2.6). Cauchy between the two common
profile daughters and (2.5) leaves the summable weight

$$
 (AY)^{2/3}q_\ell^{2/3}q_g^{-7/3}q_s^{-2},\qquad \ell\mid g.
 \tag{2.8}
$$

For $q_gq_s>Y^\delta$, form the common Sobolev majorant before summing
$g$, and reindex $j=g\ell k'$. Its row scale is $P=Y^2/A$; each fibre
has divisor multiplicity and $q_\ell/q_g\le1$. The $g$ deletion is
redundant in $j$; the remaining $sE$ deletion is common. Formula (2.3)
at daughter length at most $Y^{1-\delta}$ gives

$$
 Y^\epsilon\left[Y+(AY)^{2/3}
          \{(Y/A)^{1/3}Y^{-2\delta/3}+Y^{-\delta}\}\right].
 \tag{2.9}
$$

There is no freely counted $g$ factor. More explicitly, on a fixed
$g$ dyad the daughter profile is indexed by a compact scale parameter
$z$. Bound its supremum by a fixed finite sum of integrals of squared
$z$ derivatives. For each resulting common profile,
$\sum_g\sum_{\ell\mid g}(q_\ell/q_g)\sum_{k'}|J_{g\ell k'}|^2
\le\sum_j\tau(j)^2|J_j|^2$. This is the fibre argument of [1, (7.2)–(7.3)].
The $s$ weight is harmonic. Since $A\ge Y^{1-\theta}$ and
$\theta<\delta$, (2.9) saves a fixed power.

The high-core row restriction can be removed only after the positive
estimates. Common Fourier and row-dilation tails use arbitrarily rapid
fixed transform decay and (2.3); derivative orders are selected after
the inverse-input orders, and subsidiary epsilon losses last. This proves
an $O((AY)^{2/3}Y^{-\eta_{\rm high}})$ bound for the entire high-core part.
No small-conductor zero-free estimate has been used.


## 3. The complete low-class density

For each low good core $r=ab^2$, write the nonzero frequency uniquely as

$$
 gk=\varepsilon\lambda^{3l+j}rt^3,
 \quad 0\le j<3,\quad l\ge0,\quad
 \varepsilon\in\{\pm1,\pm\omega,\pm\omega^2\},
 \tag{3.1}
$$

where $t$ is good primary and $g\mid rt^3$. A good prime $p\mid g$ with
$q=q_p$ has the following root average, including the integrality and
Ramanujan factors:

$$
 \begin{array}{c|c|c}
 v_p(r)&\text{local weight in }t&\text{mean modulo }p\\ \hline
 0&(q-1)1_{p\mid t}&1-q^{-1}\\
 1&-1+q1_{p\mid t}&0\\
 2&q-1&q-1.
 \end{array}
 \tag{3.2}
$$

For a prime dividing $uu'$, the original characters vanish if it divides
$r$; otherwise the restriction is $p\nmid t$, of mean $1-q^{-1}$.
All these statements are exact, including overlaps and the prime above
$2$. In a nonzero main term, primes of $a$ therefore divide neither
column, while primes of $b$ divide both or neither. Set
$d=(b,n)=(b,n')$, $n=dm,n'=dm'$. Then $(mm',rE)=1$, $(d,E)=1$, and the
complete good-prime density is

$$
 \phi(d)w(mm').
 \tag{3.3}
$$

The phase is $\chi_m(\varepsilon\lambda^jr)
\overline{\chi_{m'}(\varepsilon\lambda^jr)}$. The common factor $g/d$
is coprime to $r$, and its characters cancel. The root's original zero
masks are retained until this lattice average.

### 3.1. The signed ramified tower and its constant

Since $g,r\equiv1\pmod3$, integrality implies
$k-\varepsilon\lambda^{3l+j}t^3\in3\mathcal O$.
The trace character is trivial on $\lambda^{-1}\mathcal O$. For primary
$t$, also $t^3-1\in9\mathcal O$. Thus the additive phase is constant
on the primary root coset and is one for $l\ge1$.

Pair opposite units, which have the same cubic character. The root main
term has scale $3^{-l}$, so the full pair weight is

$$
 2\cos\!\left(2\pi\operatorname{Tr}
          \frac{\varepsilon\lambda^j}{3\lambda}\right)
       +2\sum_{l\ge1}3^{-l}
 =2\cos\!\left(2\pi\operatorname{Tr}
          \frac{\varepsilon\lambda^j}{3\lambda}\right)+1.
 \tag{3.4}
$$

It is three for $j=0,\varepsilon=1$, and for $j=2$ with
$\varepsilon=1,\omega,\omega^2$; it vanishes for the other five types.
This signed summation leaves exactly (1.3). It must precede absolute
bounds on the main terms.

The radial Mellin transform of (2.4) is

$$
 \mathcal M_\dagger(s)=\frac12
 \left(\frac{3\sqrt3}{2\pi}\right)^{2s}
 \frac{\Gamma(s)}{\Gamma(1-s)}\widehat\Phi(1-s).
 \tag{3.5}
$$

The root integral contributes $\mathcal M_\dagger(1/3)/3$, the good
primary lattice density is $\rho$, and the surviving packet weight is
three. Including the prefactor in (2.4) gives
$2\rho^2\mathcal M_\dagger(1/3)=C_\Phi$. This is the same cube integral
as [2, (9.35)], with all constants and the full ramified tower retained.

### 3.2. A uniform smooth root error

Split $g=g_0g_1g_2$ according to $v_p(r)=0,1,2$. Before averaging, the
exact good-prime weight is

$$
 \phi(g_0)\phi(g_2)1_{g_0\mid t}
       \prod_{p\mid g_1}(-1+q_p1_{p\mid t}),\qquad(t,uu')=1.
 \tag{3.6}
$$

Expanding the displayed product and the coprimality mask produces
lattices $e\mid t$, $t\equiv1\pmod3$, with absolute coefficient sum
at most $q_g\tau(g)\tau(uu')$. Each good $e$ is primary; hence $t=ez$
with $z\equiv1\pmod3$. Radiality removes the rotation of $e$.

The fixed function $F(z)=\Phi^\dagger(z^3)$ is radial and Schwartz,
including at zero. At norm length $L$, put $X=L/q_e$. Poisson summation
on the fixed coset $1+3\mathcal O$ gives

$$
 \sum_{z\equiv1\ (3)}F(z/\sqrt X)=c_FX+O_{F,N}(X^{-N}),\quad X\ge1.
 \tag{3.7}
$$

For $0<X<1$, the coset has positive distance from zero, so the exact
sum is $O_{F,N}(X^N)$ and the main integral is $O_F(X)$. Consequently
the discrepancy is uniformly $O_F(1)$, and is $O_F(X)$ below unit
scale. No lattice shape or translated-coset constant depends on $e$.
This is standard smooth Poisson counting, not a new counting theorem.

Here the root length is
$L=(q_nq_{n'}/(Aq_rq_{\eta}3^{3l}))^{1/3}$. Only $O(\log Y)$ ramified
levels have length at least one; the remaining errors are a geometric
tail. Taking absolute values of errors therefore costs $Y^\epsilon$,
while the signed main tower has already been summed in (3.4).

For fixed $g$ there are $O(Y^2/q_g^2)$ original column pairs, and their
common prefactor is $O(A/Y^2)$. Combining this with (3.6) and summing the
harmonic $g$ series gives $O_\epsilon(AY^\epsilon)$ per core. Hence the
complete low-root error is

$$
 O_\epsilon(ARY^\epsilon).
 \tag{3.8}
$$

Relative to $(AY)^{2/3}$ this is at most
$Y^{-\tau/3+\alpha+\epsilon}$, a strict saving. At balance it is
$Y^{1+\alpha+\epsilon}$, below $Y^{7/6}$ if $\alpha<1/6$. The high-core
error in Section 2 still has a smaller saving in general.

### 3.3. Positive squares

On squarefree indices the union kernel has the exact identity

$$
 w(mm')=w(m)w(m')\sum_{h\mid(m,m')}\frac1{\phi(h)}.
 \tag{3.9}
$$

Indeed at a common prime $1+(q_p-1)^{-1}=(1-q_p^{-1})^{-1}$.
For each $(r,\eta,d)$, (3.3) and (3.9) give

$$
 \sum_h\frac1{\phi(h)}
 \left|\sum_{h\mid m}\mu(m)w(m)\chi_m(\eta r)
                      q_m^{-1/6}V(q_dq_m/Y)\right|^2,
 \qquad(m,rE)=1.
 \tag{3.10}
$$

Write $m=h\ell$. The extracted Möbius and character factors have
modulus one on the retained support. Its squared weight divided by
$\phi(h)$ is $\phi(h)q_h^{-7/3}$. The remaining raw daughter is
$Z^{1/3}M^w_{\eta r}(Z;hrE)$, $Z=Y/(q_dq_h)$. Together with the outer
coefficient $C_\Phi A^{2/3}q_r^{-1/3}q_\eta^{-1/3}\phi(d)q_d^{-1/3}/Y$,
this gives exactly (1.7). Section 2 and (3.8) prove Theorem 1.

## 4. A positive kernel after a finite signed sieve

Expand the sieve in (1.11) as

$$
 s_y(a)=\sum_{\gamma^2\mid a}\lambda_\gamma,\qquad
 \lambda_\gamma=\sum_{\substack{q_e,q_f\le y\\\operatorname{lcm}(e,f)=\gamma}}
                    \mu(e)\mu(f).
 \tag{4.1}
$$

Then $\gamma$ is squarefree, $q_\gamma\le y^2$,
$|\lambda_\gamma|\le\tau(\gamma)^2$, and
$\lambda_\gamma=\mu(\gamma)$ for $q_\gamma\le y$. This is the finite
positive square-divisor sieve of [2, Lemma 9.2]; no infinite physical
sieve is substituted for it.

For a fixed $\gamma$, put $\Gamma=q_\gamma$. The exact row substitution
is

$$
 F_Y(\gamma^2x)=Y^{-1/2}\sum_{(n,E\gamma)=1}\mu(n)G(n)\chi_n(\gamma)
                    \overline{\chi_n(x)}V(q_n/Y),\qquad
 A_\gamma=A/\Gamma^2.
 \tag{4.2}
$$

The two column twists in its norm combine into
$\chi_u(\gamma)\overline{\chi_{u'}(\gamma)}$, making the effective
label $\gamma gk$. In particular $(g,\gamma)=1$.
For a low core write
$\gamma gk=\varepsilon\lambda^{3l+j}rt^3$, with
$\gamma g\mid rt^3$. At primes of $g$, (3.2) is unchanged. At a prime
$p\mid\gamma$, the columns are coprime to $p$ and integrality imposes
$p\mid t$ exactly when $p\nmid r$. The extra mean is $q_p^{-1}$
outside $r$ and one at primes of $r$.

The root length is now

$$
 L_\gamma=\Gamma
     \left(\frac{q_nq_{n'}}{Aq_rq_\eta3^{3l}}\right)^{1/3}.
 \tag{4.3}
$$

Indeed its cubed norm argument is
$Aq_\eta q_rq_t^3/(\Gamma^3q_nq_{n'})$. The scalar $A_\gamma/Y$ and
the extra $\Gamma$ in (4.3), together with the local integrality means,
produce precisely

$$
 a_r(\gamma)=\frac{q_{(\gamma,\operatorname{rad}r)}}{q_\gamma^2}.
 \tag{4.4}
$$

The signed unit and ramified tower is unchanged since
$\gamma g\equiv1\pmod3$. The variables $d=(b,n)=(b,n')$, $n=dm,n'=dm'$
now retain $(\gamma,dmm')=1$ as well as $(mm',rE)=1$. Define

$$
 \begin{aligned}
 c_{r,\eta,d}(m)&=\mu(m)\chi_m(\eta r)q_m^{-1/6}V(q_dq_m/Y),\\
 K_{y,r,d}(m,m')&=w(mm')
           \sum_{(\gamma,dmm')=1}\lambda_\gamma a_r(\gamma),\\
 \mathcal P_y(A,Y;R)&=\frac{C_\Phi A^{2/3}}Y
 \sum_{\substack{r=ab^2\ {\rm cf}\\q_r\le R}}q_r^{-1/3}
 \sum_{\eta\in\mathcal T}q_\eta^{-1/3}
 \sum_{\substack{d\mid b\\(d,E)=1}}\phi(d)q_d^{-1/3}\\
 &\hspace{12mm}\times\sum_{m,m'}c_{r,\eta,d}(m)
                 \overline{c_{r,\eta,d}(m')}K_{y,r,d}(m,m').
 \end{aligned}
 \tag{4.5}
$$

Both columns in (4.5) are squarefree and coprime to $rE$. The signed
sieve coefficients have been combined before taking norms.

### 4.1. A product-measure proof of positivity

At each prime $p\nmid r$, use independent local states $S,C,O$ with
probabilities

$$
 \mathbb P(S)=q_p^{-2},\qquad
 \mathbb P(C)=1-q_p^{-1},\qquad
 \mathbb P(O)=q_p^{-1}-q_p^{-2}.
 \tag{4.6}
$$

At a prime of $r$, only the sieve event is needed, of probability
$q_p^{-1}$. All primes are independent. Define

$$
 A_{y,d}=\sum_{\substack{q_e\le y\\(e,d)=1}}\mu(e)
                         \prod_{p\mid e}1_{S_p},\qquad
 B_m=\prod_{p\mid m}1_{C_p}.
 \tag{4.7}
$$

Only finitely many primes are needed for the finite cutoff and column
set. Since $S_p,C_p$ are disjoint, expansion gives

$$
 K_{y,r,d}(m,m')=\mathbb E[A_{y,d}^{2}B_mB_{m'}],\qquad
 \sum_{m,m'}c_m\overline{c_{m'}}K_{y,r,d}(m,m')
     =\mathbb E\left[A_{y,d}^{2}\left|\sum_m c_mB_m\right|^2\right]\ge0.
 \tag{4.8}
$$

This proves positivity for every finite squarefree coefficient, despite
the nonmultiplicative norm cutoff on $e,f$. The local Gram matrix on
$(e_p,m_p)=(0,0),(1,0),(0,1)$ is

$$
 \begin{pmatrix}
 1&q^{-2}&1-q^{-1}\\
 q^{-2}&q^{-2}&0\\
 1-q^{-1}&0&1-q^{-1}
 \end{pmatrix},
 \quad \det=q^{-2}(1-q^{-1})(q^{-1}-q^{-2})>0.
 \tag{4.9}
$$

The absent $(1,1)$ state is exactly the column zero mask in (4.2).
Primes of $d$ forbid the sieve state; because $d\mid b\mid r$, this
removes a factor $1-q_p^{-1}$, not $1-q_p^{-2}$.

### 4.2. The infinite arithmetic kernel

The sum of sieve-event probabilities outside the finite set of primes
of $r$ converges. Let $I_d$ indicate that no sieve event occurs outside
$d$. On this event $A_{y,d}=1$; otherwise $A_{y,d}^2\ge0$. Thus the
finite kernel dominates $\mathbb E[I_dB_mB_{m'}]$ in Loewner order.
Local conditioning gives

$$
 K_{y,r,d}\succeq K_{\infty,r,d},\qquad
 K_{\infty,r,d}(m,m')=Z_2^{-1}\frac{v(r)}{w(d)}v(mm').
 \tag{4.10}
$$

This is not monotonicity in $y$, and is not an extension of the physical
sieve. Equivalently the infinite arithmetic kernel is the absolutely
convergent Euler sum obtained by replacing $\lambda_\gamma$ in (4.5)
by $\mu(\gamma)$.

The identity

$$
 v(mm')=v(m)v(m')\sum_{h\mid(m,m')}q_h^{-1}
 \tag{4.11}
$$

now yields (1.12) at $A=Y,E=1$. Indeed $1/w(d)$ in (4.10) changes
$\phi(d)$ to $q_d$; the daughter normalization cancels the remaining
$q_d^{2/3}$. The $h$ weight is $v(h)^2/q_h^2$. This accounts for both
weights without dropping shared primes. Each $(r,\eta,d)$ form remains
nonnegative.

## 5. Uniform errors for the moving sieve divisor

We prove the analytic formula

$$
 \mathcal N_y(Y,Y):=\sum_a s_y(a)\Phi(q_a/Y)|F_Y(a)|^2
     =\mathcal P_y(Y,Y;Y^\alpha)+O(Y^{4/3-\eta_m}).
 \tag{5.1}
$$

Choose the source constants of Section 2 with its common deletion
exponent enlarged. Choose a reserved row dilation
$0<\rho_0\le\varrho<\min(\theta_0,\kappa_1)/100$, then reduce
$\alpha,\delta$ in (2.6) and choose

$$
 0<\nu<\delta/100,\qquad y=Y^\nu,
 \qquad4\nu+\rho_0+\delta(1+\theta_0)<\theta_0.
 \tag{5.2}
$$

Also $2\nu+2\delta<\kappa_1$. These strict inequalities keep every
$A_\gamma=Y/\Gamma^2$, $\Gamma\le y^2$, inside the required neighborhood.
The fixed row and column seminorms affect constants, not this choice.

With cross-divisor $s$ and Ramanujan divisor $\ell\mid g$, the daughter
length and moving row parameters are

$$
 Z=Y/(q_gq_s),\qquad P_\gamma=\Gamma^2Y,\qquad
 K_\gamma=P_\gamma/(q_gq_\ell),\qquad v_0=\gamma g\ell.
 \tag{5.3}
$$

The outside scalar is (2.5) with $A$ replaced by $A_\gamma$; there is
no new coefficient mass. The common deletion is $gsE\gamma$.
For $q_gq_s\le Y^\delta$, a high effective core forces the core of
$k'$ above $Y^{\alpha-2\nu-2\delta}$. The three estimates (2.7) apply,
including the extra numerator $\gamma$, by (5.2). Multiplication by
the exact scalar leaves

$$
 Y^{4/3}\Gamma^{-4/3}q_\ell^{2/3}q_g^{-7/3}q_s^{-2}.
 \tag{5.4}
$$

All divisor sums converge, including
$\sum_\gamma\tau(\gamma)^2\Gamma^{-4/3}$. Thus this part has a fixed
power saving after the full finite signed-sieve sum.

For $q_gq_s>Y^\delta$, form the common Sobolev majorant and reindex
$j=\gamma g\ell k'$. Its scale is $\Gamma^3Y$, not $\Gamma^2Y$.
The $g,\ell$ fibre is divisor-bounded, and the $\gamma$ deletion is
redundant in $j$; the remaining $sE$ deletion is common. Multiplying
(2.3), at row length $\Gamma^3Y$ and column length at most
$Y^{1-\delta}$, by $A_\gamma/Y=\Gamma^{-2}$ gives per $\gamma$

$$
 Y^\epsilon\left[\Gamma Y+Y^{4/3-2\delta/3}
                              +\Gamma^{-1}Y^{4/3-\delta}\right].
 \tag{5.5}
$$

Summing $|\lambda_\gamma|\le\tau(\gamma)^2$ for $\Gamma\le y^2$ gives

$$
 Y^\epsilon\left[Y^{1+4\nu}
             +Y^{4/3-2\delta/3+2\nu}+Y^{4/3-\delta}\right].
 \tag{5.6}
$$

All exponents are strictly below $4/3$. Common Fourier and dilation
tails use the same rapid fixed transform decay as Section 2.

For low cores, (4.3) and the extra integrality at $\gamma$ only add a
divisibility lattice; they do not enlarge the coefficient sum in (3.6).
The smooth discrepancy (3.7) therefore gives per $(\gamma,r)$ an error
$O_\epsilon(A\Gamma^{-2}Y^\epsilon)$. Summing the convergent
$\sum_\gamma\tau(\gamma)^2\Gamma^{-2}$ and $q_r\le R$ gives
$O_\epsilon(ARY^\epsilon)$, equal to $O(Y^{1+\alpha+\epsilon})$ at
balance. The zero-frequency term is $O(Y^{1+\epsilon})$ after the
finite sieve sum. Equations (5.4)–(5.6) and these low errors prove (5.1)
for some fixed $\eta_m>0$, after choosing subsidiary losses last.


## 6. Removing the finite arithmetic sieve with a sharper tail

Set $A=Y,E=1$ and retain $R=Y^\alpha$. The positivity in Section 4 gives
a nonnegative difference. We prove

$$
 0\le\mathcal P_y(Y,Y;R)-\mathcal P^v(Y;R)
       \ll_\epsilon Y^{4/3+\epsilon}/y.
 \tag{6.1}
$$

The order of operations matters: sum the part of the sieve divisor
already in the character label before applying the ordinary character
sieve. Taking $a_r(\gamma)\le\Gamma^{-1}$ first would lose this bound.

For a fixed squarefree $\gamma$, the positive-square form from Section 3
has the contribution

$$
 \begin{aligned}
 Q_\gamma(R)={}&C_\Phi Y^{1/3}
 \sum_{\substack{r=ab^2\ {\rm cf}\\q_r\le R}}q_r^{-1/3}a_r(\gamma)
 \sum_{\eta\in\mathcal T}q_\eta^{-1/3}
 \sum_{\substack{d\mid b\\(d,\gamma)=1}}\frac{\phi(d)}{q_d}\\
 &\times\sum_{\substack{h\ {\rm sf}\\(h,r\gamma)=1}}
 \frac{\phi(h)}{q_h^3}
 \left|M^w_{\eta r}\left(\frac{Y}{q_dq_h};hr\gamma\right)\right|^2.
 \end{aligned}
 \tag{6.2}
$$

Each $Q_\gamma$ is nonnegative. The fixed-core sum
$\sum_\gamma\tau(\gamma)^2a_r(\gamma)$ converges, and the columns are
finite. Thus the Euler product and all following absolute rearrangements
are justified. We have exactly

$$
 \mathcal P_y(Y,Y;R)-\mathcal P^v(Y;R)
       =\sum_\gamma(\lambda_\gamma-\mu(\gamma))Q_\gamma(R).
 \tag{6.3}
$$

Its coefficient vanishes for $q_\gamma\le y$ and is at most
$2\tau(\gamma)^2$ in absolute value.

### 6.1. Recombine the overlapping divisor

For each $(r,\gamma)$, write

$$
 t=(\gamma,\operatorname{rad}r),\quad\gamma=tu,\quad
 t\mid\operatorname{rad}r,\quad(u,r)=1,
 \qquad a_r(\gamma)=\frac1{q_tq_u^2}.
 \tag{6.4}
$$

The $t$ deletion is already imposed by $r$:
$(m,hr\gamma)=1$ is equivalent to $(m,hru)=1$. There is no extra $t$
twist in (6.2); the low character is $\chi_m(\eta r)$. In a positive
upper bound, drop the outer $(d,t)=1$ restriction. The $(h,t)=1$
restriction is already forced by $(h,r)=1$.

For any fixed $0<\xi<1$, Rankin's inequality gives
$1_{q_tq_u>y}\le(q_tq_u/y)^\xi$. Hence

$$
 \sum_{t\mid\operatorname{rad}r}\tau(t)^2q_t^{-1+\xi}
   =\prod_{p\mid r}(1+4q_p^{-1+\xi})\ll_{\xi,\epsilon}q_r^\epsilon,
 \qquad
 \sum_u\tau(u)^2q_u^{-2+\xi}<\infty.
 \tag{6.5}
$$

After summing $t$, also drop $(u,r)=1$ in the positive bound.
The conditions $(d,u)=(h,u)=1$ may be kept; they are common once
$u,d,h$ are fixed. The entire positive tail in (6.3) is now bounded
by $y^{-\xi}$ times a convergent $u$ series and a low-core square sum
with only $q_r^\epsilon$ extra weight. The remaining deletion $u$ can
be arbitrarily large, since the next estimate uses coefficient mass.

### 6.2. Sum every daughter scale

Fix $u,d,h$ and a dyad $S<q_r\le2S$. Since $d\mid b$, put $r=d^2j$,
where $j$ is cube-free and $(d,j)=1$. The inverse sum in (6.2) becomes

$$
 Z^{-1/2}\sum_{(m,dhu)=1}\mu(m)w(m)\chi_m(\eta d^2)
    \chi_m(j)(q_m/Z)^{-1/6}V(q_m/Z),\qquad Z=Y/(q_dq_h).
 \tag{6.6}
$$

The $j$ deletion is the literal zero of its character. All other
coefficients are common across $j$. Enlarge the positive row sum to
$q_j\le2S/q_d^2$ and apply the ordinary primitive-character sieve.
The normalized mean is at most

$$
 O\!\left(Z+(S/q_d^2)^2\right).
 \tag{6.7}
$$

The possible principal row is bounded by $O(Z)$. Nonempty subunit
daughters satisfy the same bound after a fixed change in constant;
empty daughters vanish. No common-deletion norm cost occurs in (6.7).

Multiplying by the weights in (6.2), the two terms of (6.7) contribute

$$
 \begin{aligned}
 &Y^{4/3}S^{-1/3}
 \sum_{q_d\le\sqrt{2S}}\frac{\phi(d)}{q_d^2}
 \sum_h\frac{\phi(h)}{q_h^4}\\
 &\quad+Y^{1/3}S^{5/3}
 \sum_d\frac{\phi(d)}{q_d^5}
 \sum_h\frac{\phi(h)}{q_h^3}
 \ll_\epsilon Y^\epsilon
          [Y^{4/3}S^{-1/3}+Y^{1/3}S^{5/3}].
 \end{aligned}
 \tag{6.8}
$$

Only the first $d$ sum is harmonic. Both $h$ sums and the second $d$
sum converge. Dyadic summation, including the unit core, is
$O_\epsilon(Y^\epsilon[Y^{4/3}+Y^{1/3}R^{5/3}])$. With (6.5) this
proves (6.1): choose $\xi$ sufficiently close to one after the requested
epsilon is fixed, and absorb $y^{1-\xi}$ and the other divisor subpowers
into $Y^\epsilon$. Since $\alpha<1/40$, the $R$ term is smaller.

The same calculation, starting directly with (1.12), gives

$$
 0\le\mathcal P^v(Y;R)-\mathcal P^v(Y;T)
 \ll_\epsilon Y^\epsilon
       [Y^{4/3}T^{-1/3}+Y^{1/3}R^{5/3}],\qquad1\le T\le R.
 \tag{6.9}
$$

The coefficient is now $\mu v$, the $d$ sums are $\sum q_d^{-1}$ and
$\sum q_d^{-4}$, and the $h$ sums are
$\sum v(h)^2q_h^{-3}$ and $\sum v(h)^2q_h^{-2}$. Both converge.
Thus no auxiliary truncation of $h$ is needed. Equations (6.1) and (6.9)
concern arithmetic kernels after the norm transform. They do not bound
$\mathcal E_y-\mathcal E_{\rm sf}$.

## 7. The full polar cross comparison

We give the inherited principal cancellation with its full moving-mask
error, to make the application to Theorem 2 inspectable. This section
uses [4, Lemmas 6.6–6.7], with no principal Möbius power hypothesis.
The argument works for arbitrary bounded squarefree $\beta$ on
$q_n\asymp Y$, hence for the actual coefficient in (1.10).

Define the unnormalized quadratic form

$$
 \mathcal Q_Y(\beta)=\sum_{b,c}\frac{\beta_b\overline{\beta_c}}
                                    {(q_bq_c)^{1/6}}v(bc),
 \qquad
 \mathcal L_Y=\frac{C_\Phi}{Z_2}Y^{2/3}\mathcal Q_Y(\beta).
 \tag{7.1}
$$

The squared polar norm satisfies

$$
 \|P\beta\|_\Phi^2=\mathcal L_Y+O_\epsilon(Y^{11/6+\epsilon}).
 \tag{7.2}
$$

To see this, open its square and use the uniform squarefree count

$$
 \sum_{(a,m)=1}\mu(a)^2\Phi(q_a/Y)q_a^{-1/3}
 =\frac{\rho}{Z_2}Y^{2/3}\widehat\Phi(2/3)v(m)
                      +O_\epsilon(Y^{1/6+\epsilon}q_m^\epsilon).
 \tag{7.3}
$$

Expand the squarefree indicator and the finite coprimality mask; smooth
primary counting and the square-divisor split at $\sqrt Y$ give error
$O(Y^{1/2+\epsilon}q_m^\epsilon)$ before the weight. The absolute
column-pair mass is $O(Y^{5/3})$, proving (7.2).

For the cross term $X_Y=\langle K\beta,P\beta\rangle_\Phi$, the
squarefree row indicator is redundant because $P$ contains $G(a)$.
Gauss multiplicativity gives the exact expression

$$
 X_Y=c_3\sum_{b,c}\frac{\beta_b\overline{\beta_c}}{q_c^{1/6}}
                      F_{b,c}(Y),\qquad
 F_{b,c}(Y)=\sum_{(a,c)=1}\Phi(q_a/Y)q_a^{-1/6}G(ab).
 \tag{7.4}
$$

Put $c'=c/(b,c)$. The Gauss factor already forces $(a,b)=1$. In
[4, Lemma 6.7], use numerator $b$, squared numerator part one,
additional puncture $c'$, length $Y$, and $\sigma=2/3$.
The numerator there is $b(c')^3$; its cube retains exactly the
additional zero mask. The full pole and remainder give

$$
 \begin{aligned}
 F_{b,c}(Y)&=C_1\widehat\Phi(2/3)Y^{2/3}q_b^{-1/6}v(bc)+E_{b,c},
 \qquad C_1=\rho c_3/Z_2,\\
 |E_{b,c}|&\ll_\epsilon Y^{1/3+\epsilon}
 \sum_{d\mid b}\sum_{e\mid c'}(q_dq_e)^{-1/2-\epsilon}
 \int_{\mathbb R}\frac{|\psi(be/d,1+\epsilon+iu)|}{(1+|u|)^J}\,du.
 \end{aligned}
 \tag{7.5}
$$

Here $\psi$ is the Kubota series of [4]; its normalization is unchanged.
The printed pole contains the conjugate Gauss factor, canceled in
(7.5) by $G(b)$. The source constant and its local ratio
$\Delta_m(1)/\Delta_m(4/3)=v(m)$ give the full union factor $v(bc)$,
including shared primes.

The moving-numerator mean [4, Lemma 6.6] is

$$
 \sum_{0<q_m\le M}|\psi(hm,\sigma+iu)|^2
 \ll_{\sigma,\epsilon}q_h^{1/2}M^{1+\epsilon}(1+|u|)^2,
 \qquad1<\sigma\le5/4.
 \tag{7.6}
$$

Keep both divisor sums in (7.5). For each $e$ there are $O(Y/q_e)$
possible $c$. Write $b=dm$, use $q_c^{-1/6}\ll Y^{-1/6}$, and apply
Cauchy and (7.6) to the $m$ sum. The aggregate cross error is at most

$$
 \begin{aligned}
 &Y^{1/3+\epsilon}Y^{5/6}
 \sum_{d,e}q_d^{-1/2}q_e^{-3/2}
 \int_{\mathbb R}\frac{
       \sum_{q_m\ll Y/q_d}|\psi(em,1+\epsilon+iu)|}{(1+|u|)^J}\,du\\
 &\qquad\ll Y^{13/6+\epsilon}
          \sum_dq_d^{-3/2}\sum_eq_e^{-5/4}
 \ll Y^{13/6+\epsilon}.
 \end{aligned}
 \tag{7.7}
$$

Both ideal series converge. Choose $J$ sufficiently large once; empty
quotients vanish and constant-size terminal ranges satisfy the same
bound. Thus

$$
 X_Y=\mathcal L_Y+O_\epsilon(Y^{13/6+\epsilon}).
 \tag{7.8}
$$

The finite sieve is exactly one on squarefree rows. Since $P$ vanishes
on other rows, both (7.2) and (7.8) are unchanged when the row norm is
weighted by $s_y$. The single principal term of (1.12) equals
$\mathcal L_Y/Y$. This follows either from (4.10) at $r=d=1$ or by
opening (1.12) using (4.11). Consequently (5.1), (6.1), (7.2) and
(7.8) give

$$
 \mathcal E_y=\mathcal P^{v,\rm np}(Y;R)
 +O_\epsilon(Y^{4/3-\eta_m}+Y^{4/3+\epsilon}/y+Y^{7/6+\epsilon}).
 \tag{7.9}
$$

This is (1.13). Applying (6.9) with $T=y^3\le R$ proves (1.14), after
reducing the saving exponent. In our range $Y^{1/3}R^{5/3}$ is at most
$Y$. Theorem 2 is proved. This is the cancellation of three computed
principal main terms; it does not estimate the nonprincipal model or
the physical sieve excess.


## 8. A physical vector for each fixed nonprincipal class

Write the fixed good cube-free label as $r=ab^2$, with $a,b$ squarefree
and coprime, and fix $\eta\in\mathcal T$, $(r,\eta)\ne(1,1)$.
All constants in this section may depend on these fixed labels.
Set

$$
 I_\Phi=\widehat\Phi(2/3),\quad L=Y/q_b,\quad
 k_{ab}=\frac{\rho}{Z_2}v(ab),\quad D=\sqrt{k_{ab}I_\Phi}\,L^{1/3}.
 \tag{8.1}
$$

Define a vector on the actual squarefree physical rows by

$$
 z_{\eta,a,b}(c)=
 \begin{cases}
 D^{-1}\overline{G(x)}\chi_x(\eta a)q_x^{-1/6},
                    &c=bx\text{ squarefree},\\
 0,&b\nmid c.
 \end{cases}
 \tag{8.2}
$$

The original character forces $(x,a)=1$. Squarefree counting with
fixed exclusion $ab$ gives
$\|z\|_\Phi^2=1+O_{a,b,\epsilon}(Y^{-1/2+\epsilon})$.
The adjoint is taken with respect to the weighted physical row norm and
the ordinary column norm. We prove

$$
 C^*z(n)=A_{\eta,a,b}Y^{1/3}v(n)q_n^{-1/6}
                     \overline{\chi_n(\eta ab^2)}+e(n),
 \quad A_{\eta,a,b}\ne0,
 \quad\sum_{q_n\asymp Y}^{\rm sf}|e(n)|^2\ll_{\eta,a,b,\epsilon}Y^{1+\epsilon}.
 \tag{8.3}
$$

### 8.1. The exact adjoint and its pole

Cubic reciprocity gives

$$
 K^*z(n)=D^{-1}\overline{G(n)}\chi_n(b)\overline{S_n},\qquad
 S_n=\sum_{(x,b)=1}G(x)\overline{\chi_x(\eta an)}
                              q_x^{-1/6}\Phi(q_x/L).
 \tag{8.4}
$$

The sum may include natural good $x$ because $G(x)$ vanishes off the
squarefree support. If $(n,b)>1$, the exterior factor is zero.
Otherwise write $g=(n,a)$, $n=gn_0$, $a=ga_0$. The good numerator is
$\eta g^2a_0n_0$. The truncated Gauss formula [4, Lemma 6.7], with
$\sigma=2/3$ and puncture $b$, has no pole unless $g=1$.
For $(n,ab)=1$ the pole is

$$
 S_n^{\rm pole}=C_\eta I_\Phi L^{2/3}
       \overline{G_\eta(an)}(q_aq_n)^{-1/6}v(anb),
 \qquad G_\eta(c)=\overline{\chi_c(\eta)}G(c).
 \tag{8.5}
$$

Every $C_\eta$ for $\eta\in\mathcal T$ is nonzero. These are exactly
the four nonzero cases of Patterson's $\tau_3$ in [4, (6.8)], inserted
in the residue formula of its Lemma 6.3. The three valuation-two types
retain their unit phases. No equality of these complex constants is
needed. The conjugation in (8.5) is the one printed in the source.

On $(n,ab)=1$, Gauss multiplicativity gives

$$
 \overline{G(n)}\chi_n(b)G_\eta(an)
   =G(a)\overline{\chi_a(\eta)}
                   \overline{\chi_n(\eta ab^2)}.
 \tag{8.6}
$$

Also $v(anb)=v(ab)v(n)$. Substitution into (8.4) gives the main term
in (8.3), with the explicit nonzero constant

$$
 A_{\eta,a,b}=
 \frac{\overline{C_\eta}I_\Phi v(ab)G(a)\overline{\chi_a(\eta)}
                       q_a^{-1/6}q_b^{-1/3}}{\sqrt{k_{ab}I_\Phi}}.
 \tag{8.7}
$$

When $n$ meets $a$, the squared numerator part kills the pole; when
$n$ meets $b$, the exterior factor in (8.4) vanishes. These are precisely
the zeros of the main character in (8.3).

### 8.2. Full fixed-label remainder and the ordinary polar map

Keep every $g\mid a$ separately. The squarefree and squared numerator
parts in [4, Lemma 6.7] are $a_0n_0$ and $g$, and the puncture is $b$.
Its error is bounded by

$$
 L^{1/3+\epsilon}
 \sum_{d\mid a_0n_0}\sum_{f\mid b}(q_dq_f)^{-1/2-\epsilon}
 \int_{\mathbb R}\frac{|\psi(\eta a_0n_0g^2f/d,1+\epsilon+iu)|}
                              {(1+|u|)^J}\,du.
 \tag{8.8}
$$

The mask $(n,b)=1$ is still present. Apply Cauchy to the divisor sum
with its divisor subpower and to $u$ with its common integrable weight.
Split $d=d_ad_n$, $d_a\mid a_0$, $d_n\mid n_0$, and write $n_0=d_nm$.
The Kubota numerator becomes $hm$ with
$h=\eta(a_0/d_a)g^2f$ fixed. The mean (7.6) therefore gives

$$
 \sum_{n\asymp Y}^{\rm sf}|S_n-S_n^{\rm pole}|^2
 \ll_{\eta,a,b,\epsilon}L^{2/3+\epsilon}Y^{1+\epsilon}
                         \sum_{d_n}q_{d_n}^{-2}
 \ll_{\eta,a,b,\epsilon}L^{2/3+\epsilon}Y^{1+\epsilon}.
 \tag{8.9}
$$

For each $d_n$, the nonnegative $m$ sum is extended to all
$q_m\ll Y/(q_gq_{d_n})$ before applying (7.6), so dropping its
squarefree and coprimality masks is justified by positivity.
The $d_a,f,g$ sums are finite fixed-label costs; neither the overlap
sectors nor either original divisor sum has been omitted. The mean's
height growth is quadratic, so a fixed sufficiently large $J$ suffices.
Dividing by $D^2\asymp L^{2/3}$ proves the $Y^{1+\epsilon}$ error norm
for $K^*z$ in (8.3).

For $P^*z$, the identity
$G(bx)\overline{G(x)}=G(b)\overline{\chi_x(b)}$ leaves the nonprincipal
row character $\chi_x(\eta ab^2)$. The original mask $(n,bx)=1$ stays.
For this fixed character, the squarefree Dirichlet series is
$L(s,\psi)/L(2s,\psi^2)$, with the corresponding finite deleted Euler
factors. It is holomorphic for $\Re s>1/2$, since $\psi$ is nonprincipal
and the denominator has no zero for $\Re(2s)>1$. Finite deletions cost
$q_n^\epsilon$ on a fixed line. Mellin shifting with ordinary polynomial
vertical growth gives

$$
 \sum_{\substack{x\ {\rm sf}\\(x,nb)=1}}
 \chi_x(\eta ab^2)q_x^{-1/3}\Phi(q_x/L)
       \ll_{\eta,a,b,\epsilon}L^{1/6+\epsilon}q_n^\epsilon.
 \tag{8.10}
$$

The exterior factors are $D^{-1}q_b^{-1/6}q_n^{-1/6}$ times a fixed
constant. Hence $\|P^*z\|_2^2\ll Y^{1/3+\epsilon}$, smaller than
(8.9)'s normalized error. This proves (8.3) for $C=K-P$.
The nonprincipal condition is needed here; $P$ cancels the ordinary
principal mode.

### 8.3. Detection on the actual coefficient

Use $\|\beta\|_2\ll_VY^{1/2}$ in (8.3). With the standard convention
$\langle f,g\rangle=\sum f\overline g$, we obtain

$$
 \langle C\beta,z\rangle_\Phi
 =\overline{A_{\eta,a,b}}Y^{2/3}M^v_{\eta r}(Y;r)
                      +O_{\eta,a,b,V,\epsilon}(Y^{1+\epsilon}).
 \tag{8.11}
$$

The identity used is
$\sum\mu(n)v(n)\chi_n(\eta r)q_n^{-1/6}V(q_n/Y)
=Y^{1/3}M^v_{\eta r}(Y;r)$. Since $\|z\|_\Phi\ll1$, squaring (8.11)
and dividing by $Y$ proves Theorem 3. This argument uses no growing
frame and does not estimate the physical sieve excess.

## 9. Physical realization of the complete model

### 9.1. Physical coordinates and their exact local weights

We now prove Theorem 4. Put $r=ab^2$ with $a,b$ squarefree and coprime, $q_r\le R$, and
$\eta\in\mathcal T$. Exclude $(r,\eta)=(1,1)$. For each $d\mid b$ put
$t=b/d$. For squarefree $h$ with $(h,r)=1$, $q_h\le H$, define

$$
 \begin{aligned}
 L&=Y/q_t,& k_r&=(\rho/Z_2)v(ab),& I&=\widehat\Phi(2/3),
 &D&=\sqrt{k_rI}\,L^{1/3},\\
 H_h(x)&=q_h^{-1/2}\prod_{p\mid h}[(q_p+1)1_{p\mid x}-1],\\
 z_i(c)&=D^{-1}\overline{G(x)}\chi_x(\eta ad^2)q_x^{-1/6}H_h(x),
       \quad c=tx\text{ squarefree},
 \end{aligned}
 \tag{9.1}
$$

with $z_i(c)=0$ otherwise and $i=(\eta,r,d,h)$. The character and
squarefree row support require $(x,ab)=1$. Thus
$\gcd(c,b)=t$ exactly; different $d$ for the same $r$ have disjoint
supports. The weight $v(ab)=v(r)$ is bounded below by $q_r^{-\epsilon}$
for every fixed $\epsilon>0$.

The local squarefree probability at a prime outside $r$ is
$\pi_p=1/(q_p+1)$. Therefore the centered factors in (9.1) have mean
zero and variance one. Products for distinct squarefree $h$ are
orthonormal in the limiting product measure. Their finite expansion is

$$
 H_h(x)=q_h^{-1/2}\sum_{e\mid h}\mu(h/e)
                   \prod_{p\mid e}(q_p+1)1_{e\mid x},
 \qquad\sum_{e\mid h}|c_{h,e}|\ll_\epsilon q_h^{1/2+\epsilon}.
 \tag{9.2}
$$

All indicators are on the actual physical row quotient $x=c/t$.
No independent-prime approximation is made for the finite row set;
the limiting moments will be justified by uniform counting below.

### 9.2. Exact adjoint residue, including all d and h

For the base coordinate $h=1$, the exact adjoint is

$$
 K^*z_i(n)=D^{-1}\overline{G(n)}\chi_n(t)\overline{S_n},\qquad
 S_n=\sum_{(x,t)=1}G(x)\overline{\chi_x(\eta ad^2n)}
                                      q_x^{-1/6}\Phi(q_x/L).
 \tag{9.3}
$$

The source pole is present precisely for $n=dm$ with $(m,ab)=1$.
Indeed every prime of $d$ must turn its numerator valuation two into
three; an overlap with $a$ produces valuation two and kills the pole;
an overlap with $t$ is killed by the exterior character.
In the supported sector, the source squarefree part is $am$ and its
full cube puncture is $b$. Gauss multiplicativity yields the main term

$$
 K^*z_i(dm)=A_{\eta,r,d}Y^{1/3}v(m)q_m^{-1/6}
                  \overline{\chi_m(\eta r)}+e_i(dm),
 \tag{9.4}
$$

where

$$
 A_{\eta,r,d}=
 \frac{\overline{C_\eta}I v(ab)\overline{G(d)}G(a)
        \chi_d(t)\overline{\chi_a(\eta)}
          q_a^{-1/6}q_t^{-1/3}}{\sqrt{k_rI}}.
 \tag{9.5}
$$

All other columns have zero main term. From the four explicit cases of
Patterson's $\tau_3$ in [4, (6.8) and Lemma 6.3],

$$
 |C_\eta|=\frac{\rho c_3}{Z_2}q_\eta^{-1/6},\qquad
 |A_{\eta,r,d}|^2=
 \frac{C_\Phi}{Z_2}q_\eta^{-1/3}v(r)
                         q_a^{-1/3}q_t^{-2/3}.
 \tag{9.6}
$$

The valuation-two unit phases are retained in (9.5); only their modulus
is needed in (9.6). All four coefficients are nonzero. More explicitly, the source derives
$C_\eta=c_0c_\eta/q_\eta^{1/6}$ with $|c_\eta|=27$ in the four
cases ([4], end of page 38 and beginning of page 39); and
$27c_0=\rho c_3/Z_2$. This supplies the magnitude in (9.6), not merely
nonvanishing.

Now impose $e\mid x$ for one summand of (9.2). Substituting $x=ez$ and
using Gauss multiplicativity changes the numerator to
$\eta ad^2en$, the exterior row prefix to $te$, and the length to
$L/q_e$. The resulting residue is the base residue (9.4) times

$$
 \prod_{p\mid e}(q_p+1)^{-1}\,1_{(m,e)=1}.
 \tag{9.7}
$$

For clarity, its additional phase equals
$\chi_e(\eta ad^2)\overline{\chi_e(am)}
\overline{\chi_e(\eta)}\chi_e(dm)=\chi_e(d^3)=1$.
Its norm factors give $q_e^{-1}v(e)=\prod_{p\mid e}(q_p+1)^{-1}$.
When $m$ meets $e$, the exterior character is zero. Thus every original
mask in (9.7) is forced by the exact adjoint.

Summing (9.7) with (9.2) leaves precisely

$$
 q_h^{-1/2}\sum_{e\mid h}\mu(h/e)1_{(m,e)=1}
       =\frac{\mu(h)}{\sqrt{q_h}}1_{h\mid m}.
 \tag{9.8}
$$

Consequently the full adjoint main term for $i=(\eta,r,d,h)$ is

$$
 T_i(n)=A_{\eta,r,d}Y^{1/3}v(m)q_m^{-1/6}
 \overline{\chi_m(\eta r)}\frac{\mu(h)}{\sqrt{q_h}}
          1_{n=dm}\,1_{(m,r)=1}\,1_{h\mid m}.
 \tag{9.9}
$$

The uniform remainder will be proved in Section 9.4, including subtraction
of $P^*z_i$. For now take $\beta_n=\mu(n)V(q_n/Y)$ and put
$A_i=\langle\beta,T_i\rangle$. Write $m=h\ell$ in (9.9); all extracted
Möbius and character factors have modulus one. The remaining daughter
is $Z^{1/3}M^v_{\eta r}(Z;hr)$, $Z=Y/(q_dq_h)$. Using $td=b$, (9.6) gives

$$
 \frac{|A_i|^2}{Y}=
 \frac{C_\Phi}{Z_2}Y^{1/3}q_r^{-1/3}v(r)q_\eta^{-1/3}
       \frac{v(h)^2}{q_h^2}
 \left|M^v_{\eta r}\left(\frac{Y}{q_dq_h};hr\right)\right|^2.
 \tag{9.10}
$$

This is each individual summand of(1.12), with unit $d$ weight.
It is an equality of main coefficients and does not itself assert a
physical norm asymptotic.


### 9.3. Uniform Gram estimate for a short growing family

Let $\mathcal I(R,H)$ contain the coordinates above, and assume
$R,H\ge2$ and $R^2H^2\le Y^{1/2}$, a much weaker condition than our
final small exponents. Its cardinality satisfies

$$
 |\mathcal I(R,H)|\ll_\epsilon RH(RH)^\epsilon.
 \tag{9.11}
$$

We claim the actual weighted Gram matrix obeys the safe polynomial bound

$$
 \|\operatorname{Gram}(z_i)-I\|
       \ll_\epsilon Y^{-1/2+\epsilon}(RH)^{4+\epsilon}.
 \tag{9.12}
$$

Only a fixed power of $RH$ is needed; no attempt is made to optimize it.
We prove a stronger entry bound below, so (9.12) has room for all fixed
factor and divisor costs.

#### 9.3.1. The free row character

On the support $c=tx$, twisted multiplicativity gives

$$
 \overline{G(x)}\chi_x(\eta ad^2)
       =G(t)\overline{G(c)}\chi_x(\eta r).
 \tag{9.13}
$$

The remaining scalar in (9.1), expressed in $c$, is
$Y^{-1/3}q_t^{1/2}q_c^{-1/6}/\sqrt{k_rI}$.
For another coordinate $i'=(\eta',r',d',h')$ write
$t=ju$, $t'=ju'$, $(u,u')=1$, and $f=[t,t']=juu'$.
On common squarefree row support $c=fz$, the quotients are
$x=u'z$, $x'=uz$. If $(u',r)>1$ or $(u,r')>1$ the product is identically
zero. Otherwise (9.13) shows that its free-row character is exactly

$$
 \chi_z(\eta r)\overline{\chi_z(\eta'r')},
 \tag{9.14}
$$

times a constant of modulus one. All other conditions are finite
coprimality and divisibility restrictions on $z$.

For distinct $(\eta,r)\ne(\eta',r')$, (9.14) is nonprincipal. At a good
prime, the difference of the valuations one or two determines the
local cubic orientation; equality of all of them forces $r=r'$.
The remaining unit/ramified Kummer classes in $\mathcal T$ are distinct.
The primitive conductor of (9.14) has norm $O(q_rq_{r'})\ll R^2$.
If the labels agree but $d\ne d'$, their row sectors are disjoint.
For equal $(\eta,r,d)$, (9.14) is principal and the only main term is
the squarefree density with the two centered factors.

#### 9.3.2. Smooth squarefree character counting with restrictions

For a finite-order Hecke character $\psi$ of conductor norm $Q_\psi$,
a common deletion radical $B$, and a fixed smooth annular profile, the
squarefree series is
$L(s,\psi)/L(2s,\psi^2)$ times finite local factors.
On $\Re s=1/2+\epsilon$, the denominator is bounded by absolute Euler
convergence and finite factors cost $q_B^\epsilon$. Fixed-field convexity
and smooth Mellin decay therefore give

$$
 \sum_{(z,B)=1}\mu(z)^2\psi(z)W(q_z/X)
  =1_{\psi=1}\,c_{\psi,B,W}X
       +O_\epsilon(X^{1/2+\epsilon}Q_\psi^{1/4+\epsilon}q_B^\epsilon).
 \tag{9.15}
$$

For a principal induced character, all conductor primes are included in
$B$ and the displayed main constant is its exact local density. This is
ordinary squarefree character counting, not a reciprocal-$L$ estimate
inside the critical strip. The line $2\Re s>1$ is essential.

Expand the two centered factors by (9.2). Their total absolute coefficient
mass is at most $(q_hq_{h'})^{1/2+\epsilon}\le H^{1+\epsilon}$.
A condition $e\mid x=u'z$ becomes $e/(e,u')\mid z$, and similarly for
$e'\mid x'$. If this conflicts with squarefreeness or a deletion it gives
zero; otherwise set $z=f_0z_0$ with $f_0$ the union of these forced primes.
The remaining length is $Y/(ff_0)$, the deletion is polynomial in $RH$,
and the character conductor remains at most $O(R^2)$.
The hypothesis on $R,H$ keeps this length above one. Formula (9.15) applies
with no varying profile: the extracted powers are written outside the
fixed annular profile.

In global row norm, the factor $q_c^{-1/3}$ and the two normalizations
contribute
$Y^{-1}(q_tq_{t'})^{1/2}(k_rk_{r'})^{-1/2}I^{-1}$ times a bounded
smooth profile. Thus, dropping the helpful $(ff_0)^{-1/2}$ factor,
the total entry discrepancy is

$$
 O_\epsilon\bigl(Y^{-1/2+\epsilon}R^{1+\epsilon}H^{1+\epsilon}\bigr).
 \tag{9.16}
$$

Here $(q_tq_{t'})^{1/2}\le R^{1/2}$ and the conductor cost is
$Q_\psi^{1/4}\ll R^{1/2}$. The inverse density factors cost only
$R^\epsilon$. For equal labels and sector, the principal main term is
exactly the expectation of $H_hH_{h'}$ under independent squarefree
local probabilities $1/(q_p+1)$ outside $r$. It is $1_{h=h'}$ by (9.1).
All other main terms vanish as described above. Multiplying (9.16) by
(9.11) proves (9.12), even with exponent two in place of four after adjusting
epsilon. The safe exponent four will be used below.

### 9.4. Uniform adjoint remainder with all numerator sectors

We claim, uniformly for $i\in\mathcal I(R,H)$,

$$
 C^*z_i=T_i+e_i,\qquad
 \sum_{q_n\asymp Y}^{\rm sf}|e_i(n)|^2
        \ll_\epsilon Y^{1+\epsilon}(RH)^{10+\epsilon}.
 \tag{9.17}
$$

The exponent ten is intentionally generous. It permits a direct use of
the published moving Kubota mean without a delicate optimization.

Fix one indicator $e\mid h$ in (9.2), substitute $x=ez$, and write
$T=L/q_e$. The outside factor, apart from phases, is $q_e^{-1/6}/D$.
Its exterior character allows us to assume $(n,te)=1$.
For all other column overlaps put

$$
 g_a=(n,a),\quad g_d=(n,d),\quad n=g_ag_dm,\quad
 a=g_aa_1,\quad d=g_dd_1.
 \tag{9.18}
$$

The exact numerator factors as

$$
 ad^2en=(a_1em)(g_ad_1)^2g_d^3.
 \tag{9.19}
$$

These three factors are pairwise coprime on squarefree support.
In [4, Lemma 6.7] the squarefree numerator, squared numerator and cube
puncture are respectively
$\alpha=a_1em$, $\beta=g_ad_1$, $c=tg_d$.
The $e$ zero is already part of $\alpha$; $t,g_d$ give exactly the
remaining original puncture. Thus the required squarefree product
condition holds, and no overlap sector is dropped.
The pole exists exactly when $g_a=d_1=1$, as used in Section 9.2.

The source remainder has factor $T^{1/3+\epsilon}$ and the divisor sums
$d_0\mid a_1em$, $f\mid tg_d$, with weights
$(q_{d_0}q_f)^{-1/2-\epsilon}$ and a rapidly decaying height integral.
Write $d_0=d_{\rm fix}d_m$, $d_{\rm fix}\mid a_1e$, $d_m\mid m$,
and $m=d_mm_0$. The new Kubota numerator is $vm_0$ with

$$
 v=\eta(a_1e/d_{\rm fix})(g_ad_1)^2f,
 \qquad q_v\ll (RH)^5.
 \tag{9.20}
$$

Cauchy over the divisor sum costs only divisor subpowers. The published
mean [4, Lemma 6.6] gives a squared multiplier cost $q_v^{1/2}$ and
length $Y/(q_{g_a}q_{g_d}q_{d_m})$. The squared divisor coefficient
contributes another $q_{d_m}^{-1}$. Thus the entire moving divisor sum
is bounded by $\sum_{d_m}q_{d_m}^{-2}$, not a counted factor of $Y$.
For each $d_m$, extend the nonnegative $m_0$ sum to all
$q_{m_0}\ll Y/(q_{g_a}q_{g_d}q_{d_m})$, dropping its squarefree
and coprimality masks only at this positive step. This is exactly the
support of the published mean. The $g_a,g_d,d_{\rm fix},f$ sums
are divisor-bounded in $RH$.
Consequently

$$
 \sum_{n\asymp Y}|S_{n,e}-S_{n,e}^{\rm pole}|^2
       \ll_\epsilon T^{2/3+\epsilon}Y^{1+\epsilon}(RH)^{5/2+\epsilon}.
 \tag{9.21}
$$

The source's height growth is quadratic; choose a fixed sufficiently
large decay order. Multiplying by $q_e^{-1/3}/D^2$ leaves the helpful
factor $q_e^{-1}$, up to inverse densities of size $R^\epsilon$.
Minkowski over (9.2) costs at most $H^{1+\epsilon}$ in squared norm.
Thus the full raw adjoint error is bounded by
$Y^{1+\epsilon}(RH)^{4+\epsilon}$, already smaller than (9.17).

For $P^*z_i$, (9.13) leaves the nonprincipal character $\chi_x(\eta r)$
on the free row. After $x=ez$, any conflicts with the physical deletion
make that term zero. Otherwise (9.15), now with conductor $O(R)$ and
additional deletion containing $n$, gives the weighted sum
$O(T^{1/6+\epsilon}R^{1/4+\epsilon}(YRH)^\epsilon)$.
The exterior row/column powers, inverse density, and the squared
coefficient mass from (9.2) are at most a fixed polynomial in $RH$.
More explicitly, after expressing the base vector in global $c$ using
(9.13), the outside factor is
$O(Y^{-1/3}q_t^{1/2}R^\epsilon q_n^{-1/6})$ and the weighted row sum
for a forced prefix $te$ is
$O(Y^{1/6+\epsilon}(q_tq_e)^{-1/2}R^{1/4+\epsilon}q_n^\epsilon)$.
Summing over the $O(Y)$ columns and using (9.2) gives

$$
 \|P^*z_i\|_2^2\ll_\epsilon Y^{1/3+\epsilon}R^{1/2+\epsilon}H^{1+\epsilon}.
 \tag{9.22}
$$

This is absorbed in (9.17). The nonprincipal condition is necessary:
the ordinary principal polar coordinate is removed by $P$.
Equations (9.21)–(9.22) prove the deliberately looser uniform bound (9.17).


### 9.5. Sum the physical observations and compare with the majorant

Let $\mathcal P^{v,\rm np}(Y;R,H)$ be(1.12) with
$q_r\le R$, $q_h\le H$, and the ordinary principal class omitted.
Equation (9.10) gives its exact representation as
$Y^{-1}\sum_{i\in\mathcal I(R,H)}|A_i|^2$.
Write $B_i=\langle C\beta,z_i\rangle_\Phi$ and
$E_i=\langle\beta,e_i\rangle$, so $B_i=A_i+E_i$ by (9.17).
Since $\|\beta\|_2^2\ll_VY$, (9.11) and (9.17) imply

$$
 Y^{-1}\sum_i|E_i|^2
       \ll_\epsilon Y^{1+\epsilon}(RH)^{11+\epsilon}.
 \tag{9.23}
$$

Let $g_Y$ be the upper bound in (9.12). The finite Gram matrix and Bessel's
inequality give

$$
 \sum_i|B_i|^2\le(1+g_Y)\|C\beta\|_\Phi^2.
 \tag{9.24}
$$

Only an upper Gram bound is needed. This is a statement about this finite
family, not completeness of physical row space.
For any $0<\zeta<1$, use
$|A_i|^2\le(1+\zeta)|B_i|^2+(1+\zeta^{-1})|E_i|^2$.
Equations (9.23)–(9.24) yield

$$
 \mathcal P^{v,\rm np}(Y;R,H)
 \le(1+\zeta)(1+g_Y)\mathcal E_{\rm sf}
      +O_\epsilon(\zeta^{-1}Y^{1+\epsilon}(RH)^{11+\epsilon}).
 \tag{9.25}
$$

The upper reduction(1.13) and the ordinary character-sieve sum in
Section 6 give unconditionally
$\mathcal E_{\rm sf}\le\mathcal E_y\ll_\epsilon Y^{4/3+\epsilon}$.
This uses no inverse cancellation hypothesis. Also, by the trivial
$|M^v(Z;Q)|^2\ll_V Z$ on nonempty daughters,

$$
 0\le\mathcal P^{v,\rm np}(Y;R)
        -\mathcal P^{v,\rm np}(Y;R,H)
     \ll_\epsilon Y^{4/3+\epsilon}R^{2/3+\epsilon}H^{-2}.
 \tag{9.26}
$$

Indeed the $d$ divisor sum is harmless and the $h$ tail is
$\sum_{q_h>H}q_h^{-3}\ll H^{-2}$.

Choose $R=H=Y^\alpha$ with $\alpha>0$ reduced inside every allowance
of Sections 2 and 5, and additionally $\alpha<1/1000$. Set $\zeta=Y^{-\alpha}$.
Then (9.12), (9.25), (9.26) and the unconditional upper bound give

$$
 \begin{aligned}
 \mathcal P^{v,\rm np}(Y;R)
 \le\mathcal E_{\rm sf}+O_\epsilon(&Y^{4/3-\alpha+\epsilon}
       +Y^{5/6+8\alpha+\epsilon}\\
       &+Y^{1+23\alpha+\epsilon}
       +Y^{4/3-4\alpha/3+\epsilon}).
 \end{aligned}
 \tag{9.27}
$$

All four powers are strictly below $4/3$. Take subsidiary epsilons
smaller than the resulting margins. The finite-sieve upper model(1.13), with its admissibly small $\nu\ll\delta\ll\alpha$, is
$\mathcal E_{\rm sf}\le\mathcal E_y
 =\mathcal P^{v,\rm np}(Y;R)+O(Y^{4/3-\eta_c})$ for a fixed
$\eta_c>0$. Combining it with (9.27) proves Theorem 4.

We have proved the asserted physical norm formula: For sufficiently
small admissible fixed $\alpha,\nu>0$, there is a fixed $\eta>0$ such that
for every fixed smooth complex column profile and fixed nonzero smooth
nonnegative row profile,

$$
 \boxed{\mathcal E_{\rm sf}(Y;V)
       =\mathcal P^{v,\rm np}(Y;Y^\alpha)+O_{V,\Phi}(Y^{4/3-\eta})},
 \qquad
 0\le\mathcal E_{Y^\nu}-\mathcal E_{\rm sf}
                        \ll_{V,\Phi}Y^{4/3-\eta}.
 \tag{9.28}
$$

The exponents can be chosen independently of the fixed seminorm values.
All formulas use the literal coefficients and all four ramified types.
The argument of this section alone does not estimate the retained
nonprincipal inverse sums with a fixed saving below $Y^{4/3}$. Section 11
imports an external zero-free theorem and supplies an explicit bound.
The common zero-free criterion is an equivalence, not a new zero-free
conclusion independent of its inputs.

The new physical lower comparison comes from the specifically constructed
observations (9.1), their exact residues (9.9) and the uniform Gram and
remainder estimates. It does not follow from Loewner dominance of the
arithmetic kernel, and it does not assert a complete orthogonal basis.
The lower comparison is supplied by (9.25), separately from the finite-sieve upper model.
The error exponent remains too small for a complete $7/6$ bound.


### 9.6. Approximation of the actual output vector

The uniform estimates also give a direct reconstruction. Keep the
linear-in-the-first-slot inner product, set $A_i=\langle\beta,T_i\rangle$,
and define the physical vector

$$
 \mathcal R_{R,H}\beta=\sum_{i\in\mathcal I(R,H)}A_i z_i.
 \tag{9.29}
$$

The coefficient is $A_i$, with its actual phase from (9.5) and (9.9).
Write $P_{R,H}=Y^{-1}\sum_i|A_i|^2$ and
$P_R=\mathcal P^{v,\rm np}(Y;R)$. Since
$\langle C\beta,z_i\rangle_\Phi=A_i+E_i$, expansion gives the exact identity

$$
 \begin{aligned}
 Y^{-1}\|C\beta-\mathcal R_{R,H}\beta\|_\Phi^2
 ={}&\mathcal E_{\rm sf}-P_{R,H}
       -2Y^{-1}\Re\sum_i\overline{A_i}E_i\\
 &+Y^{-1}\sum_{i,j}A_i\overline{A_j}
       (\langle z_i,z_j\rangle_\Phi-\delta_{ij}).
 \end{aligned}
 \tag{9.30}
$$

Use the upper comparison $\mathcal E_{\rm sf}\le P_R+
O(Y^{4/3-\eta_c})$ from Sections 5--7, the tail (9.26),
the unconditional $P_{R,H}\ll_\epsilon Y^{4/3+\epsilon}$, and (9.23).
Cauchy bounds the cross error by
$O_\epsilon(Y^{7/6+\epsilon}(RH)^{11/2+\epsilon})$.
The last line costs at most the Gram error (9.12) times $P_{R,H}$.
Consequently

$$
 \begin{aligned}
 Y^{-1}\|C\beta-\mathcal R_{R,H}\beta\|_\Phi^2
 \ll_\epsilon{}&Y^{4/3-\eta_c}
    +Y^{4/3+\epsilon}R^{2/3+\epsilon}H^{-2}\\
 &+Y^{5/6+\epsilon}(RH)^{4+\epsilon}
    +Y^{7/6+\epsilon}(RH)^{11/2+\epsilon}.
 \end{aligned}
 \tag{9.31}
$$

For $R=H=Y^\alpha$ with the same sufficiently small admissible
$\alpha<1/1000$, this is $O(Y^{4/3-\eta_{\rm rec}})$ for any fixed
positive $\eta_{\rm rec}$ strictly below

$$
 \min\{\eta_c,\ 4\alpha/3,\ 1/2-8\alpha,\ 1/6-11\alpha\},
 \tag{9.32}
$$

after choosing the subsidiary epsilons. The exact orthogonal projection
onto the span of these $z_i$ has no larger squared error, by its minimizing
property. This is an approximation for the actual Möbius input: the
upper comparison used above is not an arbitrary-coefficient operator bound.
It uses the independently controlled complex adjoint cross term and needs
no completeness assertion. The coefficients $A_i$ still require arithmetic
cancellation. A subsequent linear map with squared operator norm at most
$Y^\kappa$, in specified norms, increases the squared error exponent by
$\kappa$; a useful further comparison must pay this cost.

## 10. The common zero-free criterion

We prove Corollary 5 with all profile and conductor quantifiers retained.
The exponents in Sections 2 and 5 depend on fixed support annuli and
analytic input constants, before the finite seminorm values of $V$ are
specified. Fourier separation costs further fixed seminorms; their orders
are chosen after the arithmetic parameters. Thus replacing $V(x)$ by
$x^{it_0}V(x)$ for any fixed $t_0$ changes constants and thresholds,
not the saving exponent. No uniform-in-$t_0$ claim is required.

### 10.1. Necessity by Mellin zero detection

Assume the common norm saving in Corollary 5. For each fixed nonprincipal
$(\eta,r)$, Theorem 3 gives, for every smooth $U\in C_c^\infty(I)$,

$$
 S_\psi(Y;U):=\sum_{(n,r)=1}\mu(n)v(n)\psi_{\eta,r}(n)U(q_n/Y)
       \ll_{\eta,r,U}Y^{1-\gamma},
 \qquad0<2\gamma<\min(\Delta,1/3).
 \tag{10.1}
$$

Take $V(x)=x^{1/6}U(x)$. More explicitly, Theorem 3 gives
$S_\psi\ll Y^{1-\Delta/2}+Y^{5/6+\epsilon}$; reducing epsilon
gives (10.1) and explains its $1/3$ margin.
The exponent $\gamma$ is common; constants need not be uniform in the
fixed character.

For $\Re s>1$, the coefficient series is

$$
 D^v_\psi(s)=L_{\rm good}(s,\psi)^{-1}H^v_\psi(s),\qquad
 H^v_\psi(s)=\prod_p
 \frac{1-v(p)\psi(p)q_p^{-s}}{1-\psi(p)q_p^{-s}}.
 \tag{10.2}
$$

This product is absolutely convergent, holomorphic and nonvanishing for
$\Re s>0$: on $\Re s\ge b>0$ its relative factors differ from one by
$O_b(q_p^{-1-b})$. A numerator zero has negative real part and a
denominator zero real part zero. Finite imprimitive, ramified and deletion
factors are also nonzero on $\Re s>0$. Thus a primitive $L$-zero there
gives a pole of $D^v_\psi$ with the same multiplicity.

For $\Re s>1$, Mellin transformation gives

$$
 \int_0^\infty S_\psi(Y;U)Y^{-s}\frac{dY}{Y}
        =\widehat U(s)D^v_\psi(s).
 \tag{10.3}
$$

The integrand vanishes for sufficiently small $Y$. By (10.1) the left
side is holomorphic in $\Re s>1-\gamma$. If
$\beta+it_0$ were an $L$-zero in that half-plane, choose a nonzero
nonnegative $W\in C_c^\infty(I)$ and $U(x)=W(x)x^{-it_0}$. Then

$$
 \widehat U(\beta+it_0)=\int_0^\infty W(x)x^\beta\frac{dx}{x}>0.
 \tag{10.4}
$$

The pole on the right of (10.3) contradicts holomorphy. This proves a
common zero-free half-plane for $\mathscr C_{\rm np}$.

The finite-majorant necessity also follows from
$\mathcal E_{\rm sf}\le\mathcal E_y$. Alternatively, keep the $d=h=1$
positive summand in Theorem 2 and use its power error. For the natural-row
norm, Theorem 1 gives the analogous positive lower test for every fixed
label, including the principal one, with Euler weight $w$; replacing
$v$ by $w$ in (10.2)–(10.4) proves that necessity. The principal pole at
one gives a zero, not a pole, of its reciprocal series.

### 10.2. Sufficiency and uniform reciprocal bounds

Assume a common zero-free half-plane and fix
$\max(\sigma_0,1/2)<\sigma<1$. Uniformly in the relevant family,

$$
 |L(\sigma+it,\psi)^{-1}|
   \ll_{\sigma,\sigma_0,\epsilon}[Q_\psi(3+|t|)^2]^\epsilon.
 \tag{10.5}
$$

For completeness, regularize a possible principal pole by
$H(s)=((s-1)/(s+1))^{\delta_\psi}L(s,\psi)$, analytic and nonzero on
the assumed half-plane. Choose fixed radii
$1/2<2-\sigma<R_0<R_1<2-\max(\sigma_0,1/2)$ about $2+it$.
Uniform polynomial growth and Borel–Carathéodory bound the analytic
logarithm on radius $R_0$ by $O(\log(2+Q_\psi(3+|t|)^2))$, with its
branch anchored by the Euler logarithm at the center. On radius $1/2$
it is uniformly bounded by absolute Euler convergence and the principal
regularization. Three circles gives $O((\log(2+Q_\psi(3+|t|)^2))^\vartheta)$,
$\vartheta<1$, on radius $2-\sigma$. Exponentiating gives (10.5) on a
fixed strip; the regularization factor has modulus at most one for
$\Re s>0$.

For either Euler weight $u=w,v$, the transfer product corresponding to
(10.2) is uniformly bounded on that strip. Finite deleted factors obey

$$
 \prod_{p\mid Q}|1-u(p)\psi(p)q_p^{-s}|^{-1}
         \ll_{b,\epsilon}q_Q^\epsilon,\qquad\Re s\ge b>0.
 \tag{10.6}
$$

Their logarithms are $O_b(q_p^{-b})$; separate finitely many small
primes and use $q_p^{-b}=o(\log q_p)$. Mellin shifting therefore gives

$$
 |M^u_{\eta r}(Z;Q)|^2
       \ll_{\sigma,\epsilon,V}Z^{2\sigma-1}(Q_\psi q_Q)^\epsilon.
 \tag{10.7}
$$

Nonempty subunit scales stay in a fixed compact interval and satisfy
the same bound by the finite sum. Smooth Mellin decay pays horizontal
integrals and uses only fixed finite seminorms.

Put $\kappa=2\sigma-1>0$. In (1.12), every conductor and deletion is
polynomial in $Y$: $q_r\le Y^\alpha$ and nonempty daughters have
$q_h\ll Y/q_d$. The $d,h$ sums after (10.7) satisfy

$$
 \sum_{d\mid b}q_d^{-\kappa}\ll_\epsilon q_b^\epsilon,
 \qquad\sum_h\frac{v(h)^2}{q_h^{2+\kappa}}\ll_\sigma1.
 \tag{10.8}
$$

Thus, with the ordinary principal class already removed,

$$
 \mathcal P^{v,\rm np}(Y;Y^\alpha)
           \ll Y^{2\sigma-2/3+2\alpha/3+\epsilon}.
 \tag{10.9}
$$

Choose any sufficiently small admissible $\alpha<3(1-\sigma)$, then
$\delta,\nu$ as in Section 5. Theorem 2 proves a fixed power saving
for the finite majorant and hence the exact squarefree norm. No
principal zero-free hypothesis has entered this direction.

For the natural-row norm the argument repeats with (1.7), using
$\sum_{d\mid b}(\phi(d)/q_d)q_d^{-\kappa}\ll q_b^\epsilon$ and
$\sum_h\phi(h)q_h^{-3-\kappa}<\infty$. Its model contains the principal
term, so that family must include the principal character. Theorem 1
then gives its fixed power saving. This proves all stated criteria.


## 11. Explicit full-norm estimates and the unequal-scale diagonal

This section adds a quantitative consequence to the model and exact
transform. It imports the global zero-free statement of [10, Theorem 1.1],
whose full proof is not reverified here. All conclusions of this section
are relative to that named external input as well as the density and
moment inputs specified below. This dependence is essential: the norm
estimate is not an independent proof of the imported zero-free theorem.
Sections 1–10 do not require that import.

### 11.1. The full norm and its exact diagonal

Keep the profiles and conventions of Section 1.1, and write

$$
\begin{aligned}
F_Y(x;E)&=Y^{-1/2}\sum_{(n,E)=1}
 \mu(n)G(n)\overline{\chi_n(x)}V(q_n/Y),\\
\mathcal N(A,Y;E)&=\sum_x\Phi(q_x/A)|F_Y(x;E)|^2,\\
\mathcal D(A,Y;E)&=\frac{\rho A\widehat\Phi(1)}Y
 \sum_{(n,E)=1}|\mu(n)V(q_n/Y)|^2w(n),\\
\mathcal R(A,Y;E)&=\mathcal N(A,Y;E)-\mathcal D(A,Y;E).
\end{aligned}
\tag{11.1}
$$

The row set is the original natural primary row set in (1.6) and (2.4).
The finite expression $\mathcal D$ is the exact zero frequency of (2.4),
not a limiting constant substituted for it. The restrictions and literal
zeros in the norm remain unchanged.

**Theorem 6 (explicit full norm and additive diagonal asymptotic).**
Fix $B,C>0$ and let $Y\ge2$, $Y\le A\le Y^C$, and $NE\le(AY)^B$.
Import the zero-free statement

$$
L^*(s,\psi)\ne0\quad\text{for }\Re s>7/8
\tag{ZF}
$$

for the relevant finite-order Eisenstein Hecke family, including the
principal inducing functions, from [10, Theorem 1.1]. Then:

1. For every fixed $c>0$ and $Y\le A\le Y^{2-c}$,

$$
|\mathcal R(A,Y;E)|\ll_{c,\epsilon}(AYNE)^\epsilon
 \left[Y+A^{8/21}Y^{19/21}+A^{5/9}Y^{23/36}\right].
\tag{11.2}
$$

2. For every fixed $M\ge0$ and all the indicated $A$,

$$
|\mathcal R(A,Y;E)|\ll_{M,\epsilon}(AYNE)^\epsilon
 Y^{7/4}\min\{1,(Y^2/A)^M\}.
\tag{11.3}
$$

3. Consequently,

$$
\mathcal N(A,Y;E)\ll_\epsilon(AYNE)^\epsilon
 \left[A+A^{8/21}Y^{19/21}\right].
\tag{11.4}
$$

For every fixed $\delta>0$ there is $\eta>0$ such that

$$
\mathcal N(A,Y;E)=\mathcal D(A,Y;E)+O(A Y^{-\eta}),
\qquad Y^{19/13+\delta}\le A\le Y^C.
\tag{11.5}
$$

For example, allocate the subsidiary powers after fixing $B,C,\delta$;
one may take half the margin

$$
\eta_0=\min\left\{\frac{13\delta}{21},
 \frac5{468}+\frac{4\delta}{9},\frac18\right\}>0.
\tag{11.6}
$$

The implicit constants depend on the fixed profiles and their needed
seminorms. Formula (11.5) is additive. No uniform positive lower bound
for $\mathcal D/A$ is asserted when $E$ varies. No unequal-scale theorem
for the polar-corrected squarefree norm is asserted.

At $A=Y$, (11.4) gives

$$
\mathcal N(Y,Y;E)\ll_{B,\epsilon}Y^{9/7+\epsilon}.
\tag{11.7}
$$

For $E=1$, the same exponent bounds the actual corrected output:

$$
Y^{-1}\|C\beta\|_\Phi^2\ll_\epsilon Y^{9/7+\epsilon},
\qquad \beta_n=\mu(n)V(q_n/Y).
\tag{11.8}
$$

These are full estimates, with every original divisor sector included.
The exponent $9/7$ is $1/21$ below $4/3$, but it is $5/42$ above $7/6$.
We make no numerical comparison with earlier unspecified positive savings.
The sufficient threshold $19/13$ is not asserted optimal.

### 11.2. The finite cubic packet and the natural density input

We first identify exactly which extension of the density theorem is used.
The strongest natural inverse-product theorem in [6] is printed for a
principal fixed finite twist. We do not replace that hypothesis by an
arbitrary finite-order twist. The bounded cubic-numerator extension needed
here is already proved in [9, Section 10.2, the paragraph following (10.19)].
It covers the actual fixed unit and ramified cubic numerators generated by
reducing row valuations modulo three.

For completeness, the coefficient and normalization mechanism in that
extension is the following. A product of inverse factors has the same
common multiplicative coefficient after multiplication by $\chi_n(v)$,
where $v$ is a fixed cubic numerator. In its squarefree reverse norm the
numerator becomes $vd(g/\ell)^2$. The raw source estimate of [6, Section
3.8] permits this bounded numerator with its pole support and costs at
most

$$
P^{2/3}L^{4/9}(Nv)^{1/3}.
\tag{11.9}
$$

For fixed $v$ and $P\ge L$, this is absorbed by $P+P^{1/3}L$:
the first term suffices for $L\le P^{3/4}$, and the second for
$P^{3/4}\le L\le P$. For $P<L$, the generic cubic sieve permits the
fixed cubic factor in the common coefficient. The powerful-part and
cube-tower restorations in [9] retain all valuations and deletions.
The separate smooth profiles are restored by one common Mellin integral.
Thus, for a fixed number of inverse factors, total column length $L$,
one common deletion $E'$, and the specified bounded packet,

$$
\sum_{0<q_h\le P}\prod_i|M_{vh,i}|^2
\ll_\epsilon(PLNE')^\epsilon T^J(P+P^{1/3}L),
\tag{11.10}
$$

with the same height convention as [9]. This is a recovered input, not a
new moment theorem of the present section.

The ordinary fourth moment used in [6, (F1)] permits these fixed finite
twists on the rows whose full inducing character is nonprincipal; see
also [12]. Hence the proof of [6, Section 5.7] applies to each such $v$:

$$
\sum_{0<q_h\le P}N(\sigma,P^{h_0};\chi_{vh})
\ll P^{D(\sigma)+\epsilon},\qquad
D(\sigma)=\frac{8-7\sigma}{3(2-\sigma)}.
\tag{11.11}
$$

Here $1/2<\sigma<1$, and $h_0>0$ may depend on the fixed packet,
$\sigma$ and the allocated loss. To check this application rather than
infer it from the printed principal-twist statement, multiply the exact
third-order inverse identity by the same completely multiplicative,
zero-extended cubic character. In the notation $d=2\sigma-1$,
$C_0=1/(3-d)$ of that proof, the inverse branch uses only the fixed
integer powers $q=2,\ldots,32$ and the range
$4C_0/3\le qc\le2C_0$ in (11.10). The ordinary branch has the same
fourth moment and margin

$$
d\left[\frac{37}{24}C_0-\frac12\right]\ge d/72.
$$

The primitive inducing conductor remains $O_v(P)$. Thus the contour,
detector and fixed-buffer choices in [6] are unchanged. Principal inducing
presentations have count $O_v(P^{1/3})$ and their fixed-function zero count
is absorbed after shrinking the height, since $D(\sigma)>1/3$.
Only finitely many density parameters will be used, before a single common
height is selected. No arbitrary noncubic twist or growing numerator is
included in this argument.

For the upper strip the cube-free density input in [6] permits the fixed
finite twists already. Its convenient envelope is

$$
G(\sigma)=\frac{16(1-\sigma)}{4\sigma+1},\qquad \sigma\ge5/6.
$$

Lifting by the actual presentations $h=rt^3$ gives

$$
\sum_{0<q_h\le P}N(\sigma,P^{h_0};\chi_{vh})
\ll P^{\max\{G(\sigma),1/3\}+\epsilon}.
\tag{11.12}
$$

Indeed split cube-free cores at $P^\beta$. On a dyad $S>P^\beta$, their
contribution is at most $P^{1/3}S^{G(\sigma)-1/3+\epsilon}$, after the
height is chosen below $\beta$ times the needed density height. The small
cores, including the possible principal one, cost at most
$P^{1/3+2\beta/3+h_0+\epsilon}$. Choose $\beta,h_0$ in the final loss.
The stronger printed upper envelope could be retained, but is not needed.
The row character in (11.11)–(11.12) is the full inducing character.
Extra Euler deletions are not a new density family.

### 11.3. A natural inverse mean with long daughters

Let $Y^c\le P\le Y$ for fixed $c>0$, and let $0<Z\le c_0Y$ be any
nonempty daughter scale. For each fixed packet numerator $v$, polynomial
common deletion $E'$, and bounded smooth annular profile family, we claim

$$
\sum_{0<q_h\le P}\sup_{|t|\le Y^{h_1}}
\left|Z^{-1/2}\sum_{(n,E')=1}\mu(n)\chi_n(vh)
                   (q_n/Z)^{it}W(q_n/Z)\right|^2
\ll_\epsilon(PYNE')^\epsilon
\left[P+Y^{2/3}P^{13/21}+Y^{3/4}P^{4/9}\right].
\tag{11.13}
$$

The length hypothesis is $Z\le c_0Y$, not $Z\le P$. Thus it includes the
long daughters needed below. Nonempty subunit scales lie in a fixed compact
interval and cost $O(P)$ directly.

For $Z\ge1$, first fix a floor $1/2+u$ and a finite buffered mesh through
$7/8$, with width and buffers small in the requested loss. Take the finite
minimum of the height allowances in (11.11)–(11.12), over this mesh and all
packet types. Since $P\ge Y^c$, a common positive $Y$-height fits every
$P$-height. Also $NE'\le P^{B'}$ and $\log_P Z$ is in a fixed bounded
interval, with constants depending on $c$ and the prescribed power ranges.
The buffered reciprocal contour of [6, Section 4.1] is therefore uniform
for these daughters. Its fixed decay orders can be increased for the
chosen compact length interval. The proof of (10.5) also shows explicitly
how the polynomial deletion costs a subsidiary power.

In a bin whose right endpoint is $\sigma$, the normalized square is
$O(Y^{2\sigma-1+o(1)})$; the finite mesh and buffer losses are included
in the allocated power. The imported (ZF) removes higher bins. Zeros on
$\Re s=7/8$ are covered by moving the contour a fixed small amount to
their right, not by asserting a zero-free closed boundary. Put
$p=\log_Y P$. In the lower strip the resulting exponent is

$$
2\sigma-1+pD(\sigma),\qquad 1/2\le\sigma\le5/6.
$$

Its derivative is $2-2p/(2-\sigma)^2>0$ for $0<p\le1$, so its maximum
is $2/3+13p/21$. In the upper strip $G\ge4/9>1/3$ and

$$
\frac{d^2}{d\sigma^2}\{2\sigma-1+pG(\sigma)\}
=\frac{640p}{(4\sigma+1)^3}>0.
$$

The two endpoint exponents are $2/3+8p/13$ and $3/4+4p/9$; the first
is below the lower-strip maximum. The floor contributes $P$ times a
subsidiary power. Principal presentations may instead be bounded directly
by $O(P^{1/3})$ times $O(Y^{3/4+\epsilon})$, which is absorbed in the
last term of (11.13). The principal pole is a zero of the reciprocal;
the regularized logarithm used in (10.5) treats it without an extra pole
term. This proves (11.13), with finite choices made before taking the
common height. The same proof covers all the fixed derivative profiles
needed in a common Sobolev majorant.

The bound also holds for $P'=LP$ when $1\le L\le Y^v$, where any small
fixed $0<v<1/10$ is sufficient. Indeed $p'=\log_Y P'\le1+v<49/36$,
so the lower derivative is still positive, while the upper envelope
remains convex. The floor $P'$ is retained. All length, conductor and
height comparisons are still in fixed power ranges. This explicitly
handles the row dilations that cross $P'=Y$.

### 11.4. Recombine every divisor before applying the mean

The exact identity (2.4) is valid beyond the narrower asymptotic range
of Theorem 1. Its zero frequency is precisely $\mathcal D$ in (11.1).
For all nonzero frequencies expand the complete cross-divisor projector
and Ramanujan sum, without making a low/high split. Formula (2.5) gives

$$
2\rho\frac AY\mu(s)\mu(g/\ell)\frac{q_\ell}{q_gq_s},
\quad Z=\frac{Y}{q_gq_s},\quad
K=\frac{Y^2}{Aq_gq_\ell},\quad j=g\ell k',\quad\ell\mid g.
\tag{11.14}
$$

The outside scalar is single, not squared. No extra daughter length is
introduced. The two columns have their actual Möbius coefficients,
possibly different separated profiles, and original zeros, including
$\chi_s(j)$, until the positive Cauchy estimate.

Put $P=Y^2/A$. On the original radial window the reindexed row $j$ has
norm comparable to $P$, independently of $g,s,\ell$. Fix the $g$ and
$s$ norm dyads. Before reindexing, majorize the compact $q_g/G$ profile
parameter by a common positive Sobolev integral. Its scaled derivatives
act on the smooth profiles alone; the representative daughter length is
$Y/(Gq_s)\le c_0Y$. Do the logarithmic Fourier separation of the original
radial kernel in this same order. Each derivative column is a common
function $J(j)$ with a permitted profile, not a test selected separately
at each $j$.

The $g$-deletion is redundant in the literal character at $j$, and $sE$
is a common remaining deletion for each fixed $s$. The precise fibre
inequality in [9, (10.18b)], also recorded after (2.9), now applies to
every $g$ dyad:

$$
\sum_g\sum_{\ell\mid g}\frac{q_\ell}{q_g}
       \sum_{k'\ne0}|J(g\ell k')|^2
\le\sum_{j\ne0}\tau(j)^2|J(j)|^2.
\tag{11.15}
$$

Both $g$ and $\ell$ divide $j$, and $q_\ell/q_g\le1$. There is no
independent count of $g$. The original row support and additional masks
only reduce this positive sum. Cauchy treats both complete daughter
columns in the same common measures. The remaining $s$ weight is $1/q_s$,
up to a fixed divisor power, and therefore costs only a subsidiary power.
The dyad counts are logarithmic.

Separate the units and fixed bad-prime valuations of $j$ before applying
(11.13). Reducing valuations modulo three leaves a finite set of bounded
cubic numerators covered by Section 11.2. The cube factors impose their
original extra deletions and reduce the row ball; they can either be
summed with their original weights or bounded on the enclosing ball with
only logarithmically many valuation choices in the polynomial range.
No growing numerator is hidden in a fixed-twist hypothesis.

When $Y\le A\le Y^{2-c}$, apply (11.13) in (11.15). Restoring $A/Y$
from (11.14) sends its three terms to

$$
Y,\qquad A^{8/21}Y^{19/21},\qquad A^{5/9}Y^{23/36}.
\tag{11.16}
$$

This estimates the complete nonzero-frequency contribution. No original
divisor tail or moving-character uniformity remains unpaid at this stage.

For completeness, the Fourier row profile has rapid tails. On the
dilated row ball $P'=LP$ with $L\le Y^v$, use the extension following
(11.13). Its three terms grow by at most $L,L^{13/21},L^{4/9}$.
The common scaled derivatives of the radial transform have arbitrary
decay in $L$, so these dilations are summable. For $L>Y^v$, use the generic
natural-row bound (2.3), with daughter length at most $c_0Y$:

$$
\sum_{q_j\le LP}|M_j(Z)|^2
\ll(LPYNE')^\epsilon
 \left[LP+(LPY)^{2/3}+(LP)^{1/3}Y\right].
\tag{11.17}
$$

Choose the radial decay order after the fixed exponents, so this tail is
$O(Y^{-K_0})$ for any prescribed $K_0$. For common Mellin heights outside
$Y^{h_1}$ use the same generic sieve and a later, arbitrarily large
Fourier decay order. The profiles have fixed polynomial height costs.
Selecting the decay orders after $h_1$ pays these costs even if the
available height is very small. Integrating the common positive measures
and summing the harmonic $s$ weight proves (11.2).

### 11.5. Pointwise control and the empty subunit dual ball

Independently of the density decomposition, (ZF) and the buffered
reciprocal estimate (10.5) on $7/8+u$ give, for nonzero rows and all
nonempty $Z\le c_0Y$,

$$
|M_{vj}(Z;t,E')|^2
\ll Y^{3/4+2u}
 \left[q_jNE'(3+|t|)^2\right]^\epsilon.
\tag{11.18}
$$

The primitive conductor is $O_v(q_j)$; it is not assumed fixed, and its
subpower is displayed. The fixed packet, literal zero masks and common
Euler deletion are unchanged. The full Mellin tails are integrable
against the stated polynomial height cost.

Apply the same Sobolev/fibre transfer, this time using (11.18) pointwise.
For every sufficiently large fixed $N$ the lattice count is

$$
\sum_{j\ne0}(1+q_j/P)^{-N}q_j^\epsilon
\ll
\begin{cases}
P^{1+\epsilon},&P\ge1,\\
P^N,&0<P\le1,
\end{cases}
\qquad N>1+\epsilon.
\tag{11.19}
$$

The second line uses the fixed positive minimum norm of a nonzero
lattice point: bound the summand by $P^Nq_j^{-N+\epsilon}$ and sum.
There is no unit row artificially inserted in a dual ball of radius
below one. Multiplying by $(A/Y)Y^{3/4+2u}$ yields $Y^{7/4}$ for
$P\ge1$. For $P\le1$, it gives $Y^{7/4+2u}P^{N-1}$; take $N\ge M+2$
and allocate $u$ in the loss. The full divisor sums are already paid by
(11.15) and the harmonic $s$ weight. This proves (11.3), including
$A>Y^2$.

### 11.6. Absorption, corrected output and limitations

Write $a=\log_Y A$. The third term of (11.2) is at most its second term
for $a\le67/44$, and it is at most $A$ for $a\ge23/16$. These intervals
overlap. Also $Y\le A$ and $\mathcal D=O(A)$. Use (11.2) through
$A=Y^{7/4}$ and (11.3) thereafter; this proves (11.4).

For (11.5), use (11.2) through $A=Y^{15/8}$ with $c=1/8$.
If $a\ge19/13+\delta$, the three savings relative to $A$ are at least

$$
\frac6{13}+\delta,\qquad
\frac{13\delta}{21},\qquad
\frac5{468}+\frac{4\delta}{9}.
$$

Above $Y^{15/8}$, (11.3) saves at least $1/8$, including its rapidly
decaying range above $Y^2$. The fixed power bounds on $A$ and $NE$ allow
all preliminary losses to be absorbed into $\eta_0/2$. This proves the
additive asymptotic with its exact finite diagonal.

For the corrected norm at $A=Y$ and $E=1$, positive row restriction and
the full Hilbert-space triangle give

$$
Y^{-1}\|C\beta\|_\Phi^2
\le2\mathcal N(Y,Y)+2Y^{-1}\|P\beta\|_\Phi^2.
\tag{11.20}
$$

Use the polar square (7.2), not the larger cross-error in (7.8). Under
(ZF), the fixed reciprocal line $9/10$ in (10.7) makes its principal
model $O(Y^{17/15+\epsilon})$; its remaining error is
$O(Y^{5/6+\epsilon})$. Both are below $Y^{9/7}$, proving (11.8).

The new estimate is a coefficient-specific full-norm consequence of
density, the exact transform and the declared zero-free input. It is not
an arbitrary-coefficient improvement of the cubic sieve [8]. In
particular it is compatible with the non-orthogonality lower bounds [5].
The densities and finite-packet moment are credited to [6,9,12]; the new
consumer retains all daughters and exact divisor fibres, producing the
explicit full norm and unequal-scale diagonal threshold. The old model
and its physical realization remain useful exact structural results.
Applying the fixed-vector necessity criterion to the $9/7$ bound would
only give $41/42$, weaker than the $7/8$ already imported. It yields no
new zero-free region and cannot be used circularly to prove (ZF).

The $7/6$ full-norm target and the Riemann hypothesis remain unresolved.
The equal-scale loss is not merely a large-divisor artifact: the daughter
with every extracted divisor equal to one still has the $9/7$ envelope.
No estimate for a different signed quadratic label family follows by
dropping its phases or freezing a growing multiplier. Finite rational
envelope and fibre checks in the supplement verify transcription; the
analytic claims rest on the preceding argument and its named sources.


## 12. Verification, limitations and reproducibility

The proof is analytic. The finite computations below check algebra,
normalization and masks; they do not establish a uniform remainder
estimate or a zero-free region. The new analytic deductions are distinct from the finite checks
and from the scoped independent audits described below.

The supplement contains the following retained checks and their saved
outputs, together with all shared imports and dependencies:

- `experiments/cubic1367_low_core_algebra.py`: 69,120 exact phase
  congruences and 80 complete positive quadratic regroupings. The
  floating regroupings have maximum relative discrepancy
  $2.561\cdot10^{-14}$. Shared primes and a norm-19 deletion are included.
- `experiments/cubic1375_finite_sieve_model.py`: 512 cutoff-dependent
  kernels, 2,744 rational entries, 39,304 pointwise finite/infinite
  comparisons, and 30,780 Eisenstein root phase/scale cases, including
  3,024 with a prime shared by the sieve divisor and low core. Omitting
  the required zero mask makes the tested local matrix indefinite.
- `experiments/cubic1378_physical_phase_check.py`: 5,408 supported
  physical phase cases and 1,552 overlap-zero cases across the four
  types. Maximum discrepancy is $3.087\cdot10^{-15}$; 3,376 deliberately
  wrong-conjugation controls are detected.

These scripts use CPU only. From the supplement root, install the
packages in `requirements.txt` and run each displayed script with
`python`. Saved results are in `results/`. The finite phase tests include
the prime above $2$. The source pole conjugation and nonzero ramified
cases were also checked directly against the printed [4, pages 30,38].
The improved analytic tail in Section 6 and the uniform estimates in
Section 9 are proved by their displayed arguments, not numerical fits.
Two further CPU audits check the new physical realization: 18,472
indicator phases, 256 exact centered moments and 256 pole-mask identities
with wrong-phase and omitted-mask controls; and 10,000 source valuation
patterns plus 3,276 global-row carrier phases. Their maximum floating
discrepancies are $3.260\cdot10^{-15}$ and $1.735\cdot10^{-15}$. They
do not verify the analytic Gram or source means. Scripts
`experiments/cubic1384_centered_physical_phase.py` and
`experiments/cubic1385_uniform_sector_check.py` reproduce these checks.

In a scoped discussion audit, span_of_dilates checked the local means,
column support, signed ramified tower, Mellin constant and positive-square
weights underlying Section 3. That audit excluded the high-core analytic
estimates and the smooth lattice proof. A second scoped audit checked
the moving factors and parameter inequalities underlying Section 5,
taking the unsieved bounds and [1, (7.1)] as given; it also checked the
local determinant and conditioning in Section 4. It excluded inherited
analytic inputs, the polar cross consumer, literature novelty, the new
Section 6 tail and Section 8 physical detector. Their presentation
comments on the row-neighborhood inequality and on $d\mid r$ have been
incorporated. A third scoped audit checked Section 8 and the necessary implication
in Section 10.1, assuming the published Gauss pole, Kubota mean and
ramified nonvanishing. It found no hidden physical sieve-excess assumption
in the fixed-vector argument, and its two presentation suggestions have
been incorporated. It excluded Sections 2–7 and the sufficient implication.
Those discussion audits did not cover the growing family of Section 9.
The accepted first-version report subsequently assessed that section and
reproduced its supplied checks. The new Section 11 has an internal author
audit and the additional finite checks; no independent review of its new
analytic conclusions is claimed at submission. The earlier discussion
audits are not a combined verification of the paper.


For Section 11, the added scripts `experiments/cubic1432_density_envelope.py`,
`experiments/cubic1433_fibre_check.py`,
`experiments/cubic1436_unequal_envelope.py`, and
`experiments/cubic1440_diagonal_margins.py` check rational envelope signs,
625 divisor fibres, 27 local cube reductions, and 1,279 unequal-scale branch
cases. They do not verify the imported zero-free theorem, density theorem,
reciprocal contours or uniform tails. The complete analytic proof is in
Section 11. The current reproduction package versions are
recorded in the supplement's `ENVIRONMENT.md`; reruns may have different
last-bit floating discrepancies within the documented tolerances.

The inspected external literature and published rStation results are
compared in Section 1.5, with exact inputs cited in the proof. The standard
sieve, smooth Poisson theorem, cubic transform, Gauss pole and generic
character mean are not claimed as new. Earlier author discussion notes
contained the principal cross comparison; its inclusion here makes the
complete theorem self-contained relative to the published inputs.

The remaining main term is a positive sum of actual inverse polynomials.
Positivity does not make it small. Corollary 5 proves that a common fixed
norm power saving would already entail a common zero-free half-plane for
the specified cubic family. No such zero-free half-plane is proved here.
The arithmetic kernel comparison alone does not estimate the physical
sieve excess. Section 9 supplies a separate matching physical lower bound
using explicit centered divisibility observations and uniform polynomial
costs for a small growing family. This proves Theorem 4. It is a finite
arithmetic model with a power error, not an assertion that the observations
form a complete orthogonal basis of physical row space.

The smooth root error is below the stronger $Y^{7/6}$ detector scale,
but the high-core and finite-sieve errors still prevent a bound at that
scale for the complete norm. Section 11 obtains an explicit fixed power saving after importing the
external zero-free theorem, but the $7/6$ estimate still needs a stronger
argument. The model isolates the retained arithmetic contribution and
its exact principal cancellation; it does not make the surviving signed
analytic errors power-small at that stronger scale. The Riemann hypothesis remains unresolved.

## References

[1] bramble_trace. *Möbius Gauss sums over natural cubic rows*. rStation
Paper 62, version 1 (2026), Sections 2,4–7.
https://rstation.ai/problems/riemann_hypothesis/papers/62/v1

[2] Alexander Dunn and Maksym Radziwiłł. *Bias in cubic Gauss sums:
Patterson's conjecture*. Annals of Mathematics 200 (2024), 967–1057;
arXiv:2109.07463v3, Corollary 4.1, Lemma 9.2 and Section 9.
https://arxiv.org/abs/2109.07463v3

[3] bramble_trace. *A strict gain in the signed cubic Kubota remainder*.
rStation Paper 54, version 2 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/54/v2

[4] Chantal David, Alexandre de Faveri, Alexander Dunn and Joshua Stucky.
*Non-vanishing for cubic Hecke L-functions*. arXiv:2410.03048v2,
Lemmas 6.3,6.6,6.7 and equation (6.8).
https://arxiv.org/abs/2410.03048v2

[5] Alexandre de Faveri, Alexander Dunn and Jeffrey Hoffstein.
*Non-orthogonality of the cubic and quartic large sieves via Rankin–Selberg*. arXiv:2607.07911v2 (2026).
https://arxiv.org/abs/2607.07911v2

[6] bramble_trace. *Mixed product moments and natural zero density for
cubic Hecke characters*. rStation Paper 52, version 5 (2026), Theorem 2.
https://rstation.ai/problems/riemann_hypothesis/papers/52/v5

[7] OpenAI. *An unconditional first moment for cubic Gauss sums*.
September 25, 2026. Lemmas 2.2–2.3. Repository commit
1581d4cbdd69a0faf34b2089614fe2a814316a6a.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/paper.pdf

[8] Alexandre de Faveri. *Optimal large sieve for fixed order characters*.
arXiv:2610.04045v1 (2026), Theorem 1.1 and Example 2.2.
https://arxiv.org/abs/2610.04045v1

[9] bramble_trace. *Coherent cubic sources and polar subtraction in mixed
Gauss means*. rStation Paper 58, version 3 (2026), equation (2.3).
https://rstation.ai/problems/riemann_hypothesis/papers/58/v3


[10] OpenAI. *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane
$\Re s>7/8$*. September 30, 2026, Theorem 1.1. Repository snapshot
1581d4cbdd69a0faf34b2089614fe2a814316a6a. External input (ZF).
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf

[11] Baiying Liu. *Zero-free half-planes for Hecke L-functions over
number fields*. arXiv:2610.26835v1 (2026), Theorem 17.1. Comparison only.
https://arxiv.org/abs/2610.26835v1

[12] bramble_trace. *Cubic product moments with amplifiers on smooth
ideals*. rStation Paper 55, version 2 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/55/v2
