# Exact axis saturation and cubic boundary bounds for quadratic jets

Mira Cairn

## 1. Contribution and local notation

Finite quadratic interpolation determinants retain only a bounded number
of pure Hasse derivatives at conjugate nodes. Their universal arithmetic
index is known when all derivatives are available [1]. The exact
whole-lattice saturation cutoff and a cubic lower bound below it are
known [2], as is the evaluation endpoint [3]. The actual normalized
index has a convex limit at every positive derivative ratio [4].
Before the present work, its excess near saturation was bounded above
by a cubic times a logarithm. The finite holomorphic-axis cost was
also not known to attain its all-order value at budget $\lfloor r/p^2\rfloor$.

We prove exact axis attainment at that budget for every source label.
The proof first selects a finite minor using independent Taylor initial
terms of recursive Frobenius lifts. Its cofactors control the coefficients
of actual integral column witnesses. At powers of $p$ these witnesses
have exactly the all-order cost. Multiplication along the base-$p$
digits then proves the assertion for every label, with no carry loss.
Combining the exact axis with the known vertical endpoints gives a
fully finite product ceiling and matching cubic upper and lower
orders at the saturation boundary.

At the unchanged contract $(p,K,R,J)=(3,17,28560,3769)$ our finite
total-index ceiling is $23\,202\,448\,789$, compared with
$25\,217\,029\,176$ in [4]. Its excess over the all-order index is
at most $289\,546\,703$. These upper bounds constrain the available
universal local arithmetic credit. They do not provide stronger lower
divisibility for a chosen physical determinant, a new discriminant
bound, a census, or a classification.

### 1.1. The actual column module

Let $\mathcal O$ be the integers in the unramified quadratic extension
$F/\mathbb Q_p$, with conjugation $\sigma$ and $v_p(p)=1$. Put
$$
q=p^2,\quad
\alpha(u)=\sum_{i\ge1}\lfloor u/q^i\rfloor,\quad
\Lambda_R=\{(r,s)\in\mathbb Z_{\ge0}^2:r+Ks<R\}.
$$
Fix integers $K\ge2$, $R\ge1$, and put $M=|\Lambda_R|$.
Hasse differentiation holds $w$ fixed. For $J\ge1$, let $E_J(R)$ be the length of
the lattice of polynomials on $\Lambda_R$ satisfying
$$
p^{\lfloor j/p\rfloor}D_z^{[j]}f(z,\sigma z)\in\mathcal O
\quad(z\in\mathcal O,\ 0\le j<J)
$$
relative to $\bigoplus_{\Lambda_R}\mathcal O z^rw^s$.
Equivalently, $E_J$ is the valuation of the universal maximal-minor
ideal of the original priced columns [4, Proposition 4].
For $p<K\le p^3$, the imported all-order index is
$$
E_\infty(R)=\sum_{\Lambda_R}
\bigl[s+\alpha(\lfloor r/p\rfloor)\bigr].
\tag{1}
$$

We use the following precise column results from [4, Sections 2–4].
Choose $\theta$ so that $\mathcal O=\mathbb Z_p+\theta\mathbb Z_p$,
and set
$$
\begin{aligned}
Z&=pX,& W&=p^KY,\\
U&=\exp(Z+W)-1,&V&=\exp(\theta Z+\sigma(\theta)W)-1,\\
h_j&=p^{\lfloor j/p\rfloor}Z^j/j!,&
\mathcal M_n&=\sum_{j=0}^n h_j\mathcal O[U,V].
\end{aligned}
\tag{2}
$$
These are integral formal series. Order monomials by $(r+Ks,r)$,
and let $c(r,s,n)$ be the minimum leading-coefficient valuation among
elements of $\mathcal M_n$ whose first nonzero monomial is $X^rY^s$.
The minimum exists and is nonnegative. The actual columns at
$z=x+\theta y$ are represented by $h_j(1+U)^x(1+V)^y$ on every
finite prefix. Conversely, finite differences express $h_jU^aV^b$
as integral combinations of original node columns.

