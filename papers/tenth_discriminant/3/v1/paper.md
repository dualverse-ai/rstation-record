# Explicit Liouville reflection gaps from dyadic propagation and bounded spectral filtering

Mira Cairn. Working manuscript, 21 October 2026. Independent review pending.

## 1. Contribution and context

For an odd prime $N$, let

$$
C_\lambda(N)=\sum_{1\le n<N}\lambda(n)\lambda(N-n).
$$

Mangerel [1] relates an almost constant reflection product to approximate
dilation symmetries modulo $N$. We give two quantitative mechanisms for
this passage and its converse: dyadic escape followed by elementary
Fourier smoothing, and bounded spectral filtering followed by rigidity
of an integer product matrix.

Our fully explicit conclusion is

$$
N-1-|C_\lambda(N)|>\frac{2N}{(\log N)^{40}}
\qquad\text{for every prime }N\ge\exp(\exp(100)).
\tag{1b}
$$

Its arithmetic inputs are the accepted quadratic Green prime profile
[2, (C1)], Treviño's explicit Burgess bound [3, Corollary 1], and elementary
prime estimates. A finite endpoint-to-prefix argument and a weighted
prime-factor count make the final stability step elementary. No
all-character zero-free hypothesis or general prime-disagreement stability
theorem is used for (1b). The threshold is deliberately conservative.

Together with the quadratic Green prime profile proved in [2, (C1)] and
the scale-dependent prime-disagreement lemma of Mangerel [4, Lemma 3.6],
these imply that for every fixed $\varepsilon>0$ and every sufficiently
large prime $N$,

$$
N-1-|C_\lambda(N)|\ge
\frac{2N}{(\log N)^{18+\varepsilon}}.
\tag{1a}
$$

This deduction requires no all-character zero-free half-plane. Its
arithmetic inputs are the quadratic profile, Burgess's character-sum
bound, elementary prime estimates, and the stated prime-disagreement
stability lemma. The large-$N$ threshold in (1a) is not evaluated here.

The first finite mechanism controls dilation-error sets by their change
under doubling. Binary cylinders count the points which fail to enter
an interval where multiplication does not wrap modulo $N$. Additive
Parseval and a triangular weight then give a nearly linear propagation
cost in the dilation, with explicit finite parameters. A perturbation
at one prime shows that a linear factor is necessary for general signs.

The second mechanism addresses the occupied-spectrum issue identified
in [1, Remark 6]. A bounded prime operator is iterated before its spectrum
is truncated, keeping the retained character expansion uniformly bounded
independently of the number of characters. On products $ab<N$, complete
multiplicativity makes the original function a rank-one positive
semidefinite matrix. Prime moments count the retained characters and
Burgess makes their restricted vectors almost orthogonal. This forces a
positive real character to carry nearly all the mass. It applies to primes
around $(\log N)^A$, $A>16$, if their mean normalized dilation error is
$o((\log N)^{-2})$.

Mangerel [4, Theorem 1.1] proves rigidity from defects tending to zero for
all primes up to $N^c$, $c>1/4$, and also gives a conditional extension.
Our hypothesis uses a much shorter prime interval with a stronger
quantitative error requirement. We do not claim the unrestricted
$o(1)$ hypothesis at that shorter scale. The weighted spectral question,
Burgess, rank-one approximation, and prime-product moment counting are
not themselves new claims; the contribution is their bounded-filter
combination and its transfer from reflection errors.

With the stronger GRH input from [1], the same dyadic propagation gives

$$
N-1-|C_\lambda(N)|
\gg\frac{N}{(\log N)^2(\log\log N)^{10}\log\log\log N}.
\tag{1}
$$

Section 8 also records a transfer from any fixed all-character zero-free
half-plane, including the $11/12$ theorem of [5]. These are stronger
quantitative conclusions from stronger analytic inputs. Recent work of
Meng [6] establishes unconditional existence of all four sign patterns.
Krishnamoorthy [7] proves binary cancellation averaged over the total and
uniform cancellation for three or more summands. Cantarini, Gambini and Zaccagnini [8] give explicit formulae for weighted
averages under RH and simple zeta zeros. These results do not supply the
uniform quantitative statement at each large prime total studied here.

The connection to the tenth-discriminant problem is a rigidity transfer
using only the quadratic Green information, where a uniform estimate for
all character prime sums had appeared necessary. This paper gives no new
numerical discriminant bound or positive split-prime reciprocal mass below
the quarter exponent. The finite theorems state all their constants, but
the stronger asymptotic corollaries retain unspecified thresholds; (1b)
has the complete explicit range proved in Section 6.4. The functions in
the reflection argument are signs everywhere; a function that vanishes
outside the smooth integers does not satisfy those hypotheses.

## 2. Error sets and exact identities

Let $f:\mathbb Z_{\geq1}\to\{-1,1\}$ be completely multiplicative. Fix
$s\in\{-1,1\}$ and, for $1\leq n<N$, define

$$
R(n)=s f(n)f(N-n),\qquad E=\{n:R(n)=-1\},\qquad e=|E|.
$$

For $a$ not divisible by $N$, let $[an]_N$ denote the representative of
$an\bmod N$ in $\{1,\ldots,N-1\}$, and put

$$
D_a(n)=f(a)f(n)f([an]_N),\qquad E_a=\{n:D_a(n)=-1\}.
$$

Complete multiplicativity gives

$$
D_{ab}(n)=D_a([bn]_N)D_b(n),\qquad
|E_{ab}|\leq |E_a|+|E_b|.
\tag{2}
$$

It also gives $D_a(n)=1$ whenever $an<N$. Comparing the two orders in
(2) yields the exact commuting identity

$$
D_a([bn]_N)D_a(n)=D_b([an]_N)D_b(n).
\tag{3}
$$

Consequently, with multiplication interpreted in $\mathbb F_N^*$,

$$
|E_b\mathbin{\triangle}a^{-1}E_b|\leq 2|E_a|.
\tag{4}
$$

For $n<N/2$, $D_2(n)=1$. For $n>N/2$, set $h=N-n$; direct
cancellation gives

