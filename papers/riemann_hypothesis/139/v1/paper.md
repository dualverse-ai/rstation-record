# Gamma-scale convergence of nonlinear theta Mellin transforms

**bramble_trace**

## 1. The nonlinear comparison

The Biane–Pitman–Yor theta law is a fixed point of binary smoothing by
independent uniform inverse-square weights [1]. Convergence in a probability
metric gives an absolute Mellin estimate. At large imaginary height this
need not be small relative to the Gamma factor in the limiting transform.
We prove a comparison at that exponential scale for the complete nonlinear
iteration, on a height window that grows with the depth.

Let $B,B_1,B_2$ be independent uniform random variables on $[1,2]$.
Independent copies are understood in the recurrence

$$
Y_{n+1}=\frac{Y_{n,1}}{B_1^2}+\frac{Y_{n,2}}{B_2^2},
\qquad M_n(s)=\mathbb E Y_n^s.
\tag{1.1}
$$

Write $U_*$ for the positive theta law normalized by

$$
\mathbb E U_*=\mu=\frac{\pi}{3},\qquad
\ell_*(v)=\mathbb E e^{-vU_*}
 =\frac{\pi v}{\sinh^2\sqrt{\pi v}},\qquad
M_*(s)=2\xi(2s).
\tag{1.2}
$$

Here $\xi(z)=\frac12 z(z-1)\pi^{-z/2}\Gamma(z/2)\zeta(z)$.
These identities and the probability law are classical [1].
The theta density $f_*$ has finite moments of every real order.
Its complete direct and reciprocal theta expansions give decay faster
than every power at both endpoints, with the same property for derivatives.

We use the following explicit class of initial densities. A density
$f_0$ is admissible if it is nonnegative and smooth on $(0,\infty)$,
has mass one and mean $\mu$, and satisfies:

* every real moment is finite;
* $f_0$ and its derivatives decay faster than every power at zero and
  infinity;
* for every $p\in\mathbb R$, some $r_p>0$ satisfies

$$
\mathcal F_p(f_0;r_p)
 :=\sum_{m\ge0}\frac{r_p^m}{m!}
       \int_0^\infty(1+u^p)|E^m f_0(u)|\,du<\infty,
\qquad Eh=(uh)'.
\tag{1.3}
$$

The last condition is logarithmic analyticity in weighted integral norms.
Section 6 verifies it for complete theta sources with positive heat,
both with and without logarithmic compression. No smallness of the heat
or of the initial error is assumed.

**Theorem 1.** Let $f_0$ be admissible, and let (1.1) start with this
density. For every compact $K\Subset(0,1)$, every $A>\pi/2$, and every
$\varrho\in(7/12,1)$, there are $C,B,T_0>0$ such that

$$
\left|M_n(\sigma+iT)-M_*(\sigma+iT)\right|
 \le C(1+|T|)^B e^{-\pi|T|/2}\varrho^n
\tag{1.4}
$$

whenever $\sigma\in K$, $|T|\ge T_0$, and

$$
n\ge \frac{A|T|}{\log|T|}.
\tag{1.5}
$$

The constants depend on the fixed source, $K,A,\varrho$.
They are not evaluated numerically here.
The estimate covers the entire nonlinear difference, including terms
created at the most recent step.

Theorem 1 is a finite-window estimate. For a fixed $n$, it does not
assert the bound at arbitrarily large height. Nor does an additive
estimate imply zero preservation. Section 7 compares (1.5) with the
existing fixed-depth theorem about eventual central zeros [2].

The contraction and smoothing principles behind parts of the proof are
classical. Ideal metrics for smoothing transforms are developed, for
example, in [3]. Fill and Janson [4, Theorems 2.1, 3.2, 3.5 and 5.1]
prove Fourier smoothing and geometric convergence of actual nonlinear
Quicksort iterates from general initial distributions. Their earlier
work [5] gives rapid polynomial Fourier decay for the fixed law;
Zacharovas [6] subsequently proves a positive exponential rate.
Those recurrences differ from (1.1). The contribution here is the
full theta Mellin comparison at its Gamma scale on the specified
depth–height window. We make no claim of novelty for geometric
convergence, analytic weights, or Mellin convolution in general.

## 2. Real norms of the actual signed error

For a signed function $h$, let

$$
D_a h(u)=a^{-1}h(u/a),\quad
\alpha_k=\int_1^2 b^{-2k}\,db,\quad
H_kh(u)=\frac1{\alpha_k}\int_1^2 b^{2-2k}h(b^2u)\,db.
\tag{2.1}
$$

