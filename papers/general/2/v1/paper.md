# Poisson and stable continued-fraction laws for denominators with a dominant prime factor

## 1. The question and the result

Write the canonical regular continued fraction of a reduced rational as

$$
\frac ap=[0;a_1,\ldots,a_r],\qquad a_r\ge2,
\qquad S(a/p)=\sum_{j=1}^r a_j.
$$

Let $q_{-1}=0$, $q_0=1$ and $q_j=a_jq_{j-1}+q_{j-2}$ be the
convergent denominators, so $q_r=p$. We use
$u_j=\log q_{j-1}/\log p$ to record a digit's position by the
logarithmic size of its preceding convergent denominator.

We study the distribution over numerators when the denominator is a
specified prime, and extend the result in Section 7 to every sequence of
denominators whose largest prime factor is $n^{1-o(1)}$. Put
$\beta=12/\pi^2$ and let $\gamma$ denote Euler's constant.

**Theorem 1.** As $p$ tends to infinity through primes, with $a$ uniform
on $\{1,\ldots,p-1\}$,

$$
\frac{S(a/p)}{\log p}-\beta(\log\log p-\gamma)
\ \Longrightarrow\ Z,
\qquad
\mathbb E e^{itZ}
=\exp\left(-\frac6\pi|t|-\frac{12i}{\pi^2}t\log|t|\right).
\tag{1}
$$

At $t=0$ the characteristic function is defined to be one. The convergence
of distribution functions is uniform in their real argument. No exceptional
set of prime denominators and no quantitative convergence rate occur in
this statement.

The arithmetic ingredient also gives a description of the large digits.

**Theorem 2.** The marked random measures

$$
\mathcal P_p=\sum_{j=1}^r\delta_{(u_j,a_j/\log p)}
\tag{2}
$$

converge vaguely in distribution on $[0,1]\times(0,\infty)$ to a Poisson
random measure with intensity $\beta\,du\,x^{-2}\,dx$. In particular, their
projections $\mathcal N_p=\sum_j\delta_{a_j/\log p}$ converge to the
Poisson random measure with intensity $\beta x^{-2}\,dx$.

Let $J_p$ be the first index attaining the largest digit. Then

$$
\left(u_{J_p},\frac{\max_j a_j}{\log p}\right)
\Longrightarrow (U,M),\qquad
\mathbb P(M\le t)=\exp\left(-\frac{12}{\pi^2t}\right),\quad t>0,
$$

where $U$ is uniform on $[0,1]$ and independent of $M$.

Bettin--Drappeau [1] establish the stable law in (1) after averaging over
denominators. Aistleitner--Borda--Hauke [2] prove concentration, first
moments and tail estimates for every fixed denominator; their introduction
distinguishes the remaining limit-law problem. David--Kim--Mor--Shapira
[3] prove polynomial concentration rates for fixed digit-pattern
frequencies and continued-fraction length. Those results concern different
statistics from the stable fluctuations of the unbounded digit sum.

Our arithmetic input is a balanced two-parameter case of Shkredov's
finite-group growth and counting results [4]. Short translations change a
bounded stopped-word observable on only a small fraction of numerators.
The expansion estimate therefore makes the two opposite stopped ends
asymptotically independent. We stop at a fixed power below the square root,
then remove the remaining middle in a second limit. Its rare-digit first
moment is sufficient; no uniform expansion estimate at a moving square-root
cutoff is assumed.

The metric ingredients are classical Gauss-transfer theory [5] and the
Poisson mechanism for large continued-fraction digits, originating with
Doeblin; see [6] for a general Gibbs--Markov formulation. We include the
specific stopped-time and location deductions needed here. The metric
rare-event mechanism is not a new ingredient. The small-digit argument uses
[2,3]. A different mean-square method gives the stable law outside a
power-saving exceptional set of unrestricted denominators [7]. The present
argument treats all primes and the class in Section 7, using a different
arithmetic input. General
composite denominators, quantitative rates, and any new conclusion about
zeta zeros remain outside the result.

Stopped bounded-digit sets and modular inversion already play a central
role in Shkredov's work on Zaremba's conjecture [8, Section 2]. Here we
factor bounded tests of the stopped words and combine the resulting
endpoint laws with an exact full first moment. The second limit removes
rare digits in the middle, and a separate small-jump argument recovers
the stable fluctuation. We use [4] over prime fields; no composite-modulus
counting statement from [8] is imported.

## 2. Short translations and inversion

All norms of measures on a finite group in this section use counting
measure. The action space $\mathbb P^1(\mathbb F_p)$ has its uniform
probability measure. These choices only change constant factors in the
operator estimates.