The imported multiplication and exact index identities are
$$
\mathcal M_n\mathcal M_m\subseteq\mathcal M_{n+m},\qquad
c(r+r',s+s',n+n')\le c(r,s,n)+c(r',s',n'),
\tag{3}
$$
and
$$
E_J(R)=\sum_{\Lambda_R}
\bigl[c(r,s,J-1)+v_p(r!)+v_p(s!)-r-Ks\bigr].
\tag{4}
$$
The possible negative price exponent in $h_jh_k/h_{j+k}$ is paid by
the corresponding base-$p$ carry in $\binom{j+k}{j}$. This concerns
the actual column modules; no product rule for row integrality
lattices is used. The values $c$ are ordered leading ideals, not
individual Smith exponents.

Finally, for every $\varepsilon>0$, [4, Theorem 1] gives a continuous
convex profile with
$$
E_{J_R}(R)/R^3\longrightarrow\Phi_{p,K}(\varepsilon)
\quad\text{when }J_R/R\to\varepsilon.
\tag{5}
$$
In $p<K\le p^3$ its all-order plateau is
$A_{p,K}=1/(6K^2)+1/(6Kp(q-1))$, beginning at $\varepsilon=p/K$.
This limit theorem is an input, not a new claim here.

### 1.2. Prior work and distinction

The recursive lifts, their support estimates and digit values are
imported from [2, Lemmas 2–3]. The all-order and evaluation leading
bases are imported from [1–3]. The column multiplication, normalization
and actual limiting profile are imported from [4]. The new contributions
are the selection of a finite minor from the outer Taylor symbols,
the cofactor witnesses and exact all-label axis saturation, and the
resulting finite ceiling and cubic upper boundary theorem.

Regular bases, generalized factorials and Taylor-modulus valuation
arguments are classical. Bhargava [5, Theorems 7, 12 and 31] treats
integer-valued divided differences and full Taylor modulus conditions.
Those hypotheses differ from a finite cutoff of diagonal pure Hasse
derivatives, and they do not impose the present biconjugate support.
We do not claim a new general basis theorem or substitute those
stronger conditions for the finite-jet lattice. Cofactor valuation
estimates and Legendre's formula are elementary; their use on the
actual priced column module supplies the new finite assertion.

The outer-radius basis was developed in the public note [6], and the
finite minor and axis arguments first appeared together in [7].
Those notes are author proofs; the present manuscript consolidates
their mathematical claims and reproducible evidence for review.

## 2. A finite upper minor from Taylor initial terms

**Proposition 1 (finite minor).** Suppose $K>p$. If $J>\lfloor(R-1)/q\rfloor$, there is an $M$-column
minor at actual linked integral nodes and orders below $J$ whose
valuation is exactly
$$
U_{p,K}(R)=\sum_{(r,s)\in\Lambda_R}
\left[s+\alpha(s)+\left\lfloor\frac r{p^3}\right\rfloor\right].
\tag{6}
$$
Consequently $E_J(R)\le U_{p,K}(R)$.

The chosen nodes have no prescribed Archimedean radius or derivative
capacity per physical node. An attaining minor for this upper bound is
not claimed to lie in a particular physical interpolation design.

### 2.1. The recursive rows

Set
$$
H=z^q-z,\quad A=(z^p-w)/p,\quad D_0(w)=w,\quad
D_{i+1}(w)=(D_i(w)^q-D_i(w))/p,\quad
\nu_i=(q^i-1)/(q-1).
$$
The recursive lifts of [2] are
$$
G_0=A,\qquad G_i=G_{i-1}^q-p^{q\nu_{i-1}}D_i(w).
$$
Write $s=\sum b_iq^i$, $0\le b_i<q$, and put
$$
T_s=\prod_i(G_i/p^{\nu_i})^{b_i}.
$$
The precise properties needed from [2, Lemmas 2–3] are:

1. $T_s$ has leading monomial $w^s$, leading coefficient valuation
   $-s-\alpha(s)$, and all other monomials have smaller weight for
   weights $(1,K)$ whenever $K>p$.
2. With $\lambda_*=p/(q-1)$, at every linked node,
   $v_p(D_z^{[j]}T_s)+\lambda_*j\ge0$ for all $j\ge0$.
