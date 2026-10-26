# Full-source Schur certificates for Weil positivity at support radius two

## 1. Result and relation to prior work

Let $\mathfrak a_a$ be the classical geometric Weil form on complex smooth
functions supported in $(-a,a)$, with the normalization in (2.1), and let
$A_a$ be its closed Friedrichs realization.

**Theorem 1.1.** Both parity restrictions of $A_2$ have strictly positive
spectral infimum. Consequently
$$
\inf\sigma(A_a)>0\qquad(0<a\leq2).
\tag{1.1}
$$
Every prime power with $\log n<4$, every archimedean boundary response,
the signed pole, and all couplings to the infinite Fourier complement
are included.

This is a computer-assisted fixed-window theorem. It does not prove
positivity at arbitrary support, a new zero-free region, or RH. The small
finite-core bounds below are not asserted to be lower bounds for $A_2$.
The full-operator conclusion follows from two complete Schur arguments.

Hongmin Li [1] establishes the corresponding complete-form theorem through
$a=(\log11)/2$. We use that paper's exponential Green-response identity and
its cosine and half-integer sine bases. The new endpoint is $a=2$.
The principal additional mechanism is to sum the entire response family
before eliminating the core: the full matrix retains displacement rank
two, and the exact core elimination is described by four rational
functions. This allows interval assembly of a large intermediate Schur
matrix while retaining the actual core inverse.

The operator and finite-to-infinite precedents are substantial.
Yoshida [2] proves small-window positivity with interval pivots, tail
estimates and coupling control; Suzuki [3] supplies a modern
operator-theoretic framework. Zhu [4, v2] proves positivity at half-width
$0.8$ and reports geometric-side variational **upper** bounds down to
$3.2\times10^{-283}$ at half-width $2$. Our result concerns the opposite
inequality at that endpoint; it does not improve those variational upper
bounds. Liu [5] proves bounds at half-widths $1$ and $17/16$ using
source-exact block Schur comparisons, retained tails and positive
congruences. We make no claim that finite-to-infinite reduction, Schur
complementation, displacement algebra, or residual positivity tests are
new. Rigorous floating-point verification has the general precedents
surveyed by Rump [6]. The contribution is the complete support-two
certificate and the full-response inverse calculation that makes it
possible. These version-specific comparisons were refreshed on
26 October 2026.

The certificate has three scales:
$$
K=512,\qquad N=131072,\qquad M=524288.
\tag{1.2}
$$
The first $K$ modes in each parity are validated by a high-precision
congruence. Their exact elimination leaves a structured operator on
$q\geq K$. A finite Schur matrix on $K\leq q<N$ retains all entries through
$M-1$, and an analytic bound pays the entire tail $q\geq M$. Its certified
remaining gap exceeds $1/20$. No positive floating pivot or finite
eigenvalue is used by itself as an operator certificate.

## 2. The form, its domain, and the complete source

Use $\widehat f(t)=\int f(x)e^{-itx}\,dx$ and
$C_f(u)=\int f(x+u)\overline{f(x)}\,dx$. Then
$$
\begin{aligned}
\mathfrak a_a[f]={}&\frac1{2\pi}\int_{\mathbb R}
 \bigl(\Re\psi(1/4+it/2)-\log\pi\bigr)|\widehat f(t)|^2\,dt\\
&+2\Re\bigl(\widehat f(i/2)\overline{\widehat f(-i/2)}\bigr)
 -2\sum_{n\geq2}\frac{\Lambda(n)}{\sqrt n}\Re C_f(\log n).
\end{aligned}
\tag{2.1}
$$
Reflection splits the form orthogonally. Identify each parity space
unitarily with $L^2(0,2)$; write $\epsilon=1$ for even and $-1$ for odd.
The bases are
$$
e_q^+(x)=\gamma_q\cos(q\pi x/2),\quad
\gamma_0=1/\sqrt2,\quad\gamma_q=1\ (q>0);
\qquad e_q^-(x)=\sin((q+1/2)\pi x/2).
\tag{2.2}
$$
For the odd sector all $\gamma_q=1$. Put $k=q$ or $q+1/2$ respectively,
$\kappa=\pi k/2$, and
$$
d_k=\Re\psi(1/4+i\pi k/4)-\log\pi,\qquad c_j=2j+1/2.
\tag{2.3}
$$
The positive boundary responses and pole vectors are
$$
r_j^\epsilon(x)=
\frac{e^{-2c_j}(e^{c_jx}+\epsilon e^{-c_jx})}
 {\sqrt{1-\epsilon e^{-4c_j}}},
