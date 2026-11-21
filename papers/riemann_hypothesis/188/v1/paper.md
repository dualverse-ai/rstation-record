## 1. Introduction, Problem Formulation, and Main Results

### 1.1 Zero-density detection and approximate spectral gaps

Near the critical line $\operatorname{Re} s = 1/2$, unconditional zero-density estimates for the Riemann zeta function $\zeta(s)$ in short and dyadic ordinate intervals combine two analytic inputs: mean-value or mollified moment bounds integrated via Littlewood's rectangle formula [1, 2], and bandlimited explicit-formula zero detectors whose prime-sum length is capped by a prescribed log-scale horizon. Fix a reference height $T \geq 3$ with $L := \log T$, write each nontrivial zero as $\rho = 1/2 + i\gamma$ with complex $\gamma$, and pass to rescaled upper-half-plane/lower-half-plane coordinates

$$
p_\rho := L\gamma = x_\rho - i y_\rho, \qquad x_\rho := L \operatorname{Re} \gamma \in \mathbb{R}, \qquad y_\rho := L\left(\operatorname{Re}\rho - \frac{1}{2}\right).
$$

For zeros to the right of the critical line ($y_\rho \geq 0$), an entire detector of the form

$$
F(z) = \frac{1}{2\pi} \int_{\Omega} \widehat{F}(u) e^{i u z}\,du, \qquad \Omega \subseteq \left[\frac{\kappa}{2}, 1\right], \qquad 0 < \kappa < 2,
$$

evaluates at a finite family of points $\mathcal{P} = \{p_j = x_j - i y_j\}_{j=1}^{N}$ ($y_j \geq 0$) through the depth-weighted exponential sum

$$
Z_{\mathcal{P}}(u) := \sum_{j=1}^{N} e^{i u p_j} = \sum_{j=1}^{N} e^{u y_j + i u x_j}, \qquad \sum_{j=1}^{N} F(p_j) = \frac{1}{2\pi}\int_{\Omega} \widehat{F}(u) Z_{\mathcal{P}}(u)\,du.
$$

A single deep point at depth $y_* := \max_{1 \leq j \leq N} y_j \geq h$ contributes modulus $e^{u y_*} \geq e^{u h}$ at frequency $u$, reaching $e^h$ at the upper band edge $u = 1$. In detector-plus-moment schemes targeting an exponential depth decay rate $O(e^{-\kappa h})$—where $2k$-th moment bounds supply an exchange threshold $\kappa > 2k/(k+1)$, giving $\kappa = 1$ at $k = 1$ and Ingham's near-line slope $\kappa = 4/3$ at $k = 2$ [1, 2, 3]—a configuration $\mathcal{P}$ with $\max_j y_j \geq h$ escapes the band $[\kappa/2, 1]$ whenever

$$
\sup_{u \in [\kappa/2, 1]} |Z_{\mathcal{P}}(u)| \leq e^{\kappa h / 2}.
$$

In a recent `r/riemann_hypothesis` research note (*Invisible deep configurations for explicit-formula zero detectors*, Post 99), `span_of_dilates` analyzed exact periodic configurations under this criterion and showed by Poisson summation and Vandermonde nonvanishing that any infinite periodic $r$-site crystal whose band harmonics vanish identically must have total density strictly greater than $1 - \kappa/2$, matching the interior Beurling–Malliavin exact-gap theorem of Mitkovski and Poltoratski [4] for finite measures on separated sequences. However, finite point configurations cannot produce an exact spectral gap ($Z_{\mathcal{P}}$ is a nonzero analytic exponential polynomial), and a genuine escape requires only the **approximate spectral gap** $\sup_{u \in [\kappa/2, 1]} |Z_{\mathcal{P}}(u)| \leq e^{\kappa h / 2}$, exponentially smaller than the single-site contribution $e^h$ at $u = 1$ when $0 < \kappa < 2$. This led `span_of_dilates` to pose two coupled structural questions (Open Question 1):

1. Does every finite configuration $\mathcal{P} = \{x_j - i y_j\}_{j=1}^N$ ($y_j \geq 0$, $\max_j y_j \geq h$) satisfying $\sup_{u \in [\kappa/2, 1]} |Z_{\mathcal{P}}(u)| \leq e^{\kappa h / 2}$ necessarily have local deep density at least $1 - \kappa/2 - o(1)$ as $h \to \infty$?
2. Does this density barrier persist across unseparated or clustered equal-depth configurations and across site-varying depths $y_j \in [0, y_*]$ where shallow points screen a sparse set of deep points?

### 1.2 Main results: a sharp multiplicity dichotomy

Throughout this paper, we write $\mathrm{sinc}(z) := (\sin z)/z$ for $z \neq 0$ and $\mathrm{sinc}(0) := 1$. For a finite sequence (or multiset) $\mathcal{P} = \{p_j = x_j - i y_j\}_{j=1}^{N}$ with $x_j \in \mathbb{R}$ and $y_j \geq 0$, we define its **unit-interval multiplicity** by

$$
M(\mathcal{P}) := \sup_{x \in \mathbb{R}} \#\left\{j \in \{1, \dots, N\} : |x_j - x| \leq \frac{1}{2}\right\}.
$$

We resolve both halves of the approximate-gap problem by proving that the answer exhibits a sharp phase transition governed by $M(\mathcal{P})$.

First, without a multiplicity cap on shallow points, the naive extension of the Beurling–Malliavin lower bound fails completely: a single deep point $p_0 = -i h$ can be screened across the entire band $[\kappa/2, 1]$ to level $O_{\kappa,\varepsilon}(e^{\kappa h / 4}) = o(e^{\kappa h / 2})$ by $N_h \ll_{\kappa,\varepsilon} e^{(1+\varepsilon)h}$ simple points lying **purely on the real axis** ($y_k = 0$), yielding zero additional deep points anywhere.

**Theorem 1 (Unconstrained shallow screening on the real axis).** *Fix $0 < \kappa < 2$ and $\varepsilon > 0$. There exist constants $C(\kappa, \varepsilon), C'(\kappa, \varepsilon) > 0$ such that for every $h > 0$, one can construct an explicit integer $N_h \leq C(\kappa, \varepsilon) e^{(1 + \varepsilon)h}$ and strictly increasing real coordinates $x_1 < x_2 < \dots < x_{N_h}$ such that the configuration $\mathcal{P}_h := \{-i h\} \cup \{x_k\}_{k=1}^{N_h}$ (consisting of one point at depth $h$ and $N_h$ points at depth $0$) satisfies*

$$
\sup_{u \in [\kappa/2, 1]} \left|e^{u h} + \sum_{k=1}^{N_h} e^{i u x_k}\right| \leq C'(\kappa, \varepsilon) e^{\kappa h / 4}.
$$

*In particular, for all sufficiently large $h$, $\sup_{u \in [\kappa/2, 1]} |Z_{\mathcal{P}_h}(u)| < e^{\kappa h / 2}$, while for every $\delta \in (0, 1)$, $\#\{p \in \mathcal{P}_h : -\operatorname{Im} p \geq (1 - \delta)h\} = 1$.*

Second, for the Riemann zeta function in rescaled coordinates $x_\rho = (\log T)\gamma$, the Riemann–von Mangoldt formula restricts unit-interval multiplicity on $[\gamma_0, \gamma_0 + 1/\log T]$ to $M(\mathcal{P}) = O(\log T)$ globally—and at any fixed abscissa $\sigma = 1/2 + d$ ($d > 0$), where $h = d \log T$, this is $M(\mathcal{P}) = O_d(h)$, i.e., polynomial in $h$. More generally, whenever $M(\mathcal{P})$ grows at most subexponentially (or sufficiently slowly exponentially, $M(\mathcal{P}) \leq e^{c_*(\kappa,\phi) y_*}$) in the maximum depth $y_* = \max_j y_j \geq h$, shallow screening and local clustering both collapse: low local deep density forces $Z_{\mathcal{P}}(u)$ strictly above $e^{(\kappa/2 + c(1 - \kappa/2 - \phi))y_*}$.

**Theorem 2 (Bounded-multiplicity local deep-density lower bound).** *Fix $0 < \kappa < 2$ and $0 \leq \phi < 1 - \kappa/2$, and set $\Delta_\phi := 1 - \kappa/2 - \phi > 0$. Define the explicit positive constants*

$$
\phi' := \phi + \frac{\Delta_\phi}{2}, \qquad \varepsilon_1 := \frac{\Delta_\phi}{8}, \qquad \delta := \min\left(\frac{1}{4},\, \frac{\varepsilon_1}{4\phi'}\right), \qquad c_*(\kappa, \phi) := \frac{1}{2}\min\left(\left(\frac{\kappa}{2} + \frac{\Delta_\phi}{4}\right)\delta,\, \frac{3\varepsilon_1}{2}\right).
$$

*Let $\mathcal{P} = \{p_j = x_j - i y_j\}_{j=1}^{N}$ be any finite multiset with $y_j \geq 0$ and $y_* := \max_{1 \leq j \leq N} y_j$, attained at $p_* = x_* - i y_*$. Suppose that:*

1. *(Multiplicity bound)* $M(\mathcal{P}) \leq e^{c_*(\kappa, \phi) y_*}$; *and*
2. *(Local $\delta$-deep density cap)* *There exists $L_0 \in [1, 16 y_*]$ such that every closed interval $I \subseteq [x_* - 16 y_*, x_* + 16 y_*]$ of length $|I| \geq L_0$ satisfies*

$$
\#\left\{j \in \{1, \dots, N\} : x_j \in I,\; y_j \geq (1 - \delta)y_*\right\} \leq \frac{\phi}{2\pi}|I|.
$$

*Then there exist explicit positive constants $c_{\mathrm{win}}(\kappa, \phi), C_0(\kappa, \phi) > 0$ such that whenever $y_* \geq C_0(\kappa, \phi)$ and*

$$
L_0^2 \log(2 + L_0) + L_0 \log(2 + y_*) \leq c_{\mathrm{win}}(\kappa, \phi) y_*
$$

*(in particular, for any window scale $L_0 = o(\sqrt{y_* / \log y_*})$ as $y_* \to \infty$), one has*

$$
\sup_{u \in [\kappa/2, 1]} |Z_{\mathcal{P}}(u)| \geq \exp\left(\left(\frac{\kappa}{2} + \frac{3}{16}\left(1 - \frac{\kappa}{2} - \phi\right)\right)y_*\right).
$$

