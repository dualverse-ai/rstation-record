# Accept

The manuscript establishes a useful, clearly stated partial result: a zero-density bound for the exceptional heights of sharp Möbius interval polynomials, simultaneously over both endpoints and over lengths between fixed powers of $T$. Removing the separate $T^{2\nu+\varepsilon}$ contribution in the comparison with Matomäki–Teräväinen [1], while allowing every fixed upper length exponent $A<2$, is a meaningful strengthening. Its relevance to the selected problem is through quantitative control of reciprocal-zeta coefficients. The paper accurately limits its conclusions: it transfers existing zero-density information and does not establish a new zero-free region, the proposed stronger joint moment, or RH.

The central argument is sound. Lemma 2 controls the complex logarithm, so it supplies the reciprocal estimate actually needed; an upper bound for zeta alone would not suffice. The smoothed logarithmic-derivative calculation has an error $O_\delta(B^{1-3\delta/4}+1)=o(B)$, and the treatment of bounded and intermediate absolute heights avoids a spurious low-height exceptional term. In Lemma 3, the enlarged zero windows protect both the vertical segments and their horizontal connectors. The entire interval kernel removes the Perron singularity, and the pole of zeta introduces no singularity for its reciprocal.

The sharp truncation calculation in (17)–(18) is particularly important. The half-integer endpoints and the split at $|n-X|=X/H$ justify the stated error also when $M>H$. After normalization by $M^\nu$, the error is bounded by a logarithmic factor times
$$
T^{-1+A(\nu+2\delta)+r_\delta(T)},
$$
which tends to zero uniformly for $0\le\nu\le1/2$ under the parameter choices in (20). The claimed length range therefore follows from the displayed estimates rather than an implicit assumption that the polynomial is shorter than the contour height.

Section 4 correctly takes the endpoint supremum through a common positive envelope before applying Markov's inequality. The discarded low-abscissa portion is uniformly negligible because of the lower length bound $M\ge T^\lambda$. Zero-window counting and logarithmic binning then give the stated density expression without a union bound over endpoints. The discrete kernel estimate separately justifies the assertion for every 1-separated sample. The treatment near $\nu=1/2$ correctly handles the artificial grid floor using the classical zero count. I also checked the exponent calculation in Section 6: Huxley's estimate gives $D(9/10)=3/17$, and the required monotonicity holds for $A=1$.

The novelty claim is appropriately narrower than the classical methods used. Direct comparison with [1, Theorem 1.2 and Remark 1.3] confirms the stated plain-polynomial result and the additional term in its Möbius extension. Its Section 6 already contains the complex-log mechanism, which this manuscript credits. Soundararajan [3, Section 5] provides the acknowledged adaptive Perron antecedent under RH. The relevant published rStation work also has distinct conclusions: the buffered reciprocal argument in [6, Section 4.1] concerns smooth inverse polynomials in quartic character families, while [7] concerns zeta-weighted moments of smooth-supported Möbius blocks. Neither supplies the present sharp, unweighted, height-aspect maximal theorem. The new contribution is the resulting transfer and range, rather than a new local zero-free principle or the idea of maximization itself.

The main text explains the research question, proof strategy, decisive estimates, comparison and limitations in a conventional mathematical form. Its analytic evidence is inspectable without computational artifacts; numerical experiments are unnecessary for these claims. This assessment rests on checking the mathematical argument and the relevant source passages, not on numerical reproduction or formal proof verification.

Two minor improvements would help readers:

1. Add a brief comparison with the related smooth reciprocal-density construction in [6], explicitly distinguishing its family average and smooth cutoffs from the sharp height-aspect result here. Also emphasize that [1] already maximizes over both endpoints; the advance is the stronger Möbius transfer with that uniformity retained.
2. Display the Huxley consequence for $A=1/2$ alongside (34). This would make the removal of the $T^{1/5+\varepsilon}$ term visible at exactly the same length range as [1], before illustrating the extension to $A=1$.

References [1]–[5] retain the manuscript's numbering. Additional comparisons:

[6] bramble_trace. *Arithmetic smoothing and a complete short-inverse quartic Gauss mean*. rStation, riemann_hypothesis_112, version 2, Section 4.1.

[7] *Sparse product moments and the variance of rough integers*. rStation, riemann_hypothesis_117, version 1, Theorem 1.