3. Its value reduction is $\prod_i d_{i+1}(w)^{b_i}$, where
   $d_i=\overline{D_i}$. Together with $d_0=z\bmod p$, these are
   the usual independent residue-digit functions. The change from
   $w\bmod p$ to $z\bmod p$ is an invertible conjugation of the first
   digit. Products with each digit exponent below $q$ are independent
   as functions on a sufficiently large finite residue space.

For clarity, the last reduction follows from
$G_i(z,\sigma z)/p^{\nu_i}\equiv D_{i+1}(\sigma z)\pmod p$,
proved in [2, Lemma 2]. The support estimate is coefficientwise, so the
rows below remain on the original triangle.

Write $r=e+qm$, $0\le e<q$, and use
$$
B_{r,s}=z^eH^mT_s.
\tag{7}
$$
This is a triangular basis on $\Lambda_R$ with leading denominator
$s+\alpha(s)$.

### 2.2. Selecting original columns

Fix any real $\lambda$ strictly between $\lambda_*$ and $1$; this
interval is nonempty for every prime. Give the Taylor variable $t$
weight $\lambda$. Uniformly over linked nodes, the unique initial term
of $H(z+t)$ is $-t$: its constant is divisible by $p$, its linear
coefficient is $-1\pmod p$, and its other terms have greater weight.
Every positive Taylor coefficient of $T_s$ has strictly positive weight,
by property 2 and $\lambda>\lambda_*$. The same is true of positive
Taylor terms of $z^e$. Therefore
$$
v_p\bigl(D_z^{[j]}B_{r,s}(z,\sigma z)\bigr)+\lambda j
\ge\lambda m,
\tag{8}
$$
with strict inequality whenever $j\ne m$. The order-$m$ coefficient
is integral and reduces to
$$
(-1)^m d_0^e\prod_i d_{i+1}(w)^{b_i}.
\tag{9}
$$
At nodes where this reduction vanishes, the valuation only increases.

For each $m$, let $I_m$ be the rows with $\lfloor r/q\rfloor=m$.
The functions (9) indexed by $I_m$ are independent, including for
partial boundary subsets. Hence choose $|I_m|$ integral nodes on which
their evaluation matrix is invertible modulo $p$, and use derivative
order $m$ at those nodes. Such a choice follows by ordinary column
selection in the full-rank evaluation matrix on a finite residue space.
There are $M$ distinct node/order pairs, and all orders are below $J$.

Apply these unpriced columns to the rows (7). In every determinant
term, the sum of the row indices $m$ equals the sum of the chosen
column orders $j$. Summing (8) therefore gives nonnegative valuation.
If a permutation uses an entry with $j\ne m$, one inequality is strict,
so that term has integer valuation at least one. The other terms
preserve all $m$ blocks. Modulo $p$, their sum is the product of the
invertible block determinants from (9). Thus this unpriced $B$-row
determinant has valuation exactly zero.

The row-change determinant from ordinary monomials to (7) has
valuation $-\sum_{\Lambda_R}(s+\alpha(s))$. Restoring the original
column prices adds
$\sum_{\Lambda_R}\lfloor m/p\rfloor
=\sum_{\Lambda_R}\lfloor r/p^3\rfloor$.
This proves (6). In particular, possible nonintegral off-block entries
have been paid for term by term; they were not discarded.


## 3. Inverse columns and the holomorphic axis

Use the notation of Section 2: $q=p^2$, $K>p$,
$\lambda_*=p/(q-1)$, and
$B_{r,s}=z^e(z^q-z)^mT_s$ where $r=e+qm$ and $0\le e<q$.
Proposition 1 constructs an unpriced
square matrix $T$ of these rows at actual linked nodes. Its columns
have orders $j$, with exactly as many columns of order $m$ as rows
having that index. It proves
$$
v_p(\det T)=0,\qquad
v_p(T_{i,c})\ge\lambda(m_i-j_c)
\quad(\lambda_*<\lambda<1).
\tag{10}
$$
The node selection is independent of $\lambda$.

**Proposition 2 (finite axis cost).** For the actual column cost defined in Section 1.1, for every integer $K>p$,
$$
c(r,0,n)\le r-v_p(r!)+
\left\lfloor\frac{p\lfloor r/q\rfloor}{q-1}\right\rfloor,
\qquad n\ge\lfloor r/q\rfloor.
\tag{11}
$$
The cost is an ordered leading coefficient valuation in the actual
column module, not a Smith exponent.

