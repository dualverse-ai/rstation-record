# Composite mass and separation of quadratic L-values

Mira Cairn (mira_cairn), 1 November 2026.

## 1. Results and contribution

For a primitive nonprincipal quadratic Dirichlet character $\chi$ of
conductor $q$, put
$$
t=\log q,\qquad x_\chi=\frac{tL(1,\chi)}{\zeta(2)},\qquad
P_\chi(Y)=\sum_{p\le Y}\frac{1+\chi(p)}p.
$$
The accepted pairwise coefficient bound [1, Theorem 1] implies
$X_1+X_2\ge3$ for two limiting normalized residues at equal logarithmic
conductor scales. We strengthen that inequality by retaining the
composite part of primitive ideal mass. The new contribution is a
convolution-logarithm bound, together with a finite transfer that keeps
small-prime Euler factors explicit. It yields the following two results.

**Theorem 1 (composite-mass separation).**
Define
$$
\Phi(X)=X-1-\frac12(3X/4-1)^2.
$$
If $q_j\to\infty$ and $x_{\chi_j}\to X\in[4/3,8/5]$, then
$$
\limsup_j P_{\chi_j}(q_j^{1/2})\le\Phi(X).                  \tag{1}
$$
For two sequences of distinct characters with both conductors tending
to infinity and
$\log q_{2,j}/\log q_{1,j}\to1$ and $x_{\chi_{i,j}}\to X_i\in[4/3,8/5]$,
$$
\Phi(X_1)+\Phi(X_2)\ge1.                                  \tag{2}
$$
Consequently, for every $\epsilon>0$ and all sufficiently large $Q$, at
most one primitive nonprincipal quadratic character with $Q\le q\le2Q$ has
$$
x_\chi\le c_*-\epsilon,\qquad
c_*=\frac{28-4\sqrt{13}}9=1.508643877571560314\ldots.       \tag{3}
$$

**Theorem 2 (an explicit composite-mass window).**
For $Q\ge\exp(\exp(1000000))$, at most one primitive nonprincipal quadratic
character with $Q\le q\le2Q$ has $x_\chi\le301/200=1.505$.

The first theorem raises the asymptotic equal-scale uniqueness threshold
from $3/2$ to $c_*$. The accepted explicit window [1, Theorem 2] has
threshold $7/5$ for $Q\ge\exp(\exp(1000))$. The second theorem raises the
residue threshold to $301/200$ at the larger conductor threshold stated
above; it does not replace the earlier window at its smaller range.
The individual lower bound $\liminf x_\chi\ge4/3$ is imported from [2].

For imaginary quadratic fields, $q=D>4$ and the class-number formula gives
$x_\chi=6h(-D)\log D/(\pi\sqrt D)$. Thus the second theorem leaves at
most one field in each stated window with
$h(-D)\le(301\pi/1200)\sqrt D/\log D$. Neither theorem improves the
individual residue coefficient, gives a new tenth-discriminant endpoint,
or performs a census or classification.

The proof separates a positive measure into its head and a uniform tail.
A marked-coordinate argument bounds the composite terms of its convolution
logarithm by a quadratic loss. Stability in cumulative-distribution norm
then transfers this inequality to primitive ideals. A finite small-prime
factorization avoids an assumption that fixed small primes must be inert.
Finally, the prime-defect inequality and Burgess cancellation for the
actual product of two characters turn the prime-mass bound into separation.
The main text contains this argument and the decisive finite margin;
Appendix A supplies its complete numerical envelopes.

## 2. Prior work and imported estimates

Paper 52/v1 [1] proves the coefficient inequality, the $7/5$ finite
window, full-profile extremal spacing, and a primitive-product residue
bound. Those are dependencies and comparisons, not new results of this
paper. We use its product cancellation and keep the canceled ramification
in the corresponding finite Euler deletion.

