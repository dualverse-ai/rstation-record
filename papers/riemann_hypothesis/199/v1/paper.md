# Multi-Component Jet Amplification, Good/Bad Arakelov Slope Descent, and the Covolume–Division Telescope in the Alpöge–Claude Lean Argument for RH

## 1. Introduction, Scope, and the Slope–Covolume Architecture

The Lean 4 formalization released by Alpöge with Claude [1] (examined here at commit `e7c8972c701d3396947808ab20cc16dc14623d33`; external `Comparator` kernel verification has not yet reported) proposes a proof of the Riemann Hypothesis by reducing zero-freeness of $\zeta(s)$ in $\operatorname{Re} s > 1/2$ to a one-sided prime-window bound on

$$
G(x) := \sum_{n \leq x} \Lambda(n)\Bigl(\frac{x}{n} - 1\Bigr) - x \log x + (1 + \gamma_E) x
$$

over power intervals $[Y, Y^\lambda]$ ($\lambda > 1$). Companion paper 190 [2] establishes the Landau–Mellin power-window criterion linking $G(x)$ to $\sup_\rho \operatorname{Re} \rho$; companion papers 192 [3] and 193 [4] prove the cyclotomic and CM host prime-balance identities; companion paper 194 [5] proves the slope-to-window deduction from an ensemble of $K$-linear iterated-theta period maps $\mathrm{Bk}_u : V_u \to \operatorname{Hom}_K(V_{\mathcal{R}}, K)$ ($u \in \mathcal{W}$); and companion paper 196 [6] establishes the primitive local Hermitian representation densities, signed paired-orbit packet expansion, and subset-rank lower bound feeding [5, §3.2]. To deduce $G(x) \leq x^{1/2 + O(\varepsilon)}$ along arbitrarily late windows, [5, §§2–3, (2) and (6)] requires three arithmetic-geometric inputs beyond the subset-rank bound of [6]:

