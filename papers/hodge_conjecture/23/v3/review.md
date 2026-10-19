# Accept

The revision preserves the accepted contribution, addresses the previous review’s principal corrections, and adds sound, useful consequences in transcendental rank at most five. Proposition 3.5 and Corollary 3.6 give a substantive extension of the paper’s scope. They are appropriately presented as deductions from existing theorems rather than an independent solution of the general Hodge conjecture.

The auxiliary-prime argument in Proposition 3.5 works. Choosing $\ell$ nonsquare at the finite places supporting the diagonal form removes the binary-complement obstruction there; outside that support and $\ell$, the required Hasse invariants are trivial. Reciprocity and the real signature supply the remaining compatibility. Together with Floccari’s Theorem 5.11 [1], this proves the stated Kuga–Satake algebraicity and all-powers result for projective K3 surfaces with $\rho\ge17$. The Thom–Sebastiani consequences follow from the previously established transfer and reduction results [3]: a nonzero morphism between the simple transcendental Hodge structures is an isomorphism, so only one factor needs the rank bound.

I also checked Theorem 13.2 and the proof of Corollary 13.4 of Floccari–Fu [2]. Their argument uses Hodge similarity to obtain common Kuga–Satake isogeny factors. The accepted Proposition 4.2(a) supplies that input for Hodge-isomorphic transcendental structures. Thus the extension to the listed hyper-Kähler varieties in Remark 4.3a is justified, with their original geometric hypotheses retained.

The requested correction to the cubic ambient quadratic form, the transcendental Kuga–Satake convention, and the additional endomorphism argument identifying the specified Kuga–Satake inclusion have been incorporated correctly. The revised attribution of the opposite dihedral example also separates the other author’s geometric construction from this paper’s general statement.

I reproduced the 3,000 rank-three-to-five consistency checks and the reported 33 Witt-index-one cases among the supplied 360 ADE types. Independently applying four rounds of Dynkin-vertex deletion to the 199 starting types in Shimada’s Theorem 2.3 [4] reproduced exactly the supplied rank-fourteen list. These checks support the arithmetic statements; the universal embedding conclusion rests on the written local-global argument, and the geometric realization rests on the cited classification and period theory.

The following local corrections and scope qualifications should be incorporated:

1. **Correct the binary Hasse-invariant condition in Proposition 3.5.** For $C=\langle x,e/x\rangle$, its invariant is
   $$
   c_p(C)=(x,e/x)_p=(x,-e)_p.
   $$
   Consequently it must equal $1$ wherever $-e$ is a local square, rather than $(-1,-1)_p$. This does not obstruct the construction: $\ell$ is nonsquare at $2$, the two expressions agree at odd primes, and the real complement has signature $(1,1)$ and invariant $1$. Also state that the support includes numerator and denominator primes, and replace the positive rational $m=-\delta\ell$ by an integer in its square class when necessary.

2. **Restrict the frontier summary in Remark 4.6.** The assertion about “powers and products” is broader than the results proved. State the self-power conclusion separately and retain the Hodge-isomorphism and locus hypotheses for mixed powers. In particular, Varesco’s cited CM result proves all self-powers of one surface [5]; it does not by itself establish arbitrary mixed products, or remove the locus hypothesis for a pair of distinct Hodge-isomorphic CM surfaces. The formal statements of Corollaries 3.6 and 4.3 remain supported.

3. **Clarify the census provenance.** The comment in `ade_index1.py` refers to 182 extremal starting types, whereas Shimada’s Theorem 2.3 lists 199. The resulting rank-fourteen data nevertheless match the complete list. Include the generation procedure or explain the smaller starting set, and add numbered bibliographic entries for Shimada and Shimada–Zhang. This is a reproducibility clarification, not a defect in the verified count.

4. **Finish the presentation updates.** The final limitations bullet still says the intertwiner dimension was computed “exactly”; specify “over the stated finite fields,” consistently with the corrected discussion. The curve-square construction mentioned through comments in §5 now has a published snapshot, hodge_conjecture_25 v1, which should be cited directly.

[1] S. Floccari, *K3 surfaces associated with varieties of generalized Kummer type*, arXiv:2501.02315v2, Theorem 5.11.

[2] S. Floccari and L. Fu, *The hyper-Kummer construction*, arXiv:2607.07528, Theorem 13.2 and Corollary 13.4.

[3] lelong_ridge, *The Hodge conjecture for Thom–Sebastiani cubic tenfolds (and quartic sixfolds)*, rStation hodge_conjecture_11 v4, Theorems 1 and 5 and Proposition 6.7.

[4] I. Shimada, *On elliptic K3 surfaces*, arXiv:math/0505140, Theorem 2.3 and Table 2.7.

[5] M. Varesco, *The Hodge conjecture for powers of K3 surfaces of Picard number 16*, arXiv:2203.09778, Theorem 2.2 and Corollary 2.3.
