## 1. Problem, Definitions, and Contributions

A rational Diophantine $m$-tuple is a set of $m$ distinct nonzero rational numbers $\{a_1,\dots,a_m\} \subset \mathbb{Q}^\times$ such that $1 + a_i a_j \in \mathbb{Q}^2$ for all $1 \le i < j \le m$. Infinitely many rational Diophantine sextuples ($m = 6$) are known [1, 2, 3], whereas no rational Diophantine septuple ($m = 7$) is known [4], and whether infinitely many $20/21$ *almost septuples* exist remains open [4] (Problems 3.2 and 3.3).

Among the known infinite families of rational sextuples, the **Piezas–Dujella–Kazalicki fibration** [2] occupies a central geometric position. Fix a rational parameter $m \in \mathbb{Q} \setminus \{0, \pm 1, 1/2\}$ and set

$$
A(m) = m^2 - 1, \qquad B(m) = \frac{2m - 1}{(m - 1)^2}, \qquad P(m) = A(m) B(m) = \frac{(m + 1)(2m - 1)}{m - 1}.
$$

Consider Diophantine quadruples $(x_1, x_2, x_3, x_4)$ satisfying the disjoint-pair product constraints $x_1 x_3 = A(m)$ and $x_2 x_4 = B(m)$, so that $1 + x_1 x_3 = m^2$ and $1 + x_2 x_4 = \left(\frac{m}{m - 1}\right)^2$ are automatically rational squares [2, 5]. On such quadruples, let $b, c$ denote the two regular fifth elements of $\{x_1, x_2, x_3, x_4\}$ [6]:

$$
b, c = \frac{(1 + P) S_4 + 2 U_4 \pm 2 R_6}{(P - 1)^2},
$$

where $S_4 = \sum_{i=1}^4 x_i$, $U_4 = P \sum_{i=1}^4 x_i^{-1}$, and $R_6 = \prod_{1 \le i < j \le 4} r_{ij}$ with $r_{ij}^2 = 1 + x_i x_j$. On the Piezas locus $(A(m), B(m))$, the fifteenth radicand $1 + bc$ is identically a square [2, 5]: writing $S = x_1 + x_3$ and $T = x_2 + x_4$, one has

$$
r_{bc} = \frac{m - 1}{2 m^2}(S - T), \qquad 1 + bc = r_{bc}^2.
$$

Over each non-boundary parameter $m$, the rooted Piezas sextuples $(x_1, x_2, x_3, x_4, b, c; (r_{ij}))$ form an abelian surface $A_m$ isogenous over $\mathbb{Q}(m)$ to the self-product $E_m \times E_m$ of the smooth elliptic curve

$$
E_m \colon Y^2 = X(X + 1)(X + P(m)),
$$

which is in turn $2$-isogenous over $\mathbb{Q}(m)$ to the elliptic curve $\mathcal{E}_m$ introduced by Dujella and Kazalicki [2] (§2).

### Enumerated Classical Seventh-Entry Formulas and Extension Degrees

To avoid ambiguity in degree terminology, let $\mathcal{K}_m = \mathbb{Q}(m)(A_m)$ denote the function field of the *rooted* Piezas surface (where all six entries $X = (x_1, x_2, x_3, x_4, b, c)$ and all fifteen edge roots $r_{ij}$ are rational functions). For any algebraic candidate seventh coordinate $y \in \overline{\mathcal{K}_m}^\times$, two distinct degrees arise:

1. the **coordinate definition degree** $[\mathcal{K}_m(y) : \mathcal{K}_m]$ required to adjoin $y$ itself to the rooted sextuple field (versus degree $\le 2$ over the *unrooted* symmetric sextuple field when $y$ satisfies a quadratic equation whose discriminant is a product of $r_{ij}^2$); and
2. the **residual root-extension degree** $[\mathcal{K}_m(y, \sqrt{1 + x_1 y}, \dots, \sqrt{1 + x_6 y}) : \mathcal{K}_m(y)]$ required to adjoin all six new seventh-element square roots.

Throughout this paper, all formula-based seventh-entry obstruction claims are restricted to the explicit finite family of **$82$ classical seventh-entry formulas** over $X = (x_1, x_2, x_3, x_4, b, c)$, each having **coordinate definition degree $1$ over the rooted field $\mathcal{K}_m$**:

- **$40$ signed regular-fourth formulas ($R_4$):** for each of the $\binom{6}{3} = 20$ three-subsets $\{u_1, u_2, u_3\} \subset X$, the two branches $d_\pm = u_1 + u_2 + u_3 + 2 u_1 u_2 u_3 \pm 2 r_{12} r_{13} r_{23}$, which already make $1 + u_a d_\pm$ squares in $\mathcal{K}_m$ for $a \in \{1, 2, 3\}$ and leave $3$ residual radicands (generic residual root-extension degree $2^3 = 8$);
- **$30$ signed regular-fifth formulas ($R_5$):** for each of the $\binom{6}{4} = 15$ four-subsets $Q \subset X$ with $\prod_{u \in Q} u \neq 1$, the two Dujella regular fifths $y_{5,\pm}$ [6], which make $1 + u y_{5,\pm}$ squares in $\mathcal{K}_m$ for all $u \in Q$ and leave $2$ residual radicands (generic residual root-extension degree $2^2 = 4$);
- **$12$ signed Gibbs quintuple formulas ($P_6$):** for each of the $\binom{6}{5} = 6$ five-subsets $Q_5 = X \setminus \{x_{\mathrm{omit}}\}$, the two roots $t_{c,\pm}$ of the Gibbs quintuple quadratic $c_2 t^2 + c_1 t + c_0 = 0$ [10, 11], whose five quintuple radicands $1 + q_a t_{c,\pm}$ ($q_a \in Q_5$) all share a single square class $A_{\mathrm{Gb}} \in \mathcal{K}_m^\times / \mathcal{K}_m^{\times 2}$ while $B_{\mathrm{Gb}} = 1 + x_{\mathrm{omit}} t_{c,\pm}$ forms a second residual class (generic residual root-extension degree $2^2 = 4$).

*Remark on [9].* Theorem 2 of [9] proves that on the *universal* rooted sextuple variety, the least residual root-extension degree of a seventh coordinate in the rooted field is $4$, with residual square-class patterns $(0, 0, 0, 0, A, B)$ or $(A, A, A, A, A, B)$ depending on $4$ or $5$ entries. However, [9] does not assert that every coordinate with those patterns must be one of the $30$ $R_5$ or $12$ $P_6$ formulas, nor does it classify constructions arising after specialization to $A_m$ (while non-collision $R_4$ branches have residual root-extension degree $8$). Accordingly, we make **no claim** that the $82$ classical formulas exhaust all algebraic seventh-entry constructions on $A_m$.

### Four Open Questions on $A_m$ and Summary of Results

Building on Dujella–Kazalicki [2] and recent rStation investigations of $A_m$ [5, 7, 8, 21, 23], we address four concrete questions (no rational Diophantine septuple is claimed):

1. **Exact rational torsion specialization on $E_m$ and $\mathcal{E}_m$:** Dujella and Kazalicki [2] (Propositions 2 and 4(d)) proved that their generic section $P_{\mathrm{DK}}(m) \in \mathcal{E}_m(\mathbb{Q}(m))$ has infinite order over $\mathbb{Q}(m)$ and constructed a rationality coset $-P_{\mathrm{DK}}(m) + R_{\mathrm{DK}}(m) + 2 \mathcal{E}_m(\mathbb{Q})$ without requiring $2m - 1 \in \mathbb{Q}^{\times 2}$. By Silverman's specialization theorem, $\operatorname{rank} \mathcal{E}_m(\mathbb{Q}) \ge 1$ holds outside a finite set of rational parameters $m$, but **which exact rational parameters $m \in \mathbb{Q} \setminus \{0, \pm 1, 1/2\}$ specialize that section to torsion** remained undetermined.
   - **Proposition 1 & Theorem 1 (§3):** We exhibit the explicit Vélu $2$-isogenies $\psi \colon E_m \to \mathcal{E}_m$ and $\widehat{\psi} \colon \mathcal{E}_m \to E_m$ and prove symbolically over $\mathbb{Z}[m]$ that $\widehat{\psi}(-P_{\mathrm{DK}}(m) + R_{\mathrm{DK}}(m)) = Q_{\mathrm{univ}}(m) = \left(B(m), \frac{B(m) m^2}{m - 1}\right) \in E_m(\mathbb{Q}(m))$, which carries exact $2$-descent class $(2m - 1, 1)$ on $E_m$. Using $E_m[2](\mathbb{Q}) \cong (\mathbb{Z}/2\mathbb{Z})^2$ and Mazur's torsion theorem, we factor all ten univariate torsion equations (orders $3, 4, 6, 8$) in $\mathbb{Z}[m]$ and prove that **$m = 2$ is the unique non-boundary rational torsion specialization**. Hence $\operatorname{rank} E_m(\mathbb{Q}) = \operatorname{rank} \mathcal{E}_m(\mathbb{Q}) \ge 1$, $\operatorname{rank} A_m(\mathbb{Q}) \ge 2$, and the duplication-coset map $\Phi_m(P_1, P_2) = (2 P_1, Q_{\mathrm{univ}}(m) + 2 P_2)$ embeds a Zariski-dense rank-$\ge 2$ lattice of ordinary rational Piezas sextuples for **every** $m \in \mathbb{Q} \setminus \{0, \pm 1, 1/2, 2\}$.
2. **Degeneracy census, $(\mathbb{Z}/2\mathbb{Z})^3$ orbit structure, and characteristic-zero partial splits among $\{R_4, R_5, P_6\}$:** Proposition 1 of [2] and Proposition 1 of [5] established that $\{x_1, x_3, b, c\}$ and $\{x_2, x_4, b, c\}$ are regular Diophantine quadruples identically on $A_m$. Prior computational checks on $A_m$ [23] sampled only the $70$ ($R_4, R_5$) formulas modulo three small primes ($p \in \{103, 127, 211\}$), omitting the $12$ Gibbs $P_6$ formulas and supplying no characteristic-zero generic proof.
   - **Theorem 2 & Proposition 2 (§4):** From the established double-$R_4$ identities of [2, 5], we prove that exactly **$22 = 8 R_4 + 12 R_5 + 2 P_6$** of the $82$ classical branches degenerate identically on $A_m$ into sextuple entries or $0$, leaving **$60 = 32 R_4 + 18 R_5 + 10 P_6$ non-collision branches** ($308$ non-empty residual $\mathbb{F}_2$-combinations). Under the commuting rooted automorphism group $G = \langle \tau_{13}, \tau_{24}, \tau_{bc} \rangle \cong (\mathbb{Z}/2\mathbb{Z})^3$, these $60$ branches decompose into **$19$ disjoint orbits** ($5 P_6 + 6 R_5 + 8 R_4$, $89$ residual checks). Furthermore, we prove the exact characteristic-zero identities $1 + c d_+ = (S - b)^2 - (4m^2 - 1)$ and $1 + c d'_+ = (T - b)^2 - \frac{(3m - 1)(m + 1)}{(m - 1)^2}$ and—via Kummer norm reduction on the quadric-intersection cover $C_1 \times C_2$ and two-slice Euclidean polynomial GCD in $\mathbb{Q}[m]$ (`verify_all.py`)—prove unconditionally in characteristic zero that the orbits of $\{x_1, x_3, b\}$ and $\{x_2, x_4, b\}$ split on $A_{m_0}$ **if and only if** $m_0 = -1/2$ and $m_0 = 1/3$ respectively (exchanged by $\sigma_{\mathrm{Pz}}(m) = \frac{m}{m - 1}$).
   - **Theorem 3 (§5):** *(a)* On $E_5 \times E_5$ over $\mathbb{Q}$, Auslander–Buchsbaum local factoriality and Hilbert's Theorem 90 certify unconditionally in characteristic zero (`verify_all.py`) that **$0 / 60$** non-collision classical branches ($0 / 308$ residual masks) split generically over $\overline{\mathbb{Q}}(m)$. *(b)* Good reduction at $7$ odd primes (`14` smooth $\mathbb{F}_{p^2}$ fibres in `verify_all.py`) proves unconditionally in characteristic zero that **$0 / 60$** branches split on the smooth CM fibres $P(m_0) = -1$ ($m_0 = \frac{-1 \pm \sqrt{5}}{2}$). *(c)* Pure-stdlib $\mathbb{F}_{p^2}$ witness-pair checks across $8$ primes $p \in \{53, \dots, 89\}$ (`524` fibres in `verify_all.py`) together with guarded two-slice $\mathbb{F}_{q^d}$ truncated square-root elimination at $p \in \{10007, 10009\}$ (Lemma 1; `s2_two_slice_intersection_exact.py`) establish modular special-fibre exclusions across all $10$ primes.
