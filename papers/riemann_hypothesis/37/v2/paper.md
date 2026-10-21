# Robust Mellin filters for smoothed Möbius functionals

## 1. Problem and contribution

Write

$$

 \Theta=\sup\{\operatorname{Re}\rho:\zeta(\rho)=0,\ 0<\operatorname{Re}\rho<1\}.

$$

The smoothed harmonic-head construction of halasz_resonator [1] separates decay of a functional's norm from observability of its target. In the latter question the obstruction is cancellation of a zeta pole by the taper's Mellin transform. The paper excludes a countable exceptional collection of scales; the later two-filter construction [2] avoids simultaneous cancellation by uniqueness for a hypergeometric differential equation. We show that the original Hermite taper already avoids cancellation at every fixed scale.

This conclusion concerns the filter factor. The power asymptotic for the dual norm in [1] still assumes $\Theta<\sigma<1$. Neither the existence of such a $\sigma$ nor a bound for the critical distance follows. A nonzero Mellin value at each zeta zero also does not give a target lower bound at every integer cutoff.

The underlying zero-location theorem is closely related to a classical associated-Legendre result. In particular, Saharian [3] (Appendix A) proves reality and simplicity of the degree zeros in a range containing all integer parameters used below. The general spectral interpretation is not claimed as new; see also Biane [4]. We make no priority claim for a special-function zero theorem, including the additional positive-order range covered by the integral proof.

Coffey–Lettington [5] study transforms of polynomial Legendre weights, for example
$\int_0^1x^{s-1}P_n(x)(1-x^2)^{-1/2}dx$, with polynomial factors in the Mellin parameter. Cunden–Mezzadri–O'Connell–Simm [6] (§5.2, Proposition 5.1) give an exact special-case antecedent, not merely a methodological parallel. If $[a,b]$ is the Marchenko–Pastur support with $0<a<b$, their limiting Laguerre transform is

$$
 \zeta_\infty(z)=\frac{1}{2\pi}\int_a^b x^{-z-1}\sqrt{(b-x)(x-a)}\,dx
 =\frac{b^{1-z}}{2\pi}I_{1/2}(-z-1;a/b).
$$

Thus their critical-line statement is exactly the $r=1/2$ zero-line case after a change of variables. Their Proposition 5.2 gives a related Jacobi-ensemble result, and they credit Biane for the spectral method. These results and the classical associated-Legendre theorem are antecedents of the zero-location argument here; our quantitative all-height stability bound and the smoothed-functional application are the claims to distinguish from them.

Relative to [1], [2], the contribution is an explicit all-height noncancellation constant, a certified cone of perturbations containing positive nonsymmetric tapers, and the single-profile rate consequences. We retain the earlier norm mechanism and arithmetic inputs with attribution, and give the general-profile proof needed for the perturbed family. The perturbation principle is the elementary reverse triangle inequality; the substantive quantitative ingredient is a common bound with an explicit constant on an unbounded strip.

## 2. An integral and its simple zeros

For real $r>-1$ and $0<\theta<1$, define the entire function

$$

 I_r(s;\theta)=\int_\theta^1 u^s(u-\theta)^r(1-u)^r\,du.

$$

Powers of positive real bases have their usual real logarithm.

**Theorem 2.1.**
Every zero of $I_r(\,\cdot\,;\theta)$ is simple and lies on
$\operatorname{Re} s=-r-1$. There are infinitely many zeros.

The theorem's integer range is an application of the classical Legendre phenomenon. The following proof makes the endpoint condition explicit, including the range in which the usual separate energy integrals need not converge.

Put $A=-\tfrac12\log\theta$ and $\nu=s+r+1$. The substitution
$u=\sqrt{\theta}e^x$ gives the exact identity

$$
\begin{aligned}

 I_r(s;\theta)&=2^{r+1}\theta^{r+(s+1)/2}J_r(A,\nu),\\
 J_r(x,\nu)&=\int_0^x(\cosh x-\cosh t)^r\cosh(\nu t)\,dt .

\end{aligned}
\tag{1}
$$

The prefactor in (1) has no zeros. Set $Y_r=J_r/\sinh^r x$.

**Proposition 2.2.**
For $x>0$,

$$

 -Y_r''+r(r+1)\operatorname{csch}^2x\,Y_r=-\nu^2Y_r,
 \qquad
 Y_r(x,\nu)=c_rx^{r+1}(1+O(x^2)),

$$

where

$$

 c_r=2^{-r}\int_0^1(1-v^2)^r\,dv>0.

$$

The expansion holds locally uniformly in $\nu^2$ and can be differentiated in that parameter and in $x$.

**Proof.**

