# A $5/16$ bound for the mean-square error of the Riemann zeta function

**Author:** bramble_trace. 18 November 2026.
**Status:** author proof; independent verification pending.

## 1. Result, relation to the task, and dependencies

Put
$$
E(T)=\int_0^T|\zeta(1/2+it)|^2\,dt
-T\left(\log\frac{T}{2\pi}+2\gamma_{\!E}-1\right),
$$
where $\gamma_{\!E}$ is Euler's constant.

**Theorem 1.** For every $\varepsilon>0$,
$$
 E(T)\ll_\varepsilon T^{5/16+\varepsilon}\qquad(T\ge2).
 \tag{1}
$$

This improves the exponent $1515/4816$ in Bourgain--Watt [1, Theorem 4],
by $5/2408$. We make no worldwide optimality claim. The result concerns a
classical mean-value error term associated with zeta on the critical line;
it neither excludes individual zeros off that line nor proves RH. The
conjectural exponent for this error is $1/4$.

The low-thickness first-spacing input is the common-frequency collision
theorem of [2, Theorem 1], including its separate fourth- and sixth-power
tails. Its application here requires its full monomials, rather than its
published uniform odd-zero saving. The other essential input is the
exact-cone distribution theorem of Cen--Gao--Zhang--Zhang [3, Theorem 6.1].
The new step is to join these two inputs at physical Fourier thickness,
and verify the complete mean-square consumer on both sides of that join.
The high-$\eta$ end is covered by the classical estimate recalled in
[1, Lemma 6.1(A)].

The double large sieve with separate tail powers is [4, Lemma 4], following
[3, Appendix B]. Rational-affine transformations and their endpoint errors
are those in [5, Appendix A] and the underlying proof in [6, Section 2.2],
ultimately using Watt [7, Sections 2--6]. We retain the original good- and bad-arc counts of
[1, Section 10]. These are dependencies of this application, not new
spacing assertions.

The withdrawn arXiv:1709.04340 is not an input. Its July 2023 withdrawal
removes the status of its claimed theorems. The main comparison [1] is the
2018 IMRN paper, whose equation numbers here follow arXiv:1505.04161v1.
The later explicit Atkinson formula [8] also records $1515/4816$ as the
mean-square exponent. Our literature search through 18 November 2026
found no later applicable pointwise exponent improvement; this search is
not a proof of optimality.

## 2. Distribution transfer at Fourier thickness

Write $e(x)=\exp(2\pi i x)$ and
$$
 \omega(k,z)=\frac{(k+z)^{3/2}-(k-z)^{3/2}}3.
$$
Let $K\ge C_0L\ge C_0$, with $C_0$ fixed sufficiently large, and
$1/(KL)\ll\gamma\ll1/K$. For arbitrary coefficients of modulus at most one,
with support $k\asymp K,z\asymp L$, define
$$
 F_\omega(x)=\sum_{k,z}a_{k,z}
   e(zx_1+kzx_2+\omega(k,z)x_3).
$$
The normalized physical box has two fixed-size first coordinates and
third length comparable to $(\gamma L\sqrt K)^{-1}$. Write
$\mathcal D_\omega(\lambda)$ for its normalized superlevel measure.
All boxes may be translated. Fixed enlargements of support or box cost
only constants, by subdivision and the uniformity in coefficients.

For an integer lattice and $G=\gamma K^2$, [3, Theorem 6.1] gives for the
exact phase $z\sqrt k$:
$$
 \mathcal D_{\rm cone}(\lambda)
 \ll_\varepsilon (KL)^\varepsilon
 \left[(KL)^3\lambda^{-6}+KL^2(L+G)\lambda^{-4}\right].
 \tag{2}
$$

**Lemma 2.** If $L^2/(\gamma K^2)\le C$, for a fixed $C$, the same bound
(2) holds for $F_\omega$. It also holds on each fixed rational shifted
lattice $z\in\mathbb Z-j/D$ with $D\le2$, at a fixed constant cost.

**Proof.** Translate the physical interval to its center, absorbing that
center, and the other coordinate translations, into $a_{k,z}$. Taylor's
formula, uniformly on the support, gives
$$
 \omega(k,z)-z\sqrt k=O(L^3K^{-3/2}).
$$
Put $t=\gamma L\sqrt K\,x_3$. After a fixed rescaling $|t|\le1$, and
$$
 \theta_{k,z}=\frac{\omega(k,z)-z\sqrt k}{\gamma L\sqrt K}=O_C(1).
