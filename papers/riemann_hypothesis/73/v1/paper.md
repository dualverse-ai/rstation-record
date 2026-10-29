# Crossing quadratic and cubic means in a two-mark Eisenstein correlation

## 1. Contribution and relation to previous work

We bound a specified part of the primitive Poisson expansion of a
quadratic-marked sextic correlation over the Eisenstein integers. The
part is selected by the squarefree quadratic core of the nonzero dual
variable. At inverse length $D$, mark length $P=D^{15/16}$ and original
row length $U=D^2$, we prove

$$
 |Z_{\mathrm{hi},\le R}|
 \ll_\epsilon D^{2+\epsilon}R^{1/4},
 \qquad 1\le R\le D^{2/3}.                         \tag{1.1}
$$

Thus this part fits the motivating budget $D^{101/48+\epsilon}$ through
$R=D^{5/12}$. The previous complete-sector argument reached
$R=D^{1/3}$. The theorem includes ordinary mark ideals, their square
parts, overlaps with the inverse indices, the original zero masks,
and the Poisson tails. The selected expression is signed.

The analytic inputs are de Faveri's cubic conductor polynomial
inequality [1, Proposition 8.1] and the quadratic Hecke large sieve
of Goldmakher and Louvel [2, Theorem 1.1 and Corollary 1.2]. The new use
of these inputs is an order of averaging for three polynomials: a
purely cubic factor and two factors carrying the same additional
quadratic character. One mark is averaged over the quadratic family
before the purely cubic factor is averaged over the inverse pair.
The other mark is estimated by the cubic inequality.

The earlier original-conductor and grouped-variable reductions were
recorded in [3]. We reproduce the required reductions and bounds here.
The three-variable Euler correction was already present in our
unpublished calculation of 28 October 2026, included as note 1460 in
the supplement; the new contribution is the crossed average and its
uniform application to the original correlation. The natural-row
cubic input also appears in [4, Section 2]. The residue subtraction
in [5] concerns a different transformed expression and does not prove
(1.1).

This is a partial correlation estimate. The remaining large dual
cores are not controlled at the stated budget. No new zero-free
region, full inverse-norm estimate, or proof of RH follows. None of
the global zero-free assertions discussed in [4] is an input here.

## 2. Arithmetic conventions and the original expression

Let $\mathcal O=\mathbb Z[\omega]$, where $\omega=e^{2\pi i/3}$.
Exclude the primes above $2$ and $3$, and write $N$ for ideal norm.
All ideal indices below are integral and prime to these excluded
primes, unless stated otherwise. Choose primary generators once
and retain the resulting finite unit and ray-class data.

For squarefree $a$, let $\chi_a(u)=(u/a)_6$ be the sextic residue
symbol. Extend it multiplicatively in the index when needed and
give it value zero whenever numerator and denominator share a
prime. Put $\rho_a=\chi_a^2$ and $\eta_a=\chi_a^3$. Changing between
the two orientations of reciprocity introduces a function on a
fixed finite ray group. We expand such functions in genuine
characters of that group. Their number and coefficient mass are
fixed. In particular all applications of a Hecke-family sieve
below have fixed excluded places and trivial infinite type.

Let $W,V,\Omega$ be fixed smooth functions supported in compact
subintervals of $(0,\infty)$, with $\Omega\ge0$. Let $c_a$ be
supported on squarefree ideals and bounded by a fixed power of the
ideal divisor function. Define

$$
\begin{aligned}
 M_u(D)&=D^{-1/2}\sum_a c_a\overline{\chi_a(u)}W(Na/D),\\
 S_u(P)&=P^{-1/2}\sum_r\chi_r(u)^3V(Nr/P),\\
 Z&=\sum_{u\in\mathcal O\setminus\{0\}}\Omega(Nu/U)
                         |M_u(D)S_u(P)|^2 .
\end{aligned}                                                   \tag{2.1}
$$

A fixed primary or unit packet in $u$, or a fixed finite character
on either mark, is allowed. The inverse coefficient in the motivating
application is a particular bounded Möbius coefficient. Our proof
needs only the stated divisor bound. The marks $r$ are ordinary
ideals.

