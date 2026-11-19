# Arithmetic restrictions on sparse periodic Collatz itineraries

Lyapunov Weaver. Author manuscript, 18 November 2026. Not yet reviewed.

## 1. The structural case and the new result

A global period-$p$ skeleton for a one-sided infinite word fixes one letter
on each residue class modulo $p$, except for specified holes. A hole can
carry different letters in different aligned blocks. We consider skeletons
at an unbounded sequence of periods; neither nesting nor a fixed rule for
filling the holes is assumed.

For the shortcut Collatz map

$$
C(x)=\begin{cases}x/2,&x\equiv0\pmod2,\\(3x+1)/2,&x\equiv1\pmod2,\end{cases}
$$

let $\Phi(w)\in\mathbb Z_2$ be the unique source with binary parity word
$w$. For an exponent word $e$, execution means that the actual odd
endpoints satisfy $x_{i+1}=(3x_i+1)/2^{e_i}$ and
$e_i=v_2(3x_i+1)$. Thus its binary coding is $e\mapsto10^{e-1}$.
Write $\beta=\log_2 3$.

**Theorem 1 (two holes, arbitrary geometry).**

1. If a non-eventually-periodic binary word has global skeletons with at
   most two holes at unbounded periods, its $\Phi$-value is not a positive
   rational with odd denominator.
2. If a non-eventually-periodic exponent word over $\{1,\ldots,E\}$,
   with $E$ fixed, has such skeletons, no positive rational with odd
   denominator executes it.

The same conclusions hold for exactly three holes whose internal and
boundary gaps all tend to infinity. More generally, the following bounds
hold for any fixed hole count.

**Theorem 2 (separated holes).** Suppose the skeletons have exactly $m\ge1$
holes $0\le t_1<\cdots<t_m<p$ and

$$
\min\{t_1,t_2-t_1,\ldots,t_m-t_{m-1},p-1-t_m\}\longrightarrow\infty. \tag{1}
$$

The uniform mean $\alpha$ in the exponent case, or uniform one-density
$\rho$ in the binary case, exists. Positive rational execution is impossible
in the respective ranges

$$
\frac{m\beta}{m+2}<\alpha<\beta,
\qquad
\frac1\beta<\rho<\frac{m+2}{m\beta}.                       \tag{2}
$$

Non-eventual-periodicity is unnecessary in these contracting ranges.
For non-eventually-periodic words the respective ranges $\alpha\ge\beta$
and $\rho\le1/\beta$ are also excluded, by the inherited argument in
Section 6. Since $3\beta<5$, (2) covers every contracting mean or density
for $m=2,3$.

The accepted sparse-feature result [1] proves the exponent bound
$\alpha>m\beta/(m+1)$ without a geometric condition. Clustered holes are
already covered without a mean restriction by [2], even for signed
rational sources. The new result removes the mean restriction for two
arbitrarily placed holes and improves the separated-hole threshold.
The binary statement requires an additional positivity identity: a raw
binary feature can be negative, whereas the reduced coordinates used
here are positive.

The approximation framework and bounded-feature representation come from
[1] and the aligned-dictionary method [3], with generalized-series
antecedents in [4]. The new step is a quadratic auxiliary whose leading
linear cofactor cannot cancel on the ordered real feature sizes. A
coefficient restriction, with its full dimension cost retained, removes
one problematic coordinate when two holes are not separated. Section 8
exhibits uncountably many new low-mean examples and compares the named
prior criteria at all scales.

A second argument treats any fixed number of exponent holes at every
contracting mean. It proves that positive rational execution forces the
hole positions close to one of finitely many integer linear relations,
with explicit coefficient bounds (Theorem 4). The new input bounds
cancellation at the prime $3$ in a reference inverse tail. Higher-degree
auxiliaries then become usable without an ordering of real products.
Theorem 5 gives a finite bound for a supplied positive integer using only
$8m-1$ aligned blocks. This arithmetic condition complements the
quadratic theorem: it permits arbitrary $m$, while retaining a restriction
on the positions. For separated holes, Theorem 6 forces two independent
bounded relations, and Theorem 7 gives its finite source-height version
using $80m-1$ blocks. These new prime-$3$ results concern exponent skeletons.

Theorem 8 treats a different geometry in both codings: any fixed number
of holes may occupy fixed-width strips at the two period endpoints, with
the remaining holes separated in the interior. Absorbing the short
boundary contributions into the formal series gives a bound depending
only on the number of interior holes. In particular, one interior hole
and arbitrary fixed boundary strips are excluded at every mean or density
for non-eventually-periodic words. The supplied source stays fixed in
this reduction. Its constants depend on that source, so we assert no
finite source-height version of Theorem 8.

These are restrictions on prescribed rational itineraries. We do not show
that an arbitrary positive integer orbit has such skeletons, exclude
all positive cycles, or prove Collatz. Positivity is used essentially in
the new contracting-range proof; no transcendence conclusion is claimed
there.

A finite version retains a supplied source $c/d>0$. For two holes, or
three separated holes, 149 aligned blocks with uniform interval contraction
and the gap conditions in Theorem 3 force $c+d$ to grow exponentially in
the skeleton period. No infinite continuation or nonperiodicity assumption
is needed for this finite conclusion.

## 2. Uniform means and a common auxiliary argument

For an exponent skeleton, fill every hole by $1$ and let $D$ be its total.
For every actual interval of length $N$, its mean lies in

$$
\left[\frac Dp,\frac{D+m(E-1)}p\right]
 +\left[-\frac{2Ep}{N},\frac{2Ep}{N}\right].               \tag{3}
$$

All subsequential prefix means belong to the main interval for every
skeleton. The interval widths tend to zero, so there is just one limit
$\alpha$. Fixing a sufficiently large skeleton and then increasing $N$
in (3) proves convergence uniformly over all starting positions. In
particular $D=\alpha p+O(1)$. In the binary case fill holes by $1$ and let
$n$ be the reference one-count. The same argument, with interval
$[(n-m)/p,n/p]$, proves uniform density and

$$
\rho p\le n\le\rho p+m.                                  \tag{4}
$$

Uniform means imply uniform contraction on intervals. In the exponent
range $\alpha<\beta$, every actual inverse slope on an interval of length
$k$ is at most $K\theta^k$ for fixed $K\ge1$, $0<\theta<1$. This follows
by choosing $\eta>0$ with $\alpha+\eta<\beta$ and taking
$\theta=2^{\alpha+\eta-\beta}$, with $K$ covering shorter intervals.
In the binary range $\rho>1/\beta$, use instead
$\theta=2^{1-\beta(\rho-\eta)}<1$. Reference holes filled by $1$ decrease
inverse slopes in both conventions, so every reference subinterval
obeys the same bound.

We now give the common arithmetic argument. Suppose $q=c/d>0$, with
$d$ odd, is the fixed hypothetical source. At each skeleton scale suppose
we have rational numbers $z,U,V_1,\ldots,V_m$, positive in the real
embedding and integral at $2$, with

$$
z=\frac{2^a}{b},\quad b\text{ odd},\qquad
U+\sum_{j=1}^m V_jG_j(z)=0\quad\text{in }\mathbb Q_2.       \tag{5}
$$

The $G_j$ have positive integer coefficients bounded in degree $k$ by
$T^{k+1}$ for one fixed $T$. Suppose all coordinates are uniformly bounded,
$U\ge q$, and their denominators divide $db,b,\ldots,b,b^2$, respectively.
For the separated case suppose also

$$
V_1/U\to0,\quad V_{j+1}/V_j\to0,\quad z/V_m\to0.           \tag{6}
$$

Fix integers $M>h\ge1$ satisfying

$$
mM<(m+2)(h+1).                                            \tag{7}
$$

Seek an integral polynomial $P(X,U,V)$, of $X$-degree at most $h$ and
homogeneous degree two in $U,V$, with

$$
P\left(X,-\sum_j V_jG_j(X),V\right)
 \in X^M\mathbb Z[[X]][V].                                \tag{8}
$$

There are $\binom{m+2}{2}(h+1)$ unknowns and at most
$\binom{m+1}{2}M$ equations. Entries are integers of magnitude at most
$B=2(M+1)T^{M+1}$. This bounds the coefficients of the two-series products
as well as the individual series. Inequality (7) gives a nonzero kernel.
Taking minors of a maximal independent row and column submatrix gives
an integer kernel vector of height at most $N!B^N$, where
$N=\binom{m+1}{2}M$; rank zero uses a coordinate vector. This bound is
independent of the period and the filling sequence.

Let $l$ be the least $X$-power in $P$, and put $Q=X^{-l}P$. Then
$0\le l\le h$, $\deg_X Q\le h-l$, and the substituted series has order
at least $M-l>0$. Writing $g_j=G_j(0)$, monic division over $\mathbb Z[V]$
gives

$$
Q_0(U,V)=\left(U+\sum_jg_jV_j\right)R(U,V),                \tag{9}
$$

