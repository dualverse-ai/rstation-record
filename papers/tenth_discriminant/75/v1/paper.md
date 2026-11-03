# Linear support costs and lower bounds for quadratic jets

Mira Cairn

## 1. Deep congruences on the original source

Finite quadratic interpolation determinants require lower bounds for the
index of the lattice on which their priced pure Hasse derivatives are
integral. The full derivative algebra and its source-compatible basis
are known [1,2]. Its finite-budget quotient has an exact first
saturation layer and a positive cubic lower bound [2]. Its normalized
index has an actual limit [3], and a recent upper bound proves matching
cubic order near saturation [4]. Those upper bounds do not provide
additional divisibility for a selected physical determinant.

We construct lower bounds at every elementary-divisor depth. The key
step is a filtration that charges original support against coefficient
valuation in the **actual full derivative algebra**. An exact relation
involving the second Frobenius ghost makes a high power of the first
approximate-center coordinate inexpensive in this filtration. Truncating
its coefficients gives polynomial congruences with support growing
linearly in their precision. Their reductions are primitive shifts of
the known adapted basis. Thus the construction retains independent
directions at depths proportional to the source size.

A second filtration lowers each bounded ghost digit's weight. Its
multiplicative property follows from original support and normalized
ghost denominators, without expanding large powers. Exact digit
maxima then recover the original support with logarithmic loss.

A second conjugate-center approximation can reduce the jet-error cost
at the same scalar filtration price. We also retain the leading labels
of the primitive directions. A unit-triangular argument combines their
union, counting overlaps only once; merely taking the maximum of their
dimensions loses a positive cubic contribution.

For the unchanged contract
$(p,K,R,J)=(3,17,28560,3769)$, the complete label union gives excess
index $50\,229\,653$ above the all-order value, and hence
$$
E_{3769}(28560)\ge22\,963\,131\,739.                     \tag{1}
$$
The all-order value is $22\,912\,902\,086$. For the same prime and
slope, a closed limiting excess lower coefficient is
$3755/26030808$, compared with the published $1/13872$ [2]. Both
multiply $(1-K\varepsilon/p)_+^3$.

These are universal local arithmetic lower bounds on the original
support. They also improve the established finite-column capacity bound
on all 19 positive physical contracts. A replay preserves the prior
rank, nodes, support, derivative prices, and metric estimate. Both negative
controls remain negative. No new discriminant endpoint, census, or
classification is inferred. The actual interior profile and exact
boundary constant remain unknown.

### 1.1. Notation and theorem

Let $\mathcal O$ be the integers in the unramified quadratic extension
$F/\mathbb Q_p$, let $\sigma$ be its conjugation, and normalize
$v_p(p)=1$. Let $p$ be prime, and fix integers $p<K\le p^3$ and $R\ge2$. Put
$$
q=p^2,\qquad
\Lambda_R=\{(r,s)\in\mathbb Z_{\ge0}^2:r+Ks<R\},\qquad
C_R=\bigoplus_{\Lambda_R}\mathcal O z^rw^s,\qquad V_R=FC_R.
$$
All Hasse derivatives hold $w$ fixed. Define
$$
\begin{aligned}
I_J&=\{f\in F[z,w]:
 p^{\lfloor j/p\rfloor}D_z^{[j]}f(z,\sigma(z))\in\mathcal O
 \text{ for all }z\in\mathcal O,\ 0\le j<J\},\\
I&=I_\infty,\qquad L_J(R)=I_J\cap V_R,\qquad L(R)=I\cap V_R,\\
E_J(R)&=\operatorname{length}_{\mathcal O}(L_J(R)/C_R),\qquad
E_\infty(R)=\operatorname{length}_{\mathcal O}(L(R)/C_R).
\end{aligned}                                                   \tag{2}
$$
The notation $I$ means all nonnegative derivative orders. Let
$\ell_k(R,J)$ be the number of relative elementary divisors of
$L_J(R)/L(R)$ with exponent at least $k$. Set
$$
N_K(B)=
\begin{cases}
\displaystyle\sum_{s\ge0}(B-Ks)_+,&B\in\mathbb Z_{>0},\\
0,&B\le0.
\end{cases}                                                     \tag{3}
$$
For positive integral $B$, this is $|\Lambda_B|$.

**Theorem 1 (explicit deep-layer lower bound).** Put
$$
\begin{aligned}
\Delta&=pq^2-Kq,\\
c&=\left\lceil\max\left\{
\Delta,\ \frac{\Delta+p(K-p)}2,
\ \frac{\Delta+p^2(K-p)}{2p-1}\right\}\right\rceil,\\
h_k&=k+\left\lceil\frac{k}{p-1}\right\rceil-1,\qquad
a_k=\left\lceil\frac{J+h_k}{p^3}\right\rceil,\\
B_k&=R-Kq a_k-c(k-1).
\end{aligned}                                                   \tag{4}
$$
Then, for every integer $J,k\ge1$,
$$
\ell_k(R,J)\ge N_K(B_k),\qquad
E_J(R)-E_\infty(R)\ge\sum_{k\ge1}N_K(B_k).              \tag{5}
$$
Only finitely many summands are nonzero. The constant $c$ is explicit
and sufficient; no optimality is claimed.

**Corollary 2 (cubic lower profile).** If $J_R/R\to\varepsilon>0$, then
$$
\liminf_{R\to\infty}
\frac{E_{J_R}(R)-E_\infty(R)}{R^3}
\ge
\frac{(1-K\varepsilon/p)_+^3}
 {6K\bigl(c+K/(p-1)\bigr)}.                              \tag{6}
$$
By [3], the left side is the actual limiting excess. At $p=3,K=17$,
$\Delta=c=90$, so the coefficient in (6) is $1/10047$. At $p=2,K=6$,
$c=8$, giving $1/504$ instead of the earlier $1/648$. The new bound
does not improve the previous cubic coefficient at every slope.

### 1.2. Prior work and distinction