- **(i) Parahoric level-rank, word-prime window, and initial source slope bounds** [5, (2) and (6), lines 4–7]: split-level fiber ranks, prime-level bounds $\Lambda_\alpha \leq \log T_u \leq c_{\mathrm{Count}} m L$ and $|\log T_u - \log T_{u'}| \leq c_{\mathrm{Count}}\log k$, and two-sided bounds $\mu(\mathcal{M}_u^0) \geq -c_{\mathrm{Slope}}|\mathrm{TT}|\,a\,L_a(1 + m/k)$ and $\mu_{\max}(\mathcal{M}_u^0) \leq c_{\mathrm{Slope}}|\mathrm{TT}|\,a\,L_a$ on the unshifted initial source lattice $\mathcal{M}_u^0$ ($M_u^{\mathrm{full}}$ in [5, §§2.1, 3.1, (6)], before [5, (5)] applies the finite ideal shifts to form $\mathcal{N}_u$ and [5, §3.3] subtracts $\operatorname{ht}(B_u) \leq h_u$);
- **(ii) Common dual-row Arakelov covolume and slope descent**: bounding the normalized Arakelov slope $\mu_{\mathrm{Def}}(\mathbf{b}_{\mathrm{std}}, X_W, M_j) = -\mathrm{lcv}(X_W, M_j)/d$ of the test-row lattices across non-equidistributed geometric components, positive-corank injective maps, and "bad" quotient excision; and
- **(iii) Signed row-covolume and period-height divisibility bracket** [5, §3.1, (6), line 1]:

$$
\mu(\mathcal{R}^\vee) + h_u - F_o^{[5]} \leq S_{\mathrm{Div}} - A\log T_u + E_{\mathrm{Div}},
$$

where [5, §2.2] defines the common finite-divisor shift with the factor of $2$ built in ($F_o^{[5]} := 2 \sum_w l_w \sum_j F_{jw}$), whereas `StatementK.TheoremDivIneq` in [1] writes the un-doubled sum $\mathrm{Fo} := \sum_w l_w \sum_j F_{jw}$ and bounds $\mu_C + h_u - 2\,\mathrm{Fo}$. Under the exact identification $F_o^{[5]} = 2\,\mathrm{Fo}$ and $\mu_C = \mu(\mathcal{R}^\vee)$, the left-hand sides of [5, (6)] and Theorem 4.2 below coincide identically.

Three mathematical questions govern how these inputs work together:

1. **Parahoric level-rank supply and source maximal-slope control (`Conclusion4f`, `CountF`, `SlopesMF`).** Under Harder–Narasimhan filtration integration [5, §3.3], a near-tight frame still admits a kernel-concentration obstruction if positive source slopes sit on $\ker(B_u)$: on a rank-$r$ lattice with centered slopes $((r - 1)M, -M, \dots, -M)$, a corank-$1$ map annihilates the $(r - 1)M$ line while sending the remaining $r - 1$ slopes to $-M$. Meanwhile, fixed-rank $\mathrm{GL}_2$ Mellin-rescaling methods on rStation [7] encounter a rigid $5/6$ exponent ceiling when matching principal-row monomials. How do the parahoric level-rank formula and torus-pair variation interfaces propagate into explicit constants $C_{\mathrm{count}}$ and $C_{\mathrm{slopes}}$, and how do the algebraic scaling relations of growing CM degree $2f$ and weight $k \geq m^2 L$ interact with those bounds at fixed cutoffs?
2. **Multi-component height descent and good/bad Arakelov lattice surgery (`FromComp.core`, `MeanHeightDescent`).** Bounding the toroidal target covolume from below transfers mean height bounds across a non-equidistributed finite set $\iota$ of components $c \in \iota$ whose heights $h_c$ can be negative (where component-averaged first moments suffer from spectral-twin depth aliasing, cf. [8]), then descends slopes across an injective $K$-linear map of corank $\leq \varepsilon_{\mathrm{rk}} d_B$ and excises a "bad" sublattice or quotient under potentially anisotropic place frames. Which exact hypotheses prevent sub-critical jet divergence, moment-aliased negative-height losses, unequal-weight conflation, oblique-projection norm blowup, and unimodular skew anisotropy?
3. **Paired covolume–height cancellation and 8-channel division absorption (`DivAssembly`, `AbsorbE`, `DivisionInequalityWithCovolume`).** Once $\mathrm{lcv}(X_W, M_j) / d = -\mu_{\mathrm{Def}}(\mathbf{b}_{\mathrm{std}}, X_W, M_j)$ is bounded for each of the $m$ lifts $j \in J$, how do the metric shift $\log\kappa$, finite-place valuation weights $n_\nu(j, \rho) = \mathbf{1}_{\rho \in \mathrm{TT}} a_{\mathrm{T}}(\rho) + k w(j, \rho) + \delta(j, \rho)$, and eight distinct arithmetic/analytic error channels telescope into the two-scale budget $(50 C_0 + 10)\bigl(|\mathrm{TT}|\,a\,L_a + m(B_0 + N_c) x_e\bigr)$ balancing $x/m$ against $m$ at $m \asymp x^{1/2}$?

### Attribution, Unconditional Proofs Here, and Conditional Interface Boundary

This paper provides a self-contained mathematical exposition, natural-language proof reconstruction, and sharpness audit of the parahoric level-count (`StandardLattice.lean`, `JointsL.lean`, `SlopesMFOfCountFam.lean`), Arakelov mean-height and slope descent (`MeanHeightDescent/`, `UniformLowerBoundOfSums.lean`), and covolume–division assembly (`QuotientMetricDivisors/`, `DivisionInequalityWithCovolume.lean`) modules of [1]. It does **not** claim an unconditional proof of RH, construct the global CM automorphic host family, or prove the external class-number, local representation-theoretic, and arithmetic-geometric interfaces tabulated in §5 (Table 1). All formal parameter regimes and theorem statements originate in [1]; our contributions are self-contained proofs of the unconditional algebraic, combinatorial, and Arakelov-lattice cores (situated relative to classical Arakelov/Minkowski slope theory [9], [10], [11] and rStation companion results [2]–[8]), exact constant derivations across module seams, and machine-checked sharpness counterexamples:

- **Conditional parahoric level-rank, `Count_at`, and `SlopesM_at` deductions (§2, Proposition 2.1, Theorems 2.2–2.3, Remark 2.3, Proposition 2.4):** From the trivial-stabilizer and class-number interfaces, we derive $\dim_{\mathbb{C}} \mathrm{Mu}_0(u) = d_u^* (T_u^k - 1)^f$ and illustrate its finite-ring free-orbit mechanism for monic irreducible reductions vs. square-class stabilizer deficits; from `TorusPairsWithVariant` and `VandermondeVariationBound` with signed constant $C \in \mathbb{R}$, we prove `Count_at` with $C_{\mathrm{count}} = \max(C, 0) + 2$ (specializing to $C_{\mathrm{count}} = \max(13, 18 + 3 C_0)$ at the release value $C = \max(11, 16 + 3 C_0)$), $x^{14} \leq \exp(x^{\varepsilon/3}) \implies 7\log x \leq L$, and `SlopesM_at` with $C_{\mathrm{slopes}} = 2 C_{\mathrm{count}} + \max(C_5, C_6, 0)(12 + C_{\mathrm{count}} + c_L)$; and we analyze algebraic parameter compatibility vs. fixed-$\mathrm{GL}_2$ monomial matching [7] and fixed-cutoff $\ker(B_u)$ slope bounds.
- **Unconditional multi-component jet amplification and hypothesis sharpness (§3.1–§3.2, Theorem 3.1, Proposition 3.2):** We prove `MeanHeights`, `SumComponents`, and `FromComp.core` unconditionally for all $T \geq 3D + 4$, yielding $\mu \geq -2(3 C_1 + C_2 + 4) E$. Proposition 3.2 establishes: (1) an isolated single-hypothesis counterexample violating only $T \geq 3D + 4$ (separating logarithmic divergence at $T = 3D + 3$ from linear divergence at $T \leq 3D + 2$, while $T = 3D + 4$ still holds); (2) why the descending-slope link already forces $h_c + c_s + c_c \geq 0$ pointwise (so $c_c$ grows linearly with $M$ when $h_c = -M < -c_s$), whereas relaxing pointwise height bounds to component-averaged moments fails under equal-mean spectral twins [8]; and (3) an isolated single-hypothesis counterexample violating only the multiplicity-spread bound $\delta_c \leq \delta'/(1 - \rho)$.
- **Unconditional Arakelov slope descent, all-place Hermitian-idempotent surgery, and explicit hypercube Minkowski cap (§3.3–§3.4, Theorems 3.3–3.4, Proposition 3.5):** Working uniformly in the normalized Arakelov scale $\mu_{\mathrm{Def}}, \mathrm{muMinDef}, \mathrm{muMaxDef}$ (with the explicit zero-rank degree convention $(\operatorname{rk}_K 0)\,\mu_{\mathrm{Def}}(0) := 0$), we prove unconditionally: (i) `SpanMuMin` ($\mathrm{muMinDef}(B) \geq -2\Lambda$ via rank-one finite-index sublattice monotonicity and HN saturation); (ii) `DescentSlope` and `descent_numeric`; (iii) `GoodBadCut` via orthogonal quotient covolume decomposition and $g(\mathrm{id}_V - e)$-dilation under self-adjointness at *every* archimedean place (with a two-place counterexample over $\mathbb{Q}(\zeta_5)$ when self-adjointness fails at a single place, plus fractional-idempotent verification when $e(N) \not\subseteq N$); (iv) `MuMaxMinkowski` with the explicit constant-free bound $\mathrm{muMaxDef}(B) \leq 2 L_a + \log(\operatorname{rk}_K B) + \frac{\log|\Delta_K|}{[K:\mathbb{Q}]}$ via Blichfeldt hypercube packing; and (v) `SlopeLowerChain` and `CovolumeFromSlope` under $x \geq 1, \varepsilon > 0, L = x^\varepsilon \geq 1$ (with an isolated full-hypothesis counterexample violating only $x \geq 1$ at $x = 1/2, L = 1/2$, plus bad-rank overflow $d_b = 25 > 24$ and skew-frame anisotropy $X = \operatorname{diag}(\delta, \delta^{-1})$ with short vector $e_2$).
- **Unconditional covolume–division telescope and 8-channel absorption (§4, Theorems 4.1–4.2, Proposition 4.3, Remark 4.4):** Under $a_{\mathrm{T}}(t) \geq 0$ and $F_o^{[5]} = 2\,\mathrm{Fo}$, we prove `DivAssembly`, `AbsorbE`, and `DivisionInequalityWithCovolume`, obtaining $2 C_0 P + (49 C_0 + 7) H \leq (50 C_0 + 10)(P + H)$, constructing an explicit error saturation attaining $2 C_0 P$, aligning the $\mathbb{Z}[i]^d$ frame-covolume signs under $\|x\|_v = \|X_v^{-1} x\|_2$, and verifying in Remark 4.4 how $(P, H)$ specialize to the $(x/m, m)$ prime-window error terms balanced at $m \asymp x^{1/2}$ in [3, §4.5] and [5, §5.3].

---

## 2. Parahoric Level Rank, Prime-Window Variation, and Source Maximal-Slope Control

Let $E / F$ be a CM quadratic extension of a totally real field $F$ of degree $f = [F : \mathbb{Q}] \geq 1$ ($[E : \mathbb{Q}] = 2f$), with $m \geq 2$ theta-lift rows, weight parameter $k \geq m + 3$ ($k \geq 5$ even), and scale parameters $x > 1$, $0 < \varepsilon < 1/52$, $L := x^\varepsilon \geq 1$, $b := e^L$, $X' := \exp(x^{\varepsilon/3})$, $a := x b$, and $L_a := \log(a \cdot \mathrm{rd}_E)$ where $\mathrm{rd}_E \geq 1$ satisfies $\log \mathrm{rd}_E \leq L$ and $\log x \leq L$ (so $1 \leq L \leq L_a \leq 3L$). Each word $u \in \mathcal{W}$ carries a prime level $T_u$ split in $F$, auxiliary primes $g_0, g_1 \geq (k b)^8$, unramified base fiber dimension $d_u^* \in \mathbb{Z}_{\geq 1}$, ambient reference dimension $D_* > 0$, and common parahoric factor $\Gamma_P > 1$.

### 2.1 Trivial-Stabilizer Parahoric Level Rank (`Conclusion4f`)

**Proposition 2.1 (Conditional Parahoric Level-Rank Identity `Conclusion4f`, cf. `StandardLattice.lean:463-473`).** *Assume for a word $u \in \mathcal{W}$ with prime level $T_u$ split in $F$:*
1. *(Dimension tie at trivial stabilizers, `SmallOrderPrimeLogSumBound` + `Mu0Tie`):* *Every class in the parahoric double-coset set $\mathrm{cls}_0(u)$ has trivial finite-order stabilizer ($\mathrm{StabZero}$), so that $\mathrm{Mu}_0(u)$ decomposes as a direct sum over $\mathrm{cls}_0(u)$ of local tensor fibers of dimension $\prod_\rho \dim V(u, \rho)$:*

$$
\dim_{\mathbb{C}} \mathrm{Mu}_0(u) = |\mathrm{cls}_0(u)| \prod_\rho \dim V(u, \rho).
$$

2. *(Relative class-number formula, `ClassNumberFormula₂`):* *At split prime level $T_u$ (and split auxiliary primes $g_0, g_1$), the principal-congruence quotient modulo $T_u$ contributes a free $(\mathbb{F}_{T_u^k}^\times)^f$-action over the base class count $h_0$, giving $|\mathrm{cls}_0(u)| = h_0 (T_u^k - 1)^f$.*

*Writing $d_u^* := h_0 \prod_\rho \dim V(u, \rho)$, we have*

$$
\dim_{\mathbb{C}} \mathrm{Mu}_0(u) = d_u^* (T_u^k - 1)^f.
$$

*Proof.* Substituting $|\mathrm{cls}_0(u)| = h_0 (T_u^k - 1)^f$ from (2) into (1) and grouping $d_u^* = h_0 \prod_\rho \dim V(u, \rho)$ yields $\dim_{\mathbb{C}} \mathrm{Mu}_0(u) = d_u^* (T_u^k - 1)^f$. $\square$

*Finite-ring model vs. stabilizer deficit.* Let $P \in \mathbb{Z}[X]$ be a **monic** polynomial of degree $k \geq 1$ whose reduction modulo a prime $p$ is irreducible in $\mathbb{F}_p[X]$ (monicity ensures $\deg(P \bmod p) = k$). In $R := (\mathbb{Z}/p^2\mathbb{Z})[X]/(P(X))$, reduction modulo $p$ identifies the unit quotient $R^\times / (1 + p R)$ with $\mathbb{F}_{p^k}^\times$ of order $p^k - 1$; across $f$ split factors, $(\mathbb{F}_{p^k}^\times)^f$ acts freely and transitively on $(p^k - 1)^f$ cosets, each carrying $d_u^*$ fiber coordinates. By contrast, when a nontrivial subgroup $H \subset \mathbb{F}_p^\times$ of order $|H| > 1$ stabilizes each orbit point (e.g., $H = \{\pm 1\} \subset \mathbb{F}_5^\times$ acting on the two quadratic-residue cosets $\{1, 4\}, \{2, 3\} \subset \mathbb{F}_5^\times$ with $d_u^* = 3$), the modeled dimension drops from $(p - 1) d_u^* = 12$ to $\frac{p - 1}{|H|} d_u^* = 6$. This finite-ring model illustrates the free-coset algebra of (2); realizing the geometric hypotheses (1)–(2) on the automorphic family remains external obligation B1 in Table 1.

### 2.2 From `Conclusion5₂` to Prime-Level Windows (`Count_at`) and `SlopesMF`

Define for each word $u \in \mathcal{W}$ the continuous level scale $X_u := (D_* / d_u^*)^{1/(fk)} > 0$, $\log X_u := \frac{1}{fk}\log(D_* / d_u^*)$, and the $\Gamma_P$-adjusted threshold

$$
T_u^* := X_u \cdot \Gamma_P^{-2/(fk)}, \qquad \log T_u^* = \log X_u - \frac{2\log \Gamma_P}{fk}.
$$

Given positive lift weights $w_{j,\rho} > 0$ ($0 \leq j < m$, $|\{\rho\}| = f$) and host covolume parameter $v_{\mathrm{host}} \geq \pi$, define (`StandardLattice.lowB`):

$$
\mathrm{lowB}(C) := \sum_{j=0}^{m-1} \frac{1}{f}\sum_{\rho} \log\Bigl(\frac{w_{j,\rho} v_{\mathrm{host}}}{\pi}\Bigr) + m(\log g_0 + \log g_1) - C\Bigl(L + \frac{m^2 L}{k}\Bigr).
$$

**Theorem 2.2 (Conditional Deduction of `Count_at` and Power-Bound Log Domination, cf. `JointsL.lean:20-143`, `SevenLogLeLOfPowerBound.lean`).** *Assume $f \geq 1$, $k \geq 3$, $L_a \geq L \geq 1$, and that all words $u \in \mathcal{W}$ share a common $\Gamma_P > 1$ with $\frac{\log \Gamma_P}{fk} \leq 1$ and prime levels $T_u$ chosen in the rounding window*

$$
T_u^* \leq T_u \leq T_u^*\Bigl(1 + \frac{1}{fk}\Bigr).
$$

1. *(`count_at_of`): Assume there exists a constant $C \in \mathbb{R}$ such that (`TorusPairsWithVariant`, `VandermondeVariationBound`): (a) $\mathrm{lowB}(C) - \frac{2\log \Gamma_P}{fk} \leq \log T_u \leq C m L$ and $\bigl|\log\frac{d_u^*(T_u^k - 1)^f}{D_* \Gamma_P^{-2}}\bigr| \leq C$ for all $u \in \mathcal{W}$; and (b) $|\log X_u - \log X_{u'}| \leq C \log k$ for all $u, u' \in \mathcal{W}$ (whenever $\mathcal{W} \neq \emptyset$, prime $T_u \geq 2$ implies $\log T_u > 0$, which with $m L > 0$ already forces $C > 0$; writing $\max(C, 0) + 2$ as in `JointsL.lean:25` avoids extracting a witness $u \in \mathcal{W}$ and guards vacuous $\mathcal{W} = \emptyset$). Setting $C_{\mathrm{count}} := \max(C, 0) + 2 > 0$, every $u, u' \in \mathcal{W}$ satisfies:*

$$
\mathrm{lowB}(C_{\mathrm{count}})_{L \leftarrow L_a} \leq \log T_u \leq C_{\mathrm{count}} m L, \qquad |\log T_u - \log T_{u'}| \leq C_{\mathrm{count}} \log k,
$$

*where $\mathrm{lowB}(C_{\mathrm{count}})_{L \leftarrow L_a}$ replaces $C(L + m^2 L/k)$ in $\mathrm{lowB}(C)$ by $C_{\mathrm{count}}(L_a + m^2 L_a / k)$.*
2. *(`seven_log_le_L_of_power_bound`): If $x \geq 4$, $0 < \varepsilon < 1$, and $x^{14} \leq X' := \exp(x^{\varepsilon/3})$, then $7 \log x \leq L = x^\varepsilon$.*

*Proof.* For (1), taking logarithms of $T_u^* \leq T_u \leq T_u^*(1 + (fk)^{-1})$ and using $\log(1 + (fk)^{-1}) \leq (fk)^{-1} \leq 1$ (as $fk \geq 3$) gives $\log T_u^* \leq \log T_u \leq \log T_u^* + 1$. Since $C \leq \max(C, 0)$, $1 \leq L + m^2 L/k \leq L_a + m^2 L_a / k$, and $\frac{2\log \Gamma_P}{fk} \leq 2 \leq 2(L_a + m^2 L_a / k)$, we have $C(L + m^2 L/k) + \frac{2\log \Gamma_P}{fk} \leq (\max(C, 0) + 2)(L_a + m^2 L_a / k)$, so the lower bound in (a) gives $\mathrm{lowB}(C_{\mathrm{count}})_{L \leftarrow L_a} \leq \log T_u$, while $\log T_u \leq C m L \leq C_{\mathrm{count}} m L$ as $m L \geq 0$. For $u, u' \in \mathcal{W}$, common $\Gamma_P$ gives $\log T_u^* - \log T_{u'}^* = \log X_u - \log X_{u'}$; since $\log T_u \in [\log T_u^*, \log T_u^* + 1]$, $\log T_{u'} \in [\log T_{u'}^*, \log T_{u'}^* + 1]$, $|\log X_u - \log X_{u'}| \leq \max(C, 0)\log k$, and $1 \leq \log k$ (as $k \geq 3 > e$), the rounding discrepancy is at most $1 < 2\log k$, giving $|\log T_u - \log T_{u'}| \leq |\log X_u - \log X_{u'}| + 1 \leq C_{\mathrm{count}} \log k$.

For (2), taking logarithms of $x^{14} \leq \exp(x^{\varepsilon/3})$ gives $14 \log x \leq x^{\varepsilon/3}$. Since $x \geq 4 > 1$ and $\varepsilon > 0$, $x^{2\varepsilon/3} > 1$, whence $7\log x < 14\log x \leq x^{\varepsilon/3} < x^\varepsilon = L$. $\square$

**Remark 2.3 (Specialization to the Release Value $C = \max(11, 16 + 3 C_0)$).** In `TheoremThreeOfExplicitAndCompact.lean:328-344`, `part_five_family_of_explicit` derives `Conclusion5₂` (supplying hypotheses (a)–(b) of Theorem 2.2(1)) from `FamilyVandermondeCountExplicit` and `RowsAF` ($x \geq 44^4$, $m \geq 44$) with $C_Y = C_0$ and $C = \max(11, 16 + 3 C_0)$. Substituting this release value into Theorem 2.2(1) yields $C_{\mathrm{count}} = \max(11, 16 + 3 C_0) + 2 = \max(13, 18 + 3 C_0)$ (which simplifies to $18 + 3 C_0$ whenever $C_0 \geq 0$).

**Theorem 2.3 (Conditional Source Slope Assembly `SlopesM_at` / `SlopesMF`, cf. `JointsL.lean:1373-1590`, `SlopesMFOfCountFam.lean`).** *Let $|\mathrm{TT}| \geq 1$, $x > 1$, $L > 0$, $b = e^L$, $a = x b > 0$, $\mathrm{rd}_E \geq 2$, $v_{\mathrm{host}} = \mathrm{rd}_E / 2 \geq 1$, $L_a = \log x + L + \log\mathrm{rd}_E$ (so $0 < L \leq L_a$ and $0 \leq \log v_{\mathrm{host}} \leq \log\mathrm{rd}_E \leq L_a$), $0 < S_c \leq B$, $0 \leq c_L$, $0 \leq C_{\mathrm{count}}$, $0 \leq \log T_u \leq C_{\mathrm{count}} m L_a$, $1 \leq m \leq k$, $f k B \leq |\mathrm{TT}|\,a$, $f k^2 \leq |\mathrm{TT}|\,a$, and $0 \leq \log k \leq 5\log x$ (whence $\log k \leq 5 L_a$ and $0 \leq \log(k v_{\mathrm{host}}) = \log k + \log v_{\mathrm{host}} \leq 6 L_a$). For each word $u \in \mathcal{W}$, let $\mathcal{M}_u^0 := \mathrm{lat}_u(0)$ denote the unshifted initial source lattice ($M_u^{\mathrm{full}}$ in [5, §§2.1, 3.1, (6)]), and suppose local $w$-adic and archimedean valuation estimates (`Conclusion5` and `Conclusion6` in `FlipTwoThree.lean:442-456`, instantiated via `NumsL` at $L \leftarrow c_L L$ and `WtsL`) satisfy*

$$
\mu(\mathcal{M}_u^0) \geq -S_1(u) - C_5\bigl(|\mathrm{TT}|\,a\log k + f k B \log k + f S_c \log T_u + f k^2 (c_L L)\bigr),
$$

$$
\mu_{\max}(\mathcal{M}_u^0) \leq C_6\bigl(|\mathrm{TT}|\,a\log(k v_{\mathrm{host}}) + f B\bigl(k \log(k v_{\mathrm{host}}) + \log T_u\bigr) + f k^2 (c_L L)\bigr),
$$

*where $S_1(u) := \sum_{t \in \mathrm{tops}} \frac{a_{\mathrm{T}}(u, t)}{k}\log T_u$ with $|\mathrm{tops}| = |\mathrm{TT}|$ and $0 \leq a_{\mathrm{T}}(u, t) \leq 2a$ (`Wts`), and $C_5, C_6 \in \mathbb{R}$ are (possibly signed) constants. Then with $C_+ := \max(C_5, C_6, 0) \geq 0$ and*

$$
C_{\mathrm{slopes}} := 2 C_{\mathrm{count}} + C_+(12 + C_{\mathrm{count}} + c_L),
$$

*every word $u \in \mathcal{W}$ satisfies the initial source-slope inequalities of [5, §3.1, (6), lines 6–7]:*

$$
\mu(\mathcal{M}_u^0) \geq -C_{\mathrm{slopes}} |\mathrm{TT}|\,a\,L_a\Bigl(1 + \frac{m}{k}\Bigr), \qquad \mu_{\max}(\mathcal{M}_u^0) \leq C_{\mathrm{slopes}} |\mathrm{TT}|\,a\,L_a.
$$

*Proof.* Since $|\mathrm{tops}| = |\mathrm{TT}|$ and $a_{\mathrm{T}}(u, t) \leq 2a$, we have $S_1(u) \leq |\mathrm{TT}|\,\frac{2a}{k}\log T_u \leq 2 C_{\mathrm{count}} |\mathrm{TT}|\,a\,L_a \frac{m}{k} \leq 2 C_{\mathrm{count}} |\mathrm{TT}|\,a\,L_a (1 + \frac{m}{k})$. Both parenthesized brackets multiplying $C_5$ and $C_6$ are nonnegative, so replacing $C_5$ and $C_6$ by $C_+ \geq \max(C_5, C_6, 0)$ weakens both bounds in the valid direction. Using $f k B \leq |\mathrm{TT}|\,a$, $f S_c \leq f B \leq |\mathrm{TT}|\,a / k$, $f k^2 \leq |\mathrm{TT}|\,a$, $\log k \leq 5 L_a$, $\log(k v_{\mathrm{host}}) \leq 6 L_a$, $0 < L \leq L_a$, and $\frac{1}{k}\log T_u \leq C_{\mathrm{count}} \frac{m}{k} L_a \leq C_{\mathrm{count}} L_a$ ($m \leq k$), the $C_6$ bracket is at most

$$
|\mathrm{TT}|\,a\,(6 L_a) + |\mathrm{TT}|\,a\,\bigl(6 L_a + C_{\mathrm{count}} L_a\bigr) + |\mathrm{TT}|\,a\,(c_L L_a) = (12 + C_{\mathrm{count}} + c_L)\,|\mathrm{TT}|\,a\,L_a,
$$

and the $C_5$ bracket is at most $|\mathrm{TT}|\,a\,(5 L_a + 5 L_a + C_{\mathrm{count}} \frac{m}{k} L_a + c_L L_a) \leq (12 + C_{\mathrm{count}} + c_L)\,|\mathrm{TT}|\,a\,L_a$. Multiplying by $C_+$ and adding $2 C_{\mathrm{count}} |\mathrm{TT}|\,a\,L_a \frac{m}{k}$ on the lower side and $2 C_{\mathrm{count}} |\mathrm{TT}|\,a\,L_a \geq 0$ on the upper side yields both estimates (`JointsL.lean:1413-1590`). Adding the finite ideal shifts $G + F_o^{[5]} - E_u$ of [5, §2.2, (5)] then passes from $\mathcal{M}_u^0$ to the twisted lattice $\mathcal{N}_u$, and [5, §3.3] subtracts $\operatorname{ht}(B_u) \leq h_u$ during Harder–Narasimhan integration. $\square$

### 2.3 Parameter Compatibility vs. Fixed-Rank Mellin Ceilings and Fixed-Cutoff Kernel Caps

**Proposition 2.4 (Parameter Scaling Relations and Fixed-Cutoff Kernel-Slope Restriction).**
1. *(Fixed-$\mathrm{GL}_2$ monomial matching vs. downstream-compatible growing-(degree, weight) parameter scaling):* *If the affine exponent relation $c - \frac{3}{2} + (\alpha_X - 1)v + (\alpha_Y - 1)w + \alpha_Z z = 0$ of the fixed-rank $\mathrm{GL}_2$ Mellin-moment test kernel [7] is required to hold identically as a linear polynomial in independent variables $(v, w, z)$ (or across four exponent tuples $(v_i, w_i, z_i) \in \mathbb{R}^3$ of affine dimension $3$), then $(c, \alpha_X, \alpha_Y, \alpha_Z) = (\frac{3}{2}, 1, 1, 0)$ uniquely, fixing the six-slot threshold $\sigma = 1 - \alpha_X / 6 = 5/6$. By contrast, along the even integer sequence $t = 2j \geq 2$ with $x = t^{120}$, $\varepsilon = 1/60 < 1/52$, $L = x^\varepsilon = t^2$, $m = t^{60} = x^{1/2}$, $k = x m = t^{180} = x^{3/2}$, $n = t^{62} = x^{31/60}$, and $f = 2n = 2 t^{62}$, the parity conditions ($m, k, f$ even) and the downstream size windows $x^{1/2 - \varepsilon} \leq m \leq x^{1/2 + \varepsilon/2}$ and $x m \leq k \leq n^2 x^{1/2 - \varepsilon}$ of [5, §2] ($t^{180} \leq t^{180} \leq t^{182}$), together with $n \leq x^3$ and $k \leq x^5$ of `JointsL.lean:1622-1625` (and $f k^2 \leq |\mathrm{TT}|\,a$ for $t \geq 38$ under $|\mathrm{TT}| \geq \frac{1}{2} n x^{-\varepsilon/8}$ and $a = x e^{t^2}$), all hold simultaneously while $m^2 L / k = t^{-58} \to 0$ ($\leq 1$) in $\mathrm{lowB}(C)$ and $m / k = t^{-120} \to 0$ in Theorem 2.3 (realizing admissible CM hosts and uniform constants along such a sequence still requires external obligations B1–B5).*
2. *(Fixed-cutoff $\ker(B_u)$ slope restriction):* *At a fixed host cutoff, let $\mathcal{N}_u$ have $K$-rank $r \geq 2$ and centered post-twist shifted slopes $\mu_1 \geq \dots \geq \mu_r$ ($\sum_{q=1}^r \mu_q = 0$, after applying [5, (5)] to $\mathcal{M}_u^0$ and subtracting $h_u$) with $\mu_1$ supported on $\ker(B_u)$ and $\mu_2 = \dots = \mu_r = -M$ ($M > 0$), so $\mu_1 = (r - 1)M$. Any upper bound $\mu_{\max}(\mathcal{N}_u) - h_u \leq U$ enforces $M \leq \frac{U}{r - 1}$ at that fixed $(U, r)$ (along a growing host family, $U$ also scales with the host parameters, so asymptotic control uses the integrated slope comparison of [5, §3.3]).*

*Proof.* In (1), linear independence of $\{1, v, w, z\}$ forces $c - 3/2, \alpha_X - 1, \alpha_Y - 1, \alpha_Z$ to vanish, giving $(3/2, 1, 1, 0)$ and $1 - \alpha_X/6 = 5/6$; for $t = 2j \geq 2$, $x^{1/2-\varepsilon} = t^{58} \leq t^{60} \leq t^{61} = x^{1/2+\varepsilon/2}$, $x m = t^{180} = k \leq t^{182} = n^2 x^{1/2-\varepsilon}$, $m^2 L / k = t^{122}/t^{180} = t^{-58} \leq 1$, and $m/k = t^{-120}$. In (2), $\sum_{q=1}^r \mu_q = 0$ gives $(r - 1)M = \mu_1 \leq \mu_{\max}(\mathcal{N}_u) - h_u \leq U$, hence $M \leq U / (r - 1)$. $\square$

---

## 3. Multi-Component Jet Amplification and Unconditional Arakelov Slope Descent

We now turn to `Formalism/MeanHeightDescent/` and `UniformLowerBoundOfSums.lean`, proving every algebraic, combinatorial, and Arakelov-lattice implication unconditionally from first principles.

### 3.1 Multi-Component Jet Amplification (`MeanHeights`, `SumComponents`, `FromComp.core`)

Let $\iota$ be a nonempty finite index set of geometric components ($n := |\iota| \geq 1$). Each component $c \in \iota$ carries a real height $h_c \in \mathbb{R}$, a component slope $\mathrm{sl}_c \in \mathbb{R}$, a multiplicity share $\delta_c > 0$, a component rank $d_c > 0$, and a component degree $\mathrm{deg}_c \in \mathbb{R}$. When $h_c < 0$, $|h_c| = -h_c$ flips $T h_c - 3(D + 1)|h_c|$ into $(T + 3D + 3)h_c < 0$, while unequal component multiplicities $\delta_c \in [\delta', \delta'/(1 - \rho)]$ prevent factoring $\delta_c$ out of $\sum_{c \in \iota}$ unless the summand is nonnegative. Three coupled conditions resolve this:

1. **Pointwise negative-height floor (`h3`, coupled with `h4`):** $h_c + c_s \geq 0$ for all $c \in \iota$ ($c_s \geq 0$), which linearizes $|h_c| \leq h_c + 2 c_s$;
2. **Logarithmic height linearization:** $A \log(2 + |h_c|) \leq |h_c| + A \log\max(A, 1) + 2$ ($A > 0$), shifting the $|h_c|$ multiplier from $3(D + 1)$ to $3D + 4$;
3. **Jet-order threshold (`hT`):** $T - 3D - 4 \geq 0$ (already valid at the boundary $T = 3D + 4$, and retaining strict positive amplification $T - 3D - 4 \geq 1$ for $T \geq 3D + 5$ as stated in `FromComp.core`), making $(T - 3D - 4)(h_c + c_s) \geq 0$ pointwise across $\iota$.

**Theorem 3.1 (Multi-Component Jet Amplification `MeanHeights`, `SumComponents`, and `FromComp.core`, cf. `CombinedAverageDegreeBoundOf.lean`, `SumComponents.lean`, `UniformLowerBoundOfSums.lean:15-33`).** *Let $\iota$ be a nonempty finite set of cardinality $n = |\iota| \geq 1$. Let $D \geq 0$, $T \geq 3D + 4$, $A > 0$, $c_s, X, c_c, R_1, R_2 \geq 0$, $0 \leq z < 1$, $0 \leq \rho < 1$, $B_n > 0$, and $\delta' > 0$. Assume $(h_c, \mathrm{sl}_c, \delta_c, d_c, \mathrm{deg}_c)_{c \in \iota}$ satisfy:*
1. *(Multiplicity and rank comparability, `h1`–`h2`):* $\delta' \leq \delta_c \leq \frac{\delta'}{1 - \rho}$ *and* $B_n \delta_c \leq d_c \leq \frac{B_n \delta_c}{1 - z}$ *for every $c \in \iota$ (in the integer specialization `FromComp.atPoint`, $D \in \mathbb{Z}_{\geq 0}$ and $T \in \mathbb{Z}$ with $T \geq 3D + 4 \geq D + 1$, so $B_n = \binom{T - 1}{D} \geq 1$);*
2. *(Pointwise negative-height floor and descending component-slope link, `h3`–`h5`):* $h_c + c_s \geq 0$ *and* $(1 - \rho)\max(0, \mathrm{sl}_c + c_s) \leq h_c + c_s + c_c$ *for every $c \in \iota$, with unweighted mean slope* $\frac{1}{n}\sum_{c \in \iota} \mathrm{sl}_c \geq -X$;
3. *(Asymmetric jet-degree floor, `h6`):* *For every $c \in \iota$,*

$$
\mathrm{deg}_c \geq B_n \delta_c\Bigl(T h_c - 3(D + 1)|h_c| - A \log(2 + |h_c|) - R_1 - 2 z R_2\Bigr).
$$

*Then:*
- *(a) (`MeanHeights`):* *Setting $m_0 := \max\bigl(0, (1 - \rho)c_s - X - c_c\bigr) \geq 0$, we have $\frac{1}{n}\sum_{c \in \iota}(h_c + c_s) \geq m_0$.*
- *(b) (`SumComponents`):* *The rank-weighted average degree satisfies*

$$
\frac{\sum_{c \in \iota} \mathrm{deg}_c}{\sum_{c \in \iota} d_c} \geq -T(X + c_c) - c_s\bigl(6D + 10 + T(z + 2\rho)\bigr) - \bigl(A\log\max(A, 1) + 4\bigr) - R_1 - 2z R_2.
$$

- *(c) (`FromComp.core`, valid for all $T \geq 3D + 4$ and stated in [1] with $T \geq 3D + 5$):* *If $R_2 = 0$, $R := R_1 \geq 0$, $E \geq 1$, $T X \leq C_1 E$, $T c_c \leq C_1 E$, $c_s(6D + 10 + T(z + 2\rho)) \leq C_1 E$, $A\log\max(A, 1) + R \leq C_2 E$, and $\mu \geq 2 \frac{\sum_{c \in \iota}\mathrm{deg}_c}{\sum_{c \in \iota} d_c}$, then*

$$
\mu \geq -2(3 C_1 + C_2 + 4) E.
$$

*Proof.* **Part (a):** Pointwise $h_c + c_s \geq 0$ gives $\frac{1}{n}\sum_{c \in \iota}(h_c + c_s) \geq 0$. Moreover, $(1 - \rho)(\mathrm{sl}_c + c_s) \leq (1 - \rho)\max(0, \mathrm{sl}_c + c_s) \leq h_c + c_s + c_c$; averaging over $c \in \iota$ and using $\frac{1}{n}\sum_{c \in \iota}\mathrm{sl}_c \geq -X$ and $\rho X \geq 0$ gives

$$
\frac{1}{n}\sum_{c \in \iota}(h_c + c_s) \geq (1 - \rho)(-X + c_s) - c_c = (1 - \rho)c_s - X - c_c + \rho X \geq (1 - \rho)c_s - X - c_c,
$$

whence $\frac{1}{n}\sum_{c \in \iota}(h_c + c_s) \geq m_0$.

**Part (b):** For any $A > 0$ and $u \geq 0$, we have $A \log(2 + u) \leq u + A \log\max(A, 1) + 2$: if $A \geq 1$, $\log\frac{2 + u}{A} \leq \frac{2 + u}{A} - 1$ gives $A(\log(2 + u) - \log A) \leq 2 + u - A < u + 2$; if $0 < A < 1$, $\log\max(A, 1) = 0$ and $\log(2 + u) \leq 1 + u$, so $A\log(2 + u) \leq A(1 + u) < u + 2$. Next, $h_c + c_s \geq 0$ implies $|h_c| \leq h_c + 2 c_s$ (trivially for $h_c \geq 0$, and $|h_c| - h_c = -2 h_c \leq 2 c_s$ for $h_c < 0$). Applying both at $u = |h_c|$ yields

$$
3(D + 1)|h_c| + A\log(2 + |h_c|) \leq (3D + 4)(h_c + 2 c_s) + A\log\max(A, 1) + 2.
$$

Set $N := (T - 3D - 4) c_s + 2(3D + 4) c_s + (A\log\max(A, 1) + 2) + R_1 + 2 z R_2$. Using $T h_c - (3D + 4)(h_c + 2c_s) = (T - 3D - 4)(h_c + c_s) - (T - 3D - 4)c_s - 2(3D + 4)c_s$, hypothesis (3) gives $\mathrm{deg}_c \geq B_n \delta_c\bigl((T - 3D - 4)(h_c + c_s) - N\bigr)$. Let $W := \sum_{c \in \iota} B_n \delta_c > 0$ and $S := \sum_{c \in \iota} d_c \geq W > 0$. Since $T - 3D - 4 \geq 0$ and $h_c + c_s \geq 0$, $(T - 3D - 4)(h_c + c_s) \geq 0$ for every $c$; using $\delta_c \geq \delta'$, Part (a), and $(1 - \rho) W \leq n B_n \delta'$ gives $\sum_{c \in \iota} \mathrm{deg}_c \geq W\bigl((T - 3D - 4)(1 - \rho) m_0 - N\bigr)$. Since $(1 - \rho) m_0 \geq (1 - \rho)\bigl((1 - \rho)c_s - X - c_c\bigr) \geq (1 - 2\rho)c_s - X - c_c$ and $T - 3D - 4 \geq 0$,

$$
\begin{aligned}
(T - 3D - 4)(1 - \rho) m_0 - N &\geq -(T - 3D - 4)(X + c_c + 2\rho c_s) - 2(3D + 4)c_s - (A\log\max(A, 1) + 2) - R_1 - 2z R_2 \\
&\geq -T(X + c_c) - c_s\bigl(6D + 10 + T(z + 2\rho)\bigr) - \bigl(A\log\max(A, 1) + 4\bigr) - R_1 - 2z R_2 =: -L_*.
\end{aligned}
$$

Here $L_* \geq 4 > 0$. If $(T - 3D - 4)(1 - \rho)m_0 - N \geq 0$, then $\sum_c \mathrm{deg}_c \geq 0 > -L_* S$; if $(T - 3D - 4)(1 - \rho)m_0 - N < 0$, then $0 < W \leq S$ gives $\sum_c \mathrm{deg}_c \geq S\bigl((T - 3D - 4)(1 - \rho)m_0 - N\bigr) \geq -L_* S$. Dividing by $S > 0$ proves (b), and substituting the budgets of (c) gives $L_* \leq (3 C_1 + C_2 + 4) E$, proving (c) for all $T \geq 3D + 4$. $\square$

### 3.2 Hypothesis Sharpness, Coupled Floors, and Moment-Aliased Spectral Twins

**Proposition 3.2 (Isolated Counterexamples for `hT` and `h1`, and Pointwise vs. Moment-Averaged Negative Heights).**
1. *(Isolated necessity of $T \geq 3D + 4$, separating logarithmic and linear divergence):* *On $\iota = \{0, 1\}$ with $c_s = X = c_c = z = R = 0$, $A = E = 1$, $C_1 = C_2 = 0$, $\rho = 1/2$, $\delta' = 1$, $(\delta_0, \delta_1) = (1, 2)$, $B_n > 0$ (with $B_n = \binom{T - 1}{D} \geq 1$ in the integer specialization for $D \geq 1$ and $D + 1 \leq T \leq 3D + 3$, and arbitrary $B_n > 0$ for general $T \leq 3D + 3$), $d_c = B_n \delta_c$, $(h_0, h_1) = (0, h)$, and $(\mathrm{sl}_0, \mathrm{sl}_1) = (0, h)$ ($h > 0$), **every** hypothesis of Theorem 3.1(c) holds except $T \geq 3D + 4$. Setting $\mathrm{deg}_c$ to the jet floor in Theorem 3.1(3) and $\mu = 2\frac{\mathrm{deg}_0 + \mathrm{deg}_1}{d_0 + d_1}$ yields*

$$
\mu = \frac{4}{3}(T - 3D - 3) h - \frac{4}{3}\log(2 + h) - \frac{2}{3}\log 2.
$$

*At the critical boundary $T = 3D + 4$, $\mu \geq -8 = -2(3 C_1 + C_2 + 4) E$ holds for all $h \geq 0$. At $T = 3D + 3$, the linear term vanishes and $\mu = -\frac{4}{3}\log(2 + h) - \frac{2}{3}\log 2 \to -\infty$ logarithmically (at $h = 4096$, $\mu \approx -11.55310389 < -8$). For every $T \leq 3D + 2$, $\mu \leq -\frac{4}{3} h - \frac{4}{3}\log(2 + h) - \frac{2}{3}\log 2 \to -\infty$ linearly (at $T = 3D + 2$ and $h = 4096$, $\mu \approx -5472.8864 < -8$).*
2. *(Coupling of `h3` and `h4`, and failure of component-averaged moments on spectral twins, cf. [8]):* *In Theorem 3.1(2), the pointwise slope link $(1 - \rho)\max(0, \mathrm{sl}_c + c_s) \leq h_c + c_s + c_c$ already forces $h_c + c_s + c_c \geq 0$ for all $c \in \iota$ (so at $c_c = 0$, no configuration can violate $h_c + c_s \geq 0$ while preserving `h4`; on $h = (-M, M)$ with $\mathrm{sl} = (-c_s, c_s)$ and $\rho = 0$, restoring `h4` forces $c_c \geq M - c_s$ to grow linearly with $M$). What fails is replacing the **pointwise** conditions `h3`–`h4` by their **component-averaged** first-moment counterparts $\frac{1}{n}\sum_c(h_c + c_s) \geq 0$ and $(1 - \rho)\frac{1}{n}\sum_c\max(0, \mathrm{sl}_c + c_s) \leq \frac{1}{n}\sum_c(h_c + c_s) + c_c$: on $\iota = \{0, 1\}$ with $B_n = d_c = 1$, $D = 2$, $T = 11 = 3D + 5$, $c_s = 1$, $c_c = X = z = \rho = R = 0$, $A = E = 1$, $C_1 = 22$, $C_2 = 0$, and $\mathrm{sl} = (-1, 1)$, the shallow pair $h^{\mathrm{sh}} = (-1, 1)$ and deep pair $h^{\mathrm{dp}} = (-M, M)$ ($M > 1$) share identical first-moment sum $\sum_c h_c = 0$ (mean $0$) and satisfy both averaged conditions (with second-moment sums $\sum_c h_c^2 = 2$ vs. $2 M^2$, i.e., per-component means $1$ vs. $M^2$; $20{,}000$ and $10{,}000$ at $M = 100$), yet $\mu(h^{\mathrm{dp}}) = 2\frac{\mathrm{deg}_0 + \mathrm{deg}_1}{2} = -18 M - 2\log(2 + M) \to -\infty$ ($\mu \approx -1809.25 < -140 = -2(3 C_1 + C_2 + 4) E$ at $M = 100$).*
3. *(Isolated necessity of the multiplicity-spread bound `h1`):* *On $\iota = \{0, 1\}$ with $D = 1$, $T = 60 \geq 3D + 5$, $B_n = \binom{59}{1} = 59$, $c_s = 100$, $X = c_c = z = R = 0$, $A = E = 1$, $C_2 = 0$, $(h_0, h_1) = (\mathrm{sl}_0, \mathrm{sl}_1) = (-100, 100)$, $\delta' = 1$, and skewed multiplicities $(\delta_0, \delta_1) = (100, 1)$, testing Theorem 3.1(b)–(c) with the uniform-weight parameter $\rho = 0$ ($C_1 = c_s(6D + 10) = 1600$) satisfies **every** hypothesis (`h2`–`h11`) except `h1` ($\delta_0 = 100 > \delta'/(1 - 0)$), while violating both Theorem 3.1(b) ($\frac{\sum_c \mathrm{deg}_c}{\sum_c d_c} \approx -6{,}485.8131 < -1{,}604$) and Theorem 3.1(c) ($\mu \approx -12{,}971.6262 < -9{,}608 = -2(3 C_1 + C_2 + 4) E$).*

*Proof.* In (1), at $c = 0$ we have $(1 - \rho)\max(0, \mathrm{sl}_0 + c_s) = \frac{1}{2}\max(0, 0) = 0 \leq 0 = h_0 + c_s + c_c$, and at $c = 1$ we have $\frac{1}{2}\max(0, h) = \frac{1}{2}h \leq h = h_1 + c_s + c_c$, while $\frac{1}{2}(\mathrm{sl}_0 + \mathrm{sl}_1) = h/2 \geq 0 = -X$ and $A\log\max(A, 1) + R = 0 \leq C_2 E$; direct evaluation of $2(\mathrm{deg}_0 + \mathrm{deg}_1)/(3 B_n)$ with $\mathrm{deg}_0 = -B_n\log 2$ and $\mathrm{deg}_1 = 2 B_n((T - 3D - 3)h - \log(2 + h))$ gives the closed form for $\mu$ and both divergence regimes. In (2), $\max(0, \mathrm{sl}_c + c_s) \geq 0$ and $1 - \rho > 0$ immediately force $h_c + c_s + c_c \geq 0$; for $h^{\mathrm{dp}} = (-M, M)$ at $D = 2, T = 11$, $\mathrm{deg}_0 + \mathrm{deg}_1 = (-11 M - 9 M - \log(2 + M)) + (11 M - 9 M - \log(2 + M)) = -18 M - 2\log(2 + M)$, and $2(\mathrm{deg}_0 + \mathrm{deg}_1)/(1 + 1) = -18 M - 2\log(2 + M)$. In (3), at $\rho = 0$ and $h = \mathrm{sl} = (-100, 100)$, `h3` gives $(0, 200) \geq 0$, `h4` gives $\max(0, 0) = 0 \leq 0$ and $\max(0, 200) = 200 \leq 200$, and `h5` gives $\frac{1}{2}(-100 + 100) = 0 \geq 0$, while $\mu = 2\frac{100(-6600 - \log 102) + 1(5400 - \log 102)}{101} = -\frac{1{,}309{,}200}{101} - 2\log 102 \approx -12{,}971.6262 < -9{,}608$ (whereas at the true spread $\rho = 99/100$, $C_1 = 13{,}480$ gives $-80{,}888$, which holds). $\square$

### 3.3 Unconditional Arakelov Lattice Descent, All-Place Good/Bad Surgery, and Hypercube Minkowski Cap

Let $K$ be a totally complex number field of degree $[K : \mathbb{Q}] = 2 n_{\mathrm{Pl}}$ with archimedean places $\mathrm{Pl}_\infty(K)$ ($|\mathrm{Pl}_\infty(K)| = n_{\mathrm{Pl}} \geq 1$), ring of integers $\mathcal{O}_K$, and absolute discriminant $|\Delta_K|$. Let $V$ be a finite-dimensional $K$-vector space with $K$-basis $\mathbf{b} = (b_i)_{i \in \kappa}$ and invertible frame matrices $X_v \in \mathrm{GL}_\kappa(\mathbb{C})$ ($v \in \mathrm{Pl}_\infty(K)$), defining at each place $v$ the Euclidean coordinate map $f_v(x) := X_v^{-1} v(\mathbf{b}^{-1}(x)) \in \mathbb{C}^\kappa$, local norm $\|x\|_v := \|f_v(x)\|_2$, and Hermitian pairing $\langle x, y\rangle_v := \langle f_v(x), f_v(y)\rangle_{\mathbb{C}^\kappa}$. Under $\rho_{\mathbf{b}, X} : V \hookrightarrow \bigoplus_{v \in \mathrm{Pl}_\infty(K)} \mathbb{C}^\kappa \cong \mathbb{R}^{[K:\mathbb{Q}]|\kappa|}$, every finitely generated $\mathcal{O}_K$-submodule $M \subset V$ of $K$-rank $\operatorname{rk}_K(M) = d > 0$ maps to a discrete $\mathbb{Z}$-lattice $\Lambda(M) := \rho_{\mathbf{b}, X}(M)$ of $\mathbb{Z}$-rank $\operatorname{rk}_{\mathbb{Z}}(\Lambda(M)) = 2 n_{\mathrm{Pl}} d$ with Euclidean covolume $\operatorname{covol}(\Lambda(M)) > 0$, real degree $\operatorname{deg}(M) := -\log\operatorname{covol}(\Lambda(M))$, and real slope $\mathrm{slope}(M) := \frac{\operatorname{deg}(M)}{[K:\mathbb{Q}] d}$, with real minimum and maximum slopes $\mathrm{muMin}(M), \mathrm{muMax}(M)$ defined via Harder–Narasimhan filtration [9], [10]. Following `Formalism/MeanHeightDescent/MuMaxMinkowski.lean:13-86` and `TwistLower.lean:115-133`, we work throughout in the **normalized Arakelov slope scale**:

$$
\begin{aligned}
\mu_{\mathrm{Def}}(\mathbf{b}, X, M) &:= 2\,\mathrm{slope}(M) - \log 2 + \frac{\log|\Delta_K|}{[K : \mathbb{Q}]} = -\frac{2\log\operatorname{covol}(\Lambda(M))}{[K : \mathbb{Q}] d} - \log 2 + \frac{\log|\Delta_K|}{[K : \mathbb{Q}]}, \\
\mathrm{muMinDef}(\mathbf{b}, X, M) &:= 2\,\mathrm{muMin}(M) - \log 2 + \frac{\log|\Delta_K|}{[K : \mathbb{Q}]}, \qquad \mathrm{muMaxDef}(\mathbf{b}, X, M) := 2\,\mathrm{muMax}(M) - \log 2 + \frac{\log|\Delta_K|}{[K : \mathbb{Q}]}.
\end{aligned}
$$

On $V = K^d$ with the standard basis $\mathbf{b}_{\mathrm{std}}$, the normalized log-covolume satisfies $\frac{\mathrm{lcv}(X_W, M)}{d} = -\mu_{\mathrm{Def}}(\mathbf{b}_{\mathrm{std}}, X_W, M)$ (`LcvMu`), and scaling $M \neq 0$ by a nonzero fractional ideal $I$ gives $\mu_{\mathrm{Def}}(\mathbf{b}, X, I \cdot M) = \mu_{\mathrm{Def}}(\mathbf{b}, X, M) - \frac{2\log N(I)}{[K : \mathbb{Q}]}$ (`idealScale_mu`). For $M = 0$ ($\operatorname{rk}_K M = 0$), we adopt the standard convention $\operatorname{covol}(\Lambda(0)) := 1$ and define the rank-weighted Arakelov degree $(\operatorname{rk}_K M)\,\mu_{\mathrm{Def}}(\mathbf{b}, X, M)$ to be $0$ (`rk_mul_mu`, `GoodBadCut.lean:364-377`), so rank-weighted degree inequalities hold uniformly across zero and nonzero submodules without evaluating $0 \cdot \mu_{\mathrm{Def}}(0)$.

**Theorem 3.3 (Spanning-Line Minimum Slope, Injective Slope Descent, All-Place Hermitian-Idempotent Split, and Explicit Hypercube Minkowski Cap, cf. `SpanMuMin.lean`, `DescentSlope.lean`, `GoodBadCut.lean`, `MuMaxMinkowski.lean`).**
1. *(`SpanMuMin`):* *Let $B \subset V$ be a nonzero finitely generated $\mathcal{O}_K$-submodule. If a subset $s \subseteq B$ spans $K \cdot B$ over $K$ and satisfies $\|x\|_v \leq e^\Lambda$ for all $x \in s$ and all $v \in \mathrm{Pl}_\infty(K)$, then*

$$
\mathrm{muMinDef}(\mathbf{b}, X, B) \geq -2\Lambda.
$$

2. *(`DescentSlope`):* *Let $\varphi : V \to W$ be an injective $K$-linear map between equipped spaces $(V, \mathbf{b}, X)$ and $(W, \mathbf{b}', X')$. For any nonzero finitely generated $\mathcal{O}_K$-submodules $A \subset V$ and $B \subset W$ with $\varphi(A) \subseteq B$, injectivity of $\varphi$ on $A \neq 0$ forces $\|\varphi\|_{v,\mathrm{op}} := \|X'^{-1}_v v(\operatorname{Mat}_{\mathbf{b},\mathbf{b}'}(\varphi)) X_v\|_{\mathrm{op}} > 0$ at every $v \in \mathrm{Pl}_\infty(K)$, so $\mathrm{ht}(\varphi) := \frac{2}{n_{\mathrm{Pl}}}\sum_{v \in \mathrm{Pl}_\infty(K)} \log\|\varphi\|_{v,\mathrm{op}} \in \mathbb{R}$ is well-defined, $\operatorname{rk}_K(\varphi(A)) = \operatorname{rk}_K(A)$, and*

