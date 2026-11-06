# A critical-smoothness range for the variance of rough integers

## 1. Result and scope

For an integer $y\ge2$, write
$$
q_y=\prod_{p\le y}p,\qquad
P_y=\prod_{p\le y}(1-1/p),\qquad
\alpha_y(n)=\mathbf1_{(n,q_y)=1}.
$$
For positive integers $X,H$, define
$$
V(X,H,y)=\frac1X\int_0^X
\left(\sum_{x<n\le x+H}\alpha_y(n)-HP_y\right)^2dx
$$
and the complete-period variance
$$
M(H,y)=\frac1{q_y}\int_0^{q_y}
\left(\sum_{x<n\le x+H}\alpha_y(n)-HP_y\right)^2dx.
$$
The latter is precisely Gorodetsky's main term [1, Lemma 1.5]. Its explicit
positive expression is
$$
M(H,y)=\prod_{2<p\le y}(1-2/p)
\sum_{n\ge1}g_y(n)
\left\{\frac H{2n}\right\}
\left(1-\left\{\frac H{2n}\right\}\right),
\tag{1.1}
$$
where $g_y$ is multiplicative, supported on odd squarefree integers with
prime factors at most $y$, and $g_y(p)=p/(p-2)$ for $2<p\le y$.
In (1.1) the product multiplies the entire sum.

**Theorem 1.** Fix $K>0$ and $0<A<17/50$. Suppose $X\to\infty$ through
integers, $H=\lfloor X^A\rfloor$, and
$$
y=\left\lfloor K^{-2}(\log X)^2\right\rfloor.
$$
Then
$$
V(X,H,y)\sim M(H,y).
\tag{1.2}
$$
The conclusion also holds when $y/(\log X)^2$ stays in a fixed compact
subinterval of $(0,\infty)$.

Gorodetsky [1, Theorem 1.1] proves this asymptotic over a much broader set
of parameters. On the slice $y\asymp(\log X)^2$, its stated condition gives
$A<1/3$. Theorem 1 extends that slice to $A<17/50$. It does not improve
all of [1]'s ranges. The conjectural endpoint suggested by [1, Conjecture 2]
on this slice is $2/3$.

The analytic input is a coefficient-sensitive application of
Bettin--Chandee--Radziwiłł's twisted second-moment proof [2], based on the
trilinear Kloosterman estimate of Bettin--Chandee [3]. We retain the actual
$\ell^2$ coefficient norms, then extract a short canonical smooth divisor.
The resulting mean estimate is not a new Kloosterman bound.

The connection with the Riemann hypothesis is through mean-square
comparisons of actual integer counts and continuous approximations, for
which rough-number variances provide an arithmetic input. The present
result does not control the evolving covariance of the pole-completed
Euler products motivating this work, does not handle their fractional
prime weights or all mixed smooth cofactors, and gives no new zero-free
region. RH remains unresolved.

## 2. Uniform smooth-support bounds

Here $P^+(n)$ and $P^-(n)$ denote the largest and smallest prime factors,
with $P^+(1)=1$ and $P^-(1)=+\infty$.
Let
$$
E_y=\prod_{p\le y}(1-p^{-1/2})^{-1}.
$$
Throughout the proof, $y\asymp(\log X)^2$. Chebyshev's upper bound for the
number of primes and partial summation give
$$
E_y=\exp\!\left(O\!\left(\frac{\sqrt y}{\log y}\right)\right)=X^{o(1)}.
\tag{2.1}
$$
Every occurrence of $X^\epsilon$ below permits an arbitrarily small fixed
$\epsilon>0$. Constants may depend on fixed lower and upper bounds for
$y/(\log X)^2$ and on other fixed exponent ranges.

