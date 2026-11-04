# Square-numerator means for quartic Kubota series in nonzero angular type

## 1. Result and relation to previous work

David, Dunn, Hamieh and Lin [1, Section 1.2] anticipate a Lindelöf-on-average estimate in the squarefree parameter of their quartic Gauss-sum series. Their Proposition 9.5 proves an exponent $3/2$ for the normalized level mean; Remark 9.7 suggests that the quadratic large sieve could improve the estimate when that parameter is prime. We prove the exponent $1$ for all squarefree parameters, with a fixed nonzero angular type and a polynomial, rather than optimal, height cost. The prediction and the use of the quadratic large sieve are due to [1]. The contribution here is the direct treatment of the full square-numerator series, including its ramified terms and all completion tails, followed by the level-series transfer.

De Faveri, Dunn and Hoffstein [2, Proposition 8.1] obtain an all-numerator second mean for spherical quartic Kubota series by Rankin–Selberg regularization. Such an ambient estimate, with numerator norm bounded by $A$, cannot supply the square-parameter exponent here just by positivity: numerators $\nu a^2$ with $q_a\le U$ have norm of order $U^2$. Our proof instead uses their square structure and the nonspherical functional equation recorded in [1]. It does not assume an extension or restriction theorem for [2].

Let $\mathcal O=\mathbb Z[i]$, $\lambda=1+i$, and $q_a=Na$. All unqualified sums below run over odd primary Gaussian integers, equivalently odd ideals with their unique primary generators. Write $\mu$ for the Gaussian Möbius function, and put

$$
\omega(a)=\frac{\overline a}{|a|},\qquad
g_4(r,c)=\sum_{x\bmod c}\left(\frac{x}{c}\right)_4
                 \exp\left(2\pi i\operatorname{Tr}_{\mathbb Q(i)/\mathbb Q}\frac{rx}{c}\right),
\qquad \gamma(r,c)=\frac{g_4(r,c)}{\sqrt{q_c}}.
\tag{1}
$$

We use the additive and angular conventions of [1, (3.4), (4.1)]; replacing the angular convention by its conjugate replaces $\ell$ by $-\ell$ throughout. Quartic and quadratic symbols are zero on nonunits. For $\beta\in\{1,1+\lambda^3\}\pmod4$, define

$$
\psi_\beta(v,r,\ell)=
 \sum_{c\equiv\beta\ (4)}\frac{g_4(r,c)\omega(c)^\ell}{q_c^v},
\qquad \operatorname{Re}v>\frac32,
\tag{2}
$$

and use its meromorphic continuation from [1]. Let

$$
\mathcal D=\{i^j\lambda^k:0\le j,k<4\}.
$$

**Theorem 1.** Fix $\ell\in\mathbb Z\setminus\{0\}$ and $0<\delta<1/16$. For every $\epsilon>0$ there is $A=A(\delta,\epsilon,\ell)$ such that, uniformly for $U\ge2$, $t\in\mathbb R$, $\nu\in\mathcal D$ and the two choices of $\beta$,

$$
\sum_{q_a\le U}\mu^2(a)
 \left|\psi_\beta(1+\delta+it,\nu a^2,\ell)\right|^2
 \ll_{\delta,\epsilon,\ell} U^{1+\epsilon}(1+|t|)^A.
\tag{3}
$$

Here and below constants may depend on the fixed field. No hypothesis on zeros of an $L$-function is used.

For the level version, let $\psi_\beta(v,\nu,\ell;\alpha)$ denote (2) with the additional restriction $\alpha\mid c$. Set

$$
\begin{aligned}
Z_\ell(s)&=\sum_d\frac{\omega(d)^{4\ell}}{q_d^{4s-1}},\\
\Delta_s(\alpha)&=\prod_{p\mid\alpha}
             (1-q_p^{1-4s}\omega(p)^{4\ell}),\\
f_{\nu,\beta}(s;\alpha)&=q_\alpha^s
                  \psi_\beta(s+1/2,\nu,\ell;\alpha),\\
h_{\nu,\beta}(s;\alpha)&=Z_\ell(s)\Delta_s(\alpha)
                                      f_{\nu,\beta}(s;\alpha).
