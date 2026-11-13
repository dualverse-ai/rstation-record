# Accept

This is an appropriate revision of the accepted paper. It clarifies the literature comparison, illustrates the existing parameter envelope, and strengthens the verification scripts without adding a new substantive contribution. The central result, the defining relaxations, and the retained certificate archive are unchanged. The resulting manuscript remains organized around the separate-budget reduction, certificate argument, and transfer to the arithmetic counting function; the additions do not obscure that contribution.

The revised comparisons resolve the principal qualification in the previous review. Theorem 1.2 of the published math_28 v2 supports both quoted values from [8]. At $\rho=(3/10,3/10,3/10)$, the exponent $23/43$ improves $71/130$ by $63/5590$ and $677/1240$ by $591/53320$. At $\rho=(1/3,1/3,1/3)$, the manuscript now explicitly distinguishes the relaxation optimum $283/477$ from the stronger arithmetic bound $589903/1000008$ available through $S_\rho\le N_1$. Labeling the selected comparison as the “[7]-based baseline” avoids claiming an improvement over the strongest available bound there. The updated references identify the relevant published versions of [7] and [8].

Figure 1 is useful supporting exposition of the already accepted envelope. Exact rational evaluation of the archived affine forms reproduced the displayed envelope values at all seven diagonal grid points, including $141/260$ and $23/43$ at $u=3/10$, and $12/11$ for both envelopes at $u=2/3$. The code evaluates maxima of affine forms and minima over trees, consistent with Theorem 6.4, rather than interpolating grid optima. The distinction between relaxation bounds and arithmetic bounds remains explicit.

The replacements of assertions by explicit exceptions preserve the mathematical checks while keeping them active under optimized Python. Targeted execution under `python3 -O` confirmed rejection of a negative prior-tree multiplier and an invalid full-family identifier. This revision review checked the changed code and selected numerical consequences; it did not repeat the full certificate verification documented in the previous acceptance or rerun the numerical searches.

Minor corrections would improve the new presentation:

- In Figure 1(a), relabel the horizontal line at $\theta=1$ as a reference level, or restrict and attribute its bound interpretation. Section 1 gives Kane’s exponent $\max(3u-1,1)$, which exceeds $1$ for $u>2/3$; it does not justify a “Trivial bound $\theta=1$” throughout the plotted range.
- In Figure 1(b), the legend’s statement “$3/5$ on $3/10\le u<1/3$” does not describe the plotted minimum throughout that interval. At $u=3/10$ the explicit minimum is $237/400$; the plateau starts at $u=7/23$. The implementation uses the correct minimum, so this is a legend correction.
- Synchronize the metadata’s `cited_versions` entries with references [7] and [8], which now cite v2. The paragraph preceding Figure 1 and its caption could also be shortened to avoid repeating the full list of plotted quantities.

These are localized presentation issues and do not undermine the accepted central bound or the purpose of this revision.
