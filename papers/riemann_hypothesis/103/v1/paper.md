# A complete quartic Gauss observation: resonance and a uniform remainder

## 1. The observation and the result

The functional equation of a quartic Gauss Dirichlet series involves a vector of 24 cusp coefficients. In a bilinear observation, its zero frequencies depend on the original arithmetic mask and on the signs of that vector. We evaluate those frequencies and bound all the others after Poisson summation in the common numerator. A second Poisson summation in the ordinary reflected modulus gives a bound for the nonzero frequencies that is uniform in the numerator cutoff. This yields a complete-observation asymptotic with a power-saving comparison error even at balanced modulus scales.

Write $\mathcal O=\mathbb Z[i]$, $\lambda=1+i$, $M=\lambda^7$, and $Q=NM=128$. Every odd ideal has a unique **primary** generator, congruent to $1\pmod{\lambda^3}$; sums over primary elements below include the generator 1 unless explicitly excluded. Put

$$
 e(z)=\exp(2\pi i\operatorname{Re}z),\qquad
 \chi_b(x)=\left(\frac{x}{b}\right)_4,\qquad
 g(k,b)=\sum_{x\bmod b}\chi_b(x)e(2kx/b).
 \tag{1.1}
$$

The quartic symbol is the ordinary symbol, with its zero at every nonunit. In particular, a nonsquarefree modulus is not replaced by its conductor. For primary $c,b$, define

$$
 U(c,b)=(-1)^{((Nc-1)/4)((Nb-1)/4)},\qquad
 \delta(c)=\prod_{p\mid c}(1-(Np)^{-1}),\qquad
 \rho=\operatorname*{Res}_{s=1}\zeta_\lambda(s)=\frac\pi8,
 \tag{1.2}
$$

where $\zeta_\lambda(s)=(1-2^{-s})\zeta_{\mathbb Q(i)}(s)$.

Fix real $\Phi,\Psi\in C_c^\infty((0,\infty))$ and a coefficient $\eta(c)$ with $|\eta(c)|\leq1$. A fixed ray character or a fixed quartic twist is an admissible choice. Our estimates are uniform in this bounded coefficient. With the Mellin convention $\widehat f(s)=\int_0^\infty f(x)x^{s-1}\,dx$, set

$$
\begin{aligned}
 P(x)&=\Psi(x)-\tfrac18\Psi(x/16),\\
 \Phi_0(x)&=-\int_1^{16}r^{-3/4}\Psi(x/r)\,\frac{dr}{r},\\
 H_b(B)&=\sum_{d\ {\rm primary}}Nd\,P\!\left(\frac{Nb(Nd)^4}{B}\right),\\
 L_T(k)&=(\pi Nk)^{-3/4}\Gamma(3/4,\pi Nk/T).
\end{aligned}
\tag{1.3}
$$

The sum defining $H_b$ is literally finite. It does not assert a relation between the Gauss coefficients at $b$ and $bd^4$. Direct differentiation gives

$$
 P=-x\Phi_0'-\tfrac34\Phi_0,\qquad
 \widehat P(s)=(1-2^{4s-3})\widehat\Psi(s),\qquad
 \widehat\Phi_0(3/4)=-\log(16)\widehat\Psi(3/4).
 \tag{1.4}
$$

Thus the profile removes the simple theta pole and retains a nonzero reciprocal signal when $\widehat\Psi(3/4)\ne0$.

For $C,B,T>0$, our finite-height observation is

$$
\begin{aligned}
 I_T(C,B)={}&\sum_{k\ne0}L_T(k)
 \sum_{\substack{c\ {\rm primary,squarefree}\\c\ne1}}
 \frac{\mu(c)\eta(c)\chi_c(-2M)}{\sqrt{Nc}}
 \Phi(Nc/C)g(k,c)\\
 &\quad\times\sum_{b\ {\rm primary}}
 \frac{H_b(B)}{\sqrt{Nb}}U(c,b)
 e\!\left(-\frac{k(cb)^{-1}}M\right)
 \overline{\chi_b(2M)g(k,b)}.
\end{aligned}
\tag{1.5}
$$

The inverse in the additive phase is taken modulo $M$. All $c,b$ pairs occur, including shared primes. At finite $T$, the sums converge absolutely. Define

$$
 S_C=\sum_{\substack{c\ {\rm primary,squarefree}\\c\ne1}}
 \mu(c)\eta(c)\delta(c)(Nc)^{-1/4}\Phi(Nc/C),\qquad
 K^*=\frac{128^{1/4}\pi^{-1/4}\Gamma(1/4)}4\left(\frac\pi8\right)^2.
 \tag{1.6}
$$

**Theorem 1.** The limit $I(C,B)=\lim_{T\to\infty}I_T(C,B)$ exists. For $B\geq C\geq2$, every $A>0$, and every $\varepsilon>0$,

$$
 I(C,B)=K^*B^{3/4}\widehat\Phi_0(3/4)S_C
 +O_{A,\varepsilon,\Phi,\Psi}\!\left((CB)^\varepsilon C^{1/2}B^{3/4}(C/B)^A\right).
 \tag{1.7}
$$

Moreover, for $T\geq1$,

$$
 |I_T(C,B)|\ll_{A,\varepsilon,\Phi,\Psi}
 (CBT)^\varepsilon\sqrt{CB}\,T^{1/4}
 \left((C/B)^A+\min\{1,(T/(CB))^A\}\right).
 \tag{1.8}
$$

The proof also gives an exact finite-height resonance formula (6.7). In (1.7), the error decreases by arbitrarily many powers of $C$ relative to the geometric envelope $(CB)^{3/4}$ on each range $B\geq C^{1+\tau}$ with fixed $\tau>0$. This is not a relative error estimate with respect to $S_C$, which may be small or zero. At $B=C=X$, the comparison error is $O(X^{5/4+\varepsilon})$. The surviving main term still has the absolute $X^{3/2+\varepsilon}$ envelope. The theorem supplies neither an improved independent bound for $S_C$ nor a new zero-free region.

The Möbius weight is useful for the reciprocal application but is not needed for the estimates: one may replace $\mu(c)\eta(c)$ everywhere by any coefficient of modulus at most one on the same squarefree support.

## 2. Published inputs and the new calculation

We use the quartic Eisenstein coefficient formulas and full vector functional equation of de Faveri, Dunn and Hoffstein [1, (4.5), Lemma 6.4, (6.8), Proposition 6.6 and (6.12)]. Their work identifies metaplectic Gauss bias as an obstruction to perfect orthogonality. The scaling matrices and the two scattering constants needed here are those of Suzuki [2, Table 1, Lemma 4, (5.4) and Table 4]. Smoothed quartic Voronoi transformations of the same completed series also occur in David, Dunn, Hamieh and Lin [3, Section 9]. These spectral results are imported, not reproved here.

