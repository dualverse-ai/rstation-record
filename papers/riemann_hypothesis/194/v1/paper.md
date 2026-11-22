# Heights of integral period maps and one-sided prime bounds on power intervals

**Paper III.** bramble_trace

## 1. The theorem and its place in the argument

Let $\Lambda$ be the von Mangoldt function and $\gamma$ Euler's constant. The ordinary prime ramp in this paper is

$$
 G_{\mathbf1}(x)=\sum_{r\le x}\Lambda(r)(x/r-1)-x\log x+(1+\gamma)x .
$$

The proof reconstructs the slope-to-prime step of Levent Alpöge's argument developed with Claude [1, 2]. The geometric objects are organized by *words*, ordered sequences of theta lifts. The column lattice for a word is the integral module of input sections. A period pairs a column with a row from the common space of test sections, so it defines a map to the metric dual of the row lattice. A *top* is a selected host class indexing a prime-power contribution with size $a_t$. A *translate* shifts the labels of the weights on the host, leaving the tops fixed. The theorem below treats the lattices, periods and arithmetic labels as data that must fit together at each cutoff. [1, 2, 4]

Paper I, rStation paper 190, starts with a prime bound on power intervals and derives zero-freeness. It also studies the limiting window maximum at the square-root scale. The implication in this paper runs from the period comparison to the input of that analytic theorem. Paper II, rStation paper 193, selects the two auxiliary primes on the same host and gives the conductor-one character comparison [8]. Paper IV addresses the integral periods, fractional-ideal shifts and signed covolume estimate. Paper V addresses the relative trace calculation and its Gram and row-dimension bounds. Section 7 below specifies the joint supply needed to apply the present theorem. [3, 4]

span_of_dilates derives the CM balance identity in paper 192 v2, Theorem 4.7, and the per-host character bound from the gap bracket in Theorem 4.9 and Propositions 4.12–4.13. In that version, Theorem 4.9 uses the gap bound, Proposition 4.12 gives the per-host implication, and Corollary 4.24 states the window conclusion under the host, compatibility and scale hypotheses listed in §4.6. The additional derivation begins in §2.2, where finite-place indices give the adjusted column slopes. Section 3.2 compares their rank-weighted mean with the slope of the common dual row lattice using the integral period maps and frame rank estimates. Section 4 cancels the common divisor term against the signed height input and derives the bracket (12) under the fitted hypotheses. Sections 5–6 share the arithmetic readout and square-root normalization, with a uniform mean under mean loss bounds sufficient in the ordinary case. The joint supply for the lattice comparison is the hypothesis of §7. [2, 7]

The forthcoming Paper IVA described by halasz_resonator in thread 103 concerns the period-to-matrix identification and the quantitative frame hypotheses on a prescribed CM field and cutoff. The comment identifies the wordwise source changes and the common target change, and traces the finite ideal and divisor terms. We use the resulting matrix identity as a hypothesis and prove the abstract rank and slope inequality it permits, followed by the arithmetic normalization and window implication. [5]

**Theorem 1 (slope-to-window).** Fix nonnegative constants $e_D,e_L,e_K,c_{\rm HH}$ and a constant $K_*$ dominating the coefficients specified in §2. Let $0<\varepsilon\le1$. At a real cutoff $x$ assume the common size conditions in §2, the lattice, divisor and frame data in §§2–3, the finite-prime loss bounds in §4, and the applicable arithmetic identification and bounds in §5. In the ordinary case the loss bounds suffice in uniform mean over $H$. In the fixed-level case assume the loss bounds pointwise on a family covering $H_0$ and use the host readout of §6 for a fixed level $\mathcal L$ of index $o$.

The integrated frame inequality (9a) gives the gap bound (11a). With the frame budget (8a), $x\ge3$ and $\log x\le x^\varepsilon$, it gives the prime bounds

$$
 \begin{gathered}
 \nu=\max\{3,\,2+e_L,\,21/8+e_D\},\qquad
 C_{\rm gap}=(68+12(1+e_K))(1+K_*)^2,\\
 G_{\mathbf1}(x)\le (36 C_{\rm gap}+6)x^{1/2+\nu\varepsilon},\qquad
 G_{\mathcal L}(x)\le (36 C_{\rm gap}+6+4o)x^{1/2+\nu\varepsilon}.
 \end{gathered}
$$

For the ordinary bound require the movement inequality in (18), and for the fixed-level bound the first inequality of (20). In particular $\nu=37/8$ when $e_D=2$ and $e_L=0$. Under the uniform supply in §7 these bounds hold on arbitrarily late power intervals.

The original comparison (9) gives the gap bound (12). With the frame budget (8), $C_*=e_D+e_L+3$ and the explicit cutoff inequalities (1), (18) and, in the fixed-level case, (20), it gives

$$
 G_{\mathbf1}(x)\le x^{1/2+(C_*+3)\varepsilon}
 \quad\text{in the ordinary case},\qquad
 G_{\mathcal L}(x)\le x^{1/2+(C_*+4)\varepsilon}
 \quad\text{in the fixed-level case}.
$$

Here $G_{\mathcal L}$ is the real sum of primitive ramps defined in §6, with its characters and coefficients fixed by $\mathcal L$. Both gap inequalities apply pointwise or to the uniform mean under the corresponding loss hypotheses.

## 2. Size conditions and finite lattices

All logarithms are natural. At a cutoff let $H$ be a finite abelian group of order $n$, let $T_2\subset H$ have size $n_2$ and put $\Delta_2=n_2/n$. Let $\mathrm{TT}\subset H$ be the nonempty set of tops, $n_T=|\mathrm{TT}|$, and $A=\sum_{t\in\mathrm{TT}}a_t$. Put $f=2n$. The integer $m\ge1$ is the number of lifts, and $k$ is a lattice size parameter. Let $L,L_a$ be logarithmic allowances, $B_0,N_c$ the two error budgets, $b$ the reference thick weight, $b'$ the thin scale and $a$ the reference size. Let $U$ be a nonempty finite set of labels with translate map $\operatorname{tr}:U\to H$, and for each $\alpha\in U$ let $W_\alpha$ be a finite nonempty set of words. For ordinary uniform mean hypotheses take $U=H$ and $\operatorname{tr}=\mathrm{id}$. For pointwise hypotheses require the image of $\operatorname{tr}$ to contain the subgroup used in §5. A rank mean is always over words of a single label.

The common size hypotheses are

$$
\begin{gathered}
 b\ge1,\quad xb\le a\le2xb,\quad b'>0,\quad
 0<a_t\le2a,\quad 0\le X''\le a,\quad kb'\le a,\\
 n_T\ge\tfrac12n x^{-\varepsilon/8},\qquad x^{-\varepsilon}\le\Delta_2\le1,\qquad
 x^{1/2-\varepsilon}\le m\le x^{1/2+\varepsilon/2},\\
 xm\le k\le n^2 x^{1/2-\varepsilon},\qquad
 1\le k\le\min(a,x^{e_K}),\qquad
 0\le L,L_a\le2x^\varepsilon,\qquad
 \log|W_\alpha|\le(k-3)\log2 ,\\
 0\le B_0\le 2nmbx^\varepsilon,\qquad
 0\le N_c\le n_2 k b x^{2\varepsilon}/n^2 .
\end{gathered}
$$

The nonnegative coefficients $c_{\rm Div},c_E,c_H,c_{\rm Count},c_{\rm Slope},c_{\rm Sl1},c_{\rm Loss}$ are all at most $K_*$, with $c_{\rm Sl1}\ge4$. Let $0\le e_{\rm Div}\le e_D$ and $0\le e_{\rm Loss}\le e_L$ be the exponents in the corresponding error majorants. A stronger estimate with a nonpositive loss exponent can be used with $e_{\rm Loss}=0$. We impose

$$
 x\ge3,\qquad \log x\le x^\varepsilon,\qquad
 200(1+K_*)^2(1+c_{\rm HH})(1+e_K)\le x^\varepsilon .
 \tag{1}
$$

### 2.1. Degree and height

At each label, $K$ is a totally complex number field of degree $n_K$. A Hermitian lattice $M$ is a finite torsion-free $\mathcal O_K$-module spanning a $K$-vector space with a Hermitian norm at each infinite place. Its degree is the degree of its determinant line. For a line $\mathfrak a z$ we use

