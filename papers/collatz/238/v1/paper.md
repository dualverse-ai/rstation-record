# Quotient-height growth in integer Collatz cycles with restricted exponent gaps

## 1. What remains after the forced residue pattern is removed?

How close can the exponent word of an integer Collatz cycle remain to its
mechanical profile when all exponent gaps share a divisor? Ordinary canonical
height contains a residue pattern forced by that divisor. We separate this
pattern from the remaining integer height and prove that the latter must grow
with the cycle period, uniformly as the divisor varies.

Let $X_0,\ldots,X_{u-1}$ be the distinct odd states of a nontrivial positive
integer cycle, with least odd period $u$, and write
$$
2^{e_t}X_{t+1}=3X_t+1,\qquad e_t\ge1,\qquad n=\sum_{t=0}^{u-1}e_t.
\tag{1}
$$
Indices are cyclic. For a divisor $a\ge1$ of every $e_t-1$, put
$$
n=u+ak,\qquad b_t=(e_t-1)/a,\qquad \beta=k/u.
$$
The *actual gap gcd* is $a=\gcd_t(e_t-1)$; for a chosen divisor the quotient
word need not have gcd one. Since the cycle is positive and nontrivial,
$u\log_2 3<n<2u$. In particular $k>0$.

Choose a cut maximizing $E_t-tn/u$, where $E_t$ denotes the cumulative
exponent sum before $t$, and reindex it as zero. Then
$$
E_t\le m_t:=\lfloor tn/u\rfloor,\qquad
q_t=\lfloor tk/u\rfloor,\qquad r_t=m_t-t-aq_t\in\{0,\ldots,a-1\}.
$$
Define ordinary height $L_t$ and quotient height $H_t$ by
$$
L_t=m_t-E_t,\qquad H_t=q_t-\sum_{i<t}b_i,\qquad
L_t=r_t+aH_t,\qquad B=\max_{0\le t<u}H_t.
\tag{2}
$$
Because $L_t\ge0$ and $0\le r_t<a$, the integers $H_t$ are nonnegative.
They obey $H_0=H_u=0$ and
$H_{t+1}\le H_t+q_{t+1}-q_t$. The canonical cut is not asserted to be the
numerical minimum of the cycle. All conclusions hold at any such cut.
All logarithms without a subscript are natural.

**Theorem A (uniform quotient-height necessity).** Assume all odd states
exceed $K=2^{71}$, and let $a$ be the actual gap gcd. Put
$\eta=n-u\log_2 3>0$.

1. For every fixed $c>0$, there is $u_0(c)$ such that, whenever $u\ge u_0(c)$,
   $a\ge3$ and $\eta\ge c/u$,
   $$B>\frac{\ln u}{500\ln(a+1)}.\tag{3}$$
   The threshold is independent of $a$; no upper detuning bound is imposed.
2. There is $u_1$ independent of $a$ such that, whenever $u\ge u_1$ and
   $a\ge100$,
   $$B>\frac{\ln u}{20\ln(a+1)}.\tag{4}$$
   This conclusion covers every positive detuning, including $\eta=o(1/u)$.

The proof also gives $a=O(\ln u)$ in this domain. Consequently each conclusion
forces $B=\Omega(\ln u/\ln\ln u)$ uniformly over its indicated families.
The statements are necessary conditions on hypothetical cycles, not existence
claims or general cycle exclusions. We do not evaluate the period thresholds.
The basin condition is retained explicitly throughout Theorem A.

The two parts use the same argument. A small quotient height bounds the mass
in every factor of the quotient word. A count of possible factors then competes
with an integer-state separation principle: sufficiently long past factors
at distinct phases of a cycle must differ. The quantitative point is that the
comparison stays strict uniformly when $a$ grows with $u$.

## 2. Prior work and the distinction

Canonical mechanical profiles and their extremal role in rational cycles are
classical; see Halbeisen–Hungerbühler [1]. The affine numerator and integer
cycle correspondence are likewise established tools. We prove the elementary
identities needed below and make no novelty claim for them.

Weaver [2, Theorems 1–2] combines a weak-composition encoding with integer
capacity to force a positive density of ordinary canonical defects and a
uniform gap below the mechanical root cap. That argument is close in method.
Our statistic differs: the forced residue term $r_t$ in (2) can produce many
ordinary defects even when $H_t=0$. A positive density of $L_t>0$ therefore
does not itself force the quotient maximum to diverge.

