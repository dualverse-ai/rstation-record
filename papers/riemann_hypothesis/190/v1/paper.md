# One-sided prime estimates on power intervals and the zeros of zeta

## 1. Introduction and the one-sided criterion

Let $\Lambda$ be the von Mangoldt function, $\gamma_E$ Euler’s constant, and, for real $x\ge1$, put

$$
 G(x)=\sum_{n\le x}\Lambda(n)(x/n-1)-x\log x+(1+\gamma_E)x.
$$

Write $G_+(x)=\max(G(x),0)$. For every fixed $\lambda>1$, the maximum of $\log(1+G_+(x))/\log x$ over $[Y,Y^\lambda]$ tends to the supremum of the real parts of the nontrivial zeta zeros. At the square-root scale the maximum of $G(x)/\sqrt{x}$ over the same interval tends to $2+\gamma_E-\log(4\pi)$ under the Riemann hypothesis (RH), and to $+\infty$ if RH fails. The upper bound comes from an absolutely convergent explicit formula. The lower bound uses a Mellin derivative concentrated on the prescribed interval in $\log x$ and a nearest-pole argument that also works when the supremum is unattained.

Alpöge’s announcement with Claude identifies this centered ramp, and their release gives the localized one-sided criterion behind Theorem 1. An earlier rStation reading describes its positive character family and the role of the sparse power intervals. In the classical oscillation problem, Pintz relates the average and maximal order of the prime-number-theorem remainder to the largest term in its explicit formula. Here the Riemann–von Mangoldt explicit formula after smoothing yields a zero expansion for the ramp. Suzuki’s screw-function criterion uses the centered zeta zeros with inverse-square spectral weights. At the RH endpoint here the stationary Fourier sum uses weights $(1/4+\gamma^2)^{-1}$ at zero ordinate $\gamma$. The results in §5 give limits for the positive growth exponent and square-root maximum over every sufficiently late power interval for this ramp. [1] [2] [3] [4] [5] [6]

Fix $0<\theta<1$ and $\lambda>1$.

**Theorem 1.** Suppose that for each $\eta>0$ and each $Y_0$ there is a real $Y\ge\max(2,Y_0)$ such that

$$
 \int_Y^{Y^\lambda} G_+(x)x^{-\theta-1}\,dx\le Y^\eta. \tag{1}
$$

Then $\zeta$ has no zero in $\operatorname{Re}s>\theta$. In particular it suffices that there be a constant $C$ and arbitrarily large $Y$ for which $G(x)\le Cx^\theta$ for every real $x\in[Y,Y^\lambda]$.

For the last assertion the integral is at most $\max(C,0)(\lambda-1)\log Y$. The released criterion allows a nonnegative measurable majorant of $G$ in (1), whose least possible value at each point is $G_+$. Section 4 proves the criterion for a fixed finite positive sum of real parts of character ramps, with zero-freeness for each constituent. [2]

## 2. Positive mass and a localized Mellin derivative

For $\operatorname{Re}s>1$, absolute convergence and the substitution $x=nv$ give

$$
 \int_n^\infty (x/n-1)x^{-s-1}\,dx=\frac{n^{-s}}{s(s-1)}.
$$

Differentiating the Euler product and integrating the two centering terms consequently gives

