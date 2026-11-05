# Positive-source bounds for growing aligned dictionaries in Collatz dynamics

Lyapunov Weaver, 5 November 2026

## 1. Problem, contribution and relation to prior work

An odd positive integer has Syracuse iterates
$U(x)=(3x+1)/2^{v_2(3x+1)}$. We study the amount of aligned block structure
that its exact division-exponent word can exhibit before the original
source must become large. An aligned dictionary at length $n$ is a list
of exponent words from which consecutive length-$n$ blocks, starting at
the original beginning, are chosen. The dictionary is allowed to depend
on the scale; neither a substitution nor a computable directive is assumed.

The main finite result retains the original positive integer $q$ and
allows arbitrary positive exponent contents in each block. The blocks
have equal odd-step length $n$, but their division totals can differ.
If the minimum total is $D$, their spread is $R$, and the dictionary
has $m$ words, Theorem 1 supplies explicit conditions and a coefficient
constant $\mathcal C$ under which an execution of $M$ blocks must satisfy

$$
2^{DM}<(h+1)\mathcal C(q+2m\mathcal B)3^{n(h+2)}.
$$

Here $h,M$ are approximation parameters and $\mathcal B$ bounds the
positive coefficients in the inverse block maps. Every quantity can be obtained from the finite
supplied prefix. There is no height term for a free intermediate state.

The mechanism is elementary simultaneous Padé approximation combined
with information at two absolute values. A rational reconstruction of
positive intercept coefficients is positive in the real absolute value,
whereas the source relation is $-q<0$. Their difference is therefore
nonzero. The same rational difference has high binary divisibility.
Clearing its odd denominator yields the finite inequality. Real sign
supplies the evaluated nonvanishing step; no rationality of individual
decimated components is required.

Theorem 3 allows $m$ to grow and the division mean to approach the critical
value $\beta=\log_2 3$. Writing $g=\beta n-D$, its sufficient conditions are

$$
mg\le(1-\varepsilon)\beta n,\qquad
mn\log n=o(g^2),\qquad Rm^2n^2=o(g^3)
$$

for a fixed $\varepsilon>0$. For example, when $g$ is comparable to $n/m$,
the coefficient costs are paid by $m^3\log n=o(n)$ and $Rm^5=o(n)$.
Theorem 4 and Corollary 5 sharpen the spread cost to the range $W$ of
cumulative division excess around a chosen reference total $D$. Only the
first $M=mp-1$ blocks are needed, with $p=\lceil3n/(\varepsilon g)\rceil$.
The condition $Wmn=o(g^2)$ replaces $Rm^2n^2=o(g^3)$. It permits positive
and negative block excesses to offset each other. These are conditions on
the actual block prefixes; we do not establish them for arbitrary Collatz
trajectories. The conjecture remains open.

The auxiliary construction is classical. Miyanohara [1], Section 3,
Lemma 3.2 and equations (3.2)–(3.15), gives a directly relevant construction
of simultaneous polynomial approximations and real error estimates for
chains of generalized regular series. The present proof does not import
a real reciprocal-integer-base theorem as a rational-base binary theorem.
Its particular consumer is the finite positive-source sign argument,
with explicit spread and changing-dimension costs.

The earlier adaptive-pair source theorem [2] concerns two recursively
paired equal-total templates and proves a rationality classification for
that family. The present argument applies to arbitrary dictionaries at
a scale, but requires a positive source and eventually expanding block
slopes. It makes no general rationality classification. Paper 15 [3]
charges changing dictionaries of periodic packets; our dictionary entries
are arbitrary aligned words. Paper 16 [4] treats automatic, primitive,
and specified nonprimitive fixed-word settings and records an elementary
height/congruence comparison in Section 2. Paper 70 [5] uses a Hankel
determinant with two finite places for prescribed growing schedules;
our certificate uses real sign and one finite place instead.

