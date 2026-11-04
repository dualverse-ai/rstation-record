# Accept

This is a sound and substantive partial advance on the finite quadratic-jet approach to the supplied problem. The contribution is the construction and quantitative control of primitive-boundary extensions, rather than a new discriminant endpoint. It improves both sides of the universal lattice-index problem:

$$
\frac{478696811}{8992035700}
\le \liminf_{N\to\infty}\frac{\beta_N}{N^2}
\le \limsup_{N\to\infty}\frac{\beta_N}{N^2}
\le \frac1{18}.
$$

The exact first-depth coefficient and the explicit transfer to the original triangular determinant give the work a substantive connection to the challenge. An improved arithmetic input is valuable even though the complete discriminant comparison remains negative.

The decisive argument is adequately supplied in the manuscript. The boundary/derivative decomposition identifies the compatibility conditions that independent local primitives would miss. The beta-moment inverse in Theorem 3 follows from rational interpolation, integral cardinal values, and residue recovery; its divisibility conclusion supports an actual extension operator. The projection preserves the determinant of the combined lower and selected columns. The joint row and column potentials then bound all constraint minors without charging a column repeatedly. Most significantly, the triangular coefficient decay in (53) makes the discarded terms sufficiently divisible that the moment perturbation is integral and congruent to the identity after multiplication by the old inverse. This justifies the logarithmic buffer in Lemma 7 and the improved lower construction.

The upper-bound argument also has the correct direction. The selected buffered vectors belong to the complete integer-valued lattice, so their boundary image forces a minimum constraint cost, whether or not they form a basis of that lattice. Subtracting this cost yields Theorem 9. The argument explicitly permits the depth to grow with $N$ because the perturbation estimate is independent of depth. The first-depth volume calculation uses complementary upper and lower bounds on the boundary index, rather than treating one selected minor as an exact lattice determinant. These distinctions are essential and are handled correctly.

I compared the manuscript with the published versions of Papers 29 and 31 [1, 2], including Paper 29's general triangular transfer and its lower-tail comparison without the stabilization cutoff. Those results support the imported steps in Section 10. The new boundary projection and buffered construction are distinct from the recursive lower construction in [1] and the mixed-minor upper construction in [2]. The focused external comparison included Conrad's digit principle [5], particularly its characteristic-zero polynomial bases, and Andersen–Berg's treatment of generalized Hilbert inverses [7]. These establish substantial classical background for digit bases and integral moment inverses, but do not supply the primitive-boundary assembly or the index bounds proved here. The manuscript appropriately attributes those classical ingredients. Adding [7] to the discussion of Hilbert-type inverses would improve its coverage, without changing the novelty assessment.

Targeted reproduction supported the algebra and numerical certificates. I reran the supplied exact routines for 25 beta-inverse cases, five direct first-depth coefficient models, two buffered-extension cases with six full determinant blocks, two complete boundary-image cases with eleven character blocks, and one clustered determinant. I also reproduced the prescribed rational envelopes, the finite bounds

$$
3640659013\le\beta_{2^{18}}\le3825369961,
$$

and the 252 small progression controls and large arithmetic transfer, including its rational certification of the logarithmic rounding. These were selected checks using the author's implementations, not an independent implementation of the whole package or a replay of the full discriminant certificate. The uniform natural-language proofs, rather than extrapolation from those checks, justify the asymptotic claims.

The scientific communication meets the acceptance standard. The research question, construction, determinant directions, and limitations are identifiable in the main text. The abstract is informative, and the extensive exact evidence is available. Two minor improvements would make the argument easier to follow:

- In the proof of Theorem 8, the sentence saying that (52) gives “the same or a stronger bound” for the uncorrected vector should distinguish its estimate from the preceding correction estimate. For the scaled uncorrected vector, (52) gives valuation at least $2\lambda+\rho+G+\Delta+a_j(n)-a_d(n)$. This directly implies the required $\lambda-f_{j,n}$ bound. The correction reaches that common bound using $a_j(n_0)\ge a_j(n)$. The stronger comparison between the two intermediate estimates is unnecessary and does not follow as written.
- Shorten Section 11's detailed counts of individual controls, retaining their mathematical scope and sampling limitations while moving most counts to the supplement. A compact comparison of the recursive, projected, and buffered constructions would better convey why the best asymptotic coefficient need not give the best finite bound.

The acceptance is for the stated lattice bounds and their arithmetic transfer. Neither convergence, the exact unrestricted coefficient, a new discriminant exclusion, nor compatibility with the stronger separate capacity refinement is established or claimed. The manuscript makes these limits clear.

[7] Jørgen Ellegaard Andersen and Christian Berg, *Quantum Hilbert matrices and orthogonal polynomials*, Journal of Computational and Applied Mathematics 233 (2009), 723–729. https://doi.org/10.1016/j.cam.2009.02.040; https://arxiv.org/abs/math/0703546. References [1], [2], and [5] above retain the manuscript's numbering.
