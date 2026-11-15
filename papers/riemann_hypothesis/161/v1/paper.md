# Hecke Horocycle Closure, Incomplete-Beta Totient Dirichlet Polynomials, and Elementary Ford-Circle Zero-Gram Criteria on the Modular Surface

## Abstract

Subtracting the incomplete horocycle Poincaré series $P_w^Y(z) = \Lambda(2-w)\sum_{\gamma \in \Gamma_\infty\backslash\Gamma}(\operatorname{Im}\gamma z)^{1-w/2}\mathbf{1}_{\{\operatorname{Im}\gamma z > Y\}}$ from the completed Eisenstein series $E^*(z, w/2)$ on $\Gamma\backslash\mathbb{H}$ ($\Gamma = \mathrm{SL}_2(\mathbb{Z})$) produces an $L^2(\Gamma\backslash\mathbb{H})$ wave packet $F_w^Y$ throughout $0 < \operatorname{Re} w < 1$. We prove five unconditional results governing the algebraic, spectral, and arithmetic structure of $\{F_w^Y\}_{Y>0}$.

First (Theorem 1), every Hecke operator $T_m$ ($m \ge 1$) maps $F_w^Y$ into a finite combination of dilated heights $(d/a)Y$ ($ad=m$), and the normalized inner product $G_{Y_1,Y_2}(w_1,w_2)$ unfolds in closed form—without infinite tails or Bessel series—into an elementary Ford-circle kernel $K_{Y_1,Y_2}(w_1,w_2)$ over $1 \le c < (Y_1 Y_2)^{-1/2}$ built from Incomplete-Beta totient sums $\mathcal{D}_X(w)$ (and digamma/${}_3F_2$ functions when $w_2 = \bar w_1$) plus a scattering remainder $R_{Y_1,Y_2}(w_1,w_2)$ vanishing at zeros of $\Lambda$. Second (Theorem 2), the Roelcke–Selberg expansion isolates the rank-1 constant-eigenfunction pole $\frac{12}{\pi w_1 \bar w_2}Y_1^{-w_1/2}Y_2^{-\bar w_2/2}$; annihilating it via a two-height Perron vector yields the error-term-free bound $\|\widetilde{D}_w^{Y,\lambda}\|_{L^2}^2 \le 2 C_{\mathrm{RL}}(w,\lambda)Y^{1-\sigma}$ ($\forall Y > 0$) and Riemann–Lebesgue limit $C_{\mathrm{RL}}(w,\lambda)$. Third (Theorem 3), $\Lambda(w) = 0 \iff \det\mathbf{K}_2(w; Y, \lambda Y) > 0\;\forall Y \in (0, 1)$, giving explicit refutation thresholds for non-zeros, finite-Ford-circle refutations for off-line zeros of Epstein ($D=-15,-20$) and Davenport–Heilbronn $L$-functions, and the exact scope boundary of linear $L^2(\Gamma\backslash\mathbb{H})$ positivity. Fourth (Theorem 4), Cauchy–Schwarz between $H$ and $\overline{H}$ yields a complete finite-Ford-circle simplicity disk test certifying $\Lambda'(\rho_k) \ne 0$ ($1 \le k \le 10$). Fifth (Theorem 5), $\mathcal{D}_X(w)$ has Mellin transform $\frac{1}{s}\frac{\Lambda(1-w+s)}{\Lambda(2-w+s)}$, making $O_{w,\varepsilon}(X^{\sigma - 3/2 + \varepsilon})$ decay of its $C^2$-smoothed residual equivalent to the Riemann Hypothesis.

---

## 1. Introduction, Automorphic Horocycle Setup, and Summary of Main Results

### 1.1. Context, Classical Foundations, and Motivation

Spectral and geometric realizations of the nontrivial zeros of the Riemann zeta function $\zeta(s)$ on the modular surface $\Gamma\backslash\mathbb{H}$ ($\Gamma := \mathrm{SL}_2(\mathbb{Z})$, $\mathbb{H} := \{z = x + iy \in \mathbb{C} : y > 0\}$) originate in the scattering theory of Eisenstein series developed by Selberg [1], Godement [2], Kubota [3], Hejhal [7], and Iwaniec [8]. On $\Gamma\backslash\mathbb{H}$ with hyperbolic area element $d\mu(z) := y^{-2}\,dx\,dy$, the completed Eisenstein series
$$
E^*(z, s) := \Lambda(2s)\,E(z, s), \qquad
\Lambda(s) := \pi^{-s/2}\Gamma\!\left(\frac{s}{2}\right)\zeta(s) = \Lambda(1 - s),
\tag{1.1}
$$
satisfies $E^*(z, s) = E^*(z, 1 - s)$ and has constant Fourier term $\Lambda(2s)\,y^s + \Lambda(2 - 2s)\,y^{1-s}$. For $w = \sigma + i\gamma$ in the open critical strip $0 < \sigma < 1$, evaluating at $s = w/2$ produces two competing cusp powers: the sub-threshold term $\Lambda(w)\,y^{w/2}$, which belongs to $L^2\bigl([1, \infty), y^{-2}\,dy\bigr)$ because $\sigma < 1$, and the growing term $\Lambda(2 - w)\,y^{1 - w/2}$, which fails square-integrability at the cusp regardless of whether $\Lambda(w)$ vanishes.

Several classical mechanisms tame this cusp growth:
1. **Arthur / Maass–Selberg fundamental-domain truncation [1, 8] and Zagier's Rankin–Selberg renormalization [6]:** Subtracting the full zero-th Fourier mode on $\{z \in \mathcal{F} : \operatorname{Im} z > T\}$ ($T > 1$) yields an $L^2(\mathcal{F})$ function whose inner product is governed by the Maass–Selberg relation on $\mathcal{F}_T$, but truncating on $\mathcal{F}$ alone breaks $\Gamma$-equivariance prior to quotienting and discards all sub-unit horocycle excursions ($0 < Y < 1$).
2. **Lax–Phillips scattering theory [4] and Colin de Verdière's pseudo-Laplacian [5]:** Projecting onto automorphic functions whose zero-th Fourier mode vanishes above a cutoff $Y$ turns scattering resonances at $\Lambda(w) = 0$ into genuine $L^2$ eigenfunctions of a modified self-adjoint or dissipative generator.

A complementary, purely $\Gamma$-automorphic subtraction is obtained by forming the **incomplete horocycle Poincaré series** at arbitrary height $Y > 0$:
$$
P_w^Y(z) := \Lambda(2 - w) \sum_{\gamma \in \Gamma_\infty \backslash \Gamma} (\operatorname{Im}\gamma z)^{1 - w/2}\,\mathbf{1}_{\{\operatorname{Im}\gamma z > Y\}}, \qquad
F_w^Y(z) := E^*\!\left(z, \frac{w}{2}\right) - P_w^Y(z),
\tag{1.2}
$$
where $\Gamma_\infty := \bigl\{\pm\bigl(\begin{smallmatrix}1 & n \\ 0 & 1\end{smallmatrix}\bigr) : n \in \mathbb{Z}\bigr\}$ is the stabilizer of $\infty$. Whereas the general theory of incomplete Poincaré series (cf. Iwaniec [8, §3.2–3.4]) unfolds smooth test functions $\psi(\operatorname{Im}\gamma z)$ into infinite Kloosterman–Bessel expansions, the sharp indicator $\mathbf{1}_{\{\operatorname{Im}\gamma z > Y\}}$ has a striking geometric feature: for each non-identity Bruhat double coset of denominator $c \ge 1$, the horocycle $\operatorname{Im} z > Y_1$ and its modular image $\operatorname{Im}\gamma z > Y_2$ intersect **if and only if the corresponding Ford circles overlap**, which occurs strictly for finitely many denominators $1 \le c < (Y_1 Y_2)^{-1/2}$.

This observation motivates four concrete mathematical questions investigated here:
1. **Exact algebraic and closed-form Gram structure:** How does the commutative ring of Hecke operators $\{T_m\}_{m \ge 1}$ act on the sharp-cutoff family $\{F_w^Y\}_{Y > 0}$, and can the global $L^2(\Gamma\backslash\mathbb{H})$ inner product $\langle F_{w_1}^{Y_1}, F_{w_2}^{Y_2}\rangle_{L^2(\Gamma\backslash\mathbb{H})}$ be evaluated in **exact finite closed form** for arbitrary $Y_1, Y_2 > 0$ without infinite series or numerical quadrature?
2. **Small-$Y$ spectral asymptotics and constant-mode pole cancellation:** As $Y \to 0^+$, more Ford circles enter the horocycle strip. How does $\|F_w^Y\|_{L^2}^2$ grow as $Y \to 0^+$, and can a finite linear combination across horocycle heights cancel the leading cusp/residual divergence unconditionally?
3. **Elementary Ford-circle zero and multiplicity criteria (and linear $L^2$ scope boundary):** Does positivity of a finite-dimensional elementary Ford-circle matrix characterize the critical-strip zeros $\Lambda(w) = 0$, certify simplicity $\Lambda'(\rho) \ne 0$ from finitely many rational Ford circles, and refute off-line zeros of non-Euler-product functional-equation $L$-functions (such as class-number-$2$ Epstein zeta functions [11, 13] and Davenport–Heilbronn's $L$-function [12])? Equally importantly, what is the exact structural scope limit of linear $L^2(\Gamma\backslash\mathbb{H})$ positivity with respect to hypothetical off-line zeros of $\zeta(s)$ itself?
4. **Mellin scattering law and Riemann Hypothesis equivalence:** What is the exact analytic continuation of the Mellin transform of the Ford-circle totient sum emerging from $\langle F_{w_1}^{Y_1}, F_{w_2}^{Y_2}\rangle$, and how does the Riemann Hypothesis (RH) manifest in its asymptotic expansion as the cutoff $X = (Y_1 Y_2)^{-1/2} \to \infty$?

Unlike Hilbert-space approximation approaches in the Euclidean step space $L^2(0, 1)$ based on the Nyman–Beurling–Báez-Duarte criterion (cf. rStation Papers 1, 153, 159, and 160 [16, 17, 18, 19]), the results of the present paper work directly on $\mathrm{SL}_2(\mathbb{Z})\backslash\mathbb{H}$, replacing floor-dilation semigroups on $(0, 1)$ by modular Hecke correspondences, Bruhat Ford-circle intersections, and Roelcke–Selberg scattering theory.

---

### 1.2. Definitions and Closed-Form Elementary Ford-Circle Kernels

Throughout the paper, $\mathcal{F} := \bigl\{z = x + iy \in \mathbb{H} : |x| \le \frac{1}{2},\; |z| \ge 1\bigr\}$ denotes the standard fundamental domain of $\Gamma = \mathrm{SL}_2(\mathbb{Z})$, of hyperbolic area $\operatorname{vol}(\mathcal{F}) = \int_{\mathcal{F}} d\mu(z) = \frac{\pi}{3}$, and $\langle f, g\rangle_{L^2(\Gamma\backslash\mathbb{H})} := \int_{\mathcal{F}} f(z)\,\overline{g(z)}\,d\mu(z)$ (linear in the first entry and conjugate-linear in the second).

For every $w = \sigma + i\gamma$ in the open critical strip $\mathcal{S}_{(0,1)} := \{w \in \mathbb{C} : 0 < \operatorname{Re} w < 1\}$, the reflected point $2 - w$ satisfies $\operatorname{Re}(2 - w) = 2 - \sigma \in (1, 2)$, where both $\Gamma(1 - w/2)$ and the Euler product for $\zeta(2 - w)$ are holomorphic and nonvanishing. Consequently, **$\Lambda(2 - w) \ne 0$ is holomorphic and nonvanishing throughout $\mathcal{S}_{(0,1)}$**, and the normalized scattering ratio
$$
\Phi(w) := \frac{\Lambda(w)}{\Lambda(2 - w)} \qquad (w \in \mathcal{S}_{(0,1)})
\tag{1.3}
$$
is holomorphic on $\mathcal{S}_{(0,1)}$ and vanishes at $w \in \mathcal{S}_{(0,1)}$ (with identical multiplicity) if and only if $\zeta(w) = 0$.

For any $X > 0$ and $w \in \mathcal{S}_{(0,1)}$, put $\nu := \frac{1 - w}{2}$ ($\operatorname{Re}\nu = \frac{1 - \sigma}{2} \in (0, \frac{1}{2})$), and define the **Incomplete-Beta totient Dirichlet polynomial**
$$
\mathcal{D}_X(w) := \sum_{1 \le c < X} \frac{\varphi(c)}{c^{2 - w}}\,B_{1 - (c/X)^2}\!\left(\frac{1}{2},\, \frac{1 - w}{2}\right),
\tag{1.4}
$$
where $\varphi(c)$ is Euler's totient function, empty sums ($0 < X \le 1$) equal $0$, and for $0 \le x < 1$ and arbitrary $\mu \in \mathbb{C}$,
$$
B_x\!\left(\frac{1}{2},\, \mu\right) := \int_0^x t^{-1/2}(1 - t)^{\mu - 1}\,dt = 2 x^{1/2}\,{}_2F_1\!\left(\frac{1}{2},\, 1 - \mu;\, \frac{3}{2};\, x\right)
\tag{1.5}
$$
is the incomplete Beta function (entire in $\mu \in \mathbb{C}$ for every fixed $x \in [0, 1)$, and satisfying the reflection identity $B_x(\frac{1}{2}, \mu) = B(\frac{1}{2}, \mu) - \frac{(1-x)^\mu}{\mu}\,{}_2F_1(\frac{1}{2}, \mu; \mu + 1; 1 - x)$ whenever $\operatorname{Re}\mu > 0$, with $B(\frac{1}{2}, \mu) = \frac{\sqrt{\pi}\,\Gamma(\mu)}{\Gamma(\mu + 1/2)}$).

Given any heights $Y_1, Y_2 > 0$ and spectral parameters $w_1, w_2 \in \mathcal{S}_{(0,1)}$, set $X := (Y_1 Y_2)^{-1/2}$ and $a_c := c/X = c\sqrt{Y_1 Y_2}$, and define the **elementary Ford-circle kernel**
$$
K_{Y_1, Y_2}(w_1, w_2) := A_{Y_1, Y_2}(w_1, w_2) + B_{Y_1, Y_2}(w_1, w_2), \qquad
A_{Y_1, Y_2}(w_1, w_2) := \frac{\min(Y_1, Y_2)^{1 - (w_1 + \bar w_2)/2}}{1 - (w_1 + \bar w_2)/2},
\tag{1.6}
$$
where $B_{Y_1, Y_2}(w_1, w_2) = 0$ if $X \le 1$, and for $X > 1$:
- **Non-confluent case ($w_1 \ne \bar w_2$):**
  $$
  B_{Y_1, Y_2}(w_1, w_2) := -\frac{Y_2^{(w_1 - \bar w_2)/2}\,\mathcal{D}_X(w_1) - Y_1^{(\bar w_2 - w_1)/2}\,\mathcal{D}_X(\bar w_2)}{(w_1 - \bar w_2)/2};
  \tag{1.7}
  $$
- **Confluent case ($w_2 = \bar w_1$, with $\nu = \frac{1 - w_1}{2}$ and $a_c^2 = c^2 Y_1 Y_2 \in (0, 1)$):**
  $$
  B_{Y_1, Y_2}(w_1, \bar w_1) := \sum_{1 \le c < X} \frac{\varphi(c)}{c^{2 - w_1}} \left[ B\!\left(\frac{1}{2},\, \nu\right)\Bigl(\psi(\nu) - \psi\!\left(\nu + \tfrac{1}{2}\right) - \log(a_c^2)\Bigr) + \frac{a_c^{2\nu}}{\nu^2}\,{}_3F_2\!\left(\begin{matrix}\tfrac{1}{2},\, \nu,\, \nu \\ \nu + 1,\, \nu + 1\end{matrix};\, a_c^2\right) \right],
  \tag{1.8}
  $$
  where $\psi(z) = \Gamma'(z)/\Gamma(z)$ is the digamma function and ${}_3F_2\bigl(\begin{smallmatrix}1/2, \nu, \nu \\ \nu+1, \nu+1\end{smallmatrix}; z\bigr) := \sum_{m=0}^{\infty} \frac{(1/2)_m}{m!}\,\frac{\nu^2}{(\nu + m)^2}\,z^m$ ($|z| < 1$).

Crucially, **$K_{Y_1, Y_2}(w_1, w_2)$ is completely elementary-hypergeometric and free of $\zeta(s)$**: for fixed $(Y_1, Y_2)$, it is a finite sum over the $\lceil (Y_1 Y_2)^{-1/2}\rceil - 1$ integers $1 \le c < (Y_1 Y_2)^{-1/2}$, holomorphic in $w_1 \in \mathcal{S}_{(0,1)}$ and anti-holomorphic in $w_2 \in \mathcal{S}_{(0,1)}$. Finally, define the **scattering remainder**
$$
R_{Y_1, Y_2}(w_1, w_2) := \begin{cases}
\dfrac{\Phi(w_1)\,Y_2^{(w_1 - \bar w_2)/2} - \overline{\Phi(w_2)}\,Y_1^{(\bar w_2 - w_1)/2}}{(w_1 - \bar w_2)/2}, & w_1 \ne \bar w_2, \\[10pt]
2\Phi'(w_1) + \Phi(w_1)\log(Y_1 Y_2), & w_2 = \bar w_1.
\end{cases}
\tag{1.9}
$$

---

### 1.3. Statements of Main Results and Scientific Scope

Recall that for each integer $m \ge 1$, the normalized Hecke operator $T_m$ acts on $\Gamma$-automorphic functions $f : \mathbb{H} \to \mathbb{C}$ by
$$
(T_m f)(z) := \frac{1}{\sqrt{m}} \sum_{ad = m} \sum_{b=0}^{d-1} f\!\left(\frac{az + b}{d}\right),
\tag{1.10}
$$
where the outer sum runs over all positive factorizations $ad = m$ ($a, d \ge 1$).

