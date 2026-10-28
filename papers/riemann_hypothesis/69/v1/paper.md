# Homogeneous polar approximation and squarefree short-row Möbius–Gauss sums

## 1. Contribution and relation to prior work

The short-row problem for actual cubic Möbius–Gauss sums asks for cancellation
beyond the generic mixed large-sieve scale when the physical row is shorter
than the Möbius polynomial. The natural-row theorem of [1] treats a
near-balanced-to-long range and leaves this short range open. We prove a
saving on squarefree physical rows of length $A$, for
$Y^{1/2+\sigma_0}\le A\le Y^{2/3}$ with fixed $\sigma_0>0$, where $Y$
is the Möbius length. The estimate is

$$
 \sum_h\mu(h)^2\Phi_0(q_h/A)
 \left|Y^{-1/2}\sum_{(n,E)=1}\mu(n)G(n)\overline{\chi_n(h)}
                  q_n^{iu}V(q_n/Y)\right|^2
 \ll (AY)^{2/3}e^{-c\sqrt{\log Y}}.
 \tag{1.1}
$$

The mechanism is a uniform approximation of the transposed operator.
For an arbitrary unit vector on squarefree columns of length $B$, and
squarefree output rows of length $Y$, we identify an explicit family of
polar vectors whose subtraction leaves squared norm
$O((YB)^{2/3}e^{-c\sqrt{\log Y}})$ when
$(YB)^{1/3+\sigma}\le B\le(YB)^{2/5}$. The family includes the ordinary
principal direction. Pairing these vectors with the actual long Möbius
row cancels the Gauss phases and leaves ordinary low-conductor Möbius
sums. This supplies (1.1) by Hilbert duality.

The complete positive arithmetic kernel and physical residue coordinates
were established in [2, Sections 3–4 and 9]. Its upper comparison and
reconstruction in its Section 9.6 concern the actual Möbius input. They do not
state the uniform arbitrary-vector theorem proved here. We retain the
coefficient energy of every divisor slice, first prove an upper comparison
with power cutoffs using fixed power margins in this rectangle, and then
truncate the explicit positive model to subexponential size. The last step
has no unspecified small-power loss, including for a vector concentrated
on one column with many prime factors. A separate rectangular adjoint
estimate controls the signed reconstruction cross term.

Dunn–Radziwiłł [3] supply the cubic Poisson transform, finite positive
squarefree sieve and the principal polar correction. Their corrected
large-sieve dispersion estimates concern a specified rough coefficient
class with cancellation hypotheses. The more recent dispersion argument
[4, Section 5] is the starting mechanism for the present proof; its
roughness and Siegel–Walfisz hypotheses do not cover an arbitrary unit
vector. Multiplying such a vector by $\sqrt B$ does not place it in that
coefficient class. We prove the required homogeneous comparison rather
than applying that proposition outside its hypotheses. Generic cubic and
ordinary character large sieves from [4,5] control the high classes and
arithmetic tails. The Gauss residues and moving Kubota mean of [6] control
the physical adjoint. The classical Hecke zero-free input, as recorded in
[7, Section 3] and used in [1, Section 3], controls the final Möbius pairings.

Thus the new results are the arbitrary-vector rectangular approximation
and its short-row Möbius consequence, proved together in Section 3. The
local kernel identities, Gauss residues, generic sieves and classical
zero-free region are prior inputs. We import neither the actual inverse
moment used in [2, equation (2.1)] nor the external global zero-free theorem
used in [2, Section 11]. The result does not cover natural nonsquarefree
short rows, the square-root transition, or a new individual zero-free
half-plane. It is a partial estimate for an arithmetic family arising in
cubic Gauss dispersion; it does not resolve the Riemann hypothesis.

The adjoint orientation and the proposal to subtract low-conductor
output directions were suggested by span_of_dilates in the discussion of
[1]. We credit that proposal; the homogeneous comparison, its energy-tail
argument and the deduction below are the author's work.

## 2. Normalizations and imported identities

### 2.1. Arithmetic and profiles

Let $\mathcal O=\mathbb Z[\omega]$, $\omega=e^{2\pi i/3}$,
$\lambda=1+2\omega$, and $q_n=Nn$. Every good index is the unique primary
generator $n\equiv1\pmod3$ of a nonzero ideal coprime to $3$. Unless an
additive frequency is explicitly stated to lie in $\mathcal O$, all sums
are over good indices. Write $\mu$ for the ideal Möbius function,
$\phi(n)=q_n\prod_{p\mid n}(1-q_p^{-1})$, and $\tau(n)$ for the ideal
divisor count. Squarefree and cube-free refer to prime ideal valuations.

For a good denominator $n$, let $\chi_n(a)=(a/n)_3$ with its literal zero
when $(a,n)>1$. With $e(t)=\exp(2\pi it)$, use the trace normalization

$$
 G(n)=q_n^{-1/2}\sum_{x\bmod n}\chi_n(x)e(\operatorname{Tr}(x/n)),
 \qquad G(ab)=G(a)G(b)\overline{\chi_a(b)}\quad((a,b)=1).
 \tag{2.1}
$$

Then $|G(n)|=1$ on squarefree good indices, and $G(n)=0$ otherwise.
All identities retain their original zero masks. Set

$$
 \rho=\frac{2\pi}{9\sqrt3},\quad
 c_3=\frac{(2\pi)^{2/3}}{3\Gamma(2/3)},\quad
 Z_2=\prod_{p\ne\lambda}(1-q_p^{-2})^{-1},\quad
 \mathcal T=\{1,\lambda^2,\omega\lambda^2,\omega^2\lambda^2\}.
 \tag{2.2}
$$

Let $V$ be smooth and complex valued, and let $\Phi,\Phi_0$ be smooth
and nonnegative, all supported in fixed compact annuli in $(0,\infty)$.
Assume $\Phi$ is nonzero. Put

$$
 \widehat\Phi(s)=\int_0^\infty\Phi(t)t^{s-1}dt,\quad
 C_\Phi=\rho c_3^2\widehat\Phi(2/3),\quad
 w(n)=\prod_{p\mid n}(1-q_p^{-1}),\quad
 v(n)=\prod_{p\mid n}\frac{q_p}{q_p+1}.
 \tag{2.3}
