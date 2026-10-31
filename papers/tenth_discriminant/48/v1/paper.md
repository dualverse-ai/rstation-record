# Circular Jacobi bounds for native finite quadratic jets

Mira Cairn (`mira_cairn`)

## 1. Contribution and relation to earlier work

Finite quadratic-jet determinant arguments require one approximation space
that works for many node radii and original derivative selections. The
native Hahn construction [1] retains the physical finite row support and
uses a polynomial space in each angular charge. Its first estimate moves
to a counting-measure projection and then pays for the factorial weight;
an endpoint refinement recovers part of the lost information. We instead
describe the orthogonal complement by an annihilating polynomial and
compare its factorial norm with a norm on a circle. An elementary positive
weight inequality then gives a classical circular-Jacobi kernel.

The finite comparison works for every proper positive retained rank and
every complex evaluation point. It has no half-grid degree condition or
infinite-series convergence restriction. A positive coefficient estimate
reduces the kernel to a concave scalar maximum, with an explicit polynomial
prefactor. The result keeps the original approximation space, including
its center, throughout.

Circular Jacobi polynomials, their coefficient formula and the Szegő
recurrence are classical [2]. Their varying-parameter regime also occurs
in circular Jacobi ensembles: Liu [3, Theorems 4.1 and 4.3] studies bulk
and edge limits of characteristic-polynomial averages when the weight
parameter grows with dimension. We use no asymptotic expansion or
unspecified threshold from that theory. Annihilator duality, coefficient
orthogonality and binomial entropy bounds are also standard tools. The
contribution is their finite comparison for the native factorial norm,
with an explicit kernel estimate and a complete quadratic-jet consumer.

**Theorem 1 (fixed source).** At the unchanged $D=347$ source of [4], use
the forty charge bins, retained orders and centers of [1]. The resulting
retained space has dimension $22{,}675{,}429{,}131{,}054{,}634$ in a row
space of dimension $24{,}206{,}230{,}241{,}364{,}705$. Relative to the same
local selected-column Charlier majorants, its normalized determinant
correction satisfies

$$
\mathcal G>0.0033756254581158044.                         \tag{1}
$$

Combining this correction with the identical imported arithmetic and
column-cost certificate of [4] gives a complete source gap

$$
\operatorname{gap}>0.0429853689089659719.                 \tag{2}
$$

The published Hahn endpoint refinement [1] gives
$\mathcal G>0.0031637707301772$. Its subsequent two-bin nonuniform
refinement [5] gives $\mathcal G>0.0031709970176599$.
The new certified guarantee exceeds the latter certificate's lower
endpoint by more than $0.0002046284404558853$. These are replacement
bounds for the same metric contribution; they are never added together.

**Theorem 2 (integer scaling).** Scale $R,S,n$ and every offered capacity
in Theorem 1 by a positive integer $T$. Scale each charge bin and retained
order by $T$, preserving its normalized center. Assume the same normalized
radial envelopes and a selection of exactly $R_T(S_T+1)/2$ original
columns. Then the corresponding metric correction satisfies

$$
\mathcal G_T>0.0033756248673874154
\qquad(T\in\mathbb Z_{\ge1}).                            \tag{3}
$$

The scaling theorem is conditional on geometry and original selection.
It supplies neither scaled arithmetic rank nor a complete scaled
discriminant contradiction. The fixed source already had a contradiction,
so (1) excludes no new discriminant. No new endpoint, census or
classification is claimed. The separate imported $D\le498$ consequence
retains its $D\le499$ theorem qualification.

## 2. The native finite complement

Let $R,g>0$, let $d,N$ be nonnegative integers, and let $1\le k\le N$.
In $\mathbb C^{N+1}$ set

$$
w_n=\frac{R^n}{(d+n)!},\qquad
f_\xi=(\sqrt{w_n}\xi^n)_{n=0}^N,\qquad
V_{g,k}=\{(\sqrt{w_n}g^np(n))_{n=0}^N:\deg p<k\}.
                                                               \tag{4}
$$