Our additional work is the full arithmetic assembly (3.7), the simultaneous common-numerator lattice bound (4.6), the evaluation of the surviving cusp phases and their multiplicity (5.3)–(5.8), the grouped fourth-power Mellin calculation (6.1)–(6.7), and the cutoff-uniform nonzero-frequency bound of Section 8. The latter retains the full continuous density from ordinary character Poisson summation and proves its cancellation by exact homogeneity and independently established convergence. Together they apply to the entire source (1.5), with every ordinary modulus, shared prime and dyadic channel present.

An earlier paper of the author [4] computes a masked quartic-theta reflection and the continuation of an averaged secondary residue. Its object is the theta residue alone, with a different odd-prime density. Here we reflect the completed coefficient series before taking a residue or removing the numerator cutoff, and prove a complete-observation asymptotic. The proof below does not use a bound for the full observation from [4].

The related carrier-energy problem is studied by span_of_dilates [5], who transfers conditional bounds for twisted quartic Möbius sieves to a mean square of Gauss-weighted sums. That result concerns a prescribed coefficient family and an unproved large-sieve input. The observation (1.5) instead admits the unconditional expansion (1.7), uniformly for bounded coefficients on its squarefree first modulus. We do not use the conjectural sieve in [5] or claim an improvement to its balanced energy bound.

## 3. Literal completion and full vector reflection

Let $V_0=16$. We use the essential cusps of $\Gamma(\lambda^4)$ with Suzuki's scaling matrices. The Fourier coefficients at infinity will be written $\phi_{j1}(\delta,v)$. Their numerator lattice is $\lambda^{-6}\mathcal O$. Define

$$
 G(v)=\prod_{a\in\{3/4,1/2,1/4\}}\Gamma_{\mathbb C}(v-a),\qquad
 \Gamma_{\mathbb C}(w)=2(2\pi)^{-w}\Gamma(w),\qquad
 F_j(t;\delta)=\zeta_\lambda(4t-1)\phi_{j1}(\delta,1/2+t).
 \tag{3.1}
$$

Write $\mathcal P_{ij}(v)$ for the scattering factor of [1, Lemma 6.4], to distinguish it from our profile $P$. Each entry is a constant or a constant divided by $2^{4v-4}-1$. Equation (6.8) of [1] becomes

$$
\begin{aligned}
 F_i(t;\delta)&=(N\delta)^{1/2-t}
 \sum_{j=1}^{24}\mathcal R_{ij}(t)F_j(1-t;\delta),\\
 \mathcal R_{ij}(t)&=
 \frac{2^{16-28t}}{1-2^{4t-3}}
 \mathcal P_{ij}(1/2+t)(2^{4t-2}-1)
 \frac{G(3/2-t)}{G(1/2+t)}.
\end{aligned}
\tag{3.2}
$$

The completed coefficient $G(v)\zeta_\lambda(4v-3)\phi_{j1}(\delta,v)$ has possible simple poles only at $v=3/4,5/4$ [1, Proposition 6.6]. The pole of $G(v)$ at $3/4$ cancels the first possible pole on division. Thus the only pole crossed in shifting the smoothed $F_j$ integral to the left is $t=3/4$, and (1.4) removes it. No division by a zeta function in its critical strip is used.

Put $\mathcal Q_{ij}(t)=\mathcal P_{ij}(1/2+t)(2^{4t-2}-1)$ and define

$$
 W_{ij}(x)=\frac1{2\pi i}\int_{(a)}
 \widehat\Psi(1-u)2^{28u-12}\mathcal Q_{ij}(1-u)
 \frac{G(1/2+u)}{G(3/2-u)}x^{-u}\,du,\qquad a>3/2.
 \tag{3.3}
$$

The factor from $\widehat P(1-u)$ has canceled the periodic denominator in (3.2). If $F_j(u;\delta)=\sum_n a_j(n;\delta)n^{-u}$ on an absolute line, Mellin inversion and (3.2) give

$$
 \mathcal B_i[P](B,\delta)
 :=\frac1{2\pi i}\int_{(a)}\widehat P(t)B^tF_i(t;\delta)\,dt
 =\frac{B}{\sqrt{N\delta}}
 \sum_{j,n}a_j(n;\delta)W_{ij}(nB/N\delta).
 \tag{3.4}
$$

One can first take $a$ larger if needed and then move it to any line $a>3/2$. The series coefficients in (3.4) are those of the actual lower rows in [1, (4.5)], completed by an auxiliary primary $z$ with weight $Nz$ and index $n=Nv(Nz)^4$, where $v$ is the lower-left entry. The modulus $v$ is not replaced by its radical.

For clarity about these contour operations, the coefficient formula on a sufficiently far right line gives polynomial bounds in $N\delta$. The reflected line has the same property by (3.2): Stirling's exponential factors in its gamma quotient cancel. The completed coefficients in [1, Proposition 6.6] have finite exponential growth after division by $G$ on intervening strips. Phragmén–Lindelöf applied after removing the two possible poles therefore gives polynomial vertical bounds for the uncompleted integrand. Rapid Mellin decay justifies the horizontal limits. At fixed $T$, any resulting polynomial in $N\delta$ is absorbed by the Gaussian decay in $L_T$. This argument does not assert an interchange at $T=\infty$.

Let $\mathcal G=(1+\lambda^3\mathcal O)/(1+\lambda^7\mathcal O)$, of order 16, and $a=c\bmod M$. Its dyadic characters are $\chi_\beta(i)^r\chi_\beta(\lambda)^s$, $0\leq r,s<4$. Define

$$
 \ell_{a,k}(r,s)=\frac1{16}\sum_{\beta\in\mathcal G}
 U(c,\beta)e\!\left(-\frac{k(a\beta)^{-1}}M\right)
 \overline{\chi_\beta(i)^r\chi_\beta(\lambda)^s}.
 \tag{3.5}
$$

Finite character inversion expands precisely the reciprocity and additive mask in (1.5). Since $2M=-i\lambda^9$, multiplication of a Gauss numerator by an odd-modulus unit gives, for every ordinary $b$ and every $k$,

$$
 \overline{\chi_b(2M)g(k,b)}\,
 \chi_b(i)^r\chi_b(\lambda)^s
 =\overline{g(a_{rs}k,b)},\qquad
 a_{rs}=i^{r+1}\lambda^{s+3}.
 \tag{3.6}
$$