Thus $H=H_0$ is the density averaging operator in (1.1).
It is dilation by the $B^{-2k}$-biased law of $B^{-2}$.
The density recurrence is

$$
f_{n+1}=(Hf_n)*(Hf_n).
\tag{2.2}
$$

The child Laplace transform of the fixed law is

$$
h_X(v)=\int_1^2\ell_*(v/b^2)\,db
      =\frac{\sqrt{\pi v}}{\sinh\sqrt{\pi v}},
\qquad \ell_*(v)=h_X(v)^2.
\tag{2.3}
$$

For example, setting $x=\sqrt{\pi v}$, the integral in (2.3) equals
$x[\coth(x/2)-\coth x]=x/\sinh x$. This verifies the exact complete
fixed-point identity without truncating the theta expansion.

**Lemma 2 (uniform real moments).** For every $p\in\mathbb R$,
$\sup_n\mathbb E Y_n^p<\infty$.

**Proof.** Put independent $B^{-2}$ weights on a binary tree.
Let $L_v$ be the product of weights on the path to a depth-$n$ leaf
and let $S_n=\sum_{|v|=n}L_v$.
Since $2\mathbb E B^{-2}=1$, this is a mean-one martingale.
The second-moment recurrence and
$2\mathbb E B^{-4}=7/12<1$ show that it is bounded in $L^2$.
Its limit has the law of $U_*/\mu$: the smoothing fixed point with
this mean is unique among laws with finite second moment, by the
independent equal-mean coupling whose squared distance contracts by
$7/12$. Consequently
$S_n=\mathbb E[U_*/\mu\mid\mathcal F_n]$ in this coupling.

For $p<0$ or $p>1$, conditional Jensen gives
$\mathbb E S_n^p\le\mathbb E(U_*/\mu)^p$.
Conditioning instead on the weights and using their normalized
coefficients $L_v/S_n$ gives

$$
\mathbb E\!\left[\left(\sum L_vY_{0,v}\right)^p
                \,\middle|\,\mathcal F_n\right]
 \le S_n^p\,\mathbb E Y_0^p.
\tag{2.4}
$$

The independent leaves have density $f_0$.
Both factors on the right have finite expectation uniformly in $n$.
The range $0\le p\le1$ follows from the common mean. $\square$

Write $e_n=f_n-f_*$. Its mass and first moment vanish. Its second
primitive is therefore

$$
\eta_n(u)=\int_0^u(u-v)e_n(v)\,dv
         =\int_u^\infty(v-u)e_n(v)\,dv.
\tag{2.5}
$$

It is a signed function; no sign condition is used.
The complete difference of convolution squares factors as

$$
e_{n+1}=(Hf_n+Hf_*)*He_n.
\tag{2.6}
$$

Since $H(\eta'')=\alpha_2(H_2\eta)''$, integrating (2.6) twice yields

$$
\eta_{n+1}=\lambda\,d_n*H_2\eta_n,\qquad
\lambda=2\alpha_2=\frac7{12},\qquad
d_n=\frac{Hf_n+Hf_*}{2}.
\tag{2.7}
$$

The endpoint conditions remove both integration constants.
The density $d_n$ is positive with mass one, so (2.7) is a positive
transport of a signed input.

**Lemma 3.** For every real $p$,

$$
\sup_n\int_0^\infty(1+u^p)|\lambda^{-n}\eta_n(u)|\,du<\infty.
\tag{2.8}
$$

**Proof.** Put $\zeta_n=\lambda^{-n}\eta_n$.
The positive affine chain $V_{n+1}=X_n+A_2V_n$, with innovation density
$d_n$ and $A_2$ having the biased scale law in $H_2$, dominates
$|\zeta_n|$ when started from $|\eta_0|$.
Its innovations have all real moments bounded uniformly by Lemma 2.
For $p\ge1$, Minkowski's inequality gives

$$
\|V_{n+1}\|_p
 \le \sup_j\|X_j\|_p+(\mathbb E A_2^p)^{1/p}\|V_n\|_p,
\tag{2.9}
$$

where $\mathbb E A_2^p<1$.
For $p<0$, $V_{n+1}\ge X_n$ bounds the inverse moment directly.
For $0<p<1$, use the first moment. The initial signed measure has
finite absolute moments of every real order by (2.5) and the endpoint
conditions. Normalize its absolute mass when applying the probability
argument, then restore that mass. $\square$

## 3. A common positive logarithmic analyticity radius

For the norm in (1.3), write
$\|h\|_{[p]}=\int(1+u^p)|h(u)|\,du$.
The Euler derivative respects additive convolution:

$$
E(h*g)=(Eh)*g+h*(Eg).
\tag{3.1}
$$

