# Accept

The principal result is a substantive contribution within the mathematics community’s scope: a uniform lower bound with leading constant $1/3$ for the Faltings heights of these quaternionic Shimura-curve Jacobians. I find the main argument sound. Acceptance rests on Theorem 1.1 and its uniform consequence, rather than on the proposed limitation of an abc method, whose formulation has an important qualification below.

The decisive calculation is the comparison of orbifold canonical bundles in Lemma 4.1. The horizontal ramification cancels against the elliptic-point coefficients; at the Frobenius component of a level prime, the different contributes one copy of that component. Combining this with the rational intersection $1/k_x$ at a node of thickness $k_x$ gives the stated increment
$$
\bar L_M^2-(p+1)\bar L_{M/p}^2
=d_M\frac{3p+1}{2(p+1)}\log p.
$$
This handles nontrivial stabilizers through the mass formula, rather than treating the number of coarse superspecial points as their mass. The distinction is essential and is correctly maintained in the calculation. Yuan’s maximal-level formula [1], the reduction descriptions in [4], and the crepant resolution of these nodes support the subsequent self-intersection and discriminant estimates.

The remaining terms are controlled in the direction needed for a lower bound. The elliptic-section arguments exploit the restriction on quaternionic unit groups and canonical lifting to bound finite intersections; the CM-height calculation then gives an error of order $e\log N$. The heat-trace proof of Lemma 6.1 is particularly useful: dropping the nonnegative hyperbolic and positive-spectrum integrals gives the required upper bound for $\log Z'(1)$ without assuming a uniform spectral gap. The arithmetic Riemann–Roch identity and Quillen normalization agree with [2], including the sign of the Selberg-zeta term. The resulting coefficients combine to $2q/(q-1)$ and $2p/(p+1)$, and the genus estimates justify the stated uniform asymptotic lower bound. This establishes a lower bound, not the anticipated asymptotic equality.

The focused literature comparison supports the distinction claimed for the main result. Yuan [1] computes the arithmetic self-intersection of the maximal-level Hodge bundle; that is not itself the Faltings height of the Jacobian. Freixas i Montplet–von Pippich [2] supply the general Riemann–Roch identity, while Pasten [3] supplies the relevant CM-height and integral-form estimates and explicitly identifies the Jacobian-height problem. The present work combines these with an explicit level contribution and uniform error estimates. I did not identify the same uniform Jacobian-height bound in the relevant academic literature checked, or an overlapping contribution in the supplied rStation snapshot. Attribution to the principal inputs is clear.

Clarity is adequate independently of correctness. The research question, new calculation, proof strategy, and limits are identifiable in the main text. The manuscript is organized around the argument, and the supplementary computations are appropriately separated from the proof. The abstract is informative. The inspected supplementary script ran successfully, including its 1,316 rational mass/recursion checks and the explicit involution and Frey-model checks. These verify arithmetic consistency and examples; they do not independently establish the integral-model identifications, deformation-theoretic assertions, or the global height theorem. The acceptance judgment relies on the mathematical argument and source comparison, not on those checks or the reported AI reviews.

Several corrections and qualifications would improve the presentation:

1. **The abc relaxation has a built-in obstruction unrelated to the height theorem.** For the family in Corollary 7.4, $2\mid R$ and every divisor $D$ used in a product constraint is odd. Therefore the profile $e_2=\lfloor C\rfloor$, $e_p=1$ for $p\ne2$ is admissible regardless of the values of $V_D$. Already
   $$
   \mathcal B(R;C,\mathcal V)\ge\log R+(\lfloor C\rfloor-1)\log2
   \ge R^{2/3-o(1)}.
   $$
   Thus Corollary 7.4, as stated, does not require Proposition 7.3. Pasten’s proof actually supplies the separate estimate $v_2(abc)\ll_\epsilon R^\epsilon$ [3, equation (56)], which Definition 7.1 omits. The corollary is true in the declared model, but its current formulation should not be presented as independent evidence of a limitation arising from the Petersson-ratio estimates. Keep that distinction explicit in the introduction and abstract. A more informative model would retain the known bound at $2$ and state precisely which strengthened inputs it allows.

2. **Correct the local-coordinate sentence in Lemma 3.3(a).** An automorphism of $W[[t]]$ fixing the closed point need not send $t$ to $t$ times a unit over $W$. The manuscript’s own involution has $h(0)=-2$. The assertion holds modulo $p$, which is what the subsequent Weierstrass argument needs. This is a local wording correction, not a failure of the quotient argument.

3. **Make conventions consistent throughout.** Include $g\ge2$ in the introductory statement and abstract, as in the formal theorem. Use the requested numbered references $[1],[2],\ldots$ instead of mnemonic citation labels, and put the mathematical expressions in the metadata abstract inside LaTeX delimiters. It would also help to emphasize that the node-count discriminant term in Section 4.6 is the arithmetic-surface term in Riemann–Roch, not the conductor exponent of the Jacobian.

References used in this review:

[1] X. Yuan, *Modular Heights of Quaternionic Shimura Curves*, Theorems 1.1–1.2. [arXiv:2205.13995](https://arxiv.org/abs/2205.13995).

[2] G. Freixas i Montplet and A.-M. von Pippich, *Riemann–Roch isometries in the non-compact orbifold setting*, Proposition 8.1 and Theorem 10.1. [arXiv:1604.00284](https://arxiv.org/abs/1604.00284).

[3] H. Pasten, *Shimura curves and the abc conjecture*, Sections 13–16, especially Theorems 13.2, 14.1 and 16.7. [arXiv:1705.09251v4](https://arxiv.org/abs/1705.09251v4).

[4] J. Stankewicz, *Twists of Shimura curves*, Theorems 2.6 and 2.8. [arXiv:1208.3594](https://arxiv.org/abs/1208.3594).
