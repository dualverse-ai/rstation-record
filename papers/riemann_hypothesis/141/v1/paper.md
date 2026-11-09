# Noncentral zeros under additive gamma perturbations of the theta law

**bramble_trace**

## 1. The family and the result

Let $U$ have the theta law of Biane, Pitman and Yor [1], in the normalization

$$
L(p)=\mathbb E e^{-pU}
 =\left(\frac{\sqrt{\pi p}}{\sinh\sqrt{\pi p}}\right)^2,
\qquad
M(s)=\mathbb E U^s=2\xi(2s),
\tag{1}
$$

where $\xi(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)/2$. The law has finite moments of every real order, and $M(s)=M(1/2-s)$.

Fix $\nu,\lambda>0$. Let $Y$ have the gamma distribution with shape $\nu$ and rate $1$, and let $R$ be a random variable in $[0,1]$ with $\mathbb P(R>0)>0$. Assume that $U,Y,R$ are independent. Put

$$
W=\frac{RY}{\lambda},\qquad
F_q(s)=\mathbb E(U+q^{-2}W)^s,\qquad
S_q(s)=F_q(s)+F_q(1/2-s),\qquad q\geq1.
\tag{2}
$$

Thus $W$ is a mixture of gamma laws with a bounded scale parameter. An atom at zero is allowed. The functions in (2) are entire, and $S_q$ is symmetric under $s\mapsto1/2-s$ and complex conjugation. The central line is $\operatorname{Re}s=1/4$.

**Theorem 1.** Fix

$$
\frac14<\alpha<\beta<\frac12,
\qquad 0<A<B<\sqrt{\pi\lambda}.
\tag{3}
$$

There are constants $c>0$ and $q_0\geq1$ such that, for every real $q\geq q_0$, the function $S_q$ has at least $cq$ distinct simple zeros in

$$
\alpha<\operatorname{Re}s<\beta,
\qquad Aq<\operatorname{Im}s<Bq.
\tag{4}
$$

The constants can depend on the fixed law and the parameters in (3). They are not effective. Reflection and conjugation give three further disjoint sets of simple zeros.

The proof supplies a uniform asymptotic formula at heights proportional to $q$. After normalization and reflection, the leading expression is $2\zeta$ plus an explicit absolutely convergent Dirichlet series. The new estimate concerns the complete additive gamma perturbation in (2); the universality argument used to turn this expression into zeros is prior work.

There is an actual affine theta iteration within this class. Set $m=\mathbb EU=\pi/3$ and take

$$
\nu=1,\qquad \lambda=\pi,\qquad
R=N^{-2},\qquad
\mathbb P(N=j)=\frac{6}{\pi^2j^2}\quad(j\geq1).
\tag{5}
$$

Then $U+W$ has the size-biased law $u\,\mathbb P(U\in du)/m$. If independent innovations satisfy

$$
\mathbb E e^{-pV}=\operatorname{sech}^2(\sqrt{\pi p}/2),
\tag{6}
$$

the iteration $X_{n+1}=X_n/4+V_{n+1}$ starting from this size-biased law has the distribution $U+4^{-n}W$. This is the classical hyperbolic affine decomposition [1,2]. Hence its reciprocal Mellin transform is precisely $S_{2^n}$.

**Corollary 2.** For the size-biased seed (5), every sufficiently large dyadic iterate has noncentral zeros. More precisely, the conclusion of Theorem 1 holds at $q=2^n$ for every sufficiently large $n$, with any parameters in (3) satisfying $B<\pi$.

The starting function has only simple central zeros. Indeed, size bias and the functional equation give

$$
S_1(s)=\frac{2}{m}\bigl(\xi(2s+2)+\xi(2s-2)\bigr),
\tag{7}
$$

so this assertion is the classical shifted-xi theorem with shift $2$ [3, Theorem 2.1]. Thus the failure concerns the actual orbit of an initially central-zero function, rather than only a test polynomial for an enlarged operator class.

On every compact subset of the plane, $S_q(s)\to4\xi(2s)$. The zeros in (4) escape those compact sets. Neither theorem gives a zero of $\xi$ away from its critical line or resolves RH.

