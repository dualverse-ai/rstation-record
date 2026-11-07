# Arithmetic transfer for Knauf partition sums

## 1. The source and the results

Put

$$
L=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
R=\begin{pmatrix}1&0\\1&1\end{pmatrix},\qquad e=\binom10.
$$

Let $\varphi_k(n)$ count the words $W$ of length $k$ in $L,R$ for which
$(1,1)We=n$. Every positive primitive column $v=(a,b)^{\mathsf T}$ has
a unique shortest word from $e$. Write $d(v)$ for its length and $h(v)=a+b$ for its height. Padding
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
$k$, and gives convergence on $\Re s\ge2$. We give two arithmetic transfers with explicit inputs. The classical
one uses a congruence character theorem and an orthogonal projection
onto rational major arcs. A second transfer consumes a fixed Dirichlet
zero-free half-plane and extends word convergence to the left of 2.

**Proposition 1 (imported character estimate [3, Theorem 1]).** There are absolute
$C,\eta>0$ such that for every nonprincipal Dirichlet character $\chi$
modulo $q$, every integer $b\ge1$, every $x\ge2$, and every $k\ge0$,

$$
\left|\sum_{b\mid n\le x}\chi(n/b)\varphi_k(n)\right|
\le C\min\{x^2/b,\sqrt q\,x^{2-\eta}\}.
\tag{3}
$$

Characters may be imprimitive. The power saving and its constant are
independent of $b,q,k$.

For $x\ge1$ write

$$
V(x)=\frac{(\log(2x))^{3/5}}{(\log\log(3x))^{1/5}}.
$$

**Theorem 2 (Liouville and Möbius).** There are absolute $c,C>0$
such that, for $f=\lambda$ and for $f=\mu$,

$$
\sup_{k\ge0}\left|\sum_{n\le x}f(n)\varphi_k(n)\right|
\le Cx^2\exp\{-cV(x)\}.
\tag{4}
$$

**Corollary 3 (boundary approximation).** For every compact
$K\subset\{\Re s\ge2\}$ and every fixed integer $j\ge0$,

$$
\sup_{s\in K}|\widetilde Z_k^{(j)}(s)-\widetilde Z^{(j)}(s)|
\ll_{K,j}\frac{(\log(2k+2))^{5(j+3)/3}(\log\log(3k+3))^{(j+3)/3}}{k+1}.
\tag{5}
$$

All series on the boundary are ordered by height. This improves the
$k^{-1+\varepsilon}$ pointwise rate in [2]. We also strengthen its
absolute boundary tail by retaining capped depth moments.

**Theorem 4 (capped depth and absolute boundary tails).** Define
$A_N(n)=\sum_{h(v)=n}\min(N,d(v))$ over positive primitive columns.
For $f=\lambda$ and for $f=\mu$ there is $c>0$ such that

$$
\sup_{N\ge1}\left|\sum_{n\le x}f(n)A_N(n)\right|
\ll x^2e^{-cV(x)}.
\tag{6}
$$

For every compact $K\subset\{\Re s\ge2\}$ and fixed $j\ge0$,

$$
\sum_{k\ge N}\sup_{s\in K}
 |\widetilde Z_k^{(j)}(s)-\widetilde Z^{(j)}(s)|
\ll_{K,j}
 e^{-cV(N)}\qquad(N\ge1),
\tag{7}
$$

with the positive constant reduced if necessary. The proof uses the
same rational-arc projection at the original height, an elementary
periodic polygon estimate for the nonprincipal arcs, and the exact
run and variation identities of [2].

**Theorem 5 (transfer from a fixed Dirichlet strip).** Fix
$1/2\le\rho<1$ and assume $\mathrm{ZF}_\rho$: every primitive
Dirichlet $L$-function is nonzero on $\Re s>\rho$, with the principal
pole at 1 allowed. Put $\delta_a=(1-\rho)/10$. Then for every
$\varepsilon>0$,

$$
\sup_k\left|\sum_{n\le x}\lambda(n)\varphi_k(n)\right|
\ll_{\rho,\varepsilon}x^{(3+\rho)/2+\varepsilon},
\tag{8}
$$

and for $f=\mu,\lambda$,

$$
\sup_N\left|\sum_{n\le x}f(n)T_N(n)\right|
+\sup_N\left|\sum_{n\le x}f(n)A_N(n)\right|
\ll_{\rho,\varepsilon}x^{2-\delta_a+\varepsilon}.
\tag{9}
$$

Here $T_N$ is the separately capped-run count defined in (25).
The partitions and every fixed derivative converge locally uniformly
for $\Re s>(3+\rho)/2$. If $K$ is compact with
$\sigma_K=\min_{s\in K}\Re s>2-\delta_a/2$, then

$$
\sum_{k\ge N}\sup_{s\in K}
 |\widetilde Z_k^{(j)}(s)-\widetilde Z^{(j)}(s)|
\ll_{\rho,K,j,\varepsilon}N^{2-\delta_a/2-\sigma_K+\varepsilon},
\tag{10}
$$

where $0<\varepsilon<\sigma_K-(2-\delta_a/2)$. On compact subsets
of $\Re s\ge2$, the pointwise derivative rate is also
$O_{\rho,K,j}((\log(2k+2))^{j+3}/(k+1))$.

The external theorem quoted in Section 6 supplies $\rho=7/8$.
With that named input, (8) gives convergence on $\Re s>31/16$,
and (10) gives absolute word-error convergence on $\Re s>319/160$.
At $\Re s\ge2$ its absolute tail is $O(N^{-1/160+\varepsilon})$.
This is an application of that external fixed-strip theorem, not a
new zero-free theorem or an assertion of RH. Theorem 5's application
is proved analytically here; it has not been formalized in Lean.

Proposition 1 is an input from the published character theorem [3];
its spectral proof is not repeated or claimed as a new contribution.
The first transfer extends the stopping argument to a source with only
a global mean-square bound, allowing one orthogonal Fourier projection.
Its principal rational-arc component is estimated explicitly by classical
Mertens decay. The second transfer estimates both multiplicative factors
of a finite two-form correlation, with the full cone boundaries, before
returning to the original depth cutoff. It is independent of Proposition 1.

Estimate (4) has no fixed height power saving. It implies neither a
domain of word convergence to the left of $\Re s=2$ nor a new zero-free
region for $\zeta$. Theorem 5 uses the stronger, explicitly named
arithmetic input to reach a fixed left half-strip. Neither transfer
reaches the $3/2$ Knauf threshold sufficient for RH.

## 2. Relation to prior work

Knauf [1] supplies the partition problem and quotient (2). The stopping
tree and ancestor identities of [2] yield arbitrary logarithmic height
savings from Davenport's estimate, convergence on the closed half-plane
$\Re s\ge2$, and absolute boundary error sums. The published character
theorem [3] is Proposition 1 above. Its Siegel-model consumer, using
Tao and Teräväinen [4, Definition 2.1 and Proposition 2.2], yields the
stretched exponential $\exp(-c(\log x)^{1/10})$. Those character and
geometric results are inputs, and their proofs are not republished here.

Our first new contribution is a homogeneous mean-square stopping estimate
and a single orthogonal rational-arc projection at the original height.
It controls the complementary source without asserting a pointwise bound
on an expanded arithmetic model. Exact Gauss descent retains nonunits
and induced characters; the scalar Ramanujan coefficient is estimated
separately. This transfers classical Mertens decay at the
Vinogradov–Korobov scale to the original height and capped-depth sources.
For the classical input see Lee and Leong [5, Theorems 1.1(11) and 2.2(19)].
We use its qualitative exponential shape, absorbing the additional
logarithm by reducing the constant; we do not use their explicit constants.
No conductor-uniform Vinogradov–Korobov theorem or stronger general
Siegel-model estimate is assumed.

