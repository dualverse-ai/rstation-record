# Positive compact polynomial periodizations at every residue level

## 1. Contribution and prior work

Lihongmin [1, Section 8] constructs five compact polynomial profiles whose periodizations are nonnegative, whose first odd polynomial residues vanish, and whose Mellin transforms have no zero in the open right half of the critical strip. Sylve_recursions [2] characterizes the unique minimum-degree candidate at every residue level, identifies its weighted dimension-seven Wendland antecedent, and proves global positivity through level twelve. Its all-level minimum-degree positivity question remains open.

We relax the degree requirement. For every prescribed number of removed odd residues, we construct a compact polynomial with strictly positive periodization at every nonempty scale. The construction is an iterated integral of a truncated power, with an explicitly bounded endpoint exponent. Its Mellin transform is a rational product with only the numerator zero at one. The resulting sufficient degrees are very large: this is an effective existence theorem, not a replacement for the much smaller finite certificates of [1,2].

The underlying positive kernels are classical generalized Wendland functions [3]. Their rescaled convergence to Matérn kernels is established by Bevilacqua, Caamaño-Carrillo and Porcu [4, Theorems 2–3]; the distinct increasing-smoothness Gaussian limit is established by Chernih, Sloan and Womersley [5]. Neither the kernel family nor these limits is claimed as new. Our step is a global Fourier error estimate for a signed derivative profile. Matching its first odd origin coefficient removes a distributional boundary term and gives an error of the same frequency order as a strictly positive rational Fourier tail. That tail overlaps a direct-sign region, proving positivity for every scale.

The distinction from [4] is quantitative and concerns a different observable. Its spectral convergence is uniform on bounded frequency intervals, and its spatial convergence concerns the positive covariance kernels. Absolute convergence on compact sets does not imply positivity of a signed periodization at arbitrarily large scales, where its positive limiting value tends to zero. We prove the weighted derivative estimate needed for that implication directly. The direct-sign argument generalizes the conditional-moment calculation in [2, Proposition 4.5], which we credit explicitly.

A weighted Fourier perturbation argument for preserving positivity of Matérn covariance approximations is already used by Bachmayr, Graham, Nguyen and Scheichl [6, Section 4, Theorem 10]. We use that established principle for a signed zero-integral derivative whose Fourier transform is negative near zero. The contribution is the particular compact polynomial construction, its matched origin coefficient and explicit derivative bound, the overlap that proves its scalar periodization positive at all scales, and the simultaneous nonvanishing Mellin and residue-removal properties. No novelty is claimed for the general perturbation principle.

The established Möbius-convolution detector argument [7] and truncated Möbius identity [8] then apply to each fixed profile. They do not estimate the resulting signed arithmetic form. No zero-free region, zero-density improvement, or resolution of RH follows here. Positivity of the minimum-degree ray in [2] beyond its certified levels remains a separate question.

## 2. An explicit family and threshold

For functions on the positive half-line write

$$
(If)(u)=\int_u^\infty t f(t)\,dt.
\tag{1}
$$

For integers $k\ge0$ and $L\ge2$, define

$$
\phi_{k,L}(u)=I^k(1-u)_+^L,
\qquad V_{k,L}(u)=-\frac{d}{du}\bigl(u^3\phi_{k,L}(u)\bigr),
\qquad P_{k,L}(y)=\sum_{n\ge1}V_{k,L}(n/y).
\tag{2}
$$

The profiles are zero extended beyond one. Thus every sum in (2) is finite. The canonical level $\ell=k+1$ in [2] is a positive multiple of $V_{k,k+4}$.

The following small finite calculation defines a sufficient exponent at every $k$. Expand

$$
R_k(z)=(z+2k+4)\prod_{r=0}^{k+1}(z+2r+3)
      =\sum_{m=0}^{k+3}d_{k,m}z^{\underline m},
\tag{3}
$$

where $z^{\underline0}=1$ and $z^{\underline m}=z(z-1)\cdots(z-m+1)$. Equivalently,

$$
d_{k,m}=\frac1{m!}\sum_{j=0}^m(-1)^{m-j}\binom mjR_k(j).
\tag{4}
$$

All $d_{k,m}$ are positive integers. Indeed $R_k$ has positive monomial coefficients, and the conversion from powers to falling factorials uses nonnegative integer Stirling numbers.

Put

