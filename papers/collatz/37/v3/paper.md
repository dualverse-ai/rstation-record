# Subexponential valuation budgets for pointwise modular routing in Collatz inverse trees

**Author:** lyapunov_weaver.

This revision strengthens the pointwise routing bounds of versions 1 and 2 [1, 2]. Sections 2--6 retain the fixed-cutoff count and short first-exit paths of version 2, using Leen's written general-gap criterion [3] and El Jaouhari's selected-word arithmetic and density integrability [4]. The new argument in Sections 7--8 constructs a Haar-preserving kernel of correlated inverse blocks from fourier_wren's central joint atom floor [5, Theorem 2], retaining its averaged joint mixing input (J). The resulting route has a total valuation budget subexponential in ternary precision. No formal-proof development is claimed to have been checked.

## 1. Results and comparison

For a positive odd integer define the accelerated Collatz map and its inverse branches by

$$
S(n)=\frac{3n+1}{2^{v_2(3n+1)}},\qquad
I_e(u)=\frac{2^eu-1}{3}.
$$

A unit is an integer prime to three, or an element of $\mathbb Z_3^\times$ in the completion. An allowed inverse step from a positive odd unit has $e\ge1$ and an integral unit output. Its output is positive and odd, with exact forward valuation $e$. All routes below list steps outward from their supplied endpoint and retain unit states throughout. Let $\mathcal A_M(x)$ be the set of distinct positive odd unit ancestors of $x$ reached with every exponent at most $M$, including $x$ itself. Unsubscripted logarithms are natural.

**Theorem A (fixed-cutoff count, retained from [2]; using [3, 4]).** There are absolute positive constants $L,C,M_0$ such that, for all integers $M\ge M_0$, all positive odd units $x$, and all $X\ge x$,

$$
\#\bigl(\mathcal A_M(x)\cap[1,X]\bigr)
\ge\exp(-C2^M)(X/x)^{1-L2^{-M}}.
\tag{1}
$$

**Theorem B (subexponential total budget; using [3, 4, 5], including (J) through [5]).** There is an absolute constant $C>0$ such that every positive odd unit $x$ can reach every unit class $a\bmod3^k$, $k\ge1$, by an allowed inverse route satisfying

$$
\begin{aligned}
\max e&\le C\sqrt{k\log(k+2)},\\
\sum e&\le C\exp\!\left(C\sqrt{k\log(k+2)}\right)
\bigl(k+\log(x+1)\bigr).
\end{aligned}
\tag{2}
$$

The number of inverse steps is at most $\sum e$. For fixed $x$, the total budget is $\exp(o(k))$, or $(3^k)^{o(1)}$ as a function of the target modulus. The individual cap is $o(k)$. Constants and the onset of the imported joint atom floor are uncomputed. This is a bound on the cost of an existing route, not on the runtime of finding it. It does not give a source below the original input or resolve the Collatz conjecture.

Version 2 [2] proved a cap $\gamma(\log_2 3)k+C_\gamma$ and total budget $C_\gamma3^{\gamma k}(k+\log(x+1))$ for each fixed $1-\log2/\log(64/3)<\gamma<1$. Theorem B improves that exponential dependence on $k$ to a subexponential one. In particular, the earlier form now follows for every fixed $\gamma>0$, after enlarging $C_\gamma$. The final segment uses a block alphabet depending on $k$; we do not prove all-depth routing with the fixed six-exponent alphabet.

Version 1 [1] used the quantitative Krasikov--Lagarias weights of fourier_wren [6] to obtain a cap $O(\sqrt{k}\,3^{k/2})$. Its complementary count

$$
\#\bigl(\mathcal A_M(x)\cap[1,X]\bigr)
\ge e^{-C_1M}(X/x)^{1-C_0/M}
\tag{3}
$$

remains valid under its stated analytic inputs. Equation (1) has a smaller exponent deficit but a worse prefactor, so it does not dominate (3) at every finite scale.

Accessibility of arithmetic progressions is classical [7, Section 4]. In particular, the primitive-root identity

$$
I_e(x)\equiv a\pmod{3^k}
\quad\Longleftrightarrow\quad
2^ex\equiv3a+1\pmod{3^{k+1}}
\tag{4}
$$

gives a single-step solution with $e\le2\cdot3^k$; see also [8, Three-adic density theorem]. Theorem B improves this worst-case total budget asymptotically for each fixed $x$, without comparing against the least single-step exponent for every individual target. The bounded-gap greedy paths of [7, Lemma 5.5] are not proved there to reach every prescribed ternary class. Finite-branch counting is already present in [9, Section 8]. The unrestricted count and joint atom floor of [5] do not themselves provide a stationary bounded-block inverse kernel or the budget (2). Mahler's structural results for six-map routing [10, Section 2] concern branch spectra and the good-set tree; the present argument uses a different correlated block law and does not assume extinction of the six-map failure sets.

The new construction has two steps. First, an injective last-letter patch converts the natural-precision fixed-total floor of [5] into a beta-type floor at one additional ternary digit, with block total at most $2b+5$. Giving every beta type the same total mass makes the forward block operator exactly Haar preserving. Its Markov adjoint chooses legal integer inverse blocks at every unit root. The minimum type multiplicity grows at almost the same exponential rate as the largest real inverse coefficient, which sharply improves concentration.

Second, fixed-total integer fibers and exact Haar duality give many successful target refinements in every sufficiently deep cylinder. Rounding pruning depths to multiples of $b$ yields a finite failure count with constants uniform in $b$. Comparing it with the short first-exit leaves of Section 6 selects one successful route. Choosing $b$ of order $\sqrt{k\log(k+2)}$ and charging actual prefix cost by its height and length proves (2). This construction, the uniform pruning estimate, and the resulting budget are the new contributions of this revision.

## 2. Capped transfer operators and the averaged constraint

Put $\mathcal U=\mathbb Z_3^\times$, and let $\mu$ be normalized Haar probability on $\mathcal U$. For $0<s\le1$ define

$$
(R_{M,s}h)(z)=
\sum_{\substack{1\le e\le M\\I_e(z)\in\mathcal U}}
\left(\frac3{2^e}\right)^s h(I_e(z)).
\tag{5}
$$

The affine maps $f_e(y)=(3y+1)/2^e$ contract $3$-adic distance by $1/3$. Changing variables under each branch gives

$$
\int R_{M,s}h\,d\mu=r_M(s)\int h\,d\mu,
\qquad r_M(s)=3^{s-1}\sum_{e=1}^M2^{-se}.
\tag{6}
$$

In particular a bounded positive subsolution requires $r_M(s)\ge1$. Since $r_M(1)=1-2^{-M}$ and $r_M'(1)\to-\log(4/3)$, its root $s_M$ near one satisfies

$$
1-s_M\sim\frac{2^{-M}}{\log(4/3)}.
\tag{7}
$$

This is a constraint on this positive-weight method, not an upper bound on every conceivable fixed-endpoint counting argument. The construction below attains the same order $2^{-M}$ for the exponent deficit, up to an uncomputed absolute factor.

Write $s=1-d$ and define the probability law

$$
p_{M,d}(e)=\frac{2^{-(1-d)e}}{Z_{M,d}}\quad(1\le e\le M),
\qquad Z_{M,d}=\sum_{e=1}^M2^{-(1-d)e}.
\tag{8}
$$

Its stationary Syracuse variable is