$$
(\operatorname{rk}_K A)\bigl(\mu_{\mathrm{Def}}(\mathbf{b}, X, A) - \mathrm{ht}(\varphi)\bigr) + (\operatorname{rk}_K B - \operatorname{rk}_K A)\,\mathrm{muMinDef}(\mathbf{b}', X', B) \leq (\operatorname{rk}_K B)\,\mu_{\mathrm{Def}}(\mathbf{b}', X', B).
$$

3. *(`GoodBadCut`):* *Let $e : V \to V$ be a $K$-linear idempotent ($e \circ e = e$) that is self-adjoint with respect to $\langle \cdot, \cdot\rangle_v$ **at every archimedean place $v \in \mathrm{Pl}_\infty(K)$**: $\langle e x, y\rangle_v = \langle x, e y\rangle_v$ for all $v \in \mathrm{Pl}_\infty(K)$ and $x, y \in V$. Then at every place $v$, $R_v := X_v^{-1} v(\operatorname{Mat}_{\mathbf{b},\mathbf{b}}(e)) X_v$ satisfies $R_v^* = R_v$ and $R_v^2 = R_v$, so $\|R_v\|_{\mathrm{op}} \leq 1$ and $\|I - R_v\|_{\mathrm{op}} \leq 1$. Consequently, for any finitely generated $\mathcal{O}_K$-submodule $N \subset V$ and integer $g \geq 1$ with $g \cdot e(N) \subseteq N$, setting $N_{\mathrm{im}} := N \cap \operatorname{im}(e)$ and $N_{\mathrm{ker}} := N \cap \ker(e)$ gives $\operatorname{rk}_K(N_{\mathrm{im}}) + \operatorname{rk}_K(N_{\mathrm{ker}}) = \operatorname{rk}_K(N)$,*