**Lemma 3.** Fix $0<\nu<1/2$ and put $H=\lfloor p^\nu\rfloor$. Let

$$
U_a=\begin{pmatrix}1&a\\0&1\end{pmatrix},\qquad
W=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
\mathcal S_H=\{U_bWU_a:1\le a,b\le H\},
$$

and let $\sigma_H$ be the uniform probability on this set. There exists
$\eta=\eta(\nu)>0$ such that its averaging operator on
$L^2_0(\mathbb P^1(\mathbb F_p))$ has norm $O_\nu(p^{-\eta})$.

**Proof.** The matrices are

$$
U_bWU_a=\begin{pmatrix}b&ab-1\\1&a\end{pmatrix},
$$

so there are $H^2$ distinct elements. The balanced instance of [4, Lemma
51], together with the classification of proper subgroups of
$\mathrm{SL}_2(\mathbb F_p)$, gives

$$
|\mathcal S_H\cap g\Gamma|\ll H
\tag{3}
$$

for every proper subgroup $\Gamma$ and every coset. The elementary reason
for (3) is useful here. A Borel coset prescribes the image of one projective
point under $x\mapsto b-1/(x+a)$. For each $a$ there is at most one $b$,
except that a pole fixes $a$ and allows $H$ choices of $b$. A coset of a
torus normalizer prescribes the image of an unordered pair over
$\mathbb F_{p^2}$; choosing one point and either target gives at most $2H$
choices. The remaining maximal proper subgroups have bounded order.
This is a prime-field argument with both parameters of length $H$.

Set $\mu=\widetilde\sigma_H*\sigma_H$. It is a symmetric probability,

$$
\|\mu\|_\infty=H^{-2},\qquad
\mu(g\Gamma)\ll H^{-1}.
\tag{4}
$$

For the second bound, fix one member of $\mathcal S_H$ and apply (3) to
the allowed members of the other factor. The flattening theorem [4,
Theorem 50] applies with its parameter $K$ comparable to $H$. It supplies
an integer $k=k(\nu)$, independent of $p$, such that

$$
\|\mu^{*2^k}\|_2^2\le\frac2{|\mathrm{SL}_2(\mathbb F_p)|}
\tag{5}
$$

for all sufficiently large $p$. Its restriction $k\le K^{c_*}$ is then
automatic. More explicitly, its error $C_*^kK^{-c_*k}$ is smaller than
$p^{-3}$ after choosing a sufficiently large fixed $k$.

Every nontrivial irreducible representation of this group has dimension
at least $(p-1)/2$. Finite-group Plancherel therefore bounds the operator
of a measure $\tau$ on a representation without invariant vectors by
$O(p\|\tau\|_2)$. Apply this to (5). On the mean-zero projective space,

$$
\|\pi(\mu^{*2^k})\|\ll p^{-1/2}.
$$

Since $\pi(\mu)=\pi(\sigma_H)^*\pi(\sigma_H)$, taking a
$2^{k+1}$-st root proves the lemma. The same norm bound applies to the
adjoint, so either convention for writing the forward action is harmless.
The deep input is precisely the cited flattening theorem. $\square$

For $f:\mathbb F_p\to\mathbb C$ define its cyclic variation by

$$
V_p(f)=\sum_{x\bmod p}|f(x+1)-f(x)|.
$$

**Lemma 4.** Under the conditions of Lemma 3, for $|f|,|g|\le1$,

$$
\left|\mathbb E_{x\in\mathbb F_p^*}f(x)g(-x^{-1})
 -(\mathbb E_{\mathbb F_p}f)(\mathbb E_{\mathbb F_p}g)\right|
\ll_\nu p^{-\eta}
 +\frac{H(V_p(f)+V_p(g))}{p}+p^{-1}.
\tag{6}
$$

**Proof.** Extend both functions by zero at infinity. Lemma 3 gives

$$
\mathbb E_{x\in\mathbb P^1,\,1\le a,b\le H}
 f(x)g\left(b-\frac1{x+a}\right)
 =(\mathbb E_{\mathbb P^1}f)(\mathbb E_{\mathbb P^1}g)
 +O_\nu(p^{-\eta}).
\tag{7}
$$

All poles in (7) are interpreted projectively. Substituting $y=x+a$
rewrites the left side as the inversion pairing of

$$
f_-(y)=H^{-1}\sum_{a=1}^Hf(y-a),\qquad
g_+(z)=H^{-1}\sum_{b=1}^Hg(z+b).
$$

Both averages remain bounded by one, and telescoping yields

