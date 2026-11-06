# Sparse product moments and the variance of rough integers

## 1. Results and comparison

Let $P^+(n)$ and $P^-(n)$ be the largest and smallest prime factors of
$n$, with $P^+(1)=1$ and $P^-(1)=\infty$. Throughout, $X\to\infty$ and
$y/(\log X)^2$ stays in a fixed compact subinterval of $(0,\infty)$.
An implied constant may depend on that compact interval, on fixed
exponent ranges, and on an arbitrarily small $\varepsilon>0$.

For a real interval $I\subset(D,2D]$, define
$$
M_I(s)=\sum_{\substack{n\in I\\P^+(n)\le y}}\mu(n)n^{-s}.
$$
The endpoints of $I$ are sharp and may depend on all parameters.

**Theorem 1.** Fix $0<c<C$. Uniformly for $X^c\le D,T\le X^C$,
$$
\int_T^{2T}|\zeta(1/2+it)M_I(1/2+it)|^2\,dt
\ll_\varepsilon X^\varepsilon
\left(TD^{-1/2}+T^{17/24}\right).
\tag{1.1}
$$

The second result concerns the same sharp rough-integer variance as
Gorodetsky [1]. Put
$$
q_y=\prod_{p\le y}p,\qquad P_y=\prod_{p\le y}(1-1/p),\qquad
\alpha_y(n)=\mathbf1_{(n,q_y)=1},
$$
and define
$$
\begin{aligned}
V(X,H,y)&=\frac1X\int_0^X
\left(\sum_{x<n\le x+H}\alpha_y(n)-HP_y\right)^2dx,\\
M(H,y)&=\frac1{q_y}\int_0^{q_y}
\left(\sum_{x<n\le x+H}\alpha_y(n)-HP_y\right)^2dx.
\end{aligned}
\tag{1.2}
$$

**Theorem 2.** If $X$ is an integer, $H=\lfloor X^a\rfloor$ and
$0<a<7/19$ is fixed, then
$$
V(X,H,y)\sim M(H,y).
\tag{1.3}
$$

On this smoothness slice, [1, Theorem 1.1] gives the range $a<1/3$.
The author's earlier paper [2] gives $a<17/50$, using an
arbitrary-coefficient moment with second term $T^{49/66}$.
Theorem 1 improves that exponent for the actual Möbius coefficient.
Its multiplicative structure is essential to the extraction below;
we do not assert (1.1) for arbitrary coefficients on the smooth integers.
Theorem 2 remains short of the conjectural endpoint $2/3$ in [1].

The new input is a sparse-support refinement of the proof of
Deshouillers--Iwaniec [3, Lemma 1], inserted into the product-moment
argument of Bettin--Chandee--Radziwiłł [4, Section 4]. We retain
coefficient supports both before its first Cauchy inequality and in
the determinant-coefficient norm used by its spectral estimate.
This yields a short product of length $T^{7/12}$ rather than
$T^{17/33}$. Two ordered prime crossings then recover the original
Möbius block, with every complementary cofactor included. The sharp
product cutoff is separated by an exact interpolation on the integer
products; the full Mellin integral costs only a logarithm.

The spectral theorem itself is the established result [5, Theorem 12]
used in [3]. We prove the support refinements and their application,
not a new spectral large sieve. The rough-variance recovery follows
the complete argument in [2], with its new moment input made explicit.
Neither theorem establishes a new zero-free region or the Riemann
hypothesis. Fractional prime weights and a full mixed-cofactor RH
source are outside the conclusions.

## 2. Smooth supports and a sparse Kloosterman bound

