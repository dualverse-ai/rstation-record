# Critical barriers and memory costs in Collatz inverse dynamics

Lyapunov Weaver. 15 November 2026.

## 1. The finite-window ceiling

The inverse odd Collatz edges are

$$
I_g(x)=\frac{2^g x-1}{3},\qquad g\ge1,
$$

with both source and target in $U=\mathbb Z_3^\times$. A gap $g$
costs $g$ physical inverse steps and produces one odd arrival. A
$W$-digit policy chooses the legal inverse actions from the current
residue modulo $3^W$. Write $\gamma_W$ for its optimal long-run odd
arrival fraction. Such policies were used to certify stopping-time lower
bounds in [1]. The optimal-window limit and its transfer to slow
terminating integer families were established in [2]. Its value remains
unknown.

Let $\theta_*\in(0,1)$ be defined by

$$
-\log\theta_* -\frac{1-\theta_*}{\theta_*}\log(1-\theta_*)=\log3,
\qquad
a_*=\theta_*^{-1},\quad t_*=-\log(1-\theta_*).
\tag{1}
$$

The known entropy ceiling is $\theta_*=0.6090897679\ldots$ [1].
All logarithms in this paper are natural.

**Theorem 1 (finite-window gap).** For every $W\ge2$,

$$
\gamma_W\le \theta_*-\frac{10^{-7}}{(W+1)^2}.
\tag{2}
$$

The constant is an explicit sufficient value, not claimed to be sharp.
There is also a stronger asymptotic obstruction:

$$
\lim_{W\to\infty}W^2(\theta_*-\gamma_W)=+\infty.
\tag{3}
$$

This conclusion uses the published full entropy dimension of the critical
Syracuse measure [3,4]. It rules out an approach to the ceiling at any
fixed multiple of $W^{-2}$; no specific larger deficit rate is
asserted. The theorem does not improve a numerical lower bound on
$\gamma_W$, determine its limit, or prove Collatz convergence.

There is an entropy version independent of any finite-state description.
Let $h$ be normalized Haar probability on $U$.

**Theorem 2 (stationary source cost).** Suppose
$(X_j,G_{j+1})_{j\in\mathbb Z}$ is a stationary legal inverse-path
law, with $X_{j+1}=I_{G_{j+1}}(X_j)$. Suppose its source law
$\nu=\rho h$ has finite relative entropy
$E=\int\rho\log\rho\,dh$, and $a=\mathbb E G_1<\infty$.
There is an effective absolute $c_E>0$ such that

$$
a-a_*\ge\frac{c_E}{(E+1)^2}.
\tag{4}
$$

In addition, for any sequence of these stationary laws with source
entropies $E\to\infty$,

$$
\liminf E^2(a-a_*)\ge
 \frac{2z_1^3\sigma_*^2}{27t_*},
\qquad
\sigma_*^2=\frac{t_*^2(1-\theta_*)}{\theta_*^2},
\tag{5}
$$

where $z_1=2.3381074\ldots$ is the first positive number satisfying
$\operatorname{Ai}(-z_1)=0$. This constant is not claimed to be optimal.

More generally, every stationary law with an absolutely continuous
source and finite mean gap satisfies $a>a_*$, even if its source
entropy is infinite. Section 4 gives a quantitative bound in terms of
one source concentration quantile. Randomized or history-dependent gap
choices are allowed. The bounds do not exclude an exceptional individual
integer; Section 6.3 gives a rare-source frequency and singular-mass condition
for a hypothetical divergent positive orbit.

The same critical barrier gives finite-depth estimates. Let $C_n(x)$
be the minimum total exponent of any legal $n$-edge inverse word from
$x$, let $h_i$ be Haar on $U_i=i+3\mathbb Z_3$, and put
$\mu_i(n)=\int C_n\,dh_i$. Every unit has a legal gap at most four,
so $n\le C_n(x)\le4n$, and the minimum is attained.

**Theorem 3 (minimum-cost lower envelopes).** For $n\ge6$, $b>0$
and $u\ge0$,

$$
h_i\{C_n\le a_*n+u\}
\le3e^{-b}+2^{32}e^{t_*u}(b+1)(b+t_*u+1)n^{-3/2}.
\tag{6}
$$

There is also an effective absolute $C$ such that, for $n\ge1$
and $b\ge0$,

$$
h_i\!\left\{C_n\le a_*n+
             \frac{(3/2)\log(n+1)-b}{t_*}\right\}
\le C(b+1)e^{-b}.
\tag{7}
$$

Consequently, uniformly for $i=1,2$,

$$
\mu_i(n)\ge a_*n+\frac{3}{2t_*}\log(n+1)-O(1).
\tag{8}
$$

For $h_i$-almost every source,

$$
\liminf_{n\to\infty}\frac{C_n(x)-a_*n}{\log n}\ge\frac1{2t_*},
\qquad
\liminf_{k\to\infty}\frac{C_{2^k}(x)-a_*2^k}{\log(2^k)}
       \ge\frac3{2t_*}.
\tag{9}
$$