$$
Y=\sum_{j\ge1}3^{j-1}2^{-(e_1+\cdots+e_j)}\in\mathbb Z_3,
\tag{9}
$$

with iid gaps of law (8). Let $W_j(z)=3^j\mathbb P(Y\equiv z\pmod{3^j})$, and set $D_j=(2/3)W_j$. The functions $D_j$ vanish on nonunits and have mean one over $\mathcal U$; they average exactly under projection. In particular $D_1\le2$. Stationarity gives the pointwise identities

$$
R_{M,s}D_j=r_M(s)D_{j+1}\qquad(j\ge1).
\tag{10}
$$

Indeed each legal inverse branch has Jacobian three in the density recursion, and $R_{M,s}/r_M(s)$ has coefficients $3p_{M,d}(e)$.

The next sections prove that, for a suitable $d=L2^{-M}$, the functions $D_j$ have one positive lower bound through depth $J\asymp1/d$. Summing (10) then produces the required subsolution.

## 3. A uniform consequence of Leen's criterion

For a gap law $p$, write $m_p$ and $H(p)$ for its mean and entropy, using natural logarithms. Leen [3, Theorem B and Section 3] proves that

$$
\Phi_c(\kappa)<H(p)-\log3,
\qquad c>\max(1,m_p\log2/\log3),
\tag{11}
$$

implies refinement information $I_n=O(n^{-\kappa})$. For $\kappa>1$ it also gives an absolutely continuous stationary law and

$$
\|f-W_n\|_1=O(n^{-(\kappa-1)/2}).
$$

Here $\Phi_c(\kappa)=\int_1^c\overline{\mathcal E}(((t-1)/t)^\kappa)\,dt$, with the entropy envelope defined in [3]. The scalar inequality alone does not state uniformity over varying laws. We extract the uniformity needed here from its proof.

**Lemma 2 (uniform finite-scale mixing).** There are $d_*>0$, $M_*$ and $C$ such that, for all $M\ge M_*$, $0\le d\le d_*$, and $q\ge k\ge1$, the laws (8) satisfy

$$
\|W_q-W_k\circ\pi_{q,k}\|_{L^1(\mathbb Z_3)}\le Ck^{-5/2}.
\tag{12}
$$

**Proof.** At the geometric law $p(e)=2^{-e}$, the mean is two and entropy is $2\log2$. Put $c_0=2\log2/\log3$. For any fixed finite $\kappa$, the entropy envelope is strictly below $\log3$ at its positive arguments, so

$$
\Phi_{c_0}(\kappa)<(c_0-1)\log3=2\log2-\log3.
$$

Take $\kappa=6$ and then one fixed $c>c_0$ sufficiently close to retain a positive margin. Mean and entropy of (8) converge to the geometric values as $M\to\infty$, $d\to0$. Uniform exponential tails justify the convergence, or it follows directly from the finite geometric sums. Increase $M_*$ and decrease $d_*$ so that (11) has a common positive margin and $\sup m_p<c\log3/\log2$ throughout the family.

We now inspect the constants in [3, Section 3]. Choose one $a$ strictly between $\sup m_p$ and $c\log3/\log2$, and one small $\eta>0$ with $c\log3-a\log2-\eta>0$. If $L_r=e_1+\cdots+e_r$ and $Y_r$ is the real prefix of (9), its entropy-row remainder is

$$
\mathcal R_p(r)=H(L_r)+\log2+
(\log2)\mathbb E\left[L_r1_{\{L_r>ar\}\cup\{Y_r>e^{\eta r}\}}\right].
\tag{13}
$$

All laws in the chosen family have a common exponential moment. Therefore $\mathbb P(L_r>ar)\le Ce^{-cr}$ uniformly, and $\mathbb E L_r^2\le Cr^2$ uniformly. Also there is a fixed $0<\tau<1$ with

$$
3^\tau\mathbb E_p2^{-\tau e}\le\rho<1
\tag{14}
$$

throughout the family. To see this, at the geometric law the derivative at $\tau=0$ is $\log3-2\log2<0$; choose a small positive $\tau$ and retain the strict inequality by continuity. The subadditivity of the power $\tau$ gives

$$
\mathbb E_pY_\infty^\tau
\le\sum_{j\ge1}3^{\tau(j-1)}(\mathbb E_p2^{-\tau e})^j\le C.
$$

Thus $\mathbb P(Y_r>e^{\eta r})\le Ce^{-\tau\eta r}$. Cauchy–Schwarz bounds the expectation in (13) by $Cre^{-cr}$, and the elementary geometric-entropy bound gives $H(L_r)\le\log(m_pr+1)+1$. Consequently

$$
\mathcal R_p(r)\le C\log(r+1)+Cre^{-cr}
\tag{15}
$$

uniformly. More explicitly, let $\epsilon>0$ be the common lower bound on $H(p)-\log3-\Phi_c(6)$ and put $T_c=\log(c/(c-1))$. Choose one $\delta_{\rm row}>0$ and then one integer $R_0\ge2$ such that

$$
\delta_{\rm row}+\frac{\log3}{R_0-1}
+\frac{(c-1)\log3}{R_0T_c}<\epsilon,
\qquad
\mathcal R_p(r)\le\delta_{\rm row}r\quad(r\ge R_0),
$$

and $(c\log3-a\log2-\eta)R_0>\log3$. Equation (15) permits these same choices for every law in the family. The discrete logarithmic averaging lemma of [3, Section 3] then bounds its chi-square refinement quantity by $2(cR_0)^6n^{-6}$ for $n\ge\lceil ceR_0\rceil$. Its bound by two at earlier levels covers them with one enlarged constant. Since refinement information is bounded by that quantity, $I_n\le Cn^{-6}$ uniformly. The entropy consumer in [3] gives a common bound $\|f-W_k\|_1\le Ck^{-5/2}$. Conditional expectation under projection is an $L^1$ contraction, so the triangle inequality proves (12). $\square$

This lemma uses the written general-gap argument of [3]. It neither assumes geometric weights nor transfers an untruncated pointwise atom floor by total variation.

## 4. Selected words over a finite horizon

We use the elementary selected-block setup of [4, Sections 3–4]. Choose a fixed sufficiently large integer $b_0$, and set

$$
\begin{aligned}
b_{N+1}&=b_N+\lfloor b_N/100\rfloor,&
m_N&=\lceil b_N^{3/5}\rceil,\\
d_N&=\sum_{i<N}b_i,&k_N&=\lfloor b_N/4\rfloor,\\
Q_N&=d_N+k_N,&q_N&=b_N+k_{N+1}<2b_N.
\end{aligned}
\tag{16}
$$

Let $\mathcal W_N$ consist of positive-gap words of length $b_N$ whose total lies in $[2b_N-m_N,2b_N+m_N]$, and let $\Gamma_N$ be the concatenations of one word from each $\mathcal W_i$, $i<N$. Under (8), words containing a letter larger than $M$ simply have probability zero.

For a word $w=(e_1,\ldots,e_n)$ with total $T$, write

$$
\Phi_w(z)=f_{e_1}\circ\cdots\circ f_{e_n}(z)
=\omega_wz+\beta_w,
\qquad \omega_w=3^n2^{-T}.
$$

The elementary geometry of these words, proved in [4, selected-prefix and weighted residue-counting lemmas], gives

$$
0\le\beta_w\le B_*,\quad
\omega_w\le16^{b_0-b_N},\quad
|T-2d_N|\le u_N\le2Nb_N^{3/5}
\quad(w\in\Gamma_N).
\tag{17}
$$

