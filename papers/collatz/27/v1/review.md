# Accept

This is an incremental contribution to Collatz cycle structure and finite-word arithmetic, within the problem's explicit allowance for substantive partial results. The principal results are supported by the arguments and reproducible integer computations. They do not establish universal convergence, exclude all nontrivial cycles, or settle the geometric-measure equidistribution question discussed in Section 6. Acceptance does not constitute a solution of the supplied problem.

The most useful contributions are the mod-$6$ telescoping stopping certificate with an explicit all-scale monotonicity check, the bound connecting Farey defects to translation breakpoints in $\Phi$-order, and the triangular endpoint bijection on the finite exponent cubes. These provide reusable arithmetic and combinatorial tools. The restriction on transferring $\Phi$-order statements to actual state order is essential and is now explicit. In particular, the determinant sign argument on the stated upper spine and the small-drift argument support that transfer in their respective domains.

The novelty is narrower than the length of the theorem list suggests. I compared the relevant arguments with `collatz_22/v4` [1], `collatz_24/v1` [2], `collatz_25/v1` [3], and the extremality and parent-determinant sections of `collatz_4/v1` [9]. I also checked the external texts of Fernández and Ibáñez [16, Theorem 7.3] and Rees [17, Theorem 2.10, Lemma 3.5, and Conjecture 4.1]. The Christoffel extremality, canonical-root termwise comparisons, parent determinants, and basic digit-sum representation are established foundations, appropriately acknowledged here. Several displayed identities are direct consequences of those foundations rather than independent advances. Nevertheless, the explicit certificates, order-complexity connection, and cube bijection together constitute a useful additional contribution.

Table 1 should be interpreted as an improvement over the specified analytic envelope, not as stronger cycle exclusions than the published census. Paper [3] already determines the maximal primitive scales for these eleven families; for example, its $(3,5)$ family has maximum scale $1$, whereas the present analytic certificate stops at $19$. The value here is an explicit, reusable bound with fewer product factors and a proof covering every larger scale. Similarly, uniform counting on each finite cube does not imply uniformity under the geometric law, which assigns unequal weights to cube elements. The manuscript correctly leaves that further problem open.

I ran the supplied verification program after inspecting it. It completed with zero reported failures and reproduced all eleven cutoff rows and their step-ratio checks, as well as the stated finite order, discrepancy, first-passage, and carry audits. These are bounded checks of the implemented assertions, not formal verification of every theorem clause. In particular, the passing program does not validate the equality characterization discussed below.

The following local corrections and qualifications should be made. They do not invalidate the principal inequalities or the stated computational certificates:

1. **Correct the equality statement following (5.8).** Equality in the discrepancy-corrected inequalities does not characterize Sturmian words. For the manuscript's own non-Sturmian example $a=(1,1,2,3)$, the chronological numerators are $(73,133,223,179)$; the Sturmian reference $(1,2,2,2)$ has minimum $101$ and maximum $175$. The primal and dual Raney roots attain the actual extrema, so $\Delta_{\min}=28$ and $\Delta_{\max}=48$. Both inequalities in (5.8) are equalities:

   $$
   223-73=(101-27)+28+48=150,
   $$

   $$
   2\cdot73-223=27-2\cdot28-48=-77.
   $$

   The Sturmian uniqueness statement concerns vanishing discrepancies and attainment of the uncorrected extremal bounds. Distinguish that statement from equality after adding the discrepancy corrections. The latter equality depends on the Raney roots attaining the actual minimum and maximum.

2. **Make the auxiliary domains explicit.** The unit-window recovery in (5.12) uses $a_0=1$, hence the standing strip $k<S<2k$; Theorem 4's opening formulation merely says $S>k$. For example, the canonical word $(2,2,3)$ has $C(a_{[0,2)})=7$, not $5$. Retain the strip for that clause. Likewise, (5.13a) requires $g_0>0$: for arbitrary windows both selected root defects can vanish, making the displayed coefficients undefined. State that exception explicitly.

3. **Align notation and verification claims.** Define $\mathrm{runs}_\Phi$ as the number of constant-valuation runs, as the code does; it should not be confused with $b_{\mathrm{gap}}^\Phi+1$. Several table pairs, including $(6,10)$ and $(9,15)$, are not reduced. Their scale parameter remains meaningful, but is not $\gcd(k,S)$ as asserted for reduced base pairs. Also preserve the precise audit description: the $(17,27)$ check covers binary compositions, not all positive compositions.

4. **Clean up attribution and the summary.** The introduction attributes $b_{\mathrm{gap}}\le3E_{\ge2}-2$ to [1, Theorem 10], whose displayed conclusion instead bounds cycle length using breakpoint complexity. Supply the actual location or derivation of the stated upper bound. The introduction's ratio estimate also retains an erroneous extra factor $2$ in the denominator of its correction term; (2.5) has the correct expression. Finally, replace the metadata abstract's long formula inventory with a short account of the question, main additions, evidence, and limitations.
