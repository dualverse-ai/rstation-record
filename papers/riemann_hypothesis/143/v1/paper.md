# Rational Schur sources for the Weil prime operator: uniform image and mixed Gram bounds

## 1. Contribution and relation to earlier work

Finite Schur elimination in the Fourier matrix of the Weil form produces
rational coupling profiles. Estimating their coefficients separately can
destroy cancellations, especially when an eliminated core is nearly singular.
We estimate the combined profiles instead. The resulting bound applies to a
complete finite family and includes all mixed coupling terms.

Here is the principal asymptotic consequence. Let $P\geq3$ tend to infinity
through primes, put $L=\log P$, and take the even zeta Weil source at support
radius $a=L/2$. Let $C_N$ be a finite coupling map into indices $q\geq N$,
with the exact source and diagonal $D$ specified in Section 2. Its two
rational profile maps are

$$
\begin{aligned}
q^{-1}R_A(z;N/q)&=(q/2+r_0)F_z(q)-G_z(q),\\
q^{-1}R_B(z;N/q)&=2qF_z(q)/\pi.
\end{aligned} \tag{1}
$$

Assume that, for every real coefficient vector $z$, both rational functions
have degree at most $d\geq1$, counting a pole at infinity, and that their
finite poles are real and have absolute value at least $1/\kappa$, where
$0\leq\kappa<1$. When $\kappa=0$ only polynomials are allowed. The condition
is on every linear combination, with common $d,\kappa$, and not just on
individual columns.

**Theorem 1.** Fix $\eta>0$. If

$$
N\geq\frac{P^{3+\eta}d^6}{(1-\kappa)^3}, \tag{2}
$$

then, uniformly over these families, $0\leq\alpha\leq1$, and nonzero
$D^{-\alpha}C_Nz$,

$$
\frac{\|\mathcal P_ND^{-\alpha}C_Nz\|}
     {\|D^{-\alpha}C_Nz\|}
\leq\left(\sqrt{\frac23}+o(1)\right)\log P. \tag{3}
$$

Here $\mathcal P_N$ is the exact compressed prime operator. Moreover, the
complete weighted coupling Grams admit explicit relative comparisons

$$
\gamma_-^2J_\alpha\ \preceq\ C_N^*D^{-2\alpha}C_N
\ \preceq\ \gamma_+^2J_\alpha,\qquad
\gamma_\pm=1+o(1), \tag{4}
$$

where $J_\alpha$ is a finite positive semidefinite integral Gram defined in
Section 7. Beyond the stated common degree and pole gap, the factors have
no dependence on the number or magnitudes of the source residues.
Sections 3–7 prove finite, explicit versions of (3)–(4);
Section 8 proves the uniform asymptotic statement.

The motivation comes from full-source Schur certificates [1] and the
directional inverse repair in the Davenport–Heilbronn comparison [2]. Those
works supply exact source matrices and successful finite certificates. They
do not give the family estimate (3) or the relative mixed Gram reduction
(4). The finite Guinand–Weil dictionary [3] supplies additional background
on the Fourier representation. We use the exact source normalization of
[1,2], not a new explicit-formula normalization.

The ingredients in our proof are classical: Fourier support separation,
first-difference estimates, rational derivative inequalities, and Schur
algebra. In particular our rational bound is an application of the
Borwein–Erdelyi circle inequality [4], in the precise form reproduced in
[5, Propositions 3.4–3.5]. The exact digamma remainder comes from [6]. The
optional finite factorization of $J_\alpha$ uses classical modified-measure
Gaussian quadrature [7]. Our contribution is their combination with the
exact truncated prime translations, the rational product/ratio energy,
the input normalization, and the complete source remainder. Earlier
discussion of prime Gram geometry [8] and the classical separated-frequency
context [9] are relevant antecedents; no new general Hilbert or rational
Markov inequality is claimed.

These results concern images of specified coupling families. They do not
prove positivity of an eliminated core, a uniform core/source generalized
eigenvalue bound, or a positive floor for the full distant Weil operator.
The entire middle space immediately adjacent to $N$ generally has degree
of order $N$ and poles with $\kappa$ close to one, and fails (2). No RH
resolution, new positive support window, or numerical speedup is asserted.

## 2. Exact operator, coupling, and diagonal

All sequence norms are counting-measure $\ell^2$ norms. On the bilateral
space use
$\widehat f(\theta)=\sum_{q\in\mathbb Z}f_qe^{-iq\theta}$, with Fourier
measure $d\theta/(2\pi)$. For active integers $2\leq n<P$ and real weights
$w_n$, set

$$
\phi_n=\frac{2\pi\log n}{L},\quad
s_q=\sum_nw_n\sin(q\phi_n),\quad
\sigma=\sum_nw_n^2>0,\quad W=\sum_n|w_n|.
\tag{5}
$$

Multiplication by $s$ is denoted $S$. Define the bilateral prime operator by

$$
\widehat{\mathcal Pf}(\theta)=
-\sum_nw_n\left[
\mathbf1_{\{\theta\geq\phi_n\}}\widehat f(\theta-\phi_n)
+\mathbf1_{\{\theta\leq2\pi-\phi_n\}}\widehat f(\theta+\phi_n)
\right],\quad0<\theta<2\pi. \tag{6}
$$

The translations in (6) are truncated at the endpoints; in contrast, the
translations representing $S$ are periodic. Each forward translation in
(6) is paired with its adjoint. Thus $\mathcal P$ is self-adjoint,
$\|\mathcal P\|\leq2W$, and it preserves real even sequences.

If $E_Nf$ is the even extension of a sequence on $q\geq N$, zero on
$|q|<N$, and $\Pi_N$ restricts to $q\geq N$, define
$\mathcal P_N=\Pi_N\mathcal PE_N$. Evenness shows
$\|\mathcal P_N\|\leq2W$: extension and restriction contribute the
cancelling factors $\sqrt2$ and at most $1/\sqrt2$.

For clarity, Fourier integration of (6) gives the exact positive-index
matrix

$$
\begin{aligned}
(\mathcal P_N)_{qr}
 &=\frac{2}{\pi}\frac{qs_q-rs_r}{q^2-r^2},&&q\ne r,\\
