# The full ballot rate for Collatz inverse survival

Lyapunov Weaver. 18 November 2026. Author manuscript, not yet reviewed.

## 1. Result and relation to prior work

For the odd Collatz map
$$
U(x)=\frac{3x+1}{2^{v_2(3x+1)}},
$$
let $\mathcal I_L$ and $\mathcal I_L^{\mathrm{strict}}$ be the asymptotic and strict all-prefix inverse-minimal valuation-word families of [1, Definition 1.2]. Both require expanding forward prefixes. The asymptotic condition excludes smaller predecessors, at every prefix endpoint and every inverse depth up to that prefix length, for all sufficiently large sources in the cylinder. The strict condition requires this for every positive source in the cylinder. We recall the precise definitions in Section 2. A word of division total $S$ has normalized odd $2$-adic Haar weight $2^{-S}$.

Put
$$
\vartheta=\log_2 3,\qquad
u_* =1-\frac1\vartheta,\qquad
\lambda_*=(\vartheta-1)
 \left(\frac{2(\vartheta-1)}{\vartheta}\right)^{-\vartheta}
=0.9465045768325841\ldots,
$$
and $F(L)=L^{2/3}\log^{1/3}(L+2)$. All unlabelled logarithms are natural.

**Theorem 1 (the full ballot rate).** There are absolute positive constants $c,C$ such that, for every sufficiently large $L$, there is a family $\mathcal J_L\subseteq\mathcal I_L^{\mathrm{strict}}$ satisfying
$$
\mu_2(\mathcal J_L)\ge\lambda_*^L\exp\{-CF(L)\},
\qquad
\|w\|\le\vartheta L-cF(L)\quad(w\in\mathcal J_L).       \tag{1}
$$
Consequently both limits exist and
$$
\lim_{L\to\infty}\mu_2(\mathcal I_L^{\mathrm{strict}})^{1/L}
=\lim_{L\to\infty}\mu_2(\mathcal I_L)^{1/L}
=\lambda_*.                                             \tag{2}
$$
For every fixed $0<u<u_*$, there are positive $c_u,C_u$ such that
$$
\mu_2(\mathcal I_L)\ge c_u\Lambda(u)^L(L+2)^{-C_u},
\qquad
\Lambda(u)=\frac{u}{1-u}(2u)^{-1/(1-u)}.                  \tag{3}
$$

The previously published unconditional interval was a lower bound $0.751095$ and the upper bound $\lambda_*$ [1, Theorem 2]. The upper bound is the classical terminal ballot Chernoff bound. We match it for both survival families. Subsequent work [2,3,4] develops predecessor-renewal, pullback and Fourier methods, with stronger survival bounds conditional on renewal decay. Our argument establishes the full-alphabet rate without assuming or proving that decay. It does not settle the binary-alphabet rate. The selected words do not form a shift-invariant subshift, so the shift-invariant obstruction in [3] is respected.

There is also an actual integer consequence at the same horizon as [1, (3.9)]. Set
$$
L(X)=\lfloor\log_3X\rfloor,\qquad
\beta=1+\log_3\lambda_*=0.9499555271883306\ldots.
$$
For all sufficiently large $X$,
$$
\#\left\{x\in[X/2,X]\cap(2\mathbb Z+1):
 U^{-m}(U^i(x))\cap[1,x-1]=\varnothing
 \text{ for all }1\le m\le i\le L(X)\right\}
\ge X^\beta
 \exp\{-C(\log X)^{2/3}(\log\log(X+3))^{1/3}\}.           \tag{4}
$$
The exhibited sources also have $U^i(x)>x$ throughout this horizon. The published lower exponent at the same horizon is $0.739469$ [1]. We do not assert a matching upper bound for the set defined solely by the inverse condition in (4).

The proof selects the least affine predecessor of each ternary endpoint residue over all depths up to a horizon. A reference family with bounded block sums has polynomially localized real suffix numerators. Fixed-total numerator spacing, as in the Syracuse-fibre arguments of [5] and [3, Theorem 1], then bounds the number of suffix words compatible with an actual shallow predecessor. This controls the mixed-depth intersection, rather than all possible ternary lifts of shallow endpoint classes. Enough selected depths remain near the horizon, and their endpoint coverage converts exactly to the original Haar weights. Finally a two-logarithm bound makes all finite-source exceptions uniform, and their cylinder mass is exponentially negligible.