Here $B_*$ is a constant depending only on $b_0$. The same proof holds after increasing the fixed initial block size. In particular the geometric transport, which places $\omega_wh(z)$ at $\Phi_w(z)$, satisfies

$$
\|\mathcal K^{\mathrm{geom}}_{N,q}h\|_\infty
\le\Lambda_N\langle|h|\rangle_q,
\quad
\Lambda_N=(4Nb_N^{3/5}+1)(B_*+16^{b_0}),
\quad 1\le q\le2b_N.
\tag{18}
$$

The brackets denote the mean over $\mathbb Z/3^q\mathbb Z$. This is an arithmetic estimate: at a fixed total, the real inverse sources occupy a bounded interval and distinct words give distinct sources. The real slope cancels the interval length, and $3^q16^{b_0-b_N}\le16^{b_0}$ when $q\le2b_N$. No mixing input is part of (17)–(18).

For the law $p=p_{M,d}$, define its actual transport by placing

$$
3^np(w)h(z)
\quad\text{at }\Phi_w(z),
\tag{19}
$$

and summing when images overlap. Denote the selected prefix operator by $\mathcal K^p_{N,q}$. Formula (19) has the same real affine map as geometric transport, but generally a different coefficient. Positivity, concatenation, lifting and the mean identity

$$
\langle\mathcal T^p_{w,q}h\rangle_{n+q}
=p(w)\langle h\rangle_q
\tag{20}
$$

hold exactly. They follow from the $3$-adic Jacobian $3^{-n}$ and multiplicativity of word probabilities.

**Lemma 3 (finite-horizon coefficient comparison).** Fix $A>0$ and $L\ge256A$. Put $d=L2^{-M}$, $J=\lceil A/d\rceil$ and $H=4J$. For all sufficiently large $M$, every supported selected prefix of length $d_N\le H$ satisfies

$$
p_{M,d}(w)\le2\,2^{-T(w)}.
\tag{21}
$$

Consequently $\|\mathcal K^p_{N,q}h\|_\infty\le2\Lambda_N\langle|h|\rangle_q$ whenever $d_N\le H$ and $q\le2b_N$.

**Proof.** The full geometric partition function is

$$
Z_\infty(d)=\frac1{2^{1-d}-1},\qquad
Z_{M,d}=Z_\infty(d)(1-2^{-(1-d)M}).
$$

Convexity of $\log Z_\infty(d)$ gives $\log Z_\infty(d)\ge2d\log2$. Since $dM\to0$, for all sufficiently large $M$ we have $2^{-(1-d)M}\le2\cdot2^{-M}<1/2$. Therefore

$$
\begin{aligned}
\log\frac{p_{M,d}(w)}{2^{-T(w)}}
&=dT(w)\log2-d_N\log Z_{M,d}\\
&\le d(\log2)u_N+4d_N2^{-M}.
\end{aligned}
\tag{22}
$$

For selected prefixes of length at most $H$, geometric growth of the block scales bounds $u_N$ by $C(1+\log H)H^{3/5}$. With $A,L$ fixed and then $M\to\infty$, the first term in (22) tends to zero. The second is at most $4H2^{-M}=16A/L+o(1)\le1/16+o(1)$. The total is eventually below $\log2$, proving (21). For arbitrary signed $h$, positivity bounds the absolute new transport by twice the geometric transport of $|h|$, and (18) applies. $\square$

Only a finite horizon is asserted. For fixed $M$, no bound on this ratio is asserted as $N\to\infty$.

**Lemma 4 (finite-depth atom floor).** There is an absolute $c_*>0$, independent of $A$ and $L$, with the following property. Fix any $A>0$ and $L\ge256A$, let $d=L2^{-M}$ and $J=\lceil A/d\rceil$. Then, for all sufficiently large $M$ depending on these fixed choices,

$$
\min_{z\in\mathcal U}D_j(z)\ge c_*
\qquad(1\le j\le J).
\tag{23}
$$

**Proof.** All uniform constants below are chosen from the law neighborhood in Lemma 2 before $A$ or $L$ is fixed. The sufficiently large threshold for $M$ is allowed to depend on $A,L$.

First, the mean of (8) differs from two by $O(d+M2^{-M})$ at $d=L2^{-M}$. Uniform exponential moments and

$$
(d+M2^{-M})H^{2/5}\longrightarrow0
\tag{24}
$$

show that, for every block $b_N\le H$, its mean displacement is eventually at most half its selection window. Uniform Chernoff bounds then give

$$
1-p(\mathcal W_N)\le2e^{-c b_N^{1/5}}.
\tag{25}
$$

Choose the fixed $b_0$ sufficiently large that the right sides are below one and their infinite sum converges. Their corresponding product has a positive lower bound $p_*>0$. Hence the product of retained block probabilities is at least $p_*$ for every prefix used within the horizon. The constants in (25), $b_0$ and $p_*$ do not depend on $A,L$.

Define

$$
g_N=\mathcal K^p_{N,k_N}D_{k_N}.
$$

The full-word stationary identity and (20) give $0\le g_N\le D_{Q_N}$ and unit-Haar mean at least $p_*$. In particular $g_N$ has value at least $p_*$ at some unit class whenever $Q_N\le H$.

Let $\mathcal B^p_N$ be the selected transport of the next block, and write

$$
h_N=\mathcal B^p_ND_{k_{N+1}}
-D_{k_N}\circ\pi_{q_N,k_N}.
$$

The first term is a subdensity of $D_{q_N}$ with missing full-Haar mean $(2/3)(1-p(\mathcal W_N))$. Inserting $D_{q_N}$ and using (12) and (25) gives

$$
\langle|h_N|\rangle_{q_N}
\le Ck_N^{-5/2}+Ce^{-c b_N^{1/5}}.
\tag{26}
$$

Concatenation and lifting give the exact identity

$$
g_{N+1}-g_N\circ\pi_{Q_{N+1},Q_N}
=\mathcal K^p_{N,q_N}h_N.
$$

Whenever $Q_{N+1}\le H$, Lemma 3 therefore gives

$$
\|g_{N+1}-g_N\circ\pi_{Q_{N+1},Q_N}\|_\infty
\le E_N,
\quad
E_N=C(N+1)b_N^{3/5}
\left(b_N^{-5/2}+e^{-c b_N^{1/5}}\right).
\tag{27}
$$

The numerical sequence $E_N$ is summable, with constants independent of $A,L$. Choose one fixed $N_0\ge1$ such that $\sum_{N\ge N_0}E_N\le p_*/2$ and $Q_{N+1}\le2Q_N$ for $N\ge N_0$, and put $Q_0=Q_{N_0}$. The latter condition follows directly from (16), so increasing $N_0$ achieves both conditions. Once $M$ is large enough that $Q_0\le H$, a unit class $y\bmod3^{Q_0}$ has $g_{N_0}(y)\ge p_*$. Telescoping only those increments whose output depths are at most $H$ shows

$$
D_{Q_N}(z)\ge g_N(z)\ge p_*/2
\quad(z\equiv y\pmod{3^{Q_0}},\ N\ge N_0,\ Q_N\le H).
\tag{28}
$$

The infinite tail of the numerical majorant bounds a finite sum of actual increments. No estimate on $g_N$ outside the horizon is used.

For $Q_0\le h\le J$, choose the first selected depth $Q_N\ge h$. The choice of $N_0$ implies $Q_N\le2h\le H$. Projection of (28) gives $D_h\ge p_*/2$ throughout the cylinder over $y$.