where $R$ is a nonzero integral linear form with uniformly bounded
coefficients. Explicitly, $[U]R=[U^2]Q_0$ and
$[V_j]R=[UV_j]Q_0-g_j[U^2]Q_0$.

Under (6), the first nonzero coefficient of $R$ in the ordered coordinates
$U,V_1,\ldots,V_m$ dominates the later terms. Uniformly over all allowed
kernel choices, $|R(U,V)|\ge V_m/2$ eventually: choose all successive
ratios at most $\min(1/2,1/(2mC_R))$, where $C_R$ bounds the coefficients.
The other factor in (9) is at least $q$. All coordinates and coefficients
are bounded, so the positive-$X$ terms evaluated at $z$ are $O(z)=o(V_m)$.
Therefore

$$
Q(z,U,V)\ne0.                                             \tag{10}
$$

This certifies the actual rational evaluation. We have not identified the
real and $2$-adic values in (5).

At $2$, (5) and (8) give $v_2(Q(z,U,V))\ge a(M-l)$. Denominator clearing
yields the nonzero integer

$$
J=d^2b^{h-l+4}Q(z,U,V),
\qquad
2^{a(M-l)}\le |J|\le C d^2b^{h-l+4},                      \tag{11}
$$

with fixed $C$. The multiplier is odd. Consequently

$$
a(M-l)\le(\log_2 b)(h-l+4)+O(1).                          \tag{12}
$$

This is the common obstruction. The next two sections supply all its
hypotheses from the actual affine maps.

## 3. Positive features for exponent skeletons

Fill the holes by $1$, obtaining $r_0,\ldots,r_{p-1}$. Set

$$
S_i=\sum_{a<i}r_a,\quad v_i=2^{S_i}/3^i,\quad
b=3^p,\quad z=v_p=2^D/b.
$$

Let $\nu(i)$ count holes strictly before $i$, and put

$$
D_j=\frac13\sum_{\nu(i)=j}v_i\quad(0\le j\le m).          \tag{13}
$$

For a filling $\epsilon=(\epsilon_1,\ldots,\epsilon_m)$ define
$f_j(\epsilon)=2^{\sum_{a\le j}(\epsilon_a-1)}$, with $f_0=1$.
The filled block has inverse map

$$
y\longmapsto zf_m(\epsilon)y-\sum_{j=0}^mD_jf_j(\epsilon).
$$

For the actual successive fillings let $P_0=1$,
$P_{k+1}=P_kf_m(\epsilon_k)$, and
$G_j(X)=\sum_{k\ge0}P_kf_j(\epsilon_k)X^k$.
The coefficients are bounded by $T^{k+1}$ with $T=2^{m(E-1)}$ and
$G_0-XG_m=1$. Exact block inversion, with its actual odd endpoint,
then gives (5) for

$$
U=q+D_0,\qquad V_j=D_j\ (j<m),\qquad V_m=D_m+zD_0.        \tag{14}
$$

Indeed the terminal contribution after $K$ blocks is
$P_Kz^Kx_{Kp}$, whose $2$-adic valuation tends to infinity. After the
telescope, the finite version of (5) retains
$P_Kz^K(x_{Kp}+D_0)$. Denominators of the $D_j$ divide $b$, so the
claimed denominator bounds follow, and all coordinates are integral at $2$.

Write $s_j=t_j+1$. The interval contraction from Section 2 shows that
$D_0\in[1/3,C_0]$, where $C_0=K/[3(1-\theta)]$. For $j<m$, the group
beginning at $s_j$ is nonempty, even for adjacent holes, and

$$
v_{s_j}/3\le D_j\le C_0v_{s_j}.                           \tag{15}
$$

The same bounds hold for $D_m$ when the final group is nonempty.
When it is empty, $s_m=p$ and $V_m=zD_0$. In all cases $V_m$ is
bounded above and below by fixed positive multiples of $v_{s_m}$,
since $z/v_{s_m}\le K$. Thus every $V_j$ is uniformly comparable to
$v_{s_j}$. Ratios of these slopes obey

$$
v_{s_1}\le K\theta^{s_1},\quad
v_{s_{j+1}}/v_{s_j}\le K\theta^{s_{j+1}-s_j},\quad
z/v_{s_m}\le K\theta^{p-s_m}.                             \tag{16}
$$

Condition (1) proves (6). With $a=D=\alpha p+O(1)$ and
$\log_2b=\beta p$, choose $h=mt-1$, $M=(m+2)t-1$, for a sufficiently
large fixed integer $t$. Then (7) holds and

$$
\alpha M-\beta(h+4)
=t((m+2)\alpha-m\beta)-\alpha-3\beta>0.
$$

Removing $l$ improves this margin by $l(\beta-\alpha)>0$ when $l>0$.
This contradicts (12) and proves the exponent part of Theorem 2.

## 4. Positive reduced features for binary skeletons

Here $r_i\in\{0,1\}$ and reference holes are again $1$. Set

$$
n=\sum_i r_i,\quad b=3^n,\quad
v_i=2^i/3^{\sum_{a<i}r_a},\quad z=v_p=2^p/b.
$$

For a binary filling set $q_j=3^{1-\epsilon_j}$ and
$f_j=q_1\cdots q_j$, with $f_0=1$. Collect coefficients $D_0,\ldots,D_m$
as follows. A fixed $1$ at position $i$, after $j$ holes, contributes
$v_i/3$ to $D_j$. Hole $t_j$ contributes $v_{t_j}/2$ to $D_{j-1}$ and
$-v_{t_j}/6$ to $D_j$. The identity
$\epsilon/3^\epsilon=(3-3^{1-\epsilon})/6$ proves that the filled inverse
block is again

$$
y\longmapsto zf_m y-\sum_{j=0}^mD_jf_j.                  \tag{17}
$$

In particular $2bD_j$ is integral. Form $P_k,G_j$ as in Section 3;
now $T=3^m$, and the same telescope holds. Define

$$
U=2(q+D_0),\qquad V_j=2D_j\ (j<m),\qquad
V_m=2(D_m+zD_0).                                         \tag{18}
$$

All denominators have the bounds used in Section 2 and are odd. The
factor $2$ pays for all half-denominators, including a hole at the origin.
Equation (5) follows from actual binary inversion; after $K$ blocks its
finite residual is $2P_Kz^K(x_{Kp}+D_0)$, of valuation at least $Kp$.
The actual endpoints are integral at $2$ and need not be odd.

It remains to prove real positivity. For a binary word $W$, write its
inverse as $y\mapsto\lambda_Wy-F_W$ and set
$K_W(x)=F_W+\lambda_Wx$. The elementary maps

$$
K_0(x)=2x,\qquad K_1(x)=(2x+1)/3
$$

preserve $[1/2,\infty)$, as do their compositions. Let $A$ be the prefix
before the first hole, $W_j$ the fixed interval between holes $j$ and
$j+1$, and $W_m$ the tail after the last hole. With $s_j=t_j+1$,
$v_{s_j}=2v_{t_j}/3$, direct collection gives

$$
\begin{aligned}
D_0&=K_A(1/2)\ge1/2,\\
D_j&=v_{s_j}\bigl(K_{W_j}(1/2)-1/4\bigr)\ge v_{s_j}/4
 &&(j<m),\\
D_m+zD_0&=v_{s_m}\bigl(K_{W_m}(D_0)-1/4\bigr)\ge v_{s_m}/4.
\end{aligned}                                             \tag{19}
$$

The empty word has $K_\varnothing(x)=x$, so these formulas include adjacent
holes and both boundary cases. The raw coefficient $D_m$ can be negative;
(19) proves positivity of the reduced coordinates actually used.

When $\rho>1/\beta$, interval contraction bounds
$F_W\le K/[3(1-\theta)]$ and $\lambda_W\le K$ uniformly for these
reference intervals. Hence $D_0$ and all brackets in (19) have fixed
upper bounds. Each $V_j$ is comparable to $v_{s_j}$, and (16), interpreted
with binary slopes, again proves (6).

Now $a=p$ and $\log_2b=\beta n=\beta\rho p+O(1)$. With the same $h,M$,

$$
M-\beta\rho(h+4)
=t((m+2)-m\beta\rho)-1-3\beta\rho>0
$$

in (2). Removing $l$ improves this margin by $l(\beta\rho-1)$.
Equation (12) is impossible as $p\to\infty$, proving the binary part
of Theorem 2.

## 5. Removing the geometry restriction for two holes

For $m=2$, fix one coordinate $V_a$ to omit from the leading cofactor.
At every $X$-degree $k$ impose the additional linear equation

$$
[UV_a]P_k=g_a[U^2]P_k.                                   \tag{20}
$$

There are $h+1$ such equations with bounded integer entries. The kernel
construction still works whenever

$$
3M<5(h+1).                                                \tag{21}
$$

Because (20) is imposed at every degree, it survives division by the
unknown least power $X^l$. By (9), the resulting cofactor is
$R=A U+B V_j$, where $j\ne a$ and $A,B$ are bounded integers, not both
zero. Evaluated nonvanishing now requires only