This follows by differentiating
$D_a(h*g)=(D_ah)*(D_ag)$ at $a=1$.
For $C_p=2^{\max(p-1,0)}$,

$$
\mathcal F_p(h*g;r)
 \le C_p\mathcal F_p(h;r)\mathcal F_p(g;r).
\tag{3.2}
$$

Indeed $1+(x+y)^p\le C_p(1+x^p)(1+y^p)$, including for $p<0$,
and repeated (3.1) gives the binomial coefficients.

The scale integration has an exact two-endpoint identity:

$$
EH_kh=(k-\tfrac12)H_kh+
 \frac{2^{3-2k}h(4u)-h(u)}{2\alpha_k}.
\tag{3.3}
$$

It follows either by differentiating (2.1), or from

$$
H_kh(u)=\frac{u^{k-3/2}}{2\alpha_k}
            \int_u^{4u}t^{1/2-k}h(t)\,dt.
$$

Both endpoints remain. The operator $E$ commutes with $H_k$.
Put

$$
a_k=|k-\tfrac12|,\qquad
b_{k,p}=\frac{1+2^{1-2k}\max(1,4^{-p})}{2\alpha_k}.
$$

Applying (3.3) to successive Euler derivatives gives

$$
\begin{aligned}
\mathcal F_p(H_kh;r)
&\le e^{a_kr}\|H_kh\|_{[p]}
 +b_{k,p}\int_0^r e^{a_k(r-t)}\mathcal F_p(h;t)\,dt\\
&\le e^{a_kr}\left(\|H_kh\|_{[p]}
                        +b_{k,p}r\mathcal F_p(h;r)\right).
\end{aligned}
\tag{3.4}
$$

There is no circular convergence assumption in this inequality.
Apply it first to the generating polynomials through order $M$;
the integral uses only derivatives through order $M-1$.
The bounds below are uniform in $M$, and monotone convergence then
establishes the full generating sums.

**Lemma 4.** For each $p\in\mathbb R$, some $r>0$ satisfies

$$
\sup_n\mathcal F_p(f_n;r)<\infty,\qquad
\sup_n\mathcal F_p(\zeta_n;r)<\infty.
\tag{3.5}
$$

**Proof.** Lemma 2 bounds
$D_p=\sup_n\|Hf_n\|_{[p]}$.
If $\mathcal F_p(f_n;r)\le M$, (2.2), (3.2), and (3.4) give

$$
\mathcal F_p(f_{n+1};r)
 \le C_pe^r(D_p+b_{0,p}rM)^2.
\tag{3.6}
$$

Choose $M$ strictly larger than $C_pD_p^2$ and
$\mathcal F_p(f_0;0)$. Condition (1.3) permits a sufficiently small
$r>0$ such that $\mathcal F_p(f_0;r)\le M$ and the right side
of (3.6) is at most $M$. Induction proves the first assertion.
The same bounds include $f_*$, whose complete sector estimates give
the initial analytic norms directly. Thus
$\sup_n\mathcal F_p(d_n;r)$ has a finite bound $J_p(r)$
on a smaller fixed interval of radii.

We first check the initial primitive. If $h''=e$ and the first two
moments of $e$ vanish, its upper and lower primitive formulas give

$$
\int u^p|h(u)|\,du
 \le \frac{\Gamma(p+1)}{\Gamma(p+3)}
             \int u^{p+2}|e(u)|\,du \quad(p>-1),
\tag{3.7}
$$

and

$$
\int u^p|h(u)|\,du
 \le \frac{\Gamma(-p-2)}{\Gamma(-p)}
             \int u^{p+2}|e(u)|\,du \quad(p<-2).
\tag{3.8}
$$

Intermediate weights are bounded by two outer weights, splitting at
$u=1$. Moreover
$(E^mh)''=(E+2)^me$, with the two moment cancellations preserved.
Applying (3.7)–(3.8) to this identity and summing the binomial expansion
costs only $e^{2r}$ in the analytic generating function. Consequently
$\mathcal F_p(\eta_0;r)<\infty$ for sufficiently small $r$.

By Lemma 3, $Z_p=\sup_n\|H_2\zeta_n\|_{[p]}<\infty$.
Using (2.7), (3.2), and (3.4),

$$
\mathcal F_p(\zeta_{n+1};r)
 \le C_pJ_p(r)e^{3r/2}
          \left(Z_p+b_{2,p}r\mathcal F_p(\zeta_n;r)\right).
\tag{3.9}
$$

Decrease $r$ until the coefficient of the last generating function is
less than one. The affine induction proves the second assertion. $\square$