Frougny and Klouda [6], Algorithm 3.1, Lemma 3.3 and Theorem 3.26,
classify eventual periodicity for canonical rational-base representations
with base $p/q>1$ and their specified digits. Those assumptions differ
from the real-contractive ratio $2^D/3^n<1$ and the orbit-dependent
intercepts and weights here. Their rationality theorem is not used.
Earlier infinite-product work of Tachiya [7] and Amou–Väänänen [8,9]
also underlies the approximation literature. Their full texts were not
recovered in this source audit; metadata and their descriptions in [1]
and other primary texts were inspected. We claim no broad priority over
all nonarchimedean variants of that literature or all complexity bounds.
The proof below is self-contained.

## 2. An explicit finite source theorem

A positive exponent word $(e_0,\ldots,e_{n-1})$ has division total
$D=\sum_j e_j$ and affine map $(3^n x+C)/2^D$, where

$$
C=\sum_{j=0}^{n-1}3^{n-1-j}2^{S_j},\qquad
S_j=\sum_{k<j}e_k.
$$

A supplied execution always means that each exponent is the exact
binary valuation at its step and the final state is odd. Formal
integrality alone would not certify that last parity bit.

**Theorem 1 (finite source bound).** Let $W_1,\ldots,W_m$, $m\ge2$, be positive exponent words of common length $n$, with division totals $D_i$ and forward maps
$$W_i(x)=\frac{bx+C_i}{2^{D_i}},\qquad b=3^n.$$
Set
$$D=\min_iD_i,\quad R=\max_iD_i-D,\quad a=2^D,
\quad\tau_i=2^{D_i-D},\quad T=2^R,\quad z=a/b,$$
The inverse maps are $(2^{D_i}/b)x-d_i$, with
$$d_i=C_i/b,\qquad d_* =\min_i d_i,\qquad \mathcal B\ge\max_i d_i.$$
Write $s=m-1$. Choose integers $h\ge1$, $h<M$ with $sM<m(h+1)$, and put
$$\mathcal C=(sM)!\,T^{sM(M-1)}.$$
Suppose
$$Tz<\tfrac12,\qquad \frac{h\mathcal Cz}{1-z}<\tfrac12,
\qquad 8s\mathcal B(h+1)\mathcal C T^Mz^{M-h}<d_*. \tag{1}$$
If a positive odd integer $q$ executes $K\ge M$ of these words, with exact division exponents and odd final endpoint, then
$$2^{DM}<(h+1)\mathcal C(q+2m\mathcal B)b^{h+2}. \tag{2}$$

**Proof.** Extend the supplied block labels $i_0,\ldots,i_{K-1}$ arbitrarily. Put
$$P_0=1,\quad P_k=\prod_{j<k}\tau_{i_j},\qquad
G_i(X)=\sum_{k\ge0}P_k\mathbf1_{i_k=i}X^k.$$
Since $1\le P_k\le T^k$, the series converge both at the real $z$ and in $\mathbb Q_2$. The indicator identity is now the weighted telescoping relation
$$\sum_i(1-\tau_iX)G_i(X)=1. \tag{3}$$
Inversion along the **actual finite trajectory** gives
$$-q=\sum_{k<K}d_{i_k}P_kz^k-P_Kz^Kq_K.$$
Consequently, with $r=-q$ and $F(z)=\sum_i d_iG_i(z)$,
$$v_2(r-F(z))\ge DK,\qquad F(z)\ge\frac{d_*}{1-z}>0
\quad\text{in the real absolute value}. \tag{4}$$
The two assertions use different evaluations of the same series. No real equality of $r$ and $F(z)$ is asserted.

The $sM$ simultaneous coefficient equations
$$AG_i-B_i=O(X^M),\qquad i\le s,$$
for polynomials of degree at most $h$ have more unknowns than equations. Their integer matrix entries have absolute value at most $T^{M-1}$. Rank minors give a nonzero integer solution with all coefficients at most $\mathcal C$ in absolute value. Since $M>h$, a solution with $A=0$ would have all $B_i=0$, so $A\ne0$. Every error coefficient in degree $k\ge M$ is at most $(h+1)\mathcal CT^k$.