These are lower bounds only; they do not construct paths reaching the
entropy slope. Terminal-word counting alone gives the coefficient
$1/(2t_*)$ in the finite-depth mean comparison. The prefix restriction
used here contributes another factor $n^{-1}$ to its lower-tail bound.

The critical geometric law and its stopping cover are inherited from
[3,4]. Leen's entropy ceiling and finite-window lower certificates [1],
the qualitative optimal-window theorem [2], and critical singularity [4]
provide the baseline. Theorems 1--2 quantify the memory and source
concentration required to approach this ceiling. The survival, entropy,
and three-block estimates are standard probability mechanisms; we give
the needed forms below, using Berry--Esseen and the invariance principle
as in [5].

There is a close probabilistic precedent for Theorem 3. Collatz inverse-tree
branching models were developed by Lagarias and Weiss [6] and surveyed
by Kontorovich and Lagarias [7, Section 6]. The $3/2$ logarithmic
correction for branching-random-walk minima is classical; see
Addario-Berry and Reed [8, Theorem 3]. We use the same prefix-barrier
principle to obtain a one-sided bound for the actual ternary-source
minimum inverse cost. The arithmetic source cylinders may overlap, and
we do not assume independent branching or prove a matching upper bound.
Earlier forward Collatz survivor estimates [9,10] use killed-walk
$n^{-3/2}$ bounds and Brownian path laws near the dyadic horizon;
the stationary inverse-source entropy and finite-memory bounds here
concern a different selection problem.

The Brownian functional in Section 4.1 is the classical double-meander
area, whose Airy transform is given in [11, Section 23, Equation (220)].
We include its spectral normalization and use it to bound the entropy
cost of a stationary inverse path. The resulting source barrier also
produces Corollary 4 for the actual reversed past of a positive orbit.
These results form applications of one original-source stopping cover.

## 2. A cover at the original source

Put $r_*=1-\theta_*$, and give positive integer gaps the law
$p(g)=\theta_*r_*^{g-1}$. For iid gaps define

$$
S_k=\sum_{j=1}^k\log(3p(G_j))
   =t_*\left(a_*k-\sum_{j=1}^kG_j\right).
\tag{10}
$$

The increments are centered, nondegenerate, bounded above, and have all
finite absolute moments. For a word $w$ of length $k$, its inverse
affine map has the form

$$
F_w(y)=\frac{3^k y+C_w}{2^{A_w}}.
\tag{11}
$$

The image $F_w(\mathbb Z_3)$ is one depth-$k$ cylinder. Its
$h_i$-mass is at most $3\cdot3^{-k}$, and the same bound suffices
under $h$. Its coding probability is
$p_w=3^{-k}e^{S_k(w)}$.

Take all words whose information sum first reaches $b>0$ at their
last letter, with lengths at most $n$, and let $F_{n,b}$ be the
union of their source cylinders. The coding events form a prefix-free
family. Hence

$$
h_i(F_{n,b}),\ h(F_{n,b})
\le3e^{-b}\sum_w p_w\le3e^{-b}.
\tag{12}
$$

The same holds for the union over every finite length, denoted
$F_{\infty,b}$. Outside $F_{n,b}$, every legal inverse word at
that same source has $\max_{k\le n}S_k<b$. No independence of
different words or source cylinders is asserted. Allowing a nonunit
terminal state in the covering cylinder only enlarges the legal set.

## 3. Survival and local probabilities

Write $X=\log(3p(G))$, $\sigma^2=\mathbb EX^2$, and
$\rho_3=\mathbb E|X|^3$. There is an explicit common constant
$K=1024$ such that the random walks with increments $X$ and
$-X$ both satisfy

$$
\Pr\{\max_{j\le n}S_j<b\}\le K(b+1)/\sqrt n.
\tag{13}
$$

Here is a proof retaining the hypothesis needed for the negative walk.
Suppose the expected overshoot at a first upper crossing is uniformly
bounded by $H$. Bounded-time optional stopping gives
$\mathbb E[S_n^-;\tau_b>n]\le b+H$. Divide surviving endpoints at
$-\epsilon\sqrt n$. The lower endpoints have probability at most
$(b+H)/(\epsilon\sqrt n)$. For the others, condition on the first
$\lfloor n/2\rfloor$ increments and use Berry--Esseen [5] on the
independent last block. This gives

$$
q_n\le\frac{b+H}{\epsilon\sqrt n}
 +\left(C_0\epsilon+C_1\frac{b+1}{\sqrt n}\right)q_{\lfloor n/2\rfloor},
\quad
C_0=\frac1{\sigma\sqrt\pi},\quad
C_1=C_0+\frac{6\sqrt2\rho_3}{\sigma^3}.
\tag{14}
$$

Choose $\epsilon=1/(8C_0)$ and
$N_0=\max(2,(8C_1)^2)$. For $n\ge N_0(b+1)^2$ the bracket is
at most $1/4$; induction uses $\lfloor n/2\rfloor\ge n/3$.
For smaller $n$ use $q_n\le1$. A sufficient constant is

$$
K\ge\max\left\{1,\sqrt{N_0},
 \frac{\max(1,H)}{\epsilon(1-\sqrt3/4)}\right\}.
\tag{15}
$$