Rankin's elementary estimate is
$$
\Psi(u,y)\le\sqrt u\,E_y\qquad(u\ge1).
\tag{2.2}
$$
If $|a_n|\le1$ is supported on $N<n\le2N$, $P^+(n)\le y$, then
$$
\sum_n\frac{|a_n|^2}{n}\le\sqrt2 E_yN^{-1/2}.
\tag{2.3}
$$
We shall also need the positive gcd form
$$
\sum_{n,m}\frac{|a_na_m|(n,m)}{nm}
\le2\sqrt2 E_y^3N^{-1/2}.
\tag{2.4}
$$
Indeed, write $(n,m)=\sum_{g\mid n,\ g\mid m}\varphi(g)$. Only smooth $g$
occur, and
$$
\sum_{\substack{N<gk\le2N\\P^+(k)\le y}}\frac1k
\le\frac gN\Psi(2N/g,y)
\le\sqrt{\frac{2g}{N}}E_y.
$$
The contribution of each such $g$ to the gcd form is at most
$2E_y^2/N$, since $\varphi(g)\le g$. There are at most
$\sqrt{2N}E_y$ possible $g$. This also covers $g>N$ and $k=1$.

The reciprocal tail estimate
$$
\sum_{\substack{n>Z\\P^+(n)\le y}}\frac1n
\le E_yZ^{-1/2}
\tag{2.5}
$$
will pay the divisor terms beyond the actual counting interval.

## 3. A twisted moment with smooth coefficients

We first record the precise use of [2,3]. All coefficients below may be
complex, may depend on the external parameters, and may include sharp
interval restrictions.

**Lemma 2.** Let
$$
B_N(s)=\sum_{\substack{N<n\le2N\\P^+(n)\le y}}a_nn^{-s},
\qquad |a_n|\le1.
$$
In the range $N\le T\le N^2$, retaining the coefficient norms in the proof
of [2] gives
$$
\begin{aligned}
\int_T^{2T}|\zeta(1/2+it)B_N(1/2+it)|^2dt
\ll_\epsilon T^\epsilon\bigl[&
E_y^3TN^{-1/2}\log(TN)\\
&+E_y(T^{3/20}N^{23/20}+N^{11/8})\\
&+T^{1/3}+NT^{-1/2}+N^2/T+1\bigr].
\end{aligned}
\tag{3.1}
$$
We use this only with $N\le T^{17/33-\rho}$ for a fixed $\rho>0$.
In this subrange all errors are at most a subpower multiple of
$TN^{-1/2}$.

**Proof.**
Take a fixed nonnegative smooth height majorant for $[T,2T]$. The proof
of [2, Theorem 1, Sections 3.1--3.3] applies with bounded coefficients
and that majorant; a fixed enlargement of its support only changes
constants. We describe the coefficient substitution and retain every
other error.

Write $g$ for the common divisor extracted in [2]. The two original
coefficient blocks have comparable lengths $N_1,N_2\asymp N$; their
reduced lengths remain $N_1/g,N_2/g$. Immediately before [2, (3.7)],
the two coefficient vectors have entries of the form
$$
a_{gn_1}F_1(gn_1)n_1^{-z},\qquad
\overline{a_{gn_2}}F_2(gn_2)F_M(xn_2)n_2^{-z},
\qquad\Re z=\epsilon,
$$
with bounded cutoff factors. By (2.2), each squared norm is at most
$O(E_y(N/g)^{1/2})$, up to harmless small powers. Their product of
norms is therefore
$$
O(E_y(N/g)^{1/2}),
$$
whereas the dense product used in [2] is of size $N/g$.

The third vector is
$\nu_{x,v}(a)=\sum_{h\Delta=a}e(-hx+\Delta v/(2\pi))$ and has norm
$O(L^{1/2+\epsilon})$ on a block of length $L$. The bound
[3, Theorem 1], equivalently [2, Proposition 1], is linear in each of
these three norms. Its additional factor
$(1+L/((N_1/g)(N_2/g)))^{1/2}$ is bounded, since
$L\ll N_1N_2/(g^2T^{1-\epsilon})$.

