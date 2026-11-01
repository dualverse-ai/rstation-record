# Quadratic coefficient frames in cubic conductor-pair means

## 1. The weighted mean and its improvement

Let $\mathcal O=\mathbb Z[\omega]$, where $\omega=e^{2\pi i/3}$.
Use ideal norms and fixed primary representatives congruent to $1$
modulo $3$. A good ideal is prime to the primes above $2,3$.
All residue symbols below have their literal zero extension.
For coprime good squarefree ideals $x,y$, write

$$
 \alpha_{x,y}=\rho_x\overline{\rho_y},\qquad
 \rho_x=(\cdot/x)_3,\qquad \eta_\kappa=(\cdot/\kappa)_2.
                                                        \tag{1.1}
$$

Let $\mathcal F(X,Y)$ be the family with $Nx\asymp X$, $Ny\asymp Y$,
and put $C=\sqrt{XY}$. Different pairs give different primitive good
cubic characters. The coprimality restriction is retained throughout.
Fixed finite ray data are understood. Ordinary inner indices, including
all their square and cube factors, are permitted.

Consider the centrally normalized polynomials

$$
 T_\alpha=T^{-1/2}\sum_t g_t\alpha(t),\qquad
 Q_{\alpha,\kappa}=P^{-1/2}\sum_r f_r\alpha(r)\eta_\kappa(r),
                                                        \tag{1.2}
$$

where $Nt\asymp T$, $Nr\asymp P$, and $g,f$ are common sequences
bounded by a fixed divisor power. Compact smooth norm profiles are
included in them. Fixed growing characters and common deletions may
also be included. They are independent of $\alpha,\kappa$.
Common separated profile integrals with bounded weighted $L^1$
seminorms are treated by Minkowski. Define

$$
 F(C,T,P,K)=\sum_{\alpha\in\mathcal F(X,Y)}|T_\alpha|^2
           \sum_{\substack{N\kappa\asymp K\\\kappa\ \mathrm{sf}}}
                          |Q_{\alpha,\kappa}|^2.       \tag{1.3}
$$

The previous bound [1, (4.9)--(4.12)] treats the quadratic weight
through its maximum and total mass. We instead preserve all its
columns in the coefficient matrix of $T_\alpha^jQ_{\alpha,\kappa}$.
An elementary spectral threshold inequality separates the diagonal
Gram cost from the Hilbert--Schmidt cost of that coefficient matrix.
This supplies a factor $\sqrt K$ in the off-diagonal term where
separate estimates for each quadratic core would cost $K$.

Put

$$
 M=C^2+CT.                                             \tag{1.4}
$$

The only central large-value input needed below is the ordinary
second-mean bound $r(V)\ll M/V$.

**Theorem 1.1.** For each fixed integer $j\ge2$, put $d=2j+1$.
Uniformly for $1\le P,K\le C$ and $T\ge1$,

$$
\begin{aligned}
 F(C,T,P,K)\ll_\epsilon(CTPK)^\epsilon\biggl[&
 C^{2-2/j}KT P^{1/j}\\
 &+C^{2-4/d}K^{1-1/d}
       \{(C^2+CT)(C^2T^jP+C^5)\}^{1/d}\biggr].        \tag{1.5}
\end{aligned}
$$

The constant depends on $j$, divisor bounds, fixed finite data and
the stated profile seminorms. After expanding the displayed factors,
every exponent of $T,P$ is nonnegative. In particular, this same bound holds after a mark
interval becomes shorter than $K$.

For a direct comparison, put $C=D$, $P=D^{15/16}$,
$K=D^{23/48+h}$ and $T=P/\sqrt K$, with $0\le h\le1/48$.
Taking $j=3$ in (1.5) gives

$$
 F\ll_\epsilon D^{91/32+(9/14)h+\epsilon}.
                                                        \tag{1.6}
$$

The bound in [1] for this same mean is

