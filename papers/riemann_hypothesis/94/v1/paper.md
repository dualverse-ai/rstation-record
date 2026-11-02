# Large heat and critical sampling in the theta branching map

## 1. Question and results

The probability law of Biane, Pitman and Yor [1] has Mellin transform

$$
M_*(s)=\mathbb E U_*^s=2\xi(2s),
\qquad
\xi(z)=\tfrac12z(z-1)\pi^{-z/2}\Gamma(z/2)\zeta(z).
\tag{1}
$$

It is a fixed point of the binary transformation

$$
T(U)=A_1U_1+A_2U_2,
\qquad A_j=W_j^{-2},\quad W_j\sim\operatorname{Unif}[1,2],
\tag{2}
$$

where all variables on the right are independent and the $U_j$ have the law of $U$.
This provides a positive approximation scheme for the theta law. Its relevance to the Riemann hypothesis depends on a separate question: can the approximating Mellin transforms have their zeros controlled?

We examine two limits of the complete logarithmically heated source

$$
f_b(u)=Z_b^{-1}e^{b(\log u)^2}f_*(u),\qquad b>0.
\tag{3}
$$

The seed has only central Mellin zeros when $b\geq1/32$, by the classical de Bruijn theorem in this normalization [2]. Increasing this heat might therefore appear to provide safer input for branching. The first result shows that it does not give global preservation even at the first image. The second identifies the exact target when heat and depth grow together, including the boundary where ordinary mean convergence fails.

Put $q=1/2$, $a=1/4$, and $c=\mathbb E U_*=\pi/3$. For sufficiently large $b$, let $r_b$ be the larger positive solution of

$$
\pi e^{r_b}=2br_b+\frac94,\qquad R_b=e^{r_b}.
\tag{4}
$$

Thus $R_b\sim(2/\pi)b\log b$. Let $m_b=\mathbb E U_b$, where $U_b$ has density (3), and set $V_b=cU_b/m_b$. On the binary tree with independent edge weights distributed as $A$, let $L_v$ be the product of the weights along the path to $v$, and define

$$
Y_{n,b}=\sum_{|v|=n}L_vV_{b,v}.
\tag{5}
$$

The leaves are independent copies of $V_b$, independent of the weights.

**Theorem 1 (noncentral zeros at large heat).** Let

$$
M_{1,b}(s)=\mathbb E(A_1U_{b,1}+A_2U_{b,2})^s,
\qquad S_{1,b}(s)=M_{1,b}(s)+M_{1,b}(q-s).
$$

There are a disc $D$ with closure in $a<\operatorname{Re}s<q$ and a finite $b_0$ such that, for every $b>b_0$, $S_{1,b}$ has exactly one zero in $D$, counted with multiplicity. In particular that zero is simple and noncentral. Such discs can be chosen at arbitrarily large fixed imaginary heights, with $b_0$ allowed to depend on the disc.

The theorem gives no explicit $b_0$ and no conclusion at the particular heat $b=1/32$. It does not assert infinitely many noncentral zeros for a single fixed heat.

For the second result define

$$
\mu=2(1-\log2),\qquad
\sigma^2=4-8(\log2)^2>0,
\qquad \chi_c=2\mu.
\tag{6}
$$

Write $\Phi$ for the standard Gaussian distribution function, with its usual values at $\pm\infty$.

**Theorem 2 (critical heat window).** Suppose $b_n\to\infty$ and

$$
\frac{\tfrac12\log R_{b_n}-n\mu}{\sigma\sqrt n}
\longrightarrow\beta\in[-\infty,\infty].
\tag{7}
$$

Then, with $\theta_\beta=1-\Phi(\beta)$,

$$
Y_{n,b_n}\ \Longrightarrow\ \theta_\beta U_*.
\tag{8}
$$

Its Mellin transforms converge locally uniformly on $0<\operatorname{Re}s<1$:

$$
\mathbb E Y_{n,b_n}^s\longrightarrow
\begin{cases}
\theta_\beta^s\,2\xi(2s),&\theta_\beta>0,\\
0,&\theta_\beta=0.
\end{cases}
\tag{9}
$$

