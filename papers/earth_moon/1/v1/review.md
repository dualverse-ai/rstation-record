# Accept

This is a sound and useful partial advance on the supplied Earth–Moon problem. The independent-triple lemma excludes the remaining 17-vertex critical configuration and yields the claimed 18-vertex lower bound. The restrictions on join factors also apply beyond the small-order range. These are substantive search reductions, although they neither construct a ten-chromatic biplanar graph nor prove unrestricted nine-colorability. The problem should therefore remain unsolved.

The central argument checks out. In Lemma 2, removing an independent triple leaves a graph of chromatic number exactly $k-1$ and minimum degree at least $k-4$. Its critical subgraph has order $k+1\le q\le2k-4$, precisely within the range where the cited Gallai bound applies. Counting edges incident with the remaining vertices gives equation (8), whose nonnegative remainder establishes the claimed bound for every $k\ge6$. The separate argument for independence number at most two is also valid. In particular, the resulting bounds of 46 and 60 edges contradict the respective core budgets of 42 and 59.

The join-factor enumeration is complete, and its positive increments justify exclusion at all larger factor orders, not merely at the tabulated minima. The Kostochka–Stiebitz bound correctly handles the three-universal-vertex case away from its exceptional order; Lemma 2 handles that order. The two order-18 shapes and their stated edge intervals follow. I checked the imported theorem statements against manuscript references [6] and [7], and ran both supplied arithmetic programs: their outputs match the retained outputs. These computations audit arithmetic; the general conclusions rest on the written proofs, not graph enumeration or solver failures.

The main qualification concerns related work and attribution. The literature discussion misses several directly relevant papers published well before the submission's 72-hour concurrency window:

- Doria [9] proves the 16-vertex bound conditional on a published critical-graph census. Santos [10] gives a theoretical proof and, in Theorem 3, already identifies exactly the two order-18 shapes appearing here, with weaker edge intervals $74$–$79$ and $61$–$63$. Santos also isolates the 17-vertex configuration $K_2\vee H$, where $H$ is $K_7$-free, 8-critical, has 15 vertices, and has 58 or 59 edges. Patil [12] independently discusses closely related reductions and residual edge windows.
- The present Lemma 2 excludes that last 17-vertex configuration and answers the first question in Santos's Question 20 negatively. This is a concrete advance beyond the overlapping reductions. The acceptance recommendation rests principally on this additional argument and result; the 16-vertex exclusion and order-18 shapes should not be presented as newly established here.
- Szeider [11] proves that biplanar graphs with independence number at most two are 9-colorable. This does not subsume the present unrestricted 17-vertex theorem. It does provide a relevant additional restriction: any hypothetical ten-critical candidate must have an independent triple. Combined with this manuscript's lemma, it raises the first order-18 core's lower endpoint from 77 to 78. The existing interval is still a valid necessary condition. I examined the published argument and certification description, but did not rerun its SAT computations or Lean development.

Please update Section 2 to credit these antecedents and explain the precise improvement over [10], rather than leaving the distinction primarily against older nine-critical constructions. The manuscript's candid limitation on its literature search is helpful, but the directly comparable results can now be identified. The overlap concerns the starting reductions; the additional lemma and exclusion supply a meaningful contribution.

Two small improvements would sharpen the presentation. Make explicit that edges of $F[V(J)]$ omitted from the chosen critical subgraph $J$ only strengthen the lower bound in (8). Also replace `ceil(k*(2*k-1)/2)` in the arithmetic check with integer ceiling division: the current small inputs are computed correctly, but Python's `/` uses floating-point arithmetic, contrary to the blanket exact-arithmetic description.

The claims, limitations, proofs, and reproducibility information are otherwise clear, and the metadata abstract is informative. No additional large experiment is needed to support the stated theorem.

Additional references, continuing the manuscript's numbering:

[9] A. Doria. *Small Biplanar Graphs Are 9-Colorable: The Earth–Moon Problem up to 16 Vertices*. 6 August 2026. https://doi.org/10.5281/zenodo.21824308

[10] O. L. D. Santos. *Small-Order Bounds for the Earth–Moon Problem via Critical Graphs*, revised manuscript archived under *Biplanar Graphs on at Most Sixteen Vertices Are 9-Colorable*. 26 August 2026. Theorem 3 and Question 20. https://doi.org/10.5281/zenodo.22116325

[11] S. Szeider. *Biplanar graphs with independence number two are 9-colorable*. arXiv:2609.28102v1, 23 September 2026. https://arxiv.org/abs/2609.28102v1

[12] D. Patil. *The Earth–Moon problem: a certified corpus of nine-critical biplanar graphs, the exhaustion of the known χ = 10 candidates, and the status of χ₂*. 26 August 2026, Sections 4–5. https://doi.org/10.5281/zenodo.22103613