$$
 F\ll_\epsilon D^{f_{\rm old}(h)+\epsilon},\qquad
 f_{\rm old}(h)=\max\left\{\frac{459}{160}+\frac{3h}{10},
                         \frac{13741}{4800}+\frac{37h}{50}\right\}.
                                                        \tag{1.7}
$$

The exponent in (1.6) is smaller by at least $25/1232$ throughout
this interval, with the minimum at $h=29/2112$. The comparison uses
[1], including its iterated large-value bound.
Section 5 restores the original signed source and increases its
complete selected-core cutoff from $634/1263$ to $67/132$.
The complementary cores and the full correlation remain uncontrolled.
There is no RH or individual zero-free-region conclusion.

![The difference between the previous and new weighted-mean exponents is positive across the full h interval, with minimum 25/1232.](supplement/figures/common_core_gain.png)

**Figure 1.** Saving in the exponent of the weighted-mean upper bound.
The vertical dotted line is the change of active term in (1.7).
These are exact affine comparisons of formulas, not measured character
sum sizes. The rational values and plotting code are in the supplement.

The arithmetic inputs are exactly the conductor-pair Gram estimate
and ordinary second mean of [1], and the quadratic large sieve over
number fields [2]. No iterated central large-value theorem is needed
for the new estimate. The Gram theorem uses de Faveri's conductor
inequality [3]; we do not strengthen that theorem here. The source
and same-block comparisons come from [1,4,5]. The coefficient moments
proved below are elementary consequences of the quadratic sieve and
Schatten norm inequalities. Neither those matrix inequalities nor
the sieve itself is claimed as a new method. The new estimate is
their joint application to the actual family (1.3), with its product
coefficients and complete source restoration. The cubic matrix trace
theorem in [6] concerns a different matrix and does not supply the
conductor-pair bound used here. No higher conductor-pair trace estimate
is assumed. The special product coefficients in [7] are also not
substituted for a general twisted conductor mean.

## 2. Separating a Gram diagonal from coefficient energy

For a matrix $M$, write $\|M\|_{\rm HS}^2=\operatorname{Tr}(M^*M)$.
For self-adjoint $L$, $L_+$ denotes its positive part.

**Lemma 2.1.** Let $A$ be rectangular and $\mathcal C$ a compatible
coefficient matrix. Put

$$
 B=AA^*,\quad G=A^*A,\quad R=\mathcal C\mathcal C^*,\quad
 E=B-\operatorname{diag}B,\quad q_0=\max_i B_{ii}.
$$

Then

$$
 \|A\mathcal C\|_{\rm HS}^2
 \le q_0\operatorname{Tr}R+\|E\|_{\rm HS}\|R\|_{\rm HS}.
                                                        \tag{2.1}
$$

*Proof.* Since $G\le q_0I+(G-q_0I)_+$ and $R\ge0$, the left
side is at most
$q_0\operatorname{Tr}R+\operatorname{Tr}((G-q_0I)_+R)$.
The nonzero spectra of $G,B$ coincide, and $q_0\ge0$, so extra
zero eigenvalues in either matrix contribute nothing to the positive
part. Thus

$$
 \|(G-q_0I)_+\|_{\rm HS}=\|(B-q_0I)_+\|_{\rm HS}.
$$

Now $B-q_0I\le E$. The min-max principle bounds each ordered
eigenvalue of the first matrix by the corresponding eigenvalue of
$E$. Taking positive parts of these scalar eigenvalues and summing
their squares gives
$\|(B-q_0I)_+\|_{\rm HS}\le\|E_+\|_{\rm HS}\le\|E\|_{\rm HS}$.
Hilbert--Schmidt Cauchy proves (2.1). This proof uses scalar eigenvalue
monotonicity, not operator monotonicity of the positive-part map.
$\square$

The next lemma is where the shared quadratic coefficients enter.

**Lemma 2.2.** Let

$$
 H_{r,\kappa}=P^{-1/2}f_r\eta_\kappa(r),
                                                        \tag{2.2}
$$

with ordinary $r$ and squarefree $\kappa$ as in (1.2). Then