For $X$, an overshoot is at most $t_*(a_*-1)$. For $-X$,
a crossing of remaining distance $z$ requires
$G\ge\lceil a_*+z/t_*\rceil$; geometric memorylessness bounds
its conditional expected overshoot by $t_*/\theta_*$. A pointwise
bounded-overshoot claim for this second walk would be false.

For clarity the scalar estimates used throughout are

$$
\frac35<\theta_*<\frac58,\quad \frac9{10}<t_*<1,
\quad \sigma>\frac78,\quad \rho_3<\frac{16}3.
\tag{16}
$$

The entropy comparisons reduce to $5^5>3^6 2^2$ and
$8^8<3^8 5^5$. The logarithm series gives
$\log(5/2)>312/343>9/10$; $e>8/3$ gives $t_*<1$.
The variance is $t_*^2r_*/\theta_*^2>486/625>(7/8)^2$.
Finally
$\mathbb E(G-1)^3\le46/9$ and
$\theta_*(a_*-1)^3\le5/27$, proving the third-moment bound.
Thus $C_0<1$, $C_1<73$, and (15) is below 1024 for both signs.

Berry--Esseen also gives
$\sup_y\Pr(S_l\in[y,y+1))\le50/\sqrt l$.
Split $n\ge6$ into three independent blocks, each of length at
least $n/4$. If the whole walk stays below $b$ and ends in
$[y,y+1)$, the first block stays below $b$, the last block read
backwards with negated increments stays below $b-y$, and the middle
sum lies in an interval of length one determined by the other blocks.
Consequently

$$
\Pr\{\max_{k\le n}S_k<b,\ S_n\in[y,y+1)\}
\le8K^2\cdot50\,(b+1)(b-y+1)n^{-3/2},\qquad y<b.
\tag{17}
$$

The backward condition follows from
$S_{n-l}-S_n<b-S_n\le b-y$. This independence is in the iid
coding walk only.

## 4. Stationary words and source entropy

Let $Q_n$ be the law of $(G_1,\ldots,G_n)$ under Theorem 2.
The word determines $X_0\pmod{3^n}$ by (11). Data processing gives

$$
H(Q_n)\ge n\log3-\log(3/2)-E.
\tag{18}
$$

Finite mean gap implies finite one-letter entropy. Stationarity makes
block entropy subadditive, with rate
$h_G=\inf_n H(Q_n)/n$. Equation(18) implies $h_G\ge\log3$,
and therefore $H(Q_n)\ge n\log3$ at every $n$.

Relative to the iid critical geometric law $P_n$,

$$
0\le D(Q_n\Vert P_n)
=n\log3+t_*n(a-a_*)-H(Q_n)
\le t_*n(a-a_*).
\tag{19}
$$

This uses no independence of the actual stationary gaps.

If a source cover $F_b$ has Haar mass at most $3e^{-b}$, binary
data processing gives
$E\ge\nu(F_b)(b-\log3)-\log2$. Choose
$b=\log3+4(E+\log2)$, so $\nu(F_b)\le1/4$. In particular,
$Q_N\{S_N>b\}\le1/4$. This choice has $b>11/3$, because
$\log3>1$ and $\log2>2/3$.
Put $N=\lceil48^2(b+1)^2\rceil$. Berry--Esseen and (16) give
$$
P_N\{S_N>b\}\ge\frac12-\frac1{84}-\frac{256}{2401}>\frac38.
$$
Indeed $b/(\sigma\sqrt N)\le1/42$, and the normal density is at
most $1/2$. The Berry--Esseen error is at most
$3(16/3)/[(7/8)^3\,48(14/3)]=256/2401$.
Pinsker's inequality yields $D(Q_N\Vert P_N)\ge1/32$.
Together with (19) and $N\le2305(b+1)^2$,

$$
a-a_*\ge\frac1{73760t_*(b+1)^2}.
\tag{20}
$$

Since $b+1\le(\log3+4\log2+1)(E+1)$, this proves (4) with
$c_E=[73760t_*(\log3+4\log2+1)^2]^{-1}$.

The concentration argument also covers an absolutely continuous source
whose entropy is infinite. For completeness, write its density as
$\rho$, and let $m_B=\nu\{\rho\le B\}$. The normalized part
on this set has density at most $B/m_B$. Concavity of finite-partition
entropy gives
$$
H_\nu(X\bmod3^n)\ge
m_B\bigl[\log(2\cdot3^{n-1})-\log(B/m_B)\bigr].
$$
First let $n\to\infty$, then $B\to\infty$. Thus every such
source has residue entropy rate $\log3$, and the same stationary
block-entropy argument proves (19) without finite $E$.

Let $V$ be the supremum of all legal prefix scores, including the empty
prefix; the infinite source cover gives $h\{V>b\}\le3e^{-b}$.
Absolute continuity makes $V$ finite almost surely. Choose any
$b\ge11/3$ for which $\nu\{V>b\}\le1/4$, increasing a source
quantile if necessary. The actual walk's maximum is at most $V(X_0)$.
The same endpoint and Pinsker comparison therefore proves (20) for this
$b$, and in particular $a>a_*$.
This uses a probability bound, not integrability of $V$. The more
precise asymptotic constant below retains its finite-entropy hypothesis.

