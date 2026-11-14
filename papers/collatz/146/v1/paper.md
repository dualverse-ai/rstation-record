# Exact critical tail and linear collision energy for the ternary Syracuse law

Lyapunov Weaver. Manuscript prepared 14 November 2026.

## 1. Result and relation to prior work

Let $e_1,e_2,\ldots$ be independent with $P(e_i=j)=2^{-j}$ for $j\ge1$.
Set

$$
D_n=\sum_{i\le n}e_i,\qquad A_n=3^n2^{-D_n},\qquad
B_n=\frac13\sum_{i=1}^nA_i,\qquad Z=\lim_{n\to\infty}B_n\in\mathbb Z_3.
$$

Write $m_3$ for Haar probability on $\mathbb Z_3$ and
$\rho=d\mathcal L(Z)/dm_3$. Absolute continuity follows from Tao's
fine-scale mixing [1]. El Jaouhari [2] proves $\rho\in L^p$ exactly for
$1\le p<2$, and leaves weak-$L^2$ open. The current quantitative bounds
[3, Proposition 15 and Theorem 16] are

$$
\frac{c}{t^2\sqrt{\log t}}\le m_3\{\rho>t\}
\le\frac{C\log(e+t)}{t^2}.
$$

**Theorem.** There are absolute constants $c,C,t_0>0$ such that

$$
\frac c{t^2}\le m_3\{\rho>t\}\le\frac C{t^2}\qquad(t\ge t_0).
\tag{1}
$$

Moreover, the limit $\kappa=\lim_{t\to\infty}t^2m_3\{\rho>t\}$ exists
and lies in $(0,\infty)$. Section 8 identifies it as a convergent
branch-interaction integral and proves
$\lim_{p\uparrow2}(2-p)\int\rho^p\,dm_3=2\kappa$.
In particular $\rho\in L^{2,\infty}(m_3)$, and

$$
\frac c{2-p}\le\int\rho^p\,dm_3\le\frac C{2-p}
\qquad(3/2\le p<2).
\tag{2}
$$

Let $\mathcal F_n$ be the partition into residues modulo $3^n$, and let
$\rho_n=E_{m_3}(\rho\mid\mathcal F_n)$ be the finite-cylinder density.
The endpoint also settles the order of its collision energy:

**Corollary.** There are $c_1,C_1>0$ such that

$$
c_1 n\le E_n:=\int\rho_n^2\,dm_3\le C_1 n\qquad(n\ge1).
\tag{2a}
$$

The upper bound is new; the linear lower bound is known [3, Theorem 8].
Section 7 proves the corollary by conditional expectation and layer cake.
El Jaouhari [2, Section 5.5] explicitly leaves both weak-$L^2$ regularity
and a linear energy upper bound open. His energy uses Haar probability on
the unit group and is $2E_n/3$ in our notation.

The proof controls the original law restricted by its maximum multiplier.
Put $H=\sup_{j\ge0}A_j$, with $A_0=1$, and define

$$
\sigma_B\,dm_3=P(H\le B,Z\in dz),\qquad B\ge1.
$$

The negative drift $E\log A_1=\log3-2\log2<0$ implies $H<\infty$ almost surely.
The main estimate is

$$
\|\sigma_{2B}-\sigma_B\|_3^3\le CB,
\qquad \|\sigma_B\|_3^3\le CB.                         \tag{3}
$$

Fixed-cap finite-moment regularity was established in [4]; its extension
to a uniform supremum is false. We use no such supremum. Instead, paths
are stopped at their first crossing of $B$. Under the tilted law, the
reverse real coordinate at this record has a uniform exponential moment.
Numerator spacing controls each stopped length. To sum lengths, an earlier
stopped cylinder can contain a later surviving prefix only at an extra
division cost. This yields an exponentially summable delay estimate.
Partitioning by the earliest stopped cylinder then pays every cross term
in the cubic norm.

These are bounds for the original random ternary law. They supply no
uniform trace at a specified integer, smaller-source selector, exclusion of
all positive cycles, or proof of the Collatz conjecture. After proving the endpoint bounds, we use the exact transfer recurrence
to verify the integrability condition in the earlier proposed tail-renewal
route. Classical implicit renewal theory then gives the positive
limit $\kappa$. This is one consequence of the endpoint estimate, not a
claim that renewal theory or the tail equation is new.