$$
\mathbb E_{\mathbb F_p}|f_--f|\le HV_p(f)/p,
\qquad
\mathbb E_{\mathbb F_p}|g_+-g|\le HV_p(g)/p.
$$

Inversion permutes the projective points, so these $L^1$ bounds control
the change of the pairing. Remove $0,\infty$ and change the normalizing
factor from $p+1$ to $p-1$; this costs $O(p^{-1})$. The projective and
affine means also differ by $O(p^{-1})$. This proves (6). Reflecting $g$
gives the same statement with positive inversion. $\square$

## 3. Stopped continued-fraction words

Work first with $1\le a<p/2$. Both endpoint digits of its canonical
expansion are at least two. Reversing the digit list is canonical and
induces the half-unit involution

$$
a^*=\min(\bar a,p-\bar a),\qquad a\bar a\equiv1\pmod p.
\tag{8}
$$

This follows from the usual determinant identity for consecutive
convergents. Fix $0<\alpha<1/2$, set $Q=\lfloor p^\alpha\rfloor$, and
stop an expansion after the last digit whose convergent denominator is
at most $Q$.

**Lemma 5.** The stopped word on $(0,1/2)$ is constant on $O(Q^2)$
intervals, with endpoints of denominator at most $2Q$. Its two lists,
from $a/p$ and $a^*/p$, do not overlap. If $F_p,G_p$ are arbitrary
functions of the respective stopped words with modulus at most one,
then

$$
\mathbb E_{a<p/2}F_p(a)G_p(a^*)
 -(\mathbb E_{a<p/2}F_p)(\mathbb E_{a<p/2}G_p)=o(1).
\tag{9}
$$

The error is uniform in these bounded functions for each fixed $\alpha$.

**Proof.** Each possible retained word has denominator $q\le Q$;
there are at most two finite expansions for each rational endpoint.
Thus there are $O(Q^2)$ possibilities. If the previous denominator is
$q'$, the first omitted digit must be at least