\end{aligned}
\tag{4}
$$

These are the normalizations in [1, (9.1)–(9.2)], with the fixed dyadic numerator $\nu$ allowed.

**Corollary 2.** With the hypotheses of Theorem 1 and $s=1/2+\delta+it$,

$$
\sum_{q_\alpha\le U}\mu^2(\alpha)
        |h_{\nu,\beta}(s;\alpha)|^2
 \ll_{\delta,\epsilon,\ell}U^{1+\epsilon}(1+|t|)^A.
\tag{5}
$$

There is a concrete averaged Type-I consequence. For $R\in C_c^\infty((0,\infty))$, define

$$
F_\beta(x,\ell;\alpha)=
 \sum_{\substack{c\equiv\beta\ (4)\\\alpha\mid c}}
              \gamma(1,c)\omega(c)^\ell R(q_c/x).
\tag{6}
$$

**Corollary 3.** For fixed nonzero $\ell$, every $\epsilon>0$, and $1\le U\le x$,

$$
\sum_{q_\alpha\le U}\mu^2(\alpha)
          |F_\beta(x,\ell;\alpha)|
 \ll_{R,\epsilon,\ell}x^{1/2+\epsilon}U^{1/2+\epsilon}.
\tag{7}
$$

This improves the $x^{1/2}U^{3/4}$ part of [1, Lemma 9.1 and Proposition 9.5] in the stated fixed nonzero angular range. As [1] already explains for its anticipated improvement, it does not improve their prime estimate, whose limitation is Type II. It also supplies no zero-density estimate or zero-free region: a fixed square-numerator mean does not control the mixed moving-numerator forms appearing in a quartic zero detector.

## 2. Arithmetic reduction and the common coefficients

The external analytic inputs are [1, Theorem 5.1], the full cusp functional equation [1, (4.24)–(4.28)], and its holomorphy and strip growth [1, Proposition 4.3]. We also use the explicit finite cusp expansions [1, (4.15)–(4.22)] and the exact level identity [1, (8.5)].

The quadratic large sieve, in the orientation needed here, states that

$$
\sum_{q_r\le M}\mu^2(r)
 \left|\sum_{q_c\le C}b_c\mu^2(c)\left(\frac r c\right)_2\right|^2
 \ll_\epsilon (MC)^\epsilon(M+C)\sum_{q_c\le C}|b_c|^2.
\tag{8}
$$

Quadratic reciprocity changes the orientation in [1, Theorem 5.1] to (8). Fixed primary residue restrictions or a fixed column coprimality mask may be included in $b_c$.

For squarefree $a$, local Gauss-sum support [1, (3.4)–(3.7)] implies that the only nonzero odd moduli in $g_4(\nu a^2,c)$ have the form

$$
c=e^3c_1,\qquad e\mid a,\qquad \mu^2(c_1)=1,\qquad(c_1,a)=1.
\tag{9}
$$

Write $a=er$ and $C(e,c_1)=((q_e-1)/4)((q_{c_1}-1)/4)\pmod2$. The exact CRT identity is

$$
\gamma(\nu a^2,e^3c_1)=
 \overline{\left(\frac{\nu}{e^3c_1}\right)_4}
 (-1)^{C(e,c_1)}
 \left(\frac r e\right)_2\left(\frac r{c_1}\right)_2
 \gamma(e^2,e^3)\gamma(1,c_1),
\qquad |\gamma(e^2,e^3)|=q_e.
\tag{10}
$$

Indeed, CRT contributes $(-1)^{C(e,c_1)}(e/c_1)_2$. Numerator twisting contributes $(r/e)_2$ from $e^3$ and $(er/c_1)_2$ from $c_1$; the two occurrences of $(e/c_1)_2$ cancel. The dyadic numerator is a unit modulo the entire odd modulus, giving the first factor in (10).

The two quotient-dependent quadratic symbols in (10) are absent from the printed ramified branch of [1, (9.29)]. Their omission does not affect the absolute estimate subsequently used in [1]. It would affect an application of (8), so we retain both symbols explicitly.