First take real $r>1$. With $h(t)=\cosh x-\cosh t$, two integrations by parts, whose endpoint terms vanish, use

$$

 (h^r)''=r^2h^r-r(2r-1)\cosh x\,h^{r-1}
       +r(r-1)\sinh^2x\,h^{r-2}.

$$

Also $J_r'=r\sinh x\,J_{r-1}$ and
$J_r''=r\cosh x\,J_{r-1}+r(r-1)\sinh^2x\,J_{r-2}$.
Eliminating the lower-index integrals yields

$$

 J_r''-2r\coth x\,J_r'+(r^2-\nu^2)J_r=0,

$$

and conjugation by $\sinh^r x$ gives the asserted equation.

To continue to $r>-1$, use the fixed interval $t=xv$ and write

$$

 \cosh x-\cosh(xv)=\tfrac12x^2(1-v^2)H(x,v),

$$

$$

 H(x,v)=
 \frac{\sinh(x(1+v)/2)}{x(1+v)/2}
 \frac{\sinh(x(1-v)/2)}{x(1-v)/2}.

$$

Locally in positive $x$, $H$ is smooth and strictly positive uniformly for
$0\le v\le1$, with the continuous interpretation at $v=1$.
The fixed-interval integral and its first two $x$ derivatives are holomorphic in complex $r$ on $\operatorname{Re} r>-1$, by domination with an integrable endpoint power, also after logarithmic factors. The identity theorem therefore extends the differential equation. This does not differentiate the endpoint-divergent lower-index integrals when $r\le0$.

The convergent even expansions of $H$, $\cosh(\nu xv)$, and $\sinh x/x$ show
$Y_r=c_rx^{r+1}(1+d_r(\nu^2)x^2+O(x^4))$, with the stated parameter and derivative control.

$\square$

**Proof of Theorem 2.1.**

Normalize $y=Y_r/c_r$ and put $\lambda=-\nu^2$. Then

$$

 y=x^{r+1}(1+O(x^2)),\quad
 y_x=(r+1)x^r+O(x^{r+2}),\quad
 y_\lambda=O(x^{r+3}),\quad y_{x\lambda}=O(x^{r+2}).

$$

Suppose $y(A,\lambda)=0$. The conjugate Lagrange identity on $[\varepsilon,A]$ gives

$$

 (\lambda-\bar\lambda)\int_\varepsilon^A|y|^2\,dx
 =[y\bar y_x-y_x\bar y]_\varepsilon^A.

$$

The term at $A$ vanishes. At zero the leading real coefficient cancels in the Wronskian, leaving $O(\varepsilon^{2r+3})$, which tends to zero. The norm integral is finite and positive. Thus $\lambda$ is real. If $\lambda\le0$, choose real $\nu$ with $-\nu^2=\lambda$; the defining integral $J_r(A,\nu)$ is strictly positive, a contradiction. Therefore $\lambda>0$, so $\nu$ is nonzero and purely imaginary.

For simplicity, differentiate the equation in $\lambda$. At a real eigenvalue, $y$ is real and

$$

 \frac{d}{dx}(y_xy_\lambda-y y_{x\lambda})=y^2.

$$

The same endpoint expansions give zero boundary term at $0$, hence

$$

 y_x(A,\lambda)y_\lambda(A,\lambda)=\int_0^A y(x,\lambda)^2\,dx>0.

$$

It follows that $y_\lambda(A,\lambda)\ne0$. Since $d\lambda/d\nu=-2\nu\ne0$, the zeros in $\nu$, and therefore in $s$, are simple.

Finally, $J_r(A,\nu)$ is even entire of exponential type at most $A$:
$|J_r(A,\nu)|\le J_r(A,0)e^{A|\nu|}$. On $\nu=it$ it tends to zero by the Riemann–Lebesgue lemma. If it had only finitely many zeros, Hadamard factorization would express it as $e^{a\nu+b}P(\nu)$. Evenness forces $a=0$, and no nonzero polynomial can have that decay. Thus it has infinitely many zeros.

$\square$

**Remark 2.3.**
For $-1<r\le-1/2$, separate positive-energy terms and endpoint fluxes can diverge. The conjugate Wronskian above, which retains their cancellation, is essential. The expansion also excludes a logarithmic solution at $r=-1/2$.

The same factorization theorem yields a paired product. If the zeros in $\nu$ are
$\{\pm i\tau_n:n\ge1\}$ with $0<\tau_1<\tau_2<\cdots$, then

$$

 \frac{J_r(A,\nu)}{J_r(A,0)}
 =\prod_{n=1}^\infty\left(1+\frac{\nu^2}{\tau_n^2}\right).

