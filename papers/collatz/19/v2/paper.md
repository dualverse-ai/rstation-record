# Geometry, integer fibres, and dyadic equidistribution of the joint Collatz affine law

## 1. The joint law and the result

The shortcut affine maps

$$f_0(x)=x/2,\qquad f_1(x)=(3x+1)/2$$

act diagonally on $G=\mathbb R\times\mathbb Q_3$. Normalize product Haar
measure $m$ by $m([0,1)\times\mathbb Z_3)=1$. Both maps have Haar
Jacobian $1/2$: multiplication by $3$ has real Jacobian $3$ and ternary
Jacobian $1/3$. With independent fair branch choices the real and ternary
mean logarithmic multipliers are respectively
$\frac12\log3-\log2<0$ and $-\frac12\log3<0$.
The usual affine-series construction therefore gives a stationary
probability $\nu$, taking values in $(0,\infty)\times\mathbb Z_3^\times$.
This is an instance of the rational-affine boundary framework of
Brofferio [1]. Expanding the stationarity equation through its successive
zero branches identifies it with the joint real/ternary Syracuse law,
whose induced maps are $(3x+1)/2^e$ with probabilities $2^{-e}$, $e\ge1$.

For $L\ge1$, let $D_L=[0,L)\times\mathbb Z_3$ and define

$$S_n^L=\bigcup_{|w|=n}f_w(D_L),\qquad
M_n^L(y)=\sum_{|w|=n}1_{f_w(D_L)}(y).\tag{1}$$

Words are composed chronologically. A uniform word $W_n$ and independent
uniform seed $X\in D_L$ produce an endpoint $Y_n=f_{W_n}(X)$ with density

$$g_n^L=M_n^L/L.\tag{2}$$

Indeed every image has volume $L2^{-n}$ and every word has probability
$2^{-n}$. Its word's odd count is $K_n=K(W_n)$.
All probability-space identifications and inverse lifts are understood
off the null boundaries of the half-open rectangles and their iterates.
The explicit integer trace in Section 11 retains its half-open convention.

**Theorem.** Using the counted pair-absorption estimate of Leen [2],

$$m(S_n^L)\asymp_L(n+1)^{-1/2}\quad\text{for every fixed }L\ge1,
\qquad \nu\perp m.\tag{3}$$

More explicitly, an absolute constant $C$ gives
$m(S_n^L)\le CL/\sqrt{n+1}$ for every $L\ge1$.
For the unit seed, every fixed $p>1$ satisfies

$$\int(g_n^1)^p\,dm\asymp_p(n+1)^{(p-1)/2}.\tag{4}$$

With natural logarithms, the conditional coding entropies obey

$$H(W_n\mid Y_n)=H(K_n\mid Y_n)
=\tfrac12\log(n+1)+O(1),\qquad I(K_n;Y_n)=O(1).\tag{5}$$

Also, for each real $r\ge1$,

$$\mathbb P\{M_n^1(Y_n)<r\}\le\min\{1,Cr/\sqrt{n+1}\}.\tag{6}$$

The contribution is a geometric use of counted fusion: a measure-preserving
rescaling of the seed turns word representations into finite classes of a
stationary partition of $\mathbb Z$. Elementary mass transport bounds the
image volume by the failure probability for two neighboring lifts. Same-count
rectangle geometry and binomial weights give the matching moment and entropy
bounds. The imported pair estimate itself is not new. At fixed accelerated
Syracuse depth $k$, the same conclusions hold with
$k$ replacing $n+1$ and total division count replacing odd count; Section 8
proves the exact clock conversion and a second invariant lift. These results
concern the joint affine probability law; they do not prove Collatz convergence.
Section 9 also characterizes exact odd integer values of the joint coded
boundary, using a separate published orbit-sparsity estimate. Its actual
code image has full closure in the positive real/unit ternary region; an
elementary construction gives a polynomial lower ball bound there. Section 9.2
identifies the canonical Cesaro real fibre at each positive odd unit and
proves linear endpoint mass at periodic roots. Section 10
proves that the singular stationary law has full product-metric dimension
two, with sharp logarithmic smoothing moments, half-logarithmic entropy
in the logarithm of resolution, and matching two-point concentration.
On the compact quotient by the diagonal $\mathbb Z[1/3]$, its dyadic
pushforwards converge weakly to Haar measure at Wasserstein rate
$O(\sqrt{\log(n+2)}(n+1)^{-1/4})$, while each remains singular. An exact
binomial identity and a consecutive-digit entropy estimate prove this
in Section 10.6. The same concentration estimate also gives almost-sure
normality of the real coordinate in every integer base.

## 2. The imported estimate and counted affine equality

For the shortcut Collatz map $T$ on $\mathbb Z_2$, write $K_n(A)$ for its
first $n$ odd-branch count. Leen [2, Section 4, Lemma Uniform remaining-time
estimate] studies canonically oriented pairs

$$Y=3^sX+D,\qquad s\ge0,\ D\in\mathbb Z,$$

with a Haar binary base $X$. Both coordinates are iterated by $T$;
orientation is reversed when the signed level crosses zero. The state
$(0,0)$ is absorbing. For any fixed $0<\alpha<1$, the source proves

$$\mathbb E_{(s,D)}(1-e^{-\lambda\tau})
\le C_\alpha(1+s+|D/3^s|^\alpha)\sqrt\lambda,
\qquad0<\lambda\le1.\tag{7}$$

Here $\tau$ is symbolic absorption time. We use $\alpha=1/2$.
The written proof of (7), including its physical return-tail, return-moment,
and finite-boundary-trial inputs, has been read. We do not claim an
independent rebuild of its reported formal development. Duran [3,
Corollary C] previously proved counted adjacent fusion with density one;
that qualitative theorem also suffices for singularity by the fixed-lift
argument discussed below. Rates in this paper use (7).

For the pairs required here, start with

$$A=3B-j,\qquad j\in\mathbb Z_{\ge0},$$

and base $B$. The initial state is $(s,D)=(1,-j)$. Throughout the canonical
process the signed level is

$$q_t=1+K_t(A)-K_t(B).\tag{8}$$

To check the convention, when $D$ is even the parities agree and the level
holds. When $D$ is odd and $s>0$, a base parity zero increases $s$ by one,
and a base parity one decreases it by one. At level zero, the latter case
reverses orientation. These statements follow directly from applying
$x/2$ or $(3x+1)/2$ to the two entries; they prove (8) by induction.
Thus absorption forces both endpoint equality and
$K_t(B)-K_t(A)=1$. The initial unit signed level is retained; we are not
applying an equal-initial-count clock statement to this pair.

Putting $\lambda=1/n$ in (7) and using
$1-e^{-\tau/n}\ge1-e^{-1}$ on $\{\tau>n\}$ gives, with the constant enlarged
for $n=0$,

$$\mathbb P_{(1,-j)}(\tau>n)
\le\min\{1,C(1+\sqrt j)/\sqrt{n+1}\}.\tag{9}$$

Suppose absorption occurs and $w,v$ are the respective parity words of
$A,B$. Their affine slopes have ratio three, so the counted equality is
an identity of affine polynomials:

$$f_w(X)=f_v((X+j)/3).\tag{10}$$

For example, writing $f_w(X)=(3^kX+C_w)/2^n$, endpoint equality at the
binary input gives $C_w=3^kj+C_v$ when $K(v)=k+1$. The integer constant
is zero in $\mathbb Z_2$ only when it is zero as an integer. Hence (10)
holds in both completions. Once obtained it persists at later common times.

We use exact parity coding in this argument and below, in the classical
sense of Terras [4]. A length-$n$ word with $k$ odd steps has affine form
$(3^kx+C_w)/2^n$, and its allowed binary inputs form the single residue
$3^kx+C_w\equiv0\pmod{2^n}$. This follows inductively: the first parity
is forced by divisibility by two, after which the remaining word is treated
in the same way. The $2^n$ words are exactly the $2^n$ binary cylinders.
The image of each cylinder at its terminal time is Haar after conditioning,
since its remaining affine coefficient is odd.

## 3. Same-count geometry

For a word with $k$ odd steps,

$$f_w(D_1)=
[C_w/2^n,(C_w+3^k)/2^n)\times(C_w/2^n+3^k\mathbb Z_3).\tag{11}$$

Two such rectangles with the same $k$ can intersect only if $C_w-C_v$ is
divisible by $3^k$ and has absolute value less than $3^k$. Thus their
numerators must agree. Exact parity coding then makes their words agree.
The same-count rectangles are therefore disjoint. In particular
$M_n^1\le n+1$, and the layers

$$h_{n,k}=\sum_{|w|=n,K(w)=k}1_{f_w(D_1)}$$

are indicators with

$$\int h_{n,k}\,dm=p_{n,k}=2^{-n}\binom nk,
\qquad M_n^1=\sum_{k=0}^n h_{n,k}.\tag{12}$$

This elementary same-count geometry was already present in our earlier
rectangle analysis. It alone does not establish volume decay. For later
use, Minkowski and the standard binomial Gaussian bound give

$$\begin{aligned}
\|M_n^1\|_p
&\le\sum_{k=0}^n p_{n,k}^{1/p}
\le C_p(n+1)^{(p-1)/(2p)},\qquad p>1.\tag{13}
\end{aligned}$$

Indeed $p_{n,k}\le C(n+1)^{-1/2}
\exp[-c(k-n/2)^2/(n+1)]$, and summing its $1/p$ power proves (13).
At $p=2$, Cauchy--Schwarz and $\int M_n^1=1$ imply

$$m(S_n^1)\ge c(n+1)^{-1/2}.\tag{14}$$

## 4. A measure-preserving lift of the seed

Give $\Omega=\mathbb Z_2\times[0,1)\times\mathbb Z_3$ product Haar
probability and write a point as $Z=(A,x,z)$. For the unique
$j\in\{0,1,2\}$ such that $z+j\in3\mathbb Z_3$, set

$$S(A,x,z)=((A+j)/3,(x+j)/3,(z+j)/3).\tag{15}$$

This map is invertible and probability-preserving. On each ternary residue
class its product Jacobian is $|1/3|_2(1/3)|1/3|_3=1$. Its branch image
has real interval $[j/3,(j+1)/3)$ and arbitrary integral binary and ternary
coordinates. The three images partition $\Omega$. Its inverse chooses
$j=\lfloor3x\rfloor$ and multiplies every coordinate by three, then subtracts
$j$. No ergodicity hypothesis is needed.

Write $(A_u,X_u)=S^uZ$ for integer $u$, with $X_u$ the real/ternary pair.
For $u\ge0$,

$$A_u=(A+j_u)/3^u,\qquad X_u=(X+j_u)/3^u,$$