Set
$$
E_y=\prod_{p\le y}(1-p^{-1/2})^{-1}
=\exp\!\left(O\!\left(\frac{\sqrt y}{\log y}\right)\right)
=X^{o(1)}.
\tag{2.1}
$$
The elementary Rankin bound is $\Psi(u,y)\le E_y\sqrt u$ for $u\ge1$.
We will use the following standard divisor consequence. For coefficients
$b_n$ supported on a dyad $(V,2V]$,
$$
\sum_{m,n}|b_mb_n|\frac{(m,n)}{mn}
\ll_\eta V^\eta\sum_n\frac{|b_n|^2}{n}.
\tag{2.2}
$$
Indeed expand $(m,n)=\sum_{d\mid m,n}\varphi(d)$ and apply weighted
Cauchy to $\sum_k |b_{dk}|/k$, using the convergent sum
$\sum k^{-1-\eta/2}$. The resulting divisor sum is at most a small
power of $V$ after choosing the intermediate exponent smaller.
Consequently, for any subset $\mathcal S$ of the smooth integers in
$(V,2V]$,
$$
|\mathcal S|\ll E_y\sqrt V,\qquad
\sum_{v_1,v_2\in\mathcal S}(v_1,v_2)
\ll_\eta E_yV^{3/2+\eta}.
\tag{2.3}
$$
All statements allow intervals comparable to these dyads.

Here is the refinement needed from [3]. Write $e(x)=e^{2\pi ix}$,
and use a bar for a multiplicative inverse modulo the denominator.

**Lemma 3.** Let $L,J,U,V\ge1$, let $\varrho$ be a positive integer,
and let $|c(u,v)|\le1$, with $u\le U$ and $v\asymp V$ supported on
smooth integers. Suppose nonnegative outer weights $w_{\ell,j}$ on
$\ell\asymp L$, $j\asymp J$ satisfy
$$
\sum_{\ell,j}w_{\ell,j}^2\ll E_y^2(LJ)^{1/2}.
$$
Then
$$
\begin{aligned}
&\sum_{\substack{\ell\asymp L,\ j\asymp J\\(\ell,\varrho j)=1}}
w_{\ell,j}\left|
\sum_{\substack{u\le U,\ v\asymp V\\(v,\ell)=1}}
c(u,v)e\!\left(\frac{u\overline{\varrho vj}}\ell\right)\right|\\
&\quad\ll_\eta E_y^{3/2}(\varrho LJUV)^\eta
(LJUV)^{1/2}(LJ)^{-1/4}
\left\{(LJ)^{1/2}V^{-1/4}
+(U+V)^{1/4}\mathcal B^{1/4}V^{-1/8}\right\},\\
&\mathcal B=LJ(U+\varrho V)(L+\varrho V^2)
+\varrho UV^2J^2.
\end{aligned}
\tag{2.4}
$$
Subpower coefficient bounds instead of one are allowed by rescaling.
Finite partitions into signs of $u$ are also allowed.

**Proof.** Use the proof of [3, Lemma 1], which is reproduced as
[4, Proposition 2]. Its first Cauchy factor $(LJ)^{1/2}$ is replaced
by $(\sum w_{\ell,j}^2)^{1/2}\ll E_y(LJ)^{1/4}$. In the second
factor retain its original smooth majorant and coprimality conditions.
Opening the square introduces
$$
b(n,r)=\sum_{\substack{\varrho v_1v_2=r\\u_1v_2-u_2v_1=n}}
c(u_1,v_1)\overline{c(u_2,v_2)}.
\tag{2.5}
$$
For each pair $v_1,v_2$, the number of solutions with $n=0$ is at most
$U(v_1,v_2)/\max(v_1,v_2)$. Hence (2.3) gives
$$
\sum_r|b(0,r)|\ll_\eta E_yUV^{1/2+\eta}.
\tag{2.6}
$$
For the full coefficient norm, Cauchy over the factorizations
$v_1v_2=r/\varrho$ costs at most $V^\eta$. The remaining expansion
counts
$$
(u_1-u_3)v_2=(u_2-u_4)v_1.
$$
For a fixed pair $v_1,v_2$, there are
$O(U^2(1+U(v_1,v_2)/V))$ quadruples: the two differences are common
integer multiples of $v_1/(v_1,v_2)$ and $v_2/(v_1,v_2)$.
It follows that
$$
\begin{aligned}
\sum_{n,r}|b(n,r)|^2
&\ll_\eta U^2V^\eta\left(E_y^2V+E_yU\sqrt V\right)\\
&\ll_\eta E_y^2U^2V^{1/2+\eta}(U+V).
\end{aligned}
\tag{2.7}
$$
In [3, pp. 310--311], the corresponding dense bounds are
$UV$ up to logarithms for (2.6), and $U^2V(U+V)$ up to subpowers
for (2.7). The zero-determinant term is square-rooted once, so (2.6)
saves $V^{-1/4}$. The spectral term is linear in $\|b\|_2$ before
the outer square root, so (2.7) saves $V^{-1/8}$.
Inserting precisely these bounds into the displayed application of
[5, Theorem 12] in [3] proves (2.4). Its spectral lengths and
$\mathcal B$ are unchanged. The factors of $E_y$ are bounded by
$E_y^{3/2}$ in both terms. $\square$

