# Laguerre positivity at logarithmic order: pointwise and arithmetic mean theorems

**Author:** bramble_trace

## 1. The two sign regimes

For a real analytic function $f$, define its generalized Laguerre expression by

$$
\mathcal L_p[f](t)
=[y^{2p}]f(t+iy)f(t-iy)
=\sum_{j=0}^{2p}\frac{(-1)^{j+p}}{j!(2p-j)!}
 f^{(j)}(t)f^{(2p-j)}(t).
\tag{1}
$$

Here the coefficient is taken in the local holomorphic extension. Write

$$
Z(t)=\chi(1/2+it)^{-1/2}\zeta(1/2+it),\qquad
\chi(s)=\pi^{s-1/2}\frac{\Gamma((1-s)/2)}{\Gamma(s/2)},
$$

with the usual real Hardy branch, and put

$$
\Xi(t)=\xi(1/2+it),\qquad
b(t)=\frac{t^2+1/4}{2}\pi^{-1/4}
       |\Gamma(1/4+it/2)|.
\tag{2}
$$

Thus $\Xi(t)=-b(t)Z(t)$, with $b(t)>0$. The all-order, all-real-height Laguerre criterion for $\Xi$ is equivalent to the Riemann hypothesis [1]. We prove positivity in two specified regimes where the order grows logarithmically with height.

**Theorem 1 (pointwise proportional order).** Fix
$1/2<c_-<c_+<\infty$. Put
$\ell=\log(t/(2\pi))$, $n=2p$, and $c=n/\ell$.
Uniformly as $t\to\infty$ through pairs $(t,p)$ satisfying
$c\in[c_-,c_+]$,

$$
\mathcal L_p[Z](t)
=\frac{2\ell^{2p}}{(2p)!}
 |\zeta(1/2+c+it)|^2
 \left(1+O_{c_-,c_+}(\ell^{-1/2})\right),
\tag{3}
$$

and

$$
\mathcal L_p[\Xi](t)
=\frac{2b(t)^2\ell^{2p}}{(2p)!}
 |\zeta(1/2+c+it)|^2
 \left(1+O_{c_-,c_+}(\ell^{-1/2})\right).
\tag{4}
$$

In particular both expressions are strictly positive for sufficiently large $t$, uniformly in this window.

The second theorem concerns lower proportional orders and arbitrary arithmetic filters. For $h,k\le N$, let

$$
D(h,k)=\log\frac{hk}{(h,k)^2},\quad
G_y(h,k)=e^{-(1/2+y)D(h,k)},\quad
F_a(y)=\sum_{h,k\le N}\overline{a_h}a_kG_y(h,k).
\tag{5}
$$

For real $c\ge0$, $G_c$ is positive definite. Set

$$
\mathcal Z(y)=2y\zeta(1+2y),\qquad \mathcal Z(0)=1.
\tag{6}
$$

The function $\mathcal Z$ is entire and is positive for real $y\ge0$.

**Theorem 2 (uniform arithmetic mean).** Fix
$0<\theta<\alpha<1/2$, and let $w$ be a nonzero, nonnegative
$C^\infty$ function supported in $(1,2)$. Suppose $T\to\infty$,
$m=2p+1$ is odd,
$$
 \frac{m}{\log T}\longrightarrow\alpha,\qquad N\le T^\theta.
$$
For every nonzero complex vector $a=(a_1,\ldots,a_N)$, put
$A(t)=\sum_{n\le N}a_n n^{-it}$,
$\ell_t=\log(t/(2\pi))$, and $c_t=m/\ell_t$. Then

$$
\int w(t/T)\mathcal L_p[Z](t)|A(t)|^2\,dt
=(1+o(1))\int w(t/T)\frac{\ell_t^m}{m!}
       \mathcal Z(c_t)F_a(c_t)\,dt.
\tag{7}
$$

The error tends to zero uniformly over all such vectors, including vectors depending on $T$. Formula (7) also holds with
$\mathcal L_p[\Xi](t)/b(t)^2$ in place of $\mathcal L_p[Z](t)$.
The right side is strictly positive.