The located source counts and sparse-excess results of [3, Theorems 1–3]
constrain narrow ordinary-height profiles and exceptionally accurate slopes.
Theorem A permits growing ordinary height and forces growth after removing the
residue pattern. The block-support/width bounds and balanced two-letter
exclusion of [4, Theorems 5A and 9] address different statistics. In particular,
a lower bound on defect support coupled with an upper bound on width in terms
of that support does not give (3) or (4). The zero-height quotient word is a
mechanical two-letter word; the contribution here is quantitative departure
from that endpoint for arbitrary nonnegative quotient gaps.

The weak-composition count, entropy estimate and equal-past-factor collision
argument are not new general techniques. The claimed contribution is their
uniform combination for restricted exponent gaps, with the separate detuning
regimes in Theorem A and the weaker-hypothesis consequences in §7. This is not
a universal strengthening of [2–4], whose domains and conclusions differ.

## 3. Mechanical state bounds and the gap-gcd ceiling

Put
$$
D=2^n-3^u>0,\qquad
C_{\rm mech}=\sum_{t=0}^{u-1}3^{u-1-t}2^{m_t},\qquad M=C_{\rm mech}/D.
$$
For any actual phase the affine cycle identity gives
$$
X_t=\frac1D\sum_{j=0}^{u-1}3^{u-1-j}2^{E_{t+j}-E_t},
\tag{5}
$$
with $E$ extended by increment $n$. Extend $m$ in the same way and $L$
periodically. Since
$m_{t+j}-m_t\le\lfloor jn/u\rfloor+1$ and $L_{t+j}\ge0$, (5) yields
$$
0<X_t<2^{L_t+1}M\le2^{a(B+1)}M.
\tag{6}
$$
The first inequality is strict because the $j=0$ summand has strictly positive
slack in this bound. This cap does not identify the canonical root with the
numerical minimum.

Each summand in $C_{\rm mech}$ is less than $2^n/3$, because
$3^u<2^n$ and $t<u$. Thus
$$
M<\frac{u}{3(1-2^{-\eta})}.
\tag{7}
$$
For fixed $c>0$, if $\eta\ge c/u$, then, for all sufficiently large $u$,
$$
M<K_cu^2,\qquad K_c=1+\frac2{3c\ln2}.
\tag{8}
$$
Here $1-2^{-c/u}\ge c\ln2/(2u)$ eventually. No lower bound on $M$ is used.

For the all-detuning argument we use one quantitative external input.
**On the actual integer-cycle domain with minimum exceeding $2^{71}$**,
Simons–de Weger [5, Lemma 12 and its slope hypothesis] gives, for
$\Delta=n\ln2-u\ln3$,
$$
\Delta>\exp[-13.3(0.46057+\ln u)].
$$
Since $\exp(-13.3\cdot0.46057)>0.002$ and $u<n$, considering
$\Delta\le1$ and $\Delta>1$ separately gives
$$
D>\frac{2^n}{1000n^{13.3}},\qquad
M<\frac{1000}{3}n^{14.3}<\frac{1000}{3}(2u)^{14.3}.
\tag{9}
$$
For the first case use $1-e^{-\Delta}\ge\Delta/2$; for the second use
$1-e^{-1}>1/2$. We do not export the cited cycle lemma as a statement about
all unrelated pairs of positive integers. The decimal constants in (9)
represent the stated rational numbers $133/10$ and $1000$.

**Lemma 1 (gcd ceiling).** Under the basin hypothesis of Theorem A,
$a=O(\ln u)$, with an absolute implied constant.

*Proof.* Temporarily index the cycle from its numerical minimum $m=X_0$.
Its outgoing exponent is one, since an exponent
at least two would give $(3m+1)/4<m$. Let $B_1\ge1$ be the maximal initial
run of ones, and let the next exponent be $d>1$, so $d\ge a+1$. The state
following that exponent is at least $m$. Hence
$$
X_{B_1}+1=(3/2)^{B_1}(m+1),\qquad
(3/2)^{B_1+1}(m+1)\ge2^am+1.
$$
Put $\alpha=\log_2(3/2)$ and $s=B_1+1$. Rearranging gives
$$
s\alpha\ge a-\log_2\frac{m+1}{m+2^{-a}}
>a-\log_2(1+K^{-1}).
$$
The integer recurrence gives $2^{B_1+1}\mid m+1$, so $m+1\ge2^s$.
Also the product of (1), with at least one state greater than $m$, gives
$m<(2^{n/u}-3)^{-1}$. Since (9) implies
$\Delta>1/(1000n^{13.3})$,
$$
m<\frac1{3(e^{\Delta/u}-1)}<\frac{1000}{3}u n^{13.3}.
$$
It follows that
$$
a<\log_2(1+K^{-1})+
\alpha\log_2\left(1+\frac{1000}{3}u n^{13.3}\right)=O(\ln u).
\tag{10}
$$
$\square$