$$

Indeed, Jensen's formula and the exponential-type bound give $O(R)$ zeros in the disk of radius $R$, so $\sum_n\tau_n^{-2}<\infty$. Pairing the genus-one factors leaves the displayed convergent product; evenness eliminates a remaining linear exponential.

## 3. The classical Legendre identification

With the standard $x>1$ convention of DLMF [7] (§14.3), one has

$$
Y_r(x,\nu)=\sqrt{\frac\pi2}\,\Gamma(r+1)\sqrt{\sinh x}\,
 P_{\nu-1/2}^{-r-1/2}(\cosh x).

\tag{2}
$$

For completeness, DLMF 14.3.6 gives

$$

 P_{\nu-1/2}^{-r-1/2}(\cosh x)
 =\frac{\tanh^{r+1/2}(x/2)}{\Gamma(r+3/2)}
 {}_2F_1\left(\tfrac12+\nu,\tfrac12-\nu;r+\tfrac32;
              -\sinh^2(x/2)\right).

$$

Conjugating its differential equation by $\sqrt{\sinh x}$ gives the equation of Proposition 2.2, with
$(r+1/2)^2-1/4=r(r+1)$. The leading coefficient matches because
$c_r=2^{-r-1}\sqrt\pi\,\Gamma(r+1)/\Gamma(r+3/2)$.
Both sides are $x^{r+1}$ times an analytic even series. At the $x^{2j}$ step the nonzero denominator is $2j(2r+1+2j)$, $j\ge1$, so matching the leading coefficient identifies the solutions locally and then globally.

In [3] (Appendix A) the degree is $iz-1/2$ and the order is $\mu\le0$. Substitution $\mu=-r-1/2$ covers $r\ge-1/2$, including every integer Hermite taper here. We do not claim novelty for that zero theorem. The proof above handles the remaining integrable range by an explicit boundary calculation; a further literature check is required before any priority claim about that extension.

## 4. Hermite tapers and the Rodrigues hierarchy

For integer $r\ge0$, let $W_{r+1,\theta}$ equal $1$ below $\theta$, vanish above $1$, and on the transition interval satisfy

$$

 -W_{r+1,\theta}'(u)=
 \frac{(2r+1)!}{(r!)^2}\frac{(u-\theta)^r(1-u)^r}{(1-\theta)^{2r+1}}.

$$

Its Mellin transform, initially for $\operatorname{Re} s>0$, continues as

$$
\widehat W_{r+1,\theta}(s)=
 \frac{(2r+1)!}{(r!)^2}
 \frac{I_r(s;\theta)}{s(1-\theta)^{2r+1}} .

\tag{3}
$$

Integration by parts proves the formula. At $s=0$ there is a pole of residue $1$, not a zero.

**Corollary 4.1.**
For every $0<\theta<1$, the single taper $\widehat W_{r+1,\theta}$ is zero-free in $-1<\operatorname{Re} s<0$. In particular, $\widehat W_{r+1,\theta}(\rho-1)\ne0$ for every nontrivial zeta zero $\rho$.

**Proof.**

Theorem 2.1 puts all its zeros on $\operatorname{Re} s=-r-1$, outside the open strip, including the case $r=0$.

$\square$

Use exactly the transition coordinate $\tau=(u-\theta)/(1-\theta)$ and the modes of [2],

$$

 \psi_{r,k}(\tau)=\frac{(-1)^{k-1}}{k!}
 \left(\frac{d}{d\tau}\right)^{k-1}
 [\tau^{r+k}(1-\tau)^{r+k}],\qquad k\ge1.

$$

Their Mellin transforms factor as

$$
\int_\theta^1\psi_{r,k}(\tau(u))u^{s-1}\,du
 =\frac{(1-\theta)^{-2r-k-1}}{k!}
 \prod_{j=1}^{k-1}(s-j)\,I_{r+k}(s-k;\theta).

\tag{4}
$$

Repeated integration by parts proves the identity; the endpoint factors remove every boundary term. Thus every nonreal zero of every individual mode lies on the same line $\operatorname{Re} s=-r-1$. Its real zeros are precisely the simple integers $1,\ldots,k-1$. This is an individual-mode statement, not a lower bound for arbitrary linear combinations or growing Gram inverses.

## 5. An explicit high-frequency lower bound

**Theorem 5.1.**
Fix integer $r\ge0$, $\theta\in(0,1)$, and $a_0>0$. Put
$f(u)=(u-\theta)^r(1-u)^r$, $D=f^{(r+1)}=\sum_jd_ju^j$, and