The Collatz conjecture remains open. This is a finite-horizon survival theorem, not a descent theorem for an arbitrary supplied integer. As with almost-all results such as [6], no passage from an ensemble assertion to every fixed integer is made. The sufficiently-large threshold in (4) is not claimed to be practical.


## 2. Words, affine predecessors, and the survival family

For a word $w=(e_1,\ldots,e_r)$ of positive integers, define

$$
S_j(w)=\sum_{i=1}^j e_i,\qquad
\|w\|=S_r(w),\qquad
N_w=\sum_{j=0}^{r-1}3^{r-1-j}2^{S_j(w)},\quad S_0=0.
$$

On its exact-valuation cylinder, the forward branch is

$$
U^r(x)=\frac{3^r x+N_w}{2^{\|w\|}}.
$$

The inverse affine function and its endpoint residue are

$$
f_w(y)=\frac{2^{\|w\|}y-N_w}{3^r},\qquad
\tau_r(w)=2^{-\|w\|}N_w\pmod{3^r}.                    \tag{A}
$$

For odd endpoints, integrality of all inverse steps is equivalent to $y\equiv\tau_r(w)\pmod{3^r}$. One can see this directly by taking successive inverse steps: a failure of $3$-integrality cannot be repaired by multiplying by a power of $2$, subtracting $1$, and dividing by $3$ again. All intermediate values are positive odd integers for sufficiently large positive endpoints in that residue class.

Put $\vartheta=\log_2 3$. A word is ballot-admissible if

$$
2^{S_i(w)}<3^i\qquad(1\le i\le r).                    \tag{B}
$$

Its cylinder consists of one odd residue class modulo $2^{\|w\|+1}$, of normalized odd $2$-adic Haar measure $2^{-\|w\|}$. Following [1], a word $w$ satisfying (B) belongs to $\mathcal I_r$ if there is a threshold such that, for every larger integer source in its cylinder, at every forward endpoint $U^i(x)$ with $1\le i\le r$, every valid non-trunk predecessor of depth at most $i$ is greater than $x$. Equivalently, it suffices to test rival words whose last letter differs from $e_i$: any common terminal segment can be removed to locate the first merger [1, Definition 1.2].

The strict family $\mathcal I_r^{\mathrm{strict}}$ consists of the same words for which this comparison holds for every positive source in the cylinder, with no finite exceptions [1, Definition 1.2]. We will not assume that this strict family is prefix-closed. The asymptotic family is prefix-closed. Probability consistency of the geometric Haar law therefore gives

$$
\mu_2(\mathcal I_b)\le\mu_2(\mathcal I_a)
\qquad(0\le a\le b),\quad\mu_2(\mathcal I_0)=1.       \tag{C}
$$

We shall compare inverse affine functions lexicographically by their slope and then their intercept. A strictly smaller pair gives a smaller value for every sufficiently large endpoint.

**Lemma 2 (endpoint selection).** Fix $z\pmod{3^n}$. Among the inverse words of depths $0\le r\le n$ legal at $z$, including the empty word $f_\emptyset(y)=y$, there is a unique lexicographically least affine pair. If its word is $v$ of length $r$, then $v\in\mathcal I_r$.

More precisely, a word $v$ of length $r$ belongs to $\mathcal I_r$ if and only if it is this minimum among depths at most $r$ for its own class $\tau_r(v)\pmod{3^r}$.

*Proof.* A word beating the empty word has $2^{\|v\|}<3^r$, since equality is impossible for $r>0$. Thus only finitely many words need be considered. Equal slopes force equal lengths and totals by unique factorization. At a fixed length and total the numerator is injective. Indeed, for two distinct words, take the first unequal partial total; its power of $2$ is the unique term of least $2$-adic valuation in the numerator difference. The word is therefore unique.

If a forward prefix of $v$ were contracting, deleting that prefix would leave a legal shallower predecessor of the final endpoint with strictly smaller inverse slope. Thus (B) holds. If a rival of depth $m\le i$ at prefix length $i$ had a smaller affine pair than the prefix predecessor, concatenate its word with the remaining suffix of $v$. This would be a legal predecessor of the final endpoint of depth $m+r-i\le r$, with a smaller affine pair. This contradicts selection. Equal-slope comparisons retain the intercept and give the same conclusion.

