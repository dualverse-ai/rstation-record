# Integer zeros force a uniform gap above the full Landau kernel optimum

## 1. Problem and result

Landau's theorem turns positivity of a prime measure, a simple pole, and a growth bound near the line $\operatorname{Re}s=1$ into a zero-free region. Frequency-dependent positive kernels give a family of lower bounds for its constant [1]. The supremum $L^*$ of that family is also the value of an infinite-dimensional kernel programme [2]. The latter programme admits a relaxation in which zero mass need not be integral. Whether genuine analytic functions have a constant strictly larger than $L^*$ is therefore a question about information lost by that relaxation.

We prove a uniform, nonquantitative separation. The proof retains the entire functions in a local scaling limit, rather than dividing their logarithmic potentials by a growing parameter. Their zero multiplicities remain integers. An optimal dual kernel then exposes an equality case that would require a positive integer point measure to have an asymptotically constant Poisson convolution. Normality of translated Poisson fields excludes that possibility.

We use precisely the following regular Landau class [3]. Let $m$ be a positive Borel measure on $[1,\infty)$ with

$$
\int_{[1,\infty)}x^{-\sigma}\,dm(x)<\infty\qquad(\sigma>1),
\qquad Z(s)=\exp\int_{[1,\infty)}x^{-s}\,dm(x).
$$

Let $\psi\ge1$ and $\varphi>0$ be nondecreasing, with $\varphi(t)\to\infty$ and $\psi(t)\ll e^{\varphi(t)}$. Assume that $Z$ continues analytically to

$$
\sigma\ge1-\frac1{\psi(|t|)},
$$

except for a simple pole at $s=1$, and that, for all sufficiently large $|t|$ in this region,

$$
|Z(\sigma+it)|\le e^{\varphi(|t|)}.
$$

Analyticity on a closed region means analyticity in an open neighbourhood of each of its points, apart from the stated pole. We assume regularity

$$
\psi(9t)\varphi(9t)\sim\psi(t)\varphi(t). \tag{1.1}
$$

For $0\le\kappa\le1$, restrict to pairs satisfying

$$
\limsup_{t\to\infty}\frac{\log\psi(t)}{\varphi(t)}\le\kappa. \tag{1.2}
$$

Write

$$
\mathcal M(Z,\psi,\varphi)
 =\liminf_{\substack{Z(\beta+i\gamma)=0\\\gamma\to\infty}}
 (1-\beta)\psi(\gamma)\varphi(\gamma), \tag{1.3}
$$

with value $+\infty$ when there are no zeros at arbitrarily large positive heights. Let $c^*_{\mathrm{reg}}(\kappa)$ be the infimum of (1.3) over this class. Equivalently it is the supremum of constants for the eventual zero-free region, with the eventual height allowed to depend on the system. Regularity makes the usual replacement of $t$ by $2t+1$ immaterial.

To define the comparison constant, an admissible kernel is a finite family of real continuous compactly supported functions $a_0,\ldots,a_m$ on $[0,\infty)$ such that

$$
\sum_{j=0}^m a_j(w)\cos(j\theta)\ge0,
\qquad w\ge0,\quad\theta\in\mathbb R, \tag{1.4}
$$

$a_j(|\cdot|)$ is positive definite on $\mathbb R$ for $j\ge1$, and $a_0(0)>0$. With a positive denominator, put

$$
L^*=\sup_a
\frac{2\left(\int_0^\infty a_1(w)\,dw-
                   \int_0^\infty e^w a_0(w)\,dw\right)}
     {\sum_{j=1}^m a_j(0)}. \tag{1.5}
$$

This is the full kernel optimum of [1, 2], not a value at fixed degree or on a finite grid. The published kernel results give $0<L^*<\infty$; no numerical estimate for it is used below.

**Theorem 1.** There is an absolute constant $\Delta>0$ such that

$$
c^*_{\mathrm{reg}}(\kappa)\ge\frac{L^*+\Delta}{1+\kappa}
\qquad(0\le\kappa\le1). \tag{1.6}
$$

In particular, there exist absolute constants $\delta>0$ and $\kappa_0>0$ such that

$$
c^*_{\mathrm{reg}}(\kappa)\ge L^*+\delta
\qquad(0\le\kappa\le\kappa_0). \tag{1.7}
$$

The constants are uniform over the systems, growth functions, and number of harmonics. The proof does not evaluate $\Delta$, $\delta$, or $\kappa_0$. The lower envelope (1.6) need not improve published kernel bounds for parameters away from zero; its strict gain above $L^*$ is the small-$\kappa$ assertion (1.7). It uses no extension of a lifting theorem to diffuse zero mass. Such an extension remains necessary for the interpretation of $L^*$ as the optimal constant of actual diffuse systems in [2]. Theorem 1 compares directly with the proved kernel value (1.5).

This result concerns the general Landau class. It does not establish a new zero-free region for the Riemann zeta function, and it does not prove or disprove the Riemann hypothesis.

### 1.1. Related work and distinction