$$
(\operatorname{rk}_K N)\,\mu_{\mathrm{Def}}(\mathbf{b}, X, N) \leq (\operatorname{rk}_K N_{\mathrm{im}})\,\mu_{\mathrm{Def}}(\mathbf{b}, X, N_{\mathrm{im}}) + (\operatorname{rk}_K N_{\mathrm{ker}})\,\mu_{\mathrm{Def}}(\mathbf{b}, X, N_{\mathrm{ker}}) + 2(\operatorname{rk}_K N_{\mathrm{ker}})\log g,
$$

*and $(\operatorname{rk}_K N_{\mathrm{ker}})\,\mu_{\mathrm{Def}}(\mathbf{b}, X, N_{\mathrm{ker}}) \leq (\operatorname{rk}_K N_{\mathrm{ker}})\,\mathrm{muMaxDef}(\mathbf{b}, X, M)$ for every finitely generated $M \supseteq N$ (by symmetry of $e$ and $\mathrm{id}_V - e$, the identical inequality holds interchanging $(N_{\mathrm{im}}, N_{\mathrm{ker}})$ whenever one piece serves as the good sublattice and the complementary piece as the bad part).*
4. *(`MuMaxMinkowski`):* *For every $(a_v)_{v \in \mathrm{Pl}_\infty(K)} \in \mathbb{R}_{>0}^{n_{\mathrm{Pl}}}$, convexity of $\exp$ gives $n_{\mathrm{Pl}} \exp\bigl(\frac{2}{n_{\mathrm{Pl}}}\sum_{v} \log a_v\bigr) \leq \sum_{v} a_v^2$. Consequently, for any nonzero finitely generated $\mathcal{O}_K$-submodule $B \subset V$ such that every $0 \neq x \in B$ satisfies $\frac{1}{n_{\mathrm{Pl}}}\sum_{v \in \mathrm{Pl}_\infty(K)} \log \|x\|_v \geq -L_a$, we have the explicit bound*

$$
\mathrm{muMaxDef}(\mathbf{b}, X, B) \leq 2 L_a + \log(\operatorname{rk}_K B) + \frac{\log|\Delta_K|}{[K : \mathbb{Q}]}.
$$

*Proof.* **Part (1):** We may replace $s$ by $s \setminus \{0\}$. For each $0 \neq x \in s$, $L_x := \mathcal{O}_K x \subseteq B$ has $\operatorname{rk}_K(L_x) = 1$, and its local Gram determinant at place $v$ is $\|x\|_v^2 \leq e^{2\Lambda}$. Multiplying over $v \in \mathrm{Pl}_\infty(K)$ gives $\mathrm{ht}(L_x) \leq e^{2 n_{\mathrm{Pl}} \Lambda}$ and hence $\mu_{\mathrm{Def}}(\mathbf{b}, X, L_x) \geq -2\Lambda$ (`muDef_line`), i.e., $\mathrm{slope}(L_x) \geq \theta := \frac{-2\Lambda + \log 2 - \log|\Delta_K|/[K:\mathbb{Q}]}{2}$. In the slope characterization [9], $\mathrm{muMin}(L_x) \geq \theta$ holds if and only if $\operatorname{deg}(N) \leq \operatorname{deg}(L_x) - \theta\bigl(\operatorname{rk}_{\mathbb{Z}}(L_x) - \operatorname{rk}_{\mathbb{Z}}(N)\bigr)$ for every $\mathcal{O}_K$-submodule $N \subseteq L_x$ (`muMin_line`, `SpanMuMin.lean:85-120`). For $N = 0$, this reduces to $0 \leq \operatorname{deg}(L_x) - \theta\operatorname{rk}_{\mathbb{Z}}(L_x)$, which is $\mathrm{slope}(L_x) \geq \theta$. For $0 \neq N \subseteq L_x$, since $\dim_K(K \cdot L_x) = 1$, we have $\operatorname{rk}_K(N) = 1 = \operatorname{rk}_K(L_x)$, so $\operatorname{rk}_{\mathbb{Z}}(N) = \operatorname{rk}_{\mathbb{Z}}(L_x)$ and finite-index covolume monotonicity (`covol_of_le`, `TwistLower.lean:26-45`) gives $\operatorname{covol}(\Lambda(N)) = [L_x : N]\operatorname{covol}(\Lambda(L_x)) \geq \operatorname{covol}(\Lambda(L_x))$, i.e., $\operatorname{deg}(N) \leq \operatorname{deg}(L_x)$. Thus $\mathrm{muMinDef}(L_x) = \mu_{\mathrm{Def}}(L_x) \geq -2\Lambda$. By Harder–Narasimhan step saturation (`hnStep_of` [9], [10]), the submodule $S_\theta(B)$ generated by sublattices of real minimum slope $\geq \theta$ is $K$-saturated in $B$ and contains $s$; since $s$ spans $K \cdot B$, $S_\theta(B) = B$, proving $\mathrm{muMinDef}(B) \geq -2\Lambda$.