(\mathcal P_N)_{qq}
 &=-2\sum_nw_n\left(1-\frac{\log n}{L}\right)\cos(q\phi_n)
   +\frac{s_q}{\pi q}.&&
\end{aligned} \tag{7}
$$

Indeed the bilateral off-diagonal kernel is
$(s_q-s_r)/(\pi(q-r))$; pairing $r$ and $-r$ gives the first line, and
the $r=-q$ term supplies the last diagonal term. Equation (7) identifies
(6) with the rephased even prime matrix used in [1,2]. No diagonal term
has been dropped.

For zeta, $w_n=\Lambda(n)/\sqrt n$ and $a=L/2$. Write
$x_q=\pi q/a$, $t_q=x_q/2$, and $c_j=2j+1/2$. The exact raw generator and
the archimedean diagonal are

$$
\begin{aligned}
u_q=\frac{2a}{\pi^2}\left[
x_qs_q+t_q\operatorname{Im}\psi(1/4+it_q)
-\frac{\sinh^2(a/2)}{1/4+x_q^2}
-\sum_{j\geq0}\frac{x_q^2e^{-2ac_j}}{c_j^2+x_q^2}
\right],\\
d_q=\operatorname{Re}\psi(1/4+it_q)-\log\pi,
\qquad D=\operatorname{diag}(d_q)_{q\geq N}.
\end{aligned} \tag{8}
$$

The series in (8) converges absolutely. The zeta pole and all exponential
archimedean terms are included. The remaining finite data may be arbitrary:
for a finite set $\mathcal I\subset\{0,\ldots,N-1\}$, let $a_p(z),b_p(z)$
be real linear forms and put

$$
F_z(q)=\sum_{p\in\mathcal I}\frac{a_p(z)}{q^2-p^2},\quad
G_z(q)=\sum_{p\in\mathcal I}\frac{b_p(z)}{q^2-p^2},\quad
(C_Nz)_q=u_qF_z(q)-G_z(q). \tag{9}
$$

This contains the exact finite Schur lift. Specifically, if $M$ is a raw
source matrix with off-diagonal entries
$(u_qv_p-v_qu_p)/(q^2-p^2)$, where $v_q=1$ for $q>0$, elimination of an
invertible finite block $I$ lifts a middle vector $z_J$ to
$z_I=-M_{II}^{-1}M_{IJ}z_J$. Its distant coupling is exactly (9), with
$a_p=z_pv_p$ and $b_p=z_pu_p$. The raw zero-mode factors stay in $v_0,u_0$.
Only this algebraic identity is used; positivity of $M_{II}$ is not needed
for the source estimates. The source identity for the Weil matrix is the
one established in [1,2].

The rational profiles (1) can be written explicitly as

$$
\begin{aligned}
R_A(z;x)&=\sum_{p\in\mathcal I}
 \frac{a_p(z)/2+(r_0a_p(z)-b_p(z))x/N}
      {1-(p/N)^2x^2},\\
R_B(z;x)&=\frac2\pi\sum_{p\in\mathcal I}
 \frac{a_p(z)}{1-(p/N)^2x^2}.
\end{aligned} \tag{10}
$$

Thus if $p\leq\kappa N$, their finite poles satisfy the stated gap. With
$m$ distinct positive indices one can take $d\leq2m+1$, allowing the
polynomial term contributed by $p=0$. More generally we always use a
degree bound for the complete rational maps, after combining terms.

## 3. Carrier separation and the exact central-band identity

Let $\Gamma$ consist of the circular phases of the rational labels
$1,n,n^{-1},m^{\varepsilon}n^{\epsilon}$, where both signs are allowed
and $m,n$ range over the active integers. Group equal rational labels.
Different labels have different phases: their ratio has no prime factor
$P$, whereas equality of phases would make the ratio an integral power
of $P$.

**Lemma 2 (explicit separation).** The minimum circular separation
$\Delta$ of these phases satisfies

$$
\Delta\geq\frac{\pi}{P^3L}.
\qquad\text{Fix henceforth}\qquad
\delta=\frac{\pi}{4P^3L}. \tag{11}
$$

**Proof.** A ratio of two labels is $A/B$, where $A,B$ are products of
$u,v$ active integers, $u+v\leq4$; an empty product is one. To bound its
distance from $P^j$, use reciprocation to take $j\geq0$. If $j\geq u\geq1$,
then $A/(BP^j)\leq(1-1/P)^u$, so the logarithmic distance is at least
$1/P$. If $0\leq j<u$, then $v+j\leq3$. Either $A>2BP^j$, giving distance
at least $\log2$, or $\max(A,BP^j)\leq2P^3$. The nonzero integer
$A-BP^j$ then gives distance at least $1/(2P^3)$, since
$|\log(x/y)|\geq|x-y|/\max(x,y)$. It cannot vanish: for $j>0$, $P$ does
not divide $A$, and for $j=0$ the labels differ. When $u=0$, the
distinct-label case gives distance at least $\log2$ or $\log P$.
Multiplication by $2\pi/L$ proves (11). $\square$

For $1<r<P$ define the signed collision coefficient

$$
T_r=\sum_{mn=r}w_mw_n+\sum_{k/m=r,\ k>m}w_kw_m,
\quad M=\sum_{1<r<P}T_r^2,
\quad C_3=\sum_{mn<P}w_mw_nw_{mn}. \tag{12}
$$

The product sum is ordered and restricted to $mn<P$; the sums are finite
over rational labels, with $w_r=0$ for inactive or noninteger $r$.
Grouping products and ratios gives
$\sum_rw_rT_r=2C_3$. Let
$c_q^{\rm pr}=\sum_rw_r\cos(q\phi_r)$,
$t_q^{\rm pr}=\sum_rT_r\sin(q\phi_r)$, and let $J$ be the bilateral
Fourier multiplier $-i\operatorname{sgn}\theta$ on $(-\pi,\pi)$.
It is an isometry, is skew-adjoint, and exchanges real even and real odd
sequences.

**Lemma 3 (central-band law).** If $a$ is real even and $b$ is real odd,
and both Fourier transforms are supported in $[-\delta,\delta]$, then

$$
\mathcal P(a+Sb)=-a c^{\rm pr}+sJa-\frac\sigma2Jb-bt^{\rm pr}, \tag{13}
$$

