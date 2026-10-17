# Accept

The revision preserves the accepted contribution, supplies useful missing proof details, and adds a sound explanation of why a single compact-type Weil structure does not account for the positive classes in the sharpness example. It remains a partial result concerning positivity and projectivity of complex tori, not a solution of the projective Hodge conjecture.

Convention 3.1 makes the decomposable-vector estimates precise. Lemma 8.0 correctly adapts the Jordan-chain construction to a nilpotent antilinear map. With the adapted basis made unitary, the sign $(-1)^{p(p-1)/2}$ and the lower bound for $b$ give the stated growth contradiction using $D_A$. The expanded Cartan-involution argument, the dual certificate for Theorem C, and the rational Casimir construction of $K_5$ address the previous review's substantive requests for clarification. These additions support the existing argument without enlarging its conclusions improperly.

The new Proposition 10.2 is supported by its linear-algebra proof. Definiteness on $V_+$ gives opposite signs on $W$ and $W'$. Testing a weakly positive $c\omega^2+w$ on $\Lambda^2W$ and on mixed decomposable vectors forces $c=0$. The remaining off-diagonal Weil component takes negative values after varying the phase of $ts$, unless it vanishes. This establishes
$$
(\mathbb{R}\omega^2\oplus W_E)\cap\mathrm{WP}^2=\{0\}.
$$
The identification of the Weil lines with complex fourth powers also explains their relation to $K_5$, while the nonzero rotational average of $h^2$ explains why the Kraines class belongs to none of these individual Weil subspaces. This is a useful extension of the accepted example. It does not duplicate the indexed Fermat-double-cover paper. The distinction from Markman's abelian Weil-type results [13–15] is appropriate: those results do not supply the missing bundle on the non-projective compact component.

Targeted execution of `t29.py` reproduced the Weil-class coefficient match with residual about $1.1\times10^{-16}$ and the definite Hermitian form. Execution of `t30.py` reproduced signature $(2,4)$ and negative sampled margins, although the values were approximately $-0.484$ and $-1.260$, rather than the reported $-0.40$ and $-1.12$. These computations are consistency checks; the proposition rests on the proof. In particular, the script samples coefficient directions and uses local minimization, so “best margins over the Hodge space” should be replaced by “best margins among the sampled directions,” with normalization and numerical environment specified.

Two further scope clarifications would improve the revision:

- Keep the new rank-two discussion in Section 12.B explicitly conjectural. The omitted case analysis and the numerical classification do not establish a universal exclusion. In particular, `t36b.py` classifies approximate coefficient patterns; it does not certify that every solution has the asserted geometric pullback structure. Replace “a seed therefore needs rank at least 3” with a qualified statement about the tested construction ansatz, unless a complete argument is supplied. I do not regard this explicitly labelled heuristic as an additional proved result.
- The abstract should say that the $K_5$-component is the **negative** of the class associated with a nonnegative quartic, as Proposition 12.2 states. Likewise, the conditional conclusion is rational spanning by second Chern characters, not necessarily realization of each Hodge class as one bundle's Chern class. Label the proof following Corollary 12.3 as the proof of Proposition 12.2 to avoid ambiguity.

Separating the seed-dependent corollary from the proved bundle statement is helpful. The existence of such a seed and the extension to reflexive sheaves remain open, as the revision acknowledges. These qualifications do not undermine the accepted main theorem or the new positivity obstruction.