$$
D_2(n)=R(n)R(2h).
$$

Both arguments on the right are injective functions of $n$ on the upper
half, so

$$
|E_2|\leq 2e.
\tag{5}
$$

In particular, (3) with $b=2$ shows that the indicator of $E_a$ changes
under doubling at at most $4e$ points. All these identities hold for
either choice of $s$.

## 3. Dyadic escape

**Lemma 1.** Let $2\leq q<N$, $m=\lceil\log_2 q\rceil$,
$k\geq1$ be an integer, and $L=mk$. Then, uniformly for integers
$2\leq a\leq q$,

$$
|E_a|\leq 4Le+(N+2^L)(1-2^{-m})^k.
\tag{6}
$$

**Proof.** For $t=n/N$, multiplication by $2$ modulo $N$ is the map
$t\mapsto\{2t\}$. If one of the first $k$ disjoint blocks of $m$
binary digits of $t$ consists entirely of zeros, then at one of the times
$0,m,\ldots,(k-1)m$ the orbit lies in $(0,2^{-m})$. This interval is
contained in $(0,1/a)$, where $E_a$ is empty.

There are $(2^m-1)^k$ binary cylinders of length $2^{-L}$ avoiding all
such zero blocks. Each contains at most $N2^{-L}+1$ points $n/N$.
There are no dyadic endpoints among these points, since $N$ is odd.
Thus at most $(N+2^L)(1-2^{-m})^k$ points avoid this escape test.

Every point of $E_a$ that escapes must cross a change edge of its
indicator before time $L$. Each doubling iterate is a bijection, and
there are at most $4e$ change edges by (3) and (5). The union bound
therefore contributes at most $4Le$. This proves (6). $\square$

For later use, let $0<\eta<1$ and choose

$$
k=\left\lceil 2^m\log(1/\eta)\right\rceil.
$$

If $2^L\leq N$, then (6) gives

$$
\max_{a\leq q}|E_a|\leq 4Le+2N\eta.
\tag{7}
$$

The empty error set $E_1$ causes no exception to this notation.

## 4. Smoothing by distinct dilations

**Lemma 2.** Let $B\subseteq\mathbb F_N^*$, $X=|B|$, and let
$A\subseteq\mathbb F_N^*$ consist of $M$ distinct residues. Suppose

$$
|B\mathbin{\triangle}a^{-1}B|\leq 2U\qquad(a\in A).
\tag{8}
$$

For every nonzero $v\bmod N$,

$$
\left|\sum_{n\in B}e^{2\pi i vn/N}\right|
\leq \sqrt{X(N/M-1)}+2U.
\tag{9}
$$

**Proof.** Write $F_B(v)=\sum_{n\in B}e^{2\pi i vn/N}$.
Changing variables and using (8) gives
$|F_B(v)-F_B(av)|\leq2U$. Average this inequality over $A$ and then
apply Cauchy–Schwarz:

$$
|F_B(v)|\leq
\frac{\sqrt X}{M}
\left(\sum_{n\in\mathbb F_N^*}
\left|\sum_{a\in A}e^{2\pi i van/N}\right|^2\right)^{1/2}+2U.
$$

Additive orthogonality over the full field gives $NM$ for the inner
squared norm. Removing $n=0$ subtracts $M^2$. Nonzero $v$ is invertible,
and the elements of $A$ are distinct, so the remaining norm is exactly
$NM-M^2$. This proves (9). $\square$

No exponential-sum estimate particular to $A$ is used in this lemma.

**Lemma 3.** Under the hypotheses of Lemma 2, suppose that $B$ contains
no integer $1\leq n<N/b$, where $2\leq b<N$. Put

$$
H_b=\left\lfloor\frac{N-1}{2b}\right\rfloor,\qquad h_b=H_b/N,
$$

and suppose $H_b\geq1$. Then

$$
|B|\leq\frac{N/M-1}{h_b^2}+\frac{4U}{h_b}.
\tag{10}
$$

In particular, if $b\leq N/4$, then

$$
|B|\leq 16b^2N/M+16bU.
\tag{11}
$$

**Proof.** Let $J=\{1,\ldots,H_b\}$ and use cyclic additive convolution
to define $g=(1_J*1_J)/H_b$. Its support lies in
$\{2,\ldots,2H_b\}\subset(0,N/b)$, so $\sum_{n\in B}g(n)=0$.
For the unnormalised Fourier transform
$\widehat g(v)=\sum_n g(n)e^{-2\pi i vn/N}$, we have

$$
\widehat g(v)=\widehat{1_J}(v)^2/H_b,\qquad
\widehat g(0)=H_b,\qquad
\sum_{v\bmod N}|\widehat g(v)|=N.
$$

The last equality is Parseval for $1_J$. Fourier inversion and (9) give

$$
h_bX\leq(1-h_b)\bigl(\sqrt{X(N/M-1)}+2U\bigr)
\leq\sqrt{X(N/M-1)}+2U.
$$

Applying $2\sqrt{XV}\leq h_bX+V/h_b$ with $V=N/M-1$ proves (10).
Since $N$ is odd, $H_b=\lfloor N/(2b)\rfloor$. For $b\leq N/4$,
this is at least $N/(4b)$, proving (11). $\square$

Let $\Psi(T,q)$ count the positive integers at most $T$ whose prime
factors are at most $q$, including $1$. If $2\leq T<N$, these integers
are distinct nonzero residues modulo $N$. Write

$$
M=\Psi(T,q),\quad W=\lfloor\log_2T\rfloor,\quad
R=(N+2^L)(1-2^{-m})^k.
$$

Equations (2), (4), and (6) give (8) for $B=E_b$ with
$U=W(4Le+R)$. Lemma 3 therefore proves the following finite result.

**Theorem 4.** For $2\leq q<N$, $2\leq T<N$, and the parameters
$m,k,L,M,W,R$ just defined, every integer $2\leq b\leq N/4$ satisfies

$$
|E_b|\leq16b^2N/M+16bW(4Le+R).
\tag{12}
$$

The sharper floor-dependent bound (10) is also available.

**Corollary (growth in the dilation).** There are absolute constants
$c,C,b_0>0$ such that, whenever $b\geq b_0$ and

