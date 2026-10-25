# Accept

The update makes substantive extensions to the accepted determinant method: the multibranch norm window and continuous level-set optimization improve the class-number-one thresholds, while the reduced-form and genus arguments extend the method to general class numbers. The contribution is the explicit proof route and its quantitative estimates. The class-number lists themselves are already known, as the manuscript appropriately acknowledges through [15] and [19]. The exponent-sensitive bounds also have a different scope from the unrestricted fixed-exponent results in [16, 18].

The common-denominator correction in Section 6.4(2) is sound. Keeping the three terms together gives

$$
\Delta_{1/S}(D)\geq
\frac{C_{1/S}(D_{\mathrm{lo}})+\frac{3(K+3)}{8K}\log(X/X_{\mathrm{lo}})}{S(D)}.
$$

Positivity of the anchor constant therefore permits discarding this entire contribution uniformly on the infinite tail. It does not require freezing a positive coefficient proportional to $1/S(D)$ at its initial value. The unit-slice formulation of the Fubini–Jensen saving, the primitive norm progressions, and the squared-ideal argument for the two-torsion fiber bound support the new extensions. In particular, the latter correctly distinguishes injection below $\sqrt{M(D)}$ from the larger fibers possible below $M(D)$.

I reproduced the multibranch verification, including all eight Rosser–Schoenfeld intervals, all six exact-prime intervals, and the new hybrid boundary intervals. The Decimal infinite-tail enclosure was

$$
[0.0008437816579606860548871,\;0.0008437900779883421356001],
$$

with positive logarithmic coefficient exceeding $0.18769$. The hybrid enclosure on $[863,867]$ reproduced as approximately $[0.0020883080,0.0020883385]$.

The class-number-24 and class-number-30 programs also completed successfully, reproducing the stated tail margins and all 3,793 fields, with maximum discriminant $166,147$. I additionally evaluated the supplied tail bound for every $2\leq h\leq16$ and every admissible genus stratum; the smallest resulting margin exceeded $0.295$. An independent reduced-form histogram through $D=166,147$ reproduced every class-number total and maximum in Table 4. This independently checks the finite totals in that range; exclusion of larger discriminants and the group-structure calculations rely on the reviewed argument and the supplied verifiers.

For Theorem 1.4, I completed the hierarchy verifier in a review copy with a bounded memoization cache and the conservative rounding correction described below. All assertions passed: the minimum margins remained $0.039593$ for Tier I and $0.106818$ for Tier II, and the unrestricted quartic-ray margin exceeded $0.135263$ after normalization by $\log h$. The specialized exponent bounds also passed. These computations reproduce the author's mathematical certificates with the stated local correction; they are not an independent implementation or a formal verification of the entire proof.

The following local corrections and reproducibility improvements should accompany the accepted update:

- In `Sigma_univ_iv`, replace the fixed allowance $89$ in $R_{\mathrm{lo}}=c_RX-89$ by an allowance covering every selected $K$, such as $109$, or use the individual anchor's $K$. The hierarchy now includes $K=109$, so $89$ is insufficient. For example, at $D=1,000,000,039$, $29X$ has remainder $94$ modulo $109$. The complete rerun with $109$ retained all positive margins and the reported bounds.
- Reconcile Section 6.5(1)'s annular-row explanation and displayed edge term with the implementation. Points in the interior hole are excluded from the window sum; they should not be described as an additional plateau contribution. A full row has the integral bound plus one maximum-value term, whereas an annular row has two endpoint terms. After halving per class, this gives the code's edge factor $\int_0^1\widetilde w(\max(u_{\min},v^2))\,dv+\sqrt{u_{\min}}\widetilde w(u_{\min})$. The displayed formula instead doubles that factor. State explicitly which valid bound produces the numerical certificates.
- Include the $2\leq h\leq16$ tail assertions in the distributed main routines, especially the $h=16$, genus-rank-four case. The existing routines print tail checks only for $17\leq h\leq30$, although their finite censuses include smaller class numbers. Bound the hierarchy's memoization cache as well: the original run exhausted a 1 GiB limit, while clearing that cache periodically preserved the results.
- In Section 6.6, the rectangular lattice for even discriminant has covering radius $\sqrt{D+4}/4$, equal to the chosen $\delta_D$, rather than $\sqrt D/4$. The radius bound actually used remains valid. Simplify the metadata abstract so that the new results and their scope are easier to distinguish from the accepted baseline.
