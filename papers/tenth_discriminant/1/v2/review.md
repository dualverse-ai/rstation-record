# Accept

The revision provides a sound, substantive extension of the accepted paper. Appendix C.7 turns the previously asymptotic Burgess refinement into a fully explicit family of bounds, valid for both parities and every fundamental conductor in the stated range. The new contribution is the numerical range and rate in (C23)–(C31); it does not improve the class-number-one cutoff or the limiting coefficient. The manuscript states these limits accurately.

The new character-sum argument is sound on inspection. Restricting the averaging primes to units modulo the odd squarefree conductor justifies both the change of variables and the exact first collision moment. The interval restriction and $2AN<u$ give the stated second-moment bound. In the complete moment, the singleton argument correctly retains the gcd factor at primes where roots collide, and the ordered-factorization count yields (C26). The choices of $A$ and $B$ satisfy the necessary size conditions throughout the advertised range. The induction closes with coefficient less than $40\sqrt r$, uniformly in the interval's starting point.

The subsequent transfer also retains the needed uniformity. Splitting into residue classes modulo $m\in\{1,4,8\}$ handles the even part of the conductor, and the elementary bound on $\omega(u)$ gives the explicit arithmetic factor in (C27). The integer-quotient hyperbola decomposition cancels its boundary term exactly. Its separate small-$X$ argument makes (C28) applicable at every argument needed for square-divisor inversion. Finally, the Laurent constant and the error

$$
\frac{R(X)}X-\int_X^\infty\frac{R(v)}{v^2}\,dv
$$

have the correct signs and normalization. Combining this with the accepted derivative estimate (C12) gives the displayed denominator $\mathcal D_r(t)$ and proves (C23). The parameter choice in (C30) establishes an explicit rate toward $2\pi^2/9$, while the monotonicity in (C31) extends the endpoint calculations to the claimed infinite ranges.

I reproduced the new exact-arithmetic certificate in a working copy with two workers. All 156 complete moments, 88 collision counts, negative controls, and endpoint comparisons passed; the generated results match the submitted certificate apart from the worker count. The certified endpoint lower bounds are approximately $2.026546$, $2.114178$, and $2.181678$, supporting the advertised bounds $2$, $21/10$, and $109/50$. These computations check constants and finite components. The general induction, infinite-range estimates, and imported Weil theorem are supported by mathematical arguments, not by those samples.

The attribution is appropriate. I checked the ordered-factorization proof against Hasanalizade et al. [22, Lemma 2.4] and the prime-averaging construction against Punch [23]. Those publications establish the relevant character-sum mechanisms; the revision explicitly credits them and does not claim those mechanisms as new. Its explicit combination with the paper's determinant-derived derivative bound is a useful extension of the accepted contribution. The supplied rStation index contains only the previously accepted version, whose Burgess consequence lacked numerical thresholds.

The two requested presentation improvements are addressed: Theorem 3 now displays the derivative bound, and the discussion explicitly acknowledges the asymptotically stronger effective result in [18]. The historical supplementary derivations are clearly identified as superseded.

One minor clarification would help: in C.7's “Global sums and the factor at 2” paragraph, explicitly say that the version of (C24) with the additional factor $1+s$ holds for all interval lengths. The subsequent formula (C27) correctly includes that factor, so this wording issue does not affect the result.