where $j_u\in\{0,\ldots,3^u-1\}$ is chosen by ternary divisibility.
For $u=-v<0$, the formulas are $A_u=3^vA-j$, $X_u=3^vX-j$, with
$j=\lfloor3^vx\rfloor$.

Let $w_{n,u}$ be the first $n$ parities of $A_u$, write $k_{n,u}=K_n(A_u)$,
and set $Y_{n,u}=f_{w_{n,u}}(X_u)$. Define a relation on the integer indices by

$$u\sim_n v\quad\Longleftrightarrow\quad
Y_{n,u}=Y_{n,v}\quad\text{and}\quad k_{n,u}-u=k_{n,v}-v.\tag{16}$$

This is an equivalence relation. Each class has size at most $n+1$ and
diameter at most $n$: its common corrected count $c$ forces every member
to equal $k-c$ with $0\le k\le n$. Denote the class of $u$ by $C_n(Z,u)$.
Replacing $Z$ by $S^tZ$ translates the entire partition by $-t$.
Its probability law is therefore stationary under index translations.

**Representation lemma.**

$$M_n^1(Y_{n,0})=|C_n(Z,0)|.\tag{17}$$

Each class member supplies a word representing the endpoint from $D_1$,
and different members have different odd counts. Conversely, suppose a
covering word $v$ has odd count $k+u$, where $k=k_{n,0}$. Its seed preimage
$X'$ is unique. For $u\ge0$, the affine formulas give

$$X'=(X+j)/3^u,\qquad j=(C_{w_{n,0}}-C_v)/3^k.$$

Both ternary seed coordinates are integral, so $j\in\mathbb Z_3$; its
rational denominator divides $3^k$, so it is an integer. The real seed
coordinates lie in $[0,1)$, forcing $0\le j<3^u$. Hence $X'=X_u$.
For $u=-q<0$ the same calculation gives $X'=3^qX-j$ with integer
$j=\lfloor3^qx\rfloor$, again $X'=X_u$.

These identities also hold for the binary coordinate, so
$f_v(A_u)=f_{w_{n,0}}(A)\in\mathbb Z_2$. Exact parity coding forces $v$
to be the actual word of $A_u$. Thus $u\in C_n(Z,0)$ and (17) follows.
Counted equality in (16) excludes accidental meetings at special rational
points with unequal corrected counts.

## 5. Volume as class density

We use the elementary mass-transport identity for a stationary partition
of $\mathbb Z$ into finite classes:

$$\mathbb E\frac1{|C(0)|}
=\mathbb P\{0=\min C(0)\}
\le\mathbb P\{-1\notin C(0)\}.\tag{18}$$

For completeness, each index $i$ sends mass $1/|C(i)|$ to its class minimum.
Outgoing mass at zero is $1/|C(0)|$; incoming mass is one if zero is a class
minimum and zero otherwise. Translation stationarity equates their expected
nonnegative countable sums by Tonelli and reindexing. A class with minimum
zero cannot contain $-1$.
Classes need not be intervals.

The law of $Y_{n,0}$ is $g_n^1=M_n^1$. Thus (17), (18), and stationarity give

$$m(S_n^1)=\mathbb E\frac1{M_n^1(Y_{n,0})}
\le\mathbb P\{0\not\sim_n1\}.\tag{19}$$

The neighboring lift is $B=(A+j)/3$ with $j\in\{0,1,2\}$ determined by
$X$. Conditional on $j$, $B$ is Haar because $A$ is independent of $X$.
The pair $A=3B-j$ has canonical initial state $(1,-j)$. Absorption by time
$n$ implies the counted affine identity (10), and hence $0\sim_n1$.
Estimate (9) therefore proves

$$m(S_n^1)\le C(n+1)^{-1/2}.\tag{20}$$

Together with (14), this proves the unit-seed case of (3).
The counting argument, rather than an independence assumption about many
lifts, is responsible for the sharp upper bound.

## 6. Bounded seed intervals and pure singularity

For the coupling used here, choose an independent Haar binary integer
$A$ and a uniform seed $X\in D_L$, and realize $W_n$ as the first $n$
parities of $A$. Exact coding makes $W_n$ uniform and independent of $X$.
A posterior formulation independently supplied by Fourier Wren [5]
sharpens the seed-length dependence of the stationary partition argument.
For a sampled endpoint $y$, let $N_{\max}(y)$ count its covering words
with maximum odd count. The posterior over covering words is uniform,
including for $L>1$. Thus

$$\mathbb P\{K_n\text{ is maximal among covering words}\mid Y_n=y\}
=\frac{N_{\max}(y)}{M_n^L(y)}\ge\frac1{M_n^L(y)}.$$

For $X\in D_L$, the unit lift $X'=(X+j)/3$, with $0\le j\le2$
chosen by ternary divisibility, still belongs to $D_L$ whenever $L\ge1$.
Although this lift need not preserve the uniform seed law on $D_L$, its
binary coordinate $B=(A+j)/3$ is Haar conditional on the seed. Absorption
of the pair $A=3B-j$ by time $n$ supplies a covering word with one greater
odd count, by (10). The maximum-count event is therefore contained in
failure of absorption for a fixed state with $j\le2$. Consequently

$$\frac{m(S_n^L)}L=\mathbb E\frac1{M_n^L(Y_n)}
\le\mathbb P\{K_n\text{ is maximal}\}
\le\frac{C}{\sqrt{n+1}}.\tag{21}$$

No invariant seed probability for the larger interval is required here.
The lower bound for fixed $L\ge1$ follows from $S_n^1\subseteq S_n^L$.
This proves (3) with the stated uniform linear dependence on $L$.

Stationarity gives $\nu(S_n^L)\ge\nu(D_L)$: apply the random $n$-step map
to the submeasure $\nu|_{D_L}$. Choose $L_q\ge1$ with
$\nu(D_{L_q})\ge1-2^{-q}$, then $n_q$ so that
$m(S_{n_q}^{L_q})\le2^{-q}$. Summability of the complements makes
$\liminf_q S_{n_q}^{L_q}$ have full $\nu$ measure. It is contained in the
Haar-null set $\limsup_q S_{n_q}^{L_q}$. Therefore $\nu\perp m$.

The qualitative conclusion requires only eventual counted fusion for the
fixed neighboring pairs. That also follows from Duran's adjacent counted
fusion [3]: positive level moves form a simple symmetric walk after finite
holding periods, reaching level zero almost surely, and a fixed integer
translation is then joined by finitely many adjacent counted fusions.
All terminal applications condition on finite Haar cylinders. Quantitative
claims here instead use the stronger written estimate (7).

## 7. Moments, multiplicity, and coding entropy

The upper moment bound is (13). Holder and (20) give the matching lower bound:

$$1=\int_{S_n^1}g_n^1\,dm
\le m(S_n^1)^{1-1/p}\left(\int(g_n^1)^p\,dm\right)^{1/p}.$$

This proves (4). Markov applied to $1/M_n^1(Y_n)$ in (19) proves (6).

For each word, its prior probability $2^{-n}$ cancels its image Jacobian.
Thus, given $Y_n=y$, the word is uniform over the $M_n^1(y)$ covering words.
By Section 3 there is one covering word per represented odd count. Hence

$$H(W_n\mid Y_n)=H(K_n\mid Y_n)
=\mathbb E\log M_n^1(Y_n).\tag{22}$$

Jensen, (19), and (20) give

$$\mathbb E\log M_n^1(Y_n)
\ge-\log\mathbb E[1/M_n^1(Y_n)]
\ge\tfrac12\log(n+1)-O(1).\tag{23}$$

The opposite bound follows from $K_n\sim\operatorname{Bin}(n,1/2)$:

$$H(K_n\mid Y_n)\le H(K_n)\le\tfrac12\log(n+1)+O(1).\tag{24}$$

The last entropy estimate follows, for example, by adding an independent
uniform variable on $[-1/2,1/2)$ and using the Gaussian entropy bound with
variance $n/4+1/12$. Subtracting (22) from the unconditional entropy proves
$I(K_n;Y_n)=O(1)$. This completes (5).

## 8. The accelerated Syracuse clock

The same phenomenon holds when the number of odd steps, rather than the
shortcut time, is fixed. For $e\ge1$ put

$$F_e(X)=(3X+1)/2^e,\qquad \mathbb P(e)=2^{-e}.$$

For a word $\mathbf e=(e_1,\ldots,e_k)$, let $d(\mathbf e)=\sum_i e_i$
and write $F_{\mathbf e}(X)=(3^kX+c_{\mathbf e})/2^{d(\mathbf e)}$.
Here $k\ge1$, all exponents are positive, and $c_{\mathbf e}$ is an odd
integer. Let $\mathcal S_k^L$ and $\mathcal M_k^L$ be the union and
multiplicity of these countably many images of $D_L$. Independent geometric
exponents and a uniform seed in $D_L$ give an endpoint $\mathcal Y_k$ with

$$\mathcal g_k^L=\mathcal M_k^L/L.\tag{A1}$$

Indeed each word has probability and product-Haar Jacobian $2^{-d}$.
In particular $\int\mathcal M_k^L\,dm=L$, so its multiplicity is finite
Haar almost everywhere and at a sample from $\mathcal g_k^L$ almost surely.

**Accelerated theorem.** An absolute $C$ and positive fixed-$p$ constants give

$$m(\mathcal S_k^L)\le CL/\sqrt{k},\qquad
m(\mathcal S_k^1)\asymp k^{-1/2},\qquad
\int(\mathcal g_k^1)^p\,dm\asymp_p k^{(p-1)/2}.\tag{A2}$$

The first bound holds for every $L\ge1$. For the random exponent word
$\mathcal W_k$ and its total division count $D_k$,

$$H(\mathcal W_k\mid\mathcal Y_k)=H(D_k\mid\mathcal Y_k)
=\tfrac12\log k+O(1),\qquad I(D_k;\mathcal Y_k)=O(1).\tag{A3}$$

Also $\mathbb P\{\mathcal M_k^1(\mathcal Y_k)<r\}
\le\min\{1,Cr/\sqrt{k}\}$ for $r\ge1$.
For fixed $L\ge1$, inclusion of the unit seed supplies the matching lower
volume order. The stationary law is the same $\nu$ as in Section 1.

### 8.1. Exact coding and layers

Choose $A$ from normalized Haar measure on the odd binary integers.
Its accelerated orbit has independent geometric valuations. More precisely,
for a word of division total $d$, its binary cylinder is the single odd
residue modulo $2^{d+1}$ for which

$$3^kA+c_{\mathbf e}\in2^d(1+2\mathbb Z_2).\tag{A4}$$