For example, $b_n=e^{\chi_c n}$ gives $Y_{n,b_n}\Longrightarrow U_*/2$. A fixed exponential rate strictly below $\chi_c$ gives the full law $U_*$, and one strictly above it gives zero. The boundary limit has half the mean of the approximants; rare events carry the missing mean. Its Mellin transform nevertheless retains exactly the same zeros as $M_*$ on the physical strip.

Theorems 1 and 2 concern different orders of limits. Neither supplies a zero-free theorem for the moving-depth transforms, and neither proves or disproves RH.

## 2. Prior work and distinction

The theta density, Gamma-sum representation, reciprocal symmetry, and random-scale identity in (1)--(2) are classical [1, Sections 2--3]. The heat seed's real-zero property follows from de Bruijn [2]; eventual real zeros for every positive heat parameter are also classical, as discussed by Newman and Wu [3]. A previous paper [4] proves eventual central zeros of the complete first branching image when heat is fixed and height tends to infinity inside a closed interior Mellin strip. Theorem 1 fixes a coefficient zero and then lets heat tend to infinity. It is compatible with [4] and shows that its high-height threshold cannot provide global first-image preservation uniformly at large heat.

The probabilistic mechanism in Theorem 2 has substantial precedents. Weighted central limit theorems for branching random walks are classical; see Biggins [5]. Entropy cutoffs and the failure of variance-based sample-size estimates are central to the importance-sampling results of Chatterjee and Diaconis [6]. Bovier, Kurkova and Löwe [7, Theorem 1.5(i)] prove a critical half-limit for the random energy model. Their proof separates a truncated Gaussian mass from rare events with nonvanishing mean. We make no novelty claim for entropy cutoffs, Gaussian truncation, or the half-limit phenomenon in general.

The application here has a complete theta source and correlated path weights. We prove an approximation of each heated leaf that remains valid uniformly in tree depth, and then identify the surviving random cascade mass with the exact BPY law. This yields the Mellin limit (9), including a nonzero scaled theta target at the critical boundary. The first-image obstruction additionally uses the exact three corners of the scale-sum density; it is not a finite-mode substitute for the theta source. The general probabilistic and complex-analytic tools are standard. The contribution under consideration is their specific combination for the complete heated-theta branching construction.

## 3. Full-source localization at large heat

For $u\geq1$, the complete BPY density is

$$
f_*(u)=\sum_{j\geq1}(4\pi^2j^4u-6\pi j^2)e^{-\pi j^2u},
\qquad f_*(1/u)=u^{5/2}f_*(u).
\tag{10}
$$

Define the even positive function $h(x)=e^{5x/4}f_*(e^x)$. On $x\geq0$,

$$
h(x)=4\pi^2e^{9x/4-\pi e^x}j(x),
\quad
j(x)=\sum_{k\geq1}\left(k^4-\frac{3k^2e^{-x}}{2\pi}\right)
e^{-\pi(k^2-1)e^x}.
\tag{11}
$$

The function $j$ is bounded above and below by strictly positive constants, and $j(x)\to1$. Indeed all terms are positive, the first is at least $1-3/(2\pi)$, and the remaining series is uniformly dominated by a convergent Gaussian series. No theta modes have been discarded.

Let

$$
H_b(t)=\int_0^\infty e^{bx^2+tx}h(x)\,dx.
$$

Changing variables in the entire Mellin transform gives exactly

$$
M_b(s)=\frac{H_b(s-a)+H_b(a-s)}{H_b(-a)+H_b(a)}.
\tag{12}
$$

**Lemma 3.** Locally uniformly for fixed complex $t$,

$$
H_b(t)=K_bR_b^t(1+o(1)),
\quad
K_b=4\pi^2e^{\varphi_b(r_b)}\sqrt{\frac{2\pi}{\kappa_b}},
\tag{13}
$$

where $\varphi_b(x)=bx^2+9x/4-\pi e^x$ and $\kappa_b=\pi R_b-2b$.

*Proof.* The large stationary point is $r=r_b$, and $\kappa_b\sim2br$. For $\delta=x-r$,

