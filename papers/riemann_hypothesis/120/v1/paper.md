# Zero-density bounds for maximal sharp Möbius sums

## 1. The maximal transfer

Zero-density estimates for the Riemann zeta function constrain the large
values of Dirichlet polynomials. Matomäki and Teräväinen [1, Theorem 1.2]
make this implication quantitative for plain interval polynomials. Their
Remark 1.3 sketches a transfer to Möbius and prime polynomials using
Heath–Brown's identity, with an additional term of size
$T^{2\nu+\varepsilon}$. We give a direct transfer for the Möbius polynomial
that has no such additional term. It is simultaneous in both sharp
endpoints and permits polynomial lengths up to $T^A$ for every fixed
$A<2$.

The proof uses classical ingredients. Ivić [2, Section 2] bounds a complex
branch of $\log\zeta$ in a local zero-free region; the related argument
in [1, Section 6] is particularly convenient here. Adaptive sharp Perron
contours occur in Soundararajan [3, Section 5]. The estimates in that paper
are conditional on RH and are not used here. Our use of a fixed grid, an
entire interval kernel, and a positive convolution gives one uniform
envelope before the endpoints are maximized. A sharp truncation estimate
that remains valid when the polynomial length exceeds the contour height
provides the longer range.

Write
$$
N_\zeta(\sigma,U)
=\#\{\rho=\beta+i\gamma:\zeta(\rho)=0,
\ 0<\beta<1,\ \beta\ge\sigma,\ |\gamma|\le U\},
$$
counting multiplicities. Throughout, $T$ is sufficiently large in terms
of the fixed parameters. We use Lebesgue measure on the real line.
A set is **1-separated** if distinct elements have distance at least 1.

