# Accept

This revision appropriately corrects and clarifies the accepted contribution. It preserves the upper bounds for selections supported on free ring-line caps and the obstruction to the specified relaxation at $M=4$. It introduces no new substantive contribution requiring a separate submission, and the additions do not materially worsen the paper's organization or clarity.

The principal changes address the previous review. The abstract and introduction now distinguish fixed-$M$ limiting coefficients from finite-prime bounds, including the useful example $30/17$ at $M=8,p=17$. The free ring-line cap hypothesis is explicit, and the discussion of the unrestricted full-lift search in [8] no longer treats its entire search class as covered. Theorem 3 now correctly distinguishes directional $L_d$-injectivity of its patterns from simultaneous Queen injectivity of a residue support. The added attribution to Kurz [16] appropriately identifies the classical product bound and the previously known capacity modulo four.

The new differentiation argument supplies the missing justification for monotonicity. From $\mu(\mu^2-3\mu+4)=2M^2$, it correctly obtains

$$
M^2\frac{d}{dM}\left(\frac{\mu}{M}\right)
=\frac{\mu(4-\mu^2)}{3(\mu-1)^2+1}<0
\qquad(M>2).
$$

This is supporting explanation for an existing claim, rather than an expansion of the scientific scope.

I inspected and ran the revised standard-library verifier; all five passes succeeded. In particular, the corrected factor of five in the $M=3$ analytic-tail comparison is present, and the final pass now recomputes the bounds before comparing them with the eight stored benchmark cardinalities. The Farkas certificates and rational partition witness also passed. The certificate bundle's mathematical data are unchanged. This verifies the retained certificates and cardinality comparisons; it does not reproduce the searches in [8] or the optional SciPy discovery runs.

The added discussion of [18] accurately credits the subsequent determinant-general result instead of incorporating its proof as another contribution. Its constants agree with Theorem 1 of Paper 103 v2. The distinction between determinant-general supports and general free ring-line caps remains essential.

A few minor presentation qualifications remain:

- In the abstract and summary, explicitly attribute the endpoint thresholds $p=19$ at $M=3$ and $p=43$ at $M=5$ to the integer floors. The displayed unfloored expressions themselves exceed $1.8$ at those endpoints. The proof already supplies the valid sharper bounds $102/57<1.8$ and $386/215<1.8$, respectively; the thresholds are sound, but the compressed wording can suggest an incorrect numerical implication.
- In the new note citing [18], specify the whole-period windows $n=4mp$. That paper's stated density bound does not cover arbitrary window sides. Likewise, the abstract's $M=2$ statement for $m\in\{3,4\}$ should retain the respective prime thresholds $41$ and $107$, or say “for sufficiently large $p$.”
- The abstract remains crowded with constants and certificate counts. Shortening it around the support hypothesis, the two incidence arguments, the partial-selection extension, and the relaxation limitation would make the contribution easier to identify; the detailed thresholds are already accessible in the tables.

These are minor wording refinements. The revision remains a meaningful restricted upper-bound result and does not meet the selected problem's solve definition: it neither constructs an unbounded family above $1.8n$ nor excludes such families without the support restrictions.