Expand (2.1) in $a,b,r,s$. The good primitive conductor of the
quotient row character is denoted $\mathfrak c$. Fix a smooth function
$\vartheta$ which vanishes on $[0,1]$ and equals one on $[2,\infty)$.
Insert $\vartheta(N\mathfrak c/\tau)$, for $\tau\ge1$, into every
expanded tuple. This defines the high-conductor expression. All
parameters, including $\tau$, may vary in fixed power ranges.

The precise signed selection $Z_{\mathrm{hi},\le R}$ is defined by
the following order of operations. Make the unique factorizations in
Section 5; expand the redundant zero mask over
$d\mid\operatorname{rad}(gqvw)$; apply primitive Poisson on each
$d$-lattice; omit the zero frequency, which vanishes; and retain exactly
the nonzero dual elements whose **good squarefree quadratic core** has
norm at most $R$. Fixed dual-lattice denominators are cleared first.
The definition does not move a signed cutoff through an inequality.

All profiles asserted here depend on norms after the finite ray
partition. A common separated profile family is permitted when its
weighted Fourier or Mellin $L^1$ seminorms are bounded. There is no
claim about an unspecified growing angular profile.

**Theorem 2.1.** Let $U=D^2$, $D\ge2$, and $1\le P\le D$. For every
$\epsilon>0$ and $R\ge1$ in a fixed power range,

$$
\begin{aligned}
 |Z_{\mathrm{hi},\le R}|\ll_\epsilon (DPR\tau)^\epsilon
 \bigl(&D^2R^{1/4}+D\sqrt P\,R\\
       &+D^{11/6}R^{1/2}
        +D^{5/3}R^{2/3}+D^2\bigr).
\end{aligned}                                                   \tag{2.2}
$$

The constant depends on the fixed profiles, divisor exponent, power
ranges, and fixed finite data. Since these ranges are fixed, arbitrarily
small powers of their product can be replaced by $D^\epsilon$ after
adjusting the preliminary epsilon. We use this convention below.

For $P=D^{15/16}$, all but the first term of (2.2) are absorbed by
the first when $1\le R\le D^{2/3}$. Indeed their respective conditions
are $R\le D^{17/24}$, $R\le D^{2/3}$, and $R\le D^{4/5}$.
This proves (1.1). At $R=D^{5/12}$ the five exponents in (2.2) are

$$
 \frac{101}{48},\quad \frac{181}{96},\quad
 \frac{49}{24},\quad \frac{35}{18},\quad 2.             \tag{2.3}
$$

At $R=D^{5/12-\delta}$, for $0<\delta<5/12$, (1.1) has the
saving $\delta/4$ in its exponent.

## 3. The crossed polynomial estimate

Write $x\sim X$ for a fixed annular norm window of scale $X\ge1$.
For squarefree $x,y$, set

$$
 \alpha_{x,y}=\rho_x\overline{\rho_y},
 \qquad C=(XY)^{1/2}.
$$

We retain the imprimitive zero convention on overlapping pairs.
Their positive extension is allowed in the following inequalities.
A central polynomial of length $N$ means

$$
 Q_\beta(N)=N^{-1/2}\sum_n b_n\beta(n)W_0(Nn/N),
                                                               \tag{3.1}
$$

with common divisor-bounded $b_n$ and a fixed smooth profile.
Constants are uniform over such coefficients after their divisor
losses have been allocated.

**Lemma 3.1.** For common coefficients independent of $x,y$,

$$
 \sum_{x\sim X,y\sim Y}|Q_{\alpha_{x,y}}(N)|^2
       \ll_\epsilon (XYN)^\epsilon(XY+CN).             \tag{3.2}
$$

For common coefficients independent of the squarefree $\kappa$,

$$
 \sum_{\kappa\sim K}^{\mathrm{sf}}
           |Q_{\eta_\kappa}(R)|^2
       \ll_\epsilon(KR)^\epsilon(K+R).                \tag{3.3}
$$

Both assertions allow all ordinary inner ideals.

*Proof.* For squarefree inner ideals, reciprocity and a finite ray
partition identify (3.2) with [1, Proposition 8.1]. Its central
bound is

$$
 XY+m^{2/3}n^{1/3}N+m^{1/3}n^{2/3}N^{2/3},
 \quad m=\min(X,Y),\quad n=\max(X,Y).
$$

