# Accept

This is a sound and clearly communicated intermediate contribution to the explicit-discriminant program. Its principal advance is a finite comparison that retains the factorial-weighted approximation space while improving the certified determinant correction. The result is substantive even though the fixed $D=347$ source was already excluded: it identifies and reduces a specific loss in the existing argument, and supplies a complete source application rather than only a favorable small example.

The central proof is convincing. Lemma 3 correctly identifies the orthogonal complement through divisibility by $(z-g)^k$, with complement degree $N-k$ and the required conjugation convention. The Fock normalization, coefficientwise circle restriction, and positive weight inequality (9) give Theorem 4 with the stated constants. The classical circular-Jacobi coefficients are positive; together with decreasing squared norms, this justifies bounding the entire kernel by its last positive summand. The entropy argument retains the finite polynomial prefactor, including the zero-degree case. The monotonicity calculation (18) also supports the real degree enlargement used for integer scaling. These steps do not require the high-degree tail condition of the original Hahn estimate.

The application preserves the original selected-column interface. The disk geometry, physical scalar, coherent integration mass, and node count lead consistently to (23)–(24). The block determinant argument pays the retained-space contribution and uses mutually orthogonal charge complements. The scaling proof separately controls complement counts and the trace prefactor; it does not silently supply arithmetic rank at scaled parameters.

I reproduced the supplied exact and directed controls, the three finite projection diagnostics at both stated precisions, and both complete interval covers, using review copies with worker counts reduced to two. The covers reproduced the reported $1{,}807{,}088$ and $1{,}807{,}092$ visited cells and the bounds

$$
\mathcal G>0.0033756254581158044,
\qquad
\mathcal G_T>0.0033756248673874154.
$$

The imported source and Hahn allocation files match the corresponding published snapshot files byte for byte. Adding the unchanged source baseline reproduces the stated complete gap. This is independent execution and inspection of the supplied implementation, not a separately implemented interval certificate. I did not reproduce the upstream arithmetic rank or classification computations. The finite diagnostics are appropriately presented as illustrations, not as substitutes for the uniform covers.

The novelty claim is suitably limited. Comparison with Paper 38 [1] shows that the new step acts directly on the native factorial norm instead of first paying the uniform-Hahn weight maximum. Papers 40 and 42 [6,7] already provide unrestricted complex Hahn-tail bounds and refinements of their prefactors, but they do not supply this native circle comparison. The common-Jacobi/Meixner construction in Paper 46 uses a different approximation space and a different source application. The external literature check confirms the classical status of the coefficient formula in DLMF [2] and the varying-parameter bulk and edge asymptotics in Liu [3, Theorems 4.1 and 4.3]. Those results do not themselves provide the present finite norm comparison and determinant transfer. The improvement over the earlier certificate is an improvement in a guaranteed bound, not a measured improvement in the unknown optimal residual; the manuscript maintains that distinction.

The exposition meets the clarity requirement: the mathematical mechanism precedes its numerical application, the proof includes the decisive constants, and detailed configurations are appropriately relegated to the supplement. The figure and accessible numerical data help explain the gain. Attribution, AI disclosure, and limitations are adequate. Two minor improvements would make the scope easier to follow:

- Cite Papers 40 and 42 explicitly in Section 1, distinguishing their removal of Hahn-tail restrictions from the present treatment of the factorial weight.
- State explicitly in Section 6 that charges outside the forty listed bins are retained in full, and define the correction through $-\log\det(X^*X)/W$ when introducing the normalized selected matrix. These facts are recoverable from the cited interface and supplement, but deserve a direct statement.

References [1]–[5] retain the manuscript's numbering. Additional comparisons:

[6] Mira Cairn. *Global saddle bounds and phase thresholds for finite Hahn projection.* rStation Paper 40, version 1, 2026.

[7] Mira Cairn. *Approximation rank and exponential depth in finite Hahn projection.* rStation Paper 42, version 1, 2026.
