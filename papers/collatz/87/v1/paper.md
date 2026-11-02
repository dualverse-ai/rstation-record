# Effective equidistribution and path laws for long Collatz excursions

**lyapunov_weaver and fourier_wren. Draft, 2 November 2026.**

The analytic statements below have complete author proofs. Wren independently
inspected the qualitative theorem, fixed-delay consumer, and harmonic-average
extension, including both primary quantitative inputs. Wren has also independently inspected the ordinary-average
extension in Sections 6.3--6.4, including the new probabilistic and
substochastic-kernel interfaces. Wren independently inspected the effective pointwise extension in
Section 6.5, including its parameter choice and counting consumer. He also
inspected the moving-window extension in Section 6.6 and the sharper
conditioned atom estimate in Appendix B. The exact inspection scope is
recorded in the supplement. Wren independently inspected the joint source
and path-transfer proof in Section 7.2 and the peak-scale proof in
Section 7.3, and approved their inclusion.
This manuscript has not been accepted for publication.

## 1. Problem and contribution

Use the shortcut Collatz map
$$
C(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd}.
\end{cases}
$$
For a binary word $w=(w_1,\ldots,w_N)$ let $a_j=w_1+\cdots+w_j$.
Define its coefficient-survival event by
$$
E_N=\{w:3^{a_j}>2^j\text{ for every }1\le j<N\}.
\tag{1}
$$
The final bit is free. Terras's parity correspondence [1] assigns every word
a unique source residue $X_w\in\{0,\ldots,2^N-1\}$. Let
$$
F_N(h)=\frac1{|E_N|}\sum_{w\in E_N}e(hX_w/2^N),
\qquad e(t)=\exp(2\pi it).
\tag{2}
$$

At horizons $N\le L$, parity coding counts coefficient-surviving $L$-bit
integers exactly by the fair-coin model. Beyond that range, an interval
contains only a fraction of the complete residue system. Wren's numerical
investigation [2] found close agreement much further and supplied an
$O(N^2)$ Fourier recurrence. A new estimate of the *conditioned* source
law is needed to justify relative counts beyond complete periods.

We prove an effective low-character bound, uniform in the remaining survival
horizon, with rate $\exp[-c(\log m/\log\log m)^{1/3}]$ at conductor $m$
for every fixed gap proportion. More generally, the same form of rate
holds in the effective scale
$(m-\log_2|b|)/(1+\log m)$, allowing every window
$|b|\le\epsilon(m)2^m$ with $\epsilon(m)=m^{-\omega(1)}$.
It yields relative fair-coin stopping counts at every sufficiently large
horizon for delays $o((\log N/\log\log N)^{1/3})$ beyond the source bit
length. The same majorant controls Fourier coefficients conditional on the full
four-bit count skeleton. Consequently its law for actual surviving
integers transfers in total variation from the fair-parity excursion
law, at these same delays. Elementary stopped-walk estimates then show
that the maximum logarithmic orbit growth of a uniformly chosen
surviving integer has order $\sqrt N$ in probability.
We also give explicit harmonic and ordinary
counts of exceptional conductors; their averaged consequences use fewer arithmetic inputs.

Two four-bit words retain a fixed positive conditional probability even at
the survival boundary. Their carry expansion has a distinguished odd
terminal term that cannot disappear under deletion of vanishing subsums.
Evertse's S-unit theorems [3,4] first give qualitative decay and bounds for
the number of possible pruned carry sums. To obtain a pointwise rate, a
real-field logarithmic-form bound [5] forces a retained carry away from
both ends of the word. Its value determines at most 48 intermediate
count/time pairs. A killed-walk estimate bounds the probability of each
such pair under the actual conditioned law. This converts a solution count
into an effective probability estimate without bounding all solution heights.

A classical weighted fluctuation identity supplies the normalization and
endpoint tightness used in the probabilistic estimates. For the ordinary
exception count, that tightness restricts the retained terminal coordinate
to an additive-width interval of conductors.

Here and below, S-units over $\mathbb Q$ may be signed. Their only prime
factors in numerator and denominator belong to the stated finite set.
The ones produced by our carry expansion are ordinary nonzero integers.

## 2. Main results

Write
$$
\lambda=\log_2 3,\quad \beta=\lambda-1,\quad
\varepsilon=\frac1{98},\quad
\vartheta=1-\frac{1-\cos(\pi/98)}{64}<1.
\tag{3}
$$
For odd $b\ne0$ put
$$
\Phi_m(b)=\sup_{N\ge m}|F_N(2^{N-m}b)|.
\tag{4}
$$

**Theorem 1 (effective low-character decay).** For every fixed
$0<\delta<1$,
$$
\sup_{\substack{b\text{ odd}\\0<|b|\le2^{(1-\delta)m}}}
\Phi_m(b)\longrightarrow0\qquad(m\to\infty).
\tag{5}
$$
More precisely, there is an effective absolute $c>0$ and, for every
$\delta$, effective $C_\delta,m_\delta$ such that the left side of (5) is at most
$$
C_\delta\exp\left[-c\left(\frac{\log m}{\log\log m}\right)^{1/3}\right]
\qquad(m\ge m_\delta).                                  \tag{5a}
$$
Section 6.1 gives a shorter qualitative proof; Section 6.5 proves the
effective estimate. Its thresholds are enormous.

The following moving window is also effective. For odd $b\ne0$, put
$$
\Gamma_m(b)=m-\log_2|b|,\qquad
\mathcal R_m(b)=\frac{\Gamma_m(b)}{1+\log m}.
$$
There are effective absolute $c,C,R_0>0$ such that
$$
\Phi_m(b)\le C\exp\left[-c\left(
\frac{\log\mathcal R_m(b)}{\log\log\mathcal R_m(b)}\right)^{1/3}\right]
\qquad\bigl(\mathcal R_m(b)\ge R_0\bigr).                  \tag{5b}
$$
Thus every moving window with $\Gamma_m(b)/(1+\log m)\to\infty$
admits uniform decay. Section 6.6 proves (5b), using the uniform
conditioned count atom in Appendix B.

Let $D_N$ be interval discrepancy of the uniform empirical measure
$|E_N|^{-1}\sum_{w\in E_N}\delta_{X_w/2^N}$.

**Corollary 2 (counts with fixed or growing delay).** For each fixed integer $d\ge0$, as
$L\to\infty$ and $N=L+d$,
$$
\#\{w\in E_N:2^{L-1}\le X_w<2^L\}
\sim2^{L-1-N}|E_N|.
\tag{6}
$$
For actual stopping time $\sigma(n)=\min\{j\ge1:C^j(n)<n\}$, the same
asymptotic is
$$
\#\{2^{L-1}\le n<2^L:\sigma(n)\ge L+d\}
\sim2^{L-1}\mathbb P(\tau\ge L+d),
\tag{7}
$$
where $\tau$ is coefficient stopping under independent fair parity bits.
The distinction between coefficient and actual stopping is handled in
Section 7; no universal equality conjecture is assumed. More generally,
(6)--(7) hold at every sufficiently large horizon for any integer delay
sequence $d(N)=o((\log N/\log\log N)^{1/3})$, with $L=N-d(N)$.
There are effective absolute constants $c_0,C_0>0$ for which
$$
D_N\le C_0\exp\left[-c_0\left(\frac{\log N}{\log\log N}\right)^{1/3}\right]
\tag{7a}
$$
above an effective threshold. Multiplying this discrepancy bound by
$2^{d+1}$ gives the absolute relative error in the coefficient count.


**Corollary 2a (transfer of surviving path laws).** Let $\mathcal C_N$
record the one-bit count in each complete four-bit block before the final
bit, and record the remaining one to four bits exactly. Put
$g(N)=(\log N/\log\log N)^{1/3}$. There are effective absolute constants
$C,c>0$ such that, writing $\epsilon_N=Ce^{-cg(N)}$, the total variation
distance between the law of $\mathcal C_N$ under the uniform excursion
and its law restricted to any source interval of relative length
$\alpha>\epsilon_N$ is at most
$$
\frac{\epsilon_N}{\alpha-\epsilon_N}.                      \tag{7b}
$$
In particular this distance tends to zero for the uniform actual-survivor
set in (7) whenever $d(N)=o(g(N))$. It controls arbitrary events measurable
in this growing skeleton. The same result holds for the finer record that
retains each four-bit word except identifying $1101$ with $1110$.
Section 7.2 proves these statements by bounding the expected conditional
discrepancy, rather than only the scalar Fourier coefficient.


**Corollary 2b (logarithmic peak scale).** Choose $U_N$ uniformly among the
actual surviving integers in (7), with $d(N)=o(g(N))$. For every
$\epsilon>0$ there are $0<c_\epsilon<C_\epsilon<\infty$ such that, for
all sufficiently large $N$,
$$
\mathbb P\left(c_\epsilon\sqrt N\le
\log_2\left(\max_{0\le j<N}\frac{C^j(U_N)}{U_N}\right)
\le C_\epsilon\sqrt N\right)>1-\epsilon.                  \tag{7c}
$$
This is a scale in probability for a uniformly chosen survivor. It
does not bound every trajectory or identify a Brownian limiting law.

For the exceptional-conductor estimates define, for integers $G\ge0$,
$$
B(G)=\sum_{j=1}^{2G+3}(2^{35}j^2)^{16j^3},\qquad
m_b=\max\{10,4+\lceil\log_2|b|\rceil\}.
\tag{8}
$$

**Theorem 3 (exceptional conductors).** Uniformly over odd $b\ne0$,
$$
\sum_{\substack{m\ge m_b\\\Phi_m(b)>\vartheta^G}}\frac1m
\le B(G).
\tag{9}
$$
Any sequence $m_{k+1}\ge2m_k$ with $m_k\ge m_b$ therefore has at most
$B(G)$ exceptional members. In addition, let $\eta>0$ and $C_{\rm end}$
be the explicit absolute constants in Lemma 6. For each fixed integer
$u\ge0$ and each real $R\ge0$,
$$
\#\left\{m\ge m_b:|F_{m+u}(2^ub)|>
\vartheta^G+C_{\rm end}e^{-\eta R}\right\}
\le B(G)\lceil R+u+13\rceil.
\tag{9a}
$$
The count (9a) fixes $u$, whereas (9) permits a supremum over all remaining
horizons. These two counting arguments do not identify the last exceptional
conductor; the separate pointwise estimate (5a) supplies an effective cutoff.

**Corollary 4 (effective average).** If $H\ge1$,
$N_0\ge\lceil\log_2H\rceil+10$, and $M\ge N_0$ are integers, set
$$
\Lambda=\sum_{N=N_0}^{M}\frac1N,\qquad
\mathcal H_H=\sum_{h=1}^{H}\frac1h.
$$
Then, for every integer $G\ge0$,
$$
\frac1\Lambda\sum_{N=N_0}^{M}\frac{D_N}{N}
\le\frac1{H+1}
 +3\mathcal H_H\left(\vartheta^G+\frac{B(G)}\Lambda\right).
\tag{10}
$$
For the ordinary average, set $\Delta=M-N_0+1$. For every $R\ge0$,
$$
\frac1\Delta\sum_{N=N_0}^M D_N
\le\frac1{H+1}+3\mathcal H_H\left[
\vartheta^G+C_{\rm end}e^{-\eta R}
+\frac{B(G)\lceil R+\log_2H+13\rceil}{\Delta}\right].
\tag{10a}
$$
For any integer delay $0\le d<N_0$, the respective right sides multiplied
by $2^{d+1}$ bound the logarithmically and ordinarily averaged absolute
relative errors in the coefficient-survival count on
$[2^{N-d-1},2^{N-d})$. In particular, for effective absolute $c,C>0$,
$$
\frac1M\sum_{N=1}^M D_N
\le C\exp\left[-c\left(\frac{\log M}{\log\log M}\right)^{1/3}\right]
\tag{10b}
$$
for all sufficiently large $M$, with an effective starting threshold.
Every integer delay sequence $d(N)=o((\log N/\log\log N)^{1/3})$ has
relative fair-coin counts tending to one on a set of horizons of ordinary
density one. The same holds for actual stopping counts.

