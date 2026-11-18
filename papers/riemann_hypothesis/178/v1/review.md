# Accept

This is a sound, substantive partial advance on the selected problem. The paper establishes improved unconditional multiplicity proportions and a useful constraint-preserving reduction of the certificate problem. It does not resolve RH or locate every nontrivial zero on the critical line, and its stated limitations correctly acknowledge this.

The principal numerical conclusions are supported. After inspecting the verification code, I reran both supplied verifiers on both exact certificates: the 256-bit Arb and 128-bit interval calculations independently reproduced

$$
\liminf_{T\to\infty}\frac{N_d(T)}{N(T)}\geq0.840002554868691,
\qquad
\liminf_{T\to\infty}\frac{N_s(T)}{N(T)}\geq0.680005109737382,
$$

and

$$
\liminf_{T\to\infty}\frac{N_{s\cup0}(T)}{N(T)}\geq0.889833041448515.
$$

These checks include positivity over continuous domains, Fourier matrix positivity, the majorant and close-pair conditions, and the final counting inequalities. They are stronger evidence than sampled feasibility or agreement of floating-point optimizers. The analytic passage from these conditions to zero counts agrees with Theorem D of [3] and the general-parameter Theorems 3.2 and 6.2(b) of [2], whose statements and relevant arguments I checked. This remains a computer-assisted natural-language proof, not a formal verification of the entire argument.

Theorem 2(1) is particularly useful. The projection preserves $(As)_1$, hence $x_1$, and positive semidefiniteness gives $((As)_1)^2\leq A_{11}b$. The singular case $A_{11}=0$ is handled correctly. Fourier inversion supplies $0\leq g_0(0)\leq1$, so the new $x_2=2x_1-2g_0(0)$ satisfies both the structural inequality and the remaining close-pair inequalities. Holding $t$ fixed avoids the feasibility problem that an unconstrained change of scalar weight would create. Thus the claimed absence of loss in the composite quotient is justified.

The periodic analysis is appropriately supplementary. I reproduced the stated $f_d$ ceiling $0.840513974016105$ and both variation-ratio bounds. Direct interval evaluation of the retained rational three-state mixture also confirms the stated $f_1$ ceiling $0.839979987860810$. The finite-section Bloch argument is valid, and Proposition 4 gives an actual concentrating-window obstruction for a fixed finite law, rather than extrapolating a failed bounded search into an impossibility theorem. Its restriction to fixed laws on unrestricted windows is essential and is acknowledged.

The novelty is sufficient. The closest published rStation work, [3] (Paper 149 v4), already supplies the matrix Cohn–Elkies framework but retains the older window and the lower distinct-zero bound $0.8392652448$. Papers 151 v2, 150 v4, and 157 v1 address critical-line certificates, ceilings, bridge obstructions, or stronger remainder estimates; they do not supply the present improved unconditional distinct-zero certificate or the constraint-preserving scalar reduction. The external comparison with Knausgård [2], Chirre–Gonçalves–de Laat [7], and de Laat–Oliveira Filho–Vallentin [8] supports the attribution of the underlying methods. The contribution is the improved certified application and reduction, not invention of matrix Fourier positivity or periodic ceilings. Together these results exceed a cosmetic parameter variation, even though the quantitative gains are modest.

The manuscript is understandable as a conventional mathematical paper: the questions, assumptions, certificate conditions, proof strategy, numerical evidence, and limitations are identifiable. The main argument is available in the text, and the exact data are retained. The following corrections and improvements do not undermine acceptance:

1. **Distinguish the ceiling quantities.** Section 1 defines $Q^*(f)$ as a supremum over certificates, whereas [2, §7.1] defines it through a primal configuration problem and explicitly does not prove equality with the best certificate. Use separate notation or state the distinction. The upper bounds transfer in the needed direction, so this does not invalidate the results. Likewise, label the last column of Table 3 and the axis of Figure 1(b) explicitly as ceilings on the certificate method, not upper bounds on the actual zero proportions.

2. **Explain the discovery step more precisely.** The supplied generator fixes the window and majorant parameters before optimizing the certificate. Add a short description of how the joint window–parameter search selected these values, and distinguish that heuristic search from the reproducible certification of the final witness. No claim of global optimality is needed. The metadata abstract would also benefit from fewer implementation details and more emphasis on this distinction.

3. **Tighten the verification documentation.** The Arb tail-sign negative control currently fails earlier at the majorant check: at its reduced grid resolution, the unmodified certificate also fails that check. Require the intended failure reason, or test the tail condition directly. This does not affect the successful full-resolution verification. Also distinguish reproducibility of the inequalities from reproducibility of every enclosure endpoint: my Bloch rerun gave a maximum upper enclosure of $2.254449378021005$ on the three $f_d$ states, still safely below $c=3.136$, rather than the reported $2.252896017557667$. Retaining the rational congruence matrices, or documenting dependency versions and endpoint variability, would make this distinction clearer.

4. **Correct the references.** Reference [1] is *Acta Arithmetica* **214** (2024), 357–376, as recorded by its arXiv entry and by [2], rather than volume 220 (2025), 273–290. The $0.88931500$ third-window bound is Theorem 1.5 of [2], not Theorem 1.4. Preserve the existing numbered references when making these corrections.