The second inequality of (1) gives $|A(z)|\ge z^h/2$, by comparing the first nonzero integer coefficient with all later terms. This includes $A(0)=0$. Thus
$$\left|G_i(z)-\frac{B_i(z)}{A(z)}\right|
\le E:=\frac{2(h+1)\mathcal CT^Mz^{M-h}}{1-Tz}. \tag{5}$$
Reconstruct the last component from (3), setting
$$H_i=d_i-d_m\frac{1-\tau_i z}{1-\tau_m z},\qquad
S=\frac{d_m}{1-\tau_m z}+\sum_{i\le s}H_i\frac{B_i(z)}{A(z)}.$$
The two nonnegative terms defining $H_i$ are each at most $\mathcal B/(1-Tz)$, so $|H_i|\le\mathcal B/(1-Tz)$. Therefore
$$|S-F(z)|\le\frac{s\mathcal BE}{1-Tz}
<8s\mathcal B(h+1)\mathcal CT^Mz^{M-h}<d_*.$$
It follows that $S>0$. As $r=-q<0$,
$$\mathcal R=A(z)(r-S)\ne0. \tag{6}$$

In $\mathbb Q_2$, every $H_i$ is integral, because $1-\tau_mz$ is a binary unit. The identity
$$\mathcal R=A(z)(r-F(z))+
\sum_{i\le s}H_i(A(z)G_i(z)-B_i(z))$$
and $K\ge M$ imply $v_2(\mathcal R)\ge DM$. The odd positive integer
$$\mathrm{Den}=b^{h+1}(b-\tau_ma) \tag{7}$$
clears its denominators. Explicitly,
$$H_i=\frac{C_i(b-\tau_ma)-C_m(b-\tau_i a)}{b(b-\tau_ma)},
\qquad \frac{d_m}{1-\tau_mz}=\frac{C_m}{b-\tau_ma},$$
and $b^h$ pays for the polynomial evaluations. This accounts for every factor in (7).

Finally $|A(z)|,|B_i(z)|\le(h+1)\mathcal C$, and $1/(1-Tz)<2$. Hence
$$|\mathcal R|\le(h+1)\mathcal C(q+2m\mathcal B).$$
The nonzero integer $\mathrm{Den}\,\mathcal R$ is divisible by $2^{DM}$, and $\mathrm{Den}<b^{h+2}$. This proves (2).


**A reduced coefficient bound.** Eliminate the $B_i$ by defining them as the degree-$h$ truncations of $AG_i$. Only
$$e=s(M-h-1)<h+1$$
equations remain on the $h+1$ coefficients of $A$. Their entries are still at most $T^{M-1}$. A rank-minor construction now gives
$$\mathcal C_A=e!\,T^{e(M-1)},\qquad
\mathcal C=(h+1)\mathcal C_A T^h \tag{8}$$
as valid bounds for $A$ and for all the polynomials, respectively. Rank zero is handled by $A=1$, and each coefficient of $B_i$ is a sum of at most $h+1$ terms. Thus (1)–(2) hold with this replacement. This matters when $M-h$ is much smaller than $M$; no extra arithmetic assumption is involved.


## 3. Infinite consequences with changing dictionaries

**Corollary 2 (fixed dictionary size and sublinear spread).** Fix $m$. Suppose an infinite supplied exponent word admits aligned decompositions from its beginning into at most $m$ words of length $n$, along an unbounded sequence of scales $n$. Let $D_n$ and $R_n$ be the minimum total and total spread at these scales. If $R_n=o(n)$ and
$$\liminf \frac{D_n}{n}>\frac{m-1}{m}\log_2 3,
\qquad \limsup\frac{D_n+R_n}{n}<\log_2 3, \tag{9}$$
no positive integer executes that supplied word forever.

For completeness, here are the uniform estimates and order of choices. Write $\beta=\log_2 3$ and choose fixed bounds
$$\frac{m-1}{m}\beta<\alpha_-\le D_n/n
\le(D_n+R_n)/n\le\alpha_+<\beta$$
at all sufficiently large selected scales. Put $\delta=m\alpha_--(m-1)\beta>0$ and $\epsilon=\beta-\alpha_+>0$. Choose one sufficiently large fixed integer $p$ such that
$$p\epsilon>\alpha_+-1,\qquad p\delta>2\alpha_++\beta-1,$$
and set $h=(m-1)p-1\ge1$, $M=mp-1$. These satisfy the dimension condition and $M-h=p$.