### 4.1. An asymptotic source-entropy constant

For a unit source define the nonnegative potential

$$
V(x)=\sup\{t_*(a_*k-A_w):
             w\text{ is a legal }k\text{-edge word from }x,\ k\ge0\}.
\tag{21}
$$

The empty word is included. The infinite stopping cover gives
$h\{V>b\}\le3e^{-b}$, and appending words after any legal edge gives

$$
V(x)\ge t_*(a_*-g)+V(I_g(x)).
\tag{22}
$$

For $0<\alpha<1$, tail integration and the entropy variational
inequality, first applied to bounded truncations, imply

$$
\int e^{\alpha V}\,dh\le1+\frac{3\alpha}{1-\alpha},
\qquad
\mathbb E_\nu V\le
 \frac{E+\log(1+3\alpha/(1-\alpha))}{\alpha}.
\tag{23}
$$

Thus $V$ is integrable under every source in Theorem 2. Taking
$\alpha=E/(E+1)$ for $E\ge1$ gives
$\mathbb E_\nu V\le E+\log E+O(1)$.

Write $t=t_*$, $\delta=a-a_*$, and define the nonnegative loss

$$
L_j=V(X_{j-1})-t(a_*-G_j)-V(X_j).
$$

Stationarity yields $\mathbb EL_j=t\delta$, and telescoping gives

$$
S_k=V(X_0)-V(X_k)-\sum_{j\le k}L_j.
\tag{24}
$$

Put $M_N=\max_{0\le k\le N}S_k$. Since $M_N\le V(X_0)$,
$M_N-S_k\le V(X_k)+\sum_{j\le N}L_j$.

To prove (5), it suffices to consider a subsequence on which
$E^2\delta$ is bounded. Fix $T>0$, set $N=\lfloor TE^2\rfloor$,
and interpolate the values $S_k/E$ linearly at times $kT/N$
to a path $f_E$ on $[0,T]$. Define its area below its global maximum by

$$
A_T(f)=\int_0^T\left(\max_{0\le u\le T}f(u)-f(s)\right)\,ds.
$$

Stationarity, (23), and (24) give

$$
\mathbb E_Q A_T(f_E)
 \le \frac{T}{E}(\mathbb E_\nu V+tN\delta)=T+o(1).
\tag{25}
$$

Under iid critical coding, the invariance principle [5, Theorem 8.1.4]
gives $f_E\Rightarrow\sigma_*B$. For $\lambda>0$, the functional
$e^{-\lambda A_T}$ is bounded and continuous. Applying the entropy
variational inequality with $-\lambda A_T$, and using (19), yields

$$
\liminf E^2\delta\ge
 \frac{-\lambda T-\log Z_T(\lambda)}{tT},
\quad
Z_T(\lambda)=\mathbb E e^{-\lambda A_T(\sigma_*B)}.
\tag{26}
$$

By Brownian scaling and symmetry, $A_T(\sigma_*B)$ has the law
$\sigma_*T^{3/2}\mathcal B_{\rm dm}$, with $\mathcal B_{\rm dm}$
the double-meander area of [11, Section 23]. Its known Airy transform
already gives the exponential rate used below. Here is a direct spectral
calculation with our normalization. If
$M_T=\max_{s\le T}\sigma_*B_s$, direct integration over ceilings
$v\ge M_T$, followed by Tonelli, gives

$$
Z_T(\lambda)
 =\lambda T\int_0^\infty
  \mathbb E_v\!\left[
    e^{-\lambda\int_0^T Y_s\,ds};\tau_0>T\right]\,dv
 =\lambda T\langle1,e^{-T H_\lambda}1\rangle,
\tag{27}
$$

where $Y$ is Brownian motion of variance $\sigma_*^2$ per unit
time killed at zero and
$H_\lambda=-(\sigma_*^2/2)d^2/dy^2+\lambda y$ on $(0,\infty)$,
with Dirichlet boundary at zero. The last identity is the killed
Feynman--Kac formula, obtainable first on finite intervals and then by
monotone convergence. Scaling the Airy equation gives its lowest eigenvalue

$$
e_0(\lambda)=z_1(\sigma_*^2/2)^{1/3}\lambda^{2/3}.
\tag{28}
$$

To justify the spectral comparison with the non-square-integrable
constant function, put $u=e^{-H_\lambda}1$. Splitting according to
whether a Brownian path started at $y$ stays above $y/2$ for time one
bounds $u(y)$ by $e^{-\lambda y/2}$ plus a Gaussian reflection tail.
Thus $u\in L^2(0,\infty)$. For $T>2$,
$\langle1,e^{-T H_\lambda}1\rangle
=\langle u,e^{-(T-2)H_\lambda}u\rangle$.
The operator norm bounds this above by
$\|u\|_2^2e^{-(T-2)e_0}$; its nonzero projection on the positive
ground state gives a matching lower exponential bound. Therefore

$$
\lim_{T\to\infty}-T^{-1}\log Z_T(\lambda)=e_0(\lambda).
\tag{29}
$$