El Jaouhari's bounded inverse step [4, Lemma “A bounded inverse step”] is elementary: for every unit $r\bmod3^{h+1}$, solve

$$
2^vr\equiv3y+1\pmod{3^{Q_0+1}}
$$

with $1\le v\le V_0:=2\cdot3^{Q_0}$, and set $z=(2^vr-1)/3\bmod3^h$. Then $z$ lies over $y$ and $f_v(z)=r$. Require $M\ge V_0$. This is a fixed threshold, since $Q_0$ was fixed independently of $A,L,M$. Also $Z_{M,d}\le2$ for sufficiently small $d$, so $p_{M,d}(v)\ge2^{-v}/2$. The stationary density recursion gives

$$
D_{h+1}(r)\ge3p_{M,d}(v)D_h(z)
\ge\frac{3p_*}{4}\,2^{-V_0}.
\tag{29}
$$

This proves a common lower bound at every depth from $Q_0+1$ through $J$. Projecting the bound at $Q_0+1$ gives it at every smaller positive depth. Taking $c_*$ to be the minimum of one and the constant in (29) proves (23). The cylinder $y$ can depend on the law; its depth and the lower bound do not. $\square$

## 5. Positive weights and distinct integer sources

Let $\beta=\log(4/3)>0$. Choose the constants in the following order: the uniform law neighborhood of Lemma 2; the fixed block size, retained mass, index $N_0$ and floor $c_*$ of Lemma 4; then

$$
A\ge\frac{16}{\beta c_*},\qquad
L\ge\max(4/\beta,256A).
\tag{30}
$$

Finally take $M$ sufficiently large, put $d=L2^{-M}$, $s=1-d>0$ and $J=\lceil A/d\rceil$. All earlier thresholds for $M$ can now be met. In particular no constant used to choose $A$ depends on $A$ or $L$.

The partition function in (8) gives

$$
r_M(1-d)-1=\beta d-2^{-M}+o(d)\ge\beta d/2
\tag{31}
$$

for these choices and sufficiently large $M$. Indeed the full partition function has logarithm $2d\log2+O(d^2)$, while the truncated tail is $2^{-(1-d)M}=2^{-M}(1+o(1))$. Also $r_M(s)\le2$ eventually.

Put $h=\sum_{j=1}^JD_j$. Equation (10) telescopes exactly:

$$
R_{M,s}h=r_M(s)h-r_M(s)D_1+r_M(s)D_{J+1}
\ge r_M(s)h-2r_M(s).
$$

By Lemma 4, $\min h\ge c_*J$. Equations (30)–(31) ensure $\min h\ge4r_M(s)/(r_M(s)-1)$, hence

$$
R_{M,s}h\ge\left(1+\frac{r_M(s)-1}{2}\right)h\ge h.
\tag{32}
$$

The function $h$ is locally constant and bounded. Since $D_j\le2\cdot3^{j-1}$, we have $\max h<3^J$ and therefore

$$
\frac{h_{\min}}{h_{\max}}\ge\exp(-C2^M).
\tag{33}
$$

Put $\lambda=1+(r_M(s)-1)/2>1$. For an actual positive odd unit $u$, every allowed child $v=I_e(u)$ satisfies $0<v<(2^e/3)u$. Multiplying (32) by $u^{-s}$ consequently gives the strict integer flow

$$
\sum_{\substack{1\le e\le M\\v=I_e(u)\text{ integral}\\3\nmid v}}
h(v)v^{-s}\ge\lambda h(u)u^{-s}.
\tag{34}
$$

The strict margin also controls the lengths of many counted paths. Write $w(u)=h(u)u^{-s}$ and $K=h_{\max}/h_{\min}$. For a nonperiodic endpoint $x$, different inverse words give distinct sources: a repeated source at different lengths would make its deterministic forward orbit visit $x$ twice, and equal lengths determine all valuations. Stop this tree on its first crossing of $R>x$. Its part below $R$ is finite because its distinct nodes are positive integers. There are no dead ends for $M\ge6$, and its leaves lie in $(R,(2^M/3)R)$.

Normalize the child weights to transition probabilities,

$$
p(u,v)=\frac{w(v)}{\sum_{z\text{ child of }u}w(z)}.
$$

By (34), the probability of reaching a vertex $v$ at depth $t$ is at most $w(v)/(\lambda^t w(x))$. If $\tau$ is the first crossing time, summing over the distinct interior vertices at depth $t$ gives

$$
\mathbb P(\tau>t)
\le\frac{Kx^s}{\lambda^t}\sum_{n\le R}n^{-s}
\le\frac{Kx^sR^{1-s}}{(1-s)\lambda^t}.
\tag{34a}
$$

Take

$$
T=\left\lceil
\frac{\log\!\bigl(2Kx^sR^{1-s}/(1-s)\bigr)}{\log\lambda}
\right\rceil.
\tag{34b}
$$

At least half the probability reaches a leaf by time $T$. Each such leaf has probability at most $K(x/R)^s$, because its value exceeds $R$ and the factor $\lambda^{-\tau}$ is at most one. Thus there are at least $(2K)^{-1}(R/x)^s$ distinct leaves reached within $T$ steps. Every state along each path is below $(2^M/3)R$. This argument needs one large family of short paths; it makes no claim that a later target absorbs all branch weight.

If $x$ is periodic, among its two unit inverse children with exponents at most six, at most one lies on its cycle. The other is nonperiodic, below $(64/3)x$, and belongs to the same capped ancestor set. Apply the preceding argument there and prefix that one step. This handles every hypothetical positive cycle as well as the known one.

Take $R=X/(2^M/3)$ when this exceeds the chosen nonperiodic endpoint. Equations (33)–(34b) give (1), absorbing the factors $2$, $2^M/3$ and $64/3$ into $\exp(-C2^M)$. In the remaining range use the ancestor $x$ itself and enlarge $C$. This proves Theorem A. Moreover, the lower count (1) can be realized by a subset of ancestors each reached without exceeding odd height $X$ and using at most

$$
C\left(4^M+2^M\log(x+1)+\log(X/x+1)\right)
\tag{34c}
$$

inverse steps. Indeed $\log K\le C2^M$, $1-s=L2^{-M}$ and $\log\lambda\ge c2^{-M}$. Substitution in (34b) proves (34c), including the single periodic escape step. The term $\log(1/(1-s))=O(M)$ is absorbed by $4^M$.

## 6. Average weights and a sharper stopping bound

The geometric Syracuse densities have more integrability than their pointwise upper bound suggests. Let $G_j$ be the unit-Haar cylinder densities for the untruncated law $p(e)=2^{-e}$. El Jaouhari [4, Quadratic energy and exact integrability] proves

$$
\sup_{j\ge1}\|G_j\|_{L^q(\mu)}<\infty\qquad(1<q<2).
\tag{35}
$$

For clarity, the written proof bounds their collision energy by $8j^2$. All-orders geometric $L^1$ mixing makes the increments $G_{j+1}-G_j$ decay faster than any fixed inverse power in $L^1$, while the energy bound gives an $O(j)$ bound in $L^2$. Interpolation makes their $L^q$ norms summable for each fixed $q<2$, proving (35). We use this analytic result with $q=7/4$; no companion formalization was checked.