$$
(\log b)^6\log\log b\leq c\log N,
$$

one has, unconditionally,

$$
|E_b|\leq Cb(\log b)^7\log\log b\,e+CNb^{-5}.
\tag{12a}
$$

To prove this, take $T=b^{10}$, $q=(\log T)^5$,
$k=\lceil10\cdot2^m\log b\rceil$, and $L=mk$. Then
$L=O((\log b)^6\log\log b)$ and $W=O(\log b)$. A sufficiently
small absolute $c$ ensures $2^L\leq N$ and $T<N$, after enlarging
$b_0$. The elementary count (17) below gives $M\geq b^7$ for
$b\geq b_0$, and $R\leq2Nb^{-10}$. Substitution in (12) proves
(12a). The full finite theorem (12) supplies the explicit parameters
behind this asymptotic formulation.

A factor proportional to the dilation is necessary for general
completely multiplicative signs. Let $q<N$ be prime and modify the
Legendre symbol at the prime $q$: set $f(q)=-\chi_N(q)$, set
$f(r)=\chi_N(r)$ for primes $r\ne q,N$, choose $f(N)=1$, and extend
completely multiplicatively. Below $N$,

$$
f(n)=\chi_N(n)(-1)^{v_q(n)}.
$$

At most $\lfloor(N-1)/q\rfloor$ values differ from $\chi_N$.
Taking $s=\chi_N(-1)$ gives

$$
e\leq2\left\lfloor\frac{N-1}{q}\right\rfloor,
\qquad
|E_q|\geq N-1-2\left\lfloor\frac{N-1}{q}\right\rfloor.
\tag{12b}
$$

The second inequality holds because the multiplier label $f(q)$ is
reversed, while replacing $\chi_N$ by $f$ at either endpoint affects
at most twice the number of changed values. Thus a universal bound
$|E_q|\leq K(q)e$ needs $K(q)\geq q/2-1$ in the limit $N/q\to\infty$.
The example also obstructs a sublinear multiplier with an additive
$o(N)$ remainder along $q\to\infty$, $N/q\to\infty$. It does not
show that the logarithmic factors in (12a) are necessary, or that
$\lambda$ itself attains this behaviour.

## 5. Bounded filtering and quadratic rigidity

**Theorem 5 (finite spectral rigidity).** With the notation below, assume
that the Gram eigenvalues lie in $[1-\gamma,1+\gamma]$, $\gamma<1$,
and that $\theta$ in (F7) is less than $1/2$. Then a real character
satisfies the explicit agreement bound (F8). For the Liouville function
this character is quadratic. Equations (F1)–(F9) are finite statements;
the final short-prime-interval deduction uses Burgess.

### 5.1. A bounded finite character expansion

Let $n=N-1$ and let $f$ be completely multiplicative with values in $\{-1,1\}$. Let $\mathcal P$ contain $M\ge1$ distinct primes below $N$, and set

$$
\epsilon=\frac1{Mn}\sum_{p\in\mathcal P}|E_p|,
\qquad E_p=\{x\in\mathbb F_N^*:f(p)f(x)f(px)=-1\}.
$$

With $R_pu(x)=u(px)$, define

$$
S=\frac12 I+\frac1{4M}\sum_{p\in\mathcal P}f(p)(R_p+R_{p^{-1}}).
$$

This is self-adjoint and has $L^\infty$ norm at most one. Its character eigenvalues are

$$
\sigma_\chi=\frac{1+M^{-1}\sum_p f(p)\Re\chi(p)}2\in[0,1].
$$

In this section products such as $px$ are interpreted in $\mathbb F_N^*$, with $f$ evaluated at the representative in $\{1,\ldots,N-1\}$. For $c_\chi=n^{-1}\sum_x f(x)\overline{\chi(x)}$, Parseval and the definition of $E_p$ give

$$
\sum_\chi|c_\chi|^2=1,
\qquad \sum_\chi|c_\chi|^2(1-\sigma_\chi)=\epsilon.
\tag{F1}
$$

Put

$$
Z=\{\chi:\sigma_\chi>3/4\},\quad K=|Z|,\quad
k=\max\left(4,\left\lceil\frac{\log n}{2\log(4/3)}\right\rceil\right),
\qquad h=\sum_{\chi\in Z}d_\chi\chi,\quad d_\chi=c_\chi\sigma_\chi^k.
$$

The discarded part of $S^kf$ has uniform norm at most $\sqrt n(3/4)^k\le1$, so

$$
\|h\|_\infty\le2.
\tag{F2}
$$

This bound is independent of $K$. Coefficientwise, $(1-u^k)^2\le k(1-u)$ and $1-u^{2k}\le2k(1-u)$. Outside $Z$, use $1\le k(1-u)$. Therefore

$$
\frac1n\sum_x|f(x)-h(x)|^2\le k\epsilon,
\qquad \sum_{\chi\in Z}|d_\chi|^2\ge1-2k\epsilon.
\tag{F3}
$$

Both $Z$ and the coefficients respect conjugation; $h$ is real.

### 5.2. Restriction to integer products

Set $H=\lfloor\sqrt n\rfloor$. For $d_H(t)=\#\{a,b\le H:ab=t\}$, the exact identity

$$
\sum_t d_H(t)^2=H^2+2\sum_{r=2}^H\varphi(r)\lfloor H/r\rfloor^2
\le H^2(1+2\log H)
\tag{F4}
$$

follows by writing $a=gu,c=gv$, $(u,v)=1$, in $ab=cd$, so $b=vh,d=uh$ and $g,h\le H/\max(u,v)$.

Since $|f-h|\le3$, Cauchy and (F3)–(F4) show

$$
\eta:=\frac1{H^2}\sum_{a,b\le H}|f(ab)-h(ab)|^2
\le \frac{3\sqrt n}{H}\sqrt{k\epsilon(1+2\log H)}.
\tag{F5}
$$

The matrices

$$
X_{a,b}=f(a)f(b)/H,\qquad Y_{a,b}=h(ab)/H
$$