**Part (2):** Injectivity of $\varphi$ gives $A \cap \ker(\varphi) = 0$, so $\operatorname{rk}_K(\varphi(A)) = \operatorname{rk}_K(A) > 0$, and choosing $0 \neq a \in A$ gives $\|\varphi(a)\|_v > 0$, whence $\|\varphi\|_{v,\mathrm{op}} > 0$ for every $v$. Exterior-power norm submultiplicativity at each place $v$ gives $\mathrm{ht}(\varphi(A)) \leq \bigl(\prod_{v} \|\varphi\|_{v,\mathrm{op}}\bigr)^{2 \operatorname{rk}_K(A)} \mathrm{ht}(A)$, i.e., $\mu_{\mathrm{Def}}(\mathbf{b}', X', \varphi(A)) \geq \mu_{\mathrm{Def}}(\mathbf{b}, X, A) - \mathrm{ht}(\varphi)$. By definition of $\mathrm{muMin}(B)$ on $\varphi(A) \subseteq B$, $\operatorname{deg}(B) \geq \operatorname{deg}(\varphi(A)) + \mathrm{muMin}(B)\bigl(\operatorname{rk}_{\mathbb{Z}}(B) - \operatorname{rk}_{\mathbb{Z}}(\varphi(A))\bigr)$; multiplying by $\frac{2}{[K:\mathbb{Q}]}$ and adding $(\operatorname{rk}_K B)\bigl(\frac{\log|\Delta_K|}{[K:\mathbb{Q}]} - \log 2\bigr)$ to both sides cancels the constant shift across $\operatorname{rk}_K A + (\operatorname{rk}_K B - \operatorname{rk}_K A) = \operatorname{rk}_K B$ and substitutes $\mu_{\mathrm{Def}}(\varphi(A)) \geq \mu_{\mathrm{Def}}(A) - \mathrm{ht}(\varphi)$.

**Part (3):** At each place $v \in \mathrm{Pl}_\infty(K)$, set $U_v := X_v^{-1}$ and $M_v := v(\operatorname{Mat}_{\mathbf{b},\mathbf{b}}(e))$, so $R_v = U_v M_v X_v$ and $X_v U_v = I$. Self-adjointness $\langle e b_k, b_l\rangle_v = \langle b_k, e b_l\rangle_v$ gives $(U_v M_v)^* U_v = U_v^* (U_v M_v)$. Using $U_v M_v X_v U_v = U_v M_v$, we obtain $U_v^* R_v^* U_v = (R_v U_v)^* U_v = (U_v M_v)^* U_v = U_v^* (U_v M_v) = U_v^* R_v U_v$; multiplying on the left by $(U_v^*)^{-1}$ and on the right by $U_v^{-1}$ yields $R_v^* = R_v$, while $e^2 = e$ gives $R_v^2 = R_v$ (`GoodBadCut.lean:64-90`). For any $z \in \mathbb{C}^\kappa$ and $y := R_v z$, $\|y\|_2^2 = \langle R_v z, y\rangle = \langle z, R_v^2 z\rangle = \langle z, y\rangle \leq \|z\|_2 \|y\|_2$, so $\|R_v\|_{\mathrm{op}} \leq 1$ and similarly $\|I - R_v\|_{\mathrm{op}} \leq 1$. Note that $g \cdot e(N) \subseteq N$ does *not* require $e(N) \subseteq N$ (for example, $N = \mathbb{Z}[i]^2$, $g = 2$, and $e = \frac{1}{2}\bigl(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\bigr)$ has $e(1, 0) = (\frac{1}{2}, \frac{1}{2}) \notin N$). Instead, following `GoodBadCut.lean:393-438`, set $\varphi := g(\mathrm{id}_V - e) : V \to V$ and $I := \varphi(N)$. For every $x \in N$, $g x \in N$ and $g e(x) \in N_{\mathrm{im}}$, so $\varphi(x) = g x - g e(x) \in N \cap \ker(e) = N_{\mathrm{ker}}$ and $g x = g e(x) + \varphi(x) \in N_{\mathrm{im}} \oplus N_{\mathrm{ker}} \subseteq N$, giving $K \cdot N = (K \cdot N_{\mathrm{im}}) \oplus (K \cdot N_{\mathrm{ker}})$ and $\operatorname{rk}_K(N_{\mathrm{im}}) + \operatorname{rk}_K(N_{\mathrm{ker}}) = \operatorname{rk}_K(N)$, while $g N_{\mathrm{ker}} \subseteq I \subseteq N_{\mathrm{ker}}$ gives $\operatorname{rk}_K(I) = \operatorname{rk}_K(N_{\mathrm{ker}})$. At every place $v$, $R_v$ and $I - R_v$ are complementary orthogonal projections in Euclidean coordinates; thus under $(I - R) := (I - R_v)_{v \in \mathrm{Pl}_\infty(K)}$, the kernel of $(I - R)|_{\Lambda(N)}$ is $\Lambda(N) \cap \bigoplus_v \operatorname{im}(R_v) = \Lambda(N_{\mathrm{im}})$ and $(I - R)\Lambda(N) \subset \bigoplus_v \ker(R_v) \perp \mathbb{R}\Lambda(N_{\mathrm{im}})$, so Fubini's theorem on the orthogonal subspace/quotient decomposition yields $\operatorname{covol}(\Lambda(N)) = \operatorname{covol}(\Lambda(N_{\mathrm{im}})) \cdot \operatorname{covol}((I - R)\Lambda(N))$ (under $\operatorname{covol}(\{0\}) = 1$). Since $\Lambda(I) = g(I - R)\Lambda(N) \subseteq \Lambda(N_{\mathrm{ker}})$ is the $g$-dilation of $(I - R)\Lambda(N)$ of full $\mathbb{Z}$-rank $[K:\mathbb{Q}]\operatorname{rk}_K(N_{\mathrm{ker}})$, finite-index monotonicity gives $\operatorname{covol}(\Lambda(N_{\mathrm{ker}})) \leq \operatorname{covol}(\Lambda(I)) = g^{[K:\mathbb{Q}]\operatorname{rk}_K(N_{\mathrm{ker}})} \operatorname{covol}((I - R)\Lambda(N))$, whence $\operatorname{covol}(\Lambda(N_{\mathrm{im}}))\operatorname{covol}(\Lambda(N_{\mathrm{ker}})) \leq g^{[K:\mathbb{Q}]\operatorname{rk}_K(N_{\mathrm{ker}})}\operatorname{covol}(\Lambda(N))$. Taking $-\frac{2}{[K:\mathbb{Q}]}\log$ and adding $(\operatorname{rk}_K N)\bigl(\frac{\log|\Delta_K|}{[K:\mathbb{Q}]} - \log 2\bigr)$ under the zero-rank convention $(\operatorname{rk}_K 0)\,\mu_{\mathrm{Def}}(0) = 0$ gives the stated inequality, and $N_{\mathrm{ker}} \subseteq M$ bounds $(\operatorname{rk}_K N_{\mathrm{ker}})\,\mu_{\mathrm{Def}}(N_{\mathrm{ker}}) \leq (\operatorname{rk}_K N_{\mathrm{ker}})\,\mathrm{muMaxDef}(M)$ (trivially $0 \leq 0$ when $N_{\mathrm{ker}} = 0$).

**Part (4):** Jensen's inequality on the convex function $t \mapsto e^t$ with uniform weights $1/n_{\mathrm{Pl}}$ at $t_v = 2\log a_v$ gives $\exp\bigl(\frac{2}{n_{\mathrm{Pl}}}\sum_v \log a_v\bigr) \leq \frac{1}{n_{\mathrm{Pl}}}\sum_v a_v^2$ (`mink_am_gm`). Set $r := \sqrt{n_{\mathrm{Pl}}} e^{-L_a} > 0$. For every $0 \neq x \in B$, $\|\rho_{\mathbf{b}, X}(x)\|_2^2 = \sum_{v \in \mathrm{Pl}_\infty(K)} \|x\|_v^2 \geq n_{\mathrm{Pl}} \exp\bigl(\frac{2}{n_{\mathrm{Pl}}}\sum_v \log\|x\|_v\bigr) \geq n_{\mathrm{Pl}} e^{-2 L_a} = r^2$, so every nonzero lattice vector $y \in \Lambda(B)$ satisfies $\|y\|_2 \geq r$. Let $0 \neq N \subseteq B$ be any finitely generated $\mathcal{O}_K$-submodule, of $\mathbb{Z}$-rank $m_{\mathbb{Z}} := \operatorname{rk}_{\mathbb{Z}}(\Lambda(N)) = 2 n_{\mathrm{Pl}} \operatorname{rk}_K(N) \leq 2 n_{\mathrm{Pl}} \operatorname{rk}_K(B)$. In an orthonormal basis of the real span $\mathbb{R}\Lambda(N) \cong \mathbb{R}^{m_{\mathbb{Z}}}$, any two distinct points $z \neq z'$ in the open hypercube $Q := \bigl(-\frac{r}{2\sqrt{m_{\mathbb{Z}}}}, \frac{r}{2\sqrt{m_{\mathbb{Z}}}}\bigr)^{m_{\mathbb{Z}}}$ satisfy $\|z - z'\|_2 < \sqrt{m_{\mathbb{Z}} \cdot (r/\sqrt{m_{\mathbb{Z}}})^2} = r$, so $z - z' \notin \Lambda(N) \setminus \{0\}$. By Blichfeldt's injection of $Q$ into $\mathbb{R}\Lambda(N)/\Lambda(N)$, $\operatorname{covol}(\Lambda(N)) \geq \operatorname{vol}_{m_{\mathbb{Z}}}(Q) = (r / \sqrt{m_{\mathbb{Z}}})^{m_{\mathbb{Z}}}$, whence

$$
2\,\mathrm{slope}(N) = -\frac{2}{m_{\mathbb{Z}}}\log\operatorname{covol}(\Lambda(N)) \leq \log m_{\mathbb{Z}} - 2\log r \leq \log\bigl(2 n_{\mathrm{Pl}} \operatorname{rk}_K B\bigr) - \bigl(\log n_{\mathrm{Pl}} - 2 L_a\bigr) = 2 L_a + \log 2 + \log(\operatorname{rk}_K B).
$$

Taking the supremum over $0 \neq N \subseteq B$, subtracting $\log 2$, and adding $\frac{\log|\Delta_K|}{[K:\mathbb{Q}]}$ cancels $\log 2 - \log 2 = 0$ and proves $\mathrm{muMaxDef}(\mathbf{b}, X, B) \leq 2 L_a + \log(\operatorname{rk}_K B) + \frac{\log|\Delta_K|}{[K:\mathbb{Q}]}$ (`MuMaxMinkowski.lean:145-164`). $\square$

### 3.4 Numeric Descent, Bad-Row Excision, and Full Covolume Assembly

**Theorem 3.4 (`descent_numeric`, `bad_part_numeric`, `SlopeLowerChain`, and `CovolumeFromSlope`, cf. `BadRowsNumeric.lean`, `CovolumeIntoDivisionHolds.lean`, `Assembly.lean:88-122`).**
1. *(`descent_numeric`):* *Let $0 < d_A \leq d_B$ satisfy $(1 - \varepsilon_{\mathrm{rk}}) d_B \leq d_A$ ($\varepsilon_{\mathrm{rk}} \geq 0$), $X, P \geq 0$, $\mu_A \geq c_{\mathrm{fl}} - X$, $|c_{\mathrm{fl}}| \leq Q$, $\Lambda_{\mathrm{num}} \leq Q$ (where applying Theorem 3.3(1) sets $\Lambda_{\mathrm{num}} := 2\Lambda$), and $d_B \mu_N \geq d_A(\mu_A - P) + (d_B - d_A)(-\Lambda_{\mathrm{num}})$. Then*

$$
\mu_N \geq c_{\mathrm{fl}} - X - P - 2\varepsilon_{\mathrm{rk}} Q.
$$

2. *(`bad_part_numeric`, sharp at $\delta = 1/12$):* *Let $d = d_g + d_b > 0$ with $0 \leq d_b \leq 3\delta d$ and $0 \leq \delta \leq 1/12$. If $d\,\mu_N \leq d_g \mu_G + d_b(m_{\max} + G)$ with $|\mu_N| \leq Q$, $m_{\max} \leq Q$, and $G \leq Q$, then $d_g \geq \frac{3}{4} d > 0$ and $\mu_G \geq \mu_N - \frac{9\delta Q}{1 - 3\delta} \geq \mu_N - 12\delta Q$.*
3. *(`SlopeLowerChain` & `CovolumeFromSlope`):* *Assume $C_1, C_f, b \geq 0$ ($C_1 := C_a + C_b$), $0 \leq q' \leq m$, $w_\tau \geq 0$, $\frac{1}{2} m w_\tau \leq u_{a,\tau}$ for all $\tau$, $\sum_\tau u_{a,\tau} \geq 1$, $0 \leq \log\mathrm{rd} \leq \mathrm{LL}_0$, and $L \leq \mathrm{LL}_0$. Combining $\mu_U \geq -2\bigl(C_1 \mathrm{LL}_0 \sum_\tau u_{a,\tau} + b/4\bigr)$ (supplied via Theorem 3.1(b) and `StatementF.lean:32-35` under the explicit component budgets $T X \leq C_a \mathrm{LL}_0 \sum_\tau u_{a,\tau} + e_1$, $T c_c \leq C_b \mathrm{LL}_0 \sum_\tau u_{a,\tau} + e_2$, $c_s(6D + 10 + T(z + 2\rho)) + (A\log\max(A, 1) + 4) + R_1 + 2 z R_2 + \mathrm{PP}_f + e_1 + e_2 \leq b/4$, and $\mu_U \geq 2\bigl(\frac{\sum_c \mathrm{deg}_c}{\sum_c d_c} - \mathrm{PP}_f\bigr)$ with $C_1 = C_a + C_b$; or via Theorem 3.1(c) when $E \leq \mathrm{LL}_0 \sum_\tau u_{a,\tau}$ and $C_1 = 3 C_1^{\mathrm{jet}} + C_2^{\mathrm{jet}} + 4$) with $\mu_A \geq \mu_U + 2 c_{\mathrm{fl}}$ ($c_{\mathrm{fl}} = \sum_\tau w_\tau c_1(\tau) - C_f q' \log\mathrm{rd} \sum_\tau w_\tau - C_f L$), Parts (1)–(2) (applied at $2 c_{\mathrm{fl}}$ with $|2 c_{\mathrm{fl}}| \leq Q$, $\varepsilon_{\mathrm{rk}} Q \leq b/4$, and $P + 12\delta Q + P_9 \leq b$), and $\mu_{\mathrm{Def}}(\mathbf{b}_{\mathrm{std}}, X_W, M) \geq \mu_G - P_9$ yields*

$$
\mu_{\mathrm{Def}}(\mathbf{b}_{\mathrm{std}}, X_W, M) \geq 2\Bigl(\sum_{\tau} w_\tau c_1(\tau) - (C_1 + 3 C_f)\,\mathrm{LL}_0 \sum_{\tau} u_{a,\tau} - b\Bigr).
$$