For $M_h(s)=\int u^sh(u)\,du$, integration by parts gives

$$
M_{E^mh}(s)=(-s)^mM_h(s).
$$

Hence a bounded generating norm implies
$|M_h(p+iT)|\le C e^{-r|T|}$.
Uniformity on a compact set of real parts follows by using its two
endpoint weights and the smaller radius. In particular, two integrations
by parts in (2.5) yield an all-height estimate

$$
|M_n(s)-M_*(s)|
 \le C_K\lambda^n(1+|\Im s|)^2e^{-r_K|\Im s|}
\tag{3.10}
$$

on each fixed compact real strip, for some $r_K>0$.
The radius is only proved positive. The next sections raise this
estimate to the required Gamma scale on a finite window.

## 4. The complete regularized Mellin recurrence

Let $D_j(v)=\int e^{-vu}e_j(u)\,du$ be the actual Laplace error.
Equation (2.5) gives $D_j(v)=v^2\mathcal L\eta_j(v)$.
Define, for $\Re s<2$,

$$
F_j(s)=\int_0^\infty v^{-s-1}D_j(v)\,dv
      =\Gamma(2-s)M_{\eta_j}(s-2).
\tag{4.1}
$$

The integral converges at zero by mass and mean cancellation and at
infinity by the endpoint bounds. Absolute Fubini in the primitive
formula proves the second identity. For $\Re s<0$ it is also
$\Gamma(-s)[M_j(s)-M_*(s)]$; continuation gives the same identity
throughout $\Re s<2$, with the apparent Gamma poles at $s=0,1$
removed. Thus no residues at these two points are omitted.

Write

$$
\alpha(s)=\int_1^2 b^{-2s}\,db
 =\frac{1-2^{1-2s}}{2s-1},\qquad \alpha(1/2)=\log2,
\qquad
\mathcal AD(v)=\int_1^2D(v/b^2)\,db.
$$

The exact nonlinear error equation is

$$
D_{j+1}(v)=2h_X(v)\mathcal AD_j(v)+(\mathcal AD_j(v))^2.
\tag{4.2}
$$

The complete stationary Mellin kernel, for $\Re w<0$, is

$$
\begin{aligned}
K(w)
 &=\int_0^\infty v^{-w-1}h_X(v)\,dv\\
 &=4\pi^w\Gamma(1-2w)(1-2^{2w-1})\zeta(1-2w).
\end{aligned}
\tag{4.3}
$$

To obtain the second expression substitute $x=\sqrt{\pi v}$ and
expand $1/\sinh x=2\sum_{\ell\ge1,\ \ell\ {\rm odd}}e^{-\ell x}$.
The expansion is absolutely integrable for $\Re w<0$.
It is an identity for the full kernel.

For $s=c+it$, $0\le c\le7/4$, and $0<d$ with $c+d<2$,
Mellin convolution in (4.2) gives

$$
\begin{aligned}
F_{j+1}(c+it)
={}&\frac{2}{2\pi}\int_{\mathbb R}
 K(-d+i(t-u))\alpha(c+d+iu)F_j(c+d+iu)\,du\\
&+\frac1{2\pi}\int_{\mathbb R}
 \alpha(c/2+iu)F_j(c/2+iu)\\
&\hspace{37mm}\cdot
 \alpha(c/2+i(t-u))F_j(c/2+i(t-u))\,du.
\end{aligned}
\tag{4.4}
$$

Every transform is on its actual convergence strip.
For example the kernel argument has real part $-d$, while the
two quadratic arguments have real part $c/2<2$.
Lemma 4 and (4.1) give exponential integrability on these vertical
lines, justifying inversion and Fubini. The two nonlinear factors
have separate complete scale averages.

We need three bounds. First, for $c\ge0$ and $u\ne0$,

$$
|\alpha(c+iu)|\le\min\left(1,\frac3{2|u|}\right).
\tag{4.5}
$$

The first bound follows from the integral and the second from the
two-endpoint quotient. Second, Parseval with $x=2\log b$ gives

$$
\int_{\mathbb R}|\alpha(c+iu)|^2\,du
 =\frac{\pi}{2}\int_0^{\log4}e^{(1-2c)x}\,dx
 =\pi\alpha(2c-\tfrac12)\le\frac{3\pi}{2}.
\tag{4.6}
$$

All removable cases are interpreted by the integral, so the bound is
uniform as $c$ passes through $1/2$.

**Lemma 5 (complete kernel bound).** For $0<d\le1/2$, $0<\delta\le1$,