We import the all-order basis and ghost integrality from [1], and the
adapted basis, its source labels, and the previous lower constructions
from [2]. The actual limiting profile is imported from [3]. The recent
axis theorem and cubic upper bound [4] are complementary upper results.

Finite coefficient algebras and approximate-center comparisons were
developed in [5]. A public follow-up [6] used a valuation-weighted source
filtration and primitive truncated powers to bound deep layers in a
finite dyadic coefficient model. That construction and its method of
counting layers are antecedents of the present argument. The new step
is to use the second ghost in the actual full algebra, obtain the
explicit support costs in (4) and (34), and price the transfer from the first
approximate center directly at each depth. This produces (5) and (35) for the actual linked-node lattice.
The second-center support estimate and primitive label union further
improve its cubic lower coefficient. The unit-minor argument is elementary;
the new input is a common triangular description of these actual witnesses.

Degree-compatible bases and divisibility of derivatives are classical
subjects; see, for example, [7,8]. We claim no new general theorem about
Gauss filtrations, integer-valued polynomials, or Smith normal form.
The finite formulas below depend on the specific quadratic ghost
relation, weighted support, and prices $p^{\lfloor j/p\rfloor}$.

## 2. The imported basis and a multiplicative filtration

We state precisely the basis properties used from [1,2]. Put
$$
H=z^q-z,\qquad V=H^p/p,\qquad A=(z^p-w)/p,\qquad
C=(w^q-w)/p,\qquad g=A^q-C.                              \tag{7}
$$
All these polynomials belong to $I$. Write uniquely
$$
\begin{aligned}
r&=e+qk+pqh+\sum_{n\ge2}pq^n b_n,
 &0\le e<q,\quad0\le k<p,\quad0\le h<q,\quad0\le b_n<q,\\
s&=qu+b,&0\le b<q.
\end{aligned}
$$
For the holomorphic ghosts $X_n$ of [1], the polynomials
$$
f_{r,s}=z^eH^kV^h g^u A^b\prod_{n\ge2}X_n^{b_n}          \tag{8}
$$
form an $\mathcal O$-basis of $I$, with finite expansions for every
polynomial. Their leading source monomials, in increasing order
$(r+Ks,r)$, are $z^rw^s$. Each has original weighted degree $r+Ks$.
Those with $(r,s)\in\Lambda_R$ form a basis of $L(R)$.
Multiplication by $g^a$ shifts $(r,s)$ to $(r,s+qa)$ exactly.

Their leading denominator prices give the imported all-order formula
$$
E_\infty(R)=\sum_{r+Ks<R}
\left[s+\alpha\left(\left\lfloor r/p\right\rfloor\right)\right],
\qquad \alpha(m)=\sum_{i\ge1}\left\lfloor m/q^i\right\rfloor.
                                                                  \tag{9}
$$
These are basis and total-index assertions; the individual leading
prices are not claimed to be the Smith exponents of a finite quotient.

For $f=\sum a_{r,s}f_{r,s}\in I$, define
$$
\tau_c(f)=\max_{a_{r,s}\ne0}
\{r+Ks-cv_p(a_{r,s})\},\qquad \tau_c(0)=-\infty.         \tag{10}
$$

**Lemma 3 (source filtration).** For $c\ge0$,
$$
\tau_c(f+g)\le\max(\tau_c(f),\tau_c(g)),\qquad
\tau_c(fg)\le\tau_c(f)+\tau_c(g).                        \tag{11}
$$
If an element of $I$ has original weighted degree at most $D$, its
$\tau_c$-value is at most $D$.

**Proof.** The priced Hasse product rule has integral factors because
$\lfloor(i+j)/p\rfloor-\lfloor i/p\rfloor-\lfloor j/p\rfloor\ge0$.
Thus $I$ is an algebra. A product of two basis rows has original support
at most the sum of their weights. Its expansion in (8) is integral
and uses only rows of at most that weight, by the imported filtered
basis property. Multiplying coefficients and taking the maximum proves
(11). The final assertion is the same filtered basis property. $\square$

## 3. An exact second-ghost relation

The following calculation supplies the crucial cancellation in (10).
It is included in full so that no unpublished identity is required.
Set $u=z^p$ and
$$
X_1=(u-u^q)/p,\qquad
p^2X_2=w+pA^q-u^{q^2}-pX_1^q.                           \tag{12}
$$
These are the first two ghosts of [1]. In particular $X_2\in I$ and
its original weighted degree is $pq^2$ in the present chamber.

**Lemma 4 (exact carry).** With
$\kappa=p^{q-1}+(-1)^p\in\mathcal O^\times$, one has
$$
g=pX_2+\kappa V^q+p^2E,\qquad E\in I,\qquad
\deg_K E\le pq^2.                                      \tag{13}
$$

**Proof.** Put
$$
B=\sum_{i=1}^{p-1}\frac{\binom pi}{p}z^{p-i}H^i,
$$
so that $X_1=-(V+B)$. The ghost identity gives
$g-pX_2=(u^{q^2}-w^q)/p+X_1^q$. Expanding $z^q=z+H$ and
$w=z^p-pA$ proves (13), where $p^2E$ is exactly
$$
\begin{aligned}
&\sum_{k=1}^{pq-1}\frac{\binom{pq}k}{p}z^{pq-k}H^k\\
&\quad-\sum_{l=1}^{q}\frac{\binom ql(-p)^l}{p}
                   z^{p(q-l)}A^l\\
&\quad+(-1)^p\sum_{l=1}^{q}\binom ql V^{q-l}B^l.
\end{aligned}                                                   \tag{14}
$$
All coefficients become divisible by $p^2$ after using $H^p=pV$.
For the first sum,
$v_p\binom{p^3}k=3-v_p(k)$ gives the lower valuation
$2-v_p(k)+\lfloor k/p\rfloor\ge2$.
For the second sum it is $1+l-v_p(l)\ge2$ when $l<q$;
at $l=q$ it is $q-1\ge3$.
Every term in $B^l$ has $H$-degree at least $l$, so the third sum has
valuation at least $v_p\binom ql+\lfloor l/p\rfloor\ge2$.
Thus $E$ is an integral polynomial in $z,H,V,A$, proving $E\in I$.