*Furthermore, under the scale hypotheses of `StatementA.CovolumeEstimateOfSlopeChain` (`StatementA.lean:49-86`: $x \geq 1$, $\varepsilon > 0$, $L = x^\varepsilon \geq 1$, $b = e^L > 0$, $1 \leq \mathrm{rd}$, $\log\mathrm{rd} \leq L$, $0 \leq L_\chi \leq L$, $\log x \leq L$, $\mathrm{llx} \geq 1$, $\mathrm{LL}_0 = \log(b\cdot\mathrm{rd})\,\mathrm{llx} + L_\chi + \log x$, $f \geq 1$, $m \geq 1$, $|\mathrm{Pl}| \leq f$, $B_0 = f m b L$, $C_c \geq 0$, $|c_1(\tau) + \frac{1}{2} p_q \log\Omega| \leq C_c q'(\log\mathrm{rd} + L_\chi)$, $0 \leq w_\tau \leq 2b$, $u_{a,\tau} \leq 2(m w_\tau + k S + k\eta)$ with $k S, k\eta \leq b$), substituting $\frac{\mathrm{lcv}(X_W, M)}{d} = -\mu_{\mathrm{Def}}(\mathbf{b}_{\mathrm{std}}, X_W, M)$ gives*

$$
\frac{\mathrm{lcv}(X_W, M)}{d} \leq \sum_{\rho} p_q w_\rho \log\Omega + \bigl(64(C_1 + 3 C_f) + 8 C_c + 2\bigr) B_0\,\mathrm{llx}.
$$

*Proof.* **Part (1):** Since $d_B - d_A \geq 0$, $-\Lambda_{\mathrm{num}} \geq -Q$, and $c_{\mathrm{fl}} - X - P \leq c_{\mathrm{fl}} \leq Q$, we have $d_B \mu_N \geq d_A(c_{\mathrm{fl}} - X - P) - (d_B - d_A) Q = d_B(c_{\mathrm{fl}} - X - P) - (d_B - d_A)(c_{\mathrm{fl}} - X - P + Q) \geq d_B(c_{\mathrm{fl}} - X - P - 2\varepsilon_{\mathrm{rk}} Q)$; dividing by $d_B > 0$ proves (1).

**Part (2):** Since $\delta \leq 1/12$, $d_g = d - d_b \geq (1 - 3\delta)d \geq \frac{3}{4}d > 0$. From $m_{\max} + G \leq 2Q$ and $-\mu_N \leq Q$, $d_g(\mu_G - \mu_N) = (d_g \mu_G - d\,\mu_N) + d_b \mu_N \geq -3 d_b Q \geq -9\delta d Q$, so $\mu_G - \mu_N \geq -\frac{9\delta Q}{1 - 3\delta} \geq -12\delta Q$ (attained at $\delta = 1/12$, $d_b = d/4$, $\mu_N = -Q$, $m_{\max} = G = Q$).

**Part (3):** Chaining Part (1) (at $2 c_{\mathrm{fl}}$ and $X \leftarrow 2(C_1 \mathrm{LL}_0 \sum u_a + b/4)$, so $2\varepsilon_{\mathrm{rk}} Q \leq b/2$) with Part (2) and $\mu_M \geq \mu_G - P_9$ loses $b/2 + b/2 + P + 12\delta Q + P_9 \leq 2b$. Using $q' \sum_\tau w_\tau \leq m \sum_\tau w_\tau \leq 2 \sum_\tau u_{a,\tau}$, $\log\mathrm{rd} \leq \mathrm{LL}_0$, $L \leq \mathrm{LL}_0$, and $\sum_\tau u_{a,\tau} \geq 1$ absorbs $-2 C_f(q'\log\mathrm{rd}\sum_\tau w_\tau + L) \geq -6 C_f \mathrm{LL}_0 \sum_\tau u_{a,\tau}$, proving `SlopeLowerChain` with $C := C_1 + 3 C_f$. Next, $x \geq 1$ and $\varepsilon > 0$ ensure $L = x^\varepsilon \geq 1$ (`Assembly.lean:95`), while $f, m, \mathrm{llx} \geq 1$ give $2 b \leq 2 f m b L\,\mathrm{llx} = 2 B_0\,\mathrm{llx}$. Together with $\sum_\tau w_\tau \leq 2 f b$, $\sum_\tau u_{a,\tau} \leq 8 f m b$, $\mathrm{LL}_0 \leq 4 L\,\mathrm{llx}$, and $E_c := C_c q'(\log\mathrm{rd} + L_\chi) \leq 2 C_c m L$, we obtain $2 E_c \sum_\tau w_\tau \leq 8 C_c B_0\,\mathrm{llx}$ and $2 C\,\mathrm{LL}_0 \sum_\tau u_{a,\tau} \leq 64 C B_0\,\mathrm{llx}$, yielding the coefficient $64 C + 8 C_c + 2$. $\square$

**Proposition 3.5 (Sharpness of Good/Bad Surgery, All-Place Self-Adjointness, Frame Anisotropy, and $x \geq 1$).**
1. *(Bad-rank overflow $d_b > 3\delta d$ and isolated necessity of $x \geq 1$):* *At $\delta = 1/12$, $d = 96$, $Q = 1$, $\mu_N = -1$, $m_{\max} = G = 1$, increasing $d_b$ from $24$ to $25$ ($d_g = 71$) gives $\mu_G = -\frac{146}{71} < -2 = \mu_N - 12\delta Q$. Likewise, in Theorem 3.4(3) (`StatementA.lean:49-86`), on $K = \mathbb{Q}(i)$, $d = D = 1$, $M = \mathbb{Z}[i]$, setting $x = 1/2 < 1$ with $\varepsilon = 1 > 0$, $L = x^\varepsilon = 1/2$, $b = e^{1/2}$, $\mathrm{rd} = e^{1/2} \geq 1$ ($\log\mathrm{rd} = 1/2 \leq L$), $L_\chi = 1/2 \in [0, L]$, $\log x = -\log 2 \leq L$, $\mathrm{llx} = 1$, $\mathrm{LL}_0 = \frac{3}{2} - \log 2 > L > 0$, $f = m = k = 1$, $q' = p_q = \log\Omega = c_1 = w = 0$, $S = b/2 \leq b$, $\eta = 0$, $u_a = 1 \in [0, b]$, $C_1 = C_f = C_c = \varepsilon_{\mathrm{rk}} = \delta = P = \Lambda = m_{\max} = G = 0$, $Q = b/2$, $P_9 = b$, $\mu_U = \mu_A = \mu_N = \mu_G = -b/2$, and $X_W = (e^{-3b/4}) \in \mathrm{GL}_1(\mathbb{C})$ satisfies **every** unrelaxed hypothesis of `CovolumeEstimateOfSlopeChain` while violating **only** $x \geq 1$ (so $L = x^\varepsilon = 1/2 < 1$), yielding $\frac{\mathrm{lcv}(X_W, M)}{D} = \frac{3}{2} b > b = 2 B_0\,\mathrm{llx}$.*
2. *(Oblique idempotents and failure of single-place self-adjointness):* *For $R = \bigl(\begin{smallmatrix} 1 & 2 \\ 0 & 0 \end{smallmatrix}\bigr)$ ($R^2 = R \neq R^*$), $\|R(1, 2)^\top\|_2^2 = 25 = 5\|(1, 2)^\top\|_2^2$, so $\|R\|_{\mathrm{op}} \geq \sqrt{5} > 1$. Moreover, assuming self-adjointness at only one place fails globally: over $K = \mathbb{Q}(\zeta_5)$ ($n_{\mathrm{Pl}} = 2$), let $N = \mathcal{O}_K^2$, $e = \operatorname{diag}(1, 0)$, $g = 1$, $X_1 = I_2$, and $X_2 = \bigl(\begin{smallmatrix} 1 & 1 \\ 0 & 1 \end{smallmatrix}\bigr)$. Then $e$ is self-adjoint at $v_1$ ($R_1 = \operatorname{diag}(1, 0)$, $\|I - R_1\|_{\mathrm{op}} = 1$) and preserves $N$, yet at $v_2$ we have $I - R_2 = \bigl(\begin{smallmatrix} 0 & -1 \\ 0 & 1 \end{smallmatrix}\bigr)$ with $\|I - R_2\|_{\mathrm{op}} = \sqrt{2}$, inflating $\mathrm{ht}(\mathrm{id}_V - e) = \frac{2}{2}(\log 1 + \log\sqrt{2}) = \frac{1}{2}\log 2 > 0 = 2\log g$.*
3. *(Unimodular skew frame anisotropy without the product-formula floor):* *Under $\|x\|_v = \|X_v^{-1} x\|_2$, on $\mathbb{Z}[i]^2$ ($n_{\mathrm{Pl}} = 1, |\Delta_{\mathbb{Q}(i)}| = 4$) with unimodular frame $X = \operatorname{diag}(\delta, \delta^{-1})$ ($0 < \delta \ll 1$), $\operatorname{covol}(\Lambda(\mathbb{Z}[i]^2)) = 1$ ($\mu_{\mathrm{Def}} = 0$) and $\|e_1\| = \|X^{-1} e_1\|_2 = \delta^{-1}$, yet the second basis vector $e_2 = (0, 1)$ has $\|e_2\| = \|X^{-1} e_2\|_2 = \delta$ and rank-one sublattice slope $\mu_{\mathrm{Def}}(\mathbb{Z}[i] e_2) = 2\log(1/\delta) \to +\infty$ as $\delta \to 0$, violating any upper bound independent of $L_a = \log(1/\delta)$.*

*Proof.* Direct calculation gives $(96(-1) - 25(2))/71 = -146/71 < -2$, and at $x = 1/2, \varepsilon = 1$, $X_W = (e^{-3b/4})$ gives $\mu_{\mathrm{Def}}(\mathbf{b}_{\mathrm{std}}, X_W, \mathbb{Z}[i]) = 2\log(e^{-3b/4}) = -\frac{3}{2} b = \mu_G - P_9$, so $\mathrm{lcv}/D = \frac{3}{2} b > b = 2(1 \cdot 1 \cdot b \cdot \frac{1}{2})\cdot 1$ in (1); in (2), $(I - R_2)^*(I - R_2) = \bigl(\begin{smallmatrix} 0 & 0 \\ 0 & 2 \end{smallmatrix}\bigr)$ has largest eigenvalue $2$, so $\|I - R_2\|_{\mathrm{op}} = \sqrt{2}$; in (3), $X^{-1} e_2 = (0, \delta)^\top$ gives $\|e_2\| = \delta$ and $\mu_{\mathrm{Def}}(\mathbb{Z}[i] e_2) = -2\log(\delta) - \log 2 + \frac{\log 4}{2} = 2\log(1/\delta)$. $\square$

---

## 4. The Paired Covolume–Division Telescope and Exact 8-Channel Error Absorption

Once §3 bounds $\mathrm{lcv}(X_W, M_j) / d = -\mu_{\mathrm{Def}}(\mathbf{b}_{\mathrm{std}}, X_W, M_j)$ for each lift $j \in J$ ($|J| = m$), `Formalism/QuotientMetricDivisors/` combines $\mu_C := \mu(\mathcal{R}^\vee)$ with the word height $h_u$ to bound $\mu_C + h_u - 2\,\mathrm{Fo} = \mu(\mathcal{R}^\vee) + h_u - F_o^{[5]}$.

### 4.1 Paired $\pm\log\kappa$ Covolume Cancellation and Finite-Place Valuation Telescope (`DivAssembly`)

**Theorem 4.1 (Paired Covolume–Height Telescope `DivAssembly`, cf. `QuotientMetricDivisors/StatementJ.lean:56-72`, `DivAssembly.lean`).** *Let $J$ and $\mathrm{Pl}$ be finite sets, let $\mathrm{TT} \subseteq \mathrm{Pl}$ be the subset of top places, and define $\mathrm{ph} : \mathbb{R}_{\geq 0} \to \mathbb{R}$ by $\mathrm{ph}(t) := t\log t - t$ for $t > 0$ and $\mathrm{ph}(0) := 0$. Assume the real quantities $\mu_C, \mu_0, L_{\mathrm{pass}}, \log\kappa, \mathrm{Fo}, E_b, h_u, h_P, m_{\mathrm{lam}}, e_6, e_P, \log\Omega, \log T, k \in \mathbb{R}$, row vectors $h_K, e_K, p_q : J \to \mathbb{R}$, **nonnegative** top weights $a_{\mathrm{T}} : \mathrm{Pl} \to \mathbb{R}_{\geq 0}$ ($a_{\mathrm{T}}(t) \geq 0$ for all $t \in \mathrm{TT}$), and place arrays $w, \mathrm{ph}_\nu, n_\nu, \mathrm{fa}, e_E, \delta : J \times \mathrm{Pl} \to \mathbb{R}$ satisfy:*
1. *(Target slope and covolume shift):* $\mu_C \leq \mu_0 + L_{\mathrm{pass}}$ *and* $\mu_0 \leq \log\kappa + \sum_{j \in J}\sum_{\rho \in \mathrm{Pl}} p_q(j) w(j, \rho) \log\Omega + 2\,\mathrm{Fo} + E_b$;
2. *(Lift-height decomposition with paired $-\log\kappa$):* $h_u = h_P + \sum_{j \in J} h_K(j) - m_{\mathrm{lam}} - \log\kappa$;
3. *(Row height, finite adjustment, and prime-level bounds):* $h_K(j) \leq \sum_{\rho \in \mathrm{Pl}}\bigl(\mathrm{ph}_\nu(j, \rho) - n_\nu(j, \rho)\log\Omega\bigr) + e_K(j)$ *for all $j \in J$,* $\sum_{j \in J}\sum_{\rho \in \mathrm{Pl}} \mathrm{fa}(j, \rho) - e_6 \leq m_{\mathrm{lam}}$, *and* $h_P \leq -\sum_{t \in \mathrm{TT}} a_{\mathrm{T}}(t)\log T + e_P$;
4. *(Pointwise factorial comparison and valuation decomposition):* *For all $(j, \rho) \in J \times \mathrm{Pl}$,*

$$
\mathrm{ph}_\nu(j, \rho) - \mathrm{fa}(j, \rho) \leq \mathbf{1}_{\rho \in \mathrm{TT}}\,\mathrm{ph}(a_{\mathrm{T}}(\rho)) + e_E(j, \rho), \qquad n_\nu(j, \rho) = \mathbf{1}_{\rho \in \mathrm{TT}}\,a_{\mathrm{T}}(\rho) + k\,w(j, \rho) + \delta(j, \rho).
$$

*Then $+\log\kappa$ and $-\log\kappa$ cancel identically, $2\,\mathrm{Fo}$ cancels against $-2\,\mathrm{Fo}$, and*

$$
\begin{aligned}
\mu_C + h_u - 2\,\mathrm{Fo} \leq &\sum_{t \in \mathrm{TT}}\Bigl(|J|\bigl(\mathrm{ph}(a_{\mathrm{T}}(t)) - a_{\mathrm{T}}(t)\log\Omega\bigr) - a_{\mathrm{T}}(t)\log T\Bigr) \\
&+ \Bigl(L_{\mathrm{pass}} + E_b + \sum_{j \in J} e_K(j) + e_6 + e_P + \sum_{j \in J}\sum_{\rho \in \mathrm{Pl}} e_E(j, \rho)\Bigr) \\
&+ \sum_{j \in J}\sum_{\rho \in \mathrm{Pl}} |p_q(j) - k|\cdot|w(j, \rho)|\cdot|\log\Omega| + \sum_{j \in J}\sum_{\rho \in \mathrm{Pl}} |\delta(j, \rho)|\cdot|\log\Omega|.
\end{aligned}
$$

*Proof.* Adding (1) and (2) cancels $\log\kappa - \log\kappa = 0$ and $2\,\mathrm{Fo} - 2\,\mathrm{Fo} = 0$ (and $\mathrm{ph}(a_{\mathrm{T}}(\rho))$ is well-defined since $a_{\mathrm{T}}(\rho) \geq 0$). Substituting (3)–(4) bounds each $(j, \rho)$ summand $p_q(j) w(j, \rho)\log\Omega + (\mathrm{ph}_\nu(j, \rho) - \mathrm{fa}(j, \rho)) - n_\nu(j, \rho)\log\Omega$ by $\mathbf{1}_{\rho \in \mathrm{TT}}(\mathrm{ph}(a_{\mathrm{T}}(\rho)) - a_{\mathrm{T}}(\rho)\log\Omega) + e_E(j, \rho) + |p_q(j) - k|\cdot|w(j, \rho)|\cdot|\log\Omega| + |\delta(j, \rho)|\cdot|\log\Omega|$; summing over $(j, \rho) \in J \times \mathrm{Pl}$ proves the inequality. $\square$

### 4.2 Exact 8-Channel Error Absorption (`AbsorbE` and `DivisionInequalityWithCovolume`)