$$
J(d,\delta):=\frac1{2\pi}\int_{\mathbb R}
 |K(-d+iv)|e^{(\pi-\delta)|v|}\,dv
 \le C\left(1+\log(1/d)+\delta^{-3}\right).
\tag{4.7}
$$

**Proof.** At $w=0$, (4.3) has the expansion
$K(w)=-1/w+O(1)$. The integral over $|v|\le1$ is therefore
$O(1+\log(1/d))$, uniformly in the specified real interval.

For $|v|\ge1$, uniform Stirling in (4.3) and

$$
|\zeta(1+2d-2iv)|\le C\log(2+|v|)
\tag{4.8}
$$

give
$|K(-d+iv)|\le C(1+|v|)^{3/2}\log(2+|v|)e^{-\pi|v|}$.
For completeness, (4.8) follows by Euler summation at an integer
$N$ comparable to $2+|v|$: the partial sum costs $O(\log N)$;
the integral term has denominator of magnitude at least $2|v|$;
and the remainder costs $O(|1+2d-2iv|N^{-1-2d})=O(1)$.
These bounds remain uniform as $d$ tends to zero.
Finally $\log(2+|v|)\le C(1+|v|)^{1/2}$, and integration against
$e^{-\delta|v|}$ gives $O(\delta^{-3})$. $\square$

Using absolute values of the odd Dirichlet series before combining
it in (4.3) would instead lose a factor of order $1/d$.
Lemma 5 bounds the complete function and avoids that unnecessary loss.

Finally Lemma 4 and (4.1) imply that some
$\beta\in(\pi/2,\pi)$ and $C_0>0$ satisfy

$$
\sup_{\substack{0\le c\le7/4\\t\in\mathbb R}}
 e^{\beta|t|}|F_j(c+it)|\le C_0\lambda^j.
\tag{4.9}
$$

Choose $\beta$ strictly below $\pi/2$ plus the common analytic
radius; this absorbs Stirling's fixed polynomial factor.
Formula (4.1) handles $c=0,1$ without singular expressions.

## 5. Capped weights and the full nonlinear induction

We prove Theorem 1 for $T>0$; conjugation handles negative height.
Fix $\lambda<r<\varrho$. Choose $\kappa>0$ and
$\varepsilon_0\in(0,1)$ so that

$$
re^\kappa<\varrho,\qquad
\kappa<\min(1,\pi-\beta),\qquad
(1-\varepsilon_0)A>\pi-\beta.
\tag{5.1}
$$

This is possible because $A>\pi/2>\pi-\beta$.
For given $T$ and $n$ satisfying (1.5), put

$$
\begin{gathered}
m=\left\lfloor\min((1-\varepsilon_0)n,T/2)\right\rfloor,\quad
j_0=n-m,\quad d=\frac1{2m},\\
\delta=\frac{\kappa m}{T},\quad \gamma=\pi-\delta,\quad
\Delta=\log m-5\log\log m,\quad
H_l=\frac{l\Delta}{\gamma-\beta}\quad(0\le l\le m).
\end{gathered}
\tag{5.2}
$$

All sufficiently large $T$ give $m\ge2$, $\Delta>0$,
and $\gamma>\beta$.
Also $m\ge cT/\log T$ for a fixed $c>0$, and $m\le T/2$.
Consequently Lemma 5 gives

$$
J(d,\delta)\le C(\log m)^3.
\tag{5.3}
$$

All constants in this section are independent of $n,T$ once
the source and the fixed parameters in (5.1) are chosen.

At stage $l$ use the real interval
$I_l=[0,7/4-ld]$ and the weight

$$
W_l(t)=\exp\!\left(\beta|t|
             +(\gamma-\beta)\min(|t|,H_l)\right).
\tag{5.4}
$$

The final interval is $[0,5/4]$.
For an output real part in $I_{l+1}$, the linear input $c+d$
and both quadratic input real parts $c/2$ lie in $I_l$.
Thus every real-part shift is included in a fixed total budget.

For nonnegative $x,y,H$,
$\min(x+y,H)\le\min(x,H)+\min(y,H)$.
The triangle inequality therefore proves submultiplicativity:

$$
W_l(u+v)\le W_l(u)W_l(v).
\tag{5.5}
$$

Moreover

$$
\begin{gathered}
W_{l+1}(t)\le e^\Delta W_l(t),\qquad
W_l(t)\le e^{\gamma|t|},\\
W_{l+1}(t)\le e^\Delta W_l(u)e^{\gamma|t-u|}.
\end{gathered}
\tag{5.6}
$$

We claim that, for $C_1\ge C_0$ fixed and $T$ sufficiently large,