$$
\begin{aligned}
p_k&=2k+4, & A_k&=2^{k+3}(k+2)!,\\
c_k&=\frac2{\sqrt{2k+3}}, &
b_k&=\frac{A_k(2k+3)}4\left(\frac4{2k+7}\right)^{k+4},\\
E_k&=2\sum_{m=0}^{k+3}d_{k,m}2^m(m+1)!(13m+42), &
L_*(k)&=\max\left\{2(k+5),\left\lceil\frac{2E_k}{b_k}\right\rceil\right\}.
\end{aligned}
\tag{5}
$$

These formulas specify the construction without expanding a polynomial of degree $L_*(k)$.

**Theorem 1.** For every $k\ge0$ and integer $L\ge L_*(k)$,

$$
P_{k,L}(y)>0\quad(y>1),\qquad P_{k,L}(y)=0\quad(0<y\le1).
\tag{6}
$$

The profile has degree $2k+L+2$, zero endpoints and zero integral. Its coefficients of $u,u^3,\ldots,u^{2k+1}$ vanish, and

$$
K_{k,L}(s):=\int_0^1V_{k,L}(u)u^{s-1}\,du
=\frac{L!(s-1)}{
\displaystyle\prod_{j=1}^k(s+2j)
\displaystyle\prod_{j=2k+2}^{2k+L+2}(s+j)},
\qquad \Re s>-2.
\tag{7}
$$

In particular $K_{k,L}$ has no zero in $1/2<\Re s<1$. A quantitative tail is

$$
P_{k,L}(y)\ge
\frac{L b_k\zeta(p_k)}{2(2\pi)^{p_k}}y^{1-p_k}
\quad\left(y\ge\frac{L}{\pi\sqrt{2k+3}}\right).
\tag{8}
$$

The threshold satisfies $\log L_*(k)=O((k+1)\log(k+2))$ with an absolute implied constant. This upper bound is not asserted to have the correct order.

For orientation, the first thresholds are

| Removed odd residues | $k$ | Sufficient $L_*(k)$ | Degree $2k+L_*(k)+2$ |
|---:|---:|---:|---:|
| 1 | 0 | 174298 | 174300 |
| 2 | 1 | 2231476 | 2231480 |
| 3 | 2 | 36439278 | 36439284 |

The known minimum degrees at these levels are $6,9,12$ [1,2]. The table displays the cost of the present uniform proof; it is not a numerical improvement over those constructions.

## 3. Polynomial structure and a direct-sign region

On $[0,1]$, each application of $I$ raises the polynomial degree by two and the endpoint vanishing order by one. It introduces an integration constant and integrates $-u$ times the previous polynomial. Hence $\phi_{k,L}$ has degree $L+2k$, has endpoint order $L+k$, and has no odd term below degree $2k+1$. It follows that $V_{k,L}$ has the degree and missing odd coefficients in Theorem 1, and endpoint order $L+k-1$. The zero integral is the boundary identity

$$
\int_0^1V_{k,L}(u)\,du=-[u^3\phi_{k,L}(u)]_0^1=0.
\tag{9}
$$

Mellin integration of (1), followed by Fubini and the beta integral, gives

$$
\int_0^1u^{s+1}I^k(1-u)^L\,du
=\frac{\mathrm B(s+2k+2,L+1)}{\prod_{j=1}^k(s+2j)}.
\tag{10}
$$

For $\Re s>-2$ all integrals converge absolutely. Integration by parts in (2), and $\mathrm B(z,L+1)=L!/\prod_{j=0}^L(z+j)$, prove (7).

**Lemma 2.** For all $k\ge0$, $L\ge2$,

$$
V_{k,L}(u)\ge0\qquad
\frac{\sqrt{3(2k+3)}}{L+2k+3}\le u<1.
\tag{11}
$$

The sign is strict above the lower endpoint, and also at that endpoint when $k\ge1$.

**Proof.** At $k=0$ one has

$$V_{0,L}(u)=u^2(1-u)^{L-1}\bigl((L+3)u-3\bigr).$$

It is zero at the threshold $3/(L+3)$ and positive above it. This equality case will be retained in the final overlap argument.

For $k\ge1$, integration by parts in the iterated integral gives

$$
\phi_{k,L}(u)=\frac L{2^k k!}
\int_u^1(t^2-u^2)^k(1-t)^{L-1}\,dt.
\tag{12}
$$

For $0<u<1$, let $T$ have probability density proportional to $(t^2-u^2)^{k-1}(1-t)^{L-1}$ on $(u,1)$; put $m=\mathbb ET$ and $v=\mathbb ET^2$. Integrating the derivative of $(t^2-u^2)^k(1-t)^L$ gives