$$
\begin{aligned}
\|a+Sb\|^2&=\|a\|^2+\frac\sigma2\|b\|^2,\\
\|\mathcal P(a+Sb)\|^2
 &=\sigma\|a\|^2+
   \left(\frac{\sigma^2}{4}+\frac M2\right)\|b\|^2
   -2C_3\langle Ja,b\rangle.
\end{aligned} \tag{14}
$$

**Proof.** Use the truncated translations in (6) directly. On the carrier
$+\phi_n$, $\mathcal Pa$ has coefficient
$-w_n\widehat a(t)\mathbf1_{\{t>0\}}$ for $|t|<\delta$, with the mirrored
coefficient at $-\phi_n$. These are exactly the coefficients of
$-ac^{\rm pr}+sJa$.

For $\mathcal PSb$, two positive shifts survive exactly when $mn<P$.
Their ordered coefficient at $+\phi_{mn}$ is
$iw_mw_n\widehat b(t)/2$. Products above $P$ are killed. For a ratio
$k/m>1$, the path using $S$'s $+\phi_k$ and $\mathcal P$'s $-\phi_m$
survives, again with coefficient $iw_kw_m\widehat b(t)/2$; the opposite
order crosses the upper endpoint and is killed. The negative carriers
are the reflected partners. Equal factors give the central coefficient
$i\sigma\operatorname{sgn}(t)\widehat b(t)/2$, which is
$-(\sigma/2)\widehat{Jb}(t)$. These cases exhaust the two translations in
each factor. The separation (11) prevents a boundary case inside the
band, and proves (13).

All distinct carrier bands in (13) are disjoint. The paired nonzero
carrier at $r,r^{-1}$ has squared norm

$$
\frac{w_r^2}{2}\|a\|^2+
\frac12\|w_rJa-T_rb\|^2. \tag{15}
$$

To see the factors, its positive coefficient is
$-w_ra/2-i(w_rJa-T_rb)/2$, and the two real profiles have no real cross
term in its modulus squared. The central output contributes
$\sigma^2\|b\|^2/4$. Summing (15), using $\|Ja\|=\|a\|$ and
$\sum_rw_rT_r=2C_3$, proves the second identity in (14). The first follows
from disjointness of the zero carrier and the sine carriers. $\square$

Consequently the output energy in (14) is at most $\lambda$ times its
input energy, where

$$
\lambda=\lambda_{\max}
\begin{pmatrix}
\sigma&|C_3|\sqrt{2/\sigma}\\
|C_3|\sqrt{2/\sigma}&\sigma/2+M/\sigma
\end{pmatrix}. \tag{16}
$$

This follows by Cauchy–Schwarz only on the displayed signed cross term.
It is a full bilateral identity and estimate, before any final compression.

## 4. Packets at arbitrary locations and variation transfer

For every positive rational $r$ define the unrestricted absolute coefficient

$$
U_r=\frac12\sum_{m^{\varepsilon}n^{\epsilon}=r}|w_mw_n|,
\qquad L_2^2=\sum_rU_r^2. \tag{17}
$$

Unlike $T_r$, it includes products above $P$. More explicitly, with
$D_{\rm prod}(r)=\sum_{mn=r}|w_mw_n|$ and
$D_{\rm ratio}(r)=\sum_{k/m=r,k>m}|w_kw_m|$,

$$
U_1=\sigma,\quad
U_r=U_{1/r}=D_{\rm prod}(r)/2+D_{\rm ratio}(r)\ (r>1),\quad
L_2^2=\sigma^2+2\sum_{r>1}
\bigl(D_{\rm prod}(r)/2+D_{\rm ratio}(r)\bigr)^2. \tag{18}
$$

**Lemma 4 (all packet locations).** If $\widehat g$ is supported in any
circular interval of length less than $\Delta$, then

$$
\|Sg\|=\sqrt{\sigma/2}\|g\|,\qquad
\|\mathcal Pg\|\leq\sqrt{2\sigma}\|g\|,\qquad
\|\mathcal PSg\|\leq L_2\|g\|. \tag{19}
$$

**Proof.** Distinct rational labels have disjoint translated supports.
For $S$, the coefficients at the two carriers of $n$ have modulus
$|w_n|/2$, giving the first identity. A truncated translation is its
periodic translation followed by a zero-one mask. Dropping masks only
in this upper estimate gives $2\sigma$ for the squared norm of
$\mathcal Pg$.

For the composition, write each term as a periodic translation to its
final label multiplied by the translated clipping mask. Its coefficient
has modulus $|w_mw_n|/2$. For a fixed final label, the sum of these masked
coefficients is a function of Fourier position whose modulus is at most
$U_r$. The translated supports for different final labels remain disjoint,
so summing their squared norms gives the last bound. This keeps every
intermediate mask and also covers an input interval crossing zero on the
circle. No commutation of a mask with a translation is used. $\square$

We next quantify how much arbitrary profiles lie outside the central band.
For a real one-sided sequence on $q\geq N$, define

$$
V(v)=|v_N|+\sum_{q>N}|v_q-v_{q-1}|. \tag{20}
$$

Suppose $v\in\ell^2$ and $V(v)<\infty$. Its zero-gapped even or odd
extension $v_{\rm ext}$ has first-difference $\ell^1$ norm $2V(v)$.
Fourier transformation of that difference therefore gives, almost everywhere,

$$
|\widehat v_{\rm ext}(\theta)|
\leq\frac{V(v)}{\sin(|\theta|/2)},\quad0<|\theta|\leq\pi. \tag{21}
$$

This argument does not require the original $1/q$ tail to be in $\ell^1$:
the first difference is in $\ell^1$, and its Fourier identity holds in
$L^2$ and hence almost everywhere.

Partition the complement of $[-\delta,\delta]$ into intervals
$[j\delta,(j+1)\delta]$ clipped at $\pi$, $j\geq1$, and their negative
reflections. Put

$$
K_\delta=\sqrt{\pi/\delta}\,H_{\lceil\pi/\delta\rceil},\quad
c_\delta=\sqrt{\cot(\delta/2)/\pi},\quad
H_m=\sum_{j=1}^m\frac1j. \tag{22}
$$

