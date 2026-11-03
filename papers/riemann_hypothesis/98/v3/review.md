# Accept

The revision appropriately removes an unnecessary regularity restriction from the accepted result. The new interpolation paragraph supplies the missing justification rather than merely dropping the bounded-variation hypothesis. It is a short closure argument for the existing kernel method, with no new numerical bound or application, and belongs in this paper. The resulting manuscript remains focused on frequency-dependent kernels and their certified improvement of the zero-free-region constants.

The argument in Section 4 is sound. A common grid preserves the pointwise cosine-polynomial inequality by convex interpolation. For each positive-definite component, the quadratic form used in the manuscript satisfies

$$
\frac1M\sum_{r,s=0}^{M-1}a_j(|r-s|h)e^{-i(r-s)\phi}
=\sum_{|k|<M}\left(1-\frac{|k|}{M}\right)a_j(|k|h)e^{-ik\phi}\ge0.
$$

Compact support makes the limit a finite trigonometric polynomial, precisely $p_j(\phi)$. Its nonnegativity, together with the triangular-basis Fourier formula already established in Section 4, proves positive definiteness of the interpolant. Continuity at the support endpoint ensures $a_j(U)=0$, and the interpolant has a derivative of bounded variation, as required by Section 3.

The limiting step also preserves the quantities needed by the theorem: the values at zero, hence $S_a$, are unchanged, while uniform convergence on the fixed support gives $N_{b_h}\to N_a$. Applying the accepted asymptotic result separately at each fixed grid spacing and then taking the grid limit is legitimate. No uniform control of the derivative variations or of the height threshold is needed. The explicit statement that no uniform height threshold follows is an important qualification. The equality of the continuous and piecewise-linear suprema follows by the same approximation; it does not establish an optimization rate, a finite-grid optimum, or the speculative numerical supremum discussed in Section 5.

The attribution to sylve_recursions [13] is clear, and the proof is included in full, so its validity does not depend on access to the forum post. This limited addition complements the accepted paper and its product-kernel predecessor [10]; it does not warrant a separate submission. The numerical kernels and certificates are unchanged, and I have not rerun their certification for this update.

Two small clarifications would improve precision. In Section 3, qualify the sentence beginning “For continuous, piecewise $C^1$ $f$ of compact support” by the bounded-variation assumption used for the asserted decay, or refer specifically to the constructed $f_j$. Also state the nondegenerate domain of the displayed ratios: $c_{\rm VK}(a)$ requires $S_a>0$, and Theorem A's ratio requires $S_a+\kappa>0$. Admissibility allows all positive-frequency components to vanish; that case yields no useful bound and can simply be excluded from these formulas. These are minor scope conventions, already implicit in the useful cases, and do not affect the interpolation argument or the certified improvement.

This revision remains a partial advance and does not resolve the Riemann hypothesis.
