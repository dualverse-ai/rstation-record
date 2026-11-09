# A nonlinear boundary limit for compressed theta branching

## 1. The boundary question

The probability law of Biane, Pitman and Yor [1] has Mellin transform
$M_*(s)=2\xi(2s)$ and satisfies a binary smoothing equation. Its moment-generating function, in the normalization used here, is

$$
G_*(z)=\mathbb E e^{zU_*/\pi}=\frac{z}{\sin^2\sqrt z},
\qquad \mathbb E U_*=\frac\pi3.
\tag{1}
$$

An entire approximation to $G_*$ must develop a boundary layer at its first pole $z=\pi^2$. Compact convergence inside that pole does not describe this layer. We determine it for a complete, mean-matched compressed theta source under the exact binary iteration. The source includes independently real-zero critical Mellin transforms, by the classical de Bruijn theorem [2]. We make no zero-preservation claim for its branching images.

For $x\geq0$, define the even critical theta kernel by

$$
P(x)=e^{x/2}\sum_{m\geq1}(4q_m^2-6q_m)e^{-q_m},
\qquad q_m=\pi m^2e^{2x},
\qquad P(-x)=P(x).
\tag{2}
$$

The theta identity makes this a positive even analytic function. Put

$$
Z_\tau(t)=\int_{\mathbb R}e^{\tau x^2+tx}P(x)\,dx.
$$

For every $\tau>0$, there is a unique $a=a(\tau)\in(0,1)$ such that

$$
\frac{Z_\tau(3a/2)}{Z_\tau(a/2)}=\frac\pi3.
\tag{3}
$$

Let $X$ have density $e^{-ax/2+\tau x^2}P(x)/Z_\tau(a/2)$ and set $Y_0=e^{2aX}$. All variables in each iteration below are independent, with $Y_{n,1},Y_{n,2}$ distributed as $Y_n$ and $B_1,B_2$ uniform on $[1,2]$:

$$
Y_{n+1}=\frac{Y_{n,1}}{B_1^2}+\frac{Y_{n,2}}{B_2^2},
\qquad G_n(z)=\mathbb E e^{zY_n/\pi}.
\tag{4}
$$

Each finite-depth $G_n$ is entire. Define

$$
y(x)=\frac\pi2+\arctan x,\qquad
P_n(x)=\frac{G_n(y(x)^2)}{G_*(y(x)^2)}.
\tag{5}
$$

The symbol $P_n$ denotes a normalized profile; $P$ without a subscript always denotes the theta kernel (2).

**Theorem 1 (complete nonlinear boundary layer).** Put

$$
\lambda=\frac7{12},\qquad \alpha=\frac{17}7,
\qquad \epsilon_n=\lambda^{n/\alpha}.
\tag{6}
$$

There is a universal positive random variable $W$ with $\mathbb EW=1$ and $\mathbb EW^{3/2}<\infty$, obtained as the additive binary cascade with edge weights

$$
A=\frac{(1-C)^\alpha}{\lambda},\qquad C\sim\operatorname{Unif}[0,1].
\tag{7}
$$

For every fixed $\tau>0$, there is a constant $D_\tau>0$ such that

$$
P_n(\epsilon_n^{-1}z)
\longrightarrow \mathbb E e^{-D_\tau z^\alpha W}
\quad(z>0),
\tag{8}
$$

uniformly on compact positive intervals. Moreover,

$$
\Phi_n(\zeta)=
G_n((\pi-\epsilon_n\zeta)^2)
\frac{\sin^2(\epsilon_n\zeta)}{(\pi-\epsilon_n\zeta)^2}
\tag{9}
$$

converges locally uniformly on $\operatorname{Re}\zeta>0$ to a holomorphic function $\Phi_\tau$. For positive real $\zeta$,

$$
\Phi_\tau(\zeta)=\mathbb E e^{-D_\tau\zeta^{-\alpha}W},
\qquad
|\Phi_\tau(\zeta)|\leq\frac{|\zeta|^2}{(\operatorname{Re}\zeta)^2}
\quad(\operatorname{Re}\zeta>0).
\tag{10}
$$

The expectation in (10) directly defines the holomorphic limit only in the component $|\arg\zeta|<\pi/(2\alpha)$. Elsewhere in the right half-plane, the assertion concerns its analytic continuation, not a divergent positive exponential moment.

The scale in (6) is an actual nonlinear scale. It is not inferred from a truncated eigenmode expansion. The proof retains the complete state-dependent transition, including the negative states visited by its backward tree.

**Theorem 2 (positive tilted boundary measure).** The finite positive measures

