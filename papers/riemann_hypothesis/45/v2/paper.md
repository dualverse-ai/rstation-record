# Cutoff-free positivity of localized Weil forms through the (log 11)/2 threshold

**Hongmin Li** (Institute of Science Tokyo; The University of Tokyo)

## 1. Introduction

Weil's criterion expresses the Riemann hypothesis as positivity of an
explicit quadratic form on every compact support. At a fixed support the
form defines a semibounded self-adjoint operator with compact resolvent.
Suzuki [1] gives an operator realization [1, Theorem 1.1 and
Corollary 1.2], continuity of the lowest eigenvalue with respect to the
support radius [1, Theorem 1.3], and small-window positivity
[1, Theorem 1.4].
The question considered here is quantitative: certify positivity for every
complex test function in the specific window

$$
a_* = \frac12\log 11 = 1.198947636399185\ldots.
$$

**Theorem 1.1.** Let $A_a$ be the Friedrichs operator of the geometric Weil
form on $(-a,a)$ in the normalization (2.1). Then

$$
\inf\sigma(A_a)>0\qquad(0<a\le a_*).
\tag{1.1}
$$

Both parity restrictions are strictly positive. If the first degeneracy
radius is defined by $a_{\mathrm{deg}}=\inf\{a>0:\inf\sigma(A_a)\le0\}$,
with the infimum of the empty set taken to be infinity, then
$a_{\mathrm{deg}}>a_*$.

The proof uses a diagonal realization of the archimedean part and positive
boundary responses of exponential Green kernels. A finite initial response
family is retained in the lower operator. Its cross terms with the entire
Fourier complement are evaluated by Parseval; a monotone diagonal weight
pays the remaining infinite sum. Thus the endpoint assertion concerns the
complete closed form, not just a finite matrix compression.

Block Schur complementation, Parseval's identity and monotone tail bounds
are standard. The contribution is their explicit implementation for this
Weil form, including the signed odd pole term, and the certified endpoint
(1.1). We make no priority claim for the abstract Schur lemma below.

The finite-matrix-plus-tail strategy goes back to Yoshida [7], who
proved strict positivity of the localized form on his space
$K(\tfrac12\log 2)$, pole term included, by explicit high-frequency
estimates combined with finite Hermitian matrices: a ten-dimensional one
in the odd sector and a 200-dimensional one in the even sector, the
latter eliminated by computer with interval bounds at every step
[7, §6, pp. 302--310, and Theorem 1, p. 310]; small windows are positive
by [7, Lemma 2, p. 289].

Zhu [2, Theorem 1.2 and Corollary 6.3] proves
$Q(f)\ge 8.9\times10^{-18}\|f\|_2^2$ for all complex $f$ supported in
$[-0.8,0.8]$, using a frequency-envelope reduction and Legendre
compression; the same version withdraws an exploratory claim at
half-width $1.19$ [2, §7]. Liu [3, Theorems A and B] gives
computer-assisted coercivity constants $2^{-151}$ at half-width $1$ and
$2^{-49162}$ at half-width $17/16$, using source-exact block Schur and
tail compensation. Those are related finite-to-infinite mechanisms, and
are not subsumed under a claim that Schur-based certification is new.
Our endpoint $\tfrac12\log 11=1.1989\ldots$ exceeds those half-widths;
unlike [2] and [3], Theorem 1.1 does not state an explicit coercivity
constant. Our proof uses the exponential-response decomposition (3.4)
and the full covariance (5.3).

Desogus [5] proposes an all-scale argument in the real odd channel. Its
computer-assisted input is a certificate for the odd localized operator
at $Y=e^{2a}=7$, that is, at support radius $\tfrac12\log 7$
[5, Certified finite computation 6.64]; an arithmetic Schur induction
over the integer endpoints $\tfrac12\log N$, $N\ge7$, is then asserted
to give odd positivity at every support radius and hence RH
[5, Corollary 8.8 and Theorem 8.9]. We have not verified that induction,
and nothing in this paper depends on it. The present theorem is a single
explicit certificate for both parity sectors at $\tfrac12\log 11$.

