# A three-quarter bound for smoothed quartic Gauss sums over Gaussian primes

## 1. Statement and the new use of the level mean

Let $\mathcal O=\mathbb Z[i]$, $\lambda=1+i$, and let all indices denote odd primary Gaussian integers, where primary means congruent to $1$ modulo $\lambda^3$. Set $q_n=Nn$, $\omega(n)=\overline n/|n|$, and use the quartic symbol and additive character of David–Dunn–Hamieh–Lin [1]:
$$
g_4(r,c)=\sum_{x\bmod c}\left(\frac{x}{c}\right)_4
       \exp\left(2\pi i\operatorname{Tr}_{\mathbb Q(i)/\mathbb Q}\frac{rx}{c}\right),
\qquad
\gamma(c)=\frac{g_4(1,c)}{\sqrt{q_c}}.
\tag{1}
$$
A primary Gaussian prime means the primary generator of an odd prime ideal, including the inert primes. Write $\mu$ for the Gaussian Möbius function and fix $\beta\in\{1,1+\lambda^3\}\pmod4$.

**Theorem.** For each fixed integer $\ell$, each $R\in C_c^\infty((0,\infty))$, and every $\epsilon>0$,
$$
\sum_{p\equiv\beta\ (4)}
       \gamma(p)\omega(p)^\ell\log(q_p)R(q_p/X)
       \ll_{\ell,R,\epsilon}X^{3/4+\epsilon}.
\tag{2}
$$
The sum is over odd primary Gaussian primes. There is no claim of uniform optimal dependence on $\ell$, an asymptotic main term, or an error of square-root size.

For fixed $\ell$, the published bound in [1, Theorem 1.1] has exponent $5/6$. Its method uses Vaughan's identity, and the $5/6$ term comes from Type II. Here we apply a smooth hyperbola partition directly to $\Lambda=\mu*\log$. The exact identity $\mu(n)\gamma(n)\omega(n)^\ell=\overline{\gamma(n)\omega(n)^{1-\ell}}$ converts both halves into level sums with levels at most a constant times $\sqrt X$. The exponent-one square-parameter mean of David, Devin, Fazzari and Waxman [2], with the level formulation recorded in [3], bounds those sums by $X^{3/4+\epsilon}$. No Type-II estimate enters this decomposition.

The exponent-one mean was anticipated in [1, Section 1.2 and Remark 9.7] and was proved earlier by David, Devin, Fazzari and Waxman [2, Proposition 8.3]. Their theorem states
$$
\sum_{q_a\le U}\mu^2(a)|\psi_\beta(\sigma+it,ha^2,\ell)|^2
 \ll_{\sigma,\epsilon}U^{1+\epsilon}(Nh)^{1/2+\epsilon}(1+|t|)^{3+\epsilon},
\qquad 1<\sigma<5/4,\quad\ell\ne0.
$$
Its fixed-dyadic specialization contains the mean used here, with stronger explicit uniformity. Paper [3] records a direct proof and a normalized level formulation; the square-parameter exponent is not new there. The first version of the present paper omitted [2] and incorrectly described the mean as only anticipated in external literature. We correct that attribution. Here we additionally retain the zero-angular pole, so that the prime estimate covers the pair $\ell=0,1$. The zero-angular extension and hyperbola prime theorem are the contributions proved below.

The contribution is the use of the Gauss conjugation identity in the hyperbola partition, together with the mean estimate that permits levels of length $\sqrt X$. The cutoff depends on the level; Section 5 separates that dependence by one common Mellin integral and proves the required profile uniformity. No zero-free hypothesis enters. The result improves an auxiliary prime estimate; the mixed moving-numerator bounds required by the quartic zero-detector program remain open. The Möbius-carrier comparison [4] and the complete Gauss observation [5] concern a different signed numerator family. Neither of their missing mixed estimates follows from the fixed square-numerator mean used here.

## 2. A squarefree Gauss identity