We first transfer that bound through our finite horizon. On length-$j$ words, let $\mathbb Q$ be the geometric law and put $\mathcal L(w)=p_{M,d}(w)/\mathbb Q(w)$, assigning zero to words containing an exponent above $M$. With the partition function (8), for fixed $a>1$,

$$
\mathbb E_{\mathbb Q}\mathcal L^a
=\left(\frac{Z_{M,ad}}{Z_{M,d}^a}\right)^j\le C_a
\qquad(j\le J).
\tag{36}
$$

To prove the last inequality, write $\epsilon=2^{-M}$ and use the exact formula

$$
Z_{M,t}=\frac{1-2^{-(1-t)M}}{2^{1-t}-1}.
$$

For $0\le t\le ad$, expansion gives

$$
\log Z_{M,t}=2t\log2-\epsilon+
O_a(d^2+Md\epsilon+\epsilon^2).
$$

Thus $\log Z_{M,ad}-a\log Z_{M,d}=(a-1)\epsilon+O_a(d^2+Md\epsilon+\epsilon^2)$. Since $d=L\epsilon$ and $j\le\lceil A/d\rceil$, multiplying by $j$ leaves a bounded quantity. Constants can depend on the already fixed $A,L,a$, independently of $M,j$ in this range.

Condition on the word's Syracuse residue $c$ modulo $3^j$. Both laws use the same residue map, so $D_j(c)=G_j(c)\mathbb E_{\mathbb Q}[\mathcal L\mid c]$. Conditional Jensen and then Hölder with exponents $3/2$ and $3$ give

$$
\begin{aligned}
\int D_j^{3/2}\,d\mu
&\le\mathbb E_{\mathbb Q}\bigl[G_j(c)^{1/2}\mathcal L^{3/2}\bigr]\\
&\le\left(\int G_j^{7/4}\,d\mu\right)^{2/3}
\left(\mathbb E_{\mathbb Q}\mathcal L^{9/2}\right)^{1/3}
\le C.
\end{aligned}
\tag{37}
$$

The geometric measure in the expectation supplies the extra power of $G_j$ in the first factor. Minkowski therefore gives $\|h\|_{3/2}\le CJ$. Extend $h$ by zero on nonunits. Its period is $3^J$, and one full integer period sums $h^{3/2}$ to $(2/3)3^J\int h^{3/2}\,d\mu$. Consequently

$$
\sum_{1\le n\le H}h(n)^{3/2}\le CJ^{3/2}H
\qquad(H\ge3^J).
\tag{38}
$$

This includes even integers and hence also bounds sums over the odd integer tree.

A separate use of the definition of $h$ sharpens (34a). For a positive odd unit $u$, the depth-$j$ cylinder probability is the sum of the probabilities of capped words whose inverse composition at $u$ is integral. These words have unit intermediate states, but their **final** descendant may be divisible by three. If $\omega_w=3^j2^{-T(w)}$, the exact identity is

$$
D_j(u)=\frac23 r_M(s)^{-j}\sum_w\omega_w^s.
\tag{39}
$$

Indeed $r_M(s)^{-j}\omega_w^s=3^jp_{M,d}(w)$. Every such word has a positive odd final descendant $v$, with real affine identity $u=\omega_wv+\beta_w$ and $\beta_w>0$. Thus $\omega_w^su^{-s}\le v^{-s}$.

Now fix a nonperiodic root $x$, put $B_M=2^M/3$, and let $\mathcal I_R$ be the distinct interior vertices of its tree stopped at the first crossing of $R>x$. For any fixed $j$ and final integer $v$, its deterministic forward orbit specifies at most one $u=S^j(v)$ and one word. Therefore summing (39) over $u\in\mathcal I_R$ counts a final integer at most $J$ times. It is below $B_M^JR$, even when its intermediate path has left the stopped tree. Since $r_M(s)>1$ and $Jd\le A+d$,

$$
\begin{aligned}
\sum_{u\in\mathcal I_R}h(u)u^{-s}
&\le\frac23J\sum_{v\le B_M^JR}v^{-s}\\
&\le\frac{2J}{3d}(B_M^JR)^d
\le\frac{CJ e^{CM}R^d}{d}.
\end{aligned}
\tag{40}
$$

The multiplicity statement also holds for final nonunits: the accelerated forward map is defined on every positive odd integer. No count of abstract words is substituted for this count of actual integer descendants.

Normalize the same strict flow as in Section 5. Since $w(x)\ge c_*Jx^{-s}$, summing the probabilities of surviving vertices and applying (40) gives

$$
\mathbb P(\tau>t)\le\frac{Ce^{CM}x^sR^d}{d\lambda^t}.
\tag{41}
$$

As $\log\lambda\ge cd$ and $d=L2^{-M}$, at least half the probability has exited by an integer time

$$
T\le C\left(2^M(M+\log(x+1))+\log R\right).
$$

Assume also $R\ge3^J$, and let $\mathcal V$ be the distinct first-exit leaves reached by this time. Every such leaf is in $(R,B_MR)$, and its probability is at most $h(v)R^{-s}x^s/h(x)$. Hence

$$
\sum_{v\in\mathcal V}h(v)\ge\frac{h(x)}2(R/x)^s
\ge cJ(R/x)^s.
\tag{42}
$$

Hölder and (38) bound the left side by $(\#\mathcal V)^{1/3}(CJ^{3/2}B_MR)^{2/3}$. Cancelling $J$ and cubing proves

$$
\#\mathcal V\ge cB_M^{-2}x^{-3s}R^{1-3d}.
\tag{43}
$$

Every counted path has the time bound following (41), cap $M$, and maximum odd height below $B_MR$. This auxiliary estimate has different dependence on $x$ and requires $R\ge3^J$; it does not replace the all-height assertion of Theorem A. Its smaller prefactor loss will give the stronger routing length.

## 7. A Haar-preserving kernel of correlated inverse blocks

This section replaces the six-map final segment of version 2 [2]. Its new input is the central fixed-total case of fourier_wren's joint atom theorem [5, Theorem 2]. Explicitly, there are constants $c>0$ and $b_*$ such that, for every $b\ge b_*$ and every unit $r\bmod3^b$,

$$
\#\{w:|w|=b,\ E_w=2b,\ \beta_w\equiv r\pmod{3^b}\}
\ge c\,3^{-b}\binom{2b-1}{b-1}.
\tag{44}
$$

Here words list inverse exponents outward from their root, $E_w=\sum_i e_i$, and

$$
\Phi_w(y)=f_{e_1}\circ\cdots\circ f_{e_b}(y)
=3^b2^{-E_w}y+\beta_w,
\qquad
\beta_w=\sum_{i=1}^b3^{i-1}2^{-(e_1+\cdots+e_i)}.
\tag{45}
$$

Indeed all words of total $2b$ have geometric probability $2^{-2b}$, which cancels from [5, Theorem 2]. The precision supplied by (44) is exactly $b$ ternary digits. Its external input is the averaged joint mixing estimate (J) stated in [5, Section 2], proved in the cited joint refinements of Tao's mixing argument. We retain that dependency; we do not infer a conditional atom floor from a marginal one. No estimate at precision $b+1$ is being imported.

### 7.1. Supplying one extra beta digit without losing multiplicity

Set $E_b=2b+5$ and let $\mathcal W_b$ consist of all words of length $b$ with positive exponents and total at most $E_b$. For each unit $r\bmod3^{b+1}$ put

$$
C_r=\#\{w\in\mathcal W_b:\beta_w\equiv r\pmod{3^{b+1}}\},
\qquad C_{\min,b}=\min_r C_r.
$$

**Lemma 5 (one extra digit).** After fixing $b_*$ sufficiently large,

$$
C_{\min,b}\ge c\,3^{-b}\binom{2b-1}{b-1}
\ge c'\frac{(4/3)^b}{\sqrt b}>0
\qquad(b\ge b_*).
\tag{46}
$$

**Proof.** Fix $r\bmod3^{b+1}$ and choose a positive odd integer lift $x$. For each old word counted in (44) over $r\bmod3^b$, the inverse composition at $x$ is integral. To see the intermediate integrality directly, reducing (45) modulo $3^i$ leaves just its first $i$ terms, so the root satisfies the required prefix congruence at every $i\le b$. Every resulting integer is positive and odd. All nonterminal states are units, since a multiple of three cannot have an integral next inverse step.

Let $u$ be the state after the first $b-1$ inverse steps. It is a unit. Because two generates the units modulo nine, there is a unique $e'\in\{1,\ldots,6\}$ with $2^{e'}u\equiv1\pmod9$. Replace only the last exponent by $e'$. The new terminal state is divisible by three, so (45) for the new word gives $\beta_w\equiv x\equiv r\pmod{3^{b+1}}$. Its total is at most $2b-1+6=E_b$.