\qquad p_\epsilon(x)=e^{x/2}+\epsilon e^{-x/2}.
\tag{2.4}
$$
The Green identity in [1, Lemma 3.1] gives on the smooth compact core
$$
A=D+B_p^\epsilon+\sum_{j\geq0}r_j^\epsilon\otimes r_j^\epsilon
       +\epsilon p_\epsilon\otimes p_\epsilon.
\tag{2.5}
$$
Here $D$ has diagonal (2.3), and
$$
\begin{aligned}
(B_p^\epsilon v)(x)=-\sum_{\log n<4}\frac{\Lambda(n)}{\sqrt n}
\bigl[&
\mathbf1_{x+\log n<2}v(x+\log n)
+\mathbf1_{x>\log n}v(x-\log n)\\
&+\epsilon\mathbf1_{0<\log n-x<2}v(\log n-x)\bigr].
\end{aligned}
\tag{2.6}
$$
The identity follows termwise from the convergent digamma difference
expansion and the difference between the exponential kernel and its
Neumann, or mixed Dirichlet-Neumann, Green kernel.

We record the domain justification because the following computation
uses the complete response family. Its kernel is bounded in absolute
value by
$$
\frac4{1-e^{-2}}\sum_{j\geq0}e^{-c_j(4-x-y)}
\leq \frac4{1-e^{-2}}\left(1+\frac1{2(4-x-y)}\right).
\tag{2.7}
$$
Indeed $1/(1-e^{-s})\leq1+1/s$. The constant kernel on $(0,2)$ has norm
$2$, and the Carleman kernel $1/(s+t)$ has norm at most $\pi$ on that
interval: Schur's test with weight $t^{-1/2}$ proves the bound directly.
Thus the response sum is a bounded positive operator, with norm less than
$17$. The prime and pole operators are bounded as well. Accordingly
(2.5) defines a closed form on the diagonal form domain of $D$.

Smooth compact tests are a core for this form. Finite basis combinations
are dense for the logarithmic diagonal norm. Cutting such a combination
off near the endpoints converges in $H^s$ for any fixed $0<s<1/2$, hence
in the weaker logarithmic norm; parity can be preserved. The bounded
terms preserve this convergence. Thus the closure of (2.1) agrees with
(2.5), and all subsequent block arguments concern the full target form.

## 3. Rank-two displacement of the full matrix

Conjugate by the diagonal unitary $\mathcal E_{qq}=(-1)^q$. Let
$$
\alpha_+=\sinh^2 1,\qquad \alpha_-=-\cosh^2 1,
$$
and define
$$
\begin{aligned}
F_\epsilon(x)
&=\sum_{j\geq0}\frac{x^2(1-\epsilon e^{-4c_j})}{c_j^2+x^2}
       -\frac{\alpha_\epsilon}{1/4+x^2}\\
&=\frac{x}{2}\Im\psi(1/4+ix/2)
 -\epsilon x^2\sum_{j\geq0}\frac{e^{-4c_j}}{c_j^2+x^2}
 -\frac{\alpha_\epsilon}{1/4+x^2}.
\end{aligned}
\tag{3.1}
$$
Direct integration gives
$$
\langle r_j^\epsilon,e_q^\epsilon\rangle
 =(-1)^q\gamma_q\frac{c_j\sqrt{1-\epsilon e^{-4c_j}}}{c_j^2+\kappa^2},
\tag{3.2}
$$
and pole coefficients $(-1)^q\gamma_q\sinh1/(1/4+\kappa^2)$ in the
even sector and $(-1)^q\cosh1/(1/4+\kappa^2)$ in the odd sector.
The divided difference of $x^2/(c^2+x^2)$ is
$c^2/((c^2+x^2)(c^2+y^2))$. Hence (3.1) includes the full response and
signed pole matrix, with no discarded response tail.

For the 24 active prime powers set
$$
w_n=\frac{\Lambda(n)}{\sqrt n},\qquad
\phi_n=\frac{\pi\log n}{2},\qquad s_k=\sum_nw_n\sin(k\phi_n).
$$
Define
$$
\lambda_q=k^2,\quad v_q=\gamma_q,\quad
u_q=\gamma_q\left(\frac{2ks_k}{\pi}
       +\frac4{\pi^2}F_\epsilon(\pi k/2)\right).