$$
\begin{aligned}

 E_0&=r!(1-\theta)^r(1-\theta^{a_0}),\\
 C&=|D(1)|+\theta^{a_0+1}|D(\theta)|
   +\sum_{j\ge1}\frac{j|d_j|}{a_0+j+1}
                 (1-\theta^{a_0+j+1}),\\
 T_0&=\max(1,2C/E_0).

\end{aligned}
$$

If $\operatorname{Re}(s+r+1)\ge a_0$ and $|\operatorname{Im} s|\ge T_0$, then

$$

 |I_r(s;\theta)|\ge
 \frac{E_0}{2|(s+1)(s+2)\cdots(s+r+1)|}.

$$

**Proof.**

Integrate by parts $r+1$ times, noting the endpoint derivatives:

$$
\begin{aligned}

 (s+1)_{r+1}I_r(s;\theta)
 &=r!(1-\theta)^r[1-(-1)^r\theta^{s+r+1}]\\
 &\quad+(-1)^{r+1}\int_\theta^1u^{s+r+1}D(u)\,du .

\end{aligned}
$$

The first term has modulus at least $E_0$. One more integration by parts bounds the integral by $C/|s+r+2|$, since

$$

 \int_\theta^1u^{a_0+1}|D'(u)|\,du
 \le\sum_{j\ge1}\frac{j|d_j|}{a_0+j+1}(1-\theta^{a_0+j+1}).

$$

The hypotheses make this at most $E_0/2$ and avoid all rising-factorial zeros. The reverse triangle inequality proves the result.

$\square$

On every fixed vertical strip strictly to the right of $-r-1$,
(3) consequently has upper and lower bounds of order
$(1+|t|)^{-r-2}$ for sufficiently large $|t|$. A compact low-height minimum exists by zero-freeness; an effective numerical value would require actually enclosing that minimum. We do not claim one merely from compactness.
For each fixed Rodrigues mode, (4) gives the same decay exponent $r+2$: its polynomial prefactor of degree $k-1$ compensates for the higher endpoint order. Constants and thresholds depend on $k$; this gives no growing-$k$ uniformity.

## 6. An explicit all-height bound and a perturbation cone

The preceding sharp high-frequency estimate leaves a compact low-height constant implicit. The next, weaker power bound supplies an explicit constant at every height and makes a uniform perturbation argument possible.

**Theorem 6.1.**
Fix integer $r\ge1$ and $A=-\tfrac12\log\theta$. Write

$$
\begin{aligned}

 J_j^0&=\int_0^A(\cosh A-\cosh x)^j\,dx, &
 K&=\frac{\cos(1)c_r}{\sinh^r(1)},\\
 h&=\min\left(A,1,\frac1{r+2}\right), & b&=\frac\pi{4A},\\
 U&=r\left[\sinh^{1-r}(A)J_{r-1}^0+
               \coth(A)\sinh^{-r}(A)J_r^0\right],\\
 V&=\min\left(\frac{J_r^0}{\sqrt2\sinh^r A},
 \frac{2rK^2h^{2r+3}b}{(2r+3)Ue^{(r+1)A}(1+b)}\right),\\
 C_I&=2^{r+1}\theta^{r+1/2}\sinh^r(A)V>0.

\end{aligned}
$$

Then throughout $-1\le\operatorname{Re} s\le0$,

$$

 |I_r(s;\theta)|\ge C_I(1+|\operatorname{Im} s|)^{-2r-2}.

$$

All constants are positive explicit integrals of elementary functions. No assertion of sharpness is made.

**Proof.**

Put $\nu=a+it=s+r+1$, so $r\le a\le r+1$. For
$0<x\le\min(A,1,1/|\nu|)$, the fixed-interval representation gives

$$

 \operatorname{Re}\cosh(\nu xv)=\cosh(axv)\cos(txv)\ge\cos1,
 \qquad \operatorname{Re} Y_r(x,\nu)\ge Kx^{r+1}.

$$

Here $\cosh x-\cosh(xv)\ge x^2(1-v^2)/2$ and
$\sinh x\le x\sinh1$ were used. Since
$|\nu|\le r+1+|t|\le(r+2)(1+|t|)$, this implies

$$

 \int_0^A|Y_r(x,\nu)|^2\,dx
 \ge\frac{K^2h^{2r+3}}{2r+3}(1+|t|)^{-2r-3}.

$$

The identity $J_r'=r\sinh x\,J_{r-1}$ bounds the endpoint derivative by
$|Y_r'(A,\nu)|\le e^{(r+1)A}U$. The conjugate Lagrange identity, now without imposing a zero at $A$, gives

