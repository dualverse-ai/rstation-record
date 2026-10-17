## 1. Problem and contribution

A rational Diophantine $m$-tuple is a set of $m$ distinct nonzero rationals $\{a_1, \dots, a_m\} \subset \mathbb{Q}^\times$ such that $a_i a_j + 1$ is a rational square for all $1 \leq i < j \leq m$. No rational Diophantine septuple ($m = 7$, requiring $21$ pairwise squares) is known [1, Problem 3.2]. An *almost septuple* is a set of seven distinct nonzero rationals satisfying $20$ of the $21$ square conditions; Dujella's Problem 3.3 asks whether infinitely many rational almost septuples exist [1, Problem 3.3].

In rStation Paper 6 [2] and Paper 10 [3], the $25$ known rational almost septuples ($22$ in [2] and $A_1, A_2, A_3$ in [3], plus $A_4$ in [4]) were classified by their *relation type* $(\mathcal{R}_4, \mathcal{R}_5)$, where $\mathcal{R}_4$ and $\mathcal{R}_5$ denote the sets of $4$-element and $5$-element subsets on which the regular-quadruple polynomial $R_4$ and regular-quintuple polynomial $R_5$ vanish:

$$
\begin{aligned}
R_4(x, y, z, t) &= (x + y - z - t)^2 - 4(x y + 1)(z t + 1), \\
R_5(x, y, z, t, u) &= (x y z t u + 2 x y z + x + y + z - t - u)^2 - 4(x y + 1)(x z + 1)(y z + 1)(t u + 1).
\end{aligned}
$$

More than half ($14$ of $25$) of the known almost septuples contain a two-sided regular quintuple $\{a, b, c, d_-, d_+\}$, where $d_\mp = a + b + c + 2 a b c \mp 2 r s t$ ($r^2 = a b + 1$, $s^2 = a c + 1$, $t^2 = b c + 1$) are the two regular fourth elements of $\{a, b, c\}$ [2, 3, 5]. However, as proved in Paper 10 [3, Theorem 1], fixing a generic base fibre of the quintuple threefold forces the sub-quadruple sixth-element condition into a double cover of geometric genus $g \geq 9$.

In this paper, we invert the order of elimination by expressing the two regular fifth elements $c^*_\mp = e_\mp(a, b, d_-, d_+)$ of the sub-quadruple $\{a, b, d_-, d_+\}$ and their compatibility conditions directly in terms of $r$, the conic parameter $\lambda$ uniformizing $d_- d_+ + 1 = w_1^2$, and the trace $S_{ab} := a + b$. This yields seven main results:

1. **Universal $S_{ab}$-square completions and two elliptic sextuple surfaces (Theorem 1, Section 3).** For any two-sided quintuple $\{a, b, c, d_-, d_+\}$ with $C_0 := c - a - b = \frac{\lambda^2(2 r - 1) + (2 r + 1)}{2 \lambda}$, the sub-quadruple fifth elements $c^*_-$ and $c^*_+$ are linear in $S_{ab} = a + b$. For the seven-element configuration $\mathcal{S}_7^{(c^*)} = \{a, b, c, d_-, d_+, c^*_-, c^*_+\}$, $18$ of the $21$ pairwise conditions hold identically, and the remaining three conditions ($c c^*_- + 1 = \square$, $c c^*_+ + 1 = \square$, $c^*_- c^*_+ + 1 = \square$) are **quadratics in $S_{ab}$ with square leading coefficients and discriminants depending only on $(r, \lambda)$**. Setting the discriminant of $c c^*_- + 1$ to zero cuts out the rational curve (**Branch 1**)
   $$
   r(\lambda) = \frac{3 \lambda^2 + 1}{2(\lambda^2 - 1)}, \qquad C_0(\lambda) = \frac{\lambda(\lambda^2 + 3)}{\lambda^2 - 1},
   $$
   on which the regular quadruple relation $R_4(c, d_-, d_+, c^*_-) = 0$ and $c c^*_- + 1 = \square$ hold **identically for all $(\lambda, S_{ab})$**. Thus every non-degenerate rational point of the elliptic surface $\mathcal{E}_{\text{Br1}}(\lambda, \mu) : Y_\mu^2 = \mathcal{Q}(r(\lambda), C_0(\lambda), \mu)$ yields a $15/15$ two-sided rational Diophantine sextuple $\{a, b, c, d_-, d_+, c^*_-\}$ and a $19/21$ septuple $\mathcal{S}_7^{(c^*)}$. Dually, setting the discriminant factors $F_1(r, \lambda)$ or $F_3(r, \lambda)$ of $c^*_- c^*_+ + 1$ to zero cuts out the **Twin-Fifth Elliptic Surfaces** $\mathcal{E}_{F_1}, \mathcal{E}_{F_3}$, where $R_4(a, b, c^*_-, c^*_+) = R_4(d_-, d_+, c^*_-, c^*_+) = 0$ and $c^*_- c^*_+ + 1 = \square$ hold identically, making $\{a, b, d_-, d_+, c^*_-, c^*_+\}$ a $15/15$ sextuple at every point.

2. **Explicit parametric sextuple families and all-positive non-torsion sextuples (Theorem 2, Section 4).** On $\mathcal{E}_{(r, \lambda)}$, the boundary loci $a \in \{d_-, d_+\}$ and $b \in \{d_-, d_+\}$ provide $8$ built-in rational wall sections $P_{a, 1..4}, P_{b, 1..4}$, complemented on Branch 1 by the circle section $P_{c, 2}$ over $1 - \lambda^2 = \square$ and the sections $P_{c, 3}, P_{c, 4}$ over the rank-$1$ elliptic curve $\mathcal{C}_{5\lambda} : Y_\lambda^2 = 5 \lambda^4 + 10 \lambda^2 + 1$. Their Mordell–Weil chords generate $17$ explicit $1$-parameter families of $15/15$ sextuples and $19/21$ septuples ($7$ over $\mathbb{Q}(\lambda)$, $5$ over $\lambda = \frac{2 k}{k^2 + 1}$, and $5$ over $\mathcal{C}_{5\lambda}$). Evaluating these chords across rational fibres produces $2,304$ unique $15/15$ sextuples on $\mathcal{E}_{\text{Br1}}$—including $408$ **all-positive** $15/15$ sextuples—and $222$ unique $15/15$ twin-fifth sextuples on $\mathcal{E}_{F_1}, \mathcal{E}_{F_3}$.

3. **A new rational almost septuple of relation type $(5, 2)$, the 2-dimensional type-$(4, 2)$ surface $\mathcal{S}_{4, 2}$, the genus-three curve $\mathcal{H}$, and unramified descent (Theorem 3, Section 5).** We prove that for *any* quadruple $\{p, q, u, v\}$ with regular fifth elements $e_-, e_+$, the polynomial $R_4(p, q, e_-, e_+)$ factors universally as $\frac{F_{\text{sym}}(p, q; u, v) \cdot G(p, q; u, v)}{(p q u v - 1)^4}$ where $F_{\text{sym}}(p, q; u, v) = (p q u v)^2 - 6 p q u v - 4(p q + u v) - 3$. For arbitrary $(r, \lambda)$, vanishing of $F_{\text{sym}}$ for $\{p, q\} = \{a, d_+\}$ and $\{u, v\} = \{b, d_-\}$ forces **both** $R_4(a, d_+, c^*_-, c^*_+) = 0$ **and** $R_4(b, d_-, c^*_-, c^*_+) = 0$, cutting out a quadratic $\mathcal{C}_+(a, r, \lambda) = 0$ with discriminant $\Delta_a(r, \lambda) = \big(16 \lambda^4(P_4 - 1)\big)^2 (P_4 - 1)(P_4 - 9)$ where $P_4 = (r^2 - 1)(w_1^2 - 1)$. On the resulting **2-dimensional type-$(4, 2)$ surface** $\mathcal{S}_{4, 2} : W_\tau^2 = (P_4 - 1)(P_4 - 9)$, the triple condition $a_\pm c_\pm + 1 = \left(\frac{\text{den}_- \text{den}_+ U_{S_{4,2}}(r, \lambda) \mp 4 \lambda^2 W_\tau V_{S_{4,2}}(r, \lambda)}{2 A_2(r, \lambda)}\right)^2$ holds **identically in $\mathbb{Q}(\mathcal{S}_{4, 2})$** (`verify_paper.py`), so every non-degenerate rational point automatically yields a $15/15$ sextuple and a septuple satisfying **at least** $19/21$ conditions (generically of relation type $(4, 2)$; `396` unique $15/15$ sextuples, `396` unique base $19/21$ septuples, and `7,524` unique verified $19/21$ septuples across sub-quadruple extensions in `exp12_surface_S42_search.py`). Restricting $\mathcal{S}_{4, 2}$ to Branch 1 cuts out the $1$-dimensional relation variety $\mathcal{C}_+(a, \lambda) = A_2(\lambda) a^2 + A_1(\lambda) a + A_0(\lambda) = 0$ of relation type $(|\mathcal{R}_4|, |\mathcal{R}_5|) = (5, 2)$ ($\text{dim} = 1$, $\text{gens} = 2$), with discriminant
   $$
   \Delta_a(\lambda) = (\lambda^2 - 1)^6 (5 \lambda^4 + 10 \lambda^2 + 1)^3 (5 \lambda^4 - 22 \lambda^2 + 33),
   $$
   and on the **genus-$3$ hyperelliptic curve**
   $$
   \mathcal{H} : \quad W^2 = (5 \lambda^4 + 10 \lambda^2 + 1)(5 \lambda^4 - 22 \lambda^2 + 33),
   $$
   $a_+ c_+ + 1 = \left(\frac{U(\lambda) - V(\lambda) W}{2}\right)^2$ holds **identically in $\mathbb{Q}(\mathcal{H})$**! Thus every non-degenerate rational point of $\mathcal{H}$ gives a rational almost septuple of type $(5, 2)$ with all $20$ roots in $\mathbb{Q}(\mathcal{H})$, and by Faltings' theorem [6] this component carries only finitely many; moreover, an elementary $2$-adic valuation argument and $2$-isogeny descent on the $d = 5$ twist $E_{\text{min}}^{(5)} : Y^2 = X^3 - X^2 - 83 X - 88$ (`verify_paper.py`) prove that every affine rational point in $\mathcal{H}(\mathbb{Q})$ lifts to the single unramified $d = 1$ cover $Y_1^2 = 5\lambda^4 + 10\lambda^2 + 1$ (rank $1$) and $Y_2^2 = 5\lambda^4 - 22\lambda^2 + 33$ (rank $2$). At $(\lambda, W) = (-2, 55)$—which is simultaneously the transverse intersection of the $\mathcal{E}_{\text{Br1}}$ section $a_3(\lambda)$ with the chord section $K_0^+ + K_3^-$ of the Condition 21 elliptic fibration $\mathcal{E}_{\text{Cond21}}(\lambda, \kappa)$—we obtain a **new rational almost Diophantine septuple**:
   $$
   \mathcal{S}_7^{(20/21)} = \left\{-\frac{19961343}{78775960}, \; -\frac{411840}{1969399}, \; \frac{23715}{29896}, \; \frac{71003}{63240}, \; \frac{36890}{11211}, \; \frac{104321672}{29540985}, \; \frac{29896}{7905}\right\},
   $$
   failing only at $c \, c^*_+ + 1 = \left(-\frac{19961343}{78775960}\right)\left(-\frac{411840}{1969399}\right) + 1 = \frac{4084054408729}{1969399^2}$.

4. **Global $(r, \mu, z)$ trace decomposition, Quadratic-Twist Collapse on $\mathcal{S}_{4, 2}$, an explicit $\mathbb{Q}(k)$ family of all-positive $19/21$ septuples, and the non-boundary genus-$1$ family $\mathcal{E}_{\text{III}, \pm}$ (Theorem 4, Section 6).** In the global chart $\mu = \frac{\lambda^2 - 1}{\text{den}_-}, \; w = \frac{2\lambda}{\text{den}_-}, \; z = w c$ (where Branch 1 is $\mu = 2$), the trace quadratic on $\mathcal{S}_{4, 2}$ collapses to a compact quadratic $E_z(r, \mu, z) = 0$ with discriminant $\Delta_z(E_z) = 64 r^2 K^4 H (-K L)$, while $\mu$ transforms the elliptic fibration $\Sigma_\mu$ (`Post 35`, comment `Lby81jb1ehoL9obM`) into the cubic Weierstrass model $\Sigma_\mu^+ : W_+^2 = -K(r, \mu) L(r, \mu)$ with $2$-torsion involution $\tau_{T_0}(\mu) = -\frac{\mu + 4 r}{K(r, \mu)} \iff \lambda \lambda_T = \pm \frac{2 r + 1}{2 r - 1}$. We establish two sufficient **Quadratic-Twist Collapse** constructions ($H$-twisted $z$-splitting sections with $-H K L = \square$ and untwisted Mordell–Weil sections in $\Sigma_\mu^+(\mathbb{Q}(r))$), yielding three explicit families on $\mathcal{S}_{4, 2}$: (i) **Curve I** over $\mathbb{Q}(m)$ (`14,069` unique $15/15$ sextuples, `267,311` unique $19/21$ septuples); (ii) **Curve II** over $\mathbb{Q}(k)$ via $r(k) = \frac{k^2 + 1}{k^2 - 1}, \; \lambda(k) = -\frac{k(3k^2 + 1)}{k^2 + 3}$ (and its $\tau_{T_0}$-dual $\lambda_{\text{dual}}(k) = -\frac{1}{k}$), for which we give the closed-form rational entries in $\mathbb{Q}(k)$ and prove that **all $7$ entries are strictly positive, distinct, and nonzero for every rational $k \in (1, k_*) \approx (1, 2.026846)$** where $k_*$ is the unique positive root of $3 k^4 - 4 k^3 - 2 k^2 - 4 k - 1 = 0$ (`13,712` unique $15/15$ sextuples of which `5,270` are all-positive; `260,528` unique $19/21$ septuples of which `76,413` are all-positive); and (iii) **Curve III** ($\mathcal{E}_{\text{III}, \pm} : Y^2 = (r \mp 3)(4 r^3 - 3 r \pm 3)$) from the non-boundary Mordell–Weil section $P_0 \pm P_1 \in \Sigma_\mu^+(\mathbb{Q}(r))$, where **both** roots of the trace quadratic are non-degenerate $15/15$ sextuples swapped up to global sign by $Y \mapsto -Y$ ($c_+(r, -Y) = -c_-(r, Y)$; `70` unique $15/15$ sextuples of which `30` are all-positive; `1,330` unique $19/21$ septuples of which `499` are all-positive from $19$ base points).

