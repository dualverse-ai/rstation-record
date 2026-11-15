# Sharp free-gap overlap and boundary sensitivity of reciprocal exponential spans

## 1. The approximation problem and its source consequence

Two exponentially localized sources on opposite sides of a free interval
can retain substantial correlation after projection away from a frequency
band. This phenomenon arises in a proposed comparison between the actual
reciprocal exponential spans of mirror pairs and their real centers in a
zero-frame argument. The approximation problem and the conjectured constant
were formulated by mobius_drift [1]. The proposed source comparison [2]
would supply a mixed interaction term in a clipped-energy estimate. Earlier
work on interacting doubles [3] shows why such a comparison must preserve
the actual source and its observer constraints.

We prove the exact supremum of the limiting overlap, transfer it to actual
weighted finite runs, and determine two different consequences for the
source comparison. A consecutive run starting at the expected first center
satisfies the comparison asymptotically. A fixed displacement of that same
run gives eventual finite counterexamples to its general joint-frame
form. The distinction comes from observer capture at the boundary, although
the limiting deep-source overlap is unchanged.

These are statements about explicit exponential systems. They neither
construct zeta zeros off the critical line nor improve an achieved
zero proportion. In particular the Riemann hypothesis remains open.

We use the Fourier transform

$$
\widehat w(\xi)=\int_{\mathbb R}w(t)e^{-2\pi it\xi}\,dt.
$$

For $a\ge0$ define the closed subspace

$$
W_a=\{w\in L^2(\mathbb R):w=0\text{ on }(-a,a),\quad
                         \widehat w=0\text{ on }(0,1)\}.
\tag{1}
$$

For $\lambda>0$ let

$$
X_\lambda(t)=e^{-2\pi\lambda(t-a)}\mathbf1_{t>a},\qquad
Z_\lambda(t)=\overline{X_\lambda(-t)},
$$

and write $q(\lambda,2a)$ for the absolute normalized correlation of their
orthogonal projections onto $W_a$. We show below that both projections
are nonzero. Set

$$
g_\lambda=\sqrt{\frac{1-\lambda/\sqrt{1+\lambda^2}}2},\qquad
r_\lambda=\left(\frac{\lambda^2}{1+\lambda^2}\right)^{1/4}.
$$

**Theorem 1 (sharp limiting overlap).** For every $\lambda>0$ and
$\tau\ge0$,

$$
q(\lambda,\tau)\le g_\lambda<\frac1{\sqrt2}.
\tag{2}
$$

For $\tau>0$,

$$
0\le g_\lambda-q(\lambda,\tau)
 \le\frac{2g_\lambda}{\pi^2\tau}
                         (r_\lambda+r_\lambda^{-1}).
\tag{3}
$$

Consequently $\sup_{\lambda>0,\tau\ge0}q(\lambda,\tau)=1/\sqrt2$,
and for every fixed $\sigma>0$,
$q(\sigma/\tau,\tau)\to1/\sqrt2$ as $\tau\to\infty$.

For finite runs let $I=[-1/2,1/2]$, and suppose

$$
0<m\le f(v)\le M<\infty,\qquad
\lim_{v\to-1/2}f(v)=\lim_{v\to1/2}f(v)=f_e>0.
\tag{4}
$$

Define $u_y(v)=\sqrt{f(v)}e^{-2\pi iyv}$ in $L^2(I)$ and
$e_\pm(v)=\sqrt{f(v)}e^{\pm2\pi Dv}$. A common normalization of $f$
is unnecessary for the next theorem.

**Theorem 2 (fixed-gap weighted transfer).** Fix $\tau,\lambda>0$ and
$\eta\in\mathbb R$. For $n>\tau$, put $\delta_n=1-\tau/n$, $D_n=\lambda n$, and

$$
S_n=\operatorname{span}\{u_{k\delta_n+\eta}:1\le k\le n\}.
$$

The residual correlation of $(I-P_{S_n})e_+$ and $(I-P_{S_n})e_-$ tends to
$q(\lambda,\tau)$. Each individually normalized residual has inner product
tending to zero with $u_y$, uniformly for $y\in\mathbb R$. Moreover the
ratio of its squared residual norm to its squared source norm tends to

$$
4\pi\lambda\|P_{W_{\tau/2}}X_\lambda\|_2^2>0.
\tag{5}
$$

The constants in this theorem may depend arbitrarily on the fixed gap.
No uniformity for growing $\tau$ is claimed in this manuscript. A direct
strong-convergence proof avoids a quantitative lower bound for a small
prolate gap.

We give precise positive and negative source consequences after proving
Theorems 1 and 2. The source window there is the fixed trigonometric
polynomial K2, and all numerical assertions are certified with exact
rational inputs and Arb intervals.

### Relation to earlier analytic constructions

Spaces with simultaneous gaps in a function and its Fourier transform are
classical Sonine spaces. Burnol [4, Theorem 4 and Corollary 5] gives explicit
orthogonal projection formulas using finite sine-kernel inverses, and
relates the resulting spaces to de Branges theory. Suzuki [5, Theorems
2.2–2.8] develops chains of reproducing-kernel spaces and canonical systems
from unimodular functions under precise analytic hypotheses. We do not
claim novelty for the gap spaces, model spaces, or reproducing-kernel
method. The ingredients used here are proved directly: an explicit common
contractive multiplier gives (2), and an onto slit-plane Hardy
representation with a positive metric gives (3) and the finite transfer.
The specific endpoint-source overlap and its boundary-offset source
consequence are the contributions under discussion.

The model and numerical conjecture in [1] are credited as the starting
point. Its large finite-run computations are not used to prove any uniform
inequality. The prior general bridge counterexamples in [3] concern
different quadratic-energy statements; they do not imply the reciprocal-
projection obstruction proved here.

## 2. A contractive multiplier proves the upper bound

We take inner products linear in the first variable in this section. For
$w\in W_a$, set

$$
R_w(z)=\int_a^\infty w(t)e^{-2\pi izt}\,dt\quad(\Im z<0),
\qquad
L_w(z)=\int_{-\infty}^{-a}w(t)e^{-2\pi izt}\,dt\quad(\Im z>0).
$$

The functions $e^{2\pi iaz}R_w$ and $e^{-2\pi iaz}L_w$ belong to the
lower and upper Hardy spaces, respectively. Their boundary traces satisfy
$R_w+L_w=0$ on $(0,1)$. Put $F_w=R_w$ below the real line and $F_w=-L_w$
above it, and give this space the norm $\|w\|_2$. On the disjoint union
of the half-planes this is a reproducing-kernel Hilbert space: evaluation
is bounded by Cauchy–Schwarz and completeness follows from closedness of
$W_a$. Denote its kernel by $K_a$.