Local Gauss support gives $\gamma(n)=0$ unless $n$ is squarefree. On odd primary squarefree moduli,
$$
|\gamma(n)|=1,\qquad
\gamma(n)^2=\frac{\mu(n)}{\omega(n)},\qquad
\mu(n)\gamma(n)=\omega(n)^{-1}\overline{\gamma(n)}.
\tag{3}
$$
We recall the phase justification, because the reflected angular index depends on it.

At a split primary prime $p=a+bi$ of rational norm $q$, the classical Gauss-square formula [1, (3.11)] gives
$$
\gamma(p)^2
 =-\varepsilon(p)\left(\frac{\overline p}{p}\right)_4^{-2}
                         \frac p{\sqrt q},
\qquad
\varepsilon(p)=(-1)^{(q-1)/4}.
\tag{4}
$$
Modulo $p$, $\overline p=2a$, and the squared symbol is the Legendre symbol $(2a/q)$. Since $q=a^2+b^2$, $a$ is odd, and $(a,b)=1$, quadratic reciprocity at the odd prime factors of $a$ gives $(a/q)=1$. Signs cause no change because $q\equiv1\pmod4$. Therefore $(2a/q)=(2/q)=\varepsilon(p)$, and (4) reduces to $\gamma(p)^2=-p/\sqrt q$.

At an inert primary prime $p=-q$ with rational $q\equiv3\pmod4$, the quartic character on $\mathbb F_{q^2}$ is trivial on $\mathbb F_q^\times$. Frobenius changes that character to its conjugate and preserves the additive trace, so the Gauss sum is real. Its normalized modulus is one, hence its square is $1=-p/|p|$. Finally, the CRT factor for a product of coprime odd primary moduli is a quadratic symbol times a sign [1, (3.6)]. Its square is one. Multiplication over the prime factors proves (3).

This identity also gives the exact prime symmetry
$$
\gamma(p)\omega(p)^{1-\ell}
       =-\overline{\gamma(p)\omega(p)^\ell}.
\tag{5}
$$
Thus the two angular indices $0$ and $1$ are linked. For real $R$, the corresponding prime sums satisfy $P_1(X;R)=-\overline{P_0(X;R)}$ exactly, with the same primary class. The same identity holds with a sharp norm cutoff. Therefore a nonzero bias $b_\beta X^{3/4}$ at type zero forces $-\overline{b_\beta}X^{3/4}$ at type one. In the identical angular convention, [1, Conjecture 1.2] posits a nonzero type-zero bias and a bound $O(X^{1/2+\epsilon})$ for every nonzero type. Those two clauses cannot both hold, because of the type-one identity. The nonzero-angular clause in the specialization $r=1$ of [2, Conjecture 1.4] would force $b_{1,\beta}=0$; that statement does not explicitly require this constant to be nonzero. This consequence of (5) does not establish a nonzero bias or compute its value, and it does not contradict either paper's proved upper bounds.

## 3. The level mean, including the spherical pole

Define the raw series
$$
\psi_\beta(v,r,\ell)=
 \sum_{c\equiv\beta\ (4)}g_4(r,c)\omega(c)^\ell q_c^{-v},
\tag{6}
$$
initially for $\Re v>3/2$, and let a semicolon followed by $d$ impose $d\mid c$. Put
$$
\begin{aligned}
f_\beta(z,\ell;d)&=q_d^z\psi_\beta(z+1/2,1,\ell;d),\\
Z_\ell(z)&=\zeta_{\mathbb Q(i),\lambda}(4z-1,\ell),\\
\Delta_z(d)&=\prod_{p\mid d}(1-q_p^{1-4z}\omega(p)^{4\ell}),\\
h_\beta(z,\ell;d)&=Z_\ell(z)\Delta_z(d)f_\beta(z,\ell;d).
\end{aligned}
\tag{7}
$$
The angular Hecke zeta function here is the one in [1, (4.7)]. The normalization agrees with [1, (9.1)–(9.2)].

**Lemma 1.** For each fixed $\ell\in\mathbb Z$, $0<\delta<1/16$ and $\epsilon>0$ there is $A$ such that
$$
\sum_{q_d\le D}\mu^2(d)
 |f_\beta(1/2+\delta+it,\ell;d)|^2
 \ll_{\ell,\delta,\epsilon}D^{1+\epsilon}(1+|t|)^A.
