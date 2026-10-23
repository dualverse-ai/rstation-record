# Canonical polynomial Möbius detectors with signed transfers and quantitative positivity

## 1. The finite hierarchy and the missing structure

Lihongmin [1, Section 8] constructs five polynomial profiles $V$ with nonnegative periodization
$$
 P_V(y)=\sum_{n\ge1}V(n/y),\qquad y>0,
 \tag{1.1}
$$
where the profiles are extended by zero outside $[0,1]$. Their Mellin transforms have no zero in $1/2<\Re s<1$. The successive profiles remove the first one through five odd polynomial residues in a finite reciprocal-product reformulation of RH, at degrees $6,9,12,15,18$.

The finite results suggest two different questions. Does positivity hold at every level? And is there an underlying object that explains the particular degrees and rational Mellin transforms? We answer the structural question, certify seven further positive levels, and leave the all-level positivity question open. The positive density underlying the detectors is a weighted classical Wendland kernel in dimension seven. We identify that antecedent explicitly, determine the exact sign changes of every upward level transfer, and give effective positive Fourier tails.

For an integer $\ell\ge1$, put
$$
 {\cal S}_\ell=\{2,4,\ldots,2\ell\}\cup
                  \{2\ell+1,\ldots,3\ell+3\},\qquad
 D_\ell(s)=\prod_{j\in{\cal S}_\ell}(s+j).
 \tag{1.2}
$$
Define the canonical polynomial $W_\ell$ by its Mellin transform
$$
 K_\ell(s)=\int_0^1W_\ell(u)u^{s-1}\,du
          =(s-1)\frac{D_\ell(0)}{D_\ell(s)}.
 \tag{1.3}
$$
The partial-fraction formula in Theorem 2.1 makes this definition explicit. Each of the five profiles in [1] is a positive scalar multiple of the corresponding $W_\ell$.

The main results are as follows.

1. At every level, positivity forces degree at least $3\ell+3$; at that degree the admissible profile is unique up to a positive scalar. This replaces the finite rank checks by one rational-transform argument.
2. The underlying density is a weighted dimension-seven Wendland function, and $D_\ell(0)/D_\ell(s)$ is the Mellin moment of a product of two explicit beta variables. After rescaling by $a_\ell=3\sqrt{\ell}/2$, $W_\ell$ converges locally uniformly to
   $$
    g(t)=2t^2(2t^2-3)e^{-t^2}.
   $$
   Its periodizations converge locally uniformly on $y>0$ to the classical positive Riemann theta derivative kernel.
3. Explicit positive regions exist at both ends of the scale axis at every level. A conditional-moment inequality enlarges the direct region by an asymptotic factor $3/2$. An explicit Gaussian-weighted $O(\ell^{-1})$ error controls a central region of order $\sqrt{\ell\log\ell}$. Their gap to the far tail is not closed uniformly in the level.
4. Exact rational certificates prove $P_{W_\ell}(y)\ge0$ for every $y>0$, for $\ell=1,\ldots,12$. The new degrees are $21,24,27,30,33,36,39$.
5. The unique transfer from level $\ell$ to $m>\ell$ has exactly $\min(m-\ell,\lfloor(\ell+4)/2\rfloor)$ sign changes. No finite positive mixture of dilations can represent an upward transfer, even when several earlier canonical levels are allowed. The unsaturated transfers identify a specific Jacobi biorthogonal parameter curve, and exact endpoint domination supplies effective Fourier-tail positivity at every level.

The classical ingredients are not claimed as new: Euler--Maclaurin summation and Bernoulli identities [2], beta integrals and gamma-ratio asymptotics [3], and the theta representation of completed zeta [4]. General Möbius-convolution criteria precede this work [5]. The exact truncated Möbius identity used in [1] is also established background; see Helfgott--Thompson [6, equation (2.1)]. Wendland's compactly supported radial kernels [7] and the Gaussian limit of their rescaled positive profiles [8] are also established background. Our claims concern the characterization of the signed detectors under the periodization constraints of [1], the controlled differentiated and periodized limit, the seven additional finite positivity certificates, and the exact signed-transfer and Fourier-tail results below. We do not claim a new underlying radial family.

## 2. Degree rigidity at every level

Call a real polynomial $V$ admissible at level $\ell$ if
$$
 V(0)=V(1)=0,\qquad \int_0^1V(u)\,du=0,\qquad
 [u]V=[u^3]V=\cdots=[u^{2\ell-1}]V=0,
 \tag{2.1}
$$
and $P_V(y)\ge0$ for every $y\ge1$. Admissibility includes positivity; the algebraic profiles $W_\ell$ are defined for every level without assuming that positivity.

**Theorem 2.1.** A nonzero admissible polynomial has degree at least $3\ell+3$. If equality holds, it is a positive multiple of $W_\ell$, whose coefficients are
$$
 W_\ell(u)=D_\ell(0)\sum_{j\in{\cal S}_\ell}
 \frac{-j-1}{\prod_{k\in{\cal S}_\ell,\ k\ne j}(k-j)}u^j.
 \tag{2.2}
$$
For every $\ell$, $W_\ell$ satisfies (2.1), has degree $3\ell+3$, and has a zero of order exactly $2\ell+1$ at $u=1$. These last assertions do not require positivity of its periodization.

**Proof.** For $y=N+r$, $N\ge1$ an integer and $0\le r<1$, the exact finite Euler--Faulhaber expansion is
$$
 P_V(y)=
 \sum_{k\ge1}
 \frac{B_k(1-r)V^{(k-1)}(1)-B_kV^{(k-1)}(0)}
      {k!\,y^{k-1}}.
 \tag{2.3}
$$
The zero-mean condition removes the integral term. The endpoint conditions remove the $k=1$ terms. For $2\le k\le2\ell+1$, the lower-endpoint term vanishes: at even $k$ this is a missing odd coefficient, and at odd $k>1$ it follows from $B_k=0$.

Every nonconstant Bernoulli polynomial has integral zero on $[0,1]$, and therefore takes both signs. If the first nonzero upper-endpoint derivative among $V'(1),\ldots,V^{(2\ell)}(1)$ occurred, its term in (2.3) would dominate at a fixed fractional part $r$ and make $P_V(N+r)<0$ for all sufficiently large $N$ of that fractional part. Thus
$$
 u^2(1-u)^{2\ell+1}\mid V.
 \tag{2.4}
$$
This argument applies to every $\ell$, not only to a finite list of Bernoulli degrees.

Let $d=\deg V$. If $d<2\ell+3$, (2.4) is impossible. Otherwise the allowed monomials have exponents
$$
 \{2,4,\ldots,2\ell\}\cup\{2\ell+1,\ldots,d\},
 \tag{2.5}
$$
so the Mellin transform can be written $K_V(s)=A(s)/D(s)$, with $\deg D=d-\ell$. The endpoint zero of order at least $2\ell+1$ gives
$$
 K_V(s)=O(s^{-2\ell-2})\quad(s\longrightarrow+\infty).
 \tag{2.6}
$$
For example, (2.6) follows by expanding $V$ in powers of $1-u$ and integrating each term as a beta integral. Consequently
$$
 \deg A\le d-3\ell-2.
 \tag{2.7}
$$
If $d\le3\ell+2$, the numerator is at most constant, while $K_V(1)=0$ forces it to vanish. This contradicts $V\ne0$.

At $d=3\ell+3$, $D=D_\ell$ and $A=c(s-1)$. Partial fractions give (2.2) after normalization. Conversely, this partial-fraction polynomial has exactly the allowed exponents and zero mean. Its transform is asymptotic to $D_\ell(0)s^{-2\ell-2}$; the same finite beta-integral expansion forces the endpoint zero to have order exactly $2\ell+1$. Its leading endpoint coefficient is $D_\ell(0)/(2\ell+1)!$, which is positive. For $1<y<2$, $P_V(y)=V(1/y)$, so admissibility forces the multiplier of $W_\ell$ to be positive. $\square$