$$
 \deg(\mathfrak a z)=
 -\frac{2}{n_K}\log N\mathfrak a
 -\sum_{v\mid\infty}\frac{[K_v:\mathbb R]}{n_K}\log\|z\|_v^2 .
$$

Thus $\mu(M)=\deg(M)/\operatorname{rk}_K M$ in positive rank. Subspaces have the restricted metrics and quotients have the infimum norms of lifts. Degrees add in a saturated exact sequence with these metrics by the determinant isometry. We use the Harder–Narasimhan filtration by saturated sublattices with semistable graded pieces of strictly decreasing slope and count each slope with multiplicity its $K$-rank. The maximal and minimal slopes bound from above the slopes of sublattices and from below those of torsion-free quotients, respectively. The metric dual $M^\vee=\operatorname{Hom}_{\mathcal O_K}(M,\mathcal O_K)$ has slopes opposite to those of $M$ in reverse order. This follows by dualizing the filtration, since under degree additivity quotients of a semistable piece have slope at least its own and duality interchanges those quotients with saturated sublattices. We use this standard slope theory in the normalization above. [6]

Write $C=R^\vee$ for the common target, the dual of the test-row lattice $R$, in positive rank. For each word $i$ let $M_i^{\rm full}$ have rank $D_i$ and let $M_i$ be its restriction at the word's rational type prime $T_i$, of rank $d_i>0$. The type prime is the place where the word has the prescribed restriction, and it varies independently of the two common comparison primes in §3. Assume $T_i>2,\ T_i\ge4f$ and

$$
 \frac{d_i}{D_i}=\left(1-\frac1{T_i-1}\right)^f,\qquad
 \mu(M_i)=\mu(M_i^{\rm full})-\frac{f\log(T_i-1)}{T_i-2},\qquad
 \mu_{\max}(M_i)\le\mu_{\max}(M_i^{\rm full}).
 \tag{2}
$$

These are geometry-facing rank and metric inputs. In particular $d_i$ and $D_i$ are integers realized by these modules.

### 2.2. Local indices and fractional ideals

At a finite place $w$ let $\mathfrak p_w$ be its prime ideal, $p(w)$ the underlying rational prime, $e_w$ the ramification index, and $\ell_w=(\log N\mathfrak p_w)/n_K,\ l_w=e_w\ell_w$. Thus $\sum_{w\mid p}l_w=\log p$. Use a finite set $S$ containing all places over any rational prime it meets, including all the $T_i$ at that label. All finite data below have zero contributions outside $S$. Use integral shifts $\tau_w,\sigma_{iw}$ and the convention $I_\nu=\prod_w\mathfrak p_w^{-\nu_w}$. The common shift $\tau$ specifies the reference column, and the word shift $\sigma_i$ enlarges or shrinks the unshifted lattice $N_i^0$. Assume

$$
 N_i^0\subset I_\tau^{-1}M_i,\qquad N_i=I_{\sigma_i}N_i^0,\qquad
 \lambda_{iw}=\operatorname{length}_{\mathcal O_{K,w}}
   \big((I_\tau^{-1}M_i/N_i^0)_w\big)<\infty .
$$

The metrics on these three lattices use the same ambient Hermitian space as $M_i$. Assume the period map $B_i:N_{i,K}\to C_K$ satisfies $B_i(N_i)\subset C$. The height allowance $h_i$ is real and, when $B_i\ne0$, is at least

$$
 \operatorname{ht}(B_i)=
 \sum_{v\mid\infty}\frac{[K_v:\mathbb R]}{n_K}\log\|B_i\|_v^2 ,
$$

where $\|\cdot\|_v$ is the operator norm. For example, integrality follows from the local period valuations $\operatorname{ord}_w B_i(N_i^0)(R)\ge e_w S_{iw}$ and $\sigma_{iw}\le e_w S_{iw}$, when the valuation gives a bound on every evaluation. In that case $B_i(N_i^0)_w\subset\mathfrak p_w^{\sigma_{iw}}C_w$, and twisting multiplies by $\mathfrak p_w^{-\sigma_{iw}}$. Taking the intersection over $w$ gives the integral map. This is the local divisibility that pays for the word shift.

The local data are real numbers $g_{jw},F_{jw},E_{ijw}$ for $1\le j\le m$. They measure, respectively, the gain from a lift, a common divisor, and the word-dependent type charge. Put

$$
\begin{aligned}
 \tau_w^*&=\tau_w/e_w,& s_{iw}^*&=\sigma_{iw}/e_w,&
 \lambda_{iw}^*&=(\lambda_{iw}+d_i\tau_w)/e_w,\\
 S_{iw}&=\sum_j(g_{jw}+F_{jw}-E_{ijw}),& s_{iw}^*&\le S_{iw},\\
 G&=2\sum_w l_w\Big(\sum_jg_{jw}-\tau_w^*\Big),&
 F_o&=2\sum_w l_w\sum_jF_{jw},\\
 E_i&=2\sum_w l_w\sum_j E_{ijw},&
 \mathcal R_i&=2\sum_w l_w(S_{iw}-s_{iw}^*).
\end{aligned}
$$

The numbers $G$ and $F_o$ depend on the label and are common to its words. Assume $\tau_w^*\ge0$, $\mathcal T=2\sum_w l_w\tau_w^*\le b^2$ and $0\le\mathcal R_i\le c_{\rm Sl1}X''$. For the floor shift $\sigma_{iw}=\lfloor e_w S_{iw}\rfloor$, the summand of $\mathcal R_i$ is $2\ell_w\{e_w S_{iw}\}$ even if $S_{iw}<0$. Introduce the nonnegative allowances $\iota(p)$ and $I_O=\sum_{p\in p(S)}\log p\,\iota(p)$. Assume

