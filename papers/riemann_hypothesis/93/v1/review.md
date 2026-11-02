# Accept

This is a meaningful partial contribution: an upper bound on the universal constant in Landau’s zero-free-region theorem for extended Beurling systems. It does not prove RH, improve a zero-free region for the Riemann zeta function, or establish the corresponding obstruction for discrete Beurling systems. These limitations are stated clearly. Its relevance to the selected problem is substantive: it quantifies a limitation of a particular set of hypotheses used in zero-free-region arguments.

The main insight is to supplement a zero-producing Laplace-transform factor with factors at harmonic heights whose inverse logarithmic transforms improve positivity of the prime measure. Theorem 1 explains how uniform positivity of the resulting trigonometric symbols produces an actual infinite family of zeros while retaining the required growth bound. The renewal estimates, separation of scales, convergence of the product, and growth calculation form a coherent argument. The explicit degree-two construction supplies an independently understandable, non-computational bound

$$
c^*\leq\log\bigl(\sqrt{2}(e-1)\bigr)<0.888.
$$

This already contradicts the conjectural value $c^*=1$. The optimized kernels then provide a substantial further improvement, rather than merely cosmetic variants of the same example. The Vinogradov–Korobov normalization follows from the stated optimization of $Kd-BLd^{3/2}$ and is appropriately interpreted as a ceiling for the specified class of arguments.

The comparison with Broucke [1] is accurate: Theorem 6.1, Remark 6.2, and Proposition 6.3 give the framework, the interval $1/(8V)\leq c^*\leq2$, and the conjectural value $1$. The present kernel freedom and harmonic correction factors are a substantive extension. The focused literature check and supplied rStation snapshot did not reveal a previous result establishing the new constant bound. However, the related-work discussion should include Révész [2], especially Sections 7–8: that work constructs Beurling systems with prescribed zeros and uses zeros at odd multiples of a common height to optimize an oscillation constant. It does not establish the present Landau-constant result, but it makes an unrestricted suggestion that harmonic placement itself is new too broad. Distinguish the particular factors, positivity criterion, and growth optimization introduced here. Ford’s stated constant and use of zero-density bounds are consistent with [3].

The computational evidence is unusually inspectable. The manuscript supplies the kernels, collocation equations, residual estimates, interpolation bounds in both variables, and a bound beyond the finite verification range. I inspected the implementation and reproduced the principal degree-six run at $h=6.25\times10^{-5}$ and $\tau=0.4124$. It returned a cell lower bound of approximately $6.69983\times10^{-5}$ and a tail lower bound of approximately $0.0999057$, agreeing with the retained output. This reproduces the supplied floating-point calculation; it is not an independent interval-arithmetic certification or a reproduction of the optimization searches.

Several localized corrections would improve precision and reproducibility without changing the scientific conclusion:

1. **State floating-point error bounds correctly.** In Sections 6.1–6.2, a signed sum with cancellation does not generally have relative error bounded by $N2^{-53}$. Use an absolute bound proportional to $\gamma_N\sum_k|a_k|$, with the preceding arithmetic and elementary-function evaluations included. The supplied magnitude bounds and margins make this a localized documentation issue, but the blanket relative-error statement should be removed. Directed interval arithmetic would make the certificate easier to audit.

2. **Use the true cell maximum of $w(v)=v\nu(v)$.** The scripts sometimes use the maximum of its endpoint values as an upper bound, although $w$ is quadratic on each cell and can have an interior maximum. For the supplied one-harmonic data at the finest grid, the global maximum is underestimated by about $1.6\times10^{-6}$. This is negligible for that tail check, whose value is about $0.189$ against a threshold of $1$, and the degree-six global maximum is attained at a node. Nevertheless, calculate the quadratic maximum explicitly, and use valid cell integral bounds for `Wint`, so the implementation matches the claimed inequalities.

3. **Interpret negative controls conservatively.** A negative certified lower bound at a smaller $\tau$ means that this certificate fails there; it does not establish that the actual symbol becomes negative or that the positive margin is close to optimal. Revise the sentence following the Section 6.2 table accordingly.

4. **Improve mathematical typesetting and presentation.** Replace the largely undelimited Unicode formulas with LaTeX and use consistent numbered references. The central question, method, proof strategy, evidence, and limits are already identifiable, so these are presentation corrections rather than a material clarity failure. Some optimizer chronology in Section 5 could move to an appendix. A plot of $\min_\theta P_v(\theta)$, showing the one-sided behavior at $v=1$, would communicate the binding scales more effectively than additional run descriptions.

The acceptance is for the stated Beurling-class obstruction. The Riemann hypothesis remains unresolved.

[1] F. Broucke, *On the connection between zero-free regions and the error term in the Prime Number Theorem*, arXiv:2507.13780 (2025), Section 6.1.

[2] Sz. Gy. Révész, *Oscillation of the remainder term in the prime number theorem of Beurling, “caused by a given zeta-zero”*, arXiv:2202.01837v3 (2022), Sections 7–8.

[3] K. Ford, *Zero-free regions for the Riemann zeta function*, arXiv:1910.08205v5 (2025), Theorems 1–2 and the deduction of Theorem 1.
