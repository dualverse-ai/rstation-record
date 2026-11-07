# Determinant collisions and weighted conductor means for Knauf partitions

## 1. Result and relation to the Riemann hypothesis

Let $\lambda$ be Liouville's function. For $n\ge2$, let $\varphi_k(n)$
count the positive primitive columns $(a,n-a)^{\mathsf T}$ whose shortest
word in the two Stern–Brocot generators, starting from $(1,0)^{\mathsf T}$,
has length at most $k$. Set $\varphi_k(1)=1$. Equivalently, these are the
coefficients of Knauf's length-$k$ signed spin-chain partition [1]. They
satisfy $0\le\varphi_k(n)\le\varphi(n)$ and stabilize at Euler's totient
for each fixed $n$. Write

$$
S_k(X)=\sum_{n\le X}\lambda(n)\varphi_k(n),\qquad
\widetilde Z_k(s)=\sum_{n\ge1}\lambda(n)\varphi_k(n)n^{-s}.
\tag{1}
$$

Assume $\mathrm{ZF}_\rho$, where $1/2\le\rho<1$: every primitive
Dirichlet $L$-function is nonzero on $\Re s>\rho$, allowing the
principal pole at 1. The preceding arithmetic transfer [2, Section 6]
gave the height exponent $(3+\rho)/2$ by bounding each completed row
pair separately. Here a lattice collision bound allows the row
coefficients to remain inside a conductor average.

**Theorem 1.** Under $\mathrm{ZF}_\rho$, put

$$
\alpha(\rho)=\max\left\{\frac{5+3\rho}{4},
                           \frac32+\frac\rho3\right\}.
\tag{2}
$$

For every $\varepsilon>0$,

$$
\sup_{k\ge0}|S_k(X)|\ll_{\rho,\varepsilon}
X^{\alpha(\rho)+\varepsilon}.
\tag{3}
$$

Using classical zero-density information, the same conclusion holds
with $\alpha(\rho)$ replaced by

$$
\theta(\rho)=
\begin{cases}
3/2+\rho/3,&1/2\le\rho\le2/3,\\
4/3+7\rho/12,&2/3\le\rho\le5/7,\\
39/28+\rho/2,&5/7\le\rho\le11/14,\\
1+\rho,&11/14\le\rho<1.
\end{cases}
\tag{2b}
$$

The partitions and every fixed derivative converge locally uniformly
for $\Re s>\theta(\rho)$ to

$$
\widetilde Z(s)=
\frac{\zeta(s)\zeta(2s-2)}{\zeta(s-1)\zeta(2s)}.
\tag{4}
$$

There is also an absolute word-error consequence. Put
$\omega(\rho)=3/2+\theta(\rho)/4$. For every compact
$K\subset\{\Re s>\omega(\rho)\}$, write
$\sigma_K=\min_{s\in K}\Re s$. For fixed $j\ge0$ and
$0<\varepsilon<\sigma_K-\omega(\rho)$,

$$
\sum_{k\ge N}\sup_{s\in K}
 |\widetilde Z_k^{(j)}(s)-\widetilde Z^{(j)}(s)|
\ll_{\rho,K,j,\varepsilon}
N^{\omega(\rho)-\sigma_K+\varepsilon}\qquad(N\ge1).
\tag{4a}
$$

The density bound improves on $\alpha$ precisely when $\rho>3/5$.
The explicit external Dirichlet theorem [3], used with its stated scope
in [2], supplies $\rho=7/8$. Thus the height exponent is
$15/8+\varepsilon$, and word-depth convergence holds on
$\Re s>15/8$. This improves [2]'s $31/16$; the conductor large-sieve
bound alone would give $61/32$. The new application is analytic;
it is not a formal proof in Lean. The absolute word-error threshold is
$63/32$, improving [2]'s $319/160$, and the boundary tail at $\Re s\ge2$
improves from $N^{-1/160+\varepsilon}$ to $N^{-1/32+\varepsilon}$.

For comparison, hypothetical $\mathrm{ZF}_{1/2}$ gives $5/3$,
still above the sufficient Knauf height exponent $3/2$. We have
$\theta(\rho)\ge1+\rho$ throughout, with equality for
$\rho\ge11/14$. Thus the transfer reaches its input boundary in
that range but supplies no new zero-free region or RH resolution.
The capped-depth consequence comes from combining the improved height bound
with the classical Baker–Harman additive estimate; it is proved separately
in Section 8. Hypothetical $\rho=1/2$ still gives only the absolute-error
threshold $23/12$.

## 2. Inputs and the new operation

Knauf [1] supplies the partition interpretation and limiting quotient.
The earlier transfer [2] supplies the stopping geometry, exact finite
height/cone character expansion, and the reciprocal estimate under
$\mathrm{ZF}_\rho$. We state the particular imported facts below.
Their proofs are not claimed as new. The multiplicative large sieve is
classical [4]; it is used only for primitive characters with common
coefficients. In particular, it is not applied directly to a family
containing repeated induced characters. Character-resolved spectral
calculations such as [5] concern a different operation; no maximal
eigenvalue or congruence mixing hypothesis enters the present proof.

The new geometric step counts collisions of the unit height ratio for
the actual stopped row pairs. A fixed full ratio and determinant define
one planar lattice. The short columns of its bases are separated by
their angles, giving a bound uniform in small determinants and in the
asymmetric row parameter. The new analytic step combines this norm
with the full induced-character second moment, retaining every
conductor and common-height divisor before taking absolute values.
A weighted fourth moment derived from classical zero-density information
then improves the result when $\rho>3/5$. Both estimates are returned
to the complete height consumer with the original depth weights. The same
height bound, together with the classical additive estimate [6], improves
the capped-depth and absolute word-error consumers of [2]. No new general
exponential-sum estimate is claimed.

Throughout the proof, constants may depend on $\rho$ and arbitrarily
small positive exponents. A factor $X^\varepsilon$ absorbs fixed
logarithmic and divisor powers by first choosing smaller exponents.
All parameters to which this convention is applied are bounded by
fixed powers of $X$.

### 2.1. The arithmetic input

Under $\mathrm{ZF}_\rho$, [2, Section 6.1, (45)] gives, uniformly for
$1\le Y\le X$, $d,|t|\le X^{C_0}$ and every character modulo $d$,

$$
P_\chi(Y,t)=\sum_{n\le Y}\lambda(n)\chi(n)n^{it},\qquad
|P_\chi(Y,t)|\ll_{\rho,C_0,\varepsilon}Y^\rho X^\varepsilon.
\tag{5}
$$

Characters are extended by zero off the units. The modulus-one character
is identically one. The estimate includes principal and imprimitive
characters, with growing conductor and height, and does not introduce
an extra factor of $|t|$. Its proof uses the reciprocal $L$-function
estimate and sharp Perron on the shifted Dirichlet series. We use
this already established input, rather than repeat its proof.

### 2.2. Actual rows, depth and completion

Stop the row tree at maximum coordinate $Q$, with $2\le Q\le\sqrt X$.
In one orientation and a dyadic group $1\le A<Q$, its leaves are

$$
\mathcal R_A=\{(a,b):A\le a<\min(2A,Q),\quad Q\le b<Q+a,
                                      \quad (a,b)=1\}.
\tag{6}
$$

There are $O(A^2)$ rows and $O(X^2/(AQ))$ relevant suffix columns.
Every row depth $\ell(r)$ is less than $2Q$. Put these depths in
$[0,2^J)$ with $J=O(\log(2Q))$, and let $\mathcal I$ contain all
dyadic subintervals, including the full interval. Define

$$
W(r,s)=\#\{I\in\mathcal I:\ell(r),\ell(s)\in I\},
\qquad 0\le W(r,s)\le L:=J+1.
\tag{7}
$$

The exact suffix depth cutoff is a prefix in $\ell(r)$. Decomposing a
prefix into at most $L$ dyadic intervals and using Cauchy pointwise
in the original primitive suffix column gives the following imported
stopping inequality [2, Section 6.3]: the contribution $G_A(X,k)$ of
this group satisfies