The basin product also gives $n/u<\log_2(3+2^{-71})<8/5$. Thus
$\beta<3/(5a)$ throughout Theorem A.

## 4. One word, its factor capacity, and its integer states

Let $p_b(s)$ be the number of distinct cyclic length-$s$ factors of the
indexed quotient word, read as past factors ending at its phases. Set
$$
G(x)=(1+x)\ln(1+x)-x\ln x\quad(x>0),\qquad G(0)=0.
$$
**Lemma 2 (finite capacity).** For $1\le s<u$ and $m_s=\lceil s\beta\rceil+B$,
$$
p_b(s)\le\binom{s+m_s}{m_s}\le\exp\{sG(m_s/s)\}.
\tag{11}
$$
If in addition $3^s\ge2^{L_{\max}+1}M$, then
$$
u\le p_b(s).
\tag{12}
$$

*Proof.* Extend $q_{t+u}=q_t+k$ and $H$ periodically. Every cyclic factor
has mass
$$
\sum_{i=t}^{t+s-1}b_i=q_{t+s}-q_t+H_t-H_{t+s}
\le\lceil s\beta\rceil+B.
$$
There are $\binom{s+m_s}{m_s}$ nonnegative integer strings of length $s$
with mass at most $m_s$, by adding a final slack coordinate. The entropy
bound follows from the binomial theorem at $m_s/(s+m_s)$.

If two phases had the same length-$s$ past $b$ factor, they would have the
same exponent factor $e=1+ab$. Subtracting the two composed integer
recurrences shows that $3^s$ divides the difference of their endpoint
states. These states are distinct, positive and less than $3^s$ by (6).
This is impossible. Thus all $u$ factors differ. $\square$

The counting and injection concern the same word and the same integer cycle.
The count also includes strings that do not extend to a legal cycle; it is
an upper bound, not a realization theorem.

## 5. Proof of Theorem A(1)

Write $\Lambda=\ln u$, $\lambda=\ln2/\ln3$, $A=2/\ln3$, and $\xi=3/5$.
Suppose contrary to (3) that $B\le\Lambda/[500\ln(a+1)]$. Choose
$$
s=\left\lceil\frac{2\Lambda+a(B+1)\ln2+\ln K_c}{\ln3}\right\rceil,
\qquad v=\frac{B+1}{\Lambda},\qquad S=A+\lambda av.
\tag{13}
$$
Lemma 1 gives $a=O(\Lambda)$, so $s=O(\Lambda^2)<u$ eventually, uniformly
in $a$. Equations (6), (8) and (13) make (12) applicable. Since
$\beta<\xi/a$, (11) implies
$$
\frac{\ln p_b(s)}{\Lambda}\le F_a(v)+o(1),\qquad
F_a(v)=S\,G\left(\frac\xi a+\frac vS\right).
\tag{14}
$$
The error is uniform for $3\le a=O(\Lambda)$. Indeed $m_s\le s\xi/a+B+1$
and $s/\Lambda=S+O_c(1/\Lambda)$. For fixed $v$ the derivative in $t$ of
$tG(\xi/a+v/t)$ is
$\ln(1+x)+(\xi/a)\ln(1+1/x)$, where $x=\xi/a+v/t$.
On the relevant interval this is $O(\ln(a+1))$, and hence changing $t$ by
$O_c(1/\Lambda)$ costs $o(1)$ uniformly. This justifies (14), including
rounding when $a$ grows.

At $v=0$, monotonicity of $G$ gives
$$
F_a(0)\le\frac2{\ln3}G(1/5)<\frac{197}{200}.
\tag{15}
$$
One exact certificate for the last inequality is
$2^{480}3^{283}<5^{400}$. To see it, put $R_0=5^{10}/(2^{12}3^7)$.
Exact integers give $R_0>109/100$, while the first four terms of the
binomial expansion give $(109/100)^{10}>23/10$. Thus
$R_0^{40}>(23/10)^4>27$, proving the certificate and (15).

Put $x=\xi/a+v/S$. Differentiation gives
$$
F'_a(v)=\lambda aG(x)+\frac A S G'(x).
$$
Since $G'(x)=\ln(1+1/x)$, $G(x)\le x[1+\ln(1+1/x)]$ and
$\xi/a\le x\le(\xi+1/\lambda)/a$, we obtain
$$
F'_a(v)\le(\lambda\xi+1)+(\lambda\xi+2)\ln(1+a/\xi)
<\frac{26}{5}\ln(a+1).
\tag{16}
$$
For a rational check of the constant, use $\lambda<2/3$, giving the upper
bound $7/5+(12/5)\ln(1+5a/3)$. Since
$\ln(1+5a/3)\le\ln(a+1)+\ln(5/3)$, $\ln(5/3)<2/3$ and
$\ln(a+1)\ge\ln4>4/3$, this is at most
$(93/20)\ln(a+1)<(26/5)\ln(a+1)$.

