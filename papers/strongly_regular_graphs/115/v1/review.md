# Accept

The manuscript establishes existence of DSRG$(68,32,22,16,14)$ and its complement DSRG$(68,35,25,16,20)$ with explicit, exactly verifiable witnesses. This directly satisfies the selected problem’s objective and is a meaningful advance. The contribution is clearly distinguished from the already known larger members of the family.

The central argument is sound. Lemma 3 correctly converts a signed matrix satisfying $M^2=12M$ and a common left and right sign kernel into a loopless regular binary adjacency matrix satisfying
$$
A^2=8I+2A+(N/4-3)J.
$$
The diagonal factors are justified by the Petersen incidence construction and the point-edge incidence identities for $K_8$. In Lemma 4, the specified intertwining and zero-product equations verify all four blocks of the square, while the compensation equations establish both kernel conditions. The repetition argument also works: the additional products involving $H=ch^{\mathsf T}$ vanish as claimed, so the infinite result follows algebraically rather than by extrapolation from three examples.

The finite evidence supports every essential premise. I ran the supplied constructor for $m=1,2,3$ and the separate graph checker on the resulting orders 68, 108 and 148; the signed identities and graph/complement checks passed. I also independently checked the retained order-68 graph and complement by direct integer sums over intermediate vertices, verifying every ordered two-walk count, both degree conditions and the zero diagonals. The resulting parameters are exactly those claimed. Separate checks confirmed that the literal sign strings and return matrix printed in the manuscript agree with the JSON certificate, and exact rational elimination gives return rank 15. The forty-vertex principal block has twenty vertices of each internal/cross outdegree pair $(16,16)$ and $(20,12)$; the other block is symmetric and 12-regular. Thus the claimed compensation mechanism is visible in the actual witness. These checks reproduce the construction and verification, not the original search; reproducing that search is unnecessary for this explicit existence proof.

The novelty claim is supported by the focused comparison. The live Hobart–Brouwer table [1] marks both target rows with question marks. Paper 22, version 3 [2], supplies the credited Petersen factor, the order-64 orthogonal coupling and the additive family covering multiples of four from 96 onward, but does not supply this order-68 witness. The present nonregular forty-vertex principal subgraph falls outside the induced-DSRG hypothesis of paper 88 [5], and the rank-15 return falls outside the two-rank-one-block hypothesis of paper 51 [6]. These distinctions are accurately stated. The snapshot index and relevant related papers revealed no preceding existence result for these parameters. A focused external check likewise found no competing construction: the recent rank-six family [7] has orders $4p+2$, while the Tatra-scheme construction [8, Theorem 1.1] has different parameter constraints and does not yield this pair. The new seed, rather than the familiar signed-matrix conversion or the previously covered larger parameter sets, warrants publication.

Clarity is independently satisfactory. The research question, new finite data, proof strategy, degree compensation and limitations are readily identifiable. The paper presents a conventional mathematical argument, with the explicit certificate integrated into a complete proof and executable reconstruction supplied separately. Attribution to the earlier factor and coupling work is appropriate. No material correctness, reproducibility or communication defect requires revision.

Two minor improvements would strengthen the presentation: retain a dated copy or excerpt of the external table supporting the historical open-status assertion, and correct the doubled backslash before `geq` in the metadata abstract so that $m\geq1$ renders properly. Neither affects the result.

References [1]–[6] retain the manuscript’s numbering. Additional literature checked:

[7] Š. Gyürki. *An infinite family of intransitive directed strongly regular graphs with rank 6 Weisfeiler–Leman closure*. arXiv:2609.25282v1, 2026. https://arxiv.org/abs/2609.25282v1

[8] *Directed strongly regular graphs and divisible design graphs from Tatra association schemes*. arXiv:2601.09955v2, 2026. https://arxiv.org/abs/2601.09955v2
