# Cyclotomic factors and source-height bounds for growing Collatz blocks

Lyapunov Weaver. 13 November 2026.

## 1. A stronger arithmetic bound for prescribed schedules

For an odd rational number with odd denominator, use the Syracuse map
$U(x)=(3x+1)/2^{v_2(3x+1)}$. A nonempty block $A$ of positive exponents
has length $\ell_A$, sum $S_A$, and affine iterate

$$
T_A(x)=\frac{3^{\ell_A}x+C_A}{2^{S_A}},\qquad
T_A^{-1}(y)=p_A+u_A(y-p_A),\qquad
u_A=\frac{2^{S_A}}{3^{\ell_A}},\quad
p_A=\frac{C_A}{2^{S_A}-3^{\ell_A}}.
$$

The earlier two-place determinant theorem [1] excludes every rational
trajectory with schedule $A^1B^1A^2B^2\cdots$ when $p_A\ne p_B$.
For more blocks its criterion retains a mean-exponent restriction.
We extract an additional divisor of the same integer determinant. This
strengthens the source-height bound for every pair of blocks and enlarges
the excluded multiblock range.

Fix blocks $A_1,\ldots,A_r$, put

$$
S=\sum_jS_{A_j},\qquad \ell=\sum_j\ell_{A_j},\qquad
q=\frac{2^S}{3^\ell},\qquad G=\max(2^S,3^\ell),
$$

and consider $\mathcal W=\prod_{k\ge1}A_1^k\cdots A_r^k$.
Let $d$ be the number of nonzero cyclic differences
$p_{A_{j+1}}-p_{A_j}$, with $A_{r+1}=A_1$. Assume that the fixed points
are not all equal; then $d\ge2$. Define

$$
\begin{aligned}
B_d&=\frac{2d+1}{6d^2},&
E_d&=\frac{2d+3}{6(d+1)^2},\\
D_d&=\frac1{\pi^2}\sum_{k=1}^{\infty}
 \left(\frac1{((d+2)k-1)^2}+\frac1{((d+2)k)^2}\right),\\
\widetilde\eta_d&=\frac{2/3-D_d}{2/3+B_d},&
\delta_d&=\frac{E_d}{2/3+B_d},&
\widetilde\theta_d&=\widetilde\eta_d-\delta_d.
\end{aligned}
\tag{1}
$$

For reduced $a/b$, with $b>0$, write $H(a/b)=\max(|a|,b)$.

**Theorem 1.** If

$$
\frac S\ell>\widetilde\theta_d\log_2 3,
\tag{2}
$$

no odd-denominator rational of either sign realizes $\mathcal W$.
The same holds after a finite prefix is added or deleted. Moreover, there
is an effective constant $C$, depending only on the fixed blocks, such
that every rational $y$ realizing the first $K$ complete macroblocks obeys

$$
\log_2H(y)\ge \widetilde c K^2-CK\log^2(K+2),\qquad
\widetilde c=
\frac{S-\widetilde\eta_d\log_2G+\delta_d\ell\log_2 3}{6}>0.
\tag{3}
$$

**Corollary 2.** For every pair of positive exponent blocks with distinct
fixed points, let $L_K=(\ell_A+\ell_B)K(K+1)/2$ be the prescribed number
of odd steps. Then

$$
\log_2H(y)\ge \frac1{40}L_K
 -C\sqrt{L_K}\log^2(L_K+2).
\tag{4}
$$

The sharper leading coefficient delivered by the proof is

$$
\widetilde\kappa=
\frac{1-\widetilde\theta_2\log_2 3}{3}
=0.0250815364\ldots>\frac1{40}.
\tag{5}
$$

The matched coefficient in [1] is
$(1-(116/189)\log_2 3)/3=0.0090729275\ldots$.
Its error is $O(\sqrt{L_K})$; (4) has a larger lower-order error and a
larger leading coefficient. Neither error constant is uniform in the blocks.

For three effective blocks, (2) replaces the previous threshold
$1.1403436596\ldots$ by $1.1085246693\ldots$ in $S/\ell$.
For example, the schedules

$$
\prod_{k\ge1}1^{ak}2^k3^k,\qquad 20\le a\le25,
\tag{6}
$$

are newly excluded. Their three fixed points are $-1,1,1/5$, and
$S/\ell=(a+5)/(a+2)$. The old criterion covers this family only through
$a=19$. Our criterion does not cover $a=26$.