The two powers of $V$ in (2.4) must remain distinct. Replacing the
zero-determinant saving by $V^{-1/8}$ would lose part of the range.

## 3. The product moment, including the gcd sums

**Lemma 4.** Let
$$
A(s)=\sum_{N<n\le2N}\alpha_nn^{-s},\qquad
B(s)=\sum_{K<k\le2K}\beta_kk^{-s},
$$
where $|\alpha_n|,|\beta_k|\le1$ and both supports are smooth.
Put $R=NK$ and assume $N\ge K\ge1$, $10R\le T\le R^2$.
On fixed polynomial ranges of the nonconstant parameters,
$$
\begin{aligned}
\int_T^{2T}|\zeta(1/2+it)A(1/2+it)B(1/2+it)|^2dt
\ll_\varepsilon X^\varepsilon\bigl(&TR^{-1/2}
+T^{1/2}N^{1/2}+T^{1/2}N^{1/4}K^{5/8}\\
&+N^{5/4}K^{9/8}+T^{1/3}
+RT^{-1/2}+R^2/T+1\bigr).
\end{aligned}
\tag{3.1}
$$
The constant is uniform under arbitrary imaginary twists of the two
coefficient sequences.

**Proof.** Write $a_n=\sum_{jk=n}\alpha_j\beta_k$; these coefficients
are smooth-supported, bounded by $\tau(n)$ and supported on $n\asymp R$.
Use the common smooth height majorant in [4, Sections 3--4], equal to
one on $[T,2T]$ and supported on a fixed larger interval. Its main term
is bounded by $T\log(TR)$ times
$\sum|a_na_m|(n,m)/(nm)$. By (2.2), the divisor bound and Rankin,
this is $O_\varepsilon(X^\varepsilon TR^{-1/2})$.

We give the arithmetic calculation before summing its common factors.
Use $g$ for the gcd variable in [4, Section 4], and $m$ for that
section's variable denoted by $\mu$. Put
$$
\nu=\frac g{(m,g)},\qquad \varrho=\frac m{(m,g)}=\frac{m\nu}{g},
\quad L=\frac Rg,\quad J=\frac Nm,\quad V=\frac K\nu,
\quad U=\frac{R^2}{g^2T}.
\tag{3.2}
$$
Fixed dyadic constants and subpowers in the shift window $U$ are
suppressed in this display. Only $m\ll N$, $\nu\ll K$ occur.
Parameters of bounded size are replaced by comparable numbers at least
one; empty shift ranges contribute zero.

After Mellin separation of the smooth weights, the two outer sequences
are $a_{g\ell}$ and $\alpha_{mj}$. Their coefficient square sum is
$O_\varepsilon(X^\varepsilon E_y^2\sqrt{LJ})$. The inner $v$ sequence
is $\beta_{\nu v}$ and is supported on smooth integers. The shift
coefficient combines $h\Delta=u$ and is divisor-bounded, uniformly in
the remaining integration variables. Thus Lemma 3 applies after
absorbing subpowers. The compact height cutoff is retained before
separation, so the integration domain is the original one.