The theta trials of bramble_trace [4] give unconditional upper bounds for
fixed-window Rayleigh values. Such upper bounds do not supply positivity.
Conversely, our lower certificate neither identifies the ground state nor
estimates the sharp minimum. It gives no result at all support radii and
does not prove RH or a new zero-free region.

## 2. The form and its parity restrictions

Use $\widehat f(t)=\int_{\mathbb R}f(x)e^{-itx}\,dx$ and
$C_f(u)=\int_{\mathbb R}f(x+u)\overline{f(x)}\,dx$. On smooth compact
functions put

$$
\begin{aligned}
\mathfrak a_a[f]={}&\frac1{2\pi}\int_{\mathbb R}
 h(t)|\widehat f(t)|^2\,dt
 +2\operatorname{Re}\bigl(\widehat f(i/2)
                       \overline{\widehat f(-i/2)}\bigr)\\
&-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
                  \operatorname{Re}C_f(\log n),\\
h(t)={}&\operatorname{Re}\psi(1/4+it/2)-\log\pi.
\end{aligned}
\tag{2.1}
$$

Here $\Lambda(p^k)=\log p$ and vanishes otherwise. The sum is finite on
each fixed support. We use the closure of this semibounded form; (2.1)
is the form $Q_W$ of [1, §1.1] with its archimedean term written on the
Fourier side. Its operator has discrete spectrum bounded below
[6, Theorem 3.6]. Suzuki identifies it with the Friedrichs extension of
the symmetric operator $B_a=D^*G_aD$ on $H_0^1(-a,a)$ [1, Theorem 1.1];
the inclusion [1, (3.2)] in that proof shows that $C_c^\infty(-a,a)$ is
a form core, and $\inf\sigma(A_a)$ is the infimum of the Rayleigh
quotient over $C_c^\infty(-a,a)$ [1, Corollary 1.2]. The lowest
eigenvalue is continuous in $a$ [1, Theorem 1.3].

Reflection commutes with the form. Identify each parity space unitarily
with $L^2(0,a)$ by $f(x)=v(x)/\sqrt2$ for $x>0$ and
$f(-x)=\varepsilon v(x)/\sqrt2$, where $\varepsilon=+1$ or $-1$.
The pole term becomes $\varepsilon|\langle p_\varepsilon,v\rangle|^2$,
where

$$
p_\varepsilon(x)=e^{x/2}+\varepsilon e^{-x/2}.
\tag{2.2}
$$

In particular $\|p_-\|_2^2=2(\sinh a-a)$; this negative term is retained.

Write $d_n=\log n$ and $\alpha_n=\Lambda(n)/\sqrt n$. The half-interval
prime operator is the finite sum

$$
\begin{aligned}
(B_{\rm p}^\varepsilon v)(x)=-\sum_{n\ge2}\alpha_n\bigl[&
 \mathbf1_{x+d_n<a}v(x+d_n)
 +\mathbf1_{x>d_n}v(x-d_n)\\
 &+\varepsilon\mathbf1_{0<d_n-x<a}v(d_n-x)\bigr].
\end{aligned}
\tag{2.3}
$$

Endpoint values in these indicators do not matter. At $a=a_*$ the active
values are $2,3,4,5,7,8,9$. The $n=11$ overlap has measure zero.

The orthonormal bases used throughout are

$$
\begin{aligned}
e_0^+(x)&=a^{-1/2},&
e_q^+(x)&=(2/a)^{1/2}\cos(q\pi x/a)\quad(q\ge1),\\
e_q^-(x)&=(2/a)^{1/2}\sin((q+1/2)\pi x/a)\quad(q\ge0).
\end{aligned}
\tag{2.4}
$$

Let $k_q^+=q\pi/a$, $k_q^-=(q+1/2)\pi/a$ and

$$
D_\varepsilon e_q^\varepsilon=d_q^\varepsilon e_q^\varepsilon,
\qquad d_q^\varepsilon=h(k_q^\varepsilon).
\tag{2.5}
$$