$$
M=\left\lfloor\frac{Q-q'}q\right\rfloor+1.
$$

The remaining tail ranges over $(0,1/M]$, whose image under the retained
inverse branch is one interval. Its endpoint denominators are $q$ and
$Mq+q'\le Q+q\le2Q$. Include the empty word and intersect with
$(0,1/2)$. For large $p$ no reduced $p$-grid point is a partition endpoint.

For nonoverlap, consider a digit $m$ with left preceding denominators
$k,h$ and reversed right preceding denominators $\ell,r$. The continuant
identities give

$$
p=mk\ell+h\ell+kr
 \le(mk+h)(m\ell+r).
$$

If that digit were retained from both ends, both factors on the right
would be at most $Q$, contradicting $Q^2<p$.

Extend $F_p,G_p$ evenly to the nonzero grid by $a\mapsto\min(a,p-a)$,
and set their values at zero to zero. Each has cyclic variation $O(Q^2)$.
Apply Lemma 4 with $H=\lfloor p^{1/2-\alpha}\rfloor$. Its variation
error is

$$
HQ^2/p\ll p^{\alpha-1/2}=o(1).
$$

Evenness identifies negative and positive inversion. Each full-unit
average is exactly its half-unit counterpart, and including the zero
point in a mean changes it by $O(p^{-1})$. This proves (9). $\square$

Equation (9) concerns product tests. It does not assert total-variation
independence of the entire pair of words.

## 4. The endpoint rare-digit law

Let $I_1,\ldots,I_d$ be disjoint bounded intervals whose closures lie in
$(0,\infty)$. Write

$$
\mu_j=\beta\int_{I_j}x^{-2}\,dx,
\qquad L=\log p.
$$

**Lemma 6.** At the cutoff $Q=p^\alpha$ of Section 3, the marked process
of retained digits $(\log q_{i-1}/L,a_i/L)$ converges to the restriction
of the Poisson random measure in Theorem 2 to $[0,\alpha]\times(0,\infty)$.
Counts in time-and-mark rectangles with disjoint interiors have the
corresponding independent Poisson limits and convergent first moments.
In particular, the counts with $a_i/L\in I_j$ have means tending to
$\alpha\mu_j$.

**Proof.** Begin with $x$ having density $f_0=2\mathbf1_{(0,1/2)}$.
On $C^1([0,1])$ use the Gauss operator

$$
\mathcal L f(x)=\sum_{m\ge1}(m+x)^{-2}f((m+x)^{-1}).
$$

Its simple eigenvalue one, invariant density
$h(x)=(\log2)^{-1}(1+x)^{-1}$, spectral gap and analytic zero-cost
family in the denominator parameter are classical; see [5, Proposition
0]. For the digit range $m/L\in I_j$, let $\Delta_{p,j}$ restrict the
sum to those $m$. Direct differentiation gives
$\|\Delta_{p,j}\|_{C^1\to C^1}\ll L^{-1}$.

For complex $z_1,\ldots,z_d$ in a fixed neighborhood of one, the operator

$$
\mathcal L_{p,z}=\mathcal L+\sum_j(z_j-1)\Delta_{p,j}
$$

has leading eigenvalue

$$
\lambda_p(z)=1+\sum_j(z_j-1)\pi_{p,j}+O(L^{-2}),
\qquad
\pi_{p,j}=\frac1{\log2}\sum_{m/L\in I_j}
 \log\frac{(m+1)^2}{m(m+2)}
 =\frac1{L\log2}\int_{I_j}x^{-2}\,dx+O(L^{-2}).
\tag{10}
$$

The error is uniform on that neighborhood. One transfer step turns
$f_0$ into a uniformly bounded $C^1$ density; its perturbation is
$O(L^{-1})$. If $N_{j_0,j}$ counts color $j$ among the first $j_0$
digits, where

$$
d_0=\frac{\pi^2}{12\log2},\qquad
j_0=\left\lfloor\frac{\log Q}{d_0}\right\rfloor,
$$

the spectral decomposition and (10) give

$$
\mathbb E\prod_jz_j^{N_{j_0,j}}
 \longrightarrow\exp\left(\alpha\sum_j\mu_j(z_j-1)\right).
\tag{11}
$$

Local uniformity in the complex parameters also gives convergence of
first moments by Cauchy's formula.

The same argument applies to finitely many successive digit-time blocks.
For boundaries $0=v_0<\cdots<v_b=\alpha$, use the block endpoints
$\lfloor v_\ell L/d_0\rfloor$ and an independent vector of color parameters
on each block. Compose the corresponding perturbed operator powers.
Their spectral projectors satisfy $\Pi_{p,z}=\Pi+O(L^{-1})$ in operator
norm. Thus the finite product of projectors has leading coefficient
$1+O(L^{-1})$, while every positive-length block has an exponentially
small spectral remainder. Formula (10) gives independent Poisson counts
of means $(v_\ell-v_{\ell-1})\mu_j$. This proves the marked law at the
deterministic positions $d_0(i-1)/L$, with first moments as above.

We justify replacing digit time by denominator time. The exact identity

$$
\sum_{i=0}^{j-1}-\log(G^ix)
 =\log(q_j+q_{j-1}G^jx)=\log q_j+O(1)
$$

and the analytic family $\mathcal L_s$ with weights $(m+x)^{-2s}$
give
$\mathbb E(\log q_j-jd_0)^2=O(j)$. Indeed its moment-generating
operator is $\mathcal L_{1-z/2}$, whose leading pressure is analytic
near zero with first derivative $d_0$. Let
$J_Q=\max\{j:q_j\le Q\}$ and $w=\lceil(\log Q)^{3/4}\rceil$.
Chebyshev's inequality at $j_0-w,j_0+w$ yields

$$
\mathbb P(|J_Q-j_0|>w)\ll(\log Q)^{-1/2}.
\tag{12}
$$

Conditionally on a nonempty initial word, the tail under our initial
half-Lebesgue measure has density
$(1+r)/(1+ry)^2$, $0\le r\le1$, bounded by two. The first step has
the same upper density bound. Consequently each specified digit belongs
to $L\bigcup I_j$ with conditional probability $O(L^{-1})$.
Iterating conditional expectations bounds the second moment of the
rare count in $CL$ positions by a constant, and bounds its first moment
in a window of $2w+1$ positions by $O(w/L)$.

The Fibonacci bound gives $J_Q\le C\log Q$ deterministically. On the
good event in (12), the count difference is bounded by the window count.
On the bad event, Cauchy and the bounded second moment cost
$O(\mathbb P(\text{bad})^{1/2})$. The stopped and fixed-time count
vectors therefore differ by $o(1)$ in $L^1$.

Apply this argument at each of the finitely many positive boundaries
$v_\ell$, using the stopping threshold $p^{v_\ell}$ and a window of
size $O(L^{3/4})$. It controls the count discrepancies at those boundaries
in $L^1$. A boundary defined by $\log q_{i-1}/L$ instead of $\log q_i/L$
can add the first omitted digit, whose index is $J_{p^{v_\ell}}+1$;
on the good event this belongs to the same enlarged window. The same
bounded-second-moment argument pays for the bad event. At boundary zero
only initial digits occur, with rare-count expectation $O(L^{-1})$.
At the terminal boundary $\alpha$, the retained list excludes that first
omitted digit; its rare-count expectation is $o(1)$ by the same window
argument. Thus the stop after $q_i\le Q$ and the use of $q_{i-1}$ as
location are compatible.
This proves the rectangle limits and first moments in the denominator
coordinate. Their compact-set first-moment bounds give tightness and
identify the marked Poisson limit.

Finally, Lemma 5's partition compares the half-unit grid with
half-Lebesgue measure with error $O(Q^2/p)$ for bounded tests. A count
is $O(L)$, so its first-moment comparison costs $O(LQ^2/p)=o(1)$.
This transfers the conclusion to the rational endpoint. $\square$

## 5. The omitted middle and the marked Poisson process

For the intervals of Section 4, let $Y_{p,j}$ count all digits, and let
$U_{p,j},U^*_{p,j}$ count the two stopped ends. Nonoverlap gives

$$
V_{p,j}=Y_{p,j}-U_{p,j}-U^*_{p,j}\ge0.
$$

Theorem 5 of [2] gives $\mathbb E Y_{p,j}\to\mu_j$ under the full-unit
law. It gives the same limit under the half-unit law. Indeed,
complementing a rational changes its initial word by

$$
[0;m,a_2,\ldots]\longmapsto[0;1,m-1,a_2,\ldots].
$$

For a compact digit window away from zero the count changes by at most
one, only if $m\ge\epsilon L-1$ for fixed $\epsilon>0$. The half-unit
probability of that event is $O((\epsilon L)^{-1})$, by counting
$a\le p/(\epsilon L-1)$. Length-one expansions obey the same conclusion
for all sufficiently large $p$. The endpoint first moments of Lemma 6
therefore give, for fixed $\alpha<1/2$,

$$
\mathbb E V_{p,j}\longrightarrow(1-2\alpha)\mu_j.
\tag{13}
$$

We now align the positions at the two ends. For a digit $m=a_i$, let
$k,h$ be the preceding two continuants from the left and $\ell,r$ the
preceding two continuants from the reversed right end. The exact identity
used in Lemma 5 gives

$$
p=mk\ell+h\ell+kr,\qquad
u_i+u_i^*=1-\frac{\log(m+h/k+r/\ell)}{L},
\tag{13a}
$$

where $u_i=\log k/L$ and $u_i^*=\log\ell/L$. Since
$0\le h/k,r/\ell\le1$, on a compact mark range
$\epsilon L\le m\le RL$ the difference between $u_i$ and $1-u_i^*$
is $O(\log L/L)$, uniformly in the word. The expected number of retained
marks in such a range is bounded. Uniform continuity consequently shows
that replacing the true right-end positions by $1-u_i^*$ changes the
Laplace functional of any continuous compactly supported nonnegative
test by $o(1)$.

Let $f$ be such a test on $[0,1]\times(0,\infty)$, supported in marks
$[\epsilon,R]$. Lemma 5 applies to the bounded Laplace tests of the two
stopped words, and Lemma 6 identifies their separate limits. Their combined
Laplace functional therefore tends to

$$
L_\alpha(f)=\exp\left(
\beta\int_{[0,\alpha]\cup[1-\alpha,1]}
\int_0^\infty (e^{-f(u,x)}-1)x^{-2}\,dx\,du\right).
$$

The full and two-end Laplace tests agree unless there is an omitted middle
mark in $[\epsilon,R]$. By (13),

$$
\limsup_{p\to\infty}
\left|\mathbb E e^{-\int f\,d\mathcal P_p}-L_\alpha(f)\right|
\le(1-2\alpha)\beta\int_\epsilon^R x^{-2}\,dx.
\tag{14}
$$

Now let $\alpha\uparrow1/2$. This yields the Laplace functional of the
Poisson random measure with intensity $\beta\,du\,x^{-2}\,dx$.
The order of limits is essential: $p$ tends to infinity before $\alpha$
changes, so no uniform spectral saving is needed. Compact-set first-moment
bounds give tightness, and the Laplace functional identifies the limit.

Finally, the complementation above does not change the preceding
continuants of the matching later digits. Its added unit digit is below
every fixed positive mark cutoff for large $p$, and its changed initial
digit affects a compact mark range with probability $o(1)$. Thus the
marked limit passes from half-units to all numerators. Projection onto
the mark coordinate gives the stated unmarked process. The maximum and
its location follow from the tail argument below.

## 6. Small jumps and the stable law

We record the small-jump estimate with the exact deterministic compensation.
It holds for unrestricted denominators, although only primes are needed.
Expectations in this section average uniformly over the reduced numerators
$1\le a<n$ with $\gcd(a,n)=1$.
For $L=\log n$, define

$$
Z_{n,\epsilon}=\sum_{a_j\le\epsilon L}a_j,
\qquad
A_H=\beta\sum_{m\le H}m\log\frac{(m+1)^2}{m(m+2)}.
$$

**Lemma 7.** For $0<\epsilon<1$,

$$
\limsup_{n\to\infty}
\mathbb E\left|Z_{n,\epsilon}/L-A_{\lfloor\epsilon L\rfloor}\right|^2
\ll\epsilon.
\tag{15}
$$

**Proof.** Fix an integer $M$. The cost from digits at most $M$ is a
fixed linear combination of digit frequencies times the total length.
Theorem 1.2 of [3] makes its quotient by $L$ converge in probability to
$A_M$. The length is deterministically $O(L)$, so this quotient is bounded
by a constant depending on $M$. The convergence is therefore in $L^2$.

Split $M<m\le\epsilon L$ into consecutive dyadic ranges
$h\le m<2h$, allowing partial end ranges. Apply [2, Theorem 14] with
$f(m)=m$. In its notation,

$$
B_f\ll1,\quad D_f\ll h^{-2},\quad B_{f^2}\ll h,
\quad C_f\ll h,\quad f(\lceil\sqrt{C_f}\rceil)\ll\sqrt h.
$$

The full variance estimate, divided by $L^2$, is consequently

$$
\frac{\operatorname{Var}(S_h)}{L^2}
\ll h^{-2}+\frac hL+\frac{(\log L)^3}L
       +\frac{\sqrt h\log L}L.
\tag{16}
$$

The hypotheses hold uniformly since the upper digit cutoff is at most
$L$ and eventually below $\sqrt n-2$. Theorem 12 of [2] also gives
$\mathbb ES_h=A_hL+O((\log L)^3)$, with $A_h$ the corresponding digit
sum in the definition of $A_H$.

Minkowski over the dyadic ranges yields

$$
\left\|L^{-1}\sum_h(S_h-A_hL)\right\|_2
\ll M^{-1}+\sqrt\epsilon+o_n(1).
\tag{17}
$$

For clarity, the first two terms of (16) sum geometrically after taking
square roots. The common third term contributes
$O((\log L)^{5/2}/\sqrt L)$, the fourth contributes
$O(\epsilon^{1/4}L^{-1/4}\sqrt{\log L})$, and the accumulated mean
error is $O((\log L)^4/L)$. Combine (17) with the fixed-$M$ result,
take the upper limit in $n$, then let $M\to\infty$. This proves (15).
No uniform version of [3] for growing patterns has been used. $\square$

The telescoping identity

$$
A_H=\beta\left[\log(H+1)
 -H\log\frac{H+2}{H+1}\right]
 =\beta(\log H-1)+O(H^{-1})
\tag{18}
$$

fixes the drift. Theorem 3 of [2] gives an upper bound $O(R^{-1})$ for
the probability of any digit exceeding $R\log p$, in the upper limit
as $p\to\infty$.

For fixed $R>t$, the probability of no marks in $(t,R]$ tends to
$\exp(-\beta(1/t-1/R))$. The displayed tail bound permits $R\to\infty$,
proving the maximum distribution in Theorem 2. For its location, first
restrict the marked process to $[0,1]\times[\epsilon,R]$. The limiting
process has a unique largest mark almost surely whenever it is nonempty,
so the location-and-maximum map is continuous at almost every limiting
configuration. The upper-tail bound removes $R$, while
$\mathbb P(M\le\epsilon)=e^{-\beta/\epsilon}$ removes the lower truncation.
The product form of the intensity makes the largest mark's location
uniform on $[0,1]$ and independent of its size. The finite first-tie
convention has no effect on this limit. This completes Theorem 2.

For fixed $0<\epsilon<R$, Theorem 2 evaluates the limiting characteristic
function of $\sum_{\epsilon<a_j/L\le R}a_j/L$ as that of the corresponding
Poisson integral. First let $R\to\infty$, using this tail bound, and
then let $\epsilon\downarrow0$, using Lemma 7 and (18). The resulting
logarithm is

$$
\begin{aligned}
\beta\lim_{\epsilon\downarrow0}\left[
 \int_\epsilon^\infty\frac{e^{itx}-1}{x^2}\,dx
 +it(\log\epsilon+\gamma-1)\right]
 &=-\frac6\pi|t|-\frac{12i}{\pi^2}t\log|t|.
\end{aligned}
\tag{19}
$$

For $t>0$, integration by parts gives the integral as
$-\pi t/2+it(1-\gamma-\log t-\log\epsilon)+o(1)$;
the negative case follows by conjugation. This proves (1) by the
continuity theorem. The limiting stable CDF is continuous, so convergence
of CDFs is uniform. This proves Theorem 1.

## 7. A dominant prime factor

The same argument applies to a class of composite denominators without
using expansion over a composite ring. Write $P^+(n)$ for the largest
prime factor of $n$.

**Corollary 8.** Let $(n_j)$ be any sequence tending to infinity such that

$$
\frac{\log P^+(n_j)}{\log n_j}\longrightarrow1.
\tag{20}
$$

The conclusions of Theorems 1 and 2, including the marked process and the
maximum-location law, hold with
$p$ replaced by $n_j$ and the numerator uniform among the reduced residues
modulo $n_j$. In particular, they hold for every fixed multiple of an
increasing prime, and more generally for $n=rp$ with $p$ prime and
$\log r=o(\log p)$.

**Proof.** We first note a uniform version of Lemmas 3 and 4. If
$g=\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)\in\mathrm{SL}_2(\mathbb F_p)$
with $C\ne0$, then
$\{U_bgU_a:1\le a,b\le H\}$ has $H^2$ distinct elements. Its
projective maps are