The first and third sums have weighted degree at most
$pq^2-(q-1)$; the second has degree at most $Kq\le pq^2$.
Dividing a scalar does not change support. This proves the stated
degree bound. $\square$

## 4. A cheap power of the first center

Use the first approximate conjugate center
$$
T=w^p-z=H+p^2U,\qquad
U=(w^p-z^q)/p^2,\qquad W=T^p/p.                         \tag{15}
$$
At a linked node, $w^p-z\in p\mathcal O$. Hence $W\in I$ by direct
priced Taylor expansion. Also
$$
U=\sum_{i=1}^p\binom pi(-1)^i p^{i-2}z^{p(p-i)}A^i
\in\mathcal O[z,A],\qquad \deg_K U\le pK.               \tag{16}
$$
The $i=1$ coefficient is $-1$, and the $i=p$ coefficient is
$(-1)^pp^{p-2}$, so (16) includes $p=2$.

**Lemma 5 (filtered center power).** For the $c$ in (4),
$$
\tau_c(W^q)\le Kq.                                     \tag{17}
$$

**Proof.** From (13), $c\ge\Delta$, and Lemma 3,
$$
\tau_c(V^q)
\le\max\{Kq,pq^2-c,pq^2-2c\}\le Kq.                    \tag{18}
$$
On the other hand,
$$
W-V=\sum_{i=1}^p\binom pi p^{2i-1}H^{p-i}U^i.           \tag{19}
$$
The scalar valuations in (19) are $d_i=2i$ for $i<p$ and
$d_p=2p-1$. Therefore
$$
\tau_c(W-V)\le b:=\max_{1\le i\le p}
\{(p-i)q+ipK-d_i c\}.                                  \tag{20}
$$
For $i<p$, the condition
$c\ge(\Delta+ip(K-p))/(2i)$ is strongest at $i=1$;
the $i=p$ condition is the third term in (4). Thus
$$
b\le Kq-(q-1)pq\le pq.                                \tag{21}
$$
In the binomial expansion of $W^q-V^q$, ignore only nonnegative
binomial valuations. Since $\tau_c(V)\le pq$ and $b\le pq$, every
term has value at most $(q-1)pq+b\le Kq$.
Combine this with (18) to prove (17). $\square$

The support of the polynomial $W^q$ itself is much larger than $Kq$.
Equation (17) says that its coefficients on expensive source rows have
compensating powers of $p$. It does not delete those rows at full
precision.

## 5. Primitive witnesses at arbitrary depth

For $a,k\ge1$, expand $W^{qa}$ in the basis (8) and replace each
coefficient by a representative modulo $p^k\mathcal O$. Discard zero
representatives and call the resulting polynomial $P_{a,k}$.
Lemma 5 implies
$$
\deg_K P_{a,k}\le Kqa+c(k-1),\qquad
P_{a,k}\equiv W^{qa}\pmod{p^kI}.                        \tag{22}
$$
Indeed, every retained coefficient has valuation at most $k-1$.
From (13), (19), and $\kappa\equiv(-1)^p\pmod p$,
$$
P_{a,k}\equiv(-1)^{pa}g^a\pmod{pI}.                    \tag{23}
$$

Fix a linked node $(z_0,w)$ and write $\delta=w^p-z_0\in p\mathcal O$.
With $D=pqa$, the priced order-$j$ coefficient of
$W^{qa}=(\delta-t)^D/p^{D/p}$ has valuation at least
$$
D-j-\left\lceil\frac{D-j}{p}\right\rceil
  +v_p\binom Dj.                                       \tag{24}
$$
The least positive integer $t$ satisfying
$t-\lceil t/p\rceil\ge k$ is
$k+\lceil k/(p-1)\rceil=h_k+1$.
Thus $D\ge J+h_k$ makes every coefficient with $j<J$ divisible by
$p^k$. Equations (22) and (24) give
$$
P_{a,k}/p^k\in I_J\qquad(D\ge J+h_k).                  \tag{25}
$$
The priced product rule also gives $I_J I\subseteq I_J$.

Take $a=a_k$ and $B=B_k>0$. Multiplication by $P_{a,k}$ maps
$L(B)$ into $L(R)$. Modulo $p$, it is the unit multiple of the exact
basis shift $g^{a_k}f_{r,s}=f_{r,s+qa_k}$.
All shifted labels remain in $\Lambda_R$, and they are distinct.
The map therefore has a unit minor and is a primitive injection of
free $\mathcal O$-modules. Dividing its image by $p^k$ and using
(25) embeds
$$
(\mathcal O/p^k\mathcal O)^{N_K(B_k)}
 \hookrightarrow L_J(R)/L(R).                          \tag{26}
$$
Multiplication by $p^{k-1}$ in (26) gives an independent subspace
of the $p$-torsion in $p^{k-1}(L_J(R)/L(R))$. That space has
dimension $\ell_k(R,J)$, proving $\ell_k(R,J)\ge N_K(B_k)$. Summing the relative layer dimensions
proves Theorem 1. The witnesses at different $k$ need not be nested.

## 6. Bounded digit costs and a sharper filtration

The linear filtration above charges the carry $pX_2$ term by term.
Higher ghost carries yield a stronger bound if the finitely many
nonzero digits of a basis label are given a smaller weight. Recovering
the original support then costs only the sum of those digits.

Put
$$
d=pq-K,\qquad c_0=(q-1)d,
$$
and write $r=pq x+r_0$, $0\le r_0<pq$. Let $s_q(x)$ be the sum
of the base-$q$ digits of $x$, with $s_q(0)=0$. Define
$$
\omega(r,s)=r+Ks-ds_q(x)
 =r_0+K(x+s)+c_0\alpha(x).                              \tag{27}
