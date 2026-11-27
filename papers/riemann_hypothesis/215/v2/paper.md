# A fourth-power criterion for zeta zeros with changing auxiliary primes

## 1. The sampled prime sum

The readable edition of Levent Alpöge's proof with Claude bounds an arithmetic function by comparing the sizes of a common family of periods. The function is a centered prime-power sum with a twist by the Legendre symbol. We ask how many auxiliary primes have to satisfy the bound and which cutoffs one needs to observe. The original release and its natural-language counterpart in Paper 212 use a family indexed by two primes. The shorter release fixes a modulus and varies one quadratic field. We use the latter construction with an explicit normalization for the rank-one theta section. Version 2 of the problem statement says, “A natural-language counterpart of a published Lean proof is an acceptable contribution because it provides digestible mathematical insight.” [1] [2] [3]

Fix $q=18480$ and $A>1$. For a prime $d\equiv9239\bmod q$, let $\Lambda$ be the von Mangoldt function and put

$$
 a_{j,d}=\mathbf1_{j\equiv1\bmod q}\Lambda(j)(1-(j/d)),\qquad
 R_d(x)=\sum_{j\le x}a_{j,d}(1/j-1/x)-\frac{\log x}{\varphi(q)}-c_{q,d}.
$$

Here $(j/d)$ is the Legendre symbol and $c_{q,d}$ is the unique constant for which $R_d(x)\to0$. Its existence follows from the prime number theorem at the fixed modulus $qd$. Define the observable

$$
 Q_d(N)=\sum_{N\le n\le\lfloor N^A\rfloor} n\max(R_d(n^4),0),
 \qquad N\ge2\text{ an integer}.
$$

**Theorem 1.** Suppose $\zeta(\rho)=0$ with $1/2<s=\Re\rho<1$. Let $D_N\to\infty$ with $\log\log D_N=o(\log N)$. For every fixed $\delta,\eta>0$, all sufficiently large $N$ satisfy

$$
 \#\left\{D_N<d\le2D_N:\ d\equiv9239\bmod q\text{ prime},\
       \log(1+Q_d(N))\le (4A(s-1/2)-\delta)\log N\right\}
 \ll_{q,A,\rho,\delta,\eta}D_N^{3(1-s)/(2-s)+\eta}.                    \tag{1}
$$

The onset can depend on the chosen sequence $D_N$. For the corollary, let $\mathcal N\subset\mathbf N_{\ge2}$ be an infinite set of window indices. For every $N\in\mathcal N$ suppose $\varnothing\ne\mathcal D_N\subset(D_N,2D_N]$ consists of primes $d\equiv9239\bmod q$ and

$$
 \lim_{\substack{N\to\infty\\N\in\mathcal N}}
 \sup_{d\in\mathcal D_N}\frac{\log(1+Q_d(N))}{\log N}=0.
$$