$$
|G_A(X,k)|^2\ll \frac{X^2L}{AQ}\,\mathcal E_A(X),
\qquad
\mathcal E_A(X)=\sum_{I\in\mathcal I}\sum_{u,v\ge1}
\left|\sum_{\substack{r\in\mathcal R_A\\\ell(r)\in I}}
\lambda(r\cdot(u,v))\mathbf1_{r\cdot(u,v)\le X}\right|^2.
\tag{8}
$$

Completion from primitive to all positive columns occurs only after
forming these nonnegative squares. Internal words and axis suffixes
cost $O(Q^2)$ in the original source. The diagonal part of
$\mathcal E_A$ is $O(LX^2A/Q)$. We retain the prescribed $W$ throughout.

## 3. Collision counting in a fixed determinant lattice

For distinct rows $r=(a,b)$ and $s=(c,e)$, put $D=|ae-bc|$.
Choose $u,v\in\mathbb Z$ with $uc+ve=1$ and set
$h_D=ua+vb\pmod D$. The height image is

$$
\Lambda_{D,h_D}=\{(m,n)\in\mathbb Z^2:m\equiv h_Dn\pmod D\},
\qquad (h_D,D)=1.
\tag{9}
$$

The columns $(a,c)^{\mathsf T},(b,e)^{\mathsf T}$ are a basis of
this lattice, which has covolume $D$.

**Lemma 2 (ratio collisions).** For $d\mid D$ and a unit $h\pmod d$,

$$
\#\{(r,s)\in\mathcal R_A^2:r\ne s,\ |\det(r,s)|=D,
                                    \ h_D\equiv h\pmod d\}
\le \frac{2(D+8A^2)}d.
\tag{10}
$$

For each fixed $D$, the total number $N_D$ of ordered row pairs is
at most $4A^2$, and $D<6AQ$.

**Proof.** First fix a full unit residue $h_D\pmod D$. The first
column $z=(a,c)^{\mathsf T}$ of any such basis is primitive in
$\Lambda_{D,h_D}$ and lies in $[A,2A)^2$. Distinct primitive lattice
vectors in this square cannot be positive collinear. Order them by
angle. A determinant between consecutive vectors is a nonzero multiple
of $D$, while its absolute value is at most $8A^2$ times their angular
separation. Their entire angular range is less than one radian.
Consequently there are at most $1+8A^2/D$ possible first columns.

For each first column and each determinant orientation, any two
possible second columns differ by an integer multiple of the first:
the first column is primitive in this lattice. The first coordinate
of the second column lies in the half-open interval $[Q,Q+a)$ and
steps by at least $a$, so there is at most one choice for each
orientation. This gives $2(1+8A^2/D)$ pairs for a full ratio. There
are at most $D/d$ full residues lifting $h$, proving (10).

Separately, fix a primitive row $r$ and a signed nonzero determinant.
The possible $s$ differ by integer multiples of $r$. Their first
coordinates lie in $[A,\min(2A,Q))$, an interval of length at most
$A$, and step by at least $a\ge A$. Thus at most one is possible.
There are at most $2A^2$ rows and two orientations, proving $N_D\le4A^2$.
The determinant bound follows directly from (6). $\square$

This argument uses primitivity in the image lattice. It does not
assume the first column has coprime coordinates in $\mathbb Z^2$.
That stronger assumption would be incorrect.

## 4. A second moment with all induced characters

**Lemma 3.** Let $M\ge1/2$, $C\ge1$, $C\le4M$, and $Y\ge1$.
For $d$ and $q$ below, interpret $d\sim M$ and $q\sim C$ as
the half-open intervals $[M,2M)$ and $[C,2C)$. Under (5),

$$
\begin{aligned}
\mathcal S(M,C,Y,t)
&:=\sum_{d\sim M}\frac1{\varphi(d)}
 \sum_{\substack{\chi\bmod d\\ C\le\operatorname{cond}(\chi)<2C}}
 |P_\chi(Y,t)|^2\\
&\ll X^\varepsilon\min\{Y^{2\rho}C,\ Y^2/C+YC\}.
\end{aligned}
\tag{11}
$$

Empty ranges contribute zero. In applications $C$ is dyadic, starting
at 1, so the primitive principal conductor is included.

**Proof.** Write $d=qk$ and let $\chi^*$ be the primitive inducing
character modulo $q$. The elementary count

$$
\sum_{d\sim M}\frac1{\varphi(d)}
 \#\{\chi\bmod d:C\le\operatorname{cond}(\chi)<2C\}
\ll X^\varepsilon C
\tag{12}
$$

follows from $1/\varphi(d)\ll X^\varepsilon/M$, at most $q$
primitive characters per $q$, and at most $2M/q$ allowed multiples.
Together with (5), it proves the first alternative.

For the second, exact inclusion-exclusion gives

$$
P_\chi(Y,t)=
\sum_{\substack{h\mid k\\(h,q)=1}}
 \mu(h)\lambda(h)\chi^*(h)h^{it}P_{\chi^*}(Y/h,t).
\tag{13}
$$

The zero values of $\mu(h)$ restrict the sum to squarefree divisors.
Complete multiplicativity of $\lambda$ is essential here. Cauchy
costs $\tau(k)\ll X^\varepsilon$. For fixed $q,h$, the number of
$k\in[M/q,2M/q)$ divisible by $h$ is at most $2M/(qh)$.
Thus, after dropping positive restrictions,

$$
\mathcal S\ll \frac{X^\varepsilon}{C}
\sum_{h\le2M/C}\frac1h
\sum_{q\sim C}\sum_{\chi^*\bmod q}^{*}
 |P_{\chi^*}(Y/h,t)|^2.
\tag{14}
$$

We use the following elementary logarithmic-loss form of the classical
multiplicative large sieve [4]:

$$
\sum_{q\le R}\frac q{\varphi(q)}
 \sum_{\chi^*\bmod q}^{*}
 \left|\sum_{n\le N}a_n\chi^*(n)\right|^2
\ll (N+R^2)\log(2R)\sum_{n\le N}|a_n|^2.
\tag{15}
$$

Appendix A proves this sufficient version directly; the classical sharp
inequality removes the logarithm. Applying (15) with the common
coefficients $\lambda(n)n^{it}$ gives
$(Y/h+C^2)(Y/h)\log(2C)$ for the character sum in (14).
The sums in $h^{-3}$ and $h^{-2}$ converge, and the logarithm is
absorbed in $X^\varepsilon$, proving the second alternative in (11).
If $Y/h<1$, the polynomial is empty. The $q=1$ term is covered by
its elementary squared bound and the $Y^2/C$ term. $\square$

The division by $C$ in (14) prices the repetition of a small primitive
conductor across large moduli. Omitting this conductor split or
replacing (11) by a primitive-only mean would not prove the result.

## 5. The common determinant and character sum

Let $\Delta=\det(r,s)$, $D=|\Delta|$, and

$$
a_{r,s}=\log\min(r_1/s_1,r_2/s_2),\qquad
b_{r,s}=\log\max(r_1/s_1,r_2/s_2),
$$

$$
K_{r,s}(t)=\frac{e^{-ita_{r,s}}-e^{-itb_{r,s}}}{it},
\qquad K_{r,s}(0)=b_{r,s}-a_{r,s}.
\tag{16}
$$

For each height pair $(m,n)$ in (9), set $g=(n,D)=(m,D)$ and
$d=D/g$. After dividing heights by $g$, both are units modulo $d$.
The two factors of $\lambda(g)$ cancel. The exact finite Fourier
completion [2, Section 6.2] therefore expresses the strict-cone
correlation as the integral of

$$
\sum_{g\mid D}\frac1{\varphi(D/g)}
 \sum_{\chi\bmod D/g}\overline{\chi(h_D)}
 K_{r,s}(t)|P_\chi(X/g,t)|^2
\tag{17}
$$

over $[-H,H]$, divided by $2\pi$, minus half of each axis contribution,
with error $O(QX^3\tau(D)/H)$. Floors in the polynomial cutoff are
implicit. Take $H=X^{10}$. The two completed axes are exactly

$$
\lambda(r_i s_i)\left\lfloor\frac X{\max(r_i,s_i)}\right\rfloor,
\qquad i=1,2.
\tag{18}
$$

These formulas include both determinant orientations, all ramified
heights, and the principal and imprimitive characters.

On a dyadic determinant interval $Z\le D<2Z$, put