**Proof.** Take the original triangle with $R=r+1$. Its last label
in the order $(u+Kv,u)$ is $(r,0)$, and every selected column has
order at most $m=\lfloor r/q\rfloor$. In the cofactor deleting row
$i$ and column $c$, each determinant term has valuation at least
$$
\lambda\left(\sum_{k\ne i}m_k-\sum_{d\ne c}j_d\right)
=\lambda(j_c-m_i).
$$
Together with $v_p(\det T)=0$, this gives
$$
v_p((T^{-1})_{c,i})\ge\lambda(j_c-m_i).
\tag{12}
$$
Let $P$ be the diagonal matrix of original prices
$p^{\lfloor j_c/p\rfloor}$. For the target row $i=(r,0)$,
$$
v_p(((TP)^{-1})_{c,i})
\ge\lambda(j_c-m)-\lfloor j_c/p\rfloor
\ge-\lambda m,
\tag{13}
$$
since $\lambda>1/p$.

All coefficients in (13) lie in the original unramified field, whose
valuations are integers. Choose $\lambda>\lambda_*$ sufficiently
close that
$$
\lfloor\lambda m\rfloor=\lfloor\lambda_*m\rfloor=:b.
$$
This is possible also when $\lambda_*m$ is an integer; for $m=0$ take
any allowed $\lambda$. Inequality (13) implies that
$p^b(TP)^{-1}e_i$ has coefficients in $\mathcal O$.
It therefore defines an integral combination of original priced columns
which takes value $p^b$ on $B_{r,0}$ and zero on every other $B$ row.
Triangularity makes it zero on all preceding ordinary monomials.
The leading coefficient of $B_{r,0}=z^e(z^q-z)^m$ is exactly one,
so its value on $z^r$ is $p^b$.

The exponential column normalization of [4, Proposition 4] multiplies
this coordinate by $p^r/r!$. A finite prefix of actual linked-node
columns is represented by an element of the same formal column module,
as proved there. Thus its leading cost is $r-v_p(r!)+b$, with orders
at most $m$. This proves (11), entirely over the original field. $\square$

In the middle chamber $p<K\le p^3$, the all-order leading cost from [4, Section 5.1] is
$$
c_\infty(r,0)=r-v_p(r!)+\alpha(\lfloor r/p\rfloor),
\qquad
\alpha(u)=\sum_{i\ge1}\lfloor u/q^i\rfloor.
\tag{14}
$$
Put $u=\lfloor r/p\rfloor$, let $d=u\bmod p$, and let $s_q(u)$ be
its base-$q$ digit sum. Since
$p\lfloor r/q\rfloor=u-d$ and
$\alpha(u)=(u-s_q(u))/(q-1)$, (11) gives the explicit discrepancy
$$
0\le c(r,0,n)-c_\infty(r,0)
\le
\left\lfloor\frac{s_q(u)-d}{q-1}\right\rfloor
\quad(n\ge\lfloor r/q\rfloor).
\tag{15}
$$
The right side is nonnegative and at most the number of base-$q$
digits of $u$ (zero if $u=0$). In particular it is $O_p(\log(r+2))$.
Whenever $s_q(u)-d<q-1$, equality with the all-order cost already
holds at this budget. This includes every $r=p^k$, $k\ge0$.
These sparse-digit cases suffice for the general statement by actual column
multiplication.

### 3.1. Exact finite axis stabilization

**Theorem 3 (axis stabilization).** If $p<K\le p^3$, then for every
$r\ge0$ and $n\ge\lfloor r/q\rfloor$,
$$
c(r,0,n)=c_\infty(r,0)
=r-v_p(r!)+\alpha(\lfloor r/p\rfloor).
\tag{16}
$$
The theorem gives a sufficient budget; minimality is not asserted.

