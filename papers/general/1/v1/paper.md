# Mean-square profiles for full continued-fraction cost sources

## 1. The source and the result

This paper asks whether the full continued-fraction cost distribution at
an individual denominator can be approximated by the profile obtained
from its summatory transfer operator. We prove a mean-square approximation
and a stable law outside a power-saving exceptional set. These are
results about Euclidean costs and arithmetic dynamics. The signed Knauf
application in Section 7 is conditional on scalar Liouville cancellation;
no new information about the locations of zeta zeros is asserted.

For a positive primitive column $v=(a,b)^{\mathsf T}$, let $d(v)$ be the
length of its shortest word from $e_1=(1,0)^{\mathsf T}$ in the matrices

$$
L=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
R=\begin{pmatrix}1&0\\1&1\end{pmatrix}.
$$

Products act on the column from the left. The shortest word ends on the
right with $R$. Define, for $n\ge2$ and $\theta\in\mathbb R$,

$$
C_\theta(n)=\sum_{\substack{1\le a<n\\(a,n)=1}}
 e^{i\theta d(a,n-a)},\qquad
\varphi_k(n)=\#\{1\le a<n:(a,n)=1,\ d(a,n-a)\le k\}.
\tag{1}
$$

Thus $C_0(n)=\varphi(n)$, with $\varphi$ Euler's totient. The unique
padding convention identifies $\varphi_k$ with the coefficients of
Knauf's length-$k$ partition [1]. We keep the actual shortest-word cost,
with no restriction on partial quotients and no selected ensemble.

The scalar Gauss-transfer asymptotic of Bettin--Drappeau [2] and its
all-frequency extension used in [3, Section 4] provide constants
$\theta_0,\delta>0$ and bounded functions $c(\theta),s(\theta)$ such that

$$
\sum_{2\le n\le Y}C_\theta(n)=
\begin{cases}
c(\theta)Y^{s(\theta)}+O(Y^{2-\delta}),&|\theta|\le\theta_0,\\
O(Y^{2-\delta}),&\theta_0<|\theta|\le\pi.
\end{cases}
\tag{2}
$$

We can arrange $3/2\le\Re s(\theta)\le2$ and $|s(\theta)|\le3$.
With the notation of [2, Theorem 3.1], $s=2+U$ and
$c=e^{-i\theta+V}/(2\zeta(2))$: their digit-sum convention is
$\Sigma(a/n)=d(a,n-a)+1$. Define the residue profile

$$
M_\theta(n)=
\begin{cases}
\zeta(2)c(\theta)s(\theta)\varphi(n)n^{s(\theta)-2},
   &|\theta|\le\theta_0,\\
0,&\theta_0<|\theta|\le\pi,
\end{cases}
\tag{3}
$$

and extend it periodically in $\theta$. In particular $M_0(n)=\varphi(n)$.
The functions in (3) come from the scalar residue, without fitting the
height coefficients or differentiating in $\theta$.

Let $\eta>0$ be the uniform primitive-row congruence saving recalled
precisely in Section 5. Both $\eta$ and $\delta$ may be decreased to absorb
fixed logarithms in the imported results.

**Theorem 1 (coefficient profile).** Uniformly for real $\theta$,
$X\ge2$, and $2\le B\le X^{1/100}$,

$$
\sum_{X<n\le2X}|C_\theta(n)-M_\theta(n)|^2
\ll_\varepsilon X^\varepsilon\left(
 X^3B^{-1/2}+X^{3-2\eta}B^6+
 X^{3-2\delta}B^3+X^3B^{-2}\right).
\tag{4}
$$

Consequently, for

$$
\kappa=\min\left(\frac1{400},\frac\eta{13},\frac\delta7\right)>0,
\qquad
\sup_{\theta\in\mathbb R}
\sum_{X<n\le2X}|C_\theta(n)-M_\theta(n)|^2
\ll_\varepsilon X^{3-2\kappa+\varepsilon}.
\tag{5}
$$

No numerical value of the two imported spectral savings is asserted.
The elementary new input is a minor-arc estimate for the full source.
Write $e(t)=e^{2\pi it}$, $\mathbb T=\mathbb R/\mathbb Z$, and fix
$w\in C_c^\infty((1/2,3))$. Put

$$
S_{\theta,w}(\alpha)=\sum_{n\ge2}w(n/X)C_\theta(n)e(n\alpha),
\qquad
\mathfrak M_X(B)=\bigcup_{q\le B}\ \bigcup_{a\bmod q}^{*}
 \{\alpha:\|\alpha-a/q\|\le2B/X\}.
$$

**Theorem 2 (full-source minor energy).** For $2\le B\le X^{1/4}$,

$$
\sup_{\theta\in\mathbb R}
\int_{\mathbb T\setminus\mathfrak M_X(B)}
 |S_{\theta,w}(\alpha)|^2\,d\alpha
\ll_{w,\varepsilon}X^{3+\varepsilon}B^{-1/2}.
\tag{6}
$$

The same estimate, up to logarithms, holds with $C_\theta(n)$ replaced
by any sharp depth cap $\varphi_k(n)$. Pairing its minor projection
against any coefficients of modulus at most one on $(X,2X]$ costs at
most $X^{2+\varepsilon}B^{-1/4}$.

