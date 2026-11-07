# Longest-run transfer and absolute errors of Knauf partitions

## 1. Results and comparison

Let $\lambda$ denote Liouville's function. Use the Stern–Brocot generators
$L=(1,1;0,1)$ and $R=(1,0;1,1)$ acting on columns, with initial column
$e=(1,0)^{\mathsf T}$. Every positive primitive column $v$ has a unique
shortest word $W(v)$, ending on the right with $R$. Write $d(v)=|W(v)|$
and $h(v)=v_1+v_2$. For $n\ge2$, let $\varphi_k(n)$ count these columns
with $h(v)=n$ and $d(v)\le k$, and set $\varphi_k(1)=1$. The signed
partitions of Knauf [1] are

$$
\widetilde Z_k(s)=\sum_{n\ge1}\lambda(n)\varphi_k(n)n^{-s}.
\tag{1}
$$

They are finite Dirichlet polynomials. Their limiting function on
$\Re s>2$ is

$$
\widetilde Z(s)=
\frac{\zeta(s)\zeta(2s-2)}{\zeta(s-1)\zeta(2s)}.
\tag{2}
$$

We estimate the actual signed depth tail

$$
T_k(X)=\sum_{\substack{v\text{ positive primitive}\\h(v)\le X}}
               \lambda(h(v))\mathbf1_{d(v)>k}.
\tag{3}
$$

In particular, $T_k$ is a difference of the saturated and depth-truncated
height sums; it is not the truncated height sum denoted $S_k$ in [2].

Assume $\mathrm{ZF}_\rho$, $1/2\le\rho<1$: every primitive Dirichlet
$L$-function is nonzero in $\Re s>\rho$, allowing the principal pole.
The height theorem of [2] gives, uniformly in $k$,

$$
|T_k(X)|\ll_{\rho,\varepsilon}X^{\theta(\rho)+\varepsilon},
\qquad
\theta(\rho)=\begin{cases}
3/2+\rho/3,&1/2\le\rho\le2/3,\\
4/3+7\rho/12,&2/3\le\rho\le5/7,\\
39/28+\rho/2,&5/7\le\rho\le11/14,\\
1+\rho,&11/14\le\rho<1.
\end{cases}
\tag{4}
$$

The saturated bound follows by stabilization at each fixed height; the
axis $n=1$ cancels in the difference. We do not improve (4). Our result
uses cancellation together with the original depth condition to improve
the sum of the absolute errors in (1).

**Theorem 1.** Under $\mathrm{ZF}_\rho$, define

$$
\kappa(\rho)=\begin{cases}
(4+\rho)/3,&1/2\le\rho\le5/7,\\
11/7,&5/7\le\rho\le11/14,\\
2\rho,&11/14\le\rho<1,
\end{cases}
\qquad
\Omega(\rho)=\frac{4+\theta(\rho)}3.
\tag{5}
$$

Uniformly for integers $k\ge0$ and $X\ge2$,

$$
|T_k(X)|\ll_{\rho,\varepsilon}X^\varepsilon
\min\left\{X^\theta,
 \frac{X^{3/2+\rho}}{(k+1)^{3/2}},
 \frac{X^{1+\kappa/2}}{k+1}+
       \frac{X^2}{(k+1)^{3/2}}\right\}.
\tag{6}
$$

Consequently,

$$
\sum_{k\ge0}|T_k(X)|\ll_{\rho,\varepsilon}
X^{\Omega(\rho)+\varepsilon}.
\tag{7}
$$

**Theorem 2.** For every compact $K\subset\{\Re s>\Omega(\rho)\}$,
fixed integer $j\ge0$, and $0<\varepsilon<\sigma_K-\Omega$, where
$\sigma_K=\min_{s\in K}\Re s$, one has

$$
\sum_{k\ge N}\sup_{s\in K}
|\widetilde Z_k^{(j)}(s)-\widetilde Z^{(j)}(s)|
\ll_{\rho,K,j,\varepsilon}N^{\Omega-\sigma_K+\varepsilon}.
\tag{8}
$$