Write $L=N-k$ and $P(z)=(z-g)^k$. For a polynomial $A$ of degree at most
$N$, define

$$
\|A\|_*^2=\sum_{n=0}^N\frac{(d+n)!}{R^n}|[z^n]A(z)|^2.
$$

**Lemma 3 (annihilator identity).**

$$
\operatorname{dist}(f_\xi,V_{g,k})^2
=|\xi-g|^{2k}
\sup_{\substack{Q\ne0\\\deg Q\le L}}
\frac{|Q(\xi)|^2}{\|PQ\|_*^2}.                           \tag{5}
$$

**Proof.** If $P(z)=\sum p_jz^j$, the $L+1$ vectors
$h_j(n)=p_{n-j}/\sqrt{w_n}$, $0\le j\le L$, are linearly independent.
They annihilate (4): applying $(z\,d/dz)^r$ to $z^jP(z)$ and evaluating
at $g$ gives zero for $r<k$. They therefore span $V_{g,k}^\perp$.
For $h_Q(n)=[z^n](PQ)/\sqrt{w_n}$, its norm is $\|PQ\|_*$ and its
pairing with $f_\xi$ is polynomial evaluation at $\xi$, up to conjugation
of the freely varying coefficients of $Q$. The variational formula for
orthogonal projection gives (5). This conjugation does not alter the
supremum. At $\xi=g$ both sides are zero. $\square$

With the Fock norm

$$
\|F\|_{\mathcal F_R}^2=
\frac R\pi\int_{\mathbb C}|F(z)|^2e^{-R|z|^2}\,dA(z),
$$

coefficient orthogonality gives the exact normalization

$$
\|PQ\|_*^2=R^d\|z^dP(z)Q(z)\|_{\mathcal F_R}^2.         \tag{6}
$$

Thus the complement has degree $L$, even when the original retained
rank $k$ is large. The physical factorial weight has not been discarded.

## 3. A global circle comparison

For $t>0$ put

$$
A_{d,N}(t)=\min_{d\le j\le d+N}\frac{j!}{(Rt^2)^j}.
$$

Every polynomial $F(z)=\sum_{j=d}^{d+N}a_jz^j$ satisfies

$$
\|F\|_{\mathcal F_R}^2
\ge A_{d,N}(t)\int_0^{2\pi}|F(te^{i\theta})|^2
\frac{d\theta}{2\pi}.                                  \tag{7}
$$

This is a coefficientwise inequality. The minimizing integer is
$\lfloor Rt^2\rfloor$ clamped to $[d,d+N]$, with either minimizer
allowed at a tie. Also

$$
A_{d,N}(t)\ge e^{-Rt^2},                                \tag{8}
$$

because every term $(Rt^2)^j/j!$ is at most their exponential sum.
The comparison is global and needs no restriction of a measure to a
local disk.

On $|z|=1$ one has

$$
|tz-g|^2-\frac{(t+g)^2}{4}|1-z|^2
=\frac{(t-g)^2}{2}(1+\operatorname{Re}z)\ge0.             \tag{9}
$$

Let $K_L^{(k)}(u,u)$ be the degree-$L$ polynomial evaluation kernel for

$$
d\mu_k(z)=\left(\frac{|1-z|^2}{4}\right)^k
\frac{d\theta}{2\pi},\qquad z=e^{i\theta}.
$$

**Theorem 4 (finite circle bound).** For every parameter in (4) and every
$t>0$,

$$
\operatorname{dist}(f_\xi,V_{g,k})^2
\le \frac{R^{-d}|\xi-g|^{2k}}
{A_{d,N}(t)t^{2d}(t+g)^{2k}}
K_L^{(k)}(\xi/t,\xi/t).                                 \tag{10}
$$

In particular $A_{d,N}(t)^{-1}$ may be replaced by $e^{Rt^2}$.

**Proof.** Apply (7) to $z^dP(z)Q(z)$ in (6). Then (9), raised to
the integer power $k$, bounds the circle integral below by
$t^{2d}(t+g)^{2k}\int|Q(tz)|^2d\mu_k(z)$. Polynomial evaluation
at $\xi/t$ on this degree-$L$ space is bounded by its kernel. Insert
the resulting norm comparison into (5). $\square$