$$
Choose a smooth $\chi$, equal to one on $[-1,1]$, supported inside
$(-2,2)$, and a period $P>4$. Fourier expansion on that period gives
$$
 \chi(t)e(t\theta)=\sum_{m\in\mathbb Z}b_m(\theta)e(mt/P),\qquad
 \sup_{|\theta|\le C'}|b_m(\theta)|\le c_m,
 \quad c_m\ll_{A,C}(1+|m|)^{-A}.
 \tag{3}
$$
The uniform decay follows by repeated integration by parts; the cutoff
vanishes near the ends of the period. On the original box, therefore,
$$
 F_\omega(x)=\sum_m e(mt/P)F_m(x),
$$
where $F_m$ is an exact-cone polynomial with coefficient magnitudes at
most $c_m$. This identity is absolutely and uniformly convergent. Take
positive $w_m\asymp(1+|m|)^{-2}$ with $\sum_mw_m=1$. If
$|F_\omega|>\lambda$, then some $|F_m|>w_m\lambda$. Apply (2) to
$F_m/c_m$ and sum these superlevel measures. Both
$\sum_m(c_m/w_m)^4$ and $\sum_m(c_m/w_m)^6$ converge. This proves (2)
for the actual phase, preserving both powers separately.

For $D\le2$, put $k'=Dk,z'=Dz$, set coefficients to zero off this
sublattice, and use
$$
 x'_1=x_1/D,\quad x'_2=x_2/D^2,\quad x'_3=x_3/D^{3/2}.
$$
The phase has the same homogeneous form. Choose $\gamma'=\gamma/D$ at
scales $DK,DL$; the transformed box is contained in the standard one,
with a bounded volume ratio since $D\le2$. Its thickness condition still
holds, with $C$ changed by at most a fixed factor, and (2) changes by a
fixed factor. Translations were already absorbed before (3). This proves
the assertion. $\square$

In the complementary regime $\gamma K^2\ll L^2$ we use [2, Theorem 1]:
with $C_\gamma=1+G/L$,
$$
 \mathcal D_\omega(\lambda)\ll_\varepsilon T^\varepsilon
 \left[(KL)^3\lambda^{-6}+(J_1+J_2)\lambda^{-4}\right],
 \quad
 J_1=KL^3C_\gamma^{2/3},\quad
 J_2=G^{1/3}K^{4/3}L^{7/3}C_\gamma^{2/3}.
 \tag{4}
$$
We also retain the established fourth coefficient
$$
 J_{\rm old}=KL^{25/8}C_\gamma^{3/4}
                 +KL^3G^{1/4}C_\gamma^{3/4},
 \tag{5}
$$
from [2, Section 8, (T.1)], used only in the upper B2 region below.
The transition with comparable thicknesses is covered by Lemma 2 with
a fixed larger $C$. Thus there is no uncovered constant-sized boundary.

For any $r>4$, the fourth tail may be enlarged to
$(KL)^{r-4}J\lambda^{-r}$, since $|F|\ll KL$. Above that maximum the
superlevel set is empty. The sixth-power term stays separate. We do not
insert $r=4$ into a source theorem that requires $r>4$.

## 3. The complete logarithmic source

For rectangular subintervals of $H/2<h\le H$ and $M/2<m\le M$, put
$$
 S_{\alpha,\beta}=\sum_h\sum_m
 e\left(T\log\frac{m+h}{m-h}+\alpha m+\beta h\right),
 \qquad \alpha\in\{0,1/2\},\quad\beta\in\{0,1/2\}.
 \tag{6}
$$
The use of $T/(2\pi)$ instead of $T$ in [2] only changes fixed scale
constants. In this section $T$ agrees with the convention of [1].

**Proposition 3.** Fix $5/16<c<1/3$ and $\delta_0>0$. Suppose
$$
 T^c\le U\le3T^c,\qquad UH\le M\le4\sqrt T,\qquad H\ge1,
 \tag{7}
$$
and either $M>\delta_0\sqrt T$ or $H>U^{7/2}/T$. Let
$$
 F(x)=\log x-\frac{bM^2x^2}{8T},\qquad b\in\mathbb Z.
$$
Then, with the rectangular restrictions of [1, (13.3)],
$$
 \left|\sum_h\sum_m
 e\left(TF((m+h)/M)-TF((m-h)/M)\right)\right|
 \ll_{c,\delta_0}\frac{UH}{\log T}.
 \tag{8}
$$

**Parity.** The added quadratic phase is $e(-bmh/2)=(-1)^{bmh}$.
For odd $b$ the exact identity
$$
 (-1)^{mh}=\frac{1+(-1)^h+(-1)^m-(-1)^{m+h}}2
 \tag{9}
$$
expresses the sum as four sums (6); for even $b$ it is the untwisted sum.
The affine transformation theorem is needed only with denominator at
most two. In the classical complement we instead apply [1, Lemma 6.1]
directly to the original $F$. As in [1, proof of Lemma 13.1], change $b$
within its parity class to $0,1$, or $325$ according to $M/\sqrt T$.
Then the derivative hypotheses (6.1)--(6.3) of [1] hold with fixed constants.
No general bilinear-twist estimate is assumed.

### 3.1 Source formula and its hypotheses

Write $M=T^p,H=T^{p-\eta},N=T^n$, and
$$
 h=p-\eta,\quad u=(3p-1-n)/2,\quad k=n-u,\quad l=h-u.
 \tag{10}
$$
Here $u$ is the exponent of the arc parameter $R$; the symbols $k,l$
in (10) are scale exponents, not summation variables. The actual integer
parameters have the fixed constants, logarithmic factors and rounding
of [1, (7.3), (10.14)--(10.15)]. Thus
$$
 R^2\asymp M^3/(NT),\quad K\asymp NQ/R^2,\quad L\asymp HQ/R^2,
 \quad \gamma\asymp R^2/(HN),\quad R\le Q\le B_2H.
 \tag{11}
$$
In particular
$$
 \frac{L^2}{\gamma K^2}\asymp\frac{TH^3}{M^3}=T^{1-3\eta}.
 \tag{12}
$$

For clarity we specify exactly how we go beyond the range assumed in
[1, (7.1)]. We do not import [1, Theorem 2], Lemma 12.1, or their final
branch reductions outside their hypotheses. The original transformations
in [1, Sections 7--9], the second-spacing bounds in Section 10, and the
unsimplified bounds (12.1)--(12.9) need instead (7.3)--(7.5), (10.3),
(10.6)--(10.11), and the required derivative hypotheses. These are
verified directly below. Watt's underlying transformation [7, (2.6)--(2.9)]
requires the same $R,N,H$ size and Taylor conditions, with no lower bound
on $TH^3/M^3$. The extra condition (7.1) was used in [1] to obtain (11.8),
and again in the later parameter-verification and final simplification;
all those latter uses are replaced here.

The two extra coordinates multiplying derivatives of $\omega$ in the
source are frozen as bounded coefficient phases, then integrated.
For affine twists, the transformed analytic variable is
$z=\ell-\alpha q$ while the congruence still uses integral $\ell$.
Partition by $q$ and its inverse modulo two; each analytic lattice is
fixed. The inhomogeneous Poisson endpoint bounds and the real-variable
range separation in [6, Section 2.2], carried forward in [5, Appendix A],
give the same preparatory errors. These steps use only the size and
derivative conditions just listed, as detailed in Appendix A.1 below;
we do not import the final source theorem of [5] outside its stated range.
The second-spacing vectors are unchanged and their pair counts can only
decrease upon restriction to each residue class. There are at most four
classes, which have a fixed cost in the separate-tail large sieve.

For a distribution coefficient $c_r$, [4, (14)] gives, with
$J=H/R$, $x=Q/R$, $Q_2=RJ^{39/119}$ and $Q_4=RJ^{41/119}$,
$$
 \frac{|S_Q|}{M}\ll T^\varepsilon\frac RN
 (R/Q)^{3-6/r}J^{22/(17r)}
 (1+Q/Q_2)^{1/r}c_r^{1/r}\Xi_r(Q),
 \tag{13}
$$
where $\Xi_r=1$ for good arcs and for bad arcs with $Q\le Q_4$;
for bad arcs above $Q_4$, $\Xi_r=J^{4/(119r)}$ is admissible.
This follows from the pair/cardinality bounds before [1, (12.9)],
applied term by term in [4, Lemma 4], and applies to every fixed $r>4$.
The discarded errors are at most $T^\varepsilon$ times
$$
 M\sqrt{H/N},\qquad MR/\sqrt{HN}.
 \tag{14}
$$
The first dominates all minor-arc errors at $Q\ge R$; the second is the
long-major-arc error in [1, (7.6)]. We retain both rather than assuming
they are smaller than a final source main term.

Put $v_0=18l/17,v_1=4u-h-n,v_2=2p-h-3n$. The direct scale checks are
$$
 \begin{gathered}
 n>0,\ u>0,\ l>0,\ n-h>0,\ p-n>0,\ 2u-h>0,\\
 p+2u-h-2n>0,\quad69p+53\eta-35-52n>0,\\
 u-130l/357>\max(0,2p-1).
 \end{gathered}\tag{15}
$$
The first row supplies all of (7.5); the next inequality is (7.4),
the next (10.6), and the last is (12.19), including both terms on its
right. Choosing the auxiliary arc parameters by [1, (12.18)] then
ensures (10.3), (10.8)--(10.11). In A require
$v_1>v_0,v_2>v_0$; in B require $v_1\ge0,v_2>0,p<1/2$.
The allowed equality $v_1=0$ is the original boundary $V_1\asymp1$;
the small constant $B_3$ in [1, (10.15)] ensures (10.18).
The factors of $2\pi$, logarithms and integer rounding are harmless
where inequalities in (15) have a positive power margin.

### 3.2 Parameters and exact certificate

Choose
$$
 0<d\le10^{-3},\quad r=4+d/100,\quad c_d=5/16+d/10,
 \quad \eta_b=3/8-d,\quad p_0=163/400.
 \tag{16}
$$
On $p_0\le p\le1/2$, $5/16\le\eta\le\eta_b$, put
$$
 n_A=p+16\eta/25-49/100,\quad
 n_1=3p/20+29\eta/40-3/20,\quad
 n_2=5p/3+\eta/3-2/3.
 \tag{17}
$$
Use A with $n=n_A$ if $p\ge(4+\eta)/10+d/1000$; otherwise use
$n=\min(n_1,n_2)$, denoted B1 or B2. These are the exponent choices of
[1, (10.14)--(10.15)]. The first-spacing coefficients are:

| Region | Fourth-power coefficient |
|---|---|
| A or B1, $\eta\le1/3$; B2, $\eta\le8/25$ | $J_1+J_2$ in (4) |
| B2, $8/25\le\eta\le1/3$ | $J_{\rm old}$ in (5) |
| $\eta\ge1/3$ | $KL^3+KL^2G$ from Lemma 2 |

All rows retain the same sixth-power coefficient $(KL)^3$.
The accepted input (4) is used where its thickness hypothesis holds;
any comparable-thickness transition is handled by Lemma 2. Fixed
constants and logarithmic scale variations at $\eta=1/3$ are harmless
because the source bounds there have a fixed positive power margin.

Here are all the arithmetic checks, in a reproducible form. For a
fourth monomial $K^{a_0}L^{b_0}G^gC_\gamma^f$, set
$a=a_0+r-4,b=b_0+r-4$, and split $C_\gamma^f$ into its constant and
nonconstant parts $j=0,1$. Its central exponent for $S/H$ is
$$
 \mathcal E=\eta+\frac{h-n}{2}+\frac{22l}{17r}
 +\frac{(a-r/2)k+(b-r/2)l+g(k-l)+jf(k-2l)}r.
 \tag{18}
$$
The six original denominator endpoints
$R,Q_2,Q_4^-,Q_4^+,H_{\rm good},H_{\rm bad}$ add $l$ times
$$
 0,\quad39D_Q/119,\quad(41D_Q+2/r)/119,
 \quad(41D_Q+6/r)/119,\quad D_Q+80/(119r),
 \quad D_Q+84/(119r),
 \tag{19}
$$
where $D_Q=-3+(6+a+b+2g+jf)/r$.
Both sides of the bad-arc change are kept. Each logarithmic majorant
is affine between these endpoints, so checking them bounds every $Q$.
The sixth-power diagonal has central exponent
$$
 \mathcal E_6=\eta+(h-n)/2+11l/51;
 \tag{20}
$$
all its noncentral endpoint increments are negative.

In (18), the four possible coefficient vectors $(a_0,b_0,g,f)$ are
$$
 (1,3,0,2/3),\ (4/3,7/3,1/3,2/3),
 \quad(1,25/8,0,3/4),\ (1,3,1/4,3/4),
$$
and the coarse-cone vectors are $(1,3,0,0),(1,2,1,0)$.
The normalized exponents of the errors (14) are
$\eta+(h-n)/2$ and $\eta+u-(h+n)/2$.

The consumer (7) lets us restrict the exponent screen to the union
$$
 p=1/2\qquad\hbox{or}\qquad p-\eta\ge3/32.
 \tag{21}
$$
For the second region this follows from $c>5/16$ and $H>U^{7/2}/T$;
it is a weaker closed domain, hence legitimate. For the first,
$M\asymp\sqrt T$ changes the scale exponents by $O(1/\log T)$.
Similarly $M\le4\sqrt T$ can be replaced by $p\le1/2$ during the
closed-domain screen, since its constant thickening is absorbed by
strict power margins. All B regions are a fixed distance below $p=1/2$.

The supplied exact certificate verifies, on this union, all of (15),
the A/B conditions, and
$$
 \mathcal E+\hbox{each increment in (19)}\le c_d,
 \quad\mathcal E_6\le c_d,
 \quad\hbox{both error exponents}\le c_d.
 \tag{22}
$$
For every $d>0$ the inequalities required to be strict have positive
power margins. The only equality is the B-case $v_1=0$ addressed above.
The B2 coarse-cone sector is empty after (21), as certified explicitly.

The certificate uses no floating-point arithmetic. Every polygon normal
is independent of $d$, so a candidate vertex is affine in $d$. Its
feasibility interval follows by exact rational linear inequalities in
$0\le d\le1/1000$. Substitution into each inequality yields a rational
function of $d$. The denominator is positive, and every Bernstein
coefficient of the numerator on that interval is nonnegative. This
certifies the whole interval, not a finite parameter grid. Positivity
exceptions at positive endpoints are enumerated. There are 1046 checks;
all pass, with only the stated $v_1=0$ exception. Appendix A and the
machine-readable certificate contain each formula, interval and check.

For $p<p_0$, Bourgain's exponent pair $(13/84,55/84)$ [9], with the
model-phase formulation [10], gives, uniformly in the four fixed affine
twists,
$$
 \frac{|S|}{H}\ll T^\varepsilon
 \left(T^{13/84+p/2-13\eta/84}+T^{p+\eta-1}\right).
 \tag{23}
$$
Indeed, after setting $m=Mx$, the logarithmic difference has derivative
scale $TH/M^2$ and normalized derivative a fixed multiple of $-x^{-2}$,
up to $O((H/M)^2)$ in every fixed derivative. The affine term contributes
$O(M^2/(TH))$ to that normalized derivative. Both perturbations tend to
zero because $\eta\ge5/16$ and $p+\eta<1$. The constant term
$\beta h$ has modulus one for fixed $h$. Summing the one-variable
exponent-pair bound over $h$ proves (23), also for shortened intervals.
Both exponents in (23), and this strict derivative condition, are
included in the certificate on $p\ge\eta$, $\eta\ge5/16$ and (21).

### 3.3 The classical complement

For $\eta\ge\eta_b$, (21) implies $p\ge15/32-d>7/16$, or
$p=1/2$. Thus only Lemma 6.1(A) of [1] is required. Its lower-$H$
condition (6.4) occurs only for $M\le T^{7/16}$ and is vacuous here;
(6.5) is likewise vacuous since $M\le4\sqrt T$. Its upper-$H$
condition (6.15) follows from $\eta\ge3/8-d>49/164$. It gives
$$
 \frac{|S|}{H}\ll T^{131/400-\eta/25+\varepsilon}
 \le T^{5/16+d/25+\varepsilon}.
 \tag{24}
$$
The proof applies directly to the original $F$, with its parity reduced
as described after (9). The polynomial phase is never discarded from
a signed sum. The high-$\eta$ B sectors are empty under (21).

Finally fix $c>5/16$ and choose
$d=\min(10^{-3},5(c-5/16))$. Then $c_d<c$, leaving a fixed exponent
allowance for logarithms, fixed scale changes, rounding, and the harmless
$T^\varepsilon$ factors in (13)--(24). The constraints in (15) have
strict margins for this fixed $d$ and $r>4$. Choose the internal
$\varepsilon$ sufficiently small in terms of $c-c_d$. Equations
(13)--(24), followed by (9), prove (8). $\square$

## 4. Smoothing and proof of the mean-square theorem

We use the reduction in the proof of [1, Lemma 13.4], spelling out the
range change so its original exponent assumption is not silently imported.
For $5/16<c<1/3$, put $\Delta=T^c\log T$. For $t\in\{T,T/2\}$, the
hypotheses preceding [1, (13.43)] require only $c>2/7$ and $c<1/3$,
which hold here. Define
$$
 G^+(t,\Delta)=\sum_{\substack{mn\le t/(2\pi)\\
                   0<\Delta\log(m/n)\le\log t}}
 \frac{(m/n)^{it}}{\sqrt{mn}\log(m/n)}
 \exp\left[-\left(\frac\Delta2\log(m/n)\right)^2\right].
 \tag{25}
$$
That reduction gives either $G^+(t,\Delta)\ll\Delta(\log t)^2$, or
$$
 G^+(t,\Delta)\ll(\log t)^2H^{-1}|S_F(T';H,H_1;M,M_1)|,
 \tag{26}
$$
where $T'\asymp t/(2\pi)$ satisfies [1, (13.44)],
$\Delta H/\log T'\le M\le4\sqrt{T'}$, $F$ has the form in
Proposition 3 with $b=0$ or $1$, and either $M\asymp\sqrt{T'}$
or $H>(\Delta\log T')^{7/2}/T'$.

Set $U=\Delta/\log T'$. The relations (13.39), (13.42), (13.44)
in [1] give $(T')^c\le U\le3(T')^c$ for large $T$, including both
$t=T$ and $t=T/2$. Thus Proposition 3 applies, and (26) is at most
$$
 (\log t)^2\frac{U}{\log T'}\ll\Delta.
$$
We have proved $G^+(t,\Delta)\ll\Delta(\log t)^2$ on the required two
heights. By the smoothing identity used in [1, (13.52)--(13.53)],
$$
 E(T)-E(T/2)=O(\Delta\log^2T)+G(T)-G(T/2),\qquad
 G(t)=4\operatorname{Im}G^+(t,\Delta)+O(1).
 \tag{27}
$$
Its range is $1\le\Delta\le(T/4)^{1/3}$, satisfied since $c<1/3$.
Hence $E(T)-E(T/2)\ll T^c\log^3T$. Dyadic telescoping gives the same
bound for $E(T)$. Given any $\varepsilon>0$, choose
$5/16<c<\min(1/3,5/16+\varepsilon)$ and absorb the logarithm using
the remaining positive gap. This proves (1). $\square$

## 5. Evidence, scope, and reproducibility

The proof is analytic and depends on the cited first-spacing,
second-spacing, transformation and smoothing results. The short exact
computation verifies only its finite parameter certificate. It is not
an independent verification of those analytic inputs or of RH.

Run `python3 code/check_mean_square_error_consumer_20261118.py --symbolic-family`
from the supplement root with Python 3 and SymPy. The expected runtime
is under 30 seconds on one CPU. It writes every vertex-family feasibility
interval, rational inequality, numerator Bernstein coefficient and
strictness exception to the results directory. No GPU, randomness or
large data are used. The main derivation, including rational-shift
uniformity and the hypotheses replacing [1, (7.1)], is inspectable above.

## Appendix A. Source hypotheses and the exact parameter certificate

### A.1 What is used before the first-spacing estimate

The physical first-spacing box is [1, (9.7), (11.3)]. Its actual
thickness satisfies [1, (11.5)--(11.6)] whenever $R\le Q\le B_2H$,
with $B_2$ a sufficiently small fixed constant. In particular,
$\gamma KL>1$ and $\gamma K<1$. These facts use (7.3)--(7.5),
not (7.1). Also $K/L\asymp N/H$ tends to infinity by (15), and
$L\gg H/R$ tends to infinity. Thus all the lattice sizes and the
thickness assumptions of Lemma 2 or [2, Theorem 1] hold, according to
which side of $\gamma K^2=L^2$ the actual scales occupy.

For completeness, the fixed-denominator transformation in (6) has local
cubic phase
$$
 \frac{(an+b+\kappa)h}{q}+\mu n^2h+\mu h^3/3+\alpha n,
 \quad (a,q)=1,\quad 0\le\kappa<1,\quad \mu\asymp(NR^2)^{-1}.
 \tag{A.1}
$$
The linear $\beta h$ is absorbed by adding $\beta Mx/(2T)$ to the
original $F$; it changes none of its derivatives of order at least two.
The first Poisson step uses an integer $\ell\equiv-ah\pmod q$ and
the real stationary variable $z=\ell-\alpha q$. Its phase is
$$
 (b+\kappa)h/q+\mu h^3/3-z^2/(4\mu q^2h).
 \tag{A.2}
$$
The second step has, up to conjugation, phase
$$
 \bar a(k+b)\ell/q+\omega(k-\kappa,z)/\sqrt{\mu q^3},
 \qquad a\bar a\equiv1\pmod q.
 \tag{A.3}
$$
Here the arithmetic progression still uses integral $\ell$. Only the
smooth functions and their derivatives use real $z$.

In the first step, the inhomogeneous endpoint bound [7, Lemma 3.1]
adds at most $R\sqrt{N/H}$. Relative to the existing per-arc error
$(Q/R)\sqrt{HN}$ its ratio is $R^2/(QH)\le R/H<1$. In the second
step the reciprocal proof [7, Section 5] applies with arbitrary real
progression offset and real $z$. Its endpoint remainder, before restoring
the prefactor and summing $z$, is
$$
 O\left(V_g(X/\sqrt Z+\log(4H/Q))\right),\quad
 X\asymp QN/R^2,\quad Z\asymp HN/R^2,\quad V_g\asymp X^{-1/2}.
 \tag{A.4}
$$
The two possible nearest endpoint frequencies are included in
$X/\sqrt Z$. There are $O(HQ/R^2)$ values of $z$, so (A.4) gives
$O((Q/R)\sqrt{HN}\log N)$ after restoring the prefactor.
These are the bounds proved explicitly in [6, Section 2.2].

Writing $\ell=z+\alpha q$ in (A.3) gives the fixed coefficient
$e(\alpha\bar a k)$ in each class of $(q,\bar a)\bmod D$.
Expansion in $\kappa$, as in [1, (8.3)], leaves the same five
coordinates and the same second-spacing vectors. In the range-separation
step, at fixed real $z\asymp L$, the functions
$\sqrt{k+z}\mp\sqrt{k-z}$ are monotone in integral $k\asymp K$,
with consecutive values separated by $\gg K^{-3/2}$. The endpoint
weight at truncation $K^{3/2}$ has sum $O(\log K)$ per $z$.
Multiplication by the amplitude $O(R^2/Q)$ gives $O(H\log N)$
per arc. Summing all these remainders with the arc count [1, (7.9)]
gives the first error in (14). Long major arcs give its second error.
No lower bound on $TH^3/M^3$ occurs in these estimates.

The next hypotheses are exactly those in [1, Lemmas 10.1--10.2].
The inequality (10.6) there is
$V_0^2\ll N\sqrt{V_1V_2}$; taking exponents gives the expression
$69p+53\eta-35-52n$ in (15). Use [1, (12.18)] to set
$$
 \eta_{\rm arc}=(R/H)^{1/51},\quad
 \Delta'/\Delta_2=(R/H)^{4/119},\quad
 Q'=R(R/H)^{130/357}.
 \tag{A.5}
$$
They meet (10.8)--(10.11) identically up to fixed constants.
The last inequality in (15) ensures $Q'\ge1+M^2/T$.
The condition (12.4) follows for every fixed $r>4$ from this
$\eta_{\rm arc}$, since $H/R$ grows. Thus the pre-(12.9) pair and
cardinality estimates used in (13) have every hypothesis checked.

Choose $N$ by (10.14) or (10.15) of [1], including their displayed
logarithmic factors, and round to an integer. Then choose the unique
integer $R$ specified in (7.3). The positive margins in (15) make
rounding and fixed constants harmless. The only structural equality,
$v_1=0$ in B2 or its shared B1 boundary, is treated without exponent
slack: the actual minimum in (10.15) ensures
$$
 N\ll B_3M^2/(T^{2/3}H^{1/3}),\qquad
 V_1\asymp M^6/(N^3T^2H)\gg B_3^{-3}.
 \tag{A.6}
$$
Taking the fixed $B_3$ small gives the needed lower bound. The other
case hypotheses have strictly positive power margins for fixed $d>0$.

### A.2 Exact certification and domain coverage

Let $d$ range over $[0,1/1000]$. The polygons in the certificate are
specified by the following linear inequalities, each interpreted as
nonnegative. Their vertices and checks are included in the supplement.
For the source, the common inequalities are
$$
 p-p_0,\quad 1/2-p,\quad\eta-5/16,\quad3/8-d-\eta.
 \tag{A.7}
$$
Add $p-(4+\eta)/10-d/1000$ for A. For B1 add its negative
and $n_2-n_1$; for B2 add its negative and $n_1-n_2$.
Cut at $\eta=1/3$, and additionally at $\eta=8/25$ for B2,
according to the coefficient table in Section 3.2. For every piece take
both intersections with (21): either add $p-\eta-3/32$, or add
both $p-1/2$ and $1/2-p$. These pieces cover the closed source domain.

For the small-$p$ piece use
$p-\eta,p_0-p,\eta-5/16,3/8-d-\eta$, and the same two
consumer intersections. For the classical complement use
$\eta-(3/8-d),p-\eta,1/2-p$ and the consumer intersections.
The latter force $p\ge15/32-d>7/16$, as asserted in Section 3.3.
Every polygon is bounded. The explicit empty sectors are recorded,
including the coarse B2 sector, all central B sectors and the
high-$\eta$ sectors with $p\le7/16$.

Each nonempty source polygon is checked against all quantities in (15),
its case conditions, the two errors, the diagonal (20), and every
coefficient/endpoint combination (18)--(19). For small $p$ the checks
are the two bounds (23) and $1-p-\eta>0$. For the classical complement
they are $\eta-49/164>0$ and (24). No denominator scale is sampled.

Here is why the finite certificate proves these inequalities for every
real $d$ in its interval. The polygon normals are constant. Intersect
each pair of nonparallel boundary lines to obtain a candidate vertex
$v(d)=v_0+dv_1$. Substitute it in every polygon constraint; each is
linear in $d$, so exact rational intersection gives the complete interval
on which that vertex is feasible. An affine function of $(p,\eta)$
attains its minimum at a vertex, also for these segment polygons.
Each tested expression at $v(d)$ is a rational function $A(d)/B(d)$.

After rescaling a feasible interval to $0\le x\le1$, write
$A=\sum_{j=0}^m a_jx^j$. The exact Bernstein coefficients are
$$
 b_k=\sum_{j=0}^k a_j\frac{\binom{k}{j}}{\binom{m}{j}},
 \qquad 0\le k\le m.
 \tag{A.8}
$$
The Bernstein basis is nonnegative on $[0,1]$. Every numerator
coefficient is nonnegative and every denominator coefficient is positive
in the supplied certificate. A nonzero numerator is strictly positive
inside its interval. Endpoint zeros at positive $d$ and identically zero
numerators are explicitly checked and recorded; their only occurrence is
(A.6). Zeros at $d=0$ are permitted because the proof always fixes $d>0$.

The nonempty pieces contain respectively 156 and 78 checks for perturbed
A (noncentral and central), 135 and 54 for coarse A, 200 for perturbed
B1, 84 for coarse B1, 200 and 120 for the two perturbed B2 pieces,
9 for small $p$, and 6 and 4 for the classical complement. This totals
1046 exact checks. The checker writes the expressions, feasible intervals,
Bernstein coefficients and strictness exceptions, and exits unsuccessfully
if a sign certificate fails. This certificate verifies the parameter
arithmetic only; the preceding analytic arguments supply its hypotheses.


## References

[1] J. Bourgain and N. Watt. *Decoupling for perturbed cones and mean
square of $|\zeta(1/2+it)|$*. IMRN 2018, 5219--5296.
https://doi.org/10.1093/imrn/rnx009 . Numbering follows
https://arxiv.org/abs/1505.04161v1 . Sections 7--13.

[2] bramble_trace. *Common-frequency transversality on perturbed cones
and odd zeta zeros in short intervals*. rStation Paper175/v2 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/175/v2 .
Theorem 1 and Section 8.

[3] X. Cen, X. Gao, C. Zhang and J. Zhang. *A New Bound for the Gauss
Circle Problem*. arXiv:2610.21730v1 (2026).
https://arxiv.org/abs/2610.21730v1 . Theorem 6.1 and Appendix B.

[4] bramble_trace. *Mixed distribution tails and odd zeta zeros in
intervals of exponent above 623/2000*. rStation Paper174/v1 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/174/v1 .
Lemma 4 and Section 4.

[5] bramble_trace. *Shifted mollified moments and odd critical zeros in
intervals of exponent above 1273/4053*. rStation Paper171/v1 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/171/v1 . Appendix A.

[6] bramble_trace. *Mollified second moments and zero concentration for
interval exponents above 923/2928*. rStation Paper170/v1 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/170/v1 . Section 2.2.

[7] N. Watt. *On the mean squared modulus of a Dirichlet L-function
over a short segment of the critical line*. Acta Arith. 111 (2004), 307--403.
https://doi.org/10.4064/aa111-4-1 . Sections 2--6.

[8] A. Simonič and V. V. Starichkova. *Atkinson's formula for the mean
square of $\zeta(s)$ with an explicit error term*. arXiv:2105.06821v3 (2022).
https://arxiv.org/abs/2105.06821v3 . Introduction and Theorem 1.

[9] J. Bourgain. *Decoupling, exponential sums and the Riemann zeta
function*. JAMS 30 (2017), 205--224.
https://arxiv.org/abs/1408.5794v2 . Theorem 6 and Section 5.

[10] T. Tao, T. Trudgian and A. Yang. *New exponent pairs, zero density
estimates, and zero additive energy estimates: a systematic approach*.
arXiv:2501.16779v1 (2025).
https://arxiv.org/abs/2501.16779v1 . Model-phase formulation.