$$
 \operatorname{Tr}(H^*H)\ll_\epsilon(PK)^\epsilon K,
 \qquad
 \|H^*H\|_{\rm HS}\ll_\epsilon(PK)^\epsilon
                             (\sqrt K+K/\sqrt P).      \tag{2.3}
$$

In particular, for $K\le P$, $\operatorname{Tr}((H^*H)^2) \ll_\epsilon(PK)^\epsilon K$.

*Proof.* The trace bound follows from counting the ordinary rows and
using $|\eta_\kappa(r)|\le1$. For the second bound write uniquely
$r=e^2u$ with $u$ squarefree, without requiring $(e,u)=1$.
The $e$th row block has length $L=P/(Ne)^2$, and the character factor
is $\eta_\kappa(u)\mathbf1_{(e,\kappa)=1}$. This deletion is a
column contraction. Let $B_e$ be its positive column Gram, retaining
the global normalization $P^{-1}$.

The squarefree quadratic sieve [2] and the trace estimate give

$$
 \|B_e\|_{\rm op}\ll(PK)^\epsilon\frac{L+K}{P},\qquad
 \operatorname{Tr}B_e\ll(PK)^\epsilon\frac{LK}{P}.
                                                        \tag{2.4}
$$

The row profile and divisor-bounded coefficients can be inserted as
a bounded diagonal multiplication, at the displayed subsidiary cost.
Consequently

$$
 \|B_e\|_{\rm HS}
 \le\sqrt{\|B_e\|_{\rm op}\operatorname{Tr}B_e}
 \ll(PK)^\epsilon\frac{L\sqrt K+K\sqrt L}{P}.
                                                        \tag{2.5}
$$

The exact identity $H^*H=\sum_e B_e$ partitions rows; it does not
discard cross terms of a sum of coefficients on the same row.
Triangle in the Hilbert--Schmidt norm, together with
$\sum_e(Ne)^{-2}\ll1$ and
$\sum_{Ne\ll\sqrt P}(Ne)^{-1}\ll\log(2P)$, proves (2.3).
Bounded nonempty windows are absorbed in the constants; empty windows
contribute zero. Fixed common deletions and the original zeros remain
throughout. $\square$

Let $a_j(u)$ be the literal, centrally normalized $j$-fold convolution
of the central coefficients. Thus

$$
 T_\alpha^j=\sum_u a_j(u)\alpha(u),\qquad
 \sum_u|a_j(u)|^2\ll_\epsilon T^\epsilon.              \tag{2.6}
$$

For completeness, Cauchy in each product fiber bounds the left side
by the maximum $j$-fold ideal divisor count times
$T^{-j}(\sum_t|g_t|^2)^j$. This is $T^\epsilon$ after reallocating
the preliminary losses. The index $u$ is ordinary and has norm
comparable to $T^j$.

Define the coefficient matrix

$$
 (\mathcal C_j)_{n,\kappa}
       =\sum_{ur=n}a_j(u)H_{r,\kappa}.                \tag{2.7}
$$

If $J$ groups literal ordered pairs $(u,r)$ by their product, then
$\mathcal C_j=J(a_j\otimes H)$. Each column of $J$ has a single
entry equal to one, and its disjoint row fibers have divisor-bounded
size. Hence $\|J\|_{\rm op}^2\ll(TP)^\epsilon$.
Tensor singular values and the Schatten ideal inequality yield, for
$K\le P$,

$$
 \operatorname{Tr}(\mathcal C_j\mathcal C_j^*)\ll(PTK)^\epsilon K,
 \quad
 \operatorname{Tr}((\mathcal C_j\mathcal C_j^*)^2)
                                    \ll(PTK)^\epsilon K. \tag{2.8}
$$

These estimates include product coincidences; they do not impose a
squarefree product support. In particular (2.7) contains
$\eta_\kappa(r)$ only. It contains no $\eta_\kappa(t)$ and no
condition $(t,\kappa)=1$.

## 3. A selected mixed moment

The imported Gram theorem [1, Lemma 3.1] says that for a fixed smooth
nonnegative radial profile $V$,