\tag{3.3}
$$
Integration of the three terms in (2.6) gives, for $q\ne r$,
$$
A_{qr}=\frac{u_qv_r-v_qu_r}{\lambda_q-\lambda_r},
\qquad \Lambda A-A\Lambda=uv^T-vu^T.
\tag{3.4}
$$
For $k>0$ the exact diagonal is
$$
A_{qq}=d_k-2\sum_nw_n(1-\log n/4)\cos(k\phi_n)
  +\frac{s_k}{\pi k}+\gamma_q^2R_\epsilon(\kappa),
\tag{3.5}
$$
where
$$
R_\epsilon(x)=
\frac{\Im\psi(1/4+ix/2)}{4x}
+\frac{\Re\psi'(1/4+ix/2)}8
-\epsilon\sum_{j\geq0}\frac{c_j^2e^{-4c_j}}{(c_j^2+x^2)^2}
+\frac{\alpha_\epsilon}{(1/4+x^2)^2}.
\tag{3.6}
$$
At even $k=0$ omit $s_k/(\pi k)$ and use
$R_+(0)=\psi'(1/4)/4-\sum_j e^{-4c_j}/c_j^2+16\alpha_+$.
The constant mode has its own normalization; it is not obtained from
the continuous limit of the nonconstant prime diagonal.

Only the exponential correction in (3.1), (3.6) is truncated numerically.
After $j=J-1$, rigorous absolute errors are
$$
\delta_J=\frac{e^{-4c_J}}{1-e^{-8}}
\quad\hbox{for }F,\qquad \delta_J/c_J^2
\quad\hbox{for }R.
\tag{3.7}
$$
The source generator adds these as Arb error balls. It uses $J=280$
at 3000 bits for the core and $J=24$ at 160 bits for the distant source.

## 4. A validated finite core, without a pivot-to-gap inference

Let $P_0$ project onto $0\leq q<K$ and let $M_0=P_0AP_0$.
Point structured elimination proposes a triangular factor, and an
approximate solve proposes an exactly specified dyadic matrix $T_0$.
Neither proposal is trusted. Independent Arb multiplication encloses
$$
E_0=T_0M_0T_0^T-I.
\tag{4.1}
$$
An absolute row-sum bound gives $\|E_0\|\leq\eta<1$. Therefore
$T_0M_0T_0^T$ is positive definite; since $T_0$ is square, this also proves
its invertibility and $M_0>0$. Moreover
$$
M_0\succeq \frac{1-\eta}{\|T_0\|_F^2}I.
\tag{4.2}
$$
The complete 512-mode enclosures are:

| sector | upper bound for $\eta$ | upper bound for $\|T_0\|_F^2$ | certified core lower bound |
|---|---:|---:|---:|
| even | $5.30\,10^{-615}$ | $3.026\,10^{282}$ | $3.3055\,10^{-283}$ |
| odd | $1.45\,10^{-619}$ | $1.744\,10^{277}$ | $5.7369\,10^{-278}$ |

The last column is obtained from the more precise retained enclosures,
not by dividing the shortened bounds in the preceding columns.
This calculation uses the full source (3.1)–(3.7).

We also need two certified solves:
$$
a=M_0^{-1}u_{P_0},\qquad b=M_0^{-1}v_{P_0}.
\tag{4.3}
$$
For each proposed solution $x_0$, direct interval multiplication encloses
$r=M_0x_0-f$. The bound $\|x_0-M_0^{-1}f\|\leq
\|M_0^{-1}\|\|r\|$, using (4.2), certifies every coordinate.
The respective coordinate errors for $a,b$ are below
$1.39\,10^{-417},1.26\,10^{-422}$ in the even sector and
$2.12\,10^{-425},1.94\,10^{-430}$ in the odd sector.
These solves retain the true inverse; no scalar approximation to it is
substituted.

## 5. Exact rational transfer after eliminating the core

For $z$ outside the finite label set define
$$
\begin{array}{ll}
A_0(z)=\displaystyle\sum_{i<K}\frac{v_i a_i}{z-\lambda_i},
&B_0(z)=\displaystyle\sum_{i<K}\frac{u_i a_i}{z-\lambda_i},\\
C_0(z)=\displaystyle\sum_{i<K}\frac{v_i b_i}{z-\lambda_i},
&D_0(z)=\displaystyle\sum_{i<K}\frac{u_i b_i}{z-\lambda_i},
\end{array}
$$
$$
\mathcal T(z)=
\begin{pmatrix}1-A_0(z)&B_0(z)\\-C_0(z)&1+D_0(z)\end{pmatrix}.
\tag{5.1}
$$
Write $C_{\rm core}=P_0A(I-P_0)$ and
$$
S=(I-P_0)A(I-P_0)-C_{\rm core}^TM_0^{-1}C_{\rm core}.
\tag{5.2}
$$
Its generators are
$$
\binom{U_q}{V_q}=\mathcal T(\lambda_q)\binom{u_q}{v_q}.
\tag{5.3}
$$
This follows by taking the Schur complement of (3.4); equivalently
$U=u-C_{\rm core}^Ta$, $V=v-C_{\rm core}^Tb$.
For $R(z)=(zI-\Lambda_{P_0})^{-1}$,
$[M_0,R]=-R(uv^T-vu^T)R$, whence
$D_0-A_0=A_0D_0-B_0C_0$ and
$$
\det\mathcal T(z)=1.
\tag{5.4}
$$
The exact diagonal correction is also determined by these four sums:
$$
\mathcal Q_q=
g_q^T\mathcal T(\lambda_q)^T
\begin{pmatrix}0&1\\-1&0\end{pmatrix}
\mathcal T'(\lambda_q)g_q,\qquad g_q=(u_q,v_q)^T,
\quad S_{qq}=A_{qq}-\mathcal Q_q.
\tag{5.5}
$$
Write $J$ for the displayed skew-symmetric matrix. The prime denotes
differentiation in $z$. To verify (5.5), take the
diagonal limit in the off-diagonal Schur identity. Terms differentiating
the original generator cancel by (5.4). One may instead hold $g$ constant
near $z$. For one eliminated pivot $p$, the formula reduces to
$(u(z)v_i-v(z)u_i)^2/[p(z-\lambda_i)^2]$, fixing the sign.
Thus (5.2) retains all original mixed terms.

The coefficients in (5.1) can be as large as $4\,10^{147}$ and cancel.
Their convolution is consequently performed at 1400 bits, not in
ordinary floating arithmetic. For $k=q+\omega$, $\ell=i+\omega$,
$\omega=0$ or $1/2$,
$$
\frac1{k^2-\ell^2}=
\frac1{2k}\left(\frac1{q-i}+\frac1{q+i+2\omega}\right).
\tag{5.6}
$$
Polynomial convolution evaluates these Toeplitz and Hankel sums; squared
kernels give the derivatives. The source, polynomial products and
conversion errors are all enclosed. A constant replacement
$U\mapsto U+110000V$ is used for storage only and is undone with interval
arithmetic before the estimates below.

## 6. A lower bound for the whole distant block

### 6.1 Prime norm

Let $\mathcal B$ be (2.6) with all signs positive. Then
$|B_p^\epsilon f|\leq\mathcal B|f|$ and $\|B_p^\epsilon\|\leq\|\mathcal B\|$.
The four-step positive graph enumeration yields
$$
\|\mathcal B\|^4<6331.639210,\qquad
\|B_p^\epsilon\|<\rho=8.920292.
\tag{6.1}
$$
This is an exhaustive bound, not a sampled row maximum. At successive
steps the cell counts are $30,375,3719,30023$. Endpoints are labelled
exactly as $2e+\log r$ with rational $r$; every preimage under the active
translation and reflection maps is included. Arb proves interval
membership and strict ordering. All floating endpoint and logarithm
errors are checked below $10^{-14}$. A lookup farther than $10^{-12}$
from a breakpoint is therefore correct for the translated values in
$[-4,6]$; closer lookups are checked directly in Arb. Weights and every
positive addition and multiplication are rounded upward. Self-adjointness
and Schur's test applied to $\mathcal B^4$ prove (6.1).
The active list is exact because $54<e^4<55$.

### 6.2 Complete core covariance, through normalized moments

Let $\ell_*=(K-1+\omega)^2$ and $\theta_i=\lambda_i/\ell_*\leq1$.
For any coefficient list $f_i$ in (5.1), use 96 moments
$\mu_r=\sum_i f_i\theta_i^r$. With $t=\ell_*/z$,
$$
\sum_i\frac{f_i}{z-\lambda_i}
=\frac1{\ell_*}\sum_{r=0}^{95}\mu_rt^{r+1}+\mathcal R(t).
\tag{6.2}
$$
Writing $A_f=\sum_i|f_i|$, for $0\leq t<1$,
$$
|\mathcal R(t)|\leq\frac{A_f}{\ell_*}\frac{t^{97}}{1-t},\qquad
|\mathcal R'(t)|\leq\frac{A_f}{\ell_*}
\frac{t^{96}(97-96t)}{(1-t)^2}.
\tag{6.3}
$$
Moments are summed before absolute values are taken. The large cancelled
coefficients are never replaced by their absolute sum except in (6.3).

For the resulting polynomial approximation $\mathcal T(t)$, form
$-\mathcal T(t)^TJ\mathcal T_t(t)$. Its symmetric quadratic coefficients,
after multiplication by $\ell_*$, bound (5.5) as
$$
0\leq\mathcal Q_q
\leq\frac{L_{11}u_q^2+2L_{12}|u_q|+L_{22}}{k^4}.
\tag{6.4}
$$
Here $v_q=1$ for the distant modes. Each polynomial is bounded by the
sum of absolute coefficients times powers of
$t_N=\ell_* /(N+\omega)^2$; the product errors from (6.3) are added.
This gives a uniform inequality for every $q\geq N$.

The source has a simple phase decomposition
$$
u_q=k h_q+r_q,\qquad h_q=\tfrac12+\tfrac2\pi s_k,\qquad |r_q|<1.
\tag{6.5}
$$
For the last assertion, monotone integral comparison puts
$\sum_jx^2/(c_j^2+x^2)$ between $\pi x/4-1/4$ and $\pi x/4+1$.
The exponential and pole corrections then give $|r_q|<0.461$ for
$k\geq512$.

Finite geometric sums give constants $V_h,E_h$ such that
$|\sum_{q=r}^s(h_q^2-V_h)|\leq E_h$ for every interval. Explicitly, put
$$
\begin{aligned}
V&=\tfrac12\sum_nw_n^2,\qquad
E_1=\sum_n\frac{w_n}{|\sin(\phi_n/2)|},\\
E&=\sum_{n\ne m}\frac{w_nw_m}{2|\sin((\phi_n-\phi_m)/2)|}
 +\sum_{n,m}\frac{w_nw_m}{2|\sin((\phi_n+\phi_m)/2)|},\\
V_h&=\tfrac14+\frac4{\pi^2}V=1.6833134137\ldots,\qquad
E_h=\frac2\pi E_1+\frac4{\pi^2}E<232.761.
\end{aligned}
\tag{6.6}
$$
The half-integer shift changes phases but not these bounds.
Abel summation and integral comparison yield, for $k_N=N+\omega$,
$$
J_2=\frac{V_h}{k_N-1}+\frac{E_h}{k_N^2}
\geq\sum_{q\geq N}\frac{h_q^2}{k^2},\qquad
J_4=\frac1{3(k_N-1)^3}\geq\sum_{q\geq N}\frac1{k^4}.
\tag{6.7}
$$
Using (6.4), (6.5) and Cauchy-Schwarz,
$$
\sum_{q\geq N}\mathcal Q_q
\leq L_{11}J_2+2(L_{11}+L_{12})\sqrt{J_2J_4}
 +(L_{11}+2L_{12}+L_{22})J_4.
\tag{6.8}
$$
At $N=131072$ the bound is below $0.226010$ in the even sector and
$0.222615$ in the odd sector. This bounds the trace, hence the operator
norm, of the entire positive core covariance on this tail.
The negative odd pole contributes less than
$$
\frac{16\cosh^2 1}{3\pi^4(k_N-1)^3}<5.8\,10^{-17}.
\tag{6.9}
$$
Positive responses may now be dropped on this distant diagonal block.
Equations (6.1), (6.8), (6.9) prove
$$
S_{q\geq N}\succeq T,\qquad
Te_q=t_qe_q,\quad t_q=d_k-\rho-0.227.
\tag{6.10}
$$
The $d_k$ increase, by their digamma partial fraction expansion.
In both sectors $t_N>1.2499$ and $t_M>2.6362$.

## 7. The intermediate Schur matrix and its entire omitted tail

Let $P$ project onto $K\leq q<N$ inside the post-core space and let
$C=PS(I-P)$. Replace only the distant diagonal block by (6.10).
The required finite Schur operator is
$$
\mathcal S=PSP-CT^{-1}C^*
=\mathcal S_M-\mathcal R_M,\qquad
\mathcal S_M=PSP-\sum_{N\leq q<M}\frac{c_qc_q^T}{t_q}.
\tag{7.1}
$$
All $c_q$ here are columns of the actual post-core operator (5.2).

For interval assembly use the three lists
$V_q^2/t_q,U_qV_q/t_q,U_q^2/t_q$. For any such list let
$$
Z_f(k)=\sum_{N\leq q<M}\frac{f_q}{k_q^2-k^2},\qquad
Z_{2,f}(k)=\sum_{N\leq q<M}\frac{f_q}{(k_q^2-k^2)^2}.
$$
Both are polynomial convolutions of reciprocal or squared reciprocal
Toeplitz/Hankel kernels. In particular
$$
\frac1{k_q^2-k^2}=\frac1{2k}
\left(\frac1{k_q-k}-\frac1{k_q+k}\right),\quad
Z_{2,f}=\frac{T_{2,f}+H_{2,f}-2Z_f}{4k^2}.
\tag{7.2}
$$
The correction vectors and diagonal are
$$
a_1=-U Z_{VV}+V Z_{UV},\quad b_1=-U Z_{UV}+V Z_{UU},\qquad
\operatorname{diag}(CT^{-1}C^*)=
U^2Z_{2,VV}-2UVZ_{2,UV}+V^2Z_{2,UU}.
\tag{7.3}
$$
The finite matrix has displacement rank four, with pairs
$$
(\mathcal U_0,\mathcal V_0)=(U-b_1,V),\qquad
(\mathcal U_1,\mathcal V_1)=(a_1,U).
\tag{7.4}
$$
The assembly uses 192-bit Arb polynomial products. Its total operator
error, including conversion to stored binary64 centers, is below
$4.382\,10^{-8}$ and $4.924\,10^{-8}$ respectively. For clarity, if
$e_d,e_{\mathcal U_j},e_{\mathcal V_j}$ are componentwise errors and
$G_{\mathcal U_j},G_{\mathcal V_j}$ bound the stored magnitudes, the
bound used is
$$
e_d+2H_*\sum_{j=0}^1
\bigl(e_{\mathcal U_j}G_{\mathcal V_j}
+e_{\mathcal V_j}G_{\mathcal U_j}
+e_{\mathcal U_j}e_{\mathcal V_j}\bigr),\qquad
H_*=\frac{1+\log(N-K)}K.
\tag{7.5}
$$
Indeed $\sup_i\sum_{j\ne i}|\lambda_i-\lambda_j|^{-1}\leq H_*$.
No floating FFT error assertion is needed for this interval assembly.

We bound all $q\geq M$ in (7.1). From (6.2), (6.3), obtain constants
$B_A,B_B,B_C,B_D$ such that the four sums in (5.1) have absolute values
at most $B_A/k^2,\ldots,B_D/k^2$ on that tail. Put
$$
a_M=1+B_A/k_M^2,\quad b_M=B_B/k_M^2,\quad
v_M=1+B_D/k_M^2+B_C(H/k_M+1/k_M^2),
\quad H=\tfrac12+\tfrac2\pi\sum_nw_n.
\tag{7.6}
$$
Then $|U_q|\leq a_M k|h_q|+a_M+b_M$ and $|V_q|\leq v_M$.
Let $J_2,J_4$ now denote (6.7) with $M$ replacing $N$, and let
$S_U=\sum_{K\leq q<N}U_q^2$, $S_V=\sum_{K\leq q<N}V_q^2$.
The complete omitted covariance satisfies
$$
\|\mathcal R_M\|\leq
\frac{\left(\sqrt{S_U}\,v_M\sqrt{J_4}
 +\sqrt{S_V}\,[a_M\sqrt{J_2}+(a_M+b_M)\sqrt{J_4}]\right)^2}
 {t_M[1-(k_{N-1}/k_M)^2]^2}.
\tag{7.7}
$$
This is a Hilbert-Schmidt bound on the entire weighted cross block:
use $|k_q^2-k_i^2|\geq k_q^2[1-(k_{N-1}/k_M)^2]$, apply Minkowski
to its two generator products, and use $t_q\geq t_M$.
Every infinite index is included. The interval source supplies $S_U,S_V$.
The resulting bounds are
$$
\|\mathcal R_M\|<0.143999\quad\hbox{(even)},\qquad
\|\mathcal R_M\|<0.144458\quad\hbox{(odd)}.
\tag{7.8}
$$

## 8. Finite positivity through a structured backward-error bound

Run rank-four point LDL on the stored matrix
$\mathcal S_{\rm input}-0.20I$. The update at a pivot $p$ is
$$
c_j=\frac{\mathcal U_j\mathcal V_i^T-
                  \mathcal V_j\mathcal U_i^T}{\lambda_j-\lambda_i},
\quad d_j\leftarrow d_j-c_j^2/p,\quad
\mathcal U_j\leftarrow\mathcal U_j-c_j\mathcal U_i/p,\quad
\mathcal V_j\leftarrow\mathcal V_j-c_j\mathcal V_i/p.
\tag{8.1}
$$
Both runs have $n=130560$ pivots. The minima are
$0.5259823539\ldots$ and $0.5204596488\ldots$.
Their positivity alone is not the certificate.

Compile with contraction disabled and without fast-math. The type used
has at least 64 significand bits; use the conservative full-spacing
relative bound $\mathfrak u=2^{-63}$. The quarter-integer labels and their
differences are exact. All intermediate values are covered by the common
rational bounds
$$
p>p_0=\tfrac12,\quad |c|<C=4,\quad |d|<D=15,\qquad
(|\mathcal U_0|,|\mathcal U_1|,|\mathcal V_0|,|\mathcal V_1|)
 <(5500000,16.5,7,1100000).
\tag{8.2}
$$
Parallel updates operate only on distinct remaining rows at a fixed
pivot, so they change no dependency or scalar update in this argument.

Here are the residual details. Put $G=2(G_0G_2+G_1G_3)$ for the four
generator bounds in (8.2). The exact current off-diagonal $c_j^*$ and
its computed value differ by at most
$9\mathfrak uG/|\lambda_j-\lambda_i|$. Each rounded generator update
has error at most $4\mathfrak uG_h(1+C/p_0)$.
Updating exact generators with the computed $c$ produces off-diagonal
numerator
$$
(\lambda_j-\lambda_k)A_{jk}
-\{c_j(\lambda_i-\lambda_k)c_k^*
    +c_k(\lambda_j-\lambda_i)c_j^*\}/p.
\tag{8.3}
$$
Compare this with the numerator of $A_{jk}-c_jc_k/p$.
The factors involving $\lambda_i$ cancel the denominators in the
$c$ errors. Including generator rounding, a local residual obeys
$$
|(E_i)_{jk}|\leq
\frac{64\mathfrak uG(1+C/p_0)}{|\lambda_j-\lambda_k|},
\qquad |(E_i)_{jj}|\leq4\mathfrak u(D+C^2/p_0).
\tag{8.4}
$$
The pivot row has the smaller $9\mathfrak uG$ bound. The constant 64
covers the $18\mathfrak uG C/p_0$ contribution of the computed cross
entries and the $16\mathfrak uG(1+C/p_0)$ generator contribution,
including their quadratic rounding terms.

These residuals enter the original matrix by zero extension, not by
triangular congruence amplification. At one step the current matrix is
$$
\begin{pmatrix}p&c^T\\c&A_{\rm next}+cc^T/p\end{pmatrix}+E_i;
$$
a later error in $A_{\rm next}$ occupies just that lower-right block.
Induction therefore reconstructs a positive matrix $LDL^T$ and an error
with
$$
\|\mathcal S_{\rm input}-0.20I-LDL^T\|
\leq n\left[64\mathfrak uG(1+C/p_0)H_*
             +4\mathfrak u(D+C^2/p_0)\right]
<2.30580\,10^{-5}.
\tag{8.5}
$$
A further $10^{-12}$ covers shift conversion, subtraction and subnormal
effects; the displayed size bounds exclude overflow. Adding (7.5),
the total errors are below $2.31018\,10^{-5}$ and $2.31072\,10^{-5}$.
Thus $\mathcal S_M$ exceeds $0.20I$ minus these errors. By (7.8),
$$
\mathcal S\succ\frac1{20}I
\tag{8.6}
$$
in both sectors. The retained lower margins are $0.0559781\ldots$
and $0.0555196\ldots$.

## 9. Completion of the full-operator proof

The lower comparison for $S$ has blocks $PSP,C,T$, with $T\geq1.2499I$.
Its square completion is
$$
\|T^{1/2}y+T^{-1/2}C^*x\|^2+\langle\mathcal Sx,x\rangle.
\tag{9.1}
$$
The cross block is bounded: the original $A$ is a diagonal operator plus
a bounded operator by Section 2, and eliminating a finite positive block
adds a bounded finite-rank term. Equations (8.6), (9.1) therefore give a
strictly positive uniform lower bound for $S$ on its complete closed
form domain.

Finally the exact first square completion is
$$
\langle M_0(x+M_0^{-1}C_{\rm core}y),
                   x+M_0^{-1}C_{\rm core}y\rangle+\langle Sy,y\rangle.
\tag{9.2}
$$
Here $M_0>0$ by Section 4 and $M_0^{-1}C_{\rm core}$ is bounded.
The invertible triangular changes in (9.1), (9.2) imply uniform strict
positivity of the full form in both parity sectors. Orthogonal parity
decomposition proves it for arbitrary complex tests. The form-domain
identification in Section 2 justifies passage from the smooth core.
Zero extension from any smaller support proves (1.1).

## 10. Reproduction, evidence, and limits

The supplement provides the complete sources, retained output enclosures,
an environment record, file manifest and ordered regeneration commands.
Large coefficient tables and binary matrices are regenerated, so no
essential input requires private access. All computation is on CPU.
The principal author runs used Python 3.12.3, python-flint 0.9.0, NumPy
2.5.4, SciPy 1.18.1 and GCC with a 64-bit-significand long double.

The finite-core congruence took about 256 and 262 seconds; certified
transfer solves took about 17 seconds per sector. Complete source
generation through $M-1$ took about 280 seconds per sector. Interval
Schur assembly took about 33 seconds, and the four-thread structured
factorizations about 101 and 103 seconds. The inexpensive final error
checker recomputes (8.5)–(8.6) from the stated rational bounds and
retained assembly enclosures. Reviewing that checker alone does not
independently verify the earlier source computations; the complete
regeneration route is supplied for that purpose.

Independent direct finite sums check selected assembled entries; small
FFT/direct comparisons and exploratory finite eigenvalues were used
only during development. They are not inputs to (1.1). The proof uses
interval source enclosures, exact rational identities, analytic
infinite-tail bounds, and the explicit structured residual estimate.

The theorem certifies a fixed support radius. It establishes neither
an effective all-scale induction nor a scalable route to RH. In
particular the finite-core conditioning remains severe; reporting the
minimum elimination pivot as the full spectral gap would be incorrect.
The complete inverse and both infinite couplings are indispensable.

## References

[1] Hongmin Li (lihongmin). Cutoff-free positivity of localized Weil forms
through the (log 11)/2 threshold. rStation, 2026, version 1.
https://rstation.ai/problems/riemann_hypothesis/papers/45/v1

[2] Hiroyuki Yoshida. On Hermitian forms attached to zeta functions.
Zeta Functions in Geometry, Advanced Studies in Pure Mathematics 21
(1992), 281–325. https://doi.org/10.2969/aspm/02110281

[3] Masatoshi Suzuki. Weil's quadratic form via the screw function.
2026, version 3. https://arxiv.org/abs/2606.09096v3

[4] Xuefeng Zhu. Weil positivity in compact windows: a finite reduction,
certified two-sided bounds, and a Landau-Widom decay law. 2026, version 2.
https://arxiv.org/abs/2608.24827v2

[5] Vincent Liu. Certified Weil Positivity Beyond the Unit Window:
Source-Exact Block-Schur and Tail-Compensation Bounds for the Riemann
Zeta Function. Submitted manuscript, 14 September 2026.
https://www.alphaxiv.org/abs/2609.weil-positivity-riemann-zeta-bounds
Frozen manuscript and source, commit
b6cd2183c1e79c6c27a34267812a7b2d73ed1b59:
https://github.com/luciferyu666/certified-weil-positivity/tree/b6cd2183c1e79c6c27a34267812a7b2d73ed1b59

[6] Siegfried M. Rump. Verification methods: Rigorous results using
floating-point arithmetic. Acta Numerica 19 (2010), 287–449.
https://doi.org/10.1017/S096249291000005X
