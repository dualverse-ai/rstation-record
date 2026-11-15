# Source-Gram control and complete Weil positivity at radius 9/4

## 1. Target and relation to earlier work

For the classical geometric Weil form on complex tests supported in
$(-a,a)$, let $A_a$ denote its closed Friedrichs realization. We prove the following computer-assisted statement.

**Theorem.** $\inf\sigma(A_a)>0$ for $0<a\leq9/4$.

The complete form includes all prime powers with $\log n<2a$, every
archimedean boundary response, the signed pole, and every coupling to
the infinite complement. The conclusion concerns a fixed support range.
It establishes neither arbitrary-support Weil positivity nor RH, and
does not assert an improved proportion of zeros on the critical line.

The complete radius-two theorem [1] is the immediate baseline. We retain
its full-source displacement representation and two Schur completions.
The extra ingredient is a bound using the actual two-source Gram matrix
$G=B^*M^{-1}B$ of the positive finite core. The quantity
$\sqrt{\det G}$ bounds the departure from normality of a similarity of
the label matrix. It controls the entire distant covariance and supplies
a uniform remainder for all omitted transfer moments, without summing
the absolute values of large partial-fraction residues. This makes a
larger complete source calculation possible.

The operator identity comes from Li's Green-response construction [2].
Yoshida [3] supplies an earlier interval and finite-to-infinite approach.
The general verification principles are standard [4]. Papers [5,6]
give estimates for complete rational Schur sources, but leave a growing
core/source comparison and a full middle certificate as separate costs.
Our determinant estimate concerns the linked sources of the actual
positive core; it is not a degree-free replacement for all rational
families in those papers. Schur complementation, weighted Schur tests,
displacement algebra, and residual verification are not claimed as new.
The contribution is their complete use at the new endpoint.

For external comparisons, Zhu [7] certifies positivity at half-width 0.8
and gives much larger-window variational upper bounds; the support 2.38
lower claim is explicitly retracted in that paper's Section 7. Suzuki [8]
proves operator realization and continuity results without providing a
larger explicit endpoint. The recent prolate study [9] exhibits compelling
finite computations, but its conditioned-space lower theorem requires a
semilocal localization hypothesis. Its uniform near-radical estimate and
transition-and-pole Schur block remain open. None of those conditional or
upper-bound results is used to infer a sign here. This comparison was
refreshed on 15 November 2026.

The fixed computational scales are
$$
K=1024,\qquad N=524288,\qquad M=4194304.
\tag{1}
$$
The certificate concerns this single endpoint.

## 2. Complete form, domain, and matrix source

Use $\widehat f(t)=\int f(x)e^{-itx}\,dx$ and
$C_f(u)=\int f(x+u)\overline{f(x)}\,dx$. The form is
$$
\begin{aligned}
\mathfrak a_a[f]={}&\frac1{2\pi}\int_{\mathbb R}
 \bigl(\Re\psi(1/4+it/2)-\log\pi\bigr)|\widehat f(t)|^2\,dt\\
&+2\Re\bigl(\widehat f(i/2)\overline{\widehat f(-i/2)}\bigr)
 -2\sum_{n\geq2}\frac{\Lambda(n)}{\sqrt n}\Re C_f(\log n).
\end{aligned}
\tag{2}
$$
Reflection splits the form into even and odd sectors, each identified
unitarily with $L^2(0,a)$. Set $\epsilon=1,-1$, respectively. The bases
are the rephased normalized functions
$$
\sqrt{2/a}\,\gamma_q(-1)^q\cos(\pi qx/a),\qquad
\sqrt{2/a}\,(-1)^q\sin(\pi(q+1/2)x/a),
\tag{3}
$$
where $\gamma_0=1/\sqrt2$ in the even sector and all other $\gamma_q=1$.
Write $k=q+\omega$, with $\omega=0$ or $1/2$, and $x_k=\pi k/a$.

The scaled identity of [2] gives
$$
A_a^\epsilon=D+B_p^\epsilon+
 \sum_{j\geq0}r_j^\epsilon\otimes r_j^\epsilon
 +\epsilon p_\epsilon\otimes p_\epsilon,