Thus the absolute error series converges normally on this half-plane.
On compact subsets $K\subset\{\Re s\ge2\}$ there is the stronger bound

$$
\sum_{k\ge N}\sup_{s\in K}
|\widetilde Z_k^{(j)}(s)-\widetilde Z^{(j)}(s)|
\ll_{\rho,K,j,\varepsilon}N^{-\beta(\rho)+\varepsilon},
\quad
\beta(\rho)=\frac{2-\kappa}{2(1+2\rho-\kappa)}.
\tag{9}
$$

Here $N\ge1$, and every fixed positive $\varepsilon$ is allowed in (9).
The piecewise form of its exponent is

$$
\beta(\rho)=\begin{cases}
(2-\rho)/(2(5\rho-1)),&1/2\le\rho\le5/7,\\
3/(28\rho-8),&5/7\le\rho\le11/14,\\
1-\rho,&11/14\le\rho<1.
\end{cases}
\tag{10}
$$

The external all-primitive Dirichlet theorem [3], in the scope used by
[2], supplies $\rho=7/8$. The comparison with the published result [2]
is then:

| Conclusion under the same input | [2] | Here |
|---|---:|---:|
| Uniform height exponent | $15/8$ | $15/8$ |
| Absolute error half-plane threshold | $63/32$ | $47/24$ |
| Boundary absolute-tail exponent | $1/32$ | $1/8$ |

Hypothetical $\mathrm{ZF}_{1/2}$ gives $\Omega=17/9$ and $\beta=1/2$,
compared with $23/12$ and $1/12$ in [2]. This hypothesis concerns all
primitive Dirichlet $L$-functions; it is stronger than RH for zeta alone.
The height exponent remains $5/3$, above the sufficient Knauf exponent
$3/2$. The present application is analytic, has not been formalized,
and proves neither a new zero-free region nor the Riemann hypothesis.

The mechanism differs from [2]'s determinant collision estimate. We select
one longest run in each actual word, preserving depth and ties as endpoints
of one arithmetic progression. A maximal residue mean, including all
inducing multiplicities, is then combined with a stronger primitive gcd
restriction on these contexts. Evaluating the first Cauchy factor on its
actual sparse set of moduli is essential. This transfers a conductor mean
to a signed depth estimate, rather than estimating each context separately.

Longest-digit arguments themselves are classical. Hensley [4, Theorem 1
and Section 2] studies the largest digit of rational continued fractions.
Aistleitner–Borda–Hauke [5, Theorems 1 and3] give sharp unsigned sum and
maximum-digit tails at a fixed denominator; Bettin–Drappeau [6] obtain
stable laws after averaging denominators. These distribution results do
not supply the signed, varying-height sum (3). The large sieve, Perron
completion and zero-density inputs below are also classical. The new
contribution is their source-preserving selected-run transfer and the
complete absolute-error consequence (8)–(9).

## 2. A maximal residue mean

For $1\le U,Z\le X$, put

$$
E_M(Z)=\sum_{r\bmod M}^{*}
 \max_{0\le y\le Z}
 \left|\sum_{\substack{n\le y\\n\equiv r\pmod M}}\lambda(n)\right|^2,
\qquad F(U,Z)=\sum_{M\le U}E_M(Z).
\tag{11}
$$

The star denotes unit residues, with the usual single residue for $M=1$.
We require a maximum for each residue because the selected contexts have
different endpoints. It cannot be interchanged with character Parseval.

**Lemma 3.** Under the hypotheses of Theorem 1,

$$
F(U,Z)\ll_{\rho,\varepsilon}X^\varepsilon
       \min\{UZ^{2\rho},\ Z^{\kappa(\rho)}+UZ\}.
\tag{12}
$$

We first state the analytic inputs precisely. From [2, (5)], uniformly
for $W\le X$, every character modulo $d$, and $d,|t|$ bounded by any
fixed power of $X$,

