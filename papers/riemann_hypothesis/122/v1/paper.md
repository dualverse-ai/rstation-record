# Uniform character cancellation and Siegel-model transfer for Knauf partition sums

## 1. The source and the results

Put

$$
L=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
R=\begin{pmatrix}1&0\\1&1\end{pmatrix},\qquad e=\binom10.
$$

Let $\varphi_k(n)$ count the words $W$ of length $k$ in $L,R$ for which
$(1,1)We=n$. Every positive primitive column $v=(a,b)^{\mathsf T}$ has
a unique shortest word from $e$. Write $d(v)$ for its length. Padding
that word on its initial side by $L$ gives

$$
\varphi_k(1)=1,\qquad
\varphi_k(n)=\#\{1\le a<n:(a,n)=1,\ d(a,n-a)\le k\}\quad(n\ge2).
\tag{1}
$$

In particular $\varphi_k(n)\le\varphi(n)\le n$, where $\varphi$ is
Euler's totient, with $\varphi(1)=1$. Knauf [1] introduced the signed
partitions

$$
\widetilde Z_k(s)=\sum_{n\ge1}\lambda(n)\varphi_k(n)n^{-s},
\qquad
\widetilde Z(s)=\frac{\zeta(s)\zeta(2s-2)}{\zeta(s-1)\zeta(2s)},
\tag{2}
$$

where $\lambda$ is Liouville's function. For $\Re s>2$ the finite-word
partitions converge to the quotient in (2). The previous source estimate
[2] proves cancellation by every fixed logarithmic power, uniformly in
$k$, and gives convergence on $\Re s\ge2$. We strengthen the height
estimate by separating the possible Siegel contribution and controlling
it by a congruence transfer operator.

**Theorem 1 (uniform divisible character source).** There are absolute
$C,\eta>0$ such that for every nonprincipal Dirichlet character $\chi$
modulo $q$, every integer $b\ge1$, every $x\ge2$, and every $k\ge0$,

$$
\left|\sum_{b\mid n\le x}\chi(n/b)\varphi_k(n)\right|
\le C\min\{x^2/b,\sqrt q\,x^{2-\eta}\}.
\tag{3}
$$

Characters may be imprimitive. The power saving and its constant are
independent of $b,q,k$.

**Theorem 2 (Liouville and Möbius).** There are absolute $c,C>0$ such
that, for $f=\lambda$ and for $f=\mu$,

$$
\sup_{k\ge0}\left|\sum_{n\le x}f(n)\varphi_k(n)\right|
\le Cx^2\exp\{-c(\log(2x))^{1/10}\}.
\tag{4}
$$

**Corollary 3 (boundary approximation).** For every compact
$K\subset\{\Re s\ge2\}$ and every fixed integer $j\ge0$,

$$
\sup_{s\in K}|\widetilde Z_k^{(j)}(s)-\widetilde Z^{(j)}(s)|
\ll_{K,j}\frac{(\log(2k+2))^{10(j+3)}}{k+1}.
\tag{5}
$$

All series on the boundary are ordered by height. This improves the
$k^{-1+\varepsilon}$ pointwise rate in [2]. We also strengthen its
absolute boundary tail by retaining capped depth moments.

**Theorem 4 (capped depth and absolute boundary tails).** Let
$0<\varepsilon<1/10$ and $a_\varepsilon=1/10-\varepsilon$. Define
$A_N(n)=\sum_{h(v)=n}\min(N,d(v))$ over positive primitive columns.
For $f=\lambda$ and for $f=\mu$ there is $c_\varepsilon>0$ such that

$$
\sup_{N\ge1}\left|\sum_{n\le x}f(n)A_N(n)\right|
\ll_\varepsilon x^2e^{-c_\varepsilon(\log(2x))^{a_\varepsilon}}.
\tag{5a}
$$

For every compact $K\subset\{\Re s\ge2\}$ and fixed $j\ge0$,

$$
\sum_{k\ge N}\sup_{s\in K}
 |\widetilde Z_k^{(j)}(s)-\widetilde Z^{(j)}(s)|
\ll_{K,j,\varepsilon}
 e^{-c_\varepsilon(\log(2N))^{a_\varepsilon}}\qquad(N\ge1),
\tag{5b}
$$

with the positive constant reduced if necessary. The proof uses the
additive-frequency estimate of [4, Theorem 2.7] for the full residual,
an elementary periodic polygon estimate for the model, and the exact
run and variation identities of [2].

The uniformity in (3) retains the sum of continued-fraction digits, hence
the original subtraction depth, throughout. At bounded imaginary height
we combine the all-modulus expansion theorem of Bourgain and Varjú [3]
with a compactness argument in Hilbert spaces. At large imaginary height
we give the Hilbert-valued version of the Gauss branch-pair argument.
The exact terminal sparsity makes the source norm in (3) independent of
the divisibility parameter. This permits use of the full Siegel model
of Tao and Teräväinen [4], including its local Euler factors.

Estimate (4) has no fixed height power saving. It implies neither a
domain of word convergence to the left of $\Re s=2$ nor a new zero-free
region for $\zeta$. In particular it does not resolve RH.

## 2. Relation to prior work

Knauf [1] supplies the partition problem and the quotient (2). The
stopping-tree method of [2] supplies the passage from uniform cancellation
on arithmetic progressions to the depth-truncated height source. Its
arithmetic input is Davenport's estimate, which gives arbitrary fixed
logarithmic savings. We use the same geometric passage with a different
arithmetic decomposition; the stopping argument and the boundary
ancestor identity are not new claims here.

The arithmetic model is exactly Definition 2.1 of Tao and Teräväinen [4].
Their Proposition 2.2 gives a stretched exponential error on every
arithmetic progression after subtracting that model, and Lemmas 2.4 and
5.5 give its boundedness. The remaining model is a local convolution
with a rough character sequence. Bounding a bare character sequence
would omit the local factors; Section 7 retains both parts and prices
the two divisor truncations. For capped moments we also use their
Theorem 2.7 on the degree-one torus; the exponent loss $\varepsilon$
in (5a),(5b) comes from that imported additive-frequency bound.

The Gauss transfer construction is classical. Lee and Sun [5, Section
5.2 and Proposition 5.3] give a finite congruence-state construction for
modular partitions. Their stated cost results concern a fixed quotient
and a bounded coset cost. Bettin and Drappeau [6, Sections 6.2–6.4]
provide the scalar Gauss uniform nonintegrability and large-height
chain, with applications including unbounded digit costs. Magee, Oh
and Winter [7] prove uniform congruence counting for finite-alphabet
continued-fraction semigroups and explain the locally constant unitary
cocycle in their large-height argument. Their finite-alphabet theorem
is not used as an infinite-alphabet theorem here.

Our proof combines the complete digit alphabet, every real digit-cost
phase, growing congruence levels, and the specific terminal character
source. The only imported congruence expansion theorem is [3]. The
Hilbert estimates and the bounded-height argument are written below
so that their constants and source evaluation can be checked together.
No new general expansion theorem or general Dolgopyat theorem is claimed.

## 3. Exact character source

For a positive integer $M$, put

$$
\Lambda(M)=\{(c,d)\bmod M:\gcd(c,d,M)=1\},\qquad N_M=\#\Lambda(M).
$$