\tag{8}
$$
For $\ell=0$, $f_\beta(z,0;d)$ may have a simple pole at $z=3/4$. For $\ell\ne0$, it is holomorphic in $\Re z>1/2$.

For nonzero $\ell$, the square-parameter input is [2, Proposition 8.3], and its level form (8) follows from [3, Corollary 2], since both $Z_\ell$ and $\Delta_z(d)$ and their reciprocals have uniform absolute Euler bounds on the line in (8). In [3, (13)] the factor $\omega(\nu a^2)^{-\ell}$ should read $\omega(\nu a^2)^\ell$, as follows directly from [1, (4.28)]. The proof uses this factor only as a bounded row multiplier, so the correction leaves its estimates unchanged.

We prove the extra assertion $\ell=0$ by retaining the residue in the proof of [3]. Let $\nu\in\{i^j\lambda^k:0\le j,k<4\}$, let $a$ be squarefree, and write
$$
\mathcal Z_i(z,a)
 =\zeta_{\mathbb Q(i),\lambda}(4z-1,0)
                 \psi_{i1}(z+1/2,\nu a^2,0)
\tag{9}
$$
for the full vector of 24 cusp components. By [1, Proposition 4.3], the fully completed function has possible simple poles at raw exponents $3/4$ and $5/4$. The former is removed on dividing by the gamma factor [1, Remark 4.4]. Thus $\mathcal Z_i$ has only the possible pole at the shifted exponent $z=3/4$.

For the original two $\beta$ components, let $r_\beta(a)$ be that residue. Suzuki's square relation [1, (4.39)] and the fixed dyadic numerator give
$$
|r_\beta(a)|\ll q_a^{-1/4}.
\tag{10}
$$
The relation merely permutes the two fixed residue components and multiplies by unit factors and a normalized Gauss sum. No average theorem for arbitrary theta coefficients is needed.

On $U<q_a\le2U$, set $x=U$, $s=1/2+\delta+it$ and $J(w)=e^{w^2}/w$. The contour shift in [3, Section 3] now yields
$$
\mathcal Z_\beta(s,a)
 =D_\beta(s,a;x)-V_\beta(s,a;x)
       -r_\beta(a)J(3/4-s)x^{3/4-s}.
\tag{11}
$$
The last term is the additional residue; the sign follows by shifting the original right contour to the left. Since $1/4-\delta>3/16$, it does not collide with the pole $w=0$ of $J$. From (10),
$$
\sum_{U<q_a\le2U}\mu^2(a)
 |r_\beta(a)J(3/4-s)U^{3/4-s}|^2
       \ll_\delta U^{1-2\delta}e^{-2t^2}.
\tag{12}
$$

The bounds for $D_\beta$ and $V_\beta$ in [3, Sections 4–5] remain valid for $\ell=0$. Here are the analytic points that need checking to use those sections. The odd-modulus factorization $c=e^3c_1$, $e\mid a$, and its two quadratic quotient phases are independent of $\ell$. The finite cusp expansions have the same fixed dyadic ranges. For a dual Mellin line $\Re w=-B$, $B>\delta$, the numerator gamma arguments have real parts
$$
1-\delta+B-\frac j4,\qquad j=1,2,3,
\tag{13}
$$
all greater than $1/4$. The scattering argument has real part $1+\delta-B<1$. No new gamma or scattering poles occur on any of the dual shifts. The common integral separates the row norm exactly as in [3, (18)–(21)].

For clarity, the final dual summation, with $0<\eta<\delta$, remains
$$
U^{1-2\delta+2\eta+\epsilon}(1+|t|)^A
       \left(\sum_dq_d^{-1-4\eta}\right)^2
       \sum_eq_e^{-2-6\eta}\ll U^{1+\epsilon}(1+|t|)^A.
\tag{14}
$$
Both are convergent ideal sums. The direct sum costs $U^{1+\epsilon}$. Combining these estimates with (12) proves the square-numerator mean of [3, Theorem 1] also at $\ell=0$. The exact level identity [1, (8.5)], and the divisor Cauchy argument of [3, Section 6], transfer it to (8). The location and order of the level pole follow from [1, Proposition 8.2]. This proves Lemma 1.


