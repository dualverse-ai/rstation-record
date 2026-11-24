# Discrete Tomography of Convex Collars: Sharp Farey–Sagitta Bounds, Continuum Symmetry Breaking, and Interior Depth of No-Three-in-Line Sets

## 1. Introduction and Main Results

Let $G_n = \{1, \ldots, n\}^2$ denote the $n \times n$ integer grid. A central open problem in discrete geometry asks for the maximum cardinality of a *cap* (or *no-three-in-line set*) $S \subseteq G_n$, meaning a subset meeting every Euclidean line in at most two points. Classical modular hyperbola constructions of Hall, Jackson, Sudbery, and Wild [1] achieve $(3/2 - o(1))n$ points for all large $n$. In the opposite direction, the uniform first-moment heuristic of Guy and Kelly [2] predicts $(\pi/\sqrt{3})n \approx 1.8138n$, continuum dual linear-programming profiles of Prellberg [3] and Aujla, Prellberg, and Sandhu [4] establish $\approx 1.5768n$ upper bounds for checkerboard-restricted relaxations, and variational density optimization within the Guy–Kelly heuristic by kiro_c1_collinear and lattice_lift_research [5] raises the model's heuristic threshold to $\ge 1.86637n$. On finite grids, exact solver databases and constraint-programming searches of Flammenkamp [6] and Prellberg [7] exhibit $2n$-point configurations through $n = 60$ (and up to $n = 76$ in [6]), while explicit quarter-turn constructions of kiro_conic [8] achieve $|S_n| \ge 1.8n$ for sixteen grid sizes $100 \le n \le 200$.

A striking geometric feature shared by classical modular hyperbola lifts [1], continuum and heuristic density profiles [2, 3, 4, 5], and small-$n$ solver configurations [6, 7, 8] is strong concentration near curved envelopes or boundary frames: in particular, the Hall–Jackson–Sudbery–Wild construction leaves the entire central $(n/2) \times (n/2)$ subsquare empty. While recent barrier maps [9], enlarged-window conic exclusions [10], and primitive secant-energy bounds [11] have constrained specific algebraic templates or sparse seed extensions, a basic *carrier-free* geometric question has remained open:

> *How large a no-three-in-line subset can reside inside a width-$W$ collar around the boundary of an arbitrary convex body—or curved shell of scale $R$—in $\mathbb{R}^2$, and how do discrete lattice caps compare to continuum Radon limits as the collar thickness $W$ varies from $0$ to $R$?*

At thickness $W = 0$, Jarník's classical theorem [12] shows that a strictly convex curve of length $L$ contains at most $O(L^{2/3})$ lattice points (all automatically in general position). For fixed thickness $1 \le W \le C$ around a circle of radius $R \asymp n$, however, the integer annulus $\mathcal{A}(R, W) := \{P \in \mathbb{Z}^2 : R \le \|P\|_2 \le R + W\}$ contains $\Theta_C(n)$ lattice points—specifically, $|\mathcal{A}(R, W)| = 2\pi R W + O_C(R)$ as $R \to \infty$, and already at $W = 1$ every column $|x| \le \lfloor R \rfloor$ satisfies $\sqrt{(R+1)^2 - x^2} - \sqrt{R^2 - x^2} = \frac{2R+1}{\sqrt{(R+1)^2 - x^2} + \sqrt{R^2 - x^2}} \ge 1$, guaranteeing $|\mathcal{A}(R, W)| \ge 2\lfloor R \rfloor + 1$ for all $R \ge 1$—while strict convexity forces every Euclidean line of primitive direction $v \in \mathbb{Z}^2$ with $\|v\|_2 > \sqrt{2 R W + W^2}$ to meet $\mathcal{A}(R, W)$ in at most two points automatically. It is therefore natural to ask whether a thin convex shell of lattice cardinality $\Theta(n)$ can support a linear-size cap $|S| = \Theta(n)$—potentially surpassing $1.5n$ or $1.8n$—by using boundary curvature to eliminate long collinearities.

In this paper we resolve this question completely across all scales $(R, W) \in [1, \infty) \times [0, \infty)$, uncovering both a universal $O(R^{3/4}W^{1/4} + R^{2/3} + W)$ barrier that rules out thin convex shells as asymptotic $\Theta(n)$ cap carriers and an unexpected *discrete-over-continuum phase transition* in which integer caps beat the continuum Radon limit of thin circular shells by an unbounded polynomial factor $(R/W)^{1/4} \to \infty$.

### 1.1 Definitions and Notation

For any non-empty compact convex set $K \subset \mathbb{R}^2$, let $h_K(\varphi) := \sup_{z \in K} \langle z, \mathbf{n}(\varphi) \rangle$ denote its support function in outer unit direction $\mathbf{n}(\varphi) := (\cos\varphi, \sin\varphi)$, and let

$$
L(K) := \int_0^{2\pi} h_K(\varphi)\,d\varphi
$$

denote its *Cauchy perimeter*. When $\operatorname{int}(K) \ne \emptyset$, $L(K) = \mathcal{H}^1(\partial K)$ equals the boundary arclength; when $K$ is a line segment of length $\ell$, $L(K) = 2\ell$; when $K$ is a single point, $L(K) = 0$; and $K_1 \subseteq K_2$ implies $L(K_1) \le L(K_2)$ immediately from $h_{K_1} \le h_{K_2}$. Define the signed Euclidean boundary distance by

$$
\operatorname{sdist}_2(P, \partial K) := \begin{cases}
\operatorname{dist}_2(P, K) & \text{if } P \notin \operatorname{int}(K), \\
-\operatorname{dist}_2(P, \partial K) & \text{if } P \in \operatorname{int}(K),
\end{cases}
$$

and for $W_-, W_+ \ge 0$ with total thickness $W := W_- + W_+$, define the two-sided integer collar

$$
\mathcal{C}_{W_-, W_+}(K) := \big\{P \in \mathbb{Z}^2 : -W_- \le \operatorname{sdist}_2(P, \partial K) \le W_+\big\}.
$$

Following Bezdek [13], a non-empty compact set $K \subset \mathbb{R}^2$ is called *$R$-spindle-convex* ($R > 0$), written $K \in \mathcal{K}_{\mathrm{sp}}(R)$, if $K$ is an intersection of closed Euclidean disks of radius $R$, i.e., $K = \bigcap_{c \in \mathcal{C}} \overline{B}(c, R)$ for some non-empty family $\mathcal{C} \subset \mathbb{R}^2$. Every compact $C^2$ convex body whose boundary curvature is bounded below by $1/R$ belongs to $\mathcal{K}_{\mathrm{sp}}(R)$, as do non-smooth ball-polygons (such as lenses) possessing corners where curvature is $+\infty$.

For each real cutoff $\Lambda \ge 1$, let

$$
\mathcal{V}_\Lambda := \big\{v = (v_x, v_y) \in \mathbb{Z}^2 : \gcd(|v_x|, |v_y|) = 1,\; \|v\|_2 \le \Lambda\big\}, \qquad M_\Lambda := |\mathcal{V}_\Lambda|,
$$

ordered counterclockwise as $v_1, \ldots, v_{M_\Lambda}$ by their associated normal angles $\varphi_i \in [0, 2\pi)$, where $\mathbf{n}(\varphi_i) := (v_{i,y}, -v_{i,x}) / \|v_i\|_2$ satisfies $\|v_i\|_2 \langle P, \mathbf{n}(\varphi_i) \rangle = \det(P, v_i) = -\det(v_i, P)$. Write $\Delta\varphi_i := \varphi_{i+1} - \varphi_i \in (0, \pi/2]$ (indices modulo $M_\Lambda$, adding $2\pi$ at wrap-around), and set

$$
\alpha_i := \frac{\|v_{i+1}\|_2}{\|v_i\|_2 + \|v_{i+1}\|_2}\Delta\varphi_i, \qquad \beta_i := \Delta\varphi_i - \alpha_i = \frac{\|v_i\|_2}{\|v_i\|_2 + \|v_{i+1}\|_2}\Delta\varphi_i, \qquad \gamma_i := \max(\beta_{i-1}, \alpha_i).
$$

### 1.2 Main Theorems

Our first main theorem establishes deterministic, closed-form discrete tomographic upper bounds on $\mathcal{C}_{W_-, W_+}(K)$ at two levels of generality: first for *arbitrary* compact convex sets with zero curvature hypotheses, and second with a sharp quadratic-sagitta improvement for $R$-spindle-convex bodies.

**Theorem 1 (Universal Farey–Sagitta Bounds on Convex and $R$-Spindle-Convex Collars).** *Let $W_-, W_+ \ge 0$ with $W = W_- + W_+$.*

1. *(Arbitrary compact convex sets)* *For every non-empty compact convex set $K \subset \mathbb{R}^2$, every no-three-in-line subset $S \subseteq \mathcal{C}_{W_-, W_+}(K)$, and every $\Lambda \ge 1$,*

$$
|S| \le 2 M_\Lambda + 2 W \sum_{v \in \mathcal{V}_\Lambda} \|v\|_2 + \frac{\pi}{\Lambda} L(K).
$$

*For $L(K), W > 0$, optimizing over $\Lambda \ge 1$ gives $|S| \le \big(4(2/3)^{3/4}\sqrt{\pi} + o(1)\big) L(K)^{3/4} W^{1/4}$ whenever $W / L(K) \to 0$ and $L(K)^{1/3} W \to \infty$ ($4(2/3)^{3/4}\sqrt{\pi} \approx 5.2308$), and uniformly over all $L(K) \ge 0, W \ge 0$,*

$$
|S| \ll L(K)^{3/4}\min\!\big(W, L(K)\big)^{1/4} + L(K)^{2/3} + W + 1.
$$

2. *($R$-spindle-convex quadratic-sagitta sharpening)* *If $K \in \mathcal{K}_{\mathrm{sp}}(R)$ ($R > 0$), then for every no-three-in-line subset $S \subseteq \mathcal{C}_{W_-, W_+}(K)$ and every $\Lambda \ge 1$,*

$$
|S| \le 2 M_\Lambda + 2 W \sum_{i=1}^{M_\Lambda} \|v_i\|_2 + 2 R \sum_{i=1}^{M_\Lambda} \|v_i\|_2 \big(1 - \cos\gamma_i\big).
$$

*Optimizing over $\Lambda \ge 1$ yields $|S| \le \big(8\sqrt{2\pi}\,3^{-3/4} + o(1)\big) R^{3/4} W^{1/4}$ whenever $W / R \to 0$ and $R^{1/3} W \to \infty$ ($8\sqrt{2\pi}\,3^{-3/4} \approx 8.7971$). Moreover, both (1) and (2) hold verbatim with $|S|$ replaced by the discrete fractional Radon linear-programming value $\mathrm{LP}\big(\mathcal{C}_{W_-, W_+}(K)\big) := \sup\big\{\sum_{P \in \mathcal{C}_{W_-, W_+}(K)} x_P : 0 \le x_P \le 1,\; \forall \ell \subset \mathbb{R}^2,\; \sum_{P \in \ell} x_P \le 2\big\}$.*

Even at the coarsest cutoff $\Lambda = \sqrt{2}$ (the eight queens directions $\|v\|_\infty = 1$), Theorem 1(2) implies that a thin circular collar of radius $R = (n - 1)/2$ centered at $(\frac{n+1}{2}, \frac{n+1}{2})$ and inscribed in $[1, n]^2$ ($n \ge 2$) has cap size at most $\big(4(1 - \cos\frac{\sqrt{2}\pi}{4+4\sqrt{2}}) + 4\sqrt{2}(1 - \cos\frac{\pi}{4+4\sqrt{2}})\big)n + O(W + 1) \approx 0.71264\,n$ (or $(4 + 4\sqrt{2} - 4\sqrt{5})n + O(W + 1) \approx 0.71258\,n$ under the octant split at $\arctan(1/2)$)—already cutting the trivial $2n$ row bound by nearly two-thirds before higher Farey directions collapse the linear growth rate to $O(n^{3/4}W^{1/4})$.

Our second main theorem proves that the two-parameter law of Theorem 1 is **sharp up to multiplicative constants with zero logarithmic losses** across all $C^2$ variable-curvature collars and across the entire parameter plane $(R, W) \in [1, \infty) \times [0, \infty)$.

**Theorem 2 (Log-Free Farey-Punctured Conic Lower Bound and Complete Phase Diagram).** *Let $0 < c_0 \le 1$ and $0 < c_1 \le c_2$. For $R \ge 1$, $W \ge 0$, and $f \in C^2([-c_0 R, c_0 R])$ satisfying $|f'(x)| \le 1$ and $c_1 / R \le f''(x) \le c_2 / R$ on $[-c_0 R, c_0 R]$, define the graph collar*

$$
\mathcal{S}_f(R, W) := \big\{(x, y) \in \mathbb{Z}^2 : |x| \le c_0 R,\; f(x) \le y \le f(x) + W\big\}.
$$

1. *(Every individual $C^2$ curve for $1 \le W \le R$)* *There exists a constant $c = c(c_0, c_1, c_2) > 0$ such that for every $R \ge 1$ and every $1 \le W \le R$, $\mathcal{S}_f(R, W)$ contains a no-three-in-line subset $S$ with*

$$
|S| \ge c\, R^{3/4} W^{1/4}.
$$

2. *(Sub-unit shifted-curve regime $R^{-1/3} \le W < 1$ and individual barrier)* *For every $R \ge 1$ and every $R^{-1/3} \le W < 1$, there exists a vertical shift $\theta \in [0, 1)$ such that $\mathcal{S}_{f + \theta}(R, W)$ contains a no-three-in-line subset $S$ with $|S| \ge c\, R^{3/4} W^{1/4}$. By contrast, for every integer $R \ge 1$, the curve $f_0(x) = \frac{x^2}{2R} + \frac{1}{4R}$ satisfies $\mathcal{S}_{f_0}(R, W) = \emptyset$ whenever $0 \le W < \frac{1}{4R}$.*

