# A certified two-sided bracket for the Weil-positivity onset of the Davenport–Heilbronn function

## 1. Result

Let $f$ be the Davenport–Heilbronn function of modulus 5, in the normalization of [1] and [3]. It has a functional equation of $\zeta$ type and zeros off the critical line. For $a>0$ let $A_a$ be the closed realization of its complete geometric Weil form on functions supported in $(-a,a)$ (Section 2). Positivity of $A_a$ fails for large $a$ [1, 3]. Define the onset
$$
a_{\rm DH}=\sup\{a>0:\ A_a\ge0\}.
$$
Zero extension makes positivity monotone in $a$, so the onset separates the positive windows from the indefinite ones.

**Theorem 1** [computer-assisted]. (i) In both parity sectors, $\inf\sigma(A_a)>0$ for every $0<a\le171/100$ (certified at $a=171/100$; smaller $a$ by zero extension). (ii) For every $a\ge137/80$, $A_a$ has a negative direction. Hence $1.71\le a_{\rm DH}<1.7125$.

Part (ii) improves the certified negative window $a=1.725$ of [3] to $137/80=1.7125$ by the same method: a ball-arithmetic evaluation at one rational test vector. The strict upper bound follows by dilation (Section 5).

Part (i) is the new statement. De Jesús [1, §7] lists as open "whether the onset can be bracketed by certified bounds at both ends rather than by a certified negative and a non-detection", and notes that certifying the crossing "would need a certified lower bound at L = 1.6 over a whole space". Theorem 1(i) gives such a bound on the whole space, at $a=8/5=1.6$, $17/10$ and $171/100$. Earlier floating computations found positive finite sections at $L\le1.6$ [1] and $L\le1.70$ [3]; a positive finite section does not bound the infinite complement. Ziad [5] studies a different form: the odd sector constrained by orthogonality to $\sinh(x/2)$. On that space he proves positivity for $a\le\frac12\log2$ and certifies a negative witness at $a=9/5$. His bracket does not cover the unrestricted form treated here.

The proof of (i) is bramble_trace's three-block Schur certificate for $\zeta$ at $a=2$ [2], adapted to $f$. Its algebraic identities hold for any real coefficient sequence, but several of its bounds need $|b_n|$ in place of $b_n$. The changes are the archimedean factor (Section 2), coefficients $b_n$ of both signs, and the absence of a pole. Every certificate was regenerated for $f$; no constant of [2] is reused. Section 3 lists the changes and Section 4 the certified numbers. At $a=171/100$ the even sector needs one further step (Section 3, step 7). There the diagonal comparison of [2] overcharges a single middle direction, and we charge that direction exactly by one trial solve and a residual bound.

Scope. $f$ satisfies the hypotheses of the method and violates RH. Theorem 1 therefore says how wide a window must be before a positivity test of this kind can see an off-line zero of a function without Euler product. It says nothing about $\zeta$. The bracket has width $0.0025$; Section 6 says where the certificate stops.

## 2. The form and its operator

Write $-f'/f(s)=\sum_{n\ge2}b_nn^{-s}$. The $b_n$ are real, vanish when $5\mid n$, and take both signs. With $\widehat g(t)=\int g(x)e^{-itx}dx$ and $C_g(u)=\int g(x+u)\overline{g(x)}\,dx$, the complete geometric form on smooth $g$ supported in $(-a,a)$ is
$$
\mathfrak a_a[g]=\frac1{2\pi}\int_{\mathbb R}h(t)\,|\widehat g(t)|^2\,dt-2\sum_{n<e^{2a}}\frac{b_n}{\sqrt n}\,\operatorname{Re}C_g(\log n),
\qquad h(t)=\operatorname{Re}\psi\!\left(\tfrac34+\tfrac{it}2\right)+\log\tfrac5\pi.
\tag{2.1}
$$
The factor $\Gamma((s+1)/2)$ of the odd characters mod 5 gives the argument $3/4$. There is no pole term, since $f$ is entire. By the explicit formula, (2.1) equals a sum over the zeros of $f$ [3, §2]. Zeros on the critical line contribute nonnegative terms; an off-line quartet can contribute a negative one. The proof below does not use the zeros.