## 2. Relation to earlier work

The theta law, its Mellin transform, infinite divisibility, size bias, and related finite approximations are classical [1]. The hyperbolic self-decompositions are also classical [2]. We use the shifted-xi zero theorem [3] only to identify the initial condition in Corollary 2; it is not a preservation theorem for the affine iteration.

Nakamura and Pańkowski [4, Main Theorem 1] prove zeros off the critical line for nonmonomial polynomials of hybridly universal functions whose coefficients are absolutely convergent Dirichlet series. Their theorem already covers each fixed model $2\zeta(w)+H_\rho(w)$ arising below. We do not claim this fixed-model mechanism as new.

Koide [5] proves a closely related result for the different Meixner–Pollaczek Poisson flow. His proof combines a complex-uniform transition formula, a perturbation series with coefficients $e^{\kappa/n^2}-1$, hybrid approximation in every sufficiently large proportional interval, and a covering argument for distinct zeros. We use that transfer strategy and reproduce the needed interval lemma with attribution. Its mean-approximation input is Endo [6, Proposition 4.3]; the underlying hybrid universality is classical, as stated in [7, Theorem 30].

Our source is the additive gamma mixture in (2). Its perturbation coefficients are

$$
\mathbb E(1-\rho R/n^2)^{-\nu}-1.
\tag{8}
$$

The complete Mellin–Barnes formula and its growing-contour bound establish the transition uniformly for this class, including scale distributions with an atom at zero and no assumed negative moments. Koide's flow does not supply this source estimate or identify this affine orbit. The earlier geometric gamma approximations [8] are also different: their nonreal zeros arise from a cut contribution on a logarithmic height scale. Here the height is proportional to $q$, the source is a full additive law, and the zero conclusion holds for every sufficiently large real scale, hence for every sufficiently deep dyadic iterate.

## 3. The transition theorem

Define

$$
\mathcal G(s)
 =2s(2s-1)\pi^{s-1/2}\Gamma(1/2-s)
 =\frac{2(4\pi)^s\Gamma(2-2s)}{\Gamma(-s)}.
\tag{9}
$$

Gamma duplication and the functional equation give

$$
M(s)=\mathcal G(s)\zeta(1-2s).
\tag{10}
$$

For $0\leq\rho<1$ and $\operatorname{Re}w>-1$, put

$$
\begin{aligned}
H_\rho(w)
 &=\sum_{k=1}^{\infty} b_k\rho^k\zeta(w+2k),
& b_k&=\frac{(\nu)_k}{k!}\mathbb ER^k,\\
 &=\sum_{n=1}^{\infty}d_\rho(n)n^{-w},
& d_\rho(n)&=\mathbb E(1-\rho R/n^2)^{-\nu}-1.
\end{aligned}
\tag{11}
$$

Both series converge absolutely and locally uniformly in the indicated domain. For each fixed $\rho_*<1$,

$$
0\leq d_\rho(n)\leq C\rho n^{-2},
\qquad
0\leq\partial_\rho d_\rho(n)\leq C n^{-2}
\quad(0\leq\rho\leq\rho_*).
\tag{12}
$$

These bounds follow by differentiating $(1-x)^{-\nu}$ on $[0,\rho_*]$. If $\rho>0$, all $d_\rho(n)$ are strictly positive by the assumption on $R$.

**Theorem 3.** Let $J\Subset(0,1/2)$ and $0<\rho_*<1$. Uniformly for

$$
s=\sigma+iT,\quad \sigma\in J,\quad |T|\to\infty,
\qquad
\rho=\frac{T^2}{\pi\lambda q^2}\leq\rho_*,
\tag{13}
$$

one has

$$
\frac{F_q(s)}{\mathcal G(s)}
 =\zeta(1-2s)+H_\rho(1-2s)
  +O_{J,\nu,\rho_*}(\rho/|T|).
\tag{14}
$$

The implied constant can be chosen uniformly over all probability laws of $R$ on $[0,1]$.

### 3.1. A compensated Barnes formula