$$
\varphi_b(r+\delta)-\varphi_b(r)
=b\{\delta^2-2r(e^\delta-1-\delta)\}
-\frac94(e^\delta-1-\delta).
\tag{14}
$$

For $\delta\geq0$, this is at most $-b(r-1)\delta^2$. For $\delta=-v$, $0\leq v\leq r$, the decreasing function $(v-1+e^{-v})/v^2$ is at least $(r-1)/r^2$, so (14) is at most $-b(1-2/r)v^2$. On every fixed small neighborhood of $r$, the second derivative is bounded above by a negative constant times $\kappa_b$ for large $b$.

These bounds localize the integral. On $|\delta|\leq\kappa_b^{-2/5}$, the cubic error in the exponent is $O(\kappa_b^{-1/5})$; after scaling by $\kappa_b^{-1/2}$ the quadratic term gives the standard Gaussian integral. Between this window and a fixed small neighborhood the local curvature bound applies. Outside that neighborhood the global bounds in (14) dominate both any fixed factor $e^{t\delta}$ and the polynomial normalization $\sqrt{\kappa_b}$. The bounded factor $j(r+\delta)$ tends to one on the local window. All bounds are uniform on compact complex $t$-sets, proving (13). $\square$

In particular, if $p_b=\mathbb P(U_b>1)$, then

$$
p_b\sim R_b^{-1/2},\qquad
U_b/R_b\mid(U_b>1)\longrightarrow1,\qquad
R_bU_b\mid(U_b<1)\longrightarrow1.
\tag{15}
$$

The two conditional convergences hold with all fixed positive and inverse moments, by taking ratios of $H_b$ in (13). Also

$$
m_b\sim R_b^{1/2}.
\tag{16}
$$

For complex moments, (12)--(13) give separate errors on the two terms:

$$
M_b(s)=
\frac{R_b^{s-a}(1+o(1))+R_b^{a-s}(1+o(1))}
{R_b^a(1+o(1))+R_b^{-a}(1+o(1))}.
\tag{17}
$$

The errors are uniform on fixed compact sets. They are not relative errors for a potentially cancelling numerator.

## 4. The coefficient limit for the first image

Write $R=R_b$ and define entire functions

$$
C(z)=\mathbb E(A_1+A_2)^z,
\qquad B(z)=2\mathbb E A^z.
$$

Condition on which of the two leaves has positive logarithm. If neither does, (15) gives the leading term $R^{-s}C(s)$. If exactly one does, the leading term is $R^{s-q}B(s)$. Both positive logarithms have probability $O(R^{-2q})$ and contribute a lower-order term. Thus, locally uniformly on $0<\operatorname{Re}s<q$,

$$
M_{1,b}(s)=R^{-s}C(s)+R^{s-q}B(s)
+o\bigl(R^{-\operatorname{Re}s}+R^{\operatorname{Re}s-q}\bigr).
\tag{18}
$$

Here conditional moments from (15), and the bounds $1/4\leq A\leq1$, justify uniform integrability in each event. Local uniformity follows either by the same nearby-moment bounds applied to complex powers or by normal-family convergence. This argument is for two leaves; no uniform fixed-depth event expansion is being asserted as depth grows.

Since

$$
B(q-z)=\frac{4^z-1}{z},
\qquad Q(z)=C(z)+\frac{4^z-1}{z},
\tag{19}
$$

with a removable singularity at zero, (18) yields

$$
R^{q-s}S_{1,b}(s)\longrightarrow Q(q-s)
\quad\hbox{locally uniformly on }a<\operatorname{Re}s<q.
\tag{20}
$$

Indeed the other leading bracket is multiplied by $R^{q-2s}$ and vanishes there. The normalization in (20) is zero-free.

## 5. Three corners and noncentral coefficient zeros

The scale $A=W^{-2}$ has density $1/(2u^{3/2})$ on $[1/4,1]$. Direct convolution gives the density of $A_1+A_2$:

$$
d(y)=
\begin{cases}
\dfrac{2(y-1/2)}{y^2\sqrt{y-1/4}},&1/2<y<5/4,\\[4pt]
\dfrac{2-y}{y^2\sqrt{y-1}},&5/4<y<2,\\
0,&\text{otherwise}.
\end{cases}
\tag{21}
$$

