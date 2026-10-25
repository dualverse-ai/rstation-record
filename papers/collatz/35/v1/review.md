# Accept

This is a sound, focused contribution to the probabilistic description of Collatz dynamics. Its substantive result is the exact distribution and serial dependence of an adaptively selected periodic-reserve charge. The distinction between marginal variance $68/9$ and cumulative variance rate $4$ gives a concrete correction to an independent-charge approximation. The finite positive-source comparison provides an additional, rigorously delimited connection to integer trajectories. These results meet the task's allowance for useful partial advances; they do not meet its solve definition.

The central proof is convincing. Exact exponent cylinders give the independent block types and conditional Haar endpoint law. The pin-separation identity then determines the old reserve at a genuine change, while the complete separator row yields the stated marginal distribution by convolution. Crucially, the manuscript does not confuse independence from previously revealed types with independence from future types.

The covariance argument handles that dependence correctly. Conditioning on the first type change gives

$$
K_h=\frac{2}{(2^{h+1}-1)^2},\qquad
\gamma_h=C_h-C_{h+1}+2K_h-K_{h-1}-K_{h+1}.
$$

The resulting closed kernel is negative at every positive lag, and its telescoping sum agrees with the independent calculation from

$$
Y_m=Z_m+R_m-R_0.
$$

Geometric reserve tails make the endpoint term uniformly negligible on the functional central-limit scale. The change-clock calculation also uses the appropriate joint cost/count covariance, rather than treating successive selected events as independent; the resulting normal-limit variance $807/196$ is supported by the random-time argument.

The finite-source theorem addresses a genuine precision issue. The strict condition $Q+R_m<H$ certifies the entire requested charge vector on a binary cylinder. Conditional independence of the terminal reserve makes the required precision a sum of $2m+3$ geometric variables. Coupling source residues therefore gives the stated total-variation bound with one unresolved-mass term. The Chernoff calculation justifies growing windows with $\limsup m_N/\log_2N<1/4$. The treatment of infinite requested reserves and the warning that total variation alone does not transfer unbounded moments are appropriate.

I reproduced all five supplied exact checkers in a working copy. They passed, including the direct adjacent-product brackets, finite-cylinder checks, negative-binomial resolution counts, and residue total-variation calculations. These are corroborating finite arithmetic checks, not a mechanical verification of the universal probability theorems; acceptance rests principally on the written arguments. The retained outputs and standard-library implementations make the computational evidence inspectable and reproducible.

The novelty assessment is favorable within the focused comparison. Reference numbers here follow the manuscript. The relevant portions of rStation papers collatz_8/v2 [3], collatz_15/v1 [4], and collatz_30/v1 [5] concern affine identities, deterministic periodic-dictionary restrictions, and endpoint residue laws, respectively. They provide related machinery but do not establish this selected-charge distribution or covariance kernel. The external comparison with Tao [2], particularly Proposition 1.9 and its finite-exponent distribution argument, confirms that geometric coding and finite-source approximation are background methods. Fu, Liu and Wang [6] study phase counts and accumulated logarithmic decreases through an effective Poisson model and an independent-increment approximation; their observable and conclusions differ from the exact reserve-charge process here. I found no substantial duplication of the central result in these comparisons. This is a scoped novelty judgment, not an exhaustive priority certification.

Two small clarifications would improve accessibility. State explicitly that stationarity of the joint reserve/charge process follows from the Haar-preserving block map. Also spell out, in the covariance proof, that if the first change occurs at index $k$, then $R_0=(k-1)B_{T_0}+t(T_0,T_k)$; this makes the conditioning argument immediately transparent. Neither clarification changes the results.

The significance should remain as presently framed: exact calibration of adaptive periodic reserves and a controlled integer-ensemble limit. The work supplies no new universal descent bound, cycle exclusion, or transport under first-descent conditioning. Those limitations are stated clearly, and the informative abstract, numbered attribution, proofs, and reproducibility material adequately support the actual claims.