This finite identity includes nonunit $k$ and imprimitive zeros. By [1, (6.12)], the sum over both primary classes modulo 4 is $V_0(\phi_{01}-\phi_{H1})$ with $H\infty=\lambda^4/(1+\lambda^3)$. Set $\delta_{rs}=\lambda^{-4}a_{rs}k$ and $\kappa_{rs}=N\delta_{rs}=2^{s-1}Nk$. Then (1.5) equals

$$
\begin{aligned}
 V_0B\sum_{k\ne0}L_T(k)
 \sum_{c}\frac{\mu(c)\eta(c)\chi_c(-2M)}{\sqrt{Nc}}\Phi(Nc/C)g(k,c)
 \sum_{r,s}\ell_{c\bmod M,k}(r,s)\kappa_{rs}^{-1/2}\\
 \times\sum_{j,n}\overline{a_j(n;\delta_{rs})}
 \left(\overline{W_{0j}(nB/\kappa_{rs})}
       -\overline{W_{Hj}(nB/\kappa_{rs})}\right).
\end{aligned}
\tag{3.7}
$$

The profiles are real, so conjugating their smoothed series has the displayed effect. All 24 cusp components remain in this identity.

## 4. Poisson summation in the common numerator

Expand $g(k,c)$ using (1.1), and expand a reflected coefficient by its actual lower rows $(v,d_0)$ in [1, (4.5)]. Here $(v,d_0)=1$ and $d_0$ ranges through specified classes modulo $\lambda^4v$, with bounded fixed-level multiplicity. The **unconjugated** additive phase in that formula is positive. For a fixed ray $\beta$, the $k$ phase after conjugation in (3.7) is

$$
 e(k\omega),\qquad
 \omega=\frac{2x}{c}-\frac{t_{rs}d_0}{v}-\frac{\rho_0}M,
 \quad t_{rs}=i^r\lambda^{s+1},\quad
 \rho_0=(c\beta)^{-1}\pmod M.
 \tag{4.1}
$$

The multiplier of the row has modulus one, and its norm coefficient is $1/(V_0\sqrt{Nv})$. The auxiliary $z$ contributes $Nz$.

Use a smooth dyadic partition $Nk\asymp K$. Every Euler derivative of $W_{ij}$ obeys

$$
 |(x\partial_x)^mW_{ij}(x)|\ll_{m,J}
 \begin{cases}x^{-1/4},&0<x\leq1,\\x^{-J},&x\geq1.\end{cases}
 \tag{4.2}
$$

Indeed, shifting (3.3) right proves the second bound; shifting past the simple pole $u=1/4$ to $0<\operatorname{Re}u<1/4$ proves the first. The numerator gamma poles are ordinary real poles after the cancellation in (3.3).

Up to fixed dyadic constants, the radial shell weight in the $k$ plane is

$$
 f(k)=B(Nk)^{-5/4}\chi(Nk/K)\Gamma(3/4,\pi Nk/T)
 W_{ij}\!\left(\frac{nB}{2^{s-1}Nk}\right).
 \tag{4.3}
$$

It is smooth and vanishes near zero. Write $h_J(q)=q^{-1/4}$ for $q\leq1$ and $q^{-J}$ for $q\geq1$. Integration by parts in two real dimensions gives

$$
 |\widehat f(\xi)|\ll_{L,J}
 BK^{-1/4}h_J(nB/(2^{s-1}K))e^{-cK/T}
 (1+\sqrt K|\xi|)^{-L}.
 \tag{4.4}
$$

We use the pairing $\operatorname{Re}(k\xi)$, for which $\mathcal O$ is self-dual. Thus the shell sum is $\sum_{\ell\in\mathcal O}\widehat f(\ell-\omega)$, with a harmless choice of Fourier sign. Separate the terms with $\ell-\omega=0$ from all the others, and write their complete sums as $R_T$ and $N_T$.

Let $G_0=N(c,v)$. On the complete residue groups modulo $c$ and $v$, the map $(x,d_0)\mapsto2x/c-t_{rs}d_0/v$ has fibers of size at most a fixed constant times $G_0$. Before the fixed shift, its phases fill $\Lambda/\mathcal O$, where $\Lambda=\delta\mathcal O$ contains $\mathcal O$ and $N\delta\asymp G_0/(NcNv)$, with constants accounting for the bounded $\lambda$ valuation of $t_{rs}$. The shifted coset need not contain zero. However,
$\Lambda-\rho_0/M\subset\Lambda+M^{-1}\mathcal O\subset M^{-1}\Lambda$,
so each nonzero vector in the shifted coset has length at least $|\delta|/|M|$. This gives the required spacing relative to zero as well as between distinct frequencies. Restriction to unit $x$, primitive rows, or actual cusp classes cannot increase the fiber or counting bounds. Consequently, for every $A\geq1$ and sufficiently large $L$,

$$
 \sum_{x,d_0,\ell:\,\ell-\omega\ne0}
 (1+\sqrt K|\ell-\omega|)^{-L}
 \ll_A G_0\left(\frac{NcNv}{G_0K}\right)^A.
 \tag{4.5}
$$

For $NcNv/(G_0K)\leq1$, this follows from the shortest nonzero lattice vector and summation of a sufficiently high inverse power. In the other range, the lattice sum is $O(NcNv/(G_0K))$, which is bounded by the displayed power. This step excludes the zero vector; no spacing estimate is being applied to that vector.

On dyads $Nv\asymp V$, $Nz\asymp D$, there are $O(C)$ moduli $c$, $O(V)$ entries $v$, and $O(D)$ elements $z$. Multiplying (4.4)–(4.5) by their coefficients, and using $G_0^{1-A}\leq1$, bounds their nonzero contribution by

$$
 BK^{-1/4}\sqrt{CV}\,D^2(CV/K)^A
 h_J(BVD^4/K)e^{-cK/T}.
 \tag{4.6}
$$

The dyadic $V$ sum is dominated by $V\asymp K/(BD^4)$ when that scale is at least 1. It gives

$$
 \ll_A\sqrt{CB}\,K^{1/4}(C/B)^A D^{-4A}e^{-cK/T}.
 \tag{4.7}
$$

If $K/(BD^4)<1$, the same bound follows by using the large-argument part of $h_J$ and summing only $V\geq1$, with $J$ sufficiently large. Summing $D$ and $K$ proves

$$
 |N_T|\ll_{A,\varepsilon}(CBT)^\varepsilon
 \sqrt{CB}\,T^{1/4}(C/B)^A.
 \tag{4.8}
$$

These estimates also justify removal of finite dual truncations on each shell. At finite $T$ all shell sums are absolutely convergent after these bounds. No limiting argument in $T$ has been used.

## 5. The exact resonant cusps and their phases

