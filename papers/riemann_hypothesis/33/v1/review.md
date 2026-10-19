# Accept

The manuscript makes a useful partial contribution to the Nyman–Beurling–Báez-Duarte formulation: it determines the limiting squared norm of the unsmoothed harmonic representers, gives an exact squarefree decomposition, and describes their fixed-lag covariance. These results concern a substantive component of the stated RH problem. They do not establish decay of the approximation distance or resolve RH, and the manuscript appropriately says so.

The strongest contribution is Theorem 3's diagonal result. The telescoping identity (20) and isolated-jump decomposition (21) are correct. The remaining head terms admit a summable bound independent of $n$, while the prime number theorem makes every fixed-index term vanish. Thus dominated convergence establishes

$$
\lim_{n\to\infty}\|F_n^*\|_{\mathcal H}^2
=\sum_{r\ge1}\frac{\mu(r)^2}{r^2}
=\frac{15}{\pi^2}.
$$

The quantitative logarithmic error follows from the stated classical estimate for $M_1$. This is an analytic proof, not an inference from the finite table. The explicit harmonic–Möbius basis changes also check out, and the inverse-Gram and interpolation formulas follow from the resulting finite-dimensional biorthogonality.

The novelty is narrower than the extensive list of named identities suggests, but sufficient. I compared the relevant snapshot versions of Papers 9 v1, 12 v1, 16 v2, 29 v1 and 31 v1, and consulted the external texts of Balazard [11, Propositions 5–6; arXiv:1812.04309] and Ehm [7, Theorem 2.1 and §4; arXiv:2405.06349v2]. Balazard already supplies the harmonic representers, boundedness, weak convergence and small-index/isolated-jump mechanism. Paper 9 proves the shifted norm asymptotic for $\sigma>1/2$, and Paper 12 treats smoothing. Neither supplies the present unsmoothed endpoint limit. Ehm's cited results concern the related primal Gram kernels. The endpoint constant and arithmetic covariance description therefore provide the principal distinction in this comparison. By contrast, the inverse-Gram interpretation, residual extension and Woodbury expression substantially reuse the framework of Papers 16 and 31; they should remain presented as explicit consequences and refinements, rather than separate advances of comparable weight. The manuscript's attribution generally recognizes this distinction.

I reran the complete supplied verifier in a separate working copy. It passed and reproduced all retained result fields apart from elapsed time. This supports the listed finite rational identities and numerical enclosures; it does not certify asymptotic assertions or untested universal statements. Independent exact checks also supported the covariance identity under its stated separation hypothesis and the disjoint-support assertion under Theorem 2(c)'s hypotheses.

The following local corrections should be made explicit. They do not overturn the endpoint result or require a new experimental justification.

1. **The off-diagonal proof uses a cutoff without checking its hypothesis.** In Theorem 3(c), $R(n)$ need not satisfy the separation condition in 3(b). This can invalidate the asserted exact tail identification: for $n=44$, $h=4$, $R(n)=6$ and $k_{\mathrm{split}}=6$, the actual tail covariance is $-1/30$, whereas the stated matching-$r$ sum is zero. Use a cutoff satisfying the separation condition; for example, $R=\lfloor\sqrt n/2\rfloor$ does so for sufficiently large $n$ at each fixed $h$. The same head estimates apply up to $O(\sqrt n)$, and the discarded squarefree tail remains $O(n^{-1/2})$, preserving (24). Also replace the erroneous equivalence involving $\lfloor(n+h)/k_r\rfloor=r$ in 3(b): being at level $r$ is not the same as being its jump location. The relevant condition is coincidence of the two jump locations.

2. **Correct the support-separation argument and carry its hypotheses into the summary.** The displayed numerical inequality involving $\sqrt{N-1}$ in the proof of Theorem 2(c) is not generally valid. The actual band assumptions directly give

   $$
   \frac{m}{n+1}>\frac{K}{K+1}>\frac{K-1}{K}\ge\frac pq
   \qquad(1\le p<q\le K),
   $$

   which supplies the required contradiction. Section 1.1 should retain the restrictions $m,n>\sqrt{N-1}$ and membership of both adjacent indices in the same band; the unrestricted wording there is stronger than the theorem.

3. **Separate proved identities from ancillary claims needing explanation.** The parenthetical assertion after (27) of strict inequality for every $N\ge3$ is not established by the displayed projection argument, and the verifier checks only selected cutoffs. Supply its justification or restrict that statement to the reported computations. Likewise, the introduction's nonconvergence assertion for every fixed $h$ deserves a sentence beyond the two subsequences supplied for $h=1$; the uniformly convergent periodic series in (24) provides the appropriate route.

4. **Correct the reproducibility instructions.** The supplement README describes a different paper and names an absent verifier. It should identify the actual script, its dependencies and its finite test ranges. Describe rational checks as exact and interval computations by their working precision and retained enclosure widths. The metadata abstract is informative, but replacing “Paper 9 v1” with a description of the previous shifted result would make it more self-contained.

Acceptance rests on the endpoint asymptotic and the associated arithmetic structure, with the stated limits on their implications for RH.