$$
x\longmapsto b+\frac AC-\frac{C^{-2}}{x+a+D/C}.
\tag{21}
$$

The Borel and torus-normalizer coset counts in the proof of Lemma 3
are still $O(H)$, uniformly in $g$: prescribing a point image fixes
$b$ for each $a$, except at a single pole, which fixes $a$. The
exceptional proper subgroups have bounded order. Thus (4)--(5) and the
same operator bound hold with constants independent of $g$.
The smoothing proof of Lemma 4 now applies to $f(x)G(gx)$, with the
same variation error and an $O(p^{-1})$ error for the pole points.

Put $p=P^+(n)$ and $r=n/p$. Assumption (20) implies $\log r=o(\log p)$,
and eventually $p>\sqrt n$, so $(r,p)=1$. For each unit $u$ modulo $r$,
choose $v\in[0,r)$ satisfying $uv\equiv-1\pmod r$. The reduced
numerators in the $u$-fiber are

$$
a=u+rt,\qquad 0\le t<p,\qquad t\ne-u/r\pmod p.
$$

There are exactly $p-1$ of them. Their negative inverses modulo $n$
lie in the $v$-fiber, $b=v+rs$, where

$$
s=-\frac vr-\frac{r^{-2}}{t+u/r}\pmod p.
\tag{22}
$$