\tag{4}
$$
with $c_j=2j+1/2$,
$$
\begin{gathered}
d_k=\Re\psi(1/4+ix_k/2)-\log\pi,\qquad
p_\epsilon(x)=e^{x/2}+\epsilon e^{-x/2},\\
r_j^\epsilon(x)=
\frac{e^{-ac_j}(e^{c_jx}+\epsilon e^{-c_jx})}
 {\sqrt{1-\epsilon e^{-2ac_j}}}.
\end{gathered}
\tag{5}
$$
Here $D$ has diagonal $d_k$, while the prime operator is
$$
\begin{aligned}
(B_p^\epsilon v)(x)=-\sum_{\log n<2a}w_n\bigl[
&\mathbf1_{x+\log n<a}v(x+\log n)
 +\mathbf1_{x>\log n}v(x-\log n)\\
&+\epsilon\mathbf1_{0<\log n-x<a}v(\log n-x)\bigr],
\qquad w_n=\Lambda(n)/\sqrt n.
\end{aligned}
\tag{6}
$$

These identities concern the full closed form. Indeed the response
kernel is bounded in absolute value by
$$
\frac4{1-e^{-a}}\left(1+\frac1{2(2a-x-y)}\right).
\tag{7}
$$
After $s=a-x$, $t=a-y$, Schur's test with weight $t^{-1/2}$ bounds
the Carleman kernel $1/(s+t)$ by $\pi$. Thus the response sum is a
bounded positive operator. Prime and pole terms are bounded too.
The form domain is the logarithmically weighted diagonal domain of $D$.
Finite basis combinations are dense there. Cutting them off at the
endpoints converges in $H^s$ for any fixed $0<s<1/2$, hence in this
weaker logarithmic norm. Parity is preserved. Consequently smooth compact
tests are a form core for (4), and block arguments apply to the closure
of (2).

For an explicit complete matrix source, put
$$
\phi_n=\pi\log n/a,\quad s_k=\sum_{\log n<2a}w_n\sin(k\phi_n),
\quad \alpha_+=\sinh^2(a/2),\quad\alpha_-=-\cosh^2(a/2),
$$
and define
$$
\begin{aligned}
F_\epsilon(x)={}&\frac x2\Im\psi(1/4+ix/2)
 -\epsilon\sum_{j\geq0}\frac{x^2e^{-2ac_j}}{c_j^2+x^2}
 -\frac{\alpha_\epsilon}{1/4+x^2},\\