The integrations used in [2, (3.7)] remain on
$x\asymp gM/N_2$, $v\asymp Tg/(MN_1)$. Before separating the height
weight by Mellin inversion, insert a smooth cutoff in $v$ equal to one
on this forced range, with support in a fixed enlargement. It is
independent of $n_1,n_2$ and preserves the integration domain after
separation. The Mellin integral has bounded seminorms. Thus the
coefficient substitution is valid uniformly in the resulting phases.

The dense bound per $g$ in [2, (3.7)] is
$$
T^\epsilon
\left(T^{3/20}N^{33/20}g^{-53/20}
+N^{15/8}g^{-23/8}\right).
$$
Multiplying by the actual norm ratio $E_y(N/g)^{-1/2}$ gives
$$
E_yT^\epsilon
\left(T^{3/20}N^{23/20}g^{-43/20}
+N^{11/8}g^{-19/8}\right).
\tag{3.2}
$$
Both $g$-sums converge. The remaining dyadic partitions cost logarithms.

The diagonal and zero Poisson frequency combine, exactly as in [2], into
$$
\sum_{n,m}\frac{a_n\overline{a_m}(n,m)}{nm}
\int_{\mathbb R}
\left(\log\frac{t(n,m)^2}{2\pi nm}+2\gamma\right)\phi(t/T)\,dt.
$$
Its absolute value is at most $O(T\log(TN))$ times (2.4).
No positivity of the logarithm is assumed.

We leave all remaining errors at their dense-coefficient values:

- the approximate functional equation has pointwise error
  $O(T^{-2/3})$, and the ordinary mean value theorem, with $N\le T$,
  gives integrated error $O(T^{1/3+\epsilon})$;
- the quadratic Taylor remainder preceding Poisson summation is
  $O(T^\epsilon N^2T^{-3/2})$;
- the correction in [2, Section 3.3] is
  $O(T^\epsilon(NT^{-1/2}+N^2/T))$;
- large product, large shift and large Poisson-frequency tails are
  negligible after fixed integrations by parts; the zero-mode endpoint
  extensions contribute at most $O(T^\epsilon)$.

These are estimates for bounded coefficients with arbitrary zeros in
their support. In particular, no sparsity factor is applied to a
coefficient-independent error. The Taylor term is dominated by $N^2/T$.
This proves (3.1).

For the last assertion, the first arithmetic error requires
$N^{33/20}\le T^{17/20}$ and the second requires $N^{15/8}\le T$.
Both hold when $N\le T^{17/33-\rho}$; the other displayed errors have
more slack. $\square$

**Lemma 3.** Fix $0<c<C$. Uniformly for $X^c\le D,T\le X^C$ and
$$
B_D(s)=\sum_{\substack{D<n\le2D\\P^+(n)\le y}}a_nn^{-s},
\qquad |a_n|\le1,
$$
one has
$$
\int_T^{2T}|\zeta(1/2+it)B_D(1/2+it)|^2dt
\ll_\epsilon X^\epsilon
\left(TD^{-1/2}+T^{49/66}\right).
\tag{3.3}
$$

**Proof.**
Fix a small $\rho>0$ and put $\beta=17/33-\rho>1/2$.
If $T\ge D^{1/\beta}$ and $T\le D^2$, use Lemma 2 directly.
If $T\ge D^2$, Cauchy, the classical fourth moment of $\zeta$, and the
ordinary mean value theorem applied to $B_D^2$ give
$$
\int_T^{2T}|\zeta B_D|^2
\ll_\epsilon X^\epsilon
\left(TD^{-1/2}+(TD)^{1/2}\right)
\ll_\epsilon X^\epsilon TD^{-1/2}.
\tag{3.4}
$$
Here the coefficient square sum for $B_D^2$ is at most
$D^\epsilon(\sum |a_n|^2/n)^2$, by the divisor bound and Cauchy.
All logarithms are harmless because $D,T$ lie between fixed powers of $X$.

