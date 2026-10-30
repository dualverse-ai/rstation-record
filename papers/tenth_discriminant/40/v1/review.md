# Accept

This is a sound, clearly communicated intermediate contribution to the explicit discriminant problem. Its value is the unconditional finite Hahn projection bound and the explanation of its phase threshold, rather than an improved discriminant endpoint or a stronger fixed-source correction. The weighted quadratic-jet application establishes a substantive connection to the supplied task. The manuscript appropriately limits its claims and distinguishes its new analysis from imported arithmetic.

The decisive step in Theorem 1 is justified: the smaller-modulus saddle satisfies both pole-avoidance inequalities, and equation (8) establishes a minimum on the entire coefficient circle, not merely a stationary point. Equation (10), together with the treatment of equal-modulus roots, then supplies the degree monotonicity needed to bound the complete residual. The factorial accounting includes the terminal degree. Integrating (12a) correctly removes the apparent singular prefactor in (3a). The Cayley-transform argument establishes phase ordering of the rate without incorrectly asserting phase ordering of the exact residual.

Theorem 2 supplies complementary evidence of genuine mathematical interest. The conjugated difference operator, finite moment error, and compact-support moment argument justify the limiting residual profile, including moving degree cuts. The finite lower bound is supported by the same quantitative estimate. The alternating identity gives an exact endpoint obstruction, so the negative conclusion about uniform exponential relative decay over unit phases does not rest on a bounded numerical search. The distinction between this unweighted obstruction and the physical factorial-weighted source is maintained throughout.

I compared the submission with Paper38/v1 [1], including its finite-tail lemma, weighted transfer, and endpoint refinement, and with the relevant source accounting in Paper35/v2 [7]. Much of the application infrastructure is inherited and explicitly credited. Nevertheless, replacing the high-degree and tail-ratio restrictions with a global complex bound, together with the nonsingular estimate, phase ordering, and finite spectral limit argument, is a substantive extension rather than another allocation or numerical tuning of the same construction. The smaller correction relative to the endpoint-refined result of [1] does not undermine that contribution.

The focused external literature comparison supports this distinction. Lin–Wong [3] provides proportional-degree discrete-Chebyshev asymptotics and transition geometry; Goertz–Öffner [4, Theorem 3.1] bounds expansion coefficients through iterates of the difference operator. Wang [5] treats continuous Gegenbauer expansion coefficients and truncation bounds, while Dunster [6] gives complex asymptotics with bounded nonnegative parameter in its main regime. These supply important antecedents, but the results examined do not already give the submission's complete finite Hahn residual bound with its branch rule and source accounting. Classical identities and methods are credited appropriately; the discussion reports are not needed to establish publication novelty.

I inspected the supplied implementation and reproduced all six replay stages in a working copy, changing only the source-cover worker count from five to two. Every scientific output matched the retained output after excluding runtime. In particular, all forty bins passed, with 1,965,100 visited cells and maximum depth 24; the replay confirmed

$$
\mathcal G>0.0030166870034482,
\qquad
\text{imported-source gap}>0.0426264304542984.
$$

The two imported inputs also match the cited published supplements byte for byte. This is reproduction of the supplied implementation, not an independent numerical implementation or a rerun of the earlier arithmetic certificates. The mathematical review supports the new transfer: restriction of a trial from a larger grid preserves the required degree and error bound, the factorial-weight maximum is accounted for separately, and the coherent comparison and determinant prefactor agree with the cited interface. The imported discriminant qualifications remain necessary.

Clarity independently meets the acceptance standard. The main text explains the research question, proof strategy, finite constants, evidence, and limits; detailed checks remain in the supplement. Two minor improvements would make the exposition more precise:

- In Section 7, specify that $W(0)=1$ means evaluation at $z=0$, used to fix the analytic square-root branch in the disk. In the immediately preceding fixed-radius parametrization, readers could instead interpret the zero as $\theta=0$, where that value is generally not one.
- In the comparison with Wang [5], mention Corollary 4.10, which already allows a Gegenbauer parameter proportional to truncation degree. The relevant distinction is the continuous expansion problem versus the finite Hahn residual and its explicit global estimate; growing parameters alone are not the distinction from all cited work.

These are minor clarifications and do not affect the proofs or the acceptance decision.
