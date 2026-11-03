# Convex asymptotic profiles and explicit upper bounds for quadratic jets

Mira Cairn

## 1. The actual finite-budget index

Finite quadratic interpolation determinants use pure Hasse derivatives
at conjugate nodes. Their arithmetic contribution is governed by the
index of the lattice on which the priced derivatives are integral.
The all-order index is known [1,2], as are the exact first saturation
layer and its cutoff [3]. The evaluation endpoint, sublinear budgets
and some complete boundary quotients were determined in [4]. Finite
algebra approximations with an arbitrarily small cubic error, and the
complete first dyadic model, were obtained in [5]. The actual index at
a fixed positive interior derivative ratio was not shown to converge.

We prove that this actual normalized index has a limit. The limiting
profile is finite, nonincreasing and convex. The proof uses the universal
**column** modules: their derivative budgets add under multiplication,
with a binomial coefficient paying for a possible loss in the Hasse
price. This gives a subadditive function of two source labels and the
budget. An elementary convex homogenization argument then applies on
the original weighted triangle. No multiplication rule for the row
integrality lattices is assumed.

We also give an explicit finite upper bound by combining the known
first layer with the known whole-lattice derivative-band transport.
It controls every relative elementary-divisor depth and yields a closed
upper function for the new limiting profile. On the unchanged contract
$(p,K,R,J)=(3,17,28560,3769)$, the total index is at most
$25\,217\,029\,176$, compared with the evaluation ceiling
$58\,080\,244\,220$. An index ceiling is not additional lower arithmetic
credit for a selected determinant.

The limit formula is implicit. We do not evaluate the complete interior
profile or give an effective convergence rate. We prove that finite
polyhedral approximations decrease to it, but do not bound the number
of generators required for a prescribed error. The known endpoint bases
also give a closed upper profile by an explicit conical allocation. No new discriminant
endpoint, census or classification follows from these local results.

### 1.1. Notation and main theorem

Let $\mathcal O$ be the integers in the unramified quadratic extension
$F/\mathbb Q_p$, let $\sigma$ be its conjugation, and normalize
$v_p(p)=1$. Fix an integer $K\ge2$. For $R\ge2$ put
$$
\Lambda_R=\{(r,s)\in\mathbb Z_{\ge0}^2:r+Ks<R\},\qquad
C_R=\bigoplus_{\Lambda_R}\mathcal Oz^rw^s,\qquad V_R=FC_R.
$$
The Hasse derivatives hold $w$ fixed. Define
$$
\begin{aligned}
L_J(R)&=\{f\in V_R:
 p^{\lfloor j/p\rfloor}D_z^{[j]}f(z,\sigma(z))\in\mathcal O
 \text{ for all }z\in\mathcal O,\ 0\le j<J\},\\
E_J(R)&=\operatorname{length}_{\mathcal O}(L_J(R)/C_R),\qquad J\ge1.
\end{aligned}                                                     \tag{1}
$$
Evaluations separate $V_R$, so these lengths are finite; Section 3 also
proves this from a triangular column construction.

**Theorem 1 (actual volume and convexity).** For every prime $p$,
integer $K\ge2$ and real $\varepsilon>0$, there is a number
$\Phi_{p,K}(\varepsilon)$ such that, for every integer sequence
$J_R\ge1$ with $J_R/R\to\varepsilon$,
$$
\lim_{R\to\infty}\frac{E_{J_R}(R)}{R^3}
 =\Phi_{p,K}(\varepsilon).                                      \tag{2}
$$
The function $\Phi_{p,K}$ is finite, nonnegative, nonincreasing and
convex on $(0,\infty)$. In particular it is continuous there.
There is an explicitly defined nonnegative, convex, homogeneous
function $g_{p,K}$ on $\mathbb R_{\ge0}^3$ for which
$$
\Phi_{p,K}(\varepsilon)
=\int_{x+Ky<1}g_{p,K}(x,y,\varepsilon)\,dx\,dy
 +\frac{K+1}{6K^2(p-1)}-\frac1{3K}.                             \tag{3}
$$
All integrations here and below also impose $x,y\ge0$.

The definition of $g_{p,K}$ uses finite, exactly computable leading
coefficient ideals, given in (6) and (12). It is not a claim that an
arbitrary finite presentation has a Hilbert polynomial.

### 1.2. Classical ingredients and distinction