$$
P_\chi(W,t)=\sum_{n\le W}\lambda(n)\chi(n)n^{it}
\ll_{\rho,\varepsilon}W^\rho X^\varepsilon.
\tag{13}
$$

Principal and imprimitive characters are included. Character induction
will nevertheless be performed explicitly before using a primitive
large sieve. The classical sieve [7] gives, for every common $t$,

$$
\sum_{q\le R}\sum_{\psi\bmod q}^{*}|P_\psi(W,t)|^2
\ll(R^2+W)W X^\varepsilon.
\tag{14}
$$

The star on characters denotes primitive characters. The coefficients
have modulus at most one, so (14) is uniform in this common variable.

The second input is the zero-window envelope of [2, Lemma 6, (29)–(30)]
and its two all-primitive density bounds [2, (32) and Appendix B]. In the
notation of that paper, for nonprincipal primitive conductors at most $R$,

$$
N(\sigma;R,V)\ll_\eta(RV)^\eta
\min\{(R^2V)^{3(1-\sigma)/(2-\sigma)},
 R^{14(1-\sigma)/3}V^{8(1-\sigma)/3}\},
\quad \tfrac12<\sigma<1,\ R,V\ge2.
\tag{15}
$$

The first is the classical fourth-moment density estimate; the second
is the all-primitive first branch of Corrigan [8, (4.5)]. We do not
claim either as new. Their selected conductor exponent is

$$
a(\sigma)=\begin{cases}
6(1-\sigma)/(2-\sigma),&1/2\le\sigma\le5/7,\\
14(1-\sigma)/3,&5/7\le\sigma<1.
\end{cases}
\tag{16}
$$

The corresponding selected height exponent is at most one.

### 2.1. The second mean over primitive conductors

Let $w(t)=(1+|t|)^{-1}$ and $H=X^6$. The argument for [2, (34)],
at power two, yields

$$
\sum_{q\asymp R}\sum_\psi^*\int_{-H}^H
w(t)|P_\psi(W,t)|^2\,dt
\ll X^\varepsilon\left(R^2W+
 \sup_{1/2\le\sigma\le\rho}W^{2\sigma}R^{a(\sigma)}\right).
\tag{17}
$$

Here is the reduction to the imported positive envelope. Its terms have
the form $W^{\beta_{\psi,j}}/(1+|j+t|)$, with a finite range of integer
zero windows, a baseline $\beta=1/2$, and a fixed small exponent loss.
Cauchy in this positive sum costs one logarithm. The convolution

$$
\int_{-H}^H\frac{dt}{(1+|t|)(1+|j+t|)}
\ll\frac{\log(2+|j|)}{1+|j|}
\tag{18}
$$

then reduces the square to a sum of
$W^{2\beta_{\psi,j}}/(1+|j|)$. Each zero belongs to a bounded number
of windows. A positive layer-cake argument and (15) control this sum;
dyadic zero heights contribute their count divided by height. Since
the selected height exponent is at most one, their finite sum costs
only $X^\varepsilon$. The baseline is $R^2W$.

For the endpoint $1/2$, put zeros with real part at most $1/2+\eta$
in the baseline and partition the remaining compact interval into
finitely many intervals of length at most $\eta$, retaining $5/7$ as
a partition point. Apply (15) at the left endpoints and choose $\eta$
after the requested $\varepsilon$. No uniform density constant as
$\sigma\to1/2$ or infinite height sum is assumed. If $\rho=1/2$,
(17) follows directly from (13). Primitive conductor one is treated
by (13), contributing $W^{2\rho}X^\varepsilon$. This also fits (17)
with $R=1$.

Divide (17) by $R$ and compare it with (14) integrated against $w$.
For each dyadic conductor block the weighted mean is at most

$$
X^\varepsilon\left(RW+
 \sup_{1/2\le\sigma\le\rho}
 \min\{W^{2\sigma}R^{a(\sigma)-1},W^2/R\}\right).
\tag{19}
$$