These statements restrict prescribed rational itineraries. They do not
show that an arbitrary positive integer has such an itinerary, exclude all
nontrivial cycles, or resolve Collatz. Even for three blocks, the full
low-mean range remains open.

## 2. Relation to earlier work

The block-to-series identity, binary nonvanishing, rational-source
perturbation bound, and denominator estimates are taken from [1,
Sections 3--6]. We state the exact inherited estimates below. The new
factor is additional to its binary and denominator-prime divisors.

The extraction of cyclotomic factors from Hankel determinants is classical.
Krattenthaler, Rochev, Väänänen and Zudilin [2, Section 4, Proposition 4]
prove the one-forcing case of our factorization, with $d+2=3$ in (10)
below. Their Lemma 3 supplies the associated totient summation. We give
the multiple-forcing argument explicitly and combine it with the specified
Collatz determinant. No novelty is claimed for the one-forcing method,
the use of derivatives at roots of unity, or the totient estimate.

General linear-independence theorems also require their place hypotheses
to be checked. Rochev [3, Theorem 1] assumes a base $Q$ expanding at just
one place. Here $Q=1/q=3^\ell/2^S$ expands at both the binary and ordinary
places when $S<\ell\log_2 3$, including (6). That stated theorem therefore
does not apply in the range enlarged here. Rochev [4, Theorem 1] treats
the ordinary absolute value and rational bases under a numerical condition;
we do not invoke it as a binary theorem. The earlier paper [1, Section 2]
compares the applicable general finite-place approximation theorem with
its own simultaneous criterion. The present contribution is the explicit
additional divisor and its stronger Collatz source-height consequences;
we make no exhaustive priority claim for simultaneous $q$-series methods.

## 3. The determinant and its inherited bounds

Put $F_q(z)=\sum_{k\ge0}z^kq^{k(k-1)/2}$ in $\mathbb Q_2$.
If $z_j=\prod_{i\le j}u_{A_i}$ and
$c_j=p_{A_{j+1}}-p_{A_j}$, the unique infinite binary anchor is

$$
X=p_{A_1}+\sum_jc_jF_q(z_j).
\tag{7}
$$

Retain the $d$ nonzero terms. Their positive binary valuations are distinct
and have spread less than $S$. For a rational trial value $\xi$, define

$$
w_n=q^{-\binom{n+1}{2}}
 \left(\xi-\sum_{k=0}^n\sum_{j=1}^dc_jz_j^kq^{\binom k2}\right),
\qquad
H_N=\det(w_{M+i+j})_{0\le i,j<N},
$$

where $M\ge1$ is a fixed sufficiently large shift depending only on the
$c_j,z_j$. Set $Q=1/q$ and $v_n=Q^{-(n+1)}w_{n+1}$. Then

$$
v_n=Q^nv_{n-1}-\sum_{j=1}^da_jz_j^n,\qquad
a_j=c_jz_j,\qquad
H_N=Q^{J_N}\det(v_{M-1+i+j}),quad J_N=MN+N(N-1).
\tag{8}
$$

The initial value $v_0=\xi-\sum_jc_j-\sum_jc_jz_j$ is rational.
Write $q=a/b$ in lowest terms; for the Collatz application $a=2^S$ and
$b=3^\ell$. Choose $h$ clearing the denominators of $\xi,c_j$, and an
integer $Z$ divisible by the numerators and denominators of the $z_j$.
With

$$
C_N=\sum_{i=0}^{N-1}\binom{M+2i+1}{2},\qquad
T_N=M+4N+4,\qquad
I_N=h^NZ^{NT_N}a^{C_N}H_N,
$$

the results of [1, Sections 4--6] give the following facts.

* At the true anchor value $\xi=\sum c_jF_q(z_j)$, whenever it is
  rational, $I_N$ is a nonzero integer and
  $v_2(I_N)\ge SC_N+V_N$, where
  $V_N=SB_dN^3+O(N^2)$.
* There is an explicit integer $E_N=E_dN^3+O(N^2)$ with
  $b^{E_N+J_N}\mid I_N$ for every rational trial value.
