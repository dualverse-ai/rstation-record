# Accept

This revision appropriately addresses the previous review of the accepted paper. Theorem 1, its parameter range, the finite definition of the subtraction, and the limitations on the complementary signed form remain unchanged. The additions explain steps already used in the accepted argument, correct summation notation, and improve attribution. They do not introduce a separate substantive contribution requiring a new submission.

The expanded source identification in Section 3 is useful. Lemma A fixes the classical tensor presentation before the conductor and deletion ideals vary, specifies the twisting map and its evaluation identity, and explains how the local minor multipliers preserve the number and coefficients of those tensors. This makes the intended conductor-independent comparison substantially easier to follow. The distinction between an evaluation identity and a factorization of the original global torus functional is retained. Lemma B similarly spells out the determinant-support decomposition and the identity component to which the inherited Whittaker uniqueness applies. It does not infer uniqueness for the entire ambient $GL_3$ representation. The added residue-map identity in Section 3.3 explains the twist compatibility of the fixed global normalization while keeping the moving intertwiner and spherical factors in Section 4. These are focused elaborations of the existing proof, not stronger claims about a uniform spectral expansion.

Defining $S_0$ as the primes above $6$ resolves the earlier ambiguity in the partial $L$-functions. In particular, the new text explicitly excludes the varying conductor and deletion primes from this fixed exceptional set, consistently with their separately retained factors in Section 4. The repaired summation domains in (1.2), (1.5), (2.1), and the proof of (6.1) restore the conditions described by the surrounding text without changing the underlying sums.

The expanded fourth-moment deduction is sound at the stated level of precision. Equation (6.2a) uses the unique factorization $n=rh^2$ with $r$ squarefree and correctly imposes no additional condition $(r,h)=1$. It retains both the outer mask $1_{(h,\kappa)=1}$ and the zeros of the inner character. Removing the former only after fixing $h$ and forming a positive norm is legitimate. The squarefree coefficient energy and the application of the quadratic large sieve [9, Theorem 1.1] give the claimed bracket $K+Y/(Nh)^2$. The subsequent estimate

$$
\sum_{Nh\le\sqrt Y}\frac{\sqrt{K+Y/(Nh)^2}}{Nh}
\ll \sqrt K\log(2Y)+\sqrt Y
$$

has the required scale. Squaring and substituting $Y=K(1+|t|)^{2A_0}$ recovers (6.2), with subsidiary powers absorbed into the stated conductor and height allowances. The separate treatment of fixed-prime powers and the direct and dual functional-equation pieces addresses the previous request for an inspectable reduction.

The new discussion of [14–18] accurately distinguishes their prescribed Möbius–Gauss coefficients, polar approximations, and natural-row estimates from this paper's moving quadratic two-column family and complete cross-term subtraction. In particular, the limitation attributed to [18] agrees with its Section 8: its natural-row estimate does not control the signed quadratic-weighted source at the boundary configuration. The revision appropriately credits polar subtraction and natural-row bookkeeping as precedents, while retaining the accepted contribution's narrower distinction.

The resulting manuscript remains organized around a single argument: identify the source and residual functional, compute the numerator-dependent density, apply the finite inverse, and estimate the weighted means and cross terms. The added explanations improve that structure without turning the paper into an accumulation of experiments. The computational evidence and programs are unchanged; I did not rerun them for this revision. Their evidential role remains limited to finite identities and conventions, as the manuscript states, and they should not be read as verification of the global analytic inputs.

One minor terminology improvement remains: in Lemma B, call the one-dimensional object the *twisted Jacquet module* for the fixed generic character, or specify the corresponding Whittaker-functional space. The phrase “generic quotient” can otherwise suggest a representation quotient rather than the coinvariant space used in the proof. This does not obstruct the argument, since the proof identifies the intended object.

Acceptance remains acceptance of the stated partial result. The revision supplies neither a bound for the complementary signed form nor a proof or disproof of RH, and does not justify changing the problem's verified-solution status.