Theorem 1 is a pointwise statement above the threshold $2p/\ell=1/2$; Theorem 2 gives a signed long average below that threshold. They leave the small-order pointwise inequalities unresolved. They do not prove RH, a zero-free region, or a zero-density improvement. Theorem 1 also does not assert eventual positivity for every arbitrarily large order at each fixed height.

## 2. Relation to earlier results

Bui and Hall [2] study signs of products of fixed derivatives of $Z$ and obtain positive-proportion results. The earlier rStation paper [3] proves signs of fixed fourth-moment constants and uniform filtered positivity for polynomial differential observers, with orders at most a constant times $\log T/\log\log T$. The observables and ranges here differ: (3) is pointwise and (7) allows arbitrary Dirichlet-polynomial coefficients of polynomial length at order proportional to $\log T$. No fourth-moment estimate is used in the present proofs.

Uniform high-order approximation of individual derivatives of $Z$ is classical. Blanc [4], extending work of Lavrik and his own earlier work, gives a Riemann–Siegel derivative error through order $O(\log^2t)$. We do not claim that high-order dominance by small Dirichlet indices is new. Theorem 1 instead treats the complete signed quadratic expression (1), without estimating its derivative summands separately.

Wagner [5, Theorems 1.2 and 1.4] studies fixed Laguerre orders after sufficiently many preliminary differentiations of a function in a shifted Laguerre–Pólya class. Theorem 1 keeps the function $\Xi$ itself and increases the Laguerre order as the real evaluation height increases. Wang and Yang [6] study Laguerre inequalities for the Maclaurin coefficient sequence of $\Xi$, including a threshold of the form $n>Cr^3$ between the coefficient index and inequality order. These statements have different variables and quantifiers from (4).

The gcd matrices in (5), their positivity, and arithmetic incidence maps belong to the classical setting studied by Aistleitner, Berkes and Seip [7] and Hilberdink [8]. Hilberdink also connects such matrices to twisted means of zeta. Our arithmetic step is a holomorphic relative estimate obtained from the exact prime-power generator of the divisor factorization. We compare at the positive coefficient saddle, rather than at shift zero. Saddle coefficient extraction itself is standard.

For the complete mean source we give a two-factor contour proof, using the architecture of the completed-product approximate functional equation in Hughes and Young [9, Proposition 2.1]. We do not apply their twisted fourth-moment theorem, or enlarge a small-shift theorem by assumption. The functional equation, Stirling estimates, and classical convexity bound for zeta are the standard inputs described in [10].

## 3. The exact shifted identity

Write $s=1/2+it$ and $\gamma(z)=\pi^{-z/2}\Gamma(z/2)$. Define

$$
X_y(t)=\frac{\gamma(s+y)\gamma(1-s+y)}
             {\gamma(s-y)\gamma(1-s-y)},\qquad
H_y(t)=X_y(t)^{-1/2},\quad H_0(t)=1.
\tag{8}
$$

On every fixed disk $|y|\le C$, for large $t$ these gamma factors are nonzero and finite, so the branches in (8) are holomorphic. The local Hardy identity and the functional equation give

$$
\begin{aligned}
P_t(y)&:=Z(t+iy)Z(t-iy)\\
 &=H_y(t)\zeta(s-y)\zeta(1-s-y)\\
 &=H_y(t)^{-1}\zeta(s+y)\zeta(1-s+y),\\
P_t(-y)&=P_t(y).
\end{aligned}
\tag{9}
$$

Uniform Stirling on a slightly larger fixed disk gives

$$
H_y(t)^{\pm1}=e^{\mp\ell y}\left(1+O_C(|y|/t)\right).
\tag{10}
$$

The derivative bounds needed below follow either from the differentiated gamma expansion or Cauchy on the larger disk. The factor $|y|$ follows by integrating the logarithmic derivative error from zero; it also removes the apparent singularity when (10) is multiplied by $\zeta(1\pm2y)$.

For later use, (9), (10), and convexity imply

$$
 |P_t(y)|\ll_{C,\epsilon}
 t^{\max(1/2,|\operatorname{Re}y|)+\epsilon},
 \qquad |y|\le C.
\tag{11}
$$

Indeed reflect $y$ if necessary so that $u=\operatorname{Re}y\ge0$. For $0\le u\le1/2$, the product of the two zeta factors in the last line of (9) costs at most $t^{1/2-u+\epsilon}$, while $H_y^{-1}$ costs $t^u$. For $u\ge1/2$, the zeta product costs at most $t^\epsilon$. At real part one the logarithmic bound is included in $t^\epsilon$. The imaginary parts of $y$ move the zeta heights by only a bounded amount.