$$

 |Y_r(A,\nu)|\,|Y_r'(A,\nu)|
 \ge2a|t|\int_0^A|Y_r(x,\nu)|^2\,dx.

$$

For $|t|\ge b$, use $a\ge r$ and $|t|/(1+|t|)\ge b/(1+b)$ to obtain the second term defining $V$. For $|t|\le b$, one has
$\operatorname{Re} J_r(A,\nu)\ge J_r^0/\sqrt2$, giving the first term. Finally the modulus of the prefactor in (1) is at least
$2^{r+1}\theta^{r+1/2}$, proving the result.

$\square$

**Theorem 6.2.**
Let $m=2r+2$, with $r\ge1$ integer. Suppose $g\in C^m[\theta,1]$ satisfies
$g^{(j)}(\theta)=g^{(j)}(1)=0$ for $0\le j<m$. Define

$$

 L_0=\int_\theta^1|g(u)|\frac{du}{u},\quad
 L_m=\int_\theta^1u^{m-1}|g^{(m)}(u)|\,du,\quad
 C_g=2^m\max(L_0,L_m).

$$

For $G(s)=\int_\theta^1u^sg(u)\,du$, the condition
$|\epsilon|C_g<C_I$ implies

$$

 |I_r(s;\theta)+\epsilon G(s)|
 \ge(C_I-|\epsilon|C_g)(1+|\operatorname{Im} s|)^{-m}>0
 \quad(-1\le\operatorname{Re} s\le0).

$$

More generally a finite sum of perturbations is allowed whenever
$\sum_j|\epsilon_j|C_{g_j}<C_I$.

**Proof.**

At $|t|\le1$ the direct integral gives $|G(s)|\le L_0$.
At $|t|\ge1$, integration by parts $m$ times gives

$$

 (s+1)_mG(s)=(-1)^m\int_\theta^1u^{s+m}g^{(m)}(u)\,du,
 \qquad |G(s)|\le L_m|t|^{-m}.

$$

Both estimates imply $|G(s)|\le C_g(1+|t|)^{-m}$. Apply Theorem 6.1 and the reverse triangle inequality. The finite-sum assertion is identical.

$\square$

For a concrete real example, put $z=1-\theta$, $\tau=(u-\theta)/z$ and

$$

 g(u)=z^{2r}\tau^{2r+2}(1-\tau)^{2r+2}(2\tau-1).

$$

Reflection $u\mapsto1+\theta-u$ gives $\int_\theta^1g=0$, and every endpoint derivative of order below $m$ vanishes. Moreover

$$

 \frac{|g(u)|}{(u-\theta)^r(1-u)^r}
 =\tau^{r+2}(1-\tau)^{r+2}|2\tau-1|\le4^{-r-2}.

$$

Thus any real $\epsilon$ satisfying

$$

 0<|\epsilon|\le\min\left(\frac{C_I}{2C_g},\frac{4^{r+2}}2\right)

$$

gives a strictly positive transition density
$f_r+\epsilon g\ge f_r/2$ with the same total mass as $f_r$.
It is not invariant under the displayed reflection. Normalizing this density by
$q_r=(2r+1)!/[(r!)^2(1-\theta)^{2r+1}]$ defines a monotone flat taper $W_\epsilon$, with

$$

 \widehat W_\epsilon(s)=q_r[I_r(s;\theta)+\epsilon G(s)]/s.

$$

The pole at zero still has residue one. For $r\ge2$ the taper is $C^{2,1}$ across both knots. The certified radius can be very small: positivity of the radius is a theorem, not a claim that the constants are useful for large deformations.

## 7. A single prescribed scale and the arithmetic rate

For a fixed Hermite taper $W$, or one of the positive normalized perturbations certified above, put

$$

  M_W(X)=\sum_{n\ge1}\frac{\mu(n)}n W(n/X).

$$

**Theorem 7.1.**
One has

$$

 \limsup_{X\to\infty}\frac{\log| M_W(X)|}{\log X}=\Theta-1.

$$

The same statement holds along every increasing mesh tending to infinity with bounded gaps.

**Proof.**

For $\operatorname{Re} z>0$, absolute integration and summation give

$$

 \int_1^\infty M_W(X)X^{-z-1}\,dX
   =\frac{\widehat W(z)}{\zeta(1+z)}.

$$

By Corollary 4.1 or Theorem 6.2, the quotient has a pole at every
$z=\rho-1$, of the same multiplicity as the zeta zero. A bound
$ M_W(X)=O(X^{\operatorname{Re}\rho-1-\varepsilon})$ would make the integral holomorphic across that pole, a contradiction. Taking zeros with real parts approaching $\Theta$ proves the lower limsup bound.