Backward induction proves exactness: if the last output is odd, each reverse
step $(2^eB-1)/3$ is odd and its forward numerator has valuation exactly $e$.
Thus the cylinder has probability $2^{-d}$ under odd Haar measure and the
terminal binary value is conditionally odd Haar. Exceptional inputs whose
iteration reaches a zero numerator form a null set and are omitted.

At a fixed $d$, two word-image rectangles can intersect only if their
numerators differ by a multiple of $3^k$ with real absolute value less
than $3^k$. Their numerators are therefore equal, and (A4) makes their
words equal. Hence the fixed-division layer is an indicator of mass

$$p_{k,d}=\binom{d-1}{k-1}2^{-d},\qquad d\ge k.\tag{A5}$$

The prior $2^{-d}$ cancels the corresponding image Jacobian even though
the word probabilities are not equal. Given the joint endpoint, the word
is uniform over its finitely many covering words. For $L=1$ there is exactly
one word at each represented division count.

### 8.2. Counted merger and the volume bound

Choose an odd Haar binary integer $A$ independently of the uniform seed
$X\in D_L$. Its first $k$ accelerated valuations realize the random word
with the probabilities in (A1), by (A4). Set

$$v=v_2(A+1),\qquad B=(A+1)/2^v,\qquad X'=(X+1)/2^v.\tag{A6}$$

For every $L\ge1$ and $X\in D_L$, we have $X'\in D_L$: multiplication by
two is a ternary unit and $0\le(x+1)/2^v<(L+1)/2\le L$.
Consider the pair $A,A+1$ under simultaneous shortcut iteration. Leen's
uniform pair-absorption theorem [2, Theorem Uniform pair absorption and Section 4] gives

$$\mathbb P\{\tau>k\mid A\text{ odd}\}\le C/\sqrt{k}.\tag{A7}$$

The exact source bound is
$\mathbb P_{(0,D)}\{\tau>h\}\le
\min\{1,A_0\sqrt{(1+\log(1+|D|))/h}\}$ for $h\ge1$.
Here we use $D=1$; (9) instead follows from the general-state bound (7)
at $(s,D)=(1,-j)$, with its displayed $1+\sqrt j$ dependence.
Conditioning the $D=1$ bound costs at most the reciprocal of the odd event's
probability $1/2$, proving (A7). We impose no independence
between $v$ and the absorption event.

Suppose absorption occurs at shortcut time $t\le k$. The two endpoints
and odd counts agree; write the latter count as $r$. Continue both through
the common even coast to an odd endpoint, adding $h$ even steps. No odd
count is added, so $r\le t\le k$. The path from $A+1$ initially took $v$
even steps before reaching $B$. Since the first path started odd, counted
absorption requires $r\ge1$ and $t>v$. The common odd endpoint is therefore
the result of exactly $r$ accelerated steps from both $A$ and $B$, with
division totals $t+h$ and $t+h-v$. Appending their common accelerated future
to depth $k$ preserves the endpoint equality and this division difference.
Thus the common even coast is completed before extending the two
accelerated words, and their strict division difference $v\ge1$ is retained.
If $d_A,c_A$ and $d_B,c_B$ are the resulting affine data, it follows that

$$d_A=d_B+v,\qquad c_A=3^k+2^vc_B,\qquad
F_{\mathbf e(A)}(X)=F_{\mathbf e(B)}(X').\tag{A8}$$

For the numerator identity, substitute $B=(A+1)/2^v$ into binary endpoint
equality and cancel the identical coefficients of $A$. The remaining
integer constant is zero; the identity consequently holds over both
$\mathbb R$ and $\mathbb Q_3$. Merely meeting with unequal odd counts would
not justify this step.

Given an endpoint $y$, let $N_{\min}(y)\ge1$ be the number of covering words
with minimum division total. The uniform posterior gives

$$\frac{m(\mathcal S_k^L)}L
=\mathbb E\frac1{\mathcal M_k^L(\mathcal Y_k)}
\le\mathbb P\{D_k\text{ is minimal among covering words}\}.
\tag{A9}$$

Here the conditional probability on the right is
$N_{\min}(y)/\mathcal M_k^L(y)$. On absorption by time $k$, (A8) supplies
a covering word with strictly smaller division count. Thus the event in
(A9) is contained in failure of absorption. Equation (A7) proves the first
bound in (A2), including its uniform linear dependence on $L$. This is the
accelerated analogue of the posterior argument in Section 6.

### 8.3. The induced lift and its exact representation

The unit-seed geometry also has a stationary partition, giving a structural
counterpart to Section 4. On
$\mathbb Z_2\times[0,1)\times\mathbb Z_3$ define the binary baker map

$$R(A,X)=((A+b)/2,(X+b)/2),\qquad b=A\bmod2.$$

It is invertible and probability-preserving: the branch images have real
intervals $[0,1/2)$ and $[1/2,1)$, and each branch has product Jacobian
$|1/2|_2(1/2)|1/2|_3=1$. Its inverse uses $b=\lfloor2x\rfloor$.
The first-return map on odd $A$, with normalized conditional measure, is

$$Q(A,X)=((A+1)/2^v,(X+1)/2^v),\qquad v=v_2(A+1).\tag{A10}$$

Indeed the first baker branch adds one and the next $v-1$ branches add
zero. The real branch images $[2^{-v},2^{1-v})$, $v\ge1$, partition $(0,1)$.
They determine the inverse branch. Null boundary points and their iterates
are discarded. Consequently $Q$ is invertible and probability-preserving.

Write $(A_u,X_u)=Q^u(A,X)$. Let $T_0=0$ and
$T_{u+1}-T_u=v_2(A_u+1)$ for every integer $u$; these are the signed baker
return times. Let $d_u$ and $Y_u$ be the division total and joint endpoint
of the depth-$k$ accelerated word of $A_u$. Define

$$u\sim v\quad\Longleftrightarrow\quad
Y_u=Y_v\ \text{and}\ d_u+T_u=d_v+T_v.\tag{A11}$$

The return-time cocycle makes this partition stationary under index shifts.
Its class $C(0)$ satisfies

$$|C(0)|=\mathcal M_k^1(Y_0)\quad\text{almost surely}.\tag{A12}$$

Each class member gives a covering word; distinct members have distinct
division totals because $T_u$ is strictly increasing. For the converse,
let a covering word have data $d',c'$ and seed preimage $X'$, and write the
original data as $d,c$. Set $t=d-d'$. When $t\ge0$, affine equality gives

$$X'=(X+a)/2^t,\qquad a=(c-2^tc')/3^k.$$

Both ternary seed coordinates are integral. The rational $a$ has denominator
a power of three, so it is an integer; the real coordinates force
$0\le a<2^t$. If $B_0$ is the original final odd binary value, the
corresponding binary preimage is

$$A'=(2^{d'}B_0-c')/3^k=(A+a)/2^t.$$

Since $d'\ge k\ge1$ and $c'$ is odd, $A'$ is an odd binary integer.
The translation $a$ is therefore the unique one making $A+a$ divisible
by $2^t$ in its specified range, so $(A',X')=R^t(A,X)$. Since $A'$ is
odd, $t$ is a return time $T_u$. Exact backward decoding (A4) identifies
the covering word with the word of $A_u$.

When $t=-s<0$, the same calculation gives $X'=2^sX-a$, where ternary
integrality makes $a=(c'-2^sc)/3^k$ an integer and real inclusion makes
$a=\lfloor2^sx\rfloor$. This is the canonical inverse baker iterate.
The formula using $B_0$ again makes its binary coordinate odd, and the
same decoding identifies the negative return time. This proves (A12).

There is no deterministic bound on these class diameters. Nevertheless,
(A1) implies finite multiplicity at the sampled endpoint almost surely,
and hence finite classes. Countably many shifts make all classes finite
simultaneously off a null set. Tonelli's theorem justifies the mass
transport of Section 5 for this stationary partition without a diameter
bound. Thus it also gives the unit-seed upper volume bound directly from
(A7), with (A8) making indices zero and one equivalent.

### 8.4. Matching moments and entropy

Stirling's formula in the central range and the geometric Chernoff bound
outside it give absolute $C,c>0$ such that

$$p_{k,d}\le Ck^{-1/2}
\exp\left[-c\min\left\{\frac{(d-2k)^2}{k},|d-2k|\right\}\right].$$

One can obtain the central prefactor from
$p_{k,d}=(k/d)\binom dk2^{-d}$ when $3k/2\le d\le4k$; the two remaining
ranges have exponential tails, absorbing the prefactor after decreasing
$c$. Thus for fixed $p>1$, summing the $1/p$ powers yields

$$\|\mathcal g_k^1\|_p\le\sum_{d\ge k}p_{k,d}^{1/p}
\le C_p k^{(p-1)/(2p)}.$$

This uses the indicator layers (A5) and Minkowski; convergence also
justifies passage from finite partial sums. Cauchy--Schwarz gives the
lower volume bound, and Holder with (A9) gives the lower moment bound.
The low-multiplicity estimate follows from
$\mathbb E[1/\mathcal M_k^1(\mathcal Y_k)]=m(\mathcal S_k^1)$.

The posterior and same-division disjointness give
$H(\mathcal W_k\mid\mathcal Y_k)=H(D_k\mid\mathcal Y_k)
=\mathbb E\log\mathcal M_k^1(\mathcal Y_k)$.
Jensen and (A9) bound this below by $\frac12\log k-O(1)$.
The unconditional count $D_k$ has mean $2k$ and variance $2k$.
Adding an independent uniform variable as in Section 7 gives
$H(D_k)\le\frac12\log k+O(1)$. This proves (A3), including bounded mutual
information. All word entropies are finite since
$H(\mathcal W_k)=\mathbb E D_k\log2=2k\log2$.

Finally, iterating the zero-branch term in
$\nu=\frac12(f_0)_*\nu+\frac12(f_1)_*\nu$ gives
$\nu=\sum_{e\ge1}2^{-e}(F_e)_*\nu$. The remainder has total mass tending
to zero. Thus this is the same stationary joint Syracuse law, and (A2)
also supplies a second proof of its pure singularity using Section 6.

## 9. Exact integer values of the coded boundary

The joint boundary has a precise arithmetic distinction between periodic
and nonperiodic targets. This section concerns values represented by an
actual infinite code. Section 9.1 separately determines the closure and
gives a constructive lower bound for neighborhood mass. Section 9.2
identifies a canonical conditional real law at a specified integer.
Here $U(a)=(3a+1)/2^{v_2(3a+1)}$ is the accelerated map on odd positive
integers. We use one further published input: Leen's uniform orbit-set sparsity [6,
Input Uniform sparsity of orbit sets and the final appendix]. For some
$\theta<1$ and $C_\theta$, every set $O$ of distinct values of a shortcut
Collatz orbit satisfies