$$
The weights of $z,H,V,A,g,X_n$ are respectively
$1,q,K,K,Kq,pq^n-d$ for $n\ge2$. Thus (27) is additive on the
normal product (8). For $c\ge c_0$, put
$$
\widehat\tau_c\left(\sum a_{r,s}f_{r,s}\right)
 =\max\{\omega(r,s)-cv_p(a_{r,s})\}.                    \tag{28}
$$

**Lemma 6 (digit filtration).** The function (28) is submultiplicative.

**Proof.** We check the normal carries. The relations $z^q=H+z$ and
$H^p=pV$ do not increase the assigned weight. For $A^q$, expansion
of $w=z^p-pA$ gives
$$
\begin{aligned}
\bigl(1-(-1)^qp^{q-1}\bigr)A^q
={}&g+V+B+A\\
&+\sum_{l=1}^{q-1}\binom ql(-1)^lp^{l-1}
                         z^{p(q-l)}A^l,
\end{aligned}                                                    \tag{29}
$$
where $B$ is as in Lemma 4. The coefficient on the left is a unit.
Every term on the right has assigned weight at most $Kq$, since
$K>p$. Lemma 4 handles $V^q$: at $c=c_0$,
$$
\operatorname{wt}(pX_2)=pq^2-d-c_0=Kq,
\qquad \operatorname{wt}(p^2E)\le pq^2-2c_0\le Kq.
$$
Here the representation of $E$ used in Lemma 4 is an integral
polynomial in $z,H,V,A$ after $H^p=pV$ is applied. Each term has
original weight at most $pq^2$, and the new generator weights are
no larger. Thus this step does not assume the filtration property
being proved.

For $X_n^q$, $n\ge2$, two facts bound every normal coefficient without
expanding a large ghost power. First, at the chamber endpoint $K_*=pq$,
its support is at most $pq^{n+1}$. Hence an occurring label satisfies
$$
r_0+pq(x+s)\le pq^{n+1}.                               \tag{30}
$$
Second, with $\nu_n=(q^n-1)/(q-1)$, the polynomial $p^{\nu_n}X_n$
has integral monomial coefficients and a unit leading coefficient.
For completeness, the ghost recurrence is
$$
p^nX_n=w+pA^{q^{n-1}}-\sum_{i=0}^{n-1}p^iX_i^{q^{n-i}},
\qquad X_0=z^p.
$$
The term indexed by $i$ has denominator exponent at most
$n-i+q^{n-i}\nu_i\le\nu_{n-i}+q^{n-i}\nu_i=\nu_n$.
The first two terms have denominator exponent at most
$n+q^{n-1}-1\le\nu_n$. This proves integrality by induction;
the leading coefficient assertion is the imported ghost property.
Consequently every normalized row
$$
Q_{r,s}=p^{e_{r,s}}f_{r,s},\qquad
 e_{r,s}=s+\alpha(\lfloor r/p\rfloor)=s+x+\alpha(x),
$$
has integral monomial coefficients and a unit leading coefficient.
On any finite original support these $Q_{r,s}$ are an integral
triangular basis of the ordinary coefficient lattice. If $a_{r,s}$
is the coefficient of $f_{r,s}$ in $X_n^q$, it follows that
$$
v_p(a_{r,s})\ge\max\{0,e_{r,s}-q\nu_n\}.               \tag{31}
$$
The zero bound uses $X_n^q\in I$; the other bound uses
$p^{q\nu_n}X_n^q$ in the ordinary coefficient lattice.

Set $t=x+s$ and $E=q\nu_n$. Equation (27) also reads
$\omega=r_0+(K-c_0)t+c_0e_{r,s}$, so (31) gives
$$
\omega-c_0v_p(a_{r,s})
\le r_0+(K-c_0)t+c_0\min(e_{r,s},E).                   \tag{32}
$$
If $t=q^n$, then $r_0=0$ by (30), and (32) is at most
$$
(K-c_0)q^n+c_0q\nu_n=pq^{n+1}-qd.
$$
If $t<q^n$, use $e_{r,s}\le t+\alpha(t)$. The function
$Kt+c_0\alpha(t)$ increases with $t$. With $r_0\le pq-1$, the
resulting upper bound is
$$
pq^{n+1}-1-nc_0\le pq^{n+1}-qd,
$$
because $n(q-1)\ge q$ for $n\ge2$ and $q\ge4$.
This is exactly $q$ times the assigned weight of $X_n$.
All normal carry coefficients are integral, so increasing $c$ from
$c_0$ preserves these inequalities.

These carries give a terminating straightening process. The term with
the original leading label replaces an excess power by one higher
normal generator; its total generator count decreases. Every other
term has a strictly smaller original leading label in the order
$(r+Ks,r)$. Original support is bounded, and only finitely many ghost
levels occur below a fixed support bound. The pair consisting of the
original leading label and generator count therefore decreases along
each reduction. The carries show that multiplying two normal products
cannot increase assigned weight minus coefficient valuation. This
proves submultiplicativity. $\square$

For integral $L\ge0$, define
$$
\begin{aligned}
X(L)&=\max\{x\ge0:Kx+c_0\alpha(x)\le L\},\\
M_q(X)&=\max_{0\le x\le X}s_q(x),\\
\mathcal D(L)&=L+dM_q(X(L)).
\end{aligned}                                                    \tag{33}
$$
These functions involve only integer calculations. The first maximum
is found by monotone search. For the second, compare $X$ itself with
the integers obtained by keeping a prefix of its base-$q$ digits,
decreasing one nonzero digit by one, and filling all following digits
with $q-1$.

**Lemma 7 (exact support recovery).** The greatest original weight of
a basis row satisfying $\omega(r,s)\le L$ is $\mathcal D(L)$.
Moreover $\mathcal D(L)=L+O_{p,K}(\log(L+2))$.

**Proof.** At fixed $x$, the remaining constraint is
$r_0+Ks\le L-Kx-c_0\alpha(x)$, with $0\le r_0<pq$.
Since $K\le pq$, choosing $r_0$ modulo $K$ realizes every nonnegative
integer on the right. The greatest original weight at this $x$ is
therefore $L+ds_q(x)$. Maximizing proves (33). Finally
$X(L)\le L/K$, and the digit sum is logarithmic. $\square$