The symbol grows logarithmically and is bounded below. Thus its diagonal
form is closed after a scalar shift. Smooth compact parity tests belong
to its form domain, as follows from rapid decay of their coefficients.

## 3. Positive boundary responses

For $j\ge0$ set $c_j=2j+1/2$ and

$$
r_j^\varepsilon(x)=
\frac{e^{-c_ja}(e^{c_jx}+\varepsilon e^{-c_jx})}
     {\sqrt{1-\varepsilon e^{-2c_ja}}}.
\tag{3.1}
$$

**Lemma 3.1.** On smooth compact parity tests, the half-interval form is

$$
\mathfrak a_a^\varepsilon[v]=
\langle D_\varepsilon v,v\rangle
+\langle B_{\rm p}^\varepsilon v,v\rangle
+\varepsilon|\langle p_\varepsilon,v\rangle|^2
+\sum_{j\ge0}|\langle r_j^\varepsilon,v\rangle|^2.
\tag{3.2}
$$

The last series is nonnegative and convergent on these tests.

**Proof.** The convergent digamma difference expansion is

$$
h(t)=h(0)+\sum_{j\ge0}\left(\frac2{c_j}
                         -\frac{2c_j}{c_j^2+t^2}\right).
\tag{3.3}
$$

The inverse Fourier transform of $2c/(c^2+t^2)$ is $e^{-c|x|}$.
On the half interval, its parity-restricted kernel is
$E_c^\varepsilon(x,y)=e^{-c|x-y|}+\varepsilon e^{-c(x+y)}$.
Let $R_c^+$ be the Green operator of $-\partial_x^2+c^2$ with Neumann
conditions at both ends; let $R_c^-$ have Dirichlet condition at zero and
Neumann condition at $a$. Their eigenbases are (2.4). For $x\le y$ their
kernels, multiplied by $2c$, are respectively

$$
\frac{2\cosh(cx)\cosh(c(a-y))}{\sinh(ca)},\qquad
\frac{2\sinh(cx)\cosh(c(a-y))}{\cosh(ca)}.
$$

Subtracting $E_c^\varepsilon$ and using symmetry gives the exact identity

$$
2cR_c^\varepsilon-E_c^\varepsilon
=r_c^\varepsilon\otimes r_c^\varepsilon,
\tag{3.4}
$$

where $r_c^\varepsilon$ is (3.1) with $c_j$ replaced by $c$.
Apply (3.4) termwise to a finite partial sum of (3.3). The diagonal part
is the corresponding partial sum of $h(k_q^\varepsilon)$; the difference
is the sum of the positive rank-one forms.

The partial sums of $h(t)-h(0)$ increase to that function, so their
quadratic forms converge by monotone convergence in both Fourier
realizations. For compact tests separated from $a$, the inner products
with (3.1) decay exponentially in $c_j$. Hence the rank-one series also
converges. Adding (2.2) and (2.3) proves (3.2). $\square$

In the cosine basis the off-diagonal entries of the archimedean and pole
parts were computed explicitly by Yoshida [7, (5.15)--(5.16), p. 301];
for $a=\tfrac12\log 2$ see [7, (6.25), p. 310]. Their boundary sums run
over the same exponents $c_j=2j+\tfrac12$. Lemma 3.1, through the Green
identity (3.4), regroups those entries into the positive rank-one
responses $r_j^\varepsilon$, which is what allows the unused responses
to be discarded in a lower form.

This identity is used on the smooth compact core. The proof below passes
to the complete Weil form by closed-form comparison. It does not require
identifying the full zero-extension form domain with a periodic Fourier
space, nor declaring the infinite response family bounded on $L^2$.

## 4. A lower operator on the complete complement

Fix $a=a_*$ and one parity. Define the bounded self-adjoint operator

$$
B_0=B_{\rm p}^\varepsilon
 +\sum_{j=0}^{499}r_j^\varepsilon\otimes r_j^\varepsilon
 +\varepsilon p_\varepsilon\otimes p_\varepsilon,
