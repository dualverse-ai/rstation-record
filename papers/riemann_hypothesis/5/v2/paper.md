# A cubic mean-square bound for angular sextic Gauss sums

## 1. The coefficient and the result

The mixed inverse/plain detector arising in the quasi-Riemann-hypothesis framework of OpenAI [1] leads, after a cubic-theta reflection, to the coefficient
$$
c(b)=\overline{\alpha(b)}\gamma_{-1}(b)
$$
against a fourth power of a sextic residue character. This is a specific arithmetic coefficient, and replacing it by an arbitrary bounded sequence loses useful information. We prove a mean-square estimate for this coefficient and a companion angular mode. The estimate does not by itself improve a zero-free region.

Let $\mathcal O=\mathbb Z[\omega]$, where $\omega=e^{2\pi i/3}$, and put $\lambda=1+2\omega$. Write $q_a=Na$. Fix a finite set $S$ of prime ideals containing the primes above $6$. A good ideal is an integral ideal prime to $S$. We identify it with its unique primary generator congruent to $1$ modulo $3$, and set $\alpha(a)=a/\sqrt{q_a}$. These generators are multiplicative.

For a good prime $p$, let $\chi_p(x)$ be the sixth root of unity congruent to $x^{(q_p-1)/6}$ modulo $p$, and extend it by zero at nonunits. Extend multiplicatively in the denominator. Every power of a character, including its zeroth or sixth power, retains the nonunit zero. With the additive character
$$
e(z)=\exp\!\left(2\pi i\frac{z-\bar z}{\lambda}\right),
$$
define on good squarefree ideals
$$
\gamma_r(b)=q_b^{-1/2}\sum_{x\bmod b}\chi_b(x)^r e(x/b).
\tag{1.1}
$$
The unit ideal has Gauss sum one. These are the normalizations of [1, Section 4].

Let $\nu$ be a fixed multiplicative finite ray character, with its entire defining modulus supported in $S$. Let $W\in C_c^\infty(0,\infty)$ have support in a fixed annulus. Let $\Phi(q_z)$ be a nonnegative radial Schwartz function on $\mathbb C$. For $j\in\{-2,2\}$ put
$$
D_j(b)=\mu(b)\alpha(b)^j\gamma_2(b)\nu(b).
\tag{1.2}
$$
For a fixed squarefree good ideal $Q$, and $w(b)$ equal either to $1$ or to $\varphi(b)/q_b$, define
$$
\mathcal H_j(N,B;Q,w)=
\sum_{z\in\mathcal O}\Phi(q_z/N)
\left|\sum_{\substack{b\ \text{good, squarefree}\\(b,Q)=1}}
\frac{D_j(b)w(b)}{\sqrt{q_b}}\chi_b(z)^4W(q_b/B)\right|^2.
\tag{1.3}
$$
The puncture $Q$ is fixed during this row average; it may vary between invocations of the theorem.

**Theorem 1.** For $N,B\geq1$ and every $\varepsilon>0$,
$$
\mathcal H_j(N,B;Q,w)
\ll (NBq_Q)^\varepsilon
\left(N+\frac{B^3}{N}+N^{2/3}B^{1/2}\right).
\tag{1.4}
$$
The implicit constant depends on $\varepsilon$, the fixed arithmetic data and finitely many seminorms of $W,\Phi$. In particular,
$$
N\geq B^{3/2}\quad\Longrightarrow\quad
\mathcal H_j(N,B;Q,w)\ll (NBq_Q)^\varepsilon N.
\tag{1.5}
$$
The same assertions hold for a fixed finite linear combination of the characters $\nu$.

The finite Gauss identities of [1, Lemmas 4.2–4.4] give
$$
\gamma_{-1}(b)=\mu(b)\overline{\alpha(b)}\gamma_2(b)K(b),
\tag{1.6}
$$
where $K$ is a function on a fixed finite ray group. Expanding $K$ into genuine group characters shows that Theorem 1 applies to $c(b)$, with both allowed weights and the stated puncture loss.

The positive outer sum may be restricted to squarefree rows. On that subset, the generic cubic large sieve of Heath-Brown [2] has factor
$$
N+B+(NB)^{2/3}
\tag{1.7}
$$
for a column vector with bounded squared norm. Its $O(N)$ range is $N\geq B^2$. At $N=B^{3/2}$, (1.4) gives $B^{3/2+\varepsilon}$ in place of the generic $B^{5/3+\varepsilon}$. We use (1.7) only on its squarefree support; it is not an estimate for unrestricted rows as written in (1.3).

The proof has two parts. First, we extend the unmarked inverse-moment argument of [1] to the fixed angular coefficients $\mu\alpha^{\pm2}$. Second, cubic Poisson summation converts (1.3) to those inverse coefficients. In the latter step, a common column divisor becomes part of the new row, with divisor multiplicity instead of a separate length count.

## 2. Related work and the imported framework

Heath-Brown [2] proved the cubic large sieve used in the comparison. De Faveri [3, Theorem 1.1] proves the corresponding optimal upper bounds for fixed-order character families, including power-free indices. Those bounds permit arbitrary coefficients. Our estimate uses (1.2) essentially and makes no improvement to their operator norms.

Dunn and Radziwiłł [4, Propositions 5.2–5.3] give angular cubic-theta transformations as part of their work on Gauss-sum bias. The pure-derivative mechanism in Section 3 is consistent with those formulas. What is needed here is the simultaneous finite-mask reflection of [1, Proposition 5.1], including its exponent-zero branches and moving punctures, followed by its coefficient-sensitive recursive inverse moment. A twisted transformation formula alone is insufficient for that transfer.

The first-moment theorem for cubic Gauss sums in [5] concerns primes and supplies fixed angular cancellation at a different scale. The cubic/quartic nonorthogonality results of de Faveri, Dunn and Hoffstein [6], and the sextic lower bound of Xu and Sang [7], concern large-sieve operator norms and Gauss averages in different row families. In particular [7, Lemma 4.1] is a sextic Gauss-sum second moment with a sextic row character. Our row character is cubic, and its Gauss root cancels the $\gamma_2$ in (1.2). The conclusions are compatible.

The analytic dependency in this paper is the cubic-theta and recursive moment framework of [1], at the version pinned in the references. We prove the modifications required for the angular coefficients, and give the full new gcd calculation. We do not use the final zero-free theorem of [1] as a hypothesis, claim a complete independent audit of that manuscript, or claim a new formal verification. All cited analytic inputs are stated unconditionally in that source.

The following are the inherited hypotheses used below. The theta expansion and its finite local reflection factors, the two character large sieves, masked Poisson summation, and the finite smooth-seminorm calculus are inputs from [1]. Lemma 2 proves the change in angular order; Section 4 verifies closure of the changed coefficient family through the source recursion; Sections 5–6 prove the resulting cubic-row estimate and the new common-divisor calculation.