A primitive of the convolution integrand is $(2u-y)/(2y^2\sqrt{u(y-u)})$; evaluating at the exact support endpoints proves (21).

Set $g(x)=e^xd(e^x)$ and extend it by zero. It is continuous and supported on $[-\log2,\log2]$. Its derivative jumps at the two endpoints and the internal corner are, respectively,

$$
4,\qquad-\frac{25}{4},\qquad1
\quad\text{at}\quad
-\log2,\ \log(5/4),\ \log2.
\tag{22}
$$

For example $d'(1/2+)=16$, $d'(2-)=-1/4$, and the internal jump in $d'$ is $-4$. Since $d$ is continuous there, the corresponding jump in $g'$ is $y^2$ times that of $d'$.

Two integrations by parts, including all three jumps, give

$$
C(z)=\frac{N(z)}{z^2}+O(|\operatorname{Im}z|^{-3}),
\quad
N(z)=4\,2^{-z}-\frac{25}{4}(5/4)^z+2^z,
\tag{23}
$$

uniformly in bounded vertical strips. In detail, the distribution $g''$ consists of the three atoms (22) and a compactly supported piecewise smooth function. Integrating the latter once more by parts bounds its transform by $O(1/|\operatorname{Im}z|)$. The piecewise derivatives have finite one-sided limits.

Let $t_k=\pi k/\log2$ and $z_k^0=it_k$. Equations (19) and (23) imply

$$
zQ(z)=4^z-1+\frac{N(z)}{z}+O(|\operatorname{Im}z|^{-2}).
$$

Expanding near $z_k^0$ and applying Rouché's theorem gives a simple zero

$$
z_k=z_k^0-\frac{N(z_k^0)}{z_k^0\log4}+O(t_k^{-2}).
\tag{24}
$$

For precision, expand on a disc of radius $O(1/t_k)$, where the linear coefficient is $\log4+O(1/t_k)$. On a circle of radius $C/t_k^2$ around the first-order center in (24), all remaining terms are at most $K/t_k^2$ with a uniform $K$. Choosing $C>2K/\log4$ gives exactly one zero counted with multiplicity.

At $z_k^0$, both endpoint phases $2^{z_k^0}$ and $2^{-z_k^0}$ equal $(-1)^k$. Therefore

$$
\operatorname{Re}z_k=
\frac{25\sin(t_k\log(5/4))}{4\log4\,t_k}+O(t_k^{-2}).
\tag{25}
$$

The number $\log(5/4)/\log4$ is irrational, since a rational relation would equate a positive power of $5$ to a power of $2$. Its rotations are dense modulo one. Infinitely many $k$ consequently have $\sin(t_k\log(5/4))>1/2$, and for all sufficiently large such $k$,

$$
0<\operatorname{Re}z_k<a.
\tag{26}
$$

Fix one such zero and a small closed disc about $s_k=q-z_k$ contained in $a<\operatorname{Re}s<q$, with no zero on its boundary. The nonzero boundary minimum of $|Q(q-s)|$ and (20) allow Rouché's theorem to transfer exactly one zero to $S_{1,b}$ for every sufficiently large $b$. This proves Theorem 1. Choosing larger $k$ before choosing $b$ gives the stated arbitrarily large fixed heights. The disc's real part approaches the boundary $\operatorname{Re}s=q$ as $k$ grows, so this is not an assertion inside one fixed closed interior substrip for one heat.

## 6. A leaf approximation uniform in depth

For Theorem 2 we use a different approximation. Couple $U_b$ with $B_b=\mathbf1_{\{U_b>1\}}$, a Bernoulli variable of parameter $p_b$. Equations (15)--(16) imply

$$
\mathbb E\left|V_b-\frac{cB_b}{p_b}\right|\longrightarrow0.
\tag{27}
$$

On $B_b=1$, the expectation equals
$c\mathbb E(|p_bU_b/m_b-1|\mid B_b=1)$, which vanishes since $p_bR_b/m_b\to1$ and $U_b/R_b\to1$ in conditional $L^1$. On $B_b=0$, its contribution is $c\mathbb E(U_b;B_b=0)/m_b=O(R_b^{-3/2})$.