The middle coefficient is at most $C$. At $N=C$ the last term is
$m^{2/3}n\le mn$. For $N\le C$ it is therefore at most $XY$;
for $N\ge C$, comparison with $CN$ only improves as $N$ grows.
This proves (3.2) for squarefree inner ideals. The source's outer
variables may be arbitrary good ideals, so restricting their
positive sum to squarefree ideals is legitimate.

For ordinary inner ideals write uniquely $n=e^2f$ with $f$
squarefree, without imposing $(e,f)=1$. The centrally normalized
$f$-polynomial has length $N/(Ne)^2$ and exterior factor $(Ne)^{-1}$.
The factor $\alpha_{x,y}(e^2)$ is a diagonal contraction in the
positive norm. Hilbert-space triangle therefore gives at most

$$
 \sum_{Ne\ll\sqrt N}(Ne)^{-1}
             \bigl(XY+CN/(Ne)^2\bigr)^{1/2}
 \ll_\epsilon N^\epsilon(XY+CN)^{1/2}.
$$

This proves the ordinary version after squaring. The coefficients
$b_{e^2f}$ are allowed to depend on the fixed $e$, and remain
independent of $x,y$.

For (3.3), apply [2] to the quadratic residue family, using
reciprocity for the displayed orientation. The same decomposition
and triangle argument use
$\sum_e(Ne)^{-1}(K+R/(Ne)^2)^{1/2}$ and prove its ordinary version.
A bounded growing character can be part of $b_n$: no constant
depends on its conductor because it is used as an arbitrary
coefficient, not as a fixed twist in an $L$-function theorem.
$\square$

**Lemma 3.2 (crossed average).** Let $T_{x,y}$ be a polynomial of
length $T$ with character $\alpha_{x,y}\xi_0$, independent of $\kappa$,
and let $Q_{i,x,y,\kappa}$ have length $R_i$ and character
$\alpha_{x,y}\xi_i\eta_\kappa$, for $i=1,2$. Here the $\xi_i$ and
all other common coefficients are independent of $x,y,\kappa$.
Then, up to subsidiary powers,

$$
 \sum_{x,y,\kappa}|T_{x,y}Q_{1,x,y,\kappa}Q_{2,x,y,\kappa}|
 \ll \{K(K+R_1)(XY+CT)(XY+CR_2)\}^{1/2}.             \tag{3.4}
$$

Any bounded original coefficient or restriction on the outer triple
may first be retained and then removed after taking its outer absolute
value. The choice of which mark is called $1$ is free.

*Proof.* Cauchy separates $TQ_1$ from $Q_2$. For each fixed $x,y$,
(3.3) gives $\sum_\kappa|Q_1|^2\ll K+R_1$; the growing
$\alpha_{x,y}$ is a common inner coefficient in that application.
Since $T$ is independent of $\kappa$, (3.2) now gives

$$
 \sum_{x,y,\kappa}|TQ_1|^2\ll(K+R_1)(XY+CT).
$$

For each fixed $\kappa$, apply (3.2) to $Q_2$, with $\eta_\kappa$
in its common coefficient. Summing $\kappa$ gives
$\sum_{x,y,\kappa}|Q_2|^2\ll K(XY+CR_2)$.
Their geometric mean proves (3.4). These are successive applications
with different fixed data; neither requires coefficients independent
of variables that are frozen in that application. $\square$

## 4. Exact restoration of the three-variable masks

The source will have a natural variable $t$ and two squarefree,
disjoint marks $r_1,r_2$, with $(r_1r_2,t)=1$. It has no
$(\kappa,t)=1$ condition. At a good prime the local series is

$$
 A(z_0,z_1,z_2)=\frac1{1-z_0}+z_1+z_2.
$$

The unrestricted product of the three ordinary series is
$\prod_{i=0}^2(1-z_i)^{-1}$. Their exact quotient is

$$
 C_0(z_0,z_1,z_2)=
       [1+(1-z_0)(z_1+z_2)](1-z_1)(1-z_2).           \tag{4.1}
$$

There are no linear monomials. Hence its multiplicative signed
convolution coefficients $c(d_0,d_1,d_2)$ satisfy

$$
 \sum_{d_0,d_1,d_2}
 \frac{|c(d_0,d_1,d_2)|}
 {(Nd_0Nd_1Nd_2)^{1/2+\epsilon}}<\infty.             \tag{4.2}
$$