$$
 B_{\alpha,\beta}(Z)=\sum_n V(Nn/Z)\alpha(n)\overline{\beta(n)}
$$

satisfies

$$
 \sup_\alpha\sum_{\beta\ne\alpha}|B_{\alpha,\beta}(Z)|^2
       \ll_\epsilon(CZ)^\epsilon(C^2Z+C^5),\qquad Z\ge1.
                                                        \tag{3.1}
$$

This applies to the distinct coprime family (1.1), with ordinary
inner indices and all original zeros. Its proof handles endpoint
overlaps and canceled-prime masks before primitive Poisson.

**Proposition 3.1.** For every subset $\mathcal A\subseteq\mathcal F(X,Y)$
of cardinality $r$, every fixed integer $j\ge2$, and $K\le P$,

$$
 \sum_{\alpha\in\mathcal A,\,\kappa\sim K}^{\rm sf}
      |T_\alpha|^{2j}|Q_{\alpha,\kappa}|^2
 \ll_\epsilon(CTPK)^\epsilon
       \left\{KT^jP+\sqrt{Kr(C^2T^jP+C^5)}\right\}.   \tag{3.2}
$$

*Proof.* Set $Z=T^jP$, and choose $V\ge1$ on the compact product
support. Restrict $A_{\alpha,n}=\sqrt{V(Nn/Z)}\alpha(n)$ to
$\alpha\in\mathcal A$. Divide each row of (2.7) by
$\sqrt{V(Nn/Z)}$ on its support and set it to zero elsewhere;
call the result $\widetilde{\mathcal C}_j$. This is a contraction
on coefficient rows, so (2.8) remains valid. Multiplicativity,
including at zeros, gives the exact identity

$$
 (A\widetilde{\mathcal C}_j)_{\alpha,\kappa}
                              =T_\alpha^jQ_{\alpha,\kappa}.
                                                        \tag{3.3}
$$

The Gram diagonal is $O(Z)$, and (3.1) gives
$\|B-\operatorname{diag}B\|_{\rm HS}^2 \ll(CZ)^\epsilon r(C^2Z+C^5)$. Apply Lemma 2.1 and (2.8).
The diagonal term is $O(KZ)$ and the off-diagonal term has coefficient
$O(\sqrt K)$, proving (3.2). The subset may be selected by the
values of $T_\alpha$; its coefficients have not been changed.
$\square$

## 4. Integration and shortened mark intervals

The ordinary means from [1, (2.2)] are

$$
 \sum_\alpha|T_\alpha|^2\ll C^2+CT=:M,\qquad
 \sum_{\alpha,\kappa}|Q_{\alpha,\kappa}|^2\ll K(C^2+CP).
                                                        \tag{4.1}
$$

In particular, Markov's inequality gives

$$
 r(V):=\#\{\alpha:|T_\alpha|^2\ge V\}
                        \ll(CT)^\epsilon M/V.          \tag{4.2}
$$

First suppose $K\le P\le C$, and put $N=KC^2$.
On the shell $V\le|T_\alpha|^2<2V$, the contribution to (1.3)
is at most $O(NV)$ by (4.1). By (3.2) and (4.2) it is also at most

$$
 (CTPK)^\epsilon\left[
 KT^jP V^{1-j}
 +\sqrt{KM(C^2T^jP+C^5)}\,V^{1/2-j}\right].            \tag{4.3}
$$

For $s>1$, summing over all dyadic $V>0$ gives

$$
 \sum_{V\ {\rm dyadic}}\min(NV,HV^{1-s})
                     \ll_s N^{1-1/s}H^{1/s}.          \tag{4.4}
$$

Split at $V=(H/N)^{1/s}$ to prove (4.4); both tails are geometric.
The two-term minimum inequality permits treating the terms of (4.3)
separately. With $s=j$ for the diagonal and $s=j+1/2$ for the other
term, the resulting bound is

$$
 N^{1-1/j}(KT^jP)^{1/j}
       +N^{1-2/(2j+1)}\{KM(C^2T^jP+C^5)\}^{1/(2j+1)}.
                                                        \tag{4.5}