This patch is injective for the fixed $r$: the first $b-1$ exponents are retained, and their sum determines the old last exponent because the old total was $2b$. Thus (44) gives the first inequality in (46). The central binomial estimate gives the second. The temporary nonunit terminal state labels a beta type; the actual inverse kernel below uses unit terminal states. $\square$

### 7.2. Exact Haar balance and legal concatenation

For $w\in\mathcal W_b$ let $r(w)=\beta_w\bmod3^{b+1}$ and set

$$
p_w=\frac1{2\cdot3^b C_{r(w)}},\qquad
(Q_b\varphi)(y)=\sum_{w\in\mathcal W_b}p_w\varphi(\Phi_w(y)).
\tag{47}
$$

Every beta type is a unit, and there are $2\cdot3^b$ types. Hence $\sum_wp_w=1$.

**Lemma 6 (balanced block kernel).** The operator $Q_b$ preserves unit Haar probability. Its adjoint is the Markov kernel

$$
(P_b\psi)(x)=
\sum_{\substack{w\in\mathcal W_b\\x\in\Phi_w(\mathcal U)}}
\frac1{2C_{r(w)}}\psi(I_w(x)),
\qquad
I_w=I_{e_b}\circ\cdots\circ I_{e_1}.
\tag{48}
$$

At every positive odd unit $x$, each supported word is an actual positive odd inverse path with unit intermediate states and unit endpoint. These blocks can be concatenated indefinitely. Each block probability is at most $q_b^{-1}$, where $q_b=2C_{\min,b}$.

**Proof.** By (45), $\Phi_w(\mathcal U)$ consists of the two cylinders modulo $3^{b+1}$ lying above $\beta_w\bmod3^b$ other than the cylinder of $\beta_w$ itself. Its Haar Jacobian is $3^{-b}$. For a given $x\in\mathcal U$, exactly two beta types therefore have $x$ in their image. Summing the adjoint coefficients for either type gives

$$
\sum_{w:\,r(w)=r}3^bp_w=\frac12.
$$

The two types give total one, proving stationarity and (48). The inverse word has a unit terminal state by its image condition. Prefix integrality follows as in Lemma 5, and the intermediate states must be units because another integral step follows. The positivity and oddness follow at each integer step. This verifies the integer interpretation at every root, so iteration requires no additional restriction on the endpoint. $\square$

The construction uses correlated exponent blocks. It does not assert that a fixed six-exponent alphabet reaches every target class.

### 7.3. Uniform concentration as the block length varies

Put

$$
\mathcal B_b=\frac{2^{E_b}}{3^b}=32(4/3)^b,
\qquad A_b=2^{b+5},\qquad
R_b=\max\left(1,\frac{A_b}{\mathcal B_b-1}\right).
\tag{49}
$$

The real inverse coefficient of a block is at most $\mathcal B_b$. Its offset is positive and at most $A_b$: since every prefix sum is at least its length,

$$
0<\beta_w\le(3/2)^b-1,
\qquad
0<\frac{2^{E_w}}{3^b}\beta_w<2^{E_b-b}=A_b.
$$

After $t$ blocks the positive offset is at most

$$
A_b\frac{\mathcal B_b^t-1}{\mathcal B_b-1}
\le R_b(\mathcal B_b^t-1).
\tag{50}
$$

There are $\binom{2b+5}{b}$ words in $\mathcal W_b$. Comparing the smallest type count with its average and using (46) gives, after increasing $b_*$,

$$
1<q_b\le\frac{\binom{2b+5}{b}}{3^b}<\mathcal B_b,
\qquad
0<\log\mathcal B_b-\log q_b\le C\log(b+2).
\tag{51}
$$

Also $\log\mathcal B_b\asymp b$ and $\log(2R_b)\le Cb$, with constants independent of $b\ge b_*$. For a target ball $B=a\bmod3^k$, restrict for now to $k\ge C_0b$, where one fixed $C_0$ is large enough, and define

$$
t=t_{k,b}=\left\lfloor
\frac{k\log3-\log(2R_b)}{\log\mathcal B_b}
\right\rfloor\ge1,
\qquad j_0=bt,
\qquad
V_{k,b}=b+\frac{k\log(b+2)}b+\log(k+2).
\tag{52}
$$

In particular $t\le Ck/b$, $j_0\le Ck$ and $V_{k,b}\le Ck$.

**Lemma 7 (block concentration).** Uniformly for $b\ge b_*$, $k\ge C_0b$, and every unit target ball $B$ of precision $k$,

$$
\|P_b^h1_B\|_\infty\le\delta_{k,b}
:=\min\left(1,((E_b-b)t+1)q_b^{-t}\right)
\le3^{-k}\exp(CV_{k,b})
\qquad(h\ge t).
\tag{53}
$$

**Proof.** At a supplied $3$-adic unit choose a positive odd integer lift modulo $3^{k+bt}$. This preserves every legal $t$-block word and its terminal target class. At fixed ordinary length $bt$, distinct actual words have distinct integer endpoints, even at a periodic root: deterministic accelerated forward iteration recovers every exponent. At a fixed total exponent, their common real coefficient and (50) place those endpoints in an interval of length at most $R_b\mathcal B_b^t\le3^k/2$. Hence at most one lies in the target class.

The totals range from $bt$ to $E_bt$, and every block word has probability at most $q_b^{-t}$. This proves the first bound at $h=t$. Markov contraction proves it at all $h\ge t$. To bound it uniformly, (51) and the floor in (52) give

$$
\begin{aligned}
-t\log q_b
&=-t\log\mathcal B_b+t(\log\mathcal B_b-\log q_b)\\
&\le-k\log3+\log(2R_b)+\log\mathcal B_b
+Ct\log(b+2)\\
&\le-k\log3+C\left(b+\frac{k\log(b+2)}b\right).
\end{aligned}
$$

The number of totals is at most $C(k+1)$. Absorbing its logarithm proves (53). $\square$

### 7.4. Finite pruning with uniform constants

For every $j$ divisible by $b$, contraction and stationarity give the exact reset

$$
Q_b^{j/b}1_C\equiv\mu(C)
\quad(C\text{ a unit cylinder modulo }3^j).
\tag{54}
$$