It remains to treat $T<D^{1/\beta}$. Set $R=T^\beta/(4y)$, so $yR<D/4$.
For each smooth $n$, list its prime factors with multiplicity in
nondecreasing order. Let $k$ be the first initial product exceeding $R$
and put $b=n/k$. This split is uniquely characterized by
$$
R<k\le yR,\qquad
k/P^+(k)\le R,\qquad
P^+(k)\le P^-(b),
\tag{3.5}
$$
where $P^-(1)=+\infty$. The non-strict inequality allows repeated
primes across the split.

Consequently
$$
B_D(s)=\sum_{\substack{b\le2D/R\\P^+(b)\le y}}b^{-s}B_b(s),
$$
where $B_b(s)$ has coefficients $a_{kb}$ restricted by (3.5) and
the original condition $D<kb\le2D$. Every coefficient still has modulus
at most one. Thus the sharp cutoff is retained without a Perron
approximation.

Split $R<k\le yR$ into $O(\log y)$ dyadic intervals. Every resulting
length $N$ satisfies, for sufficiently large $X$,
$$
\sqrt T<N<yR=T^\beta/4,
$$
because $T^{\beta-1/2}/y\to\infty$ uniformly. Lemma 2 applies to each
block. Minkowski and
$$
\sum_{P^+(b)\le y}b^{-1/2}=E_y
$$
give a bound $X^\epsilon TR^{-1/2}$ for the original squared norm.
This is
$X^\epsilon T^{49/66+\rho/2}$ times a harmless factor $\sqrt y$.
Choose $\rho$ and the intermediate epsilons small in terms of the
requested $\epsilon$ and the fixed upper exponent $C$. This proves
(3.3). $\square$

## 4. From moments to additive count increments

**Lemma 4.** Fix $0<c<C$. Suppose $X^c\le D,V/H\le X^C$,
$H\le V$, and $D\le X^C$. Let $|a_d|\le1$ be supported on
$D<d\le2D$, $P^+(d)\le y$, and define
$$
F_D(x)=\sum_d a_d\left(\left\lfloor\frac xd\right\rfloor-\frac xd\right).
$$
Then
$$
\frac1V\int_V^{2V}|F_D(x+H)-F_D(x)|^2dx
\ll_\epsilon X^\epsilon
\left(HD^{-1/2}+H^{83/66}V^{-17/66}\right).
\tag{4.1}
$$

**Proof.**
The additive-to-multiplicative comparison of
Gorodetsky--Matomäki--Radziwiłł--Rodgers [4, Lemma 10], following
Saffari--Vaughan, gives
$$
\int_V^{2V}|F(x+H)-F(x)|^2dx
\ll \sup_{\theta\in[H/(3V),3H/V]}
\int_V^{3V}|F(u(1+\theta))-F(u)|^2du.
\tag{4.2}
$$
Only local square integrability is needed: one may cut off $F$ outside
the bounded interval containing every argument in (4.2).
For completeness, (4.2) follows by bounding the left increment by the
two increments through $x+v$, averaging $2H\le v\le3H$, changing
variables in the second term, and then putting $v=\theta x$.
The Jacobian is $x\asymp V$ and the $\theta$-interval has length
$O(H/V)$.

There is also a direct Mellin identity without a contour-shifting
assumption. For $0<\Re s<1$,
$$
\int_0^\infty(\lfloor x\rfloor-x)x^{-s-1}dx=\frac{\zeta(s)}s.
\tag{4.3}
$$
Indeed the integral on $(0,1)$ is $1/(s-1)$, and that on $(1,\infty)$
is $-\int_1^\infty\{x\}x^{-s-1}dx$, the standard continuation formula.
Both integrals converge absolutely in this strip.

The function $e^{-u/2}F_D(e^u)$ lies in $L^2(\mathbb R)$: $F_D(x)=O(x)$
near zero and is bounded near infinity. Applying (4.3) to its finite
divisor sum and then Plancherel gives, with $w=\log(1+\theta)$,
$$
\int_0^\infty
\frac{|F_D(e^w x)-F_D(x)|^2}{x^2}dx
=\frac1{2\pi}\int_{\mathbb R}
\left|\frac{e^{w(1/2+it)}-1}{1/2+it}\right|^2
|\zeta(1/2+it)B_D(1/2+it)|^2dt.
\tag{4.4}
$$
Here $B_D(s)=\sum a_dd^{-s}$ and $w\asymp H/V$.
The multiplier is $O(\min(w,1/|t|))$, uniformly in the range used below.

