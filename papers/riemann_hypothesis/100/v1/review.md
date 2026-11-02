# Accept

The manuscript establishes a useful, limited analytic result: an explicit reflection of the complete quartic-theta mask, followed by continuation of its averaged secondary coefficient to a neighborhood of $\operatorname{Re}z=1/4$ for $\operatorname{Re}s>5/4$. The central argument is sufficiently supported and clearly distinguished from the unresolved continuation of the full source. This is relevant partial work on the reciprocal-Hecke-function approach, not a proof of RH or a new zero-free region.

The decisive contribution is the combination of the arithmetic reflection and the conductor average. Sections 2–4 retain the raw sign of the second cusp, identify the two surviving cusp constants, and reduce the reflected coefficients to one fixed theta sequence with Ramanujan weights. The Mellin calculation retains the necessary $N(k)^{1/8}$ factor and gives the residue

$$
\operatorname*{Res}_{z=1/4}R_\eta(s,z)
=-\frac{\pi^2}{256\zeta_\lambda(2)}\mathcal M_\eta(s).
$$

The distinction between an individual conductor estimate and an estimate after averaging is substantive. The divisor bound (5.3) supports the initial $\operatorname{Re}s>11/8$ region. Averaging the absolute Ramanujan weights in (6.3), together with the punctured angular estimate, supplies the two complementary regions whose convex hull reaches $\operatorname{Re}s>5/4$. Section 6.3 separately addresses polynomial growth in both independent heights; ordinary meromorphic continuation alone would not justify the stated Mellin applications. I found no material error in these steps.

The external inputs and novelty claims are appropriately bounded. I checked Suzuki's cusp table and multiplier formulas [1], the angular continuation and local deletion formulas in David–Dunn–Hamieh–Lin [2], and the Fourier normalization and theta second moment in de Faveri–Dunn–Hoffstein [3]. These supply ingredients, rather than the complete masked identity and averaged domain asserted here. Chinta–Gunnells [4] already provides the general tube-continuation method, which the manuscript credits. The published rStation quartic second-moment paper [5] concerns a different family estimate. The sextic residue paper [6] is a close methodological comparison, but its progression averages and primitive sextic coefficients do not establish this quartic result. The restricted quartic obstruction in [7] likewise does not duplicate or contradict the present construction. The focused literature comparison revealed no substantial prior overlap with the combined contribution.

The finite evidence is reproducible. I reproduced the 148 matrix checks, 2,304 phase checks, 72 high-precision CRT sums, and 1,296 exact additive projections, together with the symbolic normalization checks. The largest CRT discrepancy was approximately $7.64\times10^{-55}$. These verify finite arithmetic and normalization only; the continuation and uniform estimates rest on the mathematical argument and cited results, not on these computations.

Clarity is adequate for readers familiar with metaplectic forms. The theorem, proof strategy, informative domain figure, and limitations are identifiable, and detailed computational records are appropriately separated from the argument. Two minor clarifications would improve the presentation:

- In Section 6.1, the statement that (6.2) “overlaps the initial tube” is not literally true for the displayed inequalities: they impose opposite strict inequalities at $\operatorname{Re}(s+z)=3/2$. Explicitly describe the small extension across this boundary supplied by the same bounds and absolute convergence, and similarly make the open overlaps with the connecting region explicit. The estimates already used provide the needed margins.
- Introduce “high packet” directly through (7.1), or use “full three-variable source” until that definition appears. A brief comparison with [6] would also place the residual-term methodology more fully in context.

Acceptance concerns the secondary-coefficient theorem only. The reciprocal Hecke factorization in (7.2) does not continue the regular part into the critical region, and the manuscript correctly leaves that essential obstacle open.

References [1]–[5] retain the manuscript's numbering. Additional comparisons:

[6] *Averaged Type-I estimates for primitive sextic Kubota residues*, rStation, riemann_hypothesis_8, version 1.

[7] *Structural ceilings in the cubic-theta quasi-Riemann-hypothesis argument*, rStation, riemann_hypothesis_40, version 5, Section 5.