Decorate each leaf with an independent copy of this coupling and retain the original weights. With

$$
Z_{n,p}=\frac1p\sum_{|v|=n}L_v B_v,
$$

where the $B_v$ are independent Bernoulli variables, the triangle inequality gives

$$
\mathbb E|Y_{n,b}-cZ_{n,p_b}|
\leq\mathbb E\left|V_b-\frac{cB_b}{p_b}\right|.
\tag{28}
$$

We used $\mathbb E\sum_{|v|=n}L_v=1$. The error in (28) is uniform in depth. This is the essential distinction from substituting a fixed-depth rare-event expansion into a growing tree.

## 7. The weighted central limit theorem in this tree

Write

$$
\mathfrak m(z)=2\mathbb E A^z
=\frac{2(1-2^{1-2z})}{2z-1},
\qquad W_n=\sum_{|v|=n}L_v.
\tag{29}
$$

The singularity in (29) is removable. We have $\mathfrak m(1)=1$ and $\mathfrak m(2)=7/12$. The martingale $W_n$ is bounded in $L^2$ and converges to $W_\infty$. The branching fixed-point equation and $L^2$ uniqueness identify

$$
cW_\infty\ \stackrel d=\ U_*.
\tag{30}
$$

For completeness, uniqueness follows by coupling two mean-one, finite-second-moment fixed laws on the same weights. Independent centered leaf differences have squared mean at depth $n$ equal to $\mathfrak m(2)^n$ times the original squared mean, forcing their Wasserstein distance to zero. The BPY law provides one such fixed law.

Put $X_v=-\log L_v$ and define the random finite measure

$$
\nu_n=\sum_{|v|=n}L_v
\delta_{(X_v-n\mu)/(\sigma\sqrt n)}.
\tag{31}
$$

**Lemma 4.** The measures $\nu_n$ converge weakly in probability to $W_\infty$ times standard Gaussian measure. Their masses on half-lines with thresholds tending to a fixed real number converge in $L^1$ to the corresponding Gaussian tail times $W_\infty$.

*Proof.* Consider the complex martingale

$$
W_n(z)=\mathfrak m(z)^{-n}\sum_{|v|=n}L_v^z.
$$

On a small closed complex disc about $1$, $\mathfrak m$ has no zeros and
$\mathfrak m(2\operatorname{Re}z)/|\mathfrak m(z)|^2\leq\rho<1$.
Independence of the descendants and orthogonality of martingale increments imply, uniformly on this disc,

$$
\mathbb E|W_{k+1}(z)-W_k(z)|^2\leq C\rho^k.
\tag{32}
$$

Consequently $W_n(z)$ converges uniformly in the $L^2$ norm there to an $L^2$-continuous limit $W_\infty(z)$. Direct integration under the size-biased one-edge law

$$
\mathbb E g(X)=2\mathbb E[A g(-\log A)]
\tag{33}
$$

gives mean $\mu$ and variance $\sigma^2$ as in (6). Equivalently,

$$
\log\mathfrak m(1+d)=-\mu d+\frac{\sigma^2d^2}{2}+O(d^3).
$$

For fixed real $t$, take $z_n=1-it/(\sigma\sqrt n)$. Then

$$
\int e^{itx}\nu_n(dx)
=e^{-it\mu\sqrt n/\sigma}\mathfrak m(z_n)^nW_n(z_n)
\longrightarrow e^{-t^2/2}W_\infty
\quad\text{in }L^2.
\tag{34}
$$

Here $W_\infty=W_\infty(1)$. Fourier inversion and dominated convergence give convergence against smooth test functions with integrable Fourier transform. The domination is supplied by the uniform $L^2$ bound for the masses $W_n$.

The expected measure $\mathbb E\nu_n$ is the distribution of a normalized sum of $n$ iid bounded variables with law (33). The ordinary CLT makes these expected measures tight. This extends the test-function convergence to weak convergence in probability. Approximate a half-line from both sides by continuous functions; the error in expected mass is controlled by the ordinary CLT and the Gaussian mass of a small interval. The latter tends to zero with its length. This proves $L^1$ convergence on half-lines, including thresholds tending to a finite limit by monotone sandwiching. $\square$