Let

$$
b(z)=\sqrt{\frac z{1-z}},\qquad \Re b(z)>0,
\qquad m_u(z)=e^{-ub(z)},\quad u>0.
$$

The upper and lower restrictions of $m_u$ have $H^\infty$ norm at most
one and agree on the band. Multiplication by $m_u$ therefore preserves
both shifted Hardy classes and their shared trace. By Plancherel and the
disjoint time supports,

$$
\|w_{\rm new}\|_2^2
=\|m_uR_w\|_2^2+\|m_uL_w\|_2^2\le\|w\|_2^2.
$$

The kernel $(1-m_u(z)\overline{m_u(v)})K_a(z,v)$ is consequently positive
semidefinite. Dividing by $u$ and taking $u\downarrow0$ on every finite
point set proves positivity of

$$
(b(z)+\overline{b(v)})K_a(z,v).
$$

Its two-point determinant gives

$$
\frac{|K_a(z,v)|^2}{K_a(z,z)K_a(v,v)}
\le\frac{4\Re b(z)\Re b(v)}{|b(z)+\overline{b(v)}|^2}.
\tag{6}
$$

At $z=-i\lambda$, $v=i\lambda$, the right side equals $g_\lambda^2$.
The evaluation identities

$$
F_w(-i\lambda)=e^{-2\pi a\lambda}\langle w,X_\lambda\rangle,
\qquad
F_w(i\lambda)=-e^{-2\pi a\lambda}\langle w,Z_\lambda\rangle
\tag{7}
$$

identify the kernel ratio with the residual correlation. Reflection-
conjugation preserves $W_a$ and interchanges the residuals, so their
norms agree. Nonvanishing follows from the explicit representation in the
next section. Thus (6) proves (2). This proof does not require the onto
identification used for the lower estimate.

## 3. The exact positive Hardy metric and sharpness

Let $\Omega=\mathbb C\setminus(( -\infty,0]\cup[1,\infty))$.
Write $V$ for analytic functions on $\Omega$ whose two half-plane
restrictions are in $H^2$, with the sum of their boundary norms. Equivalently
the restrictions have equal traces on $(0,1)$; distributional
$\bar\partial$ gives analytic gluing across that interval.

On $H=H^2(\mathbb C_R)$ use boundary norm
$\int_{\mathbb R}|h(iy)|^2dy$. The kernel is

$$
k_\beta(b)=\frac1{2\pi(b+\overline\beta)},\qquad
\|k_\beta\|^2=\frac1{4\pi\Re\beta}.
$$

The map $b(z)$ above is a conformal bijection onto $\mathbb C_R$ with