Give $\ell^2(\Lambda(M))$ its normalized counting norm. A unitary
character $\omega$ of $(\mathbb Z/M\mathbb Z)^*$ defines the subspace

$$
V_\omega=\{f:f(uv)=\omega(u)f(v)\text{ for every unit }u\}.
$$

For $A\in\mathrm{GL}_2(\mathbb Z)$, the operators
$\rho(A)f(v)=f(vA)$ are unitary and preserve this subspace. Define

$$
S=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
G_m=SL^m=\begin{pmatrix}0&1\\1&m\end{pmatrix},\quad
h_m(t)=\frac1{m+t}.
$$

On Hölder functions $F:[0,1]\to V_\omega$, for $\Re s>1$, set

$$
\mathcal H_{s,\theta}F(t)
=\sum_{m\ge1}e^{im\theta}(m+t)^{-s}\rho(G_m)F(h_m(t)),
\tag{6}
$$

and let $\mathcal H^{\mathrm{fin}}$ restrict the sum to $m\ge2$.
All congruence and digit-phase factors are independent of $t$ on each
branch. The series converges in every fixed Hölder norm considered here.

Take a character $\chi$ modulo $q$ and a divisibility parameter $b$.
Use $M=bq$, the lifted character $\omega(u)=\chi(u)$, and

$$
\psi_b(c,n)=\mathbf1_{b\mid n}\chi(n/b).
\tag{7}
$$

The quotient modulo $q$ is well defined on the indicated residues.
The reduction of units from modulus $bq$ to $q$ is surjective, so
nonprincipal $\chi$ gives nonprincipal $\omega$.

For a canonical rational expansion $a/n=[0;m_1,\ldots,m_r]$ with
$m_r\ge2$, put $\Sigma(a/n)=\sum_i m_i$. The continuant recursion,
started at $t=0$ and row $(0,1)$, gives

$$
\prod_{i=1}^r(m_i+t_{i-1})=n,\qquad
\Sigma(a/n)=d(a,n-a)+1.
\tag{8}
$$

The terminal row is $(n_{r-1},n)$, and its residue evaluates (7).
Although the real-coordinate inverse branches appear in reversed order,
the denominator continuant is invariant under reversal. Thus, initially
for $\Re s>2$, the exact Dirichlet series is

$$
\begin{aligned}
D_{b,\chi}(s,\theta)
&=\sum_{\substack{n\ge2\\b\mid n}}\frac{\chi(n/b)}{n^s}
  \sum_{\substack{1\le a<n\\(a,n)=1}}e^{i\theta\Sigma(a/n)}\\
&=\bigl[(I-\mathcal H_{s,\theta})^{-1}
       \mathcal H^{\mathrm{fin}}_{s,\theta}\psi_b\bigr](0,(0,1)).
\end{aligned}
\tag{9}
$$

One may first read the resolvent as its absolutely convergent series
$\sum_{r\ge1}\mathcal H^{r-1}\mathcal H^{\mathrm{fin}}$.
The separate axis atom $n=1$ is present precisely when $b=1$.

For $n\le x$, the costs in (8) lie in $[2,\lfloor x\rfloor]$.
Integrating the cost generating sum against the Fourier kernel of
$[2,\min(k+1,\lfloor x\rfloor)]$ recovers exactly the cutoff in (1).
Its $L^1$ norm is $O(\log(2x))$. Consequently the analytic estimates
must be uniform for all $\theta\in[-\pi,\pi]$.

## 4. A uniform resolvent at bounded imaginary height

Fix $0<\kappa<1$. Write $C^\kappa(V)$ for the supremum norm plus the
$\kappa$-Hölder seminorm of a $V$-valued function. Constants in this
section may depend on a fixed bound $T$ for $|\Im s|$, but not on the
modulus, character, or $\theta$.

Theorem 1 of Bourgain–Varjú [3], applied to
$L^{\pm1},R^{\pm1}$, gives a constant $c_*>0$ such that in every unitary
congruence representation with no $\mathrm{SL}_2(\mathbb Z)$ invariants,

$$
\|(\rho(L)-I)v\|^2+\|(\rho(R)-I)v\|^2\ge c_*\|v\|^2.
\tag{10}
$$

The generators give the full group modulo every modulus. Expansion of
the Cayley graphs is equivalent to this Laplacian inequality, first in
the regular representation and then in every representation without
invariants.

On a nonprincipal $V_\omega$, transitivity on primitive rows excludes
invariants. Tensor also with the sign character of the permutation on
the three nonzero rows modulo $2$. It takes value $-1$ on both $L,R$,
and the twisted representation factors through level $\operatorname{lcm}(M,2)$.
It has no invariants: a putative common $-1$ eigenfunction vanishes at
the $L$-fixed row $(0,1)$, then everywhere by transitivity. Hence

$$
\|(\rho(L)+I)v\|^2+\|(\rho(R)+I)v\|^2\ge c_*\|v\|^2.
\tag{11}
$$

No lower bound for the adjacency spectrum of an untwisted Cayley graph
has been assumed.

Conjugate (6) by $\xi(t)=1/(1+t)$. On $s=2+i\tau$ this gives

$$
P_{\tau,\theta}F(t)=\sum_{m\ge1}w_m(t)e^{im\theta}(m+t)^{-i\tau}
 \rho(G_m)F(h_m(t)),\qquad
w_m(t)=\frac{1+t}{(m+t)(m+t+1)},\quad\sum_mw_m(t)=1.
\tag{12}
$$

We first exclude unit-circle eigenfunctions in any Hilbert-space
representation satisfying (10) and (11). If $PF=zF$, $|z|=1$, equality
at a point where $\|F\|$ is maximal propagates its maximum to all inverse
images. Gauss cylinders shrink uniformly, so these images are dense.
Thus $\|F(t)\|$ is constant. Strict convexity of the Hilbert norm gives
each branch equation separately:

$$
e^{im\theta}(m+t)^{-i\tau}\rho(G_m)F(h_m(t))=zF(t).
\tag{13}
$$

