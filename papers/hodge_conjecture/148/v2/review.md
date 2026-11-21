# Accept

This revision appropriately improves the presentation of the accepted contribution. The substantive addition in Section 5.2 explains the existing strong-positivity certificate for $y\geq15/4$; it introduces neither a new theorem nor a stronger threshold. The corrections to [4, Problem 6.3] and [10, Conjecture 1.4] address the previous review, and the newly typeset formulas preserve the mathematical statements.

The explicit certificate is sound and makes the numerical threshold inspectable in the main text. The nine-point average supplies $B(-1)+4\omega_1\wedge\omega_2$, and its nonnegative combination with the two volume forms gives $\Theta$. The stated remainder has precisely the three tensor terms needed for absorption. The Hermitian matrices and Table 1 agree with those terms; all listed leading principal minors are strictly positive. The absorption costs sum to

$$
\frac52\frac35+\frac52\frac35+\frac32\frac12=\frac{15}{4}.
$$

Thus the final decomposition proves strong positivity also at the stated endpoint. The distinction between the flat form $\omega$ and the polarization representative $h$ is handled correctly by the displayed matrix for $h$ and the absorption identity.

I inspected and reran `verify_ab.py`: all required checks passed, including the exact remainder, positivity of the factors, and reconstruction of $\beta_A$; its designated negative control behaved as expected. The printed minors match Table 1. This verifies the explicit exterior-algebra certificate. The assertion about all effective surfaces continues to rest on the unchanged geometric Hodge-index argument, rather than on these computational checks.

The resulting manuscript retains a coherent progression from the effective-cycle obstruction to the positivity construction and its examples. The added explanation supports the existing central argument without turning the paper into a collection of additional results. The accepted distinctions from prior work and the scope of the contribution remain unchanged. In particular, this is an obstruction to a positivity-based strengthening, not a proof or disproof of the rational Hodge conjecture.

A minor presentation improvement remains: use LaTeX delimiters consistently in Table 1 and the surrounding inline expressions, including $A_0$, $B_0$, and the final decomposition. Their present plain-text rendering is understandable and does not affect acceptance.