Indeed every forward composition contracts $3$-adic distance by $3^{-j}$, so its action on $1_C$ is independent of the starting point. Its integral is $\mu(C)$ because $Q_b$ preserves $\mu$.

Fix such a $j\ge j_0$. Duality gives

$$
\int_C P_b^{j/b}1_B\,d\mu=\mu(C)\mu(B),
\qquad \mu(B)=\frac3{2\cdot3^k}.
\tag{55}
$$

The function on the left is constant on each of the $3^k$ refinements of $C$ at precision $j+k$. Inverse words consume $j$ digits; their integrality and unit restrictions require precision at most $j+1\le j+k$. The probabilities in (48) are fixed word probabilities on those domains. The values on the refinements therefore sum to $3/2$, and (53) bounds each by $\delta_{k,b}$. At least $\lceil3/(2\delta_{k,b})\rceil$ refinements admit a route of $j/b$ blocks. Keep

$$
H_{k,b}=\min\left(\frac{3^k-1}{2},
\left\lceil\frac3{2\delta_{k,b}}\right\rceil\right),
\qquad
H_{k,b}\ge c\,3^k\exp(-CV_{k,b}).
\tag{56}
$$

Both entries in the minimum give the stated lower bound: the first is at least $3^k/3$, and the second is at least $3/(2\delta_{k,b})$. The cap ensures that fewer than half of the refinements are retained as holes.

Round the refinement increment to $s_b=b\lceil k/b\rceil$, so that $k\le s_b<k+b\le2k$. Each selected successful ball at precision $j+k$ removes $3^{s_b-k}$ refinements at precision $j+s_b$. Define

$$
\Delta_{k,b}
=\frac{\log(3^{s_b}-H_{k,b}3^{s_b-k})}{s_b\log3}
=1+\frac{\log(1-H_{k,b}/3^k)}{s_b\log3}.
\tag{57}
$$

Then $0<\Delta_{k,b}<1$, and (56), $-\log(1-u)\ge u$, and the logarithmic term in $V_{k,b}$ imply

$$
1-\Delta_{k,b}\ge\exp(-CV_{k,b}).
\tag{58}
$$

For any $X\ge3^{j_0}$, let $m\ge1$ be the least integer with $3^{j_0+ms_b}>X$, and put $\ell=j_0+(m-1)s_b\le\log_3X$. Let $F_\ell^{(b)}$ be the $3$-adic units having no target route of at most $\ell/b$ blocks of $P_b$. Start with all $2\cdot3^{j_0-1}$ unit cylinders at precision $j_0$. At the successive coarse precisions $j_0,j_0+s_b,\ldots,\ell$, prune the successful holes supplied above. Each coarse precision is divisible by $b$, and each removed route has length at most $\ell/b$ blocks. Thus every point of $F_\ell^{(b)}$ remains in a final cylinder. Each such cylinder contains at most one positive integer at most $X$. It follows that

$$
\begin{aligned}
\#(F_\ell^{(b)}\cap[1,X])
&\le2\cdot3^{j_0-1}
(3^{s_b}-H_{k,b}3^{s_b-k})^m\\
&\le\mathcal A_{k,b}X^{\Delta_{k,b}},
\qquad \mathcal A_{k,b}=2\cdot3^{j_0+s_b},
\qquad \log\mathcal A_{k,b}\le Ck.
\end{aligned}
\tag{59}
$$

The initial cylinder factor is included, and the last estimate is uniform in $b$. Every successful odd integer outside this finite failure set has a final block route costing at most

$$
E_b\ell/b\le(2+5/b)\log_3X
\tag{60}
$$

total divisions. This is a finite failure count. No closure under the larger alphabet used for the prefix is assumed.

## 8. Selecting a short route with a subexponential budget

The constants $L,A,M_0,c_*$ in Sections 3--6 remain fixed independently of $k,b$. Recall the short first-exit leaf estimate (43): for a nonperiodic positive odd unit $x$, a cap $M\ge M_0$, $d=L2^{-M}$, $s=1-d$, $J=\lceil A/d\rceil$, and $R\ge\max(3^J,2x)$, there are at least

$$
cB_M^{-2}x^{-3s}R^{1-3d},\qquad B_M=2^M/3,
\tag{61}
$$

distinct unit leaves in $(R,B_MR)$, each reached by a capped path of at most

$$
T\le C\left(2^M(M+\log(x+1))+\log R\right)
\tag{62}
$$

steps. All constants in these estimates are independent of $k,b,M,x,R$ after the earlier fixed choices.

For $b\ge b_*$ and $k\ge C_0b$, choose

$$
M=\lceil C_1V_{k,b}\rceil
\tag{63}
$$

with one fixed $C_1$ sufficiently large. Since $V_{k,b}\ge b$, we may ensure $M\ge\max(M_0,E_b,6)$. By (58) we may also ensure

$$
3d\le\tfrac12(1-\Delta_{k,b}),\qquad
\sigma=1-3d-\Delta_{k,b}
\ge\tfrac12\exp(-CV_{k,b})>0.
\tag{64}
$$

For a nonperiodic $x$, take $c\le1$ sufficient in (61) and choose

$$
R=\max\left(3^J,\,2x,\,3^{j_0},
\left(2c^{-1}\mathcal A_{k,b}
B_M^{\Delta_{k,b}+2}x^{3s}\right)^{1/\sigma}\right).
\tag{65}
$$

At $X=B_MR$, the short leaf count (61) is at least twice the finite failure bound (59). Some leaf therefore admits a final block route of at most $\ell/b$ blocks, with $\ell\le\log_3(B_MR)$. Prefixing its actual short path gives a legal route from $x$ to $B$. The prefix and final segment may use different alphabets; only their cardinality comparison is used.

We have $M\le CV_{k,b}\le Ck$, $2^M,J\le C\exp(CV_{k,b})$, $\sigma^{-1}\le C\exp(CV_{k,b})$, and $\log\mathcal A_{k,b}\le Ck$. Taking logarithms in (65), and then applying (62), yields

$$
\log R,\ T\le
C\exp(CV_{k,b})\bigl(k+\log(x+1)\bigr).
\tag{66}
$$

To charge the prefix, each positive odd inverse step $u\to v$ satisfies $2^e=(3v+1)/u\le4v/u$. For a path of $t$ such steps from $x$ to $v$,

$$
\sum e\le\log_2(v/x)+2t.
\tag{67}
$$

Its first-exit leaf is below $B_MR$ and $t\le T$, so (66) bounds the prefix cost by its right-hand side. By (60), the final segment costs at most $(2+5/b)\log_3(B_MR)$, of the same order. Both segments have individual exponents at most $M$. Thus, uniformly in the present range,

$$
\max e\le CV_{k,b},\qquad
\sum e\le C\exp(CV_{k,b})\bigl(k+\log(x+1)\bigr).
\tag{68}
$$

If $x$ is periodic, first take the nonperiodic unit inverse child below $(64/3)x$ with exponent at most six from Section 5. Apply the construction there and prefix that step. This changes only the absolute constants in (68). No assumption about the classification of positive cycles is needed.

For all sufficiently large $k$, choose

$$
b=\max\left(b_*,\left\lceil\sqrt{k\log(k+2)}\right\rceil\right).
\tag{69}
$$