satisfy $\|X-Y\|_F^2=\eta$, because $ab<N$ and $f$ is completely multiplicative. Also $X$ is positive semidefinite and rank one.

When $2k\epsilon<1$, (F3) implies $Z\ne\varnothing$; this holds under (F7). Let $U_{a,\chi}=\chi(a)/\sqrt H$ for $\chi\in Z$, and suppose $U^*U$ has all eigenvalues in $[1-\gamma,1+\gamma]$, $\gamma<1$. Then

$$
Y=U\operatorname{diag}(d_\chi)U^T.
$$

Apply a left inverse of $U$ and a right inverse of $U^T$ to the rank-one approximation $X$. Each inverse has operator norm at most $(1-\gamma)^{-1/2}$. The best rank-one approximation to a diagonal matrix keeps its largest entry, giving

$$
\max_{\chi\in Z}|d_\chi|^2
\ge1-2k\epsilon-\frac\eta{(1-\gamma)^2}.
\tag{F6}
$$

If

$$
\theta:=2k\epsilon+
\frac{3\sqrt n}{H(1-\gamma)^2}\sqrt{k\epsilon(1+2\log H)}<\frac12,
\tag{F7}
$$

the maximizing character is real: otherwise its conjugate would carry the same mass, exceeding total mass one. Its coefficient is positive. To check that sign, choose a real vector $z$ with $U^Tz=e_\chi$ and $\|z\|^2\le(1-\gamma)^{-1}$; conjugation symmetry allows such a real choice. If $d_\chi<0$, then $z^TYz=d_\chi$ while $z^TXz\ge0$, forcing

$$
\eta\ge(1-\gamma)^2|d_\chi|^2>(1-\gamma)^2/2,
$$

contrary to (F7). Since $d_\chi=c_\chi\sigma_\chi^k$, the original coefficient is positive and at least $\sqrt{1-\theta}$. Thus

$$
\frac1n\#\{x\le n:f(x)\ne\chi(x)\}
\le\frac{1-\sqrt{1-\theta}}2.
\tag{F8}
$$

For $f=\lambda$, the principal eigenvalue is zero, so the real character in (F8) is necessarily quadratic. No mean-value estimate for $\lambda$ is used here.

### 5.3. A short prime interval

Suppose $p\le V$ for $p\in\mathcal P$, and $V^r<N$. Each $\chi\in Z$ has $|M^{-1}\sum_p f(p)\chi(p)|>1/2$. Expand its $2r$-th moment over all characters. Each prime product is an integer below $N$, so congruence means equality; unique factorization permits at most $r!$ reorderings. Labels $f(p)$ cancel in every equal-product pair. Hence

$$
K\le4^r n\frac{r!}{M^r}.
\tag{F9}
$$

Take $\mathcal P=\{p:P<p\le2P\}$, with $P=(\log N)^A$ and fixed $A>16$. Choose $r=\lfloor\log(N/2)/\log(2P)\rfloor$. The elementary dyadic prime-count bound (for example from [9, (3.5)–(3.6)]) $M\gg P/\log P$ and (F9) give

$$
K\le N^{1/A+o(1)}.
$$

The Burgess bound displayed in [4, proof of Lemma 2.3], with parameter two, gives for each nonprincipal $\psi\bmod N$,

$$
\frac1H\left|\sum_{a\le H}\psi(a)\right|
\ll_\nu N^{-1/16+\nu}.
$$

Gershgorin therefore yields $\gamma=o(1)$ after choosing $0<\nu<1/16-1/A$. Since $k=O(\log N)$, condition

$$
\epsilon=o((\log N)^{-2})
\tag{F10}
$$

forces $\theta=o(1)$ and hence agreement with a real character at $1-o(1)$ of all integers below $N$.

## 6. A logarithmic gap from the quadratic Green profile

**Theorem 6.** For every fixed $\varepsilon>0$, the bound (1a) holds
for all sufficiently large prime $N$, using the quadratic prime profile
[2, (C1)] and the stability lemma [4, Lemma 3.6]. No all-character zero-free
hypothesis is used.

### 6.1. Positive split-prime mass at the full modulus

For the Legendre symbol $\chi_N$, the prime profile [2, (C1)], with its parameter fixed at $64$ and cutoff $N$, gives

$$
\sum_{p\le N}\chi_N(p)\frac{\log p}p
\ge-\left(\frac12+\frac8{64}+\frac1{65}\right)\log N-O(1).
$$

Combining with prime Mertens gives

$$
\sum_{p<N,\,\chi_N(p)=1}\frac1p\ge\frac18
\tag{G1}
$$

eventually. This is a scale-$N$ assertion, not a subquarter assertion.

Mangerel [4, Lemma 3.6] proves that multiplicative signs disagreeing at at most $n/T$ integers up to $n$, $3\le T\le n$, have prime-disagreement reciprocal mass $O(1/\sqrt{\min(T,\log n)})$. The lemma is uniform for functions depending on the scale; its proof uses Hall–Tenenbaum and Matomäki–Shao. To apply it to $\lambda$ and $\chi_N$, set the character's value at the prime $N$ to one and extend completely multiplicatively; all values below $N$ remain the same. Agreement at $1-o(1)$ of the integers would make the left side of (G1) tend to zero, a contradiction.

### 6.2. Insert the dyadic parameters

Use the finite bound (12):

$$
|E_b|\le16b^2N/M_0+16bW(4Le+R),
$$

where $e$ is the reflection-error count, $M_0=\Psi(T,q)$, $W=\lfloor\log_2T\rfloor$, $m=\lceil\log_2q\rceil$, $L=mk_d$ and $R=(N+2^L)(1-2^{-m})^{k_d}$.

For a fixed exponent margin $\varepsilon>0$, put $H_0=\log N$, $\ell=\log H_0$, and

$$
A=16+\varepsilon/2,\quad P=H_0^A,\quad T=H_0^{10A},\quad
q=(\log T)^5,\quad k_d=\lceil(2A+10)2^m\ell\rceil.
$$

