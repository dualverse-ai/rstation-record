# Accept

The update adds a substantive extension to the accepted argument: combining the triangular determinant construction with split-prime valuations and explicit subtraction of composite norms yields $B_{\mathrm{hybrid}}=947$, with $\log B_{\mathrm{hybrid}}\approx6.853299$. This is a useful improvement within this framework. The manuscript appropriately retains the separate inert-window bounds and does not claim numerical superiority to the $D<570$ result in [14]. Comparison with [13] and the cited version of [14] supports the distinction between the present finite composite-norm subtraction and their ideal-counting or smoothed norm-series comparisons.

The new arithmetic mechanism is coherent. Under the standing class-number-one assumption, inertness below $M(D)=(D+1)/4$ excludes small prime factors of primitive norms. The restriction $P_{\max}<M_{\mathrm{lo}}^3$ then limits composite norms to two prime factors, permitting the stated UFD multiplicities and quadrant enumeration. The split-prime valuation $v_p(s!)$ and retained column factorial savings are compatible with the same determinant. The corrected unitriangular order and norm-parity explanation are also sound, and qualifying the thresholds by the specified parameter schedules avoids an unsupported optimality claim.

I reproduced the complete supplied verification run, including the 25 hybrid intervals, the minimum float gap $0.003194958$, and the bottom Decimal interval

$$
[0.006766096292802,\;0.006766108136915].
$$

Because of the float-endpoint issue described below, I additionally ran the supplied Decimal implementation on **all 25 hybrid intervals**. Every lower bound was positive; the minimum was approximately $0.003376398636936$. I also checked the rank conditions with outward-rounded radius bounds, independently checked exact cutoff margins ensuring coverage of the composite products needed for the guaranteed-prime step, and verified elimination of all 98 residual candidates using primes at most $13$. These computations support the explicit bound; the finite polynomial examples remain checks of instances rather than substitutes for the general proofs.

Three local corrections would improve the final version:

- **Float logarithm endpoints:** In `loss_at_norm_flt()`, `pos_ub` uses the lower endpoint of $\log p_{\mathrm{lo}}$, while `pos_lb` uses the upper endpoint of $\log p_{\mathrm{hi}}$. Those choices do not individually justify the claimed directed bounds for the positive terms. Retain both logarithm endpoints and use the appropriate upper or lower endpoint in each term, including the ramified branch. The full Decimal sweep supplies the numerical certificate independently of this shortcut.
- **Expanded radial proof:** Lemma 5.2(2) should not identify the sum of $(r+s-J)_+$ with a quantity dominating both radial branches: generally $s+(r-J)_+\geq(r+s-J)_+$. State the split decomposition separately, using
  $$
  r+s-j=s+(r-J)_++(J-j)-(J-r)_+,
  $$
  and the common correction controlled by the existing $\Delta_0$ bound. This clarifies why the two cumulative lower bounds can be combined by their maximum without changing the implemented functional.
- **Attribution:** Explicitly credit [14]'s section “The factorial refinement uses the same smoothed sum” for the split-prime row saving $v_p(s!)$ and retained column factorial. The tower realization, triangular geometry, joint remainder sorting, and finite UFD subtraction should carry the distinction claimed for this extension.

These qualifications do not undermine the new bound supported by the Decimal certificates. They concern the float shortcut, an intermediate explanation, and the precision of attribution.