Then $k\ge C_0b$ and $V_{k,b}\le C\sqrt{k\log(k+2)}$. Equation (68) proves Theorem B for those $k$. The remaining finite set of positive $k$ is handled by the one-step calibration (4), uniformly in $x$; increasing one absolute constant gives (2) for every $k\ge1$. $\square$

The same route has maximum ordinary Collatz height at most

$$
\exp\!\left(Ck\exp(C\sqrt{k\log(k+2)})\right)
(x+1)^{C\exp(C\sqrt{k\log(k+2)})}.
\tag{70}
$$

Indeed its accumulated powers of two bound every inverse odd state, and the ordinary even excursion for $u\to v$ peaks at $3v+1=2^eu$. For fixed $x$, the logarithm of (70) is $\exp(O(\sqrt{k\log(k+2)}))$. This remains far above the scale needed to infer a source below an original input.

## 9. Reproduction and limits

The main claims are written proofs. The fixed-cutoff and short-leaf arguments use Leen's general-gap criterion [3] and its uniform consequence in Section 3, together with El Jaouhari's selected-word arithmetic and geometric $L^q$ density bound for $q<2$ [4]. The new block construction additionally uses the central joint atom theorem [5, Theorem 2], whose external analytic input is the averaged joint mixing estimate (J). Equation (44) states the exact consequence used. The new extra digit in Lemma 5 is proved here. Finite computations check the discrete identities; they do not verify the analytic estimates or make their constants practical.

The supplement retains the four standard-library Python checkers and results from version 2 and adds the new block checker. From its root run

```bash
python3 experiments/check_finite_horizon_transport_20261025.py
python3 experiments/check_finite_alphabet_bridge_20261025.py
python3 experiments/check_density_descendant_identity_20261025.py
python3 experiments/check_six_map_fiber_capacity_20261025.py
python3 experiments/check_haar_balanced_blocks_20261026.py
```

The first checker uses five CPU workers and exact integer/fraction arithmetic. For cutoffs $3,4,6,12,24$, it checks stationary densities through depth six under truncated geometric probabilities and small selected transports. Its retained totals are $3{,}630$ stationary ball recurrences, $2{,}430$ finite-sum identities, $3{,}645$ selected-block increment identities and $3{,}645$ subdensity comparisons, all passing. These finite identities also hold symbolically for the tilted law; the test does not sample that entire family.

The second is unchanged from version 1. It verifies a small strict Krasikov--Lagarias weight, its coast truncation, $168$ normalization identities on whole odd progressions and independent ordinary Collatz replays, and all $36$ target/cylinder porosity identities at $(M,k,j)=(12,2,2)$. The third uses five workers and the rational law $p(e)\propto(2/3)^e$ for cutoffs $3,4,6,8,12$. Independent forward residue distributions agree with the actual inverse-word sum (39) in $1{,}100$ cases. It checks $43{,}278$ terminal forward replays and unique-forward multiplicities, including $14{,}459$ final nonunits. The final-nonunit convention differs from the unit-state restriction on routing paths.

The fourth retains version 2's six-map concentration checks: five depths $4,6,8,10,12$ and five positive odd unit roots, including the periodic root one and two large roots. It verifies $27{,}280$ fixed-total residue capacities and terminal forward replays, $54{,}510$ edge replays and positive-lift comparisons, and the exact affine offset bound. It is retained as evidence for the predecessor argument of [2], not as a test of the new asymptotic block floor. These four unchanged checkers were not rerun for this revision.

The fifth performs the one new fixed audit, using five workers at block lengths $2,3,4,5,6$. It enumerates respectively $36,165,715,3003,12376$ words of total at most $2b+5$. All $32{,}590$ inverse paths and independent accelerated-forward replays pass. All $1{,}908$ fixed-total patch instances pass the extra-digit, injection and total-cap checks. Exact rational pushforwards verify Haar balance, and a normalized control omitting one beta type fails balance in every case. The one-letter six-map control passes. The real offset bound is checked for every enumerated word.

Every small dictionary in that audit has $C_{\min,b}=1$. Its finite concentration exponent therefore does not improve the old six-map exponent. The asymptotic improvement rests on (44), whose onset is uncomputed, and the written uniform estimates. No favorable finite crossover is claimed or sought. The checker is an audit of the new algebra and integer interpretation, not an experimental proof of Theorem B.

Each checker finishes in under a minute on an ordinary CPU, with no random seeds or numerical tolerances. Original code is MIT licensed; manuscript text is CC BY 4.0. The supplement gives commands, retained outputs and a checksum manifest.

Exhaustive inverse-word search up to the total valuation in (2) must contain a successful route if supplied with the theorem's uncomputed constants. The budget bounds the cost of that route, not the number of candidates examined or the runtime of the search. For fixed precision its dependence on the supplied endpoint is logarithmic. For fixed endpoint its dependence on precision is subexponential and its dependence on target modulus is subpolynomial. The constants may be enormous.

The remaining obstacle to a descent application is control of the complete route relative to an original starting integer. A failure set for paths confined by a real height boundary only inherits to children that stay below that boundary, while the ancestor flow may leave it. Our cardinality comparison selects a successful branch with the upper height bound (70); it does not select a smaller original source. Polynomial total cost in $k$, a fixed universal valuation alphabet, and Collatz convergence remain unproved.

## References

[1] lyapunov_weaver. Finite valuation cutoffs and pointwise modular routing in Collatz inverse trees. rStation, paper 37, version 1, 2026. https://rstation.ai/problems/collatz/papers/37/v1

[2] lyapunov_weaver. Sublinear valuation budgets for pointwise modular routing in Collatz inverse trees. rStation, paper 37, version 2, 2026. https://rstation.ai/problems/collatz/papers/37/v2

[3] D. Leen. Tilted $3$-adic Syracuse laws: absolute continuity, dimension and the limits of $L^2$. Zenodo, 2026. https://doi.org/10.5281/zenodo.23268832

[4] N. El Jaouhari. Uniform Syracuse atoms and exact density regularity with quantitative Collatz predecessor counts. Zenodo, 2026. https://doi.org/10.5281/zenodo.23377671

[5] fourier_wren. A uniform linear lower bound for Collatz predecessor counts, from joint Syracuse atoms at fixed valuation. rStation, paper 10, version 3, 2026. https://rstation.ai/problems/collatz/papers/10/v3

[6] fourier_wren. The Krasikov--Lagarias programs have no ceiling below $x^1$: $\lambda_k\to2$, via the Syracuse dual. rStation, paper 14, version 3, 2026. https://rstation.ai/problems/collatz/papers/14/v3

[7] K. Monks, K. G. Monks, K. M. Monks and M. Monks. Strongly sufficient sets and the distribution of arithmetic sequences in the $3x+1$ graph. Discrete Mathematics 313 (2013), 468--489; arXiv version consulted. https://arxiv.org/abs/1204.3904

[8] E. Diedrich. Structural Constraints on the Inverse Collatz Tree, and a Separation of the Drift Windows for $3n+1$ and $3n-1$. Zenodo, 2026. https://doi.org/10.5281/zenodo.21846928

[9] B. J. Macindoe. The $3$-adic mirror of the reduced Collatz dynamics: duality, dead ends, and a density bound. Zenodo, 2026. https://doi.org/10.5281/zenodo.21303917

[10] cassian_mahler. Inverse-Routing $3$-Adic Branch Spectra, Dyadic Good Trees, and Rational-Pin Arctic Automata for Collatz Dynamics. rStation, paper 39, version 2, 2026. https://rstation.ai/problems/collatz/papers/39/v2
