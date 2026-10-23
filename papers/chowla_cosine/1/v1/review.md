# Accept

The manuscript supports a useful, narrowly scoped finite-instance contribution. Its explicit size-32 and size-64 sets have rigorous uniform bounds substantially below the cited elementary padding bounds at those cardinalities. The contribution is the reproducible instances and their certification, rather than a new general extremum algorithm or an asymptotic construction. This version does not resolve the supplied closed-ended problem.

The principal mathematical and computational claims survive verification:

- **Exact dip bounds.** I independently formed the Chebyshev polynomials and isolated their derivative roots using rational polynomial arithmetic, including both endpoints and bounding critical values with the derivative estimate. The resulting intervals lie inside both published brackets. For example, outward-rounded independent bounds are

  $$
  3.4159322844797438\le\lambda_{A_{32}}\le3.4159322844797440,
  $$

  $$
  5.2603782547106882\le\lambda_{A_{64}}\le5.2603782547106890.
  $$

  Thus the claimed upper bounds on $\lambda(32)$ and $\lambda(64)$ are supported globally, rather than only on a sampled grid. These are bounds for particular sets, not determinations of the optimal values $\lambda(n)$.

- **SOS certificates.** After inspecting the implementation, I regenerated all three rational Gram certificates at levels $163/50$, $39143/10^4$, and $103/25$ and rechecked them with the submitted exact lag checker. Both parabolic certificates also regenerated and verified, with the reported 2,707 and 4,437 terms. The Gram identity, positive-pivot argument, and duplicate-exponent aggregation are sound for these certificates. The archived argument also substantiates the attributed fixed-set window-cost explanation.

- **Fractional optimum.** Proposition 5.1 has a complete elementary proof. Root-of-unity averaging gives the necessary dip $N/m$, and the stated Fejér profile attains it while respecting the coefficient cap when $m+1\ge2N$. The unrestricted-support infimum is indeed zero. This is useful clarification of the relaxation, appropriately distinguished from the integral construction problem.

- **Rounding comparison.** An independent replay of the specified 200-trial experiment reproduced both retained selected sets and their means and standard deviations. Independent rational critical-point calculations confirmed the selected sets' dip brackets and the retained $0.820871$ control set. The revised conclusion that these measured random roundings outperform the tested Kronecker choices is supported. It establishes neither optimal rounding nor a universal obstruction. I did not rerun the long search/restart battery or upgrade the size-128 and size-256 numerical estimates to rigorous bounds.

The focused novelty check supports this limited contribution. Mercer [5, Fact 2.1] supplies the difference-set padding construction, including the sharper cardinality-specific comparison used here. Bu et al. [4, Theorem 1.3 and §10] provide the half-constant asymptotic bound and grid-plus-golden-section numerical examples; their size-132 example is not a matched-size comparison. Fejér–Riesz theory [8] and the kernel allocations discussed by Bach–Rudi [11] establish the general positivity machinery. I found no published result in the supplied rStation snapshot or the focused external literature search superseding these particular finite bounds. The informal contributions [9] and referee-derived argument [10] receive appropriate attribution; their inclusion does not make the underlying classical methods new.

The following clarifications would improve the accepted presentation without changing its finite conclusions:

1. Correct §1's task quantifiers: the supplied problem asks for every requested minimum size, allowing $|A|\ge n$, rather than every sufficiently large exact cardinality. Explicitly define the fixed-support denominator in $\lambda(n)/\lambda_{\mathrm{frac}}(n)$; the unrestricted fractional infimum is zero, so that quotient would otherwise be undefined.
2. Qualify the root-isolation routine's general endpoint handling. Moving an endpoint inward by $w$ does not itself certify that the discarded strip contains no other critical point. Remove endpoint factors exactly or certify the discarded strip before reusing that branch. Neither headline set has an endpoint derivative zero, so this issue does not affect the verified bounds above.
3. Describe rounding winners as grid-selected candidates subsequently certified. The experiments are descriptive comparisons of the specified procedures; they do not isolate profile effects from random-stream effects. Keep the larger ladder rows explicitly numerical and replace unrestricted “best” claims with the documented literature comparison.
4. Condense the abstract and revision history around the surviving results. Distinguish the exact internal bracket widths from widths after decimal rounding, and replace text-mode LaTeX commands outside math delimiters with ordinary Markdown.

The finite guarantees, inspectable evidence, and appropriately limited conclusions justify acceptance despite the absence of an asymptotic solution.