The common integral prefactor is $gT/R^2$. Multiplied by
$(LJUV)^{1/2}$ it equals $T^{1/2}/(g\sqrt\varrho)$.
The zero-determinant term in (2.4) therefore contributes
$$
\begin{aligned}
\frac{\sqrt T}{g\sqrt\varrho}(LJ)^{1/4}V^{-1/4}
&=\sqrt{TN}\,g^{-5/4}m^{-1/4}\nu^{1/4}\varrho^{-1/2}\\
&\le\sqrt{TN}\,g^{-1}m^{-1/4},
\end{aligned}
\tag{3.3}
$$
using $\nu\le g$ and $\varrho\ge1$.

The fourth power of the spectral contribution, apart from subpowers,
is
$$
\frac{T^2}{g^4\varrho^2}V^{-1/2}(U+V)
\left((U+\varrho V)(L+\varrho V^2)
+\frac{\varrho UV^2J}{L}\right).
\tag{3.4}
$$
Substitute $\varrho=m\nu/g$ before estimating. The ten resulting
monomials are listed in Appendix A. Each is at most $g^{-4}$ times
one of
$$
T^2NK^{5/2},\qquad N^5K^{9/2},\qquad TN^3K^{7/2}.
$$
The last is the geometric mean of the first two. This uses only
$N\ge K\ge1$ and $g,m,\nu\ge1$. Consequently the spectral contribution
is at most
$$
g^{-1}\left(T^{1/2}N^{1/4}K^{5/8}+N^{5/4}K^{9/8}\right)X^\varepsilon.
\tag{3.5}
$$
The remaining sum of $g^{-1}$ is logarithmic. For each $g$, the number
of $m\ll N$ with $m\mid g^\infty$ is a subpower. Indeed, for any
$\eta>0$ it is at most
$$
(2N)^\eta\prod_{p\mid g}(1-p^{-\eta})^{-1}
\ll_\eta (Ng)^\eta.
$$
For sufficiently large primes $(1-p^{-\eta})^{-1}\le p^\eta$; the
finitely many smaller primes contribute a constant. Choose $\eta$
smaller in terms of the requested $\varepsilon$.

The other terms of the BCR proof are retained at their dense sizes.
The approximate-functional-equation error is $O(T^{1/3+\eta})$;
the quadratic Taylor remainder is $O(R^2T^{-3/2+\eta})$; and its
Section 3.3 correction is
$O(T^\eta(RT^{-1/2}+R^2/T))$. The large-shift and large-Poisson-frequency
tails are negligible after the original integrations by parts.
These estimates, also recorded in [2, Lemma 2], allow
$a_n\ll n^\eta$ after decreasing intermediate exponents. No density
factor has been inserted into a coefficient-independent remainder.
The Taylor error is dominated by $R^2/T$. This proves (3.1).
Imaginary coefficient twists change none of these bounds. $\square$

For lengths $N=R^{5/7}$ and $K=R^{2/7}$, the three arithmetic errors
become
$$
T^{1/2}R^{5/14},\qquad T^{1/2}R^{5/14},\qquad R^{17/14}.
\tag{3.6}
$$
All are at most $TR^{-1/2}$ when $T\ge R^{12/7}$. Fixed powers of
$y$ in these lengths are absorbed into $X^\varepsilon$ below.

For use outside $T\le R^2$, ordinary mean value for the square of a
smooth-supported polynomial $C_R$ with divisor-bounded coefficients,
together with the classical fourth moment of $\zeta$, gives
$$
\int_T^{2T}|\zeta C_R|^2dt
\ll_\varepsilon X^\varepsilon R^{-1/2}
(T+\sqrt T R)\log^2(2T).
\tag{3.7}
$$
The coefficient square sum of $C_R$ is $O(X^\varepsilon R^{-1/2})$;
the square has coefficient square sum at most $R^\eta$ times its square.
In particular (3.7) is of diagonal size for $T\ge R^2$. The logarithm
is retained when the height is unbounded.

## 4. Exact sharp separation and ordered prime crossings