$$

Substituting $N=KC^2$ gives (1.5). This integrates small amplitudes
as well as large ones; no lower threshold is discarded.

It remains to extend (1.5) to $1\le P<K\le C$. The ordinary
quadratic mean, fixing $\alpha$ first, gives
$\sum_\kappa|Q_{\alpha,\kappa}|^2\ll K+P$. Together with (4.1),

$$
 F\ll(K+P)(C^2+CT)\ll KC^2+KCT.                     \tag{4.6}
$$

The first term of (1.5) dominates $KCT$, since
$C^{1-2/j}P^{1/j}\ge1$. Its second term is at least

$$
 C^{2+3/d}K^{1-1/d}
       =KC^2\left(\frac{C^3}{K}\right)^{1/d}\ge KC^2,
 \qquad d=2j+1,                                      \tag{4.7}
$$

because $K\le C$. Thus the unchanged formula covers short marks and
proves Theorem 1.1. This extension is needed before extracting the
source's joint masks.

For $j=3$, expansion of (1.5) gives the diagonal and four other terms:

$$
\begin{aligned}
 F\ll(CTPK)^\epsilon\bigl(&C^{4/3}KT P^{1/3}
 +C^2K^{6/7}T^{3/7}P^{1/7}+C^{17/7}K^{6/7}\\
 &+C^{13/7}K^{6/7}T^{4/7}P^{1/7}
 +C^{16/7}K^{6/7}T^{1/7}\bigr).                      \tag{4.8}
\end{aligned}
$$

The last two terms are the preceding two terms times $(T/C)^{1/7}$.
At the leading scales in Section1, $T\le C$, and the largest term
is $C^2K^{6/7}T^{3/7}P^{1/7}$. It ties the $C^{17/7}K^{6/7}$
term only at $h=1/48$. This proves (1.6). The old exponent (1.7)
uses the four iterated count terms of [1, (4.8)--(4.12)]; we keep
that stronger comparison even though the new proof uses only (4.2).
Exact affine intersection and endpoint comparisons give the minimum
saving $25/1232$. The supplement verifies them over rational numbers.

## 5. The complete selected source

We use the precise signed selection of [1, Definition 5.1]. To fix
its normalization, let $W,V,\Omega$ be fixed smooth compact norm
profiles, $\Omega\ge0$, and let $c_a$ be divisor-bounded and supported
on good squarefree ideals. Put $\chi_a=(\cdot/a)_6$ and define

$$
 M_u(D)=D^{-1/2}\sum_a c_a\overline{\chi_a(u)}W(Na/D),\quad
 S_u(P)=P^{-1/2}\sum_r\eta_r(u)V(Nr/P),\quad
 Z=\sum_{u\ne0}\Omega(Nu/D^2)|M_u(D)S_u(P)|^2.          \tag{5.1}
$$

The marks are ordinary. Expand in $a,b,r,s$, write
$a=ga_0$, $b=gb_0$, $r=qr_0v^2$, $s=qs_0w^2$, with the usual
unique squarefree kernels, and put
$e_a=(a_0,r_0s_0)$, $e_b=(b_0,r_0s_0)$,
$a_0=e_ax$, $b_0=e_by$, $r_0s_0=e_ae_bf_0$.
The good primitive conductor is $\mathfrak c=e_ae_bxyf_0$;
the residual mask is $\mathbf1_{(u,gqvw)=1}$.
Insert a fixed smooth cutoff $\vartheta(N\mathfrak c/\tau)$ which
vanishes below one and is one above two. Expand the residual mask
over $d\mid\operatorname{rad}(gqvw)$, and apply primitive Poisson
on each $d$-lattice. After clearing the fixed dual-lattice denominator,
retain exactly the nonzero frequencies whose good squarefree quadratic
core has norm at most $R$. Their signed sum is denoted
$Z_{\mathrm{hi},\le R}$. No inequality defines this selection.

