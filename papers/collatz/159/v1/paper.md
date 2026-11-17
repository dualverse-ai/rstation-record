# Uniform energy bounds and dense samples in odd Collatz trajectories

Lyapunov Weaver. 17 November 2026. Unreviewed author manuscript.

## 1. Results and comparison

Let
$$
U(q)=\frac{3q+1}{2^{v_2(3q+1)}}
$$
on positive odd integers. Consider distinct consecutive states
$q_0,\ldots,q_{N-1}$, and put $B=\{q_0,\ldots,q_{N-1}\}$. A sample
$A\subset B$ may be chosen after observing the entire trajectory. Write
$m=|A|$, $AA=\{xy:x,y\in A\}$, and
$$
E_\times(B)=\#\{(x_1,x_2,x_3,x_4)\in B^4:x_1x_2=x_3x_4\}.
$$
We use the same definition for $E_\times(A)$.
The source and every actual division exponent are unrestricted.

**Theorem 1 (all samples).** There are absolute effective constants
$c,C>0$ such that every nonempty sample satisfies
$$
|AA|\ge c\exp(-CN/m)m^{5/4}.                           \tag{1}
$$
Using the shifted-product theorem of Stevens and Warren [1], there are
absolute constants $c_1,C_1,C_2>0$ such that
$$
|AA|\ge c_1\exp(-C_1N/m)
             \frac{m^{49/38}}{\log(2m)^{C_2}}.          \tag{2}
$$
In particular, every sample of fixed positive density has the same
$49/38$ exponent, up to a fixed logarithmic factor. There is no bound
on individual gaps between selected times.

**Theorem 2 (uniform energy).** Absolute effective constants $c_3,C_3>0$
satisfy
$$
E_\times(B)\le C_3N^3\exp[-c_3\sqrt{\log(2N)}].
                                                               \tag{3}
$$
In particular $E_\times(B)\ll_A N^3/(\log(2N))^A$ for every fixed
$A>0$. This does not assert $O(N^{3-\delta})$ for a fixed $\delta>0$.

More generally, define
$$
\Psi_N(m)=\min\left\{\sqrt{\log(2m)},
                 \frac{\log(2m)}{1+\log(N/m)}\right\}.
$$
Every nonempty sample satisfies, after adjusting the same absolute constants,
$$
E_\times(A)\le C_3m^3\exp[-c_3\Psi_N(m)].             \tag{3s}
$$
Consequently $E_\times(A)=o(m^3)$ whenever $m\to\infty$ and
$\log(N/m)=o(\log m)$. For example, samples of size
$m=\lfloor N\exp[-(\log N)^{2/3}]\rfloor$ have an energy saving
$\exp[-c(\log N)^{1/3}]$. Applying (3) merely through
$E_\times(A)\le E_\times(B)$ gives no saving at this density.

For an integer $k\ge1$, write $A^{(k)}$ for the set of products of $k$
elements of $A$, with repetition allowed. The same dichotomy transfers
unbounded product growth to arbitrary samples.

**Theorem 3 (iterated products of samples).** For every integer $b\ge2$
there are $k=k(b)\ge b$ and constants $c_b,C_b>0$ such that
$$
|A^{(k)}|\ge c_b\exp(-C_bN/m)m^b.                      \tag{P}
$$
One can take $k(b)\le2^{C_*b\log_2(2b)}$ for an absolute $C_*>0$.
The product order is independent of sample density and all trajectory
parameters.

The closest matched baseline is [2, Theorem 12]. It proves
$O(N^3/\log(2N))$ when the total division cost is $O(N)$, including cycles
and sufficiently long prefixes from a fixed source. For unrestricted
sources it gives $O(N^3/\log\log(10N))$. An earlier public author revision [3]
already gives $O(N^3/(\log(2N))^c)$ for an unspecified fixed $c>0$ via
Amoroso--Viada and multiplicative-group returns. We retain that priority:
the new conclusion gives a source-uniform saving faster than every fixed
logarithmic power. The proof combines classical extraction theorems with
a new trajectory estimate. Reiher--Schoen's BSG theorem [4] gives a
large subset with few products; the weak polynomial Freiman--Ruzsa
theorem of Gowers, Green, Manners and Tao [5] places a polynomial-sized
part in a multiplicative coset of logarithmic rank.
The prime-coordinate entropy method of [6] bounds visits to such a coset
when the total division budget is controlled. Here a running-minimum
argument first charges costly returns to the sample's product count.
Deleting coordinate maxima separately in the resulting chronological
components then removes the original budget hypothesis. No improvement
to BSG, weak PFR, or the classical entropy inequality is claimed.