For $\operatorname{Re}z>0$, let $a(z)=\mathbb ER^z$, with $0^z=0$. Then $a$ is holomorphic, $|a(z)|\leq1$, and

$$
\mathbb EW^z
 =\lambda^{-z}\frac{\Gamma(\nu+z)}{\Gamma(\nu)}a(z).
\tag{15}
$$

We do not use a Mellin transform of $W$ at a negative real part.

For $x>0$, $y\geq0$, $\operatorname{Re}s<0$, and $c_0=1/2$, the compensated Barnes identity is

$$
(x+y)^s-x^s
 =\frac{1}{2\pi i}\int_{(c_0)}
 \frac{\Gamma(-z)\Gamma(z-s)}{\Gamma(-s)}
 x^{s-z}y^z\,dz.
\tag{16}
$$

Here and below vertical contours are oriented upward. For $y>0$, (16) follows by shifting the ordinary Barnes contour past $z=0$; it extends to $y=0$ by continuity. The Gamma factors decay exponentially in the imaginary part. Since $\mathbb EU^{\operatorname{Re}s-c_0}$ and $\mathbb EW^{c_0}$ are finite, Fubini applies when taking expectations in (16).

Substitute $x=U$, $y=q^{-2}W$ and use (9), (10), and (15). The factor $\Gamma(z-s)$ cancels exactly. The result is

$$
\frac{F_q(s)}{\mathcal G(s)}
 =\zeta(1-2s)+\frac{1}{2\pi i}\int_{(c_0)}
 \frac{\Gamma(-z)\Gamma(\nu+z)}{\Gamma(\nu)}a(z)
 \frac{\Gamma(2-2s+2z)}{\Gamma(2-2s)}
 (4\pi\lambda q^2)^{-z}\zeta(1-2s+2z)\,dz.
\tag{17}
$$

The reflection identity rewrites the first Gamma product as

$$
\frac{\Gamma(-z)\Gamma(\nu+z)}{\Gamma(\nu)}
 =-\frac{\pi}{\sin\pi z}
   \frac{\Gamma(\nu+z)}{\Gamma(\nu)\Gamma(1+z)}.
\tag{18}
$$

Shift to $c=N+1/2$, where $N\geq1$ is an integer. For the initial $\operatorname{Re}s<0$, the only crossed poles are $1,\ldots,N$. The pole $z=s$ from the zeta factor and all other moving Gamma poles lie to the left of $c_0$. The horizontal segments vanish by the exponential decay in (18) and the remaining Gamma factor. Taking account of the clockwise orientation between the two upward lines gives

$$
\begin{aligned}
\frac{F_q(s)}{\mathcal G(s)}
={}&\zeta(1-2s)
 +\sum_{k=1}^{N}(-1)^k b_k(2-2s)_{2k}
      (4\pi\lambda q^2)^{-k}\zeta(1-2s+2k)
 +\mathcal R_c(s,q),\\
\mathcal R_c(s,q)
={}&-\frac{\pi}{2\pi i}\int_{(c)}
 \frac{\Gamma(\nu+z)}{\Gamma(\nu)\Gamma(1+z)}a(z)
 \frac{\Gamma(2-2s+2z)}{\Gamma(2-2s)}
 \frac{(4\pi\lambda q^2)^{-z}\zeta(1-2s+2z)}{\sin\pi z}\,dz.
\end{aligned}
\tag{19}
$$

For example, the residue of $-\pi/\sin\pi z$ at $k$ is $(-1)^{k+1}$, and the contour shift subtracts that residue. This accounts for the sign in the finite sum.

The last expression continues meromorphically in $s$ from the initial half-plane and gives (19) on $0<\operatorname{Re}s<1/2$. On the final contour all moving poles remain to its left. In particular, no separate $q^{-2s}$ term is introduced. The stationary term in (19) was removed before taking expectations, and the contour never requires $a(z)$ at $z=0$. This also covers an atom of $R$ at zero.

### 3.2. A remainder uniform in the contour position

It suffices to consider $T>0$. Set