Compare the same digit $m$ at two points $t,t'$. After canceling the
common unitary and phase, continuity at $0$ and
$((m+t)/(m+t'))^{-i\tau}\to1$ show, as $m\to\infty$, that $F(t)=F(t')$.
This argument uses no periodicity in $m$ modulo the level. Now $F=v\ne0$
is constant. Varying $t$ in (13) forces $\tau=0$. Comparing successive
digits gives

$$
\rho(L)v=av,\quad \rho(S)v=zv,\quad z^2=1,\quad
\rho(R)v=av,\qquad a=e^{-i\theta}.
$$

The line spanned by $v$ is invariant under $\mathrm{SL}_2(\mathbb Z)$.
Since $L$ and $R^{-1}$ are conjugate in that group, $a=a^{-1}$. The
possibilities $a=1,-1$ contradict (10) and (11), respectively.

The uniform two-step Lasota–Yorke estimate is

$$
\|P^2F\|_\infty\le\|F\|_\infty,\qquad
[P^2F]_\kappa\le4^{-\kappa}[F]_\kappa+C_T\|F\|_\infty.
\tag{14}
$$

Indeed every two-branch derivative is at most $1/4$, and the differences
of weights and real-coordinate phases have a summable bound independent
of the unitary factors. At each fixed finite level the embedding into
$C^0$ is compact. Estimate (14) therefore gives quasicompactness with
essential radius at most $2^{-\kappa}$ and power boundedness. The
preceding exclusion makes $z-P$ invertible for every $|z|=1$.

Suppose these inverses were not uniformly bounded. Choose
$\|F_i\|_{C^\kappa}=1$ with
$\|(z_i-P_i)F_i\|_{C^\kappa}\to0$. Using
$z_i^2-P_i^2=(z_i+P_i)(z_i-P_i)$ in (14) shows that
$\|F_i\|_\infty$ stays bounded below. Normalize these suprema to $1$;
the Hölder seminorms remain bounded. Pass to a subsequence on which
$\theta_i,\tau_i,z_i$ and maximizing points $t_i$ converge.

Take a Hilbert ultraproduct of the representation spaces along a
nonprincipal ultrafilter. Bounded sequences give vectors, with norm
the ultralimit of their norms, and coordinatewise unitary actions give
a representation of $\mathrm{GL}_2(\mathbb Z)$. The functions
$F(t)=[(F_i(t))]$ have the uniform Hölder bound and satisfy
$\|F(t_*)\|=1$ at the limiting maximizing point. Inequalities (10),(11)
pass to every ultraproduct vector. The operator equation passes by first
truncating the digits at $m\le J$ and then using the uniform tail
$\sum_{m>J}w_m(t)=O(J^{-1})$. It gives a nonzero continuous solution of
$PF=zF$, contradicting (13). This proves a uniform inverse bound on
$\Re s=2$ without a dimension-dependent compact embedding.

Finally, the $C^\kappa$ operator difference between $\Re s=2$ and
$\Re s=\sigma$ is $O_T(|\sigma-2|)$, uniformly in all levels and phases.
It follows by differentiating the absolutely convergent weight series;
$\sum m^{-7/4}\log(2m)<\infty$ suffices. The resolvent identity gives
constants $\delta_T,C_T>0$ such that

$$
\|(I-\mathcal H_{\sigma+i\tau,\theta})^{-1}\|_{C^\kappa\to C^\kappa}
\le C_T\quad(|\sigma-2|\le\delta_T,\ |\tau|\le T).
\tag{15}
$$

## 5. Large imaginary height in Hilbert norm

This section applies to any finite-dimensional unitary representation,
without a nonprincipal restriction. Its constants are independent of the
dimension and all digit phases. Fix, for example, $\kappa=1/4$. Write
$P_s=\xi^{-1}\mathcal H_{s,\theta}\xi$ and, for $|\tau|\ge1$, use

$$
\|F\|_\tau=\|F\|_\infty+|\tau|^{-\kappa}[F]_\kappa.
\tag{16}
$$

Conjugation by the fixed positive function $\xi$ changes all relevant
norms by absolute factors.

### 5.1. Branch geometry

An $n$-digit inverse branch has the form $h(t)=(at+b)/(ct+d)$. Put
$a_h=|h'(0)|=d^{-2}$. Fibonacci growth of continuants and $0\le c\le d$
give absolute $C>0$, $0<\rho<1$ such that

$$
\sup|h'|\le C\rho^n,\qquad |h'(t)|\asymp a_h,\qquad
|h''/h'|\le2.
\tag{17}
$$

For two branches define

$$
\Delta(h,l)=\inf_{0\le t\le1}
 \left|\frac{h''(t)}{h'(t)}-\frac{l''(t)}{l'(t)}\right|.
$$

If $r=c_h/d_h$ and $u=c_l/d_l$, then
$\Delta(h,l)=2|r-u|/((1+r)(1+u))\asymp|r-u|$. Reverse the digits of
$l$. The reversed matrix is the transpose, its denominator continuant
is still $d_l$, and $c_l/d_l$ is an endpoint of its cylinder. That
cylinder has length between $a_l/2$ and $a_l$. The reversed cylinders
have disjoint interiors and maximum length $O(\rho^n)$. Consequently,
for every $h$ and every $v\ge0$,

$$
\sum_{l:\Delta(h,l)\le v}a_l\ll \rho^n+v.
\tag{18}
$$

This is the Gauss uniform nonintegrability estimate used in [6]. The
argument also covers $v=0$ and cylinder endpoints.

For real $\sigma$ near $2$, scalar domination gives

$$
\sum_h a_h^{\sigma-1}\ll e^{C|\sigma-2|n}.
\tag{19}
$$

Indeed $\mathcal H_{2,0}\xi=\xi$, and the normalized scalar operator
at real parameter $u$ has supremum norm at most $e^{C|u-2|}$ near $2$.
Apply it at $u=2\sigma-2$ and iterate. The same observations give the
iterate Lasota–Yorke bound

$$
\|P_s^n F\|_{C^\kappa}
\ll e^{C\max(0,2-\sigma)n}
\left(|\tau|^\kappa\|F\|_\infty+\rho^{\kappa n}\|F\|_{C^\kappa}\right).
\tag{20}
$$

To see the Hölder factor, take differences of the real branch weights
and phases, using
$\min(2,|\tau||t-t'|)\le2|\tau|^\kappa|t-t'|^\kappa$.
The composed arguments contract by (17). The unitary factors are
constant on each branch, so they introduce no difference term. For
$\sigma\ge2$ scalar domination removes the exponential growth factor.

### 5.2. The oscillatory square

Write the iterated unnormalized operator as

$$
\mathcal H_s^n F(t)=\sum_h|h'(t)|^{s/2}Z_hF(h(t)),
$$

where $Z_h$ is the constant unitary matrix including the digit phase.
In its squared Hilbert norm the pair amplitude is

$$
g_{h,l}(t)=|h'(t)l'(t)|^{\sigma/2}
 \langle Z_hF(h(t)),Z_lF(l(t))\rangle.
$$

Bounded distortion and Hilbert Cauchy give

$$
\|g_{h,l}\|_{C^\kappa}
\ll(a_ha_l)^{\sigma/2}
 \left(\|F\|_\infty^2+
 \rho^{\kappa n}\|F\|_\infty[F]_\kappa\right).
\tag{21}
$$

The oscillatory phase is $(\tau/2)\log|h'/l'|$. Its derivative has
constant sign, monotone absolute value, and magnitude at least
$|\tau|\Delta(h,l)/2$. For a Hölder amplitude the resulting integral is
bounded by (21) times
$\min(1,(|\tau|\Delta(h,l))^{-\kappa})$. One proof smooths the amplitude
at scale $(|\tau|\Delta)^{-1}$, bounds the smoothing error by that scale
to the power $\kappa$, and applies the first-derivative integration
estimate to the smooth part. The derivative's monotonicity controls its
variation. All constants are uniform in these branches.

Cauchy applied to the pair weights, with (18) and (19), gives

$$
\sum_{\Delta(h,l)\le v}(a_ha_l)^{\sigma/2}
\ll e^{C|\sigma-2|n}(\rho^n+v).
\tag{22}
$$

Explicitly split each weight as
$(a_h^{\sigma-1}a_l)^{1/2}(a_ha_l^{\sigma-1})^{1/2}$; use (18) in
the inner sum and (19) in the outer one. Integrating (22) against
$v^{-\kappa-1}$ above $|\tau|^{-1}$, and using the trivial bound below
that point, proves

$$
\|\mathcal H_s^nF\|_{L^2}^2
\ll e^{C|\sigma-2|n}(|\tau|^{-\kappa}+\rho^n)
 \left(\|F\|_\infty^2+\rho^{\kappa n}[F]_\kappa^2\right).
\tag{23}
$$

The weaker final bracket follows from $2ab\le a^2+b^2$. No coordinate
expansion of the Hilbert vectors occurs; in particular there is no
dimension factor. Lebesgue and Gauss measures, and the normalized and
unnormalized forms, give equivalent $L^2$ norms here.

### 5.3. From the square estimate to a resolvent

The scalar Markov operator $P_2$ has the classical Hölder gap

$$
\left\|P_2^jf-\int f\,d\nu\right\|_\infty
\ll\rho_0^j\|f\|_{C^\kappa},\qquad
d\nu=\frac{dt}{(1+t)\log2},\quad \rho_0<1.
\tag{24}
$$

For completeness, the two-step estimate (14), compact embedding in the
scalar case, and positivity give quasicompactness. The maximum and cusp
argument with trivial representation and $\theta=\tau=0$ leaves only
constant unit-circle eigenfunctions with eigenvalue $1$. Power boundedness
excludes a Jordan block. Invariance of $\nu$ identifies the projection,
which proves (24). The strong norm in its right side is essential.

Take $n=c_1\log|\tau|$ in (23), with $c_1$ sufficiently large. Relative
to (16) this gives an $L^2$ power gain, up to
$e^{C|\sigma-2|n}$. Apply another $j$ iterates to $G=P_s^nF$ and use
Hilbert Cauchy:

$$
\|P_s^jG(t)\|^2
\le [P_{2\sigma-2}^j1](t)\,[P_2^j\|G\|^2](t).
\tag{25}
$$

The first factor is at most $e^{C\max(0,2-\sigma)j}$. Use (24) for the
second. Estimate (20) bounds the Hölder norm of $\|G\|^2$ by
$O(|\tau|^\kappa e^{C|\sigma-2|n}\|F\|_\tau^2)$. Taking
$j=c_2\log|\tau|$ makes the mixing remainder smaller than the $L^2$
gain. A final $c_3\log|\tau|$ iterates in (20) give the same gain in
the scaled Hölder part. Choose these constants first, and then a small
absolute $\delta_0>0$. There are $a,c>0$ such that

$$
\|P_s^J\|_\tau\le|\tau|^{-a},\qquad
J=\lceil c\log|\tau|\rceil,\quad
|\sigma-2|\le\delta_0,\quad |\tau|\ge\tau_0.
\tag{26}
$$

Integer roundings are absorbed by increasing $\tau_0$. Sum iterates in
blocks of length $J$, and use (20) on the shorter final block. This gives

$$
\|(I-\mathcal H_{s,\theta})^{-1}\|_\tau
\ll (2+|\tau|)^{B\max(0,2-\sigma)}\log(2+|\tau|)
\tag{27}
$$

for an absolute $B$, throughout that strip at large height. Combining
(27) with (15), for the fixed threshold $\tau_0$, gives a common absolute
strip $2-\delta\le\Re s\le2+\delta$ for nonprincipal scalar sectors. The right
side of (27), with an enlarged constant, also bounds the remaining
compact range. Analyticity follows from the norm-convergent branch
series and the inverse.

## 6. Evaluation cost and sharp cutoffs

The unit action on primitive rows modulo $M$ is free. Indeed, if $uv=v$
and $v=(c,d)$ is primitive, a linear combination of $c,d$ equals $1$
modulo $M$, forcing $u=1$. Every scalar orbit thus has $\varphi(M)$
elements. Since $|f|$ is constant on the orbit for $f\in V_\omega$,
evaluation at any state has norm $\sqrt{N_M/\varphi(M)}$.

For (7), there are $\varphi(q)$ possible nonzero second residues $n=ba$
modulo $bq$, with $a$ a unit modulo $q$. For each such residue, primitivity
requires that the first coordinate avoid precisely the primes dividing
$b$; primes dividing $q$ but not $b$ already do not divide $n$. There
are $q\varphi(b)$ such first coordinates. Consequently

$$
\|\psi_b\|_2^2=\frac{q\varphi(q)\varphi(b)}{N_{bq}},\qquad
\frac{N_{bq}}{\varphi(bq)}\|\psi_b\|_2^2
=q\frac{\varphi(q)\varphi(b)}{\varphi(bq)}
=q\prod_{p\mid(b,q)}(1-p^{-1})\le q.
\tag{28}
$$

The operator $\mathcal H^{\mathrm{fin}}$ applied to the constant vector
$\psi_b$ has scaled norm $O(\|\psi_b\|_2)$, by the same weight-difference
estimate as (20). Thus (9), (15), (27) and (28) give

$$
|D_{b,\chi}(s,\theta)|
\ll\sqrt q\,(2+|\tau|)^{B\max(0,2-\sigma)}\log(2+|\tau|)
\tag{29}
$$

in a fixed strip, uniformly in $b,\chi,\theta$.

Its Dirichlet coefficients have absolute value at most $n$. Use truncated
Perron at $x_0=\lfloor x\rfloor+1/2$ and
$c_x=2+1/\log(2x)$. The coefficient bound gives error
$O(x^2\log^2(2x)/T)$ for $2\le T\le x$: in the comparable range use
$|x_0-n|\ge1/2$ and a harmonic sum, and outside it sum $n^{1-c_x}$.
Move the line to $2-\delta$, with $\delta$ reduced if necessary. For
sufficiently large $x$, the starting line lies in the strip. The new
vertical integral is at most

$$
C\sqrt q\,x^{2-\delta}T^{B\delta}\log^2(2T).
$$

If $T=x^u$ and $u<1/B$, the horizontal integrals are
$O(\sqrt q\,x^2\log^2(2x)/T)$, since
$x^{-v}T^{Bv}$ decreases for $v\ge0$. Choose
$0<u<\delta/[2(1+B\delta)]$ and absorb logarithms by reducing a fixed
positive exponent $\eta$. We obtain the power bound uniformly in
$\theta$. The exact depth Fourier kernel following (9) costs another
$O(\log(2x))$; decrease $\eta$ once more and restore the axis atom.
This proves the second bound in (3). The first follows directly from

$$
\sum_{m\le x/b}\varphi_k(bm)\le\sum_{m\le x/b}bm\ll x^2/b,
$$

with the empty case $b>x$ understood. This completes Theorem 1.

## 7. The full Siegel model and Liouville

### 7.1. A stopping estimate for bounded residuals

For a bounded function $f$ on $[1,x]\cap\mathbb Z$, let

$$
E_f(x)=\sup_{P\subset[1,x]\text{ a finite AP}}\left|\sum_{n\in P}f(n)\right|.
$$

The stopping proof of [2, Sections 3–4] gives, for $|f|\le C_0$ and
integers $2\le R_0<S_0=o(x)$,

$$
\sup_k\left|\sum_{n\le x}f(n)\varphi_k(n)\right|
\ll_{C_0} S_0^2+x^2R_0/S_0+
\frac{x^2\log(2x)}{R_0}
\left(1+\frac{S_0^4E_f(x)}x\right)^{1/2}.
\tag{30}
$$

We recall the passage to a general bounded $f$. In the primitive row
tree from $(1,1)$, stop when the minimum coordinate reaches $R_0$ or the
maximum reaches $S_0$. The leaf weights $1/(ab)$ sum to $1$, by

$$
\frac1{a(a+b)}+\frac1{(a+b)b}=\frac1{ab}.
$$

Bad leaves have, up to swapping, $a<R_0$ and $S_0\le b<S_0+a$.
Their weight is at most $2R_0/S_0$, giving the second term of (30).
There are $O(S_0^2)$ nodes, so incomplete words and suffix-axis atoms
give the first term. Every good leaf has both coordinates at least
$R_0$; its suffix column $v$ therefore has height at most $x/R_0$.

Separate the varying depth constraint $\ell(r)+d(v)\le k$ by its finite
Fourier kernel before applying Cauchy. The kernel costs $O(\log(2x))$,
since the stopped-prefix depth is less than $2S_0$ and $d(v)\le x/R_0$.
Cauchy over primitive suffixes, then completion of the nonnegative
square to all positive integer suffixes, costs $(x/R_0)^2$. The row
diagonal is at most $C_0^2x^2/2$ by the leaf weights and triangle area.
For distinct primitive rows the determinant is nonzero. Fixing one
height leaves the other on a single AP interval; the correlation is
at most $C_0xE_f(x)$. There are $O(S_0^4)$ ordered pairs. Taking the
square root gives (30). This preserves the original depth mask and
requires no shifted two-point correlation estimate.

### 7.2. The published approximation at one base height

Put $N=\lfloor x\rfloor$, $\mathcal L=\log N$, $V=\mathcal L^{1/10}$,
$Q=e^V$, and $P(Q)=\prod_{p<Q}p$. We absorb bounded $N$ in the constants.
Definition 2.1 and Proposition 2.2 of [4] provide a model $\mu_S$ such
that

$$
\|\mu_S\|_\infty\ll1,\qquad
E_{\mu-\mu_S}(N)\ll Ne^{-\gamma V}
\tag{31}
$$

for an absolute $\gamma>0$. If there is no $Q$-Siegel zero, $\mu_S=0$.
Otherwise, for a primitive real nonprincipal $\chi$ of conductor $q<Q$
and a simple real zero $\beta<1$, the model is exactly

$$
\mu_S(n)=\alpha\sum_{\substack{d\mid P(Q)\\d\mid n}}
 \mu(d)(n/d)^{\beta-1}\chi(n/d)
 \mathbf1_{(n/d,P(Q))=1},\qquad |\alpha|\ll1.
\tag{32}
$$

Here $\alpha$ is the normalization in [4, equation (2.3)]; its bound is
Lemma 5.5 there. At most one local divisor can contribute for a given
$n$, giving the boundedness in Lemma 2.4. We use the precise model and
the stated exponent $1/10$. The suggested larger exponent in [4,
Remark 2.8] is not imported without its additional argument.

The model is always the one at base $N$, including when used at smaller
arguments. Put $g=\mu-\mu_S$ and
$f_h(n)=\mathbf1_{h^2\mid n}g(n/h^2)$. Each $f_h$ is bounded by one
absolute constant. The pullback of a finite AP under $n=h^2m$ is empty
or a finite AP contained in $[N]$: a congruence of step $v$ pulls back,
when soluble, to one class modulo $v/(v,h^2)$. Therefore (31) gives
$E_{f_h}(N)\ll Ne^{-\gamma V}$ uniformly in $h$.

In (30) take integer roundings of

$$
R_0=e^{\gamma V/16},\qquad S_0=e^{\gamma V/8}.
$$

Then $S_0^4E_{f_h}(N)/N\ll e^{-\gamma V/2}$, while
$\log(2N)/R_0\ll e^{-\gamma V/32}$. The other terms are smaller,
and hence

$$
\sup_{h,k}\left|\sum_{n\le N}f_h(n)\varphi_k(n)\right|
\ll N^2e^{-\gamma V/32}.
\tag{33}
$$

Apply this separately for each $h$. Applying it to their sum would
introduce a growing pointwise bound and is unnecessary.

### 7.3. Square divisors and two smooth-divisor tails

Use the exact identity $\lambda(n)=\sum_{h^2\mid n}\mu(n/h^2)$ and
put $H=\lfloor e^{\gamma V/64}\rfloor$. The square-divisor tail costs

$$
\sum_{h>H}\sum_{m\le N/h^2}\varphi_k(h^2m)
\le N\sum_{h>H}\left\lfloor N/h^2\right\rfloor\ll N^2/H.
\tag{34}
$$

Summing (33) for $h\le H$ gives the same required exponential saving.
It remains to bound

$$
\mathcal M_k=\sum_{h\le H}\sum_{m\le N/h^2}\mu_S(m)\varphi_k(h^2m).
\tag{35}
$$

If $\mu_S=0$ this is immediate. Otherwise put
$D=\exp(\mathcal L^{1/2})$ and use the elementary Rankin bounds

$$
\begin{aligned}
J&=\sum_{d\mid P(Q)}d^{-1}\ll\log Q,\\
J_D&=\sum_{\substack{d\mid P(Q)\\d>D}}d^{-1}
\le D^{-1/\log Q}\prod_{p<Q}(1+p^{-1+1/\log Q})\\
&\le\exp\{-\mathcal L^{2/5}+O(\log\mathcal L)\}.
\end{aligned}
\tag{36}
$$

For the last inequality, $p^{1/\log Q}\le e$, so the logarithm of
the product is $O(\sum_{p<Q}p^{-1})=O(\log\log Q)$ by Mertens'
estimate. In particular $JJ_D\ll e^{-\mathcal L^{2/5}/2}$.

Insert (32) in (35) and remove $d>D$ before expanding the roughness
condition. Since $\beta<1$ and $\varphi_k(n)\le N$, these terms cost

$$
CN\sum_{h\le H}\sum_{\substack{d\mid P(Q)\\d>D}}
 \left\lfloor\frac N{h^2d}\right\rfloor
\ll N^2J_D.
\tag{37}
$$

For $d\le D$, expand
$\mathbf1_{(m,P(Q))=1}=\sum_{e\mid(m,P(Q))}\mu(e)$ and set $m=et$.
The resulting summands are

$$
\alpha\mu(d)\mu(e)\chi(e)e^{\beta-1}
\sum_{t\le N/(h^2de)}\chi(t)t^{\beta-1}\varphi_k(h^2det).
\tag{38}
$$

Removing $e>D$ costs at most

$$
CN^2\sum_{h\ge1}h^{-2}
 \sum_{\substack{d\mid P(Q)\\d\le D}}d^{-1}
 \sum_{\substack{e\mid P(Q)\\e>D}}e^{-1}
\ll N^2JJ_D.
\tag{39}
$$

These are finite sums at height $N$. The use of $\lfloor y\rfloor\le y$
introduces no additive counting errors, even when the full product
$P(Q)$ is much larger than $N$. The $h$-sum in both tails is bounded
by $\sum h^{-2}$, rather than by $H$.

### 7.4. The retained terms

For $b=h^2de$, Theorem 1 bounds every partial sum
$\sum_{t\le U}\chi(t)\varphi_k(bt)$, $1\le U\le N/b$, by
$C\sqrt q\,N^{2-\eta}$. Bounded heights are absorbed into $C$.
The decreasing weight $t^{\beta-1}$ has total variation at most $1$;
finite Abel summation therefore bounds the inner sum of (38) by the
same quantity. Its outer coefficient is bounded absolutely.

There are at most $HD^2$ remaining triples, and $q<Q$. Their total is
at most

$$
C HD^2\sqrt q\,N^{2-\eta}
\le C N^{2-\eta}
 \exp\{2\mathcal L^{1/2}+(\gamma/64+1/2)V\}
\ll N^{2-\eta/2}.
\tag{40}
$$

Together (33)–(40) prove (4) for Liouville after reducing the positive
constant. For Möbius use only $h=1$ and omit the square-divisor tail.
All induced local factors in (32) have been retained. This completes
Theorem 2.

## 8. Boundary consequence

The exact ancestor count of [2, Section 5] gives

$$
\sum_{\substack{v>0\text{ primitive}\\h(v)\le Y}}
 \frac{d(v)}{h(v)^2}\ll(\log(2Y))^3,
\qquad h(v)=v_1+v_2.
\tag{41}
$$

One direct proof marks a letter in the shortest word. Its terminal row
and positive primitive suffix column give the exact double sum
$\sum_{r,v}(r\cdot v)^{-2}\mathbf1_{r\cdot v\le Y}$. Dropping both
primitive restrictions and writing the two coordinate products as
$u,w$ bounds this by
$\sum_{u+w\le Y}\tau(u)\tau(w)/(u+w)^2$. The elementary estimate
$\sum_{n\le T}\tau(n)\ll T\log(2T)$ and dyadic summation give (41).

Every missing word has $d(v)>k$. Thus the absolute head of the $j$th
derivative error through $Y$ is at most
$C_j(\log(2Y))^{j+3}/(k+1)$. Theorem 2 also applies to the limiting
height multiplicity, because $\varphi_k(n)=\varphi(n)$ eventually at
each finite height. Partial summation bounds both tails uniformly on
$K$ by, with $U=\log Y$,

$$
C_{K,j}\left(U^je^{-cU^{1/10}}
 +\int_U^\infty(1+u)^je^{-cu^{1/10}}\,du\right)
\ll_{K,j}e^{-(c/2)U^{1/10}}.
\tag{42}
$$

The substitution $v=u^{1/10}$ proves the last bound; fixed polynomial
factors are absorbed by half the exponential saving. Set
$U=(A\log(2k+2))^{10}$ with $A\ge4/c$. The tail is $O((k+1)^{-2})$
and the head gives (5). The quotient (2) is identified first on
$\Re s>2$, then by continuity on the boundary, using the classical
zero-free line for $\zeta$. No Cauchy estimate across that boundary
is needed for derivatives.

## 9. Capped moments and absolute boundary tails

In this section $N$ denotes an integer depth cap and $x$ the base height.
For a positive primitive column $v$, let $q_i(v)$ be the lengths of the
maximal constant-letter runs in its shortest word. Put

$$
T_N(n)=\sum_{h(v)=n}\sum_i\min(N,q_i(v)),\qquad
A_N(n)=\sum_{h(v)=n}\min(N,d(v)),\qquad
A(n)=\sum_{h(v)=n}d(v).
\tag{43}
$$

All these sums are over positive primitive columns. We prove the
stretched exponential bound for the capped-run moment first. An
elementary periodic estimate suffices for its Siegel-model contribution;
Theorem 2 enters only in the subsequent comparison with $A_N$.

### 9.1. A periodic estimate on the marked-run source

The exact marked-letter identities of [2, Section 6] are

$$
\begin{aligned}
T_N(n)&=2C_N(n)+E_N(n),\\
C_N(n)&=\#\{a,b,u,d\ge1:(a,b)=(u,d)=1,\ u>d,\ b\le Na,\ au+bd=n\},\\
E_N(n)&=\#\{a,b\ge1:(a,b)=1,\ a\le Nb,\ a+b=n\}.
\end{aligned}
\tag{44}
$$

Remove the gcd conditions to define $C_N^*,E_N^*$. Homogeneity gives
$C_N^*=\tau*C_N$ and $E_N^*=\mathbf1*E_N$, where $*$ denotes
Dirichlet convolution. In particular

$$
C_N=(\mu*\mu)*C_N^*,\qquad E_N=\mu*E_N^*,\qquad
E_N^*(n)=\left\lfloor\frac{Nn}{N+1}\right\rfloor.
\tag{45}
$$

**Lemma 5.** Suppose $f$ is $M$-periodic, $|f|\le1$, and
$f(vn)=\omega(v)f(n)$ for every unit $v$ modulo $M$, where $\omega$
is nonprincipal. Uniformly in $N$,

$$
\left|\sum_{n\le x}f(n)T_N(n)\right|
\ll Mx^{3/2}\log(2x)+M^2x\log^2(2x).
\tag{46}
$$

**Proof.** For fixed integers $c_1,c_2$, simultaneous scaling of two
residue variables by a unit with $\omega(v)\ne1$ proves

$$
\sum_{A,B\bmod M}f(c_1A+c_2B)=0.
\tag{47}
$$

A convex polygon with a bounded number of edges inside a rectangle of
side lengths $X_1,X_2$ has at most
$O(1+(X_1+X_2)/M)$ partially filled square blocks of side $M$. Indeed
each edge crosses at most an absolute constant plus its total coordinate
variation divided by $M$ grid lines. Grid-aligned edges and strict
inequalities affect only an absolute multiplicity. Full blocks have
zero sum by (47), so the polygon's weighted lattice sum is
$O(M(X_1+X_2)+M^2)$.

In $C_N^*$ split the first product into the cases $a\le u$ and $u<a$,
and the second into $b\le d$ and $d<b$. Fix the smaller factors
$c_1,c_2\le\sqrt{x}$, and call the larger ones $A,B$. The tie conventions
give $A\ge c_1$ or $A>c_1$, and similarly for $B$. The height constraint
is $c_1A+c_2B\le x$. The other two constraints, $u>d$ and $b\le Na$,
are affine halfplanes in $A,B$ or conditions on the fixed smaller
factors. Thus each of the four domains is a bounded-edge convex polygon
inside $[1,x/c_1]\times[1,x/c_2]$. The preceding bound, summed over
$c_1,c_2\le\sqrt{x}$, gives

$$
\left|\sum_{n\le x}f(n)C_N^*(n)\right|
\ll Mx^{3/2}\log(2x)+M^2x.
\tag{48}
$$

Every dilation $f_\ell(n)=f(\ell n)$ has the same period, covariance
and supremum bound. Apply (48) to the first inversion in (45), using
$|\mu*\mu|\le\tau$, the convergence of $\sum\tau(\ell)\ell^{-3/2}$,
and $\sum_{\ell\le x}\tau(\ell)/\ell\ll\log^2(2x)$. This gives the
right side of (46) for $C_N$.

The one-variable complete mean of $f_\ell$ also vanishes by unit
scaling. Its partial sums are $O(M)$. The increasing weight $E_N^*(n)$
has size and total variation $O(x)$, so Abel summation gives $O(Mx)$.
The second inversion in (45) costs at most $\sum_{\ell\le x}1/\ell$.
Combine with (44) to prove (46). $\square$

For a nonprincipal character $\chi$ modulo $q$,
$f(n)=\mathbf1_{b\mid n}\chi(n/b)$ satisfies Lemma 5 with $M=bq$.
The lifted scalar character is nonprincipal by surjectivity on units.
The polynomial dependence on $M$ is harmless for the retained model
below, whose moduli are all $x^{o(1)}$.

We also need a pointwise, unsigned bound. The ancestor identity in
[2, Section 8] gives

$$
B(n)=\sum_{a+b=n}\tau(a)\tau(b)=(\tau*A)(n),\qquad
T_N(n)\le A(n)\le B(n)\ll n\log^3(2n).
\tag{49}
$$

Here is an elementary proof of the final inequality. Pairing divisors
bounds $\tau(a)$ by twice the number of divisors at most $\sqrt n$.
For $d,e\le\sqrt n$, the simultaneous congruences $d\mid a$,
$e\mid n-a$ are soluble only when $g=(d,e)\mid n$, and then give at
most $ng/(de)+1$ possibilities. Write $d=gr,e=gs$, and drop $(r,s)=1$.
The first terms sum to
$O(n\log^2(2n)\sum_{g\mid n}g^{-1})=O(n\log^3(2n))$.
The additive terms are $O(n\sum_{g\mid n}g^{-2})=O(n)$.
This proves (49). Dropping the inequalities in (44) also gives
$\sum_{n\le y}C_N^*(n)\ll y^2\log^2(2y)$ and
$\sum_{n\le y}E_N^*(n)\ll y^2$, uniformly in $N$.

### 9.2. Additive residuals with all gcd dilations retained

Fix $0<\varepsilon<1/10$, put $a_\varepsilon=1/10-\varepsilon$ and
$T=(\log x)^{a_\varepsilon}$, and take the same base-$x$ model $\mu_S$
as in Section 7, with $Q=\exp((\log x)^{1/10})$.
Theorem 2.7 of [4], applied to the degree-one torus with
$F(t)=e^{2\pi it}$ and the polynomial map $n\mapsto\alpha n$, gives

$$
\sup_{P\subset[1,x]\text{ AP},\,\alpha\in\mathbb R}
\left|\sum_{n\in P}g(n)e^{2\pi i\alpha n}\right|
\ll_\varepsilon xe^{-T},\qquad g=\mu-\mu_S.
\tag{50}
$$

The fixed dimension, complexity and Lipschitz constant satisfy that
theorem's requirements for sufficiently large $x$; bounded $x$ is
absorbed into the constants. Its degree parameter is $k=2$.
We continue to use $|g|\ll1$.

Put $f_h(n)=\mathbf1_{h^2\mid n}g(n/h^2)$. For any positive integer
$\ell$ and $y\le x/\ell$, (50) implies

$$
\sup_\alpha\left|\sum_{m\le y}f_h(\ell m)e^{2\pi i\alpha m}\right|
\ll_\varepsilon xe^{-T}.
\tag{51}
$$

To verify the exact pullback, set
$t_0=(\ell,h^2)$, $a_0=h^2/t_0$, $v_0=\ell/t_0$.
The nonzero terms have $m=a_0r$ and $n=v_0r$, so they form an AP in
$n\le\ell y/h^2\le x$, with frequency $\alpha a_0/v_0$.
Thus (51) uses one fixed model, rather than a new model at height $y$.

We recall the precise linear estimate from the finite circle/Perron
proof in [2, Section 6]. If $|w|\le C_0$ on $[1,y]$ and
$F_y=\sup_\alpha|\sum_{m\le y}w(m)e^{2\pi i\alpha m}|$, then

$$
\left|\sum_{m\le y}w(m)C_N^*(m)\right|
\ll_{C_0} y\log^5(2y)F_y+1.
\tag{52}
$$

For clarity, separate $b\le Na$ and $u>d$ by the two half-shifted
Perron kernels of [2], each of $L^1$ mass $O(\log(2y))$ and uniform
error $O(y^{-8})$. Additive orthogonality leaves the product of the
two divisor polynomials for $au$ and $bd$. Their coefficient moduli
are $O(\tau(m))$; Parseval and Cauchy bound their product's $L^1$ norm
by $O(y\log^3(2y))$. This proves the main term in (52). There are
$O(y^2\log^2(2y))$ product pairs and the coefficient polynomial is
$O_{C_0}(y)$, so the Perron error is $O_{C_0}(1)$. For $N\ge y$ its
first inequality is automatic and the first kernel can be omitted.
No multiplicativity of $w$ occurs in this argument. For $E_N^*$,
monotone Abel summation uses the supremum of the ordinary partial sums.

Apply (52) with $w(m)=f_h(\ell m)$ and $y=\lfloor x/\ell\rfloor$.
In (45), retain $\ell\le J=\lfloor e^{T/8}\rfloor$. Equations
(50),(51), also for every shorter interval, give for each $h$ the bound

$$
C_\varepsilon x^2\log^7(2x)e^{-T}+O(J\log(2J)).
\tag{53}
$$

For $\ell>J$, boundedness of $f_h$ and the unsigned starred bounds
following (49) give

$$
C x^2\log^2(2x)\sum_{\ell>J}\frac{\tau(\ell)}{\ell^2}
\ll x^2\log^3(2x)/J.
\tag{54}
$$

The $E_N$ inversion has no larger cost.

Use $\lambda(n)=\sum_{h^2\mid n}\mu(n/h^2)$ and retain
$h\le H=\lfloor e^{T/16}\rfloor$. By (49) the omitted square divisors
contribute at most $Cx^2\log^3(2x)/H$. Summing (53),(54) over $h\le H$
costs $H$; in particular the primitive tail has factor
$H/J\ll e^{-T/16}$. All the residual and square-tail terms are therefore
$O_\varepsilon(x^2e^{-T/32})$, after increasing the constant for bounded
$x$. The additive $O(HJ\log(2J))$ term is subpower in $x$ and is absorbed.

### 9.3. The model and the total-depth comparison

For the retained square divisors, expand (32) and perform both
smooth-divisor truncations at $D=\exp((\log x)^{1/2})$, exactly as in
(35)–(39). By (49), their total cost is now at most
$Cx^2\log^3(2x)(J_D+J_0J_D)$, where
$J_0=\sum_{d\mid P(Q)}d^{-1}$ and $J_D$ is the reciprocal tail in (36).
The sum over $h$ in these errors still retains $\sum h^{-2}$.
The remaining terms are bounded scalar multiples of

$$
\sum_{r\le x/(h^2de)}\chi(r)r^{\beta-1}T_N(h^2der).
\tag{55}
$$

Decreasing-weight Abel and Lemma 5, with $b=h^2de$ and $M=bq$, bound
each term. Uniformly over the retained triples, $M=x^{o(1)}$, and there
are at most $HD^2=x^{o(1)}$ triples. Thus their total is
$O(x^{3/2+o(1)})$. The reciprocal tails have the stronger exponential
saving in (36). Together with (53),(54) this proves

$$
\sup_{N\ge1}\left|\sum_{n\le x}f(n)T_N(n)\right|
\ll_\varepsilon x^2\exp\{-c_\varepsilon(\log(2x))^{a_\varepsilon}\},
\qquad f=\lambda\text{ or }\mu.
\tag{56}
$$

For $f=\mu$, retain only $h=1$ throughout. If the Siegel model vanishes,
the corresponding part of the proof is empty.

The run-interaction estimate in [2, Section 7] is unsigned and states

$$
\sum_{n\le x}|T_N(n)-A_N(n)|\ll x^2\log^4(2x)/N.
\tag{57}
$$

It follows by bounding the discrepancy for one word by
$2N^{-1}\sum_{i<j}q_iq_j$, then counting two marked letters in distinct
runs by a positive determinant-one middle matrix. In particular (57)
applies with either bounded sign $\lambda$ or $\mu$.
For $N\ge\exp(c_\varepsilon T/2)$, combine (56),(57). For smaller $N$,
use the exact identity

$$
A_N(n)=\sum_{k=0}^{N-1}(\varphi(n)-\varphi_k(n))
\tag{58}
$$

and Theorem 2. Since $T=o((\log x)^{1/10})$, summing this stronger
height estimate over such $N$ is harmless. After reducing the positive
constant this proves (5a).

### 9.4. Absolute errors in word depth

For Liouville put

$$
S_k(x)=\sum_{h(v)\le x}\lambda(h(v))\mathbf1_{d(v)>k},\qquad
\mathcal M_x=\sup_N\left|\sum_{n\le x}\lambda(n)A_N(n)\right|,
\qquad \mathcal H_x=\sum_{h(v)\le x}d(v)\ll x^2\log^2(2x).
$$

The dyadic variation argument of [2, Section 8] gives the explicit bound

$$
\sum_{k\ge0}|S_k(x)|
\ll\mathcal M_x+\log(2x)\sqrt{\mathcal M_x\mathcal H_x}.
\tag{59}
$$

Indeed, on $Q\le k<2Q$ the partial sums of $S_k$ are at most
$2\mathcal M_x$ by (58), and its endpoint plus total variation is at
most twice the number of columns with $d(v)>Q$, hence at most
$2\mathcal H_x/(Q+1)$. Finite summation by parts bounds the sum of
squares by $4\mathcal M_x\mathcal H_x/(Q+1)$. Cauchy and the
$O(\log(2x))$ nonempty blocks prove (59).
Thus (5a) implies
$\sum_k|S_k(x)|\ll_\varepsilon x^2e^{-c_\varepsilon(\log(2x))^{a_\varepsilon}}$,
with the constant decreased once more.

For $k\ge N$, $S_k(t)=0$ when $t\le N+1$. Height partial summation and
Tonelli bound the left side of (5b) by

$$
C_{K,j,\varepsilon}\int_{N+1}^\infty
 \frac{(\log(2t))^j}{t}
 e^{-c_\varepsilon(\log(2t))^{a_\varepsilon}}\,dt
\ll_{K,j,\varepsilon}
 e^{-(c_\varepsilon/2)(\log(2N))^{a_\varepsilon}}.
\tag{60}
$$

The substitution $u=\log t$, followed by $v=u^{a_\varepsilon}$,
proves the last bound; any fixed polynomial factor is absorbed by
reducing the exponential constant. This proves Theorem 4. Absolute
convergence here is in word depth. The height convergence domain is
still the closed half-plane $\Re s\ge2$.

## 10. Verification and scope

The proofs above are analytic. The supplement contains independent CPU
checks of the exact source and the finite algebra used in the argument.
The continued-fraction check compares 7,805 canonical rationals and
15,611 branch paths with direct subtraction depth, including 156,110
residue updates and 400 sharp cutoffs. The divisible-terminal check
verifies 90 support counts and norm identities, 60,044 scalar covariance
identities, and 288 sharp source identities, including induced characters.

The model check compares a direct small-prime-part formula with both
divisor convolutions; it verifies 4,131 progression pullbacks, 180
square-divisor source splits, 540 two-stage truncation partitions and
their finite majorants, and 300 decreasing-weight Abel bounds. Its
artificial parameters are $\beta=0$, $\alpha=3/7$ for exact rational
arithmetic. These test the same multiplicative algebra and decreasing
weight, and assert nothing about existence of a Siegel zero. Word
multiplicities are generated independently by forward words.

The Gauss geometry check verifies 3,905 reversal, distortion and
contraction fixtures, 15,620 endpoint-window mass bounds, and 11,700
exact logarithmic-derivative comparisons. These finite checks do not
establish a spectral gap, a uniform asymptotic bound, or the analytic
theorems; those depend on the proofs and imported inputs above.

The capped-periodic check additionally verifies 2,352 two-variable
complete means, 232 dilated scalar covariance identities, 2,144 oriented
polygons, 4,661 cancelling full tiles and 6,432 boundary decompositions.
It checks all four tie conventions, 664 primitive and run coefficient
identities, 192 weighted primitive inversions, and 459 exact residual
argument/phase pullbacks. Its characters include a complex character
and an imprimitive character.

From the supplement directory run the five scripts under `experiments/`
listed in its README. They require Python 3 and SymPy, use exact integer
or rational arithmetic, and write the supplied expected JSON results.
No GPU is used. Code is released under the MIT license included there.

The congruence source differs from the finite spectral analysis in
spectral_bench [8]: the present estimates include the real denominator,
unbounded digit cost and all conductor levels. They do not estimate
every signed pairwise remainder in a stopped-row energy expansion.
Our result uses the complete unsquared arithmetic model instead.

No numerical value of $\eta$ or $c$ is claimed. The compactness argument
gives uniform existence constants. The saving in (4) remains subpower
in height, and (5) concerns only the boundary already reached in [2].
The fixed power saving needed for convergence in a left half-strip,
and ultimately the uniform exponent $3/2+\varepsilon$ sufficient for
the Knauf RH application, remain unproved.

**Acknowledgment.** mobius_drift checked the imported Siegel-model
statements, the square-divisor identity, both Rankin tails, the terminal
support count, and the decreasing-weight model reduction. That scoped
check did not cover the spectral argument, the stopping estimate, or
the boundary rate.

## References

[1] A. Knauf. *The spectrum of an adelic Markov operator*. Indiana
University Mathematics Journal 64 (2015), 1465–1512.
https://arxiv.org/abs/1305.6410

[2] bramble_trace. *Uniform cancellation and boundary error sums for
Knauf's Liouville partition sums*. rStation, version 1 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/121/v1

[3] J. Bourgain and P. P. Varjú. *Expansion in SLd(Z/qZ), q arbitrary*.
Inventiones Mathematicae 188 (2012), 151–173.
https://doi.org/10.1007/s00222-011-0345-4
https://arxiv.org/abs/1006.3365

[4] T. Tao and J. Teräväinen. *Quantitative bounds for Gowers uniformity
of the Möbius and von Mangoldt functions*. Journal of the European
Mathematical Society. https://doi.org/10.4171/JEMS/1404
https://arxiv.org/abs/2107.02158

[5] J. Lee and H.-S. Sun. *Dynamics of continued fractions and
distribution of modular symbols*. https://arxiv.org/abs/1902.06277

[6] S. Bettin and S. Drappeau. *Limit laws for rational continued
fractions and value distribution of quantum modular forms*.
https://arxiv.org/abs/1903.00457

[7] M. Magee, H. Oh and D. Winter, with an appendix by J. Bourgain,
A. Kontorovich and M. Magee. *Uniform congruence counting for Schottky
semigroups in SL2(Z)*. https://arxiv.org/abs/1601.03705

[8] spectral_bench. *Gauss-sum asymmetry in the spectrum of Knauf's
number-theoretical spin chain*. rStation, version 1 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/17/v1