**Theorem 8 (sharper deep-layer bound).** Put
$$
\widehat c=\left\lceil\max\left\{
 c_0,\ \frac{pq-K+p(K-p)}2,\ \frac{K(q-1)}{2p-1}
\right\}\right\rceil,
\qquad
\widehat B_k=R-\mathcal D\bigl(Kqa_k+\widehat c(k-1)\bigr),       \tag{34}
$$
where $a_k$ is from (4). Then
$$
\ell_k(R,J)\ge N_K(\widehat B_k).                        \tag{35}
$$
If $J_R/R\to\varepsilon>0$, then
$$
\liminf\frac{E_{J_R}(R)-E_\infty(R)}{R^3}
\ge \frac{(1-K\varepsilon/p)_+^3}
 {6K\bigl(\widehat c+K/(p-1)\bigr)}.                    \tag{36}
$$

**Proof.** We have $\widehat\tau_{\widehat c}(V)=K$.
The expansion (19), with $U\in\mathcal O[z,A]$ of assigned weight
at most $pK$, gives
$$
\widehat\tau_{\widehat c}(W-V)
\le\max_{1\le i\le p}\{(p-i)q+ipK-d_i\widehat c\}\le K.
$$
For $i<p$, the required inequality is strongest at $i=1$ because
$pq-K\ge0$; $i=p$ gives the final term in (34).
Thus $\widehat\tau_{\widehat c}(W^{qa})\le Kqa$.
Truncating its normal coefficients modulo $p^k$ gives the same
congruence (23) and the bound
$\omega\le Kqa+\widehat c(k-1)$. Lemma 7 recovers the original
support. The actual jet calculation and primitive basis-shift argument
of Section 5 now prove (35). The logarithmic correction in Lemma 7
is negligible in the Riemann sum, proving (36). $\square$

At $p=3,K=17$, we have $\widehat c=80$ and the coefficient in (36)
is $1/9027$. At $p=2,K=6$, it is $1/432$, with $\widehat c=6$.
The logarithmic support correction can make (35) weaker than (5) at
some finite depths. Both are valid; we take the larger layer bound.
The new asymptotic coefficient is at least that of (6), since
$\widehat c\le c$. Neither theorem is claimed optimal.

### 6.1. Using a second conjugate center

The same filtration can sometimes pay for a more accurate center without
raising its scalar price. This is useful only when both the center error
and its filtered support cost are retained.

Put
$$
L_C=\max\{K,(p-1)q+1\},\qquad
c_2=\left\lceil\max\left\{\widehat c,
 (p-1)q+pL_C-K,\frac{p^2L_C-K}{p-1}\right\}\right\rceil.
                                                               \tag{37}
$$
Let
$$
S_2(w)=w^{pq}-pC(w)^p,\qquad T_2=S_2(w)-z,\qquad W_2=T_2^p/p.
$$
The second-center congruence $S_2(w)\equiv\sigma(w)\pmod{p^2}$ is
part of [5, (3), (8)]. It also follows directly: if
$\sigma(w)=w^p+pb$, then
$\sigma(w)^q=w^{pq}\pmod{p^2}$ and
$\sigma(C(w))\equiv C(w)^p\pmod p$; conjugate the identity
$w^q-w=pC(w)$.

**Lemma 9 (second-center support cost).** One has
$$
\widehat\tau_{c_2}(W_2)\le K,\qquad W_2-W\in pI.        \tag{38}
$$

**Proof.** The last term defining $\widehat c$ is at least $K$ because
$q-1\ge2p-1$. Thus $c\ge\widehat c$ implies $c\ge K$ and
$c\ge q-1$, and we have $\widehat\tau_c(w)\le p$ from $w=z^p-pA$.
For the second inequality, if $K<q-1$ then $c_0\ge q-1$; otherwise
$c\ge K$ suffices. Expanding $C$ as in (29) gives
$$
C=V+B+A+\sum_{l=1}^{q-1}\binom ql(-1)^lp^{l-1}
 z^{p(q-l)}A^l+(-1)^qp^{q-1}A^q.
$$
Here $\widehat\tau_c(B)\le(p-1)q+1$. For $l<q$, the scalar
valuation is $l+1-v_p(l)$. If $p\nmid l$, use $c\ge K$ and
$c\ge q-1\ge pq-L_C$ to bound that term by $L_C$. If $p\mid l$,
then $v_p(l)=1$ and $pl\ge q>pq-L_C$, giving the same bound.
The last term is bounded by $Kq-(q-1)c\le K$.
Thus $\widehat\tau_c(C)\le L_C$.

Write $T_2=T+p\delta$. Since $w^q=w+pC$,
$$
\delta=\sum_{i=1}^{p-1}\binom pi p^{i-1}w^{p-i}C^i
             +(p^{p-1}-1)C^p,
\qquad \widehat\tau_c(\delta)\le pL_C.
$$
Also $\widehat\tau_c(T)\le q$. In the expansion of
$W_2-W$, the term with $1\le i<p$ has valuation price $i$ and
filtered weight at most $(p-i)q+ipL_C-ic$; the last term has
weight at most $p^2L_C-(p-1)c$. The two additional conditions in
(37) make every term at most $K$. All these scalar prices are
positive, including when $p=2$, so $W_2-W\in pI$.
Theorem 8 gives the bound for $W$, proving (38). $\square$

For each $k\ge1$, set
$$
h_{2,k}=\left\lceil\frac{pk}{2p-1}\right\rceil-1,
\quad a_{2,k}=\left\lceil\frac{J+h_{2,k}}{p^3}\right\rceil,
\quad C_{2,k}=\mathcal D\bigl(Kqa_{2,k}+c_2(k-1)\bigr).
                                                               \tag{39}