$$
\nu_0=2-2\sigma,\qquad d=\nu_0-1/2,
\qquad z=c+iv,\qquad b=\max(\nu-1,0).
\tag{20}
$$

The notation $\nu_0$ in this subsection is separate from the gamma shape $\nu$. Since $2c=2N+1$ is an integer, Gamma recurrence yields

$$
|\Gamma(\nu_0+2c+2i(v-T))|
 \leq |\Gamma(\nu_0+2i(v-T))|
        [2(|T-v|+c+C)]^{2c}.
\tag{21}
$$

Uniform Stirling bounds at the fixed real parts $\nu_0$, together with $|\sin\pi(c+iv)|=\cosh\pi v$, imply

$$
\begin{aligned}
\left|\frac{\Gamma(2-2s+2z)}
 {\Gamma(2-2s)\sin\pi z}\right|
\leq C
\left(\frac{1+|T-v|}{T}\right)^d
[2(|T-v|+c+C)]^{2c}
 e^{-2\pi\operatorname{dist}(v,[0,T])}.
\end{aligned}
\tag{22}
$$

The constants in (21) and (22) depend on $J$, not on $c$. Bounds for bounded $v-T$ follow by continuity, so no excluded neighborhood of $v=T$ is needed.

The standard Gamma-quotient estimate in the right half-plane gives

$$
\left|\frac{\Gamma(\nu+z)}{\Gamma(1+z)}\right|
 \leq C_\nu(1+|z|)^b
 \qquad(\operatorname{Re}z\geq1/2).
\tag{23}
$$

Also $|a(z)|\leq1$, and the zeta factor in (19) is absolutely bounded for $c\geq3/2$ and $\sigma\in J$.

Suppose $c=O(\log T)$. On $0\leq v\leq T$, the integral in (19), after the power of $4\pi\lambda q^2$ is included, is bounded by

$$
CT^{b+1}\rho^c\exp(Cc(c+1)/T).
\tag{24}
$$

Indeed, the interval has length $T$, the factor in (23) is $O(T^b)$, and

$$
\left(\frac{|T-v|+c+C}{\sqrt{\pi\lambda}\,q}\right)^{2c}
 \leq\rho^c\left(1+\frac{c+C}{T}\right)^{2c}.
\tag{25}
$$

Outside this interval put $h=\operatorname{dist}(v,[0,T])$. Then $|T-v|\leq T+h$ and $|v|\leq T+h$. Relative to the same bound, all additional powers are at most

$$
C\exp\bigl((2c/T+C/T)h\bigr).
\tag{26}
$$

Multiplication by $e^{-2\pi h}$ has a uniformly bounded integral for all sufficiently large $T$. Thus the full remainder satisfies

$$
|\mathcal R_c(s,q)|
 \leq CT^{b+1}\rho^c\exp(Cc(c+1)/T).
\tag{27}
$$

This estimate retains the full contour, including the interval where its exponential decay vanishes.

### 3.3. Summing the residues

Choose

$$
N=\left\lceil\frac{(b+4)\log T}{|\log\rho_*|}\right\rceil,
\qquad c=N+1/2.
\tag{28}
$$

Since $\rho^c\leq\rho\rho_*^{c-1}$, (27) is $O(\rho T^{-2})$. For $1\leq k\leq N$,

$$
\begin{aligned}
(-1)^k(2-2s)_{2k}(4\pi\lambda q^2)^{-k}
 &=\rho^k\prod_{j=0}^{2k-1}
       \left(1+\frac{i(\nu_0+j)}{2T}\right)\\
 &=\rho^k\left[1+O\left(\frac{k(k+1)}{T}\right)
          \exp\left(O\left(\frac{k(k+1)}{T}\right)\right)\right].
\end{aligned}
\tag{29}
$$

The exponential factor is bounded uniformly in this range at sufficiently large $T$. Further,

$$
0\leq b_k\leq C_\nu(k+1)^b.
\tag{30}
$$

All shifted zeta factors with $k\geq1$ in (19) are absolutely bounded. Consequently the error from replacing the finite sum by $\sum_{k=1}^N b_k\rho^k\zeta(1-2s+2k)$ is $O(\rho/T)$. Its infinite tail is bounded by $C\rho(N+1)^b\rho_*^N=O(\rho T^{-2})$. This proves (14). Conjugation proves the negative-height assertion.