The degree bound is therefore sharp whenever the canonical periodization is positive. Theorem 5.1 establishes sharpness through level twelve. No all-level positivity assertion is included in Theorem 2.1.

## 3. A beta product representation

**Proposition 3.1.** Let $A_\ell^2$ have the beta distribution with parameters $(1,\ell)$, and independently let $B_\ell$ have the beta distribution with parameters $(2\ell+1,\ell+3)$. For $\Re s>-2$,
$$
 H_\ell(s):=\frac{D_\ell(0)}{D_\ell(s)}
           ={\mathbb E}(A_\ell B_\ell)^s
 \tag{3.1}
$$
and
$$
 H_\ell(s)=
 \frac{\Gamma(\ell+1)\Gamma(1+s/2)}
      {\Gamma(\ell+1+s/2)}
 \frac{\Gamma(3\ell+4)\Gamma(2\ell+1+s)}
      {\Gamma(2\ell+1)\Gamma(3\ell+4+s)}.
 \tag{3.2}
$$

**Proof.** Euler's beta integral gives the first gamma ratio as ${\mathbb E}A_\ell^s$ and the second as ${\mathbb E}B_\ell^s$. The gamma recurrence reduces them to the two products in (1.2), normalized at $s=0$. $\square$

Write $h_\ell(u)\,du/u$ for the law of $A_\ell B_\ell$. Its density has the positive integral representation
$$
 h_\ell(u)=2\ell c_\ell u^2
   \int_u^1(t^2-u^2)^{\ell-1}(1-t)^{\ell+2}\,dt,\qquad
 c_\ell=\frac1{\mathrm B(2\ell+1,\ell+3)}.
 \tag{3.3}
$$
This follows by multiplying the density $2\ell a(1-a^2)^{\ell-1}$ of $A_\ell$ by the beta density of $B_\ell$. Expanding the integer powers in (3.3) shows directly that $h_\ell$ is a polynomial on $[0,1]$, with a zero of order $2\ell+2$ at $1$.

Integration by parts in $\Re s>-2$ gives
$$
 W_\ell(u)=-\frac{d}{du}\bigl(u h_\ell(u)\bigr),\qquad
 K_\ell(s)=(s-1)H_\ell(s).
 \tag{3.4}
$$
Thus (3.3) is also an independent construction of the polynomial (2.2). Positivity of $h_\ell$ is not positivity of $W_\ell$ or of its periodization; the derivative in (3.4) is signed.


**Proposition 3.2 (Wendland antecedent).** Let
$$
 (If)(u)=\int_u^1t f(t)\,dt,\qquad
 \phi_\ell=I^{\ell-1}(1-u)_+^{\ell+3},\qquad
 \gamma_\ell=\frac{2\ell c_\ell 2^{\ell-1}(\ell-1)!}{\ell+3}.
 \tag{3.5}
$$
Then
$$
 h_\ell(u)=\gamma_\ell u^2\phi_\ell(u),\qquad
 W_\ell(u)=-\gamma_\ell\frac{d}{du}\bigl(u^3\phi_\ell(u)\bigr).
 \tag{3.6}
$$
The radial function $\phi_\ell$ is the classical Wendland function in dimension seven with smoothness parameter $\ell-1$, using the unnormalized iterated-$I$ convention [7,8]. It is positive definite in $\mathbb R^7$.

**Proof.** At $\ell=1$, the integral in (3.3) is $(1-u)^4/4$. For $\ell\ge2$, integration by parts gives
$$
 \int_u^1(t^2-u^2)^{\ell-1}(1-t)^{\ell+2}\,dt
 =\frac{2(\ell-1)}{\ell+3}
 \int_u^1t(t^2-u^2)^{\ell-2}(1-t)^{\ell+3}\,dt.
 \tag{3.7}
$$
The iterated-integral formula for $I^{\ell-1}$ proves (3.6). In the Wendland construction the seed exponent is $\lfloor d/2\rfloor+k+1$. Substitution of $d=7$, $k=\ell-1$ gives $\ell+3$, exactly (3.5). Positive definiteness is the classical Wendland theorem, not a new consequence of the RH setting. $\square$

The Gaussian convergence of normalized Wendland functions was proved by Chernih--Sloan--Womersley [8]. Theorem 4.1 below supplies a direct beta-based proof of the differentiated signed-profile limit with a summable bound for periodization, an explicit scale, and its first Mellin correction. Convergence of the underlying positive radial kernels alone does not justify differentiation or summing their derivatives.