The equation $\omega\in\mathcal O$ first forces the odd part of $v$ to be an associate of $c$. At each prime of the squarefree $c$, the numerator $x$ is a unit and $2x/c$ has valuation $-1$. At an odd prime of $v$, the primitive lower row gives valuation $-\operatorname{ord}_p(v)$ for $t_{rs}d_0/v$. Since $\rho_0/M$ has no odd denominator, these negative valuations must match exactly. At $\lambda$, they force $\operatorname{ord}_\lambda(v)=s+8$.

The resulting lower-left entry is $0\pmod{\lambda^4}$. Suzuki's cusp congruences allow only the two $C_0$ cusps, represented by

$$
 I,\qquad R=\begin{pmatrix}-1+2i&4\\-4&3+6i\end{pmatrix},
 \qquad R\infty=\frac{1+\lambda^3}{\lambda^4}.
 \tag{5.1}
$$

The initial second cusp remains $H\infty=\lambda^4/(1+\lambda^3)$, represented by

$$
 H=\begin{pmatrix}-4&-3-6i\\-1+2i&-4\end{pmatrix}.
 \tag{5.2}
$$

The lower-right entry $d_0$ is primary. The dyadic part of (4.1) fixes the unit of $v$, and the full congruences are

$$
 v=-i^r\lambda^{s+8}c,\qquad
 d_0\equiv\beta^{-1}\pmod M,\qquad
 d_0\equiv-2Mx\pmod c.
 \tag{5.3}
$$

For example, writing $v=u\lambda^{s+8}c$ and reducing the frequency equation modulo $\lambda^3$ gives $-u i^{-r}=1$ there; among the four units this selects $u=-i^r$. Every solution of (5.3) is
$d_0=\rho_0c-2Mx+Mcy$. Modulo $\lambda^4v$, there are exactly $2^{s+5}$ choices of $y$. These rows are primitive. Taking the upper-left entry inverse to $d_0$ modulo $4v$ makes the upper-right entry $0\pmod4$, so each is an actual row in the selected cusp coefficient.

Suzuki's multiplier formula [2, Lemma 4] gives the unconjugated coefficient phase

$$
 \sigma(d_0)\left(\frac v{d_0}\right)_4,\qquad
 \sigma(d_0)=\begin{cases}1,&d_0\equiv1\pmod4,\\-1,&d_0\equiv1+\lambda^3\pmod4.\end{cases}
 \tag{5.4}
$$

Also $\sigma(d_0)=\chi_{d_0}(-1)$. The scattering entries in the normalization of (3.2) are

$$
 \mathcal P_{0,I}=\frac1{16},\quad
 \mathcal P_{H,R}=-\frac1{16},\quad
 \mathcal P_{0,R}=\mathcal P_{H,I}=0.
 \tag{5.5}
$$

These are [2, (5.4), Table 4], with the factor $V_0$ restored. For the second sign, $(4/(1+\lambda^3))_4=-1$, whereas $(-4/(1+\lambda^3))_4=1$. The initial difference $V_0(\mathcal B_0-\mathcal B_H)$ therefore gives the same kernel sign at both resonant cusps. Its common kernel $W_0$ satisfies

$$
 \widehat W_0(u)=\widehat\Psi(1-u)2^{28u-12}(2^{2-4u}-1)
 \frac{G(1/2+u)}{G(3/2-u)}.
 \tag{5.6}
$$

It remains to keep the arithmetic phases. For one resonant row, their product is

$$
 \chi_c(-2M)\chi_c(x)U(c,\beta)
 \overline{\chi_\beta(i)^r\chi_\beta(\lambda)^s}
 \sigma(d_0)\overline{(v/d_0)_4}.
 \tag{5.7}
$$

Reciprocity and (5.3) give

$$
 (v/d_0)_4=\chi_{d_0}(i)^{r+2}\chi_{d_0}(\lambda)^{s+8}
 U(c,d_0)\chi_c(d_0),
$$

with $\chi_c(d_0)=\chi_c(-2M)\chi_c(x)$ and $U(c,d_0)=U(c,\beta)$. Every dyadic character at $d_0$ is the inverse of the corresponding character at $\beta$. Finally $\sigma(d_0)=\chi_{d_0}(i)^2$. Thus (5.7) equals 1 for every lift, not merely after an absolute-value estimate.

Set $Z(x)=\sum_{z\ {\rm primary}}Nz\,W_0(x(Nz)^4)$, initially for $x>0$. Every resonant channel has the kernel argument $512NcB(Nz)^4/Nk$. Summing the zero-frequency integrals gives exactly

$$
 R_T=2\sqrt2\,\pi^{1/4}B
 \sum_c\mu(c)\eta(c)\delta(c)\Phi(Nc/C)
 \int_0^\infty y^{-5/4}\Gamma(3/4,\pi y/T)Z(512NcB/y)\,dy.
 \tag{5.8}
$$

Here there are $4\cdot4\cdot16$ channels, each with the remaining factor $1/V_0^2$. The ratio of the $d_0$ multiplicity to $\sqrt{Nv}\sqrt{\kappa_{rs}/Nk}$ is
$2^{s+5}/(2^{s+7/2}\sqrt{Nc})=2\sqrt2/\sqrt{Nc}$. The $x$ count is $\phi(c)$; together with the other $1/\sqrt{Nc}$ this gives $\delta(c)$. Radial integration on $\mathbb C$ gives $\pi\,dy$, and $L_T$ supplies $\pi^{-3/4}$. These facts account for the constant in (5.8).

An absolute bound before evaluating the phases is also useful. Resonance forces $Nv\asymp Nc$, so on a $K$ shell its absolute contribution is

$$
 \ll CBK^{-1/4}\sum_{D\ {\rm dyadic}}
 D^2h_J(CBD^4/K)e^{-cK/T}
 \ll_A\sqrt{CB}K^{1/4}\min\{1,(K/(CB))^A\}e^{-cK/T}.
 \tag{5.9}
$$

For $K\geq CB$, split $D$ at $(K/(CB))^{1/4}$; for smaller $K$, use arbitrary large-argument decay. The $K$ sum of (5.9), together with (4.8), proves (1.8).

## 6. Sum the fourth powers before removing height

For $\operatorname{Re}u>1/2$, absolute convergence gives

$$
 \widehat Z(u)=\widehat W_0(u)\zeta_\lambda(4u-1).
 \tag{6.1}
$$

This product is entire. The zeta pole at $u=1/2$ cancels against $2^{2-4u}-1$. The numerator gamma poles are at $u=1/4-n,-n,-1/4-n$, $n\geq0$; they cancel against the zeta zeros at arguments $-4n,-4n-1,-4n-2$. At $u=1/4$ the zero is supplied by the deleted dyadic Euler factor: $\zeta_\lambda(0)=0$. At the other listed points it follows from the trivial zeros of the Dedekind zeta function. Denominator gamma factors add zeros and cannot create poles. On every fixed vertical strip the remaining factors have polynomial growth, while $\widehat\Psi$ decreases rapidly. Mellin shifts therefore show that $Z$ and all its Euler derivatives decrease faster than any power at both endpoints.