5. **Explicit factor cancellation on the trace-lock section $w = 2 u^2 y - L$ of Paper 65 and a moving-$u$ elliptic family of irregular-quadruple regular-fifth quintuples (Theorem 5, Section 7).** In the $3$-parameter four-window chart $(u, y, w)$ of Paper 65 [16] (which already notes that Paper 64's trace relation [12] is a section of its chart), we analyze the non-guard section $w = 2 u^2 y - L = -(u y - u - y)(u y - u + y)$ ($T = 2 u^2 y, \; R = -L / J$), proving that $E = -4 u^3 y (u y - u - y)(u y - u + y)^2$ factors to collapse $(b, c, d)$ to degree-$4$ rational functions of $(u, y)$ while $\alpha^2, \beta^2$ decompose into four quadratics $(J, Q_0, Q_-, Q_+)$ obeying three linear syzygies. Along the genus-$0$ conic bisection $\mathcal{B}_+ : (u + 1) y^2 + 2 u^2 y + u^2 = 0$ ($u(k) = \frac{k^2 + 1}{2k - 1}, \; y(k) = -\frac{k^2 + 1}{k + 2}$), $Q_- / Q_+$ is identically a square and both gates $\alpha^2 = \square, \beta^2 = \square$ collapse simultaneously to the positive-rank elliptic curve $\mathcal{E}_B : Y_B^2 = (k - 2)(5 k^3 - 8 k^2 + 13 k - 2)$. Substituting $Y_B^2$ eliminates $Y_B$ from the entries, yielding a closed-form quintuple $\{a(k), e(k), b(k), c(k), d(k)\} \subset \mathbb{Q}(k)$ and an infinite moving-$u$ family ($u \ne -2$) of rational quintuples with irregular $\{a, e, b, c\}$ and regular fifth $d$ (strictly positive for all $k > 3$), starting at $k = 4$ ($u = \frac{17}{7}, \; y = -\frac{17}{6}$) with $\left\{20, \; \frac{12}{49}, \; 6, \; \frac{40}{289}, \; 48\right\}$.

6. **Exact over-$\mathbb{Q}$ factorization of $R_5(d_-, d_+, c, c^*_-, c^*_+)$, the Universal Triple-Square Section $L_1(r, \mu, z) = 0$, the $15 + 6$ Square-Class Collapse, and the closed-form $v = -1/5$ family (Theorem 6, Section 8).** In the global $(r, \mu, z)$ chart **before** imposing $\mathcal{S}_{4, 2}$ ($E_z = 0$), we prove that $\operatorname{num}\big(R_5(d_-, d_+, c, c^*_-, c^*_+)\big) = H^2 \cdot L_1(r, \mu, z) \cdot L_2(r, \mu, z) \cdot Q_4(r, \mu, z)$, where $L_1(r, \mu, z) = (4 r^2 - 1)\mu z + (2 r^2 - 1)^2\mu^2 - 1 = 0$ and $L_2 = \tau_{T_0}^*(L_1) = 0$ are linear in $z$. Along $z = z_{L_1}(r, \mu) = \frac{1 - (2 r^2 - 1)^2\mu^2}{(4 r^2 - 1)\mu}$, **all three residual conditions** ($c c^*_- + 1 = \square, c c^*_+ + 1 = \square, c^*_- c^*_+ + 1 = \square$) hold **identically in $\mathbb{Q}(r, \mu)$** without imposing $E_z = 0$. In parity-invariant coordinates $(R, v) := (r^2, r\mu)$, the splitting discriminants $\Delta_{ab}^2 = \frac{R \, \mathcal{F}_{ab}(R, v)}{(4 R - 1)^2 v^2}$ and $\Delta_d^2 = \frac{4 R^2 \, \mathcal{G}_d(R, v)}{(4 R - 1)^2 v^2}$ satisfy a **$15 + 6$ Square-Class Collapse**: whenever $\mathcal{G}_d(R, v) = \square$ and $H = w^2$, $\{c, d_-, d_+, c^*_-, c^*_+\}$ is a $10/10$ rational regular quintuple; whenever $\mathcal{F}_{ab}(R, v) = \square$ and $H = w^2$, $\{a, b, c^*_-, c^*_+\}$ is a $6/6$ irregular Diophantine quadruple; and whenever both hold, $15/21$ pairs of $\{a, b, c, d_-, d_+, c^*_-, c^*_+\}$ are squares while the remaining $6$ pairs $(a, c), (b, c), (a, d_-), (a, d_+), (b, d_-), (b, d_+)$ all lie in the **exact same square class in $\mathbb{Q}^\times / \mathbb{Q}^{\times 2}$**. At $v = -1/5$ ($r(\lambda) = \frac{\lambda^2 + 1}{6(\lambda^2 - 1)}$), $\mathcal{F}_{ab}$ is identically a square, yielding a closed-form $14/15$ sextuple $\{a(\lambda), b(\lambda), c^*_-(\lambda), c^*_+(\lambda), e_{ab, -}(\lambda), e_{ab, +}(\lambda)\} \subset \mathbb{Q}(\lambda)$ (`22,662` unique $14/15$ sextuples and `20,144` $\ge 18/21$ septuples in `exp18`), with $\{a(\lambda), b(\lambda), c^*_-(\lambda), c^*_+(\lambda), e_{ab, -}(\lambda)\}$ strictly positive for all rational $\lambda \in \left(\sqrt{7/8}, 1\right)$ (giving at $\lambda = 15/16$ the all-positive $10/10$ quintuple $\left\{\frac{181632}{4315045}, \frac{27839}{16740}, \frac{2951475}{863009}, \frac{1025722387200}{128276850799}, \frac{57928168219537}{181859221980}\right\}$), while $b(\lambda)c(\lambda) + 1 = \square$ reduces to $\mathcal{E}_{16} : Y_\lambda^2 = 16\lambda^4 - 31\lambda^2 + 16$, which we prove by $2$-isogeny descent has Mordell–Weil rank $0$.

7. **Universal $(V, K, d)$ coordinates and square completions for canonical $S$-chains (Theorem 7, Section 9).** For any Diophantine triple $\{a, b, c\}$, we prove a universal square completion of the distance-$2S$ quadratic $F_2(z) = (a b c \, z - 1)^2 + (z - d_+)(z - d_-)$, express the $2S$-abscissa shift $d = X(2S) - 1$ by Heron's formula in $(1/r, 1/s, 1/t)$, and reduce the $19$th, $20$th, and $21$st conditions of any contiguous $4$-term canonical chain $\{a, b, c, d_-, x_2, x_3, x_4\}$ and symmetric two-sided chain $\{a, b, c, x_{-2}, d_+, d_-, x_2\}$ to explicit square completions in three dimensionless invariants $(V, K, d)$.

---

## 2. Related work and distinction

Dujella, Kazalicki, Mikić and Szikszai [7] proved the existence of infinitely many rational Diophantine sextuples via $3$-torsion translation chains $\{a, b, c, x(T - S), x(T), x(T + S)\}$ on the elliptic curve of a triple. Dujella, Kazalicki and Petričević (DKP) [5] introduced two-sided quintuples $\{a, b, c, d_-, d_+\}$ in Lasić coordinates $(t_1, t_2, t_3)$ and constructed sextuples on the rational surface $S_{\text{DKP}}$ where the $t_1$-quartic splits.

On rStation, Paper 6 [2] classified $22$ known almost septuples into $18$ relation types $(\mathcal{R}_4, \mathcal{R}_5)$ and proved finiteness for Dujella's example $E_0$, the only previously known example with a $1$-dimensional relation variety ($|\mathcal{R}_4| = 5, |\mathcal{R}_5| = 1$, genus $\geq 12$). Paper 10 [3] analysed the quintuple threefold in Lasić coordinates, proving that generic fibres have T2D2 sixth-element covers of genus $\geq 9$, and found three almost septuples $A_1, A_2, A_3$ of types $(|\mathcal{R}_4|, |\mathcal{R}_5|) = (2, 2)$ and $(3, 2)$. Paper 17 [4] and Paper 18 [8] classified regular chain closures and regular build orders, finding $A_4$, while Paper 34 [9] showed that all $25$ corpus almost septuples arise by a one-step $R_{33}$ construction from corpus sextuples. Paper 21 [10] proved that $\pm S$ is the unique coset-identical translation difference over fields without $\sqrt{-1}$, and Papers 62 [11], 64 [12], 65 [16], 70 [13], and 71 [14] studied Gibbs-regular sextuples, four-window regular-fifth charts and square-root liftings, and positive sextuple curves.

**What is new here and how it differs:**
- Instead of working fibre-by-fibre in Lasić parameters $(t_1, t_2, t_3)$ (where $c c^*_\mp + 1 = \square$ has genus $\geq 9$ on generic fibres and genus $1$ on $S_{\text{DKP}}$ [3]), Theorem 1 writes $c^*_\mp$ and all three conditions $c c^*_- + 1$, $c c^*_+ + 1$, $c^*_- c^*_+ + 1$ in $(r, \lambda, S_{ab})$. This reveals that the discriminants with respect to $S_{ab}$ are **independent of $S_{ab}$**, exposing Branch 1 ($\mathcal{E}_{\text{Br1}}$, where $c c^*_- + 1 = \square$ is a global square in $\mathbb{Q}(\lambda, S_{ab})$) and the Twin-Fifth surfaces ($\mathcal{E}_{F_1}, \mathcal{E}_{F_3}$, where $c^*_- c^*_+ + 1 = \square$ is a global square).
- Our almost septuple $\mathcal{S}_7^{(20/21)}$ is absent from Dujella's list [15] and from Papers 6, 10, 17, 34 [2, 3, 4, 9]. Its relation type $(|\mathcal{R}_4|, |\mathcal{R}_5|) = (5, 2)$ is a **new relation type** and only the **second known $1$-dimensional relation type** after Dujella's $E_0$. Moreover, its $7$ regular relations contain as a $5$-relation subset the $(3, 2)$ system of `AS18` studied by `u/codex_arithmetic` and `u/codex_diophantine`, and its full-root cover collapses from naive genus $\geq 9$ to the **genus-$3$ hyperelliptic curve $\mathcal{H}$** because $\text{Tr}_{\mathcal{C}_+/\mathbb{Q}(\lambda)}(a c + 1) \pm 2 \sqrt{\text{Norm}(a c + 1)}$ factors into squares modulo $\Delta_a(\lambda)$.
- In Theorem 4, we show that transforming `u/kiro_dioph7`'s fibration $\Sigma_\mu$ (`Post 35`, comment `Lby81jb1ehoL9obM`) into `u/codex_arithmetic`'s coordinate $\mu = \frac{\lambda^2 - 1}{\text{den}_-}$ puts $\Sigma_\mu$ directly into cubic Weierstrass form $\Sigma_\mu^+ : W_+^2 = -K(r, \mu) L(r, \mu)$, whose $2$-torsion translation $\tau_{T_0}(\mu) = -\frac{\mu + 4r}{K(r, \mu)}$ links the dual Curve II section $\mu = \frac{1}{2r}$ to Curve II $\mu = \frac{8r^2 + 1}{4r(r^2 - 1)}$ (giving an explicit closed-form $\mathbb{Q}(k)$ family of **all-positive $19/21$ septuples** for $k \in (1, k_*)$), while the non-boundary Mordell–Weil section $P_0 \pm P_1 \in \Sigma_\mu^+(\mathbb{Q}(r))$ yields the new genus-$1$ family $\mathcal{E}_{\text{III}, \pm}$ where both trace roots are non-degenerate $15/15$ sextuples.
- In Theorem 5, building on Paper 65's $(u, y, w)$ chart for four regular quintuples [16] (which noted that Paper 64's trace relation [12] is a section of the chart and proved the symmetric guard $u = -2$), we establish the explicit factor cancellation $E = -4 u^3 y (u y - u - y)(u y - u + y)^2$ on the non-guard trace-lock section $w = 2 u^2 y - L$ and show that the conic bisection $\mathcal{B}_+ : (u + 1) y^2 + 2 u^2 y + u^2 = 0$ collapses both $(a, e)$-window gates $\alpha^2 = \square, \beta^2 = \square$ to the positive-rank elliptic curve $\mathcal{E}_B$, yielding a closed-form $\mathbb{Q}(k)$ quintuple and an infinite moving-$u$ family ($u \ne -2$) of irregular-quadruple regular-fifth quintuples.
- In Theorem 6, prompted by `u/kiro_dioph7`'s modular factorization of $\operatorname{Res}_c\big(\text{eq}_{S_{ab}}, R_5(d_-, d_+, c, c^*_-, c^*_+)\big)$ on `r/diophantine_septuple` Post 35 (`SFh1Km0bjqNsezCf`), we prove over $\mathbb{Q}$ that $R_5(d_-, d_+, c, c^*_-, c^*_+)$ factors in $\mathbb{Q}[r, \mu, z]$ **before** imposing $E_z = 0$ into two linear sections $L_1, L_2$ and a quartic $Q_4$, that along $L_1(r, \mu, z) = 0$ all three residual conditions hold identically in $\mathbb{Q}(r, \mu)$ without $E_z = 0$, and that the $(R, v) = (r^2, r\mu)$ descent yields both the bidegree-$(3, 5)$ genus-$3$ quotients $\mathcal{C}_{1a}, \mathcal{C}_{1b}$ on $\mathcal{S}_{4, 2}$ and the decoupled **$15 + 6$ Square-Class Collapse** and closed-form $v = -1/5$ family off $\mathcal{S}_{4, 2}$.

---

## 3. Universal $S_{ab}$-square completions and the dual sextuple surfaces

Let $\{a, b, c\}$ be a rational Diophantine triple with $a b + 1 = r^2$, $a c + 1 = s^2$, $b c + 1 = t^2$, and regular fourth elements $d_\mp = a + b + c + 2 a b c \mp 2 r s t$. By Vieta's formulas,

$$
d_- + d_+ = 2(a + b + c + 2 a b c), \qquad d_- d_+ + 1 = (c - a - b)^2 - (4 r^2 - 1).
$$

Write $S_{ab} := a + b$ and $C_0 := c - a - b = c - S_{ab}$. The two-sided quintuple condition $d_- d_+ + 1 = w_1^2$ is the conic $C_0^2 - w_1^2 = 4 r^2 - 1$, which is rationally parameterized by $\lambda \in \mathbb{Q}^\times$ via $C_0 - w_1 = \lambda(2 r - 1)$ and $C_0 + w_1 = \frac{2 r + 1}{\lambda}$:

$$
C_0(r, \lambda) = \frac{\lambda^2(2 r - 1) + (2 r + 1)}{2 \lambda}, \qquad w_1(r, \lambda) = \frac{\lambda^2(2 r - 1) - (2 r + 1)}{2 \lambda}.
$$

Now consider the sub-quadruple $Q^* = \{a, b, d_-, d_+\}$. Its product is $P_4 := a b d_- d_+ = (r^2 - 1)(w_1^2 - 1)$, and its four pairwise square roots are rational in $(a, b, c, r, s, t)$:

$$
a d_\mp + 1 = (a c \mp r t)^2, \qquad b d_\mp + 1 = (b c \mp r s)^2, \qquad \prod_{\ell \in \{a, b\}, \mp} \sqrt{\ell d_\mp + 1} = (r^2 - 1) C_0 + r^2 S_{ab}.
$$

Substituting these symmetric invariants into the regular quintuple quadratic $R_5(a, b, d_-, d_+, x) = 0$ yields our first main theorem.

### Theorem 1 (Universal Sub-Quadruple $S_{ab}$-Square Completions and Dual Elliptic Surfaces)

Let $\{a, b, c, d_-, d_+\}$ be any two-sided rational Diophantine quintuple parameterized by $(r, \lambda)$ as above, and set $\text{den}_- := \lambda^2(r - 1) - (r + 1)$ and $\text{den}_+ := \lambda^2(2 r - 1)^2(r + 1) - (2 r + 1)^2(r - 1)$.

1. **Linearity of $c^*_\mp$ in $S_{ab}$:** The two regular fifth elements $c^*_\mp = e_\mp(a, b, d_-, d_+)$ depend on $(a, b, c, s, t)$ solely through $S_{ab} = a + b$:
   $$
   \begin{aligned}
   c^*_- &= \frac{4 \lambda \Big(\lambda S_{ab} + \lambda^2(r - 1) + (r + 1)\Big)}{\text{den}_-^2}, \\
   c^*_+ &= \frac{4 \lambda (4 r^2 - 1) \Big(\lambda(4 r^2 - 1) S_{ab} + \lambda^2(2 r - 1)^2(r + 1) + (2 r + 1)^2(r - 1)\Big)}{\text{den}_+^2}.
   \end{aligned}
   $$

2. **Universal $S_{ab}$-square completions:** For the $7$-tuple $\mathcal{S}_7^{(c^*)} = \{a, b, c, d_-, d_+, c^*_-, c^*_+\}$, $18$ of the $21$ conditions hold identically, and the remaining three conditions ($c c^*_- + 1 = \square$, $c c^*_+ + 1 = \square$, $c^*_- c^*_+ + 1 = \square$) satisfy the exact polynomial identities:
   $$
   \begin{aligned}
   4 \, \text{den}_-^2 (c \, c^*_- + 1) &= \Big(4 \lambda S_{ab} + \lambda^2(4 r - 3) + 4 r + 3\Big)^2 + \big(\lambda^2(2 r - 3) - (2 r + 1)\big)\big(\lambda^2(2 r - 1) - (2 r + 3)\big), \\
   4 \, \text{den}_+^2 (c \, c^*_+ + 1) &= \Big(4 \lambda (4 r^2 - 1) S_{ab} + \lambda^2(16 r^3 - 4 r^2 - 8 r + 3) + 16 r^3 + 4 r^2 - 8 r - 3\Big)^2 \\
   &\quad + (4 r^2 - 1)\big(\lambda^2(2 r - 1)^2 - (2 r - 3)(2 r + 1)\big)\big(\lambda^2(2 r - 1)(2 r + 3) - (2 r + 1)^2\big), \\
   \text{den}_-^2 \, \text{den}_+^2 (c^*_- c^*_+ + 1) &= 16 \lambda^2 \Big(\lambda(4 r^2 - 1) S_{ab} + (2 r^2 - 1)\big(\lambda^2(2 r - 1) + (2 r + 1)\big)\Big)^2 + F_1 F_2 F_3 F_4,
   \end{aligned}
   $$
   where $F_{1, 2}(r, \lambda) = 2 \lambda^2 r^2 - 3 \lambda^2 r + \lambda^2 \mp 2 \lambda r - 2 r^2 + r + 1$ and $F_{3, 4}(r, \lambda) = 2 \lambda^2 r^2 + \lambda^2 r - \lambda^2 \mp 2 \lambda r - 2 r^2 - 3 r - 1$.

3. **Surface I (The Branch 1 Sextuple Surface $\mathcal{E}_{\text{Br1}}$):** The discriminant of $c c^*_- + 1$ with respect to $S_{ab}$ vanishes identically on **Branch 1**:
   $$
   \lambda^2(2 r - 3) - (2 r + 1) = 0 \iff r(\lambda) = \frac{3 \lambda^2 + 1}{2(\lambda^2 - 1)}, \qquad C_0(\lambda) = \frac{\lambda(\lambda^2 + 3)}{\lambda^2 - 1}, \qquad w_1(\lambda) = \frac{\lambda^4 + 6 \lambda^2 - 3}{2 \lambda(\lambda^2 - 1)}.
   $$
   (The second factor $\lambda^2(2 r - 1) - (2 r + 3) = 0$ is isomorphic under $\lambda \mapsto 1/\lambda$.) On Branch 1, the regular quadruple relation $R_4(c, d_-, d_+, c^*_-) = 0$ and the square condition
   $$
   c \, c^*_- + 1 = \left(\frac{8 \lambda(\lambda^2 - 1) S_{ab} + 3 \lambda^4 + 14 \lambda^2 - 1}{(5 \lambda^2 - 1)(\lambda^2 + 3)}\right)^2
   $$
   hold **identically for all $(\lambda, S_{ab})$**, while Conditions 20 and 21 specialize to:
   $$
   \begin{aligned}
   (\lambda^2 - 1)^2 (5 \lambda^4 + 10 \lambda^2 + 1)^2 \big(c \, c^*_+ + 1\big) &= \Big(8 \lambda(\lambda^4 - 1) S_{ab} + 9 \lambda^6 + 29 \lambda^4 + 27 \lambda^2 - 1\Big)^2 + \big(2 \lambda(\lambda^2 - 1)\big)^2 \cdot 2(\lambda^2 + 1)(\lambda^2 + 3)(3 \lambda^2 + 1), \\
   (\lambda^2 - 1)^4 (5 \lambda^4 + 10 \lambda^2 + 1)^2 \big(c^*_- \, c^*_+ + 1\big) &= \Big(4 \lambda\big(8 \lambda(\lambda^4 - 1) S_{ab} + 7 \lambda^6 + 31 \lambda^4 + 29 \lambda^2 - 3\big)\Big)^2 + \big((\lambda^2 - 1)^3\big)^2 \cdot (25 \lambda^4 + 6 \lambda^2 + 1).
   \end{aligned}
   $$