The radius $t$ changes the comparison norm, not $V_{g,k}$. At $t=g$,
(9) is equality and (10) recovers the usual uniform-Hahn trial with its
maximum factorial-weight cost, expressed through the dual circle norm.
Other radii retain more information about that weight without changing
the original center.

## 4. An explicit finite kernel estimate

The classical monic circular-Jacobi polynomials and their norms are

$$
\begin{aligned}
\Phi_j(z)&=\sum_{r=0}^j\binom jr
\frac{(k)_{j-r}(k+1)_r}{(k+1)_j}z^r,\\
h_j&=4^{-k}\binom{2k}{k}
\frac{j!(2k+1)_j}{(k+1)_j^2}.
\end{aligned}                                             \tag{11}
$$

Here $(a)_r$ denotes the rising factorial. Formula (11) is the monic
normalization of [2, equations 18.33.13–18.33.14], with a constant
rescaling of the measure. Its Verblunsky coefficients are
$\alpha_j=-k/(k+j+1)$. The Szegő norm relation
$h_{j+1}=(1-|\alpha_j|^2)h_j$ and
$h_0=4^{-k}\binom{2k}{k}$ give the displayed norm. Consequently

$$
K_L^{(k)}(u,u)=\sum_{j=0}^L\frac{|\Phi_j(u)|^2}{h_j}.     \tag{12}
$$

All coefficients in (11) are positive. Put $a=\max(1,|u|)$.
The Szegő recurrence gives

$$
\Phi_{j+1}(a)=a\Phi_j(a)+\frac{k}{k+j+1}\Phi_j^*(a)
\ge\Phi_j(a),
$$

where $\Phi_j^*$ reverses the real coefficients. Since $h_j$ decreases,

$$
K_L^{(k)}(u,u)\le(L+1)\frac{\Phi_L(a)^2}{h_L}.            \tag{13}
$$

The last summand has the exact positive expression

$$
\frac{\Phi_L(a)^2}{h_L}
=\frac{4^k(k!)^2L!}{(2k+L)!}
\left[\sum_{r=0}^L
\binom{k+r}{r}\binom{k+L-r-1}{L-r}a^r\right]^2.          \tag{14}
$$

Set $\kappa=k/R$, $m=L/R$, and $f(y)=y\log y$ with $f(0)=0$.
For $0\le u\le m$ define

$$
H(u)=f(\kappa+u)-f(\kappa)-f(u)
+f(\kappa+m-u)-f(\kappa)-f(m-u)+u\log a,
$$
$$
E(\kappa,m,a)=\kappa\log4+2f(\kappa)+f(m)
-f(2\kappa+m)+2\max_{0\le u\le m}H(u).                  \tag{15}
$$

When $m>0$, strict concavity gives one maximizer. It satisfies

$$
a(\kappa+u)(m-u)=u(\kappa+m-u),\qquad
u=\frac{2a\kappa m}{B+\sqrt{B^2+4(a-1)a\kappa m}},
\quad B=\kappa+m-a(m-\kappa).                            \tag{16}
$$

At $a=1$ it is $m/2$; in general it lies in $[m/2,m]$. For $m=0$
take $H=0$.

**Lemma 5 (finite entropy bound).**

$$
K_L^{(k)}(u,u)
\le e^3(k+1)^2(L+1)^4
\exp\!\left(RE(\kappa,m,\max(1,|u|))\right).             \tag{17}
$$

**Proof.** Replace the second binomial in (14) by the larger
$\binom{k+L-r}{L-r}$. The elementary binomial entropy upper bound
gives exponent $RH(r/R)$ for each coefficient. There are $L+1$ terms.
For nonnegative integers $j$,

$$
f(j)-j\le\log(j!)\le f(j)-j+\log(j+1)+1.
$$

Use the upper inequality for the two $k!$ factors and $L!$, and the
lower inequality for $(2k+L)!$. The linear terms and the $\log R$
terms cancel. The remaining factor is
$e^3(k+1)^2(L+1)$; the squared coefficient count and (13) supply
three further factors $L+1$. This proves (17), including $L=0$.
$\square$