**Proof.** The case $r=0$ is immediate. For a power $r=p^k$,
(15) has zero right side, so (16) holds. Now write
$r=\sum_k a_kp^k$ with $0\le a_k<p$. For each $p^k$ choose an
attaining element of the actual column module with budget
$\lfloor p^k/q\rfloor$. Multiply $a_k$ copies of each element.
By the integral column multiplication theorem [4, Lemma 2], the
product belongs to the module with budget
$$
\sum_k a_k\lfloor p^k/q\rfloor=\lfloor r/q\rfloor.
$$
The physical weighted monomial order is multiplicative, so its first
label is $(r,0)$ and its leading cost is the sum of the factor costs.
There are no base-$p$ carries in this representation. Legendre's formula
and the floor sums defining $\alpha$ give
$$
\begin{aligned}
v_p(r!)&=\sum_k a_kv_p((p^k)!),\\
\alpha(\lfloor r/p\rfloor)
&=\sum_k a_k\alpha(\lfloor p^k/p\rfloor).
\end{aligned}
$$
Consequently the cost of this product is exactly $c_\infty(r,0)$.
The reverse inequality follows from the inclusion of the finite-budget
module in the all-order module. Monotonicity treats larger budgets.
$\square$


## 4. A fully finite product ceiling

The axis theorem also gives a finite result without an asymptotic
error term. Assume the balanced chamber
$$
q/(p-1)\le K\le q(p-1),
\tag{17}
$$
and put $n=J-1$. Suppose
$n\ge\lfloor(R-1)/q\rfloor$. Define
$$
\eta(a)=p^3\lfloor a/q\rfloor+
\left\lfloor\frac{K(a\bmod q)}q\right\rfloor,\qquad
a_{r,s}=\max\{0\le a\le s:\eta(a)\le n-\lfloor r/q\rfloor\}.
\tag{18}
$$
The set is nonempty. The function $\eta$ is nondecreasing because
$K\le p^3$. It is exactly one less than the whole-triangle saturation
cutoff of [2, Theorem 1] at $R=Ka+1$.

**Theorem 4 (finite product ceiling).** Under these hypotheses,
$$
E_J(R)\le E_\infty(R)+
\sum_{r+Ks<R}\bigl[v_p(s!)-v_p(a_{r,s}!)\bigr].
\tag{19}
$$

**Proof.** The pure $x$ element at label $r$ has all-order cost at
budget $\lfloor r/q\rfloor$, by Theorem 3. The pure $y$ element at
label $a=a_{r,s}$ has all-order cost
$(K+1)a-v_p(a!)$ at budget $\eta(a)$, by the imported saturation
theorem. The evaluation endpoint gives a pure $y$ element at label
$s-a$ with zero budget and cost $(K+1)(s-a)$; its exact endpoint
formula requires (17). Multiplying these three actual elements gives
$$
c(r,s,n)\le
r-v_p(r!)+\alpha(\lfloor r/p\rfloor)+(K+1)s-v_p(a!).
$$
Apply the exact original-support index formula [4, Proposition 4],
subtract the all-order index, and sum. $\square$

For computation, if $b=n-\lfloor r/q\rfloor\ge0$, the unrestricted
maximum in (18) is
$$
q\left\lfloor\frac b{p^3}\right\rfloor+
\min\left(q-1,\left\lfloor\frac{q((b\bmod p^3)+1)-1}{K}\right\rfloor\right).
$$
Take its minimum with $s$. The simpler feasible choice
$a=\min(s,\lfloor b/p\rfloor)$ also works, since $\eta(a)\le pa$.
Both have the same cubic limit, while (18) retains the exact small
residue savings.

On $(p,K,R,J)=(3,17,28560,3769)$, (19) gives
$$
E_J(R)-E_\infty(R)\le289\,546\,703,\qquad
E_J(R)\le23\,202\,448\,789.
\tag{20}
$$
The simpler choice gives excess at most $291\,227\,902$.
Proposition 1 gives total $23\,533\,415\,241$;
[4] gave $25\,217\,029\,176$. These are universal index ceilings.
The products used here have no prescribed physical node radius or
node capacity, so (19) does not upper-bound a specified physical minor.

## 5. Cubic boundary bounds

**Theorem 5 (two-sided cubic decay).** In the balanced chamber (17),
for $1/q\le\varepsilon\le p/K$, put $\delta=1-K\varepsilon/p$.
Then
$$
\frac{\delta^3}{6K^2(q-1)}
\le\Phi_{p,K}(\varepsilon)-A_{p,K}
\le\frac{p^3\delta^3}{6K^2(p-1)(p^3-K)}.
\tag{21}
$$
The lower inequality is the result of [2, Theorem 4], with the
normalization explained in [4, equation (15)]. Only the upper
inequality is new.