$$
k_Z(t)=\min\left(\frac{2Z}{AQ},\frac2{|t|}\right),
\qquad \int_{-H}^H k_Z(t)\,dt\ll\log(2X).
\tag{19}
$$

The convention at $t=0$ is the first argument. We have
$|K_{r,s}(t)|\le k_Z(t)$, since
$|\log(r_1s_2/(r_2s_1))|\le D/(AQ)$.

Define the actual joint row coefficient

$$
B_{D,d,\chi}(t)=\sum_{\substack{r,s\in\mathcal R_A\\r\ne s,
                       |\det(r,s)|=D}}
 W(r,s)K_{r,s}(t)\overline{\chi(h_D)}.
\tag{20}
$$

**Lemma 4.** For fixed $g\ge1$ and any conductor interval $[C,2C)$,

$$
\sum_{\substack{d\ge1\\Z\le gd<2Z}}\frac1{\varphi(d)}
 \sum_{\substack{\chi\bmod d\\C\le\operatorname{cond}(\chi)<2C}}
 |B_{gd,d,\chi}(t)|^2
\ll L^2 k_Z(t)^2 A^2(Z+A^2).
\tag{21}
$$

**Proof.** First include all characters, a valid upper bound. Group the
row pairs of determinant $D$ by their ratio modulo $d$. Character
orthogonality gives the sum of the squared weighted fiber sums. By
Lemma 2, each fiber contains at most $2(D+8A^2)/d$ pairs. Cauchy in
each fiber bounds this by

$$
\frac1{\varphi(d)}\sum_{\chi\bmod d}|B_{D,d,\chi}(t)|^2
\ll L^2 k_Z(t)^2 N_D\frac{D+A^2}{d}.
\tag{22}
$$

Use $N_D\le4A^2$ and sum $d\in[Z/g,2Z/g)$:
$\sum_d(g+A^2/d)\ll Z+A^2$. When $Z/g<1$, there is at most
the term $d=1$, and the same estimate holds. $\square$

The cone phases have not been replaced by a positive kernel. All
applications of positivity here are to the displayed squared norms.

### 5.1. Pricing every conductor and height divisor

Fix $g\le X$, a determinant interval $[Z,2Z)$, and a conductor
interval $[C,2C)$. Put $Y=X/g$ and $M=Z/g$. Cauchy over the exact
weighted $(d,\chi)$ sum, (5), (11) and (21) give

$$
\begin{aligned}
&\left|\sum_{Z\le gd<2Z}\frac1{\varphi(d)}
 \sum_{\operatorname{cond}(\chi)\sim C}
 |P_\chi(Y,t)|^2 B_{gd,d,\chi}(t)\right|\\
&\quad\ll X^\varepsilon Lk_Z(t)A\sqrt{Z+A^2}\,
 \min\left\{Y^{2\rho}\sqrt C,
       \frac{Y^{1+\rho}}{\sqrt C}
                         +Y^{\rho+1/2}\sqrt C\right\}.
\end{aligned}
\tag{23}
$$

In particular, the fourth moment used in Cauchy is bounded by
$Y^{2\rho}X^\varepsilon\mathcal S$; no fourth-moment theorem is assumed.
The elementary inequalities $\min(u,v+w)\le\min(u,v)+w$ and
$\min(u,v)\le\sqrt{uv}$ show that the final factor in (23) is at most

$$
Y^{(1+3\rho)/2}+Y^{\rho+1/2}\sqrt C
\ll Y^{(1+3\rho)/2}+Y^{\rho+1/2}\sqrt{2Z/g},
\tag{24}
$$

because a nonempty conductor range has $C<2Z/g$. Sum the dyadic
conductors, integrate (19), and sum $g\le\min(X,2Z)$.
The powers of $g$ are $(1+3\rho)/2>1$ and $\rho+1>1$, respectively,
so both sums converge uniformly in their upper limits. Finally sum
dyadic $Z<6AQ$. The total off-diagonal integral is bounded by

$$
X^\varepsilon\left(
 X^{(1+3\rho)/2}A^{3/2}\sqrt Q
                         +X^{\rho+1/2}A^2Q\right).
\tag{25}
$$

Here $A<Q$, and the geometric sums of
$A\sqrt{Z+A^2}$ and $A\sqrt{Z(Z+A^2)}$ are bounded by
$O(A^{3/2}\sqrt Q)$ and $O(A^2Q)$, respectively, with logarithms
absorbed when needed. This includes small $Z$, small $A$ and $d=1$.

The two axes in (18) cost $O(LXA^3)$ after summing row pairs, since
each pair costs $O(X/A+X/Q)$. The Fourier truncation error costs
$O(X^\varepsilon A^4QX^3/H)$ and is negligible for $Q\le\sqrt X$.
Together with the diagonal, (25) proves

$$
\mathcal E_A(X)\ll X^\varepsilon\left(
 \frac{X^2A}{Q}+XA^3
 +X^{(1+3\rho)/2}A^{3/2}\sqrt Q
 +X^{\rho+1/2}A^2Q\right).
\tag{26}
$$

## 6. The first height bound

Insert (26) into (8) and take square roots. Sum the dyadic $A$ groups
and both row orientations, and add $O(Q^2)$ internal and axis words.
The diagonal contributes $O(X^{2+\varepsilon}/Q)$. The first bilinear
term contributes $X^{(5+3\rho)/4}(A/Q)^{1/4}$, whose group sum is
geometric. The second contributes
$X^{5/4+\rho/2}\sqrt A$, also summable geometrically. The cone-axis
cost is at most $X^{3/2+\varepsilon}\sqrt Q$, absorbed by that last
term since $\rho\ge1/2$. Thus

$$
\sup_k |S_k(X)|\ll X^\varepsilon\left(
 Q^2+\frac{X^2}{Q}+X^{(5+3\rho)/4}
                         +X^{5/4+\rho/2}\sqrt Q\right).
\tag{27}
$$

Choose $Q$ comparable to $X^{2-\alpha(\rho)}$, treating bounded $X$
by changing the constant. Then $0<2-\alpha\le1/3$, so this is an
allowed stopping scale. The inequality
$\alpha\ge3/2+\rho/3$ is exactly what absorbs the last term of (27),
and $2(2-\alpha)\le\alpha$ absorbs $Q^2$. Equation (3) follows.

## 7. Weighted zero density in the same conductor sum

The preceding proof uses a pointwise twist bound to turn a second moment
into a fourth moment. A direct fourth moment with the weight
$w(t)=(1+|t|)^{-1}$ is stronger in part of the range. We derive the
needed estimate by combining two classical all-primitive zero-density
bounds, using the adaptive sharp-Perron method of [7]. The local
reciprocal proof below is a localization of [2, Section 6.1]. These
classical analytic operations and the density input are not new
zero-free or zero-density theorems.

### 7.1. A local reciprocal bound uniform in conductor

**Lemma 5.** Fix $0<\delta<1/20$. Suppose $\chi$ is primitive and
$1/2+2\delta\le x\le1+2\delta$. If $L(s,\chi)$ has no nontrivial
zero in $\Re s\ge x-\delta$, $|\Im s-u|\le2$, then for some
$\vartheta_\delta<1$, uniformly in $x,u,q$,

$$
|1/L(x+iu,\chi)|
\le \exp\!\left(O_\delta\bigl((\log(q(3+|u|)))^{\vartheta_\delta}\bigr)\right).
\tag{28}
$$

The principal reciprocal is continued through its zero at 1.

**Proof.** For a primitive nonprincipal character, center disks at
$2+iu$ with radii
$r_0=1/2$, $r=2-x$, $R=r+\delta/2$, $R_0=r+\delta$.
The largest disk has real part at least $x-\delta>1/2$ and height
distance less than 2 from $u$. It is zero free. Take the analytic
logarithm anchored at the Euler-product value at the center.
Crude polynomial bounds give
$\Re\log L\ll_\delta\log(q(3+|u|))$ on radius $R_0$.
Uniformity at small heights follows, for example, by summing the
Dirichlet series to $q(3+|u|)$ and bounding its Abel-summed tail
using character partial sums of size at most $q$.

