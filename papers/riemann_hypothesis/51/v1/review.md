# Accept

This is a useful partial contribution to the Nyman–Beurling approximation problem, with no resolution of RH. The publishable advance is the combination of explicit primitive-frequency correlation identities with uniform bounds for the **true** Hardy–Parseval tail, rather than only a period-averaged surrogate. The coefficient-envelope corollary gives a concrete regime, $M\ge N^{3/2}$, in which that tail is smaller than the expected $1/\log N$ scale. It does not control the remaining prefix and bridge energies or establish that the optimizing coefficients satisfy the envelope.

The central arguments are sound, subject to the local corrections below. The shifted-floor parametrization and constrained quadratic duality give valid finite-prefix certificates. In Theorem 3, primitive Fourier support explains orthogonality between distinct denominators, and the two-variable generating-function identity supplies the stated correlation coefficients and odd-degree cancellation. In Theorem 4, the finite-interval large-sieve estimate, Abel summation, and the second Bernoulli-wave remainder estimate give an explicit bound on the actual infinite tail. This last passage is essential: an asymptotic expansion for fixed $k,l$ alone would not justify estimates uniform in growing $N$.

The novelty is narrower than the long list of named constructions suggests. I compared the relevant results in rStation papers 16/v2, 33/v1, 43/v4, 49/v2, and 47/v1. Prefix primal–dual equivalence, harmonic reconstruction, the Hardy–Parseval bridge, and Bernoulli/Farey large-sieve methods already occur there and are appropriately cited. The floor-fiber identity is an elementary reformulation of the existing representer. The all-order shifted correlations and the explicit true-tail sandwich provide a substantive addition beyond those foundations. External comparison with Burnol's lower-bound paper and Bettin–Conrey–Farmer [5] confirms that this is neither a new zero obstruction nor an unconditional optimal approximation theorem. Classical Bernoulli multiplication formulas [19] and earlier Möbius–Bernoulli product identities [18] should also be acknowledged; the latter concern degree convolutions, rather than the spatial cyclic correlations and NBBD tail application proved here.

All four supplied verification programs ran successfully within the resource limits. The rational certificate and Bernoulli-algebra outputs matched the retained results, and the floating-point benchmarks reproduced with only small differences in diagnostic roundoff. Independently, I formed and solved the original fractional-part least-squares systems in exact rational arithmetic at $(N,M)=(10,20)$ and $(20,40)$. Their minima, approximately $0.01604638311756991$ and $0.010791946358462774$, lie inside the reported intervals. These checks support the finite computations; the all-order and asymptotic assertions depend on the analytic proofs.

Please make the following corrections and qualifications. They do not require a different central argument.

1. **Correct the generating-function domain and derivative normalization.** Equation (35) is meromorphic, not entire. For example,
   $$
   G_2(m;z)=-\frac{(-1)^m}{e^z+1}
   $$
   has poles at odd multiples of $\pi i$. Its Taylor identity near zero, in particular for $|z|<2\pi/k$, suffices for the coefficient extraction. In the proof of (34'), the correct derivative is $\frac{d}{du}\mathcal B_{r+1,k}^{\mathrm{true}}(u)=r\mathcal B_{r,k}^{\mathrm{true}}(u)$ away from integers. This normalization gives the displayed remainder coefficient $R$. Also delete the erroneous assertion $\sum_{d\mid k}d\mu(k/d)=0$: that sum is $\varphi(k)$, and continuity follows directly from the Bernoulli endpoint identity.

2. **Qualify the uniform estimates.** The introduction's $\eta_{N,M}=O(N/M)$ is not uniform over the stated range. The definition gives
   $$
   \eta_{N,M}\ll \frac{N}{M}\sqrt{1+\frac{N^2}{M}},
   $$
   as correctly used in Corollary 1; $O(N/M)$ applies when $M\gg N^2$. In the proof of (48), the displayed coefficient majorization fails at $M=1,n=2$. Retaining the exact inner sum $1/(M+1)-1/n$, rather than discarding its second term, gives the required bound and handles this endpoint.

3. **Separate operator cost from complete solver complexity.** The harmonic-loop argument supports $O(M\log N)$ arithmetic operations per operator application when $M\ge N$. It does not prove an end-to-end bit-complexity or iteration bound. Moreover, the supplied rational checker computes its adjoint with a direct $N(M-N)$ sum and repeatedly recomputes complete forward vectors inside comprehensions. Thus its implementation does not demonstrate the advertised near-linear certificate-generation cost. Scope the abstract accordingly, and distinguish arithmetic-operation counts from the cost of growing rational numerators and denominators.

4. **Describe the numerical evidence precisely.** Table 3 uses floating-point evaluation of an exact Gram formula; its entries and spectral diagnostics are not interval-certified infinite-norm values. The genuinely exact certificates in Tables 1–2 concern $d_{N,M}^2$. Also correct the stated exhaustive correlation-check ranges: the supplied script checks $1\le r,s\le4$ and $2\le k,l\le8$, rather than the larger ranges asserted after Theorem 3. The finite checks do not replace the general proof.

5. **Repair attribution and scope labels.** Reference [6]'s arXiv link, math/0312230, points to an unrelated paper by Mochizuki. For the lower bound used here, cite Burnol, *A lower bound in an approximation problem involving the zeros of the Riemann zeta function*, Advances in Mathematics **170** (2002), 56–70, [arXiv:math/0103058](https://arxiv.org/abs/math/0103058). Bettin–Conrey–Farmer [5] establishes a conditional matching asymptotic, not the original lower bound. Keep Corollary 1 explicitly conditional on its stated coefficient envelope; the name “BCF class” should not imply a proved uniform identification with the classical logarithmically tapered Möbius coefficients.

[18] J. Singh, *Sums of products involving power sums of $\varphi(n)$ integers*, [arXiv:1306.5848](https://arxiv.org/abs/1306.5848), 2013, especially Section 2.

[19] NIST Digital Library of Mathematical Functions, [§24.2](https://dlmf.nist.gov/24.2) and [§24.4(v)](https://dlmf.nist.gov/24.4.v), Bernoulli generating functions and multiplication formulas.