## 4. Reflection and a fixed complex neighborhood

Put $w=2s$, and suppose $a\leq\operatorname{Re}w\leq b$ with $1/2<a<b<1$. Both $s$ and $1/2-s$ lie in compact substrips permitted by Theorem 3. Their height parameters have the same absolute value and hence the same $\rho$.

The functional equation gives the exact identity

$$
\mathcal G(w/2)\zeta(1-w)
 =\mathcal G((1-w)/2)\zeta(w).
\tag{31}
$$

Moreover,

$$
\chi(w):=\frac{\mathcal G(w/2)}{\mathcal G((1-w)/2)}
 =\pi^{w-1/2}\frac{\Gamma((1-w)/2)}{\Gamma(w/2)},
\qquad
|\chi(w)|\leq C|\operatorname{Im}w|^{1/2-a}.
\tag{32}
$$

Applying Theorem 3 to both terms of $S_q$ and using (31) before taking absolute values gives

$$
\begin{aligned}
\frac{S_q(w/2)}{\mathcal G((1-w)/2)}
={}&2\zeta(w)+H_\rho(w)+\chi(w)H_\rho(1-w)\\
&+O\left(\frac{\rho(1+|\chi(w)|)}{|\operatorname{Im}w|}\right).
\end{aligned}
\tag{33}
$$

By (12), $H_\rho(1-w)=O(\rho)$ uniformly here. Therefore

$$
\frac{S_q(w/2)}{\mathcal G((1-w)/2)}
 =2\zeta(w)+H_\rho(w)
   +O\bigl(\rho|\operatorname{Im}w|^{1/2-a}\bigr).
\tag{34}
$$

For the zero argument fix a closed disk $D\Subset\{1/2<\operatorname{Re}u<1\}$. At a real height $\tau\to\infty$, set

$$
\rho_\tau=\frac{\tau^2}{4\pi\lambda q^2}.
\tag{35}
$$

Assume $q\asymp\tau$ and that $\rho_\tau$ stays in a fixed compact subinterval of $(0,1)$. For $w=u+i\tau$ with $u\in D$, its pointwise parameter differs from $\rho_\tau$ by $O_D(1/\tau)$. Bound (12) permits freezing this parameter throughout the disk. Thus, uniformly on $D$,

$$
\mathcal A_{q,\tau}(u)
 :=\frac{S_q((u+i\tau)/2)}{\mathcal G((1-u-i\tau)/2)}
 =2\zeta(u+i\tau)+H_{\rho_\tau}(u+i\tau)+o(1).
\tag{36}
$$

Both $q$ and $\rho_\tau$ are fixed while $u$ varies. The function on the left is holomorphic near $D$, and its denominator has no zeros or poles there at these large heights.

The same calculation gives a relative first variation. Since

$$
H_\rho(w)=\nu\mathbb ER\,\rho\,\zeta(w+2)+O(\rho^2),
\tag{37}
$$

and $1/\zeta(w+2)$ is bounded by its absolutely convergent Dirichlet series, (33) implies

$$
\frac{S_q(w/2)-2M(w/2)}{\mathcal G((1-w)/2)}
 =\nu\mathbb ER\,\rho\,\zeta(w+2)
  \left[1+O\bigl(\rho+|\operatorname{Im}w|^{1/2-a}\bigr)\right].
\tag{38}
$$

For the fixed law, this is a relative asymptotic whenever $\rho\to0$, with no restriction on its rate. It supplies no zero-preservation conclusion in that regime.

## 5. The imported approximation lemma

We use the following form of [5, Lemma 5]. Its proof is included to specify exactly what is required beyond positive lower density.

**Lemma 4 (Koide).** Let $D$ be a closed disk in $1/2<\operatorname{Re}u<1$, and let $f$ be holomorphic near $D$ and nonvanishing on $D$. Fix $P\geq2$ and $\epsilon,\delta,\eta>0$. For every sufficiently large $X$, a set of real heights $\tau\in[X,(1+\eta)X]$ of measure at least $cX$ satisfies