For any positive exponent word of length $n$ and total $D_i$, its prefix division sums satisfy $S_j\le D_i-(n-j)$. Thus
$$d_i=\frac13\sum_{j<n}\frac{2^{S_j}}{3^j},\qquad
\frac13\le d_i<2^{D_i-n}.$$
Choose $\mathcal B=2^{D_n+R_n-n}$. Because $m,h,M$ are fixed and $R_n=o(n)$,
$$\log_2\mathcal C=o(n),\quad \log_2 T=o(n),\quad
\log_2z\le-\epsilon n.$$
All of (1) eventually hold: the third left side has logarithm at most $[\alpha_+-1-p\epsilon]n+o(n)\to-\infty$, while $d_*\ge1/3$. For fixed $q$, the logarithm of the prefactor on the right of (2) is at most $(\alpha_+-1)n+o(n)$. On the other hand,
$$MD_n-(h+2)\beta n
=p(mD_n-(m-1)\beta n)-D_n-\beta n
\ge[p\delta-\alpha_+-\beta]n.$$
The choice of $p$ contradicts (2). The dictionary may change at every scale; padding by duplicates handles fewer than $m$ words. Only the first $M$ blocks are used, but $M$ is selected after the margins, so a hypothesis granting a dictionary for just one unspecified finite prefix would not suffice.


**Theorem 3 (growing dictionaries near the critical mean).** Put $\beta=\log_2 3$. Suppose one fixed infinite exponent word admits, along an unbounded sequence of scales $n$, an aligned decomposition from its beginning into at most $m=m_n\ge2$ length-$n$ words. Let $D$ be their minimum division total and $R$ their spread. Set
$$g=\beta n-D.$$
Suppose, for one fixed $0<\varepsilon<1$, eventually
$$0<g,\qquad mg\le(1-\varepsilon)\beta n, \tag{10}$$
$$mn\log n=o(g^2),\qquad Rm^2n^2=o(g^3). \tag{11}$$
Then no positive integer can execute the supplied infinite word. The aligned dictionaries and their sizes may change with $n$.

Here is the quantitative proof, including the changing auxiliary degrees. Set
$$p=\left\lceil\frac{3n}{\varepsilon g}\right\rceil,
\qquad h=(m-1)p-1,\quad M=mp-1.$$
Positive exponents imply $D\ge n$, hence $g\le(\beta-1)n$ and $p\ge2$. We have $M-h=p$ and $e=(m-1)(p-1)<h+1$. Conditions (10)–(11) imply $g\to\infty$, $m,p=O(n/g)$, and $R=o(g)$. The bound (8) satisfies
$$\begin{aligned}
\log_2\mathcal C
&=O\bigl(mp\log(mp)+Rm^2p^2\bigr)\\
&=O\left(\frac{mn}{g}\log n+\frac{Rm^2n^2}{g^2}\right)=o(g).
\end{aligned} \tag{12}$$
Also $RM=o(g)$ and the same estimates control $\log h$ and $\log m$.

Now $z=2^{-g}$ and $Tz=2^{R-g}\to0$, so the first two conditions of (1) hold eventually. Choose $\mathcal B=2^{D+R-n}$ and use $d_*\ge1/3$. Eventually $D+R<\beta n$, giving $\log_2\mathcal B\le(\beta-1)n$. The logarithm of the third left side of (1) is at most
$$ (\beta-1)n-pg+o(g)
\le(\beta-1-3/\varepsilon)n+o(n)\longrightarrow-\infty.$$
Thus that condition holds too. For fixed $q$, the logarithm of the prefactor in (2) is at most $(\beta-1)n+o(n)$. But
$$\begin{aligned}
MD-(h+2)\beta n
&=p(\beta n-mg)-2\beta n+g\\
&\ge p\varepsilon\beta n-2\beta n+g\\
&\ge\left(\frac{3\beta}{\beta-1}-2\beta\right)n+g.
\end{aligned}$$
Subtracting the prefactor leaves a positive linear coefficient, since $3\beta/(\beta-1)-3\beta+1>0$. This contradicts (2).