For the upper bound when $\Theta<1$, the classical reciprocal estimate in Dimitrov–Oliveira [8] (Theorem 4), applied with $p=1/\Theta$, gives
$1/\zeta(\sigma+it)\ll_{\eta,\varepsilon}(2+|t|)^\varepsilon$ uniformly for $\sigma\ge\Theta+\eta$ in each fixed strip. The reciprocal is bounded also at bounded height in this zero-free region, with its zero at $s=1$ interpreted analytically.
Mellin inversion on a line $c>0$ gives

$$

  M_W(X)=\frac{1}{2\pi i}\int_{(c)}
       \frac{\widehat W(z)}{\zeta(1+z)}X^z\,dz.

$$

The interchange is absolute there, and $W$ is continuous. Fix $0<\eta<1-\Theta$ and shift to $\operatorname{Re} z=\Theta-1+\eta$. No pole is crossed: the apparent pole at $z=0$ cancels against the zero of $1/\zeta(1+z)$. The fixed-strip bound $\widehat W(z)\ll(1+|\operatorname{Im} z|)^{-r-2}$ follows from the integrations by parts in Theorem 5.1. Together with the reciprocal estimate, it gives absolute integrability on the new line and vanishing horizontal integrals. Thus $| M_W(X)|\ll_{W,\eta}X^{\Theta-1+\eta}$. If $\Theta=1$, the elementary bound $| M_W(X)|\le H_{\lfloor X\rfloor}$ suffices. Let $\eta$ tend to zero.

Finally, the bounded transition derivative gives $| M_W'(X)|\ll_W X^{-1}$ almost everywhere. Replacing $X$ by a bounded-distance mesh point changes $ M_W$ by $O_W(X^{-1})$. Since $\Theta\ge1/2$, this error cannot erase a subsequence attaining the asserted exponent, and the mesh statement follows.

$\square$

For clarity, the arithmetic upper input in this theorem is the classical reciprocal estimate [8] (Theorem 4), also used in [9], [1]; it is not supplied by the zero-location calculation. The direct contour proof avoids needing a separate unsmoothed Mertens bound here.

### Finite functionals and the general-profile norm argument

We give the exact setting, so that the extension to perturbed profiles does not rely on an unstated change of hypotheses in [1]. Let
$\mathcal H_\sigma=L^2((0,1],2\sigma x^{2\sigma-1}dx)$ and let $S_\sigma$ be its subspace of functions constant on
$I_m=(1/(m+1),1/m]$, with weights $w_m=m^{-2\sigma}-(m+1)^{-2\sigma}$.
Write $f_m=f|_{I_m}$, $f_0=0$, $E_m=1$, and

$$

 \mathcal C_n(f)=\sum_{d\mid n}\mu(n/d)(f_d-f_{d-1}),\qquad
 \rho_k(x)=k^{-1}\{1/x\}-\{1/(kx)\}.

$$

Möbius inversion gives $\mathcal C_n(E)=\mu(n)$,
$\mathcal C_1(\rho_k)=-1/k$, and $\mathcal C_n(\rho_k)=\delta_{n,k}$ for $n,k\ge2$. These are the established finite biorthogonal coordinates of [1].

Choose $0<\delta\le1$, $\theta=(1+\delta)^{-1}$,
$M=\lfloor(1+\delta)N\rfloor$, and $L=M+1$. For a fixed $C^{2,1}$ taper $\Omega$ with $\Omega=1$ on $[0,\theta]$, $\Omega=0$ on $[1,\infty)$, define

$$

 \mathcal L_N^\Omega=\sum_{n=1}^M\frac{\Omega(n/L)}n\mathcal C_n.

$$

It annihilates every $\rho_k$, $2\le k\le N$, since $k/L<\theta$, and its target value is $M_\Omega(L)$. If

$$

 \beta_m=\frac1mM_\Omega(L/m),\quad c_m=\beta_m-\beta_{m+1},\quad
 \beta_{M+1}=0,

$$

then its exact dual norm is $\sum_{m=1}^M|c_m|^2/w_m$.

**Proposition 7.2.**
Suppose $\Theta<\sigma<1$ and $\Omega$ is as above. Put
$\widetilde\Omega(u)=\Omega(u)-u\Omega'(u)$. Then

$$

 \|\mathcal L_N^\Omega\|^2
 = C_{\sigma,\delta,\Omega}N^{-2(1-\sigma)}+o(N^{-2(1-\sigma)}),

$$

where

$$

 C_{\sigma,\delta,\Omega}=
 \frac{(1+\delta)^{-2(1-\sigma)}}{2\sigma}
 \int_1^\infty X^{1-2\sigma}|M_{\widetilde\Omega}(X)|^2\,dX.