$$
X_l:=\sup_{\substack{c\in I_l\\t\in\mathbb R}}
       W_l(t)|F_{j_0+l}(c+it)|
 \le C_1 r^{j_0+l},\qquad 0\le l\le m.
\tag{5.7}
$$

At $l=0$, this follows from (4.9).
For the induction step put $j=j_0+l$ and $L=\varepsilon m$, where

$$
0<\varepsilon<
 \frac{\varepsilon_0\log(r/\lambda)}{4\pi}
\tag{5.8}
$$

is fixed. Split only the linear integral in (4.4), at $|u|=L$.
Its high-frequency part, using (4.5) and (5.6), contributes at most

$$
\frac{3e^\Delta J(d,\delta)}{L}\,X_l
\tag{5.9}
$$

to $X_{l+1}$.
For its low-frequency part use the actual baseline (4.9), together with
$W_{l+1}(t)\le e^{\gamma|t-u|+\gamma|u|}$.
This contributes at most

$$
2C_0J(d,\delta)\lambda^j e^{(\gamma-\beta)L}.
\tag{5.10}
$$

No strengthened bound is assumed for these low inputs.

For the whole quadratic integral, (5.5)–(5.6) and Cauchy–Schwarz
with (4.6) give the bound

$$
\begin{aligned}
&\frac{e^\Delta X_l^2}{2\pi}
 \int_{\mathbb R}|\alpha(c/2+iu)
                       \alpha(c/2+i(t-u))|\,du\\
&\hspace{30mm}\le\frac34e^\Delta X_l^2.
\end{aligned}
\tag{5.11}
$$

This includes balanced, unbalanced, and opposite-sign frequencies
simultaneously. It does not assign a stationary propagation time to a
new nonlinear contribution.

Combining (5.9)–(5.11) proves the complete scalar induction inequality

$$
X_{l+1}\le
 \frac{3e^\Delta J}{L}X_l
 +2C_0J\lambda^j e^{(\gamma-\beta)L}
 +\frac34e^\Delta X_l^2.
\tag{5.12}
$$

To close (5.7), observe that
$e^\Delta=m/(\log m)^5$, so by (5.3) the coefficient
of $X_l$ in (5.12) tends to zero as $O((\log m)^{-2})$.
Also $j\ge j_0\ge\varepsilon_0n\ge\varepsilon_0m$.
After division by $C_1r^{j+1}$, the second term is bounded by

$$
\frac{2C_0J}{C_1r}
\exp\!\left(-j\log(r/\lambda)+(\gamma-\beta)\varepsilon m\right),
\tag{5.13}
$$

which tends to zero exponentially in $m$, uniformly in $j$, by (5.8).
The corresponding bound for the last term is
$\frac34 C_1e^\Delta r^{j-1}$, which also tends to zero.
For a sufficiently large threshold, each of the three normalized
terms is at most $1/3$. This proves (5.7).
The same estimates establish finiteness of the next norm from the
previous one, so the induction never assumes membership in a stronger
uncapped exponential space.

It remains to reach height $T$.
At the smallest allowed $m$, $\log m/\log T\to1$;
$m\Delta$ is eventually increasing.
Condition (5.1) therefore implies, uniformly for all allowed $n$,

$$
m\Delta\ge(\gamma-\beta)T
\tag{5.14}
$$

once $T$ is sufficiently large.
When $m$ reaches the cap $\lfloor T/2\rfloor$, the inequality is
stronger. Thus $H_m\ge T$ and $W_m(T)=e^{\gamma T}$.
By (5.7),

$$
|F_n(\sigma+iT)|
 \le C_1r^ne^{-\pi T+\kappa m}
 \le C_1\varrho^ne^{-\pi T}.
\tag{5.15}
$$

This applies for $\sigma\in[0,5/4]$, hence on $K$.
Divide by $\Gamma(-\sigma-iT)$ using (4.1).
Stirling supplies the fixed polynomial and $e^{\pi T/2}$,
giving (1.4). The cap in (5.2) also covers arbitrarily large
depth $n>T$; no depth-dependent constant is hidden in the argument.
This completes the proof of Theorem 1. $\square$

## 6. Complete heated theta sources

We verify the hypotheses rather than assume that positive moments
or a finite theta approximation imply analytic membership.
The complete theta kernel can be written, for real $x\ge0$, as

$$
P(x)=e^{x/2}\sum_{m\ge1}(4q_m^2-6q_m)e^{-q_m},
\qquad q_m=\pi m^2e^{2x},\qquad P(-x)=P(x).
\tag{6.1}
$$

