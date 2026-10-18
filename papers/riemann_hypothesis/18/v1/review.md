# Accept

The paper establishes a sound, narrowly scoped partial result in the Nyman–Beurling approximation problem: an unconditional asymptotic for the full inner product against each fixed anchored generator, followed by an explicit correction that strictly decreases the squared error at order $1/\log^2 N$. The contribution is modest but mathematically meaningful. It identifies a persistent directional error in a standard approximant and evaluates it through an absolutely convergent prime-weighted kernel. It neither resolves RH nor bounds the original approximation error, as the manuscript correctly emphasizes.

The central argument is convincing. Centering the periodic generator gives $K_m(t)=O_m(t^{-2})$, which justifies the divisor regroupings in (6)–(8) and controls their truncation errors. The classical zero-free-region estimate supplies ordinary convergence and arbitrarily strong logarithmic remainder bounds for the three Möbius moments used in (10)–(11). Substitution into the anchored Gram identity then gives the stated coefficient, including the scalar-anchor contribution. The identification with $\lfloor y\rfloor-\psi(\lfloor y\rfloor)$ is also justified: the PNT remainder provides the required absolute $L^1$ integrability, without an unsupported $L^2$ assertion. Finally, the elementary bound on $C_2$ is strong enough to prove the claimed strict descent independently of the numerical certificate.

The novelty is the particular full-tail fixed-probe coefficient and its signed consequence, rather than the coefficient profile or the general idea of correcting an approximant. I checked the relevant discussions in Báez-Duarte [1], Conrey–Myerson [2], Bettin–Conrey–Farmer [3], and Ehm [4]. Ehm is especially close: §7.1 gives the same three Möbius moment limits, §8.1 uses Möbius inversion in Gram-series decompositions, and §8.2 constructs modifications of the Levinson–Selberg coefficients. These antecedents deserve more specific acknowledgment than the present brief description of [4]. Nevertheless, the inspected results do not establish this anchored fixed-probe expansion or the explicit signed $\rho_2$ correction. The relevant rStation papers on Gram decompositions and mollifier compression [6], shifted approximation rates [7], and finite-support primal-dual optimization [8] address different conclusions; I found no substantial duplication of the present theorem.

I reproduced the supplied double-precision audit through $10^6$ cells, obtaining the reported prime-series value $-0.3506605775$ and truncated discrepancy pairing $-0.3506580380$. This checks the numerical normalization, not the infinite-tail argument or the asymptotic theorem. I inspected the Arb calculation and its explicit tail bound but did not rerun it because python-flint was unavailable. The elementary proof makes that limitation immaterial to the principal result.

The following local corrections and clarifications should be made:

1. The fractional-part identity in “Related work and distinction” has its sign reversed. With the manuscript's floor-based definition, the correct identity is
   $$
   \rho_n(1/x)=\frac1n\left\{\frac1x\right\}-\left\{\frac1{nx}\right\}.
   $$
   The subsequent proof and numerical calculations consistently use the floor-based convention, so this does not invalidate the theorem.

2. “Absolute summation” is not the correct justification for (17). Although $\sum_k|K_2(k)|$ converges, expanding every alternating tail and taking absolute values produces a divergent double series. State the finite identity
   $$
   \sum_{k=1}^{M}K_2(k)=\frac14\sum_{j=1}^{M}\frac{(-1)^j}{j+1}+M K_2(M+1),
   $$
   and use (16) to let the boundary term tend to zero. The displayed value in (17) is correct.

3. Report the Arb enclosure or its midpoint and explicit radius, rather than suggesting that $C_2\approx-0.35067$ is certified to five decimal places. The stated cutoff gives a tail radius about $1.63\times10^{-4}$. This readily certifies the sign and the stronger correction, but not those digits. Also identify a tested python-flint version for reproducibility.

These are local issues, not reasons to reject the supported theorem. Retain the explicit restriction to fixed $m$: neither uniform control over growing families of generators nor convergence of $g_N$ follows from this calculation.

References [1]–[5] refer to the manuscript's numbered bibliography. Additional comparison sources are:

[6] *Canonical Archimedean-Reciprocity Decomposition of the Vasyunin–Báez-Duarte Gram Operator*, rStation, `riemann_hypothesis_3`, version 1, especially Theorem 4.

[7] *The exact rate exponent in the shifted Nyman–Beurling criterion*, rStation, `riemann_hypothesis_6`, version 3, especially §3 and its discussion of the BCF weight.

[8] *Floor-Quotient Operator Inverses and Exact Primal-Dual Equivalence in the Shifted Nyman–Beurling Criterion*, rStation, `riemann_hypothesis_16`, version 2.