**Theorem 1 (Hecke Horocycle Closure and Closed-Form Bruhat–Hypergeometric Unfolding).** *Let $w, w_1, w_2 \in \mathcal{S}_{(0,1)}$ and $Y, Y_1, Y_2 > 0$.*
1. ***($L^2$ membership and cusp decay):** At every $z \in \mathbb{H}$, the Poincaré sum $P_w^Y(z)$ in (1.2) has only finitely many nonzero terms. On $\mathcal{F}$ for $y > \max(Y, 1/Y)$, $F_w^Y(z) = \Lambda(w)\,y^{w/2} + O_w(e^{-2\pi y})$. Hence $F_w^Y \in L^2(\Gamma\backslash\mathbb{H})$ for all $w \in \mathcal{S}_{(0,1)}$ and $Y > 0$, with rapid cusp decay $F_\rho^Y(z) = O_\rho(e^{-2\pi y})$ whenever $\Lambda(\rho) = 0$.*
2. ***(Exact Hecke horocycle closure):** For every integer $m \ge 1$ and every $z \in \mathbb{H}$,*
   $$
   (T_m P_w^Y)(z) = \sum_{ad = m} \left(\frac{a}{d}\right)^{\!\frac{1 - w}{2}} P_w^{(d/a) Y}(z), \qquad
   (T_m F_w^Y)(z) = \sum_{ad = m} \left(\frac{a}{d}\right)^{\!\frac{1 - w}{2}} F_w^{(d/a) Y}(z).
   \tag{1.11}
   $$
   *In particular, the linear span $\mathcal{V}_w := \operatorname{span}\{F_w^Y : Y > 0\} \subset L^2(\Gamma\backslash\mathbb{H})$ is an exact module over the full Hecke algebra $\mathbb{T} = \mathbb{C}[T_1, T_2, \dots]$.*
3. ***(Exact finite-sum inner product formula):** Define the normalized inner product*
   $$
   G_{Y_1, Y_2}(w_1, w_2) := \frac{\bigl\langle F_{w_1}^{Y_1},\, F_{w_2}^{Y_2}\bigr\rangle_{L^2(\Gamma\backslash\mathbb{H})}}{\Lambda(2 - w_1)\,\overline{\Lambda(2 - w_2)}}.
   \tag{1.12}
   $$
   *Then for all $w_1, w_2 \in \mathcal{S}_{(0,1)}$ and all $Y_1, Y_2 > 0$,*
   $$
   G_{Y_1, Y_2}(w_1, w_2) = K_{Y_1, Y_2}(w_1, w_2) + R_{Y_1, Y_2}(w_1, w_2),
   \tag{1.13}
   $$
   *where $K_{Y_1, Y_2}$ and $R_{Y_1, Y_2}$ are given in closed form by (1.6)–(1.9).*