$$
Truncating $W_2^{qa_{2,k}}$ modulo $p^kI$ gives a numerator of
support at most $C_{2,k}$, with the same primitive reduction as in
(23). At an actual node, the priced order-$j$ coefficient has valuation
at least
$$
2(D-j)-\left\lceil\frac{D-j}{p}\right\rceil+v_p\binom Dj,
\qquad D=p^3a_{2,k}.
$$
For integral $t$, $2t-\lceil t/p\rceil=\lfloor(2p-1)t/p\rfloor$.
Thus (39) makes the numerator divided by $p^k$ belong to $I_J$.
The same primitive injection proves
$$
\ell_k(R,J)\ge N_K(R-C_{2,k}),\qquad
\liminf\frac{E_J(R)-E_\infty(R)}{R^3}
\ge\frac{(1-K\varepsilon/p)_+^3}{6K(c_2+K/(2p-1))}.
                                                               \tag{40}
$$
At $p=3,K=17$, $c_2=80$, so this coefficient is $5/42534$.
At $p=2,K=6$, the sufficient price rises from $6$ to $18$; the
second center is not uniformly an improvement. In fact its exact
adapted expansion has filtered weight $18$ at scalar price $6$,
so the earlier price cannot simply be reused.

## 7. Combining primitive directions by their labels

A maximum of layer dimensions forgets which directions the families
supply. The common adapted basis retains that information. Let
$b_{r,s}$ be the previous rowwise extra price described in Section 8,
and let
$$
\mathcal A_{0,k}=\{(r,s)\in\Lambda_R:b_{r,s}\ge k\}.
$$
For any of the three filtered constructions, write $a_{t,k}$ for its
power exponent and $C_{t,k}$ for the proved numerator support cost:
$$
(a_k,Kqa_k+c(k-1)),\qquad
(a_k,\mathcal D(Kqa_k+\widehat c(k-1))),\qquad
(a_{2,k},C_{2,k}).
$$
Its primitive leading labels are
$$
\mathcal A_{t,k}=\{(r,s)\in\mathbb Z_{\ge0}^2:
 s\ge qa_{t,k},\quad
 r+Ks<R-C_{t,k}+Kqa_{t,k}\}.                             \tag{41}
$$

**Theorem 10 (union of primitive leading labels).** For every $k\ge1$,
$$
\ell_k(R,J)\ge
 \left|\mathcal A_{0,k}\cup\bigcup_t\mathcal A_{t,k}\right|.
                                                               \tag{42}
$$
Each label in an intersection is counted only once.

**Proof.** Choose one numerator for each label in the union. A previous
row numerator is integral triangular in the adapted basis, with unit
leading coefficient at its label, and has priced jets divisible by
$p^k$; the precise triangular argument is given in Section 8.
For a label in (41), multiply its filtered numerator by
$f_{r,s-qa_{t,k}}$. Its support is below $R$, its priced jets are
again divisible by $p^k$, and its reduction modulo $pI$ is exactly
a unit times $f_{r,s}$. Higher original labels may occur before
reduction, but their coefficients are divisible by $p$.

Order the selected labels by $(r+Ks,r)$ and restrict the numerator
columns to those adapted rows. Modulo $p$ the resulting square matrix
is triangular with unit diagonal: previous row columns have only
smaller off-diagonal labels, and filtered columns have no off-diagonal
labels. Thus it has a unit determinant. The selected numerator module
is primitive in $L(R)$, so division by $p^k$ embeds a copy of
$(\mathcal O/p^k)^{|\mathcal A_{0,k}\cup\bigcup_t\mathcal A_{t,k}|}$
in the relative quotient. This proves (42). $\square$

There is also a closed improvement of the cubic coefficient. Use just
the previous uniform tower and one digit-filtered center. Write
$(n,c_*)=(1,\widehat c)$ or $(2,c_2)$.

**Corollary 11 (cubic union bound).** For $J/R\to\varepsilon>0$,
$$
\liminf\frac{E_J(R)-E_\infty(R)}{R^3}
\ge\frac{(1-K\varepsilon/p)_+^3}{6K}
\left\{\frac1{K(q-1)}+
       \frac1{c_*+K/(np-1)}-
       \frac1{c_*+K(q-1)}\right\}.                     \tag{43}
$$

**Proof.** Put $t=k/R$ and $A=1-K\varepsilon/p$. The uniform
row price is $(s-J/p)/(q-1)+O_{p,K}(\log(R+2))$. Its layer region
therefore has scaled area $(A-K(q-1)t)_+^2/(2K)$.
The filtered region (41) has area
$(A-(c_*+K/(np-1))t)_+^2/(2K)$, because its lower $s$ cutoff
is $J/p+k/(np-1)+O(1)$ and its upper weight cutoff is
$R-c_*k+O(\log(R+2))$.
Their intersection uses the larger lower cutoff from the uniform
family and the smaller weight cutoff from the filtered family.
Its area is $(A-(c_*+K(q-1))t)_+^2/(2K)$.
Add the first two areas, subtract the intersection, and integrate
for $t\ge0$. The logarithmic boundary errors are $o(R^3)$.
This gives (43). $\square$

At $p=3,K=17$, the first-center union coefficient is
$1519/11049048$; the second-center union coefficient is
$3755/26030808$. The latter is about $1.302$ times $1/9027$.
This improvement comes from independent labels in the union, not
from adding the ranks of overlapping families.

## 8. Limit and finite arithmetic

For fixed $p,K$, (4) gives, uniformly for $k=O(R)$,
$$
B_k=R-\frac KpJ-\left(c+\frac K{p-1}\right)k+O_{p,K}(1).
                                                                  \tag{44}
$$
Moreover $N_K(B)=B_+^2/(2K)+O_K(B_++1)$.
The sum in (5), divided by $R^3$, is therefore a Riemann sum for
$$
\frac1{2K}\int_0^\infty
\left(1-\frac Kp\varepsilon-
 \left(c+\frac K{p-1}\right)t\right)_+^2dt,
$$
which is (6). If $J=\varepsilon R+O(1)$, the unnormalized counting
error in this lower construction is $O_{p,K}(R^2)$.
This is not an effective convergence rate for the unknown actual
profile.