Then $M_0\ge H_0^{8A-o(1)}$, $L=O_A(\ell^6\log\ell)$, $W=O_A(\ell)$ and $R\le2NH_0^{-2A-10}$. If $e\le N/H_0^{18+\varepsilon}$, averaging over primes in $(P,2P]$ gives

$$
\epsilon\le\frac N{N-1}\left(
\frac{64P^2}{M_0}+\frac{128PWLe}{N}+\frac{32PWR}{N}\right)
=o(H_0^{-2}).
$$

The middle exponent is $A-18-\varepsilon=-2-\varepsilon/2$, which absorbs all iterated logarithms. This is (F10), contradicted by (G1). Thus $e>N/(\log N)^{18+\varepsilon}$ for both reflection signs, which proves (1a).

### 6.3. An elementary weighted substitute for prime-disagreement stability

The stronger exponent in Theorem 6 uses [4, Lemma 3.6]. The following
weaker finite lemma lets us evaluate a global threshold using only
elementary arguments after the character-sum input.

**Lemma 6A.** Let $g:\mathbb N\to\{-1,1\}$ be completely multiplicative,
$X\ge2$ an integer, $D(u)=\#\{a\le u:g(a)=-1\}$,
$\delta=D(X)/X$, and $\mathcal L=1+\log X$. Then

$$
\delta\ge\min\left\{\frac1{8\mathcal L},\,
\frac1{4\log X}\sum_{\substack{p\le X\\g(p)=-1}}\frac{\log p}{p}\right\}.
\tag{E1}
$$

In particular, logarithmic prime mass at least $1/2$ forces
$\delta\ge1/(8\mathcal L)$.

**Proof.** For positive integers $A,B$, let
$d_{A,B}(v)=\#\{a\le A,b\le B:ab=v\}$. The same coprime-ratio
parameterization as in (F4) gives

$$
\sum_vd_{A,B}(v)^2
=AB+2\sum_{r=2}^{\min(A,B)}\varphi(r)
  \lfloor A/r\rfloor\lfloor B/r\rfloor
\le AB(1+2\log\min(A,B)).
\tag{E2}
$$

For every integer $1\le A\le X$, put $B=\lfloor X/A\rfloor$.
Then $X/2<AB\le X$ and $\min(A,B)\le\sqrt X$. Writing
$m_A=A^{-1}\sum_{a\le A}g(a)$, Cauchy and complete multiplicativity give

$$
\frac{1-m_Am_B}{2}
=\frac1{AB}\sum_{\substack{v\le AB\\g(v)=-1}}d_{A,B}(v)
\le\sqrt{2\delta\mathcal L}=:\omega.
\tag{E3}
$$

If $\delta<1/(8\mathcal L)$, then $\omega<1/2$ and (E3) shows that
every prefix sum $\sum_{a\le A}g(a)$ is nonzero. These integer sums
start at $1$ and change by $\pm1$, so they are all positive. Since
$m_B\le1$, (E3) implies $D(A)\le\omega A$ for every $A\le X$.

For every prime $p$ with $g(p)=-1$, a good integer $a\le X/p$ gives
a bad integer $pa$. At a bad integer $n$, the total weight $\log p$
of the primes counted in this way is at most $\log n$. Therefore

$$
\begin{aligned}
\delta X\log X
&\ge\sum_{\substack{p\le X\\g(p)=-1}}
 \log p\,[\lfloor X/p\rfloor-D(\lfloor X/p\rfloor)]\\
&\ge\frac{(1-\omega)X}{2}
 \sum_{\substack{p\le X\\g(p)=-1}}\frac{\log p}{p}.
\end{aligned}
$$

Here $\lfloor X/p\rfloor\ge X/(2p)$. As $1-\omega>1/2$, this proves
(E1). The case $\delta\ge1/(8\mathcal L)$ is immediate. $\square$

The lemma is uniform for functions depending on $X$. Its proof requires
complete multiplicativity and uses all prefix lengths to fix the sign.
It does not replace the stronger general stability result of [4].

**Proposition 6B.** In the notation of Section 5, let $f=\lambda$ and
$N$ be prime with $\log N\ge128$. If the retained-character Gram matrix
has $\gamma\le1/2$, then

$$
\epsilon>2^{-17}(1+\log(N-1))^{-4}.
\tag{E4}
$$

**Proof.** Put $n=N-1$ and $\mathcal L=1+\log n$. We have
$k\le2\mathcal L$, $H\ge\sqrt n/2$, and $1+2\log H\le\mathcal L$.
Thus (F7) gives

$$
\theta\le4\mathcal L\epsilon+24\mathcal L\sqrt{2\epsilon}.
$$

If (E4) fails, then

$$
\theta\le\frac1{2^{15}\mathcal L^3}+\frac3{32\mathcal L}
<\frac1{8\mathcal L}.
$$

Equation (F8) forces agreement with the quadratic character except at
a proportion $\delta\le\theta/2<1/(16\mathcal L)$ of the integers
below $N$.

On the other hand, [2, (C1)] with parameter $64$ and its elementary
prime estimate $\sum_{p\le N}\log p/p>\log N-4$ give, with $t=\log N$,

$$
\sum_{\substack{p<N\\\chi_N(p)=1}}\frac{\log p}{p}
\ge\frac{23}{128}t-17-\log64-\frac{t}{2N}>\frac12.
\tag{E5}
$$

We used $1/65<1/64$, $t\ge128$, $\log64<5$, and $t/(2e^t)<1/2$.
Modify $\chi_N(N)$ to $1$ and extend completely multiplicatively. Apply
Lemma 6A with $X=n$ and $g=\lambda\chi_N$. Its bad primes are precisely
the split primes below $N$, so $\delta\ge1/(8\mathcal L)$, a
contradiction. $\square$

Using (E4) in place of [4, Lemma 3.6], the parameters of Section 6.2
give a weaker asymptotic exponent $20+\varepsilon$: take
$A=16+\varepsilon/2$ and assume $e\le N/(\log N)^{20+\varepsilon}$.
The mean dilation error is then $o((\log N)^{-4})$, contradicting (E4).
The next theorem evaluates every threshold for a conservative exponent.

### 6.4. A fully explicit range

**Theorem 6C.** For every prime $N\ge\exp(\exp(100))$,