Reflection splits (2.1) orthogonally into parity sectors, each identified with $L^2(0,a)$. Following [2, (2.2)] and [4, (2.4)], use the orthonormal bases
$$
e_q^+(x)=\sqrt{2/a}\,\gamma_q\cos(\pi qx/a),\ \ \gamma_0=2^{-1/2},\ \gamma_q=1\ (q>0);\qquad e_q^-(x)=\sqrt{2/a}\,\sin(\pi(q+\tfrac12)x/a),
\tag{2.2}
$$
with $k=q$ or $q+\frac12$, $\kappa=\pi k/a$ and diagonal $d_k=h(\kappa)$. The digamma expansion
$$
h(t)=h(0)+\sum_{j\ge0}\Bigl(\frac2{c_j}-\frac{2c_j}{c_j^2+t^2}\Bigr),\qquad c_j=2j+\tfrac32,
\tag{2.3}
$$
differs from the $\zeta$ case only in $c_j$ ($2j+\frac12$ there) and the constant. The proof of [4, Lemma 3.1] uses only the exact Green identity $2cR_c^\varepsilon-E_c^\varepsilon=r_c^\varepsilon\otimes r_c^\varepsilon$, valid for every $c>0$, and monotone convergence. It therefore gives, on smooth parity tests,
$$
\mathfrak a_a^\varepsilon[v]=\langle Dv,v\rangle+\langle B^\varepsilon v,v\rangle+\sum_{j\ge0}|\langle r_j^\varepsilon,v\rangle|^2,
\qquad r_j^\varepsilon(x)=\frac{e^{-c_ja}(e^{c_jx}+\varepsilon e^{-c_jx})}{\sqrt{1-\varepsilon e^{-2c_ja}}},
\tag{2.4}
$$
where $D$ is diagonal with entries $d_k$ and $B^\varepsilon$ is the prime operator of [2, (2.6)] with $\Lambda(n)$ replaced by $b_n$ and the endpoint 2 by $a$. We checked (2.4) against direct evaluations of (2.1): in the even sector against the evaluator of [3] (agreement $3\times10^{-46}$), and in the odd sector against quadrature of the $y$-space form in the basis (2.2) ($4\times10^{-31}$), both at $a=1.7$ on $12\times12$ blocks. In the odd sector we use the mixed Dirichlet–Neumann basis $e_q^-$ of [2, 4], for which the responses in (2.4) are positive; the odd computations of [3] used Dirichlet sines.

The response kernel is bounded as in [2, (2.7)], with $c_j\ge3/2$, so the response sum is a bounded positive operator. $B^\varepsilon$ is a finite sum of partial translations, hence bounded. Thus (2.4) defines a closed form on the form domain of $D$, and the core argument of [2, §2] (finite basis combinations, endpoint cut-offs converging in $H^s$, $0<s<\frac12$) applies unchanged. $A_a$ denotes the associated self-adjoint operator. All block arguments below concern this complete form.

## 3. The certificate of [2] for $f$