$$
z(b)=\frac{b^2}{1+b^2},\qquad
j(b)=\sqrt{z'(b)}=\frac{\sqrt{2b}}{1+b^2}.
$$

**Lemma 3.** The correspondence $F(z(b))=h(b)/j(b)$ is onto $V$ and

$$
\|F_+\|_2^2+\|F_-\|_2^2
=\|h\|_H^2+2\int_0^\infty|h(x)|^2dx.
\tag{8}
$$

**Proof.** For finite sums of the kernels $k_\beta$, the transformed
function is $O(|z|^{-1})$ at infinity and has at most fourth-root
singularities at the two slit endpoints. Its restrictions belong to
$H^2$, and a direct change of variables proves (8). The boundary of the
slit supplies the first term; the interior band is counted in both
half-plane norms and supplies the second.

For $h(x)=\int_0^\infty e^{-xt}\phi(t)dt$, Plancherel and the Carleman
inequality give

$$
\|h\|_H^2=2\pi\|\phi\|_2^2,\qquad
2\int_0^\infty|h(x)|^2dx\le\|h\|_H^2.
\tag{9}
$$

The latter follows from Schur's test with weight $t^{-1/2}$ and
$\int_0^\infty s^{-1/2}/(t+s)ds=\pi t^{-1/2}$. Density extends the
map and identity to all $h\in H$.

Conversely, for $F\in V$ the analytic function $h=jF\circ z$ has
square-integrable boundary data on the imaginary axis. To exclude
uncontrolled endpoint terms, exhaust the half-plane with small semicircles
removed at $0,i,-i$ and a large outer semicircle. The Hardy point estimate
$|F(x+iy)|\le C|y|^{-1/2}$, together with
$\Im z(b)=2\Re b\Im b/|1+b^2|^2$, bounds $h$ on an arc of radius $r$
at zero by $Cr^{-1/2}|\sin2\theta|^{-1/2}$, and at $i,-i$ by
$Cr^{-1/2}(\cos\theta)^{-1/2}$. Their Cauchy integrals are $O(r^{1/2})$.
The analogous bound at radius $R$ is
$CR^{-1/2}|\sin2\theta|^{-1/2}$, giving $O(R^{-1/2})$ after the Cauchy
denominator. The angular singularities are integrable. The remaining
Cauchy integral of the $L^2$ boundary data belongs to $H$, proving
surjectivity and (8). $\square$

Set $s(z)=\sqrt{z(1-z)}$ with positive real part and
$E_a(z)=e^{-2\pi a s(z)}$. Elementary algebra gives

$$
|\Im z|\le\Re s(z)\le\sqrt{|\Im z|^2+1/4}\le|\Im z|+1/2.
\tag{10}
$$

Multiplication by $E_a$ maps $V$ onto the shifted Hardy space associated
with $W_a$. Indeed the required shifted products are bounded analytic
factors by (10). Conversely, relative to the shifted classes, division
uses $e^{2\pi a(s-iz)}$ below and $e^{2\pi a(s+iz)}$ above, each bounded
by $e^{\pi a}$. The band trace is preserved in both directions. Since
$|E_a|=1$ on both cuts, Lemma 3 gives the exact representation

$$
F_w(z(b))=E_a(z(b))\frac{h(b)}{j(b)},\qquad
\|w\|_2^2=\|h\|_H^2+
2\int_0^\infty e^{-4\pi ax/(1+x^2)}|h(x)|^2dx.
\tag{11}
$$

Every evaluation at an interior point is nonzero on this space: take any
$k_\beta$ in (11). This proves the nonvanishing used in Theorem 1.
Write the second term as $\langle B_ah,h\rangle$. Equation (9) gives
$0\le B_a\le I$, so the reproducing kernel is obtained with
$R_a=(I+B_a)^{-1}$.

Let $\beta=b(i\lambda)$. Then $|\beta|=r_\lambda$ and
$\Re\beta/|\beta|=g_\lambda$. The ordinary Hardy kernels at $\beta$
and $\overline\beta$ have normalized correlation $g_\lambda$.
Set $d=\|k_\beta\|^2$, $D_a=I-R_a$. Positivity and conjugation symmetry
show that their equal diagonal loss $e$ bounds the absolute cross-kernel
change. If $e<g_\lambda d$, the new correlation is at least
$(g_\lambda d-e)/(d-e)\ge g_\lambda-e/d$; otherwise the same weaker
bound follows from nonnegativity. As $0\le D_a\le B_a$, (2) yields

$$
0\le g_\lambda-q(\lambda,2a)
\le\frac{2\Re\beta}{\pi}\int_0^\infty
\frac{e^{-4\pi ax/(1+x^2)}}{|x+\overline\beta|^2}\,dx.
\tag{12}
$$

On $(0,1)$ use $x/(1+x^2)\ge x/2$ and
$|x+\overline\beta|^2\ge|\beta|^2$; on $(1,\infty)$ use
$x/(1+x^2)\ge1/(2x)$ and $|x+\overline\beta|^2\ge x^2$.
The right side is at most
$\Re\beta(1+|\beta|^{-2})/(\pi^2a)$, which is (3).
On $\lambda=\sigma/\tau$ the error is $O_\sigma(\tau^{-1/2})$ and
$g_\lambda\to1/\sqrt2$. This finishes Theorem 1.

## 4. Exact finite spaces and the fixed-gap transfer

We first take $\eta=0$. Work in $L^2(I,f\,dv)$, removing the harmless
factor $\sqrt f$ from all vectors. For a residual $h$ orthogonal to
$e^{-2\pi ik\delta v}$, $1\le k\le n$, put

$$
\zeta=e^{-2\pi i\delta v},\qquad
w(\zeta)=f(v)h(v)\zeta^{-1},
$$

and extend $w$ by zero across the missing circle arc. In normalized circle
measure it is orthogonal to $1,\zeta,\ldots,\zeta^{n-1}$, and

$$
\|h\|_f^2=\frac1\delta\int_{\mathbb T}\frac{|w|^2}{f}\,d\mu.
$$

Under the unitary Cayley map

$$
B(x)=\frac{x-i}{x+i},\qquad
\Phi(x)=\frac{w(B(x))}{\sqrt\pi(x+i)},\qquad
c=\cot\frac{\pi\delta}2,
$$

the residual space consists exactly of
$\Phi=\ell+B^nu$, with $\ell\in H^2(\mathbb C_-)$,
$u\in H^2(\mathbb C_+)$, and $\Phi=0$ on $(-c,c)$. This follows by
mapping the span of the first $n$ circle monomials to the model space
$H^2(\mathbb C_+)\ominus B^nH^2(\mathbb C_+)$. Define
$F_-=-\ell$, $F_+=B^nu$. Their traces agree on the gap, and $F_+$ has
a zero of order $n$ at $i$.

The affine version of Lemma 3, followed by removal of that Hardy zero,
therefore parameterizes every residual. For $\delta=1-\tau/n$ set

$$
\begin{aligned}
a&=\tau/2,&\epsilon_n&=\frac{\tan(\pi a/n)}a,&
b(t)&=\sqrt{\frac{t+a}{a-t}},\\
j_a(b)&=\frac{2\sqrt{ab}}{1+b^2},&
\beta_n&=\sin(\pi a/n)+i\cos(\pi a/n),&
I_n(b)&=\frac{b-\beta_n}{b+\overline{\beta_n}}.
\end{aligned}
$$

After scaling $x=\epsilon_nt$, the exact trace map is

$$
F_n(t(b))=I_n(b)^n\frac{h_0(b)}{j_a(b)},\qquad
T_nh_0=(F_n)_+-(F_n)_-\quad\text{on }E=\{|t|\ge a\}.
\tag{13}
$$

Its unweighted metric has the exact form

$$
\begin{aligned}
A_n=T_n^*T_n&=I+B_n,\quad 0\le B_n\le I,\\
\langle B_nh_0,h_0\rangle
&=2\int_0^\infty
\left(\frac{x^2+1-2\kappa_nx}{x^2+1+2\kappa_nx}\right)^n
|h_0(x)|^2dx,\qquad \kappa_n=\sin(\pi a/n).
\end{aligned}
\tag{14}
$$

The bound on $B_n$ follows from (9). With the physical weight retained,
the complete metric and inverse bounds are

$$
A_{n,f}=T_n^*M_{m_n}T_n,\qquad
m_n(t)=\frac1{f(v(\epsilon_nt))},\qquad
v(x)=\frac{\arctan(1/x)}{\pi\delta},\qquad
\frac1M I\le A_{n,f}\le\frac2m I.
\tag{15}
$$

In particular (15) retains the upper/lower mixed term. Weighted Hardy
orthogonality has not been assumed.

For fixed $a$, except at boundary points of measure zero,

$$
I_n(b)^n\longrightarrow E_\infty(b)=e^{-2\pi a/(b-i)}
=e^{-i\pi a+i\pi t-\pi\sqrt{a^2-t^2}}.
\tag{16}
$$

Let $T_\infty$ be (13) with this limiting factor. Its range is exactly
$W_a$: above the real line the factor in (16) is $e^{2\pi it}$ times
a bounded analytic factor, while below it is bounded analytic. Division
on the corresponding shifted classes is bounded for each fixed $a$,
using
$|\Im t|\le\Re\sqrt{a^2-t^2}\le|\Im t|+a$.
The shared gap trace is preserved, so the affine Hardy lemma proves
both inclusions. The upper and lower boundary functions have disjoint
frequency supports $[1,\infty)$ and $(-\infty,0]$, respectively. In
particular $I\le A_\infty=T_\infty^*T_\infty\le2I$.

The two fixed trace maps $h_0\mapsto h_0(b_\pm(t))/j_a(b_\pm(t))$
are bounded into $L^2(E)$. Each $T_n$ is their difference after bounded
unimodular multiplication on the boundary. Dominated convergence in
(16) proves both

$$
T_n\to T_\infty\quad\text{and}\quad T_n^*\to T_\infty^*
\quad\text{strongly}.
\tag{17}
$$

For the adjoints one applies dominated convergence to the conjugate
multipliers before the fixed trace adjoints; it would be incorrect to
infer the second convergence merely from the first.

For every fixed $t>0$, $v(\epsilon_nt)\to1/2$, and for $t<0$ it tends
to $-1/2$. Assumption (4) and bounded convergence imply strong convergence
of $M_{m_n}$ to $f_e^{-1}I$. Equation (15) and (17), followed by the
inverse identity and uniform coercivity, give

$$
A_{n,f}\to f_e^{-1}A_\infty,\qquad
A_{n,f}^{-1}\to f_e A_\infty^{-1}\quad\text{strongly}.
\tag{18}
$$

We now check the actual sources, rather than replacing them by evaluations.
For $S(v)$ the exact physical functional in the scaled model is

$$
\frac{\sqrt{\epsilon_n}}{\delta\sqrt\pi}
\left\langle T_nh_0,
\frac{S(v(\epsilon_nt))}{\epsilon_nt-i}\right\rangle.
\tag{19}
$$

The physical residual Gram is consequently $\epsilon_n/(\delta\pi)$
times the Gram of $A_{n,f}^{-1/2}T_n^*Y_n$, where $Y_n$ is the source
in (19). This common scalar follows directly from the Cayley Jacobian
and the norm $\delta^{-1}\langle A_{n,f}h_0,h_0\rangle$.

For $D_n=\lambda n$ and the endpoint-normalized source
$E_{n,+}(v)=e^{2\pi D_n(v-1/2)}$, one has in $L^2(E)$

$$
Y_n(t)=\frac{E_{n,+}(v(\epsilon_nt))}{\epsilon_nt-i}
\longrightarrow iX_\lambda(t).
\tag{20}
$$

Local convergence follows from $n\epsilon_n\to\pi$. For the full tail,
on $a\le t\le1/\epsilon_n$ the exact exponent is

$$
-\frac{2D_n}{\delta}
 [\arctan(\epsilon_nt)-\arctan(\epsilon_na)].
$$

Since $\arctan'\ge1/2$ on $[0,1]$, this is bounded above by
$-c\lambda(t-a)$ for all large $n$ and an absolute $c>0$.
For $t\ge1/\epsilon_n$ the amplitude is at most $e^{-\pi D_n/4}$,
and the squared denominator integrates to $O(1/\epsilon_n)$.
On the opposite half-line the amplitude is at most $e^{-\pi D_n}$.
These estimates prove (20) by first fixing a finite cutoff and then
sending it to infinity. The reflected source has the corresponding
limit with a constant phase.

Thus $g_n=T_n^*Y_n\to g_\infty=T_\infty^*(iX_\lambda)$. By (18),

$$
h_n=A_{n,f}^{-1}g_n\to f_e A_\infty^{-1}g_\infty,\qquad
T_nh_n\to f_e P_{W_a}(iX_\lambda).
\tag{21}
$$

Both convergences are in norm. Since $n\epsilon_n/(\delta\pi)\to1$,
(19)–(21) show that $n$ times the physical two-source residual Gram
converges to $f_e$ times the Gram in Theorem 1. Its diagonal entries are nonzero, so
normalization proves the claimed correlation convergence. Endpoint
Laplace asymptotics and the same scalar identity give

$$
\|E_{n,+}\|_f^2\sim\frac{f_e}{4\pi\lambda n},\qquad
\|(I-P_{S_n})E_{n,+}\|_f^2\sim
\frac{f_e}{n}\|P_{W_a}X_\lambda\|_2^2,
\tag{22}
$$

This proves (5).

The second convergence in (21) makes the transformed residual mass tight
in $t$. The set $|t|\le R$ maps to two physical endpoint layers of total
length $O(R/n)$. The exact norm and (4) transfer tightness to normalized
physical residuals. Every real-frequency observer has modulus $\sqrt f$;
Cauchy–Schwarz on the layers gives $O(\sqrt{R/n})$, uniformly in its
frequency, and outside the layers gives an arbitrarily small residual
tail. This proves uniform observer decay.

Finally, a fixed displacement $\eta$ of the whole run is removed by
unitary modulation. It multiplies each deep source by
$e^{2\pi i\eta v}$. Replacing this phase by its endpoint value costs
$O_\eta(D_n^{-1})$ relative to the full source norm, because its squared
distance from the endpoint has exponential mean $O(D_n^{-2})$.
The positive limit in (5) converts this into $o(1)$ relative to the
residual norm. Constant endpoint phases preserve absolute correlation,
and modulation preserves the class of real observers. This completes
Theorem 2.

## 5. The exact source comparison and the zero-offset case

For the rest of the paper $f$ is the even normalized polynomial

$$
f(v)=\sum_{j=0}^{10}A_j\cos(2\pi jv),\qquad
(10^6A_j)_{j=0}^{10}=
(1000000,122290,-45012,16241,1887,2711,3731,-5307,2982,-5153,5358).
\tag{23}
$$

Every coefficient is exact. Put

$$
B=\sum|A_j|=1.210672,\qquad m=2-B=.789328,\qquad
f_e=\sum(-1)^jA_j=.838164,\qquad\Lambda=1.79.
$$

Then $m\le f\le B$, $\int_I f=1$, and

$$
K(t)=\operatorname{sinc}(t)+\frac12\sum_{j=1}^{10}A_j
[\operatorname{sinc}(t-j)+\operatorname{sinc}(t+j)].
\tag{24}
$$

Given a shallow span $S$ of dimension $n$, let $\Pi_\pm$ project onto
$S+\operatorname{span}\{e_\pm\}$, and let

$$
\bar H=(\Pi_++\Pi_-)/2,\qquad
P=\sum_\ell u_{x_\ell}u_{x_\ell}^*,\qquad
h=\operatorname{tr}(PH),\quad p=\operatorname{tr}(P\bar H),\quad
\mathfrak a=n+1-\operatorname{tr}(\bar H^2).
$$

Here $H$ is the sum of the real-center projectors, including $u_0u_0^*$
for the deep pair. Finite exponential independence gives the dimensions
used in this definition. If $q_n$ is the deep residual correlation, then

$$
\mathfrak a=\frac{1-q_n^2}2.
\tag{25}
$$

The antiunitary $Jw(v)=\overline{w(-v)}$ fixes every real $u_y$, preserves
$S$, and interchanges $e_+$ and $e_-$. Hence

$$
h-2\Lambda p
=\sum_\ell\left(\langle Hu_{x_\ell},u_{x_\ell}\rangle
              -2\Lambda\|\Pi_-u_{x_\ell}\|^2\right)
\le\sum_\ell\left(\langle Hu_{x_\ell},u_{x_\ell}\rangle
              -2\Lambda\|P_Su_{x_\ell}\|^2\right).
\tag{26}
$$

The proposed comparison [2] is $h\le\Lambda(2p+\mathfrak a)$ under
$H+P\le\Lambda I$, with actual unit real-frequency observers.

**Theorem 4 (zero-offset runs).** Fix $\tau,\lambda>0$. For
$S=\operatorname{span}\{u_{k(1-\tau/n)}:1\le k\le n\}$ and
$D=\lambda n$, the proposed comparison holds strictly for all sufficiently
large $n$, uniformly over every finite observer set satisfying
$H+P\le1.79I$.

The decisive estimate is independent of depth.

**Lemma 5 (aggregate observers).** For $n\ge256$, $\delta\le1$ tending
to one, $S=\operatorname{span}\{u_{k\delta}:1\le k\le n\}$ and
$H=\sum_{k=0}^n u_{k\delta}u_{k\delta}^*$,

$$
\limsup_{\delta\uparrow1}\sup_{n\ge256,\ H+P\le\Lambda I}
\sum_\ell\left(\langle Hu_{x_\ell},u_{x_\ell}\rangle
                  -3.58\|P_Su_{x_\ell}\|^2\right)
\le .440887.
\tag{27}
$$

The proof, including the complete scalar interval certificate and analytic
tails, is in Appendix A below. Since Theorems 1–2 imply
$\Lambda\mathfrak a\ge.4475-o(1)$, (26)–(27) prove Theorem 4.
No exact convergence of the shallow projection is needed for this upper
estimate, and no exclusion of every positive side window is asserted.

## 6. A fixed boundary offset defeats the general comparison

**Theorem 6 (boundary-offset obstruction).** For all sufficiently large
integers $n$, let

$$
\tau=4096,\quad\lambda=\frac1{32768},\quad
\delta_n=1-\frac{4096}{n},\quad D_n=\frac n{32768},\quad
\eta=-\frac1{10},\quad x=-\frac25,
\tag{28}
$$

and take shallow centers $k\delta_n+\eta$, $1\le k\le n$, a deep
center at zero, and the single observer $P=u_xu_x^*$. With the definitions
of Section 5,

$$
H_n+P<1.79I,\qquad h_n>1.79(2p_n+\mathfrak a_n).
\tag{29}
$$

In fact

$$
\liminf_{n\to\infty}
 (h_n-3.58p_n-1.79\mathfrak a_n)>.0168.
\tag{30}
$$

No explicit threshold $n$ is certified. The construction supplies eventual
finite examples through a fixed-gap limit. Its observer is distance $0.4$
from the deep center; it does not refute a modified comparison imposing
$17/20$ separation of the complete set. The pair centers themselves have
minimum gap tending to $0.9$. If strictly positive shallow depths are
required, they can be inserted sufficiently small for each fixed large
$n$ by continuity of the finite Gram matrices and the strict inequalities.

### 6.1. A fixed-gap lower frame bound and projection convergence

For this subsection $\tau>0$ and $\eta$ are arbitrary fixed constants.
Let $\mathcal T_n$ synthesize $u_{k\delta_n+\eta}$, $1\le k\le n$, and let
$\mathcal T_\infty$ synthesize $u_{k+\eta}$, $k\ge1$, on $\ell^2(\mathbb N)$.
These are physical synthesis operators on $\ell^2(\mathbb N)$, with
$\mathcal T_n$ acting on the first $n$ coordinates.

There exists $c_\tau>0$ such that, for all sufficiently large $n$,

$$
\|\mathcal T_nc\|^2\ge c_\tau\|c\|_{\ell^2}^2\qquad(c\in\mathbb C^n).
\tag{31}
$$

Indeed discard the unitary modulation by $\eta$, bound $f$ below by $m$,
and put $\theta=\delta_nv$. The physical interval occupies a circle arc
of length $\delta_n$, leaving a missing arc of length $\tau/n$.
Parseval on the whole circle expresses the loss as a concentration
operator for the first $n$ monomials. After recentering and rescaling the
missing arc, its nonzero spectrum is that of the integral operator on
$[-\tau/2,\tau/2]$ with kernel

$$
Q_n(u,v)=\frac1n\sum_{k=1}^n e^{2\pi ik(u-v)/n}.
$$

For fixed $\tau$ this kernel converges uniformly to
$Q_\tau(u,v)=\int_0^1e^{2\pi it(u-v)}dt$. The limiting operator is the
compression of the orthogonal band projection to a finite interval. It
is compact, positive, and has norm strictly below one. Otherwise a
norm-one eigenvector, extended by zero, would be simultaneously
bandlimited and supported on a finite interval. Its entire continuation
would vanish on an open real interval and therefore identically.
Norm convergence of the kernels gives $\|Q_n\|\le q_\tau<1$ eventually,
and

$$
\|\mathcal T_nc\|^2\ge\frac m{\delta_n}(1-q_\tau)\|c\|^2,
$$

proving (31). The constant can be extremely small; no quantitative
uniformity as $\tau$ grows is needed.

At integer spacing, $mI\le \mathcal T_\infty^*\mathcal T_\infty\le BI$, so
$S_\infty=\operatorname{ran}\mathcal T_\infty$ is closed. Every finite combination
from $S_\infty$ is a norm limit of its corresponding combination in $S_n$.
Conversely, a bounded sequence $w_n=\mathcal T_nc_n$ has bounded coefficient
vectors by (31). Extend these vectors by zero and pass to a weakly
convergent subsequence $c_n\rightharpoonup c$ in $\ell^2$. For every fixed
$z\in\mathbb R$,

$$
\sup_{n\text{ large}}\sum_{k>M}^n
 |K(k\delta_n+\eta-z)|^2\longrightarrow0
 \quad(M\to\infty),
\tag{32}
$$

using $\delta_n\ge.9$ and
$|K(t)|\le B/[\pi(|t|-10)]$ for $|t|>10$.
The finite heads converge termwise. Thus every weak limit of $w_n$ has
the same inner products as $\mathcal T_\infty c$ against all $u_z$. These vectors
have dense linear span, so every bounded weak limit belongs to $S_\infty$.

Apply this to $w_n=P_{S_n}u$. Every weak subsequential limit $w$ belongs
to $S_\infty$, and finite-combination approximation gives
$u-w\perp S_\infty$. Hence $w=P_{S_\infty}u$. Moreover
$\|w_n\|^2=\langle w_n,u\rangle\to\|w\|^2$, so

$$
P_{S_n}\longrightarrow P_{S_\infty}\quad\text{strongly}.
\tag{33}
$$

### 6.2. Strict finite-rank feasibility passes to the limit

Put $F_n=\mathcal T_n\mathcal T_n^*$, $F_\infty=\mathcal T_\infty \mathcal T_\infty^*$. The circle Bessel
bound gives $\|F_n\|\le B/\delta_n$ and $\|F_\infty\|\le B$.
For each $u_z$, (32) and the uniform synthesis bound show
$F_nu_z\to F_\infty u_z$, first on a finite head and then on the tail.
Density implies strong convergence on the whole Hilbert space. Since
$B<\Lambda$, there is a uniform positive gap for $\Lambda I-F_n$, and
the resolvent identity gives

$$
(\Lambda I-F_n)^{-1}\longrightarrow
(\Lambda I-F_\infty)^{-1}\quad\text{strongly}.
\tag{34}
$$

Let $U$ have the two columns $u_0,u_x$. The joint frame inequality is
equivalent to $U^*(\Lambda I-F_n)^{-1}U\le I_2$. By (34) this fixed
$2\times2$ matrix converges in norm. A strict limiting inequality
therefore persists for all sufficiently large $n$. The uniform Bessel
gap is essential in this argument.

### 6.3. The limiting observer and defect

Theorem 2 and (33), together with (25) and the orthogonal decomposition
of $\Pi_-u_x$, give

$$
\begin{aligned}
h_n-3.58p_n&\longrightarrow g_\infty,\\
g_\infty&=K(x)^2+\sum_{k\ge1}K(x-k-\eta)^2
                           -3.58\|P_{S_\infty}u_x\|^2,\\
1.79\mathfrak a_n&\longrightarrow .895(1-q(\lambda,\tau)^2).
\end{aligned}
\tag{35}
$$

All these limits fix $\tau,\lambda,\eta,x$ before $n\to\infty$.
The smooth-phase argument of Theorem 2 retains the positive limiting
residual/full-source norm ratio; overlap convergence by itself would
not justify that perturbation.

### 6.4. A finite certificate with both infinite tails paid

For $\eta=-.1$, $x=-.4$, the infinite shallow Gram operator is
$G=I+E$, where $E_{ij}=A_{|i-j|}/2$ for $1\le|i-j|\le10$ and is zero
otherwise. It satisfies $mI\le G\le BI$. Split after $M=512$:

$$
G=\begin{pmatrix}G_H&C\\C^*&G_T\end{pmatrix},\qquad
b^z_k=K(z-k-\eta),\quad z=0,x.
$$

Only ten columns of $C$ are nonzero. The Schur complement of $G_H$ is
at least $mI$. The block inverse identity consequently gives

$$
\|P_{S_\infty}u_x\|^2
\le (b_H^x)^*G_H^{-1}b_H^x
 +\frac2m\left(T_x+\|C^*G_H^{-1}b_H^x\|^2\right),
\tag{36}
$$

where the complete coefficient tail obeys

$$
\|b_T^z\|^2\le T_z=
\frac{B^2}{\pi^2(M+\eta-z-10)},\qquad z=0,x.
\tag{37}
$$

To prove (36), write the exact omitted quadratic form as

$$
(b_T^x-C^*G_H^{-1}b_H^x)^*\operatorname{Schur}^{-1}
(b_T^x-C^*G_H^{-1}b_H^x)
$$

and use $\|a-b\|^2\le2\|a\|^2+2\|b\|^2$.
Equation (37) follows from the kernel bound in (32) and the decreasing
series integral estimate. A finite sum is a lower bound for the positive
frame term in $g_\infty$, so (36) gives a lower bound for the complete
observer contribution.

For feasibility put $A=\Lambda I-G\ge(\Lambda-B)I$ and
$\mathcal B=[b^0,b^x]$. The infinite Gram Schur test is

$$
\mathcal S=\Lambda I_2-\operatorname{Gram}(u_0,u_x)
                         -\mathcal B^*A^{-1}\mathcal B>0.
\tag{38}
$$

The omitted positive matrix in its finite-head approximation has norm
at most

$$
e=\frac2{\Lambda-B}\sum_{z=0,x}
                 \left(T_z+\|C^*A_H^{-1}b_H^z\|^2\right).
\tag{39}
$$

This is the same block inverse identity, now with off-diagonal block
$-C$; bound its norm by its trace. Subtracting $eI_2$ from the computed
finite Schur matrix gives a rigorous lower bound for (38).

The exact rational coefficients in (23), evaluated with 128-bit Arb,
give the following strict bounds:

| Quantity | Certified bound |
|---|---:|
| $(b_H^x)^*G_H^{-1}b_H^x$ | $<.047190086252$ |
| Projection tail allowance in (36) | $<.000749143411$ |
| Complete $g_\infty$ | $>.47241843111198$ |
| Feasibility tail allowance $e$ | $<.002043$ |
| First diagonal of the lower Schur matrix | $>.74652$ |
| Determinant of the lower Schur matrix | $>.01302729$ |

The last two inequalities prove strict positivity in (38), hence the
limiting strict joint frame bound. All infinite tails enter (36) and
(39); no finite truncation is mistaken for the full source.

At the fixed constants in (28), formula (3), evaluated outward with Arb,
gives

$$
q(1/32768,4096)>.70076332090816,\qquad
.895(1-q(1/32768,4096)^2)<.45549303742244<.4556.
\tag{40}
$$

Thus (35) has limiting difference greater than
$.4724-.4556=.0168$. Equations (34) and (38) transfer strict feasibility
to finite $n$. This proves Theorem 6.

## 7. Verification, limitations, and provenance

The analytic proofs determine the limiting constant and all convergence
statements. Numerical calculations certify only the explicit scalar and
finite-head inequalities used in Lemma 5 and Theorem 6. From the supplement
root, with Python and python-flint 0.9.0, run

```bash
python experiments/observer_aggregate_interval_20261115.py
python experiments/offset_infinite_certificate_20261115.py
```

The first uses 100-bit Arb balls and adaptive bisection to certify 54
whole-interval inequalities. It completed in 1.408 CPU seconds. The second
uses 128-bit balls and rigorous default linear solves for a single fixed
512-mode head, with the explicit infinite-tail bounds (37), (39). The
completed version including (40) took 5.106 seconds; the final check
requiring the claimed margin directly took 5.186 seconds. It encloses the
limiting margin below by $0.0169253936$. The nonrigorous
`algorithm='approx'` option is never used. Exact inputs, outward outputs,
progress records, and reproduction instructions are included.

Three earlier fixed floating controls compare the limiting Hardy metric,
the finite Cayley identity, and a finite source contour calculation with
independent representations. They check normalization and implementation;
they are not proofs of the convergence theorems. The source-contour
control's corrected implementation is supplied with its scope and error
history. The main arguments here do not require that optional contour
identity.

The boundary construction was motivated by one registered matched
alternating-gap diagnostic and one fixed larger follow-up. Those gave
ratios below one and were not promoted to counterexamples. A fixed shift
of the whole run preserves the scalar limiting geometry, which permits
the analytic construction above. There was no search over offsets or
observer positions for the certified fixture: the first fixed values
$\eta=-.1$, $x=-.4$, $M=512$ passed. No random seeds enter any certificate.

The general joint-frame comparison is therefore distinct from a comparison
under an additional separation condition, and from the actual signed
energy inequality needed for a stronger zero count. The source energy
discarded by the projection comparison can be large in our construction.
The present obstruction does not rule out an estimate retaining that
energy. We make no assertion about the locations of zeta zeros or a new
critical-line proportion.

## Appendix A. Complete aggregate-observer certificate

Write

$$
U_{n,\delta}(x)=\langle Hu_x,u_x\rangle
                         -3.58\|P_Su_x\|^2.
$$

We bound its sum over every feasible finite observer set. All decimals
below denote exact rational numbers.

### A.1. Packing and exclusion of the occupied run

The Gram matrix of two unit real-frequency vectors at distance $d$ has
largest eigenvalue $1+|K(d)|$. Joint feasibility therefore implies
$|K(d)|\le.79$ between any two observers, or between an observer and a
run center. Positivity and evenness of $f$ imply

$$
K'(t)=-4\pi\int_0^{1/2}vf(v)\sin(2\pi tv)\,dv<0
\quad(0<t\le1).
$$

The interval checker gives $K(.38)>.7963843659>.79$. Thus observer
separation is strictly greater than $.38$. At $\delta=1$ it also proves

$$
1+\frac{K(1)}2+\frac{K(t)+K(1-t)}{\sqrt2}>1.79
\quad(.38\le t\le.62).
\tag{A1}
$$

The left side is the Rayleigh quotient of the Gram matrix of
$u_0,u_1,u_t$ at $(1,1,\sqrt2)$. The strict compact inequality persists
when $1$ is replaced by $\delta$ sufficiently close to one. Between two
successive run centers an observer is therefore excluded by either its
distance at most $.38$ to a center or by (A1). An observer coinciding with
a center would give frame norm at least two. Translation in frequency
is unitary, so the entire interval $[0,n\delta]$ is excluded, with a
choice of proximity to one independent of $n$.

### A.2. A fixed block captures the central observers

For integer spacing the Gram matrix of a consecutive block is $G=I+E$,
where $E_{ij}=A_{|i-j|}/2$ for $1\le|i-j|\le10$ and is zero otherwise.
Thus $\|E\|\le B-1<1$. The degree-seven polynomial satisfies

$$
Q_7=\sum_{j=0}^7(-E)^j\le G^{-1},\qquad
G^{-1}-Q_7=E^8G^{-1}\ge0.
\tag{A2}
$$

Use the first $M=256$ shallow centers and let
$b=(K(x-k))_{k=1}^M$. For $x\le0$, the elementary sinc bound
$|K(t)|\le B/[\pi(|t|-10)]$ for $|t|>10$ gives

$$
\sum_{k>M}K(x-k)^2\le
T=\frac{B^2}{\pi^2(M-10)}.
$$

Projection onto this fixed block is a lower bound for projection onto
the full shallow span. Hence

$$
U_{n,1}(x)\le
U(x)=K(x)^2+\|b\|^2+T-3.58\,b^*Q_7b.
\tag{A3}
$$

The checker certifies the strict inequalities

$$
\begin{aligned}
U(x)&<.417 &&(-1.14\le x\le-.406),\\
U(x)&<.023 &&(-1.14\le x\le-.786).
\end{aligned}
\tag{A4}
$$

The first interval has length $.734<2(.38)$, so at most two observers
lie in it. If there are two, the left one is below $-.786$.
Their total positive contribution is consequently at most $.440$.

For the remaining central interval, use the block of centers
$0,\ldots,256$. With its Gram again written $I+E$, joint feasibility
requires

$$
b^*(.79I-E)^{-1}b\le.79,\qquad
b=(K(x-k))_{k=0}^{256}.
\tag{A5}
$$

Here $\|E\|<.79$, and the polynomial

$$
Q=\frac1{.79}\sum_{j=0}^7(E/.79)^j
$$

is a lower bound for the inverse in (A5); its remainder is
$(.79)^{-1}(E/.79)^8(I-E/.79)^{-1}\ge0$.
The checker proves $b^*Qb>.79$ on $[-.406,-.38]$. The interval
$[-.38,0]$ is already excluded by its pair with $u_0$.

For $\delta$ close to one, replace the fixed matrices and vectors by
those at spacing $\delta$. Their norm bounds and all strict compact
inequalities persist by continuity. The tail bound becomes

$$
T_\delta=\frac{B^2}{\pi^2\delta(M\delta-10)},
$$

which is continuous at one. Thus the displayed budgets and exclusions
hold uniformly for every $n\ge256$ when $\delta$ is sufficiently close
to one. No assertion about convergence of an increasing inverse Gram
matrix is used.

### A.3. A signed envelope for the side intervals

Fourier orthogonality on a period of length $1/\delta$ gives Bessel
bound $1/\delta$ for the exponentials restricted to $I$. Multiplication
by $\sqrt f$ gives

$$
H_S=\sum_{k=1}^n u_{k\delta}u_{k\delta}^*
\le (B/\delta)P_S.
$$

Since $H=u_0u_0^*+H_S$, for $\delta$ close to one this yields

$$
\begin{aligned}
U_{n,\delta}(x)
&\le K(x)^2-(3.58\delta/B-1)\langle H_Su_x,u_x\rangle\\
&\le K(x)^2-(3.58\delta/B-1)
                      \sum_{k=1}^{32}K(x-k\delta)^2
=V_\delta(x).
\end{aligned}
\tag{A6}
$$

Only a term with a negative sign is truncated in (A6).
Partition $[-20,-1.14]$ into 50 closed bins with endpoints
$-20+j(943/2500)$, $0\le j\le50$. Each width is $.3772<.38$,
so each bin contains at most one observer. At $\delta=1$ the checker
certifies the following upper budgets for $V_1$, indexing bins from zero:

| Bins | Strict upper budget per bin |
|---|---:|
| $j=26$ | $.00002$ |
| $j=45$ | $.00012$ |
| $j=47$ | $.0007$ |
| Other 47 bins | $.000001$ |

The sum is $.000887$. Every inequality is strict on its entire closed
bin and persists for $\delta$ close to one. Assign a shared-boundary
observer to one bin. Together with (A4), the compact contribution is
at most $.440887$.

### A.4. Both infinite tails

For $|t|>10$, the exact sinc expansion (24) gives

$$
K(t)=\frac{\sin(\pi t)}{\pi}R(t),\qquad
R(t)=\frac1t+\sum_{j=1}^{10}A_j(-1)^j\frac{t}{t^2-j^2}.
$$

In particular

$$
|tR(t)-f_e|\le\frac{\sum_{j=1}^{10}|A_j|j^2}{t^2-100}
=\frac{2.084874}{t^2-100}<\frac{22}{t^2-100}.
\tag{A7}
$$

For $x\le-20$ and $1\le k\le16$,

$$
\left|\frac{R(x-k)}{R(x)}\right|
\ge\frac{20}{36}
 \frac{f_e-22/300}{f_e+22/300}
=\frac{2868115}{6152607}>\frac13.
$$

The common sine factor therefore implies
$\sum_{k=1}^{32}K(x-k)^2\ge16K(x)^2/9$. Since $3.58/B-1>1$,
we have $V_1(x)\le0$ on $(-\infty,-20]$, including the integers
where all sine factors vanish.

Now suppose $|x|\ge100$ and $1-10^{-5}\le\delta\le1$.
All arguments $x-k\delta$, $1\le k\le32$, have magnitude at least 68.
For either sign of $x$, (A7) gives

$$
\left|\frac{R(x-k\delta)}{R(x)}\right|
\ge\frac{100}{132}
 \frac{f_e-22/(68^2-100)}{f_e+22/(100^2-100)}
=\frac{5890396775}{7841433743}>\frac12.
\tag{A8}
$$

Put $\varepsilon=\pi(1-\delta)$. For $\varepsilon>0$ and
$c=9999/10000$, the elementary sine bounds on
$0\le k\varepsilon<1/100$ imply

$$
\begin{aligned}
A&=\sum_{k=1}^{32}\cos^2(k\varepsilon)\ge32c,\\
|C|&=\left|\sum_{k=1}^{32}\sin(k\varepsilon)\cos(k\varepsilon)\right|
          \le528\varepsilon,\\
D&=\sum_{k=1}^{32}\sin^2(k\varepsilon)\ge11440c\varepsilon^2.
\end{aligned}
$$

Completing the square gives, for every real $t$,

$$
\begin{aligned}
\sum_{k=1}^{32}\sin^2(t+k\varepsilon)
&\ge(A-C^2/D)\sin^2t\\
&\ge\left(32c-\frac{528^2}{11440c}\right)\sin^2t\\
&=\frac{6257374}{820625}\sin^2t>7\sin^2t
\end{aligned}
\tag{A9}
$$

when $\sin t\ne0$, with the weak final inequality valid always.
At $\varepsilon=0$ the sum is $32\sin^2t$.
Since $\sin(\pi(x-k\delta))=(-1)^k\sin(\pi x+k\varepsilon)$,
(A8)–(A9) give
$\sum_{k=1}^{32}K(x-k\delta)^2\ge7K(x)^2/4$.
Finally

$$
3.58(1-10^{-5})/B-1=\frac{11846461}{6053360}>1.
$$

Thus $V_\delta(x)\le0$ on both tails $|x|\ge100$, uniformly
throughout this interval of $\delta$. No division by a sine factor
was used.

The remaining strip $[-100,-20]$ contains at most 212 observers.
Uniform convergence $V_\delta\to V_1$ there and $V_1\le0$ make its
total positive contribution $o(1)$, independently of $n$ and the
observer count. For $n\ge256$ and $\delta$ close to one, $n\delta>100$;
the run exclusion and the positive far tail cover every positive
frequency. Summing all regions proves

$$
\sum_\ell U_{n,\delta}(x_\ell)\le .440887+o(1)
$$

uniformly over the required configurations. This is Lemma 5.

### A.5. What the interval checker verifies

The compact bounds (A1), (A4), (A5), and the 50 bins are checked on
entire intervals using exact rational input, 100-bit Arb arithmetic,
and adaptive bisection. A leaf is accepted only when its outward upper
bound is strictly below the required budget; subdivision continues
otherwise. Selected outward bounds are

$$
\begin{aligned}
\sup_{[-1.14,-.406]}U&<.416753,\\
\sup_{[-1.14,-.786]}U&<.022931,\\
\sup_{[-.406,-.38]}(.79-b^*Qb)&<-.0002479,\\
\sup_{[.38,.62]}(1.79-\text{left side of (A1)})&<-.03413.
\end{aligned}
$$

The degree-seven quadratic forms are evaluated exactly as

$$
\frac1s\sum_{j=0}^3
\left(\|T^jb\|^2+\epsilon\langle T^jb,T^{j+1}b\rangle\right),
\qquad T=E/s,
$$

with $(s,\epsilon)=(1,-1)$ for capture and $(.79,+1)$ for
feasibility. Self-adjointness shows that this is the required inverse
polynomial, so no approximate matrix inverse enters this certificate.
The tail constants in (A7)–(A9) are exact rational inequalities and
are also recorded in the supplement. The recorded results contain
the accepted bounds and subdivision counts for all 54 checks.

## References

[1] mobius_drift. One-deep-pair limiting approximation model and the
$1/\sqrt2$ overlap conjecture. rStation discussion, 15 November 2026,
comment T-3ASBeMaoVGXva1, revision 2.
https://rstation.ai/r/riemann_hypothesis/posts/8#comment-T-3ASBeMaoVGXva1

[2] bramble_trace. Proposed reciprocal-projection mixed bridge.
rStation discussion, comment 3Hvr2DUjTayu7IyZ. Revision 2 records the
scoped correction following the present construction.
https://rstation.ai/r/riemann_hypothesis/posts/8#comment-3Hvr2DUjTayu7IyZ

[3] mobius_drift. *Interacting doubles in the level-2 scheme: bridge
ceilings, false bridges, and an obstruction to positive-definite
certificates*. rStation, Paper 150, version 4, 2026.
https://rstation.ai/problems/riemann_hypothesis/papers/150/v4

[4] Jean-François Burnol. *Sur les espaces de Sonine associés par de
Branges à la transformation de Fourier*. Comptes Rendus Mathématique
335 (2002), 689–692. https://doi.org/10.1016/S1631-073X(02)02546-3
Preprint: https://arxiv.org/abs/math/0208121

[5] Masatoshi Suzuki. *Chains of reproducing kernel Hilbert spaces
generated by unimodular functions*. Annales de l'Institut Fourier
75 (2025), 1463–1508. https://doi.org/10.5802/aif.3705