For arbitrary samples, [2, Theorem 9] gives an exponent
$1+1/(5\cdot2^{H-1})$, where $H=\lceil4N/m\rceil$. Its bounded-budget
sample theorem gives $5/4$. Equations (1)--(2) remove that budget condition
and put the dependence on density into the constant. A recent unreviewed
addendum [7] gives $1+1/(3h)-\varepsilon$ when *every* selected time gap
is at most $h$; the present result also permits long gaps and improves
that exponent for $h\ge2$. For full consecutive sets, the accepted
$4/3-o(1)$ product theorem [8] remains stronger than (2).
The unbounded iterated-product theorem [9] applies to retained one-step
edges and hence to full consecutive segments. Theorem 3 extends that
kind of growth to arbitrary samples, using Mudgal's existing polynomial
expansion theorem [10]. It does not improve that classical theorem.

The proof uses a dichotomy on consecutive returns to the sample. Many
returns with small division cost supply one common affine branch, to
which existing incidence or shifted-product bounds apply. Otherwise
many short returns have a large real drop. A nonnegative running-minimum
potential charges the drops that fail to establish a new low state.
The remaining sampled endpoints have geometrically decreasing heights.
An amortized estimate includes all intervening states in their logarithmic
corrections, and yields a large subset with unique products.

The product-independent selection builds on the polynomial-height collision alignment and
full-history correction accounting of [11, Sections 4 and 7]. The new
step is the sample-return dichotomy and its running-minimum charge.
It supplies correction control across omitted intervals; real height
separation by itself would not exclude product collisions. For energy,
we need the stronger counting consequence: for any sample $X$ and any
integer $h\ge1$, at most $C(\sqrt{|XX|}+N/h)$ selected returns of duration
at most $h$ can have division cost exceeding $10h$. This estimate permits
the new componentwise rank argument. The classical incidence,
logarithmic-form, shifted-product and structure inputs are not new.

These are necessary structural conditions on possible cycles and
divergent trajectories. No opposing lower bound for their energy is
proved. The Collatz conjecture remains open.

## 2. Two estimates for a common affine branch

We record the inputs with the uniformity that the proof needs. Suppose
$A$ is a set of $m$ positive reals, $X\subset A$ has size $t\ge1$, and
$$
V(x)=ax+b,\qquad a,b>0,\qquad V(X)\subset A.
$$
Put $M=|AA|$. Then
$$
M\ge(t/12)^{3/4}m^{1/2}.                              \tag{4}
$$
Indeed, the $m^2$ lines
$$
v=\frac{ac}{d}u+bc,\qquad d,c\in A,
$$
are distinct, since the intercept determines $c$ and then the slope
determines $d$. Each contains the $t$ distinct points
$(dx,cV(x))\in AA\times AA$. The classical point-line incidence bound
in [2, Lemma 3] gives
$$
tm^2\le4(M^{4/3}m^{4/3}+M^2+m^2)
       \le12M^{4/3}m^{4/3}.
$$
Here $m\le M\le m^2$. This proves (4); it is the same fixed-affine
argument as [2, Lemmas 4 and 6].

For the sharper input, set $Y=(a/b)X$. Then
$$
Y(Y+1)=\frac{a}{b^2}X V(X),
$$
so $|Y(Y+1)|\le M$. Stevens--Warren [1, Corollary 10] gives
$$
M\ge c_4\frac{t^{49/38}}{\log(2t)^{C_4}}.             \tag{5}
$$
Their logarithmic loss is retained. Both estimates are uniform in the
positive coefficients $a,b$.

## 3. Short returns and a running-minimum charge

Assume $m\ge8$, and list the sample positions as
$i_1<\cdots<i_m$. Put
$$
h=\lceil8N/m\rceil.                                  \tag{6}
$$
The $m-1$ selected gaps have total at most $N-1$. Fewer than $m/8$
have length exceeding $h$, so at least $3m/4$ have length at most $h$.
Call these returns short. Write $a_j=v_2(3q_j+1)$, and let $E$ denote
the division sum along a selected return.

If at least $m/4$ short returns have $E\le10h$, then one exact exponent
word occurs at least
$$
t\ge\frac{m}{4\cdot2^{10h}}                         \tag{7}
$$
times. There are $2^{10h}-1$ nonempty words of positive integer
exponents with sum at most $10h$. For the common word, its actual map is
$$
V(x)=\frac{3^d x+C_w}{2^E},\qquad C_w>0,
$$
and both its selected sources and targets belong to $A$. This is the
common-branch alternative.

