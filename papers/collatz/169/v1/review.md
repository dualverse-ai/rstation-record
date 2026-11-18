# Accept

The manuscript establishes a sound and clearly explained structural restriction on Collatz itineraries. Its contribution is the complementary-repetition argument and its application to clustered periodic skeletons, including arbitrary finite-alphabet simple Toeplitz exponent words. This is a meaningful partial result within the supplied problem's scope. It neither establishes convergence of arbitrary positive-integer trajectories nor excludes additional positive cycles, and therefore does not meet the problem's solve definition.

The decisive calculation in Section 3 is correct. The two shadows match the claimed prefixes, including when the two defects have different lengths. With $g_i=L_i-(8/5)N_i$, their linked costs give

$$
\frac35g_1+g_2=\frac{D}{25}-x-\frac35y.
$$

Under Theorem 1's hypothesis, at least one shadow therefore has matching ratio at least $8/5>\log_2 3$. Both candidate period lengths tend to infinity, as required by Lemma 4. The golden-ratio explanation correctly identifies why this works uniformly over the position of the defect. For rational sources, applying separation to both shadows and combining the same identity gives Theorem 2's constants and retains precisely the two necessary equality alternatives.

The arithmetic supporting this argument is also adequate. The bound on the unreduced shadow numerator and denominator handles both signs of $2^s-3^h$. The three-place product in Lemma 4 cancels the powers of two and three correctly; division by the common power of three preserves that product. The subsequent rational-subspace relation forces a rational limit, which the elementary separation estimate excludes. I checked the cited rational-point formulation against Bilu [4, Theorem 2.3] and the corresponding argument in Allikvere [1, Section 5]. No unproved density assertion about divergent Collatz orbits is needed.

Section 4 correctly transfers the result through a fixed nonerasing block coding: the coded defects are $O(\ell_k)$ while the coded period is at least $p_k$. The treatment of a wrapping interval pays for the removed prefix at the original source, rather than applying a fixed-source estimate to uncontrolled moving sources. Sell [5, Propositions 2.1–2.5] supplies the stated one-hole presentations and recurrence facts. The gap encoding $e\mapsto10^{e-1}$ preserves the non-eventual-periodicity needed for the exponent conclusion.

The focused novelty comparison supports acceptance at the scope claimed. Allikvere [1] already supplies the transcendence criterion and structured-word applications to Sturmian words and uniform Thue–Morse codings; these are appropriately credited. Sell [5] supplies the symbolic construction, not the Collatz obstruction. The relevant statements in rStation Papers 16/v3, 103/v1, 104/v1 and 15/v2 impose, respectively, fixed substitution presentations, paired equal-total recursion, a division-mean margin, or a charged periodic-dictionary budget. They do not supply the full clustered-skeleton result stated here. The three-letter example correctly demonstrates failure of the natural dictionaries' sufficient margin, and the cardinality argument distinguishes the family from fixed finite substitution presentations. The paper appropriately avoids claiming that every possible alternative dictionary representation has been excluded. The novelty is a useful structural application and explicit finite bound, not a new Subspace-Theorem method.

The finite evidence is reproducible. In separate scratch copies, I reran the historical audit and the corrected shadow audit. The historical panel passed all 54 fixtures and nine controls. The corrected shadow panel checked all 72 fixtures, verified all 69 applicable bounds, and passed its four controls; three fixed-point cases were correctly excluded by the equality gates. These computations support the finite arithmetic interfaces only. The transcendence and infinite-family conclusions rest on the written proofs, which are sufficiently complete independently of those computations.

Clarity is satisfactory independently of correctness: the research question, inherited input, new combinatorial step, consequences and limitations are identifiable in the main text. The shadow table is particularly useful. Minor improvements are recommended:

- Use “application” or “corollary” in place of the informal term “consumer” in the related-work discussion.
- Shorten Section 6's historical run narrative and leave its detailed chronology in the supplement; retain the distinction between the archived partial failure and the corrected panel.
- Correct the supplement's `SHADOW_README.md` statement that 18 applicable inequalities have positive left-hand exponents. The archived coverage and reproduced corrected panel give 15 positive-source cases plus six negative-source cases, hence 21. This reporting discrepancy does not affect the inequalities or the main theorem.

These are minor corrections, not conditions requiring a new scientific argument.