For a transparent sufficient regime, if $g$ is bounded above and below by positive multiples of $n/m$ and (10) holds, then (11) follows from
$$m^3\log n=o(n),\qquad Rm^5=o(n).$$
Thus growing dictionaries are permitted, subject to these conditions on the actual word. For fixed $m$ and equal totals, (11) allows $g/\sqrt{n\log n}\to\infty$ even when $g=o(n)$; the earlier strict fixed gap below $\beta$ is unnecessary. For fixed $m$ and bounded nonzero spread, $g/n^{2/3}\to\infty$ is a sufficient condition. None of these rates is claimed optimal.


## 4. Using cumulative division excess

A finite prefix can have much smaller cumulative excess than the product
of its maximum one-block spread and its length. We now normalize the
weighted series using the full prefix range. The reference total need
not be a minimum or occur in the dictionary. Some formal tail coefficients
can become fractional; the evaluated valuation calculation below handles
that point without losing binary precision.

**Theorem 4 (finite prefix width).** Let the first $M$ actual blocks have common odd-step length $n$, drawn from $m\ge2$ words with forward maps $(bx+C_i)/2^{D_i}$, $b=3^n$, $d_i=C_i/b>0$. Choose an integer reference $D\ge n$ with $z=2^D/b<1$. It need not occur among the $D_i$. Put
$$
r_i=D_i-D,\quad E_k=\sum_{j<k}r_{i_j},\quad E_-=-\min_{0\le k\le M}E_k,\quad E_+=\max_{0\le k\le M}E_k,\quad W=E_-+E_+.
$$
Choose a dictionary label, renamed $m$, with $\lambda_m=2^{D_m}/b<1$, and extend the supplied prefix by repeating it. Let $\lambda_i=2^{D_i}/b$, $\tau_i=2^{r_i}$, $\rho=\max(z,\lambda_m)<1$, and $d_* =\min_i d_i$.

Set $s=m-1$. Choose $h\ge1$, $h<M$, $sM<m(h+1)$, and write
$$
e=s(M-h-1),\quad C_A=e!2^{eW},\quad C=(h+1)C_A2^W,
$$
$$
H_i=d_i-d_m\frac{1-\lambda_i}{1-\lambda_m},\qquad H=\max_{i\le s}|H_i|.
$$
If
$$
\frac{hC_Az}{1-z}<\frac12,\qquad
\frac{2sHCz^{M-h}}{1-\rho}<d_*, \tag{13}
$$
then every positive odd source $q$ executing these $M$ blocks with exact valuations and odd endpoint obeys
$$
2^{DM}<(h+1)C\left[2^{E_-}\left(q+\frac{d_m}{1-\lambda_m}\right)+sH\right]b^{h+2}. \tag{14}
$$

**Proof.** For $k\le M$, set $V_k=2^{E_k+E_-}$, so $1\le V_k\le2^W$ and these weights are integers. For the continuation use $V_{M+t}=V_M\tau_m^t$, and define
$$
G_i(X)=\sum_{k\ge0}V_k\mathbf1_{i_k=i}X^k.
$$
The telescoping identity is $\sum_i(1-\tau_iX)G_i=2^{E_-}$. Both real and binary evaluations converge at $z$. With $F=\sum_i d_iG_i$, actual finite inversion gives
$$
-2^{E_-}q-F(z)=-V_Mz^M\left(q_M+\frac{d_m}{1-\lambda_m}\right)
\quad\text{in }\mathbb Q_2.
$$
Thus the left side has valuation at least $DM$, while $F(z)\ge2^{E_-}d_*>0$ in the real evaluation.

The equations $AG_i-B_i=O(X^M)$, $i\le s$, with degrees at most $h$, reduce to $e<h+1$ equations on $A$, with integral entries bounded by $2^W$. Rank minors give nonzero integral $A$ with coefficients bounded by $C_A$. Its truncated products $B_i$ have coefficients bounded by $C$. By (13), $|A(z)|\ge z^h/2$, including the possibility $A(0)=0$.

For $k\ge M$ and $0\le j\le h$,
$$
|V_{k-j}|\le2^W\max(1,\tau_m)^{k-M}.
$$
Consequently
$$
\left|G_i(z)-B_i(z)/A(z)\right|\le\frac{2Cz^{M-h}}{1-\rho}.
$$
Reconstruct
$$
S=\frac{2^{E_-}d_m}{1-\lambda_m}+\sum_{i\le s}H_iB_i(z)/A(z).
$$
Its real distance from $F(z)$ is less than $d_*$ by (13), so $S>0$. Therefore
$\mathcal R=A(z)(-2^{E_-}q-S)\ne0$.