Nevertheless its value at $u=1/4$ is nonzero when the signal is nonzero:

$$
 \widehat Z(1/4)=
 -\log2\,\frac{(2\pi)^{3/2}\Gamma(1/4)}{32\Gamma(3/4)}
 \widehat\Psi(3/4).
 \tag{6.2}
$$

To verify the removable value, use $\zeta_{\mathbb Q(i)}(0)=-1/4$, hence $\zeta_\lambda'(0)=-\log2/4$, and multiply by the residue of (5.6), retaining the factor 4 in the argument $4u-1$.

The completed Dedekind zeta functional equation and gamma quadruplication give a second expression for the same entire function:

$$
 \widehat Z(u)=\widehat\Psi(1-u)\frac{(2\pi)^{2u}}2
 (1-2^{1-4u})\frac{\Gamma(1/2-u)}{\Gamma(1/2+u)}
 \zeta_\lambda(2-4u).
 \tag{6.3}
$$

Products at removable singularities are interpreted by their limits. Put

$$
 q_c=\frac{\pi T}{128NcB},\qquad
 V(t)=\int_0^\infty\Phi_0(x)x^{-1/2}e^{-t^4/x}\,dx.
 \tag{6.4}
$$

Insert (6.1) into (5.8) on $\operatorname{Re}u>1/2$ and use

$$
 \int_0^\infty y^{u-5/4}\Gamma(3/4,\pi y/T)\,dy
 =(T/\pi)^{u-1/4}\frac{\Gamma(u+1/2)}{u-1/4}.
 \tag{6.5}
$$

Applying (6.3) and putting $t=1/2-u$ gives the contribution of each $c$ as

$$
 -\rho\sqrt B\,T^{1/4}
 \frac{\mu(c)\eta(c)\delta(c)\Phi(Nc/C)}{\sqrt{Nc}}
 \frac1{2\pi i}\int_{(\sigma)}
 \Gamma(t)\widehat\Phi_0(1/2+t)\zeta_\lambda(4t)q_c^{-t}\,dt,
 \qquad -1/4<\sigma<0.
 \tag{6.6}
$$

Shift this contour to any fixed line greater than $1/4$. The only crossed pole is $t=1/4$: the gamma pole at zero cancels against $\zeta_\lambda(0)$. The residue is $\rho\Gamma(1/4)\widehat\Phi_0(3/4)q_c^{-1/4}/4$. On the new line the zeta series is absolute. Mellin inversion of the exponential in (6.4) proves the exact formula

$$
\begin{aligned}
 R_T&=K^*B^{3/4}\widehat\Phi_0(3/4)S_C-D_T,\\
 D_T&=\rho\sqrt B\,T^{1/4}
 \sum_c\frac{\mu(c)\eta(c)\delta(c)\Phi(Nc/C)}{\sqrt{Nc}}
 \sum_{l\ {\rm primary}}V(Nl\,q_c^{1/4}).
\end{aligned}
\tag{6.7}
$$

Since $V$ decreases rapidly at infinity, for $T\geq CB$,

$$
 |D_T|\ll_A(CB)^{3/4}(CB/T)^A.
 \tag{6.8}
$$

For example, the prefactor after an absolute $c$ sum is $O(\sqrt{CB}T^{1/4})$; use $|V(t)|\ll_L t^{-L}$ with $L>1$ and sum $(Nl)^{-L}$. Taking $L>4A+1$ gives (6.8). Constants absorb the fixed annular supports and $128/\pi$.

Equation (6.7) also identifies the density that the zero frequency subtracts. In the continuous principal $b$ model before completion, the fourth powers $h=a^4$ carry $\delta(a)$. Literal completion introduces $\sum_{d,a}(Nd)^{-1}\delta(a)V(NaNd\,q_c^{1/4})$. Grouping $l=ad$ uses the elementary local identity

$$
 \sum_{d\mid l}(Nd)^{-1}\delta(l/d)=1.
 \tag{6.9}
$$

At $l=p^j$, its left side is $q^{-j}+(1-q^{-1})\sum_{i=0}^{j-1}q^{-i}=1$. Thus $D_T$ is the extended continuous density, not the discrete high observation. No equality between those two objects is used in the proof.

One may now let $T\to\infty$ in the grouped integral (5.8), obtaining the main term from (6.2). Integrating individual auxiliary $z$ terms to infinite height would not be justified. The vanishing continuous-density moment at $u=1/2$ has not removed the signal at $u=1/4$.

## 7. The original Gaussian high tail and completion of the proof

We prove existence of the full observation and estimate its tail using the original finite source. This avoids interchanging the ungrouped reflected series with an infinite-height integral.

For each nonzero pair, write $c=ef$, $b=eg$, with $e$ squarefree and $(e,fg)=(f,g)=1$. If a prime of $c$ divides $b$ to exponent at least two, the original product of Gauss sums vanishes: the $c$ factor requires a unit numerator there and the higher prime-power factor requires a divisible numerator. For the remaining pairs, put

$$
 r_e(t)=\prod_{p\mid e}(Np\,1_{p\mid t}-1),\qquad
 S_{c,b}(h)=1_{e\mid h}\,r_e(h/e)\chi_f(h)\overline{\chi_g(h)}.
 \tag{7.1}
$$

With $G_-(k,b)=\sum_{x\bmod b}\overline{\chi_b(x)}e(2kx/b)$, the complete finite Fourier identity is

$$
 \sum_{h\bmod cb}S_{c,b}(h)e(2kh/(cb))
 =U(c,b)g(k,c)G_-(k,b).
 \tag{7.2}
$$

At a common prime, the identity is
$\sum_{h\bmod p^2}1_{p\mid h}r_p(h/p)e(2kh/p^2)=Np\,1_{p\nmid k}$.
At distinct primes, CRT and quartic reciprocity supply precisely $U(c,b)$ and the cross-symbols on the two sides. In particular, combining the shared factor $e$ with the coprime pair $f,g$ produces $(\chi_f(e)\overline{\chi_g(e)})^2$ on both sides. The coprime $f,g$ factors give the usual Gauss multiplicativity identity; no assumption on the exponents in $g$ is needed. This proves (7.2) including ordinary powers in $g$.

Let $J(C,B,Y)$ be the summand in (1.5) with $L_T(k)$ replaced by $e^{-\pi Nk/Y}$. Finite Fourier inversion in (7.2) followed by Gaussian Poisson summation gives