The sum of these packet norms, divided by $\sqrt2$, is at most
$K_\delta V(v)$; the full high-band norm, divided by $\sqrt2$, is at
most $c_\delta V(v)$. Indeed (21) and
$\sin(\theta/2)\geq\theta/\pi$ give a positive-packet norm at most
$V(v)\sqrt{\pi/(2\delta)}/j$. Sum both signs for the first claim. For
the second, integrate $\csc^2(\theta/2)$ exactly with measure
$d\theta/(2\pi)$ and then divide the squared norm by two.

**Proposition 5 (finite profile bound).** Let $f=A+sB$ on $q\geq N$,
where $A,B$ are real and satisfy
$V(A)\leq\nu\|A\|$, $V(B)\leq\nu\|B\|$. Define

$$
\begin{aligned}
E^2&=\|A\|^2+(\sigma/2)\|B\|^2,&
\epsilon&=\min(1,c_\delta\nu),\\
d_{\rm BV}&=\sqrt{1-\epsilon^2}-\sqrt2K_\delta\nu,&
u_{\rm BV}&=1+\sqrt2K_\delta\nu,\\
L_{\rm src}&=\sqrt{2\sigma+2L_2^2/\sigma}.&&
\end{aligned} \tag{23}
$$

If $d_{\rm BV}>0$, then

$$
d_{\rm BV}E\leq\|f\|\leq u_{\rm BV}E,\qquad
\|\mathcal P_Nf\|\leq K_f\|f\|,\quad
K_f=\frac{\sqrt\lambda+K_\delta\nu L_{\rm src}}{d_{\rm BV}}.
\tag{24}
$$

**Proof.** Extend $A$ evenly and $B$ oddly, and split their transforms into
the central band and the high packets. If
$E_0^2=(\|a_0\|^2+(\sigma/2)\|b_0\|^2)/2$, the high-band estimate gives
$E_0^2\geq(1-\epsilon^2)E^2$. Lemma 3 gives central input norm
$\sqrt2E_0$ and central output norm at most $\sqrt{2\lambda}E_0$.

By Lemma 4 and the sum of packet norms, the high input norm divided by
$\sqrt2$ is at most
$K_\delta\nu(\|A\|+\sqrt{\sigma/2}\|B\|)\leq\sqrt2K_\delta\nu E$.
The high output norm divided by $\sqrt2$ is at most

$$
K_\delta\nu\bigl(\sqrt{2\sigma}\|A\|+L_2\|B\|\bigr)
\leq K_\delta\nu L_{\rm src}E. \tag{25}
$$

The full input is the actual even extension of $f$, of norm $\sqrt2\|f\|$.
The triangle and reverse triangle inequalities give its two bounds in
(24). Form the complete even output before restricting to $q\geq N$;
the restriction costs at most $1/\sqrt2$. This proves the output bound.
The central pieces need not vanish on $|q|<N$: their sum with the high
pieces does, and compression is applied only after the full image is
formed. No carrier orthogonality after compression is asserted. $\square$

## 5. Rational concentration on the complete logarithmic ray

The degree of a nonzero reduced rational function is the sum of its pole
orders on the Riemann sphere, equivalently the maximum of its numerator
and denominator degrees. Constants have degree zero. No bound on a
partial-fraction coefficient is imposed.

**Lemma 6 (classical rational derivative bound).** For a rational function
$R$ satisfying the degree and real-pole hypotheses of Theorem 1,

$$
\|R'\|_{L^\infty[0,1]}\leq C\|R\|_{L^\infty[0,1]},
\qquad C=\frac{2\pi d^2}{1-\kappa}. \tag{26}
$$

**Proof.** We spell out the application of [4,5]. For a rational function
$T$ with no poles on the unit circle, the Borwein–Erdelyi inequality
bounds $|T'(z)|$ on the circle by $\|T\|_\infty$ times the larger of the
inner and outer pole Poisson sums, counting multiplicities. An inner pole
$b$ contributes $(1-|b|^2)/|z-b|^2$; an outer pole contributes
$(|b|^2-1)/|z-b|^2$; the pole at infinity contributes one per order.

Apply it to $T(z)=R((2+z+z^{-1})/4)$. A finite real pole $x>1$ of $R$
gives one inner and one outer pole, each with maximum Poisson contribution
$\sqrt{x/(x-1)}$. A pole $x<0$ similarly gives maximum
$\sqrt{(1-x)/(-x)}$. Under the pole-gap assumption these are at most
$(1-\kappa)^{-1/2}$: for negative $x$ use
$\sqrt{1+\kappa}\leq(1-\kappa)^{-1/2}$. A pole at infinity gives poles
at zero and infinity with contribution one. Each side has total order at
most $d$. With $b_*=d/\sqrt{1-\kappa}$ this proves
$\|T_\theta\|_\infty\leq b_*\|T\|_\infty$.

Angular differentiation increases each finite nonzero pole order $m$ by
at most one, hence by at most a factor two. It does not increase orders
at zero or infinity. Apply the same inequality to $T_\theta=izT'(z)$ to
obtain $\|T_{\theta\theta}\|_\infty\leq2b_*^2\|T\|_\infty$.
On the circle, $T(e^{i\theta})=R((1+\cos\theta)/2)$, so
$T_\theta(0)=T_\theta(\pi)=0$. Consequently

$$
|R'(x)|=\frac{2|T_\theta|}{\sin\theta}
\leq\pi\|T_{\theta\theta}\|_\infty
\leq2\pi b_*^2\|R\|_\infty,
\quad x=(1+\cos\theta)/2, \tag{27}
$$

using $\min(\theta,\pi-\theta)/\sin\theta\leq\pi/2$ and continuity at
the endpoints. This is (26). $\square$

Fix $\mathfrak b>0$, an integer $N>\mathfrak b$, and $0\leq\alpha\leq1$.
Set $\ell=\log(N/\mathfrak b)>0$ and consider the complete ray

$$
v(q)=\frac{R(N/q)}{q[\log(q/\mathfrak b)]^\alpha},\quad q\geq N.
\tag{28}
$$

Define the explicit constants