For each fixed $e$, all dependence on $r$ in (10), apart from $(r/c_1)_2$, is a bounded row multiplier. The restrictions $(c_1,e)=1$ and $c_1\equiv e\beta\pmod4$ are common column restrictions; the zero of $(r/c_1)_2$ enforces $(r,c_1)=1$. The restriction $(r,e)=1$ can be dropped by positivity after taking the squared absolute value. Thus (8) has one common column sequence, as required.

## 3. A balanced completed identity

For each of the 24 essential cusps in [1, Section 4], use the shifted completed series

$$
\mathcal Z_j(z,a;\ell)=
 Z_\ell(z)\psi_{j1}(z+1/2,\nu a^2,\ell).
\tag{11}
$$

The two components corresponding to $\beta=1,1+\lambda^3$ differ from $Z_\ell(z)\psi_\beta(z+1/2,\nu a^2,\ell)$ by fixed nonzero constants [1, (4.12)–(4.13)]. We can absorb these constants in subsequent finite linear combinations. Put

$$
G_\infty(v,\ell)=\prod_{j=1}^3
           \Gamma_{\mathbb C}\left(v+\frac{|\ell|}{2}-\frac j4\right),
\qquad \Gamma_{\mathbb C}(v)=2(2\pi)^{-v}\Gamma(v).
\tag{12}
$$

The functional equation [1, (4.28)] gives

$$
\begin{aligned}
\mathcal Z_i(z,a;\ell)
={}&(q_\nu q_a^2)^{1/2-z}\omega(\nu a^2)^{-\ell}
 \frac{G_\infty(3/2-z,-\ell)}{G_\infty(1/2+z,\ell)}\\
&\quad\times\sum_{j=1}^{24}
 A_{ji}(2^{-1/2-z},\ell)\mathcal Z_j(1-z,a;-\ell).
\end{aligned}
\tag{13}
$$

Each $A_{ji}(2^{-v},\ell)$ is rational in $2^{-v}$ and holomorphic when $\operatorname{Re}v\ne1,5/4$. The series $G_\infty(z+1/2,\ell)\mathcal Z_j(z,a;\ell)$ is entire for $\ell\ne0$. Hence $\mathcal Z_j$ is entire as well, since the reciprocal gamma product is entire. The standard strip bounds needed below follow from [1, Proposition 4.3] and Stirling's formula.

Fix a dyadic annulus $U<q_a\le2U$, put $s=1/2+\delta+it$, and choose $x=U$. We use the entire smoothing numerator

$$
J(w)=\frac{e^{w^2}}w,\qquad
E(y)=\frac1{2\pi i}\int_{(c)}J(w)y^{-w}\,dw
    =\frac12\operatorname{erfc}\left(\frac{\log y}{2}\right),\quad c>0.
\tag{14}
$$

For every fixed $B>0$, $E(y)\ll_B\min(1,y^{-B})$ and $1-E(y)\ll_B y^B$. On an absolute right line integrate $J(w)x^w\mathcal Z_i(s+w,a;\ell)$. Move that line to $\operatorname{Re}w=-\operatorname{Re}s-2\eta$, where $0<\eta<\delta$. The only pole crossed is $w=0$. Gaussian vertical decay, the strip bounds and Stirling justify the move. Consequently

$$
\mathcal Z_i(s,a;\ell)=D_i(s,a;x)-V_i(s,a;x),
\tag{15}
$$

where $D_i$ is the original smoothed Dirichlet series and $V_i$ is the integral on the new line after applying (13). In particular, for either original $\beta$ component,

$$
D_\beta=
\sum_d\omega(d)^{4\ell}q_d^{1-4s}
 \sum_{c\equiv\beta\ (4)}
 \gamma(\nu a^2,c)\omega(c)^\ell q_c^{-s}
                              E(q_cq_d^4/x).
\tag{16}
$$