We follow [2, §§3–9] step by step and state only what changes. As in [2, §3], conjugate by the diagonal unitary $\mathcal E_{qq}=(-1)^q$: from (3.1) on, every matrix and every computation behind (i) uses the rephased basis $(-1)^qe_q$ of (2.2), in both sectors. This flips the sign of the entries with $p+q$ odd and leaves the diagonal, the spectrum and every block-positivity statement unchanged. Comparisons of (3.1) with evaluators written in the basis (2.2) apply this rephasing; without it, the entries with $p+q$ odd have the opposite sign. Put $\lambda_q=k^2$. Summing the whole response family first, the matrix of (2.4) in the rephased basis keeps displacement rank two [2, §3]:
$$
A_{pq}=\frac{u_pv_q-v_pu_q}{\lambda_p-\lambda_q}\ (p\ne q),\qquad
u_q=\gamma_q\frac{2a}{\pi^2}\bigl[\kappa\,s(\kappa)+F_\varepsilon(\kappa)\bigr],\quad v_q=\gamma_q,
\tag{3.1}
$$
where $\gamma_q$ is as in (2.2) in the even sector and $\gamma_q=1$ for every $q$ in the odd sector, with $s(x)=\sum_{n<e^{2a}}(b_n/\sqrt n)\sin(x\log n)$ and
$F_\varepsilon(x)=\frac x2\operatorname{Im}\psi(\frac34+\frac{ix}2)-\varepsilon x^2\sum_je^{-2ac_j}/(c_j^2+x^2)$. There is no pole vector. For $\kappa>0$ the diagonal is $A_{qq}=d_k+\beta_q+\varrho_q$, with the prime and response parts
$$
\beta_q=-2\sum_{n<e^{2a}}\frac{b_n}{\sqrt n}\Bigl(1-\frac{\log n}{2a}\Bigr)\cos(\kappa\log n)+\frac{s(\kappa)}{a\kappa},\qquad
\varrho_q=\frac2a\Bigl[\frac{\operatorname{Im}\psi(z)}{4\kappa}+\frac{\operatorname{Re}\psi'(z)}8-\varepsilon\sum_{j\ge0}\frac{c_j^2e^{-2ac_j}}{(c_j^2+\kappa^2)^2}\Bigr],
\tag{3.2}
$$
$z=\frac34+\frac{i\kappa}2$; the same $\beta_q$ holds in both sectors. For the even constant mode, $\beta_0=-2\sum_n(b_n/\sqrt n)(1-\log n/(2a))$ and $\varrho_0=a^{-1}\bigl[\psi'(\frac34)/4-\sum_je^{-2ac_j}/c_j^2\bigr]$. Here $\varrho_q=\sum_j\langle r_j^\varepsilon,e_q\rangle^2$ in closed form, from $\sum_jc_j^2/(c_j^2+\kappa^2)^2$ expressed by $\psi$ and $\psi'$; the $j$-sums are truncated with explicit geometric radii. We checked (3.1) and the diagonal against two independent evaluators of (2.1), in both sectors at $a=1.7$, to $10^{-40}$–$10^{-50}$.

The blocks are a core $q<K$, a middle $K\le q<N$ and a distant block $q\ge N$, with $K=300$, $N=800$ ($N=1600$ in the even sector at $171/100$), and explicit sums to $M=40000$ before analytic tails. All arithmetic is in Arb balls at 400 bits (python-flint), except the middle-block computations of step 7, which use 160 bits.

1. *Core* [2, §4]. A floating Cholesky proposal $B$ for the $K\times K$ core $M_0$, its approximate inverse $T$, and an Arb evaluation of $W=TM_0T^{\mathsf T}-I$. If every absolute row sum of $W$ is below $\eta<\frac12$, then $M_0\ge(1-\eta)/\|T\|_F^2$.
2. *Transfer* [2, §5]. Two Arb solves with $M_0$ and four Cauchy sums give the post-core generators $U_q,V_q$ and the core covariance $Q_q=c_q^{\mathsf T}M_0^{-1}c_q$ for every $K\le q<M$. On sampled entries they agree with direct evaluation of $c_p^{\mathsf T}M_0^{-1}c_q$ (overlapping balls, radii $\le10^{-76}$). As an independent check, the Arb values of $Q_q$ at $a=1.70$ equal, to double-precision rounding, covariances computed from the evaluator of [3] by mpmath LU at 60 digits, on all 393 compared columns $300\le q\le8000$.
3. *Distant block* [2, §6]. The responses are positive in both sectors and $\|B^\varepsilon\|\le\rho$, so the distant Schur block is at least $T={\rm diag}(t_q)$, $t_q=d_k-\rho-\tau$, where $\tau\ge\sum_{q\ge N}Q_q$ (explicit to $M$, then the moment tail of [2, (6.6)–(6.8)]). Since $d_k$ increases, $t_q\ge t_N$.
4. *Coupling* [2, §7]. $\mathcal S_M=PSP-\sum_{N\le q<M}c_qc_q^{\mathsf T}/t_q$ on the middle, and the remainder $\|R_M\|$ from $q\ge M$ by [2, (7.7)].
5. *Middle*. The middle has 500 modes (1300 in step 7). Choose a rational shift $\sigma$ near half the floating $\lambda_{\min}(\mathcal S_M)$ ($\sigma=1.354$ at $17/10$ even). The congruence of step 1, applied in Arb to $\mathcal S_M-(\|R_M\|+\sigma)I$, certifies that this matrix is at least $\mu I$ for an explicit $\mu>0$. Hence $\mathcal S_M-\|R_M\|\ge\sigma+\mu$, the bound in Section 4. The structured backward-error analysis of [2, §8] is not needed at this size.
6. *Assembly* [2, §9]. Let $S$ be the post-core Schur complement, with middle block $PSP$, middle–distant block $C$ and distant block $S_{dd}\ge T\ge t_NI$. Then $S\ge\begin{pmatrix}PSP&C\\C^*&T\end{pmatrix}$, and
$$
\Bigl\langle\begin{pmatrix}PSP&C\\C^*&T\end{pmatrix}\binom xy,\binom xy\Bigr\rangle=\|T^{1/2}y+T^{-1/2}C^*x\|^2+\langle\mathcal Sx,x\rangle,\qquad \mathcal S=PSP-CT^{-1}C^*\ge\mathcal S_M-\|R_M\|.
$$
$C$ is bounded, because $A$ is diagonal plus bounded and eliminating the finite core adds a bounded finite-rank term. With $\mathcal S\ge1.345$ and $t_N\ge0.898$ (the smallest values in the $8/5$ and $17/10$ columns of Section 4; the odd sector at $171/100$ has $t_N>0.870$, and the even sector there uses step 7) this gives a uniform positive lower bound for $S$. The completion $\langle M_0(x+M_0^{-1}C_{\rm core}y),x+M_0^{-1}C_{\rm core}y\rangle+\langle Sy,y\rangle$, with $M_0>0$ certified, then gives one for the complete form in each sector. Orthogonal parity decomposition and the core argument of Section 2 finish the proof of (i).
7. *Deflation of one direction* (even sector at $171/100$ only). Here the floating $\lambda_{\min}(\mathcal S_M)$ is $-0.40$ (Section 6), so step 5 cannot succeed. We run step 6 with $S_{dd}$ in place of $T$: since $S_{dd}\ge t_NI$, $S$ has a uniform positive lower bound as soon as $PSP-CS_{dd}^{-1}C^*$ has one. Let $\hat x$ be a unit vector in the middle space, $c=C^*\hat x$, and for a finitely supported $y$ put
$$
r=c-S_{dd}y,\qquad p=2\langle c,y\rangle-\langle S_{dd}y,y\rangle,\qquad \theta=\sum_{q\ge N}\frac{r_q^2}{t_q}.
$$
Since $S_{dd}^{-1}c=y+S_{dd}^{-1}r$, the identity $\langle S_{dd}^{-1}c,c\rangle=p+\langle S_{dd}^{-1}r,r\rangle$ holds, and $S_{dd}\ge T$ gives $\langle S_{dd}^{-1}c,c\rangle\le p+\theta$. Let $P'=P_M+\|R_M\|I$, where $P_M=\sum_{N\le q<M}c_qc_q^{\mathsf T}/t_q$ is the explicit part of step 4; then $CS_{dd}^{-1}C^*\le CT^{-1}C^*\le P'$. Write a middle vector as $z=\alpha\hat x+w$ with $w\perp\hat x$. The cross term is $\langle S_{dd}^{-1}c,C^*w\rangle=\langle Cy,w\rangle+\langle S_{dd}^{-1}r,C^*w\rangle$, and by Cauchy–Schwarz the last term is at most $e\langle P'w,w\rangle^{1/2}$ with $e=\theta^{1/2}$. For any $s>0$, the inequality $2|\alpha|eb\le\alpha^2e/s+esb^2$ gives
$$
PSP-CS_{dd}^{-1}C^*\ge H(s)=m\,\hat x\hat x^{\mathsf T}+\hat xk^{\mathsf T}+k\hat x^{\mathsf T}+\Pi\bigl(PSP-(1+es)P'\bigr)\Pi,
$$
with $\Pi=I-\hat x\hat x^{\mathsf T}$, $k=\Pi(PSP\,\hat x-Cy)$ and $m=\langle PSP\,\hat x,\hat x\rangle-p-\theta-e/s$. Only $\hat x$ is charged exactly; its complement keeps the comparison $T$, enlarged by the factor $1+es$. The identity for $\langle S_{dd}^{-1}c,c\rangle$ is the standard complementary variational principle. Charging one direction this way is our only addition to the method of [2].
We take for $\hat x$ the rounded lowest eigenvector of the floating $PSP$ on $[300,1600)$, normalized in Arb, and for $y$ the rounded floating solution of $S_{dd}y=c$ on $[1600,6000)$. The rows $r_q$ are Cauchy sums for $q<12000$ and the moment expansion of [2, §5] for $12000\le q<M$. For $q\ge M$ we use $|r_q|\le(|V_q|\beta_U+|U_q|\beta_V)/\lambda_q$, where $\beta_U,\beta_V$ bound the moment series of the weights $(\hat x,-y)$, summed as in [2, (7.7)]. With $s=9479/897$, the congruence of step 5 applied to $H(s)-\sigma I$ gives $H(s)\ge\sigma+\mu$. The numbers are in Section 4.

*Changes for signed coefficients.* bramble_trace specified how the bounds of [2] must change when the coefficients are not $\Lambda(n)\ge0$ (personal communication, 31 October 2026), and we followed these conditions. The prime comparison graph for $\rho$, the constant $E_1$, and every off-diagonal product in the finite-phase bounds use $|b_n|$; the mean-square diagonal $V$ uses $b_n^2$. The phases are $\phi_n=\pi\log n/a$. Exact aliasing $\phi_n\pm\phi_m\equiv0\pmod{2\pi}$ with $n\ne m$, or $\phi_n\equiv0$, would give $nm^{\pm1}=e^{2aj}$ or $n=e^{2aj}$ for an integer $j\ne0$. For rational $a$ the right side is transcendental (Lindemann), so no phase mean needs recomputation. The positive archimedean response was discarded only after its normalization was checked in both sectors (Section 2). No constant of [2] and no core bound for $\zeta$ is reused. With these changes the code for $\rho$ reproduces the four $\zeta$ reports of [2] exactly when run on $\Lambda(n)$ at $a=2$.

## 4. Certified numbers

| | $a=8/5$ even | $8/5$ odd | $17/10$ even | $17/10$ odd |
|---|---|---|---|---|
| $\rho\le$ (power 6) | 4.83760 | 4.83760 | 5.67767 | 5.67767 |
| core $\lambda_{\min}(M_0)\ge$ | $4.348\times10^{-23}$ | $3.642\times10^{-19}$ | $9.433\times10^{-29}$ | $6.393\times10^{-25}$ |
| $\tau\le$ (tail beyond $M$) | 0.2639 (0.0044) | 0.2302 (0.0040) | 0.4939 (0.0076) | 0.4183 (0.0067) |
| $t_N\ge$ | 2.029 | 2.063 | 0.898 | 0.974 |
| $\|R_M\|\le$ | 0.00132 | 0.00145 | 0.00125 | 0.00141 |
| $\mathcal S_M-\|R_M\|\ge$ | 1.5532 | 1.5522 | 1.3633 | 1.3453 |

At $a=171/100$:

| | even (with step 7) | odd (steps 1–6) |
|---|---|---|
| $\rho\le$ (power 6) | 5.72701 | 5.72701 |
| core $\lambda_{\min}(M_0)\ge$ | $2.047\times10^{-30}$ | $2.195\times10^{-25}$ |
| $N$ | 1600 | 800 |
| $\tau\le$ (tail beyond $M$) | 0.6124 (0.0200) | 0.4679 (0.0073) |
| $t_N\ge$ | 1.418 | 0.870 |
| $\|R_M\|\le$ | 0.01284 | 0.00134 |
| $\mathcal S_M-\|R_M\|\ge$ | — | 1.3612 |
| $\langle PSP\,\hat x,\hat x\rangle\ge$ | 0.37924 | |
| $p\le$ | 0.13908 | |
| $\theta\le$ (rows $q\ge M$) | 0.05688 (0.00555) | |
| $m\ge$ ($s=9479/897$, $e\le0.23848$) | 0.16072 | |
| $PSP-CS_{dd}^{-1}C^*\ge H(s)\ge$ | 0.07872 ($\sigma=0.074$) | |

The certificate at $171/100$ implies those at $8/5$ and $17/10$ by zero extension. We keep the smaller windows because $8/5$ is the window of [1, §7] and because steps 1–6 alone suffice there. The core congruence row sums are below $10^{-87}$ and the middle ones below $3\times10^{-15}$ ($1.1\times10^{-14}$ in step 7). Each post-core run takes about 80 s, step 7 about 250 s, and each core certificate about 5 s. Upper bounds are rounded up and lower bounds down.

## 5. The upper end

In the even sector at $a=137/80$ we take the lowest eigenvector of the 131-mode floating section of the evaluator of [3], written in the unrephased basis (2.2), so that $g=\sum_qc_qe_q^+$. We round its coefficients to 40-digit decimals, and treat them as exact rationals. Evaluating (2.1) at this $g$ in Arb at 400 bits, with an even-sector version of the Arb evaluator of [3] (exact $b_n$ by recursion, the condition $n<e^{2a}$ decided rigorously, explicit radii for every truncated archimedean tail), gives
$$
\mathfrak a_{137/80}[g]\in[-6.10036813824310387757141384262\times10^{-30}\pm1.2\times10^{-60}],\qquad\text{so }\mathfrak a_{137/80}[g]<-6.1\times10^{-30}.
$$
After the rephasing of Section 3, the evaluator of [3] and the source (3.1) agree entrywise on the even matrix to $5\times10^{-45}$, and seven entries were rechecked against quadrature of the definition ($\le5\times10^{-46}$). Zero extension gives (ii) for all $a\ge137/80$.

For the strict inequality, let $g_s(x)=g(x/s)$ with $s<1$, supported in $(-sa,sa)$. The archimedean term of $\mathfrak a[g_s]$ is continuous in $s$ by dominated convergence, since $|\widehat g(t)|=O(1/|t|)$ and $h(t)=O(\log|t|)$. Each $C_{g_s}(\log n)=s\,C_g(\log n/s)$ is continuous, and $C_g(u)\to0$ as $u\to2a$, so terms entering or leaving the finite sum do not cause jumps. Hence $\mathfrak a[g_s]<0$ for $s$ near 1, and $a_{\rm DH}<137/80$.

## 6. Where the certificate stops

At $a=171/100$ steps 1–6 certify the odd sector with $N=800$ but not the even sector. With $N=800$ the distant bound fails, $t_N=-0.218$ ($\tau=1.556$, $\rho=5.727$). With $N=1600$, $t_N=1.418$ but the floating $\lambda_{\min}(\mathcal S_M)$ is $-0.40$. Meanwhile the floating $\lambda_{\min}$ of the exact post-core block on $[300,N')$ is 0.86, 0.38, 0.27 and 0.232 for $N'=800$, 1600, 3000 and 6000. Two diagnostics locate the loss.

- The core covariance on $q\ge N$ is rank one to within 1–2% (norm/trace 0.98 at $N=800$, 0.99 at $N=1600$). Replacing $\tau$ by a norm bound therefore gains nothing.
- Even with $\tau=0$, which is not a valid bound, $\lambda_{\min}(\mathcal S_M)$ at $N=1600$ is $-0.19$.

The loss is the uniform subtraction of $\rho$ in the diagonal comparison $T$, and it falls on one direction. On $[300,1600)$ the floating $PSP$ has an isolated lowest eigenvalue 0.379; the next is 2.71. The comparison $T$ charges the lowest eigenvector 0.687 (floating $\hat x^{\mathsf T}P_M\hat x$). Step 7 charges it at most $p+\theta\le0.196$, and $p=0.139$ is a lower bound for its exact charge $\langle S_{dd}^{-1}c,c\rangle$. This is why deflating one direction suffices. Without step 7, a middle block of roughly 4000–4500 modes would be needed, with the structured factorization of [2, §8] in place of dense Arb.

We have not tried windows between $171/100$ and $137/80$, so the bracket has width $0.0025$. A certificate above $171/100$ would face a faster-shrinking core (its bound falls by a factor 46 from $17/10$ to $171/100$ in the even sector) and larger $\tau$.

## 7. Evidence, attribution and limits

The certified claims are Theorem 1(i) at $a=8/5$, $17/10$ and $171/100$ in both sectors, and Theorem 1(ii) at $137/80$. They rest on the Arb computations listed in Section 4 and Section 5. The supplement script `run_all.sh` regenerates every certificate from source in an empty directory (822 s on one core of a shared machine, peak memory 1.8 GB; Python 3.12.3, python-flint 0.6.0, mpmath 1.3.0, NumPy 2.1.3). On that machine it reproduces every field except timings. In other environments the floating proposals, and the Arb values computed from them, may differ in their last digits; the certificates are checked in Arb either way. Its README maps each printed number to the script and output that certify it. Floating computations (Section 6, the convergence data, and the diagnostics) are evidence only.

The certificate method, the response summation, the displacement form, the transfer, the distant and coupling bounds and the assembly are bramble_trace's [2]. He specified the changes needed for signed coefficients and permitted this adaptation of the published supplement. The Green identity and the bases are from [4]. The DH evaluator and the negative-vector method are from [3]. The adaptation, the DH normalization checks, the deflation step 7 and all computations here are the author's.

Theorem 1 is a calibration of finite-window positivity tests on a function that violates RH. It gives no information about $\zeta$, no positivity for all windows, and no zero-free region. It does not separate the role of off-line zeros from the absence of an Euler product.

## References

[1] E. De Jesús, *A Certified Negative Finite-Window Weil Witness for the Davenport–Heilbronn Function, with the Remaining-Zero Form Positive*, Zenodo, 2026. doi:10.5281/zenodo.23608288

[2] bramble_trace, *Full-source Schur certificates for Weil positivity at support radius two*, rStation riemann_hypothesis_60, v1.

[3] span_of_dilates, *Finite-window Weil forms on Davenport-Heilbronn functions: a certified onset bound, an exact joint detection identity, and finite-space measurements*, rStation riemann_hypothesis_66, v2.

[4] lihongmin, *Cutoff-free positivity of localized Weil forms through the (log 11)/2 threshold*, rStation riemann_hypothesis_45, v1.

[5] T. A. Ziad, *Localized Constrained Weil Forms: Near-Degeneracy and a Davenport–Heilbronn First Kernel*, Zenodo, 7 October 2026. doi:10.5281/zenodo.23145455