3. **Bielliptic Richelot locus of the seventh-entry genus-$2$ curve $C_X$:**
   - **Theorem 4 (§6.1):** Grouping $C_X \colon y^2 = \prod_{z \in X}(1 + z e)$ into $Q_1, Q_2, Q_3$ gives $Q_3(e) = \frac{1}{m} Q_1(e) + \frac{m - 1}{m} Q_2(e) + \left(r_{bc}^2 - \frac{m^2}{m - 1}\right) e^2$ and $\det(Q_1, Q_2, Q_3) = (T - S)\left(r_{bc}^2 - \frac{m^2}{m - 1}\right)$. For $m = 1 + \tau^2$ ($\tau \in \mathbb{Q}^\times$), $S - T = \pm \frac{2 m^3}{\tau^3}$ projects via $S T = u + v + \frac{P}{u} + \frac{P}{v}$ ($v = B w$) to a **single bidegree-$(2, 2)$ genus-$1$ Kummer curve** $K_{\mathcal{R}} \subset \mathbb{P}^1_u \times \mathbb{P}^1_v$ birational over $\mathbb{Q}(\tau)$ to an explicit Weierstrass cubic $E_{\mathcal{R},\tau}$ of positive generic rank over $\mathbb{Q}(\tau)$ and rank $\ge 1$ at $\tau = 2$ ($m = 5$) certified by Mazur's theorem in `verify_all.py` (with exact ranks $1$ at $m = 5$ and $0$ at $m = 2$ certified by optional algebraic $2$-descent `pari.ellrank`, though quotient points do not automatically lift to $A_m(\mathbb{Q})$). Along $\mathcal{R}_\pm$, the Wronskian involution $\iota(e) = \frac{\alpha e + \beta}{\gamma e - \alpha}$ preserves $Q_1, Q_2, Q_3$ simultaneously and—covered without exception by a Möbius chart on $\gamma \neq 0$ over $k(X)(\sqrt{\Delta_\iota})$ and an affine linear chart on $\gamma = 0$ over $k(X)$—splits $J(C_X) \sim E'_X \times E''_X$.
4. **Corrected height-box and Mordell–Weil coset sieves (§6.2):**
   - Using the exact necessary residue predicate $q(q + x_i p) \in \mathbb{F}_\ell^2$ ($\ell \nmid q$, unit-tested for $100\%$ recall on a verified $15/15 \to 20/21$ control sextuple), an exhaustive $5$-active-prime sieve across **`213` rational Piezas sextuples** (`13` fibres, `0` skipped) and all **`304,462` nonzero coprime rationals** $|p|, q \le 500$ (`64,850,406` pairs), complemented by a **Knapp-halved Mordell–Weil coset sieve** evaluating $(2 c_0 + 1) P_{\mathrm{zero}} + 2 c_1 G_1 + 2 c_2 G_2 + 2 c_3 G_3$ ($|c_j| \le 5$) across **`20` Piezas sextuples spanning all `13` harvested fibres** (`292,820` coefficient vectors across $10$ good primes, retaining all mod-$\ell$ reductions to $\mathcal{O}$ and unit-tested on both $777480/2879^2 \bmod 2879$ and `60/60` sextuple completions, with sampled corner coordinates up to `12,231` bits), finds zero $21/21$ septuples and zero non-classical $20/21$ hits.

---

## 2. Related Work and Exact Attribution

Dujella and Kazalicki [2] (§2) introduced the fibration of Diophantine quadruples with fixed disjoint-pair products, proving that on the Piezas specialization $A(m), B(m)$ the two regular fifths $b, c$ satisfy $1 + bc = r_{bc}^2$ and that both $\{x_1, x_3, b, c\}$ and $\{x_2, x_4, b, c\}$ are regular quadruples [2, Proposition 1]; they also established a generic infinite-order point $P_{\mathrm{DK}}(m)$ and rationality coset $-P_{\mathrm{DK}}(m) + R_{\mathrm{DK}}(m) + 2 \mathcal{E}_m(\mathbb{Q})$ on their elliptic model $\mathcal{E}_m$ [2, Propositions 2 and 4(d)] (see also [3]).

On rStation, [5] constructed a full-root model for the double-Piezas incidence (re-recording the regular-quadruple identities in Proposition 1 and §4 of [5] and proving local solubility everywhere), [23] noted the abelian-surface structure of $A_m$ and ran a $3$-prime modular scan of the $70$ ($R_4, R_5$) candidates, [7] reduced the fixed-pairing common-regular-fifth locus over a varying two-parameter subfamily of Piezas sextuples to an irreducible genus-$20$ curve, [8] proved a complete Chabauty/quadratic-height exclusion for a specific mixed-fifth curve on $m = -1/2$, and [21] established an elliptic Chabauty obstruction over $\mathbb{Q}(\sqrt{-7})$ for the $s = \pm 1$ spoke-ratio Piezas pencil. In the broader sextuple literature, [9] determined the generic residual extension degree $4$, [13] proved general type ($\kappa \ge 0$) for higher $m$-tuple varieties, [11] audited Gibbs $P_6$ regularity across $4388$ sextuples, [20] executed a rank-$68$ genus-$17$ Mordell–Weil sieve on an antipodal quintuple, and [14, 15, 16] studied witness-frame and $P_6$ double-plane surfaces.

Relative to [2, 5, 7, 8, 9, 11, 21, 23], our specific new contributions are:

1. **Explicit dual $2$-isogeny bridge and complete rational torsion classification (Proposition 1 & Theorem 1):** Whereas [2] proves generic infinite order over $\mathbb{Q}(m)$, Proposition 1 identifies $\widehat{\psi}(-P_{\mathrm{DK}}(m) + R_{\mathrm{DK}}(m)) = Q_{\mathrm{univ}}(m)$ on $E_m$ and Theorem 1 determines *every* rational torsion specialization ($m = 2$ uniquely on $\mathbb{Q} \setminus \{0, \pm 1, 1/2\}$).
2. **Classical $82$-formula collision census, $19$-orbit $(\mathbb{Z}/2\mathbb{Z})^3$ table, and characteristic-zero/modular obstructions (Theorems 2 & 3):** Taking the double-$R_4$ identities of [2, Prop. 1; 5, Prop. 1] as established input, we classify all $22$ collisions including Gibbs $P_6$, prove generic non-splitting over $\overline{\mathbb{Q}}(m)$ and smooth $P(m_0) = -1$ non-splitting in characteristic zero, prove characteristic-zero iff conditions for the $-1/2$ and $1/3$ conics via exact function-field norm reduction, and supply guarded modular exclusions across $10$ primes.
3. **Bielliptic Richelot pencil syzygy, universal Weierstrass cubic $E_{\mathcal{R},\tau}$ of $K_{\mathcal{R}}$, and complete two-chart quotient equations (Theorem 4), plus infinity-retaining Mordell–Weil coset sieving (§6.2).**

---

## 3. Dual 2-Isogeny to $\mathcal{E}_m$, Universal Section $Q_{\mathrm{univ}}(m)$, and Mazur Rank Theorem

### 3.1. Kummer Coordinates, 2-Descent Coset Law, and Comparison with [2]

Let $m \in \mathbb{Q} \setminus \{0, \pm 1, 1/2\}$, so $A(m) \neq 0$, $B(m) \neq 0$, $P(m) \neq 0$, and $P(m) - 1 = \frac{2 m^2}{m - 1} \neq 0$; hence $E_m \colon Y^2 = X(X + 1)(X + P(m))$ is smooth. Put $u = x_1 x_2$ and $w = x_1 / x_2$, with $v = B(m) w = B(m) x_1 / x_2$. On a rooted quadruple $(x_1, x_2, x_3, x_4)$ with $x_1 x_3 = A(m)$ and $x_2 x_4 = B(m)$, the four cross-pair radicands decouple into

$$
r_{12}^2 = 1 + u, \quad r_{34}^2 = 1 + \frac{P}{u}, \qquad r_{14}^2 = 1 + v, \quad r_{23}^2 = 1 + \frac{P}{v}.
$$

Setting $U = (u, u r_{12} r_{34})$ and $V = (v, v r_{14} r_{23})$ defines two points in $E_m(\mathbb{Q})$. Conversely, away from $E_m[2](\mathbb{Q}) = \{\mathcal{O}, (0,0), (-1,0), (-P,0)\}$, a pair $(U, V) = ((X_U, Y_U), (X_V, Y_V)) \in E_m(\mathbb{Q})^2$ recovers rational entries $x_1, x_2, x_3, x_4$ and rational roots $r_{ij}$ if and only if

$$
X_U + 1 \in \mathbb{Q}^{\times 2}, \qquad X_V + 1 \in \mathbb{Q}^{\times 2}, \qquad x_1^2 = \frac{X_U X_V}{B(m)} = \frac{(m - 1)^2 X_U X_V}{2m - 1} \in \mathbb{Q}^{\times 2}.
$$

Under the $2$-descent homomorphism $\delta \colon E_m(\mathbb{Q}) \to (\mathbb{Q}^\times / \mathbb{Q}^{\times 2})^2$ given away from $E_m[2]$ by $\delta(X, Y) = (X \bmod \mathbb{Q}^{\times 2}, (X + 1) \bmod \mathbb{Q}^{\times 2})$ with $\ker \delta = 2 E_m(\mathbb{Q})$, these three conditions read

$$
\delta_2(U) = 1, \qquad \delta_2(V) = 1, \qquad \delta_1(U) \delta_1(V) \equiv 2m - 1 \pmod{\mathbb{Q}^{\times 2}}.
$$

To relate $E_m$ directly to Dujella and Kazalicki's elliptic curve [2, §2] (with parameter $t$ written here as $m$), recall their model

$$
\mathcal{E}_m \colon S_{\mathrm{DK}}^2 = T_{\mathrm{DK}}^3 - \frac{2(2 m^2 - m + 1)}{m - 1} T_{\mathrm{DK}}^2 + P(m)^2 T_{\mathrm{DK}},
$$

together with their $\mathbb{Q}(m)$-rational points [2, Propositions 2 and 4(d)]

$$
P_{\mathrm{DK}}(m) = \left(\frac{(2m - 1)^2 (m + 1)}{m - 1}, \, \frac{2m (2m - 1)^2 (m + 1)}{m - 1}\right), \qquad R_{\mathrm{DK}}(m) = \bigl(P(m), \, 2 P(m)\bigr).
$$

**Proposition 1 (Explicit Dual $2$-Isogeny Equivalence with [2]).** *Over $\mathbb{Q}(m)$ ($m \notin \{0, \pm 1, 1/2\}$), translation of $E_m$ by $X = X_1 - 1$ followed by Vélu's $2$-isogeny formula with kernel $\langle (-1, 0) \rangle \subset E_m(\mathbb{Q}(m))$ defines the $2$-isogeny $\psi \colon E_m \to \mathcal{E}_m$ and its dual $\widehat{\psi} \colon \mathcal{E}_m \to E_m$ (with kernel $\langle (0, 0) \rangle \subset \mathcal{E}_m(\mathbb{Q}(m))$ and $\widehat{\psi} \circ \psi = [2]_{E_m}$):*

$$
\psi(X, Y) = \left(\frac{Y^2}{(X + 1)^2}, \, \frac{Y\bigl((X + 1)^2 + P(m) - 1\bigr)}{(X + 1)^2}\right), \qquad \widehat{\psi}(T_{\mathrm{DK}}, S_{\mathrm{DK}}) = \left(\frac{S_{\mathrm{DK}}^2}{4 T_{\mathrm{DK}}^2} - 1, \, \frac{S_{\mathrm{DK}}\bigl(T_{\mathrm{DK}}^2 - P(m)^2\bigr)}{8 T_{\mathrm{DK}}^2}\right).
$$

*Under $\widehat{\psi}$, Dujella and Kazalicki's coset representative $-P_{\mathrm{DK}}(m) + R_{\mathrm{DK}}(m) \in \mathcal{E}_m(\mathbb{Q}(m))$ maps identically to*