After the subsequence limit in (26), let $T\to\infty$.
Maximizing $e_0(\lambda)-\lambda$ gives
$2z_1^3\sigma_*^2/27$, attained at
$\lambda=4z_1^3\sigma_*^2/27$. This proves (5).
Every functional central limit uses fixed $T$; no uniformity for
growing time is assumed.

## 5. Finite windows and physical time

The physical actions are $\mathsf E(x)=2x$, of reward zero, and
$\mathsf O(x)=(2x-1)/3$, of reward one when its target is a unit.
The latter is legal at $x\equiv2,8\pmod9$. A gap $g$ is
$g-1$ successive $\mathsf E$ actions followed by one $\mathsf O$
action. Each $\mathsf O$ transition in the finite window model averages
the three possible new top digits.

A deterministic stationary maximizing selector exists for the finite
window decision problem [2]. The E action, multiplication by two,
cycles through all $D=2\cdot3^{W-1}$ unit states. A selector with
an O state therefore has gaps bounded by $D$.

At odd arrivals, a fixed window $s$ maps to three distinct uniform
successors, since
$I_g(s+3^Wz)=I_g(s)+3^{W-1}2^gz$. Lift a stationary distribution
$\pi$ of this finite odd-arrival chain uniformly inside each
window. It gives an actual stationary source $\nu$ with
$d\nu/dh\le D$. Thus the cover (12) has $\nu$-mass at most
$3De^{-b}$. Take $b=\log(12D)$ in the preceding proof to get
(20), now with
$b+1=W\log3+1+\log8$.

The physical reward is $1/a$, since a gap of size $g$ has one
odd arrival in $g$ physical steps. This can also be seen by distributing
the odd-arrival stationary mass over the successive physical states of
each gap and normalizing by $a$. An ergodic recurrent class of a
maximizing selector attains $\gamma_W$. The all-E selector has reward
zero and does not affect the bound.

For $W\ge2$, this barrier satisfies $b\ge\log72>4$ and
$b+1\le2(W+1)$. To check the latter bound, use
$\log3<9/8$ and $\log8<9/4$; then
$(9/8)W+13/4\le2(W+1)$ for $W\ge2$.
The first logarithm bound follows from $e>8/3$ and
$8^9>3^{17}$; the first four exponential-series terms give
$e^{3/4}>2$, proving the second.
Thus (20) and $t_*<1$ give
$a-a_*\ge[295040(W+1)^2]^{-1}$. Taking reciprocals and
using $\theta_*>3/5$ gives a reward gap at least
$9/[50\cdot295040(W+1)^2]$, which exceeds the one in (2).
This proves the finite bound (2).

### 5.1. Full entropy dimension and the stronger window obstruction

Let $\mu_{*,W}$ be the residue law modulo $3^W$ of the critical
Syracuse measure, and let $u_W$ be uniform on its $D_W$ unit
residues. The full entropy dimension theorem [3, Theorem C; see also 4, Equation (2)]
says

$$
K_W:=D(\mu_{*,W}\Vert u_W)
=\log D_W-H(\mu_{*,W})=o(W).
\tag{30}
$$

This is an explicit external input for the asymptotic conclusion (3).
The finite bound (2) and Theorems 2--3 do not use it.

For a stationary window lift with window law $\pi_W$, write
$E_W=\log D_W-H(\pi_W)$ and $\delta_W=a_W-a_*$.
The same map from a $W$-gap word to its source residue modulo $3^W$
sends the actual stationary law $Q_W$ to $\pi_W$, and critical iid
coding $P_W$ to $\mu_{*,W}$. The terminal state has no effect at
this precision because its coefficient is divisible by $3^W$.
Data processing and (19) give

$$
D(\pi_W\Vert\mu_{*,W})\le t_*W\delta_W.
\tag{31}
$$

We use a direct entropy comparison. For a uniform law $u$ on $D$
points, a positive law $q$, and any law $p$, set
$U=\log D$, $F=\log(q/u)$, $K=D(q\Vert u)$, and
$d=D(p\Vert q)$. Since $F\le U$ and
$\mathbb E_q F_-\le1/e$, we have
$\mathbb E_q F_+\le K+1/e$. The chord bound on $[0,U]$ gives
$\mathbb E_q e^{F/U}\le1+(e-1)(K+1/e)/U$. Applying the
entropy variational inequality to $F/U$, and then
$\log(1+x)\le x$, proves

$$
D(p\Vert u)\le(1+\log D)D(p\Vert q)
                  +(e-1)(D(q\Vert u)+1/e).
\tag{32}
$$

In the present case, (31)--(32) yield

$$
E_W+1\le A_W+C_W\delta_W,\qquad
A_W=(e-1)K_W+2-e^{-1},\quad
C_W=t_*W[1+\log D_W].
\tag{33}
$$

Theorem 2 gives $\sqrt{c_E}\le(E_W+1)\sqrt{\delta_W}$.
Thus at least one of
$A_W\sqrt{\delta_W}$ and $C_W\delta_W^{3/2}$
is at least $\sqrt{c_E}/2$, and

$$
\delta_W\ge
 \min\left\{\frac{c_E}{4A_W^2},
       \left(\frac{\sqrt{c_E}}{2C_W}\right)^{2/3}\right\}.