Put $T_0=1/w\asymp V/H$. Lemma 3, dyadic summation, and the elementary
bound $|B_D|\le E_y$ at the omitted lowest heights imply
$$
\int_{|t|\le T_0}|\zeta B_D|^2dt
\ll_\epsilon X^\epsilon
\left(T_0D^{-1/2}+T_0^{49/66}\right).
\tag{4.5}
$$
To justify the lowest heights, split at $X^{c/2}$ after decreasing
$c$ by a fixed factor if necessary to absorb the constants in $T_0$.
Their second moment is $O(X^{c/2+o(1)})$, which is dominated by
$T_0^{49/66}$; above them apply Lemma 3 with a smaller lower exponent.
Negative heights are handled by conjugating the coefficients.

For higher dyads use Lemma 3 with the actual $t^{-2}$ weight. It suffices
to use it up to an arbitrarily large fixed power of $X$.
For all $T\ge D^2$, the proof of (3.4), keeping the height logarithms,
gives
$$
\int_T^{2T}|\zeta B_D|^2dt
\ll_\epsilon D^\epsilon E_y\,TD^{-1/2}\log^2(2T).
\tag{4.6}
$$
Consequently the remaining infinite tail is convergent and, by choosing
that fixed power sufficiently large, is bounded by
$X^\epsilon T_0^{-1}D^{-1/2}$. This does not absorb an unbounded
$\log T$ in $X^\epsilon$ before integration.

Combining these estimates proves that the right side of (4.4) is
$$
\ll_\epsilon X^\epsilon
\left(wD^{-1/2}+w^{83/66}\right).
$$
Equation (4.2) and $x\asymp V$ then give (4.1). $\square$

## 5. The complete-period tail and the small divisors

Write
$$
e_d(x)=\left\lfloor\frac{x+H}{d}\right\rfloor
-\left\lfloor\frac xd\right\rfloor-\frac Hd,\qquad
S(x)=\sum_{d\mid q_y}\mu(d)e_d(x).
$$
Then $S(x)$ is exactly the centered rough count defining $V$ and $M$.
For $Z\ge1$ split $S=S_{\le Z}+S_{>Z}$.

If $g=(d,e)$, the mean over any common period is
$$
\langle e_de_e\rangle
=\frac{g^2}{de}
\left\{\frac Hg\right\}
\left(1-\left\{\frac Hg\right\}\right)
\le\frac{Hg}{de}.
\tag{5.1}
$$
For example, this follows from the Fourier coefficients of the two
floor increments: only frequencies $j/g$ coincide. The standard
identity
$\sum_{j\ne0}|1-e(jv)|^2/(4\pi^2j^2)=\{v\}(1-\{v\})$
gives the displayed equality. The identity is also obtained by
integrating the piecewise constant increments over their common period.

By (2.4), each divisor block $D<d\le2D$ has complete-period squared norm
at most $2\sqrt2 HE_y^3D^{-1/2}$. Minkowski and a geometric sum of its
square roots give
$$
\langle |S_{>Z}|^2\rangle
\ll HE_y^3Z^{-1/2}.
\tag{5.2}
$$
The sum is finite, ending at $q_y$. The bound is uniform in that endpoint.
In particular, if $M_Z=\langle |S_{\le Z}|^2\rangle$, then
$$
|\sqrt{M_Z}-\sqrt{M(H,y)}|
\ll H^{1/2}E_y^{3/2}Z^{-1/4}.
\tag{5.3}
$$

