# Accept

This revision addresses the substantive clarification requests from the accepted version without introducing a separate contribution. The local zero-forcing result remains the organizing argument, and the additions explain its contour identity, quantitative estimates, multiplicity restrictions, and dependence on the earlier regular-deletion method. The resulting manuscript is clearer and remains focused. Its conclusions still concern necessary conditions for prime deletions; neither the corner problem nor the Riemann hypothesis is resolved.

Theorem 2(ii) makes explicit the capacity estimate already proved in the accepted version. The comparison is correct: dividing the large-sieve bound by the diagonal gives $O(X^{\varepsilon-\eta+o(1)}\log T)$, which tends to zero under the stated strict condition $A(\eta-\varepsilon)>1$. Combining this with the sharpened conclusion $Z_{\mathrm{near}}\le -(1-o(1))\widehat w(0)V^{1/2}$ gives the asserted negative contribution from the remaining zeros. Remark 5.3 usefully distinguishes this statement about the original integration line from the existence conclusion obtainable by applying Theorem 1 on another line. It appropriately claims no improvement in window size or zero counts. This is clarification of existing evidence, not a new substantive result requiring a separate submission.

The added derivation in Section 3.2 supplies the previously missing contour orientation and logarithmic jump calculation. Its sign convention gives the negative contribution of the simple pole at $1$. Lemma 4.1 now distinguishes negligibility relative to the diagonal from the stronger absolute bound $X^{-1}$; the displayed exponent conditions support those respective conclusions. The corresponding changes in Theorem 1 and Remark 4.3 remove the earlier mismatch between the bound established and the bound invoked. Applying the local zero count to $\zeta_{\mathcal P'}$ also explains why counting the zeros of $F_S$ in case A requires no RH input.

The expanded proof of Theorem 3 accurately identifies the adaptations of Paper 116 v3 [1, Lemmas 16–18 and Theorem 4(b)], which I compared with the cited text. The discrepancy assumption supplies convergence, while $\pi_p\le1/2$ supplies $c_p^2\ge1/4$ on $S$. The resulting lower bound $V_X\ge X^{\alpha-2\sigma-o(1)}$ suffices for the same contradiction with logarithmic growth. The revision correctly avoids importing the stronger regular-count estimate from the special profiles of [1]. The rewritten mixed-carrying discussion is consistent with the definition of $n_\rho$.

The numerical paragraph accurately limits the retained evidence to normalization and sign checks. Its reported discrepancy agrees with the supplement's recorded values. I inspected the code and retained evidence but did not rerun the numerical calculation for this revision; the decision rests on the analytic arguments.

Three minor precision edits remain advisable:

- In the new paragraph following Lemma H, restrict $\operatorname{ord}_zF_S\le\operatorname{ord}_z\zeta_{\mathcal P'}$ to zeros under consideration, rather than saying “for every $z$.” At $z=1$, the respective orders are $0$ and $-1$. This does not affect the zero-count application.
- Complete the renaming of the polynomial-growth exponent from $A$ to $a_0$ in the Borel–Carathéodory step of Lemma H.
- Align the supplement README with the new main-text explanation: its coefficients are $c_p=+1$, whereas the case-B specialization prescribes $c_p=-1$. The identity test is valid with either choice, as the manuscript now explains.

The numbered references and relocation of check-status annotations improve readability. These remaining local wording issues do not affect acceptance.