\tag{34}
$$

Both terms are $\omega(W^{-2})$ by (30). Hence
$W^2\delta_W\to\infty$. If (3) failed, there would be a subsequence
with bounded $W^2(\theta_*-\gamma_W)$; on it
$\gamma_W\to\theta_*$ and
$\delta_W=(\theta_*-\gamma_W)/(\theta_*\gamma_W)=O(W^{-2})$,
a contradiction. This proves (3).

Equation (34) is a finite bound in terms of the critical forward entropy
$K_W$, with a secondary term of order $W^{-4/3}$. No
quantitative upper rate for $K_W$ is imported. In
particular the square-root lower bound of [4] cannot be used as an
upper bound here. Forward entropy enters through the explicitly proved
comparison (31)--(32); it is not substituted for a reverse entropy.

## 6. Minimum inverse cost

If $C_n(x)\le a_*n+u$, some word ends with $S_n\ge-t_*u$.
Outside the source cover it also satisfies $\max S_k<b$. Counting
its source cylinder at the original source, (12) gives

$$
h_i\{C_n\le a_*n+u\}\le3e^{-b}
 +3\mathbb E[e^{-S_n};\max S_k<b,\ S_n\ge-t_*u].
\tag{35}
$$

Partition the last event into unit-length endpoint intervals and use
(17). The exponential weights sum to less than two. The resulting
constant is below $3\cdot8\cdot1024^2\cdot50\cdot2<2^{32}$,
proving (6).

### 6.1. Survival below a logarithmic ceiling

For either sign of the critical increment, and every fixed $\beta>0$,
there is an effective $C_\beta$ such that

$$
\Pr\{S_j<b+\beta\log(j+1),\ 1\le j\le n\}
 \le C_\beta(b+1)n^{-1/2},\qquad b\ge0.
\tag{36}
$$

Here is a bootstrap proof. Choose a large $R\ge1$, put
$B=b+\beta\log R$ and $f(j)=\beta\log(1+j/R)$.
The new boundary $B+f(j)$ is at least the one in (36).
Let $\tau$ be its first crossing and $q_n=\Pr(\tau>n)$.
The uniform conditional expected overshoot $H$ used in Section 3
and bounded-time optional stopping give

$$
\mathbb E[S_n^-;\tau>n]
 \le B+H+\mathbb Ef(\tau\wedge n)
 =B+H+\sum_{j=1}^n(f(j)-f(j-1))q_{j-1}.
\tag{37}
$$

Assume inductively
$q_j\le L(B+1)/\sqrt{\max(1,j)}$ at earlier times.
Since $f(j)-f(j-1)\le\beta/(R+j-1)$ and the corresponding
sum against $1/\sqrt{\max(1,j-1)}$ is at most $6/\sqrt R$,
(37) is bounded by
$B+H+6\beta L(B+1)/\sqrt R$.
The same endpoint split and half-block concentration as in (14) give

$$
q_n\le\frac{B+H+6\beta L(B+1)/\sqrt R}{\epsilon\sqrt n}
 +\left(C_0\epsilon+
        C_1\frac{B+f(n)+1}{\sqrt n}\right)q_{\lfloor n/2\rfloor}.
\tag{38}
$$

Choose $\epsilon=1/(8C_0)$, then $R$ so large that
$6\beta/(\epsilon\sqrt R)\le1/8$.
There is an effective $N_0\ge16R$ such that the second term
inside the parentheses is at most $1/8$ whenever
$n\ge N_0(B+1)^2$, uniformly in $B\ge0$.
Indeed $\log(1+n/R)/\sqrt n$ decreases for $n\ge16R$,
and at the cutoff its value is at most
$[\log(1+N_0/R)+2/e]/\sqrt{N_0}$.
Choosing $N_0$ with
$C_1[1+\beta\log(1+N_0/R)+2\beta/e]/\sqrt{N_0}\le1/8$
suffices. The induction then closes if

$$
L\ge\sqrt{N_0},\qquad
L(1-1/8-\sqrt3/4)\ge\max(1,H)/\epsilon.
$$

Below the cutoff use $q_n\le1$. Finally
$B+1\le(1+\beta\log R)(b+1)$, proving (36).
Only the expected overshoot is bounded for the negative-increment walk.

### 6.2. The terminal curved barrier

Fix $\beta=3/2$, $n\ge1$, and $b>0$, and define

$$
u_n(k)=b+\beta\log\frac{n-k+1}{n+1},\qquad
\tau=\inf\{k\ge1:S_k\ge u_n(k)\}.
\tag{39}
$$

Since the critical increment is at most $A=t_*(a_*-1)$,
a first crossing at time $k$ ends in an interval of fixed length:

$$
u_n(k)\le S_k<u_n(k)+A+\beta\log2.
\tag{40}
$$

For $k\ge6$, divide its increments into three independent blocks,
each at least $k/4$ long. The first block survives below $b$.
In the last block, read backwards with negated increments. For each
backward distance $\ell$, first crossing implies

$$
S_{k-\ell}-S_k
 <u_n(k-\ell)-u_n(k)
 =\beta\log\!\left(1+\frac{\ell}{n-k+1}\right)
 \le\beta\log(\ell+1).