The exponential encoding of evaluation columns and its finite-difference
interpretation are classical Mahler-transform ideas; the broader
$p$-adic Fourier context is [6]. Leading-value semigroups, their convex
cones and volume asymptotics are standard in Newton–Okounkov theory;
see [7, Sections 1.1–1.4 and 2.1–2.4]. We prove the elementary
subadditive lemma needed here directly. No new general semigroup
asymptotic theorem is claimed.

The task-specific steps are the integral column product with the exact
prices $p^{\lfloor j/p\rfloor}$, an explicit leading-$Y$ element on the
original weighted order, and the exact factorial normalization relating
leading coefficient ideals to (1). These establish the hypotheses that
were missing from a direct row-lattice argument. Papers [1–5] provide
important endpoint and comparison inputs, but do not establish (2).
The new finite upper comparison in Section 6 uses the theorems of [3,5];
a preliminary author proof of that comparison appeared in [8].

## 2. Integral column series and their product

Choose $\theta\in\mathcal O$ whose residue is outside $\mathbb F_p$,
so $\mathcal O=\mathbb Z_p+\theta\mathbb Z_p$ and
$\theta'-\theta$ is a unit, where $\theta'=\sigma(\theta)$.
In the formal power series ring $F[[X,Y]]$ put
$$
\begin{aligned}
Z&=pX,&W&=p^KY,\\
U&=\exp(Z+W)-1,&V&=\exp(\theta Z+\theta'W)-1,\\
h_j&=p^{\lfloor j/p\rfloor}\frac{Z^j}{j!},&
\mathcal M_n&=\sum_{j=0}^nh_j\mathcal O[U,V],\quad n\ge0.
\end{aligned}                                                     \tag{4}
$$
All these series are coefficient-integral. Indeed, an exponential
coefficient at $X^rY^s$ has valuation at least
$r+Ks-v_p(r!)-v_p(s!)\ge0$, and
$v_p(h_j)=j+\lfloor j/p\rfloor-v_p(j!)\ge0$.
The exponentials are formal; no analytic convergence is used.

**Lemma 2 (column multiplication).**
$\mathcal M_n\mathcal M_m\subseteq\mathcal M_{n+m}$.

**Proof.** The algebra $\mathcal O[U,V]$ is closed under multiplication,
and
$$
h_jh_k=
\binom{j+k}{j}
p^{\lfloor j/p\rfloor+\lfloor k/p\rfloor-\lfloor(j+k)/p\rfloor}
h_{j+k}.                                                        \tag{5}
$$
The exponent on $p$ is either zero or minus one. In the latter case,
$j\bmod p+k\bmod p\ge p$, and the binomial coefficient is divisible
by $p$. This follows, for example, from the first-digit carry in
Legendre's factorial formula. Thus the scalar in (5) is integral.
$\square$

Order monomials increasingly by $(r+Ks,r)$. This is a multiplicative
well-order, and every monomial has finitely many predecessors. Define
$$
c(r,s,n)=\min\{v_p(a):
f\in\mathcal M_n,\quad
\operatorname{in}(f)=aX^rY^s\},                                 \tag{6}
$$
where $\operatorname{in}$ means the first nonzero monomial in this
order. Existence of the minimum is part of the next lemma.

**Lemma 3 (linear bound and subadditivity).** Put
$\gamma=K+v_p((K-1)!)$. For all nonnegative integers $r,s,n$,
$$
0\le c(r,s,n)\le r+\gamma s.                                    \tag{7}
$$
The function is nonincreasing in $n$, and
$$
c(r+r',s+s',n+n')\le c(r,s,n)+c(r',s',n').                       \tag{8}
$$

**Proof.** The first term of $U$ is $pX$. Set $b=v_p((K-1)!)$ and
consider the following element of $\mathcal O[U,V]$:
$$
F_Y=p^b\left[(1+V)-\sum_{i=0}^{K-1}\binom\theta iU^i\right].     \tag{9}
$$
Its displayed coefficients are integral because the numerator of
$\binom\theta i$ is integral and $v_p(i!)\le b$. On setting $Y=0$,
the identity $(1+V)=(1+U)^\theta$ shows that every pure $X$ term of
degree below $K$ vanishes. The coefficient of $Y$ is
$p^{K+b}(\theta'-\theta)$. At weight $K$, the monomial $Y$ precedes
$X^K$. Thus $F_Y$ has first monomial $Y$ and leading valuation
$\gamma$. Products $U^rF_Y^s$ prove (7). The nonempty set of attainable
nonnegative valuations has a minimum. Increasing $n$ enlarges the
module. Finally multiply elements attaining the two minima in (8) and
apply Lemma 2. Their first monomials multiply and their leading
valuations add. $\square$

## 3. The exact original-support index

Let $\mathfrak a_R=(X^rY^s:r+Ks\ge R)$. Project (4) into
$\mathcal O[[X,Y]]/\mathfrak a_R$, identified with
$\mathcal O^{\Lambda_R}$. Denote the projected module by
$\mathcal M_{n,R}$.

**Proposition 4 (exact leading-ideal formula).** For $J\ge1$,
$$
E_J(R)=\sum_{r+Ks<R}
\left[c(r,s,J-1)+v_p(r!)+v_p(s!)-r-Ks\right].                   \tag{10}
$$

**Proof.** At a linked node
$(z,w)=(x+\theta y,x+\theta'y)$, with $x,y\in\mathbb Z_p$, its
priced order-$j$ column is encoded by
$$
h_j(1+U)^x(1+V)^y.
$$
In the weighted quotient, binomial expansion is finite and its
coefficients $\binom xa\binom yb$ are integral. Conversely finite
differences at nonnegative integer $x,y$ express each $h_jU^aV^b$ as
an integral combination of these node columns. Hence their full span
is exactly $\mathcal M_{J-1,R}$, including all linked nodes.

The coefficient at $X^rY^s$ of the displayed series is the original
priced Hasse entry multiplied by
$$
\frac{p^{r+Ks}}{r!s!}.                                         \tag{11}
$$
The preceding construction retains precisely $\Lambda_R$ and all
original prices.

Filter the projected module by imposing zeros at the ordered earlier
coordinates. Its leading coefficient ideal at $(r,s)$ is exactly
$p^{c(r,s,J-1)}\mathcal O$. This ideal does not depend on the later
cutoff: any projected element is represented by a series in
$\mathcal M_{J-1}$, and its earlier coefficients are the same. Lemma 3
also supplies a triangular full-rank family. The successive quotient
ideals, or triangular elimination over a DVR, therefore give
$\operatorname{length}(\mathcal O^{\Lambda_R}/\mathcal M_{J-1,R})
=\sum c(r,s,J-1)$.

Let $D_{J,R}$ be the original universal column lattice. Its integrality
dual is $L_J(R)$, so
$\operatorname{length}(L_J/C_R)=
\operatorname{length}(\mathcal O^{\Lambda_R}/D_{J,R})$.
Applying the diagonal scaling (11) gives (10). $\square$

The values $c$ are ordered leading-ideal valuations, not individual
Smith exponents. Their sum is the index. All statements about the
ordinary denominator cap remain valid: the exact lattice (1) is being
computed, and no cap has been discarded from a finite model.

## 4. Convex homogenization and the limit

We state the elementary result used for the function in Lemma 3.

**Lemma 5 (subadditive homogenization).** Suppose
$a:\mathbb N^d\to[0,\infty)$ is subadditive and
$a(v)\le C\lVert v\rVert_1$. Define, using finite representations,
$$
g(x)=\inf\left\{\sum_i\lambda_i a(v_i):
\lambda_i\ge0,\ v_i\in\mathbb N^d,\ \sum_i\lambda_i v_i=x\right\}.
                                                                    \tag{12}
$$
Then $g$ is finite, nonnegative, convex and positively homogeneous.
If $v_N/N\to x\in(0,\infty)^d$, then
$a(v_N)/N\to g(x)$. Convergence is uniform for $v_N/N$ in a compact
subset of this open orthant.

**Proof.** Coordinate-axis representations give finiteness and a
linear upper bound. Combining or scaling representations proves
convexity and homogeneity. A finite convex function is continuous in
the open orthant, and $g(v)\le a(v)$ for integer $v$. This proves the
lower limit assertion.

For the upper limit, fix $0<\delta<1$ and choose a representation of
$(1-\delta)x$ whose cost is at most
$(1-\delta)g(x)+\delta$. Use $\lfloor N\lambda_i\rfloor$ copies of
each $v_i$. Their coordinatewise sum is at most $v_N$ for large $N$,
because every coordinate of $x$ is positive. The remaining integer
vector has norm at most
$N\delta\lVert x\rVert_1+o(N)+O(1)$. Subadditivity gives
$$
\limsup_N\frac{a(v_N)}N
\le(1-\delta)g(x)+\delta+C\delta\lVert x\rVert_1.
$$
Letting $\delta$ decrease to zero proves convergence. If compact
uniform convergence failed, a sequence of exceptions would have a
subsequence $v_N/N$ tending to an interior point, contradicting what
was just proved. $\square$

Apply (12) to $a(r,s,n)=c(r,s,n)$ and call the result $g_{p,K}$.
Since $c(0,0,n)=0$, adding a budget-axis vector shows that $g_{p,K}$
is nonincreasing in its third argument. Lemma 5 gives compact uniform
convergence away from $x=0,y=0$ at every positive budget ratio.

In (10), divide by $R^3$. The sum of $c/R$ converges to the integral
in (3). Indeed, compact uniform convergence treats the triangle away
from its coordinate axes; the omitted strips have arbitrarily small
area and are bounded by $x+\gamma y+O(R^{-1})$ using (7). Ordinary
Riemann sums treat the sloping boundary. Legendre's formula gives
$$
v_p(r!)+v_p(s!)=\frac{r+s}{p-1}+O_p(\log(R+2)),
$$
so its total error is $O_{p,K}(R^2\log(R+2))$. Finally,
$$
\int_{x+Ky<1}x\,dx\,dy=\frac1{6K},\qquad
\int_{x+Ky<1}y\,dx\,dy=\frac1{6K^2}.
$$
This proves (3). Nonnegativity follows from the finite indices.
Convexity and monotonicity follow by integration. Theorem 1 is proved.

### 4.1. Finite polyhedral upper approximations

For $N\ge1$, restrict (12) to integer generators
$r+s+n\le N$, including all three unit axes, and call the resulting
function $g_N$. These functions are rational polyhedral, bounded
between zero and $x+\gamma y$, and decrease pointwise to $g_{p,K}$.
The last assertion follows because every finite representation in
(12) occurs in some such generator set. Consequently
$$
\int_{x+Ky<1}g_N(x,y,\varepsilon)\,dx\,dy
 +\frac{K+1}{6K^2(p-1)}-\frac1{3K}
\downarrow\Phi_{p,K}(\varepsilon).                              \tag{13}
$$
For rational $\varepsilon$ each left-hand side can be evaluated by
rational polyhedral integration. Every required $c(r,s,n)$ is a finite
coefficient-module calculation: discard monomials after $(r,s)$ and
use the finitely many generators $h_jU^aV^b$ with
$a+b+j\le r+Ks$. This is a convergent upper procedure with no asserted
effective error rate. It does not license adding indices from unrelated
row constructions.

### 4.2. A certified finite cone that improves the endpoint bound

The finite-generator procedure can give a useful strict improvement
before the entire profile is known. At $p=2,K=4$, exact column
certificates in the supplement prove
$$
c(16,0,4)\le3,\qquad c(0,6,2)\le27,\qquad c(4,6,2)\le28.       \tag{13a}
$$
These are statements about the original formal column modules, with
no auxiliary support or changed Hasse price. To describe the
certificates, take $\theta^2+\theta+1=0$. Each is an explicitly listed
finite sum $\sum q_{jab}h_jU^aV^b$, with $j\le n$ and
$q_{jab}\in\mathbb Q(\theta)\cap\mathcal O$. Every rational coordinate
of $q_{jab}$ has an odd denominator. The coefficient at $X^rY^s$ is
checked using the original-node difference formula
$$
\frac{2^{r+4s}}{r!s!}
\sum_{j,a,b}q_{jab}2^{\lfloor j/2\rfloor}\binom rj
\sum_{x=0}^a\sum_{y=0}^b
(-1)^{a+b-x-y}\binom ax\binom by
(x+\theta y)^{r-j}(x+\theta'y)^s,                              \tag{13b}
$$
where terms with $j>r$ are zero. On the complete initial segment ending
at the target, this coefficient is zero except at that target, where
it equals $2^c$. The three segments have $45,85,114$ coordinates,
respectively. Thus the $244$ exact rational identities in the checker,
together with the odd denominators, certify (13a) without trusting a
modular rank computation or a floating-point solver.

Combine (13a) with the four endpoint rays proved in Section 5.1 and
the zero-cost budget axis. In the notation $(x,y,n;\text{cost})$ the
eight generators are
$$
\begin{gathered}
(1,0,0;1/2),\ (0,1,0;5),\ (1,0,1/2;1/6),\ (0,1,2;4),\\
(0,0,1;0),\ (16,0,4;3),\ (0,6,2;27),\ (4,6,2;28).
\end{gathered}
$$
Their conical cost $G$ is an upper bound for $g_{2,4}$. Exact rational
polyhedral integration at $\varepsilon=1/8$ gives
$$
\Phi_{2,4}(1/8)
\le\int_{x+4y<1}G(x,y,1/8)\,dx\,dy-\frac1{32}
=\frac{1807}{73728}=0.0245090060\ldots .                       \tag{13c}
$$
The endpoint bound alone is $295/9216=0.0320095486\ldots$.
Using the two new axis witnesses without the mixed witness gives
$4597/184320=0.0249403211\ldots$; the mixed column makes a further
strict improvement. The supplement enumerates the rational vertices
of the finite linear-programming dual, clips their affine regions on
the triangle, and integrates them exactly. Those dual constraints
describe this upper construction; they are not a global lower
certificate for $g_{2,4}$. Equation (13c) is a limiting index ceiling,
not a finite-index estimate or a value of the actual profile.

## 5. The known plateau and the remaining interior problem

In the middle chamber $p<K\le p^3$, the all-order formula [1,3] gives
$$
A_{p,K}:=\lim_{R\to\infty}\frac{E_\infty(R)}{R^3}
=\frac1{6K^2}+\frac1{6Kp(p^2-1)}.                               \tag{14}
$$
The exact saturation cutoff in [3] is $J_{\rm sat}=(p/K)R+O_{p,K}(1)$.
Thus $\Phi_{p,K}(\varepsilon)=A_{p,K}$ for $\varepsilon>p/K$,
and continuity from Theorem 1 gives equality also at $\varepsilon=p/K$.
The already published growing-power lower construction [3, Theorem 4,
equation (19)] implies, for $0<\varepsilon<p/K$ and
$\delta=1-K\varepsilon/p$,
$$
\Phi_{p,K}(\varepsilon)-A_{p,K}
\ge\frac{\delta^3}{6K^2(p^2-1)}.                               \tag{15}
$$
Its floor-sum proof applies to general $R$; the factor $1/6$ reflects
the normalization $R=KS$ used there. We do not claim this lower bound
or its row family as new. Equations (14)–(15) identify the exact start
of the plateau of the limiting profile.

The sublinear-budget comparison in [4, Theorem 2] remains the appropriate
endpoint input at $\varepsilon=0$; Theorem 1 itself concerns positive
ratios. Where $p^2/(p-1)\le K\le p^2(p-1)$, the exact evaluation formula
[4, Theorem 1] has leading value
$$
\frac{p}{6K^2(p-1)}+\frac1{6Kp(p-1)}.
$$
This last slope restriction is material, including $K=4$ when $p=2$.
No unrestricted evaluation formula is being inferred from it.

### 5.1. An explicit upper profile from the endpoint bases

In the evaluation chamber
$$
\frac{p^2}{p-1}\le K\le p^2(p-1),
$$
the preceding endpoint bases and the joint convexity of $g_{p,K}$ give
another closed bound. For $0<\varepsilon<p/K$, set
$\delta=1-K\varepsilon/p$. Then
$$
\Phi_{p,K}(\varepsilon)-A_{p,K}
\le \mathcal V_{p,K}(\varepsilon)
:=\frac{\delta^3}{6K(p^2-1)}
 +\frac{\delta^2(3-2\delta)}{6K^2(p-1)}.                         \tag{15a}
$$

Here is a derivation from the exact filtered bases, including the
required budget. The evaluation basis [4, Section 3] is triangular on
every initial segment of the weighted order. By the dual leading-ideal
calculation in Proposition 4, its exact leading coefficient cost is
$$
c(r,s,0)=r+Ks-v_p(r!)-v_p(s!)+s+v_p(s!)+m+v_p(m!),
\qquad m=\lfloor r/p^2\rfloor.
$$
The all-order analogue is
$$
c_\infty(r,s)=r+Ks-v_p(r!)-v_p(s!)+s+
 \sum_{i\ge1}\left\lfloor r/p^{2i+1}\right\rfloor.
$$
Here $c_\infty$ denotes the eventual value at a fixed label. Thus the
asymptotic evaluation coefficient costs are
$$
a_E=1-1/p,\qquad b_E=K+1
$$
on the $x$ and $y$ axes at zero budget. The corresponding all-order
costs from [1,3] are
$$
a_A=1-\frac1{p-1}+\frac1{p(p^2-1)},\qquad
b_A=K+1-\frac1{p-1}.
$$
A coefficient at $(r,s)$ is already in the all-order projected module
when the derivative budget saturates the triangle $R=r+Ks+1$.
Equation (16) below therefore allows the all-order axis costs with
budget rates $p/K$ and $p$, respectively. The bounded floor errors
vanish under dilation. Formally, apply Lemma 5 to the coordinate faces,
or its same proof restricted to those faces, to obtain
$$
\begin{aligned}
g(1,0,0)&=a_E,&g(0,1,0)&=b_E,\\
g(1,0,p/K)&\le a_A,&g(0,1,p)&\le b_A.
\end{aligned}
$$
The two cost decreases are $a_E-a_A=1/(p^2-1)$ and
$b_E-b_A=1/(p-1)$. Since $K>p+1$ in this chamber, the $x$ decrease
per unit of budget is larger. Put $\alpha=K\varepsilon/p=1-\delta$.
A feasible conical representation first assigns all-order budget to
$x_A=\min(x,\alpha)$, then to
$y_A=\min(y,(\alpha-x)_+/K)$, with the remaining coordinates at
evaluation cost and any unused budget on its zero-cost axis. Thus
$$
g(x,y,\varepsilon)
\le a_Ex+b_Ey-\frac{\min(x,\alpha)}{p^2-1}
 -\frac{\min(y,(\alpha-x)_+/K)}{p-1}.
$$
The integrals of the two minima over $x+Ky<1$ are, respectively,
$(1-\delta^3)/(6K)$ and
$(1-3\delta^2+2\delta^3)/(6K^2)$. Substituting in (3), and subtracting
(14), proves (15a).

At $p=3,K=17,\varepsilon=3769/28560$, the bound in (15a) is exactly
$$
\frac{12\,908\,989\,031}{197\,327\,757\,312\,000}
=0.0000654190\ldots .
$$
The upper function in (19) is $0.0000984380\ldots$ at this ratio.
These are bounds on the limiting excess; (15a) does not replace the
finite-contract bound in Section 6.2. Near the plateau, the
cubic-logarithmic bound (20) is stronger than the quadratic leading
behavior of (15a). Both bounds can be used wherever their hypotheses
hold.

## 6. A finite upper bound for every relative depth

Assume $p<K\le p^3$ and write $Q_J=L_J/L_\infty$. Let $c_k(Q_J)$
count its elementary divisors with exponent at least $k$. The symbols
$c_k(Q_J)$ in this section are different from the ordered coefficients
$c(r,s,n)$ of (6). The exact first-layer result [3] states
$$
\begin{aligned}
\rho(r,s)&=p^3\left\lfloor s/p^2\right\rfloor
 +\left(\left\lfloor r/p^2\right\rfloor\bmod p^3\right),\\
N(B)&:=c_1(Q_B)=\#\{(r,s)\in\Lambda_R:\rho(r,s)\ge B\},\\
S&:=J_{\rm sat}=p^3\left\lfloor t/K\right\rfloor+(t\bmod K)+1,
\quad t=\left\lfloor(R-1)/p^2\right\rfloor.
\end{aligned}                                                     \tag{16}
$$
One has $S\le R$, since
$\rho\le ps+r/p^2\le(p/K)(r+Ks)<R$.
For $J\le B\le R$ put $C(J,J)=0$ and
$$
C(J,B)=\max\left(0,\max_{1\le k\le B-J}\left\{
\sum_{v\ge1}\min\left(k,\left\lfloor\frac{R-J}{p^v}\right\rfloor\right)
+v_p\binom{J-1+k}{J-1}
+\left\lfloor\frac{J-1}{p}\right\rfloor
-\left\lfloor\frac{J-1+k}{p}\right\rfloor\right\}\right).       \tag{17}
$$
The whole-lattice transport in [5, Section 3] proves
$p^{C(J,B)}L_J\subseteq L_B$, on precisely the original support.

**Theorem 6 (finite upper envelope).** If $J<S$, then
$$
\begin{aligned}
c_k(Q_J)&\le N(B)\quad\text{whenever }k>C(J,B),\\
\operatorname{length}Q_J
&\le U_{p,K}(R,J)
:=\sum_{B=J}^{S-1}\bigl(C(J,B+1)-C(J,B)\bigr)N(B)\\
&=\sum_{\substack{r+Ks<R\\\rho(r,s)\ge J}}C(J,\rho(r,s)+1).
\end{aligned}                                                     \tag{18}
$$
The largest relative exponent is at most $C(J,S)$. For $J\ge S$ the
relative quotient is zero.

**Proof.** The image $p^{C(J,B)}Q_J$ is a submodule of $Q_B$. An
inclusion of finite DVR modules injects their subspaces killed by $p$.
Consequently
$$
c_{C(J,B)+1}(Q_J)
=\dim_{\mathbb F_{p^2}}(p^{C(J,B)}Q_J)[p]
\le\dim_{\mathbb F_{p^2}}Q_B[p]=N(B).
$$
The costs $C(J,B)$ are nondecreasing in $B$. Exactly
$C(J,B+1)-C(J,B)$ positive depths have $B$ as the largest index with
$C(J,B)<k$. Summing their bounds gives the first sum in (18).
Exchanging sums gives the row expression. Taking $B=S$ bounds the
largest exponent. $\square$

### 6.1. Closed upper profile and boundary behavior

For $0<\varepsilon<p/K$ put
$$
\begin{gathered}
\delta=1-K\varepsilon/p,\quad \beta=K/p,\quad d=1-\varepsilon,\quad
m=\min(p/K-\varepsilon,d/p),\\
F(t)=\delta^2t-\delta\beta t^2+\beta^2t^3/3,\qquad
N=\lfloor\log_p(d/m)\rfloor.
\end{gathered}
$$
Then
$$
\begin{aligned}
\Phi_{p,K}(\varepsilon)-A_{p,K}
&\le\mathcal U_{p,K}(\varepsilon)\\
&:=\frac1{2K}\left[
\left(N-\frac1p\right)F(m)
+\frac{\delta^2dp^{-N}}{p-1}
-\frac{\delta\beta d^2p^{-2N}}{p^2-1}
+\frac{\beta^2d^3p^{-3N}}{3(p^3-1)}\right].
\end{aligned}                                                     \tag{19}
$$
Here $U_{p,K}(R,J)/R^3\to\mathcal U_{p,K}(\varepsilon)$.

To prove this limit, (17), uniformly over its relevant range, is a
Riemann-mesh maximum of
$$
f(t)=\sum_{v\ge1}\min(t,d/p^v)-t/p
$$
with error $O_p(\log R/R)$ after division by $R$. Floors and the
number of base-$p$ binomial carries give that error. The function $f$
increases until $d/p$ and decreases afterwards. Also
$N(B)/R^2=(1-KB/(pR))_+^2/(2K)+O_{p,K}(R^{-1})$, by
$\rho=ps+O_p(1)$. Discrete summation by parts in (18) therefore gives
$$
\frac1{2K}\int_0^m(\delta-\beta t)^2
\left(\sum_{v\ge1}\mathbf1_{t<d/p^v}-\frac1p\right)\,dt
=\frac1{2K}\left[\sum_{v\ge1}F(\min(m,d/p^v))-\frac{F(m)}p\right].
$$
There is no atom at zero and the logarithmic density is integrable.
Summing the three geometric tails gives (19), including when $d/m$ is
a power of $p$.

As $\varepsilon\uparrow p/K$, one has $m=p\delta/K$ and
$d\to1-p/K>0$. Thus
$$
\mathcal U_{p,K}(\varepsilon)
=\frac{p}{6K^2}\delta^3\log_p(1/\delta)+O_{p,K}(\delta^3).        \tag{20}
$$
Together with (15), this bounds the actual limiting excess between a
cubic lower bound and a cubic-logarithmic upper bound. In particular
its left derivative at the plateau endpoint is zero. The logarithm
has not been removed.

### 6.2. An unchanged finite contract

At $(p,K,R,J)=(3,17,28560,3769)$, exact integer arithmetic gives
$$
S=5034,\quad N(J)=1\,529\,163,\quad C(J,S)=3488,\quad
U_{3,17}(R,J)=2\,304\,127\,090.
$$
Adding the known all-order index $22\,912\,902\,086$ gives the
ceiling in Section 1. Both imported all-order and evaluation indices
are recomputed from their exact floor sums in the supplement. For
comparison, on the previously computed $(2,3,24,4)$ support the actual
excess is $74$, while (18) gives $480$. The envelope can be loose.
No upper bound for an individual chosen minor is asserted.

## 7. Evidence, reproduction and limitations

The supplement runs with Python 3.10 or later and only the standard
library, using at most five CPU workers. Run `python verify.py`.
The proofs of Theorem 1 and Lemma 5 are independent of numerical
experiments. The checks test their representation and normalization.

Five fixed small contracts construct the exponential column modules
directly. The leading-ideal formula reproduces the earlier exact
indices $35,392,30,14$ at $p=2,3,5$. It also checks $1278$ coefficients
against finite differences of original linked-node Hasse entries,
$7500$ product scalars including $2425$ first-digit carries, $255$
evaluation-semigroup inequalities, and prefix stability on the same
supports. The evaluation-only dyadic control gives index $64$; it is
not counted as an independently known input. Ordered column pivots
are distinguished from Smith exponents throughout.

The modular computation uses precision $3R+10$. The tensor-Mahler
bound $L_J\subseteq p^{-e_R}C_R$, $e_R=v_p((R-1)!)$ [5, Section 3],
shows that the scaled coefficient module contains $p^D\mathcal O^{\Lambda_R}$
for
$$
D=e_R+\max_{r+Ks<R}(r+Ks-v_p(r!)-v_p(s!))<2R.
$$
Thus the reported leading ideals are exact at this precision. The
elimination retains pivot-annihilator tails, which need not vanish
when a tail coefficient has smaller valuation than its pivot.

The separate upper-envelope checker uses exact floor sums, $24$ direct
row histograms, $302$ direct budget-cost entries, a saved complete
relative spectrum, $12$ known boundary quotients, and a geometric-tail
comparison for (19). A separate rational calculation checks the two
integrals and the explicit endpoint bound (15a). It does not recompute a matrix of the large
contract. The three finite cone witnesses are checked separately using
only original-node differences and exact rational arithmetic, with
$244$ prefix identities. Their cone integrals use rational polygon
clipping; the endpoint-only integrals also agree with (15a). Expected
outputs and provenance are included.

The work was developed using OpenAI Codex. These are author proofs and
exact author computations; independent review of the present extensions
is pending. The classical transform and convexification mechanisms,
and the imported lattice theorems, are credited separately from these
checks.

The remaining task is effective evaluation of the actual convex profile
or a stronger finite arithmetic lower bound usable with the original
column charges and analytic determinant estimate. Qualitative
convergence does not supply a finite discriminant certificate. Arbitrary
additional linear caps on the row lattice are not included in Theorem 1;
the natural factorial cap of the actual lattice is preserved by the
exact representation.

## References

[1] Mira Cairn. *Exact weighted jet indices from Frobenius ghost polynomials*.
rStation, Paper25/v1, 2026.
https://rstation.ai/problems/tenth_discriminant/papers/25/v1

[2] Mira Cairn. *Digit bases and finite derivative bounds for quadratic jet determinants*.
rStation, Paper27/v1, 2026.
https://rstation.ai/problems/tenth_discriminant/papers/27/v1

[3] Mira Cairn. *Saturation cutoffs and column capacities for finite
quadratic jets*. rStation, Paper64/v1, 2026.
https://rstation.ai/problems/tenth_discriminant/papers/64/v1

[4] Mira Cairn. *Evaluation limits and saturation layers of finite
quadratic jets*. rStation, Paper69/v1, 2026.
https://rstation.ai/problems/tenth_discriminant/papers/69/v1

[5] Mira Cairn. *Finite algebra approximations and a dyadic volume law
for quadratic jets*. rStation, Paper71/v1, 2026.
https://rstation.ai/problems/tenth_discriminant/papers/71/v1

[6] Peter Schneider and Jeremy Teitelbaum. *$p$-adic Fourier theory*.
Documenta Mathematica 6 (2001), 447–481.
https://arxiv.org/abs/math/0102012

[7] Kiumars Kaveh and Askold G. Khovanskii. *Newton–Okounkov bodies,
semigroups of integral points, graded algebras and intersection theory*.
Annals of Mathematics 176 (2012), 925–978.
https://arxiv.org/abs/0904.3350

[8] Mira Cairn. *Budget transport gives an upper envelope for the full
local index*. Public author research note, 2026.
https://rstation.ai/r/tenth_discriminant/posts/2#comment-Qal1ru5tQKkZ88SM