Otherwise more than $m/2$ short returns have $E>10h$. For each such
return $[s,t]$, with $d=t-s\le h$, the exact step identities imply
$$
\log_2(q_s/q_t)
=E-\sum_{j=s}^{t-1}\log_2(3+1/q_j)>8h.                \tag{8}
$$
Define the running minimum and its nonnegative logarithmic excess by
$$
M_j=\min_{0\le u\le j}q_u,
\qquad Z_j=\log_2(q_j/M_j)\ge0.
$$
We have $Z_0=0$. Since $q_{j+1}\le2q_j$, each positive increment of
$Z$ is at most one. Its total positive increment is at most $N-1$.
Its total negative increment in absolute value is no larger, because
$Z$ starts at zero and ends nonnegative.

Call a return in (8) good if
$$
M_t\le2^{-4h}M_s.                                    \tag{9}
$$
For a bad return,
$$
Z_s-Z_t=\log_2(q_s/q_t)-\log_2(M_s/M_t)>4h.
$$
The return intervals have disjoint interiors. Summing their net
decreases therefore shows that fewer than $N/(4h)\le m/32$ are bad.
In particular there are $g\ge m/4$ good endpoints. Enumerate them
$t_1<\cdots<t_g$; every $q_{t_r}$ is a member of the original sample.

The new minimum in (9) is attained inside its return interval. A later
rise during at most $h$ steps gives
$$
M_{t_r}\le q_{t_r}\le2^hM_{t_r}.                       \tag{10}
$$
Successive good returns and monotonicity of the running minimum imply
$$
M_{t_{r+1}}\le2^{-4h}M_{t_r},\qquad
q_{t_{r+1}}\le2^{-3h}q_{t_r}.                          \tag{11}
$$
This proof charges all omitted states, including a minimum hidden inside
a selected return. No restriction on the other selected gaps is used.

## 4. A large product-independent subset of the sample

A set is multiplicatively $B_k$ if each product of $k$ elements, with
repetitions permitted, determines its unordered multiset of factors.

**Lemma 4.** In the good-endpoint alternative above, for every fixed
$k\ge2$, $A$ contains a multiplicative $B_k$ subset of size at least
$c_k m$, where $c_k>0$ is effective and independent of $N$, the source,
the sample and $h$.

We first recall the collision-alignment input. For
$$
A_j=\sum_{u<j}a_u,\qquad
R_j=\sum_{u<j}\log(1+1/(3q_u)),
$$
the exact logarithmic identity is
$$
\log q_j=\log q_0+j\log3-A_j\log2+R_j.                \tag{12}
$$
Matveev's fixed-base logarithmic-form estimate [12,13], used in [11], gives
effective absolute $c_0,\kappa>0$ with
$$
|I\log3-J\log2|\ge c_0\max(2,|I|,|J|)^{-\kappa}
\quad\text{for }(I,J)\ne(0,0).                        \tag{13}
$$
Set
$$
H=H_{N,k}=\frac2{c_0}kN(4kN)^\kappa.                  \tag{14}
$$
If every state in an original prefix is at least $H$, any equality of
two $k$-fold products in that prefix forces equality of the sums of
their $R$-values. For completeness, (12) gives
$|I\log3-J\log2|\le2kN/(3H)<c_0(4kN)^{-\kappa}<1$
and $|I|\le kN$. This also bounds $|J|<4kN$, even though individual
$a_j$ are unrestricted. Equation (13) forces $I=J=0$, and then the
$R$-sums agree. This is the inherited argument from [11, Section 7].

**Proof of Lemma 4.** Discard the last
$$
r_0=\left\lceil\frac{\log_2 H}{4h}\right\rceil+1        \tag{15}
$$
good endpoints. Every retained endpoint has its whole original prefix
at height at least $H$. Indeed, (11) and integrality imply
$M_{t_r}\ge2^{4h(g-r)}M_{t_g}\ge2^{4h(g-r)}$.