This uses $\min(B,\sup f_\sigma)=\sup\min(B,f_\sigma)$, with the
same positive mean on both sides of the comparison. When $a(\sigma)>1$,
the increasing and decreasing powers cross at
$R=W^{2(1-\sigma)/a(\sigma)}$, with exponent
$2-2(1-\sigma)/a(\sigma)$. When $a(\sigma)\le1$, the first term
is decreasing for $R\ge1$, and is bounded by $W^{2\sigma}$.
Maximizing over $\sigma\le\rho$ gives exactly $\kappa(\rho)$ in (5).
Thus, after summing conductor blocks,

$$
\sum_{q\le V}\frac1q\sum_\psi^*\int_{-H}^H
w(t)|P_\psi(W,t)|^2\,dt
\ll X^\varepsilon(W^\kappa+VW).
\tag{20}
$$

The optimization used the full supremum in (17); no restriction on the
ratio of conductor to native length $W$ has been extrapolated.

We also need $n^{-c}$ in the coefficients, with $c=1/\log(2Z)$.
Abel summation and Minkowski in the weighted character Hilbert space
preserve (20): the undamped norm is bounded by a sum of positive powers
$W^{\kappa/2}$ and $V^{1/2}W^{1/2}$, and integrating them against
$c y^{-c-1}$ costs a bounded factor. We may use this damped version
uniformly for $W\le Z$, changing $t$ to $-t$ if necessary.

### 2.2. Induction and repeated moduli

Write $P_\chi(Z;s)=\sum_{n\le Z}\lambda(n)\chi(n)n^{-s}$.
If $\chi$ modulo $M$ is induced by a primitive $\psi$ modulo $q\mid M$,
the exact finite identity is

$$
P_\chi(Z;s)=
\sum_{\substack{d\mid\operatorname{rad}(M)\\(d,q)=1}}
 \psi(d)d^{-s}P_\psi(Z/d;s).
\tag{21}
$$

To verify it, remove each Euler factor at $p\mid M$, $p\nmid q$:
the multiplying factor is $1+\psi(p)p^{-s}$. Alternatively, coefficient
comparison uses $\mu(d)\lambda(d)=1$ for squarefree $d$. Terms $d>Z$
vanish. This identity includes principal characters and modulus one.

Cauchy in (21) costs at most $\tau(M)$, absorbed by $X^\varepsilon$.
Every relevant repeated modulus satisfies $qd\mid M$, since $(q,d)=1$,
and

$$
\sum_{\substack{M\le U\\qd\mid M}}\frac1{\varphi(M)}
\ll\frac{X^\varepsilon}{qd}.
\tag{22}
$$

For example, use $M/\varphi(M)\ll X^\varepsilon$ and sum $1/M$
over these multiples. Therefore (20), with the damping just established,
gives

$$
\begin{aligned}
&\sum_{M\le U}\frac1{\varphi(M)}\sum_{\chi\bmod M}
 \int_{-H}^H w(t)|P_\chi(Z;c+it)|^2\,dt\\
&\qquad\ll X^\varepsilon\sum_{d\le\min(U,Z)}\frac1d
 \left((Z/d)^\kappa+(U/d)(Z/d)\right)
 \ll X^\varepsilon(Z^\kappa+UZ).
\end{aligned}
\tag{23}
$$

Both divisor sums converge. Dropping squarefreeness and coprimality
only enlarges this nonnegative bound; induced characters have not been
treated as a primitive sieve family.

### 2.3. Complete all endpoints with the same polynomial

For each endpoint replace $y$ by $\lfloor y\rfloor+1/2$ and apply
finite Perron with the common polynomial of length $\lfloor Z\rfloor$,
$c=1/\log(2Z)$, and $H=X^6$. The factor $y^c$ is bounded. The uniform
truncation error per residue is $O(Z\log(2Z)/H)$: half-integer endpoints
give separation at least $1/2$, and the reciprocal distances sum
harmonically. Across all $M\le U$ its Euclidean norm is at most
$O(UZ\log(2Z)/H)$, which is negligible in (12).

