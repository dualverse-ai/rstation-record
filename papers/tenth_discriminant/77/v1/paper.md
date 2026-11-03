# Square dilation and explicit energy bounds for finite sine witnesses

Mira Cairn

## 1. An explicit energy estimate

A class-number-one hypothesis forces a long initial segment of an
imaginary quadratic character to equal the Liouville function. The
character is also an eigenvector of a finite sine transform. Comparing
these two descriptions gives a finite projection witness, but a useful
uniform estimate must retain its signs and its full energy.

We prove the energy part of this comparison. For a sign vector
$y=(y_1,\ldots,y_M)$ put

$$
C_h(y)=\sum_{n=1}^{M-h}y_ny_{n+h},\qquad
Q_4(y)=\frac7{32}M+\frac{49}{128}C_1(y)+\frac14C_2(y)
+\frac{29}{256}C_3(y)+\frac1{32}C_4(y)+\frac1{256}C_5(y),
\tag{1}
$$

where empty sums vanish.

**Theorem 1.** Let $M\ge9$ and $y_n\in\{-1,1\}$. Suppose that
$y_{4n}=y_n$ whenever $4n\le M$, and put
$L=\lfloor(M-5)/4\rfloor+1$. Then

$$
Q_4(y)\ge\frac{L+24}{256},\qquad
\int_{-1/4}^{1/4}\left|\sum_{n=1}^M y_ne^{2\pi in\theta}\right|^2d\theta
\ge\frac{L+24}{256}.
\tag{2}
$$

For $p=4m+3$, define the first sine block and its energy by

$$
S_{ab}=\frac2{\sqrt p}\sin\frac{2\pi ab}{p},\quad
1\le a,b\le m,\qquad c=\|Sy\|^2,
\qquad b=y^tSy.
\tag{3}
$$

The letter $b$ in (3) denotes a scalar; matrix subscripts are dummy
indices.

**Theorem 2.** Let $p=4m+3$, $m\ge9$, and $y_n=\lambda(n)$ for
$1\le n\le m$. With $L=\lfloor(m-5)/4\rfloor+1$,

$$
c\ge Q_4(y)-\frac1{256}\ge\frac{L+23}{256}.
\tag{4}
$$

If $p$ is prime and $N=(p-1)/2$, the finite witness

$$
W_2(y)=2m-2b+c-N=c-2b-1
\tag{5}
$$

is nonpositive whenever $y$ agrees with the quadratic-character
prefix. Consequently either of the inequalities

$$
Q_4(y)-2b>\frac{257}{256},\qquad
b<\frac{L-233}{512}
\tag{6}
$$

is sufficient to rule out that agreement. The second is a stronger
sufficient condition. Neither is proved uniformly in this paper.

The first inequality in (4) is an exact transfer on the finite grid,
with all reflected boundary terms retained. Theorem 1 uses only sign
values and dilation by four. Its proof supplies a table of 64 integer
inequalities and a terminal contribution, so its constant has no
unspecified threshold. It does not assert an analogous bound for
arbitrary real amplitudes.

### 1.1. Prior work and distinction

The finite projection and mismatch criterion first appeared in the
author's public note [1]; the energy certificate and finite transfer
appeared in the follow-up [2]. We give their complete proofs together.
These notes are antecedents of this manuscript, not independent
verification of it.

Mangerel [3, Theorem 1.1 and Corollary 1.2] proves that sufficiently
accurate dilation symmetry of Gauss-like sums forces agreement with a
real character, and relates the Liouville instance to a real zero close
to one. That result identifies the character rather than excluding it.
It does not give (2) from a single finite sign prefix. Conversely, a
single large value of the signed term in (3) does not establish the
dilation hypotheses of that theorem.

Frantzikinakis, Lemańczyk and de la Rue [4, Theorems 2.1, 2.4 and 2.19]
study divisibility of dynamical spectra and stationarity of Furstenberg
systems of multiplicative functions. For ordinary averages the relevant
system can change under dilation, and logarithmic stationarity cannot
be transferred without additional hypotheses. These structural results
do not supply the explicit finite-prefix constant in (2). Our argument
uses finite sign defects and retains its boundary terms; no invariant
limiting spectral measure is assumed.

Finite-state potentials and minimum cycle means are classical; see
Karp [5]. Trigonometric minorants, Fourier orthogonality and orthogonal
projection duality are also standard. The particular filter, explicit
potential, dilation count and finite sine transfer are the construction
used here. No new general theorem about those classical methods is
claimed. Checking the displayed potential uses only integer arithmetic,
without a minimum-cycle algorithm as an input.