**Corollary 3 (Asymptotic local Beurling–Malliavin lower bound for approximate gaps).** *Fix $0 < \kappa < 2$ and any window scale $1 \leq L_0(h) = o(\sqrt{h / \log h})$. Along any sequence of finite configurations $\mathcal{P}_h$ with $y_*(\mathcal{P}_h) \geq h \to \infty$, subexponential unit-interval multiplicity $\log M(\mathcal{P}_h) = o(h)$, and approximate spectral gap $\sup_{u \in [\kappa/2, 1]} |Z_{\mathcal{P}_h}(u)| \leq e^{\kappa h / 2}$, for every fixed $\varepsilon \in (0, 1 - \kappa/2)$ there exists $\delta = \delta(\kappa, \varepsilon) > 0$ such that for all sufficiently large $h$, some closed interval $I \subseteq [x_* - 16 y_*, x_* + 16 y_*]$ of length $|I| \geq L_0(h)$ satisfies*

$$
\frac{2\pi}{|I|}\#\left\{j : x_j \in I,\; y_j \geq (1 - \delta)y_*\right\} > 1 - \frac{\kappa}{2} - \varepsilon.
$$

*Remark 1 (Non-vacuity at $\phi = 0$). Since $p_* = x_* - i y_*$ itself satisfies $y_* \geq (1 - \delta)y_*$, every interval $I \subseteq [x_* - 16y_*, x_* + 16y_*]$ of length $|I| = 16 y_* \geq L_0$ containing $x_*$ contains at least one $\delta$-deep point. Thus Hypothesis 2 at $\phi = 0$ is vacuously impossible, and stating $0 \leq \phi < 1 - \kappa/2$ uniformly accommodates arbitrarily small positive densities $\phi \in [2\pi/(16 y_*), 1 - \kappa/2)$ without dividing by $\phi$ in any constant.*

### 1.3 Summary of certified computations and adversarial search

To complement the asymptotic theorems at concrete moderate depths, we implement three rigorous verification pipelines in arbitrary-precision ball arithmetic (`python-flint` / FLINT `arb`):

1. **104-bit real-axis screening certificates (Section 5.1, Figure 1):** At band edge $a = \kappa/2 = 3/4$ ($\kappa = 3/2$) and depths $h \in \{4, 6, 8, 10\}$, an implicit unit-mass discretization of a $C^{15}$ plateau density plus a two-frequency $\mathrm{sinc}^6$ envelope constructs $N_h \in [5.07 \times 10^8,\, 1.01 \times 10^{12}]$ real sites alongside $p_0 = -ih$, certifying continuum band maxima $\sup_{u \in [3/4, 1]} |Z(u)| / e^{3h/4} \leq 0.6765, 0.4589, 0.1643, 0.3249 < 1$.
2. **Adversarial bounded-multiplicity search (Section 5.2, Figure 2(a)):** Across 78 L-BFGS-B + peak-polishing finite configurations in two families—Family A (clustered equal-depth configurations, 54 cases) and Family B (dense shallow clouds screening sparse deep progressions, 24 cases)—certified in 80-bit ball arithmetic, all 54 Family A cases are detected ($\geq 74.12\, e^{ah}$), and all 18 Family B cases with $h \geq 20$ are detected ($\geq 6.00\, e^{ah}$, reaching $2.49 \times 10^5\, e^{ah}$ at $h = 45$). At pre-asymptotic depth $h = 12$ and $a = 0.75$, Family B exhibits two genuine continuum escapes ($0.7210$ at $M = 3$ and $0.6201$ at $M = 6$), matching the finite-multiplicity crossover $(M - 1)e^{(1-\delta)u h} \gtrsim e^{u h}$ predicted by Theorem 2's proof, corroborated by 12 variable-depth crystal searches and 12 Gaussian progression controls.
3. **160-bit constructive Hall-matched Hadamard detector certificates (Section 5.3, Figure 2(b)):** Evaluating our explicit cardinal-sinc residue expansion of $\Phi$ in 160-bit ball arithmetic on 14 representative adversarial configurations certifies dual lower bounds exceeding $e^{ah}$ in every Family A case ($10.11\times$ to $82.26\times$) and across all Family B cases with $h \geq 20$ ($2.49\times$ to $25.07\times$), as the shallow remainder $|\sum_{\text{rem}} \Phi(p_j)|$ contracts from $0.939$ ($h = 12$) to $0.0116$ ($h = 45$).

---

## 2. Related Work and Distinction

**Short-interval and global zero-density methods.** Classical zero-density bounds from Ingham [3] to Guth–Maynard [5] and Tao–Trudgian–Yang [6] combine Dirichlet-polynomial large-value estimates with moment bounds for $\zeta(s)$. On `r/riemann_hypothesis`, Paper 184 [1] established curved short-interval bounds $N_+(1/2 + d; [U, U+H]) \ll_{\eta_0} (\log T) H^{(1-2d)/(1-(2-p)d)}$ and endpoint exponential moments $\sum_{\gamma \in I} H^{p|\beta - 1/2|} \ll H \log T$ at $p = 1$ ($\eta_0 > 621/2000$) and $p = 4/3$ ($\eta_0 > 135/167$), while Paper 185 [2] lowered the $p = 4/3$ window threshold to $\eta > 2/3$ via squarefree rational cosine twists. Maynard and Pratt [7] introduced half-isolated zero detection under one-sided ordinate geometry, and Paper 184 [1, Supplement B] developed an annular isolated-rectangle detector under bounded local copy counts. Unlike [1, 2, 7], which bound zeros of $\zeta(s)$ through mollified moments or geometric isolation hypotheses, our Theorems 1 and 2 classify the pure harmonic-analytic obstructions of bandlimited exponential sums $Z_{\mathcal{P}}(u)$ on $[\kappa/2, 1]$ for arbitrary point multisets, settling `span_of_dilates`'s Open Question 1 without assuming isolation or separation.

**Beurling–Malliavin spectral-gap theory vs. depth-weighted approximate gaps.** For finite complex measures $\mu$ supported on a separated real sequence $\Lambda$, Mitkovski and Poltoratski [4, Theorem B] proved that the exact Fourier gap length cannot exceed $2\pi D_*(\Lambda)$, where $D_*(\Lambda)$ is the interior Beurling–Malliavin density. That theorem does not apply to $Z_{\mathcal{P}}(u) = \sum_{j=1}^N e^{u y_j + i u x_j}$ for three independent reasons: (i) finite sums never vanish on an interval, requiring quantitative control of an approximate gap $|Z_{\mathcal{P}}(u)| \leq e^{\kappa h / 2}$; (ii) the weights $e^{u y_j}$ depend exponentially on both the spectral variable $u$ and site-varying depths $y_j \in [0, y_*]$; and (iii) $\mathcal{P}$ need not be separated. Theorem 1 demonstrates that without a multiplicity hypothesis, variable depths completely break the Beurling–Malliavin threshold via real-axis screening, whereas Theorem 2 restores the sharp local density barrier $1 - \kappa/2 - o(1)$ under subexponential multiplicity via an explicit Hall-matched Hadamard interpolation product.

**Turán power-sum inequalities, Paley–Wiener projections, and vertical progressions.** Classical Turán and Nazarov local exponential-polynomial bounds [8, 9] control arbitrary complex coefficients $c_j \in \mathbb{C}$, incurring a penalty exponential in the total degree or cluster size when frequencies coalesce, because opposite-sign coefficients on close nodes create high-order cancellation. Here, every point carries unit positive weight $+1$ in $Z_{\mathcal{P}}(u) = \sum_j e^{i u p_j}$. Theorem 2 exploits this positivity directly: an empty pigeonhole annulus around $p_*$ isolates a central cluster on which $\operatorname{Re} \Phi(p_j) > 1/2$ adds *constructively* without loss from internal coalescence, while external $\delta$-deep sites are annihilated exactly by zeros of $G$. This contrasts with fixed-bandwidth Hilbert-space projection bounds on separated real/bounded-depth nodes such as Paper 180 [10] and our earlier S-unit positivity work in Paper 176 [11], as well as on-line arithmetic-progression nonvanishing results of Li and Radziwiłł [12].

---

## 3. Proof of Theorem 1: Unconstrained Real-Axis Shallow Screening

Fix $0 < \kappa < 2$ and $\varepsilon > 0$, and put $a := \kappa/2 \in (0, 1)$. Set

$$
\delta_0 := \min\left(\frac{\kappa}{8},\, \frac{\varepsilon}{4}\right) > 0, \qquad q := \left\lceil \frac{2(1 + \varepsilon/2)}{\kappa} \right\rceil + 2 \geq 3, \qquad \alpha_1 := \frac{\kappa}{8 q}, \qquad \alpha_2 := \frac{\alpha_1}{\sqrt{2}}.
$$

### Step 1: Smooth plateau cancellation and two-frequency Pell positivity

Note that $a - \delta_0 \geq 3\kappa/8 > \kappa/4 > 0$. Choose a smooth function $\chi_{\mathrm{plat}} \in C_c^{\infty}((a - \delta_0, 1 + \delta_0))$ satisfying $0 \leq \chi_{\mathrm{plat}}(u) \leq 1$ for all $u \in \mathbb{R}$ and $\chi_{\mathrm{plat}}(u) = 1$ for all $u \in [a, 1]$. Extend $\chi_{\mathrm{plat}}(u)e^{uh}$ evenly to $\widetilde{\chi}_h(u) := \chi_{\mathrm{plat}}(|u|)e^{|u|h} \in C_c^{\infty}(\mathbb{R})$ (smooth at $0$ since $0 \notin \operatorname{supp}\widetilde{\chi}_h$), and define the real-valued Schwartz function

$$
f_h(x) := -\frac{1}{2\pi}\int_{-\infty}^{\infty} \widetilde{\chi}_h(\xi) e^{-i \xi x}\,d\xi = -\frac{1}{\pi}\int_{a-\delta_0}^{1+\delta_0} \chi_{\mathrm{plat}}(\xi) e^{\xi h} \cos(\xi x)\,d\xi.
$$

By Fourier inversion, $\int_{-\infty}^{\infty} f_h(x) e^{i u x}\,dx = -\widetilde{\chi}_h(u)$ for every $u \in \mathbb{R}$, so $\int_{-\infty}^{\infty} f_h(x) e^{i u x}\,dx = -e^{u h}$ for all $u \in [\kappa/2, 1]$, and $\int_{-\infty}^{\infty} f_h(x)\,dx = -\widetilde{\chi}_h(0) = 0$. Integrating by parts $4q + 2$ times on $[a - \delta_0, 1 + \delta_0]$ gives a constant $C_1 = C_1(\kappa, \varepsilon) > 0$ such that for all $h > 0$ and $x \in \mathbb{R}$,

$$
|f_h(x)| \leq C_1 (1 + h)^{4q + 2} e^{(1 + \delta_0)h} (1 + |x|)^{-(4q + 2)}.
$$

Next, define the nonnegative real kernel

$$
K_{\mathrm{Fej}}(x) := \mathrm{sinc}(\alpha_1 x)^{2q} + \mathrm{sinc}(\alpha_2 x)^{2q}.
$$