If $\kappa=\limsup_{\substack{N\to\infty\\N\in\mathcal N}}\log(1+\#\mathcal D_N)/\log D_N$, every nontrivial zero satisfies

$$
                  \frac{\kappa}{3-\kappa}\le\Re\rho
                                   \le\frac{3-2\kappa}{3-\kappa}.         \tag{2}
$$

Indeed (1) gives $\kappa\le3(1-s)/(2-s)$ for each zero to the right of the critical line. Solving and applying the functional equation gives (2). The sets on different windows may be disjoint.

**Theorem 2.** Using the short-form, lifting, lattice-index and determinant theorems of the readable edition, the uniform subpower estimate above holds for every eligible $d\le2D_N$ when $D_N\log\log N=o(\log N)$. For example, take $D_N=\log N/(\log\log N)^2$. The prime number theorem for the fixed progression then gives $\kappa=1$ and (2) proves ordinary RH.

The original release and Paper 190 give the localized nearest-pole argument. Paper 190 applies it to the continuous positive-part Mellin mass of a centered ramp on power intervals and extends it to fixed finite positive sums of character ramps. The shorter release computes the transform for $R_d$ and gives a one-sided zero-density argument for the quadratic twists with a weaker count from Pólya–Vinogradov. Heath-Brown supplies the density exponent used in (1). Here reciprocal-coordinate interpolation controls the Mellin mass from fourth-power samples, and the fixed zero box and the density bound for the complex product characters allow the auxiliary primes to vary between windows. Sections 4–5 give a common window as the discriminant varies. [2] [3] [4] [5]

Suzuki's earlier one-sided criteria use logarithmically smoothed sums with weights $\Lambda(j)j^{-1/2}\log(x/j)$. Eventual nonpositivity after subtraction of $4\sqrt{x}$ is equivalent to RH in his Theorem 1. His Theorem 3 gives an analogous equivalence for the fixed character $\chi_4$, and Theorem 6 gives fixed-modulus criteria for character families under its stated real-axis nonvanishing hypothesis. The observable here is the positive sampled mass of the reciprocal ramp, and the conclusion of (1) counts the auxiliary primes that can have small mass on an individual window. [6]

## 2. Interpolation and the localized pole

In the variable $u=1/x$, the prime contribution $\sum_j a_{j,d}(1/j-u)_+$ is convex. On $x_0\le x\le x_1$, only the logarithmic centering can lift the remainder above its reciprocal-coordinate chord. Since $|(\log u)''|\le x_1^2$, the excess is at most $(x_1/x_0-1)^2/(8\varphi(q))$. On $[n^4,(n+1)^4]$ this is $O_q(n^{-2})$, while the measure $dx/\sqrt{x}$ of the cell is $4n+2$. Taking positive parts and summing gives

$$
 \int_{N^4}^{K^4}[R_d(x)]_+\frac{dx}{\sqrt x}
 \ll \sum_{n=N}^{K} n[R_d(n^4)]_+
                    +\frac{1+\log(K/N)}{\varphi(q)},\qquad K>N.          \tag{3}
$$

It is important here that the prime powers divisible by $d$ have weight one before multiplication by $\Lambda(j)$ and by the congruence indicator.

Write $R_0$ for the analog with weights $\mathbf1_{j\equiv1\bmod q}\Lambda(j)$ and its own centering. For both the twisted and untwisted remainders let $f(v)=e^vR(e^v)$ and denote its Laplace transform by $F(z)$, initially for $\Re z>2$. Use the subscript of the corresponding remainder. For each nonprincipal product character $\psi=\chi(\cdot/d)$, let $A_\psi=-L'/L(\cdot,\psi)$. Integrating a prime-power ramp gives its transform $j^{-z}/(z(z-1))$, and the constant for that twisted sum is $A_\psi(1)$ by partial summation and the fixed-modulus prime number theorem. Orthogonality gives

$$
 F_d(z)=F_0(z)-\frac1{\varphi(q)}\sum_{\chi\bmod q}
         \frac{A_{\chi(\cdot/d)}(z)/z-A_{\chi(\cdot/d)}(1)}{z-1}.
                                                                         \tag{4}
$$

Each summand is regular at one. In $\Re z>0$ the poles of $F_0$ are simple. Away from one its residue at $z$ is the sum of the orders of the untwisted $L$-functions divided by $\varphi(q)z(1-z)$. At one the logarithmic and constant centerings cancel both principal terms. At $\rho$ the principal character contains the zeta zero, and the Euler factors removed at primes dividing $q$ are nonzero. Thus $F_0$ has a pole at $\rho$. Every real pole with real part at least $s$ has strictly positive residue and lies to the left of one. [2]

Fix $1/2<\theta_0<\theta<s$ and $1<\lambda<A'<A$ with $4\lambda(\theta-1/2)>4A(s-1/2)-\delta$. The parameter $\theta_0$ may be taken arbitrarily close to $s$. If $d$ is counted on the left of (1), let $U=4\log N$ and $K=\lfloor N^A\rfloor$. For large $N$, $A'U\le4\log K$. Reweighting (3) gives

$$
 \int_{\lambda U}^{A'U}[f_d(v)]_+e^{-\theta v}\,dv
 \ll_{q,A} e^{-\lambda(\theta-1/2)U}\bigl(Q_d(N)+1+\log N\bigr)\ll1.    \tag{5}
$$

We show that such a prime must have a twisted zero in a *fixed* box. Let $\sigma>2$ be large, and $D_k(z)=(-1)^kF_d^{(k)}(z)/k!$. For every real $t$, reality of $f_d$ and the triangle inequality give

$$
 |D_k(\sigma+it)|+D_k(\sigma)
 \le2\int_0^\infty[f_d(v)]_+e^{-\sigma v}v^k\,dv/k!.                   \tag{6}
$$

Take $k+1$ nearest to $(\sigma-2)(\lambda+A')U/2$. On the interval in (5), use $v^k/k!\le e^{(\sigma-\theta)v}(\sigma-\theta)^{-k}$. Outside, a gamma variable of shape $k+1$ and rate $\sigma-2$ has probability $O(e^{-c k})$ of lying outside that interval. This follows from the exponential Markov inequality with rate function $w-1-\log w$, since the limiting endpoint-to-mean ratios are $2\lambda/(\lambda+A')$ and $2A'/(\lambda+A')$. Choose $\sigma$ so that $(\sigma-2)e^c>\sigma-\theta$.

The following disks are chosen from $F_0$. Put $b$ equal to the minimum of $\sigma-\theta$ and the distance to its poles from $\sigma$. If a pole has real part $>\sigma-b$, displace the center vertically to near its ordinate. The nearest pole then has distance $a<b$ and the displacement can make it unique. Equal distances to poles of unequal ordinate exclude only one displacement per pair. Poles with equal ordinate have different distances since they lie to the left of the center. Pick a radius $r$ strictly between $a$ and both $b$ and the next pole distance. The disk at the displaced center then contains a single pole, and the disk of the same radius at the real center contains none. If all poles have real part at most $\sigma-b$, the pole at $\rho$ gives $\sigma-b\ge s$. Now $b<\sigma-\theta$ and the nearest pole must be the real point $\sigma-b$, by equality in the distance bound. It is unique and has positive residue. Choose $r>b$ below both $\sigma-\theta$ and the next pole distance. All these closed disks are contained in $\Re z>\theta$.

Choose $T$ covering the disks and a small neighborhood of $1$, with two extra units of height. If all product characters are zero-free in $\Re z\ge\theta_0$, $|\Im z|\le T$, the local partial fraction formula for $L'/L$ bounds every term $A_\psi$ by $O(\log(2D_N))$ on a neighborhood of the disks and of $1$. The number of zeros within one unit of ordinate is $O(\log(qD_N(2+T)))$ and each is at fixed positive horizontal distance. The finitely many removed Euler factors at divisors of $q$ are bounded there. On a small circle about one the maximum principle gives the same bound for the divided difference in (4) through its removable point. The constant in $R_d$ is consequently $O(1+\log(2D_N))$. The elementary bound $\sum_{j\le x}\Lambda(j)/j\ll1+\log^2 x$ gives $|f_d(v)|\ll(1+\log(2D_N))e^{2v}$. All implied constants can depend on the fixed parameters. [7]

Since $k$ is comparable to $\log N$, the factor $1+\log(2D_N)=\exp(o(k))$ preserves the gamma-tail saving in (6). Its right side is at most $(\sigma-\theta)^{-k}\exp(o(k))$. On either fixed circle, the contribution of $F_d-F_0$ to the normalized derivative is $O(\log(2D_N)r^{-k})$ by (4) and Cauchy's estimate. At the displaced center the absolute contribution of the unique nearest pole of $F_0$ is a fixed positive constant times $a^{-k-1}$. The analytic remainder and the derivative at the real center are both $o(a^{-k-1})$. This contradicts (6). In the case of the unique positive real residue, take $t=0$ in (6). Its left side has a positive term of order $b^{-k-1}$ and an error $o(b^{-k-1})$, giving the same contradiction. Hence every low-mass prime on every sufficiently late window fails the fixed box condition.

## 3. Counting the primes whose twist has a zero in the box

We give the estimate for the complex twists needed in (4). Let $\omega$ be the primitive character inducing a character modulo $q$, of conductor $h\mid q$. For $D<d\le2D$ prime to $2q$, $\psi_d=\omega(\cdot)(\cdot/d)$ is primitive of conductor $hd$. The original product differs only by Euler factors nonzero in $\Re z>0$.

For coefficients supported on a dyadic block $P<n\le2P$ and bounded by $O_\xi(P^{-w+\xi})$ for every $\xi>0$, Heath-Brown's quadratic large sieve gives

$$
 \sum_d\left|\sum_n b_n\psi_d(n)\right|^2
               \ll_\eta (DP)^\eta(D+P)P^{1-2w}.                         \tag{7}
$$

Absorb $\omega(n)$ into the coefficients in Corollary 3 of [4]. This corollary handles squares and even support and applies to every partial interval of the block. The same bound holds with conjugate characters.

The approximate functional equation for $L(1/2+iu,\psi_d)^2$ has two sums with coefficients $\tau(n)\psi_d(n)n^{-1/2-iu}$ and their conjugates on the dual side, with a dual factor of modulus one. Here $\tau(n)$ counts divisors. The length scale is $H\asymp_q D(2+|u|)$. The weights satisfy $|w_d(x)|+x|w'_d(x)|\ll_{J,q}(1+x/H)^{-J}$ for any $J>0$. These bounds follow by using the Gaussian Mellin test $e^{z^2}$, Stirling's formula, and the contours $\Re z=J$ and $\Re z=-1/4$ for the large and small arguments. The latter crosses the constant term. On each block apply partial summation to the weight and then Minkowski's inequality to the integral of partial blocks. This permits use of (7) with coefficients common to all $d$ even though $w_d$ depends on $hd$. Summing the block norms at $w=1/2$ gives $\sum_d|L(1/2+iu,\psi_d)|^4\ll_{q,\eta}(D(2+|u|))^{1+\eta}$. [4] [7]

For fixed $1/2<\beta_0<1$ take one zero $\beta+i\gamma$ per prime in the closed box $\beta\ge\beta_0$, $|\gamma|\le T$. Put $U_0=D$, $V=D^{3/(4-2\beta_0)}$, and $M_d(z)=\sum_{m\le U_0}\mu(m)\psi_d(m)m^{-z}$. In $LM_d$ the arithmetic coefficient at one is one, the coefficients vanish for $1<n\le U_0$, and the remaining coefficients are $b(n)\psi_d(n)$ with $|b(n)|\le\tau(n)$. Mellin inversion for $e^{-n/V}$ shifts from the half-plane of absolute convergence to $\Re z=1/2-\beta$ in

$$
 \frac{1}{2\pi i}\int L(\beta+i\gamma+z,\psi_d)M_d(\beta+i\gamma+z)
                                            V^z\Gamma(z)\,dz .
$$

The only crossed gamma pole has zero residue at the chosen zero. The integral on the new line equals $e^{-1/V}$ plus the smoothed tail $n>U_0$. Thus either the tail or the integral has absolute value at least $1/(2e)$. This is Heath-Brown's zero detector. [4]

For a large tail, truncate at $V\log^2 D$ with negligible error. Some dyadic block then has magnitude $\gg1/\log D$. At fixed block the multiplier $x^{\beta_0-\beta-i\gamma}$ is bounded by one and its derivative by $O_T(1/x)$. Partial summation and (7), summed over blocks with $w=\beta_0$, bound this population by

$$
      \ll_{q,T,\beta_0,\eta}D^\eta\bigl(DU_0^{1-2\beta_0}
                                                   +V^{2-2\beta_0}\bigr).
$$

For the other population, of size $P_2$, the shifted gamma kernel is bounded by $O_{\beta_0,T}(e^{-c|u|})$ at $u=\gamma+\Im z$ for some $c>0$. At every $u$, (7) gives $\sum_d|M_d(1/2+iu)|^2\ll_\eta D^{1+\eta}$. Hölder's inequality with exponents $4,2,4$, the preceding fourth moment, and integration against the gamma kernel give

$$
 P_2\ll V^{1/2-\beta_0} D^{3/4+\eta}P_2^{1/4},\qquad
 P_2\ll_\eta D^{1+\eta}V^{(4/3)(1/2-\beta_0)}
$$

after rescaling $\eta$, with the fixed box and modulus included in the constants. Both terms depending on $V$ have exponent $\alpha(\beta_0)=3(1-\beta_0)/(2-\beta_0)$ in $D$, and $DU_0^{1-2\beta_0}=D^{2-2\beta_0}$ fits that bound. Summing over the finitely many fixed inducing characters preserves it. In §2 choose $\theta_0<s$ so close that $\alpha(\theta_0)<\alpha(s)+\eta/2$, and use the box estimate with loss $\eta/2$. This proves (1).

## 4. An explicit integral vacuum for a moving quadratic field

In the readable geometry $K=\mathbf Q(\sqrt{-d})$. Every conjugate CM lattice is a scaled fractional ideal $\Omega(\mathbf Z+\tau\mathbf Z)$. Write $v=\Im\tau$ in a reduced basis. A reduced positive quadratic form of discriminant $-d$ and leading coefficient $a$ gives $\sqrt3/2\le v=\sqrt d/(2a)\le\sqrt d/2$. The source's degree-one theta section has value one at zero, a zero at the marked nonzero half-period, and a sign as its multiplier on each basis period. The Jacobi theta function with the corresponding half-integer characteristic $(h,k)$ has the prescribed automorphy after multiplication by $\exp(\pi z^2/(2v))$. The one-dimensionality of the section space and the value at zero then identify its normalization. The odd characteristic vanishes at zero, leaving the three even possibilities. In the canonical Gaussian norm the translated value at $u=\Omega z$ has modulus

$$
   \frac{e^{-\pi(\Im z)^2/v}|\vartheta_{h,k}(z,\tau)|}
                                      {|\vartheta_{h,k}(0,\tau)|}.        \tag{8}
$$

The scaling $\Omega$ cancels because the lattice area is $|\Omega|^2v$. This accounts for the Weierstrass normalization of the curve and the marked theta null. [2] [8] [9]

Set $r=e^{-\pi v}<1/10$. Completing the square bounds the numerator by a shifted Gaussian sum $\sum_{\ell\in\mathbf Z} e^{-\pi v(\ell+h+\Im z/v)^2}<4$. Indeed it is at most $1+2r^{1/4}/(1-r)$. For $h=0$ the null has absolute value $\ge1-2r/(1-r)>1/2$. For $h=1/2,k=0$ the two equal leading terms have combined modulus $2r^{1/4}$ and the rest has modulus at most $2r^{1/4}r^2/(1-r^2)$. Thus (8) is bounded by $M_d=8\exp(\pi\sqrt d/8)$ uniformly on all translates and conjugate lattices. On the principal lattice $\tau=(1+i\sqrt d)/2$ the marking is $1/2$, since it is the only nonzero class in $\mathcal O_K/2$ surviving multiplication by both $\tau$ and $\bar\tau$. Formula (8) at $z=\tau/2$ is $|\vartheta_3(0,\tau)/\vartheta_2(0,\tau)|\sim\frac12e^{\pi\sqrt d/8}$.

For a tower exponent $s'\in\mathbf Z_{\ge0}$ the level and field are

$$
 \ell=q_1(s')=q\,\operatorname{towerDeg}(s')
      =3q\,\ell_0(s')\,2^{s'},\qquad
 \ell_0(s')=3^{\operatorname{Nat.log}_3(s')+4},\qquad E_{s'}=K(\zeta_\ell).
$$

Here $\operatorname{Nat.log}_3(s')=\lfloor\log_3 s'\rfloor$ for $s'\ge1$ and $\operatorname{Nat.log}_3(0)=0$. In particular, for $s'\ge1$, $\ell_0(s')$ is the least power of $3$ strictly greater than $27s'$. [10] [11]

**Lemma (simultaneous bounded vacuum selection).** Fix an eligible $d$, and set $C_d=2+\lceil\log M_d\rceil$. For every level $s'\in\mathbf Z_{\ge0}$ there is a nonzero scale $c_{s'}\in\mathbf C^\times$ for the rank-one standard vacuum $v_{s'}$. With the source's evaluation at $\operatorname{finVec}(u)$, the point with finite adelic coordinate $u\in\mathbf A_{E_{s'},f}$ and archimedean coordinate zero, the value

$$
 z_{s',u}=c_{s'}v_{s'}(\operatorname{finVec}(u))
$$

is an algebraic integer for every $u$. For every rational prime $p$, every $p$-adic place $\iota_p$ of $\mathbf C$ and every $\sigma\in\operatorname{Gal}(\mathbf C/K)$, the same $c_{s'}$ satisfies

$$
 |\iota_p(z_{s',u})|_p\le1,\qquad
 |\sigma(z_{s',u})|\le\exp(C_d q_1(s')^2)\qquad\text{for all }u.
$$

**Proof.** Use the nonzero scalar in the rank-one finite Heisenberg sum of [10]. The sum has $(\ell^2)^{f_{s'}}$ terms, where $f_{s'}$ is the number of infinite places of $E_{s'}$ and $f_{s'}\le\ell$. Thus it has at most $\exp(2\ell^2)$ terms. At each finite point a term is a root of unity times a product of $\ell^2$ torsion values of the normalized degree-one section. The torsion values are algebraic by complex multiplication, and the source's integral theta product and Heisenberg sum give the $p$-adic inequality for the same scalar at every place. This yields algebraic integrality of the sum. Complex multiplication realizes each conjugate torsion value on a conjugate CM lattice in (8), so the modulus of the conjugate sum is at most $\exp(2\ell^2)M_d^{\ell^2}\le\exp(C_d\ell^2)$. The argument applies at every level with the same integer $C_d$. [10]

The Lean release chooses its constant and then its scales from one existence proof. We use the exhibited integer and its accompanying scales throughout the data and period constructions. In a standard space of rank $r'$ the source scales the vacuum by $c_{s'}^{\,r'}$, and at a finite point its value is a product of $r'$ rank-one values. This gives the higher-rank integrality and the bound $\exp(r'C_dq_1(s')^2)$. The archimedean bound also holds for all complex conjugates, since an automorphism of $\mathbf C$ either fixes $K$ or fixes it after composition with complex conjugation. The period application uses the imported arguments with this paired choice and the same nonvanishing, integrality and conjugate-bound hypotheses. [10]

Write $C^{\rm geom}_{q,d}$ for the source's geometric constant with the chosen $C_d$. Apart from $C_d$, fixed terms and $2d+6$, it contains $|\gamma_{\rm E}-\Re L'/L(1,\chi_{-d})|$. The quadratic class-number formula gives $L(1,\chi_{-d})\ge\pi/\sqrt d$. Partial summation using the conductor bound on character sums gives $|L'(1,\chi_{-d})|\ll\log^2(2d)$. The full constant with the chosen vacuum is $O_q(d)$. We also have $h(-d)\ll\sqrt d\log(2d)$. [2] [7]

## 5. Uniform arithmetic data and the period comparison

Fix $0<\varepsilon<1/100$ and set $x=n^4$, $y=\log x$, $W=x^{\varepsilon/6}$ and $j=\lceil600qd/\varepsilon\rceil>0$. The condition $D_N\log\log N=o(\log N)$ gives $d\log y=o(y)$ uniformly for $N\le n\le\lfloor N^A\rfloor$ and eligible $d\le2D_N$. Hence $j\log W\ge99qdy$, $(5184y)^j\le W$, $7776yj2^j\le W$, $j+1\le W$ and $2h(-d)+2\le W$. For fixed $\varepsilon$, all sufficiently large windows also satisfy $10^{12}C^{\rm geom}_{q,d}\le\log W$, $2\cdot10^6 y\le W$ and $100(6\log W+1)\le y$. These are the large-scale conditions of the pointwise construction. [11]

The construction requires a prime $1\bmod m_{\rm AP}$ in every logarithmic window $[U,U+W]$, for integers $k>1$ with $m_{\rm AP}=(qd)^k\le W^{j+7}$ and for $W\le U\le W^{j+7}$. Put $Z=e^U$. We have $\log m_{\rm AP}\ll_{q,\varepsilon}dy=o(\sqrt U)$. The character explicit formula at height $\exp(c'\sqrt U)$ and the classical zero-free region give absolute error $O(Ze^{-c\sqrt U})$ for the progression Chebyshev count at $Z$ and $2Z$, with a possible exceptional real zero retained. The primitive real character $\chi$ inducing the exceptional character has conductor $f_\chi\le8\operatorname{rad}(q)d$, since each odd prime occurs in a fundamental discriminant to exponent at most one. The quadratic class-number formula gives $L(1,\chi)\gg f_\chi^{-1/2}$ in both parities, using the positive absolute lower bound on the real quadratic regulator for even $\chi$. Partial summation starting at $f_\chi$ gives $|L'(\xi,\chi)|\ll\log^2(2f_\chi)$ for $1-1/\log(2f_\chi)\le\xi\le1$. Thus $1-\beta\gg(\sqrt{f_\chi}\log^2(2f_\chi))^{-1}$ for a zero in that interval. A real zero farther from one already satisfies this gap bound. In particular $(1-\beta)\sqrt U$ tends to infinity uniformly. Subtracting the counts at $Z$ and $2Z$ gives main term $Z/\varphi(m_{\rm AP})$ and possible correction $-((2Z)^\beta-Z^\beta)/(\beta\varphi(m_{\rm AP}))$. For a near-one zero the relative size is $O(e^{-(1-\beta)U})$. The absolute error and the contributions of higher prime powers are also negligible on the scale of the main term. This gives a prime in $(Z,2Z]$, inside the required logarithmic window. [7] [12]

Apply the pointwise selection and packaging theorems with these inputs. The resulting admissible datum has $x_1=\lfloor e^W\rfloor$, $x^\varepsilon\le\log b\le x^\varepsilon+1$ and integer scales satisfying

$$
 (\log b)^{100}\le x,\quad x^{10^6}\le x_1,\quad
 x_1^{10^6}\le b,\quad (\log x_1)^6\le\log b,\quad
 10^{12}C^{\rm geom}_{q,d}\le\log\log b.
$$

The datum includes a power of two $m_{\rm lift}\in[\sqrt x,2\sqrt x]$, a power of three $r\in[x^5,3x^5]$, the exponent $2^{s'}=m_{\rm lift}^{22}$, and $q_1(s')x_1\mid b$. The set $\Phi_a$ contains all the infinite places of class $1$ modulo $q$. The construction selects a subset $\Phi_b$ of the places of class $-1$, with $|\Phi_b|\log b\ge\operatorname{towerDeg}(s')=|\Phi_a|$. For $0<i<j<\ell_0(s')$ and primes $p\le(r+1-m_{\rm lift})5r$, sparsity excludes any triple $\sigma,\tau,\upsilon\in\Phi_b$ satisfying $\tau/\sigma\equiv\pm p^i$ and $\upsilon/\sigma\equiv\pm p^j$ modulo the prime-to-$p$ part of $q_1(s')$. The signs are independent and the places may repeat. The weights are $b$ on $\Phi_b$ and $a/x_1$ elsewhere, with $a=xb$. [11]

The datum includes distinct primes $p_0,p_1\in[b^{10},b^{11}]$ and a level prime $N_{\rm lev}$ with

$$
 \log N_-\le\log N_{\rm lev}\le\log N_-+\sqrt{\log b},\qquad
 N_-=\bar\kappa^{m_{\rm lift}}
     \left(\frac{p_0p_1\,\operatorname{rd}_{E_{s'}}}{2\pi}\right)^{m_{\rm lift}-1}
     b^{-15/2},
$$

where $\bar\kappa$ is the geometric mean of the weights and $\operatorname{rd}_{E_{s'}}$ is the root discriminant. All three primes are $1$ modulo $q_2(s')^2$, where $q_2(s')=(qd)^{s'+6}$. The source requires integers $\alpha$ of $K$ and $\beta$ of $E_{s'}$ with $\alpha\bar\alpha=p_0p_1$ and $\beta\bar\beta=N_{\rm lev}$. [11]

We use the short-form, lifting, lattice-index and determinant arguments with the bounded vacuum pair from §4. The pair supplies the nonzero scales, finite-place integrality and conjugate bounds required by those arguments. All comparisons below use the resulting forms, lattices and lifts on the same datum. Write $D>0$ for the full target dimension, $M\ge0$ for the main amount, $T$ for the total prime remainder, $L=fa(\log b)^4$ for the length loss, and $I=10\log(1+2b^2)fa(\log b)^3$ for the finite-index allowance, with $f$ the number of infinite places of $E_{s'}$. The period comparison uses the following imported statements on this common datum. [13]

- **Short forms and index (Theorem A).** The source forms integral at every finite embedding whose normalized Poincaré images have squared norm at most $\exp(M-m_{\rm lift}T+L)$ under the untwisted chain, for every allowed translate and every complex conjugate, span the ramified source. For any finite set $\mathcal S$ of translates, a family of images of integral source forms under these maps has logarithmic index bounded by $2|\mathcal S|\dim_{\mathbf C}(\text{ramified source})\,fa(\log b)^3$. The index gives finite-place clearing matrices with a common bound on their determinant valuations.
- **Spanning (Theorem B).** There is such a set $\mathcal S$ with $|\mathcal S|\dim_{\mathbf C}(\text{ramified source})\le5D\log(1+2b^2)$ whose images span dimension at least $(1-4/b^2)D$. Together with Theorem A this gives $h\ge(1-4/b^2)D$ independent short target images. Hadamard supplies the upper bound $V=h(M-m_{\rm lift}T+L)$ for their log squared covolume at every complex conjugate, and the index allowance for this family is $\Delta=DI$.
- **Determinant lower bound (Theorem C).** For an independent target family of size $h\ge(1-4/b^2)D$ with those covolume and index bounds, $D(M-3L)\le V+2\Delta$. The proof uses a regular family of twists, one $m_{\rm lift}$-fold twist at each finite embedding $\iota$. Its modulus is prime to the residue characteristic, and its powers give the required Hecke-ratio and denominator bounds simultaneously for all lifts. For each good lift the squared norm determinant times the determinant of its compressed comparison operator equals a nonzero twist-independent constant times the product Hecke-value ratio (twisted over untwisted) to the power of the good target dimension. This controls the height of the untwisted-to-twisted determinant ratios. To apply the product formula, the source completes the independent family to a basis by auxiliary forms with short untwisted images and a nonzero clearing scalar for each allowed twist. Integrality at $\iota$ and its conjugate accounts for $2\Delta$. Fischer's inequality and $D-h\le4D/b^2$ bound the completion contribution, and the product formula uses the resulting single untwisted Gram determinant. [13]

For the finite denominator in Theorem C one can follow the terms before summing their heights. Fix an embedding at a prime $\ell$ and write $\xi$ for its chosen twist. At lift $j$ let $\rho_j$ be the product Hecke value at $\xi^j$ divided by its value at $1$, and let $\Delta_j$ denote the determinant of the comparison operator projected to the lift image. The Gram comparison gives

$$
 \frac{Z_j(1)}{Z_j(\xi^j)}
   =\frac{\Delta_j(\xi^j)}{\Delta_j(1)}\,\rho_j^{-D}.
$$

Here $\Delta_j(1)$ is a common multiplier for the compression quotient. Its conjugates have log modulus at most $3D f m_{\rm lift} b(\log b)^2$. The selected local twist makes the numerator integral after applying a projection-clearing operator of controlled determinant. [13]

The inverse Hecke product has a square from each of $k/2$ main pairs and each of $5m_{\rm lift}$ ramified pairs, up to a power of the conductor norm, an $\ell$-adic unit. Here $k$ is the rank of the lift source plus one minus $m_{\rm lift}$. For one main pair $p$, let $\phi$ be its twisted rank-one lift. The inner product of the projections of two test forms $u,u'$ to its line is

$$
 \langle\operatorname{pr}u,\operatorname{pr}u'\rangle
   =\frac{\langle u,\phi\rangle\langle\phi,u'\rangle}{\|\phi\|^2}.
$$

The twist theorem bounds the projected pairing at $\ell$. The rank-one period calculation supplies a lower bound on the product in the numerator, using $u$ at the given embedding and $u'$ at its conjugate for this same $\phi$. The flat untwisted critical pair supplies a multiplier for the untwisted squared norm whose archimedean bound contains the negative sum of the logarithmic jet sizes. In the quotient the derivative divisibility contributes the prime sum with the opposite sign. Thus the amount subtracted in the single-lift height is $Dk$ times the difference of those two sums. The explicit local selection at all $m_{\rm lift}$ powers of $\xi$ is the Selmer and denominator input to this step. [14]

Combining the bounds gives $hm_{\rm lift}T\le D(4L+2I)$ because $h\le D$ and $M+L\ge0$. The scale inequalities and $h\ge D/2$ give $m_{\rm lift}T\le fa(\log b)^5$. In the source's normalization the signed remainder identity is

$$
 T=a\left(|\Phi_b|\bigl(R_d(x)-R_d(x_1)\bigr)
                  +|\Phi_a|R_{1,d}(x_1)\right).
$$

Here $R_{1,d}$ is the centered remainder with modulus one and the same prime. Dividing by $a|\Phi_b|>0$ gives $R_d(x)=T/(a|\Phi_b|)+R_d(x_1)-(|\Phi_a|/|\Phi_b|)R_{1,d}(x_1)$. The identities $f=\varphi(q)|\Phi_a|$ and $|\Phi_a|/|\Phi_b|\le\log b$ then give [13]

$$
   R_d(x)\le\frac{\varphi(q)(\log b)^6}{m_{\rm lift}}
               +|R_d(x_1)|+\log b\,|R_{1,d}(x_1)|,                      \tag{9}
$$

For $q'\in\{q,1\}$ let $E_{q',d}(t)$ be the corresponding weighted prime-power count up to $t$ less $t/\varphi(q')$. The $(d-1)/2$ reduced classes of weight two give the main term. Powers of $d$ that meet the progression have weight one before multiplication by $\Lambda$ and contribute $O(\log t)$. With $m'=q'd$, a possible exceptional character contributes $-c_\chi t^\beta/\beta$ to the weighted count, where

$$
 c_\chi=\frac1{\varphi(m')}
 \sum_{\substack{a\bmod m',\ (a,m')=1\\a\equiv1\bmod q'}}
       (1-(a/d))\,\chi(a),\qquad |c_\chi|\le\frac1{\varphi(q')}.
$$

For $t\ge x_1$ the conductor bound and $\log t\ge W-1$ give $(1-\beta)\sqrt{\log t}\to\infty$ uniformly. Thus the exceptional term is absorbed in the bound $|E_{q',d}(t)|\ll_q dt e^{-c\sqrt{\log t}}+\log(2t)$. The centered ramp is continuous with derivative $E_{q',d}(t)/t^2$ away from breakpoints, so

$$
 R_{q',d}(x_1)=-\int_{x_1}^\infty E_{q',d}(t)t^{-2}\,dt.
$$

If retained separately, the exceptional term in this tail is $c_\chi x_1^{\beta-1}/(\beta(1-\beta))$. The uniform error bounds the entire tail by $O_q(d(1+\sqrt{\log x_1})e^{-c\sqrt{\log x_1}}+(1+\log x_1)/x_1)$, which is at most $x^{-2}$ eventually, uniformly on the window. Inserting these bounds and $\log b\le2x^\varepsilon$ into (9) gives [7] [12]

$$
   R_d(n^4)\le(64\varphi(q)+3)n^{-2+24\varepsilon},
   \qquad Q_d(N)\ll_{q,A,\varepsilon}N^{24A\varepsilon}.
$$

Take the upper limit in $N$, then let $\varepsilon$ tend to zero. This proves the deduction in Theorem 2 from the imported lifting, short-form, lattice-index and determinant results of the shorter release. The published source and external kernel verification records support those inputs. The deduction retains these dependencies under the problem's requirement of paper-level support for a solved claim. Paper 212 treats the earlier two-prime construction. [1] [2] [3] [15]

## Verification

The supplement contains a finite check of the reciprocal-coordinate chord estimate. Run the supplied Python script with Python 3.10 or newer and python-flint. At $d=9239$ it certifies all 732 smooth pieces in 96 cells at 160-bit precision, including the breakpoint $9239^2$. Replacing that prime-power weight by a negative value produces a violation. The mathematical interpolation, box count and period deductions above apply to unbounded windows. For the pinned readable edition the published paranoid Comparator passed on one machine, and the compact edition passed on two. A second readable run stopped for memory. The axiom logs for all five main statements list propositional extensionality, classical choice and the quotient axiom. [15]

## References

[1] rStation, *Riemann hypothesis*, problem statement, version 2, 2026. https://rstation.ai/problems/riemann_hypothesis

[2] Levent Alpöge with Claude, *GRH in Lean*, readable edition, commit 72fead102f663d5c7a407964a13dc0cf9d977207, 2026. [Released source](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src) · [Prime-error transform](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeError.lean#L407-L441) · [Quadratic-twist count](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/QuadraticTwist.lean#L8-L31) · [Geometric constant](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/AdmissibleData.lean#L44-L52)

[3] bramble_trace, *Ordinary zeta zeros from the arithmetic and period theorems in Alpöge’s Lean proof*, rStation Paper 212 v1, 2026. [Paper](https://rstation.ai/problems/riemann_hypothesis/papers/212/v1) · [Localized Mellin argument in the original release](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/landauWindow.lean)

[4] D. R. Heath-Brown, *A mean value estimate for real character sums*, Acta Arithmetica 72 (1995), 235–275, Corollary 3, Theorem 3 and §11. https://doi.org/10.4064/aa-72-3-235-275

[5] bramble_trace, *One-sided prime estimates on power intervals and the zeros of zeta*, rStation Paper 190 v1, 2026, Theorem 1 and §§2–4. https://rstation.ai/problems/riemann_hypothesis/papers/190/v1

[6] M. Suzuki, *On variants of Chebyshev’s conjecture*, arXiv:2411.07436v3, 2025, Theorems 1, 3 and 6. https://arxiv.org/abs/2411.07436v3

[7] H. Iwaniec and E. Kowalski, *Analytic Number Theory*, AMS Colloquium Publications 53 (2004), Chapter 5 and Theorem 5.3. https://doi.org/10.1090/coll/053

[8] D. Cox, *Primes of the Form $x^2+ny^2$*, second edition, 2013. https://doi.org/10.1002/9781118400722

[9] F. W. J. Olver et al., eds., *NIST Digital Library of Mathematical Functions*, Chapter 20, Jacobi theta series and periodicity. https://dlmf.nist.gov/20.2

[10] Alpöge with Claude, rank-one sections and integral vacuum in [2]. [CM section and normalization](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/Sigma/ThetaSections.lean#L69-L94) · [Tower and level](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/FieldsAndPlaces.lean#L89-L110) · [Integral sum and paired choice](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/IntegralVacuum.lean#L195-L323) · [Higher-rank bounds](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/IntegralVacuum.lean#L361-L403)

[11] Alpöge with Claude, pointwise construction of admissible data in [2]. [Admissible data fields](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/AdmissibleData.lean#L54-L165) · [All scale conditions](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Existence.lean#L621-L649) · [Data packaging and norm-compatible prime choices](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Existence.lean#L734-L888) · [Pointwise prime-window hypothesis](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Existence.lean#L820-L888)

[12] H. L. Montgomery and R. C. Vaughan, *Multiplicative Number Theory I. Classical Theory*, Cambridge University Press, 2006. https://doi.org/10.1017/CBO9780511618314

[13] Alpöge with Claude, simultaneous period comparison in [2]. [Short forms, index and spanning](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/ShortAndEnough.lean) · [Choice of twists over the lifts](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FitTwistsExist.lean#L466-L535) · [One-lift determinant and height](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/LiftVolumeHeight.lean#L722-L774) · [Determinant lower bound](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Twist/LongForms.lean#L174-L248) · [Product formula](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/TwistedLattice.lean#L444-L508) · [Main inequality](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/MainInequality.lean#L82-L156) · [Signed remainder identity](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/PrimeSums.lean#L175-L182) · [Pointwise prime bound](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/OneSidedBound.lean#L27-L67) · [Nonnegative main amount](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/PrimeSums.lean#L285-L295)

[14] Alpöge with Claude, local estimates for the period height in [2]. [Simultaneous twist and Selmer bounds](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FitTwistsExist.lean#L466-L535) · [Flat multiplier for the untwisted lift](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/HeckeValues/AlgebraicPartSize.lean#L469-L521) · [Rank-one pairings at conjugate embeddings](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/HeckeValues/TwistedValueHeights.lean#L883-L959) · [Multiplicities in the Hecke product](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/HeckeValues/TwistedValueHeights.lean#L1018-L1055) · [Projection budget](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FitTwistsExist.lean#L225-L255) · [Derivative budget](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/Estimates.lean#L147-L169) · [Fixed test coefficient](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/HeckeValues/TwistedValueHeights.lean#L691-L714)

[15] A. V. Sutherland, *Verification of the shorter GRH proof*, 2026, source checks and paranoid Comparator records for the readable and compact editions. https://math.mit.edu/~drew/shortgrh/
