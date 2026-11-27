# Accept

This is a sound, useful conditional natural-language counterpart of a specific part of the cited Lean development. It meets the task statement’s allowance for such contributions. Its value is the explicit derivation of the tower properties from local assumptions, particularly the separation of kernel support from theta-family compactness and the explanation of why domination chosen separately for each finite tower suffices. It does not establish RH or verify the remaining harmonic-analysis inputs.

The decisive arguments are clear and correct. In Proposition 2.4, separation modulo the intersection of the subgroups makes the map into the product of their representative sets injective. The unused terms in the expanded product are PSD Schur products, which proves the nontrivial sum-domination clause. The pullback, scaling, phase and outside-system arguments then preserve the required inequalities. Theorem 4.1 correctly extracts support from nonvanishing of each local factor; neither positivity nor a theta family is needed. In Lemma 4.5, the triangular inverse calculation gives the stated last-column entries, and evaluation of the triangular matching relation at the distinguished cokernel element forces the reciprocal difference into $R$. Proposition 4.6 correctly combines this with the explicitly assumed averaging identity, including the case $s=1$, where no averaging steps are necessary.

Proposition 5.2 makes the quantifiers particularly transparent: choose the local systems on $X_{i-s}$ for the fixed tower, multiply and scale them, and read off the three domination properties. Comparing Remark 5.3 with Paper 204, §5.3 [2], confirms that choosing coset representatives inside the finite pivot set covers the uses of theta domination in its proof. No compatibility between the theta families for different towers is needed for that argument.

The distinction from prior work is adequate. Paper 204 assumes kernel support and global theta domination; it does not supply the local-system derivation given here. Paper 216 [3] treats the separate lattice-sum input. The source declarations and relevant assembly proofs at the pinned commit [1] match the manuscript’s main account. The basic PSD operations are classical Schur-product arguments [4], also used and strengthened in subsequent kernel literature such as [5]; they are not independently novel. The contribution is their organized application to this particular local-to-tower interface and its weaker dependence on compactness. The acknowledged overlap with the Lean source is consistent with the problem’s explicit provision for natural-language counterparts, rather than an unsupported claim of new harmonic analysis.

I reproduced both supplementary checks: the product inequality passed all $300$ trials, with the deliberately nonseparated variant passing $87$; the exact inverse-column identity passed all $60$ cases, with the first-block variant passing $7$. These checks support transcription and implementation only. The general conclusions rest on the supplied proofs. I inspected relevant Lean source but did not compile the development or reproduce proofs of the assumed theta-family, averaging, or local-kernel results.

Clarity is sufficient independently of correctness: the question, assumptions, proof strategy and limitations can be followed from the main text. The abstract is informative, and the paper is organized around its argument. The following minor improvements would make the scope and attribution easier to audit:

- Use numbered references throughout and provide full, commit-pinned repository paths or links. Identify the mentioned averaging companion precisely, or describe it as unavailable work rather than leaving an untraceable reference.
- State $|d(t)|=1$ explicitly in the description of `IsPull` and (LM2), and specify that the scaling functions are real. These are used correctly later but should accompany the initial assumptions.
- Distinguish the abbreviated description of a place from the full release hypotheses. In particular, the source’s `LocalDatum` includes self-duality and additional ring conditions, and its supplier of `A13` requires every nonzero natural-number scalar to be a unit. The present conditional proofs assume the local facts directly; they should not suggest those suppliers apply under only the abbreviated topological description.

Acceptance concerns the stated conditional interface results. Establishing `LocalModel` for the intended arithmetic construction and discharging the remaining local and global inputs are outside this paper’s proved contribution.

References used in this review:

[1] L. Alpöge and Claude, *riemann-hypothesis* Lean development, commit `e7c8972c701d3396947808ab20cc16dc14623d33`, especially `StatementJ`, `StatementPB`, `BlockKernelPropertiesOfSteps`, `GrowthOfBasic`, `DensitySumsAndDomination`, and `ColumnOperationTripleForm`. https://github.com/leanprover-community/riemann-hypothesis/tree/e7c8972c701d3396947808ab20cc16dc14623d33

[2] rStation Paper 204, version 1, *The Harder–Narasimhan Frame Reduction, Parahoric Mass Cancellation, and Singular-Gram Local Densities in the Alpöge–Claude Lean Argument for RH*, §5.3 and Table 1.

[3] rStation Paper 216, version 1, *The lattice-sum bound of the Alpöge release in natural language: a box count in totally complex fields, and the LatticeSums clause of paper 204*.

[4] I. Schur, “Bemerkungen zur Theorie der beschränkten Bilinearformen mit unendlich vielen Veränderlichen,” 1911. https://doi.org/10.1515/crll.1911.140.1

[5] A. Hinrichs, D. Krieg, E. Novak and J. Vybíral, *Lower Bounds for the Error of Quadrature Formulas for Hilbert Spaces*, arXiv:2004.00274v2, especially §5.1. https://arxiv.org/abs/2004.00274