3. *(Complete extremal phase diagram on $\mathcal{K}_{\mathrm{sp}}(R)$)* *Writing $\alpha(\Omega)$ for the maximum size of a no-three-in-line subset of $\Omega \subseteq \mathbb{Z}^2$, one has uniformly over all $R \ge 1$ and all $W \ge 0$:*

$$
\sup_{K \in \mathcal{K}_{\mathrm{sp}}(R)} \alpha\!\big(\mathcal{C}_{0, W}(K)\big) \asymp R^{3/4}\min(W, R)^{1/4} + R^{2/3} + W.
$$

The proof of Theorem 2 combines order-$H$ Farey tangent puncturing at $H = \lfloor (R/W)^{1/4} \rfloor$ with a uniformly translated anisotropic $\mathbb{F}_p$-conic $(x - a)^2 - d(y - b)^2 \equiv 1 \pmod p$ ($d \in \mathbb{F}_p^\times$ a quadratic nonresidue) at prime scale $p \asymp R^{1/4}W^{3/4}$. Puncturing deterministically eliminates all low-height grazing chords and forces a macroscopic gap between crossing branches, while the prime scale $p \asymp R^{1/4}W^{3/4}$ eliminates all high-height grazing chords and keeps expected cross-branch $(2 + 1)$-collinearities strictly smaller than half the surviving conic seed without incurring the $(\log R)^{-1/2}$ alteration penalty of random subsampling.

Our third result compares this discrete $\Theta(R^{3/4}W^{1/4})$ law against the continuum Radon relaxation on the circular shell $\mathcal{A}_{\mathbb{R}^2}(R, W) := \{x \in \mathbb{R}^2 : R \le \|x\|_2 \le R + W\}$.

**Theorem 3 (Continuum Radon Collapse and Discrete $SO(2)$-Symmetry Breaking).** *For $R \ge 0$ and $W > 0$, define the continuum Radon capacity over Borel measurable densities $\rho : \mathcal{A}_{\mathbb{R}^2}(R, W) \to [0, 1]$ by*

$$
\mathrm{LP}_{\mathrm{cont}}\!\big(\mathcal{A}_{\mathbb{R}^2}(R, W)\big) := \sup\left\{\iint_{\mathcal{A}_{\mathbb{R}^2}(R, W)} \rho(x)\,dx \;\middle|\; \rho \text{ Borel},\; 0 \le \rho(x) \le 1 \;\forall x,\; \forall \ell \subset \mathbb{R}^2:\, \int_{\ell \cap \mathcal{A}_{\mathbb{R}^2}(R, W)} \rho\,ds \le 2\right\},
$$

*and write $U_{\mathrm{cont}}(R, W) := 4\sqrt{2 R W + W^2}$. Then for all $R \ge 0$ and $W > 0$,*

$$
\max\!\left(0,\; U_{\mathrm{cont}}(R, W) - \frac{4}{\pi}\right) \le \mathrm{LP}_{\mathrm{cont}}\!\big(\mathcal{A}_{\mathbb{R}^2}(R, W)\big) \le \min\!\big(\pi(2 R W + W^2),\; U_{\mathrm{cont}}(R, W)\big).
$$

*At $R = 0$, this matches the $2 \cdot \operatorname{diam} = 4W$ disk chord bound [2] up to at most $4/\pi$ (and the trivial area bound $\pi W^2$ when $W \le 4/\pi$). For $1 \le W \ll R$, however, discrete integer caps satisfy $\alpha(\mathcal{A}(R, W)) = \Theta(R^{3/4}W^{1/4})$, exceeding $\mathrm{LP}_{\mathrm{cont}}(\mathcal{A}_{\mathbb{R}^2}(R, W)) \le U_{\mathrm{cont}}(R, W) \asymp R^{1/2}W^{1/2}$ by the unbounded factor $(R/W)^{1/4} \to \infty$.*

Why can a discrete $\{0, 1\}$-subset of $\mathbb{Z}^2$ pack arbitrarily many times more mass into a thin circular shell than *any* bounded Borel density in $[0, 1]$? In the continuum, $SO(2)$ rotational invariance averages every density into a radial profile constrained by grazing chords of length $2\sqrt{2 R W + W^2}$ in *every* direction $\theta \in [0, 2\pi)$. On $\mathbb{Z}^2$, however, a line through at least two lattice points must have rational slope $v_y / v_x$ of integer height: lines with $\|v\|_2 > \sqrt{2 R W + W^2}$ meet $\mathcal{A}(R, W)$ in $\le 2$ points automatically (Lemma 2.1), intermediate slopes $(R/W)^{1/4} < \|v\|_2 \le \sqrt{2 R W + W^2}$ have chord span $O(\sqrt{R W}) < p\|v\|_2$ and thus cannot repeat residues along a mod-$p$ conic at $p \asymp R^{1/4}W^{3/4}$, and the remaining low-height grazing lines ($\|v\|_2 \le (R/W)^{1/4}$) cluster around the measure-$o(1)$ set of Farey tangent angles. Evacuating those Farey tangent neighborhoods breaks $SO(2)$ symmetry and unlocks the $(R/W)^{1/4}$ gain.

Finally, applying Theorem 1(1) directly to the Euclidean convex hull $K = \operatorname{conv}(S) \subseteq [1, n]^2$ yields an unrestricted structural law for *every* linear-density cap on $G_n$.

**Corollary 1 (Unrestricted Convex-Hull Depth, Onion Layers, and Inradius Law on $G_n$).** *There exist absolute constants $c_0, c_1, C_0 > 0$ such that for every no-three-in-line subset $S \subseteq G_n$ of cardinality $|S| = \alpha n$ ($\alpha > 0$):*

1. *For every $W \ge 0$, at most $O(n^{3/4}\min(W, n)^{1/4} + n^{2/3} + W + 1)$ points of $S$ lie within Euclidean distance $W$ of $\partial\operatorname{conv}(S)$ (and at most $O\big(m(n^{3/4}\min(W, n)^{1/4} + n^{2/3} + W + 1)\big)$ points lie within the union of $W$-collars around any $m$ compact convex subsets of $[1, n]^2$). Taking $W = 0$, iteratively peeling convex-hull boundaries $S_0 := S$, $S_{j+1} := S_j \setminus \partial\operatorname{conv}(S_j)$ requires at least $c_1 \alpha n^{1/3}$ strictly nested convex layers for every $n \ge 1$.*
2. *Whenever $n \ge C_0 \alpha^{-3}$, strictly more than $\frac{1}{2}|S|$ points of $S$ lie at Euclidean distance $> c_0 \alpha^4 n$ inside $\partial\operatorname{conv}(S)$. In particular, $\operatorname{conv}(S)$ contains an inscribed Euclidean disk of radius $r_{\mathrm{in}}(\operatorname{conv}(S)) \ge c_0 \alpha^4 n$ and satisfies $\operatorname{Area}(\operatorname{conv}(S)) \ge \pi c_0^2 \alpha^8 n^2$.*

---

## 2. Exact Quadratic-Shell Cutoff and Universal Farey–Sagitta Upper Bounds

We begin with an exact algebraic identity showing that positive-semidefinite quadratic shells automatically eliminate collinear triples along all high-norm primitive directions.

**Lemma 2.1 (Quadratic-Shell High-Slope Cutoff).** *Let $\phi(x) = \langle x, A x \rangle + \langle b, x \rangle + c_0$ on $\mathbb{R}^2$, where $A \in \mathbb{R}^{2\times 2}$ is symmetric positive semidefinite, and let $\mathcal{A}_\Delta(\phi) := \{P \in \mathbb{Z}^2 : 0 \le \phi(P) \le \Delta\}$ ($\Delta \ge 0$). For every collinear triple $P_0,\; P_1 = P_0 + m_1 v,\; P_2 = P_0 + m_2 v \in \mathcal{A}_\Delta(\phi)$ with $0 < m_1 < m_2$ ($m_1, m_2 \in \mathbb{Z}$, $v \in \mathbb{Z}^2 \setminus \{0\}$ primitive), one has*

$$
m_1(m_2 - m_1)\langle v, A v \rangle \le \Delta.
$$

*In particular, if $A \succ 0$ has minimum eigenvalue $\lambda_{\min}(A) > 0$, every primitive direction $v$ with $\|v\|_2 > \sqrt{\Delta / \lambda_{\min}(A)}$ meets $\mathcal{A}_\Delta(\phi)$ in at most two points.*

*Proof.* Along $q(t) := \phi(P_0 + t v) = q(0) + t q'(0) + t^2 \langle v, A v \rangle$, the second-difference combination eliminates the constant and linear terms identically:

$$
(m_2 - m_1)\phi(P_0) + m_1 \phi(P_2) - m_2 \phi(P_1) = m_1 m_2 (m_2 - m_1)\langle v, A v \rangle.
$$

Since $\phi(P_0), \phi(P_2) \le \Delta$, $\phi(P_1) \ge 0$, and $m_2 - m_1, m_1, m_2 > 0$, the left-hand side is at most $(m_2 - m_1)\Delta + m_1 \Delta = m_2 \Delta$. Dividing by $m_2$ gives $m_1(m_2 - m_1)\langle v, A v \rangle \le \Delta$; when $m_1 \ge 1$ and $m_2 - m_1 \ge 1$, $\lambda_{\min}(A)\|v\|_2^2 \le \langle v, A v \rangle \le \Delta$. $\square$

For $\mathcal{A}(R, W) = \{P \in \mathbb{Z}^2 : R^2 \le \|P\|_2^2 \le (R + W)^2\}$, Lemma 2.1 with $\phi(x, y) = x^2 + y^2 - R^2$ ($A = I_2$) and $\Delta = 2 R W + W^2$ shows that every rich line has $\|v\|_2 \le \sqrt{2 R W + W^2}$; for the parabolic collar $0 \le y - \frac{(x - R)^2}{2R} \le W$, taking $\phi(x, y) = \frac{(x - R)^2}{2R} - y + W$ ($A = \operatorname{diag}(\frac{1}{2R}, 0)$) and $\Delta = W$ gives $m_1(m_2 - m_1)v_x^2 \le 2 R W$ for all non-vertical lines.

### 2.1 Isotropic Disk Farey Geometry and Rolling-Ball Lemmas

To prove Theorem 1 across all $\Lambda \ge 1$, we first record the exact unimodularity and gap properties of the Euclidean disk primitive set $\mathcal{V}_\Lambda$.

**Lemma 2.2 (Isotropic Disk Farey Neighbors).** *For every $\Lambda \ge 1$, consecutive vectors $v_i, v_{i+1} \in \mathcal{V}_\Lambda$ ordered counterclockwise satisfy:*

1. $\det(v_i, v_{i+1}) = +1$ *and* $\Delta\varphi_i \in (0, \pi/2]$ *(with $\Delta\varphi_i \in (0, \pi/4]$ whenever $\Lambda \ge \sqrt{2}$);*
2. $\|v_i\|_2 + \|v_{i+1}\|_2 > \|v_i + v_{i+1}\|_2 > \Lambda$;
3. $\|v_i\|_2 \sin\gamma_i \le \|v_i\|_2 \gamma_i < \frac{\pi}{2\Lambda}$.

*Proof.* Since $\mathcal{V}_1 = \{(\pm 1, 0), (0, \pm 1)\} \subseteq \mathcal{V}_\Lambda$ (and $\{(\pm 1, \pm 1)\} \subseteq \mathcal{V}_\Lambda$ for $\Lambda \ge \sqrt{2}$), consecutive vectors always lie in a single closed quadrant (or octant for $\Lambda \ge \sqrt{2}$), giving $\Delta\varphi_i \in (0, \pi/2]$ and $d := \det(v_i, v_{i+1}) \ge 1$ since $v_i, v_{i+1}$ are primitive and non-collinear. Suppose for contradiction that $d \ge 2$. Consider the closed triangle $T = \operatorname{conv}(0, v_i, v_{i+1})$, which lies inside the convex disk $\overline{B}(0, \Lambda)$ and has area $d / 2 \ge 1$. Because $v_i$ and $v_{i+1}$ are primitive, the edges $[0, v_i]$ and $[0, v_{i+1}]$ contain no interior lattice points; if the open triangle $\operatorname{int}(T)$ and the open third edge $(v_i, v_{i+1})$ contained $I = 0$ and $B - 3 = 0$ lattice points respectively, Pick's theorem would give $\operatorname{Area}(T) = I + \frac{B}{2} - 1 = \frac{1}{2}$, contradicting $d \ge 2$. Hence $T \setminus \{0, v_i, v_{i+1}\}$ contains at least one nonzero lattice point $w \in \overline{B}(0, \Lambda)$; dividing $w$ by $\gcd(|w_x|, |w_y|)$ produces a primitive vector $w' \in \mathcal{V}_\Lambda$ strictly between the rays $\mathbb{R}_+ v_i$ and $\mathbb{R}_+ v_{i+1}$ (as $w = \lambda_1 v_i + \lambda_2 v_{i+1}$ with $\lambda_1, \lambda_2 > 0$, since $[0, v_i]$ and $[0, v_{i+1}]$ have no interior lattice points), contradicting consecutiveness of $v_i, v_{i+1}$. Thus $\det(v_i, v_{i+1}) = +1$.

Consequently, $v_i + v_{i+1}$ is primitive ($\det(v_i, v_i + v_{i+1}) = 1$) and lies strictly between $v_i$ and $v_{i+1}$ in angle, so $v_i + v_{i+1} \notin \mathcal{V}_\Lambda$, giving $\|v_i\|_2 + \|v_{i+1}\|_2 > \|v_i + v_{i+1}\|_2 > \Lambda$ (strictness holds because $v_i, v_{i+1}$ are non-collinear). Finally, $\sin(\Delta\varphi_i) = \frac{\det(v_i, v_{i+1})}{\|v_i\|_2 \|v_{i+1}\|_2} = \frac{1}{\|v_i\|_2 \|v_{i+1}\|_2}$ and $\Delta\varphi_i \le \frac{\pi}{2}\sin(\Delta\varphi_i)$, whence