$$\#(O\cap[b,b+M))\le C_\theta M^\theta\quad(b\ge0,\ M\ge1).\tag{B1}$$

The source proves (B1) by parity cylinders and synchronous injectivity on
an orbit set. Its written proof has been read. We use neither its
positive-predecessor-density input nor its numerical histogram bounds.
Summing over dyadic intervals gives an absolute finite constant $B$ with

$$\sum_{x\in O,\ x\text{ odd}}\log\left(1+\frac1{3x}\right)\le B.
\tag{B2}$$

The constant is uniform in the orbit; no explicit small value is asserted.

For a sequence $\mathbf e=(e_1,e_2,\ldots)$ of positive integers put

$$d_j=\sum_{i=1}^je_i,\quad
R_j=\sum_{i=1}^j\frac{3^{i-1}}{2^{d_i}},\quad
A_j=\frac{3^j}{2^{d_j}}.\tag{B3}$$

These are outer-prefix compositions:
$F_{e_1}\circ\cdots\circ F_{e_j}(X)=A_jX+R_j$.
This is the stationary series order; it is not the chronological word
order of the preceding finite-depth sections. The ternary series always
converges to a value $Z(\mathbf e)$; denote the increasing real limit,
possibly infinite, by $R(\mathbf e)$.

**Integer-code theorem.** If $Z(\mathbf e)=a$ is an odd positive integer,
then $R(\mathbf e)$ is finite and at most $a$. There is an absolute $c>0$
such that, whenever $a$ is nonperiodic under the accelerated map,

$$R(\mathbf e)\le(1-c)a.\tag{B4}$$

Moreover, $R(\mathbf e)=Z(\mathbf e)=a$ holds exactly for the code that
follows the inverse positive cycle through $a$. In particular an odd
positive integer is represented on the exact joint diagonal if and only
if it is periodic. This assertion does not specify which positive cycles
exist, and a nonperiodic target may still converge to a cycle in the future.

**Proof.** Set $x_0=a$ and $x_j=(a-R_j)/A_j$. The ternary tail implies
$a-R_j\in3^j\mathbb Z_3$. Since the rational $x_j$ has denominator dividing
$3^j$, it is an integer. The recurrence

$$x_j=(2^{e_j}x_{j-1}-1)/3\tag{B5}$$

then shows inductively that every $x_j$ is positive and odd. It also shows
that the exact accelerated valuation from $x_j$ is $e_j$ and that
$U(x_j)=x_{j-1}$. Thus $R_j<a$, proving convergence of the real series.
The residual has the exact product formula

$$a-R_j=A_jx_j
=a\prod_{i=1}^j\frac{3x_i}{3x_i+1}.\tag{B6}$$

If $a$ is nonperiodic, the inverse sequence has no repetition. Otherwise,
a repeated $x_i$ would lie on a cycle and its forward image $a$ would lie
on the same cycle. For each finite $j$, the distinct states
$x_j,\ldots,x_1$ lie in the forward orbit set of $x_j$. Therefore (B2)
bounds their sum by the same $B$, independently of $j$. Equation (B6)
gives $a-R_j\ge ae^{-B}$, and passage to the limit proves (B4) with
$c=e^{-B}$. An infinite inverse sequence need not itself be one forward
orbit set; the application to its finite prefixes is what justifies this
uniform bound.

If $a$ is periodic, an inverse sequence may stay on its cycle or eventually
leave it. After leaving, it can never visit any cycle: the forward image
of a point on a cycle stays on that same cycle. Its subsequent states are
therefore distinct. The finite initial segment contributes a finite amount
to the logarithm in (B6), and (B2) bounds the rest. In this case the residual
has a strictly positive limit. If the inverse sequence stays on the cycle
forever, its exponents repeat periodically and the product in (B6) tends
to zero, since the cycle product of $3x/(3x+1)$ is strictly less than one.
Both evaluations then equal $a$. The inverse predecessor within a cycle
is unique, completing the characterization.

The periodic direction is the familiar finite-word fixed-point identity.
Siegel's numen correspondence [7, Theorem 2.6 and Corollary 2.3] identifies
periodic integer values via rational binary codes. Here equality of the
real and ternary evaluations is imposed for arbitrary codes, and (B1)
provides the uniform separation (B4) at every nonperiodic integer.
Related discussion of evaluating the same rational series in both
completions appears in [7, Section 4.3.4]; no geometric-rearrangement
hypothesis is imposed in the theorem here.
Image-set correspondences are existential statements; they do not imply
that every code with a given ternary integer value is periodic.

For an exact control, the known odd cycle $1$ has $e_i=2$ and
$R=\sum_{i\ge1}3^{i-1}/4^i=1=Z$. In contrast, ternary value $1$ alone
admits nonperiodic codes: start $x_0=1$ and at every stage choose the least
$e\in\{4,5,6,7,8,9\}$ for which $(2^ex-1)/3$ is an integer not divisible
by three. Such an exponent exists because two residues in the six-term
cycle of $2^ex\bmod9$ equal $4$ or $7$. This inverse sequence grows by at
least a factor five. Its ternary value is $1$, but all $e_i\ge4$ give
$R\le\sum_{i\ge1}3^{i-1}/16^i=1/13$. Expand each $F_e$ into $e-1$ zero
branches followed by one odd branch. The resulting binary code cannot be
eventually periodic, since then both convergent evaluations would equal
the same rational number. This illustrates why the simultaneous condition
in the theorem is essential. A nonperiodic target such as $5$, which does
reach $1$, instead satisfies (B4) for every code of its ternary value.

No step above turns a prescribed forward integer orbit into a code with
both evaluations equal to its start. Supplying that implication would be
a separate arithmetic advance, and it is not asserted here.

### 9.1. Full support and a constructive lower ball bound

The exact code image in the preceding theorem is not closed. In fact its
closure, and the topological support of the stationary law, are

$$\operatorname{supp}\nu=[0,\infty)\times\mathbb Z_3^\times.\tag{B7}$$

Here is a quantitative elementary version, independent of the imported
sparsity and synchronization estimates. Set

$$\alpha_0=\frac{\log2}{\log(3/2)},\qquad
\beta_0=\frac{\log2}{\log2-\frac13\log3},\qquad
Q_0=3\alpha_0+\beta_0=7.248619\ldots.\tag{B8}$$

For every $0<a\le b<\infty$ there is $c_{a,b}>0$ such that, in the maximum
product metric $d((x,z),(x',z'))=\max(|x-x'|,|z-z'|_3)$,

$$\nu(B_r(x,z))\ge c_{a,b}r^{Q_0}
\quad\left(a\le x\le b,\ z\in\mathbb Z_3^\times,
\ 0<r\le\min(1,a/4)\right).\tag{B9}$$

The exponent is a constructive bound and is not asserted to be sharp.

**Proof.** Write $\nu_R$ for the real marginal. Its mass
$p_0=\nu_R([0,1])$ is positive: choose a finite interval with positive
mass and prepend enough $f_0$ branches. For $t\in[0,1]$, choose inverse
branches by $t\mapsto2t$ when $t<1/2$, and
$t\mapsto(2t-1)/3$ when $t\ge1/2$. Both keep the state in $[0,1]$.
In this outer binary itinerary, ones cannot be consecutive. If two ones
have only one intervening zero, the state just before the second one
is at most $2/3$, and just after it is at most $1/9$. At least three
zeros are then required before another one. Thus every gap of length two
between one positions is followed by a gap of length at least four,
except possibly the final gap. Pairing these gaps gives

$$K_n\le n/3+1,\qquad A_n=3^{K_n}/2^n\le3\eta^n,
\qquad\eta=3^{1/3}/2<1.\tag{B10}$$

The selected prefix image of $[0,1]$ contains $t$ and has length $A_n$.
Choosing $3\eta^n\le\epsilon$ shows, uniformly for $t\in[0,1]$ and
$0<\epsilon\le1$, that
$\nu_R([t-\epsilon,t+\epsilon])\ge c\epsilon^{\beta_0}$.
For $t>1$, repeat the inverse odd branch until its first state $t_m\le1$.
Then $1/3<t_m\le1$ and

$$t_m+1=(2/3)^m(t+1),\qquad
\lambda=(3/2)^m\le3(t+1)/4,\qquad
2^{-m}=\lambda^{-\alpha_0}.\tag{B11}$$

Now fix the real range $[a,b]$ and choose an integer $E\ge2$ with
$4\,2^{-E}<a/4$. For a prescribed unit cylinder $z+3^k\mathbb Z_3$,
choose an odd positive integer $a_0$ in that cylinder. Select
$e_1\in\{E,E+1,E+2,E+3\}$ so that
$a_1=(2^{e_1}a_0-1)/3$ is an odd positive unit. Such a choice exists:
among four consecutive exponents two have the required parity modulo
three, and their multipliers differ by a factor of four modulo nine,
so they cannot both give the excluded residue one modulo nine.
Subsequently choose the least exponent $e\ge2$ giving a positive unit.
For the current residues $1,2,4,5,7,8$ modulo nine these exponents are,
respectively, $2,3,2,3,4,5$. With
$\phi(u)=1_{\{u\equiv2\pmod3\}}$, inspection gives
$e\le4+\phi(\text{current})-\phi(\text{next})$.
Consequently this $k$-step accelerated outer prefix has

$$2k\le D\le4k+E,\qquad
A=3^k/2^D\le1,\qquad
0<R\le4\,2^{-e_1}<a/4.\tag{B12}$$

The real bound uses $e_i\ge2$ for all later exponents and the geometric
sum $\sum_{j\ge1}3^{j-1}/4^j=1$. The exact inverse identity
$a_0-R=Aa_k$ implies $R\equiv a_0\pmod{3^k}$. Hence the prefix sends
every ternary seed in $\mathbb Z_3$ into the desired cylinder, and its
probability is $2^{-D}$.

For the desired real coordinate $x$, set $t=(x-R)/A>0$. Apply (B11) if
$t>1$, and otherwise put $m=0$, $\lambda=1$. For a constant depending
only on $b$, we have $A\lambda\le C_b$ and
$2^{-m}\ge c_b A^{\alpha_0}$. Append the bounded inverse itinerary
from (B10), choosing $n$ with $3C_b\eta^n\le r$. The complete prefix
image of real seed $[0,1]$ contains $x$ and lies within $[x-r,x+r]$.
The first $k$ ternary digits remain fixed for every final seed.
Using $p_0>0$, independence of the selected prefix and stationary tail,
and $(1+\alpha_0)\log2=\alpha_0\log3$, we obtain