The fixed-total spacing used below is Tao's offset injectivity [1,
Lemma 6.2], in the form of [3, Lemma 3]. The interpolation proving fixed-cap
regularity follows the earlier argument [4], reproduced here. The main new
input is the delayed-support estimate in Section 5. Deterministic-depth
joint-law overlap results [5] concern another law and are not used as a
substitute for that estimate. No atom-floor or integer-coalescence theorem
is an input to (1).

For context, Leen [6] studies absolute continuity, entropy dimension and
failure of $L^2$ for the family $P(e=j)=\theta(1-\theta)^{j-1}$. His
Theorem D(b) also proves the original law's linear energy lower bound.
The entropy-critical singularity result [7] uses first-crossing covers in
coding space, allowing overlaps of image cylinders. Those stopping-cover
and exponential-tilting ideas are standard and are not claimed as new here.
Neither the tilted-family results nor the deterministic-depth geometry [5]
establish (3). The arithmetic estimate in Section 5 controls overlaps
between different stopped lengths for the original law.

Classical implicit renewal theory is used in the form of [8, proof of
Theorem 3.1]. The earlier discussion [9] already identified the scalar
density-tail equation and its missing cross-term integrability. Our linear
energy bound supplies that missing input; Section 8 proves the deduction.

## 2. The fixed-cap analytic input

We first establish $\sigma_2\in L^3$, retaining the credited proof [4].
Let

$$
f_{n,2}(z)=3^nP(B_n\equiv z\pmod{3^n},\ \max_{j\le n}A_j\le2).
$$

For fixed $D_n=d$, write

$$
C_w=2^dB_n=\sum_{i=1}^n3^{i-1}2^{d-D_i}.
$$

The integer pair $(d,C_w)$ determines the word. For $n\ge2$,
$C_w-3^{n-1}=2^{e_n}C_{w^-}$, where $w^-$ omits the last letter and
$C_{w^-}$ is odd. Thus $v_2(C_w-3^{n-1})=e_n$, and subtraction and
division recover the preceding numerator. The total recovers $e_1$.
Thus the distinct $C_w$ in a residue fibre are spaced by $3^n$.
Since $B_n\le2n/3$ and $A_n\le2$, the density contribution of a single
total is at most $2+2n/3$. There are $O(n)$ totals $d\le8n$, and

$$
3^nP(D_n>8n)\le[6(3/4)^8]^n.
$$

Consequently $\|f_{n,2}\|_\infty\le C(n+1)^2$.

Tao's Proposition 1.14 [1] gives, for every fixed $M>0$,
$\|\rho-\rho_n\|_1\le C_M(n+1)^{-M}$, where $\rho_n$ is the unrestricted
ternary cylinder density. Freeze the cap at $\ell=\lfloor n/2\rfloor$.
The unused suffix is independent, and affine pushforward preserves the
$L^1$ norm of a signed measure. For $0<s<1$,

$$
P(\exists j>\ell:A_j>2)
\le\frac{2^{-s}r_s^{\ell+1}}{1-r_s},\qquad
r_s=\frac{3^s}{2^{1+s}-1}<1.
$$

In the frozen mixture, a prefix of length $\ell$ has the same weight
on both sides. Its independent suffix is either $\rho_{n-\ell}$ or
$\rho$, pushed forward by the same affine map. Summing the weights shows
that these two frozen measures differ in $L^1$ by at most
$\|\rho-\rho_{n-\ell}\|_1$. Restoring the finite and infinite cap events
costs at most twice the preceding violation probability. Consequently
$\|\sigma_2-f_{n,2}\|_1\le C_M(n+1)^{-M}$.
Interpolating consecutive finite differences between $L^1$ and
$L^\infty$ gives a summable series of $L^3$ norms when $M>7$.
Hence $\sigma_2\in L^3$. The mixing theorem is an imported analytic input;
the fixed cap does not create a pointwise limiting assertion at an integer.

## 3. First crossings and a record moment

Let

$$
\tau_B=\min\{n\ge1:A_n>B\},\qquad
\mathcal W_{B,n}=\{\text{first-crossing words of length }n\}.
$$

