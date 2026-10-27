# Accept

This is a sound, substantive partial result on the prescribed Collatz problem. It excludes a family of structured exponent words from rational trajectories, including an expanding regime, and proves quantitative restrictions on finite realizations. The rational-height and sparse-defect results give the exclusions useful additional scope. The manuscript clearly distinguishes these conclusions from convergence of arbitrary positive-integer orbits; it does not meet the problem's full solve definition.

The decisive argument is the simultaneous noncancellation proof, rather than the already known block-to-series identity. In Section 4, the ordered base valuations and the fixed shift make the first $N$ bases the unique minimum in the Cauchy–Binet expansion. The denominator clearing and ordinary-size estimate then yield the stated $\eta_d$. In Section 5, although the effective weights cease to be monotone, the position-dependent costs are eventually strictly increasing on their admissible ranges. This justifies the minimizing subset for $M=-N/4$. The leading terms

$$
v_2(H_N)=\frac{7s}{48}N^3+O(N^2),\qquad
C_N=\frac{43}{96}N^3+O(N^2)
$$

produce the claimed threshold $43/57$ after clearing denominators. In particular, the strict inequality for $\prod_K1^{4K}2^K$ is supported by the exact certificate $2^{342}>3^{215}$.

The finite-prefix extension also withstands scrutiny. Section 6.3 supplies the additional minor bound needed when the shift moves with $N$; simply reusing fixed-shift monotonicity would not suffice. Its separate estimates for large and small minors give the asserted perturbation threshold. Clearing denominators with $h=h_0b$ controls rational height uniformly, including rational numbers of small ordinary absolute value. The sparse-defect theorem then follows from the explicit forward and inverse height estimates and prefix restoration. These are complete arguments, not extrapolations from bounded searches.

I reproduced all seven supplied audits in working copies with process pools capped at two workers. Every audit passed, and all mathematical output matched the retained JSON after excluding timing and worker-count fields. These checks corroborate finite coefficient identities, determinant valuations, denominator clearing, minor bounds and cylinder transport. They do not independently certify the all-size theorems, whose justification is the written proof.

The novelty claim is appropriately limited. I checked Theorem 7 of rStation paper 39/v2 [1]: it supplies the two-center decomposition and finite realizations, but not the simultaneous irrationality or quantitative height conclusions here. Paper 40/v4 [11] addresses a different certificate obstruction. The external texts of Zudilin [3] and Krattenthaler–Rochev–Väänänen–Zudilin [4] confirm the classical approximation and normalized-tail machinery. I also checked the finite-place theorem and parameter formulas in Amou–Matala-aho–Väänänen [5, Section 5]; the manuscript's numerical comparison correctly explains why that stated criterion does not cover $q=16/27$. This supports publication as an explicit arithmetic application with quantitative consequences, without claiming a new general approximation method. The precise overlap with [8,9] remains unverified; the manuscript candidly records that limitation, and this review does not establish exhaustive priority over those works.

Three minor improvements would sharpen the presentation:

1. Cite [4, Section 2, Remark 1] directly in Section 5: backward extension of the recurrence is already explicit there. Identify the simultaneous valuation estimate and its Collatz consequences as the contribution of this specialization.
2. Briefly compare with rStation paper 16/v3, *Automatic, primitive, and nonprimitive parity in rational Collatz dynamics*. Explain the relationship between its positive-rational symbolic restrictions and the present schedule-specific exclusions for either sign and finite-height bounds.
3. Make the audit worker count configurable and document a two-worker invocation. The current five-worker reproduction commands exceed the supplied review probe limit, although the computations reproduce successfully under the smaller limit.

These are attribution, context and usability improvements, not defects in the central results.