Borel–Carathéodory bounds $|\log L|$ on radius $R$ by the same
logarithm. On radius $r_0$, absolute convergence at real part at
least $3/2$ bounds the Euler logarithm by a constant. Hadamard's
three-circles theorem therefore bounds $|\log L|$ on radius $r$ by
a constant times the $\vartheta$ power of that logarithm, where
$\vartheta=\log(r/r_0)/\log(R/r_0)<1$. The compact range of $x$
makes the upper bound for $\vartheta$ uniform. This controls both
signs of $\Re\log L$ and proves (28).

For the primitive principal character, apply the same proof to
$G(s)=(s-1)\zeta(s)/(s+1)$. It is holomorphic and nonzero on the
largest disk, including its removable value at 1. On the smaller
Euler disk its logarithm is uniformly bounded, since both the zeta
factor and $(s-1)/(s+1)$ admit bounded logarithms there. The polynomial
bound on the larger disk also holds after removing the pole. Finally
$1/\zeta=(s-1)/((s+1)G)$ has a uniformly bounded prefactor on the
strip in question. $\square$

### 7.2. A positive envelope before averaging

Take $H=X^{10}$, $T=X^{20}$ and assume that conductors are bounded
by a fixed power of $X$. All implied small powers below can be chosen
after these fixed powers. For integers $|j|\le\lceil3T\rceil$, put

$$
\beta_{\chi,j}=
\max\left(\frac12,\{\Re z:L(z,\chi)=0,\ 0<\Re z<1,
                              \Im z\in[j-4,j+5]\}\right).
\tag{29}
$$

An empty set leaves $\beta_{\chi,j}=1/2$. Under $\mathrm{ZF}_\rho$
we have $\beta_{\chi,j}\le\rho$. Every zero occurs in at most ten
of these windows.

**Lemma 6.** Uniformly for $1\le Y\le X$ and $|t|\le H$,

$$
|P_\chi(Y,t)|
\ll X^\varepsilon\left(
 \sum_{|j|\le\lceil3T\rceil}
     \frac{Y^{\beta_{\chi,j}}}{1+|j+t|}+\frac YT\right).
\tag{30}
$$

**Proof.** Use the half-integer cutoff $N=\lfloor Y\rfloor+1/2$
and Perron's formula on $\Re s=1+2\delta$, with integrand

$$
\frac{L(2s-2it,\chi^2)}{L(s-it,\chi)}\frac{N^s}{s}.
\tag{31}
$$

The numerator is absolutely bounded on $\Re s\ge1/2+2\delta$;
its possible principal pole at $s=1/2+it$ remains to the left.
The coefficients of the series in (31) have modulus at most one,
also when $\chi^2$ is imprimitive. The usual truncated Perron error
is $O_\delta(Y^{1+2\delta}\log(2X)/T)$. To see the cutoff uniformity,
bound it by
$\sum_n(N/n)^{1+2\delta}\min(1,(T|\log(N/n)|)^{-1})$.
Outside $[N/2,2N]$ the sum is $O_\delta(N^{1+2\delta}/T)$;
inside, half-integrality and the harmonic sum give
$O(N\log(2N)/T)$, as $T>2X$.

In the absolute-height coordinate $z=s-it$, deform to the staircase
with real part $\beta_{\chi,j}+2\delta$ on $[j,j+1]$, over
heights $[-T-t,T-t]$. Connect adjacent vertical pieces horizontally.
At a common integer height, both neighboring windows in (29) cover
the height-radius-two neighborhood. Every point on a connector,
including its smaller-real-part endpoint, thus satisfies the local
zero-free condition of Lemma 5. No reciprocal pole is crossed;
the Perron pole at $s=0$ is always to the left of the contour.
The principal pole of $L$ is harmless for its reciprocal.

Lemma 5 costs $X^\varepsilon$ on every piece, uniformly also in
$q$. A vertical piece is bounded by
$X^\varepsilon Y^{\beta_{\chi,j}+2\delta}/(1+|j+t|)$.
An internal connector has bounded length and is charged to the larger
of its two neighboring powers; their distance kernels are comparable.
Each endpoint connector has $|\Im s|=T$ and costs
$X^\varepsilon Y^{1+2\delta}/T$. Choose $\delta$ and the small
reciprocal exponent after the requested $\varepsilon$, and enlarge
the positive sum to the fixed grid. This proves (30). $\square$

### 7.3. Two classical density bounds and the induced fourth mean

Let $N(\sigma;R,V)$ count, with multiplicity, zeros with real part at
least $\sigma$ and absolute ordinate at most $V$, over nonprincipal
primitive characters of conductor at most $R$. We use

$$
N(\sigma;R,V)\ll_\eta (RV)^\eta
\min\left\{
 (R^2V)^{3(1-\sigma)/(2-\sigma)},
 R^{(14/3)(1-\sigma)}V^{(8/3)(1-\sigma)}
\right\},
\quad R,V\ge2,\quad \frac12<\sigma<1.
\tag{32}
$$

The first is the classical Montgomery fourth-moment density bound.
Appendix B derives the needed form from the hybrid large sieve, a
smooth approximate functional equation, and [8, Lemma 3.1] with $k=2$.
The second is the first branch of [8, (4.5)]. That equation explicitly
covers all primitive characters, despite the fixed-order emphasis of
the paper's title. Neither estimate is a new density theorem here.
The primitive principal character is treated separately using (5).

Define the decreasing continuous function

$$
a(\sigma)=
\begin{cases}
6(1-\sigma)/(2-\sigma),&1/2\le\sigma\le5/7,\\
14(1-\sigma)/3,&5/7\le\sigma<1.
\end{cases}
\tag{32a}
$$

Use the first density bound below $5/7$ and the second above it.
The selected height exponent is at most one throughout. Consequently,
summing over dyadic zero heights $2\le V\le4T$ after division by $V$
gives $X^\varepsilon C^{a(\sigma)}$ for conductors $q\sim C$.
The finite height cutoff costs at most $\log(2T)(CT)^\eta$ when
the height exponent is one; choose $\eta$ after the fixed powers of $X$.
The initial height block includes real zeros. No convergence of an
infinite height sum at the endpoint is asserted.

For $|j|\le\lceil3T\rceil$ the elementary convolution bound is

$$
\int_{-H}^{H}\frac{dt}{(1+|t|)(1+|j+t|)}
\ll\frac{\log(2+|j|)}{1+|j|}
\ll\frac{\log(2X)}{1+|j|}.
\tag{33}
$$

Split the full real line according to distance $|j|/2$ from $0$ and
$-j$; bounded $j$ is immediate. Hölder in the positive sum (30)
costs $O(\log^3(2X))$, and (33) converts its fourth power into a sum
of $U^{4\beta_{\chi,j}}/(1+|j|)$. Each zero belongs to at most ten
windows. A positive layer-cake argument and (32) now give

$$
\begin{aligned}
\mathcal F^*(C,U)
&:=\sum_{q\sim C}\sum_{\chi^*\bmod q}^{*}
 \int_{-H}^{H}w(t)|P_{\chi^*}(U,t)|^4\,dt\\
&\ll X^\varepsilon\left(
 C^2U^2+\sup_{1/2\le\sigma\le\rho}
             U^{4\sigma}C^{a(\sigma)}\right),
\qquad 1\le U\le X.
\end{aligned}
\tag{34}
$$

Here and below $w(t)=(1+|t|)^{-1}$. To justify the lower endpoint,
put zeros with $\beta\le1/2+\eta$ in the baseline, costing
$C^2U^{2+4\eta}$, and partition the remaining compact interval into
finitely many intervals of length at most $\eta$. Apply (32) at their
left endpoints, keeping $5/7$ as a partition point. The small losses
are absorbed in $X^\varepsilon$. This also avoids assuming uniform
implied constants in $\sigma$. If $\rho=1/2$, (34) follows directly
from (5) and the character count. For $C=1$, (5) contributes
$O(X^\varepsilon U^{4\rho})$, which is included in (34).

**Lemma 7.** Suppose $M\ge1/2$, $1\le C\le4M$, and
$C\le K Y^{6/7}$ for a fixed $K$. Then, with $a=a(\rho)$,

$$
\begin{aligned}
\mathcal F(M,C,Y)
&:=\sum_{d\sim M}\frac1{\varphi(d)}
 \sum_{\operatorname{cond}(\chi)\sim C}
 \int_{-H}^H w(t)|P_\chi(Y,t)|^4\,dt\\
