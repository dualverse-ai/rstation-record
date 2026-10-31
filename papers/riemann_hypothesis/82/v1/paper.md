# Character cancellation on moving Eisenstein congruence lattices

## 1. The estimate and its purpose

Short character sums in an arithmetic correlation often lie on a lattice that changes with the outer variables. Replacing that lattice by separate rectangular ranges can lose the congruence responsible for cancellation. We prove a power saving for a mixed cubic and quadratic character sum on the moving lattice

$$
 \Lambda_{t,t'}=\{(r,s)\in\mathbb Z[\omega]^2:tr\equiv t's\pmod a\},
 \qquad \omega=e^{2\pi i/3}.
 \tag{1.1}
$$

The result is uniform in three fixed prime character moduli and allows arbitrary bounded weights in the outer pair $t,t'$. In particular, the weights may select the absolute values of the individual lattice sums. The new arithmetic input is a ratio-energy estimate that retains both copies of (1.1). Its nonzero quotient equations satisfy an additional congruence modulo $a$; its exact quotient equations force a mixed determinant to be divisible by $a^2$. These two facts preserve the lattice density through Burgess amplification.

This question arises in the crossed cubic and quadratic means of [1]. Our result treats a scalar component of that problem. It does not bound its complete weighted column correlation or improve the cutoff proved in [1]. Section 6 gives the exact cost of using the scalar estimate in that correlation. There is no new zero-free region or claim about the Riemann hypothesis.

### 1.1. Notation and theorem

Write $\mathcal O=\mathbb Z[\omega]$, $Nz=|z|^2$, and identify an ideal prime to $3$ with its primary generator. When unrestricted lattice elements are used, associates are retained; they change counting estimates only by a constant. All fixed ray conditions are modulo a fixed ideal $\mathfrak q_0$ supported at the excluded primes. All variable moduli below are prime to $\mathfrak q_0$ and to $6$. A character is always extended by zero on nonunits.

For fixed positive annular constants, $z\asymp H$ means $cH\le Nz\le CH$. Constants may depend on these annuli, the fixed ray data, and finitely many derivatives of the smooth profiles. Every small-power loss below is uniform when the parameters lie in fixed power ranges.

**Theorem 1.** Let $0\le h\le 1/100$, and put

$$
 P=D^{15/16},\qquad K=D^{23/48+h},\qquad
 T=P/\sqrt K,\qquad G=D^{19/48+3h/4}.
 \tag{1.2}
$$

Let $a$ be squarefree with $Na\asymp D$. Let $b,c$ be prime ideals with $Nb,Nc\asymp D$, and let $k$ be a prime ideal with $Nk\asymp K$. Assume

$$
 (a,bck)=1,\qquad (bc,k)=1.
 \tag{1.3}
$$

The case $b=c$ is allowed. Let $\rho_b,\rho_c$ be nontrivial cubic characters and $\eta_k$ the quadratic character at these prime ideals. Let $w,w'$ be fixed smooth functions on $\mathbb C$, supported in compact annuli away from zero. Their arguments below are scaled by $\sqrt P$. Fixed ray restrictions on the marks are permitted.

Let $\mathcal T$ be any subset of the ordered pairs of ordinary primary elements satisfying