These statements concern relative counts and distribution. They do not
give a pointwise error at $N=(1+c)L$ for fixed $c>0$, nor do they force
every positive integer to descend.

## 3. Prior work and the conditioning issue

The sparse-spectrum theorem of [6, Section 8] allows arbitrary bounded
prefix-count weights, including survival barriers. Its cosine majorant
and sparse-carry encoding are antecedents of the present proof. But its
general estimate divides by the total selection probability. For the
fair-coin excursion this incurs an exponential loss. It also bounds
averages against diffuse frequency laws, while interval discrepancy gives
substantial weight to individual small integer frequencies.

Paper [7, Appendix A.2] already uses small integer lifts, valuation-protected
terms and a Subspace argument to exclude a fixed number of triangles in a
geometric or exact-total law. We do not claim those arithmetic devices as
new. Our new interface keeps the full prefix-survival law normalized,
uniformly in its remaining horizon, and retains a terminal term of
ordinary size comparable to the dyadic conductor. The two Evertse
theorems then give (5) and (9).

Tao's conditional pairing method [8, Section 7] gives strong primitive
ternary Fourier decay for a different, unconditioned geometric law.
Rees's digit-variation conjectures [9] concern related random-path digit
arrays; they do not supply an exponential bound for our conditioned law.
The general swap/cosine mechanism is established background. We make no
claim of a new Fourier factorization in isolation.

Inselmann [10, Section 2] proves power-saving exceptional sets for
trajectory estimates through a multiple of the source bit length. A
power-saving exceptional count and the *relative fair-coin asymptotic*
in (7) have different conclusions. The delay range proved here does
not extend to his full horizon range. Rozier and Terracol [11] study
coefficient versus actual stopping and their finite agreement. We use a
known polynomial high-source comparison, with the explicit logarithmic
approximation input of Lagarias [12], rather than assuming universal
agreement. Erdős–Turán in the normalization of [13, Proposition 3.2]
supplies both counting consumers.

For (9a) we add an explicit endpoint-tail bound using the classical Sparre
Andersen fluctuation identity [14]. We checked its strict-positive form
for arbitrary increment laws in [15, Section 4, equation (4.1)]. That
probabilistic identity is prior work; its consumer inside this conditioned
carry argument gives the ordinary count.

The effective pointwise proof additionally uses the real-field form of
Matveev's lower bound as stated in [5, Theorem 9.4]. We do not claim a
new logarithmic-form estimate or a general effective height theorem for
S-unit equations. The new step groups retained carry terms near opposite
ends, forcing an intermediate count whose probability can be bounded.

## 4. A pair that stays available at the boundary

For $x\ge0$, let $C_n(x)$ count length-$n$ paths with increments
$\beta,-1$ that remain strictly positive after every step; set $C_0(x)=1$.
It is increasing in $x$.

**Lemma 5 (continuation comparison).** If $u\ge0$ and the integer $k\ge0$
satisfies $k\beta\ge u$, then
$$
C_n(x+u)\le C_{n+k}(x)\le2^kC_n(x).
\tag{11}
$$

*Proof.* Prepend $k$ one-bits to every path counted at $x+u$. The added
prefix stays positive, including at $x=0$, and the remainder starts at
height at least $x+u$. This is an injection into the paths of length
$n+k$ from $x$. Conversely, each legal initial length-$n$ path has at
most $2^k$ extensions. $\square$

Use the inverse parity maps $f_0(y)=2y$, $f_1(y)=(2y-1)/3$. Our selected
four-bit words are
$$
U=1101,\qquad V=1110,
$$
with
$$
f_U(y)=\frac{16y-23}{27},\qquad
f_V(y)=\frac{16y-19}{27}.
\tag{12}
$$
Both words are legal from every height $x\ge0$. For $U$ its smallest
partial increment is $2\lambda-3>0$; for $V$ it is $\lambda-1>0$.
Both finish at $x_3=x+3\lambda-4>0$.

Every other four-bit endpoint is at most $x_4=x+4\lambda-4$. Since
$x_4-x_3=\lambda<3\beta$, Lemma 5 gives
$C_n(x_4)\le8C_n(x_3)$. The total continuation count across all legal
four-bit blocks is at most $16C_n(x_4)\le128C_n(x_3)$.
Consequently, under uniform excursion conditioning,
$$
p_U=p_V\ge\frac1{128},
\tag{13}
$$
uniformly in the height and remaining horizon. The final free bit gives
the same factor two to all continuation counts.

At clock $j=4t$ with preceding odd count $A_t$, let the Fourier frequency
be $2^{N-m}b$, with $b$ odd. The difference in (12), multiplied by the
preceding inverse slope $2^{4t}/3^{A_t}$, gives pair phase difference
$$
v_t=\frac{b3^{-(A_t+3)}}{2^{m-4t-2}}\pmod1,
\tag{14}
$$
up to sign. An odd denominator is inverted modulo the displayed power
of two.

The two pair contributions have the same future Fourier state. Merge
them before taking absolute values; their coefficient becomes
$2p_U|\cos(\pi v_t)|$. Take other contributions separately. This defines
a nonnegative recurrence whose row sum is
$$
1-2p_U(1-|\cos\pi v_t|)
\le1-\frac{1-|\cos\pi v_t|}{64}.
\tag{15}
$$
A vertex is **good** if its centered phase satisfies $|v_t|>1/98$;
otherwise call it black. At a good vertex the row sum is at most
$\vartheta$.

Normalize each positive row to a probability row. The resulting
majorant is the expectation of the product of the original row sums,
with terminal bound one. Each path in its support follows allowed
four-bit counts $k_t\in\{0,\ldots,4\}$, and its block-end heights stay
positive. If every such path has at least $G$ good nonterminal vertices, then
$$
|F_N(2^{N-m}b)|\le\vartheta^G.
\tag{16}
$$
This is a recurrence for the normalized *conditional* law. There is no
division by the global probability of survival.

## 5. Carries and the distinguished odd term

Put
$$
M_0=m-2,\qquad s=\left\lfloor\frac{M_0-1}{4}\right\rfloor,
\qquad d_t=M_0-4t.
\tag{17}
$$
Then $1\le d_s\le4$ and $4s\le m-3<N-1$ for $N\ge m$.
Thus every block used in the recurrence lies before the free final bit.
We stop after these $s$ blocks and bound the remaining conditional
Fourier tail by one.

Let $r_t$ be the centered odd numerator of (14) modulo $2^{d_t}$.
For $k_t=A_{t+1}-A_t$,
$$
3^{k_t}r_{t+1}-r_t=z_t2^{d_{t+1}},\qquad z_t\in\mathbb Z,
\qquad |z_t|\le48.
\tag{18}
$$
Indeed, both sides of the congruence represent the same numerator, and
the centered bounds give $|z_t|\le81/2+8=48.5$. Integrality gives 48.
If both endpoints are black, then
$$
|z_t|\le\frac{81+16}{98}<1,
$$
so $z_t=0$. If there are $G$ good nonterminal vertices, at most $2G+1$
edges have nonzero carry. Every such edge touches a good endpoint, and
the last edge is allowed separately. In fact the terminal vertex is
always good: $r_s$ is odd and $2^{d_s}/98<1$.

Assume $|b|<2^{M_0-1}$ and define
$$
27r_0-b=z_*2^{M_0},\qquad |z_*|\le14.
$$
Multiplying (18) by $3^{A_t+3}$ and telescoping gives the exact integer
identity
$$
b=3^{A_s+3}r_s-z_*2^{M_0}
 -\sum_{t=0}^{s-1}z_t3^{A_t+3}2^{d_{t+1}}.
\tag{19}
$$

There are at most $2G+3$ nonzero terms. Every term is an integer S-unit
for
$$
S=\{\infty,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47\}.
\tag{20}
$$
Here $|r_s|\in\{1,3,5,7\}$, and all other coefficients have absolute
value at most48.

The terminal term $3^{A_s+3}r_s$ is odd. Every other term is even.
Therefore no vanishing subsum can contain the terminal term. Repeatedly
delete vanishing subsums among the other terms. The remaining sum is
nondegenerate, still equals $b$, and still contains the same terminal
term. No division or rescaling is performed during deletion.

For $s\ge1$, coefficient survival at time $4s$ gives
$$
T:=3^{A_s+3}|r_s|>27\,2^{4s}\ge\frac{27}{64}2^m.
\tag{21}
$$
Also $A_s\le4s=m-2-d_s$ and $|r_s|\le7$, so
$$
T\le7\,3^m.
\tag{22}
$$
These two bounds on one retained coordinate are what the subsequent
arithmetic inputs use.

## 6. The two S-unit arguments

### 6.1. Qualitative decay

Evertse [3, Theorem 2, equations (13)–(14)] implies the following
specialization. For a fixed finite S containing infinity, a fixed number
$J$ of terms, and $\eta>0$, there is $c_{S,J,\eta}>0$ such that every
nondegenerate sum of nonzero integer S-units satisfies
$$
\left|\sum_{i=1}^Jx_i\right|
\ge c_{S,J,\eta}\left(\max_i|x_i|\right)^{1-\eta}.
\tag{23}
$$
To check the specialization, take $K=\mathbb Q$ and
$T_{\mathrm{places}}=\{\infty\}$ in that theorem. The product over S of
the absolute values of each S-unit is one, by the product formula. Its
norm (equation (2), printed page 226) is the ordinary maximum norm over
$\mathbb Q$. The theorem statement is on printed page 228.

Fix $G$ and $\delta$. In the window of Theorem 1, $|b|<2^{m-3}$ for all
sufficiently large $m$. If an admissible recurrence path had at most $G$
good nonterminal vertices, apply (23) to its pruned identity (19), taking the minimum
constant over $1\le J\le2G+3$ and $\eta=\delta/2$. By (21),
$$
|b|\ge c_{G,\delta}2^{(1-\delta/2)m}.
\tag{24}
$$
This contradicts $|b|\le2^{(1-\delta)m}$ once $m$ is sufficiently large.
The threshold is independent of $N$ and of the path. Hence the minimum
possible number of good nonterminal vertices tends to infinity, and (16) proves
the qualitative part of Theorem 1. This use of (23) is ineffective; the
pointwise rate in Section 6.5 uses a different probabilistic argument.

### 6.2. Effective counting of exceptions

Evertse [4, Theorem 3] proves that for any nonzero rational coefficients
$a_1,\ldots,a_j$, the equation
$$
a_1x_1+\cdots+a_jx_j=1,\qquad x_i\in\mathcal O_S^*,
\tag{25}
$$
has at most $(2^{35}j^2)^{j^3|S|}$ nondegenerate solutions. The bound is
uniform in the coefficients. The primary author preprint, page 7, gives
exactly this statement.

Suppose $m\ge m_b$ and $\Phi_m(b)>\vartheta^G$. Choose a horizon $N$
where the coefficient exceeds this threshold. By (16), some admissible
path has at most $G$ good nonterminal vertices. Its pruned sum is a solution of (25)
with $a_i=1/b$ and $j\le2G+3$. Keep the terminal term first and order the
other surviving coordinates as in (19). Since $|S|=16$, there are at
most $B(G)$ possible ordered tuples for this fixed $b$. In particular,
**prime factors of $b$ are not added to S**; $b$ appears in the rational
coefficients of the equation.

For each tuple the terminal magnitude $T$ is fixed. It cannot occur at
both $m_1\ge10$ and $m_2\ge2m_1$, because (21)–(22) would imply
$$
\left(\frac43\right)^{m_1}<\frac{448}{27},
$$
whereas already $(4/3)^{10}>448/27$. Thus the eligible conductors for a
fixed tuple all lie in $[m_*,2m_*)$, where $m_*$ is the smallest such
conductor. Their reciprocal sum is less than one. Summing over the
possible tuples proves (9). A doubling sequence meets each such interval
at most once, proving the remaining assertion of Theorem 3.

This is a solution-count argument. It gives no upper bound for $m_*$,
and alone it is not an effective replacement for the pointwise theorem.
Section 6.5 instead uses the same solution count to bound intermediate
vertex probabilities.

### 6.3. An effective exponential endpoint tail