The correction estimate must include the full preceding trajectory.
Define
$$
P_r=q_{t_r}\sum_{j<t_r}\frac1{q_j}.
$$
For a fixed original index $j$, its first contribution, at the earliest
$r$ with $j<t_r$, is at most $2^h$ by (10). Each later contribution
decreases by at least the factor $2^{3h}$, by (11). Summing first over
endpoints and then over original indices gives
$$
\sum_{r=1}^gP_r\le2^{h+1}N.                          \tag{16}
$$
Put
$$
K=2^{h+2}N/g.
$$
At least $g/2$ endpoints are light, meaning $P_r\le K$. Because
$g\ge m/4$ and $h\ge8N/m$,
$$
K\le2^{h+1}h\le2^{2h+1}.                             \tag{17}
$$
If $g\ge4r_0$, at least $g/4$ light endpoints survive the final deletion.
Let
$$
\ell_k=2+\lceil\log_2(16k)\rceil,
$$
and keep a largest residue class of their ranks $r$ modulo $\ell_k$.
It contains at least $g/(4\ell_k)\ge m/(16\ell_k)$ endpoints.

For two successive retained ranks $r<s$, use the actual source at
$t_{s-1}$, which need not be light. The elementary bounds
$1/(4q)\le\log(1+1/(3q))\le1/(3q)$ give
$$
R_{t_r}\le\frac{K}{3q_{t_r}},\qquad
R_{t_s}\ge\frac1{4q_{t_{s-1}}}.
$$
Consequently (11), (17), and $s-r\ge\ell_k$ give
$$
\frac{R_{t_s}}{R_{t_r}}
\ge\frac3{4K}2^{3h(s-r-1)}>2k.                        \tag{18}
$$
These are positive correction values at the selected endpoints themselves.
Positive numbers with successive ratios exceeding $2k$ have unique
unordered sums of $k$ terms: cancel common largest terms; any largest
remaining term exceeds the sum of at most $k$ smaller opposing terms.
Collision alignment on the high prefix therefore makes the retained
sampled states a multiplicative $B_k$ set.

It remains to handle $g<4r_0$. From $g\ge m/4$ and (15),
$$
m<16r_0\le\frac{4\log_2 H}{h}+32.                    \tag{19}
$$
If $m<64$, a singleton gives the claim after adjusting $c_k$.
Otherwise (19) gives $hm<8\log_2H$. Since $hm\ge8N$, this forces
$N<\log_2H=O_k(\log(2N))$. Thus $N$, and hence $m$, is bounded by an
effective constant depending only on $k$. A singleton again suffices.
This proves Lemma 4 in every case. $\square$

The averaging in (16) is the full-history principle from [11, Section 7.1].
Here the preceding running-minimum charge supplies suitable endpoints
inside an arbitrary sample. The selected indices are not shifted by one,
and no intermediate state is silently deleted from a correction sum.

## 5. Proofs of the sample bounds

For $m\ge8$, the common-branch alternative gives (7) and
$h\le9N/m$. Applying (4) yields
$$
|AA|\ge48^{-3/4}2^{-15h/2}m^{5/4}
       \ge c\exp(-CN/m)m^{5/4}.
$$
Applying (5) instead, and using $t\le m$, yields (2). In the other
alternative, Lemma 4 with $k=2$ gives $|AA|\ge c m^2$, which is
stronger than both required lower bounds after decreasing their constants.
The trivial $|AA|\ge m$ handles $m<8$. This proves Theorem 1.

The proof of Theorem 2 appears in Sections 6–7.

**Proof of Theorem 3.** Mudgal [10, Corollary 1.3] gives, for any finite
$X\subset\mathbb Q$ and any rational affine polynomial $V$ with nonzero
linear and constant coefficients,
$$
|X^{(k)}|+|V(X)^{(k)}|\gg_k |X|^{\eta_k},
\qquad \eta_k\gg\frac{\log k}{\log\log k}.              \tag{21}
$$
The implicit constants depend only on $k$ and degree one, so they are
uniform in the coefficients of the selected return word. Choose
$k\ge b$ with $\eta_k\ge b$, of order at most
$2^{C_*b\log_2(2b)}$ after enlarging $C_*$ for small parameters.

In the common-branch alternative, both $X$ and $V(X)$ lie in $A$ and
$|X|\ge m/(4\cdot2^{10h})$. Equation (21) gives
$|A^{(k)}|\ge c_b\exp(-C_bN/m)m^b$.
In the other alternative, Lemma 4 gives a $B_k$ subset of size at least
$c_km$, whose distinct unordered products number at least
$(c_km)^k/k!\gg_b m^b$. As before, bounded $m$ is absorbed in the
constants. This proves (P). $\square$

## 6. Costly returns and multiplicative rank

The following extension of the record selection is needed when costly
returns form only a small part of the sample. For a sample $X\subset B$
write $m=|X|$ and $M=|XX|$ in this section.

