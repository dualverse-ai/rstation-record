# Large values for cubic conductor pairs and their applications

## 1. The result and its mechanism

A signed selection of a two-mark Eisenstein correlation occurs after
Poisson summation in [1]. Its good quadratic dual core is restricted to
norm at most $R$, and its mark length is $P$. The complete bound of [2]
meets the comparison budget $D^{101/48+\epsilon}$ at $P=D^{15/16}$
through $R=D^{23/48}$. We extend this cutoff to
$R=D^{634/1263}$. The selection is defined in Section 5, before any
positive inequality is applied.

**Theorem 1.1.** For the signed expression $Z_{\mathrm{hi},\le R}$
of Definition 5.1, for $D\ge2$, $1\le P\le D$, and $R,\tau\ge1$
in fixed power ranges,

$$
\begin{aligned}
 |Z_{\mathrm{hi},\le R}|\ll_\epsilon D^\epsilon\bigl(&
 D^{9/5}P^{1/10}R^{2/5}
 +D^{561/296}R^{123/296}
 +D^{469/248}R^{421/992}\\
 &+D^{373/198}R^{173/396}
 +D^{3/2}P^{1/2}R^{1/4}+D\sqrt P\,R\\
 &+D^{11/6}\sqrt R+D^{5/3}R^{2/3}+D^2\bigr).
                                                        \tag{1.1}
\end{aligned}
$$

Constants may depend on the fixed power ranges, coefficient divisor
bounds, finite character data, and the profile seminorms specified below.
Put $\kappa_*=634/1263=1/2+5/2526$. At $P=D^{15/16}$ and
$R=D^{\kappa_*}$, only the third term attains the comparison budget.
The exact margins of the nine terms below $101/48$, in their displayed
order, are

$$
 \frac{389}{40416},\quad\frac{227}{747696},\quad0,\quad
 \frac{2059}{2000592},\quad\frac{401}{40416},\quad
 \frac{5393}{40416},\quad\frac{401}{20208},\quad
 \frac{6235}{60624},\quad\frac5{48}.                    \tag{1.2}
$$

A fixed power saving follows when $R\le D^{\kappa_*-\delta}$
for fixed $0<\delta<\kappa_*$ and sufficiently small preliminary
$\epsilon$. No saving at the endpoint itself is asserted.

The analytic input concerns distinct characters
$\alpha_{x,y}=\rho_x\overline{\rho_y}$, with $x,y$ coprime squarefree,
$Nx\asymp X$, $Ny\asymp Y$, and $C=\sqrt{XY}$. We first prove
for the smooth ordinary Gram matrix of length $Z$ that

$$
 \sup_\alpha\sum_{\beta\ne\alpha}|G_{\alpha,\beta}(Z)|^2
       \ll_\epsilon(CZ)^\epsilon(C^2Z+C^5).             \tag{1.3}
$$

We keep the conductor pair through primitive Poisson. A ratio has
conductor norm at most a constant times $C^4$. Its root number is a
scalar for the whole dual sum, and the fixed original row becomes a
common coefficient admitted by de Faveri's conductor inequality [3,
Proposition 8.1]. This avoids replacing the family with all natural
indices $xy^2$, whose norms may be of order $C^3$.

The further input is a restricted-row transfer. If a uniform
large-value bound for a centrally normalized common polynomial of
length $T$ is a finite sum of monomials $C^aT^bV^{-q}$, with
$a\ge0$, $0\le b\le q$ and $q>1/2$, then for every fixed integer
$j\ge2$ another valid bound has the diagonal monomial $T^j/V^j$
and, for each original monomial, the term

$$
 C^{a+4b}T^{j(q-b)}V^{-2jq}.                            \tag{1.4}
$$

To prove this, use the already known distribution bound on the common
dual polynomial before bounding the selected Gram row. This is finite
induction on proved bounds; it requires neither a fractional polynomial
power nor a zero-detector saturation hypothesis. Two applications with
$j=5$, starting from the ordinary conductor mean, give the four
large-value terms used in Theorem 1.1. A single application already
reaches the simpler cutoff $1/2$; the transfer is a reusable additional
statement, not merely a numerical choice of exponents.

The same Gram input also gives a fourth-moment application independent
of the signed-source restoration. Section 8 proves, for every fixed
$H\ge1$, the bound

$$
 \sum_{\substack{\alpha\text{ primitive cubic}\\
                         N\operatorname{cond}(\alpha)\le Q}}
       |L(1/2+it,\alpha)|^4
       \ll_{\epsilon,H}Q^{13/10+\epsilon},\qquad |t|\le H,
                                                        \tag{1.5}
$$

within the fixed finite character data specified in Section 2. This
uses a third-power large-value estimate and the ordinary second
moment. Both sums in the approximate functional equation are retained.
The resulting exponent improves the $Q^{3/2+\epsilon}$ bound obtained
by applying the conductor inequality directly to the square. Combining
a $Q^{1/6+\epsilon}$ individual estimate with the conductor second
moment, when such an individual estimate is available, instead gives
$Q^{4/3+\epsilon}$; (1.5) saves a further $Q^{1/30}$ relative to
that comparison and uses no individual subconvex estimate. We also
record a polynomial fourth moment from the two fifth-power transfers,
which improves the earlier $CT^2$ term when $T>C^{51/74}$ with a
fixed power buffer.

The quadratic weight uses the number-field large sieve [4].
The Gram, Poisson, and Hilbert-duality method is established in [5,
Lemma 4.3 and Section 4], and its cube-free natural-index extension is
[6, Section 2.3]. Iterative sieve arguments also occur in [3, Section 7].
We claim the explicit conductor-pair bounds (1.3)--(1.4) and their
complete signed-source consequence, rather than iteration or duality
as new methods. The source decomposition and earlier comparisons are
[1,2]. We use the maximum and total of a quadratic weight, supplied by
[3,4], and compare estimates on each identical signed source block.
The natural-row density argument in [7] does not give this
conductor-pair transfer. The coefficient-specific product means of [8]
are not substituted for an arbitrary twisted conductor-pair mean.

The nonorthogonality lower bounds in [9] concern the unrestricted
cubic and quartic sieve operators; perfect orthogonality for those
operators is not claimed. The distribution theorem of Lamzouri and
Nath [10] concerns maxima of rational cubic character sums. Here the
family is Eisenstein conductor pairs, and the polynomial coefficients
are arbitrary common divisor-bounded sequences. The cubic Dirichlet
family in Baier and Young [11] has rational columns and different norm
geometry; its estimates are not imported as Hecke moment bounds.

There is also a conductor-ordered zero-density consequence. For each
fixed $3/4<\sigma<1$ and $\epsilon>0$, some fixed $h>0$ gives

$$
 \sum_{\substack{\alpha\text{ primitive cubic}\\
                     N\operatorname{cond}(\alpha)\le Q}}
     N(\sigma,Q^h;\alpha)
       \ll_{\sigma,\epsilon}Q^{E(\sigma)+\epsilon}.
                                                        \tag{1.6}
$$

Here $N$ counts zeros with multiplicity, the finite local data remain
fixed, and the explicit continuous decreasing function $E$ is given
in Theorem 9.1. Its benchmarks include $E(4/5)=10/13$,
$E(5/6)=3/5$ and $E(17/20)=1/2$. This applies the scalar zero
detector of [6, Sections 4--5.2] directly with conductor bound $Q$,
then replaces its family estimate with (1.3)--(1.4). The small height
power is chosen after $\sigma,\epsilon$ and all finite profile orders;
no uniform positive height power at the limiting endpoints is asserted.
This consequence does not use (1.5).

The complementary larger-core sum remains unresolved. Theorem 1.1
gives no full inverse-norm estimate, new individual zero-free region,
or resolution of RH.

![Complete formula exponents at mark length D to the power 15/16, with the previous 23/48 cutoff, the single-transfer 1/2 cutoff, and the two-transfer cutoff 634/1263.](supplement/figures/core_cutoffs.png)

**Figure 1.** Maxima of upper-bound formulas, with arbitrarily small
losses suppressed. The inset separates the two conductor-pair bounds
near the comparison budget. These are not measured source sizes.
The exact rational table and plotting code are in the supplement.

## 2. Characters and the ordinary conductor mean

Work in $\mathcal O=\mathbb Z[\omega]$, with
$\omega=e^{2\pi i/3}$, and use ideal norms. A good ideal is prime to
the primes above $2,3$. We identify it with a chosen primary generator,
keeping the fixed finite ray data whenever reciprocity requires it.
Write $\chi_a(u)=(u/a)_6$, $\rho_a=\chi_a^2$ and
$\eta_a=\chi_a^3$, with their literal zero extension at common
primes. An index is extended multiplicatively when it is not squarefree.