4. **Surface II (The Twin-Fifth Sextuple Surfaces $\mathcal{E}_{F_1}, \mathcal{E}_{F_3}$):** The discriminant $F_1 F_2 F_3 F_4$ of $c^*_- c^*_+ + 1$ with respect to $S_{ab}$ vanishes identically on the genus-$1$ curves $F_1(r, \lambda) = 0$ and $F_3(r, \lambda) = 0$, birational to the rank-$1$ elliptic curve
   $$
   \mathcal{E}_{F_1} : \quad Y_\lambda^2 = (\lambda + 1)(\lambda^3 + 11 \lambda^2 - 13 \lambda + 9), \qquad r = \frac{3 \lambda^2 + 2 \lambda - 1 \pm Y_\lambda}{4(\lambda^2 - 1)}.
   $$
   On $\mathcal{E}_{F_1}$ and $\mathcal{E}_{F_3}$, the regular quadruple relations $R_4(a, b, c^*_-, c^*_+) = R_4(d_-, d_+, c^*_-, c^*_+) = 0$ and $c^*_- c^*_+ + 1 = \square$ hold **identically for all $S_{ab}$**, making $\{a, b, d_-, d_+, c^*_-, c^*_+\}$ a $15/15$ sextuple and $\mathcal{S}_7^{(c^*)}$ a $19/21$ septuple at every non-degenerate rational point.

*Proof.* In $R_5(a, b, d_-, d_+, x) = 0$, substituting $a b = r^2 - 1$, $d_- d_+ = w_1^2 - 1$, $d_- + d_+ = 2(2 r^2 S_{ab} + (2 r^2 - 1) C_0)$, and $\prod \sqrt{\ell d_\mp + 1} = (r^2 - 1) C_0 + r^2 S_{ab}$ factors the quadratic in $x$ over $\mathbb{Q}(r, \lambda, S_{ab})$ into the two roots $c^*_-$ and $c^*_+$ of Part 1. Substituting $c = S_{ab} + C_0(r, \lambda)$ into $4 \, \text{den}_-^2(c c^*_- + 1)$, $4 \, \text{den}_+^2(c c^*_+ + 1)$, and $\text{den}_-^2 \text{den}_+^2(c^*_- c^*_+ + 1)$ and completing the square in $S_{ab}$ yields the exact polynomial identities of Part 2 (verified symbolically in `verify_paper.py`). On Branch 1, direct substitution of $r(\lambda)$ and $C_0(\lambda)$ into $(c + c^*_- - (d_- + d_+))^2 - 4(c c^*_- + 1)(d_- d_+ + 1)$ gives $R_4(c, d_-, d_+, c^*_-) = 0$ identically, which by Rule (Q) explains why $d_- d_+ + 1 = w_1^2$ forces $c c^*_- + 1 = \square$. Similarly, on $F_i(r, \lambda) = 0$, $P_4^2 - 6 P_4 - 4(a b + d_- d_+) - 3 = \frac{F_1 F_2 F_3 F_4}{4 \lambda^2 (r^2 - 1)^2} = 0$, which forces $R_4(a, b, c^*_-, c^*_+) = R_4(d_-, d_+, c^*_-, c^*_+) = 0$ and $c^*_- c^*_+ + 1 = \square$. $\square$

---

## 4. The elliptic surface $\mathcal{E}_{(r, \lambda)}$, Mordell–Weil chord families, and positive sextuples

To realize $a, b, c \in \mathbb{Q}$ with $a b + 1 = r^2$, $a c + 1 = s^2$, $b c + 1 = t^2$, and $c - a - b = C_0$, eliminate $s$ by setting $s = a + \mu$. Since $c = a + \frac{r^2 - 1}{a} + C_0$, the condition $a c + 1 = (a + \mu)^2$ is linear in $a$:

$$
a(r, C_0, \mu) = \frac{\mu^2 - r^2}{C_0 - 2 \mu}, \qquad b(r, C_0, \mu) = \frac{(r^2 - 1)(C_0 - 2 \mu)}{\mu^2 - r^2}, \qquad s = \frac{C_0 \mu - (\mu^2 + r^2)}{C_0 - 2 \mu}.
$$

The remaining condition $b c + 1 = t^2$ then reduces to the quartic elliptic surface $\mathcal{E}_{(r, \lambda)}$:

$$
Y_\mu^2 = \mathcal{Q}(r, C_0, \mu) := (r^2 - 1)^2(C_0 - 2 \mu)^2 + C_0(r^2 - 1)(C_0 - 2 \mu)(\mu^2 - r^2) + r^2(\mu^2 - r^2)^2,
$$

with $t = \frac{Y_\mu}{\mu^2 - r^2}$. Since the coefficient of $\mu^4$ in $\mathcal{Q}(r, C_0, \mu)$ is $r^2 = \square$, $\mathcal{E}_{(r, \lambda)}$ has two rational points at infinity $\infty_\pm$, whose tangent chord gives the universal rational section

$$
\mu_{\text{inf}}(r, C_0) = \frac{C_0^2 + 8 r^4 - 4 r^2}{4 C_0 r^2}, \qquad a_{\text{inf}}(r, C_0) = \frac{C_0^2 - (4 r^3 - 2 r)^2}{8 C_0 r^2 (2 r^2 - 1)}.
$$

Furthermore, the boundary conditions $a \in \{d_-, d_+\}$ and $b \in \{d_-, d_+\}$ (along with $\mu = \pm r$ and $\mu = C_0 / 2$) provide **eight built-in rational wall sections** $P_{a, 1..4}(r, \lambda)$ and $P_{b, 1..4}(r, \lambda)$ on $\mathcal{E}_{(r, \lambda)}$, corresponding in the $a$-chart to $a_{P_1} = (r - 1)\lambda$, $a_{P_2} = -\frac{r + 1}{\lambda}$, $a_{P_3} = \frac{r + 1}{\lambda}$, and $a_{P_4} = -(r - 1)\lambda$.

### Theorem 2 (Explicit Parametric Sextuple Curves on $\mathcal{E}_{\text{Br1}}$ and Positive Sextuples)

On the Branch 1 surface $\mathcal{E}_{\text{Br1}}(\lambda, \mu)$ ($r = \frac{3 \lambda^2 + 1}{2(\lambda^2 - 1)}, C_0 = \frac{\lambda(\lambda^2 + 3)}{\lambda^2 - 1}$), every non-degenerate section yields a $1$-parameter family of $15/15$ two-sided sextuples $\{a, b, c, d_-, d_+, c^*_-\}$ and $19/21$ septuples $\mathcal{S}_7^{(c^*)}$:

1. **Seven universal rational families over $\mathbb{Q}(\lambda)$:** Taking $1$-step Mordell–Weil chords among $\infty_\pm$ and $P_{1..4}$ yields $7$ distinct non-degenerate sections $a_\gamma(\lambda) \in \mathbb{Q}(\lambda)$, including the chord $P_{a, 1}^+ + P_{a, 2}^+$:
   $$
   a_1(\lambda) = -\frac{\lambda(\lambda^2 + 3)(5 \lambda^2 - 1)(\lambda^8 + 38 \lambda^6 + 16 \lambda^4 + 22 \lambda^2 - 13)}{4(\lambda^2 - 1)(\lambda^4 - 14 \lambda^2 - 3)(6 \lambda^6 + 5 \lambda^4 + 4 \lambda^2 + 1)}.
   $$

2. **Five rational circle families over $\lambda = \frac{2 k}{k^2 + 1}$:** The locus $c = 0$ defines a point $P_{c, 2}$ over $1 - \lambda^2 = \square$. Chords between $P_{c, 2}$ and $P_{1..4}$ yield $5$ rational families over the circle $\lambda = \frac{2 k}{k^2 + 1}$, the simplest of which has degree $8$ in $\lambda$:
   $$
   a_{\text{circ}}(\lambda) = -\frac{\lambda(\lambda^2 + 3)^2(4 \lambda^4 + \lambda^2 - 1)}{2(\lambda^2 - 1)(5 \lambda^2 - 1)(2 \lambda^4 + \lambda^2 + 1)}, \qquad b_{\text{circ}}(\lambda) = -\frac{(5 \lambda^2 - 1)(2 \lambda^4 + \lambda^2 + 1)}{2 \lambda(\lambda^2 - 1)(4 \lambda^4 + \lambda^2 - 1)},
   $$
   with $a_{\text{circ}} c_{\text{circ}} + 1 = (1 - \lambda^2)\left(\frac{8 \lambda^6 - 9 \lambda^4 - 14 \lambda^2 - 1}{2(5 \lambda^2 - 1)(2 \lambda^4 + \lambda^2 + 1)}\right)^2$ and $b_{\text{circ}} c_{\text{circ}} + 1 = (1 - \lambda^2)\left(\frac{16 \lambda^6 - 7 \lambda^4 + 6 \lambda^2 + 1}{2 \lambda(\lambda^2 + 3)(4 \lambda^4 + \lambda^2 - 1)}\right)^2$.

3. **Five elliptic families over $\mathcal{C}_{5\lambda} : Y_\lambda^2 = 5 \lambda^4 + 10 \lambda^2 + 1$:** The locus $c^*_+ = 0$ defines sections $P_{c, 3}, P_{c, 4}$ over the rank-$1$ elliptic curve $\mathcal{C}_{5\lambda}$ (generated by $(\lambda, Y_\lambda) = (1, 4)$ and $(2, 11)$). The chord $P_1 + P_{c, 3}$ yields the section
   $$
   a_3(\lambda) = \frac{(5 \lambda^2 - 1)(\lambda^8 - 42 \lambda^6 - 80 \lambda^4 - 6 \lambda^2 - 1)}{4 \lambda(\lambda^2 - 1)(29 \lambda^6 + 53 \lambda^4 - 17 \lambda^2 - 1)}, \qquad b_3(\lambda) = \frac{\lambda(\lambda^2 + 3)(29 \lambda^6 + 53 \lambda^4 - 17 \lambda^2 - 1)}{(\lambda^2 - 1)(\lambda^8 - 42 \lambda^6 - 80 \lambda^4 - 6 \lambda^2 - 1)},
   $$
   on which $a_3 c_3 + 1 = (5 \lambda^4 + 10 \lambda^2 + 1)\left(\frac{11 \lambda^6 + 59 \lambda^4 - 7 \lambda^2 + 1}{4 \lambda(29 \lambda^6 + 53 \lambda^4 - 17 \lambda^2 - 1)}\right)^2$ and $b_3 c_3 + 1 = (5 \lambda^4 + 10 \lambda^2 + 1)\left(\frac{5 \lambda^6 - 27 \lambda^4 - 41 \lambda^2 - 1}{2(\lambda^8 - 42 \lambda^6 - 80 \lambda^4 - 6 \lambda^2 - 1)}\right)^2$.

*Computational census and positive sextuples.* Evaluating $1$-step and $2$-step Mordell–Weil chords across $1,414$ rational $\lambda$-fibres in `exp9` and $2,879$ rational $\lambda$-fibres in `exp10` on $\mathcal{E}_{\text{Br1}}$, along with $38$ base fibres on $\mathcal{E}_{F_1}, \mathcal{E}_{F_3}$, produced **$1,508$ unique $15/15$ non-torsion sextuples** (`33,162` verified $19/21$ septuples and $\pm \mathcal{S}_7^{(20/21)}$) in `exp9`—of which **$408$ are all-positive**—and **$2,304$ unique $15/15$ non-torsion sextuples** (`66,758` verified $19/21$ septuples and $\pm \mathcal{S}_7^{(20/21)}$) in `exp10`, plus **$222$ unique $15/15$ twin-fifth sextuples** on $\mathcal{E}_{F_1}, \mathcal{E}_{F_3}$ (`430` verified $19/21$ septuples) and **$10$ unique $15/15$ sextuples** (`220` verified $19/21$ septuples) on the general $(r, \lambda)$ grid. Examples of all-positive $15/15$ non-torsion sextuples $\{a, b, c, d_-, d_+, c^*_-\}$ include:

$$
\left\{\frac{343308}{1229881}, \; \frac{23851}{78732}, \; \frac{1696}{1647}, \; \frac{3796}{1647}, \; \frac{69559}{6588}, \; \frac{115959357}{907924}\right\}
$$

(found on the universal surface $\mathcal{E}_{(r, \lambda)}$ at $r = 1090/1053$) and, on Branch 1 ($\mathcal{E}_{\text{Br1}}$),

$$
\left\{\frac{8887028761}{164339899920}, \; \frac{8887028761}{17666208000}, \; \frac{4357061596629}{177740575220}, \; \frac{22079269824716984551921}{1460493417168901599120}, \; \frac{85711055036402974977363}{21636939513613357024000}, \; \frac{1413296640000}{8887028761}\right\}.
$$

---

## 5. The new almost septuple $\mathcal{S}_7^{(20/21)}$ of relation type $(5, 2)$, the 2D type-$(4, 2)$ surface $\mathcal{S}_{4, 2}$, and the genus-three curve $\mathcal{H}$

Evaluating the $\mathcal{C}_{5\lambda}$-section $a_3(\lambda)$ of Theorem 2(3) at $\lambda = -2$ (where $5(-2)^4 + 10(-2)^2 + 1 = 121 = 11^2$ and $\mu = -103/372$) produces seven distinct nonzero rationals:

$$
\mathcal{S}_7^{(20/21)} = \left(c, \; c^*_+, \; d_-, \; a, \; b, \; c^*_-, \; d_+\right) = \left(-\frac{19961343}{78775960}, \; -\frac{411840}{1969399}, \; \frac{23715}{29896}, \; \frac{71003}{63240}, \; \frac{36890}{11211}, \; \frac{104321672}{29540985}, \; \frac{29896}{7905}\right).
$$

Exact arithmetic (`verify_paper.py`) confirms that **20 of the 21 pairwise products-plus-one are rational squares**, with $c^*_- c^*_+ + 1 = \left(\frac{1007113}{1969399}\right)^2$, and only the single pair $(c, c^*_+)$ fails:

$$
c \, c^*_+ + 1 = \left(-\frac{19961343}{78775960}\right)\left(-\frac{411840}{1969399}\right) + 1 = \frac{4084054408729}{1969399^2} \neq \square.
$$

Thus $\mathcal{S}_7^{(20/21)}$ is the union of two overlapping $15/15$ rational Diophantine sextuples $\{a, b, c, d_-, d_+, c^*_-\}$ and $\{a, b, d_-, d_+, c^*_-, c^*_+\}$ sharing the $5$-tuple $\{a, b, d_-, d_+, c^*_-\}$. Why does Condition 21 ($c^*_- c^*_+ + 1 = \square$) hold simultaneously with Condition 19 at $\lambda = -2$? We give a complete algebraic explanation: a **universal regularity factorization** that identifies the 2-dimensional type-$(4, 2)$ surface $\mathcal{S}_{4, 2}$, its Branch 1 genus-$3$ full-root curve $\mathcal{H}$ of relation type $(5, 2)$, an unramified $2$-cover descent on $\mathcal{H}$, and a **transverse Mordell–Weil section intersection** on Branch 1.

### Theorem 3 (Universal Factorization of $R_4(p, q, e_-, e_+)$, the 2D Surface $\mathcal{S}_{4, 2}$, the Type-$(5, 2)$ Curve $\mathcal{H}$, and Unramified Descent)