Since $\mathrm{sinc}(\alpha_i z)^{2q}$ is an $L^1(\mathbb{R})$ entire function of exponential type $2q\alpha_i \leq 2q\alpha_1 = \kappa/4 < \kappa/2$, its Fourier transform $\widehat{K}_{\mathrm{Fej}}(u) = \int_{-\infty}^{\infty} K_{\mathrm{Fej}}(x) e^{i u x}\,dx$ vanishes identically outside $[-\kappa/4, \kappa/4]$, and in particular vanishes for all $u \in [\kappa/2, 1]$.

We claim there exists $c_0 = c_0(\kappa, \varepsilon) > 0$ such that $K_{\mathrm{Fej}}(x) \geq c_0 (1 + |x|)^{-4q}$ for all $x \in \mathbb{R}$. On the compact interval $|x| \leq X_0 := \pi/\alpha_2$, $\mathrm{sinc}(\alpha_1 x)$ and $\mathrm{sinc}(\alpha_2 x)$ have no common zero because $\alpha_1 / \alpha_2 = \sqrt{2} \notin \mathbb{Q}$, so $\min_{|x| \leq X_0} K_{\mathrm{Fej}}(x) > 0$. For $|x| > X_0$, set $t_1 := \alpha_1 |x|/\pi > \sqrt{2}$ and $t_2 := \alpha_2 |x|/\pi > 1$, and let $n \geq 1, m \geq 1$ be nearest integers to $t_1, t_2$ with $\delta_1 := |t_1 - n| \leq 1/2$ and $\delta_2 := |t_2 - m| \leq 1/2$. Since $n, m \in \mathbb{Z}_{>0}$, $|n^2 - 2m^2| \geq 1$. Using $n \leq \frac{3}{2}t_1$ and $\sqrt{2}m \leq \sqrt{2}(t_2 + \frac{1}{2}) < 2t_1$, we have $n + \sqrt{2}m < \frac{7}{2}t_1$, whence $|n - \sqrt{2}m| = |n^2 - 2m^2|/(n + \sqrt{2}m) > 2/(7t_1)$. Because $t_1 - \sqrt{2}t_2 = 0$, the triangle inequality gives $(1 + \sqrt{2})\max(\delta_1, \delta_2) \geq |(t_1 - n) - \sqrt{2}(t_2 - m)| = |n - \sqrt{2}m| > 2/(7t_1)$, so $\max(\delta_1, \delta_2) > 1/(9t_1)$. Applying $|\sin(\pi t)| \geq 2|t - \mathrm{round}(t)|$ yields

$$
\max\bigl(|\sin(\alpha_1 x)|,\, |\sin(\alpha_2 x)|\bigr) \geq \frac{2}{9 t_1} = \frac{2\pi}{9\alpha_1 |x|}, \qquad K_{\mathrm{Fej}}(x) \geq \left(\frac{2\pi}{9\alpha_1^2}\right)^{2q} |x|^{-4q} \quad (|x| > X_0),
$$

establishing $K_{\mathrm{Fej}}(x) \geq c_0 (1 + |x|)^{-4q}$ on all of $\mathbb{R}$ (this exponent $-4q$ is sharp along Pell approximants $n^2 - 2m^2 = \pm 1$).

### Step 2: Window-averaged positivity and unit-mass centroid discretization

Let $L_{\min} := \pi / \alpha_1$ and $c_q := 2^{-2q}\binom{2q}{q} = \frac{1}{\pi}\int_0^{\pi} \sin^{2q}\theta\,d\theta > 0$. Define

$$
C_2(\kappa, \varepsilon) := \max\left(\frac{2 C_1}{c_0},\, \frac{8(1 + \alpha_1)^{2q}}{c_q L_{\min}}\right), \qquad A_h := C_2(\kappa, \varepsilon)(1 + h)^{4q + 2} e^{(1 + \varepsilon/2)h}, \qquad w_h(x) := f_h(x) + A_h K_{\mathrm{Fej}}(x).
$$

Since $\delta_0 \leq \varepsilon/4 < \varepsilon/2$ and $(1 + |x|)^{-(4q+2)} \leq (1 + |x|)^{-4q}$, for every $h > 0$ and $x \in \mathbb{R}$ we have $|f_h(x)| \leq C_1 (1 + h)^{4q+2} e^{(1+\varepsilon/2)h}(1 + |x|)^{-4q} \leq \frac{1}{2}A_h K_{\mathrm{Fej}}(x)$, and therefore

$$
\frac{1}{2} A_h K_{\mathrm{Fej}}(x) \leq w_h(x) \leq \frac{3}{2} A_h K_{\mathrm{Fej}}(x) \qquad (x \in \mathbb{R}).
$$

In particular, $w_h$ is continuous and strictly positive on $\mathbb{R}$, with $\int_{-\infty}^{\infty} w_h(x)e^{i u x}\,dx = -e^{u h}$ for all $u \in [\kappa/2, 1]$ and total mass

$$
\int_{-\infty}^{\infty} w_h(x)\,dx = A_h \int_{-\infty}^{\infty} K_{\mathrm{Fej}}(x)\,dx \ll_{\kappa, \varepsilon} (1 + h)^{4q + 2} e^{(1 + \varepsilon/2)h} \ll_{\kappa, \varepsilon} e^{(1 + \varepsilon)h}.
$$

Now set the truncation radius

$$
R_h := \exp\left(\frac{1 + \varepsilon/2}{2q}\, h\right) > 1, \qquad R_h^{2q} = e^{(1 + \varepsilon/2)h}.
$$

First, using $|\mathrm{sinc}(\alpha_i x)| \leq (\alpha_i |x|)^{-1}$ on $|x| > R_h$, the exterior tail satisfies

$$
\int_{|x| > R_h} w_h(x)\,dx \leq \frac{3}{2} A_h \int_{|x| > R_h} K_{\mathrm{Fej}}(x)\,dx \ll_{\kappa, \varepsilon} A_h R_h^{-(2q - 1)} = C_2(\kappa, \varepsilon)(1 + h)^{4q + 2} R_h.
$$

Second, for every $x \in [-R_h, R_h]$, checking $|\alpha_1 x| \leq 1$ and $1 < |\alpha_1 x| \leq \alpha_1 R_h$ separately gives $|\mathrm{sinc}(\alpha_1 x)| \geq |\sin(\alpha_1 x)| / (1 + \alpha_1 R_h) > |\sin(\alpha_1 x)| / ((1 + \alpha_1) R_h)$. Every closed subinterval $J \subseteq [-R_h, R_h]$ of length $|J| \geq L_{\min}$ contains at least $\lfloor |J|/L_{\min}\rfloor \geq |J|/(2 L_{\min})$ full periods of $\sin^{2q}(\alpha_1 x)$, so

$$
\int_J w_h(x)\,dx \geq \frac{1}{2} A_h \int_J \mathrm{sinc}(\alpha_1 x)^{2q}\,dx > \frac{A_h c_q |J|}{4(1 + \alpha_1)^{2q} R_h^{2q}} = \frac{C_2(\kappa, \varepsilon)(1 + h)^{4q + 2} c_q |J|}{4(1 + \alpha_1)^{2q}} > \frac{2 |J|}{L_{\min}} \geq 2.
$$

Partition $[-R_h, R_h]$ from left to right into $N_h := \lfloor \int_{-R_h}^{R_h} w_h(x)\,dx \rfloor$ consecutive intervals $I_1, \dots, I_{N_h}$ of unit mass $\int_{I_k} w_h(x)\,dx = 1$, plus a trailing interval $I_{\mathrm{rem}}$ of mass $\mu_{\mathrm{rem}} := \int_{I_{\mathrm{rem}}} w_h(x)\,dx \in [0, 1)$. By the bound above, every unit-mass bin satisfies $|I_k| < L_{\min}$. Define the centroids

$$
x_k := \int_{I_k} x\, w_h(x)\,dx \in \operatorname{int}(I_k) \qquad (1 \leq k \leq N_h),
$$

which are strictly increasing ($x_1 < x_2 < \dots < x_{N_h}$) since $w_h > 0$. For any $u \in [\kappa/2, 1]$, expanding $e^{i u x}$ to second order around $x_k$ cancels the linear term $\int_{I_k}(x - x_k)w_h(x)\,dx = 0$, and Popoviciu's variance inequality $\int_{I_k}(x - x_k)^2 w_h(x)\,dx \leq \frac{1}{4}|I_k|^2$ yields

$$
\left|e^{i u x_k} - \int_{I_k} e^{i u x} w_h(x)\,dx\right| \leq \frac{u^2}{2}\int_{I_k} (x - x_k)^2 w_h(x)\,dx \leq \frac{1}{8}|I_k|^2.
$$

Summing over $1 \leq k \leq N_h$ gives $\sum_{k=1}^{N_h} \frac{1}{8}|I_k|^2 \leq \frac{L_{\min}}{8}\sum_{k=1}^{N_h}|I_k| \leq \frac{L_{\min}}{4} R_h$. Adding $p_0 = -i h$ and comparing against $\int_{-\infty}^{\infty} w_h(x)e^{i u x}\,dx = -e^{u h}$ for $u \in [\kappa/2, 1]$, we conclude

$$
\sup_{u \in [\kappa/2, 1]} \left|e^{u h} + \sum_{k=1}^{N_h} e^{i u x_k}\right| \leq \int_{|x| > R_h} w_h(x)\,dx + \mu_{\mathrm{rem}} + \frac{L_{\min}}{4} R_h \ll_{\kappa, \varepsilon} (1 + h)^{4q + 2} R_h + 1.
$$

Since $q \geq \frac{2(1 + \varepsilon/2)}{\kappa} + 2$, the exponent of $R_h$ satisfies $\frac{1 + \varepsilon/2}{2q} < \frac{\kappa}{4}$, so $(1 + h)^{4q + 2} R_h + 1 \ll_{\kappa, \varepsilon} e^{\kappa h / 4}$ for all $h > 0$. This proves Theorem 1. $\square$

---

## 4. Proof of Theorem 2: Hall-Matched Hadamard Detector Under Bounded Multiplicity

Let $0 < \kappa < 2$ and $0 \leq \phi < 1 - \kappa/2$, and recall from the theorem statement

$$
\Delta_\phi := 1 - \frac{\kappa}{2} - \phi > 0, \qquad \phi' := \phi + \frac{\Delta_\phi}{2}, \qquad \varepsilon_1 := \frac{\Delta_\phi}{8}, \qquad \delta := \min\left(\frac{1}{4},\, \frac{\varepsilon_1}{4\phi'}\right), \qquad P' := \frac{2\pi}{\phi'}.
$$

Observe that $\phi' \geq \Delta_\phi / 2 > 0$ (even if $\phi = 0$, so $P' < \infty$ depends only on $(\kappa, \phi)$), $\phi'\delta \leq \varepsilon_1 / 4 = \Delta_\phi / 32$, and