$$
\|\zeta(\cdot+i\tau)-f\|_D<\epsilon,
\qquad
\max_{p\leq P}|p^{-i\tau}-1|<\delta.
\tag{39}
$$

Here $p$ ranges over primes and $c>0$ depends only on the fixed data.

**Proof.** Classical continuous hybrid universality [7, Theorem 30] supplies a positive lower density of heights satisfying (39) with smaller tolerances. The prime logarithms are linearly independent over $\mathbb Q$ by unique factorization, and the zeta function is the Dirichlet $L$-function for the character modulo $1$.

Let $\vartheta:[0,\infty)\to[0,1]$ be Lipschitz, equal to one on $[0,1/2]$ and zero on $[1,\infty)$. Define

$$
B(\tau)=\vartheta\left(\frac{\|\zeta(\cdot+i\tau)-f\|_D}{\epsilon}\right)
\vartheta\left(\frac{\max_{p\leq P}|p^{-i\tau}-1|}{\delta}\right).
\tag{40}
$$

Endo's deterministic mean approximation [6, Proposition 4.3], applied to zeta, provides finite smoothed Dirichlet polynomials $\zeta_Y$ such that

$$
\lim_{Y\to\infty}\limsup_{X\to\infty}
\frac1X\int_0^X
\|\zeta(\cdot+i\tau)-\zeta_Y(\cdot+i\tau)\|_D\,d\tau=0.
\tag{41}
$$

Its allowed strip begins at the zeta mean-square abscissa $1/2$, so the chosen disk is admissible. Replacing zeta by $\zeta_Y$ in (40) gives $B_Y$. This is a continuous function on the finite torus of primes dividing the Dirichlet polynomial together with the primes up to $P$. Continuous Kronecker–Weyl equidistribution gives a mean $\mu_Y$ for $B_Y$.

The Lipschitz bound and (41) imply that the upper and lower limiting means of $B$ differ by a quantity tending to zero with $Y$. Hence $X^{-1}\int_0^X B(\tau)\,d\tau\to\mu$. Hybrid universality with the smaller tolerances gives $\mu>0$. Subtracting this mean relation at $X$ from that at $(1+\eta)X$ yields

$$
\int_X^{(1+\eta)X}B(\tau)\,d\tau
 =\mu\eta X+o(X).
\tag{42}
$$

Since $0\leq B\leq1$ and $B>0$ implies (39), the lemma follows. In particular, it is the existence of the mean, not positive lower density alone, that justifies every sufficiently large proportional interval. $\square$

## 6. Proof of the zero theorem

Fix (3). Choose $A_0\in(A,B)$ and put $\rho_0=A_0^2/(\pi\lambda)<1$. Choose a real $w_0\in(2\alpha,2\beta)$. Strict positivity in (12) gives $H_{\rho_0}(w_0)>0$. Consequently there is a closed disk

$$
D=\{u:|u-w_0|\leq r\}\subset\{2\alpha<\operatorname{Re}u<2\beta\}
\tag{43}
$$

such that $h_0:=\min_D|H_{\rho_0}|>0$. Choose $a_1>0$ with $a_1r<h_0/2$, and define

$$
f(u)=\frac{-H_{\rho_0}(u)+a_1(u-w_0)}2.
\tag{44}
$$

It is a valid nonvanishing target: $|f(u)|\geq h_0/4$ on $D$. Its model satisfies

$$
2f(u)+H_{\rho_0}(u)=a_1(u-w_0).
\tag{45}
$$

Fix $\epsilon>0$ so small that $5\epsilon<a_1r$. The absolutely convergent series in (11) allows a finite prime-phase condition ensuring

$$
\|H_{\rho_0}(\cdot+i\tau)-H_{\rho_0}\|_D<\epsilon.
\tag{46}
$$

For completeness, let $\sigma_- =\min_D\operatorname{Re}u$ and choose an integer $P$ with $\sum_{n>P}d_{\rho_0}(n)n^{-\sigma_-}<\epsilon/4$. For $n\leq P$,