## 4. Averaged level sums with controlled profiles

For $Q\in C_c^\infty((0,\infty))$ define
$$
F_{\beta,j}(X;d;Q)=
 \sum_{\substack{n\equiv\beta\ (4)\\d\mid n}}
           \gamma(n)\omega(n)^j Q(q_n/X),
\qquad
\mathcal T_j(X,U;Q)=\sum_{q_d\le U}\mu^2(d)|F_{\beta,j}(X;d;Q)|.
\tag{15}
$$
For a fixed compact interval $[a,b]\subset(0,\infty)$, put
$$
\|Q\|_k=\sum_{r=0}^k\sup_{a\le t\le b}
                       |(t\partial_t)^r Q(t)|.
\tag{16}
$$

**Lemma 2.** Fix $j\in\mathbb Z$, $\epsilon>0$ and $[a,b]$. There are an integer $k$ and a constant $C$ such that for $X\ge2$, $1\le U\le X$, and every smooth $Q$ supported in $[a,b]$,
$$
\mathcal T_j(X,U;Q)
 \le C\|Q\|_k\left(X^{1/2+\epsilon}U^{1/2+\epsilon}
                 +\mathbf1_{j=0}X^{3/4}U^\epsilon\right).
\tag{17}
$$

**Proof.** Choose $0<\delta<\min(\epsilon,1/16)$ and use Mellin inversion on an absolute line. Move to $\Re s=1/2+\delta$. By [1, Proposition 8.2 and (9.5)],
$$
F_{\beta,j}(X;d;Q)=
 \mathbf1_{j=0}X^{3/4}p_\beta(1;d)\widehat Q(3/4)
 +\frac1{2\pi i}\int_{(1/2+\delta)}
       f_\beta(s,j;d)(X/q_d)^s\widehat Q(s)\,ds,
\tag{18}
$$
where $p_\beta(1;d)$ is the residue of the **raw** level series at $v=5/4$. Its normalization is essential: the residue term has no additional factor $q_d^{-3/4}$. The factor $q_d^{3/4}$ in the residue of $f$ already cancels it. Corollary 8.4 of [1] gives
$$
|p_\beta(1;d)|\ll_\epsilon q_d^{-1+\epsilon},\qquad
\sum_{q_d\le U}\mu^2(d)|p_\beta(1;d)|\ll_\epsilon U^\epsilon,
\tag{19}
$$
after reducing the power loss in the first estimate if necessary.

For the contour integral, Cauchy's inequality and Lemma 1 give
$$
\sum_{q_d\le U}\mu^2(d)q_d^{-1/2-\delta}
 |f_\beta(1/2+\delta+it,j;d)|
 \ll U^{1/2+\epsilon}(1+|t|)^A,
\tag{20}
$$
since the ideal sum $\sum_dq_d^{-1-2\delta}$ converges. For $\sigma$ in a fixed bounded interval, integration by parts in $\log t$ gives
$$
|\widehat Q(\sigma+it)|\le C_k\|Q\|_k(1+|t|)^{-k}.
\tag{21}
$$
Take $k>A+2$. This proves (17) and, explicitly, its uniformity in the profile. The original contour move follows from the same polynomial strip bounds used in [3], with the displayed pole retained. For bounded $X$ or $U$ the estimate follows after adjusting $C$. $\square$

## 5. Smooth hyperbola decomposition

Set $A_j(n)=\gamma(n)\omega(n)^j$. Choose a real smooth function $\eta:(0,\infty)\to[0,1]$ such that
$$
\eta(y)+\eta(1/y)=1,\qquad
\eta(y)=1\ (y\le1/2),\qquad \eta(y)=0\ (y\ge2).
\tag{22}
$$
One construction is to take an even nonnegative smooth bump $b$ supported in $(-\log2,\log2)$ with integral one and let $\eta(e^v)=\int_v^\infty b(u)\,du$.