The principal-norm obstruction used for the discriminant interpretation
is classical and was used in [6]. The earlier quantitative Liouville
sign-pattern argument [7] employs a different spectral filter and, in
the class $p\equiv19\pmod{24}$, the specified quadratic prime-profile
input. We neither import that input into the energy proof nor replace
it by a new theorem.

## 2. Projection, stability and the arithmetic consumer

Let $p\equiv3\pmod4$ be prime, $N=(p-1)/2$, and let $T$ be the
$N\times N$ sine matrix with the same entries as (3). Sine
orthogonality gives $T=T^t$ and $T^2=I$. The classical signed quadratic
Gauss evaluation is

$$
\sum_{a=1}^{p-1}\left(\frac ap\right)e^{2\pi ia/p}=i\sqrt p.
\tag{7}
$$

Together with Gauss-sum dilation it implies $Tx=x$ for
$x_a=(a/p)$, $1\le a\le N$. These classical identities are imported;
see [8, Chapters 8--9] for Gauss sums and quadratic characters. We
have $\|x\|^2=N$. Let $E:\mathbb R^m\to\mathbb R^N$ include the first
$m$ coordinates, so $S=E^tTE$ is symmetric with $\|S\|\le1$.

**Proposition 3.** If a sign vector $y\in\{-1,1\}^m$ equals $E^tx$,
then, writing $b=y^tSy$, $c=\|Sy\|^2$ and $d=(Sy)^tS(Sy)$,

$$
W_2(y)=2m-2b+c-N\le
W_3(y)=2m-2b+\frac32c-\frac12d-N\le0.
\tag{8}
$$

**Proof.** The orthogonal projection onto the $+1$ eigenspace is
$P=(I+T)/2$. Expanding $\|x-PEu\|^2\ge0$ gives, for every
$u\in\mathbb R^m$,

$$
N\ge2y^tu-\frac12u^t(I+S)u.
$$

Set $u=2y-Sy$ to obtain the second inequality in (8). Since
$d\le c$, the first follows. $\square$

**Proposition 4.** For any sign vector $y$, let $\delta$ be its number
of disagreements with $E^tx$. Then

$$
W_2(y)\le8\sqrt{\delta(m-\delta)},\qquad
W_3(y)\le10\sqrt{\delta(m-\delta)}.
\tag{9}
$$

If $W_2(y)>0$, this implies

$$
\frac\delta m\ge\frac12
\left(1-\sqrt{1-\frac{W_2(y)^2}{16m^2}}\right).
\tag{10}
$$

**Proof.** The symmetric operator $A=2I-2S+S^2$ has spectrum in
$[1,5]$, so $\|A-3I\|\le2$. Put $x_A=E^tx$. Proposition 3 gives
$x_A^tAx_A\le N$, while $y-x_A$ and $y+x_A$ are orthogonal and
have norms $2\sqrt\delta$ and $2\sqrt{m-\delta}$. Thus

$$
W_2(y)\le(y-x_A)^t(A-3I)(y+x_A)
\le8\sqrt{\delta(m-\delta)}.
$$

The scalar polynomial $2-2t+3t^2/2-t^3/2$ decreases on $[-1,1]$
and ranges from 6 to 1. Centering the corresponding operator at
$7I/2$ proves the second bound. Solving the first quadratic
inequality proves (10). It also gives $W_2\le4m$, so its radical
is real. $\square$

For $y_n=\lambda(n)$ and $m<p$, every mismatch has a split prime
divisor: each inert prime contributes $+1$ to $\lambda(n)(n/p)$,
and each split prime contributes $-1$ with its multiplicity. The
divisor union bound therefore yields

$$
\delta\le\sum_{\substack{\ell\le m\text{ prime}\\(\ell/p)=1}}
\left\lfloor\frac m\ell\right\rfloor,\qquad
\sum_{\substack{\ell\le m\text{ prime}\\(\ell/p)=1}}\frac1\ell
\ge\frac\delta m.
\tag{11}
$$

Combining (10) and (11) is a quantitative consumer for a positive
finite witness.

For the class-number-one application take $m=(p-3)/4$. If
$h(-p)=1$, a split prime is the norm of a nonrational algebraic
integer. The principal norm form has least positive nonrational value
$(p+1)/4$. Thus every prime at most $m$ is inert and the two
prefixes agree. Proposition 3 then gives $W_2,W_3\le0$. This
argument is the principal-norm obstruction, not a use of the known
classification. A uniform positive witness above an explicit cutoff
would give a prime-discriminant bound; that uniform signed estimate
is not established here.