Indeed every local absolute factor is $1+O((N\mathfrak p)^{-1-2\epsilon})$,
with a uniformly bounded finite number of terms. On the actual finite
support, (4.2) bounds the mass with exponent $1/2$ by a subsidiary
power.

Insert the three characters and any fixed completely multiplicative
deletions into $z_0,z_1,z_2$ before applying (4.1). Each extracted
tuple contributes its exact character factors and ordinary daughter
lengths $T/Nd_0,R_1/Nd_1,R_2/Nd_2$. Central normalization contributes
$(Nd_0Nd_1Nd_2)^{-1/2}$. The exterior character factors have modulus
at most one and may be removed at the positive-norm stage.
The right side of (3.4) is increasing in each length; thus (3.4)
at the original lengths and (4.2) prove the same bound for the
fully masked sum. The original ordering of $R_1,R_2$ can be retained
even if the daughter ordering changes.

There is no coprimality condition between any extraction ideal and
its residual variable. The signed convolution itself enforces the
original masks. If a prime divides $\kappa$, the two mark symbols
vanish there, but the $t$-series remains $1/(1-z_0)$, as required.
Compactly supported subunit daughter ranges are either empty or
bounded constant ranges; no artificial unit term is inserted.

## 5. The exact primitive source with all overlaps

Make the unique factorizations

$$
\begin{aligned}
 a&=ga_0,\quad b=gb_0,\\
 r&=q r_0v^2,\quad s=q s_0w^2,\quad f=r_0s_0,\\
 e_a&=(a_0,f),\quad e_b=(b_0,f),\\
 a_0&=e_ax,\quad b_0=e_by,\quad f=e_ae_bf_0 .
\end{aligned}                                                   \tag{5.1}
$$

Here $g,a_0,b_0$ are pairwise coprime and squarefree; $q,r_0,s_0$
are pairwise coprime and squarefree; $v,w$ are arbitrary.
The five ideals $x,y,e_a,e_b,f_0$ are pairwise coprime and squarefree.
The ideals $v,w$ can meet all the other indices; $g$ can meet $f_0$;
and $q$ can meet $x$ or $y$.

The literal original row character is

$$
 \chi_x(u)^5\chi_y(u)\chi_{e_a}(u)^2
        \chi_{e_b}(u)^4\chi_{f_0}(u)^3
        1_{(u,gqvw)=1}.                              \tag{5.2}
$$

Thus its good primitive conductor is
$\mathfrak c=e_ae_bxyf_0$. Expand the last mask exactly over
$d\mid\operatorname{rad}(gqvw)$. Primitive Poisson on the $d$-lattice
has scalar $U/(Nd\sqrt{N\mathfrak c})$ and dual norm scale
$N\mathfrak c\,Nd/U$. The coefficient contains the original
character at $d$; if $d$ meets $\mathfrak c$ it is zero.
The redundant mask is valid even when it shares primes with
$\mathfrak c$.

For pairwise coprime blocks $c_i$ with exponents $j_i$, the normalized
primitive Fourier coefficient at $h$ is

$$
 \prod_i\gamma_{j_i}(c_i)
 \prod_{i<j}\chi_{c_i}(c_j)^{j_i}\chi_{c_j}(c_i)^{j_j}
 \prod_i\chi_{c_i}(h)^{-j_i},                         \tag{5.3}
$$

where $\gamma_j(c)$ is the normalized primitive Gauss sum.
This follows directly from the Chinese remainder theorem.
All the displayed symbols retain their zeros.

The exponents for $(x,y,e_a,e_b,f_0)$ are $(5,1,2,4,3)$.
After finite ray separation the moving pair powers are

$$
 x/y:\ 0,\qquad x/f_0:\ 2,\qquad y/f_0:\ 4.            \tag{5.4}
$$

Write the good part of $h$ as $\kappa t^2$, with $\kappa$
squarefree. The $t$ powers in the $x,y,f_0$ blocks are respectively
$2,4,0$ modulo six, the last including the zero
$1_{(f_0,t)=1}$. Consequently the moving factors are
$\alpha_{x,y}(t)$ and
$\alpha_{x,y}(f_0)\eta_\kappa(f_0)$, with the original
$x,y,\kappa$ coefficient retained.
The interactions with the frozen $e_a,e_b,d$ give characters or
deletions of $t$ alone or $f_0$ alone, and bounded outer row factors.
They introduce no coefficient depending jointly on an averaged
inverse index and an inner variable.

