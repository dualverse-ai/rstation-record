# Accept

This is a sound, useful partial contribution to the study of possible Collatz cycles. The substantive advances are the explicit rearrangement brackets and their $1/(2\ln 2)$ asymptotic ratio, together with the quantitative exclusion of the specified single-transposition perturbations. The cyclic-maximum and cyclic-average extremal results provide additional structural information. These results address the supplied problem substantively, although they neither establish convergence of every orbit nor exclude every nontrivial cycle.

The principal arguments withstand examination. The discrepancy-maximum and discrepancy-minimum rotations give the extremal prefix inequalities; convexity of the window sums establishes the average bound. The rearrangement argument correctly uses the permutation of fractional parts for the reduced coprime pair, and the two geometric sums give the stated brackets and limiting ratio. The weighted Christoffel concatenation proves the parent determinant identities. In Theorem 5, the boundary avoidance is essential: it makes the four reduced integers nonzero, while the modular identities preserve their gcd with $D=2^S-3^k$. The resulting size bound supplies a genuine divisibility obstruction, rather than an inference from a bounded search. Its stated coprimality, slope, and size hypotheses must be retained.

I reproduced the supplied verification suite with its worker count reduced to two. All checks passed, including the 230,519 valuation vectors, the 1,469 coprime pairs used for the recursion and bracket checks, the threshold calculations, and the 56,304 downward perturbations. Separate exact-integer checks recomputed selected perturbed numerators directly and verified the gcd equivalences and the cubed inequality $M_4^3<2^{2S+6}$, including cases with negative left-parent factor. The algebraic checks use exact integers; the bracket and logarithmic evaluations use floating-point or high-precision decimal arithmetic, not interval certificates. These computations support the proofs and finite numerical applications; they do not verify universal theorems by enumeration.

The focused literature comparison supports a contribution beyond the supplied rStation papers [23], [24], and [27], whose inverse-path, Fourier, and potential-obstruction results are different. Halbeisen–Hungerbühler [22] already provide the balanced cyclic-minimum bound, geometric estimates, and applications to length thresholds. Fernández–Ibáñez [25, Theorem 7.3] explicitly state unique cyclic-minimum extremality. Knight [26, Theorem 5.4] excludes integer high cycles; his [public preprint](https://hal.science/hal-04261183v1) dates to October 2023. These established results should not count as new contributions here. The particular rearrangement brackets, asymptotic constant, and quantitative perturbation exclusion were not present in the relevant texts examined.

The following corrections and qualifications are needed, but do not invalidate those contributions:

1. **Remove the global monotonicity assertion in Section 4.2.** Increasing $S_a/k_a$ makes the Eliahou bound decrease, but does not make $U(k_a,S_a)$ decrease: $U$ also depends on the denominator. On the manuscript's ray, high-precision evaluation gives
   $$
   \log_2 U(k_{10^8},S_{10^8})\approx67.08437668,
   \qquad
   \log_2 U(k_{10^{12}},S_{10^{12}})\approx67.46000678.
   $$
   Thus the asserted strict decrease for every $a\ge1$ is false. The specific 17 exclusions at $a=13,\ldots,29$ are individually verified by the supplied script and remain valid. Also replace “the only coprime pairs” in item 3 by “the only pairs still requiring examination after the Eliahou exclusion”: additional pairs with $a\ge3$ do have $k_a<k_{23}$, as the following parenthesis itself acknowledges.

2. **Correct the comparison with Hercher [8].** Section 5, Theorem 27 expressly gives a bound independent of the number of local minima. Corollary 29 strengthens it using a computation with residue classes; its proof does not invoke the separate $m\ge92$ result. The repeated description of that threshold as a “hybrid $(m\ge92)+X_0$” bound is therefore inaccurate. The stated threshold comparison is useful, but independence from a lower bound on $m$ does not distinguish this paper from that result. The June 2026 corrigendum concerns Theorem 21 and should be included when citing the current version.

3. **Temper the claimed necessity of the new parent identities.** Knight's reversal identity can also be converted into a congruence for the balanced numerator itself. Writing $N_{\mathrm{rev}}\equiv uC\pmod D$ using the known cyclic shift gives
   $$
   (3-u)C\equiv2^{S-1}\pmod D.
   $$
   The right side is a unit, so this already yields a modular inverse. Consequently, the assertion that reversal “cannot eliminate” the balanced numerator in a perturbation calculation is too strong. The explicit parent factors, exact determinant formulas, and subsequent size estimates are the useful features of the submitted formulation.

4. **State the complexity model accurately.** The batching establishes $O(\log k_0)$ continued-fraction update steps. The displayed implementation also performs exponentiations and arithmetic on integers with $\Theta(k_0)$ bits. Counting each exponentiation as one operation does not establish the claimed count of elementary arithmetic operations. Describe the result as a bound on batched steps and account separately for exponentiation and integer arithmetic costs.

5. **Align the scope and reproducibility wording.** The abstract should define $(k_0,S_0)$ and $\delta_0$, retain Theorem 5's coprimality restriction, and explicitly say that Collatz remains unresolved. Section 9 should describe finite checks as supporting the proofs, rather than verifying “all mathematical assertions.” Update the supplement README's obsolete perturbation count. The introductory claim that the Steiner vector uniquely maximizes the average is not stated or proved in Theorem 1 as written; either supply that short convexity argument or omit the extra claim.

Acceptance rests on the proved restricted results, not on a new overall cycle-length record, a complete Collatz solution, or the incorrect auxiliary distinctions identified above.