The distinction from previous work is at the source. Bourgain--Kontorovich
[4, Section 5] develop the bilinear Cauchy--Poisson method for their
selected thin ensemble. We reproduce its relevant counting arguments for
all primitive words and their actual cost phase. Exact cardinalities in
two stopping geometries replace dimension losses and discarded cones.
A full additive Fourier integral treats the height window. The congruence
and scalar inputs in (2) and Section 5 are prior results from [2,3,5];
they are not proved anew here. Earlier Knauf stopping and conductor
estimates [6,7] control signed consumers under arithmetic hypotheses;
(4) instead estimates the cost coefficients themselves relative to their
complete residue profile. This is the substantive contribution, alongside
its stronger minor projection. The scalar consequence in Section 7 uses
only the same scalar Liouville assumption as [3].

The coefficient estimate also gives an individual-denominator consequence.
Aistleitner--Borda--Hauke [8] prove concentration and tail bounds for every
denominator and discuss the remaining fixed-denominator limit-law question.
In Section 8 we prove the Bettin--Drappeau stable law for each denominator
outside a set with counting function $O_\varepsilon(Y^{1-\kappa+\varepsilon})$.
The error is uniform over all distribution thresholds. The stable law over
all Farey fractions is the prior theorem [2, Theorem 2.5]; the passage to
individual denominators uses the new mean-square estimate. A limit law for
every denominator remains open here.

The bound (5) is still close to cubic. It does not reach the
$X^{2+\varepsilon}$ coefficient energy that would give a square-root
average residual, and it does not prove RH or a new zero-free region.

## 2. Stopping words and the bilinear inequality

### 2.1. Exact source factorization

The subtractive Euclidean algorithm proves that each positive primitive
column has one shortest word. Conversely, every word ending on the right
with $R$ is shortest for its column. Starting with the row $(1,1)$ and
multiplying the letters in product order gives an injective binary tree:
from a row $(u,v)$ the children are $(u,u+v)$ and $(u+v,v)$, and the parent
is recovered by subtracting the smaller coordinate. Thus a word ending
with $R$ has terminal row $(n,b)$ with $1\le b<n$ and $(n,b)=1$, where
$n$ is its column height. The word is determined by this row as well.

For any prefix code obtained by first hitting a monotone row condition,
a shortest word continuing strictly beyond its stopping prefix factors
uniquely as $PV$, where $V$ is a shortest positive suffix. If
$r=(1,1)P$ and $v=Ve_1$, then

$$
h(PV)=r\cdot v,\qquad d(PV)=|P|+d(v).
\tag{7}
$$

Therefore its cost phase is the product of a row phase and a suffix
phase, each of modulus one. Words that stop at their last letter have
axis suffix $e_1$; words that do not stop are separate boundary terms.
We count these terms explicitly below. The height window in (7) is not
a product of a row weight and a suffix weight.

### 2.2. Cauchy and Poisson with bounded coefficients

Suppose a row set $\mathcal R$ is contained in a fixed box of side $O(Z)$
and has cardinality $H$, and a finite positive primitive suffix set is
$\mathcal V$. For coefficients of modulus at most one, Cauchy in the
rows followed by a nonnegative smooth majorant and Poisson summation
bounds a bilinear sum by

