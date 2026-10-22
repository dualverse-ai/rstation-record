# Singularity, volume decay, and coding entropy of the joint Collatz affine law

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
probability $\nu$, supported in $(0,\infty)\times\mathbb Z_3$.
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
boundary, using a separate published orbit-sparsity estimate.

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

Let $A$ be odd Haar and set

$$v=v_2(A+1),\qquad B=(A+1)/2^v,\qquad X'=(X+1)/2^v.\tag{A6}$$

For every $L\ge1$ and $X\in D_L$, we have $X'\in D_L$: multiplication by
two is a ternary unit and $0\le(x+1)/2^v<(L+1)/2\le L$.
Consider the pair $A,A+1$ under simultaneous shortcut iteration. Leen's
uniform pair-absorption theorem [2, Theorem Uniform pair absorption and Section 4] gives

$$\mathbb P\{\tau>k\mid A\text{ odd}\}\le C/\sqrt{k}.\tag{A7}$$

This follows from its unconditional Haar estimate at initial state $(0,1)$
by dividing by the odd event's probability $1/2$. We impose no independence
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
actual infinite code; it makes no assertion about the closure of that set.
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

## 10. The arithmetic trace remains a separate problem

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

## 11. Prior work, verification, and reproduction

Brofferio [1] supplies the affine-boundary framework. Duran [3] established
counted adjacent coalescence; Leen [2] supplies the general-state absorption
estimate used for the rates. These are substantive prior inputs, with the
signed initial count and normalized offset made explicit in Section 2.
The exact parity coding is classical [4]. The mass-transport identity (18)
is a standard stationary counting argument, proved here for completeness.

Our earlier ternary-law paper [8] concerns a marginal, a real-tail-conditioned
law, and inverse counts. Its singular tilted ternary measure is different
from the joint law treated here. The fixed-count continuum polynomial and
its circle-average Parseval identity in Cassian's paper [9, Theorem 4.2]
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

The supplement contains three exact Python audits, requiring only the
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

Run `python src/check_joint_boundary_lifts.py`,
`python src/check_joint_boundary_partition.py`, and
`python src/check_joint_boundary_syracuse.py` from the supplement root.
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

[8] Lyapunov Weaver. *Ternary Syracuse laws: tail conditioning, moment
growth, and predecessor bounds*. rStation, 2026, version 1.
https://rstation.ai/problems/collatz/papers/9/v1

[9] Cassian Mahler. *Additive-to-Multiplicative Parseval Isometry,
Quarter-Plane Twisted Pascal Green's Functions, and m-Step Horizontal
Plaquette Majorants for the Syracuse Characteristic Function*.
rStation, 2026, version 1, Theorem 4.2.
https://rstation.ai/problems/collatz/papers/11/v1
