# Binary entropy, character decay and weighted resonances for geometric Collatz words

## 1. Problem and contribution

Mary Rees studies the pushforward of independent geometric division
exponents through Collatz iteration and conjectures strong uniformity of
an associated dyadic digit sum at a resolution proportional to the number
of odd steps [1]. For every fixed geometric parameter, we prove polynomial
decay of every nontrivial binary character of the actual canonical endpoint,
uniformly at each fixed linear bit precision below $\log_2(3)$ times the
word length. Qualitatively the bias tends to zero whenever the binary
modulus is of smaller order than the canonical interval size $3^n$.
The final division block may truncate its valuation.

We retain explicit logarithmic-resolution estimates for canonical and raw
digit laws. The canonical law is relatively uniform pointwise at one
logarithmic scale; the new character argument strengthens bounded collision
energy at twice that scale to convergence to one, and hence total variation
convergence. The raw law retains a logarithmic energy bound and pointwise
uniformity at a double-logarithmic bit scale. This linear-precision
character statement concerns individual characters and does not control their
exponentially large squared sum. Theorem 6 in Section 8 states the new
result and its limits precisely.

We also retain an exact asymptotically critical division total. Uniformly
in every prescribed window $|D-\log_2(3)n|\le G(n)=o(n)$, every nontrivial
binary character has vanishing bias at each fixed linear bit precision
$p\le\lambda n$, $\lambda<\log_2 3$. Theorem 7 proves this qualitative
assertion with no effective rate. Fixing the total
removes the multiplier diffusion used by the iid proof; the new argument
instead controls an adapted critical pair process and retains the clock
mixture when reducing the ternary conductor.

For $\alpha<\log_3 2$, the known extension of Tao's primitive Fourier
estimate already gives stronger canonical projection bounds [2,3]. Our
all-parameter estimates include the critical parameter $\alpha=\log_3 2$
and larger parameters, where that estimate is unavailable. Section 7
states the comparison precisely.

The logarithmic bounds use a multiplicative collision count over the
units modulo a power of three. Such counting belongs to the universal-hashing
framework [4,5]. Its use here requires two additional steps: an exact
split of a Collatz word into an independent prefix and suffix, and a
collision bound valid for every suffix-dependent translation. Only the
actual suffix multiplier is approximated by uniform measure, with an
explicit error. This approximation is justified at logarithmic depth.
For canonical pointwise uniformity, Fourier inversion and the elementary
Ramanujan-sum identity control the worst common translation directly.
The new character argument combines the same exact split and multiplier
estimate with normalized Parseval, giving polynomial primitive ternary
decay. A periodic tent controls mass at the ends of the canonical interval;
a bounded-variation cutoff then completes to binary characters with only
a logarithmic coefficient cost. No Subspace or triangle-excursion input
is needed for Theorem 6. The exact-total Theorem 7 uses the separate
geometric and arithmetic inputs recorded in Appendix A.

We use the shortcut Collatz map

$$
C(n)=\begin{cases}n/2,&n\equiv0\pmod2,\\(3n+1)/2,&n\equiv1\pmod2.
\end{cases}
$$

Fix $\alpha\in(0,1)$ and put $q=1-\alpha$. Unless explicitly conditioned in Sections 9 or 11, the exponents are
independent, with

$$
\mathbb P(e_i=j)=\alpha q^{j-1},\qquad j\geq1.
$$

For a word of length $r$, write

$$
E_i=e_1+\cdots+e_i,\quad E_0=0,\quad S=E_r,
\quad S_i=e_i+\cdots+e_r.
$$

The word specifies the $S$ shortcut parities
$10^{e_1-1}\cdots10^{e_r-1}$. Let $n_e$ be its unique representative
in $[0,2^S)$ and let $u_r=C^S(n_e)$. In particular, the last division
block may terminate before the next odd state; $u_r$ need not be odd.
For an integer $a$, let $[a]_N$ denote its representative in $[0,N)$.
Inverses of powers of two in the following expressions are taken modulo
the indicated odd modulus. Define the raw integer

$$
W_r=\sum_{i=1}^r3^{r-i}[2^{-S_i}]_{3^i}.
\tag{1}
$$

Section 2 proves that $0<u_r<3^r$ and $u_r=[W_r]_{3^r}$, and identifies
(1) with the raw dyadic digit sum in [1]. Thus the laws studied here use
the fixed initial multiplicative residue $1$.

Set

$$
\begin{aligned}
\beta_\alpha&=\frac{1+q^2}{(1+q)^2},&
b_\alpha&=\frac{8q}{\alpha^2+4q},\\
T_h&=2\cdot3^{h-1},&
\varepsilon_{r,h}&=\sqrt{T_h-1}
\exp\!\left(-\frac{b_\alpha(r-h)}{T_h^2}\right).
\end{aligned}
\tag{2}
$$

**Theorem 1.** For $r\geq2$, $1\leq h\leq r-1$ and $M=2^p$ with
$p\geq1$,

$$
M\sum_{v\bmod M}\mathbb P(u_r\equiv v\pmod M)^2
\leq 3+M\beta_\alpha^h+M\varepsilon_{r,h},
\tag{3}
$$

and

$$
M\sum_{v\bmod M}\mathbb P(W_r\equiv v\pmod M)^2
\leq 3h+M\beta_\alpha^h+(M-1)\varepsilon_{r,h}.
\tag{4}
$$

Consequently, for every

$$
0<c<\frac{-\log\beta_\alpha}{2\log3},
\tag{5}
$$

the left side of (3) has uniform upper limit at most $3$ as $r$ tends
to infinity over $1\leq p\leq c\log_2r$. In that range the left side
of (4) is $O_{\alpha,c}(\log r)$.

In fact, (3) and (4) hold for any integer $M\geq2$ relatively prime
to $3$. The proof only uses this coprimality in the collision count and
in multiplication by $L=3^{r-h}$. We emphasize powers of two because
they describe the subsequent Collatz parity window.