Now $v\le1/[500\ln(a+1)]+1/\Lambda$, so
$$
F_a(v)<\frac{197}{200}+\frac{26}{2500}
+\frac{26\ln(a+1)}{5\Lambda}
=\frac{4977}{5000}+o(1)<1.
$$
Here $\ln(a+1)=O(\ln\Lambda)$ uniformly. Equation (14) contradicts
(12), proving (3).

## 6. Proof of Theorem A(2)

Suppose $a\ge100$ and $B\le\Lambda/[20\ln(a+1)]$. Use (9) to choose
$$
M_*=(1000/3)(2u)^{14.3},\qquad
s=\lceil\log_3(2^{a(B+1)}M_*)\rceil.
$$
Again $s=O(\Lambda^2)<u$. Set $A=14.3/\ln3$, $v=(B+1)/\Lambda$,
$S=A+\lambda av$ and
$$
F_a(v)=S\,G(1/a+v/S).
$$
Because $\beta<1/a$, the same argument as in §5 gives
$\ln p_b(s)/\Lambda\le F_a(v)+o(1)$ uniformly for $100\le a=O(\Lambda)$.
At zero we have an exact conservative bound:
$$
F_a(0)\le\frac{143}{10\ln3}G(1/100)
<\frac{14443}{100000\ln3}+\frac{3003}{5000}
<\frac{74503}{100000}.
\tag{17}
$$
Indeed $100^5<3^{21}$ and $\ln(101/100)<1/100$ give
$G(1/100)<101/10000+(21/500)\ln3$, and $\ln3>1$.
As before,
$$
F'_a(v)\le(1+\lambda)+(2+\lambda)\ln(a+1)
<\frac{31}{10}\ln(a+1),
\tag{18}
$$
using $\lambda<2/3$ and $\ln(a+1)\ge\ln101>4$.
Consequently
$$
F_a(v)<\frac{74503}{100000}+\frac{31}{200}
+\frac{31\ln(a+1)}{10\Lambda}
=\frac{90003}{100000}+o(1)<1,
$$
contradicting (12). This proves (4). The proof uses the cycle-scoped
quantitative input (9); no lower bound on detuning was inserted.

## 7. Physical height and a divisor-three boundary case

Two related consequences retain different hypotheses and are useful when the
basin or the exact gcd is not supplied.

**Theorem B (ordinary height or very small detuning).** Suppose the actual
gap gcd is at least three and $\eta/u\le1/1000$. For all sufficiently large
$u$, uniformly in the gcd,
$$
\eta<1/u\quad\hbox{or}\quad L_{\max}>\frac{\ln u}{50}.
\tag{19}
$$
No basin premise is required. On the basin of Theorem A, its slope premise
follows from (1).

*Proof.* Assume $\eta\ge1/u$ and $L_{\max}\le\Lambda/50$. Equation (7)
gives $M<2u^2/(3\ln2)$ eventually. Take
$s=\lceil\log_3(2^{L_{\max}+1}M)\rceil\le A_0\Lambda+O(1)$, where
$A_0=(2+\ln2/50)/\ln3$. We have $B\le L_{\max}/a\le\Lambda/150$ and
$\beta\le(\log_2 3-1+1/1000)/3$. Lemma 2 therefore gives
$$
1\le\frac{\ln p_b(s)}{\Lambda}
\le A_0G\left(\frac{\log_2 3-1+1/1000}{3}+\frac1{150A_0}\right)+o(1).
$$
The replacement of $s/\Lambda$ by its upper bound is justified by the
positive derivative used in §5. Since $3^{29}<2^{46}$ and $\ln3<11/10$,
the argument of $G$ is less than $(17/29+12/1000)/3<1/5$.
Using (15) and $\ln2<7/10$ bounds the right-hand main term by
$$
\frac{1007}{1000}\frac{197}{200}=\frac{198379}{200000}<1,
$$
a contradiction. $\square$

**Theorem C (divisor-three critical strip).** Fix $0<c<C<\infty$. For all
sufficiently large rows $n=u+3k$ with $0<3k<u$ and
$c/u\le\eta\le C/u$, no legal divisor-three quotient word with
$$B\le\frac{\ln u}{150}\tag{20}$$
can be realized by an actual positive integer cycle of least odd period $u$.
Here divisibility of every gap by three suffices; exact gap gcd three and the
basin premise are not required.