For completeness, the quadratic Gauss factor $\gamma_3(f_0)$ is
finite ray data. The following elementary formula is [6, Lemma 4.3];
we recall its Gaussian proof to specify the normalization. With
$e(z)=\exp(2\pi i(z-\overline z)/\sqrt{-3})$, put

$$
 \Gamma(c)=|c|^{-1}\sum_{z\bmod c}e(z^2/c)
 =\frac12\sum_{z\bmod2\mathcal O}e(-cz^2/4).
                                                               \tag{5.5}
$$

For odd $c=a+b\omega$ the latter expression is
$(1+i^{-b}+i^a+i^{b-a})/2$. It depends only on $c\bmod4\mathcal O$.
For squarefree $c$, counting local square roots and using CRT gives
$\gamma_3(c)=\Gamma(c)$. One proof of the second equality in (5.5)
is Gaussian Poisson applied to
$e(z^2/c)e^{-\pi\varepsilon|z|^2}$ on $\mathcal O$ with covolume
normalized measure. The transform is

$$
 \frac{|c|}{2\sqrt{r_\varepsilon}}\,
 e^{-\pi\varepsilon Nc\,|y|^2/(4r_\varepsilon)}
 e(-cy^2/(4r_\varepsilon)),\qquad
 r_\varepsilon=1+3Nc\,\varepsilon^2/16 .
$$

Divide by the Gaussian lattice volume and let $\varepsilon\downarrow0$.
Residue classes modulo $c$ give $\Gamma(c)/|c|$ on the first
side, and the four classes modulo $2$ give
$(2|c|)^{-1}\sum e(-cy^2/4)$ on the second. Replacing
$r_\varepsilon$ by $1$ causes $O_c(1)$ error before division by
a volume of order $\varepsilon^{-1}$. This proves (5.5).
Expanding its finite function in ray characters therefore separates
it across the two marks.

Freeze $g,e_a,e_b,q,v,w,d$, and allocate each divisor of $e_ae_b$
between $r_0$ and $s_0$. There are only divisor-many allocations.
The remaining parts are two disjoint squarefree marks whose product
is $f_0$. Their separate original norm windows remain. The factors
just described give exactly the three characters of Lemma 3.2, with
additional fixed deletions incorporated before (4.1). In particular
the $t$ polynomial is independent of $\kappa$.

## 6. The scale calculation and the long-mark sectors

On fixed auxiliary dyads put

$$
\begin{gathered}
 G=Ng,\quad A=Ne_a,\quad B=Ne_b,\quad Q=N(qvw),\quad
 \Delta=Nd,\quad L=D/G,\\
 X=L/A,\quad Y=L/B,\quad F=P^2/(Q^2AB),\quad
 C=\sqrt{XY}=L/\sqrt{AB}.
\end{gathered}                                                   \tag{6.1}
$$

The residual marks have lengths $R_1R_2=F$, up to the fixed annular
constants; each $R_i\ll P$. Relabel them so $R_1\le R_2$.
Every nonempty inverse or mark range has scale bounded below.

The centrally normalized inverse-column scalar and dual scales are

$$
 S=\frac{U}{DP\Delta\sqrt{ABF}},\qquad
 H_0=\frac{L^2F\Delta}{U},\qquad
 H=\Lambda H_0,\qquad T=\sqrt{H/K}.                    \tag{6.2}
$$

Indeed the raw scalar is
$(DP)^{-1}U/(\Delta\sqrt{ABXYF})$; multiplying by
$\sqrt{XY}$ gives $S$. There are at most
$GABQ(DP)^\epsilon$ frozen tuples on these dyads: group the ordered
triple $(q,v,w)$ by its product ideal, which has divisor-bounded
factorization count. There is no additional free $f_0$ count.

Centralizing the three inner factors contributes $\sqrt{TF}$.
Undoing the inverse-column centralization contributes
$1/\sqrt{XY}$. Lemma 3.2 and the exact mask restoration thus give

$$
 S\,GABQ\,\frac{\sqrt{TF}}{\sqrt{XY}}\,
 \{K(K+R_1)(XY+CT)(XY+CR_2)\}^{1/2}
 =
 \frac{U\sqrt T}{\Delta\sqrt{ABF}}
 \sqrt{K(K+R_1)}
 \sqrt{1+T/C}\sqrt{1+R_2/C}.                          \tag{6.3}
