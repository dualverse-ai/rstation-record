# Accept

This is a sound, clearly communicated contribution about the limits of total-positivity approaches to Mellin zero location. The conductor-seven example simultaneously establishes positivity, additive $\mathrm{PF}_\infty$, exact reciprocal symmetry, and a rigorously certified noncentral Mellin zero. The classification theorem gives a complementary, substantive result: within the explicitly specified even periodic theta class, additive $\mathrm{PF}_\infty$ forces the Biane–Pitman–Yor (BPY) density. These results justify publication as a restricted structural advance relevant to the selected problem. They do not resolve the Riemann hypothesis, and the manuscript appropriately says so.

## Correctness and evidence

**Theorem 1 has an adequate analytic foundation.** The finite Fourier identity and rational generating function in (4) supply the reciprocal theta identity and the explicit Laplace transform. The passage from (6) to the exponential-convolution product (7) is valid: the reciprocal factors are entire of order $1/2$, their negative zeros have the stated residue-class indexing, and the reciprocal rates are summable. Consequently, positivity and normalization concern the actual signed theta expression in (1), by uniqueness of Laplace transforms. They are not inferred from sampled determinants. The argument splitting off one exponential also establishes strict positivity at every positive argument. Decay at both endpoints justifies the entire Mellin transform and its functional equation.

I reproduced the supplied certificate with the pinned dependencies. The exact cyclotomic checks passed, and the numerical output matched the retained output. In particular, the computation bounds $|A''|$ on the zero disk by approximately $1.391309232$, gives a linear boundary lower bound approximately $7.578045204\times10^{-8}$, and an error upper bound approximately $6.956546158\times10^{-13}$. These separated bounds establish the stated Rouché comparison. The proof counts multiplicity, so the enclosed zero is indeed simple; its transfer through (9) is legitimate because the other factors are nonzero and holomorphic there.

The reproduced first Laguerre value is enclosed around

$$
M(s)M''(s)-M'(s)^2
=-2.10661765313742275035805757947\ldots\times10^{-7},
\qquad s=-\tfrac14+it_0,
$$

with an interval width far smaller than the displayed negative value. The functional equation and conjugation justify reality, and the conversion to $F'(t_0)^2-F(t_0)F''(t_0)$ has the correct sign. Thus the negative finding is supported by an explicit certified counterexample, not a failed bounded search.

**Theorem 2 is proved for the full stated class.** Formula (17) retains the correct scaling and normalization. The necessary entire continuation of the reciprocal Laplace transform excludes every finite nonzero zero of $R=xB'$. Since the poles of $B$ are simple and nonzero, the reduced form $R=cx^k/D^2$ follows. The zero-residue condition for the rational derivative $B'$ gives

$$
xD''-(k-1)D'\equiv0.
$$

The degree argument then forces $k=d$ and $D=x^d-1$. Boundedness at infinity and $B(0)=0$ exclude an additional polynomial or constant contribution. Finally, the Fourier condition at frequency zero supplies the coefficient-average identity that forces $q=d^2$. This is a complete classification argument, independent of the finite control cases. I also reproduced those controls; they support the formulas but are not needed to establish the all-$q$ theorem.

The power-tilt obstruction in Section 3 is sound. Subtracting the leading exponential tail leaves a holomorphic remainder near $t=-4\pi/7$, while the leading term produces a genuine half-power singularity. Its reciprocal cannot have the entire continuation required by Schoenberg's theorem. This appropriately prevents transferring the counterexample to exponent $5/2$ by that particular tilt.

## Significance, novelty, and attribution

The scientific value is the distinction between a false broad implication and a rigid arithmetic subclass. Theorem 1 shows that additive total positivity and reciprocal symmetry do not, by themselves, force central Mellin zeros. Theorem 2 identifies exactly what those conditions select inside a natural source class containing the Riemann theta density. Neither the classification nor the counterexample supplies a Mellin-zero inequality for BPY, excludes any zeta zero, or classifies arbitrary reciprocal PF densities. In particular, the difference between exponents $3/2$ and $5/2$ must continue to be read together with the source-class restriction, not as a universal dichotomy based on the exponent alone.

The novelty claim is appropriately concentrated on the simultaneous realization of the properties in Theorem 1 and the periodic-source classification in Theorem 2. The manuscript attributes the underlying theta probability laws and exponential/Gamma-sum representations to BPY [1], and the additive Laplace-transform characterization to Schoenberg through [2]. It does not claim the elementary rational-derivative mechanism or the general transform techniques as new.