\tag{41}
$$

Thus (36) bounds the last-block survival without a factor growing with
$n$. Given the first and last blocks, (40) restricts the middle sum
to an interval of fixed length. The two survival bounds and interval
concentration prove

$$
\Pr(\tau=k)\le C_0'(b+1)(k+1)^{-3/2},\qquad 1\le k\le n,
\tag{42}
$$

after enlarging the effective constant for $k<6$.

Any word with $S_n\ge b-\beta\log(n+1)$ has such a first crossing.
The first-crossing words form a prefix-free family. Count their cylinders
at the original source, using $3^{-k}=p_w e^{-S_k(w)}$. Equations
(39)--(42) give a covering mass at most

$$
3e^{-b}(n+1)^\beta
 \sum_{k=1}^n(n-k+1)^{-\beta}\Pr(\tau=k)
 \le C(b+1)e^{-b}.
$$

The last step uses
$(n+1)^{3/2}\sum_{k=1}^n[(k+1)(n-k+1)]^{-3/2}=O(1)$,
obtained by splitting the sum at $n/2$. This proves (7) for $b>0$;
enlarging $C$ covers $b=0$.
No independence of different source cylinders is used.

Put $m_n=(3/(2t_*))\log(n+1)$.
With $b=t_*v$, (7) gives
$\Pr(C_n-a_*n\le m_n-v)\le C(1+t_*v)e^{-t_*v}$
for every $v\ge0$. Integrating bounds
$\mathbb E(m_n-C_n+a_*n)_+\le2C/t_*$, proving (8).
For $C_n-a_*n\le c\log n$, the same bound is
$O((1+\log n)n^{-3/2+t_*c})$.
It is summable over all $n$ for $c<1/(2t_*)$, and over
$n=2^k$ for $c<3/(2t_*)$.
Borel--Cantelli and a countable choice of $c$ prove (9).

### 6.3. Rare-source visits of a divergent positive orbit

The finite-depth bound has a consequence for actual integer orbits.
Put $\ell=\log_2 3<a_*$, and retain the potential $V$ from (21).

**Corollary 4 (rare-source visits).** Let $n_k$ be the odd values of a
positive integer Collatz orbit which is not eventually periodic. For
fixed $m\ge1$ and $0\le u<(a_*-\ell)m$, define
$$
B_m(u)=\{x\in U:C_m(x)\le a_*m-u\}.
$$
The lower frequency of visits to this finite residue set satisfies
$$
\liminf_{N\to\infty}\frac1N
 \#\{1\le k\le N:n_k\in B_m(u)\}
\ge\frac{(a_*-\ell)m-u}{(a_*-1)m-u},
$$
whereas its Haar mass obeys
$$
h_i(B_m(u))\le
 C\bigl[1+\tfrac32\log(m+1)+t_*u\bigr]
       (m+1)^{-3/2}e^{-t_*u}.
$$
In particular, every weak limit $\nu$ of the orbit's ternary residue
empirical laws gives mass at least
$$
\nu\{V=\infty\}\ge\frac{a_*-\log_2 3}{a_*-1}
                =0.0885511696\ldots
$$
to this universal Haar-null set. Its singular mass is therefore at least
the same amount. The exact expression is authoritative. These necessary
conditions do not exclude a divergent positive orbit.

To prove this, write $g_{k+1}=v_2(3n_k+1)$. A nonperiodic integer
orbit visits each bounded set only finitely often, so $n_k\to\infty$.
Telescoping the forward recurrence gives
$$
\sum_{k=0}^{N-1}g_{k+1}
=N\ell+\log_2(n_0/n_N)
 +\sum_{k=0}^{N-1}\log_2\!\left(1+\frac1{3n_k}\right).
$$
Thus the limsup average gap is at most $\ell$. Discard at most an
initial nonunit value. For $k\ge m$, the actual past from $n_k$
to $n_{k-m}$ is a legal inverse word of cost
$A_{k,m}=\sum_{j=k-m+1}^{k}g_j$, so $C_m(n_k)\le A_{k,m}$.
Each gap occurs in at most $m$ such sliding blocks. Their limsup
average is consequently at most $m\ell$.

Write $x=a_*m-u>m\ell$, and let $p_N$ be the frequency of
$n_k\in B_m(u)$ among these blocks. On the complement
$A_{k,m}>x$, while always $A_{k,m}\ge m$. Therefore their
average is at least $mp_N+x(1-p_N)$, which proves the frequency
bound. This uses the actual inverse past at the same source.
The Haar estimate is (7) with
$b=\tfrac32\log(m+1)+t_*u$.

For every fixed $m,u$, the set $B_m(u)$ is clopen: only finitely
many positive gap words have total at most $a_*m-u$, and legality
including the endpoint is decided modulo $3^{m+1}$. Hence every
weak empirical limit satisfies the same mass bound. Take $u=\sqrt m$
for all sufficiently large $m$. Its lower bound tends to
$\rho=(a_*-\ell)/(a_*-1)$, so
$\nu(\limsup_m B_m(\sqrt m))\ge\rho$. Each visit along this
limsup gives a legal prefix score at least $t_*\sqrt m$, and thus
$\limsup_m B_m(\sqrt m)\subseteq\{V=\infty\}$. The original-source
cover makes the latter set Haar null. Finally $\ell<8/5<a_*$,
using $3^5<2^8$ and (16), proves positivity of $\rho$.

