# Logarithmic residue resolution for geometric Collatz words

## 1. Problem and contribution

Mary Rees studies the pushforward of independent geometric division
exponents through Collatz iteration and conjectures strong uniformity of
an associated dyadic digit sum at a resolution proportional to the number
of odd steps [1]. We prove unconditional estimates at a logarithmic
resolution, for every fixed geometric parameter. The canonical endpoint
has bounded normalized collision energy at one logarithmic scale and
relative pointwise uniformity at half that scale. We also bound the
energy of the raw digit sum and prove its pointwise uniformity at a
double-logarithmic bit scale.

For $\alpha<\log_3 2$, the known extension of Tao's primitive Fourier
estimate already gives stronger canonical projection bounds [2,3]. Our
all-parameter estimates include the critical parameter $\alpha=\log_3 2$
and larger parameters, where that estimate is unavailable. Section 7
states the comparison precisely.

The mechanism is a multiplicative collision count over the units modulo
a power of three. Such counting belongs to the universal-hashing
framework [4,5]. Its use here requires two additional steps: an exact
split of a Collatz word into an independent prefix and suffix, and a
collision bound valid for every suffix-dependent translation. Only the
actual suffix multiplier is approximated by uniform measure, with an
explicit error. This approximation is justified at logarithmic depth.
For canonical pointwise uniformity, Fourier inversion and the elementary
Ramanujan-sum identity control the worst common translation directly.

We use the shortcut Collatz map

$$
C(n)=\begin{cases}n/2,&n\equiv0\pmod2,\\(3n+1)/2,&n\equiv1\pmod2.
\end{cases}
$$

Fix $\alpha\in(0,1)$ and put $q=1-\alpha$. All exponents below are
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
the independent law $\nu_h$. Since $L$ is odd, multiplication by $L$
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

Subsequent mod9 and resolvent refinements by Mahler [9] improve the
critical prefix step ratio further, below $1/2$. His equation (1.10)
also identifies the stronger global asymptotic base furnished by the
earlier tilted-fibre method [7,8]. Section 5.3 includes that input and
its stronger projection consequences with explicit attribution. A global
bound with a prefactor does not imply the same bound on a one-step
energy ratio. We use neither the printed resolvent coefficients nor a
numerical crossover depth from [9]. All these prefix estimates retain
the short-multiplier-seed limitation described next.

The limitation of the proof has a specific source. The multiplier in
(13) depends on one suffix sum, with spread of order $\sqrt r$ for fixed
$\alpha$. Uniformity over its complete period $T_h$ is available in
Lemma 4 only at the short depth used above. Taking $h$ proportional to
$r$ would invalidate the small-error conclusion. Further information
in the actual suffix translation is discarded by convexity in Section 5.

These results control a probability law on exponent words. They do not
establish descent for an individual positive integer, a stronger
compression exponent, or the Collatz conjecture. A polynomial bound for
normalized collision energy at $p$ proportional to $r$ would be a
substantially stronger arithmetic input. At present (3)--(6a) provide
explicit unconditional estimates for slowly growing moduli.

## 8. Reproducibility and verification scope

All asymptotic estimates have analytic proofs above. The supplement
contains five finite audit programs and their saved reports. From its
root, run the following commands separately:

```sh
python experiments/rees_multiplicative_collision_audit.py --workers 5 --output multiplicative.json
python experiments/rees_canonical_collision_audit.py --workers 5 --output canonical.json
python experiments/rees_prefix_lift_audit.py --workers 5 --output prefix.json
python experiments/rees_canonical_pointwise_audit.py --workers 5 --output pointwise.json
python experiments/cassian_shifted_prefix_audit.py
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