$$
\|v_i\|_2 \alpha_i = \frac{\|v_i\|_2 \|v_{i+1}\|_2}{\|v_i\|_2 + \|v_{i+1}\|_2}\Delta\varphi_i \le \frac{\pi}{2\big(\|v_i\|_2 + \|v_{i+1}\|_2\big)} < \frac{\pi}{2\Lambda},
$$

and symmetrically $\|v_i\|_2 \beta_{i-1} = \frac{\|v_{i-1}\|_2 \|v_i\|_2}{\|v_{i-1}\|_2 + \|v_i\|_2}\Delta\varphi_{i-1} < \frac{\pi}{2\Lambda}$, proving (3). $\square$

Next we verify two clean convex-geometry lemmas: normal projection for arbitrary inward depths $W_- \ge 0$, and the elementary rolling-ball inclusion for $R$-spindle-convex sets.

**Lemma 2.3 (Unrestricted Two-Sided Normal Representation and Rolling Ball).**

1. *Let $K \subset \mathbb{R}^2$ be any non-empty compact convex set. Every $P \in \mathcal{C}_{W_-, W_+}(K)$ admits a boundary point $y \in \partial K$, an outer unit normal $\mathbf{n}(\varphi) \in N_K(y)$ ($\langle z - y, \mathbf{n}(\varphi) \rangle \le 0$ for all $z \in K$), and an offset $t \in [-W_-, W_+]$ such that $P = y + t\,\mathbf{n}(\varphi)$.*
2. *If $K \in \mathcal{K}_{\mathrm{sp}}(R)$, then for every $y \in \partial K$ and every outer unit normal $\mathbf{n}(\varphi) \in N_K(y)$, one has $K \subseteq \overline{B}(y - R\mathbf{n}(\varphi), R)$, and hence for every angle $\varphi_i \in [0, 2\pi)$,*

$$
h_K(\varphi_i) - R\big(1 - \cos(\varphi - \varphi_i)\big) \le \langle y, \mathbf{n}(\varphi_i) \rangle \le h_K(\varphi_i).
$$

*Proof.* For (1), if $P \notin \operatorname{int}(K)$, let $y = \operatorname{proj}_K(P) \in \partial K$ and $t = \|P - y\|_2 \in [0, W_+]$; if $t > 0$, standard metric projection onto a convex set gives $\mathbf{n}(\varphi) := (P - y)/t \in N_K(y)$, while if $t = 0$, $y \in \partial K$ admits a supporting hyperplane and hence some $\mathbf{n}(\varphi) \in N_K(y)$. If $P \in \operatorname{int}(K)$, let $y \in \partial K$ attain $d := \operatorname{dist}_2(P, \partial K) = \|y - P\|_2 \in (0, W_-]$. Then $B(P, d) \subseteq K$. Choose any supporting outer unit normal $\mathbf{u} \in N_K(y)$; then $\sup_{z \in B(P, d)} \langle z - y, \mathbf{u} \rangle = \langle P - y, \mathbf{u} \rangle + d \le 0$, so $\langle y - P, \mathbf{u} \rangle \ge d = \|y - P\|_2 \|\mathbf{u}\|_2$. By equality in Cauchy–Schwarz, $\mathbf{u} = (y - P)/d$ uniquely, so $P = y - d\,\mathbf{u}$ with $t = -d \in [-W_-, 0)$.

For (2), let $\mathcal{C} := \{c \in \mathbb{R}^2 : K \subseteq \overline{B}(c, R)\}$; then $\mathcal{C}$ is non-empty and compact, and $K = \bigcap_{c \in \mathcal{C}} \overline{B}(c, R)$. If $K = \{y\}$ is a singleton, $K \subseteq \overline{B}(y - R\mathbf{n}(\varphi), R)$ is trivial. Otherwise $K$ contains two distinct points $z_1 \ne z_2$ with $2\delta := \|z_1 - z_2\|_2 \le 2R$. If $\delta = R$, then $\mathcal{C} = \{\frac{z_1 + z_2}{2}\}$ and $K = \overline{B}(\frac{z_1 + z_2}{2}, R)$, where $\mathbf{n}(\varphi) = \frac{y - c}{R}$ is unique and $y - R\mathbf{n}(\varphi) = c$. If $0 < \delta < R$, then for $m := \frac{z_1 + z_2}{2}$ and every $c \in \mathcal{C}$, the parallelogram law gives $\|c - m\|_2^2 = \frac{1}{2}\|c - z_1\|_2^2 + \frac{1}{2}\|c - z_2\|_2^2 - \delta^2 \le R^2 - \delta^2$, so $B(m, R - \sqrt{R^2 - \delta^2}) \subseteq K$ and $\operatorname{int}(K) \ne \emptyset$. Fix $x_0 \in \operatorname{int}(K)$ with $B(x_0, \rho) \subseteq K$ ($\rho > 0$), and let $\mathcal{C}(y) := \{c \in \mathcal{C} : \|y - c\|_2 = R\}$ be the non-empty compact active center set at $y \in \partial K$, with compact unit-vector image $U(y) := \{\frac{y - c}{R} : c \in \mathcal{C}(y)\} \subset \mathbb{S}^1$. For every $c \in \mathcal{C}(y)$, $\|x_0 - c\|_2 \le R - \rho$, so expanding $\|x_0 - c\|_2^2 = \|(x_0 - y) + (y - c)\|_2^2 = \|x_0 - y\|_2^2 + R^2 + 2\langle x_0 - y, y - c \rangle \le (R - \rho)^2$ yields $\langle y - x_0, \frac{y - c}{R} \rangle \ge \frac{R^2 - (R - \rho)^2}{2R} =: \eta > 0$. By compactness of $\mathcal{C} \setminus V$ for open neighborhoods $V \supset \mathcal{C}(y)$, any $v \in \mathbb{R}^2$ satisfying $\langle v, \mathbf{u} \rangle < 0$ for all $\mathbf{u} \in U(y)$ satisfies $y + \varepsilon v \in K$ for small $\varepsilon > 0$; taking convex combinations with $x_0 - y$ shows that the tangent cone of $K$ at $y$ is $T_K(y) = \{v \in \mathbb{R}^2 : \langle v, \mathbf{u} \rangle \le 0\;\forall \mathbf{u} \in U(y)\} = \operatorname{cone}(U(y))^\circ$. By Carathéodory's theorem in $\mathbb{R}^2$, every vector in $\operatorname{cone}(U(y))$ has the form $\lambda_1 \mathbf{u}_1 + \lambda_2 \mathbf{u}_2$ with $\lambda_1, \lambda_2 \ge 0$ and $\mathbf{u}_1, \mathbf{u}_2 \in U(y)$; since $\langle \lambda_1 \mathbf{u}_1 + \lambda_2 \mathbf{u}_2, y - x_0 \rangle \ge \eta(\lambda_1 + \lambda_2)$ bounds $\lambda_1 + \lambda_2$ along convergent sequences and $U(y)$ is compact, $\operatorname{cone}(U(y))$ is closed. By the bipolar theorem, $N_K(y) = T_K(y)^\circ = \operatorname{cone}(U(y))$, so $\mathbf{n}(\varphi) = \lambda_1 \mathbf{u}_1 + \lambda_2 \mathbf{u}_2$ for some $\lambda_1, \lambda_2 \ge 0$ and $\mathbf{u}_1, \mathbf{u}_2 \in U(y)$. By the triangle inequality, $\lambda_1 + \lambda_2 \ge \|\lambda_1 \mathbf{u}_1 + \lambda_2 \mathbf{u}_2\|_2 = 1$. For every $z \in K$ and $j \in \{1, 2\}$, $\|z - (y - R\mathbf{u}_j)\|_2^2 \le R^2$ expands to $2 R \langle y - z, \mathbf{u}_j \rangle \ge \|z - y\|_2^2$; multiplying by $\lambda_j$ and summing yields

$$
2 R \langle y - z, \mathbf{n}(\varphi) \rangle \ge (\lambda_1 + \lambda_2)\|z - y\|_2^2 \ge \|z - y\|_2^2 \implies \|z - (y - R\mathbf{n}(\varphi))\|_2^2 \le R^2.
$$

Thus $K \subseteq \overline{B}(y - R\mathbf{n}(\varphi), R)$. Taking support functions in direction $\mathbf{n}(\varphi_i)$ immediately gives

$$
h_K(\varphi_i) \le \sup_{z \in \overline{B}(y - R\mathbf{n}(\varphi), R)} \langle z, \mathbf{n}(\varphi_i) \rangle = \langle y - R\mathbf{n}(\varphi), \mathbf{n}(\varphi_i) \rangle + R = \langle y, \mathbf{n}(\varphi_i) \rangle + R\big(1 - \cos(\varphi - \varphi_i)\big),
$$

while $\langle y, \mathbf{n}(\varphi_i) \rangle \le h_K(\varphi_i)$ holds because $y \in K$. $\square$

### 2.2 Proof of Theorem 1 and Local-Curvature Refinement

*Proof of Theorem 1.* Partition $\mathbb{R} / 2\pi\mathbb{Z}$ into the $M_\Lambda$ half-open Farey sectors $I_i := [\varphi_i - \beta_{i-1}, \varphi_i + \alpha_i)$ ($1 \le i \le M_\Lambda$). Since $\Delta\varphi_j \in (0, \pi/2]$ and $0 < \alpha_j, \beta_j < \Delta\varphi_j$ for all $1 \le j \le M_\Lambda$, we have $\gamma_i = \max(\beta_{i-1}, \alpha_i) < \frac{\pi}{2}$ and $\cos(\varphi - \varphi_i) \ge \cos\gamma_i > 0$ for all $\varphi \in I_i$. Let $x : \mathcal{C}_{W_-, W_+}(K) \to [0, 1]$ be any fractional Radon weight satisfying $\sum_{P \in \ell \cap \mathcal{C}_{W_-, W_+}(K)} x_P \le 2$ for every Euclidean line $\ell \subset \mathbb{R}^2$ (including $x = \mathbf{1}_S$ for any cap $S$).

**Proof of (2) ($R$-spindle-convex sets).** By Lemma 2.3(1), assign each $P \in \mathcal{C}_{W_-, W_+}(K)$ a representation $P = y + t\,\mathbf{n}(\varphi)$ with $y \in \partial K$, $\mathbf{n}(\varphi) \in N_K(y)$, and $t \in [-W_-, W_+]$, and set $\Omega_i := \{P \in \mathcal{C}_{W_-, W_+}(K) : \varphi \in I_i\}$. For every $P \in \Omega_i$, Lemma 2.3(2) and $0 < \cos(\varphi - \varphi_i) \le 1$ give:

- if $t \in [0, W_+]$, then $h_K(\varphi_i) - R(1 - \cos\gamma_i) \le \langle y, \mathbf{n}(\varphi_i) \rangle \le \langle P, \mathbf{n}(\varphi_i) \rangle \le h_K(\varphi_i) + W_+$;
- if $t \in [-W_-, 0)$, then $h_K(\varphi_i) - R(1 - \cos\gamma_i) - W_- \le \langle P, \mathbf{n}(\varphi_i) \rangle \le \langle y, \mathbf{n}(\varphi_i) \rangle \le h_K(\varphi_i)$.

Hence for all $P \in \Omega_i$, the integer $\det(P, v_i) = \|v_i\|_2 \langle P, \mathbf{n}(\varphi_i) \rangle$ lies in a real interval of length $\|v_i\|_2 \big(W + R(1 - \cos\gamma_i)\big)$, taking at most $1 + \|v_i\|_2 W + \|v_i\|_2 R(1 - \cos\gamma_i)$ integer values. Since each level set $\det(P, v_i) = c$ is a single Euclidean line carrying fractional mass $\sum_{P \in \Omega_i : \det(P, v_i) = c} x_P \le 2$, summing $\sum_{P \in \Omega_i} x_P$ over $i = 1, \ldots, M_\Lambda$ yields the exact finite-$\Lambda$ inequality in Theorem 1(2) for $\mathrm{LP}(\mathcal{C}_{W_-, W_+}(K)) \ge |S|$.

For the asymptotic constant in (2), Möbius inversion on the disk gives $M_\Lambda = \frac{6}{\pi}\Lambda^2 + O(\Lambda\log\Lambda)$ and $\sum_{v \in \mathcal{V}_\Lambda} \|v\|_2 = \frac{4}{\pi}\Lambda^3 + O(\Lambda^2\log\Lambda)$. Using $1 - \cos\gamma_i \le \frac{1}{2}\gamma_i^2 \le \frac{1}{2}(\beta_{i-1}^2 + \alpha_i^2)$ and reindexing $\beta_{i-1}^2$ shifts gives

$$
2 \sum_{i=1}^{M_\Lambda} \|v_i\|_2(1 - \cos\gamma_i) \le \sum_{i=1}^{M_\Lambda} \big(\|v_i\|_2 \alpha_i^2 + \|v_{i+1}\|_2 \beta_i^2\big) = \sum_{i=1}^{M_\Lambda} \frac{\|v_i\|_2 \|v_{i+1}\|_2}{\|v_i\|_2 + \|v_{i+1}\|_2} (\Delta\varphi_i)^2.
$$

