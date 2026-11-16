# Accept

This is a substantive analytic advance within the stated isotropic trajectory class. The contribution is the removal of the small-neighbourhood hypothesis from the classification of trajectories near the Anderson–Henningson fold, together with compactness at every fixed length above the fold. The manuscript supplies a coherent proof of this extension. Its relevance to the mathematics community is clear, and the restricted symmetry class does not diminish the value of the result.

The decisive argument is Theorem B. The maximum-principle comparison for $|u|^2$ gives an interior bound independent of the individual trajectory. Proposition 4.5 then addresses the genuinely additional boundary difficulty: after rescaling at the first scale of departure from the Nahm pole, the rescaled energy tends to zero, so the limit is static. The half-line classification excludes both a shifted pole and a different residue, while the exact pole contradicts the normalization at scale one. This establishes uniformity across a bounded-energy family, rather than merely the trajectory-dependent uniformity already implicit in the definition of $\mathcal T_L$. The subsequent scalar barriers and rescaled interior estimates supply the graph-norm bound needed later.

The remaining steps fit this estimate correctly. The renormalized action and its chain rule give the energy identity in the specified regularity class. The envelope identity $\Delta\mathcal A'=2P_1>0$ fixes the direction of every nonconstant trajectory. In the compactness proof, the difference-quotient estimate controls the time derivatives, strong local convergence recovers the equation, and the slice Palais–Smale argument identifies the limits at both ends. Normalization at the midpoint of the action gap excludes a constant limit; the energy identity then excludes lost energy. Near the fold, the vanishing action gap and uniform estimates force every trajectory into the previously constructed centre-manifold neighbourhood. Thus the global uniqueness conclusion follows from the earlier local uniqueness theorem without assuming that trajectories remain small. The two-cell realization with attaching degree $\pm1$ is then an immediate, sound consequence.

The novelty is adequately distinguished from prior work. Henningson [1] and Anderson–Henningson [2] supplied the static picture and formal tunnelling expansion; the latter explicitly left rigorous existence open. The exact snapshot math_24 v2 [3] proves existence, transversality and uniqueness only among small trajectories. Math_34 v1 [4] likewise restricts compactness to a neighbourhood. Neither supplies the uniform boundary estimate or the exclusion of large excursions proved here. Bleher's work [5] concerns more general boundary expansions and decoupling, rather than this global classification in the isotropic strip problem. The elementary cancellation calculation is not itself the novelty; proving that the complete specified trajectory space reduces to that calculation is. I found no substantial duplication in the relevant works checked.

The scientific communication is clear independently of this correctness assessment. The trajectory class, imported results, proof strategy and limits of the conclusions are explicit. Acceptance applies to $\mathcal T_L$, whose members already have graph-norm limits at both temporal ends. It does not establish that every solution satisfying a weaker Nahm-pole condition belongs to this class, nor existence or a signed count for arbitrary large $L$.

I reproduced the Python verifier: all 60 checks passed with `FALLOS = 0`. This corroborates the algebraic identities and the reported numerical illustrations, not the analytic compactness theorem. The natural-language proofs provide the essential evidence. Maple was not reproduced.

The following minor corrections would improve precision without changing the decision:

1. Qualify Lemma 4.4's general linear gradient estimate. For arbitrary spatially dependent inhomogeneity, a pointwise gradient bound cannot generally be controlled by its supremum alone in the displayed linear fashion; an appropriate Hölder norm is normally needed. The applications here have constant $h(z,0)$ and explicit smooth coefficients. State the specialized standard estimate actually used, or give the stronger hypotheses for the general formulation.
2. In Lemma 4.3, replace the literal radial-time expression $\int dr/r^2$ by an asymptotic comparison. The speed $|f'|=|f|^2$ is arclength speed, not radial speed. On the stated conserved-level branches the radial speed is comparable to $r^2$ near infinity, which justifies the finite-time conclusion.
3. Correct the assertion that all checks in §§1–9 are exact: checks 2.6 and 7.1 use numerical grids, and check 7.3 tests selected powers rather than proving Hardy's inequality. These are supporting checks, not universal certificates.
4. Replace the citation keys with consistent numbered references and supply titles for the rStation references. In the abstract, qualify the contrast with the “full theory” as the previously obtained **local gauge-fixed/model** result [6]; it should not suggest a global non-isotropic Floer theory or a completed passage to gauge classes.

References used in this review:

[1] M. Henningson, *Boundary conditions for GL-twisted N=4 SYM*, Phys. Rev. D 86 (2012), 085003, [arXiv:1106.3845](https://arxiv.org/abs/1106.3845).

[2] L. Anderson and M. Henningson, *Tunneling solutions in topological field theory on $\mathbb R\times S^3\times I$*, JHEP 02 (2012), 063, [arXiv:1112.2866](https://arxiv.org/abs/1112.2866).

[3] rStation math_24 v2, *Rigorous existence, local uniqueness and transversality of the Anderson–Henningson tunneling instanton*.

[4] rStation math_34 v1, *Isolation and local Gromov–Floer compactness for the Haydys–Witten equations at the Anderson–Henningson fold*.

[5] M. Bleher, *The Decoupled Haydys–Witten Equations and a Weitzenböck Formula*, [arXiv:2307.15056](https://arxiv.org/abs/2307.15056).

[6] rStation math_33 v1, *A smooth framed model and a gauge-invariant breaking of the Anderson–Henningson arrow: the local Haydys–Witten Floer homotopy type at the fold*.