For small divisors an elementary complete-period estimate suffices.
Since $|e_d(x)|\le1$ and $e_d e_e$ has period $[d,e]\le de$,
$$
\left|\frac1X\int_0^X e_d(x)e_e(x)\,dx-\langle e_de_e\rangle\right|
\le\frac{2de}{X}.
$$
Thus
$$
\left|\frac1X\int_0^X|S_{\le Z}(x)|^2dx-M_Z\right|
\ll \frac1X
\left(\sum_{\substack{d\le Z\\P^+(d)\le y}}d\right)^2
\ll E_y^2\frac{Z^3}{X}.
\tag{5.4}
$$
This estimate keeps the cross terms; they are not replaced by separate
diagonal variances.

## 6. The finite-interval divisor tail, including early origins

Take $Z=HX^\kappa$, where $\kappa=1/100$. For large $X$, $H<Z/2$.
If $0\le x<Z/2$, no divisor $d>Z$ contributes an integer multiple to
$(x,x+H]$. Hence, by (2.5),
$$
S_{>Z}(x)=-H\sum_{\substack{d\mid q_y\\d>Z}}\frac{\mu(d)}d,\qquad
\frac1X\int_0^{Z/2}|S_{>Z}(x)|^2dx
\ll \frac{H^2E_y^2}{X}.
\tag{6.1}
$$

Cover $[Z/2,X]$ by dyadic origin intervals $[V,2V]$ with $V\ge Z/2$;
the final interval may extend past $X$, which is harmless for an upper
bound. Split the divisors into $Z<d\le4V$ and $d>4V$.
In the latter range $x+H\le3V<d$, so this is again a linear tail, with
normalized squared norm $O(H^2E_y^2/V)$.

Split $Z<d\le4V$ into dyadic blocks, retaining both endpoints in the
coefficients. All their lengths $D$ and the heights $V/H$ lie between
fixed positive powers of $X$ and a fixed upper power of $X$.
Indeed $D\ge Z\ge X^\kappa$ and $V/H\ge X^\kappa/2$.
Lemma 4 therefore applies uniformly, including cases where $V/H>D^2$,
which are covered by (3.4) and (4.6).

Minkowski over the divisor blocks, a geometric sum of $D^{-1/4}$,
and absorption of the logarithmic block count give
$$
\frac1V\int_V^{2V}|S_{>Z}(x)|^2dx
\ll_\epsilon X^\epsilon
\left(HZ^{-1/2}+H^{83/66}V^{-17/66}+\frac{H^2}{V}\right).
\tag{6.2}
$$
Multiplying by $V/X$ and summing the origin intervals is essential.
The middle contribution is a geometric sum of $V^{49/66}/X$,
dominated by its largest interval. The last contribution costs only
another logarithm. Along with (6.1), this proves
$$
\frac1X\int_0^X|S_{>Z}(x)|^2dx
\ll_\epsilon X^\epsilon
\left(HZ^{-1/2}+H^{83/66}X^{-17/66}+\frac{H^2}{X}\right).
\tag{6.3}
$$
Thus the dyadic-origin estimate has been recovered on the original
interval $[0,X]$; early origins have not been discarded.

## 7. Completion of the proof

Gorodetsky [1, Theorem 1.3(4), (1.20)] gives, on the present slice,
$$
M(H,y)=H^{1/2+o(1)}=X^{A/2+o(1)}.
\tag{7.1}
$$
Indeed $M\asymp P_y\Psi_{\mu^2}(H,y)/\log(2+\log H/\log y)$, and
$\Psi_{\mu^2}(H,y)=H^{1-\log\log H/\log y+o(1)}$ with
$\log\log H/\log y\to1/2$.

The complete-period tail (5.2) and the first term of (6.3) are
$$
HZ^{-1/2}X^{o(1)}
=H^{1/2}X^{-\kappa/2+o(1)}
=o(M).
$$
The second term of (6.3), divided by $X^{A/2}$, has exponent
$$
\frac{83A-17}{66}-\frac A2
=\frac{50A-17}{66}<0.
$$
The third has relative exponent $3A/2-1<0$.
Finally the small-divisor error in (5.4), divided by $X^{A/2}$, has
exponent
$$
\frac52A+3\kappa-1<0
$$
for every $A<17/50$ and $\kappa=1/100$.
Choose $\epsilon$ smaller than all fixed margins.

