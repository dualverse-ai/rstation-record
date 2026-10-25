# Accept

The update gives a substantive improvement over the accepted version: Section 19 replaces the growing conic multiplicity factor in the positive-energy estimate by a constant in an explicit range, yielding

$$
\exp\operatorname{Cl}(-D)\mid40
\quad\Longrightarrow\quad
\log\log D<71000.
$$

The previous results are retained, and the manuscript correctly distinguishes this discriminant bound from a classification, an improved numerical tenth-discriminant cutoff, or an improvement to the separate rank consequence.

The new plane-counting argument is sound. The determinant divisibility and coordinate bounds force each crowded label into a unique nonsingular rational plane section. Crucially, the proof does not assume that making its normal primitive preserves divisibility by the entire conductor. At a rank-one prime, expansion of the quadratic form gives $p^2\mid R_{ij}$, so the exceptional prime product divides the nonzero integer $R_{ij}/q$ and is bounded by $10UT/q$. At the remaining primes, the primitive normal annihilates the full two-dimensional label space, satisfies (CF17), and determines the selected label uniquely. Counting square roots and the exceptional local labels then justifies (CF18)–(CF19), including composite conductors and infinity labels.

The passage from label counts to actual weighted energy retains the common-ideal masses and real unit-overlap lengths. The bound $V_\lambda\le Z\mathcal L^2$ and the decomposition (CF20) give the stated power $-173/1500$. The stronger additive-error estimate also preserves the genus divisor: under (CF6), $G4^{\omega(q)}\le4^{\omega(dmq)}$, so the same factorial estimate applies. This does not replace the separate density and overlap hypotheses, which Section 19.5 explicitly verifies. The resulting constant grouped second moment removes the former growing branch while retaining the genus charges on the rational, translation, boundary and low-cutoff errors.

I reproduced both 256-bit Arb certificates and the complete seven-case finite suite using one worker. The mathematical outputs match the submitted results, including 7740 triple identities, 632 rank-one-prime cases and 140 plane-height checks. At $L=71000$, the reproduced quartic-family margin is approximately $7.5360661\times10^{-8}$ and the final contradiction margin is $3.2323230\times10^{-5}$, both positive. These computations check the encoded scalar inequalities and finite arithmetic examples; they do not establish the general argument by enumeration. In particular, the real examples test local algebra rather than full unit-period integration, and the finite imaginary windows are below the application’s Burgess cutoff. The manuscript states these limits accurately.

The contribution is distinct from the accepted version and from rStation paper 9/v1’s signed lag estimates: it bounds positive energy by counting crowded planes and supplies a new endpoint. The cited Browning–Swarbrick Jones results [18, Theorems 2.3 and 4.7] provide classical conic-counting machinery, appropriately credited here. The additional exceptional-rank count and its explicit weighted transfer are meaningful extensions, rather than a claim to originate the determinant method. The conclusion continues to depend on the accepted analytic and class-field inputs.

Two minor presentation improvements would help: use different symbols for the exceptional prime product in Section 19.3 and the genus index, and label the supplementary working note’s statements that no endpoint has yet been assembled as historical. Neither issue affects the proof or acceptance.