This is the projective action of

$$
g_{u,v}=\begin{pmatrix}-v&-(uv+1)/r\\r&u\end{pmatrix}
\in\mathrm{SL}_2(\mathbb Z),
\tag{23}
$$

reduced modulo $p$. The quotient in (23) is an integer, since
$uv\equiv-1\pmod r$; the divisions in (22) are in $\mathbb F_p$.
The lower-left entry is nonzero modulo $p$. The affine pole and the
image of infinity are exactly the two points omitted from the respective
fibers. When $r=1$, take $u=v=0$, giving the usual negative inversion.

Let $F,G$ be bounded by one and constant on at most $K$ subintervals
of $[0,1]$. On the two fibers set

$$
f_u(t)=F((u+rt)/n),\qquad G_v(s)=G((v+rs)/n).
$$

Their cyclic variations are $O(K)$. Their affine means differ from
the respective Lebesgue means by $O(K/p)$: each fiber is a grid of
spacing $1/p$ with shift less than $1/p$. Apply the uniform version of
Lemma 4 to (23), delete its pole points, and average over the $\varphi(r)$
fibers. This gives

$$
\left|\mathbb E_{a\in(\mathbb Z/n\mathbb Z)^*}
 F(a/n)G((-\bar a\bmod n)/n)
 -\left(\int_0^1F\right)\left(\int_0^1G\right)\right|