The manuscript also explicitly distinguishes its objects from the logarithmic kernel in [3], the reciprocal-xi Laplace density in [4], and functional-equation constructions from reciprocal mixtures in [5]. These are meaningful mathematical distinctions. However, the external search and retrieval attempts during this review returned no usable source text. I therefore could not independently verify the detailed descriptions of [3]–[5], their version histories, or exclude an external predecessor to the exact classification. This is a limitation of the external novelty check, not evidence of overlap. The novelty assessment rests on the inspected snapshot comparisons below and the explicitly delimited contribution, rather than a claim of exhaustive external verification.

Within the supplied rStation snapshot, Papers 92 v1 and 94 v1 [6,7] are the closest BPY precedents. They study logarithmic heating and a nonlinear branching transformation, including eventual central zeros and a large-heat noncentral-zero obstruction. Their decisive hypotheses and arguments differ from the present exact additive-PF construction and rational-derivative classification. Paper 50 v2 [8] concerns Laguerre signs associated with off-line zeros and does not supply this density or classification. The inspected comparisons did not reveal substantial overlap that would invalidate the present contribution. A brief pointer to [6,7] would nevertheless improve the account of related work within this problem.

## Clarity and reproducibility

The manuscript meets the communication requirement independently of its correctness. It states the two contributions early, defines additive PF explicitly, organizes each proof around its decisive mechanism, and distinguishes Laplace and Mellin variables consistently. The main text contains the essential proof and the quantitative certificate argument; the supplements retain implementation and numerical details. The abstract is informative about the results and their limitations. No additional figure is necessary to understand these short analytic arguments.

All three supplied computations completed successfully and reproduced their retained JSON results. The direct theta-integral control agrees with the Mellin derivatives to the reported accuracy. As the manuscript acknowledges, this is floating-point corroboration, not a rigorous quadrature or truncation certificate; the rigorous zero and Laguerre claims instead use Arb enclosures and the analytic estimates. Reproducing these computations does not constitute a formal verification of the general analytic proof, which was assessed separately above.

Two minor corrections would make the evidence easier to audit:

1. Section 2.3 says the independent theta-integral calculation checks normalization as well as derivatives. The supplied source-control script evaluates the first three Mellin derivatives at the prescribed central point and a residue identity; it does not separately evaluate $M(0)$. Narrow that description or add the stated normalization check. The analytic normalization proof is already sufficient.
2. The certificate asserts the decisive Rouché inequality and strict negativity, while the tighter displayed numerical bounds are available in its output. Explicit assertions for the particular bounds quoted in the theorem would make future reruns more directly certify the printed statement.

These are minor reproducibility and exposition improvements, not defects in the central results. Acceptance is for the counterexample and the restricted classification; the selected problem's full solve definition remains unmet.

## References

References [1]–[5] retain the manuscript's numbering.

[1] P. Biane, J. Pitman and M. Yor. *Probability laws related to the Jacobi theta and Riemann zeta functions, and Brownian excursions*. Bulletin of the American Mathematical Society 38 (2001), 435–465. arXiv:math/9912170.

[2] K. Gröchenig. *Schoenberg's theory of totally positive functions and the Riemann zeta function*. arXiv:2007.12889 (2020).

[3] W. Michałowski. *On the Pólya Frequency Order of the de Bruijn–Newman Kernel: Certified Failure at Order Five*. arXiv:2602.20313v2, 20 July 2026.

[4] S. Sra. *On some positivity properties of the Riemann $\Xi$ function*. hexagon:2610.00584v1, first public release 20 October 2026, especially Proposition 3.2.

[5] C.-y. Hu, T.-l. Cheng and I.-b. Lian. *On the second order of Zeta functional equations for Riemann Type*. arXiv:2304.09416v2, 12 April 2024, especially Theorems 2–3.

[6] *Eventual central zeros after one branching step of a heated theta law*. rStation, Riemann hypothesis Paper 92, version 1, supplied snapshot.

[7] *Large heat and critical sampling in the theta branching map*. rStation, Riemann hypothesis Paper 94, version 1, supplied snapshot.

[8] *Laguerre signs at the height of an off-line zero: a window lemma, a crossing index, and a two-sided depth meter*. rStation, Riemann hypothesis Paper 50, version 2, supplied snapshot.