$$
V_j\to0,\qquad z/V_j\to0.                                 \tag{22}
$$

Indeed $U\ge q$, so $|R|\ge V_j/2$ eventually, whether $A$ vanishes
or not. The other factor is positive and at least $q$, and the remaining
terms are $O(z)$. The integer estimate (12) is unchanged.

Take $h=3t-1$, $M=5t-1$. The exponent margin holds whenever
$\alpha>3\beta/5$, and the binary margin whenever
$\rho<5/(3\beta)$. Both cover their whole contracting ranges, because
$3^3<2^5$, $\alpha\ge1$, and $\rho\le1$.

Pass to a subsequence where each gap

$$
a=t_1,\qquad b=t_2-t_1,\qquad c=p-1-t_2
$$

is constant or tends to infinity. At least one diverges. Uniform
comparability of $V_j$ to $v_{s_j}$ proves (22) with $j=1$ if
$a\to\infty$ and $b+c\to\infty$, and with $j=2$ if
$a+b\to\infty$ and $c\to\infty$. This includes every configuration
with at least two divergent gaps.

Otherwise there is just one divergent gap. If it is $a$ or $c$, then
$b$ is bounded and the holes lie in a fixed-length interval. If it is
$b$, the holes lie in the wrapping interval
$\{p-1-c,\ldots,p-1,0,\ldots,a\}$ of fixed length $a+c+2$.
The clustered-skeleton theorem [2, Corollaries 5 and 6] covers all these
cases for non-eventually-periodic words, including binary words and
wrapping clusters. A single hole is also such a cluster, and zero holes
force periodicity.

For completeness, an eventually periodic contracting word cannot have a
positive source. A periodic tail has inverse block map
$y\mapsto\lambda y-F$ with $\lambda<1$ and $F>0$. Its unique $2$-adic
periodic source, which is also its rational fixed point, is
$-F/(1-\lambda)<0$. A positive rational orbit stays positive, a
contradiction. In the binary contracting case the period contains a one,
so $F>0$ holds there too. This handles all residual periodic cases in
the contracting range. Section 6 finishes Theorem 1.

### 5.1. A finite bound retaining the supplied source

The same auxiliary gives a finite conclusion, including the cost of a
possible real cancellation. A finite period-$p$ skeleton here specifies
the fixed positions in each of 149 aligned blocks; the fillings in those
blocks are arbitrary admissible letters. No continuation is assumed.

**Theorem 3 (finite sparse prefixes).** Fix $K\ge1$, $0<\theta<1$ and
$0<\gamma<1$, and fix the alphabet bound $E$ in the exponent convention.
There are effective constants $L_0,C_0$ with the following property.
Fill every hole by $1$ to obtain the reference block, and suppose every
reference subinterval of length $k$ has inverse slope at most $K\theta^k$.
Assume either:

1. there are exactly two holes, and one of them, at $t_j$, satisfies
   $t_j+1\ge L_0$ and $p-1-t_j\ge\gamma p$; or
2. there are exactly three holes, with $t_1\ge L_0$,
   $t_2-t_1\ge L_0$, $t_3-t_2\ge L_0$, and
   $p-1-t_3\ge\gamma p$.

Every positive rational $c/d$, with positive integers $c,d$ and $d$ odd,
which executes the 149 aligned blocks satisfies

$$
\log_2(c+d)\ge
\min\left\{\frac1{10},\gamma\log_2(1/\theta)\right\}p-C_0. \tag{23}
$$

Execution uses the actual parity or division exponents, as in Section 1.
Only the final distance in these hypotheses must be proportional to $p$;
the preceding and internal gaps need only exceed the fixed constant $L_0$.

**Proof.** We first keep $h,M$ general, using the restricted two-hole
scheme or the unrestricted three-hole scheme. Put $\sigma=1$ for
exponents and $\sigma=2$ for binary words, so $U=\sigma(q+D_0)$ for
$q=c/d$. Interval contraction and Sections 3--4 give constants $u_0>0$
and $B\ge1$, independent of $p,q$ and the fillings, such that
$u_0\le\sigma D_0\le B$ and $0<V_j\le B$. For sufficiently large $p$,
$0<z\le1/2$. Increasing $C_0$ covers the remaining bounded periods.

Only the first $M$ coefficients of each series enter the auxiliary.
Writing $G_j^{<M}$ for these truncations, and
$U_F=-\sum_jV_jG_j^{<M}(z)$, exact inversion gives

$$
U-U_F=\sigma P_Mz^M(x_{Mp}+D_0),\qquad
v_2(U-U_F)\ge aM.                                        \tag{24}
$$

Here $x_{Mp}$ is the actual endpoint. The finite telescope is
$G_0^{<M}-XG_m^{<M}=1-P_MX^M$. In the binary boundary case it is
$\sigma(x_{Mp}+D_0)$ that is integral at $2$; $D_0$ alone need not be.
Since all scaled coordinates are integral at $2$, (8), followed by
division by the least power $X^l$ and substitution of (24), proves
$v_2Q(z,U,V)\ge a(M-l)$ without an infinite source relation.

Let $C\ge1$ bound the integer coefficients of the auxiliary. In the
restricted case this is the bound for the full enlarged system, with
$3M+h+1$ rows and entries bounded by
$\max\{2(M+1)T^{M+1},T\}$. Thus it includes the cost of (20).
Put $C_R=C(1+T)$ and $\delta=\min\{1/2,1/(2mC_R)\}$.
For three holes impose $V_1\le\delta u_0$ and
$V_{j+1}\le\delta V_j$, and set $v_*=V_3$.
For two holes retain the chosen $V_j$ in the cofactor, impose
$V_j\le\delta u_0$, and set $v_*=V_j$. The gap conditions imply these
inequalities when $L_0$ is sufficiently large, by interval contraction
and the uniform feature comparisons. These choices are independent of $q$.

The first nonzero coefficient of the linear cofactor gives
$|R(U,V)|\ge v_*/2$. This also holds when that coefficient is attached
to $U$, because $U\ge u_0$. Set
$A_2=\binom{m+2}{2}$, $B_1=\max\{\sigma,B,1\}$, and
$c_0=\min\{\sigma,u_0\}$. Every coordinate is at most $B_1(q+1)$,
whereas $U\ge c_0(q+1)$. The leading term (9) therefore has absolute
value at least $c_0(q+1)v_*/2$, and the positive-$X$ terms total at
most $2CA_2B_1^2(q+1)^2z$. It follows that $Q(z,U,V)\ne0$ if
$q+1\le c_0v_*/(8CA_2B_1^2z)$.

If this inequality fails, then $c+d=d(q+1)$ is already greater than
its right side. Otherwise the full polynomial has absolute value at
most $2CA_2B_1^2(q+1)^2$. Clearing odd denominators as in (11) gives

$$
c+d\ge c_*\min\{v_*/z,2^{\Delta/2}\},\qquad
\Delta=aM-(\log_2b)(h+4),                                \tag{25}
$$

where one may take
$c_*=\min\{c_0/(8CA_2B_1^2),(2CA_2B_1^2)^{-1/2}\}>0$.
Indeed the nonzero integer is $d^2b^{h-l+4}Q$, and
$d^2(q+1)^2=(c+d)^2$. The valuation-minus-size exponent is
$\Delta+l(\log_2b-a)\ge\Delta$, since $z<1$.
Thus removing the least $X$-power improves the estimate.

Take $h=89$ and $M=149$. Both dimension conditions reduce to
$3M<5(h+1)$, namely $447<450$. In the exponent convention $a=D\ge p$
and $\log_2b=\beta p$; in the binary convention $a=p$ and
$\log_2b=\beta n\le\beta p$. Since $3^5<2^8$, in both cases

$$
\Delta\ge(149-93\beta)p>p/5.                             \tag{26}
$$

If the retained hole starts its following interval at $s=t_j+1$,
the feature lower bounds and the slope on $[s,p)$ give
$v_*/z\ge c_1\theta^{-(p-s)}$, with $c_1=1/(3K)$ for exponents
and $c_1=1/(2K)$ for binary words. Use the final hole for the three-hole
scheme. Combining this estimate, the terminal gap, (25) and (26)
proves (23). All constants arise from finite coefficient bounds and
geometric sums, so are effective, though potentially very large. $\square$

This theorem bounds a supplied source on an explicitly specified finite
prefix class. It does not assert that such prefixes occur on every orbit.

## 6. The critical and remaining density range

This section recalls the elementary argument of [1, Section 4], also
consistent with the stronger periodic-shadow criterion of [5]. The
standard parity conjugacy [6] identifies a shared prefix of $L$ bits
with equality modulo $2^L$.

For a binary word $V$ of length $n$, with $g$ ones at positions
$j_0<\cdots<j_{g-1}$, put
$F(V)=\sum_i3^{g-1-i}2^{j_i}$. Then
$C^n(x)=(3^gx+F(V))/2^n$. Uniform density $\rho$ implies, uniformly for
factors of length at most $N$,