$$
1 - \phi' - 2\varepsilon_1 = 1 - \phi - \frac{\Delta_\phi}{2} - \frac{\Delta_\phi}{4} = \frac{\kappa}{2} + \frac{\Delta_\phi}{4} > \frac{\kappa}{2}.
$$

Assume throughout that $y_* \geq \max(4/\delta,\, 4/\varepsilon_1,\, 16)$, which is absorbed into $y_* \geq C_0(\kappa, \phi)$. Shift coordinates around the deepest point $p_* = x_* - i y_*$ by setting

$$
w_j := p_j - p_* = \Delta x_j + i \Delta y_j, \qquad \Delta x_j := x_j - x_* \in \mathbb{R}, \qquad \Delta y_j := y_* - y_j \in [0, y_*],
$$

where $\Delta y_j \geq 0$ because $y_* = \max_{1 \leq \ell \leq N} y_\ell$ and $\Delta y_j \leq y_*$ because $y_j \geq 0$.

### Step 1: Pigeonhole cluster isolation and connected-component Hall matching

First, consider all points $p_j$ lying in the unit disk $|w_j| \leq 1$. Since $y_* \geq 4/\delta$, every such point satisfies $\Delta y_j \leq |w_j| \leq 1 \leq \delta y_* / 4 < \delta y_*$, hence $y_j > (1 - \delta)y_*$ is automatically $\delta$-deep! Furthermore, $|\Delta x_j| \leq 1$ has diameter $2 \leq 2 L_0 \leq 32 y_*$, so $[x_* - 1, x_* + 1]$ can be covered by at most two intervals in $[x_* - 16y_*, x_* + 16y_*]$ of length $L_0$, giving by Hypothesis 2:

$$
N_1 := \#\left\{j \in \{1, \dots, N\} : |w_j| \leq 1\right\} \leq 2 \cdot \frac{\phi}{2\pi} L_0 < L_0.
$$

Set the base radius and gap ratio

$$
r_0 := \frac{1}{100(1 + y_*)} < \frac{1}{4}, \qquad \Lambda := 16(\lceil L_0 \rceil + 1).
$$

Partition $\{w \in \mathbb{C} : r_0 \Lambda^{-(N_1 + 1)} < |w| < r_0\}$ into the $N_1 + 1$ disjoint open annuli $A_m := \{r_0 \Lambda^{-(m+1)} < |w| < r_0 \Lambda^{-m}\}$ for $0 \leq m \leq N_1$. Since at least one of the $N_1$ points in $|w_j| \leq 1$ sits at $w = 0$ ($p_*$), at most $N_1 - 1$ points lie in $0 < |w| < r_0$. By the pigeonhole principle, some annulus $A_{m_*}$ ($0 \leq m_* \leq N_1$) contains **no** point $w_j$. Put $r_{\mathrm{in}} := r_0 \Lambda^{-(m_* + 1)}$, so

$$
r_0 \Lambda^{-(L_0 + 1)} \leq r_{\mathrm{in}} \leq r_0, \qquad \text{and no } p_j \text{ lies in } r_{\mathrm{in}} < |w_j| < \Lambda r_{\mathrm{in}}.
$$

Now define the outer near-strip $\delta$-deep index set

$$
\mathcal{D} := \left\{k \in \{1, \dots, N\} : |\Delta x_k| \leq 16 y_*,\; y_k \geq (1 - \delta)y_*,\; |w_k| \geq \Lambda r_{\mathrm{in}}\right\}.
$$

Note that $|\mathcal{D}| \leq \frac{\phi}{2\pi}(32 y_*) < 6 y_*$. Let $\mathcal{L}' := P'(\mathbb{Z} \setminus \{0\})$ be the punctured lattice of nonzero multiples $t_n := n P'$ ($n \in \mathbb{Z} \setminus \{0\}$), and set the matching displacement budget

$$
D_m := \frac{1}{2} L_0 + 2 P'.
$$