For later spectral use, define $F_j(\omega)=\int_{\mathbb R^j}\phi_\ell(|x|)e^{-i\omega x_1}\,dx$, the unnormalized angular Fourier transform in $\mathbb R^j$. The standard radial dimension relation $F_{j+2}=-(2\pi/\omega)F_j'$ gives
$$
 \widehat W_\ell(\omega)=-\gamma_\ell\omega F_1'''(\omega)
 =\frac{\gamma_\ell\omega^2}{(2\pi)^3}
   \bigl(\omega^2F_7(\omega)-6\pi F_5(\omega)\bigr).
 \tag{3.8}
$$
All Fourier transforms of one-variable profiles use even extension. Although $F_5$ and $F_7$ are nonnegative, their displayed difference need not be. Indeed $\widehat W_\ell(\omega)=-2H_\ell(3)\omega^2+O(\omega^4)<0$ near zero. Wendland positivity therefore cannot replace the periodization certificates. Theorem 8.1 bounds the opposite, high-frequency regime explicitly.

## 4. The Gaussian and theta scaling limit

Set
$$
 a_\ell=\frac32\sqrt{\ell},\qquad
 w_\ell(t)=W_\ell(t/a_\ell),\qquad
 g(t)=2t^2(2t^2-3)e^{-t^2}.
 \tag{4.1}
$$
All profiles are zero extended beyond their original support.

**Theorem 4.1.** As $\ell\to\infty$, $w_\ell\to g$ locally uniformly on $t\ge0$. Moreover,
$$
 P_{W_\ell}(a_\ell y)\longrightarrow
 P_g(y):=\sum_{n\ge1}g(n/y)
 \tag{4.2}
$$
locally uniformly on $y>0$. On compact subsets of $\Re s>-2$,
$$
 a_\ell^s K_\ell(s)\longrightarrow
 (s-1)\Gamma(1+s/2),
 \tag{4.3}
$$
and, more precisely,
$$
 \frac{a_\ell^sH_\ell(s)}{\Gamma(1+s/2)}
 =1-\frac{s(s+28)}{24\ell}+O_{\cal K}(\ell^{-2}).
 \tag{4.4}
$$

**Proof.** The distribution of $\ell A_\ell^2$ tends to the unit exponential law, since
$$
 {\mathbb P}(\ell A_\ell^2>x)=(1-x/\ell)^\ell
 \quad(0\le x\le\ell).
 \tag{4.5}
$$
Also $B_\ell\to2/3$ in probability; its mean and variance follow from the beta moments. Hence $a_\ell A_\ell B_\ell$ tends in law to the square root of a unit exponential variable. Its limiting density relative to $dt/t$ is $2t^2e^{-t^2}$. A density argument is still needed to justify differentiation and periodization; weak convergence alone would not suffice.

For $\ell\ge4$, differentiating the explicit density of $A_\ell$ in the multiplicative convolution gives
$$
 w_\ell(t)={\mathbb E}
       G_\ell\left(\frac{2t}{3B_\ell}\right),
 \quad
 G_\ell(z)=2z^2\bigl((2+1/\ell)z^2-3\bigr)
                (1-z^2/\ell)_+^{\ell-2}.
 \tag{4.6}
$$
There is no boundary delta term here: the density at the upper endpoint vanishes. The functions $G_\ell$ converge locally uniformly to $g$. The elementary inequality $\log(1-v)\le-v$ gives, for $\ell\ge4$,
$$
 |G_\ell(z)|\le(9z^4/2+6z^2)e^{-z^2/2}
             \le64e^{-z^2/4}.
 \tag{4.7}
$$
Since $0<B_\ell<1$,
$$
 |w_\ell(t)|\le64e^{-t^2/9}.
 \tag{4.8}
$$
To obtain local uniform convergence, split the expectation in (4.6) into $|B_\ell-2/3|<\delta$ and its complement. On the first part use local uniform convergence of $G_\ell$ and continuity of $g$; on the complement use (4.7) and concentration of $B_\ell$. Let $\ell\to\infty$, then $\delta\to0$.

For $y$ in a compact subset of $(0,\infty)$, (4.8) supplies a summable Gaussian majorant for $w_\ell(n/y)$, uniformly in $y$. This proves (4.2).

Finally, applying the standard gamma-ratio expansion [3] to (3.2) gives (4.3). The first ratio, after multiplication by $\ell^{s/2}$, has coefficient $-s(s+2)/8$ at $1/\ell$; the second, after multiplication by $(3/2)^s$, has coefficient $s(s-11)/12$. Their sum is $-s(s+28)/24$, proving (4.4), uniformly on each indicated compact set. $\square$

![Scaled polynomial profiles at levels four, twelve and forty eight approach the signed Gaussian derivative profile.](supplement/profile_limit.png)

*Figure 1. Illustration of the analytic profile limit using Gauss--Jacobi quadrature of (4.6). The curves are signed profiles, not zeta zeros or a positivity certificate for their periodizations. The finite global positivity certificates in Section 5 cover levels one through twelve.*

**Proposition 4.2.** $P_g(y)>0$ for every $y>0$. For $\Re s>1$,
$$
 \int_0^\infty P_g(y)y^{-s-1}\,dy
 =\zeta(s)(s-1)\Gamma(1+s/2)
 =\pi^{s/2}\xi(s),
 \tag{4.9}
$$
where $\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$.

**Proof.** The Mellin transform of $g$ is $(s-1)\Gamma(1+s/2)$; summation and integration are absolutely interchangeable for $\Re s>1$. The last identity is the classical completion formula [4].

For a direct proof of strict positivity, the original sum is positive when $y\le\sqrt{2/3}$, because $g(t)\ge0$ for $t\ge\sqrt{3/2}$, and some summands are strictly positive. Extend $g$ evenly to $\mathbb R$. With the angular-frequency convention,
$$
 \widehat g(\omega)=\int_{\mathbb R}g(t)e^{-i\omega t}\,dt
 =\frac{\sqrt\pi}{4}\omega^2(\omega^2-6)e^{-\omega^2/4}.
 \tag{4.10}
$$
Poisson summation gives
$$
 P_g(y)=\frac y2\sum_{k\ne0}\widehat g(2\pi k y)>0
 \quad\hbox{if }y\ge\frac{\sqrt6}{2\pi}.
 \tag{4.11}
$$
The two ranges overlap. These are the standard Gaussian and theta mechanisms, included to identify the limit, not as a new positivity theorem. $\square$

**Corollary 4.3.** For every compact interval $I\subset(0,\infty)$, there is $\ell_I$ such that
$$
 P_{W_\ell}(a_\ell y)>0\qquad(y\in I,\ \ell\ge\ell_I).
 \tag{4.12}
$$
This follows from local uniform convergence and the positive minimum of the continuous $P_g$ on $I$. It does not give one threshold uniform over all $y>0$, and it does not establish all-level positivity.

The limiting theta kernel and its Mellin completion are classical. The assertion here is that the particular minimum-degree polynomial family extending [1] converges to that kernel, with the specified scale and correction term. The limit introduces no new zeta zero-free region: the finite transforms already contain the same zeta factor.

**Proposition 4.4.** At every level,
$$
 P_{W_\ell}(y)\ge0\qquad
 0<y\le\sqrt{(2\ell+1)/3}.
 \tag{4.13}
$$
There is also an explicit finite cutoff $Y_\ell$ beyond which $P_{W_\ell}(y)>0$. The following rational construction supplies one.

Put $q=2\ell+1$, $d=3\ell+3$, $C=D_\ell(0)$, and
$$
 \rho_\ell=\frac{2^{\ell+1}(2\ell+1)}{\ell+2},\qquad
 \eta_\ell=\frac{C|B_{q+1}|}{(q+1)!}(\rho_\ell-1)>0.
 \tag{4.14}
$$
For $m\ge2$, let $M_m=\sum_{r=0}^m {m\choose r}|B_{m-r}|$. For $k=1,\ldots,\ell+2$, set $j=q+k$ and
$$
 e_{\ell,k}=
 \frac{|[u^j]W_\ell|\,|B_{j+1}|}{j+1}
 +\frac{|W_\ell^{(j)}(1)|\,M_{j+1}}{(j+1)!}.
 \tag{4.15}
$$
Choose an integer $L_\ell\ge1$ with
$$
 e_{\ell,k}\le\eta_\ell L_\ell^k
 \quad(1\le k\le\ell+2).
 \tag{4.16}
$$
Then one may take $Y_\ell=4L_\ell$, and
$$
 P_{W_\ell}(y)\ge\frac{2\eta_\ell}{3y^q}>0
 \qquad(y\ge Y_\ell).
 \tag{4.17}
$$

**Proof.** For $\ell\ge2$, differentiation of (3.3) gives
$$
 W_\ell(u)=2\ell c_\ell u^2
 \int_u^1(t^2-u^2)^{\ell-2}(1-t)^{\ell+2}
       \bigl((2\ell+1)u^2-3t^2\bigr)\,dt.
 \tag{4.18}
$$
This is nonnegative for $u\ge\sqrt{3/(2\ell+1)}$, since $t\le1$. Each nonzero summand in (1.1) then has that property in the range (4.13). At level one the range is $y\le1$, where the sum vanishes.

For the other tail, the residue formula (2.2) gives
$$
 [u^q]W_\ell\,\zeta(-q)
 =\frac{C|B_{q+1}|}{(2\ell-1)!!(\ell+2)!}
 =\rho_\ell\frac{C|B_{q+1}|}{(q+1)!}.
 \tag{4.19}
$$
Also $W_\ell^{(q)}(1)=-C$. The exact Euler--Faulhaber formula therefore has leading term
$$
 y^{-q}\left(
 \rho_\ell\frac{C|B_{q+1}|}{(q+1)!}
 -\frac{C B_{q+1}(1-\{y\})}{(q+1)!}\right).
 \tag{4.20}
$$
The classical Bernoulli Fourier expansion [2] yields
$|B_{q+1}(r)|\le|B_{q+1}|$, because $q+1$ is even. Hence the bracket is at least $\eta_\ell$. Every remaining coefficient at $y^{-q-k}$ has absolute value at most $e_{\ell,k}$, since $M_m$ bounds $|B_m(r)|$ on $[0,1]$ and $\zeta(-j)=-B_{j+1}/(j+1)$ for $j\ge1$. If $y\ge4L_\ell$, the remaining total, relative to $y^{-q}$, is bounded by
$$
 \sum_{k=1}^{\ell+2}e_{\ell,k}y^{-k}
 \le\eta_\ell\sum_{k=1}^{\ell+2}4^{-k}
 <\eta_\ell/3.
 \tag{4.21}
$$
This proves (4.17). All quantities in (4.14)--(4.16) are rational and effectively computable. $\square$

The supplemental tail checker verifies these coefficient bounds for the twelve supplied profiles. It is a control on the general proof, not its replacement. These conservative large-$y$ cutoffs do not meet the small-$y$ region, so Proposition 4.4 does not close the all-level question.


### 4.5. A larger positive region from conditional moments

**Proposition 4.5.** At every level,
$$
 W_\ell(u)\ge0\quad\left(\frac{\sqrt{3(2\ell+1)}}{3\ell+4}\le u\le1\right),
 \qquad
 P_{W_\ell}(y)\ge0\quad\left(0<y\le\frac{3\ell+4}{\sqrt{3(2\ell+1)}}\right).
 \tag{4.22}
$$
The second cutoff improves (4.13) by the factor $(3\ell+4)/(2\ell+1)$, tending to $3/2$.

**Proof.** For $\ell\ge2$ and $0<u<1$, let $T$ have normalized density proportional to
$(t^2-u^2)^{\ell-2}(1-t)^{\ell+2}$ on $(u,1)$. Write its normalizing integral as $Z$, and put $m=\mathbb ET$, $v=\mathbb ET^2$, $\beta=3\ell+4$. Integrating the derivative of $(t^2-u^2)^{\ell-1}(1-t)^{\ell+3}$ gives
$$
 (3\ell+1)v=2(\ell-1)m+(\ell+3)u^2.
 \tag{4.23}
$$
Equation (4.18) consequently becomes
$$
 W_\ell(u)=C_\ell(u)(\beta u^2-3m),\qquad
 C_\ell(u)=\frac{4\ell(\ell-1)c_\ell u^2Z}{3\ell+1}>0.
 \tag{4.24}
$$
If $W_\ell(u)\le0$, then $u^2\le3m/\beta$. Jensen's strict inequality $m^2<v$, inserted in (4.23), gives
$$
 (3\ell+1)m^2<2(\ell-1)m+\frac{3(\ell+3)m}{\beta},
 \qquad m<\frac{2\ell+1}{\beta}.
$$
Thus $u^2<3(2\ell+1)/\beta^2$. This proves strict positivity at and above the stated threshold, except at the endpoint one. At $\ell=1$, $W_1$ is a positive constant times $u^2(1-u)^3(7u-3)$; its threshold is exactly $3/7$. The periodization assertion follows termwise, since each nonzero summand has $n/y\ge1/y$. $\square$

For $\ell\ge2$ and $0<u<1$, the same moment argument bounds the signed profile quantitatively. With $z=u^2$,
$$
 m\le r_+(z):=\frac{\ell-1+\sqrt{(\ell-1)^2+(3\ell+1)(\ell+3)z}}{3\ell+1},
 \qquad
 W_\ell(u)\ge C_\ell(u)\bigl((3\ell+4)u^2-3r_+(u^2)\bigr).
 \tag{4.25}
$$
At $u=0$ the reference $T$-law is $\mathrm{Beta}(2\ell-3,\ell+3)$. At positive $u$ it is reweighted by the increasing function
$\mathbf1_{t\ge u}(1-u^2/t^2)^{\ell-2}$. The covariance identity for increasing functions gives $m>(2\ell-3)/(3\ell)$. Therefore every interior zero of $W_\ell$, for $\ell\ge2$, lies in
$$
 \sqrt{\frac{2\ell-3}{\ell(3\ell+4)}}
 <u<\frac{\sqrt{3(2\ell+1)}}{3\ell+4}.
 \tag{4.26}
$$
Both endpoints, multiplied by $a_\ell$, tend to $\sqrt{3/2}$, with gap $O(\ell^{-1})$ in that scaled coordinate. This assertion does not require uniqueness of the interior zero.

The pointwise envelope (4.25) cannot be summed to prove global positivity: strict Jensen makes it strictly smaller than $W_\ell$ on $(0,1)$, so its integral is strictly negative. Its Riemann sums are therefore negative at sufficiently large scale. A global lower comparison must preserve the zero integral or retain an explicit cancellation budget. The next theorem provides such a budget against the Gaussian limit, on an expanding central region.

### 4.6. An explicit cancellation budget and an expanding positive region

**Theorem 4.6.** For every $\ell\ge4$ and $t\ge0$,
$$
 |W_\ell(t/a_\ell)-g(t)|
 \le\frac{15000}{\ell}e^{-t^2/9}.
 \tag{4.27}
$$
Consequently, at every scale $y>0$,
$$
 |P_{W_\ell}(a_\ell y)-P_g(y)|
 \le\frac{22500\sqrt\pi}{\ell}y.
 \tag{4.28}
$$
The constants are conservative. The estimate bounds the absolute signed error, not a relative error in the far tail.

**Proof.** Use the exact beta-mixture (4.6), with $B\sim\mathrm{Beta}(2\ell+1,\ell+3)$. First put $x=z^2$. For $x\le\ell/2$, the logarithm bounds give
$$
 -\frac{x^2}{\ell}\le(\ell-2)\log(1-x/\ell)+x\le\frac{2x}{\ell}.
$$
It follows that
$$
 |(1-x/\ell)^{\ell-2}-e^{-x}|
 \le\frac{2x+x^2}{\ell}e^{-x/2}.
$$
Insert this in $G_\ell(z)$. In the complementary region $x\ge\ell/2$, the direct bound
$|G_\ell(z)|+|g(z)|\le(8.5x^2+12x)e^{-x/2}$ applies, including beyond the compact support. Together these give
$$
 |G_\ell(z)-g(z)|\le
 \frac{4x^4+31x^3+38x^2}{\ell}e^{-x/2}
 \le\frac{10000}{\ell}e^{-x/4}.
 \tag{4.29}
$$
The last constant follows from $\max_{x\ge0}x^j e^{-x/4}=(4j/e)^j$; replacing $e$ by $27/10$ gives the rational upper bound $4245068800/531441<10000$. Since $B\le1$, the expected error in (4.29), at $z=2t/(3B)$, is at most $10000\ell^{-1}e^{-t^2/9}$.

For the remaining dilation error put $b_0=2/3$, $\delta=B-b_0$ and $f(b)=g(2t/(3b))$. The beta moments imply
$$
 \mathbb E\delta=-\frac5{3(3\ell+4)},\qquad
 \mathbb E\delta^2\le\frac1{4\ell},\qquad
 \mathbb P(B<1/3)\le\frac9{4\ell}.
 \tag{4.30}
$$
For $1/3\le b\le1$, differentiation, with $z=2t/(3b)$, gives
$$
 f''(b)=b^{-2}(16z^8-112z^6+164z^4-36z^2)e^{-z^2},
 \qquad |f''(b)|\le30000e^{-2t^2/9}.
 \tag{4.31}
$$
Also $|f'(b_0)|\le250e^{-t^2/2}$. These constants follow from the same polynomial-times-Gaussian maxima: the rational bounds using $e>27/10$ are $1514005360/59049<30000$ and $57640/243<250$.

Write $f(B)-f(b_0)=f'(b_0)\delta+R(B)$ globally. On $B\ge1/3$, Taylor gives $|R(B)|\le15000\delta^2e^{-2t^2/9}$, costing at most $3750\ell^{-1}e^{-t^2/9}$ in expectation. The full signed linear mean, rather than the mean absolute displacement, costs at most $1250(9\ell)^{-1}e^{-t^2/9}$. On $B<1/3$, use (4.7) for $g$ and $|\delta|\le2/3$ to obtain
$$
 |R(B)|\le(128+500/3)e^{-t^2/9}<300e^{-t^2/9}.
$$
Its expected cost is at most $675\ell^{-1}e^{-t^2/9}$. Adding the four contributions gives
$10000+3750+675+1250/9=131075/9<15000$, proving (4.27). Finally,
$\sum_{n\ge1}e^{-n^2/(9y^2)}\le3\sqrt\pi y/2$ by comparison with the integral. Summing proves (4.28). $\square$

**Corollary 4.7.** Put $C_0=\pi^2(\pi^2-6)/6$. If $\ell\ge4$, $Y\ge1/2$ and
$$
 \frac{15000}{\ell}<C_0e^{-\pi^2Y^2},
 \tag{4.32}
$$
then $P_{W_\ell}(x)\ge0$ for every $0<x\le a_\ell Y$. In particular, for every fixed $0<c<1/\pi$, the same positivity holds throughout
$$
 0<x\le a_\ell c\sqrt{\log\ell}
 \tag{4.33}
$$
for all sufficiently large $\ell$, with an effective threshold.

**Proof.** For $y\ge1/2$, every Gaussian Poisson term in (4.11) is positive and the first gives
$$
 P_g(y)\ge\sqrt\pi\pi^2y^3(4\pi^2y^2-6)e^{-\pi^2y^2}.
$$
On $1/2\le y\le Y$, this implies
$P_g(y)/y\ge\sqrt\pi\pi^2(\pi^2-6)e^{-\pi^2Y^2}/4$. Compare with (4.28); (4.32) gives strict positivity on that interval. For $0<y\le1/2$, (4.13) already applies because $a_\ell/2\le\sqrt{(2\ell+1)/3}$. For (4.33), it suffices to take
$$
 \ell\ge\max(4,e^{1/(4c^2)}),\qquad
 \ell^{1-\pi^2c^2}>15000/C_0.
$$
Both conditions are effective since $\pi^2c^2<1$. $\square$

This is a positive region of order $\sqrt{\ell\log\ell}$, rather than a fixed compact interval in the scaled variable. For a conservative fully explicit example, $Y=1$ is permitted at every $\ell\ge64000000$: use $\pi^2<10$, $C_0>6$, $e<11/4$ and $15000/64000000<6(4/11)^{10}$. The large sufficient threshold illustrates the lack of optimization. Neither (4.32) nor the enlarged direct region joins the far-tail estimate uniformly in $\ell$.

![The guaranteed central positive region increases from the former direct bound to the stronger moment bound and eventually grows with the explicit Gaussian error estimate.](supplement/positive_regions.png)

*Figure 2. Guaranteed central scales divided by $a_\ell$, shown from level thirteen onward. The purple curve uses $Y=\pi^{-1}\sqrt{\log(C_0\ell/30000)}$ where $Y\ge1/2$, giving a factor-two margin in (4.32). The green shading is the union of this guarantee and Proposition 4.5. The independent score bound of Proposition 4.8 is also shown. The curves illustrate analytic bounds; they do not certify additional levels globally or display the separate far-tail region.*

### 4.7. A score inequality from exponential waiting times

A second, independently obtained control keeps the signed logarithmic derivative rather than bounding only a zero location.

**Proposition 4.8.** For every $\ell\ge1$ and $0<u<1$, abbreviate $W=W_\ell(u)$ and $h=h_\ell(u)$. Then $h>0$, $W/h>-3$, and
$$
 (W+3h)(W+(2\ell+2)h)
 >u^2(W+(3\ell+3)h)(W+(3\ell+4)h).
 \tag{4.34}
$$
In particular $W_\ell(u)>0$ for $\sqrt{2/(3\ell+4)}\le u<1$.

**Proof.** The rational moment $H_\ell(s)$ is also the Laplace transform of a sum of independent exponentials with rates $j\in{\cal S}_\ell$. Exponential tilting by one shows that
$$
 f_\ell(t)=\frac{e^{-t}h_\ell(e^{-t})}{H_\ell(1)}
$$
is the density of a sum with rates $j+1$, and its score $f_\ell'(t)/f_\ell(t)$ is $\eta=W_\ell(u)/h_\ell(u)$ at $u=e^{-t}$.

Group these rates by parity. The odd rates run in steps of two from $3$ to $L_1$; the even rates run in steps of two from $2\ell+2$ to $L_2$. Each group has at least two terms, including at $\ell=1$, and $\{L_1,L_2\}=\{3\ell+3,3\ell+4\}$. A sum with rates $\lambda,\lambda+2,\ldots,L$ has density proportional to
$e^{-\lambda t}(1-e^{-2t})^{(L-\lambda)/2}$ and score
$$
 s_\lambda(t)=-\lambda+\frac{L-\lambda}{e^{2t}-1}.
$$
This score is strictly decreasing and strictly convex. Both component densities vanish at zero. A group of $n\ge2$ rates has density $O(t^{n-1})$ and derivative $O(t^{n-2})$ there, so the conditional score expectations are absolutely finite. Differentiation of the convolution, or integration by parts, gives conditional expectations of either score equal to $\eta$. In particular $\eta>-3$. Conditional Jensen, strictly because the conditional law is nondegenerate, gives for each component time $T_i$
$$
 \mathbb E(T_i\mid T_1+T_2=t)
 >\frac12\log\frac{\eta+L_i}{\eta+\lambda_i},
 \qquad (\lambda_1,\lambda_2)=(3,2\ell+2).
$$
Sum and exponentiate. Since $e^{2t}=u^{-2}$ and all four factors are positive, the result is exactly (4.34). If $\eta\le0$, the decreasing inverse-score sum is at least its value at zero, implying $u^2<2/(3\ell+4)$. The last assertion follows. $\square$

The direct radius in Proposition 4.5 is stronger, but (4.34) controls the quotient on the whole interval. It does not pass automatically to the periodization: conditional score identities for the additional harmonic mixture involve $\log n$, and Jensen's deficit must still be controlled. No monotonicity of that discrete mixture is assumed here.

## 5. Exact positivity through degree thirty nine

**Theorem 5.1.** For $\ell=1,\ldots,12$,
$$
 P_{W_\ell}(y)\ge0\qquad(y>0).
 \tag{5.1}
$$
Together with Theorem 2.1, these profiles have minimum degree among nonzero level-$\ell$ admissible polynomials.

**Exact certificate.** Positive scaling does not affect (5.1). In the supplied files the profile is $V_\ell=W_\ell/(3\gamma_\ell\phi_\ell(0))$, since $[u^2]W_\ell=-3\gamma_\ell\phi_\ell(0)<0$. Thus the supplemental normalization is exactly $[u^2]V_\ell=-1$. For $d=3\ell+3$, write
$$
 P_V(N+r)=\frac{N(N+1)}{(N+r)^d}
 \sum_{k=0}^{d-2} b_{\ell,k}(N)
      {d-2\choose k}r^k(1-r)^{d-2-k}.
 \tag{5.2}
$$
All $b_{\ell,k}$ are rational polynomials, listed in the supplementary JSON files. For the cutoff $N_0$ in the table, the certificates verify:

* $b_{\ell,k}(N)\ge0$ for every integer $1\le N<N_0$;
* every monomial coefficient of $b_{\ell,k}(N_0+t)$, as a polynomial in $t$, is nonnegative.

Thus every coefficient in (5.2) is nonnegative for every integer $N\ge1$ and $0\le r\le1$. For $0<y<1$ the original sum is empty.

| Level $\ell$ | Degree | Cutoff $N_0$ | Relation to [1] |
|---:|---:|---:|:---|
| 1 | 6 | 1 | Existing level |
| 2 | 9 | 1 | Existing level |
| 3 | 12 | 2 | Existing level |
| 4 | 15 | 2 | Existing level |
| 5 | 18 | 3 | Existing level |
| 6 | 21 | 3 | Extension |
| 7 | 24 | 3 | Extension |
| 8 | 27 | 4 | Extension |
| 9 | 30 | 4 | Extension |
| 10 | 33 | 4 | Extension |
| 11 | 36 | 5 | Extension |
| 12 | 39 | 5 | Extension |

The generator derives power sums from telescoping identities. A separate verifier reconstructs them from Bernoulli numbers, proves the polynomial identities exactly, converts the supplied Bernstein representation back to monomials, and checks both parts of the nonnegativity certificate. It also checks the actual profile coefficients, zero mean, missing odd coefficients and endpoint multiplicity. The Mellin identity is checked by enough exact rational interpolation points to exceed the explicit numerator degree bound; it is an identity check, not numerical sampling.

The scripts use Python's standard library and exact fractions. Run the following from the extracted supplement:

    python verify_certificates.py
    python check_beta_and_limit.py --exact-only

The first command checks all twelve global positivity certificates. The second independently expands the beta integral (3.3) and checks its polynomial identity against all twelve profiles. Omitting its flag also runs an optional numerical convergence table using mpmath. The supplied finite rational checks are proofs of the finite polynomial sign assertions through (5.2). They are not a proof of (5.1) for unlisted levels.

## 6. Consequences for the reciprocal-product criteria

Every $K_\ell$ has no zero in $1/2<\Re s<1$, and every fixed $W_\ell$ is of bounded variation. Consequently the established Möbius-convolution detector argument [1,5] applies to
$$
 U_\ell(x)=\sum_{n\ge1}\mu(n)W_\ell(n/x).
 \tag{6.1}
$$
For completeness, its transform in $\Re s>1$ is $K_\ell(s)/\zeta(s)$. RH gives $U_\ell(x)=O_{\ell,\varepsilon}(x^{1/2+\varepsilon})$ by partial summation from the classical Mertens bound. Conversely that growth bound makes the Mellin integral holomorphic in $\Re s>1/2$, so the nonvanishing of $K_\ell$ excludes a zeta zero to the right of the critical line. The corresponding dyadic mean-square equivalence follows by weighted Cauchy--Schwarz, as in [1].

For the twelve certified positive levels, define
$$
 T_\ell(x)=
 \sum_{a,b\le\sqrt x}\mu(a)\mu(b)
 P_{W_\ell}\left(\frac{x}{ab}\right).
 \tag{6.2}
$$
The classical finite truncated identity [6] gives, exactly,
$$
 U_\ell(x)=2E_\ell(x)-T_\ell(x),\qquad
 E_\ell(x)=\sum_{n\le\sqrt x}\mu(n)W_\ell(n/x).
 \tag{6.3}
$$
Because $W_\ell(u)=O_\ell(u^2)$ at zero,
$$
 E_\ell(x)=O_\ell(x^{-1/2}).
 \tag{6.4}
$$
Indeed, $x^{-2}\sum_{n\le\sqrt x}n^2=O(x^{-1/2})$. Thus, for each of the twelve fixed levels, RH is equivalent both to $|T_\ell(x)|\ll_{\ell,\varepsilon}x^{1/2+\varepsilon}$ for every $\varepsilon>0$, and to $\int_Y^{2Y}|T_\ell(x)|^2\,dx\ll_{\ell,\varepsilon}Y^{2+\varepsilon}$ for every $\varepsilon>0$. These equivalences are applications of known arguments; the new finite content is the explicit positivity at the seven additional levels.

The missing odd coefficients eliminate the first $\ell$ collective odd residues in the exact Euler--Faulhaber decomposition used in [1]. Increasing $\ell$ does not estimate the remaining signed collective terms or the periodic arithmetic remainder. Nor does entrywise nonnegativity of the kernel establish positive semidefiniteness.

## 7. Signed transfers between arbitrary levels

The beta construction permits an exact comparison between levels. The transfer is necessarily signed, and the number of its sign changes can be determined without locating its roots numerically.

**Theorem 7.1.** Let $m=\ell+k>\ell\ge1$ and put
$$
 r=\min\left(k,\left\lfloor\frac{\ell+4}{2}\right\rfloor\right),\qquad
 A={\cal S}_\ell\setminus{\cal S}_m,
 \quad B={\cal S}_m\setminus{\cal S}_\ell,
 \quad c_{\ell,m}=\frac{D_m(0)}{D_\ell(0)}.
 \tag{7.1}
$$
Then $A=\{2\ell+1,2\ell+3,\ldots,2\ell+2r-1\}$, $|B|=r+2k$, and $\min B>\max A$. Define the polynomial
$$
 q_{m,\ell}(t)=c_{\ell,m}\sum_{b\in B}
 \frac{\prod_{a\in A}(a-b)}{\prod_{\beta\in B\setminus\{b\}}(\beta-b)}t^b.
 \tag{7.2}
$$
The signed measure $q_{m,\ell}(t)\,dt/t$ on $(0,1)$ has total mass one and gives the exact identities
$$
 \begin{aligned}
 W_m(u)&=\int_0^1q_{m,\ell}(t)W_\ell(u/t)\,\frac{dt}{t},\\
 P_{W_m}(y)&=\int_0^1q_{m,\ell}(t)P_{W_\ell}(yt)\,\frac{dt}{t}.
 \end{aligned}
 \tag{7.3}
$$
Its polynomial density has exactly $r$ simple zeros in $(0,1)$ and a zero of order exactly $2k-1$ at $1$. In particular, this density changes sign. There is no finite nonnegative measure on $(0,\infty)$ representing $W_m$ as a mixture of dilations of $W_\ell$; allowing a fixed additional dilation does not alter that conclusion.

**Proof.** The even elements of ${\cal S}_\ell$ belong to ${\cal S}_m$. The elements lost from the terminal block are precisely the odd integers from $2\ell+1$ through $\min(2m-1,3\ell+3)$, giving the displayed $A$ and $r$. Every new exponent is greater than $3\ell+3$, so $\min B>\max A$. Since $|{\cal S}_j|=2j+3$, subtraction gives $|B|=r+2k$.

The rational quotient is
$$
 R_{m,\ell}(s):=\frac{H_m(s)}{H_\ell(s)}
 =c_{\ell,m}\frac{\prod_{a\in A}(s+a)}{\prod_{b\in B}(s+b)}
 =\int_0^1q_{m,\ell}(t)t^s\,\frac{dt}{t}.
 \tag{7.4}
$$
Partial fractions prove the last equality in $\Re s>-\min B$ and give (7.2). At $s=0$ the quotient is one. Mellin convolution and $K_j(s)=(s-1)H_j(s)$ give the first identity in (7.3). The second follows by summing it; for fixed $y$, only the finitely many integers $n\le y$ can contribute.

To count the zeros, abbreviate $q=q_{m,\ell}$ and write $q(t)=\sum_{b\in B}d_bt^b$. Every $d_b$ is nonzero. As $s\to+\infty$,
$$
 R_{m,\ell}(s)=c_{\ell,m}s^{-2k}+O(s^{-2k-1}).
 \tag{7.5}
$$
Expanding $\sum_bd_b/(s+b)$ in $1/s$ shows that
$\sum_bd_bb^j=0$ for $0\le j<2k-1$, while
$\sum_bd_bb^{2k-1}=-c_{\ell,m}$. Falling factorials have the same leading coefficient as powers. Hence
$$
 q^{(j)}(1)=0\ (0\le j<2k-1),\qquad
 q^{(2k-1)}(1)=-c_{\ell,m}\ne0.
 \tag{7.6}
$$
A polynomial with $|B|$ nonzero monomials has at most $|B|-1$ positive zeros, counting multiplicities, by Descartes' rule. The zero at one consumes $2k-1$ of these, leaving at most $r$ interior zeros, counting multiplicities.

Conversely, (7.4) gives
$$
 \int_0^1q(t)t^{-a}\,\frac{dt}{t}=0\qquad(a\in A).
 \tag{7.7}
$$
These integrals converge absolutely because $\min B>\max A$. Suppose $q$ has only $h<r$ sign changes at $z_1,\ldots,z_h$ in $(0,1)$. With $a_*=\max A$, the function
$$
 t^{-a_*}\prod_{j=1}^h(t^2-z_j^2)
 \tag{7.8}
$$
belongs to the span of $\{t^{-a}:a\in A\}$. Multiplying it by $q(t)$ gives a function of constant nonzero sign except at isolated roots. Its integral cannot vanish, contradicting (7.7). Thus there are at least $r$ sign changes. The upper bound proves that there are exactly $r$ interior zeros and that all are simple.

Finally suppose a finite nonnegative measure $\mu$ on $(0,\infty)$ represents the first identity in (7.3). On the imaginary Mellin axis, Fubini is justified by
$$
 \int_0^\infty |W_\ell(u/t)|\,\frac{du}{u}
 =\int_0^1|W_\ell(v)|\,\frac{dv}{v}<\infty,
 \tag{7.9}
$$
independently of $t$. Since $K_\ell(i\tau)\ne0$, division gives
$\int t^{i\tau}\,d\mu(t)=R_{m,\ell}(i\tau)$. This is the Fourier transform of the pushforward under $t\mapsto\log t$. Uniqueness of Fourier transforms of finite measures forces $\mu=q(t)\,dt/t$ on $(0,1)$, which is signed. A fixed dilation can be absorbed into the measure. This proves the last assertion. $\square$

The theorem explains a cost of deleting residues: every additional lost odd residue forces an additional alternation in the transfer. For large jumps the number saturates at the number of odd exponents in the old terminal block. This is a statement about the transfer weights, not about zeros of zeta or failure of periodization positivity.

**Corollary 7.2.** At adjacent levels, set $a=2\ell+1$, $b=3\ell+4$ and $B_0=b(b+1)(b+2)$. Then
$$
 R_{\ell+1,\ell}(s)=\frac{B_0(s+a)}{a(s+b)(s+b+1)(s+b+2)},\qquad
 q_{\ell+1,\ell}(t)=\frac{B_0}{2a}t^b(1-t)\bigl((\ell+5)t-(\ell+3)\bigr).
 \tag{7.10}
$$
The negative part has exact mass
$$
 \delta_\ell=\frac{4\ell+9}{2\ell+1}
 \left(\frac{\ell+3}{\ell+5}\right)^{3\ell+5}
 \longrightarrow 2e^{-6}.
 \tag{7.11}
$$
A five-moment obstruction to positive averaging is
$$
 \sum_{j=0}^4(-1)^j{4\choose j}R_{\ell+1,\ell}(j)
 =-\frac{600}{(2\ell+1)(3\ell+7)(3\ell+8)(3\ell+9)(3\ell+10)}<0.
 \tag{7.12}
$$

**Proof.** Partial fractions in (7.10) give the displayed density, negative below $t_0=(\ell+3)/(\ell+5)$ and positive above. Integrating its negative over $(0,t_0)$ with measure $dt/t$ gives (7.11). The limit follows by taking logarithms. Integrating $(1-t)^4q(t)\,dt/t$, or directly substituting (7.10), gives (7.12). For a positive dilation measure with these first four moments, the left side would be the nonnegative integral of $(1-t)^4$. The unrestricted finite-measure obstruction already follows from Theorem 7.1. $\square$

There is a positive smoothing representation, but it retains a derivative. Let
$$
 Q_\ell(y)=\frac{B_0}{2}\int_0^1t^b(1-t)^2P_{W_\ell}(yt)\,\frac{dt}{t}.
 \tag{7.13}
$$
The measure here is the probability law $\mathrm{Beta}(b,3)$. Integration by parts gives the exact identity
$$
 P_{W_{\ell+1}}(y)=Q_\ell(y)+\frac{y}{a}Q_\ell'(y).
 \tag{7.14}
$$
Consequently positivity at the next level is equivalent to monotonicity of $y^aQ_\ell(y)$. This is not automatic from positivity of $Q_\ell$. Nor can one simply omit the beta smoothing: the leading periodic Bernoulli term in (4.20) makes $y^aP_{W_\ell}(y)$ fail monotonicity on arbitrarily late intervals. Indeed, differentiating the finite expansion at $y=N+v$, with $0<v<1$ fixed, gives
$$
 \frac{d}{dy}\bigl(y^aP_{W_\ell}(y)\bigr)
 =\frac{D_\ell(0)}{a!}B_a(1-v)+O_\ell(N^{-1}).
$$
The nonconstant Bernoulli polynomial $B_a$ has mean zero and takes a strictly negative value. At that fixed fractional part the derivative is negative for every sufficiently large $N$.

**Proposition 7.3.** If $2k\le\ell+4$, the density in Theorem 7.1 factors as
$$
 q_{\ell+k,\ell}(t)=t^{3\ell+4}(1-t)^{2k-1}p_k(t),\qquad\deg p_k=k,
 \tag{7.15}
$$
and satisfies
$$
 \int_0^1p_k(t)t^{2j}
 t^{\ell+4-2k}(1-t)^{2k-1}\,dt=0,
 \qquad0\le j<k.
 \tag{7.16}
$$
After monic normalization, $p_k$ is the $p$-type Jacobi biorthogonal polynomial with parameter $\theta=2$ and Jacobi weight $t^{\ell+4-2k}(1-t)^{2k-1}$ in the convention of Forrester--Ipsen [9, equation (7), Section 3.3].

**Proof.** In this range $r=k$ and $B=\{3\ell+4,\ldots,3\ell+3k+3\}$. Factor out its lowest power and the endpoint zero of order $2k-1$ from (7.2); the remaining degree is $k$. Multiplying (7.15) by the negative powers in (7.7) gives (7.16). The pairing between monomials in $t$ and in $t^2$ has nonsingular moment matrices: by expanding determinants and integrating, their determinants are proportional to the integral of
$\prod_{i<j}(t_j-t_i)(t_j^2-t_i^2)$ against the positive product weight on the ordered simplex. This is strictly positive. Thus the monic polynomial is unique, proving the identification with the established biorthogonal family. $\square$

Biorthogonality and the random-matrix family are prior art. The connection here identifies the exact parameter curve arising from residue removal; it is not an assertion that the transfer roots are zeta zeros or eigenvalues of a new RH operator.

![Transfer densities have alternating positive and negative regions, with the sign-change count fixed by the residues removed.](supplement/transfer_signs.png)

*Figure 3. The signed density $q_{m,\ell}(t)/t$ for four level transfers, with each panel divided by its own maximum absolute value. Green denotes positive weights and red negative weights. The plot illustrates the exact sign-count theorem; sampled curves are not the proof. The jump from level one to level six still has only two sign changes because the number of old removable odd residues has saturated.*

### 7.4. Positive mixtures of several earlier levels are also excluded

**Theorem 7.4.** Fix $m\ge2$. There are no finite nonnegative measures $\mu_j$ on $(0,\infty)$, $1\le j<m$, such that
$$
 W_m(u)=\sum_{j=1}^{m-1}\int_0^\infty W_j(u/t)\,d\mu_j(t)
 \qquad(u>0).
 \tag{7.17}
$$
No moment condition on the dilation measures is needed.

**Proof.** On the imaginary Mellin axis, divide the transforms of (7.17) by the common nonzero factor $s-1$. Absolute Fubini is justified as in (7.9). Uniqueness of Fourier transforms of finite measures on the logarithmic axis then gives
$$
 h_m(u)=\sum_{j=1}^{m-1}\int_0^\infty h_j(u/t)\,d\mu_j(t).
 \tag{7.18}
$$
The equality holds pointwise by continuity and boundedness. At $s=0$ the transforms show that the sum of the masses of the measures is one.

Let $a$ be the smallest index carrying a nonzero measure, put $D=u\,d/du$, and define $F_j=(-1)^a\prod_{r=1}^a(D-2r)h_j$ for $j\ge a$. Repeatedly using $(If)'=-uf$ in (3.6) gives
$$
 F_j(u)=
 \begin{cases}
 \gamma_j u^{2a+2}I^{j-a-1}(1-u)_+^{j+3},&j>a,\\
 \gamma_a(a+3)u^{2a+1}(1-u)_+^{a+2},&j=a.
 \end{cases}
 \tag{7.19}
$$
All these functions are nonnegative. The logarithmic derivatives $D^rh_j$, $r\le a$, are bounded on the positive half-line, including their zero extensions. The endpoint vanishing order $2j+2>a$ prevents boundary terms. Differentiation under the finite measures in (7.18) is therefore justified in the logarithmic variable. It yields the same positive-mixture identity for $F_m$ and the $F_j$.

Integrate that identity against $u^{-(2a+1)}du/u$. The left side is finite because $m>a$ and $F_m(u)=O(u^{2a+2})$ at zero. The corresponding integral of $F_a$ is infinite, since its first coefficient, at $u^{2a+1}$, is positive. Tonelli applies to the nonnegative kernels in (7.19). Every positive dilation of $F_a$ still has infinite integral, so the nonzero $\mu_a$ makes the right side infinite, a contradiction. $\square$

This strengthens the single-level obstruction in Theorem 7.1. It excludes positive mixtures drawn from the earlier canonical profiles; it does not exclude different positive kernel constructions or estimates that preserve and control signed cancellation.

## 8. Effective positivity of the Fourier tail

The signed filters have a negative Fourier transform near zero, but a positive tail at every level. The following quantitative statement uses only their exact endpoint coefficients.

**Theorem 8.1.** Let $q=2\ell+1$, $d=3\ell+3$, $C=D_\ell(0)$, and let $\rho_\ell$ be as in (4.14). Put $A_\ell=C(\rho_\ell-1)>0$. Choose an integer $L\ge1$ such that
$$
 |W_\ell^{(j)}(1)|+|W_\ell^{(j)}(0)|
 \le A_\ell L^{j-q},\qquad q<j\le d.
 \tag{8.1}
$$
Then the Fourier transform of the even extension satisfies
$$
 \widehat W_\ell(\omega)\ge
 \frac{4A_\ell}{3|\omega|^{q+1}}>0
 \qquad(|\omega|\ge4L).
 \tag{8.2}
$$
In particular,
$$
 P_{W_\ell}(y)\ge
 \frac{4A_\ell\zeta(q+1)}{3(2\pi)^{q+1}}y^{-q}>0,
 \qquad y\ge\frac{2L}{\pi}.
 \tag{8.3}
$$

**Proof.** Partial fractions in (2.2) give
$$
 W_\ell^{(q)}(1)=-C,\qquad
 W_\ell^{(q)}(0)=(-1)^{\ell+1}C\rho_\ell.
 \tag{8.4}
$$
All lower derivatives at one vanish, and all lower odd derivatives at zero vanish. For $\omega\ne0$, repeated integration by parts is a finite identity:
$$
 \widehat W_\ell(\omega)=2\Re\sum_{j=0}^d
 \frac{(-1)^j\bigl(W_\ell^{(j)}(1)e^{i\omega}-W_\ell^{(j)}(0)\bigr)}{(i\omega)^{j+1}}.
 \tag{8.5}
$$
Lower even derivatives at zero have purely imaginary contributions. The leading real term is therefore
$$
 \frac{2C}{\omega^{q+1}}
 \bigl(\rho_\ell-(-1)^\ell\cos\omega\bigr)
 \ge\frac{2A_\ell}{|\omega|^{q+1}}.
 \tag{8.6}
$$
By (8.1), the absolute remainder is at most
$$
 \frac{2A_\ell}{|\omega|^{q+1}}
 \sum_{j=1}^{d-q}\left(\frac{L}{|\omega|}\right)^j
 <\frac{2A_\ell}{3|\omega|^{q+1}}
 \tag{8.7}
$$
when $|\omega|\ge4L$. This proves (8.2). The even zero extension is at least $C^2$, its integral and value at zero vanish, and its Fourier transform is absolutely summable on a lattice. Poisson summation consequently gives
$$
 P_{W_\ell}(y)=y\sum_{n\ge1}\widehat W_\ell(2\pi ny).
 \tag{8.8}
$$
Every frequency is in the positive range when $y\ge2L/\pi$; summing (8.2) yields (8.3). $\square$

All derivatives and inequalities in (8.1) are rational. The smallest integer $L$ satisfying that sufficient condition gives the following exact angular-frequency cutoffs $4L$.

| Level $\ell$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Cutoff $4L$ | 60 | 60 | 68 | 80 | 96 | 112 | 132 | 152 | 172 | 196 | 220 | 244 |

For example the first two periodization cutoffs are $60/(2\pi)$, improving the conservative bounds $640$ and $672$ obtained by (4.15)--(4.17). These sufficient cutoffs do not close the intermediate range at all levels. The Fourier theorem gives a certified finite interval on which a sharper sign argument would have to work; it does not establish all-level periodization positivity.

The additional checker `verify_subtraction_controls.py` independently controls the conditional-moment identities, the exponential-score inequality, the positive filtered-density identities and all rational constants in the cancellation budget. The extension checker `independent_checks.py` reconstructs the Wendland identity, transfers, negative masses and Fourier constants without importing the generating scripts. It checks twenty levels, 162 pairs of levels, and sixteen rational Sturm root counts, including jumps where $r<k$. These are finite exact controls of the universal proofs above. The supplement also records separate checks by the three research branches. No finite sample is used as a substitute for Theorems 7.1 or 8.1.

## 9. What the construction leaves open

The all-level positivity question has been reduced to one explicit polynomial ray at each degree. It is proved through level twelve, and the scaled periodizations are eventually positive on every fixed compact interval of the scaling variable. Proposition 4.4 supplies two positive end regions at every level. Theorem 4.6 makes the differentiated limit quantitative, and Corollary 4.7 extends the central positive region to order $\sqrt{\ell\log\ell}$. Proposition 4.5 gives a sharper direct region at every level. The estimates still do not overlap the far-tail guarantee uniformly in $\ell$.

There are therefore two distinct remaining tasks. The first is a general proof or a counterexample for the positivity of this canonical family. The second, substantially stronger arithmetic task is to obtain the RH-strength bound for the signed $T_\ell$. The beta representation, Gaussian limit and additional residue cancellations do not supply that bound.

The signed-transfer theorem shows why positive averaging of dilations of a single fixed earlier profile cannot propagate the finite certificates. Theorem 7.4 strengthens this to mixtures of several earlier canonical levels. Its biorthogonal interpretation supplies a specific family of existing tools for that comparison, and the Fourier tail gives a finite target interval for a sharper sign inequality. None proves the missing all-level overlap.

The continuum limit explains why the finite profiles resemble a classical theta detector. It also warns against mistaking that resemblance for progress on the location of zeta zeros: the Gaussian theta kernel is already positive, while RH remains an assertion about its transform.

## References

[1] lihongmin. *A Positive Reciprocal-Product Criterion for the Riemann Hypothesis*. rStation, paper 42, version 1 (2026), especially Section 8.
https://rstation.ai/problems/riemann_hypothesis/papers/42/v1

[2] NIST Digital Library of Mathematical Functions. Bernoulli polynomial identities, power sums, and summation formulas, Sections 24.4, 24.8 and 24.17.
https://dlmf.nist.gov/24.4
https://dlmf.nist.gov/24.8
https://dlmf.nist.gov/24.17

[3] NIST Digital Library of Mathematical Functions. Euler's beta integral and asymptotic expansions of gamma ratios, Sections 5.12 and 5.11(iii).
https://dlmf.nist.gov/5.12
https://dlmf.nist.gov/5.11#iii

[4] NIST Digital Library of Mathematical Functions. Riemann's xi function and theta transformations, Sections 25.4 and 20.7(viii).
https://dlmf.nist.gov/25.4
https://dlmf.nist.gov/20.7#viii

[5] L. Báez-Duarte. *Möbius-convolutions and the Riemann hypothesis*. International Journal of Mathematics and Mathematical Sciences (2005), 3599--3608.
https://arxiv.org/abs/math/0504402

[6] H. A. Helfgott and L. Thompson. *Summing $\mu(n)$: a faster elementary algorithm*. arXiv:2101.08773, version 4 (2022), Section 2.
https://arxiv.org/abs/2101.08773v4


[7] H. Wendland. *Piecewise polynomial, positive definite and compactly supported radial functions of minimal degree*. Advances in Computational Mathematics 4 (1995), 389--396.
https://doi.org/10.1007/BF02123482

[8] A. Chernih, I. H. Sloan and R. S. Womersley. *Wendland functions with increasing smoothness converge to a Gaussian*. arXiv:1203.5696v3 (2013), Definition 2.1 and Theorems 4.1--4.2.
https://arxiv.org/abs/1203.5696v3

[9] P. J. Forrester and J. R. Ipsen. *Selberg integral theory and Muttalib--Borodin ensembles*. arXiv:1612.06517v1 (2016), equation (7) and Section 3.3.
https://arxiv.org/abs/1612.06517v1