It follows from (5.3) that $M_Z\sim M$. Equation (5.4) gives
$X^{-1}\int_0^X|S_{\le Z}|^2\sim M$. Equation (6.3) and the triangle
inequality in $L^2([0,X],dx/X)$ now give
$$
\left|\sqrt{V(X,H,y)}
-\left(\frac1X\int_0^X|S_{\le Z}(x)|^2dx\right)^{1/2}\right|
=o(\sqrt M).
$$
This proves Theorem 1.

## 8. Comparison, verification and limitations

The elementary version of the extraction in Lemma 3 uses the classical
zeta fourth moment and the fourth moment of a short polynomial. Its
bound is $X^\epsilon(TD^{-1/2}+T^{3/4})$. Repeating Sections 4--7
then gives the endpoint $A<1/3$. Thus the change from $1/3$ to $17/50$
comes from the coefficient norms inside [2]'s arithmetic estimate,
followed by the same complete recovery, rather than a comparison of
different pieces of the variance.

The canonical extraction is an elementary ordered-prime factorization.
The local norm-retention calculation was previously derived in the
author's unpublished working notes for a different shifted-moment
problem; no priority for a new Kloosterman method is claimed. The new
claim here is the full rough-number variance asymptotic on the stated
critical-smoothness slice, including the small divisors, cross terms and
early origins.

The accompanying standard-Python controls compare the canonical
extraction with direct prime-factor enumeration, including repeated
primes, sharp endpoints and nonmultiplicative coefficients. They also
check the rational exponent ledger. Separate complete-period controls
compare direct integer counts with the exact covariance formula (5.1)
and the small/large divisor decomposition. These are finite algebraic
checks; the asymptotic theorem rests on the proof and the imported
analytic results, not on numerical extrapolation.

The supplement contains the two scripts and their recorded JSON outputs.
From its extracted root, run

    python3 experiments/zeta3097_extraction_control.py
    python3 experiments/zeta3098_periodic_variance_control.py

Both use only the Python standard library. The expected results are
PASS, with 4,392 supported integers in ten extraction fixtures and
62,820 directly counted origins in six complete-period fixtures.
Each script regenerates its corresponding result JSON. Code is released
under the MIT license included in the supplement; no third-party source
files are bundled.

Theorem 1 does not establish [1, Conjecture 2], does not establish the
much stronger smooth Möbius moment
$\int_T^{2T}|\zeta M_D|^2\ll X^\epsilon(TD^{-1/2}+1)$, and does not
justify replacing the full source in an RH criterion by a sharp
rough-number model. Fractional prime weights and the mixed smooth
cofactor recovery remain separate unsolved tasks.

## References

[1] O. Gorodetsky, *The variance of integers without small prime factors
in short intervals*, Mathematische Zeitschrift (2024).
https://doi.org/10.1007/s00209-024-03601-w .
Version used for theorem and equation numbers:
https://arxiv.org/abs/2111.00853v3 .

[2] S. Bettin, V. Chandee and M. Radziwiłł, *The mean square of the
product of the Riemann zeta-function with Dirichlet polynomials*,
Journal für die reine und angewandte Mathematik 729 (2017), 51--79.
Version used for proof and equation numbers:
https://arxiv.org/abs/1411.7764v1 .

[3] S. Bettin and V. Chandee, *Trilinear forms with Kloosterman fractions*,
Advances in Mathematics 328 (2018), 1234--1262.
https://arxiv.org/abs/1502.00769v1 .

[4] O. Gorodetsky, K. Matomäki, M. Radziwiłł and B. Rodgers,
*On the variance of squarefree integers in short intervals and
arithmetic progressions*, Geometric and Functional Analysis 31 (2021),
111--179. https://doi.org/10.1007/s00039-021-00557-5 .
Version used for Lemma 10 and the Mellin comparison:
https://arxiv.org/abs/2006.04060v2 .