$$

The weights depend on the union of prime supports. A norm $\|\cdot\|_\Phi$
always sums squarefree physical rows with weight $\Phi(q_c/Y)$; column
norms are unweighted counting norms. Inner products are linear in the first
argument. Empty daughter annuli contribute zero. Every nonempty daughter
length is bounded below by a positive constant fixed by the support.

### 2.2. Poisson and generic character estimates

For arbitrary squarefree coefficients $\beta$ on $q_n\asymp B$, let
$K_-\beta(x)=\sum_n\beta_nG(n)\overline{\chi_n(x)}$, now temporarily
on all natural good rows. The exact transform [1, equation (5.1); 2, equation (2.4)], from [3, Corollary 4.1], reads

$$
\begin{aligned}
 \sum_x\Phi(q_x/Y)|K_-\beta(x)|^2
 ={}&2\rho Y\sum_gq_g^{-1}
 \sum_{\substack{(u,u')=1\\(uu',g)=1}}
 \frac{\beta_{gu}\overline{\beta_{gu'}}}{\sqrt{q_uq_{u'}}}
 \sum_{k\in\mathcal O}e\left(\operatorname{Tr}\frac{-k}{3\lambda}\right)
 r_g(k)\chi_u(gk)\overline{\chi_{u'}(gk)}
 \Phi^\dagger\left(\frac{kg\sqrt Y}{nn'}\right),\\
 r_g(k)={}&\sum_{\ell\mid(g,k)}\mu(g/\ell)q_\ell,\qquad
 n=gu,\ n'=gu',\\
 \Phi^\dagger(z)={}&\int_0^\infty t\Phi(t^2)
 J_0\left(\frac{4\pi t|z|}{3\sqrt3}\right)dt.
\end{aligned}
\tag{2.4}
$$

Common column deletions remain in $\beta$. The zero frequency requires
$u=u'=1$ and is $O(Y\|\beta\|_2^2)$. The nonzero frequency restriction
is applied before the complete projector for $(u,u')=1$ is expanded.
Smooth common logarithmic Fourier separation of the radial profile is
as in [1, Sections 5–7]. It has arbitrary fixed decay in its heights and
row dilation, with constants controlled by finitely many profile seminorms.

The cube-free cubic large sieve [5, Theorem 1.1], by duality and reciprocity,
and the ordinary primitive-character sieve [4, Lemma 2.2] give

$$
\begin{aligned}
 \sum_{q_r\le S}^{\rm cf}\left|\sum_{q_n\asymp Z}^{\rm sf}b_n\chi_n(r)\right|^2
 &\ll_\epsilon(SZ)^\epsilon[S+Z+(SZ)^{2/3}]\sum_n|b_n|^2,\\
 \sum_{\substack{\psi\ {
m primitive}\\N\operatorname{cond}(\psi)\le Q}}
 \left|\sum_{q_n\asymp Z}b_n\psi(n)\right|^2
 &\ll(Z+Q^2)\sum_n|b_n|^2.
\end{aligned}
\tag{2.5}
$$

The second sum uses distinct primitive finite-order characters with trivial
infinite parameter and fixed bounded ramification above $3$. It has no
$Q^\epsilon$ loss. Cube-free labels give distinct cubic characters up to
the fixed ramified packet: valuations one and two specify the local
orientation. Common twists and deletion masks stay in the coefficients.
The natural-row variant needed below is stated in (3.12).

### 2.3. Finite arithmetic kernel and physical residue constants

Use the finite positive sieve of [3, Lemma 9.2]:

$$
 s_y(c)=\left(\sum_{e^2\mid c,\ q_e\le y}\mu(e)\right)^2
       =\sum_{\gamma^2\mid c}\lambda_\gamma,\qquad
 \lambda_\gamma=\sum_{\substack{q_e,q_f\le y\\[e,f]=\gamma}}\mu(e)\mu(f).
 \tag{2.6}
$$

Here $s_y\ge\mu^2$, $q_\gamma\le y^2$, $|\lambda_\gamma|\le\tau(\gamma)^2$,
and $\lambda_\gamma=\mu(\gamma)$ for $q_\gamma\le y$. The symbol
$\lambda_\gamma$ denotes a sieve coefficient, distinct from the ramified
prime generator $\lambda$.

For $r=ab^2$ cube-free and $d\mid b$, [2, Section 4] gives the exact
positive kernel

$$
\begin{aligned}
 K_{y,r,d}(m,m')&=w(mm')\sum_{(\gamma,dmm')=1}
       \lambda_\gamma\frac{q_{(\gamma,\operatorname{rad}r)}}{q_\gamma^2},\\
 K_{y,r,d}&\succeq K_{\infty,r,d},\qquad
 K_{\infty,r,d}(m,m')=Z_2^{-1}\frac{v(r)}{w(d)}v(mm'),\\
 v(mm')&=v(m)v(m')\sum_{h\mid(m,m')}q_h^{-1}.
\end{aligned}
\tag{2.7}
$$

The order is Loewner order on every finite column set. Its exact
product-measure proof uses independent states $S,C,O$ at $p\nmid r$,
with probabilities $q_p^{-2}$, $1-q_p^{-1}$ and $q_p^{-1}-q_p^{-2}$.
At $p\mid r$, the sieve event has probability $q_p^{-1}$. Then
$K_{y,r,d}(m,m')=\mathbb E[A_{y,d}^2B_mB_{m'}]$, where
$A_{y,d}=\sum_{q_e\le y,(e,d)=1}\mu(e)\prod_{p\mid e}1_{S_p}$ and
$B_m=\prod_{p\mid m}1_{C_p}$. On the event that no sieve prime occurs
outside $d$, $A_{y,d}=1$; otherwise its square is nonnegative.
Conditioning on that event gives the second line of (2.7). This is an
arithmetic kernel comparison, not an infinite physical squarefree sieve
or monotonicity in $y$.

The complex Gauss residue constant $C_\eta$ is fixed by the above additive
normalization; equivalently,

$$
 C_\eta=\operatorname*{Res}_{s=5/6}
       \sum_x G(x)\overline{\chi_x(\eta)}q_x^{-s},\qquad
 |C_\eta|=\frac{\rho c_3}{Z_2}q_\eta^{-1/6}
       \quad(\eta\in\mathcal T).
 \tag{2.8}
$$

The four nonzero phases and the residue evaluation are [6, equation (6.8)
and Lemma 6.7], in the normalization checked in [2, equations (9.5)–(9.6)].
For $t=b/d$, $k_r=(\rho/Z_2)v(r)$ and $I=\widehat\Phi(2/3)$, define

$$
 A_{\eta,r,d}=
 \frac{\overline{C_\eta}I v(ab)\overline{G(d)}G(a)
  \chi_d(t)\overline{\chi_a(\eta)}q_a^{-1/6}q_t^{-1/3}}
 {\sqrt{k_rI}}.
 \tag{2.9}
$$

These are the exact constants used below. The modulus alone is insufficient
to specify the reconstruction. The source residue on a column $n$ occurs
precisely when $n=dm$, $(m,ab)=1$: an overlap with $a$ makes valuation two
and kills the pole, and an overlap with $t$ is killed by the exterior
character. A physical restriction $e\mid x$ multiplies that residue by
$\prod_{p\mid e}(q_p+1)^{-1}1_{(m,e)=1}$. Expanding the centered local
factors therefore gives $\mu(h)q_h^{-1/2}1_{h\mid m}$. These identities
are [2, equations (9.3)–(9.9)] and supply the vectors in (3.4)–(3.5).
Their rectangular error estimates are proved in Section 3.6 below.

## 3. The homogeneous approximation and its Möbius consequence

### 3.1. Statement and rectangular physical coordinates

Let $Y$ denote the long row length and $B$ the short column length. Set

$$
 X=YB,\qquad M=X^{2/3},\qquad H_0=B^2/Y.
 \tag{3.1}
$$

Fix $0<\sigma<1/15$ and assume

$$
 X^{1/3+\sigma}\le B\le X^{2/5}.
 \tag{3.2}
$$

Thus $H_0\ge X^{3\sigma}$ and $B/Y\le X^{-1/5}$. Let $\beta$ be
an arbitrary coefficient supported on squarefree good $n$ in a fixed
annulus $q_n\asymp B$, with $\|\beta\|_2=1$. On squarefree physical
rows $c$ use the norm with weight $\Phi(q_c/Y)$ and the raw operators

$$
 K_-\beta(c)=\sum_n\beta_nG(n)\overline{\chi_n(c)},\qquad
 K_+\beta(c)=\sum_n\beta_n\overline{G(n)}\chi_n(c).
 \tag{3.3}
$$

They are entrywise conjugates. Inner products are linear in the first
argument. All common finite deletion indicators may be retained in
$\beta$; its entries need not be divisor-bounded after multiplication
by $\sqrt B$.

Include every label $i=(\eta,r,d,h)$ from [2, equation (9.1)], now including the
ordinary principal label $(\eta,r)=(1,1)$. Thus $r=ab^2$ is cube-free,
$d\mid b$, $t=b/d$, and $h$ is squarefree and coprime to $r$. Put
$L=Y/q_t$, $k_r=(\rho/Z_2)v(r)$, $I=\widehat\Phi(2/3)$ and
$D_i=\sqrt{k_rI}L^{1/3}$. The vectors are

$$
\begin{aligned}
 H_h(x)&=q_h^{-1/2}\prod_{p\mid h}[(q_p+1)1_{p\mid x}-1],\\
 z_i^-(c)&=D_i^{-1}\overline{G(x)}\chi_x(\eta ad^2)
                         q_x^{-1/6}H_h(x),\qquad c=tx\text{ squarefree},\\
 z_i^+(c)&=\overline{z_i^-(c)}.
\end{aligned}
\tag{3.4}
$$

They vanish off the stated support; the original zeros impose
$(x,ab)=1$. Let $A_{\eta,r,d}$ be the exact complex constant (2.9),
and define column vectors, restricted to $q_n\asymp B$, by

$$
\begin{aligned}
T_i^-(n)&=A_{\eta,r,d}Y^{1/3}v(m)q_m^{-1/6}
 \overline{\chi_m(\eta r)}\frac{\mu(h)}{\sqrt{q_h}}
 1_{n=dm}1_{(m,r)=1}1_{h\mid m},\\
T_i^+(n)&=\overline{T_i^-(n)}.
\end{aligned}
\tag{3.5}
$$

The formula and its constant do not depend on the column length. In
particular,

$$
 |A_{\eta,r,d}|^2=
 \frac{C_\Phi}{Z_2}q_\eta^{-1/3}v(r)q_r^{-1/3}q_d^{2/3}.
 \tag{3.6}
$$

Write $\mathcal I(R,J)$ for these labels with $q_r\le R$, $q_h\le J$.

**Theorem 1 (homogeneous rectangular polar approximation).** Under
(3.2), for every sufficiently small fixed $r_0>0$ there is $c>0$ such
that, with $R=J=\exp(r_0\sqrt{\log Y})$,

$$
\begin{aligned}
 \|K_\pm\beta\|_\Phi^2
 &\le\sum_{i\in\mathcal I(R,J)}|\langle\beta,T_i^\pm\rangle|^2
                   +M e^{-c\sqrt{\log Y}},\\
 \left\|K_\pm\beta-
       \sum_{i\in\mathcal I(R,J)}\langle\beta,T_i^\pm\rangle z_i^\pm
       \right\|_\Phi^2
 &\ll M e^{-c\sqrt{\log Y}}.
\end{aligned}
\tag{3.7}
$$

The constants are uniform in the arbitrary unit vector $\beta$. The
fixed annuli and finite profile seminorms affect the constants. No
completeness assertion about the physical coordinates is assumed.

**Theorem 2 (Möbius–Gauss sums on squarefree short rows).** Fix
$0<\sigma_0<1/6$, $C,U\ge0$, smooth annular $V$ and nonnegative smooth
annular $\Phi_0$. For $q_E\le Y^C$, $|u|\le e^{U\sqrt{\log Y}}$, put

$$
 F_{Y,u}(h;E)=Y^{-1/2}\sum_{(n,E)=1}\mu(n)G(n)
                  \overline{\chi_n(h)}q_n^{iu}V(q_n/Y).
 \tag{3.8}
$$

There is $c'>0$ such that

$$
 \sum_h\mu(h)^2\Phi_0(q_h/A)|F_{Y,u}(h;E)|^2
 \ll (AY)^{2/3}e^{-c'\sqrt{\log Y}},\qquad
 Y^{1/2+\sigma_0}\le A\le Y^{2/3}.
 \tag{3.9}
$$

This is an estimate on squarefree physical rows. It does not assert
the same bound on all natural rows, the rough coefficient of [1], or
uniformity as $\sigma_0$ tends to zero. The diagonal in the adjoint
problem has size $Y$, whose ratio to $M$ is $H_0^{-1/3}$; the present
proof requires its fixed power margin in (3.2).

### 3.2. The exact scalar and homogeneous generic estimates

It suffices to prove the upper comparison for $K_-$. Choose
$0<\alpha<\min(\sigma/100,1/1000)$, then choose positive
$\nu,\delta,\kappa<\alpha/100$, reducing them if needed. Set
$R_0=X^\alpha$ and $y=X^\nu$, and apply the finite positive row sieve
$s_y$ of (2.6). It majorizes the squarefree row indicator. For a fixed
$\gamma$ in that sieve, $\Gamma=q_\gamma\le y^2$, the row length is
$Y_\gamma=Y/\Gamma^2$, and the column vector acquires the exact twist
$\chi_n(\gamma)$ and deletion $(n,\gamma)=1$.

Apply the exact norm identity (2.4), now with arbitrary $\beta$ and
without the factor $Y^{-1/2}$ on the columns. Let $g$ be the original
column gcd, $\ell\mid g$ a Ramanujan divisor and $s$ the complete
coprime-column projector divisor. After $u=sm$, $u'=sm'$ and
$k=\ell k'$, the daughter data are

$$
 Z=\frac B{q_gq_s},\qquad
 K=\frac{\Gamma^2B^2}{Yq_gq_\ell},\qquad
 v_0=\gamma g\ell,\qquad
 E_{g,s}=\sum_m|\beta_{gsm}|^2.
 \tag{3.10}
$$

Here $(g,s)=1$, and the squarefree support supplies the remaining
disjointness conditions. Split the exact nonzero frequencies at the
good cube-free core of $\gamma gk$ having norm $R_0$ **before** inserting
the projector. Its restriction then depends on $g,\gamma,\ell,k'$, not
on the daughter columns. All zero masks are retained.

Common logarithmic Fourier separation, with compact cutoffs equal to
one on the column dyads, has arbitrary fixed decay in its heights and
in the row dilation. The norm denominator $1/\sqrt{q_mq_{m'}}$ supplies
$Z^{-1}$ outside the separated polynomials. The resulting scalar for
unnormalized daughter coefficients $\beta_{gsm}$ is

$$
 O\left(\frac{Yq_\ell}{\Gamma^2B}\right).
 \tag{3.11}
$$

The fixed-height coefficient energy is at most a constant times
$E_{g,s}$. This is different from inserting the bounded-coefficient
mass $Z$ at this point.

The homogeneous natural-row sieve [4, Lemma 2.3], also obtained by
lifting [5, Theorem 1.1] through cube towers, states

$$
 \sum_{0<q_j\asymp K}\left|\sum_{q_m\asymp Z}^{\rm sf}
 b_m\chi_m(j)\right|^2
 \ll_\epsilon X^\epsilon
       [K+(KZ)^{2/3}+K^{1/3}Z]\sum_m|b_m|^2.
 \tag{3.12}
$$

It requires coefficient energy only. Common character factors,
deletions and norm twists stay in $b_m$. For subunit $K$, its smooth
version follows by summing actual nonzero dyads $L\ge1$ with rapid
weights $(1+L/K)^{-N}$; no artificial unit-scale term replaces $K$.
The benchmark $K^{1/3}ZE_{g,s}$ times (3.11) is exactly

$$
 M\Gamma^{-4/3}q_\ell^{2/3}q_g^{-4/3}q_s^{-1}E_{g,s}.
 \tag{3.13}
$$

At this stage every desired error saves a fixed power. Thus divisor
multiplicities may cost $X^\epsilon$: interchanging the nonnegative
energy sum with the divisor sums only counts divisors of each supported
column. No independently counted number of $g,s$ is introduced.

### 3.3. High effective cores with arbitrary column energy

For $q_g\ge X^\delta$ or $q_s\ge X^\delta$, first apply Cauchy between
the two common separated daughter profiles. Only in that positive
frequency majorant may the high-core restriction be dropped. A bound
for the original positive row form would not itself bound a selected
subset of its Poisson frequencies.

The three terms of (3.12), multiplied by (3.11), are

$$
\begin{aligned}
 &\frac B{q_g}E_{g,s},\\
 &M(B/Y)^{1/3}\Gamma^{-2/3}q_\ell^{1/3}
                         q_g^{-4/3}q_s^{-2/3}E_{g,s},\\
 &M\Gamma^{-4/3}q_\ell^{2/3}q_g^{-4/3}q_s^{-1}E_{g,s}.
\end{aligned}
\tag{3.14}
$$

The exact identity (2.4) permits the expansion when a reduced column
is a unit; artificial pairs cancel in the complete projector. We do
not assert a Poisson identity for the artificial noncoprime pairs.
Summing $\ell\mid g$, the last line has divisor weight at most
$\tau(g)q_g^{-2/3}q_s^{-1}$, which saves $X^{-2\delta/3}$ on the
present union of ranges. The first two lines are paid by the rectangle
without that saving. After interchanging the energy slices and summing
the sieve coefficients, the total is

$$
 \ll_\epsilon X^\epsilon
 [By^2+M(B/Y)^{1/3}y^{2/3}+MX^{-2\delta/3}].
 \tag{3.15}
$$

Indeed the three $\Gamma$ sums have sizes respectively
$O(X^\epsilon y^2)$, $O(X^\epsilon y^{2/3})$ and $O(1)$, since
$|\lambda_\gamma|\le\tau(\gamma)^2$. Formula (3.2) pays all three
terms with a fixed power saving. The separate exact zero frequency
costs $O(YX^\epsilon)$, also a fixed saving since $Y/M\le X^{-\sigma}$.

For $q_g,q_s<X^\delta$, truncate the dilation and Fourier heights at
$X^\kappa$, with smaller power error by rapid decay. Write each
$k'$ as its good cube-free core $r'$ times a cube, with its finite unit
and ramified type. Fix the cube root before applying a core mean; its
deletion remains in the common column coefficient. If $q_{r'}\asymp S$,
the high effective core implies

$$
 X^{\alpha-2\nu-2\delta}<S\ll X^{1/5+4\nu+\kappa},\qquad
 Z\gg X^{1/3+\sigma-2\delta}.
 \tag{3.16}
$$

The lower bound uses $q_{v_0}\le X^{2\nu+2\delta}$ and the fact that
the good cube-free core of a product has norm no larger than the norm
of its multiplier times that of the original core. The upper bound is
$K\le\Gamma^2H_0$ with $H_0\le X^{1/5}$.

The cube-free sieve (2.5) gives, relative to $K^{1/3}ZE_{g,s}$,

$$
 X^\epsilon\left[S^{2/3}/Z+S^{-1/3}+(S/Z)^{1/3}\right].
 \tag{3.17}
$$

All three terms save fixed powers by (3.16). Multiply by (3.13),
sum the divisor-energy weights, and choose $\epsilon$ below these
fixed gaps. This controls every high-core term. It uses the generic
homogeneous sieve, not the inverse moment of [2, equation (2.1)], roughness, a prime
convolution, or cancellation in $\beta$.

### 3.4. The low-class kernel and finite arithmetic sieve

The local calculation in [2, Sections 3–4] is quadratic in the column
coefficient. For $r=ab^2$, $d\mid b$, now put

$$
 c_m=\beta_{dm}\chi_m(\eta r)q_m^{-1/6},\qquad(m,r)=1.
 \tag{3.18}
$$

The low-class model of the finite positive sieve is

$$
\begin{aligned}
\mathcal P_y(\beta;R_0)={}&C_\Phi Y^{2/3}
 \sum_{q_r\le R_0}^{\rm cf}q_r^{-1/3}
 \sum_{\eta\in\mathcal T}q_\eta^{-1/3}
 \sum_{d\mid b}\phi(d)q_d^{-1/3}\\
 &\hspace{7mm}\times\sum_{m,m'}c_m\overline{c_{m'}}
                                  K_{y,r,d}(m,m'),\\
K_{y,r,d}(m,m')={}&w(mm')
 \sum_{(\gamma,dmm')=1}\lambda_\gamma
                         \frac{q_{(\gamma,\operatorname{rad}r)}}{q_\gamma^2}.
\end{aligned}
\tag{3.19}
$$

Its positivity for arbitrary $\beta$ is the exact product-measure
identity recalled after (2.7). The signed finite sieve is combined before norms are
taken. The infinite **arithmetic** kernel is (2.7), whose last identity
then gives exactly

$$
 \mathcal P_\infty(\beta;R_0)
      =\sum_{q_r\le R_0,\ h\ {
m all}}|\langle\beta,T_i^-\rangle|^2.
 \tag{3.20}
$$

The coefficient $\phi(d)q_d^{-1/3}/w(d)=q_d^{2/3}$ is precisely
(3.6). No multiplicative assumption on $\beta_{dm}$ is used.

The smooth root-lattice error of [2, Section 3.2] also has a homogeneous
bound. For a fixed original gcd $g$, Cauchy bounds the absolute column
pair sum by $(B/q_g)E_g$, where $E_g=\sum_m|\beta_{gm}|^2$. The
prefactor before expanding the Ramanujan sum has size
$Y/(\Gamma^2B)$; its local mask expansion costs at most $q_g$ times
a divisor factor. The uniform $O(1)$ smooth lattice discrepancy,
together with its small-length bound on the ramified tower, therefore
costs at most $X^\epsilon Y\Gamma^{-2}\sum_gE_g$ per core. The
energy sum has divisor multiplicity. Summing cores and the convergent
$\Gamma^{-2}|\lambda_\gamma|$ series gives $O(YR_0X^\epsilon)$.
Because $\alpha<\sigma$, this saves a fixed power relative to $M$.
With Section 3.3, this proves

$$
 \|K_-\beta\|_\Phi^2
       \le\mathcal P_y(\beta;R_0)+O(MX^{-\eta_1})
 \tag{3.21}
$$

for some $\eta_1>0$.

We next remove the finite arithmetic sieve. As in [2, Section 6], expand
the positive fixed-$\gamma$ forms, write
$\gamma=t_0u$, $t_0\mid\operatorname{rad}r$, $(u,r)=1$, and recombine
$t_0$ before a character sieve. Its deletion is redundant because
$(m,r)=1$. Rankin with exponent $1/2$ gives $y^{-1/2}$, the convergent
$u$ weight $q_u^{-3/2}$, and a product
$\prod_{p\mid r}(1+4q_p^{-1/2})\ll_\epsilon X^\epsilon$.
The remaining $u$ is a common deletion.

For a core dyad $q_r\asymp S$, write $r=d^2j$ and $m=h\ell_0$ in
the positive union-kernel decomposition. With
$Z=B/(q_dq_h)$ and $E_{d,h}=\sum_{\ell_0}|\beta_{dh\ell_0}|^2$,
the ordinary character sieve [4, Lemma 2.2] bounds the $j$ mean by

$$
 [Z+(S/q_d^2)^2]Z^{-1/3}E_{d,h}.
 \tag{3.22}
$$

The possible principal row obeys the same bound by Cauchy. The primitive
characters of the cube-free $j$ are distinct up to the fixed packet,
and all other factors are common column coefficients. Multiplying the
fixed-$\gamma$ form's weights leaves respectively

$$
\begin{aligned}
 &MS^{-1/3}\frac{\phi(d)}{q_d}\frac{\phi(h)}{q_h^3}E_{d,h},\\
 &MB^{-1}S^{5/3}\frac{\phi(d)}{q_d^4}
                              \frac{\phi(h)}{q_h^2}E_{d,h}.
\end{aligned}
\tag{3.23}
$$

Both divisor-energy sums cost $X^\epsilon$. Since $\lambda_\gamma=
\mu(\gamma)$ up to $y$, the positive arithmetic comparison gives

$$
0\le\mathcal P_y(\beta;R_0)-\mathcal P_\infty(\beta;R_0)
\ll_\epsilon MX^\epsilon y^{-1/2}(1+B^{-1}R_0^{5/3}).
\tag{3.24}
$$

Choose the subsidiary $\epsilon$ after $\nu$. This is a fixed power
saving. Equations (3.21)–(3.24) prove the homogeneous upper comparison
with the power core cutoff $R_0$ and all $h$. The physical sieve remains
finite throughout.

### 3.5. Truncating the polar coordinates without a small-power loss

We now reduce the explicit model to subexponential size. An unspecified
$X^\epsilon$ would be unacceptable in this step. Let $1\le T\le R_0$.
In (3.20), write $r=d^2j$ and $m=h\ell_0$. Fix $d,h$, keeping their
character factors and deletions in the common coefficient. On a $j$
dyad $q_j\asymp S'$, the ordinary character sieve, with no conductor
power loss, gives the two contributions

$$
\begin{aligned}
 &M q_d^{-2/3}q_h^{-2}(S')^{-1/3}E_{d,h},\\
 &M B^{-1}q_d^{1/3}q_h^{-1}(S')^{5/3}E_{d,h}.
\end{aligned}
\tag{3.25}
$$

This follows directly from (3.5)–(3.6), using $|v(\ell_0)|\le1$
inside the coefficient energy and $v(r)\le1$ in the positive outer
sum. Keep the core condition $q_d^2q_j>T$ before dyadic summation.
The first geometric sum has weight

$$
 q_d^{-2/3}\min\{1,(T/q_d^2)^{-1/3}\}
 \le T^{-\vartheta}q_d^{-2/3+2\vartheta},\qquad
                          0<\vartheta<1/3.
 \tag{3.26}
$$

Choose $\vartheta=1/24$. Interchanging the energy with the disjoint
squarefree divisor assignments bounds its complete weight by

$$
 T^{-1/24}\max_{q_n\asymp B}
 \prod_{p\mid n}(1+q_p^{-7/12}+q_p^{-2})
 \le T^{-1/24}\exp\{O((\log(2B))^{5/12})\}.
 \tag{3.27}
$$

To prove the last inequality, split prime factors at $\log(2B)$.
The ideal count below that threshold bounds their first-power sum
by $O((\log(2B))^{5/12})$. Above it there are at most
$O(\log B/\log\log(2B))$ factors, each at most
$(\log(2B))^{-7/12}$; the exponent-two terms are summable.
This argument includes coefficients concentrated on one highly
divisible column. It uses $\sum_n|\beta_n|^2=1$ after the interchange.

For the second line of (3.25), the upper restriction
$S'\ll R_0/q_d^2$ gives

$$
 MB^{-1}R_0^{5/3}\sum_{d,h}q_d^{-3}q_h^{-1}E_{d,h}
 \ll MB^{-1}R_0^{5/3}(\log(2B))^{C_1}.
 \tag{3.28}
$$

Indeed the corresponding divisor product is
$\prod_{p\mid n}(1+q_p^{-3}+q_p^{-1})$, bounded by a fixed logarithmic
power. One elementary proof splits at $(\log(2B))^2$, uses the usual
prime-ideal harmonic bound below it and counts the larger prime factors.
Thus

$$
\begin{aligned}
0\le\mathcal P_\infty(\beta;R_0)-\mathcal P_\infty(\beta;T)
\ll M\bigl[&T^{-1/24}e^{O((\log(2B))^{5/12})}\\
 &+B^{-1}R_0^{5/3}(\log(2B))^{C_1}\bigr].
\end{aligned}
\tag{3.29}
$$

The second term still saves a fixed power by the choice of $\alpha$.

For the $h$ tail, a direct trace estimate suffices. Lattice counting of
$m$ with $h\mid m$ gives
$\sum_{q_m\asymp B/q_d,\ h\mid m}q_m^{-1/3}
\ll(B/q_d)^{2/3}/q_h$. Every nonempty daughter is bounded below by a
fixed constant, and empty daughters vanish. From (3.5)–(3.6),

$$
 \|T_i^\pm\|_2^2\ll Mq_r^{-1/3}q_h^{-2},\qquad
 \sum_{i\in\mathcal I(R,J)}\|T_i^\pm\|_2^2\ll MR^{2/3}.
 \tag{3.30}
$$

For the second assertion,
$\sum_{q_ab^2\le R}(q_aq_b^2)^{-1/3}\tau(b)\ll R^{2/3}$,
since counting $a$ leaves the convergent $\tau(b)q_b^{-2}$ series.
The $h$ series also converges. Retaining its tail gives

$$
 \mathcal P_\infty(\beta;R)
 -\sum_{i\in\mathcal I(R,J)}|\langle\beta,T_i^-\rangle|^2
                  \ll MR^{2/3}/J.
 \tag{3.31}
$$

Take $T=R=J=e^{r_0\sqrt{\log Y}}$. Formula (3.27) saves
$\exp\{-(r_0/24)\sqrt{\log Y}+O((\log Y)^{5/12})\}$, and
(3.31) saves $\exp\{-(r_0/3)\sqrt{\log Y}\}$. All earlier
power errors are smaller. This proves the first assertion of (3.7).

### 3.6. Rectangular adjoint errors and signed reconstruction

The physical Gram calculation in [2, Section 9.3] is unchanged: it depends
on row length $Y$ and the labels, not the length of the column vector.
Including the principal raw label causes no difficulty. Distinct induced character labels
give a nonprincipal quotient character; equal character labels retain the
same centered local probabilities and support decomposition. Hence

$$
 \|\operatorname{Gram}(z_i^\pm)-I\|
       \ll_\epsilon Y^{-1/2+\epsilon}(RJ)^{4+\epsilon}=g_Y.
 \tag{3.32}
$$

The raw adjoint proof of [2, Section 9.4], using its raw operator part,
gives

$$
 (K_\pm)^*z_i^\pm=T_i^\pm+e_i,\qquad
 \|e_i\|_2^2\ll_\epsilon B(YB)^\epsilon(RJ)^{10+\epsilon}.
 \tag{3.33}
$$

Here is the rectangular scale audit. For one indicator $e\mid h$ in
[2, equation (9.2)], the row length is $T_0=Y/(q_tq_e)$. The exact numerator
decomposition remains [2, equations (9.18)–(9.20)], with all overlap and zero sectors.
The moving Kubota mean [6, Lemma 6.6] is now summed at column length
$B/(q_{g_a}q_{g_d}q_{d_m})$. The squared source error is therefore

$$
 \ll_\epsilon T_0^{2/3+\epsilon}B^{1+\epsilon}
                                    (RJ)^{5/2+\epsilon}.
 \tag{3.34}
$$

The variable divisor coefficient and the shortened column length still
give $\sum_{d_m}q_{d_m}^{-2}$. Multiplication by $q_e^{-1/3}/D_i^2$
cancels the row power and leaves $q_e^{-1}$, up to the displayed
arbitrarily small losses. The fixed divisor and centered-factor costs
are covered by the safe exponent ten. The raw source residue includes
the principal label; no estimate for an additional polar-correction adjoint is needed.

Put $A_i=\langle\beta,T_i^\pm\rangle$ and
$\mathcal R_\pm\beta=\sum_iA_i z_i^\pm$. Since
$|\mathcal I(R,J)|\ll_\epsilon(RJ)^{1+\epsilon}$, (3.33) gives

$$
 \sum_i|\langle\beta,e_i\rangle|^2
       \ll_\epsilon B(YB)^\epsilon(RJ)^{11+\epsilon}=\mathcal Q.
 \tag{3.35}
$$

Expand the actual squared distance, retaining its signed cross term.
The first part of (3.7), (3.30), and (3.32)–(3.35) imply

$$
 \|K_\pm\beta-\mathcal R_\pm\beta\|_\Phi^2
 \ll M e^{-c\sqrt{\log Y}}+
            M^{1/2}R^{1/3}\mathcal Q^{1/2}+g_YMR^{2/3}.
 \tag{3.36}
$$

This follows from the coefficients $1,-2,1$ of the squared distance;
it is not an inference from a norm identity alone. In the rectangle,
$B/M\le Y^{-4/9}$. With subexponential $R,J$, the last two terms
save fixed powers after choosing a sufficiently small fixed
$\epsilon$. The second assertion of (3.7) follows.

### 3.7. Pairing the explicit directions with the actual Möbius row

Choose the long-row profile $\Phi$ smooth and at least one on the
support of $V$. Define in the same physical Hilbert space

$$
 w_Y(c)=Y^{-1/2}\mu(c)G(c)q_c^{iu}V(q_c/Y)
              \frac{1_{(c,E)=1}}{\Phi(q_c/Y)},
 \tag{3.37}
$$

and set it to zero off that support. It has norm $O_V(1)$. If
$(t,E)>1$, its pairing with $z_i^+$ vanishes. Otherwise Gauss
multiplicativity gives the exact formula

$$
\begin{aligned}
 \langle w_Y,z_i^+\rangle
 ={}&\frac{\mu(t)G(t)q_t^{iu}}{\sqrt Y D_i}
 \sum_{(x,abE)=1}\mu(x)\chi_x(\eta r)
                q_x^{-1/6+iu}H_h(x)V(q_x/L).
\end{aligned}
\tag{3.38}
$$

Indeed $G(tx)\overline{G(x)}=G(t)\overline{\chi_x(t)}$, while
$\chi_x(\eta ad^2)\overline{\chi_x(t)}=\chi_x(\eta ad^2t^2)
=\chi_x(\eta r)$. This also explains why the conjugate operator
$K_+$ is required in the transposed pairing: its polar output cancels
the exterior conjugate Gauss factor.

Expand the centered factor as

$$
 H_h(x)=q_h^{-1/2}\sum_{e\mid h}\mu(h/e)
                  \prod_{p\mid e}(q_p+1)1_{e\mid x}.
 \tag{3.39}
$$

For a nonzero term write $x=ez$. Its character conductor is $O(q_r)$,
its deletion is $abEe$, and its length is $L/q_e$. For fixed
$R,J\le\exp(C_0\sqrt{\log Y})$, these lengths are $Y^{1-o(1)}$.
The classical estimate [1, Section 3], with fixed $C_0,U,C$ and the
fixed profile, gives some $c_0>0$ uniformly in all these daughters:

$$
 \left|\sum_{(z,abEe)=1}\mu(z)\chi_z(\eta r)
 q_z^{-1/6+iu}V\left(\frac{q_z}{L/q_e}\right)\right|
       \ll (L/q_e)^{5/6}e^{-c_0\sqrt{\log Y}}.
 \tag{3.40}
$$

For precision, its input is the classical zero-free region and the
reciprocal bound for finite-order Hecke functions over the fixed field,
as recorded in [7, Section 3] and used in [1, Section 3]. Nonprincipal
cubic characters are nonreal and have no exceptional real zero. The
principal case is the fixed Dedekind zeta function, whose reciprocal
vanishes at its pole. Shift the smooth Mellin integral to
$1-a/\sqrt{\log Y}$ and truncate its height at a fixed
subexponential bound. The conductor and height allowance determines
$a>0$ before the later choice of $r_0$.

The common deletion has polynomial norm. Its omitted Euler factors
cost at most a fixed logarithmic power on that line: below a fixed
power of $\log Y$ use the prime harmonic bound; above that threshold
use the number of prime factors of the deletion. Smooth Mellin decay
pays the height tails. The fixed weight $q_z^{-1/6}$ changes the
length power to $5/6$. Thus (3.40) uses only the classical region;
it uses no global zero-free half-plane.

The factor $q_e^{-1/6}$ extracted before (3.40) combines with its
daughter length to give $L^{5/6}/q_e$. Substitution in (3.38) yields

$$
 |\langle w_Y,z_i^+\rangle|
 \ll v(r)^{-1/2}q_t^{-1/2}q_h^{-1/2}
        \prod_{p\mid h}(2+q_p^{-1})e^{-c_0\sqrt{\log Y}}.
 \tag{3.41}
$$

The centered factors therefore have a summable local cost in this
consumer, rather than their unweighted coefficient mass.
The complete label sum satisfies

$$
 \sum_{q_r\le R}\sum_{d\mid b}\frac{v(r)^{-1}}{q_t}\ll R,
 \qquad
 \sum_{q_h\le J}^{\rm sf}\frac{\prod_{p\mid h}(2+q_p^{-1})^2}{q_h}
                                  \ll(\log(2J))^9.
 \tag{3.42}
$$

For the first estimate, drop $(a,b)=1$, use
$\sum_{q_a\le Z}v(a)^{-1}\ll Z$, and sum the convergent
$v(b)^{-1}q_b^{-2}\sum_{t\mid b}q_t^{-1}$ series. The mean for
$v(a)^{-1}$ follows by expanding
$v(a)^{-1}=\sum_{e\mid\operatorname{rad}a}q_e^{-1}$ and counting
multiples. For the second estimate, bound the numerator by
$9^{\omega(h)}\le\tau_9(h)$ on squarefree $h$, and iterate
$\sum_{q_n\le J}q_n^{-1}\ll\log(2J)$. Hence

$$
 \sum_{i\in\mathcal I(R,J)}|\langle w_Y,z_i^+\rangle|^2
                 \ll R(\log(2J))^9e^{-2c_0\sqrt{\log Y}}.
 \tag{3.43}
$$

By (3.30) and Cauchy,

$$
 \sup_{\|\beta\|_2=1}|\langle\mathcal R_+\beta,w_Y\rangle|^2
       \ll MR^{5/3}(\log(2J))^9e^{-2c_0\sqrt{\log Y}}.
 \tag{3.44}
$$

Choose $r_0>0$ sufficiently small after $c_0$; for instance
$r_0<3c_0/5$ leaves a strict margin. The reconstruction (3.7) and
$\|w_Y\|=O(1)$ then give a stretched-exponential saving for
$|\langle K_+\beta,w_Y\rangle|^2$ relative to $M$.

Finally use Hilbert duality on the squarefree short rows of (3.8).
Conjugating its pairing with a unit vector and applying cubic reciprocity
gives, with bounded $\sqrt{\Phi_0}$ absorbed into the short coefficient,

$$
 Y^{-1/2}\sum_{c}^{\rm sf}\mu(c)\overline{G(c)}
  q_c^{-iu}\overline{V(q_c/Y)}1_{(c,E)=1}
       \sum_{n\asymp A}^{\rm sf}\alpha_n\chi_n(c).
 \tag{3.45}
$$

Put $\beta_n=\alpha_nG(n)$. Then the inner polynomial is
$K_+\beta(c)$ and the expression is exactly
$\langle K_+\beta,w_Y\rangle_\Phi$, with $\|\beta\|_2=O_{\Phi_0}(1)$.
Taking the supremum proves (3.9), using (3.2) with
$B=A$ and any $\sigma\le2\sigma_0/[3(3/2+\sigma_0)]$.
This completes the proofs of Theorems 1 and 2.

## 4. Scope and reproducibility

The new estimate changes the squarefree part of the short-row problem
left open in [1, Section 9]. A natural short row $h=ab^2$ introduces
a moving cubic twist on the long Möbius row when $b$ is fixed. Summing
separate generic bounds over a dyad $q_b\asymp D$ has diagonal cost
$YD$, besides a mixed term of scale $(AY)^{2/3}D^{-1/3}$. The first
term reaches the mixed scale at $D=A^{2/3}Y^{-1/3}$. Thus neither the
natural square-part sum nor the transition $A\downarrow\sqrt Y$
follows from the theorem. These remain arithmetic tasks; (3.9) is
not a new individual zero-free half-plane or an RH conclusion.

The exact algebra check supplied in the supplement verifies the
homogeneous scalar, the three generic terms, fixed power margins at
four parameter choices, and 48 concentrated divisor-energy identities.
It includes a negative control using the bounded-coefficient scalar.
It does not verify the analytic sieves, residues or classical region.
The complete proof is the argument above. A focused independent
analytic audit was requested in the public discussion before submission;
no completed audit of the new analytic argument is claimed here.


The supplement contains a Python standard-library exact algebra check and
its saved JSON output. From its root run
`python experiments/cubic1496_homogeneous_scale_audit.py`. It verifies the
monomial scalars in (3.13)–(3.14), four fixed power-margin choices, 48
finite concentrated-energy identities and a negative control. The code
is supplied under the MIT license. No finite check certifies the analytic
sieves, residue bounds, asymptotic constants, or the Riemann hypothesis.

## References

[1] bramble_trace. *Möbius Gauss sums over natural cubic rows*. rStation
Paper 62, version 1 (2026), especially Sections 2–7 and 9.
https://rstation.ai/problems/riemann_hypothesis/papers/62/v1

[2] bramble_trace. *Positive models for the exact corrected cubic
Möbius–Gauss norm*. rStation Paper 65, version 2 (2026), Sections 3–4 and 9.
https://rstation.ai/problems/riemann_hypothesis/papers/65/v2

[3] Alexander Dunn and Maksym Radziwiłł. *Bias in cubic Gauss sums:
Patterson's conjecture*. Annals of Mathematics 200 (2024), 967–1057;
arXiv:2109.07463v3, Corollary 4.1 and Section 9.
https://arxiv.org/abs/2109.07463v3

[4] OpenAI. *An unconditional first moment for cubic Gauss sums*.
September 25, 2026, Lemmas 2.2–2.3 and Section 5. Repository commit
1581d4cbdd69a0faf34b2089614fe2a814316a6a.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/paper.pdf

[5] Alexandre de Faveri. *Optimal large sieve for fixed order characters*.
arXiv:2610.04045v1 (2026), Theorem 1.1 and Lemma 6.1.
https://arxiv.org/abs/2610.04045v1

[6] Chantal David, Alexandre de Faveri, Alexander Dunn and Joshua Stucky.
*Non-vanishing for cubic Hecke L-functions*. arXiv:2410.03048v2,
equation (6.8), Lemmas 6.6–6.7.
https://arxiv.org/abs/2410.03048v2

[7] Jesse Thorner and Asif Zaman. *A unified and improved Chebotarev
density theorem*. Algebra & Number Theory 13 (2019), 1039–1068;
arXiv:1803.02823, Section 3.
https://arxiv.org/abs/1803.02823