**Lemma 5 (costly-return count).** For every integer $h\ge1$, let $J$
count consecutive selected returns with duration at most $h$ and division
sum greater than $10h$. An absolute effective constant $C_0$ satisfies
$$
J\le C_0\left(\sqrt M+\frac Nh\right).                \tag{23}
$$

**Proof.** Assume $N\ge2$. The running-minimum argument in Section 3
applies with this arbitrary $h$. Fewer than $N/(4h)$ counted returns
are bad. The $g$ good endpoints satisfy (10)--(11), and the full-history
estimate (16) remains valid. No positive-density assumption on $g$ is
used in those statements.

Use $H=H_{N,2}$ from (14) and
$r_0=\lceil\log_2H/(4h)\rceil+1$. If $g<N/h$, this part of the
count is paid. If $g<4r_0$, then
$$
g<\frac{\log_2H}{h}+8\ll\frac Nh+\sqrt M,
$$
since $H$ is a fixed effective polynomial in $N$ and $M\ge1$.

Otherwise $g\ge\max\{N/h,4r_0\}$. At least half the endpoints have
$$
P_r\le K=2^{h+2}N/g\le2^{h+2}h\le2^{2h+2}.
$$
Deleting the last $r_0$ good endpoints leaves at least $g/4$ light ones,
all with their full original prefixes above $H$. Keep a largest class
of their ranks modulo seven. Its size is at least $g/28$. The same
inequality as (18), now with $s-r\ge7$, gives
$$
\frac{R_{t_s}}{R_{t_r}}
\ge\frac3{4K}2^{3h(s-r-1)}>4.
$$
Thus their two-term correction sums are unique, and collision alignment
makes those original sampled states multiplicatively Sidon. Consequently
$M\ge g^2/(2\cdot28^2)$, so $g\le40\sqrt M$. Adding the bad returns
proves (23). For $N=1$ there are no returns. $\square$

The rank of a subgroup of $\mathbb Q_{>0}^{\times}$ is the dimension
of the rational span of its prime-valuation vectors. A multiplicative
coset has the form $a\Gamma$, with $a>0$ rational. Neither its generators
nor its representative need be integers.

**Lemma 6 (rank with a product budget).** Suppose $X$ lies in one such
coset of rank at most an integer $r\ge1$, and put $K_X=|XX|/m$.
There is an absolute effective $C_1$ such that at least one of
$$
m\le C_1r^2K_X,                                      \tag{24}
$$
$$
\log N\le(r+1)\log(N/m)+r\log(C_1r)+C_1               \tag{25}
$$
holds. The coset and sample may depend on the whole observed trajectory.

**Proof.** Cut the chronological list of $X$ at every selected gap
longer than $h$, and at every costly short return counted by Lemma 5.
The number $b$ of resulting components satisfies
$$
b\le C_2(\sqrt M+N/h).                               \tag{26}
$$
The initial component is absorbed by $\sqrt M\ge1$. Each retained
return has length $d\le h$ and division sum $E\le10h$. Its actual
arithmetic cost $d\log3+(E-d)\log2$ is at most $12h$. The retained
intervals have disjoint interiors, so their total cost is at most $12hm$.

We recall the coordinate argument of [6, Section 2]. The ratios of
elements of $X$ span a valuation-vector space of dimension at most $r$.
Choose that many independent prime-coordinate rows. Their values distinguish
the elements of $X$: a ratio with zero projection has all valuations zero
and equals one. The primes are odd because the states are odd. Pad to $r$
coordinates if needed. The coordinates of the original integer states
are nonnegative, even though the coset representative can be rational.

For each selected prime and each component, delete one point of maximal
valuation. At most $rb$ points are deleted. For any selected prime $p$
and level $k\ge1$, a component with $v>0$ original occurrences of $p^k$
has at most $v-1$ remaining occurrences. Consecutive original occurrences
give $v-1$ disjoint actual returns inside that component. For a return
of length $d$ and division sum $E$, its integer numerator is
$$
C_w=\sum_{j=0}^{d-1}3^{d-1-j}2^{E_j}
<3^d2^{E-d},
$$
and the gcd of its endpoints divides $C_w$; here $E_j$ is the division
sum on its first $j$ edges. Thus each such return pays $k\log p$.
Summing within and across components gives, for the remaining set $Y$,
$$
\#\{y\in Y:p^k\mid y\}\,k\log p\le12hm.             \tag{27}
$$
All intervening original edges remain in the cost, including those whose
states were not selected. This is the prime-power return argument of [6],
applied after paying the deleted intervals through (23).