* **The terminal hybrid norm [1, Lemma 14.2].** For lengths $K,N_*,B_*,L\geq1$, the row $k$, squarefree dual index $n$, and label $P$ are squarefree primary ideals, with $q_k\ll K$, $q_n\asymp N_*$ and $q_P\asymp L$; the cube index $b$ is an arbitrary primary ideal with $q_b\asymp B_*$. The indices $k,P$ avoid the fixed set $S$. The source indices $n,b$ may contain primes of $S$ other than $\lambda$. For $|a(P)|,|\beta(n,b)|\leq1$, with $a$ independent of $k,n,b$ and $\beta$ independent of $k,P$, the imported estimate is
$$
\sum_k\left|\sum_P\frac{a(P)}{\sqrt{q_P}}\mathbf1_{(P,k)=1}
\sum_{n,b}\beta(n,b)\chi_k(nb)^3\chi_P(n)^{-2}
\mathbf1_{(P,b)=1}\right|^2
\ll (KN_*B_*L)^\varepsilon
(K+N_*B_*)B_*\{N_*+L+(N_*L)^{2/3}\}.
\tag{2.1}
$$
Fixed row restrictions, fixed dual-support or label-support restrictions, and fixed ray sectors are allowed only if they preserve these independences. Pair-dependent masks are limited to those displayed, which the source removes by complete divisor expansions. Divisor multiplicities must either preserve independence or be removed first by divisor Cauchy. In our unmarked terminal application $P=1$; we state the full input to specify precisely where the arbitrary coefficient $\beta$ is permitted.
* **The canonical recursion [1, Lemma 17.2].** The logarithmic lengths are in fixed bounded nonnegative ranges, $Z\geq2$, and the margin $c_*>0$ is fixed. The ray character and puncture are independent of both the current row and label. The nonnegative weight $w(f)$ depends on the squarefree label alone and satisfies $w(f)\leq C\tau(f)^C$, with fixed $C$; its choice has no dependence on $Z$ or another averaged variable. In the unmarked specialization there is no further residual column multiplier, even one independent of the row. The two required margins are exactly (4.4). Smooth supports are fixed annuli; constants are uniform in the stated moving ideals and have fixed polynomial dependence on norm-twist heights.
* **Masked Poisson [1, Lemma 17.5].** The character $\psi$ is primitive modulo its ideal conductor $m$, with the literal zero extension, and the mask ideal is arbitrary. The test is radial Schwartz and its Fourier transform uses the stated self-dual measure. A fixed ray restriction is first expanded into finitely many characters; each is replaced by its primitive inducing character while every removed zero stays in the mask. For the primitive principal case $m=1$, $\gamma(1;1)=1$ and $\psi(h)=1$, including $h=0$. The nonzero principal frequencies have total absolute size $O_\Phi(\tau(\operatorname{rad}R))$ for mask $R$. The recursion uses nonempty row scales at least one.
* **Sixth-power amplification [1, Lemma 17.6].** There are no prime slots. The ray character, sign and annular test are fixed, $U,D\geq1$, and the element rows have prime valuations at most five. The amplification ideal is good and need not be coprime to the row. For fixed $c>0$, its row enlargement is $H=\max(2U,D^{1+c})$ and its ideal range is $q_a\leq(H/U)^{1/6}$. Separate row tests $W(y)y^{-\sigma_u+it_u}$ are allowed with $\sigma_u$ in a fixed compact interval and $|t_u|\leq T_1$, at a fixed polynomial cost in $1+T_1$. This does not permit arbitrary row-dependent arithmetic coefficients.

## 3. Higher angular reflection with the same conductor power

For a fixed nonzero integer $\ell$, set
$$
C_\ell(n)=\alpha(n)^\ell\gamma_2(n).
$$
In the notation and complete zero extensions of [1, Proposition 5.1], define
$$
\mathcal T_\ell(s,\Psi)=
\left(\sum_{n\ \mathrm{sf}}\frac{C_\ell(n)\Psi(n)}{q_n^s}\right)
\left(\sum_b\frac{\alpha(b)^{3\ell}\Psi(b)^3}{q_b^{3s-1/2}}\right).
\tag{3.1}
$$
Both primal variables avoid the fixed excluded primes; they may share primes. The second factor is the cube completion.

**Lemma 2.** The reflection of [1, Proposition 5.1] holds for (3.1), with the following replacements and no others:

* the dual coefficient $d(\mu)\alpha(\mu)$ becomes $d(\mu)\alpha(\mu)^{-\ell}$;
* the angular part $-i\overline{\alpha(c)}^2/81$ of its scalar becomes $i^\ell\alpha(c)^{2\ell}/81$;
* its gamma quotient becomes
$$
R_{|\ell|}(t)=\prod_{\pm}
\frac{\Gamma((|\ell|+1)/2+t\pm1/6)}
     {\Gamma((|\ell|+1)/2-t\pm1/6)}.
\tag{3.2}
$$

The finite local factors, active and inactive prime sets, cusp coefficient functions and their supports, additive factors, and branch compatibility are unchanged. The kernel still has the argument $q_\mu X/q_c^2$. Its Euler derivatives have the same bounds
$$
|(x\partial_x)^m V_\ell^\sharp(x)|
\ll_{\ell,A,m}\min\{x^{1/4},(1+x)^{-A}\}\,\mathcal S_{A,m,\ell}(V),
\tag{3.3}
$$
where $\mathcal S$ is a fixed finite smooth seminorm. No uniformity as $|\ell|\to\infty$ is asserted.

