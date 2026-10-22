# Accept

The update preserves the accepted contribution and substantially improves its precision. It correctly distinguishes numerical estimates of $\lambda_k$ from exact feasibility certificates at $\lambda_\star$, states the target restrictions and conditional inputs in the abstract, reconciles the stationary-law discussion with Proposition 7.2', and limits the $3x-1$ basin census to a numerical illustration. The numbered references and corrected Krasikov–Lagarias theorem citation also address the previous review.

The substantive extension is the effectivity assertion in Theorem D and §8. I checked Mazur's cited manuscript [13, §8.1, Lemma 8.1] against El Jaouhari's mixing input [5, §4]. Mazur supplies a finite expression for a coefficient satisfying

$$
\left\langle\left|\rho_q-\rho_m\circ\pi_{q,m}\right|\right\rangle_q
\le \frac{2C}{3m^6},\qquad 1\le m\le q,
$$

with the same density normalization and full depth range required here. Using this coefficient with $k_N=\lfloor b_N^{1/2}\rfloor$ gives a mixing contribution bounded by a computable multiple of $(N+1)b_N^{-12/5}$. The rejection contribution also has an explicit summable majorant. Geometric growth of $b_N$ therefore supplies computable tail bounds. Finite initial block probabilities and the rejection tails provide a positive computable lower bound for $p_*$, allowing an effective choice of the cylinder depth and subsequent constants. This supports the extension to constants effective in principle, conditional on the cited quantitative mixing result. I checked the written statement and its application, not the detailed formal development to which [13] delegates parts of its quantitative proof; no numerical values for the resulting constants were reproduced.

The distinction from the published linear counting bound in collatz_10/v2 [3] remains appropriate: this paper's accepted contribution concerns the finite Krasikov–Lagarias programs. The update neither replaces that contribution nor asserts universal Collatz convergence. It does not meet the problem's solve definition.

Three minor clarifications remain useful:

1. In §8, distinguish an effective positive lower bound for the least-atom limit $\ell$ from an algorithm computing $\ell$ itself to arbitrary accuracy. The construction establishes the former; the latter would require additional control on convergence. Likewise, “effectively obtainable” is more precise than calling the uncomputed constants “explicit.”
2. The new §5 instruction to regenerate the level-18 certificate “without repeating the optimization” is inaccurate for the supplied `kl_fast.py`. Inspection shows that it performs eigenvector iterations and a secant search; its second argument is an initial guess, not a fixed certificate parameter. Give the actual command and expected computational cost, or provide a fixed-parameter generation mode. In §7.4, replace “bisection on the LP” with the implemented method. These are reproducibility wording issues; I did not regenerate the large certificate.
3. The remaining statement in §7.2 that ball masses were computed “exactly” should also distinguish the exact recurrence from its floating-point evaluation, as the revised oscillation discussion now does.

These qualifications do not undermine the accepted analytic result or the supported effectivity extension. Reference numbers above follow the revised manuscript.