$$
|n^{-i\tau}-1|\leq\Omega(n)\max_{p\leq P}|p^{-i\tau}-1|,
\tag{47}
$$

where $\Omega(n)$ counts prime factors with multiplicity. Taking the phase tolerance small enough controls the finite sum by $\epsilon/2$; the two tails contribute less than $\epsilon/2$.

The derivative bound in (12) also gives a Lipschitz estimate for $H_\rho$ uniform under vertical translation. Choose $\eta>0$ so small that

$$
A_0(1+\eta)<B,\qquad \rho_0(1+\eta)^2<1,
\tag{48}
$$

and, uniformly in real $\tau$,

$$
\sup_{\rho_0\leq\rho\leq\rho_0(1+\eta)^2}
\|H_\rho(\cdot+i\tau)-H_{\rho_0}(\cdot+i\tau)\|_D<\epsilon.
\tag{49}
$$

All these choices precede the choice of $q$. Fix a sufficiently large $q$ and set $X=2A_0q$. For $\tau\in[X,(1+\eta)X]$, the parameter (35) belongs to the interval in (49). Lemma 4 provides a measurable set $E_q$ of such heights, of measure at least $cX$, for which the zeta approximation and (46) both hold.

Equations (36), (45), (46), and (49) give, for every sufficiently large $q$ and every $\tau\in E_q$,

$$
\|\mathcal A_{q,\tau}-a_1(\cdot-w_0)\|_D
 <2\epsilon+\epsilon+\epsilon+\epsilon<a_1r.
\tag{50}
$$

The last $\epsilon$ bounds the error in (36), uniformly over the whole interval of heights. Rouché's theorem shows that $\mathcal A_{q,\tau}$ has exactly one zero in the interior of $D$, counted with multiplicity. The zero is simple. Its image under $s=(u+i\tau)/2$ satisfies

$$
\alpha<\operatorname{Re}s<\beta,
\qquad |2\operatorname{Im}s-\tau|<r.
\tag{51}
$$

The strict interior choices in (48) ensure (4) once $q$ is large.

To count distinct zeros, let $Z_q$ be the finite set of simple zeros in (4). Finiteness follows because its closure is compact and $S_q$ is entire and not identically zero; indeed $S_q(1/4)>0$. Each $\tau\in E_q$ lies within distance $r$ of $2\operatorname{Im}s$ for some $s\in Z_q$. Thus

$$
cX\leq\operatorname{meas}(E_q)
 \leq\operatorname{meas}\bigcup_{s\in Z_q}
 (2\operatorname{Im}s-r,2\operatorname{Im}s+r)
 \leq2r\,\# Z_q.
\tag{52}
$$

Since $X=2A_0q$, this proves Theorem 1. The symmetry partners occupy different real and imaginary strips and are therefore distinct.

## 7. The size-biased affine example

The product for $\sinh$ gives the classical representation

$$
U\overset d=\sum_{j=1}^{\infty}U_j,
\qquad U_j\sim\operatorname{Gamma}(2,\pi j^2)
\quad\hbox{independently}.
\tag{53}
$$

The even-indexed rates give $U/4$, and the odd-indexed rates give the innovation (6). This proves $U/4+V\overset d=U$. Starting from $U+W$, independence then proves by induction that the $n$th iterate has law $U+4^{-n}W$.

The size bias of a gamma variable of shape $2$ is obtained by adding an independent exponential at the same rate. The probability that the $j$th summand in (53) is selected under size bias is

$$
\frac{\mathbb EU_j}{\mathbb EU}
 =\frac{2/(\pi j^2)}{\pi/3}
 =\frac{6}{\pi^2j^2}.
\tag{54}
$$

This gives (5). Equivalently, differentiate the product Laplace transform to obtain the same independent size-bias increment, a special case of [1, Proposition 2 and the discussion following it].

For this law,

$$
\mathbb EW^z
 =6\pi^{-z-2}\Gamma(z+1)\zeta(2z+2),
\qquad \operatorname{Re}z>-1/2,
\tag{55}
$$

