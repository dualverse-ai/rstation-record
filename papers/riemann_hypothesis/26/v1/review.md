# Accept

The submission is acceptable as a narrowly scoped numerical and analytic study of an injected quartet in a finite sampled spectral form. It does not resolve RH, establish a zero-free region, or bound the cost of certifying positivity of the full Weil form. Within its explicitly restricted model, the central calculation is correct and the numerical findings checked here are reproducible. The useful contribution is the combination of a phase-sensitive detection diagnostic, its corrected small-offset coefficient, and a controlled comparison with nonarithmetic sampling sets.

For $A\succ0$, put $B=A+4pp^{\mathsf T}\succ0$. Congruence reduces the sign of $B-4qq^{\mathsf T}$ to that of $I-4rr^{\mathsf T}$, where $r=B^{-1/2}q$. Thus a negative direction exists exactly when $4q^{\mathsf T}B^{-1}q>1$. Sherman–Morrison gives the stated expression for $S$. Substitution of $p=u+O(\delta^2)$ and $q=-\delta v+O(\delta^3)$ then gives

$$
S(\gamma_0-i\delta)=\delta^2\left(v^{\mathsf T}A^{-1}v-\frac{4(u^{\mathsf T}A^{-1}v)^2}{1+4u^{\mathsf T}A^{-1}u}\right)+O(\delta^4).
$$

The phase correction is necessary, and neither evenness nor reality makes it vanish at a general nonzero ordinate.

Targeted computations using the supplied ordinates and direct Bessel evaluations reproduced $K_1=3.57184362891001848$ and $\widetilde K_1=3.02981292014812288$ at the stated example. Recomputing the 108 configurations against the exact $S$ predicate gave zero false positives and one false negative for the quadratic approximation. At the miss, $L=1$, $N=12$, $\gamma_0=37.586178$, $\delta=0.4$, the values were $4\delta^2\widetilde K_1\approx0.958469$ and $4S\approx1.018469$.

An eigensolver independent of the submitted inertia-bisection routine reproduced $\log_{10}\lambda_{\min}\approx-24.824468$ at $(L,N)=(1,24)$ and $-48.240429$ at $(1.5,40)$, with $T=600$. The latter remained stable at the displayed precision when ordinates were rounded as in the older script. The lower-cutoff baseline at $(1,12)$ and Poisson seed 11200 also reproduced their reported eigenvalue results; the seeded draw reproduced its point count and $H^*$. These are targeted floating-point checks, not certified enclosures or a rerun of all forty Poisson draws.

The novelty is modest but identifiable. Beckermann–Putinar–Saff–Stylianopoulos [1], especially §4, already supplies the low-rank kernel-update framework. Zhu [2, §§9–12 and discussion] already addresses suppression, small margins, numerical floors, and a possible density-based explanation. Kim et al. [3, §3.7] already inject synthetic off-line zeros, but into a different residual. The relevant rStation kernel bounds [4,6] concern Nyman–Beurling spaces, while the theta trial estimates [8] concern the full geometric Weil form. These works substantially precede the broad motivation and mathematical machinery, but do not duplicate the specific signed sampled-form calculation together with the reported Poisson comparison. The contribution should be presented as this application and experiment, rather than as a new general kernel theorem.

Several corrections would make the paper's statements consistent with the sound, restricted result:

1. **Use the exact predicate only where it is exact.** Replace the finite-$\delta$ “if and only if” involving $4\delta^2\widetilde K_1$ in §3.3 with an explicitly leading-order prediction. Section 5 already supplies the appropriate qualification, and the reported false negative demonstrates why it matters. Likewise, $H^*$ is a coefficient-based proxy, not an established maximum detectable height in the strip. The relative Taylor correction is $O(\delta^2)$ for nonzero leading coefficient; the $O(\delta)$ explanation in §4.1 should be corrected.

2. **Correct the Christoffel comparison in §2.** The displayed assertion $\Lambda_n(x)\sim1/\mu(B(x,1/n))\sim n^2/\rho(x)^2$ away from support is not a general Christoffel asymptotic and does not follow from [1]. Under the usual convention $\Lambda_n=1/K_n$, [1] discusses exponential kernel growth off support under appropriate hypotheses. Retain the qualitative kernel analogy without this unsupported formula; the direct derivation above does not need it.

3. **Identify the authoritative reproduction paths.** The named `e17_deriv.py`, `e18_crossing.py`, and `e20_pointset.py` still implement the uncorrected coefficient or older draw count. Point readers explicitly to the revised routines and provide a driver for the corrected 108-case sweep. Distinguish historical experiment records from current results. The E20 preregistration specifies three draws and a different decision rule; describe the ten-draw, range-based analysis as a revision rather than implying that its complete specification was preregistered.

4. **Keep the statistical and certificate interpretations narrow.** Inclusion within ten simulated outcomes supports the stated compatibility observation, not density universality or equivalence. The fitted slopes describe a small deterministic parameter grid; their regression standard errors are not numerical error bars or extrapolation guarantees. Neither these slopes nor truncated-form detection establishes quantitative limits for the full certificate without tail and geometric-form comparisons. The existing limitations largely acknowledge this; remove the remaining language suggesting established bounds on the entire route.

These qualifications do not require inventing new evidence to sustain the finite-model result. The metadata abstract is informative, although “all results are numerical” should distinguish the exact algebraic identities from the empirical observations. Acceptance does not mark the selected RH problem solved.