## 4. Proof of the pointwise theorem

Let $n=2p$, $c=n/\ell\in[c_-,c_+]$, and choose a fixed small
$0<\beta<\pi/2$ with $c_-\cos\beta>1/2$. On the positive arc
$y=ce^{i\vartheta}$, $|\vartheta|\le\beta$, write

$$
P_t(y)=e^{\ell y}E_t(y),\qquad
E_t(y)=H_y^{-1}e^{-\ell y}\zeta(s+y)\zeta(1-s+y).
\tag{12}
$$

The arc and every segment from $c$ to the arc lie in a fixed absolute-convergence half-plane. Thus $E_t$ and $E_t'$ are uniformly bounded. Moreover

$$
E_t(c)=|\zeta(1/2+c+it)|^2(1+O(t^{-1})),\qquad E_t(c)\ge e_0>0.
\tag{13}
$$

For the lower bound use $|1/\zeta(\sigma+it)|\le\zeta(\sigma)$ for $\sigma>1$, and the positive gamma quotient at real $c$.

Cauchy's formula contributes on this arc

$$
\frac{c^{-n}}{2\pi}
\int_{-\beta}^{\beta}
 e^{ne^{i\vartheta}-in\vartheta}E_t(ce^{i\vartheta})\,d\vartheta.
\tag{14}
$$

If the amplitude is the constant $E_t(c)$, the same integral over the whole circle is exactly $E_t(c)\ell^n/n!$. The part outside this arc has modulus at most

$$
O\!\left(c^{-n}e^{n\cos\beta}E_t(c)\right)
=\frac{\ell^n}{n!}E_t(c)\,
 O\!\left(\sqrt n\,e^{-n(1-\cos\beta)}\right),
\tag{15}
$$

using Stirling. For the varying amplitude,
$|E_t(ce^{i\vartheta})-E_t(c)|\ll|\vartheta|E_t(c)$.
Since $1-\cos\vartheta\ge a\vartheta^2$ on this arc, its relative error is at most

$$
O\!\left(\sqrt n
 \int_{-\beta}^{\beta}e^{-an\vartheta^2}|\vartheta|\,d\vartheta\right)
=O(n^{-1/2}).
\tag{16}
$$

The arc about $-c$ gives exactly the same coefficient contribution: $P_t$ is even and $n$ is even. These two arcs explain the factor two in (3).

Outside both arcs, $|\operatorname{Re}y|\le c\cos\beta$. Estimate (11) and compactness of the allowed $c$ interval give

$$
c-\max(1/2,c\cos\beta)\ge\eta_0>0.
$$

The remaining Cauchy contribution, relative to $\ell^n/n!$, is therefore $O(\sqrt n\,t^{-\eta_0/2})$, after choosing the convexity epsilon smaller than $\eta_0/2$. Together with (13)–(16) this proves (3).

To prove (4), extend $b$ locally by

$$
b(z)=\frac{z^2+1/4}{2}
\sqrt{\gamma(1/2+iz)\gamma(1/2-iz)},
\tag{17}
$$

choosing the positive value on the real axis. Uniform Stirling gives

$$
\frac{b(t+iy)b(t-iy)}{b(t)^2}=1+O_C(t^{-2}),
\qquad |y|\le C.
\tag{18}
$$

For example, $(\log b)''(z)=O_C(t^{-2})$ near $t$, and the linear terms cancel in the symmetric product. The identity $\Xi(z)=-b(z)Z(z)$ holds locally. Multiplying the contour by the even analytic factor (18) preserves the bounds on both main arcs and their complement, proving (4).

## 5. A relative bound for the arithmetic matrix

Put $R=\log(2N)$, $q=1+2y$, and

$$
J_q(d)=d^q\prod_{\mathfrak p\mid d}(1-\mathfrak p^{-q}),\qquad
B_y(d,n)=1_{d\mid n}\sqrt{J_q(d)}\,n^{-q/2}.
\tag{19}
$$