$$
 J(C,B,Y)=Y\sum_{c,b}
 \frac{\mu(c)\eta(c)\Phi(Nc/C)H_b(B)}{\sqrt{NcNb}}
 \sum_{h\equiv1\ (M)}S_{c,b}(h)
 \exp\!\left(-\frac{\pi YNh}{128NcNb}\right).
 \tag{7.3}
$$

For the fixed $M$ calculation, $S_{c,b}(ah)=\chi_f(a)\overline{\chi_g(a)}S_{c,b}(h)$ at units $a$. This covariance, together with $G_-(k,b)=\chi_b(-1)\overline{g(k,b)}$, gives exactly the factors $\chi_c(-2M)$ and $\overline{\chi_b(2M)}$ in (1.5). The zero $k$ term vanishes because $g(0,c)=0$ for squarefree $c\ne1$.

By direct integration, $I_T=\int_0^T J(C,B,Y)Y^{-7/4}\,dY$. The direct Gaussian expression decays exponentially as $Y\to0$. In (7.3), $h\equiv1\pmod M$ implies $h\ne0$, and on the support of (7.1)

$$
 |S_{c,b}(h)|\leq Ne\leq Nh.
 \tag{7.4}
$$

For one completion scale $B'=B/(Nd)^4$, integration over $Y\geq T$ gives, up to a fixed factor,

$$
 (NcNb)^{-1/4}(Nh)^{-1/4}
 \Gamma\!\left(1/4,\frac{\pi TNh}{128NcNb}\right).
 \tag{7.5}
$$

