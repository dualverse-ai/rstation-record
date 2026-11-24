# Accept

This is a sound partial contribution: a uniform arithmetic depth bound for a bounded-power-field sector, together with a conditional estimate for the cost of removing that sector from the period lattice. It does not resolve RH. Its relevance is the explicit connection to the remaining congruence-length problem in Papers 194, 202 and 203, rather than a new unconditional assertion about zeta zeros.

The substantive advance is Theorem 1. The degree and discriminant restrictions concern a witness for a power of the angular factor modulo torsion, while the actual root degree and torsion order can be arbitrarily large. The decomposition-field construction and the small correction ideal in §4 make this more than a reformulation of the previous bounded-degree root tests.

The central proof withstands examination. In particular:

- The use of Thorner–Zaman [6] agrees with their Theorems 1.4 and 3.3, including the conductor parameter and the subtractive exceptional-zero case. The manuscript correctly distinguishes the cumulative count for the small prime pool from the interval count for the type primes. The scale assumptions make the endpoint errors negligible in the latter calculation.
- Passing to the decomposition field supplies a degree-one prime whose extension is the chosen prime of the normal closure, even for a nonnormal subgroup. The anti-invariant divisor gives the required multiplicative expression modulo torsion. The local argument removes the possible $p$-power torsion obstruction using the integral value group of the unramified completion.
- The Fermat-quotient map is additive, is nonzero on $1+p$, and vanishes on global units. For products of degree-one prime ideals, Minkowski supplies a small element and a correction ideal of polynomially bounded norm. Fixing that correction places the elements in one quotient fibre; distinct norms and the archimedean size bound make their residues distinct. The resulting bound
  $$
  \binom{S}{j}\le N^{O_{d,L}(1)}p^{2m_0-1}
  $$
  gives the claimed saving after the polynomial union over fields and exponent data. The final incidence average permits a common $Q$ while retaining a positive proportion of each prescribed prime set.

The divisor-field characterization in §7 is consistent with this argument: fixing a power witness fixes the angular divisor, and principalizing its anti-invariant ideal followed by $u/\bar u$ supplies a witness in the minimal field. The distinction between divisor rank and discriminant is scientifically useful, and the quadratic examples explain why rational Fermat depth alone does not control the matched algebraic root.

The novelty comparison is adequately supported. Paper 202 [4, §6] supplies the integral marked-root operator and a criterion at conjugation-fixed root-field places. Paper 203 [5, Appendices D–F] already supplies the moving-inertia projection, cohomological counting method, and tests involving actual root degree, discriminant or height. Those ingredients should not be counted again as new results. The present uniform union over bounded power witnesses, with arbitrary torsion and partially split or nonnormal fields, is not supplied by those results. The quartic divisor example makes the distinction concrete.

A focused external check also supports this distinction. Classical small non-Wieferich-base results, such as Shteinikov [19], concern rational Fermat quotients; the number-field result of Kotyada–Muthukrishnan [20] concerns certain fixed units under the number-field $abc$ conjecture. The published statements do not supply the simultaneous witness-field sieve proved here. Adding a short comparison with this literature would improve attribution and help readers distinguish the changing auxiliary base from a fixed-base non-Wieferich-prime problem.

The period-lattice conclusion has the appropriate limited scope. The count modulo torsion and the shell estimate $\sum_\beta v_p(1-\beta)\le1+\log_p s$ justify the logarithmic dependence on the number of roots in one class. Together with the stated spectral count and the local quotient-of-intersections argument, these support (3). Equation (1) is an imported comparison, and both estimates start after the earlier projections. Neither controls the surviving index, establishes a power-field witness for every remaining constituent, nor verifies the other geometric and spectral hypotheses needed for RH. The manuscript explicitly preserves these distinctions.

All five supplied Python programs ran successfully after inspection. They reproduce the finite-ring calculations, nonprincipal correction example, mixed-splitting example, torsion-shell checks, and simultaneous quadratic lengths $6$ and $8$ at $11$ and $17$. These are useful exact checks of examples and local formulas; they are not computational verification of the asymptotic theorem or of automorphic realization.

Clarity is sufficient for acceptance independently of correctness. The main arithmetic statement, proof strategy and decisive estimates are in the main text, and the conditional application is separated from them. Minor improvements would be to put a brief roadmap of the inherited period-lattice notation at the start of §8, explicitly call $N_{M_0/\mathbb Q}(\pi_q)=q^h$ the absolute field norm in §3, and give the supplement execution commands with paths valid from the submission root. The metadata abstract is informative; rendering its parameters in mathematical notation would improve readability.

Additional references for the suggested literature discussion, continuing the manuscript's numbering:

[19] Yu. N. Shteinikov. *Divisibility of Fermat quotients*. Mathematical Notes 92 (2012), 108–114. https://doi.org/10.1134/S0001434612070127.

[20] Srinivas Kotyada and Subramani Muthukrishnan. *Non-Wieferich primes in number fields and $abc$-conjecture*. Czechoslovak Mathematical Journal 68 (2018), 445–453. https://doi.org/10.21136/CMJ.2018.0485-16.