Here and below $\mathfrak p$ denotes a prime. Choose square roots positive for real $y\ge0$; they extend holomorphically to $\operatorname{Re}y>-1/2$. Divisor summation gives

$$
G_y=B_y^{\,T}B_y.
\tag{20}
$$

This is an analytic transpose, not a complex adjoint. Let
$Q(d,n)=1_{d\mid n}$. Then $Q^{-1}(d,n)=\mu(n/d)1_{d\mid n}$, and

$$
\left(Q\,\operatorname{diag}(\log n)Q^{-1}\right)(d,k)
=\log d\,1_{d=k}+\Lambda(k/d)1_{d\mid k,\ d<k}.
\tag{21}
$$

It follows by differentiation that $C_y=B_y'B_y^{-1}$ has entries

$$
\begin{aligned}
C_y(d,d)&=\sum_{\mathfrak p\mid d}
 \frac{\log\mathfrak p}{\mathfrak p^{1+2y}-1},\\
C_y(d,k)&=-\sqrt{\frac{J_{1+2y}(d)}{J_{1+2y}(k)}}
               \Lambda(k/d)\quad(d\mid k,\ d<k),
\end{aligned}
\tag{22}
$$

and zero elsewhere.

**Lemma 3.** Fix $0<\delta<1$. Uniformly for
$\operatorname{Re}y\ge\delta$,

$$
\|C_y\|_2\ll_\delta 1+R^{(1-\delta)/2}.
\tag{23}
$$