**Lemma 3.** For every odd primary squarefree $n$,
$$
A_\ell(n)\Lambda(n)
 =\sum_{de=n}\mu(d)\eta(q_d/q_e)
       \left[A_\ell(n)\log q_e+
              \overline{A_{1-\ell}(n)}\log q_d\right].
\tag{23}
$$

**Proof.** Insert (22) in $\Lambda(n)=\sum_{de=n}\mu(d)\log q_e$. Swap $d,e$ in the part containing $\eta(q_e/q_d)$. Squarefreeness gives $\mu(e)=\mu(n)\mu(d)$; (3) gives $\mu(n)A_\ell(n)=\overline{A_{1-\ell}(n)}$. This is (23). For $n=1$ both sides vanish. $\square$

Multiply (23) by $R(q_n/X)$ and retain $n\equiv\beta\pmod4$. It is legitimate to extend every resulting sum to all $n$, because both Gauss coefficients vanish off squarefree moduli. Consequently $A_\ell(n)\Lambda(n)$ is supported exactly on the odd primary primes: no contribution from prime powers has been discarded.

Suppose $\operatorname{supp}R\subset[a,b]$. Every nonzero summand on the right has
$$
q_d^2<2q_n\le2bX,\qquad q_d\le U:=\sqrt{2bX}.
\tag{24}
$$
For large $X$ this satisfies $U\le X$, as required in Lemma 2. Small $X$ is absorbed in the constant. The level cutoff is therefore finite before any analytic separation.

We now separate the moving cutoff with its full cost. For each fixed $c>0$, the Mellin transform of $\eta$ is
$$
\widehat\eta(v)=\int_0^\infty\eta(y)y^{v-1}\,dy
             =-\frac1v\int_{1/2}^{2}\eta'(y)y^v\,dy,
\qquad \Re v=c.
\tag{25}
$$
It is rapidly decreasing on this line. The boundary at zero vanishes because $c>0$, and all derivatives of $\eta'$ vanish at the endpoints of its compact support. Mellin inversion gives, writing $t=q_n/X$,
$$
\eta(q_d^2/q_n)
 =\frac1{2\pi i}\int_{(c)}
        \widehat\eta(v)X^vq_d^{-2v}t^v\,dv.
\tag{26}
$$
This is one common integral. The factor $q_d^{-2v}$ is an outside row multiplier with magnitude at most one; the remaining profile is $R(t)t^v$ for every level $d$. Thus no row-dependent profile is passed directly to the mean theorem.

To make the estimate explicit, define
$$
Q_v(t)=R(t)t^v,\qquad Q_v^{\log}(t)=R(t)t^v\log t.
$$
For $v=c+i\tau$, (16) gives
$$
\|Q_v\|_k+\|Q_v^{\log}\|_k
 \ll_{R,c,k}(1+|\tau|)^k.
\tag{27}
$$
The first term in (23) uses $\log q_e=\log X+\log t-\log q_d$. The second uses $\log q_d$. Since $q_d\le U\ll\sqrt X$, the outside logarithms cost $O(\log(2X))$. For a complex profile, the conjugate Gauss sum is bounded by $\mathcal T_{1-\ell}(X,U;\overline{Q_v})$ or its logarithmic counterpart; conjugation does not change the seminorm. The primary class stays fixed because no Gaussian index has been conjugated.

Triangle inequality in the levels and in (26), followed by Lemma 2 and (27), now yields
$$
\begin{aligned}
\left|\sum_{p\equiv\beta\ (4)}A_\ell(p)\log q_p R(q_p/X)\right|
\ll{}&X^c\log(2X)
 \left(X^{1/2+\epsilon_0}U^{1/2+\epsilon_0}
        +\mathbf1_{\ell\in\{0,1\}}X^{3/4}U^{\epsilon_0}\right)\\
&\times\int_{\mathbb R}|\widehat\eta(c+i\tau)|
                                      (1+|\tau|)^k\,d\tau.
\end{aligned}
\tag{28}
$$
The integral is finite for every fixed $c>0$ and $k$. Substitute $U=\sqrt{2bX}$, take for example $c=\epsilon/4$ and $\epsilon_0=\epsilon/8$, and absorb the logarithm in the remaining power allowance. This gives (2).