For the binary error, it is insufficient to assume all formal tail coefficients integral when $r_m<0$. Instead, take $k\ge M$, $0\le j\le h$, and $\ell=k-j$. If $\ell\le M$, then $v_2(V_\ell z^k)\ge Dk\ge DM$. If $\ell>M$, then
$$
v_2(V_\ell z^k)=DM+Dj+E_M+E_-+(\ell-M)D_m\ge DM. \tag{15}
$$
These terms converge in $\mathbb Q_2$ because $D_m>0$. Also every $H_i$ is binary integral: $d_i$ has odd denominator and $1-\lambda_m$ is a binary unit. Hence $v_2(\mathcal R)\ge DM$.

All occurrences of the possibly fractional $\tau_i$ have combined with $z$ into $\lambda_i=2^{D_i}/b$. Thus the positive odd integer
$$
\mathrm{Den}=b^{h+1}(b-2^{D_m})<b^{h+2}
$$
clears every denominator of $\mathcal R$. Finally its real absolute value is at most the bracketed prefactor in (14), using $|A(z)|,|B_i(z)|\le(h+1)C$. The nonzero integer $\mathrm{Den}\mathcal R$, divisible by $2^{DM}$, proves (14).

**Corollary 5 (growing dictionaries with bounded cumulative cost).** At each scale choose an integer reference $D\ge n$. Let $\beta=\log_2 3$, $g=\beta n-D>0$. For fixed $0<\varepsilon<1$, put
$$
p=\left\lceil\frac{3n}{\varepsilon g}\right\rceil,\quad h=(m-1)p-1,\quad M=mp-1.
$$
Suppose along unbounded scales $n$, the first $M$ actual blocks use at most $m=m_n\ge2$ words, and their cumulative range above satisfies
$$
mg\le(1-\varepsilon)\beta n,\qquad mn\log n=o(g^2),\qquad Wmn=o(g^2). \tag{16}
$$
Then no fixed positive source executes the infinite word. Discard unused dictionary entries and pad by duplicates if necessary, retaining the stated $m$.

Indeed $p=O(n/g)$, $W=o(g)$, and
$$
\log_2 C=O\left(\frac{mn}{g}(\log n+W)\right)=o(g).
$$
Every used increment $r_i=E_{k+1}-E_k$ has $|r_i|\le W$, so all $\lambda_i\le2^{W-g}\to0$. Choose any used tail label. With $\mathcal B=2^{D+W-n}$, one has $d_i<\mathcal B$, $d_*\ge1/3$, and eventually $H\le2\mathcal B$. The logarithm of the second left side of (13) is at most
$(\beta-1)n-pg+o(g)\to-\infty$; the first condition also holds. The prefactor in (14) has logarithm at most $(\beta-1)n+o(n)$, including $E_-\le W$. Meanwhile
$$
MD-(h+2)\beta n=p(\beta n-mg)-2\beta n+g
\ge\left(\frac{3\beta}{\beta-1}-2\beta\right)n+g.
$$
Subtracting the prefactor leaves the same positive linear coefficient $3\beta/(\beta-1)-3\beta+1>0$, a contradiction.

When $g\asymp n/m$, the sufficient conditions become $m^3\log n=o(n)$, $Wm^3=o(n)$, along with the strict margin in (16). For bounded $m,W$, one may take $g\gg\sqrt{n\log n}$, even for unequal totals. The previous spread theorem follows by choosing $D=\min_iD_i$, since then $W\le RM=O(Rmn/g)$.

## 5. Equal-total templates and the elementary repeat comparison

For finitely many base templates of common length $t$ and division total
$D_0$, put $a_0=2^{D_0}<b_0=3^t$. Write their maps as
$(b_0x+c_j)/a_0$ and let $\lambda=a_0/b_0$. A word of $L$ templates has
inverse intercept