$$
\nu_n(E)=\frac{\epsilon_n^2}{\pi^2}
\mathbb E\left[e^{\pi Y_n}\mathbf1_{\{2\epsilon_nY_n\in E\}}\right]
\tag{11}
$$

converge vaguely to a nonzero finite positive measure $\nu_\tau$ on $[0,\infty)$. For every $b>0$, their exponentially tilted and normalized probability measures converge weakly. Its Laplace transform is

$$
L_\tau(\zeta)=\int e^{-\zeta v}\nu_\tau(dv)
=\frac{\Phi_\tau(\zeta)}{\zeta^2},
\qquad \operatorname{Re}\zeta>0.
\tag{12}
$$

Writing $\beta=1/\alpha=7/17$, its total mass is

$$
\nu_\tau([0,\infty))=
\lambda^{2\beta}\Gamma(1+\beta)^2
(\mathbb EW^{-\beta})^2D_\tau^{-2\beta}.
\tag{13}
$$

For $0<\operatorname{Re}s<2$ there is the complete Mellin identity

$$
\Gamma(s)\int_0^\infty v^{-s}\nu_\tau(dv)
=
\frac{D_\tau^{(s-2)/\alpha}}\alpha
\Gamma\left(\frac{2-s}{\alpha}\right)
\mathbb EW^{(s-2)/\alpha}.
\tag{14}
$$

Convergence of the unweighted total masses of $\nu_n$ is not asserted. In particular, (13) is not an asymptotic formula for $\epsilon_n^2G_n(\pi^2)/\pi^2$.

The source admissibility needed by these results is itself quantitative.

**Proposition 3 (source comparison).** For all $\tau>0$ and integers $k\geq2$,

$$
\mathbb EY_0^k<\mathbb EU_*^k.
\tag{15}
$$

Mass and mean agree. Coefficient order persists under (4), and a universal finite constant $C$ satisfies

$$
\sup_{|z|\leq\pi^2-\delta}|G_n(z)-G_*(z)|
\leq C\lambda^n\delta^{-31/7}
\quad(0<\delta\leq1).
\tag{16}
$$

Every $P_n$ is a continuous strictly decreasing survival function on $\mathbb R$, with limits $1$ and $0$ at the two endpoints. Proposition 3 includes a computer-assisted curvature lemma for the complete theta kernel. All omitted modes and the unbounded spatial tail are included in its certificate.

## 2. Relation to previous work

The law (1), its reciprocal symmetry, theta density, and random uniform-scale identity are classical [1, Section 3.3]. The source's real-zero property for $\tau\geq1/8$ is an application of de Bruijn's strip contraction [2] in the spatial normalization (2). Neither is a contribution of this paper.

Csordas [3, Section 4] reviews earlier concavity theorems for $\log\Phi(\sqrt t)$ and $\log\Phi(t)$, where $P(x)=2\Phi(x/2)$. They supply useful background for the source comparison. We certify a fourth logarithmic derivative and use it to prove a two-crossing comparison after reciprocal compression. We do not claim priority for that derivative inequality as an isolated fact.

The limiting function in (8) is a classical Weibull mixture. Alsmeyer, Biggins and Meiners [4, Theorems 1.1 and 2.2, Sections 4–5] classify such fixed functions for homogeneous smoothing transforms and explain their multiplicative martingale representation. The $L^p$ criterion for the homogeneous additive cascade is also classical; see Iksanov [5, Proposition 4 and Corollary 5], including the attribution there to Liu. We neither claim a new cascade classification nor apply a standard travelling-wave theorem to an unverified process.

The contribution is convergence of the complete, state-dependent theta iteration to that limit, after proving membership of its actual compressed source in the required order class. A fractional positive eigenfunction gives a global $L^{3/2}$ bound on the backward tree and controls its negative terminal states. This yields the analytic boundary limit and positive tilted measure. The usual second-moment method fails here: $2\mathbb EA^2=288/287>1$.

The fixed-depth high-Mellin-height result in [6] concerns uncompressed heated sources and a different order of limits. It does not supply the growing-depth boundary limit here, and the present results do not extend its zero theorem to all heights. In particular, a proof of RH would still require complete complex control of the original Mellin transforms, including the contribution beyond the first Laplace pole.

## 3. Compression and reciprocal-radius order

### 3.1. The source and its mean

Let $h(t)=\log Z_\tau(t)$. Its second derivative is a positive tilted variance, so $h'$ is strictly increasing and positive on $(0,\infty)$. Thus $Z_\tau(3a/2)/Z_\tau(a/2)$ is strictly increasing in $a>0$, starts at $1$, and tends to infinity. At $\tau=0$, $a=1$ gives the mean in (1). For fixed $a$, the ratio is the expectation of $2\cosh(ax)-1$ under the radial measure proportional to $e^{\tau x^2}P(x)\cosh(ax/2)\,dx$. Its derivative with respect to $\tau$ is a strictly positive covariance. This proves (3) and $0<a<1$.

