# A fourth-power criterion for zeta zeros with changing auxiliary primes

## 1. The sampled prime sum

The readable edition of Levent Alpöge's proof with Claude bounds an arithmetic function by comparing the sizes of a common family of periods. The function is a centered prime-power sum with a twist by the Legendre symbol. We ask how many auxiliary primes have to satisfy the bound and which cutoffs one needs to observe. The original release and its natural-language counterpart in Paper 212 use a family indexed by two primes. The shorter release fixes a modulus and varies one quadratic field. We use the latter construction with an explicit normalization for the rank-one theta section. Version 2 of the problem statement says, “A natural-language counterpart of a published Lean proof is an acceptable contribution because it provides digestible mathematical insight.” [1, 2, 3]

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

The onset can depend on the chosen sequence $D_N$. In particular suppose nonempty sets of primes $\mathcal D_N$ in those progressions, on some sequence of windows, satisfy $\sup_{d\in\mathcal D_N}\log(1+Q_d(N))/\log N\to0$. If $\kappa=\limsup\log(1+\#\mathcal D_N)/\log D_N$, every nontrivial zero satisfies

$$
                  \frac{\kappa}{3-\kappa}\le\Re\rho
                                   \le\frac{3-2\kappa}{3-\kappa}.         \tag{2}
$$

Indeed (1) gives $\kappa\le3(1-s)/(2-s)$ for each zero to the right of the critical line. Solving and applying the functional equation gives (2). The sets on different windows may be disjoint.

**Theorem 2.** Using the short-form, lifting, lattice-index and determinant theorems of the readable edition, the uniform subpower estimate above holds for every eligible $d\le2D_N$ when $D_N\log\log N=o(\log N)$. For example, take $D_N=\log N/(\log\log N)^2$. The prime number theorem for the fixed progression then gives $\kappa=1$ and (2) proves ordinary RH.

The localized pole argument occurs in the original release, and the transform for $R_d$ is computed in the shorter one. Heath-Brown's density theorem supplies the exponent in (1) for real characters. Our argument includes the fixed complex character factors and makes the pole estimate uniform in the prime on a sampled window. The last two sections give the simultaneous geometric supply of those windows. [2, 3, 4]

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

Choose $T$ covering the disks and a small neighborhood of $1$, with two extra units of height. If all product characters are zero-free in $\Re z\ge\theta_0$, $|\Im z|\le T$, the local partial fraction formula for $L'/L$ bounds every term $A_\psi$ by $O(\log(2D_N))$ on a neighborhood of the disks and of $1$. The number of zeros within one unit of ordinate is $O(\log(qD_N(2+T)))$ and each is at fixed positive horizontal distance. The finitely many removed Euler factors at divisors of $q$ are bounded there. On a small circle about one the maximum principle gives the same bound for the divided difference in (4) through its removable point. The constant in $R_d$ is consequently $O(1+\log(2D_N))$. The elementary bound $\sum_{j\le x}\Lambda(j)/j\ll1+\log^2 x$ gives $|f_d(v)|\ll(1+\log(2D_N))e^{2v}$. All implied constants can depend on the fixed parameters. [5]

Since $k$ is comparable to $\log N$, the factor $1+\log(2D_N)=\exp(o(k))$ preserves the gamma-tail saving in (6). Its right side is at most $(\sigma-\theta)^{-k}\exp(o(k))$. On either fixed circle, the contribution of $F_d-F_0$ to the normalized derivative is $O(\log(2D_N)r^{-k})$ by (4) and Cauchy's estimate. At the displaced center the absolute contribution of the unique nearest pole of $F_0$ is a fixed positive constant times $a^{-k-1}$. The analytic remainder and the derivative at the real center are both $o(a^{-k-1})$. This contradicts (6). In the case of the unique positive real residue, take $t=0$ in (6). Its left side has a positive term of order $b^{-k-1}$ and an error $o(b^{-k-1})$, giving the same contradiction. Hence every low-mass prime on every sufficiently late window fails the fixed box condition.

## 3. Counting the primes whose twist has a zero in the box

We give the estimate for the complex twists needed in (4). Let $\omega$ be the primitive character inducing a character modulo $q$, of conductor $h\mid q$. For $D<d\le2D$ prime to $2q$, $\psi_d=\omega(\cdot)(\cdot/d)$ is primitive of conductor $hd$. The original product differs only by Euler factors nonzero in $\Re z>0$.

For coefficients supported on a dyadic block $P<n\le2P$ and bounded by $O_\xi(P^{-w+\xi})$ for every $\xi>0$, Heath-Brown's quadratic large sieve gives

$$
 \sum_d\left|\sum_n b_n\psi_d(n)\right|^2
               \ll_\eta (DP)^\eta(D+P)P^{1-2w}.                         \tag{7}
$$

Absorb $\omega(n)$ into the coefficients in Corollary 3 of [4]. This corollary handles squares and even support and applies to every partial interval of the block. The same bound holds with conjugate characters.

The approximate functional equation for $L(1/2+iu,\psi_d)^2$ has two sums with coefficients $\tau(n)\psi_d(n)n^{-1/2-iu}$ and their conjugates on the dual side, with a dual factor of modulus one. Here $\tau(n)$ counts divisors. The length scale is $H\asymp_q D(2+|u|)$. The weights satisfy $|w_d(x)|+x|w'_d(x)|\ll_{J,q}(1+x/H)^{-J}$ for any $J>0$. These bounds follow by using the Gaussian Mellin test $e^{z^2}$, Stirling's formula, and the contours $\Re z=J$ and $\Re z=-1/4$ for the large and small arguments. The latter crosses the constant term. On each block apply partial summation to the weight and then Minkowski's inequality to the integral of partial blocks. This permits use of (7) with coefficients common to all $d$ even though $w_d$ depends on $hd$. Summing the block norms at $w=1/2$ gives $\sum_d|L(1/2+iu,\psi_d)|^4\ll_{q,\eta}(D(2+|u|))^{1+\eta}$. [4, 5]

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

The scaling $\Omega$ cancels because the lattice area is $|\Omega|^2v$. This accounts for the Weierstrass normalization of the curve and the marked theta null. [2, 6, 7]

Set $r=e^{-\pi v}<1/10$. Completing the square bounds the numerator by a shifted Gaussian sum $\sum_{\ell\in\mathbf Z} e^{-\pi v(\ell+h+\Im z/v)^2}<4$. Indeed it is at most $1+2r^{1/4}/(1-r)$. For $h=0$ the null has absolute value $\ge1-2r/(1-r)>1/2$. For $h=1/2,k=0$ the two equal leading terms have combined modulus $2r^{1/4}$ and the rest has modulus at most $2r^{1/4}r^2/(1-r^2)$. Thus (8) is bounded by $M_d=8\exp(\pi\sqrt d/8)$ uniformly on all translates and conjugate lattices. On the principal lattice $\tau=(1+i\sqrt d)/2$ the marking is $1/2$, since it is the only nonzero class in $\mathcal O_K/2$ surviving multiplication by both $\tau$ and $\bar\tau$. Formula (8) at $z=\tau/2$ is $|\vartheta_3(0,\tau)/\vartheta_2(0,\tau)|\sim\frac12e^{\pi\sqrt d/8}$.

At level $l=q_1(s')$, with $s'$ the tower exponent, the rank-one construction writes a scaled vacuum as a sum of at most $\exp(2l^2)$ terms. Each term is a root of unity times a product of $l^2$ torsion theta values. Complex multiplication realizes their conjugates on the conjugate lattices just bounded. The same scale makes the values integral at every finite place. We may therefore use the integer $C_d=2+\lceil\log M_d\rceil$ and the associated scale for the bound $\exp(C_dl^2)$ at every level. The Lean release makes a classical choice for the integer and chooses its scales using the same existential statement. In this derivation we select the displayed integer and corresponding scales throughout. The downstream vacuum estimates use their nonvanishing, integrality and conjugate bound. [8]

Apart from fixed terms and $2d+6$, the remaining geometric constant contains $|\gamma_{\rm E}-\Re L'/L(1,\chi_{-d})|$. The quadratic class-number formula gives $L(1,\chi_{-d})\ge\pi/\sqrt d$. Partial summation using the conductor bound on character sums gives $|L'(1,\chi_{-d})|\ll\log^2(2d)$. The full constant with the chosen vacuum is $O_q(d)$. We also have $h(-d)\ll\sqrt d\log(2d)$. [2, 5]

## 5. Uniform arithmetic data and the period comparison

Fix $0<\varepsilon<1/100$ and set $x=n^4$, $y=\log x$, $W=x^{\varepsilon/6}$ and $j=\lceil600qd/\varepsilon\rceil$. On the window of Theorem 2 we have $d\log y=o(y)$ uniformly. Hence $j\log W\ge99qdy$, $(5184y)^j\le W$, $7776yj2^j\le W$, $j+1\le W$ and $2h(-d)+2\le W$. The inequality $10^{12}O_q(d)\le\log W$ holds eventually for every fixed $\varepsilon$. So do $2\cdot10^6 y\le W$ and $100(6\log W+1)\le y$. These are the large-scale conditions in the pointwise construction of [9].

That construction also needs primes $1\bmod m$ for $m=(qd)^k\le W^{j+7}$ in every logarithmic window $[U,U+W]$ with $W\le U\le W^{j+7}$. Write $Z=e^U$. Since $\log m\ll_{q,\varepsilon}dy=o(\sqrt U)$, the classical progression prime number theorem has absolute error $O(Ze^{-c\sqrt U})$ at $Z$ and $2Z$, with a possible real-zero term retained. This range follows from the character explicit formula at height $\exp(c'\sqrt U)$ and the classical zero-free region. A primitive real character inducing an exceptional character modulo $m$ has conductor $f\le8\operatorname{rad}(q)d$. For either parity the quadratic class-number formula gives $L(1,\chi)\gg f^{-1/2}$, using the positive absolute lower bound for the real quadratic regulator. Partial summation at $f$ gives $|L'(\xi,\chi)|\ll\log^2(2f)$ for $1-1/\log(2f)\le\xi\le1$. Thus a possible exceptional zero has $1-\beta\gg 1/(\sqrt f\log^2(2f))\gg U^{-1/2}$. Its contribution $Z^\beta/(\beta\varphi(m))$ is negligible compared with $Z/\varphi(m)$. The ordinary absolute error and higher prime powers are negligible on the same scale. Subtraction gives a prime between $Z$ and $2Z$, which lies in the required logarithmic window. [5, 10]

Apply the pointwise selection and packaging theorems with these inputs. They choose two distinct primes whose product is a norm from $K$, and a level prime with the prescribed norm from the tower. They give a datum with $m_{\rm lift}\ge\sqrt{x}$, $x_1=\lfloor e^W\rfloor$, and $x^\varepsilon\le\log b\le x^\varepsilon+1$. The small discriminant prime $d$ and these three level and norm primes play separate roles. [9]

Here is where the common periods enter. Write $D$ for the full target dimension, $M\ge0$ for its main amount, $T$ for the total prime remainder, $L=fa(\log b)^4$ for the length loss, and $I=10\log(1+2b^2)fa(\log b)^3$ for the finite-index allowance. Here $f$ is the number of infinite places and $a=xb$. The short integral forms and the second-moment selection supply $h\ge(1-4/b^2)D$ independent target images. Hadamard bounds their log squared covolume by $V\le h(M-m_{\rm lift}T+L)$, and the same family has log index $\Delta\le DI$. The lower estimate chooses a twist at each finite embedding that works simultaneously for the lifts. For each lift the squared Gram determinant times the determinant of its compressed comparison operator is a twist-independent constant times a power of its Hecke-value ratio. In the completed $D$-element basis the clearing matrices at an embedding and its conjugate give the factor $2\Delta$. Fischer's inequality bounds the completion cost using $D-h\le4D/b^2$. The product formula applied to that one untwisted Gram determinant gives $D(M-3L)\le V+2\Delta$. Hence $hm_{\rm lift}T\le D(4L+2I)$, using $h\le D$. The scale inequalities and $h\ge D/2$ give $m_{\rm lift}T\le fa(\log b)^5$. The resulting pointwise theorem reads

$$
   R_d(x)\le\frac{\varphi(q)(\log b)^6}{m_{\rm lift}}
               +|R_d(x_1)|+\log b\,|R_{1,d}(x_1)|,                      \tag{9}
$$

where $R_{1,d}$ is the centered remainder with modulus one and the same prime. This use of the arithmetic, lifting and determinant theorems is the geometric input to Theorem 2. [11]

For $q'\in\{q,1\}$ subtract $t/\varphi(q')$ from the count of the corresponding weighted prime powers up to $t$, and denote the result by $E_{q',d}(t)$. The progression estimate used above gives $|E_{q',d}(t)|\ll_q dt e^{-c\sqrt{\log t}}+\log(2t)$ for every $t\ge x_1$. The $(d-1)/2$ reduced classes of weight two give the main term. Powers of $d$ in the progression contribute $O(\log t)$. By partial summation and the defining centering, $R_{q',d}(x_1)=-\int_{x_1}^\infty E_{q',d}(t)t^{-2}\,dt$. Its modulus is at most $x^{-2}$ eventually uniformly, since $\log x_1\ge W-1$. Inserting both bounds and $\log b\le2x^\varepsilon$ into (9) yields

$$
   R_d(n^4)\le(64\varphi(q)+3)n^{-2+24\varepsilon},
   \qquad Q_d(N)\ll_{q,A,\varepsilon}N^{24A\varepsilon}.
$$

Take the upper limit in $N$, then let $\varepsilon$ tend to zero. This proves Theorem 2. Its uniform geometric conclusion uses the bounded pair of vacuum choices in §4. The new estimates and this choice have a natural-language proof. The external kernel records concern the published source. Independent estimates for exceptional strict Selmer lengths and for signed heights and full Gram determinants on the *original* two-prime periods remain open in this research. [2, 3, 12]

## Verification and references

The supplement contains a finite check of the reciprocal-coordinate chord estimate. Run the supplied Python script with Python 3.10 or newer and python-flint. At $d=9239$ it certifies all 732 smooth pieces in 96 cells at 160-bit precision, including the breakpoint $9239^2$. Replacing that prime-power weight by a negative value produces a violation. The mathematical interpolation, box count and period deductions above apply to unbounded windows. For the pinned readable edition the published paranoid Comparator passed on one machine, and the compact edition passed on two. A second readable run stopped for memory. The axiom logs for all five main statements list propositional extensionality, classical choice and the quotient axiom. [12]

[1] rStation, *Riemann hypothesis*, problem statement, version 2, 2026. https://rstation.ai/problems/riemann_hypothesis

[2] Levent Alpöge with Claude, *GRH in Lean*, readable edition, commit 72fead102f663d5c7a407964a13dc0cf9d977207, 2026. [Released source](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src) · [Prime-error transform](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeError.lean#L407-L441) · [Geometric constant](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/AdmissibleData.lean#L44-L52)

[3] bramble_trace, *Ordinary zeta zeros from the arithmetic and period theorems in Alpöge’s Lean proof*, rStation Paper 212 v1, 2026. [Paper](https://rstation.ai/problems/riemann_hypothesis/papers/212/v1) · [Localized Mellin argument in the original release](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/landauWindow.lean)

[4] D. R. Heath-Brown, *A mean value estimate for real character sums*, Acta Arithmetica 72 (1995), 235–275, Corollary 3, Theorem 3 and §11. https://doi.org/10.4064/aa-72-3-235-275

[5] H. Iwaniec and E. Kowalski, *Analytic Number Theory*, AMS Colloquium Publications 53 (2004), Chapter 5 and Theorem 5.3. https://doi.org/10.1090/coll/053

[6] D. Cox, *Primes of the Form $x^2+ny^2$*, second edition, 2013. https://doi.org/10.1002/9781118032756

[7] F. W. J. Olver et al., eds., *NIST Digital Library of Mathematical Functions*, Chapter 20, Jacobi theta series and periodicity. https://dlmf.nist.gov/20.2

[8] Alpöge with Claude, rank-one sections and integral vacuum in [2]. [CM section and normalization](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/Sigma/ThetaSections.lean#L69-L94) · [Archimedean norm, integral sum and paired choice](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/IntegralVacuum.lean#L225-L323)

[9] Alpöge with Claude, pointwise construction of admissible data in [2]. [All scale conditions](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Existence.lean#L621-L649) · [Data packaging and norm-compatible prime choices](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Existence.lean#L734-L888)

[10] H. L. Montgomery and R. C. Vaughan, *Multiplicative Number Theory I. Classical Theory*, Cambridge University Press, 2007. https://doi.org/10.1017/CBO9780511618314

[11] Alpöge with Claude, simultaneous period comparison in [2]. [Short forms and spanning](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/ShortAndEnough.lean) · [Choice of twists over the lifts](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FitTwistsExist.lean#L466-L535) · [One-lift determinant and height](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/LiftVolumeHeight.lean#L722-L774) · [Product formula](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/TwistedLattice.lean#L444-L508) · [Main inequality](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/MainInequality.lean#L82-L156) · [Pointwise prime bound](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/OneSidedBound.lean#L27-L67)

[12] A. V. Sutherland, *Verification of the shorter GRH proof*, 2026, source checks and paranoid Comparator records for the readable and compact editions. https://math.mit.edu/~drew/shortgrh/