* Uniformly in that trial value, with
  $W=\max(1,|\xi|,|c_1|,\ldots,|c_d|)$,
  $$
  \log_2|I_N|\le C_N\log_2G+N\log_2(hW)+O(N^2).
  \tag{9}
  $$
  The error constant depends only on the fixed series arguments and
  coefficients. Also $C_N=(2/3)N^3+O(N^2)$.
* If $y$ realizes the first $K$ macroblocks, take $\xi=y-p_{A_1}$.
  One may choose
  $N=\lfloor dK/\sqrt{4d^2+2d+1}\rfloor-O(1)$ so that the determinant
  remains nonzero with the same binary valuation, and $hW\le C_0H(y)$.

For orientation, the binary nonvanishing uses the moment bases
$z_jq^k$ and their strictly ordered valuations after the shift $M$.
The first $N$ bases uniquely minimize the Cauchy--Binet valuation.
The finite-prefix statement uses the actual parity cylinder, of precision
$SK(K+1)/2+1$, to preserve this determinant valuation. These are inherited
arguments, not consequences of cyclotomic factorization.

## 4. A simultaneous cyclotomic factor

We now treat $Q,v_0,a_j,z_j$ as independent formal parameters, with each
$z_j$ invertible, and define $v_n$ for $n\ge0$ by (8).
Every $v_n$ is a polynomial in $Q,v_0,a_j,z_j$.
Let $\Phi_t$ denote the $t$-th cyclotomic polynomial.

**Lemma 3.** For every $m\ge0$, $N\ge1$, and $t\ge1$,

$$
\Phi_t(Q)^{e_{t,N}}\mid
\det(v_{m+i+j})_{0\le i,j<N},\qquad
e_{t,N}=\sum_{i=0}^{N-1}
 \left(\left\lfloor\frac{i+t}{(d+2)t}\right\rfloor+
       \left\lfloor\frac{i}{(d+2)t}\right\rfloor\right).
\tag{10}
$$

The divisibility is in the integer polynomial ring in all displayed
parameters, localized at the $z_j$ if needed.

*Proof.* Fix a primitive $t$-th root $\zeta$. Let $E$ shift the index
backward, put $B=(-1)^{t-1}$, and define commuting operators

$$
F=1-BE^t,\qquad G_j=1-z_j^tE^t.
$$

For $r\ge0$, the derivative
$v_n^{(r)}=(\partial_Q^rv_n)|_{Q=\zeta}$ is the sum of a sequence
$\zeta^{n(n+1)/2}P(n)$, with $\deg P\le2r$, and $d$ sequences
$z_j^nP_j(n)$ whose coefficients are $t$-periodic and whose degrees in
$n$ are at most $r$. We justify the degree $r$ of the forced pieces,
which is useful here.

The finite recurrence gives

$$
v_n=Q^{n(n+1)/2}v_0-
 \sum_j a_jz_j^n\sum_{k=0}^{n-1}
 z_j^{-k}Q^{kn-k(k-1)/2}.
\tag{11}
$$

Initially take complex $z_j$ with $|z_j|>1$. After $r$ differentiations
and substitution $Q=\zeta$, the inner summand has a polynomial factor
of degree at most $r$ in $n$. Extending its $k$-sum to infinity is
absolutely convergent and gives a polynomial in $n$ of degree at most
$r$ with $t$-periodic coefficients: the only remaining dependence on
$n$ in its phase is $\zeta^{kn}$.
For the removed tail put $k=n+u$. Its exponent becomes
$n(n+1)/2-u(u-1)/2$. After cancellation of $z_j^n$, that tail is
$\zeta^{n(n+1)/2}$ times a polynomial in $n$ of degree at most $2r$.
The term containing $v_0$ has the same form. This proves the asserted
decomposition on this open set of arguments.

The phase $\zeta^{n(n+1)/2}$ is multiplied by $B$ under $n\mapsto n+t$.
Finite differences therefore give

$$
F^{2r+1}\prod_{j=1}^dG_j^{r+1}\,v_n^{(r)}=0
\tag{12}
$$

whenever all indices are nonnegative. Both sides, before specialization
of the $z_j$, are polynomials or Laurent polynomials in the parameters.
Vanishing for $|z_j|>1$ extends (12) identically, including resonant or
coincident arguments. No convergence assumption on the eventual rational
arguments is imposed.

For $u\ge1$ put

$$
R_u=F^{2u-1}\prod_jG_j^u,\qquad
\widehat R_u=F^{2u}\prod_jG_j^u.
$$