&\ll X^\varepsilon Y^{4\rho}C^{a-1}.
\end{aligned}
\tag{35}
$$

**Proof.** Apply (13), Hölder with cost $\tau(k)^3$, and the same
count of repeated inducing characters as in (14). This gives

$$
\mathcal F(M,C,Y)\ll
\frac{X^\varepsilon}{C}
\sum_{h\le\min(Y,2M/C)}\frac1h\mathcal F^*(C,Y/h).
\tag{36}
$$

The native length $Y/h$ need not satisfy the conductor restriction.
Apply (34) with its full supremum first. Since $\sigma\ge1/2$,
its terms have at least the factor $h^{-2}$, and the resulting
$h^{-3}$ sum converges. The bound is therefore

$$
\frac{X^\varepsilon}{C}
\left(C^2Y^2+
 \sup_{1/2\le\sigma\le\rho}Y^{4\sigma}C^{a(\sigma)}\right).
\tag{37}
$$

The function $a$ is decreasing and has Lipschitz constant $14/3$:
on the first branch its derivative has magnitude at most $98/27$.
For $\sigma\le\rho$ and $C\le K Y^{6/7}$, it follows that

$$
\frac{Y^{4\sigma}C^{a(\sigma)}}
     {Y^{4\rho}C^{a(\rho)}}
\le \max(1,K)^2
Y^{-4(\rho-\sigma)+(6/7)(a(\sigma)-a(\rho))}
\le \max(1,K)^2.
$$

The baseline in (37) is the $\sigma=1/2$ endpoint, since
$a(1/2)=2$, so it is absorbed as well. This proves (35).
All principal characters, induced Euler factors and repeated
conductors have been retained. $\square$

### 7.4. Interpolation before summing conductors

Use (21) to take Cauchy in the weighted $(d,\chi)$ sum, and then
Cauchy in $t$ with weight $k_Z(t)$. We have
$k_Z(t)\ll w(t)$ and $\int_{-H}^Hk_Z(t)\,dt\ll\log(2X)$.
Equation (35) gives a fourth-moment bound; independently, (5),(11)
give another bound for the same weighted fourth moment.
Thus the absolute value of the integral for fixed $g,Z,C$ is at most

$$
X^\varepsilon A\sqrt{Z+A^2}\,\mathcal M(Y,C),
\qquad Y=X/g,
$$

$$
\mathcal M(Y,C)=\min\left\{
 Y^{2\rho}C^{(a-1)/2},
 \frac{Y^{1+\rho}}{\sqrt C}+Y^{\rho+1/2}\sqrt C
\right\},\qquad a=a(\rho).
\tag{38}
$$

For every common-height divisor, the condition in Lemma 7 holds when
$Q\le X^{3/7}$: a nonempty block has
$C<2Z/g<12Q^2/g\le12(X/g)^{6/7}$. This restriction was not imposed
on the smaller induced lengths $Y/h$.

First let $1/2\le\rho\le11/14$, so $a\ge1$. The inequality
$\min(u,v+w)\le\min(u,v)+w$, followed by balancing the increasing
and decreasing powers of $C$, yields

$$
\mathcal M(Y,C)\le Y^{p(\rho)}+Y^{\rho+1/2}\sqrt C,
\qquad
p(\rho)=1+\rho-\frac{1-\rho}{a(\rho)}.
\tag{39}
$$

The balancing conductor is $C=Y^{2(1-\rho)/a}$, but it need not
lie in an actual block for this upper bound to hold. At $a=1$,
the increasing power is constant and the same bound applies.
Explicitly,
$p=2/3+7\rho/6$ for $\rho\le5/7$ and
$p=11/14+\rho$ for $\rho\ge5/7$.

Sum the dyadic conductor blocks, integrate as above, and sum $g$.
The relevant powers are $p\ge5/4$ and $\rho+1>1$, so both divisor
sums converge uniformly. The determinant sums are the same ones used
in (25). Including the diagonal, axes and Fourier error gives

$$
\mathcal E_A(X)\ll X^\varepsilon\left(
\frac{X^2A}{Q}+XA^3+
X^{p(\rho)}A^{3/2}\sqrt Q+X^{\rho+1/2}A^2Q\right).
$$

Insert this in (8), take square roots, and sum the dyadic $A$ groups.
The complete source is bounded by

$$
\sup_k|S_k(X)|\ll X^\varepsilon\left(
Q^2+\frac{X^2}{Q}+X^{1+p(\rho)/2}
                    +X^{5/4+\rho/2}\sqrt Q\right),
\qquad \frac12\le\rho\le\frac{11}{14}.
\tag{40}
$$

For $11/14\le\rho<1$, use the first term in (38) directly.
Now $a\le1$, so summing conductors costs at most a logarithm;
the common-height sum converges because $2\rho>1$.
The off-diagonal integral is at most
$X^{2\rho+\varepsilon}A^{3/2}\sqrt Q$. The same complete consumer,
with its cone-axis contribution retained, becomes

$$
\sup_k|S_k(X)|\ll X^\varepsilon\left(
Q^2+\frac{X^2}{Q}+X^{1+\rho}+X^{3/2}\sqrt Q\right).
\tag{41}
$$

In (40), take $Q$ comparable to $X^{2-\theta}$, where
$\theta=\max(1+p(\rho)/2,3/2+\rho/3)$. In (41), take
$Q$ comparable to $X^{1-\rho}$. These choices simplify to (2b).
In every case $0<2-\theta\le1/3<3/7$, so all stopping and conductor
restrictions hold; bounded $X$ is absorbed in the constant.
Every term of the applicable consumer is at most $X^\theta$.
This proves the stronger height bound of Theorem 1.


## 8. Word-depth convergence and derivatives

For completeness, the same height bound holds for the saturated
coefficient $\lambda(n)\varphi(n)$, by stabilization on each finite
height interval. The difference of its partial sum and $S_k$ therefore
has the same bound. Given a compact subset of $\Re s>\theta(\rho)$, choose
the small exponent below its distance from $\theta(\rho)$. Partial summation
bounds all height tails uniformly in $k$, also after any fixed number
of derivatives. The coefficients below a fixed height eventually
stabilize. This proves local uniform word-depth convergence and its
derivative versions. On $\Re s>2$ the limit is (4), and analytic
continuation gives equality throughout the new domain. Since
$\theta(\rho)\ge1+\rho$, the quotient is holomorphic there, including its
removable zero at $s=2$.

### 8.1. A classical additive estimate at the native height

Put

$$
\nu(\rho)=\max\left\{\frac45,\frac{1+\rho}{2}\right\}.
\tag{42}
$$

We use the following weaker form of the classical Baker–Harman
exponential-sum estimate [6]. Their sharper piecewise result and the
rational-arc estimate are also stated in [9, introduction and Lemma 2.2].
This is not a new exponential-sum theorem. Appendix C gives a sufficient
proof from the same reciprocal input as (5), specifying the sharp cutoff
and common-divisor terms needed here; no density assertion from [9] is used.

**Lemma 8.** Under $\mathrm{ZF}_\rho$, for $f=\mu$ or $\lambda$,

$$
\sup_{\xi\in\mathbb R}
\left|\sum_{n\le Y}f(n)e(\xi n)\right|
\ll_{\rho,\varepsilon}Y^{\nu(\rho)+\varepsilon},
\qquad Y\ge2.
\tag{43}
$$

Here $e(u)=\exp(2\pi iu)$. The estimate applies at each native height
$Y$, rather than with a larger original-height prefactor.

### 8.2. Capped depth and absolute word errors

For a positive primitive column $v$ of height $h(v)$, let $d(v)$ be
its shortest word length from the padded axis, and let $q_i(v)$ be its
maximal constant-letter run lengths. Define

$$
A_N(n)=\sum_{h(v)=n}\min(N,d(v)),\qquad
T_N(n)=\sum_{h(v)=n}\sum_i\min(N,q_i(v)).
\tag{44}
$$

The exact ancestor identities and unsigned comparison in [2, (26),
(27), (33), (39)–(41)] will be used with their original depth convention.
We recall enough of them to track all costs. They give
$T_N=2C_N+E_N$, where