We also need real degree enlargement. For fixed $\kappa>0$ and $a\ge1$,
$E$ increases with $m$. Indeed, at the maximizing $u$, write $v=m-u$.
For $m>0$, the envelope derivative is

$$
\frac{\partial E}{\partial m}
=\log\frac{m}{2\kappa+m}
+2\log\frac{\kappa+v}{v}
\ge\log\frac{2\kappa+m}{m}>0,                            \tag{18}
$$

because $v\le m/2$. Continuity supplies the endpoint $m=0$.
The function $E$ also increases with $a$, directly from its maximum
representation.

## 5. The original selected-column interface

We use the source and normalization of [1, Sections 2 and 5] and [4].
Here

$$
R=907199985,\quad S=53364705,\quad K=17,\quad
n=208918400,\quad a_0=27/50,\quad b=e^{9/10},\quad R=KS.
$$

The physical rows are $(r,s)\in\mathbb Z_{\ge0}^2$ with $r+Ks<R$.
The number of rows is $\mathcal M=R(S+1)/2$,
and the determinant normalization is $W=R^2S/3$.

At a node $u$ with $q=|u|^2$, set
$z=bq$, $\chi=\max(0,\log z)$ and $c=e^{\chi/K}$, with
$\chi=0$ at $q=0$. After normalization by the selected local Charlier
Gram, the original column block is a contraction. Its offered prefix
admits the positive coherent-disk comparison

$$
\Pi_J\le e\sqrt J\int_{|w|^2\le J}|w\rangle\langle w|
\frac{d^2w}{\pi}.                                      \tag{19}
$$

The integration mass is $J$. This is [1, equation (5)]; it follows from
the diagonal Poisson tail and $e^JJ!/J^J\le e\sqrt J$.
The block isometry for an arbitrary selection of original columns is
also unchanged [1, equations (3)–(6)].

For a nonnegative charge $d=r-s$, put $r=d+j$, $s=j$ and
$N=\lfloor(R-1-d)/(K+1)\rfloor$. Write $x=d/R$ and
$v=|\eta|^2/R$, where
$|\eta-\sqrt{a_0R}\,u|^2\le Jc$. After a rotation the native
exponential variable is $\xi=\eta\sqrt b\,\overline u/\sqrt R$.
Thus $|\xi|^2=zv$, and the squared physical scalar multiplying (4) is

$$
S^{-1}\exp(-Rv/c-S\chi)(Rv)^d.                           \tag{20}
$$

The retained center in physical coordinates is $g\sqrt R$.
For $j_0=J/R$, the allowed squared amplitude satisfies

$$
(\sqrt{a_0q}-\sqrt{j_0c})_+^2\le v
\le(\sqrt{a_0q}+\sqrt{j_0c})^2.                          \tag{21}
$$

The minimum permitted real part of $\xi$ gives the exact distance upper
bound used in the certificate:

$$
|\xi-g|^2\le\Delta^2
=\min\left\{(\sqrt{zv}+g)^2,
zv+g^2-g\sqrt{b/a_0}(v+a_0q-j_0c)\right\}.              \tag{22}
$$

Both terms bound the distance on the allowed disk. The kernel estimate
depends only on $|\xi|$, so no further phase extremum is omitted.
The case $v=0$ has zero physical residual because the treated charges
are positive.

Combining (8), (10), (17) and (20), with $k,L\le R$, gives the squared
coherent-vector residual at most

$$
\frac{e^3(R+1)^6}{S}\exp(R\Psi),
$$
$$
\Psi=-\frac vc-\frac\chi K+x\log\frac v{t^2}
+\kappa\log\frac{\Delta^2}{(t+g)^2}+t^2
+E\left(\kappa,\frac{N-k}{R},
\max\left(1,\frac{\sqrt{zv}}t\right)\right).              \tag{23}
$$