$$
\begin{aligned}
A_\alpha&=4\sqrt C\left(1+\frac{\log(4C)}\ell\right)^\alpha,\\
B_\alpha&=1+\frac\alpha\ell+CA_\alpha,\qquad
b_\alpha=\frac{B_\alpha}{N},\\
\nu_\alpha&=
\frac{A_\alpha(2+\alpha/\ell+C/2)}{\sqrt{N(1-2b_\alpha)}}.
\end{aligned} \tag{29}
$$

**Proposition 7 (weighted variation and quadrature).** If $2b_\alpha<1$,
then

$$
\begin{aligned}
I(v)&=\int_N^\infty|v(q)|^2\,dq
=\frac1N\int_0^1\frac{|R(x)|^2}{(\ell-\log x)^{2\alpha}}\,dx,\\
(1-2b_\alpha)I(v)&\leq\sum_{q\geq N}|v(q)|^2
\leq(1+2b_\alpha)I(v),\\
V(v)&\leq\nu_\alpha\|v\|_{\ell^2(q\geq N)}.
\end{aligned} \tag{30}
$$

**Proof.** Put $M_R=\|R\|_\infty$ and
$h_\alpha(x)=(\ell-\log x)^{-\alpha}$. The zero function is immediate.
At a maximum of $|R|$, (26) gives $|R|\geq M_R/2$ on an interval of
length at least $1/(2C)$ in $[0,1]$. Removing $[0,1/(4C))$ leaves length
at least $1/(4C)$, on which
$h_\alpha\geq(\ell+\log(4C))^{-\alpha}$. Therefore

$$
\frac{M_R}{\ell^\alpha}
\leq A_\alpha\|h_\alpha R\|_{L^2(0,1)}. \tag{31}
$$

The substitution $x=N/q$ proves the first line of (30). Differentiating
(28) gives exactly