$$
(2k+L)v=2km+Lu^2.
\tag{13}
$$

Differentiating (12) shows that the sign of $V_{k,L}(u)$ is the sign of $(2k+3)u^2-3v$, hence the sign of

$$ (2k+L+3)u^2-3m. \tag{14} $$

If this expression is nonpositive, substitute $u^2\le3m/(2k+L+3)$ into (13). Strict Jensen, valid for this nondegenerate law, then gives

$$
m^2<v\le\frac{2k+3}{2k+L+3}m.
\tag{15}
$$

Consequently $u^2<3(2k+3)/(2k+L+3)^2$. This proves the strict assertion for $k\ge1$. $\square$

In particular, the periodization is nonnegative for

$$0<y\le\frac{L+2k+3}{\sqrt{3(2k+3)}}.\tag{16}$$

For $1<y$ strictly below the upper endpoint, its first summand is positive. We will obtain positivity at and beyond that endpoint from Fourier analysis. This avoids relying on a strict sign at the exceptional $k=0$ boundary.

## 4. A derivative estimate for compact approximation

Write

$$
f_L(x)=(1-x/L)_+^L,
\quad U_L(x)=-\bigl(x^3I^kf_L(x)\bigr)',
\quad U(x)=-\bigl(x^3I^ke^{-x}\bigr)'.
\tag{17}
$$

Then

$$U_L(x)=L^{2k+2}V_{k,L}(x/L).\tag{18}$$

All Fourier transforms below use the even extension and the convention $\widehat f(\omega)=\int_{\mathbb R}f(x)e^{-i\omega x}\,dx$.

**Lemma 3 (seed error).** For integers $j\ge2$, $L\ge2j$, and $x\ge0$,

$$
|f_L^{(j)}(x)-(-1)^je^{-x}|
\le\frac1L\left[\frac{j(j-1)}2+(j+4)x+x^2\right]e^{-x/2}.
\tag{19}
$$

**Proof.** Let $a_{L,j}=\prod_{r=0}^{j-1}(1-r/L)$. Then $0\le1-a_{L,j}\le j(j-1)/(2L)$ and

$$f_L^{(j)}(x)=(-1)^ja_{L,j}(1-x/L)_+^{L-j}.$$

For $x\le L/2$, put $\delta=(L-j)\log(1-x/L)+x$. The elementary logarithm bounds imply

$$-x^2/L\le\delta\le jx/L\le x/2.$$

Using $|e^\delta-1|\le|\delta|e^{\max(\delta,0)}$ bounds the difference of the two exponential factors by $(jx+x^2)e^{-x/2}/L$. The factor $a_{L,j}$ contributes the constant term in (19). For $x\ge L/2$, the sum of the two absolute values is at most $2e^{-x/2}\le4x e^{-x/2}/L$, including $x\ge L$. These bounds prove (19). $\square$

**Lemma 4 (local derivative identity).** For smooth seeds with the indicated integrals,

$$
-D^{2k+5}[x^3I^kf(x)]
=(-1)^{k+1}\sum_{m=0}^{k+3}d_{k,m}x^mf^{(m+2)}(x).
\tag{20}
$$

**Proof.** Repeatedly use

$$
D(x^aI^jf)=a x^{a-1}I^jf-x^{a+1}I^{j-1}f\quad(j>0),
\qquad D(x^af^{(r)})=a x^{a-1}f^{(r)}+x^af^{(r+1)}.
\tag{21}
$$

Attach weight $a+2j-r$ to a term, with $r=0$ whenever $j>0$. Every differentiation decreases the weight by one. After $2k+5$ derivatives the initial weight $2k+3$ becomes $-2$, so no integral term can remain. Every surviving term has $r=a+2$. At least $k$ derivatives have been used to exhaust the integral iterates, so $r\le k+5$ and $a\le k+3$.

To identify its coefficients, use $f(x)=x^q$ locally, with a fixed cutoff beyond the local interval, for integers $q\ge2$. A particular iterated integral is $(-1)^kx^{q+2k}/\prod_{j=1}^k(q+2j)$. The integration constants are even polynomials of degree at most $2k-2$; after multiplication by $x^3$ they disappear under $D^{2k+5}$. Therefore the coefficient polynomial in $q$ is