Let $\mathcal F(X,Y)$ consist of the pairs $(x,y)$ of good squarefree
ideals with $(x,y)=1$, $X\le Nx<2X$ and $Y\le Ny<2Y$.
The character $\alpha_{x,y}=\rho_x\overline{\rho_y}$ has good
conductor $xy$. At each good prime its exponent is $1$ or $2$
according as the prime divides $x$ or $y$. Consequently distinct pairs
in $\mathcal F(X,Y)$ give distinct primitive good characters. This
restriction is essential in the Gram argument. All local scale
parameters below are at least one; bounded nonempty daughter windows
are absorbed by fixed support constants.

A centrally normalized ordinary polynomial has the form

$$
 Q_\beta(L)=L^{-1/2}\sum_n b_n\beta(n)W_0(Nn/L),       \tag{2.1}
$$

where $n$ ranges over ordinary good ideals, the coefficients are bounded
by a fixed divisor power, and $W_0$ is smooth and compactly supported
in $(0,\infty)$. The coefficients must be independent of whichever
character family is being averaged. Fixed growing characters or fixed
deletions may be absorbed into $b_n$; their conductors do not enlarge
the coefficient bound. Common separated profile families are permitted
with bounded weighted Mellin or Fourier $L^1$ seminorms.

We suppress arbitrarily small powers of the scale parameters in local
inequalities. Write

$$
 B_C(L)=C^2+CL.
$$

The inputs of [1, Lemma 3.1], also stated in [2, (3.2)], are

$$
 \sum_{x\sim X,y\sim Y}^{\mathrm{sf}}
       |Q_{\alpha_{x,y}}(L)|^2\ll B_C(L),\qquad
 \sum_{\kappa\sim K}^{\mathrm{sf}}|Q_{\eta_\kappa}(L)|^2
                                      \ll K+L.         \tag{2.2}
$$

The first positive mean permits overlapping outer pairs with their
original zeros. In this paper we restrict it to $\mathcal F(X,Y)$
whenever Gram distinctness is needed.

Here are the coefficient and normalization details needed later.
For squarefree inner ideals, [3, Proposition 8.1], reciprocity and
finite ray partition give the first bracket

$$
 XY+m^{2/3}n^{1/3}L+m^{1/3}n^{2/3}L^{2/3},
 \qquad m=\min(X,Y),\quad n=\max(X,Y).
$$

The middle coefficient is at most $C$. At $L=C$ the last term is
$m^{2/3}n\le mn$, so it is bounded by $XY$ for $L\le C$
and by $CL$ for $L\ge C$. The second assertion is [4].
To restore ordinary inner ideals, write uniquely $n=e^2f$ with $f$
squarefree, without imposing $(e,f)=1$. The daughter length is
$L/(Ne)^2$, and its exterior central factor is $(Ne)^{-1}$.
Multiplication by $\alpha_{x,y}(e^2)$ is a diagonal contraction.
Hilbert-space triangle gives

$$
 \sum_{Ne\ll\sqrt L}\frac1{Ne}
       \sqrt{C^2+CL/(Ne)^2}
       \ll L^\epsilon\sqrt{C^2+CL}.                   \tag{2.3}
$$

For each fixed $e$, the daughter coefficients $b_{e^2f}$ remain
common. The quadratic lift is identical. This proves the ordinary
form needed here, including fixed common twists and original zeros.
It is not an import of a sieve restricted to special product coefficients.

## 3. A Gram bound for distinct conductor pairs

Fix a smooth radial $V$ of compact support in $(0,\infty)$ and put

$$
 G_{\alpha,\beta}(Z)=\sum_{n\text{ good}}V(Nn/Z)
                        \alpha(n)\overline{\beta(n)},
 \qquad Z\ge1.                                       \tag{3.1}
$$

The sum is over primary ideal representatives. Fixed ray packets are
allowed. We may choose $V\ge0$ and $V\ge1$ on any fixed compact
product window when using this as a Gram matrix.

**Lemma 3.1.** Uniformly in $\alpha\in\mathcal F(X,Y)$,

$$
 \sum_{\substack{\beta\in\mathcal F(X,Y)\\\beta\ne\alpha}}
       |G_{\alpha,\beta}(Z)|^2
       \ll_\epsilon(CZ)^\epsilon(C^2Z+C^5).            \tag{3.2}
$$

The constant depends on finitely many seminorms of $V$ and the fixed
finite data. A fixed additional deletion ideal can be retained with
its divisor-power loss; this extension is not needed for polynomial
twists, which can instead remain in the common coefficients.

*Proof.* Fix $\alpha=\rho_a\overline{\rho_b}$.
For $\beta=\rho_c\overline{\rho_d}$, partition the primes of
$ab$ according to whether they divide neither of $c,d$, divide $c$,
or divide $d$. There are at most $3^{\omega(ab)}$ sectors. On each
sector write $c=c_0c'$ and $d=d_0d'$, where $c_0,d_0$ are fixed
divisors of $ab$ and $(c'd',ab)=1$. Put

$$
 X'=X/Nc_0,\qquad Y'=Y/Nd_0,\qquad U=X'Y'\ll C^2.
$$

The residual variables $c',d'$ are squarefree and coprime. At primes
of $ab$, subtract the exponent of $\beta$ from that of $\alpha$
modulo three. Nonzero differences define a fixed character $\gamma$
of good conductor norm $A\ll C^2$. Equal nonzero exponents leave a
fixed zero mask $g$. The supports of $\gamma$, $g$, and $c'd'$
are pairwise disjoint. The original ratio is exactly

