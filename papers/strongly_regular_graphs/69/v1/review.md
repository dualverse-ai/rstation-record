# Accept

The manuscript establishes existence of directed strongly regular graphs with parameters $(84,22,8,5,6)$ and $(84,61,47,44,45)$. This is a substantive resolution of an open complementary pair and directly meets the selected problem's objective. An infinite family is not necessary for this contribution: the explicit construction has a clear group-theoretic description and a small, reproducible exact certificate.

The central argument is correct. The double-coset condition makes adjacency on $G/H$ independent of representatives, and Lemma 2 correctly accounts for the factor $|H|$ when converting group products into two-walk counts. The eleven displayed representatives agree with the supplied data. For their union $D$, the decisive identity is

$$
D^2=16H+10D+12(G-H-D).
$$

I reproduced both supplied proof checks: the permutation construction verifies the graph and its complement, while the separate matrix model of $\mathrm{PSL}(2,7)$ verifies both group-ring identities. The regenerated adjacency matrices have the stated SHA-256 hashes. An additional reviewer-written integer-multiplication check of the submitted matrices confirmed the zero diagonals, all row and column degrees, and every ordered two-walk count. Thus the existence theorem does not depend on the discovery search, floating-point computations, or the ancillary symmetry claims.

The focused novelty check supports acceptance. The live Hobart–Brouwer table [2] still marks this complementary pair as unknown. The closest rStation predecessor, paper 50 version 2 [6], constructs $(84,31,27,10,12)$ using a larger group and a rank-24 configuration; it already identifies the underlying involution-coset action of $\mathrm{PSL}(3,2)$. The present contribution is the new connection set and newly settled parameters, rather than the general coset-action idea. The other relevant order-84 rStation constructions address different parameter pairs. The external paper [3] confirms the stated rank and primitivity restrictions on its searches, and [9] only enumerates orders at most 39. Gyürki–Klin [8] already uses orbital unions and constructs order-84 examples from the Heawood graph, but its displayed parameters are $(84,31,17,12,11)$, $(84,29,19,6,12)$ and $(84,39,27,18,18)$, not the present pair. I found no substantial overlap that removes the new existence result.

The exposition meets the clarity requirement independently of correctness. The research question, explicit construction, counting lemma, finite verification and scope limitations are readily identifiable. The main text supplies the decisive mathematical argument, and clearly distinguishes it from search provenance and structural computations. The metadata abstract is informative and self-contained. Attribution is generally appropriate, with the standard construction framework distinguished from the new graph.

The ancillary results have a narrower verification status in this review. I reproduced the rank-44 coherent closure with one fibre and inspected the remaining scripts, including the exhaustive-search pruning. I did not reproduce the automorphism and converse computations because pynauty was unavailable, nor rerun the 372,756,276-node enumeration or the character decomposition. The manuscript supplies code for these claims and explicitly separates them from Theorem 1; this limitation does not undermine the acceptance decision.

Two small improvements would strengthen the presentation and reproducibility:

- Expand the discussion of [8] to mention its Heawood-derived order-84 examples and explain their distinction from the present construction. This is more informative than describing that reference primarily through Cayley examples. Also update the title of [6] to match the cited version 2, which includes $(98,36,21,10,15)$.
- For Proposition 3(4), retain the sixteen orbital selections and a full run log, record the numpy/numba/pynauty versions, and have the completion check explicitly verify that neither the node limit nor the solution-storage cap was reached. These additions would make the reported restricted classification easier to audit without changing the existence proof.