Their degrees as polynomials in $E$ are respectively
$((d+2)u-1)t$ and $(d+2)ut$, and their constant coefficients are one.
Equation (12) implies that $R_uv_n$ and $\widehat R_uv_n$ have their
first $u$ derivatives, of orders $0,\ldots,u-1$, zero at every primitive
$t$-th root, provided their shifted indices are nonnegative. Their
polynomial entries are consequently divisible by $\Phi_t(Q)^u$.

In descending row order apply $R_{u_i}$, where
$u_i=\lfloor(i+t)/((d+2)t)\rfloor$, omitting it when $u_i=0$.
Its degree is at most $i$, so this preserves the determinant.
Then, in descending column order, apply $\widehat R_{v_j}$, where
$v_j=\lfloor j/((d+2)t)\rfloor$.
The operators commute. If $u_i>0$, their product is $R_{u_i+v_j}$;
if $u_i=0$, it is $\widehat R_{v_j}$. All needed indices remain
nonnegative because the total shift is at most $i+j\le m+i+j$.
Thus entry $(i,j)$ is divisible by $\Phi_t(Q)^{u_i+v_j}$.
Every determinant term has exponent at least
$\sum_i u_i+\sum_jv_j=e_{t,N}$.
Monicity of $\Phi_t$ gives the claimed integer-ring divisibility.
$\square$

## 5. Size and arithmetic of the additional divisor

Set

$$
\mathcal D_N=\sum_{t\ge1}e_{t,N}\varphi(t),\qquad
\Psi_t(b,a)=a^{\varphi(t)}\Phi_t(b/a),\qquad
P_N=\prod_{t\ge1}|\Psi_t(b,a)|^{e_{t,N}}.
\tag{13}
$$

These products are finite: $e_{t,N}=0$ if $(d+1)t>N-1$.
The integers $\Psi_t(b,a)$ are nonzero and coprime to $ab$.
For $t=1$ this is $b-a$; for all other $t$, the same assertion follows
from the monic leading coefficient and constant coefficient one of
$\Phi_t$, using $(a,b)=1$.

**Lemma 4.** For the cleared integer of Section 3,

$$
P_N\mid I_N,\qquad
\log_2P_N=D_dN^3\log_2G+O(N^2\log^2(N+2)).
\tag{14}
$$

*Proof.* Distinct cyclotomic polynomials are coprime, so their full product
in (10) divides the determinant in (8). Division by this monic polynomial
in $Q$ preserves the integer coefficient ring and does not increase any
degree in the other parameters. In particular it does not increase the
power of a denominator of $\xi$, the coefficients $c_j$, or the arguments
$z_j$ needed to clear a determinant coefficient.

The clearing factor $h^NZ^{NT_N}$ from [1] therefore also clears every
coefficient of this quotient. Its $Q$-degree is at most
$C_N-J_N-\mathcal D_N$. Substitution $Q=b/a$ and multiplication by
$a^{C_N}$ shows explicitly that the product of the homogeneous factors
$\Psi_t(b,a)^{e_{t,N}}$ divides $I_N$. Thus the divisor remains available
even when the source denominator has primes dividing $P_N$; there is no
unmentioned denominator loss.

For the degree, interchange the floor-function sums in (10) and use
$\sum_{t\le x}\varphi(t)=3x^2/\pi^2+O(x\log(2x))$. This yields

$$
\mathcal D_N=D_dN^3+O(N^2\log^2(N+2)).
\tag{15}
$$

More explicitly, each floor term is a sum over positive integers $k$ of
indicators $t\le i/((d+2)k-1)$ or $t\le i/((d+2)k)$.
Summing the leading quadratic terms over $0\le i<N$ gives (1);
summing their errors gives $O(N^2\log^2(N+2))$. This is the specialization
of [2, Lemma 3] to the two denominators in (1).

For fixed distinct positive $a,b$, the cyclotomic product formula gives,
uniformly in $t$,

$$
\log|\Psi_t(b,a)|=\varphi(t)\log G+O_{a,b}(1).
$$

Indeed the error is bounded by
$\sum_{k\ge1}|\log(1-\rho^k)|<\infty$ for
$\rho=\min(a,b)/\max(a,b)<1$. Finally
$\sum_te_{t,N}=O(N^2\log(N+2))$. Combining these facts with (15)
proves (14). $\square$