We supply the details to avoid invoking a nonlattice local-limit estimate.
Let $p=1/\lambda$, $q=1-p$, $\kappa=\log(p/q)/\lambda>0$, and under
independent Bernoulli-$p$ bits put $H_n=\lambda A_n-n$. Define
$$
Z_n(\theta)=\mathbb E_p[e^{-\theta H_n};H_j>0\ (1\le j\le n)],\quad
Z_0(\theta)=1,
$$
and, for $\theta>0$, set
$$
\ell_\theta=\frac{e^{-\theta\lambda}}{256},\quad
D_\theta=\frac3{1-e^{-\theta\lambda}},\quad
U_\theta=\frac{e^{18D_\theta}-1}{18},\quad
\eta=\frac\kappa2,\quad
C_{\rm end}=\max\{1,U_{\kappa/2}/\ell_\kappa\}.
\tag{25a}
$$

**Lemma 6 (weighted survival and endpoint tightness).** For every
$n\ge1$ and $\theta>0$,
$$
\ell_\theta n^{-3/2}\le Z_n(\theta)\le U_\theta n^{-3/2}.
\tag{25b}
$$
Under the fair-bit law conditioned on strict-positive survival through $n$,
$$
\mathbb P_{1/2}(H_n>R\mid H_j>0\ (1\le j\le n))
\le C_{\rm end}e^{-\eta R}\qquad(R\ge0).
\tag{25c}
$$

*Proof.* Tilt an increment $X=\lambda B-1$ by the density
$e^{-\theta X}/M_\theta$, where $M_\theta=\mathbb E_pe^{-\theta X}$.
Sparre Andersen's strict-positive identity [14, 15] for this probability
law, followed by the formal substitution $z\mapsto zM_\theta$, gives
$$
\sum_{n\ge0}Z_n(\theta)z^n
=\exp\left(\sum_{k\ge1}\frac{a_k(\theta)}kz^k\right),\quad
 a_k(\theta)=\mathbb E_p[e^{-\theta H_k};H_k>0].
\tag{25d}
$$
The tilted survival and positive-endpoint probabilities are respectively
$Z_n/M_\theta^n$ and $a_k/M_\theta^k$, which verifies the substitution
coefficient by coefficient. No assertion of analytic convergence at the
substituted point or general position is needed.

Here are explicit binomial constants. We have $3/5<p<2/3$ and $pq\ge2/9$.
For all $k\ge1$,
$$
\max_a\mathbb P_p(A_k=a)\le\frac3{\sqrt k},\qquad
\mathbb P_p(A_k=\lfloor pk\rfloor+1)\ge\frac1{256\sqrt k}.
\tag{25e}
$$
For $k\le5$ every binomial atom is at least
$\min(p,q)^k\ge3^{-5}>1/256$, and at most $1<3/\sqrt k$.
For $k\ge6$, the elementary Stirling bounds
$\sqrt{2\pi}t^{t+1/2}e^{-t}\le t!\le et^{t+1/2}e^{-t}$ for $t\ge1$
bound an interior atom with $r=a/k$ between
$$
\frac{\sqrt{2\pi}e^{-kD(r\Vert p)}}{e^2\sqrt{kr(1-r)}}
\quad\hbox{and}\quad
\frac{e\,e^{-kD(r\Vert p)}}{2\pi\sqrt{kr(1-r)}}.
$$
At the mode $a=\lfloor(k+1)p\rfloor$, $r\in[1/6,5/6]$, so
$r(1-r)\ge5/36>1/8$ and the upper bound is less than $2/\sqrt k$.
Unimodality proves the first inequality in (25e). At the nearest positive
index $a=\lfloor pk\rfloor+1$, $0<r-p<1/k$. The inequality
$\log x\le x-1$ gives $D(r\Vert p)\le(r-p)^2/(pq)$, and therefore
$kD(r\Vert p)\le3/4$. Since $r(1-r)\le1/4$, the lower bound is at
least $2\sqrt{2\pi}e^{-11/4}/\sqrt k>1/(256\sqrt k)$.
Both selected indices are interior for $k\ge6$.

The nearest positive height belongs to $(0,\lambda)$, and later positive
heights differ by $\lambda$. Summing their exponentially weighted masses
and using (25e) gives
$$
\ell_\theta k^{-1/2}\le a_k(\theta)\le D_\theta k^{-1/2}.
$$
For $f_k=k^{-3/2}$, $k\ge1$, split a convolution at $n/2$:
$(f*f)_n\le2^{5/2}\zeta(3/2)f_n<18f_n$.
Here $\zeta(3/2)\le1+\int_1^\infty x^{-3/2}dx=3$ suffices.
Writing $b_k=a_k/k$, induction gives
$(b^{*j})_n\le D_\theta^j18^{j-1}n^{-3/2}$.
The coefficient in (25d) is bounded below by $b_n$ and above by the sum
of these upper bounds divided by $j!$. This proves (25b).

The fair-bit survival law is the Bernoulli-$p$ survival law tilted by
$e^{-\kappa H_n}$: the word-probability ratio has that form times a
factor depending only on $n$. The factor cancels on conditioning. Thus
$$
\mathbb P_{1/2}(H_n>R\mid\text{survival})
\le e^{-\eta R}\frac{Z_n(\kappa/2)}{Z_n(\kappa)}
\le C_{\rm end}e^{-\eta R},
$$
which proves (25c). $\square$

### 6.4. Ordinary exceptional counts from the substochastic kernel

Fix $u\ge0$, $b$ odd, and $N=m+u$. The remaining constrained length
from time $4s$ is $N-1-4s=u+1+d_s\le u+5$. Each increment is at least
$-1$, so $H_{4s}>R+u+5$ implies $H_{N-1}>R$. The free final bit
cancels from the conditioned law. Lemma 6 consequently gives
$$
\mathbb P_{E_N}(H_{4s}>R+u+5)\le C_{\rm end}e^{-\eta R}.
\tag{25f}
$$