$$
C H^{1/2}Z\,
\#\{(v,v')\in\mathcal V^2:
       \|\alpha(v-v')\|_\infty\le c_0/Z\}^{1/2}.
\tag{8}
$$

Here the distance is coordinatewise to $\mathbb Z^2$, and $c_0>0$ can
be any sufficiently small fixed constant. To see the asserted majorant,
take the squared modulus of the inverse Fourier transform of a smooth
compact bump, scaled so that it is positive on the fixed row box and
has Fourier support in $[-c_0,c_0]^2$. Multiplying by a fixed constant
makes it at least one there. After Poisson, every lattice sum is zero
unless the frequency difference lies within $c_0/Z$ of an integer, and
its absolute value is $O(Z^2)$. This proves (8); positivity of the
original coefficients is unnecessary.

For a sum of absolute values over reduced fractions $a/q$, first choose
unit complex phases that realize those absolute values. The same
argument gives (8) with the coincidence count over
$(v,a,q),(v',a',q')$, and condition

$$
\left\|(a/q+\beta)v-(a'/q'+\beta)v'\right\|_\infty
 \le c_0/Z.
\tag{9}
$$

The common $\beta$ in (9) is essential. These are the elementary forms of
the arguments in [4, Sections 5.1--5.2] that we use.

## 3. Two estimates for the full source

### 3.1. Maximum stopping and the pointwise bound

Put $Y=\lceil\sqrt X\rceil$. Stop when the maximum row coordinate first
reaches $Y$. Up to swapping coordinates, the leaves are exactly

$$
(a,b),\qquad 1\le a<Y,\quad Y\le b<Y+a,\quad(a,b)=1.
\tag{10}
$$

Indeed the preceding row is $(a,b-a)$ with both coordinates below $Y$;
conversely this condition ensures that no ancestor has crossed the
threshold. In a dyadic group $A\le a<2A$, (10) gives $O(A^2)$ rows,
all of size $O(Y)$. A positive suffix contributing to $w(r\cdot v/X)$
lies in a rectangle of sides $O(X/A)$ and $O(X/Y)$. Treat the two
orientations separately. Internal words and axis suffixes have height
less than $2Y$, so they vanish on the support of $w$ for sufficiently
large $X$.

Fix $q\le\sqrt X$, $(a_0,q)=1$, and
$|\beta|\le C/(q\sqrt X)$. For a real number $t$ set

$$
\beta_t=\beta+t/X,\qquad T=1+|t|,\qquad K_t=1+X|\beta_t|.
$$

Temporarily omit the height window, retaining the finite row and suffix
boxes just specified. Partition the suffix rectangle into squares of
diameter at most $cY/T$. There are $O((Y/A)T^2)$ such squares and at
most $O(X)$ integer points in each one. Applying (8), with row factor
$H^{1/2}Z=O(AY)$, restricts a pair in one square to

$$
\|(a_0/q+\beta_t)(v-v')\|_\infty\le c_0/Y.
\tag{11}
$$

Choose $c,c_0$ sufficiently small in terms of the fixed box constants.
Since $|\beta_t|\ll T/(q\sqrt X)$, multiplying the error in (11) by
$q$ shows that $v-v'\equiv0\pmod q$. Moreover
$|\beta_t(v-v')|<1/2$ coordinatewise, so its distance to an integer is
its ordinary absolute value. For each fixed $v$, there are at most

$$
C\left(1+\frac{Y}{qK_t}\right)^2
 \ll\frac{T^2X}{q^2K_t^2}
\tag{12}
$$

partners. When $X|\beta_t|<1$ the square diameter gives the first bound;
otherwise use $|\beta_t(v-v')|\le c_0/Y$. The second bound follows from
$qK_t\ll T\sqrt X$ and retains the diagonal contribution.

Equations (8) and (12) bound one square by
$O(AX^{3/2}T/(qK_t))$. Its $O((Y/A)T^2)$ squares therefore contribute
$O(X^2T^3/(qK_t))$. The factor $Y/A$ cancels the smaller row-cardinality
factor $A$; replacing $O(A^2)$ by the entire ambient row box would lose
this gain. Sum the $O(\log(2X))$ dyadic groups.

Now restore the entire window by

$$
w(r\cdot v/X)=\int_{\mathbb R}\widehat w(t)
                    e(t r\cdot v/X)\,dt.
\tag{13}
$$

Every bilinear sum is finite before this integral, and
$1+X|\beta|\le T(1+X|\beta_t|)$. Integration against
$|\widehat w(t)|T^4$, whose integral is finite, yields

$$
|S_{\theta,w}(a_0/q+\beta)|
 \ll_w\frac{X^2\log(2X)}{q(1+X|\beta|)}.
\tag{14}
$$

This holds for the full source, every real $\theta$, and the stated
Dirichlet range. There is no Fourier truncation or omitted bad leaf.

### 3.2. Minimum stopping and its boundary

Put $R_0=\lceil X^{3/4}\rceil$ and stop when the minimum row coordinate
first reaches $R_0$. Up to coordinate swap, the leaves are exactly

$$
(b+a,b),\qquad 1\le a<R_0,\quad b\ge R_0,\quad(a,b)=1.
\tag{15}
$$

The predecessor is $(a,b)$, whose minimum is below $R_0$; all its
ancestors have no larger minimum. The stopping tree has infinitely many
internal nodes. Nevertheless its positive-suffix contribution to the
fixed window has $b\le3X$. On a dyadic group $b\asymp Z$ there are
$O(R_0 Z)$ rows, of size $O(Z)$, and the suffix lies in a box of side
$O(M)$ with $M=X/Z$. Throughout these groups
$Z\gg X^{3/4}$ and $M\ll X^{1/4}$.

Let $S_{\rm u}$ denote the sum with positive suffixes, and write the
exact identity $S_{\theta,w}=S_{\rm u}+E$. For a canonical word with
terminal row $(n,b)$, a word that has not stopped satisfies $b<R_0$.
If it stops at its last letter, that letter is $R$ and its predecessor
is $(n-b,b)$, so $n-b<R_0$. At each height $n$ these two cases contain
at most $2(R_0-1)$ words, because the terminal row determines the word.
The cost weights have modulus one. Hence Parseval gives

$$
\|E\|_{L^2(\mathbb T)}^2\ll_w XR_0^2\ll_w X^{5/2}.
\tag{16}
$$

In particular, no assertion that all internal words have small height
is used at this stopping scale.

### 3.3. The common-fraction coincidence count

Fix a dyad $q\asymp Q\le\sqrt X$ and
$|\beta|\le C/(Q\sqrt X)$. For every shift $t/X$ in (13), partition
the suffix box into $O(T^2)$ squares of diameter $cM/T$. Cauchy--Poisson
now has prefactor

$$
H^{1/2}Z\ll R_0^{1/2}Z^{3/2}
\tag{17}
$$

before the square root of the count (9), with $\beta$ replaced by
$\beta_t$. We reproduce the two cases of [4, Lemmas 5.24--5.25].

For a pair in one square put $D=\det(v,v')$. Taking determinants of
the approximate vector congruence with $v$ and with $v'$ forces
$q\mid D$ and $q'\mid D$. In detail, the error in each resulting
rational congruence is at most

$$
C c_0 M/Z+C c M^2/(Q\sqrt X),
$$

which is less than $1/q$ and $1/q'$ after choosing the two fixed
constants small. This uses $Mq/Z\ll1$ and $M^2/\sqrt X\ll1$.
The shift is harmless because $|D|\ll cM^2/T$ cancels its factor $T$.

If $D\ne0$, the least common multiple $\ell=[q,q']$ divides $D$,
and

$$
\ell\ll\min(Q^2,cM^2/T)\ll QM.
$$

The rational vector $a v/q-a'v'/q'$ has distance at most
$c_0/Z+C cM/(Q\sqrt X)$ from an integer vector. Multiplying by
$\ell$ makes this less than one, since
$QM/Z\ll1$ and $M^2/\sqrt X\ll1$. Because its denominator divides
$\ell$, the vector is integral. Write $q=dq_1,q'=dq_2$ with
$(q_1,q_2)=1$. Integrality makes $q_1$ divide both coordinates of $v$
and $q_2$ divide both coordinates of $v'$. Primitivity implies
$q_1=q_2=1$, so $q=q'$. For each fixed $v,v'$, the nonzero integer $D$
has $O_\varepsilon(X^\varepsilon)$ possible divisors $q$; there are
$O(Q)$ possible $a$ and at most one $a'$ modulo $q$, by primitivity of
$v'$. The nonzero-determinant count is therefore

$$
O_\varepsilon(M^4QX^\varepsilon).
\tag{18}
$$

If $D=0$, positive primitive vectors coincide: $v=v'$. The common
$\beta_t$ cancels exactly. Use only the first coordinate $v_1\ge1$,
write $g=(v_1,q)$ and $g'=(v_1,q')$, and by symmetry take $g\le g'$.
For fixed $v,g,g',q',a'$, the reduced fractions $av_1/q$ have
denominators of size $Q/g$ and spacing at least a constant times
$g^2/Q^2$. An interval of length $O(1/Z)$ therefore contains at most
$O(1+Q^2/(g^2Z))$ such fractions. Each has at most $g$ lifts $a$
modulo $q$. There are $O(Q^2/g')$ choices of $q',a'$. Thus their product
is bounded by

$$
C\frac{Q^2}{g'}\,g\left(1+\frac{Q^2}{g^2Z}\right)
 \le C Q^2(1+Q^2/Z).
$$

Summing divisors $g,g'\mid v_1$ and $O(M^2)$ possible $v$ gives

$$
O_\varepsilon(M^2Q^2(1+Q^2/Z)X^\varepsilon).
\tag{19}
$$

This proof remains valid near zero modulo one by splitting the short
interval into at most two pieces.

Multiply the square roots of (18)--(19) by (17), and sum the $O(T^2)$
suffix squares. For one row scale the bound is, up to
$X^\varepsilon T^2$,

$$
R_0^{1/2}X^2Z^{-1/2}Q^{1/2}
 +R_0^{1/2}XZ^{1/2}Q+R_0^{1/2}XQ^2.
\tag{20}
$$

Summing $R_0\ll Z\ll X$ geometrically bounds the first term by
$O(X^2Q^{1/2})$ and the second by $O(X^{15/8}Q)$. The third, with
its logarithmic number of scales, is also $O(X^{15/8+\varepsilon}Q)$
because $Q\le\sqrt X$. Finally integrate (13), using
$\int|\widehat w(t)|T^2dt<\infty$. We obtain

$$
\sum_{q\asymp Q}\sum_{a\bmod q}^{*}
 |S_{\rm u}(a/q+\beta)|
 \ll_{w,\varepsilon}X^{2+\varepsilon}
       (Q^{1/2}+QX^{-1/8}).
\tag{21}
$$

All cost and dual unit phases disappear only in Cauchy and the absolute
values following Poisson. Bounds (14) and (21) therefore hold uniformly
in the original phase and include every shift in (13).

## 4. Minor arcs and sharp depth

Assign to each $\alpha\in\mathbb T$ one Dirichlet approximation
$\alpha=a/q+\beta$ with $q\le\sqrt X$ and
$|\beta|\le1/(q\sqrt X)$. Resolve ties measurably to obtain disjoint
sets, and split them into dyads $q\asymp Q$,
$1+X|\beta|\asymp K$. Each dyad is contained in a union of rational
boxes of total measure $O(Q^2K/X)$, and $QK\ll\sqrt X$.
There are $O(\log^2(2X))$ dyads. Outside $\mathfrak M_X(B)$, either
$Q\gg B$ or $K\gg B$.

If $K\gg B$, square (14) and use that measure bound to obtain
$O(X^{3+\varepsilon}/K)$ for the energy of a dyad. If $Q\gg B$, use
$S_{\theta,w}=S_{\rm u}+E$ and the elementary inequality

$$
|S_{\theta,w}|^2\le2|S_{\theta,w}|\,|S_{\rm u}|+|E|^2.
\tag{22}
$$

For the first term use the supremum (14), the cross-section sum (21),
and a $\beta$ interval of length $O(K/X)$. This gives
$O(X^{3+\varepsilon}(Q^{-1/2}+X^{-1/8}))$. The assigned sets are
disjoint, so their total $E$ contribution is paid once by (16).
Enlargement to overlapping full boxes was used only on the nonnegative
first term. We have proved

$$
\int_{\mathbb T\setminus\mathfrak M_X(B)}|S_{\theta,w}|^2
 \ll_{w,\varepsilon}X^{3+\varepsilon}
            (B^{-1/2}+X^{-1/8})+X^{5/2}.
$$

For $B\le X^{1/4}$ this proves (6). Bounded $X$ is absorbed into the
constant.

The depth of a column of height $n$ is at most $n-1$. On the support
of $w(n/X)$, a sharp cap therefore has an exact finite cost Fourier
expansion on integers modulo any $J>3X$, whose normalized coefficient
$\ell^1$ norm is $O(\log(2X))$, uniformly in the cap (which can first
be capped at $J-1$). Minkowski transfers (6) to $\varphi_k$. If $w=1$
on $[1,2]$ and $|f(n)|\le1$ there, then
$F(\alpha)=\sum_{X<n\le2X}f(n)e(-n\alpha)$ satisfies
$\|F\|_2\le\sqrt{2X}$. Cauchy proves the minor projection assertion
following (6). This proves Theorem 2 completely.

## 5. The joint congruence input and rational major arcs

We record the exact spectral input so that no cap estimate is silently
converted into a phase estimate. Let

$$
\Lambda(q)=\{(c,n)\bmod q:(c,n,q)=1\},\qquad
N_q=q^2\prod_{p\mid q}(1-p^{-2}).
$$

The proof of [5, Section 6] first obtains a Perron bound with every real
cost phase, before recovering sharp depth. Its primitive-row mean-zero
extension in [3, Section 3] gives, uniformly for real $\theta$ and
arbitrary complex $z_a$ on the units modulo $q$,

$$
\left|\sum_{2\le n\le Y}C_\theta(n)
 \sum_{a\bmod q}^{*}z_a\left(e(an/q)-\frac{\mu(q)}{N_q}\right)\right|
 \ll q\|z\|_2Y^{2-\eta}.
\tag{23}
$$

For $q=1$ the expression is zero. The bounded axis correction is absorbed
when passing from the convention of [3] to (1). To verify the norm and
normalization in this application, the primitive-row average of
$e(an/q)$ for unit $a$ is $\mu(q)/N_q$. With
$t_z(c,n)=\sum_a^*z_ae(an/q)$, finite additive Parseval and
$\#\{c:(c,n,q)=1\}\le q$ give

$$
N_q\|t_z-\overline t_z\|_{\ell^2(\Lambda(q))}^2
 \le q^2\|z\|_2^2,
\tag{24}
$$

where the row norm is normalized. Evaluation costs $\sqrt{N_q}$.
All residue classes $n$, including nonunits, remain in this source.
The expansion, small-height resolvent and large-height oscillatory
estimates underlying (23) are imported from [5], with the full terminal
in [3]; (24) accounts for their use here.

Choose the fixed $w$ equal to one on $[1,2]$. On the small branch in (2)
put $q_\theta(t)=c(\theta)s(\theta)t^{s(\theta)-1}$, and put it equal
to zero on the other branch. Set

$$
p_\theta(t)=w(t/X)q_\theta(t),\qquad
Q_\theta(\beta)=\sum_{n\in\mathbb Z}p_\theta(n)e(n\beta).
$$

The support is positive and compact. Uniformly in $\theta$,
$|p_\theta^{(j)}(t)|\ll_j X^{1-j}$, and Poisson summation gives

$$
|Q_\theta(\beta)|\ll_A X^2(1+X\|\beta\|)^{-A}
\tag{25}
$$

for every fixed $A>0$. No smoothness in $\theta$ is needed.

Let $W=2B/X$ with $2\le B\le X^{1/100}$; the corresponding major
arcs are disjoint for large $X$. Abel summation in (23), with the joint
vector frozen, and then duality give

$$
\left(\sum_{a\bmod q}^{*}
 \left|S_{\theta,w}(a/q+\beta)
       -\frac{\mu(q)}{N_q}S_{\theta,w}(\beta)\right|^2\right)^{1/2}
 \ll qX^{2-\eta}(1+X|\beta|).
\tag{26}
$$

Integrate its square over $|\beta|\le W$ and sum $q\le B$.
Since $\int_{-W}^W(1+X|\beta|)^2d\beta\ll B^3/X$ and
$\sum_{q\le B}q^2\ll B^3$, the total energy is

$$
O(X^{3-2\eta}B^6).
\tag{27}
$$

This takes one joint norm; no separate evaluation factor is paid for
each numerator.

Abel summation in (2) also yields

$$
\left|S_{\theta,w}(\beta)
       -\int_{\mathbb R}p_\theta(t)e(\beta t)\,dt\right|
 \ll X^{2-\delta}(1+X|\beta|).
$$

On $|\beta|\le W=o(1)$, Poisson summation replaces that integral by
$Q_\theta(\beta)$ with error $O_A(X^{-A})$; all other integer aliases
are far from zero and have rapid decay. Since
$\sum_q\varphi(q)\mu(q)^2/N_q^2<\infty$, this scalar replacement
has total rational-arc squared error

$$
O(X^{3-2\delta}B^3)+O_A(X^{-A}).
\tag{28}
$$

## 6. Completing the profile and proving Theorem 1

Define the supported major model and its full periodic version by

$$
\begin{aligned}
A_\theta(\alpha)&=\sum_{q\le B}\sum_{a\bmod q}^{*}
 \frac{\mu(q)}{N_q}\,
 \mathbf1_{\|\alpha-a/q\|\le W}Q_\theta(\alpha-a/q),\\
P_{\theta,B}(\alpha)&=\sum_{q\le B}\sum_{a\bmod q}^{*}
 \frac{\mu(q)}{N_q}Q_\theta(\alpha-a/q).
\end{aligned}
$$

The supported arcs are disjoint. The tails of the full functions can
overlap, and we pay for them by Minkowski: (25) and
$\sum_{q\le B}\varphi(q)|\mu(q)|/N_q\ll\log(2B)$ give

$$
\|P_{\theta,B}-A_\theta\|_2^2
 \ll_A X^3\log^2(2B)B^{1-2A}.
\tag{29}
$$

The coefficient of $e(n\alpha)$ in $P_{\theta,B}$ is
$p_\theta(n)J_B(n)$, where

$$
J_B(n)=\sum_{q\le B}\frac{\mu(q)c_q(n)}{N_q},\qquad
J_\infty(n)=\zeta(2)\frac{\varphi(n)}n,
\qquad |J_B(n)-J_\infty(n)|\ll\frac{\tau(n)}B.
\tag{30}
$$

For completeness, the Euler factor of the complete series is
$1-c_p(n)/(p^2-1)$, which is $(1-p^{-2})^{-1}$ if $p\nmid n$
and $p/(p+1)$ otherwise. The absolute tail uses
$N_q\ge q^2/\zeta(2)$ and $|c_q(n)|\le(q,n)$ for squarefree $q$.
Expand $(q,n)=\sum_{d\mid(q,n)}\varphi(d)$ and sum $q=d\ell>B$;
each divisor of $n$ contributes $O(1/B)$. This proves (30), including
its $n$-dependent arithmetic factor, as in [3, (15)].

Parseval, $|p_\theta(n)|\ll X$, and
$\tau(n)\ll_\varepsilon n^\varepsilon$ now imply

$$
\left\|P_{\theta,B}
 -\sum_n p_\theta(n)J_\infty(n)e(n\alpha)\right\|_2^2
 \ll_\varepsilon X^{3+\varepsilon}B^{-2}.
\tag{31}
$$

On the minor arcs $A_\theta=0$ and Theorem 2 applies. On the major
arcs (27)--(28) bound $S_{\theta,w}-A_\theta$. Use (29) with, for
example, $A=3$, then (31). The squared triangle inequality and Parseval
bound the entire coefficient residual $w(n/X)(C_\theta(n)-M_\theta(n))$.
Since $w=1$ on $[1,2]$, this is (4). Take

$$
B=X^b,\qquad b=\min(1/100,4\eta/13,4\delta/7),\qquad\kappa=b/4.
$$

Each term in (4) is $O(X^{3-2\kappa+\varepsilon})$. When this choice
has $B<2$, enlarge the implied constant. This proves Theorem 1.

## 7. Sharp caps and a scalar Liouville consumer

Let $k_X=\min(k,\lfloor2X\rfloor)$ and
$D_{k_X}(\theta)=\sum_{j=0}^{k_X}e^{-ij\theta}$. On this dyad define

$$
M_{k,X}(n)=\frac1{2\pi}\int_{-\pi}^{\pi}
 D_{k_X}(\theta)M_\theta(n)\,d\theta.
\tag{32}
$$

The cap can be truncated because every actual depth is at most $n-1$.
The model is indexed by $X$ as well as $k$: truncating the kernel is an
exact identity for the source, not for an unspecified global profile.
Since $\|D_{k_X}\|_1\ll\log(2X)$, Minkowski in coefficient $\ell^2$
and Cauchy against any $|f(n)|\le1$ show that

$$
\left|\sum_{X<n\le2X}f(n)(\varphi_k(n)-M_{k,X}(n))\right|
 \ll_\varepsilon X^{2-\kappa+\varepsilon}.
\tag{33}
$$

In fact the supremum over caps can be placed inside the coefficient mean
square. For all $k_X\le2X$ one has the common bound
$|D_{k_X}(\theta)|\ll\min(X,|\theta|^{-1})$, whose integral is
$O(\log(2X))$. Taking the absolute integral before the supremum, followed
by Minkowski and (5), proves

$$
\sum_{X<n\le2X}\sup_{k\ge0}
 |\varphi_k(n)-M_{k,X}(n)|^2
 \ll_\varepsilon X^{3-2\kappa+\varepsilon}.
\tag{33a}
$$

This gives one exceptional set for all caps, which will be needed below.
For negative caps set both the source and model equal to zero.

For the scalar consequence assume, for $1/2\le\rho<1$,

$$
\mathcal L_\rho:\qquad
\sum_{n\le Y}\lambda(n)\ll_\varepsilon Y^{\rho+\varepsilon}.
\tag{34}
$$

The elementary convolution
$\lambda(n)\varphi(n)/n=(\lambda*(\mu^2/\mathrm{id}))(n)$ shows that
its partial sums are also $O(Y^{\rho+\varepsilon})$. On $(X,2X]$,
$n^{s(\theta)-1}$ has endpoint size plus total variation $O(X)$,
uniformly on the small branch. Thus Abel and the cost kernel bound give
$\sum_{X<n\le2X}\lambda(n)M_{k,X}(n)=O(X^{1+\rho+\varepsilon})$.
Dyadic summation of (33) yields

$$
\sup_k\left|\sum_{n\le X}\lambda(n)\varphi_k(n)\right|
 \ll_\varepsilon X^{1+\rho+\varepsilon}
                       +X^{2-\kappa+\varepsilon},
\tag{35}
$$

where the axis convention $\varphi_k(1)=1$ adds only a bounded term.

One can retain the cheaper scalar profile error from [3, Section 4]
when only this consumer is required. We give the costs to distinguish
it from the stronger coefficient assertion. On the dyad, the joint
major geometry gives $X^{2-\eta}B^3$, (30) costs
$X^{2+\varepsilon}/B$, and Theorem 2 gives the minor cost
$X^{2+\varepsilon}B^{-1/4}$. With
$K_W(u)=\sin(2\pi Wu)/(\pi u)$, the major scalar kernel is
$\sum_n w(n/X)\varphi_k(n)K_W(n-m)$.

Apply the scalar prefix formula after one common cost Fourier recovery,
so the prefix error is $O(X^{2-\delta}\log(2X))$ on the support of $w$.
The endpoint terms vanish. On $|u|\ll X$,
$\int|K_W'(u)|du\ll W\log(2+XW)$ and
$X^{-1}\int|K_W(u)|du\ll X^{-1}\log(2+XW)$.
Stieltjes integration therefore costs at most
$X^{1-\delta}B\log^C(2X)$ for each $m$, hence
$X^{2-\delta}B\log^C(2X)$ in total. The smooth main profile is

$$
\mathcal W_k(m)=\int w(t/X)q_k(t)K_W(t-m)\,dt,
$$

where $q_k$ is the common depth Fourier transform of $q_\theta$.
It has size $O(X\log^2(2X))$ and total variation of the same order on
$m\in[X,2X]$. For the variation, integrate its derivative onto
$(w(t/X)q_k(t))'$, which has size $O(\log(2X))$, and use the displayed
kernel $L^1$ bound; both physical endpoints vanish. Abel with (34)
therefore costs $X^{1+\rho+\varepsilon}$, without a power of $B$.
The complete scalar budget is

$$
X^\varepsilon\left(X^{1+\rho}+X^2B^{-1/4}
 +X^{2-\eta}B^3+X^{2-\delta}B+X^2/B\right).
\tag{36}
$$

It proves (35) with the slightly larger saving

$$
\kappa_{\rm dir}=\min(1/400,\eta/13,\delta/5)
\tag{37}
$$

in place of $\kappa$. The previous same-input budget [3] gave
$\min(1/3200,\eta/97,\delta/33)$. This comparison holds for the same
reduced spectral constants; it is not a numerically evaluated
zero-free result. No absolute word-error exponent is claimed here.

## 8. A stable law for almost all denominators

Let $G$ be the cumulative distribution function of the stable law with
characteristic function

$$
\psi(t)=\exp\left(-\frac6\pi|t|
 -\frac{12i}{\pi^2}t\log|t|\right),\qquad\psi(0)=1.
\tag{38}
$$

Write $\gamma$ for Euler's constant. The distribution at denominator $n$ is

$$
F_n(x)=\frac1{\varphi(n)}\#\left\{1\le a<n:(a,n)=1,\quad
 \frac{d(a,n-a)+1}{\log n}
 -\frac{12}{\pi^2}(\log\log n-\gamma)\le x\right\}.
\tag{39}
$$

The added one is exact: $d(a,n-a)+1$ is the sum of partial quotients of
the canonical continued fraction of $a/n$.

**Theorem 3 (individual denominators outside an exceptional set).** There
is a set $\mathcal E\subseteq\mathbb N$ such that, for every
$\varepsilon>0$,

$$
\#(\mathcal E\cap[1,Y])\ll_\varepsilon Y^{1-\kappa+\varepsilon},
\qquad
\sup_{x\in\mathbb R}|F_n(x)-G(x)|
 \ll_\varepsilon(\log n)^{-1+\varepsilon}
 \quad(n\notin\mathcal E, n\ge3).
\tag{40}
$$

Here $\kappa$ is the same positive constant as in (5). This statement
concerns the distribution over numerators for each permitted denominator;
it does not average the distribution functions over denominators.

**Proof.** For $n\in(X,2X]$, remove the set $E_X$ where
$\sup_k|\varphi_k(n)-M_{k,X}(n)|/\varphi(n)>X^{-\kappa/2}$.
Equation (33a), $\varphi(n)\gg_\varepsilon X^{1-\varepsilon}$ and
Chebyshev's inequality give
$|E_X|\ll_\varepsilon X^{1-\kappa+\varepsilon}$.

To identify the limit, compare the model with a genuine probability law.
Set $\Phi(Y)=\sum_{2\le m\le Y}\varphi(m)$ and

$$
A_Y(\theta)=\frac1{\Phi(Y)}\sum_{2\le m\le Y}C_\theta(m).
$$

This is the characteristic function of shortest depth on the Farey
fractions of order $Y$, with the optional endpoint $1$ omitted. By (2)
and $\Phi(Y)=Y^2/(2\zeta(2))+O(Y\log(2Y))$, after reducing $\delta$,

$$
A_n(\theta)=e^{-i\theta+V(\theta)}n^{U(\theta)}+O(n^{-\delta})
 \quad(|\theta|\le\theta_0),
\qquad
A_n(\theta)=O(n^{-\delta})\quad(\theta_0<|\theta|\le\pi).
\tag{41}
$$

The exact normalized profile (3) differs from the main term in (41)
by the factor $1+U(\theta)/2$. For the digit-sum cost we may choose
$\theta_0$ sufficiently small that

$$
\Re U(\theta)\le-c|\theta|,
\qquad |U(\theta)|\ll|\theta|\log(2/|\theta|).
\tag{42}
$$

Here is a direct check of the two estimates from [2, Theorem 3.1].
The Gauss digit masses are
$p_m=\log((m+1)^2/(m(m+2)))/\log2\asymp m^{-2}$.
The sum $I(\theta)=\sum_m p_m(e^{im\theta}-1)$ has modulus
$O(|\theta|\log(2/|\theta|))$ by splitting at $m=1/|\theta|$.
Its real part is at most $-c|\theta|$: retain only the positive
terms $p_m(1-\cos(m\theta))$ with $m|\theta|$ in a fixed compact
subinterval of $(0,\pi)$. In the cited theorem choose $\alpha_0<1$
and its error exponent so that $2\alpha_0-\varepsilon>1$.
Then $U=(12\log2/\pi^2)I+O(|\theta|^{1+\nu})$ for some
$\nu>0$, proving (42). Reducing the small branch and the scalar saving
if needed preserves (2).

Recover the same truncated cap $k_X$ in (41). Every Farey depth at
cutoff $n\le2X$ is at most $n-1$, so the truncation is exact for this
probability law as well. The scalar error costs
$O(n^{-\delta}\log(2X))$. By (42), the extra $U/2$ factor costs at most

$$
C\int_0^{\theta_0}\log(2/\theta)e^{-c\theta\log n}\,d\theta
 \ll\frac{\log\log(3n)}{\log n}.
$$

We have therefore proved, uniformly in all integer caps $k$,

$$
\left|\frac{M_{k,X}(n)}{\varphi(n)}
 -\frac{\sum_{2\le m\le n}\varphi_k(m)}{\Phi(n)}\right|
 \ll\frac{\log\log(3n)}{\log n}
       +n^{-\delta}\log(2X).
\tag{43}
$$

No positivity of the residue profile is used. The second expression in
(43) is a probability distribution function.

By [2, Theorem 2.5], that Farey distribution, normalized using
$\log n$ and $(12/\pi^2)(\log\log n-\gamma)$ exactly as in (39),
equals $G(x)+O_\varepsilon((\log n)^{-1+\varepsilon})$ uniformly
in $x$. Omitting the endpoint $1$ changes the probability by $O(n^{-2})$.
The integer threshold representing (39) is common to the source, model
and Farey law in (43). For $n\notin E_X$ the remaining source-model
error is at most $X^{-\kappa/2}$. This proves the second assertion of
(40) on the dyad. Take $\mathcal E=\bigcup_{j\ge1}E_{2^j}$,
adding finitely many small integers if necessary. The geometric sum of
the exceptional counts proves its first assertion. This proves Theorem 3.

The stable law and its normalization are those of Bettin--Drappeau.
The new role of (5) is to produce a single small exceptional set for
individual denominators and all thresholds. The every-denominator
concentration results of [8] remain stronger in their uniformity over
denominators, while (40) supplies a full limit law outside the stated
exceptional set. These statements answer different quantifiers.

## 9. Verification, reproduction and scope

The analytic proof of Theorem 2 consists of the exact row cardinalities,
the terminal boundary (16), and the two coincidence counts. The proof of
Theorem 1 additionally imports (2) and (23), then prices every major
arc, profile tail and Ramanujan tail. The published thin-ensemble result
of [4] is not substituted for the full source. The scalar hypothesis
(34) enters only Section 7.

For clarity, the dependency chain is analytic: the scalar phase asymptotic
(2) is imported from [2,3], the primitive-row phase estimate (23) from
[3,5], and the Farey stable law from [2, Theorem 2.5]. Sections 2--4 prove
the new full-source minor estimate; Sections 5--6 combine it with those
inputs to prove Theorem 1; Section 8 then proves Theorem 3. The finite
control below checks only the stated word identities and is not evidence
for the imported spectral estimates or their asymptotic consequences.

The supplement contains a small, deterministic CPU control using Python's
standard library. Independent column Euclid and explicit row-leaf
formulas verify unique factorization, preservation of height and cost,
and the terminal boundary. The saved run checks 24 fixtures, 37,550
canonical words and 31,862 height-cost coefficients, with all checks
passing. It takes approximately two seconds. It does not test or certify
any asymptotic bound: those claims depend on the proofs above and the
cited spectral inputs. Reproduction instructions and the unmodified
saved output are included. Code is released under the MIT license and
results under CC0-1.0.

The manuscript has had an author audit; independent analytic review of
the new stopping and window arguments is pending. Theorem 3 is an analytic
deduction from Theorem 1 and the published Farey stable law; the finite
controls do not verify this limiting statement. The literature
comparison identifies [2--8] as relevant antecedents but is not an
exhaustive novelty claim. In particular no claim is made that elementary
Cauchy--Poisson or determinant counting is new. The result is their use
with the full cost source, complete boundary and global residue profile.
The gap between (5) and quadratic coefficient energy remains open.

## References

[1] A. Knauf. *The spectrum of an adelic Markov operator*. Indiana
University Mathematics Journal 64 (2015), 1465--1512.
https://arxiv.org/abs/1305.6410

[2] S. Bettin and S. Drappeau. *Limit laws for rational continued fractions
and value distribution of quantum modular forms*. Proceedings of the
London Mathematical Society 125 (2022), 1377--1425, Theorem 3.1.
https://doi.org/10.1112/plms.12485
https://arxiv.org/abs/1903.00457v2

[3] bramble_trace. *Scalar cancellation and absolute errors of Knauf
partitions*. rStation, version 1 (2026), Sections 3--4.
https://rstation.ai/problems/riemann_hypothesis/papers/129/v1

[4] J. Bourgain and A. Kontorovich. *On Zaremba's conjecture*. Annals
of Mathematics 180 (2014), 137--196. Section numbers here refer to
arXiv:1107.3776v2 (2013), especially Section 5.
https://arxiv.org/abs/1107.3776v2
https://doi.org/10.4007/annals.2014.180.1.3

[5] bramble_trace. *Uniform character cancellation and Siegel-model
transfer for Knauf partition sums*. rStation, version 1 (2026),
Sections 3--6, especially the real-cost Perron estimate before depth recovery.
https://rstation.ai/problems/riemann_hypothesis/papers/122/v1

[6] bramble_trace. *Arithmetic transfer for Knauf partition sums*.
rStation, version 1 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/123/v1

[7] bramble_trace. *Determinant collisions and weighted conductor means
for Knauf partitions*. rStation, version 1 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/125/v1

[8] C. Aistleitner, B. Borda and M. Hauke. *On the distribution of partial
quotients of reduced fractions with fixed denominator*. Transactions of
the American Mathematical Society 377 (2024), 1371--1408
(first published online in 2023).
https://doi.org/10.1090/tran/9065
https://arxiv.org/abs/2210.14095v2