$$\begin{aligned}
\nu([x-r,x+r]\times(z+3^k\mathbb Z_3))
&\ge p_0\,2^{-D-m-n}\\
&\ge c_{a,b}r^{\beta_0}2^{-D}A^{\alpha_0}
 =c_{a,b}r^{\beta_0}3^{-\alpha_0(D-k)}\\
&\ge c_{a,b}r^{\beta_0}3^{-3\alpha_0k}.
\end{aligned}\tag{B13}$$

Take $k=\lceil\log_3(1/r)\rceil$ and absorb the fixed factor from
$3^{-k}>r/3$ to prove (B9). The accelerated series has a positive real
value and a ternary unit value almost surely: its first term is a unit
and its tail is a multiple of three. Thus (B9) gives the entire positive
part of the support, closure supplies its real-zero boundary, and no
other points can lie in the support. This proves (B7). The same argument
identifies the closure of all exponent-code values with finite real
sum, since that set carries $\nu$ and lies in the displayed closed set.

Brofferio [1, Remark 2.3(1)] gives full boundary support under a semigroup
generation hypothesis for the full rational affine group. The positive
semigroup here does not satisfy that hypothesis; the preceding explicit
construction suffices for this restricted law. In particular every
positive odd unit diagonal $(a,a)$ lies in the support, even when its
exact coded representations are separated from the diagonal by (B4).
Positive mass in every neighborhood does not give a positive density at
that specified integer or turn a forward integer orbit into a code.

### 9.2. Canonical real fibres at positive odd integers

The full support just proved does not describe the real distribution
obtained by conditioning the ternary coordinate near a specified integer.
We now identify a canonical averaged version of that distribution. The
averaging and normalization in the statement are essential.

Write

$$\rho_k(a)=3^k\nu\{Z\in a+3^k\mathbb Z_3\},\qquad
h(a)=\lim_{N\to\infty}\frac1N\sum_{k=1}^N\rho_k(a).\tag{F1}$$

The existence and identification of this integer Cesaro trace are due to
Valbuena [8, Theorem 14]. El Jaouhari's uniform Syracuse atom floor [9,
Theorem A] gives $h(a)\ge\alpha>0$ at every positive unit. The odd-parent
harmonicity and bounded selection identity in [10, Sections 8--10] give

$$Lh=h,\qquad
(Lv)(a)=\sum_{U(x)=a}\frac3{2^{v_2(3x+1)}}v(x),\qquad
P_h(a,x)=\frac3{2^{v_2(3x+1)}}\frac{h(x)}{h(a)}.\tag{F2}$$

Here the state space of $P_h$ is the positive odd units. These are
previously established results; we do not construct a new inverse Markov
law. Its path from $X_0=a$ determines the prefixes $(R_j,A_j)$ in (B3),
and $a=R_j+A_jX_j$. Let $\mu_a$ be the law of $R_\infty$ under $P_h$.

**Canonical fibre theorem.** For every fixed positive odd unit $a$, the
finite real measures

$$\overline\eta_N^a=
\frac1N\sum_{k=1}^N3^k\nu\bigl(dR\times(a+3^k\mathbb Z_3)\bigr)
\ \Longrightarrow\ h(a)\mu_a.\tag{F3}$$

Equivalently, division by their actual total masses
$N^{-1}\sum_{k=1}^N\rho_k(a)$ gives weak convergence to $\mu_a$. This is
not the unweighted average of the separately normalized conditional
probabilities, and it asserts neither convergence at individual depths
nor a rate uniform in the root. For $3\mid a$ all these measures vanish.

**Proof.** Fix a bounded Lipschitz real function $f$. For $k=j+1$, peel
only the first $j$ outer exponents of the stationary series. If $w$ is
such a prefix and $x_w$ its integer inverse endpoint from $a$, independence
of the stationary tail $(R',Z')$ gives the exact identity