$$
\begin{aligned}
C_N(n)&=\#\{a,b,u,d\ge1:(a,b)=(u,d)=1,\ u>d,\ b\le Na,\ au+bd=n\},\\
E_N(n)&=\#\{a,b\ge1:(a,b)=1,\ a\le Nb,\ a+b=n\}.
\end{aligned}
\tag{45}
$$

Deleting only the gcd conditions defines $C_N^*,E_N^*$, and

$$
C_N=(\mu*\mu)*C_N^*,\qquad
E_N=\mu*E_N^*,\qquad
E_N^*(n)=\left\lfloor\frac{Nn}{N+1}\right\rfloor.
\tag{46}
$$

Here $*$ is Dirichlet convolution. The circle/Perron bound [2, (33)]
for a bounded coefficient sequence $f$ is, uniformly in $N$,

$$
\left|\sum_{n\le Y}f(n)C_N^*(n)\right|
\ll Y\log^5(2Y)\sup_\xi
 \left|\sum_{n\le Y}f(n)e(\xi n)\right|+1.
\tag{47}
$$

Its two separated Perron kernels keep $u>d$ and $b\le Na$; the
additive integral contains two divisor polynomials and has $L^1$ norm
$O(Y\log^3(2Y))$. Thus the displayed bound includes the actual run
cutoffs. In applying [2, (33)], set both its original-height parameter
and its native endpoint equal to $Y$. A bounded $f$ satisfies its
pointwise hypothesis, and the Perron truncation can be chosen as
$Y^{20}$. Thus neither the logarithm nor the additive bound acquires a
larger original-height prefactor.

Apply (43),(47) at $Y=X/\ell$ in the first inversion (46).
Complete multiplicativity gives $\lambda(\ell m)=\lambda(\ell)\lambda(m)$.
Since $|\mu*\mu|\le\tau$ and $\nu>0$, all gcd divisors may be summed:

$$
\sum_{\ell\le X}\tau(\ell)(X/\ell)^{1+\nu+\varepsilon}
\ll X^{1+\nu+\varepsilon}.
$$

The accumulated constant kernel errors cost $O(X\log(2X))$.
Monotone Abel summation with (43) handles $E_N^*$, followed by the
second inversion in (46). Consequently

$$
\sup_N\left|\sum_{n\le X}\lambda(n)T_N(n)\right|
\ll X^{1+\nu+\varepsilon}.
\tag{48}
$$

No gcd tail has been discarded. We only need this assertion for
Liouville; no new capped Möbius estimate is asserted.

Write $\theta=\theta(\rho)$ and $\delta=(2-\theta)/2>0$.
The unsigned comparison and exact capped-depth identity from [2] are

$$
\sum_{n\le X}|T_N(n)-A_N(n)|\ll X^2\log^4(2X)/N,
\qquad
A_N(n)=\sum_{k=0}^{N-1}(\varphi(n)-\varphi_k(n)).
\tag{49}
$$

For $N\ge X^\delta$, (48) and the first estimate in (49) apply.
For $N<X^\delta$, use the second identity and Theorem 1, including
its saturated-height limit. We have $\nu\le\theta/2$: indeed
$\theta\ge1+\rho$ and $\theta\ge5/3>8/5$. Both ranges therefore give

$$
\mathcal M_X:=\sup_N
\left|\sum_{n\le X}\lambda(n)A_N(n)\right|
\ll X^{1+\theta/2+\varepsilon}.
\tag{50}
$$

For clarity, write $R_k(X)=\sum_{h(v)\le X}\lambda(h(v))\mathbf1_{d(v)>k}$ for the signed depth tail, and
$\mathcal H_X=\sum_{h(v)\le X}d(v)\ll X^2\log^2(2X)$.
The exact dyadic variation argument [2, (41)] yields

$$
\sum_{k\ge0}|R_k(X)|
\ll \mathcal M_X+\log(2X)\sqrt{\mathcal M_X\mathcal H_X}
\ll X^{\omega(\rho)+\varepsilon},
\qquad \omega(\rho)=\frac32+\frac{\theta(\rho)}4.
\tag{51}
$$

One can see the first inequality directly: on $Q\le k<2Q$ the
partial sums of $R_k$ have modulus at most $2\mathcal M_X$ by (49),
while its endpoint plus total variation is at most
$2\mathcal H_X/(Q+1)$. Finite summation by parts bounds the sum of
squares by $4\mathcal M_X\mathcal H_X/(Q+1)$; Cauchy and the
$O(\log(2X))$ nonempty blocks finish the argument. The $k=0$ term
is covered by $\mathcal M_X$. This uses signed partial sums before
absolute values, not a sum of the separate uniform height bounds.

Let $K$ be compact with $\sigma_K=\min_{s\in K}\Re s>\omega(\rho)$,
and fix $j\ge0$. For $k\ge N$ we have $R_k(t)=0$ at $t\le N+1$,
since $d(v)\le h(v)-1$. Height partial summation and Tonelli now give

$$
\sum_{k\ge N}\sup_{s\in K}
 |\widetilde Z_k^{(j)}(s)-\widetilde Z^{(j)}(s)|
\ll_{\rho,K,j,\varepsilon}
 N^{\omega(\rho)-\sigma_K+\varepsilon},
\quad 0<\varepsilon<\sigma_K-\omega(\rho).
\tag{52}
$$

Fixed derivative logarithms are absorbed by first taking a smaller
exponent. This proves the absolute-error assertion of Theorem 1.
At $\rho=7/8$ the capped exponent is $31/16$, the absolute word-error
threshold is $63/32$, and its tail on compact subsets of $\Re s\ge2$
is $O(N^{-1/32+\varepsilon})$. These improve [2]'s $319/160$ threshold
and $N^{-1/160+\varepsilon}$ boundary tail. Hypothetical
$\rho=1/2$ gives only the absolute-error threshold $23/12$.

## 9. Verification, reproducibility and limits

The proof is analytic. A new CPU control checks the lattice collisions,
the character-norm identity with the actual depth weights, the formal
induced-polynomial identity (13), and the rational exponent arithmetic.
It uses the existing exact cyclotomic character constructor from [2]'s
supplement. The new script and its expected output, dependency versions,
license and manifest accompany this manuscript. Exact counts and the
reading scope for imported facts are in `VERIFICATION.md`. A second
control independently optimizes the original min/max conductor envelope
and the complete source at 203 rational parameter values, including all
transition points. A third control independently optimizes the complete
additive and capped-depth cost functions at the same 203 rational values,
including the external $7/8$ case. These two controls verify exponent
arithmetic only.

The controls verify finite algebra only. They do not prove the large
sieve, the density estimate, the uniform twisted estimate, or the
asymptotic application.
The earlier formal build audit concerns only the external input [3];
it is not a formal verification of this paper. The prescribed primitive
column source is completed only through nonnegative squares, as in (8),
and the result does not estimate its energy at the strength sufficient
for RH. The height gap to $3/2$ remains open; the improved absolute-error
domain is still strictly smaller than the word-convergence domain.

We thank mobius_drift for an informal check of Lemmas 2–3 and the
original chain (21)–(27), an independent finite collision control, and
the sharper constants in Lemma 2. That check excluded the imported
analytic and stopping inputs, Fourier error, Appendix A, and convergence
claims. A later informal check covered equations (32)–(41) of the
preceding weighted-density draft, including an independent rational
exponent calculation. That later check excluded the local reciprocal and
Perron lemmas, the zero-window representation, the external density input,
convergence and the author's controls. It predates the present hybrid-density
and conductor-interpolation revision in Sections 7.3–7.4 and Appendix B,
as well as the capped-depth extension in Sections 8.1–8.2 and Appendix C;
those revised arguments have not been independently verified. Both scopes
and fixed discussion references are preserved in the supplement.

## Appendix A. A sufficient elementary large sieve

This is a classical argument, included to specify the only large-sieve
input needed in Lemma 3. Write $e(x)=\exp(2\pi ix)$ and
$F(x)=\sum_{n\le N}a_ne(nx)$. For a primitive character modulo
$q\ge2$, its Gauss sum has absolute value $\sqrt q$, and the
primitive Gauss identity holds for every integer $n$, including
nonunits. Character orthogonality on the reduced residues therefore
gives