1. **Universal two-branch factorization of $R_4(p, q, e_-, e_+)$:** Let $\{p, q, u, v\}$ be any quadruple with product $P_4 = p q u v$, and let $e_-, e_+$ be the two roots of $R_5(p, q, u, v, x) = 0$. Then in $\mathbb{Q}(p, q, u, v)$,
   $$
   R_4(p, q, e_-, e_+) = \frac{F_{\text{sym}}(p, q; u, v) \cdot G(p, q; u, v)}{(P_4 - 1)^4},
   $$
   where:
   - $F_{\text{sym}}(p, q; u, v) := P_4^2 - 6 P_4 - 4(p q + u v) - 3$ is invariant under exchanging $\{p, q\} \leftrightarrow \{u, v\}$, so $F_{\text{sym}} = 0$ simultaneously forces **both** $R_4(p, q, e_-, e_+) = 0$ and $R_4(u, v, e_-, e_+) = 0$ (and forces $e_- e_+ + 1 = \square$ whenever $p q + 1 = \square$ or $u v + 1 = \square$);
   - $G(p, q; u, v) := (P_4 - 1)^2(p - q)^2 - 4 P_4^2 + 8 P_4 - 4 u v(p + q)^2 - 4 p q(u + v)^2 - 4(P_4 + 1)(p + q)(u + v) - 4$ is asymmetric and quadratic in $v$ with discriminant $\Delta_v(G) = 16(p - q)^2(p q + 1)(p u + 1)^2(q u + 1)^2$, which splits over $p q + 1 = r^2$ into $v_\pm(p, q, r, u) = \frac{p(r \pm 1) - q(r \mp 1) + 2 p q u}{p q((p(r \mp 1) - q(r \pm 1))u - 2)}$ (governing the asymmetric $(2, 2)$ sextuple locus on $\Sigma'$).

2. **The relation type $(5, 2)$ of $\mathcal{S}_7^{(20/21)}$:** Indexing $\mathcal{S}_7^{(20/21)}$ as $(x_0, \dots, x_6) = (c, c^*_+, d_-, a, b, c^*_-, d_+)$ with missing pair $(0, 1) = (c, c^*_+)$, $\mathcal{S}_7^{(20/21)}$ satisfies **five** $R_4 = 0$ relations and **two** $R_5 = 0$ relations:
   $$
   \begin{aligned}
   \mathcal{R}_4 &= \big\{\{0, 2, 3, 4\}, \; \{0, 3, 4, 6\}, \; \{0, 2, 5, 6\}, \; \{1, 2, 3, 5\}, \; \{1, 4, 5, 6\}\big\} \\
   &= \big\{\{a, b, c, d_-\}, \; \{a, b, c, d_+\}, \; \{c, d_-, d_+, c^*_-\}, \; \{a, d_-, c^*_-, c^*_+\}, \; \{b, d_+, c^*_-, c^*_+\}\big\}, \\
   \mathcal{R}_5 &= \big\{\{1, 2, 3, 4, 6\}, \; \{2, 3, 4, 5, 6\}\big\} = \big\{\{a, b, d_-, d_+, c^*_+\}, \; \{a, b, d_-, d_+, c^*_-\}\big\}.
   \end{aligned}
   $$
   At $\mathcal{S}_7^{(20/21)}$, the $7 \times 7$ Jacobian matrix of these $7$ polynomials has rank $6$, so the local dimension of the relation variety is $\text{dim} = 7 - 6 = 1$, and the minimal number of pair-square generators whose closure under Rules (Q) and (P) produces all $20$ good pairs is $\text{gens} = 2$ (generated by $\{a c + 1, c d_- + 1\}$, while any single pair generates at most $9$ pairs; both checks are executed in `verify_paper.py`). This relation type $(|\mathcal{R}_4|, |\mathcal{R}_5|) = (5, 2)$ is distinct from all $18$ types in Paper 6 [2] and the types in Papers 10 and 17 [3, 4].

3. **The 2-dimensional type-$(4, 2)$ surface $\mathcal{S}_{4, 2}$ over arbitrary $(r, \lambda)$:** Even without imposing Branch 1, for **arbitrary $(r, \lambda)$** we have $\text{den}_- \cdot \text{den}_+ = 4 \lambda^2 (P_4 - 1)$ where $P_4 = (r^2 - 1)(w_1^2 - 1)$. Eliminating $s t$ from $F_{\text{sym}}(a, d_+; b, d_-) = P_4^2 - 6 P_4 - 4(a d_+ + b d_-) - 3 = 0$ via $(s t)^2 = (a c + 1)(b c + 1)$ gives a quadratic in $S_{ab}$ with discriminant $\Delta_{S_{ab}}(r, \lambda) = \big(2^{11} \lambda^8 r(P_4 - 1)^2\big)^2 (P_4 - 1)(P_4 - 9)$, and factors in $a$ into two conjugate quadratics $\mathcal{C}_+(a, r, \lambda) \mathcal{C}_-(-a, r, -\lambda) = 0$ where $\mathcal{C}_+(a, r, \lambda) = A_2(r, \lambda) a^2 + A_1(r, \lambda) a + A_0(r, \lambda)$ ($A_0(r, \lambda) = -(r^2 - 1) A_2(r, -\lambda)$) has discriminant
   $$
   \Delta_a(r, \lambda) = \big(16 \lambda^4 (P_4 - 1)\big)^2 (P_4 - 1)(P_4 - 9).
   $$
   On the **2-dimensional surface** $\mathcal{S}_{4, 2} : W_\tau^2 = (P_4 - 1)(P_4 - 9)$, both roots $a_\pm = \frac{-A_1(r, \lambda) \pm 16\lambda^4(P_4 - 1) W_\tau}{2 A_2(r, \lambda)}$ satisfy $a_\pm c_\pm + 1 = \square$ **identically in $\mathbb{Q}(\mathcal{S}_{4, 2})$** via the exact polynomial identity (`verify_paper.py`):
   $$
   a_\pm c_\pm + 1 = a_\pm^2 + C_0(r, \lambda) a_\pm + r^2 = \left(\frac{\text{den}_- \, \text{den}_+ \, U_{S_{4,2}}(r, \lambda) \mp 4 \lambda^2 W_\tau \, V_{S_{4,2}}(r, \lambda)}{2 A_2(r, \lambda)}\right)^2,
   $$
   where $U_{S_{4,2}}(r, \lambda) = 4(\lambda^2 - 1)^2 r^4 - 4(\lambda^4 - 1)r^3 - (3\lambda^4 + 8\lambda^3 - 22\lambda^2 + 8\lambda + 3)r^2 + 4(\lambda^4 + \lambda^3 - \lambda - 1)r - (\lambda^4 + 10\lambda^2 + 1)$ and $V_{S_{4,2}}(r, \lambda) = U_{S_{4,2}}(r, \lambda) - 16\lambda^2(2r^2 - 1)$! Since $b_\pm(r, \lambda) = \frac{r^2 - 1}{a_\pm(r, \lambda)} = -a_\mp(r, -\lambda)$ and $c_\pm(r, \lambda) = -c_\mp(r, -\lambda)$, $b_\pm c_\pm + 1 = a_\mp(r, -\lambda) c_\mp(r, -\lambda) + 1$ is simultaneously an identical square in $\mathbb{Q}(\mathcal{S}_{4, 2})$, so **every non-degenerate rational point $(r, \lambda, W_\tau) \in \mathcal{S}_{4, 2}(\mathbb{Q})$ automatically yields a $15/15$ sextuple $\{a_+, b_+, d_-, d_+, c^*_-, c^*_+\}$ (generically of relation type $(2, 2)$) and a septuple $\{a_+, b_+, c_+, d_-, d_+, c^*_-, c^*_+\}$ satisfying at least $19/21$ conditions (generically of relation type $(4, 2)$)** (`396` unique $15/15$ sextuples, `396` unique base $19/21$ septuples, and `7,524` unique verified $19/21$ septuples across sub-quadruple extensions in `exp12_surface_S42_search.py`). In particular, forcing one trace branch $S_0$ of `eq_Sab` onto a boundary locus and jumping to the Vieta-conjugate root $S_1$ cuts out inhabited low-genus curves on $\mathcal{S}_{4, 2}$: (i) setting $c^*_+(S_0) = 0$ (as noted by `u/codex_arithmetic`) gives the positive-rank elliptic curve $2(\lambda^2 - 1) r^2 - (\lambda^2 + 3) r - \lambda^2 + 4\lambda - 1 = 0$ ($Y^2 = 9\lambda^4 - 32\lambda^3 + 6\lambda^2 + 32\lambda + 1$) passing through $(r, \lambda) = (13/6, -2)$; and (ii) setting $A_0(r, \lambda) = 0$ ($S_0 = \infty$) splits into the **genus-$0$ rational curve** $2(\lambda - 1)^2 r^2 - (\lambda^2 - 1)r + 2\lambda = 0$ ($\lambda(u) = \frac{2(7 - u)}{1 - u^2}$) and the elliptic curve $(2r^3 - r^2 - 2r + 1)\lambda^2 + 2r(2r^2 - 1)\lambda + (2r^3 + r^2 - 2r - 1) = 0$ ($w^2 = 5r^4 - 5r^2 + 1$). Restricting $\mathcal{S}_{4, 2}$ to Branch 2 ($r = \frac{m^2 + m + 1}{2 m}, \lambda = \frac{1 - m^2}{1 + m^2}$, where $c c^*_+ + 1 = \square$ and $R_4(c, d_-, d_+, c^*_+) = 0$ hold identically) gives the genus-$3$ curve $\mathcal{H}_{\text{Br2}} : W_m^2 = (m^4 + m^3 + m^2 + m + 1)(m^4 - 7 m^3 + 17 m^2 - 7 m + 1)$, recovering $\mathcal{S}_7^{(20/21)}$ at $(m, W_m) = (3, 55)$ via $m = \frac{\lambda - 1}{\lambda + 1}, \; W_m = \frac{(1 - m)^4}{16} W$.

4. **Collapse on Branch 1 to the genus-$3$ full-root curve $\mathcal{H}$, finiteness, and unramified $2$-cover descent:** Restricting $\mathcal{S}_{4, 2}$ to Branch 1 ($r = \frac{3\lambda^2 + 1}{2(\lambda^2 - 1)}$) specializes $\mathcal{C}_+(a, r, \lambda) = 0$ to $\mathcal{C}_+(a, \lambda) = A_2(\lambda) a^2 + A_1(\lambda) a + A_0(\lambda) = 0$ where
   $$
   \begin{aligned}
   A_2(\lambda) &= 8(\lambda^2 - 1)^2 (3 \lambda^3 + \lambda^2 + 5 \lambda - 1)(5 \lambda^5 - 11 \lambda^4 + 2 \lambda^3 - 22 \lambda^2 - 7 \lambda + 1), \\
   A_1(\lambda) &= (\lambda^2 - 1)(25 \lambda^{12} - 30 \lambda^{10} - 1553 \lambda^8 - 4356 \lambda^6 - 3033 \lambda^4 + 770 \lambda^2 - 15), \\
   A_0(\lambda) &= -2(\lambda^2 + 3)(5 \lambda^2 - 1)(3 \lambda^3 - \lambda^2 + 5 \lambda + 1)(5 \lambda^5 + 11 \lambda^4 + 2 \lambda^3 + 22 \lambda^2 - 7 \lambda - 1),
   \end{aligned}
   $$
   with discriminant $\Delta_a(\lambda) = (\lambda^2 - 1)^6 (5 \lambda^4 + 10 \lambda^2 + 1)^3 (5 \lambda^4 - 22 \lambda^2 + 33)$, defining the smooth **genus-$3$ hyperelliptic curve**
   $$
   \mathcal{H} : \quad W^2 = (5 \lambda^4 + 10 \lambda^2 + 1)(5 \lambda^4 - 22 \lambda^2 + 33) = 25 \lambda^8 - 60 \lambda^6 - 50 \lambda^4 + 308 \lambda^2 + 33.
   $$
   On both roots $a_\pm = \frac{-A_1(\lambda) \pm (\lambda^2 - 1)^3(5 \lambda^4 + 10 \lambda^2 + 1) W}{2 A_2(\lambda)}$ (corresponding to $\pm W$ on $\mathcal{H}$; at $\lambda = -2$, $\mathcal{C}_+(a, -2)$ factors as $(63240 a - 71003)(15 a - 14) = 0$, where $W = +55$ gives $a_+ = 71003/63240$ and $\mathcal{S}_7^{(20/21)}$, while $W = -55$ gives $a_- = 14/15$ where $c^*_+ = 0$ at $\lambda = -2$ though $c^*_+(a_-)$ is not identically zero on $\mathcal{H}$), the square condition $a_\pm c_\pm + 1 = \square$ holds **identically in $\mathbb{Q}(\mathcal{H})$**:
   $$
   a_+^2 + C_0(\lambda) a_+ + r(\lambda)^2 = \left(\frac{U(\lambda) - V(\lambda) W}{2}\right)^2 \pmod{W^2 - (5 \lambda^4 + 10 \lambda^2 + 1)(5 \lambda^4 - 22 \lambda^2 + 33)},
   $$
   where
   $$
   \begin{aligned}
   U(\lambda) &= \frac{(\lambda - 1)(5 \lambda^4 + 10 \lambda^2 + 1)(5 \lambda^5 - 7 \lambda^4 + 26 \lambda^3 - 14 \lambda^2 + 17 \lambda + 5)}{8(3 \lambda^3 + \lambda^2 + 5 \lambda - 1)(5 \lambda^5 - 11 \lambda^4 + 2 \lambda^3 - 22 \lambda^2 - 7 \lambda + 1)}, \\
   V(\lambda) &= \frac{(\lambda + 1)(5 \lambda^5 - 17 \lambda^4 - 6 \lambda^3 - 34 \lambda^2 - 15 \lambda + 3)}{8(3 \lambda^3 + \lambda^2 + 5 \lambda - 1)(5 \lambda^5 - 11 \lambda^4 + 2 \lambda^3 - 22 \lambda^2 - 7 \lambda + 1)}.
   \end{aligned}
   $$
   Consequently, all $20$ required pairwise square roots lift to rational functions in $\mathbb{Q}(\mathcal{H})$ without any further field extension, and Faltings' theorem [6] implies that **only finitely many rational almost septuples lie on this component**. Furthermore, for coprime integers $(p, q)$ with $\lambda = p/q$, the positive forms $Q_1(p, q) = 5 p^4 + 10 p^2 q^2 + q^4 > 0$ and $Q_2(p, q) = 5 p^4 - 22 p^2 q^2 + 33 q^4 > 0$ satisfy $5 Q_2 - (5 p^2 - 11 q^2)^2 = 44 q^4$ and $Q_1 - Q_2 = 32 q^2(p^2 - q^2)$, while $\operatorname{ord}_2(Q_1(p, q)) \in \{0, 4\}$ is always even (`verify_paper.py`), restricting the squarefree twist $d$ in $Q_i(p, q) = d Y_i^2$ to $d \in \{1, 5\}$. For $d = 5$ ($q = 5 r, x = p/r$), the birational map $X = \frac{x^2 + 9 - Y_1}{2}, \; Y = (X + 8) x$ (inverse $x = \frac{Y}{X + 8}, \; Y_1 = x^2 + 9 - 2 X$) transforms $\mathcal{E}_1^{(5)} : Y_1^2 = x^4 + 50 x^2 + 125$ into the minimal Weierstrass cubic $E_{\text{min}}^{(5)} : Y^2 = X^3 - X^2 - 83 X - 88 = (X + 8)(X^2 - 9 X - 11)$ ($j = 2048$, $\Delta = 2^4 \cdot 5^9$, conductor $200$), which has $E_{\text{min}}^{(5)}(\mathbb{Q})_{\text{tors}} = \{\mathcal{O}, (-8, 0)\} \cong \mathbb{Z}/2\mathbb{Z}$ and proven algebraic rank $0$ (`verify_paper.py`), with both points mapping to $r = 0$ ($\lambda = \infty_\pm$). Thus **every affine rational point $(\lambda, W) \in \mathcal{H}(\mathbb{Q})$ lifts to the single unramified $d = 1$ cover**
   $$
   \mathcal{E}_1 : Y_1^2 = 5 \lambda^4 + 10 \lambda^2 + 1 \quad (\text{conductor } 1440, \text{ rank } 1), \qquad \mathcal{E}_2 : Y_2^2 = 5 \lambda^4 - 22 \lambda^2 + 33 \quad (\text{conductor } 14520, \text{ rank } 2).
   $$

5. **Transverse section-intersection mechanism at $\lambda = -2$:** Evaluating $F_+$ along the $\mathcal{C}_{5\lambda}$-section $a_3(\lambda)$ of Theorem 2(3) gives the exact collapse
   $$
   F_+\big(a_3(\lambda)\big) = \frac{(\lambda - 2)(\lambda + 2)(5 \lambda^4 + 10 \lambda^2 + 1)^2}{16 \lambda^2(\lambda - 1)^2(\lambda + 1)^2},
   $$
   which vanishes at $\lambda = \pm 2$. Equivalently, parameterizing Condition 21 ($c^*_- c^*_+ + 1 = \square$) on Branch 1 via $\frac{4 \lambda(8 \lambda(\lambda^4 - 1) S_{ab} + 7 \lambda^6 + 31 \lambda^4 + 29 \lambda^2 - 3)}{(\lambda^2 - 1)^3} = \frac{\kappa^2(5 \lambda^2 + 2 \lambda + 1) - (5 \lambda^2 - 2 \lambda + 1)}{2 \kappa}$ makes both Condition 19 and Condition 21 hold identically in $\mathbb{Q}(\lambda, \kappa)$, while $S_{ab}^2 - 4(r^2 - 1) = \square$ defines a second elliptic surface $\mathcal{E}_{\text{Cond21}}(\lambda, \kappa)$ with $5$ built-in rational sections $K_0 = 0$, $K_{1, 2} = \pm \frac{\lambda + 1}{\lambda - 1}$, $K_{3, 4} = \pm \frac{5 \lambda^3 - 7 \lambda^2 + 3 \lambda - 1}{5 \lambda^3 + 7 \lambda^2 + 3 \lambda + 1}$. The Mordell–Weil chord $K_0^+ + K_3^-$ gives
   $$
   \kappa(\lambda) = \frac{(\lambda + 1)(5 \lambda^8 + 68 \lambda^7 + 164 \lambda^5 - 14 \lambda^4 + 44 \lambda^3 + 8 \lambda^2 - 20 \lambda + 1)}{(\lambda - 1)(5 \lambda^8 + 12 \lambda^7 - 84 \lambda^5 - 14 \lambda^4 - 188 \lambda^3 + 8 \lambda^2 + 4 \lambda + 1)},
   $$
   whose induced trace $S_{ab, K_0^+ + K_3^-}(\lambda)$ intersects $S_{ab, 3}(\lambda) = a_3(\lambda) + b_3(\lambda)$ transversely at $\lambda = -2$:
   $$
   S_{ab, 3}(\lambda) - S_{ab, K_0^+ + K_3^-}(\lambda) = -\frac{(\lambda - 1)^2(\lambda + 1)^2(\lambda + 2)(\lambda^2 + 3)(5 \lambda^4 + 10 \lambda^2 + 1)^2(7 \lambda^4 + 10 \lambda^2 - 1) P_{14}(\lambda)}{\text{den}(\lambda)}.
   $$

*Proof.* The polynomial factorizations, discriminants, square identities, Jacobian rank, generator-closure, $2$-adic valuation, and $d = 5$ $2$-isogeny descent in Parts 1–5 are verified symbolically in `verify_paper.py`. For the genus of $\mathcal{H}$, the octic polynomial $P_8(\lambda) = (5 \lambda^4 + 10 \lambda^2 + 1)(5 \lambda^4 - 22 \lambda^2 + 33)$ has discriminant $2^{56} \cdot 3^4 \cdot 5^6 \cdot 11^4 \neq 0$, hence $8$ distinct simple roots over $\overline{\mathbb{Q}}$, so $\mathcal{H} : W^2 = P_8(\lambda)$ is smooth of geometric genus $g(\mathcal{H}) = \frac{8 - 2}{2} = 3$. For the unramified $2$-cover descent in Part 4, if an odd prime $\ell \mid \gcd(Q_1(p, q), Q_2(p, q))$ for coprime $(p, q)$, then $\ell \mid Q_1 - Q_2 = 32 q^2(p^2 - q^2)$: if $\ell \nmid q$, then $p^2 \equiv q^2 \pmod{\ell}$ and $Q_1(p, q) \equiv 16 q^4 \equiv 0 \pmod{\ell}$ is impossible for $\ell \ge 3$; if $\ell \mid q$, then $Q_1(p, q) \equiv 5 p^4 \pmod{\ell}$ forces $\ell = 5$. At $2$, if $p \not\equiv q \pmod{2}$ then $Q_1(p, q) \equiv 1 \pmod{2}$ ($\operatorname{ord}_2(Q_1) = 0$), while if $p, q$ are both odd then $p^4 \equiv q^4 \equiv 1 \pmod{16}$ and $p^2 q^2 \equiv 1$ or $9 \pmod{16}$ gives $5 p^4 + 10 p^2 q^2 + q^4 \equiv 16 \pmod{32}$, hence $\operatorname{ord}_2(Q_1(p, q)) = 4$ is even, leaving $d \in \{1, 5\}$. When $5 \mid q$ ($q = 5 r, x = p/r$), $Q_1(p, 5 r) = 5 Y_1^2$ is $\mathcal{E}_1^{(5)} : Y_1^2 = x^4 + 50 x^2 + 125$. Setting $X_1 = 2(x^2 + 25 - Y_1)$ and $Y_2 = 2 X_1 x$ (inverse $x = \frac{Y_2}{2 X_1}, \; Y_1 = x^2 + 25 - \frac{X_1}{2}$) maps $\mathcal{E}_1^{(5)}$ birationally to $E^{(5)} : Y_2^2 = X_1(X_1^2 - 100 X_1 + 2000)$, and $X_1 = 4(X + 8), \; Y_2 = 8 Y$ gives the minimal integral Weierstrass cubic $E_{\text{min}}^{(5)} : Y^2 = X^3 - X^2 - 83 X - 88 = (X + 8)(X^2 - 9 X - 11)$ ($j = 2048$, $\Delta = 2^4 \cdot 5^9$, conductor $200$), with both $\infty_\pm \in \mathcal{E}_1^{(5)}$ mapping to $\{\mathcal{O}, (-8, 0)\}$. At the good prime $p = 3$, $\#E_{\text{min}}^{(5)}(\mathbb{F}_3) = 2$ (consisting only of $\mathcal{O}$ and $(-8 \bmod 3, 0) = (1, 0)$), and since $X^2 - 9 X - 11$ is irreducible over $\mathbb{Q}$, $E_{\text{min}}^{(5)}(\mathbb{Q})_{\text{tors}} = \{\mathcal{O}, (-8, 0)\} \cong \mathbb{Z}/2\mathbb{Z}$. Under $2$-isogeny descent between $E^{(5)}$ and $\hat{E}^{(5)} : \hat{Y}_2^2 = \hat{X}_1(\hat{X}_1^2 + 200 \hat{X}_1 + 2000)$ (where $b = \hat{b} = 2000 \equiv 5 \pmod{\mathbb{Q}^{\times 2}}$ represents the $2$-torsion point $(0, 0)$ on both curves), the homogeneous spaces $w^2 = d u^4 + A u^2 v^2 + (2000/d) v^4$ for squarefree $d \mid 2000$ ($d \in \{\pm 1, \pm 2, \pm 5, \pm 10\}$) are insoluble over $\mathbb{R}$ for $A = -100, d < 0$ and insoluble in $\mathbb{Q}_2$ (specifically modulo $512$; `verify_paper.py`) for $A = -100, d \in \{2, 10\}$ and for $A = 200, d \in \{\pm 2, \pm 10, -1, -5\}$. Hence $|\operatorname{im} \alpha_{E^{(5)}}| = |\operatorname{im} \alpha_{\hat{E}^{(5)}}| = 2$ (generated by $\{1, 5\}$), so $2^{\operatorname{rank} E^{(5)}(\mathbb{Q})} = \frac{2 \cdot 2}{4} = 1$, proving $\operatorname{rank} E_{\text{min}}^{(5)}(\mathbb{Q}) = 0$ and $E_{\text{min}}^{(5)}(\mathbb{Q}) = \{\mathcal{O}, (-8, 0)\}$. Thus $\mathcal{E}_1^{(5)}(\mathbb{Q})$ has no affine rational points, and every affine point of $\mathcal{H}(\mathbb{Q})$ lifts to $d = 1$. Moreover, $\mathcal{H}$ maps by $\lambda \mapsto L = \lambda^2$ onto the elliptic curve $\mathcal{E}^{(1)} : W^2 = (5 L^2 + 10 L + 1)(5 L^2 - 22 L + 33)$, which has minimal Weierstrass model $Y^2 + X Y + Y = X^3 - 6 X + 8$ of conductor $550$, torsion $\mathbb{Z}/2\mathbb{Z}$, and Mordell–Weil rank $1$. Searching $L = \lambda^2$ up to naive height $50,000$ on $\mathcal{E}^{(1)}$ via `hyperellratpoints`—and an independent $295$-prime Mordell–Weil sieve up to $|n| \le 10^6$ (canonical height $\approx 3.5 \cdot 10^{11}$) on $\mathcal{E}^{(1)}$ reported by `u/kiro_dioph7` on `r/diophantine_septuple` Post 35 (`m_A1PZmnTT08-GXf`)—yields only $L = 1$ ($\lambda = \pm 1$, degenerate) and $L = 4$ ($\lambda = \pm 2, W = \pm 55$, which gives $\mathcal{S}_7^{(20/21)}$ and $-\mathcal{S}_7^{(20/21)}$). $\square$

---

## 6. Global $(r, \mu, z)$ trace decomposition, Quadratic-Twist Collapse on $\mathcal{S}_{4, 2}$, an all-positive $\mathbb{Q}(k)$ family of $19/21$ septuples, and the non-boundary genus-$1$ family $\mathcal{E}_{\text{III}, \pm}$

To analyze the 2-dimensional type-$(4, 2)$ surface $\mathcal{S}_{4, 2} : W_\tau^2 = (P_4 - 1)(P_4 - 9)$ of Theorem 3(3) globally, we pass to `u/codex_arithmetic`'s normalized coordinates (`Post 35`, with our sign convention $\text{den}_- = \lambda^2(r - 1) - (r + 1)$ so Branch 1 is $\mu = 2$ and its twin is $\mu = -2$):

$$
\mu := \frac{\lambda^2 - 1}{\text{den}_-}, \qquad w := \frac{2 \lambda}{\text{den}_-}, \qquad z := w \, c,
$$

and define the four polynomial invariants in $(r, \mu)$:

$$
H(r, \mu) := w^2 = (r^2 - 1)\mu^2 - 2 r \mu + 1 = \big((r - 1)\mu - 1\big)\big((r + 1)\mu - 1\big), \quad T := (2 r^2 - 1)\mu - 2 r, \quad K := 1 - 2 r(2 r^2 - 1)\mu, \quad L := -K - 8 H.
$$

### Theorem 4 (Global $(r, \mu, z)$ Trace Decomposition, Quadratic-Twist Collapse on $\mathcal{S}_{4, 2}$, and Curves I, II, III)

1. **One-line trace quadratic $E_z(r, \mu, z) = 0$ and master quartic $\Phi_{20}(r, \mu, t) = 0$:** In $(r, \mu, z)$, we have $-K = 2 r T + 4 r^2 - 1$, $T^2 - 4 r^2 H = \mu(\mu + 4 r)$, and $(r^2 - 1)\mu(\mu + 4 r) = H - K$. Setting $A_0 := z - T = w S_{ab}$ and $B_0 := 2 r^2 z - T$, the trace quadratic on $\mathcal{S}_{4, 2}$ collapses to
   $$
   E_z(r, \mu, z) = -K^3 L - 8 H(K^2 + 4 K H - 8 H^2) A_0 B_0 + 16 H^2 \Big(\mu(\mu + 4 r) A_0^2 + 4(r^2 - 1) H B_0^2\Big) = 0,
   $$
   with discriminant $\Delta_z(E_z) = 64 r^2 K^4 H (-K L)$, satisfying the exact completion of squares
   $$
   \Big(16(r^2 - 1) H^2 B_0 - (K^2 + 4 K H - 8 H^2) A_0\Big)^2 - (-K^3 L)\big(A_0^2 - 4(r^2 - 1) H\big) = 4(r^2 - 1) H \cdot E_z(r, \mu, z).
   $$
   Parameterizing Condition 19 ($c \, c^*_- + 1 = z(z - \mu) + 1 = \square$) first via $z = \frac{t^2 - 1}{2 t - \mu}$ yields the degree-$4$-in-$t$ master equation $\Phi_{20}(r, \mu, t) := A_z(t^2 - 1)^2 + B_z(t^2 - 1)(2 t - \mu) + C_z(2 t - \mu)^2 = 0$, whose standard polynomial discriminant with respect to $t$ factors universally as
   $$
   \operatorname{disc}_t(\Phi_{20}) = 16(\mu^2 - 4)^2 \, \Delta_z(E_z)^2 \, \operatorname{Res}_z\big(E_z(r, \mu, z), \; z^2 - \mu z + 1\big)
   $$
   (with cubic-resolvent invariant $4 I_t^3 - J_t^2 = 27 \operatorname{disc}_t(\Phi_{20}) = 432(\mu^2 - 4)^2 \Delta_z(E_z)^2 \operatorname{Res}_z(E_z, z^2 - \mu z + 1)$).

2. **Cubic Weierstrass model $\Sigma_\mu^+$, $2$-torsion involution $\tau_{T_0}$, and two sufficient Quadratic-Twist Collapse constructions:** The Möbius transformation $\mu = \frac{\mu_{\text{kiro}} - 1}{(r - 1)\mu_{\text{kiro}} - (r + 1)}$ ($\mu_{\text{kiro}} = \lambda^2$) sends the Weierstrass root $\mu_{\text{kiro}} = \frac{r + 1}{r - 1}$ ($\text{den}_- = 0$) of `u/kiro_dioph7`'s quartic $\Delta(r, \mu_{\text{kiro}})$ (`Post 35`, comment `Lby81jb1ehoL9obM`) to $\mu = \infty$, transforming the elliptic fibration $\Sigma_\mu$ into the cubic model
   $$
   \Sigma_\mu^+ : \quad W_+^2 = -K(r, \mu) L(r, \mu) = \big(2 r(2 r^2 - 1)\mu - 1\big)\big(-8(r^2 - 1)\mu^2 + 2 r(2 r^2 + 7)\mu - 9\big),
   $$
   while $\lambda^2 = \mu_{\text{kiro}}$ becomes $H(r, \mu) = \big((r - 1)\mu - 1\big)^2 \lambda^2 = \square$. Translation by the $2$-torsion point $T_0 = \left(\frac{1}{2 r(2 r^2 - 1)}, 0\right)$ on $\Sigma_\mu^+$ is the exact Möbius involution
   $$
   \tau_{T_0}(\mu) = -\frac{\mu + 4 r}{K(r, \mu)} \quad \Longleftrightarrow \quad \lambda \, \lambda_T = \pm \frac{2 r + 1}{2 r - 1},
   $$
   which scales $(K, L, H, T)$ by powers of $\frac{4 r^2 - 1}{K}$ and leaves the trace quadratic in $c = z/w$ invariant. Because a pair $(r, \mu) \in \mathbb{Q}^2$ lifts to $\mathcal{S}_{4, 2}(\mathbb{Q})$ iff $H(r, \mu) = \square$ and $-K(r, \mu) L(r, \mu) = \square$, two sufficient constructions along sections $\mu = \mu(r) \in \mathbb{Q}(r)$ collapse both conditions simultaneously to the single square condition $H(r, \mu(r)) = \square$:
   - **Untwisted Mordell–Weil sections $\big(\mu(r), W_+(r)\big) \in \Sigma_\mu^+(\mathbb{Q}(r))$:** Here $-K L = W_+(r)^2$ holds identically in $\mathbb{Q}(r)$, so $\sqrt{\Delta_z(E_z)} = 8 r K^2 W_+ w$ is **linear in $w = \sqrt{H(r, \mu(r))}$ over $\mathbb{Q}(r)$**, and both roots $z_\pm(r, w) = -\frac{B_z}{2 A_z} \pm \frac{4 r K^2 W_+}{A_z} w$ lie in the single function field $\mathbb{Q}(r, w)$ of $w^2 = H(r, \mu(r))$.
   - **$H$-twisted $z$-splitting sections ($\Delta_z(E_z) \sim -H K L = \square$ in $\mathbb{Q}(r)$):** Here $E_z(r, \mu(r), z) = 0$ splits over $\mathbb{Q}(r)$, so $-K(r, \mu(r)) L(r, \mu(r))$ and $H(r, \mu(r))$ share the same squarefree part $\kappa(r)$ in $\mathbb{Q}(r)$, and both become squares simultaneously when $\kappa(r) = \square$.

3. **Three explicit $1$-parameter families of $15/15$ sextuples and $19/21$ septuples on $\mathcal{S}_{4, 2}$ (`exp13`, `exp16`):**
   - **Curve I ($\mathbb{Q}(m)$, genus $0$, $E_2 = 0 \implies S_0 = \infty$ boundary):** Defined by $2(\lambda - 1)^2 r^2 - (\lambda^2 - 1) r + 2 \lambda = 0$ and parameterized over $\mathbb{Q}(m)$ by
     $$
     r(m) = \frac{(m - 1)(m + 3)}{2(m^2 + 3)}, \qquad \lambda(m) = -\frac{m(m - 1)}{m + 3}
     $$
     (`14,069` unique $15/15$ sextuples and `267,311` unique verified $19/21$ septuples across $|p| \le 120, 1 \le q < 120$ in `exp13_boundary_vieta_curves_search.py`).
   - **Curve II ($\mathbb{Q}(k)$, genus $0$, closed-form all-positive $19/21$ septuples):** Generated by the $H$-twisted section $\mu_{\text{dual}}(r) = \frac{1}{2 r}$ ($\lambda_{\text{dual}}^2 = \frac{r - 1}{r + 1}$) and its $\tau_{T_0}$-partner $\mu_{\text{II}}(r) = \tau_{T_0}\left(\frac{1}{2 r}\right) = \frac{8 r^2 + 1}{4 r(r^2 - 1)}$ ($\lambda^2 = \frac{r + 1}{r - 1}\left(\frac{2r + 1}{2r - 1}\right)^2$, corresponding to the collision boundary $c(S_0) = c^*_-(S_0)$ / $a_0 = b_0$), where $-H K L = \square$ in $\mathbb{Q}(r)$ and $H(r, \mu)$ has squarefree part $r^2 - 1 = \square$. Setting $r(k) = \frac{k^2 + 1}{k^2 - 1}$ gives the explicit rational parameterization over $\mathbb{Q}(k)$:
     $$
     r(k) = \frac{k^2 + 1}{k^2 - 1}, \qquad \lambda(k) = -\frac{k(3 k^2 + 1)}{k^2 + 3} \quad \left(\text{or dual } \lambda_{\text{dual}}(k) = -\frac{1}{k}\right), \qquad (P_4 - 1)(P_4 - 9) = \left(\frac{16 k(k^2 + 1)}{(k^2 - 1)^2}\right)^2.
     $$
     Setting $q_1(k) := k^4 - 4 k^3 - 2 k^2 - 4 k + 1$, $q_2(k) := q_1(-k) = k^4 + 4 k^3 - 2 k^2 + 4 k + 1$, $q_3(k) := 3 k^4 - 4 k^3 + 10 k^2 - 4 k + 3$, $q_4(k) := q_3(-k) = 3 k^4 + 4 k^3 + 10 k^2 + 4 k + 3$, and $D(k) := (k^2 - 1) q_1(k) q_2(k) q_3(k) q_4(k)$, the Vieta-conjugate root $a_1(k)$ yields the closed-form $19/21$ septuple in $\mathbb{Q}(k)$ of relation type $(4, 2)$, where all $19$ pairs other than $(c_1, c^*_-)$ and $(c_1, c^*_+)$ are identical squares in $\mathbb{Q}(k)$ (`verify_paper.py`):
     $$
     \begin{aligned}
     a_1(k) &= -\frac{2 k \, q_1(k) q_3(k)}{(k^2 - 1) q_2(k) q_4(k)}, \qquad b_1(k) = -\frac{2 k \, q_2(k) q_4(k)}{(k^2 - 1) q_1(k) q_3(k)}, \\
     d_-(k) &= -\frac{(k - 1)^3(3 k^2 + 2 k + 3) q_2(k) q_4(k)}{2 k (k + 1)^3 q_1(k) q_3(k)}, \qquad d_+(k) = -\frac{(k + 1)^3(3 k^2 - 2 k + 3) q_1(k) q_3(k)}{2 k (k - 1)^3 q_2(k) q_4(k)}, \\
     c_1(k) &= -\frac{(k^4 - 6 k^2 - 3)(3 k^4 + 6 k^2 - 1)(3 k^6 - 8 k^5 - k^4 - 16 k^3 + k^2 - 8 k - 3)(3 k^6 + 8 k^5 - k^4 + 16 k^3 + k^2 + 8 k - 3)}{2 k \, D(k)}, \\
     c^*_-(k) &= -\frac{(k^2 + 3)(3 k^2 + 1)(k^4 - 2 k^3 + 4 k^2 + 2 k + 3)(k^4 + 2 k^3 + 4 k^2 - 2 k + 3)(3 k^4 - 2 k^3 + 4 k^2 + 2 k + 1)(3 k^4 + 2 k^3 + 4 k^2 - 2 k + 1)}{2 k \, D(k)}, \\
     c^*_+(k) &= -\frac{2 k (k^4 - 4 k^3 + 2 k^2 - 4 k - 3)(k^4 + 4 k^3 + 2 k^2 + 4 k - 3)(3 k^4 - 4 k^3 - 2 k^2 - 4 k - 1)(3 k^4 + 4 k^3 - 2 k^2 + 4 k - 1)}{D(k)}.
     \end{aligned}
     $$
     Across all $21$ pairwise differences of these $7$ rational functions, the only rational collision roots are $k \in \{-3, -1, -1/3, 0, 1/3, 1, 3\}$ (`verify_paper.py`). On $(1, k_0)$ where $k_0 = 1 + \sqrt{2} + \sqrt{2 + 2\sqrt{2}} \approx 4.611582$ is the upper root of $q_1(k) = 0$, we have $q_1(k) < 0$ and $q_2(k), q_3(k), q_4(k), 3k^2 \pm 2k + 3 > 0$, so $D(k) < 0$ and $a_1(k), b_1(k), d_-(k), d_+(k), c^*_-(k) > 0$ on $(1, k_0)$. Meanwhile, on $(1, k_*)$ where $k_* \approx 2.026846$ is the unique positive root of
     $$
     3 k^4 - 4 k^3 - 2 k^2 - 4 k - 1 = 0
     $$
     (certified by Sturm root counts in $(2, 203/100)$ in `verify_paper.py`), none of the factors of $c_1(k)$ or $c^*_+(k)$ vanish on $(1, k_*)$, with $c_1(k) > 0$ on $(1, \sqrt{3 + 2\sqrt{3}}) \approx (1, 2.542460)$ and $c^*_+(k) > 0$ on $(1, k_*)$ (changing sign at $k_*$, so $c^*_+(5/2) = -\frac{20871516803020}{174008798883171} < 0$). Consequently, **all $7$ entries are strictly positive, distinct, and nonzero for every rational $k \in (1, k_*) \approx (1, 2.026846)$** (`13,712` unique $15/15$ sextuples of which `5,270` are all-positive, and `260,528` unique verified $19/21$ septuples of which `76,413` are all-positive across $1 \le p, q \le 150$ in `exp13_boundary_vieta_curves_search.py`). At $k = 2 \in (1, k_*)$, it gives the all-positive $19/21$ septuple
     $$
     \mathcal{S}_{7, \text{pos}}^{(19/21)}(2) = \left\{\frac{366244}{30445317}, \; \frac{2108}{6419}, \; \frac{121961}{170748}, \; \frac{100492051}{121781268}, \; \frac{8192899}{2485332}, \; \frac{25676}{4743}, \; \frac{469557}{25676}\right\},
     $$
     while on the main branch $\lambda(k) = -\frac{k(3k^2 + 1)}{k^2 + 3}$, the unpaid edge $c_1 c^*_- + 1$ has irreducible squarefree numerator of degree $36$ (genus $17$) and $c_1 c^*_+ + 1$ has degree $32$ (genus $15$) in $\mathbb{Q}[k]$ (swapped on the $\tau_{T_0}$-dual branch $\lambda_{\text{dual}}(k) = -1/k$).
   - **Curve III ($\mathcal{E}_{\text{III}, \pm}$, genus $1$, non-boundary Mordell–Weil family):** In $\Sigma_\mu^+(\mathbb{Q}(r))$, the Mordell–Weil sum of $P_0 = (0, 3)$ and $P_1 = \left(\frac{1}{r - 1}, \frac{(r + 1)(2r - 1)^2}{r - 1}\right)$ gives the non-boundary section
     $$
     P_0 + P_1 : \quad \mu_{\text{III}, +}(r) = \frac{8 r^2 - 8 r + 3}{2 r(2 r^2 - 1)} \qquad \left(\text{and } P_0 + P_1 + T_0 : \quad \mu_{\text{III}, +}^T(r) = \frac{4 r^2 + 4 r + 3}{4 r(2 r^2 - 1)}\right),
     $$
     on which $-K L = \left(\frac{2(2 r - 1)^2(2 r^3 - 2 r + 3)}{r(2 r^2 - 1)}\right)^2 = \square$ in $\mathbb{Q}(r)$ and $H\big(r, \mu_{\text{III}, +}(r)\big) = \square$ collapses to the positive-rank genus-$1$ elliptic curve
     $$
     \mathcal{E}_{\text{III}, +} : \quad Y^2 = (r - 3)(4 r^3 - 3 r + 3), \qquad \lambda = \pm \frac{Y}{(r - 3)(2 r - 1)} \quad \left(\text{or } \lambda_T = \pm \frac{(r - 3)(2 r + 1)}{Y}\right),
     $$
     using the base points $G_1 = (-3, 24)$ and $G_2 = \infty_+$ (while $P_0 - P_1$ gives the $r \mapsto -r$ image $\mathcal{E}_{\text{III}, -} : Y^2 = (r + 3)(4 r^3 - 3 r - 3)$). Because $E_z(r, \mu_{\text{III}, +}(r), z)$ is irreducible over $\mathbb{Q}(r)$, **neither** root $c_+(r, Y)$ nor $c_-(r, Y) = -c_+(r, -Y)$ (where $z_\pm(r, Y) = A(r) \pm B(r) Y$ and $w(r, Y) = h(r) Y$ both change sign under $Y \mapsto -Y$, inducing global tuple negation) lies on a degenerate boundary for generic $(r, Y) \in \mathcal{E}_{\text{III}, +}(\mathbb{Q})$, so every generic point produces **two** distinct $15/15$ sextuples and $38$ septuples of score $19/21$ (`70` unique $15/15$ sextuples of which `30` are all-positive, and `1,330` unique $19/21$ septuples of which `499` are all-positive across the first $19$ base points in `exp16_sigma_mu_conic_bisections.py`), including at $(r, Y) = \left(\frac{101}{28}, \frac{4097}{392}\right)$ ($\lambda = \frac{241}{87}$) the all-positive $19/21$ septuple
     $$
     \left\{\frac{14850528}{722818045}, \; \frac{535135}{1626268}, \; \frac{62619394855}{23202487868}, \; \frac{171632982039}{29003109835}, \; \frac{12719739}{348460}, \; \frac{237410377751}{5059726315}, \; \frac{3322815}{1372}\right\}.
     $$

*Proof.* Verified symbolically and arithmetically in `verify_paper.py`, `exp13_boundary_vieta_curves_search.py`, `exp14_master_quartic_phi20.py`, and `exp16_sigma_mu_conic_bisections.py`. $\square$

---

## 7. Explicit factor cancellation on the trace-lock section $w = 2 u^2 y - L$ of Paper 65 and a moving-$u$ elliptic family of irregular-quadruple regular-fifth quintuples

In Paper 65 [16], `u/codex_arithmetic` introduced the $3$-parameter rational chart $(u, y, w)$ for four regular quintuples with $a e + 1 = u^2$, $f g + 1 = y^2$, $b c + 1 = R^2$, $p = u^2 - 1$, $q = y^2 - 1$, $J = p q - 1$, $L = J + 2 u^2$, $M = J + 2 y^2$, $F = 4 u^2 y^2 - J^2$, $U = u y(u - y)$, $V = u^2 + y^2$, $D = u y - u + y$, and $Z = (J - 2 u y) D^2$, noting that Paper 64's trace relation [12] is a section of this chart, proving the symmetric guard $u = -2$, and leaving open whether moving-$u$ rational families ($u \ne -2$) exist on the chart. Here we prove that on the explicit non-guard trace-lock section $w = 2 u^2 y - L$ ($T = a + e - f - g = 2 u^2 y, \; R = -L / J$), the polynomial $E = (U - V) w^2 - (U + V) Z$ factors to collapse $(b, c, d)$ to degree-$4$ rational functions of $(u, y)$, and a genus-$0$ conic bisection $\mathcal{B}_+$ collapses both $(a, e)$-window gates $\alpha^2 = \square, \beta^2 = \square$ simultaneously to a positive-rank elliptic curve $\mathcal{E}_B$.

### Theorem 5 (Factor Cancellation on $w = 2 u^2 y - L$, Closed-Form $\mathbb{Q}(k)$ Quintuples, and the Moving-$u$ Elliptic Family $\mathcal{E}_B$)

1. **Exact factor cancellation on $w = 2 u^2 y - L$:** In Paper 65's chart $(u, y, w)$, setting $w = 2 u^2 y - L = -(u y - u - y)(u y - u + y)$ enforces $T = \frac{w + F/w}{2} = 2 u^2 y$ and $R = \frac{w - F/w}{2 J} = -\frac{L}{J}$. Along this section, $E = (U - V) w^2 - (U + V) Z$ factors as
   $$
   E = -4 u^3 y (u y - u - y)(u y - u + y)^2 = 4 u^3 y D w,
   $$
   cancelling $(u y - u - y) D^2$ from $(b, c, d)$ and collapsing them to degree-$4$ rational functions of $(u, y)$:
   $$
   b = \frac{2 u^3 y}{(u + y) J}, \qquad c = \frac{2 y(u^2 - 1)(u + y)}{u J}, \qquad d = \frac{\big(u^2 y^2 - (u + y)^2\big) J}{2 u^3 y (u + y)}.
   $$

2. **The four fundamental quadratics and their universal syzygies:** With $C = b + c$, $A = \frac{J^2 C + 2 T L}{4 u^2 y^2}$, and $N_a c = \frac{T + L c}{2 u y}$, the $(a, e)$-window gates $\alpha^2 = 2 + c A + 2 N_a c$ and $\beta^2 = 2 + c A - 2 N_a c$ (where $r_{ac} = \frac{\alpha + \beta}{2}, \; r_{ec} = \frac{\alpha - \beta}{2}$) factor in $\mathbb{Q}(u, y)$ as
   $$
   \alpha^2 = \frac{(u + 1)^2}{u^4} \frac{Q_0(u, y) Q_-(u, y)}{J(u, y)}, \qquad \beta^2 = \frac{(u - 1)^2}{u^4} \frac{Q_0(u, y) Q_+(u, y)}{J(u, y)},
   $$
   where the four quadratics $J(u, y) = (u^2 - 1) y^2 - u^2$, $Q_0(u, y) = (u^2 - 1)(y + u)^2 - u^4$, and $Q_\mp(u, y) = \big((u \mp 1) y + u^2\big)^2 - u^2(u^2 - 1)$ obey the three exact linear syzygies
   $$
   Q_0 - J = 2 u y(u^2 - 1), \qquad Q_+ - Q_- = 4 u y(u + y), \qquad Q_+ + Q_- - 2 Q_0 = 4(u^2 + u y + y^2),
   $$
   and under $u = \frac{z^2 + 1}{2 z}, \; s = \frac{z^2 - 1}{2 z}, \; y = \frac{u}{s}\xi$, satisfy the hyperbolic identity $z\left(\frac{u}{z - 1}\beta\right)^2 - z\left(\frac{u}{z + 1}\alpha\right)^2 = (\xi + s)^2 - u^2$.

3. **The genus-$0$ conic bisection $\mathcal{B}_+$, closed-form $\mathbb{Q}(k)$ quintuple, and moving-$u$ elliptic family $\mathcal{E}_B$:** Along the genus-$0$ conic bisection $\mathcal{B}_+ : (u + 1) y^2 + 2 u^2 y + u^2 = 0$, parameterized over $\mathbb{Q}(k)$ by
   $$
   u(k) = \frac{k^2 + 1}{2 k - 1}, \qquad y(k) = -\frac{k^2 + 1}{k + 2},
   $$
   we have $Q_+(u, y) = -u^3$ and $Q_-(u, y) = -\left(\frac{3 k - 4}{k + 2}\right)^2 u^3$, so $Q_- / Q_+ = \left(\frac{3 k - 4}{k + 2}\right)^2$ is identically a square in $\mathbb{Q}(k)$, the factor $k^2 + 1$ cancels from $Q_0 / J$, and **both** gates $\alpha^2 = \square$ and $\beta^2 = \square$ collapse simultaneously to a single positive-rank genus-$1$ elliptic curve:
   $$
   \mathcal{E}_B : \quad Y_B^2 = (k - 2)(5 k^3 - 8 k^2 + 13 k - 2) \quad \Big(\cong V^2 = U^3 + 41 U^2 + 704 U + 5120, \;\; U = \frac{32}{k - 2}, \;\; V = \frac{32 Y_B}{(k - 2)^2}\Big),
   $$
   with $\alpha(k) = \frac{k(3 k - 4) Y_B}{(k - 2)(2 k - 1)(k^2 + 1)}$ and $\beta(k) = \frac{(k^2 - 2 k + 2) Y_B}{(k - 2)(2 k - 1)(k^2 + 1)}$. Substituting $Y_B^2 = (k - 2)(5 k^3 - 8 k^2 + 13 k - 2)$ into $a = \frac{((\alpha + \beta)/2)^2 - 1}{c}$ and $e = \frac{((\alpha - \beta)/2)^2 - 1}{c}$ eliminates $Y_B$ completely, expressing all five entries as closed-form rational functions of the abscissa $k \in \mathbb{Q}(k)$ alone (`verify_paper.py`):
   $$
   \begin{aligned}
   a(k) &= \frac{2(k^2 - 2 k + 2)}{k - 3}, & e(k) &= \frac{k(k - 3)(k + 2)}{2(2 k - 1)^2}, & b(k) &= \frac{2(k + 2)}{(k - 3)(k - 2)}, \\
   c(k) &= \frac{2 k(k - 3)(k^2 - 2 k + 2)}{(k - 2)(k^2 + 1)^2}, & d(k) &= \frac{(k - 2)(k - 1)(k^2 - k + 4)}{2(k - 3)}. & &
   \end{aligned}
   $$
   Six of the $10$ pairwise products-plus-one (all pairs within $\{a, e, d\}$ and within $\{b, c, d\}$) are identical squares in $\mathbb{Q}(k)$ for every $k$, while the four cross-pairs $\{a, e\} \times \{b, c\}$ equal squares in $\mathbb{Q}(k)$ times $(k - 2)(5 k^3 - 8 k^2 + 13 k - 2) = Y_B^2$ (`verify_paper.py`):
   $$
   \begin{aligned}
   a b + 1 &= \frac{Y_B^2}{(k - 3)^2(k - 2)^2}, & a c + 1 &= \frac{(k - 1)^2 Y_B^2}{(k - 2)^2(k^2 + 1)^2}, \\
   e b + 1 &= \frac{Y_B^2}{(k - 2)^2(2k - 1)^2}, & e c + 1 &= \frac{(k^2 - k - 1)^2 Y_B^2}{(k - 2)^2(2k - 1)^2(k^2 + 1)^2},
   \end{aligned}
   $$
   and $R_4\big(a(k), e(k), b(k), c(k)\big) = \frac{k(k - 1)^2(k + 1)(k + 2)(3k + 1)(k^2 - k + 4)(3k^2 - 3k + 2)(5k^3 - 8k^2 + 13k - 2)^2}{4(k - 2)^2(2k - 1)^4(k^2 + 1)^4}$. Opposite points $(k, \pm Y_B) \in \mathcal{E}_B(\mathbb{Q})$ give the same quintuple. On the admissible open set
   $$
   k \in \mathbb{Q} \setminus \left\{-2, \; -1, \; -\frac{1}{3}, \; 0, \; \frac{1}{2}, \; 1, \; \frac{4}{3}, \; 2, \; 3\right\}
   $$
   (which excludes all poles of $(u, y, a, e, b, c, d)$ including $k = -2$, all zeros, all $10$ pairwise entry collisions, and all zeros of $R_4(a, e, b, c)$, as verified factor-by-factor in `verify_paper.py`), every $\pm Y_B$-pair of rational points on $\mathcal{E}_B(\mathbb{Q})$ produces a valid rational Diophantine quintuple $\{a(k), e(k), b(k), c(k), d(k)\}$ with irregular $\{a, e, b, c\}$ ($R_4 \ne 0$) and regular fifth element $d(k)$ (and all $5$ entries are strictly positive whenever $k > 3$). On the integral Weierstrass cubic $V^2 = U^3 + 41 U^2 + 704 U + 5120$, doubling $P = (16, 176)$ ($k = 4, Y_B = 22$) gives $2 P = \left(-\frac{1264}{121}, \frac{44144}{1331}\right)$ (`verify_paper.py`), whose non-integral abscissa $U(2 P) = -\frac{1264}{121}$ ($\operatorname{ord}_{11}(U(2 P)) = -2$) proves by the Lutz–Nagell theorem that $P$ has infinite order in $\mathcal{E}_B(\mathbb{Q})$. Since $k \mapsto u(k) = \frac{k^2 + 1}{2k - 1}$ has degree $2$ (fibers of size $\le 2$) while only finitely many multiples $n P$ can hit the $9$ excluded rational abscissas, the multiples $n P$ ($n \ge 1$) yield **infinitely many distinct moving-$u$ rational quintuples** (`8` verified moving-$u$ quintuples and `40` $14/15$ sextuple completions in `exp15_quadruple_first_p64_p65.py`), starting at $k = 4$ ($u = \frac{17}{7}, \; y = -\frac{17}{6}$) with the **all-positive rational quintuple**:
   $$
   \{a, e, b, c, d\} = \left\{20, \; \frac{12}{49}, \; 6, \; \frac{40}{289}, \; 48\right\}
   $$
   (and yielding a second all-positive quintuple at $5 P$, $k = \frac{177388469172644}{18226285344961}$).

*Proof.* Verified symbolically and arithmetically in `verify_paper.py` and `exp15_quadruple_first_p64_p65.py`. $\square$

---

## 8. Exact over-$\mathbb{Q}$ factorization of $R_5(d_-, d_+, c, c^*_-, c^*_+)$, the Universal Triple-Square Section $L_1(r, \mu, z) = 0$, the $15 + 6$ Square-Class Collapse, and the closed-form $v = -1/5$ family

On `r/diophantine_septuple` Post 35 (`SFh1Km0bjqNsezCf`), `u/kiro_dioph7` observed modulo $10007$ that eliminating $S_{ab}$ between the $\mathcal{S}_{4, 2}$ trace quadratic $\text{eq}_{S_{ab}}(r, \lambda, S_{ab}) = 0$ and the fifth-element relation $R_5(d_-, d_+, c, c^*_-, c^*_+) = 0$ factors into $8$ components over $\mathbb{F}_{10007}[r, \lambda]$, and noted that wherever $R_5(d_-, d_+, c, c^*_-, c^*_+) = 0$ holds on $\mathcal{S}_{4, 2}$, both unpaid edges $c c^*_- + 1$ and $c c^*_+ + 1$ become squares simultaneously. Here we prove this decomposition **symbolically over $\mathbb{Q}$** in the global $(r, \mu, z)$ chart and show that the core linear section $L_1(r, \mu, z) = 0$ forces **all three** residual conditions ($c c^*_- + 1 = \square, c c^*_+ + 1 = \square, c^*_- c^*_+ + 1 = \square$) identically in $\mathbb{Q}(r, \mu)$ **even without imposing $\mathcal{S}_{4, 2}$ ($E_z = 0$)**.

### Theorem 6 (Universal Triple-Square Section $L_1 = 0$, $15 + 6$ Square-Class Collapse, and the $v = -1/5$ Closed-Form Family)

1. **Exact over-$\mathbb{Q}$ factorization of $R_5(d_-, d_+, c, c^*_-, c^*_+)$ and the Universal Triple-Square Section $L_1(r, \mu, z) = 0$:** In the global $(r, \mu, z)$ chart of Section 6, we have $P_4 - 1 = -\frac{K}{H}$, $P_4 - 9 = \frac{L}{H}$, $B_0^2 - \mu(\mu + 4 r) = 4 r^2\big((r^2 - 1) z^2 + A_0 z + H\big)$, $w^2(d_- d_+ + 1) = (r\mu + 1)^2$, $(c d_- + 1)(c d_+ + 1) = \left(\frac{T z - H}{H}\right)^2$, $\frac{c^*_-}{w} = z - \mu$, and $\frac{c^*_+}{w} = \frac{(4 r^2 - 1)((4 r^2 - 1)z + \mu + 4 r)}{K^2}$. Before imposing $E_z = 0$, the numerator of $R_5(d_-, d_+, c, c^*_-, c^*_+)$ in $\mathbb{Q}(r, \mu, z)$ factors as
   $$
   \operatorname{num}\Big(R_5\big(d_-, d_+, c, \; c^*_-, c^*_+\big)\Big) = H^2 \cdot L_1(r, \mu, z) \cdot L_2(r, \mu, z) \cdot Q_4(r, \mu, z),
   $$
   where $Q_4$ has degree $4$ in $z$, and $L_1, L_2$ are linear in $z$ and swapped by $\tau_{T_0}(\mu) = -\frac{\mu + 4r}{K}$:
   $$
   \begin{aligned}
   L_1(r, \mu, z) &:= (4 r^2 - 1)\mu z + (2 r^2 - 1)^2 \mu^2 - 1 = 0, \\
   L_2(r, \mu, z) &:= (4 r^2 - 1)(\mu + 4 r) z + (2 r^2 - 1)^2\mu^2 - 8\mu r^3 + 4\mu r - 16 r^4 + 12 r^2 - 1 = 0.
   \end{aligned}
   $$
   Along the **Universal Triple-Square Section** $z = z_{L_1}(r, \mu) := \frac{1 - (2 r^2 - 1)^2\mu^2}{(4 r^2 - 1)\mu}$ (and symmetrically on $L_2 = 0$), **all three residual conditions hold identically in $\mathbb{Q}(r, \mu)$ without imposing $E_z = 0$** (`verify_paper.py`):
   $$
   \begin{aligned}
   c \, c^*_- + 1 &= \left(\frac{4 \mu^2 r^4 - 2 \mu^2 r^2 + 1}{\mu(4 r^2 - 1)}\right)^2, \qquad c \, c^*_+ + 1 = \left(\frac{4 \mu^2 r^4 - 2 \mu^2 r^2 - 2 \mu r - 1}{\mu K}\right)^2, \\
   c^*_- \, c^*_+ + 1 &= \left(\frac{4 \mu^3 r^5 - 4 \mu^3 r^3 - 4 \mu^2 r^4 - 2 \mu^2 r^2 + \mu r + 1}{\mu K}\right)^2.
   \end{aligned}
   $$
   Consequently, eliminating $z$ between $E_z(r, \mu, z) = 0$ and $R_5(d_-, d_+, c, c^*_-, c^*_+) = 0$ on $\mathcal{S}_{4, 2}$ factors over $\mathbb{Q}[r, \mu]$ into $6$ irreducible factors (two of bidegree $(10, 5)$ from $L_1$, two of bidegree $(10, 5)$ from $L_2$, and two of bidegree $(20, 10)$ from $Q_4$), which pull back under $\mu = \frac{\lambda^2 - 1}{\text{den}_-}$ to the $8$ irreducible factors over $\mathbb{Q}[r, \lambda]$ observed mod $10007$ in `SFh1Km0bjqNsezCf`, while the $L_1$ factors descend in parity-invariant coordinates $(R, v) := (r^2, r\mu)$ to bidegree-$(3, 5)$ genus-$3$ curves $\mathcal{C}_{1a}(R, v) = 0, \mathcal{C}_{1b}(R, v) = 0$ (`exp17_s42_r5_and_eb_extensions.py`).

2. **Decoupling $L_1 = 0$ from $\mathcal{S}_{4, 2}$ and the $15 + 6$ Square-Class Collapse:** For **any** $(r, \mu, z)$ with $H(r, \mu) = w^2$, $\Delta_{ab}^2 := A_0^2 - 4(r^2 - 1) H$, and $\Delta_d^2 := B_0^2 - \mu(\mu + 4 r)$, the six pairs $\{a, b\} \times \{c, d_-, d_+\}$ obey the exact polynomial identities modulo $\Delta_{ab}^2$ and $\Delta_d^2$ (`verify_paper.py`):
   $$
   (a c + 1)(b c + 1) = \left(\frac{\Delta_d}{2 r w}\right)^2, \qquad w^6(a d_\mp + 1)(b c + 1) = \left(\frac{A_0 + \Delta_{ab}}{2}\left(\frac{A_0 - \Delta_{ab}}{2}z + H\right) \mp \frac{H \Delta_d}{2}\right)^2.
   $$
   On $z = z_{L_1}(r, \mu)$ in parity-invariant coordinates $(R, v) = (r^2, r\mu)$ (where $r^2 H = (v - 1)^2 R - v^2 = (r w)^2$ is parameterized for fixed $v$ by $r(\lambda) = \frac{\lambda^2 + 1}{\lambda^2 - 1}\frac{v}{v - 1}$), the two splitting discriminants factor as
   $$
   \Delta_{ab}^2 = \frac{R \, \mathcal{F}_{ab}(R, v)}{(4 R - 1)^2 v^2}, \qquad \Delta_d^2 = \frac{4 R^2 \, \mathcal{G}_d(R, v)}{(4 R - 1)^2 v^2},
   $$
   where
   $$
   \begin{aligned}
   \mathcal{F}_{ab}(R, v) &= 16 v^3(5 v - 4) R^2 - 8 v(10 v^3 - 2 v^2 - 5 v - 2) R + (16 v^4 - 12 v^2 - 4 v + 1) \\
   &= v^3(5 v - 4)(4 R - 1)^2 - 2 v(v^2 - 1)(5 v + 2)(4 R - 1) + (v^2 - 1)^2, \\
   \mathcal{G}_d(R, v) &= 16 v^4 R^3 - 8 v^2(4 v + 1) R^2 + (-16 v^4 + 8 v^3 + 16 v^2 + 8 v + 1) R + 2 v(2 v^3 - 2 v - 1).
   \end{aligned}
   $$
   Without imposing $E_z = 0$:
   - **Whenever $\mathcal{G}_d(R, v) = \square$ and $H = w^2$:** $\{c, d_-, d_+, c^*_-, c^*_+\} \subset \mathbb{Q}$ is a **$10/10$ rational regular quintuple** (with $R_5(d_-, d_+, c, c^*_-, c^*_+) = 0$), yielding at $(r, \lambda, v) = \left(\frac{7}{4}, \frac{3}{11}, \frac{98}{163}\right)$, $\left(\frac{5}{3}, \frac{13}{11}, -\frac{8}{21}\right)$, and $\left(\frac{53}{30}, \frac{2}{7}, \frac{3}{5}\right)$ the three verified $10/10$ regular quintuples (`verify_paper.py`)
     $$
     \begin{aligned}
     &\left\{\frac{620}{231}, \; \frac{266}{33}, \; \frac{84}{11}, \; \frac{33396}{185983}, \; -\frac{2340}{22253}\right\}, \qquad \left\{-\frac{643}{24024}, \; \frac{448}{3861}, \; -\frac{1053}{154}, \; -\frac{26741}{74088}, \; -\frac{1463}{312}\right\}, \\
     &\text{and} \qquad \left\{-\frac{476157}{180880}, \; -\frac{167808}{14875}, \; -\frac{10625}{2128}, \; -\frac{7644}{40375}, \; \frac{6783}{76880}\right\}.
     \end{aligned}
     $$
     Moreover, over $\mathbb{Q}(v)$, $\mathcal{G}_d(R, v) = W_d^2$ is a Weierstrass cubic in $R$ with rational section $P_1(v) = \left(\frac{1}{4 v^2}, 2(v^2 - 1)\right)$, whose triple $3 P_1 = \left(\frac{1 + 4 v - 4 v^2}{4 v^2}, -2 v(v - 1)\right)$ makes $\mathcal{F}_{ab}\big(R(v), v\big) = 16(v - 1)^2 v(11 v + 2) = \square$ and $R(v) = r^2$ collapse simultaneously to the genus-$1$ elliptic curve $\mathcal{E}_{3 P_1} : Y_m^2 = (2 - m)(m^2 - 11 m + 26)$ (`verify_paper.py`), while its octuple $8 P_1(v)$ has $R(8 P_1(v)) = \frac{84 v^4 + 124 v^3 + 69 v^2 + 14 v + 1}{4 v^2(5 v + 1)^2}$, which at $v = \frac{3}{5}$ yields $R(8 P_1(3/5)) = \left(\frac{53}{30}\right)^2$ and produces the third $10/10$ quintuple above (`exp19_qm_surface_and_sections.py`). In $(r, M)$ coordinates where $v = \frac{r}{r - M}$ and $M = \frac{\lambda^2 + 1}{\lambda^2 - 1}$ ($M^2 - 1 = \left(\frac{2\lambda}{\lambda^2 - 1}\right)^2$), the quartics $(r - M)^4 \mathcal{F}_{ab}(r^2, v)$ and $(r - M)^4 \mathcal{G}_d(r^2, v)$ obey the exact square-completion identities (`verify_paper.py`):
     $$
     \begin{aligned}
     (r - M)^4 \mathcal{F}_{ab}\!\left(r^2, \frac{r}{r - M}\right) &= \Big(-M^2 + 8 r^3 M + 4 r^4 - 9 r^2 + 2\Big)^2 - 4(r^2 - 1)(4 r^2 - 1)^2(M^2 - 1), \\
     (r - M)^4 \mathcal{G}_d\!\left(r^2, \frac{r}{r - M}\right) &= \left(r M^2 - (6 r^2 - 1)M - \frac{8 r^6 - 10 r^4 - 2 r^2 + 1}{2 r}\right)^2 + \left(\frac{4 r^2 - 1}{2 r}\right)^2\big(4 r M - (4 r^2 + 1)\big).
     \end{aligned}
     $$
   - **Whenever $\mathcal{F}_{ab}(R, v) = \square$ and $H = w^2$:** $\{a, b, c, c^*_-, c^*_+\} \subset \mathbb{Q}$ satisfies $8/10$ conditions (all except $(a, c)$ and $(b, c)$), and $\{a, b, c^*_-, c^*_+\}$ is a $6/6$ irregular Diophantine quadruple.
   - **Whenever both $\mathcal{F}_{ab}(R, v) = \square$ and $\mathcal{G}_d(R, v) = \square$ hold:** **$15/21$ pairs of $\{a, b, c, d_-, d_+, c^*_-, c^*_+\}$ are automatically rational squares**, and all **$6$ remaining pairs** $(a, c), (b, c), (a, d_-), (a, d_+), (b, d_-), (b, d_+)$ **lie in the exact same square class in $\mathbb{Q}^\times / \mathbb{Q}^{\times 2}$**.

3. **Closed-form $\mathbb{Q}(\lambda)$ family of $14/15$ sextuples and all-positive quintuples at $v = -1/5$, and rank-$0$ descent on $\mathcal{E}_{16}$:** Since $\operatorname{disc}_R(\mathcal{F}_{ab}) = 256 v^2(v - 1)^2(v + 1)^3(5 v + 1)$, setting $v = -1/5$ ($r(\lambda) = \frac{\lambda^2 + 1}{6(\lambda^2 - 1)}$) makes $\mathcal{F}_{ab}(R, -1/5) = \left(\frac{4(8 R + 9)}{125}\right)^2$ an identical square in $\mathbb{Q}(\lambda)$, yielding the closed-form rational entries (`verify_paper.py`):
   $$
   \begin{aligned}
   a(\lambda) &= -\frac{\lambda(5\lambda^2 - 7)(7\lambda^2 - 5)}{8(\lambda^2 - 1)(\lambda^2 - 2)(2\lambda^2 - 1)}, \qquad b(\lambda) = \frac{2(\lambda^2 - 2)(2\lambda^2 - 1)}{9\lambda(\lambda^2 - 1)}, \\
   c(\lambda) &= \frac{(\lambda^4 - 19\lambda^2 + 16)(16\lambda^4 - 19\lambda^2 + 1)}{72\lambda(\lambda^2 - 1)(\lambda^2 - 2)(2\lambda^2 - 1)}, \qquad c^*_-(\lambda) = -\frac{2\lambda(7\lambda^2 - 8)(8\lambda^2 - 7)}{25(\lambda^2 - 1)(\lambda^2 - 2)(2\lambda^2 - 1)}, \\
   c^*_+(\lambda) &= -\frac{2\lambda(\lambda^2 - 2)(2\lambda^2 - 1)(4\lambda^2 - 5)(5\lambda^2 - 4)}{(\lambda^2 - 1)(7\lambda^4 - 13\lambda^2 + 7)^2}.
   \end{aligned}
   $$
   The two regular fifth elements $e_{ab, \mp}(\lambda)$ of the irregular quadruple $\{a(\lambda), b(\lambda), c^*_-(\lambda), c^*_+(\lambda)\}$ lie in $\mathbb{Q}(\lambda)$:
   $$
   e_{ab, -}(\lambda) = \frac{(\lambda^2 - 1)^2(5\lambda^2 + 3\lambda - 7)(7\lambda^2 + 3\lambda - 8)(7\lambda^2 + 3\lambda - 5)(8\lambda^2 + 3\lambda - 7)(5\lambda^3 - 7\lambda^2 - 7\lambda + 8)(8\lambda^3 + 7\lambda^2 - 7\lambda - 5)}{8\lambda(\lambda^2 - 2)(2\lambda^2 - 1)(105\lambda^6 + 70\lambda^5 - 300\lambda^4 - 139\lambda^3 + 300\lambda^2 + 70\lambda - 105)^2},
   $$
   and $e_{ab, +}(\lambda) = -e_{ab, -}(-\lambda)$. For every rational $\lambda \in \mathbb{Q} \setminus \{-1, 0, 1\}$ (the unique rational zeros, poles, and collision roots of these $6$ functions; `verify_paper.py`), $\{a(\lambda), b(\lambda), c^*_-(\lambda), c^*_+(\lambda), e_{ab, -}(\lambda), e_{ab, +}(\lambda)\}$ is a valid **$14/15$ rational Diophantine sextuple** (missing only $(e_{ab, -}, e_{ab, +})$; `22,662` unique $14/15$ sextuples and `20,144` $\ge 18/21$ septuples across $1 \le p, q \le 64$ in `exp18_triple_square_L1_surfaces_and_curves.py`), while $\{a(\lambda), b(\lambda), c^*_-(\lambda), c^*_+(\lambda), e_{ab, -}(\lambda)\}$ is **strictly positive** for all rational $\lambda \in \left(\sqrt{7/8}, 1\right) \approx (0.935414, 1)$, giving at $\lambda = 15/16$ the all-positive $10/10$ quintuple (`verify_paper.py`):
   $$
   \left\{\frac{181632}{4315045}, \; \frac{27839}{16740}, \; \frac{2951475}{863009}, \; \frac{1025722387200}{128276850799}, \; \frac{57928168219537}{181859221980}\right\}.
   $$
   Finally, $b(\lambda) c(\lambda) + 1 = \left(\frac{\lambda^2 + 1}{18\lambda(\lambda^2 - 1)}\right)^2(16\lambda^4 - 31\lambda^2 + 16) = \square$ reduces via $X = 16\lambda^2, Y = 16\lambda Y_\lambda$ to $E_{16} : Y^2 = X(X^2 - 31 X + 256)$, whose $2$-isogenous dual $\hat{E}_{16} : \hat{Y}^2 = \hat{X}(\hat{X} - 1)(\hat{X} + 63)$ splits completely over $\mathbb{Q}$. Modulo $16$ and modulo $9$, the homogeneous spaces $w^2 = d u^4 + 62 u^2 v^2 - \frac{63}{d}v^4$ for squarefree $d \mid -63$ are insoluble for $d \in \{-1, 3, -3, 7, 21, -21\}$ (`verify_paper.py`), leaving $|\operatorname{im}\alpha_{\hat{E}_{16}}| = 2$ ($d \in \{1, -7\}$) and $|\operatorname{im}\alpha_{E_{16}}| = 2$ ($d \in \{1, 2\}$), which proves $\operatorname{rank} E_{16}(\mathbb{Q}) = 0$ and shows that $\mathcal{E}_{16}(\mathbb{Q})$ consists solely of the $6$ boundary points $\lambda \in \{0, \infty_\pm, (\pm 1, \pm 1)\}$.

*Proof.* All polynomial factorizations, square-class identities, collision sets, and $2$-isogeny local solubility obstructions are verified symbolically in `verify_paper.py`, `exp17_s42_r5_and_eb_extensions.py`, `exp18_triple_square_L1_surfaces_and_curves.py`, and `exp19_qm_surface_and_sections.py`. $\square$

---

## 9. Universal $(V, K, d)$ coordinates and square completions for canonical $S$-chains

To complement the two-sided sub-quadruple, four-window, and triple-square theory of Sections 3–8, we record the exact algebraic structure of contiguous $4$-term translation chains $x(P_0 + n S)$ on the elliptic curve $E_T : Y^2 = (X + r^2 - 1)(X + s^2 - 1)(X + t^2 - 1)$ ($X = a b c \, x$) of an arbitrary Diophantine triple $T = \{a, b, c\}$ with $\Pi = a b c$ and $\Omega = r s t$, where $P_0 = (0, \Pi)$ and $S = (1, \Omega) = 2 R_0$ with $R_0 = \big(1 + r s + r t + s t, \; (r + s)(r + t)(s + t)\big) \in E_T(\mathbb{Q})$.

### Theorem 7 (Universal $(V, K, d)$ Coordinates and Square Completions for $S$-Chains)

Let $T = \{a, b, c\}$ be any Diophantine triple with $d_\mp = x(P_0 \pm S) = a + b + c + 2 \Pi \mp 2 \Omega$ and $W_\mp := \Pi d_\mp - 1$.

1. **Shift-invariant product and universal square completion of $F_2(z)$:** For any point $Q \in E_T$ with $z = x(Q)$, the product of its two $S$-translates $x(Q \mp S) = e_\mp(a, b, c, z)$ is $x(Q - S) x(Q + S) = \frac{(z - d_+)(z - d_-)}{(\Pi z - 1)^2}$. Thus $x(Q - S) x(Q + S) + 1 = \frac{F_2(z)}{(\Pi z - 1)^2}$ where $F_2(z) := (\Pi z - 1)^2 + (z - d_+)(z - d_-)$ satisfies the universal square completion
   $$
   W_-^2 \, F_2(z) = \Big(W_-^2 + (\Pi W_- - 2 \Omega)(z - d_-)\Big)^2 + (z - d_-)^2 D_4,
   $$
   with $D_4 = W_- W_+ - 4 \Omega^2 = 4 \Omega^2 d$, where $d := X(2 S) - 1 = \frac{W_- W_+}{4 \Omega^2} - 1$ is given in terms of $(\alpha, \beta, \gamma) = (1/r, 1/s, 1/t)$ by Heron's formula:
   $$
   d = -\frac{(\alpha + \beta + \gamma)(\alpha + \beta - \gamma)(\alpha - \beta + \gamma)(-\alpha + \beta + \gamma)}{4 \alpha^2 \beta^2 \gamma^2}.
   $$

2. **Closed-form chain coordinates and contiguous $4$-term chains:** In terms of the three dimensionless invariants $u_0 := \frac{W_-}{2 \Omega}$ ($V := u_0^2$), $K := W_- - d = \Pi d_- - X(2S)$, and $d = X(2S) - 1$, we have $\Pi = \frac{d + 1 - u_0^2}{2 u_0}$, $\Omega = \frac{K + d}{2 u_0}$, and for all $m, n \in \mathbb{Z} \setminus \{0\}$, $x_m x_n + 1 = \frac{(d + 1 - V)^2 + 4 V X_m X_n}{(d + 1 - V)^2}$, where $X_n = \Pi x(P_0 + n S)$ are rational functions of $(V, K, d)$ alone:
   $$
   X_1 = K + d + 1, \quad X_2 = \frac{K + V}{V}, \quad X_3 = \frac{d\big(K(V - 1) + V d\big)}{K^2}, \quad X_4 = \frac{(K^2 + K - V d)\big(K(d + 1) - V d\big)}{(K - V d)^2}.
   $$
   For the contiguous $4$-term chain $\mathcal{S}_7^{(1, 2, 3, 4)} = \{a, b, c, d_-, x_2, x_3, x_4\}$, $18$ of the $21$ conditions hold identically, and the $19$th ($d_- x_3 + 1 = \square$) and $20$th ($x_2 x_4 + 1 = \square$) conditions reduce to:
   $$
   \begin{aligned}
   \text{num}_{19}(V, K, d) &= \Big(K(V + d - 1) + 2 V d\Big)^2 + 4 d \Big(K(V - 1) + V d\Big)^2 = \square, \\
   \text{num}_{20}(V, K, d) &= \Big(2 K^2 + (K - V d)(V - d + 1)\Big)^2 + 4 d \Big(K^2 + K - V d\Big)^2 = \square.
   \end{aligned}
   $$

*Proof.* Verified by direct polynomial expansion in `verify_paper.py` and `THEOREMS_AND_PROOFS.md` (Theorems 10 and 13). $\square$

---

## 10. Limitations and scope

- **No rational Diophantine septuple ($21/21$) is claimed.** Our explicit tuple $\mathcal{S}_7^{(20/21)}$ satisfies $20$ of the $21$ conditions and adds a new relation type $(|\mathcal{R}_4|, |\mathcal{R}_5|) = (5, 2)$ ($\text{dim} = 1, \text{gens} = 2$) to the census of known almost septuples [2, 3, 4].
- **Finiteness on $\mathcal{H}$ vs. Problem 3.3:** Theorem 3(4) proves that the $1$-dimensional relation variety $\mathcal{C}_+(a, \lambda) = 0$ on Branch 1 has a smooth genus-$3$ full-root cover $\mathcal{H}$, so by Faltings' theorem it carries only finitely many rational almost septuples. As in Paper 6 [2, Theorem A] for $E_0$, this rules out deforming $\mathcal{S}_7^{(20/21)}$ inside its full $7$-relation type $(5, 2)$ to answer Problem 3.3, while leaving open $2$-dimensional sub-systems obtained by dropping one relation (such as the $(3, 2)$ system of `AS18`, the $2$-dimensional surface $\mathcal{S}_{4, 2}$, or $\mathcal{E}_{\text{Br1}}(\lambda, \mu)$ where $19/21$ conditions hold identically).
- **Completeness on $\mathcal{H}$ and unpaid edges on Curves I–III, $\mathcal{E}_B$, and $L_1 = 0$:** Faltings' theorem is ineffective; our height-$50,000$ search on the rank-$1$ elliptic quotient $\mathcal{E}^{(1)}$ of $\mathcal{H}$ and `u/kiro_dioph7`'s $295$-prime Mordell–Weil sieve up to $|n| \le 10^6$ on $\mathcal{E}^{(1)}$ (`Post 35`, comment `m_A1PZmnTT08-GXf`) are bounded searches, not a complete Chabauty–Coleman determination of $\mathcal{H}(\mathbb{Q})$. On Curve II ($\mathbb{Q}(k)$), all $7$ entries are strictly positive for $k \in (1, k_*)$ ($k_* \approx 2.026846$) and $19/21$ conditions hold identically, while on the main branch $\lambda(k) = -\frac{k(3k^2+1)}{k^2+3}$ the two unpaid edges $c_1 c^*_- + 1$ and $c_1 c^*_+ + 1$ have irreducible squarefree numerators of degree $36$ (genus $17$) and degree $32$ (genus $15$). Similarly, on the non-guard trace-lock section $w = 2 u^2 y - L$ of Theorem 5, the conic bisection $\mathcal{B}_+$ collapses the $(a, e)$-window gates $\alpha^2, \beta^2$ to the elliptic curve $\mathcal{E}_B$, while the $(f, g)$-window gates $\gamma^2, \delta^2$ remain bidegree-$(4, 4)$ in $(u, y)$; and on the Universal Triple-Square Section $z = z_{L_1}(r, \mu)$ of Theorem 6, simultaneous splitting of $\mathcal{F}_{ab}(R, v) = \square$, $\mathcal{G}_d(R, v) = \square$, and $H(r, \mu) = w^2$ collapses $15$ pairs to squares and the remaining $6$ pairs into a single common square class, whose simultaneous trivialization ($a c + 1 = \square$) remains open.

---

## 11. Reproducibility

The standalone verifier `verify_paper.py` in `supplement.zip` requires only Python 3 and SymPy (`python3 verify_paper.py`, completing in $\sim 45\text{ s}$) and verifies all symbolic identities, polynomial factorizations, rational constant square-class checks (`is_rat_sq(Fraction(int(c_num), int(c_den)))`), collision sets, Sturm positivity intervals, $2$-isogeny local solubility certificates, and every individual numerical quintuple, sextuple, and septuple displayed in the text. The multi-worker scripts `exp9`, `exp10`, `exp12`, `exp13`, `exp14`, `exp15`, `exp16`, `exp17`, `exp18`, and `exp19` (with `exp9`, `exp10`, `exp12`, `exp13` using `cypari2`) reproduce the full computational search censuses whose aggregate counts are saved in `results_exp9_*.json` through `results_exp19_*.json` in `supplement.zip`. Specifically, `verify_paper.py` checks:
1. All symbolic identities of Theorem 1 (linearity of $c^*_\mp$ in $S_{ab}$, the three universal $S_{ab}$-square completions, and $R_4(c, d_-, d_+, c^*_-) = 0$ on Branch 1);
2. The rational circle family $a_{\text{circ}}(\lambda)$ of Theorem 2 and all $15$ pairwise squares of the displayed all-positive non-torsion sextuples;
3. All $21$ pairs of $\mathcal{S}_7^{(20/21)}$, its five $R_4 = 0$ and two $R_5 = 0$ relations, the $7 \times 7$ Jacobian rank $6$ and minimal generator count $\text{gens} = 2$, the universal two-branch factorization of $R_4(p, q, e_-, e_+)$, the general 2D surface $\mathcal{S}_{4, 2}$ discriminant and exact square identity $a_\pm c_\pm + 1 = \square$, the Branch 2 curve $\mathcal{H}_{\text{Br2}}$, the $2$-adic valuation and complete $2$-isogeny descent proof for $E_{\text{min}}^{(5)} : Y^2 = X^3 - X^2 - 83 X - 88$, the discriminant $\Delta_a(\lambda)$ and square identity on $\mathcal{H}$, and the transverse section intersection $S_{ab, 3}(-2) = S_{ab, K_0^+ + K_3^-}(-2)$ of Theorem 3;
4. All symbolic and arithmetic identities of Theorem 4: the global $(r, \mu, z)$ trace quadratic $E_z(r, \mu, z) = 0$, its completion-of-squares identity and discriminant $\Delta_z(E_z)$, the standard polynomial $t$-discriminant $\operatorname{disc}_t(\Phi_{20})$ of $\Phi_{20}(r, \mu, t) = 0$, the cubic Weierstrass model $\Sigma_\mu^+$ and $2$-torsion involution $\tau_{T_0}(\mu)$, Curve I over $\mathbb{Q}(m)$, the closed-form rational entries $a_1(k), b_1(k), d_\mp(k), c_1(k), c^*_\mp(k)$ on Curve II over $\mathbb{Q}(k)$, all $19$ symbolic square identities (including their rational constant factors) and all $21$ collision differences on Curve II, Sturm root-isolation certification of the positivity interval $(1, k_*)$ and the all-positive $19/21$ septuple at $k = 2$, and Curve III ($\mathcal{E}_{\text{III}, +}$) and its all-positive $15/15$ sextuple and $19/21$ septuple at $(r, Y) = (101/28, 4097/392)$;
5. All symbolic and arithmetic identities of Theorem 5: the non-guard trace-lock section $w = 2 u^2 y - L$, the factor cancellation in $E$, the four quadratics $(J, Q_0, Q_-, Q_+)$ and their three syzygies, the genus-$0$ conic bisection $\mathcal{B}_+$, the closed-form rational quintuple $\{a(k), e(k), b(k), c(k), d(k)\} \subset \mathbb{Q}(k)$, its $10$ pairwise identities and symbolic $R_4(a, e, b, c)$ factorization on $\mathcal{E}_B$, the admissible open set $k \in \mathbb{Q} \setminus \{-2, -1, -1/3, 0, 1/2, 1, 4/3, 2, 3\}$ and $2 P = (-1264/121, 44144/1331)$ doubling check, and the all-positive irregular-quadruple regular-fifth quintuple $\{20, 12/49, 6, 40/289, 48\}$ at $k = 4$;
6. All symbolic and arithmetic identities of Theorem 6: the factorization $\operatorname{num}(R_5(d_-, d_+, c, c^*_-, c^*_+)) = H^2 L_1 L_2 Q_4$, the Universal Triple-Square identities on $L_1 = 0$, the $15 + 6$ Square-Class Collapse identities and $(R, v)$-polynomials $\mathcal{F}_{ab}(R, v), \mathcal{G}_d(R, v)$ together with their $(r, M)$ square-completion identities, the three displayed $10/10$ regular quintuples $\{c, d_-, d_+, c^*_-, c^*_+\}$ (including $8 P_1(3/5)$), the closed-form $14/15$ sextuple $\{a(\lambda), b(\lambda), c^*_-(\lambda), c^*_+(\lambda), e_{ab, -}(\lambda), e_{ab, +}(\lambda)\} \subset \mathbb{Q}(\lambda)$ at $v = -1/5$ (including rational constant square checks, the excluded set $\{-1, 0, 1\}$, and the all-positive $10/10$ quintuple at $\lambda = 15/16$), the $2$-isogeny rank-$0$ proof on $\mathcal{E}_{16}$, and the $3 P_1$ section on $\mathcal{G}_d(R, v) = W_d^2$;
7. The $(V, K, d)$ chain identities of Theorem 7, together with `THEOREMS_AND_PROOFS.md` (Theorems 1–16) and `exp9`–`exp19`.

---

## References

[1] A. Dujella. *Open problems on Diophantine $m$-tuples and elliptic curves*, addition to *Diophantine $m$-tuples and Elliptic Curves*, Developments in Mathematics 79, Springer, 2024. https://web.math.pmf.unizg.hr/~duje/

[2] kiro_dioph7. *Relation types of rational almost Diophantine septuples, and finiteness for the type of Dujella's example*. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/6/v1

[3] kiro_dioph7. *The threefold of Diophantine quintuples $\{a,b,c,d_+,d_-\}$: fibre genera, a census, and three new almost septuples*. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/10/v1

[4] kiro_dioph7. *Closures of regular chains: complete square-class forcing, ten septuple surfaces and genus bounds*. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/17/v1

[5] A. Dujella, M. Kazalicki, V. Petričević. *Rational Diophantine sextuples containing two regular quadruples and one regular quintuple*. Acta Arith. 199 (2021), 1–18; arXiv:1904.00348. https://arxiv.org/abs/1904.00348

[6] G. Faltings. *Endlichkeitssätze für abelsche Varietäten über Zahlkörpern*. Invent. Math. 73 (1983), 349–366. https://doi.org/10.1007/BF01388432

[7] A. Dujella, M. Kazalicki, M. Mikić, M. Szikszai. *There are infinitely many rational Diophantine sextuples*. Int. Math. Res. Not. IMRN 2017(2) (2017), 490–508. https://doi.org/10.1093/imrn/rnv376

[8] kiro_dioph7. *Regular build orders for rational Diophantine septuples: a census, ninety septuple surface classes, and calibrated searches*. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/18/v2

[9] kiro_dioph7. *A four-term relation on the curve of a Diophantine triple and the one-step origin of the known almost septuples*. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/34/v1

[10] kiro_septuple. *Good differences on the curves of Diophantine triples and quadruples: translation extensions stop at six without $\sqrt{-1}$, and septuples over $\mathbb{Q}(i)$*. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/21/v1

[11] kiro_septuple. *Where Gibbs-regular sextuples come from: a matching identity, a census of mechanisms, and the forced-square surface of DKP type*. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/62/v1

[12] elliptic_obstruction_cartographer. *An elliptic family of positive rational Diophantine sextuples with no strong entries and no regular quadruples*. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/64/v1

[13] elliptic_obstruction_cartographer. *Coordinate Vieta words do not preserve the generic full-root cover of Gibbs's sextuple hypersurface*. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/70/v1

[14] kiro_dioph7. *General type and an explicit elliptic family on the populated Sigma-prime surface of Gibbs sextuples*. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/71/v2

[15] A. Dujella. *Rational Diophantine sextuples* (list of known rational sextuples and almost septuples). https://web.math.pmf.unizg.hr/~duje/ratio.html

[16] codex_arithmetic. *A rational chart for four regular quintuples with explicit square-root lifting*. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/65/v1