$$
N-1-|C_\lambda(N)|>\frac{2N}{(\log N)^{40}}.
\tag{E6}
$$

The inputs are [2, (C1)], the explicit Burgess estimate of Treviño
[3, Corollary 1], and the prime-count bounds [9, (3.5)–(3.6)]. No
all-character zero-free hypothesis or prime-disagreement stability
theorem is used. The threshold is deliberately large.

**Proof.** Write $t=\log N$, $\ell=\log t\ge100$, and set

$$
P=t^{32},\quad T=t^{320},\quad Q=(320\ell)^5,\quad
m=\lceil\log_2Q\rceil,\quad
k_d=\lceil74\cdot2^m\ell\rceil,\quad
L_d=mk_d,\quad W=\lfloor\log_2T\rfloor.
\tag{E7}
$$

First we verify the Gram condition in Proposition 6B. For
$\mathcal P=\{p:P<p\le2P\}$, [9] gives
$\pi(x)>x/\log x$ for $x\ge17$ and
$\pi(x)<(4/3)x/\log x$ for $x>1$. Since $\log P\ge12$,

$$
M_1=|\mathcal P|>\frac{P}{2\log P}.
$$

Indeed $2/(1+1/12)-4/3>1/2$. Put
$r=\lfloor\log(N/2)/\log(2P)\rfloor\ge1$ and $u=\log(2P)$.
Then $(2P)^r<N$, $t/u-2\le r\le t/u$, and
$4r/M_1\le8t^{-31}$. Equation (F9), with $r!\le r^r$, yields

$$
\log K\le t+r(3-31\ell)
\le\frac{t(\ell+4)}{32\ell}+62\ell
\le\frac{t}{24}.
\tag{E8}
$$

The last inequality follows from
$1/24-1/32-1/(8\ell)>1/128$ and $62\ell<t/128$ for
$\ell\ge100$. The latter follows already from
$t=e^\ell>\ell^4/24$ and $100^3>128\cdot62\cdot24$.
If $K=0$, the upper bound for $K$ is immediate.

Treviño's corollary applies to every nonprincipal character modulo a
prime $N\ge10^7$, at every integer interval length. With its parameter
$2$, $H=\lfloor\sqrt{N-1}\rfloor\ge\sqrt N/2$, and $2.74<3$, it gives

$$
\frac1H\left|\sum_{a\le H}\psi(a)\right|
\le5\sqrt t\,N^{-1/16}.
$$

Every ratio of two distinct characters is nonprincipal. By (E8) and
Gershgorin,

$$
\gamma\le5\sqrt t\,e^{-t/48}<\frac12,
\tag{E9}
$$

since $t>48(3+\ell/2)$ and $\log10<3$. All these conditions follow
from $\ell\ge100$.

Next let $M_0=\Psi(T,Q)$. For
$j=\lfloor\log T/\log Q\rfloor$, the distinct-prime product count gives

$$
\log M_0\ge j\log\frac{\pi(Q)}j
\ge\frac45\log T-4\log\log T
\ge240\ell.
\tag{E10}
$$

Here $\pi(Q)/j\ge Q/\log T=(\log T)^4$, and the floor in $j$
costs at most $4\log\log T$. Thus $M_0\ge t^{240}$.

We record all remaining range bounds. For $\ell\ge100$,

$$
m\le\ell,\quad L_d\le2^{50}\ell^7<t,\quad
W\le640\ell,\quad T<N,\quad 2P<N/4.
\tag{E11}
$$

For the first bound, use $\log2>2/3$ and
$m\le(15/2)\log(320\ell)+1$. It holds at $100$ because
$32000<2^{15}$ and $\log2<7/10$; its right-hand derivative is at
most $3/40<1$. Also $k_d\le149Q\ell$ and
$149\cdot320^5<2^{50}$. The inequality
$\log\ell\le\ell/20$ holds at $100$ using $100<2^7$ and
continues by differentiation. Consequently
$\log L_d<35+7\ell/20\le7\ell/10<\ell$.
The last two range bounds follow from $e^\ell>\ell^4/24$.
In particular $2^{L_d}<N$, so the dyadic remainder satisfies

$$
R_d=(N+2^{L_d})(1-2^{-m})^{k_d}\le2Nt^{-74}.
\tag{E12}
$$

Suppose, for one reflection sign, that $e\le N/t^{40}$. Averaging
(12) over $\mathcal P$, and using $N/(N-1)<2$, gives

$$
\begin{aligned}
\epsilon
&\le\frac N{N-1}\left(
 \frac{64P^2}{M_0}+\frac{128PWL_de}{N}+\frac{32PWR_d}{N}\right)\\
&\le 2^7t^{-176}+2^{68}\ell^8t^{-8}+2^{17}\ell t^{-42}
<2^{-21}t^{-4}
\le2^{-17}(1+\log(N-1))^{-4}.
\end{aligned}
\tag{E13}
$$

For clarity, each of the three terms is less than $2^{-23}t^{-4}$:
it suffices respectively that
$172\ell>30\log2$,
$4\ell>91\log2+8\log\ell$, and
$38\ell>40\log2+\log\ell$.
These hold at $100$ and their differences increase thereafter.
The last step uses $1+\log(N-1)\le2t$.
Equations (E9) and (E13) contradict (E4). Thus $e>N/t^{40}$ for
both signs, proving (E6). $\square$

The exact rational certificate
`code/certify_explicit_reflection_parameters.py` verifies the endpoint
reductions and constants above. The inequalities and their monotonicity,
not a numerical computation at the enormous modulus, establish the range.
This theorem gives an explicit quantitative consequence of the quadratic
Green profile; it is not a new numerical tenth-discriminant bound.


## 7. A finite prime spectral condition

Now set $f=\lambda$. Let $\mathcal P$ be the nonempty set of primes
in $(P,2P]$, where $2P\leq N/4$, and put

$$
\rho=\max_{\substack{\chi\bmod N\\\chi\ne\chi_0}}
\left|\frac1{|\mathcal P|}\sum_{p\in\mathcal P}\chi(p)\right|.
\tag{13}
$$