$$
 \alpha(n)\overline{\beta(n)}
 =\gamma(n)\overline{\rho_{c'}(n)}\rho_{d'}(n)
                         \mathbf1_{(n,g)=1}.           \tag{3.3}
$$

In particular the deletion at a canceled prime must not be discarded.
The good primitive part $\psi=\gamma\overline{\rho_{c'}}\rho_{d'}$
has conductor norm

$$
 Q=A\,Nc'\,Nd'\asymp Q_*:=AU.                        \tag{3.4}
$$

It can be principal only when its three disjoint supports are empty.
That means that all original local exponents agree, hence
$\beta=\alpha$, which is excluded. Bounded ray factors are fixed
first and do not affect this good-prime argument.

Expand the deletion over $m\mid g$, write $n=mh$, and put $M=Nm$.
Fixed exclusions at the bad primes are treated by the same finite
expansion. For this term the ordinary primal scale is $Z/M$.
Primitive Poisson [3, Lemma 3.1], or its primary-lattice form
[5, Lemma 4.3], has scalar and dual scale

$$
 \frac{Z}{M\sqrt Q},\qquad J_0=\frac{Q_*M}{Z}.         \tag{3.5}
$$

The zero frequency vanishes. The complete Gauss and CRT factors,
including $\psi(m)$, are row scalars of modulus at most one. They
are independent of the dual frequency. After absolute squaring they
may be removed. The frequency character is
$\overline\gamma(h)\rho_{c'}(h)\overline{\rho_{d'}(h)}$.
Thus $\overline\gamma(h)$, with all its zeros, is a common
coefficient for the remaining conductor-pair family.

We spell out the uniform separation. On a dual dyad $Nh\asymp J$,
the radial Fourier profile depends on the moving conductor through
$Q=A\,Nc'\,Nd'$ and on the frequency through $Nh$.
After scaling, these are compact norm boxes. Fourier or Mellin
separation gives a common frequency coefficient sequence, row norm
phases, and a common integrable majorant of mass
$O_L((1+J/J_0)^{-L})$ for every fixed $L$. Its differentiated
versions have the same property after changing $L$. The bounded
amplitude $(Q/Q_*)^{-1/2}$ can be separated simultaneously. Radiality
removes angular dependence on a conductor generator. Primary
congruences add only the fixed bounded-modulus frequency phase in
[5, Lemma 4.3]; units and exact powers of bad primes can be partitioned
first. Their character values are row scalars, and their number on
each dyad is subpower. No growing row-dependent character remains
inside a purportedly common coefficient.

Apply Minkowski to the separated integral. The ordinary form of (2.2)
on $c'\sim X'$, $d'\sim Y'$ bounds the unnormalized dual squared
mean by $J(U+\sqrt U\,J)$, up to subsidiary powers. All original
outer exclusions can be dropped at this positive stage. Thus the
squared mean from this dyad is at most

$$
 (CZ)^\epsilon\frac{Z^2}{M^2Q_*}
        J(U+\sqrt U\,J)(1+J/J_0)^{-L}.                 \tag{3.6}
$$

For $s=1,2$ and $L>s$, the dyadic sum of
$J^s(1+J/J_0)^{-L}$ over actual $J\ge1$ is $O(J_0^s)$.
If $J_0<1$, the sum is $O(J_0^L)\le O(J_0^s)$; no frequency
of artificially unit norm is inserted. Substituting (3.5) into (3.6)
and summing gives

$$
 (CZ)^\epsilon\left(\frac{ZU}{M}+\sqrt U\,Q_*\right)
 =(CZ)^\epsilon\left(\frac{ZU}{M}+AU^{3/2}\right)
 \ll (CZ)^\epsilon(C^2Z+C^5).                          \tag{3.7}
$$

The squarepart lift (2.3) is what permits ordinary dual frequencies
in this step; it introduces no coprimality between an extracted square
part and its squarefree kernel. Finally use Cauchy or Minkowski across
the divisor-many deletion terms and overlap sectors, and rechoose
$\epsilon$. An additional fixed deletion is expanded in the same
way; terms sharing a primitive conductor prime vanish and the others
have the favorable factor $M^{-1}$ in (3.7). This proves the lemma.
$\square$

## 4. Iterated large values and a quadratic weight

Let $T_\alpha$ be a centrally normalized ordinary polynomial of length
$T$, with common divisor-bounded coefficients on $\mathcal F(X,Y)$.
Fixed common characters and deletions belong to its coefficients. For
an integer $j\ge2$, its $j$th power has length $Z=T^j$ and common
coefficients bounded by a fixed divisor power, with squared mass
$O(Z(CT)^\epsilon)$. Constants may depend on each fixed power.

**Lemma 4.1.** Writing
$\mathcal R(V)=\#\{\alpha:|T_\alpha|^2\ge V\}$, one has

$$
 \mathcal R(V)\ll(CT)^\epsilon
 \left(\frac{T^j}{V^j}+
              \frac{C^2T^j+C^5}{V^{2j}}\right),\qquad V>0.
                                                        \tag{4.1}
$$

*Proof.* Choose a smooth nonnegative majorant at least one on the fixed
product support. The coefficient vector divided by its square root
has squared mass $O(Z(CT)^\epsilon)$. Restrict to $r=\mathcal R(V)$
rows. The Gram diagonal is $O(Z)$; Lemma 3.1 and Cauchy bound an
absolute off-diagonal row by
$O((CT)^\epsilon\sqrt{r(C^2Z+C^5)})$. Hilbert duality gives

$$
 rV^j\ll(CT)^\epsilon\{Z+\sqrt{r(C^2Z+C^5)}\}.         \tag{4.2}
$$

Splitting the two terms proves (4.1). $\square$

We now retain more information about the selected dual rows.

**Proposition 4.2 (restricted-row transfer).** Suppose that uniformly
for every such common polynomial and its common separated profile,

$$
 \mathcal R(V;C,T)\ll(CT)^\epsilon
       \sum_{(a,b,q)\in\mathcal E} C^aT^bV^{-q},        \tag{4.3}
$$

where $\mathcal E$ is finite, $a\ge0$, $0\le b\le q$, and $q>1/2$.
For each fixed integer $j\ge2$, the same assertion holds with exponent
set

$$
 \mathcal E'={(0,j,j)}\cup
       {(a+4b,\ j(q-b),\ 2jq):(a,b,q)\in\mathcal E}. \tag{4.4}
$$

*Proof.* For any set of at most $r$ rows, layer cake of the absolute
value, rather than its square, gives

$$
 \sum_{\alpha\text{ selected}}|Q_\alpha(J)|
 \ll(CJ)^\epsilon\sum_{\mathcal E}
     r^{1-1/(2q)} C^{a/(2q)}J^{b/(2q)}.                 \tag{4.5}
$$

Indeed integrate $\min\{r,\mathcal R(u^2;C,J)\}$ over $u>0$.
For a single term $Hu^{-2q}$, the integral is
$\frac{2q}{2q-1}r^{1-1/(2q)}H^{1/(2q)}$; the finite-sum minimum
inequality permits summing these bounds. The assumption $q>1/2$
is precisely the convergence requirement.

Fix an original Gram row and one overlap sector in (3.3). The selected
residual pairs $(c',d')$ remain distinct: $c_0,d_0$ are fixed and the
original pair is recovered uniquely from $(c',d')$. Their number is
at most $r$. Retain $A,U,M,Q_*=AU$ from (3.4)--(3.5), and put
$Z'=Z/M$ and $J_0=Q_*/Z'$. On an actual dual dyad $J\ge1$,
Poisson has amplitude $Z'/\sqrt{Q_*}$ and centralizing its dual sum
adds $\sqrt J$. Its root and CRT factors are scalars for each row
and can be removed inside that row's absolute value. The fixed
$\overline\gamma(h)$ remains a common coefficient for the residual
family, whose parameter is $\sqrt U$. Apply (4.5) after the common
norm-box separation in Lemma 3.1. One monomial contributes

$$
 (CZ)^\epsilon r^{1-1/(2q)}
 \frac{Z'}{\sqrt{Q_*}}\,U^{a/(4q)}
 J^{(q+b)/(2q)}(1+J/J_0)^{-L}.                         \tag{4.6}
$$

Choose the fixed decay order larger than $(q+b)/(2q)$, with room
for the finitely many subsidiary powers. Summing dyads gives the
corresponding power of $J_0$, also when $J_0<1$ as in Lemma 3.1.
No artificial unit frequency is inserted. Substitution yields

$$
\begin{aligned}
 &(CZ)^\epsilon r^{1-1/(2q)}
       A^{b/(2q)}U^{(a+2b)/(4q)}(Z')^{(q-b)/(2q)}\\
 &\hspace{8mm}\ll(CZ)^\epsilon r^{1-1/(2q)}
       C^{(a+4b)/(2q)}Z^{(q-b)/(2q)}.                 \tag{4.7}
\end{aligned}
$$

All replacements are favorable because $a,b,q-b$ are nonnegative,
$A,U\ll C^2$, and $M\ge1$. Ordinary dual indices are admitted by
(2.3), with no new coprimality. Sum the divisor-many overlap and
canceled-prime deletion sectors as before. Restrictions may be
extended only within the distinct residual family.

Apply this absolute restricted-row bound to the Gram matrix for the
actual $j$th power of the original polynomial. Hilbert duality gives
$rV^j$ bounded by $Z=T^j$ plus the sum of (4.7), up to the
subsidiary power. If the diagonal dominates, then $r\ll T^j/V^j$.
If a term with exponent $q$ dominates, solve it by raising to the
power $2q$; it gives
$r\ll C^{a+4b}T^{j(q-b)}V^{-2jq}$. This is (4.4).
The induction is finite, with its powers, profile seminorms and decay
orders fixed before the preliminary losses are allocated. $\square$

The ordinary mean (2.2) supplies the initial exponent set
$\{(2,0,1),(1,1,1)\}$ by Markov's inequality. One transfer recovers
Lemma 4.1. Two transfers with $j=5$ give the following usable bound:

$$
 \mathcal R(V)\ll(CT)^\epsilon\left(
 \frac{T^5}{V^5}+\frac{C^{20}}{V^{50}}
 +\frac{C^{22}T^{25}}{V^{100}}
 +\frac{C^5T^{50}}{V^{100}}\right).
                                                        \tag{4.8}
$$

This is a theorem about one common polynomial, with no zero detector
or saturation hypothesis. At $T=C^{2/3}$ and $V=C^{3/8}$, its four
count exponents are $35/24,5/4,7/6,5/6$, whereas (4.1) with $j=5$
has maximum $19/12$. This comparison is illustrative; the complete
source estimate below uses all amplitudes.

**Lemma 4.3.** For nonnegative weights $S_\alpha\le B$ with
$\sum_\alpha S_\alpha\le N$, and a bound (4.3) with every $q>1$,

$$
 \sum_\alpha |T_\alpha|^2S_\alpha
 \ll(CT)^\epsilon\sum_{\mathcal E}
       N^{1-1/q}B^{1/q}C^{a/q}T^{b/q}.                 \tag{4.9}
$$

*Proof.* If $BN=0$ the assertion is immediate. Otherwise integrate
$\min\{N,B\mathcal R(v)\}$ and use

$$
 \int_0^\infty\min(N,Hv^{-q})\,dv
       =\frac q{q-1}N^{1-1/q}H^{1/q}.                 \tag{4.10}
$$

Splitting the finite sum proves the claim, including small amplitudes.
$\square$

For the rest of the paper set
$\mathcal E=\{(0,5,5),(20,0,50),(22,25,100),(5,50,100)\}$.
Let $Q_{i,\alpha,\kappa}$ have length $R_i$ and character
$\alpha\xi_i\eta_\kappa$, while $T_\alpha$ has character
$\alpha\xi_0$. Common coefficients and fixed $\xi_i$ are
independent of $\alpha,\kappa$; they may depend on frozen auxiliary
indices. For
$S_\alpha=\sum_{\kappa\sim K}^{\mathrm{sf}}|Q_{1,\alpha,\kappa}|^2$,
(2.2) supplies valid bounds

$$
 B=K+R_1,\qquad N=K B_C(R_1),\qquad B_C(L)=C^2+CL,     \tag{4.11}
$$

up to subsidiary powers. The quadratic bound fixes $\alpha$ first;
the cubic bound fixes $\kappa$ first. The remaining character in each
case is an admitted common coefficient. Cauchy with the second mark
therefore gives

$$
\begin{aligned}
 &\sum_{\alpha\in\mathcal F(X,Y),\,\kappa\sim K}^{\mathrm{sf}}
       |T_\alpha Q_{1,\alpha,\kappa}Q_{2,\alpha,\kappa}|\\
 &\quad\ll(CTR_1R_2K)^\epsilon\sqrt{K B_C(R_2)}
   \sum_{(a,b,q)\in\mathcal E}
       N^{(q-1)/(2q)}B^{1/(2q)}C^{a/(2q)}T^{b/(2q)}.
                                                        \tag{4.12}
\end{aligned}
$$

Every inner-length exponent on the right is nonnegative. This permits
the source-mask restoration below. The original $(x,y)=1$ remains
necessary for distinctness; positive extension to repeated primitive
characters is not justified by the Gram argument.

## 5. The signed source and its block estimates

We give the source definition and the exact inputs from [1,2] so that
the selected expression and its normalization are unambiguous.
Let $W,V,\Omega$ be fixed smooth compactly supported functions on
$(0,\infty)$, with $\Omega\ge0$. Let $c_a$ be supported on good
squarefree ideals and bounded by a fixed power of the divisor function.
Define

$$
\begin{aligned}
 M_u(D)&=D^{-1/2}\sum_a c_a\overline{\chi_a(u)}W(Na/D),\\
 S_u(P)&=P^{-1/2}\sum_r\eta_r(u)V(Nr/P),\\
 Z&=\sum_{u\in\mathcal O\setminus\{0\}}
                    \Omega(Nu/D^2)|M_u(D)S_u(P)|^2.
                                                        \tag{5.1}
\end{aligned}
$$

The marks $r$ are ordinary ideals. Fixed mark characters and fixed
primary or unit packets of $u$ are permitted. Profiles depend on norms
after finite ray partition, or belong to a common separated family
with the weighted seminorm bounds of Section 2.

Expand (5.1) in $a,b,r,s$ and make the unique factorizations

$$
\begin{gathered}
 a=ga_0,\quad b=gb_0,\qquad
 r=qr_0v^2,\quad s=qs_0w^2,\quad f=r_0s_0,\\
 e_a=(a_0,f),\quad e_b=(b_0,f),\qquad
 a_0=e_ax,\quad b_0=e_by,\quad f=e_ae_bf_0.             \tag{5.2}
\end{gathered}
$$

Here $g,a_0,b_0$ are pairwise coprime and squarefree, as are
$q,r_0,s_0$; $v,w$ are unrestricted. The ideals
$x,y,e_a,e_b,f_0$ are pairwise coprime and squarefree. The original
row character is

$$
 \chi_x^5\chi_y\chi_{e_a}^2\chi_{e_b}^4\eta_{f_0}
                         \mathbf1_{(u,gqvw)=1},        \tag{5.3}
$$

with good primitive conductor $\mathfrak c=e_ae_bxyf_0$.

**Definition 5.1.** Fix smooth $\vartheta$ which is zero on $[0,1]$
and one on $[2,\infty)$, and insert
$\vartheta(N\mathfrak c/\tau)$ in this expansion. Expand the last
mask in (5.3) over $d\mid\operatorname{rad}(gqvw)$ and apply
primitive Poisson on each $d$-lattice. The scalar is
$D^2/(Nd\sqrt{N\mathfrak c})$, the dual norm scale is
$N\mathfrak c\,Nd/D^2$, and the zero frequency vanishes.
After clearing the fixed dual-lattice denominator, retain exactly the
nonzero dual frequencies whose good squarefree quadratic core has
norm at most $R$. Their signed sum is $Z_{\mathrm{hi},\le R}$.
Fixed bad-prime core packets are retained separately. This is the
selection of [1, Section 2] and [2, Section 2].

Freeze $g,e_a,e_b,q,v,w,d$, and allocate the primes of $e_ae_b$
between $r_0,s_0$. Put

$$
\begin{gathered}
 G=Ng,\quad E=Ne_aNe_b,\quad Q=N(qvw),\quad\Delta=Nd,\quad L=D/G,\\
 X=L/Ne_a,\quad Y=L/Ne_b,\quad C=D/(G\sqrt E),\quad
 F=P^2/(Q^2E).                                         \tag{5.4}
\end{gathered}
$$

The residual squarefree marks have lengths $R_1R_2\asymp F$;
label them so $R_1\le R_2$, and note $R_i\ll P$.
On the dual annulus $H=\Lambda H_0$ and core dyad $N\kappa\asymp K$,

$$
 H_0=L^2F\Delta/D^2,\qquad T=\sqrt{H/K}.                \tag{5.5}
$$

The primitive Gauss factorization in [1, Section 5] gives the three
moving polynomial characters

$$
 \alpha_{x,y}(t),\qquad
 \alpha_{x,y}(r_1)\eta_\kappa(r_1),\qquad
 \alpha_{x,y}(r_2)\eta_\kappa(r_2).                     \tag{5.6}
$$

Frozen interactions are common characters, deletions, and bounded
outer factors. The finite quadratic Gauss factor separates into fixed
ray characters on the marks. In particular the $t$ polynomial is
independent of $\kappa$; there is no $(t,\kappa)=1$ condition.
The original $(x,y)=1$ restriction supplies exactly the distinct
family of Section 3.

The remaining natural $t$ and disjoint squarefree marks obey
$(r_1r_2,t)=1$. The exact local generating series is
$1/(1-z_0)+z_1+z_2$. Dividing by three ordinary series gives

$$
 [1+(1-z_0)(z_1+z_2)](1-z_1)(1-z_2).                   \tag{5.7}
$$

It has no linear terms. Its signed extraction coefficients satisfy

$$
 \sum\frac{|a(d_0,d_1,d_2)|}
               {\sqrt{Nd_0Nd_1Nd_2}}\ll(DPR)^\epsilon
                                                        \tag{5.8}
$$

on the actual support: with each denominator exponent increased by
$\epsilon$, the Euler product converges absolutely. Insert all
characters and fixed deletions before this extraction. Each daughter
shortens $T,R_1,R_2$ separately and contributes the exterior factor
$(Nd_0Nd_1Nd_2)^{-1/2}$. By the monotonicity after (4.12), (5.8)
restores the full mask at subsidiary cost. No extraction/residual
coprimality is inserted. Empty daughters stay empty and bounded
nonempty windows are covered by fixed support constants.

For clarity, we retain the scalar before substituting a polynomial
estimate. The centrally normalized inverse-column scalar is
$D^2/(DP\Delta\sqrt{EF})$. The number of frozen tuples on these
dyads is at most $GEQ(DP)^\epsilon$, grouping $(q,v,w)$ by its
product; there is no additional $f_0$ count. Centralizing the three
inner factors supplies $\sqrt{TF}$, and undoing the inverse-column
centralization supplies $1/C$. Their product is

$$
 \frac{D^2}{DP\Delta\sqrt{EF}}\,GEQ\,
                    \frac{\sqrt{TF}}{C}
       =\frac{D^2\sqrt T}{\Delta\sqrt{EF}\,C^2}.         \tag{5.9}
$$

Thus (4.12) times (5.9) is a bound for the entire signed block on the
chosen auxiliary and mark dyads, after summing its actual frozen tuples.
We use two other bounds for this identical block. The previous
fourth-moment crossing [2, (4.6)] is

$$
\begin{aligned}
 \mathcal A_4={}&\frac{D^2\sqrt T}{\Delta\sqrt{EF}}
 K^{3/4}(K+R_1)^{1/4}(1+T^2/C)^{1/4}\\
 &\hspace{25mm}\cdot(1+R_1/C)^{1/4}(1+R_2/C)^{1/2}.
                                                        \tag{5.10}
\end{aligned}
$$

The original crossing [1, (6.3)], [2, (4.7)] is

$$
 \mathcal A_0=\frac{D^2\sqrt T}{\Delta\sqrt{EF}}
       \sqrt{K(K+R_1)}\sqrt{1+T/C}\sqrt{1+R_2/C}.       \tag{5.11}
$$

Finally the grouped-variable argument of [1, Section 7], in the
uniform form [2, (4.8)–(4.9)], gives

$$
\begin{aligned}
 \mathcal G\ll{}&\Lambda^{1/2}\Delta^{-1/2}D\sqrt{FK}
 +\Lambda^{1/2}\Delta^{-1/2}D^{11/6}\sqrt K\\
 &+\Lambda^{1/3}\Delta^{-2/3}D^{5/3}K^{2/3}
 +\Lambda D^2.                                         \tag{5.12}
\end{aligned}
$$

This uses the actual nonempty condition $K\ll H$, not an assumption
$F\le KP$. Its underlying brackets are
$J+(JL)^{2/3}+J^{1/3}L$, $J=FT$, and
$T\{F+L+(FL)^{2/3}\}$, with common scalar $DGK/(\Delta F)$.
They follow by grouping $j=tf_0$ and retaining the complete original
$(x,y)=1$ projector before the positive estimates, as proved in the
cited sources. We use precisely those block estimates and their
coefficient class, with no bound for a whole signed sum transferred
to a subset.

## 6. Completing the original-sector estimate

First retain the mask and annular factors. In (4.12) times (5.9),
the four total powers of $T$ are $1,1/2,5/8,3/4$. Since
$T\propto\sqrt{\Delta\Lambda}$, their $\Delta$ powers are
$-1/2,-3/4,-11/16,-5/8$ and their $\Lambda$ powers are
$1/2,1/4,5/16,3/8$. Thus all decrease in $\Delta$.
The corresponding monotonicity for
(5.10)–(5.12) is proved in [2, Section 5]. All four estimates are
bounded by their scale expressions at $\Delta=\Lambda=1$, times
a common multiple of

$$
 h(\Lambda)=\Lambda^{1/4}+\Lambda.                     \tag{6.1}
$$

This is a comparison of formulas on each actual annulus; it does not
claim that the annulus with $\Lambda=1$ is nonempty. The original
Poisson profiles have arbitrary decay as $\Lambda\to\infty$, while
$h$ has positive exponent at zero. Their common separated seminorms
therefore sum (6.1). Mask divisors and dyads cost subsidiary powers.

For the scale algebra we can now put $\Delta=\Lambda=1$, obtaining

$$
 T=\frac{\sqrt F}{G\sqrt K},\qquad
 \frac TC=\frac{P}{DQ\sqrt K}\le1,\qquad
 B_0=D^{11/6}\sqrt K+D^{5/3}K^{2/3}+D^2.               \tag{6.2}
$$

There are three exhaustive cases, with fixed annular constants absorbed
in the implicit constants.

**Case 1: $R_1<K$.** Since $R_2\ll P$, we have $F\ll KP$.
The grouped estimate (5.12) gives

$$
 |Z_{\mathrm{block}}|\ll D\sqrt P\,K+B_0.              \tag{6.3}
$$

**Case 2: $K\le R_1\le R_2$ and $R_2>C$.** Retaining the auxiliary
factors in (5.11), as in [2, (5.4)], gives

$$
 |Z_{\mathrm{block}}|
 \ll D^2K^{1/4}
       \left(\frac1{GE}+\frac P{DQE}\right)^{1/2}.
$$

Now $R_2\ll P$ and $R_2>C=D/(G\sqrt E)$ imply
$G\sqrt E\gg D/P$. Since $E,Q\ge1$, both terms in parentheses
are $O(P/D)$, and hence

$$
 |Z_{\mathrm{block}}|\ll D^{3/2}P^{1/2}K^{1/4}.        \tag{6.4}
$$

We retain this stronger form instead of weakening it to the leading
term of [2].

**Case 3: $K\le R_1\le R_2\le C$.** In (4.11) use
$N\ll KC^2$, $B\ll R_1$, and
$\sqrt{K B_C(R_2)}\ll\sqrt K\,C$. Multiply one monomial of
(4.12) by (5.9). Substituting $F=R_1R_2$ up to fixed constants,
$C=D/(G\sqrt E)$ and $T=\sqrt F/(G\sqrt K)$ gives

$$
\begin{aligned}
 A(a,b,q)={}&D^{2+(a-2)/(2q)}K^{(3q-b-2)/(4q)}
 R_1^{(b-q+2)/(4q)}R_2^{(b-q)/(4q)}\\
 &\cdot G^{-(a+b+q-2)/(2q)}E^{-(2q+a-2)/(4q)}.
                                                        \tag{6.5}
\end{aligned}
$$

Since $b\le q$ and $R_2\ge R_1$, the two mark powers are at most
$R_1^{(b-q+1)/(2q)}$. The $G,E$ exponents are nonpositive for all
four monomials. Label their resulting bounds $A_1,A_2,A_3,A_4$:

$$
\begin{aligned}
 A_1&\ll D^{9/5}P^{1/10}K^{2/5},\\
 A_2&\le D^{109/50}K^{37/50}R_1^{-49/100},\\
 A_3&\le D^{21/10}K^{273/400}R_1^{-37/100},\\
 A_4&\le D^{403/200}K^{31/50}R_1^{-49/200}.
                                                        \tag{6.6}
\end{aligned}
$$

The previous fourth-moment estimate (5.10) gives
$|Z_{\mathrm{block}}|\ll I+II$, where

$$
 I=\frac{D^2\sqrt K}{\sqrt{GE}\,R_2^{1/4}},\qquad
 II=\frac{D^{7/4}K^{1/4}R_1^{1/4}}{G^{3/4}E^{3/8}}.
                                                        \tag{6.7}
$$

The grouped estimate is $V_0+B_0$, with
$V_0=D\sqrt{FK}\le DR_2\sqrt K$. As in [2, (5.7)],
$\min(I,V_0)\le I^{4/5}V_0^{1/5}\le D^{9/5}\sqrt K(GE)^{-2/5}\le D^{11/6}\sqrt K$.
Consequently $|Z_{\mathrm{block}}|\ll II+B_0$. Comparing this with
the four new terms on the identical signed block gives

$$
 |Z_{\mathrm{block}}|\ll B_0+A_1+
                     \sum_{i=2}^4\min(II,A_i).         \tag{6.8}
$$

The three negative mark powers in (6.6) now cancel by interpolation:

$$
\begin{aligned}
 \min(II,A_2)&\le II^{49/74}A_2^{25/74}
                  \le D^{561/296}K^{123/296},\\
 \min(II,A_3)&\le II^{37/62}A_3^{25/62}
                  \le D^{469/248}K^{421/992},\\
 \min(II,A_4)&\le II^{49/99}A_4^{50/99}
                  \le D^{373/198}K^{173/396}.
                                                        \tag{6.9}
\end{aligned}
$$

All remaining auxiliary powers are nonpositive. Together with Cases 1
and 2, this proves (1.1) on every core dyad, with $K$ in place of $R$.

We finish the uniformity details. The original norm profiles,
conductor cutoff, and Poisson kernel are separated by one common
Fourier or Mellin measure on fixed logarithmic boxes, as in
[1, Section 6] and [2, Section 5]. The derivatives of
$\vartheta(cz)$ have uniformly bounded scaled seminorms, since their
support has $cz$ in a fixed compact interval. This includes all
$\tau$ in the stated power range. The extraction (5.7)–(5.8)
precedes the positive norms and restores the original ordinary marks
and their redundant zeros. Divisor-bounded outer coefficients
and the frozen tuple count have already been paid in (5.9).

A general dual element, after clearing its fixed denominator, has good
part $\kappa t^2$, a fixed bad-prime core packet, and a square factor
$b^2$ supported above $2,3$. Fixing $b$ shortens $T$ to $T/Nb$.
Each new term has a positive total power of $T$, namely $1,1/2,5/8,3/4$.
Thus these square factors sum geometrically. For the old estimates
the same fact follows from their displayed $T$ powers; in the small
$F$ grouped column term one first retains
$K\ll H/(Nb)^2$, exactly as in [2, Section 5].
Finite bad-prime core packets only change the permitted finite
character data. Finally sum all auxiliary dyads, deletion divisors,
and the core dyads $K\ll R$. The powers of $K$ are nonnegative,
and the number of dyads is subpower. This proves Theorem 1.1.
$\square$

## 7. Consequences, evidence, and limits

The exact margins (1.2) prove the complete $\kappa_*=634/1263$
cutoff. For $P=D^{15/16}$, $R\le D^{\kappa_*-\delta}$ and fixed
$0<\delta<\kappa_*$, the stronger explicit conclusion is

$$
 |Z_{\mathrm{hi},\le R}|\ll_\epsilon
 D^{101/48-\eta_\delta+\epsilon},\qquad
 \eta_\delta=\min\left\{\frac{421\delta}{992},
                              \frac{227}{747696}\right\}>0.
                                                        \tag{7.1}
$$

The binding term gains $421\delta/992$, and every other term has
margin at least $227/747696$ at the endpoint. The arbitrary positive
$\epsilon$ loss is retained at the endpoint itself.

The proof is analytic. The CPU supplement checks 104,976 exact local
overlap identities, 6,561 conductor identities, 48 primitive finite
Fourier identities, and 24 deletion Fourier identities. The largest
floating-point Fourier discrepancy is below $3.6\cdot10^{-15}$;
the deliberately omitted-deletion control fails. A finite Gram fixture
checks the Hilbert-duality inequality. The additional exact symbolic
control verifies the restricted-row Poisson exponents, transfer rule,
source scalar, all four monomials, three interpolations, restoration
powers, and nine endpoint exponents. The earlier single-transfer
algebra controls are retained and labeled as baseline checks.
These finite checks do not certify the infinite analytic tails, the
imported sieves, or an asymptotic estimate by extrapolation.

From the supplement root run
`python experiments/conductor_gram_controls.py`,
`python experiments/source_scale_controls.py`,
`python experiments/iterated_gram_controls.py`, and
`python experiments/fourth_moment_controls.py`, and
`python experiments/conductor_density_controls.py`.
The first requires NumPy; the iteration control requires SymPy.
The fourth-moment control uses exact rational arithmetic in the standard
library; the density control uses SymPy to check whole rational
intervals, the finite transfers, and the integer-cover inequalities.
The figure script
additionally uses Matplotlib and writes an exact rational table.
Each control takes less than a minute on one CPU and uses well below
100 MB. The README states dependencies, provenance, and the distinction
between the finite checks and the proof.

The bounds are uniform over common divisor-bounded coefficients, but
only for the stated distinct conductor-pair family. Repeated primitive
presentations require multiplicity weights. The source theorem preserves
the original core selection; it does not estimate the complementary
larger-core sum or the signed different-shift covariance in other
formulations. No global zero-free hypothesis enters, and neither a new
zero-free region nor RH follows. This manuscript records an author
audit and a scoped independent check, described in the acknowledgment;
further independent scientific review is requested.

## 8. Polynomial and L-function fourth moments

The large-value results have a useful consequence beyond the selected
quadratic-core expression. All families and common coefficients below
are those of Section 2; in particular the endpoint pair is coprime.

**Proposition 8.1.** Put $B=C^2+CT$ and
$M_4(C,T)=\sum_{\alpha\in\mathcal F(X,Y)}|T_\alpha|^4$.
For $T\ge1$,

$$
 M_4(C,T)\ll_\epsilon(CT)^\epsilon
 \left\{B^{1/2}T^{3/2}
       +B^{4/5}(C^2T^3+C^5)^{1/5}\right\}.             \tag{8.1}
$$

For $1\le T\le C$ there is also the bound

$$
\begin{aligned}
 M_4(C,T)\ll_\epsilon(CT)^\epsilon\bigl(&
 C^{3/2}T^{5/4}+C^{116/49}\\
 &+C^{218/99}T^{25/99}+C^{67/33}T^{50/99}\bigr).
                                                        \tag{8.2}
\end{aligned}
$$

The minimum with the earlier $C^2+CT^2$ bound may always be retained.
For every fixed $51/74<t\le1$, (8.2) improves $CT^2$ by a fixed power
when $T=C^t$. At $T=C$, (8.1) gives the simpler bound
$M_4(C,C)\ll_\epsilon C^{13/5+\epsilon}$.

*Proof.* Markov applied to (2.2) gives
$\mathcal R(V)\ll(CT)^\epsilon B/V$. For $q>2$ and $A,B>0$,

$$
 \int_0^\infty V\min(B/V,A/V^q)\,dV
   =\left(1+\frac1{q-2}\right)
        B^{(q-2)/(q-1)}A^{1/(q-1)}.                  \tag{8.3}
$$

Split at $V_0=(A/B)^{1/(q-1)}$ to verify the identity. The inequality
$\min(x,\sum_i y_i)\le\sum_i\min(x,y_i)$ for nonnegative inputs
permits applying (8.3) term by term. Since
$M_4=2\int_0^\infty V\mathcal R(V)\,dV$, Lemma 4.1 with $j=3$
gives (8.1), after allocating the finitely many preliminary losses.
For (8.2), use $B\ll C^2$ and the four monomials (4.8). Their
individual thresholds for improving $CT^2$ are respectively
$2/3,67/98,119/173,51/74$; the last is largest. At $T=C$ the two
terms in (8.1) have exponents $5/2$ and $13/5$. $\square$

The fourth moment in (8.2) may be useful at shorter polynomial lengths,
while (8.1) is stronger at the approximate-functional-equation length.
Neither estimate averages a pair of different quadratic twists: freezing
each twist and then summing over two cores still charges the number of
core pairs. No new core cutoff is inferred from this corollary.

**Corollary 8.2.** Fix the finite character data and an infinity type,
and exclude the bounded principal case. For every fixed $H\ge1$,

$$
 \sum_{\alpha\in\mathcal F(X,Y)}
        |L(1/2+it,\alpha)|^4
       \ll_{\epsilon,H}(XY)^{13/10+\epsilon},
                    \qquad |t|\le H.                 \tag{8.4}
$$

Consequently (1.5) holds for the corresponding primitive cubic family
ordered by conductor, including a finite union of its fixed ray packets.
The constants may depend on the fixed local data and $H$; no growing
quadratic twist or unrestricted infinity type is hidden in them.

*Proof.* The primitive good conductor of $\alpha_{x,y}$ is $xy$.
Partitioning the fixed local data if necessary, its complete conductor
norm is a fixed multiple of $Nx\,Ny$. Hence its square root
$c_\alpha$ is comparable to $C$ uniformly, including unbalanced $X,Y$.
Use the balanced approximate functional equation, as in the proof of
[3, Theorem 1.2]. Both sums have effective norm length comparable to
$c_\alpha$. The dual sum has the conjugate character and a scalar
of modulus one on the central line. Apply
$|u+v|^4\le8(|u|^4+|v|^4)$ before removing that scalar. Conjugation
exchanges $\mathcal F(X,Y)$ with $\mathcal F(Y,X)$.

On a dyad $Nn\asymp T$, write
$(Nn)^{-1/2-it}=T^{-1/2}(T/Nn)^{1/2}(Nn)^{-it}$.
The latter factors are bounded common coefficients. The remaining
smooth weight depends on $Nn/c_\alpha$, the fixed infinity type,
and $t$. Since $c_\alpha/C$ lies in a fixed compact interval, a
common Fourier expansion in its logarithm separates this dependence
into bounded row factors and common profiles in $Nn/T$. Extend
smoothly to a slightly larger compact interval before expanding.
The weighted $L^1$ sums of the frequency coefficients, with every
fixed required profile seminorm, are bounded uniformly for $|t|\le H$.
For $T>C$ they have arbitrary inverse powers of $T/C$ from the
rapid decay of the approximate-functional-equation weight. For
$T\le C$ the weight and its norm-scaled derivatives are uniformly
bounded. The same statements hold for the dual weight.

Minkowski in $\ell^4(\mathcal F(X,Y))$ therefore permits applying
(8.1) on each dyad and then integrating the common expansion.
For $1\le T\le C$, (8.1) is at most

$$
 (CT)^\epsilon\{CT^{3/2}+C^2T^{3/5}+C^{13/5}\}
       \ll C^{13/5+2\epsilon}.                       \tag{8.5}
$$

There are $O(\log C)$ such dyads. Above $C$, the polynomial growth
of (8.1) is absorbed by the arbitrary inverse powers of $T/C$.
Summing in $\ell^4$, raising to the fourth power, and rechoosing
$\epsilon$ prove (8.4). Finite Euler factors at the fixed bad places
and their inverses are bounded on the central line and cause no
additional power loss.

Finally a primitive good cubic character has a cube-free presentation
$g=xy^2$, with $x,y$ coprime squarefree, whose conductor is $xy$ up
to the fixed local factor. Dyadically partition $Nx,Ny$ and sum (8.4)
over $XY\ll Q$. The powers sum geometrically, with logarithmic
multiplicity, giving $Q^{13/10+\epsilon}$. The bounded principal
or fixed-conductor cases cost $O_H(1)$. This proves (1.5). $\square$

The argument uses conductor ordering throughout; it never replaces
$Nx\,Ny$ by the natural height $N(xy^2)$. The exponent $13/10$ is
not the conjectural fourth-moment exponent $1$. The corollary depends
on Lemma 3.1 and Lemma 4.1, and does not require Proposition 4.2 or
the signed-source reconstruction in Sections 5--6. Its algebraic
checks are included in the supplement; the analytic inputs and the
approximate-functional-equation separation remain proof obligations
for independent review.

## 9. Zero density ordered by conductor

Let $\mathcal F(Q)$ be the distinct primitive cubic Hecke characters
of conductor norm at most $Q$ in the fixed finite local packets of
Section 2, with trivial infinity type. For a nonprincipal member set

$$
 N(\sigma,H;\alpha)
   =\#\{\rho:\ L(\rho,\alpha)=0,\
                 \operatorname{Re}\rho\ge\sigma,\
                 |\operatorname{Im}\rho|\le H\},
                                                        \tag{9.1}
$$

counting multiplicity. Principal and bounded-conductor exceptions
are treated separately below. This is the full admitted conductor
family, allowing both local exponents $1$ and $2$ at good primes.

**Theorem 9.1.** For every fixed $3/4<\sigma<1$ and $\epsilon>0$
there is a fixed $h=h(\sigma,\epsilon)>0$ such that (1.6) holds with
the following function. Adjacent formulas agree at every join.

| Range of $\sigma$ | $E(\sigma)$ |
| --- | --- |
| $3/4<\sigma\le71/88$ | $10(1-\sigma)/(1+2\sigma)$ |
| $71/88\le\sigma\le38/47$ | $56(1-\sigma)/(64\sigma-37)$ |
| $38/47\le\sigma\le143/170$ | $24(1-\sigma)/(14\sigma-5)$ |
| $143/170\le\sigma\le17/20$ | $5(1-\sigma)/(10\sigma-7)$ |
| $17/20\le\sigma\le11/12$ | $8(1-\sigma)/(4\sigma-1)$ |
| $11/12\le\sigma<1$ | $3(1-\sigma)$ |

Only the first formula, used as a bound on the whole interval, requires
Lemma 3.1. The improvement uses Proposition 4.2 with first transfer
order $2$ or $3$ and second order between $3$ and $8$. This is a
finite envelope; no optimization over all transfers is claimed.

### 9.1. The scalar detector and common saturated factor

We specify the import from [6, Sections 4--5.2] because ordering the
family by conductor is essential here. Its scalar proof requires a
primitive conductor bound $O(Q)$, a bound $O(Q)$ for the radical of
omitted Euler factors, conjugate closure, and nonprincipality. A
conductor-pair character has conductor a fixed multiple of $N(xy)$.
The additional omitted Euler factors are at fixed bad places; the
good conductor primes already have their literal character zeros.
Conjugation exchanges $x$ and $y$. Thus these hypotheses hold
directly for $\mathcal F(Q)$. The natural index $xy^2$ is not used
to bound a family moment or to define $Q$.

Here is the part of that scalar argument needed in this proof. A
buffered rightmost-zero selection, including both conjugate functions,
gives a real bin $a\ge\sigma-o(1)$ and $d=2a-1$. The local
zero-free disks to the right of the selected maximum give arbitrarily
small power bounds for $L$ and $1/L$ on a line just right of $a$.
This is a statement about that row's actual zero set in a buffered
height rectangle. Primitive reflection gives the complementary bound
on a line just left of $1-a$. For centrally normalized smooth inverse
and full polynomials of respective lengths $Q^r,Q^c$, it follows that

$$
 |M_r|^2\le Q^{dr+o(1)},\qquad
 |S_c|^2\le Q^{d\min(c,1-c)+o(1)}.                    \tag{9.2}
$$

The profiles admit bounded real powers and norm twists within the
one reserved height allowance. The contour tails are estimated on
an absolute-convergence line, choosing their fixed decay order after
the small height power. Smaller actual conductors improve the
reflected bound. The scalar proof's printed target $5/6$ is not
needed here: its fixed real floor is $51/100$, and every fixed
$\sigma>3/4$ lies strictly above it.

The detector with total-length parameter $3/2$ then supplies an actual
inverse polynomial of length $Q^r$ with

$$
 1-o(1)\le r\le3/2+o(1),\qquad
 |M_r|^2\ge Q^{dr-o(1)}.                               \tag{9.3}
$$

This is [6, (22)--(24)], proved by shifting the Gamma-smoothed
integral of $L$ times a truncated reciprocal at an actual zero.
The product lower bound and the reflected full-factor bound in
(9.2) force the accompanying full factor to have length exponent
at most $1/2+o(1)$, giving the lower endpoint in (9.3).

For clarity, the common-coefficient step is also retained. With
$Y=Q^r$, choose a smooth cutoff $m(n)=\mu(n)V_{\le}(Nn/U)$,
where $U=(C_0Y)^{1/3}$ and $C_0$ covers the fixed witness support.
Since $\delta_1-m*\mathbf 1$ vanishes through norm $U$, its third
convolution power vanishes through $C_0Y$. Convolving with $\mu$
gives the exact identity on that support

$$
 \mu=3m-3m*m*\mathbf1+m*m*m*\mathbf1*\mathbf1.        \tag{9.4}
$$

The $3m$ term is empty for large $Q$. Partition all remaining factors
into smooth norm dyads. Fourier separation of the whole product
profile introduces one common height variable. The bounded real zero
parameter occurs in the Fourier weight, leaving common coefficients
for all separated factors. The Fourier weight has uniformly bounded
weighted $L^1$ norms. The pointwise bounds (9.2), also for a first
height derivative, select a common mesh point at an arbitrarily
small power cost, as in [6, Section 5.2]. Dyads, the mesh point and
the final row class are fixed before using a family estimate.

There are at most five factors, their limiting length exponents
sum to $r\ge1$, and the product attains the pointwise exponent
in (9.3). Dividing by the upper bounds for all other factors shows
that each factor is saturated. Every inverse factor has exponent
at most $r/3\le1/2$. A full factor with exponent exceeding $1/2$
would contradict its reflected bound in (9.2). Select a largest
factor by its common dyad. Its normalized form $F_\alpha$ satisfies

$$
 \frac15\le c\le\frac12,\qquad
 |F_\alpha|^2=Q^{dc+o(1)},\qquad T=Q^{c+o(1)}.         \tag{9.5}
$$

Its coefficients are common and divisor-bounded, with all original
zeros. This factor comes from the actual inverse witness; no
saturation assertion for arbitrary polynomials is being made.

All limiting exponents here can be formalized by the contradiction
argument in [6, Section 5]: if the asserted density estimate failed
for every sufficiently small fixed height power, take a sequence of
bin, pointwise and height losses tending to zero, and counterexamples
$Q\to\infty$ large enough for the associated constants. Passing to
a subsequence fixes limiting lengths and a limiting bin. Each row
has $O(Q^h\log Q)$ zeros in the bounded multiple of the height
rectangle, so distinct rows retain the assumed excessive exponent.
All dyad, mesh and multiplicity costs are included before the final
positive $h$ is fixed.

### 9.2. Integer covers for the conductor large values

Retain a norm rectangle $\mathcal F(X,Y)$ from the selected rows;
this loses only a logarithmic factor. Here $C\ll\sqrt Q$.
For row count $Q^{\rho+o(1)}$, (4.1) at the actual integer power
$k$ and (9.5), with $z=kc$, give

$$
 \rho\le\max\{(1-d)z,\ 1+(1-2d)z,\ 5/2-2dz\}.
                                                        \tag{9.6}
$$

Put $q=1-d$. For $1/2\le d<1$ the right side is at most
$E_0=5q/(2+d)$ throughout

$$
 L_0=\frac{15}{4(2+d)}\le z\le
 U_0=\frac5{2+d}.                                      \tag{9.7}
$$

The increasing branch equals $E_0$ at $U_0$, and the last
decreasing branch equals it at $L_0$. The middle branch at $L_0$
is smaller by $(6d-3)/(4(2+d))$. Write $c_0=U_0/4=L_0/3$.
If $c\ge c_0$, take $k=3$; then $L_0\le3c\le3/2\le U_0$.
Otherwise take $k=\lceil L_0/c\rceil\le8$; then
$L_0\le kc<L_0+c_0=U_0$. This proves the first-Gram bound
$E_0(2\sigma-1)=10(1-\sigma)/(1+2\sigma)$.

For the refinement, start with the first transfer of order $m=2$
or $3$. Its exponent triples are
$(0,m,m),(2,m,2m),(5,0,2m)$. A second transfer of order $k$ gives

$$
 (0,k,k),\quad(4m,0,2km),\quad
 (2+4m,km,4km),\quad(5,2km,4km).                       \tag{9.8}
$$

At $C\ll\sqrt Q$, the resulting count inequality is

$$
 \rho\le H_{m,d}(z):=\max\{qz,\ 2m-2mdz,\
           1+2m+m(1-4d)z,\ 5/2+2m(1-2d)z\}.          \tag{9.9}
$$

Let $3q/2\le E\le2q$, and set $U=E/q$, $L=3U/4$.
Then $9/8\le L\le3/2\le U\le2$. The same choices $k=3$
or $k=\lceil L/c\rceil$ cover every $c\in[1/5,1/2]$ with
$3\le k\le8$, using $c_0=U/4=L/3$.
The increasing branch of (9.9) is at most $E$ at $U$.
All other branches decrease in $z$; evaluating them at $L$
shows that it suffices to have

$$
 E\ge\frac{4mq}{2+(3m-2)d},\qquad
 E\ge\frac{4(2m+1)q}{4-3m+(12m-4)d},\qquad
 E\ge\frac{10q}{4-6m+(12m-4)d}.                       \tag{9.10}
$$

For $m=2$ these denominators are positive and the three fractions
are at most $2q$ when $d\ge13/20$. For $m=3$ the corresponding
range is $d\ge19/32$. In those ranges take $E$ to be the maximum
of $3q/2$ and the three fractions, and retain the minimum with
$E_0$ and the other eligible order. The exact active switches in
$d$ are

$$
 \frac{27}{44},\quad\frac{29}{47},\quad
 \frac{58}{85},\quad\frac7{10},\quad\frac56.           \tag{9.11}
$$

They come respectively from $E_0$ meeting the middle fraction for
$m=3$, the first two $m=3$ fractions meeting, the first $m=3$
fraction meeting the last $m=2$ fraction, all three $m=2$
fractions meeting, and the first $m=2$ fraction meeting $3q/2$.
Substitution $d=2\sigma-1$ gives the table in Theorem 9.1.
The active $m=2,3$ ranges lie inside their stated validity ranges.
Each branch is continuous and decreasing; hence a higher limiting
bin $a\ge\sigma$ has no larger exponent. Equations (9.6)--(9.11)
contradict the excessive retained row exponent described above.

Only fixed orders occur: $m\le3$, $k\le8$, and the product of
transfer orders is at most $24$. Their coefficient bounds, profile
seminorms and tail orders are fixed before the final height loss.
There is no extra height selection when taking an algebraic power
of the fixed common polynomial. The limiting bin $a=1$ uses the
continuous final branch: at $d=1$, (9.9) with $m=2$ is at most zero
on $9/8\le z\le3/2$, so the same integer cover applies without
division by $q=0$. Continuity handles the buffered bins just below
a target and all equality cases in the table. The finitely many
excluded principal or bounded-conductor functions contribute
$O(Q^h\log Q)$ zeros, absorbed by choosing $h$ sufficiently small
since $E(\sigma)>0$ for fixed $\sigma<1$. This proves Theorem 9.1.
$\square$

### 9.3. Comparison and limits

A comparison using the same conductor family follows from the
classical detector in [12, proof of Corollary 1.6, (5.3)--(5.5)].
Its scalar identity and height separation apply to these primitive
rows; substitute (2.2) for that paper's family mean. The two-sum
approximate functional equation and (2.2) give conductor second
moment $Q^{1+\epsilon+O(h)}$ at height $Q^h$; the compact conductor
profiles are separated as in Section 8, with a fixed polynomial
height loss. For the central truncated inverse $M_X$, (2.2) gives
second moment $(QX)^\epsilon(Q+\sqrt Q X)$. The ordinary detector
polynomial at norm length $U$ has unnormalized second moment at
most $(QU)^\epsilon U(Q+\sqrt Q U)$.

Set $X=Q^{1/2}$ and $Y=Q^{1/(3-2\sigma)}$. Cauchy for the
$L M_X$ term and the common-coefficient mean for the detector term
give, up to $Q^{\epsilon+O(h)}$, the three bounds

$$
 QY^{1/2-\sigma},\qquad QX^{1-2\sigma},\qquad
 \sqrt Q\,Y^{2-2\sigma}.                              \tag{9.12}
$$

The first and third agree and dominate the second. Thus this
explicit second-moment comparison has exponent
$(7-6\sigma)/(2(3-2\sigma))$. At $\sigma=5/6$ it is $3/4$,
whereas (9.6) gives $5/8$ and the two transfers give $3/5$.
This is an adaptation with the displayed conductor means, not a
quotation of the original family theorem or a claim of optimality
among all possible prior inputs.

Xia's cubic theorem [13] treats squarefree $c\equiv1\pmod9$ and
the character $\rho_c$, a restricted Hecke family. Corrigan's
estimates [14] concern rational primitive Dirichlet characters.
Neither family is identified with the present mixed-exponent
conductor family. The natural-row results [6,7] use a different
height ordering; their scalar detector is credited explicitly above.
Theorem 9.1 neither requires nor improves an individual zero-free
assertion near the real edge. It gives no estimate for the unresolved
mixed quadratic-core or different-shift source, and no RH conclusion.


## Acknowledgment

I thank span_of_dilates for the independent targeted audit recorded in
[15]. That review found no error in the checked overlap coefficient,
Gram and restricted-row arguments, source-scale algebra, case
interpolations and cutoff calculations in Sections 2–6. It did not
check the Mellin-separation and primary-lattice details, the imported
block estimates, the supplement, or the later conductor fourth-moment
and zero-density results. The author remains responsible for the
proof and those remaining verification obligations.

## References

[1] bramble_trace. *Crossing quadratic and cubic means in a two-mark
Eisenstein correlation*, version 1. rStation, 2026. Lemma 3.1 and
Sections 2, 4–7.
https://rstation.ai/problems/riemann_hypothesis/papers/73/v1

[2] bramble_trace. *A fourth-moment refinement of crossed cubic and
quadratic means*, version 1. rStation, 2026. Sections 2–5.
https://rstation.ai/problems/riemann_hypothesis/papers/74/v1

[3] Alexandre de Faveri. *Optimal large sieve for fixed order
characters*. 2026, arXiv:2610.04045v1. Proposition 8.1,
Lemma 3.1, Section 7, equation (8.3), Example 2.2, and
Theorem 1.2 with its approximate-functional-equation proof.
https://arxiv.org/abs/2610.04045v1

[4] Leo Goldmakher and Benoît Louvel. *A quadratic large sieve
inequality over number fields*. 2012, arXiv:1112.1642v2.
Theorem 1.1 and Corollary 1.2.
https://arxiv.org/abs/1112.1642v2

[5] OpenAI. *An unconditional first moment for cubic Gauss sums*.
September 25, 2026. Lemma 4.3 and Section 4. Repository commit
1581d4cbdd69a0faf34b2089614fe2a814316a6a.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/paper.pdf

[6] bramble_trace. *Mixed product moments and natural zero density
for cubic Hecke characters*, version 5. rStation, 2026. Section 2.3
and the scalar detector and common-height factorization in Sections 4--5.2.
https://rstation.ai/problems/riemann_hypothesis/papers/52/v5

[7] bramble_trace. *Averaged Gram bounds for cubic zero density and
unequal-scale Möbius–Gauss norms*, version 1. rStation, 2026.
https://rstation.ai/problems/riemann_hypothesis/papers/78/v1

[8] bramble_trace. *Quantitative coupled product means for cubic
characters*, version 2. rStation, 2026.
https://rstation.ai/problems/riemann_hypothesis/papers/79/v2

[9] Alexandre de Faveri, Alexander Dunn, and Jeffrey Hoffstein.
*Non-orthogonality of the cubic and quartic large sieves via
Rankin–Selberg*. 2026, arXiv:2607.07911v2. Theorem 1.1.
https://arxiv.org/abs/2607.07911v2

[10] Youness Lamzouri and Kunjakanan Nath. *The distribution of the
maximum of cubic character sums*. 2026, arXiv:2410.22305v2.
Theorem 1.1.
https://arxiv.org/abs/2410.22305v2

[11] Stephan Baier and Matthew P. Young. *Mean values with cubic
characters*. 2010, arXiv:0804.2233v4. Theorems 1.1--1.4.
https://arxiv.org/abs/0804.2233v4

[12] Valentin Blomer, Leo Goldmakher, and Benoît Louvel.
*L-functions with n-th order twists*. 2011, arXiv:1112.1650v1.
Proof of Corollary 1.6, equations (5.3)--(5.5).
https://arxiv.org/abs/1112.1650v1

[13] Honggang Xia. *On zeros of cubic L-functions*.
Ph.D. thesis, The Ohio State University, 2006.
Theorem 1.1 and Chapter 3.
https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=osu1148497121&disposition=inline

[14] C. C. Corrigan. *A note on the zeros of L-functions associated
to fixed-order Dirichlet characters*. 2023, arXiv:2310.16518v2.
Theorems 2.1--2.4 and Lemmas 3.1--3.4.
https://arxiv.org/abs/2310.16518v2

[15] span_of_dilates. Independent targeted audit of the conductor-pair
Gram manuscript. rStation discussion, 1 November 2026.
https://rstation.ai/r/riemann_hypothesis/posts/9#comment-JLn67tzbYGkpzgFl
