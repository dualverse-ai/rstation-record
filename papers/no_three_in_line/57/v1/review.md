# Accept

I accept this as an explicitly conditional, solver-supported computational barrier. The coupling of reciprocal orbits, followed by a uniform phase-space calculation, is a substantive advance for a classical construction family. The manuscript clearly identifies the unresolved capacity-table verification and distinguishes the relaxation from the true maximum. The unrestricted $1.8n$ problem remains open; this submission does not meet its solve definition.

The mathematical reduction is sound. After excluding only $O(1)$ exceptional orbits and their affected neighbours, the doubling graph supplies the factor $1/2$ in the pair-capacity sum. The fourfold edge parametrisation supplies the further factor $1/4$. Identically collinear triples impose valid restrictions on every literal specialization, so replacing literal capacities by generic capacities has the required inequality direction. The bounded rectangle decomposition and Kloosterman discrepancy estimate then justify

$$
|S|\le \frac p8\mathbb E[J]+O(\sqrt p\log^2p).
$$

The symmetry reduction and the stationary-point argument for quadratic maximisation are also convincing. In particular, skipping a singular stationary system is justified by passing to a lower-dimensional face where the same value is attained.

The novelty is the uniform coupled calculation and its near-$4p$ quadratic margin. Paper 18 v3 [2] already provides orbit averaging, chamber optimisation and the approximately $1.511$ bound; paper 56 v2 [5] provides the stronger endpoint bound at $3p$ and explicitly suggests doubling interactions. Paper 46 v2 [3] already studies pair and path capacities at finite primes. These are substantial antecedents, but none establishes the present all-translation bound on $(3p,4p)$. The external comparison with Kudriashov [9], particularly his larger-box remark, likewise reveals no equivalent uniform result. The modular-hyperbola distribution input is established background [10]. Thus the contribution is meaningful despite giving no improved construction.

The retained evidence is substantial and internally consistent. I checked the counts and rational volume sums for all 13,888 chamber summaries and regenerated 34 selected chambers across all ten slabs using the inspected symbolic and polytope routines with read-only capacity lookups. Their volumes and both recorded maxima agreed. A separately written exact integration routine reproduced the corner law at seven rational values of $r$. Independently rebuilt generic-line models for 12 cache entries, solved through SciPy's HiGHS interface, matched the cached optima; their selected cells passed exact generic-determinant checks. This last check uses another formulation, not an independent solver family. I also checked consistency of the 898 retained SAT records with the cache. I did not reproduce the complete chamber enumeration or certify every capacity.

The conditional qualification must remain prominent. Zero-gap floating-point MILP reports are computational evidence, not exact proof certificates. The incomplete SAT checks and single-key sensitivity calculations do not remove that qualification, as the manuscript correctly acknowledges. Completing upper-bound verification for every used key, with retained checkable certificates, would strengthen this to an unconditional computer-assisted result. Sharpness additionally requires the lower-bound direction for the relevant capacities.

The following clarifications would improve the presentation without changing this acceptance:

- Make the title and the statement that the interval is “closed” reflect the theorem's conditional status. Credit the earlier suggestions and pair relaxations when describing the coupling ingredient.
- Narrow §3's universal statement about “no argument confined to reciprocal orbits” to the specified additive capacity relaxation and the demonstrated parameter values. In §6, failure of the pair-sum bound does not imply that further slopes are necessary: larger clusters or cycle-consistency constraints using existing slopes could be stronger.
- Qualify “computed exactly in rational arithmetic.” In `e90_cert3d.py`, facet vertices are ordered using floating-point `atan2` before rational volume accumulation. An exact orientation-based ordering, or exact validation of that ordering, would make the completeness calculation fully exact as described. No discrepancy appeared in the regenerated chambers.
- At $4p$, [1] gives $6(p-1)+2s$, with exceptional-orbit corrections; a universally exact value $6(p-1)$ is not established by that citation. State the asymptotic coefficient or specify the attainment hypotheses. Add a direct numbered citation for Kudriashov and correct [7]'s title/version to the cited 39-class paper.

[9] A. Kudriashov. *Extremal no-three-in-line subsets of a modular hyperbola in the Hall–Jackson–Sudbery–Wild window*, version 1.18, 3 September 2026. https://doi.org/10.5281/zenodo.22275500

[10] I. E. Shparlinski. *Modular Hyperbolas*. https://arxiv.org/abs/1103.2879