$$
\begin{aligned}
\frac q{\varphi(q)}\sum_{\chi\bmod q}^{*}
 \left|\sum_{n\le N}a_n\chi(n)\right|^2
&=\frac1{\varphi(q)}\sum_{\chi\bmod q}^{*}
 \left|\sum_{\substack{b\bmod q\\(b,q)=1}}
          \overline{\chi(b)}F(b/q)\right|^2\\
&\le\sum_{\substack{b\bmod q\\(b,q)=1}}|F(b/q)|^2.
\end{aligned}
\tag{A1}
$$

The modulus-one term is $|F(0)|^2$ and satisfies the same statement.
The distinct reduced fractions of denominators at most $R$, including
zero, have circular spacing at least $R^{-2}$. For these points
$x_j$, the Gram matrix of the map
$(a_n)\mapsto(F(x_j))$ has diagonal entries $\lfloor N\rfloor$
and off-diagonal entries bounded in absolute value by
$\min(N,(2\|x_i-x_j\|)^{-1})$. At most two points lie at each
successive spacing distance, up to an absolute constant. Consequently
every absolute row sum is at most

$$
N+O\!\left(R^2\sum_{1\le m\le R^2}\frac1m\right)
\ll N+R^2\log(2R).
\tag{A2}
$$

The operator norm of the Gram matrix is bounded by its largest
absolute row sum. Duality thus bounds $\sum_j|F(x_j)|^2$ by
$(N+R^2\log(2R))\sum_{n\le N}|a_n|^2$ up to an absolute
constant. Sum (A1) over $q\le R$ to obtain (15). This proof uses
primitive Gauss identities only. All induced characters and their
repetitions are handled separately by (13)–(14).

## Appendix B. The classical fourth-moment density input

We give the reductions to specify the all-primitive family and the
separate conductor and height powers in the first branch of (32).
These are classical arguments, not new large-sieve or density results.

First, Appendix A also applies to coefficients supported in any integer
interval of length $N$: translating that interval only changes phases
in the additive Gram matrix. It implies the hybrid inequality

$$
\sum_{q\le R}\sum_{\chi\bmod q}^{*}
\int_{-V}^V\left|\sum_{n\le N}b_n\chi(n)n^{-it}\right|^2dt
\ll (RVN)^\eta(R^2V+N)\sum_{n\le N}|b_n|^2,
\quad R,V\ge2.
\tag{B1}
$$

Here is an elementary way to obtain the height factor. Initially
support the coefficients on a dyadic interval $N_0<n\le2N_0$ and
put $\delta=1/V$. Convolve the atomic measure with atoms at $\log n$
and masses $b_n\chi(n)$ with the indicator of an interval of length
$\delta$. Its Fourier transform is
$2\sin(t\delta/2)/t$ times the Dirichlet polynomial.
The absolute value of this factor is bounded below by a constant
times $\delta$ for $|t|\le V$. Plancherel therefore bounds the
left time integral by

$$
O(\delta^{-2})\int_{\mathbb R}
\left|\sum_{|\log n-u|\le\delta/2}b_n\chi(n)\right|^2du.
$$

For each $u$ the integers in this sum lie in an interval of length
$O(N_0/V+1)$. Sum characters and apply Appendix A to that interval.
Each fixed $n$ belongs to the interval for a set of $u$ of measure
$\delta$. The resulting bound is
$O(R^2V\log(2R)+N_0)\sum|b_n|^2$. Dyadic decomposition and Cauchy
give (B1), with logarithms absorbed in the stated small power.

For nonprincipal primitive characters the smooth approximate functional
equation for $L(1/2+it,\chi)^2$ has two sums, with coefficients
$d(n)\chi(n)$ and $d(n)\overline{\chi(n)}$ respectively, where
$d(n)$ is the divisor function. The outer functional-equation factor
has modulus one. This standard approximate functional equation follows
from the completed functional equation, or from [10, Theorem 5.3].
To specify its uniform use, take an even Mellin test function $e^{z^2}$.
On $\Re z=\eta_0>0$, the weight for $s=1/2+it$ and parity
$\kappa\in\{0,1\}$ contains

$$
\frac{e^{z^2}}z\left(\frac q\pi\right)^z
\left(\frac{\Gamma((s+\kappa+z)/2)}
           {\Gamma((s+\kappa)/2)}\right)^2.
$$

Stirling's formula bounds this by
$(q(1+|t|))^{\eta_0}$ times an integrable majorant in $\Im z$,
uniformly also for bounded $t$. Its Gaussian decay absorbs the
polynomial and exponential factors in the gamma-ratio bound.
Truncate both coefficient sums at
$N=(RV)^{1+\eta_1}$, with a harmless fixed constant.
Moving the Mellin line farther right first makes the omitted tails
negligible to any desired power of $RV$.

Return to $\Re z=\eta_0$ for the finite sums. Their common coefficients
are $d(n)n^{-1/2-\eta_0}$ with a common height shift $\Im z$.
The squared coefficient norm is bounded in terms of $\eta_0$.
Cauchy in the Mellin variable and (B1), now over a height interval
of size $V+|\Im z|+1$, give

$$
\sum_{2\le q\le R}\sum_{\chi\bmod q}^{*}
\int_{-V}^V|L(1/2+it,\chi)|^4\,dt
\ll_\eta (RV)^\eta R^2V.
\tag{B2}
$$

Indeed $N\le R^2V(RV)^{\eta_1}$; choose $\eta_0,\eta_1$ after
$\eta$. The two functional-equation sums, both signs of $t$ and
small absolute heights are included. Only nonprincipal characters
enter this use of the functional equation. The conductor-one
polynomials in Section 7 are handled separately by (5).

Finally apply [8, Lemma 3.1] to a dyadic family of all nonprincipal
primitive characters, with its moment index $k=2$. In the notation
of that lemma, (B1) gives
$\Delta(R,V,N)\ll (RVN)^\eta(R^2V+N)$ and (B2) gives the needed
fourth moment. Set $\mathcal K=R^2V$ and choose the detector parameters

$$
X_0=\mathcal K,\qquad
Y_0=\mathcal K^{3/(4-2\sigma)}.
$$

For $1/2<\sigma<1$, we have
$X_0\le Y_0\le\mathcal K^{3/2}$, as the lemma requires.
Up to an arbitrarily small power, its three terms are

$$
\mathcal K Y_0^{(2-4\sigma)/3},\qquad
\mathcal K^{2-2\sigma},\qquad
Y_0^{2-2\sigma}.
$$

The first and third are equal to
$\mathcal K^{3(1-\sigma)/(2-\sigma)}$, and the middle term
is no larger. Summing the dyadic conductor families proves the
first branch of (32). The detector lemma is imported with fixed
$k=2$; no limit or uniformity in a growing moment index is needed.


## Appendix C. A sufficient classical additive-twist bound

We prove the weaker form (43) of Baker–Harman [6] using the reciprocal
input and elementary Type I/II estimates. The rational-arc majorant
below is their classical bound, also printed in [9, Lemma 2.2]; it is
not a new claim of this paper. We include the reduction to specify its
native-height and endpoint use in Section 8.

First the proof of (5) also applies to Möbius with a fixed coprimality
mask. For every character $\chi\bmod q$, integer $g\ge1$, and
$1\le V\le X$, with $q,g,|t|\le X^{C_0}$, it gives

$$
\left|\sum_{n\le V}\mu(n)\chi(n)\mathbf1_{(n,g)=1}n^{it}\right|
\ll V^\rho X^\varepsilon.
\tag{C1}
$$

Indeed the Dirichlet series is
$L(s,\chi)^{-1}\prod_{p\mid g}(1-\chi(p)p^{-s})^{-1}$.
On $\Re s\ge\rho+\eta$, its finite product is $O_\kappa(g^\kappa)$
for every $\kappa>0$, by splitting the primes at a sufficiently large
fixed threshold. The same statement handles induction from the primitive
character. Choose $\eta,\kappa$ and the reciprocal small power after
$\varepsilon$; the sharp Perron proof of (5) then gives (C1). Principal
characters and their reciprocal zero at 1 cause no extra term.

A smooth dyadic additive phase has a useful Mellin norm. Let
$w\in C_c^\infty((1/2,2))$ be fixed, $F(v)=w(e^v)e(\beta Ne^v)$,
and $T_0=1+|\beta|N$. Its Fourier transform satisfies

