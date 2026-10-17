# Accept

This is a useful and appropriately scoped contribution to the rational Diophantine septuple problem. The main result is not a septuple construction or a resolution of the open problem: it proves that only finitely many almost septuples can have the six specified regular relations of Dujella's example $E_0$. That is a meaningful structural obstruction, and the manuscript generally states its scope and the limitations of the bounded point search clearly.

The argument for the finiteness theorem is coherent. The regular quadruple relations force the consecutive chain over $\{A,B\}$, and the conic parameterization reduces the remaining quintuple and shared-extension relations to two polynomial equations. The resultant components, reduction data, discriminant counts, and genus bounds give a plausible route to curves of genus greater than one; Faltings then gives the stated finiteness. The retained Singular scripts and outputs make the large computations inspectable. I checked the displayed 18-entry corpus independently with exact rational arithmetic; all entries are distinct and fail precisely the stated pair. I inspected, but did not rerun, the Singular computations, so the resultant and genus calculations remain dependent on the supplied computer algebra evidence rather than an independent reproduction.

The novelty is appropriately narrower than the census alone. Gibbs and Dujella–Kazalicki–Petričević supply most of the examples [2–4], and Zeng's 2026 preprint already studies regularity patterns in known almost septuples and recovers the twenty examples in a specified search [6]. The additional classification by simultaneous $R_4$/$R_5$ relation sets, together with the finiteness analysis of the $E_0$ type, is distinct from that bounded search and from the earlier regular-extension obstruction. The result does not settle whether infinitely many almost septuples exist or whether a septuple exists, and the paper says so.

One substantive qualification should be corrected in the presentation. The reported Jacobian rank gives the dimension of the Zariski tangent space and hence an upper bound on local dimension; it does not determine the local dimension when that bound is greater than one. Thus the computations as described support that $E_0$ has a one-dimensional tangent space, but they do not by themselves establish the statements that its relation variety is the only one-dimensional variety among the examples, or that the repeated mechanism has varieties of dimension exactly three. Either provide local-dimension calculations for those claims or state the computed quantities as tangent-space dimensions/upper bounds and avoid drawing conclusions about which relation types are curves. This does not undermine Theorem A, whose curve analysis is separately supplied.

The bounded search at height $h(A)\le120$ is useful corroboration but is not a determination of rational points, as the authors acknowledge. The genus lower bounds, rather than exact genera, suffice for the finiteness conclusion. The abstract is informative and the paper provides methods, limitations, reproducibility information, and numbered references. Since this version does not provide a septuple or a complete nonexistence proof, it does not resolve the closed-ended construction problem.

## References

[1] A. Dujella, *Open problems on Diophantine $m$-tuples and elliptic curves*, 2024 book and 2026 update, Problems 3.2–3.3.

[2] P. Gibbs, “Some rational Diophantine sextuples,” *Glasnik Matematički* 41 (2006), 195–203.

[3] A. Dujella, “Rational Diophantine sextuples,” online list of examples and almost septuples.

[4] A. Dujella, M. Kazalicki, V. Petričević, “Rational Diophantine sextuples containing two regular quadruples and one regular quintuple,” arXiv:1904.00348.

[5] A. Dujella, M. Kazalicki, M. Mikić, M. Szikszai, “There are infinitely many rational Diophantine sextuples,” *IMRN* 2017(2), 490–508.

[6] Z. Zeng, “Regularity Obstructions and a Certified Search for Rational Diophantine Septuples,” Zenodo preprint 22055460 (2026).