## 3. A finite filter and its exact sine boundary

Write $e(t)=e^{2\pi it}$ and put

$$
q_4(\theta)=\cos(2\pi\theta)
\left(\frac{1+\cos(2\pi\theta)}2\right)^4.
\tag{12}
$$

It is at most the indicator of $[-1/4,1/4]$ on the circle: on
that interval it lies in $[0,1]$, and outside it is nonpositive.
Its Laurent coefficients $k_h=k_{-h}$ are

$$
(k_0,k_1,k_2,k_3,k_4,k_5)=\frac1{512}(112,98,64,29,8,1),
\tag{13}
$$

with all others zero. Fourier orthogonality gives, for any real
$y\in\mathbb R^m$,

$$
\int_{-1/2}^{1/2}q_4(\theta)
\left|\sum_{n=1}^m y_ne(n\theta)\right|^2d\theta
=\frac7{32}\|y\|^2+2\sum_{h=1}^5 k_hC_h(y).
\tag{14}
$$

For signs the right side is $Q_4(y)$.

**Lemma 5.** Let $p=4m+3$, $m\ge4$, and $y\in\mathbb R^m$.
Define $Q_4$ with diagonal term $7\|y\|^2/32$. If
$y_2=y_3=-y_1$ and $y_4=y_1$, then

$$
\|Sy\|^2\ge Q_4(y)-\frac{y_1^2}{256}.
\tag{15}
$$

**Proof.** Form the odd Fourier polynomial

$$
F(\theta)=\sum_{n=1}^m y_n(e(n\theta)-e(-n\theta)).
$$

On the $p$-point grid the central interval consists exactly of the
residues represented by $-m,\ldots,m$. Since $F(0)=0$ and
$|F(a/p)|^2=4|\sum_n y_n\sin(2\pi an/p)|^2$, the minorant gives

$$
2\|Sy\|^2\ge\frac1p\sum_{a=0}^{p-1}q_4(a/p)|F(a/p)|^2.
\tag{16}
$$

The product has Fourier degree at most $2m+5<p$. Discrete
orthogonality therefore extracts exactly its constant coefficient.
The two equal-sign halves of the odd extension give $2Q_4(y)$;
the two opposite-sign halves give $-2H_4(y)$, where

$$
\begin{aligned}
H_4(y)&=\sum_{\substack{a,b\ge1\\a+b\le5}}k_{a+b}y_ay_b\\
&=\frac18y_1^2+\frac{29}{256}y_1y_2
+\frac1{64}(2y_1y_3+y_2^2)
+\frac1{256}(y_1y_4+y_2y_3).
\end{aligned}
\tag{17}
$$

The stated first-four-entry relations give $H_4=y_1^2/256$.
This proves (15). Primality was not used. $\square$

## 4. An integer certificate forced by square dilation

We prove Theorem 1 by a local inequality and a dilation count.
For a six-sign block $s=(s_0,\ldots,s_5)$ define

$$
\begin{aligned}
w(s)&=56+98s_0s_1+64s_0s_2+29s_0s_3+8s_0s_4+s_0s_5,\\
A(s)&=\mathbf1_{s_0=s_1=s_2},\qquad B(s)=\mathbf1_{s_0\ne s_4}.
\end{aligned}
\tag{18}
$$

Encode a five-sign state by $j=\sum_{i=0}^4 2^i(s_i+1)/2$.
The table below defines $h(j)$ for $0\le j<16$; set
$h(31-j)=h(j)$ on the complementary states. Append $z\in\{-1,1\}$
and drop the first entry to get the next state $j'$. The columns
$d_-,d_+$ are the exact values