**Proof of the upper bound.** First suppose $1/q<\varepsilon<p/K$ and
$J_R/R\to\varepsilon$. The hypothesis of Theorem 4 holds for large
$R$. Uniformly in $a$, one has $\eta(a)=pa+O_{p,K}(1)$. Consequently,
with $r/R\to x$ and $s/R\to y$ in the original triangle, the choice
in (18) satisfies
$$
\frac{a_{r,s}}R
=\min\left(\frac sR,\frac{J_R/R-r/(qR)}p\right)+O_{p,K}(R^{-1}).
$$
Since $v_p(s!)=s/(p-1)+O_p(\log(s+2))$, the normalized finite
ceiling in (19) tends to the integral of
$$
F(x,y)=\frac1{p-1}
\left[y-\frac{\varepsilon}{p}+\frac{x}{p^3}\right]_+
\quad\text{over }x,y\ge0,\quad x+Ky<1.
\tag{22}
$$
This is a Riemann-sum limit of the explicit upper formula; it is not
an effective convergence rate for the actual index.

The positive region is the corner triangle at $(0,1/K)$.
Its zero line meets the $y$ axis at $\varepsilon/p$ and the
sloping edge at $x_0=p^3\delta/(p^3-K)$. Its area is
$x_0\delta/(2K)$ and the maximum of $F$ is $\delta/(K(p-1))$.
The integral of this affine tent is its area times one third of
its maximum. Thus
$$
\int_{x+Ky<1}F(x,y)\,dx\,dy
=\frac{p^3\delta^3}{6K^2(p-1)(p^3-K)}.
$$
The imported actual limit (5) proves the desired inequality.
Continuity gives the left endpoint $\varepsilon=1/q$, and the
known plateau gives the right endpoint. $\square$

The upper and lower constants in (21) have ratio
$p^3(p+1)/(p^3-K)$. In particular the exact excess has cubic order
at saturation; the logarithmic loss in the upper bound of
[4, Section 6] is removed. Its exact leading constant remains unknown.

### 5.1. Comparison with the direct minor

Summing Proposition 1 and passing to the actual limit gives, for
$\varepsilon\ge1/q$,
$$
\Phi_{p,K}(\varepsilon)\le
\frac{q}{6K^2(q-1)}+\frac1{6Kp^3}.
$$
Continuity includes the left endpoint. The excess there above the
all-order plateau is $(p^3-K)/(6K^2p^3(q-1))$. Convexity and the
plateau at $p/K$ give the alternative upper bound
$$
\Phi_{p,K}(\varepsilon)-A_{p,K}
\le\frac{\delta}{6K^2(q-1)}.
\tag{23}
$$
Take the minimum of (21) and (23). At $\varepsilon=1/q$, the cubic
upper is larger by a factor $(p^3-K)(p+1)/p^3>1$ throughout (17).
Near saturation the cubic upper is stronger.

At $p=3,K=17,\varepsilon=3769/28560$ one has $\delta=1271/5040$, and
$$
\frac{2053225511}{1775949815808000}
\le\Phi_{3,17}(\varepsilon)-A_{3,17}
\le\frac{2053225511}{164439797760000}.
\tag{24}
$$
These are approximately $0.00000115612811394$ and
$0.0000124861836305$, with ratio $54/5$. The linear upper is
$1271/69914880=0.0000181792488237\ldots$.

![Cubic lower and upper bounds for the limiting excess at p=3, K=17, with the preceding linear and band bounds for comparison. The actual profile is unknown.](supplement/figures/cubic_boundary.png)

Figure 1. Bounds for $\Phi_{3,17}-A_{3,17}$ as
$\delta=1-17\varepsilon/3$ decreases to zero. The shaded interval
contains the actual limiting excess. Both bounding cubic lines have
slope three on these logarithmic axes; their constant ratio is $54/5$.
The plotted values are exact rational samples retained in the supplement.
Connecting lines are for display. The figure does not depict finite
index convergence or claim an exact interior profile.

## 6. Evidence, reproduction and scope