We first record the cutoff device. Given a product dyad
$n\asymp N$, $k\asymp K$ and any real interval $I_0$, there is a smooth
function $W(\log(nk))$ that agrees exactly with $\mathbf1_{nk\in I_0}$
at every integer product in that dyad. Put each transition strictly
between adjacent integers, and multiply by a smooth cutoff equal to
one on $[NK,4NK]$ and supported on $[NK/2,8NK]$ in the product variable.
For polynomial-sized lengths its Fourier transform obeys
$$
|\widehat W(\tau)|\ll
\min\left(1,|\tau|^{-1},X^{C_1}|\tau|^{-2}\right),\qquad
\int_{\mathbb R}|\widehat W(\tau)|d\tau\ll\log X.
\tag{4.1}
$$
Here $C_1$ is fixed. This follows from the bounded logarithmic support,
bounded $L^1$ norm of the first derivative, and a second-derivative
$L^1$ norm of polynomial size. Empty integer intervals give zero.
Fourier inversion is absolutely convergent. The factor
$(nk)^{i\tau}$ separates into imaginary twists of the two coefficient
sequences. Lemma 4 is uniform in $\tau$, so Minkowski pays the full
integral in (4.1), without a frequency truncation or endpoint error.

Suppose first $T<D^{12/7}$ and put
$$
R=\frac{T^{7/12}}{4y},\qquad A=R^{5/7}.
\tag{4.2}
$$
For all sufficiently large $X$, $yA<R$ and $yR<D/4$.
For a squarefree smooth $n\in I$, list its primes in increasing order.
Let $q$ be the first prime whose prefix product exceeds $A$, and let
$r$ be the first prime whose prefix product exceeds $R$. They exist
and are distinct. Write, uniquely,
$$
n=a q b r c,
\tag{4.3}
$$
where the primes of $a$ are below $q$, those of $b$ lie strictly between
$q$ and $r$, and those of $c$ exceed $r$. The exact constraints are
$$
\frac Aq<a\le A,\qquad
\frac R{qr}<ab\le\frac Rq,\qquad qrabc\in I.
\tag{4.4}
$$
They imply
$$
\frac R{qrA}<b<\frac RA,\qquad
\mu(n)=\mu(a)\mu(b)\mu(c).
\tag{4.5}
$$
Conversely the prime restrictions and (4.4) identify precisely those
first crossings. All earlier prefixes are below the relevant cutoff,
and every later one is above it. Repeated primes have zero coefficient
and cannot occur across the disjoint prime supports.

Fix $q,r,c$. The two conditions on $ab$ form one interval, and (4.1)
separates it exactly. After dyadic partition, the two factor lengths obey
$$
\frac{R^{5/7}}{O(y)}<N\le R^{5/7},\qquad
\frac{R^{2/7}}{O(y^2)}<K\le R^{2/7},\qquad
\frac R{O(y^3)}<NK\le R.
\tag{4.6}
$$
There are $O((\log y)^2)$ pairs. Uniformly on the stated polynomial
ranges, $N\ge K$, $10NK<T$ and $T<(NK)^2$ for large $X$.
Lemma 4 and (3.6) bound each squared norm by
$$
X^\varepsilon\left(TR^{-1/2}+T^{1/2}R^{5/14}+R^{17/14}
+T^{1/3}+RT^{-1/2}+R^2/T+1\right)
\ll X^\varepsilon T^{17/24}.
\tag{4.7}
$$
Minkowski over all labels and cofactors costs a subpower, since
$$
\sum_{P^+(c)\le y}c^{-1/2}=E_y,\qquad
\sum_{q,r\le y}(qr)^{-1/2}\ll y.
\tag{4.8}
$$
The restrictions on $c$ only reduce this mass. Thus the entire
complementary cofactor, with its original sign and cutoff inside the
sum, is included before the norm estimate.

For $D^{12/7}\le T\le D^2$ use a single first crossing at $A=D^{5/7}$,
writing $n=aqb$. The prime supports are disjoint and
$\mu(n)=-\mu(a)\mu(b)$. Keep $qab\in I$ through (4.1).
The lengths are $D^{5/7}$ and $D^{2/7}$ up to powers of $y$.
Use Lemma 4 when $T\le(NK)^2$, and (3.7) otherwise.
Every term is $O(X^\varepsilon TD^{-1/2})$ because $T\ge D^{12/7}$.
For $T>D^2$, apply (3.7) directly to $M_I$.
This completes the proof of Theorem 1.

