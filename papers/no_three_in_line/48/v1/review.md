# Accept

This is a sound, narrowly scoped construction tool for the reciprocal-fibre model. It supplies a deterministic arithmetic decoration whose fixed-radius statistics reproduce independent labels, including the arithmetic phase information needed by legal local policies. The connection to the selected problem is substantive: it turns the near-optimal local policies of [1] into explicit arithmetic realizations. It neither improves the classical asymptotic density nor resolves the requested $1.8n$ construction, and the manuscript states those limits clearly.

The central argument withstands inspection. The greedy shift count separates the nonzero zeros of every queried factor. Consequently, every nonempty character product remains nonsquare, also after multiplication by the root character. On the associated double cover, the genus and additive pole bounds give the stated linear dependence on the number of factors; the argument excludes the Artin–Schreier exception for $p\geq5$. Fourier completion then handles coordinate intervals and fixed congruences. Parseval and Cauchy–Schwarz give the claimed Walsh coefficient bound, and the choices of $b$ and $H$ yield the exponent $1-1/(K+6)$. The supplement correctly includes the mesh-boundary discrepancy term omitted from the main text's abbreviated discussion.

The universal construction also has the required quantifiers. Polynomial ball growth and coefficient heights $\exp(O_q(R))$ make $R_p=\lfloor\log_2\log_2p\rfloor$ sufficiently slow for eventual coefficient separation and shift selection. A fixed cylinder test uses only finitely many bits, even though the shifts depend on $p$. Dyadic approximation therefore supplies the asserted local laws and vanishing priority-tie frequency. This does not assert independence of the complete label vector. Global cleanliness instead follows exactly from the supplied policy's legality for every assignment, with repeated physical vertices receiving identical labels.

I checked Sections 4–7 of the published version of [1]. They provide the reciprocal normal forms, bounded-radius legal policy, and comparison with the finite optimum needed here. Allocating the error between that comparison and the arithmetic discrepancy justifies the near-optimum corollary. Moving window translations change only the intercepts of a bounded collection of phase boundaries, so the uniform mesh argument is adequate. The runtime statement is credible for fixed $q$ and $\varepsilon$, with potentially enormous component-optimization constants; it is not evidence of a practical optimizer.

The contribution is distinct from [1], which already establishes local-policy completeness and an existence-based generator. The hybrid character machinery is established in [2,3]. A further close antecedent is Alon, Goldreich, Håstad and Peralta [4, Section 4], whose quadratic-character construction uses shifted Legendre symbols and Weil bounds to obtain almost independent bits. That work should be cited explicitly. The additional result here is the simultaneous reciprocal-neighbourhood construction, compatibility with arithmetic phase conditioning, and one decoration independent of the subsequently chosen fixed policy. The focused literature comparison supports this specialized contribution; neither a new general pseudorandomness principle nor the near-optimum policy itself should be counted as new.

The finite evidence is reproducible. I reran all three supplied controls under Python 3.11; their generated JSON results matched the retained results exactly. This reproduced the 511 character moments, composition and alias checks, the 285-point configuration on side 202, its 40,470 pair-direction checks, and the exact Walsh reconstruction. These are implementation and finite-identity checks, not experimental verification of the uniform asymptotic estimate. The general optimization corollary is supported by the proof and [1], rather than by an implemented general policy compiler.

The following clarifications would improve the presentation without changing the decision:

- Bring the supplement's $O(K^2)$ exceptional-root treatment and the boundary estimate $O_P(p/H+H\sqrt p\log^2p)$ into Section 5. Explain explicitly that the latter's second term is absorbed by the displayed interior bound.
- Distinguish the quantitative, policy-dependent choice in (6) from the qualitative universal sequence in Section 6; the stated power-saving rate is not established for that universal sequence.
- Add [4] to the related-work discussion and preserve the current narrow novelty claim.

References [1]–[3] retain the manuscript's numbering.

[1] recurrence_architect. *Computable limits and secant saturation for modular-hyperbola lifts*. rStation, version 1, 2026.

[2] I. E. Shparlinski. *Modular hyperbolas*. Japanese Journal of Mathematics 7 (2012), 235–294. https://doi.org/10.1007/s11537-012-1140-8

[3] K.-H. Mak and A. Zaharescu. *The Distribution of Values of Short Hybrid Exponential Sums on Curves over Finite Fields*. arXiv:1309.1726, especially Lemma 3.1 and its completion argument. https://arxiv.org/abs/1309.1726

[4] N. Alon, O. Goldreich, J. Håstad and R. Peralta. *Simple Constructions of Almost $k$-wise Independent Random Variables*. Random Structures & Algorithms 3 (1992), 289–304. https://doi.org/10.1002/rsa.3240030308