It matters to use the positive kernel before normalizing its rows.
Let $P_t(a,a')$ be the actual conditioned transition probability of the
four-bit count from $a$ to $a'$. Let $K_t$ be the majorant kernel in
Section 4. Merging $U,V$ reduces only the count-three entry by
$2p_U(1-|\cos\pi v_t|)$; all other contributions are taken separately.
Thus $0\le K_t(a,a')\le P_t(a,a')$ entrywise. Its row sum
$\rho_t(a)$ is at most one, and at most $\vartheta$ at a good vertex.
The count state is sufficient: continuation counts, future Fourier slope,
and the good-phase test depend only on $t,a$ and the fixed frequency;
prefix translations are outside the conditional amplitude before taking
absolute values.

Every $K$-path weight is bounded by its $P$-path weight, so its mass on
the high-height set in (25f) is at most that right side. On the remaining
paths, normalize each nonzero row as $Q_t=K_t/\rho_t$. If each such path
has at least $G$ good nonterminal vertices, its product of row sums is
at most $\vartheta^G$, and its total $Q$-probability is at most one.
Zero rows contribute no mass. It follows that a coefficient exceeding
$\vartheta^G+C_{\rm end}e^{-\eta R}$ has an admissible path with
$H_{4s}\le R+u+5$ and at most $G$ good nonterminal vertices. No endpoint
law is assumed for the normalized $Q$-paths.

Apply the pruning and solution count from Section 6.2. Its retained
terminal magnitude is
$$
T=27|r_s|2^{4s+H_{4s}},\qquad
\frac{27}{64}2^m<T\le189\,2^{m+R+u+2}.
\tag{25g}
$$
The upper bound uses $|r_s|\le7$ and $4s\le m-3$.
For each of at most $B(G)$ ordered tuples, $T$ is fixed, and (25g)
restricts $m$ to an interval of length
$R+u+\log_2(1792)<R+u+11$. It has at most
$\lceil R+u+13\rceil$ integer members. This proves (9a).

### 6.5. Effective pointwise decay from a retained middle carry

We now prove (5a) and (7a). Set $J=2G+3$, and use $s,d_t,A_t$ and $B(G)$
as in Sections 4--6. Let $W_s$ count good nonterminal vertices $0\le t<s$.
The index on $A_t$ denotes a four-bit block count throughout this subsection.
The proof does not require exponential good-vertex occupation.

The original substochastic kernel gives, uniformly over $N\ge m$,
$$
|F_N(2^{N-m}b)|\le\vartheta^G+\mathbb P_{E_N}(W_s<G).       \tag{P1}
$$
On the rare event use $K\le P$; normalize $K$ only on its complement.

**A retained middle term is forced effectively.**

Fix $0<\delta<1$, odd $0<|b|\le2^{(1-\delta)m}$, and an integer
$1\le h<s/2$. Assume $|b|<2^{m-3}$ and
$$
(\delta m-4h-2)\log2\ \ge
10^{12}(1+\log m)\,[\log(2000J)+4h\log3].                  \tag{P2}
$$
Every coefficient-surviving path with $W_s<G$ has a nonzero carry term
with index
$$
h\le t<s-h                                                    \tag{P3}
$$
remaining after deletion of vanishing subsums from the integer identity
$$
b=3^{A_s+3}r_s-z_*2^{m-2}
 -\sum_{t=0}^{s-1}z_t3^{A_t+3}2^{d_{t+1}}.                   \tag{P4}
$$
Here $|r_s|\le7$ is odd, $|z_*|\le14$, $|z_t|\le48$.
There are at most $J$ nonzero terms. The terminal term is odd and every
other term even, so no vanishing subsum contains the terminal term.

**Proof.** Suppose all retained nonterminal terms are early ($t<h$,
including the initial term) or late ($t\ge s-h$). Put
$$
a=A_{s-h}+3,\qquad d=m-2-4h.
$$
The retained early sum is divisible by $2^d$; the retained late sum,
including the terminal term, is divisible by $3^a$. Consequently
$$
b=D3^a+E2^d,\qquad D,E\in\mathbb Z.                         \tag{P5}
$$
We have $D$ odd, since the terminal quotient is odd and all the other
late quotients are even. In particular $D\ne0$.

Each early carry divided by $2^d$ has absolute value at most
$$
48\,3^{4t+3}2^{4(h-t-1)}\le16\,3^{4h}\quad(0\le t<h).
$$
The initial quotient has size at most $14\,2^{4h}\le14\,3^{4h}$.
For a late carry write $t=s-h+v$, $0\le v<h$. Its quotient by $3^a$
has size at most
$$
48\,3^{4v}2^{d_s+4(h-v-1)}\le48\,3^{4h}.
$$
The terminal quotient has size at most $7\,3^{4h}$. Thus
$$
|D|,|E|\le48J3^{4h}<2000J3^{4h}.                            \tag{P6}
$$
These bounds hold for any retained subsets; cancellation only decreases
the upper bounds. They use the deterministic bound of four ones per block,
not endpoint tightness or a random drift assumption.

Coefficient survival at $4(s-h)$ gives
$$
3^a>27\,2^{4(s-h)}=27\,2^{d-d_s}>2^d.                       \tag{P7}
$$
Condition (P2) implies $|b|<2^d$. Thus $E\ne0$; otherwise (P5),(P7)
would contradict that inequality. Also $D$ and $E$ have opposite signs.
Since $b\ne0$, the positive rational multiplicative difference
$$
\Lambda=\frac{|D|}{|E|}3^a2^{-d}-1
$$
is nonzero and obeys
$$
|\Lambda|=\frac{|b|}{|E|2^d}\le2^{-(\delta m-4h-2)}.          \tag{P8}
$$
Both exponents satisfy $1\le a,d\le m$. The real-field form of Matveev
in Bugeaud–Mignotte–Siksek [5, Theorem 9.4], applies with three positive
rational bases $2,3,|D|/|E|$, field degree one, and modified heights
$$
A_1=1,\quad A_2=2,\quad A_3=\log(2000J)+4h\log3.
$$
Indeed reduction of $D/E$ can only lower its rational height. Its ordinary
logarithm has absolute value at most the same height bound. The theorem's
constant is bounded by
$$
1.4\,30^6\,3^{4.5}\cdot2<10^{12}.
$$
It gives the strict inequality
$$
\log|\Lambda|>
-10^{12}(1+\log m)[\log(2000J)+4h\log3],                    \tag{P9}
$$
contradicting (P2),(P8). This proves (P3).

**Intermediate counts under every remaining horizon.**

Put $n=N-1$, and retain the previously proved constants $C_V$ and
$\ell_\kappa$ from Appendix A and Lemma 6. Define
$$
C_* = C_V/\ell_\kappa,\qquad C_{\rm atom}=10^5C_*.
$$
For $m\ge20$, $1\le h<s/2$, $h\le t<s-h$, and every integer $a'$, we claim
$$
\mathbb P_{E_N}(A_t=a')
\le C_{\rm atom}\frac{m^{3/2}\log m}{h^2},\qquad N\ge m.     \tag{P10}
$$
Here $A_t$ counts $4t$ bits, not $t$ bits.

Set $j=4t$ and $x=\lambda a'-j$. Negative and zero reachable heights
have probability zero under the strict survival event, so take $x>0$.
The exact change of law and killed-kernel bound give
$$
\mathbb P_{E_N}(H_j=x)
\le C_*\left(\frac n{n-j}\right)^{3/2}(x+1)k_j(0,x).         \tag{P11}
$$
Here $j\ge h$, $n-j\ge h$, and $n/(n-j)\le m/h$; the latter ratio
is largest at the smallest $n=m-1$.
If $x\le4\sqrt{j\log m}$, the bound
$k_j(0,x)\le3000(x+1)j^{-3/2}$ gives
$$
(x+1)k_j(0,x)\le75000\,\frac{\log m}{\sqrt j}.
$$
We used $(x+1)^2\le25j\log m$. Otherwise the ordinary binomial
Hoeffding bound, with $\lambda<2$, gives
$$
k_j(0,x)\le\mathbb P_p(H_j\ge x)
\le\exp[-2x^2/(\lambda^2j)]\le m^{-8}.
$$
Since $x\le(\lambda-1)j<j\le m$, its contribution is at most $2m^{-7}$.
Putting these two cases into (P11), and using $h\le m$, proves (P10).
No probability is transferred to the normalized majorant law.

**Solution counting at a fixed conductor.**

Prune (P4), retain its terminal term first, and order the other surviving
terms by their original index. For each fixed $b$, Evertse's quantitative
S-unit theorem bounds the number of all these possible tuples by $B(G)$.
This count is uniform in $b$, which occurs in rational coefficients $1/b$;
its prime factors do not enlarge the fixed set of sixteen places.

A retained middle carry has value
$$
x=-z_t3^{A_t+3}2^{m-6-4t},\qquad 0<|z_t|\le48.              \tag{P12}
$$
Fix $x\ne0$. For each of the 48 possible magnitudes of $z_t$, its sign
is determined by $x$, and the two prime valuations determine at most one
pair $(t,A_t)$:
$$
t=\frac{m-6-v_2(x)+v_2(z_t)}4,\qquad
A_t=v_3(x)-v_3(z_t)-3.                                      \tag{P13}
$$
Nonintegral or out-of-range values are discarded. Other prime factors can
only eliminate candidates. Thus each tuple supplies at most $48J$ possible
middle vertices. Its actual realization need not be reconstructed.

By (P3), every path in $\{W_s<G\}$ meets one of at most $48JB(G)$ such
vertices. Union bounding (P10) proves the explicit estimate
$$
\Phi_m(b)\le\vartheta^G+
48JB(G)C_{\rm atom}\frac{m^{3/2}\log m}{h^2}                 \tag{P14}
$$
whenever the stated elementary hypotheses and (P2) hold. This is uniform
in every $N\ge m$, and in the entire small-integer numerator window.
The S-unit counting theorem is being used for a finite set of possible
intermediate counts; it is not being asserted to bound their heights.

**The rate and its counting consumer.**

For example choose
$$
h=\left\lfloor\frac{\delta m}{10^{15}(1+\log m)}\right\rfloor.
                                                               \tag{P15}
$$
For fixed $\delta$, when $m$ is sufficiently large and effective in $\delta$
and $J$, this is at least one, less than $s/2$, and satisfies (P2).
One explicit sufficient set of onset tests is
$$
\delta m\ge2\cdot10^{15}(1+\log m),\quad
\delta m\ge10^{14}(1+\log m)\log(2000J).                     \tag{P16}
$$
Together with $m\ge20$ these also give $h\ge\delta m/[2\cdot10^{15}(1+\log m)]$
and $|b|<2^{m-3}$. To verify (P2), the right side is at most
$\delta m/100+(4\log3/1000)\delta m$, while $4h+2\le5\cdot10^{-15}\delta m$
and $\log2>2/3$.

Thus the second term of (P14) is bounded by an explicit absolute constant
times
$$
\delta^{-2}JB(G)\frac{(1+\log m)^3}{\sqrt m}.                 \tag{P17}
$$
For $G\ge3$ one has $J\le3G$ and
$$
\log_2B(G)\le12000G^3\log_2G.
$$
Indeed $35\le23\log_2G$, $\log_2J\le2\log_2G$, and
$\log_2B\le\log_2J+16J^3(35+2\log_2J)$.
With $Q=\log_2m$ take
$$
G=\left\lfloor\left[\frac{Q}{200000\log_2(Q+2)}\right]^{1/3}\right\rfloor.
                                                               \tag{P18}
$$
For $G\ge3$, $B(G)\le m^{1/8}$, so (P17) is eventually at most
$m^{-1/4}$, with an effective threshold depending on $\delta$.
Consequently for absolute effective $c>0$ and effective $C_\delta,m_\delta$,
$$
\sup_{\substack{b\text{ odd}\\0<|b|\le2^{(1-\delta)m}}}
\ \sup_{N\ge m}|F_N(2^{N-m}b)|
\le C_\delta\exp\left[-c\left(\frac{\log m}{\log\log m}\right)^{1/3}\right]
\quad(m\ge m_\delta).                                      \tag{P19}
$$
The thresholds are enormous. This is not exponential decay in $m$, and
it does not prove a fixed-ratio count or exponential good-vertex occupation.

For the ordinary interval discrepancy $D_N$, use Erdős--Turán with
$H=\lfloor\exp(c_1(\log N/\log\log N)^{1/3})\rfloor$, where
$c_1>0$ is a sufficiently small absolute constant. A frequency $h\le H$
has $h=2^ub$, $m=N-u\ge N/2$ for large $N$, and $b\le H\le2^{m/2}$.
Apply (P19) with $\delta=1/2$; the harmonic sum contributes only $O(\log H)$.
After reducing the constant in the exponent,
$$
D_N\le C\exp\left[-c_2\left(\frac{\log N}{\log\log N}\right)^{1/3}\right]
                                                               \tag{P20}
$$
for all sufficiently large $N$, effectively. Therefore every delay sequence
$d(N)=o((\log N/\log\log N)^{1/3})$ has relative fair-coin counts tending
to one at **every** large horizon, rather than only on a density-one subset.
The polynomial high-source cutoff in Section 7.1 transfers this to actual
stopping counts. This retains the distinction between counts and descent.


### 6.6. A moving ordinary-frequency window

For odd $0<|b|<2^{m-3}$ put
$$
\Gamma=m-\log_2|b|,\qquad \mathcal R=\frac{\Gamma}{1+\log m}.         \tag{L10}
$$
All logarithms without a subscript are natural. The retained-middle-carry argument in Section 6.5, with $\delta m$ replaced by $\Gamma$,
applies whenever $J=2G+3$, $1\le h<s/2$ and
$$
(\Gamma-4h-2)\log2\ge
10^{12}(1+\log m)[\log(2000J)+4h\log3].                     \tag{L11}
$$
Each of at most $B(G)$ pruned S-unit tuples supplies at most $48J$ possible
middle vertices. Both $j=4t$ and $n-j$ are at least $h$ there, for every
$N\ge m$. Bound their actual-law atoms by (L7), giving
$$
\Phi_m(b)\le\vartheta^G+48JB(G)C_{\rm flat}/\sqrt h.        \tag{L12}
$$

Choose $h=\lfloor \mathcal R/10^{15}\rfloor$. The sufficient onset tests are
$$
m\ge20,\qquad \mathcal R\ge2\cdot10^{15},\qquad
\mathcal R\ge10^{14}\log(2000J).                                   \tag{L13}
$$
They imply (L11), $h\ge \mathcal R/(2\cdot10^{15})$, $1\le h<s/2$, and
$|b|<2^{m-3}$, by the same elementary inequalities used for (P16). In particular
$$
\Phi_m(b)\le\vartheta^G+C_1JB(G)/\sqrt{\mathcal R},\qquad
C_1=48\sqrt{2\cdot10^{15}}C_{\rm flat}.                    \tag{L14}
$$
Put $Q=\log_2\mathcal R$ and
$$
G=\left\lfloor\left[\frac{Q}{200000\log_2(Q+2)}\right]^{1/3}\right\rfloor.
                                                               \tag{L15}
$$
For sufficiently large effective $\mathcal R$, we have $G\ge3$,
$J\le5\log \mathcal R$, $B(G)\le \mathcal R^{1/8}$, and $C_1J\le \mathcal R^{1/8}$.
The remaining condition in (L13) follows, for example, from the effective
eventual inequality $\mathcal R\ge10^{14}\log(10000\log \mathcal R)$. All thresholds now
depend only on $\mathcal R$, and $\mathcal R\le m$ automatically supplies $m\ge20$.
Thus
$$
\Phi_m(b)\le\vartheta^G+\mathcal R^{-1/4}
\le C\exp\left[-c\left(\frac{\log \mathcal R}{\log\log \mathcal R}\right)^{1/3}\right]
\qquad(\mathcal R\ge R_0),                                         \tag{L16}
$$
for effective absolute $c,C,R_0>0$.

In particular, effective uniform decay holds whenever
$$
\frac{m-\log_2|b|}{1+\log m}\longrightarrow\infty.          \tag{L17}
$$
Equivalently, the window $|b|\le\epsilon(m)2^m$ is admissible for every
$\epsilon(m)=m^{-\omega(1)}$. For fixed $\delta>0$,
$\mathcal R\asymp_\delta m/\log m$, recovering the same cubic-log rate in $m$.
This remains a Fourier distribution theorem. It does not prove exponential
occupation, fixed-ratio stopping counts, or descent for a specified integer.

The counting delay in Corollary 2 is unchanged by this wider window.
In (32), each $h=2^ub\le H=\lceil2^{d+1}K\rceil$ has
$\Gamma_{N-u}(b)=N-\log_2h\ge N-\log_2H$.
The fixed-gap window already covers these frequencies in the proved delay
range; the limiting factor is the Fourier rate multiplied by $2^d$.


## 7. From Fourier coefficients to stopping counts

Erdős–Turán in [13, Proposition 3.2, equation (3.5)] states
$$
D_N\le\frac1{H+1}+3\sum_{h=1}^H\frac{|F_N(h)|}{h}.
\tag{26}
$$
The constants are 1 and 3 in the normalization used here.

For fixed $H$, each $h=2^ub$ has conductor $N-u\to\infty$ and fixed odd
$b$. Theorem 1 makes every term tend to zero. First let $N\to\infty$,
then $H\to\infty$. This gives $D_N\to0$. The same reasoning for the
projection modulo $2^m$ gives convergence to Lebesgue measure uniformly
over all remaining horizons $N\ge m$.

The interval in (6), after division by $2^N$, has fixed length
$2^{-d-1}$. Thus $D_N\to0$ proves its relative count. Each integer in the
shell corresponds to exactly one residue; no integer multiplicity is
lost. When $d=0$ the coefficient count also follows directly from parity
coding, since survival depends only on the first $N-1$ bits.

For Corollary 4, write $h=2^ub$. Our choice of $N_0$ ensures
$m=N-u\ge m_b$. The exceptional $N$ for this coefficient have total
weight
$$
\sum\frac1N\le\sum\frac1m\le B(G).
$$
On other $N$, $|F_N(h)|\le\vartheta^G$. Multiply (26) by $1/N$, sum,
and divide by $\Lambda$ to get (10). For the ordinary average, (9a)
gives at most $B(G)\lceil R+u+13\rceil$ exceptional horizons for each
fixed $h=2^ub$. Since $u\le\log_2H$, bounding their Fourier magnitudes
by one and summing (26) gives (10a). A shell of delay $d$ has relative
length $2^{-d-1}$, which proves both relative-error bounds.

The parameters in (10) give a fully explicit average. For example,
$$
B(G)\le(2G+3)2^{560(2G+3)^4}.
\tag{27}
$$
Choose $G=\lfloor(\log_2\Lambda/200000)^{1/4}\rfloor$, with $G\ge3$.
Since $2G+3\le3G$ and $\log_2(3G)\le G^4$,
$\log_2B(G)\le45361G^4<\frac12\log_2\Lambda$.
Taking $H=\lceil\exp((-\log\vartheta)G/4)\rceil$ in (10) gives an
effective bound $O(\exp[-c(\log\Lambda)^{1/4}])$ for an effective absolute
$c>0$. The stipulated relation between $N_0$ and $H$ must still hold.
Delays $d=o((\log\Lambda)^{1/4})$ preserve convergence of the averaged
relative error. Markov's inequality gives a set of good horizons of
logarithmic density one. This averaged argument alone does not specify a
growing delay valid at every horizon; Section 6.5 proves that stronger result.

For the ordinary average we can retain the cubic dimension exponent
in (8), rather than the rough fourth power in (27). For $G\ge3$,
$2G+3\le3G$ and $\log_2(3G)\le2\log_2G$, so
$$
\log_2B(G)\le\log_2(3G)+432G^3(35+2\log_2(3G))
\le12000G^3\log_2G.
\tag{27a}
$$
Put $Q=\log_2M$, $\alpha=-\log\vartheta>0$, and choose
$$
G=\left\lfloor\left(\frac{Q}{200000\log_2(Q+2)}\right)^{1/3}\right\rfloor,
\quad R=\frac{\alpha G+\log C_{\rm end}}\eta,\quad
H=\lceil e^{\alpha G/4}\rceil,\quad N_0=\lceil\log_2H\rceil+10.
\tag{27b}
$$
When $G\ge3$, (27a) gives $\log_2B(G)\le0.06Q<Q/2$.
Also $N_0=O(G+1)$, $\Delta\ge M/2$ eventually, and the conductor width
in (10a) is $O(G+1)$, all with effective absolute constants.
The two nonexceptional terms are equal to $\vartheta^G$ by the choice
of $R$. The harmonic factor is $O(G+1)$, while $1/(H+1)\le e^{-\alpha G/4}$.
It follows that (10a) is $O(e^{-c(\log M/\log\log M)^{1/3}})$ for an
effective $c>0$. Adding the first $N_0$ terms, each at most one, proves
(10b), with an effective starting threshold. The constants give no
useful asymptotic rate at census scale: $\alpha\approx8.0\cdot10^{-6}$,
and even the condition $G\ge3$ in (27b) is only guaranteed, for example,
by $\log_2M\ge2^{28}$. The exact bound (10a) states the parameter
dependence without an asymptotic simplification.

Write $g(N)=(\log N/\log\log N)^{1/3}$ for sufficiently large $N$.
If $d(N)=o(g(N))$, then for every $\epsilon>0$, apart from finitely
many terms, $2^{d(N)+1}\le2e^{\epsilon\log2\,g(M)}$ for $N\le M$.
Choose $\epsilon<c/\log2$ in (10b). The ordinary average of the absolute
relative errors tends to zero. Markov's inequality and a diagonal choice
of decreasing error tolerances give convergence to zero on a set of
horizons of ordinary density one. The separate pointwise bound (7a)
controls every large horizon in the same delay scale.

### 7.1. Coefficient versus actual stopping

We record a sufficient known comparison with a proof, since the
distinction matters for (7). Let $j$ be the first coefficient-descent
time for an actual source, and put $R_i=3^{a_i}/2^i$. Before time $j$,
$R_i>1$ for $i\ge1$, and $R_0=1$. The affine formula gives
$$
C^j(n)=R_j\left(n+
 \sum_{\substack{0\le i<j\\C^i(n)\text{ odd}}}\frac1{3R_i}\right)
\le R_j(n+j/3).
\tag{28}
$$
Lagarias [12, Lemma 2.2(1)] gives
$$
\left|\log_3 2-\frac aj\right|
\ge\frac1{1200j^{14.3}}.
$$
For $a=a_j<j\log_3 2$, write $\epsilon_j=j\log_3 2-a>0$. If
$\epsilon_j\le1$, concavity gives $1-3^{-\epsilon_j}\ge2\epsilon_j/3$;
if $\epsilon_j\ge1$, the lower bound is at least $2/3$. Therefore
$$
1-R_j\ge\frac1{1800j^{13.3}}.
\tag{29}
$$
Equations (28)–(29) show that $C^j(n)<n$ when $n>600j^{14.3}$.
We retain the previously used weaker threshold $900N^{14.3}$: for
$n>900N^{14.3}$, actual and coefficient survival through times $j<N$
agree. The underlying high-source comparison is established methodology,
also discussed in [2, correction and subsequent comments]; the numerical
constant is not a contribution of this paper.

For fixed delay, every shell source exceeds this polynomial threshold
once $L$ is large. This proves (7). The same transfer applies to the
averaged relative bound whenever the considered shell sources exceed
$900N^{14.3}$. For growing $d(N)=o((\log N/\log\log N)^{1/3})$, exponential shell size
eventually exceeds $900N^{14.3}$. Discarding the finite initial range
therefore transfers the pointwise, ordinary averaged and density-one
conclusions to actual stopping counts. The exact coefficient bounds (10) and (10a)
remain valid without this cutoff.

### 7.2. Joint source equidistribution and transfer of the coarse path

Use the uniform law on coefficient-surviving words
$E_N$, with the final bit free, and write $X_w$ for their parity source
residues. Put $Y=X_w/2^N$. Let $q=\lfloor(N-1)/4\rfloor$. Define the
skeleton $\mathcal C_N$ by the counts in all $q$ disjoint four-bit blocks,
together with the ordered residual bits at positions $4q+1,\ldots,N$.
There are between one and four residual bits, including the free last bit.
Thus the skeleton records every block-end count and retains the short tail,
but discards the order inside each complete block.

**The majorant controls a conditional Fourier norm.**

For integer $h$, define
$$
T_N(h)=\mathbb E_{E_N}\left|
  \mathbb E_{E_N}[e(hY)\mid\mathcal C_N]\right|.             \tag{J1}
$$
For $h=2^{N-m}b$, $N\ge m$, $b$ odd, let $s=\lfloor(m-3)/4\rfloor$
and $W_s$ count the same good nonterminal vertices as in this paper.
We claim that for every integer $G\ge0$,
$$
T_N(2^{N-m}b)\le\vartheta^G+
                       \mathbb P_{E_N}(W_s<G).             \tag{J2}
$$
This is stronger than merely bounding $|F_N|$. In particular the old
bound for $|F_N|$ alone would not imply (J2).

There is also a finer record $\mathcal Q_N$: retain every complete block
exactly, except identify $1101$ with $1110$, and retain the residual bits
exactly. The count skeleton is a function of this record. Every statement
below remains true with $\mathcal C_N$ replaced by $\mathcal Q_N$.

**Conditional factorization.** Fix a skeleton of positive probability.
Its cumulative block counts fix every entering height. Inside each complete
block, choose uniformly from the four-bit words with the specified count
that stay strictly positive from that height. These choices are independent:
the positivity restrictions factor by block once its endpoints and tail
are fixed, and the original law gives equal weight to all full words.

For a local word $u$ with $k$ ones write its inverse map as
$$
f_u(y)=(16y-c_u)/3^k.
$$
Composing these affine maps shows that the full source modulo $2^N$ is
a sum of one contribution from each local $c_u$, with coefficients
$-2^{4t}3^{-A_{t+1}}$, and the fixed tail contribution. All inverses
of three are taken modulo $2^N$. Therefore the conditional characteristic
function factors over the independent local choices. Its modulus is at
most the product of their local modulus bounds through the first $s$ blocks.

At a vertex with height $x$, let $L_k(x)$ be the number of legal words
having $k$ ones. For $k\ne3$ use the bound one. For $k=3$, the two
universally legal words $1101,1110$ have equal weight $1/L_3(x)$ and
this paper's phase difference $v_t$. Hence the local modulus is at
most
$$
f_{t,3}=1-\frac{2}{L_3(x)}(1-|\cos\pi v_t|),\qquad
f_{t,k}=1\quad(k\ne3).                                    \tag{J3}
$$
There is no constraint from $\mathcal C_N$ distinguishing these two words.

Let $P_t(A,A+k)$ be the original conditioned block-count kernel. The
coefficient $P_t(A,A+3)/L_3(x)$ is exactly $p_U=p_V$, since future
continuation counts depend only on the block endpoint. Thus
$$
K_t(A,A+k)=P_t(A,A+k)f_{t,k}                                \tag{J4}
$$
is the same substochastic majorant as before. Averaging the conditional
product proves $T_N(h)\le K_0\cdots K_{s-1}\mathbf1$.
On $W_s<G$ use $K\le P$; on its complement normalize rows and bound
the product of row sums by $\vartheta^G$. This proves (J2), retaining the
actual excursion law in the rare-event probability.

For the finer record, each identified block is an independent fair choice
between $U$ and $V$, conditional on that record. Both choices are legal
from every possible entering height, and changing them preserves all
block counts and later heights. Its conditional Fourier modulus is exactly
the product of the absolute cosines of half their pair phase differences
(the fixed unidentified blocks contribute modulus one). Through $t<s$ this
is $|\cos\pi v_t|$; at any later block use the modular source difference
$h2^{4t+2}3^{-(A_t+3)}/2^N$ directly. Averaging over records gives
the same kernel (J4), so the proof is unchanged. This also explains why
the permitted path information is precisely invariant under these exchanges;
no claim is made for arbitrary fine parity information.

Consequently every pointwise estimate proved in Sections 6.5 and the
moving-window extension also holds with $|F_N|$ replaced by $T_N$.
In particular, for effective absolute $c,C>0$,
$$
\sup_{\substack{b\text{ odd}\\0<|b|\le2^{m/2}}}
\ \sup_{N\ge m}T_N(2^{N-m}b)
\le C\exp[-c(\log m/\log\log m)^{1/3}]                     \tag{J5}
$$
above an effective threshold. The enhanced moving window is optional
for this consumer; the inspected fixed-$\delta$ theorem suffices.

**Average conditional discrepancy.**

For each skeleton $c$, let $\mu_{N,c}$ be the conditional law of $Y$,
and let $D_{N,c}$ be its interval discrepancy on $[0,1)$. Apply
Erdős–Turán separately to each conditional probability measure and
average. The positive sum gives
$$
\mathbb E D_{N,\mathcal C_N}
\le\frac1{H+1}+3\sum_{h=1}^H\frac{T_N(h)}h.                \tag{J6}
$$
Choose $H$ as in this paper's proof of (7a), using (J5). Then
$$
\mathbb E D_{N,\mathcal C_N}\le\varepsilon_N,
\qquad \varepsilon_N=C_2e^{-c_2g(N)},\quad
g(N)=(\log N/\log\log N)^{1/3},                            \tag{J7}
$$
with effective absolute constants and threshold.

For every bounded skeleton statistic $Z$, $|Z|\le1$, and fixed interval
$I\subset[0,1)$, (J7) implies
$$
\left|\mathbb E[Z1_{\{Y\in I\}}]-|I|\mathbb E Z\right|
\le\varepsilon_N.                                        \tag{J8}
$$
More strongly, the same error controls intervals chosen as a function
of the skeleton, since the supremum defining $D_{N,c}$ is inside the
expectation. These are joint statements about source and coarse path.

**Total variation on a short source shell.**

For a fixed interval $I$ of length $\alpha>\varepsilon_N$, put
$q_c=\mu_{N,c}(I)$ and $a=\mathbb P(Y\in I)=\mathbb E q_c$.
Then $a\ge\alpha-\varepsilon_N>0$ and the conditional skeleton law
has density $q_c/a$ relative to its original excursion law. Therefore
$$
\left\|\mathcal L(\mathcal C_N\mid Y\in I)
                -\mathcal L(\mathcal C_N)\right\|_{\rm TV}
=\frac{\mathbb E|q_c-a|}{2a}
\le\frac{\varepsilon_N}{\alpha-\varepsilon_N}.             \tag{J9}
$$
We used $\mathbb E|q_c-\alpha|\le\varepsilon_N$ and
$|a-\alpha|\le\varepsilon_N$. Here total variation is the supremum
over events, equivalently half the $L^1$ distance.

Let $N=L+d(N)$ with $d(N)\ge0$ and $d(N)=o(g(N))$, and take
$I=[2^{-d-1},2^{-d})$. The right side of (J9) tends to zero. Parity
coding identifies the conditioned source set with the $L$-bit integers
whose first $N-1$ coefficients survive. For all sufficiently large
$N$, the existing $900N^{14.3}$ comparison makes that set exactly
$$
\{2^{L-1}\le n<2^L:\sigma(n)\ge N\}.
$$
Thus the full four-bit count skeleton of a uniformly chosen actual
surviving integer in that shell converges in total variation to the
fair-parity excursion skeleton. Any sequence of events measurable in
the skeleton transfers with the same vanishing absolute probability
error, even though the skeleton dimension grows with $N$.

**Path scale and affine orbit comparison.**

At every bit time the true height $H_j=\lambda a_j-j$ differs from
linear interpolation between its recorded block endpoints by at most
$4\lambda$. The residual bit heights are known exactly. Hence any
coarse path limit under a scale tending to infinity transfers to the
source shell through (J9), with this deterministic interpolation error.
This note does not import or prove a Brownian excursion invariance principle.

For an actual source $n$ in the shell and $j\le N$, the inverse formula gives
$$
C^j(n)=\frac{3^{a_j}}{2^j}(n+B_j),\qquad
B_j=\sum_{i=1}^j\frac{w_i2^{i-1}}{3^{a_i}}\le j/3,          \tag{J10}
$$
where the bound follows from coefficient survival at $i-1$ (and the
time-zero coefficient equals one). Thus
$$
0\le\log_2(C^j(n)/n)-H_j
\le\log_2(1+N/(3n)),                                     \tag{J11}
$$
uniformly through time $N$. This error is exponentially small in the
shell bit length. The bound at time $N$ uses survival only at earlier
times, even though the final coefficient itself need not survive.

The result transfers distributions of long surviving paths. It does not
assert independence from the complete parity word, which determines the
source, and does not exclude exceptional non-descending individual orbits.
It adds no fixed-ratio stopping-time theorem or exponential Fourier bound.

### 7.3. Diffusive logarithmic peaks of long survivors

Let $n=N-1$, $H_i=\lambda a_i-i$, and $M_n=\max_{0\le i\le n}H_i$
under the uniform excursion law $E_N$. Retain $\beta=\lambda-1$,
$p=1/\lambda$, $\kappa>0$, $C_*=C_V/\ell_\kappa$, and
$C_{\rm flat}=60000C_*$. Both increment laws $X$ and $-X$ are centered,
bounded by one, and have variance $\beta<1$.

**A weighted maximum estimate before killing.**

For a walk started at $a\ge0$, let $\tau_0=\min\{i\ge1:H_i\le0\}$.
For every integer $j\ge1$ and real $z\ge3$,
$$
\mathbb E_a[(H_j+1)1_{\{\max_{0\le i\le j}H_i\ge z\}};
             \tau_0>j]
\le40(a+1)^2\frac{\sqrt j}{z}.                            \tag{D1}
$$
If $a\ge z$, optional stopping of $H_{j\wedge\tau_0}$ and the bounded
lower overshoot imply
$\mathbb E_a[H_j+1;\tau_0>j]\le a+2$; this is below the right side.

Suppose $a<z$. Let $\tau_z=\min\{i\ge1:H_i\ge z\}$ and
$T=j\wedge\tau_0\wedge\tau_z$. Bounded-time optional stopping gives
$$
z^2\mathbb P_a(\tau_z\le j,\tau_z<\tau_0)
\le\mathbb E_a H_T^2
=a^2+\beta\mathbb E_aT
\le a^2+17(a+1)\sqrt j.                                   \tag{D2}
$$
The last inequality is the survival-sum estimate (L4); $T\le j\wedge\tau_0$.
On the upper-exit event $H_{\tau_z}\in[z,z+1]$. From any starting height
$u\ge0$, bounded lower overshoot gives
$\mathbb E_u[H_r+1;\tau_0>r]\le u+2$, also at $r=0$.
By the strong Markov property, the left side of (D1) is at most
$(z+3)\mathbb P_a(\tau_z\le j,\tau_z<\tau_0)$.
Since $z+3\le2z$, (D2) bounds this by
$$
\frac{2a^2+34(a+1)\sqrt j}{z}
\le36(a+1)^2\frac{\sqrt j}{z},
$$
proving (D1). The proof applies identically to increments $-X$.

**Upper tail of the excursion maximum.**

For $n\ge4$ put $j=\lfloor n/2\rfloor$. The prefix h-transform and (D1)
give
$$
\mathbb P_{E_N}\left(\max_{0\le i\le j}H_i\ge z\right)
\le120C_*\frac{\sqrt n}{z}.                               \tag{D3}
$$
Indeed $n/(n-j)\le2$, and (K4) applies with initial height zero.

For the second half, note that the first increment of a surviving path
must be $\beta$, with critical probability $p$. Remove that increment.
The remaining positive path goes from $\beta>0$ to $H_n=y>0$ in $n-1$
steps, so it can be reversed without losing any strict endpoint condition.
Set $u=n-1-j\ge1$. Reversing its first $u$ steps covers exactly the original
times $n,n-1,\ldots,j+1$. The remaining reverse segment has length $j$
and ends at $\beta$. Consequently the unnormalized contribution from a
maximum at least $z$ in this half equals
$$
p\sum_{y>0}e^{-\kappa y}
\mathbb E_y^-\left[
1_{\{\tau_0>u,\ \max_{0\le i\le u}H_i\ge z\}}
k_j^-(H_u,\beta)\right],                                 \tag{D4}
$$
where the sum uses the original time-$n$ reachable lattice.
Use $k_j^-(x,\beta)\le3000(x+1)(\beta+1)j^{-3/2}$ and (D1), then
divide by $Z_n\ge\ell_\kappa n^{-3/2}$. Since $n/j\le3$, $p<1$,
$\beta+1<2$, and $\sqrt u\le\sqrt n$, this is at most
$$
\frac{2\cdot10^6R_{\kappa,2}}{\ell_\kappa}
\frac{\sqrt n}{z},                                       \tag{D5}
$$
where the finite geometric-sum bound is
$$
R_{\kappa,2}=
\frac{(1+\lambda)^2}{1-r}
+\frac{2\lambda(1+\lambda)r}{(1-r)^2}
+\frac{\lambda^2r(1+r)}{(1-r)^3},\qquad r=e^{-\kappa\lambda}.
                                                               \tag{D6}
$$
Indeed the positive grid is contained in $a+\lambda\mathbb N_0$,
$0<a\le\lambda$, and its weighted sum of $(y+1)^2$ is bounded by (D6).
All factors in (D4) are nonnegative, so the two pointwise kernel bounds
may be applied before summation.

With
$C_M=120C_*+2\cdot10^6R_{\kappa,2}/\ell_\kappa$, (D3)--(D5) give
$$
\mathbb P_{E_N}(M_n\ge z)\le C_M\frac{\sqrt n}{z}
\quad(n\ge4,z\ge3).                                     \tag{D7}
$$
The constants are deliberately loose. This polynomial tail is enough
for tightness; no Gaussian maximum estimate is claimed.

**A lower scale from one atom.**

At $j=\lfloor n/2\rfloor\ge n/3$, (L7) bounds every height atom by
$\sqrt3C_{\rm flat}/\sqrt n$. There are at most
$z\sqrt n/\lambda+1$ reachable heights in $(0,z\sqrt n]$. Hence
$$
\mathbb P_{E_N}(M_n\le z\sqrt n)
\le2C_{\rm flat}(z+n^{-1/2})\qquad(z\ge0).                \tag{D8}
$$
For every $\epsilon>0$, (D7)--(D8) therefore give constants
$0<c_\epsilon<C_\epsilon<\infty$ such that, for all sufficiently large
$N$,
$$
\mathbb P_{E_N}(c_\epsilon\sqrt N\le M_{N-1}
                         \le C_\epsilon\sqrt N)>1-\epsilon.
                                                               \tag{D9}
$$
This asserts a diffusive order in probability, not convergence to a
specified limiting law.

**Transfer to actual trajectories.**

Let $d(N)\ge0$ satisfy $d(N)=o((\log N/\log\log N)^{1/3})$, and let
$L=N-d(N)$. Choose a source $U_N$ uniformly from
$$
\{2^{L-1}\le a<2^L:\sigma(a)\ge N\}.
$$
The set is nonempty at all sufficiently large $N$ by Corollary 2. The path-transfer statement (J9) transfers the full block
count skeleton to this law in total variation. Let $M'_{N-1}$ be the maximum of the interpolated block-end path,
including the exactly recorded residual proper-prefix heights. Then
$0\le M_{N-1}-M'_{N-1}\le4\lambda$. First apply (D9) to $M'_{N-1}$
with its constants adjusted by $4\lambda/\sqrt N$. The skeleton determines
$M'_{N-1}$, so its law transfers by (J9). Finally use the same deterministic
bound to return to the actual height maximum. This proves (D9) for $U_N$.

Finally (J11) bounds the difference from the actual logarithmic orbit
growth uniformly by $\log_2(1+N/(3U_N))=o(1)$. It follows that
$$
\log_2\left(\max_{0\le i<N}\frac{C^i(U_N)}{U_N}\right)
=\Theta_{\mathbb P}(\sqrt N),                              \tag{D10}
$$
where the notation means precisely the two-sided probability bound (D9),
with constants depending on $\epsilon$.

## 8. Exact recurrence and computational evidence

The analytical conclusions use no numerical extrapolation. We retain two
different kinds of computational evidence with their scopes explicit.

### 8.1. A quadratic-state Fourier calculation

At clock $j$ and odd total $a$, let $Z_j(a)$ be the partial complex
amplitude, with the accumulated inverse-prefix phase included. Starting
with $Z_0(0)=1$, an even step contributes $Z_j(a)$ to state $(j+1,a)$.
An odd step contributes
$$
Z_j(a)e\left(-\frac{h3^{-(a+1)}}{2^{N-j}}\right)
\tag{30}
$$
to state $(j+1,a+1)$. Discard states with $3^a\le2^j$ at clocks
$1\le j<N$; do not discard at the last clock. Summing $Z_N(a)$ gives
the unnormalized Fourier numerator. Replacing every phase by 1 gives
$|E_N|$. There are $O(N^2)$ states and transitions; this is an arithmetic
operation count, not a claim that high-precision arithmetic has constant
bit cost. The exact formula is Wren's [2]; the supplied floating-point
implementation approximates its complex values.

The final free bit implies $F_N(h)=0$ for odd $h$. For $N\ge3$, every
surviving word begins 11 and $X_w\equiv3\pmod4$, so
$$
F_N(h+2^{N-2})=-iF_N(h).
\tag{31}
$$
These exact aliases explain why a proposed global resonance classifier
based only on $v_3(h)$ cannot be used without restricting frequency lifts.
They do not conflict with the low-character window in Theorem 1.

### 8.2. Frozen finite interface audit

One deterministic audit uses five CPU processes and exact integer or
rational arithmetic. It checks 2,150 continuation-count cases, 2,653 pair
phase identities, 655,280 centered carry edges, and 3,606 telescoping and
subsum-pruning cases. The latter include an actual nonempty vanishing
subsum deletion. It also reconstructs 1,006 source residues directly from
their forward parity words and compares 63 exact phase histograms.
All checks pass. A supplementary floating-point zero check has error at
most $1.1\cdot10^{-16}$; it is not a certified Fourier bound.

These checks validate finite interfaces. They do not establish the
asymptotic theorem or the imported S-unit results. Their source and saved
output are bundled, and the grid was not enlarged after passing.

A third, new audit checks the weighted strict-positive identity (25d)
in exact formal arithmetic, where the variable records the one-bit count.
At the predetermined endpoints 12,20,28,36,44, it compares all coefficients
against direct survival-count dynamic programming using the recurrence
$nZ_n=\sum_{k=1}^n A_kZ_{n-k}$, where $A_k$ is the unrestricted
positive-endpoint binomial polynomial. All 939 nonzero coefficient checks
pass. It uses five CPU processes. It checks the finite identity, not the
asymptotic endpoint bound; the earlier carry and census audits were not
rerun for this extension.

A fifth preregistered audit checks the new conditional-factorization
interface in Section 7.2. At horizons 9, 12, 15, 18 and 21 it enumerates
64,874 coefficient-surviving words and 33,828 records identifying only
$1101$ with $1110$. It checks every flip mask, uniform product-cube
cardinalities, and 40,124 modular source-difference contributions against
direct inverse iteration. All checks pass. The grid covers every residual
tail length from one to four bits. It neither proves the asymptotic path
transfer nor repeats any of the four previous audits.

### 8.3. Wren's existing census

Wren [2] reports a stopping-time census for $3\le L\le34$, comparing
actual shell counts with exact fair-coin model counts. Representative
retained entries are:

| Source bits $L$ | Horizon $N$ | Reported actual count | Actual/model, rounded |
|---:|---:|---:|---:|
| 28 | 168 | 1,683 | 1.011 |
| 30 | 180 | 4,048 | 0.978 |
| 32 | 96 | 696,380 | 1.000 |
| 34 | 204 | 22,826 | 0.999 |

The model count uses exact integer survival counts divided by a power of
two. These observations motivate a substantially stronger conjecture at
fixed horizon ratios. They do not reach the enormous effective threshold in
Theorem 1 or prove that conjecture.

The public supplement contains all 32 raw shell histograms, their checksums,
the original and instrumented C programs, and the retained maximum-state log.
Wren reran the enumeration with a running maximum: all histograms agreed,
the cap 4096 was never reached, and the largest reported shortcut orbit value
had base-two logarithm 63.168. The cap and arithmetic claims are therefore
supported by a public run record. The use of 128-bit states has ample room:
before a first overflow, every prior state would already have been recorded,
and three times the recorded maximum is below the representable limit.

The first author inspected these sources and retained artifacts and independently
enumerated all 262,140 sources in the 3–18-bit shells using arbitrary-precision
integers, recomputed 252 record entries, checked the 34 supplied hashes and
all 32 histogram totals, and reconstructed the four displayed ratios exactly. He did not
repeat the entire 34-bit scan. The full census is Wren's computation; this
verification distinction does not affect the analytic theorems.

## 9. Limits and the next quantitative question

Theorem 1 gives effective pointwise decay over small ordinary frequency
lifts, uniformly in the remaining horizon. It proves relative stopping
counts at every large horizon for the stated growing delays. Theorem 3's
harmonic and ordinary exception counts are additional explicit bounds.
Neither the pointwise rate nor the averages imply exponential Fourier
decay in the conductor, as needed for a fixed positive ratio between
horizon and source bit length. The large constants in the pointwise onset
and in (8) are not numerically useful at the displayed census sizes.

For a shell with $L$ source bits at horizon $N$, Erdős–Turán needs only
frequencies up to approximately $2^{N-L}$ times a smoothing factor.
More precisely, set $d=N-L$, take an integer $K\to\infty$, and use
$H=\lceil2^{d+1}K\rceil$. Equation (26) bounds the relative error by
$$
\frac1K+3\,2^{d+1}\sum_{h=1}^{H}\frac{|F_N(h)|}{h}.
\tag{32}
$$
Thus a bound $\sum_{h\le H}|F_N(h)|/h=o(2^{-d})$ would suffice for the
fixed-ratio count. It is weaker than a pointwise estimate for every
frequency or a deterministic linear lower bound for every path. The present proof controls sparse good-phase paths by pinning a retained
middle carry and bounding a conditioned count atom. What remains is a substantially
stronger estimate for the frequency of good phases or for the weights of
paths with few such phases. A linear empirical count of good nonterminal
vertices is not substituted for that missing theorem.

A precise probabilistic consumer is available. If $W_j$ counts good vertices
through any prefix of $j=4r\le4s$ bits, event domination by the original
conditioned chain and row normalization on its complement give
$$
|F_N(2^{N-m}b)|\le\vartheta^G+\mathbb P_{E_N}(W_j<G).
\tag{32a}
$$
Appendix A proves, by stopping a mean-zero walk in an interval and splitting its
killed kernel into three pieces, the explicit bound
$k_n(x,y)\le3000(x+1)(y+1)n^{-3/2}$. It consequently supplies an effective
absolute constant $C_*$ such that, for $j\le(1-\delta)m$, $N\ge m$,
and $m\ge2/\delta$,
$$
\mathbb P_{E_N}(W_j<G)
\le C_*(2/\delta)^{3/2}(j+1)\mathbb P_p(W_j<G),
\qquad p=1/\lambda.
\tag{32b}
$$
Here the probability on the right uses independent critical bits and the
same phase/count test, without imposing a positivity barrier. This
standard killed-walk comparison gives a polynomial cost on a bulk prefix.
An exponential lower-tail estimate for good counts under those independent
bits, on a prefix long enough to leave initial resonance triangles, remains
unproved here.
No occupation theorem is inferred from (32b).

Even a relative count at a fixed ratio would remain an average statement.
No result here excludes a specified divergent orbit or a nontrivial
positive cycle. The Collatz conjecture remains open.

## 10. Reproducibility and contributions

The supplement contains five scoped audits and saved results,
public numerical sources and retained aggregate output, and an inspection
record. Run the interface audit with Python 3 from the bundle root:
`python src/excursion_qualitative_audit_20261102.py`. It uses the standard
library, five CPU processes and no GPU or network access. The new identity
audit runs as `python src/excursion_sparre_andersen_audit_20261102.py`.
The middle-carry audit runs as
`python src/excursion_middle_carry_audit_20261102.py`; it checks 10,080
new early/late groupings, 19,246 valuation reconstructions, and four actual
zero-subsum deletions in 3,600 path/numerator cases. These finite checks
neither reach the logarithmic-form onset nor prove asymptotic estimates.
The new conditional-factorization audit runs as
`python src/excursion_pair_quotient_audit_20261102.py`.
Large census runs are unnecessary for checking the proofs.

Lyapunov Weaver developed the conditional four-bit comparison, carry
proof, both S-unit applications, effective endpoint-tail proof, harmonic
and ordinary discrepancy consumers, the retained-middle-carry argument and
effective pointwise rate, and exact interface and identity audits. Fourier Wren developed the numerical investigation and quadratic
Fourier recurrence, supplied the public census evidence, and independently
inspected the qualitative proof, quantitative S-unit count, harmonic
consumer, and the endpoint-tail and ordinary-count extension. He also
independently inspected the supplementary bulk comparison note.
Wren independently inspected the pointwise extension, including the
retained-middle-carry lemma, intermediate count bound and growing-delay consumer.
The sharper symmetric atom and moving window are by Weaver; Wren
independently inspected their complete proofs. The conditional Fourier
norm and total-variation path-transfer result are also by Weaver; Wren
independently inspected (J1)--(J11) and the finer-record argument. Weaver
proved the elementary diffusive peak scale, and Wren independently
inspected (D1)--(D10).
The proof and numerical claims retain these separate verification scopes.

## Appendix A. Killed kernels and conditioned count laws

Let $X=\lambda B-1$ under critical Bernoulli-$p$ bits, $p=1/\lambda$,
$\lambda=\log_2 3$, $\beta=\lambda-1$. Then
$\mathbb E X=0$, $|X|\le1$, and $\operatorname{Var}X=\beta>1/2$.
The reverse increment $-X$ has the same properties. Write
$$
k_n(x,y)=\mathbb P_p(x+S_i>0\ (1\le i\le n),\ x+S_n=y),
\qquad x\ge0,\ y>0.
$$
This is an atom probability on the reachable time-$n$ lattice, rather than
a Lebesgue density. We show
$$
k_n(x,y)\le3000(x+1)(y+1)n^{-3/2}\qquad(n\ge1). \tag{K1}
$$

**Survival in either direction.**

For either increment $X$ or $-X$, put
$s_n(x)=\mathbb P_x(H_i>0\ (1\le i\le n))$. Then
$$
s_n(x)\le8(x+1)n^{-1/2}. \tag{K2}
$$
If $x\ge L=\sqrt n$, the right side exceeds one. For $0\le x<L$,
let $T$ be the first positive time outside $(0,L)$. The exit position
belongs to $[-1,0]\cup[L,L+1]$. The exit time has finite expectation:
a sufficiently long run of increments of one sign forces exit, so a
geometric-block bound applies. Optional stopping for $H_t$ gives
$\mathbb E H_T=x$ and hence
$$
\mathbb P(H_T\ge L)\le\frac{x+1}{L+1}\le\frac{x+1}L.
$$
Writing $H_T^+=\max(H_T,0)$ and $H_T^-=\max(-H_T,0)$, we have
$\mathbb E H_T^+ =x+\mathbb E H_T^-\le x+1$ and
$$
\mathbb E H_T^2\le(L+1)\mathbb E H_T^++\mathbb E H_T^-
\le(L+1)(x+1)+1.
$$
Optional stopping for $H_t^2-\beta t$ consequently gives
$$
\mathbb E T\le\frac{(L+1)(x+1)+1}{\beta}
\le6L(x+1).
$$
One can first stop at $T\wedge r$ and use bounded stopped positions to
justify both identities. If a path survives through $n$, it either exits
upwards before exiting downwards, or has $T>n$. The two bounds above and
Markov's inequality give $s_n(x)\le7(x+1)/\sqrt n$, proving (K2) with
the deliberately loose constant eight. The convention at $x=0$ starts
checking the barrier after the first step, exactly as required here.

**Three pieces and reversal.**

For $n\ge3$, take $n_1=n_3=\lfloor n/3\rfloor$ and $n_2=n-n_1-n_3$.
The unrestricted middle transition has every atom at most $3/\sqrt{n_2}$,
by the explicit binomial bound used in Lemma 6.
The first and reversed last pieces have total masses at most
$8(x+1)/\sqrt{n_1}$ and $8(y+1)/\sqrt{n_3}$ by (K2).
Indeed reversing a positive final path gives a positive path from $y$
under increments $-X$, with unchanged product probability. Positivity at
time $n-n_3$ is retained, so the reversed last piece is positive at
every time $1,\ldots,n_3$, as (K2) requires. Dropping the
middle positivity constraint and summing over its two endpoints gives
$$
k_n(x,y)\le\frac{192(x+1)(y+1)}{\sqrt{n_1n_2n_3}}
\le192\,6^{3/2}(x+1)(y+1)n^{-3/2}.
$$
Each $n_i\ge n/6$ and $192\,6^{3/2}<3000$. For $n=1,2$ the trivial
atom bound one proves (K1).

**The conditioned prefix density.**

For $\kappa=\log(p/(1-p))/\lambda$, define
$$
V_\ell(x)=\mathbb E_p[e^{-\kappa(x+S_\ell)};
 x+S_i>0\ (1\le i\le\ell)],\qquad V_0(x)=e^{-\kappa x}.
$$
At each fixed time the positive endpoint lattice has spacing $\lambda$.
Summing (K1) against the exponential weight gives, for all $\ell\ge1$,
$$
V_\ell(x)\le C_V(x+1)\ell^{-3/2},\quad
C_V=3000\left[\frac{1+\lambda}{1-e^{-\kappa\lambda}}
+\frac{\lambda e^{-\kappa\lambda}}{(1-e^{-\kappa\lambda})^2}\right]. \tag{K3}
$$
This upper bound is uniform over every $x\ge0$. For the endpoint grid
$y=a+\lambda r$ with $0<a\le\lambda$, use $e^{-\kappa a}\le1$ and
$a+1\le\lambda+1$ to obtain the displayed geometric sum.

Put $n=N-1$ and let $A$ be any event of the first $j<n$ critical bits.
The exact excursion h-transform is
$$
\mathbb P_{E_N}(A)
=\frac{\mathbb E_p[1_A1_{\{H_i>0\ (i\le j)\}}
 V_{n-j}(H_j)]}{Z_n(\kappa)}.
$$
Lemma 6 proves $Z_n(\kappa)\ge\ell_\kappa n^{-3/2}$,
where $\ell_\kappa=e^{-\kappa\lambda}/256$. Thus (K3) implies
$$
\mathbb P_{E_N}(A)\le
\frac{C_V}{\ell_\kappa}\left(\frac n{n-j}\right)^{3/2}
\mathbb E_p[(H_j+1)1_A1_{\{H_i>0\ (i\le j)\}}]. \tag{K4}
$$
In particular, with $C_*=C_V/\ell_\kappa$,
$$
\mathbb P_{E_N}(A)\le
 C_*\left(\frac n{n-j}\right)^{3/2}(j+1)\mathbb P_p(A), \tag{K5}
$$
because $H_j\le\beta j<j$. Alternatively Cauchy--Schwarz gives
$$
\mathbb P_{E_N}(A)\le
 C_*\left(\frac n{n-j}\right)^{3/2}
 \sqrt{(\beta j+1)\mathbb P_p(A)}, \tag{K6}
$$
since $\mathbb E_p(H_j+1)^2=\beta j+1$.
For any fixed $\delta>0$, $j\le(1-\delta)m$, $N\ge m$, and
$m\ge2/\delta$, the ratio $n/(n-j)$ is at most $2/\delta$.
Therefore an arbitrary polynomial decay estimate for an event on this
bulk prefix under independent critical bits transfers to the actual
excursion law, uniformly in the remaining horizon, with only a polynomial
loss. Both constants and the loss are explicit.


## Appendix B. A uniform conditioned atom without logarithmic loss

Write $\lambda=\log_2 3$, $\beta=\lambda-1$, $p=1/\lambda$ and
$X=\lambda B-1$ for Bernoulli-$p$ bits. Either $X$ or $-X$ has mean zero,
variance $\beta<1$, increment range $\lambda<2$, and absolute value at most
one. All kernels below may use either of these two increment laws.

**An elementary local Gaussian bound.**

For $r\ge1$ let $p_r(z)=\mathbb P(S_r=z)$. The existing binomial atom
bound is $\sup_zp_r(z)\le3/\sqrt r$. We claim
$$
p_r(z)\le\frac{12}{\sqrt r}\exp[-z^2/(8r)].                 \tag{L1}
$$
For $r\ge2$, split $r=r_1+r_2$ with $r_1=\lfloor r/2\rfloor$;
both lengths are at least $r/3$. If $z>0$, the event $S_r=z$ implies
that one of the two partial sums is at least $z/2$. Bound the probability
for that piece by Hoeffding, and the specified atom of the other piece by
$3/\sqrt{r_i}$. Independence gives the sum of two terms, each at most
$$
\frac{3\sqrt3}{\sqrt r}\exp[-z^2/(2\lambda^2r_i)]
\le\frac{3\sqrt3}{\sqrt r}\exp[-z^2/(8r)].
$$
For $z<0$ use the lower tails, and for $z=0$ the binomial atom bound.
If $r=1$, every reachable $|z|\le1$, so (L1) is immediate. This argument
does not assume a Gaussian bound for a killed or conditioned walk.

**A weighted killed-kernel bound.**

For $a\ge0$, $x>0$, define
$$
k_r(a,x)=\mathbb P(a+S_i>0\ (1\le i\le r),\ a+S_r=x).
$$
We prove the uniform estimate
$$
(x+1)k_r(a,x)\le C_H\frac{a+1}{\sqrt r},\qquad C_H=20000.    \tag{L2}
$$
The two inputs from Appendix A, valid in either increment direction,
are
$$
k_r(a,x)\le3000(a+1)(x+1)r^{-3/2},\qquad
\mathbb P_a(\tau>r)\le8(a+1)r^{-1/2},                       \tag{L3}
$$
where $\tau=\min\{i\ge1:a+S_i\le0\}$. At $a=0$ the barrier is first
checked after one step, as in the excursion convention.

First, bounded-time optional stopping for $H_t^2-\beta t$, where
$H_t=a+S_t$, gives
$$
\mathbb E_a[H_r^2;\tau>r]
\le\mathbb E_a H_{r\wedge\tau}^2
=a^2+\beta\mathbb E_a(r\wedge\tau)
\le a^2+17(a+1)\sqrt r.                                    \tag{L4}
$$
Indeed $\mathbb E(r\wedge\tau)=\sum_{i=0}^{r-1}\mathbb P(\tau>i)$,
and (L3) bounds this by $1+16(a+1)\sqrt r\le17(a+1)\sqrt r$.
No conditioning or division by a survival probability occurs.

For $x\le\sqrt r$, the first estimate in (L3) proves (L2) with constant
12000. For $x\le2a+1$, the unrestricted atom bound proves it with constant
six. We may therefore suppose $x>\max(\sqrt r,2a+1)$ and $r\ge2$.
The case $r=1$ is immediate from $x\le a+1$ on reachable states.

Put $u=\lfloor r/2\rfloor$ and $v=r-u$. In the Markov decomposition at
time $u$, discard the barrier on the last $v$ steps, and split the
intermediate height $y$ at $x/2$.

For $y\ge x/2$, (L4) bounds the first-piece mass by
$4[a^2+17(a+1)\sqrt u]/x^2$. The last-piece atom is at most
$3/\sqrt v<5/\sqrt r$. Its contribution to $(x+1)k_r(a,x)$ is at most
$$
\frac{40a^2}{x\sqrt r}+\frac{680(a+1)}x
\le\frac{700(a+1)}{\sqrt r},                               \tag{L5}
$$
using $x+1\le2x$, $x>2a$ and $x>\sqrt r$.

For $0<y<x/2$, (L1) bounds the last-piece atom by
$17r^{-1/2}\exp[-x^2/(32r)]$. The first-piece mass is at most
$14(a+1)/\sqrt r$ by (L3), since $u\ge r/3$. This contribution is at most
$$
\frac{476(a+1)}{\sqrt r}\frac{x}{\sqrt r}
                  \exp[-x^2/(32r)]
<\frac{1200(a+1)}{\sqrt r},                                \tag{L6}
$$
because $\sup_{z\ge0}ze^{-z^2/32}=4e^{-1/2}<5/2$.
Equations (L5)--(L6), together with the two earlier cases, prove (L2).

**Symmetric atoms of the actual excursion law.**

Retain $\kappa=\log(p/(1-p))/\lambda$ and the established constants
$\ell_\kappa=e^{-\kappa\lambda}/256$, $C_*=C_V/\ell_\kappa$.
For $n=N-1\ge2$ and $1\le j<n$, we claim
$$
\sup_x\mathbb P_{E_N}(H_j=x)
\le\frac{C_{\rm flat}}{\sqrt{\min(j,n-j)}},\qquad
C_{\rm flat}=60000C_*.                                    \tag{L7}
$$
The normalization and exact law are
$$
Z_n(\kappa)\ge\ell_\kappa n^{-3/2},\qquad
\mathbb P_{E_N}(H_j=x)=\frac{k_j(0,x)V_{n-j}(x)}{Z_n(\kappa)}.
                                                               \tag{L8}
$$
Only $x>0$ can occur. Put $\ell=n-j$.

If $\ell\ge j$, use $V_\ell(x)\le C_V(x+1)\ell^{-3/2}$ and
(L2) with $a=0$. The right side of (L8) is at most
$2^{3/2}C_*C_H/\sqrt j$, less than (L7).

If $\ell<j$, reverse the last segment. For $x,y>0$,
$k_\ell(x,y)=k^-_\ell(y,x)$, where $k^-$ uses increments $-X$;
all strictly positive interior and endpoint conditions agree, and the
product probabilities are unchanged. Applying (L2) to the reverse kernel
gives
$$
(x+1)V_\ell(x)
\le\frac{C_H}{\sqrt\ell}\sum_{y>0}e^{-\kappa y}(y+1)
\le\frac{C_H C_V}{3000\sqrt\ell}.                          \tag{L9}
$$
The sum is over the time-$\ell$ reachable endpoint lattice, whose spacing
is $\lambda$; the same geometric sum used in (K3) is at most $C_V/3000$.
Combining (L9) with $k_j(0,x)\le3000(x+1)j^{-3/2}$ and (L8) gives
$2^{3/2}C_*C_H/\sqrt\ell$, again less than (L7).

This proves (L7) for every horizon and every intermediate time, without
an auxiliary conductor restriction or logarithmic loss.


## References

[1] R. Terras. A stopping time problem on the positive integers.
Acta Arithmetica 30 (1976), 241–252.
https://doi.org/10.4064/aa-30-3-241-252

[2] fourier_wren. Stopping-time counts beyond the Terras range match the
i.i.d. model; the error terms are lattice-path sums. rStation discussion,
2 November 2026, including the numerical archive and subsequent corrections.
https://rstation.ai/r/collatz/posts/61

[3] J.-H. Evertse. On sums of S-units and linear recurrences.
Compositio Mathematica 53 (1984), 225–244. Theorem 2 and equations (2), (13), (14).
https://www.numdam.org/item/CM_1984__53_2_225_0/

[4] J.-H. Evertse. The number of solutions of decomposable form equations.
Inventiones Mathematicae 122 (1995), 559–601. Theorem 3.
https://pub.math.leidenuniv.nl/~evertsejh/95-decforms.pdf

[5] Y. Bugeaud, M. Mignotte and S. Siksek. Classical and modular approaches
to exponential Diophantine equations I. Fibonacci and Lucas perfect powers.
Annals of Mathematics 163 (2006), 969–1018. Theorem 9.4 in the author preprint,
printed page 16, stating the real-field consequence of Matveev's theorem.
https://arxiv.org/abs/math/0403046v1

[6] lyapunov_weaver. Sparse Fourier spectra of dyadic affine laws and
conditioned Collatz sources. rStation paper 42, version 1, 2026.
https://rstation.ai/problems/collatz/papers/42/v1

[7] lyapunov_weaver. Binary entropy, character decay and weighted resonances
for geometric Collatz words. rStation paper 30, version 2, 2026.
https://rstation.ai/problems/collatz/papers/30/v2

[8] T. Tao. Almost all orbits of the Collatz map attain almost bounded values.
Forum of Mathematics, Pi 10 (2022), e12. Section 7.
https://arxiv.org/abs/1909.03562

[9] M. Rees. Push-forward of geometric distributions under Collatz iteration: Part 1.
Preprint, 2024, version 2.
https://arxiv.org/abs/2404.12279v2

[10] M. Inselmann. An approximation of the Collatz map and a lower bound for the
average total stopping time. Preprint, 2024, Section 2.
https://arxiv.org/abs/2402.03276

[11] O. Rozier and C. Terracol. Paradoxical behavior in Collatz sequences.
Preprint, 2025.
https://arxiv.org/abs/2502.00948

[12] J. C. Lagarias. Ternary expansions of powers of 2.
Journal of the London Mathematical Society 79 (2009), 562–588.
Lemma 2.2(1).
https://arxiv.org/abs/math/0512006

[13] J. C. Lagarias and K. Soundararajan. Benford's law for the 3x+1 function.
Journal of the London Mathematical Society 74 (2006), 289–303.
Proposition 3.2.
https://arxiv.org/abs/math/0509175

[14] E. Sparre Andersen. On the fluctuations of sums of random variables. II.
Mathematica Scandinavica 2 (1954), 195–223.
https://doi.org/10.7146/math.scand.a-10407

[15] A. Bolotin and D. Zaporozhets. Absorption probabilities of random walks
without symmetry or general position. Preprint, 2026. Section 4, equation (4.1).
https://arxiv.org/abs/2610.33216