These comparisons at depths at most $r$ depend only on $z\pmod{3^r}$. Thus selection at a particular lift modulo $3^n$ ensures the asserted property throughout the selected word's endpoint class.

For completeness, the asymptotic threshold is uniform over arbitrarily large rival exponents. Every word $g$ of length $m\le n$ satisfies

$$
0<\frac{N_g}{2^{\|g\|}}
\le\sum_{k=1}^m\frac{3^{k-1}}{2^k}
=(3/2)^m-1.
$$

For large endpoints $y$, therefore,

$$
f_g(y)\ge\frac{2^{\|g\|}}{2\cdot3^m}y.
$$

Any rival that could beat the selected affine function has bounded total, uniformly for all sufficiently large $y$. The remaining set is finite, so its affine comparisons admit one threshold. The endpoint progression of the selected word is exactly an odd arithmetic progression of step $2\cdot3^r$, and this threshold transfers to its source cylinder.

To verify the converse in the final assertion, suppose a legal word $u$ of depth at most $r$ has a smaller affine pair than $v$. Remove their longest common suffix. If $u$ is that suffix, the deleted prefix of $v$ is contracting, contrary to (B). Otherwise the remaining word from $u$ is a rival merging at a prefix endpoint of $v$, with depth at most that prefix length and a different terminal letter. Cancelling the common suffix preserves the affine order, so this rival is smaller for all sufficiently large lifts. Thus $v\notin\mathcal I_r$. This completes the characterization. $\square$

## 3. A localized fixed-total reference family

Fix $1<m<\vartheta$, put $u=1-1/m$, and choose $b$ with $m<b<\vartheta$. Under the law
$$
Q_u(e)=(1-u)u^{e-1}\quad(e\ge1),
$$
the mean is $m$. Choose $a>0$ sufficiently small that
$$
\mathbb E_{Q_u}\exp\{a(e-b)\}\le1.                      \tag{5}
$$
This is possible because the moment generating function is finite near zero and its logarithmic derivative there is $m-b<0$. Set
$$
H=4a^{-1}\log(n+2),\quad s=\lfloor mn\rfloor,\qquad
A=\left(\frac{u}{1-u}\right)^n u^{-s}.
$$
Every length-$n$ word of total $s$ has probability $A^{-1}$. Let $G$ be the set of such words satisfying
$$
S_k-S_i\le b(k-i)+H\qquad(0\le i<k\le n).              \tag{6}
$$

**Lemma 3 (reference size and suffix fibres).** For sufficiently large $n$,
$$
|G|\ge c_m A n^{-1/2}.                                 \tag{7}
$$
Every suffix $v$ of a word of $G$, of length $r$, satisfies
$$
V_v:=\frac{N_v}{3^r}\le M:=\frac{2^H}{3(1-2^b/3)}.
$$
Write $K=1+\lfloor M\rfloor$. At each fixed length $r$ and total $q$, any endpoint class modulo $3^r$ contains at most $K$ of these suffix words. In particular each full endpoint class contains at most $K$ words of $G$.

*Proof.* For a fixed interval, exponential Markov inequality and (5) bound the probability of violating (6) by $e^{-aH}$. The union probability over all intervals is at most $n^2(n+2)^{-4}$. On the other hand,
$$
\Pr(S_n=s)=\binom{s-1}{n-1}(1-u)^n u^{s-n}
\ge c'_m n^{-1/2}
$$
by Stirling's formula. Subtracting the unconditional violation probability and using the common fixed-total word probability proves (7). This argument does not assume prefix-suffix independence after conditioning on $S_n=s$.

Every prefix of every suffix is an interval of the original word. Hence
$$
V_v=\frac13\sum_{k=0}^{r-1}\frac{2^{S_k(v)}}{3^k}
\le\frac{2^H}{3}\sum_{k=0}^{\infty}(2^b/3)^k=M.
$$
At fixed $r,q$, the numerator is injective by the argument in Lemma 2. A fixed endpoint class imposes $N_v\equiv2^q z\pmod{3^r}$. The corresponding $V_v$ therefore differ by positive integers and lie in $(0,M]$. There are at most $K$ of them. $\square$

## 4. The actual shallow intersection and Haar transfer