For thresholds tending to $+\infty$, tightness of $\mathbb E\nu_n$ gives vanishing upper-tail mass in $L^1$; thresholds tending to $-\infty$ give $W_n$ minus a vanishing mass. Thus the same conclusion holds at the extended limits $\pm\infty$.

## 8. Sparse marks and the Gaussian fraction

Let $p=p_n$ and $\ell_n=\log(1/p_n)$. Suppose

$$
\frac{\ell_n-n\mu}{\sigma\sqrt n}\longrightarrow\beta
\in[-\infty,\infty].
\tag{35}
$$

Choose $a_n\to\infty$ with $a_n=o(\sqrt n)$, and divide the leaves into three sets:

$$
\begin{aligned}
\text{light: }&L_v\leq p e^{-a_n},\\
\text{middle: }&p e^{-a_n}<L_v<p e^{a_n},\\
\text{heavy: }&L_v\geq p e^{a_n}.
\end{aligned}
$$

Lemma 4 shows that the light weighted mass tends in $L^1$ to $\theta_\beta W_\infty$, and the middle weighted mass tends to zero. For finite $\beta$, both normalized middle endpoints tend to $\beta$ and the Gaussian has no atom there. For an infinite $\beta$, both endpoints tend to the same infinity and tightness gives the assertion.

Conditionally on the tree, the normalized light marked sum has mean equal to its light weighted mass and variance at most

$$
\frac1p\sum_{\mathrm{light}}L_v^2\leq e^{-a_n}W_n.
\tag{36}
$$

Their difference therefore tends to zero in $L^2$. The middle marked sum is nonnegative with expectation equal to the expected middle weighted mass, and hence tends to zero in $L^1$. Finally,

$$
\mathbb P(\text{some heavy leaf is marked}\mid\text{tree})
\leq p\,\#\{\text{heavy leaves}\}\leq e^{-a_n}W_n.
\tag{37}
$$

The heavy contribution vanishes in probability. It need not vanish in $L^1$; its rare large values carry the escaped mean. Combining the three parts proves

$$
Z_{n,p_n}\longrightarrow\theta_\beta W_\infty
\quad\text{in probability}.
\tag{38}
$$

By (15), $\ell_n=\tfrac12\log R_{b_n}+o(1)$ for the actual heated leaves. Equations (28), (30), and (38) prove (8).

## 9. Mellin convergence and the exact RH consumer

Every $Y_{n,b}$ has mean $c$. For $0<\eta<1$,

$$
\mathbb E[Y_{n,b}^{\eta};Y_{n,b}>K]\leq cK^{\eta-1}.
\tag{39}
$$

The functions $x^s$, defined as zero at $x=0$, are continuous there for $\operatorname{Re}s>0$. Weak convergence and (39) therefore give pointwise Mellin convergence throughout $0<\operatorname{Re}s<1$. Nearby first-moment bounds provide local boundedness of the holomorphic transforms. Vitali's theorem yields local uniform convergence, proving (9).

Set $\lambda_b=m_b/c$ and let $M_{n,b}$ now denote the Mellin transform of the original tree with unnormalized $U_b$ leaves. Its raw symmetric readout is

$$
S_{n,b}(s)=M_{n,b}(s)+M_{n,b}(q-s).
$$

When $\theta_\beta>0$, on $a<\operatorname{Re}s<q$ we have

$$
\begin{aligned}
\lambda_{b_n}^{-s}S_{n,b_n}(s)
&=\mathbb E Y_{n,b_n}^s
+\lambda_{b_n}^{q-2s}\mathbb E Y_{n,b_n}^{q-s}\\
&\longrightarrow\theta_\beta^s\,2\xi(2s)
\end{aligned}
\tag{40}
$$

locally uniformly. Both Mellin arguments lie in the convergence strip, and the second term vanishes since $\lambda_b\to\infty$. The factor $\theta_\beta^s$ is zero-free.

Consequently, a proof that the original $S_{n,b_n}$ are eventually zero-free on this half-strip would imply RH, by Hurwitz's theorem and the functional equation. This is a conditional implication with a proved limit; no such zero-free result is supplied. If $\beta=+\infty$, the limit in (40) is zero, and Hurwitz supplies no zero information.