**Theorem 1.** Fix $0<\lambda<A<2$ and $\varepsilon>0$. For
$0\le\nu\le1/2$, let $E_\mu(T,\nu;\lambda,A)$ consist of those
$t\in[-T,T]$ for which there are integers
$$
T^\lambda\le M\le T^A/2,\qquad M<M'\le2M,
$$
with
$$
\left|\sum_{M<n\le M'}\frac{\mu(n)}{n^{1+it}}\right|
\ge M^{-\nu}.
$$
Then
$$
\operatorname{meas} E_\mu(T,\nu;\lambda,A)
\ll_{\lambda,A,\varepsilon} T^\varepsilon
\sup_{\max(1/2,1-\nu-\varepsilon)\le\sigma\le1}
T^{A(\sigma-(1-\nu))}N_\zeta(\sigma,4T).                 \tag{1}
$$
The same right-hand side bounds the cardinality of every 1-separated
subset of $E_\mu(T,\nu;\lambda,A)$. The constants and the threshold for
$T$ are uniform in $\nu\in[0,1/2]$.

The threshold $M^{-\nu}$ can be replaced by $cM^{-\nu}$ for any fixed
$c>0$, with constants also depending on $c$. Fixed positive factors in
the length limits, or any fixed upper ratio $M'/M$, are harmless.
Consequently a formulation with real endpoints follows by taking floors.

At $A=1/2$, the density expression in (1) has the same form as [1,
Theorem 1.2], without a separate polynomial term. This distinction is
specific to the reciprocal Dirichlet series. It is holomorphic at 1,
whereas the plain and prime Dirichlet series have poles. Section 5
recovers the known small-height term for the plain polynomial by
subtracting its pole and then restoring its continuous main term.

Theorem 1 is a consequence of zero-density information, not a new estimate
for $N_\zeta$. In particular it does not prove RH. It does not assume
simple zeros, bounds for $1/\zeta'(\rho)$, or statistical independence
between zeta values and nearby zeros.

## 2. A classical local reciprocal bound

We supply the version of the zero-free estimate needed for the proof,
including low absolute heights. Its method is the complex-log argument
of [2, Section 2, especially (2.7)] and [1, Section 6]. The use of the
complex logarithm is relevant: an upper bound for $|\zeta|$ alone would
not bound its reciprocal.

**Lemma 2.** Let $0<\delta<1/10$ be fixed and put
$$
B=\log(8T),\qquad L=B^2.
$$
Suppose $1/2+2\delta\le x\le1+2\delta$, $|u|\le3T+2$, and
there is no nontrivial zero in
$$
\operatorname{Re}z\ge x-\delta,
\qquad |\operatorname{Im}z-u|\le L.                    \tag{2}
$$
Then
$$
\left|\frac1{\zeta(x+iu)}\right|\le T^{r_\delta(T)},
\qquad r_\delta(T)\longrightarrow0,                   \tag{3}
$$
uniformly in $x,u$. If $|u|\ge2$, the same conclusion holds for
$|\zeta(x+iu)|$. On the full range of $u$, it holds for
$|\zeta(x+iu)-1/(x+iu-1)|$, with the removable value understood.

*Proof.* First assume $|u|\ge L$ and put $Y=B^{3/2}$. For
$b\in[x,2]$, absolute convergence and Mellin inversion give
$$
\sum_{n\ge1}\Lambda(n)e^{-n/Y}n^{-b-iu}
=-\frac1{2\pi i}\int_{(2)}
\frac{\zeta'}{\zeta}(b+iu+w)\Gamma(w)Y^w\,dw.          \tag{4}
$$
Truncate at $|\operatorname{Im}w|=Y$ and move the contour to
$\operatorname{Re}w=-\delta/2$. For large $T$, the local zero
neighborhoods along this rectangle lie within (2), since $Y+1<L$.
Also $|u|-Y>2$, so the pole of zeta is not encountered. The only
crossed pole of the integrand is the Gamma pole at $w=0$.

The standard local partial-fraction formula is
$$
\frac{\zeta'}{\zeta}(a+iv)
=\sum_{|\gamma-v|\le1}\frac1{a+iv-\rho}
+O(\log(|v|+2)),                                      \tag{5}
$$
uniformly on a fixed real strip away from the pole, together with the
local zero count $O(\log(|v|+2))$; see [1, (6.1)] or [4, Chapter IX].
Every denominator on the new contour has real part at least
$\delta/2$. Thus the logarithmic derivative there is
$O_\delta(B)$. Real parts beyond 2 can instead be handled by absolute
convergence. Stirling's formula, including the horizontal and truncated
tails, gives uniformly in $b$
$$
-\frac{\zeta'}{\zeta}(b+iu)
=\sum_{n\ge1}\Lambda(n)e^{-n/Y}n^{-b-iu}
+O_\delta(BY^{-\delta/2}+1).                           \tag{6}
$$
Here the integral of $|\Gamma(-\delta/2+iv)|$ over $v\in\mathbb R$
is finite with a constant depending on $\delta$.

Integrate (6) horizontally from $x$ to 2, using the continuous branch
of the logarithm anchored at the absolutely convergent
$\log\zeta(2+iu)$. We obtain
$$
\begin{aligned}
\log\zeta(x+iu)-\log\zeta(2+iu)
={}&\sum_{n\ge2}\frac{\Lambda(n)}{\log n}e^{-n/Y}
       (n^{-x-iu}-n^{-2-iu})\\
&+O_\delta(BY^{-\delta/2}+1).
\end{aligned}                                         \tag{7}
$$
Since $\Lambda(n)/\log n\le1$, bounding the sum by the one at real
part $1/2$ gives
$$
|\log\zeta(x+iu)|
\ll_\delta B^{3/4}+B^{1-3\delta/4}+1=o_\delta(B).        \tag{8}
$$
Both signs of the real part of this logarithm are therefore controlled.
This proves the bounds for zeta and its reciprocal at these heights,
uniformly through real part 1.

For $2\le|u|\le L$, apply (5) along the horizontal segment from
$x+iu$ to $2+iu$. The local zero count and the fixed separation give
$$
\left|\frac{\zeta'}{\zeta}(b+iu)\right|
\ll_\delta\log(|u|+2),\qquad x\le b\le2.
$$
Horizontal integration implies
$$
|\zeta(x+iu)|+|1/\zeta(x+iu)|
\ll_\delta (|u|+2)^{C_\delta}
\ll_\delta (\log(8T))^{2C_\delta}.                     \tag{9}
$$
For $|u|\le2$, compactness on the fixed zero-separated strip bounds
the reciprocal. Its apparent singularity at 1 is removable and is
in fact a zero. The function
$$
F(z)=\zeta(z)-\frac1{z-1}                              \tag{10}
$$
is entire and bounded on this compact strip. For $|u|\ge2$, subtracting
the pole term changes the zeta bound by only a bounded quantity.
Absorb all the constants and logarithmic factors in $T^{r_\delta(T)}$.
This proves the lemma. $\square$

## 3. A sharp interval envelope on one fixed grid

**Lemma 3.** Under the length assumptions of Theorem 1, fix
$0<\delta<1/10$. There are numbers $\beta_j\in[1/2,1]$, on a fixed
integer grid depending only on $T$, for which
$$
\begin{aligned}
\left|\sum_{M<n\le M'}\mu(n)n^{-1-it}\right|
\ll_\delta{}&T^{r_\delta(T)}M^{2\delta}
\sum_j\frac{M^{\beta_j-1}}{1+|j-t|}\\
&+\frac{T^{r_\delta(T)}M^{2\delta}\log(2M)}{T},
\end{aligned}                                         \tag{11}
$$
simultaneously for $t\in[-T,T]$ and all endpoint pairs. For
$\alpha>1/2$ they satisfy
$$
\#\{j:\beta_j\ge\alpha\}
\ll (\log(8T))^2N_\zeta(\alpha,4T).                   \tag{12}
$$

*Proof.* Let $J$ be the integers whose unit intervals intersect
$[-3T,3T]$. With $L=(\log(8T))^2$, set
$$
\beta_j=\max\left(\frac12,
\{\beta:\zeta(\beta+i\gamma)=0,
\ \gamma\in[j-2L,j+1+2L]\}\right).                     \tag{13}
$$
Only nontrivial zeros are used. Each zero belongs to at most $4L+3$
of these windows, and all the relevant ordinates have absolute value at
most $4T$ for large $T$. This gives (12).

Set
$$
s=1+it,\quad X=M+\tfrac12,\quad Z=M'+\tfrac12,
\quad H=2T,\quad c=2\delta,
$$
and use the entire kernel
$$
\Phi_{X,Z}(w)=\frac{Z^w-X^w}{w}
=\int_X^Z v^{w-1}\,dv.                                \tag{14}
$$
Its value at zero is $\log(Z/X)$. For $-1/2\le a\le2\delta$,
$$
|\Phi_{X,Z}(a+iy)|\ll_\delta\frac{M^a}{1+|y|}.         \tag{15}
$$
Use the integral in (14) when $|w|\le1$ and its quotient otherwise.
The ratio $Z/X$ is bounded by 2.

Subtracting the two half-integer truncated Perron formulas gives
$$
\sum_{M<n\le M'}\mu(n)n^{-s}
=\frac1{2\pi i}\int_{c-iH}^{c+iH}
          \frac{\Phi_{X,Z}(w)}{\zeta(s+w)}\,dw
+O_\delta\left(\frac{M^{2\delta}\log(2M)}{T}\right).
                                                               \tag{16}
$$
We verify the error without assuming $M\le H$. At $X$ its absolute
value is bounded, up to a constant depending on $c$, by
$$
\sum_{n\ge1}\frac1n\left(\frac Xn\right)^c
\min\left(1,\frac1{H|\log(X/n)|}\right).               \tag{17}
$$
Outside $[X/2,2X]$, this is $O_c(X^c/H)$. Inside that interval, it
is bounded by a constant times
$$
\frac1X\sum_{n\in[X/2,2X]}
\min\left(1,\frac X{H|n-X|}\right).                   \tag{18}
$$
If $X/H<1/2$, half-integrality gives $|n-X|\ge1/2$, so the sum
is $O(\log(2X)/H)$. If $X/H\ge1/2$, the
$O(X/H+1)$ terms with $|n-X|\le X/H$ contribute $O(1/H)$;
the remaining harmonic sum contributes $O(\log(2X)/H)$.
The same estimate holds at $Z$. This proves (16) throughout the claimed
range, and indeed for any endpoint length.

In the absolute-height coordinate $z=s+w$, shift the contour over
$[t-H,t+H]$ from real part $1+2\delta$ to the staircase having
real part $\beta_j+2\delta$ over $[j,j+1]$. Join neighboring pieces
by horizontal segments and add the two endpoint connectors. For each
vertical piece, all zeros at its height are to its left. At a common
integer height, both adjacent enlarged windows cover the local zero
neighborhood; this protects even the smaller real-part endpoint of the
connector. Thus no reciprocal pole is crossed and Lemma 2 applies to
all pieces and connectors. The pole of zeta at 1 is harmless for its
reciprocal, and (14) removes the Perron pole at $w=0$.

On a vertical piece, (15) bounds the contribution by
$$
\ll_\delta T^{r_\delta(T)}
\frac{M^{\beta_j-1+2\delta}}{1+|j-t|}.
$$
An internal connector has bounded length. Bound its power of $M$ by
the larger of the two adjacent powers and absorb it in their contributions;
the neighboring distance kernels are comparable. An endpoint connector
has $|\operatorname{Im}w|=H$ and real part at most $2\delta$, so costs
$O_\delta(T^{r_\delta(T)}M^{2\delta}/T)$. Extending the resulting
positive sum to all of $J$ is allowed. Combining these bounds with (16)
proves (11). $\square$

## 4. Taking the supremum before Markov's inequality

We prove Theorem 1. The distance kernel in Lemma 3 has the three
elementary properties
$$
\begin{aligned}
\sup_{|t|\le T}\sum_{j\in J}\frac1{1+|j-t|}&\ll\log(8T),\\
\sup_{j\in J}\int_{-T}^{T}\frac{dt}{1+|j-t|}&\ll\log(8T),\\
\sup_{j\in J}\sum_{t\in\mathcal S}\frac1{1+|j-t|}&\ll\log(8T)
\end{aligned}                                         \tag{19}
$$
for every 1-separated $\mathcal S\subset[-T,T]$. The last bound follows
by grouping the sample points according to their unit distance from $j$.

Put $\beta_0=1-\nu$. Choose
$$
0<\eta<\min\left(\frac1{10},
                  \frac{\varepsilon}{16(A+1)}\right),
$$
then choose $\delta>0$ so small that
$$
\delta<\min\left(\frac\eta4,
               \frac{1-A/2}{4A},\frac1{20}\right).    \tag{20}
$$
All remaining losses will be absorbed by taking $T$ sufficiently large.
In particular we may make $r_\delta(T)$ smaller than fixed positive
fractions of $\lambda\eta$, $\varepsilon$ and $1-A/2$.

Multiply (11) by $M^\nu$. Its error is at most
$$
T^{-1+A(\nu+2\delta)+r_\delta(T)}O(\log T)=o(1),       \tag{21}
$$
uniformly in $\nu\le1/2$, by $A<2$ and (20).

First suppose $\beta_0-1/2>\eta$. By (19), the part with
$\beta_j\le\beta_0-\eta$ contributes at most
$$
O_\delta\left(
T^{r_\delta(T)-\lambda(\eta-2\delta)}\log T\right)
=o(1),                                                \tag{22}
$$
uniformly for every allowed endpoint pair. For the remaining grid indices,
$$
M^{\beta_j-\beta_0+2\delta}
\le T^{2A\delta+A\eta}T^{A(\beta_j-\beta_0)}.           \tag{23}
$$
If the exponent on $M$ is nonnegative, use $M\le T^A$.
Otherwise the left side is at most 1 and
$\beta_j-\beta_0> -\eta$ proves the inequality.

Equations (21)–(23) imply that the *entire maximal event*, with both
endpoints allowed to depend on $t$, is contained in
$$
\left\{t:\sum_{\beta_j>\beta_0-\eta}
\frac{T^{A(\beta_j-\beta_0)}}{1+|j-t|}
\ge c_\delta T^{-r_\delta(T)-2A\delta-A\eta}\right\}. \tag{24}
$$
No endpoint union bound has been taken. Apply Markov's inequality to
this single positive convolution and use the second line of (19).
For a 1-separated subset use its third line instead. Both operations
give an upper bound
$$
\ll_\delta T^{r_\delta(T)+2A\delta+A\eta}\log(8T)
\sum_{\beta_j>\beta_0-\eta}T^{A(\beta_j-\beta_0)}.     \tag{25}
$$
Partition the remaining $\beta_j$ into intervals of width $1/\log(8T)$,
starting at $\beta_0-\eta>1/2$. Within a bin the displayed weight
changes by at most a constant depending on $A$. Using (12) at each
lower bin endpoint bounds (25) by
$$
\ll_{\delta,A} T^{r_\delta(T)+2A\delta+A\eta}
(\log(8T))^4
\sup_{\beta_0-\eta\le\sigma\le1}
T^{A(\sigma-\beta_0)}N_\zeta(\sigma,4T).               \tag{26}
$$
Our parameter choices absorb the prefactor into $T^\varepsilon$.
Enlarging the supremum down to $\max(1/2,\beta_0-\varepsilon)$
proves (1) in this case.

If $0\le\beta_0-1/2\le\eta$, use the trivial $O(T)$ bound for
measure or for the size of a separated subset. The supremum in (1)
includes $\sigma=1/2$. Zero symmetry and the classical zero count
[4] imply $N_\zeta(1/2,4T)\gg T\log T$. Thus the right-hand side
of (1) is at least
$$
\gg T^{\varepsilon-A\eta}T\log T\gg T.               \tag{27}
$$
This completes the proof, including uniformity through $\nu=1/2$.
A fixed positive threshold constant only changes the constants in (22)
and (24) and the threshold for sufficiently large $T$.

The same proof permits fixed positive multiples of the lower and upper
length bounds and any fixed endpoint ratio. For real endpoints $M,M'$,
take their floors in the sum. For large $T$, the lower integer endpoint
is at least $M/2$, the upper-to-lower ratio is bounded by 3, and the
threshold changes by a bounded factor uniformly in $\nu$. This proves
the stated real-endpoint variant. $\square$

**Remark 4.** More generally one may fix $A>0$ and restrict
$0\le\nu\le1/2$ by $A\nu\le1-\kappa$, with fixed $\kappa>0$.
Replace $1-A/2$ by $\kappa$ in (20)–(21); the rest of the argument is
unchanged. The restriction is a sufficient condition for the error
estimate used here. We make no optimality claim for it.

## 5. The plain polynomial and its continuous main term

The following comparison explains why the small-height term in [1,
Theorem 1.2] is genuine. It is a recovery of a known bound, not a second
novel theorem.

Take $0<\lambda<1/2$, $A=1/2$, and let
$$
\begin{aligned}
P_{M,M'}(t)&=\sum_{M<n\le M'}n^{-1-it},\\
J_{M,M'}(t)&=\int_{M+1/2}^{M'+1/2}x^{-1-it}\,dx,\\
R_{M,M'}(t)&=P_{M,M'}(t)-J_{M,M'}(t).
\end{aligned}                                         \tag{28}
$$
For $\operatorname{Re}z>1$, the entire function $F$ from (10) satisfies
$$
F(z)=\sum_{n\ge1}n^{-z}-\int_1^\infty x^{-z}\,dx.
$$
Applying truncated Perron to the discrete and continuous parts gives
$$
R_{M,M'}(t)
=\frac1{2\pi i}\int_{c-iH}^{c+iH}
               \Phi_{X,Z}(w)F(1+it+w)\,dw
+O_\delta\left(\frac{M^{2\delta}\log(2T)}T\right).    \tag{29}
$$
The discrete error was proved in Lemma 3. At an endpoint $X$, the
continuous error is bounded by
$$
\int_1^\infty \frac1x\left(\frac Xx\right)^c
\min\left(1,\frac1{H|\log(X/x)|}\right)dx.             \tag{30}
$$
Outside $[X/2,2X]$ it is $O_c(X^c/H)$. Within that interval,
$|x-X|\le X/H$ contributes $O(1/H)$ and the complement contributes
$O(\log(2H)/H)$. This justifies (29), including its continuous cutoff.

Both $F$ and $\Phi$ are entire. Lemma 2 bounds $F$ on the same
staircase, so the contour proof gives (11) with $R$ in place of the
Möbius sum. Section 4 consequently gives the density term in (1) for
the centered maximal event, also at any fixed positive threshold.

On the other hand,
$$
|J_{M,M'}(t)|\le\min\left(\log2,\frac2{|t|}\right),    \tag{31}
$$
where the second expression is used only for $t\ne0$. If
$|P_{M,M'}(t)|\ge M^{-\nu}$, then either
$|R_{M,M'}(t)|\ge M^{-\nu}/2$ or
$|J_{M,M'}(t)|\ge M^{-\nu}/2$. The latter condition implies
$$
|t|\le4M^\nu\le4T^{\nu/2}.                           \tag{32}
$$
Its measure and every separated sample count are $O(T^{\nu/2})$.
Thus restoring the continuous main term gives the density expression
plus $T^{\nu/2}$, which is the form of [1, Theorem 1.2], after the
arbitrarily small exponent losses. No corresponding continuous term
appears for the Möbius series because $1/\zeta$ is holomorphic at 1.

## 6. A density consequence and the remaining task

Huxley's classical density estimate for $3/4\le\sigma\le1$, recorded
also in [5, (1.3)], is
$$
N_\zeta(\sigma,4T)
\ll_\epsilon T^{D(\sigma)+\epsilon},\qquad
D(\sigma)=\frac{3(1-\sigma)}{3\sigma-1}.               \tag{33}
$$
Take $A=1$ and $\nu=1/10$. On a neighborhood of $[9/10,1]$,
$$
\frac{d}{d\sigma}(D(\sigma)+\sigma)
=1-\frac6{(3\sigma-1)^2}<0.
$$
The supremum in Theorem 1 is therefore bounded by its value at the
lower endpoint, with the small endpoint displacement absorbed into an
arbitrarily prescribed final exponent loss. We obtain the explicit
consequence
$$
\operatorname{meas}E_\mu(T,1/10;\lambda,1)
\ll_{\lambda,\varepsilon} T^{3/17+\varepsilon},
\qquad 0<\lambda<1,                                  \tag{34}
$$
and the same bound for separated samples. This includes all integer
interval pairs with $T^\lambda\le M\le T/2$. In the shorter range
$A=1/2$, the additional $T^{2\nu+\varepsilon}$ in [1, Remark 1.3]
would instead contribute $T^{1/5+\varepsilon}$ at this value of $\nu$.
Equation (34) makes the difference in the direct transfer explicit.

For other length exponents one must retain the supremum in (1) unless
monotonicity has been checked. For example, $D(\sigma)+A\sigma$ need
not be decreasing throughout the interval when $A>3/2$. The endpoint
$A=2,\nu=1/2$ is not covered by the negligible-error argument.

The estimate is useful for controlling large values of the actual sharp
inverse coefficients rather than a smooth replacement or a decomposition
with an exceptional short factor. It does not bound the zeta-weighted
mass of those exceptional heights better than an arbitrary-set estimate.
In particular, a stronger mean estimate for the product of zeta with a
long sharp Möbius inverse remains a separate arithmetic problem. The
theorem neither improves the input zero-density bounds nor establishes
RH.

## 7. Verification and reproducibility

The argument is entirely analytic. Equations (4)–(9) prove the required
local reciprocal input from the classical partial fractions and zero
count. Equations (17)–(18) cover both orders of polynomial length and
contour height. Equations (21)–(27) give the uniform parameter choices
and both versions of the maximal estimate. Section 5 independently
accounts for the pole term in the known plain-polynomial comparison.
No numerical experiment, unproved zero simplicity, or computational
verification of finitely many zeta zeros is used.

The distinctive conclusion is the simultaneous sharp Möbius transfer
(1), with its longer range and no additional polynomial term. The local
zero-free argument, Perron deformation, elementary positive-kernel
estimate, and density input are credited to their classical sources or
proved explicitly above. This comparison with [1] does not assert that
its Heath–Brown sketch is incorrect.

## References

[1] K. Matomäki and J. Teräväinen. *A note on zero density results implying
large value estimates for Dirichlet polynomials*. 2024, arXiv:2403.13157v1.
https://arxiv.org/abs/2403.13157v1

[2] A. Ivić. *Large values of some zeta-functions near the line
$\sigma=1$*. Hardy–Ramanujan Journal 11 (1988), 13–29.
https://doi.org/10.46298/hrj.1988.104

[3] K. Soundararajan. *Partial sums of the Möbius function*.
Journal für die reine und angewandte Mathematik 631 (2009), 141–152;
arXiv:0705.0723v2.
https://arxiv.org/abs/0705.0723v2

[4] E. C. Titchmarsh, revised by D. R. Heath-Brown. *The theory of the
Riemann zeta-function*. Second edition, Oxford University Press, 1986.
https://global.oup.com/academic/product/the-theory-of-the-riemann-zeta-function-9780198533696

[5] L. Guth and J. Maynard. *New large value estimates for Dirichlet
polynomials*. 2024, arXiv:2405.20552.
https://arxiv.org/abs/2405.20552