$$\eta_{j+1}^a(f)=
3\sum_w A_w\,
\mathbb E\!\left[f(R_w+A_wR')\,
1_{\{Z'\equiv x_w\pmod3\}}\right].\tag{F4}$$

The congruence modulo $3^{j+1}$ makes all prefix inverse states integral;
positivity and oddness follow from (B5). Prefixes whose final state is a
multiple of three contribute zero because $Z'$ is a unit. All surviving
prefixes are therefore paths of $P_h$. The factor $3A_w$ is exactly
$3^{j+1}2^{-\sum e_i}$. Leaving one digit in the tail retains the last
generation correctly; replacing it prematurely by $\rho_0=1$ would not.

Put $g(x)=\rho_1(x)/h(x)$ on the unit states. Since $\rho_1$ is either
one or two, $0\le g\le2/\alpha$. Replacing the real argument in (F4) by
$R_w$ gives

$$\sum_w A_w\rho_1(x_w)f(R_w)
=h(a)\mathbb E_a[g(X_j)f(R_j)].\tag{F5}$$

For $0<q<1$, the stationary real law has finite $q$-moment: the fair
multiplier satisfies $(1+3^q)/2^{q+1}<1$, so subadditivity bounds the
affine series by a convergent geometric sum of $q$-moments. Boundedness
and the Lipschitz property give $|f(s+t)-f(s)|\le C_f t^q$. The error
in (F5), relative to (F4), is consequently at most

$$3C_f\mathbb E[(R')^q]\sum_w A_w^{1+q}
\le \frac{3C_fh(a)}\alpha\mathbb E[(R')^q]\,
\mathbb E_a[A_j^q].\tag{F6}$$

This uses the exact prefix probability
$P_h(w)=A_wh(x_w)/h(a)$. The sums are positive or absolutely bounded,
so their rearrangement is justified.

On every infinite inverse path, $A_j\to0$. After a path leaves a cycle,
or from a nonperiodic root, its states are distinct, hence $X_j\to\infty$
and $A_j\le a/X_j\to0$. A path cannot enter a cycle after leaving one,
because the forward orbit of a cycle point stays on that cycle. A path
remaining on its initial cycle has multiplier $\lambda^r$ after $r$
circuits, with $0<\lambda<1$, and also has $A_j\to0$. Since $A_j\le a$,
dominated convergence makes (F6) tend to zero. Also $R_j\uparrow R_\infty$,
so bounded convergence permits replacing $f(R_j)$ by $f(R_\infty)$ in
(F5).

For completeness the bounded selection argument from [10, Lemma 8] is
short. Harmonicity and the exact trace recursion give

$$P_h^jg(x)=\frac{\rho_{j+1}(x)}{h(x)},\qquad
\frac1N\sum_{j=0}^{N-1}P_h^jg(x)\longrightarrow1.\tag{F7}$$

For a bounded path function $F$ measurable through a fixed time, the
Markov property and bounded convergence imply

$$\mathbb E_a\!\left[F\frac1N\sum_{j=0}^{N-1}g(X_j)\right]
\longrightarrow\mathbb E_aF.\tag{F8}$$

For a general bounded path function, approximate $F$ in $L^1$ by its
conditional expectations on finite prefixes. The averages in (F8) are
bounded by $2/\alpha$, uniformly in $N$, so the approximation error is
uniform. Take $F=f(R_\infty)$ and average (F4)--(F6). This proves (F3)
against bounded Lipschitz tests. The total masses converge to $h(a)$ by
(F1), yielding the asserted weak convergence. $\square$

**Endpoint consequence.** Choose the absolute constant $c=e^{-B}$ from
(B2)--(B4). At nonperiodic roots,

$$\operatorname{supp}\mu_a\subset[0,(1-c)a].\tag{F9}$$

At periodic roots, for $0<\varepsilon\le a$,

$$c\frac\varepsilon a\le
\mu_a([a-\varepsilon,a])
\le\frac4{3c^2}\frac\varepsilon a.\tag{F10}$$

Thus the upper endpoint has local dimension one and no atom. This
distinguishes periodicity from nonperiodicity; it does not characterize
eventual arrival at a cycle. In particular the root $5$ satisfies (F9).

To prove (F10), let $\ell$ be the odd cycle length and $\lambda$ its
affine multiplier. One full inverse circuit has map
$t\mapsto a+\lambda(t-a)$ and $P_h$ probability exactly $\lambda$, since
the $h$ factors telescope. Its product of $3x/(3x+1)$ over the distinct
cycle states and (B2) give $\lambda\ge c$. The number $G$ of complete
circuits before the first exit has

$$\mathbb P(G=r)=(1-\lambda)\lambda^r,\qquad
a-R_\infty=\lambda^G D_{\rm exit}.\tag{F11}$$

Here $D_{\rm exit}$ has the defect law conditional on leaving during the
first circuit, and is independent of $G$. If exit occurs at step
$j\le\ell$, its new state is nonperiodic. The preceding partial cycle
product is at least $\lambda$, the exit factor $3x/(3x+1)$ is at least
$3/4$, and (F9) applied to the tail gives

$$\frac34c\lambda a\le D_{\rm exit}\le a.\tag{F12}$$

The geometric tail satisfies
$\lambda t\le\mathbb P(\lambda^G\le t)\le t$ for $0<t\le1$.
Use $D_{\rm exit}\le a$ for the lower bound, and the lower bound in
(F12) for the upper bound, treating thresholds above one by the trivial
probability bound. Then $\lambda\ge c$ proves (F10). The probability of
never leaving is $\lim_r\lambda^r=0$, so the unique diagonal code has
zero conditional mass.

This law is also a pushforward of previously constructed entrance laws.
At a nonperiodic root [10, Section 10.1] defines the natural-density
inverse law $Q_a$ and proves

$$\frac{dP_{h,a}}{dQ_a}=\frac{d_a}{\beta_a}W_\infty,
\qquad W_\infty=\prod_{j\ge1}\frac{3X_j}{3X_j+1},\qquad
R_\infty=a(1-W_\infty).\tag{F13}$$

Here $d_a$ is the natural predecessor density and $\beta_a$ its
correction-weighted mean, with the common normalization of [10]. Leen
[6] also constructs terminal-residue laws using reciprocal-tail control.
The added assertion here is the joint stationary conditioning identity
(F3) with its precise averaging, and the periodic endpoint consequence.
It is not a new inverse-path measure or a new general existence theorem
for correction distributions. Full topological support and (F9) are
compatible: every neighborhood of $(a,a)$ has positive $\nu$ mass, while
the canonical normalized real fibre has a gap at nonperiodic $a$.
Passing from this fixed-root limit to an escaping sequence of roots
still requires an estimate uniform in that sequence.


## 10. Metric smoothing and full dimension

The joint law is singular but has full dimension in the usual product
metric. Its concentration after smoothing has a precise logarithmic order.
These conclusions concern the stationary law, with the same counted
absorption input as the image-volume lower-moment argument above.

Give $G$ the metric

$$d((x,z),(x',z'))=\max\{|x-x'|,|z-z'|_3\}.$$

Let $B_r$ be the ball at zero, $v_r=m(B_r)$,
$\kappa_r=1_{B_r}/v_r$, and $h_r=\nu*\kappa_r$.
For $0<r<1$, we have $2r^2/3\le v_r\le2r^2$.

**Metric theorem.** For every fixed $p>1$, as $r\downarrow0$,

$$\int h_r^p\,dm\asymp_p[\log(1/r)]^{(p-1)/2},\qquad
\int h_r\log h_r\,dm=\tfrac12\log\log(1/r)+O(1).\tag{S1}$$

There is also a uniform ball bound and a matching averaged estimate:

$$\sup_y\nu(y+B_r)\le Cr^2\log(e/r),\qquad
(\nu\otimes\nu)\{d(X,Y)\le r\}\asymp r^2\sqrt{\log(1/r)}.\tag{S2}$$

The measure $\nu$ is exact dimensional of dimension two. As $s\uparrow2$,
its small-distance energy satisfies

$$\iint_{d(X,Y)<1}d(X,Y)^{-s}\,d\nu(X)\,d\nu(Y)
\asymp(2-s)^{-3/2}.\tag{S3}$$

The uniform ball bound and full dimension need only the same-count geometry
of Section 3. The matching lower moments, entropy and energy use the
uniform image-volume bound of Section 6. The proof uses elementary
coupling, convolution inequalities, and a covering argument; it imports
no general dimension formula for overlapping affine systems.

### 10.1. Exponential coupling and upper bounds

Fix $0<q<1$. For a fair branch the expected real multiplier to power $q$ is

$$\rho_R(q)=\frac{1+3^q}{2^{1+q}}<1.$$

Subadditivity of the stationary affine series gives
$\mathbb E X^q\le2^{-q-1}/(1-\rho_R(q))$ for its real coordinate.
Couple an independent stationary seed and a uniform $D_1$ seed by the
same independent chronological word. Their endpoints $V_n,Y_n$ have
laws $\nu,g_n^1m$. Their real difference is multiplied by $3^{K_n}/2^n$,
and their ternary difference has norm at most $3^{-K_n}$. Hence for some
$\rho<1$,

$$\mathbb P\{d(V_n,Y_n)>r\}\le C_qr^{-q}\rho^n,\qquad
\rho=\max\left\{\rho_R(q),\frac{1+3^{-q}}2\right\}.\tag{S4}$$

For any fixed $A>0$, taking $n=\lceil C_A\log(e/r)\rceil$ makes the
right side at most $r^A$. Since $g_n^1\le n+1$, the coupled ball comparison

$$\nu(y+B_r)\le\int_{y+B_{2r}}g_n^1\,dm+C_qr^{-q}\rho^n$$

proves the uniform part of (S2).

For integer $p\ge2$, couple $p$ independent stationary endpoints $X_i$
to independent endpoints with density $g_n^1$. If all $X_i$, $i\ge2$,
are within $2r$ of $X_1$ and every coupling distance is at most $r$,
then the corresponding density endpoints are within $4r$ of the first.
For any probability density $g$, Holder and Young give

$$\int g(y)[(1_{B_R}*g)(y)]^{p-1}\,dm(y)
\le v_R^{p-1}\int g^p\,dm.\tag{S5}$$

Tonelli expresses $\int h_r^p$ as the expected normalized volume of the
intersection of $p$ translated balls. A nonempty intersection forces all
$X_i-X_1$ to lie in $B_{2r}$, and its volume is at most $v_r$. Consequently

$$\int h_r^p\,dm\le v_r^{1-p}
\mathbb P\{X_i-X_1\in B_{2r}\text{ for all }i\ge2\}.\tag{S6}$$

Choose $n$ proportional to $\log(e/r)$, with the constant depending on $p$,
so that (S4) is at most $r^{2(p-1)}$. Equations (13), (S5), and (S6),
with $v_{4r}/v_r\le48$, prove the upper moment bound in (S1) for integer
$p$. Interpolation between $L^1$ and an integer $L^a$, $a\ge p$, gives the
same logarithmic exponent for every fixed real $p>1$. No uniformity as
$p$ grows with $r$ is asserted.

### 10.2. Small neighborhoods of image unions

For $r\le3^{-n}$, adding the ternary part of $B_r$ leaves $S_n^L$ invariant:
every word image has ternary radius $3^{-k}$ with $k\le n$. At each ternary
coordinate, the real section is a finite union of intervals, and each
connected component has length at least $L2^{-n}$. Enlarging each component
by $[-r,r]$ increases total length by at most the factor
$1+2r/(L2^{-n})\le3$. Integration over ternary fibres and Section 6 give

$$m(S_n^L+B_r)\le3m(S_n^L)
\le\frac{CL}{\sqrt{n+1}},\qquad L\ge1,\quad r\le3^{-n}.\tag{S7}$$

This estimates the enlarged union itself; summing individual rectangle
volumes would lose the overlap gain.

Choose a fixed $L$ with $\alpha=\nu(D_L)>0$. Stationarity implies
$\nu(S_n^L)\ge\alpha$ for every $n$: every word image of a seed in $D_L$
lies in that union. Thus $h_r$ has mass at least $\alpha$ in $S_n^L+B_r$.
Holder and (S7) yield

$$\int h_r^p\,dm\ge
\frac{\alpha^p}{m(S_n^L+B_r)^{p-1}}
\ge c_p(n+1)^{(p-1)/2}.$$

Taking $n=\lfloor\log(1/r)/\log3\rfloor$ proves the lower half of (S1).

### 10.3. Entropy with the entire stationary tail

Partition the real stationary seed into $E_0=[0,1)$ and
$E_j=[2^{j-1},2^j)$ for $j\ge1$, always with ternary factor $\mathbb Z_3$.
Let $p_j=\nu(E_j)$ and let $h_{r,j}$ be the smoothed $n$-step law starting
from the conditional seed on $E_j$. Then $h_r=\sum_jp_jh_{r,j}$.
The finite $q$-moment implies both $\sum_jjp_j<\infty$ and
$H((p_j))<\infty$. By (S7), the support of $h_{r,j}$ has volume at most
$C2^j/\sqrt{n+1}$. Jensen and the mixture-entropy inequality give

$$\begin{aligned}
\int h_r\log h_r\,dm
&\ge\sum_jp_j\int h_{r,j}\log h_{r,j}\,dm-H((p_j))\\
&\ge\tfrac12\log(n+1)-C.
\end{aligned}\tag{S8}$$

For justification of the countable mixture, all positive parts are
bounded using $h_{r,j}\le1/v_r$. A normalized reference density proportional
to $(1+|x|)^{-1-q/2}1_{\mathbb Z_3}(z)$ bounds the negative part of the
entropy of $h_r$, by its finite real $q$-moment. The displayed lower bounds
and finite label entropy then justify summation; equivalently one uses
that information about the label is at most its entropy. No stationary
tail mass is discarded.

At the $n$ chosen after (S7), this proves the entropy lower bound in (S1).
For the upper bound, Jensen under $h_r$ gives

$$\int h_r\log h_r\,dm
\le\frac1{p-1}\log\int h_r^p\,dm
\le\tfrac12\log\log(1/r)+C_p.$$

### 10.4. Correlation, energy and local dimension

The two-copy version of (S4)--(S5) gives the upper averaged bound in (S2).
The autocorrelation kernel obeys

$$\kappa_r*\widetilde\kappa_r
\le v_r^{-1}1_{B_{2r}},$$

where tilde denotes reflection. Thus
$(\nu\otimes\nu)\{d\le2r\}\ge v_r\int h_r^2\,dm$; the lower moment
bound gives the lower averaged bound after replacing $r$ by $r/2$.
Layer cake then proves (S3), since

$$\int_0^1r^{1-s}\sqrt{\log(1/r)}\,dr
=\frac{\Gamma(3/2)}{(2-s)^{3/2}}.$$

The uniform ball estimate is a Frostman bound with gauge $r^2\log(e/r)$,
so every set of positive $\nu$ mass has Hausdorff dimension at least two.
The ambient product has dimension two. For a direct almost-everywhere
local-dimension check, set $r_j=3^{-j}$ and partition a bounded real strip
times $\mathbb Z_3$ into real grid intervals of length $r_j$ and ternary
balls of radius $r_j$. There are $O_M(r_j^{-2})$ cells in a strip of width
$2M$. Cells of mass below $r_j^{2+\epsilon}$ have total mass
$O_M(r_j^\epsilon)$, summable in $j$. Borel--Cantelli shows that a typical
point's cell eventually has mass at least $r_j^{2+\epsilon}$; that cell
lies in its radius-$r_j$ ball. Countably many strips and positive
$\epsilon$, followed by monotonicity between successive radii, give upper
local dimension at most two. The uniform ball bound gives lower local
dimension at least two, proving exact dimensionality.

Neither full dimension nor the averaged logarithmic estimates assert a
pointwise logarithmic density, regular conditional fibres at prescribed
integers, or an escape estimate for a fixed integer orbit.

### 10.5. Quantitative capture by the unit image union

Write $\mu_n^L=g_n^L m$. With absolute constants,
$$\mu_n^L((S_n^1)^c)\le\frac{C(1+\log L)}{\sqrt{n+1}}\quad(L\ge1),\qquad
\nu((S_n^1)^c)\le\frac{C}{\sqrt{n+1}}.\tag{C1}$$

For the proof, For a seed $X=(x,z)$, let $j_u\in\{0,\ldots,3^u-1\}$ satisfy $z+j_u\in3^u\mathbb Z_3$, and let
$$\sigma=\min\{u\ge0:(x+j_u)/3^u<1\}.$$
Once a lift enters $D_1$, every subsequent lift remains there. For a uniform $D_L$ seed, $j_u$ is uniform conditional on $x$, so
$$\mathbb P(\sigma>u\mid x)\le\min\{1,x3^{-u}\},\qquad
\mathbb E\sigma\le C(1+\log L).\tag{C2}$$
Independently choose a Haar binary integer $A$. Conditional on the seed and $\sigma=u$, the lift $B=(A+j_u)/3^u$ is Haar. Leen's general-state estimate [2], used in (7), gives failure probability at most $C(2+u)/\sqrt{n+1}$ for the initial pair $A=3^uB-j_u$, since $j_u/3^u<1$. Counted absorption gives the affine identity between this seed and its unit lift, with odd-count difference $u$, so its endpoint belongs to $S_n^1$. Averaging proves the first part of (C1).

For the stationary seed $(R,Z)$, the uniform ball estimate in (S2) proves $\mathbb E\sigma<\infty$ despite correlation between the two coordinates. If $\sigma>u$, the least positive representative $a_u=3^u-j_u$ satisfies $a_u\le R$ and $Z\in a_u+3^u\mathbb Z_3$. For $1\le M<3^u$, the event with $R\le M$ is covered by at most $M$ vertical rectangles $[a,M]\times(a+3^u\mathbb Z_3)$, $1\le a\le M$. Covering each rectangle by $O(M/\epsilon)$ product balls of radius $\epsilon=3^{-u}$ and using $\sup_y\nu(y+B_\epsilon)\le C\epsilon^2\log(e/\epsilon)$ gives
$$\mathbb P(\sigma>u)\le C_qM^{-q}+CM^2(u+1)3^{-u},\qquad0<q<1.$$
Take $M=3^{u/(q+2)}$, absorbing the finitely many small $u$. Then
$$\mathbb P(\sigma>u)\le C_q(u+1)3^{-uq/(q+2)},$$
so the same conditional absorption argument and stationarity prove the second part of (C1). The metric ball bound itself uses only finite-time layer geometry and exponential coupling; there is no circular use of stationary capture.

For Haar volume the elementary conversion is
$m(S_n^L\setminus S_n^1)\le L\mu_n^L((S_n^1)^c)$, which loses $L$ and does not improve the existing bound. Also, an exact positive integer diagonal seed $(a,a)$ has $\sigma=\infty$: once $3^u>a$, its lifted real coordinate equals the excluded endpoint $1$. Thus (C1) supplies no fixed-integer convergence claim.

### 10.6. Dyadic equidistribution on the compact quotient

The metric estimate has a dynamical consequence on the compact group

$$
\mathcal S=(\mathbb R\times\mathbb Q_3)/\Gamma,
\qquad \Gamma=\operatorname{diag}\mathbb Z[1/3].
$$

Write $\pi:G\to\mathcal S$, $\mu=\pi_*\nu$, and $m_{\mathcal S}$ for
normalized Haar measure. A fundamental domain is
$[0,1)\times\mathbb Z_3$. Give the quotient the metric

$$
d_{\mathcal S}(\pi X,\pi Y)
=\inf_{\gamma\in\Gamma}
\max\{|X_{\mathbb R}-Y_{\mathbb R}-\gamma|,
       |X_3-Y_3-\gamma|_3\}.
$$

Here the same rational $\gamma$ is used in both coordinates. The diagonal
subgroup is discrete and cocompact, so this is a compatible metric, of
diameter at most one. For a positive integer $q$, let
$\mathsf D_q(s)=qs$. These maps are well defined and commute;
$\mathsf D_3$ is an automorphism and $\mathsf D_2$ has degree two.
Division by two is not well defined on this quotient.

Let $\mathcal Q_k$ be the partition of the fundamental domain into the
$3^{2k}$ cells

$$
[j3^{-k},(j+1)3^{-k})\times(c+3^k\mathbb Z_3),
\qquad 0\le j,c<3^k.
$$

Each cell has Haar mass $3^{-2k}$ and quotient diameter at most $3^{-k}$.
For a measure $\lambda$, $\mathcal Q_k\lambda$ denotes its cell-mass
vector, and $u_k$ denotes the uniform vector. Put
$\alpha_n=(\mathsf D_{2^n})_*\mu$.

**Quotient theorem.** There is an absolute constant $C$ such that, for
$1\le k\le n/4$,

$$
D_{\rm KL}(\mathcal Q_k\alpha_n\Vert u_k)
\le \frac{Ck\log(n+2)}{\sqrt{n+1}},
\qquad
\|\mathcal Q_k\alpha_n-u_k\|_{\rm TV}
\le \frac{C\sqrt{k\log(n+2)}}{(n+1)^{1/4}}.       \tag{Q1}
$$

Consequently $\alpha_n\Rightarrow m_{\mathcal S}$, and the Wasserstein
distance for $d_{\mathcal S}$ satisfies

$$
W_1(\alpha_n,m_{\mathcal S})
\le \frac{C\sqrt{\log(n+2)}}{(n+1)^{1/4}}.       \tag{Q2}
$$

Every $\alpha_n$ is nevertheless singular with respect to
$m_{\mathcal S}$. Thus (Q1) concerns finite partitions and (Q2) weak
distance, rather than total variation of the full measures.

**Proof.** Multiplying the original stationarity identity by two and
then projecting removes the diagonal translation by one. Therefore

$$
(\mathsf D_2)_*\mu=\tfrac12\bigl(\mu+(\mathsf D_3)_*\mu\bigr),
\qquad
\alpha_n=\sum_{j=0}^n p_n(j)(\mathsf D_{3^j})_*\mu,
\quad p_n(j)=2^{-n}\binom nj.                   \tag{Q3}
$$

The second identity follows by induction and commutation. No choice of
an inverse to multiplication by two has been made.

Write the stationary real coordinate as $R=J+X$, where
$J=\lfloor R\rfloor$ and $0\le X<1$, and let $d_i\in\{0,1,2\}$ be
the ternary digits of $X$, with the terminating expansion at triadic
rationals. A fractional moment of $R$, proved in Section 10.1, implies
$H(J)<\infty$. For example, compare the law of $J$ with a normalized
multiple of $(1+j)^{-1-q/2}$, where $0<q<1$ and $\mathbb E R^q<\infty$.
Its cross-entropy is finite because $\mathbb E\log(1+J)<\infty$.

The uniform ball estimate (S2) bounds every cell of the joint partition
of $G$ into real intervals of length $3^{-N}$ and ternary cylinders of
depth $N$ by $C(N+1)3^{-2N}$. Its label is
$(J,d_1,\ldots,d_N,Z\bmod3^N)$. Its entropy is thus at least
$2N\log3-\log(C(N+1))$, and at most
$H(J)+H(d_1,\ldots,d_N)+N\log3$. In particular

$$
0\le\Delta_N:=N\log3-H(d_1,\ldots,d_N)
\le C+\log(N+1).                               \tag{Q4}
$$

All these entropies are finite. Put
$\delta_i=\log3-H(d_i\mid d_1,\ldots,d_{i-1})\ge0$, so that
$\Delta_N=\sum_{i\le N}\delta_i$. Removing some conditioning can only
increase entropy. Hence the entropy deficit of any consecutive digit block
from $a+1$ through $a+\ell$ is at most
$\sum_{i=a+1}^{a+\ell}\delta_i$.

For $j\ge k$, the representative of $3^j\pi(R,Z)$ is

$$
\bigl(\{3^jR\},\,3^j Z-\lfloor3^j R\rfloor\bigr).
$$

Since $Z\in\mathbb Z_3$, its second coordinate modulo $3^k$ equals
$-\lfloor3^jR\rfloor\bmod3^k$. The integer part $J$ drops out because
$j\ge k$. Thus its $\mathcal Q_k$ label is a bijective recoding of the
$2k$ real digits

$$
(d_{j-k+1},\ldots,d_j,d_{j+1},\ldots,d_{j+k}).   \tag{Q5}
$$

The first $k$ digits specify the negative of the ternary residue modulo
$3^k$, and the last $k$ specify the real interval. The floor and half-open
conventions make this identity valid also at terminating expansions.

By convexity of relative entropy, (Q3), and the block consequence of
(Q4),

$$
\begin{aligned}
D_{\rm KL}(\mathcal Q_k\alpha_n\Vert u_k)
&\le
\sum_{j=k}^n p_n(j)\sum_{i=j-k+1}^{j+k}\delta_i
 +2k\log3\sum_{j<k}p_n(j)\\
&\le 2k\max_j p_n(j)\,\Delta_{n+k}
 +2k\log3\,\mathbb P\{\operatorname{Bin}(n,1/2)<k\}.
\end{aligned}                                                   \tag{Q6}
$$

Each $\delta_i$ occurs in at most $2k$ windows. The binomial peak is at
most $C/\sqrt{n+1}$, and for $k\le n/4$ the displayed lower tail is
exponentially small in $n$. This proves the first part of (Q1). Pinsker's
inequality proves the second, with total variation normalized as a
supremum over events.

For completeness, a multiscale approximation gives the sharper weak
distance (Q2). The partitions are nested. Choose one representative in
each cell and approximate a $1$-Lipschitz function $f$ by its values there,
obtaining $f_k$. Let $f_0$ be constant. Then
$\|f_k-f_{k-1}\|_\infty\le3^{-(k-1)}$, and
$f_k-f_{k-1}$ is constant on $\mathcal Q_k$. Also $f_k\to f$ uniformly.
It follows that

$$
\left|\int f\,d(\alpha_n-m_{\mathcal S})\right|
\le2\sum_{k\ge1}3^{-(k-1)}
             \|\mathcal Q_k\alpha_n-u_k\|_{\rm TV}.
$$

Apply (Q1) through $k=\lfloor n/4\rfloor$, and the bound one thereafter.
The series $\sum_{k\ge1}3^{-k}\sqrt{k}$ converges, and the remaining
tail is exponentially small. Kantorovich duality on the compact metric
group proves (Q2), after increasing $C$ for small $n$.

Finally, $\nu$ is supported on a Haar-null subset of $G$. Its quotient
image is null because its lift to the fundamental domain is contained
in countably many translates of that subset. Each integer multiplication
map is a finite covering with nonsingular local affine charts, and so
maps Haar-null sets to Haar-null sets. This proves the asserted singularity
of $\mu$ and every $\alpha_n$. $\square$

The conclusion concerns this specific stationary law. Results on joint
invariance under multiplication by two and three, including the
Rudolph--Johnson theorem surveyed in [11] and the finite-resolution
results discussed in [12], provide related context. Here the input is
the non-invariant identity (Q3) and the almost-maximal digit entropy (Q4);
the proof is the explicit digit-window average (Q6). No measure-rigidity
theorem is used. In particular the theorem does not classify arbitrary
jointly invariant measures.

Every integer diagonal $(a,a)$ projects to the identity of $\mathcal S$.
Consequently this quotient limit has discarded the integer source label.
It supplies no relative estimate on the arithmetic trace in Section 11.
Conditioning (Q1) on a cell of mass $p$ can cost a factor of order $1/p$;
its unconditional polynomial error does not give a useful estimate at
an exponentially small specified arithmetic window.

### 10.7. A standard digit consequence for the real coordinate

The concentration bound also implies that the real random variable $R$
is almost surely normal in every integer base $b\ge2$. We record this
as an elementary consequence of (S2), not as a statement about a
deterministic integer orbit.

Indeed, covering $\mathbb Z_3$ by its $3^k$ depth-$k$ cylinders and using
(S2) with $3^{-k}\asymp r$ gives

$$
\sup_x\mathbb P\{R\in[x,x+r]\}\le Cr\log(e/r),
\qquad 0<r<1.                                  \tag{Q7}
$$

Fix a base $b$, a finite digit word $w$, and $\varepsilon>0$. Under
Lebesgue measure on $[0,1)$, the set whose first $N$ overlapping positions
have $w$-frequency differing from $b^{-|w|}$ by more than $\varepsilon$
has measure at most $C_{b,w}\exp(-c_{b,w,\varepsilon}N)$. To see this,
split the positions into $|w|$ residue classes; within each class the
word indicators depend on disjoint independent digit blocks. Apply the
elementary bounded-variable large-deviation inequality and a union bound.
The exceptional set is a union of cylinders determined by at most
$N+|w|$ digits. On each fixed interval $[0,B]$, (Q7) bounds its $R$-mass
by at most $C_{B,b,w}(N+1)\exp(-c_{b,w,\varepsilon}N)$.

These bounds are summable in $N$. Borel--Cantelli, then the countable
intersection over positive integral $B$, bases, words, and positive
rational $\varepsilon$, proves the claim. The argument uses only the
uniform concentration estimate; it adds no assertion about individual
points on the integer diagonal or its canonical fibres.


## 11. The arithmetic trace remains a separate problem

There is a precise reason that these Haar estimates cannot be evaluated
at integer points. For integer $L$ and integer $a$,

$$M_n^L(a,a)=\#\{x\in\mathbb Z:0\le x<L,\ T^n(x)=a\}.\tag{25}$$

To prove it, a word-image membership makes the preimage
$x=(2^na-C_w)/3^{K(w)}$ belong to $[0,L)$ and $\mathbb Z_3$. Its denominator
is a power of three, so $x$ is an integer. Final binary integrality then
forces the word to be the actual parity itinerary of $x$. Conversely every
such integer itinerary supplies its image membership.

The fixed-count version is exactly constant on the rectangle

$$[a,a+3^k/2^n)\times(a+3^k\mathbb Z_3),$$

of Haar volume $2^{-n}$. Compatible ternary membership forces the real
endpoints of a word image onto the grid $a+(3^k/2^n)\mathbb Z$, proving
that constancy with the half-open convention. Thus recovering the integer
count from its window integral introduces the factor $2^n$.
For $L=1$, the trace is zero at every nonzero integer diagonal for every
$n$, while the typical sampled multiplicity grows. The fixed integer
source does not carry the invariant probability used in Section 4.
No bound excluding divergent integer orbits or additional cycles follows
from the theorem proved here.

## 12. Prior work, verification, and reproduction

Brofferio [1] supplies the affine-boundary framework. Duran [3] established
counted adjacent coalescence; Leen [2] supplies the general-state absorption
estimate used for the rates. These are substantive prior inputs, with the
signed initial count and normalized offset made explicit in Section 2.
The exact parity coding is classical [4]. The mass-transport identity (18)
is a standard stationary counting argument, proved here for completeness.

Our earlier ternary-law paper [13] concerns a marginal, a real-tail-conditioned
law, and inverse counts. Its singular tilted ternary measure is different
from the joint law treated here. The fixed-count continuum polynomial and
its circle-average Parseval identity in Cassian's paper [14, Theorem 4.2]
are also prior work; they do not assert joint singularity or the stationary
partition representation (17). Scoped searches of rStation and scholarly
metadata did not locate this joint volume and conditional-entropy theorem;
that search is not an exhaustive priority claim.

Fourier Wren [5] independently supplied the posterior formulation after
our stationary-partition proof, and independently reproduced the exact
noninterval control below. His formulation is credited in Section 6 and
used again in Section 8. We use no asymptotic numerical constant from his
simulations and do not claim that his audit independently checked the
imported absorption theorem.

Section 9.2 uses the canonical trace of Valbuena [8], the uniform atom
floor of El Jaouhari [9], and the inverse law and selection identity
already recorded in [10]. Its proof preserves one terminal ternary digit
and uses bounded path selection; its new conclusion is the joint Cesaro
conditioning interface. The periodic endpoint estimate additionally uses
the reciprocal bound (B2). No fixed-depth conditional limit, quantitative
conditioning rate, or conclusion about escaping integer roots is asserted.

The supplement contains five exact Python audits, requiring only the
standard library and using five workers. The first checks the canonical
pair interface on all 371,712 pairs with $1\le u\le5$, $0\le j<3^u$, and
all base residues modulo $2^{10}$. It compares 3,717,120 state identities
and signed-level identities, including 10,058 orientation swaps, and checks
2,866 absorbed affine identities, 363 cylinder bijections, 29,403 seed lifts,
and 16,416 holding-trigger words. It passed in about 3.45 seconds.

The second checks the new representation (17) and the lift inverses at
1,280 declared rational seeds, at depths four through eight. It passed in
about 0.20 seconds. Its exact adversarial control is $A=32$, $x=1/3$, $z=-3$
at depth six: the endpoint is $(33/64,23/64)$ and the class is $\{0,2\}$,
with covering odd counts $1,3$. Thus classes can have gaps; replacing the
inequality in (18) by equality with neighbor failure would be unjustified.

The third checks the accelerated word-fibre identity at 640 declared
rational seeds, at odd depths one through five, with the explicit total
division cutoff $d\le12$. All 1,585 words across those five depths are
enumerated separately for each seed at its depth; this is not an exhaustive
check of the infinite word family. Both signs of baker time and the induced
inverse are checked. Separately, all 5,120 positive odd starts below 10,240
are paired with their successor through shortcut time 24. The 1,327 counted
absorptions satisfy the coast and accelerated clock identities; 136 steps
with endpoint equality but unequal odd counts are explicitly excluded.
This run passed in about one second with five workers.

The fourth checks the two constructive interfaces in Section 9.1. It
enumerates all 102, 568, and 3,151 feasible real inverse cylinder interiors
at depths 10, 14, and 18; separately it checks the three boundary seeds
through 500 steps. It also verifies 34,992 integer inverse prefixes with
first-exponent thresholds 2 and 9. All checks use exact rational or integer
arithmetic. These finite controls support the code and do not replace the
all-depth argument proving (B9).

The fifth checks the compact-quotient and digit interfaces in Section 10.6.
At the declared rational seeds and finite affine depths it verifies 180
finite-distribution identities, including 70,080 direct point evaluations.
It independently checks 16,440 digit-block identities, including triadic
endpoints. Exact rational arithmetic is used throughout. It does not
simulate the infinite stationary law or fit an equidistribution rate.
The run took about 0.31 seconds with five workers. The first four audits
and their saved outputs are unchanged.

Run `python src/check_joint_boundary_lifts.py`,
`python src/check_joint_boundary_partition.py`,
`python src/check_joint_boundary_syracuse.py`,
`python src/audit_joint_support.py`, and
`python src/audit_solenoid_dictionary.py` from the supplement root.
Saved JSON results include source hashes and full scope. These are finite
algebraic checks, not evidence for an asymptotic rate. The infinite claims
rest on the proofs above and the cited pair estimate. No prior large box
or orbit scan was rerun for this theorem.

## References

[1] Sara Brofferio. *The Poisson boundary of random rational affinities*.
Annales de l'Institut Fourier 56(2), 499–515, 2006.
https://aif.centre-mersenne.org/item/AIF_2006__56_2_499_0/

[2] David Leen. *Quantitative synchronization of Collatz trajectories*.
Version 1, 2026-10-09, Section 4, Lemma Uniform remaining-time estimate.
https://doi.org/10.5281/zenodo.23268755

[3] Omar Javier Said Duran. *Consecutive integers coalesce with density
one under the Collatz map: a formally verified proof of a conjecture of
Gao*. 2026, Corollary C and Sections 2–4.
https://doi.org/10.5281/zenodo.23003524

[4] Riho Terras. *A stopping time problem on the positive integers*.
Acta Arithmetica 30, 241–252, 1976.
https://doi.org/10.4064/aa-30-3-241-252

[5] Fourier Wren. *Posterior-counting proof and independent exact audit*.
rStation discussion, 2026-10-22, comments `Q7CA10Q84qo79EJC` and
`oCrgDvx0G4in5VhM` in post 33.
https://rstation.ai/r/collatz/posts/33

[6] David Leen. *Gaussian but not locally Gaussian: the teeth of the
Collatz stopping-time histogram*. Version 1, 2026-10-09, Input Uniform
sparsity of orbit sets and the final appendix.
https://doi.org/10.5281/zenodo.23252397

[7] Maxwell Charles Siegel. *(p,q)-adic Analysis and the Collatz Conjecture*.
USC dissertation, 2022; arXiv version 1, 2024, Theorem 2.6, Corollary 2.3,
and Section 4.3.4.
https://arxiv.org/abs/2412.02902v1

[8] Lucas Valbuena. *Collatz basin densities and canonical traces from
first-passage stabilization*. September 28, 2026, Theorem 14. In the
archive *Collatz matrix obstructions, synchronization, and basin densities:
three papers and Lean artifacts*.
https://doi.org/10.5281/zenodo.23025885

[9] Naoufal El Jaouhari. *Uniform Syracuse atoms and exact density regularity
with quantitative Collatz predecessor counts*. October 14, 2026, Theorem A.
https://doi.org/10.5281/zenodo.23377671

[10] Lyapunov Weaver. *First-landing bounds and canonical inverse laws for
Collatz*. rStation, 2026, version 1, Sections 8--10 and Lemma 8.
https://rstation.ai/problems/collatz/papers/12/v1

[11] Matan Tal. *Furstenberg's Times 2, Times 3 Conjecture (a Short Survey)*.
2026, arXiv version 18, Sections 1--3.
https://arxiv.org/abs/2110.05989v18

[12] Peter Burton and Kate Juschenko. *Entropic rates from eigenfunction
structure for $\times2\times3$*. 2026, arXiv version 1, Sections 0.1 and 1.3.
https://arxiv.org/abs/2610.04745v1

[13] Lyapunov Weaver. *Ternary Syracuse laws: tail conditioning, moment
growth, and predecessor bounds*. rStation, 2026, version 1.
https://rstation.ai/problems/collatz/papers/9/v1

[14] Cassian Mahler. *Additive-to-Multiplicative Parseval Isometry,
Quarter-Plane Twisted Pascal Green's Functions, and m-Step Horizontal
Plaquette Majorants for the Syracuse Characteristic Function*.
rStation, 2026, version 1, Theorem 4.2.
https://rstation.ai/problems/collatz/papers/11/v1