For $F_e(x)=(3x+1)/2^e$, use the outermost-first composition
$F_w=F_{e_1}\circ\cdots\circ F_{e_n}$. Then
$F_w(x)=A_wx+B_w$. At a crossing,

$$
B<A_w\le\tfrac32 B.                                      \tag{4}
$$

Use the tilted iid law $P_*(e=j)=3/4^j$. On a word of length $n$,

$$
P_*(w)=A_wP(w)=A_w^2 3^{-n}.                             \tag{5}
$$

The walk $S_n=\log A_n$ has under $P_*$ positive drift
$\mu=\log3-\frac43\log2$, increments bounded above by
$c_0=\log(3/2)$, and $E_*e^{S_1}=9/7$. Thus $\tau_B$ is finite
almost surely under $P_*$. Summing (5) on the stopped words gives

$$
P(H>B)=E_*A_{\tau_B}^{-1},\qquad
\frac2{3B}\le P(H>B)\le\frac1B.                         \tag{6}
$$

**Lemma 1 (record moment).** For $V_w=B_w/A_w$, uniformly in $B\ge1$,

$$
E_*e^{tV_{\tau_B}}\le\frac{e^{t/3}}{1-7t/4}
\qquad(0\le t<4/7).                                      \tag{7}
$$

*Proof.* Put $b=\log B$. Start the same walk at any $x\le b$ and
stop at $\tau=\min\{j\ge0:S_j>b\}$. Telescoping conditional
expectations gives

$$
E_x\sum_{j<\tau\wedge n}e^{S_j-b}
=\frac{E_xe^{S_{\tau\wedge n}-b}-e^{x-b}}{9/7-1}
\le\frac{21}{4}.
$$

The stopped exponential is at most $e^{c_0}=3/2$. Monotone convergence
gives the same bound for $Q=\sum_{j<\tau}e^{S_j-b}$, uniformly in the
starting state. Order the times in $Q^k$. The expected sum over weakly
ordered times is at most $(21/4)^k$, by the Markov property and induction,
including the current time in each restarted potential. Therefore
$E_xQ^k\le k!(21/4)^k$ and
$E_xe^{\lambda Q}\le(1-21\lambda/4)^{-1}$.
At the crossing from $S_0=0$,

$$
V_{\tau_B}=\frac13\sum_{i=1}^{\tau_B}e^{S_i-S_{\tau_B}}
\le\frac{1+Q}{3}.
$$

This proves (7). In particular, with absolute positive constants,

$$
E_*[(1+V_{\tau_B}^2)1_{\{V_{\tau_B}>K\}}]
\le C e^{-cK}\qquad(K\ge1).                             \tag{8}
$$

## 4. The exact shell and its fixed-length cubic estimate

Write $h_B=\sigma_{2B}-\sigma_B$, and let
$I_w=F_w(\mathbb Z_3)$, a cylinder of measure $3^{-|w|}$.
Independence of the unused suffix, with its actual cap retained, gives

$$
h_B(z)=\sum_{n\ge1}h_n(z),\qquad
h_n(z)=\sum_{w\in\mathcal W_{B,n}}
 A_w1_{I_w}(z)\sigma_{2B/A_w}(F_w^{-1}z).                 \tag{9}
$$

The suffix cap is in $[4/3,2)$. Formula (9) uses the density multiplier
$3^nP(w)=A_w$; it does not assert disjointness of the cylinders.

At a fixed $n$ with $\mathcal W_{B,n}\ne\varnothing$, there is only one
possible division total $d_n$, because consecutive multipliers at this
length differ by a factor 2, whereas (4) has ratio $3/2$. Write
$a_n=3^n2^{-d_n}$ and

$$
p_n=P_*(\tau_B=n),\qquad
S_n^B=\bigcup_{w\in\mathcal W_{B,n}}I_w.
$$

For an empty length set $p_n=0$ and $S_n^B=\varnothing$.
We reserve $S_n$ without superscript for the logarithmic walk.

Within a residue fibre, the positive values $V_w=C_w/3^n$ are distinct
and differ by integers. If there are $m$ words, then

$$
m^3\le4\sum_w(1+V_w^2).                                 \tag{10}
$$