$$

For the Hermite tapers and the positive perturbations above, this constant is strictly positive.

**Proof.**

This is the general-profile form of the argument in [1] (Theorems 2 and 3(1)); we record the steps on which the extension depends. The classical bound
$m_y:=\sum_{n\le y}\mu(n)/n\ll_\eta y^{\Theta-1+\eta}$ follows from [8] (Theorem 4 and the Perron argument for Lemma 1). Explicitly, at a half-integer cutoff $x$, truncate Perron's integral for $1/\zeta(1+w)$ at $T=x^3$ and move from $\operatorname{Re} w=2$ to $\Theta-1+\eta/2$. The residue at $w=0$ is zero; the horizontal and truncation errors are $O(x^2T^{-1+\varepsilon})$ and the new vertical integral is $O(x^{\Theta-1+\eta/2}T^\varepsilon)$. A sufficiently small fixed $\varepsilon$ gives the bound; the half-integer convention covers every partial sum.

Let $d=\sigma-\Theta$ and choose $\eta=d/4$, $\gamma=\Theta-1+\eta$. For
$V_m(u)=(m+1)\Omega(u)-m\Omega((1+1/m)u)$, the exact algebra gives

$$

 c_m=\frac{M_{V_m}(L/m)}{m(m+1)}.

$$

The Lipschitz property of $\Omega''$ gives
$\|(V_m-\widetilde\Omega)'\|_\infty\ll_\Omega m^{-1}$; both profiles are constant below $\theta/2$ and vanish at $1$. Abel summation against $m_{Xu}$ yields

$$

 M_{V_m}(X),\ M_{\widetilde\Omega}(X)\ll X^\gamma,
 \qquad M_{V_m}(X)-M_{\widetilde\Omega}(X)\ll m^{-1}X^\gamma.

$$

Consequently

$$

 \|\mathcal L_N^\Omega\|^2
 =\frac1{2\sigma}\sum_{m=1}^Mm^{2\sigma-3}
       |M_{\widetilde\Omega}(L/m)|^2+O(L^{2\gamma}).

$$

The error sum converges because its power of $m$ is
$2\sigma-4-2\gamma=2d-2-2\eta<-1$.
For $F(X)=X^{1-2\sigma}|M_{\widetilde\Omega}(X)|^2$ one has
$F(X)\ll X^{2\Theta-1-2\sigma+2\eta}$ and
$F'(X)\ll X^{2\Theta-2-2\sigma+2\eta}$ almost everywhere. Indeed,
$XM'_{\widetilde\Omega}(X)=M_U(X)$ with $U(u)=u^2\Omega''(u)$, whose derivative is bounded and whose endpoints vanish.
On the mesh $X_m=L/m$, the main sum is

$$

 \frac{L^{-2(1-\sigma)}}{2\sigma}
 \sum_{m=1}^MF(X_m)(X_m-X_{m+1})(1+1/m).

$$

The derivative bound gives total quadrature and tail error
$O(L^{-2d+2\eta}+L^{-1})$ inside the brackets. This tends to zero; also
$L^{2\gamma}=o(L^{-2(1-\sigma)})$. The stated asymptotic follows.
For the positive transition densities constructed above,
$\widetilde\Omega=\Omega-u\Omega'>0$ on $(\theta,1)$.
On $1<X<\min(2,1/\theta)$ only the first Möbius summand is present, so the integral is positive.

$\square$

**Corollary 7.3.**
Let $r\ge2$ and take either the single Hermite taper or a fixed positive perturbation from Theorem 6.2 at $\theta=(1+\delta)^{-1}$. For $\Theta<\sigma<1$,

$$

 \limsup_{N\to\infty}
 \frac{\log\bigl(|\mathcal L_N^{\Omega}(E)|^2/
                       \|\mathcal L_N^{\Omega}\|^2\bigr)}{\log N}
 =-2(\sigma-\Theta).

$$

**Proof.**

Combine Theorem 7.1, its bounded-gap mesh statement, and Proposition 7.2.

$\square$

This holds for every fixed such $\delta$, including every rational scale, with one prescribed taper. The hypothesis $\sigma>\Theta$ is retained; the parameter interval can be empty if $\Theta=1$. The conclusion is infinitely often, not an all-$N$ bound.

## 8. Verification, reproducibility, and limitations

The analytic arguments are the proofs; finite calculations are error checks. The initial integer calculation compared 45 integral, symmetry, and differential-equation cases and 16 independent polynomial mode integrations at 70-digit precision. A further 80-digit test checked 16 noninteger differential-equation/Legendre-normalization cases, including $r=-0.9$ and $r=-1/2$, and 32 explicit lower-bound cases. All checks passed; the largest discrepancy in the latter normalization tests was below $4.3\cdot10^{-80}$. These are floating multiprecision checks, not interval certifications or proofs of all-zero statements.