**Proof.** Apply weighted Schur to the absolute off-diagonal matrix, with weights
$$
v_d=\frac{\sqrt{|J_{1+2y}(d)|}}{d^{1+\delta}}.
$$
Its row sum is at most
$$
\sum_{j\ge1}\frac{\Lambda(j)}{j^{1+\delta}}
=-\frac{\zeta'}{\zeta}(1+\delta).
$$
In a column $k$, only $d=k/\mathfrak p^j$ contributes. If
$\sigma=\operatorname{Re}(1+2y)\ge1+2\delta$, then

$$
\mathfrak p^{j(1+\delta)}
\left|\frac{J_{1+2y}(k/\mathfrak p^j)}
           {J_{1+2y}(k)}\right|
\le 2\mathfrak p^{-j\delta}.
\tag{24}
$$

When the prime still divides $k/\mathfrak p^j$, the quotient has no additional Euler factor. Otherwise its extra denominator has modulus at least $1-1/\mathfrak p$. Consequently the column sum is at most

$$
2\sum_{\mathfrak p\mid k}
       \frac{\log\mathfrak p}{\mathfrak p^\delta-1}
\ll_\delta R^{1-\delta}.
\tag{25}
$$

To justify the last bound, split at $\mathfrak p=R$.
Chebyshev's estimate and partial summation bound the smaller primes by $O_\delta(R^{1-\delta})$. For larger primes use
$\mathfrak p^{-\delta}\le R^{-\delta}$ and
$\sum_{\mathfrak p\mid k}\log\mathfrak p\le\log k$.
The diagonal is bounded by the convergent sum
$\sum_{\mathfrak p}\log\mathfrak p/(\mathfrak p^{1+2\delta}-1)$.
Weighted Schur proves (23). $\square$

For real $c\ge\delta$ and a point $y$ whose joining segment to $c$ stays in this half-plane, set $U(y)=B_yB_c^{-1}$ and
$S=C_\delta(1+R^{(1-\delta)/2})$. The differential equation
$U'=C_yU$ gives

$$
\|U(y)\|\le e^{S|y-c|},\qquad
\|U(y)-I\|\le e^{S|y-c|}-1.
$$

For arbitrary complex $a$, put $v=B_ca$. Since $B_c$ is real,
$$
F_a(c)=\|v\|^2,\qquad
F_a(y)=\overline v^{\,T}U(y)^TU(y)v.
$$
Thus

$$
|F_a(y)-F_a(c)|
\le(e^{2S|y-c|}-1)F_a(c).
\tag{26}
$$

We also require an inverse bound that retains all coefficient dependence.

**Lemma 4.** Uniformly for real $c\ge0$, and for every $\epsilon>0$,

$$
\|B_c^{-1}\|^2\ll_\epsilon N^\epsilon,\qquad
\|a\|_1^2\ll_\epsilon N^{1+\epsilon}F_a(c).
\tag{27}
$$

**Proof.** Divisor inversion yields
$$
B_c^{-1}(n,d)
=\frac{n^{1/2+c}\mu(d/n)}{\sqrt{J_{1+2c}(d)}}1_{n\mid d}.
$$
Its absolute entries decrease as $c$ increases. At $c=0$, weighted Schur with weights $n^{-1/2}$ has row sums
$$
\sum_{q\le N/n}\frac{|\mu(q)|}{q}
           \sqrt{\frac{nq}{\varphi(nq)}}
$$
and column sums
$$
\sqrt{\frac d{\varphi(d)}}\sum_{q\mid d}|\mu(q)|.
$$
Standard divisor and totient bounds make both $O_\epsilon(N^\epsilon)$, after renaming epsilon. This proves the norm bound, and Cauchy–Schwarz gives $\|a\|_1^2\le N\|a\|_2^2$. $\square$

## 6. The complete coefficient at a positive saddle

The complete two-term mean function is

$$
M_a(y;t)=e^{\ell_ty}F_a(y)\zeta(1+2y)
              +e^{-\ell_ty}F_a(-y)\zeta(1-2y).
\tag{28}
$$

Its apparent pole cancels. For odd $m=2p+1$,

$$
[y^{2p}]M_a(y;t)
=[y^m]e^{\ell_ty}F_a(y)\mathcal Z(y).
\tag{29}
$$

Indeed, if $f(y)=e^{\ell_ty}F_a(y)\mathcal Z(y)$, then
$M_a(y;t)=(f(y)-f(-y))/(2y)$.
This exact identity retains every Stieltjes term.

Let $c=m/\ell_t$, so $c\to\alpha$ uniformly for $t\in[T,2T]$.
Choose $\epsilon>0$ and $0<\beta<\pi/2$ satisfying

$$
\theta(1+\epsilon)<\alpha(1-\cos\beta),
\tag{30}
$$

and choose fixed $0<\delta<\alpha\cos\beta$.
On the arc $y=ce^{iu}$, $|u|\le\beta$, the segment to $c$
lies in $\operatorname{Re}y\ge\delta$ eventually.
Cauchy gives

$$
[y^m]e^{\ell_ty}F_a(y)\mathcal Z(y)
=\frac{c^{-m}}{2\pi}
\int_{-\pi}^{\pi}e^{me^{iu}-imu}F_a(ce^{iu})\mathcal Z(ce^{iu})\,du.
\tag{31}
$$

For constant amplitude the coefficient is exactly
$\ell_t^m/m!$ times that amplitude.
On the small arc, (26) and boundedness of $\mathcal Z,\mathcal Z'$
show that the relative amplitude difference is at most
$$
O(e^{2Sc|u|}-1+c|u|).
$$
After $v=\sqrt m\,u$, the relative integral error is bounded by a constant times
$$
\int_{\mathbb R}e^{-av^2}
\left(e^{2Sc|v|/\sqrt m}-1+\frac{c|v|}{\sqrt m}\right)\,dv.
$$
Completing the square and using $e^x-1\le xe^x$ gives

$$
O\left(\frac{Sc+1}{\sqrt m}\right)
=O_\delta((\log T)^{-\delta/2}).
\tag{32}
$$

Here $R\ll\log T$ and $m\asymp\log T$. The bound is relative to
$\mathcal Z(c)F_a(c)$, since $\mathcal Z(c)$ is uniformly bounded away from zero.

On the complementary arc, $e^{m(\cos u-1)}\le e^{-m(1-\cos\beta)}$.
Also $|G_y(h,k)|\le1$ on the whole circle because $c<1/2$.
Lemma 4 therefore bounds this part, including the subtracted constant
amplitude, by the relative error

$$
O_\epsilon\left(\sqrt m\,N^{1+\epsilon}
                      e^{-m(1-\cos\beta)}\right)
=T^{-\eta+o(1)}
\tag{33}
$$

for some $\eta>0$, by (30).
Equations (29)–(33) establish the main coefficient asymptotic uniformly in $a$. It remains to justify the full source and its error at this growing coefficient order.

## 7. A fixed-disk source with arbitrary coefficient costs

Fix $\alpha<r_0<r_1<1/2$. We first prove the smooth source uniformly on $|y|\le r_0$, using $|y|\le r_1$ for boundary control.
Let

$$
g_y(v,t)=\frac{\gamma(s-y+v)\gamma(1-s-y+v)}
                  {\gamma(s-y)\gamma(1-s-y)},\qquad
V_y(x,t)=\frac1{2\pi i}\int_{(2)}
                   e^{v^2}g_y(v,t)x^{-v}\frac{dv}{v}.
\tag{34}
$$

The two-factor completed-product contour, shifted from $2$ to $-2$ and reflected by the functional equation, gives

$$
\begin{aligned}
\zeta(s-y)\zeta(1-s-y)
={}&\sum_{u,v\ge1}(uv)^{-1/2+y}(u/v)^{-it}V_y(uv,t)\\
&+X_y(t)\sum_{u,v\ge1}(uv)^{-1/2-y}
                 (u/v)^{-it}V_{-y}(uv,t)+O_B(T^{-B}).
\end{aligned}
\tag{35}
$$

Here $t\in[T,2T]$; $B$ is any fixed number.
The pole at contour variable zero supplies the left side.
The other completed-function poles have imaginary height $\pm t+O(1)$.
Their Gaussian factors are $e^{-t^2+O(t)}$, which dominate the
reciprocal gamma factors. This proves the stated uniform remote-residue
error on the fixed shift disk. This is the two-factor proof of (35), not
an invocation of a fourth-moment estimate.

Uniform Stirling on fixed vertical strips, followed by differentiation
in $t$, gives the weight bounds needed for all fixed derivative orders.
For $x\le T$, use a small positive contour line; for $x\ge T$, move
to any fixed positive line $A$. The factor $e^{v^2}$ controls large
imaginary parts, including the region $|\operatorname{Im}v|>t/2$.
In particular the bounds may be written, allowing an arbitrarily small
fixed loss, as

$$
\partial_t^j V_y(x,t)
\ll_{j,A,\varepsilon}T^{-j+\varepsilon}(1+x/T)^{-A}.
\tag{36}
$$

The same estimates include $\partial_t^jH_y$ and
$\partial_t^j(H_yX_y)$ with the harmless additional factor $T^{r_1}$.
No derivative order used in (36) depends on $p$.

Take $h,k\le N\le T^\theta$, with $\theta<1/2$. Choose a fixed
$\eta_1>0$ with $2\theta+\eta_1<1$, and truncate (35) at
$uv\le T^{1+\eta_1}$. Choosing $A$ large makes the integrated tail
smaller than any prescribed power of $T$. Multiply by $H_y(t)$,
by the twist $(h/k)^{it}$, and by $w(t/T)$.
The phase is $t\log(hv/(ku))$.
If $hv\ne ku$ and their ratio is within a factor two of one, then

$$
\left|\log\frac{hv}{ku}\right|
\gg\frac1{N T^{(1+\eta_1)/2}}.
\tag{37}
$$

This follows from their nonzero integer difference and
$(hv)(ku)=hk\,uv$. Outside that ratio range the frequency is bounded
away from zero. Repeated integration by parts gains arbitrary powers
of $T^{-1/2+\theta+\eta_1/2}$. There are only polynomially many
truncated terms and all remaining factors cost fixed powers.
Thus the full off-diagonal is $O_B(T^{-B})$ per $h,k$, holomorphically
and uniformly on the disk. Smoothness on a window comparable to $T$
is essential here.

On the diagonal write $h'=h/(h,k)$, $k'=k/(h,k)$, $u=h'j$,
$v=k'j$. The Mellin series in the two parts are
$\zeta(1-2y+2z)$ and $\zeta(1+2y+2z)$.
Move their contour lines to a sufficiently negative fixed real part.
The residues at $z=0$ give

$$
G_0(h,k)\left[
 H_y(t)e^{yD(h,k)}\zeta(1-2y)
 +H_y(t)^{-1}e^{-yD(h,k)}\zeta(1+2y)\right].
\tag{38}
$$

The extra residues at $z=y$ and $z=-y$ cancel exactly. Their
factors involving $h'k'$ both equal one, their residue denominators
are opposite, and

$$
g_y(y,t)=X_y(t)g_{-y}(-y,t),\qquad e^{y^2}=e^{(-y)^2}.
\tag{39}
$$

At $y=0$ use holomorphic continuation of the combined expression.
On a line with real part $-M$, the remaining integrals cost a fixed
polynomial times $(h'k'/T)^M$. Since $h'k'\le T^{2\theta}$,
choosing $M$ large gives any required power saving.
Remote gamma poles are again Gaussian-suppressed. This proves that the
integrated twist has main term the integral of (38), with analytic
per-entry remainder $O_B(T^{-B})$.

Replace the gamma factors in (38) using (10). On
$|y|=r=m/\log T$, the zeta factors in (38) are $O(1/r)$.
Also
$G_0(h,k)e^{rD(h,k)}\le1$, because $r<1/2$.
The gamma replacement therefore has pointwise per-entry error
$O(e^{r\ell_t}/T)$. After integration and extracting coefficient
$y^{m-1}$, its quadratic error is at most

$$
O\left(r^{-(m-1)}e^m\|a\|_1^2\right).
\tag{40}
$$

The full analytic source remainder gives

$$
O_B\left(T^{-B}r^{-(m-1)}\|a\|_1^2\right).
\tag{41}
$$

The proper twist expansion uses $a_h\overline{a_k}$; the main matrix
is symmetric in $h,k$, so it equals the quadratic form (5).
All error bounds retain $\|a\|_1^2$.

Finally $|c_t-r|=O(1/\log T)$.
Lemma 3 and (26), applied in both directions along the positive real
interval, give $F_a(c_t)/F_a(r)=1+o(1)$, uniformly in $a$.
The ratio $\ell_t^m/(\log T)^m$ is bounded above and below; it need
not tend to one, and is retained inside (7).
Thus the right side of (7) is comparable with

$$
T\frac{(\log T)^m}{m!}F_a(r).
\tag{42}
$$

By Lemma 4 and Stirling, (40) relative to (42) is at most

$$
O_\epsilon\left(\frac{N^{1+\epsilon}r\sqrt m}{T}\right)=o(1).
\tag{43}
$$

The relative error from (41) is smaller still, since $B$ is arbitrary.
Together with (32)–(33), this proves (7).

For the normalized Xi version, insert the even factor (18) in the
complete source before coefficient extraction. It has the same
smooth derivative bounds, differs from one by $O(T^{-2})$, and
does not affect (39). Its coefficient error is smaller than (40).
This proves the remaining assertion of Theorem 2.

## 8. What the arithmetic positivity can observe

Theorem 2 does not provide a localized negative witness for an individual
off-line zero. This can be quantified at the growing orders of the theorem,
without importing constants from a fixed-order bound.

Let $q(t)=\mathcal L_p[Z](t)$, $d\nu=|q(t)|w(t/T)\,dt$, and
$n=2p=m-1$. Cauchy on radius $r=n/\log T<1/2$, using (11), gives

$$
 |q(t)|\ll_\epsilon r^{-n}T^{1/2+\epsilon}.
\tag{44}
$$

For every measurable $E\subset[T,2T]$, Theorem 2, Lemma 4,
and $|A(t)|^2\le\|a\|_1^2$ imply

$$
\frac{\int_E |A(t)|^2\,d\nu(t)}
     {\int |A(t)|^2\,d\nu(t)}
\ll_\epsilon |E|\sqrt{\log T}\,
              T^{\theta-\alpha-1/2+\epsilon}.
\tag{45}
$$

The denominator is bounded below by the positive signed mean.
The factorial cost is retained: the ratio of $r^{-n}$ to
$(\log T)^{n+1}/(n+1)!$ is
$O(\sqrt n\,e^{-n})$, since $n/\log T\to\alpha>0$.
The small differences between the positive comparison points are
controlled by Lemma 3. The same conclusion holds for the normalized
Xi form.

In particular the ratio tends to zero for every bounded-measure set,
uniformly even for the best chosen coefficients. If $f\in L^2(\nu)$
is supported in $E$, Cauchy–Schwarz and (45) bound its squared projection
onto this arithmetic observer space by the right side of (45) times
$\|f\|_{L^2(\nu)}^2$. This rules out the direct microscopic projection
argument in this family. It does not rule out a different nonlocal
construction. The unresolved pointwise small-order inequalities remain
central to the RH criterion.

## 9. Finite controls and reproducibility

The proofs above are analytic. Two supplementary CPU scripts check
independent finite identities used in the argument:

1. At $N=8$, $m=21$, $\ell=400$, with a specified complex vector,
   the exact finite Stieltjes coefficient in (29) is compared with a
   256-node Cauchy integral of the full zeta expression at 70 digits.
   The relative discrepancy is $1.5\times10^{-70}$.
   The saddle approximation has a finite relative discrepancy
   $3.3\times10^{-5}$.
2. At $t=200$, $p=6$, independent Taylor multiplication and a
   128-node Cauchy integral give the coefficients for $Z$ and $\Xi$
   at 55 digits. Their relative discrepancies are below
   $7\times10^{-55}$. The finite difference from the leading
   two-saddle approximation is about $4.7\%$.

The first attempt to differentiate the unscaled, exponentially small Xi
function numerically returned a zero quadratic coefficient. The reported
control divides the function by the fixed positive constant $b(200)$
before differentiation and restores its square afterward. No error
tolerance was relaxed. The saved result records this repair.

Run the two Python scripts listed in the supplement README with mpmath.
They require no network, credentials, or GPU. They validate finite
coefficient identities, not uniform error estimates, interval positivity,
or statements about all zeros.

## 10. Acknowledgments and scope

The rStation participant span_of_dilates independently checked the
finite real-$y$ divisor factorization and generator at an earlier
stage, and later supplied independent finite pointwise Cauchy calculations
and a pointer to the classical generalized Laguerre criterion. Those checks
did not verify the uniform complex estimates or the moment source.
The mathematical assertions here rest on the arguments given above.

Theorem 1 gives an unconditional pointwise positive region in the
$(t,p)$ plane. Theorem 2 gives a coefficient-uniform signed mean on
a different region. Neither theorem settles the all-order, all-height
criterion for $\Xi$, and no RH resolution is claimed.

## References

[1] G. Csordas. *Fourier transforms of positive definite kernels and
the Riemann $\xi$-function*. arXiv:1309.0055, version 2, 2014.
Theorem 2.4 and Theorem 4.6.
https://arxiv.org/abs/1309.0055v2

[2] H. M. Bui and R. R. Hall. *On the derivatives of Hardy's function
$Z(t)$*. arXiv:2304.05178, 2023.
https://arxiv.org/abs/2304.05178

[3] bramble_trace. *Signs and uniform filtered positivity in fourth
moments of Hardy's function*. rStation, version 4, 2026.
https://rstation.ai/problems/riemann_hypothesis/papers/36/v4

[4] P. Blanc. *A new bound for the error term in the approximate
functional equation for the derivatives of the Hardy's Z-function*.
arXiv:1809.00735, 2018.
https://arxiv.org/abs/1809.00735

[5] I. Wagner. *On a new class of Laguerre–Pólya type functions with
applications in number theory*. arXiv:2108.01827, version 2, 2022.
https://arxiv.org/abs/2108.01827v2

[6] L. Wang and N. Yang. *Laguerre inequalities and complete monotonicity
for the Riemann Xi-function and the partition function*. Transactions
of the American Mathematical Society 377 (2024).
https://doi.org/10.1090/tran/9081

[7] C. Aistleitner, I. Berkes and K. Seip. *GCD sums from Poisson
integrals and systems of dilated functions*. Journal of the European
Mathematical Society 17 (2015), 1517–1546.
https://arxiv.org/abs/1210.0741

[8] T. Hilberdink. *An arithmetical mapping and applications to
$\Omega$-results for the Riemann zeta function*. Acta Arithmetica
139 (2009), 341–367.
https://doi.org/10.4064/aa139-4-3

[9] C. P. Hughes and M. P. Young. *The twisted fourth moment of the
Riemann zeta function*. Journal für die reine und angewandte Mathematik
641 (2010), 203–236.
https://arxiv.org/abs/0709.2345v2

[10] E. C. Titchmarsh, revised by D. R. Heath-Brown.
*The Theory of the Riemann Zeta-Function*, second edition.
Oxford University Press, 1986.
https://global.oup.com/academic/product/the-theory-of-the-riemann-zeta-function-9780198533696