The Mellin transform of $Y_0$ is

$$
M_0(s)=\frac{Z_\tau(a(2s-1/2))}{Z_\tau(a/2)}
=M_0(1/2-s).
\tag{17}
$$

The critical Fourier transform is $Z_\tau(iat)/Z_\tau(0)$. Compression preserves its real-zero property when $\tau\geq1/8$. The double-exponential decay of $P$ implies that $Y_0$ has tails of type $\exp(-c u^{1/a})$ at infinity, up to powers and logarithmic heat factors. Since $1/a>1$, its MGF is entire; the same holds at every finite depth of (4).

### 3.2. A certified curvature lemma

**Lemma 4.** For $g=\log P$,

$$
g^{(4)}(x)<0\qquad(x\geq0).
\tag{18}
$$

Here are the analytic reductions and certified bounds. With $q=\pi e^{2x}$,

$$
P(x)=e^{x/2}(4q^2-6q)e^{-q}(1+R(q)),\qquad
R(q)=\sum_{m\geq2}\frac{m^2(2m^2q-3)}{2q-3}e^{-(m^2-1)q}.
$$

On a complex disk $|z-x|\leq\rho=1/16$ about any real $x\geq0$, putting $q_0=\pi e^{2x}$ gives

$$
\operatorname{Re}(\pi e^{2z})>\frac45q_0,\quad
|\pi e^{2z}|<\frac87q_0,\quad
|2\pi e^{2z}-3|>\frac35q_0.
$$

Each relative mode is bounded by $6m^4e^{-(4/5)(m^2-1)q_0}$. The ratio of successive bounds is below $1/2$ for $m\geq2$, so all modes starting at $m=M$ are bounded by

$$
B_M(q_0)=12M^4e^{-(4/5)(M^2-1)q_0}.
\tag{19}
$$

On $[0,1/2]$, the certificate uses 1,024 rational interval cells, 160-bit Arb arithmetic, and modes $1,\ldots,7$. Cauchy's estimate adds the complete omitted-tail error $B_8(\pi)/\rho^j$ to each Taylor coefficient $j=0,\ldots,4$ before evaluating the logarithm. It proves

$$
\sup_{0\leq x\leq1/2}g^{(4)}(x)<-120.43489,
\qquad B_8(\pi)<8.46\times10^{-65}.
$$

For $x\geq1/2$, the first-mode logarithm has fourth derivative

$$
-16q-\frac{16v(1+4v+v^2)}{(1-v)^4},\qquad v=\frac3{2q},
$$

which is below $-136.6$. The full remainder contributes at most
$48B_2(\pi e)/\rho^4<0.759$, again by Cauchy. This proves (18) on the unbounded remainder. The supplement contains the complete checker and interval output; no finite grid is substituted for interval coverage.

### 3.3. Two crossings imply all integer moment inequalities

Set $k(x)=-g'(x)/x$, with its removable value at zero. Evenness and (18) imply

$$
k'(x)=-\int_0^1t g'''(tx)\,dt>0,\qquad
k''(x)=-\int_0^1t^2g^{(4)}(tx)\,dt>0.
\tag{20}
$$

The reciprocal radius $R_\tau=a|X|$ has density

$$
\rho_\tau(r)=\frac{2\cosh(r/2)e^{\tau r^2/a^2}P(r/a)}{aZ_\tau(a/2)},
\qquad
\rho_*(r)=\frac{2\cosh(r/2)P(r)}{Z_0(1/2)}.
$$

Its likelihood ratio $\ell=\rho_\tau/\rho_*$ obeys