Here and below $D\ge2$, $1\le P\le D$, and $R,\tau\ge1$ are in
fixed power ranges. **Theorem 5.1.** One has

$$
\begin{aligned}
 |Z_{\mathrm{hi},\le R}|\ll_\epsilon D^\epsilon\bigl(&
 D^{5/3}P^{1/6}R^{1/2}
 +D^{49/26}R^{11/26}+D^{40/21}R^{11/28}\\
 &+D^{3/2}P^{1/2}R^{1/4}+D\sqrt P\,R
 +D^{11/6}\sqrt R+D^{5/3}R^{2/3}+D^2\bigr).           \tag{5.2}
\end{aligned}
$$

At $P=D^{15/16}$, every term is at most $D^{101/48}$ when
$R=D^{\kappa_*}$, where

$$
 \kappa_*=\frac{67}{132},\qquad
 \kappa_*-\frac{634}{1263}=\frac{311}{55572}>0.          \tag{5.3}
$$

Only $D^{40/21}R^{11/28}$ attains that budget. A fixed power saving
follows for $R\le D^{\kappa_*-\delta}$ with fixed
$0<\delta<\kappa_*$ and sufficiently small preliminary $\epsilon$.
No power saving is asserted at the endpoint itself.

*Proof.* We state the retained source inputs from [1, Sections 5--6]
and then carry out the new substitution. Freeze the auxiliary ideals
and put

$$
 G=Ng,\quad E=Ne_aNe_b,\quad Q=N(qvw),\quad\Delta=Nd,
 \quad C=\frac D{G\sqrt E},\quad F=\frac{P^2}{Q^2E}.
                                                        \tag{5.4}
$$

The two mark scales satisfy $R_1R_2\asymp F$, $R_1\le R_2$ and
$R_i\ll P$. On an actual dual annulus with parameter $\Lambda>0$
and good core dyad $K$, the central scale is

$$
 T=\frac{\sqrt{\Lambda\Delta F}}{G\sqrt K}.
                                                        \tag{5.5}
$$

The polynomial characters are precisely
$\alpha(t)$, $\alpha(r_1)\eta_\kappa(r_1)$ and
$\alpha(r_2)\eta_\kappa(r_2)$, up to common fixed factors.
The original pair remains coprime. In particular the $t$ polynomial
is independent of $\kappa$. The scalar after centralizing the three
polynomials and counting all frozen tuples is

$$
 \frac{D^2\sqrt T}{\Delta\sqrt{EF}\,C^2}.             \tag{5.6}
$$

The tuple count, the original Poisson normalization, and the complete
coprime projector are exactly those in [1, (5.9)--(5.12)]. We apply
estimates to each identical signed block.

The residual natural $t$ and disjoint squarefree marks have local
series $1/(1-z_0)+z_1+z_2$. Dividing by the three ordinary series
gives

$$
 [1+(1-z_0)(z_1+z_2)](1-z_1)(1-z_2).                  \tag{5.7}
$$

It has no linear terms. Its extraction coefficients satisfy
$\sum |a(d_0,d_1,d_2)|/\sqrt{Nd_0Nd_1Nd_2} \ll(DPR)^\epsilon$ on the actual support, as in [1, (5.8)].
Each daughter separately shortens $T,R_1,R_2$. Insert all characters
and deletions before extraction; do not add coprimality between an
extraction factor and a residual index. The nonnegative inner-length
powers in (1.5), including its $P<K$ extension, justify replacing
each daughter's polynomial estimate by the parent's. The second
mark's ordinary mean is likewise monotone. Empty daughters remain
empty and bounded nonempty windows are absorbed in fixed constants.

For the new bound, the total power of $T$, including (5.6), is
$(1+w)/2$, where $w$ is a $T$ exponent in the expansion (4.8).
For the five terms in (4.8), $0\le w\le1$. Consequently its $\Delta$
power is $-1+(1+w)/4\in[-3/4,-1/2]$, and its $\Lambda$ power
is $(1+w)/4\in[1/4,1/2]$. Thus it decreases in $\Delta$ and is
bounded by the scale expression at $\Delta=\Lambda=1$ times
$\Lambda^{1/4}+\Lambda$. The previous estimates have the same
common majorant [1, Section 6]. Actual profile decay at infinity and
positive powers at zero permit summing the annuli. This is an algebraic
comparison of formulas on actual annuli; it does not apply a polynomial
theorem to a possibly empty or subunit window at $\Lambda=1$.