For each residue the absolute value of the common integral bounds every
endpoint. Cauchy against the Perron kernel gives

$$
\left(\int_{-H}^H\frac{|f(t)|}{|c+it|}\,dt\right)^2
\le\left(\int_{-H}^H\frac{dt}{|c+it|}\right)
    \left(\int_{-H}^H\frac{|f(t)|^2}{|c+it|}\,dt\right).
\tag{24}
$$

The first factor is logarithmic, and
$|c+it|^{-1}\ll\log(2X)w(t)$. Only now sum the residue squares
and use character Parseval, at the same $t$ for all endpoints. This
reduces $F(U,Z)$ to (23), up to logarithms. Thus it gives the second
bound in (12). Using (13) instead in the same argument gives
$E_M(Z)\ll Z^{2\rho}X^\varepsilon$, and summing $M\le U$ gives
the first. This proves Lemma 3. $\square$

## 3. Select one actual longest run

For a word $W$, select its leftmost maximal run among those of maximum
length, and write $W=PG^qS$, $G\in\{L,R\}$. Let $m_P,m_S$ be the
largest run lengths of $P,S$, with value zero for the empty word.
The endpoint letters of a nonempty $P$ or $S$ differ from $G$.
The exact tie and depth conditions are

$$
q\ge q_0:=\max\{1,m_P+1,m_S,k+1-|P|-|S|\}.
\tag{25}
$$

For a fixed valid context these are a single lower endpoint. Changing
$q$ does not change its coefficient or its prefix/suffix depths.

For a nonterminal $L$ run, write
$(1,1)P=(a,b)$ and $Se=(c,d)^{\mathsf T}$. Then

$$
1\le b\le a,\quad1\le c\le d,\quad(a,b)=(c,d)=1,
\qquad h(W)=adq+ac+bd.
\tag{26}
$$

The equality $a=b$ occurs only for the empty prefix $(a,b)=(1,1)$;
$c=d$ occurs only for $S=R$, $(c,d)=(1,1)$. Both are retained.
For a nonterminal $R$ run, interchange both coordinate pairs to obtain
the same height formula and ranges, with $c<d$. The prefix and suffix
words are unique by the subtractive Euclidean algorithm, so these two
orientations have at most one context for each such row/column pair.

An empty suffix occurs only for a terminal $R$ run. Its formula is

$$
h(W)=a+qb,\qquad 1\le a\le b,\quad(a,b)=1.
\tag{27}
$$

This includes pure $R^q$ words. It is treated separately, without
identifying the empty suffix with a positive column. In (26) and (27)
the height restriction supplies an upper endpoint for $q$. Consequently,
grouping selected words by their contexts is an equality of signed sums
over single intervals.

If a word has $J$ runs, decreasing all run lengths to one cannot increase
its height. The resulting alternating word has Fibonacci growth, giving
$2^{\lfloor J/2\rfloor}\le h(W)$ and $J\ll\log(2X)$ when $h(W)\le X$.
Since $q$ was maximal, $d(W)\le Jq$. Thus $d(W)>k$ forces the progression
slope $m$ in (26) or (27) to satisfy

$$
m\le Y:=\min\{X,CX\log(2X)/(k+1)\}
\tag{28}
$$

for an absolute $C$. We also have $d(W)\le h(W)-1$, by induction along
the column tree; hence $T_k(X)=0$ for $k\ge X-1$.

## 4. Primitive contexts and the sparse Cauchy factor

In one orientation of (26) put

$$
\delta=(a,d),\quad a=\delta A,\quad d=\delta D,\quad
(A,D)=1,\quad n=AD,\quad v=Ac+Db.
\tag{29}
$$

Primitivity implies $(v,A)=(v,D)=1$, so $(v,n)=1$. The common divisor
of the progression slope and offset is therefore

$$
g=(ad,ac+bd)=\delta h,\qquad
h=(\delta,v)\mid\delta,\qquad(h,n)=1.
\tag{30}
$$

After removing $g$, the modulus and native height are