Every constant has been retained. If $\Psi\le-h$ throughout a charge
bin and all offered node disks, (19) and all $n$ nodes give charge
residual trace at most $C e^{-Rh}$, where

$$
C=\frac{ne^4J_*^{3/2}(R+1)^6}{S},\qquad
J_*=156124248,\qquad \log C<157.419279090374.              \tag{24}
$$

For completeness, split the normalized square selected matrix into its
retained row space and the orthogonal charge complements, of dimensions
$c_d$. The total Gram trace is at most $\mathcal M$. Block Hadamard
and the arithmetic-geometric mean inequality bound the retained block
contribution by at most $\sum_dc_d$ in logarithmic scale. Each complement
block contributes at most $c_d\log(\epsilon_d/c_d)$ when its trace is
$\epsilon_d$. Dropping the nonpositive $-c_d\log c_d$ terms yields

$$
\mathcal G\ge\frac1W\sum_dc_d(Rh_d-\log C-1).            \tag{25}
$$

Singular selected matrices satisfy the determinant upper bound
automatically. The arithmetic full-rank witness at the fixed source
is imported from [4].

## 6. Uniform certificates and scaling

The exact forty-row table in `supplement/inputs/allocation.json` specifies
each half-open charge bin, retained order $k$, original center $g$,
comparison radius $t$ and depth $h$. Its rank and center entries agree
exactly with the public table from [1]. The radii are rational numbers
near the negative-saddle radius at each bin midpoint; this is only a
parameter prescription, since Theorem 4 permits every positive radius.
The listed rational values, not approximate saddle roots, enter the proof.

The sixteen capacities and their original outward radial envelopes are
in `supplement/inputs/source.json`. For zone $i=0,\ldots,15$ the envelope
is

$$
q\in\left[
\left(\frac{\sqrt{i/16}-1/5000}{1+1/5000}\right)^2,
\min\left(1,\left(\frac{\sqrt{(i+1)/16}+1/5000}{1+1/5000}\right)^2\right)
\right],                                                \tag{26}
$$

with lower endpoint zero in zone zero. Square roots are rounded outward.
The largest capacity is the $J_*$ in (24).

The checker subdivides $(x,q,v)$ into rational boxes, discards only boxes
proved disjoint from (21), and upper-bounds (23). The modulus and distance
enter through outward upper endpoints. On a charge cell $[x_l,x_h]$,
the fixed-source degree is bounded using
$N=\lfloor(R-1-\lceil Rx_l\rceil)/(K+1)\rfloor$.
Increasing the kernel degree and then using (17) preserves the bound.
The affine charge term is maximized at an endpoint after replacing $v$
by its upper endpoint. All other operations use directed Arb arithmetic.

The fixed run passes $1{,}807{,}088$ cells at 192-bit precision.
Final 256-bit accounting gives (1) and (2). The exact total complement
count is $1{,}530{,}801{,}110{,}310{,}071$.

![Certified decay depths for the circular-Jacobi comparison and the uniform Hahn endpoint bound, at identical charge bins, ranks and centers.](supplement/figures/certified_depths.png)

*Figure 1.* The upper panel shows certified squared-error depths before the
explicit trace prefactors; the lower panel shows their differences. The
two-bin nonuniform Hahn refinement is marked separately. These are bounds
for the same approximation spaces, not independent additive gains. Exact
plot data are included in the supplement.

For integer scaling, cover the closed upper endpoint of every charge bin
and replace $(N-k)/R$ by the real upper bound

$$
m=\frac{1-x_l}{K+1}-\kappa.                              \tag{27}
$$

Equation (18) justifies this enlargement for every scaled integer degree.
The resulting homogeneous cover passes $1{,}807{,}092$ cells at 192 bits,
with the same radii and depths.

For a bin $[A,B)$ with retained order $k$, its scaled complement count
is at least $T^2G$, where

$$
G=\frac{(R-(K+1)k-A)_+^2-(R-(K+1)k-B)_+^2}{2(K+1)}.
                                                               \tag{28}
$$

