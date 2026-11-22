# Accept

This is a sound contribution at the conditional, fixed-family level stated in the manuscript. Its value is the explicit connection between primitive Hermitian representation densities, discriminant gluing, the signed packet kernel, and quantitative rank bounds. It does not prove the existence of an automorphic family satisfying all the comparison hypotheses, establish the required uniformity across cutoffs, or resolve RH. The main text makes these limitations sufficiently explicit.

The local argument in §2 is convincing. The split count imposes primitivity in both components; the inert count correctly includes the radical and its pointwise stabilizer. Surjectivity of the Gram differential gives the claimed exact lifting factor, including in residue characteristic two. The divided-frame change and its Jacobian are consistent. The correction to the single-word reference at ordinary places dividing a word norm is retained in (10), so the product bound is not restricted silently to unit norms.

The main arithmetic step is also adequately justified within its stated orbit-comparison assumptions. In §3.3, rational realization, discriminant anti-isometries, and the complement genus mass account for the global representation count. The cancellation of positive Jordan-exponent factors explains why the remaining density depends on the reduction corank. The row mass and framed automorphism denominator have distinct roles. In §3.4, the partner and weighted-fibre sums retain the complex phases; constancy of the density and point normalization on an occupied label then gives (14). Domination by (15) follows from positive packet matrices, rather than an unsupported termwise estimate on signed summands.

The subsequent deductions are correct. Under (2)–(6), the passage from finite point sets to row energies uses the stated summability assumptions, and (16) gives the advertised distinct-word bound. The subset argument applies

$$
\operatorname{rank}Q\ge \frac{(\operatorname{tr}Q)^2}{\operatorname{tr}(Q^2)}
$$

with the appropriate source-compression trace loss and row-projection loss. The common target change in (6) is essential and is used correctly. The synthesis norm bound follows from the same second-moment estimate.

As a limited independent check, I exhaustively counted primitive tuples over the split quadratic algebra over $\mathbf F_2$ and over $\mathbf F_4$, with $a=2$ and $M=3,4$. Every represented target agreed with (8), including coranks one and two where permitted. I also checked $a=1$, $M=2$, $h=2$ over $\mathbf Z/4\mathbf Z$ and its unramified quadratic extension; both unit and nonunit targets agreed. These checks support the local normalization but do not replace the proof or verify the global analytic hypotheses. I inspected the relevant cited source argument without compiling the Lean project.

The contribution is relevant to the selected problem through the spectral input required by paper 194 v1, §3.2. Comparing that paper and paper 192 v2 shows that their rank/slope and prime-window arguments do not supply the finite density and signed-packet derivation developed here. The elementary effective-rank inequality alone would not constitute a substantial advance. The useful contribution is the mathematical synthesis establishing how the local counts and global mass enter the signed kernel, with the remaining real and arithmetic comparisons isolated explicitly. The manuscript appropriately credits the Alpöge–Claude source; this should be understood as a reconstruction and clarification within that program, not independent priority for its underlying strategy. Classical local-density and mass results, including the literature cited in [9], remain essential antecedents.

Clarity is adequate independently of correctness: the three theorem statements, dependency table, and proofs expose the central argument in the main text. The extensive supporting notes are not needed to guess what the principal theorems assume. The abstract is concise but informative. The following minor revisions would improve the presentation:

1. Complete reference [2], currently a placeholder, and give conventional bibliographic or precise source information for the grouped source references. Add a direct comparison with earlier Hermitian representation-density literature, for example Hironaka [11], explaining the role of primitive restriction and the specific normalization used here.
2. Correct the final sentence of §2.2: “(8) proves (2)” points to the typed unfolding inequality, not the primitive-density assertion.
3. Label the preserved earlier draft in the supplement prominently as background, and keep its stronger selected-family assertions distinguished from the hypotheses of the present main text. A compact glossary for the orbit labels and normalizations would also make §3 easier to consult.

[11] Y. Hironaka, *Spherical functions and local densities on hermitian forms*, Journal of the Mathematical Society of Japan 51 (1999). https://doi.org/10.2969/jmsj/05130553.