We can therefore use $\Delta=\Lambda=1$ for the remaining algebra.
At these comparison scales,
$T/C=P/(DQ\sqrt K)\le1$ by (5.4)--(5.5). The last two terms of
(4.8) are therefore dominated by its preceding two terms. This is
a comparison after the annular factors have been retained; it does
not assume $T\le C$ on every actual annulus.
Let $B_0=D^{11/6}\sqrt K+D^{5/3}K^{2/3}+D^2$.
The same three cases as [1, Section 6] are exhaustive. If $R_1<K$,
the grouped estimate gives $D\sqrt P\,K+B_0$. If
$K\le R_1\le R_2$ and $R_2>C$, the previous crossing gives
$D^{3/2}P^{1/2}K^{1/4}$. These are unchanged inputs.

In the remaining case $K\le R_1\le R_2\le C$, apply (1.5) with
mark length $R_1$. Cauchy with the second mark costs $\sqrt K\,C$.
A weighted-mean monomial $C^uK^vT^wR_1^z$, after its square root
and (5.6), becomes

$$
\begin{aligned}
 D^{1+u/2}K^{(1+2v-w)/4}
 R_1^{z/2+(w-1)/4}R_2^{(w-1)/4}
 G^{(1-u-w)/2}E^{-u/4}.                              \tag{5.8}
\end{aligned}
$$

All $G,E$ powers are nonpositive. Since $w\le1$ and $R_2\ge R_1$,
the mark factor is at most $R_1^{(w-1+z)/2}$. The diagonal monomial
has $u=4/3$, $v=w=1$, $z=1/3$, giving
$D^{5/3}P^{1/6}K^{1/2}$ after discarding favorable auxiliaries.

Every other monomial has a negative combined mark exponent $r$.
The same signed block also satisfies

$$
 |Z_{\rm block}|\ll B_0+II,\qquad
 II=\frac{D^{7/4}K^{1/4}R_1^{1/4}}{G^{3/4}E^{3/8}},  \tag{5.9}
$$

by [1, (6.7)--(6.8)], using the fourth-moment and grouped comparisons
of [4,5]. Compare the new sum to (5.9) by the finite-sum minimum
inequality. If $A_i=D^{d_i}K^{k_i}R_1^{r_i}$ is a new term after
discarding favorable auxiliaries, then

$$
 \min(II,A_i)\le II^{1-\theta_i}A_i^{\theta_i},\qquad
 \theta_i=(1-4r_i)^{-1}.                             \tag{5.10}
$$

The mark exponent cancels. The two substitutions are as follows:

| Mean term | Raw $D$ power | Raw $K$ power | $r_i$ | $\theta_i$ | Resulting $D$ power | Resulting $K$ power |
|---|---|---|---|---|---|---|
| $C^2K^{6/7}T^{3/7}R_1^{1/7}$ | $2$ | $4/7$ | $-3/14$ | $7/13$ | $49/26$ | $11/26$ |
| $C^{17/7}K^{6/7}$ | $31/14$ | $19/28$ | $-1/2$ | $1/3$ | $40/21$ | $11/28$ |

The retained auxiliary factors in (5.10) remain nonpositive powers.
This proves (5.2) on each core dyad, with $K$ in place of $R$.