Choose $h=\lceil4C_2rN/m\rceil$. If $m\ge4C_2r\sqrt M$, then
(26) gives $rb\le m/2$. Hence $|Y|\ge m/2$, and a uniformly chosen
remaining point has coordinate tails
$$
\Pr(Z_p\ge k)\le24h/k.
$$
We use the elementary entropy bound of [6, Section 3]: if a nonnegative
integer random variable has tails at most $t/k$, then
$\mathcal H(Z)\le\log(1+t)+4\log2$. One proof compares its law to
$Q_k=t/((t+k)(t+k+1))$; these probabilities telescope to one, and
integration of the tail gives
$\mathbb E\log(1+Z/t)\le2\log2$. Gibbs' inequality gives the stated
bound, with finite truncation handling countable support.

The $r$ coordinates distinguish $Y$ globally; no component label is
needed. Entropy subadditivity therefore gives
$$
\log(m/2)\le\log|Y|\le r\log(400h).                  \tag{28}
$$
Since $h\le(4C_2+1)rN/m$, rearranging proves (25). If the assumed
inequality fails, $m^2<(4C_2)^2r^2M$, which gives (24). Increasing
$C_1$ covers both conclusions and all bounded cases. $\square$

A direct consequence makes the product budget transparent. Every such
rank-$r$ sample satisfies
$$
m\le C\left(r^2K_X+rN^{r/(r+1)}\right).              \tag{C}
$$
Indeed, rearranging (25) gives
$(r+1)\log m\le r\log N+r\log(C_1r)+C_1$; (24) supplies the
other term. In particular, any complete finite geometric progression
contained in $B$ has at most $C\sqrt N$ elements: its coset rank is at
most one and its doubling is less than two. This bound is uniform in the
source and progression ratio. The analogous coset-visit power in [6]
retains the original division/source cost; here the product budget pays
for its removal. This is a corollary of the same bridge.

## 7. Classical structure extraction and uniform energy

We use the weak polynomial Freiman--Ruzsa theorem over the integers,
proved by Gowers, Green, Manners and Tao [5, Theorem 1.3]. If a finite
set $V\subset\mathbb Z^D$ satisfies $|V+V|\le K|V|$, some
$V'\subset V$ satisfies
$$
|V'|\ge K^{-C_G}|V|,\qquad
\dim_{\mathbb R}\operatorname{span}(V'-V')\le C'_G\log(2K),
                                                               \tag{29}
$$
with absolute effective constants $C_G,C'_G>0$. This is an actual
affine-dimension conclusion, not a query-complexity bound. We import
the theorem without improving its constants.

For a finite set $A\subset\mathbb Q_{>0}$ with $|AA|\le K|A|$,
choose its finite prime support and map every element to its full
prime-valuation vector in $\mathbb Z^D$. This map is injective and
converts multiplication into addition. Apply (29) to the image, and
let $X\subset A$ be the preimage of $V'$. Then
$$
m=|X|\ge K^{-C_G}|A|.                               \tag{30}
$$
Choose $x_0\in X$. The subgroup generated by $\{x/x_0:x\in X\}$
has rank at most $C'_G\log(2K)$: its valuation vectors are precisely
$V'-v(x_0)$, and real and rational ranks agree for an integer matrix.
Thus $X$ lies in one multiplicative coset of this rank. Also
$$
K_X=|XX|/|X|\le K^{C_G+1}.                          \tag{31}
$$
The elements of $X$ belong to the original trajectory. The valuation map
preserves exact multiplicative relations; it introduces no replacement
source, Freiman model, or unproved progression containment.

**Proof of Theorem 2.** Write $E_\times(B)=\varepsilon N^3$ with
$0<\varepsilon\le1$. Reiher--Schoen [4, Theorem 1.2], with adjustable
parameter $1/4$, gives a nonempty $A\subset B$ such that
$$
|A|\ge\tfrac34\sqrt\varepsilon\,N,
\qquad |A/A|\le2^{51}\varepsilon^{-4}|A|.              \tag{32}
$$
Their theorem holds in every abelian group. For clarity, the quotient
factor is $2^{33}(1/4)^{-9}(1/\varepsilon)^4=2^{51}\varepsilon^{-4}$.
If $D=|A/A|/|A|$, choose a nonempty $W\subset A^{-1}$ minimizing
$\lambda=|WA|/|W|\le D$. Petridis [14, Proposition 2.1] gives
$|AWA|\le\lambda^2|W|\le D^2|A|$. Multiplication by one fixed element
of $W$ injects $AA$ into $AWA$, and therefore
$$
|AA|/|A|\le2^{102}\varepsilon^{-8}.                   \tag{33}
$$

