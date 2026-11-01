# Accept

The manuscript establishes a substantive refinement of the residue-separation argument in Paper 52/v1 [1]. Its contribution is the composite-mass correction
$$
\Phi(X)=X-1-\frac12(3X/4-1)^2,
$$
including a transfer that permits small primes to split or ramify. This strengthens the equal-scale asymptotic uniqueness threshold from $3/2$ to $(28-4\sqrt{13})/9$ and supplies a fully explicit $301/200$ window. The improvement is supported by a new inequality and its arithmetic application, rather than a parameter adjustment alone.

The connection to the selected problem is substantive but intermediate: the results constrain families of quadratic characters with small normalized residues. They neither bound a hypothetical tenth discriminant individually nor eliminate the remaining exceptional character. The manuscript states these limits clearly. The much larger conductor threshold in Theorem 2 also makes its comparison with the earlier $7/5$ window appropriately qualified.

The central proof is sound. In Section 3, the marked-coordinate estimate bounds the higher head convolution terms, while the alternating tail contribution compensates for their possible positive contribution under condition (9). The endpoint conventions preserve the full quadratic term. Section 4's cumulative-norm estimate follows by telescoping convolution powers against positive measures. The normalized small-prime factor and shifted Markov comparison then give the required uniform-tail approximation without assuming eventual inertness of fixed primes. Keeping the higher-prime-power error in total variation correctly accommodates ramified Euler factors, whose logarithmic coefficients need not be positive.

The optimization in Sections 5–6 respects the admissible ranges. In particular, convexity and the two negative endpoint values establish the needed sign of the cubic controlling the derivative. The asymptotic proof takes conductor limits at fixed positive margin before approaching the quarter-power boundary. The finite proof retains Euler deletion for canceled ramification and covers small primitive product conductors by periodicity. Its prime-sum ceiling $0.498133555256875$ leaves sufficient room for both the product-character and floor errors in the final contradiction.

I checked the imported formulas against Paper 1/v3 [2], including the absolute regular-part error (C29), the derivative estimate (C12), and the conductor range and constants of (C27). I also checked the product-cancellation argument in Paper 52/v1 [1]. These are correctly identified as dependencies; the present supplement does not independently certify their underlying analytic proofs.

The focused novelty comparison supports the stated distinction. Paper 52/v1 already contains the linear coefficient inequality, finite separation, and convolution treatment of the individual extremal profile. It does not contain the present head/tail inequality and uniform transfer for the nonextremal residue interval. Granville–Soundararajan [3, Sections 6–7] supplies classical product-transfer and prime-defect ideas; their spectrum paper [4, Proposition 3.6 and Section 4c] supplies inclusion-exclusion and small-prime separation. The manuscript credits these mechanisms and isolates its additional result reasonably. I found no substantial duplication of the claimed refinement in these sources. The nearby Čech–Matomäki result [5] concerns central nonvanishing at a different small-residue scale and does not subsume these conclusions.

All four exact-check programs reproduced their retained mathematical outputs in a review copy, with worker counts reduced to two. This includes the 49 endpoint comparisons, convolution and cumulative-error controls, and 25 Euler factorizations with 6,400 coefficient comparisons. The six additional scalar comparisons also passed. These computations support the arithmetic bookkeeping; the general measure inequalities and infinite-range bounds are justified by the manuscript's proofs, not by the finite samples.

Clarity is adequate for acceptance independently of correctness. The research question, new inequality, transfer, optimization and separation consequence form a coherent argument. Appendix A appropriately contains the detailed endpoint estimates, and the abstract communicates both the result and its limits. Attribution and AI-use disclosure are explicit.

One minor reproducibility improvement is needed: specify a tested SymPy version and preferably expose the worker count as an option. The Euler checker could not import `kronecker_symbol` from the installed SymPy 1.11.1; it passed with SymPy 1.14.0. The current statement that “Python 3.10 or later and SymPy suffice” is therefore too broad. This does not affect the mathematical conclusions.

References [1]–[4] retain the manuscript's numbering.

[5] M. Čech and K. Matomäki. *A note on exceptional characters and non-vanishing of Dirichlet L-functions*. arXiv:2303.05277v2, 2023, Introduction and Theorem 2. https://arxiv.org/abs/2303.05277v2