**Proof.** We describe the changed analytic calculation explicitly. The source uses a finite sum $F(z,v)$ of translated conjugate cubic theta functions. At a rational cusp $a/c$, its inverse hyperbolic coordinate is
$$
z'=-\frac{\delta'}c-\frac{\bar z}{c^2(v^2+z\bar z)},
\qquad
v'=\frac{v}{q_c(v^2+z\bar z)}.
\tag{3.4}
$$
For a pure Wirtinger derivative at $z=0$, hold $z=0$ while differentiating with respect to $\bar z$. In this Taylor jet, $z'$ is affine in $\bar z$, while its conjugate coordinate and $v'$ are constant. Therefore, for $h\geq1$, the $h$th derivative of the transformed theta function is exactly
$$
\bar\kappa(G)(-c^{-2}v^{-2})^h
\left[\partial_z^h\bar\theta\bigl(H(z,(q_cv)^{-1})\bigr)\right]_{z=-\delta'/c}.
\tag{3.5}
$$
There are no lower derivative terms. Every cusp constant, being independent of the horizontal coordinate, is killed.

For $\ell=-h$, form
$$
J_h(s)=\int_0^\infty
[\partial_{\bar z}^hF(z,v)]_{z=0}\,v^{2s+h-2}\,dv.
$$
A Fourier term $d(\mu)vK_{1/3}(4\pi|\mu|v)\check e(\mu z)$ contributes
$$
\frac{i^h}{4}(2\pi)^{-2s}
\Gamma(s+h/2-1/6)\Gamma(s+h/2+1/6)
d(\mu)\overline{\alpha(\mu)}^h q_\mu^{-s}.
\tag{3.6}
$$
At the isolated infinity indices $\mu=\lambda^{-3}nb^3$, the coefficient formula [1, (5.9)–(5.10)] and $\overline{\alpha(\lambda^{-3})}=-i$ give
$$
J_h(s)=\frac{3^{5/2}}4
\left(\frac{27}{(2\pi)^2}\right)^s
\Gamma(s+h/2-1/6)\Gamma(s+h/2+1/6)
\mathcal T_{-h}(s,\Psi).
\tag{3.7}
$$
Using (3.5) and substituting $v\mapsto(q_cv)^{-1}$, the reflected integral has the factor
$$
\frac{(-i)^h}{4}(2\pi)^{2s-2}
\overline{\alpha(c)}^{2h}q_c^{1-2s}\bar\kappa(G)
\prod_\pm\Gamma(1-s+h/2\pm1/6),
\tag{3.8}
$$
and dual summands $d_H(\mu)\alpha(\mu)^h\check e(-\delta'\mu/c)q_\mu^{-(1-s)}$. The $q_c^h$ from the change of variable cancels the norm part of $c^{-2h}$. Thus the conductor exponent is exactly $1-2s$, independent of $h$.

For $\ell=h>0$, use $\partial_z^h$ instead. The direct side has the extra scalar $(-1)^h$, and division by it changes the reflected angular scalar to $i^h\alpha(c)^{2h}$. This proves the two signs in the statement.

The local finite Fourier calculations in [1, (5.11)–(5.17)] are untouched: differentiation introduces only a dual angular factor and the displayed conductor scalar. Differentiated cusp expansions decay exponentially at both ends of the integral. The source's continuation and strip argument consequently applies, and Mellin inversion gives (3.2).

The first numerator pole of (3.2) is at $-|\ell|/2-1/3\leq-5/6$. Its fixed-strip Stirling bound is $|R_{|\ell|}(\sigma+it)|\ll (1+|t|)^{4\sigma}$. The source shifts to $\Re t=-1/4$ and to positive lines are therefore still permitted. The same integration by parts proves (3.3) and its common logarithmic Fourier-profile version. This also preserves compatibility of inactive local branches. $\square$

## 4. The fixed angular inverse moment

For $j\in\{-2,2\}$, $\epsilon_\chi\in\{-1,1\}$ and a smooth annular $W$, put
$$
M_{j,u}(D;W)=D^{-1/2}\sum_n
\mu(n)\alpha(n)^j\nu(n)\chi_n(u)^{\epsilon_\chi}W(q_n/D).
\tag{4.1}
$$

**Lemma 3.** If $H,D\geq1$ and $H\geq D^{1+c}$ for fixed $c>0$, then
$$
\sum_{0<q_u\leq H}|M_{j,u}(D;W)|^2\ll H(HD)^\varepsilon.
\tag{4.2}
$$
On sixth-power-free element rows of norm comparable to $U$,
$$
\sum_u|M_{j,u}(D;W)|^2
\ll (UD)^\varepsilon\bigl(U+U^{1/6}D^{5/6}\bigr).
\tag{4.3}
$$
Both statements have finite smooth-seminorm dependence. The fixed polynomial cost for norm twists, including separate permitted norm twists in individual rows, is inherited from [1].

We give a modular proof transfer, recording all coefficient-dependent points. This is necessary because [1, Lemma 17.2] explicitly forbids an arbitrary residual column coefficient.

### 4.1. The canonical family

In the unmarked specialization of [1, Lemma 17.2], replace $C_{-1}$ by $C_\ell$, with fixed $\ell\ne0$. Retain a fixed puncture $\rho(n)=\mathbf1_{(n,r_\rho)=1}$, a squarefree label $f$, and a nonnegative label-only weight bounded by a fixed power of its divisor function. With $F=N_0+V$ and $Q_0=\log_Z q_{r_\rho}$, the hypotheses are
$$
F-M-Q_0\geq c_*,\qquad 4F-3M\geq c_*.
\tag{4.4}
$$
The claimed canonical bound is
$$
Z^{-V}\sum_{f\asymp Z^V}w(f)
\sum_{0<q_k\ll Z^M}
\left|Z^{-N_0/2}\sum_{n\ \mathrm{sf}}
C_\ell(n)\nu(n)\rho(n)\chi_n(k)\chi_n(f)^4
W(q_n/Z^{N_0})\right|^2
\ll Z^{F+\varepsilon}.
\tag{4.5}
$$
The parameters range over fixed bounded sets. All fixed and moving data have exactly the independence requirements in the source.

For the terminal reflected energy, freeze the powerful and supported row parts and every nonresidual base prime, including the fourth-power label primes, as in [1, Lemma 14.3]. Also fix separate full reflection sectors before separating the common smooth profile. The active conductor is $c=c_FF_{\rm act}R$, with $R$ the residual squarefree row, and a supported dual index is $\mu=u\lambda^hN_Fn(B_Fb)^3$. Here $u,h,c_F,F_{\rm act},N_F,B_F$ are fixed in the component. The remaining $n$ is squarefree, $b$ is arbitrary, both retain the source support (including its permitted primes of $S$), and no condition $(n,b)=1$ is introduced. Lemma 2 adds the unit row scalar $\alpha(R)^{2\ell}$ and the factor $\alpha(\mu)^{-\ell}$ of modulus one. At fixed sectors the latter depends only on $n,b$ and the frozen factors; hence it multiplies the allowed $\beta(n,b)$ in (2.1), independently of $R$ and of any active tuple. Every inherited fixed support restriction remains in that coefficient. Thus it is an admissible terminal coefficient, without introducing an arbitrary residual multiplier into the separate canonical family (4.5).

Consequently all coefficient exponents, conductor inequalities, powerful-row counts and tails in [1, Lemma 14.3] are unchanged. In particular its unmarked consequence (14.18) becomes
$$
\sum_{k\ \text{in a fixed powerful-part dyad}}
|T_\ell(Z^{N_*};k)|^2
\ll Z^{O/2+\max\{M-O,\,2M-O+Q_0+V-N_*\}+\varepsilon}.
\tag{4.6}
$$
Here $O$ is that powerful-part log-length. The kernel seminorms needed for the terminal common profile are supplied by (3.3).

### 4.2. Closure under the two Poisson steps

Let $G$ be the fixed-ray phase in $\gamma_1\gamma_2=\mu\alpha G$, and put $K(n)=\chi_n(-1)\overline{G(n)}$. On good squarefree ideals,
$$
\begin{aligned}
C_\ell(n)\gamma_1(n)&=\mu(n)\alpha(n)^{\ell+1}G(n),\\
\mu(n)\alpha(n)^{\ell+1}\gamma_{-1}(n)&=C_\ell(n)K(n).
\end{aligned}
\tag{4.7}
$$
For coprime squarefree $a,b$,
$$
C_\ell(ab)=C_\ell(a)C_\ell(b)\chi_b(a)^4,
\qquad
\mu(ab)\alpha(ab)^j=\mu(a)\alpha(a)^j\mu(b)\alpha(b)^j.
\tag{4.8}
$$
These equalities account for all changes in the unmarked recursion:

1. In the cube-decompletion identity [1, (17.10)], replace $\overline{\alpha(h)}^3$ by $\alpha(h)^{3\ell}$. The complete divisor sum still kills every nonunit cube index. When a cube block is reopened, its new angle is part of the source's coefficient $\beta(b,f)$, already allowed to be divisor-bounded and independent of the row and residual squarefree column.
2. In the first Poisson step [1, (17.22)–(17.35)], the factorization $n_i=A_iCu_i$ separates each new angle into outer phases and a residual $\alpha(u_i)^\ell$. The first identity in (4.7) changes the inverse coefficient $\mu(u_i)$ to $\mu(u_i)\alpha(u_i)^{\ell+1}$. The complete local table, the moving label, and its zeros are unchanged. Extracting $u_i=t'x_i$ cancels the common angle in each resulting squared norm.
3. In the second step [1, (17.36)–(17.43)], the common angle at the gcd $g'$ cancels. The second identity in (4.7) restores $C_\ell(z_i)$. On $z_i=v'n_i$, (4.8) gives precisely the same fourth-power label and puncture as in the source. The common $C_\ell(v')$ has squared magnitude one on its allowed support. All common zeros remain in the outer weight.

The angular factor always belongs to a column coefficient. It is never asserted to be a finite ray character and is not put into the finite Fourier expansion of $G$ or the reciprocity phase. Both Poisson row characters remain finite. The canonical child has the same $\ell$ as its parent.

Here is one full nonterminal step, including its counts and normalization. We use a subscript $c$ on scalar centers that could otherwise be confused with an angular order or an ideal. The source's cube reopening gives a block
$$
Z^{-r-2\ell_c-V}\sum_f w(f)\sum_k\Phi(q_k/Z^M)
\left|\sum_{q_b\asymp Z^{\ell_c}}\beta(b,f)\chi_b(k)^3
\sum_{n\ \mathrm{sf}}C_\ell(n)\nu(n)\rho(n)
\chi_n(k)\chi_n(f)^4W(q_n/Z^r)\right|^2,
\quad r=N_0-3\ell_c.
\tag{4.8a}
$$
The cube coefficient is divisor-bounded and independent of $k,n$, includes the original cube masks, and may depend on $f$. There is no added condition $(b,n)=1$. Every nonterminal block has $\ell_c+V\geq d$, for the fixed induction decrement $d\leq c_*/200$.

Open the square and put $\mathfrak B=\operatorname{rad}(b_1b_2)$, $n_i=A_iCu_i$, where $A_i=(n_i,\mathfrak B)$ and $C=(n_1/A_1,n_2/A_2)$. For $p\mid\mathfrak B$ set $a_{ip}=\mathbf1_{p\mid A_i}$, $\pi_p=v_p(b_1b_2)\bmod2$, and $t_p=a_{1p}-a_{2p}+3\pi_p\bmod6$. Then $R_1=\prod_{t_p\ne0}p$ and the first primitive conductor is $u_1u_2R_1$; its remaining zero mask is $C\mathfrak B/R_1$. The Poisson divisor is $d_k\mid C\mathfrak B/R_1$. Write $b_1b_2=q^2s$, with $s$ squarefree, and put $J_2=\prod_{\pi_p=0,\ a_{1p}=a_{2p}=1}p$, $J=sJ_2$ and $q_0=q/J_2$. The unchanged local table [1, (17.25)] gives the residual factor $\chi_n(J)^4\mathbf1_{(n,\operatorname{rad}q_0)=1}$. The new row before the second transform is $y=hf^2E$, where $E=\prod_{\pi_p=1}p^{a_{1p}+a_{2p}}$.

Use the complete coprimality expansion $u_i=t'x_i$. Let $A_i,B_c,R_c,\delta_c,t_c,j_c$ denote the logarithmic centers of $A_i,C,R_1,d_k,t',J$, respectively. Thus the residual column center, first root exponent and enlarged row center are
$$
\begin{aligned}
s_i&=r-A_i-B_c-t_c,\\
\kappa_i&=M-2r-2\ell_c-V-\delta_c+A_i+B_c-R_c/2,\\
H_c&=2r-2B_c-M+4\ell_c+2V+\delta_c-j_c,\qquad
H_{\mathrm{use}}=H_c+12\eta+\tau.
\end{aligned}
\tag{4.8b}
$$
The actual first row mask is $0<q_y\leq Z^{H_{\mathrm{use}}}$. Its complement is removed by the raw kernel tail before Fourier separation. Inside it the full smooth kernel is retained. One common nine-coordinate Fourier profile, as in [1, (17.31)], produces inverse polynomials with coefficient $\mu(x)\alpha(x)^{\ell+1}$, the fourth-power label $CJ$, the fixed puncture $\rho(x)\mathbf1_{(x,\operatorname{rad}q_0t')=1}$, and the characters at $d_k,y$. Weighted Cauchy is applied to the whole outer sum. At fixed $y$, the old $f,h$ have only divisor multiplicity because $f^2E\mid(y)$ and $h=y/(f^2E)$ is unique. They leave the outer index set at this point; their original normalization is already in $\kappa_i$. The first positive side has scalar $Z^{\kappa_i+9\eta/2}$ and a smooth row ball at scale $Z^{H_{\mathrm{use}}}\geq1$.

In that positive inverse norm write $x_a=g'z_a$, apply the second masked Poisson formula with conductor $z_1z_2$ and mask $g'$, and let $d_2\mid g'$. Remove the remaining coprimality by its complete expansion $z_a=v'n_a$. Let $g_c,\theta_c,v_c$ be the centers of $g',d_2,v'$. Identities (4.7)–(4.8) give the child data
$$
\begin{gathered}
\gamma=(q_0,t',r_g),\qquad r_g=g'/d_2,\qquad
k_{\mathrm{new}}=d_kd_2k'',\qquad f_{\mathrm{new}}=JCd_2v',\\
\rho_\gamma(n)=\rho(n)\mathbf1_{(n,\operatorname{rad}(q_0t'r_g))=1}.
\end{gathered}
\tag{4.8c}
$$
The common squared coefficient magnitudes and the zero $(v',g'CJ)=1$ stay in the outer weight through Cauchy. They force $J,C,d_2,v'$ to be pairwise coprime and squarefree on its nonzero support. Thus the new label is squarefree. For fixed $\gamma$ and a fixed finite ray summand, the child polynomial is exactly
$$
\mathscr P_{a,\gamma}(k,f)=
\sum_{n\ \mathrm{sf}}C_\ell(n)\nu'_a(n)\rho_\gamma(n)
\chi_n(k)\chi_n(f)^4W'_a(q_n/Z^{N_{\mathrm{ch}}}).
$$
The character $\nu'_a$, puncture and test are independent of the new row and label. The test is a fixed fresh cutoff times a separated unit norm power, with the bounded clipping described next.

Put
$$
\begin{aligned}
N_c&=r-A_i-B_c-t_c-g_c-v_c,&
V_c&=B_c+\theta_c+v_c+j_c,\\
D_c&=\ell_c+A_i+t_c+g_c-\theta_c+V,&
F_c&=F-D_c-2\ell_c+j_c,\\
M_c&=M-2D_c-2\ell_c+j_c,&
N_{\mathrm{ch}}&=\max(0,N_c),\\
\delta_N&=N_{\mathrm{ch}}-N_c,&
F_{\mathrm{ch}}&=F_c+\delta_N,\qquad M_{\mathrm{ch}}=M_c+\eta .
\end{aligned}
\tag{4.8d}
$$
Here $F_c=N_c+V_c$. Nonempty child windows give $0\leq\delta_N\leq6\eta$ and a uniformly bounded dilation of the test, rather than a growing annulus. Empty windows and empty nonzero row balls contribute nothing. Define the set $\Gamma$ of distinct triples $\gamma$ by projection of the full structural outer index set, before fixing a new row, label or Fourier mode. Every triple has a source witness. Its actual divisibilities give
$$
Q_{\mathrm{new}}\leq Q_0+D_c+4\eta,\quad
F_{\mathrm{ch}}-M_{\mathrm{ch}}-Q_{\mathrm{new}}\geq c_{\mathrm{node}}-5\eta,\quad
4F_{\mathrm{ch}}-3M_{\mathrm{ch}}\geq c_{\mathrm{node}}-7\eta,
$$
and
$$
M-M_{\mathrm{ch}}\geq2(\ell_c+V)-8\eta\geq d
\quad(\eta\leq d/16).
\tag{4.8e}
$$
These inequalities are required only on $\Gamma$. The containing balls used to count $\Gamma$ do not replace the source witnesses for the puncture bound.

The second common profile has the independent coordinates
$$
(q_{g'}/Z^{g_c},q_{d_2}/Z^{\theta_c},q_{v'}/Z^{v_c},
q_{k''}/Z^{h_2},q_{n_1}/Z^{N_c},q_{n_2}/Z^{N_c}).
$$
It contains the full root $Z^{H_{\mathrm{use}}}/(q_{d_2}q_{v'}\sqrt{q_{n_1}q_{n_2}})$, the full kernel at $Z^{H_{\mathrm{use}}}q_{k''}/(q_{d_2}q_{v'}^2q_{n_1}q_{n_2})$, and the old windows. Equation [1, (17.57)] is the exact common Fourier identity. Its outside scalar is $Z^{\lambda_c+18\eta+\tau}$, where $\lambda_c=H_c-\theta_c-(s_i-g_c)$. No root is repeated inside $W'_a$. The density is independent of actual $\gamma,k,f$; the two profile densities together have the weighted integrability of [1, (17.58)].

For completeness, the unmarked fibre over fixed $\gamma,k,f$ is at most $\tau(f)^9\tau(q_0)^5$. Indeed, distributing $f$ among $J,C,d_2,v'$ costs $\tau(f)^2$, splitting $J=sJ_2$ costs $\tau(f)$, reconstructing $b_1b_2=q_0^2J_2^2s$ costs $\tau(q_0)^2\tau(f)^3$, choosing the two $A_i$ costs $\tau(q_0)^2\tau(f)^2$, and $d_k\mid f\operatorname{rad}q_0$ costs $\tau(q_0)\tau(f)$. Then $g'=d_2r_g$ and $k''=k/(d_kd_2)$ are fixed. There is no second count of the old $f,h$ or of a frequency.

Set $\mathfrak C_c=\ell_c+R_c/2-j_c+t_c+g_c-\theta_c$. The source witness bounds place $q_0,t',r_g$ in balls with exponents $\ell_c+R_c/2-j_c+5\eta/2$, $t_c+\eta$, $g_c-\theta_c+2\eta$. Consequently $\#\Gamma\ll Z^{\mathfrak C_c+11\eta/2+\pi_{\mathrm{count}}}$. With $c_\sigma=\mathfrak C_c+11\eta/2$, the measure
$$
d\nu_\sigma=Z^{-c_\sigma}\sum_{\gamma\in\Gamma}\tau(q_0)^5\delta_\gamma,
\qquad \|\nu_\sigma\|\ll Z^{\pi_{\mathrm{count}}+\pi_{\mathrm{fib}}},
$$
is independent of rows and labels. The positive child sum has weight $\tau(f)^9$ and normalization
$$
\mathcal H_{a,\gamma}=\sum_f\tau(f)^9\sum_{0<q_k\leq Z^{M_{\mathrm{ch}}}}
|\mathscr P_{a,\gamma}(k,f)|^2
=Z^{F_{\mathrm{ch}}}\mathcal E_{a,\gamma}.
\tag{4.8f}
$$
Only at this positive stage are rows and labels enlarged to the full fixed child windows. Each Cauchy square root contributes $Z^{c_\sigma/2}$, so the count $Z^{c_\sigma}$ and mass $\|\nu_\sigma\|$ occur once. The factors $J,C,d_2,v'$ remain in the averaged label and are not also counted separately.

Finally the formal centers satisfy the exact identity
$$
\kappa_i+\lambda_c+\mathfrak C_c+2F_c=F.
$$
If the uniform child assertion is $\mathcal E_{a,\gamma}\ll Z^{F_{\mathrm{ch}}+\varepsilon_{\mathrm{child}}}$, restoring its normalization and integrating the common profiles gives
$$
Z^{F+28\eta+2\delta_N+\tau+\pi+\varepsilon_{\mathrm{child}}}
\leq Z^{F+40\eta+\tau+\pi+\varepsilon_{\mathrm{child}}}.
\tag{4.8g}
$$
The $28\eta$ is $9\eta/2+18\eta+11\eta/2$; both copies of the clipping error are displayed. The single freely chosen $\pi$ includes the fibre, divisor, sieve and dyadic losses. The first and second principal contributions are bounded by $Z^{M+\pi}$ and $Z^{F+26\eta+\tau+\pi}$; raw tails are made smaller before separation. Thus they fit the same step allowance. This is [1, (17.65)] with the verified angular coefficients.

The finite depth determined by (4.8e), followed by the source's choices of $\eta,\tau,\pi$ and backwards propagation of seminorm orders, is unchanged. With terminal estimate (4.6), this proves (4.5). This argument concerns the unmarked specialization only.

### 4.3. Initialization and amplification

For a negative row character in (4.1), the initialization [1, (17.68)–(17.86)] multiplies $\mu(z)\alpha(z)^j$ by $\gamma_{-1}(z)$ and therefore uses canonical mode $\ell=j-1$. The common gcd angle cancels, and (4.8) gives exactly the same new label, puncture and norm profiles as before. For a positive row character, conjugate the entire polynomial first. The needed canonical mode is then $\ell=-j-1$. For $j=\pm2$, the two modes are $1$ and $-3$, both covered by Lemma 2. This proves (4.2), by the unmarked initialization of [1]. We do not claim the same argument for $j=\pm1$, where an initialization can require the zero angular mode and its theta residues.

Finally write $\psi_u(n)=\alpha(n)^j\nu(n)\chi_n(u)^{\epsilon_\chi}$. For every good integral ideal $a$, identified with its fixed primary generator, the exact sixth-power amplification identity [1, (17.90)] remains
$$
M_{j,u}(D;W)=\sum_{d\mid\operatorname{rad}(a)}
\frac{\mu(d)\psi_u(d)}{\sqrt{q_d}}
M_{j,ua^6}(D/q_d;W).
\tag{4.9}
$$
Indeed, split a squarefree column uniquely as $n=dm$, with $d\mid\operatorname{rad}(a)$ and $(m,a)=1$. Then $\psi_{ua^6}(m)=\psi_u(m)\mathbf1_{(m,a)=1}$, including when $(u,a)>1$, and multiplicativity and the change $D\mapsto D/q_d$ give (4.9). Its coefficient mass is divisor-bounded. As in [1, Lemma 17.6], take a scale supremum in (4.2), set $H=\max(2U,D^{1+c})$, and average over good $a$ of norm at most $P=(H/U)^{1/6}$. The map $(u,a)\mapsto ua^6$ is injective for sixth-power-free $u$, including its unit. The bound is $H/P$ times small powers. Choosing $c$ sufficiently small and absorbing $D^{5c/6}$ into the prescribed $\varepsilon$ proves (4.3). The source Sobolev argument for norm-twisted tests is unchanged. $\square$

## 5. An inverse estimate on cubic rows

We use the normalization $q_b^{-1/2}$ from now on; it is equivalent to (4.1) after multiplying its test by a fixed power on the annulus. For a fixed puncture $Q$, set
$$
\mathcal V_j(T,L;Q)=\sum_{0<q_k\leq T}
\left|\sum_{\substack{b\ \text{good, squarefree}\\(b,Q)=1}}
\frac{\mu(b)\alpha(b)^j\nu(b)}{\sqrt{q_b}}
\chi_b(k)^2W(q_b/L)\right|^2.
\tag{5.1}
$$

**Lemma 4.** For $T,L\geq1$,
$$
\mathcal V_j(T,L;Q)
\ll (TLq_Q)^\varepsilon
\left(T^2+T^{1/3}L^{5/6}\right).
\tag{5.2}
$$
The same bound holds with the extra factor $\varphi(b)/q_b$ in the inner sum.

**Proof.** First note an exact puncture identity. For any completely multiplicative $\psi$ with $|\psi|\leq1$ and the stated zero extensions,
$$
\sum_{(n,Q')=1}\frac{\mu(n)\psi(n)}{\sqrt{q_n}}W(q_n/L)
=\sum_{\operatorname{rad}(e)\mid Q'}\frac{\psi(e)}{\sqrt{q_e}}
\sum_n\frac{\mu(n)\psi(n)}{\sqrt{q_n}}W(q_nq_e/L).
\tag{5.3}
$$
Here $e$ ranges over all integral ideals supported on the primes of $Q'$, including arbitrary nonnegative powers of those primes; it is not restricted to squarefree divisors. The identity follows by reciprocal Euler-factor convolution and is finite on the annular support. Its absolute outside coefficient mass is at most
$$
\prod_{p\mid Q'}(1-q_p^{-1/2})^{-1}\ll_\varepsilon q_{Q'}^\varepsilon.
\tag{5.4}
$$
When $\psi$ includes a row character, each $\psi(e)$ is a bounded row multiplier. Minkowski's inequality therefore transfers (4.3) to a fixed puncture with the loss (5.4); shortening the column scale cannot increase either term in (4.3). Nonempty column scales below one lie in a fixed bounded interval and are covered directly.

Write $k=v a^3$, where $v$ is a cubefree element and $a$ is the chosen multiplicative generator of an integral ideal. Generators at the finitely many excluded primes can be fixed once and for all, as in [1, Lemma 4.1]. The unit remains in $v$. No coprimality between $v$ and $a$ is imposed. We have exactly
$$
\chi_b(k)^2=\chi_b(v^2)\mathbf1_{(b,a)=1}.
\tag{5.5}
$$
The row $v^2$ is sixth-power-free, and $v\mapsto v^2$ has multiplicity at most two. For $q_a\asymp A$, apply (4.3), its dyadic ball version, and (5.3) with puncture $Qa$. The bound for each fixed $a$ is, up to small powers,
$$
(T/A^3)^2+(T/A^3)^{1/3}L^{5/6}.
$$
There are $O(A)$ such ideals. The two contributions are respectively $T^2A^{-5}$ and $T^{1/3}L^{5/6}$. Summing the dyads proves (5.2).

For the Euler weight, expand
$$
\frac{\varphi(b)}{q_b}=\sum_{e\mid b}\frac{\mu(e)}{q_e}.
\tag{5.6}
$$
Extracting $e$ from squarefree $b$ leaves an inverse polynomial at scale $L/q_e$, with puncture $Qe$, a bounded row multiplier and outside absolute coefficient $q_e^{-3/2}$. Its mass is summable over ideals, even after a factor $q_e^\delta$ for fixed $\delta<1/2$. Minkowski and (5.2) prove the weighted assertion. $\square$

## 6. Cubic Poisson summation with all common divisors

We prove Theorem 1 first with $Q=1,w=1$.

### 6.1. The first gcd and its conductor

Open the square in (1.3) and write
$$
b_1=ga,\qquad b_2=gb,\qquad (a,b)=1,
$$
where $g,a,b$ are squarefree and $(ab,g)=1$. The row character is
$$
\chi_a(z)^4\chi_b(z)^2\mathbf1_{(z,g)=1}.
\tag{6.1}
$$
The coefficient satisfies the exact CRT relation
$$
D_j(ga)=D_j(g)D_j(a)\chi_a(g)^4,
\tag{6.2}
$$
and similarly for $b$. The common factor $D_j(g)$ cancels in the square.

For the nonprincipal terms, the primitive character in (6.1) has conductor $ab$. Its normalized Gauss root is
$$
\begin{aligned}
\gamma(\chi_a^4\chi_b^2;ab)
&=\gamma_4(a)\gamma_2(b)\chi_a(b)^4\chi_b(a)^2\\
&=\gamma_4(a)\gamma_2(b).
\end{aligned}
\tag{6.3}
$$
The last equality is cubic reciprocity on the genuine coprime support. Thus, on putting $I_j(a)=\mu(a)\alpha(a)^j\nu(a)$,
$$
D_j(a)\gamma_4(a)=I_j(a),\qquad
\overline{D_j(b)}\gamma_2(b)=\overline{I_j(b)}.
\tag{6.4}
$$

The principal case is exactly $a=b=1$, hence $b_1=b_2=g$. Its original contribution is $O(N(NB)^\varepsilon)$, by ideal counting and the fixed radial row test. Keep it separate.

The masked Poisson formula [1, Lemma 17.5] is
$$
\sum_{z\in\mathcal O}\psi(z)\mathbf1_{(z,g)=1}\Phi(q_z/N)
=\frac{N\gamma(\psi;m)}{\sqrt{q_m}}
\sum_{d\mid g}\frac{\mu(d)\psi(d)}{q_d}
\sum_{h\in\mathcal O}\overline{\psi(h)}
\widehat\Phi\!\left(\frac{Nq_h}{q_dq_m}\right),
\tag{6.5}
$$
where $\psi$ is primitive modulo $m$, and $\widehat\Phi$ is the radial Fourier transform in the source's self-dual normalization. For nonprincipal $\psi$, the term $h=0$ vanishes.

For $d\mid g$, write $g=dt$ and set $k=hdt^2$. The complete character factor on the $a$ side is
$$
\chi_a(g)^4\chi_a(d)^4\chi_a(h)^2
=\chi_a(k)^2.
\tag{6.6}
$$
This includes every zero; reducing the exponent at a prime of $d$ from eight to two does not delete its mask. Since $g\mid(k)$, the character already supplies the inherited restriction $(a,g)=1$. Moreover,
$$
q_h=\frac{q_kq_d}{q_g^2},\qquad
\frac{Nq_h}{q_dq_aq_b}=\frac{Nq_k}{q_g^2q_aq_b}.
\tag{6.7}
$$

Consequently the nonzero-frequency expression has summand
$$
\frac{N\mu(d)}{q_gq_dq_aq_b}
I_j(a)\overline{I_j(b)}\chi_a(k)^2\overline{\chi_b(k)^2}
W(q_gq_a/B)\overline{W(q_gq_b/B)}
\widehat\Phi\!\left(\frac{Nq_k}{q_g^2q_aq_b}\right),
\tag{6.8}
$$
summed over $g$ squarefree, $d\mid g$, $h\ne0$, $k=h d(g/d)^2$, and coprime squarefree $a,b$.

To permit a complete coprime-projector identity below, restore $a=b=1$ in this nonzero expression. The elementary radial Schwartz bound
$$
A\sum_{h\ne0}|\widehat\Phi(Aq_h)|\ll_\Phi1
$$
shows that its absolute cost at a fixed $g$ is $O(\tau(g)/q_g)$ times the two $W(q_g/B)$ factors. The sum over $g$ is $O(B^\varepsilon)$, absorbed in the diagonal bound. This is the principal restoration of [1, Lemma 17.5]; it makes no nonprincipal assertion at conductor one.

### 6.2. The second gcd and the exact root factor

Define the separate-column expression (6.8), with its formal product norms and full smooth kernel, also off $(a,b)=1$. It agrees with Poisson summation on that support. Insert the complete identity
$$
\mathbf1_{(a,b)=1}=\sum_{s\mid a,\ s\mid b}\mu(s),
\qquad a=sx,\quad b=sy.
\tag{6.9}
$$
Here $x,y,s$ are squarefree and $(xy,s)=1$; after (6.9), $x,y$ need not be mutually coprime. The common $I_j(s)$ has squared modulus one, and the common row character leaves the outer zero $(s,k)=1$. The residual column coefficient is $I_j(x)$ with puncture $s$.

The full real root factor is exactly
$$
\frac{N}{q_gq_dq_s^2q_xq_y}
=\frac{N}{Bq_dq_s}
\frac{B}{q_gq_s\sqrt{q_xq_y}}
\frac1{\sqrt{q_xq_y}}.
\tag{6.10}
$$
The middle factor is bounded and smooth on the actual column support. It will be included once in a common norm profile.

### 6.3. A common profile and a divisor fibre

Partition $g,s,k$ into dyadic annuli with centers $G,S_1,R$. Put $L=B/(GS_1)$. Nonempty column windows give $GS_1\ll B$; bounded nonempty subunit $L$ can be clipped with fixed constants. Use the independent normalized coordinates
$$
y_g=q_g/G,\quad y_s=q_s/S_1,\quad y_k=q_k/R,
\quad y_1=q_x/L,\quad y_2=q_y/L.
$$
The kernel argument becomes exactly
$$
\frac{NR}{B^2}\,y_k y_g^{-2}y_s^{-2}(y_1y_2)^{-1}.
\tag{6.11}
$$
The two old $W$ factors, the middle factor in (6.10) and this kernel, multiplied by fixed larger cutoffs, form one compact logarithmic profile. Its cutoffs are chosen before evaluating any actual row or ideal. Its weighted Fourier $L^1$ norm, at every required fixed order, is
$$
\ll_A\min\{1,(R/T_0)^{-A}\},\qquad T_0=B^2/N.
\tag{6.12}
$$
This follows from the source's joint-profile calculus [1, (17.7), (17.19)–(17.20)], or directly from integration by parts in the five logarithmic coordinates. Euler differentiation of (6.11) introduces fixed exponents, not powers of its scalar $NR/B^2$. The whole smooth kernel is retained; there is no column-dependent sharp selector.

At each Fourier mode, the two inner factors are inverse polynomials at the same scale $L$, with puncture $s$, row $k$, and fixed norm-twisted tests. The other modes are outer phases. Apply weighted Cauchy to the whole $(g,d,h)$-sum at this mode. For each $k$, the fibre has size at most
$$
\#\{(g,d,h):g\ \mathrm{sf},\ d\mid g,\ k=h d(g/d)^2\}
\leq \tau((k))^2.
\tag{6.13}
$$
Indeed $d,t=g/d$ are disjoint squarefree divisors of $(k)$, $dt^2\mid(k)$, and $h$ is unique. The dyadic restrictions only reduce this count. The weight $1/q_d$ is at most one. There is thus no independent count of the $g$-variable. Its original column mask is already in the character and is not reinstated.

Only after this positive inequality, enlarge the $k$-range to its complete $R$-annulus and discard the outer zero $(s,k)=1$. Lemma 4 applies to each of the two inverse norms with puncture $s$. Finally,
$$
\sum_{q_s\asymp S_1}q_s^{-1}\ll1
$$
up to fixed annular constants, and its small puncture power is harmless. Equations (6.10)–(6.13) therefore bound each $(G,S_1,R)$ block by
$$
\frac NB(NBR)^\varepsilon
\min\{1,(R/T_0)^{-A}\}
\left(R^2+R^{1/3}L^{5/6}\right).
\tag{6.14}
$$
The two Fourier-mode test seminorms are integrated against the one common weighted Fourier measure from (6.12). This is why a row-dependent kernel causes no hidden norm loss here.

There are $O(\log(2B)^2)$ pairs of $G,S_1$ dyads. Since $L\ll B$, the sum of (6.14) is, for $T_0\geq1$,
$$
\ll (NB)^\varepsilon\frac NB
\left(T_0^2+T_0^{1/3}B^{5/6}\right).
\tag{6.15}
$$
Choose the preliminary small powers below the final $\varepsilon$. For $T_0<1$, take $A>3$ plus their total loss. Nonzero lattice norms are bounded below, and $T_0^A\leq T_0^2,T_0^{1/3}$, so the same bound follows. Schwartz decay also makes the entire large-frequency tail summable. Substituting $T_0=B^2/N$ and restoring the diagonal proves (1.4) for $Q=w=1$.

### 6.4. The puncture and Euler weight

Inserting $(b_i,Q)=1$ in the original square restricts $g$ and adds $Q$ to the residual inverse puncture after (6.9). Lemma 4 gives the stated $q_Q^\varepsilon$ cost, without modifying (6.7) or (6.13).

For $w(b)=\varphi(b)/q_b$, its coprime multiplicativity gives common factors $w(g)^2$ and, after (6.9), $w(s)^2$, both at most one. The residual inverse coefficient is $I_j(x)w(x)$. The weighted assertion of Lemma 4 applies. This proves both extensions and completes Theorem 1. $\square$

## 7. Relation to the detector and limits of the conclusion

The coefficient (1.6), its Euler weight and a moving but currently fixed puncture all occur in the branch where a squarefree label is assigned to the squarefree dual index of a cubic-theta reflection. Theorem 1 supplies a mean-square input for that branch. It also identifies a reason that an absolute-value treatment of the label is wasteful: the cubic Gauss root removes $\gamma_2$ and exposes a multiplicative inverse coefficient.

An application to a mixed detector must still account for the residual cube index and the joint reflection kernel at the actual row, column and label scales. If the row norm is $K$, label norm is $B$, and completed original column length is $Y$, the largest residual squarefree dual scale in this branch is of order $K^2B/Y$. It can already exceed $B^2$, where the generic cubic sieve is sufficient. Thus the improved threshold in (1.5) alone gives no new exponent for the full mixed inverse/plain detector.

We assert no new zero-free region, no solution of RH, no general large-sieve improvement, and no estimate uniform in a growing angular order. The fixed modes $j=\pm1$, for which the initializer can meet the zero theta mode, are outside the result. We also do not allow an arbitrary bounded multiplier on the column of (1.3): the prescribed coefficient, fixed ray factors, puncture and Euler weight are part of the theorem.

## 8. Reproducibility and checks

The proof is analytic. The supplement contains two independent numerical convention checks and their saved outputs:

* `higher_angular_mellin_check.py` integrates the direct and reflected Bessel expressions at 50 decimal digits for derivative orders $1,2,3,6$. All eight relative errors are below $2.2\times10^{-50}$. It checks the normalization and conductor power in (3.6)–(3.8) for the negative modes; the positive-mode scalar is derived in the proof.
* `angular_cubic_gcd_check.py`, using the included finite arithmetic helper, directly evaluates composite Gauss roots from prime norms $7,13,19$. It checks (6.3), the full phase identity (6.6) together with (6.2)–(6.4), and the common-factor zero in (6.9). At 70 digits, its 240 full-gcd checks and 1,250 shared-factor checks have maximum errors below $1.8\times10^{-69}$ and $1.2\times10^{-70}$, respectively.

Run the scripts with Python 3 and `mpmath`; no GPU or external data is required. These finite checks verify conventions and masks. They are not evidence for an asymptotic exponent beyond the proof, nor a verification of all the analytic dependencies in [1]. The included code and result files are released under the MIT license stated in the supplement. The cited primary PDFs are not redistributed.

## References

[1] OpenAI. *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane $\Re s>7/8$*. September 30, 2026. Version pinned at repository commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`, particularly Sections 4–5, 14 and 17. https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf

[2] D. R. Heath-Brown. *Kummer's conjecture for cubic Gauss sums*. Israel Journal of Mathematics **120**, part A (2000), 97–124, Theorem 2. https://doi.org/10.1007/s11856-000-1273-y

[3] Alexandre de Faveri. *Optimal large sieve for fixed order characters*. 2026, arXiv:2610.04045v1. https://arxiv.org/abs/2610.04045v1

[4] Alexander Dunn and Maksym Radziwiłł. *Bias in cubic Gauss sums: Patterson's conjecture*. arXiv:2109.07463v3, particularly Propositions 5.2–5.3 and their proofs. https://arxiv.org/abs/2109.07463v3

[5] OpenAI. *An unconditional first moment for cubic Gauss sums*. September 25, 2026. https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/paper.pdf

[6] Alexandre de Faveri, Alexander Dunn and Jeffrey Hoffstein. *Non-orthogonality of the cubic and quartic large sieves via Rankin–Selberg*. 2026, arXiv:2607.07911v2. https://arxiv.org/abs/2607.07911v2

[7] Yuanda Xu and Hejian Sang. *A sharp lower bound for the sextic large sieve*. 2026, arXiv:2610.17675v1. https://arxiv.org/abs/2610.17675v1