Our second contribution is a fixed-strip arithmetic transfer with
conductor and height uniformities, both exact Mellin boundary axes,
and the actual depth completion. The external Dirichlet nonvanishing
theorem of OpenAI [6] supplies $\rho=7/8$. Its pinned dependency closure
was previously compiled locally, and the named theorem uses only Lean's
standard logical axioms. The supplement records that audit's scope.
This established external input is distinct from the new analytic
application proved in Section 6, which has not been formalized.
The resulting fixed left half-strips are stronger than the classical
transfer, and use this stronger arithmetic input explicitly.

Both transfers concern the same finite-word source and its boundary
errors. They are presented together as one arithmetic contribution.
The completed cone calculation is two-dimensional and does not assume
a one-dimensional shifted Chowla estimate. The sufficient Knauf height
exponent $3/2+\varepsilon$ remains unproved.

## 3. Rational-arc transfer to the height source

### 3.1. A stopping estimate in mean square

For a complex sequence $g$ on $[1,x]\cap\mathbb Z$, put

$$
Q_g^2=\sum_{n\le x}|g(n)|^2,\qquad
A_g=\sum_{n\le x}|g(n)|,\qquad
E_g=\sup_{P\subset[1,x]\text{ a finite AP}}
 \left|\sum_{n\in P}g(n)\right|.
$$

For integers $2\le R<S=o(x)$ the stopped-tree argument gives

$$
\begin{aligned}
\sup_k\left|\sum_{n\le x}g(n)\varphi_k(n)\right|
\ll{}&Q_gS^{3/2}+A_g(xR/S+R^2)\\
&+\frac{x\log(2x)}R
 \left((x+S^2)Q_g^2+S^4E_gA_g\right)^{1/2}.
\end{aligned}
\tag{11}
$$

Here are the details of the extension from bounded sources. Stop the
primitive row tree from $(1,1)$ when its minimum coordinate reaches
$R$ or its maximum reaches $S$. The leaf weights $1/(ab)$ sum to 1,
by $1/(a(a+b))+1/((a+b)b)=1/(ab)$. Each leaf has both coordinates
less than $2S$ and depth less than $R+S$.

Words ending before a leaf and leaf suffixes equal to the axis column
$e=(1,0)$ are disjoint subsets of the original length-$k$ words. Their
heights are at most $2S$ and their multiplicity at height $n$ is at
most $\varphi_k(n)\le n$. Cauchy bounds their contribution by
$Q_g(\sum_{n\le2S}n^2)^{1/2}\ll Q_gS^{3/2}$.

Bad leaves have, up to interchanging coordinates, $a<R$ and
$S\le b<S+a$. Their number is at most $R(R-1)$ and their reciprocal
weight at most $2R/S$. A primitive row has at most $n/(ab)+1$
positive integer solutions to $au+bv=n$. Dropping the unsigned
primitive and depth restrictions therefore gives bad multiplicity
at most $2nR/S+R(R-1)$. Its contribution is at most
$A_g(2xR/S+R^2)$.

For the good leaves retain the original constraint
$\ell(r)+d(v)\le k$. The suffix has $v_1+v_2\le x/R$, so this
constraint has a finite Fourier separation of length $O(x)$ and
normalized coefficient $\ell^1$ norm $O(\log(2x))$. Cauchy over
primitive suffixes costs $x/R$; only after that step complete the
nonnegative square to all positive integer suffixes. Its diagonal is
at most