$$
\widehat{\psi}\bigl(-P_{\mathrm{DK}}(m) + R_{\mathrm{DK}}(m)\bigr) = Q_{\mathrm{univ}}(m) := \left(B(m), \, \frac{B(m) m^2}{m - 1}\right) \in E_m(\mathbb{Q}(m)).
$$

*Proof.* Writing $E_m$ in $X_1 = X + 1$ gives $Y^2 = X_1^3 + (P - 2) X_1^2 + (1 - P) X_1$, where $P - 2 = \frac{2 m^2 - m + 1}{m - 1} - \frac{2m - 2}{m - 1}$; applying the standard $2$-isogeny $T_{\mathrm{DK}} = Y^2 / X_1^2$, $S_{\mathrm{DK}} = Y(X_1^2 - (1 - P)) / X_1^2$ yields $S_{\mathrm{DK}}^2 = T_{\mathrm{DK}}(T_{\mathrm{DK}}^2 - 2(P + 2) T_{\mathrm{DK}} + (P + 2)^2 + 4(1 - P)) = T_{\mathrm{DK}}^3 - \frac{2(2 m^2 - m + 1)}{m - 1} T_{\mathrm{DK}}^2 + P^2 T_{\mathrm{DK}}$, which is $\mathcal{E}_m$, with standard dual $\widehat{\psi}$. Computing $-P_{\mathrm{DK}}(m) + R_{\mathrm{DK}}(m)$ on $\mathcal{E}_m$ in $\mathbb{Q}(m)$ and applying $\widehat{\psi}$ reduces in $\mathbb{Z}[m]$ (`verify_all.py`, lines 398–455) to $(B(m), B(m) m^2 / (m - 1)) = Q_{\mathrm{univ}}(m)$. $\square$

### 3.2. Proof of Theorem 1 (All-Rational-Parameter Torsion Classification)

Because $\psi$ and $\widehat{\psi}$ are $\mathbb{Q}$-isogenies for every $m \in \mathbb{Q} \setminus \{0, \pm 1, 1/2\}$, $\operatorname{rank} E_m(\mathbb{Q}) = \operatorname{rank} \mathcal{E}_m(\mathbb{Q})$, and working on $E_m$ where all four $2$-torsion points are $\mathbb{Q}(m)$-rational allows an exact classification of every rational parameter at which $Q_{\mathrm{univ}}(m)$ specializes to torsion.

**Theorem 1.** *Let $m \in \mathbb{Q} \setminus \{0, \pm 1, 1/2\}$.*

1. *The rational section $Q_{\mathrm{univ}}(m) = \left(B(m), \frac{B(m) m^2}{m - 1}\right) \in E_m(\mathbb{Q}(m))$ satisfies $\delta(Q_{\mathrm{univ}}(m)) = (2m - 1, 1) \in (\mathbb{Q}^\times / \mathbb{Q}^{\times 2})^2$ and has duplication formula*

$$
X\bigl(2 Q_{\mathrm{univ}}(m)\bigr) = \frac{m^2 (m - 2)^2}{4 (m - 1)^2}, \qquad Y\bigl(2 Q_{\mathrm{univ}}(m)\bigr) = -\frac{m (m - 2)(m^2 - 2m + 2)(m^2 + 2m - 2)}{8 (m - 1)^3}.
$$

2. *The value $m = 2$ is the **unique** parameter in $\mathbb{Q} \setminus \{0, \pm 1, 1/2\}$ at which $Q_{\mathrm{univ}}(m)$ has finite order in $E_m(\mathbb{Q})$ (specifically, $2 Q_{\mathrm{univ}}(2) = (0, 0)$ of exact order $4$, and $\operatorname{rank} E_2(\mathbb{Q}) = \operatorname{rank} \mathcal{E}_2(\mathbb{Q}) = 0$).*
3. *Consequently, for **every** $m \in \mathbb{Q} \setminus \{0, \pm 1, 1/2, 2\}$, $Q_{\mathrm{univ}}(m)$ has infinite order, $\operatorname{rank} E_m(\mathbb{Q}) = \operatorname{rank} \mathcal{E}_m(\mathbb{Q}) \ge 1$, $\operatorname{rank} A_m(\mathbb{Q}) \ge 2$, and the duplication-coset map $\Phi_m(P_1, P_2) = (2 P_1, Q_{\mathrm{univ}}(m) + 2 P_2)$ embeds a Zariski-dense rank-$\ge 2$ lattice into the ordinary rational Piezas sextuples on $A_m(\mathbb{Q})$ (with $(2 Q_{\mathrm{univ}}(m), 5 Q_{\mathrm{univ}}(m))$ giving an explicit one-parameter rational sextuple family).*

*Proof.* (1) Since $B + 1 = \frac{m^2}{(m - 1)^2}$ and $B + P = B(1 + A) = B m^2$, we have $B(B + 1)(B + P) = \left(\frac{B m^2}{m - 1}\right)^2$ and $\delta(Q_{\mathrm{univ}}(m)) = (2m - 1, 1)$; tangent duplication on $E_m$ over $\mathbb{Z}[m]$ gives $X(2 Q_{\mathrm{univ}}(m))$ and $Y(2 Q_{\mathrm{univ}}(m))$ (`verify_all.py`).

(2) Because $E_m[2](\mathbb{Q}) \cong (\mathbb{Z}/2\mathbb{Z})^2$, Mazur's torsion theorem [17] restricts $E_m(\mathbb{Q})_{\mathrm{tors}}$ to $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2n\mathbb{Z}$ with $n \in \{1, 2, 3, 4\}$. Since $B(m) \notin \{0, -1, -P(m)\}$ for $m \notin \{0, \pm 1, 1/2\}$, $Q = Q_{\mathrm{univ}}(m)$ cannot have order $1$ or $2$, so $Q \in E_m(\mathbb{Q})_{\mathrm{tors}}$ if and only if its exact order lies in $\{3, 4, 6, 8\}$—equivalently, one of the ten equations $2Q \in E_m[2]$, $X(2Q) = X(Q + T)$ ($T \in E_m[2]$), or $4Q \in E_m[2]$ holds:

| Torsion test | Equation on $E_m$ | Primitive numerator in $\mathbb{Z}[m]$ | Rational roots |
|---|---|---|---|
| Order $4$ ($T = (0,0)$) | $X(2Q) = 0$ | $m^2 (m - 2)^2$ | $\{0, 2\}$ |
| Order $4$ ($T = (-1,0)$) | $X(2Q) = -1$ | $(m^2 - 2m + 2)^2$ | $\varnothing$ |
| Order $4$ ($T = (-P,0)$) | $X(2Q) = -P$ | $(m^2 + 2m - 2)^2$ | $\varnothing$ |
| Order $3$ ($T = \mathcal{O}$) | $X(2Q) = X(Q)$ | $(m^2 - 4m + 2)(m^2 + 2)$ | $\varnothing$ |
| Order $6$ ($T = (0,0)$) | $X(2Q) = P / X(Q)$ | $(m^2 - 2)(3m^2 - 4m + 2)$ | $\varnothing$ |
| Order $6$ ($T = (-1,0)$) | $X(2Q) = X(Q + (-1,0))$ | $m^4 + 4m^3 - 16m^2 + 16m - 4$ | $\varnothing$ |
| Order $6$ ($T = (-P,0)$) | $X(2Q) = X(Q + (-P,0))$ | $m^4 - 4m^3 + 8m^2 - 4$ | $\varnothing$ |
| Order $8$ ($T = (0,0)$) | $X(4Q) = 0$ | $(m^4 - 6m^3 + 4m^2 + 4m - 4)^2 (m^4 - 2m^3 + 8m^2 - 12m + 4)^2$ | $\varnothing$ |
| Order $8$ ($T = (-1,0)$) | $X(4Q) = -1$ | $(m^8 - 8m^7 + 32m^6 - 48m^5 + 40m^4 - 64m^3 + 96m^2 - 64m + 16)^2$ | $\varnothing$ |
| Order $8$ ($T = (-P,0)$) | $X(4Q) = -P$ | $(m^8 + 8m^7 - 48m^6 + 80m^5 - 24m^4 - 64m^3 + 96m^2 - 64m + 16)^2$ | $\varnothing$ |

The Rational Root Theorem (`verify_all.py`) checks every divisor candidate $p/q$ across all ten primitive polynomials; the only rational roots are $m = 0$ (boundary) and $m = 2$. At $m = 2$, $E_2 \colon Y^2 = X(X + 1)(X + 9)$ has $\operatorname{rank} E_2(\mathbb{Q}) = 0$ (`s2_coset_sieve.json`).

(3) For every $m \in \mathbb{Q} \setminus \{0, \pm 1, 1/2, 2\}$, $Q_{\mathrm{univ}}(m)$ has infinite order, so $\operatorname{rank} E_m(\mathbb{Q}) = \operatorname{rank} \mathcal{E}_m(\mathbb{Q}) \ge 1$ and $\operatorname{rank} A_m(\mathbb{Q}) = 2 \operatorname{rank} E_m(\mathbb{Q}) \ge 2$. Since $\delta(2 P_1) = (1, 1)$ and $\delta(Q_{\mathrm{univ}}(m) + 2 P_2) = (2m - 1, 1)$, every $(P_1, P_2) \in E_m(\mathbb{Q})^2$ outside the finite union of boundary/collision curves on $A_m$ lifts to a non-degenerate rational Piezas sextuple; in particular, $(2 Q_{\mathrm{univ}}(m), 5 Q_{\mathrm{univ}}(m))$ avoids the $R_4$-zero locus $(2 Q_{\mathrm{univ}}, \pm 3 Q_{\mathrm{univ}})$ and yields ordinary $15/15$ sextuples generically (`verify_all.py`). Because $\mathbb{Z} Q_{\mathrm{univ}}(m) \times \mathbb{Z} Q_{\mathrm{univ}}(m)$ has rank $2$ on the surface $E_m \times E_m$ and its coset $(2 a Q_{\mathrm{univ}}, (2 b + 1) Q_{\mathrm{univ}})$ meets any proper Zariski-closed subvariety in a proper subset of $\mathbb{Z}^2$, the image of $\Phi_m$ is Zariski-dense in $A_m$. $\square$

---

## 4. Degeneracy Census, $(\mathbb{Z}/2\mathbb{Z})^3$ Orbits, and Characteristic-Zero Partial Splits

### 4.1. Zero-Radical Duplication Chart and Established Double-$R_4$ Foundation

Over the quadratic cover $2m - 1 = k^2$ ($m = \frac{k^2 + 1}{2}$, $\sqrt{B} = \frac{k}{m - 1}$), the duplication map $[2] \colon E_m \times E_m \to A_m$, $(P_1, P_2) \mapsto (2 P_1, 2 P_2)$ with $P_i = (X_i, Y_i) \in E_m$, expresses all six entries $X = (x_1, x_2, x_3, x_4, b, c)$ and all fifteen edge roots $r_{ij}$ as rational functions without auxiliary radicals:

$$
\begin{aligned}
\sqrt{u} &= \frac{X_1^2 - P}{2 Y_1}, & r_{12} &= \frac{X_1^2 + 2 X_1 + P}{2 Y_1}, & r_{34} &= \frac{X_1^2 + 2 P X_1 + P}{X_1^2 - P}, \\
\sqrt{v} &= \frac{X_2^2 - P}{2 Y_2}, & r_{14} &= \frac{X_2^2 + 2 X_2 + P}{2 Y_2}, & r_{23} &= \frac{X_2^2 + 2 P X_2 + P}{X_2^2 - P},
\end{aligned}
$$

with $x_1 = \frac{\sqrt{u}\sqrt{v}}{\sqrt{B}}$, $x_2 = \frac{\sqrt{u}\sqrt{B}}{\sqrt{v}}$, $x_3 = \frac{A}{x_1}$, $x_4 = \frac{B}{x_2}$, $r_{13} = m$, $r_{24} = \frac{m}{m - 1}$, $r_{bc} = \frac{m - 1}{2 m^2}(S - T)$, and the fifth-element roots $r_{x_i b}, r_{x_i c} = \frac{x_i r_{jk} r_{jl} r_{kl} \pm r_{ij} r_{ik} r_{il}}{P - 1}$ [6].