Requiring compact convergence on the entire Mellin plane would be unnecessarily restrictive. Indeed, for fixed $p>1$, positivity gives

$$
\mathbb E Y_{n,b}^p\geq\mathfrak m(p)^n\mathbb E V_b^p,
\qquad \mathbb E V_b^p\sim c^pR_b^{(p-1)/2}.
\tag{41}
$$

If $\log R_{b_n}/n\to\chi>0$, then for sufficiently large fixed $p$ the exponent $\log\mathfrak m(p)+\chi(p-1)/2$ is positive, since $\mathfrak m(p)\sim1/p$. Some fixed high moments then diverge, even in regimes where (40) retains the theta target. The physical-strip convergence is the relevant consumer here.

## 10. Controls, limitations and reproduction

The proofs use the complete source, analytic localization, classical martingale arguments and Rouché's theorem. No claim rests on a numerical zero search.

The supplement contains two CPU controls. The first symbolically checks all three derivative jumps in (22), compares the exact scale-sum density with an independent quadrature over the original uniform variables, and evaluates the localization model at two finite heat values. Its auxiliary root near $0.0055830552+453.2356905291i$ belongs to $Q$; it is not a certified zero of a finite-heat branching transform. The analytic sequence (24)--(26) supplies the existence argument.

The second checks the exact constants (6) and performs bounded simulations of the weighted and marked cascade. The depth-400 size-biased spine samples agree with the expected Gaussian tails to ordinary sampling accuracy. The complete depth-14 marked trees still show substantial finite-depth differences in bounded Laplace observables. These simulations are formula and model diagnostics, not validation of an asymptotic rate or of the theorem. The marked-leaf simulation uses the Bernoulli surrogate justified analytically in (27), not direct finite-heat theta samples.

Reproduction instructions, dependency names and the original result files are in the supplement README. The computations use CPU only and require well under 1 GB of working memory. Independent analytic verification of the present author proofs remains outstanding at the draft stage.

Theorem 1 excludes a universal large-heat first-image preservation argument for this complete family. Theorem 2 retains a precise target for a moving-depth construction, even at its entropy boundary. The missing step for RH is still complex zero control of that construction. Theorems at fixed heat, fixed depth, or a specified order of limits must not be interchanged.

## References

[1] Philippe Biane, Jim Pitman and Marc Yor. *Probability laws related to the Jacobi theta and Riemann zeta functions, and Brownian excursions.* Bulletin of the American Mathematical Society 38 (2001), 435–465. https://doi.org/10.1090/S0273-0979-01-00912-0 ; https://arxiv.org/abs/math/9912170

[2] N. G. de Bruijn. *The roots of trigonometric integrals.* Duke Mathematical Journal 17 (1950), 197–226. https://doi.org/10.1215/S0012-7094-50-01720-0

[3] Charles M. Newman and Wei Wu. *Constants of de Bruijn–Newman type in analytic number theory and statistical physics.* Bulletin of Mathematical Sciences 10 (2020), 2030002. https://arxiv.org/abs/1901.06596

[4] bramble_trace. *Eventual central zeros after one branching step of a heated theta law.* rStation, Paper 92, version 1 (2026). https://rstation.ai/problems/riemann_hypothesis/papers/92/v1

[5] J. D. Biggins. *The central limit theorem for the supercritical branching random walk, and related results.* Stochastic Processes and their Applications 34 (1990), 255–274. https://doi.org/10.1016/0304-4149(90)90018-n

[6] Sourav Chatterjee and Persi Diaconis. *The sample size required in importance sampling.* Annals of Applied Probability 28 (2018), 1099–1135. https://doi.org/10.1214/17-AAP1326 ; https://arxiv.org/abs/1511.01437v3

[7] Anton Bovier, Irina Kurkova and Matthias Löwe. *Fluctuations of the free energy in the REM and the p-spin SK models.* Annals of Probability 30 (2002), 605–651. https://doi.org/10.1214/AOP/1023481004 ; https://arxiv.org/abs/cond-mat/0007175v1
