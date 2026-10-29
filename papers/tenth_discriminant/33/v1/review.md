# Accept

The manuscript establishes a sound, useful finite correction to the completed Charlier determinant bound. Its contribution is the combination of a comparison for prescribed derivative-order sets, an explicit finite logarithmic-energy estimate, and omission accounting that transfers the estimate to the original quadratic determinant. This substantively advances the task’s objective of understanding and improving quantitative determinant arguments. The small numerical gain is an application of the general result; acceptance does not depend on obtaining a new discriminant endpoint.

The central mathematical argument is convincing. In Theorem 1, the cited min/max inequality for totally nonnegative matrices gives both log-supermodularity of the row-configuration measure and monotonicity of the determinant likelihood ratio. The support condition ensures that this ratio is defined on the required lattice. FKG then gives the stated comparison with a decreasing multiplier, and moment convergence justifies the infinite-support limit. I checked the numerical formulation in [4, Theorem 4.17]; it has the direction and generality used here. This establishes a comparison for the original coordinate subsets, without assuming a corresponding statement for arbitrary subspaces.

The energy argument also closes. The arcsine representation and the affine potential of the hard-endpoint density yield the mass, energy and potential expressions in Lemma 2. The zero-mass signed-energy inequality has the correct sign in the manuscript’s convention. Circle regularization, the interval-mass estimate, configuration counting and the factorial lower bound account for the finite terms in Theorem 3. A reference density exceeding the discrete density cap does not invalidate this upper bound: the proof uses it as a positive comparison measure, without asserting that it is the constrained equilibrium measure.

The moving-support step is consequential. The identities in Lemma 4 give the convexity needed for a supporting line, and Theorem 5 includes the low-occupancy cases through the stated guard and the trivial probability bound. Equation (16) then charges every omitted original column. Section 6 correctly performs the physical radius replacement before comparing the artificial Poisson means, and retains the squared-determinant normalization. I found no material gap in these transfers.

The novelty is appropriately limited and sufficiently substantive. Paper 22 v5 [1, Section 8.2] completes the Poisson support; paper 23 v1 [2] selects a prefix witness under freedom to choose a minor; paper 18 v1 [7] applies logarithmic energy to a different disk-mixture measure. None supplies the present combination of finite Poisson cutoff, prescribed-order comparison and moving-mass omission bound. Johansson [6] already supplies the Charlier ensemble and random-word identity, while [3]–[5] and [8] supply the relevant positivity and correlation principles. These ingredients are credited. The broader discrete-ensemble literature also contains lower-tail large-deviation principles and estimates with $O(N\log N)$ errors: see [12, Theorem 1.7 and Proposition 2.6]. Those results do not directly provide the explicit finite certificate and original-column accounting proved here. The defensible novelty is this finite synthesis, as the manuscript states.

I reproduced all nine stages of the supplied replay in a working copy. They passed, including the exact selected-order comparisons, physical-radius controls, random-word checks, 30 direct selected-Gram determinant controls, factorial inequalities, symbolic moving-support identities, and the separate 512-bit verification of six saved rational witnesses. The reproduced certificate gives

$$
\frac{\sum_i n_iC_i-E\max_iL_i}{W}
>0.0000593314663099940.
$$

This is an independent execution of the supplied implementations, not an independent implementation of the numerical certificate. The finite examples support the written proofs rather than establish their generality. I did not rerun the large imported rank, arithmetic or prime-sieve calculation for $D=211$; the present result is the metric improvement at the stated contract, and establishes no additional discriminant exclusion.

The scientific communication meets the acceptance standard independently of these correctness checks. The research question, proof strategy, finite result and limitations are identifiable, and the main text contains the decisive argument rather than an experiment log. The abstract is informative, the numerical evidence is accessible, and attribution and AI use are disclosed. A few minor improvements would help:

- Define $L_m$ explicitly as the longest weakly increasing subsequence length in the Poissonized random word, and state $R=KS$ when introducing the physical triangular contract in Section 6.
- Add a brief comparison with [12], distinguishing its constrained equilibrium rate and asymptotic statements from the present explicit finite comparison bound.
- A small table of the six bin counts, credits and omission slopes would make the numerical application easier to inspect; retain the exact rational witnesses in the supplement.

Reference numbers [1]–[11] above follow the manuscript. Additional reference:

[12] Sayan Das and Evgeni Dimitrov. *Large deviations for discrete $\beta$-ensembles*. arXiv:2103.15227v2. https://arxiv.org/abs/2103.15227v2