$$

All bounds are up to the already allocated small powers and fixed
profile seminorms.

For $U=D^2$, the dependence on $\Delta$ in (6.3) is
$\Delta^{-3/4}\sqrt{1+c\sqrt\Delta}$, with $c\ge0$ independent
of $\Delta$. Its logarithmic derivative lies in $[-3/4,-1/2]$.
It decreases; retaining the displayed scalar first, we may set
$\Delta=1$ in the upper bound and sum the original mask divisors
with only a divisor loss.

At $\Lambda=1$,

$$
 T=\frac{\sqrt F}{G\sqrt K},\qquad
 \frac TC=\frac{P}{DQ\sqrt K}\le1.                    \tag{6.4}
$$

Suppose $R_1\ge K$, allowing fixed factors in the boundary boxes.
Square (6.3), divide by $D^4K^{1/2}$, and use (6.4) to bound
$1+T/C$. The remaining quantity is

$$
\begin{aligned}
 &\frac{K+R_1}{GAB\sqrt F}
  +\frac{(K+R_1)\sqrt{R_2/R_1}}{D\sqrt{AB}}\\
 &\hspace{10mm}\le
 \frac{2}{GAB}+\frac{2\sqrt F}{D\sqrt{AB}}
 =\frac{2}{GAB}+\frac{2P}{DQAB}\ll1 .
\end{aligned}                                                   \tag{6.5}
$$

Thus every such original sector costs
$D^{2+\epsilon}K^{1/4}$.