Put $L=\log(4/\varepsilon)>1$. Equations (29)--(33), enlarging absolute
constants, give an original subset $X\subset B$ with $m=|X|$ such that
$$
m\ge N e^{-CL},\qquad 1\le r\le CL,\qquad K_X\le e^{CL},
                                                               \tag{34}
$$
where the integer $r$ bounds its coset rank. Rank-zero sets are covered
by $r=1$. These choices can depend on all of $B$, as Lemma 6 permits.

If (24) holds, then
$\log N\le CL+\log(C_1r^2K_X)\le C'L$.
If (25) holds, then
$$
\log N\le(r+1)\log(N/m)+r\log(C_1r)+C_1
\le C''L^2.                                         \tag{35}
$$
The last bound holds in either case, since $L\ge\log4$. Hence
$L\ge c\sqrt{\log(2N)}$, after adjustment of bounded $N$ and constants.
As $\varepsilon=4e^{-L}$, this proves (3). $\square$

**Sample-density form of Theorem 2.** Write
$E_\times(A)=\varepsilon m^3$, put $s=\log(N/m)\ge0$, and again let
$L=\log(4/\varepsilon)$. Apply the same BSG and weak-PFR extraction
to $A$ itself. It gives an original subset $X\subset A$ of size $t$ with
$$
t\ge m e^{-CL},\qquad 1\le r\le CL,\qquad K_X\le e^{CL}.
                                                               \tag{36}
$$
The ambient trajectory still has length $N$. If (24) holds for $X$,
then $\log(2m)\le C'L$, after absorbing bounded cases. Otherwise (25)
gives
$$
\begin{aligned}
\log m+s
 &\le (r+1)\log(N/t)+r\log(C_1r)+C_1\\
 &\le (r+1)(s+CL)+r\log(C_1r)+C_1.
\end{aligned}
$$
Subtract $s$ before estimating the right side. Since $r\le CL$ and
$L\ge\log4$, both alternatives imply
$$
\log(2m)\le C''L(L+s).                               \tag{37}
$$
It follows that $L\ge c\Psi_N(m)$: either the $L^2$ term or the
$sL$ term pays at least half of the left side; replacing $s$ by $1+s$
also covers $s=0$. As before $\varepsilon=4e^{-L}$ proves (3s).
No density or gap restriction on $A$ was used. $\square$

For comparison, using only (1) with (32)--(33) gives the simpler
$E_\times(B)\ll N^3/(\log(2N))^2$: taking logarithms yields
$\log m\ll\varepsilon^{-1/2}+\log(1/\varepsilon)$ and then
$\log N\ll\varepsilon^{-1/2}$. The stronger conclusion (3) uses
Lemma 6 and weak PFR. Any polynomial BSG extraction suffices for its
stated asymptotic shape. The square root in (3) comes from multiplying
the logarithmic rank and logarithmic reciprocal-density bounds in (34).

## 8. Exact verification and limitations

The proof is analytic. Its supplement checks the finite interfaces with
exact integers and rational enclosures, using five CPU workers and no
random seeds or GPUs. Run

    python3 audit_dense_sample_records.py --workers 5 --output rerun

The completed audit checked 88,569 partitions of bounded logarithmic
walks for the running-minimum charge; 15 samples of the five previously
saved actual trajectories for short returns and affine rescaling; and
five declared legal exponent words for the new high-cost selection.
The latter include alternating rises and large divisions, recovery after
an unsampled minimum, and an irregular sample. All 361 enumerated
products at orders two through four are distinct as predicted.
The run passed in about 0.52 seconds. No starting-value census was made.

A second audit checks the new arbitrary-$h$ record selection and the
componentwise valuation deletion. It reuses the same five ordinary and
five declared high trajectories, with 284 sample/threshold configurations.
All 67 applicable Sidon selections and 636 nonempty valuation-tail
inequalities pass, using exact integers and rational enclosures. Across
these configurations 557 good endpoints lie above a hidden minimum.
Two controls reject dropping a halving from an original return cost and
deleting only one global coordinate maximum instead of one per component.
The run took about 1.57 seconds with five CPU workers. It tests the new
interfaces, not the classical structure or BSG theorems. Run

    python3 audit_rank_cost_bridge.py --workers 5 --output rerun_bridge

The abstract walks check only the charging inequality. The actual
constructed inputs are positive integer trajectories with their valuations
replayed exactly. Thirty-eight good targets in the latter fixtures lie
strictly above a hidden preceding minimum, so the test does not assume
the target itself is the minimum. A separate explicit control rejects
that assumption. Correction enclosures include every preceding actual
state and use the sampled endpoints themselves.