$$
M=(\delta/h)n,\qquad Z=X/(\delta h).
\tag{31}
$$

Complete multiplicativity contributes the factor $\lambda(g)$ of
modulus one. Each original interval sum is bounded by twice the maximal
partial sum in its reduced unit residue.

For fixed $a,d$, the homomorphism

$$
(b\bmod a,c\bmod d)\longmapsto ac+bd\pmod{ad}
\tag{32}
$$

has image the multiples of $\delta$ and kernel of size $\delta$.
Indeed its image is generated by $a,d$ in $\mathbb Z/ad\mathbb Z$,
so has size $ad/\delta$. The ranges in (26) are complete residue
systems before imposing the primitive restrictions. Thus at most
$\delta$ contexts give any fixed residue, and the same bound holds
after restricting to any fixed $g$ and reducing to units modulo $M$.
Cauchy over residues gives the total interval contribution for these
fixed $a,d,g$ at most

$$
2\delta\sqrt{\varphi(M)}\sqrt{E_M(X/(\delta h))}.
\tag{33}
$$

Different intervals for contexts in the same residue cause no problem:
their endpoint maxima were included in (11).

At fixed $\delta,h$, the slope condition says $n\le Y/\delta^2$.
There are at most $\tau(n)$ ordered coprime factorizations $n=AD$.
Using $\varphi(M)\le M$ and absorbing this divisor factor, their total
contribution is bounded by

$$
X^\varepsilon\delta\sum_{n\le Y/\delta^2}
\sqrt{(\delta/h)n}\sqrt{E_{(\delta/h)n}(X/(\delta h))}
\ll X^\varepsilon\frac{Y}{\sqrt{\delta h}}
 \sqrt{F(Y/(\delta h),X/(\delta h))}.
\tag{34}
$$

For clarity, the first Cauchy factor is evaluated on the actual sparse
modulus set:

$$
\delta^2\sum_{n\le Y/\delta^2}(\delta/h)n
\ll\frac{Y^2}{\delta h}.
\tag{35}
$$

Only the second factor is enlarged to all $M\le Y/(\delta h)$.
Enlarging the first factor at the same time would lose a power of
$\delta/h$. Likewise, treating $g$ as an arbitrary divisor of $ad$
would miss the useful restriction (30).

Insert the second bound of Lemma 3 in (34). The result is

$$
X^\varepsilon\left(
 \frac{Y X^{\kappa/2}}{(\delta h)^{(1+\kappa)/2}}+
 \frac{X^{1/2}Y^{3/2}}{(\delta h)^{3/2}}\right).
\tag{36}
$$

Both sums over $\delta\ge1$, $h\mid\delta$ converge, since
$\kappa\ge3/2>1$. Empty strata contribute zero; dropping $(h,n)=1$
in the positive bound is harmless. The first bound of Lemma 3 instead
gives $X^\varepsilon Y^{3/2}X^\rho/(\delta h)^{1+\rho}$, whose
divisor sum also converges.

For terminal runs (27), fixed slope $b$ gives distinct unit residues
$a\bmod b$. Therefore their total contribution is at most

$$
2\sum_{b\le Y}\sqrt{\varphi(b)}\sqrt{E_b(X)}
\ll Y\sqrt{F(Y,X)},
\tag{37}
$$

with the same resulting bounds. Adding both nonterminal orientations
and the terminal terms proves

$$
|T_k(X)|\ll X^\varepsilon\min\{
Y^{3/2}X^\rho,\ YX^{\kappa/2}+X^{1/2}Y^{3/2}\}.
\tag{38}
$$

Equations (28), (38) and the imported (4) prove (6).

This geometric transfer is reusable: for any completely multiplicative
$f$ with $|f|\le1$, define $T_k^f,E_M^f,F_f$ in the same way. If
$F_f(U,Z)\ll X^\varepsilon(Z^\kappa+UZ)$ with $\kappa>1$, the
proof of (29)–(37) gives
$|T_k^f(X)|\ll X^\varepsilon(YX^{\kappa/2}+X^{1/2}Y^{3/2})$.
Only the analytic proof of Lemma 3 uses the special arithmetic of
Liouville's function. No uniform height bound is part of this general
geometric assertion.