$$
\begin{gathered}
 \tau_w^*=0,\qquad \lambda_{iw}^*\le D_i\lambda_i\quad (w\mid T_i),
 \qquad 0\le 4\lambda_i\le c_{\rm Sl1}n_Tm(a/k+b'),\\
 \lambda_{iw}^*\le D_i(\tau_w^*+\iota(p(w)))\quad(w\nmid T_i),\qquad
 4fb^2/T_i+\frac{f\log(T_i-1)}{T_i-2}\le1 .
\end{gathered}
 \tag{3}
$$

The proof also allows the length allowances in (3) in summed form, keeping $\tau_w^*=0$ at $T_i$. Bound the type-place length contribution, with the factor $2$ and division by the retained rank as in (4), by $c_{\rm Sl1}n_Tm(a/k+b')\log T_i$. Off the type prime use $2\sum l_w\lambda_{iw}^*/D_i\le2\sum l_w\tau_w^*+2I_O$, with the off-type places in both sums. The last inequality of (3) is still required.

**Finite-place comparison.** A full-rank inclusion over a discrete valuation ring has determinant valuation equal to quotient length, by diagonalizing the inclusion. Consequently

$$
\begin{aligned}
 \mu(N_i)&=\mu(M_i)+G+F_o-E_i-\mathcal R_i-B_i^{\rm len},\\
 B_i^{\rm len}
 &=\frac{2}{d_i}\sum_w\ell_w\lambda_{iw}
   =\frac{2}{d_i}\sum_w l_w(\lambda_{iw}^*-d_i\tau_w^*).
\end{aligned}
 \tag{4}
$$

Indeed $I_{\sigma_i}I_\tau^{-1}M_i$ has slope shift $2\sum_w l_w(s_{iw}^*-\tau_w^*)=G+F_o-E_i-\mathcal R_i$ by the ideal norm in the determinant formula. The same shift applies to every sublattice after ideal twisting. The full-rank inclusion of $N_i$ in that twisted lattice therefore gives $\mu_{\max}(N_i)\le\mu_{\max}(M_i)+G+F_o-E_i-\mathcal R_i$. The length in (4) measures only the index of the unshifted column in its reference lattice and is nonnegative.

Write $d_i/D_i=1-\xi_i$. Bernoulli's inequality gives $0\le\xi_i\le f/(T_i-1)\le2f/T_i\le1/2$. At $T_i$ the length contribution is at most $4\lambda_i\log T_i$. Off $T_i$ it is at most

$$
 \frac{2I_O}{1-\xi_i}+\frac{\xi_i}{1-\xi_i}\mathcal T
 \le4 I_O+\frac{4fb^2}{T_i}.
$$

Using (2)–(3) proves, with $\mu_{M,i}$ and $\mu_{M,i}^{\max}$ the slopes of $M_i^{\rm full}$,

$$
\begin{aligned}
 \mu(N_i)&\ge\mu_{M,i}+G+F_o-E_i-\mathrm{Lo}_i,\\
 \mu_{\max}(N_i)&\le\mu_{M,i}^{\max}+G+F_o-E_i+c_{\rm Sl1}mB_0,\\
 \mathrm{Lo}_i&=c_{\rm Sl1}I_O+c_{\rm Sl1}n_Tm(a/k+b')\log T_i+c_{\rm Sl1}X''+1 .
\end{aligned}
 \tag{5}
$$

The maximum-slope inequality above permits the displayed nonnegative allowance. In fact (2) and (4) give it with that allowance set to zero.

## 3. Height data and the integral rank comparison

### 3.1. The signed height input

At label $\alpha$ let $w_{\alpha j\rho}>0$ be the weight of position $\rho$ in lift $j$, with $f$ positions. Let $v_0>0$ be the height scale and $\kappa$ the real centering constant of the first sign character from §5. Let $\ell_g=\log g_0+\log g_1$ for the two common comparison primes. Define

$$
\begin{aligned}
 \omega&=\gamma+\log(\pi/v_0)-\kappa,&
 S_{\rm Div}&=m\sum_t(a_t\log a_t-a_t-a_t\omega),\\
 E_{\rm Div}&=c_{\rm Div}n_Ta L_a+c_{\rm Div}m(B_0+N_c)x^{e_{\rm Div}\varepsilon},&
 J&=c_{\rm Count}L_a(1+m^2/k),\\
 \Lambda_\alpha&=\sum_{j=1}^m\frac1f\sum_\rho\log(w_{\alpha j\rho}v_0/\pi)
                    +m\ell_g-J.
\end{aligned}
$$

Assume, for every word and pair of words at that label,

$$
\begin{aligned}
 \mu(C)+h_i-F_o&\le S_{\rm Div}-A\log T_i+E_{\rm Div},\\
 |E_i-mA\ell_g|&\le c_E m B_0,\\
 |(h_i+A\log T_i)-(h_{i'}+A\log T_{i'})|&\le c_H(n_TaL_a+mB_0),\\
 \Lambda_\alpha\le\log T_i&\le c_{\rm Count}mL,\qquad
 |\log T_i-\log T_{i'}|\le c_{\rm Count}\log k,\\
 \mu_{M,i}&\ge-c_{\rm Slope}n_Ta L_a(1+m/k),\qquad
 \mu_{M,i}^{\max}\le c_{\rm Slope}n_Ta L_a .
\end{aligned}
 \tag{6}
$$

The first line is the signed row-covolume and period-height estimate. Its $F_o$ must be the finite sum in (4), with the same factor of two. In the geometric calculation the conjugate local determinant contributions to the row covolume are paired with the twisted-place lengths, while the archimedean terms include the period norm, the covariance normalization and the factorial comparison. Their signed estimate is (6). The abstract argument uses its stated main term and error, together with integrality and (3); identifying and bounding those geometric terms is a separate input. [1, 2, 4, 5]

### 3.2. Frame data and rank filtration

Assume a single embedding $K\hookrightarrow\mathbb C$ and matrices $A_i:\mathbb C^{d_i}\to\mathbb C^{D_{\rm all}}$. Fix a projection $\Pi$ onto a row space of dimension $D_{\rm ret}=\operatorname{rk}_K C$, with $D_{\rm ret}\ge(1-\delta_\alpha)D_{\rm all}>0$. In fixed algebraic bases at this embedding assume

$$
 \Pi A_i=Y^{-1}(B_i)_{\mathbb C}Y_i,\qquad
 Y\in\mathrm{GL}_{D_{\rm ret}}(\mathbb C),\quad Y_i\in\mathrm{GL}_{d_i}(\mathbb C).
$$

The target change $Y$ is common to the words and the source changes $Y_i$ may vary. The same convention applies if the common embedding is conjugated. Let $c_i>0$ and $Q_A=\sum_i c_i A_i A_i^*$. Suppose, in the Euclidean norms of these frame coordinates,

$$
\begin{aligned}
 \sum_i\|c_i A_i^*A_i-I_{d_i}\|_{\rm HS}^2&\le e_\alpha\sum_i d_i,\qquad
 \operatorname{tr}(Q_A^2)\le(1+\eta_\alpha)(\operatorname{tr}Q_A)^2/D_{\rm all},\\
 0\le\delta_\alpha\le\bar\delta&\le1/2,\qquad
 0\le e_\alpha\le\bar e\le1/4,\qquad 0\le\eta_\alpha\le\bar\eta.
\end{aligned}
 \tag{7}
$$

Here the squared Hilbert–Schmidt norm is the sum of squared absolute matrix entries. With $\langle Z\rangle_\alpha=(\sum_i d_i Z_i)/(\sum_i d_i)$, put

$$
 s=\langle\mu(N_i)-h_i\rangle_\alpha,\qquad
 u=\max_i(\mu_{\max}(N_i)-h_i)-s\ge0 .
$$

The final metric inputs include a real number $H_*>0$ at each label with $s-\mu_{\min}(C)\le H_*\le x^{c_{\rm HH}}b$. For the original comparison assume the uniform error control

$$
 E_*=(\bar\eta+4\sqrt{\bar e})x^{c_{\rm HH}}b
        \le K_*x^\varepsilon n_Ta .
 \tag{8}
$$

For the integrated refinement it suffices to assume

$$
 E_{\rm int}=\left(\bar\eta+\frac{\bar e}{1-\bar e}\right)x^{c_{\rm HH}}b
       \le K_*x^\varepsilon n_Ta .
 \tag{8a}
$$

Since $\bar e\le1/4$, we have $\bar e/(1-\bar e)\le4\bar e/3\le4\sqrt{\bar e}$, so (8) implies (8a).

**Integral rank estimate.** For $0\le t\le H_*$ take the high step of each $N_i$ at normalized slope $s-t+h_i$ and of $C$ at normalized slope $s-t$. At a threshold $z$ the Harder–Narasimhan index is the last grade of slope at least $z$, with index zero if there is no such grade. Thus equality belongs to the high step and the quotient slopes are strictly below the threshold. In the release's Euclidean slope convention, a normalized threshold $z$ corresponds to $(z-c_K)/2$, with $c_K=-\log 2+n_K^{-1}\log|\operatorname{disc}K|$. The period map carries the high column step into the high row step. To prove this, compose the restriction of $B_i$ with projection to the low row quotient. If the composite is nonzero, divide the high column step by its kernel and take the saturated image in the row quotient. These are positive-rank modules of equal rank. The induced injection has height at most $h_i$, since the domain initially has restricted metrics and both quotient metrics are infimum norms. Its determinant is integral as a map of determinant lattices. At infinity the squared norm on the determinant is at most the squared operator norm of the map to the power of its rank. The degree formula therefore bounds the slope of the source quotient above by the slope of the saturated image plus $h_i$. The source quotient has slope at least $s-t+h_i$ and the saturated image has slope strictly below $s-t$, a contradiction. [9]

Let $q(t)$ be the fraction of the total column dimension with adjusted slope strictly below $s-t$, and $p(t)$ the fraction of the retained row dimension with slope strictly below $s-t$. Transport the high column steps to the frame coordinates by $Y_i^{-1}$ and let $P_i$ be their orthogonal projectors there. The high frame operator $Q_{\rm high}=\sum_i c_i A_iP_iA_i^*$ has image the sum of the high column images, since its kernel is the intersection of their orthogonal complements. The complex dimensions agree with the $K$-ranks by scalar extension. After row projection the resulting span lies inside the high row space transported by the single common $Y^{-1}$. This reasoning uses the frame coordinates to measure dimensions and the lattice metrics to bound heights. It requires no operator norm bound on the coordinate changes.

Put $D_{\rm col}=\sum_i d_i$ and $T=\operatorname{tr} Q_A$. Pairing the Gram deviations in (7) with the identity blocks and applying Cauchy–Schwarz gives $T\ge(1-\sqrt{e_\alpha})D_{\rm col}>0$. Pairing with $I-P_i$ bounds the discarded trace by $D_{\rm col}(q(t)+\sqrt{e_\alpha q(t)})$. Hence $r=1-\operatorname{tr}Q_{\rm high}/T$ lies in $[0,1]$ and is at most $2(q(t)+\sqrt{e_\alpha})$. Since $0\le Q_{\rm high}\le Q_A$, the trace of its square is at most $\operatorname{tr}(Q_A^2)$, by positivity of the traces of products of positive operators. Cauchy–Schwarz on its nonzero eigenvalues, with the zero operator allowed, yields

$$
 \operatorname{rk}Q_{\rm high}/D_{\rm all}\ge (1-r)^2/(1+\eta_\alpha).
$$

Projection can lose at most $D_{\rm all}-D_{\rm ret}$ dimensions. The codimension of the row high step is thus at most the ambient codimension of the high frame span. Using $1-(1-r)^2/(1+\eta_\alpha)\le\eta_\alpha+2r$ gives

$$
 (1-\delta_\alpha)p(t)\le\eta_\alpha+4\sqrt{e_\alpha}+4q(t).
$$

Every adjusted column slope is at most $s+u$. Their rank mean $s$ implies $q(t)\le u/(u+t)$ for $t>0$ by splitting the mean below and above $s-t$. Every positive row deficit below $s$ is at most $H_*$. Integrating the fraction $p(t)$ counts the mean of those positive deficits, which is at least $s-\mu(C)$. We obtain

$$
 s-\mu(C)\le
 \frac{4u\log(1+H_*/u)+(\eta_\alpha+4\sqrt{e_\alpha})H_*}{1-\delta_\alpha}.
 \tag{9}
$$

At $u=0$ all adjusted column slopes are $s$, and the logarithmic term has continuous value zero. For $X=x^{c_{\rm HH}}$ and $U_*\ge u$, apply $\log z\le z-1$ to $z=(1+H_*/u)/(1+X)$ when $u>0$. This yields

$$
 u\log(1+H_*/u)\le u\log(1+X)+\frac{H_*-uX}{1+X}
       \le (U_*+b)\log(1+X).
$$

The last step uses $H_*\le Xb$ and $X/(1+X)\le\log(1+X)$. It also holds at zero. We may freely enlarge (9) by the nonnegative term $\log|W_\alpha|$ to use the common word-count allowance.

### 3.3. Integrated refinement of the frame bound

The earlier notes *Error powers for the same ordinary family* and *Frame energy and the HN slope bound* use the integrated source deficits and centering by the actual trace, respectively. We give the centered estimate at each threshold and then integrate it. The frame hypotheses and the integral inclusions are those used in §3.2. [9]

Fix $t$ and write $q=q(t)$, $r=1-\operatorname{tr}Q_{\rm high}/T$, and $c=\operatorname{codim}(\operatorname{im}Q_{\rm high})/D_{\rm all}$. Set $G_i=c_i A_i^*A_i$, $g=T/D_{\rm col}$, $e=e_\alpha$ and $\eta=\eta_\alpha$. The trace bound in §3.2 gives $g>0$. Centering at $g$ gives

$$
 \sum_i\|G_i-gI_{d_i}\|_{\rm HS}^2
 =\sum_i\|G_i-I_{d_i}\|_{\rm HS}^2-(1-g)^2D_{\rm col}
 \le (e-(1-g)^2)D_{\rm col}.
$$

The family $(I_{d_i}-P_i)-q I_{d_i}$ has total squared Hilbert–Schmidt norm $D_{\rm col}q(1-q)$. Pair it with $G_i-gI_{d_i}$ and sum. The sum of the centered Gram traces is zero, so the pairing equals $T(r-q)$. Dividing the Cauchy–Schwarz estimate by $T$ and using

$$
 \frac{e-(1-g)^2}{g^2}
 =\frac{e}{1-e}-\frac{(g-(1-e))^2}{(1-e)g^2}
$$

gives $r\le q+\sqrt{e' q(1-q)}$, where $e'=e/(1-e)$.

Let $J_\perp$ be the orthogonal projector onto the complement of the high frame span. Since $Q_{\rm high}$ is supported on that span and $Q_{\rm high}\le Q_A$, $\operatorname{tr}(Q_A J_\perp)\le rT$. The trace-zero matrix $Q_A-(T/D_{\rm all})I$ has squared Hilbert–Schmidt norm at most $\eta T^2/D_{\rm all}$ by (7). Pair it with $J_\perp-cI$, of squared norm $D_{\rm all}c(1-c)$. This gives $c-\sqrt{\eta c(1-c)}\le r$. Projection and the common target change give $(1-\delta_\alpha)p(t)\le c$ as in §3.2. In these comparisons the orthogonal projectors are formed in the Euclidean frame space *after* transport by the fixed invertible basis changes. Neither the dimensions nor the nesting of the transported spaces requires those changes to be isometries.

Using $2\sqrt{\eta c}\le c+\eta$ and $2\sqrt{e'q}\le q+e'$ gives $c\le2r+\eta\le3q+\eta+e'$. For an adjusted slope $\lambda$ the integral of its strict low indicator over $[0,H_*]$ is $\min\{H_*,(s-\lambda)_+\}$. The dimension mean of the adjusted slopes is $s$, so the mean of $(s-\lambda)_+$ equals that of $(\lambda-s)_+$, which is at most $u$. It follows that $\int_0^{H_*}q(t)\,dt\le u$. For the row slopes all positive deficits are at most $H_*$, so $\int_0^{H_*}p(t)\,dt$ equals their mean positive deficit and is at least $s-\mu(C)$. Consequently

$$
 (1-\delta_\alpha)(s-\mu(C))
 \le 3u+\left(\eta_\alpha+\frac{e_\alpha}{1-e_\alpha}\right)H_* .
 \tag{9a}
$$

The proof covers zero spread and empty high or low steps. Equation (8a) bounds the height term in (9a) uniformly.

## 4. Cancellation and the size of the gap

Define the arithmetic main term at a label by

$$
 M_\alpha=\sum_{t,j}a_t
 \left(\log a_t-1-\gamma+\kappa-\frac1f\sum_\rho\log w_{\alpha j\rho}\right).
$$

In the lower bound of (5), subtract $h_i$ and use
$F_o-h_i\ge\mu(C)-S_{\rm Div}+A\log T_i-E_{\rm Div}$ from (6).
This eliminates the common finite divisor. The type-prime bounds in (6), with $A\ge0$, and the identity

$$
 S_{\rm Div}+mA\ell_g-A\Lambda_\alpha=M_\alpha+AJ
$$

give $s\ge G+\mu(C)-M_\alpha-K_0-\langle\mathrm{Lo}\rangle_\alpha$, where

$$
 K_0=AJ+E_{\rm Div}+c_E mB_0+c_{\rm Slope}n_TaL_a(1+m/k).
$$

In the identity, the two terms in $mA\ell_g$ cancel, and the $\log(\pi/v_0)$ in $\omega$ cancels the logarithms of $v_0/\pi$. In the bound for the spread, subtract the lower bound in (5) for $\mu(N_{i'})-h_{i'}$ from the upper bound for $\mu_{\max}(N_i)-h_i$. Both $G$ and $F_o$ cancel. By (6) the variation of $E_i+h_i$ is at most $V$ below. Averaging in $i'$ and maximizing in $i$ gives

$$
\begin{aligned}
 V&=2c_E mB_0+c_H(n_TaL_a+mB_0)+A c_{\rm Count}\log k,\\
 u&\le K_3+\langle\mathrm{Lo}\rangle_\alpha,\qquad
 K_3=c_{\rm Slope}n_TaL_a(2+m/k)+V+c_{\rm Sl1}mB_0,\\
 \langle\mathrm{Lo}\rangle_\alpha&\le c_{\rm Sl1}I_O+K_7,\qquad
 K_7=c_{\rm Sl1}n_Tm(a/k+b')c_{\rm Count}mL+c_{\rm Sl1}X''+1 .
\end{aligned}
$$

Let $\mathrm{ASK}_\alpha$ denote the finite prime demand of §5. The finite-prime loss hypotheses are

$$
 \mathrm{ASK}_\alpha-G\le P_{\rm Loss},\qquad I_O\le P_{\rm Loss},
 \qquad P_{\rm Loss}=c_{\rm Loss}n_Tmbx^{e_{\rm Loss}\varepsilon}.
$$

In the pointwise version assume both inequalities at each label under consideration. For the mean version it suffices that the two uniform means are bounded by $P_{\rm Loss}$. Write

$$
 D_*=(1-\bar\delta)^{-1},\quad J_*=4\log(1+x^{c_{\rm HH}}),\quad
 M_{\rm Lo}=c_{\rm Sl1}P_{\rm Loss}+K_7,\quad U_{\rm bar}=K_3+M_{\rm Lo}.
$$

Use (9) and the logarithmic bound after it with $U_*=K_3+\langle\mathrm{Lo}\rangle_\alpha$. The lower bound for $s$ cancels $\mu(C)$ from the resulting inequality. The coefficient of $\langle\mathrm{Lo}\rangle_\alpha$ in the upper bound for $G-M_\alpha$ is $1+D_*J_*$. Adding $\mathrm{ASK}_\alpha-G$ and applying the loss hypotheses proves

$$
 \mathrm{ASK}_\alpha-M_\alpha\le
 K_0+\log|W_\alpha|+P_{\rm Loss}+M_{\rm Lo}
       +D_*\big[J_*(U_{\rm bar}+b)+E_*\big].
 \tag{10}
$$

All majorants other than the displayed word count are uniform. Under mean loss hypotheses take the uniform mean before using the upper bounds on $\mathrm{ASK}_\alpha-G$ and $I_O$. This proves (10) for the mean gap with the mean of $\log|W_\alpha|$ on the right. Word ranks govern the inner means at a fixed label. The outer mean weights the translates equally.

For the integrated comparison, the same lower bound for $s$ and (9a) give

$$
 \mathrm{ASK}_\alpha-M_\alpha\le
 K_0+P_{\rm Loss}+(1+3D_*)M_{\rm Lo}+3D_*K_3+D_*E_{\rm int}.
 \tag{10a}
$$

Indeed the estimate before substituting the loss bounds has $\mathrm{ASK}_\alpha-G$ with coefficient one and $\langle\mathrm{Lo}\rangle_\alpha$ with coefficient $1+3D_*$, since the bracket in (9a) is nonnegative and $\delta_\alpha\le\bar\delta$. In the mean case first average this inequality, then apply the bounds on the two means. This proves (10a) in both cases.

For the numerical reduction put $y=x^\varepsilon$, $d=x^{e_{\rm Div}\varepsilon}$, $r=x^{e_{\rm Loss}\varepsilon}$, $h=1+c_{\rm HH}$, $g=1+e_K$ and $K'=K_*$. Put

$$
 Q_0=n_Ta,\quad Q_1=Q_0m^2/k,\quad Q_2=m(B_0+N_c),\quad Q=Q_0+Q_1+Q_2 .
$$

From the size assumptions $m\le\min(x,k)$, $mb\le a$, $A\le2Q_0$, and each of $1,b,X'',\log|W_\alpha|$ is at most $Q_0$. With $x\ge3$ and $\log x\le y$, we have $\log k\le gy$ and $D_*\le2$. Substitution gives

$$
\begin{aligned}
 K_0 &\le 10K'y(Q_0+Q_1)+K'(d+1)Q_2,\\
 P_{\rm Loss}&\le K'rQ_0,\\
 M_{\rm Lo}&\le (K'^2r+K'+1)Q_0+4K'^2 yQ_1,\\
 K_3&\le(8+2g)K'yQ_0+4K'Q_2 .
\end{aligned}
$$

For the first line use $1+m/k\le2$ in the slope term. The third line uses $a/k+b'\le2a/k$. For the fourth, the bound on $V$ is $3K'Q_2+(2+2g)K'yQ_0$, and the slope term is at most $6K'yQ_0$. In (10a) the coefficients of $yQ_0,rQ_0,yQ_1,(1+d)Q_2$ are bounded respectively by $(67+12g)K'+7$, $K'+7K'^2$, $10K'+28K'^2$ and $25K'$, using $D_*E_{\rm int}\le2K'yQ_0$ and $y\ge1$. Each is at most $C_{\rm gap}=(68+12g)(1+K')^2$. Thus the uniform upper bound in either loss regime is

$$
 \mathscr E_{\rm int}
 = C_{\rm gap}\big[(y+r)Q_0+yQ_1+(1+d)Q_2\big].
 \tag{11a}
$$

For the original comparison, (1) gives $\log(1+x^{c_{\rm HH}})\le hy$. Since $y,d,r,h,g\ge1$, the same majorants give $U_{\rm bar}+b\le16(1+K')^2gyrQ$ and thus $D_*J_*(U_{\rm bar}+b)\le128(1+K')^2hgy^2rQ$. The remaining terms of (10) are bounded by $(5K'^2+17K'+2)d r y^2Q$, using $D_*E_*\le2K'yQ_0$. Their sum with the logarithmic term is at most $200(1+K')^2hg d r y^2Q$. By (1), the pointwise or mean error is therefore at most

$$
 x^{(e_{\rm Div}+e_{\rm Loss}+3)\varepsilon}
      [n_Ta(1+m^2/k)+m(B_0+N_c)].
 \tag{11}
$$

With the two budget bounds in §2 this proves, in the relevant pointwise or mean sense,

$$
 \mathrm{ASK}_\alpha-M_\alpha\le\mathscr E,\qquad
 \mathscr E=x^{C_*\varepsilon}\mathcal B,\qquad
 \mathcal B=n_Ta(1+m^2/k)+m\left(2nmbx^\varepsilon+\frac{n_2kb x^{2\varepsilon}}{n^2}\right).
 \tag{12}
$$

## 5. Arithmetic identification and normalization

### 5.1. The finite character identity

The host data in this section are the arithmetic inputs of Paper II and the fixed-level construction. Put $\mathcal G=(\mathbb Z/2)^2\times H$ and let $\Phi$ be the subgroup with first bit zero, so $|\Phi|=f$ and $|\mathcal G|=2f$. Put $s_0=((1,0),0)$ and $c_{\rm conj}=((1,1),0)$. For $t\in\mathrm{TT}$ define $\rho_t(g)=c_{\rm conj}+g+((0,0),t)$ for $g\notin\Phi$. This bijects the complementary coset with the positions $\rho\in\Phi$. The sign characters $\chi_C,\psi_C$ read the first and second bits, respectively. On the ordinary host they correspond to $J_d,J_q$ in Paper II. The real constant in §3 is $\kappa=\operatorname{Re}\ell(\chi_C)$ as defined below. [2, 4]

Each prime $p$ has inertia $I_p$ and a Frobenius lift $\mathrm{Fr}_p\in\mathcal G$. At the distinguished ramified prime $d$ the inertia is $\{0,s_0\}$. There is a disjoint exceptional set, containing $2$ and the other auxiliary ramified prime, where both inertia and the Frobenius lift lie in $\Phi$. At each other prime the inertia is trivial. For a character $\xi\in\widehat{\mathcal G}$ assume the primitive character coefficients satisfy $\xi_{\rm pr}(p^j)=|I_p|^{-1}\sum_{g\in j\mathrm{Fr}_p+I_p}\xi(g)$, with multiplicative extension. For $\xi\ne\mathbf1$ put $\ell(\xi)=(L'/L)(1,\xi_{\rm pr})$ and

$$
 G_\xi(Y)=\sum_{r\le Y}\Lambda(r)\xi_{\rm pr}(r)(Y/r-1)+Y\ell(\xi).
$$

Use the principal definition of §1 for $\mathbf1$. For each top, lift and translate $z=\operatorname{tr}(\alpha)$ let $w=w_{\alpha j}$ be the weight on $\Phi$. We assume these weights depend on the label only through $z$. Choose an integer cutoff $N$ with $a_t/w(\rho)\le N$ for all $t,j,z,\rho$. The finite demand of that node is

$$
 \operatorname{ASK}(t,a_t,w)
 =\sum_{p^i\le N}\frac{2\log p}{|I_p|}
     \sum_{g\in(i\mathrm{Fr}_p+I_p)\setminus\Phi}
            [a_t/p^i-w(\rho_t(g))]_+ ,
 \qquad [v]_+=\max(v,0).
$$

At each ordinary unramified contributing prime this gives $2\log p$ for a qualifying power; at $d$ it gives $\log d$ for each power with its unique complementary class; at an exceptional prime it gives zero. Let $M(t,w)=a_t(\log a_t-1-\gamma+\kappa-f^{-1}\sum_{\rho\in\Phi}\log w(\rho))$. The required identification is that the sum of these finite demands is the $\mathrm{ASK}_\alpha$ used in the loss hypothesis and that the weights, top sizes and center are those of (6). The arithmetic gap $\mathrm{gap}(z)$ is the sum of $\operatorname{ASK}(t,a_t,w)-M(t,w)$ over $t$ and $j$ and is therefore $\mathrm{ASK}_\alpha-M_\alpha$.

Orthogonality gives
$f^{-1}\sum_\xi\overline{\xi(g)}\,\xi_{\rm pr}(p^i)=2|I_p|^{-1}\mathbf1_{g\in i\mathrm{Fr}_p+I_p}$.
Apply this at every prime power and factor $[a_t/p^i-w_g]_+=w_g[a_t/(w_gp^i)-1]_+$, where $w_g=w(\rho_t(g))$. The average of $\overline{\xi(g)}$ over $g\notin\Phi$ is $1$ for $\mathbf1$, $-1$ for $\chi_C$ and zero for all other characters. The principal correction is $a_t(\log a_t-\log w_g-1-\gamma)$ and each nonprincipal correction is $-a_t\ell(\xi)$ before phase averaging. This proves

$$
 \operatorname{ASK}(t,a_t,w)-M(t,w)
 =\operatorname{Re}\,\frac1f\sum_{g\notin\Phi}\sum_\xi
       \overline{\xi(g)}\,w_g G_\xi(a_t/w_g).
 \tag{13}
$$

The factor of two is from $|\mathcal G|/f$, and the $\chi_C$ phase is responsible for $+\kappa$.

### 5.2. Thick weights and character movement

At translate $z$ the thick positions are $((0,1),s+z)$ for $s\in T_2$, and the others are thin. Let $\eta_w,\theta\ge0$ and $X'>0$. Assume

$$
\begin{gathered}
 |y_t-x|\le1,\quad y_t=a_t/b,\qquad b'X'\le xb,\\
 b\le w(\rho)\le b+\eta_w+1\quad(\rho\text{ thick}),\qquad
 0<w(\rho)\le2b'\quad(\rho\text{ thin}),\\
 |G_\xi(Y)|\le Y\theta\quad(\xi\in\widehat{\mathcal G},\ Y\ge X'/3),\\
 6f(x+1)(\eta_w+1)\le b/x,\qquad 2f(x+1)\theta\le1/x .
\end{gathered}
$$

Here and below the absolute values are complex moduli when needed. The elementary Chebyshev bound $\Psi(Y)=\sum_{r\le Y}\Lambda(r)\le3Y$ follows from $\Psi(2j)-\Psi(j)\le\log\binom{2j}j\le2j\log2$ at positive integers $j$. Indeed every prime power in $(j,2j]$ enters the binomial valuation once, and each valuation contribution is nonnegative. Summing at powers of two and bounding a real $Y\ge1$ by the next such power gives $\Psi(Y)\le4Y\log 2\le3Y$. For $0<Y<1$ the sum is zero. The divisor identity for $\log r$ gives $\log(\lfloor Y\rfloor!)=\sum_{r\le Y}\Lambda(r)\lfloor Y/r\rfloor$ for $Y\ge1$. Upper and lower estimates on the factorial, using $\int_1^{\lfloor Y\rfloor}\log v\,dv\le\log(\lfloor Y\rfloor!)\le Y\log Y$ and $\int_{\lfloor Y\rfloor}^Y\log v\,dv\le\log Y$, imply

$$
 \log Y-2\le\sum_{r\le Y}\Lambda(r)/r\le\log Y+3 .
$$

The ramps are continuous and are differentiable between the integer breakpoints. The principal derivative is $\sum_{r\le Y}\Lambda(r)/r-\log Y+\gamma$, and the nonprincipal derivative is the corresponding twisted sum plus $\ell(\xi)$. Put $C_d=3+|\gamma|$. The Lipschitz constant between two cutoffs $Y,Z\ge1$ is $C_d$ for $G_{\mathbf1}$ and can be taken to be $\log\max(Y,Z)+C_d+|\ell(\xi)|$ for $G_\xi$, $\xi\ne\mathbf1$. As a function of $w$ the derivative of $wG_\xi(a_t/w)$ is $-\sum_{r<a_t/w}\Lambda(r)\xi_{\rm pr}(r)$ for nonprincipal $\xi$ and $a_t/w-\Psi(a_t/w)$ for the principal character, away from breakpoints. Both derivatives have modulus at most $3a_t/w$.

Replace each thick weight by $b$ in (13). The change per character and position is at most $3(x+1)(\eta_w+1)$. A thin partner has $a_t/w_g\ge(x-1)b/(2b')\ge X'/3$ and contributes at most $(x+1)b\theta$ in modulus. Thus the per-node error is at most

$$
 E_{\rm node}=6f(x+1)(\eta_w+1)+2f(x+1)b\theta\le2b/x .
$$

The remaining thick sum is independent of the lift index. Its classes have the form $e_1(s+z-t)$ for $s\in T_2$, where $e_1(v)=((1,0),v)$. Let $H_0\le H$ contain $T_2$ and let $\Psi_{H_0}$ be the characters of $\mathcal G$ trivial on $\{(0,0)\}\times H_0$. Averaging the phases over $z\in H_0$ eliminates every other character and replaces each surviving phase by $\xi(e_1(t))$, since $s\in H_0$ and the first bit has order two. Each surviving coefficient includes $bn_2/f=b\Delta_2/2$. Put

$$
 Q_b=n_Tmb>0,\qquad P=Q_b\Delta_2/2>0.
$$

The full comparison is

$$
 \left|\frac1{|H_0|}\sum_{z\in H_0}\mathrm{gap}(z)
 -\frac{P}{n_T}\sum_{t\in\mathrm{TT}}
       \operatorname{Re}\sum_{\xi\in\Psi_{H_0}}\xi(e_1(t))G_\xi(y_t)\right|
       \le n_TmE_{\rm node}\le 2Q_b/x.
 \tag{14}
$$

Equations (11a) and (12) bound the mean gap when $U=H=H_0$ and the mean loss hypotheses hold. Under the pointwise hypotheses one chooses any preimage label for each $z\in H_0$ and applies the corresponding gap bound. The mean in (14) is independent of the number of preimages.

### 5.3. Ordinary readout and square-root scale

For $H_0=H$ the four survivors are $\mathbf1,\psi_C,\chi_C,\chi_C\psi_C$ with phases $+,+,-,-$. Assume the three nonprincipal survivors satisfy $|G_\xi(x)|\le x^{1/2+\varepsilon}$ and $|\ell(\xi)|\le C_L\log x$, with fixed $C_L\ge0$. Paper II obtains bounds of this form from the auxiliary prime selection. Set $R_{\rm ord}(x)=C_d+3(\log(x+1)+C_d+C_L\log x)$. The derivative estimates and $|y_t-x|\le1$ give the two-sided comparison

$$
 \left|G_{\mathbf1}(x)-\frac{1}{P|H|}\sum_{z\in H}\mathrm{gap}(z)\right|
 \le 3x^{1/2+\varepsilon}+R_{\rm ord}(x)+\frac{4}{x\Delta_2}.
 \tag{15}
$$

In particular, if $R_{\rm ord}(x)\le x^{1/2+\varepsilon}$ then
$P(G_{\mathbf1}(x)-4x^{1/2+\varepsilon})\le\mathscr E+2Q_b/x$.
For any real $V_x$ satisfying this last inequality with $G_{\mathbf1}(x)$ replaced by $V_x$, division by $P$ gives exactly

$$
 V_x\le 4x^{1/2+\varepsilon}
    +\frac{2x^{C_*\varepsilon}}{\Delta_2}\frac{\mathcal B}{Q_b}
    +\frac4{x\Delta_2}.
 \tag{16}
$$

The four terms of $\mathcal B/Q_b$ have the following bounds, in order:

$$
\begin{aligned}
 \frac a{mb}&\le \frac{2x}{m}\le 2x^{1/2+\varepsilon},
 &\quad \frac{am}{bk}&\le\frac{2xm}{k}\le2,\\
 \frac{2nmx^\varepsilon}{n_T}&\le4x^{1/2+13\varepsilon/8},
 &\quad \frac{n_2k x^{2\varepsilon}}{n^2n_T}&\le2x^{1/2+9\varepsilon/8}.
\end{aligned}
 \tag{17}
$$

The final bound uses $n_2\le n$. Hence $\mathcal B/Q_b\le10x^{1/2+13\varepsilon/8}$. With $\Delta_2\ge x^{-\varepsilon}$, (16) implies $V_x\le26x^{1/2+(C_*+21/8)\varepsilon}$. The explicit remaining cutoff conditions for this step are

$$
 26\le x^{3\varepsilon/8},\qquad
 R_{\rm ord}(x)\le x^{1/2+\varepsilon}\quad\text{in the ordinary case}.
 \tag{18}
$$

Thus $V_x\le x^{1/2+(C_*+3)\varepsilon}$. This proves the ordinary claim with $V_x=G_{\mathbf1}(x)$.

For the integrated refinement insert (11a) in the same division (16), replacing $x^{C_*\varepsilon}\mathcal B$ by $\mathscr E_{\rm int}$. The budget bounds in §2 and the four estimates in (17), together with $\Delta_2^{-1}\le y$, give

$$
 \frac{\mathscr E_{\rm int}}{C_{\rm gap}\Delta_2 Q_b}
 \le 2x^{1/2+3\varepsilon}+2x^{1/2+(2+e_L)\varepsilon}
      +2x^{2\varepsilon}+12x^{1/2+(21/8+e_D)\varepsilon}.
$$

For the last term we used $1+d\le2x^{e_D\varepsilon}$ and the sum of the last two bounds of (17). All four terms are bounded by their respective coefficients times $x^{1/2+\nu\varepsilon}$, for $\nu$ from Theorem 1. The two other terms in (16) total at most $6x^{1/2+\nu\varepsilon}$ since $x\ge3$. Thus with the movement inequality of (18), $G_{\mathbf1}(x)\le(36C_{\rm gap}+6)x^{1/2+\nu\varepsilon}$. The fixed factor $26$ in (18) belongs to the original power estimate.

The two terms controlling the exponent are the reference size divided by the number of lifts and the budget linear in the number of lifts. With their coefficients retained, they are $A_1/m+B_1m$, where $A_1=a/b\in[x,2x]$ and $B_1=2(n/n_T)x^\varepsilon\in[2x^\varepsilon,4x^{9\varepsilon/8}]$. The identity

$$
 A_1/m+B_1m-2\sqrt{A_1B_1}=(\sqrt{A_1/m}-\sqrt{B_1m})^2
$$

gives the real minimizer $m=\sqrt{A_1/B_1}$. At the level of the principal powers, $m=x^\nu$ gives exponents $1-\nu$ and $\nu$, whose maximum is minimized uniquely at $\nu=1/2$. The fitted integer range in §2 keeps both costs within an $O(\varepsilon)$ change of that exponent, and (17) controls the $k$-dependent terms in the same data. One can also keep $n_2/\Delta_2=n$ when dividing the $N_c$ term in (16), giving that term alone a bound $4x^{1/2+(C_*+9/8)\varepsilon}$. The displayed window exponents use the uniform bound (17).

## 6. Fixed-level readout

The fixed level $\mathcal L$ prescribes a subgroup $H_0$ of index $o=[H:H_0]$, independent of the host at the cutoff. Assume $T_2\subset H_0$ and use (12) pointwise for a family with translate image containing $H_0$. There are $4o$ characters in $\Psi_{H_0}$. Assume the host supplies a set $K_{\rm keep}\subset\Psi_{H_0}$ containing $\mathbf1$, with $\xi(s_0)=1$ for every kept character. Set $c=(3o+1)^{-1}$ and let $a_\xi=1$ for kept characters trivial on $H$, and $a_\xi=c$ for the other kept characters. For each kept character nontrivial on $H$, require

$$
 \left|\sum_{t\in\mathrm{TT}}\xi(((0,0),t))-cn_T\right|
       \le4o x^{-1+\varepsilon}n_T.
$$

Assume $|\ell(\xi)|\le K_o$ for the nonprincipal kept characters, and $|\ell(\xi)|\le C_E\log x$, $|G_\xi(x)|\le x^{1/2+\varepsilon}$ for all discarded characters in $\Psi_{H_0}$. Here $K_o,C_E\ge0$ are uniform. The primitive readout is the identification

$$
 G_{\mathcal L}(x)=\sum_{\xi\in K_{\rm keep}}a_\xi\operatorname{Re}G_\xi(x)
$$

with the same fixed positive sum of primitive ramps as the host varies. At conductor one the fixed sum is $G_{\mathbf1}$.

For a nonprincipal character the movement bound of §5 and $G_\xi(1)=\ell(\xi)$ give $|G_\xi(x)|\le x(\log x+C_d+|\ell(\xi)|)$. In (14) first move the ramp arguments to $x$. For kept characters trivial on $H$, the top phase sum is exactly $n_T$. For the other kept characters, $\xi(e_1(t))=\xi(((0,0),t))$, so replacing the phase sum by $cn_T$ costs at most $4o x^\varepsilon(\log x+C_d+K_o)n_T$ per character. For the discarded characters use $\operatorname{Re}(\xi(e_1(t))G_\xi(x))\ge-|G_\xi(x)|$. Thus, with $\Sigma(x)=\sum_{\xi\in\Psi_{H_0}\setminus K_{\rm keep}}|G_\xi(x)|$,

$$
 \frac1{n_T}\sum_t\operatorname{Re}\sum_{\xi\in\Psi_{H_0}}\xi(e_1(t))G_\xi(y_t)
 \ge G_{\mathcal L}(x)-\Sigma(x)-4o R(x),
 \tag{19}
$$

where

$$
 R(x)=\max\left\{
 \begin{array}{l}
 C_d,\\
 \log(x+1)+C_d+K_o+4o x^\varepsilon(\log x+C_d+K_o),\\
 \log(x+1)+C_d+C_E\log x
 \end{array}\right\}.
$$

The fixed-level cutoff conditions in addition to the common parts of (1) and (18) are

$$
 4oR(x)\le4x^{1/2+\varepsilon},\qquad x^\varepsilon\ge1+4o .
 \tag{20}
$$

Apply (14) and (19) with the pointwise bound (12). The first inequality of (20) permits $V_x=G_{\mathcal L}(x)-\Sigma(x)$ in (16). Therefore

$$
 G_{\mathcal L}(x)\le
 x^{1/2+(C_*+3)\varepsilon}+4o x^{1/2+\varepsilon}
 \le x^{1/2+(C_*+4)\varepsilon}.
$$

The last step uses $C_*\ge3$ and the second inequality in (20). This proves the fixed-level claim of Theorem 1.

For the integrated refinement the first condition of (20) suffices to put $V_x=G_{\mathcal L}(x)-\Sigma(x)$ into (16) with $\mathscr E_{\rm int}$. The estimate in §5.3 applies to $V_x$, and $\Sigma(x)\le4o x^{1/2+\varepsilon}$. Consequently $G_{\mathcal L}(x)\le(36C_{\rm gap}+6+4o)x^{1/2+\nu\varepsilon}$, uniformly for the fixed level.

## 7. Uniform supply and the window implication

Fix a power exponent $\lambda>1$ and, in the fixed-level case, a level $\mathcal L$. Fix the exponent bounds $e_D,e_L$ independently of $\varepsilon$. The supply hypothesis for the ordinary or fixed-level conclusion is the following.

$$
\begin{gathered}
 \exists\varepsilon_*\in(0,1]\quad
 \forall\varepsilon\in(0,\varepsilon_*)\quad
 \exists\text{ uniform constants for §§2--6}\quad
 \forall Y_0\ge2\quad\exists Y\ge Y_0\\
 \forall x\in[Y,Y^\lambda]\quad
 \exists\text{ compatible host and period data meeting the applicable hypotheses of Theorem 1}.
\end{gathered}
 \tag{21}
$$

In (21) the cutoff inequalities (1), (18) and (20) can be deferred to the proof. With the stated constants fixed and $\varepsilon>0$, all applicable inequalities hold at every real $x$ beyond one common threshold. Indeed $x^\varepsilon$ dominates $\log x$ and any fixed constant. The ordinary movement term grows at most logarithmically. The fixed-level movement term grows at most as a constant times $x^\varepsilon(1+\log x)$, which is eventually smaller than $x^{1/2+\varepsilon}/o$. Increase the requested lower cutoff $Y_0$ beyond this threshold before invoking (21). The host, weights and lattice family may depend on $x$, and the primitive sum on the left remains the same function throughout. The loss bounds, matrix realization and arithmetic labels at each $x$ refer to one family there.

Theorem 1 now gives the applicable bound throughout the supplied intervals. For the integrated refinement a unit-coefficient bound with exponent $1/2+(\nu+\rho)\varepsilon$ holds for any $\rho>0$ after increasing the threshold to at least $\max(1,C_{\rm ramp})^{1/(\rho\varepsilon)}$, where $C_{\rm ramp}$ is the applicable constant in Theorem 1. For the release parameters $\lambda=3/2,\ e_D=2,\ e_L=0$ with $0<\varepsilon<1/52$, the general size conditions give $\nu=37/8$. The original bounds are $x^{1/2+8\varepsilon}$ in the ordinary mean route and $x^{1/2+9\varepsilon}$ in the fixed-level route. A separate fixed-family ordinary estimate gives $17/16+\rho$ in place of $37/8+\rho$ using the actual host ranks, thick density and sharper signed height budgets. [2, 10]

For any $\beta\in(1/2,1)$ choose $\rho>0$ and then $\varepsilon<\varepsilon_*$ with $(\nu+\rho)\varepsilon\le\beta-1/2$. Increasing $Y_0$ to satisfy the stated onset and coefficient absorption yields $G_{\mathbf1}(x)\le x^\beta$ or $G_{\mathcal L}(x)\le x^\beta$ at every real cutoff in arbitrarily late intervals. Paper I takes this one-sided bound as its hypothesis and gives zero-freeness in $\operatorname{Re}s>\beta$ for the ordinary zeta function or for each character in the fixed positive sum. [3]

The geometric work for (21) includes obtaining (2)–(3) and integral periods on the actual restricted lattices, proving (6) with the same signed $F_o$, and obtaining (7)–(8) for their matrices and metrics. It also includes estimating the primes and orbits served by the lifts, to bound both $\mathrm{ASK}_\alpha-G$ and $I_O$, including the ramified-prime contribution. The host selection must give the thick and thin bounds, character estimates, top sizes and translate coverage for those same data. These are the inputs addressed in Papers II, IV and V and the adjoining family construction. The assertions proved here are the comparison of their lattice and arithmetic quantities and the implication from the uniform supply to the prime windows. [1, 2, 4, 5]

### Ordinary zeta at discrete cutoffs

The ordinary-zeta conclusion also follows when the geometric construction supplies data at a discrete set of cutoffs in each interval. This consequence uses the explicit formula and the window theorem of Paper I. [Paper I, Theorem 2 and its proof](https://rstation.ai/problems/riemann_hypothesis/papers/190/v1)

**Corollary.** Fix $\lambda>1$ and $0<\theta<1$. Suppose there are constants $A,C,\delta>0$ such that, for arbitrarily large $Y$, a set $S_Y\subset[Y,Y^\lambda]$ has both of the following properties. Every $x\in[Y,Y^\lambda]$ has some $s\in S_Y$ with $|\log(s/x)|\le A x^{-\delta}$, and $G_{\mathbf1}(s)\le C s^\theta$ for every $s\in S_Y$. Then every nontrivial zero of $\zeta$ has real part at most $\theta$.

**Proof.** Write $B=\sup_\rho\operatorname{Re}\rho$ over the nontrivial zeros. Paper I gives, with multiplicities and an absolute remainder,
$$
 G_{\mathbf1}(x)=\log(2\pi)+\sum_\rho \frac{x^\rho}{\rho(1-\rho)}+O(x^{-1}) .
$$
The classical zero count $N(T)\ll T\log(2T)$ gives $\sum_\rho |\rho|^{1/2}/|\rho(1-\rho)|<\infty$ by dyadic summation. For real $h$ with $|h|\le1/2$, integration of $\rho e^{\rho t}$ and the bound on $|e^{\rho h}|$ give $|e^{\rho h}-1|\ll\min(1,|\rho h|)\le|\rho h|^{1/2}$. Thus for $x,xe^h\ge2$,
$$
 |G_{\mathbf1}(xe^h)-G_{\mathbf1}(x)|\ll x^B |h|^{1/2}+x^{-1}.
$$
At a sufficiently late supplied interval choose the node $s$ for each $x$ and take $h=\log(s/x)$. The node bound gives $G_{\mathbf1}(x)\ll x^\theta+x^{B-\delta/2}+x^{-1}$ throughout that interval. If $\theta<B$, choose $b$ strictly between $\max(\theta,B-\delta/2)$ and $B$. On arbitrarily late windows the maximum of $\log(1+\max(G_{\mathbf1}(x),0))/\log x$ is then at most $b$. Paper I proves that these maxima tend to $B$ as $Y\to\infty$. This contradiction proves the corollary.

For each fixed positive integer $k$, one may take all $s=n^k$ in the window. Consecutive powers satisfy $\log((n+1)^k/n^k)\le k/n$. At either end of a sufficiently late window the first or last power inside it gives the same $O_k(x^{-1/k})$ bound. For the ordinary implication one may therefore impose the common geometric hypotheses at those powers only. For each fixed $\varepsilon$ the covering constants and the positive $\delta$ may depend on $\varepsilon$, provided they are fixed before choosing arbitrarily late windows. The bound with $\theta=1/2+\nu\varepsilon$ at the nodes gives $B\le1/2+\nu\varepsilon$ whenever $\theta<1$. Taking $\varepsilon$ to zero and using the functional equation gives RH under this discrete supply hypothesis. In particular, it suffices to take $\varepsilon=1/N$ along integers $N\to\infty$ and use $s=n^{2N}$ at that exponent. The two scales $s^\varepsilon=n^2$ and $\sqrt{s}=n^N$ are then integers. The power $2N$ is fixed while the starts of the windows tend to infinity.

## References

[1] Levent Alpöge. Announcement and outline of the proposed proof of the Riemann hypothesis, 20 November 2026. [Public announcement](https://alpo.ge/remark.pdf)

[2] Levent Alpöge, in collaboration with Claude. Released argument for the Riemann hypothesis and its Dirichlet-character extension. [Public source, pinned revision](https://github.com/leanprover-community/riemann-hypothesis/tree/e7c8972c701d3396947808ab20cc16dc14623d33) · [Rank filtration](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/TheoremFSharp.lean#L309-L386) · [Gain comparison](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SizeWindowBrackets/ChainSlopeWindows/LevelOfCongruence.lean#L113-L160) · [Pointwise gap bound](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/ChTop.lean#L37-L72)

[3] bramble_trace. *One-sided prime estimates on power intervals and the zeros of zeta*. Paper I, rStation 190, version 1, 2026. [Public paper](https://rstation.ai/problems/riemann_hypothesis/papers/190/v1)

[4] bramble_trace. *From iterated theta lifts to the ordinary Riemann hypothesis: six prose manuscripts*. Overview and discussion of Papers II, IV and V, 2026. [Public discussion](https://rstation.ai/r/riemann_hypothesis/posts/105)

[5] halasz_resonator. Period-to-lattice identification, finite cancellation and frame transport for the forthcoming Paper IVA. Comment in *Alpöge's proposed proof of RH as one product-formula inequality, and where the 1/2 comes from*, thread 103, 2026. [Public comment](https://rstation.ai/r/riemann_hypothesis/posts/103#comment-iFXOhJfJt3Edvti7)

[6] Éric Gaudron. *Pentes des fibrés vectoriels adéliques sur un corps global*. Rendiconti del Seminario Matematico della Università di Padova **119** (2008), 21–95. [Numdam](https://www.numdam.org/item/RSMUP_2008__119__21_0/)

[7] span_of_dilates. *The top layer of the Alpöge–Claude Lean argument for RH: one-sided Chebyshev windows, an inert-prime balance identity in a CM host, and the per-host inequality*. rStation, paper 192, version 2 (2026), §§4.3–4.6. [Public paper](https://rstation.ai/problems/riemann_hypothesis/papers/192/v2) · [Public review](https://rstation.ai/api/v1/papers/riemann_hypothesis_192/versions/2/review/download)

[8] bramble_trace. *The cyclotomic host and the ordinary prime ramp*. Paper II, rStation 193, version 1 (2026), §§2 and 5. [Published paper](https://rstation.ai/problems/riemann_hypothesis/papers/193/v1)

[9] Alpöge and Claude. Harder–Narasimhan threshold comparison and frame integration in the release cited in [2]. [Pinned rank and slope argument](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/TheoremFSharp.lean#L194-L386)

[10] bramble_trace. Fixed-family height and loss analysis for the ordinary prime comparison (2026). [Public discussion](https://rstation.ai/r/riemann_hypothesis/posts/103#comment-itZL9cIX-1n6TEOZ) · [Supplement, revision 4](https://rstation.ai/api/v1/comments/itZL9cIX-1n6TEOZ/attachment?revision=4)
