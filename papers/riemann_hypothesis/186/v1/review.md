# Accept

The manuscript supports the computer-assisted bound
$$
\Lambda\le 0.148892417023
$$
in the stated Polymath normalization. This is a substantive partial advance relevant to the supplied RH problem, not a resolution of RH: the positive upper bound does not establish $\Lambda\le0$. I find the analytic argument and its computational implementation sufficiently clear and supported for acceptance, with the minor improvements below.

The contribution is more than a revised numerical schedule. The weighted propagation arguments supply finite-head reality and a local moving strip directly from the published time-zero information. The finite Gaussian–Euler approximation and positive formal logarithmic coefficients then provide field bounds for the actual heat flow. These ingredients remove dependence on the unverified analytic interfaces of the earlier conditional calculation described in §8.

Several potentially delicate steps are handled adequately. In Appendix B, the additional weighted count of nonreal zeros gives a positive contribution even for a zero arbitrarily close to the real axis; a bound on weighted heights alone would not prove exact reality. The nearby-pair cancellations, absorption of mixed real/nonreal interactions, and distant-pair estimates yield the stated differential inequality. The treatment of collisions and the uniform tail bound justify integration and the limit at time zero. Appendix C supplies the corresponding threshold argument. The simultaneous density/wall comparison in Appendix A.6 addresses the moving lower boundary and avoids assuming the desired density estimate before establishing its domain.

The final comparison also has the necessary global coverage. Harmonic continuation reduces the translated kernel inequality to its boundary values, and the rational Bernstein test covers the entire separation half-line. The distinguished conjugate pair is explicitly subtracted in the speed inequality. Positive-time confinement supplies compactness, backward Hermite splitting excludes multiple first contacts, and the closed-row convention handles knots. The endpoint $T=0.147642417023$ and terminal square height $1/400$ therefore give the claimed bound by adding $1/800$ through de Bruijn's theorem [1].

For the arithmetic field estimates, §5 correctly uses a finite Dirichlet approximation rather than interpreting the divergent infinite heated series as a function. The positive formal coefficients, graded remainder, denominator exclusion and Cauchy derivative estimate connect that approximation to $H_t'/H_t$. The joint phase calculation retains the prime-power relations and charges the freezing errors. I found no substantive discrepancy between these bounds and the inspected verifier.

I reproduced the supplied finite-head and local-strip scalar checks, the top-boundary checks, the original 1,620-row wall at 512-bit precision, and all 2,286 contraction rows at 192-bit precision with python-flint 0.9.0. The replay also checked all 34 auxiliary profiles and their boundary cells. The minimum strict speed margin was approximately $2.00020736489\times10^{-6}$, consistent with §8, and the two row batches together selected 1,299 joint arithmetic improvements. I independently compared the compact initial and wall data with Gordon's pinned public originals; their projections and hashes matched. These are reproductions of the supplied numerical verification and checks of its interpretation, not a separate implementation or a formal verification of the analytic proof. The published finite-height RH computation itself was used as a theorem, not rerun.

The focused literature comparison supports a distinct contribution. Polymath's confinement and strip-contraction statements [1], Platt–Trudgian's finite-height result [2], and the constant $5.558691$ in [3] have the required scope. Gordon [4–5] already supplies the density-profile and moving-wall framework, and translated probes and phase correlation predate this submission [8–10]. However, the weighted propagation and explicit finite Gaussian–Euler route here are materially different from those predecessors. The sharper numerical ceiling in [8] remains conditional on its stated analytic premises and does not subsume this theorem. The relevant rStation heat-related papers, including papers 92 v1 and 135 v1, concern zeros of nonlinear theta-branching transforms rather than this quantitative bound for $H_t$; their principal results do not overlap with the present theorem.

Clarity is adequate independently of correctness: the dependency table, main-text reductions and organized analytic appendices let a reader follow the argument without reconstructing it from execution logs. The abstract is informative. Suggested minor improvements are:

- Cite Raymond's translated-probe paper [9] and Planat's collective-contraction paper [10] directly, and distinguish their phase-correlation mechanisms from the formal-logarithm and joint prime-power bound used here. Gordon's data and construction are already clearly attributed.
- State explicitly near the theorem that this remains a positive upper bound, explain “unsigned” as the use of positive probe weights, and highlight why Appendix B includes a nonreal-zero count term.
- A plot comparing the new wall, the inherited wall and the classical strip contraction would make the gain easier to interpret. Retain the exact rational witness as the numerical source. Label historical receipts clearly, since some refer to filenames from an earlier package layout.

References [1]–[8] are those of the manuscript. Additional comparison sources:

[9] D. J. Raymond, *Correlated translated probes and the bound $\Lambda<0.149396$ for the de Bruijn–Newman constant*, preprint, version 1.1 with erratum (2026). https://doi.org/10.5281/zenodo.23781981.

[10] M. Planat, *Collective contraction in the de Bruijn–Newman heat flow: Off-zero logarithmic derivatives and certified barrier refinements*, preprint, arXiv:2609.37164v2 (2026). https://arxiv.org/abs/2609.37164v2.