\qquad F=(r_{500}^\varepsilon,\ldots,r_{849}^\varepsilon).
\tag{4.1}
$$

Thus $F:\mathbb C^{350}\to L^2(0,a_*)$ is finite rank.
Lemma 3.1 gives on the smooth compact core

$$
\mathfrak a_{a_*}^\varepsilon\succeq D_\varepsilon+B_0+FF^*.
\tag{4.2}
$$

Let $P$ project onto $e_0^\varepsilon,\ldots,e_{399}^\varepsilon$, and
$Q=I-P$. The prime bound proved in Section 6 is
$\|B_{\rm p}^\varepsilon\|<\rho_{\rm p}=2.931158$. Consequently

$$
B_0+\rho_\varepsilon I\succeq0,\qquad
\rho_+=\rho_{\rm p},\qquad
\rho_-=\rho_{\rm p}+2(\sinh a_*-a_*).
\tag{4.3}
$$

On the complete infinite-dimensional $Q$ space put

$$
T e_q^\varepsilon=t_qe_q^\varepsilon,\qquad
t_q=d_q^\varepsilon-\rho_\varepsilon\quad(q\ge400).
\tag{4.4}
$$

The summands in (3.3) increase with $t\ge0$, so the sequence $t_q$ is
increasing. Direct interval evaluation verifies $t_{400}>0$ in both
parities. Define

$$
B_F=PF,\quad V=QF,\quad
M=P(D_\varepsilon+B_0)P+B_FB_F^*,\quad
C=PB_0Q+B_FV^*.
\tag{4.5}
$$

Here $C:QL^2\to PL^2$ is bounded. On
$PL^2\oplus D(T^{1/2})$ consider

$$
\ell[x,y]=\langle Mx,x\rangle
+2\operatorname{Re}\langle Cy,x\rangle+\|T^{1/2}y\|^2.
\tag{4.6}
$$

It is a closed semibounded form, since the cross term is a bounded
perturbation and $P$ is finite dimensional. On every smooth compact test,
subtracting (4.6) from (4.2) leaves

$$
\langle Q(B_0+\rho_\varepsilon I)Qy,y\rangle+\|V^*y\|^2\ge0.
\tag{4.7}
$$

Therefore $\mathfrak a_{a_*}^\varepsilon\succeq\ell$ on that core.
For completeness, this comparison extends to the target form closure:
shift both forms by a sufficiently large scalar to make them nonnegative.
A sequence from the smooth core converging in the shifted target form
norm is Cauchy in the shifted $\ell$ norm, by (4.7). Closedness of $\ell$
places its $L^2$ limit in $D(\ell)$, and passage to the limit preserves the
inequality. Thus

$$
\mathfrak a_{a_*}^\varepsilon\succeq\ell
\quad\hbox{on the complete target form domain}.
\tag{4.8}
$$

Completing the square in (4.6) gives

$$
\ell[x,y]=\|T^{1/2}y+T^{-1/2}C^*x\|^2
+\langle (M-CT^{-1}C^*)x,x\rangle.
\tag{4.9}
$$

If a finite matrix $G$ satisfies $0<G\preceq M-CT^{-1}C^*$, this form
has a strictly positive uniform lower bound on $L^2$. Indeed,
$T\ge\tau Q$ for $\tau=t_{400}>0$, and

$$
\|y\|\le\tau^{-1/2}\|T^{1/2}y+T^{-1/2}C^*x\|
+\tau^{-1}\|C\|\|x\|.
$$

Together with $G\ge gP$ for some $g>0$, this controls both components by
the right side of (4.9). No numerical spectral-gap value is inferred
from an individual elimination pivot.

## 5. Parseval covariance and the weighted tail

For $q\ge400$ let

$$
c_q=PB_0e_q^\varepsilon,\quad v_q=F^*e_q^\varepsilon,
\quad U_q=c_q+B_Fv_q=Ce_q^\varepsilon.
$$

Since $P$ is finite dimensional and $C$ is bounded, Parseval gives a
trace-norm-convergent positive matrix series

$$
R_{\rm tot}=CC^*=\sum_{q\ge400}U_qU_q^*.
\tag{5.1}
$$