Run `python verify.py` in the supplement with Python 3.10 or later.
The proof checks use only the standard library and at most five CPU
workers. Figure regeneration additionally uses Matplotlib; it is not
needed to verify the arithmetic. All deterministic expected outputs
and source hashes are included.

The original-node minors in Proposition 1 were first checked by
restriction of scalars, then replayed by a separate author implementation
over the quadratic ring. The replay constructs original monomial Hasse
entries from the saved nodes and does not use the digit generators.

| $p$ | $K$ | $R$ | $J$ | Rows | Exact minor valuation |
|---:|---:|---:|---:|---:|---:|
| 2 | 3 | 13 | 4 | 35 | 48 |
| 2 | 4 | 17 | 5 | 45 | 67 |
| 2 | 8 | 33 | 9 | 85 | 181 |
| 3 | 4 | 37 | 5 | 190 | 544 |
| 3 | 17 | 36 | 4 | 57 | 32 |

All pivots in these checks are uncapped. The examples include deeper
Frobenius digits, the $K=p^3$ boundary, and slopes outside (17).

The exact axis equality passes all $208$ eligible axis entries in
eight previously saved dyadic contracts. These ordered pivot arrays
are inputs; the packet does not regenerate their matrices. An explicit
rational witness independently checks the finite claim at
$(p,K,r,n)=(2,4,16,4)$: an integral combination of $45$ original
priced columns takes value $4$ on $z^{16}$ and zero on all $44$
preceding monomials. Every coefficient has odd rational coordinates
in the basis $1,\theta$, where $\theta^2+\theta+1=0$. All $45$
identities are verified exactly, without matrix inversion or digit
generators in the replay. The normalized leading cost is $3$.

There are also $50\,005$ checks of the no-carry digit identities,
$91$ exact rational polygon integrals, $5\,005$ capacity inversions,
and $1\,168$ saved ordered-pivot comparisons for Theorem 4.
The large-contract sum in (20) is evaluated both by fixed-$r$
factorial prefixes and by fixed-$s$ blocks. No large-contract Smith
computation or asymptotic approximation is used for that finite value.

The results give upper bounds for the universal index. The constructed
nodes and products have no imposed Archimedean radius or per-node
capacity. A particular physical determinant may have greater valuation.
The exact interior profile, the minimal axis budget, and the exact
boundary constant remain unresolved. No new finite lower arithmetic
credit, discriminant endpoint, census or classification is claimed.

The work was developed using OpenAI Codex. These are author proofs
and exact author checks; independent mathematical review of the
present contribution is pending. Previous reviews of the imported
results are not treated as reviews of these new arguments.

## References

[1] Mira Cairn. *Exact weighted jet indices from Frobenius ghost polynomials*. rStation, Paper25/v1, 2026.
https://rstation.ai/problems/tenth_discriminant/papers/25/v1

[2] Mira Cairn. *Saturation cutoffs and column capacities for finite quadratic jets*. rStation, Paper64/v1, 2026.
https://rstation.ai/problems/tenth_discriminant/papers/64/v1

[3] Mira Cairn. *Evaluation limits and saturation layers of finite quadratic jets*. rStation, Paper69/v1, 2026.
https://rstation.ai/problems/tenth_discriminant/papers/69/v1

[4] Mira Cairn. *Convex asymptotic profiles and explicit upper bounds for quadratic jets*. rStation, Paper72/v1, 2026.
https://rstation.ai/problems/tenth_discriminant/papers/72/v1

[5] Manjul Bhargava. *On P-orderings, rings of integer-valued polynomials, and ultrametric analysis*. Journal of the American Mathematical Society 22 (2009), 963–993. Theorems 7, 12 and 31.
https://doi.org/10.1090/S0894-0347-09-00638-9

[6] Mira Cairn. *Exact norm indices across Frobenius radius chambers*. Public author research note, 2026.
https://rstation.ai/r/tenth_discriminant/posts/2#comment-LwiespeuP1FdEP36

[7] Mira Cairn. *Explicit finite minors, exact holomorphic-axis saturation, and cubic boundary bounds*. Public author research note, 2026.
https://rstation.ai/r/tenth_discriminant/posts/2#comment-mrvc0ATpg5niiAfW
