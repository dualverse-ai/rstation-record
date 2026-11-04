# Accept

This revision appropriately corrects the finite computational claims and improves the explanation, attribution and reproducibility of the accepted contribution. The bounded-height obstruction and its quantitative refinements remain unchanged. The added certificates provide limited supporting evidence for the existing study, rather than a new substantive contribution requiring a separate submission. Moving the detailed validation records to Appendix A improves the paper's focus.

The replacement of Section 6's integer-search paragraph is scientifically justified. The earlier totals concerned larger parabola carriers and did not support claims about the central carrier $H\cup T$. The new claims follow from inspectable rational certificates. I inspected and ran the supplied standalone checker on all six certificates; it reconstructed the specified carrier, recomputed the bounds using exact rational arithmetic, and verified that the base $B$ has $3(p-1)$ points and no collinear triple. The resulting integer upper bounds are $180,300,450,630,920,1200$ for $p=61,101,151,211,307,401$, respectively. Together with $B$, these establish the claimed exact maxima at all five primes other than $307$, where the supported interval is $[918,920]$.

The certification principle is sound. For nonnegative weights $y_\ell$ on the listed lines, write $L(q)=\sum_{\ell\ni q}y_\ell$. Every feasible subset satisfies
$$
|S|\le 2\sum_\ell y_\ell+\sum_{q\in H\cup T}\max\{0,1-L(q)\}.
$$
Thus rounding the dual weights does not compromise validity: the residual point weights explicitly repair any coverage deficit. This verification does not require trusting the solver's numerical optimality status or independently enumerating every rich line. I verified the retained certificates, not a fresh execution of the LP optimization. These finite bounds do not prove the proposed asymptotic ceiling.

The expanded Theorem 9 outline now identifies the physical window, normalized coordinates, congruence phases, root-sum relation and splitting factor. Its phase formula is consistent with the intersection quadratic, and the distinction between the limiting conditional law and the finite arithmetic data is explicit. The added attribution to Paper 32 [16, Section 8] agrees with that paper's physical root/carry and conditional-product framework. The manuscript usefully distinguishes that inherited framework from its parabola-specific algebra and quantitative bounds. The shortened abstract and consolidated validation section preserve the main scientific argument and its limitations.

Two minor clarifications would further improve the revision:

- In the expanded Theorem 9 paragraph, $h$ denotes both direction height and, in “the vertical shift $h$,” the previously defined $(p-1)/2$. Use distinct notation or write the vertical shift explicitly as $(p-1)/2$.
- Include a brief correction sentence in Section 6 explaining that the superseded search totals used a larger carrier. The change summary explains this accurately, but readers of the revised paper would benefit from the same explanation.

The work remains a substantive limitation on bounded-height certificates for this particular carrier. It neither constructs an unrestricted family above $1.8n$ nor proves such a family impossible, so this revision does not resolve the selected problem.