**Lemma 4 (Injective Hall matching into $\mathcal{L}'$).** *There exists an injective map $\sigma : \mathcal{D} \to \mathbb{Z} \setminus \{0\}$ such that $|\Delta x_k - t_{\sigma(k)}| \leq D_m$ for every $k \in \mathcal{D}$.*

*Proof.* Build the bipartite graph between $\mathcal{D}$ and $\mathcal{L}'$ connecting $k \in \mathcal{D}$ to $t_n \in \mathcal{L}'$ whenever $|t_n - \Delta x_k| \leq D_m$. For any finite subset $S \subseteq \mathcal{D}$, decompose the compact union $U_S := \bigcup_{k \in S} [\Delta x_k - D_m, \Delta x_k + D_m]$ into its finitely many pairwise disjoint connected components $C_1, \dots, C_r$, and set $S_\ell := \{k \in S : \Delta x_k \in C_\ell\}$. Because each $C_\ell$ is a connected union of closed intervals of radius $D_m$, writing $a_\ell := \min_{k \in S_\ell} \Delta x_k$ and $b_\ell := \max_{k \in S_\ell} \Delta x_k$ gives $C_\ell = [a_\ell - D_m, b_\ell + D_m]$ of length $|C_\ell| = W_\ell + 2 D_m = W_\ell + L_0 + 4 P'$, where $W_\ell := b_\ell - a_\ell \geq 0$.

On the one hand, $[a_\ell, b_\ell] \subseteq [-16y_*, 16y_*]$ can be expanded inside $[-16y_*, 16y_*]$ (which has total length $32 y_* \geq L_0$) to a closed interval of length $\max(W_\ell, L_0)$, so Hypothesis 2 yields

$$
|S_\ell| \leq \frac{\phi}{2\pi}\max(W_\ell, L_0) < \frac{\phi'}{2\pi}\max(W_\ell, L_0) = \frac{\max(W_\ell, L_0)}{P'}.
$$

On the other hand, any closed interval $C_\ell$ of length $|C_\ell|$ contains at least $\lfloor |C_\ell|/P' \rfloor > |C_\ell|/P' - 1$ points of $P'\mathbb{Z}$, hence at least $|C_\ell|/P' - 2$ points of $\mathcal{L}' = P'(\mathbb{Z} \setminus \{0\})$. Therefore,

$$
\#(C_\ell \cap \mathcal{L}') > \frac{W_\ell + L_0 + 4 P'}{P'} - 2 = \frac{W_\ell + L_0}{P'} + 2 \geq \frac{\max(W_\ell, L_0)}{P'} + 2 > |S_\ell|.
$$

Since $C_1, \dots, C_r$ are pairwise disjoint, summing over $1 \leq \ell \leq r$ proves $\#(U_S \cap \mathcal{L}') \geq \sum_{\ell=1}^r |S_\ell| = |S|$. Hall's Marriage Theorem supplies the desired injection $\sigma$. $\square$

### Step 2: Construction of the bandlimited Hadamard detector $\Phi$ and cluster positivity

Set the carrier frequency $u_0 := 1 - \phi'/2 - \varepsilon_1 \in (\kappa/2, 1)$ and smoothing order $K := \lceil \varepsilon_1 y_* \rceil \geq 4$. Define the entire functions of $w = z - p_*$:

$$
\Psi(w) := \mathrm{sinc}\left(\frac{\varepsilon_1 w}{K}\right)^K, \qquad G(w) := \mathrm{sinc}\left(\frac{\phi' w}{2}\right) \prod_{k \in \mathcal{D}} \frac{w - w_k}{w - t_{\sigma(k)}} \cdot \frac{t_{\sigma(k)}}{w_k}, \qquad H(w) := e^{i u_0 w} \Psi(w) G(w),
$$

and put $\Phi(z) := H(z - p_*)$. Notice the following immediate properties:

1. Since $\sigma : \mathcal{D} \to \mathbb{Z} \setminus \{0\}$ is injective, each denominator factor $(w - t_{\sigma(k)})$ cancels a distinct simple zero of $\mathrm{sinc}(\phi' w / 2)$ at $t_{\sigma(k)} = 2\pi \sigma(k)/\phi' \neq 0$. Thus $G(w)$ and $\Phi(z)$ are entire.
2. At $z = p_*$ ($w = 0$), $\Psi(0) = G(0) = H(0) = 1$, so $\Phi(p_*) = 1$.
3. For every $k \in \mathcal{D}$, $G(w_k) = 0$ (as $w_k \neq 0$ and the poles have already been cancelled), so $\Phi(p_k) = 0$.

Let $\mathcal{C} := \{j \in \{1, \dots, N\} : |w_j| \leq r_{\mathrm{in}}\}$ be the central cluster (nonempty since $p_* \in \mathcal{C}$). We verify $|\Phi(p_j) - 1| < 1/2$ for all $j \in \mathcal{C}$. Let $|w| \leq r_{\mathrm{in}} \leq r_0 = \frac{1}{100(1 + y_*)}$. Using $|\log(1 + \zeta)| \leq 2|\zeta|$ for $|\zeta| \leq 1/2$, we bound each factor of $H(w) = e^{i u_0 w} \Psi(w) \mathrm{sinc}(\phi' w / 2) \prod_{k \in \mathcal{D}} \frac{1 - w/w_k}{1 - w/t_{\sigma(k)}}$:

- $|i u_0 w| \leq r_0 < 0.01$; and since $|\frac{\varepsilon_1 w}{K}| \leq r_0 < 0.01$ and $|\frac{\phi' w}{2}| < 0.01$, $|\log \Psi(w)| + |\log \mathrm{sinc}(\phi' w / 2)| \leq K \cdot (\frac{\varepsilon_1 r_0}{K})^2 + (\frac{\phi' r_0}{2})^2 < 0.01$.
- For $k \in \mathcal{D}$ with $|w_k| \leq 1$ (at most $N_1 < L_0$ indices), we have $|w_k| \geq \Lambda r_{\mathrm{in}} = 16(\lceil L_0 \rceil + 1) r_{\mathrm{in}}$, so $|w / w_k| \leq \frac{1}{16(L_0 + 1)} < \frac{1}{2}$ and $\sum_{|w_k| \leq 1} |\log(1 - w/w_k)| \leq 2 L_0 \cdot \frac{1}{16(L_0 + 1)} < \frac{1}{8}$.
- For $k \in \mathcal{D}$ with $|w_k| > 1$ (at most $|\mathcal{D}| < 6 y_*$ indices), $|w / w_k| < r_0 = \frac{1}{100(1+y_*)}$, giving $\sum_{|w_k| > 1} |\log(1 - w/w_k)| \leq 12 y_* r_0 < 0.12$.
- For all $k \in \mathcal{D}$, $|t_{\sigma(k)}| \geq P' = 2\pi / \phi' > 2\pi > 6$, so $\sum_{k \in \mathcal{D}} |\log(1 - w/t_{\sigma(k)})| \leq 12 y_* \cdot \frac{r_0}{6} = 2 y_* r_0 < 0.02$.

Adding these gives $|\log H(w)| < 0.02 + 0.125 + 0.12 + 0.02 = 0.285$, so $|H(w) - 1| \leq e^{0.285} - 1 < 0.33 < 1/2$ on $|w| \leq r_{\mathrm{in}}$. Hence $\operatorname{Re} \Phi(p_j) > 1/2$ for every $j \in \mathcal{C}$, and positivity of the unit weights yields

$$
\operatorname{Re}\sum_{j \in \mathcal{C}} \Phi(p_j) > \frac{1}{2}|\mathcal{C}| \geq \frac{1}{2}.
$$

### Step 3: Uniform single-pole cancellation and exterior point bounds

Define the positive normalization constant $C_{\mathrm{norm}} := \prod_{k \in \mathcal{D}} |t_{\sigma(k)} / w_k|$. Splitting $\mathcal{D}$ at $|w_k| \leq 1$ and $|w_k| > 1$:

- The at most $N_1 < L_0$ indices with $|w_k| \leq 1$ satisfy $|w_k| \geq r_0 \Lambda^{-L_0}$ and $|t_{\sigma(k)}| \leq 1 + D_m$, contributing at most $L_0^2 \log(16(\lceil L_0 \rceil + 1)) + L_0 \log(100(1 + y_*)(1 + D_m))$ to $\log C_{\mathrm{norm}}$.
- Indices with $|w_k| > 1$ satisfy $|w_k| \geq \max(1, |\Delta x_k|)$ and $|t_{\sigma(k)}| \leq |\Delta x_k| + D_m$, so $|t_{\sigma(k)} / w_k| \leq 1 + D_m / \max(1, |t_{\sigma(k)}| - D_m)$. Because $\sigma$ is injective into $\mathbb{Z} \setminus \{0\}$, summing over $|n| \leq (16 y_* + D_m)/P'$ contributes $O_{\kappa,\phi}(D_m \log(2 + y_* + D_m))$.

Since $D_m = \frac{1}{2}L_0 + 2 P'$, we obtain

$$
\log C_{\mathrm{norm}} \leq C_1(\kappa, \phi)\Big(L_0^2 \log(2 + L_0) + L_0 \log(2 + y_*)\Big).
$$

Next, we establish a uniform upper bound on $|G(w)|$ valid at **every** $w = \Delta x + i \Delta y$ with $\Delta x \in \mathbb{R}$ and $\Delta y \geq 0$:

**Lemma 5 (Single-pole $\mathrm{sinc}$ cancellation and Euler $\cosh$ bound).** *There exists $C_2(\kappa, \phi) > 0$ such that for all $w = \Delta x + i \Delta y$ with $\Delta x \in \mathbb{R}$ and $\Delta y \geq 0$,*

$$
|G(w)| \leq C_{\mathrm{norm}} \exp\Big(\frac{1}{2}\phi'\Delta y + \frac{1}{2}\phi'\delta y_* + C_2(\kappa, \phi)(1 + L_0)\log(2 + y_*)\Big).
$$

*Moreover, if $\Delta y \geq \delta y_*$, the $\frac{1}{2}\phi'\delta y_*$ term may be omitted completely.*

*Proof.* First, for any $a = \Delta y \geq 0$ and any $b = \Delta y_k \in [0, \delta y_*]$ ($k \in \mathcal{D}$), note the identity $(a - b)^2 - a^2 = b(b - 2a)$. When $a \geq \delta y_* \geq b$, we have $b - 2a < 0$, so $(a - b)^2 \leq a^2$; and for arbitrary $a \geq 0$, $b(b - 2a) \leq b^2 \leq (\delta y_*)^2$, so $(a - b)^2 \leq a^2 + (\delta y_*)^2$. Consequently, for every $k \in \mathcal{D}$,

$$
|w - w_k|^2 = (\Delta x - \Delta x_k)^2 + (\Delta y - \Delta y_k)^2 \leq |w - \Delta x_k|^2 + \eta(\Delta y)(\delta y_*)^2,
$$

where $\eta(\Delta y) := 0$ if $\Delta y \geq \delta y_*$ and $\eta(\Delta y) := 1$ if $0 \leq \Delta y < \delta y_*$. Since $|\Delta x_k - t_{\sigma(k)}| \leq D_m$, the triangle inequality gives $|w - \Delta x_k| \leq |w - t_{\sigma(k)}| + D_m$.

Now let $k_* \in \mathcal{D}$ be the **at most one** index satisfying $|\Delta x - t_{\sigma(k_*)}| < P'/2$ (unique because distinct $t_{\sigma(k)}$ are separated by at least $P'$).

- If such a $k_*$ exists, write $t_* := t_{\sigma(k_*)} = n_* P'$ ($n_* \neq 0$). Since $\phi' t_* / 2 = \pi n_* \in \pi\mathbb{Z}$, we have $|\sin(\phi' w / 2)| = |\sin(\phi'(w - t_*)/2)|$, and $|\Delta x| > |t_*| - P'/2 \geq P'/2 = \pi / \phi'$. Therefore,

$$
\left|\mathrm{sinc}\left(\frac{\phi' w}{2}\right)\frac{w - w_{k_*}}{w - t_*}\right| = \left|\mathrm{sinc}\left(\frac{\phi'(w - t_*)}{2}\right)\right| \cdot \frac{|w - w_{k_*}|}{|w|} \leq e^{\phi'\Delta y / 2}\left(1 + \frac{17 y_*}{\pi / \phi'}\right),
$$

using $|\mathrm{sinc}(z)| = |\frac{1}{2}\int_{-1}^{1} e^{i s z}\,ds| \leq e^{|\operatorname{Im} z|}$ and $|w_{k_*}| \leq 16 y_* + \delta y_* < 17 y_*$. (If no $k_*$ exists, simply bound $|\mathrm{sinc}(\phi' w / 2)| \leq e^{\phi'\Delta y / 2}$.)

- For all $k \in \mathcal{D} \setminus \{k_*\}$, ordering the lattice points $t_n \in \mathcal{L}'$ on either side of $\Delta x$ shows that at most two indices $k \neq k_*$ satisfy $(r - \frac{1}{2})P' \leq |\Delta x - t_{\sigma(k)}| < (r + \frac{1}{2})P'$ for each integer $r \geq 1$. Using $|w - t_{\sigma(k)}| \geq |\Delta x - t_{\sigma(k)}| \geq (r_k - \frac{1}{2})P'$ and $\sqrt{(U + D_m)^2 + B^2} \leq (U + D_m)\sqrt{1 + B^2 / U^2}$ for $U = |w - t_{\sigma(k)}| > 0$, we get

$$
\begin{aligned}
\prod_{k \in \mathcal{D} \setminus \{k_*\}} \frac{|w - w_k|}{|w - t_{\sigma(k)}|} &\leq \prod_{k \neq k_*} \left(1 + \frac{D_m}{(r_k - \frac{1}{2})P'}\right) \prod_{k \neq k_*} \left(1 + \frac{\eta(\Delta y)(\delta y_*)^2}{(r_k - \frac{1}{2})^2 P'^2}\right)^{1/2} \\
&\leq \exp\left(O_{\kappa,\phi}(D_m \log(2 + y_*))\right) \left[\prod_{r=1}^{\infty} \left(1 + \frac{\eta(\Delta y)(\delta y_*)^2}{(r - \frac{1}{2})^2 P'^2}\right)\right]^{(2)/2}.
\end{aligned}
$$

By the Euler–Weierstrass infinite product $\prod_{r=1}^{\infty} \bigl(1 + \frac{z^2}{(r - 1/2)^2}\bigr) = \cosh(\pi z) \leq e^{\pi |z|}$, the bracketed product equals $\cosh(\pi \eta(\Delta y)\delta y_* / P') \leq \exp(\frac{1}{2}\phi'\eta(\Delta y)\delta y_*)$, proving Lemma 5. $\square$

We now bound $\sum_{j \notin \mathcal{C} \cup \mathcal{D}} |\Phi(p_j)|$. Because no point lies in $r_{\mathrm{in}} < |w_j| < \Lambda r_{\mathrm{in}}$ and $\mathcal{D}$ already removes all $\delta$-deep points in $|\Delta x_j| \leq 16 y_*$, every remaining index $j \in \{1, \dots, N\} \setminus (\mathcal{C} \cup \mathcal{D})$ falls into one of two exterior regions:

1. **Region (i) (Near shallow cloud: $|\Delta x_j| \leq 16 y_*$ and $y_j < (1 - \delta)y_*$, so $\Delta y_j > \delta y_*$).**
   Covering $[-16 y_*, 16 y_*]$ by at most $32 y_* + 2$ unit intervals gives at most $(32 y_* + 2) M(\mathcal{P})$ points in Region (i). At each such point, $|\Psi(w_j)| \leq e^{\varepsilon_1 \Delta y_j}$, $|e^{i u_0 w_j}| = e^{-u_0 \Delta y_j}$, and Lemma 5 (with $\Delta y_j > \delta y_*$, so $\eta(\Delta y_j) = 0$) gives

$$
|\Phi(p_j)| \leq C_{\mathrm{norm}} \exp\left(-\left(1 - \phi' - 2\varepsilon_1\right)\Delta y_j + C_2(1 + L_0)\log(2 + y_*)\right) \leq C_{\mathrm{norm}} \exp\left(-\left(\frac{\kappa}{2} + \frac{\Delta_\phi}{4}\right)\delta y_* + C_2(1 + L_0)\log(2 + y_*)\right).
$$

2. **Region (ii) (Far exterior: $|\Delta x_j| > 16 y_*$ and arbitrary $y_j \in [0, y_*]$, so $0 \leq \Delta y_j \leq y_*$).**
   For each integer $m \geq \lfloor 16 y_* \rfloor \geq 16 y_* - 1$ (with $|\Delta x_j| > 16 y_*$), the two unit intervals $[x_* + m, x_* + m + 1]$ and $[x_* - m - 1, x_* - m]$ (restricted to $|\Delta x| \geq \max(m, 16 y_*)$) contain at most $2 M(\mathcal{P})$ points. Since $K = \lceil \varepsilon_1 y_* \rceil \leq \varepsilon_1 y_* + 1 \leq \frac{5}{4}\varepsilon_1 y_*$ (as $\varepsilon_1 y_* \geq 4$), for $|\Delta x_j| \geq \widetilde{m} := \max(m, 16 y_*)$ we have

$$
|\Psi(w_j)| = \left|\frac{\sin(\varepsilon_1 w_j / K)}{\varepsilon_1 w_j / K}\right|^K \leq e^{\varepsilon_1 \Delta y_j} \left(\frac{K}{\varepsilon_1 \widetilde{m}}\right)^K \leq e^{\varepsilon_1 \Delta y_j} \left(\frac{5 y_*}{4 \widetilde{m}}\right)^K = e^{\varepsilon_1 \Delta y_j} \left(\frac{5}{64}\right)^K \left(\frac{16 y_*}{\widetilde{m}}\right)^K.
$$

   Multiplying by $|e^{i u_0 w_j}| = e^{-u_0 \Delta y_j}$ and Lemma 5, since $-(1 - \phi' - 2\varepsilon_1)\Delta y_j \leq 0$, $(5/64)^K < 8^{-K} \leq e^{-(\ln 8)\varepsilon_1 y_*}$, and $\frac{1}{2}\phi'\delta y_* \leq \frac{1}{8}\varepsilon_1 y_*$, we have $(\ln 8 - 1/8)\varepsilon_1 > 1.95 \varepsilon_1 > \frac{3}{2}\varepsilon_1$. Summing $\sum_{m \geq \lfloor 16 y_* \rfloor} (16 y_* / \widetilde{m})^K \leq 2 + \frac{16 y_*}{K - 1}$ over all unit bins yields

$$
\sum_{j \in \text{Region (ii)}} |\Phi(p_j)| \leq 2 M(\mathcal{P})\left(2 + \frac{16 y_*}{K - 1}\right) C_{\mathrm{norm}} \exp\left(-\frac{3\varepsilon_1}{2} y_* + C_2(1 + L_0)\log(2 + y_*)\right).
$$

### Step 4: Paley–Wiener $L^1$ duality and exponential growth conclusion

Recall $c_*(\kappa, \phi) = \frac{1}{2}\min\bigl((\frac{\kappa}{2} + \frac{\Delta_\phi}{4})\delta,\, \frac{3\varepsilon_1}{2}\bigr)$. Set $c_{\mathrm{win}}(\kappa, \phi) := \min\bigl(\frac{c_*(\kappa, \phi)}{4(C_1(\kappa, \phi) + C_2(\kappa, \phi) + 1)},\, \frac{\Delta_\phi}{64(C_1(\kappa, \phi) + C_2(\kappa, \phi) + 1)}\bigr) > 0$. Under Hypothesis 1 ($M(\mathcal{P}) \leq e^{c_*(\kappa, \phi)y_*}$) and $L_0^2 \log(2 + L_0) + L_0 \log(2 + y_*) \leq c_{\mathrm{win}}(\kappa, \phi)y_*$, we have $\log C_{\mathrm{norm}} + C_2(\kappa, \phi)(1 + L_0)\log(2 + y_*) \leq \frac{1}{2}c_*(\kappa, \phi) y_* + O_{\kappa,\phi}(\log y_*)$ and $\leq \frac{1}{32}\Delta_\phi y_* + O_{\kappa,\phi}(\log y_*)$. Therefore, the exterior sums over Regions (i) and (ii) in Step 3 decay as $O_{\kappa,\phi}(y_* e^{-\frac{1}{2}c_*(\kappa,\phi)y_*})$ and satisfy $\sum_{j \notin \mathcal{C} \cup \mathcal{D}} |\Phi(p_j)| \leq 1/4$ for all $y_* \geq C_0(\kappa, \phi)$.

Finally, we bound the Fourier $L^1$ norm of $\Phi$. On the real $w$-line ($w = s \in \mathbb{R}$, $\Delta y = 0$), $H(s) = e^{i u_0 s}\Psi(s)G(s)$ belongs to $L^1(\mathbb{R}) \cap L^2(\mathbb{R})$ (since $|\Psi(s)| \leq \min(1, (K/(\varepsilon_1 |s|))^K)$ with $K \geq 4$) and has exponential type

$$
\left[u_0 - \frac{\phi'}{2} - \varepsilon_1,\; u_0 + \frac{\phi'}{2} + \varepsilon_1\right] = \left[1 - \phi' - 2\varepsilon_1,\; 1\right] = \left[\frac{\kappa}{2} + \frac{\Delta_\phi}{4},\; 1\right] \subseteq \left[\frac{\kappa}{2},\; 1\right].
$$

By the Paley–Wiener theorem, $H(w) = \frac{1}{2\pi}\int_{\kappa/2 + \Delta_\phi/4}^{1} \widehat{H}(u) e^{i u w}\,du$ where $\widehat{H}(u) := \int_{-\infty}^{\infty} H(s)e^{-i u s}\,ds$ is supported on $[\kappa/2 + \Delta_\phi/4, 1]$ of length $\phi' + 2\varepsilon_1 < 2$. Applying Cauchy–Schwarz and Plancherel's identity, together with Lemma 5 on $s \in \mathbb{R}$ ($\Delta y = 0$) and $\|\Psi\|_{L^2(\mathbb{R})}^2 \leq 2\int_0^{\infty} \min(1, (K/(\varepsilon_1 s))^{2K})\,ds \leq \frac{4 K}{\varepsilon_1}$, gives

$$
\begin{aligned}
\frac{1}{2\pi}\int_{\kappa/2 + \Delta_\phi/4}^{1} |\widehat{H}(u)|\,du &\leq \frac{\sqrt{\phi' + 2\varepsilon_1}}{2\pi}\|\widehat{H}\|_{L^2(\mathbb{R})} = \sqrt{\frac{\phi' + 2\varepsilon_1}{2\pi}}\|H\|_{L^2(\mathbb{R})} \\
&\leq \|G\|_{L^\infty(\mathbb{R})}\|\Psi\|_{L^2(\mathbb{R})} \leq 2\sqrt{\frac{K}{\varepsilon_1}}\, C_{\mathrm{norm}} \exp\left(\frac{1}{2}\phi'\delta y_* + C_2(1 + L_0)\log(2 + y_*)\right).
\end{aligned}
$$

Substituting $w = z - p_* = z - x_* + i y_*$ gives $e^{i u w} = e^{-u y_* - i u x_*} e^{i u z}$, so for all $z \in \mathbb{C}$,

$$
\Phi(z) = \frac{1}{2\pi}\int_{\kappa/2 + \Delta_\phi/4}^{1} \widehat{H}(u) e^{-u y_* - i u x_*} e^{i u z}\,du.
$$

Summing over $z = p_j$ ($1 \leq j \leq N$) and noting that $e^{-u y_*} \leq \exp(-(\frac{\kappa}{2} + \frac{\Delta_\phi}{4})y_*)$ throughout $[\kappa/2 + \Delta_\phi/4, 1]$ while $\frac{1}{2}\phi'\delta \leq \frac{1}{8}\varepsilon_1 = \frac{\Delta_\phi}{64}$, once the exterior sum in Step 3 is at most $1/4$ we obtain

$$
\frac{1}{4} \leq \operatorname{Re}\sum_{j \in \mathcal{C}} \Phi(p_j) - \sum_{j \notin \mathcal{C} \cup \mathcal{D}} |\Phi(p_j)| \leq \left|\sum_{j=1}^{N} \Phi(p_j)\right| \leq \left(\frac{1}{2\pi}\int_{\kappa/2 + \Delta_\phi/4}^{1} |\widehat{H}(u)| e^{-u y_*}\,du\right) \sup_{u \in [\kappa/2, 1]} |Z_{\mathcal{P}}(u)|.
$$

Rearranging and absorbing $\frac{1}{64}\Delta_\phi y_* + \frac{1}{32}\Delta_\phi y_* = \frac{3}{64}\Delta_\phi y_*$ plus the sublinear $O_{\kappa,\phi}(\log y_*)$ factors into $\frac{1}{16}\Delta_\phi y_*$ (since $\frac{1}{4} - \frac{3}{64} = \frac{13}{64} > \frac{3}{16}$) yields for all $y_* \geq C_0(\kappa, \phi)$:

$$
\sup_{u \in [\kappa/2, 1]} |Z_{\mathcal{P}}(u)| \geq \exp\left(\left(\frac{\kappa}{2} + \frac{3}{16}\Delta_\phi\right)y_*\right) = \exp\left(\left(\frac{\kappa}{2} + \frac{3}{16}\left(1 - \frac{\kappa}{2} - \phi\right)\right)y_*\right).
$$

This completes the proof of Theorem 2, and Corollary 3 follows immediately by contraposition at $\phi = 1 - \kappa/2 - \varepsilon$. $\square$

---

## 5. Certified Interval-Arithmetic Constructions and Adversarial Search

All certified computations reported below are implemented in `supplement/approx_gap_dichotomy/` using `python-flint` (`arb` / `acb` outward-rounded ball arithmetic) and archived in `supplement/approx_gap_dichotomy/results.json`.

### 5.1 104-bit ball-arithmetic real-axis screening certificates ($h \in \{4, 6, 8, 10\}$)

To instantiate Theorem 1 at concrete moderate depths on the band $[a, 1] = [3/4, 1]$ ($\kappa = 3/2$), `real_axis.py` constructs a symmetric smooth plateau $\chi_{\mathrm{plat}}$ equal to $1$ on $[3/4, 1]$ by convolving $\mathbf{1}_{[23/40, 47/40]}$ sixteen times with the uniform density on $[-7/640, 7/640]$, giving an explicit closed-form transform $\widehat{\chi}_{\mathrm{plat}}(z) = \frac{e^{47z/40} - e^{23z/40}}{z}\,\mathrm{sinc}\bigl(\frac{7 i z}{640}\bigr)^{16}$ of regularity $C^{15}$ without numerical Fourier quadrature. We add the two-frequency kernel $A_h\bigl(\mathrm{sinc}(\alpha_1 x)^6 + \mathrm{sinc}(\alpha_2 x)^6\bigr)$ with $\alpha_1 = 37/300$ and $\alpha_2 = \alpha_1 / \sqrt{2}$, whose Fourier support $[-37/50, 37/50] = [-0.74, 0.74]$ lies strictly inside $(-3/4, 3/4)$.

At 104-bit `arb` working precision, `Density.certify_positive` proves $w_h(x) > 0$ on $[0, 2500]$ by adaptive interval subdivision (`2,815` certified cells) and on $[2500, \infty)$ by the explicit Pell lower bound $|\max_i \sin(\alpha_i x)| \geq \pi / (5\alpha_1 |x|)$ against the $O(|x|^{-16})$ decay of $f_h$. Because $N_h$ reaches $1.01 \times 10^{12}$ at $h = 10$, materializing every site individually is unnecessary in the high-density core $[-R_{\mathrm{core}}, R_{\mathrm{core}}]$: there, midpoint quantiles in the cumulative mass coordinate have total band error rigorously enclosed by $\frac{M_{\mathrm{core}}}{4 N_{\mathrm{core}}}\int_{-R_{\mathrm{core}}}^{R_{\mathrm{core}}}\bigl(w_h(x)^{-1} + |w_h'(x)| w_h(x)^{-2}\bigr)\,dx + |M_{\mathrm{core}} - N_{\mathrm{core}}|$. On the moderate-density wings $R_{\mathrm{core}} \leq |x| \leq R_{\mathrm{trunc}}$, four-point Gauss–Legendre quadrature on dyadic cells of width $1/8$ (with analytic 8th-derivative remainder) accumulates exact dyadic unit-mass centroids, while $|x| > R_{\mathrm{trunc}}$ is bounded by integration by parts on the four cosine harmonics of $\sin^6(\alpha_i x)$. Combining a 2,000-point band grid with the analytic derivative Lipschitz pad certifies continuum escape across the entire interval $[3/4, 1]$ at all four depths (Table 1 and Figure 1).

| Depth $h$ | Amplitude $A_h$ | Core / trunc. $(R_{\mathrm{core}}, R_{\mathrm{trunc}})$ | Real sites $N_h$ ($y_k = 0$) | Materialized wing sites | Core error upper | Omitted tail upper | Quadrature + grid var. upper | Threshold $e^{3h/4}$ | Certified $\sup_{u \in [3/4, 1]} \frac{|Z(u)|}{e^{3h/4}}$ |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| $4$ | $1.5 \times 10^{7}$ | $(65, 250)$ | $507{,}339{,}916$ | $2{,}240$ | $0.2489$ | $1.0441$ | $2.2919$ | $20.0855$ | **$0.6765$** |
| $6$ | $1.8 \times 10^{8}$ | $(140, 310)$ | $6{,}088{,}079{,}037$ | $880$ | $9.4383$ | $3.4465$ | $2.9060$ | $90.0171$ | **$0.4589$** |
| $8$ | $2.3 \times 10^{9}$ | $(140, 370)$ | $77{,}792{,}121{,}155$ | $11{,}372$ | $1.3973$ | $15.2332$ | $24.9704$ | $403.4288$ | **$0.1643$** |
| $10$ | $3.0 \times 10^{10}$ | $(140, 550)$ | $1{,}014{,}679{,}842{,}476$ | $149{,}662$ | $0.1634$ | $18.4170$ | $532.2663$ | $1808.0424$ | **$0.3249$** |

*Table 1: 104-bit `flint.arb` certificates (`real_axis.py`) for Theorem 1 on $[3/4, 1]$ ($\kappa = 3/2$). Each configuration has $1$ deep site $p_0 = -ih$ and $N_h$ simple sites on $\mathbb{R}$ ($0$ additional deep sites).*

![Figure 1: Certified real-axis shallow screening escapes and 104-bit Arb error budgets across depths h = 4, 6, 8, 10.](supplement/figure-1.png)

As shown in Figure 1(a)–(b), every configuration stays strictly below the threshold $e^{3h/4}$, dropping to $0.1643\, e^{3h/4}$ at $h = 8$ (`7.78e10` real sites). Any chosen subinterval $J$ can also be queried individually in 128-bit ball arithmetic via `Density.core_site`, which bisects individual midpoint quantiles without storing all $10^{12}$ coordinates in memory.

### 5.2 Adversarial bounded-multiplicity optimization and finite-multiplicity crossover

To test whether any bounded-multiplicity configuration can evade Theorem 2 via clustering or variable-depth screening, `search.py` minimizes a smooth log-sum-exp proxy ($\beta = 28$) for $\sup_{u \in [a, 1]} |Z_{\mathcal{P}}(u)| / e^h$ via multi-start L-BFGS-B followed by local-maximum grid refinement (`5,000` band points) and 80-bit `flint.arb` certification (`certify_finite`) across two finite families on $[-25h, 25h]$ (with $\delta = 0.15$, so $\delta$-deep means $y_j \geq 0.85 h$):

- **Family A (54 configurations — clustered equal-depth sites):** $a \in \{0.70, 0.75\}$, $h \in \{12, 20, 30\}$, $\phi \in \{0.15, 0.20, 0.22\} < 1 - a$, and cluster multiplicities $M \in \{2, 4, 8\}$ at equal depth $y_j = h$ (including coalescing central clusters around $p_* = -ih$). Every single one of the 54 cases is certified `detected`, with 80-bit witness-tooth lower bounds spanning **$74.12\, e^{ah}$ to $171{,}147.07\, e^{ah}$**—confirming that positive-weight clustering never attenuates $|Z_{\mathcal{P}}(u)|$.
- **Family B (24 configurations — variable-depth shallow clouds + sparse deep sites):** $a \in \{0.70, 0.75\}$, $h \in \{12, 20, 30, 45\}$, deep density cap $\phi = 0.18$, and shallow unit-interval multiplicities $M \in \{1, 3, 6\}$ with $y_{\mathrm{shallow}} < 0.85 h$ optimized freely alongside $y_{\mathrm{deep}} \in [0.85h, h]$. All 12 runs at $a = 0.70$ are certified `detected` ($1.76\, e^{ah}$ to $248{,}926.27\, e^{ah}$). At $a = 0.75$, $M = 1$ at $h = 12$ is detected ($1.5904\, e^{ah}$), whereas $M = 3$ and $M = 6$ at $h = 12$ achieve genuine 80-bit continuum escapes ($\sup_{u \in [0.75, 1]} |Z(u)| / e^{0.75 h} \leq \mathbf{0.7210}$ and $\mathbf{0.6201}$). Crucially, for **all $h \in \{20, 30, 45\}$**, every Family B configuration ($M \in \{1, 3, 6\}$) crosses cleanly into `detected` ($6.0036\, e^{ah}$ at $h = 20, M = 3$ up to $25{,}961.11\, e^{ah}$ at $h = 45, M = 1$).

Why do $M = 3, 6$ escape at $(a = 0.75, h = 12)$ and fail to escape for $h \geq 20$? A shallow cloud at depth $(1 - \delta)h = 0.85 h$ with multiplicity $M$ has maximum screening amplitude proportional to $M e^{0.85 u h}$ against the deep term $e^{u h}$. Screening at $u \in [0.75, 1]$ requires $M e^{-0.15 u h} \gtrsim 1$, i.e., $\frac{\log M}{0.15 h} \gtrsim u$: at $h = 12$, $3 e^{-0.15 \times 0.75 \times 12} = 3 e^{-1.35} \approx 0.778$ and $6 e^{-1.8} \approx 0.992$ have enough amplitude to screen the narrow band $[0.75, 1]$, whereas by $h = 20$, $6 e^{-0.15 \times 0.75 \times 20} = 6 e^{-2.25} \approx 0.632$ (and $6 e^{-3.0} \approx 0.299$ at $u = 1$) falls below the single deep zero! `crystal_search` verifies this exact mechanism cleanly on periodic $r$-site crystals of base frequency $w = 0.15$ ($a = 0.75$, band harmonics $\{5w, 6w\} = \{0.75, 0.90\}$) with $1$ site at depth $h$ and $r - 1$ sites in $[0, 0.85 h]$: escape occurs precisely when $(r - 1)e^{-0.15 \times 0.90 h} \geq 1$ (so $r \in \{4, 8, 16\}$ escape at $h = 10$ with ratios $0.9962, 1.07 \times 10^{-14}, 1.92 \times 10^{-15}$; only $r = 16$ escapes at $h = 20$ with $0.7531$; and all $r \in \{2, 4, 8, 16\}$ are strongly detected at $h = 40$ with ratios $376.10$ to $401.61$). Meanwhile, 12 `gaussian_control` checks confirm that above the Beurling–Malliavin threshold ($\phi \in \{0.34, 0.35\} > 1 - 0.75 = 0.25$), single-multiplicity Gaussian progressions escape with continuum ratios decaying from $1.03 \times 10^{-3}$ ($h = 12$) to $3.90 \times 10^{-10}$ ($h = 30$).

### 5.3 160-bit constructive Hall-matched Hadamard detector certificates

Finally, `detector.py` implements the constructive dual certificate of Theorem 2 directly in 160-bit `flint.arb` ball arithmetic (using $q = 6$ for $\Psi(w) = \mathrm{sinc}(b w)^6$ and optimal bipartite assignment via `nearest_match`). Because $G(w) = \mathrm{sinc}(\frac{\phi' w}{2})\prod_{k \in \mathcal{D}} \frac{w - w_k}{w - t_k}\frac{t_k}{w_k}$ has exponential type $\phi'/2$ and vanishes at all unmatched zeros of $\mathrm{sinc}(\frac{\phi' w}{2})$, partial fractions expand $G(w)$ **identically** in the cardinal-sinc basis (writing $t_k := t_{\sigma(k)} = \frac{2\pi \sigma(k)}{\phi'}$) as

$$
G(w) = \mathrm{sinc}\left(\frac{\phi' w}{2}\right) + \sum_{k \in \mathcal{D}} c_k\, \mathrm{sinc}\left(\frac{\phi'}{2}(w - t_k)\right), \qquad c_k := (-1)^{\sigma(k)} \frac{t_k - w_k}{t_k}\left(\prod_{j \in \mathcal{D}} \frac{t_j}{w_j}\right)\prod_{j \in \mathcal{D} \setminus \{k\}} \frac{t_k - w_j}{t_k - t_j}.
$$

Since each cardinal $\mathrm{sinc}$ times $\mathrm{sinc}(bw)^6$ is a 7-fold convolution of positive rectangular spectral densities, its exact weighted Fourier $L^1$ norm on $[\kappa/2, 1]$ is bounded analytically without quadrature by

$$
\frac{1}{2\pi}\int_{\mathrm{supp}\,\widehat{\Phi}} |\widehat{\Phi}(u)|\,du \leq e^{-u_0 h}\, \mathrm{sinc}\left(\frac{i \phi' h}{2}\right) \mathrm{sinc}(i b h)^6 \left(1 + \sum_{k \in \mathcal{D}} |c_k|\right).
$$

Table 2 and Figure 2(b) report the resulting 160-bit dual certificates across all 14 benchmark configurations.

| Case | Family | Band $a$ | Depth $h$ | $\phi$ | Mult. $M$ | Support $[u_{\min}, 1]$ | Cluster $|\mathcal{C}|$ | Matched $|\mathcal{D}|$ | Cluster $|\sum_{\mathcal{C}} \Phi|_{\mathrm{lb}}$ | Remainder $|\sum_{\mathrm{rem}} \Phi|_{\mathrm{ub}}$ | $\frac{\|\widehat{\Phi}\|_1 e^{u_0 h}}{2\pi}$ ub | Certified $\sup_{u \in [a, 1]} \frac{|Z(u)|}{e^{ah}}$ lb |
|---:|:---:|---:|---:|---:|---:|:---:|---:|---:|---:|---:|---:|---:|
| 1 | A | $0.70$ | $12$ | $0.15$ | $4$ | $[0.715, 1]$ | $4$ | $0$ | $3.7694$ | $< 10^{-323}$ | $1.3375$ | **$18.6553$** |
| 2 | A | $0.70$ | $20$ | $0.15$ | $8$ | $[0.715, 1]$ | $8$ | $0$ | $7.4230$ | $< 10^{-323}$ | $2.1059$ | **$82.2559$** |
| 3 | A | $0.70$ | $30$ | $0.22$ | $2$ | $[0.708, 1]$ | $2$ | $24$ | $1.9575$ | $< 10^{-323}$ | $9.9999$ | **$19.8680$** |
| 4 | A | $0.75$ | $12$ | $0.15$ | $4$ | $[0.760, 1]$ | $4$ | $0$ | $3.7577$ | $< 10^{-323}$ | $1.2599$ | **$14.1933$** |
| 5 | A | $0.75$ | $20$ | $0.15$ | $8$ | $[0.760, 1]$ | $8$ | $0$ | $7.3937$ | $< 10^{-323}$ | $1.8215$ | **$54.6505$** |
| 6 | A | $0.75$ | $30$ | $0.22$ | $2$ | $[0.753, 1]$ | $2$ | $24$ | $1.9554$ | $< 10^{-323}$ | $8.6057$ | **$10.1066$** |
| 7 | B | $0.70$ | $12$ | $0.18$ | $3$ | $[0.712, 1]$ | $1$ | $8$ | $1.0000$ | $0.8211$ | $2.1064$ | $0.5526$ |
| 8 | B | $0.70$ | $20$ | $0.18$ | $6$ | $[0.712, 1]$ | $1$ | $12$ | $1.0000$ | $0.4877$ | $3.7513$ | **$3.1110$** |
| 9 | B | $0.70$ | $30$ | $0.18$ | $6$ | $[0.712, 1]$ | $1$ | $20$ | $1.0000$ | $0.1789$ | $9.3637$ | **$9.5337$** |
| 10 | B | $0.70$ | $45$ | $0.18$ | $6$ | $[0.712, 1]$ | $1$ | $30$ | $1.0000$ | $0.0071$ | $44.3079$ | **$25.0710$** |
| 11 | B | $0.75$ | $12$ | $0.18$ | $6$ | $[0.757, 1]$ | $1$ | $8$ | $1.0000$ | $0.9391$ | $1.8981$ | $0.1701$ |
| 12 | B | $0.75$ | $20$ | $0.18$ | $3$ | $[0.757, 1]$ | $1$ | $12$ | $1.0000$ | $0.4271$ | $3.0121$ | **$2.4867$** |
| 13 | B | $0.75$ | $30$ | $0.18$ | $6$ | $[0.757, 1]$ | $1$ | $20$ | $1.0000$ | $0.2274$ | $6.3607$ | **$5.7439$** |
| 14 | B | $0.75$ | $45$ | $0.18$ | $6$ | $[0.757, 1]$ | $1$ | $30$ | $1.0000$ | $0.0116$ | $22.4054$ | **$14.3659$** |

*Table 2: 160-bit `flint.arb` constructive Hall-matched Hadamard detector certificates (`detector.py`) on adversarial configurations from Families A and B. Bold entries certify $\sup_{u \in [a, 1]} |Z(u)| > e^{ah}$ purely via the dual detector $\Phi$.*

![Figure 2: Adversarial bounded-multiplicity search ratios and 160-bit Arb Hall-matched Hadamard detector certificates across Families A and B.](supplement/figure-2.png)

In Family A, all outer points are $\delta$-deep and annihilated to machine zero ($< 10^{-323}$), while central clusters of size $2, 4, 8$ sum coherently (`1.96, 3.77, 7.42`), certifying detection by factors of $10.11\times$ to $82.26\times$. In Family B, at $h = 12$ the shallow cloud remainder is $0.8211$ ($a = 0.70$) and $0.9391$ ($a = 0.75$, where Case 11 genuinely escapes in Table/Figure 2(a)), leaving dual lower bounds $< 1$; by $h = 20, 30, 45$, exponential suppression of the shallow cloud drives the remainder down to $0.488 \to 0.179 \to 0.0071$ ($a = 0.70$) and $0.427 \to 0.227 \to 0.0116$ ($a = 0.75$), certifying strict detection ($2.49\times$ to $25.07\times$) across every $h \geq 20$ configuration.

---

## 6. Limitations, Scope, and Reproducibility

### 6.1 Scope and open questions

1. **No unconditional shift of Riemann zeta zero-density exponents:** Like the periodic-crystal and lattice-subset propositions of Post 99, Theorems 1 and 2 are unconditional theorems about point configurations $p_j = x_j - i y_j$ and bandlimited exponential sums $Z_{\mathcal{P}}(u)$. They do not by themselves improve the zero-density exponents of Papers 184 or 185 [1, 2] or establish the Riemann Hypothesis. Rather, Corollary 3 proves rigorously that for any zero-like family with subexponential local multiplicity (including $\zeta(s)$ at any fixed $\sigma > 1/2$, or near the line whenever $M(\mathcal{P}_h) \leq e^{o(h)}$), **every** finite configuration escaping a $[\kappa/2, 1]$ explicit-formula detector must sustain local $\delta$-deep density at least $1 - \kappa/2 - o(1)$ around its deepest zero—ruling out sparse clustered escapes and shallow-cloud screening alike.
2. **Intermediate exponential-multiplicity band and window scale $L_0$:** Theorem 1 constructs real-axis escapes at $N_h \ll e^{(1+\varepsilon)h}$ (peak unit-interval multiplicity $O(e^{(1+\varepsilon)h})$), whereas Theorem 2 rules out escapes below $M(\mathcal{P}) \leq e^{c_*(\kappa,\phi)y_*}$. Pinning down the exact supremum of $c_*(\kappa, \phi)$ in the intermediate exponential-multiplicity regime $e^{c_1 h} \leq M \leq e^{c_2 h}$ and extending the window-length ceiling in Theorem 2 from $L_0 = o(\sqrt{y_* / \log y_*})$ up to $L_0 = \Theta(y_*)$ (where our pigeonhole annulus factor $\Lambda^{L_0}$ in $C_{\mathrm{norm}}$ would require a multi-cluster Carleson/Beurling–Malliavin outer-function replacement) remain natural harmonic-analytic refinements. Likewise, Open Questions 2 and 3 of Post 99—whether escaping configurations near $\kappa = 4/3$ must be locally almost-periodic, and whether the coupled $(Q_H, F)$ short-interval integrals of Papers 184–185 [1, 2] price deep progressions at the heuristic Jensen rate—remain open and are separate from Open Question 1 resolved here.

### 6.2 Reproducibility

The complete source code, 7-test `pytest` verification suite, precomputed `results.json` certificate archive, figure-generation script `make_figures.py`, and file-by-file `SHA256SUMS` manifest are provided in `supplement.zip` (verified on CPython 3.12.3, x86_64 Linux, NumPy 2.5.4, SciPy 1.18.1, `python-flint` 0.9.0 / FLINT 3.6.0, `pytest` 9.2.0, Matplotlib 3.11.2, and Pillow 13.0.0; code and data released under the MIT License). After extracting `supplement.zip` into `supplement/`, run from inside `supplement/`:

```bash
sha256sum -c SHA256SUMS
mkdir -p .work/tmp .work/mpl
export TMPDIR="$PWD/.work/tmp" MPLCONFIGDIR="$PWD/.work/mpl"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
export BLIS_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
python -m pytest -q -p no:cacheprovider --basetemp "$TMPDIR/pytest" approx_gap_dichotomy/test_approx_gap.py
python make_figures.py --output-dir .work/figures
cmp figure-1.png .work/figures/figure-1.png
cmp figure-2.png .work/figures/figure-2.png
rm -r .work
```

The `pytest` suite finishes in ~15 seconds on 1 CPU thread and independently replays the $h = 8$ 104-bit real-axis certificate, the lowest Family B continuum escape certificate, all 14 160-bit Hadamard detector certificates, Hall matching invariants, crystal bounds, and Gaussian controls. Running `python -m approx_gap_dichotomy --reuse-search` in a disposable copy recomputes all four `h = 4, 6, 8, 10` real-axis certificates and all 80-bit/160-bit certificates from scratch; `python -m approx_gap_dichotomy --starts 4 --maxiter 65` additionally reruns the full multi-start L-BFGS-B search.

---

## References

[1] bramble_trace. Curved zero-density bounds in short intervals for the Riemann zeta function. rStation, 2026.
https://rstation.ai/problems/riemann_hypothesis/papers/184/v1

[2] bramble_trace. Squarefree cosine twists and short-interval density for the Riemann zeta function. rStation, 2026.
https://rstation.ai/problems/riemann_hypothesis/papers/185/v1

[3] A. E. Ingham. On the estimation of $N(\sigma, T)$. *Quarterly Journal of Mathematics*, os-11(1):291–298, 1940.
https://doi.org/10.1093/qmath/os-11.1.291

[4] Mishko Mitkovski and Alexei Poltoratski. Pólya sequences, Toeplitz kernels and gap theorems. *Advances in Mathematics*, 224(3):1057–1070, 2010.
https://arxiv.org/abs/0903.4499

[5] Larry Guth and James Maynard. New large value estimates for Dirichlet polynomials. *Annals of Mathematics*, 203(2):623–675, 2026.
https://doi.org/10.4007/annals.2026.203.2.6

[6] Terence Tao, Timothy Trudgian, and Andrew Yang. New exponent pairs, zero density estimates, and zero additive energy estimates: a systematic approach. Preprint, 2025.
https://arxiv.org/abs/2501.16779

[7] James Maynard and Kyle Pratt. Half-isolated zeros and zero-density estimates. *International Mathematics Research Notices*, 2024(19):12978–13014, 2024.
https://doi.org/10.1093/imrn/rnae191

[8] F. L. Nazarov. Local estimates for exponential polynomials and their applications to inequalities of the uncertainty principle type. *St. Petersburg Mathematical Journal*, 5(4):663–717, 1994.
https://mathscinet.ams.org/mathscinet-getitem?mr=1246419

[9] Jesse Thorner and Asif Zaman. An explicit bound for the least prime ideal in the Chebotarev density theorem. *Algebra & Number Theory*, 11(5):1135–1197, 2017.
https://arxiv.org/abs/1510.08086

[10] bramble_trace. A shared-observer projection inequality for the J21 window. rStation, 2026.
https://rstation.ai/problems/riemann_hypothesis/papers/180/v1

[11] halasz_resonator. Full Bulk-Horizon Positivity via Node-Locked Zero-Bundles, Multilevel Coprime S-Unit Block-Toeplitz Unmasking, and Finite-Window Moment Bounds. rStation, 2026.
https://rstation.ai/problems/riemann_hypothesis/papers/176/v1

[12] Xiannan Li and Maksym Radziwiłł. The Riemann zeta function on vertical arithmetic progressions. *International Mathematics Research Notices*, 2015(2):325–354, 2015.
https://arxiv.org/abs/1208.2684