The functional equation preserves the square $a^2$. More precisely, [1, (4.15)–(4.22)] expresses each dual cusp component as a finite sum of raw $\beta$ series with numerator $(-1)^j\lambda^{2b}\nu a^2$. Since $\operatorname{ord}_\lambda(\nu a^2)\le3$, its indexing set has $2\le b\le8$, besides the unshifted terms. Its coefficients are uniformly bounded row functions times fixed factors $2^{-bv}$. Removing fourth powers of the dyadic unit reduces the numerator into $\mathcal D$, term by term for odd moduli. This accounts for every cusp and introduces only finitely many fixed scales and bounded row multipliers.

Opening the dual completion on the initial absolute line, every resulting term of $V_i$ has the form

$$
\begin{aligned}
\rho(a)q_a^{-2\delta-2it}
 \sum_d &\omega(d)^{-4\ell}q_d^{-1+4\delta+4it}\\
 &\times\sum_{c\equiv\beta'\ (4)}
 \gamma(\nu'a^2,c)\omega(c)^{-\ell}
 q_c^{-1/2+\delta+it}
 T\left(s,\frac{Kq_a^2}{xq_cq_d^4}\right),
\end{aligned}
\tag{17}
$$

with $\nu'\in\mathcal D$, fixed $K>0$, and bounded $\rho(a)$. The harmless fixed factors depending on $\nu,s$ may be included in $T$; they have polynomial height cost. There are only finitely many terms of this form.

Each $T$ is a common Mellin integral of $J(w)$, the gamma quotient in (13), a fixed scattering entry, and fixed powers of 2, against $y^{-w}$. Its line can be moved to $\operatorname{Re}w=-B$ for every fixed $B>\delta$. Throughout such a move, the scattering argument has real part $1+\delta+\operatorname{Re}w<1$. Thus it crosses neither possible scattering pole line. The numerator gamma arguments have positive real part there; the reciprocal denominator has no poles. There are no other poles of $J$ in this region. It follows that

$$
T(s,y)=\frac1{2\pi i}\int_{(-B)}M(s,w)y^{-w}\,dw,
\qquad
\int_{\mathbb R}|M(s,-B+iv)|\,dv
       \ll_{B,\delta,\ell}(1+|t|)^A.
\tag{18}
$$

In particular $|T(s,y)|\ll(1+|t|)^A y^B$. Equation (18), rather than just this pointwise bound, will separate the moving row norm from the column coefficients. The choice (14) avoids the negative-integer residues of a $\Gamma(w)$ smoothing kernel when the line is moved far left.

## 4. Mean of the direct sum

Insert (10) in (16). Cauchy's inequality over $e\mid a$ costs $U^\epsilon$. Write $E_0=q_e$ and $D_0=q_d$. The completion weights have summable magnitudes $D_0^{-1-4\delta}$, so weighted Cauchy in $d$ is legitimate. For each $e,d$, the rows $r=a/e$ have length $O(U/E_0)$, the effective $c_1$ length is $x/(E_0^3D_0^4)$, and the squared outside ramified factor is $E_0^{-1-6\delta}$.

On a dyadic range $q_{c_1}\asymp C$, the squared coefficient mass is $\ll C^{-2\delta}$, times the rapid decay of $E(E_0^3D_0^4q_{c_1}/x)$. Apply (8) and sum dyadic norms by Minkowski. For effective length at least 1 this gives, up to a small power, $U/E_0+x/(E_0^3D_0^4)$. If that length is below 1, the rapid cutoff decay gives an additional arbitrary power of the effective length; in particular it yields the same upper bound. Consequently

$$
\begin{aligned}
\sum_{U<q_a\le2U}\mu^2(a)|D_\beta|^2
&\ll U^\epsilon
 \sum_e E_0^{-1-6\delta}\sum_dD_0^{-1-4\delta}
       \left(\frac U{E_0}+\frac x{E_0^3D_0^4}\right)\\
&\ll U^{1+\epsilon},\qquad x=U.
\end{aligned}
\tag{19}
$$

All displayed sums are ideal sums. The exponents needed for their absolute convergence are strictly greater than 1. In using (8) on unbounded column tails, choose its small power loss below $\delta$ and increase the cutoff decay exponent; this justifies the same estimate uniformly on those tails.

## 5. Mean of the dual sum

Insert (10) in (17). The outside magnitudes for each $e,d$ are

$$
U^{-2\delta}E_0^{-1/2+3\delta}D_0^{-1+4\delta}.
\tag{20}
$$

For that fixed pair put $R_0\asymp U/E_0\ge1$ and $Y=KU/(E_0^3D_0^4)$. In particular $Y\ll R_0$, with a fixed implied constant. On $q_{c_1}\asymp C\ge1$, substitute (18). The factor involving the row norm becomes

$$
\left(\frac{q_a}{U}\right)^{-2w};
$$

its absolute value is bounded on the annulus, independently of the Mellin height. Every remaining factor in the inner sum is a common column coefficient, apart from $(r/c_1)_2$. Apply Minkowski to the common integral, then (8). The resulting squared norm on this dyadic column range is

$$
\ll U^\epsilon(1+|t|)^A
       (R_0+C)C^{2\delta}(Y/C)^{2B},\qquad B>\delta.
\tag{21}
$$

This order of operations is essential. A row-dependent cutoff is not treated as if it were a common coefficient sequence.

Choose $B_0=\delta+\eta$ and $B_1=B_0+2$. For $C\le Y$ use $B_0$, and for $C>Y$ use $B_1$. The sum of the square roots of (21) is

$$
\ll U^\epsilon(1+|t|)^A R_0^{1/2}Y^{\delta+\eta}.
\tag{22}
$$

For completeness, when $Y\ge1$ and $C\le Y$, the summand is bounded by a constant times $R_0^{1/2}Y^{B_0}C^{-\eta}$; the dyadic sum converges. For $Y<C\le R_0$ use $B_1$ and sum $C^{-\eta-2}$, whose contribution is at most $R_0^{1/2}Y^{\delta}$. For $C>\max(Y,R_0)$, sum $C^{1/2+\delta-B_1}$; since $Y\ll R_0$, this also satisfies (22). If $Y<1$, all columns use $B_1$, and $Y^{B_1}\le Y^{B_0}$ gives (22) directly. Small sieve losses are absorbed by choosing their exponent smaller than $\eta$ and the desired final loss. These arguments account for all arbitrarily large columns.

Now Minkowski in $d$ is justified: multiplying $D_0^{-1+4\delta}$ in (20) by the $D_0$ part of $Y^{\delta+\eta}$ gives the summable weight $D_0^{-1-4\eta}$. Cauchy over $e\mid a$, followed by (20)–(22), therefore gives

$$
\begin{aligned}
\sum_{U<q_a\le2U}\mu^2(a)|V_i|^2
&\ll U^{\epsilon-4\delta}(1+|t|)^A
 \sum_e E_0^{-1+6\delta}\frac U{E_0}
 \left(U^{\delta+\eta}E_0^{-3\delta-3\eta}
                  \sum_dD_0^{-1-4\eta}\right)^2\\
&\ll U^{1-2\delta+2\eta+\epsilon}(1+|t|)^A
                      \sum_eE_0^{-2-6\eta}\\
&\ll U^{1+\epsilon}(1+|t|)^A.
\end{aligned}
\tag{23}
$$

The finite cusp sum has only changed the constant. In particular, neither the completion divisors nor the ramified moduli require a truncation with an unestimated remainder.

On $\operatorname{Re}s=1/2+\delta$, both $Z_\ell(s)$ and its reciprocal are bounded by absolute Euler products, since $\operatorname{Re}(4s-1)=1+4\delta$. Divide (15) by this factor, use (19), (23), and sum dyadic annuli. The finitely many initial indices are absorbed by the same strip bounds. This proves Theorem 1.

## 6. Transfer to levels and the averaged Type-I estimate

For squarefree $\alpha$, [1, (8.5)] simplifies to

$$
\frac{h_{\nu,\beta}(s;\alpha)}
 {Z_\ell(s)(-1)^{C(\alpha,\alpha\beta)}\omega(\alpha)^\ell}
 =\sum_{mr=\alpha}\mu(m)a_\beta(m)
          \gamma(\nu,r)\psi_{r\beta}(s+1/2,\nu r^2,\ell),
\tag{24}
$$

where

$$
a_\beta(m)=(-1)^{C(m,\beta)+(q_m-1)/4}
               \omega(m)^{3\ell}q_m^{1-3s},
\qquad |a_\beta(m)|=q_m^{-1/2-3\delta}.
\tag{25}
$$

To check the normalization, use $m^2\equiv1\pmod4$ and
$C(m,m\alpha\beta)+C(m,m\alpha)=C(m,\beta)\pmod2$ in that identity, then replace each raw Gauss sum by its normalized version. Since $\nu$ is dyadic and $r$ is odd squarefree, $|\gamma(\nu,r)|=1$. The changing subscript $r\beta$ is handled by partitioning $r$ into its two primary classes modulo 4.

Cauchy's inequality over the divisors of $\alpha$, followed by Theorem 1, gives

$$
\begin{aligned}
\sum_{q_\alpha\le U}\mu^2(\alpha)|h_{\nu,\beta}(s;\alpha)|^2
&\ll U^\epsilon(1+|t|)^A
       \sum_m q_m^{-1-6\delta}(U/q_m)^{1+\epsilon}\\
&\ll U^{1+2\epsilon}(1+|t|)^A.
\end{aligned}
\tag{26}
$$

Dropping the original coprimality of $m,r$ in this positive upper bound is legitimate. Renaming $\epsilon$ proves Corollary 2.

Finally, Mellin inversion of (6) gives

$$
F_\beta(x,\ell;\alpha)=\frac1{2\pi i}
 \int_{(1/2+\delta)}
 \frac{h_{1,\beta}(s;\alpha)}{Z_\ell(s)\Delta_s(\alpha)}
                  (x/q_\alpha)^s\widehat R(s)\,ds.
\tag{27}
$$

The move from the absolute line is justified by (24), the holomorphy for nonzero angular type, and polynomial vertical growth. Both reciprocal factors in (27) are bounded uniformly in $\alpha,t$: all their Euler factors lie in the absolute half-plane. Cauchy's inequality in $\alpha$ and (5) imply

$$
\sum_{q_\alpha\le U}\mu^2(\alpha)q_\alpha^{-1/2-\delta}
                   |h_{1,\beta}(s;\alpha)|
 \ll U^{1/2+\epsilon}(1+|t|)^A,
\tag{28}
$$

because $\sum_\alpha q_\alpha^{-1-2\delta}$ converges. The rapid vertical decay of $\widehat R$ completes (7), by taking $\delta>0$ smaller than the requested loss. This proves Corollary 3.

## 7. Scope and reproducibility

The nonzero angular restriction removes the theta poles before the contour shift. The zero-angular case, optimal hybrid dependence on $t$ and $\ell$, and a uniform theorem for a growing odd multiplier of $a^2$ are not claimed. Those extensions cannot be inferred by changing a fixed constant in (3). The RH task remains unresolved.

The proof is analytic; finite computations are controls on (10), not evidence for (3). The supplement provides a CPU checker with exact Gaussian character arithmetic and floating evaluations of complete finite residue sums, including split, conjugate and inert primes. All 1,072 fixtures passed, including 64 with a composite ramified divisor and all sixteen choices of $\nu$. The largest relative discrepancy was $1.8\times10^{-15}$, below the declared $10^{-10}$ tolerance. Removing the two quotient-dependent phases fails in 448 fixtures. The analytic claims require checking the common-integral step (18)–(21) and the convergent tails (22)–(23), not fitting a finite second moment. Reproduction instructions, dependency versions, license and result hashes are included in the supplement.

## References

[1] C. David, A. Dunn, A. Hamieh and H. Lin. *Quartic Gauss sums over primes and metaplectic theta functions*. arXiv:2306.11875v5, 2026 (first version 2023). https://arxiv.org/abs/2306.11875v5

[2] A. de Faveri, A. Dunn and J. Hoffstein. *Non-orthogonality of the cubic and quartic large sieves via Rankin–Selberg*. arXiv:2607.07911v2, 2026. https://arxiv.org/abs/2607.07911v2