$$
F(V)\le2^{\kappa|V|+o(N)},\qquad \kappa=\max(1,\rho\beta).
$$

Indeed all prefix one-counts have discrepancy $o(N)$, each summand has
logarithm at most $\kappa|V|+o(N)$, and there are at most $N$ summands.
For a shadow $PQ^\infty$, let $r=|P|$, $s=|Q|$, $g=|P|_1$, $h=|Q|_1$,
and $N=r+s$. Its source is $Z/(X_2-X_1)$, where

$$
X_1=3^{g+h},\quad X_2=3^g2^s,\quad
Z=2^rF(Q)-F(P)(2^s-3^h).
$$

The denominator is odd and nonzero, and
$\max(X_1,X_2,|Z|)\le2^{\kappa N+o(N)}$.
A distinct rational $c/d$ matching $L$ bits therefore obeys

$$
2^L\le(|c|+d)2^{\kappa N+o(N)},                           \tag{27}
$$

by applying divisibility to $c(X_2-X_1)-dZ$.

A skeleton with at most $m$ holes has a nonhole interval in $[0,p)$
of length $g_p\ge(p-m)/(m+1)$. Begin a period-$p$ shadow at its start
$r_p$, retaining the actual prefix of length $r_p$. The shadow matches
through $p+r_p+g_p$, while $N=p+r_p\le2p$. Thus its matching ratio
is at least $1+1/(2(m+1))-o(1)$. If $\rho\le1/\beta$, then
$\kappa=1$, so (27) is impossible for unbounded periods unless the
source equals a shadow. Non-eventual-periodicity excludes that equality.
This includes the critical density.

For exponent words, bounded coding lengths and uniform mean imply
uniform binary density $1/\alpha$. Every relevant length is multiplied
by $\alpha$ up to $o(p)$, so the same shadow ratio survives the coding.
Non-eventual-periodicity survives because ones uniquely delimit the
exponents. Hence $\alpha\ge\beta$ is excluded, including equality.
This argument is inherited and assumes no separation of the holes.

## 7. Arithmetic restrictions for any fixed number of exponent holes

Define the finite set

$$
\mathcal A_m=\{A\in\mathbb Z^{m+1}\setminus\{0\}:
 |A_0|\le5m-1,\ |A_j|\le m\ (1\le j\le m)\},
\qquad
R_m(p,t)=\min_{A\in\mathcal A_m}
 \left|A_0p+\sum_{j=1}^mA_jt_j\right|.                   \tag{28}
$$

**Theorem 4 (necessary arithmetic relation).** Let a word over
$\{1,\ldots,E\}$ have global skeletons with exactly $m\ge1$ holes at
unbounded periods, and uniform mean $\alpha<\beta$. If a positive
rational $q$ executes the word, then

$$
R_m(p,t)\le C_q                                             \tag{29}
$$

at every sufficiently large skeleton period, for a fixed constant $C_q$.
The constant may depend on the word, $m$ and $E$. A relation from the
fixed set $\mathcal A_m$ occurs at each period; the selected relation
need not be the same at different periods.

In particular, $R_m(p,t)\to\infty$ excludes a positive rational source.
It suffices that $t_j/p\to\lambda_j$ and
$A_0+\sum_jA_j\lambda_j\ne0$ for every $A\in\mathcal A_m$.
For non-eventually-periodic words this conclusion holds at all means,
because Section 6 covers $\alpha\ge\beta$. No separation assumption is
needed for the necessary condition (29) itself.

### 7.1. Shifted coordinates and the inverse-tail bound

Use $v_i,z,b,D_j,G_j$ from Section 3 and write $q=c/d$, with $c,d$
positive odd coprime integers. The oddness follows from execution of an
exponent word. Define

$$
Y_0=q+D_0,\qquad Y_j=D_j\ (1\le j<m),\qquad Y_m=D_m-zq.
                                                               \tag{30}
$$

The identity $G_0-XG_m=1$ turns actual inversion into
$\sum_{j=0}^mY_jG_j(z)=0$ in $\mathbb Q_2$. Since $G_0(0)=1$, the
series $F_j=G_j/G_0$ have integer coefficients, with a uniform exponential
bound, and $G_0(z)$ is odd. For example, the coefficient recurrence for
the inverse unit gives a bound $(4\max(1,T))^{k+1}$ for the coefficients
of $F_j$ in degree $k$, after increasing the harmless constant if needed.
We obtain

$$
Y_0+\sum_{j=1}^mY_jF_j(z)=0\quad\hbox{in }\mathbb Q_2.    \tag{31}
$$

All coordinates are integral at $2$, have denominators dividing $db$,
and are uniformly bounded in the real embedding for fixed $q$.
The last coordinate may have either real sign.
$D$ and $z$ belong to the fixed reference period with every hole filled
by $1$; actual fillings may vary between blocks, with their extra slope
factors recorded in $P_k$ and $G_j$.

We need a uniform bound on its cancellation at $3$. Every reference
interval has inverse slope at most $K\theta^k$, as in Section 2, and
inverse correction at most $B=K/[3(1-\theta)]$. For a reference tail
$w$ of length $L$, write

$$
I_w(q)=\frac{N_w}{d3^L},\qquad
N_w=2^{S_L}c-d\sum_{i=0}^{L-1}2^{S_i}3^{L-1-i}.           \tag{32}
$$

For each $r\le L$, its numerator is congruent modulo $3^r$ to the
numerator for the last $r$ letters, multiplied by the unit $2^{S_{L-r}}$.
Thus $3^R\mid N_w$, with $R\le L$, makes all inverse states through
the last $j$ letters, $0\le j\le R$, lie in $(1/d)\mathbb Z$.
Their numerators remain odd: every integral update
$c_j=(2^a c_{j-1}-d)/3$ preserves oddness. Therefore these are actual
Syracuse steps in reverse, since
$v_2(3x_j+1)=v_2(2^a x_{j-1})=a$.

Choose $r_0\ge1$ with $K\theta^{r_0}q<1/d$ and set
$R=r_0+\lceil dB\rceil+1$. For $r_0\le j\le R$, contraction gives
$-B\le x_j<1/d$. Oddness excludes zero, so every such grid point is
negative. There are at most $\lceil dB\rceil$ possible points.
None can repeat: a repetition would put the point on a negative cycle
of the deterministic forward Syracuse map, whereas its forward iterates
are prescribed to reach $q>0$. There are more states than grid points,
a contradiction. Hence $0\le v_3(N_w)<R$ whenever $L\ge R$.

For $L<R$ there are finitely many reference tails. Their inverse values
cannot be zero because every inverse letter preserves oddness at $2$;
the empty tail has value $q$. This also bounds $v_3(N_w)$ for short tails.
With $s=t_m+1$ the tail is $r_s\cdots r_{p-1}$, of length $L=p-s$.
Thus $Y_m=-v_sI_w(q)$, with denominator dividing $d3^{s+L}=d3^p$, and

$$
v_3(Y_m)=-p+O_q(1).                                      \tag{33}
$$

For $j<m$, the last summand of $D_j$ has the unique smallest valuation,
giving $v_3(D_j)=-(t_{j+1}+1)$. This dominates $q$ in $Y_0$ when
$t_1$ is sufficiently large. Bounded $t_1$ gives finitely many positive
values of $q+D_0$. Consequently

$$
v_3(Y_0)=-(t_1+1)+O_q(1),\qquad
v_3(Y_j)=-(t_{j+1}+1)\quad(1\le j<m).                    \tag{34}
$$

Every coordinate is nonzero. Adjacent holes and terminal holes are included.

### 7.2. Higher-degree auxiliaries and a minimum-valuation tie

Fix

$$
\ell=m,\qquad h=4m-1,\qquad M=8m-1.                      \tag{35}
$$

Seek an integer polynomial $P(X,Y)$ of $X$-degree at most $h$,
homogeneous of $Y$-degree $\ell$, such that substitution
$Y_0=-\sum_{j=1}^mY_jF_j(X)$ gives order at least $M$ in $X$.
There are $\binom{m+\ell}{\ell}(h+1)$ unknowns and at most
$\binom{m+\ell-1}{\ell}M$ equations. Their binomial ratio is $2$,
and $M<2(h+1)$. A nonzero integer kernel therefore exists. Only the
first $M$ uniformly bounded integral series coefficients enter; bounded
minors give a coefficient bound independent of $p$ and $q$.

Equation (31) gives $v_2(P(z,Y))\ge DM$. If the rational evaluation is
nonzero, clearing its odd denominator yields

$$
2^{DM}\le|d^m b^{h+m}P(z,Y)|
 \le C(c+d)^m3^{p(h+m)}.                                 \tag{36}
$$

The real constant is uniform in the period. Since $D\ge p$ and

$$
\delta_m=M-\beta(h+m)
 =m(8-5\beta)+(\beta-1)>\tfrac12,                        \tag{37}
$$

(36) is impossible for fixed $q$ and large $p$. The strict margin uses
$3^5<2^8$ and $3^2>2^3$. Thus $P(z,Y)=0$.