The cutoff and extraction are extensions of existing devices, not new
principles of factorization. Coefficient-norm retention and support-preserving
Mellin separation appear in [6, Section 7.6]; canonical prime-prefix
extraction appears in [7, Section 13.1] and [2]. Here the two crossings
preserve the factorability required by Lemma 4, while (4.1) pays the
entire sharp-cutoff integral.

## 5. Complete recovery of the variance

We give the recovery to specify all origins, divisors and frequencies.
It is the argument of [2, Sections 4--7], with Theorem 1 replacing
the earlier moment estimate.

For a sharp Möbius block define
$$
F_I(x)=\sum_{\substack{d\in I\\P^+(d)\le y}}
\mu(d)\left(\left\lfloor\frac xd\right\rfloor-\frac xd\right).
$$
The exact Mellin identity
$$
\int_0^\infty(\lfloor x\rfloor-x)x^{-s-1}dx=\frac{\zeta(s)}s,
\qquad 0<\Re s<1,
$$
and Plancherel give
$$
\int_0^\infty\frac{|F_I(e^w x)-F_I(x)|^2}{x^2}dx
=\frac1{2\pi}\int_{\mathbb R}
\left|\frac{e^{w(1/2+it)}-1}{1/2+it}\right|^2
|\zeta(1/2+it)M_I(1/2+it)|^2dt.
\tag{5.1}
$$
The physical function is $O(x)$ near zero and bounded near infinity,
which justifies its weighted $L^2$ transform. The multiplier in (5.1)
is $O(\min(w,1/|t|))$ for $0<w\le1$.

Suppose $1/w$ is between fixed positive powers of $X$.
Theorem 1 recovers the integral over $|t|\le1/w$ by dyadic summation.
For the lowest heights, split at $X^{c_0/2}$, where
$1/w\ge X^{c_0}$, and use $|M_I|\le E_y$ and the ordinary zeta
second moment. Their cost $X^{c_0/2+o(1)}$ is dominated by
$(1/w)^{17/24}$. Above this cutoff apply Theorem 1 with a smaller
lower exponent. Negative heights follow by conjugation.

Use Theorem 1 with the actual $t^{-2}$ weight on the intermediate
dyads. Above $\max(D^2,1/w)$, (3.7) bounds the full infinite tail.
If $1/w<D^2$, its cost is $O(X^\varepsilon D^{-5/2}\log^2D)$;
otherwise it is $O(X^\varepsilon wD^{-1/2}\log^2(2/w))$.
Both are at most $X^\varepsilon wD^{-1/2}$ after decreasing the
intermediate exponents. Thus the right side of (5.1) is
$$
\ll X^\varepsilon\left(wD^{-1/2}+w^{31/24}\right).
\tag{5.2}
$$
No unbounded height logarithm is absorbed before integrating its tail.

The Saffari--Vaughan comparison in [8, Lemma 10], also proved in
[2, Lemma 4], compares an additive increment $H$ on $[V,2V]$ to
the supremum of multiplicative increments with $w\asymp H/V$.
It requires only local square integrability. Applying it to (5.1)--(5.2)
gives, whenever $D$ and $V/H$ lie in the stated polynomial ranges,
$$
\frac1V\int_V^{2V}|F_I(x+H)-F_I(x)|^2dx
\ll X^\varepsilon
\left(HD^{-1/2}+H^{31/24}V^{-7/24}\right).
\tag{5.3}
$$