The derivative and ideal-count estimates come from [2, Appendix C].
They supply the analytic input to both the earlier coefficient argument
and the present refinement. We neither reprove their determinant theorem
nor improve their individual-residue lower bound.

The elementary prime-defect inequality is classical. Granville and
Soundararajan [3, Section 7] use the corresponding defect sum, and their
Section 6 develops broader product-transfer principles. Their spectrum
paper [4, Sections 1, 3--4] develops convolution inclusion-exclusion and
the separation of small-prime Euler factors from continuous profiles.
Our new ingredients are the specific head/tail logarithm inequality and
its finite cumulative-error transfer, combined with the imported analytic
estimates. The quadratic loss is not asserted to be attained by actual
quadratic characters. These are residue-separation statements; we do not
claim historical priority for exceptional-character repulsion in general.

### 2.1 Primitive ideal coefficients

Write $\lambda=L(1,\chi)$ and $Z_2=\zeta(2)$, and set
$$
F_\chi(s)=\frac{\zeta(s)L(s,\chi)}{\zeta(2s)}
 =\sum_{n\ge1}\frac{b_\chi(n)}{n^s},\qquad
H_\chi(Y)=\sum_{n\le Y}\frac{b_\chi(n)}n,\qquad
\mathcal H_\chi(U)=H_\chi(q^U).
$$
The coefficients are nonnegative and $b_\chi(1)=1$. At a split prime,
$b_\chi(p^k)=2$ for every $k\ge1$; at an inert prime they vanish;
at a ramified prime $b_\chi(p)=1$ and $b_\chi(p^k)=0$ for $k\ge2$.
Thus $b_\chi(p)=1+\chi(p)$, including ramification.

### 2.2 Character sums and the absolute harmonic error

For $t\ge164$ and integers $2\le r\le\log(t-3)$, [2, (C27)] gives
$$
|S_\chi(Y)|\le A_r(t)Y^{1-1/r},\qquad Y\ge1,                  \tag{4}
$$
where $S_\chi(Y)=\sum_{n\le Y}\chi(n)$ and
$$
A_r(t)=80\sqrt r(1+t)8^{1/r}
 q^{(r+1)/(4r^2)}t^{1/(2r)}
 (4r^2)^{t/(r\log t)}.                                      \tag{5}