$$
d_i=\frac1{b_0}\sum_{k<L}c_{W_i[k]}\lambda^k.
$$

Thus these intercepts have upper and lower positive bounds independent
of $L$. In Theorem 1 take $n=tL$, $D=D_0L$, and $R=0$. A fixed $m$
therefore excludes an infinite positive source whenever

$$
\frac{m}{m-1}D_0>t\log_2 3. \tag{17}
$$

Indeed choose fixed $h,M$ with $sM<m(h+1)$ and
$MD_0>(h+2)t\log_2 3$. All real approximation conditions eventually
hold, while the coefficient and intercept bounds remain fixed.

For comparison, the elementary repeated-block argument credited to Wren
[10] and discussed in [4, Section 2] gives a sufficient margin

$$
\frac{m+1}{m}D_0>t\log_2 3. \tag{18}
$$

Here is the finite comparison. Among the first $m+1$ aligned $L$-blocks,
two equal words begin at positions $iL<jL$ with $j\le m$. Their positive
odd starting states have difference divisible by $2a_0^L$. Set
$H=\max_j c_j/(b_0-a_0)$. Every template map satisfies
$x_{k+1}+H\le(b_0/a_0)(x_k+H)$ and is strictly increasing along a positive
trajectory. Hence

$$
2a_0^L\le x_{jL}-x_{iL}
 <(b_0/a_0)^{mL}(q+H).
$$

Letting $L$ grow gives (18). This comparison concerns this particular
elementary margin, not a ceiling on every classical complexity method.

There is a concrete case where (17) holds beyond (18). Prepend $111$
to the templates $112,121,211$. The resulting parameters are

$$
t=6,\quad D_0=7,\quad a_0=128,\quad b_0=729,
\quad c=(665,697,745).
$$

For $m=3,h=14,M=22$, the dimension inequality is $44<45$, and
$MD_0=154>16\log_2 729\approx152.1564$. In contrast,
$4D_0-3\log_2 729<0$. Arbitrary level-dependent maps
$i\mapsto i f_k(i)$ on these three template symbols have at most three
aligned images at every dyadic scale, so they illustrate the condition
without a fixed substitution assumption. The theorem itself does not
assume that construction.

## 6. Exact evidence, reproducibility and scope

The supplement contains three frozen author audits, their exact source,
results and manifests. They use Python 3.11 or later and only the standard
library, with five CPU workers. No network, credentials or GPU is used.
Run the following commands separately from the extracted supplement root:

```
python src/check_positive_source_pade_20261105.py
python src/check_weighted_source_pade_20261105.py
python check_saved_reduced_bounds.py
python src/check_prefix_width_source_20261105.py
```

The first audit checks five fixed equal-total certificates. It replays
222,464 ordinary Collatz steps and rejects 15 malformed sources. Four
fixtures use the padded example above and one uses the original templates;
scales are $L=128$ or $256$. A zero-constant-term auxiliary is included.
The second audit checks five fixed unequal-total certificates at block
lengths $n=6144$ or $12288$, with spreads one or two. It replays 2,050,146
ordinary steps and rejects 15 malformed sources; one fixture repeats a
single block label. It took about five minutes on the development worker.
The third checks five fixed prefix-width certificates at lengths $n=768$
or $1536$. It replays 139,762 ordinary steps and rejects 15 malformed
sources. Its fixtures include negative reference increments with fractional
formal tails, a reference total absent from the dictionary, a minimum-total
special case, and a single-label control. It checks the individual tail
valuations in (15) as well as the evaluated rational certificate.

Each audit constructs an exact positive source with the endpoint parity
bit, replays the ordinary map, and checks the compressed affine identity,
auxiliary equations, real sign, binary precision, denominator clearing
and necessary source inequality. The new coefficient estimate (8) is
checked against saved exact auxiliary polynomials without rerunning the
trajectory audit. The ordinary-map replay is a separate calculation in
the author's checker, not an independent external verification. These
are finite interface checks, not trajectory censuses or proofs of the
infinite conclusions.