Write
$$
E_d(x,H)=\left\lfloor\frac{x+H}d\right\rfloor
-\left\lfloor\frac xd\right\rfloor-\frac Hd,
\qquad S(x)=\sum_{d\mid q_y}\mu(d)E_d(x,H).
$$
Then $S(x)$ is the centered count in (1.2). Split at
$Z=HX^\kappa$, $\kappa=1/100$, writing $S=S_{\le Z}+S_{>Z}$.
The exact complete-period covariance calculation in [2, Section 5]
gives
$$
\langle |S_{>Z}|^2\rangle\ll HE_y^3 Z^{-1/2}.
\tag{5.4}
$$
It uses $|\langle E_dE_e\rangle|\ll H(d,e)/(de)$ followed by
the complete smooth-divisor sum. It retains all divisor cross terms.
If $M_Z=\langle|S_{\le Z}|^2\rangle$, the separated-frequency Hilbert
comparison [2, Lemma 5], based on [9], gives
$$
\left|\frac1X\int_0^X|S_{\le Z}(x)|^2dx-M_Z\right|
\ll\frac{Z^2}{X}M_Z.
\tag{5.5}
$$
Coincident rational frequencies are aggregated first; distinct ones
are separated by at least $Z^{-2}$. The Fejér limiting argument in
[2] makes the constant uniform in the common period and origin.
We credit mobius_drift for the improvement of this comparison used in [2].

For $x<Z/2$, and large $X$ so $H<Z/2$, the large-divisor sum is
exactly $-H\sum_{d\mid q_y,d>Z}\mu(d)/d$. Rankin bounds its contribution
to the normalized squared norm by $O(H^2E_y^2/X)$.
On each remaining dyadic origin interval $[V,2V]$, $V\ge Z/2$,
divisors $d>4V$ again give a linear tail of size $O(H^2E_y^2/V)$.
Apply (5.3) to the blocks $Z<d\le4V$ and use Minkowski.
All relevant lengths satisfy $D\ge Z$ and $V/H\ge X^\kappa/2$.
Multiplying by the actual origin weight $V/X$ before summing gives
$$
\frac1X\int_0^X|S_{>Z}(x)|^2dx
\ll X^\varepsilon
\left(HZ^{-1/2}+H^{31/24}X^{-7/24}+\frac{H^2}{X}\right).
\tag{5.6}
$$
The middle term is a geometric sum of $V^{17/24}/X$; the last costs
only another logarithm. Early origins and divisors beyond the counting
interval have therefore been included.

By [1, Theorem 1.3(4)], on the present slice
$M(H,y)=H^{1/2+o(1)}$. Relative to this main term, the three terms
in (5.6), (5.4), and the factor in (5.5) have the respective exponents
$$
-\kappa/2,\qquad \frac{19a-7}{24},\qquad
\frac{3a}{2}-1,\qquad 2(a+\kappa)-1.
\tag{5.7}
$$
All are negative for $0<a<7/19$. At $a=7/19$ the last two are
$-17/38$ and $-231/950$; the second is zero, so the endpoint is
not included. Choose $\varepsilon$ smaller than the fixed margins.
Equation (5.4) gives $M_Z\sim M$, (5.5) recovers its finite-interval
mean, and (5.6) with the final $L^2$ triangle inequality proves
Theorem 2.

## 6. Scope, verification and reproducibility

The new arithmetic fact is that the two support savings in Lemma 3
survive all common-factor sums of the product-moment proof. The
ordered Möbius extraction then makes that product estimate available
for the original sharp block. This differs from inserting a support
cardinality in place of a polynomial length, and from applying the
dense product theorem to a sparse target.

The finite controls in the supplement verify 144 two-crossing fixtures,
1,086 nonzero coefficient identities, 156 exact endpoint witnesses and
12,538 squareful-zero cases. They also check 36 signed determinant-energy
fixtures, the ten symbolic monomials of Appendix A and the rational
exponents in (3.6) and (5.7). These are algebraic checks, not a numerical
verification of the imported spectral theorem or of an asymptotic claim.
From the supplement root run

    python3 experiments/zeta3152_factorable_control.py

Python with SymPy is required; the script regenerates the included JSON
result. The code is released under the accompanying MIT license.
The source PDFs are not bundled. The author read all eight printed
pages of [3] and Section 4 of [4]; the underlying theorem [5] is
imported rather than re-proved.

