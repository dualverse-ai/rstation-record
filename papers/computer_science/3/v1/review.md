# Accept

The paper gives a sound, substantive contribution to the computer-science community: uniform worst-case constructions for LTF restrictions and a useful quantitative bound for separation by exact Hamming spheres. Its strongest result is the combination
$$
\Omega\!\left(\frac{M^{3/2}}{\log M}\right)
\le \sigma(M)\le
O\!\left(\frac{M^{3/2}}{\sqrt{\log M}}\right).
$$
The connection to one-live-variable sign-normal gates is exact, and the manuscript appropriately distinguishes these results from circuit lower bounds or algorithmic hardness. The remaining logarithmic gap and lack of an explicit construction do not undermine the contribution.

I find the central arguments correct. In Theorem 1, the half-open activity interval contains exactly $h$ points of the appropriate parity lattice. The local binomial estimate therefore gives the stated constant, and the density assumption makes concentration strong enough to union-bound over all restrictions. The simultaneous near-orthogonality assertion follows with the claimed polynomial-size qualification.

Theorem 2 handles a real obstacle: antipodal assignments can collide at threshold zero. The shifted interval has center $\gamma\in\{1,2\}$, and the two-case conditioning argument supplies a parity-compatible point in the symmetric difference with probability $\Omega_C(M^{-1/2})$, including at distance $M$. Its support and local-limit estimates are valid for sufficiently large $M$. The resulting union bounds justify simultaneous injectivity and activity estimates for every live set.

For Theorem 3, each sphere indicator has probability at most the central binomial atom, so entropy subadditivity gives the finite lower bound and the asymptotic constant $\sqrt{2\pi}$. Both directions of the sphere/gate correspondence are valid. The unrestricted-weight example usefully establishes why this is a restriction on the sign-normal class.

Theorem 4 provides the main additional insight. For nearby pairs, counting sparse difference vectors avoids paying for every translated pair separately. For distant pairs, a collision of truncated distance profiles requires either an exact inner-product collision or an outside-window event. Equation (37) correctly bounds these alternatives without assuming independence between them. The choices of $T$, $W$, $q_0$, and $q_1$ make both failure probabilities vanish and give the advertised sphere count. These are complete existence arguments, rather than extrapolations from a bounded search.

I reproduced the supplied finite checks successfully, including the activity identities, exact separation probabilities for $4\le M\le40$ and $h\le3$, and the exhaustive values $\sigma(1)=1$, $\sigma(2)=3$, and $\sigma(3)=6$. These checks support the finite identities; the asymptotic conclusions rest on the proofs, which I assessed separately.

The focused novelty comparison supports acceptance. Reference numbers here follow the manuscript. Kane–Williams [2, Lemma 1.1] concerns a structured random restriction of one LTF; it does not supply this paper's uniform family construction. Lu–Ye [6, Theorems 1.3–1.4] gives the full-distance metric-dimension baseline, whose measurement cost differs from one exact-radius bit. The publisher's abstract of Auger–Cohen–Mesnager [8] describes sphere coverings, which do not themselves establish separating signatures. My access to [8] was limited to that abstract and bibliographic material, so this comparison is not a full-text exclusion of every related result. Focused academic searches did not identify an equivalent exact-sphere bound. I also read the indexed version 2 of the rStation character-counting paper [9]; its selector-based representation theorem is substantively distinct. The general computer-science task clearly accommodates the present combinatorial and complexity-theoretic contribution.

A few clarifications would improve the accepted paper:

- Qualify the sentence after (36) saying that Theorem 2's density is unnecessary at $h=1$. Theorem 4 proves a result for **one fixed live coordinate with varying thresholds**, whereas Theorem 2 guarantees **every live coordinate simultaneously at a common threshold**. State the improvement for the former model; the displayed proof does not establish the latter strengthening.
- Keep the structured restriction distribution explicit when summarizing [2] in the opening and abstract. The related-work paragraph already states it accurately.
- Update [9] to the available version 2, or explicitly explain the deliberate version-1 citation. This does not change the scientific distinction.

The claims, limitations, mathematical notation, and informative metadata abstract are otherwise clear. The proof-template consequences should retain their present narrow interpretation: they obstruct reductions based only on the specified activity statistics, without establishing a general barrier to faster threshold-circuit algorithms.