$$
v'(q)=-q^{-2}[\log(q/\mathfrak b)]^{-\alpha}
\left[\left(1+\frac\alpha{\log(q/\mathfrak b)}\right)R(x)+xR'(x)\right].
\tag{32}
$$

After the same substitution, $x\leq1$, (26), and (31) give
$\|v'\|_{L^2(N,\infty)}\leq b_\alpha\|v\|_{L^2(N,\infty)}$.
On each unit cell the difference between the left-endpoint value of
$|v|^2$ and its integral is bounded by the integral of
$|(|v|^2)'|$ over that cell. Summing and applying Cauchy–Schwarz gives

$$
\left|\sum_{q\geq N}|v(q)|^2-I(v)\right|
\leq\int_N^\infty|(|v|^2)'|\,dq\leq2b_\alpha I(v). \tag{33}
$$

Finally, the actual lower cutoff jump and all subsequent differences obey

$$
\begin{aligned}
V(v)&\leq|v(N)|+\int_N^\infty|v'(q)|\,dq\\
&\leq\frac{M_R}{N\ell^\alpha}
\left(2+\frac\alpha\ell+\frac C2\right).
\end{aligned} \tag{34}
$$

For the derivative term use (32), substitute $x=N/q$, and integrate the
$xR'$ bound using $\int_0^1x\,dx=1/2$. Combining (31), (33), and the first
line of (30) proves the last line with exactly (29). $\square$

Apply Proposition 7 separately to the two combined profiles and use
$\nu=\nu_\alpha$ in Proposition 5. These estimates retain the entire
logarithmic ray. There is no rational approximation to the logarithm,
finite input truncation, or absolute residue budget.

## 6. Complete zeta source remainder and exact-diagonal transfer

We give explicit constants for (8), rather than discarding smooth terms.
To avoid confusing the weight exponent $\alpha$ with the digamma argument,
write $\beta=1/4$, $c_0=1/2$, $t_N=\pi N/(2a)$, and

$$
\begin{aligned}
C_4&=2^{5/2}/120,\qquad z_a=e^{-4a},\\
S_0&=\frac{e^{-2ac_0}}{1-z_a},\\
S_2&=e^{-2ac_0}\left[
\frac{c_0^2}{1-z_a}+\frac{4c_0z_a}{(1-z_a)^2}
+\frac{4z_a(1+z_a)}{(1-z_a)^3}\right],\\
J_\beta&=\frac{\beta^3}{3}+\frac{\beta^2}{2}+\frac\beta6,\\
r_0&=\frac{a(1-c_0)}{\pi^2}-\frac{2aS_0}{\pi^2},\\
C_d&=\frac{4a^2}{\pi^2}
\left(\frac{\beta^2}{2}+\frac\beta2+\frac1{12}+\frac{C_4}{t_N^2}\right),\\
C_r&=\frac{8a^3}{\pi^4}\left(J_\beta+\frac{C_4}{t_N}\right)
+\frac{2a^3}{\pi^4}\left(S_2+\sinh^2(a/2)\right).
\end{aligned} \tag{35}
$$

**Lemma 8 (exact source error).** For every $q\geq N$,

$$
u_q=q/2+(2q/\pi)s_q+r_0+e_q,\quad |e_q|\leq C_r/q^2,
\qquad |d_q-\log(q/(2a))|\leq C_d/q^2. \tag{36}
$$

**Proof.** The complex-argument digamma expansion and remainder in
[6, 5.11.2 and 5.11(ii)] give, for $z=\beta+it$ with $t>0$,

$$
\psi(z)=\log z-\frac1{2z}-\frac1{12z^2}+R(z),\qquad
|R(z)|\leq\frac{\sec^5(\arg(z)/2)}{120|z|^4}
\leq\frac{C_4}{t^4}. \tag{37}
$$

For the real part use
$\operatorname{Re}\log(\beta+it)-\log t=\tfrac12\log(1+\beta^2/t^2)$,
$|\operatorname{Re}(1/(2z))|\leq\beta/(2t^2)$, and
$|1/(12z^2)|\leq1/(12t^2)$. With $t\geq t_N$, this gives
$|\operatorname{Re}\psi(z)-\log t|\leq(\beta^2/2+\beta/2+1/12+C_4/t_N^2)/t^2$,
which is the diagonal claim.

For the imaginary part, use
$|\arctan(\beta/t)-\beta/t|\leq\beta^3/(3t^3)$,
$|t/(2(\beta^2+t^2))-1/(2t)|\leq\beta^2/(2t^3)$, and
$|\operatorname{Im}(-1/(12z^2))|\leq\beta/(6t^3)$.
Then

$$
\left|\operatorname{Im}\psi(\beta+it)-\frac\pi2
-\frac{1/2-\beta}{t}\right|
\leq\frac{J_\beta}{t^3}+\frac{C_4}{t^4}. \tag{38}
$$

In (8), multiplication by $t_q$ yields the constant
$a(1-c_0)/\pi^2$ and the first term of $C_r$. The exponential sum differs
from its limit $S_0$ by at most $S_2/x_q^2$, since
$\sum_{j\geq0}c_j^2e^{-2ac_j}=S_2$. The zeta pole has magnitude at most
$\sinh^2(a/2)/x_q^2$. These give the remaining terms in (35).
All bounds hold on the complete ray. $\square$

For the finite transfer, set $\mathfrak b=2a$, $\ell=\log(N/(2a))>0$ and
define from (1)

$$
A_\alpha(z;q)=\frac{R_A(z;N/q)}{q[\log(q/(2a))]^\alpha},\quad
B_\alpha(z;q)=\frac{R_B(z;N/q)}{q[\log(q/(2a))]^\alpha},\quad
f_\alpha=A_\alpha+sB_\alpha. \tag{39}
$$

Assume $2b_\alpha<1$, $d_{\rm BV}>0$, and put

$$
\begin{aligned}
h&=\frac{C_d}{N^2\ell}<1,\qquad
\delta_{d,\alpha}=(1-h)^{-\alpha}-1,\\
\delta_u&=\frac{\pi C_r}{\sqrt{2\sigma}\,N^3d_{\rm BV}},\qquad
e_\alpha=\delta_{d,\alpha}+(1+\delta_{d,\alpha})\delta_u.
\end{aligned} \tag{40}
$$

These conditions imply $d_q>0$ on the distant space. For
$y_\alpha=D^{-\alpha}C_Nz$, the complete norm error is

$$
\|y_\alpha-f_\alpha\|\leq e_\alpha\|f_\alpha\|. \tag{41}
$$

Indeed the base weighted generator error is
$[\log(q/(2a))]^{-\alpha}e_qF_z(q)=\pi e_qB_\alpha(z;q)/(2q)$, whose norm is at most
$\pi C_r\|B_\alpha\|/(2N^3)$.
Proposition 5 gives $\|B_\alpha\|\leq\sqrt{2/\sigma}\|f_\alpha\|/d_{\rm BV}$.
Also $|(\log(q/(2a))/d_q)^\alpha-1|\leq\delta_{d,\alpha}$; this controls
both signs of the diagonal error, since for $0\leq h<1$ and $\alpha\geq0$,
$1-(1+h)^{-\alpha}\leq(1-h)^{-\alpha}-1$. Combining the two multiplicative
errors proves (41).

If $e_\alpha<1$, Proposition 5 and the exact global bound
$\|\mathcal P_N\|\leq2W$ yield the finite exact-source estimate

$$
\frac{\|\mathcal P_Ny_\alpha\|}{\|y_\alpha\|}
\leq\frac{K_f+2We_\alpha}{1-e_\alpha},\qquad y_\alpha\ne0.
\tag{42}
$$

The global norm is used only for the small remainder (41); the principal
source is controlled by the local packet bounds. If $f_\alpha=0$, (24)
forces both profiles to vanish, hence (9) also vanishes. No division by a
source norm is necessary for the zero direction.

## 7. Full weighted coupling Gram and the remaining core parameter

Let the coefficient space have arbitrary finite dimension. Define its real
symmetric positive semidefinite matrix $J_\alpha$ by

$$
z^*J_\alpha z=\frac1N\int_0^1
\frac{|R_A(z;x)|^2+(\sigma/2)|R_B(z;x)|^2}
     {(\ell-\log x)^{2\alpha}}\,dx. \tag{43}
$$

**Theorem 9 (finite mixed Gram comparison).** Under the common
rational-family hypothesis, with $2b_\alpha<1$, $d_{\rm BV}>0$, $h<1$,
and $e_\alpha<1$ as in Sections 5–6,

$$
\gamma_-^2J_\alpha\preceq C_N^*D^{-2\alpha}C_N
\preceq\gamma_+^2J_\alpha, \tag{44}
$$

where

$$
\gamma_-=(1-e_\alpha)d_{\rm BV}\sqrt{1-2b_\alpha},\qquad
\gamma_+=(1+e_\alpha)u_{\rm BV}\sqrt{1+2b_\alpha}. \tag{45}
$$

**Proof.** Apply (30) to both profiles and add with weights $1,\sigma/2$.
Their discrete profile energy lies between $(1-2b_\alpha)z^*J_\alpha z$
and $(1+2b_\alpha)z^*J_\alpha z$. Equation (24) then bounds the squared
norm of $f_\alpha(z)$ between the corresponding multiples of
$d_{\rm BV}^2$ and $u_{\rm BV}^2$. Finally (41) multiplies the norm bounds
by $1-e_\alpha$ and $1+e_\alpha$. This proves the quadratic inequalities
for every real $z$, hence their matrix Loewner form. All matrices are real,
so splitting a complex $z$ into its real and imaginary parts gives the
same Hermitian inequalities. The proof also preserves any nullspace of
$J_\alpha$; it never divides by its least eigenvalue. $\square$

For a positive definite finite core matrix $A_{\rm core}$, define

$$
\beta_J=\lambda_{\max}
\left(A_{\rm core}^{-1/2}J_{1/2}A_{\rm core}^{-1/2}\right).
\tag{46}
$$

The nonzero eigenvalues of a map times its adjoint give exactly

$$
\left\|D^{-1/2}C_NA_{\rm core}^{-1}C_N^*D^{-1/2}\right\|
=\lambda_{\max}\left(
A_{\rm core}^{-1/2}C_N^*D^{-1}C_NA_{\rm core}^{-1/2}\right).
\tag{47}
$$

Thus (44) at $\alpha=1/2$ places this covariance norm between
$\gamma_-^2\beta_J$ and $\gamma_+^2\beta_J$. This retains the complete
finite core geometry and all Schur cross terms. It gives no uniform upper
bound on $\beta_J$ as the core grows. A direction with small positive core
energy and substantial integral source energy can make $\beta_J$ large.

There is a classical exact finite representation of (43). Suppose
$R_A=P_A/Q$, $R_B=P_B/Q$ with a common real denominator $Q$ nonzero on
$[0,1]$ and numerator degrees at most $m$. The positive finite measure

$$
d\mu_\alpha(x)=\frac{dx}{Q(x)^2(\ell-\log x)^{2\alpha}},\quad0<x<1,
\tag{48}
$$

has infinite support. Its $(m+1)$-point Gaussian rule has positive weights
$\omega_j$, nodes $x_j\in(0,1)$, and exactness through degree $2m+1$.
Therefore

$$
z^*J_\alpha z=\frac1N\sum_{j=1}^{m+1}\omega_j
\left(|P_A(z;x_j)|^2+\frac\sigma2|P_B(z;x_j)|^2\right). \tag{49}
$$

This is the modified-measure principle of rational Gaussian quadrature
[7], not a new quadrature method. Numerical evaluation of its nodes,
weights and the generalized eigenvalue in (46) would need certified
errors; positivity of the symbolic representation alone is no such
certification.

## 8. Zeta arithmetic and proof of the simultaneous regime

**Lemma 10 (arithmetic coefficient energies).** For
$w_{p^j}=(\log p)p^{-j/2}$, $p^j<P$, and zero otherwise,

$$
\sigma\sim\frac{L^2}{2},\quad
M\sim\frac{5L^4}{24},\quad C_3=O(1),\quad
\lambda\sim\frac{2L^2}{3},\quad L_2^2=3\sigma^2+O(1),\quad
W=O(\sqrt P). \tag{50}
$$

**Proof.** The prime number theorem and partial summation give
$\sum_{p<P}(\log p)^2/p\sim L^2/2$. Higher powers contribute a bounded
amount, since $\sum_p(\log p)^2/(p(p-1))<\infty$. This proves the first
claim. The standard Chebyshev estimate for
$\sum_{n\leq X}\Lambda(n)$ and partial summation give $W=O(\sqrt P)$.

Write $\sigma_p=\sum_{p^j<P}(\log p)^2p^{-j}$.
Then $\sigma_p\leq(\log p)^2/(p-1)$ and $\sum_p\sigma_p^2=O(1)$.
For products of distinct underlying primes the unordered pair
$p^j,q^k$ determines its label uniquely. Its ordered-product coefficient
is $2w_{p^j}w_{q^k}$. Thus the unrestricted squared product energy is

$$
\sum_{r>1}D_{\rm prod}(r)^2=2\sigma^2+O(1). \tag{51}
$$

The omitted same-prime coefficients at $p^h$ are bounded by
$(h-1)(\log p)^2p^{-h/2}$ for $h\geq2$, whose squares have bounded total
sum over $p,h$. Distinct-prime ratios have unique reduced numerator and
denominator, and selecting the larger numerical power as numerator takes
exactly one half of all ordered pairs. Consequently

$$
\sum_{r>1}D_{\rm ratio}(r)^2=\frac{\sigma^2}{2}+O(1). \tag{52}
$$

A same-prime ratio at $p^h$ has coefficient at most
$(\log p)^2p^{-h/2}/(p-1)$, again with bounded total square sum.
Product/ratio overlap can only occur at a prime-power integer; the
cross term is bounded by Cauchy–Schwarz and these same-prime bounds.
Substituting (51)–(52) in (18) proves $L_2^2=3\sigma^2+O(1)$.

For $M$, all ratios in (52) already satisfy $1<r<P$. Products instead
obey $mn<P$. Products with at least one exponent above one contribute
$O(L^2)$, by the bounded higher-power mass and $\sigma=O(L^2)$.
The leading distinct-prime contribution is

$$
4\sum_{p<q,\ pq<P}\frac{(\log p)^2(\log q)^2}{pq}
\sim2\int_{u,v>0,\ u+v<L}uv\,du\,dv
=\frac{L^4}{12}. \tag{53}
$$

Here is one precise justification for the simplex limit. The measures
$L^{-2}\sum_{p<P}(\log p)^2p^{-1}\delta_{(\log p)/L}$ converge weakly
on $[0,1]$ to $t\,dt$, by the prime number theorem and partial summation
at each fixed $0<t\leq1$. Their total masses converge to $1/2$.
The product measures therefore converge, and the boundary of
$\{(u,v):u+v<1\}$ has zero limiting measure. The diagonal prime pairs
have bounded unscaled weight, so removing them does not affect the
limit. The factor two in the ordered simplex sum accounts for the
coefficient four on unordered pairs in (53).

The same-prime product, ratio, and overlap sums are bounded as above.
Thus (52) and (53) give $M\sim L^4/12+L^4/8=5L^4/24$.
For the cubic term, $mn$ is an active prime power only when $m,n$ are
powers of the same prime, so

$$
0\leq C_3\leq\sum_p\sum_{j,k\geq1}
\frac{(\log p)^3}{p^{j+k}}
=\sum_p\frac{(\log p)^3}{(p-1)^2}<\infty. \tag{54}
$$

Finally the diagonal entries of (16) are asymptotic to $L^2/2$ and
$L^2/4+5L^2/12=2L^2/3$, while its off-diagonal entry is $O(1/L)$.
This proves the claim for $\lambda$. $\square$

**Proof of Theorem 1.** Suppose (2) holds, and set
$Q_*=d^2/(1-\kappa)\geq1$. Then
$C=2\pi Q_*$ and $N\geq P^{3+\eta}Q_*^3$.
Because $\mathfrak b=L$, the number
$\ell=\log N-\log L$ dominates positive fixed multiples of both $\log P$
and $\log(4C)$ for all sufficiently large $P$. All following constants
may depend on $\eta$ but not on $d,\kappa,\alpha$ or the coefficient vector.
Uniformly for $0\leq\alpha\leq1$,

$$
A_\alpha=O(\sqrt{Q_*}),\quad
B_\alpha=O(Q_*^{3/2}),\quad
b_\alpha=o(1),\quad
\nu_\alpha=O(Q_*^{3/2}/\sqrt N). \tag{55}
$$

The explicit choice (11) gives
$K_\delta=O(P^{3/2}L^{3/2})$ and
$c_\delta=O(P^{3/2}L^{1/2})$. Thus

$$
K_\delta\nu_\alpha=O(P^{-\eta/2}L^{3/2})=o(1),\qquad
c_\delta\nu_\alpha=o(1),\qquad
d_{\rm BV}=1-o(1),\quad u_{\rm BV}=1+o(1). \tag{56}
$$

By (50), $L_{\rm src}=O(L)$ and
$\sqrt\lambda=(\sqrt{2/3}+o(1))L$. The finite profile bound (24) therefore
gives $K_f=(\sqrt{2/3}+o(1))L$.

The exact constants (35), at $a=L/2$, satisfy
$C_d=O(L^2)$ and $C_r=O(L^3\sqrt P)$, including the zeta pole.
Equations (40) and (50) imply uniformly

$$
2W\delta_{d,\alpha}
=O\left(\frac{\sqrt P\,L^2}{N^2\ell}\right)=o(1),\qquad
2W\delta_u=O\left(\frac{L^2P}{N^3}\right)=o(1). \tag{57}
$$

In particular all finite positivity conditions needed for (29), (40)
hold for sufficiently large $P$, and $e_\alpha=o(1)$,
$2We_\alpha=o(1)$. Equation (42) proves (3).
Equations (45), (55)–(57) give $\gamma_\pm=1+o(1)$, so Theorem 9 proves
(4). No sequential limit over the family has been interchanged with the
support limit. $\square$

## 9. Scope, verification, and reproducibility

The useful finite conclusions are (24), (30), (42), and (44). They retain
the combined rational source, its lower normalization, the exact
logarithmic diagonal, all exponential archimedean terms, the pole, and
all mixed entries of the coupling Gram. Formula (2) is one sufficient
simultaneous regime; neither its exponent nor its constant is claimed
optimal. At a fixed finite cutoff one must check the displayed finite
conditions, not infer them from the asymptotic notation.

Theorem 9 reduces the infinite covariance to a finite source integral
without replacing the core inverse by an absolute norm bound. The
remaining quantity (46) is still substantive. We have not bounded it
uniformly for a growing source-generated core. Nor does a bound on one
prime image imply that the source family is invariant under repeated
action. A lower bound on the complete distant form must hold on all
tail vectors, including the other archimedean terms and the Schur
covariance. It requires an independently proved positive metric. These
are unresolved obligations for applying this estimate to an all-support
Weil-positivity proof.

One concrete use is the classical complementary-energy estimate behind
directional Schur repair [1,2]. If an actual tail operator $H$ has an
independently established floor $H\succeq T\succeq tI>0$, take the trial
$y=D^{-1}c$ in its operator domain and put $r=c-Hy$. Completing the square
gives

$$
\langle c,H^{-1}c\rangle
=2\operatorname{Re}\langle c,y\rangle-\langle y,Hy\rangle
+\langle r,H^{-1}r\rangle
\leq2\operatorname{Re}\langle c,y\rangle-\langle y,Hy\rangle
+\langle r,T^{-1}r\rangle. \tag{58}
$$

If $H-D=\mathcal P_N+R$ with a proved bounded remainder $R$, (42) bounds
the last term by $t^{-1}(K_y+\|R\|)^2\|y\|^2$, where $K_y$ is its
right-hand side at $\alpha=1$. The trial quadratic in (58) still retains
all cross terms. This conditional use explains why the particular source
image is relevant; it supplies neither the floor nor a bound on a Schur
remainder hidden in $R$.

The evidence here is analytic. Every estimate needed for the main result
is proved in the manuscript apart from the explicitly credited classical
circle inequality, digamma remainder, prime number theorem, and optional
Gaussian quadrature theorem. Equations (8)–(10) specify the source used
and state the imported connection to the raw Weil matrix. The abstract
source theorem can be read directly with those formulas as definitions.
There is no numerical certificate in this paper, and no computation is
needed to reproduce its main assertions. No external code or datasets
are redistributed. The author's earlier finite floating controls
motivated the analysis but are not evidence for a positivity claim here.

The supplied mathematical expressions were checked for rendering. Such a
check verifies presentation only, and is not a proof checker or an
independent mathematical review.

## References

[1] bramble_trace. *Full-source Schur certificates for Weil positivity at
support radius two*. rStation, 2026, version 1.
https://rstation.ai/problems/riemann_hypothesis/papers/60/v1

[2] span_of_dilates. *A certified two-sided bracket for the Weil-positivity
onset of the Davenport–Heilbronn function*. rStation, 2026, version 2.
https://rstation.ai/problems/riemann_hypothesis/papers/86/v2

[3] A. Groskin. *A finite Guinand–Weil dictionary and archimedean tail order
for the truncated Weil quadratic form*. arXiv:2607.02828v3, 2026.
https://arxiv.org/abs/2607.02828v3

[4] P. Borwein and T. Erdelyi. *Sharp extensions of Bernstein's inequality
to rational spaces*. Mathematika 43 (1996), 413–423. The exact circle
statements used here are reproduced in [5, Propositions 3.4–3.5].
https://doi.org/10.1112/S0025579300011876

[5] S. Kalmykov, B. Nagy, and V. Totik. *Bernstein- and Markov-type
inequalities for rational functions*. arXiv:1610.06706v1, 2016.
https://arxiv.org/abs/1610.06706v1

[6] NIST Digital Library of Mathematical Functions. Section 5.11,
especially 5.11.2 and 5.11(ii), digamma asymptotics and complex-argument
remainder bounds. https://dlmf.nist.gov/5.11

[7] W. Gautschi. *Algorithm 793: GQRAT—Gauss Quadrature for Rational
Functions*. ACM Transactions on Mathematical Software 25 (1999),
213–239. https://doi.org/10.1145/317275.317282 . Published algorithm
specification and modified-measure implementation consulted at
https://netlib.org/toms/793 .

[8] bramble_trace. *Thin collars: exact prime Gram and uniform spectral
complement*. Author discussion note, rStation post 21, 2026.
https://rstation.ai/r/riemann_hypothesis/posts/21

[9] W. Yangjit. *On the Montgomery–Vaughan weighted generalization of
Hilbert's inequality*. Proceedings of the American Mathematical Society,
Series B 10 (2023), 439–454; arXiv:2203.14950v1.
https://arxiv.org/abs/2203.14950v1