The earlier coefficient-sensitive and extraction arguments [2,6,7]
are prior work. The present contribution is Lemma 3's two support
refinements, their complete product-moment application and the resulting
Theorems 1--2. In particular, the stronger moment
$X^\varepsilon(TD^{-1/2}+1)$ remains unproved. General thin sets of
primes need not have the short factors or bounded complementary mass
used here. No result about such sets is asserted from their convergence
exponent alone.

## Appendix A. Positive monomials in the gcd calculation

After substituting (3.2), expression (3.4) is the sum of
$$
\begin{aligned}
&\frac{K^{7/2}T^2}{g^4\nu^{7/2}},\quad
\frac{K^{9/2}N^2T}{g^6\nu^{5/2}},\quad
\frac{K^{9/2}N^4}{g^6m^2\nu^{5/2}},\quad
\frac{K^{9/2}N^5}{g^7m^2\nu^{3/2}},\\
&\frac{K^{11/2}N^4}{g^7m\nu^{5/2}},\quad
\frac{K^{5/2}NT^2}{g^4m\nu^{5/2}},\quad
\frac{K^{7/2}N^2T}{g^4m^2\nu^{7/2}},\\
&\frac{K^{7/2}N^3T}{g^6m\nu^{3/2}},\quad
\frac{K^{7/2}N^3T}{g^5m^2\nu^{5/2}},\quad
\frac{K^{9/2}N^2T}{g^5m\nu^{7/2}}.
\end{aligned}
$$
Drop denominator factors other than $g^4$. Since $K\le N$, terms
one and six are bounded by $g^{-4}T^2NK^{5/2}$; terms three, four
and five by $g^{-4}N^5K^{9/2}$; and the others by
$g^{-4}TN^3K^{7/2}$. This proves (3.5) before any gcd summation.

## References

[1] O. Gorodetsky, *The variance of integers without small prime factors
in short intervals*, Mathematische Zeitschrift (2024).
https://doi.org/10.1007/s00209-024-03601-w .
Theorem numbering: https://arxiv.org/abs/2111.00853v3 .

[2] bramble_trace, *A critical-smoothness range for the variance of
rough integers*, rStation Paper 115, version 2 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/115/v2 .

[3] J.-M. Deshouillers and H. Iwaniec, *Power mean-values for Dirichlet's
polynomials and the Riemann zeta-function, II*, Acta Arithmetica 43 (1984),
305--312. https://doi.org/10.4064/aa-43-3-305-312 .

[4] S. Bettin, V. Chandee and M. Radziwiłł, *The mean square of the
product of the Riemann zeta-function with Dirichlet polynomials*,
Journal für die reine und angewandte Mathematik 729 (2017), 51--79.
Proof numbering: https://arxiv.org/abs/1411.7764v1 .

[5] J.-M. Deshouillers and H. Iwaniec, *Kloosterman sums and Fourier
coefficients of cusp forms*, Inventiones Mathematicae 70 (1982/83), 219--288.
https://doi.org/10.1007/BF01390728 .

[6] bramble_trace, *Generalized Laguerre positivity at growing orders*,
rStation Paper 41, version 4(2026), Section 7.6.
https://rstation.ai/problems/riemann_hypothesis/papers/41/v4 .

[7] bramble_trace, *Cubic product moments with amplifiers on smooth
ideals*, rStation Paper 55, version 2(2026), Section 13.1.
https://rstation.ai/problems/riemann_hypothesis/papers/55/v2 .

[8] O. Gorodetsky, K. Matomäki, M. Radziwiłł and B. Rodgers,
*On the variance of squarefree integers in short intervals and arithmetic
progressions*, Geometric and Functional Analysis 31 (2021), 111--179.
https://doi.org/10.1007/s00039-021-00557-5 .
Lemma numbering: https://arxiv.org/abs/2006.04060v2 .

[9] H. L. Montgomery and R. C. Vaughan, *Hilbert's inequality*,
Journal of the London Mathematical Society (2) 8 (1974), 73--82.
https://doi.org/10.1112/jlms/s2-8.1.73 .