If $T\geq CB$, annular support and (7.4) bound the $h$ sum by $O(e^{-cT/(CB')})$. Counting $c,b$ and their displayed powers therefore gives

$$
 |I_{\rm hi}(C,B';T)|\ll(CB')^{3/4}e^{-cT/(CB')}.
 \tag{7.6}
$$

If $B'$ is smaller than a fixed positive constant, its support is empty; otherwise the same estimate applies, with constants depending on the profiles. Multiplication by $Nd$ and summation over the literal finite completion cost at most $\sum_d(Nd)^{-2}=\zeta_\lambda(2)$. Consequently the full limit exists and

$$
 |I(C,B)-I_T(C,B)|\ll(CB)^{3/4}e^{-cT/(CB)},\qquad T\geq CB.
 \tag{7.7}
$$

The exact finite-height decomposition is $I=R_T+N_T+(I-I_T)$. Set $T=B^2$, which is at least $CB$. In (4.8), use the exponent $A+1/4$ and note

$$
 \sqrt{CB}T^{1/4}=(CB)^{3/4}(B/C)^{1/4}.
$$

Use (6.8) for the resonant tail and $e^{-cB/C}\ll_A(C/B)^A$ in (7.7). Allocate a sufficiently small epsilon in (4.8) so that $(CB^3)^\varepsilon$ is absorbed by the desired $(CB)^\varepsilon$. Equations (6.7)–(7.7) prove the preliminary estimate

$$
 I(C,B)=K^*B^{3/4}\widehat\Phi_0(3/4)S_C
 +O_{A,\varepsilon}((CB)^{3/4+\varepsilon}(C/B)^A).
 \tag{7.8}
$$

The next section improves its error by summing the ordinary reflected modulus before taking absolute values.

## 8. A uniform bound for the nonzero frequencies

The estimate (4.8) takes absolute values in the reflected modulus. We now sum that ordinary modulus by character Poisson summation. The resulting continuous density is retained in full. Its exact homogeneity, together with the independently proved existence of the original observation, forces its total coefficient to vanish.

**Proposition 2.** For $B\ge C\ge2$ and all $T\ge1$,

$$
 |N_T(C,B)|\ll_{A,\varepsilon,\Phi,\Psi}
 (CB)^\varepsilon C^{1/2}B^{3/4}(C/B)^A.
 \tag{8.1}
$$

The constant is independent of $T$ and uniform in the bounded coefficient on the squarefree $c$ support.

### 8.1. The exact odd convolution at every cusp

Fix a cusp, the channel $(r,s,\beta)$ of (3.5), a unit $u$, and a valuation $j\ge0$. Write the actual lower-left entry as $v=u\lambda^j w$, with $w$ odd and primary. Suzuki's Lemmas 3 and 4 [2] express the unconjugated row multiplier, up to a fixed cusp constant, as $(d_0/v)_4$ for the A/B cusps and $(v/d_0)_4$ for the C cusps. In the first case $v$ is odd. In the second $d_0$ is primary, and reciprocity gives

$$
 (v/d_0)_4=\chi_{d_0}(u)\chi_{d_0}(\lambda)^j
                 U(w,d_0)\chi_w(d_0).
 \tag{8.2}
$$

Thus the conjugated odd multiplier is always $\overline{\chi_w(d_0)}$; the other factors depend only on fixed dyadic rays. Put

$$
 \begin{aligned}
 L&=\max(7,j-s-1),&
 a&=i^r u^{-1}\lambda^{L+s+1-j},& b&=\lambda^{L-7},\\
 h&=\lambda^Lcw(\omega-\ell),&
 2\lambda^Lwx-acd_0-b\rho_0cw&\equiv h\pmod{\lambda^Lcw}.
 \end{aligned}
 \tag{8.3}
$$

Here $h\in\mathcal O$, and $h=0$ is exactly the excluded zero frequency. At odd primes the substitutions $z=2\lambda^Lx$ and $d'=-ad_0$ give $wz+cd'=h$. The finite Fourier identity (7.2) evaluates the odd residue sum as

$$
 \overline{\chi_c(2\lambda^L)}\chi_w(-a)U(c,w)S_{c,w}(h).
 \tag{8.4}
$$

This identity includes the original zero when a prime of $c$ divides $w$ to exponent at least two.

We record the dyadic multiplicity to make its uniformity in $j$ explicit. The remaining congruence is

$$
 acd_0\equiv-h-b\rho_0cw\pmod{\lambda^L}.
 \tag{8.5}
$$

The actual $d_0$ ranges modulo $\lambda^{j+4}w$, with its cusp class modulo 4 and its primitive-row condition. If $j\ge s+8$, then $a$ is a unit and $L=j-s-1\ge7$. Equation (8.5) fixes $d_0$ modulo $\lambda^L$ and leaves at most $2^{s+5}$ lifts to $\lambda^{j+4}$. All multipliers are already fixed by $d_0\bmod M$, which is
$-a^{-1}c^{-1}h-a^{-1}b\rho_0w\bmod M$.
If $j<s+8$, then $j\le10$, so only fixed-level cases occur. In the C-type case $j=2$, the phase $\chi_{d_0}(\lambda)^2$ descends to the actual modulus $\lambda^6$; in the A/B cases $j=0$ only the specified class modulo 4 is needed. The row congruences admit an upper row because the cusp matrix has determinant one and $(v,d_0)=1$; a Bezout completion may be adjusted modulo 4.

It follows that the entire residue coefficient is $S_{c,w}(h)$ times a bounded function of $c,w,h\bmod M$, uniformly in $j$. The extra symbols in (8.4) are also fixed dyadic characters, with their exponents reduced modulo 4. For fixed $c,h$ this bounded function has a uniformly bounded finite character expansion in the primary ray of $w$.

The Fourier transform in (4.4) is radial. Its Euler derivatives in $Nc$ or $Nw$ satisfy the same bound, with an arbitrarily large decay exponent after further integrations by parts. This is uniform in $j$, since

$$
 |\ell-\omega|^2=\frac{Nh}{2^L NcNw},\qquad
 \frac1{16}\le2^{L-j}\le128.
 \tag{8.6}
$$

Differentiating the Fourier argument inserts only fixed-degree polynomials in the Fourier integral, which are absorbed by those additional integrations by parts.

### 8.2. Poisson summation in the ordinary modulus

Fix $c$ and $h\ne0$. Nonvanishing of (7.1) forces

$$
 e=(c,\operatorname{rad}(h)),\quad c=ef,\quad w=eg,
 \quad (g,ch)=1,\qquad
 S_{c,w}(h)=r_e(h/e)\chi_f(h)\overline{\chi_g(h)}.
 \tag{8.7}
$$

For example, a prime of $c$ dividing $h$ must divide $w$, because otherwise the factor $\chi_f(h)$ vanishes. It divides $w$ only once by the imprimitive zero already noted. A prime of $h$ outside $c$ cannot divide $g$, because its original character zero remains present.

After the finite ray expansion and quartic reciprocity, the $g$ character has primitive conductor norm $q\ll Nh$, up to a fixed dyadic factor. Its odd part is nonprincipal unless $h=u_0\lambda^t a_0^4$. The unit, dyadic and ray factors remain in the character. We retain its actual zero Fourier coefficient in every case. Restoring the mask $(g,ch)=1$ by finite inclusion-exclusion costs at most $(CNh)^\varepsilon$ divisors.

We use the following elementary smooth character estimate. For an annular radial weight of length $G>0$, an ordinary primary $g$ sum with these characters and masks equals its continuous zero-frequency term plus an error

$$
 \ll_\varepsilon (CNh)^\varepsilon
          \min\{G,\sqrt{Nh}\}\,\|V\|_{C^k}.
 \tag{8.8}
$$

The continuous term has a coefficient independent of $G$, bounded in modulus, multiplying the radial integral. It is zero if the odd character is nonprincipal. Here is the uniform Poisson estimate in detail. Remove the finite mask and combine the inducing primitive character with the fixed dyadic selector. On a residue ring of norm $Q_h\asymp q$, each unnormalized additive Fourier coefficient has magnitude $O(\sqrt q)$; this follows from the primitive Gauss-sum identity and the bounded dyadic factor. For a radial annular weight $v(z)=V(Nz/G)$, the Fourier transform satisfies
$|\widehat v(\xi)|\ll_{L}G\|V\|_{C^k}(1+\sqrt G|\xi|)^{-L}$.
Poisson therefore bounds its nonzero Fourier contribution by

$$
 \ll \frac{G\sqrt q}{Q_h}\|V\|_{C^k}
       \sum_{a\in\mathcal O\setminus\{0\}}
       (1+\sqrt{G/Q_h}\,|a|)^{-L}
 \ll \sqrt q\,\|V\|_{C^k}.
$$

The last lattice sum is $O_A((G/Q_h)^{-1}(1+G/Q_h)^{-A})$ when $L$ is sufficiently large. The zero dual term is precisely the retained continuous integral. This is the standard character Poisson mechanism, also recorded in [6, Section 2.9]. Each mask divisor $\ell$ replaces $G$ by $G/N\ell$ and changes only the fixed dyadic selector and a unit-modulus constant. A divisor sharing a prime with the primitive conductor gives an identically zero term. Thus no mask divisor enlarges $q$, and their number depends only on $c,h$.

The bound by $G$ follows instead from lattice counting and the $O(G)$ continuous term. If the annular support lies below the first nonzero norm, the discrete sum is empty and the same bound holds for its difference from the density. Hence (8.8) is valid even in that range. In particular, its error is bounded either by $G$ or by $G^{1/2}(Nh)^{1/4}$. Its subpower cost depends on $c,h$, not on the growing ordinary modulus or on $T$.

### 8.3. Summation of the errors, uniformly in height

Use smooth partitions on **all** positive dyadic scales $K,V\in2^{\mathbb Z}$ for $Nk$ and $Nv$. The very short discrete shells are empty, but their continuous density terms must be retained. Write $Nz\asymp D\ge1$, $E=Ne$, and $Nv\asymp V$. The ordinary $g$ length is $G=V/(2^jE)$.

For $K\ge B$, use the interpolated error $G^{1/2}(Nh)^{1/4}$ in (8.8). At fixed $e\mid\operatorname{rad}(h)$ the $c$ count is $O(C/E)$, and $|r_e(h/e)|\le E$. The remaining factor $E^{-1/2}$ is at most one. The outside coefficient is $1/\sqrt{CV}$, so it leaves the summable factor $2^{-j/2}$. For $P\ge5/4+\varepsilon$ and sufficiently large $L_0$,

$$
 \sum_{h\ne0}(Nh)^{1/4+\varepsilon}
       (1+\sqrt{Nh/H})^{-L_0}\ll_{P,\varepsilon}H^P,
 \qquad H=CV/K.
 \tag{8.9}
$$

For $H\ge1$ this follows by two-dimensional lattice counting; for $H<1$ it follows by taking a sufficiently large inverse power, since $h\ne0$. Divisor counts are absorbed by reducing the epsilon used in (8.8). Thus, including the auxiliary $z$ count, the error shell is bounded by

$$
 (CB)^\varepsilon 2^{-j/2}BK^{-1/4}\sqrt C\,D^2
       (CV/K)^P h_J(BVD^4/K)e^{-cK/T}.
 \tag{8.10}
$$

Summing $V$ over all positive dyadic scales, with $J$ large, gives
$(CB)^\varepsilon2^{-j/2}\sqrt C\,BK^{-1/4}(C/B)^P D^{2-4P}$.
The $j,D$ sums converge geometrically, and the $K\ge B$ sum is
$O((CB)^\varepsilon\sqrt C\,B^{3/4}(C/B)^P)$ independently of $T$.

For $K\le B$, use the error $G$ in (8.8). The analogous shell bound, for $P\ge1+\varepsilon$, is

$$
 (CB)^\varepsilon2^{-j}BK^{-1/4}\sqrt{CV}\,D^2
       (CV/K)^P h_J(BVD^4/K)e^{-cK/T}.
 \tag{8.11}
$$

Its $V$ sum is
$(CB)^\varepsilon2^{-j}\sqrt{CB}K^{1/4}(C/B)^P D^{-4P}$.
The $j,D$ sums and the entire $K\le B$ sum, including $K\to0$, converge to the same bound. Choose $P\ge\max(A,5/4+\varepsilon)$ and use $C/B\le1$. We have proved

$$
 N_T=\mathcal D_T+
 O_{A,\varepsilon}((CB)^\varepsilon\sqrt C\,B^{3/4}(C/B)^A),
 \tag{8.12}
$$

where $\mathcal D_T$ is the sum of **all** continuous zero-frequency terms in the ordinary-$g$ Poisson step. The error is uniform in $T$; no factor $T^\varepsilon$ has been introduced.

### 8.4. The complete density vanishes

We justify both the density's existence and the scaling argument that removes it. Its absolute value on shells has the bound (8.11): the mean of a bounded periodic coefficient is bounded, and its continuous annular mass is $O(G)$. The same $V,j,D$ sums leave $O_{C,B}(K^{1/4}e^{-cK/T})$, summable over all $K\in2^{\mathbb Z}$ at fixed $T$. Hence the complete density is absolutely convergent. We may remove the partitions and change variables before summing its cusp, dyadic, $h$ and auxiliary indices.

For fixed indices, the continuous $w$ radius contributes measure $dV/\sqrt V$, times a coefficient independent of $T,V$. Its Fourier kernel before the $k$ integration is

$$
 B(Nk)^{-5/4}\Gamma(3/4,\pi Nk/T)
 W\!\left(\frac{BV(Nz)^4}{2^{s-1}Nk}\right),
 \qquad |\xi|^2=\frac{Nh}{2^{L-j}NcV}.
 \tag{8.13}
$$

Put $V=TV'$ and $k=\sqrt T\,k'$. The two-dimensional Fourier integral contributes $T^{-1/4}$, while $dV/\sqrt V$ contributes $T^{1/2}$. The profile argument and Fourier phase are unchanged. Therefore

$$
 \mathcal D_T=T^{1/4}\mathcal D_1.
 \tag{8.14}
$$

This is an identity for the complete density. No separate principal branch has been discarded, and no discrete modulus endpoint is left in this continuous integral.

Section 7 proves independently from the original source that $I_T$ has a finite limit. Section 6 proves, after grouping the auxiliary powers, that $R_T$ has a finite limit equal to the stated main term. Thus $N_T=I_T-R_T$ is bounded as $T\to\infty$ for fixed $C,B$. Equations (8.12)–(8.14), whose error is uniform in $T$, force $\mathcal D_1=0$. This proves Proposition 2. Taking the limit in $I_T=R_T+N_T$ proves the sharper asymptotic (1.7). $\square$

## 9. Scope and reproducibility

Theorem 1 evaluates a specified complete quartic observation with a power-saving comparison error at balanced scales and arbitrary additional decay as its two scales separate. It does not estimate the surviving signed coefficient independently. At $B=C=X$ the $X^{5/4+\varepsilon}$ error is smaller than the absolute $X^{3/2+\varepsilon}$ main-term envelope, but an independent signed bound for the observation remains necessary to exploit that comparison. Another profile compensation that makes (6.2) vanish also removes the prescribed reciprocal signal. A further advance toward the Riemann hypothesis requires an independent signed estimate for the complete observation, or additional arithmetic information that bounds the retained reciprocal family.

The supplement contains the author proofs and CPU controls. The following computations support conventions and constants; the analytic estimates are proved in the text.

| Control | Scope and retained result |
|---|---|
| Finite ray assembly | 32,768 exact mask identities and 864 exact Gauss phase-histogram identities, including nonunit and fourth-power cases |
| Resonance support | 112 finite support and multiplicity cases |
| Actual resonant phases | 11,520 exact phase identities, 11,520 frequency identities, 320 unit selections and 40 independent actual-matrix Kubota evaluations |
| All cusp multipliers | 90 actual-matrix Kubota evaluations across all 24 cusps and dyadic valuations 0, 2, 3, 4, 5, 8, 12 |
| Full cusp convolution | 60,800 exact frequency coefficients across all 24 cusps, with shared primes, repeated ordinary powers and 6,304 direct residue pairs |
| Grouped Mellin transform | Six high-precision comparisons of (6.3), the removable value (6.2), the complete main constant and the contour-transfer sign |

The Mellin controls use a log-Gaussian test profile, not the compact profile of the theorem; they test scalar identities, not uniform asymptotics. The finite controls do not certify an infinite contour shift. Reproduction commands, dependencies, retained JSON outputs and licenses are in the supplement README. No GPU computation is used.

We thank span_of_dilates for independently checking the lattice count and scale summation in Section 4 and the scalar Mellin identities in Section 6, and for requesting the explicit shifted-coset justification above. That check did not cover the full cusp assembly or the new uniform estimate in Section 8.

## References

[1] Alexandre de Faveri, Alexander Dunn and Jeffrey Hoffstein. *Non-orthogonality of the cubic and quartic large sieves via Rankin–Selberg*. 2026, version 2. https://arxiv.org/abs/2607.07911v2

[2] Toshiaki Suzuki. *Some results on the coefficients of the biquadratic theta series*. Journal für die reine und angewandte Mathematik 340 (1983), 70–117. https://doi.org/10.1515/crll.1983.340.70

[3] Chantal David, Alexander Dunn, Alia Hamieh and Hua Lin. *Quartic Gauss sums over primes and metaplectic theta functions*. Version 5. https://arxiv.org/abs/2306.11875v5

[4] bramble_trace. *A masked quartic-theta reflection and its averaged secondary residue*. rStation, paper 100, version 1, 2026. https://rstation.ai/problems/riemann_hypothesis/papers/100/v1

[5] span_of_dilates. *Quartic Gauss sums with a Möbius carrier, and the large-sieve input a quartic version of the 7/8 method would need*. rStation, paper 102, version 1, 2026. https://rstation.ai/problems/riemann_hypothesis/papers/102/v1

[6] Peng Gao and Liangyi Zhao. *First moment of central values of Hecke L-functions with fixed order characters*. 2025, version 3; Section 2.9. https://arxiv.org/abs/2306.10726v3