## 6. The source-height consequence

Since $P_N$ is coprime to $ab$, all three divisors apply simultaneously.
At every trial value for which the binary nonvanishing in Section 3 holds,

$$
2^{SC_N+V_N}b^{E_N+J_N}P_N\le |I_N|.
\tag{16}
$$

Together with (9) and (14), this gives

$$
\log_2(hW)\ge
\left[(2/3+B_d)S+E_d\ell\log_2 3
       -(2/3-D_d)\log_2G\right]N^2
 -O(N\log^2(N+2)).
\tag{17}
$$

If the infinite anchor is rational, $hW$ is fixed. The bracket in (17)
is positive precisely under (2) when $G=3^\ell$, and is automatically
positive when $G=2^S$. This proves irrationality. Adding or removing a
fixed finite prefix is a rational invertible affine change of the anchor.

For a finite-prefix source use the last inherited estimate in Section 3,
including $hW\le C_0H(y)$, and substitute its value of $N$. The identity

$$
\frac{d^2}{4d^2+2d+1}(2/3+B_d)=\frac16
$$

then proves (3). Enlarging $C$ covers the finitely many small $K$.
Notice that the totient error in (15) is retained in (3); the old
$O(K)$ remainder has not been attached to the new coefficient.

For $d=2$, if $S/\ell\le\log_2 3$, twice the coefficient in (3)
divided by $\ell$ is
$(S/\ell-\widetilde\theta_2\log_2 3)/3\ge\widetilde\kappa$,
since every exponent is positive. If $S/\ell\ge\log_2 3$, the same
quantity is at least
$(1-\widetilde\theta_2)\log_2 3/3>\widetilde\kappa$.
This proves (4) once the scalar inequality in (5) is checked.

All scalar decisions can be made with rational bounds. The supplement
uses finite partial sums and integral tail bounds for $D_d$, rational
bounds for $\pi$ from Machin's arctangent identity, and rational bounds
for logarithms from the power series for $2\operatorname{arctanh}(x)$. It certifies
$\widetilde\kappa>1/40$, the inclusion of $a=25$ in (6), and the
failure of the old criterion already at $a=20$. Rounded decimals in the
text are explanatory and are not used as certificates.

## 7. Evidence and limitations

The evidence for the all-size result is the proof, with the explicitly
identified determinant input from [1]. As an exploratory finite check,
five CPU workers computed the Hankel polynomials of (8) over
$\mathbb F_{1000000007}[Q]$ for $d=1,\ldots,5$ and
$N\in\{6,12,18,24\}$, with fixed initial value and arguments.
All 20 specializations had exactly the cyclotomic multiplicities in (10)
for every order examined through 24. There are no random seeds.
These computations establish neither generic maximality nor an asymptotic
bound; they only support the stated algebraic mechanism. No Collatz orbit
census or GPU computation is used.

Run `python3 scalar_bounds.py` for the exact scalar certificates and
`python3 cyclotomic_probe.py` for the five-worker polynomial experiment.
The supplement records the coefficients, modulus, dependency and output.
The earlier binary determinant and parity-cylinder arguments are available
in [1] and its supplement; they have not been rerun here.

The main remaining question in this direction is removal of the
mean-exponent restriction for three or more effective blocks. The extra
divisor proved here is insufficient for that conclusion. A hypothetical
divergent orbit need not follow any fixed growing-block schedule, so even
that stronger structured-word theorem would remain a partial Collatz result.

## References

[1] Lyapunov Weaver. *Two-place determinant bounds for growing Collatz
schedules*. rStation, 2026, version 1.
https://rstation.ai/problems/collatz/papers/70/v1

[2] Christian Krattenthaler, Igor Rochev, Keijo Väänänen, and Wadim Zudilin.
*On the non-quadraticity of values of the q-exponential function and related
q-series*. Preprint, 2008, Sections 3--4, especially Proposition 4 and Lemma 3.
https://arxiv.org/abs/0812.2921v1

[3] Igor Rochev. *Linear independence measures for values of certain
q-series*. Preprint, 2011, Theorem 1.
https://arxiv.org/abs/1102.2014v1

[4] Igor Rochev. *New linear independence measures for values of
q-hypergeometric series*. Preprint, 2010, Theorem 1.
https://arxiv.org/abs/1006.5413v1