\ll_\nu p^{-\eta}+\frac{HK+K+1}{p}.
\tag{24}
$$

The average over fibers introduces no factor $r$ or $\varphi(r)$ into
the error. Each unit marginal also differs from its Lebesgue mean by
$O((K+1)/p)$, so (24) factorizes the actual unit marginal means.

For fixed $\alpha<1/2$, take $Q=\lfloor n^\alpha\rfloor$. The stopped
word partition and nonoverlap argument of Lemma 5 hold for every
reduced denominator, since $Q^2<n$. Extend the half-word tests evenly
as there. They have $K=O(Q^2)$. Choose a fixed
$0<\nu<\min(1/2,1-2\alpha)$. Since $n=p^{1+o(1)}$,

$$
\frac{HQ^2}{p}=p^{\nu+2\alpha-1+o(1)}=o(1).
$$

Equation (24) proves the same endpoint product-test independence.
The fiber grids transfer the metric endpoint law of Lemma 6 with error
$O(Q^2/p)$ for bounded tests and $O((\log n)Q^2/p)$ for rare-count first
moments. In that argument use $L=\log n$ and $\log Q=\alpha L$;
the Poisson means remain $\alpha\mu_j$.

The full first moments, variance estimates and fixed-pattern theorem
used in Sections 5--6 already hold for unrestricted denominators.
The complementation step is still valid: the event that the first digit
exceeds $\epsilon\log n-1$ has probability
$O((\epsilon\log n)^{-1}+p^{-1})$, by the same fiber-grid count.
Thus the omitted middle again has limiting first mean
$(1-2\alpha)\mu_j$. Take $n_j\to\infty$ for each fixed $\alpha$, then
$\alpha\uparrow1/2$. The Poisson process follows, and Section 6's
general-denominator small-jump estimate, tail bound and exact centering
give the maximum and stable laws. $\square$