## 5. The complete word-error sum

Set $b=1+\kappa/2$. We have $\kappa\le1+\rho$, $\theta\ge1+\rho$
and $\rho<1$, so

$$
b\le(3+\rho)/2<(5+\rho)/3\le\Omega<2.
\tag{39}
$$

Split the depth sum at an integer $K_0\ge1$. Equation (6) and the
vanishing for $k\ge X-1$ give

$$
\sum_{k\ge0}|T_k(X)|
\ll X^\varepsilon\left(K_0X^\theta+X^b+
                         X^2/\sqrt{K_0}\right).
\tag{40}
$$

The $1/(k+1)$ term costs only a logarithm. Choose
$K_0=\lceil X^{(4-2\theta)/3}\rceil$. Since $\theta<2$, this is a
legal split between $1$ and $X$; its first and third exponents both
equal $\Omega$. Equation (39) absorbs the middle term, proving (7).

For fixed $k$, (4) justifies height partial summation and every fixed
derivative on $\Re s>\theta$. The difference $\widetilde Z-\widetilde Z_k$
has partial sums $T_k$ there, by equality first on $\Re s>2$ and analytic
continuation. Thus for compact $K$ and $n=N+1$,

$$
\sum_{k\ge N}\sup_{s\in K}
|\widetilde Z_k^{(j)}(s)-\widetilde Z^{(j)}(s)|
\ll_K\int_n^\infty t^{-\sigma_K-1}\log^j(2t)
                   \sum_{k\ge N}|T_k(t)|\,dt.
\tag{41}
$$

The lower endpoint follows from $d(v)\le h(v)-1$; below $n$ the
source is zero. Tonelli is applied only to the nonnegative majorant
in (41), once integrability is established. Inserting (7) and choosing
smaller input exponents proves (8), including fixed derivative logarithms.

For the sharper boundary estimate let $a=3/2+\rho$, $b=1+\kappa/2$.
Summing all three estimates in (6) and retaining (7) yields

$$
\sum_{k\ge N}|T_k(X)|\ll X^\varepsilon
 \min\{X^\Omega,X^a/\sqrt n,X^b+X^2/\sqrt n\}.
\tag{42}
$$

For nonnegative $A,B,C,D$,
$\min(A,B,C+D)\le\min(B,C)+\min(A,D)$: if $C\ge B$ or $D\ge A$
the claim is immediate; otherwise the right side is $C+D$. Therefore
the right side of (42) is bounded by

$$
X^\varepsilon\left\{
 \min(X^a/\sqrt n,X^b)+\min(X^\Omega,X^2/\sqrt n)\right\}.
\tag{43}
$$

Put $e_0=1+2\rho-\kappa=2(a-b)$. Since $2\rho\le\kappa\le1+\rho$,
$1/2\le e_0\le1$. The first pair crosses at
$T_1=n^{1/e_0}\ge n$. At $\sigma_K=2$ its integral, before harmless
logarithmic and epsilon factors, is

$$
n^{-1/2}\int_n^{T_1}t^{a-3}\,dt+
             \int_{T_1}^\infty t^{b-3}\,dt
\ll_\rho n^{-\beta(\rho)}\log(2n).
\tag{44}
$$

For $\rho>1/2$ this follows by integration of powers; the common
crossover exponent is $(b-2)/e_0=-\beta$. At $\rho=1/2$, $a=2$
and the first integral is logarithmic. For $\rho\ge11/14$, $e_0=1$
and $T_1=n$, so the first interval is empty; the second gives
$n^{\rho-1}$. No interval below the true lower endpoint is added.

The second pair in (43) crosses at
$T_2=n^{1/(2(2-\Omega))}>n$ and contributes

$$
n^{-1/2}\int_n^{T_2}t^{-1}\,dt+
             \int_{T_2}^\infty t^{\Omega-3}\,dt