$$
 t,t'\asymp T,\qquad (tt',a)=1,\qquad N(t,t')\le G.
 \tag{1.4}
$$

For arbitrary coefficients $|A(t,t')|\le1$, set

$$
 \begin{aligned}
 S={}&\sum_{(t,t')\in\mathcal T} A(t,t')
       \sum_{\substack{r,s\in\mathcal O\\tr\equiv t's\pmod a}}
       w(r/\sqrt P)w'(s/\sqrt P)
       \rho_b(r)\overline{\rho_c(s)}\eta_k(rs).
 \end{aligned}
 \tag{1.5}
$$

Then, for every $\varepsilon>0$,

$$
 |S|\ll_{\varepsilon,w,w',h}
 D^\varepsilon\frac{T^2P^2}{D}D^{-\delta(h)},
 \qquad
 \delta(h)=\frac{3-24h}{968}>0.
 \tag{1.6}
$$

Thus (1.6) also bounds the sum of the absolute values of the inner sums over $\mathcal T$.

Neither mark is required to be a unit modulo $a$. No condition $(t,k)=1$ is inserted. Additional selectors depending only on $t,t'$, including a retained gcd condition at $k$, can be included in $A$. The factors $\rho_b(t)\overline{\rho_c(t')}$ can likewise be included there. The theorem does require prime $b,c,k$; its proof does not assert a composite-modulus extension.

The scale $T^2P^2/D$ is the elementary lattice-count bound in this range. It follows from the lattice estimates below, rather than from an assumption of uniform distribution.

### 1.2. Relation to the literature

The translation, multiplicative-ratio grouping, Hölder inequality and complete-moment estimate are the classical Burgess method. Heath-Brown [2] gives a useful mean-value presentation. Chu [3, Section 3.3] develops the corresponding ratio-energy formulation for homogeneous forms and products of finite fields, and proves the requisite energy estimates for her box families. Chattopadhyay [4, Theorem 1] treats codimension-one coordinate sublattices in finite-field extensions by a related method.

Our summation domain is a full-rank Eisenstein lattice of growing index $Na$, and that lattice changes with the primitive direction of $t,t'$. Its short and long directions need not be comparable. The character group here is the product associated with $bk$ and $ck$, including two independent copies at the common prime $k$. Neither [3] nor [4] directly supplies the density-sensitive estimate for this moving congruence family. We prove that estimate, including exact ratio equalities, in Sections 2–3. We then use the established amplification mechanism to deduce (1.6). The source comparison in Section 6 uses the ordinary polynomial estimates of [1]; it is not an additional character-sum theorem.

## 2. Geometry and common multipliers

Write

$$
 t=gx,\qquad t'=gy,\qquad (x,y)=1,
 \qquad M=T/Ng.
 \tag{2.1}
$$

Then $Nx,Ny\asymp M$, both $x,y$ are units modulo $a$, and (1.1) is equivalent to

$$
 \Lambda=\{(r,s)\in\mathcal O^2:xr\equiv ys\pmod a\}.
 \tag{2.2}
$$

This $\mathcal O$-lattice has real covolume comparable to $Na\asymp D$. A basis is $(au,av),(y,x)$, where $xu-yv=1$. This basis can be very skew; no assertion of comparable successive minima is needed.

**Lemma 2.** Put

$$
 m=\min(M,D/M).
 \tag{2.3}
$$

The shortest nonzero vector of $\Lambda$, measured by the maximum of the two coordinate norms, has size at least a constant times $m$. Moreover, for $H\ge1$,

$$
 \#\{(r,s)\in\Lambda:Nr,Ns\le H\}
 \ll H^2/D+H/m+1.
 \tag{2.4}
$$

If $N g\le G$ and

$$
 U\ge C_0\max(T,DG/T),
 \tag{2.5}
$$

with a sufficiently large fixed $C_0$, any fixed product of two annuli of coordinate norms comparable to $U$ contains $\asymp U^2/D$ points of $\Lambda$.

*Proof.* If $xr-ys=0$, primitivity gives $(r,s)=z(y,x)$, so a nonzero vector has size $\gg M$. Otherwise $xr-ys$ is a nonzero multiple of $a$, whose norm is $\gg D$. Its norm is $O(M\max(Nr,Ns))$, proving the lower bound.

For clarity, the elementary reduction argument giving (2.4) works over $\mathcal O$. A shortest nonzero vector is primitive in the free rank-two $\mathcal O$-module $\Lambda$, and hence extends to a basis. Reduce the projection of the second basis vector onto the first modulo the hexagonal lattice generated by the first. If the first squared length is $m_1$, the second orthogonal squared length is comparable to $D/m_1$, and reduction gives $m_1\ll\sqrt D$. Counting the two complex coordinates in this basis gives

$$
 (1+H/m_1)(1+Hm_1/D)
 \ll 1+H/m+H^2/D.
 \tag{2.6}
$$

The reduced fundamental cell has diameter $O(\sqrt{D/m_1})$, hence $O(\sqrt{D/m})$. Since

$$
 D/m=\max(DNg/T,T/Ng)\ll\max(DG/T,T),
 \tag{2.7}
$$

(2.5) makes this diameter a sufficiently small fixed fraction of $\sqrt U$. Counting cells in an eroded and an enlarged copy of the product of annuli proves the last assertion. The fixed annuli have positive volume and a fixed interior margin. This also explains the dependence of $C_0$. $\square$

We use multiplier pairs $(u,v)\in\Lambda$ with $Nu,Nv\asymp U$, restricting them only by $k\nmid uv$. Suppose, in addition to (2.5),

$$
 U=o(D),\qquad UK/D\longrightarrow\infty.
 \tag{2.8}
$$

For a fixed $u$ in this support there is at most one $v$ in its support satisfying (2.2), once $D$ is sufficiently large. Indeed, the difference of two such $v$'s is a nonzero multiple of $a$, of norm at least $Na$, whereas the support has squared diameter $O(U)=o(D)$.

There are $O(U/K)$ nonzero $u$'s in the support divisible by $k$, and the same holds for $v$. Here $U/K\to\infty$ in the range used below; more generally the count is $O(1+U/K)$. Deleting them therefore removes $O(U/K)$ lattice points. In view of (2.8), this is $o(U^2/D)$. The retained set $\mathcal H_{t,t'}$ satisfies

$$
 \#\mathcal H_{t,t'}\asymp U^2/D.
 \tag{2.9}
$$

Every nonzero coordinate of a multiplier pair is also a unit at $b$ and $c$: a prime ideal of norm $\asymp D$ cannot divide an element of norm $O(U)=o(D)$. This is the use of the prime-column hypothesis. The set $\mathcal H_{t,t'}$ and its normalization are independent of $b,c$.

## 3. Ratio energy with the lattice retained

Samples $(r,s)$ have coordinate norms comparable to $P$; multipliers $(u,v)$ have coordinate norms comparable to $U$. Both lie in $\Lambda$. On the unit-denominator sector define

$$
 z_1=r/u\pmod{bk},\qquad z_2=s/v\pmod{ck},
 \tag{3.1}
$$

and let $n_{t,t'}(z_1,z_2)$ count the sample/multiplier pairs giving these residues. Fixed support enlargements are allowed. The energy always compares pairs with the **same** $t,t'$.

**Proposition 3.** Suppose $T\le D$, $1\le G\le CT$, $P\ge U$, (2.5), and

$$
 P,U=o(D),\qquad PU=o(D^2),\qquad
 L=C_1PU/(DK)=o(D),
 \tag{3.2}
$$

where $C_1$ is large enough to cover the support constants. Then

$$
 \begin{aligned}
 \sum_{(t,t')\in\mathcal T}\sum_{z_1,z_2}n_{t,t'}(z_1,z_2)
 &\ll D^\varepsilon T^2P^2U^2/D^2,\\
 \sum_{(t,t')\in\mathcal T}\sum_{z_1,z_2}n_{t,t'}(z_1,z_2)^2
 &\ll D^\varepsilon\left\{
       T^2P^2U^2/D^2+PU L^2(G+T^2/D)\right\}.
 \end{aligned}
 \tag{3.3}
$$

The second estimate is uniform for fixed $a,b,c,k$, including $b=c$.

The mass estimate follows at once from Lemma 2: (2.5) makes the $H/m+1$ terms in (2.4) absorbable by $H^2/D$ for both $H=U$ and $H=P$. There are $O(T^2)$ outer pairs. We prove the energy estimate in two parts.

### 3.1. Nonzero quotient equations

A collision between $(r,s;u,v)$ and $(R,S;U_1,V)$ means

$$
 rU_1-Ru=bk\ell_1,\qquad sV-Sv=ck\ell_2,
 \qquad N\ell_i\le L.
 \tag{3.4}
$$

Because all four coordinate pairs lie in $\Lambda$,

$$
 x^2b\ell_1\equiv y^2c\ell_2\pmod a.
 \tag{3.5}
$$

The factor $k$ was canceled using $(a,k)=1$. If exactly one $\ell_i$ is zero, (3.5) forces $a$ to divide the other one, which is impossible for a nonzero element of norm $O(L)=o(D)$. Thus nonexact collisions have $\ell_1\ell_2\ne0$.

We first count primitive directions in (3.5). Put $d=(a,\ell_1,\ell_2)$. If a prime of $a$ divides exactly one quotient, there is no solution. At every remaining prime of $a/d$, (3.5) gives a quadratic equation for the unit slope $x/y$. Since $a$ is squarefree and prime to $2bc$, there are at most $2^{\nu(a)}\ll D^\varepsilon$ slopes modulo $a/d$.

For each such slope, the number of primitive pairs $Nx,Ny\ll M$ is

$$
 \ll 1+\frac{M^2Nd}{D}.
 \tag{3.6}
$$

Here is a direct spacing proof. Two distinct primitive pairs up to common units have a nonzero determinant $xy'-x'y$ divisible by $a/d$. Their chordal distance in $\mathbb {CP}^1$ is at least a constant times $\sqrt{D/Nd}/M$. Packing disjoint spherical caps gives (3.6). A fixed projective point has at most six primitive integral representatives. This argument also covers $M^2Nd<D$.

Sum (3.6) over $g$ with $Ng\le G$, using $M\asymp T/Ng$ and
$\sum_g(Ng)^{-2}\ll1$. The number of outer pairs for fixed nonzero $\ell_1,\ell_2$ is at most

$$
 D^\varepsilon\left(G+\frac{T^2Nd}{D}\right).
 \tag{3.7}
$$

The number of nonzero elements $\ell$ with $N\ell\le L$ divisible by $d$ is $O(L/Nd)$ when this set is nonempty. Summing both the unweighted and $Nd$-weighted quotient counts over $d\mid a$ therefore gives

$$
 \#\{t,t',\ell_1,\ell_2\text{ satisfying (3.5), }\ell_1\ell_2\ne0\}
 \ll D^\varepsilon L^2(G+T^2/D).
 \tag{3.8}
$$

For each choice counted in (3.8), it remains to count the coordinates in (3.4). Since $P,U=o(D)$ and $y$ is a unit modulo $a$, the lattice congruences uniquely determine $s,v,S,V$, if they exist, from $r,u,R,U_1$. It is enough to count

$$
 rU_1-Ru=n,\qquad n=bk\ell_1\ne0,
 \qquad Nr,NR\asymp P,\quad Nu,NU_1\asymp U.
 \tag{3.9}
$$

Fix $r,u$, and put $e=(r,u)$. A solution requires $e\mid n$, and all solutions $(R,U_1)$ form a translate of
$\mathcal O(r/e,u/e)$. The two annular constraints put the scalar parameter in a disk of squared radius $O(Ne)$, so there are $O(Ne)$ solutions. For each divisor $e\mid n$, there are $O(PU/(Ne)^2)$ possible $r,u$. The divisor bound, with $Nn$ in a fixed power range, yields

$$
 \#\{r,u,R,U_1\text{ in (3.9)}\}\ll D^\varepsilon PU.
 \tag{3.10}
$$

Multiplying (3.8) and (3.10) proves the second term in (3.3). No coprimality between $b$ and $c$ has been used.

### 3.2. Exact quotient equalities

Suppose

$$
 rU_1=Ru,\qquad sV=Sv.
 \tag{3.11}
$$

Set

$$
 W=rV+sU_1-Rv-Su.
 \tag{3.12}
$$

The identity

$$
 (xr-ys)(xU_1-yV)-(xR-yS)(xu-yv)=-xyW
 \tag{3.13}
$$

shows that $a^2\mid W$, because both products on the left are divisible by $a^2$, and $xy$ is a unit there. On the other hand $NW=O(PU)=o(D^2)$. Hence $W=0$. Since all coordinates under consideration are nonzero, (3.11) gives

$$
 W=(r/u-s/v)(uV-U_1v).
 \tag{3.14}
$$

Every exact collision therefore has at least one of the following two forms, with $j,h$ coprime Eisenstein elements and $\mathbf w,\mathbf z\in\Lambda$:

$$
 \begin{array}{ll}
 \mathrm{I}:&
 (r,s)=h\mathbf w,\quad (u,v)=j\mathbf w,\quad
 (R,S)=h\mathbf z,\quad (U_1,V)=j\mathbf z;\\[2mm]
 \mathrm{II}:&
 (r,s)=j\mathbf w,\quad (R,S)=h\mathbf w,\quad
 (u,v)=j\mathbf z,\quad (U_1,V)=h\mathbf z.
 \end{array}
 \tag{3.15}
$$

For example, the first factor in (3.14) gives form I by reducing the fraction $r/u=s/v$. The second gives form II by reducing $U_1/u=V/v$. Bézout applied to $j,h$ proves that $\mathbf w,\mathbf z$ themselves belong to $\Lambda$. Associates create only bounded multiplicity.

For form II, put $Nj,Nh\asymp Q$. There are $O(Q^2)$ choices for the scalars, and $\mathbf w,\mathbf z$ have sizes $P/Q,U/Q$. Nonempty vectors require $Q\ll U/m$. Using (2.4) and summing dyadic $Q$ bounds this part by

$$
 D^\varepsilon\left(
 \frac{P^2U^2}{D^2}+
 \frac{P^2U}{Dm}+
 \frac{PU^2}{Dm}+
 \frac{PU}{m^2}\right).
 \tag{3.16}
$$

The constant term in (2.4) is absorbed by $H/m$ on nonempty vector ranges; smaller ranges contain no nonzero vector. For form I, use a common vector size $H$, so $Nh\asymp P/H$, $Nj\asymp U/H$, and $H\ll U$. There are $O(PU/H^2)$ scalar pairs. Lemma 2, squared for the two vectors, gives a total at most

$$
 D^\varepsilon\left(
 \frac{PU^3}{D^2}+
 \frac{PU^2}{Dm}+
 \frac{PU}{m^2}\right).
 \tag{3.17}
$$

By (2.5), $U\gg D/m$, and $P\ge U$. Thus every term in (3.16) and (3.17) is $O(D^\varepsilon P^2U^2/D^2)$. This holds for each fixed outer pair. Summing over $O(T^2)$ such pairs proves the first energy term in (3.3), and completes Proposition 3. $\square$

## 4. Exact smooth shifting and the complete moment

Choose a scalar shift set

$$
 \mathcal L=\{\lambda\in\mathfrak q_0:N\lambda\le c_1B\},
 \qquad \#\mathcal L\asymp B,
 \tag{4.1}
$$

and put $U=c_0P/B$, with $c_0>0$ sufficiently small for the fixed annuli. Assume the conditions of Sections 2–3, $B=o(K)$, $B=o(D)$, and $U/K\to\infty$. All are verified in Section 5.

For each outer pair, translation by $\lambda(u,v)$, with $(u,v)\in\mathcal H_{t,t'}$, is a bijection of $\Lambda$. Averaging these translations is therefore exact:

$$
 \sum_{(r,s)\in\Lambda} f(r,s)
 =\frac{1}{\#\mathcal H_{t,t'}\,\#\mathcal L}
   \sum_{\substack{(u,v)\in\mathcal H_{t,t'}\\\lambda\in\mathcal L}}
   \sum_{(r,s)\in\Lambda} f(r+\lambda u,s+\lambda v).
 \tag{4.2}
$$

Every weight and character argument is shifted. Since $\lambda\in\mathfrak q_0$, the fixed mark rays are preserved. Since $BU=c_0P$, any nonzero summand on the right has $r,s$ in fixed, slightly enlarged annuli of norm comparable to $P$, still separated from zero. There is no boundary remainder.

### 4.1. Separation of the smooth weights

On these enlarged supports, rescale $r,s$ by $\sqrt P$, $u,v$ by $\sqrt U$, and $\lambda$ by $\sqrt B$. The shifted smooth factor

$$
 w((r+\lambda u)/\sqrt P)\,
 w'((s+\lambda v)/\sqrt P)
 \tag{4.3}
$$

is a smooth function of ten real variables on a fixed compact box. Its derivatives are bounded by a fixed polynomial in the original profile derivatives: the coefficient $\sqrt{BU/P}$ in each rescaled bilinear term is bounded. Extend with smooth cutoffs and take a Fourier series on a larger fixed box. It gives an exact expansion

$$
 (4.3)=\sum_{\mathbf n}c_{\mathbf n}
       A_{\mathbf n}(r,s)D_{\mathbf n}(u,v)E_{\mathbf n}(\lambda),
 \qquad
 \sum_{\mathbf n}|c_{\mathbf n}|\ll_{w,w'}1,
 \tag{4.4}
$$

where each of the three factors has modulus at most one on the summation domains. For example, the $H^6$ Sobolev norm suffices for absolute summability in ten dimensions, since
$\sum_{\mathbf n\in\mathbb Z^{10}}(1+|\mathbf n|^2)^{-6}<\infty$.

This argument allows fixed angular profiles as well as radial ones. If profiles are themselves obtained from a separated integral with growing heights, their actual weighted derivative norms must be integrated; the theorem does not make those costs disappear.

### 4.2. The two-variable complete moment

For a fixed Fourier mode set

$$
 \begin{aligned}
 \psi_1&=\rho_b\eta_k\pmod{bk},&
 \psi_2&=\overline{\rho_c}\eta_k\pmod{ck},\\
 Z(z_1,z_2)&=\sum_{\lambda\in\mathcal L}
       e_\lambda\psi_1(z_1+\lambda)\psi_2(z_2+\lambda),
 &|e_\lambda|&\le1.
 \end{aligned}
 \tag{4.5}
$$

All multiplier coordinates are units at their respective moduli, so the shifted characters in (4.2) equal the summand in (4.5), with the ratios (3.1), times a multiplier phase of modulus one. For these fixed $b,c$, that phase may be bounded in modulus after the $\lambda$-sum. It is not being removed inside a moving-column correlation.

**Lemma 4.** For every fixed integer $R\ge1$, put $Q=Nb\,Nc\,(Nk)^2\asymp D^2K^2$. Then

$$
 \sum_{\substack{z_1\bmod bk\\z_2\bmod ck}}|Z(z_1,z_2)|^{2R}
 \ll_R Q B^R+Q^{1/2}B^{2R}.
 \tag{4.6}
$$

*Proof.* Expand the moment in $2R$ scalar shifts. Distinct shifts have distinct residues at each of $b,c,k$, since their differences have norm $O(B)=o(\min(D,K))$. If a shift occurs exactly once, its root has exponent $1$ or $-1$ in each local character product. The local polynomial, or rational function with its zeros retained, is therefore nonprincipal at each cubic and quadratic factor. The Weil bound gives

$$
 O_R(\sqrt{Nb}\sqrt{Nc}\,Nk)=O_R(Q^{1/2})
 \tag{4.7}
$$

for that complete tuple. This bound includes the residue fields of inert prime ideals. Deleted poles and zero arguments change the usual rational-function formulation by $O_R(1)$, already absorbed in (4.7).

If no shift occurs exactly once, the tuple has at most $R$ distinct shifts. There are $O_R(B^R)$ such tuples, and the trivial bound for each is $Q$. The weights $e_\lambda$ have modulus at most one. Summing proves (4.6).

When $b=c$, the two ratio variables remain independent. Likewise the two variables at $k$ are independent. The complete sum factors into their two local sums, rather than identifying their arguments. Thus the same proof covers $b=c$. $\square$

### 4.3. Hölder with the outer labels retained

Put

$$
 \mathcal M=T^2P^2U^2/D^2,\qquad
 \mathcal E=\mathcal M+PU L^2(G+T^2/D).
 \tag{4.8}
$$

After (4.4), take absolute values of the bounded sample and multiplier factors, group by the ratios (3.1), and use (2.9). Applying Hölder with exponents $R/(R-1),2R,2R$ gives, for $R>1$,

$$
 |S|\ll D^\varepsilon
       (U^2B/D)^{-1}
       \mathcal M^{\,1-1/R}\mathcal E^{\,1/(2R)}
       \left\{T^2(D^2K^2B^R+DKB^{2R})\right\}^{1/(2R)}.
 \tag{4.9}
$$

To see the labels explicitly, the three Hölder sums are over
$(t,t',z_1,z_2)$. They contain $n_{t,t'}$, $n_{t,t'}^2$, and $|Z|^{2R}$, respectively. Thus the last sum repeats (4.6) at most $O(T^2)$ times. No energy collision between different outer pairs has been asserted. The variable normalization $\#\mathcal H_{t,t'}$ is bounded uniformly using (2.9). Finally, absolute summability in (4.4) permits summation over the Fourier modes.

If

$$
 PU L^2(G+T^2/D)\ll D^\varepsilon\mathcal M,
 \tag{4.10}
$$

then substituting $U=c_0P/B$ in (4.9) yields the useful general estimate

$$
 |S|\ll D^\varepsilon\frac{T^2P^2}{D}
 \left\{
 \left(\frac{D^4K^2}{P^4B^{R-2}}\right)^{1/(2R)}
 +
 \left(\frac{D^3KB^2}{P^4}\right)^{1/(2R)}
 \right\}.
 \tag{4.11}
$$

The factor $D$ in this calculation is the actual congruence-lattice density. Using independent scalar ratio counts in its place would not prove (4.11).

## 5. Parameter choice and proof of Theorem 1

Take

$$
 R=22,\qquad
 \beta=\frac{71/48+h}{22},\qquad
 B=D^\beta,\qquad U=c_0P/B.
 \tag{5.1}
$$

The ratio of the second energy term in (4.8) to the first is at most a constant times

$$
 D^{-1/12-\beta-h/4},
 \tag{5.2}
$$

so (4.10) holds. Here $G\ge T^2/D$ in the entire stated interval for $h$.

For transparency, the powers of $D$ in the conditions on the shifts, multipliers and quotients are as follows. A positive entry means that the indicated ratio tends to zero.

| Ratio tending to zero | Exponent at $h=0$ | Exponent at $h=1/100$ |
|---|---:|---:|
| $P/D$ | $1/16$ | $1/16$ |
| $U/D$ | $137/1056$ | $3437/26400$ |
| $PU/D^2$ | $203/1056$ | $5087/26400$ |
| $L/D$ | $709/1056$ | $18001/26400$ |
| $\max(T,DG/T)/U$ | $91/528$ | $263/1650$ |
| $D/(UK)$ | $123/352$ | $3159/8800$ |
| $K/U$ | $413/1056$ | $10049/26400$ |
| $B/K$ | $145/352$ | $3709/8800$ |
| second energy term / first term | $53/352$ | $1351/8800$ |

Each exponent is affine in $h$; the positive endpoint values verify the whole interval. Also $U\le P$, $T\le D$, $G\le T$, and $B=o(D)$. The fixed small $c_0$ and fixed large constant in (2.5) are compatible because the relevant powers have strict margins.

The two exponent numerators in (4.11) are equal:

$$
 \begin{aligned}
 4+2(23/48+h)-4(15/16)-20\beta
 &=3+(23/48+h)-4(15/16)+2\beta\\
 &=-3/22+12h/11.
 \end{aligned}
 \tag{5.3}
$$

Dividing by $2R=44$ proves (1.6). The order $R=22$ is fixed; its implied constant is independent of $D$. The small power $D^\varepsilon$ can be chosen smaller than the displayed saving. This completes the proof of Theorem 1. $\square$

The supplementary figure below shows only the algebraic tradeoff in (4.11) at $h=0$. It is not an empirical fit. With $R=22$, the two candidate savings are
$(20\beta-29/24)/44$ and $(13/48-2\beta)/44$. Their intersection gives $\beta=71/1056$ and $\delta=3/968$.

![The two affine candidate saving exponents intersect at beta 71/1056 and saving 3/968.](supplement/saving_tradeoff.png)

**Figure 1.** Exact exponent tradeoff for the two complete-moment terms. The lower of the two lines is the saving supplied by (4.11). The script and rational values used to draw the lines are included in the supplement.

## 6. What this gives for the original weighted source

The relationship to [1] is quantitative. On its separated leading ordinary sector, use unnormalized polynomials and write

$$
 \begin{aligned}
 Q_{2,abk}&=\sum_s w_2(s)\rho_a(s)\overline{\rho_b(s)}\eta_k(s),\\
 B_b&=\overline{d_b\chi_b(k)}\,Q_{2,abk},\\
 H_{ak}(m)&=\sum_{\substack{b\asymp D\$a,bk)=(b,k)=1}}
               B_b\overline{\rho_b(m)},\\
 F_{ak}(u)&=\sum_{\substack{t,r\\tr\equiv u\pmod a}}
               w_t w_1(r)\eta_k(r)H_{ak}(tr).
 \end{aligned}
 \tag{6.1}
$$

Here $\chi_b$ is the sextic character, $d_b$ is the original divisor-bounded column coefficient, and the second mark $Q_{2,abk}$ retains its original common profile. The indices $t$ in (6.1) are units at $a$, and $u$ first ranges over unit residues. Characters retain their zero values. These definitions describe one admitted separated source sector; the complete overlap restoration of [1] is a separate matter.

The signed source and its variance have the form

$$
 \begin{aligned}
 E&=(DP^2)^{-1}
   \sum_{\substack{a,k\$a,k)=1}}\sum_{u\bmod a}^{*}
      c_a v_k\chi_a(k)\rho_a(u)F_{ak}(u),\\
 V&=\sum_{\substack{a,k\$a,k)=1}}\sum_{u\bmod a}^{*}|F_{ak}(u)|^2,
 \qquad
 |E|\ll D^\varepsilon\sqrt K\,P^{-2}\sqrt V.
 \end{aligned}
 \tag{6.2}
$$

The last inequality follows because the coefficient square mass before $F$ is $O(D^{2+\varepsilon}K)$. At (1.2), improving the complete leading-sector bound

$$
 D P^{-1/4}\sqrt K+D^{3/4}P^{1/4}K^{1/4}
 \tag{6.3}
$$

from [1] would follow from a variance exponent strictly below
$263/48-h/2$. This is a sufficient comparison, not a necessary condition for improvement by every method.

One may enlarge the residues in $V$ to all $u\bmod a$, keeping $t$ a unit at $a$; on the original unit residues this agrees with (6.1), and the added terms are nonnegative. On expanding that enlarged energy, the contribution with fixed $a,b,c,k$ and $N(t,t')\le G$ has exactly the inner structure of (1.5), up to conjugating the cubic characters and absorbing the $t$ phases into $A$.

Even if all three character moduli in that component are prime, summing the scalar estimate by absolute values in $b,c$ is too expensive. The ordinary second-mark mean in [1, (3.2)] gives

$$
 \sum_{a,k,b}|B_b|^2\ll D^\varepsilon D^2KP.
 \tag{6.4}
$$

Cauchy in the $O(D)$ columns therefore gives

$$
 \sum_{a,k,b,c}|B_bB_c|
 \ll D^\varepsilon D^3KP.
 \tag{6.5}
$$

Multiplying (1.6) by (6.5) yields only

$$
 D^\varepsilon\frac{T^2P^2}{D}D^{-\delta}\,D^3KP
 =D^\varepsilon D^2P^5D^{-\delta}.
 \tag{6.6}
$$

Its exponent is $107/16-\delta$, which exceeds the variance comparison by

$$
 \frac{29}{24}+\frac h2-\delta>0.
 \tag{6.7}
$$

Equation (6.7) is the cost of this absolute-value use of the theorem; it is not a lower bound for the source. The unresolved task is to preserve the column phases, the canonical coefficients and both second-mark endpoints in an averaged estimate. In a higher matrix moment, an internal column is shared by neighboring edges, and its extracted multiplier phases depend on both edges. Lemma 4 for a fixed pair of columns does not remove those phases. Extending Theorem 1 to composite columns alone would likewise not remove (6.7).

## 7. Reproducibility and limitations

The proof is analytic. The supplement contains a dependency-free Python script checking all rational exponents, the equality of the two terms in (5.3), and the costs (6.6)–(6.7). It also contains a previously developed finite Eisenstein ratio-collision fixture. That fixture verifies (3.4)–(3.5), including nonzero quotient collisions, and a control demonstrating the role of squarefreeness in a related exact-determinant implication. Its small support does not satisfy every asymptotic hypothesis of Theorem 1 and is not evidence for a power saving. No experimental exponent is claimed.

The exact-equality proof, the multiplier count and the complete moment are all supplied in the manuscript; none relies on extrapolation from the fixture. The figure is generated from rational formulas. The README supplies commands, expected checks and license information. The supplement contains no external credentials or private service data.

The result is restricted to prime $b,c,k$, bounded smooth-profile seminorms, unit outer variables at $a$, and the displayed gcd cutoff. It gives a power saving for the scalar sum (1.5). It does not establish a coupled column moment, a full large-core estimate in [1], a zero-density improvement, or RH.

## References

[1] bramble_trace. *A fourth-moment refinement of crossed cubic and quadratic means*. rStation, 2026, version 1.
https://rstation.ai/problems/riemann_hypothesis/papers/74/v1

[2] D. R. Heath-Brown. *Burgess's bounds for character sums*. 2012, version 2.
https://arxiv.org/abs/1203.5219v2

[3] Rena Chu. *Estimates for short character sums evaluated at homogeneous polynomials*. Journal of the London Mathematical Society, 2026. Preprint version 2, 2025.
https://doi.org/10.1112/jlms.70351
https://arxiv.org/abs/2501.12325v2

[4] Aishik Chattopadhyay. *Character sums over co-dimension one sub-lattices in finite field extensions*. 2026, version 4.
https://arxiv.org/abs/2505.19654v4