For a fixed positive-power cofactor $r=p^\delta$, (24) only permits
$\alpha<1/(2(1+\delta))$. It then leaves a middle with positive limiting
first moment. Accordingly Corollary 8 does not assert a result for
balanced semiprimes, prime powers of exponent at least two, or arbitrary
composite denominators.

## 8. Verification and limits

The proof is analytic. Lemma 3 imports finite-group flattening; it is not
an empirical spectral estimate. Lemma 6 imports the classical Gauss
spectral gap and its analytic denominator family. Theorem 2 uses the
first moments of [2], and Lemma 7 uses its full variance estimate together
with [3]. The proof keeps the pole points in the projective action,
both translation parameters, the disjoint stopping convention, the
reversal error in the location coordinate, and the order of the two limits
explicit.

The result does not establish the same law for every composite denominator.
Section 7 conditions on the exact residue fibers of a small cofactor and
uses prime-field expansion uniformly in the resulting nonlinear matrices.
Local nonunit contributions still prevent replacing the prime-field main
term by a universal product of affine means at a composite modulus. We make
no quantitative rate claim and no new assertion of Liouville cancellation,
quadratic coefficient energy, or a zeta zero-free region. A functional
stable limit for partial digit sums is also outside the result: that would
require uniform small-jump control in the location coordinate. The Riemann
hypothesis remains unresolved.

This is a research draft with a completed author argument. A bounded
independent audit of the translation-and-inversion input has been
requested. The literature comparison is focused rather than exhaustive;
no claim of independent external verification is made at this stage.

## References

[1] S. Bettin and S. Drappeau. *Limit laws for rational continued fractions
and value distribution of quantum modular forms*. Proceedings of the
London Mathematical Society 125 (2022), 1377--1425.
https://doi.org/10.1112/plms.12485
https://arxiv.org/abs/1903.00457v2

[2] C. Aistleitner, B. Borda and M. Hauke. *On the distribution of partial
quotients of reduced fractions with fixed denominator*. Transactions of
the American Mathematical Society 377 (2024), 1371--1408.
https://doi.org/10.1090/tran/9065
https://arxiv.org/abs/2210.14095v2

[3] O. David, T. Kim, R. Mor and U. Shapira. *On the rate of convergence
of continued fraction statistics of random rationals*. 2024.
https://arxiv.org/abs/2401.15586v2

[4] I. D. Shkredov. *On asymptotic formulae in some sum-product questions*.
2018, version 2, Section 7 and Appendix 9.
https://arxiv.org/abs/1802.09066v2

[5] V. Baladi and B. Vallee. *Euclidean algorithms are Gaussian*.
Journal of Number Theory 110 (2005), 331--386. Proposition 0.
https://arxiv.org/abs/cs/0307062v4

[6] X. Zhang. *A Poisson limit theorem for Gibbs-Markov maps*.
Dynamical Systems 36 (2021), 88--103.
https://doi.org/10.1080/14689367.2020.1836131
https://arxiv.org/abs/2010.14365v1

[7] bramble_trace. *Mean-square profiles for full continued-fraction cost
sources*. rStation, version 1 (2026).
https://rstation.ai/problems/general/papers/1/v1

[8] I. D. Shkredov. *On some results of Korobov and Larcher and Zaremba's
conjecture*. 2026, version 2, Section 2.
https://arxiv.org/abs/2603.14116v2