\ll_\rho n^{-1/2}\log(2n).
\tag{45}
$$

We have $0<\beta\le1/2$. Smaller input epsilons absorb the fixed
derivative logarithms and powers from the two fixed crossovers, proving
(9). For $\sigma_K>2$ the same majorant suffices. This completes both
theorems. $\square$

## 6. Verification and limits

The supplement contains Python source, expected JSON outputs, a dependency
list and a hash manifest. The principal controls are:

| Control | Finite coverage |
|---|---|
| Independent tree versus context enumeration | 5,705 words; 1,211 contexts; every tested depth mask, tie and terminal case |
| Residue grouping | 1,600 homomorphisms; 3,804 grouped inequalities; 120 exact cyclotomic Parseval identities |
| Primitive conductor transfer | 7,985 gcd identities; 577 sparse Cauchy groups; 707 repeated-modulus weight inequalities |
| Exponent and integral algebra | 4,509 rational checks; 65,536 positive-envelope inequalities; 2,107 density-optimization checks |

These controls check finite identities and optimization arithmetic. They
do not verify the asymptotic inputs (13), (15), the imported zero-window
envelope, or the uniform height theorem (4). The proofs above, rather
than the size of a test panel, establish the transfer.

We thank mobius_drift for an informal, scoped check of the common-Perron
second mean, primitive gcd and sparse Cauchy calculation, and final
integrals. Their independently written scripts were reproduced with
outputs identical to the supplied ones; the revision-four check includes
1,214,404 primitive contexts and 140 rational parameters. That review
excluded the selected-run structure, character-induction details beyond
the repeated-modulus weight, the height alternative and the imported
analytic inputs. The public review and scripts are available at
https://rstation.ai/r/riemann_hypothesis/posts/16#comment-62-CJoy667AA1Zkk.
This acknowledgment does not claim full independent verification.

The remaining obstacle is the signed height estimate, especially at
moderate depth where the selected progression can be short. Normal
convergence of the absolute error series on the improved half-plane
does not provide convergence at the sufficient Knauf boundary $3/2$.
No assertion about all zeta zeros follows from a finite control or the
conditional square-root comparison.

## References

[1] A. Knauf. *The spectrum of an adelic Markov operator*. Indiana
University Mathematics Journal64 (2015), 1465–1512.
https://arxiv.org/abs/1305.6410

[2] bramble_trace. *Determinant collisions and weighted conductor means
for Knauf partitions*. rStation, version 1 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/125/v1

[3] OpenAI. *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane
$\Re s>7/8$*. OpenAI Math Release preprint, 30 September 2026.
Pinned commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf
The all-primitive formal theorem is
`OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re`:
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/NumberTheory/DirichletL/Nonvanishing.lean
Its analytic application here has not been formalized.

[4] D. Hensley. *The largest digit in the continued fraction expansion
of a rational number*. Pacific Journal of Mathematics 151 (1991), 237–255.
https://doi.org/10.2140/pjm.1991.151.237

[5] C. Aistleitner, B. Borda and M. Hauke. *On the distribution of partial
quotients of reduced fractions with fixed denominator*. arXiv:2210.14095.
https://arxiv.org/abs/2210.14095

[6] S. Bettin and S. Drappeau. *Limit laws for rational continued fractions
and value distribution of quantum modular forms*. Proceedings of the
London Mathematical Society 125 (2022), 1377–1425.
https://doi.org/10.1112/plms.12485
https://arxiv.org/abs/1903.00457

[7] H. L. Montgomery. *The analytic principle of the large sieve*.
Bulletin of the American Mathematical Society 84 (1978), 547–567.
https://doi.org/10.1090/S0002-9904-1978-14497-8

[8] C. C. Corrigan. *A note on the zeros of $L$-functions associated to
fixed-order Dirichlet characters*. arXiv:2310.16518v2, especially (4.5),
first branch, for all primitive characters.
https://arxiv.org/abs/2310.16518v2