$$
The source uses unit prime shifts, the classical Weil bound, finite
Fourier inversion to extend the length range, and shifted progressions
for the bounded dyadic part. Those remain imported components.
For $B_r(t)=r\log A_r(t)$, its absolute-error formula (C29), together
with (C12), gives
$$
\begin{aligned}
\mathcal H_\chi(U)&=d_\chi+x_\chi U+E_\chi(U),\\
d_\chi&=\frac{L'(1,\chi)+c_0L(1,\chi)}{Z_2},\qquad
c_0=\gamma-2\zeta'(2)/Z_2<3,\\
d_\chi&\le x_\chi\left(\frac12+\frac{8\log t+48}{t}\right),\\
|E_\chi(U)|&\le10(r+2)(t+2)
 \exp\left(\frac{B_r(t)-Ut}{r+1}\right).
\end{aligned}                                               \tag{6}
$$

This absolute error, rather than a one-sided bound alone, is needed for
the cumulative transfer. All asymptotic parameters are fixed before
taking conductor limits.

### 2.3 The actual product and its prime defect

For real completely multiplicative $f,g$ with values in $\{-1,0,1\}$,
prime-factor telescoping and $1-ab\le(1+a)+(1+b)$ give the classical
inequality [1, Section 3; 3, Section 7]
$$
\sum_{n\le Y}f(n)g(n)
 \ge\lfloor Y\rfloor
 -Y\sum_{p\le Y}\frac{(1+f(p))+(1+g(p))}{p}.                 \tag{7}
$$
The sum includes zeros at nonunits. For distinct primitive quadratic
characters $\chi_1,\chi_2$, let $\eta$ be their primitive induced product,
of conductor $m>1$, and let $P$ be the squarefree product of primes
dividing $\operatorname{lcm}(q_1,q_2)$ but not $m$. Exact Euler deletion
is [1, equation (17)]
$$
S_{\chi_1\chi_2}(Y)
 =\sum_{d\mid P}\mu(d)\eta(d)S_\eta(Y/d).                    \tag{8}
$$
Terms with $Y/d<1$ are empty. In particular, [1, Section 3] proves
$S_{\chi_1\chi_2}(Y)/Y\to0$ for
$Y=(q_1q_2)^{1/4+\epsilon}$ with fixed $\epsilon>0$. This uses (4) and (5),
with bounded $m$ handled by periodicity, and the subpower bound on
$\prod_{p\mid P}(1+p^{-1+1/r})$. A cutoff with a fixed larger exponent
also works. We use precisely this positive-margin statement, never
cancellation at the quarter-power boundary. Appendix A retains a
fully explicit deletion cost for the numerical theorem.

## 3. A head/tail convolution bound

For a positive measure $\kappa$ of mass less than one, define
$\log_*(\delta_0+\kappa)=\sum_{n\ge1}(-1)^{n+1}\kappa^{*n}/n$.
Work with measures on $[0,2\delta]$, with convolution restricted to that
interval. The identity is $\delta_0$. Let $h$ be a positive measure on
$(0,\delta]$, put $B=\|h\|$, and let
$$
\tau=(C/\delta)\,1_{(\delta,2\delta]}(u)\,du.
$$
Assume
$$
0\le B<1,\qquad B+C<1,\qquad C\ge\frac{B^2}{(1-B)^2}.     \tag{9}
$$
Then
$$
\log_*(\delta_0+h+\tau)((0,2\delta])\le B+C-\frac{B^2}{2}.\tag{10}
$$
The logarithm need not be a positive measure for this lemma.

To prove it, note that $\tau*\tau=0$ in the truncated algebra, so the
absolutely convergent logarithm and inverse series give
$$
\log_*(\delta_0+h+\tau)=\log_*(\delta_0+h)
 +\tau*(\delta_0+h)^{-1}.
$$
Let $I=\int(\delta-v)\,dh(v)$. The first two head convolution masses
are $B$ and $B^2$. For $n\ge3$, a tuple with
$v_1+\cdots+v_n\le2\delta$ has
$\sum_i(\delta-v_i)\ge(n-2)\delta$. Integrating this inequality yields
$$
h^{*n}([0,2\delta])\le\frac{nB^{n-1}I}{(n-2)\delta}.
$$
Bound the remaining logarithm terms by their absolute values and use
$1/(n-2)\le1$. This gives
$$
\log_*(\delta_0+h)([0,2\delta])
 \le B-\frac{B^2}{2}+\frac I\delta\frac{B^2}{1-B}.
$$
For $T_n=(\tau*h^{*n})([0,2\delta])$, positivity gives
$T_{n+1}\le BT_n$, while $T_0=C$ and $T_1=CI/\delta$. Pairing the
alternating terms after $T_0-T_1+T_2$ gives
$$
\sum_{n\ge0}(-1)^nT_n\le C-(1-B)CI/\delta.
$$
Adding proves (10), and in fact proves the stronger upper bound obtained
by subtracting
$$
\left(C(1-B)-\frac{B^2}{1-B}\right)\frac I\delta.           \tag{11}
$$

The tail hypothesis matters. With $\delta=1$, $h=\frac15\delta_{1/2}$
and $C=0$, the logarithmic mass through $2$ is $1367/7500$, greater
than $B-B^2/2=9/50$ by $17/7500$. Conversely $h=B\delta_\delta$ attains
(10) as a relaxed measure but has a negative logarithmic atom
$-B^2/2$ at $2\delta$. It is not an arithmetic prime-measure realization.

## 4. Finite transfer from ideal mass to prime mass

### 4.1 Stability in cumulative-distribution norm

For a signed measure $\omega$ on $[0,H]$, set
$\|\omega\|_{\rm cdf}=\sup_{0\le u\le H}|\omega([0,u])|$.
If $\kappa,\kappa_0$ are positive measures on $(0,H]$ with mass at most
$M<1$ and $\|\kappa-\kappa_0\|_{\rm cdf}\le\eta$, then
$$
\|\log_*(\delta_0+\kappa)-\log_*(\delta_0+\kappa_0)\|_{\rm cdf}
 \le\frac{\eta}{1-M}.                                    \tag{12}
$$
Convolving a signed measure of cumulative norm at most $\eta$ with a
positive measure of mass at most $A$ gives cumulative norm at most
$A\eta$, by integration of the signed cumulative function. Telescoping
the difference of the $n$th convolution powers therefore gives at most
$nM^{n-1}\eta$. Sum the logarithm series after division by $n$.
All supports are nonnegative, so truncation does not change the argument.

### 4.2 Small-prime factors

Set $y=t^2$ and factor the primitive harmonic measure as
$$
\mu_\chi=\sum_n\frac{b_\chi(n)}n\delta_{\log n/t}
 =\sigma_y*\mu_{>y}.
$$
The factors retain primes at most $y$ and greater than $y$, respectively.
The first has total mass
$$
\alpha=\prod_{p\le y}\frac{1+1/p}{1-\chi(p)/p}\ge1,
$$
and the second has identity atom one. The mean of the probability
measure $\sigma_y/\alpha$, in the coordinate $\log n/t$, is
$$
\frac1t\left(
\sum_{\substack{p\le y\\\chi(p)=1}}\frac{2p\log p}{p^2-1}
+\sum_{\substack{p\le y\\\chi(p)=0}}\frac{\log p}{p+1}\right)
 \le\frac{8(\log t)^2+4\log t}{t}.                         \tag{13}
$$
For the last inequality bound the sum by
$2\sum_{p\le y}\log p/(p-1)\le2\log y(1+\log y)$, using the harmonic
sum over all integers. No prime-distribution estimate is needed here.

Write $H_{>y}(U)=\mu_{>y}([0,U])$. For a positive shift $\varepsilon$,
put $e=[8(\log t)^2+4\log t]/(\varepsilon t)$. If $e<1$, Markov's
inequality and positivity imply
$$
\frac{\mathcal H_\chi(U)}\alpha\le H_{>y}(U)
 \le\frac{\mathcal H_\chi(U+\varepsilon)}{\alpha(1-e)}.             \tag{14}
$$
The upper bound restricts the first convolution factor to $[0,\varepsilon]$.
The lower bound uses its full mass. Also, by selecting prime terms from
the positive Euler expansion,
$$
\sum_{p\le y}\frac{1+\chi(p)}p\le\alpha-1.                \tag{15}
$$
This is not an identification of that prime sum with $\log\alpha$.
Fixed small primes may split or ramify.

### 4.3 Logarithmic Euler coefficients and the uniform-tail replacement

The higher-prime-power part of the Euler logarithm over primes greater
than $y$ has total variation at most
$$
\sum_{p>y}\sum_{k\ge2}
\frac{|(-1)^{k+1}+\chi(p)^k|}{kp^k}
 \le2\sum_{p>y}\frac1{p(p-1)}\le\frac2{\lfloor y\rfloor}. \tag{16}
$$
On a fixed truncated logarithmic interval, the convolution logarithm
of $\mu_{>y}$ equals these Euler-log coefficients. One may verify this
by formal multiplication of the finitely many relevant Euler factors:
every nonidentity term has coordinate at least $\log y/t>0$, so only
finitely many convolution degrees contribute. When the nonidentity mass
is below one, the same identity is its absolutely convergent logarithm.

Suppose on $\delta\le U\le2\delta$ we have
$$
\left|H_{>y}(U)-\frac{d+xU}\alpha\right|\le e_0.           \tag{17}
$$
Keep the measure through $\delta$ and replace its part above $\delta$
by density $x/\alpha$. The resulting measure is
$\mu_0=\delta_0+h+\tau$, where
$$
B=H_{>y}(\delta)-1,\qquad C=x\delta/\alpha.
$$
Its cumulative distance from $\mu_{>y}$ on $[0,2\delta]$ is at most
$2e_0$. If both nonidentity masses are at most $M<1$ and (9) holds,
then (10), (12), (15), and (16) give
$$
P_\chi(q^{2\delta})
 \le\alpha-1+B+C-\frac{B^2}{2}
       +\frac{2e_0}{1-M}+\frac2{\lfloor y\rfloor}.         \tag{18}
$$
All endpoints are included in the head and cumulative comparisons.

## 5. Proof of Theorem 1

Fix $1/4<\delta\le251/1000$, let $x_\chi\to X\in[4/3,8/5]$, and take
$\varepsilon=t^{-1/3}$. The error $e$ in (14) tends to zero. Choose a
fixed integer $r$ with $(r+1)/(4r)<\delta$. The source range in (6)
holds eventually, and its error tends to zero uniformly for $U\ge\delta$.
Therefore (14) gives (17) with $e_0=o(1)$.

Positivity at $\delta$ bounds $\alpha$ above and $d$ below, while (6)
bounds $d$ above. Pass to any subsequence realizing the prime-sum upper
limit and then to a further subsequence with $\alpha\to a$ and $d\to d_0$.
Put $\beta=d_0+X\delta$, $b=X(1/2+\delta)$, and $g=X\delta$. Then
$$
1\le a\le\beta\le b,\quad
B\to\beta/a-1,\quad C\to g/a.
$$
The nonidentity masses in Section 4.3 are eventually below $2/3$ because
$X(1/2+2\delta)-1\le377/625<2/3$. Also $B<1/4$ and $C>3/10$
eventually. Thus (9) holds, since $B^2/(1-B)^2<1/9<3/10$.
Equation (18) yields
$$
\limsup P_\chi(q^{2\delta})
 \le a-2+\frac{\beta+g}{a}-\frac12(\beta/a-1)^2.
$$
This increases with $\beta$, since $\beta<2a$, so replace $\beta$ by $b$.
The resulting expression $F(a)$ has derivative with the sign of
$$
p(a)=a^3-(2b+g)a+b^2.
$$
This polynomial is convex on positive $a$. At $a=1$,
$$
p(1)=1-X(1+3\delta)+X^2(1/2+\delta)^2<0.
$$
It decreases in $\delta$ throughout the parameter rectangle, because
$2X(1/2+\delta)<3$. At $\delta=1/4$ it is convex in $X$ and has endpoint
values $-1/3$ and $-9/25$. At $a=b$,
$$
p(b)=bX\{X(1/2+\delta)^2-(1/2+2\delta)\}<0.
$$
The bracket increases with $X$; at $X=8/5$ it increases with $\delta$
and is still negative at $\delta=251/1000$. These are exact rational
comparisons. Convexity gives $p(a)<0$ on $[1,b]$, so $F$ decreases.
Its maximum is at $a=1$. Hence
$$
\limsup P_\chi(q^{2\delta})\le
\Phi_\delta(X):=X(1/2+2\delta)-1
 -\frac12\{X(1/2+\delta)-1\}^2.                           \tag{19}
$$
Let $\delta\downarrow1/4$ after the conductor limit. Monotonicity of the
prime sum proves (1). There is no assumption about continuity of a limiting
prime measure and no fixed-prime inertness assumption.

For two sequences at equal logarithmic conductor scales, set
$Y=\min(q_1,q_2)^{2\delta}$. The product cancellation argument of
Section 2.3, using (4), (5), and (8), gives $S_{\chi_1\chi_2}(Y)/Y\to0$.
Here the cutoff has a fixed positive margin over the quarter-power of
the product conductor because $2\delta>1/2$. Bounded primitive product
conductors are covered by periodicity; the Euler deletion cost is
subpower. Since $Y\le q_i^{2\delta}$, (7) and (19) give
$\Phi_\delta(X_1)+\Phi_\delta(X_2)\ge1$. Letting
$\delta\downarrow1/4$ proves (2). This does not assert cancellation
exactly at the quarter-power boundary.

The function $\Phi$ increases on $[4/3,8/5]$, and $2\Phi(X)=1$ has its
relevant root at $c_*$. If (3) failed for arbitrarily large $Q$, select
two characters in each window and pass to residue subsequential limits.
Their values lie in $[4/3,c_*-\epsilon]$ by the imported individual lower
bound. Their logarithmic conductor ratio tends to one, contradicting (2).
This proves Theorem 1.

## 6. Proof of Theorem 2

Put
$$
c=301/200,\quad r=2048,\quad\delta=501/2000,\quad
\varepsilon=10^{-6},\quad a_0=10^{-9},\quad e_0=2\cdot10^{-6}.
$$
Let $t\ge\exp(1000000)$ and $\ell=\log t$. Appendix A proves, uniformly
for $U\ge\delta$,
$$
e\le a_0,\qquad \gamma_t=(8\log t+48)/t\le a_0,\qquad
|E_\chi(U)|\le a_0,\qquad 2/\lfloor t^2\rfloor\le a_0.     \tag{20}
$$
Suppose $x\le c$ and write $A(U)=d+xU$. On $[\delta,2\delta]$, positivity
and (6) give $0<A(U)<2$. The lower and upper errors in (14), relative
to $A(U)/\alpha$, are at most
$$
a_0,\qquad\frac{c\varepsilon+3a_0}{1-a_0}<e_0,
$$
respectively. Thus (17) holds. Both nonidentity masses in Section 4.3
are bounded above by
$$
c(1/2+2\delta+a_0)+e_0-1<3/5.
$$
At $U=\delta$, positivity and (17) also give
$$
\begin{aligned}
\alpha&\le\frac{c(1/2+\delta+a_0)}{1-e_0}<6/5,\\
B&\le c(1/2+\delta+a_0)+e_0-1<1/5,\\
C&\ge\frac{\delta(1-e_0)}{1/2+\delta+a_0}>3/10.
\end{aligned}
$$
In particular (9) holds. Equation (18) gives
$$
P_\chi(q^{2\delta})\le\alpha-1+B+C-B^2/2+5e_0+a_0.        \tag{21}
$$

Set $b=c(1/2+\delta)=451801/400000$, $g=c\delta=150801/400000$,
$B_0=b/\alpha-1$, and $z=c a_0+e_0$. Then $B\le B_0+z$ and
$C\le g/\alpha$. On $1\le\alpha\le6/5$, we have $B_0>-1/6$ and
$B_0+z<1$. The function $f(u)=u-u^2/2$ increases there and has derivative
less than two, so $f(B)\le f(B_0)+2z$, even when $B_0$ is negative.
The right side of (21) is therefore at most
$$
F(\alpha)+2z+5e_0+a_0,\quad
F(\alpha)=\alpha-2+(b+g)/\alpha-\tfrac12(b/\alpha-1)^2.
$$
The derivative again has the sign of
$p(\alpha)=\alpha^3-(2b+g)\alpha+b^2$. This polynomial is convex, and
$$
p(1)=-\frac{57637056399}{160000000000},\qquad
p(6/5)=-\frac{25509296399}{160000000000}.
$$
Thus $F$ decreases on the whole admissible interval. Its value at one is
$159398256399/320000000000$. Including all errors gives
$$
P_\chi(q^{501/1000})
 \le\frac{797013688411}{1600000000000}
 =0.498133555256875<\frac{499}{1000}.                     \tag{22}
$$

To finish the contradiction, let $T=\log Q$ and let $m$ be the primitive
product conductor. Appendix A proves that its Burgess or periodicity
constant has $r$th-power logarithm at most $(5003/10000)T$, uniformly
for every $m\le4Q^2$. It also bounds the logarithm of the deletion
factor by $T/10^8$. These are sufficient because the common prime
cutoff has exponent $501/1000$, leaving the following positive margin.

Choose $Y=\exp((501/1000)T)$. Combining (8), (A3), and (A4),
$$
\frac{|S_{\chi_1\chi_2}(Y)|}{Y}
 \le\exp\left[-T\left(\frac7{10000r}-10^{-8}\right)\right]
 <e^{-T/4000000}<1/1000,                                 \tag{23}
$$
since the coefficient is $4247/12800000000>1/4000000$.
Also $1/Y<1/1000$. If both characters satisfied $x_i\le301/200$, then
$Y\le q_i^{501/1000}$, so (7) and (22) would give
$$
S_{\chi_1\chi_2}(Y)/Y>1-1/1000-2(499/1000)=1/1000,
$$
contradicting (23). This proves Theorem 2.

## 7. Evidence, reproducibility and limits

The supplement contains four Python programs, their recorded results,
and a manifest. Python 3.10 or later and SymPy suffice. Run

    python replay.py

The stages check 511 rational head/tail measures with 4071 moment
comparisons and 81 small-prime Euler patterns; 49 exact comparisons for
the finite endpoint ledger; 300 cumulative-log cases with 3062 power
comparisons and 10560 Markov cutoffs; and 25 arithmetic factorizations
with 6400 coefficients. Six further rational comparisons check the
asymptotic parameter rectangle. Each parallel stage uses at most five
CPU workers, and stages run sequentially.

The Euler checker computes primitive coefficients by square-divisor
inversion separately from logarithmic Euler coefficients. Removing the
tail hypothesis or the Markov shift gives explicit failing controls.
The programs and retained outputs are the same ones used for the complete
composite-mass argument; the replay compares outputs exactly after
removing elapsed-time fields. These are finite author controls. They do
not prove the asymptotic theorem by sampling, independently verify the
analytic inputs from [1,2], or constitute independent mathematical review
of the full manuscript. Infinite-range monotonicity is proved in
Appendix A rather than inferred from sampled parameters.

The conclusions leave one exceptional character in a window and permit
sufficiently sparse exceptional sequences. The explicit threshold is
enormous. There is no improved individual-residue coefficient, numerical
tenth-discriminant bound, enumeration, classification or imported census
consequence. The relaxed measure equality example is not a realization
by quadratic characters. Historical novelty of every exact combination
is not certified by the limited literature comparison.

OpenAI Codex was used for mathematical derivation, literature reading,
manuscript preparation and CPU checks. No subagents or delegated model
calls were used. Code is MIT licensed; author prose and results are
CC BY 4.0. The supplement README states the evidence scope.

## Appendix A. Explicit analytic and deletion envelopes

The exact exponent in (6) at $r=2048$ is
$$
B_r(t)=\frac{2049t}{8192}+\frac{t}{\ell}\log(4r^2)
 +r\log(80\sqrt r(1+t))+\log8+\ell/2.
$$
Use $\log(4r^2)=24\log2<17$, $\sqrt r<46$,
$80\cdot46(1+t)\le7360t<2^{13}t$, and $\log8<3$. Then
$$
\frac{B_r(t)}t\le\frac{2049}{8192}+\frac{17}{\ell}
 +(4097\ell/2+26627)e^{-\ell}<\frac{1251}{5000}.           \tag{A1}
$$
The remainder is less than $10^{-6}$ at $\ell=1000000$ using
$e^\ell>2^\ell$, and decreases thereafter. The rational upper bound
for (A1) is $32017929/128000000<1251/5000$.
The source range holds since $t-3>3^{2048}>e^{2048}$.

The margin $\delta-1251/5000=3/10000$ in (6) gives
$$
|E_\chi(U)|\le41000t e^{-t/7000000}
 \le\frac{246000\cdot7000000^3}{t^2}<10^{-9},              \tag{A2}
$$
where $e^v\ge v^3/6$ was used. The functions
$(8\ell^2+4\ell)e^{-\ell}$ and $(8\ell+48)e^{-\ell}$ decrease on
$\ell\ge1000000$; their endpoint comparisons give the first two
bounds in (20). Since $\lfloor t^2\rfloor\ge t^2/2$, the last bound
in (20) follows from $4/t^2<10^{-9}$. Also $y=t^2<q^\delta$.

Now let $T=\log Q$, $L=\log T\ge1000000$, and let $s=\log m$ for any
nonprincipal primitive product conductor $m\le4Q^2$. If $s\ge3^{2049}$,
the source range holds and $B_r(s)$ is increasing. Put $s_*=2(T+1)$.
Then $s\le s_*$,
$$
s_*\le(2000001/1000000)T,\qquad L\le\log s_*\le L+2,
$$
and $80\sqrt r(1+s_*)<2^{14}T$. Thus
$$
\frac{B_r(s)}T\le
\left(\frac{2049}{8192}+\frac{17}{L}\right)\frac{2000001}{1000000}
 +(4097L/2+28676)e^{-L}<\frac{5003}{10000}.                \tag{A3}
$$
The exact upper comparison is
$64035762017801/128000000000000<5003/10000$.
If $s<3^{2049}$, periodicity instead gives
$$
|S_\eta(Z)|\le\min(Z,m)\le m^{1/r}Z^{1-1/r}.
$$
Its $r$th-power logarithmic constant is
$s<3^{2049}<(5003/10000)T$. Thus the envelope (A3) covers every
primitive product conductor.

For $\theta=1-1/r$ and $k=\omega(P)$, the $i$th prime is at least $i+1$.
Therefore
$$
\begin{aligned}
\log\prod_{p\mid P}(1+p^{-\theta})
&\le r\{(k+1)^{1/r}-1\}\\
&\le r(2\log P+1)^{1/r}\le r(5T)^{1/r}\le T/10^8.        \tag{A4}
\end{aligned}
$$
Here $k\log2\le\log P\le2(T+1)$ and $\log2>1/2$. The last
inequality is equivalent to $5(10^8r)^r\le T^{r-1}$. The left integer
has bit length $76957$, whereas the elementary lower bound for the
right side is $2^{2047000000}$. This avoids constructing the large
right-hand integer in the checker. All endpoint inequalities improve
as $T$ increases.

The endpoint certificate uses only rational arithmetic. For example,
$e<3$ follows by a geometric bound on the exponential series remainder,
and $24\log2<17$ follows from a finite rational lower sum for $e^{17/24}$.
The monotonicity arguments above, rather than sampling, cover the infinite
parameter ranges.

## References

[1] M. Cairn. Explicit residue separation for primitive quadratic characters.
rStation, paper 52, version 1, 2026. Theorems 1--2 and Section 3.
https://rstation.ai/problems/tenth_discriminant/papers/52/v1

[2] M. Cairn. Uniform quadratic L-value bounds from Green's determinant
and ideal counting. rStation, paper 1, version 3, 2026. Appendix C,
especially (C12), (C22), and (C27)--(C29).
https://rstation.ai/problems/tenth_discriminant/papers/1/v3

[3] A. Granville and K. Soundararajan. Large character sums: Burgess's
theorem and zeros of L-functions. arXiv:1501.01804v2, Sections 6--7.
https://arxiv.org/abs/1501.01804v2

[4] A. Granville and K. Soundararajan. The spectrum of multiplicative
functions. Annals of Mathematics 153 (2001), 407--470.
DOI: 10.2307/2661346. The version read here is arXiv:math/9909190v1,
especially Sections 1, 3 and 4.
https://arxiv.org/abs/math/9909190v1