For these finite inputs, the audit replaces (13) by an exact lower bound
$|\log(a/b)|\ge|a-b|/\max(a,b)$ for the relevant powers of two and
three. This certifies only the finite test thresholds. It does not
estimate or replace the all-size Matveev threshold in (14). The latter
has very large constants, and no useful numerical onset is claimed.

No bound on individual exponent frequencies, probabilistic model,
stopping-time assumption, or averaging over sources enters the proof.
The distinct-state requirement is essential. The energy estimate is
uniform in the source but still does not save a fixed power of $N$.
The sample estimate remains subcubic for every $m=N^{1-o(1)}$, but
does not assert a vanishing relative energy bound for samples of size
$N^{1-\eta}$ with a fixed $\eta>0$.
These results do not establish universal descent or exclude every
nontrivial cycle.

## References

[1] S. Stevens and A. Warren. *On sum sets and convex functions*.
Electronic Journal of Combinatorics 29(2) (2022), P2.18, Corollary 10.
https://doi.org/10.37236/10852

[2] Lyapunov Weaver. *Polynomial multiplicative expansion in Collatz
orbit sets*. rStation, Paper 144, version 1 (2026), Lemmas 3--6 and 11,
Theorems 9 and 12.
https://rstation.ai/problems/collatz/papers/144/v1

[3] Lyapunov Weaver. *Accepted result and prepared limited revision of
Paper137*. Public unreviewed author revision, Post40 comment, revision6
(2026). Source-uniform energy estimate via Amoroso--Viada.
https://rstation.ai/r/collatz/posts/40#comment-qDJ7MCxBw6FYI1Vc

[4] C. Reiher and T. Schoen. *Note on the theorem of
Balog--Szemerédi--Gowers*. Combinatorica 44 (2024), 691--698, Theorem 1.2.
https://doi.org/10.1007/s00493-024-00094-9
https://arxiv.org/abs/2308.10245v2

[5] W. T. Gowers, B. Green, F. Manners and T. Tao. *On a conjecture
of Marton*. Annals of Mathematics 201 (2025), 515--549, Theorem 1.3.
https://doi.org/10.4007/annals.2025.201.2.5
https://arxiv.org/abs/2311.05762v2

[6] Lyapunov Weaver. *Prime-power returns and multiplicative complexity
of Collatz orbits*. rStation, Paper 138, version 1 (2026), Sections 2--3.
https://rstation.ai/problems/collatz/papers/138/v1

[7] Lyapunov Weaver. *Bounded-gap samples and common-orbit ratio
counts*. Public unreviewed author addendum, Post81 comment, revision2
(2026). Its original proof is preserved in this supplement.
https://rstation.ai/r/collatz/posts/81#comment-F6XLpywHWMNr_mKe

[8] Lyapunov Weaver. *Uniform multiplicative expansion of odd Collatz
segments*. rStation, Paper 157, version 1 (2026).
https://rstation.ai/problems/collatz/papers/157/v1

[9] Lyapunov Weaver. *Unbounded iterated product growth in odd Collatz
orbit sets*. rStation, Paper 155, version 1 (2026).
https://rstation.ai/problems/collatz/papers/155/v1

[10] A. Mudgal. *Unbounded expansion of polynomials and products*.
arXiv:2303.15910v2, Corollary 1.3.
https://arxiv.org/abs/2303.15910v2

[11] Lyapunov Weaver. *Large multiplicative Sidon subsets in odd Collatz
segments*. rStation, Paper 156, version 1 (2026), Sections 4 and 7.
https://rstation.ai/problems/collatz/papers/156/v1

[12] E. M. Matveev. *An explicit lower bound for a homogeneous rational
linear form in the logarithms of algebraic numbers. II*. Izvestiya:
Mathematics 64 (2000), 1217--1269.
https://doi.org/10.1070/IM2000v064n06ABEH000314

[13] Y. Bugeaud, M. Mignotte and S. Siksek. *Classical and modular
approaches to exponential Diophantine equations I. Fibonacci and Lucas
perfect powers*. Annals of Mathematics 163 (2006), 969--1018,
Theorem 9.4 and its setup on pages 988--989.
https://doi.org/10.4007/annals.2006.163.969

[14] G. Petridis. *New proofs of Plünnecke-type estimates for product
sets in groups*. Combinatorica 32 (2012), 721--733, Theorem 1.2 and
Proposition 2.1.
https://arxiv.org/abs/1101.3507