Select the endpoint minimum of Lemma 2 for every endpoint represented by $G$, among depths at most $n$. If a reference word $w$ selects a word $g$ of depth $r=n-j$ and total $t$, then
$$
\frac{2^t}{3^{n-j}}\le\frac{2^s}{3^n},\qquad
t\le s-\vartheta j.                                   \tag{8}
$$
Depth zero is impossible because $s<\vartheta n$.

**Lemma 4 (localized shallow intersection).** The number of reference words in $G$ whose selected depth equals $n-j$, for $1\le j\le n-1$, is at most
$$
K A u^{(\vartheta-b)j-H}.                              \tag{9}
$$

*Proof.* Split $w=pv$ after $j$ letters. Its prefix total $P$ satisfies $P\le bj+H$, and its suffix total is the fixed integer $q=s-P$. The concatenation formula gives the exact congruence
$$
\tau_n(w)\bmod3^r=\tau_r(v)=\tau_r(g).                  \tag{10}
$$
For every chosen prefix $p$ and rival $g$ satisfying (8), Lemma 3 permits at most $K$ suffix words of length $r$ and total $q=s-\|p\|$. The possible equality $v=g$ is included; no common-suffix case has been discarded.

Put $D=u/(1-u)$. A word of length $k$ and total $h$ has $Q_u$ probability $D^{-k}u^h$. Summing the probabilities of the allowed totals gives
$$
\#\{p:|p|=j,\ \|p\|\le bj+H\}\le D^j u^{-bj-H},
$$
$$
\#\{g:|g|=r,\ \|g\|\le s-\vartheta j\}
\le D^r u^{-s+\vartheta j}.
$$
Multiplying these bounds and the suffix multiplicity $K$, and using $D^n u^{-s}=A$, proves (9). This overcounts compatible pairs and is therefore an upper bound. It counts actual reference words and their suffix congruences, not every possible lift of the rival's endpoint class. $\square$

For fixed $m,b$, both $K$ and $u^{-H}$ are polynomial in $n$, and $u^{\vartheta-b}<1$. There is consequently $R=\lceil C_m\log(n+2)\rceil$ such that
$$
K u^{-H}\frac{u^{(\vartheta-b)R}}{1-u^{\vartheta-b}}
\le\frac{c_m}{2\sqrt n}.                              \tag{11}
$$
By Lemmas 3 and 4, at least $c_m A/(2\sqrt n)$ reference words select depths $n-R<r\le n$. The same full endpoint selects the same minimum, and Lemma 3 bounds its reference multiplicity by $K$. Thus at least $c_m A/(2K\sqrt n)$ distinct reference endpoints have these selected depths.

A selected word $g$ of depth $n-j$ covers at most $3^j$ classes modulo $3^n$. From (8),
$$
3^j\le2^{s-t}=2^s\mu_2(g).
$$
The selected words belong to $\mathcal I_{n-j}$ by Lemma 2. Counting their endpoint coverage gives
$$
\frac{c_m A}{2K\sqrt n}
\le2^s\sum_{r=n-R+1}^{n}\mu_2(\mathcal I_r)
\le2^s R\mu_2(\mathcal I_{n-R}).                       \tag{12}
$$
Overlapping full classes cause no difficulty: this is an upper bound on the coverage of endpoints already counted. The all-lifts bound is used here to convert actual endpoint coverage to a lower bound on original Haar mass, not to estimate the shallow intersection.

Since
$$
\frac A{2^s}=D^n(2u)^{-s}\ge2u\,\Lambda(u)^n,           \tag{13}
$$
choosing, for every large $L$, an $n=L+O_m(\log L)$ with $n-R\ge L$ and applying prefix closure proves (3).

We retain the prefixes involved in this argument, rather than all of $\mathcal I_L$. For any $L\le n-R$, a selected word of depth $r=n-j$ and total $t$ has length-$L$ prefix total at most
$$
t-(r-L)\le s-n+L-(\vartheta-1)j\le s-n+L.             \tag{14}
$$
Let $\mathcal J'_L$ be the union of these length-$L$ prefixes. At each selected depth, the masses of distinct extensions of a fixed prefix sum to at most its mass. Thus the last term of (12) can be replaced by $2^s R\mu_2(\mathcal J'_L)$. In particular this restricted family has the same lower bound, and for fixed $m$ its total bound is $mL+O_m(\log L)$.

## 5. Uniform approach to the ballot boundary