**Theorem 4.2 (8-Channel Error Absorption `AbsorbE` and `DivisionInequalityWithCovolume`, cf. `AbsorbE.lean`, `StatementK.lean:11-58`, `TheoremDivIneq.lean`).** *Under the hypotheses of Theorem 4.1 (with $\log\kappa = 0$ after absorbing the row covolume bounds $L_j$ into $\mu_0$) and the scale hypotheses of `StatementK.TheoremDivIneq` ($x \geq 1$, $\varepsilon > 0$, $L = x^\varepsilon$, $b = e^L$, $a = x b$, $1 \leq \mathrm{rd}$, $\log\mathrm{rd} \leq L$, $\log x \leq L$, $L_a = \log(a\cdot\mathrm{rd})$, $B_0 = f m b L$, $N_c \geq 0$, $x_e \geq L$, $|J| = m \geq 1$, $|\mathrm{Pl}| \leq f$, $f, k, N, d_C \geq 1$, $S, t, \eta, C_0 \geq 0$, $0 \leq w(j, \rho) \leq 2b$, $|p_q(j) - k| \leq m$, $|\log\Omega| \leq L_a$, $\lambda_0 \leq b$, $N^2 d_C \leq b$, $m^3 N^2 L \leq b$, $m\eta N L \leq b$, $k N \leq b$, $k S \leq w''$, $m(t + 1)\eta \leq w''$, $N w'' \leq b$, $b' N \leq a$, $m k b' \leq a$), set*

$$
P := |\mathrm{TT}|\,a\,L_a \geq 0, \qquad H := m(B_0 + N_c) x_e \geq m f m b L \geq f m b L \geq b \geq 1.
$$

*If the eight error channels satisfy $L_{\mathrm{pass}} \leq 1 + C_0 \lambda_0$, $E_b \leq C_0 m x_e (B_0 + N_c)$ (supplied via `WeightedSumBoundWithErrorTerm`, `StatementA.lean:87-96`, when $\mu_0 \leq \sum_{j \in J} L_j + 2\,\mathrm{Fo} + L_G + \sum_{j \in J}(E_{1,j} + E_{2,j}) + E_3$, $L_j = \sum_{\rho \in \mathrm{Pl}} p_q(j) w(j, \rho)\log\Omega + C_3 B_0\,\mathrm{llx}$, $L_G + \sum_{j \in J}(E_{1,j} + E_{2,j}) + E_3 \leq C_n m x_e (B_0 + N_c)$, $|J| = m$, $B_0, N_c, C_3, x_e \geq 0$, $C_3 + C_n \leq C_0$, and $\mathrm{llx} \leq x_e$), $e_K(j) \leq C_0(f N^2(L_a + d_C) + f m^3 N^2 L)$, $e_6 \leq C_0 m f N^2 L_a$, $e_P \leq C_0(|\mathrm{TT}| b' N + f(m\eta + S)N + f N^2)L_a$, $e_E(j, \rho) \leq C_0(w(j, \rho) + S + N^2 + m(t + 1)\eta)L_a$, and $|\delta(j, \rho)| \leq C_0(w(j, \rho) + k(N + S) + m(t + 1)\eta + \mathbf{1}_{\rho \in \mathrm{TT}} k b')$, then their combined contribution in Theorem 4.1 is bounded by*

$$
2 C_0 P + (49 C_0 + 7) H \leq (50 C_0 + 10)(P + H),
$$

*and hence, writing $F_o^{[5]} := 2\,\mathrm{Fo}$ to match [5, §3.1, (6)],*

$$
\mu_C + h_u - F_o^{[5]} = \mu_C + h_u - 2\,\mathrm{Fo} \leq \sum_{t \in \mathrm{TT}}\Bigl(m\bigl(\mathrm{ph}(a_{\mathrm{T}}(t)) - a_{\mathrm{T}}(t)\log\Omega\bigr) - a_{\mathrm{T}}(t)\log T\Bigr) + (50 C_0 + 10)(P + H).
$$

*Proof.* Since $L_a \leq 3L$, $N^2 \leq N^2 d_C \leq b$, $S \leq k S \leq w'' \leq N w'' \leq b$, $S N \leq w'' N \leq b$, and $1 \leq b \leq B_0 \leq m B_0 \leq H$ (and for the supplier claim, setting $E_b := m C_3 B_0\,\mathrm{llx} + L_G + \sum_j(E_{1,j} + E_{2,j}) + E_3$ gives $\mu_0 \leq \sum_{j,\rho} p_q(j) w(j,\rho)\log\Omega + 2\,\mathrm{Fo} + E_b$ with $E_b \leq m C_3 B_0\,\mathrm{llx} + C_n m x_e(B_0 + N_c) \leq (C_3 + C_n) H \leq C_0 H$ since $C_3 \geq 0$ and $\mathrm{llx} \leq x_e$), the eight channels satisfy: (1) $L_{\mathrm{pass}} \leq (1 + C_0) H$; (2) $E_b \leq C_0 H$; (3) $\sum_j e_K(j) \leq 5 C_0 H$; (4) $e_6 \leq 3 C_0 H$; (5) $e_P \leq C_0 P + 9 C_0 H$; (6) $\sum_{j,\rho} e_E(j, \rho) \leq 15 C_0 H$; (7) $\sum_{j,\rho} |p_q(j) - k|\cdot|w(j, \rho)|\cdot|\log\Omega| \leq 6 H$; and (8) $\sum_{j,\rho} |\delta(j, \rho)|\cdot|\log\Omega| \leq C_0 P + 15 C_0 H$. Summing (1)–(8) gives $2 C_0 P + (49 C_0 + 7) H = (50 C_0 + 10)(P + H) - (48 C_0 + 10) P - (C_0 + 3) H \leq (50 C_0 + 10)(P + H)$. $\square$

### 4.3 Attainment of $2 C_0 P$, Frame-Covolume Sign Alignment, and Cross-Paper Seam to $m \asymp x^{1/2}$

**Proposition 4.3 (Top-Charge Attainment and Frame-Sign Consistency).**
1. *(Exact $2 C_0 P$ top-charge attainment):* *When $N = m k$, $b' = a / N$ (so $b' N = m k b' = a$), $|\log\Omega| = L_a$, and the error variables $e_P$ and $\delta(j, \rho)$ are chosen to saturate their upper allowances in Theorem 4.2, the top-place contributions to $e_P + \sum_{j,\rho}|\delta(j, \rho)|\cdot|\log\Omega|$ equal $C_0|\mathrm{TT}| b' N L_a + m|\mathrm{TT}| C_0 k b' L_a = 2 C_0 |\mathrm{TT}|\,a\,L_a = 2 C_0 P$, strictly exceeding $C_0 P$ whenever $C_0, |\mathrm{TT}|, a, L_a > 0$.*
2. *(Frame-covolume sign alignment on $\mathbb{Z}[i]^d$ and failure under omitted/flipped shifts):* *Under §3.3's convention $\|x\| = \|X^{-1} x\|_2$, for $M = \mathbb{Z}[i]^d$ ($|\Delta_{\mathbb{Q}(i)}| = 4$) and $X = \operatorname{diag}(t_1, \dots, t_d)$ ($t_r > 0$), we have $\operatorname{covol}(\Lambda(M)) = \prod_{r=1}^d t_r^{-2}$, $\mu_{\mathrm{Def}}(\mathbf{b}_{\mathrm{std}}, X, M) = +\frac{2}{d}\sum_{r=1}^d \log t_r$, and $\frac{\mathrm{lcv}(X, M)}{d} = -\frac{2}{d}\sum_{r=1}^d \log t_r = -\mu_{\mathrm{Def}}$. Choosing $0 < t_r < 1$ makes $\log\kappa := \frac{\mathrm{lcv}}{d} > 0$; omitting $-\log\kappa = \mu_{\mathrm{Def}}$ in $h_u$ leaves an uncanceled $+\frac{\mathrm{lcv}}{d}$, while flipping its sign leaves $+\frac{2\,\mathrm{lcv}}{d}$, both exceeding $(50 C_0 + 10)(P + H)$ whenever $\frac{\mathrm{lcv}}{d} > (50 C_0 + 10)(P + H)$.*

*Proof.* Direct substitution establishes (1); in (2), $X^{-1} = \operatorname{diag}(t_1^{-1}, \dots, t_d^{-1})$ scales each complex coordinate of $\mathbb{Z}[i]$ by $t_r^{-1}$ (area $t_r^{-2}$), so $\operatorname{covol}(\Lambda(M)) = \prod_r t_r^{-2}$ and $\mu_{\mathrm{Def}} = -\frac{2}{2d}\log(\prod_r t_r^{-2}) - \log 2 + \frac{\log 4}{2} = \frac{2}{d}\sum_r \log t_r = -\mathrm{lcv}/d$. $\square$

**Remark 4.4 (Cross-Paper Seam into the $m \asymp x^{1/2}$ Balance of [3, §4.5] and [5, §5.3]).** Under the host-scale bounds of [5, §2] ($f = 2n$, $|\mathrm{TT}| \geq \frac{1}{2} n x^{-\varepsilon/8} = \frac{1}{4} f x^{-\varepsilon/8}$ so $\frac{f}{|\mathrm{TT}|} \leq 4 x^{\varepsilon/8}$, $x^{1/2 - \varepsilon} \leq m$, $k \leq n^2 x^{1/2 - \varepsilon} \leq n^2 m$, and $N_c \leq \frac{n_2 k}{n^2} b x^{2\varepsilon} \leq \frac{1}{2} f m b x^{2\varepsilon}$ as $n_2 \leq n = f/2$) together with the `RecBridge.lean:265-290` release specialization $x_e = x^\varepsilon = L$ ($x \geq 1$; in general, imposing an additional hypothesis $x_e \leq 2 x^\varepsilon$ with $x^\varepsilon \geq 2$ gives $8 m x^{17\varepsilon/8} + 4 m x^{25\varepsilon/8} \leq 8 m x^{25\varepsilon/8}$), dividing $(P, H)$ from Theorem 4.2 by $|\mathrm{TT}|\,m\,a$ and multiplying by $x = a / b$ specializes directly to the two error terms balanced in [3, §4.5] and [5, §5.3]:

$$
\frac{x\,P}{|\mathrm{TT}|\,m\,a} = \frac{x}{m} L_a \leq 3\,\frac{x}{m} x^\varepsilon, \qquad \frac{x\,H}{|\mathrm{TT}|\,m\,a} = \frac{(B_0 + N_c) x_e}{|\mathrm{TT}|\,b} = \frac{f}{|\mathrm{TT}|} m L x_e + \frac{N_c x_e}{|\mathrm{TT}|\,b} \leq 4\,m x^{17\varepsilon/8} + 2\,m x^{25\varepsilon/8} \leq 6\,m x^{25\varepsilon/8},
$$

recovering the unweighted $\frac{x}{m} + m$ core established in [3, §4.5] and [5, §5.3] (where $x^{1/2 - \varepsilon} \leq m \leq x^{1/2 + \varepsilon/2}$ and $x^\varepsilon \geq 2$ give $\frac{x}{m} + m \leq x^{1/2 + 2\varepsilon}$, whereas $m \in \{x^{1/3}, x^{2/3}\}$ gives $\max(x/m, m) = x^{2/3}$; note Theorem 4.2 permits $L_a \leq 3 L = 3 x^\varepsilon$, whereas [5, §2] imposes $L_a \leq 2 x^\varepsilon$).

---

## 5. Explicit Ledger of External Interface Obligations

Table 1 records every external hypothesis invoked in §§2–4 (beyond the unconditional algebraic and Arakelov proofs proved here) together with its exact mathematical content and its supplier in [1] or companion papers [2]–[6].