As established in **Proposition 1 of Dujella–Kazalicki [2]** and **Proposition 1 and §4 of [5]**, on every non-boundary Piezas surface $A_m$ one has $b + c = \frac{1}{m} S + \frac{m - 1}{m} T$, which yields $(S - b - c)^2 = 4(1 + x_1 x_3)(1 + bc)$ and $(T - b - c)^2 = 4(1 + x_2 x_4)(1 + bc)$; hence **both $\{x_1, x_3, b, c\}$ and $\{x_2, x_4, b, c\}$ are regular Diophantine quadruples identically on $A_m$**.

### 4.2. Degeneracy Census, Characteristic-Zero Conic Identities, and $19$-Orbit Decomposition

**Theorem 2.** *On every non-boundary Piezas abelian surface $A_m$ ($m \notin \{0, \pm 1, 1/2\}$):*

1. *(Collision Census Induced by [2, Prop. 1; 5, Prop. 1])* *Among the $82 = 40 R_4 + 30 R_5 + 12 P_6$ enumerated classical seventh-entry branches over $\mathcal{K}_m$, exactly **$22$** degenerate identically on $A_m$: $8$ $R_4$ entry collisions (on the $8$ sub-triples of $\{x_1, x_3, b, c\}$ and $\{x_2, x_4, b, c\}$), $10$ $R_5$ entry collisions (on $\{x_1, x_2, x_3, x_4\}$ and the $8$ four-subsets of $\{x_1, x_2, x_3, x_4, b\}$ and $\{x_1, x_2, x_3, x_4, c\}$), $2$ $R_5$ zero collisions (one branch on each of $\{x_1, x_3, b, c\}$ and $\{x_2, x_4, b, c\}$ outputs $0$), and $2$ Gibbs $P_6$ zero collisions (one branch on each regular quintuple $X \setminus \{c\}$ and $X \setminus \{b\}$ outputs $t_c \equiv 0$). The remaining **$60 = 32 R_4 + 18 R_5 + 10 P_6$** branches are distinct nonzero rational functions not in $X$, producing $32 \times 7 + 18 \times 3 + 10 \times 3 = 308$ non-empty $\mathbb{F}_2$-combinations of residual radicands.*
2. *(Exact Characteristic-Zero Conic Identities and Fibre Involution)* *The involution $\sigma_{\mathrm{Pz}}(m) = \frac{m}{m - 1}$ swaps $(A(m), B(m)) \leftrightarrow (B(m), A(m))$, inducing $A_m \xrightarrow{\sim} A_{\sigma_{\mathrm{Pz}}(m)}$ via $(x_1, x_2, x_3, x_4, b, c) \mapsto (x_2, x_1, x_4, x_3, b, c)$ with $\sigma_{\mathrm{Pz}}(-1/2) = 1/3$. Let $d_+$ denote the non-collision regular fourth of $\{x_1, x_3, b\}$ (the opposite branch to $d_- = c$) and $d'_+$ that of $\{x_2, x_4, b\}$. Then identically in $\mathcal{K}_m$:*

$$
1 + c d_+ = (S - b)^2 - (4 m^2 - 1), \qquad 1 + c d'_+ = (T - b)^2 - \frac{(3m - 1)(m + 1)}{(m - 1)^2}.
$$

*Consequently, for any $m_0 \in \overline{\mathbb{Q}} \setminus \{0, \pm 1, 1/2\}$, $1 + c d_+$ is a square in $\overline{\mathbb{Q}}(A_{m_0})^\times$ **if and only if** $m_0 = -1/2$ (where $d_+ = 2 S - b - c$ satisfies $1 + c d_+ = (S - b)^2$ and $1 + b d_+ = (S - c)^2$), and $1 + c d'_+$ is a square in $\overline{\mathbb{Q}}(A_{m_0})^\times$ **if and only if** $m_0 = 1/3$ (where $d'_+ = 2 T - b - c$ satisfies $1 + c d'_+ = (T - b)^2$ and $1 + b d'_+ = (T - c)^2$).*

*Proof.* (1) In any regular quadruple $\{u_1, u_2, u_3, u_4\}$, $u_4$ is one signed $R_4$ root of $\{u_1, u_2, u_3\}$ ($4 + 4 = 8$ entry collisions) and $0$ is one signed $R_5$ root since $R_5(u_1, u_2, u_3, u_4, 0) = R_4(u_1, u_2, u_3, u_4) = 0$ ($2$ zero collisions). In each regular quintuple $X \setminus \{c\}$ and $X \setminus \{b\}$, each $4$-subset has the fifth entry as one signed $R_5$ root ($2 + 4 + 4 = 10$ entry collisions) and the Gibbs constant term $c_0 = a_0^2 - 4 d_0 = R_5 = 0$ forces one root $t_c \equiv 0$ [10, 11] ($2$ zero collisions). Mutual distinctness and non-degeneracy of the remaining $60$ branches hold at $m = 5$ (`verify_all.py`), hence generically over $\mathcal{K}_m$.

(2) Lemma 1 of [12] gives $1 + d_+ d_- = (u + v - w)^2 - (4 u v + 3)$ for the two regular fourths $d_\pm$ of any Diophantine triple $\{u, v, w\}$. Applying this to $\{x_1, x_3, b\}$ on $A_m$—where $d_- = c$ by [2, Prop. 1] and $x_1 x_3 = m^2 - 1$—yields $1 + c d_+ = (S - b)^2 - (4(m^2 - 1) + 3) = (S - b)^2 - (4 m^2 - 1)$. Applying $\sigma_{\mathrm{Pz}}$ (where $x_2 x_4 = \frac{2m - 1}{(m - 1)^2}$, so $4 x_2 x_4 + 3 = \frac{(3m - 1)(m + 1)}{(m - 1)^2}$) yields the second identity. In particular, at $m_0 = -1/2$ one has $4 m_0^2 - 1 = 0$ so $1 + c d_+ = (S - b)^2$ (and $1 + b d_+ = (S - c)^2$ via $\tau_{bc}$), and at $m_0 = 1/3$ one has $1 + c d'_+ = (T - b)^2$.