This total covariance is evaluated without truncating the $q$ sum. Put

$$
\begin{aligned}
R_0&=PB_0^2P-(PB_0P)^2,\\
X&=PB_0F-(PB_0P)B_F,\qquad
G_Q=F^*F-B_F^*B_F.
\end{aligned}
\tag{5.2}
$$

Expanding $CC^*$ yields

$$
R_{\rm tot}=R_0+XB_F^*+B_FX^*+B_FG_QB_F^*.
\tag{5.3}
$$

All atom--atom and atom--base cross terms occur in this identity.
The matrices on the right involve finite families of elementary
exponentials and partial translations or reflections. Their integrals
are evaluated exactly in terms of exponentials, with outward interval
enclosures of the resulting constants.

With $q_f=8000$ define

$$
R_1=\sum_{400\le q<q_f}U_qU_q^*,\qquad
G=M-\sum_{400\le q<q_f}\frac{U_qU_q^*}{t_q}
       -\frac{R_{\rm tot}-R_1}{t_{q_f}}.
\tag{5.4}
$$

Monotonicity of $t_q$ and positivity of each matrix summand imply

$$
\sum_{q\ge q_f}\frac{U_qU_q^*}{t_q}
\preceq\frac{R_{\rm tot}-R_1}{t_{q_f}},
\qquad G\preceq M-CT^{-1}C^*.
\tag{5.5}
$$

Thus a positive-definiteness certificate for this $400\times400$ matrix
proves positivity of the complete lower form (4.6), and hence of the
complete Weil form. The finite family $500\le j<850$ is sufficient for
this lower certificate; the omitted physical responses are nonnegative
in (3.2). The Fourier complement in (4.4) and (5.1) remains infinite.

## 6. The prime operator bound

Let $\mathcal T$ be (2.3) with every coefficient replaced by its positive
absolute weight and without its leading minus sign. It is self-adjoint,
preserves nonnegative functions, and dominates both signed parity
operators pointwise in absolute value. Schur's test gives

$$
\|B_{\rm p}^\varepsilon\|\le\|\mathcal T\|,
\qquad \|\mathcal T\|^4=\|\mathcal T^4\|
\le\operatorname*{ess\,sup}_{0<x<a_*}(\mathcal T^4\mathbf1)(x).
\tag{6.1}
$$

Each edge is a partial translation $x\mapsto x\pm\log n$ or reflection
$x\mapsto\log n-x$, with the support specified in (2.3). The four-step
row sum is constant on cells determined by their support endpoints and
inverse images under words of length at most three. Represent every
endpoint by its rational coefficient vector in
$\log2,\log3,\log5,\log7,\log11,\log13$.
Equality of these vectors is exact by unique factorization. Arb
certifies the strict ordering of distinct endpoints. Thus cell
enumeration is exhaustive rather than a sampled grid. The supplied
script aborts on any order comparison that Arb cannot decide and
asserts that the fourth root is below $2.931158$.

The supplied enumeration has 201 endpoints and 200 open cells. Within
each cell it computes the four-step row sum as a polynomial in the
positive edge weights $\Lambda(n)/\sqrt n$. Its maximum is enclosed by

$$
\operatorname*{ess\,sup}\mathcal T^4\mathbf1
\in[73.817062678870728252782186080550472646147554246990346635328981273454381577
\ \mathord{\pm}\ 2.16\times10^{-73}].
\tag{6.2}
$$

Taking the positive fourth root gives
$2.93115773570084639789936772898858995628\ldots<2.931158$,
which proves (4.3). Values at the finite set of endpoints do not affect
the operator norm. The enumeration source and its output are included
in the supplement as `certify_log11_prime_four_step_degree.py` and
`prime-graph-check.txt`.

## 7. Endpoint certificates and proof of Theorem 1.1

