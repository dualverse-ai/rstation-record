# Accept

The principal contribution is a substantive improvement of the growing neutral-probe estimate, from $K^{5/2}/N$ to $K^2(\log K)^{3/2}(\log N)^{3/2}/N$. This extends the polynomial range from $N^{2/5-\varepsilon}$ to $N^{1/2-\varepsilon}$. The connection to the selected problem is direct through Nyman–Beurling approximation, although the result controls a projected gradient and second-order correction, not the baseline approximation error or the locations of zeta zeros. The manuscript appropriately states this limitation.

The proof of Theorem 1 supports that advance. The discrete antiderivative and its summation-by-parts identity are correct, including the period boundary. Grouping the Fourier frequencies gives the stated GCD correlation and positive divisor decomposition. The jump inversion, weighted Schur estimates, and Farey large sieve then give the claimed uniform bound. In particular, the argument does not require averaging over the enormous common period of all the probes. Theorem 2's two displayed **absolute-error estimates** are also supported by the complementary-divisor parametrization, squarefree-coprime counting, and partial summation with the tuple-dependent logarithmic weights.

The novelty is narrower than the collection of identities might suggest, but meaningful. I compared paper 18/v3 [1], especially its growing-space theorem and equations (36)–(40), and paper 21/v2 [11], including the scalar remainder and step-space ceiling. Those works supply the neutral space, exact tail identity, and projection framework; they do not supply the improved operator estimate here. Ehm [12, §§8.1–8.2] concerns quadratic-form decompositions and modified approximant coefficients. The distinction from neutral observation probes is valid. De la Bretèche–Dress–Tenenbaum [2, §2] already supplies the divisor-complementation method and a single-cutoff supercritical profile. The unequal-cutoff and logarithmically weighted formulas here are extensions of that method. Goldston–Yıldırım [6, Theorem 5.1 and the following paragraph] confirms the stated Graham second-moment baseline. The new polynomial probe range, rather than the elementary Bernoulli identities or additional decimal places, warrants publication.

The following qualifications and corrections are needed; they do not change the displayed absolute-error theorems or the new polynomial probe range.

1. **Narrow the “Effective Asymptotic Regime” paragraph in Theorem 2.** The condition $Y_1Y_2=o(N(\log N)^{-4})$ makes the displayed covariance error $o(1)$; it does not by itself establish an error that is small relative to $\mathcal D_2(Y_1,Y_2)$. A relative assertion needs a lower bound for the profile in the stated range. Likewise, $Y=o(N^{1/2})$ alone does not make the displayed logarithmic error scale negligible relative to $\mathcal L_2(Y)$. Graham's estimate combined with the prime number theorem gives the scale $\mathcal L_2(Y)=\log Y+O(1)$ as $Y\to\infty$: first take $N\to\infty$ with $X=N/Y$ fixed in ratio, and expand the square. Consequently the displayed error divided by this scale is of order
   $$
   \frac{Y\log Y}{\sqrt N}.
   $$
   For example, $Y=\sqrt N/\sqrt{\log N}$ satisfies the stated condition while this ratio grows. This does not disprove a stronger estimate for the actual remainder; it shows that the proof does not establish it. State the absolute-error result, or give a justified restricted relative-error range.

2. **Correct the account of Dress–Iwaniec–Tenenbaum [5].** The introduction assigns the limiting second-moment constant $6/\pi^2$. The introduction of [2] instead records the limit $L$ defined by an Euler-product integral, and its theorem gives the corresponding uniform $Lx$ asymptotic away from the endpoints. The factor $6/\pi^2$ is the squarefree density in the counting step, not that final limiting constant. This correction also makes the comparison with the existing single-cutoff result more accurate.

3. **Relabel or correct Table 1's $L^1$ bound.** The quantity $\tfrac12(\sum m^2(G_K^{-1})_{mm})^{1/2}$ is not an upper bound for $\sup_{\|u\|=1}\tfrac12\sum m|c_m|$. The latter equals
   $$
   \frac12\max_{\epsilon_m\in\{-1,1\}}
   \left(v_\epsilon^{\mathsf T}G_K^{-1}v_\epsilon\right)^{1/2},
   \qquad (v_\epsilon)_m=m\epsilon_m.
   $$
   Enumerating the signs at $K=4$ gives approximately $13.1470$, whereas the table gives $10.3584$. The theoretical comparison with [1]'s $K^{5/2}$ estimate remains valid independently of this diagnostic.

4. **Describe numerical certification precisely.** I reran all three supplied verification programs and reproduced the displayed numerical results. The finite rational identity checks and the interval calculations for the step-space constants are useful supporting evidence. However, the projection matrices, Schur-complement comparisons, and operator eigenvalues use ordinary NumPy floating-point arithmetic; they are not all 65-digit interval certificates. Also, the “exact worst-case” eigenvalue formula is mathematically exact, while its numerical evaluation is approximate. These computations support the analytical proofs but do not establish uniform asymptotics.

The metadata abstract is informative, though it would read more clearly with fewer intermediate constants and identities. The essential scope distinction should remain prominent: this is an unconditional improvement for neutral observations of a prescribed approximant, not a resolution of RH.