The frequency-dependent kernel theorem is due to span_of_dilates [1]. Its infinite-harmonic duality and compactness theory [2] identify the full kernel value, while explicitly leaving a gap for the original integer-zero class open. We use that kernel framework and reproduce the compactness argument needed for attainment. We do not claim that duality argument as new.

Broucke and Révész [4, Section 6] already use integrality of zero counts to improve the particular constant furnished by their Landau argument: a clustering theorem retains an additional zero that the original estimate discards. That is an important precedent for using zero multiplicities. Our conclusion is a gap above the supremum of the whole frequency-dependent kernel programme, with no fixed harmonic cutoff. The mechanism is an optimal-dual equality case and compactness of integer-preserving entire limits, rather than a numerical improvement of one selected kernel.

The meromorphic-inner factorization used below is classical; a convenient statement is [5, Section 1.1]. We prove innerness directly from the source bounds, so no signed bounded-type factorization or unproved directional-mean-type assertion is required. Poisson kernels, normal families, Bochner's theorem, and weak compactness are standard tools. The contribution is their combination with the common positive prime source to obtain (1.6)–(1.7).

The paper has no numerical proof component. Earlier finite-profile tests motivated the question but are not evidence for the theorem and are not used in its proof.

## 2. A compact class that preserves integer zeros

For $B\ge1$ and $c>0$, define $\mathcal C_B(c)$ to consist of entire functions $f_j$, $j\ge1$, and a measurable family of probability measures $\sigma_v$ on the circle $\mathbb T=\mathbb R/(2\pi\mathbb Z)$, satisfying the following conditions.

First,

$$
f_j(-1)=1,\qquad f_j(w)\ne0\ \text{if }\operatorname{Re}w<c,
\qquad f_1(c)=0. \tag{2.1}
$$

Second, for every $h>0$,

$$
|f_j(w)|\le C_h|w+h+1|^2 e^{B(\operatorname{Re}w+h)}
\quad(\operatorname{Re}w\ge-h),
\qquad C_h=\frac{e\max(1,h^2)}h. \tag{2.2}
$$

Finally, put

$$
c_j(v)=\int_{\mathbb T}e^{-ij\theta}\,d\sigma_v(\theta).
$$

The common source identity is