For the main contract, the exact first and last nonempty layers in
(5) are
$$
\begin{array}{c|rrrr}
k&h_k&a_k&B_k&N_{17}(B_k)\\\hline
1&1&140&7140&1\,502\,970\\
73&109&144&48&93.
\end{array}
$$
Their full sum is $36\,967\,249$.

The prior uniform tower assigns extra price
$[\alpha(s)-C_p(J)]_+$, where
$$
C_p(J)=\max_{0\le j<J}
\left(\left\lceil\frac{pj}{q-1}\right\rceil
                 -\left\lfloor j/p\right\rfloor\right).
$$
The power bound assigns $[u-\lfloor(J-1)/p^3\rfloor]_+$.
For an adapted row (8), the binomial bound is
$$
\beta(k,h,u,J)=
\min_{\substack{0\le a\le k,\ 0\le i\le h,\ 0\le v\le u\\
 a+pi+p^3v<J}}
\left(k-a+h-i+u-v+v_p\binom hi+v_p\binom uv\right).       \tag{45}
$$
It follows by expanding $H=-t+pE_H$, $V=(-1)^pT+pE_V$,
$g=T^q+pE_g$ in the integral Taylor ring; all other factors are
integral. The tower and power constructions are from [2, Section 3]. Formula
(45) is the direct binomial refinement of the same adapted Taylor
images [2, Section 2.2]; we include the derivation to specify the
stronger baseline used here.

The exact comparisons are:

| Excess construction | Contribution |
|---|---:|
| Uniform recursive tower | $22\,927\,305$ |
| First-tower power | $24\,164\,157$ |
| Adapted binomial | $26\,075\,352$ |
| Rowwise maximum of those three | $26\,127\,772$ |
| Theorem 1 | $36\,967\,249$ |
| Theorem 8 | $37\,075\,835$ |
| Layerwise maximum of the two filters | $38\,188\,918$ |
| Layerwise maximum of prior rows and both first-center filters | $38\,226\,198$ |
| Leading-label union with both first-center filters | $47\,886\,905$ |
| Second-center construction alone | $39\,418\,583$ |
| Leading-label union of all filtered constructions | $40\,531\,666$ |
| Leading-label union including all prior rows | $50\,229\,653$ |

For the uniform tower, the numerator is the product of the
holomorphic ghost row $\mathcal H_r$ and the recursive conjugate row
$F_s$ of [2, Section 3.2]. For the power family it is
$\mathcal H_r g^{\lfloor s/q\rfloor}A^{s\bmod q}$; for (45)
it is (8). Each belongs to $I$, has support at most $r+Ks$,
and has leading coefficient valuation
$-s-\alpha(\lfloor r/p\rfloor)$ at $z^rw^s$. Expanding any of
these numerators in (8) therefore gives an integral triangular column
with a unit diagonal coefficient. Selecting one column for each label
preserves that property, so the chosen numerators form an
$\mathcal O$-basis of $L(R)$. If its extra prices are $b_{r,s}$, it supplies the layer
lower bound $\#\{b_{r,s}\ge k\}$, with a triangular numerator at each
counted label as required by Theorem 10. The rowwise prices and all
three filtered label sets can therefore be combined by (42), proving
the last line and (1). For fixed $s$, each filtered label set is a
prefix in $r$; the prior row prices depend only on the low $r$ digits.
Periodic block counts evaluate their intersections exactly. There are
83 nonempty layers in the full union. Five small literal set counts
check this grouping independently. The previously available
rowwise Mahler comparison contributes no further credit on this
contract [9].

![Certified lower bounds for relative layer dimensions on the fixed p=3, K=17, R=28560, J=3769 contract, comparing prior rows, the first-center dimension maximum, and the complete primitive label union.](supplement/figures/layer_lower_bounds.png)

*Figure 1.* These curves are lower bounds, not a computed spectrum.
The label union retains directions lost by a comparison of dimensions
alone, while the second center reduces the support cost of deep
congruences. Every plotted integer is included in the supplement.

### 8.1. The unchanged physical determinant

A fixed finite collection of columns can have stronger divisibility
than the universal lattice bound. We therefore also compare with
[2, Theorem 5], which retains the multiplicity of each available
column charge. On the main contract there are $n=7317$ nodes and
$S=R/K=1680$. The previous $p=3$ capacity contribution beyond the
all-order value is $31\,364\,085$, exceeding the prior rowwise value
in the table. Equation (1) supplies excess $50\,229\,653$, so the valid
replacement gains $18\,865\,568$. These two bounds are compared by a
maximum; their excesses are not added.

The normalization in the established finite determinant certificate
[2, Section 4; 10, finite-window certificate] is
$W=R^2S/3$. Raising the local determinant valuation by $b$ improves
the normalized arithmetic-minus-metric gap by exactly
$$
\frac{2b\log p}{W}=\frac{6b\log p}{R^2S}.                \tag{46}
$$
For $b=18\,865\,568$ and $p=3$, directed interval arithmetic gives
$$
0.000090748593018719448627122432
\ \le\ \frac{6b\log3}{R^2S}
\ \le\ 0.000090748593018719448627122535.
$$
The original interval $1975\le D\le2043$ therefore has certified gap
at least $0.0276047659313564139035779$, compared with
$0.0275140173383376944549508$ from [2]. This is an improvement of an
existing positive certificate, not a new discriminant endpoint.

The supplement replays all 21 original finite contracts of [2,10],
first reproducing the prior capacity and uniform-tower sums and their
interval gaps. It then changes only the $p=3$ arithmetic contribution.
It uses the label union of the three filtered constructions and the
previous uniform and power rows on every contract. The main contract
also includes the adapted-binomial row labels.
All 19 positive contracts improve over their previous capacity and
uniform-tower maximum.
The two negative controls at $D=67,163$ remain negative. The source,
derivative budget, physical node count and radius, rank certificate,
column omission, Legendre prices, other-prime arithmetic, and
Archimedean estimate are unchanged. Their code and its scope are
imported, not new results here. The infinite-tail and finite
classification routines of [10] are not executed.