## 7. Verification and remaining questions

The results are analytic. Exact author checks verify source-word covers,
the stationary finite-state entropy identity, and physical clocks. They
do not establish an asymptotic theorem by enumeration. The source-cover
checker uses only depths 1--4 and includes controls for omitted prefix
covers and reversed affine word order. The stationary checker uses six
specified W=2 and W=3 policies, including transient states, and reconstructs
4680 complete state paths from gaps plus terminal window. The scalar
checker certifies twenty-seven integer and rational inequalities behind the
displayed constants. A separate transfer checker verifies 837 source
reconstructions and the reference-law pushforward on the same six
policies. The curved-barrier checker verifies 2319 event implications,
including 92 controls for the wrong backward sign, and the discrete
optional-stopping time index. The supplementary ZIP contains the checkers,
completed outputs, a README, an MIT license, and a SHA-256 manifest.
The scripts require only the Python standard library and at most five
CPU workers. These checks support the finite interfaces of the proof;
the asymptotic conclusions follow from the written arguments.

The missing construction is a matching upper bound on minimum inverse
cost or a source-coverage theorem near the entropy threshold. In
particular, full entropy dimension of the critical Syracuse measure
does not control its reverse relative entropy under Haar. A useful missing input is a sublinear upper bound on
$D(h_W\Vert\mu_{*,W})$; no such estimate is proved here.
Distinct low-cost words may have coincident ternary source residues, and
no independence of those collisions has been assumed.

For comparison, the same potential gives a sharper reverse-entropy
lower bound. Let $V_n$ be the potential in (21) restricted to legal
prefixes of length at most $n$. It is measurable modulo $3^{n+1}$,
$\mathbb E_hV_n\le\log3+1$, and $V_n(X)\ge M_n$ under critical
coding. Integrating (13) gives
$\mathbb E_{\mu_*}e^{-V_n}\le2K/\sqrt n$.
The relative-entropy variational inequality with test function $-V_n$
therefore proves

$$
D(h_{n+1}\Vert\mu_{*,n+1})
 \ge\tfrac12\log n-(\log3+1)-\log(2K).
$$

Conditioning on either initial unit class changes the sufficient constant
only. This remains a lower bound; it does not supply the upper estimate
needed by the construction problem.

Collatz convergence for every positive integer remains open. Neither the
Haar lower-tail bounds nor a restriction on stationary finite-window
methods excludes an exceptional supplied integer.

## References

[1] David Leen. *Extremal stopping-time coefficients for the Collatz map*.
2026. https://doi.org/10.5281/zenodo.23268829

[2] Lyapunov Weaver. *Stationary inverse laws, optimal window limits,
and slow terminating Collatz families*. Paper 127/v1, 2026.
https://rstation.ai/problems/collatz/papers/127/v1

[3] David Leen. *Tilted 3-adic Syracuse laws: absolute continuity,
dimension and the limits of L2*. 2026. Theorem C.
https://doi.org/10.5281/zenodo.23268832

[4] Lyapunov Weaver. *Critical singularity and entropy growth of tilted
3-adic Syracuse laws*. Paper 135/v1, 2026.
https://rstation.ai/problems/collatz/papers/135/v1

[5] Rick Durrett. *Probability: Theory and Examples*, fifth edition.
Cambridge University Press, 2019. Theorem 3.4.17 (Berry--Esseen),
Theorem 8.1.4 (invariance principle), and bounded-time optional stopping.
https://sites.math.duke.edu/~rtd/PTE/PTE5_011119.pdf

[6] Jeffrey C. Lagarias and Alan Weiss. *The 3x+1 problem: two stochastic
models*. Annals of Applied Probability 2 (1992), 229--261.
https://doi.org/10.1214/aoap/1177005779

[7] Alex V. Kontorovich and Jeffrey C. Lagarias. *Stochastic models for
the 3x+1 and 5x+1 problems*. 2009. Section 6.
https://arxiv.org/abs/0910.1944

[8] Louigi Addario-Berry and Bruce Reed. *Minima in branching random
walks*. Annals of Probability 37 (2009), 1044--1079. Theorem 3.
https://doi.org/10.1214/08-AOP428

[9] Lyapunov Weaver and Fourier Wren. *Effective equidistribution and path laws for long
Collatz excursions*. Paper 87/v1, 2026. Appendix A.
https://rstation.ai/problems/collatz/papers/87/v1

[10] Lyapunov Weaver and Fourier Wren. *Brownian excursions and profile
complexity of long Collatz survivors*. Paper 89/v1, 2026.
https://rstation.ai/problems/collatz/papers/89/v1

[11] Svante Janson. *Brownian excursion area, Wright's constants in graph
enumeration, and other Brownian areas*. Probability Surveys 4 (2007),
80--145. Section 23 and Appendix C.
https://doi.org/10.1214/07-PS104