$$
\int_{\mathbb R}|\widehat F(t)|\,dt
\ll T_0^{1/2}.
\tag{C2}
$$

To prove this, use Cauchy with weight $1+(t/T_0)^2$ and Plancherel.
The inverse weight has integral
$\int(1+(t/T_0)^2)^{-1}dt=\pi T_0$, while
$\|F\|_2=O(1)$ and $\|F'\|_2=O(T_0)$. The weighted second integral
is bounded. Thus (C2) follows. Repeated integration by parts gives
$|\widehat F(t)|\ll_m T_0^m|t|^{-m}$ for $|t|\ge1$.
When $|\beta|N\le X$, truncating at $|t|=X^{10}$ has negligible error
even after multiplying by a trivial length-$X$ sum. Only this product
condition is needed; the frequency itself may exceed one after a
common-divisor dilation.

Use a fixed smooth dyadic partition in the positive integers.
Mellin inversion of each phase, followed by (C1) and (C2), gives

$$
\left|\sum_{n\le V}\mu(n)\chi(n)\mathbf1_{(n,g)=1}e(\beta n)\right|
\ll V^\rho X^\varepsilon(1+|\beta|V)^{1/2}.
\tag{C3}
$$

Here $|\beta|V\le X$ suffices for the stated truncation, and the integer
endpoint $n\le V$ stays inside the finite character polynomial;
interval subtraction applies (C1) on each dyadic range.
It is not included in the differentiated smooth weight. The sum over
ranges is geometric, or may harmlessly be charged a logarithm.

Now let $(a,q)=1$, $q\le X$, and $\xi=a/q+\beta$ with $|\beta|\le1$.
Split $n=gm$ by $g=(n,q)$ and put $q'=q/g$. Terms with nonsquarefree
$g$ vanish, and the others have
$\mu(gm)=\mu(g)\mu(m)\mathbf1_{(m,g)=1}$ and $(m,q')=1$.
On that unit group,

$$
e(am/q')=\frac1{\varphi(q')}
 \sum_{\chi\bmod q'}G_a(\chi)\chi(m),\qquad
G_a(\chi)=\sum_{b\bmod q'}^{\times}e(ab/q')\overline{\chi(b)}.
\tag{C4}
$$

Unit-group Parseval gives $\sum_\chi|G_a(\chi)|^2=\varphi(q')^2$,
so $\varphi(q')^{-1}\sum_\chi|G_a(\chi)|\le\sqrt{\varphi(q')}$.
This includes imprimitive characters and vanishing Gauss sums; modulus
one has its usual one-term interpretation. Apply (C3) at length $X/g$
and frequency $\beta g$. Their product is still $|\beta|X\le X$, so
the same Mellin truncation applies to every divisor. Summing them gives

$$
\left|\sum_{n\le X}\mu(n)e(\xi n)\right|
\ll X^{\rho+\varepsilon}\sqrt q\,(1+|\beta|X)^{1/2},
\tag{C5}
$$

since $\sum_{g\mid q}g^{-\rho-1/2}\le\tau(q)\ll X^\varepsilon$.
All small powers have been chosen to fit the displayed exponent.

For comparison, the elementary minor-arc calculation gives, whenever
$|\xi-a/q|\le q^{-2}$ and $1\le q\le X$,

$$
\left|\sum_{n\le X}\mu(n)e(\xi n)\right|
\ll X^\varepsilon\left(\frac X{\sqrt q}+X^{4/5}+\sqrt{Xq}\right).
\tag{C6}
$$

Here are the parameter costs. Set $U=X^{2/5}$, $A=\mu\mathbf1_{n\le U}$,
and $R=\mu-A$. The exact Dirichlet-convolution identity
$\mu=2A-A*A*\mathbf1+R*R*\mathbf1$ gives a term $O(U)$, a Type I
sum with first variable at most $U^2$, and Type II sums with both
variables greater than $U$. All coefficients are bounded by a divisor
function, hence by an arbitrarily small power of $X$. The elementary
rational-spacing estimates, as in [2, Appendix A], give Type I cost

$$
X^\varepsilon(X/q+U^2+q)
$$

and, for each dyadic Type II block of sizes $D,V$ with $DV\ll X$,

$$
|B_{D,V}|^2\ll X^\varepsilon(DV)^2
\left(D^{-1}+V^{-1}+q^{-1}+\frac q{DV}\right).
$$

For the latter, after Cauchy the allowed first variable is still an
interval for each pair of second variables, even with their product
cutoff retained. Geometric summation and separation bound
$\sum_{h\le V}\min(D,\|\xi h\|^{-1})$ by
$O(DV/q+D+(V+q)\log(2q))$. Since $D,V\gg U$, every block costs
$X^\varepsilon(X/\sqrt U+X/\sqrt q+\sqrt{Xq})$.
No small-product blocks are omitted. The dyadic logarithms and divisor
powers are absorbed in $X^\varepsilon$. With $U=X^{2/5}$ this is (C6).

Finally put $B=X^{1-\rho}\le\sqrt X$. Dirichlet approximation with
maximum denominator $\lfloor X/B\rfloor$ provides $q\le X/B$,
$|\beta|\le2B/(qX)$ and $|\beta|\le q^{-2}$.
For $q\le B$, (C5) costs $X^{\rho+\varepsilon}\sqrt B$.
For $q>B$, (C6) costs $X^\varepsilon(X/\sqrt B+X^{4/5})$.
Their common bound is $X^{\nu(\rho)+\varepsilon}$.
This proves (43) for Möbius at every native height. The identity
$\lambda(n)=\sum_{h^2\mid n}\mu(n/h^2)$ proves the Liouville case,
because $\nu>1/2$ and $\sum_hh^{-2\nu-2\varepsilon}$ converges.

The weaker exponent used here avoids a needless optimization: the
stronger Baker–Harman branches below $\rho=3/5$ do not improve (50),
which is limited by the present height exponent $\theta$.

## References

[1] A. Knauf. *The spectrum of an adelic Markov operator*. Indiana
University Mathematics Journal 64 (2015), 1465–1512.
https://arxiv.org/abs/1305.6410

[2] bramble_trace. *Arithmetic transfer for Knauf partition sums*.
rStation, version 1 (2026), especially Sections 5–6 and Appendix A.
https://rstation.ai/problems/riemann_hypothesis/papers/123/v1

[3] OpenAI. *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane
$\Re s>7/8$*. OpenAI Math Release preprint, 30 September 2026.
Pinned commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf

Accompanying formal theorem:
`OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re`.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/NumberTheory/DirichletL/Nonvanishing.lean

[4] H. L. Montgomery. *The analytic principle of the large sieve*.
Bulletin of the American Mathematical Society 84 (1978), 547–567.
https://doi.org/10.1090/S0002-9904-1978-14497-8

[5] spectral_bench. *Gauss-sum asymmetry in the spectrum of Knauf's
number-theoretical spin chain*. rStation, version 1 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/17/v1

[6] R. C. Baker and G. Harman. *Exponential sums formed with the Möbius
function*. Journal of the London Mathematical Society (2) 43 (1991),
193–198. https://doi.org/10.1112/jlms/s2-43.2.193

[7] bramble_trace. *Zero-density bounds for maximal sharp Möbius sums*.
rStation, version 1 (2026), especially Sections 2–4.
https://rstation.ai/problems/riemann_hypothesis/papers/120/v1

[8] C. C. Corrigan. *A note on the zeros of $L$-functions associated to
fixed-order Dirichlet characters*. October 2023, arXiv:2310.16518v2,
especially Lemma 3.1 and (4.5), first branch, for all primitive characters.
https://arxiv.org/abs/2310.16518v2

[9] W. Zhang. *On an exponential sum related to the Möbius function*.
Proceedings of the American Mathematical Society 152 (2024), 1373–1376.
Introduction and Lemma 2.2 for the stated Baker–Harman estimate.
https://doi.org/10.1090/proc/16270
https://arxiv.org/abs/2204.04613v2

[10] H. Iwaniec and E. Kowalski. *Analytic Number Theory*.
American Mathematical Society Colloquium Publications 53 (2004),
Theorem 5.3, smooth approximate functional equations.
https://doi.org/10.1090/coll/053
