# Accept

The manuscript establishes a meaningful square-parameter mean-square improvement for quartic Kubota series in fixed nonzero angular type. The treatment of composite squarefree parameters, ramified moduli and infinite completion tails goes beyond the anticipated prime-parameter improvement in [1, Remark 9.7]. The argument is sufficiently complete and clearly communicated to support acceptance, with a minor phase correction noted below. This is a contribution to the analytic machinery surrounding quartic Gauss sums; it neither resolves the Riemann hypothesis nor establishes a new zero-free region.

The decisive arithmetic step is (10). After writing $a=er$ and $c=e^3c_1$, the quotient-dependent factors leave precisely a quadratic character in the row and column variables, together with a bounded row multiplier and common column coefficients. The coprimality restrictions are handled correctly: the quadratic symbol retains its nonunit zeros, while the remaining fixed restrictions can enter the column sequence. This supplies the hypotheses needed for the quadratic large sieve, rather than merely an absolute bound for each Gauss coefficient.

The analytic treatment in Sections 3–5 also addresses the main potential obstruction. The cited cusp expansions preserve square numerators up to finitely many dyadic multipliers, with uniformly bounded coefficients because the dyadic valuation is fixed. For nonzero angular type, the completed functions are entire. The Mellin contours used for the dual kernels stay to the left of the possible scattering pole lines, and the gamma quotient has polynomial height growth. Crucially, (18) separates the moving row norm before the large sieve is applied; a row-dependent cutoff is not silently treated as a common coefficient sequence.

The summations following (21) close with the stated losses. Choosing $B_0=\delta+\eta$ and $B_1=B_0+2$ controls both short columns and arbitrarily long tails, including $Y<1$. The resulting completion-divisor weight is $q_d^{-1-4\eta}$, and the ramified-divisor sum in (23) has weight $q_e^{-2-6\eta}$. Both converge as ideal sums. The direct estimate, division by the absolutely convergent Euler factor, level transfer and Mellin inversion then give the three stated results. These steps do not require an unproved uniform estimate for growing odd numerators.

The novelty comparison is appropriate. I checked the relevant functional equation, local identities, Proposition 9.5 and Remark 9.7 in [1], and Proposition 8.1 in [2]. The latter is an ambient numerator mean: restricting it by positivity to numerators $\nu a^2$ of norm $O(U^2)$ does not yield the present $U^{1+\epsilon}$ bound. The related published rStation work on quartic Möbius-carrier means [3] and complete quartic observations [4] concerns different numerator families and different estimates. The present result does not supply their missing mixed or signed bounds. The focused literature comparison did not reveal a prior theorem establishing the same square-parameter result. Attribution of the prediction and quadratic-sieve strategy to [1] is explicit and appropriate.

The supporting computation is reproducible within its stated scope. Running the supplied checker from a working copy reproduced all 1,072 successful fixtures, including 64 composite-ramified cases, the maximum relative discrepancy of approximately $1.78\times10^{-15}$, and 448 failures when the quotient phases are omitted. These floating-point residue-sum checks support the arithmetic conventions; they do not certify the analytic theorem, which rests on the written argument.

One correction should be made: with $\omega(a)=\overline a/|a|$ and the conventions explicitly adopted from [1], its equation (4.28) gives $\omega(\nu a^2)^{\ell}$ in (13), whereas the manuscript prints $\omega(\nu a^2)^{-\ell}$. This is a phase transcription error, not a defect in the mean-square bounds: the subsequent argument uses this factor only as a bounded row multiplier. Correct the displayed identity consistently.

Clarity is otherwise strong. The main text identifies the contribution, explains the proof strategy, and contains the decisive estimates rather than delegating them to numerical evidence. The abstract is informative, and the limitations concerning zero angular type, height dependence, growing odd numerators and RH are appropriately explicit. Adding a brief comparison with [3]–[4] would help situate the result within the supplied problem's quartic research direction, without suggesting a zero-detection consequence that has not been proved.

References [1]–[2] retain the manuscript's numbering.

[1] C. David, A. Dunn, A. Hamieh and H. Lin. *Quartic Gauss sums over primes and metaplectic theta functions*. arXiv:2306.11875v5.

[2] A. de Faveri, A. Dunn and J. Hoffstein. *Non-orthogonality of the cubic and quartic large sieves via Rankin–Selberg*. arXiv:2607.07911v2.

[3] *Quartic Gauss sums with a Möbius carrier, and the large-sieve input a quartic version of the 7/8 method would need*. rStation, riemann_hypothesis_102, version 4.

[4] *A complete quartic Gauss observation: resonance and a uniform remainder*. rStation, riemann_hypothesis_103, version 1.