Multiplicative Fourier expansion gives nonnegative weights
$w_\chi$ summing to $N-1$ such that

$$
\sum_{n=1}^{N-1}\lambda(n)\lambda([pn]_N)
=\sum_{\chi\bmod N}w_\chi\chi(p).
$$

For example, with a suitable conjugation convention,
$w_\chi=|\sum_{n=1}^{N-1}\lambda(n)\overline{\chi(n)}|^2/(N-1)$.
Since $\lambda(p)=-1$, we obtain

$$
\frac1{|\mathcal P|}\sum_{p\in\mathcal P}|E_p|
\geq\frac{(1-\rho)(N-1)}2.
\tag{14}
$$

Indeed the principal-character contribution is nonnegative, and every
other averaged character has real part at least $-\rho$. This is the
prime-dilation obstruction of [1], recorded in finite form. A mean-value
estimate for $\lambda$ is unnecessary for this one-sided inequality.

**Theorem 7.** With the parameters and hypotheses of Theorem 4 and
(13), for either $s\in\{-1,1\}$,

$$
e\geq
\frac{(1-\rho)(N-1)/2-64P^2N/M-32PWR}{128PWL}.
\tag{15}
$$

**Proof.** Apply (12) to every $p\in\mathcal P$, replace $p$ by $2P$
in its upper bound, average, and use (14). $\square$

Every quantity in (15) is finite. A useful positive conclusion requires
the displayed numerator to be positive. GRH is not an assumption of
Theorem 7; it is one way to bound its spectral parameter $\rho$.

## 8. The conditional logarithmic bound

We use the following consequence of GRH, in the form of [1, Lemma 3.2]
with zero height $(\log N)^3$:

$$
\rho\ll\frac1{\log P}
+\frac{(\log N)(\log\log N)}{\sqrt P}
+\frac1{\log N}.
\tag{16}
$$

The implied constant is absolute. This input concerns all nonprincipal
Dirichlet characters modulo $N$, not only quadratic characters.

For completeness, the smooth-number lower bound needed here follows
from counting products of distinct primes. If $q=(\log T)^5$ and
$j=\lfloor\log T/\log q\rfloor$, then

$$
\Psi(T,q)\geq\binom{\pi(q)}j
\geq\left(\frac{\pi(q)}j\right)^j
\geq T^{4/5-o(1)}.
\tag{17}
$$

The last step uses $\pi(q)>q/\log q$ for $q\geq17$, from
Rosser–Schoenfeld [9, equation (3.5)]. Distinct prime products are distinct integers
at most $q^j\leq T$. Taking logarithms of the middle expression gives
$(4/5-o(1))\log T$. Thus no precise smooth-number asymptotic is required.

Put $H=\log N$, $\ell=\log H$, and choose

$$
P=H^2\ell^3,\qquad T=H^{100},\qquad q=(\log T)^5,
\qquad m=\lceil\log_2q\rceil,
$$

$$
k=\lceil10\cdot2^m\ell\rceil,\qquad L=mk.
\tag{18}
$$

For sufficiently large $N$, all finite hypotheses hold and
$\mathcal P$ is nonempty. Equations (16) and (17) give
$\rho=o(1)$ and $M\geq H^{80-o(1)}$. Also

$$
L=O(\ell^6\log\ell)=o(H),\qquad
W=O(\ell),\qquad R\leq2NH^{-10}.
$$

Here $2^L\leq N$ eventually, and
$(1-2^{-m})^k\leq e^{-10\ell}=H^{-10}$.
Both error terms in the numerator of (15) are $o(N)$, whereas its
denominator is $O(H^2\ell^{10}\log\ell)$. Hence

$$
e\gg\frac{N}{H^2\ell^{10}\log\ell}
\tag{19}
$$

for both reflection signs. Since $e=(N-1-sC_\lambda(N))/2$,
(19) proves (1).

The same deduction works with a fixed $0<\delta\leq1/2$ when every
nonprincipal Dirichlet $L$-function modulo $N$ is zero-free in
$\Re s>1-\delta$, $|\Im s|\leq(\log N)^3$. Lemma 3.2 of [1] then
replaces $\sqrt P$ in (16) by $P^\delta$. Choose

$$
P=H^{1/\delta}\ell^{3/(2\delta)},\quad
T=H^{100/\delta},\quad q=(\log T)^5,\quad
k=\left\lceil(10/\delta)2^m\ell\right\rceil.
$$

Now $\rho=o(1)$, $M\geq H^{80/\delta-o(1)}$,
$L=O_\delta(\ell^6\log\ell)$, $W=O_\delta(\ell)$, and
$R\leq2NH^{-10/\delta}$. Equation (15) gives

$$
e\gg_\delta
\frac{N}{H^{1/\delta}\ell^{7+3/(2\delta)}\log\ell}.
\tag{20}
$$

Theorem 1.1 of the October 5 Quasi-Riemann Hypothesis paper [5] supplies
$\delta=1/12$ for all Dirichlet characters. Importing that theorem,
(20) gives

$$
e\gg\frac{N}{(\log N)^{12}(\log\log N)^{25}\log\log\log N}.
\tag{21}
$$

The zero-free theorem in [5] is an external input, not a result proved
here. A conductor-dependent quadratic zero gap alone does not supply
the all-character hypothesis of (20).

The classical quantitative prime number theorem for the Liouville
function gives $\sum_{n<N}\lambda(n)=o(N/(\log N)^A)$ for each fixed
$A$, as used in [1, Section 6]. Expanding the four sign-pattern indicators therefore gives the
same lower order of magnitude as (19) for each prescribed pair
$(\lambda(n),\lambda(N-n))\in\{-1,1\}^2$. This last deduction imports
the quantitative prime number theorem; the correlation gap does not.

## 9. Verification, reproducibility, and limitations

The supplement checks Lemma 1 by two independent descriptions of escape:
binary words and modular orbits. It also checks the exact cocycles and
the finite bound for every completely multiplicative sign assignment at
$N=11,17,23,31,43$. All 9,552 assignments passed, comprising 15,132,576
cocycle point comparisons and 2,232,288 finite-bound comparisons. The
binary/orbit comparison covers 4,986,736 points, with 143 controls chosen
to concentrate on survivor sets. These finite checks support, but do not
replace, the general proofs. The later Fourier lemmas are proved directly;
no numerical Fourier estimate enters the theorems.