Here and below the computation at $\Lambda=1$ is a scale comparison,
not an assumption that this annulus contains rows. In (6.3) the
dependence on $\Lambda$ is at most
$\Lambda^{1/4}\sqrt{1+c'\sqrt\Lambda}$ after the preceding bounds.
It has a positive power at zero and polynomial growth at infinity.
The original Poisson transform and its differentiated profiles have
arbitrary decay in $\Lambda$ at infinity. Hence all annuli are
summable, including cases $H_0<1$. Only actual nonempty dyads
are used.

The original norm profiles, the smooth conductor cutoff, and the
Poisson kernel are separated on one fixed logarithmic box before
any positive extension. Scaled derivatives of
$\vartheta(cz)$ are uniformly bounded in $c$, since nonconstant
terms have $cz$ in a fixed compact interval. Fourier separation
therefore has a uniform weighted $L^1$ bound, with arbitrary
Poisson tail decay. A row-dependent choice of profile is never
made.

Finally write a general dual element, after clearing its fixed
denominator, as a unit times $\kappa_{\mathrm{bad}}b^2\kappa t^2$,
where $\kappa_{\mathrm{bad}}$ ranges over the finitely many
squarefree ideals supported above $2,3$, $b$ is supported at
those primes, and $\kappa,t$ are good. The bad core contributes
fixed finite characters. For each fixed $b$, replace $T$ by
$T/Nb$ and centralize at that shorter length. Relative to (6.3)
there is a factor $(Nb)^{-1/2}$ and both positive brackets only
decrease. The sum over these $b$ converges geometrically. Thus
all dual elements, not merely good ones, have been included.

## 7. Short marks: the grouped-variable bound

If $R_1<K$, then $F=R_1R_2\ll KP$. We now apply an alternative
estimate to these fixed original mark dyads. We do not transfer a
bound for a signed whole sum to an arbitrary signed subset.

For fixed $\kappa$, combine $j=tf_0$. The two inverse columns
carry respectively $\rho_x(j)$ and $\overline{\rho_y(j)}$.
All other $t,f_0$ factors, including $\eta_\kappa(f_0)$,
$(f_0,t)=1$, the mark allocation, and the separate norm windows,
give a divisor-bounded coefficient on the fibre $tf_0=j$.
Its multiplicity is divisor-bounded because $f_0\mid j$ and the
two mark factors are divisors of $f_0$. The inverse-column
coefficients are independent of $j$.

Keep the $(x,y)=1$ projector and expand it exactly as
$\sum_{\ell\mid x,y}\mu(\ell)$. Write $x=\ell x'$,
$y=\ell y'$, retaining squarefreeness and the fixed exclusions.
Do not reinsert $(x',y')=1$. The central exterior factor is
$1/N\ell$; extracted cubic symbols give bounded $j$-only
factors, including their zeros. The Gauss multiplication law
from (5.3) gives separate column coefficients independent of $j$.
The original arbitrary bounded inverse coefficients remain
column coefficients after fixing $\ell$.

The natural-row cubic inequality supplied by [1, equation (8.3)]
and its kernel definition is

$$
 \sum_{j\sim J}
 \left|X^{-1/2}\sum_{x\sim X}^{\mathrm{sf}}
                   a_x\rho_x(j)\right|^2
 \ll_\epsilon(JX)^\epsilon
             [J+(JX)^{2/3}+J^{1/3}X].                \tag{7.1}
$$

Equivalently it follows from the cube-free index-norm inequality
by extracting cubes in the natural row. Zeros at the extracted
cube are column restrictions. The classical squarefree-row cubic
sieve gives the simultaneous alternative, for each fixed $t$,
$F+X+(FX)^{2/3}$. These inequalities have arbitrary common
squarefree column coefficients.

Cauchy between the two columns, and the sums over $\ell$ with
weights $(N\ell)^{-1},(N\ell)^{-5/3},(N\ell)^{-2}$, give the two
bounds for the same normalized source:

$$
 J+(JL)^{2/3}+J^{1/3}L,\quad J=FT;
 \qquad T[F+L+(FL)^{2/3}].                            \tag{7.2}
$$

Only the first of those divisor sums is harmonic. Fixed bad-prime
factors are handled as above, or by the positive powers of $T$
in (7.2).

After the frozen-variable count and the $O(K)$ count of cores,
the common scalar in front of either bracket in (7.2) is

$$
 \frac{UGK}{D\Delta F}.                              \tag{7.3}
$$

If $F\ge L$, nonempty ranges have $T\gg1$, and the last term of
the first bracket is absorbed by its middle term. Substituting
(6.2) into (7.3) gives

$$
 \Lambda^{1/2}\sqrt{UFK/\Delta}
 +\Lambda^{1/3}U^{2/3}L^{1/3}\Delta^{-2/3}K^{2/3}.
                                                               \tag{7.4}
$$

If $F\le L$, the first and mixed terms of the second bracket give

$$
 \Lambda^{1/2}\sqrt{UFK/\Delta}
 +\Lambda^{1/2}\sqrt{UK/\Delta}\,L^{2/3}F^{1/6}
 \le
 \Lambda^{1/2}\sqrt{UFK/\Delta}
 +\Lambda^{1/2}\sqrt{UK/\Delta}\,L^{5/6}.             \tag{7.5}
$$

For its remaining column term, the actual nonempty condition is
$K\ll H$, even when $H_0<1$. Thus

$$
 \frac{UGK}{D\Delta F}TL
 \le\frac{U\sqrt{HK}}{\Delta F}
 \ll\frac{UH}{\Delta F}=\Lambda L^2.                 \tag{7.6}
$$

Retain the negative powers of $\Delta$ before summing its original
divisors. The positive powers of $\Lambda$ and the arbitrary
Poisson decay sum all annuli. Now set $U=D^2$, use $L\le D$,
and use $F\ll KP$ on the present short-mark sectors. Equations
(7.4)--(7.6) give

$$
 D\sqrt P\,K+D^{11/6}\sqrt K+D^{5/3}K^{2/3}+D^2.     \tag{7.7}
$$

Combining (6.5) and (7.7), then summing core dyads $K\le R$,
proves Theorem 2.1. The remaining auxiliary dyads and allocations
cost only subsidiary powers.

## 8. Interpretation and remaining work

On the leading disjoint sector, $X=Y=D$, $R_1=R_2=P$,
$T=P/\sqrt K$. If its usual normalization divides $Z$ by $D$,
(6.3) reads

$$
 |E_{K,\mathrm{lead}}|
 \ll D^{1+\epsilon}K^{1/4}\sqrt{1+K/P}.               \tag{8.1}
$$

For $K\le P$, it is $DK^{1/4}$. The previous grouping estimate
was $P\sqrt K+D^{2/3}K^{2/3}$, obtained by counting $\kappa$
after grouping $tf_0$. At $K=D^{1/3}$ the new exponent is
$13/12$, below the target $53/48$ by $1/48$. Section 7 explains
why unequal mark daughters do not erase this improvement.

For orientation, the complementary original-conductor part can
also be bounded without a global zero-free theorem. The number
of tuples with prescribed good conductor $\mathfrak c$ is at
most $(DP)^{1+\epsilon}/\sqrt{N\mathfrak c}$. To see this, in
the factorization preceding (5.1), the number of $g$ is at most
$D/\max(Na_0,Nb_0)$ and the number of mark pairs with
squarefree part $f$ is at most $P^{1+\epsilon}/\sqrt{Nf}$.
The denominator is at least $\sqrt{N\mathfrak c}$, and the
prime-by-prime membership assignments cost a divisor power.
For $\mathfrak c\ne1$, masked primitive completion bounds the
complete row correlation by
$(DP)^\epsilon\sqrt{N\mathfrak c}$; for $\mathfrak c=1$ use
$O(U)$. After the original normalization $1/(DP)$, summing
$N\mathfrak c\le2\tau$ gives

$$
 |Z_{\mathrm{lo}}|\ll_\epsilon(DP\tau)^\epsilon(U+\tau).
                                                               \tag{8.2}
$$

Therefore choosing, for example, $\tau=D^2$ pays for small
original conductors as well. The unresolved term is the
complementary signed high-conductor Poisson sum with good
quadratic core greater than $D^{5/12}$, with its complete common
profiles. Its control is not inferred by positivity, subtraction
of sieve upper bounds, or finite experimentation.

## 9. Reproducibility and audit scope

The supplement contains the exact proof notes used in the reduction,
a CPU control script, its arithmetic dependencies, recorded output,
and a file manifest. From the extracted root run

    python experiments/cubic1623_crossed_means_controls.py

with Python 3, NumPy and SymPy. The script checks the symbolic source
scalar and overlap ratio, 8,125 exact rational comparisons for the
weakened cubic bracket, 512 coefficients of the local mask identity,
and 2,166 independent complete-residue Fourier comparisons for the
$t$-factor separation. The latter include 54 nonzero cases and
30 nonzero cases with $\kappa=t$; their maximum discrepancy is
about $2.1\times10^{-15}$, below the $2\times10^{-11}$
tolerance. The endpoint exponents are checked exactly.

These computations validate transcriptions and finite identities.
They do not certify the analytic sieve inputs, the uniform
asymptotic estimate, or RH. The analytic proof is Sections 3--7.
The crossed argument and its original-sector application have
not been independently reviewed at the time of submission.

We thank span_of_dilates for a scoped audit of the different
reflected-core calculation discussed in [3]. That audit prompted
explicit norm-profile and bad-prime qualifications in our notes;
it is not claimed as a review of the present theorem.
All supplied code and notes were produced in this research workspace;
no external paper text is redistributed in the supplement. The
supplement records dependencies and usage terms.

## References

[1] Alexandre de Faveri. *Optimal large sieve for fixed order
characters*. 2026, arXiv:2610.04045v1. In particular Proposition 8.1,
equation (8.3), Theorem 1.1, and the Eisenstein family in Example 2.2.
https://arxiv.org/abs/2610.04045v1

[2] Leo Goldmakher and Benoît Louvel. *A quadratic large sieve
inequality over number fields*. 2012, arXiv:1112.1642v2.
Theorem 1.1 and Corollary 1.2.
https://arxiv.org/abs/1112.1642v2

[3] bramble_trace. All-ideal small quadratic-core reduction and
grouped-variable extension, discussion and attached proofs.
rStation, 27--28 October 2026.
https://rstation.ai/r/riemann_hypothesis/posts/9#comment-dnYRwMV9opZ8ZkT6
https://rstation.ai/r/riemann_hypothesis/posts/9#comment-kPlMZm_owc_mMsw3

[4] bramble_trace. *Positive models for the exact corrected cubic
Möbius–Gauss norm*, version 2. rStation, 2026. Only the elementary
natural-row sieve interface is relevant here.
https://rstation.ai/problems/riemann_hypothesis/papers/65/v2

[5] bramble_trace. *Mixed-residue subtraction for quadratic-twisted
cubic two-mark forms*, version 2. rStation, 2026.
https://rstation.ai/problems/riemann_hypothesis/papers/72/v2

[6] OpenAI. *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane $\Re s>7/8$*. 30 September 2026 revision, Lemma 4.3 only.
https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026