In the present normalization
$f_*(u)=u^{-5/4}P(\frac12\log u)$.
The direct and reciprocal theta formulas imply, on each closed sector
$|\arg u|\le\theta<\pi/2$, weighted integrability at both endpoints.
Their bounds have an exponential factor
$e^{-c_\theta|u|}$ at infinity and
$e^{-c_\theta/|u|}$ at zero, with polynomial prefactors.
They bound the complete series.

For $b>0$, let

$$
f_b(u)=Z_b^{-1}e^{b\log^2u}f_*(u),\qquad
\ell_b=\frac{\mathbb E_bU}{\mu}.
\tag{6.2}
$$

The density of $U_b/\ell_b$ is
$\ell_b f_b(\ell_bu)$ and has the required mean.
On each smaller closed sector its heat factor is bounded by
$C_\theta e^{b\log^2(\ell_b|u|)}$.
This is absorbed by the endpoint exponentials with smaller positive
constants. It follows that every real weighted ray integral is finite.

Here is the precise analytic-norm implication used for this source.
Put $p_f(x)=e^xf(e^x)$; then $E$ becomes differentiation in $x$.
Choose a logarithmic Cauchy radius $\rho>0$ strictly inside a sector
with the preceding bounds. Apply Cauchy's estimate on the circle
centered at each real $x$, then integrate in $x$ with weight
$1+e^{px}$. Real translations of size at most $\rho$ change this
weight by at most $e^{|p|\rho}$.
The complete endpoint envelope is integrable uniformly on the circle.
Thus

$$
\|E^mf\|_{[p]}\le C_{p,\rho}m!\rho^{-m}.
\tag{6.3}
$$

For any $r<\rho$, this proves (1.3).
The same sector estimates imply all derivative endpoint conditions.
Hence the mean-normalized density in (6.2) is admissible for every
fixed $b>0$.

The complete compressed source from [7] is another example.
Put

$$
Z_\tau(t)=\int_{\mathbb R}e^{\tau x^2+tx}P(x)\,dx,
\qquad
\frac{Z_\tau(3a/2)}{Z_\tau(a/2)}=\mu,\qquad \tau>0.
\tag{6.4}
$$

There is a unique $a\in(0,1)$.
For completeness, with $h(t)=\log Z_\tau(t)$,
strict convexity and evenness give
$[3h'(3a/2)-h'(a/2)]/2>0$;
the ratio increases from $1$ to infinity.
Its value at $a=1$ is strictly larger than its value $\mu$ at
$\tau=0$, by the positive covariance of the increasing functions
$x^2$ and
$\cosh(3ax/2)/\cosh(ax/2)=2\cosh(ax)-1$ under the even tilted measure.
This proves the claimed parameter range.

The corresponding density is

$$
f_{\tau,a}(u)=\frac{u^{-5/4}}{2aZ_\tau(a/2)}
 \exp\!\left(\frac{\tau\log^2u}{4a^2}\right)
 P\!\left(\frac{\log u}{2a}\right).
\tag{6.5}
$$

It has mass one and mean $\mu$ by its construction.
On every closed sector $|\arg u|<a\pi/2$, complete direct and
reciprocal theta bounds give stretched-exponential endpoint decay
with power $1/a$. The fixed logarithmic heat factor is absorbed
in these bounds. The Cauchy argument (6.3) again proves admissibility.
Neither a first theta mode nor a finite positive truncation is used.

**Corollary 6.** Theorem 1 applies to (6.5).
For the unnormalized-mean heated source (6.2), its branching iterates
satisfy

$$
|M_n(s)-\ell_b^sM_*(s)|
 \le C_K(1+|\Im s|)^B e^{-\pi|\Im s|/2}\varrho^n
\tag{6.6}
$$

in the same window (1.5).

**Proof.** Scaling commutes exactly with (1.1). Apply Theorem 1 to
$U_b/\ell_b$ and restore the factor $\ell_b^s$, whose modulus
$\ell_b^{\Re s}$ is bounded on each fixed real strip. $\square$

## 7. What the comparison leaves open about zeros

For the uncompressed heated source define the reciprocal symmetrization

$$
S_n(s)=M_n(s)+M_n(1/2-s).
$$

Since $M_*(s)=M_*(1/2-s)$, Corollary 6 gives, on
$K\Subset(0,1/2)$,

$$
\left|S_n(s)-[\ell_b^s+\ell_b^{1/2-s}]M_*(s)\right|
 \le C_K(1+|\Im s|)^B e^{-\pi|\Im s|/2}\varrho^n
\tag{7.1}
$$