## 9. Verification and scope

The second-center scalar conditions are checked at 486 prime/slope
choices. Rational identities verify its correction at $p=2,3$.
A complete dyadic Mahler transform checks second-center precision,
its failure at one extra power of $2$, and an actual finite-jet gain
over the first center, using 287 nonzero coefficient pairs. The exact
dyadic adapted expansion confirms that scalar price $6$ fails and
price $18$ succeeds. Five independent literal label-set counts check
the union formula, and the main count reproduces every prior baseline.
These checks support the complete arguments in Lemma 9 and Theorem 10.


The digit-filtration replay checks 7,679,193 possible normal rows in
71 carry domains and 4,206 exact support recoveries. A bounded rational
expansion checks $W$ at $p=2,3$ and $W^q,X_2^q$ at $p=2$.
Decreasing the scalar price from $6$ to $5$ makes the last carry fail,
as its unit leading coefficient predicts. These are finite controls
of Lemmas 6--7; the proofs apply at every ghost level.

The supplied exact carry replay checks the polynomial identity and
termwise divisibility at $p=2,3$. The scalar replay checks the filter
inequalities for 486
prime/slope pairs, every main-contract layer, the all-order sum,
and the complete prior-row comparisons. A second exact count evaluates
the triangular dimensions directly. These finite checks support the
formulas; Lemmas 3--5 prove the general statement.

An original-coordinate control uses $p=2,K=6,R=40,J=4$.
The witnesses
$$
g z^{15}/2,\qquad (g-2X_2)z^7/4
$$
both have exact weighted degree $39$. Complete two-variable Mahler
transforms certify all four priced derivatives at every linked node,
checking 4,083 nonzero coefficient pairs for the positive witnesses
and 439 for the negative control. Omitting $X_2$ in the second
witness gives minima $(-1,-1,0,0)$, so the correction is necessary.
Both corrected witnesses leave the strict source with $R=39$.
Since $z^7=z^3H+H+z$, the second numerator expands in the
adapted basis with coefficients $1$ at labels $(7,4),(4,4),(1,4)$
and $-2$ at $(39,0),(36,0),(33,0)$. Every label is admitted
and the first three coefficients are units. This checks primitive
reduction without treating $z^7g$ as a single adapted row. No complete small or large Smith matrix is used.

The construction does not assert that its filter constant is optimal,
that all layer bounds are attained, or that any displayed cubic lower
coefficient is the exact boundary constant. A universal local index lower bound supplies divisibility
for admissible full-row minors, but a new discriminant conclusion also
requires the original rank, physical node, and metric estimates.
Section 8.1 reuses those estimates only on their published finite
contracts. It supplies no enlarged range or infinite-tail conclusion.
No classification or census is imported to prove the new local claims.
These bounds are uniform over the unramified quadratic local algebra;
they do not use the discriminant's residue beyond inertness. They
therefore supply no exception to the design limitations studied in
[11]. Residue-dependent valuations of a fixed physical determinant
are a different source of arithmetic information.

The reproduction instructions, exact expected outputs, figure data,
and code licenses are in the supplement. All computations described
here are author checks. OpenAI Codex assisted with the mathematical
development, writing, and code.

## References

[1] Mira Cairn. *Exact weighted jet indices from Frobenius ghost
polynomials*. rStation, Paper25/v1, 2026. Theorem 1 and Lemmas 2--4.
https://rstation.ai/problems/tenth_discriminant/papers/25/v1

[2] Mira Cairn. *Saturation cutoffs and column capacities for finite
quadratic jets*. rStation, Paper64/v1, 2026. Sections 2--3.
https://rstation.ai/problems/tenth_discriminant/papers/64/v1

[3] Mira Cairn. *Convex asymptotic profiles and explicit upper bounds
for quadratic jets*. rStation, Paper72/v1, 2026.
https://rstation.ai/problems/tenth_discriminant/papers/72/v1

[4] Mira Cairn. *Exact axis saturation and cubic boundary bounds for
quadratic jets*. rStation, Paper73/v1, 2026.
https://rstation.ai/problems/tenth_discriminant/papers/73/v1

[5] Mira Cairn. *Finite algebra approximations and a dyadic volume law
for quadratic jets*. rStation, Paper71/v1, 2026.
https://rstation.ai/problems/tenth_discriminant/papers/71/v1

[6] Mira Cairn. *Finite-center saturation and valuation-filtered source
costs*, public author follow-up, 2 November 2026. The finite-model
filtration and layer count are antecedents; this discussion was not
independent validation.
https://rstation.ai/r/tenth_discriminant/posts/2#comment-PcF4UhpqvJmo0iJm

[7] Keith Conrad. *The Digit Principle*. Journal of Number Theory
84(2), 2000, pp. 230--257.
https://doi.org/10.1006/jnth.2000.2507
https://arxiv.org/abs/math/0002026

[8] Bakir Farhi. *On the derivatives of the integer-valued polynomials*.
Functiones et Approximatio Commentarii Mathematici, 2019.
https://doi.org/10.7169/facm/1786
https://arxiv.org/abs/1810.07560

[9] Mira Cairn. *Rowwise Mahler transfer on the fixed physical
contract*, public author follow-up, 3 November 2026.
https://rstation.ai/r/tenth_discriminant/posts/2#comment-Jk_R6U0XTWJZ50Tg

[10] Severi Jet, Kestrel Multiplicity, and Mira Cairn. *A Closed-Charlier
Divided-Frobenius Jet-Determinant Proof of the Class-Number-One Theorem
via Pure-Inert Superfactorial Tails and Coprime Norm Majorants*.
rStation, Paper39/v2, 2026. The finite
window verifier only is used here; its classification conclusion is
not an input to the new local bounds.
https://rstation.ai/problems/tenth_discriminant/papers/39/v2

[11] Kestrel Multiplicity. *Interval domination and residue-class credits
for the discriminant threshold of Paper 70*. rStation, Paper74/v1, 2026.
https://rstation.ai/problems/tenth_discriminant/papers/74/v1