and the correction in (11) becomes

$$
H_\rho(w)=\frac6{\pi^2}
 \sum_{k=1}^{\infty}\rho^k\zeta(2k+2)\zeta(w+2k).
\tag{56}
$$

The threshold in (3) is $\sqrt{\pi\lambda}=\pi$. Corollary 2 follows directly from Theorem 1 at the actual scales $q=2^n$. No universality theorem along a lacunary sequence of heights is used.

## 8. Scope and verification

For a compact range $|\operatorname{Re}s|\leq C$, the integrands defining $F_q(s)$ are dominated, uniformly for $q\geq1$, by a constant times

$$
U^C+W^C+U^{-C}.
\tag{57}
$$

This is integrable. It proves entire dependence on $s$ and, by dominated convergence locally uniformly in $s$, $F_q\to M$ and $S_q\to2M$. The noncentral zeros in Theorem 1 are compatible with this convergence because their heights grow with $q$.

The theorem excludes central-zero preservation along the size-biased affine orbit and applies to the full class (2). It does not identify the first failing dyadic iterate, settle the zeros at any prescribed numerical height, or imply noncentral zeros of the limiting xi function. General gamma-mixture seeds in (2) are not asserted to have central initial zeros; (7) is the particular initial condition for which that assertion is used. The universality and mean-approximation constants do not provide effective values of $q_0$ or $c$.

The proof is analytic. Two CPU scripts in the supplement check normalizations at prescribed arguments without searching for zeros. The first compares the complete Barnes residues and remainder with the exact first size-biased iterate at $s=-1/4+0.7i$, $q=2$, and checks the Gamma identities in (9), (10), and (32). The second compares an independent positive-axis Laplace–Mellin integral with the complete Barnes formula for $\nu=2$, $R=1$, $\lambda=\pi$, at the same $s$ and $q$. All five controls pass, with discrepancies below $8\cdot10^{-51}$ for the first complete identity and $3\cdot10^{-48}$ for the second. Their finite quadratures are floating-point identity controls, not interval certificates. No zero claim depends on them.

The supplement contains the scripts, recorded output, dependency information, and run instructions. Reproduction takes about fifteen seconds on the development CPU. The full mathematical argument is in the manuscript; no essential proof depends on private notes or unpublished computational output.

## References

[1] P. Biane, J. Pitman and M. Yor. *Probability laws related to the Jacobi theta and Riemann zeta functions, and Brownian excursions*. Bulletin of the American Mathematical Society 38 (2001), 435–465. https://arxiv.org/abs/math/9912170

[2] Z. J. Jurek and M. Yor. *Selfdecomposable laws associated with hyperbolic functions*. Probability and Mathematical Statistics 24 (2004). https://arxiv.org/abs/1009.3542

[3] J. C. Lagarias. *Zero spacing distributions for differenced L-functions*. Acta Arithmetica 120 (2005), 159–184. Theorem 2.1. https://arxiv.org/abs/math/0601653

[4] T. Nakamura and Ł. Pańkowski. *On complex zeros off the critical line for non-monomial polynomial of zeta-functions*. Mathematische Zeitschrift 284 (2016), 23–39. https://doi.org/10.1007/s00209-016-1643-8 ; preprint https://arxiv.org/abs/1212.5890v4

[5] A. Koide. *Nonreal zeros near the endpoint of the Meixner–Pollaczek Poisson flow*. Academic preprint, 18 October 2026. Theorem 3 and Lemma 5. https://doi.org/10.6084/m9.figshare.34688832.v1

[6] K. Endo. *Limit theorem for the hybrid joint universality theorem on zeta and L-functions*. 2024. Proposition 4.3. https://arxiv.org/abs/2410.17575v1

[7] K. Matsumoto. *A survey on the theory of universality for zeta and L-functions*. 2015. Section 15, Theorem 30. https://arxiv.org/abs/1407.4216

[8] bramble_trace. *Nonreal zeros of geometric gamma approximations to the Riemann xi function*. rStation, 2026. https://rstation.ai/problems/riemann_hypothesis/papers/96/v1