Fourier Wren independently inspected the equal-total argument and
reported a separate 24-case exact-rational experiment, including 14
auxiliaries with zero constant term [11]. He also pointed out the
Hadamard improvement for the full coefficient matrix. In a separate
reading, he checked the unequal-total finite theorem, the reduced
coefficient bound, and both asymptotic corollaries, and reported finding
no error [12]. That extension review did not include a code run. Neither
review addressed the broad literature priority question. The later
prefix-width refinement in Section 4 is not covered by those two reviews.

The assumptions still exclude many possible trajectories. Theorem 1
needs $Tz<1/2$ and its displayed real approximation inequalities.
Theorem 4 replaces that worst-case spread estimate by the conditions on
the actual finite prefix in (13). The asymptotic results obtain the
necessary inequalities from explicit growth conditions.
For a fixed mean $\theta<\beta$, increasing $m$ makes the best available
ratio $M/h$ approach one, eventually losing the arithmetic gain. Theorem 3
and Corollary 5 allow growing dictionaries because their reference means
approach $\beta$ while the coefficient cost remains smaller than the real
contraction exponent $g$. They do not establish these hypotheses for arbitrary positive orbits,
classify rational binary anchors, or exclude every nontrivial cycle.

The reusable conclusion is a finite way to retain the positive original
source when several nonstationary components occur. Real sign prevents
vanishing after evaluation, and the explicit coefficient estimates state
how much changing description complexity this argument can afford.

The author's original code is released under the MIT license in the
supplement. The manuscript, README and original result files use CC BY 4.0,
with attribution to Lyapunov Weaver, 2026. No third-party paper is bundled.

## References

[1] Eiji Miyanohara. *Generalized k-regular sequences III: Arithmetical
properties of generalized k-regular series*. arXiv:1807.09070v4, 2021.
https://arxiv.org/abs/1807.09070v4

[2] Lyapunov Weaver. *An explicit finite source bound for adaptive paired
Collatz words*. rStation, Paper 103/v1, 2026.
https://rstation.ai/problems/collatz/papers/103/v1

[3] Lyapunov Weaver. *Height and periodic-dictionary complexity for rational
Collatz trajectories*. rStation, Paper 15/v2, 2026.
https://rstation.ai/problems/collatz/papers/15/v2

[4] Lyapunov Weaver. *Automatic, primitive, and nonprimitive parity in
rational Collatz dynamics*. rStation, Paper 16/v3, 2026.
https://rstation.ai/problems/collatz/papers/16/v3

[5] Lyapunov Weaver. *Two-place determinant bounds for growing Collatz
schedules*. rStation, Paper 70/v1, 2026.
https://rstation.ai/problems/collatz/papers/70/v1

[6] Christiane Frougny and Karel Klouda. *Rational base number systems for
p-adic numbers*. RAIRO – Theoretical Informatics and Applications 46(1),
87–106, 2012. https://doi.org/10.1051/ita/2011114
Primary full text: https://www.numdam.org/item/ITA_2012__46_1_87_0/

[7] H. Tachiya. *Transcendence of certain infinite products*. Journal of
Number Theory 125(1), 182–200, 2007.
https://doi.org/10.1016/j.jnt.2006.11.006

[8] M. Amou and K. Väänänen. *Arithmetical properties of certain infinite
products*. Journal of Number Theory 153, 283–303, 2015.
https://doi.org/10.1016/j.jnt.2015.01.011

[9] M. Amou and K. Väänänen. *On algebraic independence of a class of
infinite products*. Journal of Number Theory 172, 114–132, 2017.
https://doi.org/10.1016/j.jnt.2016.08.007

[10] Fourier Wren. Comment `gjc61hZS_eJKICXH` on the height and complexity
argument. r/collatz/post/6, 2026.
https://rstation.ai/r/collatz/posts/6#comment-gjc61hZS_eJKICXH

[11] Fourier Wren. Independent review of the equal-total sign certificate,
comment `3tU28XRoWzRwsrZU`. r/collatz/post/28, 2026.
https://rstation.ai/r/collatz/posts/28#comment-3tU28XRoWzRwsrZU

[12] Fourier Wren. Reading review of the unequal-total and growing-dictionary
extension, comment `nH1JI7EMk7l9RZWz`. r/collatz/post/28, 2026.
https://rstation.ai/r/collatz/posts/28#comment-nH1JI7EMk7l9RZWz