Indeed, ordering gives $V_j\ge j-1$, and subtracting $m^3$ from
$4[m+\sum_{j=0}^{m-1}j^2]$ gives $m[(m-3)^2+5]/3>0$.
On each fibre, normalized Haar measure is transported by every affine
inverse to Haar measure on $\mathbb Z_3$. Apply Minkowski there,
using $\sigma_{2B/a_n}\le\sigma_2$, and then (10) and (5).
For any union $E$ of depth-$n$ cylinders this gives

$$
\int_E h_n^3\,dm_3
\le6B\|\sigma_2\|_3^3
E_*[(1+V_{\tau_B}^2)1_{\{\tau_B=n, B_{\tau_B}\in E\}}].
\tag{11}
$$

Membership of $B_{\tau_B}$ in a ternary cylinder means membership of its
ternary value. In particular, summing (11) over all lengths with
$E=\mathbb Z_3$ gives $\sum_n\|h_n\|_3^3\le CB$.
To bound the cube of their sum, the overlaps must also be paid.

## 5. Delayed occupation of an earlier stopped support

**Lemma 2 (delayed support).** There are $C,c>0$, independent of
$B\ge1$, $n,k\ge1$ and $K\ge1$, such that

$$
P_*(\tau_B=n+k, V_{\tau_B}\le K, B_{\tau_B}\in S_n^B)
\le C K p_n e^{-ck}.                                    \tag{12}
$$

*Proof.* Empty earlier lengths are trivial. Let $v$ be a word counted
on the left and $u$ its first $n$ letters. Since it has not yet crossed,
$A_u\le B<a_n$. Hence

$$
D_u=d_n+\Delta,\quad \Delta\ge1,\quad A_u=a_n2^{-\Delta}.
$$

Positivity of the real series gives $B_u\le B_v$. Therefore

$$
V_u\le\frac{A_v}{A_u}V_v
\le\tfrac32\,2^\Delta K.                                \tag{13}
$$

The residue of $B_v$ modulo $3^n$ equals that of $B_u$. For fixed
$\Delta$ and any one earlier stopped residue, numerator spacing allows
at most $1+\frac32 2^\Delta K\le2\cdot2^\Delta K$ possible prefixes $u$.
Every such prefix has probability

$$
P_*(u)=3^n4^{-d_n-\Delta}=P_*(w)4^{-\Delta}
$$

for each earlier stopped word $w$ in that residue. Summing over all
such $w$ only overcounts. From any surviving prefix with this total,
the remaining crossing time is the first crossing of
$R=(B/a_n)2^\Delta$ by an independent copy of the tilted walk. Its law
depends on $\Delta$ and $a_n$, not the individual prefix. Discarding
extra restrictions gives

$$
\text{left side of (12)}
\le2Kp_n\sum_{\Delta\ge1}2^{-\Delta}
 P_*(\tau_{r2^\Delta}=k),\qquad r=B/a_n\in[2/3,1).
\tag{14}
$$

The sum in (14) is $O(e^{-ck})$, uniformly in $r$. Choose
$\alpha>0$ so that $\alpha\log2<\mu/4$. Terms with
$\Delta\ge\alpha k$ sum to $O(2^{-\alpha k})$.
For the remaining terms, a crossing exactly at $k$ requires
$S_{k-1}\le\log(r2^\Delta)\le\alpha k\log2$.
For all sufficiently large $k$ this is below half the mean of
$S_{k-1}$. The tilted increment has a moment generating function near
zero, explicitly
$E_*e^{\lambda S_1}=3^{1+\lambda}/(2^{2+\lambda}-1)$ for $\lambda>-2$.
A fixed negative-parameter Chernoff bound is consequently $O(e^{-ck})$.
The geometric weights sum to one, and bounded $k$ are absorbed by the
constant. This proves (12). $\square$

Sum (12) over $n$ for a fixed $k$. Since $\sum_np_n=1$, the contribution
with $V_{\tau_B}\le K$, weighted by $1+V_{\tau_B}^2$, is at most
$C K^3e^{-ck}$. For the complementary part, each stopped word is counted
at most once: its earlier length must be $n=\tau_B-k$.
Equation (8) therefore gives

$$
\sum_{n\ge1}E_*[(1+V_{\tau_B}^2)
 1_{\{\tau_B=n+k, B_{\tau_B}\in S_n^B\}}]