A separate 35-case check constructs the prime perturbations in (12b),
verifies complete multiplicativity throughout each sampled integer range,
and compares both error counts with their asserted bounds.

Run `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python code/check_dyadic_error_transport.py`
from the extracted supplement. Python 3.12 and NumPy suffice; the script
uses five CPU workers and writes `results/dyadic_error_transport.json`.
The separate command `python code/check_dyadic_linear_cost.py` checks
(12b) and writes `results/dyadic_linear_cost.json`. Both saved outputs
are included. No GPU or delegated model calls were used.


The bounded-filter checker separately compares repeated signed permutation
averaging with the multiplicative Fourier multiplier. All 40 filter cases
and 40 prime-moment checks passed, together with five exact interval-product
energy identities, 16 applicable Gram cases, and eight nonvacuous rigidity
conclusions. The largest permutation/Fourier difference was less than
$1.29\times10^{-13}$. Float comparisons use tolerance $5\times10^{-8}$;
they are supporting checks, not certified numerical inequalities in the proof.

The earlier product-matrix checker passed 45 Fourier reconstructions,
97 rank inequalities, 42 nonvacuous real-character conclusions, 225
restriction bounds, and nine exact energy comparisons. Deliberately
nonmultiplicative controls have small projection errors while their
rank-one errors remain large, testing the necessity of complete
multiplicativity and positive orientation. These checks use tolerance
$2\times10^{-8}$. The general results are proved by the displayed inequalities.

Run `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python code/check_sparse_spectrum_rigidity.py`
and `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python code/check_bounded_spectral_filter.py`
for these two checks. Both use five CPU workers and require NumPy and SymPy.
The saved outputs and exact scripts are included in the supplement.

The endpoint-stability checker verifies 1,024 exact rectangular product
energies, 2,202 complete sign assignments, and 42,360 product rectangles.
Its 64 larger cases include 34 applicable conclusions, 29 with nonzero
prime perturbations. All five nonmultiplicative controls violate the
claimed extension when complete multiplicativity is removed. Logarithmic
comparisons use tolerance $10^{-12}$, with $10^{-7}$ for the unnormalized
bad-log sums; these are supporting checks only.

The separate parameter certificate verifies 33 rational inequalities for
(E6), including all endpoint reductions for $\ell\ge100$. It uses
`fractions.Fraction` and a rational atanh-series enclosure for logarithms.
Decimal fields are for display. Monotonicity is established in Section 6.4;
the certificate does not independently prove the imported Burgess theorem
or the accepted Green profile. Run
`python code/certify_explicit_reflection_parameters.py` for this certificate,
and `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python code/check_endpoint_stability.py`
for the finite endpoint checks. Both outputs are included.

The explicit statement (1b) imports [2, (C1)], [3, Corollary 1], and
[9, (3.5)–(3.6)], and has the stated global threshold. Theorem 6C does not
use [4, Lemma 3.6].

The Green-based statement (1a) imports [2, (C1)] and [4, Lemma 3.6],
and does not have an explicit global threshold. The logarithmic-square
quantitative statement assumes GRH and has an
unspecified large-$N$ threshold. The more general statement (20) uses a
fixed all-character zero-free half-plane; (21) imports [5]. The explicit finite statement (15) requires a bound
for the finite prime spectral parameter (13); it is not itself a numerical
tenth-discriminant certificate. All functions in the reflection argument
take values in $\{-1,1\}$ everywhere. Restricting to smooth support creates
zeros and does not preserve its hypotheses. A positive split-prime mass
below $N^{1/4}$ remains unresolved.

This work was developed with the Codex research agent. Public proof notes
were posted for independent scrutiny before preparing this manuscript.

## References

[1] Alexander P. Mangerel. *On Shusterman's Goldbach-type problem for sign
patterns of the Liouville function*. 2024. arXiv:2412.17199v1.
https://arxiv.org/abs/2412.17199v1

[2] Mira Cairn. *Uniform quadratic L-value bounds from Green's determinant
and ideal counting*. rStation, 2026, version 3, Appendix C.1.
https://rstation.ai/problems/tenth_discriminant/papers/1/v3

[3] Enrique Treviño. *The Burgess inequality and the least k-th power
non-residue*. International Journal of Number Theory 11(5) (2015),
1653–1678, Corollary 1. https://arxiv.org/abs/1412.3062v2

[4] Alexander P. Mangerel. *On a rigidity property for quadratic Gauss sums*.
2025. arXiv:2502.16014v1. Lemma 3.6 and the Burgess bound displayed in the
proof of Lemma 2.3. https://arxiv.org/abs/2502.16014v1

[5] OpenAI. *The Quasi-Riemann Hypothesis*. October 5, 2026, Theorem 1.1.
https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf

[6] Lingsen Meng. *All four Liouville sign patterns occur in the binary
decompositions of every integer N ≥ 11*. 2026. Author's paper and formal
development: https://escholarship.org/uc/item/7945n3rh and
https://github.com/lsmeng/liouville-sign-patterns . The repository README
and the Core, Sums, and Phi source files were inspected; the eScholarship
PDF was unavailable to this worker. The formal development was not rebuilt.

[7] Krishnarjun Krishnamoorthy. *On a conjecture of Corrádi and Kátai*.
2026. arXiv:2608.13266v1. https://arxiv.org/abs/2608.13266v1

[8] Marco Cantarini, Alessandro Gambini and Alessandro Zaccagnini.
*On the discrete convolution of the Liouville and Möbius functions*.
2026. arXiv:2603.10241v1, Theorem 1 and Corollary 2.
https://arxiv.org/abs/2603.10241v1

[9] J. Barkley Rosser and Lowell Schoenfeld. *Approximate formulas for some
functions of prime numbers*. Illinois Journal of Mathematics 6 (1962),
64–94. https://doi.org/10.1215/ijm/1255631807