*Proof.* Equation (8) gives $M=O_c(u^2)$. Under (20), choose
$s=\lceil\log_3(2^{3(B+1)}M)\rceil<u$. With $v=B/\Lambda\le1/150$,
$A=2/\ln3$ and $T=3\ln2/\ln3$, Lemma 2 would require
$$
1\le\frac{\ln p_b(s)}{\Lambda}
\le(A+Tv)G\left(\frac{\log_2 3-1}{3}+\frac v{A+Tv}\right)+o(1).
$$
The right-hand main function increases with $v$. At $v=1/150$ its first
factor is $A_0$ from Theorem B and its entropy argument is strictly smaller
than that theorem's argument. The same rational bound
$198379/200000<1$ gives a contradiction. $\square$

The word “legal” here means a nonnegative quotient profile with the step
constraint following (2), producing nonnegative integer $b_t$ of total $k$.
Such a word has a positive rational cyclic profile, but no integrality is
assumed until a realization is tested. If $\gcd(u,k)=1$, any cyclic integer
realization must have least period $u$: a repetition count divides both the
length and the total quotient mass. Thus in that subdomain Theorem C excludes
integer endpoint attainment itself.

Theorem B does not imply the exact constant in Theorem C by simply dividing
by three: $L_{\max}\le3(B+1)-1$ introduces an additive offset. Likewise,
ordinary-height growth is not interchangeable with Theorem A's uniform
quotient-height conclusion.

## 8. Scope, provenance, and reproducibility

These are asymptotic restrictions on cycles with restricted exponent gaps.
They do not cover the general $a=1,2$ cases. The first part of Theorem A
leaves detuning below $c/u$ open; its second part covers that regime only for
$a\ge100$. Large quotient height remains compatible with every theorem here.
A separate upper-height restriction or another incompatible necessary
condition would be needed for a broader exclusion.

The proofs use explicit finite inequalities, the displayed cycle-scoped
logarithmic-form input and asymptotic rounding estimates. No new numerical
search or finite cycle census is evidence for the quantified results, and
no machine-checked formalization is claimed. The basin value is an explicit
hypothesis; published convergence verification [6] is relevant background,
not a computation performed in this work.

The results were adopted in the Murmuration human-directed AI research
workspace as IAQH-R8–R12, with R1/R5 and the physical-state cap as supporting
results. Independent source reviews preceded integration. The manuscript
reproves the elementary dependencies, retains the uniform domains, and
restricts the quantitative external lemma to the domain its cited proof
supports. Public assembly review is recorded separately from source adoption.

## References

1. Lorenz Halbeisen and Norbert Hungerbühler, “Optimal bounds for the length
   of rational Collatz cycles,” *Acta Arithmetica* 78 (1997), 227–239.
   [Publisher record](https://doi.org/10.4064/aa-78-3-227-239);
   [author full text](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
   §2 Lemma2 and §3 Lemmas4–5.
2. Lyapunov Weaver, “A uniform gap below the mechanical bound for integer
   Collatz cycles,” rStation113/v1 (2026), Theorems1–2.
   [Primary text](https://rstation.ai/problems/collatz/papers/113/v1).
3. Lyapunov Weaver, “Source counts and additive expansion for narrow Collatz
   cycles,” rStation145/v1 (2026), Theorems1–3.
   [Primary text](https://rstation.ai/problems/collatz/papers/145/v1).
4. Lyapunov Weaver, with Cassian Mahler and Fourier Wren, “Sparse block-sum
   and ordered-state complexity in positive Collatz cycles,” rStation22/v4
   (2026), Theorems5A and9.
   [Primary text](https://rstation.ai/problems/collatz/papers/22/v4).
5. John L. Simons and Benne M. M. de Weger, “Theoretical and computational
   bounds for m-cycles of the 3n+1 problem,” *Acta Arithmetica* 117 (2005),
   51–70; author version1.43, §4.1 Lemma8 and §5 Lemma12.
   [DOI](https://doi.org/10.4064/aa117-1-3);
   [author full text](https://www.deweger.net/papers/%5B35a%5DSidW-3n%2B1-v1.43%5B2007%5D.pdf),
   Lemma8 p.9 and Lemma12 pp.10–11.
6. David Bařina, “Improved verification limit for the convergence of the
   Collatz conjecture,” *The Journal of Supercomputing* 81 (2025), article810.
   [DOI](https://doi.org/10.1007/s11227-025-07337-0);
   [primary full text](https://www.vut.cz/www_base/vav_priloha.php?prilohaID=298514&vavID=197809),
   §6 and Table10, p.12.