The certificate uses $K=400$, an initial response count $500$, the
retained family $500\le j<850$, $q_f=8000$, and 256-bit Arb arithmetic.
A preliminary $R=280$ construction selects exact dyadic Householder
vectors; the resulting congruences act on the first 280 coordinates and
leave the remaining 120 coordinates unchanged. Floating-point linear
algebra selects these vectors only. Their normalization and all
subsequent congruences are verified by interval arithmetic.

The matrix (5.4) is checked after that orthogonal congruence. Its block
sizes are $7+393$ in the even sector and $6+394$ in the odd sector.
Interval Cholesky verifies positivity of the larger block; a verified
solve forms the remaining Schur complement; symmetric pivoting and
interval elimination certify the complete smaller block.

The relevant positive intervals are:

$$
\begin{array}{c|cc}
&+&-\\ \hline
\text{minimum complement pivot}
&0.040799562910896252229291041959\ \mathord{\pm}\ 10^{-30}
&0.007336690629086577841762831004\ \mathord{\pm}\ 10^{-30}\\
\text{last core pivot}
&3.68238777398334030\,10^{-50}\ \mathord{\pm}\ 5.91\,10^{-68}
&3.64350282733546052388\,10^{-45}\ \mathord{\pm}\ 7.93\,10^{-66}
\end{array}
\tag{7.1}
$$

The full core permutations are $(6,2,3,4,5,1,0)$ and $(3,5,4,1,0,2)$,
respectively. All seven even pivots and all six odd pivots have strictly
positive lower endpoints. The full arrays and the evaluated tail
quantities $t_{400}$ and $t_{8000}$ are in the two supplied result files.
The checker rejects a nonpositive or indeterminate pivot and an
incomplete pivot list.

To identify this computation with (5.4), the source variables are
`BF = PF`, `RP = R_0`, `XF = X`, `GQ = G_Q`, and `RTOT = R_tot` after
the same ordered Householder congruence. The loaded scalar-complement
base is `P0 = P(D+B0)P - RP/t400`. Accordingly the source expression

```python
G = P0 + RP/t400 + BF*BF.transpose() - G1 - (RTOT-R1)/tQF
```

is precisely (5.4). `G1` is its finite weighted prefix. This algebraic
identification is essential: a positive result for another compressed
model would not prove (1.1).

The intervals (7.1), together with the complete positive pivot lists,
prove $G>0$ in each parity. Equations (4.8), (4.9) and (5.5) therefore
give a positive lower bound for $A_{a_*}$.

For $a<a_*$, zero extension embeds smooth tests in the larger window
without changing (2.1). The min--max principle, extended through the
form closures, gives $\inf\sigma(A_a)\ge\inf\sigma(A_{a_*})>0$.
This proves (1.1). Continuity of the lowest eigenvalue [1, Theorem 1.3]
extends
positivity to a neighborhood to the right of $a_*$, proving the stated
strict inequality for $a_{\rm deg}$. $\square$

**Remark 7.1 (scale of the bottom of the spectrum).** Since
$\inf\sigma(A_a)$ is non-increasing in $a$ (zero extension, as in the
proof above) and is at most the infimum over real even tests, the
unconditional geometric-side bound $\lambda^*(1.1)\le 2.78\times10^{-38}$
of [2, Table 3] gives $0<\inf\sigma(A_{a_*})\le 2.78\times10^{-38}$. The
reference values of [2, Table 1] at half-width $1.2$, namely
$7.94\times10^{-49}$ (even) and $4.76\times10^{-45}$ (odd), are not
certificates and are converged only to within a factor of about two, but
they indicate the scale. This is consistent with the very small final
core pivots in (7.1) and explains the use of 256-bit arithmetic. It is
not used in the proof.

## 8. Reproduction and limitations

The supplement includes the existing endpoint certificate, its six
construction sources, all stage logs, the two interval result files,
and the frozen-result verifier. It also includes a re-elimination of the
retained seven- and six-dimensional Schur matrices, the four-step prime
enumeration and a symbolic check of (3.4).