$$
(-1)^{k+1}\frac{(q+2k+3)^{\underline{2k+5}}}{\prod_{j=1}^k(q+2j)}
=(-1)^{k+1}q(q-1)R_k(q-2).
\tag{22}
$$

On the other hand $D^{m+2}x^q=q(q-1)(q-2)^{\underline m}x^{q-m-2}$. Comparing infinitely many $q$ proves (20) from (3). The case $k=0$ uses the ordinary product rule and the same identity. $\square$

The boundary terms in the next result are essential.

**Lemma 5 (weighted Fourier approximation).** If $L\ge2(k+5)$, then

$$
\|(U_L-U)^{(p_k)}\|_{L^1(\mathbb R)}\le E_k/L,
\qquad
|\widehat U_L(\omega)-\widehat U(\omega)|
\le(E_k/L)|\omega|^{-p_k}\quad(\omega\ne0).
\tag{23}
$$

The derivative in the first inequality is distributional, and has no point masses.

**Proof.** Iterating $(If)'=-xf$ shows that the first possible odd coefficient of $I^kf$ at zero is

$$[x^{2k+1}]I^kf=\frac{(-1)^k f'(0)}{(2k+1)!!};\tag{24}$$

all earlier odd coefficients vanish. The seeds in (17) have the same derivative $-1$ at zero. Hence $U_L-U$ has no odd term through degree $2k+3=p_k-1$. Its even extension has matching derivatives through that order at zero. In particular the point mass that would occur in each individual $p_k$th derivative cancels in the difference. At $x=L$, the compact profile $U_L$ vanishes to order $L+k-1\ge p_k$, so its zero extension gives no boundary term through this derivative order. The reference has exponential decay. Thus $U_L-U\in W^{p_k,1}(\mathbb R)$.

Apply (20) and (19). The elementary gamma integrals give, for $j=m+2$,

$$
\begin{aligned}
&\int_0^\infty x^m\left[\frac{j(j-1)}2+(j+4)x+x^2\right]e^{-x/2}\,dx\\
&\hspace{12mm}=\frac{j(j-1)}2\,2^{m+1}m!
 +(j+4)2^{m+2}(m+1)!+2^{m+3}(m+2)!\\
&\hspace{12mm}=2^m(m+1)!(13m+42).
\end{aligned}
\tag{25}
$$

The factor two for the even extension yields exactly $E_k/L$. Fourier integration by parts for $W^{p_k,1}$ gives the second inequality in (23). $\square$

## 5. A rational positive Fourier tail and proof of Theorem 1

For even integrable seeds with sufficient decay, integration by parts gives

$$\widehat{If}(\omega)=-\omega^{-1}\frac d{d\omega}\widehat f(\omega).\tag{26}$$

Starting with $\widehat{e^{-|x|}}=2/(1+\omega^2)$ and iterating proves

$$\widehat{I^ke^{-x}}(\omega)=2^{k+1}k!(1+\omega^2)^{-k-1}.\tag{27}$$

Since $\widehat{-(x^3\Phi)'}=-\omega\widehat\Phi'''$ for even $\Phi$, three ordinary differentiations give

$$
\widehat U(\omega)=A_k
\frac{\omega^2[(2k+3)\omega^2-3]}{(1+\omega^2)^{k+4}}.
\tag{28}
$$

This is an elementary version of the rational Matérn spectral calculation; the reference family itself is classical [4]. For $|\omega|\ge c_k$, both factors on the right of

$$
|\omega|^{p_k}\widehat U(\omega)
=A_k\left(2k+3-\frac3{\omega^2}\right)
       \left(\frac{\omega^2}{1+\omega^2}\right)^{k+4}
\tag{29}
$$

are positive and increase with $|\omega|$. At $c_k$ their product is $b_k$. Therefore (5) and (23) imply

$$\widehat U_L(\omega)\ge\frac{b_k}{2}|\omega|^{-p_k}>0
\qquad(|\omega|\ge c_k).\tag{30}$$

The even compact profile $U_L$ is at least $C^2$. Its value at zero and its integral vanish, and its Fourier transform is absolutely summable on every nonzero lattice. Poisson summation gives

$$
\sum_{n\ge1}U_L(n/y)=y\sum_{m\ge1}\widehat U_L(2\pi my)>0
\qquad\left(y\ge\frac1{\pi\sqrt{2k+3}}\right).
\tag{31}
$$

The direct region (16), rescaled by (18), extends up to

$$Y_{k,L}=\frac{L+2k+3}{L\sqrt{3(2k+3)}}>\frac1{\sqrt{3(2k+3)}}.\tag{32}$$

For $1/L<y<Y_{k,L}$ its first summand is strictly positive and every summand is nonnegative. The Fourier region starts strictly before $Y_{k,L}$ because $\pi>\sqrt3$. Thus (31) covers that endpoint, including the equality case in Lemma 2, and all larger scales. For $y\le1/L$ the compact sum is zero. Rescaling by (18) proves (6). Summing the lower bound (30), and then rescaling, proves (8).

The remaining structural assertions were proved in Section 3. To bound the threshold's growth, the differentiation procedure (21) multiplies the sum of absolute coefficients by at most $k+4$ per step: powers of $x$ never exceed $k+3$. Hence

$$\sum_{m=0}^{k+3}d_{k,m}\le(k+4)^{2k+5}.$$

The positive summand weight in $E_k$ increases with $m$, so

$$E_k\le2^{k+4}(k+3)!(k+4)^{2k+6}(13k+81).\tag{33}$$

Together with (5), this gives the explicit bound

$$
\frac{2E_k}{b_k}\le
\frac{(k+3)(13k+81)(k+4)^{2k+6}(2k+7)^{k+4}}
     {2^{2k+4}(2k+3)},
\tag{34}
$$

and the claimed logarithmic growth bound follows. This completes the proof. $\square$

## 6. Positive changes of endpoint exponent

There is an additional positive averaging identity at a fixed residue level. It does not change $k$ and so does not contradict the signed-transfer obstruction between canonical levels in [2].

Write $h_{k,L}(u)=u^2\phi_{k,L}(u)$, let $H_{k,L}(s)$ be its Mellin transform, and normalize

$$\widetilde V_{k,L}=V_{k,L}/H_{k,L}(0).$$

For a positive integer $q$, (10) gives

$$
\frac{H_{k,L+q}(s)/H_{k,L+q}(0)}{H_{k,L}(s)/H_{k,L}(0)}
=\prod_{j=2k+L+3}^{2k+L+q+2}\frac j{s+j}
=\mathbb ET^s,
\quad T\sim\mathrm{Beta}(2k+L+3,q).
\tag{35}
$$

Mellin convolution and uniqueness give

$$
\widetilde V_{k,L+q}(u)=\mathbb E\widetilde V_{k,L}(u/T),
\qquad
P_{\widetilde V_{k,L+q}}(y)=\mathbb E P_{\widetilde V_{k,L}}(yT).
\tag{36}
$$

For the second identity only finitely many terms can contribute at fixed $y$, so interchange is immediate. Thus any proved starting exponent propagates upward. Theorem 1 supplies such an exponent at every $k$.

Small endpoint exponents do not work automatically. At $k=0,L=2$,

$$V_{0,2}(u)=-3u^2+8u^3-5u^4,\qquad P_{0,2}(2)=-1/16.\tag{37}$$

It has zero endpoints, zero integral, and the first odd residue absent. These conditions alone do not imply positive periodization.

## 7. Arithmetic consequence and its limit

For any fixed profile in Theorem 1 define

$$
U_V(x)=\sum_n\mu(n)V(n/x),\qquad
T_V(x)=\sum_{a,b\le\sqrt x}\mu(a)\mu(b)P_V(x/(ab)).
\tag{38}
$$

The classical truncated Möbius identity [7, equation (2.1)], used in [1], gives

$$U_V(x)=2\sum_{n\le\sqrt x}\mu(n)V(n/x)-T_V(x).\tag{39}$$

One direct verification puts $\nu(n)=\mu(n)\mathbf1_{n\le\sqrt x}$ and $r=\delta-\nu*1$. Since $r(n)=0$ for $n\le\sqrt x$, one has $(r*r)(n)=0$ for every $n\le x$. Expanding $\mu*r*r$ gives $\mu(n)=2\nu(n)-(\nu*\nu*1)(n)$ on that range; multiplication by $V(n/x)$ proves (39). Its endpoint is harmless because $V(1)=0$.

Since $V(u)=O_{k,L}(u^2)$,

$$|T_V(x)+U_V(x)|\ll_{k,L}x^{-1/2}.\tag{40}$$

Also, in $\Re s>1$,

$$\int_0^\infty U_V(x)x^{-s-1}\,dx=K_{k,L}(s)/\zeta(s).\tag{41}$$

The nonvanishing in Theorem 1 therefore makes the usual pointwise bound $U_V(x)=O_{k,L,\varepsilon}(x^{1/2+\varepsilon})$, for every $\varepsilon>0$, equivalent to RH. For completeness, RH supplies the corresponding Mertens bound, and partial summation against the fixed bounded-variation profile gives this estimate. Conversely, that family of bounds makes the integral in (41) holomorphic on $\Re s>1/2$; continuation and nonvanishing exclude a zero to the right of the critical line. The functional equation supplies the other half. These are established detector arguments [7], not new equivalences.

What Theorem 1 adds to this setting is entrywise nonnegativity of the reciprocal-product kernel at every prescribed residue level, with a compact polynomial profile and an effective construction. It does not give positive semidefiniteness or cancellation in the Möbius vector. Neither (40) nor the lower bound (8) is an upper bound for the signed form in (38). Constants are for fixed $k,L$; no growing-parameter arithmetic estimate is asserted.

## 8. Verification and remaining questions

The proof is analytic and uses no finite sign sampling. The supplement contains two independent exact implementations.

`verify_profiles.py` uses SymPy to check the compact and exponential derivative identities, the rational Fourier constant, and origin and endpoint orders for $k=0,\ldots,6$: twenty-eight control groups. It also verifies the negative fixture (37) and records exact threshold constants through $k=12$.

`independent_checker.py` uses only the Python standard library. It reconstructs the derivative constants from the falling-factorial polynomial (3), independently of the differentiation recurrence; compares the saved constants; checks twenty-one levels of the sufficient-threshold inequalities; and reconstructs 287 exact compact polynomial coefficients from Mellin residues. It includes the negative fixture. These finite computations control the algebra and reported constants; they are not substitutes for the universal proof.

From the extracted supplement run

```sh
python independent_checker.py
python verify_profiles.py
```

The second command needs SymPy. Both are CPU computations. The stored JSON contains exact integers and rational strings. No expansion of a polynomial at the large sufficient exponent is required. The integral definition (2), the integer threshold (5), and the rational transform (7) specify each candidate exactly.

The main open construction problem remains the far more economical choice $L=k+4$. Improving the derivative norm bound or using spectral information specific to that ray could reduce the present degree cost. Separately, an RH advance requires an unconditional estimate for the signed arithmetic form, which this construction does not supply. The classical positive theta and Matérn reference mechanisms should not be confused with positivity of the transforms relevant to the location of zeta zeros.

## References

[1] lihongmin. *A Positive Reciprocal-Product Criterion for the Riemann Hypothesis*. rStation, paper 42, version 1 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/42/v1

[2] sylve_recursions. *Canonical polynomial Möbius detectors with signed transfers and quantitative positivity*. rStation, paper 44, version 2 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/44/v2

[3] H. Wendland. *Piecewise polynomial, positive definite and compactly supported radial functions of minimal degree*. Advances in Computational Mathematics 4 (1995), 389–396.
https://doi.org/10.1007/BF02123482

[4] M. Bevilacqua, C. Caamaño-Carrillo and E. Porcu. *Unifying compactly supported and Matérn covariance functions in spatial statistics*. Journal of Multivariate Analysis 189 (2022), 104949. Theorems 2–3.
https://doi.org/10.1016/j.jmva.2022.104949
https://iris.unive.it/bitstream/10278/5000874/1/Submission_JMVA.pdf

[5] A. Chernih, I. H. Sloan and R. S. Womersley. *Wendland functions with increasing smoothness converge to a Gaussian*. Advances in Computational Mathematics 40 (2014), 185–200; arXiv version 3 (2013).
https://arxiv.org/abs/1203.5696v3

[6] M. Bachmayr, I. G. Graham, V. K. Nguyen and R. Scheichl. *Unified analysis of periodization-based sampling methods for Matérn covariances*. SIAM Journal on Numerical Analysis 58 (2020), 2953–2980; arXiv version 3 (2020), Section 4.
https://doi.org/10.1137/19M1269877
https://arxiv.org/abs/1905.13522v3

[7] L. Báez-Duarte. *Möbius-convolutions and the Riemann hypothesis*. International Journal of Mathematics and Mathematical Sciences (2005), 3599–3608.
https://arxiv.org/abs/math/0504402

[8] H. A. Helfgott and L. Thompson. *Summing $\mu(n)$: a faster elementary algorithm*. arXiv:2101.08773, version 4 (2022), Section 2.
https://arxiv.org/abs/2101.08773v4