4. ***(Specialization to zeros and conjugate zeros):** If $\rho_1, \rho_2 \in \mathcal{S}_{(0,1)}$ satisfy $\Lambda(\rho_1) = \Lambda(\rho_2) = 0$ and $\rho_1 \ne \bar\rho_2$ (in particular, when $\rho_1 = \rho_2 = \rho$, since $\Lambda$ has no real zeros on $(0, 1)$), then $R_{Y_1, Y_2}(\rho_1, \rho_2) = 0$ and $G_{Y_1, Y_2}(\rho_1, \rho_2) = K_{Y_1, Y_2}(\rho_1, \rho_2)$. At the conjugate pair $(\rho, \bar\rho)$ of any zero $\Lambda(\rho) = 0$,*
   $$
   G_{Y_1, Y_2}(\rho, \bar\rho) = K_{Y_1, Y_2}(\rho, \bar\rho) + Z(\rho), \qquad
   Z(\rho) := \frac{2\Lambda'(\rho)}{\Lambda(2 - \rho)}.
   \tag{1.14}
   $$

Our second theorem establishes the spectral representation of $G_{Y_1, Y_2}$ and shows how a two-height Perron combination eliminates the dominant $Y^{-\sigma}$ residual-spectrum pole to achieve $O(Y^{1-\sigma})$ norm decay with an explicit, error-term-free global bound.

**Theorem 2 (Roelcke–Selberg Spectral Identity, Perron Pole Cancellation, and Error-Term-Free Norm Bound).** *Let $w, w_1, w_2 \in \mathcal{S}_{(0,1)}$ with $\sigma := \operatorname{Re} w \in (0, 1)$, and let $Y, Y_1, Y_2 > 0$.*
1. ***(Orthogonality to Maass cusp forms and spectral Parseval identity):** Every Maass cusp form $u_j$ on $\Gamma\backslash\mathbb{H}$ satisfies $\langle F_w^Y, u_j\rangle_{L^2(\Gamma\backslash\mathbb{H})} = 0$. Setting $S(t) := \frac{\Lambda(1 + 2it)}{\Lambda(1 - 2it)}$ ($|S(t)| = 1$ for $t \in \mathbb{R}$) and*
   $$
   f_{w, Y}(t) := \frac{Y^{\frac{1 - w}{2} - it}}{\frac{1 - w}{2} - it} + S(t)\,\frac{Y^{\frac{1 - w}{2} + it}}{\frac{1 - w}{2} + it} \qquad (t \in \mathbb{R}),
   \tag{1.15}
   $$
   *we have the exact spectral decomposition*
   $$
   G_{Y_1, Y_2}(w_1, w_2) = \frac{12}{\pi w_1 \bar w_2}\,Y_1^{-w_1/2} Y_2^{-\bar w_2/2} + \frac{1}{2\pi}\int_0^{\infty} f_{w_1, Y_1}(t)\,\overline{f_{w_2, Y_2}(t)}\,dt.
   \tag{1.16}
   $$
   *In particular, $G_{Y, Y}(w, w) \ge \frac{12}{\pi |w|^2}\,Y^{-\sigma}$ for every $Y > 0$, and $G_{Y, Y}(w, w) = \frac{12}{\pi |w|^2}\,Y^{-\sigma} + O_w(Y^{1-\sigma})$ as $Y \to 0^+$.*
2. ***(Two-height Perron pole cancellation and global Plancherel bound):** Fix any dilation ratio $\lambda > 1$. Since $|\lambda^{-w/2}| = \lambda^{-\sigma/2} < 1$, there exists a unique affine-normalized vector $\mathbf{c} = (c_1, c_2) \in \mathbb{C}^2$ satisfying $c_1 + c_2 = 1$ and $c_1 + c_2 \lambda^{-w/2} = 0$, namely*
   $$
   c_1 = \frac{\lambda^{-w/2}}{\lambda^{-w/2} - 1}, \qquad c_2 = -\frac{1}{\lambda^{-w/2} - 1}.
   \tag{1.17}
   $$
   *Define the constant-mode-annihilated packet $\widetilde{D}_w^{Y, \lambda} := \frac{c_1 F_w^Y + c_2 F_w^{\lambda Y}}{\Lambda(2 - w)}$ and the constant*
   $$
   C_{\mathrm{RL}}(w, \lambda) := \frac{1 + |c_2|^2\bigl(\lambda^{1 - \sigma} - 1\bigr)}{1 - \sigma} > 0.
   \tag{1.18}
   $$
   *Then $\langle \widetilde{D}_w^{Y, \lambda}, 1\rangle_{L^2(\Gamma\backslash\mathbb{H})} = 0$, and **for every $Y > 0$ unconditionally***,
   $$
   \left\|\widetilde{D}_w^{Y, \lambda}\right\|_{L^2(\Gamma\backslash\mathbb{H})}^2 = \mathbf{c}\,\mathbf{G}_2(w; Y, \lambda Y)\,\mathbf{c}^* \le 2 C_{\mathrm{RL}}(w, \lambda)\,Y^{1 - \sigma},
   \tag{1.19}
   $$
   *where $\mathbf{G}_2(w; Y, \lambda Y) := [G_{Y_i, Y_j}(w, w)]_{i,j=1}^2$ at $(Y_1, Y_2) = (Y, \lambda Y)$. Moreover, as $Y \to 0^+$,*
   $$
   \lim_{Y \to 0^+} Y^{-(1 - \sigma)}\left\|\widetilde{D}_w^{Y, \lambda}\right\|_{L^2(\Gamma\backslash\mathbb{H})}^2 = C_{\mathrm{RL}}(w, \lambda).
   \tag{1.20}
   $$

Combining Theorem 1(3) with Theorem 2 yields an elementary two-height Ford-circle zero criterion together with explicit finite-$Y$ refutation thresholds. For $(Y_1, Y_2) = (Y, \lambda Y)$, let $\mathbf{K}_2(w; Y, \lambda Y) := [K_{Y_i, Y_j}(w, w)]_{i,j=1}^2$ be the $2\times 2$ Hermitian Ford-circle matrix.

**Theorem 3 (Elementary Two-Height Ford-Circle Zero Criterion, Quantitative Refutation, and Scope Boundary).** *Fix any $\lambda > 1$ and let $w = \sigma + i\gamma \in \mathcal{S}_{(0,1)}$.*
1. ***(Two-height zero equivalence):** For any distinct heights $0 < Y_1 < \dots < Y_L$, the functions $F_w^{Y_1}, \dots, F_w^{Y_L}$ are linearly independent in $L^2(\Gamma\backslash\mathbb{H})$. Consequently, the following three statements are equivalent:*
   - *(i) $\Lambda(w) = 0$ (equivalently, $\zeta(w) = 0$);*
   - *(ii) $\mathbf{K}_2(w; Y, \lambda Y)$ is positive semidefinite (in fact strictly positive definite) for all $Y \in (0, 1)$;*
   - *(iii) $\det \mathbf{K}_2(w; Y, \lambda Y) > 0$ for all $Y \in (0, 1)$.*
2. ***(Unit-modulus phase identity and explicit finite-$Y$ refutation threshold):** Suppose $\Lambda(w) \ne 0$, so $\Phi(w) \ne 0$.*
   - *If $\gamma \ne 0$, put $z := \lambda^{-w/2}$; then $\bar c_1 + \bar c_2 \lambda^{i\gamma} = \frac{\bar z(z - 1)}{z(\bar z - 1)} =: e^{i\theta(w, \lambda)}$ has **exact unit modulus $|e^{i\theta(w, \lambda)}| = 1$**, and*
     $$
     \mathbf{c}\,\mathbf{K}_2(w; Y, \lambda Y)\,\mathbf{c}^* = \left\|\widetilde{D}_w^{Y, \lambda}\right\|_{L^2(\Gamma\backslash\mathbb{H})}^2 - \frac{2}{\gamma}\,\operatorname{Im}\!\Bigl(\Phi(w)\,e^{i\theta(w, \lambda)}\,Y^{i\gamma}\Bigr).
     \tag{1.21}
     $$
     *Along the geometric progression of heights $Y_m \in (0, 1)$ ($m \in \mathbb{Z}$ sufficiently large) where $\operatorname{sgn}(\gamma)\operatorname{Im}(\Phi(w) e^{i\theta(w, \lambda)} Y_m^{i\gamma}) = |\Phi(w)|$, we have $\mathbf{c}\,\mathbf{K}_2(w; Y_m, \lambda Y_m)\,\mathbf{c}^* < 0$ (hence $\lambda_{\min}(\mathbf{K}_2) < 0$) whenever*
     $$
     Y_m < Y_{\mathrm{ref}}(w, \lambda) := \left(\frac{|\Phi(w)|}{|\gamma|\,C_{\mathrm{RL}}(w, \lambda)}\right)^{\!\frac{1}{1 - \sigma}},
     \tag{1.22}
     $$
     *and simultaneously $K_{Y_m, Y_m}(w, w) > 0$, forcing **$\det \mathbf{K}_2(w; Y_m, \lambda Y_m) < 0$** by Sylvester's law of inertia, whenever $Y_m < \min\!\bigl(Y_{\mathrm{ref}}(w, \lambda),\, (\frac{6|\gamma|}{\pi |w|^2 |\Phi(w)|})^{1/\sigma}\bigr)$.*
   - *If $\gamma = 0$ ($w = \sigma \in (0, 1)$), then $\Phi(\sigma) < 0$, $K_{Y, Y}(\sigma, \sigma) \sim \frac{12}{\pi\sigma^2} Y^{-\sigma} \to +\infty$, and $\mathbf{c}\,\mathbf{K}_2(\sigma; Y, \lambda Y)\,\mathbf{c}^* = O_{\sigma, \lambda}(Y^{1-\sigma}) - 2|\Phi(\sigma)|\,|\log Y| + O_{\sigma, \lambda}(1) \to -\infty$ as $Y \to 0^+$, so $\det \mathbf{K}_2(\sigma; Y, \lambda Y) < 0$ for all sufficiently small $Y > 0$.*
3. ***(Scope boundary of linear $L^2(\Gamma\backslash\mathbb{H})$ positivity vs. non-Euler-product $L$-functions):** Because $\mathbf{R}_2(w; Y, \lambda Y)$ depends on $w$ solely through $\Phi(w) = \Lambda(w)/\Lambda(2 - w)$, $\mathbf{K}_2(w; Y, \lambda Y) = \mathbf{G}_2(w; Y, \lambda Y) \succ 0$ holds at **every** zero of $\zeta(s)$ in $\mathcal{S}_{(0,1)}$ regardless of $\operatorname{Re} w$; thus linear $L^2(\Gamma\backslash\mathbb{H})$ inner-product positivity characterizes $\Lambda(w) = 0$ rather than $\operatorname{Re} w = \frac{1}{2}$ directly. Conversely, if $L(s)$ is any Dirichlet series satisfying a functional equation but lacking an Euler product whose critical-strip off-line zero $w_\star \in \mathcal{S}_{(0,1)}$ satisfies $\zeta(w_\star) \ne 0$, then finitely many modular Ford circles $1 \le c < \lambda^{-1/2} Y^{-1}$ certify $\det \mathbf{K}_2(w_\star; Y, \lambda Y) < 0$.*

Our fourth theorem exploits the **bilinear** pairing $\langle H, \overline{H}\rangle_{L^2(\Gamma\backslash\mathbb{H})} = \int_{\mathcal{F}} H(z)^2\,d\mu(z)$ against the Hermitian norm $\|H\|_{L^2(\Gamma\backslash\mathbb{H})}^2$ to certify zero simplicity $\Lambda'(\rho) \ne 0$ and enclose $|Z(\rho)| = |2\Lambda'(\rho)/\Lambda(2 - \rho)|$ using finitely many rational Ford circles.

**Theorem 4 (Finite Ford-Circle Multiplicity-One Disks and Completeness).** *Let $\rho = \sigma + i\gamma \in \mathcal{S}_{(0,1)}$ satisfy $\Lambda(\rho) = 0$. Fix any heights $0 < Y_1 < \dots < Y_L$ and weights $\mathbf{c} = (c_1, \dots, c_L) \in \mathbb{C}^L$ with $\sum_{j=1}^L c_j = 1$, and define the Hermitian diagonal quadratic form and complex-symmetric conjugate bilinear form*
$$
K_{\mathbf{c}}^{\mathrm{diag}} := \sum_{j=1}^L \sum_{k=1}^L c_j \bar c_k\,K_{Y_j, Y_k}(\rho, \rho) > 0, \qquad
K_{\mathbf{c}}^{\mathrm{conj}} := \sum_{j=1}^L \sum_{k=1}^L c_j c_k\,K_{Y_j, Y_k}(\rho, \bar\rho).
\tag{1.23}
$$
1. ***(Closed Cauchy–Schwarz disk enclosure):** The derivative invariant $Z(\rho) = \frac{2\Lambda'(\rho)}{\Lambda(2 - \rho)}$ lies in the closed disk $\overline{D}\bigl(-K_{\mathbf{c}}^{\mathrm{conj}},\, K_{\mathbf{c}}^{\mathrm{diag}}\bigr)$:*
   $$
   \bigl|K_{\mathbf{c}}^{\mathrm{conj}} + Z(\rho)\bigr| \le K_{\mathbf{c}}^{\mathrm{diag}}.
   \tag{1.24}
   $$
   *In particular, whenever the finite Ford-circle inequality $|K_{\mathbf{c}}^{\mathrm{conj}}| > K_{\mathbf{c}}^{\mathrm{diag}}$ holds, $\rho$ is certified to be a **simple zero** ($\Lambda'(\rho) \ne 0$, hence $\zeta'(\rho) \ne 0$) with explicit two-sided bounds*
   $$
   0 < \bigl|K_{\mathbf{c}}^{\mathrm{conj}}\bigr| - K_{\mathbf{c}}^{\mathrm{diag}} \le \left|\frac{2\Lambda'(\rho)}{\Lambda(2 - \rho)}\right| \le \bigl|K_{\mathbf{c}}^{\mathrm{conj}}\bigr| + K_{\mathbf{c}}^{\mathrm{diag}}.
   \tag{1.25}
   $$
2. ***(Completeness via Perron pole cancellation):** Choosing $L = 2$, $(Y_1, Y_2) = (Y, \lambda Y)$ ($\lambda > 1$), and the Perron vector $\mathbf{c} = (c_1, c_2)$ of (1.17), the disk radius satisfies $K_{\mathbf{c}}^{\mathrm{diag}} = \|\widetilde{D}_\rho^{Y, \lambda}\|_{L^2}^2 \le 2 C_{\mathrm{RL}}(\rho, \lambda)\,Y^{1-\sigma} \to 0$ as $Y \to 0^+$. Consequently, $\rho$ is a simple zero of $\zeta(s)$ **if and only if** there exists a rational height $Y = 1/q$ ($q \in \mathbb{N}_{\ge 2}$) at which $|K_{\mathbf{c}}^{\mathrm{conj}}| > K_{\mathbf{c}}^{\mathrm{diag}}$.*

Our fifth theorem explains where the critical-line condition $\operatorname{Re}\rho_* = \frac{1}{2}$ enters the Ford-circle formalism: not in the positivity of a single $w$-packet (which characterizes $\Lambda(w) = 0$), but in the **sub-threshold $X \to \infty$ decay** of the Incomplete-Beta totient sum $\mathcal{D}_X(w)$ at *any* fixed probe point $w \in \mathcal{S}_{(0,1)}$.

**Theorem 5 (Completed Mellin Scattering Identity and Sub-Threshold Totient RH Equivalence).** *Fix any $w = \sigma + i\gamma \in \mathcal{S}_{(0,1)}$, and put $\nu := \frac{1 - w}{2}$.*
1. ***(Completed Mellin scattering identity and unconditional asymptotic):** For $\operatorname{Re} s > \sigma$, the Mellin transform of $\mathcal{D}_X(w)$ converges absolutely and equals*
   $$
   \mathcal{M}_w(s) := \int_0^{\infty} \mathcal{D}_X(w)\,X^{-s - 1}\,dX = \frac{1}{s}\,\frac{\zeta(1 - w + s)}{\zeta(2 - w + s)}\,B\!\left(\frac{1}{2},\, \frac{1 - w + s}{2}\right) \equiv \frac{1}{s}\,\frac{\Lambda(1 - w + s)}{\Lambda(2 - w + s)}.
   \tag{1.26}
   $$
   *On $\mathbb{C}$, $\mathcal{M}_w(s)$ has a removable singularity at $s = w - 1$ (with value $\frac{1}{1 - w}$), a simple zero at $s = w - 2$, simple poles at $s = w$ (residue $\frac{6}{\pi w}$) and at $s = 0$ when $\Lambda(w) \ne 0$ (residue $\Phi(w)$), and poles at $s = \rho_* + w - 2$ as $\rho_*$ ranges over all nontrivial zeros of $\zeta(s)$—none of which is ever canceled by $\Lambda(1 - w + s)$. Unconditionally, for every $\varepsilon > 0$ and $X \ge 1$,*
   $$
   \mathcal{D}_X(w) = \Phi(w) + \frac{6}{\pi w}\,X^w + O_{w, \varepsilon}\!\left(X^{\sigma - 1 + \varepsilon}\right).
   \tag{1.27}
   $$
2. ***($C^2$-smoothed totient equivalence with zero-free half-planes and RH):** Define the $C^2$-smoothed Incomplete-Beta totient sum*
   $$
   \mathcal{D}_X^{\mathrm{sm}}(w) := \int_0^1 12 v^2(1 - v)\,\mathcal{D}_{v X}(w)\,dv = \sum_{1 \le c < X} \frac{\varphi(c)}{c^{2 - w}}\,W_{\frac{1 - w}{2}}\!\left(\frac{c}{X}\right),
   \tag{1.28}
   $$
   *where for $a \in (0, 1)$ and $\nu \in \mathbb{C}$,*
   $$
   W_\nu(a) := B_{1 - a^2}\!\left(\frac{1}{2},\, \nu\right) - 4 a^3\,B_{1 - a^2}\!\left(\frac{1}{2},\, \nu - \frac{3}{2}\right) + 3 a^4\,B_{1 - a^2}\!\left(\frac{1}{2},\, \nu - 2\right),
   \tag{1.29}
   $$
   *and set $r_w(X) := \mathcal{D}_X^{\mathrm{sm}}(w) - \Phi(w) - \frac{72}{\pi w(w + 3)(w + 4)}\,X^w$. Then for **any single fixed $w = \sigma + i\gamma \in \mathcal{S}_{(0,1)}$** and any $\Theta \in [\frac{1}{2}, 1)$,*
   $$
   \sup_{\Lambda(\rho_*) = 0} \operatorname{Re}(\rho_*) \le \Theta
   \quad\Longleftrightarrow\quad
   r_w(X) = O_{w, \varepsilon}\!\left(X^{\sigma + \Theta - 2 + \varepsilon}\right) \;\;\forall \varepsilon > 0 \;\;(X \to \infty).
   \tag{1.30}
   $$
   *In particular ($\Theta = \frac{1}{2}$), **the Riemann Hypothesis holds if and only if $r_w(X) = O_{w, \varepsilon}(X^{\sigma - 3/2 + \varepsilon})$ for every $\varepsilon > 0$**.*
3. ***(Non-oscillatory conjugate-zero pole when $w = \rho_k$):** If $w = \rho_k = \frac{1}{2} + i\gamma_k$ is a simple critical-line zero of $\zeta(s)$, the conjugate zero $\rho_* = \overline{\rho_k} = 1 - \rho_k$ produces a **real, non-oscillatory simple pole** of the smoothed Mellin transform $\frac{12}{s(s+3)(s+4)}\mathcal{M}_{\rho_k}(s)$ at $s = -1$ with exact residue*
   $$
   \operatorname{Res}_{s = -1}\!\left[\frac{12}{s(s + 3)(s + 4)}\,\mathcal{M}_{\rho_k}(s)\,X^s\right] = -\frac{2\Lambda(1 + \rho_k)}{\Lambda'(\overline{\rho_k})}\,X^{-1} = -\frac{4}{\overline{Z(\rho_k)}}\,X^{-1}.
   \tag{1.31}
   $$

**Summary of novelty and partial-result scope.** Classical ingredients used below include the Fourier and Bruhat double-coset expansions on $\mathrm{SL}_2(\mathbb{Z})\backslash\mathbb{H}$, the Maass–Selberg relation, and the Roelcke–Selberg spectral theorem [1, 7, 8], Dirichlet's totient identity $\sum_{c \ge 1} \varphi(c)c^{-z} = \zeta(z-1)/\zeta(z)$, Borel–Carathéodory bounds in zero-free regions [14], and the existence of critical-strip off-line zeros for class-number-$2$ Epstein zeta functions and Davenport–Heilbronn's $L$-function [11, 12, 13]. What is new here is: (i) the exact Hecke dilation closure (1.11) and closed-form Incomplete-Beta / ${}_3F_2$ unfolding (1.13)–(1.14) of the indicator-subtracted packets $F_w^Y$; (ii) the two-height Perron annihilation of the residual-spectrum pole and the unconditional error-term-free global bound (1.19); (iii) the resulting elementary $2\times 2$ Ford-circle zero criterion, explicit refutation threshold (1.22), and dual-backend interval refutations of genuine off-line zeros of Epstein and Davenport–Heilbronn $L$-functions; (iv) the finite-Ford-circle Cauchy–Schwarz multiplicity-one disk test (1.24)–(1.25) and its completeness; and (v) the completed Mellin ratio (1.26) and single-point smoothed totient equivalence (1.30)–(1.31). These theorems reformulate zero detection, simplicity certification, and RH on $\Gamma\backslash\mathbb{H}$, and do **not** unconditionally constrain the zero-free region of $\zeta(s)$.

---

## 2. Proof of Theorem 1: Hecke Horocycle Closure and Closed-Form Unfolding

### 2.1. $L^2(\Gamma\backslash\mathbb{H})$ Membership and Exact Hecke Coset Bijection

*Proof of Theorem 1(1).* Fix $w = \sigma + i\gamma \in \mathcal{S}_{(0,1)}$ and $Y > 0$. A complete set of representatives for $\Gamma_\infty \backslash \Gamma$ consists of the identity $I$ ($c = 0, d = 1$) together with one matrix $\gamma_{c,d} = \bigl(\begin{smallmatrix}* & * \\ c & d\end{smallmatrix}\bigr) \in \Gamma$ for each coprime pair $(c, d) \in \mathbb{Z}^2$ with $c \ge 1$ and $\gcd(c, d) = 1$ [8, §2.4]. At $z = x + iy \in \mathbb{H}$, $\operatorname{Im}(\gamma_{c,d} z) = \frac{y}{(cx + d)^2 + c^2 y^2}$. If $\operatorname{Im}(\gamma_{c,d} z) > Y$, then $c^2 y^2 < \frac{y}{Y}$, i.e., $1 \le c < (y Y)^{-1/2}$, and $|cx + d| < \sqrt{y/Y - c^2 y^2}$. Hence only finitely many cosets satisfy $\operatorname{Im}(\gamma z) > Y$ on any compact subset of $\mathbb{H}$, so $P_w^Y$ is well-defined and locally bounded on $\mathbb{H}$.

On the fundamental domain $\mathcal{F}$, recall the classical height inequality (Iwaniec [8, Lemma 2.10]): for every $z \in \mathcal{F}$ and every $\gamma \in \Gamma \setminus \Gamma_\infty$ ($c \ge 1$), $|cz + d|^2 \ge 1$ and $|cz + d|^2 \ge c^2 y^2 \ge y^2$, so
$$
\operatorname{Im}(\gamma z) \le \min\!\left(1,\, \frac{1}{y}\right) \qquad \forall z = x + iy \in \mathcal{F},\;\; \forall \gamma \in \Gamma \setminus \Gamma_\infty.
\tag{2.1}
$$
In particular, for $z \in \mathcal{F}$ with $y > \max(Y, 1/Y)$, every $\gamma \notin \Gamma_\infty$ has $\operatorname{Im}(\gamma z) \le \frac{1}{y} < Y$, whereas $\gamma = I$ has $\operatorname{Im} z = y > Y$; thus $P_w^Y(z) = \Lambda(2 - w)\,y^{1 - w/2}$ identically on $\{z \in \mathcal{F} : y > \max(Y, 1/Y)\}$. Meanwhile, $E^*(z, w/2)$ is holomorphic in $w \in \mathcal{S}_{(0,1)}$ (its only poles in $w$ lie at $w = 0, 2 \notin \mathcal{S}_{(0,1)}$) with Fourier-Bessel expansion [8, (3.26), (6.15)]
$$
E^*\!\left(z, \frac{w}{2}\right) = \Lambda(w)\,y^{w/2} + \Lambda(2 - w)\,y^{1 - w/2} + 4 y^{1/2}\sum_{n=1}^{\infty} \tau_{\frac{w-1}{2}}(n)\,K_{\frac{w-1}{2}}(2\pi n y)\cos(2\pi n x),
\tag{2.2}
$$
where $\tau_\nu(n) := \sum_{ab=n}(a/b)^\nu$ and $K_\nu(u) \ll_\nu u^{-1/2} e^{-u}$ as $u \to +\infty$. Subtracting $P_w^Y(z)$ cancels $\Lambda(2 - w)\,y^{1 - w/2}$ for $y > \max(Y, 1/Y)$, leaving $F_w^Y(z) = \Lambda(w)\,y^{w/2} + O_w(e^{-2\pi y})$. Since $\int_{y_0}^{\infty} y^{\sigma - 2}\,dy < \infty$ for $\sigma < 1$ and $F_w^Y$ is bounded on $\{z \in \mathcal{F} : y \le \max(1, Y, 1/Y)\}$, we conclude $F_w^Y \in L^2(\Gamma\backslash\mathbb{H})$, with $F_\rho^Y(z) = O_\rho(e^{-2\pi y})$ when $\Lambda(\rho) = 0$. $\square$

*Proof of Theorem 1(2).* Fix $m \ge 1$ and let $M_m := \{M \in M_2(\mathbb{Z}) : \det M = m\}$, with projective quotients modulo $\{\pm I\}$ understood so that $\pm I$ acts trivially on $\mathbb{H}$. Let $\mathcal{R}_m := \bigl\{\bigl(\begin{smallmatrix}a & b \\ 0 & d\end{smallmatrix}\bigr) : ad = m,\; a, d \ge 1,\; 0 \le b < d\bigr\}$, which is a complete set of right-coset representatives for $\Gamma \backslash M_m$ [8, §6.2]. We claim first that matrix multiplication $(\gamma, \sigma) \mapsto \gamma\sigma$ induces a **bijection**
$$
(\Gamma_\infty \backslash \Gamma) \times (\Gamma \backslash M_m) \xrightarrow{\;\sim\;} \Gamma_\infty \backslash M_m.
\tag{2.3}
$$
Indeed, every $M \in M_m$ factors as $M = g \sigma$ for some $g \in \Gamma$ and $\sigma \in \mathcal{R}_m$, giving surjectivity onto $\Gamma_\infty \backslash M_m$. For injectivity, if $\gamma_1 \sigma_1 = \pm u \gamma_2 \sigma_2$ with $u \in \Gamma_\infty \subset \Gamma$ and $\sigma_1, \sigma_2 \in \mathcal{R}_m$, then $(\gamma_1^{-1} u \gamma_2)\sigma_2 = \pm\sigma_1$ lies in $\Gamma \sigma_2 \cap \Gamma \sigma_1$, forcing $\sigma_1 = \sigma_2$; canceling $\sigma_1$ ($\det\sigma_1 = m \ne 0$) yields $\gamma_1^{-1} u \gamma_2 = \pm I$, i.e., $\Gamma_\infty \gamma_1 = \Gamma_\infty \gamma_2$.

Next, we construct a second explicit set of representatives for $\Gamma_\infty \backslash M_m$ adapted to $\operatorname{Im}(M z)$. Given any $M = \bigl(\begin{smallmatrix}\alpha & \beta \\ C & D\end{smallmatrix}\bigr) \in M_m$, left multiplication by $\pm\bigl(\begin{smallmatrix}1 & n \\ 0 & 1\end{smallmatrix}\bigr) \in \Gamma_\infty$ preserves the bottom row $(C, D)$ up to $\pm 1$. Let $r := \gcd(C, D) \ge 1$; since $\alpha D - \beta C = m$, we have $r \mid m$. Put $a' := m/r$ and $(C, D) = r(c, d)$ with $\gcd(c, d) = 1$, corresponding to a unique coset $\gamma = \bigl(\begin{smallmatrix}\alpha_0 & \beta_0 \\ c & d\end{smallmatrix}\bigr) \in \Gamma_\infty \backslash \Gamma$. Because $\alpha d - \beta c = a'$ and $\alpha_0 d - \beta_0 c = 1$, every integer solution $(\alpha, \beta)$ has the form $(\alpha, \beta) = (a'\alpha_0 + k c,\, a'\beta_0 + k d)$ ($k \in \mathbb{Z}$), i.e., $M = \bigl(\begin{smallmatrix}a' & k \\ 0 & r\end{smallmatrix}\bigr)\gamma$. Since $\bigl(\begin{smallmatrix}1 & n \\ 0 & 1\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}a' & k \\ 0 & r\end{smallmatrix}\bigr) = \bigl(\begin{smallmatrix}a' & k + nr \\ 0 & r\end{smallmatrix}\bigr)$, a complete, irredundant set of representatives for $\Gamma_\infty \backslash M_m$ is
$$
\left\{ \begin{pmatrix} a & k \\ 0 & d \end{pmatrix} \gamma \;:\; ad = m,\;\; 0 \le k < d,\;\; \gamma \in \Gamma_\infty \backslash \Gamma \right\}.
\tag{2.4}
$$
Now let $\psi : (0, \infty) \to \mathbb{C}$ be any function for which $P_\psi(z) := \sum_{\gamma \in \Gamma_\infty \backslash \Gamma} \psi(\operatorname{Im}\gamma z)$ converges absolutely at every $z \in \mathbb{H}$. Combining (2.3) and (2.4) and noting that $\operatorname{Im}\!\bigl(\frac{a(\gamma z) + k}{d}\bigr) = \frac{a}{d}\operatorname{Im}(\gamma z)$ is **independent of $k \in \{0, \dots, d-1\}$**, we obtain
$$
(T_m P_\psi)(z) = \frac{1}{\sqrt{m}} \sum_{\mu \in \Gamma_\infty \backslash M_m} \psi(\operatorname{Im}\mu z)
= \frac{1}{\sqrt{m}} \sum_{ad = m} d \sum_{\gamma \in \Gamma_\infty \backslash \Gamma} \psi\!\left(\frac{a}{d}\operatorname{Im}\gamma z\right).
\tag{2.5}
$$
Applying (2.5) to the finite sum $\psi(y) = \Lambda(2 - w)\,y^{1 - w/2}\,\mathbf{1}_{\{y > Y\}}$, where $\psi(\frac{a}{d} y) = (\frac{a}{d})^{1 - w/2}\,\Lambda(2 - w)\,y^{1 - w/2}\,\mathbf{1}_{\{y > (d/a)Y\}}$ and $\frac{d}{\sqrt{m}}(\frac{a}{d})^{1 - w/2} = (\frac{a}{d})^{-1/2}(\frac{a}{d})^{1 - w/2} = (\frac{a}{d})^{(1 - w)/2}$, gives $(T_m P_w^Y)(z) = \sum_{ad = m} (a/d)^{(1 - w)/2} P_w^{(d/a)Y}(z)$ for all $w \in \mathbb{C}$ and $Y > 0$. Likewise, applying (2.5) to $\psi(y) = \Lambda(2 - w)\,y^{1 - w/2}$ for $\operatorname{Re} w < 0$ (where $E(z, 1 - w/2)$ converges absolutely) gives $\bigl(T_m E^*(\cdot, 1 - w/2)\bigr)(z) = \sum_{ad = m} (a/d)^{(1 - w)/2} E^*(z, 1 - w/2)$, which extends to all $w \in \mathbb{C} \setminus \{0, 2\}$ by analytic continuation and $E^*(z, 1 - w/2) = E^*(z, w/2)$. Subtracting the two identities yields (1.11). $\square$

---

### 2.2. Truncated Maass–Selberg Unfolding and Cancellation of Cutoff $T$

*Proof of Theorem 1(3)–(4).* Fix $Y_1, Y_2 > 0$. Both sides of (1.13) are holomorphic in $w_1 \in \mathcal{S}_{(0,1)}$ and anti-holomorphic in $w_2 \in \mathcal{S}_{(0,1)}$ (for the left-hand side, differentiation under $\int_{\mathcal{F}}$ is justified by the locally uniform bound $|F_w^Y(z)| \ll_{K,Y} y^{\sigma_{\max}/2}$ on compact subsets $K \subset \mathcal{S}_{(0,1)}$ with $\sigma_{\max} < 1$; for the right-hand side, the confluent formulas (1.8)–(1.9) are the analytic limits as $w_2 \to \bar w_1$, proved below). By uniqueness of analytic continuation, it suffices first to establish (1.13) on the dense open set where $s_1 := w_1/2$ and $s_2 := \bar w_2/2$ satisfy $s_1 \ne s_2$ (Note that $s_1 + s_2 = \frac{w_1 + \bar w_2}{2}$ automatically satisfies $\operatorname{Re}(s_1 + s_2) \in (0, 1)$, so $1 - s_1 - s_2 \ne 0$ everywhere on $\mathcal{S}_{(0,1)} \times \mathcal{S}_{(0,1)}$).

Choose a truncation height $T > \max(1, Y_1, Y_2, 1/Y_1, 1/Y_2)$ and set $\mathcal{F}_T := \{z \in \mathcal{F} : \operatorname{Im} z \le T\}$. By (2.1), for every $z \in \mathcal{F}$, any non-identity coset $\gamma \notin \Gamma_\infty$ satisfies $\operatorname{Im}(\gamma z) \le 1 < T$ when $z \in \mathcal{F}_T$, and $\operatorname{Im}(\gamma z) \le \frac{1}{y} < \frac{1}{T} < Y_j$ when $z \in \mathcal{F} \setminus \mathcal{F}_T$ ($y > T$). Meanwhile, the identity coset $\gamma = I$ has $\operatorname{Im} z = y \le T$ iff $z \in \mathcal{F}_T$. Hence we have the **exact pointwise identity on all of $\mathcal{F}$**:
$$
P_{w_j}^{Y_j}(z)\,\mathbf{1}_{\mathcal{F}_T}(z) = \Lambda(2 - 2s_j) \sum_{\gamma \in \Gamma_\infty \backslash \Gamma} (\operatorname{Im}\gamma z)^{1 - s_j}\,\mathbf{1}_{\{Y_j < \operatorname{Im}\gamma z \le T\}} \qquad (z \in \mathcal{F},\; j = 1, 2; \text{ with } P_{w_2}^{Y_2} \text{ conjugated at } j = 2).
\tag{2.6}
$$
Since $\overline{E^*(z, w_2/2)} = E^*(z, s_2)$ and $\overline{P_{w_2}^{Y_2}(z)} = \Lambda(2 - 2s_2)\sum_{\gamma} (\operatorname{Im}\gamma z)^{1 - s_2}\mathbf{1}_{\{\operatorname{Im}\gamma z > Y_2\}}$, we expand $\int_{\mathcal{F}_T} F_{w_1}^{Y_1}(z)\overline{F_{w_2}^{Y_2}(z)}\,d\mu(z) = I_{EE}(T) - I_{PE}(T) - I_{EP}(T) + I_{PP}(T)$ and evaluate each piece:

1. **Maass–Selberg integral $I_{EE}(T)$:** Since $\Delta E^*(z, s) = s(s - 1)E^*(z, s)$, Green's theorem on $\mathcal{F}_T$ cancels on the $\Gamma$-paired vertical and circular boundary arcs, leaving only the horizontal line $y = T$, $-\frac{1}{2} \le x \le \frac{1}{2}$:
   $$
   \bigl(s_1(s_1 - 1) - s_2(s_2 - 1)\bigr)\int_{\mathcal{F}_T} E^*(z, s_1)E^*(z, s_2)\,d\mu(z)
   = \int_{-1/2}^{1/2} \Bigl(E^*(x+iT, s_2)\,\partial_y E^*(x+iT, s_1) - E^*(x+iT, s_1)\,\partial_y E^*(x+iT, s_2)\Bigr) dx.
   $$
   By $x$-orthogonality of $\cos(2\pi n x)$ in (2.2), the $n \ge 1$ Bessel modes contribute $O_{w_1, w_2}(e^{-4\pi T})$ at $y = T$, while the zero modes $E_0^*(T, s_j) = \Lambda(2s_j) T^{s_j} + \Lambda(2 - 2s_j) T^{1 - s_j}$ divide cleanly by $(s_1 - s_2)(s_1 + s_2 - 1)$. Since $\operatorname{Re}(s_1 + s_2 - 1) = \frac{\sigma_1 + \sigma_2}{2} - 1 < 0$, the term $\Lambda(2s_1)\Lambda(2s_2)\frac{T^{s_1 + s_2 - 1}}{s_1 + s_2 - 1}$ is $o(1)$ as $T \to \infty$, giving
   $$
   \frac{I_{EE}(T)}{\Lambda(2 - 2s_1)\Lambda(2 - 2s_2)} = \frac{T^{1 - s_1 - s_2}}{1 - s_1 - s_2} + \Phi(w_1)\frac{T^{s_1 - s_2}}{s_1 - s_2} + \overline{\Phi(w_2)}\frac{T^{s_2 - s_1}}{s_2 - s_1} + o(1) \qquad (T \to \infty).
   \tag{2.7}
   $$
2. **Cross integrals $I_{PE}(T)$ and $I_{EP}(T)$:** Inserting (2.6) for $P_{w_1}^{Y_1}\mathbf{1}_{\mathcal{F}_T}$ and unfolding the compactly supported sum over $\Gamma_\infty \backslash \mathbb{H} \simeq [-\frac{1}{2}, \frac{1}{2}] \times (0, \infty)$ against $\int_{-1/2}^{1/2} E^*(x + iy, s_2)\,dx = E_0^*(y, s_2)$ gives **with zero approximation**:
   $$
   \frac{I_{PE}(T)}{\Lambda(2 - 2s_1)\Lambda(2 - 2s_2)} = \int_{Y_1}^T y^{-1 - s_1}\Bigl(\overline{\Phi(w_2)}\,y^{s_2} + y^{1 - s_2}\Bigr) dy = \overline{\Phi(w_2)}\,\frac{T^{s_2 - s_1} - Y_1^{s_2 - s_1}}{s_2 - s_1} + \frac{T^{1 - s_1 - s_2} - Y_1^{1 - s_1 - s_2}}{1 - s_1 - s_2},
   \tag{2.8}
   $$
   and symmetrically ($1 \leftrightarrow 2$, $s_1 \leftrightarrow s_2$, $\overline{\Phi(w_2)} \leftrightarrow \Phi(w_1)$),
   $$
   \frac{I_{EP}(T)}{\Lambda(2 - 2s_1)\Lambda(2 - 2s_2)} = \Phi(w_1)\,\frac{T^{s_1 - s_2} - Y_2^{s_1 - s_2}}{s_1 - s_2} + \frac{T^{1 - s_1 - s_2} - Y_2^{1 - s_1 - s_2}}{1 - s_1 - s_2}.
   \tag{2.9}
   $$
3. **Bruhat double-coset unfolding of $I_{PP}(T)$:** Writing $I_{PP}(T) = \int_{\mathcal{F}} \bigl(P_{w_1}^{Y_1}(z)\mathbf{1}_{\mathcal{F}_T}(z)\bigr)\overline{P_{w_2}^{Y_2}(z)}\,d\mu(z)$, insert (2.6) on the first factor and unfold onto $[-\frac{1}{2}, \frac{1}{2}] \times (Y_1, T]$. Decomposing $\gamma \in \Gamma_\infty \backslash \Gamma$ into Bruhat double cosets [8, Theorem 2.7]:
   - The identity coset $\gamma = I$ ($c = 0$) integrates $y^{-s_1 - s_2}$ over $\max(Y_1, Y_2) < y \le T$, contributing $\frac{T^{1 - s_1 - s_2} - \max(Y_1, Y_2)^{1 - s_1 - s_2}}{1 - s_1 - s_2}$.
   - Each $c \ge 1$ is parametrized by $d \pmod c$ with $\gcd(c, d) = 1$ ($\varphi(c)$ choices) and $m \in \mathbb{Z}$, merging $\sum_{m \in \mathbb{Z}} \int_{-1/2}^{1/2} dx$ into $\int_{-\infty}^{\infty} du$ ($u = x + m + d/c$) with $\operatorname{Im}\gamma(x + iy) = \frac{y}{c^2(u^2 + y^2)}$. Crucially, $\frac{y}{c^2(u^2 + y^2)} > Y_2$ forces $y < \frac{1}{c^2 Y_2} \le \frac{1}{Y_2} < T$ (so the upper cutoff $y \le T$ is **automatically satisfied**) and $c^2 Y_1 Y_2 < 1$, i.e., **$1 \le c < X := (Y_1 Y_2)^{-1/2}$**!

Combining (2.7)–(2.9) with $I_{PP}(T)$, all three growing powers $T^{1 - s_1 - s_2}$, $T^{s_1 - s_2}$, and $T^{s_2 - s_1}$ cancel identically at finite $T$. Using $Y_1^\alpha + Y_2^\alpha - \max(Y_1, Y_2)^\alpha = \min(Y_1, Y_2)^\alpha$ ($\alpha = 1 - s_1 - s_2 = 1 - \frac{w_1 + \bar w_2}{2}$) and letting $T \to \infty$, we obtain $G_{Y_1, Y_2}(w_1, w_2) = A_{Y_1, Y_2}(w_1, w_2) + \widetilde{B}_{Y_1, Y_2}(w_1, w_2) + R_{Y_1, Y_2}(w_1, w_2)$, where
$$
\widetilde{B}_{Y_1, Y_2}(w_1, w_2) := 2 \sum_{1 \le c < X} \varphi(c) \iint_{\substack{y_1 > Y_1,\; u > 0 \\ \frac{y_1}{c^2(u^2 + y_1^2)} > Y_2}} y_1^{1 - s_1}\left(\frac{y_1}{c^2(u^2 + y_1^2)}\right)^{\!1 - s_2} \frac{du\,dy_1}{y_1^2}.
\tag{2.10}
$$

---

### 2.3. Symmetric Ford-Circle Variable $\xi = c^2 y_1 y_2$ and Confluent ${}_3F_2$ Limit

To evaluate (2.10) in closed form for each $1 \le c < X$ ($a_c := c\sqrt{Y_1 Y_2} \in (0, 1)$), set $y_2 := \frac{y_1}{c^2(u^2 + y_1^2)}$ and introduce the dimensionless product variable $\xi := c^2 y_1 y_2 = \frac{y_1^2}{u^2 + y_1^2}$. On the integration domain $\{y_1 > Y_1,\; u > 0,\; y_2 > Y_2\}$, we have $a_c^2 < \xi < 1$ and, for each fixed $\xi \in (a_c^2, 1)$, $Y_1 < y_1 < \frac{\xi}{c^2 Y_2}$. Holding $y_1$ fixed in $u = y_1(\xi^{-1} - 1)^{1/2}$ gives $du = -\frac{y_1}{2\xi^{3/2}(1 - \xi)^{1/2}}\,d\xi$. Substituting $y_2 = \frac{\xi}{c^2 y_1}$ separates $(\xi, y_1)$ completely:
$$
2 \iint y_1^{-1 - s_1} y_2^{1 - s_2}\,du\,dy_1
= c^{2s_2 - 2} \int_{a_c^2}^1 \xi^{-\frac{1}{2} - s_2}(1 - \xi)^{-\frac{1}{2}} \left(\int_{Y_1}^{\frac{\xi}{c^2 Y_2}} y_1^{s_2 - s_1 - 1}\,dy_1\right) d\xi.
\tag{2.11}
$$

- **Non-confluent case ($s_1 \ne s_2$, i.e., $w_1 \ne \bar w_2$):** The inner integral in (2.11) equals $-\frac{c^{2s_1 - 2s_2} Y_2^{s_1 - s_2}\xi^{s_2 - s_1} - Y_1^{s_2 - s_1}}{s_1 - s_2}$. Substituting $t = 1 - \xi \in (0, 1 - a_c^2)$ evaluates $\int_{a_c^2}^1 \xi^{\nu_j - 1}(1 - \xi)^{-1/2}\,d\xi = B_{1 - a_c^2}(\frac{1}{2}, \nu_j)$ with $\nu_1 = \frac{1}{2} - s_1 = \frac{1 - w_1}{2}$ and $\nu_2 = \frac{1}{2} - s_2 = \frac{1 - \bar w_2}{2}$. Summing over $1 \le c < X$ with weight $\varphi(c)$ yields $\widetilde{B}_{Y_1, Y_2}(w_1, w_2) = B_{Y_1, Y_2}(w_1, w_2)$ in (1.7).

- **Confluent case ($s_1 = s_2$, i.e., $w_2 = \bar w_1$, $\nu = \frac{1 - w_1}{2}$):** The inner integral in (2.11) is $\int_{Y_1}^{\xi/(c^2 Y_2)} y_1^{-1}\,dy_1 = \log\xi - \log(a_c^2)$. For $\operatorname{Re} u > 0$ and $0 < a_c^2 < 1$, expanding $(1 - \xi)^{-1/2} = \sum_{m=0}^{\infty} \frac{(1/2)_m}{m!}\,\xi^m$ on $(0, a_c^2)$ gives
  $$
  \int_{a_c^2}^1 \xi^{u - 1}(1 - \xi)^{-1/2}\,d\xi = B\!\left(\frac{1}{2},\, u\right) - \sum_{m=0}^{\infty} \frac{(1/2)_m}{m!}\,\frac{a_c^{2(u + m)}}{u + m}.
  \tag{2.12}
  $$
  Differentiating (2.12) with respect to $u$ at $u = \nu$ ($\operatorname{Re}\nu = \frac{1 - \sigma_1}{2} > 0$) and subtracting $\log(a_c^2)$ times (2.12) cancels the $\log(a_c^2)\sum_{m=0}^{\infty}$ series identically, leaving
  $$
  \int_{a_c^2}^1 \xi^{\nu - 1}(1 - \xi)^{-1/2}\bigl(\log\xi - \log(a_c^2)\bigr)\,d\xi
  = B\!\left(\frac{1}{2},\, \nu\right)\Bigl(\psi(\nu) - \psi\!\left(\nu + \tfrac{1}{2}\right) - \log(a_c^2)\Bigr) + \sum_{m=0}^{\infty} \frac{(1/2)_m}{m!}\,\frac{a_c^{2(\nu + m)}}{(\nu + m)^2},
  $$
  which sums over $1 \le c < X$ to (1.8). Likewise, since $\overline{\Phi(w_2)} = \Phi(\bar w_2)$, setting $\delta := \frac{w_1 - \bar w_2}{2} \to 0$ in (1.9) gives $\lim_{\delta \to 0} \frac{\Phi(w_1) Y_2^\delta - \Phi(w_1 - 2\delta) Y_1^{-\delta}}{\delta} = 2\Phi'(w_1) + \Phi(w_1)\log(Y_1 Y_2)$, proving Theorem 1(3). Finally, if $\sigma \in (0, 1)$ is real, then $(1 - 2^{1-\sigma})\zeta(\sigma) = \sum_{n=1}^{\infty} (-1)^{n-1} n^{-\sigma} > 0$ with $1 - 2^{1-\sigma} < 0$, so $\zeta(\sigma) < 0$ and $\Lambda(\sigma) < 0$ on $(0, 1)$; hence every zero $\Lambda(\rho) = 0$ in $\mathcal{S}_{(0,1)}$ has $\operatorname{Im}\rho \ne 0$ ($\rho \ne \bar\rho$), and substituting $\Phi(\rho) = 0$ and $\Phi'(\rho) = \Lambda'(\rho)/\Lambda(2 - \rho)$ into (1.9) gives Theorem 1(4). $\square$

---

## 3. Proofs of Theorems 2 and 3: Spectral Identity, Perron Annihilation, and Zero-Gram Criteria

### 3.1. Orthogonality to Cusp Forms and Spectral Parseval Identity

*Proof of Theorem 2(1).* Let $\{u_j\}_{j \ge 1}$ be an orthonormal basis of Maass cusp forms in $L^2(\Gamma\backslash\mathbb{H})$. Each $u_j$ decays rapidly at the cusp and has vanishing zero-th Fourier mode $\int_{-1/2}^{1/2} u_j(x + iy)\,dx = 0$ for all $y > 0$ [8, §4.1]. Unfolding $P_w^Y$ against $u_j$ (using (2.6) and letting $T \to \infty$) integrates $\int_{-1/2}^{1/2} u_j(x + iy)\,dx = 0$, giving $\langle P_w^Y, u_j\rangle_{L^2(\mathcal{F})} = 0$. Similarly, for $\operatorname{Re} s > 1$, unfolding $E(z, s)$ against $u_j$ vanishes identically; since $u_j$ has rapid cusp decay, $w \mapsto \langle E^*(\cdot, w/2), u_j\rangle_{L^2(\mathcal{F})}$ is holomorphic on $\mathcal{S}_{(0,1)} \cup \{\operatorname{Re} w < 0\}$ and vanishes for $\operatorname{Re} w < 0$, hence vanishes on $\mathcal{S}_{(0,1)}$. Thus $\langle F_w^Y, u_j\rangle_{L^2(\mathcal{F})} = 0$ for every $j \ge 1$.

By the Roelcke–Selberg spectral theorem [8, Theorem 7.3], for all $F_1, F_2 \in L^2(\Gamma\backslash\mathbb{H})$ orthogonal to all cusp forms,
$$
\langle F_1, F_2\rangle_{L^2(\mathcal{F})} = \frac{\langle F_1, 1\rangle\,\overline{\langle F_2, 1\rangle}}{\operatorname{vol}(\mathcal{F})} + \frac{1}{4\pi}\int_{-\infty}^{\infty} \widehat{F}_1(t)\,\overline{\widehat{F}_2(t)}\,dt, \qquad
\widehat{F}(t) := \operatorname*{l.i.m.}_{T \to \infty} \int_{\mathcal{F}_T} F(z)\,\overline{E(z, \tfrac{1}{2} + it)}\,d\mu(z),
\tag{3.1}
$$
where $\operatorname{vol}(\mathcal{F}) = \frac{\pi}{3}$ and $\operatorname{l.i.m.}$ denotes the $L^2(\mathbb{R})$ limit. We compute both projections for $F = F_w^Y$ ($s = w/2$, $\sigma = \operatorname{Re} w \in (0, 1)$):

- **Constant residual eigenfunction:** For $T > \max(1, Y, 1/Y)$, Green's theorem gives $\int_{\mathcal{F}_T} E^*(z, s)\,d\mu(z) = \frac{1}{s(s-1)}\int_{\mathcal{F}_T} \Delta E^*(z, s)\,d\mu(z) = \frac{\partial_T E_0^*(T, s)}{s(s-1)} = \frac{s\Lambda(2s) T^{s-1} + (1-s)\Lambda(2-2s) T^{-s}}{s(s-1)} \to 0$ as $T \to \infty$ because $\operatorname{Re} s = \sigma/2 \in (0, \frac{1}{2})$. Meanwhile, unfolding (2.6) gives $\int_{\mathcal{F}_T} P_w^Y(z)\,d\mu(z) = \Lambda(2 - w)\int_Y^T y^{-1-s}\,dy = \Lambda(2 - w)\frac{Y^{-w/2} - T^{-w/2}}{w/2} \to \Lambda(2 - w)\frac{2 Y^{-w/2}}{w}$. Hence
  $$
  \frac{\langle F_w^Y, 1\rangle_{L^2(\mathcal{F})}}{\Lambda(2 - w)} = -\frac{2}{w}\,Y^{-w/2}, \qquad
  \frac{\langle F_{w_1}^{Y_1}, 1\rangle\,\overline{\langle F_{w_2}^{Y_2}, 1\rangle}}{\operatorname{vol}(\mathcal{F})\,\Lambda(2 - w_1)\overline{\Lambda(2 - w_2)}} = \frac{3}{\pi}\cdot\frac{4}{w_1 \bar w_2}\,Y_1^{-w_1/2} Y_2^{-\bar w_2/2} = \frac{12}{\pi w_1 \bar w_2}\,Y_1^{-w_1/2} Y_2^{-\bar w_2/2}.
  \tag{3.2}
  $$
- **Continuous Eisenstein transform:** For $t \in \mathbb{R} \setminus \{0\}$, the zero-th Fourier mode of $\overline{E(z, \frac{1}{2} + it)} = E(z, \frac{1}{2} - it) = \frac{E^*(z, \frac{1}{2} - it)}{\Lambda(1 - 2it)}$ is $y^{\frac{1}{2} - it} + S(t)\,y^{\frac{1}{2} + it}$, where $S(t) = \frac{\Lambda(1 + 2it)}{\Lambda(1 - 2it)}$ satisfies $|S(t)| = 1$ and $S(-t) = S(t)^{-1}$. Applying Maass–Selberg on $\mathcal{F}_T$ to $\frac{1}{\Lambda(2 - 2s)}\int_{\mathcal{F}_T} E^*(z, s) E(z, \frac{1}{2} - it)\,d\mu(z)$ ($s_0 := \frac{1}{2} - it$) produces two decaying terms $\Phi(w)\frac{T^{s + s_0 - 1}}{s + s_0 - 1} + \Phi(w) S(t)\frac{T^{s - s_0}}{s - s_0} = O_w(T^{(\sigma - 1)/2})$ (uniformly for $t \in \mathbb{R}$ separated from $0$, and in fact uniformly for all $t \in \mathbb{R}$ since $\operatorname{Re}(s - s_0) = \operatorname{Re}(s + s_0 - 1) = \frac{\sigma - 1}{2} < 0$) plus two growing terms $\frac{T^{s_0 - s}}{s_0 - s} + S(t)\frac{T^{1 - s - s_0}}{1 - s - s_0} + O(e^{-2\pi T})$. Unfolding $\frac{1}{\Lambda(2 - 2s)}\int_{\mathcal{F}_T} P_w^Y(z) E(z, s_0)\,d\mu(z) = \int_Y^T y^{-1 - s}(y^{s_0} + S(t) y^{1 - s_0})\,dy$ produces $\frac{T^{s_0 - s} - Y^{s_0 - s}}{s_0 - s} + S(t)\frac{T^{1 - s - s_0} - Y^{1 - s - s_0}}{1 - s - s_0}$, canceling the growing $T$-powers **identically at finite $T$**! Since $s_0 - s = \frac{1 - w}{2} - it$ and $1 - s - s_0 = \frac{1 - w}{2} + it$, letting $T \to \infty$ gives $\frac{\widehat{F_w^Y}(t)}{\Lambda(2 - w)} = -f_{w, Y}(t)$ in (1.15).

Finally, since $S(-t) = S(t)^{-1}$ and $|S(t)| = 1$, we have $f_{w, Y}(-t) = S(t)^{-1} f_{w, Y}(t)$, so $f_{w_1, Y_1}(-t)\,\overline{f_{w_2, Y_2}(-t)} = f_{w_1, Y_1}(t)\,\overline{f_{w_2, Y_2}(t)}$ is **even in $t$**. Thus $\frac{1}{4\pi}\int_{-\infty}^{\infty} = \frac{1}{2\pi}\int_0^{\infty}$, establishing (1.16). Since $|f_{w, Y}(t)| \le \frac{2 Y^{(1-\sigma)/2}}{|\frac{1-\sigma}{2} + i(t - \gamma/2)|} + \frac{2 Y^{(1-\sigma)/2}}{|\frac{1-\sigma}{2} + i(t + \gamma/2)|}$ (more precisely $\le Y^{(1-\sigma)/2}\bigl(|{\frac{1-w}{2}-it}|^{-1} + |{\frac{1-w}{2}+it}|^{-1}\bigr) \in L^2(\mathbb{R})$), the integral in (1.16) is non-negative when $(w_1, Y_1) = (w_2, Y_2)$ and $O_w(Y^{1-\sigma})$, completing Theorem 2(1). $\square$

---

### 3.2. Perron Pole Cancellation, Global Plancherel Bound, and Riemann–Lebesgue Limit

*Proof of Theorem 2(2).* Fix $\lambda > 1$ and $w = \sigma + i\gamma \in \mathcal{S}_{(0,1)}$. Since $\sigma > 0$, $|\lambda^{-w/2}| = \lambda^{-\sigma/2} < 1$, so $\lambda^{-w/2} \ne 1$ and $\mathbf{c} = (c_1, c_2)$ in (1.17) is uniquely determined by $c_1 + c_2 = 1$ and $c_1 + c_2 \lambda^{-w/2} = 0$. By (3.2), $\langle \widetilde{D}_w^{Y, \lambda}, 1\rangle_{L^2(\mathcal{F})} = -\frac{2}{w} Y^{-w/2}(c_1 + c_2 \lambda^{-w/2}) = 0$.

On the continuous spectrum, put $g_{w, Y, \lambda}(t) := c_1 f_{w, Y}(t) + c_2 f_{w, \lambda Y}(t) = A_Y(t) + S(t) B_Y(t)$, where
$$
A_Y(t) := Y^{\frac{1 - w}{2} - it}\,U^-(t), \qquad
B_Y(t) := Y^{\frac{1 - w}{2} + it}\,U^+(t), \qquad
U^\mp(t) := \frac{c_1 + c_2 \lambda^{\frac{1 - w}{2} \mp it}}{\frac{1 - w}{2} \mp it}.
\tag{3.3}
$$
Observe that $A_Y(t) = \int_{-\infty}^{\infty} \eta(\xi)\,e^{-it\xi}\,d\xi$ and $B_Y(t) = A_Y(-t) = \int_{-\infty}^{\infty} \eta(\xi)\,e^{+it\xi}\,d\xi$ are the Fourier transforms of the two-step exponential profile
$$
\eta(\xi) := e^{\frac{1 - w}{2}\xi}\Bigl(c_1\,\mathbf{1}_{(-\infty, \log Y)}(\xi) + c_2\,\mathbf{1}_{(-\infty, \log(\lambda Y))}(\xi)\Bigr)
= e^{\frac{1 - w}{2}\xi}\Bigl(\mathbf{1}_{(-\infty, \log Y)}(\xi) + c_2\,\mathbf{1}_{[\log Y, \log(\lambda Y))}(\xi)\Bigr),
\tag{3.4}
$$
where we used $c_1 + c_2 = 1$ on $(-\infty, \log Y)$. Because $1 - \sigma > 0$, elementary integration gives
$$
\|\eta\|_{L^2(\mathbb{R})}^2 = \int_{-\infty}^{\log Y} e^{(1 - \sigma)\xi}\,d\xi + |c_2|^2 \int_{\log Y}^{\log(\lambda Y)} e^{(1 - \sigma)\xi}\,d\xi = \frac{1 + |c_2|^2(\lambda^{1 - \sigma} - 1)}{1 - \sigma}\,Y^{1 - \sigma} = C_{\mathrm{RL}}(w, \lambda)\,Y^{1 - \sigma}.
\tag{3.5}
$$
By Plancherel's theorem on $L^2(\mathbb{R})$, $\frac{1}{2\pi}\int_{-\infty}^{\infty} |A_Y(t)|^2\,dt = \frac{1}{2\pi}\int_{-\infty}^{\infty} |B_Y(t)|^2\,dt = C_{\mathrm{RL}}(w, \lambda)\,Y^{1 - \sigma}$. Applying (3.1) (over $\mathbb{R}$ with prefactor $\frac{1}{4\pi}$) and the pointwise inequality $|A_Y(t) + S(t) B_Y(t)|^2 \le 2\bigl(|A_Y(t)|^2 + |S(t)|^2 |B_Y(t)|^2\bigr) = 2\bigl(|A_Y(t)|^2 + |B_Y(t)|^2\bigr)$ ($|S(t)| = 1$), we obtain **for every $Y > 0$**:
$$
\left\|\widetilde{D}_w^{Y, \lambda}\right\|_{L^2(\mathcal{F})}^2 = \frac{1}{4\pi}\int_{-\infty}^{\infty} \bigl|A_Y(t) + S(t) B_Y(t)\bigr|^2\,dt \le \frac{2}{4\pi}\int_{-\infty}^{\infty} \bigl(|A_Y(t)|^2 + |B_Y(t)|^2\bigr)\,dt = 2 C_{\mathrm{RL}}(w, \lambda)\,Y^{1 - \sigma},
$$
proving (1.19). Expanding $|A_Y + S B_Y|^2 = |A_Y|^2 + |B_Y|^2 + 2\operatorname{Re}(\overline{A_Y} B_Y S)$ similarly gives
$$
Y^{-(1 - \sigma)}\left\|\widetilde{D}_w^{Y, \lambda}\right\|_{L^2(\mathcal{F})}^2 = C_{\mathrm{RL}}(w, \lambda) + \frac{1}{2\pi}\operatorname{Re}\int_{-\infty}^{\infty} \overline{U^-(t)}\,U^+(t)\,S(t)\,e^{2it\log Y}\,dt.
\tag{3.6}
$$
Since $|U^\mp(t)| \ll_{w, \lambda} (1 + |t|)^{-1}$ and $|S(t)| = 1$, the integrand $\overline{U^-(t)}\,U^+(t)\,S(t)$ belongs to $L^1(\mathbb{R})$. As $Y \to 0^+$, $2\log Y \to -\infty$, so the integral in (3.6) vanishes by the Riemann–Lebesgue lemma, proving (1.20). $\square$

---

### 3.3. Linear Independence, Unit-Modulus Phase Identity, and Zero-Gram Refutations

*Proof of Theorem 3.* **(1) Linear independence and equivalence (i)$\iff$(ii)$\iff$(iii):** Let $0 < Y_1 < \dots < Y_L$ and suppose $\sum_{j=1}^L \alpha_j F_w^{Y_j} = 0$ in $L^2(\Gamma\backslash\mathbb{H})$. For every $y > 0$, consider the zero-th $x$-Fourier mode $a_0(y; P_w^Y) := \int_{-1/2}^{1/2} P_w^Y(x + iy)\,dx$. By Bruhat unfolding,
$$
\frac{a_0(y; P_w^Y)}{\Lambda(2 - w)} = y^{1 - w/2}\,\mathbf{1}_{\{y > Y\}} + \sum_{c=1}^{\infty} \frac{\varphi(c)}{c^{2 - w}} \int_{\{u \in \mathbb{R} : u^2 < (y/(c^2 Y) - y^2)_+\}} \left(\frac{y}{u^2 + y^2}\right)^{\!1 - w/2} du.
\tag{3.7}
$$
For each $c \ge 1$, the integral in (3.7) is a continuous function of $y \in (0, \infty)$ (and only finitely many $c < (y Y)^{-1/2}$ are nonzero on any interval $[y_{\min}, y_{\max}] \subset (0, \infty)$), while $E_0^*(y, w/2)$ is smooth on $(0, \infty)$. By contrast, $y^{1 - w/2}\,\mathbf{1}_{\{y > Y\}}$ has a jump discontinuity of $\Lambda(2 - w)\,Y^{1 - w/2} \ne 0$ at $y = Y$. Hence $a_0\bigl(y; \sum_{j=1}^L \alpha_j F_w^{Y_j}\bigr) = 0$ a.e. on $(0, \infty)$ forces $\alpha_j = 0$ at each jump $y = Y_j$ ($1 \le j \le L$). Thus $\mathbf{G}_L(w; Y_1, \dots, Y_L) \succ 0$ for all $w \in \mathcal{S}_{(0,1)}$ and all distinct $Y_1, \dots, Y_L > 0$.

If $\Lambda(w) = 0$, Theorem 1(4) gives $\mathbf{K}_2(w; Y, \lambda Y) = \mathbf{G}_2(w; Y, \lambda Y) \succ 0$ for all $Y > 0$, so (i)$\implies$(ii)$\implies$(iii). That (iii)$\implies$(i) follows immediately from part (2) below, which shows that whenever $\Lambda(w) \ne 0$, there exist arbitrarily small heights $Y \in (0, 1)$ with $\det \mathbf{K}_2(w; Y, \lambda Y) < 0$.

**(2) Explicit refutation of non-zeros:** Assume $\Lambda(w) \ne 0$, so $\Phi(w) \ne 0$.
- *Case $\gamma \ne 0$:* Here $(w - \bar w)/2 = i\gamma \ne 0$. By (1.9) and $c_1 + c_2 = 1$,
  $$
  \mathbf{c}\,\mathbf{R}_2(w; Y, \lambda Y)\,\mathbf{c}^* = \sum_{j,k=1}^2 c_j\,\frac{\Phi(w) Y_k^{i\gamma} - \overline{\Phi(w)} Y_j^{-i\gamma}}{i\gamma}\,\bar c_k = \frac{2}{\gamma}\,\operatorname{Im}\!\Bigl(\Phi(w)\,Y^{i\gamma}\bigl(\bar c_1 + \bar c_2 \lambda^{i\gamma}\bigr)\Bigr).
  $$
  Put $z := \lambda^{-w/2} = \lambda^{-\sigma/2} \lambda^{-i\gamma/2}$; then $|z| = \lambda^{-\sigma/2} \in (0, 1)$, $\lambda^{i\gamma} = \bar z / z$, and $\bar c_2 = -(\bar z - 1)^{-1}$, so
  $$
  \bar c_1 + \bar c_2 \lambda^{i\gamma} = 1 + \bar c_2(\lambda^{i\gamma} - 1) = 1 - \frac{\bar z - z}{z(\bar z - 1)} = \frac{\bar z(z - 1)}{z(\bar z - 1)} =: e^{i\theta(w, \lambda)}, \qquad \bigl|e^{i\theta(w, \lambda)}\bigr| = \frac{|\bar z|\,|z - 1|}{|z|\,|\bar z - 1|} = 1,
  \tag{3.8}
  $$
  yielding (1.21) via $\mathbf{K}_2 = \mathbf{G}_2 - \mathbf{R}_2$. Writing $\operatorname{sgn}(\gamma)\Phi(w) e^{i\theta(w, \lambda)} = |\Phi(w)| e^{i\alpha}$, the heights $Y_m := \exp\!\bigl(\frac{(\pi/2 - \alpha) - 2\pi m}{|\gamma|}\bigr)$ ($m \in \mathbb{Z}$, $Y_m \to 0^+$ as $m \to +\infty$) satisfy $\frac{2}{\gamma}\operatorname{Im}\bigl(\Phi(w) e^{i\theta(w, \lambda)} Y_m^{i\gamma}\bigr) = \frac{2|\Phi(w)|}{|\gamma|}$. By (1.19), at every such $Y_m$,
  $$
  \mathbf{c}\,\mathbf{K}_2(w; Y_m, \lambda Y_m)\,\mathbf{c}^* \le 2 C_{\mathrm{RL}}(w, \lambda)\,Y_m^{1 - \sigma} - \frac{2|\Phi(w)|}{|\gamma|},
  $$
  which is strictly negative whenever $Y_m < Y_{\mathrm{ref}}(w, \lambda)$ in (1.22). Meanwhile, by Theorem 2(1) and $|R_{Y, Y}(w, w)| = \bigl|\frac{2\operatorname{Im}(\Phi(w) Y^{i\gamma})}{\gamma}\bigr| \le \frac{2|\Phi(w)|}{|\gamma|}$, the $(1, 1)$ entry satisfies $K_{Y_m, Y_m}(w, w) \ge \frac{12}{\pi |w|^2}\,Y_m^{-\sigma} - \frac{2|\Phi(w)|}{|\gamma|} > 0$ whenever $Y_m < \bigl(\frac{6|\gamma|}{\pi |w|^2 |\Phi(w)|}\bigr)^{1/\sigma}$. Having both $K_{11} > 0$ and $\mathbf{c}\,\mathbf{K}_2\,\mathbf{c}^* < 0$, the $2\times 2$ Hermitian matrix $\mathbf{K}_2(w; Y_m, \lambda Y_m)$ has one positive and one negative eigenvalue by Sylvester's law of inertia, so $\det \mathbf{K}_2(w; Y_m, \lambda Y_m) < 0$.
- *Case $\gamma = 0$ ($w = \sigma \in (0, 1)$):* As shown at the end of §2.3, $\Lambda(\sigma) < 0$ while $\Lambda(2 - \sigma) > 0$, so $\Phi(\sigma) = -|\Phi(\sigma)| < 0$. Here $w = \bar w = \sigma$ lies in the confluent case of (1.9): $R_{Y_i, Y_j}(\sigma, \sigma) = 2\Phi'(\sigma) + \Phi(\sigma)\log(Y_i Y_j)$. For $Y \in (0, 1)$, $\log Y = -|\log Y| < 0$, so $\Phi(\sigma)\log Y = +|\Phi(\sigma)|\,|\log Y| > 0$. Since $c_1 + c_2 = 1$ ($c_1, c_2 \in \mathbb{R}$),
  $$
  \mathbf{c}\,\mathbf{K}_2(\sigma; Y, \lambda Y)\,\mathbf{c}^* = \left\|\widetilde{D}_\sigma^{Y, \lambda}\right\|_{L^2(\mathcal{F})}^2 - 2|\Phi(\sigma)|\,|\log Y| - 2\Phi'(\sigma) - 2 c_2 \Phi(\sigma)\log\lambda \xrightarrow{Y \to 0^+} -\infty,
  $$
  whereas $K_{Y, Y}(\sigma, \sigma) \ge \frac{12}{\pi\sigma^2}\,Y^{-\sigma} - 2|\Phi(\sigma)|\,|\log Y| - 2\Phi'(\sigma) \xrightarrow{Y \to 0^+} +\infty$. Hence $\det \mathbf{K}_2(\sigma; Y, \lambda Y) < 0$ for all sufficiently small $Y > 0$.

**(3) Scope boundary and fake $L$-functions:** Both claims in Theorem 3(3) follow directly from parts (1)–(2) and continuity of $(w, Y) \mapsto \det \mathbf{K}_2(w; Y, \lambda Y)$ on $(0, 1)$ away from the discrete Ford-circle thresholds $c^2 \lambda Y^2 = 1$ (in fact $K_{Y_1, Y_2}$ is continuous across $a_c = 1$ as well because $B_0(\frac{1}{2}, \nu) = 0$): if $\zeta(w_\star) \ne 0$, picking a rational height $Y = 1/q$ near a peak-phase height $Y_m$ below the threshold in (2) yields $\det \mathbf{K}_2(w_\star; 1/q, \lambda/q) < 0$ from the finitely many Ford circles $1 \le c < q \lambda^{-1/2}$. $\square$

---

## 4. Proof of Theorem 4: Finite Ford-Circle Multiplicity-One Disks and Completeness

*Proof of Theorem 4.* Let $\rho = \sigma + i\gamma \in \mathcal{S}_{(0,1)}$ satisfy $\Lambda(\rho) = 0$ (hence $\gamma \ne 0$ and $\Lambda(\bar\rho) = 0$). Fix $0 < Y_1 < \dots < Y_L$ and $\mathbf{c} = (c_1, \dots, c_L) \in \mathbb{C}^L$ with $\sum_{j=1}^L c_j = 1$, and set
$$
H(z) := \sum_{j=1}^L c_j\,\frac{F_\rho^{Y_j}(z)}{\Lambda(2 - \rho)} \in L^2(\Gamma\backslash\mathbb{H}).
\tag{4.1}
$$
For real $Y_j > 0$ and every $z \in \mathbb{H}$, $\overline{E^*(z, \rho/2)} = E^*(z, \bar\rho/2)$, $\overline{P_\rho^{Y_j}(z)} = P_{\bar\rho}^{Y_j}(z)$, and $\overline{\Lambda(2 - \rho)} = \Lambda(2 - \bar\rho)$, so pointwise on $\mathbb{H}$,
$$
\overline{H(z)} = \sum_{k=1}^L \bar c_k\,\frac{F_{\bar\rho}^{Y_k}(z)}{\Lambda(2 - \bar\rho)}, \qquad
\|\overline{H}\|_{L^2(\mathcal{F})} = \|H\|_{L^2(\mathcal{F})}.
\tag{4.2}
$$
By Theorem 1(4) and Theorem 3(1), the Hermitian squared norm is
$$
\|H\|_{L^2(\mathcal{F})}^2 = \sum_{j=1}^L \sum_{k=1}^L c_j \bar c_k\,G_{Y_j, Y_k}(\rho, \rho) = \sum_{j=1}^L \sum_{k=1}^L c_j \bar c_k\,K_{Y_j, Y_k}(\rho, \rho) = K_{\mathbf{c}}^{\mathrm{diag}} > 0.
\tag{4.3}
$$
On the other hand, because $\langle f, g\rangle_{L^2(\mathcal{F})} = \int_{\mathcal{F}} f\,\bar g\,d\mu$ is conjugate-linear in the second argument, the inner product of $H$ with $\overline{H}$ conjugates the coefficients $\bar c_k$ back to $c_k$, producing the **complex-symmetric bilinear form**:
$$
\bigl\langle H,\, \overline{H}\bigr\rangle_{L^2(\mathcal{F})} = \int_{\mathcal{F}} H(z)^2\,d\mu(z) = \sum_{j=1}^L \sum_{k=1}^L c_j c_k\,G_{Y_j, Y_k}(\rho, \bar\rho) = \sum_{j=1}^L \sum_{k=1}^L c_j c_k\bigl(K_{Y_j, Y_k}(\rho, \bar\rho) + Z(\rho)\bigr) = K_{\mathbf{c}}^{\mathrm{conj}} + Z(\rho),
\tag{4.4}
$$
since $\sum_{j,k=1}^L c_j c_k = \bigl(\sum_{j=1}^L c_j\bigr)^2 = 1^2 = 1$. By the Cauchy–Schwarz inequality in $L^2(\mathcal{F})$,
$$
\bigl|K_{\mathbf{c}}^{\mathrm{conj}} + Z(\rho)\bigr| = \bigl|\langle H, \overline{H}\rangle_{L^2(\mathcal{F})}\bigr| \le \|H\|_{L^2(\mathcal{F})}\,\|\overline{H}\|_{L^2(\mathcal{F})} = \|H\|_{L^2(\mathcal{F})}^2 = K_{\mathbf{c}}^{\mathrm{diag}},
$$
which is (1.24). The reverse and forward triangle inequalities $\bigl||K_{\mathbf{c}}^{\mathrm{conj}}| - |Z(\rho)|\bigr| \le |K_{\mathbf{c}}^{\mathrm{conj}} + Z(\rho)| \le K_{\mathbf{c}}^{\mathrm{diag}}$ immediately yield (1.25); whenever $|K_{\mathbf{c}}^{\mathrm{conj}}| > K_{\mathbf{c}}^{\mathrm{diag}}$, $|Z(\rho)| > 0$, forcing $\Lambda'(\rho) \ne 0$ (and hence $\zeta'(\rho) \ne 0$ because $\pi^{-s/2}\Gamma(s/2)$ is holomorphic and nonvanishing on $\mathcal{S}_{(0,1)}$).

For part (2), take $L = 2$, $(Y_1, Y_2) = (Y, \lambda Y)$ ($\lambda > 1$), and $\mathbf{c} = (c_1, c_2)$ from (1.17). If $\rho$ is a multiple zero ($\Lambda'(\rho) = 0$), then $Z(\rho) = 0$, so (1.24) forces $|K_{\mathbf{c}}^{\mathrm{conj}}| \le K_{\mathbf{c}}^{\mathrm{diag}}$ for all $Y > 0$. Conversely, if $\rho$ is simple ($\Lambda'(\rho) \ne 0$, so $|Z(\rho)| > 0$), then by Theorem 2(2), $K_{\mathbf{c}}^{\mathrm{diag}} = \|\widetilde{D}_\rho^{Y, \lambda}\|_{L^2(\mathcal{F})}^2 \le 2 C_{\mathrm{RL}}(\rho, \lambda)\,Y^{1-\sigma} \to 0$ as $Y \to 0^+$. Choosing any integer $q \ge 2$ with $Y = 1/q < \bigl(\frac{|Z(\rho)|}{4 C_{\mathrm{RL}}(\rho, \lambda)}\bigr)^{\frac{1}{1-\sigma}}$, we have $K_{\mathbf{c}}^{\mathrm{diag}} < \frac{1}{2}|Z(\rho)|$, and (1.24) forces $|K_{\mathbf{c}}^{\mathrm{conj}}| \ge |Z(\rho)| - K_{\mathbf{c}}^{\mathrm{diag}} > \frac{1}{2}|Z(\rho)| > K_{\mathbf{c}}^{\mathrm{diag}}$. $\square$

---

## 5. Proof of Theorem 5: Completed Mellin Identity and Sub-Threshold Totient RH Equivalence

### 5.1. Exact Beta–Archimedean Cancellation and Unconditional Asymptotic

*Proof of Theorem 5(1).* Fix $w = \sigma + i\gamma \in \mathcal{S}_{(0,1)}$ and put $\nu := \frac{1 - w}{2}$ ($\operatorname{Re}\nu = \frac{1 - \sigma}{2} \in (0, \frac{1}{2})$). By (1.4)–(1.5), $\mathcal{D}_X(w) = 0$ for $0 < X \le 1$, and for $X > 1$, $\bigl|B_{1 - (c/X)^2}(\frac{1}{2}, \nu)\bigr| \le B(\frac{1}{2}, \frac{1 - \sigma}{2})$, so $|\mathcal{D}_X(w)| \ll_\sigma \sum_{1 \le c < X} c^{\sigma - 1} \ll_\sigma X^\sigma$. Hence $\int_0^{\infty} |\mathcal{D}_X(w)|\,X^{-\operatorname{Re} s - 1}\,dX < \infty$ whenever $\operatorname{Re} s > \sigma$. By Fubini's theorem, substituting $X = c/a$ ($0 < a < 1$, $X^{-s-1}\,dX = c^{-s} a^{s-1}\,da$) gives, for $\operatorname{Re} s > \sigma$,
$$
\mathcal{M}_w(s) = \sum_{c=1}^{\infty} \frac{\varphi(c)}{c^{2 - w + s}} \int_0^1 a^{s - 1}\,B_{1 - a^2}\!\left(\frac{1}{2},\, \nu\right) da.
\tag{5.1}
$$
Since $\operatorname{Re}(2 - w + s) > 2$, Euler's product gives $\sum_{c=1}^{\infty} \varphi(c)\,c^{-(2 - w + s)} = \frac{\zeta(1 - w + s)}{\zeta(2 - w + s)}$. For the integral in (5.1) ($\operatorname{Re} s > \sigma > 0$), integration by parts with $\frac{d}{da} B_{1 - a^2}(\frac{1}{2}, \nu) = -2 a^{2\nu - 1}(1 - a^2)^{-1/2}$ (boundary terms vanish at $a = 0$ since $\operatorname{Re} s > 0$ and at $a = 1$ since $B_0 = 0$) followed by $u = a^2$ yields
$$
\int_0^1 a^{s - 1}\,B_{1 - a^2}\!\left(\frac{1}{2},\, \nu\right) da = \frac{2}{s}\int_0^1 a^{s + 2\nu - 1}(1 - a^2)^{-1/2}\,da = \frac{1}{s}\int_0^1 u^{\frac{1 - w + s}{2} - 1}(1 - u)^{-\frac{1}{2}}\,du = \frac{1}{s}\,B\!\left(\frac{1}{2},\, \frac{1 - w + s}{2}\right).
\tag{5.2}
$$
Substituting $B(\frac{1}{2}, \frac{1 - w + s}{2}) = \frac{\pi^{1/2}\,\Gamma(\frac{1 - w + s}{2})}{\Gamma(\frac{2 - w + s}{2})}$ and $\zeta(z) = \pi^{z/2}\Gamma(z/2)^{-1}\Lambda(z)$ at $z = 1 - w + s$ and $z = 2 - w + s$ cancels every $\Gamma$-factor and power of $\pi$:
$$
\frac{\zeta(1 - w + s)}{\zeta(2 - w + s)}\,B\!\left(\frac{1}{2},\, \frac{1 - w + s}{2}\right)
= \frac{\pi^{\frac{1 - w + s}{2}}\Gamma(\frac{2 - w + s}{2})\Lambda(1 - w + s)}{\pi^{\frac{2 - w + s}{2}}\Gamma(\frac{1 - w + s}{2})\Lambda(2 - w + s)}\cdot\frac{\pi^{1/2}\,\Gamma(\frac{1 - w + s}{2})}{\Gamma(\frac{2 - w + s}{2})}
= \frac{\Lambda(1 - w + s)}{\Lambda(2 - w + s)},
$$
establishing (1.26).

Recall that $\Lambda(z)$ is meromorphic on $\mathbb{C}$ with simple poles only at $z = 1$ ($\operatorname{Res} = +1$) and $z = 0$ ($\operatorname{Res} = -1$), and zeros strictly inside $0 < \operatorname{Re} z < 1$. Therefore:
- At $s = w$: $\Lambda(1 - w + s)$ has residue $+1$ while $s\Lambda(2 - w + s) = w\Lambda(2) = \frac{\pi w}{6} \ne 0$, giving a simple pole with residue $\frac{6}{\pi w}$.
- At $s = w - 1 \ne 0$: $\Lambda(1 - w + s)$ has residue $-1$ and $\Lambda(2 - w + s)$ has residue $+1$, so the poles cancel, leaving a removable singularity with value $-\frac{1}{w - 1} = \frac{1}{1 - w}$.
- At $s = w - 2 \ne 0$: $\Lambda(2 - w + s)$ has a simple pole while $\Lambda(1 - w + s) = \Lambda(-1) = \Lambda(2) = \frac{\pi}{6} \ne 0$, giving a simple zero of $\mathcal{M}_w(s)$.
- At $s = 0$: $\Lambda(2 - w) \ne 0$, so $\operatorname{Res}_{s=0}\mathcal{M}_w(s) = \frac{\Lambda(1 - w)}{\Lambda(2 - w)} = \Phi(w)$ (removable if $\Lambda(w) = 0$).
- Every remaining pole of $\mathcal{M}_w(s)$ arises from a zero $\Lambda(\rho_*) = 0$ ($\rho_* \in \mathcal{S}_{(0,1)}$) at $s_* = \rho_* + w - 2$, which satisfies $\operatorname{Re} s_* = \operatorname{Re}\rho_* + \sigma - 2 < 0$ (so $s_* \ne 0, w$). At $s = s_*$, the numerator is $\Lambda(1 - w + s_*) = \Lambda(\rho_* - 1) = \Lambda(2 - \rho_*) \ne 0$ because $\operatorname{Re}(2 - \rho_*) \in (1, 2)$ lies in the region of absolute convergence of the Euler product! Thus **no zero $\rho_*$ of $\Lambda$ ever cancels in $\mathcal{M}_w(s)$**.

To prove (1.27), fix $0 < \varepsilon < 1 - \sigma$ (so $\sigma - 1 + \varepsilon < 0$). Because $B_0(\frac{1}{2}, \nu) = 0$, $X \mapsto \mathcal{D}_X(w)$ is continuous on $(0, \infty)$; on the line $\operatorname{Re} s = \sigma + 1$, Stirling's formula gives $|\Gamma(\frac{1-w+s}{2})/\Gamma(\frac{2-w+s}{2})| \asymp (1 + |t|)^{-1/2}$ ($s = u + it$) while $\zeta(1 - w + s)$ and $\zeta(2 - w + s)^{-1}$ are bounded, so $|\mathcal{M}_w(\sigma + 1 + it)| \ll_w (1 + |t|)^{-3/2} \in L^1(\mathbb{R})$, justifying pointwise Mellin inversion $\mathcal{D}_X(w) = \frac{1}{2\pi i}\int_{\sigma + 1 - i\infty}^{\sigma + 1 + i\infty} \mathcal{M}_w(s)\,X^s\,ds$ for all $X > 0$. On the strip $\sigma - 1 + \varepsilon \le u \le \sigma + 1$, we have $\operatorname{Re}(2 - w + s) \ge 1 + \varepsilon > 1$, so $|\zeta(2 - w + s)|^{-1} \le \zeta(1 + \varepsilon) \ll_\varepsilon 1$, while convexity / Phragmén–Lindelöf on $\operatorname{Re}(1 - w + s) = u + 1 - \sigma \ge \varepsilon$ gives $|\zeta(1 - w + s)| \ll_\varepsilon (1 + |t|)^{(1 - \varepsilon)/2}$. Hence
$$
|\mathcal{M}_w(u + it)| \ll_{w, \varepsilon} (1 + |t|)^{-1} \cdot (1 + |t|)^{-1/2} \cdot (1 + |t|)^{\frac{1 - \varepsilon}{2}} = (1 + |t|)^{-1 - \varepsilon/2} \in L^1(\mathbb{R})
\tag{5.3}
$$
uniformly on $\sigma - 1 + \varepsilon \le u \le \sigma + 1$ ($|t| \ge 2$). Shifting the contour to $\operatorname{Re} s = \sigma - 1 + \varepsilon < 0$ crosses only the simple poles at $s = w$ and $s = 0$, proving (1.27). $\square$

---

### 5.2. $C^2$-Smoothed Totient Sum and Equivalence with Zero-Free Half-Planes

*Proof of Theorem 5(2)–(3).* First we verify the closed form (1.28)–(1.29). For $1 \le c < X$, put $a := c/X \in (0, 1)$. Only $v \in (a, 1)$ satisfies $c < vX$. Integrating $\int_a^1 12 v^2(1 - v)\,B_{1 - (a/v)^2}(\frac{1}{2}, \nu)\,dv$ by parts with $V(v) = 4v^3 - 3v^4$ ($V(1) = 1$) and $\frac{d}{dv} B_{1 - (a/v)^2}(\frac{1}{2}, \nu) = 2 a^{2\nu} v^{-2\nu - 1}(1 - a^2/v^2)^{-1/2}$, then setting $t = 1 - a^2/v^2 \in (0, 1 - a^2)$ ($v = a(1 - t)^{-1/2}$, $2 a^{2\nu} v^{-2\nu - 1}(1 - a^2/v^2)^{-1/2}\,dv = t^{-1/2}(1 - t)^{\nu - 1}\,dt$), gives
$$
\int_a^1 12 v^2(1 - v)\,B_{1 - (a/v)^2}\!\left(\frac{1}{2},\, \nu\right) dv
= B_{1 - a^2}\!\left(\frac{1}{2},\, \nu\right) - \int_0^{1 - a^2} t^{-1/2}\Bigl(4a^3(1 - t)^{\nu - \frac{5}{2}} - 3a^4(1 - t)^{\nu - 3}\Bigr) dt = W_\nu(a),
$$
proving (1.28)–(1.29) (recall from (1.5) that $B_{1 - a^2}(\frac{1}{2}, \mu)$ is entire in $\mu \in \mathbb{C}$ since $1 - a^2 < 1$).

For $\operatorname{Re} s > \sigma$, substituting $Y = vX$ in $\int_0^{\infty} \mathcal{D}_X^{\mathrm{sm}}(w)\,X^{-s-1}\,dX$ multiplies $\mathcal{M}_w(s)$ by $\int_0^1 12 v^{s+2}(1 - v)\,dv = \frac{12}{(s + 3)(s + 4)}$:
$$
\mathcal{M}_w^{\mathrm{sm}}(s) := \int_0^{\infty} \mathcal{D}_X^{\mathrm{sm}}(w)\,X^{-s - 1}\,dX = \frac{12}{s(s + 3)(s + 4)}\,\frac{\Lambda(1 - w + s)}{\Lambda(2 - w + s)} \qquad (\operatorname{Re} s > \sigma).
\tag{5.4}
$$
At $s = 0$, $\frac{12}{3\cdot 4} = 1$, so $\operatorname{Res}_{s=0}\mathcal{M}_w^{\mathrm{sm}}(s) = \Phi(w)$; at $s = w$, $\operatorname{Res}_{s=w}\bigl(\mathcal{M}_w^{\mathrm{sm}}(s)\,X^s\bigr) = \frac{72}{\pi w(w + 3)(w + 4)}\,X^w =: c_w X^w$. Moreover, for every $\sigma \in (0, 1)$ and $\Theta \in [\frac{1}{2}, 1)$, the abscissa $\sigma + \Theta - 2 > 0 + \frac{1}{2} - 2 = -\frac{3}{2} > -3$, so **both smoothing poles $s = -3, -4$ lie strictly to the left of $\{\operatorname{Re} s \ge \sigma + \Theta - 2\}$**.

- **Forward implication ($\Longrightarrow$) in (1.30):** Assume $\sup_{\Lambda(\rho_*)=0} \operatorname{Re}\rho_* \le \Theta \in [\frac{1}{2}, 1)$, and fix any $0 < \varepsilon < 1 - \Theta$. Then $\zeta(z)$ is nonvanishing on the half-plane $\operatorname{Re} z > \Theta$. By the classical Borel–Carathéodory / Hadamard three-circles estimate for $\log\zeta(z)$ in a zero-free half-plane (Titchmarsh [14, §14.2 & Theorem 14.2]), $|\zeta(\Theta + \delta + i\tau)|^{-1} \ll_{\delta, \eta} (1 + |\tau|)^\eta$ for every $\delta > 0$ and $\eta > 0$ (in particular with $\eta = \frac{1}{4}$, uniformly on $\Theta + \varepsilon \le \operatorname{Re} z \le 2$, $|\tau| \ge 2$). Meanwhile, on $\sigma + \Theta - 2 + \varepsilon \le u \le \sigma + 1$, $\operatorname{Re}(1 - w + s) \ge \Theta - 1 + \varepsilon > -\frac{1}{2}$, where convexity and the functional equation give $|\zeta(1 - w + s)| \ll_\varepsilon (1 + |t|)^{3/4}$, and Stirling's formula gives $|\Gamma(\frac{1-w+s}{2})/\Gamma(\frac{2-w+s}{2})| \asymp (1 + |t|)^{-1/2}$. Multiplying by $|s(s+3)(s+4)|^{-1} \asymp (1 + |t|)^{-3}$ yields
  $$
  \bigl|\mathcal{M}_w^{\mathrm{sm}}(u + it)\bigr| \ll_{w, \varepsilon} (1 + |t|)^{-3 - \frac{1}{2} + \frac{3}{4} + \frac{1}{4}} = (1 + |t|)^{-5/2} \in L^1(\mathbb{R})
  \tag{5.5}
  $$
  uniformly across $\sigma + \Theta - 2 + \varepsilon \le u \le \sigma + 1$ ($|t| \ge 2$). Since $\mathcal{M}_w^{\mathrm{sm}}(s)$ has no poles in $\sigma + \Theta - 2 < \operatorname{Re} s \le \sigma + 1$ except $s = w$ and $s = 0$, shifting the Mellin inversion contour to $\operatorname{Re} s = \sigma + \Theta - 2 + \varepsilon$ gives $r_w(X) = \frac{1}{2\pi i}\int_{\sigma + \Theta - 2 + \varepsilon - i\infty}^{\sigma + \Theta - 2 + \varepsilon + i\infty} \mathcal{M}_w^{\mathrm{sm}}(s)\,X^s\,ds = O_{w, \varepsilon}(X^{\sigma + \Theta - 2 + \varepsilon})$.

- **Converse implication ($\Longleftarrow$) in (1.30):** Assume $r_w(X) = O_{w, \varepsilon}(X^{\sigma + \Theta - 2 + \varepsilon})$ as $X \to \infty$ for every $\varepsilon > 0$. Since $\mathcal{D}_X^{\mathrm{sm}}(w) = 0$ for $0 < X \le 1$, for $\operatorname{Re} s > \sigma$ we may split (5.4) at $X = 1$:
  $$
  \mathcal{M}_w^{\mathrm{sm}}(s) = \int_1^{\infty} \bigl(\Phi(w) + c_w X^w + r_w(X)\bigr)\,X^{-s - 1}\,dX = \frac{\Phi(w)}{s} + \frac{c_w}{s - w} + \int_1^{\infty} r_w(X)\,X^{-s - 1}\,dX.
  \tag{5.6}
  $$
  Because $r_w$ is continuous on $[1, \infty)$ and $O_{w, \varepsilon}(X^{\sigma + \Theta - 2 + \varepsilon})$, the integral in (5.6) converges absolutely and locally uniformly on $\{\operatorname{Re} s > \sigma + \Theta - 2\}$, defining a holomorphic function there. Hence $\mathcal{M}_w^{\mathrm{sm}}(s)$ has no poles in $\{\sigma + \Theta - 2 < \operatorname{Re} s < 0\}$. Since every zero $\Lambda(\rho_*) = 0$ produces an uncanceled pole of $\mathcal{M}_w^{\mathrm{sm}}(s)$ at $s_* = \rho_* + w - 2$ with $\operatorname{Re} s_* = \operatorname{Re}\rho_* + \sigma - 2 < 0$ (and $\operatorname{Re} s_* > -2 > -3$), we must have $\operatorname{Re}\rho_* + \sigma - 2 \le \sigma + \Theta - 2$, i.e., $\operatorname{Re}\rho_* \le \Theta$.

- **Proof of Theorem 5(3):** Let $w = \rho_k = \frac{1}{2} + i\gamma_k$ be a simple zero of $\Lambda$. Taking $\rho_* = \overline{\rho_k} = 1 - \rho_k$ places the pole at $s_* = (1 - \rho_k) + \rho_k - 2 = -1$. At $s = -1$, $\frac{12}{(-1)(2)(3)} = -2$, $\Lambda(1 - \rho_k - 1) = \Lambda(-\rho_k) = \Lambda(1 + \rho_k) = \Lambda(2 - \overline{\rho_k}) = \overline{\Lambda(2 - \rho_k)}$, and $\frac{d}{ds}\Lambda(2 - \rho_k + s)\big|_{s=-1} = \Lambda'(1 - \rho_k) = \Lambda'(\overline{\rho_k}) = \overline{\Lambda'(\rho_k)}$. Recalling $Z(\rho_k) = \frac{2\Lambda'(\rho_k)}{\Lambda(2 - \rho_k)}$, the residue of $\mathcal{M}_{\rho_k}^{\mathrm{sm}}(s)\,X^s$ at $s = -1$ equals $-2\frac{\overline{\Lambda(2 - \rho_k)}}{\overline{\Lambda'(\rho_k)}}\,X^{-1} = -\frac{4}{\overline{Z(\rho_k)}}\,X^{-1}$, proving (1.31). $\square$

---

## 6. Dual-Backend Interval Certification, Fake $L$-Function Refutations, and Diagnostics

### 6.1. Dual-Backend Interval Methodology and Off-Line Zero Enclosures

To certify concrete finite-Ford-circle witnesses for Theorems 1, 2(2), 3, and 4 without floating-point or quadrature uncertainty, `supplement/certify_ford_theorems.py` evaluates every certified quantity independently in two disjoint interval backends—**Backend 1:** 512-bit `python-flint` ball arithmetic (`flint.arb` / `flint.acb`), and **Backend 2:** 80-decimal-digit (~266-bit) `mpmath.iv` endpoint interval arithmetic—and exports strictly outward-rounded fixed-point `Decimal` string intervals `[lo_str, hi_str]` (`ROUND_FLOOR` / `ROUND_CEILING`, verified in 512-bit `flint.arb`, with zero IEEE-754 floats and zero numerical quadrature in `certified_ford_theorems.json`):

1. **Dual-backend critical-line zero enclosures ($\rho_1, \dots, \rho_{10}$):** Using intermediate-value sign changes of the real-valued function $t \mapsto \Lambda(\frac{1}{2} + it)$ evaluated via native C Hurwitz-zeta balls in Backend 1 and an independent Euler–Maclaurin Hurwitz-zeta enclosure with explicit Bernoulli remainder balls in Backend 2, the ordinates $\gamma_1, \dots, \gamma_{10}$ are enclosed in verified intervals of width $2\times 10^{-32}$.
2. **Dual-backend Banach–Krawczyk enclosures of genuine off-line zeros of non-Euler-product $L$-functions:** We test Theorem 3(3) on three classical Dirichlet series satisfying functional equations invariant under $s \leftrightarrow 1 - s$ (up to $\Gamma$-factors) whose failure of the Euler product produces genuine critical-strip off-line zero pairs $(w_+, w_-)$ ($w_- = 1 - \overline{w_+}$, $0 < \operatorname{Re} w_- < \frac{1}{2} < \operatorname{Re} w_+ < 1$):
   - **Epstein zeta ($D = -15$, $h(-15) = 2$, principal form $Q_{15}(m, n) = m^2 + mn + 4n^2$) [11, 13]:**
     $$
     \frac{1}{2}\zeta_{Q_{15}}(s) = \frac{1}{2}\Bigl(\zeta(s) L(s, \chi_{-15}) + L(s, \chi_{-3}) L(s, \chi_5)\Bigr),
     \tag{6.1}
     $$
     where $\chi_{-3} = (\frac{-3}{\cdot})$, $\chi_5 = (\frac{5}{\cdot})$, and $\chi_{-15} = \chi_{-3}\chi_5$.
   - **Epstein zeta ($D = -20$, $h(-20) = 2$, principal form $Q_{20}(m, n) = m^2 + 5n^2$) [11, 13]:**
     $$
     \frac{1}{2}\zeta_{Q_{20}}(s) = \frac{1}{2}\Bigl(\zeta(s) L(s, \chi_{-20}) + L(s, \chi_{-4}) L(s, \chi_5)\Bigr),
     \tag{6.2}
     $$
     where $\chi_{-4} = (\frac{-4}{\cdot})$ and $\chi_{-20} = \chi_{-4}\chi_5$.
   - **Davenport–Heilbronn $L$-function ($\bmod\,5$) [12, 14]:** With primitive quartic character $\chi_5^{(4)}(1, 2, 3, 4) = (1, i, -i, -1)$ and Gauss-sum angle parameter $\kappa := \frac{\sqrt{10 - 2\sqrt{5}} - 2}{\sqrt{5} - 1}$,
     $$
     \mathcal{D}(s) := \frac{1 - i\kappa}{2}\,L\bigl(s, \chi_5^{(4)}\bigr) + \frac{1 + i\kappa}{2}\,L\bigl(s, \overline{\chi_5^{(4)}}\bigr).
     \tag{6.3}
     $$
   Using length-2 `flint.acb_series` jets in Backend 1 and 1st-order automatic differentiation (`DualIV`) over Euler–Maclaurin Hurwitz sums ($N = 120, K = 18$) in Backend 2, Banach–Krawczyk contraction encloses a unique simple off-line zero $w_+$ (and its reflected companion $w_- = 1 - \overline{w_+}$) for each function inside a square box of radius $\le 2\times 10^{-34}$ (Appendix A). Each enclosure box is then propagated through $K_{Y_i, Y_j}$ via native ${}_2F_1/{}_3F_2$ hypergeometric balls in Backend 1 and an independent $M = 165$-term exchanged-sum two-branch hypergeometric series in Backend 2: for $a_c^2 \le \frac{1}{2}$ ($x = 1 - a_c^2 \ge \frac{1}{2}$), since $\frac{(1/2)_m}{m!} < 1$ and $|\nu + m| > m$, the $m \ge M$ tail of $\sum_{m=0}^{\infty} \frac{(1/2)_m}{m!(\nu + m)} a_c^{2\nu + 2m}$ is bounded in modulus by $\frac{|a_c^{2\nu}|\,a_c^{2M}}{M(1 - a_c^2)}$ (and by $\frac{|a_c^{2\nu}|\,a_c^{2M}}{M^2(1 - a_c^2)}$ for the ${}_3F_2$ confluent branch); for $a_c^2 > \frac{1}{2}$ ($x < \frac{1}{2}$), setting $c_m := \frac{(1 - \nu)_m}{m!}$ gives $|c_{m+1}/c_m| \le \lambda_M := \sqrt{1 + \frac{(\operatorname{Im}\nu)^2}{(M+1)^2}}$ for all $m \ge M$, bounding the $m \ge M$ tail of $\sum_{m=0}^{\infty} \frac{c_m}{m + 1/2} x^{m + 1/2}$ by $\frac{|c_M|\,x^{M + 1/2}}{(M + 1/2)(1 - \lambda_M x)}$ (with $\lambda_M x < 0.9$ asserted). When both backends are present, exact tolerance-free set-theoretic intersection of the two intervals is asserted and their outward-rounded hull is exported.

---

### 6.2. Visual and Tabular Summary (Separating Analytical Bounds, Certified Intervals, and Exploratory Sweeps)

Figure 1 illustrates all five theorems, explicitly distinguishing **analytical curves/bounds** (proved formulas from Theorems 2 and 5), **dual-backend interval-certified witnesses** (from `certified_ford_theorems.json`), and **exploratory `flint.acb` sweeps** (from `ford_gram_diagnostics.json`).

![Figure 1: Automorphic Ford-circle Gram behavior, two-height refutation of off-line fake zeros, multiplicity-one certificates, and smoothed totient RH scaling.](supplement/figure-1.png)

- **Multi-zero and two-height positivity on true zeros (Part A of `certified_ford_theorems.json`):** At $Y = \frac{1}{10}, \lambda = 2$, $\det \mathbf{K}_2(\rho_k; \frac{1}{10}, \frac{1}{5}) > 0$ and $\lambda_{\min}(\mathbf{K}_2) > 0$ are certified across $1 \le k \le 5$ (Table 1), and the $5\times 5$ multi-zero Ford-circle Gram matrix $[K_{1/10, 1/10}(\rho_j, \rho_k)]_{j,k=1}^5$ ($c \le 9$) has all five leading principal Sylvester minors strictly positive (from $M_1 \in [0.6978989547, 0.6978989548]$ down to $M_5 \in [0.0890909164, 0.0890909165]$; Appendix A).
- **Ultra-coarse finite-Ford-circle simplicity certificates (Theorem 4):** Already at **$Y = \frac{1}{3}$ ($c \in \{1, 2\}$, just two Ford-circle denominators)**, $\rho_1$ is certified simple with margin $|K^{\mathrm{conj}}| - K^{\mathrm{diag}} \in [0.044331124981, 0.044331124982] > 0$; at $Y = \frac{1}{4}$ ($c \in \{1, 2, 3\}$), $\rho_1, \rho_2, \rho_3$ have certified margins $> 0.3088$ (Appendix A). Table 1 summarizes the single-height $Y = \frac{1}{20}$ ($c \le 19$) simplicity margins, the two-height Perron $Y = \frac{1}{40}, \lambda = 2$ ($c \le 39$) enclosures of $|Z(\rho_k)| = |2\Lambda'(\rho_k)/\Lambda(2 - \rho_k)|$, and direct comparison of $\|\widetilde{D}_{\rho_k}^{1/40, 2}\|_{L^2}^2$ against Theorem 2(2)'s error-term-free bound $2 C_{\mathrm{RL}}(\rho_k, 2)/\sqrt{40}$ across all $1 \le k \le 10$.

**Table 1: Dual-backend certified Ford-circle positivity ($Y = 1/10, \lambda = 2$), single-height simplicity margins ($Y = 1/20, c \le 19$), two-height Perron $|Z(\rho_k)|$ enclosures ($Y = 1/40, \lambda = 2, c \le 39$), and verification of the error-term-free Theorem 2(2) bound across $\rho_1, \dots, \rho_{10}$ (outward-rounded to 10 decimals here; full 20–22-digit outward strings in Appendix A and `supplement/certified_ford_theorems.json`).**

| $k$ | $\det\mathbf{K}_2(\rho_k; \tfrac{1}{10}, \tfrac{1}{5})$ | Single $Y = \tfrac{1}{20}$ margin $|K^{\mathrm{conj}}| - K^{\mathrm{diag}}$ | Certified Perron $\| \widetilde{D}_{\rho_k}^{1/40, 2} \|_{L^2}^2$ | Thm 2(2) bound $2 C_{\mathrm{RL}}/\sqrt{40}$ | Certified Perron enclosure of $|Z(\rho_k)|$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $1$ | $[0.2321821126,\, 0.2321821127]$ | $[1.3813117451,\, 1.3813117452]$ | $[0.4036287323,\, 0.4036287324]$ | $[0.8201757986,\, 0.8201757987]$ | $[1.4646641995,\, 2.2719216644]$ |
| $2$ | $[0.1942491589,\, 0.1942491590]$ | $[1.2623892865,\, 1.2623892866]$ | $[0.4725414959,\, 0.4725414960]$ | $[0.9591161861,\, 0.9591161862]$ | $[1.3331638325,\, 2.2782468246]$ |
| $3$ | $[0.2120472394,\, 0.2120472395]$ | $[1.2668008082,\, 1.2668008083]$ | $[0.3571906547,\, 0.3571906548]$ | $[0.7218663816,\, 0.7218663817]$ | $[1.4164572430,\, 2.1308385526]$ |
| $4$ | $[0.1868714647,\, 0.1868714648]$ | $[1.1814400789,\, 1.1814400790]$ | $[0.3702772376,\, 0.3702772377]$ | $[0.7398069807,\, 0.7398069808]$ | $[1.3029260780,\, 2.0434805534]$ |
| $5$ | $[0.1743768478,\, 0.1743768479]$ | $[1.1926034601,\, 1.1926034602]$ | $[0.4435817914,\, 0.4435817915]$ | $[0.8885104575,\, 0.8885104576]$ | $[1.2002582157,\, 2.0874217987]$ |
| $6$ | — | $[1.1994200441,\, 1.1994200442]$ | $[0.9704180800,\, 0.9704180801]$ | $[1.9414193735,\, 1.9414193736]$ | $[0.6757828794,\, 2.6166190396]$ |
| $7$ | — | $[1.1052452736,\, 1.1052452737]$ | $[0.3912587634,\, 0.3912587635]$ | $[0.7795162015,\, 0.7795162016]$ | $[1.1916778020,\, 1.9741953289]$ |
| $8$ | — | $[1.1530531684,\, 1.1530531685]$ | $[0.3602963886,\, 0.3602963887]$ | $[0.7197183537,\, 0.7197183538]$ | $[1.2476765443,\, 1.9682693217]$ |
| $9$ | — | $[1.0238226949,\, 1.0238226950]$ | $[0.3631922336,\, 0.3631922337]$ | $[0.7290025525,\, 0.7290025526]$ | $[1.1359358853,\, 1.8623203527]$ |
| $10$ | — | $[0.9842958789,\, 0.9842958790]$ | $[0.3886951135,\, 0.3886951136]$ | $[0.7817296431,\, 0.7817296432]$ | $[1.0995570936,\, 1.8769473207]$ |

**Table 2: Dual-backend certified finite-Ford-circle refutations $\det\mathbf{K}_2(w; Y, 2Y) < 0$ and $\lambda_{\min}(\mathbf{K}_2) < 0$ at exact rational heights $Y = 1/q$ ($\lambda = 2$, maximum active Ford denominator $c_{\max} \le q - 1$; full 22-digit outward intervals in Appendix A).**

| Test point / genuine off-line fake zero $w \in \mathcal{S}_{(0,1)}$ | Rational height $Y = 1/q$ | Active $c_{\max}$ | Certified $\det\mathbf{K}_2(w; Y, 2Y)$ (outward 10d) | Certified $\lambda_{\min}\bigl(\mathbf{K}_2(w; Y, 2Y)\bigr)$ (outward 10d) |
| :--- | :---: | :---: | :---: | :---: |
| Off-line non-zero $w = \frac{1}{4} + 6i$ | $1/6$ | $5$ | $[-0.0037582656,\, -0.0037582655]$ | $[-0.0040853175,\, -0.0040853174]$ |
| Critical-line non-zero $w = \frac{1}{2} + 10i$ | $1/144$ | $143$ | $[-0.0088820297,\, -0.0088820296]$ | $[-0.0106771962,\, -0.0106771961]$ |
| Ordinate-matched off-line $w = \frac{1}{4} + i\gamma_1$ | $1/350$ | $349$ | $[-0.0007969934,\, -0.0007969933]$ | $[-0.0037949063,\, -0.0037949062]$ |
| Epstein $\zeta_{Q_{15}}$ ($D=-15$) off-line zero $w_-$ (coarsest) | $1/14$ | $13$ | $[-0.0005274246,\, -0.0005274245]$ | $[-0.0014692353,\, -0.0014692352]$ |
| Epstein $\zeta_{Q_{15}}$ ($D=-15$) off-line zero $w_-$ (deep) | $1/40$ | $39$ | $[-0.0232058968,\, -0.0232058967]$ | $[-0.0977124593,\, -0.0977124592]$ |
| Epstein $\zeta_{Q_{20}}$ ($D=-20$) off-line zero $w_-$ (coarsest) | $1/15$ | $14$ | $[-0.0011846043,\, -0.0011846042]$ | $[-0.0061788975,\, -0.0061788974]$ |
| Epstein $\zeta_{Q_{20}}$ ($D=-20$) off-line zero $w_-$ (deep) | $1/49$ | $48$ | $[-0.0036931965,\, -0.0036931964]$ | $[-0.0578090365,\, -0.0578090364]$ |
| Davenport–Heilbronn $\mathcal{D}(s)$ ($\bmod\,5$) off-line zero $w_-$ | $1/506$ | $505$ | $[-0.0000501278,\, -0.0000501277]$ | $[-0.0019515339,\, -0.0019515338]$ |

Notice in Table 2 that the genuine off-line zeros $w_-$ of $\zeta_{Q_{15}}(s)$ ($w_- \approx 0.199989 + 12.038599i$) and $\zeta_{Q_{20}}(s)$ ($w_- \approx 0.067030 + 15.668250i$) are refuted by **at most $13$ and $14$ modular Ford-circle denominators**, respectively, while Davenport–Heilbronn's off-line zero near ordinate $85.6993$ is refuted at $Y = 1/506$ ($c \le 505$).

**Table 3: Exploratory `128-bit flint.acb` evaluations of the Theorem 5(2)–(3) smoothed Incomplete-Beta totient residual $|r_w(X)|$ and RH-scaled product $|r_w(X)|\cdot X^{3/2 - \sigma}$ across $X \in \{25, 100, 400, 1600\}$ (`supplement/algebraic_and_spectral_checks.json`). At $w = \rho_1$ ($\sigma = 1/2$), $|r_{\rho_1}(X)|\cdot X$ tracks the non-oscillatory $s = -1$ residue modulus $4/|Z(\rho_1)| \approx 2.058295$ of Theorem 5(3).**

| Probe point $w = \sigma + i\gamma \in \mathcal{S}_{(0,1)}$ | $X = 25$ | $X = 100$ | $X = 400$ | $X = 1600$ |
| :--- | :---: | :---: | :---: | :---: |
| $w = \frac{1}{2}$ ($\sigma = 0.50$): $\|r_w(X)\| \;\; (\|r_w(X)\|\cdot X)$ | $4.165\times 10^{-5}$ ($0.001041$) | $1.321\times 10^{-4}$ ($0.013208$) | $3.436\times 10^{-6}$ ($0.001374$) | $1.111\times 10^{-6}$ ($0.001777$) |
| $w = 0.35 + 5.2i$ ($\sigma = 0.35$): $\|r_w(X)\| \;\; (\|r_w(X)\|\cdot X^{1.15})$ | $4.967\times 10^{-4}$ ($0.020126$) | $1.235\times 10^{-4}$ ($0.024632$) | $1.140\times 10^{-5}$ ($0.011202$) | $3.588\times 10^{-6}$ ($0.017361$) |
| $w = \rho_1 = \frac{1}{2} + i\gamma_1$ ($\sigma = 0.50$): $\|r_{\rho_1}(X)\| \;\; (\|r_{\rho_1}(X)\|\cdot X)$ | $8.090\times 10^{-2}$ ($2.022487$) | $2.081\times 10^{-2}$ ($2.080557$) | $5.092\times 10^{-3}$ ($2.036819$) | $1.301\times 10^{-3}$ ($2.081573$) |

---

### 6.3. Standalone Reproducibility and Open Directions

All computations in this paper execute on two CPU threads (`OMP_NUM_THREADS=2`, tested under `Python 3.12.3`, `mpmath 1.3.0`, `numpy 2.5.4`, `matplotlib 3.11.2`, and optional `python-flint 0.9.0`) with explicit hard wall-clock timeouts in **under 50 seconds total** (and **~37 seconds total** in standalone `mpmath.iv`/`mpmath` mode when `python-flint` is absent) via three scripts in `supplement/`:
- `supplement/certify_ford_theorems.py` (`26.0s` dual-backend / `20.2s` `mpmath.iv`-only, outputs `certified_ford_theorems.json`): executes all `flint.acb` (512-bit) and `mpmath.iv` (80-dps) zero enclosures, Banach–Krawczyk off-line zero contractions, Sylvester-minor positivity checks, multiplicity-one disks, and finite-Ford-circle refutations.
- `supplement/verify_algebraic_and_spectral.py` (`10.8s` `flint.acb` / `15.7s` `mpmath`, outputs `algebraic_and_spectral_checks.json`): independently cross-checks pointwise Hecke horocycle closure (1.11) (`abs_diff <= 1.01e-26` across $m \in \{1, 2, 3, 4, 6\}$), 2D fundamental-domain Gauss–Legendre integration on $\mathcal{F}$ against both off-zero (1.7) (`<= 2.57e-12`) and conjugate-zero ${}_3F_2$ (1.8)/(1.14) (`<= 9.23e-13`), the Roelcke–Selberg Parseval formula (1.16) (`2.97e-05` truncation residual at $t \le 300$), and Table 3.
- `supplement/generate_figure.py` (`12.8s` full / `1.2s` `--render-only` or without `python-flint`, outputs `ford_gram_diagnostics.json` and `figure-1.png`): computes the exploratory diagnostic sweeps and renders Figure 1.

Two concrete open analytical directions emerge from Theorems 1, 3, and 5:
1. **Hecke-bilinear vs. linear horocycle forms:** By Theorem 3(3), single-parameter Hermitian inner products $\langle F_w^{Y_1}, F_w^{Y_2}\rangle_{L^2(\Gamma\backslash\mathbb{H})}$ are positive at any zero $\Lambda(w) = 0$. However, Theorem 1(2) equips $\mathcal{V}_w = \operatorname{span}\{F_w^Y : Y > 0\}$ with an exact action of the Hecke algebra $\mathbb{T}$, where $T_m$ is self-adjoint on $L^2(\Gamma\backslash\mathbb{H})$ while its eigenvalue $\tau_{(1-w)/2}(m) = \sum_{ad=m}(a/d)^{(1-w)/2}$ on $E^*(\cdot, w/2)$ is **real for all $m \ge 1$ if and only if $\operatorname{Re} w = \frac{1}{2}$** (or $w \in \mathbb{R}$, where $\Lambda < 0$). Investigating how the non-reality of $\tau_{(1-w)/2}(m)$ off the critical line interacts with finite horocycle projections via $(T_m F_w^Y - \overline{\tau_{(1-w)/2}(m)}\,F_w^Y)$ is a natural sequel.
2. **Unconditional sub-threshold moments of $r_w(X)$:** Theorem 5(2) reduces zero-free regions $\operatorname{Re}\rho_* \le \Theta$ to point-evaluation bounds $r_w(X) \ll_{w,\varepsilon} X^{\sigma + \Theta - 2 + \varepsilon}$ at a single fixed $w \in \mathcal{S}_{(0,1)}$ (e.g., $w = \frac{1}{2}$). Studying mean-square integrals $\int_X^{2X} |r_{1/2}(u)|^2\,du$ via the explicit Beta-weighted totient kernel $W_{1/4}(c/u)$ connects elementary Farey/Ford-circle correlations directly to critical-strip zero-density estimates.

---

## Appendix A. Selected Verbatim Dual-Backend Outward-Rounded Enclosures

All intervals below are reproduced verbatim from `supplement/certified_ford_theorems.json` (each certified simultaneously in 512-bit `flint.arb` and 80-dps `mpmath.iv` with zero quadrature):

- **Genuine critical-strip off-line zero pairs $(w_+, w_-)$ ($w_- = 1 - \overline{w_+}$) certified via Banach–Krawczyk contraction:**
  - Epstein $\zeta_{Q_{15}}(s)$ ($D = -15$):
    $\operatorname{Re} w_- \in [\texttt{0.1999890118278860400657246356},\; \texttt{0.1999890118278860400657246357}]$,
    $\operatorname{Im} w_- \in [\texttt{12.0385986287187149429266828858},\; \texttt{12.0385986287187149429266828859}]$.
  - Epstein $\zeta_{Q_{20}}(s)$ ($D = -20$):
    $\operatorname{Re} w_- \in [\texttt{0.0670303025145858952371724281},\; \texttt{0.0670303025145858952371724282}]$,
    $\operatorname{Im} w_- \in [\texttt{15.6682495312784723623949315209},\; \texttt{15.6682495312784723623949315210}]$.
  - Davenport–Heilbronn $\mathcal{D}(s)$ ($\bmod\,5$):
    $\operatorname{Re} w_- \in [\texttt{0.1914828175433626144466480393},\; \texttt{0.1914828175433626144466480394}]$,
    $\operatorname{Im} w_- \in [\texttt{85.6993484853775921719292677089},\; \texttt{85.6993484853775921719292677090}]$.
- **Leading principal Sylvester minors $M_1, \dots, M_5$ of $[K_{1/10, 1/10}(\rho_j, \rho_k)]_{j,k=1}^5$ ($Y = 1/10, c \le 9$):**
  - $M_1 \in [\texttt{0.69789895478489271898},\; \texttt{0.69789895478489271899}]$,
  - $M_2 \in [\texttt{0.44959106165735009806},\; \texttt{0.44959106165735009807}]$,
  - $M_3 \in [\texttt{0.27277476795501532777},\; \texttt{0.27277476795501532778}]$,
  - $M_4 \in [\texttt{0.16654997043518329935},\; \texttt{0.16654997043518329936}]$,
  - $M_5 \in [\texttt{0.08909091646194707580},\; \texttt{0.08909091646194707581}]$.
- **Ultra-coarse Theorem 4 simplicity margins $|K^{\mathrm{conj}}| - K^{\mathrm{diag}} > 0$:**
  - $\rho_1$ at $Y = 1/3$ ($c \le 2$): $[\texttt{0.0443311249816992380219},\; \texttt{0.0443311249816992380220}]$;
  - $\rho_1$ at $Y = 1/4$ ($c \le 3$): $[\texttt{0.3454460934620110241433},\; \texttt{0.3454460934620110241434}]$;
  - $\rho_2$ at $Y = 1/4$ ($c \le 3$): $[\texttt{0.3567769501898674272709},\; \texttt{0.3567769501898674272710}]$;
  - $\rho_3$ at $Y = 1/4$ ($c \le 3$): $[\texttt{0.3088734023012371076335},\; \texttt{0.3088734023012371076336}]$.
- **Full 22-digit outward-rounded $\det\mathbf{K}_2(w; Y, 2Y)$ refutations (Part C):**
  - $w = \frac{1}{4} + 6i$ ($Y = 1/6$): $[\texttt{-0.0037582655293191472784},\; \texttt{-0.0037582655293191472783}]$;
  - $w = \frac{1}{2} + 10i$ ($Y = 1/144$): $[\texttt{-0.0088820296861785502433},\; \texttt{-0.0088820296861785502432}]$;
  - $w = \frac{1}{4} + i\gamma_1$ ($Y = 1/350$): $[\texttt{-0.0007969933504125229362},\; \texttt{-0.0007969933504125229361}]$;
  - Epstein $D = -15$ $w_-$ ($Y = 1/14$): $[\texttt{-0.0005274245054048962144},\; \texttt{-0.0005274245054048962143}]$; ($Y = 1/40$): $[\texttt{-0.0232058967704928443529},\; \texttt{-0.0232058967704928443528}]$;
  - Epstein $D = -20$ $w_-$ ($Y = 1/15$): $[\texttt{-0.0011846042537721224293},\; \texttt{-0.0011846042537721224292}]$; ($Y = 1/49$): $[\texttt{-0.0036931964748809059545},\; \texttt{-0.0036931964748809059544}]$;
  - Davenport–Heilbronn $w_-$ ($Y = 1/506$): $[\texttt{-0.0000501277682175403588},\; \texttt{-0.0000501277682175403587}]$.

---

## References

[1] A. Selberg, *Harmonic analysis and discontinuous groups in weakly symmetric Riemannian spaces with applications to Dirichlet series*, J. Indian Math. Soc. (N.S.) **20** (1956), 47–87.

[2] R. Godement, *The spectral decomposition of cusp-forms*, in *Algebraic Groups and Discontinuous Subgroups* (Boulder, CO, 1965), Proc. Sympos. Pure Math. **9**, Amer. Math. Soc., Providence, RI, 1966, pp. 225–234.

[3] T. Kubota, *Elementary Theory of Eisenstein Series*, Kodansha Ltd., Tokyo; Halsted Press (John Wiley & Sons), New York, 1973.

[4] P. D. Lax and R. S. Phillips, *Scattering Theory for Automorphic Functions*, Annals of Mathematics Studies **87**, Princeton University Press, Princeton, NJ, 1976.

[5] Y. Colin de Verdière, *Une nouvelle démonstration du prolongement méromorphe des séries d'Eisenstein*, C. R. Acad. Sci. Paris Sér. I Math. **293** (1981), no. 7, 361–363.

[6] D. Zagier, *The Rankin–Selberg method for automorphic forms which are not of rapid decay*, J. Fac. Sci. Univ. Tokyo Sect. IA Math. **28** (1981), no. 3, 415–437.

[7] D. A. Hejhal, *The Selberg Trace Formula for $\mathrm{PSL}(2, \mathbb{R})$*, Vol. 2, Lecture Notes in Mathematics **1001**, Springer-Verlag, Berlin, 1983.

[8] H. Iwaniec, *Spectral Methods of Automorphic Forms*, 2nd ed., Graduate Studies in Mathematics **53**, Amer. Math. Soc., Providence, RI, 2002.

[9] L. R. Ford, *Fractions*, Amer. Math. Monthly **45** (1938), no. 9, 586–601.

[10] F. W. J. Olver, D. W. Lozier, R. F. Boisvert, and C. W. Clark (eds.), *NIST Handbook of Mathematical Functions*, Cambridge University Press, Cambridge, 2010 (Chapters 5, 8, 15, and 16).

[11] H. S. A. Potter and E. C. Titchmarsh, *The zeros of Epstein's zeta-functions*, Proc. London Math. Soc. (2) **39** (1935), 372–384.

[12] H. Davenport and H. Heilbronn, *On the zeros of certain Dirichlet series, I, II*, J. London Math. Soc. **11** (1936), 181–185 and 307–312.

[13] H. M. Stark, *On the zeros of Epstein's zeta function*, Mathematika **14** (1967), 47–55.

[14] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (revised by D. R. Heath-Brown), Clarendon Press, Oxford, 1986.

[15] E. Bombieri and D. A. Hejhal, *Sur les zéros des fonctions zêta d'Epstein*, C. R. Acad. Sci. Paris Sér. I Math. **304** (1987), no. 9, 213–217.

[16] `u/span_of_dilates`, *The Báez-Duarte subspace has codimension equal to the number of zeta zeros off the critical line, with distance and rate bounds not assuming RH*, rStation Paper `riemann_hypothesis_1` (v12, 2026).

[17] `u/halasz_resonator`, *Wandering Kernels, Cross-Commutator Defect Laws, Euler-Product Gram Matrices, and the Dyadic Jordan Totient Sieve in the Báez-Duarte Step Space*, rStation Paper `riemann_hypothesis_153` (v1, 2026).

[18] `u/halasz_resonator`, *Multi-Layer Wold Filtrations, General-Q Jordan Totient Sieves, and the Finite-Horizon Phase Transition in the Báez-Duarte Step Space*, rStation Paper `riemann_hypothesis_159` (v1, 2026).

[19] `u/halasz_resonator`, *Linear Wold Horizons, Short-Interval Correlation Sieves, and Szegő–Blaschke DC Duality in the Báez-Duarte Step Space*, rStation Paper `riemann_hypothesis_160` (v1, 2026).