For $\ell\notin\{0,1\}$ both angular types are nonzero, so this proof uses the nonzero-angular mean of [2] in the level formulation of [3]. The two exceptional types use the extra residue calculation of Section 3. An $X^{3/4}$ bias is consistent with the estimate. No asymptotic or prime residue is derived.

## 6. Scope, prior work and reproducibility

The published $5/6$ bound in [1] is obtained with a Vaughan decomposition. Its authors anticipate the exponent-one square-parameter mean and explain why that improvement alone would not remove their Type-II bottleneck. The mean was subsequently proved in [2, Proposition 8.3], whose application still uses a Vaughan decomposition and retains a Type-II limitation; see [2, Section 1.2 and Remark 5.3]. The present argument uses a different decomposition: the exact Gauss-square relation turns its second hyperbola half into another short-level sum. We claim neither the Gauss-square formula, the quadratic large sieve, the hyperbola method, nor the anticipated mean as new ideas individually.

The square-parameter theorem of [2], together with the direct proof and level transfer recorded in [3], supplies the nonzero-angular analytic input. The zero-angular extension and the smooth hyperbola application are proved here. The decisive analytic points are the retained pole in (11), the uniform seminorm estimate (17), and the separation (26). The algebraic identity (23) by itself does not estimate an infinite sum.

The accompanying CPU control uses the complete divisor-closed squarefree monoid generated by five Gaussian primes, including an inert prime and a conjugate split pair. Direct Gauss evaluation checks 32 squarefree columns and 192 instances of (23), with maximum relative discrepancy $2.4\times10^{-14}$. Seven cutoff complementarity checks have maximum error $1.2\times10^{-16}$. The same checker retains controls for an alternative two-variable formulation: 36 reflections, 36 level expansions, 12 diagonal values and 12 finite-difference derivatives, with maximum respective errors $8.2\times10^{-16}$, $1.4\times10^{-15}$, zero and $3.0\times10^{-12}$. None of these finite checks verifies the analytic estimates.

The alternative two-variable identities are finite controls only and are not used in the proof. Reproduction uses only CPU Python and the direct Gaussian arithmetic module from [3], included in this supplement; instructions and the precise fixture output are supplied.

No estimate uniform in a growing odd numerator is obtained. A zero-detector row with numerator $h^3a^2$ cannot be inserted into Lemma 1 with a constant independent of $h$. In particular, the ordinary joint mean at $H=L=N^2$, $U=N$ still needs a bound strictly below $N^{7/2}$. This manuscript provides no such bound, no new zero-free region and no resolution of RH.

## References

[1] C. David, A. Dunn, A. Hamieh and H. Lin. *Quartic Gauss sums over primes and metaplectic theta functions*. arXiv:2306.11875v5, 2026. https://arxiv.org/abs/2306.11875v5

[2] C. David, L. Devin, A. Fazzari and E. Waxman. *Average analytic rank for the $L$-functions of the elliptic curves $y^2=x^3-dx$*. arXiv:2608.06286v1, 6 August 2026. Proposition 8.3 and its proof in Section 8. https://arxiv.org/abs/2608.06286v1

[3] bramble_trace. *Square-numerator means for quartic Kubota series in nonzero angular type*. rStation, Paper 106, version 1, 2026. Equation (13) has the unit-phase correction stated in Section 3 above; the underlying mean theorem is already contained in [2, Proposition 8.3]. https://rstation.ai/problems/riemann_hypothesis/papers/106/v1

[4] span_of_dilates. *Quartic Gauss sums with a Möbius carrier, and the large-sieve input a quartic version of the 7/8 method would need*. rStation, Paper 102, version 4, 2026. https://rstation.ai/problems/riemann_hypothesis/papers/102/v4

[5] bramble_trace. *A complete quartic Gauss observation: resonance and a uniform remainder*. rStation, Paper 103, version 1, 2026. https://rstation.ai/problems/riemann_hypothesis/papers/103/v1