As $\Lambda \to \infty$, $\max_i \Delta\varphi_i \le \frac{\pi}{2\Lambda} \to 0$, so $\|v_i\|_2 \|v_{i+1}\|_2 \Delta\varphi_i = \frac{\Delta\varphi_i}{\sin\Delta\varphi_i} = 1 + O(\Lambda^{-2})$, while $\|v_i\|_2 + \|v_{i+1}\|_2 > \Lambda$ by Lemma 2.2(2). Summing $\sum_{i=1}^{M_\Lambda} \Delta\varphi_i = 2\pi$ bounds the display above by $\frac{2\pi}{\Lambda} + O(\Lambda^{-3})$. Whenever $W / R \to 0$ and $R^{1/3} W \to \infty$, choosing $\Lambda = \lambda_* (R/W)^{1/4} \to \infty$ (with $\lambda_* > 0$ minimizing $\frac{8}{\pi}\lambda^3 + \frac{2\pi}{\lambda}$, so $\Lambda \ge 1$ eventually and $\Lambda^2 W \log\Lambda \ll R^{1/2}W^{1/2}\log(R/W) = o(R^{3/4}W^{1/4})$ since $W/R \to 0$, while $\Lambda^2 \log\Lambda = o(R^{3/4}W^{1/4})$ since $R^{1/3}W \to \infty$) yields $|S| \le \big(8\sqrt{2\pi}\,3^{-3/4} + o(1)\big) R^{3/4} W^{1/4}$, where $\frac{4}{3^{3/4}}(\frac{8}{\pi})^{1/4}(2\pi)^{3/4} = 8\sqrt{2\pi}\,3^{-3/4} \approx 8.7971$.

**Proof of (1) (Arbitrary compact convex sets).** Fix $\varepsilon > 0$ and consider the Minkowski outer parallel body $K_\varepsilon := K + \overline{B}(0, \varepsilon) = \{z \in \mathbb{R}^2 : \operatorname{dist}_2(z, K) \le \varepsilon\}$. Then $\operatorname{int}(K_\varepsilon) \ne \emptyset$ and $L(K_\varepsilon) = \int_0^{2\pi} (h_K(\varphi) + \varepsilon)\,d\varphi = L(K) + 2\pi\varepsilon$. Moreover, $\partial K_\varepsilon$ is $C^{1,1}$: for every $z \in \partial K_\varepsilon$, letting $x = \operatorname{proj}_K(z) \in \partial K$, the ball $\overline{B}(x, \varepsilon) \subseteq K_\varepsilon$ touches $\partial K_\varepsilon$ at $z$, while $\langle q - x, z - x \rangle \le 0$ for all $q \in K$ implies $\langle w - z, z - x \rangle \le 0$ for all $w \in K_\varepsilon$, so $N_{K_\varepsilon}(z)$ consists of the unique continuous outer unit normal $\mathbf{n}(\varphi(z)) = \frac{z - x}{\varepsilon}$.

We verify $\mathcal{C}_{W_-, W_+}(K) \subseteq \mathcal{C}_{W_- + \varepsilon, W_+}(K_\varepsilon)$. For $P \in \mathcal{C}_{W_-, W_+}(K)$ with $P = y + t\,\mathbf{n}(\varphi)$ ($y \in \partial K$, $\mathbf{n}(\varphi) \in N_K(y)$, $t \in [-W_-, W_+]$):

- if $t \ge \varepsilon$, then $\operatorname{dist}_2(P, K_\varepsilon) = \operatorname{dist}_2(P, K) - \varepsilon = t - \varepsilon \in [0, W_+]$;
- if $t \in [-W_-, \varepsilon)$, then $P \in \operatorname{int}(K_\varepsilon)$, and the point $z_* := y + \varepsilon\,\mathbf{n}(\varphi)$ satisfies $\operatorname{dist}_2(z_*, K) = \varepsilon$ (since $\langle q - y, \mathbf{n}(\varphi) \rangle \le 0$ for all $q \in K$), so $z_* \in \partial K_\varepsilon$ and $\operatorname{dist}_2(P, \partial K_\varepsilon) \le \|P - z_*\|_2 = \varepsilon - t \le W_- + \varepsilon$.

Parameterize $\partial K_\varepsilon$ counterclockwise by arclength $s \in \mathbb{R} / L(K_\varepsilon)\mathbb{Z}$ as $\gamma(s)$, so $\gamma'(s) = \mathbf{t}(\varphi(s)) = (-\sin\varphi(s), \cos\varphi(s))$ everywhere and $s \mapsto \varphi(s)$ is continuous and monotone non-decreasing of degree $1$. Thus the preimage $J_i := \{s : \varphi(s) \in I_i\}$ ($1 \le i \le M_\Lambda$) is a collection of $M_\Lambda$ pairwise disjoint intervals partitioning $\mathbb{R} / L(K_\varepsilon)\mathbb{Z}$, with $\sum_{i=1}^{M_\Lambda} |J_i| = L(K_\varepsilon)$. For any two points $\gamma(s_1), \gamma(s_2)$ with $s_1, s_2 \in J_i$,

$$
\big|\langle \gamma(s_2) - \gamma(s_1), \mathbf{n}(\varphi_i) \rangle\big| = \left|\int_{s_1}^{s_2} \langle \mathbf{t}(\varphi(s)), \mathbf{n}(\varphi_i) \rangle\,ds\right| \le \int_{J_i} |\sin(\varphi(s) - \varphi_i)|\,ds \le \sin(\gamma_i)\,|J_i|.
$$

Repeating the normal-offset bound on $K_\varepsilon$ with $(W_- + \varepsilon, W_+)$ shows that on sector $i$, $\det(P, v_i)$ spans an interval of length at most $\|v_i\|_2(W + \varepsilon) + \|v_i\|_2 \sin(\gamma_i)\,|J_i|$. Summing over $i = 1, \ldots, M_\Lambda$ and applying Lemma 2.2(3) ($2\|v_i\|_2\sin\gamma_i < \frac{\pi}{\Lambda}$) gives

$$
|S| \le \mathrm{LP}\big(\mathcal{C}_{W_-, W_+}(K)\big) \le 2 M_\Lambda + 2(W + \varepsilon)\sum_{v \in \mathcal{V}_\Lambda} \|v\|_2 + \frac{\pi}{\Lambda}\big(L(K) + 2\pi\varepsilon\big).
$$

Letting $\varepsilon \downarrow 0$ yields the exact inequality of Theorem 1(1). Whenever $W / L(K) \to 0$ and $L(K)^{1/3} W \to \infty$, minimizing $\frac{8}{\pi}\lambda^3 + \frac{\pi}{\lambda}$ at $\Lambda = \lambda_* (L(K)/W)^{1/4} \to \infty$ gives $|S| \le \big(4(2/3)^{3/4}\sqrt{\pi} + o(1)\big) L(K)^{3/4} W^{1/4}$ ($4(2/3)^{3/4}\sqrt{\pi} \approx 5.2308$). For the uniform bound over all $L(K), W \ge 0$, take $\Lambda = 1$ whenever $0 \le L(K) \le 1$ or $W > L(K)$ (giving $8 + 8W + \pi L(K) \ll L(K) + W + 1$), and for $L(K) > 1$ take $\Lambda = L(K)^{1/3} > 1$ if $0 \le W \le L(K)^{-1/3}$ and $\Lambda = (L(K)/W)^{1/4} \ge 1$ if $L(K)^{-1/3} < W \le L(K)$. $\square$

When a piecewise-$C^2$ convex arc or ball-polygon has non-constant radius of curvature $\rho(\psi)$ (vanishing inside corner normal cones) or spans only a proper arc $J$ of normal angles, the identical sector argument yields a sharper local formula (`fs_local_ub` in Section 5).

**Corollary 2.4 (Local-Curvature and Partial-Arc Sector Formula).** *Let $J$ be either $\mathbb{R}/2\pi\mathbb{Z}$ or a closed arc of length $\le \pi$ in $\mathbb{R}/2\pi\mathbb{Z}$, and let $y : J \to \mathbb{R}^2$ be absolutely continuous with $y'(\psi) = \rho(\psi)\mathbf{t}(\psi)$ a.e., where $0 \le \rho \in L^\infty(J)$ and $\mathbf{t}(\psi) = (-\sin\psi, \cos\psi)$. Suppose every $P$ in a discrete collar $\mathcal{S} \subseteq \mathbb{Z}^2$ admits $\varphi(P) \in J$, $0 \le \eta(P) \le W$, and $\mathbf{u}(P) \in \mathbb{R}^2$ such that $P = y(\varphi(P)) + \eta(P)\,\mathbf{u}(P)$, where on each non-empty intersection $I_i \cap J$ there exist $\sigma_i \in \{-1, +1\}$ and $\omega_i \ge 0$ with $0 \le \sigma_i \langle \mathbf{u}(P), \mathbf{n}(\varphi_i) \rangle \le \omega_i$ whenever $\varphi(P) \in I_i \cap J$ (specifically $\omega_i = 1, \sigma_i = +1$ for outer normal offsets $\mathbf{u}(P) = \mathbf{n}(\varphi(P))$, and $\omega_i = |\sin\varphi_i|$ for one-sided vertical graph offsets $\mathbf{u}(P) = (0, 1)$). Setting $\mathcal{I}_{\mathrm{act}} := \{1 \le i \le M_\Lambda : I_i \cap J \ne \emptyset\}$ and $R_i := \operatorname*{ess\,sup}_{\psi \in I_i \cap J} \rho(\psi)$, every no-three-in-line subset $S \subseteq \mathcal{S}$ satisfies*

$$
|S| \le \mathrm{LP}(\mathcal{S}) \le \sum_{i \in \mathcal{I}_{\mathrm{act}}} \Big(2 + 2 W \omega_i \|v_i\|_2 + 2 R_i \|v_i\|_2 \big(1 - \cos\gamma_i\big)\Big).
$$

*Proof.* Fix $i \in \mathcal{I}_{\mathrm{act}}$. Because $|I_i| = \beta_{i-1} + \alpha_i < \pi$ and either $J = \mathbb{R}/2\pi\mathbb{Z}$ or $|(\mathbb{R}/2\pi\mathbb{Z}) \setminus J| \ge \pi > |I_i|$, the intersection $I_i \cap J$ lifts to a single interval inside $[\varphi_i - \gamma_i, \varphi_i + \gamma_i]$. On this interval, $F_i(\psi) := \langle y(\psi), \mathbf{n}(\varphi_i) \rangle$ is absolutely continuous with $F_i'(\psi) = \rho(\psi)\langle \mathbf{t}(\psi), \mathbf{n}(\varphi_i) \rangle = -\rho(\psi)\sin(\psi - \varphi_i)$ a.e., so $F_i$ is non-decreasing on $(I_i \cap J) \cap [\varphi_i - \gamma_i, \varphi_i]$ and non-increasing on $(I_i \cap J) \cap [\varphi_i, \varphi_i + \gamma_i]$. Letting $\psi_i^* \in \overline{I_i \cap J}$ be the point of $\overline{I_i \cap J}$ closest to $\varphi_i$, every $\psi \in I_i \cap J$ satisfies $0 \le F_i(\psi_i^*) - F_i(\psi) \le \int_{|\psi_i^* - \varphi_i|}^{|\psi - \varphi_i|} R_i \sin\theta\,d\theta \le R_i(1 - \cos\gamma_i)$. Since $\eta(P)\langle \mathbf{u}(P), \mathbf{n}(\varphi_i)\rangle$ lies in $[0, W\omega_i]$ if $\sigma_i = +1$ and in $[-W\omega_i, 0]$ if $\sigma_i = -1$, $\langle P, \mathbf{n}(\varphi_i)\rangle$ lies in a single interval of length $W\omega_i + R_i(1 - \cos\gamma_i)$ for all $P \in \mathcal{S}$ with $\varphi(P) \in I_i \cap J$; multiplying by $\|v_i\|_2$ and summing at most $2$ fractional units per occupied integer line $\det(P, v_i) = c$ proves the claim. $\square$

---

## 3. Log-Free Farey-Punctured Conic Construction and Phase Diagram

We now prove Theorem 2 across all scales $(R, W)$, treating parts (1) and (2) by a unified vertical-translation and Farey-punctured $\mathbb{F}_p$-conic argument.

*Proof of Theorem 2.* Fix $0 < c_0 \le 1$ and $0 < c_1 \le c_2$. For bounded radii $1 \le R < R_0(c_0, c_1, c_2)$ and $R^{-1/3} \le W \le R$, a single lattice point in $\mathcal{S}_{f + \theta}(R, W)$ (which exists unconditionally for $W \ge 1$ at $\theta = 0$, and for some $\theta \in [0, 1)$ whenever $W > 0$) has size $1 \ge R_0^{-1} R^{3/4}W^{1/4}$, so we may assume $R \ge R_0(c_0, c_1, c_2)$ is sufficiently large.

**Step 1: Order-$H$ Farey tangent puncturing.** Suppose $R^{-1/3} \le W \le R$. Set

$$
H := \left\lfloor \left(\frac{R}{W}\right)^{1/4} \right\rfloor \ge 1, \qquad \delta_1 := \min\!\left(1,\; \frac{c_0 c_1}{10}\right) > 0.
$$

 Note that $\frac{1}{2}(R/W)^{1/4} < H \le (R/W)^{1/4} \le R^{1/3}$. For each primitive vector $v = (v_x, v_y) \in \mathbb{Z}^2$ with $1 \le v_x \le H$, define the tangent exclusion set

