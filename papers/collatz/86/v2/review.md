# Accept

This revision appropriately corrects and explains the accepted contribution. It retains the signed digit-automaton obstruction and its stated limitations, without introducing a separate substantive result. The additional discussion supports the existing computations and responds directly to the previous review. The resulting manuscript remains organized around the cancellation argument; the additions do not obscure that contribution or turn the paper into an experiment collection.

The coordinate correction in Section 2 is sound. From $r_\sigma\equiv1+2r^{(y)}_\sigma\pmod{2^m}$, the required direct-coordinate window is a marginal of the top $\ell+1$ digits in Nashida's coordinate. Thus the one-digit shift preserves the application of the cited equidistribution result. I reproduced the supplied exact enumeration for $s=6,8,\ldots,20$, including both total-variation columns and every reported congruence check. This verifies the finite distributions; the asymptotic conclusion still rests on the cited lemma and the coordinate argument.

The revised witness reporting now distinguishes the exact failure of $F(z_0)\ge F(z_m)+m$ from the stronger logarithmic test. I reproduced the six general-reader outputs and both triangular-script modes exactly. The reported exact failure ranges, $36$–$40$ and $27$–$40$ out of $40$, agree with the retained evidence. Describing the comparison of sample means as a heuristic diagnostic removes the previous unsupported claim that the proof predicts those means. These computations establish the stated finite checks, not the asymptotic theorem or all structural hypotheses for the sampled readers.

Section 5 supplies the missing rationale for the additive-reader calculations: stationary mean balance, exclusion of positive drift by the ranking inequality, and the zero-variance coboundary criterion. Restricting that interpretation to strongly connected readers, while identifying the stronger condition tested on other random DFAs, is an appropriate qualification. The rational-dimension argument is also valid: the incidence block has field-independent rank, modular rank bounds the full rational rank from below, and the explicit trivial solution space closes the dimension inequalities when excess is zero. I reproduced the complete DFA rank output. This does not establish an obstruction for arbitrary additive readers.

The dimension qualification in Lemma C(ii), the treatment of $F(z_0)=0$, and the LaTeX abstract are appropriate local corrections. A few minor consistency edits remain:

- Remove the supplement README's references to “Theorem 4” and “Proposition 5,” which do not exist in this manuscript.
- Update the witness-script docstrings: they retain the incorrect additive-log description of the ranking inequality and the language of a predicted mean, although the implemented tests and revised main text now distinguish these correctly. The window-rank script's old probabilistic explanation should likewise point to the new deterministic rank argument.
- Describe the coordinate enumeration as covering $s=6,8,\ldots,20$, rather than all $s\le20$.

These are documentation issues, not grounds for rejecting the revision. Acceptance remains for the certificate barriers and supporting finite evidence; this version does not meet the Collatz solve definition.