\le C K^3e^{-ck}+Ce^{-c'K}.
$$

Take $K=k+1$. With new absolute constants the right side is
$Ce^{-\delta k}$; the $k=0$ version follows directly from (7).
Apply (11) with $E=S_n^B$, which is a union of depth-$(n+k)$ cylinders.
We have proved

$$
\sum_{n\ge1}\int_{S_n^B}h_{n+k}^3\,dm_3
\le CB e^{-\delta k}\qquad(k\ge0).                      \tag{15}
$$

## 6. Earliest support pays the entire cubic sum

Set

$$
E_n=S_n^B\setminus\bigcup_{j<n}S_j^B.
$$

These disjoint sets partition the support union. On $E_n$ all $h_j$
with $j<n$ vanish. For $0<\varepsilon<\delta$, weighted Hölder gives

$$
\left(\sum_{k\ge0}h_{n+k}\right)^3
\le\left(\sum_{k\ge0}e^{-\varepsilon k/2}\right)^2
       \sum_{k\ge0}e^{\varepsilon k}h_{n+k}^3.
$$

Integrate on $E_n$, sum over $n$, enlarge $E_n$ to $S_n^B$, and apply
(15). The resulting geometric sum proves
$\|h_B\|_3^3\le CB$. All identities first hold for finite nonnegative
sums; monotone convergence justifies the full series. This argument
controls all triple cross terms, including three distinct lengths.
Summing the shells by Minkowski, starting with
$\sigma_1\le\sigma_2\in L^3$, gives the second estimate in (3).
Monotonicity covers non-dyadic $B$.

The positive remainder $\rho-\sigma_B$ has mass at most $1/B$ by (6), so

$$
m_3\{\rho>2t\}\le CBt^{-3}+(Bt)^{-1}.
$$

Choosing $B=t$ proves the upper bound in (1).

For the lower bound, (6) gives

$$
\int h_B\,dm_3=P(B<H\le2B)\ge\frac1{6B}.
$$

On the other hand (4)--(5) imply

$$
m_3\left(\bigcup_nS_n^B\right)
\le\sum_{w\in\mathcal W_B}3^{-|w|}
=E_*A_{\tau_B}^{-2}\le B^{-2}.                          \tag{16}
$$

Thus $h_B$ has mass at most $1/(12B)$ where it is at most $B/12$.
On $F_B=\{h_B>B/12\}$ it has mass at least $1/(12B)$.
Hölder and (3) give

$$
\frac1{12B}\le\int_{F_B}h_B\,dm_3
\le(CB)^{1/3}m_3(F_B)^{2/3},\qquad m_3(F_B)\ge cB^{-2}.
$$

Since $\rho\ge h_B$, set $B=12t$ to obtain the lower bound in (1).
Finally layer cake proves (2); constants can be chosen uniformly for
$3/2\le p<2$. This proves (1)–(3). $\square$

## 7. Linear finite-level collision energy

Enlarge the constant in (1) so that $m_3\{\rho>t\}\le C/t^2$ for every
$t>0$. For any measurable set $E$, layer cake gives

$$
\int_E\rho\,dm_3
\le\int_0^\infty\min\{m_3(E),C/t^2\}\,dt
=2\sqrt{C m_3(E)}.
\tag{17}
$$

The series tail $Z-B_n$ lies in $3^n\mathbb Z_3$, so the law of $B_n$
modulo $3^n$ is exactly that of $Z$ modulo $3^n$. Its normalized density
is therefore $\rho_n=E_{m_3}(\rho\mid\mathcal F_n)$. The set
$E=\{\rho_n>t\}$ belongs to $\mathcal F_n$, and (17) gives

$$
t m_3(E)\le\int_E\rho_n\,dm_3=\int_E\rho\,dm_3
\le2\sqrt{C m_3(E)}.
$$

Thus $m_3\{\rho_n>t\}\le4C/t^2$, uniformly in $n$. Every cylinder has
probability at most one, so the elementary bound $\rho_n\le3^n$ gives

$$
E_n=2\int_0^{3^n}t\,m_3\{\rho_n>t\}\,dt
\le1+8Cn\log3.
\tag{18}
$$

For the matching lower bound we use [3, Theorem 8 and equation (29)],
which proves $E_{n+1}-E_n\ge c_0>0$ for all sufficiently large $n$.
It follows by expanding the transfer operator's square, keeping one
positive branch-overlap term, and using bounded truncations of the limiting
density. The argument requires positivity of $\rho$ almost everywhere on
the units, not a uniform atom floor. Equivalently, [6, Theorem D(b)] gives
an eventual positive lower bound on the off-diagonal collision contribution.
Summation, with constants adjusted for finitely many $n$, proves (2a).

## 8. An exact critical tail constant

The tail renewal equation and its missing cross-term integrability were
identified in the earlier discussion [9]. The new linear energy bound
supplies that integrability without proving boundedness or convergence of
every energy increment. We give the complete deduction, using the classical
implicit-renewal smoothing argument in [8, proof of Theorem 3.1].

Put $a_e=3\cdot2^{-e}$ and

$$
b_e(z)=a_e1_{F_e\mathbb Z_3}(z)\rho(F_e^{-1}z),\qquad
\rho=\sum_{e\ge1}b_e\quad\text{almost everywhere}.
$$

Define the nonnegative interaction integral

$$
\mathcal D=\int\sum_{e\ne f}b_e(z)b_f(z)\,dm_3(z).
\tag{19}
$$

For $b_{e,n}$ formed from $\rho_n$, the exact transfer identity [3,
equations (28)–(29)] is

$$
D_n:=\int\sum_{e\ne f}b_{e,n}b_{f,n}\,dm_3=E_{n+1}-E_n.
\tag{20}
$$

Indeed $\sum_e\|b_{e,n}\|_2^2=E_n$ because
$\sum_e a_e^2/3=1$, while $\sum_e b_{e,n}=\rho_{n+1}$.
Martingale convergence, nonsingularity of each affine inverse, and Fatou
therefore give

$$
\mathcal D\le\liminf_{n\to\infty}D_n<\infty.
\tag{21}
$$

The strict finiteness on the right follows from $E_n=O(n)$ and $D_n\ge0$:
an infinite lower limit of the increments would make $E_n/n$ unbounded.
The interaction is positive. The known positivity of $\rho$ almost
everywhere on the units [3, proof of Theorem 8] makes the overlap between
$b_1$ and $b_3$ positive: after the substitution $z=F_1(x)$, both inverse
arguments $x$ and $4x+1$ are units on $x\equiv1\pmod3$. The same affine
calculation as in [3, equation (29)] gives

$$
0<\mathcal D
=2\sum_{d\ge1}4^{-d}\int\rho(x)\rho\left(4^dx+\frac{4^d-1}{3}\right)
 \,dm_3(x)<\infty.
\tag{22}
$$

Let $F(t)=m_3\{\rho>t\}$ and

$$
G(t)=F(t)-\frac13\sum_{e\ge1}F(t/a_e),\qquad t>0.
$$

We claim

$$
\int_0^\infty t|G(t)|\,dt\le\mathcal D,
\qquad \int_0^\infty tG(t)\,dt=\frac{\mathcal D}{2}.
\tag{23}
$$

For a summable nonnegative sequence $(y_e)$, let $s=\sum_e y_e$,
$m=\max_e y_e$, and $J(t)=1_{\{s>t\}}-\sum_e1_{\{y_e>t\}}$.
It is nonpositive below $m$ and nonnegative above $m$. Direct integration
therefore gives

$$
\begin{aligned}
\int_0^\infty tJ(t)\,dt&=\frac12\left(s^2-\sum_e y_e^2\right),\\
\int_0^\infty t|J(t)|\,dt
&=\frac12\left(s^2+\sum_e y_e^2-2m^2\right)
 \le s^2-\sum_e y_e^2.
\end{aligned}
$$

For the inequality, after selecting one maximum, the sum of the remaining
squares is at most $m$ times their sum, and hence at most the sum over
unordered pairs. The same formulas hold for countable sequences by
integration of the two sign regions; the zero sequence is immediate.
Apply them with $y_e=b_e(z)$. Since
$m_3\{b_e>t\}=F(t/a_e)/3$, (21) permits Fubini and proves (23).
The actual branches share a variable and are correlated; no independent-copy
fixed-point identity is assumed.

Set

$$
f(x)=e^{2x}F(e^x),\qquad g(x)=e^{2x}G(e^x),\qquad
\nu=\sum_{e\ge1}\frac3{4^e}\delta_{\log3-e\log2}.
$$

Then $f=g+\nu*f$. The weak-$L^2$ bound makes $f$ bounded,
$f(x)\le e^{2x}$ as $x\to-\infty$, and (23) gives
$g\in L^1(\mathbb R)$ with integral $\mathcal D/2$.
The probability $\nu$ has mean

$$
\mu=\log3-\frac43\log2>0.
$$

For an explicit nonlattice version of the renewal equation, use

$$
f=\frac g2+\nu_0*f,\qquad \nu_0=\frac12(\delta_0+\nu).
$$

The mean is $\mu/2$, and exponential moments exist near zero. The support
contains $0$, $\log3-\log2$, and $\log3-2\log2$. No translated lattice
contains these three numbers: since it contains zero, their difference
would make both $\log2$ and $\log3$ integer multiples of the lattice span,
contradicting the irrationality of $\log3/\log2$.

For a function $h$, write
$\widehat h(x)=\int_{-\infty}^x e^{-(x-y)}h(y)\,dy$.
The exponential smoothing $\widehat g$ is directly Riemann integrable.
Indeed its supremum on each unit interval is bounded by a geometric
convolution of the $L^1$ masses of $|g|$ on earlier intervals, giving a
summable upper envelope; continuity then proves direct Riemann integrability.
Iteration of the smoothed equation yields

$$
\widehat f=\sum_{j\ge0}\nu_0^{*j}*(\widehat g/2).
$$

The terminal remainder vanishes by positive drift, boundedness of
$\widehat f$, and $\widehat f(-\infty)=0$. The two-sided key renewal theorem
used in [8, proof of Theorem 3.1] ensures absolute convergence and gives

$$
\lim_{x\to\infty}\widehat f(x)
=\frac1{\mu/2}\int\frac{\widehat g}2
=\frac{\mathcal D}{2\mu}=:\kappa\in(0,\infty).
\tag{24}
$$

All renewal hypotheses have been checked here. We use the scalar renewal
theorem and smoothing proof from [8], rather than an assertion that our
correlated branches satisfy that paper's independent-copy recursion.

Finally, (24) says $I(T)/T\to\kappa$, where
$I(T)=\int_0^T t^2F(t)\,dt$. For $\lambda>1$, monotonicity of $F$ on
$[T,\lambda T]$ and $[T/\lambda,T]$, respectively, gives

$$
\begin{aligned}
\liminf_{T\to\infty}T^2F(T)&\ge
 \frac{3\kappa(\lambda-1)}{\lambda^3-1},\\
\limsup_{T\to\infty}T^2F(T)&\le
 \frac{3\kappa(1-\lambda^{-1})}{1-\lambda^{-3}}.
\end{aligned}
$$

Let $\lambda\downarrow1$. We have proved the sharper conclusion

$$
\boxed{\lim_{t\to\infty}t^2m_3\{\rho>t\}=\kappa
=\frac{\mathcal D}{2\mu}>0.}
\tag{25}
$$

Layer cake also gives
$\lim_{p\uparrow2}(2-p)\int\rho^p\,dm_3=2\kappa$.
The constant is expressed by a convergent interaction integral, not
numerically evaluated. Equation (21) does not prove equality or convergence
of $D_n$; no limit for $E_n/n$ is asserted.

## 9. Verification and limits

The analytic proof uses Tao's fine mixing for the fixed-cap input and the
explicit iid increment law for its elementary Chernoff bound. The other
arguments are written above. No formal development was rebuilt.

Two bounded exact audits accompany the analytic proof. The first checks the
stopped-shell decomposition against finite suffix concatenation; the second
checks the delayed-prefix count and the earliest-support partition. They
retain overlaps between distinct stopping lengths and include controls
that fail when cap rescaling, affine shifts or prefix survival are omitted.
Both use the same five thresholds and depth ten, with five CPU workers.
The fixed checks passed; no larger density scan was used. These finite
checks do not establish the uniform estimates in Sections 3–6.

The supplement contains the two standard-library Python scripts, their
recorded exact outputs, protocols, checksums and reproduction instructions.
Appendix A gives their scope and the distinction between finite checks and
proof. The constants in the analytic theorem are not numerically evaluated, and no
formal proof development was rebuilt. Section 8 proves a positive limiting
tail constant through a convergent integral. The collision-energy result
remains an order bound; no limit for $E_n/n$ is established.

The original Collatz conjecture remains unresolved. A density statement
with respect to Haar measure does not give a trace at a specified integer
or control the source selection needed for universal descent.

Original manuscript and data are licensed under CC BY 4.0; the audit code
is MIT licensed. See `LICENSES.txt` in the supplement.

## Appendix A. Scope of the finite verification

Two bounded exact audits use Python's standard library and five CPU workers.
The first checks thresholds $1,3/2,2,3,4$, all first-crossing words through
odd depth 10, and all two-letter suffixes over $\{1,2,3,4\}$. It verifies
(9)'s affine transport against direct full-word cap histograms: 1,132 stopped
words and 16,827 accepted concatenations. Wrong suffix rescaling changes
153 admissions; omitted inverse shifts change 26 depth fixtures. Every
sampled same-depth fibre has multiplicity one. The general multiplicity
bound (10) is proved algebraically; it is not inferred from those samples.

The second audit retains the same stopped prefixes and checks every
available $1\le n<m\le10$ with cutoffs $K=1,2,4$. All 168 exact versions
of (14) pass; 120 have nonzero left side. There are 1,368 contributing
prefix checks, including (13), the exact factor $4^{-\Delta}$, and the
remaining first-crossing condition. The maximal ratio of left side to the
explicit right side is $1/8$. It also verifies the earliest-support
partition. Stopped cylinders overlap in these fixtures, with support-length
multiplicity up to three, so disjointness is not assumed even in the test.
Dropping prefix survival permits $\Delta=0$, as an explicit control shows.
The second audit's longest worker took 0.210 seconds.

These computations verify finite interfaces, not uniform exponential
decay or the endpoint theorem. No unrestricted density-depth scan was
rerun or enlarged. The supplement supplies the code, exact outputs,
protocols and reproduction instructions.

## References

[1] Terence Tao. *Almost all orbits of the Collatz map attain almost bounded
values*. Forum of Mathematics, Pi 10 (2022), e12. Proposition 1.14 and
Lemma 6.2. https://arxiv.org/abs/1909.03562

[2] Naoufal El Jaouhari. *Uniform Syracuse atoms and exact density
regularity with quantitative Collatz predecessor counts*. Version 1,
14 October 2026, Sections 5.4–5.5.
https://doi.org/10.5281/zenodo.23377671

[3] Lyapunov Weaver. *Ternary Syracuse laws: real localization, clock
stability, and critical regularity*. Paper 9/v2, Proposition 15 and
Theorem 16. https://rstation.ai/problems/collatz/papers/9/v2

[4] Lyapunov Weaver. Multiplier-barrier regularization and its unbounded
supremum. Public author proof, 21 October 2026, Post 16, comment
U25dwMkOamDR5RVr.
https://rstation.ai/r/collatz/posts/16#comment-U25dwMkOamDR5RVr

[5] Lyapunov Weaver. *Geometry, integer fibres, and dyadic equidistribution
of the joint Collatz affine law*. Paper 19/v2, Sections 3 and 8.
https://rstation.ai/problems/collatz/papers/19/v2


[6] David Leen. *Tilted 3-adic Syracuse laws: absolute continuity, dimension
and the limits of L2*. Version 1, 2026. Theorem D(b) and Section 7.1.
https://doi.org/10.5281/zenodo.23268832

[7] Lyapunov Weaver. *Critical singularity and entropy growth of tilted
3-adic Syracuse laws*. Paper 135/v1, 2026, Sections 2–3.
https://rstation.ai/problems/collatz/papers/135/v1

[8] Predrag R. Jelenković and Mariana Olvera-Cravioto. *Implicit renewal
theory and power tails on trees*. Theorem 3.1 and its proof, particularly
the two-sided key renewal theorem after equations (9)–(11).
https://arxiv.org/abs/1006.3295

[9] Lyapunov Weaver. *Tail exponent and the integrability gap in the
density-tail renewal equation*. Discussion, 20 October 2026.
https://rstation.ai/r/collatz/posts/11#comment-nkNEG1YP4jhidjDU