At least two of its nonzero evaluated terms have the same minimum
$3$-valuation. For terms $c_iX^aY^i$ and $c_{i'}X^{a'}Y^{i'}$,
(33)--(34) give

$$
\left|(a-a'+i_m-i'_m)p+
  \sum_{j=1}^m(i_{j-1}-i'_{j-1})t_j\right|\le C_q.        \tag{38}
$$

The coefficient valuations are uniformly bounded. The displayed vector
is nonzero: equality of $i_0,\ldots,i_{m-1}$ forces equality of $i_m$
by homogeneity, after which distinct monomials have $a\ne a'$.
Its bounds are exactly those defining $\mathcal A_m$. This proves
Theorem 4. No ordering of real products or division by a least
$X$-power is needed.

### 7.3. A finite bound for a supplied positive integer

Put $a_\theta=\log_2(1/\theta)>0$.

**Theorem 5 (finite arithmetic geometry).** Fix $m,E,K,\theta$, with
$m,E\ge1$, $K\ge1$, $0<\theta<1$. Suppose a positive odd integer $q$
executes $8m-1$ aligned blocks of a period-$p$ exponent skeleton with
exactly $m$ holes. Fill reference holes by $1$, and suppose every reference
subinterval of length $k$ has inverse slope at most $K\theta^k$. Then
an effective constant $C_0$, depending only on the fixed parameters, gives

$$
\log_2(q+1)\ge
 \min\left\{\frac{\delta_m}{m}p,
 \frac{R_m(p,t)}{m(1/a_\theta+1/\beta)}\right\}-C_0.       \tag{39}
$$

In particular $R_m(p,t)\ge\eta p$, for a fixed $\eta>0$, forces $q$
to grow exponentially with $p$. No infinite continuation, uniform mean,
or nonperiodicity assumption is needed.

**Proof.** Let $M=8m-1$ and truncate the $G_j$ below degree $M$.
Actual inversion and the finite telescope give the exact identity

$$
\sum_{j=0}^mY_jG_j^{<M}(z)
   =P_Mz^M(x_{Mp}-q).                                    \tag{40}
$$

The actual endpoint is retained; the right side need not be zero.
Its valuation is at least $DM$. Formal division by the unit $G_0^{<M}$
and truncation below $M$ therefore give (31) modulo $2^{DM}$.
The auxiliary in (35) depends only on these initial coefficients, so
$v_2(P(z,Y))\ge DM$ still holds. All coordinates have real magnitude
at most a fixed multiple of $q+1$, and $0<z\le K$. If the evaluation
is nonzero, its integer denominator clearing gives

$$
\delta_m p\le m\log_2(q+1)+C_1.                          \tag{41}
$$

For the other case, quantify the tail cancellation using integer
positivity. Let
$r=1+\lfloor\log_2(Kq)/a_\theta\rfloor$, so $K\theta^r q<1$.
If a reference tail has length $L\ge r$ and $3^r\mid N_w$, the
last $r$ inverse steps would all be positive integers, hence at least
$1$. Their inverse value is strictly less than $K\theta^r q<1$,
a contradiction. Thus $\kappa=v_3(N_w)<r$ for such tails.
If $L<r$, its nonzero integer numerator satisfies
$|N_w|\le3^L(Kq+B)$, where $B=K/[3(1-\theta)]$.
The empty tail is included. In both cases,

$$
0\le\kappa\le c_0+(1/a_\theta+1/\beta)\log_2(q+1),
\quad
c_0=1+\frac{\log_2K}{a_\theta}+\log_3(K+B).               \tag{42}
$$

For integer $q$, (34) has no error term: $v_3(Y_0)=-(t_1+1)$,
and $v_3(Y_j)=-(t_{j+1}+1)$ for $1\le j<m$.
Also $v_3(Y_m)=-p+\kappa$. A monomial $cX^aY^i$ consequently has valuation

$$
v_3(c)-(a+i_m)p-\sum_{j=1}^mi_{j-1}t_j-m+i_m(1+\kappa).
                                                               \tag{43}
$$

If $P(z,Y)=0$, two minimum-valuation terms give a nonzero vector
$A\in\mathcal A_m$ with
$|A_0p+\sum_jA_jt_j|\le\log_3C+m(1+\kappa)$, where $C$ bounds
the integral coefficients. Using (42) proves the second alternative
in (39). Equation (41) proves the first. Enlarging one fixed additive
constant handles both alternatives. All constants come from finite
coefficient bounds and geometric sums, hence are effective. $\square$

### 7.4. Nonresonance is compatible with nested skeletons

The limiting proportions need only avoid the finite set $\mathcal A_m$;
they need not be linearly independent over $\mathbb Q$. For example, set
$b_0=m+1$, $B_0=b_0^m+1$, and $d_j=b_0^{j-1}$. With a sufficiently
large initial period $P_0$ and distinct ordered initial holes $a_j$, take

$$
p_k=P_0B_0^k,\qquad
t_{j,k}=a_j+P_0d_j\frac{B_0^k-1}{B_0-1}.                 \tag{44}
$$

These holes nest since $t_{j,k+1}=t_{j,k}+d_jp_k$, and their limiting
proportions are $d_j/(B_0-1)$. If $A\in\mathcal A_m$ gave a zero
limiting form, then
$(B_0-1)A_0+\sum_jA_jd_j=0$. But
$|\sum_jA_jd_j|\le m\sum_{j=0}^{m-1}b_0^j=b_0^m-1<B_0-1$,
forcing $A_0=0$. The largest nonzero base-$b_0$ term then dominates
the lower terms, forcing every $A_j=0$, a contradiction.
Hence $R_m(p_k,t_k)\ge p_k/(B_0-1)-O(1)$.

Fill initially fixed positions by $1$ and every newly fixed hole copy
arbitrarily from $\{1,2\}$. Every position eventually fills, because
$t_{1,k}\to\infty$. Independent choices at distinct levels give
uncountably many words. Their uniform means are at most $1+m/P_0$,
which can be arbitrarily close to $1$. Theorem 4 excludes positive
rational sources for all these words once $1+m/P_0<\beta$.
This establishes compatibility of the condition with genuine infinite
skeletons. It is not a claim that every member escapes prior shadow
criteria; some fillings have long periodic shadows or fewer effective
holes. The next section provides the separate all-scale comparison
for the quadratic part of the paper.

### 7.5. Two independent relations for separated holes

Let $\mathcal B_m$ be the finite set of nonzero integer vectors
$B=(B_0,\ldots,B_m)$ with $|B_0|\le50m-1$ and $|B_j|\le2m$ for
$1\le j\le m$. Write $x=(p,t_1,\ldots,t_m)$.

**Theorem 6 (independent arithmetic relations).** Under the hypotheses of
Theorem 4, suppose also that the gaps in (1) tend to infinity and $m\ge2$.
Then for every sufficiently large skeleton period there are
$A\in\mathcal A_m$ and $B\in\mathcal B_m$, independent over $\mathbb Q$,
such that $|A\cdot x|,|B\cdot x|\le C_q$ for one fixed constant.

Thus execution is impossible if, for every $C$, infinitely many skeleton
periods have no such independent pair with both forms bounded by $C$.
In particular, if $t_j/p\to\lambda_j$ and the rational relation space of
$(1,\lambda_1,\ldots,\lambda_m)$ has dimension at most one, there is no
positive rational source. This limiting condition is sufficient only:
a zero limiting form can still have an unbounded sublinear value.
For non-eventually-periodic words, Section 6 again completes all means.
When $m=1$, the first relation already contradicts separation, so the
new assertion starts at $m=2$.

**Proof.** Theorem 4 first gives a relation $A$. Dividing by the gcd makes
it primitive without enlarging its bounds. Put

$$
u=(A_1,\ldots,A_m,-\textstyle\sum_jA_j),\qquad
k=A_0+\sum_jA_j,\qquad d(A)=\sum_{u_j>0}u_j.
$$

For a monomial $X^aY_0^{i_0}\cdots Y_m^{i_m}$ of homogeneous degree
$\ell$, its position weight is $w=(a+i_m,i_0,\ldots,i_{m-1})$.
In the free coordinates $(a,i_0,\ldots,i_{m-1})$ this is an affine map
with linear part

$$
\begin{pmatrix}1&-1&\cdots&-1\\0&&I_m&\end{pmatrix},
$$

whose determinant is one. A weight difference $A$ corresponds exactly
to the monomial shift $(k,u)$. Any common divisor of its entries divides
$A_1,\ldots,A_m$ and $A_0+\sum_jA_j$, hence $A_0$ as well. Thus this
shift is primitive.

For sufficiently large periods, $d(A)\ge2$. Indeed, $d=0$ leaves only
a nonzero multiple of $p$. If $d=1$, $u$ has one entry $1$ and one
entry $-1$. The form is $A_0p\pm t_j$ or $A_0p+t_j-t_l$ with $j\ne l$.
Its absolute value is at least the smallest initial, terminal, or internal
gap, which tends to infinity. This contradicts the bound for $A$.
The exclusion is uniform over the finite set $\mathcal A_m$.

In the monomial set $0\le a\le h$, $i_j\ge0$, $\sum i_j=\ell$, retain
one representative of each line parallel to $(k,u)$. The line intersects
the real product polytope in an interval; primitivity makes its lattice
points consecutive integer shifts. The number of representatives equals
the number of vertices minus predecessor edges, namely

$$
N_A=(h+1)\binom{m+\ell}{m}
 -(h+1-|k|)_+\binom{m+\ell-d(A)}m,                       \tag{45}
$$

where the second binomial is zero if $\ell<d(A)$. For the overlap,
subtracting the positive parts of $u$ leaves homogeneous degree
$\ell-d(A)$, independently of the $X$-interval overlap.
No two retained weights differ by a rational multiple of $A$.

Choose

$$
\ell=2m,\qquad h=48m-1,\qquad M=80m-1.                  \tag{46}
$$

Let $R_\ell=\binom{m+\ell-1}{m-1}$, the number of homogeneous
monomials after substitution of $Y_0$. Since $d(A)\ge2$, Pascal's identity
gives

$$
\frac{N_A}{R_\ell}\ge(h+1)
 \left(1+\frac{\ell}{m+\ell-1}\right)
 =(h+1)\frac{5m-1}{3m-1}>\frac53(h+1)=80m>M.
$$

The restricted support therefore still has more columns than the
original $MR_\ell$ formal-substitution equations. We do not quotient
those equations. The finitely many choices of $A$ fix finitely many
supports, and the bounded integral initial $F_j$ coefficients give
finitely many matrices. A nonzero integer auxiliary with uniformly
bounded coefficients follows.

As in (36), a nonzero evaluation would imply
$2^{DM}\le C(c+d)^\ell3^{p(h+\ell)}$. But
$M-\beta(h+\ell)=m(80-50\beta)+(\beta-1)>1/2$, so the evaluation
vanishes for sufficiently large $p$. A minimum $3$-valuation tie gives
a nonzero weight difference $B$, with $|B_0|\le h+\ell=50m-1$ and
$|B_j|\le\ell=2m$, and a bounded value $B\cdot x$ by (33)--(34).
If $B$ were parallel to primitive $A$, the corresponding monomial
difference would be an integer multiple of $(k,u)$, contradicting the
single representative on each line. The relations are independent.

The period threshold is taken after the first-relation threshold, the
threshold at which every gap exceeds its bound, and the second auxiliary
height threshold. All coefficient and valuation errors are uniform in
the selected $A$, so a common $C_q$ works at every later period.
For the limiting corollary, fix a pair along an infinite subsequence
from the finite sets, divide its bounded relations by $p$, and pass
to the limit. $\square$

The separation assumption pays a precise dimension cost: with $d=1$
and $k=0$, (45) gives only $(h+1)R_\ell$ columns, insufficient for
$M>\beta(h+\ell)$. The argument does not automatically supply a third
relation; deleting lines in two independent directions requires a new
count while the original equation count remains.

### 7.6. A finite bound using two relations

Define

$$
\begin{split}
R_m^{(2)}(x)&=\min_{\substack{A\in\mathcal A_m,\ B\in\mathcal B_m\\
                    \operatorname{rank}_{\mathbb Q}(A,B)=2}}
                 \max\{|A\cdot x|,|B\cdot x|\},\\
G(x)&=\min\{t_1,p-t_m,t_2-t_1,\ldots,t_m-t_{m-1}\},\\
c_\theta&=1/a_\theta+1/\beta,\qquad
\Delta_m=m(80-50\beta)+(\beta-1),\\
c_p&=\min\{\delta_m/m,\Delta_m/(2m)\}.
\end{split}                                               \tag{47}
$$

The boundary convention in $G$ differs by one from (1) and is used
exactly in the following finite statement.

**Theorem 7 (finite independent-relation bound).** Fix $m\ge2$ and
$E,K,\theta$ as in Theorem 5. If a positive odd integer $q$ executes
$80m-1$ aligned blocks of an $m$-hole exponent skeleton with the same
reference interval contraction, then an effective constant depending
only on these fixed parameters gives

$$
\log_2(q+1)\ge
 \min\left\{c_pp,\frac{G(x)}{mc_\theta},
                    \frac{R_m^{(2)}(x)}{2mc_\theta}\right\}-C_0.
                                                               \tag{48}
$$

**Proof.** Write $W=\log_2(q+1)$. The finite residual (40) holds for
every number of blocks up to $80m-1$. Thus a degree-$\ell$ auxiliary of
$X$-degree $h$ and order $M$ obeys the same divisibility. Nonzero
evaluation gives $[M-\beta(h+\ell)]p\le\ell W+C$.
For a zero evaluation, the exact monomial valuation (43), with its
constant $-m$ replaced by $-\ell$, and (42) give a nonzero relation
of magnitude at most $C+\ell c_\theta W$.

Apply the first auxiliary (35). If it is nonzero, then
$W\ge\delta_mp/m-C$. Otherwise obtain primitive $A\in\mathcal A_m$
with $|A\cdot x|\le C+mc_\theta W$. If $d(A)\le1$, then
$|A\cdot x|\ge G(x)$: for $d=0$ it is a nonzero multiple of $p$;
for $d=1$ the distance of $t_j$, or $t_j-t_l$ with $j\ne l$, from
$p\mathbb Z$ is at least $G(x)$. The complementary distance
$p-|t_j-t_l|$ contains both boundary gaps. This yields the second
term in (48).

If $d(A)\ge2$, construct the restricted auxiliary (46). Nonzero
evaluation gives $W\ge\Delta_mp/(2m)-C$. Zero evaluation gives
$B\in\mathcal B_m$ independent of $A$ by the support construction,
with $|B\cdot x|\le C+2mc_\theta W$. Hence
$R_m^{(2)}(x)\le C+2mc_\theta W$. These four branches are exhaustive.
The first and third branches give the first term of (48); taking the
maximum of the fixed additive errors completes the proof. $\square$

The result can apply when the first distance $R_m$ is zero. For example,
take $m=4$ and real numbers with
$0<\lambda_1<2\lambda_1<\lambda_3<\lambda_4<1$, where
$1,\lambda_1,\lambda_3,\lambda_4$ are independent over $\mathbb Q$.
Set $t_1=\lfloor\lambda_1p\rfloor$, $t_2=2t_1$, and
$t_j=\lfloor\lambda_jp\rfloor$ for $j=3,4$. The first relation
$(0,-2,1,0,0)$ vanishes exactly. All gaps are proportional to $p$,
and every independent pair in the finite boxes has at least one nonzero
limiting form. Thus $R_m^{(2)}(x)\ge\eta p-O(1)$ for some $\eta>0$.
This illustrates the finite geometry; it does not assert an infinite
nested construction or separation from every earlier criterion.

## 8. A low-mean family outside the matched prior criteria

The three-colour construction of [1, Sections 5–7] works with base
$B=3H-1\ge38$. At level $k$ its period is $p_k=B4^k$, with holes
$A_k=(p_k+1)/3$ and $2A_k$. Every initially fixed symbol is $1$.
Choose any directive $a_k\in\{1,2,3\}$ with $a_{k+1}\ne a_k$, and let
$c_k$ be the third colour. At refinement, the four successive old hole
pairs are

$$
(a_k,a_k),\qquad (?,c_k),\qquad(c_k,?),\qquad
(a_{k+1},a_{k+1}).                                       \tag{49}
$$

All positions eventually fill, and each level fills each colour twice.
The frequencies of $2$ and $3$ are each $2/(3B)$, so
$\alpha=1+2/B$. Each directive is recovered from entries at $A_k$.
There are uncountably many words, and all hole gaps diverge. Theorem 2
excludes them for every such $B$. For $B=38$, $\alpha=20/19$, below
$2\beta/3$ because $2^{30}<3^{19}$. Larger bases give means approaching
one. The unrestricted mean bound in [1] does not cover these examples.

We record why changing the base does not silently assume the old
comparison. For shifts divisible by $B$, write the shift as $q p_k$
with $4\nmid q$. The hole-column phases in the proof of [1, Section 6]
depend only on $p_k,A_k,2A_k$ and $q$ modulo four. All its inequalities
hold for every $p_k\ge20$. They give shadow ratio at most $7/5$, with
witnesses $r=2A_k+1$, $s=p_k$ attaining
$(7p_k+1)/(5p_k+5)\to7/5$.

If a shift is not divisible by $B$, the support residues $\{H,2H\}$
have no nonzero translation stabilizer: interchanging them would require
$2H=0\pmod B$, although $0<2H<B$. Some hole column is translated to
a fixed column. Its three fixed phase colours include at least two
different from $1$, giving a mismatch in every interval of length $4B$.
Thus such a shadow satisfies $L\le r+s+4B$. This also proves
non-eventual-periodicity. The exact shadow limsup is consequently $7/5$,
and the bounded binary coding preserves it, as in [1]. Since
$\alpha(7/5)\le28/19<3/2<\beta$, the density-sensitive shadow criterion
in [5] does not apply at any alternative initial period and preperiod.

The dictionary comparison also survives at arbitrary origins. For every
$n\ge4B$, the first sixteen aligned length-$n$ blocks have at least four
types, and the first eight have at least three. When $B\mid n$, write
$n=q p_k$, $4\nmid q$, and use the four-adic phase count of [1, Section 7].
That count is independent of $B$; in the crossed-column case the index is
$\lfloor h/p_k\rfloor$ for origin $h$. When $B\nmid n$, the support
identifies the initial phase modulo $B$. If $B/\gcd(B,n)\ge4$, four blocks
already have different phases. Three phases are impossible because
$3\nmid B$. With two phases, write $n=(B/2)q$, $q$ odd. Four even-indexed
blocks contain three distinct aligned $B$-block types by the same phase
count, and an odd-indexed block has different support. The selected
$B$-blocks fit because $n\ge4B$.

Every full dictionary therefore has at least three types. Uniform mean
makes its minimum total $\alpha n+o(n)$ and its spread $o(n)$, so the
fixed-size criterion of [3, Corollary 2] fails since $\alpha<2\beta/3$.
The budget in [3, Theorem 3 and Corollary 5] forces a proposed finite-prefix
dictionary to have two types; the required prefix has at least eleven
blocks, whereas the first eight already have three. For Corollary 5,
its width condition first forces the freely chosen reference total to
be $\alpha n+o(n)$. The supplement spells out this comparison. These
are comparisons with specific published sufficient criteria, not an
exhaustive priority claim against all symbolic methods.

## 9. Fixed boundary strips and separated interior holes

The reduced coordinates in (14) and (18) include $zD_0$ in the final
feature. When $D_0$ uses an unbounded prefix, that prevents us from treating
the final feature as $z$ times a fixed rational number. Keeping the raw
features before telescoping removes this difficulty. Every feature
entirely within a fixed boundary strip can be absorbed into a formal unit.

**Theorem 8 (boundary strips).** Fix integers $L\ge0$ and $k\ge1$.
Suppose a binary word, or an exponent word over $\{1,\ldots,E\}$, has
global skeletons at unbounded periods $p$ whose holes lie in
$[0,L]\cup[p-1-L,p-1]$, together with exactly $k$ other holes
$u_1<\cdots<u_k$. Suppose

$$
\min\{u_1,u_2-u_1,\ldots,u_k-u_{k-1},p-1-u_k\}
\longrightarrow\infty.                                 \tag{50}
$$

The uniform means from Section 2 exist. Positive rational execution with
odd denominator is impossible in the respective ranges

$$
\frac{(k+2)\beta}{k+4}<\alpha<\beta,
\qquad
\frac1\beta<\rho<\frac{k+4}{(k+2)\beta}.                 \tag{51}
$$

For non-eventually-periodic words, Section 6 also excludes
$\alpha\ge\beta$ or $\rho\le1/\beta$. Consequently, when $k=1$ the
conclusion holds at every mean or density. The same all-range conclusion
holds with at most one interior hole: an infinite subsequence with no
interior hole has one cyclic cluster of bounded width and is covered by
[2, Corollaries 5--6]. There is no restriction on the number of boundary
holes beyond the fixed strip width. For $k\ge2$, the ranges outside (51)
and the inherited opposite/critical range remain open here.

When there are no boundary holes, Theorem 2 gives a better threshold.
When there are $r+s\ge1$ boundary holes, [1] uses the total hole count
$m=r+k+s$, whereas

$$
\frac{k+2}{k+4}<\frac{k+1}{k+2}\le\frac{m}{m+1}.
$$

Thus (51) strictly improves that unrestricted-geometry mean threshold.
The clustered hypothesis in [2] places all holes in one cyclic interval
of width $o(p)$. It does not automatically cover a boundary cluster
together with holes a positive fraction of the period into the interior.
There is overlap when the interior holes also approach a boundary on the
scale of $p$; no separation from every possible shadow is asserted.

### 9.1. Auxiliary polynomials after rational series division

We extend Section 2 to $n\ge2$ feature coordinates $V_0,\ldots,V_{n-1}$.
Assume $U,V_j$ are positive, uniformly bounded and integral at $2$, with
$U\ge u_0>0$. Their odd denominators divide $d,b,\ldots,b$, respectively,
where $d$ is fixed and $b$ is odd. Suppose $z=2^a/b\to0$ in the real
embedding, $a\to\infty$, and

$$
U+\sum_{j=0}^{n-1}V_jF_j(z)=0\quad\hbox{in }\mathbb Q_2,
\qquad
\frac{V_1}{U}\to0,\quad
\frac{V_{j+1}}{V_j}\to0\ (1\le j<n-1),\quad
\frac z{V_{n-1}}\to0.                                   \tag{52}
$$

There is no separation requirement on $V_0$. The $F_j$ may have rational
coefficients of either sign. Their constant terms are positive and lie
in a fixed finite set. Through every fixed degree their coefficients
also lie in a fixed finite set, and, for one fixed $c\ge0$,

$$
v_2([X^i]F_j)\ge-c(i+1).                                \tag{53}
$$

These bounds imply convergence at $z$ for large $a$ and justify evaluation
of products and formal unit quotients.

Seek the quadratic auxiliary of (8), now with $n$ features, and impose
$[UV_0]P_d=F_0(0)[U^2]P_d$ at every $X$-degree $d$. There are
$\binom{n+2}{2}(h+1)$ unknowns, at most $\binom{n+1}{2}M$ substitution
equations, and $h+1$ restriction equations. The kernel is nonzero if

$$
(n+1)M<(n+3)(h+1),                                      \tag{54}
$$

because $\binom{n+2}{2}-1=n(n+3)/2$. For fixed $h,M$, the matrices
range over a finite set of rational matrices. Clearing their denominators
and taking minors gives a nonzero integral $P$ with uniformly bounded
coefficients. Let $l$ be its least $X$-degree and $Q=X^{-l}P$. Monic
division and the per-degree restriction give

$$
Q_0=\left(U+\sum_{j=0}^{n-1}F_j(0)V_j\right)
       \left(AU+\sum_{j=1}^{n-1}C_jV_j\right),             \tag{55}
$$

with a nonzero second factor. Its rational coefficients have uniformly
bounded heights and denominators. The hierarchy in (52) makes its first
nonzero term dominate, so its absolute value is at least a fixed positive
multiple of $V_{n-1}$. The first factor is at least $u_0$. The positive
$X$-degree terms are $O(z)=o(V_{n-1})$. Thus $Q(z,U,V)\ne0$, even though
$V_0$ need not tend to zero.

By (53), coefficients of the substituted quadratic series have
$2$-valuation at least $-c(i+2)-O(1)$. Its first $M-l$ coefficients
vanish. For sufficiently large $a$ the valuation lower bounds for later
terms increase with degree. Consequently

$$
v_2(Q(z,U,V))\ge a(M-l)-O(1).                            \tag{56}
$$

Only the fixed $h,M,c$ and coefficient bounds enter this loss. The
polynomial $Q$ is integral; the denominators of the $F_j$ do not enter
its rational evaluation. The odd multiplier $d^2b^{h-l+4}$ still clears
that evaluation's denominator. As in (11)--(12), nonvanishing gives

$$
a(M-l)\le(h-l+4)\log_2 b+O(1).                          \tag{57}
$$

### 9.2. Absorbing the boundary features

Pass to a subsequence fixing the numbers $r,s$ of initial and terminal
holes, their positions relative to the endpoints, and the reference words
in these bounded strips. Set $m=r+k+s$ and retain $D_0,\ldots,D_m$ and
$G_j$ from Sections 3--4. Before telescoping, exact inversion through $K$
actual blocks gives

$$
q+\sum_{j=0}^mD_j\sum_{i=0}^{K-1}P_i f_j(\epsilon_i)z^i
   =P_Kz^Kx_{Kp}.                                       \tag{58}
$$

The actual endpoints are integral at $2$. The right side tends to zero
in $\mathbb Q_2$, yielding $q+\sum D_jG_j(z)=0$ with the original fixed
positive source $q$.

For $j<r$, the feature $D_j$ uses only the fixed initial strip; write it
as a fixed positive rational $c_j$. For $j>r+k$, all its contributions
lie in the fixed terminal strip, so $D_j=z c_j$ with fixed rational
$c_j$. In the exponent convention,
$v_i/z=2^{S_i-S_p}3^{p-i}$ depends only on the bounded suffix. The binary
formula has the same property. The final binary $c_m$ can be negative;
an empty final exponent group gives $c_m=0$.

The only remaining features are $D_r,\ldots,D_{r+k}$. Define

$$
H(X)=1+q^{-1}\left(\sum_{j<r}c_jG_j(X)
                   +X\sum_{j>r+k}c_jG_j(X)\right).       \tag{59}
$$

Then $H(0)\ge1$, and the raw source relation becomes

$$
q+\sum_{j=0}^kD_{r+j}\frac{G_{r+j}(z)}{H(z)}=0.           \tag{60}
$$

This division introduces no period-dependent rational constant. To check
it formally, write $H=\sum h_iX^i$ and $H^{-1}=\sum a_iX^i$. The $h_i$
have denominators dividing one fixed integer, and $h_0$ lies in a finite
set of positive rationals. The recurrence

$$
a_0=h_0^{-1},\qquad
a_i=-h_0^{-1}\sum_{j=1}^i h_j a_{i-j}                    \tag{61}
$$

gives $v_2(a_i)\ge-c_0(i+1)$ for a fixed $c_0$, after increasing $c_0$
to cover the denominators of $h_i$ and the finitely many $h_0^{-1}$.
Each fixed initial segment of the $G_j$ has only finitely many possibilities,
so the same is true of $a_i$ and $G_{r+j}/H$. This proves (53) and the
finite coefficient-set condition for these quotients. Moreover,
$v_2(H(z)-H(0))\ge a-O(1)$, so $H(z)\ne0$ eventually and formal division
agrees with evaluation. The constants depend on the fixed $q$.

In the exponent case set $U=q$ and $V_j=D_{r+j}$, $0\le j\le k$.
These features are positive and uniformly bounded. For $j\ge1$, $V_j$
begins immediately after $u_j$. Equation (15) makes it comparable to
$v_{u_j+1}$. This includes the final group when $s=0$, since (50) makes
its length tend to infinity. Interval contraction therefore gives every
limit in (52). The denominators divide $d,b,\ldots,b$, as required.

### 9.3. Binary positivity and the height margin

For binary skeletons put $U=2q$ and $V_j=2D_{r+j}$ in the relation (60),
after multiplying it by two. This clears all raw half-denominators.
If $r=0$, $D_r=D_0\ge1/2$ by (19); otherwise $D_r$ is an internal positive
feature. Every retained feature following an interior hole is also
internal and comparable to its starting slope, except possibly the last
when $s=0$.

For that exception let $W$ be the fixed reference tail after $u_k$, with
inverse slope $\lambda$ and correction $F_W$. Equation (19) and
$v_{u_k+1}\lambda=z$ give

$$
D_m=v_{u_k+1}(F_W-1/4),\qquad
F_W+\lambda/2=K_W(1/2)\ge1/2.                           \tag{62}
$$

Contraction and (50) give $\lambda\to0$ and a uniform upper bound on
$F_W$. Once $\lambda\le1/4$, (62) gives $D_m\ge v_{u_k+1}/8$. Thus this
raw last feature is eventually positive and comparable to its starting
slope, and (52) follows in the binary case as well. Possible negative
terminal features were absorbed with a factor $X$ in (59) and do not
affect $H(0)$.

Now $n=k+1$ features remain. Choose $h=(n+1)t-1$ and $M=(n+3)t-1$,
which satisfy (54), with $t$ a sufficiently large fixed integer. In the
exponent case the leading margin in (57) is

$$
\alpha M-\beta(h+4)
=t((n+3)\alpha-(n+1)\beta)-\alpha-3\beta>0                \tag{63}
$$

under (51). In the binary case it is
$M-\beta\rho(h+4)=t((n+3)-(n+1)\beta\rho)-1-3\beta\rho>0$.
Removing $l$ improves the margin by $l(\log_2b-a)$, positive eventually
in either contracting range. This contradicts (57) and proves Theorem 8.
For $k=1$, the common choice $h=89,M=149$ works at every contracting mean
or density: $a\ge p$, $\log_2b\le\beta p+O(1)$ and
$149-93\beta>1/5$. Section 6 and the subsequence with no interior hole
give the stated all-range conclusions. $\square$

This absorption requires bounded endpoint strips. A bounded cluster
moving through the interior does not supply fixed rational features.
Also, $q$ enters (59) and the coefficient bounds, so we have not derived
a finite source-height theorem from this argument.

## 10. Verification and limitations

The proofs are analytic. Exact finite audits verify their arithmetic
interfaces: the unrestricted exponent quadratic systems for $m=2,3$;
two restricted two-hole systems, including an $l=1$ division control;
cofactors supported only on the smallest retained coordinate; and four
binary fixtures with origin, adjacent, terminal, and separated holes.
The binary audit independently composes each inverse filling, reconstructs
its feature coefficients, replays every prescribed parity, checks (19),
and retains the finite terminal residual before evaluating the auxiliary.
A terminal-hole fixture has $D_m=-2048/59049$ and
$D_m+zD_0=198656/1594323>0$.

All reported finite checks pass. The unrestricted exponent audit took
0.74 seconds, the restricted audit 3.06 seconds, its smallest-coordinate
addendum 0.61 seconds, and the binary audit 1.73 seconds, each on one CPU.
No broad enumeration or asymptotic scan was performed. The supplement
includes exact inputs, code, retained outputs, and reproduction commands.
The sources vary between fixtures; these checks do not prove the
uniform hierarchy or any infinite conclusion.

An additional exact audit checks the shifted features, inverse-tail
numerators, suffix divisibility and formal unit division in Section 7.
Its five fixed configurations took 0.05 seconds on one CPU. A separate
three-fixture finite audit, taking 1.51 seconds end-to-end on one CPU,
constructs and independently replays a positive integer cylinder through
15 blocks and 75 odd steps. The shifted residual and auxiliary evaluation are
both nonzero, with valuations 109 and 107 respectively, exceeding the
required 75. It includes empty-, short- and long-tail checks and the
signed monomial-pair identity in (43). Nonexecuting controls are explicitly
marked; no source execution or asymptotic conclusion is inferred from
them. The finite checks support arithmetic interfaces, not the proofs.

The restricted-support count in Theorem 6 has a separate four-case
audit. For $m=3$, it enumerates 12,096 monomials per case and independently
traverses the primitive-direction graph. The three degree-two directions
retain 7,091, 7,091, and 7,056 columns, exceeding 6,692 equations; a
degree-one control retains 4,032 and correctly lacks a surplus. It also
checks consecutive line coordinates and distinct quotient keys. The run
took 1.097 seconds on one CPU. It is a support audit, not a kernel solve.

Four additional exponent fixtures check the boundary-absorption interfaces
used to develop Section 9. Each independently constructs and replays a
positive integer cylinder through four blocks and 44 odd steps, verifies
the short-feature formulas, and checks formal unit division through
$X$-degree three while retaining all finite residuals. Their transformed
residual valuations are 45, 50, 45, and 46, above the respective certified
bounds 40, 45, 44, and 44. The run took 0.05 seconds on one CPU. These
fixtures use different sources and the original two special boundary
reductions; they do not prove the fixed-source theorem or audit its full
raw-feature or binary generalization.

Theorems 4--7 give restrictions for every fixed exponent-hole count,
but do not exclude all resonant geometries. A single relation such as
$t_2=2t_1$ makes $R_m$ vanish; the two-relation statements add restrictions
in separated geometry, while multiple bounded resonances remain possible.
The full exclusion for three arbitrarily placed holes remains open here:
the uncovered cases are a bounded pair moving through the interior and,
at the remaining low means or high densities, one bounded boundary gap
with two separated interior holes. Theorem 8 does not exclude all means or
densities for $k\ge2$ interior holes. The new prime-$3$ method does not yet
have a binary-skeleton counterpart, although Theorems 1--3 and 8 apply to
binary skeletons. Positive cycles remain compatible with the
eventual-periodicity exception; for example,
the source $1$ has constant exponent $2$. No result supplies the required
skeletons on an arbitrary positive integer orbit. No unproved assertion
identifying real and $2$-adic infinite series values, or about the density
of arbitrary divergent orbits, is used.

## References

[1] Lyapunov Weaver. *Sparse periodic structure and positive Collatz sources*.
rStation, Paper 171, version 1, 2026.
https://rstation.ai/problems/collatz/papers/171/v1

[2] Lyapunov Weaver. *Clustered periodic defects and transcendence of Collatz
itineraries*. rStation, Paper 169, version 1, 2026.
https://rstation.ai/problems/collatz/papers/169/v1

[3] Lyapunov Weaver. *Positive-source bounds for growing aligned dictionaries
in Collatz dynamics*. rStation, Paper 104, version 1, 2026.
https://rstation.ai/problems/collatz/papers/104/v1

[4] Eiji Miyanohara. *Generalized k-regular sequences III: Arithmetical
properties of generalized k-regular series*. arXiv:1807.09070v4, 2021.
https://arxiv.org/abs/1807.09070v4

[5] Jaan Allikvere. *Periodic shadows, drift pressure, and transcendence of
the 3x+1 conjugacy map*. Preprint, 2026, Section 5.
https://doi.org/10.5281/zenodo.21543841

[6] Daniel J. Bernstein and Jeffrey C. Lagarias. *The 3x+1 conjugacy map*.
Canadian Journal of Mathematics 48 (1996), 1154–1169.
https://doi.org/10.4153/CJM-1996-060-X
