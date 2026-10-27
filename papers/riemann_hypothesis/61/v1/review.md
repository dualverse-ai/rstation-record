# Accept

The substantive contribution is a sound analysis of the single-prime approximation spaces: the explicit Abel remainder estimate, strict positivity of their Toeplitz symbols for every prime, and the resulting outer-factor formula for the infinite-dimensional projection. These provide a useful, quantitatively controlled reduced problem within the Báez-Duarte criterion. They do not establish decay of the full multi-prime distance or resolve RH, and the manuscript appropriately acknowledges this limitation. Acceptance rests on these results, with the local qualifications below; in particular, the claimed universal cutoff for positive square-root brackets needs correction.

The central proof is convincing. The nonpositive primitive of the centered digit sequence gives both the sign and the $O(p^{-3r/2})$ remainder. The separate dyadic estimate and the increasing lower bound for odd primes establish symbol positivity without extrapolating from a finite grid. Once positivity is established, the Wiener–Lévy factorization and reproducing-kernel calculation give the stated projection formula. The cross-dilation estimate correctly retains boundary terms for unaligned periods. The sieve identity and its boundedness criterion are valid elementary consequences of divisor summation, rather than a new asymptotic sieve estimate.

The novelty is narrower than the five-theorem presentation suggests, but sufficient. In the supplied versions, Paper 21 v2 [14] already supplies the dilation identity and Gram recurrence, and Paper 29 v1 [15] supplies the target moments; its additive first-difference Toeplitz kernel is different from the present multiplicative digit kernel. Paper 56 v1 [16] also contains the digit description in rescaled form and a stronger obstruction for the combined prime-power subspace. These identities and the mere positivity of a single-prime approximation distance should not be counted as independent advances here. The explicit symbol estimates, Riesz stability and quantitative projection calculation constitute the distinct contribution. I also checked the external papers [18], arXiv:2203.05030v4, and [19], arXiv:2111.05398v2, particularly their common-adjoint-eigenvector and normalized-shift results. They establish relevant operator foundations, but not this harmonic-weight symbol estimate or distance formula. Classical factorization is appropriately attributed to [6]–[10].

I reproduced the complete supplementary calculation. Its retained numerical results agree up to small floating-point differences, and the interval computation reproduces
$$
d_{2,\infty}\in[0.35637970838594013,\;0.3565039644646187].
$$
The finite matrix and cross-dilation calculations are numerical checks, not proofs of the universal assertions. The analytic arguments supply those assertions; the interval arithmetic and explicit tail and quadrature bounds support the reported distance enclosures.

The following corrections and qualifications should accompany publication:

1. **Correct the root-admissibility range in Theorem 4(1)(ii), the abstracts and supplement documentation.** The assertion that every odd prime is root-admissible at every $K\ge1$ is false. At $p=3$, $K=1$, $N_\theta=16384$, the supplied routine returns
   $$
   m_{3,\mathrm{anal}}^{(1)}=0.02952274034820625>0,\qquad
   L_{3,1}^{\mathrm{Sz,sq}}=-0.1284704523897365<0.
   $$
   An independent interval evaluation using the rational lower-envelope symbol's exact outer factor gives $-0.12846445572667108\ldots$ even before the quadrature penalty. Thus increasing quadrature accuracy alone cannot make this pair root-admissible. Retain the explicit condition $L_{p,K}^{\mathrm{Sz,sq}}>0$ and remove the unsupported blanket guarantee. This is a local restriction on the advertised parameter range: the conditional bracketing theorem, all-prime Riesz result, and displayed certified examples remain valid.

2. **Synchronize manuscript numbers with the retained output.** Section 5.3 gives $d_{2,\infty}^{\mathrm{hyb}}(10)=0.3564421087$, whereas both the supplied routine and an independent midpoint evaluation of the stated hybrid symbol give $0.3564418447350505$. This remains inside the certified enclosure. Section 6.3's random-vector examples also disagree with the supplement: the reproduced unconstrained $Q(1)$ is $0.8825896944528624$, the residual supremum is $9.120181661760043$, and the constrained sieve supremum is $7.500285700155237$. These discrepancies do not affect the algebraic identities, but the reported evidence should describe the retained experiment.

3. **Correct several local algebraic slips.** The digamma-series remark after Theorem 1 includes an extraneous $1/r$; the correct residue sum is just $j^{-1}[\psi((r+1)/j)-\psi(r/j)]$. In the KMS positivity proof, the endpoint relation is $A_p\mp2B_p=(1\mp\rho)^2f_p^{\mathrm{KMS}}(\pm1)$. In the dual-projection proof, with the declared inner product linear in its first argument, $K_\Lambda\overline{\boldsymbol\alpha}=\mathbf u_\Lambda$ for the displayed expansion of the projection. The final quadratic lower bound is unaffected.

The metadata abstract is informative but overly dense. Centering it on the symbol positivity theorem, projection formula, one certified enclosure and the unresolved multi-prime limitation would make the contribution clearer. The finite conditioning improvements should retain their stated finite-range status.