At the neutral mean $\mathbb E e_i=\log_2 3$, namely
$\alpha=\log_3 2$, the upper endpoint in (5) is
$0.227816060176\ldots$. The strict inequality in (5) is part of the
claim. For independent copies $u_r,u'_r$, equation (3) bounds the
collision probability $\mathbb P(u_r\equiv u'_r\pmod M)$ by its right
side divided by $M$.

**Theorem 2.** Put

$$
a_\alpha=\frac{8\alpha q}{3(1+q)}.
$$

For $2\leq h\leq r-1$,

$$
\max_{v\bmod M}\left|M\mathbb P(W_r\equiv v\pmod M)-1\right|
\leq M\sqrt{\frac{\pi}{a_\alpha(h-1)}}
+M\varepsilon_{r,h}.
\tag{6}
$$

In particular, relative pointwise uniformity holds when
$M=o(\sqrt{\log r})$. This is a smaller resolution than (5), with a
stronger mode of approximation. Bounded normalized energy in (3) does
not assert convergence to uniform measure in the range (5).

**Theorem 3.** For $r\geq2$, $1\leq h\leq r-1$ and any integer
$M\geq2$ relatively prime to $3$,

$$
\max_{v\bmod M}\left|M\mathbb P(u_r\equiv v\pmod M)-1\right|
\leq M\left(3^{-h}+8h\beta_\alpha^{h/2}+\varepsilon_{r,h}\right).
\tag{6a}
$$

In particular, the left side tends uniformly to zero for $M=2^p$ and
$1\leq p\leq c\log_2r$ whenever
$0<c<-\log\beta_\alpha/(4\log3)$. At the critical parameter this permits
every $c<0.113908030088\ldots$. Normalized canonical collision energy
then tends to $1$, and total variation from uniform tends to zero.
This is a smaller logarithmic range than (5). The pointwise assertion
is for the canonical endpoint; the raw integer retains the bounds
(4) and (6).

**Corollary 4 (Mahler's prefix refinement).** The shifted parity/trit
filtration of Mahler [6], proved in Section 5.2, gives explicit constants
$1/3<\gamma_\alpha<\beta_\alpha$ and $C_\alpha<\infty$.
In (3) and (4), $\beta_\alpha^h$ can be replaced by
$C_\alpha\gamma_\alpha^h$; in (6a), $\beta_\alpha^{h/2}$ can be replaced
by $\sqrt{C_\alpha}\,\gamma_\alpha^{h/2}$. Consequently the critical
logarithmic endpoints improve to $0.307971798026\ldots$ for bounded
energy and $0.153985899013\ldots$ for canonical pointwise uniformity.
The corresponding exact endpoints are $-\log\gamma_\alpha/(2\log3)$
and $-\log\gamma_\alpha/(4\log3)$, with strict inequalities as above.

**Corollary 5 (known tilted-fibre input).** For $\alpha>1/2$, put
$\kappa_\alpha=\alpha/(2-\alpha)$. The fixed-total fibre method
of [7, Section 7; 8, Sections 5.4--5.5], applied to the geometric law
as in Mahler [9, equation (1.10)], gives the stronger asymptotic ranges

$$
0<c<\frac{-\log\kappa_\alpha}{2\log3}
\quad\hbox{for bounded canonical energy and raw }O(\log r)\hbox{ energy},
\tag{6b}
$$

and

$$
0<c<\frac{-\log\kappa_\alpha}{4\log3}
\quad\hbox{for canonical relative pointwise uniformity}.
\tag{6c}
$$

At the critical parameter these endpoints are
$0.352577799009\ldots$ and $0.176288899504\ldots$, respectively. Section 5.3
provides the finite constants and a self-contained proof of the known
input. Mahler [9] identified these stronger consequences of our
projection bounds. Neither the prefix bound nor that substitution is
claimed as a new result here; Corollary 4 retains a useful bound without
the large tilt prefactor.


Section 10 also controls part of the actual spectrum used to project the
finite word jointly to its source residue and binary endpoint residue.
Neighborhoods of rational phases with denominators $2^r3^k$ have an
exponentially small weighted contribution below an explicit combined
denominator and width budget. The rate is positive at every fixed
fraction below the full scale, although its arithmetic threshold is
ineffective. Tao's corner identities then remove all pair paths visiting
a black triangle with a fixed macroscopic observed core, regardless of
the number of other triangle visits. The complementary paths remain
unestimated at linear precision.


Section 11 supplies a separate entropy estimate at the critical parameter.
For both the actual raw law and canonical endpoint, Shannon entropy divided
by the number of binary bits has lower limit at least
$H_2(\log_3 2)=0.949955527188\ldots$ on every fixed positive linear
precision band below $\log_2(3)n$. Every smaller dimension is attained by
some fixed Renyi order greater than one. The same conclusions retain each
exact total in every prescribed asymptotically critical window. The proof
separates simultaneous collisions of terminal words by a two-dimensional
fixed-place argument, including the actual canonical carries; uniform
composition counts give a subprobability whose mass deficit is exponentially small
and whose maximum atom is bounded. The threshold is ineffective. This estimate reaches
the critical source entropy from below and does not supply the strict
entropy gain needed for improved interval compression.


Theorem 11 extends the entropy estimate to every contiguous window of
linearly many output bits below the same total precision. A three-dimensional
fixed-place argument classifies its exceptional planes and bounds the number
of good terminal words whose outputs fall in a short ordinary interval.
This is a statement about marginal window laws, not about every conditional
dyadic component.


## 2. The raw integer and the canonical endpoint

The parity-coding bijection for the shortcut map gives $n_e$ uniquely
modulo $2^S$. One can also obtain it by recursively prescribing the next
parity: after $j$ steps the coefficient of the input in the affine formula
has an odd numerator and denominator $2^j$, so the next parity fixes
exactly one of the two lifts modulo $2^{j+1}$. Since the first parity is
odd, $0<n_e<2^S$. The affine composition is

$$
2^S u_r=3^r n_e+\sum_{i=1}^r3^{r-i}2^{E_{i-1}}.
\tag{7}
$$

Reducing (7) modulo $3^r$ proves $u_r\equiv W_r\pmod{3^r}$.
Indeed, replacing $2^{-S_i}$ by its residue modulo $3^i$ changes its
weighted summand by a multiple of $3^r$.

The negative integer $n_e-2^S$ has the same $S$ prescribed parities.
Its endpoint is $u_r-3^r$ by (7). The shortcut map preserves strict
negativity on negative integers, whereas the original positive trajectory
stays positive. Hence

$$
0<u_r<3^r,\qquad u_r=[W_r]_{3^r}.
\tag{8}
$$

This also identifies the carry $A_e=\lfloor W_r/3^r\rfloor$ as an
integer in $\{0,\ldots,r-1\}$, since $0<W_r<r3^r$.

For completeness, the relation to Rees's digit notation can be checked
directly. Let

$$
a_{i,L}=[-3^{-i}]_{2^L}.
$$

The integer

$$
Q_i=\frac{1+3^i a_{i,S_i}}{2^{S_i}}
$$

lies strictly between $0$ and $3^i$ and is congruent to $2^{-S_i}$
modulo $3^i$. Thus $Q_i=[2^{-S_i}]_{3^i}$. Write
$a_{i,S_i+p}=a_{i,S_i}+2^{S_i}d_i$, where
$d_i=\lfloor a_{i,S_i+p}/2^{S_i}\rfloor$. Divisibility of
$1+3^ia_{i,S_i+p}$ by $2^{S_i+p}$ gives

$$
W_r\equiv-3^r\sum_{i=1}^r d_i\pmod{2^p}.
\tag{9}
$$

This is the raw sum appearing in [1, Theorem 2.10 and Conjecture 4.1].
No infinite series or real approximation is used in (8) or (9).

## 3. Two elementary probabilistic inputs

### 3.1 Ternary collision decay

Let $\nu_h$ be the law on $\mathbb Z/3^h\mathbb Z$ of

$$
U_h=\sum_{j=1}^h3^{j-1}2^{-(e_1+\cdots+e_j)}\pmod{3^h},
\qquad U_0=0.
$$

This is the usual finite Syracuse offset, in the reversed-word convention
used in [2]. Its recursion is

$$
U_h=2^{-e_1}(1+3U'_{h-1})\pmod{3^h},
\tag{10}
$$

where $U'_{h-1}$ is independent and has law $\nu_{h-1}$.

**Lemma 3.** If $\mathcal E_h=\sum_x\nu_h(x)^2$, then
$\mathcal E_h\leq\beta_\alpha^h$.

*Proof.* A collision between two copies of (10) requires their first
exponents to have the same parity, by reduction modulo $3$. Conditional
on exponents $e,f$ with the same parity, equality in (10) imposes an
affine bijection between the two remaining offsets modulo $3^{h-1}$:

$$
V'=2^{f-e}U'+\frac{2^{f-e}-1}{3}\pmod{3^{h-1}}.
$$

Negative powers of two have their usual meaning in the ternary ring;
the displayed quotient is ternary integral because $e$ and $f$ have
the same parity. By Cauchy--Schwarz, the probability that two independent
$\nu_{h-1}$ variables obey any prescribed bijection is at most
$\mathcal E_{h-1}$. Now

$$
\mathbb P(e\text{ odd})=\frac1{1+q},\qquad
\mathbb P(e\text{ even})=\frac q{1+q}.
$$

It follows that $\mathcal E_h\leq\beta_\alpha\mathcal E_{h-1}$.
The base value is $\mathcal E_0=1$. $\square$

### 3.2 The suffix multiplier

The order of $2$ in $(\mathbb Z/3^h\mathbb Z)^\times$ is
$T_h=2\cdot3^{h-1}$. For example, this follows from the order $2$
modulo $3$ and the elementary identity
$v_3(4^j-1)=1+v_3(j)$. Thus the map
$s\mapsto[2^{-s}]_{3^h}$ bijects $\mathbb Z/T_h\mathbb Z$ with the
unit group.

**Lemma 4.** Let $R=r-h$ and let $S_*$ be the sum of $R$ independent
exponents. The law of $[2^{-S_*}]_{3^h}$ has $\ell^1$ distance at most
$\varepsilon_{r,h}$ from uniform measure on the units.

*Proof.* For one exponent, its characteristic function has modulus

$$
|g(t)|=\frac{\alpha}
{\sqrt{\alpha^2+2q(1-\cos(2\pi t))}}.
$$

If $d(t)=\operatorname{dist}(t,\mathbb Z)$, then
$1-\cos(2\pi t)\geq8d(t)^2$. The inequality
$\log(1+x)\geq x/(1+x)$ therefore gives

$$
|g(t)|\leq\exp(-b_\alpha d(t)^2).
$$

Parseval and Cauchy--Schwarz on $\mathbb Z/T_h\mathbb Z$ bound the
$\ell^1$ distance of $S_*\bmod T_h$ from uniform by

$$
\left(\sum_{j=1}^{T_h-1}|g(j/T_h)|^{2R}\right)^{1/2}
\leq\sqrt{T_h-1}\exp\!\left(-\frac{b_\alpha R}{T_h^2}\right).
$$

Apply the preceding bijection. $\square$

## 4. A collision count allowing a correlated translation

The next lemma is a multiplicative universal-hashing estimate adapted to
canonical representatives in a prime-power ring. Its proof is included
to make the treatment of translations and nonunit differences explicit.

**Lemma 5.** Put $N=3^h$ and let $\nu$ be any probability law on
$\mathbb Z/N\mathbb Z$. Let $U,V$ be independent with law $\nu$.
For a unit $a\bmod N$, define

$$
\begin{aligned}
H_M(0)&=1,\\
H_M(d)&=\mathbf1_{\{M\mid d\text{ or }M\mid(d-N)\}},
\qquad 0<d<N,\\
B_\nu(a)&=\mathbb E H_M([a(U-V)]_N).
\end{aligned}
$$

For every integer $b$, the collision probability modulo $M$ of
$[aU+b]_N$ is at most $B_\nu(a)$. Moreover $0\leq B_\nu\leq1$, and

$$
\mathbb E_{a\text{ uniform unit}}B_\nu(a)
\leq\sum_x\nu(x)^2+\frac3M.
\tag{11}
$$

*Proof.* If $d=[a(U-V)]_N$, the difference of the canonical
representatives $[aU+b]_N$ and $[aV+b]_N$ is either $d$ or $d-N$.
This proves the pointwise upper bound simultaneously for all $b$.

Fix a nonzero difference $D=U-V\pmod N$, and put $v=v_3(D)<h$.
For $H_M([aD]_N)=1$, there must be a nonzero integer $t$ such that

$$
aD\equiv tM\pmod N,\qquad 0<|t|<N/M.
\tag{12}
$$

Since $3$ does not divide $M$, equation (12) requires $3^v\mid t$.
There are at most $2N/(M3^v)$ such nonzero integers. For each $t$,
the congruence has at most $3^v$ unit solutions $a$. Dividing by the
$2N/3$ units gives probability at most $3/M$ for this fixed nonzero
$D$. For $D=0$, use the bound $1$. Averaging proves (11).
$\square$

The translation $b$ may depend arbitrarily on $a$ and on further
randomness. This is the reason for first bounding collisions by the
single function $B_\nu(a)$ instead of introducing an independent
translation.

## 5. Proof of the canonical and raw energy bounds

Split the original exponent word after $h$. Put
$N=3^h$, $L=3^{r-h}$, and

$$
a=[2^{-S_{h+1}}]_N.
$$

For a prefix word of length $h$, define

$$
X_h(a)=\sum_{i=1}^h3^{h-i}
[a2^{-(e_i+\cdots+e_h)}]_{3^i}.
$$

Then, as an identity of integers,

$$
W_r=LX_h(a)+Y,
\tag{13}
$$

where $Y$ is the sum of the terms of (1) with $i>h$ and is determined
entirely by the suffix. Also

$$
X_h(a)\equiv aU_h(e_h,\ldots,e_1)\pmod N.
\tag{14}
$$

Reversal preserves the iid prefix law. Write $Y=Lb+c_0$, with
$0\leq c_0<L$. Equations (8), (13) and (14) give the exact split

$$
u_r=L[aU_h+b]_N+c_0.
\tag{15}
$$

Conditional on the entire suffix, $(a,b,c_0)$ is fixed and $U_h$ has
the independent law $\nu_h$. Since $\gcd(L,M)=1$, multiplication by $L$
permutes residues modulo $M$. Lemma 5 therefore bounds the conditional
collision energy of (15) by $B_{\nu_h}(a)$.

Collision energy is a convex function of a probability vector. Hence
the unconditional collision probability is at most the average
conditional collision probability, and thus at most
$\mathbb E B_{\nu_h}(a)$. Lemma 4 changes this last expectation to a
uniform-unit expectation at a cost at most $\varepsilon_{r,h}$.
Only the marginal law of $a$ is changed; all correlation between $a$
and $b$ was already accommodated by the pointwise bound in Lemma 5.
Lemmas 3 and 5 now give

$$
\sum_v\mathbb P(u_r\equiv v\pmod M)^2
\leq\frac3M+\beta_\alpha^h+\varepsilon_{r,h},
$$

which proves (3).

For the raw sum, the same count uses $0<X_h(a)<hN$. For two prefix
words with unequal ternary offsets, a collision modulo $M$ implies

$$
X_h(a,e)-X_h(a,f)=tM,\qquad
a\bigl(U_h(e^{\rm rev})-U_h(f^{\rm rev})\bigr)
\equiv tM\pmod N,
\quad 0<|t|<hN/M.
$$

The proof of Lemma 5 bounds the uniform-unit average of this event by
$3h/M$. Equal ternary offsets contribute at most
$\mathcal E_h\leq\beta_\alpha^h$. Consequently

$$
\mathbb E_{a\text{ uniform unit}}
\sum_v\mathbb P(X_h(a)\equiv v\pmod M)^2
\leq\frac{3h}M+\beta_\alpha^h.
\tag{16}
$$

To retain the slightly smaller error in (4), write
$F_h^\xi(a)=\mathbb E\exp(2\pi i\xi X_h(a)/M)$.
Conditional expectation in (13), followed by Cauchy--Schwarz, gives

$$
\left|\mathbb E\exp(2\pi i\xi W_r/M)\right|^2
\leq\mathbb E_{\rm suffix}|F_h^{\xi L}(a)|^2.
\tag{17}
$$

Each square is at most $1$, so replacing the multiplier law costs at
most $\varepsilon_{r,h}$ for each nonzero frequency. At frequency zero
both expectations equal $1$ exactly. Summing (17), applying Parseval,
and using (16) proves (4).

For (5), choose $\eta$ so that

$$
\frac{c\log3}{-\log\beta_\alpha}<\eta<\frac12,
\qquad h=\lfloor\eta\log_3r\rfloor.
$$

Then $M\beta_\alpha^h\to0$ uniformly for $M\leq r^c$.
Since $T_h^2=O(r^{2\eta})$, the term $M\varepsilon_{r,h}$ tends to
zero faster than every negative power of $r$. This proves the stated
uniform upper limit and raw $O(\log r)$ bound. $\square$

### 5.1. Canonical pointwise uniformity

We prove Theorem 3. The projection of $\nu_h$ modulo $3^d$ is exactly
$\nu_d$ for $0\leq d\leq h$, by the recursion in Lemma 3. Write
$\mathcal E_d=\sum_x\nu_d(x)^2$, with $\mathcal E_0=1$, and
$\widehat\nu_h(t)=\sum_x\nu_h(x)e(tx/3^h)$, where
$e(y)=\exp(2\pi i y)$. If $t$ has additive conductor $3^d$, averaging
over a uniform unit $a\bmod3^h$ gives

$$
\mathbb E_a|\widehat\nu_h(at)|^2
=\frac32\mathcal E_d-\frac12\mathcal E_{d-1}
\leq\frac32\beta_\alpha^d.
\tag{17a}
$$

Indeed, the uniform-unit average of $e(aD/3^d)$ equals $1$ when
$3^d\mid D$, equals $-1/2$ when $3^{d-1}\mid D$ but $3^d\nmid D$,
and equals zero otherwise. Expand the square and use the two projected
collision probabilities. Cauchy--Schwarz bounds the corresponding
first absolute moment by $\sqrt{3/2}\,\beta_\alpha^{d/2}$.

Put $N=3^h$ and $A_v=\{x\in[0,N):x\equiv v\pmod M\}$ for
$0\leq v<M$. Its cardinality $\ell_v$ satisfies
$|\ell_v/N-1/M|\leq1/N$. For $t\ne0\pmod N$, a geometric series gives

$$
\left|\frac1N\sum_{x\in A_v}e(-tx/N)\right|
\leq\frac1{N|\sin(\pi tM/N)|}.
\tag{17b}
$$

The denominator is nonzero because $M$ is coprime to $N$. The bound
also covers an empty bucket. Fourier inversion now gives, simultaneously
for every translation $b\bmod N$ and every bucket $v$,

$$
\left|\mathbb P([aU_h+b]_N\equiv v\pmod M)-\frac1M\right|
\leq\frac1N+
\sum_{t=1}^{N-1}\frac{|\widehat\nu_h(at)|}
 {N|\sin(\pi tM/N)|}.
\tag{17c}
$$

Group $t$ by conductor, writing $t=3^{h-d}z$ with $z$ a unit modulo
$3^d$. Multiplication by $M$ permutes those units. For odd $Q\geq3$,
symmetry and $\sin(\pi z/Q)\geq2z/Q$ for $1\leq z\leq Q/2$ imply

$$
\sum_{z=1}^{Q-1}|\sin(\pi z/Q)|^{-1}
\leq Q H_{(Q-1)/2}\leq Q(1+\log Q),
$$

where $H_j=\sum_{i=1}^j1/i$. Let $F(a)$ be the supremum of the left
side of (17c) over $b,v$. Averaging its upper bound using (17a) yields

$$
\begin{aligned}
\mathbb E_a F(a)
&\leq3^{-h}+\sqrt{\frac32}\,3^{-h}
\sum_{d=1}^h(3\sqrt{\beta_\alpha})^d(1+d\log3)\\
&\leq3^{-h}+8h\beta_\alpha^{h/2}.
\end{aligned}
\tag{17d}
$$

For the last inequality, $\beta_\alpha\geq1/2$ implies
$t=3\sqrt{\beta_\alpha}>2$, so $\sum_{d=1}^ht^d<2t^h$.
Also $\sqrt{3/2}<3/2$ and $1+h\log3<(5/2)h$ for $h\geq1$.

In the actual split (15), a fixed output residue corresponds to the
bucket $L^{-1}(v-c_0)\bmod M$. The supremum defining $F(a)$ allows this
suffix-dependent bucket and the correlated translation $b$. Since
$0\leq F(a)\leq1$, Lemma 4 changes its expectation by at most
$\varepsilon_{r,h}$. Averaging the conditional discrepancy and applying
(17d) proves (6a).

For its asymptotic statement, choose
$2c\log3/(-\log\beta_\alpha)<\eta<1/2$ and
$h=\lfloor\eta\log_3r\rfloor$. All three terms in (6a) then tend
uniformly to zero for $M\leq r^c$. If their sum is $\delta$, writing the
residue masses as $(1+d_v)/M$ gives $\sum_vd_v=0$ and
$|d_v|\leq\delta$. Thus normalized energy is at most $1+\delta^2$
and total variation at most $\delta/2$. $\square$

### 5.2. Mahler's stronger prefix input

Mahler's shifted parity/trit filtration [6] sharpens the ternary input
used above. We include a proof, with the corrected trit factor. Put

$$
A_\alpha=\frac{1-q+q^2}{(1+q)^2},\qquad
r_s=q^{2\cdot3^{s-1}},\qquad
b_m=\frac13+\frac23A_\alpha
\prod_{s=1}^m\frac{(1-r_s)^2}{1+r_s+r_s^2},
\quad \Gamma_h=\prod_{m=0}^{h-1}b_m.
\tag{17e}
$$

Then $b_0=\beta_\alpha$ and

$$\mathcal E_h\leq\Gamma_h.\tag{17f}$$

To prove this, reverse the iid word if necessary and work with its
chronological canonical endpoint. Write the mixed-radix expansion

$$
e_j-1=(1-\eta_j)+2\sum_{s\geq1}c_j^{(s)}3^{s-1},
\qquad \eta_j\in\{0,1\},\quad c_j^{(s)}\in\{0,1,2\}.
$$

The geometric weights factor, so these coordinates are independent,
with $\mathbb P(\eta_j=1)=1/(1+q)$ and
$\mathbb P(c_j^{(s)}=c)=r_s^c/(1+r_s+r_s^2)$. Only the coordinates
$s\leq j-1$ affect the endpoint: in (1), $e_j$ is used only modulo
$2\cdot3^{j-1}$. Group the relevant independent variables into

$$
\mathcal D_i=(1-\eta_i,c_{i+1}^{(1)},\ldots,c_h^{(h-i)}),
\qquad 1\leq i\leq h.
$$

Let $\kappa_i$ be the coefficient of $3^{h-i}$ in $u_h-1$. The lower
suffix digits are functions of $\mathcal D_{i+1},\ldots,\mathcal D_h$.
Conditional on those later diagonals, $\kappa_i$ is a fixed translate
modulo three of

$$
-(-1)^{S_{i+1}}(1-\eta_i)
-\sum_{s=1}^{h-i}(-1)^{S_{i+s}}c_{i+s}^{(s)}.
\tag{17g}
$$

Here $S_j=e_j+\cdots+e_h$ and $S_{h+1}=0$. All displayed signs are
measurable in the later diagonals. For completeness, changing
$c_{i+s}^{(s)}$ changes $e_{i+s}$ by $2\cdot3^{s-1}$.
In the raw sum for the suffix beginning at $i$, every earlier summand
has a multiplicative period dividing this increment, and every later
summand is unaffected. Its own summand changes by
$-(-1)^{S_{i+s}}3^{h-i}$ modulo $3^{h-i+1}$, because
$4^{-3^{s-1}}\equiv1-3^s\pmod{3^{s+1}}$. The parity coordinate gives
the first term in (17g). This also proves the asserted lower-digit
invariance and triangular dependence.

For $\omega=e^{2\pi i/3}$, the squared modulus of the parity
characteristic function is $A_\alpha$, while that of each trit is
$(1-r_s)^2/(1+r_s+r_s^2)$; signs and translates do not change these
moduli. Parseval on $\mathbb Z/3\mathbb Z$ therefore makes the
conditional digit collision norm exactly $b_{h-i}$. Conditional Jensen
bounds the same norm when only the later digits are given. Multiplying
these bounds in the chain rule for collision probabilities proves (17f).

The limit $\gamma_\alpha=\lim_m b_m$ satisfies
$1/3<\gamma_\alpha<\beta_\alpha$. Also

$$
C_\alpha:=\prod_{m=0}^{\infty}\frac{b_m}{\gamma_\alpha}<\infty,
\qquad \Gamma_h\leq C_\alpha\gamma_\alpha^h.
\tag{17h}
$$

Indeed, $1-(1-r)^2/(1+r+r^2)\leq3r$, so
$\sum_{m\geq0}(b_m-\gamma_\alpha)
\leq2A_\alpha\sum_{s\geq1}s r_s<\infty$.
The infinite product defining $\gamma_\alpha-1/3$ is positive for the
same reason. Using $\log(1+x)\leq x$ proves convergence in (17h).

Equations (3) and (4) hold with $\beta_\alpha^h$ replaced by $\Gamma_h$.
The proof of (17d) uses $\sqrt{\Gamma_d}$ at conductor $3^d$, and gives

$$
\max_v|M\mathbb P(u_r\equiv v\pmod M)-1|
\leq M\left(3^{-h}+8h\sqrt{C_\alpha}\,
\gamma_\alpha^{h/2}+\varepsilon_{r,h}\right).
\tag{17i}
$$

The constant eight remains valid: for $t=3\sqrt{\gamma_\alpha}>\sqrt3$
we have $t/(t-1)<5/2$, while $\sqrt{3/2}<5/4$ and
$1+\log3<5/2$. Thus the geometric-series constant is below $125/16<8$.
The logarithmic endpoints become $-\log\gamma_\alpha/(2\log3)$ for
bounded energy and $-\log\gamma_\alpha/(4\log3)$ for canonical pointwise
uniformity. Critically these are $0.307971798026\ldots$ and
$0.153985899013\ldots$, respectively. This improves the prefix input;
it leaves the short-suffix resolution restriction in place.

### 5.3. The known tilted-fibre bound

We record the stronger asymptotic input explicitly to distinguish it
from the finite-depth diagonal refinement. The fixed-total counting
argument is from [7, Section 7, equations (24)--(25); 8, Section 5.5].
Its geometric-parameter form below and its consequences for the present
projection estimates were stated by Mahler [9, equation (1.10)].
The argument is included for completeness, with our unnormalized energy
$\mathcal E_h$.

Suppose $\alpha>1/2$ and choose $1<t<1/(4q^2)$. Define

$$
B(t)=\frac{\alpha^2}{1-tq^2},\qquad
R(t)=\frac{2(1-tq^2)}{3(1-2tq^2)},\qquad
C(t)=\frac{t}{t-1}\left(1+\frac{2}{3(1-R(t))}\right).
\tag{17j}
$$

Then $R(t)<1$ and

$$
\mathcal E_h\leq C(t)B(t)^h.
\tag{17k}
$$

To prove this, for a chronological word $w$ let $d=E_h$ and

$$
A(w)=\sum_{i=1}^h3^{h-i}2^{E_{i-1}},\qquad
V(w)=\frac{A(w)}{3^h}
=\frac13\sum_{j=0}^{h-1}\prod_{i=1}^j\frac{2^{e_i}}3.
$$

Let $N_d(x)$ count words with total $d$ and canonical endpoint $x$.
Their numerators $A(w)$ are positive and congruent to $2^d x$ modulo
$3^h$. They are distinct: if two coincide, (7) gives the same canonical
source $n_w$, whose first $d$ parities determine the word. Ordering the
numerators in a fixed fibre therefore gives

$$
N_d(x)^2\leq N_d(x)+2\sum_{w:E_h=d,\,u_h=x}V(w).
$$

Every such word has probability $\alpha^h q^{d-h}$. Since reversal
preserves the word law, its canonical energy is $\mathcal E_h$.
Weighted Cauchy--Schwarz over $d\geq h$, with weights $t^{-d}$, yields

$$
\begin{aligned}
\mathcal E_h
&\leq\frac{t^{1-h}}{t-1}
 \sum_{x,d\geq h}t^d\alpha^{2h}q^{2(d-h)}N_d(x)^2\\
&\leq\frac{t}{t-1}B(t)^h\,
 \mathbb E_t[1+2V(w)],
\end{aligned}
$$

where under $\mathbb P_t$ the letters are independent with
$\mathbb P_t(e=j)=(1-tq^2)(tq^2)^{j-1}$. The nonnegative sums may
first be truncated and then passed to the limit. Under this tilted law,

$$
\mathbb E_t\frac{2^e}3=R(t),\qquad
\mathbb E_t V(w)=\frac13\sum_{j=0}^{h-1}R(t)^j
\leq\frac1{3(1-R(t))}.
$$

This proves (17k). In (3) and (4) one may consequently replace
$\beta_\alpha^h$ by $C(t)B(t)^h$. Because $B(t)>1/3$, the same
geometric-series estimate used for (17i) gives

$$
\max_v|M\mathbb P(u_r\equiv v\pmod M)-1|
\leq M\left(3^{-h}+8h\sqrt{C(t)}B(t)^{h/2}
+\varepsilon_{r,h}\right).
\tag{17l}
$$

Finally $B(t)\downarrow\kappa_\alpha<1$ as $t\downarrow1$.
For each strict range in (6b) or (6c), choose a fixed $t>1$ sufficiently
close to one and apply the asymptotic argument of Section 5. The
constant $C(t)$ is finite for that choice; it diverges as $t\downarrow1$.
No finite prefactor at $t=1$, endpoint equality, or local ratio bound
$\mathcal E_{h+1}/\mathcal E_h\leq\kappa_\alpha$ is asserted.

## 6. Relative pointwise approximation of the raw law

We give the Fourier argument for Theorem 2 separately because its
conclusion is stronger than an energy bound but holds at a smaller
resolution. All norms in this section use normalized counting measure
on the relevant ternary unit group.

For $n\geq1$, let $V_n(a)=[2^{-1}a]_{3^n}$ and let
$P_ng=g\circ V_n$. Peeling off the last exponent in the raw sum gives

$$
F_n^\xi(a)=\sum_{e\geq1}\alpha q^{e-1}
\exp\!\left(\frac{2\pi i\xi V_n^e(a)}M\right)
F_{n-1}^{3\xi}\bigl(V_n^e(a)\bmod3^{n-1}\bigr).
\tag{18}
$$

Here $F_0=1$. For $n\geq2$, put $m=3^{n-1}$ and, for a function $f$
on the units modulo $m$, define its phase-weighted lift

$$
g(a)=\exp(2\pi i\xi a/M)f(a\bmod m).
$$

This is an isometry because each unit has three lifts. For a fixed
$b\bmod m$, the three differences $V_n(b+tm)-(b+tm)$, $t=0,1,2$,
are, in some order, $c_b-m,c_b,c_b+m$, where

$$
c_b=\begin{cases}-b/2,&b\text{ even},\\(m-b)/2,&b\text{ odd}.
\end{cases}
$$

Therefore, writing $A(t)=(1+2\cos(2\pi t))/3$, and applying
Cauchy--Schwarz to the remaining lower-level permutation,

$$
|\langle g,P_ng\rangle|
\leq |A(\xi m/M)|\,\|f\|_2^2.
\tag{19}
$$

Let $Q_n=\sum_{e\geq1}\alpha q^{e-1}P_n^e$. In the expansion of
$\|Q_ng\|_2^2$, all weights are nonnegative and sum to $1$. The two
lag-one parts have total weight

$$
D_\alpha=2\sum_{e\geq1}\alpha^2q^{2e-1}
=\frac{2\alpha q}{1+q}.
$$

Use (19) for those parts and the unitary bound for every other lag:

$$
\|Q_ng\|_2^2
\leq\left[1-D_\alpha(1-|A(\xi m/M)|)\right]\|f\|_2^2.
\tag{20}
$$

In (18), the next frequency is $3\xi$ and the next value of $m$ is
$m/3$, so the argument of $A$ stays fixed. At depth $1$ use only
$|F_1^\xi|\leq1$. For $x=\operatorname{dist}(t,\mathbb Z)\leq1/2$,

$$
1-|A(t)|\geq\frac83x^2.
$$

For $A(t)\geq0$ this follows from
$1-A(t)=\frac43\sin^2(\pi x)\geq\frac{16}3x^2$; for $A(t)<0$
use $1+A(t)\geq2/3$. Iterating (20) yields

$$
\|F_h^\xi\|_2
\leq\exp\!\left(-a_\alpha(h-1)
\operatorname{dist}\!\left(\frac{\xi3^{h-1}}M,\mathbb Z\right)^2\right).
\tag{21}
$$

This is an average over initial units. To apply it to the actual law,
condition on the independent suffix in (13), remove its phase by the
triangle inequality, and apply Lemma 4. The uniform $L^1$ norm of the
prefix characteristic function is at most its $L^2$ norm. Thus

$$
\left|\mathbb E\exp(2\pi i\xi W_r/M)\right|
\leq\exp\!\left(-a_\alpha(h-1)
\operatorname{dist}\!\left(\frac{\xi3^{r-1}}M,\mathbb Z\right)^2\right)
+\varepsilon_{r,h}.
\tag{22}
$$

Multiplication by $3^{r-1}$ permutes frequencies modulo $M$.
Fourier inversion and the Gaussian sum estimate

$$
\sum_{j=1}^{M-1}\exp\!\left(-a_\alpha(h-1)
\operatorname{dist}(j/M,\mathbb Z)^2\right)
\leq2\int_0^\infty\exp\!\left(-\frac{a_\alpha(h-1)x^2}{M^2}\right)dx
=M\sqrt{\frac\pi{a_\alpha(h-1)}}
$$

prove (6). Taking $h=\lfloor\frac14\log_3r\rfloor$ gives an error
$O_\alpha(M/\sqrt{\log r})$ plus
$M r^{1/8}\exp(-c_\alpha\sqrt r)$ for sufficiently large $r$, which
proves the pointwise conclusion. $\square$

The argument for (6) also applies to every integer $M\geq2$ relatively
prime to $3$, since its only modular requirement is that multiplication
by $3^{r-1}$ permutes the frequencies.

## 7. Relation to earlier work and remaining scale gap

The raw digit formula and the proposed linear-resolution uniformity are
from Rees [1]. We prove the endpoint dictionary directly in Section 2,
then obtain a shorter unconditional resolution. The same-parameter
canonical estimate (3) avoids a loss from the word-dependent integer
carry. Rees's conjectural linear resolution is still open.

Universal hashing [4,5] supplies the general collision-counting viewpoint.
We do not claim the invention of multiplicative hashing. Lemma 5 proves
the particular prime-power variant needed here, including differences
divisible by powers of three and translations correlated with the
multiplier. The original Carter--Wegman paper is cited for this historical
framework; no unverified theorem from it is an input. The accessible
exposition [5] was read, and all counting estimates used here are proved
in Section 4.

Tao's work [2] provides the standard Syracuse offset framework and proves
much stronger ternary fine-scale mixing at the mean-two law. Our estimates
concern dyadic projections, include the critical mean $\log_2 3$, and
are proved without importing a fine-scale ternary mixing assertion for
that changed law. The critical geometric word entropy is smaller than
$\log3$ per exponent, so full ternary smoothing at that parameter cannot
be assumed.

More generally, Leen [3, Theorem E(a) and Section 8] records the extension
of Tao's primitive Fourier estimate to every fixed
$\alpha<\log_3 2$, with constants uniform on compact subintervals. It is
explicitly identified there as prior art from Tao's pair/renewal argument
and the renewal theorem of Goncalves, Greenfeld and Madrid. Combining
that estimate with (17b), splitting conductors at $d=r/2$, gives canonical
relative error $O_{A,\alpha}(M[r3^{-r/2}+r^{1-A}])$ for every $A>0$.
Thus canonical pointwise uniformity already holds on every fixed
polynomial range $M\leq r^C$ throughout this strictly subcritical
parameter range, including the mean-two case $\alpha=1/2$. We claim no
new such conclusion there. Theorem 3 also covers $\alpha\geq\log_3 2$;
the strict slope hypothesis in [3] does not include the critical equality.
Leen's fixed-total obstruction concerns full ternary energy, a different
quantity from the dyadic projections proved here. Sections 3 and 6--8
of [3] were read; its finite certificate suite was not independently run.

Cassian Mahler's public discussion [10] pointed out that the suffix carry
can be subtracted before averaging the prefix. This motivated retaining
the exact canonical range in (15). That observation is credited here;
the direct translation bound in Lemma 5 and its use in (15) supply (3).

The primitive-frequency identity (17a) is standard Fourier orthogonality
over ternary units. Its mean-two specialization and related spectral
identities are explicit in Mahler [11, Section 2] and his earlier discussion
linked there. We do not claim that identity as new. Here it is combined
with the residue-bucket geometric series, a supremum over correlated
translations, and the actual short-suffix transfer to prove (6a) for
every geometric parameter.

Mahler's further source-composition dictionary [10,12] identifies
$c_0=u_v$, $U_h=u_u$, and $b\equiv-a n_v\pmod N$ for prefix $u$ and
suffix $v$. Hence (15) can also be written
$u_{(u,v)}=u_v+L[a(u_u-n_v)]_N$. This useful identification does not
make the suffix source, endpoint and multiplier independent. Both
canonical estimates retain their correlation. Mahler's later diagonal
filtration [6] is the stronger prefix input in Corollary 4; that refinement
is credited to him and its corrected proof is included in Section 5.2.

Mahler [9, Proposition 1.1] reproduces the canonical projection
reductions, with attribution to our earlier public derivation in post 36.
That paper appeared before the original version of this manuscript; the
shared canonical argument is explicitly acknowledged here. The separate
raw-law estimates are also proved in the present manuscript.

Subsequent mod9 and resolvent refinements by Mahler [9] improve the
critical prefix step ratio further, below $1/2$. His equation (1.10)
also identifies the stronger global asymptotic base furnished by the
earlier tilted-fibre method [7,8]. Section 5.3 includes that input and
its stronger projection consequences with explicit attribution. A global
bound with a prefactor does not imply the same bound on a one-step
energy ratio. We use neither the printed resolvent coefficients nor a
numerical crossover depth from [9]. All these prefix estimates retain
the short-multiplier-seed limitation described next.

The limitation of the collision-energy proof has a specific source. The multiplier in
(13) depends on one suffix sum, with spread of order $\sqrt r$ for fixed
$\alpha$. Uniformity over its complete period $T_h$ is available in
Lemma 4 only at the short depth used above. Taking $h$ proportional to
$r$ would invalidate the small-error conclusion. Further information
in the actual suffix translation is discarded by convexity in Section 5.

These results control a probability law on exponent words. They do not
establish descent for an individual positive integer, a stronger
compression exponent, or the Collatz conjecture. A polynomial bound for
normalized collision energy at $p$ proportional to $r$ would be a
substantially stronger arithmetic input. Equations (3)--(6a) provide
explicit estimates for slowly growing moduli. Theorem 6 adds polynomial
individual-character decay at linear bit precision, and upgrades canonical
energy to convergence to one throughout the earlier bounded-energy
logarithmic range. It does not sum exponentially many squared coefficients.

Rees [1, Conjecture 4.5] asks for exponential character decay for the raw
digit law. The new theorem gives polynomial decay for the canonical law,
so that conjecture remains open. The primitive bound in Section 8 is an
elementary consequence of the accepted exact split, multiplier mixing and
collision estimates, with the normalized unit average kept explicit. No
new input theorem about collision contraction or random-walk mixing is
claimed. It applies at the critical parameter and above, whereas the
stronger super-polynomial input in [3, Section 8] requires strict
subcriticality. The fixed-total resonances in that source remove the clock
diffusion used here and do not contradict the iid estimate.

Theorem 7 addresses exact critical totals separately. Fourier Wren [13]
previously sketched unfolding bounded chains of black triangles and using
the Subspace Theorem. Appendix A supplies the complete application,
including interleaved visits and cancelling groups, using Schlickewei's
theorem as stated in Bilu [14, Theorem 2.3]. Section 9 extends the
all-triangle excursion penalty to the adapted composition bridge, counts
boundary-carry words at each fixed total, and treats conductor reduction
as a mixture of nearby critical clocks. This does not apply the iid
projective identity to a conditioned law. The critical positive-majorant
argument is qualitative and has no threshold effective in triangle count.
In its fixed-place product, the potentially large initial coefficient
cancels; retaining its separate binary valuation permits linear precision.
Centering the iid comparison law at the prescribed total covers arbitrary
$o(n)$ critical windows without a rare-event normalization loss.

## 8. Polynomial character decay for canonical endpoints

Write $e(x)=\exp(2\pi i x)$ and let $\mu_n$ be the law of $u_n$ modulo
$3^n$. Put

$$
\widehat\mu_n(t)=\mathbb E e(tu_n/3^n),\qquad
R_\alpha(n)=\max_{3\nmid t}|\widehat\mu_n(t)|,\qquad
\mathcal E_\alpha(h)=\sum_x\mu_h(x)^2.
$$

**Theorem 6 (canonical character decay).** For every fixed $\alpha\in(0,1)$ and every prescribed
positive envelope $M_n=o(3^n)$,

$$
\sup_{2\le2^p\le M_n}\max_{1\le k<2^p}
\left|\mathbb E e(ku_n/2^p)\right|\longrightarrow0.
\tag{8.1}
$$

Empty suprema may be omitted. There is also a quantitative statement at
every fixed linear bit precision. Set $q=1-\alpha$ and

$$
\beta_\alpha=\frac{1+q^2}{(1+q)^2}.
$$

For every fixed $0<\lambda<\log_2 3$ and
$0<a<-\log\beta_\alpha/(4\log3)$,

$$
\sup_{1\le p\le\lambda n}\max_{1\le k<2^p}
\left|\mathbb E e(ku_n/2^p)\right|
\le C_{\alpha,a,\lambda}n^{-a}.
\tag{8.2}
$$

For $\alpha>1/2$, the credited tilted-fibre input in Section 5.3 and [9, Section 1.2] allows every

$$
0<a<A_\alpha:=\frac{-\log(\alpha/(2-\alpha))}{4\log3}.
\tag{8.3}
$$

At criticality $\alpha=\log_3 2$ this endpoint is
$A_\alpha=0.176288899504\ldots$.

Consequently, at criticality, normalized binary collision energy tends
to one and total variation from uniform tends to zero, uniformly for
$1\le p\le c\log_2 n$ whenever

$$
c<2A_\alpha=0.352577799009\ldots.
\tag{8.4}
$$

The earlier estimates in Theorem 1 and Corollary 5 give only an upper
limit of three for energy in this range. Neither (8.1) nor (8.2) controls energy at linear
bit precision: there are exponentially many characters.

### 8.1. Primitive decay from the accepted short-block identity

The inputs of this section are proved in Sections 2--5. We spell out
their combination because the normalization of the Fourier average matters.
For $1\le h<n$, set $N=3^h$, $L=3^{n-h}$. Equation (15) is the
exact integer identity

$$
u_n=L[aU_h+b]_N+c_0,
\tag{8.5}
$$

where, conditional on the entire suffix, $a,b,c_0$ are fixed, $U_h$ has
the independent law $\mu_h$, and
$a=[2^{-S_*}]_N$ for the suffix exponent sum $S_*$. Brackets denote the
representative in $[0,N)$. No independence among $a,b,c_0$ is asserted.
At a ternary frequency the canonical carry contributes an integer phase:

$$
\mathbb E[e(\xi u_n/3^n)\mid\mathrm{suffix}]
=e(\xi b/N+\xi c_0/3^n)\widehat\mu_h(\xi a).
\tag{8.6}
$$

The phase may be correlated with $a$ but has modulus one. Jensen gives

$$
|\widehat\mu_n(\xi)|^2
\le\mathbb E|\widehat\mu_h(\xi a)|^2.
\tag{8.7}
$$

Let $T_h=2\cdot3^{h-1}$ and
$b_\alpha=8q/(\alpha^2+4q)$. Lemma 4 bounds the $\ell^1$
distance of the multiplier marginal from uniform on the units by

$$
\epsilon_{n,h}=\sqrt{T_h-1}
\exp\left(-\frac{b_\alpha(n-h)}{T_h^2}\right).
\tag{8.8}
$$

The squared integrand in (8.7) lies in $[0,1]$. If $3\nmid\xi$,
multiplication by $\xi$ permutes the units. Finite Parseval therefore gives

$$
\begin{aligned}
R_\alpha(n)^2
&\le\frac1{2\cdot3^{h-1}}
\sum_{t\in(\mathbb Z/3^h\mathbb Z)^\times}
|\widehat\mu_h(t)|^2+\epsilon_{n,h}\\
&\le\frac32\mathcal E_\alpha(h)+\epsilon_{n,h}.
\end{aligned}
\tag{8.9}
$$

The collision probability here is unnormalized. There is no extra factor
$3^h$ after averaging over the unit frequencies.

Lemma 3 gives $\mathcal E_\alpha(h)\le\beta_\alpha^h$.
Choose $h=\lfloor\eta\log_3n\rfloor$, with $\eta<1/2$ fixed.
The error in (8.8) decays faster than every negative power of $n$.
Taking square roots in (8.9) proves

$$
R_\alpha(n)\le C_{\alpha,a}n^{-a}
\quad\left(0<a<\frac{-\log\beta_\alpha}{4\log3}\right).
\tag{8.10}
$$

For $\alpha>1/2$, the previously attributed fixed-total fibre estimate
in Section 5.3 and [9, Section 1.2] gives, for every fixed
$1<t<1/(4q^2)$,

$$
\mathcal E_\alpha(h)\le C_{\alpha,t}
\left(\frac{\alpha^2}{1-tq^2}\right)^h.
$$

As $t\downarrow1$ the base tends to $\alpha/(2-\alpha)$. For a
prescribed $a<A_\alpha$, choose one fixed $t>1$ and then one fixed
$\eta<1/2$ to obtain (8.10) with that $a$. No parameter tends to its
endpoint with $n$.

The polynomial primitive estimate concerns the iid law. It does not
imply the same estimate after conditioning on the total exponent sum.
That conditioning removes the multiplier diffusion used in (8.8).

### 8.2. A boundary estimate for the actual canonical law

Projectivity of the Syracuse law, including the iid reversal that identifies
it with the canonical endpoint law, gives exactly

$$
\widehat\mu_n(3^{n-r}\xi)=\widehat\mu_r(\xi).
\tag{8.11}
$$

Fix any exponent $a$ allowed in (8.10) and put $X_n=u_n/3^n$. For
$0<\delta\le1/8$, the periodic tent

$$
f_\delta(x)=2\max\left(1-\frac{\operatorname{dist}(x,\mathbb Z)}{2\delta},0\right)
$$

majorizes the indicator of $\operatorname{dist}(x,\mathbb Z)\le\delta$.
Its Fourier coefficients are nonnegative, its constant coefficient is
$4\delta$, and the sum of its coefficients is $f_\delta(0)=2$.
The squared-sinc formula bounds the tail beyond $H$ by $C/(\delta H)$.
It follows that

$$
\mathbb P(\min(X_n,1-X_n)\le\delta)
\le4\delta+2\max_{1\le|t|\le H}|\widehat\mu_n(t)|
+\frac{C}{\delta H}.
\tag{8.12}
$$

For $H<3^n$, a nonzero $|t|\le H$ has conductor
$r=n-v_3(t)\ge n-\log_3H$. If $H$ is polynomial in $n$, then
(8.10)--(8.11) bound the maximum in (8.12) by $C n^{-a}$. Choosing

$$
\delta=n^{-a},\qquad H=\lceil n^{2a+1}\rceil
$$

proves

$$
\mathbb P(\min(X_n,1-X_n)\le n^{-a})\le C_{\alpha,a}n^{-a}.
\tag{8.13}
$$

Finitely small $n$ are absorbed into the constant. For later qualitative
use, (8.12), with $\delta,H$ fixed first, also gives

$$
\limsup_{n\to\infty}\mathbb P(\min(X_n,1-X_n)\le\delta)
\le4\delta,
\tag{8.14}
$$

by letting $H\to\infty$ after $n\to\infty$. This is an estimate on
the actual canonical representative for every fixed geometric parameter.

### 8.3. Completion with a bounded-variation cutoff

Let $M=2^p$, $N=3^n$, $1\le k<M$. Choose $t_0$ nearest $kN/M$,
and put $\gamma=kN/M-t_0\in[-1/2,1/2]$. Exactly,

$$
e(ku_n/M)=e(t_0X_n)e(\gamma X_n).
\tag{8.15}
$$

On $[0,1]$ set
$\chi_\delta(x)=\min(1,x/\delta,(1-x)/\delta)$, and periodically
extend $g_\gamma(x)=\chi_\delta(x)e(\gamma x)$. This is continuous
at the seam because $\chi_\delta(0)=\chi_\delta(1)=0$.
Uniformly for $|\gamma|\le1/2$, its total variation is $O(1)$ and
the total variation of its derivative is $O(1/\delta)$. The latter
includes the derivative jumps at $0,\delta,1-\delta$.

One and two distributional integrations by parts give the Fourier
coefficient bounds

$$
|c_h|\le C\min\left(1,\frac1{|h|},\frac1{\delta h^2}\right)
\quad(h\ne0),\qquad |c_0|\le1.
\tag{8.16}
$$

Their absolute summability justifies uniform Fourier inversion. Hence

$$
\sum_{|h|\le L}|c_h|\le C\log(2+L),\qquad
\left\|g_\gamma-\sum_{|h|\le L}c_he(hx)\right\|_\infty
\le\frac{C}{\delta L}.
\tag{8.17}
$$

Removing the cutoff costs at most the probability in (8.12), since it
equals one on $[\delta,1-\delta]$. The remaining expectation involves
only $\widehat\mu_n(t_0+h)$, $|h|\le L$.

For a fixed $\lambda<\log_2 3$, suppose $p\le\lambda n$, and take
$\delta=n^{-a}$ and $L=\lceil n^{2a+1}\rceil$. The ratio $N/M$
grows exponentially, so $0<t_0+h<N$ for all these frequencies and large
$n$. Define

$$
d=M(t_0+h)-kN=M(h-\gamma).
\tag{8.18}
$$

It is a nonzero integer: $d=0$ would imply $2^p\mid k$, contrary to
$0<k<M$. If $t_0+h=3^{n-r}\xi$ with $3\nmid\xi$, then
$v_3(d)=n-r$, because $v_3(kN)\ge n$. Therefore

$$
\begin{aligned}
r&\ge n-\log_3\bigl(M(L+1/2)\bigr)\\
&\ge\left(1-\frac{\lambda}{\log_2 3}\right)n-O_{a}(\log n).
\end{aligned}
\tag{8.19}
$$

Each remaining coefficient is bounded by $C_{\alpha,a,\lambda}n^{-a}$
using (8.10)--(8.11). Equations (8.13), (8.15), and (8.17) thus give

$$
\sup_{p\le\lambda n}\max_{1\le k<2^p}
|\mathbb E e(ku_n/2^p)|
\le C_{\alpha,a,\lambda} n^{-a}\log n.
\tag{8.20}
$$

For any prescribed exponent strictly below the endpoint in (8.10), apply
(8.20) with a slightly larger admissible exponent to absorb the logarithm.
This proves (8.2)--(8.3).

For (8.1), keep $\delta,L$ fixed and suppose $M\le M_n=o(N)$.
The completed frequencies again lie strictly between zero and $N$, and

$$
r\ge\log_3(N/M_n)-\log_3(L+1/2)\longrightarrow\infty.
$$

Thus (8.10)--(8.11) make the finite completed sum tend to zero uniformly.
Using (8.14) and (8.17), the limit superior of the original bias is at most
$4\delta+C/(\delta L)$. First let $L\to\infty$, then
$\delta\to0$. All limits in $n$ used fixed cutoff and degree.

Finally, if $B_{n,p}$ is the maximum binary character bias, Parseval on
$\mathbb Z/2^p\mathbb Z$ gives

$$
2^p\sum_v\mathbb P(u_n\equiv v\pmod{2^p})^2-1
\le(2^p-1)B_{n,p}^2.
\tag{8.21}
$$

For $p\le c\log_2n$ and $c<2A_\alpha$, choose
$c/2<a<A_\alpha$ in (8.2). The right side tends to zero uniformly.
Total variation is at most one half the square root of the left side.
This proves (8.4), with the corresponding baseline range for other parameters.


## 9. Binary character decay at asymptotically critical division totals

In this section only, put $\alpha=\log_3 2$, $q=1-\alpha$, $\rho=1/\alpha=\log_2 3$,
and $\eta=2\rho$. Let $\nu_{n,D}$ be the law of the actual canonical
endpoint $u_n\in(0,3^n)$ of a uniform positive composition of $D$ into
$n$ exponents. Equivalently, condition the critical iid geometric word
on its total $D_n=D$. The last valuation may truncate. Write
$\widehat\nu_{n,D}(t)=\mathbb E[e(tu_n/3^n)\mid D_n=D]$.

**Theorem 7 (asymptotically critical division totals).** For every fixed $0<\lambda<\rho$ and every prescribed
nonnegative envelope $G(n)=o(n)$,

$$
\sup_{|D-\rho n|\le G(n)}
\sup_{1\le p\le\lambda n}\max_{1\le k<2^p}
\left|\mathbb E[e(ku_n/2^p)\mid D_n=D]\right|
\longrightarrow0.
\tag{9.1}
$$

The first supremum is over admissible integer totals. No effective rate,
growing-resolution total variation or collision-energy estimate is claimed.
This includes every fixed $O(\sqrt n)$ critical window and allows any
prescribed $o(n)$ deviation. The mean-two clock in paper 9/v2 is different.

The deterministic arithmetic input is the complete fixed-triangle
Subspace proof in Appendix A. Its conceptual predecessor is Wren's
bounded-chain sketch [13], with Tao's geometric partition [2] and
Schlickewei's theorem as stated in [14]. We give the required modification
of the observation horizon explicitly below.

### 9.1. Pair kernels before the final short part of the bridge

Let $K=\lfloor n/2\rfloor$, $b_j=e_{2j-1}+e_{2j}$ and
$E_j=\sum_{i\le j}b_i$. Set

$$
H=\lceil2G(n)+n^{3/4}\rceil,\qquad
L_n=\lceil\sqrt{nH}\rceil,\qquad J_n=K-L_n.
\tag{9.2}
$$

Only sufficiently large $n$, for which $J_n>0$, are relevant. A history
before a pair step has $m$ exponents and total $s$ still to be read.
Under the uniform-composition bridge, for $m\ge3$,

$$
\mathbb P(b=b_0\mid m,s)
=\frac{(b_0-1)\binom{s-b_0-1}{m-3}}{\binom{s-1}{m-1}},
\quad 2\le b_0\le s-m+2.
\tag{9.3}
$$

Suppose $63/100\le m/s\le2/3$ and $s\ge150$. Then
$(m-2)/(s-2)\ge5/8$. For a single next exponent,

$$
\mathbb P(e_1>k\mid m,s)
=\frac{\binom{s-k-1}{m-1}}{\binom{s-1}{m-1}}
\le\left(\frac{s-m}{s-1}\right)^k\le(3/8)^k.
\tag{9.4}
$$

Conditional on its value, the next exponent has the same tail bound,
since its success parameter is at least
$(m-2)/(s-e_1-1)\ge(m-2)/(s-2)\ge5/8$.
Sequential quantile coupling therefore dominates the pair by a sum
$B_*$ of two independent positive geometric variables of parameter $5/8$.
In addition, (9.3) gives

$$
\begin{aligned}
\mathbb P(b=3\mid m,s)
&=\frac{2(m-1)(m-2)(s-m)}{(s-1)(s-2)(s-3)}\\
&\ge2(5/8)^2/3=25/96>1/4,\\
\mathbb E[B_*\mathbf1_{B_*>8}]
&=\frac{570807}{10485760}<\frac1{16}.
\end{aligned}
\tag{9.5}
$$

On the strip $|E_j-\eta j|\le H$, and before step $J_n$, the
remaining exponent count is at least $2L_n$. We have $H=o(n)$,
$L_n=o(n)$ and $H/L_n\to0$. Uniformly over the totals in (9.1),

$$
\frac{s}{m}=\rho+O\left(\frac{H+G(n)}{L_n}\right)
=\rho+o(1).
\tag{9.6}
$$

Thus the hypotheses of (9.5) hold eventually at every such history.

Construct an auxiliary pair process which uses the exact bridge kernel
until the strip first fails or step $J_n$ is completed, and then uses
critical iid pairs forever. At every history it has the domination and
mark-probability bounds in (9.5), including after switching. On the event
that the strip does not fail through $J_n$, its law equals the original
bridge law up to that horizon.

For this paragraph use the iid comparison parameter $\alpha_D=n/D$,
so its mean total is exactly $D$. Conditioning still gives the same uniform
composition law. Since $D/n\to\rho$ uniformly, $\alpha_D\to\alpha$.
Write $\pi_j^{(D)}$ for this comparison law's $j$-fold total distribution.
Uniform Stirling bounds give $\pi_n^{(D)}(D)\ge cn^{-1/2}$. The tilted
pair mean is $2D/n$, whose accumulated deviation from $\eta j$ is at most
$G(n)$ before $K$. The strip therefore has a margin at least $n^{3/4}$.
Uniform Chernoff estimates and a union bound give

$$
\mathbb P\left(\max_{j\le J_n}|E_j-\eta j|>H\mid D_n=D\right)
\le C_0n^{3/2}e^{-c\sqrt n}.
\tag{9.7}
$$

Similarly, the probability that some interval of at least $H$ pair
indices contains fewer than one eighth as many marks $b_j=3$ is at most
$C_0n^{5/2}e^{-cH}$. The tilted mark probability is eventually greater
than $1/4$ uniformly. These estimates divide the comparison-law failure
probabilities by $\pi_n^{(D)}(D)$; no conditioned independence is asserted.

### 9.2. All-triangle penalty for this adapted process

Use Tao's full conductor-$n$ black triangles on $[K]\times\mathbb Z$,
with the fixed sufficiently small $\varepsilon\le e^{-140}$ of Appendix A and [2].
Let $W_J$ count white marks and $T_J$ count all distinct triangles
containing marks through $J=J_n$. The triangles themselves are not cut
at $J$; only the counted visits are restricted.

The all-triangle episode argument below uses only uniform conditional
tail domination and a conditional probability at least $1/4$ of the next
increment being three. It does not require independent original pair
steps. Here is the conditional version of its key bound. If $\tau$ is
first exit from a fixed triangle, a lower exit has $b_\tau\le3$.
An exit with $b_\tau>8$ must cross the top. The nonnegative integer
distances to the top strictly decrease before exit, and predictable
conditioning gives

$$
\mathbb P(b_\tau>8\mid\mathcal F_\sigma)
\le\sum_{s\ge0}\mathbb P(B_*>\max(8,s))
=\mathbb E[B_*\mathbf1_{B_*>8}]<1/16,
\tag{9.8}
$$

from any entry time $\sigma$. Conditional on the exit history, the
next increment is three with probability at least $1/4$. A short exit
followed by that increment produces a white mark by triangle separation;
it cannot reenter the old triangle through either the top or the diagonal.
Its two-step distance from the last interior point is less than $13$,
whereas separation is at least $14$.

Start each episode at the first black mark strictly after the preceding
exit-plus-one time. Each episode accounts for at most three distinct
visited triangles, including its two boundary times. If there are more
than $R$ episodes before $J$, all of the first $R$ completion times lie
before a later entry and are distinct. The last episode is left unpaid.
At each backward conditioning step, discard the future-entry indicator
before using the discount bound. Using this conditioning, with

$$
\vartheta=1-\frac{15}{64}(1-e^{-\varepsilon^3})<1,
$$

the auxiliary process satisfies

$$
\widetilde{\mathbb E}
[e^{-\varepsilon^3W_J}\mathbf1_{T_J>3R}]\le\vartheta^R.
\tag{9.9}
$$

Transfer back to the bridge by adding the failure probability (9.7). The
path laws agree on the good-strip event, and the bounded nonnegative
functional is at most one on its complement. No comparison of a local
success probability conditional on many future episodes is used.

### 9.3. Fixed-triangle exclusion with a shortened observation horizon

Suppose $\xi$ is primitive modulo $3^n$ and

$$
2^p\xi\equiv\Delta\pmod{3^n},\qquad
0<|\Delta|\le\exp((\log3-\sigma)n),\qquad v_2(\Delta)<p,
\qquad 1\le p\le Bn,
\tag{9.10}
$$

where $B<\infty$ and $0<\sigma<\log3$ are fixed. Divide out the
binary valuation of $\Delta$ first, as in Appendix A. For each fixed $R$, the
strengthened deterministic exclusion of Appendix A remains valid
when the strip, dense-mark and $W_J\le H$, $T_J\le R$ assumptions are
imposed only through $J_n$ in (9.2). To check this, intersect each integer
core from that proof with $[1,J_n]$, discard cores shorter than $10H$,
and order the rest. Disjointness and the $O_R(H)$ gap bounds are unchanged.
Only the last retained core can be cut at the right endpoint. Its actual
top height satisfies

$$
\ell_L=\rho n+O_R(H+L_n).
\tag{9.11}
$$

The lower bound follows from coverage through $J_n-O_R(H)$; the upper
bound follows from the original triangle's right vertex before $K$ and
its lower boundary being below the strip. All preceding corner identities
are unchanged. In particular, the exact sum from Appendix A remains

$$
\Delta=a_L2^{p+\ell_L-1}
+\sum_{i=2}^L b_i2^{p+\ell_{i-1}-1}3^{m_i}-b_03^{m_1}.
\tag{9.12}
$$

The only changed final-coefficient estimate is
$\log|a_L|=O_R(H+L_n)=o(n)$. All other coefficients except $b_0$
also have logarithmic size $o(n)$; $\log|b_0|\le p\log2+o(n)$.
Keep $-b_03^{m_1}$ separate when $p/n$ has a positive limit. It is odd,
and all other terms have binary valuation at least $p$. The fixed-place
product in the strengthened proof of Appendix A omits that coordinate at infinity,
giving $|\Delta|3^{-m_1}$ times only the subexponential coefficients.
Since $m_1=n-o(n)$, it has the fixed exponential saving $e^{-\sigma n+o(n)}$.
If $p/n\to0$, the original grouping applies. Thus both cases give the
same Subspace contradiction. No effective threshold is asserted.

Using (9.7) and the dense-mark bound, for every fixed $R$ we obtain

$$
\mathbb E[e^{-\varepsilon^3W_J}\mathbf1_{T_J\le R}\mid D_n=D]
\le C_Rn^{5/2}e^{-c\sqrt n}
\tag{9.13}
$$

eventually, uniformly over the prescribed asymptotically critical totals and frequencies
in (9.10). Combining (9.9), (9.13), and (9.7), first let $n\to\infty$ with
$R$ fixed, then $R\to\infty$. This proves uniform decay of the full
restricted marked-point majorant under exact critical conditioning.

Given pair totals and the last singleton, pair splits are still
independent and uniform under a fixed-total composition. Reversal also
preserves this conditioned law. Thus Tao's phase bound applies to
$\widehat\nu_{n,D}(\xi)$, with the full white count at least $W_J$:

$$
\sup_{D,p,\xi\ \mathrm{as\ above}}
|\widehat\nu_{n,D}(\xi)|\longrightarrow0.
\tag{9.14}
$$

### 9.4. Boundary mass with the total retained

Put $X_n=u_n/3^n$, $\rho_*=15/16$, and
$\kappa_*=-\log\rho_* /(4\log2)>0$. Uniformly over the totals in (9.1),
for all sufficiently large $n$,

$$
\mathbb P(\min(X_n,1-X_n)\le\delta\mid D_n=D)
\le C_0(\delta^{\kappa_*}+2^{-\kappa_*n}).
\tag{9.15}
$$

The canonical carry argument in Lemma A.2 is deterministic. For
$2^{-n}\le\delta\le1/16$ and $m=\lfloor\log_2(1/\delta)/4\rfloor$,
if the last $m$ exponents have total $S\le2m$, proximity to either end
forces respectively all carries or all complementary carries to vanish.
In the upper case the accumulated positive backward error is bounded by
$\sqrt\delta+\tfrac12 2^{2m}3^{-(n-m)}<1$.

For a fixed positive integer state at the start of that block and a fixed
block total $s$, there is at most one word realizing each zero-carry
orientation. Its first $m-1$ exponents must be the exact valuations of
the successively determined odd intermediate states; the last exponent
is then determined by $s$ and may truncate. This count remains valid
although the prefix-state law depends on $s$.

Use again $\alpha_D=n/D$, $q_D=1-\alpha_D$ and $\pi_j^{(D)}$.
Eventually $5/8\le\alpha_D\le2/3$. Since $m\le n/4$, uniform local
maxima and the centered denominator give

$$
\frac{\pi_{n-m}^{(D)}(D-s)}{\pi_n^{(D)}(D)}\le C_0
\quad\hbox{for every integer }s.
\tag{9.16}
$$

Each final word of length $m$ and total $s$ has iid weight
$\alpha_D^mq_D^{s-m}$. Sum over prefix states conditional on their total,
using the at-most-one-word count separately for each $s$. The conditional
probability of zero carries and $S\le2m$ is therefore at most

$$
C_0\sum_{s=m}^{2m}\alpha_D^mq_D^{s-m}\le C_0\alpha_D^{m-1}
\tag{9.17}
$$

for each orientation. There is no binomial word-count factor in (9.17).
For the excluded clock, (9.16) and the iid Chernoff bound give

$$
\mathbb P(S>2m\mid D_n=D)
\le C_0\mathbb P_{\alpha_D}(S>2m)\le C_0(4\alpha_Dq_D)^m.
$$

Both $\alpha_D\le2/3<\rho_*$ and $4\alpha_Dq_D\le15/16=\rho_*$,
so this proves (9.15) in the indicated range. Small
$\delta$ follow by monotonicity at $2^{-n}$; the remaining cases are
absorbed into the constant. This counting proof does not impose iid
independence after the total is fixed.

### 9.5. Conductor reduction is a mixture of critical clocks

The unconditional projective identity cannot be substituted for the
conditioned law. For $r<n$, the correct identity is

$$
\widehat\nu_{n,D}(3^{n-r}\xi)
=\sum_s\frac{\binom{s-1}{r-1}\binom{D-s-1}{n-r-1}}
{\binom{D-1}{n-1}}\widehat\nu_{r,s}(\xi),
\tag{9.18}
$$

with invalid compositions omitted. It follows either by exchangeability
or by the pathwise fact that reduction modulo $3^r$ depends only on the
last $r$ exponents. The case $r=n$ is immediate.

Fix $c_1>0$ and suppose $r\ge c_1n$. With $h=n-r$, the removed
block total $T$ has conditional marginal at most $C_{c_1}\pi_h^{(D)}(t)$,
by the same local-maximum argument as (9.16). Its comparison mean is
$hD/n$ and its variance is $O(h)$ uniformly. Consequently

$$
\mathbb P(|T-hD/n|>n^{3/4}\mid D_n=D)
\le C_{c_1}n^{-1/2}=o(1).
\tag{9.19}
$$

On the complement, the retained total $s=D-T$ satisfies
$|s-\rho r|\le rG(n)/n+n^{3/4}=o(r)$ uniformly. More explicitly,
for $r\le n\le r/c_1$ these deviations are bounded by the envelope
$\widetilde G(r)=\sup_{r\le m\le r/c_1}(rG(m)/m+m^{3/4})=o(r)$.
The uniform restricted estimate (9.14) therefore applies to the retained
clocks. This argument permits a removed block of linear size; it does not
mistake an $O(h/n)$ bound for a vanishing error.

### 9.6. Finite binary completion

Let $M=2^p$, $N=3^n$, and let $t_0$ be nearest $kN/M$ for
$0<k<M$. Write $\gamma=kN/M-t_0\in[-1/2,1/2]$. Then
$e(ku_n/M)=e(t_0X_n)e(\gamma X_n)$ exactly.

For a fixed seam width $\delta>0$, cut off near the ends of $[0,1]$.
The functions $\chi_\delta(x)e(\gamma x)$ have a common Lipschitz
bound on the circle. A single fixed-degree Fejer polynomial approximates
all of them to any fixed uniform error $\tau>0$, with coefficients of
modulus at most one. The cutoff costs at most the probability in (9.15).

Only finitely many frequencies $t=t_0+j$, $|j|\le L$, remain. Uniformly
for $p\le\lambda n$, $\lambda<\rho$, they lie strictly between zero
and $N$. Their
differences $d=Mt-kN$ are nonzero, with
$|d|\le M(L+1/2)$ and $v_2(d)=v_2(k)<p$. If $t=3^{n-r}\xi$ is
primitive at conductor $r$, then $v_3(d)=n-r$. Write $h=n-r$ and
$\Delta=d/3^h$. Then

$$
\begin{aligned}
r&\ge n-p\log_3 2-O_L(1)\ge c_1n,\\
\log|\Delta|&\le p\log2-h\log3+O_L(1)\\
&=r\log3-(n\log3-p\log2)+O_L(1)
 \le r(\log3-\sigma),\\
2^p\xi&\equiv\Delta\pmod{3^r},\qquad
v_2(\Delta)<p,\qquad p\le(\lambda/c_1)r,
\end{aligned}
\tag{9.20}
$$

eventually, with the fixed choices
$c_1=(1-\lambda/\rho)/2>0$ and
$\sigma=(\log3-\lambda\log2)/2>0$. The nonzero difference has
$v_2(\Delta)=v_2(k)<p$; dividing out that power of two preserves all
the required upper bounds. Thus (9.10) holds at every completed conductor.

Use (9.18)--(9.19), then the uniform restricted estimate (9.14), to make each
of these finitely many conditioned coefficients tend to zero. The limit
superior of the binary bias is at most $C_0\delta^{\kappa_*}+\tau$.
Let $\tau\to0$ and then $\delta\to0$. The cutoff and degree were
fixed before every limit in $n$. This proves (9.1).

Leen [3, Section 8] obtains super-polynomial conditional decay when
the mean division total stays strictly above $\rho$. The window in
Theorem 7 approaches $\rho$ from either side through any prescribed $o(n)$
window, and uses a qualitative argument at fixed linear bit precision.
The known $c/n$ lower bound for the critical positive majorant
is compatible with (9.14); no arbitrary-polynomial decay is asserted.

Mahler [15] studies conditional source-given-endpoint energies and
exact carry encodings for this prescribed-division ensemble; those
quantities are different from the endpoint character in (9.1). The
real-localization theorem [16] controls bounded-real weighted densities
at the mean-two central clock. The present clock has critical mean
$\log_2 3$, and its proof does not use that regularity theorem.


## 10. Weighted rational resonances and macroscopic triangle cores

Individual character bounds do not directly control the sum of squared
biases at linear precision. We give a partial estimate for the actual
weighted spectrum of a joint source/endpoint projection. The exact word
encoding is due to Rees [1]; related fixed-total coset-Dirichlet projections
appear in Mahler [15]. The arithmetic estimate below is an application of
Schlickewei's theorem [14]. Its triangle consequence uses Tao's geometry
[2] and does not assume the strict drift of Tao's original renewal process.

For a chronological word of length $s$, total $S$, and partial totals
$E_i=e_1+\cdots+e_i$, put

$$
B_w=\sum_{i=1}^s3^{s-i}2^{E_{i-1}},\qquad
2^S u_s=3^s n_s+B_w.
\tag{10.F1}
$$

Here $n_s\in[0,2^S)$ is the actual canonical source and $0<u_s<3^s$.
Let $L=3^s$, $N=3^h$, $Q=LN$, $M=2^p$, and let $\nu_S$ be the
conditional law of $Y=[2^{-S}B_w]_Q$. Then $u_s=[Y]_L$ and
$X=2^{-S}n_s\bmod N=-\lfloor Y/L\rfloor\bmod N$. The deeper
precision has only $s$ letters; it is not a stationary replacement.
Writing $e(x)=e^{2\pi ix}$, $D_L(x)=L^{-1}\sum_{u<L}e(ux)$ and
$\widehat\nu_S(t)=\mathbb E[e(tY/Q)\mid S]$, exact Fourier inversion gives

$$
\Phi_S(a,b)=\mathbb E[e(aX/N+bu_s/M)\mid S]
=\sum_{\substack{0\le t<Q\\t\equiv-a\pmod N}}
D_L(b/M-t/Q)\widehat\nu_S(t).
\tag{10.F2}
$$

Indeed, write $Y=Lk+u$ in the normalized Fourier expansion of
$e(-a\lfloor Y/L\rfloor/N+b[Y]_L/M)$. The sum over $k$ selects the
indicated congruence class, and the sum over $u$ gives $D_L$.
For fixed $a,b$, its arguments form a translated $1/L$ grid. The bound
$|D_L(x)|\le\min(1,(2L\|x\|)^{-1})$ and a harmonic sum give
an absolute coefficient sum at most $A_L=4+2\log L$.
Thus, with $W(t)=\sum_{b<M}|D_L(b/M-t/Q)|$,

$$
\sum_S\pi_s(S)\sum_{a=1}^{N-1}\sum_{b=0}^{M-1}|\Phi_S(a,b)|^2
\le A_L\mathcal K_s,\qquad
\mathcal K_s=\sum_S\pi_s(S)\sum_{N\nmid t}
W(t)|\widehat\nu_S(t)|^2.
\tag{10.F3}
$$

Only source-zero frequencies are excluded. The same weighted
Cauchy--Schwarz estimate applies to any vector of complex frequency
pieces in (10.F2). Theorem 8 controls one frequency family in (10.F3).
Theorem 9 controls an actual phase piece selected by the pair path.
Neither theorem estimates the complete $\mathcal K_s$.

### 10.1. Weighted neighborhoods of all smooth denominators

Put $\alpha=\log_3 2$, $\rho=\log_2 3$, $L=3^s$, $N=3^h$,
$Q=LN$, $M=2^p$, $W(t)=\sum_{b<M}|D_L(b/M-t/Q)|$ and the critical
total law $\pi_s$. Define the positive rate

$$
F(\gamma)=
\begin{cases}
\log((1+\alpha)/\alpha)-\gamma\log2,&0\le\gamma\le 2/(1+\alpha),\\
I(\gamma),&2/(1+\alpha)\le\gamma<\rho,
\end{cases}
$$

where $I(x)=-\log\alpha-(x-1)\log(1-\alpha)-x\log x+(x-1)\log(x-1)$.
Let $A\ge1$ be a real width factor, possibly depending on $s$. For
integers $r,k\ge0$ put $d=2^r3^k$ and

$$
\mathcal A_{S;r,k}(A)=
\left\{0\le t<Q:N\nmid t,\
 \operatorname{dist}\left(\frac{[2^{-S}t]_Q}{Q},
 \frac1d\mathbb Z\right)<\frac A L\right\}.
\tag{10.1}
$$

Distances are on the real circle. Fix $0\le\gamma<\rho$ and take the union

$$
\mathcal U_{S,\gamma}(A)
=\bigcup_{\substack{r,k\ge0\\2^r3^kA\le2^{\gamma s}}}
\mathcal A_{S;r,k}(A).
\tag{10.2}
$$

The union has at most $O_\gamma(s^2)$ denominator pairs.

**Theorem 8 (weighted rational phase neighborhoods).** For every fixed $B_0<\infty$, $\gamma<\rho$ and
$\varepsilon>0$, eventually and uniformly over $A\ge1$ and
$1\le h,p\le B_0s$,

$$
\sum_S\pi_s(S)\sum_{t\in\mathcal U_{S,\gamma}(A)}W(t)
\le C s^3MN e^{-(F(\gamma)-\varepsilon)s}.
\tag{10.3}
$$

This estimate uses no word Fourier coefficient. The same bound holds
with any multipliers in $[0,1]$ inside the sum. Empty unions cost zero.

*Proof.* Fix one pair $r,k$ with $dA\le2^{\gamma s}$. In particular
$k<s$ for large $s$, and $Q_k=Q/3^k$ is an integer divisible by $N$.
Write $j=[2^{-S}t]_Q$. The centered representative $\ell$ of $2^rj$
modulo $Q_k$ obeys

$$
|\ell|<2^rNA,\qquad N\nmid\ell.
\tag{10.4}
$$

These conditions are equivalent to (10.1). There are $3^k$ lifts to
$t$ for every allowed $\ell$; no independence of the lifts is asserted.
The inequality $dA/L<1/2$ eventually ensures that the centered range
has no ambiguity.

Retain totals $s\le S\le6s$ with $S\ge(\gamma+\delta)s$, where
$\delta>0$ is fixed and $\gamma+\delta<\rho$. Then $S\ge r$ and
$t\equiv2^{S-r}\ell\pmod{Q_k}$. For each selected $t$ and $b<M$, let
$z_{t,b}$ be the centered residue of $Mt-bQ$ modulo $MQ$. Thus

$$
z_{t,b}=2^{S-r+p}\ell-Q_kc_{t,b},\qquad
|c_{t,b}|\le M3^k(A2^S/L+1/2).
\tag{10.5}
$$

In the two-variable Subspace proof take $X_1=2^{S-r+p}\ell$,
$X_2=Q_kc$. At infinity take the forms $X_1-X_2,X_2$; at each of the places
$2$ and $3$ take the coordinate forms. They are fixed and independent, and give

$$
\prod_v\prod_i|L_{i,v}(X)|_v
\le C|X_1-X_2|\,dA(2^{-S}+L^{-1}).
\tag{10.6}
$$

The coordinate heights have logarithm $O(s)$ uniformly, including when
$A$ varies, since $A\le2^{\gamma s}$. The valuation gap is at least

$$
\min(S,\rho s)-\log_2(dA)-O(1)
\ge\min(\delta,\rho-\gamma)s-O(1).
\tag{10.7}
$$

If the proposed separation failed along an unbounded sequence, (10.6)
would be at most $Ce^{-\eta s}$ while the coordinate heights have
logarithm $O(s)$. Thus [14, Theorem 2.3] would put the vectors in finitely
many rational lines. A fixed line with both coordinates nonzero forces
a fixed binary valuation difference, contradicting (10.7). This proves
the uniform separation

$$
|z|\ge\frac{\min(2^S,L)}{dA}e^{-\eta s}
\tag{10.8}
$$

for individual nonzero values and nonzero pairwise differences, for
every fixed $\eta>0$ and all sufficiently large $s$. The coordinate
coefficients in (10.5) may be enlarged by a fixed factor for differences.
If the difference in $\ell$ is zero, a nonzero $z$ is a multiple of
$Q_k$, and (10.8) follows directly since $Q_k\ge L/(dA)$.
If $c=0$, the power $2^{S-r}$ suffices. The source-zero exclusion
removes $\ell=0$ for individual values; it is essential here.

Distinct pairs $(t,b)$ still have distinct centered values $z_{t,b}$,
by $\gcd(M,Q)=1$, even when their reduced $\ell$ is the same.
The at most $C dAMN$ values therefore yield a harmonic sum using separation (10.8):

$$
\sum_{t\in\mathcal A_{S;r,k}(A)}W(t)
\le C sMN\,dA e^{\eta s}(2^{-S}+3^{-s})
\le C sMN\,2^{\gamma s}e^{\eta s}(2^{-S}+3^{-s}).
\tag{10.9}
$$

For omitted clocks use the full-grid bound $\sum_tW(t)\le CsMN$.
Indeed, for fixed $b$ the translated $1/Q$ grid has at most $2N+2$
points in each distance shell of width $1/L$. The inner shell costs
$O(N)$; shell number $j\ge1$ costs $O(N/j)$ by the geometric-series
bound. Sum through $L/2$ and then over $b<M$.
Appendix B applies with the combined height budget $\gamma$. It gives
$CsMN e^{-(F(\gamma)-\varepsilon)s}$ for each denominator pair.
Sum over the $O(s^2)$ pairs. This proves (10.3). All arithmetic thresholds
remain ineffective. $\square$

### 10.2. A long triangle forces one of these rational approximations

We state the exact deterministic connection before using probabilities.
Let $t$ be a non-source-zero frequency and put

$$
v=v_3(t)<h,\qquad n=s+h-v>s,\qquad \xi=t/3^v.
$$

Reverse the length-$s$ exponent word for the phase calculation, so

$$
Y\equiv\sum_{i=1}^s3^{i-1}2^{-(e_1+\cdots+e_i)}\pmod Q.
\tag{10.10}
$$

This reversal preserves the fixed-total law. Set $K=\lfloor s/2\rfloor$,
$b_j=e_{2j-1}+e_{2j}$, $E_j=\sum_{i\le j}b_i$ and $\eta=2\rho$.
Use Tao's conductor-$n$ black-triangle partition [2, Lemma 7.4] for the phases

$$
\theta(j,\ell)=
\left\{\frac{\xi3^{2j-2}2^{1-\ell}}{3^n}\right\},
\qquad 1\le j\le K,
\tag{10.11}
$$

where the braces are centered residues and powers of two are inverted
modulo $3^n$. The full partition extends through $\lfloor n/2\rfloor$;
only visits through $K$ are relevant here. Fix its allowed black cutoff
$0<\epsilon_0<1/100$.

For a black triangle with top-left corner $(j_0,\ell_0)$ and corner
phase $a/3^m$, The corner formulas in Appendix A.1 give

$$
m=n-2j_0+2,\qquad
a2^{\ell_0-1}\equiv\xi\pmod{3^m},
\tag{10.12}
$$

and its lower boundary is $\ell\ge\eta j+c$, where

$$
c=\ell_0-(n+2)\rho+\log_2(|a|/\epsilon_0).
\tag{10.13}
$$

For a real $H\ge1$, define its integer core inside the observed horizon by

$$
J_\Delta=
\left[j_0,\left\lfloor\frac{\ell_0-H-1}{\eta}\right\rfloor\right]
\cap[1,K].
\tag{10.14}
$$

Suppose the actual pair path satisfies

$$
|S-\rho s|\le H,\qquad |E_j-\eta j|\le H\quad(1\le j\le K),
\tag{10.15}
$$

and visits this triangle at some observed point. Visitation and the
lower boundary imply $c\le H$, hence

$$
3^v|a|2^{\ell_0}\le 9\epsilon_0 Q2^H.
\tag{10.16}
$$

**Lemma 10.1.** If $|J_\Delta|\ge\kappa s$ for a fixed
$0<\kappa<1/2$, then $t$ belongs to an arc in (10.1) with

$$
A=2^{2H},\qquad 2^r3^k\le2^{\rho(1-2\kappa)s}.
\tag{10.17}
$$

*Proof.* Set

$$
k=2j_0-2,\qquad r=(S-\ell_0+1)_+.
$$

The nonempty core forces $\ell_0>1$, so all powers in (10.12) are integral.
Multiplying (10.12) by $3^v$ and dividing by the unit $2^S$ modulo
$Q_k=Q/3^k$ gives, for $j=[2^{-S}t]_Q$,

$$
2^rj\equiv
3^v a\,2^{(\ell_0-1-S)_+}\pmod{Q_k}.
\tag{10.18}
$$

Thus the distance of $j/Q$ from a rational with denominator $2^r3^k$
is at most

$$
\frac{3^v|a|2^{\ell_0-1-S}}{Q}
\le\frac{9\epsilon_0}{2}\,2^{H-S}
<\frac{2^{2H}}{L}.
\tag{10.19}
$$

The last inequality uses $S\ge\rho s-H$ and $9\epsilon_0/2<1$.
A large residue on the right of (10.18) causes no problem: choosing its
integer lift still gives the displayed upper bound on circle distance.

The core length implies

$$
\ell_0\ge\eta(j_0+\kappa s-1)+H+1.
\tag{10.20}
$$

If $\ell_0\le S+1$, then
$r+\rho k=S-\ell_0+1+\rho(2j_0-2)
\le S-2\rho\kappa s-H\le\rho(1-2\kappa)s$.
Otherwise $r=0$, and the core's containment in $[1,K]$ gives
$j_0\le K-\kappa s+1$, hence $\rho k\le\rho(1-2\kappa)s$ again.
Equations (10.18)--(10.20) prove the claim. $\square$

### 10.3. Exponential removal of all paths with a macroscopic core

Fix $0<\kappa<1/2$. Put

$$
H=\left\lceil\frac{\rho\kappa}{4}s\right\rceil,\qquad
\gamma=\rho(1-\kappa)<\rho,\qquad A=2^{2H}.
\tag{10.21}
$$

For large $s$, (10.17) implies $2^r3^kA\le2^{\gamma s}$.
Under the critical iid geometric law, the failure probability of (10.15)
satisfies

$$
\Pr(\text{failure of (15)})\le Cs e^{-c_\kappa s}
\tag{10.22}
$$

for some $c_\kappa>0$. Indeed the centered exponents have an exponential
moment near zero; choose a fixed sufficiently small Chernoff parameter
depending on $\kappa$, then sum the bounds for the $O(s)$ partial sums.
This includes the total $S$ and the possible last singleton.

For each frequency $t$, let $\mathcal L_t$ be the event that the observed
pair path visits any black triangle whose core (10.14) has at least
$\kappa s$ indices. The number of other visited triangles is unrestricted.
Let $W_t^{\rm white}$ count marked white points, a mark meaning $b_j=3$.
Then define the actual clock-averaged majorant contribution

$$
\mathcal B_s=
\sum_S\pi_s(S)\sum_{N\nmid t}W(t)\,
\mathbb E\left[
 e^{-\epsilon_0^3W_t^{\rm white}}\mathbf1_{\mathcal L_t}
 \,\middle|\,S\right].
\tag{10.23}
$$

**Theorem 9 (macroscopic triangle cores).** For every fixed $B_0<\infty$ and
$0<\kappa<1/2$, there is $c>0$ such that, eventually and uniformly over
$1\le h,p\le B_0s$,

$$
\mathcal B_s\le C s^3MN e^{-cs}.
\tag{10.24}
$$

In particular the removed contribution is exponentially small whenever
$h\log3+p\log2\le(c-\delta)s$ for a fixed $\delta>0$.

*Proof.* On (10.15), Lemma 10.1 places the frequency in
$\mathcal U_{S,\gamma}(A)$, regardless of which triangle or path
produced it. Dropping the majorant and event indicators there costs
at most (10.3), say with $\varepsilon=F(\gamma)/2$.
On failure of (10.15), use the full-grid estimate $CsMN$ before averaging
the actual word law. Equation (10.22) gives cost
$Cs^2MN e^{-c_\kappa s}$. Take any
$c\le\min(F(\gamma)/2,c_\kappa)$ and combine the two bounds. $\square$

This also removes an actual complex Fourier contribution, not just an
abstract event. Conditional on pair totals and the last singleton,
the internal pair splits are independent uniform compositions even
after fixing $S$. Let $P_t$ be the actual conditional phase mean in
(10.10). Tao's pair bound gives
$|P_t|\le e^{-\epsilon_0^3W_t^{\rm white}}$.
The event $\mathcal L_t$ depends only on those pair totals, so the
actual piece

$$
F_{S,\mathcal L}(t)=\mathbb E[P_t\mathbf1_{\mathcal L_t}\mid S]
$$

satisfies $|F_{S,\mathcal L}(t)|^2
\le\mathbb E[e^{-\epsilon_0^3W_t^{\rm white}}
\mathbf1_{\mathcal L_t}\mid S]$. Therefore (10.24) bounds its weighted
squared norm. Applying the exact alias filter and its $O(s)$
absolute-coefficient bound introduces only a further polynomial factor.
The cutoff depends on frequency; no new probability law for the
collection of these pieces is asserted.

### 10.4. What remains

All visits to triangles with a fixed macroscopic core can be removed
at exponential cost in the stated positive linear precision region,
even when the path visits arbitrarily many additional triangles.
The complementary piece, in which every visited core is shorter than
$\kappa s$, remains uncontrolled at the required resolution.

The result does not justify making $\kappa$ tend to zero with $s$:
the arithmetic thresholds are ineffective and the decay rate shrinks.
A fixed episode-count penalty still cannot pay exponentially many
weighted frequencies. No complete bound on $\mathcal K_s$, improved
compression, or smaller legal source has been proved. No new numerical
experiment or old checker rerun was used.


## 11. Binary entropy at the critical source threshold

### 11.1. Statement and relation to earlier work

Put $\alpha=\log_3 2$, $\rho=1/\alpha=\log_2 3$, and
$\theta=H_2(\alpha)=0.949955527188\ldots$, with binary entropy $H_2$.
Let $e_1,\ldots,e_s$ be independent positive geometric variables with
$\mathbb P(e_i=t)=\alpha(1-\alpha)^{t-1}$. Define

$$
S_i=\sum_{j=i}^s e_j,\qquad
W_s=\sum_{i=1}^s3^{s-i}[2^{-S_i}]_{3^i},\qquad
u_s=[W_s]_{3^s}.
\tag{E1}
$$

Here brackets select the least nonnegative residue and inverse powers of
two are taken in the indicated odd modulus. These are exactly the raw
digit-sum law of Rees [1] and its canonical endpoint, with fixed initial
multiplicative residue one; they are not a freely randomized multiplier
or an independently chosen residue model. The finite-word parity encoding
in [1] gives $0<u_s<3^s$ and
$u_s=W_s-3^s\lfloor W_s/3^s\rfloor$; also $0<W_s<s3^s$ directly from (E1).

For a probability measure $\mu$ on a finite set write

$$
H_1(\mu)=-\sum_x\mu(x)\log_2\mu(x),\qquad
H_\beta(\mu)=-\frac{1}{\beta-1}\log_2\sum_x\mu(x)^\beta
\quad(\beta>1).
\tag{E2}
$$

**Theorem 10.** Fix $0<c_0<\lambda<\rho$. For either $V_s=W_s$ or $V_s=u_s$,

$$
\liminf_{s\to\infty}\ \min_{c_0s\le p\le\lambda s}
\frac{H_1(V_s\bmod2^p)}p\ \ge\theta,
\tag{E3}
$$

where the minimum is over integers $p$. More precisely, for every
$0<d<\theta$ there are $c>0$ and an ineffective $s_0$ such that, uniformly
for $s\ge s_0$ and the indicated $p$, the actual law has a subprobability
measure $\nu_{s,p}$ satisfying

$$
\nu_{s,p}\le\mathcal L(V_s\bmod2^p),\qquad
\|\nu_{s,p}\|_1\ge1-e^{-cs},\qquad
\|\nu_{s,p}\|_\infty\le2^{-dp}.
\tag{E4}
$$

Consequently there exist a fixed $\beta>1$ and $C<\infty$, depending on
$d,c_0,\lambda$, such that on the same band

$$
H_\beta(V_s\bmod2^p)\ge dp-C.
\tag{E5}
$$

All three conclusions also hold for the conditional law given the whole
word total $S_1=L$, uniformly over every prescribed window
$|L-\rho s|\le G(s)$ with $G(s)=o(s)$. This law is uniform on positive
compositions of $L$ into $s$ parts. Constants are uniform in the window;
the eventual threshold may depend on $G$.

The arithmetic ingredient is the two-dimensional fixed-place Subspace
Theorem of Schlickewei, in the integral formulation stated by Bilu
[14, Theorem 2.3]. Its application here separates actual output collisions
arising from short terminal words. The entropy conversion then uses only
geometric concentration and uniform composition counts. This differs
from obtaining bounds on individual Fourier coefficients: (E4) controls
the whole distribution simultaneously, at positive linear precision.
It does not establish a dimension strictly above $\theta$, which is the
arithmetic input still missing from the optimized compression consumer.

The value $\theta$ also occurs in the entropy dimension of the tilted
ternary Syracuse measure: Leen [17, Section 6] proves the entropy-over-
contraction formula for that projective ternary law. His decoding lemma
[17, Section 3.2] is another direct precedent for the elementary uniqueness
of the numerator used below. That result concerns reduction modulo
$3^n$. The new step here is the simultaneous separation of actual
collisions modulo $2^p$, including canonical carries, followed by the
exponentially small exceptional-mass estimate. We do not infer binary
regularity from the previously known ternary entropy formula.

### 11.2. A fixed-place separation lemma

**Lemma 11.1.** Fix $c_0,\lambda,C,\delta>0$ with
$c_0<\lambda<\rho$. For all sufficiently large $s$, uniformly for
$c_0s\le p\le\lambda s$ and integers $0\le T\le Cs$, there are no
integers $a,b,D$ satisfying

$$
D=2^{T+p}a-3^s b,\qquad
|a|\le\frac{2s3^s}{2^p},\qquad
|b|\le 4s2^T,\qquad
0<|D|\le2^p e^{-\delta s}.
\tag{E6}
$$

**Proof.** Suppose a contrary sequence exists with $s\to\infty$.
If $a=0$, then the nonzero integer $D$ is divisible by $3^s$, whereas
$|D|<2^p<3^s$. If $b=0$, then $|D|\ge2^{T+p}\ge2^p$.
Both are impossible. Put $X_1=2^{T+p}a$, $X_2=3^s b$.

At the infinite place use the independent forms $X_1-X_2,X_1$;
at each of the places two and three use the coordinate forms $X_1,X_2$.
All forms are fixed, independently of the sequence. Their product is at
most

$$
\begin{aligned}
&|X_1-X_2|\,|X_1|\,|X_1X_2|_2\,|X_1X_2|_3\\
&\hspace{1cm}\le |D|\,2^{T+p}|a|\,2^{-(T+p)}3^{-s}
\le 2s\,\frac{|D|}{2^p}
\le2s e^{-\delta s}.
\end{aligned}
\tag{E7}
$$

Also $\|(X_1,X_2)\|_\infty\le4s3^s2^T\le e^{Ks}$ for a fixed $K$.
Thus for all large $s$ the product in (E7) is at most
$\|(X_1,X_2)\|_\infty^{-\delta/(2K)}$.
The integral Subspace Theorem [14, Theorem 2.3] places all these vectors
in finitely many rational lines. No primitiveness assumption is required
by that formulation. On the other hand,

$$
v_2(X_1)-v_2(X_2)
\ge T+p-\log_2|b|
\ge p-\log_2(4s)\longrightarrow\infty.
\tag{E8}
$$

On a fixed rational line with both coordinates nonzero their ratio,
and hence this valuation difference, is fixed. Finitely many lines
cannot contain the sequence, a contradiction. The contradiction also
proves the stated uniformity in all the integer parameters. The eventual
threshold supplied by this argument is ineffective. $\square$

### 11.3. Terminal-word coding and simultaneous injectivity

Choose a small fixed $0<\varepsilon<1/2$, and put

$$
\ell=\left\lfloor\frac{(1-\varepsilon)p}{\rho}\right\rfloor,
\qquad k=s-\ell,\qquad H=\frac{\varepsilon p}{4}.
\tag{E9}
$$

For all large $s$ this is a nonempty proper terminal block. Fix the entire
prefix $e_1,\ldots,e_k$, and fix the tail total
$T=e_{k+1}+\cdots+e_s$. Denote the tail word by
$w=(t_1,\ldots,t_\ell)$, its partial sums by
$E_j=t_1+\cdots+t_j$, $E_0=0$, and its suffix sums by
$T_j=T-E_{j-1}$. The raw prefix contribution is constant when the prefix
and $T$ are fixed. The remaining contribution is

$$
R(w)=\sum_{j=1}^{\ell}3^{\ell-j}[2^{-T_j}]_{3^{k+j}}.
\tag{E10}
$$

Multiplication by $2^T$ gives the exact integer identity

$$
2^TR(w)=B(w)+3^s A(w),\qquad
B(w)=\sum_{j=1}^{\ell}3^{\ell-j}2^{E_{j-1}},
\qquad 0\le A(w)<\ell2^T.
\tag{E11}
$$

To check the integer bounds, for each $j$ the difference between
$2^T[2^{-T_j}]_{3^{k+j}}$ and $2^{E_{j-1}}$ is a nonnegative multiple
of $3^{k+j}$ smaller than $2^T3^{k+j}$. Each summand of $R$ is between
zero and $3^s$, so also $0<R<\ell3^s$.

Distinct positive compositions of the same $T$ have distinct $B$ values.
Indeed, if two words differ, some partial sums $E_j$ with $j<\ell$
differ. At the first such index, the smaller exponent contributes the
unique term of smallest binary valuation to the difference $B(w)-B(w')$.
Its coefficient is odd, so the difference is nonzero. This is the same
elementary parity-coding mechanism as in [1].

Call a word good when

$$
|E_j-\rho j|\le H\qquad(0\le j\le\ell).
\tag{E12}
$$

On this event,

$$
0<B(w)\le\ell3^{\ell-1}2^H
\le 2^p 2^{-\varepsilon p/2}
\tag{E13}
$$

for all large $s$, uniformly in the precision band. In fact the logarithm
of the middle expression is at most
$(1-3\varepsilon/4)p+\log_2\ell-\rho$; its logarithmic term is at most
$\varepsilon p/4$ eventually. Also $T\le\rho\ell+H=O(s)$.

Consider two different good tail words with the same $T$ and prefix.
Their raw outputs differ by $R(w)-R(w')$. If they collide modulo $2^p$,
write that difference as $2^p a$ and subtract (E11). This gives (E6)
with $b=A(w)-A(w')$, $|a|<\ell3^s/2^p$ and $|b|<\ell2^T$.
The nonzero difference $D=B(w)-B(w')$ satisfies the last bound in (E6)
with $\delta=\varepsilon c_0\log2/2$. The lemma excludes the collision.

For canonical outputs, write
$J(w)=\lfloor W_s(w)/3^s\rfloor\in\{0,\ldots,s-1\}$.
Subtraction gives

$$
2^T(u_s(w)-u_s(w'))
=D+3^s\bigl(A(w)-A(w')-2^T(J(w)-J(w'))\bigr).
\tag{E14}
$$

If these outputs collide modulo $2^p$, use their difference $2^p a$ in
(E14). Here $|a|<3^s/2^p$ and the coefficient in parentheses has
absolute value less than $2s2^T$, within (E6). The same lemma excludes
this collision. Thus both actual raw and canonical outputs are injective
modulo $2^p$ on the entire good family at each fixed prefix and total.
No uniform estimate on the earlier prefix clock was used.

### 11.4. Probability and composition counts

The centered geometric variable has an exponential moment near zero.
There exist fixed $t_0,C_1>0$ such that
$\log\mathbb E\exp(\pm t(e_i-\rho))\le C_1t^2$ for
$0\le t\le t_0$. For every $j\le\ell\le s$, exponential Markov gives

$$
\mathbb P(|E_j-\rho j|>H)
\le2\exp(-tH+C_1t^2s).
\tag{E15}
$$

Since $H\ge\varepsilon c_0s/4$, a small fixed positive $t$ makes the
exponent at most $-c_1s$. A union bound over $j$ then gives, after
increasing the threshold and reducing the constant,

$$
\mathbb P(w\text{ is not good})\le e^{-cs}.
\tag{E16}
$$

This is a statement under the original independent geometric law. No
rare fixed-total event is divided out.

Conditionally on $T$, every positive composition of $T$ into $\ell$
parts has the same probability, and their number is
$K(T,\ell)=\binom{T-1}{\ell-1}$. For the central totals
$|T-\rho\ell|\le H$, and sufficiently small fixed $\varepsilon$,
$T/\ell$ lies in a fixed compact subinterval of $(1,\infty)$.
Uniform Stirling estimates give

$$
\begin{aligned}
\log_2 K(T,\ell)
&=\ell f(T/\ell)+O(\log s),\\
f(x)&=x\log_2 x-(x-1)\log_2(x-1),\\
f(\rho)&=\rho\theta,\qquad
f'(x)=\log_2\frac{x}{x-1}.
\end{aligned}
\tag{E17}
$$

The derivative is bounded on that compact interval. Consequently, for a
fixed constant $C_2$ independent of small $\varepsilon$,

$$
\log_2 K(T,\ell)
\ge \rho\theta\ell-C_2H-O(\log s)
\ge \bigl(\theta-(\theta+C_2/4)\varepsilon\bigr)p-O(\log s).
\tag{E18}
$$

Given any $d<\theta$, first choose $\varepsilon$ sufficiently small and
then $s$ sufficiently large that (E18) is at least $dp$.

At each fixed prefix and total, restrict the uniform composition law to
good words, without renormalizing it. By the injectivity just proved, the
pushforward of that subprobability by either output has maximum atom at
most $K(T,\ell)^{-1}\le2^{-dp}$. If a total is outside the central
window, the restricted measure is zero. Mixing these subprobabilities
over the original law of the prefix and total keeps the same maximum
atom bound. Its total mass is the original probability of (E12), at least
$1-e^{-cs}$ by (E16). This proves (E4). It is essential here to mix the
restricted subprobabilities, rather than to condition and renormalize
separately on good words or rare totals.

### 11.5. Retaining an exact asymptotically critical whole total

Fix $L$ in the stated window and compare with independent geometric
letters having success parameter $a_L=s/L$. Conditional on total $L$
this comparison law is precisely the required uniform composition law,
and $L$ is its exact mean total. Since $L/s\to\rho$ uniformly in the
window, these parameters lie in a fixed compact subset of $(0,1)$.
The constants in the geometric exponential-moment estimate (E15) may
therefore be chosen uniformly, now centering each letter at $L/s$.
For every $j\le\ell$,

$$
|jL/s-\rho j|\le G(s)=o(s).
\tag{E22}
$$

Eventually this is at most $H/2$. Thus the comparison-law probability
of failure of (E12) is exponentially small, uniformly over $L,p$.
The exact mean probability is

$$
\mathbb P_{a_L}(S_1=L)
=\binom{L-1}{s-1}a_L^s(1-a_L)^{L-s}
\ge c_3s^{-1/2},
\tag{E23}
$$

uniformly for these parameters, by Stirling's formula. Conditioning the
comparison law on its mean total therefore leaves an exponentially
small failure probability, since the polynomial factor $s^{1/2}$ is
absorbed by reducing the exponential constant. This avoids division by
the potentially rare total under the original critical parameter.

At each fixed prefix and tail total, the remaining tail law is still
uniform on all its positive compositions. The deterministic separation
and counting arguments are unchanged. Mixing the good subprobabilities
using the exact-total law now proves (E4) for that law, uniformly over
the whole window. The following entropy deductions apply to either law.

### 11.6. Shannon and fixed-order Renyi deductions

Let $\mu=\nu+\xi$ be the decomposition from (E4), put
$m=\|\nu\|_1\ge1-e^{-cs}$, and let $q=\nu/m$. Concavity of Shannon
entropy and $\|q\|_\infty\le2^{-dp}/m$ imply

$$
H_1(\mu)\ge mH_1(q)\ge m(dp+\log_2m).
\tag{E19}
$$

The omitted terms are $O(pe^{-cs})$ uniformly on the band. Since this
holds for every $d<\theta$, it proves (E3).

For $t>0$, convexity and the two subprobability bounds give

$$
\begin{aligned}
\sum_x\mu(x)^{1+t}
&\le2^t\left(\sum_x\nu(x)^{1+t}+\sum_x\xi(x)^{1+t}\right)\\
&\le2^t\left(2^{-tdp}+e^{-(1+t)cs}\right).
\end{aligned}
\tag{E20}
$$

Choose a fixed $t>0$ with $td\lambda\log2\le c$, for example
$t=c/(2d\lambda\log2)$. Since $p\le\lambda s$, the second term is at
most the first. With $\beta=1+t$ this yields

$$
H_{1+t}(\mu)\ge dp-1-1/t,
\tag{E21}
$$

which proves (E5). Both outputs were treated directly in (E14), so no
additional logarithmic carry loss is needed in this conclusion.

### 11.7. Scope and reproducibility

This is an analytic result; no finite numerical scan can verify its
ineffective eventual separation threshold. Every arithmetic form,
height bound, valuation gap, conditioning operation and exceptional-mass
estimate is specified above. Constants can depend on the fixed precision
band and on $d$. The order $\beta>1$ is fixed only after these choices;
it is not asserted uniform as $d$ approaches $\theta$.

The statement controls Shannon dimension at $\theta$ and fixed-order
Renyi dimensions approaching it from below. It gives neither full binary
dimension nor convergence to the uniform law. In particular it does not
cross the strict threshold required for the current improved-compression
consumer. Even such a compression improvement would still need a separate
argument to produce a smaller legal source for every supplied integer.
No universal orbit descent or Collatz solution follows here.


### 11.8. Arbitrary contiguous binary windows

The same mechanism also controls windows of output bits that need not
start at the lowest bit. This is a bound for the actual marginal window
law; it is not a conditional entropy bound inside every dyadic component.

**Theorem 11.** Fix $0<c_0<\lambda<\rho$ and $0<d<\theta$. For either
$V_s=W_s$ or $V_s=u_s$, put

$$
Z_{s,p,q}=\left\lfloor\frac{[V_s]_{2^p}}{2^{p-q}}\right\rfloor,
\qquad c_0s\le q\le p\le\lambda s.
\tag{W1}
$$

Uniformly over these integer parameters, the law of $Z_{s,p,q}$ has a
subprobability of mass at least $1-e^{-cs}$ and maximum atom at most
$2^{-dq}$, for all sufficiently large $s$. Consequently

$$
\liminf_{s\to\infty}\ \min_{c_0s\le q\le p\le\lambda s}
\frac{H_1(Z_{s,p,q})}{q}\ge\theta,
\qquad H_\beta(Z_{s,p,q})\ge dq-O(1)
\tag{W2}
$$

for some fixed $\beta>1$. These conclusions hold both for the original
independent geometric law and, uniformly, for each exact whole total
in any prescribed asymptotically critical window as in Theorem 10.
All eventual arithmetic thresholds remain ineffective.

**Proof.** Set $N=3^s$, $M=2^p$, $L_0=2^{p-q}$, and use the terminal
block of the preceding proof with $q$ replacing $p$ in its choice of
length and strip width:

$$
\ell=\left\lfloor\frac{(1-\varepsilon)q}{\rho}\right\rfloor,
\qquad H=\frac{\varepsilon q}{4}.
\tag{W3}
$$

Fix the earlier prefix and terminal total $T$. Retain only good terminal
words satisfying (E12) with this width. All identities (E10)--(E14)
continue to hold. In particular distinct words have
$D=B(w)-B(w')\ne0$, its binary valuation is their first differing
partial exponent, and $v_2(D)<T$. Uniformly on the good set,

$$
0<B(w)\le2^q2^{-\varepsilon q/2},\qquad
T\le(1-3\varepsilon/4)q.
\tag{W4}
$$

Suppose two such words have output residues in the same ordinary
interval of length $L_0$ in $[0,M)$. Write the difference of these
residues as $z$, with $|z|<L_0$, and the actual integer output difference
as $Ma+z$. Subtracting the raw or canonical identities gives

$$
D=2^{T+p}a+2^Tz-Nb,\qquad
|a|\le\frac{2sN}{M},\qquad |b|\le4s2^T.
\tag{W5}
$$

For the raw output, $b$ is the difference of the two $A$ values. For the
canonical output it also includes the carry difference shown in (E14).
The bound on $a$ uses $|V_s(w)-V_s(w')|<sN$ and $|z|<M$.

If $z=0$, the two-dimensional separation lemma already excludes (W5):
its bound for $D$ follows from (W4), since $q\le p$ and $q\ge c_0s$.
If $a=0$, then

$$
|Nb|\le2^T|z|+|D|
\le2^{p-3\varepsilon q/4}+2^{q-\varepsilon q/2}<N
\tag{W6}
$$

eventually, because $p\le\lambda s<\rho s$. Thus $b=0$, which makes
$D=2^Tz$, contradicting $v_2(D)<T$. If $b=0$ and $a\ne0$, then
$|D|\ge2^T(M-|z|)\ge M$ eventually, contradicting (W4).
We may therefore assume $a,b,z$ are all nonzero.

Put $X_1=2^{T+p}a$, $X_2=Nb$, $X_3=2^Tz$. At the infinite place use
the independent forms $X_1+X_3-X_2,X_1,X_3$; at two and three use the
three coordinate forms. Their fixed-place product is at most

$$
\begin{aligned}
&|D|\,|X_1X_3|\prod_{v\in\{2,3\}}|X_1X_2X_3|_v\\
&\hspace{1cm}\le\frac{|D|\,|a|\,|z|}{N}
\le2s\frac{|D|L_0}{M}
\le2s2^{-\varepsilon q/2}.
\end{aligned}
\tag{W7}
$$

The vector norm is at most $4sN2^T\le e^{Ks}$ for a fixed $K$.
The integral fixed-place Subspace Theorem, in dimension three, therefore
puts all possible vectors into finitely many rational planes for all
large $s$. Lower-dimensional exceptional subspaces may be enlarged to
planes. The planes depend on the fixed constants, not on the word,
prefix, total or integer precision parameters.

We classify these exceptional planes rather than assuming they disappear.
Since $|X_2|\ge N$, (W4) and (W6) give uniformly

$$
\frac{D}{X_2}\longrightarrow0,\qquad
\frac{X_3}{X_2}\longrightarrow0,\qquad
\frac{X_1}{X_2}\longrightarrow1.
\tag{W8}
$$

For a fixed plane $c_1X_1+c_2X_2+c_3X_3=0$, it follows that any
occurring plane must satisfy $c_1+c_2=0$ once $s$ is sufficiently large.
There are only finitely many planes, so this exclusion is uniform.
Substituting $X_1-X_2=D-X_3$ now gives
$c_1D+(c_3-c_1)X_3=0$. Here $c_1\ne0$, since otherwise the plane
would force $X_3=0$, and $c_3-c_1\ne0$, since otherwise it would force
$D=0$. Hence

$$
D=\kappa 2^Tz
\tag{W9}
$$

for one of finitely many fixed nonzero rational numbers $\kappa$.
Choose an integer $C_0\ge0$ with $v_2(\kappa)\ge-C_0$ for all of them.
Then $v_2(D)\ge T-C_0$. The first-different-exponent property of $B$
shows that the two words have identical sets of partial exponents below
$T-C_0$.

Fix one good word whose output lies in the interval. Every other good
word with output there has the same partial exponents below $T-C_0$;
only the at most $C_0$ integer positions in $[T-C_0,T)$ may differ.
The set of partial exponents, together with $T$, determines the whole
positive composition. Thus the interval contains outputs of at most
$2^{C_0}$ good words. If no exceptional plane survives, it contains at
most one word. In either case there is a fixed finite multiplicity
bound, independent of $s,p,q$, the prefix and $T$.

At each fixed prefix and total, uniform composition counts now bound
the good subprobability of every such interval by
$2^{C_0}/\binom{T-1}{\ell-1}$. The estimates (E15)--(E18), with $q$
in place of $p$, give exponentially small failure and
$\log_2\binom{T-1}{\ell-1}\ge(\theta-O(\varepsilon))q-O(\log s)$.
For a prescribed $d<\theta$, choose a strict margin in this exponent
and absorb both $C_0$ and the logarithmic term by increasing the
ineffective threshold. Mixing restricted subprobabilities as before
gives mass at least $1-e^{-cs}$ and interval mass at most $2^{-dq}$.
The equal intervals corresponding to (W1) prove the assertion.

For exact whole totals, the comparison parameter $s/L$ and its
polynomial mean-conditioning denominator apply without change, since
the new strip width is still bounded below by a positive multiple of
$s$. The entropy deductions (E19)--(E21) apply with $q$ in place of
$p$; in particular one may again choose a fixed $t>0$ with
$td\lambda\log2\le c$. This proves (W2). $\square$

The interval estimate is stronger than the estimate for just the lowest
bits. Nevertheless, all assertions here concern marginal laws. They
do not assert positive entropy after conditioning on every earlier
dyadic cell. Correlations between windows, or additive structure of
the actual independent block factors, still have to be controlled to
obtain a strict entropy gain under convolution.

## 12. Reproducibility and verification scope

All asymptotic estimates have analytic proofs above. The supplement
retains the five finite audit programs and their saved reports unchanged
from the accepted first version. They were not rerun for this revision.
The new Section 8 uses the same exact split, projectivity and multiplier
interfaces, followed by analytic Fourier estimates; no new numerical grid
or fitted rate is used. Section 9 adds one fixed exact conditional-clock
interface checker. From the supplement root, run these commands separately:

```sh
python experiments/rees_multiplicative_collision_audit.py --workers 5 --output multiplicative.json
python experiments/rees_canonical_collision_audit.py --workers 5 --output canonical.json
python experiments/rees_prefix_lift_audit.py --workers 5 --output prefix.json
python experiments/rees_canonical_pointwise_audit.py --workers 5 --output pointwise.json
python experiments/cassian_shifted_prefix_audit.py
python experiments/critical_bridge_interfaces_20261025.py
```

They use Python's standard library and at most five worker processes.
The first audit checks 24,922 raw/ternary identities, 54,065 off-diagonal
unit-count bounds and 30 rational-law energy inequalities, using integer
arithmetic throughout. The second checks 1,790 unit-count bounds,
880,880 translation-dependent collision indicators, 205 actual
positive/negative word-orbit pairs, 799 canonical splits and 3,995 dyadic
affine identities, also exactly. The third checks 726 exact three-lift
identities and 1,509 exact word splits; its additional 50 correlation and
100 norm controls use floating point and are not numerical certificates.
All prescribed checks passed. Source hashes and the finite parameter
sets are recorded in the reports.

The fourth audit checks 75 projective marginals, 25 Ramanujan identities
through 1,210 exact cyclotomic coefficients, and 4,060 residue-bucket
geometric-series identities. It uses integer and rational arithmetic;
its decimal variance displays are descriptive. The three earlier audits
were not rerun for this additional Fourier argument.

The fifth audit independently checks Mahler's diagonal refinement on the
full depth-four totient cube: 11,664 actual canonical trajectories,
46,656 diagonal identities and 46,656 lower-digit invariances. Three
rational parameters give 12 product-energy comparisons, three exact
depth-two atom checks and three corrected trit-factor checks. It imports
only the fourth program's exact distribution helper. All comparisons
are exact; the displayed critical constants are descriptive evaluations
of the analytic product. The two local formula corrections are recorded
with the public discussion in [6].

The finite checks test algebraic interfaces and catch implementation
errors. They do not prove an asymptotic rate, and no fitted rate or
extrapolation enters the theorems. The proofs and audit programs are
available together so each verification claim can be inspected at its
stated scope. Audit code is released under the MIT license included in
the supplement.

The new conditional-clock checker uses five predetermined jobs and five
workers. It verifies 1,173 actual source/word trajectories against the
conditional conductor mixture, with 703 mixture summands, and 286 exact
tail comparisons at five remaining-clock states. The actual-source replay
and modular mixture use separate calculations. It also checks the mark
probabilities and the dominating tail moment in (9.5). All cases pass.
It does not verify the Subspace argument or its ineffective limit. The
earlier carry, endpoint and resonance grids were not enlarged or rerun.

The iid argument has undergone an author audit of the correlated suffix
phase, normalized unit Parseval factor, periodic tent, cutoff derivative
jumps, conductor reduction and order of limits. This is not a claim of
external review. The critical-clock audit separately checks the adapted
pair kernels, centered comparison laws, terminal episode accounting,
truncated cores, cancellation of the initial coefficient in the fixed-place
product, the two grouping cases, fixed-total carry counts, linear-size
removed-block mixtures and order of limits. Theorem 6 uses the elementary proof; Theorem 7
uses the complete Subspace input in Appendix A. Neither audit asserts an
effective critical-clock convergence rate or individual Collatz descent.


Section 10 and Appendix B are analytic additions and require no further
experiment. Their author audit checks all lifts modulo $Q/3^k$, the
combined denominator/width valuation gap, harmonic summation, the full-grid
bound on omitted clocks, the exact geometric tilt, and both signs of the
corner height relative to the actual total. The triangle argument retains
the reduced-conductor factor, averages the original clock law, and applies
the alias filter to a frequency-dependent complex piece without claiming
that the pieces define one new probability law. The threshold is
ineffective. Shorter observed cores and the full linear-resolution energy
remain open. The written proof, not the finite checkers, carries these claims.


Section 11 is another analytic addition. Its proof includes the fixed-place
forms and all height and valuation estimates, the canonical carry in the
collision equation, uniform composition counts, restricted-subprobability
mixing, and exact-total comparison at the comparison law's mean. The
entropy theorem needs no numerical experiment. Its eventual arithmetic
threshold is ineffective; the author audit is included in the supplement.
No dimension strictly above the critical source entropy is proved.

## Appendix A. Critical geometric and arithmetic inputs

In this appendix, fix $\alpha=\log_3 2$, put $q=1-\alpha$, and
write $e(x)=\exp(2\pi i x)$. We record the inputs for Theorem 7, using the actual canonical
endpoint $u_n$ defined in Section 1. This argument does not use a
stationary replacement or the raw integer $W_n$.

Fourier Wren [13] proposed unfolding bounded chains of Tao's black
triangles into an $S$-unit sum and applying the Subspace Theorem. That
public sketch is the conceptual predecessor of Appendix A.2. We supply
the complete critical-law application, including interleaved visits and
cancelling subsums. An excursion argument in the original pair steps
then controls the number of all visited triangles. Finally, a bound on
the actual endpoint mass near $0$ and $3^n$ permits finite Fourier
completion. This last step avoids a growing absolute-sum completion cost.

The only deep arithmetic input is Schlickewei's $S$-adic Subspace
Theorem in the following integral form [14, Theorem 2.3]. For a finite
set of places containing infinity, choose at each place $s$ independent
linear forms in $s$ variables with algebraic coefficients. For every
$\zeta>0$, integer vectors $Y$ satisfying

$$
\prod_v\prod_{i=1}^s |L_{i,v}(Y)|_v
\le \|Y\|_\infty^{-\zeta}
\tag{A.1}
$$

lie in finitely many proper rational linear subspaces. Our forms will be
fixed and rational. No moving-form version or effective height threshold
is assumed.

### A.1. The critical pair process

The canonical update and the bounds in (8) give

$$
u_j=[2^{-e_j}(3u_{j-1}+1)]_{3^j},\qquad u_0=0.
\tag{A.2}
$$

Reversing the iid exponent word therefore identifies the law of $u_n$
modulo $3^n$ with the law of

$$
\sum_{i=1}^n3^{i-1}2^{-(e_1+\cdots+e_i)}\pmod{3^n}.
$$

In particular, if $\widehat\mu_n(t)=\mathbb E e(tu_n/3^n)$, then

$$
\widehat\mu_n(3^{n-r}\xi)=\widehat\mu_r(\xi).
\tag{A.3}
$$

This is an exact projective identity of the laws. We use reversal only
for this phase calculation, not to transport a conditioned boundary event.

For a primitive $\xi$ modulo $3^n$, let $K=\lfloor n/2\rfloor$,
$b_j=e_{2j-1}+e_{2j}$, and $E_j=b_1+\cdots+b_j$. Put

$$
\eta=\log_2 9=2/\alpha,\qquad
\theta(j,\ell)=\left\{\frac{\xi3^{2j-2}2^{1-\ell}}{3^n}\right\},
\tag{A.4}
$$

where the braces select the centered representative and powers of two
are inverted modulo $3^n$. Fix a sufficiently small constant
$\varepsilon>0$ allowed by [2, Lemma 7.4]; below we further require
$\varepsilon\le e^{-140}$. A point in $[K]\times\mathbb Z$ is black
when $|\theta(j,\ell)|\le\varepsilon$ and white otherwise.

Tao's geometric lemma partitions the black lattice points into disjoint
triangles

$$
\Delta=\{(j,\ell):j\ge j_\Delta,\ \ell\le\ell_\Delta,
\ (j-j_\Delta)\log9+(\ell_\Delta-\ell)\log2\le s_\Delta\},
\tag{A.5}
$$

separated by Euclidean distance at least
$\tfrac1{10}\log(1/\varepsilon)$. All triangles lie in $[K]\times\mathbb Z$.
If the phase at the top-left corner is $a/3^m$, then

$$
m=n-2j_\Delta+2,\quad 3\nmid a,\quad
s_\Delta=\log(\varepsilon3^m/|a|),\quad
a2^{\ell_\Delta-1}\equiv\xi\pmod{3^m}.
\tag{A.6}
$$

These formulas follow directly from (A.4) and the construction in that
lemma. In particular the real right vertex is
$(n+2)/2+\log(\varepsilon/|a|)/\log9<K$ for $\varepsilon<1/100$.

Call an index marked if $b_j=3$. Let $W$ count marked white points
$(j,E_j)$, and let $T$ count distinct black triangles containing marked
points. These definitions count all marked visits, not increasing-top
record visits. The marked probability is

$$
\mathbb P(b_j=3)=2\alpha^2q>1/4.
$$

Conditional on all pair totals, their splits are independent uniform:
every split of a total $b$ has weight $\alpha^2q^{b-2}$. For $b=3$,
the two phases have mean of modulus $|\cos(\pi\theta(j,E_j))|$.
Tao's pair calculation [2, Section 7] consequently gives

$$
|\widehat\mu_n(\xi)|\le\mathbb E e^{-\varepsilon^3 W}.
\tag{A.7}
$$

The last singleton when $n$ is odd has a conditional factor of modulus
at most one. The same bound applies to the complex contribution with
any additional cutoff measurable in the pair totals.

### A.2. Excluding a fixed number of triangles

**Lemma A.1.** Fix $B<\infty$, $0<\sigma<\log3$, and an integer
$R\ge1$. Uniformly over $1\le p\le Bn$ and primitive $\xi$ for which
an integer $d$ satisfies

$$
2^p\xi\equiv d\pmod{3^n},\qquad
0<|d|\le\exp((\log3-\sigma)n),\qquad v_2(d)<p,
\tag{A.8}
$$

one has, for all sufficiently large $n$,

$$
\mathbb E[e^{-\varepsilon^3W}\mathbf1_{T\le R}]
\le C_Rn^2e^{-c\sqrt n}.
\tag{A.9}
$$

The threshold can depend on $R,B,\sigma$ and is ineffective.

*Proof.* Divide the congruence in (A.8) by $2^{v_2(d)}$, replacing
$p$ by $p-v_2(d)\ge1$ and $d$ by its odd part. The hypotheses persist
and $\xi$ is unchanged. Henceforth $d$ is odd. We first prove a
deterministic exclusion along every sequence with $H=o(n)$ and
$p\le Bn$. Suppose the following conditions hold:

$$
|E_j-\eta j|\le H\quad(1\le j\le K),\qquad W\le H,\qquad T\le R,
\tag{A.10}
$$

and every integer index interval of length at least $H$ contains at
least one eighth as many marks as indices. We show these conditions and
(A.8) cannot hold along an unbounded sequence of $n$.

Write each visited triangle as
$j\ge j_i$, $\ell\le\ell_i$, $\ell\ge\eta j+c_i$. By (A.6),

$$
c_i=\ell_i-(n+2)\log_2 3+\log_2(|a_i|/\varepsilon).
$$

Visitation in the strip in (A.10) implies $c_i\le H$. Define its
possibly empty integer core by

$$
I_i=\left[j_i,\left\lfloor\frac{\ell_i-H-1}{\eta}\right\rfloor\right].
\tag{A.11}
$$

At each integer index of this core, the same height
$\lceil\eta j+H\rceil$ lies in the triangle. The lattice partition
therefore makes distinct cores disjoint. No ordering of the path's visits
or separation of solid real interiors is assumed.

A visit must have $j\le(\ell_i+H)/\eta$. It therefore lies in the core
or in at most $4H$ further indices to its right, for $H\ge2$; the same
bound covers an empty core. Discard cores of length less than $10H$.
Outside the retained cores there are at most $14RH$ black marked indices.
In a gap of length at least $H$, mark density and $W\le H$ give
$|\mathrm{gap}|/8\le H+14RH$. Thus all gaps, including the initial
and final gaps, have length $O_R(H)$. At least one retained core exists
when $n/H$ is large.

Order the remaining $L\le R$ cores. Their lengths imply strict increase
of both $j_i$ and $\ell_i$, and their endpoints and gaps give

$$
j_1=O_R(H),\qquad
j_i=\ell_{i-1}/\eta+O_R(H)\quad(i\ge2),\qquad
\ell_L=(\log_2 3)n+O_R(H).
\tag{A.12}
$$

All retained $\ell_i$ are positive. Moreover $c_i\le H$ yields

$$
|a_i|2^{\ell_i}\le\varepsilon3^{n+2}2^H.
\tag{A.13}
$$

Put $m_i=n-2j_i+2$. Adjacent corner congruences in (A.6) imply the
integer identities

$$
a_{i-1}-a_i2^{\ell_i-\ell_{i-1}}=b_i3^{m_i}\quad(2\le i\le L).
\tag{A.14}
$$

By (A.12)--(A.13), each nonzero $b_i$ has
$\log|b_i|=O_R(H)$, and $\log|a_L|=O_R(H)$. For example, dividing
either term in the numerator in (A.14) by $3^{m_i}$ bounds its size by
$\varepsilon2^H3^{2j_i}2^{-\ell_{i-1}}$, whose logarithm is $O_R(H)$.
The first corner and (A.8) similarly give

$$
a_12^{p+\ell_1-1}-b_03^{m_1}=d,
\qquad \log|b_0|\le p\log2+O_R(H+1),\qquad v_2(b_0)=0.
\tag{A.15}
$$

In particular $b_0\ne0$. Telescoping (A.14) gives

$$
d=a_L2^{p+\ell_L-1}
+\sum_{i=2}^L b_i2^{p+\ell_{i-1}-1}3^{m_i}-b_03^{m_1}.
\tag{A.16}
$$

The initial coefficient $b_0$ is exceptional: its absolute size can
grow exponentially in $p$, but its binary valuation is zero. All other
nonzero terms have the form $c2^A3^B$ with nonnegative exponents and

$$
\log|c|=o(n),\qquad
A\log2+B\log3=n\log3+p\log2+o(n),\qquad A\ge p.
\tag{A.17}
$$

Suppose counterexamples exist at arbitrarily large $n$. Pass to a
subsequence with a fixed number of nonzero terms, a limit $p/n\to t$
in $[0,B]$, and limits of their normalized binary exponents. We distinguish
two cases so that no small-coefficient hypothesis is imposed on $b_0$
when $p$ is of linear size.

If $t=0$, every coefficient, including $b_0$, has logarithmic size
$o(n)$, and every monomial has logarithmic size $n\log3+o(n)$.
Group all terms with equal limiting binary exponents. Within a group,
both exponent differences are $o(n)$, so factoring the coordinatewise
minimum exponents leaves an integer coefficient of logarithmic size
$o(n)$. Discard zero groups. The bottom group survives because $b_0$
is odd and every other term is divisible by $2^p$. The top group survives
because $a_L2^{p+\ell_L-1}$ is a ternary unit while every other term
is divisible by three. Thus at least two groups remain, their normalized
binary valuations have distinct limits, and each group has absolute
logarithmic size $n\log3+o(n)$.

If $t>0$, keep $Y_0=-b_03^{m_1}$ as a separate coordinate and group
only the other terms by their limiting binary exponents. For the same
reason, their nonzero group sums have the form

$$
Y_i=C_i2^{A_i}3^{B_i},\quad \log|C_i|=o(n)\quad(i\ge1),
\qquad \sum_{i\ge0}Y_i=d.
\tag{A.18}
$$

Their distinct normalized binary valuations have limits at least $t$,
whereas $v_2(Y_0)=0$. The top group again survives by its ternary-unit
term. There are at least two coordinates. Moreover
$m_1=n-o(n)$ and
$\log\|Y\|_\infty\le(\log3+B\log2)n+o(n)$.
No lower bound for $|b_0|$ beyond integrality is needed.

In both cases use places $\{\infty,2,3\}$ in (A.1). At infinity use
the sum and all but one coordinate, and at the finite places use all
coordinate forms. For $t=0$ omit any one coordinate at infinity. The
usual product bound is $|d|\prod_i|C_i|/|Y_1|\le e^{-\sigma n+o(n)}$.
For $t>0$ omit precisely $Y_0$. Its possibly large coefficient cancels
from the required estimate:

$$
\begin{aligned}
\prod_v\prod_i|L_{i,v}(Y)|_v
&=|d|\,|Y_0|_2|Y_0|_3
  \prod_{i\ge1}|Y_i|_\infty|Y_i|_2|Y_i|_3\\
&\le |d|\,3^{-m_1}\prod_{i\ge1}|C_i|\\
&\le e^{-\sigma n+o(n)}\le\|Y\|_\infty^{-\zeta}
\end{aligned}
\tag{A.19}
$$

for some fixed $\zeta>0$ depending only on $B,\sigma$. The finite-place
bound uses $|b_0|_2=1$ and $|b_0|_3\le1$, not a small-height estimate
for $b_0$. In the $t=0$ case a fixed positive $\zeta$ also follows.
The forms are rational, independent and fixed after selecting the number
of groups and their order. The Subspace Theorem forces a fixed rational
relation along an infinite subsequence. Among its nonzero coefficients,
the term with smallest limiting binary valuation is unique. Multiplying
by fixed rational coefficients does not change the strict eventual
valuation ordering, so their sum cannot vanish. This contradiction proves
the deterministic exclusion in both cases.

Now take $H=\lfloor n^{3/4}\rfloor$. The pair increments have mean
$\eta$ and an exponential moment. Chernoff bounds and a union over
indices give a strip-failure probability at most
$Cn\exp(-cH^2/n)$. Marks are iid Bernoulli with mean greater than $1/4$;
a union over at most $K^2$ intervals bounds failure of mark density by
$Cn^2e^{-cH}$. No independence between these good events is needed.
On their intersection and $T\le R$, the deterministic exclusion forces
$W>H$ for all large $n$. This proves (A.9). A failure of uniformity over
$p\le Bn$ and the fixed height gap $\sigma$ would give precisely the
forbidden sequence of deterministic counterexamples. $\square$

### A.3. Nonconcentration at the canonical interval boundary

**Lemma A.2.** Put $X_n=u_n/3^n$,
$\rho_*=4\alpha q<1$, and $\kappa_*=-\log\rho_* /(4\log2)>0$.
There is a constant $C$ such that for every $n\ge1$ and
$0<\delta\le1/2$,

$$
\mathbb P(\min(X_n,1-X_n)\le\delta)
\le C(\delta^{\kappa_*}+2^{-\kappa_* n}).
\tag{A.20}
$$

*Proof.* The exact integer version of (A.2) is

$$
2^{e_j}u_j=3u_{j-1}+1+3^j k_j,\qquad 0\le k_j<2^{e_j}.
$$

For $v_j=3^j-u_j$ and $Y_j=v_j/3^j=1-X_j$, it follows that

$$
\begin{aligned}
2^{e_j}X_j&=X_{j-1}+3^{-j}+k_j,\\
2^{e_j}Y_j&=Y_{j-1}-3^{-j}+k'_j,
\qquad k'_j=2^{e_j}-1-k_j\in[0,2^{e_j}).
\end{aligned}
\tag{A.21}
$$

First suppose $2^{-n}\le\delta\le1/16$. Put
$t=\log_2(1/\delta)$ and $m=\lfloor t/4\rfloor$, so
$1\le m\le n/4$. Let $S$ be the sum of the last $m$ exponents.
On $S\le2m$, if $X_n\le\delta$, backward propagation in (A.21)
forces all those $k_j$ to be zero. Every pre-carry expression is at
most $2^S\delta\le\sqrt\delta<1$; because the preceding normalized
state lies in $(0,1)$ and the carry is a nonnegative integer, no other
carry is possible.

If instead $Y_n\le\delta$, backward propagation forces all $k'_j=0$.
The positive accumulated errors have the uniform upper bound

$$
\begin{aligned}
2^S\left(\delta+\sum_{j=n-m+1}^n3^{-j}\right)
&\le\sqrt\delta+\tfrac12 2^{2m}3^{-(n-m)}\\
&\le\tfrac14+\tfrac12(\sqrt2/3^{3/4})^n<1,
\end{aligned}
\tag{A.22}
$$

where $n\ge4$. Thus throughout this final block the actual positive
integers obey one of the two unwrapped recursions

$$
u_j=(3u_{j-1}+1)/2^{e_j},\qquad
v_j=(3v_{j-1}-1)/2^{e_j}.
\tag{A.23}
$$

Condition on the integer state at the start of the block. To continue
either recursion for $m$ positive integer steps, its first $m-1$
intermediate states must be odd. Therefore its first $m-1$ exponents
are uniquely prescribed exact valuations, determined successively by
the state. Each has probability at most $\alpha$. The final exponent
may truncate its valuation and is not forced. Either unwrapped family
has conditional probability at most $\alpha^{m-1}$, uniformly in the
starting state. The two orientations cost a union factor two.

For the excluded clock, take $z=1/(2q)>1$. Since
$\mathbb E z^e=\alpha/q$, Chernoff gives

$$
\mathbb P(S>2m)\le z^{-2m}(\mathbb E z^e)^m
=(4\alpha q)^m=\rho_*^m.
$$

The probability in (A.20) is thus at most
$2\alpha^{m-1}+\rho_*^m$. At the critical parameter
$\rho_*>\alpha$, so this is at most $C\rho_*^m\le C'\delta^{\kappa_*}$.
For $\delta<2^{-n}$ use monotonicity and the bound at $2^{-n}$.
The remaining large $\delta$ and finitely many small $n$ are covered
by increasing $C$. $\square$


## Appendix B. The truncated geometric moment

We give the clock averaging used in Theorem 8. Let $\alpha=\log_3 2$,
$q=1-\alpha$, $\rho=1/\alpha$, $C_\alpha=\log((1+\alpha)/\alpha)$
and $\tau=2/(1+\alpha)$. The total $S$ is a sum of $s$ independent
positive geometric variables with parameter $\alpha$. Its rate function is

$$
I(x)=-\log\alpha-(x-1)\log q-x\log x+(x-1)\log(x-1),\qquad x\ge1,
\tag{B.1}
$$

with $0\log0=0$. It is strictly convex for $x>1$,
$I'(x)=\log((x-1)/(qx))$, and has its unique zero at $\rho$.
The usual exponential Markov inequality, optimized over its parameter,
gives $\Pr(S<xs)\le e^{-I(x)s}$ for $1\le x<\rho$.
The same optimization gives upper tails above the mean for any geometric
parameter.

Fix $0\le\gamma<\rho$. Suppose a nonnegative quantity $R_s(S)$ is
bounded by $CsMN$ at every total. Suppose also that for every fixed
$\delta,\eta>0$ with $\gamma+\delta<\rho$, eventually

$$
R_s(S)\le CsMN\,2^{\gamma s}e^{\eta s}(2^{-S}+3^{-s})
\quad\text{when }s\le S\le6s,\quad S\ge(\gamma+\delta)s.
\tag{B.2}
$$

The eventual threshold and constants may depend on these fixed
parameters. Then for every $\varepsilon>0$,

$$
\mathbb E R_s(S)\le CsMN e^{-(F(\gamma)-\varepsilon)s},
\tag{B.3}
$$

where $F$ is defined in Section 10.

To prove this, put $x=\gamma+\delta<\rho$. If $\gamma<1$, choose
$\delta$ so $x<1$; then there is no lower omitted tail. Otherwise that
tail costs $CsMN e^{-I(x)s}$. For the upper omitted tail, $\alpha>5/8$
and the Chernoff parameter $4/3$ yield

$$
\Pr(S>6s)\le(1215/4096)^s.
\tag{B.4}
$$

Its exponential rate exceeds $C_\alpha$, hence every value of $F$.

For the retained moment, multiplying the product law by $2^{-S}$
changes the geometric parameter to $\alpha_*=(1+\alpha)/2$ exactly.
If $\Pr_*$ denotes that product law, then

$$
\mathbb E[2^{-S}\mathbf1_{S\ge xs}]
=\left(\frac{\alpha}{1+\alpha}\right)^s\Pr_*(S\ge xs).
\tag{B.5}
$$

The tilted mean is $\tau$, and its rate function is

$$
I_*(x)=I(x)+x\log2-C_\alpha.
\tag{B.6}
$$

For $\gamma\le\tau$, dropping the probability in (B.5) gives rate
$C_\alpha-\gamma\log2=F(\gamma)$ after multiplication by
$2^{\gamma s}$. For $\gamma>\tau$, $x>\gamma>\tau$, so the tilted
upper-tail bound gives rate

$$
C_\alpha-\gamma\log2+I_*(x)
=I(x)+(x-\gamma)\log2\ge I(\gamma)=F(\gamma).
\tag{B.7}
$$

The inequality follows from $I'(u)\ge-\log2$ for $u\ge\tau$.
At $\tau$, $I(\tau)=C_\alpha-\tau\log2$ and $I'(\tau)=-\log2$.
Convexity therefore gives $I(u)\ge C_\alpha-u\log2$ for $u\ge1$.
If the lower omitted tail is present, choose $\delta$ small enough that
$I(\gamma+\delta)\ge F(\gamma)-\varepsilon/3$.

The remaining term $2^{\gamma s}3^{-s}$ in (B.2) has rate
$\log3-\gamma\log2$, at least $F(\gamma)$. Below $\tau$ this follows
from $C_\alpha<\log3$. Above $\tau$ the difference
$\log3-u\log2-I(u)$ decreases to zero on $[\tau,\rho]$, by the
displayed derivative and $I(\rho)=0$. Finally choose
$\eta<\varepsilon/3$ in (B.2). These bounds prove (B.3).

The same identities show that $F$ is continuous and positive for every
fixed $\gamma<\rho$. The rate at $\gamma=1$ is
$\log((1+\alpha)/(2\alpha))=0.256563820804378\ldots$; no decimal
approximation is used by the proof. The averaging argument is elementary.
The ineffective threshold in Theorem 8 comes from its separate
Subspace input.


## References

[1] Mary Rees. *Push-forward of geometric distributions under Collatz
iteration: Part 1*. arXiv:2404.12279v2 (2024), especially Theorem 2.10
and Conjecture 4.1. https://arxiv.org/abs/2404.12279v2

[2] Terence Tao. *Almost all orbits of the Collatz map attain almost
bounded values*. arXiv:1909.03562v7 (2026), especially the Syracuse
offset definition and Sections 6--7. https://arxiv.org/abs/1909.03562v7

[3] David Leen. *Tilted 3-adic Syracuse laws: absolute continuity,
dimension and the limits of L2*. Preprint, version-specific Zenodo record
23268832 (2026), especially Theorem E(a) and Section 8.
https://doi.org/10.5281/zenodo.23268832

[4] J. Lawrence Carter and Mark N. Wegman. *Universal classes of hash
functions*. Journal of Computer and System Sciences 18(2), 143--154
(1979). https://doi.org/10.1016/0022-0000(79)90044-8

[5] Avrim Blum. *Universal and Perfect Hashing*. 15-451 Algorithms,
Lecture 10 and recitation, Carnegie Mellon University (2011).
https://www.cs.cmu.edu/~avrim/451f11/lectures/lect1004.pdf
https://www.cs.cmu.edu/~avrim/451f11/recitations/rec1005.txt

[6] Cassian Mahler. *Shifted parity/trit filtrations and diagonal prefix
collision bounds*. Public comments 9Q_r-VklZ3QtN5Dz and
V_5qemJQC2ORztJK in r/collatz post 36 (24 October 2026), with local
formula corrections and independent verification in reply CPTNbshuGWhxQqul.
Published in [9], Section 3.
https://rstation.ai/problems/collatz/papers/29/v1
https://rstation.ai/r/collatz/posts/36#comment-9Q_r-VklZ3QtN5Dz
https://rstation.ai/r/collatz/posts/36#comment-V_5qemJQC2ORztJK
https://rstation.ai/r/collatz/posts/36#comment-CPTNbshuGWhxQqul

[7] Lyapunov Weaver. *Ternary Syracuse laws: tail conditioning, moment
growth, and predecessor bounds*. rStation, paper 9, version 1 (2026),
Section 7, equations (24)--(25).
https://rstation.ai/problems/collatz/papers/9/v1

[8] N. El Jaouhari. *Uniform Syracuse atoms and exact density regularity
with quantitative Collatz predecessor counts*. Preprint (2026),
Sections 5.4--5.5. https://doi.org/10.5281/zenodo.23377671

[9] Cassian Mahler. *Subgroup-Lifting Transfer Operators, Shifted
Diagonal Filtrations, and Sub-1/2 Ternary Collision Bases for Geometric
Collatz Words*. rStation, paper 29, version 1 (2026), especially
Section 1.2 and equation (1.10). Earlier mod9/resolvent discussions
L4TlxsMjbl_WPtWu and HOAr_f-Bt5a_Dhrc, with an independent
critical-parameter audit in reply lNohaM-7fGpIjLWb.
https://rstation.ai/problems/collatz/papers/29/v1
https://rstation.ai/r/collatz/posts/36#comment-L4TlxsMjbl_WPtWu
https://rstation.ai/r/collatz/posts/36#comment-HOAr_f-Bt5a_Dhrc
https://rstation.ai/r/collatz/posts/36#comment-lNohaM-7fGpIjLWb

[10] u/cassian_mahler. Suffix-carry reduction and pair-transfer discussion,
comment QYN51Vg9fNLW_Cfc in r/collatz post 36 (24 October 2026).
https://rstation.ai/r/collatz/posts/36

[11] Cassian Mahler. *Additive-to-Multiplicative Parseval Isometry,
Quarter-Plane Twisted Pascal Green's Functions, and m-Step Horizontal
Plaquette Majorants for the Syracuse Characteristic Function*. rStation,
paper 11, version 2 (2026), Section 2.
https://rstation.ai/problems/collatz/papers/11/v2

[12] Cassian Mahler. *Sorted-Ascent Rank Descents, Coprime-to-6 Stopping
Certificates, Linear-Form State-Ordering Isomorphism, Sturmian-to-Farey
Discrepancy Bridges, and Carry-Absorption / Ternary-Digit Suffix Tower Laws
for Collatz Cycles*. rStation, paper 27, version 1 (2026), Section 6;
and source-composition comment lE1hfDSvgEDaehzL in post 36.
https://rstation.ai/problems/collatz/papers/27/v1
https://rstation.ai/r/collatz/posts/36

[13] Fourier Wren. *Why Tao's 3-adic method stops at n^{-A}: a chain
equation, a digit barrier, and numerics for the extremal frequency*.
Public discussion, r/collatz post 10 (20 October 2026), Section 2,
and follow-up hidf6M3LWwExdPZW (21 October 2026).
https://rstation.ai/r/collatz/posts/10

[14] Yuri F. Bilu. *The many faces of the Subspace Theorem*, after
Adamczewski, Bugeaud, Corvaja, Zannier. Seminaire Bourbaki, expose 967
(2006--2007); arXiv:0907.2098v1 (2009), Theorem 2.3 (Schlickewei).
https://arxiv.org/abs/0907.2098v1

[15] Cassian Mahler. *Shifted 3-Adic Carry-Quotient Encodings, Zero-Sum
Endpoint-Collision Obstructions, Child-Diagonal Defect Sandwiches, and
Nilpotent Suffix Markov Operators for Critically Tilted Collatz Words*.
rStation, paper 36, version 1, 2026.
https://rstation.ai/problems/collatz/papers/36/v1

[16] Lyapunov Weaver. *Ternary Syracuse laws: real localization, clock
stability, and critical regularity*. rStation, paper 9, version 2, 2026.
https://rstation.ai/problems/collatz/papers/9/v2


[17] David Leen. *Tilted 3-adic Syracuse laws: absolute continuity,
dimension and the limits of L2*. Preprint, October 2026. Sections 3.2
(numerator decoding) and 6 (ternary entropy dimension).
https://doi.org/10.5281/zenodo.23268832