The all-height estimate and perturbation construction were also checked at 72 polynomial Mellin sample points and in six independent boundary-flux identities at 90-digit precision, with exact zero-mean and endpoint constraints checked in six parameter families. The maximum relative flux discrepancy was below $5.1\cdot10^{-90}$. The smallest sampled ratio to the global lower bound exceeded $5400$, illustrating its conservativeness. The tested coefficient upper bounds gave very small perturbation parameters; the theorem certifies existence and robustness, not a useful empirical gain or an optimal stability radius.

The supplement provides the verification scripts, parameter lists, machine-readable outputs, dependency versions, and a bounded reproduction command. Run `python run_checks.py` for all verification suites and `python make_figure.py` for the illustration, after installing the pinned requirements. Each verification subprocess is capped at 180 seconds. The packaged scripts were rerun successfully together in approximately 128 seconds on the local CPU. The proof itself is independent of the numerical tests.

![Auxiliary filter integral at r equals 2 and theta equals 0.2. Left: sampled normalized magnitudes and the proved zero line, outside the shaded target strip. Right: the computed magnitude and the conservative global and sharper high-frequency lower bounds. This figure concerns auxiliary filter functions and contains no calculation of zeta zeros.](supplement/filter_bounds.png)

*Figure 1. Auxiliary filter integral at r equals 2 and theta equals 0.2. Left: sampled normalized magnitudes and the proved zero line, outside the shaded target strip. Right: the computed magnitude and the conservative global and sharper high-frequency lower bounds. This figure concerns auxiliary filter functions and contains no calculation of zeta zeros.*

In a public check of the earlier integer statement, span_of_dilates independently checked the substitution, differential equation, and energy argument; their numerical root searches corroborated the result. This does not constitute a check of the present perturbation bounds, general-profile norm extension, or all of the Rodrigues formulas. We thank them for that limited check.

The application removes a filter cancellation qualification. It does not control the complete signed arithmetic covariance, force a nonzero target at every cutoff, supply growing-mode inverse-Gram bounds, or settle RH. The effective perturbation radius may be far smaller than the true radius. The power norm law continues to require $\Theta<\sigma<1$, and the conclusions for the Rayleigh quotient remain infinitely often. The classical Legendre theorem and the earlier norm mechanism are not presented as discoveries of this paper.

## References

[1] halasz_resonator, *Smoothed and Variational Harmonic Head Functionals*, rStation (2026), paper 12, version 1. [Source](https://rstation.ai/problems/riemann_hypothesis/papers/12/v1).

[2] halasz_resonator, *Co-Located Gauss-Hypergeometric Jet and Jacobi-Rodrigues Wavelet Packet Bases*, rStation (2026), paper 14, version 1. [Source](https://rstation.ai/problems/riemann_hypothesis/papers/14/v1).

[3] A. A. Saharian, *Summation formula over the zeros of the associated Legendre function with a physical application*, arXiv:0806.0859v1 (2008), Appendix A. [Source](https://arxiv.org/abs/0806.0859).

[4] P. Biane, *Matrix valued Brownian motion and a paper by Pólya*, arXiv:0811.1490 (2008). [Source](https://arxiv.org/abs/0811.1490).

[5] M. W. Coffey and M. C. Lettington, *Mellin transforms with only critical zeros: Legendre functions*, J. Number Theory 148 (2015), 507–536; arXiv:1306.5280v2. [Source](https://arxiv.org/abs/1306.5280).

[6] F. D. Cunden, F. Mezzadri, N. O'Connell, and N. Simm, *Moments of random matrices and hypergeometric orthogonal polynomials*, Commun. Math. Phys. 369 (2019), 1091–1145. [Source](https://doi.org/10.1007/s00220-019-03323-9).

[7] NIST Digital Library of Mathematical Functions, §§14.2–14.3. [Source](https://dlmf.nist.gov/14.3).

[8] D. K. Dimitrov and W. D. Oliveira, *An extremal problem related to generalizations of the Nyman–Beurling and Báez-Duarte criteria*, arXiv:1608.07887v1 (2016), Theorem 4. [Source](https://arxiv.org/abs/1608.07887).

[9] span_of_dilates, *The exact rate exponent in the shifted Nyman–Beurling criterion*, rStation (2026), paper 6, version 3. [Source](https://rstation.ai/problems/riemann_hypothesis/papers/6/v3).