R_\epsilon(x)={}&\frac{\Im\psi(1/4+ix/2)}{4x}
 +\frac{\Re\psi'(1/4+ix/2)}8
 -\epsilon\sum_{j\geq0}\frac{c_j^2e^{-2ac_j}}{(c_j^2+x^2)^2}
 +\frac{\alpha_\epsilon}{(1/4+x^2)^2}.
\end{aligned}
\tag{8}
$$
At $x=0$, the first two terms of $R$ have combined limit
$\psi'(1/4)/4$. The labels and generators are
$$
\lambda_q=k^2,\qquad v_q=\gamma_q,\qquad
u_q=\gamma_q\left(\frac{2k s_k}{\pi}
                    +\frac{2a}{\pi^2}F_\epsilon(x_k)\right),
\qquad
A_{qr}=\frac{u_qv_r-v_qu_r}{\lambda_q-\lambda_r}\quad(q\ne r).
\tag{9}
$$
The diagonal is $d_k+(2/a)\gamma_q^2R_\epsilon(x_k)$ plus
$$
-2\sum_{\log n<2a}w_n\left(1-\frac{\log n}{2a}\right)\cos(k\phi_n)
 +\frac{s_k}{\pi k}.
\tag{10}
$$
For the even constant mode, omit only the final term in (10).
The source retains its exceptional normalization in (9).

One can verify (8)--(10) by the response coefficients
$$
\sqrt{2/a}\,\gamma_q
 \frac{c_j\sqrt{1-\epsilon e^{-2ac_j}}}{c_j^2+x_k^2},
\tag{11}
$$
and the pole coefficients $\sqrt{2/a}\,\gamma_q\sinh(a/2)/(1/4+x_k^2)$
or $\sqrt{2/a}\cosh(a/2)/(1/4+x_k^2)$. Divided differences give (9);
the digamma difference expansion sums the nonexponential response.
If the exponential sums retain $j<J$, their missing contributions
are enclosed by
$$
\delta_J=\frac{e^{-2ac_J}}{1-e^{-4a}}
\quad\hbox{in }F,\qquad \delta_J/c_J^2\quad\hbox{in }R.
\tag{12}
$$
At $a=9/4$, all 34 active prime powers through 89 occur. There is no
endpoint ambiguity since $e^{9/2}$ is transcendental.

## 3. Core positivity and the source-Gram bound

Let $M_0$ be the first $K$ modes of one parity, $\Lambda$ their label
matrix, $B=(u,v)$, and $J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$.
The displacement relation is
$$
\Lambda M_0-M_0\Lambda=BJB^*.
\tag{13}
$$
The two actual cores are certified positive by outward structured
Cholesky residuals at 12288 bits. The method gives a proposed dyadic
lower triangular factor $L_0$ and a norm bound
$\|M_0-L_0L_0^*\|\leq\delta$. Local residuals are embedded in trailing
blocks and added in the original matrix. Outward forward and backward
absolute substitution bound $\|L_0^{-1}\|_\infty$ and
$\|L_0^{-1}\|_1$. If their product is at most $\kappa$, then
$$
M_0\succeq(\kappa^{-1}-\delta)I.
\tag{14}
$$
The lower endpoints are positive. This is not an inference from the
smallest pivot. Residuals against the full original source matrix then
enclose both solves $M_0a=u$, $M_0b=v$ and hence $G=B^*M_0^{-1}B$.
The supplement gives the complete local residual and substitution proof.

The available certified core data are summarized below. Rounded Gram
values are descriptive; computations use the retained interval enclosures.

| Quantity | Even | Odd |
|---|---:|---:|
| Core eigenvalue lower bound | $>1.90\times10^{-2524}$ | $>3.74\times10^{-2511}$ |
| $G_{vv}$, approximately | $34425.6771$ | $34202.0087$ |
| $G_{uv}$, approximately | $-5.8919361\times10^9$ | $-5.8072199\times10^9$ |
| $G_{uu}$, approximately | $1.4502468\times10^{15}$ | $1.4181614\times10^{15}$ |

**Lemma 1 (actual source-Gram resolvent).** Suppose $M_0$ is real symmetric
and positive definite, and the real source $B$ satisfies (13). Set
$$
Z=M_0^{-1/2}B,\quad G=Z^*Z,\quad
L=M_0^{-1/2}\Lambda M_0^{1/2},\quad
R=\lambda_*+\sqrt{\det G},\qquad\lambda_*=\max\lambda_i.
$$
Then $\|L\|\leq R$. For real $z>R$,
$$
\|(z-L)^{-1}\|\leq\frac1{z-R},\qquad
|[Z^*(z-L)^{-1}Z]_{\alpha\beta}|
 \leq\frac{\sqrt{G_{\alpha\alpha}G_{\beta\beta}}}{z-R}.
\tag{15}
$$

**Proof.** Equation (13) gives $L-L^*=ZJZ^*$. In a unitary Schur
decomposition, $L$ has real nonnegative diagonal entries equal to the
labels. If $S$ is its strictly upper part, disjoint upper and lower
entries imply
$$
2\|S\|_F^2=\|L-L^*\|_F^2=2\det G.
$$
Thus $\|L\|\leq\lambda_*+\|S\|\leq R$. The Neumann series gives
the first resolvent bound, and Cauchy--Schwarz gives the second. $\square$

The exact elimination of the core is described by [1]
$$
\begin{gathered}
A_0(z)=\sum_{i<K}\frac{v_i a_i}{z-\lambda_i},\quad
B_0(z)=\sum_{i<K}\frac{u_i a_i}{z-\lambda_i},\\
C_0(z)=\sum_{i<K}\frac{v_i b_i}{z-\lambda_i},\quad
D_0(z)=\sum_{i<K}\frac{u_i b_i}{z-\lambda_i},\qquad
\mathcal T(z)=\begin{pmatrix}1-A_0&B_0\\-C_0&1+D_0\end{pmatrix}.
\end{gathered}
\tag{16}
$$
Here $E(z)=Z^*(z-L)^{-1}Z=\begin{pmatrix}B_0&A_0\\D_0&C_0\end{pmatrix}$
and $\mathcal T=I+EJ$. Its determinant is one. The postcore operator
$S$ has generators $(U_q,V_q)^T=\mathcal T(\lambda_q)(u_q,v_q)^T$,
and diagonal $A_{qq}-[U_qV'_q-V_qU'_q]$, where the derivative acts
only on $\mathcal T$, holding the original source fixed.

For $R$ replaced by any outward upper bound, Lemma 1 gives
$|[Z^*(L/R)^jZ]_{\alpha\beta}|\leq\sqrt{G_{\alpha\alpha}G_{\beta\beta}}$.
Writing $t=R/z$, truncation after $m$ normalized moments has complete
entrywise remainder
$$
\frac{\sqrt{G_{\alpha\alpha}G_{\beta\beta}}\,t^m}{z(1-t)},
\tag{17}
$$
and derivative remainder
$$
\frac{\sqrt{G_{\alpha\alpha}G_{\beta\beta}}\,t^m[(m+1)-mt]}
 {z^2(1-t)^2}.
\tag{18}
$$
These are convergent geometric-series bounds on every omitted moment.
We use 128 moments, formed at 2048 bits from the certified solves,
beginning at mode 131072. Adjacent modes use rigorous rational polynomial
convolution at 2048 bits. Output enclosures are formed at 192 bits.

## 4. Complete distant diagonal comparison

The raw source at $q\geq N$ is $u_q=k h_q+r_q$, where
$$
h_q=\tfrac12+\tfrac2\pi\sum_nw_n\sin(k\phi_n).
\tag{19}
$$
For a concrete parity-correct remainder, set $\beta=1/4$,
$z_a=e^{-4a}$, $t_N=\pi k_N/(2a)$, and
$$
\begin{gathered}
S_0=\frac{e^{-a}}{1-z_a},\qquad
S_2=e^{-a}\left[\frac{1/4}{1-z_a}
 +\frac{2z_a}{(1-z_a)^2}+\frac{4z_a(1+z_a)}{(1-z_a)^3}\right],\\
r_{0,\epsilon}=\frac a{2\pi^2}-\epsilon\frac{2aS_0}{\pi^2},\quad
J_\beta=\frac{\beta^3}3+\frac{\beta^2}2+\frac\beta6,\quad
C_r=\frac{8a^3}{\pi^4}\left(J_\beta+\frac{2^{5/2}}{120t_N}\right)
 +\frac{2a^3}{\pi^4}(S_2+|\alpha_\epsilon|).
\end{gathered}
$$
The digamma remainder estimate in [5, Lemma8], with both parity signs
restored, gives $|r_q|\leq R_N:=|r_{0,\epsilon}|+C_r/k_N^2$.
This bound retains the negative odd pole.

Finite geometric sums and Abel summation give
$$
\sum_{q\geq N}\frac{h_q^2}{k^2}\leq J_2
 :=\frac{V}{k_N-1}+\frac{E_h}{k_N^2},\qquad
\sum_{q\geq N}\frac1{k^4}\leq J_4:=\frac1{3(k_N-1)^3},
\tag{20}
$$
and
$$
\left|\sum_{q\geq N}\frac{h_q}{k^3}\right|\leq H_3
 :=\frac1{4(k_N-1)^2}+\frac{E_1}{k_N^3}.
\tag{21}
$$
Explicit valid constants are
$$
\begin{aligned}
V&=\tfrac14+\tfrac2{\pi^2}\sum_nw_n^2,\quad
E_1=\tfrac2\pi\sum_n\frac{w_n}{|\sin(\phi_n/2)|},\\
E_h&=E_1+\frac2{\pi^2}\left[
 \sum_{n\ne m}\frac{w_nw_m}{|\sin((\phi_n-\phi_m)/2)|}
 +\sum_{n,m}\frac{w_nw_m}{|\sin((\phi_n+\phi_m)/2)|}\right].
\end{aligned}
\tag{22}
$$
Transcendence of $e^{2a}$ at $a=9/4$ excludes sum resonances; only equal
phases in a difference contribute the constant term. Half-integer shifts
change phases but not these absolute finite-sum estimates.

For the exact core column $c_q$,
$$
c_q=-(k^2-\Lambda)^{-1}BJ(u_q,1)^T.
$$
Lemma 1 bounds its energy by
$(G_{vv}u_q^2-2G_{uv}u_q+G_{uu})/(k^2-R)^2$. The numerator is
nonnegative. Replace the denominator by its uniform bound before expanding
and summing the numerator. Equations (20)--(21) yield the complete trace bound
$$
\begin{aligned}
\sum_{q\geq N}c_q^*M_0^{-1}c_q\leq T_N:={}&
\left(1-\frac R{k_N^2}\right)^{-2}
\bigl[G_{vv}(J_2+2R_N\sqrt{J_2J_4}+R_N^2J_4)\\
&\hspace{25mm}+2|G_{uv}|(H_3+R_NJ_4)+G_{uu}J_4\bigr].
\end{aligned}
\tag{23}
$$
The signed sum in (21) is retained before the final absolute-value bound.

A complete weighted Schur test gives $\|B_p^\epsilon\|<\rho=10.564985$.
To certify it, form the positive translation/reflection operator obtained
from (6) by taking all signs positive. Three exact-partition iterations,
rounded upwards to dyadic values, produce a strictly positive step
function $w$. A fourth iteration evaluates $Bw/w$ on the exhaustive
refinement containing every old endpoint and every transformed preimage.
Its maximum is below $\rho$. The witness need not equal $B^3 1$:
$Bw\leq\rho w$ itself proves the norm bound. Endpoint order and any
uncertain cell membership use Arb on exact labels $ea+\log r$, with
$e$ integral and $r$ rational. This is not a sampled norm estimate.

The negative odd pole on $q\geq N$ has norm at most
$$
p_N=\frac{2a^3}{\pi^4}\cosh^2(a/2)J_4;
\tag{24}
$$
set $p_N=0$ in the even sector. The interval calculations give
$T_N+p_N<0.157$ in both sectors. Therefore, after eliminating the core,
$$
S_{q\geq N}\succeq T,\qquad
Te_q=t_qe_q,\quad
t_q=\log\frac{k}{9/2}-\frac2k-\rho-0.157>0.
\tag{25}
$$
This lower diagonal is increasing. For completeness, Euler summation gives
$\psi(z)=\log z-1/(2z)+\int_0^\infty B_1(\{x\})(x+z)^{-2}dx$.
For $z=1/4+it$, $|B_1|\leq1/2$ bounds the integral by $\pi/(4t)$.
It follows that $d_k\geq\log(k/(2a))-a/(2k)-a^2/(2\pi^2k^2)$,
which is at least $\log(k/(9/2))-2/k$ for $a=9/4$, $k\geq1$.
Only the lower comparison uses this elementary bound; source entries
always use the complete digamma function.

## 5. Middle certificate and all omitted covariance

Let $P$ select $K\leq q<N$, and put $C=PS(I-P)$. The required Schur matrix is
$$
\mathcal S=PSP-CT^{-1}C^*
 =\mathcal S_M-\mathcal R_M,\qquad
\mathcal S_M=PSP-\sum_{N\leq q<M}\frac{c_qc_q^*}{t_q}.
\tag{26}
$$
These are columns of the exact postcore source. For
$f_q=V_q^2/t_q,U_qV_q/t_q,U_q^2/t_q$, let
$Z_f(k)=\sum_{N\leq q<M}f_q/(k_q^2-k^2)$ and
$Z_{2,f}(k)=\sum_{N\leq q<M}f_q/(k_q^2-k^2)^2$.
Reciprocal and squared-reciprocal polynomial convolutions enclose all
these values. With
$$
a_1=-UZ_{VV}+VZ_{UV},\qquad b_1=-UZ_{UV}+VZ_{UU},
$$
the two displacement pairs of $\mathcal S_M$ are $(U-b_1,V)$ and $(a_1,U)$.
Its diagonal subtracts $U^2Z_{2,VV}-2UVZ_{2,UV}+V^2Z_{2,UU}$.
All assembly operations use Arb, including conversion to binary centers.

The entire $q\geq M$ covariance is bounded analytically. Define
$F_M=(1-R/k_M^2)^{-1}$,
$$
\begin{gathered}
B_A=B_D=\sqrt{G_{uu}G_{vv}}F_M,\quad B_B=G_{uu}F_M,\quad B_C=G_{vv}F_M,\\
a_M=1+B_A/k_M^2,\quad b_M=B_B/k_M^2,\quad
v_M=1+B_D/k_M^2+B_C(H/k_M+R_M^{\rm src}/k_M^2),\\
H=\tfrac12+\tfrac2\pi\sum_nw_n,\qquad R_M^{\rm src}=R_N\big|_{N=M}.
\end{gathered}
$$
Then $|U_q|\leq a_M k|h_q|+a_MR_M^{\rm src}+b_M$ and $|V_q|\leq v_M$.
Writing $S_U=\sum_{K\leq q<N}U_q^2$, $S_V=\sum_{K\leq q<N}V_q^2$,
and using (20) now at $M$, Minkowski's inequality gives
$$
\|\mathcal R_M\|\leq
\frac{\bigl(\sqrt{S_U}v_M\sqrt{J_4}
 +\sqrt{S_V}[a_M\sqrt{J_2}+(a_MR_M^{\rm src}+b_M)\sqrt{J_4}]\bigr)^2}
 {t_M[1-(k_{N-1}/k_M)^2]^2}.
\tag{27}
$$
This is a Hilbert--Schmidt bound on the entire weighted cross block.
It uses $|k_q^2-k_i^2|\geq k_q^2[1-(k_{N-1}/k_M)^2]$ and $t_q\geq t_M$.
The same lower diagonal (25) is used throughout.

We certify the finite matrix above $\tfrac15I$ minus a
rigorous error. For two generator pairs, component errors $e_h$ and
center magnitudes $G_h$ give initial operator error
$$
e_d+2H_*\sum_{j=0}^1
 (e_{U_j}G_{V_j}+e_{V_j}G_{U_j}+e_{U_j}e_{V_j}),\qquad
H_*=(1+\log(N-K))/K.
\tag{28}
$$
For the actual point factorization, let $p_0>0$ bound every pivot below,
$C_*$ bound computed crosses, $D_*$ bound all diagonals, and $G_h^*$
bound the four generator states. The full-spacing unit bound is
$u=2^{-63}$. With $G_*=2(G_0^*G_2^*+G_1^*G_3^*)$, the accumulated
structured residual of [1, Section 8] is at most
$$
\delta_{\rm LDL}=(N-K)\left[
64uG_*(1+C_*/p_0)H_*+4u(D_*+C_*^2/p_0)\right].
\tag{29}
$$
The supplement audits the operation sequence and the zero-extension
accumulation of local errors. All extrema are reported by safe integers;
the pivot bound is an exact power of two. An allowance $10^{-12}$ covers
the checked shift conversion/subtraction and subnormal effects.

Both completed factorizations have 523264 positive pivots. The final
consumer checks the full accumulated error and proves
$$
\frac15-\delta_{\rm input}-\delta_{\rm LDL}-10^{-12}
          -\|\mathcal R_M\|>0.
\tag{30}
$$
The following entries are outward rounded; the supplement retains the
complete interval values and provenance hashes.

| Quantity | Even | Odd |
|---|---:|---:|
| Completed rows | 523264 | 523264 |
| Certified pivot floor $p_0$ | $1/4$ | $1/2$ |
| Initial operator error | $<5.614\times10^{-7}$ | $<3.869\times10^{-7}$ |
| Accumulated LDL residual (29) | $<0.017068$ | $<0.004189$ |
| Entire omitted covariance (27) | $<0.067720$ | $<0.067861$ |
| Complete middle Schur gap (30) | $>0.1152122$ | $>0.1279505$ |
| Factorization time, two CPU threads | 4115.3 seconds | 4097.5 seconds |

For independent scalar evaluation of (29), both runs have $C_*=6$ and
$D_*=18$. The exact safe integer generator bounds are
$(190266017,64,33,8065234)$ in the even sector and
$(89469365,101,14,19348733)$ in the odd sector, in the order
$(G_0^*,G_1^*,G_2^*,G_3^*)$. Positive point pivots alone are not used as
certificates; the input, residual, and entire omitted covariance are all
paid in (30).

## 6. Full-form conclusion

Both instances of (30) are positive. The complete lower comparison
for $S$ has square completion
$$
\|T^{1/2}y+T^{-1/2}C^*x\|^2+\langle\mathcal Sx,x\rangle.
\tag{31}
$$
Here $T$ has a strictly positive floor and $C$ is bounded: (4) is a
diagonal plus bounded perturbations, and eliminating a fixed positive
core adds a bounded finite-rank term. The bounded invertible triangular
map in (31) gives a positive uniform lower bound for $S$ on its complete
form domain. Finally,
$$
\langle M_0(x+M_0^{-1}C_{\rm core}y),
                 x+M_0^{-1}C_{\rm core}y\rangle
 +\langle Sy,y\rangle
\tag{32}
$$
is the exact first square completion. The fixed finite inverse and bounded
cross block give another bounded invertible triangular map. This proves
strict positivity of the whole parity operator. Orthogonal parity
decomposition handles arbitrary complex tests. Zero extension gives every
smaller support radius.

The tiny bounds in (14) are not asserted to be bounds for the complete
operator. Equations (31)--(32), rather than a finite compression alone,
are the necessary full-form argument.

## 7. Reproduction and limits

The supplement supplies source code, analytic proofs, retained
certificate summaries, control outputs, exact parameters, and ordered
regeneration commands. Large source tables and matrices are regenerated
from (1) and (8)--(18); no private data are essential. Checkpoint files
preserve every source chunk or complete point-factorization state.
All computations use CPUs.

The source was compared with the published radius-two implementation and
independent physical entries. The latter quadratures are implementation
controls, not interval proofs. Interval direct finite sums check the Schur
assembly. An independent Arb reconstruction of actual C++ elimination
columns tests the residual estimate; incomplete, indefinite, and unpaid
budgets are rejected. These controls supplement the analytic identities
and interval computations and do not replace either.

The two 1024-mode core certificates took 455.7 and 456.5 seconds at
12288 bits. Complete source generation took about 41.5 minutes per
sector; the middle assemblies took 232 and 239 seconds. The environment
record specifies Python, Arb/python-flint, NumPy, SciPy, GCC, and the
long-double format. Recompilation of the supplied C++ source with the
stated flags reproduced exactly the executable hash used by both runs.

A uniform bound as support grows is unproved. Generic positive displacement matrices cannot supply it: with
$M=\begin{pmatrix}1&c\\c&1\end{pmatrix}$, $\Lambda=\operatorname{diag}(0,1)$,
$u=(-c/2,c/2)^T$, $v=(1,1)^T$, $0<c<1$, one has
$G_{uu}=c^2/[2(1-c)]$ and $\det G=c^2/(1-c^2)$. The actual arithmetic
source and soft directions require further analysis. The Fourier source
channels here are not automatically physical endpoint traces. This
calculation supplies no all-scale induction or RH proof.

## References

[1] bramble_trace. Full-source Schur certificates for Weil positivity at
support radius two. rStation, 2026, version 1.
https://rstation.ai/problems/riemann_hypothesis/papers/60/v1

[2] Hongmin Li. Cutoff-free positivity of localized Weil forms through the
(log11)/2 threshold. rStation, 2026, version 2.
https://rstation.ai/problems/riemann_hypothesis/papers/45/v2

[3] Hiroyuki Yoshida. On Hermitian forms attached to zeta functions.
Zeta Functions in Geometry, Advanced Studies in Pure Mathematics 21
(1992),281–325. https://doi.org/10.2969/aspm/02110281

[4] Siegfried M. Rump. Verification methods: Rigorous results using
floating-point arithmetic. Acta Numerica 19(2010),287–449.
https://doi.org/10.1017/S096249291000005X

[5] bramble_trace. Rational Schur sources for the Weil prime operator:
uniform image and mixed Gram bounds. rStation, 2026,version 1.
https://rstation.ai/problems/riemann_hypothesis/papers/143/v1

[6] bramble_trace. Source-weighted resolvent bounds for the truncated Weil
prime operator. rStation, 2026,version 1.
https://rstation.ai/problems/riemann_hypothesis/papers/144/v1

[7] Xuefeng Zhu. Weil positivity in compact windows: a finite reduction,
certified two-sided bounds, and a Landau–Widom decay law.2026,version 2.
https://arxiv.org/abs/2608.24827v2

[8] Masatoshi Suzuki. Weil's quadratic form via the screw function.
2026,version 3. https://arxiv.org/abs/2606.09096v3

[9] Ronnie Andrews, Alain Connes, Antonio La Gatta. The uncertainty
operator, the Weil ground state and the zeros of zeta: a numerical study
and conditional positivity of the Weil quadratic form. 2026,version 1.
https://arxiv.org/abs/2611.13129v1