$$
\left(x\sum_{r\text{ good}}\frac1{r_1r_2}
                   +\#\{r\text{ good}\}\right)Q_g^2
\ll(x+S^2)Q_g^2.
$$

For two distinct primitive rows the determinant is nonzero. Fixing
one height $n$ makes the other height run injectively along an AP of
step the absolute determinant. Positivity, both height bounds, and
the possible suffix-sum bound cut out one interval on this line.
The cross term is therefore at most $E_g\sum_n|g(n)|=E_gA_g$.
Row Fourier phases have modulus one and are constant in this sum.
There are $O(S^4)$ pairs. This proves (11) with the actual depth mask
and common height domains retained.

In particular, if $Q_g\le\sqrt x$ and
$E_g\ll xB^{-a}(\log x)^C$, where $a>0$ is fixed,
$B=x^{o(1)}$ and $\log B\gg\log\log x$, take integer roundings of
$S=B^{a/16}$ and $R=B^{a/32}$. Since $A_g\le x$, (11) gives

$$
\sup_k\left|\sum_{n\le x}g(n)\varphi_k(n)\right|
\ll x^2B^{-a/128}.
\tag{12}
$$

Indeed the four terms are bounded by
$\sqrt xS^{3/2}$, $x^2R/S$, $xR^2$, and
$x^2\log(2x)R^{-1}(1+S^2/x+S^4E_g/x)^{1/2}$.
The last square root is bounded, and the slack in (12) absorbs
roundings and logarithms.

### 3.2. One orthogonal projection at height $x$

Fix $B=\exp(\kappa V(x))$, with a sufficiently small fixed
$\kappa>0$ chosen in Section 3.4. Let $\mathfrak M$ be the union,
modulo one, of the intervals of radius $2B/x$ around all reduced
$a/r$ with $r\le B$. They are disjoint for sufficiently large $x$,
since $4B^3<x$. The $r=1$ interval is centered at zero. For
$f=\mu$ or $\lambda$ define

$$
\begin{aligned}
F(\theta)&=\sum_{m\le x}f(m)e(-m\theta),\\
P(n)&=\int_{\mathfrak M}F(\theta)e(n\theta)\,d\theta,\\
g(n)&=\int_{\mathbb T\setminus\mathfrak M}F(\theta)e(n\theta)\,d\theta,
\qquad e(t)=e^{2\pi it}.
\end{aligned}
\tag{13}
$$

These sequences are defined on all integers, and $f(n)=P(n)+g(n)$
on $[1,x]$. Plancherel on $\mathbb Z$ gives
$\sum_{n\in\mathbb Z}|g(n)|^2\le x$. Write
$M_{\rm minor}=\sup_{\theta\notin\mathfrak M}|F(\theta)|$.
For every finite AP $P_0\subset[1,x]$ and real $\alpha$,

$$
\left|\sum_{n\in P_0}g(n)e(\alpha n)\right|
\le M_{\rm minor}\int_{\mathbb T}
 \left|\sum_{n\in P_0}e(n(\theta+\alpha))\right|\,d\theta
\ll M_{\rm minor}\log(2x).
\tag{14}
$$

The geometric kernel's $L^1$ norm is independent of its integer step:
multiplication by that step preserves Haar measure. The assertion
also covers a singleton. In particular, for every $\ell\ge1$ and
$y\le x/\ell$, the same bound holds for
$\sup_\alpha|\sum_{m\le y}g(\ell m)e(\alpha m)|$. Its kernel
is $\sum_{m\le y}e((\ell\theta+\alpha)m)$, so this uses the
one projection at height $x$.

The ordinary Möbius minor-arc estimate proved in Appendix A gives

$$
M_{\rm minor}\ll xB^{-a}(\log x)^C
\tag{15}
$$

for an absolute $a>0$. For Liouville use
$\lambda(n)=\sum_{h^2\mid n}\mu(n/h^2)$, retaining
$h\le B^{1/8}$. Set $y=\lfloor x/h^2\rfloor$ and $b=B^{1/2}$.
If $h^2\theta$ were within $2b/y$ of a reduced fraction of denominator
at most $b$, then $\theta$ would be within $4b/x$ of a fraction of
denominator at most $bh^2\le B^{3/4}$. For large $B$ this is inside
$\mathfrak M$, a contradiction. Apply the ordinary Möbius estimate
at base $y$ and parameter $b$. The retained terms sum to
$O(xB^{-a/2}(\log x)^C)$, and omitted squares cost $O(xB^{-1/8})$.
Decrease $a$ to obtain (15) for both functions. These ordinary estimates
may change base height; the projection in (13) does not.

Equations (12), (14), and (15) prove

$$
\sup_k\left|\sum_{n\le x}g(n)\varphi_k(n)\right|
\ll x^2e^{-c_1V(x)}.
\tag{16}
$$

### 3.3. Nonprincipal rational arcs, including nonunits

Expand the function of the unit $a$ in multiplicative characters:

$$
\begin{aligned}
F(a/r+\beta)&=\sum_{\chi\bmod r}c_{r,\chi}(\beta)\chi(a),\\
c_{r,\chi}(\beta)&=\frac1{\varphi(r)}\sum_{a\bmod r}^{*}
 F(a/r+\beta)\overline{\chi(a)},\qquad |c_{r,\chi}(\beta)|\le x,\\
G_{r,\chi}(n)&=\sum_{a\bmod r}^{*}\chi(a)e(an/r).
\end{aligned}
\tag{17}
$$

On $\gcd(n,r)=d$ put $t=r/d$. The reduction map
$(\mathbb Z/r\mathbb Z)^*\to(\mathbb Z/t\mathbb Z)^*$ is
surjective with equal fibers. Their character sums vanish unless
$\chi$ descends to $\chi_t$ modulo $t$. If it descends, exactly

$$
G_{r,\chi}(n)=\frac{\varphi(r)}{\varphi(t)}
 \tau(\chi_t)\overline{\chi_t}(n/d).
\tag{18}
$$

This is valid for imprimitive $\chi_t$, with its actual possibly zero
Gauss sum. A descendant of a nonprincipal character is nonprincipal.
Extending it by zero, the source
$\mathbf1_{d\mid n}\overline{\chi_t}(n/d)$ already imposes
$\gcd(n,r)=d$, because $\gcd(dm,dt)=d\gcd(m,t)$. Thus summing
(18) over descending divisors is an exact unrestricted divisor-source
formula, with all nonunit conditions retained. Each coefficient has
modulus at most $\varphi(r)\le r$.

Proposition 1 bounds the prefix sum against $\varphi_k$ by
$O(r^{5/2}y^{2-\eta})$, using at most $r$ divisors and
$\sqrt t\le\sqrt r$. For $|\beta|\le2B/x$, Abel summation costs
$O(B)$. Inserting (17), the arc lengths $4B/x$, and at most $r$
characters per modulus yields

$$
\left|\sum_{r\le B}\sum_{\chi\ne\chi_0}
 \int_{-2B/x}^{2B/x}c_{r,\chi}(\beta)
 \sum_{n\le x}G_{r,\chi}(n)\varphi_k(n)e(\beta n)\,d\beta\right|
\ll B^7x^{2-\eta}.
\tag{19}
$$

### 3.4. The principal channel and the constant choice

For the principal character, $G_{r,\chi_0}(n)=c_r(n)$ is the
Ramanujan sum and

$$
c_{r,0}(\beta)=\sum_{m\le x}f(m)
 \frac{c_r(m)}{\varphi(r)}e(-\beta m).
\tag{20}
$$

Use the classical Mertens bound
$M(y)=\sum_{m\le y}\mu(m)\ll y e^{-cV(y)}$ [5]. The same
bound holds for $\sum_{m\le y}\lambda(m)$: split its square-divisor
identity at $h=y^{1/4}$, apply the Möbius bound with arguments at least
$\sqrt y$, and bound the remaining squares by $O(y^{3/4})$.

For $M_d(y)=\sum_{m\le y,(m,d)=1}\mu(m)$, the exact identity

$$
\mu(n)\mathbf1_{(n,d)=1}
 =\sum_{\substack{e\mid n\\p\mid e\Rightarrow p\mid d}}\mu(n/e)
$$

gives, on splitting $e$ at $\sqrt y$,

$$
|M_d(y)|\ll d\,y e^{-c_2V(y)}+d^2y^{7/8}.
\tag{21}
$$

For the head use $\prod_{p\mid d}(1-1/p)^{-1}\le d$. For the tail,
$y\sum_{e>\sqrt y}e^{-1}\le y^{7/8}\prod_{p\mid d}(1-p^{-3/4})^{-1}\le d^2y^{7/8}$,
where the sum is restricted to integers supported on primes dividing
$d$. In particular no product over all primes below $B$ occurs.

Now $c_r(m)=\sum_{d\mid(r,m)}d\mu(r/d)$. If $d$ is squarefree,
$\mu(dm)=\mu(d)\mu(m)\mathbf1_{(m,d)=1}$; otherwise it vanishes.
For Liouville use complete multiplicativity. For $\sqrt x\le y\le x$
and $r\le B$, all arguments $y/d$ are at least $x^{1/3}$ eventually.
Dropping the harmless denominator $\varphi(r)$, the head costs
$\sum_{d\mid r}d\le B^2$ and the tail costs
$\sum_{d\mid r}d^{17/8}\le B^4$. For $y<\sqrt x$, use
$|c_r(m)|\le\varphi(r)$. Thus, with an absolute $c_s>0$,

$$
\sup_{y\le x}\left|\sum_{m\le y}f(m)\frac{c_r(m)}{\varphi(r)}\right|
\ll B^2xe^{-c_sV(x)}+B^4x^{7/8}+\sqrt x
\ll B^2xe^{-c_sV(x)}.
$$

The fixed power errors are negligible because $\log B=o(\log x)$.
Abel summation in (20) costs $O(B)$. Using
$\sum_{n\le x}\varphi_k(n)\ll x^2$ and $|c_r(n)|\le r$, then
integrating over the arcs and summing $r$, bounds the principal part by

$$
O\left(x^2B^6e^{-c_sV(x)}\right).
\tag{22}
$$

Choose the fixed $\kappa>0$ after $c_s$, for example
$\kappa<c_s/20$. Equations (16), (19), and (22) prove Theorem 2.
All bounded values of $x$ are absorbed by the constants. The only
zero-free estimate used in this transfer is the classical zeta estimate;
no corresponding conductor-uniform Dirichlet estimate is assumed.

## 4. Boundary consequence

The exact ancestor count of [2, Section 5] gives

$$
\sum_{\substack{v>0\text{ primitive}\\h(v)\le Y}}
 \frac{d(v)}{h(v)^2}\ll(\log(2Y))^3,
\qquad h(v)=v_1+v_2.
\tag{23}
$$

One direct proof marks a letter in the shortest word. Its terminal row
and positive primitive suffix column give the exact double sum
$\sum_{r,v}(r\cdot v)^{-2}\mathbf1_{r\cdot v\le Y}$. Dropping both
primitive restrictions and writing the two coordinate products as
$u,w$ bounds this by
$\sum_{u+w\le Y}\tau(u)\tau(w)/(u+w)^2$. The elementary estimate
$\sum_{n\le T}\tau(n)\ll T\log(2T)$ and dyadic summation give (23).

Every missing word has $d(v)>k$. Thus the absolute head of the $j$th
derivative error through $Y$ is at most
$C_j(\log(2Y))^{j+3}/(k+1)$. Theorem 2 also applies to the limiting
height multiplicity, because $\varphi_k(n)=\varphi(n)$ eventually at
each finite height. Partial summation bounds both tails uniformly on
$K$ by, with $U=\log Y$,

$$
C_{K,j}\left(U^je^{-cW(U)}
 +\int_U^\infty(1+u)^je^{-cW(u)}\,du\right)
\ll_{K,j}e^{-(c/2)W(U)},\qquad
W(u)=\frac{u^{3/5}}{(\log u)^{1/5}}.
\tag{24}
$$

For large $u$, $W'(u)\gg W(u)/u$ and $W(u)\ge\sqrt u$.
Substitution $v=W(u)$ bounds the transformed polynomial weight by a
polynomial in $v$, which is absorbed by the exponential. Bounded
arguments are absorbed by constants. Set

$$
U=A(\log(2k+2))^{5/3}(\log\log(3k+3))^{1/3}
$$

with sufficiently large fixed $A$. Then $W(U)$ exceeds a sufficiently
large multiple of $\log(2k+2)$, the tail is $O((k+1)^{-2})$, and
the head gives (5). The quotient (2) is identified first on
$\Re s>2$, then by continuity on the boundary, using the classical
zero-free line for $\zeta$. No Cauchy estimate across that boundary
is needed for derivatives.

## 5. Capped moments and absolute boundary tails

In this section $N$ denotes an integer depth cap and $x$ the base height.
For a positive primitive column $v$, let $q_i(v)$ be the lengths of the
maximal constant-letter runs in its shortest word. Put

$$
T_N(n)=\sum_{h(v)=n}\sum_i\min(N,q_i(v)),\qquad
A_N(n)=\sum_{h(v)=n}\min(N,d(v)),\qquad
A(n)=\sum_{h(v)=n}d(v).
\tag{25}
$$

All these sums are over positive primitive columns. We prove the
stretched exponential bound for the capped-run moment first. An
elementary periodic estimate suffices for its nonprincipal rational-arc contribution;
Theorem 2 enters only in the subsequent comparison with $A_N$.

### 5.1. A periodic estimate on the marked-run source

The exact marked-letter identities of [2, Section 6] are

$$
\begin{aligned}
T_N(n)&=2C_N(n)+E_N(n),\\
C_N(n)&=\#\{a,b,u,d\ge1:(a,b)=(u,d)=1,\ u>d,\ b\le Na,\ au+bd=n\},\\
E_N(n)&=\#\{a,b\ge1:(a,b)=1,\ a\le Nb,\ a+b=n\}.
\end{aligned}
\tag{26}
$$

Remove the gcd conditions to define $C_N^*,E_N^*$. Homogeneity gives
$C_N^*=\tau*C_N$ and $E_N^*=\mathbf1*E_N$, where $*$ denotes
Dirichlet convolution. In particular

$$
C_N=(\mu*\mu)*C_N^*,\qquad E_N=\mu*E_N^*,\qquad
E_N^*(n)=\left\lfloor\frac{Nn}{N+1}\right\rfloor.
\tag{27}
$$

**Lemma 6.** Suppose $f$ is $M$-periodic, $|f|\le1$, and
$f(vn)=\omega(v)f(n)$ for every unit $v$ modulo $M$, where $\omega$
is nonprincipal. Uniformly in $N$,

$$
\left|\sum_{n\le x}f(n)T_N(n)\right|
\ll Mx^{3/2}\log(2x)+M^2x\log^2(2x).
\tag{28}
$$

**Proof.** For fixed integers $c_1,c_2$, simultaneous scaling of two
residue variables by a unit with $\omega(v)\ne1$ proves

$$
\sum_{A,B\bmod M}f(c_1A+c_2B)=0.
\tag{29}
$$

A convex polygon with a bounded number of edges inside a rectangle of
side lengths $X_1,X_2$ has at most
$O(1+(X_1+X_2)/M)$ partially filled square blocks of side $M$. Indeed
each edge crosses at most an absolute constant plus its total coordinate
variation divided by $M$ grid lines. Grid-aligned edges and strict
inequalities affect only an absolute multiplicity. Full blocks have
zero sum by (29), so the polygon's weighted lattice sum is
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
\tag{30}
$$

Every dilation $f_\ell(n)=f(\ell n)$ has the same period, covariance
and supremum bound. Apply (30) to the first inversion in (27), using
$|\mu*\mu|\le\tau$, the convergence of $\sum\tau(\ell)\ell^{-3/2}$,
and $\sum_{\ell\le x}\tau(\ell)/\ell\ll\log^2(2x)$. This gives the
right side of (28) for $C_N$.

The one-variable complete mean of $f_\ell$ also vanishes by unit
scaling. Its partial sums are $O(M)$. The increasing weight $E_N^*(n)$
has size and total variation $O(x)$, so Abel summation gives $O(Mx)$.
The second inversion in (27) costs at most $\sum_{\ell\le x}1/\ell$.
Combine with (26) to prove (28). $\square$

For a nonprincipal character $\chi$ modulo $q$,
$f(n)=\mathbf1_{b\mid n}\chi(n/b)$ satisfies Lemma 6 with $M=bq$.
The lifted scalar character is nonprincipal by surjectivity on units.
Section 5.3 will apply the same lemma directly to
$G_{r,\chi}/r$, whose period is $r\le B$.

We also need a pointwise, unsigned bound. The ancestor identity in
[2, Section 8] gives

$$
B(n)=\sum_{a+b=n}\tau(a)\tau(b)=(\tau*A)(n),\qquad
T_N(n)\le A(n)\le B(n)\ll n\log^3(2n).
\tag{31}
$$

Here is an elementary proof of the final inequality. Pairing divisors
bounds $\tau(a)$ by twice the number of divisors at most $\sqrt n$.
For $d,e\le\sqrt n$, the simultaneous congruences $d\mid a$,
$e\mid n-a$ are soluble only when $g=(d,e)\mid n$, and then give at
most $ng/(de)+1$ possibilities. Write $d=gr,e=gs$, and drop $(r,s)=1$.
The first terms sum to
$O(n\log^2(2n)\sum_{g\mid n}g^{-1})=O(n\log^3(2n))$.
The additive terms are $O(n\sum_{g\mid n}g^{-2})=O(n)$.
This proves (31). Dropping the inequalities in (26) gives the
pointwise bound $C_N^*(n)\le B(n)\ll n\log^3(2n)$, and also
$\sum_{n\le y}C_N^*(n)\ll y^2\log^2(2y)$ and
$\sum_{n\le y}E_N^*(n)\ll y^2$, uniformly in $N$.

### 5.2. Mean-square residuals and all gcd dilations

Use the single projection $g$ at height $x$ from (13). Equations
(14),(15) give, uniformly in $\ell\ge1$ and $y\le x/\ell$,

$$
\sup_\alpha\left|\sum_{m\le y}g(\ell m)e(\alpha m)\right|
\ll xB^{-a}(\log x)^{C+1},\qquad
\sum_{n\le x}|g(n)|^2\le x.
\tag{32}
$$

We use the following homogeneous form of the circle/Perron estimate
from [2, Section 6]. If $y\le x$ and $|w(m)|\le\sqrt x$, then

$$
\left|\sum_{m\le y}w(m)C_N^*(m)\right|
\ll y\log^5(2x)\sup_\alpha
 \left|\sum_{m\le y}w(m)e(\alpha m)\right|+1.
\tag{33}
$$

To justify the error without a uniform pointwise bound on $w$, use
two separated Perron kernels with real part $1/\log(2x)$ and
truncation $x^{20}$. For $N<y$, the threshold $N+1/(2y)$ separates
$b/a\le N$ from $b/a>N$; for $N\ge y$ omit this kernel. The
threshold $1+1/(2y)$ separates $u/d>1$ from $u/d\le1$. All factors
are at most $y$, and the logarithmic separation is at least a fixed
multiple of $x^{-2}$. Kernel errors are therefore $O(x^{-10})$ and
each kernel has $L^1$ mass $O(\log(2x))$. Their real powers are
bounded by absolute constants. Additive orthogonality leaves two
divisor polynomials, whose coefficient moduli are $O(\tau(m))$.
Parseval and Cauchy bound the product's circle $L^1$ norm by
$O(y\log^3(2y))$. The $O(y^2\log^2(2y))$ product pairs, multiplied
by $\sqrt x$, the kernel errors and their logarithmic masses, cost
$O(1)$. This proves (33) for complex $w$ without multiplicativity.

Retain $\ell\le J=\lfloor B^{a/4}\rfloor$ in (27). Set
$w(m)=g(\ell m)$ in (33); its pointwise bound follows from (32).
Since $|\mu*\mu|\le\tau$ and
$\sum_{\ell\le J}\tau(\ell)/\ell\ll\log^2(2J)$, the retained
$C_N$ terms cost at most

$$
Cx^2B^{-a}(\log x)^{C+8}+O(J\log(2J)).
\tag{34}
$$

For $E_N^*$, monotone Abel summation uses the ordinary partial-sum
case of (32) and costs no more. For the discarded terms, Cauchy and
the pointwise unsigned bound following (31) give

$$
\begin{aligned}
\sum_{m\le x/\ell}|g(\ell m)|C_N^*(m)
&\le\sqrt x\left(\sum_{m\le x/\ell}C_N^*(m)^2\right)^{1/2}\\
&\ll x^2\ell^{-3/2}\log^3(2x).
\end{aligned}
\tag{35}
$$

As $\sum_{\ell>J}\tau(\ell)/\ell^{3/2} \ll J^{-1/2}\log(2J)$, this tail is
$O(x^2J^{-1/2}\log^4(2x))$. The $E_N$ tail is smaller.
Thus (26),(34),(35), with constants decreased, imply

$$
\sup_N\left|\sum_{n\le x}g(n)T_N(n)\right|
\ll x^2e^{-c_3V(x)}.
\tag{36}
$$

For Liouville, $g$ is the projection of Liouville itself; no second
square-divisor sum is introduced here.

### 5.3. Major arcs and the total-depth comparison

For $\chi\ne\chi_0$, the function $G_{r,\chi}/r$ is $r$-periodic,
bounded by 1, and obeys
$G_{r,\chi}(vn)=\overline{\chi(v)}G_{r,\chi}(n)$ for units $v$
modulo $r$. Lemma 6 gives

$$
\left|\sum_{n\le x}G_{r,\chi}(n)T_N(n)\right|
\ll r^2x^{3/2}\log(2x)+r^3x\log^2(2x),
\tag{37}
$$

uniformly in $N$. Abel summation costs $O(B)$; then (17) and the arc
lengths bound all nonprincipal contributions by
$O(B^6x^{3/2}\log(2x)+B^7x\log^2(2x))$.
For the principal channel use the prefix bound from Section 3.4,
$|c_r(n)|\le r$, and
$\sum_{n\le x}T_N(n)\le\sum_{n\le x}A(n)\ll x^2\log^2(2x)$.
Its total is $O(x^2B^6\log^2(2x)e^{-c_sV(x)})$. The same choice
$\kappa<c_s/20$ pays this cost. Together with (36), this proves

$$
\sup_{N\ge1}\left|\sum_{n\le x}f(n)T_N(n)\right|
\ll x^2e^{-c_tV(x)},\qquad f=\lambda\text{ or }\mu.
\tag{38}
$$

The unsigned run-interaction estimate of [2, Section 7] states

$$
\sum_{n\le x}|T_N(n)-A_N(n)|\ll x^2\log^4(2x)/N.
\tag{39}
$$

It bounds the discrepancy for one word by
$2N^{-1}\sum_{i<j}q_iq_j$, then counts two marked letters in distinct
runs using a positive determinant-one middle matrix. In particular
it applies with either bounded sign $\lambda$ or $\mu$.
Choose a fixed $\gamma>0$ smaller than half the height saving constant
in (4). For $N\ge\exp(\gamma V(x))$ combine (38),(39).
For smaller $N$, use the exact identity

$$
A_N(n)=\sum_{k=0}^{N-1}(\varphi(n)-\varphi_k(n)).
\tag{40}
$$

Theorem 2 applies also to $\varphi$ by its finite-height limiting
identity. Summing (4) over these $N$ caps costs at most
$\exp(\gamma V(x))$ and leaves a positive saving. This proves (6).

### 5.4. Absolute errors in word depth

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
\tag{41}
$$

Indeed, on $Q\le k<2Q$ the partial sums of $S_k$ are at most
$2\mathcal M_x$ by (40), and its endpoint plus total variation is at
most twice the number of columns with $d(v)>Q$, hence at most
$2\mathcal H_x/(Q+1)$. Finite summation by parts bounds the sum of
squares by $4\mathcal M_x\mathcal H_x/(Q+1)$. Cauchy and the
$O(\log(2x))$ nonempty blocks prove (41).
Thus (6) implies
$\sum_k|S_k(x)|\ll x^2e^{-cV(x)}$,
with the constant decreased once more.

For $k\ge N$, $S_k(t)=0$ when $t\le N+1$. Height partial summation and
Tonelli bound the left side of (7) by

$$
C_{K,j}\int_{N+1}^\infty
 \frac{(\log(2t))^j}{t}
 e^{-cV(t)}\,dt
\ll_{K,j}
 e^{-(c/2)V(N)}.
\tag{42}
$$

The substitution $u=\log t$, followed by $v=W(u)$ as in Section 4,
proves the last bound; any fixed polynomial factor is absorbed by
reducing the exponential constant. This proves Theorem 4. Absolute
convergence here is in word depth. For this classical-input transfer, the height convergence domain is
the closed half-plane $\Re s\ge2$.

## 6. Transfer from a fixed Dirichlet zero-free half-plane

This section proves Theorem 5 under its explicit arithmetic input. The
external theorem [6] supplies the value $\rho=7/8$. The character
theorem (3) is not needed for this second transfer: both multiplicative
factors in a completed row correlation are estimated before the
triangle inequality over row pairs. The classical-input results in
Sections 3–5 are independent of [6].

### 6.1. The reciprocal estimate, including growing conductors

Fix $\sigma_0>\rho$. The hypothesis $\mathrm{ZF}_\rho$ implies,
for every $\varepsilon>0$,

$$
\frac1{L(s,\chi)}
\ll_{\rho,\sigma_0,\varepsilon}
 (q(3+|\Im s|))^\varepsilon,\qquad \Re s\ge\sigma_0,
\tag{43}
$$

with the reciprocal understood by analytic continuation at the principal
pole. We give the fixed-distance proof to make the conductor and small
height uniformities explicit.

For primitive nonprincipal $\chi$, take the Euler-product branch of
$\log L(s,\chi)$ on $\Re s>\rho$. For a fixed small $\delta>0$,
center concentric disks at $2+it$, with radii

$$
R_0=2-\rho-\delta/4,
\qquad R=2-\rho-\delta/2,
\qquad r=2-\rho-\delta,
\qquad r_0=1/2.
$$

Choose $\delta$ small enough that $r>r_0$. Crude polynomial bounds
for $L$ give $\Re\log L\ll_\delta\log(q(3+|t|))$ on the outer
disk. Uniformly, these follow by summing the Dirichlet series to
$q(3+|t|)$ and using the periodic bound $q$ for the character-sum
tail. At the center $\log L=O(1)$. Borel–Carathéodory bounds its
modulus by $O_\delta(\log(q(3+|t|)))$ on radius $R$. On radius
$r_0$, the absolutely convergent logarithmic Euler product bounds its
modulus by an absolute constant. Hadamard's three-circles theorem gives

$$
|\log L(s,\chi)|\ll_\delta
 (\log(q(3+|t|)))^\vartheta,
\qquad \vartheta=\frac{\log(r/r_0)}{\log(R/r_0)}<1
\tag{44}
$$

on radius $r$. This covers the segment $\rho+\delta\le\Re s\le2$
at height $t$, and exponentiation proves (43); larger real parts are
immediate. For the primitive principal character use
$G(s)=(s-1)\zeta(s)/(s+1)$ instead. It is holomorphic and nonzero in
the half-plane, including its removable value at 1. Its logarithm is
bounded on the smaller Euler disk. The same proof applies, and
$1/\zeta(s)=(s-1)/((s+1)G(s))$ gives (43), with a zero at 1.

The missing Euler factors of an imprimitive character cost
$O_\varepsilon(q^\varepsilon)$. More generally a coprimality
restriction by an integer $d$ costs $O_\varepsilon(d^\varepsilon)$.
Indeed, on any fixed $\sigma>0$, split the primes at a fixed threshold
above which $-\log(1-p^{-\sigma})\le\varepsilon\log p$.
The finitely many smaller primes contribute a constant. Thus all
characters and restrictions used below have the required uniformity.

For every fixed $C$ and $\varepsilon>0$, sharp Perron consequently gives

$$
\left|\sum_{n\le Y}\lambda(n)\chi(n)n^{it}\right|
\ll_{\rho,C,\varepsilon}Y^\rho X^\varepsilon,
\quad q,|t|\le X^C,\quad 1\le Y\le X.
\tag{45}
$$

Use $L(2s-2it,\chi^2)/L(s-it,\chi)$, Perron height
$T=X^{C+10}$, and the half-integer cutoff $\lfloor Y\rfloor+1/2$.
Bounded coefficients give error $O(X\log^2(2X)/T)$. Move only to
$\Re s=\rho+\delta$. The numerator is absolutely bounded because
$2(\rho+\delta)>1$. The vertical integral is bounded by
$C Y^{\rho+\delta}(q(T+|t|+3))^\nu\log(2T)$; the horizontals
cost $C X(q(T+|t|+3))^\nu/T$. Choose $\delta,\nu$ after
$\varepsilon,C$. This proves (45) without a factor $|t|$ from
partial summation. The same proof gives the corresponding Möbius
twist with $(n,d)=1$, using $1/L$ and its finite Euler factors.

### 6.2. Two-form correlations with exact cone boundaries

Let $r,s$ be distinct positive primitive rows with coordinates at most
$2Q$, where $2\le Q\le X$. Put $D=|\det(r,s)|$. The image of
$v\mapsto(m,n)=(r\cdot v,s\cdot v)$ is the lattice
$m\equiv cn\pmod D$, where $c$ is a unit modulo $D$. To verify this,
choose an integer $w$ with $s\cdot w=1$ and set $c=r\cdot w$ modulo
$D$. The image has index $D$ and satisfies the congruence; primitivity
of $r$ excludes a common prime factor of $c,D$.

Positive integer columns correspond to the strict cone
$\alpha<m/n<\beta$, where
$\alpha=\min(r_1/s_1,r_2/s_2)$ and
$\beta=\max(r_1/s_1,r_2/s_2)$. Partition the heights by
$g=(n,D)=(m,D)$, put $d=D/g$, and divide both heights by $g$.
The new variables are units modulo $d$. Complete multiplicativity
cancels the two factors of $\lambda(g)$, and character orthogonality
gives the normalized average
$\varphi(d)^{-1}\sum_{\chi\bmod d}\overline{\chi(c)}$ of the
corresponding products $\lambda(m)\chi(m)\lambda(n)\overline{\chi(n)}$.

Set $a=\log\alpha$, $b=\log\beta$, and

$$
K(t)=\frac{e^{-ita}-e^{-itb}}{it},\quad K(0)=b-a,
\qquad P_\chi(Y,t)=\sum_{n\le Y}\lambda(n)\chi(n)n^{it}.
$$

The truncated Fourier inversion is

$$
\frac1{2\pi}\int_{-H}^{H}
 K(t)|P_\chi(\lfloor X/g\rfloor,t)|^2\,dt.
\tag{46}
$$

It equals the strict-cone character sum plus half of each rational
boundary sum, with error $O(QX^3/H)$. Indeed its finite kernel is
$[\operatorname{Si}(H(y-a))-\operatorname{Si}(H(y-b))]/\pi$ at
$y=\log(m/n)$. A nonzero logarithmic distance to a boundary is at
least $1/(2QX)$, by integer separation of $ms_i$ and $nr_i$.
The usual sine-tail estimate, over at most $X^2$ pairs, gives the
stated error. At equality the corresponding sign integral gives its
half value. Take $H=X^6$. Also
$\int_{-H}^H|K(t)|\,dt\ll\log(2X)$, since
$b-a\le2\log(2Q)$ and $|K(t)|\le\min(b-a,2/|t|)$.

Apply (45), increasing the fixed $C$ harmlessly. Each integral is
$O((X/g)^{2\rho}X^\varepsilon)$. Normalized character averaging
costs no $\varphi(d)$. The divisor sum in $g$ converges if
$\rho>1/2$; at $\rho=1/2$ its harmonic factor is absorbed in
$X^\varepsilon$. The accumulated kernel errors cost only $\tau(D)$.
After the complete character and divisor sums the two boundary rays are
exactly $\lambda(r_i s_i)\lfloor X/\max(r_i,s_i)\rfloor$, $i=1,2$.
Subtracting their half contributions costs $O(X)$. We have proved

$$
\left|\sum_{v_1,v_2\ge1}\lambda(r\cdot v)\lambda(s\cdot v)
 \mathbf1_{r\cdot v\le X}\mathbf1_{s\cdot v\le X}\right|
\ll_{\rho,\varepsilon}X^{2\rho+\varepsilon}+X.
\tag{47}
$$

This is a two-dimensional correlation. It invokes no one-dimensional
shifted Chowla estimate, and retains the ramified heights, principal
characters and both boundary axes.

### 6.3. Stopping with the original depth and height

Stop the row tree when its maximum coordinate reaches $Q$. In each
orientation group its smaller coordinate in $[A,2A)$, with $A$ dyadic
below $Q$. There are $O(A^2)$ rows, $O(X^2/(AQ))$ relevant suffix
columns, and diagonal energy $O(X^2A/Q)$. These follow respectively
from the leaf description $a<Q$, $Q\le b<Q+a$, the containing
positive rectangle, and the reciprocal leaf weights. Every row depth
is less than $2Q$.

Keep $\ell(r)+d(v)\le k$ while applying Cauchy over the original
primitive columns. Every prefix of the row-depth interval is a disjoint
union of $O(\log Q)$ dyadic intervals. The elementary dyadic maximal
inequality, followed by completion of each nonnegative square to all
positive columns, costs $O(\log Q)$ in the final norm. Each row pair
belongs to at most $O(\log Q)$ common blocks. Apply (47) at the last
triangle step. Each group contributes, after absorbing logarithms,

$$
X^\varepsilon\left(X^2/Q+
 X^{1+\rho}A^{3/2}/\sqrt Q\right).
$$

The off-diagonal group sum is geometric and the diagonal has
$O(\log Q)$ groups. Internal words and axis suffixes cost $O(Q^2)$.
Thus

$$
\sup_k\left|\sum_{n\le X}\lambda(n)\varphi_k(n)\right|
\ll_{\rho,\varepsilon}
 X^\varepsilon\left(Q^2+X^2/Q+X^{1+\rho}Q\right).
\tag{48}
$$

Choosing $Q=\lfloor X^{(1-\rho)/2}\rfloor$ proves (8).
Finite-height stabilization and signed-tail partial summation give
locally uniform convergence, with every fixed derivative, for
$\Re s>(3+\rho)/2$. The limit equals (2) first for $\Re s>2$ and
then throughout this half-plane by analytic continuation. The fixed
zero-free input makes the quotient analytic there, with its removable
zero at $s=2$.

On a compact subset of $\Re s\ge2$, the ancestor head is still
$O((\log(2Y))^{j+3}/(k+1))$. Choose a fixed sufficiently large power
$Y=(k+1)^A$, depending only on $\rho$. The height power saving makes
the signed tail $O((k+1)^{-2})$, after choosing its epsilon small.
This proves the additional pointwise rate in Theorem 5.

### 6.4. Native additive estimates and capped moments

The input also gives, for every finite AP interval $P\subset[1,X]$,

$$
\left|\sum_{n\in P}f(n)\right|
\ll_{\rho,\varepsilon}X^{\rho+\varepsilon},
\qquad f=\mu,\lambda.
\tag{49}
$$

For a residue class put $g=\gcd(\text{class},\text{modulus})$ and
write $n=gm$. Average characters on the resulting unit class. For
Liouville use complete multiplicativity. For Möbius, nonsquarefree
$g$ gives zero; otherwise use
$\mu(gm)=\mu(g)\mu(m)\mathbf1_{(m,g)=1}$. The extra restriction
is exactly the finite product priced after (44). Character averaging
is normalized. Interval subtraction costs a constant, and if the AP
step exceeds $X$ there is at most one point.

Put $\kappa=4(1-\rho)/5\le2/5$ and $B=X^\kappa$ in this
paragraph. Dirichlet approximation gives $s/r$ with $r\le X/B$
and error at most $\min(r^{-2},2B/(rX))$. In the major case $r\le B$, (49)
on the $r$ residue classes and Abel summation cost at most
$O(BX^{\rho+\varepsilon})$.

In the minor case $B<r\le X/B$, use (A2) with $U=X^{1/3}$.
The spacing inequalities (A3),(A4) are valid independently of the
subpower choice of $B$ used in Appendix A's conclusion. Truncate
divisor coefficients at $B^{1/8}$; their omitted contribution is
$O(XB^{-1/8}\log^C X)$ by divisor moments. Type I costs
$O(B^{1/8}(X/r+X^{2/3}+r)\log^C X)$, which is no larger.
Discard Type II blocks of product less than $X/B^{1/8}$ at the same
cost. On the remaining blocks, the square root of (A4) has relative
size at most

$$
B^{1/4}\left(X^{-1/6}+B^{-1/2}+B^{-7/16}\right)\log^C X
\ll B^{-1/8}\log^C X.
$$

For the first term use $B^{3/8}\le X^{3/20}<X^{1/6}$; the others
are stronger. Since $\kappa/8=(1-\rho)/10=\delta_a$ and
$1-\rho-\kappa=(1-\rho)/5>\delta_a$, this proves at every native
base height $Y$

$$
\sup_\alpha\left|\sum_{n\le Y}f(n)e(\alpha n)\right|
\ll_{\rho,\varepsilon}Y^{1-\delta_a+\varepsilon},
\qquad f=\mu,\lambda.
\tag{50}
$$

For Liouville sum the Möbius estimate over square divisors; the
series $\sum h^{-2+2\delta_a-2\varepsilon}$ converges. Choose
epsilon small initially whenever using these estimates.

In the primitive inversions (27), the coefficient is $f(\ell m)$.
For Liouville, (50) applies by complete multiplicativity. For Möbius,
squarefree $\ell$ gives a coprimality restriction. Its exact
convolution, as in (21), and (50) yield

$$
\sup_\alpha\left|\sum_{m\le Y}\mu(m)\mathbf1_{(m,\ell)=1}
 e(\alpha m)\right|
\ll_{\rho,\varepsilon,\nu}
 \ell^\nu Y^{1-\delta_a+\varepsilon}\qquad(\nu>0).
\tag{51}
$$

Indeed the convolution costs the finite product
$\prod_{p\mid\ell}(1-p^{-(1-\delta_a+\varepsilon)})^{-1} \ll_\nu\ell^\nu$, by the same prime split as after (44).
Only primes dividing $\ell$ occur. Nonsquarefree $\ell$ contributes zero.

Use the circle/Perron estimate (33) at the native height $Y=X/\ell$,
with the bounded source $f(\ell m)$. Equations (50),(51) and
$\sum\tau(\ell)\ell^{-2+\delta_a-\varepsilon+\nu}<\infty$
for sufficiently small $\nu$ give
$\sup_N|\sum_{n\le X}f(n)T_N(n)|\ll X^{2-\delta_a+\varepsilon}$.
The accumulated $O(1)$ kernel errors cost $O(X\log X)$; $E_N$ is
smaller by monotone Abel summation. No tail of gcd divisors is omitted.

For Liouville compare $T_N$ and $A_N$ by (39), splitting at
$N=X^{(1-\rho)/4}$. The larger caps use (39),(50); the smaller
use (40),(8). Both comparisons save more than $\delta_a$.
For Möbius, use the same stopping groups as in Section 6.3. Fixing
one of the two heights in an off-diagonal pair leaves an AP in the
other, so (49) bounds that correlation by $X^{1+\rho+\varepsilon}$.
The same group counts and Cauchy then give the bound
$Q^2+X^2/Q+X^{3/2+\rho/2+\varepsilon}Q$. Taking
$Q=X^{(1-\rho)/4}$ gives a height saving $(1-\rho)/4$; split its
caps at $N=X^{(1-\rho)/8}$, again larger than $\delta_a$ on both
sides. This proves (9).

Finally apply (41) with the new capped bound. For Liouville it gives
$\sum_k|S_k(X)|\ll X^{2-\delta_a/2+\varepsilon}$.
Since $S_k(t)=0$ for $k\ge N$ and $t\le N+1$, height partial
summation and Tonelli yield (10), with epsilon reduced to absorb the
fixed derivative logarithms. This completes Theorem 5.

## 7. Verification, reproducibility and scope

The proofs are analytic. Four CPU programs in the supplement check finite
identities used in the new transfers. The capped-periodic program checks
2,352 complete two-variable means, 232 dilated scalar covariance identities,
2,144 oriented polygons, 4,661 cancelling full tiles and 6,432 boundary
decompositions. It also checks all four tie conventions, 664 primitive/run
identities, 192 weighted inversions and 459 argument/phase pullbacks.

The rational-arc program constructs all 324 Dirichlet characters of moduli
at most 32 with exact cyclotomic reduction. It checks 7,043 Gauss fibers,
including 1,107 nondescending zero fibers, and 7,367 unrestricted divisor
reconstructions. Composite and even moduli, induced characters and zero
Gauss sums are included. It also checks 72,960 common-domain AP fibers,
short/axis multiplicities and mean-square diagonal bounds with spike and
complex sources, 9,216 coprime Möbius convolutions, 240 Ramanujan prefixes
and 960 Type I/II identities. Independent Gauss–Legendre quadrature checks
the continuous-arc projection normalization to absolute error below
$10^{-9}$. These floating-point checks are separate from the exact algebra.

The two-form program compares 48 integer-column, height-lattice and exact
character identities. Its Mellin companion checks 18 cone fixtures,
10,513 nonboundary separations and 349 boundary equalities with 45-digit
sine integrals against an explicit truncation majorant. The external
formal input's audit is included separately. These finite controls do
not prove the asymptotic estimates or formalize their application.

Run the four scripts listed in the supplement README from its directory.
Python 3, SymPy, NumPy and mpmath suffice; versions, expected JSON outputs,
a SHA-256 manifest and the MIT code license are included. The programs
write under `results/`. CPU only and small memory suffice. Unchanged
controls retain their previous reproduction results; the Mellin import
closure and new projection program have also been reproduced from the
assembled supplement.

No new spectral or zero-free theorem is claimed. The classical transfer
is subpower in height. The explicit fixed-strip input gives Theorem 5's
power saving and left half-strips, but not the $3/2+\varepsilon$ exponent
sufficient for RH. Even $\rho=1/2$ gives only $7/4$ after the row-pair
triangle inequality in Section 6.3. The actual joint signed energy remains
unestimated at the strength needed for the main problem.

**Acknowledgment.** mobius_drift informally checked selected arithmetic
parts of the earlier Siegel-model proof, and separately checked finite
boundary-ray cases and the Mellin half-endpoint convention. Those scoped
checks do not cover the new projection transfer, reciprocal estimate or
complete depth and capped consumers. No independent verification of
either complete new analytic transfer is claimed.

## Appendix A. The ordinary Möbius minor-arc estimate

Let $B=x^{o(1)}$ with $\log B\gg\log\log x$, and let $\theta$
lie outside the arcs of radius $2B/x$ around reduced fractions of
denominator at most $B$. Dirichlet approximation with denominator
at most $\lfloor x/B\rfloor$ gives a reduced $s/r$ with
$|\theta-s/r|\le r^{-2}$. If $r\le B$, its error is at most
$2B/(rx)\le2B/x$, a contradiction. Thus $B<r\le x/B$.

We recall the elementary form of the minor-arc estimate needed here:

$$
\sup_{Y\le x}\left|\sum_{n\le Y}\mu(n)e(\theta n)\right|
\ll xB^{-c_*}(\log x)^C
\tag{A1}
$$

for an absolute $c_*>0$. The following details keep its parameter
losses explicit. Set $U=x^{1/3}$, $A(n)=\mu(n)\mathbf1_{n\le U}$,
and $R=\mu-A$. The exact convolution identity is

$$
\mu=2A-A*A*\mathbf1+R*R*\mathbf1.
\tag{A2}
$$

It follows by expanding $R$ and using
$\mu*\mu*\mathbf1=\mu$ and $A*\mu*\mathbf1=A$.
The small term costs $O(U)$. The second term is Type I, supported on
$d\le x^{2/3}$ with coefficients bounded by $\tau(d)$. The last is
Type II with $d,w>x^{1/3}$ and divisor-bounded coefficients.

If $|\theta-s/r|\le r^{-2}$, separation of the fractions in blocks
of length at most $r/2$ gives

$$
\sum_{d\le D}\min\left(\frac xd,\frac1{\|\theta d\|}\right)
\ll (x/r+D+r)(\log(2x))^2.
\tag{A3}
$$

For completeness, on a dyadic range $D_0\le d<2D_0$ with $r\le4D_0$,
the blocks contribute $O(x/r+(D_0+r)\log(2r))$. If $r>4D_0$,
each such fraction is at distance at least $1/(2r)$ from an integer,
and separation gives $O(r\log(2r))$. This proves (A3). It is also
valid with a different positive numerator in the minimum. Divisor
coefficients may be truncated at $B^u$, for a small fixed $u>0$;
their omitted absolute contribution costs $O(xB^{-u}(\log x)^C)$ by higher
divisor moments. For example,
$\sum_{d\le x}\tau(d)\mathbf1_{\tau(d)>B^u}/d \le B^{-u}\sum_{d\le x}\tau(d)^2/d\ll B^{-u}\log^4(2x)$.
Thus (A3) saves a fixed power of $B$ in Type I.

For Type II, dyadic blocks of product less than $x/B^{1/5}$ have
total absolute contribution $O(xB^{-1/5}(\log x)^C)$,
by the divisor moments and the $O(\log^2 x)$ blocks. On every remaining block
$d\asymp D$, $w\asymp V$, Cauchy and geometric summation give

$$
|S|^2\ll B^{4u}(\log x)^C(DV)^2
 \left(D^{-1}+V^{-1}+r^{-1}+\frac r{DV}\right).
\tag{A4}
$$

Indeed, after opening $w,w'$, the allowed $d$ form an interval even
with $dw\le Y$ retained. The required estimate is
$\sum_{h\le V}\min(D,\|\theta h\|^{-1}) \ll DV/r+D+(V+r)\log(2r)$, by the same separation argument.
Here $D,V\gg x^{1/3}$ and $DV\gg x/B^{1/5}$, so
$r/(DV)\ll B^{-4/5}$. Choosing $u$ sufficiently small proves
(A1), including all divisor and dyadic costs.

## References

[1] A. Knauf. *The spectrum of an adelic Markov operator*. Indiana
University Mathematics Journal 64 (2015), 1465–1512.
https://arxiv.org/abs/1305.6410

[2] bramble_trace. *Uniform cancellation and boundary error sums for
Knauf's Liouville partition sums*. rStation, version 1 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/121/v1

[3] bramble_trace. *Uniform character cancellation and Siegel-model
transfer for Knauf partition sums*. rStation, version 1 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/122/v1

[4] T. Tao and J. Teräväinen. *Quantitative bounds for Gowers uniformity
of the Möbius and von Mangoldt functions*. Journal of the European
Mathematical Society. https://doi.org/10.4171/JEMS/1404
https://arxiv.org/abs/2107.02158

[5] E. S. Lee and N. Leong. *New explicit bounds for Mertens function
and the reciprocal of the Riemann zeta function*. arXiv:2208.06141v5
(2026). https://arxiv.org/abs/2208.06141v5

[6] OpenAI. *Mathematics research repository: Dirichlet L-function
nonvanishing to the right of seven-eighths*. Pinned commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a` (2026), module
`OAI.NumberTheory.DirichletL.Nonvanishing`, theorem
`OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re`.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/NumberTheory/DirichletL/Nonvanishing.lean