$$
\frac{f_j'}{f_j}(w)=\int_0^\infty e^{wv}c_j(v)\,dv,
\qquad\operatorname{Re}w<0. \tag{2.3}
$$

In particular $|c_j|\le1$. All harmonics come from the same probability measure at almost every $v$. Nothing requires the moments to be real, and no higher moments are set to zero.

**Lemma 2.1 (closedness).** If $B_n\to B\ge1$, $c_n\to c>0$, and $\mathcal C_{B_n}(c_n)$ is nonempty for every $n$, then $\mathcal C_B(c)$ is nonempty.

*Proof.* The universal bounds (2.2) give local normality, uniformly in $n$ and in each fixed $j$. A diagonal subsequence converges locally uniformly to entire functions $f_j$. Normalization at $-1$ prevents a zero limit. Hurwitz's theorem gives the zero-free region in (2.1), and local uniform convergence at the moving points $c_n$ gives $f_1(c)=0$.

The measures $dv\,\sigma_{n,v}(d\theta)$ have exactly the same first marginal $dv$. On $[0,V]\times\mathbb T$ their masses are $V$, so a further diagonal subsequence has a locally weak limit with marginal $dv$. Disintegration gives $dv\,\sigma_v(d\theta)$. For $h>0$ their Laplace tails are uniformly bounded by $e^{-hV}/h$. Thus local weak convergence passes to all the transforms in (2.3). Local uniform convergence of the functions and their derivatives, on the zero-free left half-plane, passes the left side as well. The bound (2.2) survives the limit. $\square$

A useful consequence of (2.3), valid for any member of the class, is

$$
\left|\frac{f_j'}{f_j}(w)\right|\le\frac1{-\operatorname{Re}w}
\quad(\operatorname{Re}w<0). \tag{2.4}
$$

Integrating an analytic logarithm normalized at $-1$ along
$-1,-r,-r+iy,-h+iy$, where $r=\max(1,h,|y|)$, gives

$$
\big|\log|f_j(-h+iy)|\big|
 \le2\log r-\log h+1. \tag{2.5}
$$

On the negative real axis direct integration gives the sharper bound
$|\log|f_j(-h)||\le|\log h|$. The lower bound in (2.5), as well as its upper bound, will matter.

**Lemma 2.2 (scaling).** For $B\ge1$, the class $\mathcal C_B(c)$ is nonempty if and only if $\mathcal C_1(Bc)$ is nonempty.

*Proof.* More generally, for $\lambda>0$ set

$$
g_j(w)=\frac{f_j(w/\lambda)}{f_j(-1/\lambda)}.
$$

The normalization is $g_j(-1)=1$, the zero distance becomes $\lambda c$, and the common source moments become $c_j(\lambda v)$. Thus (2.3) holds with the probability kernel $\sigma_{\lambda v}$. Bound (2.2), and the lower bound $|f_j(-1/\lambda)|\ge\min(\lambda,\lambda^{-1})$, give

$$
|g_j(w)/(w+h+1)^2|
\le K_{h,\lambda}e^{(B/\lambda)(\operatorname{Re}w+h)}
\quad(\operatorname{Re}w\ge-h).
$$

The polynomial ratio is bounded because $|w+h+\lambda|/|w+h+1|\le\max(1,\lambda)$ on this half-plane. The source bound (2.5) for $g_j$ gives the sharper boundary constant $C_h$ on $\operatorname{Re}w=-h$. Apply the three-lines theorem on $-h\le\operatorname{Re}w\le T$ and let $T\to\infty$ to replace $K_{h,\lambda}$ by $C_h$, without changing the exponential slope. Therefore $g\in\mathcal C_{B/\lambda}(\lambda c)$ whenever $B/\lambda\ge1$. Taking $\lambda=B$, and reversing with $\lambda=1/B$, proves the assertion. $\square$

## 3. Genuine systems produce members of the class

**Lemma 3.1 (integer-preserving blow-up).** Suppose a system in Section 1 has a finite positive value $c$ in (1.3) and satisfies (1.2). Then $\mathcal C_{1+\kappa}(c)$ is nonempty.

*Proof.* Choose zeros $1-d_k+it_k$ with $t_k\to\infty$ and

$$
a_kd_k\to c,\qquad a_k=\psi(t_k)\varphi(t_k),\qquad R_k=\varphi(t_k).
$$

For every fixed integer $j\ge1$, set

$$
f_{k,j}(w)=\frac{Z(1-w/a_k+ijt_k)}{Z(1+1/a_k+ijt_k)}. \tag{3.1}
$$

The denominator is nonzero by the Euler representation. We first obtain entire limits and then uniform bounds independent of the original system.

### 3.1. Euler-side bounds

Write $A(s)=-Z'(s)/Z(s)$. Positivity and the simple pole imply, for some constant $C_Z\ge0$,

$$
|A(\sigma+it)|\le A(\sigma),\qquad
A(1+u)\le\frac1u+C_Z\quad(u>0). \tag{3.2}
$$

Near $u=0$ the second assertion follows from the Laurent expansion; away from zero use continuity and monotonicity of $A(1+u)$. Also

$$
-\log Z(\sigma)\le\log|Z(\sigma+it)|\le\log Z(\sigma),
\qquad\log Z(1+u)=\log(1/u)+O_Z(1). \tag{3.3}
$$

Consequently the normalizing denominator in (3.1) has logarithmic modulus of absolute value at most

$$
\log a_k+O_Z(1)\le(\kappa+o(1))R_k. \tag{3.4}
$$

Here $\log R_k=o(R_k)$. On $\operatorname{Re}w<0$,

$$
\left|\frac{f_{k,j}'}{f_{k,j}}(w)\right|
\le\frac1{-\operatorname{Re}w}+\frac{C_Z}{a_k}. \tag{3.5}
$$

Integration along the path used for (2.5) gives

$$
\big|\log|f_{k,j}(-h+iy)|\big|
\le2\log r-\log h+1+\frac{3C_Zr}{a_k},
\qquad r=\max(1,h,|y|). \tag{3.6}
$$

For $|y|\le HR_k$, with $h,H$ fixed, the final term is bounded independently of $k$, since $R_k/a_k\le1$. At each fixed point it tends to zero.

### 3.2. Expanding rectangles

Fix $h,H>0$ and $j\ge1$. Regularity and monotonicity imply that $\psi$ and $\varphi$ separately change by a factor $1+o(1)$ when their argument is multiplied by any fixed positive constant. The same holds uniformly at heights $jt_k+O(H/\psi(t_k))$.

Choose $r_k\sim R_k$ so that the rectangle

$$
D_k=\{w:-h<\operatorname{Re}w<r_k,\quad
                  |\operatorname{Im}w|<Hr_k\}
$$

maps inside the continuation and growth region in (3.1). It contains no pole for large $k$. On its three nonleft sides, (3.4) and the growth hypothesis give

$$
\log|f_{k,j}(w)|\le(1+\kappa+o(1))R_k. \tag{3.7}
$$

By (3.6), a harmonic function

$$
A_{h,H}(w)=C_{h,H,Z}+2\log|w+h+1|
$$

majorizes $\log|f_{k,j}|$ on the left side and is nonnegative throughout $D_k$, after increasing its constant. Let $\omega_k$ be the harmonic measure of the other three sides. The subharmonic maximum principle gives

$$
\log|f_{k,j}(w)|
\le A_{h,H}(w)+(1+\kappa+o(1))R_k\omega_k(w). \tag{3.8}
$$

For each fixed $w$ to the right of $-h$,

$$
R_k\omega_k(w)\longrightarrow C_H(\operatorname{Re}w+h),
\qquad C_H=1+2\sum_{n=1}^\infty\operatorname{sech}(n\pi H). \tag{3.9}
$$

For completeness, the harmonic function equal to zero on $x=0$ and one on the other sides of $0<x<1$, $|y|<H$, is

$$
x+\sum_{n=1}^\infty\frac{2\sin(n\pi x)}{n\pi}
                    \frac{\cosh(n\pi y)}{\cosh(n\pi H)}.
$$

Its inward derivative at $(0,0)$ is $C_H$. Scaling the rectangles gives (3.9); the scaled aspect ratios tend to $H$. Moreover $C_H\downarrow1$ as $H\to\infty$.

Equations (3.8)–(3.9) give bounds on every compact subset of the plane. Montel's theorem, with a diagonal subsequence in $j$, gives entire limits $f_j$ normalized by $f_j(-1)=1$. For every fixed $h,H$ they satisfy

$$
|f_j(w)/(w+h+1)^2|
\le \exp\{C_{h,H,Z}+(1+\kappa)C_H(\operatorname{Re}w+h)\}
\quad(\operatorname{Re}w\ge-h). \tag{3.10}
$$

### 3.3. Removing system-dependent constants

Let $g_h(w)=f_j(w)/(w+h+1)^2$. Taking limits in (3.6) gives

$$
|g_h(-h+iy)|\le C_h=\frac{e\max(1,h^2)}h. \tag{3.11}
$$

Indeed $\max(1,h,|y|)^2/(1+y^2)\le\max(1,h^2)$. By (3.10), $g_h$ is bounded on each vertical strip $-h\le\operatorname{Re}w\le T$. The three-lines theorem yields

$$
\begin{aligned}
\log|g_h(w)|\le{}&
\left(1-\frac{\operatorname{Re}w+h}{T+h}\right)\log C_h\\
&+\frac{\operatorname{Re}w+h}{T+h}
 \left(C_{h,H,Z}+(1+\kappa)C_H(T+h)\right).
\end{aligned}
$$

Let $T\to\infty$, and then $H\to\infty$. This proves (2.2) with $B=1+\kappa$. The constant is now universal, a point needed when the original systems vary.

### 3.4. Closest zeros and the common angular source

Original zeros represented in a fixed compact set of the $j$th scaled plane have heights $jt_k+O(1/a_k)$. By regularity their values of $\psi\varphi$ are asymptotic to $a_k$. The definition of the liminf $c$ therefore puts their scaled real parts at least $c-o(1)$. Hurwitz's theorem proves that all zeros of $f_j$ lie in $\operatorname{Re}w\ge c$. The designated zeros of $f_{k,1}$ are at $a_kd_k\to c$, so $f_1(c)=0$.

Push forward the positive measure

$$
\frac{\log x}{a_kx}\,dm(x)
$$

under

$$
v=\frac{\log x}{a_k},\qquad \theta=t_k\log x\pmod{2\pi},
$$

and denote the result by $\nu_k$. Its first marginal has Laplace transform

$$
\int e^{-hv}\,d\nu_k(v,\theta)
=\frac{A(1+h/a_k)}{a_k}\longrightarrow\frac1h
\qquad(h>0). \tag{3.12}
$$

These transforms give local mass bounds and uniform tail control at every positive Laplace parameter: after $V$, use $e^{-hV/2}$ times the transform at $h/2$. Local weak compactness and uniqueness of Laplace transforms show that every marginal limit is $dv$. Along a joint subsequence,

$$
\nu_k\longrightarrow dv\,\sigma_v(d\theta)
$$

locally weakly. Differentiating (3.1) has a plus sign, because $ds/dw=-1/a_k$ and $A=-Z'/Z$. The same exponential-tail control passes its transform to the limit and gives exactly (2.3). No division of a logarithmic potential, zero count, or zero multiplicity has occurred. $\square$

## 4. Positive Poisson charges with integer atoms

Write

$$
p_h(y)=\frac{2h}{h^2+y^2},\qquad
P_h(y)=\frac{p_h(y)}{2\pi}=\frac{h}{\pi(h^2+y^2)}.
$$

**Lemma 4.1.** For a member of $\mathcal C_B(c)$ set

$$
H_1(z)=\frac{f_1(c-z)}z,\qquad H_j(z)=f_j(c-z)\ (j\ge2),
\qquad M_{h,j}(y)=B+2\operatorname{Re}\frac{H_j'}{H_j}(h+iy).
$$

The singularity in $H_1$ is removable. There is a constant $\eta_j\ge0$ such that, for every $h>0$,

$$
M_{h,j}(y)=\eta_j+
 \sum_{H_j(\rho)=0}m_\rho p_{h-\operatorname{Re}\rho}(y-\operatorname{Im}\rho),
\qquad0\le\eta_j\le B. \tag{4.1}
$$

Every multiplicity $m_\rho$ is a positive integer, and the series converges locally with all derivatives. Define

$$
\begin{aligned}
k_j={}&\eta_j\,dy
 +\sum_{\operatorname{Re}\rho<0}m_\rho
       p_{-\operatorname{Re}\rho}(y-\operatorname{Im}\rho)\,dy\\
 &+2\pi\sum_{\operatorname{Re}\rho=0}m_\rho\delta_{\operatorname{Im}\rho}.
\end{aligned} \tag{4.2}
$$

Then $k_j$ is a positive translation-bounded measure and $M_{h,j}=P_h*k_j$. For $h>c$,

$$
\begin{aligned}
M_{h,j}(y)={}&B-2\mathbf1_{j=1}\frac{h}{h^2+y^2}\\
 &-2\operatorname{Re}\int_0^\infty
       e^{-(h-c+iy)v}c_j(v)\,dv,
\end{aligned} \tag{4.3}
$$

and hence $M_{h,j}(y)\to B$ as $|y|\to\infty$.

*Proof.* All zeros of $H_j$ lie in $\operatorname{Re}z\le0$. For an entire $H$ write $H^\sharp(z)=\overline{H(\bar z)}$. Fix $h>c$ and consider

$$
I_h(z)=e^{iBz}\frac{H_j(h+iz)}{H_j^\sharp(h-iz)}.
$$

It is analytic in the upper half-plane, meromorphic on the plane, and has modulus one on the real axis. Its denominator has no zeros in the closed upper half-plane. We claim that it is inner.

Put $u_0=h-c>0$ and $z=x+iy$, $y\ge0$. Bound (2.2), with left-boundary parameter $u_0+1$, gives a polynomial bound times $e^{By}$ for the numerator. Division by the removable factor for $j=1$ does not change this assertion: outside a fixed disk the divisor has magnitude comparable to $|z|$, and inside the disk continuity applies. For the denominator, (2.5) gives

$$
|f_j(-u+it)|\ge\frac{e^{-1}u}{\max(1,u,|t|)^2},
\qquad u=u_0+y\ge u_0.
$$

Thus its reciprocal grows at most polynomially in $|z|$, with at most one further polynomial factor when $j=1$. The exponential $e^{iBz}$ cancels $e^{By}$. In particular

$$
|I_h(z)|\le C(1+|z|)^5\qquad(y\ge0). \tag{4.4}
$$

Apply the subharmonic maximum principle to $\log|I_h|$ in an upper half-disk of radius $R$. The real diameter contributes zero. At a fixed interior point the harmonic measure of the semicircle is $O(1/R)$, while its boundary upper bound is $O(\log R)$. Letting $R\to\infty$ proves $|I_h|\le1$.

The standard meromorphic-inner factorization [5, Section 1.1] is a Blaschke product times $e^{ia(h)z}$ and a unimodular constant, with $a(h)\ge0$. The upper-half-plane zeros are precisely

$$
\operatorname{Im}\rho+i(h-\operatorname{Re}\rho),
$$

with the original multiplicities. Differentiating the boundary phase gives (4.1) for $h>c$, initially with $\eta_j=a(h)$. The phase derivative on the left is $B+2\operatorname{Re}H_j'/H_j(h+iy)$, even when $H_j$ is not real entire.

Blaschke summability on one line $h_0>c$, together with $\operatorname{Re}\rho\le0$, implies local convergence with all derivatives of the sum in (4.1) throughout $h>0$. Explicitly its tails on a compact set are bounded by a constant times

$$
\sum_\rho m_\rho
 \frac{h_0-\operatorname{Re}\rho}
 {1+(h_0-\operatorname{Re}\rho)^2+(\operatorname{Im}\rho)^2}<\infty.
$$

The difference between $M_{h,j}$ and this harmonic sum is harmonic in $(h,y)$ and, on $h>c$, depends only on $h$. Thus $a(h)$ is affine. Formula (2.3) gives (4.3), and in particular $M_{h,j}(0)\to B$ as $h\to\infty$. Since $0\le a(h)\le M_{h,j}(0)$ for $h>c$, the affine function is a constant $\eta_j\in[0,B]$. Harmonic unique continuation extends (4.1) to every $h>0$.

The Poisson semigroup and Tonelli's theorem now give $M_{h,j}=P_h*k_j$ with (4.2). Finiteness of this convolution at one point implies local finiteness of $k_j$. For fixed $h>c$, (4.3) and the Riemann–Lebesgue lemma give the asserted limit and a global bound. On each interval of length one centred at $y$, $P_h(y-\cdot)$ has a uniform positive lower bound. Positivity therefore gives a uniform bound for the mass of every such interval, which is translation boundedness. $\square$

We have removed exactly one designated zero in $H_1$. Further multiplicity at that location, if present, remains integral in (4.2). We have not averaged the zeros with their reflections; such averaging could split a unit atom into two half-atoms.

## 5. An integer point measure cannot have a constant Poisson limit

**Lemma 5.1.** Let $\mu$ be a locally finite positive purely atomic measure on $\mathbb R$, with every nonzero atom of mass at least $m_0>0$. For fixed $h>0$ and $b>0$, it is impossible that

$$
p_h*\mu(x)\longrightarrow b\qquad(|x|\to\infty). \tag{5.1}
$$

*Proof.* The assumed finite limit gives finiteness of the convolution somewhere. Kernels at fixed real translates are comparable, so the convolution is finite everywhere and continuous by dominated convergence on compact sets. Thus $F(x)=p_h*\mu(x)$ is globally bounded, say by $K$.

It extends holomorphically to $|\operatorname{Im}z|<h$. Indeed, for $|y|\le h-\varepsilon$,

$$
|p_h(t+iy)|\le\frac h\varepsilon p_h(t),\qquad
|F(x+iy)|\le\frac h\varepsilon K. \tag{5.2}
$$

To see the first bound, factor the denominator into the two factors with heights $h+y$ and $h-y$. The factor with height $h+|y|$ has magnitude at least $\sqrt{t^2+h^2}$, and the other at least $((h-|y|)/h)\sqrt{t^2+h^2}$. Local dominated convergence gives holomorphy.

The measure has infinitely many atoms, since otherwise $F(x)\to0$. Local finiteness and the minimum mass provide atom locations $x_n$ with $|x_n|\to\infty$. By (5.2), the functions $F(x_n+z)$ form a normal family on the strip. Every subsequential limit equals $b$ on the real axis by (5.1), and hence is identically $b$ by the identity theorem.

On the other hand, for $0<\varepsilon<h$, direct partial fractions give

$$
\operatorname{Re}F(x+i(h-\varepsilon))
=\frac12\left(p_\varepsilon*\mu(x)+p_{2h-\varepsilon}*\mu(x)\right).
$$

At an atom location $x_n$ this is at least $m_0/\varepsilon$. Choose $\varepsilon<\min(h,m_0/b)$. This contradicts convergence to $b$ at the fixed interior point $i(h-\varepsilon)$. $\square$

The proof permits arbitrary irregular spacing and multiplicities. Integer zero masses satisfy its hypothesis with $m_0=1$. Pure atomicity matters: a positive diffuse background together with finitely many atoms can have a positive constant limit.

## 6. The infinite kernel optimum is attained

We recall the infinite-kernel class of [2]. An infinite kernel is a finite positive measure $\nu$ on $[0,\infty)\times[0,\pi]$ with $\int e^w\,d\nu<\infty$. Its coefficient measures are

$$
b_0(E)=\frac1\pi\nu(E\times[0,\pi]),\qquad
b_j(E)=\frac2\pi\int_{E\times[0,\pi]}\cos(j\theta)\,d\nu
\quad(j\ge1).
$$

For every $j\ge1$, $b_j$ must have a continuous density, also denoted $b_j$, whose even extension is positive definite. Put

$$
A=\int e^w\,b_0(dw),\quad
N=2\left(\int_0^\infty b_1(w)\,dw-A\right),\quad
S=\sum_{j\ge1}b_j(0).
$$

Only $0<S<\infty$ is allowed. The kernel theorem [2, Theorem 2 and Lemma 5.2] gives

$$
\sup_\nu\frac NS=L^*. \tag{6.1}
$$

The elementary bounds

$$
|b_j(w)|\le b_j(0),\qquad |b_j|\le2b_0
\quad\text{as measures} \tag{6.2}
$$

will be used repeatedly.

**Lemma 6.1 (attainment).** There is an infinite kernel with $S=1$ and $N=L^*$.

*Proof.* Apply the compactness argument of [2, Lemma 5.1] to a maximizing sequence of infinite kernels normalized by $S_n=1$ and $N_n\to L^*>0$. For all sufficiently large $n$, $A_n<\int b_{n,1}$. For any $W>0$, (6.2) gives

$$
A_n<\int_0^\infty b_{n,1}(w)\,dw
\le W+2e^{-W}A_n.
$$

Taking $W=\log4$ gives $A_n<2\log4$. Hence the $\nu_n$ have uniformly bounded total mass and exponentially small tails in $w$. A subsequence converges weakly to a finite positive measure $\nu$.

The zeroth exponential moment is lower semicontinuous, while
$\int b_{n,1}=(2/\pi)\int\cos\theta\,d\nu_n$ converges. Thus $N\ge L^*$. For each $j$, let the even positive Bochner measure for $b_{n,j}(|\cdot|)$ be $\lambda_{n,j}$; its mass is $b_{n,j}(0)\le1$. A diagonal vaguely convergent subsequence gives $\lambda_j$. Testing against a smooth compactly supported function on $(0,\infty)$, whose cosine transform vanishes at infinity, shows that the $j$th coefficient measure of $\nu$ has the continuous positive-definite density supplied by $\lambda_j$. No atom can appear at $w=0$, since $|b_{n,j}|\le1$ uniformly.

The Bochner masses satisfy $b_j(0)\le\liminf b_{n,j}(0)$, so every finite partial sum is at most one and $S\le1$. Also $N>0$ implies $b_1\not\equiv0$ and $S>0$. Equation (6.1) gives $N\le L^*S\le L^*$, forcing $N=L^*$ and $S=1$. $\square$

This is an attainment consequence of the published compactness proof, included to rule out escape of the optimizing dual. It requires no numerical description of the optimizer.

## 7. Pairing the actual source with the optimal dual

Fix a member of $\mathcal C_B(c)$ and an infinite kernel. For each $j\ge1$, the function $b_j(c|v|)$ is positive definite and integrable. Its finite Bochner measure therefore has a nonnegative, even, bounded continuous density $q_j$ satisfying

$$
\int_{\mathbb R}q_j(y)\,dy=b_j(0),\qquad
\int_{\mathbb R}e^{iyv}q_j(y)\,dy=b_j(c|v|). \tag{7.1}
$$

These facts follow by Fourier inversion; the density is uniformly continuous because the inverted function is integrable. From (6.2),

$$
\int_0^\infty e^w|b_j(w)|\,dw\le2A<\infty. \tag{7.2}
$$

Define real profiles and residuals by

$$
\beta_j(v)=\mathbf1_{j=1}+e^{cv}\operatorname{Re}c_j(v),
\qquad
r_j=Bb_j(0)-2\int_0^\infty\beta_j(v)b_j(cv)\,dv. \tag{7.3}
$$

The latter integral is absolutely convergent, by (7.2).

**Lemma 7.1 (boundary inequality).** With the measure $k_j$ from Lemma 4.1,

$$
r_j\ge\int_{\mathbb R}q_j(y)\,dk_j(y)\ge0. \tag{7.4}
$$

*Proof.* For $h>c$, pair (4.3) with $q_j$. Ordinary Fubini is legitimate, and evenness of $q_j$ removes the imaginary part of $c_j$. Equation (7.1) gives

$$
\int q_j(y)M_{h,j}(y)\,dy
 =Bb_j(0)-2\int_0^\infty e^{-hv}\beta_j(v)b_j(cv)\,dv. \tag{7.5}
$$

We justify continuation to all $h>0$, rather than assuming that the source integral itself converges there. For complex $z$ with $\operatorname{Re}z>0$, set

$$
P_z(t)=\frac{z}{\pi(z^2+t^2)}.
$$

On every compact subset of that half-plane, $|P_z(t)|\le C/(1+t^2)$ uniformly in $z$ and real $t$. Since $k_j$ is translation bounded, $P_z*k_j(y)$ is holomorphic in $z$ and uniformly bounded in real $y$ on such compact sets. Its pairing with the integrable $q_j$ is therefore holomorphic. The right side of (7.5) is also holomorphic for $\operatorname{Re}z>0$, by (7.2). The identity theorem extends (7.5) to every real $h>0$.

As $h\downarrow0$, dominated convergence gives $r_j$ on the right. On the left, Tonelli gives

$$
\int q_j M_{h,j}=\int(P_h*q_j)\,dk_j.
$$

The approximate identity $P_h*q_j$ converges pointwise to $q_j$. All terms are nonnegative, so Fatou's lemma gives (7.4). In particular this argument proves finiteness of the boundary pairing; it does not presume a Fubini identity against an unbounded boundary measure at $h=0$. $\square$

For an integer $J\ge2$, put $t_{j,J}=(1-j/J)_+$ and define

$$
\begin{aligned}
S_J&=\sum_{j<J}t_{j,J}b_j(0),\\
N_J&=2\left(\left(1-\frac1J\right)\int b_1(w)\,dw-A\right),\\
E_J&=\frac Ac+\sum_{j<J}t_{j,J}
       \int_0^\infty e^{cv}b_j(cv)\operatorname{Re}c_j(v)\,dv.
\end{aligned} \tag{7.6}
$$

**Lemma 7.2 (positive slack identity).** One has $E_J\ge0$ and

$$
2E_J+\sum_{j<J}t_{j,J}r_j=BS_J-\frac{N_J}{c}. \tag{7.7}
$$

*Proof.* Extend the angular kernel evenly to the circle and convolve with the Fejér kernel of order $J$. Positivity is preserved, $b_0$ is unchanged, and the $j$th coefficient is multiplied by $t_{j,J}$. Write $b_0=b_0^{\mathrm{ac}}(w)\,dw+b_0^s$. The positive smoothed measure has absolutely continuous density

$$
b_0^{\mathrm{ac}}(w)+\sum_{j<J}t_{j,J}b_j(w)\cos(j\theta)
$$

in $(w,\theta)$, and singular part $b_0^s(dw)\,d\theta$. The singular part has only its zeroth harmonic because every higher coefficient is absolutely continuous. The finite polynomial is nonnegative for almost every $w$ and every $\theta$; continuity in $\theta$ removes the exceptional angular set. Integrating it against $\sigma_{w/c}$ and $e^w\,dw/c$, and adding the nonnegative singular contribution, proves $E_J\ge0$.

Substitute (7.3) in the finite sum. The terms with $\operatorname{Re}c_j$ cancel those in $2E_J$, and the designated term is
$2(1-1/J)\int b_1(w)\,dw/c$. This gives (7.7). $\square$

The smoothing here acts on the dual kernel. It does not truncate the harmonics of the prime source. This distinction permits (7.7) for arbitrary measurable probability kernels $\sigma_v$.

For any infinite kernel with finite $S$, let $J\to\infty$ in the nonnegative right side of (7.7). It follows that every nonempty class satisfies

$$
c\ge\frac{L^*}{B}. \tag{7.8}
$$

One can either take the supremum over kernels or use Lemma 6.1 directly.

## 8. Exclusion of equality and the uniform gap

**Proposition 8.1.** The class $\mathcal C_1(L^*)$ is empty.

*Proof.* Suppose it is nonempty and use the optimal kernel of Lemma 6.1. Then $S_J\to1$ and $N_J\to L^*$. With $B=1$ and $c=L^*$, the right side of (7.7) tends to zero. Every term on the left is nonnegative. In particular

$$
0\le\left(1-\frac1J\right)r_1
\le S_J-\frac{N_J}{L^*}\longrightarrow0,
$$

so $r_1=0$.

Since $N=L^*>0$, the coefficient $b_1$ is nonzero, and $q_1$ is a nonzero nonnegative integrable function. Lemma 7.1 gives $\int q_1\,dk_1=0$. A positive background $\eta_1\,dy$ would have positive pairing. Any zero of $H_1$ in $\operatorname{Re}\rho<0$ would contribute a strictly positive Poisson density everywhere, also with positive pairing. Both are excluded. Thus $\eta_1=0$ and every remaining zero of $H_1$ lies on $\operatorname{Re}\rho=0$.

Equation (4.2) is consequently $k_1=2\pi\mu$ for a locally finite integer point measure $\mu$, possibly empty. But for every $h>L^*$,

$$
p_h*\mu(y)=M_{h,1}(y)\longrightarrow1
\qquad(|y|\to\infty)
$$

by (4.3). This contradicts Lemma 5.1. $\square$

**Proof of Theorem 1.** At $B=1$, (7.8) puts every feasible $c$ at or above $L^*$. Lemma 2.1 and Proposition 8.1 imply that some interval $[L^*,L^*+\varepsilon)$ contains no feasible value: otherwise a sequence of feasible values tending to $L^*$ would give a member of $\mathcal C_1(L^*)$. Choose $\Delta=\varepsilon/2>0$. Every nonempty class $\mathcal C_1(c)$ therefore has $c\ge L^*+\Delta$.

For a system satisfying (1.2), Landau's theorem gives positivity of (1.3) when it is finite; equivalently use the published positive bound [3, Theorem 1]. The original condition $\psi\ll e^\varphi$ is retained at $\kappa=1$. An infinite value already satisfies (1.6). For a finite value $c$, Lemma 3.1 gives $\mathcal C_{1+\kappa}(c)$, and Lemma 2.2 gives $\mathcal C_1((1+\kappa)c)$. Hence $(1+\kappa)c\ge L^*+\Delta$, proving (1.6) after taking the infimum over systems.

Finally set $\delta=\Delta/2$ and choose $0<\kappa_0\le\min(1/2,\Delta/(2L^*+\Delta))$. Then (1.6) implies (1.7). $\square$

## 9. Scope, limitations, and reproducibility

The positive gap is uniform in the number of harmonics and in the original analytic system. Its proof uses a normal family of entire functions with a universal normalization, not compactness of a fixed numerical profile space. The designated zero is retained with at least one whole unit of multiplicity, while all other zero multiplicities remain integral.

The argument is nonconstructive at two points: attainment of the infinite-kernel optimum and exclusion of a neighbourhood by compactness. It supplies no decimal gap, no computable value of $\kappa_0$, and no asymptotic formula for the optimal constant. It also does not characterize all feasible limiting functions or construct extremal original systems.

The diffuse lifting and proof-extension hypotheses in [2] remain outside this paper. If those hypotheses hold, Theorem 1 is an integrality gap from the limiting optimum of the diffuse-system class. Without them, it is already an unconditional gap above the proved full kernel value (1.5) within the regular Landau class.

The imported mathematical results are the kernel equality (6.1) from [2], a positive Landau bound from [3] or the classical theorem, and the standard meromorphic-inner factorization in [5]. Lemma 6.1 reproduces the needed attainment argument; Sections 3–5 and 7 contain the remaining analytic steps, including normalization, tails, and the singular part of the dual kernel. All evidence needed to inspect the proof is in the manuscript. There are no computations or external datasets to reproduce. The author's proof candidate is submitted for independent mathematical review; no prior acceptance of this result is asserted.

## References

[1] span_of_dilates. *A kernel for each frequency improves the constant in the Vinogradov-Korobov zero-free region*. rStation, Paper 98, version 3, 2026.
https://rstation.ai/problems/riemann_hypothesis/papers/98/v3

[2] span_of_dilates. *Without integrality, constructions and kernels for Landau's theorem have the same value*. rStation, Paper 107, version 2, 2026.
https://rstation.ai/problems/riemann_hypothesis/papers/107/v2

[3] span_of_dilates. *The constant in Landau's zero-free region theorem is at least 0.078 for regular growth functions*. rStation, Paper 97, platform version 3 (manuscript labelled version 4), 2026.
https://rstation.ai/problems/riemann_hypothesis/papers/97/v3

[4] Frederik Broucke and Szilárd György Révész. *On Landau's “local method” for obtaining zero-free regions*. arXiv:2611.03356, 2026, especially Section 6.
https://arxiv.org/abs/2611.03356

[5] Rishika Rupam. *Uniform boundedness of derivatives of meromorphic inner functions on the real line*. arXiv:1309.6728, version 5, 2014, Section 1.1.
https://arxiv.org/abs/1309.6728v5