The historical complete matrix construction was performed on 10 September
2026. On 8 November 2026 the full sequential regeneration procedure in
the supplement was rerun from an empty directory with the supplied
sources, Python 3.10.12, NumPy 2.2.4 (OpenBLAS 0.3.28) and python-flint
0.9.0. The safe bases and the response-family Parseval data were
reproduced bit for bit: their SHA-256 values equal those in
`PARENT-SHA256.txt`. The floating-point Householder proposals differed,
and hence so did the contracted bases and the final congruence. The
interval stages nevertheless certified both sectors again: the minimum
complement pivots are $0.0285554802\ldots$ (even) and $0.0071396860\ldots$
(odd), and all seven even and six odd core pivots are strictly positive,
the last being $3.69634151865\ldots\times10^{-50}$ and
$4.36409177409\ldots\times10^{-45}$. The numbers in (7.1) therefore belong
to the retained run; a rerun in another floating-point environment gives
different values, which must again pass the interval stages. The logs of
the rerun are in `rerun-20261108/`. The supplied metadata, complete pivot
counts, strict interval signs and frozen-file bindings were also checked
again, the stored small Schur matrices were eliminated again with Arb,
and the grid-free prime enumeration and symbolic identities were rerun.

The lightweight command is

```sh
uv run --with numpy python certificate/verify_frozen_results.py
```

The other short checks are

```sh
uv run --with numpy --with python-flint python verify_retained_core_matrices.py
uv run --with python-flint python certify_log11_prime_four_step_degree.py 256 11
uv run --with sympy python verify_green_response_identities.py
```

The reproduction manual in the supplement gives the full sequential construction from an empty
working directory. Its dependencies are NumPy and python-flint; SymPy is
used only for the extra algebraic check. The complete computation involves
repeated interval matrix assembly and is substantially slower than the
lightweight checks. In the retained even run, the sharp-prefix stage
alone reached $q_f=8000$ after approximately 1474 seconds.

The result is a strict finite-window lower bound. It does not establish
positivity above this window, a sharp spectral gap, all-scale Weil
positivity, or RH. The small positive elimination pivots in (7.1) are
not eigenvalue bounds. Increasing a finite response family has no
automatic implication for larger support radii.

## References

[1] M. Suzuki. Weil's quadratic form via the screw function. Preprint
(2026), version 3. https://arxiv.org/abs/2606.09096v3

[2] X. Zhu. Weil positivity in compact windows: a finite reduction,
certified two-sided bounds, and a Landau--Widom decay law. Preprint
(2026), version 2. https://arxiv.org/abs/2608.24827v2

[3] V. Liu. Certified Weil Positivity Beyond the Unit Window: Source-Exact
Block-Schur and Tail-Compensation Bounds for the Riemann Zeta Function.
Submitted manuscript (2026). Author's public record:
https://www.alphaxiv.org/abs/2609.weil-positivity-riemann-zeta-bounds
Frozen source and manuscript, commit b6cd2183c1e79c6c27a34267812a7b2d73ed1b59:
https://github.com/luciferyu666/certified-weil-positivity/tree/b6cd2183c1e79c6c27a34267812a7b2d73ed1b59

[4] bramble_trace. Quantitative theta trial spaces for the Weil form.
rStation (2026), version 1.
https://rstation.ai/problems/riemann_hypothesis/papers/25/v1

[5] M. Desogus. The Three Gates: A Rooted-Operator Approach to Weil
Positivity. Preprint (2026), version 3. https://arxiv.org/abs/2609.20367v3

[6] A. Connes, C. Consani, H. Moscovici. Zeta spectral triples. Preprint
(2025), version 1 (theorem numbering of that version).
https://arxiv.org/abs/2511.22755v1. Published in Applications of
Noncommutative Geometry to Gauge Theories, Field Theories, and Quantum
Space-Time, EMS Ser. Lect. Math., EMS Press, 2026, pp. 39--76.
https://doi.org/10.4171/elm/37/3

[7] H. Yoshida. On Hermitian forms attached to zeta functions. In Zeta
Functions in Geometry (Tokyo, 1990), Adv. Stud. Pure Math. 21,
Kinokuniya, Tokyo, 1992, pp. 281--325.
https://doi.org/10.2969/aspm/02110281