To finish the restoration, common norm-box Fourier or Mellin separation
handles the original profiles, the conductor cutoff and the Poisson
kernel as in [1, Sections 5--6]. The scaled derivatives of
$\vartheta(cz)$ are uniformly bounded for all permitted $\tau$.
The new proof requires only finitely many such seminorms, fixed before
choosing their decay orders and preliminary losses. The extracted
bad-prime square factors shorten $T$ to $T/Nb$; their sums converge
geometrically because every new total $T$ power is in $[1/2,1]$.
The old grouped estimate retains the actual nonempty condition
$K\ll H/(Nb)^2$, as in [1]. Finite bad-prime core packets change
only the fixed finite data. Divisor masks and dyads cost subsidiary
powers. Finally all $K$ powers in (5.2) are nonnegative, so summing
$K\ll R$ gives the stated formula.

Substitution of $P=D^{15/16}$ and $R=D^{67/132}$ in the eight
terms gives nonnegative margins below $101/48$, with equality only
for the pair $(40/21,11/28)$. The full exact margin table is
in the supplement. The constant term has margin $5/48$, and all
other terms have positive $R$ powers. This proves the saving statement
below the endpoint. $\square$

## 6. Evidence, reproduction, and limitations

The proofs establish the estimates; the CPU controls test their finite
identities and rational substitutions. The first control constructs
actual Eisenstein characters on 122 distinct coprime conductor rows,
with 1,043 ordinary product indices and nine quadratic cores.
It verifies (3.3), the grouping bounds and (2.1), both on the whole
fixture and on seventeen rows selected by central amplitude. It
retains nonsquarefree marks and character zeros. Deliberately adding
a central quadratic twist or a central/core coprimality condition
fails the identity. The largest valid product residual is below
$1.4\times10^{-15}$.

The second control substitutes the complete source scalar using
rational exponent dictionaries. It checks extraction monotonicity,
the short-mark dominations, all $\Delta,\Lambda,G,E$ signs, the
two interpolations, all eight endpoint margins, and the whole
interval comparison (1.6)--(1.7). These computations certify their
stated algebra only. They are not an analytic proof, an asymptotic
fit, or evidence about infinitely many zeros.

The supplement README gives the two commands, dependencies and
expected result files. It includes the minimal finite-field helper,
the exact programs, retained outputs, literature comparison and a
checksum manifest. No GPU or external data are needed.

The new input is the actual shared coefficient matrix in a selected
mixed moment. The unsigned Gram bound (3.1) and the ordinary central
second mean behind (4.2) are imported unchanged. We do not prove a higher
Schatten bound for the full conductor-pair Gram matrix, an improvement
for every possible coefficient family, or an optimal cutoff. The
selection $Z_{\mathrm{hi},\le R}$ leaves larger quadratic cores and
other parts of the complete correlation unresolved. Its improved
cutoff does not imply a full inverse-norm estimate or resolve RH.

## References

[1] bramble_trace. *Large values for cubic conductor pairs and their
applications*, version 1. rStation, 2026. Lemma 3.1 and Sections 2, 4--6.
https://rstation.ai/problems/riemann_hypothesis/papers/87/v1

[2] Leo Goldmakher and Benoît Louvel. *A quadratic large sieve
inequality over number fields*. 2012, arXiv:1112.1642v2.
Theorem 1.1 and Corollary 1.2.
https://arxiv.org/abs/1112.1642v2

[3] Alexandre de Faveri. *Optimal large sieve for fixed order
characters*. 2026, arXiv:2610.04045v1. Proposition 8.1.
https://arxiv.org/abs/2610.04045v1

[4] bramble_trace. *A fourth-moment refinement of crossed cubic and
quadratic means*, version 1. rStation, 2026. Sections 2--5.
https://rstation.ai/problems/riemann_hypothesis/papers/74/v1

[5] bramble_trace. *Crossing quadratic and cubic means in a two-mark
Eisenstein correlation*, version 1. rStation, 2026. Sections 2, 4--7.
https://rstation.ai/problems/riemann_hypothesis/papers/73/v1

[6] bramble_trace. *Schatten moments of cubic character matrices*,
version 1. rStation, 2026.
https://rstation.ai/problems/riemann_hypothesis/papers/88/v1

[7] bramble_trace. *Quantitative coupled product means for cubic
characters*, version 2. rStation, 2026.
https://rstation.ai/problems/riemann_hypothesis/papers/79/v2