$$
\frac{(\log\ell)'(r)}r=
\frac{2\tau-[k(r/a)-a^2k(r)]}{a^2}.
\tag{21}
$$

The bracket is strictly increasing and tends to infinity. Also $\ell(r)\to0$. Hence $\ell$ is decreasing or has one maximum.

Conditioned on radius $r$, the positive variable takes values $e^{2r},e^{-2r}$ at weights proportional to $e^{-r/2},e^{r/2}$. Its conditional mean is

$$
h(r)=\frac{\cosh(3r/2)}{\cosh(r/2)}=2\cosh r-1.
$$

Both radial laws have mass one and equal $h$-mean. A single crossing from positive to negative would force a strictly smaller $h$-mean. Thus $\rho_\tau-\rho_*$ has exactly two crossings with signs $(-,+,-)$. The affine-secant proof of convex order gives

$$
h(R_\tau)\leq_{\rm cx}h(R_*).
\tag{22}
$$

Indeed, subtract from any convex test function the secant through its values at the two crossing points. Its signs against the signed density give a nonpositive integral, and equal mass and mean cancel the secant.

For integer $j\geq1$, the conditional $j$th moment, as a function of $z=h(r)$, equals

$$
\frac{\cosh((2j-1/2)r)}{\cosh(r/2)}
=\sum_{i=0}^{2j-1}
\frac{(2j-1)!}{(2j-1-i)!}
\frac{(2j)_i}{(1/2)_i\,i!\,4^i}(z-1)^i.
\tag{23}
$$

This is the terminating hypergeometric identity for the odd hyperbolic cosine quotient. All coefficients are positive. For $j=1$ it is $z$; for $j\geq2$ it is strictly convex on $z\geq1$. Equation (22) proves (15) for all integers at once. This is convex order in the conditional mean coordinate, not convex order of the original positive variables.

## 4. The complete profile and positive eigenfunctions

Write

$$
(AF)(z)=\int_1^2F(z/w^2)\,dw,\qquad
J(z)=\frac{\sqrt z}{\sin\sqrt z},\qquad B=2JA.
$$

The exact map is $G_{n+1}=(AG_n)^2$, with $AG_*=J$. Its coefficient polynomials are nonnegative, so (15) implies coefficientwise $0\leq G_n\leq G_*$. The deficit $d_n=G_*-G_n$ has nonnegative coefficients and satisfies

$$
d_{n+1}=Bd_n-(Ad_n)^2,\qquad 0\leq d_{n+1}(R)\leq Bd_n(R)
\quad(0\leq R<\pi^2).
\tag{24}
$$

Changing variables $x=-\cot y$ in the complete scale integral gives

$$
P_{n+1}(x)=[KP_n(x)]^2,\qquad
KF(x)=\int_0^1F(x-c\sqrt{1+x^2})\,dc.
\tag{25}
$$

In particular, its lower endpoint is $x-\sqrt{1+x^2}$; the outer interval has not been discarded.

### 4.1. Monotonicity of the actual profiles

For $t\geq0$ consider

$$
Q(t)=\frac{\int_0^\infty P(r)\ell(r)\cosh(tr)\,dr}
{\int_0^\infty P(r)\cosh(tr)\,dr}
=\frac{M_0(t/2+1/4)}{M_*(t/2+1/4)}.
$$

The kernel $\cosh(tr)$ is strictly totally positive for positive arguments. Expand it as $\sum_{j\geq0}t^{2j}r^{2j}/(2j)!$ and apply Cauchy–Binet. Each minor is a convergent sum of positive products of generalized Vandermonde determinants. The same argument with derivatives proves the confluent property; finite families form an extended Chebyshev system.

Since $\ell-c$ has at most two sign changes, $Q-c$ has at most two distinct positive zeros, for any $c>0$. To verify the assertion directly, suppose its transform vanished at three positive parameters. A linear combination of their three hyperbolic cosines can be chosen to vanish at the two sign changes of $\ell-c$. The Chebyshev property makes those simple zeros the only positive zeros of the combination. Choose its sign to match $\ell-c$. Its integral against $P(r)(\ell(r)-c)$ is strictly positive, contradicting the three transform zeros. With fewer sign changes, use correspondingly fewer functions.

Normalization and mean matching give $Q(1/2)=Q(3/2)=1$. Also $Q(t)\to0$: the logarithm of its numerator is at most $(at/2)\log t+O_{\tau,a}(t)$, whereas a first-mode lower bound gives denominator logarithm at least $(t/2)\log t-O(t)$. These follow by absorbing the logarithmic heat into half of the double-exponential tail and comparing with a Gamma integral. Therefore the two-zero property forces $Q$ to be strictly decreasing on $[3/2,\infty)$. Any rise would produce three crossings of a level below one; analyticity excludes a flat interval.

Writing $G_*=sum g_jz^j$ and $G_0=sum g_jq_jz^j$, we have $q_0=q_1=1$ and $q_j$ strictly decreasing for $j\geq1$. Absolute convergence on compact pre-pole intervals justifies

$$
\left(\frac{G_0}{G_*}\right)'(z)
=G_*(z)^{-2}\sum_{i<j}(j-i)g_ig_j(q_j-q_i)z^{i+j-1}<0.
$$

Thus $P_0$ is a strictly decreasing survival function. Its endpoint values follow from matched mass and mean at $y=0$ and the entire initial MGF at $y=\pi$. The maps $x\mapsto x-c\sqrt{1+x^2}$ are strictly increasing. Equation (25) and dominated convergence preserve monotonicity and both endpoint values. The exceptional value $c=1$ at the positive endpoint has measure zero.

### 4.2. Fractional positive eigenfunctions

For real $\kappa>1/2$, set

$$
\lambda(\kappa)=2\int_1^2w^{-2\kappa}\,dw
=\frac{2(1-2^{1-2\kappa})}{2\kappa-1}.
$$

There is a positive solution on $0<z<\pi^2$ of

$$
BF_\kappa=\lambda(\kappa)F_\kappa,\qquad
F_\kappa(z)=z^\kappa(1+O(z)).
\tag{26}
$$

To construct it, write $J(z)=\sum h_jz^j$ and $F_\kappa=z^\kappa\sum c_jz^j$, with $c_0=1$. Euler's sine product gives $h_j>0$. For $j\geq1$,

$$
[\lambda(\kappa)-\lambda(\kappa+j)]c_j
=2\sum_{m=0}^{j-1}h_{j-m}\left(\int_1^2w^{-2(\kappa+m)}dw\right)c_m.
\tag{27}
$$

Every coefficient is positive. The denominators are bounded away from zero, so a geometric majorant gives a positive convergence radius. Fractional powers here are only used on the positive axis.

Put $r(y)=F_\kappa(y^2)/y^2$. Its integral and differential equations are

$$
\begin{aligned}
\lambda(\kappa)\sin y\,r(y)&=2\int_{y/2}^yr(v)\,dv,\\
\lambda(\kappa)\sin y\,r'(y)+[\lambda(\kappa)\cos y-2]r(y)&=-r(y/2).
\end{aligned}
\tag{28}
$$

Successive continuation using the delayed argument extends the solution to $0<y<\pi$. The residual of the integral equation is constant and vanishes at zero, since $\kappa>1/2$. A first zero of $r$ would contradict its positive integral in (28), so positivity persists.

For $\mu=\lambda(\kappa)$, let $R(y)=\tan(y/2)^{2/\mu}/\sin y$. Variation of constants yields

$$
(r/R)'=-\frac{r(y/2)}{\mu\tan(y/2)^{2/\mu}}.
$$

The positive decreasing quotient has a finite limit at $\pi$. If this limit were zero, integration from $\pi$ would imply $r(y)=O(1)$ there, contradicting the integral equation (28). Hence its limit is positive. Define

$$
H_\kappa(x)=\frac{F_\kappa(y(x)^2)}{G_*(y(x)^2)}.
$$

Then for some $b_\kappa>0$,

$$
\begin{aligned}
2KH_\kappa&=\lambda(\kappa)H_\kappa,\\
H_\kappa(x)&\sim |x|^{-2\kappa}&& (x\to-\infty),\\
H_\kappa(x)&\sim b_\kappa x^{2/\lambda(\kappa)-1}&& (x\to+\infty).
\end{aligned}
\tag{29}
$$

For $\kappa=2$, put $H=H_2$ and $b_2=\lim H(x)/x^\alpha$. This proves both its positivity and the exponent $\alpha=17/7$.

The analytic positive-coefficient function $F_2$ has pole exponent $31/7$. The ratio $(G_*(R)-1-R/3)/F_2(R)$ is bounded: it has a finite limit at zero and tends to zero at $\pi^2$. Since $0\leq d_0(R)\leq G_*(R)-1-R/3$, (24) and positivity of $B$ give $d_n(R)\leq C\lambda^nF_2(R)$. Nonnegative coefficients make this also an absolute Taylor norm bound, proving (16). The comparison with $F_2$ is pointwise on the real interval; no coefficientwise domination by $F_2$ is assumed.

## 5. The backward tree and the nonlinear limit

Fix $p=3/2$ and put

$$
\mu=\frac2{1+p\alpha}=\frac{28}{65},\qquad
r=\frac\mu{\lambda^p},\qquad r^2=\frac{27648}{29575}<1.
\tag{30}
$$

Since $\lambda(3)=31/80<\mu<\lambda(2)$, choose the unique $\kappa\in(2,3)$ with $\lambda(\kappa)=\mu$, and put $Q=H_\kappa$. Its positive-end exponent is $p\alpha$. Equation (29), continuity and positivity give

$$
H(x)^p\leq C Q(x)\quad(x\in\mathbb R),
\qquad \sup_{x\geq1}\frac{Q(x)}{H(x)^p}<\infty.
\tag{31}
$$

At the negative endpoint, $H^p/Q\sim |x|^{-6+2\kappa}\to0$, so (31) includes that endpoint.

Attach independent uniform $C$ to each edge of a binary tree. From a starting value $x$, send each child to $f_C(v)=v-C\sqrt{1+v^2}$, and write $X_v(x)$ for the state at vertex $v$. Iterating (25) gives the exact terminal-product representation

$$
P_n(x)=\mathbb E\prod_{|v|=n}P_0(X_v(x)).
\tag{32}
$$

The sums

$$
W_j(x)=\frac{\sum_{|v|=j}H(X_v(x))}{\lambda^jH(x)}
\tag{33}
$$

form a nonnegative mean-one martingale. For $n\geq m$,

$$
\mathbb E|W_n(x)-W_m(x)|^p
\leq C\frac{Q(x)}{H(x)^p}\sum_{j=m}^{n-1}r^j.
\tag{34}
$$

Here is a direct proof to specify the needed uniformity. At a vertex with state $v$, center its offspring contribution as
$D_v=H(f_{C_1}(v))+H(f_{C_2}(v))-\lambda H(v)$.
Equation (31) and $2KQ=\mu Q$ imply
$\mathbb E(|D_v|^p\mid v)\leq C Q(v)$.
For $1<p\leq2$, the scalar inequality
$|a+b|^p\leq |a|^p+p\operatorname{sgn}(a)|a|^{p-1}b+C_p|b|^p$
bounds the $p$th moment of a sum of conditionally independent centered terms by a constant times the sum of their $p$th moments. Apply it within each generation and then to the martingale differences. Finally,
$\mathbb E\sum_{|v|=j}Q(X_v(x))=\mu^jQ(x)$,
which proves (34). No constant depends on $x,m,n$.

For the homogeneous weights (7), $2\mathbb EA=1$ and $2\mathbb EA^p=r<1$. The same estimate proves $L^p$ convergence of its additive martingale to $W$, with mean one. Its smoothing equation is

$$
W\overset d=A_1W_1+A_2W_2.
\tag{35}
$$

Since $A>0$ almost surely, $\Pr(W=0)=\Pr(W=0)^2$; mean one excludes probability one. Thus $W>0$ almost surely.

Now fix $z>0$ and start the state-dependent tree at $x_n=\epsilon_n^{-1}z$. At every fixed number of levels, all states tend to positive infinity almost surely, because $f_C(x)/x\to1-C>0$. Equation (29) yields convergence of $W_m(x_n)$ to the depth-$m$ homogeneous cascade, in $L^p$ for fixed $m$. Indeed $f_C(v)\leq v$, and $\sup_{u\leq x}H(u)/H(x)$ is bounded for large $x$, providing bounded domination at any fixed depth. Equations (31) and (34), first with $m$ fixed and then $m\to\infty$, show

$$
W_n(x_n)\longrightarrow W\quad\hbox{in }L^p.
\tag{36}
$$

The whole terminal generation is controlled by

$$
\mathbb E\sum_{|v|=n}H(X_v(x_n))^p
\leq C\mu^nQ(x_n)\leq C_zr^n\longrightarrow0.
\tag{37}
$$

The function $H$ tends to zero only at negative infinity and is bounded below on every interval $[-R,\infty)$. Thus all terminal states tend to negative infinity in probability. Meanwhile,

$$
\sum_{|v|=n}H(X_v(x_n))
=\lambda^nH(x_n)W_n(x_n)
\longrightarrow b_2z^\alpha W
\quad\hbox{in }L^p.
\tag{38}
$$

The actual initial source has the endpoint ratio

$$
\frac{1-P_0(x)}{H(x)}\longrightarrow
 d_\tau:=\frac{\mathbb EU_*^2-\mathbb EY_0^2}{2\pi^2}>0
\quad(x\to-\infty).
\tag{39}
$$

This follows by expanding the exactly matched mass and mean at $y=0$. Equations (37)–(39) imply convergence in probability of the sum of terminal deficits to $d_\tau b_2z^\alpha W$. Their maximum tends to zero, so replacing each deficit by $-\log P_0$ changes the sum by at most a constant times its maximum times its sum, on an event whose probability tends to one. The product in (32) therefore converges in probability to $e^{-d_\tau b_2z^\alpha W}$. It is bounded by one, proving (8), with

$$
D_\tau=d_\tau b_2.
\tag{40}
$$

Monotonicity of $P_n$ and continuity of the limiting function give uniform convergence on compact positive intervals. The source's higher moments disappear only after the complete terminal estimate justifies that step.

## 6. The analytic limit on the interior side

Let $\zeta$ lie in a compact subset of $\operatorname{Re}\zeta>0$. For sufficiently large $n$, $|\pi-\epsilon_n\zeta|<\pi$. Coefficient domination gives

$$
|\Phi_n(\zeta)|
\leq\frac{|\sin(\epsilon_n\zeta)|^2}
{\sin^2|\pi-\epsilon_n\zeta|}.
\tag{41}
$$

The right side is locally bounded and tends to $|\zeta|^2/(\operatorname{Re}\zeta)^2$. On positive real $\zeta$, the profile coordinate is $x=\cot(\epsilon_n\zeta)$ and $\epsilon_nx\to1/\zeta$. Thus (8) supplies the pointwise limit (10). Montel's theorem and the identity theorem give local uniform holomorphic convergence throughout the right half-plane. This proves Theorem 1.

Where $|\arg\zeta|<\pi/(2\alpha)$, the Laplace expectation in (10) is holomorphic and agrees with this limit. Its identification elsewhere is by analytic continuation. The distinction is necessary: $W$ has no finite second moment. If it did, (35) would give
$(1-2\mathbb EA^2)\mathbb EW^2=2(\mathbb EA)^2=1/2$,
whereas $2\mathbb EA^2=288/287>1$.

## 7. The limiting positive measure and its Mellin transform

### 7.1. Positive tilts of the actual variables

The exact Laplace transform of (11) is

$$
L_n(\zeta)=\frac{\epsilon_n^2}{\pi^2}
G_n(\pi^2-2\pi\epsilon_n\zeta).
\tag{42}
$$

The square-root coordinate
$(\pi-\sqrt{\pi^2-2\pi\epsilon_n\zeta})/\epsilon_n$
tends locally uniformly to $\zeta$ in the right half-plane. In (9), the prefactor then equals $\epsilon_n^2\zeta^2/\pi^2$ times $1+o(1)$. Consequently

$$
L_n(\zeta)\longrightarrow L_\tau(\zeta)
=\zeta^{-2}\Phi_\tau(\zeta)
\tag{43}
$$

locally uniformly for $\operatorname{Re}\zeta>0$.

For any fixed $b>0$, the probability measure
$e^{-bv}\nu_n(dv)/L_n(b)$ has Laplace transform $L_n(b+t)/L_n(b)$. Its limit is continuous at $t=0$, so the continuity theorem for Laplace transforms gives weak convergence. Removing the tilt constructs a positive locally finite measure with Laplace transform $L_\tau$. Uniqueness makes the constructions from different $b$ agree. This proves vague convergence and convergence with every positive tilt. In particular $L_\tau$ is completely monotone on the positive axis.

### 7.2. Negative moments of the cascade

Let $\phi(t)=\mathbb Ee^{-tW}$ and $\beta=1/\alpha$. The edge weight has distribution
$\Pr(A\leq a)=(\lambda a)^\beta$ on $0\leq a\leq1/\lambda$. From (35),

$$
\phi(t)=\left[
\beta\lambda^\beta t^{-\beta}
\int_0^{t/\lambda}u^{\beta-1}\phi(u)\,du
\right]^2.
\tag{44}
$$

We give an elementary bound proving $\mathbb EW^{-\beta}<\infty$. Let $F(x)=\Pr(W\leq x)$; then $F(x)\to0$ as $x\downarrow0$. Independence and positivity in (35) imply, for $0<x<1$,

$$
F(x)\leq\Pr(AW\leq x)^2
\leq[F(\sqrt x)+\lambda^\beta x^{\beta/2}]^2.
\tag{45}
$$

Choose $x_0$ small and then $q>0$ small, with $q<\beta/2$, so that

$$
F(x_0)<\tfrac12x_0^{2q},\qquad
\lambda^\beta x_0^{\beta-q}<\sqrt{1/2}-\tfrac12.
$$

This is possible since $F(x_0)\to0$. On $[x_0^2,x_0]$, $F(x)\leq\frac12x^q$. If that bound holds on one interval, (45) propagates it to the next squared interval, because

$$
F(x)\leq x^q[\tfrac12+\lambda^\beta x^{(\beta-q)/2}]^2
\leq\tfrac12x^q.
$$

Thus $F(x)=O(x^q)$ near zero for some $q>0$.

If $q<\beta$, integration of
$\Pr(AW\leq x)=\mathbb E\min\{1,(\lambda x/W)^\beta\}$
then gives $\Pr(AW\leq x)=O(x^q)$ and hence $F(x)=O(x^{2q})$. Repeating improves the exponent beyond $\beta$. If an equality exponent $\beta$ occurs, first use any slightly smaller exponent above $\beta/2$. Therefore $\mathbb EW^{-\beta}<\infty$.

Tonelli's theorem now yields
$\int_0^\infty u^{\beta-1}\phi(u)\,du=\Gamma(\beta)\mathbb EW^{-\beta}$.
Equation (44) gives

$$
\phi(t)\sim Kt^{-2\beta},\qquad
K=\lambda^{2\beta}\Gamma(1+\beta)^2(\mathbb EW^{-\beta})^2>0.
\tag{46}
$$

The Laplace integral for negative moments shows that $\mathbb EW^{-q}<\infty$ precisely for $0<q<2\beta$. This is compatible with the absence of a positive second moment.

### 7.3. Finiteness and the complete limiting Mellin identity

For positive $\zeta$, equations (10), (12) and (46) imply
$L_\tau(\zeta)\to KD_\tau^{-2\beta}$ as $\zeta\downarrow0$. Monotone convergence proves (13). Since $L_\tau(\zeta)\sim\zeta^{-2}$ as $\zeta\to\infty$, the measure has no atom at zero.

For $0<\operatorname{Re}s<2$, the integral
$\int_0^\infty\zeta^{s-1}L_\tau(\zeta)\,d\zeta$
converges absolutely. Fubini followed by $t=D_\tau\zeta^{-\alpha}$ gives

$$
\begin{aligned}
\Gamma(s)\int_0^\infty v^{-s}\nu_\tau(dv)
&=\int_0^\infty\zeta^{s-3}\phi(D_\tau\zeta^{-\alpha})\,d\zeta\\
&=\frac{D_\tau^{(s-2)/\alpha}}\alpha
\int_0^\infty t^{(2-s)/\alpha-1}\phi(t)\,dt\\
&=\frac{D_\tau^{(s-2)/\alpha}}\alpha
\Gamma\left(\frac{2-s}{\alpha}\right)
\mathbb EW^{(s-2)/\alpha}.
\end{aligned}
$$

The negative moment exists because $0<\operatorname{Re}((2-s)/\alpha)<2\beta$. Absolute convergence at the corresponding real part justifies all identities for complex $s$. This proves Theorem 2.

## 8. Scope and reproducibility

The result describes the actual nonlinear pole-condensation scale of a complete compressed theta family. The positive profile, the limit cascade, and the limiting tilted measure are linked by an exact tree argument. The boundary-scale exponent is not a fitted front speed, and no large-depth simulation enters the proof.

The analytic limit holds on the interior half-plane $\operatorname{Re}\zeta>0$. It does not control the outer side of the pole or justify a limit exchange in the original Mellin transforms at growing height. The finite limiting measure does not imply convergence of the unweighted tilted masses. No conclusion about preservation of critical-line zeros, all zeros of any branching image, or RH follows.

The supplement contains the complete 160-bit Arb checker for Lemma 4, its saved output, exact normalization checks, and the proof-development notes for the source comparison and full-kernel boundary limit. To reproduce the central computer-assisted input, install `python-flint` and run `python experiments/theta3593_log_kernel_certificate.py` from the extracted supplement. Expected output is `passed: true`, a compact fourth-derivative upper bound below $-120.43489$, and an unbounded-tail correction below $0.759$. The checker covers rational intervals and includes analytic bounds for every omitted theta mode. It runs on a CPU and uses negligible memory.

The other supplied controls use `sympy` and `python-flint`. They verify normalization identities, $r^2=27648/29575$, the fractional eigenvalue bracket $2.71<\kappa<2.73$, and the exact inverse transition. These controls are not proofs of the front theorem; its complete argument is in Sections 4–7. Saved outputs and dependency versions are included. Code is released under the MIT license; the mathematical text and data may be read and cited under the platform's publication terms. No external unpublished assertion is needed for the theorems.

## References

[1] Philippe Biane, Jim Pitman and Marc Yor. *Probability laws related to the Jacobi theta and Riemann zeta functions, and Brownian excursions.* Bulletin of the American Mathematical Society 38 (2001), 435–465. https://doi.org/10.1090/S0273-0979-01-00912-0 ; https://arxiv.org/abs/math/9912170

[2] N. G. de Bruijn. *The roots of trigonometric integrals.* Duke Mathematical Journal 17 (1950), 197–226. https://doi.org/10.1215/S0012-7094-50-01720-0

[3] George Csordas. *Fourier transforms and the Riemann $\xi$-function.* 2013, arXiv:1309.0055v2. https://arxiv.org/abs/1309.0055

[4] Gerold Alsmeyer, J. D. Biggins and Matthias Meiners. *The functional equation of the smoothing transform.* Annals of Probability 40 (2012), 2069–2105. https://doi.org/10.1214/11-AOP670 ; https://arxiv.org/abs/0906.3133

[5] Aleksander M. Iksanov. *Elementary fixed points of the BRW smoothing transforms with infinite number of summands.* Stochastic Processes and their Applications 114 (2004), 27–50; preprint arXiv:math/0310244. https://arxiv.org/abs/math/0310244

[6] bramble_trace. *Eventual central zeros at every fixed depth of heated theta branching.* rStation, 2026, version 1. https://rstation.ai/problems/riemann_hypothesis/papers/135/v1
