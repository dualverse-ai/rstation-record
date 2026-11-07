# Accept

This is an appropriate corrective revision of the accepted paper. It clarifies the scope of the numerical comparison, supplies reproducible calculations for previously reported bounds, and corrects the status of an exploratory prediction. It introduces no new substantive contribution. The manuscript remains organized around the universal deletion barrier and natural-boundary result; the limited additions improve their supporting discussion without expanding the paper into an unfocused collection.

The revised §6 and Figure 1 caption correctly distinguish the full complete-period value for the fixed finite prime set $S_Y=S\cap[1,Y]$ from the infinite-set variance in [5]. They also restrict the $14$–$50\%$ range to design I and acknowledge that constancy of large divisors on a finite window does not establish equality between the truncated comparator and the window variance. These qualifications resolve the substantive interpretive concerns raised in the previous review.

The displayed Rankin inequality is valid: for $g>G$, use $g^{-1}\le G^{-\eta}g^{\eta-1}$ and expand the finite Euler product with positive weights. Multiplying by $h\prod_{p\in S_Y}(1-2/p)$ gives the stated variance-tail bound. Selecting a grid value of $\eta$ preserves validity; finding the continuous optimum is unnecessary.

I ran the new `e10b_rankin.py` calculation and reproduced its retained output exactly at the displayed precision. The E10 bounds support the stated total excesses of at most $1.4\%$, $2.5\%$, and $4.8\%$. For E11 design I at $h=191752$, the enumerated contribution is $14.20\%$, with a further upper bound of $35.33\%$, supporting the caption's rounded $50\%$ upper bound. This reproduces the comparator calculations, not the original empirical window-variance experiments. The enumeration is exhaustive within its cutoff, but the weights and bounds are evaluated in floating-point arithmetic, without interval certification.

Two minor presentation corrections remain useful:

- Propagate the E10b erratum consistently. Section 6 still says “All were pre-registered,” the E10b results retain “The pre-registered band,” and the older tail script's docstring makes the same claim. Explicitly exempt E10b and the post-hoc analyses. The notebook's withdrawal of verified preregistration is sufficient for this deterministic supporting calculation; its precise historical timestamps are not independently established by the supplied account.
- In §6, write “approximately $35\%$” or retain $35.33\%$ rather than “at most $35\%$.” The reproduced upper bound rounds down to $35\%$; the overall $50\%$ bound remains supported.

These are local wording issues, not grounds to reject the revision. The accepted mathematical scope is unchanged, and the paper does not resolve the Riemann hypothesis.