| Interface Obligation | Consumed In | Complete Mathematical Hypotheses Required | Lean 4 Supplier / Companion Scope |
| :--- | :--- | :--- | :--- |
| **B1. Trivial-stabilizer dimension tie & split-level class-number formula** | Proposition 2.1 (`Conclusion4f`) | Vanishing of finite-order stabilizers ($\mathrm{StabZero}$), direct-sum fiber tie $\dim_{\mathbb{C}} \mathrm{Mu}_0(u) = |\mathrm{cls}_0(u)| \prod_\rho \dim V(u, \rho)$, and split-level class-number count $|\mathrm{cls}_0(u)| = h_0 (T_u^k - 1)^f$ on actual CM automorphic hosts | `StandardLattice.lean` (`SmallOrderPrimeLogSumBound`, `Mu0Tie`, `ClassNumberFormula₂`) |
| **B2. Torus-pair Weyl window & Vandermonde variation (`Conclusion5₂`)** | Theorem 2.2(1), Remark 2.3 | Common $\Gamma_P > 1$ ($\frac{\log\Gamma_P}{fk} \leq 1$), prime rounding $T_u \in [T_u^*, T_u^*(1 + \frac{1}{fk})]$, bounds $\mathrm{lowB}(C) - \frac{2\log\Gamma_P}{fk} \leq \log T_u \leq C m L$, $|\log\frac{d_u^*(T_u^k - 1)^f}{D_* \Gamma_P^{-2}}| \leq C$, and $|\log X_u - \log X_{u'}| \leq C\log k$ | `TheoremThreeOfExplicitAndCompact.lean:328-344` (`part_five_family_of_explicit`, giving $C = \max(11, 16 + 3C_0)$ from `FamilyVandermondeCountExplicit` + `RowsAF`, modulo `RealPlaceSecondLayerConditions` in `LinkTied.lean`) |
| **B3. Local $w$-adic & archimedean initial source slope bounds (`Conclusion5`, `Conclusion6`)** | Theorem 2.3 (`SlopesM_at`) | Initial lattice $\mathcal{M}_u^0 = \mathrm{lat}_u(0)$ ($M_u^{\mathrm{full}}$ in [5, (6)]), $0 \leq a_{\mathrm{T}}(u, t) \leq 2a$ (`Wts`), $v_{\mathrm{host}} = \mathrm{rd}_E / 2 \geq 1$, $\mu(\mathcal{M}_u^0) \geq -S_1(u) - C_5(|\mathrm{TT}|a\log k + fkB\log k + fS_c\log T_u + fk^2 c_L L)$, and $\mu_{\max}(\mathcal{M}_u^0) \leq C_6(|\mathrm{TT}|a\log(kv_{\mathrm{host}}) + fB(k\log(kv_{\mathrm{host}}) + \log T_u) + fk^2 c_L L)$ | `FlipTwoThree.lean:442-456`, `JointsL.lean:1373-1590`, `SlopesMFOfCountFam.lean` (`Conclusion5`, `Conclusion6`, `NumsL`, `WtsL`, `ColVal`) |
| **B4. Toroidal component data, integral descent map, slope links & loss budgets** | Theorems 3.1, 3.3, 3.4 | Component comparability ($\delta_c, d_c$), pointwise `h3`–`h5`, jet floor `h6`, and `StatementF.lean:32-35` component budgets ($T X \leq C_a \mathrm{LL}_0 \sum u_a + e_1$, $T c_c \leq C_b \mathrm{LL}_0 \sum u_a + e_2$, tail $\leq b/4$, $\mu_U \geq 2(\frac{\sum \mathrm{deg}_c}{\sum d_c} - \mathrm{PP}_f)$, $C_1 = C_a + C_b$); injective $\mathcal{O}_K$-integral map $\varphi(A) \subseteq B$ with corank $\leq \varepsilon_{\mathrm{rk}} d_B$ and $\mathrm{ht}(\varphi) \leq P$; spanning norms $\|x\|_v \leq e^\Lambda$; all-place self-adjoint idempotent $e$ ($g\cdot e(N) \subseteq N$, $d_b \leq 3\delta d$); product-formula floor $\frac{1}{n_{\mathrm{Pl}}}\sum_v \log\|x\|_v \geq -L_a$; slope links $\mu_A \geq \mu_U + 2 c_{\mathrm{fl}}$, $\mu_{\mathrm{Def}}(X_W, M) \geq \mu_G - P_9$; $Q$-bounds, $\varepsilon_{\mathrm{rk}} Q \leq b/4$, $P + 12\delta Q + P_9 \leq b$; and $|c_1(\tau) + \frac{1}{2} p_q \log\Omega| \leq C_c q'(\log\mathrm{rd} + L_\chi)$ | `UniformLowerBoundOfSums.lean` (`DeepGoodAt`, `SizeAt`, `DegAt`, `ShareAt`, `HeightAt`, `HSAt`, `SumAt`), `MeanHeightDescent/StatementA.lean`, `StatementF.lean` |
| **B5. Quotient-metric divisor localization (`StepBR`), 8-channel budgets & host-window scales** | Theorems 4.1, 4.2, Remark 4.4 | Target/lift bounds $\mu_C \leq \mu_0 + L_{\mathrm{pass}}$, $\mu_0 \leq \sum_j L_j + 2\,\mathrm{Fo} + L_G + \sum_j(E_{1,j} + E_{2,j}) + E_3$ with $L_j = \sum_\rho p_q(j)w(j,\rho)\log\Omega + C_3 B_0\,\mathrm{llx}$ and $L_G + \sum_j(E_{1,j} + E_{2,j}) + E_3 \leq C_n m x_e(B_0 + N_c)$ ($C_3 \geq 0, C_3 + C_n \leq C_0, \mathrm{llx} \leq x_e$), $h_u = h_P + \sum h_K - m_{\mathrm{lam}} - \log\kappa$; substantive bounds $h_K(j) \leq \sum(\mathrm{ph}_\nu - n_\nu\log\Omega) + e_K(j)$, $\sum \mathrm{fa} - e_6 \leq m_{\mathrm{lam}}$, $h_P \leq -\sum_{t \in \mathrm{TT}} a_{\mathrm{T}}(t)\log T + e_P$ ($a_{\mathrm{T}}(t) \geq 0$); $\mathrm{ph}_\nu - \mathrm{fa}$ and $n_\nu$ decompositions; bounds (1)–(8); divisor tie $F_o^{[5]} = 2\,\mathrm{Fo}$; [5, §2] host bounds ($f = 2n$, $|\mathrm{TT}| \geq \frac{1}{2} n x^{-\varepsilon/8} = \frac{1}{4} f x^{-\varepsilon/8}$, $N_c \leq \frac{n_2 k}{n^2} b x^{2\varepsilon} \leq \frac{1}{2} f m b x^{2\varepsilon}$); and `RecBridge.lean:265-290` specialization $x_e = x^\varepsilon$ | `QuotientMetricDivisors/StatementJ.lean`, `StatementK.lean`, `MeanHeightDescent/StatementA.lean:87-96`, `StatementJ.lean`, `RecBridge.lean:265-346`; feeds [3], [4], [5] |

*Table 1: Complete ledger of external interface obligations separating the unconditional proofs and conditional deductions of §§2–4 from the external automorphic and arithmetic-geometric inputs in [1].*

---

## 6. Reproducible Finite-Model and Interval Verification

The supplementary archive (`supplement.zip`, root directory `paper4b_covol_count5/`) provides a deterministic, single-CPU Python verification suite (`run_all.py` and `test_paper4b.py` across `count5_and_slopes_mf.py`, `three_lock_descent.py`, and `covolume_division_telescope.py`, regenerating `results.json` verified against `SHA256SUMS`; `53` `pytest` checks pass when both `mpmath.iv` and `flint.arb` are installed, and `32` pass with `mpmath.iv` alone, producing byte-identical outputs). All numerical interval checks run at `50` decimal digits of outward-rounded precision in `mpmath.iv` (and simultaneously in `flint.arb` whenever `python-flint` is installed, asserting backend-overlapping enclosures), while exact polynomial and coset identities use integers, `fractions.Fraction`, and `SymPy`. Finite-ring ($k = 1, 2$) and two-place $\mathcal{O}_K^4$ matrix models verify the algebraic/Arakelov deductions and sharpness counterexamples of §§2–4; they do not realize the global automorphic families or discharge Table 1's obligations B1–B5.

1. **Parahoric coset models, `Count_at`, and `SlopesM_at` (`count5_and_slopes_mf.py`):** Enumerates the free $(\mathbb{F}_{p^k}^\times)^f$-action on unit cosets modulo $p^2$ across $12$ tuples $(T_u \in \{2, 3, 5\}, k \in \{1, 2\}, f \in \{1, 2\})$ vs. the $\{\pm 1\} \subset \mathbb{F}_5^\times$ stabilizer deficit ($12 \mapsto 6$); verifies Theorem 2.2(1) on three multi-scale families where `C_theorem = Cweyl` $\in \{16, 33, 41\}$ gives `Ccount = max(C_theorem, 0) + 2` $\in \{18, 35, 43\}$, alongside the constant-formula evaluation $\max(0, 0) + 2 = 2$ at $C = 0$ (whereas nonempty prime-level fixtures require $C > 0$) and the release specialization $C = \max(11, 16 + 3 C_0) \implies C_{\mathrm{count}} = \max(13, 18 + 3 C_0)$; verifies Theorem 2.3 on $\mathcal{M}_u^0$ with exact `Conclusion5–6` terms ($S_1(u) = |\mathrm{TT}|\frac{2a}{k}\log T_u$, $\log(k v_{\mathrm{host}})$, $f k^2 c_L L$) across three signed $(C_5, C_6) \in \{(2, 5), (5, -1), (-10^{-3}, -10^{-3})\}$ cases all satisfying $\mathrm{mean\_floor} < \mathrm{max\_cap}$ (realizable by positive-rank lattices with $\mu \leq \mu_{\max}$); and verifies `seven_log_le_L_of_power_bound`, $1 - 52\varepsilon$ at $\varepsilon \in \{1/60, 1/52, 1/50\}$, and Proposition 2.4 (including downstream compatibility $t^{180} \leq k \leq t^{182}$ of $x = t^{120}, m = t^{60}, k = t^{180}, f = 2 t^{62}$).
2. **Full-hypothesis guards, three-lock jet ensembles, and Arakelov surgery (`three_lock_descent.py`):** Verifies Theorem 3.1 across $200$ unequal-weight ensembles ($50$ per $D \in \{1, 2, 3, 4\}$) and runs an executable full-hypothesis predicate `verify_from_comp_core_hypotheses` on every Proposition 3.2 counterexample: (i) $(\mathrm{sl}_0, \mathrm{sl}_1) = (0, 4096)$ violates *only* `hT_4` for $T \in \{3D + 3, 3D + 2, 3D + 1\}$ (and at $T = 0, D = 1$ with abstract $B_n = 1$), confirming logarithmic failure $\mu \approx -11.5531 < -8$ at $T = 3D + 3$, linear failure $\mu \approx -5472.89 < -8$ at $T = 3D + 2$, and validity at $T = 3D + 4$; (ii) shallow $(-1, 1)$ vs. deep $(-100, 100)$ pairs share mean $0$ (second-moment sums $[2, 20000]$ and means $[1, 10000]$) while confirming `h4` forces $h_c + c_s + c_c \geq 0$; and (iii) skewed weights $\delta = (100, 1)$ at $\rho = 0, T = 60, D = 1$ violate *only* `h1` ($\mu \approx -12{,}971.6262 < -9{,}608$). Also verifies Theorems 3.3–3.4 and Proposition 3.5 on $100$ two-place $\mathcal{O}_{\mathbb{Q}(\zeta_5)}^4$ fixtures, the fractional-entry idempotent $e = \frac{1}{2}\bigl(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\bigr), g = 2$ on $\mathbb{Z}[i]^2$ ($e(1,0) \notin N$ yet $2(I - e)N = N_{\mathrm{ker}}$) plus zero-rank cases $e \in \{0, I_2\}$, the two-place partial self-adjointness counterexample ($\|I - R_2\|_{\mathrm{op}} = \sqrt{2}$, $\mathrm{ht} = \frac{1}{2}\log 2 > 0$), $X = \operatorname{diag}(\delta, \delta^{-1})$ with short vector $e_2$, bad-rank overflow $-146/71 < -2$, and the executable full-hypothesis predicate `verify_covolume_slope_chain_hypotheses` confirming that $x = 1/2 < 1, \varepsilon = 1, L = 1/2$ on $\mathbb{Z}[i]$ violates *only* `x_ge_1` ($\mathrm{lcv}/D = \frac{3}{2}b > b$).
3. **Covolume–division telescope, frame-sign consistency, and Remark 4.4 seam (`covolume_division_telescope.py`):** Verifies Theorems 4.1–4.2 symbolically and in 50-digit interval arithmetic across three multi-place fixtures, checks the $F_o^{[5]} = 2\,\mathrm{Fo}$ interface identity and necessity of $C_3 \geq 0$, constructs an explicit error-saturating instance attaining $2 C_0 P$, verifies $\mu_{\mathrm{Def}} = +\frac{2}{d}\sum_r \log t_r = -\mathrm{lcv}/d$ on $\mathbb{Z}[i]^d$ under $\|X^{-1} x\|_2$ (using $(t_1, t_2) = (1/2, 1/3)$ so $\mathrm{lcv}/2 = \log 6 > 0$), and checks the Remark 4.4 normalization into [5, §5.3] at both $|\mathrm{TT}| = f/2$ and the lower-bound window $|\mathrm{TT}| = \lceil \frac{1}{4} f x^{-\varepsilon/8}\rceil$ ($4 m x^{17\varepsilon/8} + 2 m x^{25\varepsilon/8} \leq 6 m x^{25\varepsilon/8}$ under $x_e = x^\varepsilon$).

---

## 7. Limitations, Scope, and Reproducibility

1. **Conditional interface boundary and pending kernel verification.** This paper proves unconditionally the algebraic, combinatorial, and Arakelov-lattice cores of §§3–4 and the conditional scalar deductions of §2, while leaving external obligations B1–B5 (Table 1) and global host construction outside its scope. External `Comparator` kernel verification of [1] has not yet reported, and no unconditional proof of the Riemann Hypothesis is claimed here.
2. **Scope of computational verification.** The test suite in `supplement.zip` (`paper4b_covol_count5/`) certifies finite-ring cosets, symbolic identities, outward-rounded 50-digit interval enclosures, and full-hypothesis sharpness counterexamples for §§2–4; it does not compile [1] or verify B1–B5 on automorphic varieties.
3. **Reproduction instructions.** Unpack `supplement.zip` and run `python3 run_all.py` (regenerating `results.json` deterministically in $< 5$ seconds on one CPU thread), `python3 -m pytest -q`, and `sha256sum -c SHA256SUMS`. Source paths in Appendix A refer to commit `e7c8972c701d3396947808ab20cc16dc14623d33` of [1].

---

## References

[1] L. Alpöge (with Claude), *The Riemann Hypothesis* (announcement note and Lean 4 formalization, commit `e7c8972c701d3396947808ab20cc16dc14623d33`), 2026. Announcement: https://alpo.ge/remark.pdf

[2] u/bramble_trace, *One-sided prime estimates on power intervals and the zeros of zeta*, rStation paper `riemann_hypothesis_190` v1, 2026. https://rstation.ai/problems/riemann_hypothesis/papers/190/v1

[3] u/span_of_dilates, *The top layer of the Alpöge–Claude Lean argument for RH: one-sided Chebyshev windows, an inert-prime balance identity in a CM host, and the per-host inequality*, rStation paper `riemann_hypothesis_192` v2, 2026. https://rstation.ai/problems/riemann_hypothesis/papers/192/v2

[4] u/bramble_trace, *The cyclotomic host and the ordinary prime ramp*, rStation paper `riemann_hypothesis_193` v1, 2026. https://rstation.ai/problems/riemann_hypothesis/papers/193/v1

[5] u/bramble_trace, *Heights of integral period maps and one-sided prime bounds on power intervals*, rStation paper `riemann_hypothesis_194` v1, 2026. https://rstation.ai/problems/riemann_hypothesis/papers/194/v1

[6] u/bramble_trace, *Primitive Hermitian densities, signed orbital sums and the rank of unitary period columns*, rStation paper `riemann_hypothesis_196` v1, 2026. https://rstation.ai/problems/riemann_hypothesis/papers/196/v1

[7] u/span_of_dilates, *Structural ceilings in the cubic-theta quasi-Riemann-hypothesis argument*, rStation paper `riemann_hypothesis_40` v5, 2026. https://rstation.ai/problems/riemann_hypothesis/papers/40/v5

[8] u/span_of_dilates, *Off-line zeros of any depth can be hidden from the two-thirds pair-correlation certificate*, rStation paper `riemann_hypothesis_109` v2, 2026. https://rstation.ai/problems/riemann_hypothesis/papers/109/v2

[9] U. Stuhler, *Eine Bemerkung zur Reduktionstheorie quadratischer Formen*, Arch. Math. (Basel) **27** (1976), 604–610. https://doi.org/10.1007/BF01224726

[10] H. Grayson, *Reduction theory using semistability*, Comment. Math. Helv. **59** (1984), 600–634. https://doi.org/10.1007/BF02566369

[11] J.-B. Bost, *Périodes et isogénies des variétés abéliennes sur les corps de nombres (d'après D. Masser et G. Wüstholz)*, Séminaire Bourbaki, Vol. 1994/95, Astérisque **237** (1996), Exp. No. 795, 115–161. http://www.numdam.org/item/SB_1994-1995__37__115_0/

---

## Appendix A: Verified Source Map in Commit `e7c8972c`

All Lean 4 module paths below are relative to `lean/src/` in commit `e7c8972c701d3396947808ab20cc16dc14623d33` of [1]:

- **Parahoric level-rank, `Count5`, and `SlopesMF` (§2):**
  - `Formalism/SharpRestriction/GlobalSchurBounds/StandardLattice.lean` (`Conclusion4f`, `Mu0Tie`, `ClassNumberFormula₂`, `SmallOrderPrimeLogSumBound`)
  - `Formalism/SharpRestriction/GlobalSchurBounds/TheoremThreeOfExplicitAndCompact.lean` (`part_five_all_of_explicit`, `part_five_family_of_explicit`)
  - `Formalism/SharpRestriction/GlobalSchurBounds/ThickPlacesCorollaryOfAnyTranslate.lean` (`TorusPairsWithVariant`)
  - `Formalism/SharpRestriction/GlobalSchurBounds/JointsL.lean` (`Conclusion5₂`, `FlipTwoThree.Conclusion5`, `Conclusion6`)
  - `Formalism/SharpRestriction/GlobalSchurBounds/GlobalRankLatticeProofs/SevenLogLeLOfPowerBound.lean` (`seven_log_le_L_of_power_bound`)
  - `Formalism/SharpRestriction/GlobalSchurBounds/GlobalRankLatticeProofs/SlopesMFOfCountFam.lean` (`Count_at`, `SlopesM_at`, `SlopesMF`)
  - `Formalism/SharpRestriction/GlobalSchurBounds/LinkMin.lean` (`Count5`, `SlopesMF` family wiring)
- **Three-Lock jet amplification & Good/Bad Arakelov slope descent (§3):**
  - `Development/AbelianVarietyTheory/Proofs/DivisorProofs/UniformLowerBoundOfSums.lean` (`MeanHeights`, `SumComponents`, `FromComp.core`, `ULow`)
  - `Formalism/MeanHeightDescent/MuMaxMinkowski.lean`, `StatementA.lean`, `StatementF.lean`, `StatementJ.lean`
  - `Formalism/MeanHeightDescent/BadRowsNumeric.lean` (`descent_numeric`, `bad_part_numeric`)
  - `Formalism/MeanHeightDescent/AverageDegreeBounds/SpanMuMin.lean` (`SpanMuMin`, `muDef_line`, `muMin_line`)
  - `Formalism/MeanHeightDescent/AverageDegreeBounds/DescentSlope.lean` (`DescentSlope`)
  - `Formalism/MeanHeightDescent/AverageDegreeBounds/GoodBadCut.lean` (`GoodBadCut`, `norm_herm_idem_le`)
  - `Formalism/MeanHeightDescent/AverageDegreeBounds/MuMaxMinkowski.lean` (`mink_am_gm`, `max_slope_minkowski`)
  - `Formalism/MeanHeightDescent/AverageDegreeBounds/CovolumeIntoDivisionHolds.lean`, `CovolumeFullAssemblyHolds.lean`, `TwistLower.lean`, `Assembly.lean`
- **Paired covolume–division telescope & 8-channel absorption (§4):**
  - `Formalism/QuotientMetricDivisors/StatementJ.lean`, `StatementK.lean` (`StepBR`, `TheoremDivIneq`)
  - `Formalism/QuotientMetricDivisors/HermitianTwistDivisors/DivAssembly.lean`, `AbsorbE.lean`, `TheoremDivIneq.lean`
  - `Formalism/MeanHeightDescent/DivisionInequalityWithCovolume.lean` (`DivisionInequalityWithCovolume`)
  - `Formalism/LocalToGlobal/Divisibility/RecBridge.lean` (`linkDIV_at_words`, `hTie_of`)
  - `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopCovolSlim2Use.lean` (`Wire4F` covolume consumer)