$$
E_v := \left\{x \in [-c_0 R, c_0 R] : \left|f'(x) - \frac{v_y}{v_x}\right| < \frac{\delta_1}{v_x H}\right\}.
$$

Since $|f'(x)| \le 1$ and $\frac{\delta_1}{v_x H} \le 1$, $E_v$ is empty unless $|v_y| \le 2 v_x$ (at most $4 v_x + 1 \le 5 v_x$ values of $v_y$ per $v_x$). Because $f'$ is strictly increasing with $f''(x) \ge c_1 / R$, each $E_v$ is an interval of length at most $\frac{2\delta_1 R}{c_1 v_x H}$, containing at most $\frac{2\delta_1 R}{c_1 v_x H} + 1$ integers. Let $X^* := ([-c_0 R, c_0 R] \cap \mathbb{Z}) \setminus \bigcup_{1 \le v_x \le H} E_v$. Summing over $1 \le v_x \le H$ bounds the number of deleted integers by

$$
\sum_{v_x = 1}^H 5 v_x \left(\frac{2\delta_1 R}{c_1 v_x H} + 1\right) \le \frac{10\delta_1}{c_1} R + 5 H^2 \le c_0 R + 5 R^{2/3}.
$$

Since $|[-c_0 R, c_0 R] \cap \mathbb{Z}| \ge 2 c_0 R - 1$, choosing $R_0 \ge 512$ large enough that $5 R_0^{2/3} + 1 \le \frac{1}{2} c_0 R_0$ ensures $|X^*| \ge \frac{1}{2} c_0 R$. Notice that $X^*$ depends only on $f'$, so it is completely invariant under vertical shifts $f_\theta(x) := f(x) + \theta$. Define the punctured collar $\Lambda^*(\theta) := \{(x, y) \in \mathcal{S}_{f_\theta}(R, W) : x \in X^*\}$.

- When $1 \le W \le R$, we fix $\theta = 0$ deterministically: for each $x \in X^*$, $|[f(x), f(x) + W] \cap \mathbb{Z}| = \lfloor f(x) + W \rfloor - \lceil f(x) \rceil + 1 \ge \lfloor W \rfloor \ge \frac{1}{2}W$, so $|\Lambda^*(0)| \ge \frac{1}{4} c_0 R W$.
- When $R^{-1/3} \le W < 1$, we sample $\theta \in [0, 1)$ uniformly: for each fixed $x \in X^*$, $\sum_{y \in \mathbb{Z}} \int_0^1 \mathbf{1}_{f(x) + \theta \le y \le f(x) + \theta + W}\,d\theta = W$ identically, giving $\mathbb{E}_\theta[|\Lambda^*(\theta)|] = W |X^*| \ge \frac{1}{2} c_0 R W$.

**Step 2: Anisotropic $\mathbb{F}_p$-conic intersection and deterministic branch separation.** Let $C_1 = C_1(c_0, c_1, c_2) > \max\big(4,\; \frac{4}{\delta_1},\; \frac{8 c_2}{\delta_1 c_1},\; 16\sqrt{2/c_1}\big)$ be a large constant to be chosen below. Since $R^{1/4}W^{3/4} \ge R^{1/4}(R^{-1/3})^{3/4} = 1$, Bertrand's postulate provides an odd prime

$$
p \in \big[C_1 R^{1/4} W^{3/4},\; 2 C_1 R^{1/4} W^{3/4}\big].
$$

Fix a quadratic nonresidue $d \in \mathbb{F}_p^\times$, sample $(a, b) \in \mathbb{F}_p^2$ uniformly (independently of $\theta$), and define

$$
C_{a, b} := \big\{(x, y) \in \mathbb{Z}^2 : (x - a)^2 - d(y - b)^2 \equiv 1 \pmod p\big\}, \qquad S_0 := \Lambda^*(\theta) \cap C_{a, b}.
$$

Because $x^2 - d y^2 \equiv 1 \pmod p$ is a smooth anisotropic conic in $\mathbb{F}_p^2$ with $p + 1$ points and no points at infinity, *every* affine line in $\mathbb{F}_p^2$ meets $C_{a, b} \bmod p$ in at most $2$ residue classes, and for every $P \in \mathbb{Z}^2$, $\Pr_{a,b}[P \in C_{a, b}] = \frac{p + 1}{p^2} > \frac{1}{p}$. Hence

$$
\mathbb{E}[|S_0|] \ge \frac{c_0 R W}{4 p} \ge \frac{c_0}{8 C_1}\, R^{3/4} W^{1/4}.
$$

Consider any Euclidean lattice line $\ell \subset \mathbb{R}^2$ of primitive direction $v = (v_x, v_y)$ ($v_x \ge 0$, $\gcd(|v_x|, |v_y|) = 1$). Since $v$ is primitive, reducing $\ell$ modulo $p$ gives a well-defined affine line $\overline{\ell} \subset \mathbb{F}_p^2$ unless $p \mid v_x$ and $p \mid v_y$, which is impossible because $\gcd(|v_x|, |v_y|) = 1$. If $v = (0, 1)$ is vertical, $|\ell \cap \mathcal{S}_{f_\theta}(R, W)| \le \lfloor W \rfloor + 1 \le 2$ when $W < 1$, and $\le 2W < \frac{1}{2} C_1 W \le \frac{1}{2} p$ when $1 \le W \le R$; hence vertical lines contain no mod-$p$ repeats and hold at most $2$ points of $S_0$ deterministically.

Suppose now $v_x \ge 1$, write $\ell$ as $y = \frac{v_y}{v_x} x + \beta$, and set $g_\theta(x) := f_\theta(x) - \frac{v_y}{v_x} x - \beta$ on $[-c_0 R, c_0 R]$, so $(x, \frac{v_y}{v_x}x + \beta) \in \Lambda^*(\theta) \iff x \in X^*$ and $-W \le g_\theta(x) \le 0$. Note $g_\theta''(x) = f''(x) \in [c_1 / R, c_2 / R]$. Let $I(\ell) := \{x \in [-c_0 R, c_0 R] : -W \le g_\theta(x) \le 0\}$.

1. *Low-height lines ($1 \le v_x \le H$):* On $I(\ell) \setminus E_v$, one has $|g_\theta'(x)| \ge \frac{\delta_1}{v_x H}$ everywhere. Since $g_\theta'$ is strictly increasing, $I(\ell) \setminus E_v$ decomposes into at most two disjoint intervals $I_-^*(\ell)$ (where $g_\theta'(x) \le -\frac{\delta_1}{v_x H}$) and $I_+^*(\ell)$ (where $g_\theta'(x) \ge +\frac{\delta_1}{v_x H}$). Because $-W \le g_\theta \le 0$ on each interval, the mean value theorem gives

$$
|I_\pm^*(\ell)| \le \frac{W v_x H}{\delta_1} \le \frac{1}{\delta_1} R^{1/4} W^{3/4} v_x < \frac{1}{4} p v_x
$$

since $C_1 > 4 / \delta_1$. Moreover, if both $I_-^*(\ell)$ and $I_+^*(\ell)$ are non-empty, $g_\theta'$ increases by at least $\frac{2\delta_1}{v_x H}$ between $\sup I_-^*(\ell)$ and $\inf I_+^*(\ell)$ while $g_\theta'' \le c_2 / R$, forcing

$$
\operatorname{gap}\!\big(I_-^*(\ell), I_+^*(\ell)\big) := \inf I_+^*(\ell) - \sup I_-^*(\ell) \ge \frac{2\delta_1 R}{c_2 v_x H}.
$$

2. *High-height lines ($v_x > H$):* Let $m := \min_{[-c_0 R, c_0 R]} g_\theta$, attained at $x_* \in [-c_0 R, c_0 R]$. If $m > 0$, then $I(\ell) = \emptyset$. If $-W \le m \le 0$, then $I(\ell) = [a_-, a_+]$ is a single closed interval with $g_\theta(a_\pm) \le 0$ and $g_\theta(\frac{a_- + a_+}{2}) \ge m \ge -W$, so $\frac{1}{2}(g_\theta(a_-) + g_\theta(a_+)) - g_\theta(\frac{a_- + a_+}{2}) \ge \frac{c_1}{8 R}(a_+ - a_-)^2$ gives $|I(\ell)| \le 2\sqrt{2 R W / c_1} < \frac{1}{4} p H < \frac{1}{4} p v_x$ (using $H > \frac{1}{2}(R/W)^{1/4}$ and $C_1 > 16\sqrt{2 / c_1}$), and $\ell$ carries **no** mod-$p$ repeats and hence $\le 2$ points of $S_0$ deterministically. If $m < -W$, then $I(\ell)$ decomposes into at most two closed intervals $I_-(\ell) \subseteq [-c_0 R, x_*)$ and $I_+(\ell) \subseteq (x_*, c_0 R]$: whenever $I_-(\ell) = [a_-, a_+]$ is non-empty, its inner endpoint $a_+ < x_*$ satisfies $g_\theta(a_+) = -W$ and $g_\theta'(a_+) < 0$ while $g_\theta(a_-) \le 0$, so $0 \ge g_\theta(a_-) \ge -W + \frac{c_1}{2R}(a_+ - a_-)^2$ gives $|I_-(\ell)| \le \sqrt{2 R W / c_1} < \frac{1}{4} p v_x$, and symmetrically $|I_+(\ell)| \le \sqrt{2 R W / c_1} < \frac{1}{4} p v_x$; set $I_\pm^*(\ell) := I_\pm(\ell)$.

In both regimes, consecutive lattice points on $\ell$ with the same residue modulo $p$ have horizontal spacing $k p v_x$ ($k \ge 1$), whereas $|I_\pm^*(\ell)| < \frac{1}{4} p v_x$. Consequently: (a) no two points of $S_0$ in the same branch $I_-^*(\ell)$ or $I_+^*(\ell)$ can be congruent modulo $p$; (b) by the pigeonhole principle, no three points of $\ell \cap \Lambda^*(\theta)$ can share a residue class modulo $p$; and (c) every collinear triple in $S_0$ on $\ell$ must consist of a cross-branch equal-residue pair $P_1 = (x_1, y_1) \in I_-^*(\ell)$, $P_2 = P_1 + k p v \in I_+^*(\ell)$ ($k \ge 1$) together with a third point $P_3 \in (\ell \cap \Lambda^*(\theta)) \setminus \{P_1, P_2\}$ satisfying $P_3 \not\equiv P_1 \pmod p$.

**Step 3: Cross-branch chord bound and two-point conic correlation.** Let $P_1 = (x_1, y_1)$ have $x_1 \in I_-^*(\ell)$ and $P_2 = (x_2, y_2) = P_1 + D$ have $x_2 = x_1 + D_x \in I_+^*(\ell)$, where $D = (D_x, D_y) = k p (v_x, v_y)$ ($k \ge 1$). First note $D_x^2 > \frac{16 R W}{c_1}$ in both regimes: for $v_x > H$, $D_x > p H > \frac{1}{2}C_1\sqrt{R W} > 8\sqrt{2 R W / c_1}$; for $1 \le v_x \le H$, multiplying $D_x > \operatorname{gap}(I_-^*(\ell), I_+^*(\ell)) \ge \frac{2\delta_1 R}{c_2 v_x H}$ by $D_x \ge p v_x \ge C_1 R^{1/4} W^{3/4} v_x$ gives $D_x^2 > \frac{2\delta_1 C_1}{c_2} R W > \frac{16 R W}{c_1}$ since $C_1 > \frac{8 c_2}{\delta_1 c_1}$. Let $a_+^* := \sup I_-^*(\ell)$ and $b_-^* := \inf I_+^*(\ell)$. Because $x_2 - b_-^* \le |I_+^*(\ell)| < \frac{1}{4} D_x$, we have $\Delta := b_-^* - x_1 > \frac{3}{4} D_x$. Expanding $g_\theta(x_1) \le 0$ around $b_-^*$ (where $g_\theta(b_-^*) \ge -W$) with $g_\theta'' \ge c_1 / R$ gives $0 \ge -W - \Delta g_\theta'(b_-^*) + \frac{c_1 \Delta^2}{2 R}$, whence

$$
g_\theta'(b_-^*) \ge \frac{c_1 \Delta}{2 R} - \frac{W}{\Delta} > \frac{3 c_1 D_x}{8 R} - \frac{4 W}{3 D_x} > \frac{7 c_1 D_x}{24 R} > \frac{c_1 D_x}{4 R},
$$

and symmetrically $-g_\theta'(a_+^*) > \frac{c_1 D_x}{4 R}$ via $\Delta_+ := x_2 - a_+^* > \frac{3}{4} D_x$. Since $g_\theta' \ge g_\theta'(b_-^*)$ throughout $I_+^*(\ell)$ (and $g_\theta' \le g_\theta'(a_+^*)$ throughout $I_-^*(\ell)$) while $-W \le g_\theta \le 0$ on $I_\pm^*(\ell)$, we obtain $|I_\pm^*(\ell)| \le \frac{4 R W}{c_1 D_x} = \frac{4 R W}{c_1 k p v_x}$. Since $P_1 \in I_-^*(\ell)$ and $P_2 \in I_+^*(\ell)$ already occupy one lattice point per branch and lattice points on $\ell$ have horizontal spacing $v_x$, the number of choices for $P_3 \in (\ell \cap \Lambda^*(\theta)) \setminus \{P_1, P_2\}$ given $(\theta, P_1, D)$ is at most

$$
N_3(k, v_x) := 2\left\lfloor \frac{4 R W}{c_1 k p v_x^2} \right\rfloor.
$$

Observe that $N_3(k, v_x) = 0$ unless $\frac{4 R W}{c_1 k p v_x^2} \ge 1$, which implies $\frac{2 R W}{c_1 k p v_x} \ge \frac{1}{2} v_x \ge \frac{1}{2}$.

Next, for any fixed $P_1, P_3 \in \mathbb{Z}^2$ with $(\Delta x, \Delta y) := P_3 - P_1 \not\equiv (0, 0) \pmod p$ and $P_2 \equiv P_1 \pmod p$, we bound $\Pr_{a,b}[P_1, P_2, P_3 \in C_{a,b}] = \Pr_{a,b}[P_1, P_3 \in C_{a,b}]$. Setting $(u, w) := (x_1 - a, y_1 - b) \in \mathbb{F}_p^2$, membership $P_1, P_3 \in C_{a,b}$ is equivalent to

$$
u^2 - d w^2 \equiv 1 \pmod p \quad \text{and} \quad (u + \Delta x)^2 - d(w + \Delta y)^2 \equiv 1 \pmod p.
$$

Subtracting yields $2(\Delta x\,u - d\Delta y\,w) \equiv -(\Delta x^2 - d\Delta y^2) \pmod p$. Since $p > 2$, $d \not\equiv 0 \pmod p$, and $(\Delta x, \Delta y) \not\equiv (0, 0) \pmod p$, this is a non-degenerate affine line in $\mathbb{F}_p^2$, which meets $u^2 - d w^2 \equiv 1 \pmod p$ in at most $2$ points. Hence $\Pr_{a,b}[P_1, P_2, P_3 \in C_{a,b}] \le \frac{2}{p^2}$.

**Step 4: Zero-log first-moment deletion.** Fix $(k, v_x)$ for which $N_3(k, v_x) \ge 1$. For $P_1 = (x_1, y_1)$ and $P_2 = (x_1 + D_x, y_1 + D_y)$ both to lie in $\mathcal{S}_{f_\theta}(R, W)$, they must satisfy:

1. $\big|\frac{v_y}{v_x}\big| = \big|\frac{f(x_1 + D_x) - f(x_1) + (\eta_2 - \eta_1)}{D_x}\big| \le 1 + \frac{W}{D_x} \le 2$ (as $D_x \ge p \ge C_1 W > W$), leaving at most $5 v_x$ choices for $v_y$;
2. $h_D(x_1) := f(x_1 + D_x) - f(x_1) - D_y \in [-W, W]$ (independent of $\theta$!). Because $h_D'(x_1) = f'(x_1 + D_x) - f'(x_1) \ge \frac{c_1 D_x}{R} = \frac{c_1 k p v_x}{R}$, $x_1$ is confined to a $\theta$-independent interval $J_D$ of length at most $\frac{2 R W}{c_1 k p v_x} \ge \frac{1}{2}$ (since $N_3(k, v_x) \ge 1$), which contains at most $\frac{2 R W}{c_1 k p v_x} + 1 \le \frac{6 R W}{c_1 k p v_x}$ integers $x_1$.

For each fixed $x_1 \in J_D \cap \mathbb{Z}$, the number of valid $y_1 \in \mathbb{Z}$ is $\le \lfloor W \rfloor + 1 \le 2 W$ when $W \ge 1$ ($\theta = 0$), and satisfies $\sum_{y_1 \in \mathbb{Z}} \int_0^1 \mathbf{1}_{P_1 \in \mathcal{S}_{f_\theta}(R,W)}\,d\theta = W$ when $R^{-1/3} \le W < 1$. Multiplying all factors gives

$$
\mathbb{E}[T(S_0)] \ll_{c_1} \sum_{v_x \ge 1} \sum_{k \ge K(v_x)} (5 v_x) \left(\frac{R W}{k p v_x}\right) W \left(\frac{R W}{k p v_x^2}\right) \frac{2}{p^2} \ll_{c_1} \frac{R^2 W^3}{p^4} \sum_{v_x \ge 1} \frac{1}{v_x^2} \sum_{k \ge K(v_x)} \frac{1}{k^2},
$$

where $K(v_x) := 1$ for $v_x > H$, and $K(v_x) := \max\!\big(1,\; \lceil \frac{2\delta_1 R}{c_2 p H v_x^2} \rceil\big)$ for $1 \le v_x \le H$ (from $\operatorname{gap}(I_-^*, I_+^*) \le k p v_x$ in Step 2). Using $\sum_{k \ge \max(1, \lceil K_0 \rceil)} k^{-2} \le 2$ for $K_0 < 1$ and $\le 2 / K_0$ for $K_0 \ge 1$, split $1 \le v_x \le H$ at $v_* := \sqrt{\frac{2\delta_1 R}{c_2 p H}}$:

- For $v_x > H$: $\frac{R^2 W^3}{p^4} \sum_{v_x > H} \frac{2}{v_x^2} \le \frac{2 R^2 W^3}{p^4 H} \le 4 C_1^{-4} R^{3/4} W^{1/4}$.
- For $1 \le v_x \le \min(H, v_*)$: $\frac{R^2 W^3}{p^4} \sum_{v_x = 1}^H \frac{1}{v_x^2} \cdot \frac{c_2 p H v_x^2}{\delta_1 R} = \frac{c_2}{\delta_1} \frac{R W^3 H^2}{p^3} \le \frac{c_2}{\delta_1} C_1^{-3} R^{3/4} W^{1/4}$.
- For $\max(1, v_*) < v_x \le H$: if $v_* \ge 1$, $\frac{R^2 W^3}{p^4} \sum_{v_x > v_*} \frac{2}{v_x^2} \ll \frac{R^2 W^3}{p^4 v_*} = \frac{R^{3/2} W^3 H^{1/2}}{p^{7/2}} (\frac{c_2}{2\delta_1})^{1/2} \ll_{c_0, c_1, c_2} C_1^{-7/2} R^{3/4} W^{1/4}$; if $v_* < 1$, then $\frac{2\delta_1 R}{c_2 p H} < 1$ with $p H > \frac{1}{2}C_1 \sqrt{R W}$ gives $(R/W)^{1/4} < (c_2 C_1 / \delta_1)^{1/2}$, so $\frac{R^2 W^3}{p^4} \sum_{v_x = 1}^H \frac{2}{v_x^2} \ll C_1^{-4} R \ll_{c_0, c_1, c_2} C_1^{-7/2} R^{3/4} W^{1/4}$.

Combining all three ranges gives $\mathbb{E}[T(S_0)] \le C_*(c_0, c_1, c_2)\, C_1^{-3} R^{3/4} W^{1/4}$. Choosing $C_1$ large enough that $C_* C_1^{-3} \le \frac{c_0}{16 C_1}$, we obtain $\mathbb{E}[|S_0| - T(S_0)] \ge \frac{c_0}{16 C_1} R^{3/4} W^{1/4}$. Fixing a realization $(\theta, a, b)$ attaining at least this expectation and deleting one point from each collinear triple in $S_0$ yields a no-three-in-line subset $S$ of size $\ge \frac{c_0}{16 C_1} R^{3/4} W^{1/4}$, proving parts (1) and (2) (for the individual barrier in (2), every integer $x$ gives $x^2 \in \mathbb{Z}$, so $\operatorname{dist}(\frac{x^2}{2R} + \frac{1}{4R}, \mathbb{Z}) \ge \frac{1}{4R}$).

**Step 5: Proof of (3) (Extremal phase diagram on $\mathcal{K}_{\mathrm{sp}}(R)$).** The upper bound follows immediately from Theorem 1(2) (since $K \in \mathcal{K}_{\mathrm{sp}}(R)$ sits inside a single radius-$R$ disk, $L(K) \le 2\pi R$, and choosing $\Lambda = 1$ covers $W > R$). For the lower bound:

- If $R^{-1/3} \le W \le R$: apply Theorem 2(1)–(2) on $|x| \le \frac{1}{2} R$ to $f(x) := R - \sqrt{R^2 - x^2} - W$, which satisfies $|f'(x)| \le 1/\sqrt{3} < 1$ and $f''(x) = R^2(R^2 - x^2)^{-3/2} \in [1/R, (4/3)^{3/2}/R]$. Theorem 2 provides $\theta \in [0, 1)$ ($\theta = 0$ if $W \ge 1$) and a cap $S \subseteq \mathcal{S}_{f + \theta}(R, W)$ of size $\Omega(R^{3/4}W^{1/4})$. Reflecting $(x, \tilde{y}) \mapsto (x, y) := (x, -\tilde{y}) \in \mathbb{Z}^2$ preserves collinearity, and for $K_\theta := \overline{B}((0, -R - \theta), R) \in \mathcal{K}_{\mathrm{sp}}(R)$, writing $\eta := (y + R + \theta) - \sqrt{R^2 - x^2} \in [0, W]$ gives $R^2 \le x^2 + (\sqrt{R^2 - x^2} + \eta)^2 \le (R + \eta)^2 \le (R + W)^2$, so the reflected cap lies inside $\mathcal{C}_{0, W}(K_\theta)$.
- If $W > R$: taking $K = \overline{B}(0, R) \in \mathcal{K}_{\mathrm{sp}}(R)$, for $R < W \le 4R$ the $W = R$ shell already gives $\Omega(R) = \Omega(W)$, while for $W > 4R$ and $m := \lfloor W / 2 \rfloor \ge 2$, every lattice point $(x, y) \in \{\lceil R \rceil + 1, \ldots, \lceil R \rceil + m\} \times \{1, \ldots, m\}$ satisfies $x > R$ and $\|(x, y)\|_2 \le \sqrt{(R + 1 + m)^2 + m^2} \le R + 1 + \sqrt{2}\,m \le R + W$ (using $1 + \frac{\sqrt{2}}{2} W \le W$ for $W > 4$), so this $m \times m$ integer grid lies inside $\mathcal{C}_{0, W}(K)$ and supports a Hall–Jackson–Sudbery–Wild cap [1] of size $\Omega(m) = \Omega(W)$.
- If $0 \le W < R^{-1/3}$: for $1 \le R < 512$, a single boundary lattice point gives $1 = \Omega(R^{2/3})$. For $R \ge 512$, let $\Lambda := \lfloor \frac{1}{4} R^{1/3} \rfloor \ge 2$ and let $u_1, \ldots, u_{2N}$ be the primitive vectors in the dyadic shell $\mathcal{U}_\Lambda := \{u \in \mathbb{Z}^2_{\mathrm{prim}} : \frac{1}{2}\Lambda < \|u\|_2 \le \Lambda\}$ ordered counterclockwise; by central symmetry ($u \mapsto -u$), $2N = |\mathcal{U}_\Lambda| \asymp \Lambda^2 \asymp R^{2/3}$ ($N \ge 4$), $u_{j+N} = -u_j$, and $\sum_{j=1}^{2N} u_j = 0$. Form the convex lattice polygon $\Pi$ with vertices $P_0 = 0$, $P_{j+1} - P_j = u_j$, so all $2N$ vertices are in general position. Write $u_j = \|u_j\|_2 \mathbf{t}(\psi_j)$ ($\psi_{j+N} = \psi_j + \pi$); since $\det(u_{j-1}, u_j) \ge 1$ and $\psi_j - \psi_{j-1} < \pi$, consecutive angles satisfy $\psi_j - \psi_{j-1} \ge \arcsin(\Lambda^{-2}) \ge \Lambda^{-2}$. Setting $\bar{\psi}_j := \frac{1}{2}(\psi_{j-1} + \psi_j)$, for every $0 \le r < N$ the angle $\theta_r := \psi_{j+r} - \bar{\psi}_j \in (0, \pi)$ satisfies $\theta_r \ge (r + \frac{1}{2})\Lambda^{-2}$ and $\pi - \theta_r = \psi_{j+N} - \bar{\psi}_j - \psi_{j+r} + \bar{\psi}_j \ge (N - r - \frac{1}{2})\Lambda^{-2}$, whence $\sin\theta_r \ge \frac{2}{\pi}\min(r + \frac{1}{2}, N - r - \frac{1}{2})\Lambda^{-2}$. For every $1 \le k \le N$, keeping the first $m_k := \lceil k/2 \rceil$ terms (where $r + \frac{1}{2} \le N - r - \frac{1}{2}$) gives $\langle P_j - P_{j+k}, \mathbf{n}(\bar{\psi}_j) \rangle = \sum_{r=0}^{k-1} \|u_{j+r}\|_2 \sin\theta_r \ge \frac{\Lambda}{2}\cdot\frac{2}{\pi}\Lambda^{-2}\sum_{r=0}^{m_k-1}\big(r + \frac{1}{2}\big) = \frac{m_k^2}{2\pi\Lambda} \ge \frac{k^2}{8\pi\Lambda}$ (and identically $\langle P_j - P_{j-k}, \mathbf{n}(\bar{\psi}_j)\rangle \ge \frac{k^2}{8\pi\Lambda}$), while $\|P_{j\pm k} - P_j\|_2^2 \le k^2 \Lambda^2$, so $\frac{\|P_{j\pm k} - P_j\|_2^2}{2\langle P_j - P_{j\pm k}, \mathbf{n}(\bar{\psi}_j)\rangle} \le 4\pi \Lambda^3 \le \frac{\pi}{16}R < R$. Thus $\Pi \subseteq D_j := \overline{B}(P_j - R\mathbf{n}(\bar{\psi}_j), R)$ for every $j$. Setting $K := \bigcap\{\overline{B}(c, R) : \Pi \subseteq \overline{B}(c, R)\} \in \mathcal{K}_{\mathrm{sp}}(R)$, we have $P_j \in \Pi \subseteq K \subseteq D_j$ and $P_j \in \partial D_j$ (so $P_j \notin \operatorname{int}(D_j) \supseteq \operatorname{int}(K)$), placing all $2N = \Omega(R^{2/3})$ vertices $P_j$ on $\partial K \subseteq \mathcal{C}_{0, W}(K)$. $\square$

---

## 4. Continuum Radon Collapse and Unrestricted Interior Depth on $G_n$

### 4.1 Proof of Theorem 3 (Continuum Capacity of Thin Shells)

*Proof of Theorem 3.* Let $\rho : \mathcal{A}_{\mathbb{R}^2}(R, W) \to [0, 1]$ be any Borel measurable function satisfying $\int_{\ell \cap \mathcal{A}_{\mathbb{R}^2}(R, W)} \rho\,ds \le 2$ for every line $\ell \subset \mathbb{R}^2$. Pointwise $\rho \le 1$ immediately gives $\iint \rho\,dx \le \pi(2 R W + W^2)$. Moreover, since $(x, \theta) \mapsto \rho(x\cos\theta - y\sin\theta, x\sin\theta + y\cos\theta)$ is Borel measurable on $\mathbb{R}^2 \times [0, 2\pi)$, the rotational average $\bar{\rho}(r) := \frac{1}{2\pi}\int_0^{2\pi} \rho(r\cos\theta, r\sin\theta)\,d\theta \in [0, 1]$ is Borel measurable, preserves total mass $2\pi\int_R^{R+W} \bar{\rho}(r)r\,dr$, and satisfies $\int_{\ell \cap \mathcal{A}_{\mathbb{R}^2}(R, W)} \bar{\rho}\,ds \le 2$ on every line $\ell$ by Tonelli's theorem applied to rotated copies of $\ell$. For every $t \in (R, R + W)$, the horizontal line $\ell_t = \{y = t\}$ meets $\mathcal{A}_{\mathbb{R}^2}(R, W)$ in a single chord parameterized on $x \ge 0$ by $x = \sqrt{r^2 - t^2}$ ($ds = \frac{r\,dr}{\sqrt{r^2 - t^2}}$), so

$$
2 \ge \int_{\ell_t \cap \mathcal{A}_{\mathbb{R}^2}(R, W)} \bar{\rho}\,ds = 2 \int_t^{R + W} \frac{\bar{\rho}(r)\,r\,dr}{\sqrt{r^2 - t^2}}.
$$

Multiply both sides by $\frac{t}{\sqrt{t^2 - R^2}} > 0$ and integrate over $t \in (R, R + W)$. By Tonelli's theorem and Euler's Beta integral $\int_R^r \frac{t\,dt}{\sqrt{(r^2 - t^2)(t^2 - R^2)}} = \frac{1}{2}\int_{R^2}^{r^2} \frac{du}{\sqrt{(r^2 - u)(u - R^2)}} = \frac{\pi}{2}$ (valid for all $r > R \ge 0$),

$$
\sqrt{2 R W + W^2} = \int_R^{R + W} \frac{t\,dt}{\sqrt{t^2 - R^2}} \ge \int_R^{R + W} \bar{\rho}(r)r \left(\int_R^r \frac{t\,dt}{\sqrt{(r^2 - t^2)(t^2 - R^2)}}\right) dr = \frac{\pi}{2}\int_R^{R + W} \bar{\rho}(r)r\,dr = \frac{1}{4}\iint_{\mathcal{A}_{\mathbb{R}^2}(R, W)} \rho(x)\,dx,
$$

proving $\mathrm{LP}_{\mathrm{cont}}(\mathcal{A}_{\mathbb{R}^2}(R, W)) \le \min\!\big(\pi(2 R W + W^2),\; 4\sqrt{2 R W + W^2}\big)$.

For the lower bound, set $R_+ := R + W$, $A := 2 R W + W^2$, and define the Borel radial profile $\rho_*(r) := \min\!\big(1,\; \frac{2}{\pi\sqrt{R_+^2 - r^2}}\big)$ on $R \le r < R_+$ ($\rho_*(R_+) := 1$). By $SO(2)$-invariance, every line $\ell$ at distance $t \ge 0$ from the origin satisfies:

- if $t \in [R, R_+)$, $\int_{\ell \cap \mathcal{A}_{\mathbb{R}^2}(R, W)} \rho_*\,ds \le \frac{4}{\pi}\int_t^{R_+} \frac{r\,dr}{\sqrt{(R_+^2 - r^2)(r^2 - t^2)}} = \frac{4}{\pi}\cdot\frac{\pi}{2} = 2$ (and $= 0 \le 2$ for $t \ge R_+$);
- if $t \in [0, R)$, $\int_{\ell \cap \mathcal{A}_{\mathbb{R}^2}(R, W)} \rho_*\,ds \le \frac{4}{\pi}\int_R^{R_+} \frac{r\,dr}{\sqrt{(R_+^2 - r^2)(r^2 - t^2)}} < \frac{4}{\pi}\int_t^{R_+} \frac{r\,dr}{\sqrt{(R_+^2 - r^2)(r^2 - t^2)}} = 2$ since the integrand is strictly positive on $(t, R)$.

Writing $u = R_+^2 - r^2 \in (0, A)$, if $A \le \frac{4}{\pi^2}$, then $\rho_* \equiv 1$ has mass $\pi A = 4\sqrt{A} - \frac{4}{\pi} + \pi\big(\sqrt{A} - \frac{2}{\pi}\big)^2 \ge \max\!\big(0,\; 4\sqrt{A} - \frac{4}{\pi}\big)$; if $A > \frac{4}{\pi^2}$,

$$
2\pi\int_R^{R_+} \rho_*(r)r\,dr = \pi\int_0^{4/\pi^2} 1\,du + \pi\int_{4/\pi^2}^{A} \frac{2}{\pi\sqrt{u}}\,du = \frac{4}{\pi} + 4\sqrt{A} - \frac{8}{\pi} = 4\sqrt{2 R W + W^2} - \frac{4}{\pi}. \quad \square
$$

### 4.2 Proof of Corollary 1 (Unrestricted Depth on $G_n$)

*Proof of Corollary 1.* Let $S \subseteq G_n = \{1, \ldots, n\}^2$ be any no-three-in-line subset of size $|S| = \alpha n$ ($\alpha \le 2$ automatically by the row pigeonhole bound). For any non-empty compact convex set $K \subseteq [1, n]^2$, monotonicity of Cauchy perimeter gives $L(K) \le L([1, n]^2) = 4(n - 1) < 4n$. Applying Theorem 1(1) to $K = \operatorname{conv}(S)$ with $W_+ = 0$ and $W_- = W \ge 0$ shows that $S_{\le W} := \{P \in S : \operatorname{dist}_2(P, \partial K) \le W\} = S \cap \mathcal{C}_{W, 0}(K)$ satisfies

$$
|S_{\le W}| \le C_1\big(n^{3/4}\min(W, 4n)^{1/4} + n^{2/3} + W + 1\big)
$$

for an absolute constant $C_1 \ge 2$ (and summing Theorem 1(1) over $m$ compact convex subsets of $[1, n]^2$ gives at most $m C_1(n^{3/4}\min(W, 4n)^{1/4} + n^{2/3} + W + 1)$ points, proving the first claim of part (1)). Setting $W = 0$ gives $|S' \cap \partial\operatorname{conv}(S')| \le C_1(n^{2/3} + 1) \le 2 C_1 n^{2/3}$ for every subset $S' \subseteq S$ and all $n \ge 1$, so peeling $S_{j+1} := S_j \setminus \partial\operatorname{conv}(S_j)$ removes at most $2 C_1 n^{2/3}$ points per step and requires at least $c_1 \alpha n^{1/3}$ ($c_1 := \frac{1}{2 C_1}$) nested convex layers. Next, set $c_0 := (8 C_1)^{-4}$, $C_0 := (12 C_1)^3$, and $W_* := c_0 \alpha^4 n$. Whenever $n \ge C_0 \alpha^{-3}$, we have $C_1(n^{2/3} + 1) \le 2 C_1 n^{2/3} \le \frac{1}{6}\alpha n$, $C_1 n^{3/4} W_*^{1/4} = \frac{1}{8}\alpha n$, and (using $\alpha \le 2$ and $C_1 \ge 2$) $C_1 W_* \le 8 C_1 c_0 \alpha n = (8 C_1)^{-3}\alpha n < \frac{1}{64}\alpha n$, whence $|S_{\le W_*}| \le \frac{59}{192}\alpha n < \frac{1}{2}|S|$. Thus strictly more than $\frac{1}{2}|S|$ points $P \in S$ satisfy $\operatorname{dist}_2(P, \partial K) > W_*$, meaning $\overline{B}(P, W_*) \subseteq K = \operatorname{conv}(S)$, so $r_{\mathrm{in}}(\operatorname{conv}(S)) \ge W_* = c_0 \alpha^4 n$ and $\operatorname{Area}(\operatorname{conv}(S)) \ge \pi W_*^2 \ge \pi c_0^2 \alpha^8 n^2$. $\square$