Conversely, let $m_0 \in \overline{\mathbb{Q}} \setminus \{0, \pm 1, 1/2\}$ and suppose $1 + c d_+ = (S - b)^2 - (4 m_0^2 - 1)$ is a square in $\overline{\mathbb{Q}}(A_{m_0})^\times$. Fix $k_0 \in \overline{\mathbb{Q}}^\times$ with $k_0^2 = 2 m_0 - 1 \neq 0$; since $P_0 := P(m_0) = \frac{(m_0 + 1)(2 m_0 - 1)}{m_0 - 1} \notin \{0, 1\}$, the two quadric-intersection curves
$$
C_1 \colon \bigl\{r_{12}^2 = 1 + s_1^2, \; \tilde{r}_{34}^2 = s_1^2 + P_0\bigr\}, \qquad C_2 \colon \bigl\{r_{14}^2 = 1 + s_2^2, \; \tilde{r}_{23}^2 = s_2^2 + P_0\bigr\}
$$
are smooth projective genus-$1$ curves over $\overline{\mathbb{Q}}$, and the degree-$2$ map $C_1 \times C_2 \to A_{m_0}$ given by $x_1 = \frac{(m_0 - 1) s_1 s_2}{k_0}$, $x_2 = \frac{k_0 s_1}{(m_0 - 1) s_2}$, $x_3 = \frac{(m_0 + 1) k_0}{s_1 s_2}$, $x_4 = \frac{k_0 s_2}{(m_0 - 1) s_1}$, $r_{34} = \tilde{r}_{34}/s_1$, $r_{23} = \tilde{r}_{23}/s_2$ injects $\overline{\mathbb{Q}}(A_{m_0})^\times \hookrightarrow \overline{\mathbb{Q}}(C_1 \times C_2)^\times$. Putting $W_1 = r_{12} \tilde{r}_{34}$ and $W_2 = r_{14} \tilde{r}_{23}$ (so $R_6 = \frac{m_0^2}{m_0 - 1} \frac{W_1 W_2}{s_1 s_2}$ and $P_0 - 1 = \frac{2 m_0^2}{m_0 - 1}$), clearing Laurent monomials in $(s_1, s_2)$ gives identically (`verify_all.py`)
$$
2 k_0 m_0^2 s_1 s_2 (S - b) = A_{\mathrm{ev}}(m_0, s_1^2, s_2^2) - k_0(m_0 - 1) W_1 W_2,
$$
where $A_{\mathrm{ev}}(m, u, v) = (4 m^4 - 3 m^2 + m - (2 m^2 - m) v) + u\bigl((2 m^3 - 3 m^2 + m) v - 2 m^2 + m\bigr)$. Multiplying $1 + c d_+ \in \overline{\mathbb{Q}}(C_1 \times C_2)^{\times 2}$ by $(2 k_0 m_0^2 s_1 s_2)^2$ shows that
$$
M := \bigl(A_{\mathrm{ev}}(m_0, s_1^2, s_2^2) - k_0(m_0 - 1) W_1 W_2\bigr)^2 - 4(4 m_0^2 - 1)(2 m_0 - 1) m_0^4 s_1^2 s_2^2 = H^2
$$
for some $H \in \overline{\mathbb{Q}}(C_1 \times C_2)^\times$. For each $\lambda \in \{1, 2\}$, choose a smooth point $Q_\lambda = (\lambda, r_{14,\lambda}, \tilde{r}_{23,\lambda}) \in C_2(\overline{\mathbb{Q}})$ and let $D_\lambda = C_1 \times \{Q_\lambda\} \subset C_1 \times C_2$. Since $M \in \overline{\mathbb{Q}}[s_1, s_2, W_1, W_2]$ has $\operatorname{ord}_{D_\lambda}(M) \ge 0$ in the discrete valuation ring $\mathcal{O}_{C_1 \times C_2, D_\lambda}$, whenever $M|_{D_\lambda} \neq 0$ we have $\operatorname{ord}_{D_\lambda}(M) = 0 = 2 \operatorname{ord}_{D_\lambda}(H)$, so $H$ restricts along $D_\lambda$ to $h_\lambda \in \overline{\mathbb{Q}}(C_1)^\times$ with $M|_{D_\lambda} = h_\lambda^2$. Now $M|_{D_\lambda}$ lies in $\overline{\mathbb{Q}}(E'_1) = \overline{\mathbb{Q}}(s_1, W_1)$ ($W_1^2 = (1 + s_1^2)(s_1^2 + P_0)$), over which $\overline{\mathbb{Q}}(C_1) = \overline{\mathbb{Q}}(E'_1)(\sqrt{1 + s_1^2})$ has degree $2$; hence $M|_{D_\lambda} = (1 + s_1^2)^\varepsilon g_\lambda^2$ ($\varepsilon \in \{0, 1\}$, $g_\lambda \in \overline{\mathbb{Q}}(E'_1)^\times$). Because $N_{\overline{\mathbb{Q}}(E'_1)/\overline{\mathbb{Q}}(s_1)}(1 + s_1^2) = (1 + s_1^2)^2$ and $(m_0 - 1)^2 W_1^2 W_2(Q_\lambda)^2 \in \mathbb{Z}[m_0][s_1^2]$ cancels all $(m_0 - 1)$ denominators, taking $N_{\overline{\mathbb{Q}}(E'_1)/\overline{\mathbb{Q}}(s_1)}(M|_{D_\lambda})$ and dividing by $(2 m_0 - 1)^2 \neq 0$ yields a polynomial $H_\lambda(m_0, s_1^2) \in \overline{\mathbb{Q}}[s_1]$ ($H_\lambda(m, u) = \sum_{d=0}^4 c_d(m, \lambda) u^d \in \mathbb{Z}[m][u]$) that is a square in $\overline{\mathbb{Q}}(s_1)$, hence in $\overline{\mathbb{Q}}[s_1]$ by Gauss's lemma. Whenever $c_4(m_0, \lambda) \neq 0$, we have $N(M|_{D_\lambda}) \neq 0$ (so $M|_{D_\lambda} \neq 0$) and $\deg_{s_1} H_\lambda(m_0, s_1^2) = 8$; writing $H_\lambda(m_0, s_1^2) = \bigl(F_{\mathrm{ev}}(s_1^2) + s_1 F_{\mathrm{odd}}(s_1^2)\bigr)^2$ forces $F_{\mathrm{ev}} F_{\mathrm{odd}} = 0$ and $F_{\mathrm{ev}} \neq 0$ (since $\deg_{s_1}(s_1^2 F_{\mathrm{odd}}(s_1^2)^2) \equiv 2 \pmod 4$), so $H_\lambda(m_0, u) = F_{\mathrm{ev}}(u)^2 \in \overline{\mathbb{Q}}[u]^2$. Completing the square on $c_4 u^4 + \dots + c_0$ gives $8 c_4^2 c_1 - c_3 D_{\mathrm{mid}} = 0$ and $64 c_4^3 c_0 - D_{\mathrm{mid}}^2 = 0$ where $D_{\mathrm{mid}} = 4 c_4 c_2 - c_3^2$. Multiplying by $c_4(m, \lambda)$ covers the case $c_4(m_0, \lambda) = 0$ as well, so every admissible $m_0 \in \overline{\mathbb{Q}} \setminus \{0, \pm 1, 1/2\}$ is a common root of $c_4(8 c_4^2 c_1 - c_3 D_{\mathrm{mid}})$ and $c_4(64 c_4^3 c_0 - D_{\mathrm{mid}}^2)$ for both $\lambda = 1$ and $\lambda = 2$. Exact Euclidean polynomial GCD in $\mathbb{Q}[m]$ (`verify_all.py`) gives
$$
\gcd_{\lambda \in \{1, 2\}}\Bigl(c_4(8 c_4^2 c_1 - c_3 D_{\mathrm{mid}}), \; c_4(64 c_4^3 c_0 - D_{\mathrm{mid}}^2)\Bigr) = m^7 \left(m - \frac{1}{2}\right)^2 \left(m + \frac{1}{2}\right),
$$
whose unique root in $\overline{\mathbb{Q}} \setminus \{0, \pm 1, 1/2\}$ is $m_0 = -1/2$. Applying the fibre isomorphism $\sigma_{\mathrm{Pz}}(m) = \frac{m}{m - 1}$ proves $1 + c d'_+ \in \overline{\mathbb{Q}}(A_{m_0})^{\times 2} \iff m_0 = \sigma_{\mathrm{Pz}}(-1/2) = 1/3$. $\square$

**Proposition 2 (Exact $(\mathbb{Z}/2\mathbb{Z})^3$ Orbit Decomposition on Rooted $A_m$).** *In rooted coordinates $(x_1, x_2, r_{12}, r_{34}, r_{14}, r_{23})$ on $A_m$, the three involutions*

$$
\begin{aligned}
\tau_{13}(x_1, x_2, r_{12}, r_{34}, r_{14}, r_{23}) &= \bigl(A/x_1, \, x_2, \, r_{23}, \, r_{14}, \, r_{34}, \, r_{12}\bigr) && \text{(swaps $x_1 \leftrightarrow x_3$, fixes $b, c$)}, \\
\tau_{24}(x_1, x_2, r_{12}, r_{34}, r_{14}, r_{23}) &= \bigl(x_1, \, B/x_2, \, r_{14}, \, r_{23}, \, r_{12}, \, r_{34}\bigr) && \text{(swaps $x_2 \leftrightarrow x_4$, fixes $b, c$)}, \\
\tau_{bc}(x_1, x_2, r_{12}, r_{34}, r_{14}, r_{23}) &= \bigl(-x_1, \, -x_2, \, r_{12}, \, r_{34}, \, r_{14}, \, r_{23}\bigr) && \text{(sends $X \mapsto (-x_1, -x_2, -x_3, -x_4, -c, -b)$)}
\end{aligned}
$$

*commute pairwise and generate $G = \langle \tau_{13}, \tau_{24}, \tau_{bc} \rangle \cong (\mathbb{Z}/2\mathbb{Z})^3$ (where $\tau_{bc}$ negates every seventh-entry candidate $y \mapsto -y$ and therefore preserves every residual radicand $1 + x_j y$ up to entry permutation). Indexing $(x_1, x_2, x_3, x_4, b, c)$ as $(0, 1, 2, 3, 4, 5)$, the $60$ non-collision branches partition into **$19$ disjoint $G$-orbits** totaling $5 \times 3 + 6 \times 3 + 8 \times 7 = \mathbf{89}$ residual square-class checks (`verify_all.py`):*

| Family | Orbit representative | Size | Residual checks | Family | Orbit representative | Size | Residual checks |
|---|---|---:|---:|---|---|---:|---:|
| $P_6$ | `omit 0 (+)` | $2$ | $3$ | $R_5$ | `(1,3,4,5) (+)` | $1$ | $3$ |
| $P_6$ | `omit 0 (-)` | $2$ | $3$ | $R_4$ | `(0,1,2) (+)` | $4$ | $7$ |
| $P_6$ | `omit 1 (+)` | $2$ | $3$ | $R_4$ | `(0,1,3) (+)` | $4$ | $7$ |
| $P_6$ | `omit 1 (-)` | $2$ | $3$ | $R_4$ | `(0,1,4) (+)` | $8$ | $7$ |
| $P_6$ | `omit 4 (-)` | $2$ | $3$ | $R_4$ | `(0,1,4) (-)` | $8$ | $7$ |
| $R_5$ | `(0,1,2,4) (-)` | $4$ | $3$ | $R_4$ | `(0,2,4) (+)` | $2$ | $7$ |
| $R_5$ | `(0,1,3,4) (-)` | $4$ | $3$ | $R_4$ | `(0,4,5) (-)` | $2$ | $7$ |
| $R_5$ | `(0,1,4,5) (+)` | $4$ | $3$ | $R_4$ | `(1,3,4) (+)` | $2$ | $7$ |
| $R_5$ | `(0,1,4,5) (-)` | $4$ | $3$ | $R_4$ | `(1,4,5) (+)` | $2$ | $7$ |
| $R_5$ | `(0,2,4,5) (-)` | $1$ | $3$ | **Total** | **$19$ orbits** | **$60$** | **$89$** |

---

## 5. Obstructions for the 60 Non-Collision Classical Formulas

### 5.1. Unconditional Characteristic-Zero Generic & Golden-Ratio Non-Splitting

**Theorem 3(a)–(b).**

- *(a) Generic non-splitting over $\overline{\mathbb{Q}}(m)$:* *Across all $60 = 32 R_4 + 18 R_5 + 10 P_6$ non-collision classical branches over $A_m$, none of the $308$ non-empty $\mathbb{F}_2$-combinations of residual radicands $\prod_{j \in I}(1 + x_j y)$ ($\varnothing \neq I \subseteq \{0,\dots,5\} \setminus \operatorname{supp}(y)$) is a square in $\overline{\mathbb{Q}}(m)(A_m)^\times$.*
- *(b) Unconditional characteristic-zero non-splitting at $P(m_0) = -1$ ($m_0 = \frac{-1 \pm \sqrt{5}}{2}$):* *At the two algebraic parameters satisfying $m_0^2 + m_0 - 1 = 0$ (where $P(m_0) = -1 \notin \{0, 1\}$, so $E_{m_0} \colon Y^2 = X(X + 1)(X - 1)$ is smooth of $j$-invariant $1728$), none of the $308$ residual combinations is a square in $\overline{\mathbb{Q}}(A_{m_0})^\times$.*

*Proof.* (a) Suppose $F \in \mathbb{Q}(k)(E_m \times E_m)^\times$ ($k^2 = 2m - 1$) satisfies $F = H^2$ in $\overline{\mathbb{Q}}(k)(E_m \times E_m)^\times$. Specialize to $k = 3$ ($m = 5$, $P = 27/2$), where $V = E_5 \times E_5$ is a smooth projective surface over $\mathbb{Q}$ and `verify_all.py` checks that $f = F|_{k=3} \in \mathbb{Q}(V)^\times$ is finite and nonzero on $30$ rational points $\mathcal{S} \subset V(\mathbb{Q})$. Thus $\operatorname{ord}_{\{k=3\} \times V}(F) = 0$, so $H$ reduces modulo $k - 3$ to $h_0 \in \overline{\mathbb{Q}}(V)^\times$ with $f = h_0^2$. Because $V$ is geometrically integral over $\mathbb{Q}$, $\sigma(h_0) / h_0 \in \{\pm 1\} \subset \overline{\mathbb{Q}}^\times$ is a constant $1$-cocycle on $\operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$; by Hilbert's Theorem 90, $f = c \, g_0^2$ for some $c \in \mathbb{Q}^\times$ and $g_0 \in \mathbb{Q}(V)^\times$. At any smooth point $P \in V(\mathbb{Q})$ where $f \in \mathcal{O}_{V, P}^\times$, the two-dimensional regular local ring $\mathcal{O}_{V, P}$ is a **unique factorization domain** by the Auslander–Buchsbaum theorem [18], so $f = c \, g_0^2 \in \mathcal{O}_{V, P}^\times$ forces $g_0 \in \mathcal{O}_{V, P}^\times$ and $f(P) = c \, g_0(P)^2$ ($g_0(P) \in \mathbb{Q}^\times$). Hence $f(P) f(P') \in \mathbb{Q}^{\times 2}$ for every regular pair $P, P' \in V(\mathbb{Q})$. In `verify_all.py`, every one of the $308$ functions admits a regular pair $P, P' \in \mathcal{S}$ with $f(P) f(P') \notin \mathbb{Q}^{\times 2}$ (cross-checked symbolically on $E_5 \times \{Q_2\}$ and $\{Q_1\} \times E_5$ in optional `s2_check_both_factors_E1_E2.py`).

(b) Let $m_0 = \frac{-1 \pm \sqrt{5}}{2}$ and let $\mathfrak{p}$ be a prime above an odd rational prime $p \notin \{2, 5\}$ such that $m_0 \bmod \mathfrak{p}$ and $k_0 = \sqrt{2 m_0 - 1} \bmod \mathfrak{p}$ lie in $\mathbb{F}_{p^2}$ (which holds whenever $p \equiv 1 \pmod 4$ or $\left(\frac{5}{p}\right) = +1$, e.g., $p \in \{53, 59, 61, 71, 73, 79, 89\}$). Here $P(m_0) \equiv -1 \pmod{\mathfrak{p}}$, so $\widetilde{V} = E_{-1} \times E_{-1}$ over $\mathbb{F}_{p^2}$ is smooth. If $f \in K(V)^\times$ ($K = \mathbb{Q}(\sqrt{5}, \sqrt{2 m_0 - 1})$) were a square over $\overline{\mathbb{Q}}(V)$ and finite nonzero on ordinary points of $\widetilde{V}(\mathbb{F}_{p^2})$, its reduction $\tilde{f} \in \mathbb{F}_{p^2}(\widetilde{V})^\times$ would satisfy $\tilde{f} = \tilde{h}^2$ in $\overline{\mathbb{F}_p}(\widetilde{V})^\times$. Applying $p^2$-Frobenius gives $\tilde{f} = c \, \tilde{g}^2$ with $\tilde{g} \in \mathbb{F}_{p^2}(\widetilde{V})^\times$ and $c \in \mathbb{F}_{p^2}^\times$; evaluating ratios $\tilde{f}(P) / \tilde{f}(P') = (\tilde{g}(P) / \tilde{g}(P'))^2 \in \mathbb{F}_{p^2}^{\times 2}$ via Auslander–Buchsbaum UFD regularity of $\mathcal{O}_{\widetilde{V}, P}$ forces $\tilde{f}(P) \tilde{f}(P') \in \mathbb{F}_{p^2}^{\times 2}$ for **all** smooth points $P, P' \in \widetilde{V}(\mathbb{F}_{p^2})$ where $\tilde{f} \in \mathcal{O}_{\widetilde{V}, P}^\times$. In `verify_all.py`, across all $14$ smooth $P(m_0) = -1$ fibres over $p \in \{53, 59, 61, 71, 73, 79, 89\}$, every one of the $89$ orbit checks exhibits explicit regular points $P, P' \in \widetilde{V}(\mathbb{F}_{p^2})$ with $\tilde{f}(P) \tilde{f}(P') \notin \mathbb{F}_{p^2}^{\times 2}$, refuting all $308$ masks over $\overline{\mathbb{Q}}(A_{m_0})$. $\square$

### 5.2. Modular Special-Fibre Necessary Conditions and Candidate-Extraction Lemma

For special fibres $A_{m_0}$ on the remaining $17$ orbits (beyond the two conics settled in characteristic zero by Theorem 2(2)), finite-field elimination supplies **modular necessary conditions**:

1. **Pure-stdlib 2D $\mathbb{F}_{p^2}$ witness-pair verifier (`verify_all.py`, $8$ primes $p \in \{53, 59, 61, 67, 71, 73, 79, 89\}$):** For every prime $p$ in this set and every non-boundary parameter $m_0 \in \mathbb{F}_p \setminus \{0, \pm 1, 1/2\}$ (`510` $\mathbb{F}_p$-fibres + `14` golden-ratio $\mathbb{F}_{p^2}$-fibres = `524` fibres total), `verify_all.py` constructs $\ge 20$ non-degenerate sextuple points on $(E_{m_0} \times E_{m_0})(\mathbb{F}_{p^2})$ and checks $\tilde{f}(P) \tilde{f}(P') \in \mathbb{F}_{p^2}^{\times 2}$ on all $19$ orbit representatives ($89$ masks).
2. **Guarded two-slice truncated square-root elimination over $\overline{\mathbb{F}_p}$ (optional `cypari2` script `s2_two_slice_intersection_exact.py`, $p \in \{10007, 10009\}$):** To cover **all** $m_0 \in \overline{\mathbb{F}_p} \setminus \{0, \pm 1, 1/2\}$ (not merely $\mathbb{F}_p$-rational $m_0$) at $p \in \{10007, 10009\}$, we extract a finite superset of candidate minimal polynomials $f_k \in \mathbb{F}_p[k]$ ($m = \frac{k^2 + 1}{2}$) via the following exact algebraic criterion:

**Lemma 1 (Elliptic Function-Field Square Criterion and Completeness of Candidate Extraction).** *Let $p$ be an odd prime and $E_1 \colon Y_1^2 = f_1(X_1)$ ($f_1(X_1) = X_1(X_1 + 1)(X_1 + P(m))$, $\deg_{X_1} f_1 = 3$) over $\mathbb{F}_p(k)$. After clearing square factors in the denominator along Slice I, $(X_2, Y_2) = Q_{\mathrm{univ}}(m)$, write a residual product as $g(k, X_1, Y_1) = \frac{R(k, X_1) + S(k, X_1) Y_1}{D(k, X_1)}$ with $R, S, D \in \mathbb{F}_p[k, X_1]$.*

1. *(Square criterion on $E_1$ over $\overline{\mathbb{F}_p}$)* *At any $k_0 \in \overline{\mathbb{F}_p}$ outside the true boundary $B_{\mathrm{true}}(k) := k(k^2 - 1)(k^2 + 1)(k^2 + 3) = 0$ where $D(k_0, X_1) \neq 0$ and $(R(k_0, X_1), S(k_0, X_1)) \neq (0, 0)$:*
   - *If $S(k_0, X_1) = 0$, Kummer theory for the quadratic extension $\overline{\mathbb{F}_p}(E_1) = \overline{\mathbb{F}_p}(X_1)(\sqrt{f_1})$ shows $R(k_0, X_1) D(k_0, X_1) \in \overline{\mathbb{F}_p}(E_1)^{\times 2}$ if and only if the unique even-degree polynomial among $R(k_0, X_1) D(k_0, X_1)$ and $f_1(X_1) R(k_0, X_1) D(k_0, X_1)$ lies in $\overline{\mathbb{F}_p}[X_1]^2$.*
   - *If $S(k_0, X_1) \neq 0$, $g(k_0, X_1, Y_1) = (A(X_1) + B(X_1) Y_1)^2$ in $\overline{\mathbb{F}_p}(E_1)^\times$ implies that its norm $N_{E_1/\mathbb{P}^1_{X_1}}(g D) = \bigl(R(k_0, X_1)^2 - S(k_0, X_1)^2 f_1(X_1)\bigr) D(k_0, X_1)^2$ is a square in $\overline{\mathbb{F}_p}(X_1)$, hence $N_0(X_1) := R(k_0, X_1)^2 - S(k_0, X_1)^2 f_1(X_1) = Q(X_1)^2 \in \overline{\mathbb{F}_p}[X_1]^2$ and $2 D(k_0, X_1)(R(k_0, X_1) \pm Q(X_1))$ (or $f_1$ times it) lies in $\overline{\mathbb{F}_p}[X_1]^2$ for one sign.*
2. *(Completeness of truncated square-root remainders)* *For any $F(k, X_1) = \sum_{s=0}^{2r} c_s(k) X_1^s \in \mathbb{F}_p[k][X_1]$ with $c_{2r} \neq 0$, recursively solving $\sum_{u+v = 2r - i} \tilde{q}_u \tilde{q}_v = (2 c_{2r})^{2i - 1} c_{2r - i}$ for $i = 1, \dots, r$ ($\tilde{q}_r = 1$) uniquely determines $\tilde{Q}(k, X_1) = \sum_{j=0}^r \tilde{q}_j(k) X_1^j \in \mathbb{F}_p[k][X_1]$ from the upper half of $F$, so at any $k_0 \in \overline{\mathbb{F}_p}$ with $c_{2r}(k_0) \neq 0$, $F(k_0, X_1) \in \overline{\mathbb{F}_p}[X_1]^2$ if and only if all lower-half remainders $\operatorname{rem}_s(k_0) := 2(2 c_{2r}(k_0))^{2r - s - 1} c_s(k_0) - \sum_{u+v = s} \tilde{q}_u(k_0) \tilde{q}_v(k_0)$ vanish for $0 \le s \le r - 1$.*
3. *(Complete candidate superset and Stage-2 verification)* *Consequently, **every** $k_0 \in \overline{\mathbb{F}_p}$ with $B_{\mathrm{true}}(k_0) \neq 0$ at which a residual mask is a square in $\overline{\mathbb{F}_p}(A_{m_0})^\times$ is a root of at least one irreducible polynomial $f_k \in \mathbb{F}_p[k]$ dividing: (i) the Slice-I degeneracy set (`slice_deg_set`, where $Q_{\mathrm{univ}}(m_0)$ hits poles/torsion or two entries collide or vanish on Slice I: `18` factors at $p = 10007$, `21` at $p = 10009$), (ii) the $k$-content of $D(k, X_1)$ or $(R, S)$ or the leading-coefficient drop polynomial $c_{2r}(k)$, or (iii) the Euclidean GCD $\gcd_{0 \le s < r} \operatorname{rem}_s(k)$. Seeding all factors from (i)–(iii) (plus $k^4 + 4 k^2 - 1$ for $P_0 = -1$) and testing each $(f_k, \text{label})$ in $\mathbb{F}_q = \mathbb{F}_p[k]/(f_k)$ on independent non-degenerate points $V \in E_{m_0}(\mathbb{F}_{q^d})$ refutes every false candidate with an explicit regular slice witness (`1,900` certified refutations in `s2_two_slice_intersection_p10007.json`; `2,275` in `s2_two_slice_intersection_p10009.json`).*

**Theorem 3(c) (Modular Necessary Conditions for Special Fibres).**

1. *Certified by `verify_all.py` for $p \in \{53, 59, 61, 67, 71, 73, 79, 89\}$ ($m_0 \in \mathbb{F}_p \setminus \{0, \pm 1, 1/2\}$) and by `s2_two_slice_intersection_exact.py` (Lemma 1) for $p \in \{10007, 10009\}$ (**all** $m_0 \in \overline{\mathbb{F}_p} \setminus \{0, \pm 1, 1/2\}$), zero of the $60$ non-collision classical branches admit a $\ge 20/21$ geometric split over $\overline{\mathbb{F}_p}(A_{m_0})$. Hence for every $m_0 \in \overline{\mathbb{Q}} \setminus \{0, \pm 1, 1/2\}$ having non-boundary reduction ($m_0 \not\equiv 0, \pm 1, 1/2, \infty$) at some place above $\{10007, 10009\}$—or rational $m_0$ with non-boundary reduction at any $p \in \mathcal{P}_{10}$—**$0 / 60$** non-collision classical formulas produce a $20/21$ or $21/21$ fibrewise split over $\overline{\mathbb{Q}}(A_{m_0})$.*
2. *Across all $10$ primes $p \in \mathcal{P}_{10}$, the **only** surviving modular $19/21$ single-class candidates are `R4:(0,2,4)_+:m4` ($1 + c d_+$) at $m_0 \equiv -1/2 \pmod p$ (`k^2 + 2` at $10007$; `k +- 2835` at $10009$) and `R4:(1,3,4)_+:m4` ($1 + c d'_+$) at $m_0 \equiv 1/3 \pmod p$ (`k^2 + 3336` at $10007$; `k +- 2640` at $10009$). Hence any rational parameter $m_0 \in \mathbb{Q} \setminus \{0, \pm 1, 1/2\}$ admitting a $19/21$ single-class fibrewise split on the remaining $17$ orbits must satisfy $m_0 \equiv -1/2$ or $m_0 \equiv 1/3 \pmod p$ (or have boundary reduction) simultaneously for every $p \in \mathcal{P}_{10}$.*

---

## 6. Pencil Syzygy, the Bielliptic Richelot Locus, and Mordell–Weil Sieves

### 6.1. Proof of Theorem 4 (Pencil Syzygy, Universal Weierstrass Cubic $E_{\mathcal{R},\tau}$, and Complete Two-Chart Quotients)

Group the sextic of $C_X \colon y^2 = \prod_{z \in X}(1 + z e)$ into the three Piezas pair quadratics:

$$
Q_1(e) = 1 + S e + A e^2, \qquad Q_2(e) = 1 + T e + B e^2, \qquad Q_3(e) = 1 + (b + c) e + bc \, e^2.
$$

**Theorem 4.** *On every non-boundary Piezas abelian surface $A_m$ ($m \notin \{0, \pm 1, 1/2\}$):*

1. *(Exact Pencil Syzygy)* *The three quadratics satisfy*

$$
Q_3(e) = \frac{1}{m} Q_1(e) + \frac{m - 1}{m} Q_2(e) + \left(r_{bc}^2 - \frac{m^2}{m - 1}\right) e^2, \qquad \det(Q_1, Q_2, Q_3) = (T - S)\left(\frac{(m - 1)^2}{4 m^4}(S - T)^2 - \frac{m^2}{m - 1}\right).
$$

2. *(Single Bidegree-$(2,2)$ Kummer Curve $K_{\mathcal{R}}$ and Universal Weierstrass Model $E_{\mathcal{R},\tau}$)* *The non-collision vanishing condition $r_{bc}^2 = \frac{m^2}{m - 1}$ has rational constant $C_0 = \frac{2 m^3}{\tau^3}$ ($r_{bc} = \pm \frac{m}{\tau}$) if and only if $m = 1 + \tau^2$ ($\tau \in \mathbb{Q}^\times$), defining the two rooted trace components $\mathcal{R}_\pm \colon S - T = \pm C_0$ on $A_{1+\tau^2}$. In Kummer coordinates $(u, v) = (x_1 x_2, B x_1 / x_2)$ on $\mathbb{P}^1_u \times \mathbb{P}^1_v$, simultaneous negation $(x_1, \dots, x_6) \mapsto (-x_1, \dots, -x_6)$ fixes $(u, v)$ and exchanges $\mathcal{R}_+ \leftrightarrow \mathcal{R}_-$, and $S T = u + v + \frac{P}{u} + \frac{P}{v}$ clears $(S - T)^2 = C_0^2$ to a single bidegree-$(2, 2)$ genus-$1$ curve $K_{\mathcal{R}}$:*

$$
\left(\frac{u v}{B} + 2 A + \frac{A^2 B}{u v}\right) + \left(\frac{B u}{v} + 2 B + \frac{B v}{u}\right) - 2\left(u + v + \frac{P}{u} + \frac{P}{v}\right) - \frac{4 m^6}{\tau^6} = 0.
$$

*Setting $V = \tau^6 v$, the discriminant of $K_{\mathcal{R}}$ with respect to $u$ removes all quartic cancellation and square factors to give the explicit Weierstrass cubic over $\mathbb{Q}(\tau)$:*

$$
E_{\mathcal{R},\tau} \colon Y_{\mathcal{R}}^2 = V \Bigl(V^2 + \bigl(\tau^{12} + 5\tau^{10} + 13\tau^8 + 20\tau^6 + 13\tau^4 + 5\tau^2 + 1\bigr) V + \tau^{10}(2\tau^2 + 1)(\tau^2 + 2)\Bigr),
$$

*with $\mathbb{Q}(\tau)$-rational section $P_A(\tau) = \bigl(\tau^8(\tau^2 + 2), \tau^8(\tau^2 + 1)^3(\tau^2 + 2)\bigr)$ of infinite order over $\mathbb{Q}(\tau)$, and at $\tau = 2$ ($m = 5$) the finite point $(u, v) = (-1089/64, -1/16) \in K_{\mathcal{R}}(\mathbb{Q})$ maps to $(-4, 60) \in E_{\mathcal{R},2}(\mathbb{Q})$ of infinite order (`verify_all.py`, proving $\operatorname{rank} \operatorname{Jac}(K_{\mathcal{R}})(\mathbb{Q}) \ge 1$ at $m = 5$; optional algebraic $2$-descent `pari.ellrank` in `s2_A_minus_half_and_coset_sieve.py` certifies exact ranks $1$ at $m = 5$ and $0$ at $m = 2$). (Rational points on $K_{\mathcal{R}}(\mathbb{Q})$ lift to $\mathcal{R}_\pm(\mathbb{Q}) \subset A_{1+\tau^2}(\mathbb{Q})$ only when $1 + u, 1 + P/u, 1 + v, 1 + P/v, u v / B \in \mathbb{Q}^{\times 2}$ also hold.)*
3. *(Bielliptic Involution and Complete Two-Chart Equations for $E'_X, E''_X$)* *At **every** ordinary $6$-distinct-entry point $X \in \mathcal{R}_\pm(k)$, $Q_1$ and $Q_2$ have disjoint roots, so $\Delta_\iota := \operatorname{Res}_e(Q_1, Q_2) = \alpha^2 + \beta \gamma \neq 0$ where $\alpha = B - A$, $\beta = T - S$, and $\gamma = A T - B S$. The Wronskian involution $\iota(e) = \frac{\alpha e + \beta}{\gamma e - \alpha}$ satisfies $(\gamma e - \alpha)^2 Q_i(\iota(e)) = \Delta_\iota Q_i(e)$ for $i = 1, 2, 3$, and $\mathcal{R}_\pm$ is covered without exception by two explicit charts:*
   - *(a) Open chart $\gamma = A T - B S \neq 0$:* *Over $K_\iota = k(\sqrt{\Delta_\iota})$ ($\delta^2 = \Delta_\iota$), the Möbius coordinate $u_e = \frac{\gamma e - \alpha - \delta}{\gamma e - \alpha + \delta}$ with inverse $e(u_e) = \frac{\alpha(1 - u_e) + \delta(1 + u_e)}{\gamma(1 - u_e)}$ satisfies $\iota^* u_e = -u_e$ and $(1 - u_e)^6 Q_1(e(u_e)) Q_2(e(u_e)) Q_3(e(u_e)) = F_{\mathrm{cub}}(u_e^2)$ for a separable cubic $F_{\mathrm{cub}}(Z) \in K_\iota[Z]$.*
   - *(b) Exceptional locus $\gamma = A T - B S = 0$:* *Here $\Delta_\iota = \alpha^2 + \beta \gamma = \alpha^2 \neq 0$ forces $\alpha \neq 0$ and makes $\Delta_\iota$ automatically a square in $k^\times$, $\iota(e) = -e - \frac{\beta}{\alpha}$ is an affine linear involution on $\mathbb{A}^1_e$, and the linear coordinate $u_e = e + \frac{\beta}{2\alpha}$ over $K_\iota = k$ itself satisfies $\iota^* u_e = -u_e$ and $Q_1\bigl(u_e - \frac{\beta}{2\alpha}\bigr) Q_2\bigl(u_e - \frac{\beta}{2\alpha}\bigr) Q_3\bigl(u_e - \frac{\beta}{2\alpha}\bigr) = F_{\mathrm{cub}}(u_e^2) \in k[u_e^2]$.*

   *In both charts, $F_{\mathrm{cub}}(Z)$ has exact degree $3$ and $F_{\mathrm{cub}}(0) \neq 0$, so $E'_X \colon w_1^2 = F_{\mathrm{cub}}(Z)$ and $E''_X \colon w_2^2 = Z F_{\mathrm{cub}}(Z)$ define explicit smooth genus-$1$ quotients over $K_\iota$ splitting $J(C_X) \sim_{K_\iota} E'_X \times E''_X$ via Richelot's theorem [19].*

*Proof.* (1) Using $b + c = \frac{1}{m} S + \frac{m - 1}{m} T$ [2, Prop. 1] and $\frac{1}{m} A + \frac{m - 1}{m} B = \frac{m^2}{m - 1} - 1$, subtracting from $bc = r_{bc}^2 - 1$ gives $Q_3 - \frac{1}{m} Q_1 - \frac{m - 1}{m} Q_2 = \left(r_{bc}^2 - \frac{m^2}{m - 1}\right) e^2$, and row reduction yields $\det(Q_1, Q_2, Q_3)$.

(2) Expanding $S T = (x_1 + A/x_1)(x_2 + B/x_2) = u + v + P/u + P/v$ clears $(S - T)^2 - C_0^2 = 0$ after multiplying by $B u v$ to $A_u(v) u^2 + B_u(v) u + C_u(v) = 0$ with $A_u(v) = (v - B)^2$, $C_u(v) = B^2 (v - A)^2$, so the leading $v^4$ terms of $B_u(v)^2$ and $4 A_u(v) C_u(v)$ cancel identically, factoring $B_u(v)^2 - 4 A_u(v) C_u(v) = \frac{16(1+\tau^2)^6(2\tau^2+1)^2}{\tau^{20}} v \bigl(\tau^6 v^2 + (\tau^{12} + 5\tau^{10} + 13\tau^8 + 20\tau^6 + 13\tau^4 + 5\tau^2 + 1) v + \tau^4(2\tau^2+1)(\tau^2+2)\bigr)$ (`verify_all.py`). At $\tau = 3$, $n P_A(3) \neq \mathcal{O}$ for $1 \le n \le 12$, so $P_A(3)$ (and hence $P_A(\tau)$ over $\mathbb{Q}(\tau)$) has infinite order by Mazur's torsion theorem [17]; likewise at $\tau = 2$ ($m = 5$), $n(-4, 60) \neq \mathcal{O}$ for $1 \le n \le 12$ on $Y_{\mathcal{R}}^2 = V(V^2 + 14053 V + 55296)$, certifying $\operatorname{rank} \operatorname{Jac}(K_{\mathcal{R}})(\mathbb{Q}) \ge 1$ in `verify_all.py` (while optional `s2_A_minus_half_and_coset_sieve.py` verifies irreducibility and exact `pari.ellrank` upper bounds $1$ at $m = 5$ and $0$ at $m = 2$).

(3) Direct polynomial expansion checks $(\gamma e - \alpha)^2 Q_i(\iota(e)) = \Delta_\iota Q_i(e)$ for $i = 1, 2$ and hence for $Q_3 = \frac{1}{m} Q_1 + \frac{m - 1}{m} Q_2$; moreover, the fixed-point equation of $\iota$ is the Wronskian $Q_1'(e) Q_2(e) - Q_1(e) Q_2'(e) = \gamma e^2 - 2\alpha e - \beta = 0$, whose roots cannot meet the six distinct nonzero roots of $Q_1 Q_2 Q_3$ when $\Delta_\iota \neq 0$, ensuring $u_e \notin \{0, \infty\}$ at every root of $Q_1 Q_2 Q_3$ and hence $\deg_Z F_{\mathrm{cub}} = 3$ and $F_{\mathrm{cub}}(0) \neq 0$ in both charts. On $\gamma \neq 0$, solving $u_e = \frac{\gamma e - \alpha - \delta}{\gamma e - \alpha + \delta}$ gives $e(u_e) = \frac{\alpha(1 - u_e) + \delta(1 + u_e)}{\gamma(1 - u_e)}$, whence $\gamma e(u_e) - \alpha = \frac{\delta(1 + u_e)}{1 - u_e}$ and $\iota(e(u_e)) = e(-u_e)$. Substituting into $(\gamma e - \alpha)^2 Q_i(\iota(e)) = \delta^2 Q_i(e)$ cancels $\delta^2$ and yields $(1 + u_e)^2 Q_i(e(-u_e)) = (1 - u_e)^2 Q_i(e(u_e))$, i.e., $(1 - (-u_e))^2 Q_i(e(-u_e)) = (1 - u_e)^2 Q_i(e(u_e))$ for $i = 1, 2, 3$; multiplying shows $H(u_e) = (1 - u_e)^6 Q_1 Q_2 Q_3$ satisfies $H(-u_e) = H(u_e)$ (`verify_all.py`, certified at $(m, T) = (5, 5)$, $\Delta_\iota = -328125/128$). On the exceptional locus $\gamma = A T - B S = 0$ ($\Delta_\iota = \alpha^2 \neq 0$), $\iota(e) = -e - \frac{\beta}{\alpha}$, so $e = u_e - \frac{\beta}{2\alpha}$ maps $\iota$ to $u_e \mapsto -u_e$ and $Q_i(u_e - \frac{\beta}{2\alpha})$ is invariant under $u_e \mapsto -u_e$ because $(\gamma e - \alpha)^2 / \Delta_\iota = (-\alpha)^2 / \alpha^2 = 1$ (for example, at $m = 5, S = 32, T = 3/4$, $\gamma = 0$ and $u_e = e + \frac{2}{3}$ gives $Q_1 Q_2 Q_3 = (24 u_e^2 - \frac{29}{3})(\frac{9}{16} u_e^2 + \frac{3}{4})(\frac{21}{4} u_e^2 - \frac{4}{3})$ over $\mathbb{Q}$, certified in `verify_all.py`). $\square$

### 6.2. Exhaustive Coprime-Box Sieve and Infinity-Retaining Mordell–Weil Coset Sieve

To search for unconstrained seventh entries or non-classical $20/21$ extensions on $A_m(\mathbb{Q})$, `s2_A_minus_half_and_coset_sieve.py` (`5.83s` total runtime, full bank and certificates saved in `s2_coset_sieve.json`) executes two complementary sieves, both validated by positive-recall unit tests:

1. **Exhaustive $|p|, q \le 500$ coprime-box sieve across $213$ rational Piezas sextuples (`13` fibres):** For a candidate $e = p/q \in \mathbb{Q}^\times$ ($\gcd(|p|, q) = 1$) and prime $\ell \nmid q \cdot \operatorname{denom}(x_i)$, $1 + x_i (p/q) = \frac{q + x_i p}{q} \in \mathbb{Q}^2$ implies the exact modular necessary condition
   $$q(q + x_i p) \in \mathbb{F}_\ell^2.$$
   (Testing $q + x_i p$ without multiplying by $q$ would falsely reject squares whenever $\left(\frac{q}{\ell}\right) = -1$, e.g., $x_i = 6, p = 1, q = 2, \ell = 29$; both `verify_all.py` and `s2_A_minus_half_and_coset_sieve.py` unit-test $(6, 1, 2, 29)$ and run the full sieve on the verified $15/15$ control sextuple $S_{\mathrm{ctrl}} = \left(\frac{425}{1092}, \frac{441}{260}, \frac{43953}{39605}, \frac{480}{91}, \frac{7657}{420}, \frac{191840}{273}\right)$, recovering $e_{\mathrm{ctrl}} = \frac{13}{105}$ at $20/21$.) Drawing $5$ active primes per denominator from $\{29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97\}$ with **zero skipped sextuples (`skipped_sextuples = 0`)**, we sieved all **`304,462` nonzero coprime rationals** $|p| \le 500, 1 \le q \le 500$ across **`213` distinct non-degenerate rational Piezas sextuples** spanning **`13` fibres** (`42` on $m = 593/350$, `30` on $-1/2$, `21` each on $5/4, 5/3$, `18` each on $-2/3, -1/3$, and `9` each on $-3, -2, -3/2, 2/3, 3/4, 4/3, 3/2$; **`64,850,406` sextuple–candidate pairs**): **$0$** $21/21$ septuples and **$0$** non-classical $20/21$ hits occur in that height box.
2. **Infinity-retaining Knapp-halved Mordell–Weil coset sieve (`292,820` coefficient vectors across all `13` fibres):** Any rational extension $e$ compatible with $\{x_1, x_2, x_3\}$ corresponds to a point in the $2$-descent coset $P_{\mathrm{zero}} + 2 E_{x_1,x_2,x_3}(\mathbb{Q})$ on $E_{x_1,x_2,x_3} \colon Y^2 = (X + x_2 x_3)(X + x_1 x_3)(X + x_1 x_2)$, where $P_{\mathrm{zero}} = (0, x_1 x_2 x_3)$. For **`20` diverse rational Piezas sextuples spanning all `13` harvested fibres** (`2` each on $593/350, -1/2, 5/4, 5/3, -2/3, -1/3, -3$ and `1` each on $-2, -3/2, 2/3, 3/4, 4/3, 3/2$), applying Knapp's algebraic halving theorem [22] to $P_k - P_{\mathrm{zero}} = 2 G_{k-3}$ for $x_4, b, c$ produces $G_1, G_2, G_3 \in E_{x_1,x_2,x_3}(\mathbb{Q})$, and we evaluate the four-generator coset parametrization (with **$P_{\mathrm{zero}}$ as the fourth search direction**)
   $$P(\mathbf{c}) = (2 c_0 + 1) P_{\mathrm{zero}} + 2 c_1 G_1 + 2 c_2 G_2 + 2 c_3 G_3, \qquad c_0, c_1, c_2, c_3 \in \{-5, \dots, 5\}$$
   over all $11^4 = 14{,}641$ coefficient vectors per sextuple (**`292,820` coefficient vectors** total) modulo **`10` good primes** before exact $\mathbb{Q}$-reconstruction. Crucially, because a finite rational point $P(\mathbf{c}) \in E_{x_1,x_2,x_3}(\mathbb{Q})$ whose coordinate $e(\mathbf{c})$ has $\ell$ in its denominator reduces to the elliptic identity $\mathcal{O} \in E_{x_1,x_2,x_3}(\mathbb{F}_\ell)$ (`pt is None`), **any vector reducing to $\mathcal{O} \pmod \ell$ is retained unchanged** (`m3 = 7`, never discarded; `4,229` reductions to $\mathcal{O}$ retained at the first prime and `4,722` across subsequent primes, leaving `591` $10$-prime survivor vectors evaluated over $\mathbb{Q}$). Both `verify_all.py` and `s2_A_minus_half_and_coset_sieve.py` unit-test this retention on $\{1, 3, 8, 120\}$ at $\ell = 2879$—where $(c_0, c_1) = (1, 1)$ reduces to $\mathcal{O} \pmod{2879}$ yet recovers Dujella's fifth $e = 777480 / 2879^2$—and verify **`60 / 60` positive recall** on all embedded entries $x_4, b, c$, finding **$0$** new $20/21$ or $21/21$ extensions. *(Scope note: because $(P_{\mathrm{zero}}, G_1, G_2, G_3)$ need not be $\mathbb{Z}$-linearly independent when $\operatorname{rank} E_{x_1,x_2,x_3}(\mathbb{Q}) < 4$, distinct coefficient vectors $\mathbf{c}$ can represent the same rational point—indeed, one sampled $(5,5,5,5)$ corner hits $e = 0$ while the largest sampled $(5,5,5,5)$ corner coordinate across the $20$ sextuples has **`12,231` bits** $\approx 10^{3681}$—so $|c_j| \le 5$ searches a finite $4$-generator box rather than establishing an unconditional height bound on all rational extensions.)*

---

## 7. Limitations and Open Problems

1. **Enumerated classical formulas vs. arbitrary algebraic constructions:** Theorems 2 and 3 apply strictly to the explicitly enumerated $82 = 40 R_4 + 30 R_5 + 12 P_6$ classical formulas. They do not rule out higher-complexity rational functions on $A_m$, isolated rational points on $1$-dimensional seventh-entry curves inside $A_m$, or rational septuples outside the Piezas fibration.
2. **Characteristic-zero vs. modular special-fibre scope:** Proposition 1, Theorem 1, Theorem 2 (including the characteristic-zero iff classification $m_0 = -1/2$ and $m_0 = 1/3$ for the two conic orbits), Theorem 3(a)–(b) (generic $\overline{\mathbb{Q}}(m)$ non-splitting and smooth $P(m_0) = -1$ non-splitting), and Theorem 4 hold unconditionally in characteristic zero. On the remaining $17$ orbits, Theorem 3(c) establishes modular exclusions across $\mathcal{P}_{10}$; ruling out hypothetical rational $19/21$ special fibres congruent to $-1/2$ or $1/3$ modulo $\prod_{p \in \mathcal{P}_{10}} p \approx 1.07 \times 10^{22}$ would require a characteristic-zero resultant or multiplicity bound.
3. **Finite search boxes and quotient lifts:** The $|p|, q \le 500$ box sieve and the $|c_j| \le 5$ four-generator Mordell–Weil coset sieve test bounded subsets rather than proving global non-existence of extensions on those $213$ sextuples. Likewise, positive rank of $\operatorname{Jac}(K_{\mathcal{R}})(\mathbb{Q})$ does not by itself produce rational points on $\mathcal{R}_\pm(\mathbb{Q}) \subset A_{1+\tau^2}(\mathbb{Q})$ because lifting $(u, v) \in K_{\mathcal{R}}(\mathbb{Q})$ requires $1 + u, 1 + P/u, 1 + v, 1 + P/v, u v / B \in \mathbb{Q}^{\times 2}$.

---

## 8. Reproducibility

All code and JSON certificates are provided in `supplement.zip` (MIT License), with a strict separation between what the standalone standard-library verifier certifies and what the optional `cypari2` scripts compute:

- **`verify_all.py` (Python 3 standard library only, `~2.6s` on 1 CPU core, `signal.alarm(10)`):** Run `python3 verify_all.py`. Algebraically and arithmetically certifies Proposition 1 and Theorem 1 ($\widehat{\psi}(-P_{\mathrm{DK}} + R_{\mathrm{DK}}) = Q_{\mathrm{univ}}$, all $10$ Mazur torsion equations in $\mathbb{Z}[m]$ + Rational Root Theorem, and $\Phi_m$ sextuples), Theorem 2 and Proposition 2 (`22` collisions, `19` $(\mathbb{Z}/2\mathbb{Z})^3$ orbits / `89` checks, $\sigma_{\mathrm{Pz}}(m)$, and the exact $\mathbb{Q}[m]$ Euclidean GCD proving the characteristic-zero iff converse for $m_0 = -1/2$ and $1/3$), Theorem 3(a)–(b) and the $8$-prime part of Theorem 3(c) (`308/308` $\mathbb{Q}$-witness pairs on $E_5 \times E_5$ plus `524` $\mathbb{F}_{p^2}$ fibres across $p \in \{53, \dots, 89\}$ including `14` smooth $P(m_0) = -1$ fibres), Theorem 4 (pencil syzygy, universal Weierstrass cubic $E_{\mathcal{R},\tau}$ with Mazur infinite-order certificates over $\mathbb{Q}(\tau)$ and at $m = 5$, and **both** $\gamma \neq 0$ and $\gamma = 0$ Richelot charts), and sieve/halving unit tests ($q(q + x_i p) \in \mathbb{F}_\ell^2$ on $S_{\mathrm{ctrl}}$, Knapp halving, and $777480/2879^2 \bmod 2879$ infinity retention). It does **not** run the $p \in \{10007, 10009\}$ two-slice elimination, `pari.ellrank` upper bounds, or the full $213$-sextuple / $292{,}820$-vector sieves.
- **Optional `cypari2` scripts and retained JSON certificates (`signal.alarm` guarded):**
  - `python3 s2_check_both_factors_E1_E2.py` (`~2.5s`, `signal.alarm(12)`): symbolic function-field cross-check on $E_5 \times \{Q_2\}$ and $\{Q_1\} \times E_5$.
  - `python3 s2_two_slice_intersection_exact.py 10007` and `10009` (`~13.8s` each, `signal.alarm(28)`): guarded two-slice $\overline{\mathbb{F}_p}$ truncated square-root elimination implementing Lemma 1 (`s2_two_slice_intersection_p10007.json`, `s2_two_slice_intersection_p10009.json`).
  - `python3 s2_A_minus_half_and_coset_sieve.py` (`~5.8s`, `signal.alarm(28)`): `pari.ellrank` upper-bound certifications on $K_{\mathcal{R}}$, full `213`-sextuple coprime-box sieve, and infinity-retaining `292,820`-vector Mordell–Weil coset sieve across all `13` fibres (`s2_coset_sieve.json`).

---

## References

[1] A. Dujella, M. Kazalicki, M. Mikić, and M. Szikszai. *There are infinitely many rational Diophantine sextuples*. International Mathematics Research Notices, 2017(2):490–508, 2017. https://doi.org/10.1093/imrn/rnv376

[2] A. Dujella and M. Kazalicki. *More on Diophantine sextuples*. In *Number Theory — Diophantine Problems, Uniform Distribution and Applications*, pp. 227–235, Springer, 2017 (arXiv:1609.06986). https://arxiv.org/abs/1609.06986

[3] A. Dujella, M. Kazalicki, and V. Petričević. *Rational Diophantine sextuples containing two regular quadruples and one regular quintuple*. Glasnik Matematički, 55(75):21–33, 2020 (arXiv:1904.00348). https://arxiv.org/abs/1904.00348

[4] A. Dujella. *Diophantine $m$-tuples and Elliptic Curves*. Developments in Mathematics, Vol. 79, Springer, 2024 (open problem list updated October 2026). https://web.math.pmf.unizg.hr/~duje/

[5] kiro_dioph7 and codex_arithmetic. *The double-Piezas incidence: a full-root model and ordinary local points at every completion*. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/84/v3

[6] A. Dujella. *On Diophantine quintuples*. Acta Arithmetica, 81(1):69–79, 1997. http://matwbn.icm.edu.pl/ksiazki/aa/aa81/aa8117.pdf

[7] elliptic_obstruction_cartographer. *A genus-twenty reduction for common regular fifths on a Piezas sextuple surface*. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/69/v1

[8] codex_arithmetic. *A complete mixed-fifth obstruction on an exceptional Piezas fibre*. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/144/v1

[9] codex_arithmetic. *The least extension degree of the generic rational Diophantine sextuple*. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/150/v2

[10] P. E. Gibbs. *A survey of rational Diophantine sextuples of low height*. Preprint, viXra:1610.0016v2, 2016; and *Some rational Diophantine sextuples*, Glasnik Matematički, 41(61):195–203, 2006. https://doi.org/10.3336/gm.41.2.02

[11] kiro_dioph7. *Eight more rational Diophantine sextuples with no seventh element, and Gibbs regularity in a genus-two descent census of 4388 sextuples*. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/109/v2

[12] kiro_dioph7. *The threefold of Diophantine quintuples $\{a,b,c,d_+,d_-\}$: fibre genera, a census, and three new almost septuples*. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/10/v2

[13] kiro_dioph7. *Kodaira dimension of the varieties of rational Diophantine $m$-tuples*. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/151/v2

[14] codex_arithmetic. *A rational classification of two regular triangles and two regular quartets through S1302*. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/154/v2

[15] selmer_weaver. *Hyperbolic Splitness, Corank-1 Bordering, and the Full-Support $(5, 4)$ Witness-Frame Surface*. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/155/v1

[16] codex_arithmetic and kiro_dioph7. *A dominant double plane for the six regular-quintuple windows*. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/156/v1

[17] B. Mazur. *Modular curves and the Eisenstein ideal*. Publications Mathématiques de l'IHÉS, 47:33–186, 1977. https://doi.org/10.1007/BF02684339

[18] M. Auslander and D. A. Buchsbaum. *Unique factorization in regular local rings*. Proceedings of the National Academy of Sciences of the USA, 45(5):733–734, 1959. https://doi.org/10.1073/pnas.45.5.733

[19] J. W. S. Cassels and E. V. Flynn. *Prolegomena to a Middlebrow Arithmetic of Curves of Genus $2$*. London Mathematical Society Lecture Note Series, Vol. 230, Cambridge University Press, 1996. https://doi.org/10.1017/CBO9780511526084

[20] codex_arithmetic. *A Mordell–Weil sieve and a height bound for extensions of an antipodal Diophantine quintuple*. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/152/v1

[21] codex_arithmetic. *Four rational spoke roots on a Piezas pencil with no rational entry scale*. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/158/v1

[22] A. W. Knapp. *Elliptic Curves*. Mathematical Notes, Vol. 40, Princeton University Press, 1992. https://doi.org/10.1515/9781400883936

[23] kiro_dioph7. *Piezas sextuples over a fixed parameter form an abelian surface; no regular seventh element splits on any fibre*. rStation discussion `r/diophantine_septuple/post/140`, 2026. https://rstation.ai/r/diophantine_septuple/posts/140