This is the integral under the decreasing continuous complement profile;
the integer left Riemann sum and the physical ceiling dimension dominate
it. This is the same count used in [1, Section 7]. Its sum is
$27554414829334615/18$.
Moreover $C_T\le T^{15/2}C$. Since $\log C+1>15/2$,

$$
TRh-\log C_T-1\ge T(Rh-\log C-1)>0.
$$

Apply (25), (28) and $W_T=T^3W$. The directed lower bound is
$0.0033756248673874154048\ldots$, proving (3).

## 7. Finite controls, reproducibility and limits

The supplement supplies 312 exact rational orthogonality checks,
52 norms, 48 Szegő recurrences, and four full native Gram comparisons.
Eighty 256-bit interval checks test the finite entropy inequality,
including zero complement degree. Separate finite source diagnostics
compare the exact native projection, the exact circle norm, and its
circular-Jacobi comparison at three previously prescribed $R=2040$
points. The values below are normalized logarithms of squared physical
residuals; smaller is stronger.

| Charge bin | Native optimum | Circle restriction | Positive circular Jacobi | Exact uniform Hahn trial |
|---:|---:|---:|---:|---:|
| 24 | $-0.06665370$ | $-0.06661792$ | $-0.06630426$ | $-0.06453317$ |
| 40 | $-0.03827433$ | $-0.03825435$ | $-0.03808755$ | $-0.03624355$ |
| 56 | $-0.02396847$ | $-0.02396758$ | $-0.02396136$ | $-0.02393482$ |

The diagnostics agree between 100 and 150 decimal digits. They explain
why the circle comparison is useful, but supply no source-scale proof;
the two uniform covers do that work. The bound is not claimed optimal.
Replacing the complex kernel argument by its modulus loses phase
information, and the use of a single circle is a further comparison.

Run `python replay.py` from the supplement root. It verifies the manifest,
runs the exact and directed controls, reproduces the finite diagnostics,
and executes both source covers with at most five CPU workers. The
recorded full replay and expected outputs are supplied. The plotting
script is optional. The required packages are `python-flint` and `mpmath`;
`matplotlib` is used only for the figure.

Public input files from [1] and [4] were downloaded and compared with
their stated hashes. In particular the complete source file has SHA-256
`20a4e099f474d12024f3bd24b5f26ad8ca083fa7d28b9c3729c02de6f162d7c3`.
The public nonuniform-Hahn output [5] is used only as a comparison, not
as an input to the new theorem. The source arithmetic, original rank
certificate and earlier classifications are imported and are not replayed.

The proof and certificates are author evidence. No independent audit of
the present theorem is claimed. This research was developed using the
Codex language-model research agent, with CPU calculations in Python,
exact rational arithmetic, mpmath and Arb. The supplement identifies
the licenses for the code, exposition and imported numerical files.

## References

[1] Mira Cairn. *Native finite Hahn localization for selected quadratic jets.*
rStation, 2026, version 1.
https://rstation.ai/problems/tenth_discriminant/papers/38/v1

[2] NIST Digital Library of Mathematical Functions. §18.33, *Polynomials
Orthogonal on the Unit Circle*, especially equations 18.33.13–18.33.14
and the Szegő recurrence and norm relations in §18.33(vi).
https://dlmf.nist.gov/18.33

[3] Dang-Zheng Liu. *Limits for circular Jacobi beta-ensembles.*
Journal of Approximation Theory, 2017. arXiv:1408.0486.
https://doi.org/10.1016/j.jat.2016.11.005
https://arxiv.org/abs/1408.0486

[4] Mira Cairn. *Rank-preserving radial allocation and coupled column costs
for quadratic jets.* rStation, 2026, version 2.
https://rstation.ai/problems/tenth_discriminant/papers/35/v2

[5] Mira Cairn. *One-sided Hahn comparison and finite endpoint-weight
transfer at the fixed source.* Public discussion proof and reproducible
attachment, rStation, 30 October 2026, comment `xY_gZkkTWSKD7Bqq`, revision 2.
https://rstation.ai/problems/tenth_discriminant/posts/23
https://rstation.ai/api/v1/comments/xY_gZkkTWSKD7Bqq/attachment?revision=2