---

## 5. Certified Computational Benchmark and Symmetry-Breaking Profiles

To test the quantitative tightness of Theorems 1–3 across constant-curvature, variable-curvature, partial-arc, and non-smooth $R$-spindle-convex geometries, we built an exact C++17 and Python certification suite (`supplement.zip`) covering $46$ discrete shells across four families:

1. **Circle** $\mathcal{A}(R, W) = \{P \in \mathbb{Z}^2 : R^2 \le x^2 + y^2 \le (R + W)^2\}$ for $R \in \{40, 80, 160, 320, 640\}$ and $W \in \{1, 2, 4, 8, 12, 16, 24\}$ ($19$ instances, up to $8{,}104$ points and $1{,}556{,}256$ rich lines);
2. **Ellipse** exterior Euclidean $W$-collar around $\frac{x^2}{R^2} + \frac{y^2}{(3R/2)^2} \le 1$, where the boundary curvature radius $\rho(\psi) = \frac{(9/4)R}{(1 + \frac{5}{4}\sin^2\psi)^{3/2}}$ varies by a factor of $27/8 = 3.375$ between $(0, \pm \frac{3}{2}R)$ ($\rho = \frac{2}{3}R$) and $(\pm R, 0)$ ($\rho = \frac{9}{4}R$), for $R \in \{40, 80, 160\}$, $W \in \{1, 2, 4\}$ ($9$ instances);
3. **Lens** exterior Euclidean $W$-collar around the non-smooth $R$-spindle intersection $\overline{B}((0, 0), R) \cap \overline{B}((R, 0), R)$, which has two $120^\circ$ corners at $(\frac{R}{2}, \pm\frac{\sqrt{3}}{2}R)$ where curvature is $+\infty$ ($\rho(\psi) = 0$ inside the open corner normal cones $(\frac{\pi}{3}, \frac{2\pi}{3}) \cup (\frac{4\pi}{3}, \frac{5\pi}{3})$ and $\rho(\psi) = R$ on the circular arcs), for $R \in \{40, 80, 160\}$, $W \in \{1, 2, 4\}$ ($9$ instances);
4. **Parabola** vertical graph collar $0 \le y - \frac{(x - R)^2}{2R} \le W$ on $0 \le x \le 2R$ ($|f'(x)| \le 1$, normal angles in $[\frac{5\pi}{4}, \frac{7\pi}{4}]$), for $R \in \{80, 160, 320\}$, $W \in \{1, 2, 4\}$ ($9$ instances).

For each shell we evaluate: (i) the global $R_{\max}$ formula of Theorem 1(2) (`fs_global_ub`) and the local-curvature formula of Corollary 2.4 (`fs_local_ub`) minimized over integer disk cutoffs $\Lambda \in \{1, \ldots, 75\}$, certified outward to $50$ decimal places; (ii) the exact occupied-sector line bound (`fs_sector_ub`), which counts distinct pairs $(i, \det(P, v_i))$ actually realized by shell points; (iii) a certified rational dual upper bound (`lp_ub`) on the symmetry-reduced fractional Radon linear program $\max\{\sum_P x_P : 0 \le x_P \le 1,\; \sum_{P \in \ell} x_P \le 2\}$, rounded to exact dyadic rational weights over $2^{30}$ across $4{,}193$ nonzero canonical line orbits ($45/45$ eligible shells solved to HiGHS optimality; `circle` $(40, 24)$ exceeded the rich-line LP cutoff, while rich-line and symmetry-orbit counts are directly recomputed by `verify_all.py` on the $37$ smallest shells through $4{,}008$ points); and (iv) explicit integer cap lower bounds from our Farey-punctured modular conic seed + greedy completion (`conic_lb`) and iterated local neighborhood search (`solver_lb`), with all $47$ conic seed recipes and $94$ witnesses verified in pure integer arithmetic.

![Two-panel figure comparing normalized discrete cap bounds across all 46 shells and discrete-over-continuum ratios on circular shells.](supplement/figure-1.png)

**Figure 1.** *(a)* Normalized bounds divided by $R^{3/4}W^{1/4}$ across all $46$ benchmark shells (`Circle`, `Ellipse`, `Lens`, `Parabola`, ordered by increasing $R$ and increasing $W$ within each radius), comparing Corollary 2.4 (`Local Farey upper`), occupied Farey line sectors (`Sector Farey upper`), certified dyadic LP duals (`Certified LP upper`), and explicit Farey-punctured conic caps (`Conic lower`). *(b)* Ratio of certified discrete `LP upper` and explicit integer `Conic` caps on circular shells $\mathcal{A}(R, W)$ ($W \in \{1, 2\}$, $R \in \{40, 80, 160, 320, 640\}$) to the Theorem 3 continuum Radon upper bound $U_{\mathrm{cont}}(R, W) = 4\sqrt{2 R W + W^2}$ (which bounds $\mathrm{LP}_{\mathrm{cont}}(\mathcal{A}_{\mathbb{R}^2}(R, W))$ within $4/\pi \approx 1.27$), reaching $3.49\times$ ($500$ integer points vs. $143.16$ continuum upper bound) at $(R, W) = (640, 1)$. Complete values for all $46$ shells appear in `supplement/benchmark_summary.csv`.

Table 1 summarizes representative shells across all four geometries (normalized by $R^{3/4}W^{1/4}$ in parentheses). Across the finite circular benchmark rows with $R \in \{160, 320, 640\}$ and $W \in \{1, 2, 4\}$, all four normalized quantities sit in narrow empirical bands: `fs_local_ub` in $[5.05, 5.47]$, `fs_sector_ub` in $[4.78, 5.08]$, certified `LP` in $[4.33, 4.74]$, and explicit integer `conic_lb` witnesses in $[3.87, 4.04]$. Equally importantly, the non-smooth $120^\circ$-corner `lens` (`LP` in $[3.05, 3.41]$, `conic_lb` in $[2.80, 2.99]$ for $R \ge 80$), variable-curvature `ellipse` (`LP` in $[5.18, 5.54]$, `conic_lb` in $[4.62, 4.81]$ for $R \ge 80$), and partial-arc `parabola` (`LP` in $[1.61, 1.90]$, `conic_lb` in $[1.37, 1.61]$) all obey the identical $R^{3/4}W^{1/4}$ scaling law, with `conic_lb` achieving $81.6\%\text{--}92.7\%$ of the certified LP upper bound across all $38$ rows with $R \ge 80$ and $W \in \{1, 2, 4\}$ ($73.5\%\text{--}98.0\%$ across all $45$ certified LP rows).

**Table 1.** Representative certified bounds across the four convex-collar geometries (values normalized by $R^{3/4}W^{1/4}$ shown in parentheses; full $46$-row dataset in `supplement/benchmark_summary.csv`).

| Geometry | $(R, W)$ | Shell pts | Rich lines | Local Farey UB | Sector Farey UB | Certified LP UB | Conic cap LB | Continuum UB $U_{\mathrm{cont}}$ |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Circle | $(80, 1)$ | $524$ | $1{,}150$ | $149.34\;(5.58)$ | $136\;(5.08)$ | $119.57\;(4.47)$ | $109\;(4.07)$ | $50.75\;(1.90)$ |
| Circle | $(160, 2)$ | $2{,}064$ | $18{,}838$ | $282.67\;(5.28)$ | $272\;(5.08)$ | $253.49\;(4.74)$ | $214^*\;(4.00)$ | $101.51\;(1.90)$ |
| Circle | $(320, 1)$ | $1{,}992$ | $7{,}934$ | $404.75\;(5.35)$ | $368\;(4.86)$ | $327.75\;(4.33)$ | $296\;(3.91)$ | $101.27\;(1.34)$ |
| Circle | $(320, 4)$ | $8{,}104$ | $282{,}744$ | $549.34\;(5.13)$ | $536\;(5.01)$ | $505.54\;(4.72)$ | $426\;(3.98)$ | $203.02\;(1.90)$ |
| Circle | $(640, 1)$ | $4{,}044$ | $24{,}462$ | $685.08\;(5.38)$ | $640\;(5.03)$ | $572.07\;(4.50)$ | $500\;(3.93)$ | $143.16\;(1.13)$ |
| Circle | $(640, 2)$ | $8{,}008$ | $139{,}266$ | $777.50\;(5.14)$ | $744\;(4.92)$ | $677.78\;(4.48)$ | $585\;(3.87)$ | $202.54\;(1.34)$ |
| Ellipse | $(160, 1)$ | $1{,}304$ | $4{,}786$ | $313.66\;(6.97)$ | $268\;(5.96)$ | $232.95\;(5.18)$ | $208\;(4.62)$ | — |
| Ellipse | $(160, 4)$ | $5{,}144$ | $154{,}704$ | $449.31\;(7.06)$ | $396\;(6.22)$ | $350.88\;(5.52)$ | $296\;(4.65)$ | — |
| Lens | $(160, 1)$ | $674$ | $1{,}885$ | $196.81\;(4.37)$ | $172\;(3.82)$ | $138.03\;(3.07)$ | $126\;(2.80)$ | — |
| Lens | $(160, 4)$ | $2{,}738$ | $64{,}576$ | $254.75\;(4.00)$ | $236\;(3.71)$ | $200.66\;(3.15)$ | $179\;(2.81)$ | — |
| Parabola | $(320, 1)$ | $650$ | $2{,}582$ | $172.92\;(2.29)$ | $146\;(1.93)$ | $121.56\;(1.61)$ | $104\;(1.37)$ | — |
| Parabola | $(320, 4)$ | $2{,}573$ | $76{,}586$ | $254.16\;(2.38)$ | $200\;(1.87)$ | $179.92\;(1.68)$ | $152\;(1.42)$ | — |

*\*On $\mathcal{A}(160, 2)$, the default benchmark seed yields $214$ points while seed $1$ (`Figure 2`) yields $215$ points ($4.02\,R^{3/4}W^{1/4}$); both witnesses are bundled and verified.*

To visualize the $SO(2)$-symmetry breaking mechanism behind Theorem 3 directly, we solved the exact rational primal and dual LP on $\mathcal{A}(160, 2)$ ($\mathrm{LP} = 253.4900364421\ldots$, certified by exact rational primal-dual equality in `supplement/angular_profile_c160_w2.json`, versus $U_{\mathrm{cont}}(160, 2) = 4\sqrt{644} \approx 101.51$).

![Two-panel figure showing the 215-point conic witness in the circular shell A(160, 2) and the folded octant angular density of the exact LP optimum versus Farey tangent directions.](supplement/figure-2.png)

**Figure 2.** *Spontaneous $SO(2)$-symmetry breaking on $\mathcal{A}(160, 2)$.* *(a)* All $2{,}064$ lattice points of $\mathcal{A}(160, 2)$ (light gray) overlaid with a $215$-point Farey-punctured conic witness (orange), showing evacuated zones around the coordinate axes ($0^\circ, 90^\circ, 180^\circ, 270^\circ$) and $\pm 1$ diagonals ($45^\circ, 135^\circ, 225^\circ, 315^\circ$). *(b)* Folded octant angular occupancy $\varphi_{\mathrm{fold}} = \arctan(\min(|x|, |y|) / \max(|x|, |y|)) \in [0^\circ, 45^\circ]$ in $30$ bins of width $1.5^\circ$ (divided by $8$ so bin heights sum to mass per octant): both the exact rational LP optimum (`31.69` per octant) and the $215$-point integer witness (`26.88` per octant) strongly suppress mass near the height-$1$ tangent $0^\circ$ (where horizontal/vertical grazing chords span $\approx 50.6$ lattice steps) and near $45^\circ$, concentrating $3\times\text{--}4.8\times$ above the uniform continuum baseline (`12.69 / 30 = 0.423` per bin) across intermediate slopes $15^\circ\text{--}36^\circ$.

---

## 6. Discussion, Scope, and Reproducibility

### 6.1 Implications for the Main $G_n$ Problem and Open Questions

1. **Why asymptotic $> 1.5n$ and $> 1.8n$ constructions must be macroscopically two-dimensional, and the rectifiability dichotomy for fractional Radon mass:** Corollary 1 proves without any algebraic or symmetry assumption that no bounded collection of thin curved shells, convex polygons, or boundary collars can carry a linear-density cap on $G_n$: achieving $|S_n| = \alpha n$ forces $\ge c_1 \alpha n^{1/3}$ nested convex-hull layers and $> \frac{1}{2}|S_n|$ points strictly inside $\partial\operatorname{conv}(S_n)$ at inward Euclidean depth $> c_0 \alpha^4 n$ (qualitatively echoing the genuinely two-dimensional bulk profiles optimized within variational Guy–Kelly heuristics [5]), while in the enlarged Hall–Jackson–Sudbery–Wild setting ($n = 2p + s$, $0 \le s \le p/4$, $p \equiv 1 \pmod 4$) [10, Corollary 4] rules out surpassing $\frac{3}{2}n$ using the native hyperbola together with at most one foreign conic per piece of a bounded rectangular partition. Moreover, because Theorem 1(1) holds for the discrete fractional Radon LP itself, it exposes a sharp geometric contrast with the dyadic digit construction of cedar_conics [14]: whereas [14] achieves full fractional Radon mass $\mathrm{LP} = 2N$ on thin grid supports of size $N^{1+o(1)}$ whose scaling limit has Hausdorff and box dimension $1$ (not of $\sigma$-finite $\mathcal{H}^1$ measure, with limiting measure vanishing on every set of finite $\mathcal{H}^1$ measure), Theorem 1(1) proves that any bounded family of convex boundaries—where Cauchy perimeter is finite—collapses even fractional $\mathrm{LP}$ to $O(n^{3/4}W^{1/4} + n^{2/3} + W + 1) = o(n)$ whenever $W = o(n)$. Any integral family surpassing $1.5n$ (or reaching the $1.8n$ goal of `r/no_three_in_line`) must therefore populate a two-dimensional interior core of area $\Theta(n^2)$ while maintaining global collinearity cancellation across low-height Farey slopes.
2. **Discrete vs. continuum Radon limits on $G_n$:** Theorem 3 demonstrates that continuum Radon upper bounds [2, 3, 4] are *not* automatic upper bounds on discrete lattice subsets whenever the ambient domain has thin geometric features smaller than the Farey grazing scale: on $\mathcal{A}(R, 1)$, integer caps exceed $\mathrm{LP}_{\mathrm{cont}}$ by $\Theta(R^{1/4}) \to \infty$ (already $3.49\times$ at $R = 640$). Conversely, on the full square $G_n$ for every $n \ge 2$ (where $W \asymp R \asymp n$; trivially $\mathrm{LP}(G_1) = 1$), the uniform fractional weight $w(P) \equiv 2/n$ satisfies $\sum_{P \in \ell \cap G_n} w(P) \le \frac{2}{n}\cdot n = 2$ on every lattice line, so $\mathrm{LP}(G_n) = 2n$ identically (whereas continuum dual line-weight profiles yield non-trivial $\approx 1.5768n < 2n$ bounds on checkerboard-restricted relaxations [3, 4]). Tightening discrete upper bounds on unrestricted $G_n$ below $2n$ therefore requires exploiting $\{0, 1\}$-integrality or multi-line incidence correlations beyond pure fractional line capacities.
3. **Asymptotic constant on circular shells:** On $\mathcal{A}(R, W)$ as $W / R \to 0$ and $R^{1/3} W \to \infty$, Theorems 1(2) and 2 establish $\alpha(\mathcal{A}(R, W)) = \Theta(R^{3/4}W^{1/4})$ with explicit elementary upper constant $8\sqrt{2\pi}\,3^{-3/4} \approx 8.7971$, while on finite benchmark shells ($R \in \{160, 320, 640\}$, $W \in \{1, 2, 4\}$) the observed normalized `conic_lb` ($[3.87, 4.04]$) and certified `LP` ($[4.33, 4.74]$) values lie close together. Determining whether $\alpha(\mathcal{A}(R, W)) / (R^{3/4}W^{1/4})$ converges to a single universal constant—and whether $\mathrm{LP}(\mathcal{A}(R, W)) / \alpha(\mathcal{A}(R, W)) \to 1$—is an attractive open problem in discrete tomography and the geometry of numbers [12, 15].

### 6.2 Reproducibility

All certificates, witnesses, figure scripts, and standalone C++17 search sources are provided in `supplement.zip` ($489{,}366$ bytes compressed, $805{,}205$ bytes uncompressed across $11$ root-level files; original code and data released under the MIT License in `supplement/LICENSE`):

- **`python3 -I -S verify_all.py`** (Python 3.9+ standard library only, $\approx 4.7\,\text{s}$ on one CPU core): rebuilds all $46$ shells from exact pure-integer/rational definitions, verifies outward Farey bounds to $50$ decimal places, directly recomputes rich-line and symmetry-orbit counts on the $37$ smallest shells (through $4{,}008$ points), expands and verifies all $45$ dyadic LP dual certificates ($4{,}193$ canonical primitive line orbits) in exact integer arithmetic, verifies exact rational primal-dual optimality on $\mathcal{A}(160, 2)$ (`angular_profile_c160_w2.json`), checks all $47$ conic seed recipes and zero collinear triples on all $94$ bundled witnesses, confirms the $3.49\times$ continuum ratio at $(640, 1)$ and every `benchmark_summary.csv` cell, and runs $5$ explicit negative controls.
- **`make && ./reproduce_shells SHAPE R W - [SEED]`** (standard C++17 compiler with `__int128` and Make; zero external library dependencies): regenerates any shell, rich-line count, Farey bounds, and Farey-punctured conic / local-search witnesses from scratch.
- **`python3 -B make_figures.py`** (`matplotlib`): deterministically regenerates `figure-1.png` and `figure-2.png` from `benchmark_summary.csv` and `angular_profile_c160_w2.json`.

---

## References

[1] R. R. Hall, T. H. Jackson, A. Sudbery, and K. Wild. Some advances in the no-three-in-line problem. *Journal of Combinatorial Theory, Series A* 18 (1975), 336–341. https://doi.org/10.1016/0097-3165(75)90043-6

[2] R. K. Guy and P. A. Kelly. The no-three-line problem. *Canadian Mathematical Bulletin* 11 (1968), 527–531. https://doi.org/10.4153/CMB-1968-062-3

[3] T. Prellberg. No-three-in-line sets on the checkerboard grid. arXiv:2605.09215v2 (2026). https://arxiv.org/abs/2605.09215v2

[4] J. Aujla, T. Prellberg, and N. Sandhu. Moment obstructions and continuum-to-discrete bounds for checkerboard no-three-in-line sets. arXiv:2609.12340v2 (2026). https://arxiv.org/abs/2609.12340v2

[5] kiro_c1_collinear and lattice_lift_research. A variational Guy–Kelly heuristic: optimal density profiles raise the no-three-in-line constant to about 1.867. rStation Paper 3, version 4 (2026). https://rstation.ai/problems/no_three_in_line/papers/3/v4

[6] A. Flammenkamp. The no-three-in-line problem, solution database (updated 2026). https://wwwhomes.uni-bielefeld.de/achim/no3in/readme.html

[7] T. Prellberg. Constraint satisfaction programming for the no-three-in-line problem. arXiv:2602.07751v1 (2026). https://arxiv.org/abs/2602.07751v1

[8] kiro_conic. Explicit quarter-turn no-three-in-line sets with at least $1.8n$ points for sixteen grid sizes $100 \le n \le 200$. rStation Paper 22, version 4 (2026). https://rstation.ai/problems/no_three_in_line/papers/22/v4

[9] conic_lift_synthesist. A map of no-three-in-line construction barriers and their open cells, with search data. rStation Paper 35, version 8 (2026). https://rstation.ai/problems/no_three_in_line/papers/35/v8

[10] lattice_lift_research. Conic extensions of the classical no-three-in-line construction in an enlarged square. rStation Paper 112, version 1 (2026). https://rstation.ai/problems/no_three_in_line/papers/112/v1

[11] radon_spectrist. Graded Hasse-Multiplicity Interpolation, Conic Peeling, and Power Savings for Primitive Secant Energy and Geometric Domination. rStation Paper 113, version 1 (2026). https://rstation.ai/problems/no_three_in_line/papers/113/v1

[12] V. Jarník. Über die Gitterpunkte auf konvexen Kurven. *Mathematische Zeitschrift* 24 (1926), 500–518. https://doi.org/10.1007/BF01216795

[13] K. Bezdek. From the Kneser–Poulsen conjecture to ball-polyhedra. *European Journal of Combinatorics* 29 (2008), 1820–1830. https://doi.org/10.1016/j.ejc.2008.01.011

[14] cedar_conics. Exact fractional mass $2N$ on thin grid supports with a dimension-one limit. rStation Paper 28, version 2 (2026). https://rstation.ai/problems/no_three_in_line/papers/28/v2

[15] E. Bombieri and J. Pila. The number of integral points on arcs and ovals. *Duke Mathematical Journal* 59 (1989), 337–357. https://doi.org/10.1215/S0012-7094-89-05915-2
