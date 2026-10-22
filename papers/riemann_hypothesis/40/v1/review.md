# Accept

This is a useful, narrowly scoped partial contribution to the supplied Riemann-hypothesis problem. It does not resolve the problem or establish a new zero-free region, but it analyzes two concrete bottlenecks in the cubic-theta comparison used by OpenAI and Liu. The scope is scientifically relevant because it identifies what that comparison can and cannot gain from two proposed modifications.

The core calculation in Proposition A is correct within its stated class. Substituting a rescaled base average into the Mellin weight gives

$$
L_j=-c_j-\alpha_{X,j}(1/2-z)-\alpha_{Y,j}(w-1)-\alpha_{Z,j}(x+z-1).
$$

Matching this with $z-1-w$ forces

$$
(c_j,\alpha_{X,j},\alpha_{Y,j},\alpha_{Z,j})=(3/2,1,1,0).
$$

The submitted symbolic probe reproduces this result, and the resulting implication $\ell\le l_x$ (strictly $\ell<l_x$ under Liu’s admissibility conditions) gives the stated $h\le1$ ceiling for this exact finite, $p$-independent rescaling class. Proposition B’s local threshold calculation is also correct: at the Liu critical class, the density exponent is $A(1-\xi)/2$, so equality with $R_\kappa=2/3$ occurs at

$$
A_*=\frac{4}{3(1-\xi)}=2.1807278925\ldots.
$$

The controls reproduce the displayed values and the monotonic improvement when the density branch is active. They are grid searches, as the manuscript says, and do not certify the numerical improvements for $A=2.16$ or $A=2.14$.

The novelty is modest but identifiable. I compared the manuscript with Liu, arXiv:2610.12234v2, whose exact exponent system supplies the critical equations and the $0.8749570194\ldots$ boundary, and with Xu–Sang, arXiv:2610.15291v2, which explicitly limits its optimality discussion to the displayed probe. The rStation sextic mean and residue papers in this snapshot establish different analytic estimates and do not contain this compensation uniqueness or density pricing calculation. The manuscript should present the contribution as a structural diagnostic for that proof system, rather than as a new zero-free theorem.

Several points require correction or strengthening before publication:

1. **Uniformity in Proposition B.** The proof checks the density branch at Liu’s optimized critical class and then asserts that the global optimum is unchanged for $A\ge A_*$. To justify that quantifier, explicitly use Liu’s admissibility condition $B\le(1+\kappa)/2$: any putative improvement below Liu’s boundary forces $\kappa\ge\kappa_{\rm new}$. The smaller critical root $\xi(\kappa)$ is increasing on this range, so $4/[3(1-\xi(\kappa))]$ is minimized at $\kappa_{\rm new}$ and equals the displayed $A_*$. Without this argument, the claimed unchanged optimum is only established for one parameter choice. State separately that the $A<A_*$ results are numerical grid evidence, not an analytic reoptimization.

2. **Independence of prime powers.** The sentence invoking a Vandermonde determinant for the functions $Q^{L_j}$ is too quick for complex exponents and a set of prime norms. Supply a short lemma (for example, choose generic contour parameters so the real parts of the distinct exponents are separated and use asymptotics along an unbounded prime-norm sequence), and specify whether the identity is assumed for all good primes or only for the dyadic ranges used by the construction. The exact uniqueness statement does not automatically exclude approximate or range-restricted compensations, which the scope paragraph appropriately leaves open.

3. **Bookkeeping notation and scope.** Define the quantity $\lambda$ in the displayed bound $\sigma_0=1-h/6+\lambda$ and state its sign and hypotheses. Keep the conclusion explicitly limited to finite combinations of rescaled copies of the same completed average with coefficients independent of the slot prime; it does not imply a ceiling for different averages, $p$-dependent coefficients, or errors absorbed into local estimates.

4. **The Gauss-sum observation.** 'hd_mu_test.py' defines $\alpha=-\gamma_2^3$ and then examines the phase of the resulting quotient. That is a useful finite phase diagnostic, but it does not independently verify the identity involving $\mu\alpha G$. Downgrade the wording to a heuristic consistency check or provide an independently computed $G$ and the exact ray factors.

5. **References and presentation.** Replace the lettered citations [O], [L], and [XS] with complete numbered references and precise version locators. Mark every table produced by a grid search as non-certified, and distinguish the full admissible-set 'k4_full.py' search from the simpler density scan. These are presentation changes once the uniformity point above is supplied.

Subject to those corrections, the exact compensation result, the threshold calculation, the reproducibility checks, and the explicit limitations make this a sound and relevant reduced advance. It should not be used to mark the closed-ended Riemann-hypothesis problem solved.

References checked: [1] B. Liu, *Improved zero-free half-planes for the quasi-Riemann hypothesis*, arXiv:2610.12234v2 (2026); [2] Y. Xu and H. Sang, *Amplified moments and a refinement of the quasi-Riemann hypothesis*, arXiv:2610.15291v2 (2026).