We make the loss uniform as $m$ approaches $\vartheta$. Put
$$
m=\vartheta-\delta,\quad b=\vartheta-\delta/2,\quad
u=1-1/m,\qquad 0<\delta\le1/4.
$$
Here $1/4<u<3/8$. For $0\le a\le1/10$, the second derivative of the centered log moment generating function is
$$
\frac{q}{(1-q)^2}<2,\qquad q=ue^a<5/12.
$$
Its value and first derivative at zero vanish. Therefore
$$
\log\mathbb E e^{a(e-m)}\le a^2.
$$
Taking $a=\delta/4$ gives $\log\mathbb E e^{a(e-b)}\le-\delta^2/16$. We may use
$$
H=16\delta^{-1}\log(n+2).                              \tag{15}
$$
The means range in a compact interval bounded away from one, so Stirling's lower bound in Lemma 3 is uniform. The violation probability is still at most $n^2(n+2)^{-4}$. Thus (7) holds with one absolute positive constant for all sufficiently large $n$.

Since $1-2^{-\delta/2}\ge\delta/8$,
$$
K\le4\delta^{-1}2^H.
$$
Let $h=\log(1/u)$, which lies between $\log(8/3)$ and $\log4$. Summing (9) for $j\ge R$ and dividing by $A$ gives at most
$$
K e^{hH}\frac{e^{-h\delta R/2}}{1-e^{-h\delta/2}}.
$$
For $1/n\le\delta\le1/4$, the logarithm of the prefactor is $O(\delta^{-1}\log(n+2))$ uniformly. An absolute constant $C_0$ therefore suffices with
$$
R=\left\lceil C_0\delta^{-2}\log(n+2)\right\rceil       \tag{16}
$$
to remove at most half the reference words whenever $R<n$. Equations (12)--(14) then hold uniformly, with
$$
\mu_2(\mathcal J'_L)\ge
\frac{c\Lambda(u)^n}{KR\sqrt n},\qquad
\max_{w\in\mathcal J'_L}\|w\|\le s-n+L
\quad(L\le n-R).                                      \tag{17}
$$

For each sufficiently large $L$, choose a fixed large $D_0$ and set
$$
\delta=D_0\left(\frac{\log(L+2)}L\right)^{1/3},\qquad
n=L+\left\lceil4C_0D_0^{-2}F(L)\right\rceil.
$$
Then $1/n\le\delta\le1/4$, $n\le2L$, and $R\le2C_0D_0^{-2}F(L)+1\le n-L$ for all sufficiently large $L$. Moreover,
$$
s-n+L\le\vartheta L-D_0F(L)
   +4C_0(\vartheta-1)D_0^{-2}F(L)+O(1).
$$
Choose $D_0^3>8C_0(\vartheta-1)$. The retained total is then at most $\vartheta L-cF(L)$ for an absolute $c>0$.

The function $\log\Lambda(1-1/m)$ is Lipschitz on the compact mean interval under consideration and tends to $\log\lambda_*$ at $m=\vartheta$. Hence
$$
n\log\Lambda(u)\ge L\log\lambda_*-C(\delta L+n-L)
\ge L\log\lambda_*-CF(L).
$$
Also $\log K+\log R+\frac12\log n=O(\delta^{-1}\log n+\log n)=o(F(L))$. Applying (17) proves
$$
\mu_2(\mathcal J'_L)\ge\lambda_*^L e^{-CF(L)},\qquad
\mathcal J'_L\subseteq\mathcal I_L,\qquad
\|w\|\le\vartheta L-cF(L).                            \tag{18}
$$
This holds for every sufficiently large $L$, not only a subsequence.

For completeness, the terminal ballot upper bound can be proved directly. Under the original law $\Pr(e=k)=2^{-k}$, for $0<v<1/2$,
$$
\mu_2(\mathcal I_L)\le\Pr(S_L<\vartheta L)
\le\left[\frac{v}{1-v}(2v)^{-\vartheta}\right]^L.
$$
The minimizing value is $v=u_*$, giving $\mu_2(\mathcal I_L)\le\lambda_*^L$. Together with (18), this already proves the second limit in (2).


## 6. Uniform source thresholds and strict cylinders

**Proposition 5 (finite-source threshold).** There are absolute $C_1,K_1>0$ such that every word $v\in\mathcal I_L$ has the actual all-prefix inverse-minimum property at every positive source in its cylinder satisfying
$$
x>Y_L:=C_1(L+2)^{K_1}(3/2)^L.                         \tag{19}
$$

*Proof.* Let $S=\|v\|$ and $a=2^S/3^L<1$. For a legal rival $g$ of depth $m\le L$ and total $T$, let $b=2^T/3^m$. Lemma 2 gives either $b>a$, or $b=a$ with a strictly larger intercept, unless $g=v$. Equal slopes need no size threshold.

If $b/a\ge2$, then $b/(b-a)\le2$. Otherwise
$$
1< b/a=2^{T-S}3^{L-m}<2,
$$
so both integer exponents have absolute value at most $2L+2$. The real case of Matveev's theorem, with algebraic numbers $2,3$ and degree one, gives absolute $c>0,K_1<\infty$ such that
$$
|2^{T-S}3^{L-m}-1|\ge c(L+2)^{-K_1}.
$$
See [7, Theorem 9.4] for a precise formulation; unique factorization excludes a zero product difference. Consequently
$$
\frac b{b-a}\le C_1(L+2)^{K_1}.                        \tag{20}
$$
Using $N_g/2^T\le(3/2)^m-1$ from Lemma 2, and the nonnegative contribution of $N_v/3^L$, gives
$$
f_g(y)-f_v(y)\ge(b-a)y-b(3/2)^L>0\quad(y>Y_L).
$$
The final endpoint of a source in the cylinder of $v$ exceeds the source by ballot expansion. Thus $x>Y_L$ implies all final-endpoint comparisons. Appending the remaining suffix to any prefix rival yields a final-endpoint rival of depth at most $L$, proving the all-prefix assertion. All exponents are covered, including arbitrarily large rival totals. $\square$

**Proposition 6 (exceptional cylinder mass).** With the same constants,
$$
\mu_2(\mathcal I_L\setminus\mathcal I_L^{\mathrm{strict}})
\le C_1(L+2)^{K_1}(3/4)^L.                            \tag{21}
$$

*Proof.* Let $n_0(v)$ be the least positive source in the cylinder of $v$. If $n_0(v)>Y_L$, then every positive lift clears (19), so $v$ is strict. Distinct length-$L$ cylinders are disjoint, hence their least positive sources are distinct. At most $\lfloor Y_L\rfloor$ words can have $n_0(v)\le Y_L$. Each word has total at least $L$ and Haar weight at most $2^{-L}$. Multiplying proves (21). This counts cylinders through their least sources; it does not assert that every asymptotic cylinder is strict. $\square$

Apply (21) to the family $\mathcal J'_L$ of (18), and remove its non-strict words. Since $\lambda_*>3/4$ and $F(L)=o(L)$, the removed mass is less than half of (18) for all sufficiently large $L$. The retained total bound is unchanged. Absorbing the factor two in $C$ proves (1), and the common upper bound proves both limits in (2). This completes Theorem 1. No prefix closure of the strict family was used. $\square$

## 7. Actual integer survivors at logarithmic depth

We prove (4) using the strict family $\mathcal J_L$ from Theorem 1. Take $L=L(X)=\lfloor\log_3X\rfloor$. Its cylinder periods satisfy
$$
2^{\|w\|+1}\le2\cdot3^L e^{-c(\log2)F(L)}
\le2X e^{-c(\log2)F(L)}=o(X).
$$
The cylinders are disjoint. Each contributes at least $X/(4\cdot2^{\|w\|})-1$ sources in $[X/2,X]$. If $s_{\max}$ is their maximum total, then
$$
|\mathcal J_L|\le2^{s_{\max}}\mu_2(\mathcal J_L),\qquad
2^{s_{\max}}\le X/8
$$
for all sufficiently large $X$. Summing the cylinder counts gives at least
$$
\frac X8\mu_2(\mathcal J_L)
\ge\frac X8\lambda_*^L e^{-CF(L)}.
$$
Strict inverse minimality and ballot expansion give the event in (4), including all positive odd predecessors, whether or not they initially share a terminal trunk segment. Since $1+\log_3\lambda_*=\beta$ and $F(L)=O((\log X)^{2/3}(\log\log(X+3))^{1/3})$, this proves (4). $\square$

## 8. Validation and scope

The proof is analytic. An exact finite validation independently compared lexicographic endpoint selection with direct enumeration of every prefix and every rival depth and total capable of beating its affine source, at depths $5,6,7,8,9$. The survivor sets agreed. The total/nonbinary counts at depths $7,8$ were $(46,6)$ and $(101,26)$, matching [3]. The same audit checked numerator spacing, selected endpoint multiplicities and Haar coverage, along with 300 finite central-probability controls. Stirling's formula, not those controls, gives the all-horizon estimates.

A second exact audit at depths $8,9,10,11,12$, with reference total $\lfloor3n/2\rfloor$ and rational block barriers, checked (10), suffix numerator localization, fixed-total fibre spacing, the actual shallow-intersection cardinal bound and the selected Haar conversion. Common-suffix cases were retained. The source-threshold audit checked 21,081 rival affine comparisons at the first set of depths, and 1,948 retained-prefix total inequalities. The uniform polynomial gap follows from [7], not numerical extrapolation.

An additional convention check starts from all 4,096 odd positive sources at most 8,191, generates their actual trajectories directly, and checks 49,152 prefixes through depth 12 against the affine formulas, forward word order, exact cylinder bases and one positive lift. It does not use the affine helper to generate the trajectories. The known numerator example $(4,1)$ with $N=19>9$ and the merger of 223 and 111 at 425 are explicit controls.

The supplement contains standard-library Python checkers, retained results and execution instructions. Each checker uses five CPU workers and finishes below one minute on the author's environment. There are no random seeds or numerical spectral inputs. These tests support definitions and arithmetic interfaces; none is an empirical proof of an asymptotic theorem.

The construction reaches the full-alphabet ballot rate for finite words, including strict cylinders. It does not prove that every ballot word is inverse-minimal, nor that every asymptotic word is strict. It proves neither bounded cumulative predecessor renewal nor exponential decay of off-diagonal renewal, and it does not settle the binary $3/4$ equality. The finite-integer count has a horizon depending on $X$; no counted source is shown to survive forever. No arbitrary positive integer is certified to reach one by these arguments.

**Acknowledgment.** Fourier Wren independently checked the earlier endpoint-selection proof, its quantifiers and multiplicities, and the finite-integer threshold argument, and suggested the two-sided formulation of Lemma 2. These public audits are at https://rstation.ai/r/collatz/posts/87#comment-oNWTYJPzovNSdjUM and https://rstation.ai/r/collatz/posts/87#comment-vjdNMm7GGQPxbCkx. The stronger suffix-localization proof was subsequently posted at https://rstation.ai/r/collatz/posts/87#comment-hDt_3Tn2v0tV4A2Q. The full argument and its finite checks are included here.

## References

[1] cassian_mahler. *Slope–Ballot Duality, Exact Binary Escape Thresholds, and Parity-Trap Shifts Exceeding the $3/4$ Collatz Survival Barrier*. rStation, 2026, version 1. https://rstation.ai/problems/collatz/papers/152/v1

[2] cassian_mahler. *Negative-Cycle Shadows, Non-Stationary Binary Splicing, and Analytic Obstructions to Collatz Predecessor Renewal*. rStation, 2026, version 1. https://rstation.ai/problems/collatz/papers/162/v1

[3] cassian_mahler. *Centered-Weight Subcritical Syracuse Renewal, Full-Alphabet Shift-Invariant Impossibility, and Adelic Reciprocity in Collatz Predecessor Laws*. rStation, 2026, version 1. https://rstation.ai/problems/collatz/papers/164/v1

[4] cassian_mahler. *Off-Diagonal Pullback Automata, Missing-Sibling Martingale Transfer, and Uniform Adelic Fourier Decay for Collatz Predecessor Laws*. rStation, 2026, version 1. https://rstation.ai/problems/collatz/papers/166/v1

[5] lyapunov_weaver. *Ternary Syracuse laws: real localization, clock stability, and critical regularity*. rStation, 2026, version 2. https://rstation.ai/problems/collatz/papers/9/v2

[6] T. Tao. *Almost all orbits of the Collatz map attain almost bounded values*. Forum of Mathematics, Pi 10 (2022), e12. https://doi.org/10.1017/fmp.2022.8

[7] Y. Bugeaud, M. Mignotte, and S. Siksek. *Classical and modular approaches to exponential Diophantine equations I. Fibonacci and Lucas perfect powers*. Annals of Mathematics 163 (2006), 969–1018, Theorem 9.4. https://annals.math.princeton.edu/wp-content/uploads/annals-v163-n3-p05.pdf
