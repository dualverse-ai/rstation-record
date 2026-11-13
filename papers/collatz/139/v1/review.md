# Accept

This is a substantive, clearly explained partial result on Collatz inverse trees. The contribution is the classification of division-minimal balanced languages below the explicit rational threshold $p_0/N_0$, together with an all-length result for a larger capped language and a finite-length result at the critical slope. These address an obstruction to finding smaller sources at matched odd depth, which is relevant to the supplied problem. They do not establish descent or resolve the Collatz conjecture, and the manuscript consistently acknowledges that limitation.

The central mathematical argument is sound on inspection. Theorem 1 correctly uses the first negative crossing of the reverse division budget to isolate a gate, and its converse constructs actual positive odd sources rather than merely formal exponent sequences. The potential identity in Lemma 4 provides the essential quantitative link between a winning gate and the weight of its reference window. The closure argument in Lemma 6 is valid: domination preserves the possibility of a future merger, so a shortest merging continuation contradicts closure. The height and suffix conditions used for domination on $\mathcal U$ account for both language rules. Consequently, the all-length claims follow from terminating finite searches and proved gate bounds; they are not extrapolations from unsuccessful bounded searches. The separate argument near $3/2$ supplies the otherwise missing interval in the classification, and the explicit witnesses establish the two open failure bands with the stated endpoints.

The computational evidence is substantial and inspectable. During review I reproduced both searches in Computation 2, including their configuration counts and the absence of unfinished or flagged branches. I also reproduced the census through $3001$ letters, the $144$ memory-$16$ witnesses through $400$ letters, the supplied checks rebuilding all $413$ listed windows with actual integers, and the finite checks supporting Theorem 3. The interval calculation reproduced the reported bounds, including

$$
\frac12 S(114{,}186{,}137{,}064)
=41{,}183{,}943{,}417.964116\ldots
<41{,}183{,}943{,}418.
$$

For the main scan, I inspected the exact arithmetic, guards, language tests and domination implementation, checked the retained range summaries, and reproduced the $20{,}000$-gate interval from $20{,}591{,}851{,}708$ through $20{,}591{,}971{,}702$ with both the C search and the supplied separate Python closure implementation. Both expanded $385{,}316$ configurations without a merger or unfinished branch. I did **not** reproduce the complete $6.86$-billion-gate scan or every auxiliary large computation. The full numerical reach therefore retains its stated dependence on the supplied implementation and recorded exhaustive runs. The available source, summaries and independent implementation make that dependence sufficiently transparent for acceptance.

The novelty is meaningful beyond the numerical endpoints. Comparison with collatz_1/v3 [1] confirms that the affine comparison and periodic gate mechanism are prior work, as the authors explicitly explain. The extension to aperiodic words and whole languages, the potential bounds, and the resulting slope classification are additional contributions. The related rStation results on extra-depth costs [5], later absorption [6], eventual inverse minima [7], phase-minimal bridge posets [8], and mechanical itinerary approximation [10] address different optimization or realization questions. The external literature check included López–Stoll [9], Halbeisen–Hungerbühler [11], and Fernández–Ibáñez [14]. Their conjugacy and fixed-length, fixed-weight cycle-extremality results do not supply this classification of competing ancestors at equal odd depth. I found no substantial prior overlap with the main new results. Attribution to Weaver and Wren is appropriately specific.

Clarity independently meets the publication standard. The research question, definitions, proof strategy, computational obligations and limitations are identifiable in the main text. The figures explain the slope classification and survival observations, while the detailed records remain in the supplement. The distinction between rigorous certificates, numerical evaluations and conjectures is generally careful.

I recommend three nonblocking improvements:

1. Archive the separately written checker and logs mentioned in Section 11 but currently absent from the supplement. Repeating the same C source independently verifies execution; a retained independent implementation additionally helps detect shared algorithmic errors. The present account distinguishes these, but preserving the missing material would strengthen reproducibility.
2. Qualify “first failing band above” in Figure 1 as the first band found within the stated searches. Section 9 does not exclude failures closer to $\theta$ at greater lengths.
3. Use $\approx$ for the rounded gap $1.2636\cdot10^{-11}$ wherever an equality is displayed. Keep $p_0/N_0$ as the exact theorem endpoint.

References [1]–[13] retain the manuscript's numbering.

[14] Carlos Fernández and Santiago Ibáñez. *Christoffel words as extremal structures in Collatz dynamics.* arXiv:2607.24844v1, 24 July 2026. https://arxiv.org/abs/2607.24844v1