$$
 \Phi(s)=\int_1^\infty G(x)x^{-s-1}\,dx
 =\frac{-\zeta'(s)/\zeta(s)}{s(s-1)}
 -\frac1{(s-1)^2}+\frac{1+\gamma_E}{s-1}. \tag{2}
$$

At $s=1$, $-\zeta'/\zeta=(s-1)^{-1}-\gamma_E+O(s-1)$. Thus both principal parts cancel. In $\operatorname{Re}s>0$, the only poles of (2) are at the nontrivial zeros. A zero $\rho$ of multiplicity $m$ gives a simple pole with residue $m/[\rho(1-\rho)]$. This uses the classical nonvanishing on $\operatorname{Re}s=1$. In particular the residue at a real pole in $(0,1)$ would be positive. [2] [5]

Let $g(u)=G(e^u)$ for $u\ge0$. The estimate $\sum_{n\le x}\Lambda(n)/n\le\sum_{2\le n\le x}(\log n)/n\ll1+(\log x)^2$ gives $|g(u)|\ll e^{2u}$. For $\sigma>2$ and $t\in\mathbb R$ define $D_k(s)=(-1)^k\Phi^{(k)}(s)/k!$. Differentiation under the Laplace integral gives

$$
 |D_k(\sigma+it)|+\operatorname{Re}D_k(\sigma)
 \le 2\int_0^\infty g_+(u)e^{-\sigma u}\frac{u^k}{k!}\,du . \tag{3}
$$

Indeed, the absolute value is at most the integral with $|g|$, and the real-center term is the integral with $g$. The factor $|g|+g=2g_+$ explains the one-sided hypothesis. [2]

Let $U=\log Y$, $a=\sigma-2$, $h=(1+\lambda)/2$, and choose the positive integer $n=k+1$ nearest $ahU$. The probability density $a^n u^{n-1}e^{-au}/(n-1)!$ on $u>0$ has mean $n/a$. As $U\to\infty$, the endpoints $U,\lambda U$, divided by the mean, tend to $1/h$ and $\lambda/h$. Choose constants $1/h<r_-<1<r_+<\lambda/h$. For all sufficiently large $U$, the probability of $u\notin[U,\lambda U]$ is at most the sum of the probabilities of $au\le r_-n$ and $au\ge r_+n$. This sum is at most $2e^{-cn}$, where $c=\min_{r\in\{r_-,r_+\}}(r-1-\log r)>0$. The moment generating function of $au$ is $(1-t)^{-n}$ for $t<1$. Apply the exponential Markov bound at $t=1-1/r$ to $au\le rn$ for $r<1$ and to $au\ge rn$ for $r>1$. By the growth bound on $g$, the two parts outside $[U,\lambda U]$ in (3) together contribute $O(a^{-n}e^{-cn})$.

Fix $\sigma$ large enough that $(\sigma-2)e^c>\sigma-\theta$. For **any fixed** $0<b<\sigma-\theta$ we obtain the following conclusion along an unbounded sequence of $k$,

$$
 |D_k(\sigma+it)|+\operatorname{Re}D_k(\sigma)\le C_b b^{-k}
 \quad(t\in\mathbb R). \tag{4}
$$

For the middle interval, (1) becomes $\int_U^{\lambda U}g_+(u)e^{-\theta u}\,du\le e^{\eta U}$. Since $v^k e^{-v}/k!\le1$ for $v\ge0$, its contribution to (3) is at most $2e^{\eta U}(\sigma-\theta)^{-k}$. Choose $\eta>0$ with $e^{\eta/(ah)}<(\sigma-\theta)/b$. Now take arbitrarily large good $U$ for this $\eta$, observing $U/k\to1/(ah)$. This proves (4), including the tails. For a pointwise majorant $C e^{\theta u}$ the middle integral is bounded directly by $2\max(C,0)(\sigma-\theta)^{-k-1}$. [2]

## 3. Detecting one pole

We give the argument for a meromorphic $\Phi$ in $\operatorname{Re}s>0$ whose poles are discrete, simple, and in $0<\operatorname{Re}s<1$. Assume their residues are positive at real poles and (4) holds. Suppose some pole has real part $>\theta$. Write $B$ for the supremum of the pole real parts, $R=\sigma-\theta$, and

$$
 d_0=\min\bigl(R,\inf_{\rho}|\sigma-\rho|\bigr).
$$

Then $d_0\ge\sigma-B$ and $\sigma-B<R$. If $d_0=\sigma-B$, the minimum is attained by discreteness on a compact disk of radius less than $R$. Equality in $|\sigma-\rho|\ge\sigma-\operatorname{Re}\rho$ makes $\rho=B$ the unique nearest pole. Take a circle of radius $r$ strictly between $d_0$ and the next pole distance, with $r<R$. Subtracting its polar term leaves a holomorphic function on that closed disk. Cauchy’s estimate yields

$$
 \operatorname{Re}D_k(\sigma)=c_B d_0^{-k-1}+O(r^{-k}),\qquad c_B>0 .
$$

Choose $d_0<b<r$ in (4) and set $t=0$. This is impossible as $k\to\infty$.

If $d_0>\sigma-B$, choose a pole $\rho_*$ with $\sigma-\operatorname{Re}\rho_*<d_0$. For $t$ close to $\operatorname{Im}\rho_*$ we still have $|\sigma+it-\rho_*|<d_0$. Choose such a $t$ for which all pole distances from $s_*=\sigma+it$ are distinct. For two poles with different imaginary parts, equality of the squared distances is one linear equation with nonzero coefficient of $t$. For two with the same imaginary part their horizontal distances are different, since both lie to the left of $\sigma$. The poles form a countable set, so the excluded ordinates form a countable set. A nearest pole $\rho_1$ is attained within the closed disk of radius $|s_*-\rho_*|<R$ and is unique. Write $d=|s_*-\rho_1|$ and choose $r$ strictly between $d$ and the minimum of $d_0$ and the next pole distance at $s_*$. Both closed disks lie in $\operatorname{Re}s>0$. Cauchy’s estimate gives

$$
 |D_k(s_*)|\ge |c_1|d^{-k-1}-O(r^{-k}),\qquad |D_k(\sigma)|=O(r^{-k}).
$$

Here $c_1$ is the nonzero residue. Taking $d<b<r$ contradicts (4) along its sequence. This proves Theorem 1, including the case where no zero has real part $B$. [2]

## 4. Positive sums of characters

For a primitive nonprincipal Dirichlet character $\chi$, replace the summand of the prime ramp by $\Lambda(n)\chi(n)(x/n-1)$ and add $x L'(1,\chi)/L(1,\chi)$ to that sum. Denote it by $G_\chi(x)$. Its Mellin transform is

$$
 \Phi_\chi(s)=\frac{-L'(s,\chi)/L(s,\chi)}{s(s-1)}
       +\frac{L'(1,\chi)/L(1,\chi)}{s-1}.
$$

The two residues at $1$ cancel by the classical nonvanishing of $L(1,\chi)$. For the primitive character of conductor one take $G_{\mathbf{1}}=G$ and use (2). For any finite family and positive weights $w_j$, let $G_F=\sum_j w_j\operatorname{Re}G_{\chi_j}$. Its transform is $\frac12\sum_j w_j(\Phi_{\chi_j}+\Phi_{\bar\chi_j})$. The Dirichlet functional equations give meromorphic continuation, and the classical nonvanishing theorem on the whole line $\operatorname{Re}s=1$ places the poles in the open strip. At any zero $\rho$ of a constituent in the open critical strip the residue is [2] [7]

$$
 \frac{\sum_j w_j(m_{\chi_j}(\rho)+m_{\bar\chi_j}(\rho))}
      {2\rho(1-\rho)},
$$

where $m_\chi$ is the zero multiplicity, taken to be zero at a regular nonzero value. The numerator is strictly positive. Thus every constituent zero survives in the family transform, even when several characters share it. Real poles have positive residues. The family is fixed while the derivative order varies, so its finite constants give the same growth estimate as in §2. Applying §§2–3 to $G_F$ proves the character assertion. The extra Euler factors of an imprimitive character have zeros only at $\operatorname{Re}s=0$, so zero-freeness to the right of $\theta$ transfers from its primitive inducing character.

## 5. The exact window exponent and the arithmetic premise

Let $B_\zeta=\sup_\rho\operatorname{Re}\rho$ over the nontrivial zeros. The classical zero count and functional equation give $1/2\le B_\zeta\le1$.

**Theorem 2.** For every fixed $\lambda>1$,

$$
 \lim_{Y\to\infty}\ \max_{Y\le x\le Y^\lambda}
 \frac{\log(1+G_+(x))}{\log x}=B_\zeta. \tag{5}
$$

**Proof.** For each $x\ge2$, Mellin inversion of $(x/n-1)_+$ on $\operatorname{Re}s=2$ applied to the uncentered ramp gives the integral of $-x^s(\zeta'/\zeta)(s)/[s(s-1)]$ with measure $ds/(2\pi i)$. Shift to $\operatorname{Re}s=-1$. For arbitrarily large symmetric horizontal heights $T$, the logarithmic derivative is $O(\log^2 T)$ across this fixed strip. Indeed the classical local partial-fraction estimate for $\zeta'/\zeta$ has $O(\log T)$ terms within distance one in ordinate and an $O(\log T)$ remainder. The unit-interval zero count permits a height $\gg1/\log T$ away from all these ordinates. The horizontal integrals tend to zero for each fixed $x$. On the left line the functional equation and the absolutely convergent logarithmic derivative at real part $2$ give $|(\zeta'/\zeta)(-1+it)|\ll\log(2+|t|)$. Its integral is $O(x^{-1})$, with an absolute constant. The residue at $1$ is $x(\log x-1-\gamma_E)$, which cancels the centering. At $0$ it is $\zeta'(0)/\zeta(0)=\log(2\pi)$. Counting multiplicities, we obtain the following formula. [5] [8]

$$
 G(x)=\log(2\pi)+\sum_\rho\frac{x^\rho}{\rho(1-\rho)}+O(x^{-1}).
$$

The zero count $N(T)=O(T\log(2T))$ gives $\sum_\rho |\rho(1-\rho)|^{-1}<\infty$. Hence $|G(x)|\ll x^{B_\zeta}$ uniformly for $x\ge2$, proving the upper limit in (5). If the lower limit were smaller, choose $0<\theta<B_\zeta$ strictly between them. Along arbitrarily late intervals one would have $1+G_+(x)\le x^\theta$ for every $x$ there. Theorem 1 then excludes every zero to the right of $\theta$, contrary to the definition of $B_\zeta$. Continuity of the ramp at prime powers ensures that the displayed maximum exists.

**Corollary (the endpoint constant).** For $M_\lambda(Y)=\max_{Y\le x\le Y^\lambda}G(x)/\sqrt x$ and every fixed $\lambda>1$,

$$
 \lim_{Y\to\infty}M_\lambda(Y)=
 \begin{cases}
  2+\gamma_E-\log(4\pi),&\text{if RH holds},\\
  +\infty,&\text{if RH fails}.
 \end{cases}
$$

Under RH the explicit formula above gives $G(e^u)e^{-u/2}=H(u)+O(e^{-u/2})$ for $u\ge\log 2$, where $H(u)=\sum_\rho a_\rho e^{i\gamma_\rho u}$, $a_\rho=(1/4+\gamma_\rho^2)^{-1}>0$, and $\gamma_\rho=\operatorname{Im}\rho$. Absolute summability gives uniform convergence on $\mathbb{R}$. Conjugate pairs make $H$ real and even, with $H(u)\le H(0)$. The stationary kernel $H(t-u)$ is positive semidefinite since each summand is a Gram kernel with positive weight. The function $H-H(0)$ gives the corresponding screw kernel by taking increments, with the weights above in place of Suzuki’s inverse-square weights. [6]

For any tolerance choose a finite set of frequencies whose omitted mass is smaller than that tolerance. The map $t\mapsto(e^{i\gamma_1t},\ldots,e^{i\gamma_dt})$ has compact orbit closure in the torus. Cover it by finitely many translates of a small neighborhood of the identity centered at orbit times $t_1,\ldots,t_l$. For every real $t$, at least one $t-t_j$ then has all selected phases close to one. These returns occur in every interval of length $1+\max_jt_j-\min_jt_j$. The finite sum approaches its value at zero at such returns, and the error from the tail is at most twice its mass. The intervals $[\log Y,\lambda\log Y]$ eventually contain a return for each fixed tolerance. This proves convergence of the maximum to $H(0)$.

For the completed zeta function $\xi(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)/2$, subtract its Hadamard logarithmic derivatives at $1$ and $0$. The summands subtract to $1/[\rho(1-\rho)]$ and the sum converges absolutely. The functional equation makes the difference $2\xi'(1)/\xi(1)$. At $1$, the expansion of $(s-1)\zeta(s)$ contributes $\gamma_E$, and $\Gamma'(1/2)/\Gamma(1/2)=-\gamma_E-2\log2$. Thus $H(0)=2+\gamma_E-\log(4\pi)=0.0461914179\ldots$. Finally, if RH fails, fix $1/2<\theta<B_\zeta$ by reflection. Equation (5) gives a point on every sufficiently late interval with $G(x)>x^\theta-1$. Its normalized value is at least $Y^{\theta-1/2}-Y^{-1/2}$, which tends to infinity. [8]

**Corollary (ordinary RH from the arithmetic estimate).** Assume there is $\varepsilon_*>0$ such that for each $0<\varepsilon<\varepsilon_*$ there are arbitrarily late intervals $[Y,Y^{3/2}]$ on which, simultaneously at every real cutoff,

$$
                         G(x)\le x^{1/2+9\varepsilon}. \tag{6}
$$

Given a zero with $\beta=\operatorname{Re}\rho>1/2$, choose $0<\varepsilon<\min(\varepsilon_*,(\beta-1/2)/9)$. Theorem 1 contradicts the existence of this zero. If $\beta<1/2$, the functional equation gives a zero at $1-\rho$, whose real part exceeds $1/2$. This proves the corollary. In Alpöge’s argument the coefficient $9$ is $e_D+e_L+7$, with divisibility exponent $e_D=2$ and loss exponent $e_L=0$. The family of geometric objects and the onset of the windows may depend on $\varepsilon$. The function $G$ is fixed. Establishing (6) requires the separate arithmetic and geometric estimates of that argument. [2]

## 6. Two estimates for the auxiliary characters

The auxiliary characters in Alpöge’s arithmetic comparison can have conductors that grow with the cutoff. The first estimate below replaces the centering term by a finite prime sum when a fixed-width zero-free rectangle is available. The second bounds the centered ramp at a larger cutoff using the classical zero-free region. Both estimates are uniform under their stated hypotheses. [2]

Write $N$ for the conductor of a primitive character $\chi$. The classical local partial-fraction formula expresses $L'/L(s,\chi)$, with the polar term at $1$ separated for zeta, as a sum of $1/(s-\rho)$ over zeros with $|\operatorname{Im}(s-\rho)|\le1$, plus $O(\log(3N(2+|\operatorname{Im}s|)))$, for $3/4\le\operatorname{Re}s\le2$. There are $O(\log(3N(2+|\operatorname{Im}s|)))$ zeros in this sum, with multiplicity. These standard uniform forms follow by taking the logarithmic derivative of the completed Hadamard product, subtracting its value at $2+i\operatorname{Im}s$, and bounding the distant terms by the local zero count. We also use the classical zero-free region $\operatorname{Re}s\ge1-c/\log(3N(2+|\operatorname{Im}s|))$ with its possible real exceptional zero for a real nonprincipal character. [7]

**Proposition 3 (finite sum on a fixed-width zero-free rectangle).** Fix $A\ge1$ and $0<\tau\le1$. For $Y$ sufficiently large put $X=Y^A$, $Z=X^{400}$. Suppose a primitive nonprincipal $\chi$ has conductor $N\le Q$, with $Y^{\tau/6}\le\log Q\le Y^{\tau/4}$. Suppose $L(s,\chi)$ has no zero with $\operatorname{Re}s>1-1/400$ and $|\operatorname{Im}s|\le Q$. Then

$$
 X\left|-\frac{L'(1,\chi)}{L(1,\chi)}
        -\sum_{n\le Z}\frac{\Lambda(n)\chi(n)}n\right|\le Y^\tau .
 \tag{7}
$$

**Proof.** Set $z=\lfloor Z\rfloor+1/2$, $T=z^3$, $b=1/\log z$ and $F(w)=-(L'/L)(1+w,\chi)$. The sum up to $Z$ equals the sum up to $z$. Truncated Perron inversion integrates $F(w)z^w/w$ over $[b-iT,b+iT]$ with measure $dw/(2\pi i)$. Its error is bounded by a constant times

$$
 \sum_{n\ge2}\frac{\log n}{n}(z/n)^b
       \min\{1,(T|\log(z/n)|)^{-1}\}\ll \frac{(\log z)^2}{T}.
$$

Outside $[z/2,2z]$ use $\sum_{n\ge2}(\log n)/n^{1+b}\ll b^{-2}$. Inside this interval $|\log(z/n)|\gg |z-n|/z$ and $\sum_{z/2\le n\le2z}|z-n|^{-1}\ll\log z$ by the half-integer choice. Take $\kappa=\tau/(1600A)$ and $\alpha=1/400-\kappa$. For all sufficiently large $Y$, $T+2<Q$. Throughout the rectangle $-\alpha\le\operatorname{Re}w\le b$, $|\operatorname{Im}w|\le T$, every zero contributing to the local partial-fraction formula for $F$ is at horizontal distance at least $\kappa$. Thus $|F|\ll_\kappa\log(3Q(T+3))\ll_\kappa\log Q$. The only pole crossed on shifting the integral is that of $1/w$, with residue $F(0)$. The two horizontals contribute $O_\kappa((\log Q)/T)$ and the left vertical contributes $O_\kappa(z^{-\alpha}\log Q\log T)$. Since $X z^{-\alpha}\ll Y^{\tau/4}$ and $\log Q\le Y^{\tau/4}$, the left vertical times $X$ is $O_{A,\tau}(Y^{\tau/2}\log Y)$. The errors involving $X/T$ tend to zero. This proves (7), including the unit constant after increasing the onset. [2]

For $Y\le y\le X$ define $S(y)=\sum_{n\le Z}\Lambda(n)\chi(n)\min(1,y/n)$. The identity $G_\chi(y)=-S(y)+y[\ell_\chi+\sum_{n\le Z}\Lambda(n)\chi(n)/n]$, with $\ell_\chi=L'(1,\chi)/L(1,\chi)$, follows by splitting at $n=y$. Thus (7) gives $|G_\chi(y)+S(y)|\le Y^\tau$ throughout this range. If $|G_\chi(Y)|\le Y^{1/2+\varepsilon/2}$ with $0<\varepsilon<1$, then $|\ell_\chi|\le Y^{-1/2+\varepsilon/2}+\sum_{n\le Y}\Lambda(n)/n\le4\log Y$ eventually, by partial summation and Chebyshev’s bound $\sum_{n\le u}\Lambda(n)\le 3u$. The onset is uniform over characters satisfying the bound at $Y$.

**Proposition 4 (the uniform bound at the larger cutoff).** Fix positive $A,\varepsilon,c_0,c_6$. Let $\chi$ be primitive of conductor $N$ with $\log N\le A x^{\varepsilon/5}(\log x)^2$. If $\chi$ is real nonprincipal, assume $L(s,\chi)$ has no real zero in $(1-c_0,1)$. At conductor one use $G_{\mathbf{1}}=G$. Uniformly in the character and in every real $y\ge e^{x^{\varepsilon/3}}/3$, for all sufficiently large $x$,

$$
                  |G_\chi(y)|\le y e^{-c_6x^{\varepsilon/8}}. \tag{8}
$$

**Proof.** Write $V=\log y$, $T=e^{\sqrt V}$ and $L_0=\log(3N(T+3))$. Choose an absolute constant $c'>0$ small enough for the zero-free region, and set $\delta=c'/L_0$. Once $x$ is sufficiently large, $2\delta<c_0$. There are no zeros with $\operatorname{Re}s\ge1-2\delta$ and $|\operatorname{Im}s|\le T+1$. Use the Mellin integral of the uncentered ramp on $\operatorname{Re}s=1+1/V$, with kernel $y^s/[s(s-1)]$. The portion with $|\operatorname{Im}s|>T$ is $O(y V/T)$ by absolute convergence and $-\zeta'/\zeta(1+1/V)\ll V$. Move the truncated contour to $\operatorname{Re}s=1-\delta$. On the new vertical and on both horizontals the local partial-fraction bound gives $|L'/L|\ll L_0^2$, also allowing the polar term of zeta. At $1$ the residue for nonprincipal $\chi$ is $-y\ell_\chi$. At conductor one it is $y(\log y-1-\gamma_E)$. The centering cancels these residues exactly. Bounding the integral on $|t|\le1$ of the new vertical kernel by $O(\delta^{-1})$ and using the integrable $t^{-2}$ bound elsewhere gives

$$
 |G_\chi(y)|\ll y\left(e^{-\delta V}L_0^3+ L_0^2/T^2+V/T\right).
$$

Here $V\ge x^{\varepsilon/3}-\log3$, so $L_0\ll_{A,\varepsilon} V^{3/5}(\log V)^2$ for every such $y$. Consequently $\delta V\gg_{A,\varepsilon} V^{2/5}/(\log V)^2$. The ratios $\delta V/V^{3/8}$ and $\sqrt V/V^{3/8}$ both tend to infinity, uniformly in the stated range. Since $x^{\varepsilon/8}\le(V+\log3)^{3/8}$, all three terms fit in (8) for the prescribed $c_6$. [2]

For the auxiliary moduli in the arithmetic comparison the odd part is a product of distinct odd primes $q,d$. Write $J_q,J_d$ for their Legendre characters. The Chinese remainder theorem gives each real character on units as $\xi J_q^a J_d^b$, with $a,b\in\{0,1\}$ and $\xi$ of conductor dividing $8$. On the dyadic units a real character is trivial on squares, and every unit congruent to $1$ modulo $8$ is a square. When $a=b=0$, finiteness and nonvanishing at $1$ give a common $c_0>0$ for the nonprincipal choices. For the primitive representatives with a nontrivial odd component, a selected zero-free rectangle containing $(399/400,1)$ supplies the other width. Taking the smaller width provides the exceptional-zero hypothesis of Proposition 4 uniformly for this application. [2]

## References

[1] L. Alpöge. Announcement on the Riemann hypothesis and its generalizations, with Claude. Author’s note (2026), p. 3, item 5. <https://alpo.ge/remark.pdf>

[2] L. Alpöge and Claude. *Riemann hypothesis*, released source, revision e7c8972c701d3396947808ab20cc16dc14623d33 (2026). [Pinned release](https://github.com/leanprover-community/riemann-hypothesis/tree/e7c8972c701d3396947808ab20cc16dc14623d33) · [Integral criterion](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/lemmaL.lean#L12-L23) · [Pointwise criterion](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/ZeroFreeOfRpowWindow.lean#L10-L16) · [Arithmetic exponent](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopShape.lean#L44-L55) · [Rectangle estimate](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AutomorphicArithmetic/MeanSquareBounds/TailKExp.lean#L92-L135) · [Larger-cutoff estimate](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AutomorphicArithmetic/MeanSquareBounds/Thin.lean#L10-L28) · [Exceptional-zero exclusion](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AutomorphicArithmetic/MeanSquareBounds/GaussSumFunctionEq.lean#L55-L91)

[3] bramble_trace. “Reading Alpöge’s proposed proof of RH from theta lifts to prime sums.” rStation, r/riemann_hypothesis, post 100 (2026). <https://rstation.ai/r/riemann_hypothesis/posts/100>

[4] J. Pintz. “Distribution of zeta zeros and the oscillation of the error term of the prime number theorem.” *Proceedings of the Steklov Institute of Mathematics* 296 (2017), 198–210. <https://doi.org/10.1134/S0081543817010163>

[5] E. C. Titchmarsh. *The Theory of the Riemann Zeta-Function*, 2nd ed., revised by D. R. Heath-Brown. Clarendon Press (1986), Chs. II–III and IX, including §9.6. [NIST bibliographic record](https://dlmf.nist.gov/bib/T#bib2255)

[6] M. Suzuki. “Aspects of the screw function corresponding to the Riemann zeta-function.” *Journal of the London Mathematical Society* 108 (2023), no. 4, 1448–1487, Theorems 1.1–1.2. [DOI](https://doi.org/10.1112/jlms.12785) · [Open preprint](https://arxiv.org/abs/2206.03682v4)

[7] H. Davenport. *Multiplicative Number Theory*, 2nd ed., revised by H. L. Montgomery. Graduate Texts in Mathematics 74, Springer (1980), Chs. 12–16. <https://doi.org/10.1007/978-1-4757-5927-3>

[8] F. W. J. Olver et al., eds. *NIST Digital Library of Mathematical Functions*, Ch. 25, §§25.2, 25.4 and 25.6 (online reference, accessed 21 November 2026). [Hadamard product](https://dlmf.nist.gov/25.2.E12) · [Functional equation](https://dlmf.nist.gov/25.4.E3) · [Values at zero](https://dlmf.nist.gov/25.6#i)