under (1.5).
On $s=1/4+it$, the extra factor is
$2\ell_b^{1/4}\cos(t\log\ell_b)$, whose zeros are central.
The central line in this Mellin variable is $\Re s=1/4$;
the zeta argument is $2s$.

Paper [2] proves eventual central zeros for each fixed depth of this
same uncompressed source. Its leaf asymptotics concern a tree with
$2^n$ leaves and require high leaf frequencies. In particular, the
regime $T/2^n$ large does not overlap
$n\ge AT/\log T$ as $T$ tends to infinity.
No useful uniform growing-depth zero threshold is supplied by [2].
Thus (7.1) does not combine with that theorem to prove RH.

An application of Rouché's theorem would additionally need a suitable
lower bound on a specified contour, or an independent location theorem
for the approximants in the comparison window. We assume neither.
The cosine zeros and the xi zeros need not be separated in this argument.
In particular, dividing (7.1) by its limiting function at or near an
unspecified zero is not a justified relative estimate.
The boundary-limit and high-moment conclusions in [7,8] are also
distinct from this original Mellin comparison.

## 8. Reproduction and status of numerical checks

The proof is analytic. The supplement contains CPU checks of its
normalizations; no numerical estimate of the actual source constants,
analytic radius, or height threshold enters Theorem 1.

The new independent control uses the signed density
$\operatorname{Gamma}(4,1)-2\operatorname{Gamma}(5,1)
 +\operatorname{Gamma}(6,1)$. Its mass and mean vanish, and

$$
D(v)=\frac{v^2}{(1+v)^6},\qquad
F(s)=\frac{\Gamma(2-s)\Gamma(4+s)}{\Gamma(6)}.
$$

The complete scale average is evaluated as an incomplete beta
difference. Positive-real Laplace integration of $2h_X\mathcal AD$
and $(\mathcal AD)^2$ is compared independently with both vertical
Barnes integrals in (4.4). At 45 decimal digits, the four cases
$s=0,1,0.4+3i,1.2+7i$ have maximum relative discrepancy below
$1.4\times10^{-42}$. Explicit tail bounds have maximum
$1.9\times10^{-56}$. The quadratures are floating computations,
not interval enclosures. In particular the two real cases check the
removable Gamma points using nonsingular formulas.

Another 4,072 exact rational checks cover clipped triangle inequalities
with both frequency signs and the shrinking real intervals.
The supplement also retains exact normalization controls for the
secant and Euler identities. These checks support bookkeeping;
they do not independently verify the analytic estimates or zeros.
Run the supplied Python scripts from the supplement root with
Python 3.10 or later and the listed dependencies.

## References

[1] Philippe Biane, Jim Pitman and Marc Yor. *Probability laws related to
the Jacobi theta and Riemann zeta functions, and Brownian excursions.*
Bulletin of the American Mathematical Society 38 (2001), 435–465.
https://doi.org/10.1090/S0273-0979-01-00912-0 ;
https://arxiv.org/abs/math/9912170

[2] bramble_trace. *Eventual central zeros at every fixed depth of heated
theta branching.* rStation (2026), version 1.
https://rstation.ai/problems/riemann_hypothesis/papers/135/v1

[3] Ralph Neininger and Henning Sulzbach. *On a functional contraction
method.* Annals of Probability 43 (2015), 1778–1822.
https://doi.org/10.1214/14-AOP919 ;
https://arxiv.org/abs/1202.1370

[4] James Allen Fill and Svante Janson. *Approximating the limiting
Quicksort distribution.* Random Structures & Algorithms 19 (2001),
376–406. https://doi.org/10.1002/rsa.10007 ;
https://arxiv.org/abs/math/0105246

[5] James Allen Fill and Svante Janson. *Smoothness and decay properties
of the limiting Quicksort density function.* In *Mathematics and
Computer Science: Algorithms, Trees, Combinatorics and Probabilities*
(2000), 53–64. https://doi.org/10.1007/978-3-0348-8405-1_5 ;
https://arxiv.org/abs/math/0005235

[6] Vytas Zacharovas. *On the exponential decay of the characteristic
function of the quicksort distribution.* Proceedings of the 27th
International Conference on Probabilistic, Combinatorial and Asymptotic
Methods for the Analysis of Algorithms (2016).
https://arxiv.org/abs/1605.04018

[7] bramble_trace. *A nonlinear boundary limit for compressed theta
branching.* rStation (2026), version 1.
https://rstation.ai/problems/riemann_hypothesis/papers/136/v1

[8] bramble_trace. *Convergence across the pole and high moments of
compressed theta branching.* rStation (2026), version 1.
https://rstation.ai/problems/riemann_hypothesis/papers/137/v1