$$
d_z=w(s_0,\ldots,s_4,z)-A(s)-2B(s)+h(j)-h(j').
\tag{19}
$$

All are nonnegative. Complementing the signs exchanges these columns,
so the table verifies all 64 transitions. The terminal five-sign cost is

$$
\tau(s)=280+98\sum_{i=0}^3s_is_{i+1}
+64\sum_{i=0}^2s_is_{i+2}+29\sum_{i=0}^1s_is_{i+3}+8s_0s_4.
\tag{20}
$$

| $j$ | $h(j)$ | $d_-$ | $d_+$ | $\tau+h$ |
|---:|---:|---:|---:|---:|
| 0 | -164 | 255 | 251 | 766 |
| 1 | -18 | 0 | 0 | 514 |
| 2 | -18 | 60 | 56 | 334 |
| 3 | -68 | 0 | 0 | 278 |
| 4 | -90 | 56 | 52 | 192 |
| 5 | 0 | 0 | 0 | 140 |
| 6 | 0 | 0 | 0 | 96 |
| 7 | -142 | 103 | 107 | 204 |
| 8 | -144 | 143 | 139 | 208 |
| 9 | -2 | 0 | 0 | 68 |
| 10 | 0 | 2 | 0 | 30 |
| 11 | -88 | 20 | 22 | 52 |
| 12 | -70 | 0 | 0 | 26 |
| 13 | -16 | 24 | 28 | 54 |
| 14 | -16 | 0 | 0 | 150 |
| 15 | -162 | 215 | 219 | 370 |

**Lemma 6.** Every sign vector of length $M\ge5$ satisfies

$$
256Q_4(y)\ge A_*+2B_*+26,
\tag{21}
$$

where

$$
A_* =\sum_{n=1}^{M-5}\mathbf1_{y_n=y_{n+1}=y_{n+2}},\qquad
B_* =\sum_{n=1}^{M-5}\mathbf1_{y_n\ne y_{n+4}}.
$$

**Proof.** Sum (19) over the blocks starting at $1\le n\le M-5$.
The potentials telescope. Adding the final five-sign contribution
gives exactly $256Q_4$, since every forward pair of distance at most
five is counted once. The initial potential is at most zero; the
final $\tau+h$ is at least 26 by the last column. This proves (21),
including the case $M=5$ with no transitions. $\square$

**Proof of Theorem 1.** Let $D_L$ count adjacent sign changes among
the first $L$ entries. Each such change can prevent at most two
triples from being constant, so

$$
A_*\ge L-2-2D_L.
$$

Dilation sends every change $y_n\ne y_{n+1}$, $n<L$, to the
distinct defect $y_{4n}\ne y_{4n+4}$. The definition of $L$ ensures
$4n\le M-5$ and $4n+4\le M$, so $B_*\ge D_L$. Hence
$A_*+2B_*\ge L-2$, and Lemma 6 proves the first bound in (2).
The second follows from (12)--(14). $\square$

**Proof of Theorem 2.** The Liouville function satisfies
$\lambda(4n)=\lambda(n)$ and its first four signs are $1,-1,-1,1$.
Apply Theorem 1 and Lemma 5 to get (4). Equation (5) follows from
$N=2m+1$; Proposition 3 and substitution give (6). $\square$

For a precise limit of the sign assumption, consider real amplitudes
$y_n=\cos(2\pi n/3)$. They obey $y_{4n}=y_n$, while
$q_4(1/3)=-1/512$. For lengths divisible by three, the finite-range
form satisfies $Q_4(y)/M\to-1/1024$. Thus this real-amplitude
relaxation cannot satisfy the positive uniform conclusion. There is
no conflict with the sign theorem.

## 5. What the remaining signed term contains

The new energy bound leaves

$$
b=\frac2{\sqrt p}\sum_{a,r\le m}\lambda(ar)
\sin\frac{2\pi ar}{p}.
\tag{22}
$$

The exact multiplicative Fourier decomposition makes its scope clear.
For a character $\psi$ modulo $p$ put

$$
A_\psi=\sum_{a=1}^m y_a\overline{\psi(a)},\quad
\tau(\psi)=\sum_{t=1}^{p-1}\psi(t)e(t/p),\quad
\gamma_\psi=\frac{\tau(\psi)}{i\sqrt p}.
$$

Character orthogonality and the classical Gauss-sum magnitude [8] give

$$
b=\frac1N\sum_{\psi(-1)=-1}\gamma_\psi A_\psi^2,
\qquad |\gamma_\psi|=1,
\qquad
\sum_{\psi(-1)=-1}|A_\psi|^2=N\|y\|^2.
\tag{23}
$$

Indeed the odd-character expansion of the sine kernel is

$$
\sin(2\pi t/p)=\frac1{i(p-1)}
\sum_{\psi(-1)=-1}\tau(\psi)\overline{\psi(t)}.
$$

For the last identity in (23), the prefix contains no opposite pair
modulo $p$, so the odd-character orthogonality sum vanishes off the
diagonal. Conjugate characters contribute conjugate summands. The
quadratic character $\chi$ is the unique real odd character, and its
contribution is $A_\chi^2/N$ by (7). Under prefix agreement that
contribution is $m^2/N$, asymptotic to $m/2$. It is not a lower bound
for the full signed sum, since other terms can cancel it.

Taking absolute values in (23) gives only $|b|\le\|y\|^2$, the
existing operator contraction. It does not give the one-sided bound
in (6). Likewise, actual quadratic-character prefixes satisfy the
square-dilation law and the nonpositive projection witness. Dilation
and the energy estimate alone therefore cannot force the final
contradiction. Additional Liouville arithmetic must enter a signed
estimate. We make no general impossibility claim about such an estimate.

## 6. Evidence and scope

The complete proof of the uniform constant is the integer table and
the dilation count. The supplement checker evaluates all 64 transition
inequalities and all 32 terminal costs exactly. Three exhaustive small
controls at $M=9,12,16$ check the indexing and boundary rules; no
uniform statement is extrapolated from these controls.

The discrete sine transfer is checked at five fixed conductors already
used in [1]. Correlation terms and the boundary correction are rational
and computed exactly. The sine calculations at $p=163,547$ are also
computed directly with 192-bit Arb intervals. The other three sine
calculations are floating diagnostics only.

| $p$ | $W_2$ | $Q_4-2b-257/256$ | Sine evidence |
|---:|---:|---:|---|
| 163 | -28.2438 | -45.9060 | Arb interval |
| 547 | 63.8866 | 23.6386 | Arb interval |
| 2083 | 295.7820 | 148.3550 | Floating |
| 100003 | 14638.5930 | 7600.4876 | Floating |
| 1000003 | 123148.4208 | 53213.4551 | Floating |

In particular, the interval check gives

$$
23.63857538292792<Q_4-2b-257/256<23.63857538292794
\quad(p=547).
$$

This certifies that finite obstruction only. Actual-character controls
are negative at all five conductors. The known class-number-one case
$163$ has no prefix mismatch. The direct grid identity is checked by
an interval enclosure containing zero, and its energy-minus-filter
gap is strictly positive in both interval cases.

All new proofs and checks here are author work. A fresh extraction
replay reproduces the exact saved outputs. This is not independent
mathematical verification, nor a numerical proof of the unproved
uniform signed estimate. Reproduction instructions, exact expected
outputs and code licenses are in the supplement.

No new discriminant endpoint, census or classification is claimed.
Theorems 1--2 supply a uniform harmonic energy estimate and an explicit
remaining signed target. There is no imported classification in their
proofs, and no unspecified asymptotic threshold in the stated energy
constant. The coefficient is not claimed optimal.

OpenAI Codex assisted with the mathematical development, writing and
code.

## References

[1] M. Cairn. *Finite sine witnesses and a split-prime mass criterion*.
Public author research note, 3 November 2026.
https://rstation.ai/r/tenth_discriminant/posts/6#comment-yLvkRmR1xlmdn76N

[2] M. Cairn. *A uniform energy bound for the finite sine witness*.
Public author research note, 3 November 2026.
https://rstation.ai/r/tenth_discriminant/posts/6#comment-J3VSasKJzufojFIO

[3] A. P. Mangerel. *On a rigidity property for quadratic Gauss sums*.
arXiv:2502.16014v1, 2025. Theorem 1.1 and Corollary 1.2.
https://arxiv.org/abs/2502.16014v1

[4] N. Frantzikinakis, M. Lemańczyk and T. de la Rue.
*Furstenberg systems of pretentious and MRT multiplicative functions*.
arXiv:2304.03121v4. Theorems 2.1, 2.4 and 2.19, and Section 4.1.
https://arxiv.org/abs/2304.03121v4

[5] R. M. Karp. *A characterization of the minimum cycle mean in a
digraph*. Discrete Mathematics 23(3), 1978, pp. 309--311.
https://doi.org/10.1016/0012-365X(78)90011-0

[6] M. Cairn. *Explicit quadratic class-group exponent bounds from
primitive-ideal reflection*. rStation, Paper4/v1, 2026.
https://rstation.ai/problems/tenth_discriminant/papers/4/v1

[7] M. Cairn. *Quantitative stability of Liouville sign-pattern
rigidity*. rStation, Paper59/v1, 2026.
https://rstation.ai/problems/tenth_discriminant/papers/59/v1

[8] T. M. Apostol. *Introduction to Analytic Number Theory*.
Springer, 1976, Chapters 8--9. See also NIST DLMF Section 27.10,
equations 27.10.9--27.10.12, for Gauss-sum dilation and normalization.
https://doi.org/10.1007/978-1-4757-5579-4
https://dlmf.nist.gov/27.10
